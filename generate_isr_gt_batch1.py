# -*- coding: utf-8 -*-
"""
Batch 1: Grand Test MCQs ISR_GT_001 to ISR_GT_025
Key distribution: A: 7, B: 6, C: 6, D: 6 (Total: 25)
Difficulty: 15 Easy, 10 Medium
"""

from isr_gt_helper import make_q

def get_batch1():
    qs = []
    
    # 001 - Key A (Easy)
    qs.append(make_q(
        num=1, diff="Easy", qtype="Concept MCQ", subtopic="Inter-State Water Disputes",
        en_stem="Under Article 262(1) of the Indian Constitution, who is empowered to provide for the adjudication of any dispute with respect to the use, distribution, or control of waters of any inter-state river?",
        ta_stem="இந்திய அரசியலமைப்பின் சரத்து 262(1)-ன் கீழ், எந்தவொரு மாநிலங்களுக்கு இடையேயான நதிநீரின் பயன்பாடு, விநியோகம் அல்லது கட்டுப்பாடு தொடர்பான தகராறுகளைத் தீர்ப்பதற்கான சட்டத்தை இயற்ற அதிகாரம் பெற்றவர் யார்?",
        en_a="Parliament of India by law", ta_a="சட்டத்தின் மூலம் இந்திய பாராளுமன்றம்",
        en_b="President of India by executive decree", ta_b="செயல்முறை ஆணை மூலம் இந்தியக் குடியரசுத் தலைவர்",
        en_c="Supreme Court of India under original jurisdiction", ta_c="அசல் அதிகார வரம்பின் கீழ் இந்திய உச்ச நீதிமன்றம்",
        en_d="Inter-State Council by unanimous resolution", ta_d="ஒருமனதான தீர்மானத்தின் மூலம் மாநிலங்களுக்கு இடையேயான கவுன்சில்",
        correct_key="A",
        exp_en="Article 262(1) clearly provides: 'Parliament may by law provide for the adjudication of any dispute or complaint with respect to the use, distribution or control of the waters of, or in, any inter-State river or river valley.'",
        exp_ta="சரத்து 262(1) தெளிவாகக் கூறுகிறது: 'மாநிலங்களுக்கு இடையேயான எந்தவொரு நதி அல்லது நதிப் பள்ளத்தாக்கின் நீரைப் பயன்படுத்துதல், விநியோகித்தல் அல்லது கட்டுப்படுத்துதல் தொடர்பான எந்தவொரு தகராறையும் அல்லது புகாரையும் தீர்ப்பதற்கு பாராளுமன்றம் சட்டத்தின் மூலம் வழிவகை செய்யலாம்.'",
        why_a_en="Option A is correct as Parliament possesses legislative authority under Article 262(1).",
        why_a_ta="விருப்பம் A சரியானது, ஏனெனில் சரத்து 262(1)-ன் கீழ் பாராளுமன்றத்திற்கு மட்டுமே சட்டமன்ற அதிகாரம் உள்ளது.",
        why_b_en="Option B is incorrect; the President cannot establish river tribunals by executive decree alone.",
        why_b_ta="விருப்பம் B தவறானது; குடியரசுத் தலைவர் வெறும் நிர்வாக ஆணை மூலம் நதிநீர் தீர்ப்பாயங்களை அமைக்க முடியாது.",
        why_c_en="Option C is incorrect; Article 262 allows Parliament to exclude the jurisdiction of the Supreme Court.",
        why_c_ta="விருப்பம் C தவறானது; சரத்து 262 உச்ச நீதிமன்றத்தின் அதிகார வரம்பை விலக்கி வைக்க பாராளுமன்றத்திற்கு அதிகாரம் அளிக்கிறது.",
        why_d_en="Option D is incorrect; the Inter-State Council is an advisory body under Article 263.",
        why_d_ta="விருப்பம் D தவறானது; மாநிலங்களுக்கு இடையேயான கவுன்சில் சரத்து 263-ன் கீழ் ஒரு ஆலோசனை அமைப்பு மட்டுமே.",
        tip_en="Article 262 empowers Parliament, not the Supreme Court or President.",
        tip_ta="சரத்து 262 பாராளுமன்றத்திற்கு அதிகாரம் அளிக்கிறது, உச்ச நீதிமன்றத்திற்கோ அல்லது குடியரசுத் தலைவருக்கோ அல்ல.",
        fact_en="Parliament enacted the Inter-State River Water Disputes Act in 1956 under the powers conferred by Article 262.",
        fact_ta="சரத்து 262 வழங்கிய அதிகாரங்களின் கீழ் பாராளுமன்றம் 1956 இல் மாநிலங்களுக்கு இடையேயான நதிநீர் தகராறுகள் சட்டத்தை இயற்றியது."
    ))

    # 002 - Key B (Easy)
    qs.append(make_q(
        num=2, diff="Easy", qtype="Concept MCQ", subtopic="Inter-State Council",
        en_stem="Which constitutional article provides for the establishment of an Inter-State Council to effect coordination between states?",
        ta_stem="மாநிலங்களுக்கு இடையே ஒருங்கிணைப்பை ஏற்படுத்துவதற்காக மாநிலங்களுக்கு இடையேயான கவுன்சிலை நிறுவ வழிவகுக்கும் அரசியலமைப்புச் சரத்து எது?",
        en_a="Article 262", ta_a="சரத்து 262",
        en_b="Article 263", ta_b="சரத்து 263",
        en_c="Article 261", ta_c="சரத்து 261",
        en_d="Article 280", ta_d="சரத்து 280",
        correct_key="B",
        exp_en="Article 263 empowers the President to establish an Inter-State Council if at any time it appears to him that the public interests would be served by the establishment of such a council.",
        exp_ta="பொது நலன் கருதி தேவைப்படும் போது மாநிலங்களுக்கு இடையேயான கவுன்சிலை நிறுவ குடியரசுத் தலைவருக்கு சரத்து 263 அதிகாரம் அளிக்கிறது.",
        why_a_en="Option A deals with adjudication of inter-state water disputes, not the Inter-State Council.",
        why_a_ta="விருப்பம் A மாநிலங்களுக்கு இடையேயான நதிநீர் தகராறுகளுக்கானது, கவுன்சிலுக்கானது அல்ல.",
        why_b_en="Option B is correct; Article 263 pertains to the Inter-State Council.",
        why_b_ta="விருப்பம் B சரியானது; சரத்து 263 மாநிலங்களுக்கு இடையேயான கவுன்சிலைக் குறிக்கிறது.",
        why_c_en="Option C deals with Public Acts, records and judicial proceedings (Full Faith and Credit).",
        why_c_ta="விருப்பம் C பொதுச் சட்டங்கள், ஆவணங்கள் மற்றும் நீதிமுறை நடவடிக்கைகள் தொடர்பானது.",
        why_d_en="Option D deals with the Finance Commission.",
        why_d_ta="விருப்பம் D நிதி ஆணையம் தொடர்பானது.",
        tip_en="Remember: 261 = Full Faith & Credit, 262 = Water Disputes, 263 = Inter-State Council.",
        tip_ta="நினைவில் கொள்க: 261 = முழு மதிப்பு, 262 = நதிநீர் தகராறு, 263 = மாநிலங்களுக்கு இடையேயான கவுன்சில்.",
        fact_en="The Inter-State Council was first formally established on May 28, 1990 by a Presidential Order.",
        fact_ta="மாநிலங்களுக்கு இடையேயான கவுன்சில் மே 28, 1990 அன்று குடியரசுத் தலைவர் ஆணை மூலம் முதன்முதலில் நிறுவப்பட்டது."
    ))

    # 003 - Key C (Easy)
    qs.append(make_q(
        num=3, diff="Easy", qtype="Concept MCQ", subtopic="Zonal Councils and Reorganisation",
        en_stem="Who serves as the permanent Common Chairman of all the five statutory Zonal Councils in India?",
        ta_stem="இந்தியாவில் உள்ள ஐந்து சட்டப்பூர்வ மண்டல கவுன்சில்களுக்கும் நிரந்தர பொதுத் தலைவராகச் செயல்படுபவர் யார்?",
        en_a="Prime Minister of India", ta_a="இந்தியப் பிரதமர்",
        en_b="President of India", ta_b="இந்தியக் குடியரசுத் தலைவர்",
        en_c="Union Minister of Home Affairs", ta_c="மத்திய உள்துறை அமைச்சர்",
        en_d="Vice-President of India", ta_d="இந்தியத் துணைக் குடியரசுத் தலைவர்",
        correct_key="C",
        exp_en="Under Section 16(1) of the States Reorganisation Act, 1956, the Union Home Minister is nominated as the Chairman of each of the five Zonal Councils.",
        exp_ta="மாநில மறுசீரமைப்புச் சட்டம் 1956-ன் பிரிவு 16(1)-ன் படி, ஐந்து மண்டல கவுன்சில்கள் ஒவ்வொன்றிற்கும் மத்திய உள்துறை அமைச்சரே தலைவராக இருப்பார்.",
        why_a_en="Option A is incorrect; the Prime Minister chairs the Inter-State Council, not Zonal Councils.",
        why_a_ta="விருப்பம் A தவறானது; பிரதமர் மாநிலங்களுக்கு இடையேயான கவுன்சிலின் தலைவர் ஆவார், மண்டல கவுன்சில்களின் தலைவர் அல்ல.",
        why_b_en="Option B is incorrect; the President does not chair Zonal Councils.",
        why_b_ta="விருப்பம் B தவறானது; குடியரசுத் தலைவர் மண்டல கவுன்சில்களுக்கு தலைமை தாங்குவதில்லை.",
        why_c_en="Option C is correct; the Union Home Minister acts as the Chairman of all Zonal Councils.",
        why_c_ta="விருப்பம் C சரியானது; மத்திய உள்துறை அமைச்சர் அனைத்து மண்டல கவுன்சில்களுக்கும் தலைவராகச் செயல்படுகிறார்.",
        why_d_en="Option D is incorrect; the Vice-President is Chairman of Rajya Sabha.",
        why_d_ta="விருப்பம் D தவறானது; துணைக் குடியரசுத் தலைவர் மாநிலங்களவையின் தலைவர் ஆவார்.",
        tip_en="PM chairs Inter-State Council (Art 263); Home Minister chairs Zonal Councils (States Reorganisation Act).",
        tip_ta="பிரதமர் மாநிலங்களுக்கு இடையேயான கவுன்சிலின் தலைவர்; உள்துறை அமைச்சர் மண்டல கவுன்சில்களின் தலைவர்.",
        fact_en="The Chief Ministers of the member states in each zone act as Vice-Chairman of the Zonal Council by rotation for one year at a time.",
        fact_ta="ஒவ்வொரு மண்டலத்திலும் உள்ள உறுப்பு மாநிலங்களின் முதலமைச்சர்கள் சுழற்சி முறையில் தலா ஒரு வருடத்திற்கு துணைத் தலைவராகச் செயல்படுகின்றனர்."
    ))

    # 004 - Key D (Easy)
    qs.append(make_q(
        num=4, diff="Easy", qtype="Concept MCQ", subtopic="Inter-State Trade and Commerce",
        en_stem="Which Part of the Indian Constitution contains provisions concerning 'Trade, Commerce and Intercourse within the Territory of India' (Articles 301 to 307)?",
        ta_stem="இந்திய அரசியலமைப்பின் எந்தப் பகுதி 'இந்திய எல்லைக்குள் வர்த்தகம், வணிகம் மற்றும் உடனுறைவு' (சரத்துகள் 301 முதல் 307 வரை) தொடர்பான விதிகளைக் கொண்டுள்ளது?",
        en_a="Part XI", ta_a="பகுதி XI",
        en_b="Part XII", ta_b="பகுதி XII",
        en_c="Part XIV", ta_c="பகுதி XIV",
        en_d="Part XIII", ta_d="பகுதி XIII",
        correct_key="D",
        exp_en="Part XIII of the Indian Constitution encompasses Articles 301 to 307, establishing freedom of trade, commerce, and intercourse throughout the territory of India.",
        exp_ta="இந்திய அரசியலமைப்பின் பகுதி XIII சரத்துகள் 301 முதல் 307 வரை உள்ளடக்கியுள்ளது, இது இந்தியா முழுவதும் வர்த்தகம், வணிகம் மற்றும் உடனுறைவு சுதந்திரத்தை நிறுவுகிறது.",
        why_a_en="Option A contains Part XI, which deals with Relations between the Union and the States.",
        why_a_ta="விருப்பம் A பகுதி XI ஆகும், இது மத்திய-மாநில உறவுகளைக் கையாள்கிறது.",
        why_b_en="Option B contains Part XII, which deals with Finance, Property, Contracts and Suits.",
        why_b_ta="விருப்பம் B பகுதி XII ஆகும், இது நிதி, சொத்து, ஒப்பந்தங்கள் மற்றும் வழக்குகளைக் கையாள்கிறது.",
        why_c_en="Option C contains Part XIV, which deals with Services under the Union and the States.",
        why_c_ta="விருப்பம் C பகுதி XIV ஆகும், இது மத்திய மற்றும் மாநிலங்களின் கீழான அரசுப் பணிகளைக் கையாள்கிறது.",
        why_d_en="Option D is correct; Part XIII specifically governs Trade, Commerce and Intercourse.",
        why_d_ta="விருப்பம் D சரியானது; பகுதி XIII வர்த்தகம், வணிகம் மற்றும் உடனுறைவைக் கையாள்கிறது.",
        tip_en="Part XI = Relations (245-263); Part XII = Finance (264-300A); Part XIII = Trade & Commerce (301-307).",
        tip_ta="பகுதி XI = உறவுகள் (245-263); பகுதி XII = நிதி (264-300A); பகுதி XIII = வர்த்தகம் (301-307).",
        fact_en="Article 301 is inspired by Section 92 of the Australian Constitution, guaranteeing freedom of inter-state trade.",
        fact_ta="சரத்து 301 ஆஸ்திரேலிய அரசியலமைப்பின் பிரிவு 92-ன் தாக்கத்தால் உருவாக்கப்பட்டது, இது மாநிலங்களுக்கு இடையேயான வர்த்தக சுதந்திரத்தை உறுதி செய்கிறது."
    ))

    # 005 - Key A (Easy)
    qs.append(make_q(
        num=5, diff="Easy", qtype="Concept MCQ", subtopic="Public Acts, Records and Judicial Proceedings",
        en_stem="According to Article 261(1) of the Indian Constitution, full faith and credit shall be given throughout the territory of India to:",
        ta_stem="இந்திய அரசியலமைப்பின் சரத்து 261(1)-ன் படி, இந்தியா முழுவதும் எவற்றிற்கு முழு நம்பிக்கையும் மதிப்பும் அளிக்கப்பட வேண்டும்?",
        en_a="Public acts, records and judicial proceedings of the Union and of every State", ta_a="மத்திய அரசு மற்றும் ஒவ்வொரு மாநிலத்தின் பொதுச் சட்டங்கள், ஆவணங்கள் மற்றும் நீதிமுறை நடவடிக்கைகளுக்கு",
        en_b="Only the statutes enacted by the Parliament of India", ta_b="இந்திய பாராளுமன்றத்தால் இயற்றப்பட்ட சட்டங்களுக்கு மட்டுமே",
        en_c="Only judgments delivered by the Supreme Court of India", ta_c="இந்திய உச்ச நீதிமன்றத்தால் வழங்கப்படும் தீர்ப்புகளுக்கு மட்டுமே",
        en_d="Policy circulars issued by the Inter-State Council", ta_d="மாநிலங்களுக்கு இடையேயான கவுன்சில் வெளியிடும் கொள்கை சுற்றறிக்கைகளுக்கு",
        correct_key="A",
        exp_en="Article 261(1) states: 'Full faith and credit shall be given throughout the territory of India to public acts, records and judicial proceedings of the Union and of every State.'",
        exp_ta="சரத்து 261(1) கூறுகிறது: 'மத்திய அரசு மற்றும் ஒவ்வொரு மாநிலத்தின் பொதுச் சட்டங்கள், ஆவணங்கள் மற்றும் நீதிமுறை நடவடிக்கைகளுக்கு இந்தியா முழுவதும் முழு நம்பிக்கையும் மதிப்பும் அளிக்கப்பட வேண்டும்.'",
        why_a_en="Option A is the exact text of Article 261(1).",
        why_a_ta="விருப்பம் A என்பது சரத்து 261(1)-ன் நேரடி வாசகமாகும்.",
        why_b_en="Option B is too narrow; it applies to both Union and every State.",
        why_b_ta="விருப்பம் B மிகவும் குறுகியது; இது மத்திய மற்றும் ஒவ்வொரு மாநிலத்திற்கும் பொருந்தும்.",
        why_c_en="Option C is incorrect; it applies to all judicial proceedings of all courts across India.",
        why_c_ta="விருப்பம் C தவறானது; இது இந்தியா முழுவதும் உள்ள அனைத்து நீதிமன்றங்களின் நடவடிக்கைகளுக்கும் பொருந்தும்.",
        why_d_en="Option D is incorrect; Inter-State Council circulars are not covered by Article 261(1).",
        why_d_ta="விருப்பம் D தவறானது; கவுன்சில் சுற்றறிக்கைகள் சரத்து 261(1)-ன் கீழ் வரவில்லை.",
        tip_en="Article 261 establishes the 'Full Faith and Credit' clause across India.",
        tip_ta="சரத்து 261 இந்தியா முழுவதும் 'முழு நம்பிக்கை மற்றும் மதிப்பு' விதியை நிறுவுகிறது.",
        fact_en="Under Article 261(3), final civil judgments delivered by any court in India can be executed anywhere in the country.",
        fact_ta="சரத்து 261(3)-ன் கீழ், இந்தியாவில் உள்ள எந்த நீதிமன்றமும் வழங்கும் இறுதி சிவில் தீர்ப்புகள் நாட்டின் எந்தப் பகுதியிலும் நிறைவேற்றப்படலாம்."
    ))

    # 006 - Key B (Easy)
    qs.append(make_q(
        num=6, diff="Easy", qtype="Concept MCQ", subtopic="Inter-State Water Disputes",
        en_stem="Under Article 262(2) of the Indian Constitution, Parliament may by law provide that neither the Supreme Court nor any other court shall exercise jurisdiction in respect of:",
        ta_stem="இந்திய அரசியலமைப்பின் சரத்து 262(2)-ன் கீழ், உச்ச நீதிமன்றமோ அல்லது வேறு எந்த நீதிமன்றமோ எந்த விவகாரத்தில் அதிகார வரம்பைப் பயன்படுத்தக் கூடாது என்று பாராளுமன்றம் சட்டம் இயற்றலாம்?",
        en_a="Inter-state boundary disputes", ta_a="மாநிலங்களுக்கு இடையேயான எல்லைத் தகராறுகள்",
        en_b="Any dispute or complaint regarding inter-state river waters referred to an adjudication tribunal", ta_b="தீர்ப்பாயத்திற்கு அனுப்பப்பட்ட மாநிலங்களுக்கு இடையேயான நதிநீர் தொடர்பான தகராறு அல்லது புகார்",
        en_c="Disputes regarding fundamental rights violations across states", ta_c="மாநிலங்களுக்கிடையேயான அடிப்படை உரிமைகள் மீறல் தொடர்பான தகராறுகள்",
        en_d="Disputes regarding Presidential elections", ta_d="குடியரசுத் தலைவர் தேர்தல் தொடர்பான தகராறுகள்",
        correct_key="B",
        exp_en="Article 262(2) specifically allows Parliament to enact a law barring the Supreme Court or any other court from exercising jurisdiction over any inter-state water dispute referred to adjudication.",
        exp_ta="சரத்து 262(2) நதிநீர் தகராறுகளைத் தீர்ப்பதற்கான சட்டம் இயற்றும் போது, உச்ச நீதிமன்றம் அல்லது வேறு எந்த நீதிமன்றமும் அதில் தலையிடாதவாறு அதிகார வரம்பை நீக்க பாராளுமன்றத்திற்கு அதிகாரம் அளிக்கிறது.",
        why_a_en="Option A is incorrect; boundary disputes fall under Article 131 original jurisdiction of the Supreme Court.",
        why_a_ta="விருப்பம் A தவறானது; எல்லைத் தகராறுகள் சரத்து 131-ன் கீழ் உச்ச நீதிமன்றத்தின் அசல் அதிகார வரம்பிற்குள் வருகின்றன.",
        why_b_en="Option B is correct; Article 262(2) bars court jurisdiction in inter-state river disputes.",
        why_b_ta="விருப்பம் B சரியானது; சரத்து 262(2) நதிநீர் தகராறுகளில் நீதிமன்ற அதிகார வரம்பைத் தடுக்கிறது.",
        why_c_en="Option C is incorrect; fundamental rights jurisdiction cannot be barred under Article 32.",
        why_c_ta="விருப்பம் C தவறானது; சரத்து 32-ன் கீழான அடிப்படை உரிமை அதிகார வரம்பைத் தடுக்க முடியாது.",
        why_d_en="Option D is incorrect; presidential election disputes are exclusively decided by Supreme Court under Article 71.",
        why_d_ta="விருப்பம் D தவறானது; குடியரசுத் தலைவர் தேர்தல் தகராறுகளை சரத்து 71-ன் கீழ் உச்ச நீதிமன்றமே விசாரிக்கும்.",
        tip_en="Section 11 of the IRWD Act, 1956 bars the jurisdiction of the Supreme Court pursuant to Article 262(2).",
        tip_ta="சரத்து 262(2)-ஐப் பின்பற்றி 1956 IRWD சட்டத்தின் பிரிவு 11 உச்ச நீதிமன்றத்தின் தலையீட்டைத் தடுக்கிறது.",
        fact_en="Notwithstanding Section 11 of IRWD Act, the Supreme Court can still entertain Special Leave Petitions under Article 136.",
        fact_ta="IRWD சட்டத்தின் பிரிவு 11 இருந்தபோதிலும், சரத்து 136-ன் கீழ் சிறப்பு விடுப்பு மனுக்களை உச்ச நீதிமன்றம் விசாரிக்க முடியும்."
    ))

    # 007 - Key C (Easy)
    qs.append(make_q(
        num=7, diff="Easy", qtype="Concept MCQ", subtopic="Inter-State Council",
        en_stem="Who serves as the Chairman of the Inter-State Council established under Article 263?",
        ta_stem="சரத்து 263-ன் கீழ் நிறுவப்பட்ட மாநிலங்களுக்கு இடையேயான கவுன்சிலின் தலைவராகச் செயல்படுபவர் யார்?",
        en_a="President of India", ta_a="இந்தியக் குடியரசுத் தலைவர்",
        en_b="Union Minister of Home Affairs", ta_b="மத்திய உள்துறை அமைச்சர்",
        en_c="Prime Minister of India", ta_c="இந்தியப் பிரதமர்",
        en_d="Speaker of the Lok Sabha", ta_d="மக்களவை சபாநாயகர்",
        correct_key="C",
        exp_en="The Prime Minister of India is the Chairman of the Inter-State Council. The members include Chief Ministers of all states and UTs with legislative assemblies, Administrators of other UTs, and six Union Cabinet ministers.",
        exp_ta="இந்தியப் பிரதமர் மாநிலங்களுக்கு இடையேயான கவுன்சிலின் தலைவராக இருக்கிறார். அனைத்து மாநில மற்றும் யூனியன் பிரதேச முதலமைச்சர்கள், யூனியன் பிரதேச நிர்வாகிகள் மற்றும் 6 மத்திய அமைச்சரவை அமைச்சர்கள் இதில் உறுப்பினர்களாக உள்ளனர்.",
        why_a_en="Option A is incorrect; the President establishes the Council, but does not chair it.",
        why_a_ta="விருப்பம் A தவறானது; குடியரசுத் தலைவர் கவுன்சிலை நிறுவுகிறார், ஆனால் தலைமை தாங்குவதில்லை.",
        why_b_en="Option B is incorrect; Home Minister chairs the Standing Committee of ISC, while PM chairs the Council.",
        why_b_ta="விருப்பம் B தவறானது; உள்துறை அமைச்சர் கவுன்சிலின் நிலைக்குழுவிற்குத் தலைமை தாங்குகிறார், கவுன்சிலுக்கு பிரதமர் தலைமை தாங்குகிறார்.",
        why_c_en="Option C is correct; Prime Minister is the Chairman.",
        why_c_ta="விருப்பம் C சரியானது; இந்தியப் பிரதமரே தலைவர் ஆவார்.",
        why_d_en="Option D is incorrect; Speaker does not chair the Council.",
        why_d_ta="விருப்பம் D தவறானது; சபாநாயகர் கவுன்சிலுக்கு தலைமை தாங்குவதில்லை.",
        tip_en="ISC Chairman = Prime Minister; Standing Committee Chairman = Union Home Minister.",
        tip_ta="ISC தலைவர் = பிரதமர்; நிலைக்குழுத் தலைவர் = மத்திய உள்துறை அமைச்சர்.",
        fact_en="The Inter-State Council is recommended to meet at least thrice in a year, though meetings are held less frequently in practice.",
        fact_ta="மாநிலங்களுக்கு இடையேயான கவுன்சில் ஒரு ஆண்டில் குறைந்தது மூன்று முறையாவது கூட வேண்டும் என்று பரிந்துரைக்கப்பட்டுள்ளது."
    ))

    # 008 - Key D (Easy)
    qs.append(make_q(
        num=8, diff="Easy", qtype="Concept MCQ", subtopic="Zonal Councils and Reorganisation",
        en_stem="The five statutory Zonal Councils (Northern, Central, Eastern, Western, and Southern) were created under which of the following?",
        ta_stem="ஐந்து சட்டப்பூர்வ மண்டல கவுன்சில்கள் (வடக்கு, மத்திய, கிழக்கு, மேற்கு மற்றும் தெற்கு) பின்வருவனவற்றில் எதன் கீழ் உருவாக்கப்பட்டன?",
        en_a="Article 263 of the Indian Constitution", ta_a="இந்திய அரசியலமைப்பின் சரத்து 263",
        en_b="First Constitutional Amendment Act, 1951", ta_b="முதலாவது அரசியலமைப்பு திருத்தச் சட்டம், 1951",
        en_c="Government of India Resolution of 1950", ta_c="1950-ஆம் ஆண்டின் இந்திய அரசுத் தீர்மானம்",
        en_d="States Reorganisation Act, 1956", ta_d="மாநில மறுசீரமைப்புச் சட்டம், 1956",
        correct_key="D",
        exp_en="The five Zonal Councils are statutory bodies created by an Act of Parliament, namely the States Reorganisation Act, 1956 (Part III). They are not constitutional bodies.",
        exp_ta="ஐந்து மண்டல கவுன்சில்கள் பாராளுமன்றத்தின் சட்டமான மாநில மறுசீரமைப்புச் சட்டம் 1956-ன் (பகுதி III) கீழ் உருவாக்கப்பட்ட சட்டப்பூர்வ அமைப்புகள் ஆகும். அவை அரசியலமைப்பு அமைப்புகள் அல்ல.",
        why_a_en="Option A is incorrect; Article 263 created the Inter-State Council, which is a constitutional body.",
        why_a_ta="விருப்பம் A தவறானது; சரத்து 263 அரசியலமைப்பு அமைப்பான மாநிலங்களுக்கு இடையேயான கவுன்சிலை உருவாக்குகிறது.",
        why_b_en="Option B is incorrect; 1st Amendment did not create Zonal Councils.",
        why_b_ta="விருப்பம் B தவறானது; 1-வது திருத்தம் மண்டல கவுன்சில்களை உருவாக்கவில்லை.",
        why_c_en="Option C is incorrect; it is an executive resolution, whereas Zonal Councils are statutory.",
        why_c_ta="விருப்பம் C தவறானது; மண்டல கவுன்சில்கள் சட்டப்பூர்வமானவை.",
        why_d_en="Option D is correct; they were created under the States Reorganisation Act, 1956.",
        why_d_ta="விருப்பம் D சரியானது; அவை மாநில மறுசீரமைப்புச் சட்டம் 1956-ன் கீழ் உருவாக்கப்பட்டன.",
        tip_en="Zonal Councils = Statutory (1956 Act); Inter-State Council = Constitutional (Article 263).",
        tip_ta="மண்டல கவுன்சில்கள் = சட்டப்பூர்வமானவை (1956 சட்டம்); மாநிலங்களுக்கு இடையேயான கவுன்சில் = அரசியலமைப்பு சார்ந்தது (சரத்து 263).",
        fact_en="North Eastern Council was set up separately under the North Eastern Council Act, 1971.",
        fact_ta="வடகிழக்கு கவுன்சில் 1971-ஆம் ஆண்டின் வடகிழக்கு கவுன்சில் சட்டத்தின் கீழ் தனியாக அமைக்கப்பட்டது."
    ))

    # 009 - Key A (Easy)
    qs.append(make_q(
        num=9, diff="Easy", qtype="Concept MCQ", subtopic="Inter-State Trade and Commerce",
        en_stem="Article 301 of the Constitution of India guarantees freedom of trade, commerce and intercourse throughout the territory of India. This freedom is primarily subject to restrictions imposed under:",
        ta_stem="இந்திய அரசியலமைப்பின் சரத்து 301 இந்தியா முழுவதும் வர்த்தகம், வணிகம் மற்றும் உடனுறைவு சுதந்திரத்திற்கு உத்தரவாதம் அளிக்கிறது. இந்த சுதந்திரம் முதன்மையாக எதன் கீழ் விதிக்கப்படும் கட்டுப்பாடுகளுக்கு உட்பட்டது?",
        en_a="Articles 302 to 305 of Part XIII", ta_a="பகுதி XIII-ன் சரத்துகள் 302 முதல் 305 வரை",
        en_b="Article 19(2) reasonable restrictions only", ta_b="சரத்து 19(2)-ன் நியாயமான கட்டுப்பாடுகள் மட்டுமே",
        en_c="Article 352 emergency provisions exclusively", ta_c="சரத்து 352 அவசரகால விதிகள் மட்டுமே",
        en_d="Ordinances promulgated by State Governors under Article 213", ta_d="சரத்து 213-ன் கீழ் மாநில ஆளுநர்கள் பிறப்பிக்கும் அவசரச் சட்டங்கள்",
        correct_key="A",
        exp_en="Article 301 declares that trade, commerce and intercourse throughout India shall be free, 'subject to the other provisions of this Part' (namely Articles 302 to 305).",
        exp_ta="சரத்து 301, 'இப்பகுதியின் பிற விதிகளுக்கு உட்பட்டு' (அதாவது சரத்துகள் 302 முதல் 305 வரை) இந்தியா முழுவதும் வர்த்தகம், வணிகம் மற்றும் உடனுறைவு சுதந்திரமாக இருக்கும் என்று அறிவிக்கிறது.",
        why_a_en="Option A is correct as Articles 302 to 305 explicitly list the constitutional limitations on Article 301.",
        why_a_ta="விருப்பம் A சரியானது, ஏனெனில் சரத்துகள் 302 முதல் 305 வரை சரத்து 301 மீதான அரசியலமைப்பு கட்டுப்பாடுகளைக் குறிப்பிடுகின்றன.",
        why_b_en="Option B is incorrect; Article 19(1)(g) applies to citizens, whereas Article 301 is a general freedom of trade in Part XIII.",
        why_b_ta="விருப்பம் B தவறானது; சரத்து 19(1)(g) குடிமக்களுக்கு மட்டுமே உரியது, சரத்து 301 பகுதி XIII-ல் உள்ள பொது வர்த்தக சுதந்திரம்.",
        why_c_en="Option C is incorrect; Article 301 restrictions apply during peacetime as well.",
        why_c_ta="விருப்பம் C தவறானது; கட்டுப்பாடுகள் அமைதிக் காலத்திலும் பொருந்தும்.",
        why_d_en="Option D is incorrect; Governor cannot override Part XIII without Presidential instructions.",
        why_d_ta="விருப்பம் D தவறானது; குடியரசுத் தலைவரின் அறிவுறுத்தலின்றி ஆளுநர் பகுதி XIII-ஐ மீற முடியாது.",
        tip_en="Article 301 is qualified by Articles 302 (Parliament), 303 (Non-discrimination), and 304 (State restrictions).",
        tip_ta="சரத்து 301 என்பது சரத்து 302 (பாராளுமன்றம்), 303 (பாகுபாடின்மை), 304 (மாநிலக் கட்டுப்பாடுகள்) ஆகியவற்றிற்கு உட்பட்டது.",
        fact_en="Unlike Article 19(1)(g) which protects only citizens, Article 301 protects the overall movement of trade across state lines.",
        fact_ta="குடிமக்களுக்கு மட்டுமே உரிமையளிக்கும் சரத்து 19(1)(g) போலன்றி, சரத்து 301 எல்லைகளைக் கடந்து நடக்கும் ஒட்டுமொத்த வர்த்தக நகர்வைப் பாதுகாக்கிறது."
    ))

    # 010 - Key B (Easy)
    qs.append(make_q(
        num=10, diff="Easy", qtype="Concept MCQ", subtopic="Inter-State Water Disputes",
        en_stem="Which of the following River Water Disputes Tribunals was constituted to adjudicate water sharing disputes involving Tamil Nadu, Karnataka, Kerala, and Puducherry?",
        ta_stem="தமிழ்நாடு, கர்நாடகா, கேரளா மற்றும் புதுச்சேரி ஆகியவற்றை உள்ளடக்கிய நதிநீர் பகிர்வு தகராறுகளைத் தீர்ப்பதற்காக அமைக்கப்பட்ட நதிநீர் தகராறு தீர்ப்பாயம் எது?",
        en_a="Krishna Water Disputes Tribunal", ta_a="கிருஷ்ணா நதிநீர் தகராறு தீர்ப்பாயம்",
        en_b="Cauvery Water Disputes Tribunal", ta_b="காவிரி நதிநீர் தகராறு தீர்ப்பாயம்",
        en_c="Godavari Water Disputes Tribunal", ta_c="கோதாவரி நதிநீர் தகராறு தீர்ப்பாயம்",
        en_d="Narmada Water Disputes Tribunal", ta_d="நர்மதா நதிநீர் தகராறு தீர்ப்பாயம்",
        correct_key="B",
        exp_en="The Cauvery Water Disputes Tribunal (CWDT) was constituted in June 1990 to resolve water sharing disputes among the basin states/UTs: Tamil Nadu, Karnataka, Kerala, and Puducherry.",
        exp_ta="காவிரி நதிநீர் தகராறு தீர்ப்பாயம் (CWDT) ஜூன் 1990 இல் வடிநில மாநிலங்கள் மற்றும் யூனியன் பிரதேசங்களான தமிழ்நாடு, கர்நாடகா, கேரளா மற்றும் புதுச்சேரி இடையேயான தகராறுகளைத் தீர்க்க அமைக்கப்பட்டது.",
        why_a_en="Option A involves Maharashtra, Karnataka, Andhra Pradesh, and Telangana.",
        why_a_ta="விருப்பம் A மகாராஷ்டிரா, கர்நாடகா, ஆந்திரா மற்றும் தெலுங்கானாவை உள்ளடக்கியது.",
        why_b_en="Option B is correct; Cauvery involves TN, Karnataka, Kerala, and Puducherry.",
        why_b_ta="விருப்பம் B சரியானது; காவிரி தகராறு தமிழ்நாடு, கர்நாடகா, கேரளா மற்றும் புதுச்சேரியை உள்ளடக்கியது.",
        why_c_en="Option C involves Maharashtra, Andhra Pradesh, Madhya Pradesh, Chhattisgarh, Odisha, and Karnataka.",
        why_c_ta="விருப்பம் C மகாராஷ்டிரா, ஆந்திரா, மத்தியப் பிரதேசம், ஒடிசா போன்றவற்றை உள்ளடக்கியது.",
        why_d_en="Option D involves Madhya Pradesh, Gujarat, Maharashtra, and Rajasthan.",
        why_d_ta="விருப்பம் D மத்தியப் பிரதேசம், குஜராத், மகாராஷ்டிரா மற்றும் ராஜஸ்தானை உள்ளடக்கியது.",
        tip_en="Cauvery = 4 entities: 3 States (TN, KA, KL) + 1 UT (Puducherry).",
        tip_ta="காவிரி = 4 பகுதிகள்: 3 மாநிலங்கள் (தமிழ்நாடு, கர்நாடகா, கேரளா) + 1 யூ.பி (புதுச்சேரி).",
        fact_en="The CWDT was headed by Justice Chittatosh Mookerjee and gave its final award on February 5, 2007.",
        fact_ta="CWDT-க்கு நீதிபதி சித்ததோஷ் முகர்ஜி தலைமை தாங்கினார், பிப்ரவரி 5, 2007 அன்று இறுதித் தீர்ப்பை வழங்கியது."
    ))

    # 011 - Key C (Easy)
    qs.append(make_q(
        num=11, diff="Easy", qtype="Concept MCQ", subtopic="Commissions and Inter-State Relations",
        en_stem="The Commission on Centre-State Relations headed by Justice R.S. Sarkaria submitted its landmark report in which year?",
        ta_stem="நீதிபதி ஆர்.எஸ். சர்க்காரியா தலைமையிலான மத்திய-மாநில உறவுகள் குறித்த ஆணையம் தனது வரலாற்றுச் சிறப்புமிக்க அறிக்கையை எந்த ஆண்டு சமர்ப்பித்தது?",
        en_a="1983", ta_a="1983",
        en_b="1971", ta_b="1971",
        en_c="1988", ta_c="1988",
        en_d="2002", ta_d="2002",
        correct_key="C",
        exp_en="The Sarkaria Commission was appointed in June 1983 and submitted its final comprehensive report to Prime Minister Rajiv Gandhi in January 1988.",
        exp_ta="சர்க்காரியா ஆணையம் ஜூன் 1983 இல் நியமிக்கப்பட்டு, ஜனவரி 1988 இல் பிரதமர் ராஜீவ் காந்தியிடம் தனது விரிவான அறிக்கையை சமர்ப்பித்தது.",
        why_a_en="Option A is the year the Sarkaria Commission was appointed, not when it submitted its report.",
        why_a_ta="விருப்பம் A ஆணையம் நியமிக்கப்பட்ட ஆண்டு, அறிக்கை சமர்ப்பிக்கப்பட்ட ஆண்டு அல்ல.",
        why_b_en="Option B is the year the Rajamannar Committee report was submitted.",
        why_b_ta="விருப்பம் B ராஜமன்னார் குழு அறிக்கை சமர்ப்பிக்கப்பட்ட ஆண்டு.",
        why_c_en="Option C is correct; the report was submitted in 1988.",
        why_c_ta="விருப்பம் C சரியானது; அறிக்கை 1988 இல் சமர்ப்பிக்கப்பட்டது.",
        why_d_en="Option D is the year the NCRWC (Venkatachaliah Commission) report was submitted.",
        why_d_ta="விருப்பம் D வெங்கடாசலையா ஆணைய அறிக்கை சமர்ப்பிக்கப்பட்ட ஆண்டு.",
        tip_en="Sarkaria Commission: Appointed 1983, Submitted 1988. Rajamannar: Appointed 1969, Submitted 1971.",
        tip_ta="சர்க்காரியா ஆணையம்: நியமனம் 1983, அறிக்கை 1988. ராஜமன்னார்: நியமனம் 1969, அறிக்கை 1971.",
        fact_en="The Sarkaria Commission made 247 recommendations, including the formal establishment of a permanent Inter-State Council under Article 263.",
        fact_ta="சர்க்காரியா ஆணையம் சரத்து 263-ன் கீழ் நிரந்தர மாநிலங்களுக்கு இடையேயான கவுன்சிலை அமைப்பது உட்பட 247 பரிந்துரைகளை வழங்கியது."
    ))

    # 012 - Key D (Easy)
    qs.append(make_q(
        num=12, diff="Easy", qtype="Concept MCQ", subtopic="Zonal Councils and Reorganisation",
        en_stem="Which state is included in the Southern Zonal Council along with Andhra Pradesh, Karnataka, Kerala, Tamil Nadu, and Puducherry?",
        ta_stem="ஆந்திரப் பிரதேசம், கர்நாடகா, கேரளா, தமிழ்நாடு மற்றும் புதுச்சேரியுடன் தெற்கு மண்டல கவுன்சிலில் சேர்க்கப்பட்டுள்ள மற்றொரு மாநிலம் எது?",
        en_a="Odisha", ta_a="ஒடிசா",
        en_b="Maharashtra", ta_b="மகாராஷ்டிரா",
        en_c="Goa", ta_c="கோவா",
        en_d="Telangana", ta_d="தெலுங்கானா",
        correct_key="D",
        exp_en="The Southern Zonal Council comprises Andhra Pradesh, Karnataka, Kerala, Tamil Nadu, Telangana, and the Union Territory of Puducherry.",
        exp_ta="தெற்கு மண்டல கவுன்சிலில் ஆந்திரப் பிரதேசம், கர்நாடகா, கேரளா, தமிழ்நாடு, தெலுங்கானா மற்றும் புதுச்சேரி யூனியன் பிரதேசம் ஆகியவை அடங்கும்.",
        why_a_en="Option A is in the Eastern Zonal Council.",
        why_a_ta="விருப்பம் A கிழக்கு மண்டல கவுன்சிலில் உள்ளது.",
        why_b_en="Option B is in the Western Zonal Council.",
        why_b_ta="விருப்பம் B மேற்கு மண்டல கவுன்சிலில் உள்ளது.",
        why_c_en="Option C is in the Western Zonal Council.",
        why_c_ta="விருப்பம் C மேற்கு மண்டல கவுன்சிலில் உள்ளது.",
        why_d_en="Option D is correct; Telangana was added to the Southern Zonal Council upon bifurcation in 2014.",
        why_d_ta="விருப்பம் D சரியானது; தெலுங்கானா 2014 இல் உருவாக்கப்பட்ட பின்னர் தெற்கு மண்டல கவுன்சிலில் சேர்க்கப்பட்டது.",
        tip_en="Southern Zone = AP, KA, KL, TN, TS + Puducherry.",
        tip_ta="தெற்கு மண்டலம் = ஆந்திரா, கர்நாடகா, கேரளா, தமிழ்நாடு, தெலுங்கானா + புதுச்சேரி.",
        fact_en="The Andaman and Nicobar Islands and Lakshadweep are not members of any Zonal Council but are special invitees.",
        fact_ta="அந்தமான் நிக்கோபார் தீவுகள் மற்றும் லட்சத்தீவுகள் எந்த மண்டல கவுன்சிலிலும் உறுப்பினர்களாக இல்லை, ஆனால் சிறப்பு அழைப்பாளர்களாக உள்ளனர்."
    ))

    # 013 - Key A (Easy)
    qs.append(make_q(
        num=13, diff="Easy", qtype="Concept MCQ", subtopic="Inter-State Trade and Commerce",
        en_stem="Under Article 302 of the Constitution, who is empowered to impose restrictions on the freedom of trade, commerce or intercourse between states in the public interest?",
        ta_stem="அரசியலமைப்பின் சரத்து 302-ன் கீழ், பொது நலன் கருதி மாநிலங்களுக்கு இடையேயான வர்த்தகம், வணிகம் அல்லது உடனுறைவு சுதந்திரத்தின் மீது கட்டுப்பாடுகளை விதிக்க அதிகாரம் பெற்றவர் யார்?",
        en_a="Parliament by law", ta_a="சட்டத்தின் மூலம் பாராளுமன்றம்",
        en_b="State Legislature by resolution", ta_b="தீர்மானத்தின் மூலம் மாநில சட்டமன்றம்",
        en_c="President by executive order", ta_c="நிர்வாக ஆணை மூலம் குடியரசுத் தலைவர்",
        en_d="Inter-State Trade Commission", ta_d="மாநிலங்களுக்கு இடையேயான வர்த்தக ஆணையம்",
        correct_key="A",
        exp_en="Article 302 states: 'Parliament may by law impose such restrictions on the freedom of trade, commerce or intercourse between one State and another or within any part of the territory of India as may be required in the public interest.'",
        exp_ta="சரத்து 302 கூறுகிறது: 'பொது நலன் கருதி தேவைப்படும் போது, ஒரு மாநிலத்திற்கும் மற்றொரு மாநிலத்திற்கும் இடையே அல்லது இந்திய எல்லைக்குள் வர்த்தக சுதந்திரத்தின் மீது பாராளுமன்றம் சட்டத்தின் மூலம் கட்டுப்பாடுகளை விதிக்கலாம்.'",
        why_a_en="Option A is correct; Parliament alone has power under Article 302.",
        why_a_ta="விருப்பம் A சரியானது; சரத்து 302-ன் கீழ் பாராளுமன்றத்திற்கு மட்டுமே அதிகாரம் உண்டு.",
        why_b_en="Option B is incorrect; State Legislature's power to restrict trade falls under Article 304(b).",
        why_b_ta="விருப்பம் B தவறானது; மாநில சட்டமன்றத்தின் வர்த்தக கட்டுப்பாட்டு அதிகாரம் சரத்து 304(b)-ன் கீழ் வருகிறது.",
        why_c_en="Option C is incorrect; executive orders cannot impose restrictions under Article 302.",
        why_c_ta="விருப்பம் C தவறானது; நிர்வாக ஆணைகள் மூலம் கட்டுப்பாடுகளை விதிக்க முடியாது.",
        why_d_en="Option D is incorrect; no such permanent authority exists under Article 307.",
        why_d_ta="விருப்பம் D தவறானது; சரத்து 307-ன் கீழ் அத்தகைய நிரந்தர அமைப்பு அமைக்கப்படவில்லை.",
        tip_en="Article 302 = Parliament can restrict trade in public interest. Article 304(b) = State can restrict with President's previous sanction.",
        tip_ta="சரத்து 302 = பாராளுமன்றம் பொது நலனுக்காக வர்த்தகத்தை கட்டுப்படுத்தலாம். சரத்து 304(b) = குடியரசுத் தலைவர் அனுமதியுடன் மாநிலம் கட்டுப்படுத்தலாம்.",
        fact_en="Parliament's power under Article 302 is limited by Article 303(1), which prohibits preference or discrimination between states, except during scarcity of goods (Art 303(2)).",
        fact_ta="பண்டங்களின் தட்டுப்பாடு ஏற்படும் போது தவிர (சரத்து 303(2)), மாநிலங்களுக்கிடையே பாகுபாடு காட்டுவதை சரத்து 303(1) தடை செய்கிறது."
    ))

    # 014 - Key B (Easy)
    qs.append(make_q(
        num=14, diff="Easy", qtype="Concept MCQ", subtopic="Inter-State Council",
        en_stem="How many Union Cabinet Ministers are nominated by the Prime Minister as members of the Inter-State Council?",
        ta_stem="மாநிலங்களுக்கு இடையேயான கவுன்சிலின் உறுப்பினர்களாக பிரதமரால் எத்தனை மத்திய அமைச்சரவை அமைச்சர்கள் பரிந்துரைக்கப்படுகிறார்கள்?",
        en_a="Four", ta_a="நான்கு",
        en_b="Six", ta_b="ஆறு",
        en_c="Ten", ta_c="பத்து",
        en_d="Twelve", ta_d="பன்னிரண்டு",
        correct_key="B",
        exp_en="The composition of the Inter-State Council includes six Union Cabinet Ministers nominated by the Prime Minister (including the Home Minister).",
        exp_ta="மாநிலங்களுக்கு இடையேயான கவுன்சிலில் பிரதமரால் பரிந்துரைக்கப்படும் ஆறு மத்திய அமைச்சரவை அமைச்சர்கள் (உள்துறை அமைச்சர் உட்பட) உறுப்பினர்களாக உள்ளனர்.",
        why_a_en="Option A is incorrect; the number is six.",
        why_a_ta="விருப்பம் A தவறானது; எண்ணிக்கை ஆறு ஆகும்.",
        why_b_en="Option B is correct; exactly six Cabinet ministers are nominated.",
        why_b_ta="விருப்பம் B சரியானது; சரியாக ஆறு அமைச்சரவை அமைச்சர்கள் நியமிக்கப்படுகிறார்கள்.",
        why_c_en="Option C is incorrect; ten ministers are not in the core composition.",
        why_c_ta="விருப்பம் C தவறானது; பத்து அமைச்சர்கள் அல்ல.",
        why_d_en="Option D is incorrect.",
        why_d_ta="விருப்பம் D தவறானது.",
        tip_en="ISC composition: PM (Chairman) + CMs of all States & UTs with assemblies + UT administrators + 6 Union Cabinet Ministers.",
        tip_ta="ISC கட்டமைப்பு: பிரதமர் (தலைவர்) + அனைத்து மாநில/யூனியன் பிரதேச முதலமைச்சர்கள் + யூனியன் பிரதேச நிர்வாகிகள் + 6 மத்திய அமைச்சர்கள்.",
        fact_en="Ministers of State with independent charge can also be nominated as permanent invitees by the Prime Minister.",
        fact_ta="தனிப்பொறுப்பு வகிக்கும் இணை அமைச்சர்களும் பிரதமரால் நிரந்தர அழைப்பாளர்களாக நியமிக்கப்படலாம்."
    ))

    # 015 - Key C (Easy)
    qs.append(make_q(
        num=15, diff="Easy", qtype="Concept MCQ", subtopic="Inter-State Water Disputes",
        en_stem="Under Section 4 of the Inter-State River Water Disputes Act, 1956, a river water dispute tribunal is constituted by:",
        ta_stem="1956-ஆம் ஆண்டின் மாநிலங்களுக்கு இடையேயான நதிநீர் தகராறுகள் சட்டத்தின் பிரிவு 4-ன் கீழ், நதிநீர் தகராறு தீர்ப்பாயம் யாரால் அமைக்கப்படுகிறது?",
        en_a="Supreme Court of India", ta_a="இந்திய உச்ச நீதிமன்றம்",
        en_b="President of India", ta_b="இந்தியக் குடியரசுத் தலைவர்",
        en_c="Central Government", ta_c="மத்திய அரசு",
        en_d="National Water Resources Council", ta_d="தேசிய நீர் வள கவுன்சில்",
        correct_key="C",
        exp_en="Under Section 4(1) of the IRWD Act, 1956, if the Central Government is of opinion that the water dispute cannot be settled by negotiations, it shall, by notification in the Official Gazette, constitute a Water Disputes Tribunal.",
        exp_ta="IRWD சட்டம் 1956 பிரிவு 4(1)-ன் படி, பேச்சுவார்த்தைகள் மூலம் தகராறைத் தீர்க்க முடியாது என்று மத்திய அரசு கருதினால், அது அரசிதழில் அறிவிக்கை வெளியிட்டு நதிநீர் தீர்ப்பாயத்தை அமைக்கும்.",
        why_a_en="Option A is incorrect; Supreme Court does not constitute the tribunal.",
        why_a_ta="விருப்பம் A தவறானது; உச்ச நீதிமன்றம் தீர்ப்பாயத்தை அமைப்பதில்லை.",
        why_b_en="Option B is incorrect; the statute specifies Central Government, not the President.",
        why_b_ta="விருப்பம் B தவறானது; சட்டம் மத்திய அரசை குறிப்பிடுகிறது, குடியரசுத் தலைவரை அல்ல.",
        why_c_en="Option C is correct; the Central Government constitutes the tribunal.",
        why_c_ta="விருப்பம் C சரியானது; மத்திய அரசே தீர்ப்பாயத்தை அமைக்கிறது.",
        why_d_en="Option D is incorrect; NWRC is a policy body.",
        why_d_ta="விருப்பம் D தவறானது; NWRC என்பது ஒரு கொள்கை அமைப்பு மட்டுமே.",
        tip_en="Central Government constitutes the tribunal, but the members (judges) are nominated by the Chief Justice of India.",
        tip_ta="மத்திய அரசு தீர்ப்பாயத்தை அமைக்கிறது, ஆனால் அதன் உறுப்பினர்களை (நீதிபதிகளை) இந்திய தலைமை நீதிபதி பரிந்துரைக்கிறார்.",
        fact_en="Section 4(2) mandates that the tribunal shall consist of a Chairman and two other members nominated by the CJI from sitting Supreme Court or High Court judges.",
        fact_ta="பிரிவு 4(2)-ன் படி தலைமை நீதிபதியால் பரிந்துரைக்கப்படும் ஒரு தலைவர் மற்றும் இரண்டு நீதிபதிகள் தீர்ப்பாயத்தில் இடம்பெறுவர்."
    ))

    # 016 - Key D (Medium)
    qs.append(make_q(
        num=16, diff="Medium", qtype="Concept MCQ", subtopic="Inter-State Trade and Commerce",
        en_stem="Under Article 304(b) of the Constitution, a State Legislature may impose reasonable restrictions on trade and commerce with other states, provided that:",
        ta_stem="அரசியலமைப்பின் சரத்து 304(b)-ன் கீழ், ஒரு மாநில சட்டமன்றம் பிற மாநிலங்களுடனான வர்த்தகம் மற்றும் வணிகத்தின் மீது நியாயமான கட்டுப்பாடுகளை விதிக்கலாம், ஆனால் அதற்குரிய நிபந்தனை என்ன?",
        en_a="The Inter-State Council approves the bill by a two-thirds majority", ta_a="மாநிலங்களுக்கு இடையேயான கவுன்சில் மூன்றில் இரண்டு பங்கு பெரும்பான்மையுடன் மசோதாவை அங்கீகரிக்க வேண்டும்",
        en_b="The High Court of the State issues an advisory clearance", ta_b="மாநில உயர் நீதிமன்றம் ஆலோசனை ஒப்புதல் வழங்க வேண்டும்",
        en_c="The Rajya Sabha passes a special resolution under Article 249", ta_c="மாநிலங்களவை சரத்து 249-ன் கீழ் சிறப்புத் தீர்மானம் நிறைவேற்ற வேண்டும்",
        en_d="No Bill for this purpose shall be introduced without the previous sanction of the President", ta_d="குடியரசுத் தலைவரின் முன் அனுமதியின்றி இதற்கான எந்தவொரு மசோதாவும் சட்டமன்றத்தில் அறிமுகப்படுத்தப்படக் கூடாது",
        correct_key="D",
        exp_en="The Proviso to Article 304(b) explicitly mandates: 'Provided that no Bill or amendment for the purposes of clause (b) shall be introduced or moved in the Legislature of a State without the previous sanction of the President.'",
        exp_ta="சரத்து 304(b)-ன் வரம்புரை தெளிவாகக் கூறுகிறது: 'குடியரசுத் தலைவரின் முன் அனுமதியின்றி பிரிவு (b)-ன் நோக்கங்களுக்காக எந்தவொரு மசோதாவோ அல்லது திருத்தமோ ஒரு மாநில சட்டமன்றத்தில் அறிமுகப்படுத்தப்படவோ அல்லது கொண்டுவரப்படவோ கூடாது.'",
        why_a_en="Option A is incorrect; Inter-State Council approval is not required.",
        why_a_ta="விருப்பம் A தவறானது; கவுன்சில் ஒப்புதல் தேவையில்லை.",
        why_b_en="Option B is incorrect; High Courts have no role in pre-legislative clearance.",
        why_b_ta="விருப்பம் B தவறானது; உயர் நீதிமன்றங்களுக்கு இதில் பங்கு இல்லை.",
        why_c_en="Option C is incorrect; Article 249 deals with national interest legislation on State List.",
        why_c_ta="விருப்பம் C தவறானது; சரத்து 249 மாநிலப் பட்டியல் தொடர்பானது.",
        why_d_en="Option D is correct; previous sanction of the President is mandatory under Article 304(b) proviso.",
        why_d_ta="விருப்பம் D சரியானது; சரத்து 304(b) வரம்புரையின் கீழ் குடியரசுத் தலைவரின் முன் அனுமதி கட்டாயமாகும்.",
        tip_en="Article 304(b) proviso = Previous sanction of the President required to introduce the bill in State Assembly.",
        tip_ta="சரத்து 304(b) வரம்புரை = மாநில சட்டமன்றத்தில் மசோதாவை அறிமுகப்படுத்த குடியரசுத் தலைவரின் முன் அனுமதி தேவை.",
        fact_en="Under Article 255, if an Act received subsequent assent of the President, the absence of previous sanction is cured.",
        fact_ta="சரத்து 255-ன் படி, பின்னர் குடியரசுத் தலைவரின் ஒப்புதல் பெறப்பட்டால், முன் அனுமதி பெறாத குறைபாடு நீக்கப்படும்."
    ))

    # 017 - Key A (Medium)
    qs.append(make_q(
        num=17, diff="Medium", qtype="Concept MCQ", subtopic="Inter-State Council",
        en_stem="The Standing Committee of the Inter-State Council was set up in 1996 for continuous consultation. Who is the Chairman of this Standing Committee?",
        ta_stem="தொடர்ச்சியான ஆலோசனைக்காக 1996 இல் அமைக்கப்பட்ட மாநிலங்களுக்கு இடையேயான கவுன்சிலின் நிலைக்குழுவின் தலைவர் யார்?",
        en_a="Union Minister of Home Affairs", ta_a="மத்திய உள்துறை அமைச்சர்",
        en_b="Prime Minister of India", ta_b="இந்தியப் பிரதமர்",
        en_c="Cabinet Secretary", ta_c="மத்திய அமைச்சரவைச் செயலாளர்",
        en_d="Senior-most Chief Minister by rotation", ta_d="சுழற்சி முறையிலான மூத்த முதலமைச்சர்",
        correct_key="A",
        exp_en="The Standing Committee of the Inter-State Council was constituted in 1996 and is chaired by the Union Home Minister. It consists of 5 Union Cabinet Ministers and 9 Chief Ministers.",
        exp_ta="மாநிலங்களுக்கு இடையேயான கவுன்சிலின் நிலைக்குழு 1996 இல் அமைக்கப்பட்டது, இதற்கு மத்திய உள்துறை அமைச்சர் தலைமை தாங்குகிறார். இதில் 5 மத்திய அமைச்சரவை அமைச்சர்களும் 9 முதலமைச்சர்களும் உள்ளனர்.",
        why_a_en="Option A is correct; Union Home Minister chairs the Standing Committee.",
        why_a_ta="விருப்பம் A சரியானது; மத்திய உள்துறை அமைச்சர் நிலைக்குழுவின் தலைவர் ஆவார்.",
        why_b_en="Option B is incorrect; PM chairs the full Inter-State Council, not the Standing Committee.",
        why_b_ta="விருப்பம் B தவறானது; பிரதமர் முழு கவுன்சிலின் தலைவர் ஆவார், நிலைக்குழுவின் தலைவர் அல்ல.",
        why_c_en="Option C is incorrect; Cabinet Secretary heads the civil services, not this ministerial committee.",
        why_c_ta="விருப்பம் C தவறானது; அமைச்சரவைச் செயலாளர் இதற்கு தலைமை தாங்குவதில்லை.",
        why_d_en="Option D is incorrect; Chief Ministers are members, not the Chairman.",
        why_d_ta="விருப்பம் D தவறானது; முதலமைச்சர்கள் உறுப்பினர்கள் மட்டுமே.",
        tip_en="Standing Committee = Chaired by Home Minister; Full Council = Chaired by Prime Minister.",
        tip_ta="நிலைக்குழு = உள்துறை அமைச்சர் தலைமை; முழு கவுன்சில் = பிரதமர் தலைமை.",
        fact_en="The Standing Committee processes and examines matters before they are placed before the full Inter-State Council.",
        fact_ta="முழு கவுன்சிலின் முன் வைக்கப்படுவதற்கு முன்பு விவகாரங்களை ஆய்வு செய்து தயாரிக்கும் பணியை நிலைக்குழு மேற்கொள்கிறது."
    ))

    # 018 - Key B (Medium)
    qs.append(make_q(
        num=18, diff="Medium", qtype="Concept MCQ", subtopic="Public Acts, Records and Judicial Proceedings",
        en_stem="Article 261(3) of the Indian Constitution gives extraterritorial validity to final judgments and orders of civil courts across India. Which category of judgments is EXCLUDED from this clause?",
        ta_stem="இந்திய அரசியலமைப்பின் சரத்து 261(3) இந்தியா முழுவதும் உள்ள உரிமையியல் நீதிமன்றங்களின் இறுதித் தீர்ப்புகளுக்கு நாடு தழுவிய செல்லுபடியாகும் தன்மையை அளிக்கிறது. இதில் எந்த வகை தீர்ப்புகள் விலக்கப்பட்டுள்ளன?",
        en_a="Civil money decrees", ta_a="பணம் மீட்பதற்கான சிவில் தீர்ப்புகள்",
        en_b="Penal and criminal court judgments", ta_b="குற்றவியல் மற்றும் தண்டனை நீதிமன்றத் தீர்ப்புகள்",
        en_c="Partition suits between family members", ta_c="குடும்ப உறுப்பினர்களுக்கு இடையேயான பாகப்பிரிவினை வழக்குகள்",
        en_d="Specific performance of contract decrees", ta_d="ஒப்பந்தத்தை நிறைவேற்றக் கோரும் சிவில் தீர்ப்புகள்",
        correct_key="B",
        exp_en="Article 261(3) states: 'Final judgments or orders delivered or passed by civil courts in any part of the territory of India shall be capable of execution anywhere within that territory according to law.' It applies only to civil courts; penal laws and criminal judgments are excluded under the general principle of private international law.",
        exp_ta="சரத்து 261(3) உரிமையியல் (சிவில்) நீதிமன்றங்களின் இறுதித் தீர்ப்புகளுக்கு மட்டுமே பொருந்தும் என்று தெளிவாகக் கூறுகிறது. குற்றவியல் நீதிமன்றத் தீர்ப்புகளுக்கு இது பொருந்தாது.",
        why_a_en="Option A is included as it is a civil court decree.",
        why_a_ta="விருப்பம் A என்பது சிவில் தீர்ப்பு என்பதால் இதில் அடங்கும்.",
        why_b_en="Option B is correct; criminal and penal judgments are excluded from Article 261(3).",
        why_b_ta="விருப்பம் B சரியானது; குற்றவியல் தீர்ப்புகள் சரத்து 261(3)-லிருந்து விலக்கப்பட்டுள்ளன.",
        why_c_en="Option C is a civil decree and is enforceable anywhere in India.",
        why_c_ta="விருப்பம் C என்பது சிவில் தீர்ப்பு என்பதால் நிறைவேற்றப்படலாம்.",
        why_d_en="Option D is a civil decree and is enforceable.",
        why_d_ta="விருப்பம் D சிவில் தீர்ப்பு என்பதால் நிறைவேற்றப்படலாம்.",
        tip_en="Article 261(3) specifically mentions 'civil courts'. Criminal judgments require extradition / CrPC procedures.",
        tip_ta="சரத்து 261(3) குறிப்பாக 'சிவில் நீதிமன்றங்களை' மட்டுமே குறிப்பிடுகிறது. குற்றவியல் தீர்ப்புகளுக்கு குற்றவியல் நடைமுறைச் சட்டம் பொருந்தும்.",
        fact_en="Under the Code of Civil Procedure (Section 38 and 39), a decree passed by a civil court in one state can be sent to a court in another state for execution.",
        fact_ta="உரிமையியல் நடைமுறைச் சட்டத்தின் கீழ் (பிரிவு 38 மற்றும் 39), ஒரு மாநில நீதிமன்றம் பிறப்பித்த தீர்ப்பை மற்றொரு மாநில நீதிமன்றத்திற்கு அனுப்பி நிறைவேற்ற முடியும்."
    ))

    # 019 - Key C (Medium)
    qs.append(make_q(
        num=19, diff="Medium", qtype="Concept MCQ", subtopic="Inter-State Water Disputes",
        en_stem="By the Inter-State Water Disputes (Amendment) Act, 2002, what time limit was introduced for the Central Government to refer a water dispute to a tribunal after receiving a request from a state?",
        ta_stem="2002-ஆம் ஆண்டின் மாநிலங்களுக்கு இடையேயான நதிநீர் தகராறுகள் (திருத்தச்) சட்டத்தின் மூலம், ஒரு மாநிலத்திடமிருந்து கோரிக்கை பெறப்பட்ட பிறகு மத்திய அரசு தகராறை தீர்ப்பாயத்திற்கு அனுப்ப எத்தனை காலக்கெடு நிர்ணயிக்கப்பட்டது?",
        en_a="Six months", ta_a="ஆறு மாதங்கள்",
        en_b="Three years", ta_b="மூன்று ஆண்டுகள்",
        en_c="One year", ta_c="ஒரு ஆண்டு",
        en_d="Five years", ta_d="ஐந்து ஆண்டுகள்",
        correct_key="C",
        exp_en="The 2002 amendment enacted the Sarkaria Commission recommendation that the Central Government must set up and refer the water dispute to a tribunal within one year of receiving a request from any state government.",
        exp_ta="ஒரு மாநில அரசிடமிருந்து கோரிக்கை பெறப்பட்ட ஒரு வருடத்திற்குள் மத்திய அரசு தகராறை தீர்ப்பாயத்திற்கு அனுப்ப வேண்டும் என்ற சர்க்காரியா ஆணையப் பரிந்துரையை 2002 திருத்தச் சட்டம் அமல்படுத்தியது.",
        why_a_en="Option A is incorrect; six months is not the statutory limit for reference.",
        why_a_ta="விருப்பம் A தவறானது; ஆறு மாதங்கள் அல்ல.",
        why_b_en="Option B is incorrect; three years is the time limit for the Tribunal to submit its report (extendable by two years).",
        why_b_ta="விருப்பம் B தவறானது; மூன்று ஆண்டுகள் என்பது தீர்ப்பாயம் அறிக்கை சமர்ப்பிப்பதற்கான காலக்கெடு ஆகும்.",
        why_c_en="Option C is correct; one year is the statutory period for reference by the Centre.",
        why_c_ta="விருப்பம் C சரியானது; மத்திய அரசு தீர்ப்பாயத்திற்கு அனுப்ப 1 ஆண்டு காலக்கெடு உள்ளது.",
        why_d_en="Option D is incorrect.",
        why_d_ta="விருப்பம் D தவறானது.",
        tip_en="2002 Amendment limits: 1 year for Central Government to set up tribunal; 3 years (extendable by 2 years) for Tribunal to give decision.",
        tip_ta="2002 திருத்த வரம்புகள்: மத்திய அரசு தீர்ப்பாயம் அமைக்க 1 ஆண்டு; தீர்ப்பாயம் தீர்ப்பு வழங்க 3 ஆண்டுகள் (மேலும் 2 ஆண்டுகள் நீட்டிக்கப்படலாம்).",
        fact_en="Prior to the 2002 amendment, there were no statutory time limits, leading to decades of delay in setting up water tribunals.",
        fact_ta="2002 திருத்தத்திற்கு முன்பு காலக்கெடு இல்லாததால், நதிநீர் தீர்ப்பாயங்களை அமைக்க பல ஆண்டுகள் தாமதம் ஏற்பட்டது."
    ))

    # 020 - Key D (Medium)
    qs.append(make_q(
        num=20, diff="Medium", qtype="Concept MCQ", subtopic="Inter-State Trade and Commerce",
        en_stem="Which article of the Constitution empowers Parliament to appoint by law an authority for carrying out the purposes of Articles 301, 302, 303, and 304, though no such authority has been appointed so far?",
        ta_stem="சரத்துகள் 301, 302, 303 மற்றும் 304-ன் நோக்கங்களை நிறைவேற்றுவதற்காக ஒரு அதிகார அமைப்பைச் சட்டத்தின் மூலம் நியமிக்க பாராளுமன்றத்திற்கு அதிகாரம் அளிக்கும் சரத்து எது (இதுவரை அத்தகைய அமைப்பு நியமிக்கப்படவில்லை)?",
        en_a="Article 301", ta_a="சரத்து 301",
        en_b="Article 303", ta_b="சரத்து 303",
        en_c="Article 305", ta_c="சரத்து 305",
        en_d="Article 307", ta_d="சரத்து 307",
        correct_key="D",
        exp_en="Article 307 empowers Parliament to appoint by law such authority as it considers appropriate for carrying out the purposes of Articles 301, 302, 303, and 304, and confer on that authority necessary powers and duties. No such authority has been set up till date.",
        exp_ta="சரத்துகள் 301 முதல் 304 வரையிலான நோக்கங்களை நிறைவேற்றுவதற்காக பொருத்தமான ஓர் அதிகார அமைப்பை பாராளுமன்றம் சட்டத்தின் மூலம் நியமிக்கலாம் என்று சரத்து 307 கூறுகிறது. ஆனால் இதுவரை அத்தகைய அமைப்பு எதுவும் அமைக்கப்படவில்லை.",
        why_a_en="Option A proclaims freedom of trade.",
        why_a_ta="விருப்பம் A வர்த்தக சுதந்திரத்தை அறிவிக்கிறது.",
        why_b_en="Option B restricts discriminatory powers.",
        why_b_ta="விருப்பம் B பாகுபாடு காட்டும் அதிகாரங்களைத் தடுக்கிறது.",
        why_c_en="Option C saves existing laws and state monopolies.",
        why_c_ta="விருப்பம் C நடைமுறையில் உள்ள சட்டங்களையும் அரசு ஏகபோகங்களையும் பாதுகாக்கிறது.",
        why_d_en="Option D is correct; Article 307 provides for appointing an Inter-State Trade authority.",
        why_d_ta="விருப்பம் D சரியானது; சரத்து 307 வர்த்தக அதிகார அமைப்பை நியமிக்க வழிசெய்கிறது.",
        tip_en="Article 307 is modelled on the Inter-State Commerce Commission of the USA, though never created in India.",
        tip_ta="சரத்து 307 அமெரிக்காவின் மாநிலங்களுக்கு இடையேயான வர்த்தக ஆணையத்தை மாதிரியாகக் கொண்டது, ஆனால் இந்தியாவில் இதுவரை உருவாக்கப்படவில்லை.",
        fact_en="Both the First ARC and Sarkaria Commission recommended setting up an authority under Article 307, but it has not been implemented.",
        fact_ta="முதல் நிர்வாக சீர்திருத்த ஆணையமும் சர்க்காரியா ஆணையமும் சரத்து 307-ன் கீழ் ஓர் அமைப்பை ஏற்படுத்தப் பரிந்துரைத்தன."
    ))

    # 021 - Key A (Medium)
    qs.append(make_q(
        num=21, diff="Medium", qtype="Concept MCQ", subtopic="Zonal Councils and Reorganisation",
        en_stem="Which of the following functions does a Zonal Council perform under the States Reorganisation Act, 1956?",
        ta_stem="மாநில மறுசீரமைப்புச் சட்டம் 1956-ன் கீழ் ஒரு மண்டல கவுன்சில் பின்வரும் எந்தப் பணியைச் செய்கிறது?",
        en_a="Functions strictly as an advisory body on matters of common interest like border disputes, linguistic minorities, and inter-state transport", ta_a="எல்லைத் தகராறுகள், மொழி சிறுபான்மையினர் மற்றும் மாநிலங்களுக்கு இடையேயான போக்குவரத்து போன்ற பொதுவான விஷயங்களில் ஆலோசனைக் குழுவாக மட்டுமே செயல்படுகிறது",
        en_b="Adjudicates binding legal verdicts between states like a court of law", ta_b="நீதிமன்றம் போல மாநிலங்களுக்கிடையே கட்டுப்படுத்தும் சட்டப்பூர்வ தீர்ப்புகளை வழங்குகிறது",
        en_c="Directly drafts and passes financial appropriations for member states", ta_c="உறுப்பு மாநிலங்களுக்கான நிதி ஒதுக்கீடுகளை நேரடியாக வரைவு செய்து நிறைவேற்றுகிறது",
        en_d="Exercises direct constitutional command over state police forces", ta_d="மாநில காவல் படைகளின் மீது நேரடி அரசியலமைப்பு கட்டளையைப் பயன்படுத்துகிறது",
        correct_key="A",
        exp_en="Under Section 21 of the States Reorganisation Act, 1956, each Zonal Council is an advisory body and may discuss and make recommendations to the Central Government and member states on matters of common interest in the field of economic and social planning, border disputes, linguistic minorities, or inter-state transport.",
        exp_ta="மாநில மறுசீரமைப்புச் சட்டம் பிரிவு 21-ன் படி, மண்டல கவுன்சில்கள் வெறும் ஆலோசனை அமைப்புகள் மட்டுமே. அவை பொருளாதார திட்டமிடல், எல்லைத் தகராறுகள், மொழி சிறுபான்மையினர் மற்றும் போக்குவரத்து போன்ற பொது நலன் சார்ந்த விஷயங்களில் பரிந்துரைகளை மட்டுமே செய்ய முடியும்.",
        why_a_en="Option A is correct; Zonal Councils are purely advisory bodies.",
        why_a_ta="விருப்பம் A சரியானது; மண்டல கவுன்சில்கள் முற்றிலும் ஆலோசனை அமைப்புகள் மட்டுமே.",
        why_b_en="Option B is incorrect; they have no judicial or binding adjudicatory powers.",
        why_b_ta="விருப்பம் B தவறானது; அவற்றுக்கு நீதித்துறை அதிகாரம் இல்லை.",
        why_c_en="Option C is incorrect; they cannot appropriate funds.",
        why_c_ta="விருப்பம் C தவறானது; அவை நிதியை ஒதுக்க முடியாது.",
        why_d_en="Option D is incorrect; police is a State subject under Entry 2 List II.",
        why_d_ta="விருப்பம் D தவறானது; காவல் துறை மாநிலப் பட்டியலில் உள்ளது.",
        tip_en="Zonal Councils = Purely advisory; cannot pass binding decrees.",
        tip_ta="மண்டல கவுன்சில்கள் = ஆலோசனை அமைப்புகள் மட்டுமே; கட்டுப்படுத்தும் ஆணைகளை பிறப்பிக்க முடியாது.",
        fact_en="Section 21(2) specifically enumerates border disputes, linguistic minorities, and inter-state transport as advisory agenda items.",
        fact_ta="பிரிவு 21(2) எல்லைத் தகராறுகள், மொழி சிறுபான்மையினர் மற்றும் போக்குவரத்தை ஆலோசனைக்குரிய அம்சங்களாகக் குறிப்பிடுகிறது."
    ))

    # 022 - Key B (Medium)
    qs.append(make_q(
        num=22, diff="Medium", qtype="Concept MCQ", subtopic="Inter-State Water Disputes",
        en_stem="Under Section 6(2) of the Inter-State River Water Disputes Act, 1956 (as amended in 2002), upon publication of the decision of the Tribunal in the Official Gazette, what legal status does the decision acquire?",
        ta_stem="1956-ஆம் ஆண்டின் மாநிலங்களுக்கு இடையேயான நதிநீர் தகராறுகள் சட்டத்தின் பிரிவு 6(2)-ன் படி (2002 திருத்தப்படி), தீர்ப்பாயத்தின் தீர்ப்பு அரசிதழில் வெளியிடப்பட்டவுடன் அது என்ன சட்ட அந்தஸ்தைப் பெறுகிறது?",
        en_a="The status of a mere administrative recommendation open to modification by the Centre", ta_a="மத்திய அரசால் மாற்றியமைக்கக்கூடிய வெறும் நிர்வாகப் பரிந்துரையின் அந்தஸ்து",
        en_b="The same force as an order or decree of the Supreme Court of India", ta_b="இந்திய உச்ச நீதிமன்றத்தின் ஆணை அல்லது தீர்ப்பிற்குரிய அதே அந்தஸ்து",
        en_c="The status of a proposed Constitutional Amendment Bill", ta_c="முன்மொழியப்பட்ட அரசியலமைப்பு திருத்த மசோதாவின் அந்தஸ்து",
        en_d="The status of an interim arbitration award subject to Governor assent", ta_d="ஆளுநரின் ஒப்புதலுக்கு உட்பட்ட இடைக்கால நடுவர் தீர்ப்பின் அந்தஸ்து",
        correct_key="B",
        exp_en="Section 6(2) inserted by the 2002 Amendment Act explicitly provides: 'The decision of the Tribunal, upon its publication in the Official Gazette, shall have the same force as an order or decree of the Supreme Court.'",
        exp_ta="2002 திருத்தச் சட்டம் மூலம் சேர்க்கப்பட்ட பிரிவு 6(2) தெளிவாகக் கூறுகிறது: 'தீர்ப்பாயத்தின் முடிவு அரசிதழில் வெளியிடப்பட்டவுடன், அது உச்ச நீதிமன்றத்தின் ஆணை அல்லது தீர்ப்பிற்குரிய அதே சக்தியைக் கொண்டிருக்கும்.'",
        why_a_en="Option A is incorrect; it is not a mere recommendation.",
        why_a_ta="விருப்பம் A தவறானது; இது வெறும் பரிந்துரை அல்ல.",
        why_b_en="Option B is correct; it has the exact force of a decree of the Supreme Court.",
        why_b_ta="விருப்பம் B சரியானது; இது உச்ச நீதிமன்றத்தின் தீர்ப்பிற்கு இணையான அதிகாரத்தைக் கொண்டுள்ளது.",
        why_c_en="Option C is incorrect; it is not a constitutional amendment.",
        why_c_ta="விருப்பம் C தவறானது; இது அரசியலமைப்பு திருத்தம் அல்ல.",
        why_d_en="Option D is incorrect; Governor has no role.",
        why_d_ta="விருப்பம் D தவறானது; ஆளுநருக்கு இதில் பங்கு இல்லை.",
        tip_en="Section 6(2) equates the gazetted tribunal award with a decree of the Supreme Court.",
        tip_ta="பிரிவு 6(2) அரசிதழில் வெளியிடப்பட்ட தீர்ப்பாய தீர்ப்பை உச்ச நீதிமன்ற தீர்ப்பிற்கு இணையாக்குகிறது.",
        fact_en="This provision was introduced to prevent states from defying tribunal awards and enacting nullifying state legislations.",
        fact_ta="மாநிலங்கள் தீர்ப்பாய தீர்ப்புகளை மீறுவதையும் முரண்பட்ட சட்டங்களை இயற்றுவதையும் தடுக்க இந்த விதி கொண்டுவரப்பட்டது."
    ))

    # 023 - Key C (Medium)
    qs.append(make_q(
        num=23, diff="Medium", qtype="Concept MCQ", subtopic="Inter-State Council",
        en_stem="In which year was the first formal meeting of the Inter-State Council held after its establishment under Article 263?",
        ta_stem="சரத்து 263-ன் கீழ் நிறுவப்பட்ட பிறகு, மாநிலங்களுக்கு இடையேயான கவுன்சிலின் முதல் முறையான கூட்டம் எந்த ஆண்டில் நடைபெற்றது?",
        en_a="1988", ta_a="1988",
        en_b="1989", ta_b="1989",
        en_c="1990", ta_c="1990",
        en_d="1996", ta_d="1996",
        correct_key="C",
        exp_en="The Inter-State Council was established on May 28, 1990, and its first formal meeting took place on October 10, 1990 under the chairmanship of Prime Minister V.P. Singh.",
        exp_ta="மாநிலங்களுக்கு இடையேயான கவுன்சில் மே 28, 1990 இல் நிறுவப்பட்டு, அதன் முதல் கூட்டம் அக்டோபர் 10, 1990 அன்று பிரதமர் வி.பி. சிங் தலைமையில் நடைபெற்றது.",
        why_a_en="Option A is 1988, when the Sarkaria Commission submitted its report.",
        why_a_ta="விருப்பம் A 1988 சர்க்காரியா ஆணைய அறிக்கை சமர்ப்பிக்கப்பட்ட ஆண்டு.",
        why_b_en="Option B is 1989, prior to the Presidential Order.",
        why_b_ta="விருப்பம் B குடியரசுத் தலைவர் ஆணைக்கு முந்தைய ஆண்டு.",
        why_c_en="Option C is correct; the first meeting occurred in October 1990.",
        why_c_ta="விருப்பம் C சரியானது; முதல் கூட்டம் அக்டோபர் 1990 இல் நடைபெற்றது.",
        why_d_en="Option D is 1996, when the Standing Committee was established.",
        why_d_ta="விருப்பம் D 1996, நிலைக்குழு அமைக்கப்பட்ட ஆண்டு.",
        tip_en="Established: May 1990. First meeting: October 1990.",
        tip_ta="நிறுவப்பட்டது: மே 1990. முதல் கூட்டம்: அக்டோபர் 1990.",
        fact_en="The Secretariat of the Inter-State Council was also established in 1991 to service both the Council and the Zonal Councils.",
        fact_ta="கவுன்சில் மற்றும் மண்டல கவுன்சில்களுக்கு உதவ 1991 இல் மாநிலங்களுக்கு இடையேயான கவுன்சில் செயலகம் அமைக்கப்பட்டது."
    ))

    # 024 - Key D (Medium)
    qs.append(make_q(
        num=24, diff="Medium", qtype="Concept MCQ", subtopic="Inter-State Trade and Commerce",
        en_stem="In the landmark case Atiabari Tea Co. Ltd. v. State of Assam (1961), what did the Supreme Court hold regarding taxes and Article 301?",
        ta_stem="வரலாற்றுச் சிறப்புமிக்க அட்டியாபாரி டீ கோ. லிமிடெட் எதிர் அசாம் மாநிலம் (1961) வழக்கில், வரிகள் மற்றும் சரத்து 301 குறித்து உச்ச நீதிமன்றம் என்ன தீர்ப்பளித்தது?",
        en_a="No tax of any kind can ever be imposed on goods moving between states", ta_a="மாநிலங்களுக்கிடையே நகரும் பொருட்களின் மீது எந்தவித வரியும் ஒருபோதும் விதிக்கப்பட முடியாது",
        en_b="Taxes are completely outside the purview of Part XIII under all circumstances", ta_b="எல்லா சூழ்நிலைகளிலும் வரிகள் பகுதி XIII-ன் வரம்பிற்கு முற்றிலும் வெளியே உள்ளன",
        en_c="Only the President has the power to determine tax rates under Article 301", ta_c="சரத்து 301-ன் கீழ் வரி விகிதங்களை நிர்ணயிக்கும் அதிகாரம் குடியரசுத் தலைவருக்கு மட்டுமே உள்ளது",
        en_d="Taxes which directly and immediately restrict the free flow of trade violate Article 301 unless saved by Article 304(b)", ta_d="சரத்து 304(b)-ஆல் பாதுகாக்கப்படாவிட்டால், வர்த்தகத்தின் சுதந்திரமான ஓட்டத்தை நேரடியாகவும் உடனடியாகவும் கட்டுப்படுத்தும் வரிகள் சரத்து 301-ஐ மீறுகின்றன",
        correct_key="D",
        exp_en="The Supreme Court held in Atiabari Tea Co. (1961) that taxing laws are not exempt from Article 301. Taxes which directly and immediately restrict the flow of trade violate Article 301 unless they comply with the restrictions under Article 304(b).",
        exp_ta="அட்டியாபாரி டீ கோ. (1961) வழக்கில் உச்ச நீதிமன்றம், வரிச் சட்டங்கள் சரத்து 301-லிருந்து விலக்கு பெறவில்லை என்றும், வர்த்தகத்தை நேரடியாகவும் உடனடியாகவும் தடுக்கும் வரிகள் சரத்து 304(b)-ன் கீழ் வராவிட்டால் சரத்து 301-ஐ மீறும் என்றும் தீர்ப்பளித்தது.",
        why_a_en="Option A is too absolute; compensatory and regulatory taxes are permitted.",
        why_a_ta="விருப்பம் A தவறானது; ஒழுங்குமுறை வரிகள் அனுமதிக்கப்படுகின்றன.",
        why_b_en="Option B is incorrect; taxes are within the purview of Part XIII.",
        why_b_ta="விருப்பம் B தவறானது; வரிகள் பகுதி XIII-க்குள் வருகின்றன.",
        why_c_en="Option C is incorrect; legislatures fix tax rates.",
        why_c_ta="விருப்பம் C தவறானது; சட்டமன்றங்களே வரி விகிதங்களை நிர்ணயிக்கின்றன.",
        why_d_en="Option D is correct; the direct and immediate restriction test was formulated here.",
        why_d_ta="விருப்பம் D சரியானது; நேரடி மற்றும் உடனடி கட்டுப்பாடு சோதனை இதில் உருவாக்கப்பட்டது.",
        tip_en="Atiabari (1961) = 'Direct and immediate restriction' test for taxes under Article 301.",
        tip_ta="அட்டியாபாரி (1961) = சரத்து 301-ன் கீழ் வரிகளுக்கான 'நேரடி மற்றும் உடனடி கட்டுப்பாடு' சோதனை.",
        fact_en="This strict test was later softened in the Automobile Transport case (1962), which carved out the doctrine of compensatory taxes.",
        fact_ta="இந்த கடுமையான சோதனை பின்னர் ஆட்டோமொபைல் டிரான்ஸ்போர்ட் வழக்கில் (1962) ஈட்டு வரிக் கோட்பாட்டை உருவாக்கி தளர்த்தப்பட்டது."
    ))

    # 025 - Key A (Medium)
    qs.append(make_q(
        num=25, diff="Medium", qtype="Concept MCQ", subtopic="Inter-State River Water Disputes",
        en_stem="Which of the following River Boards was actually constituted by the Central Government under the River Boards Act, 1956?",
        ta_stem="1956-ஆம் ஆண்டின் நதி வாரியங்கள் சட்டத்தின் கீழ் மத்திய அரசால் உண்மையில் அமைக்கப்பட்ட நதி வாரியம் எது?",
        en_a="No river board has ever been established under the River Boards Act, 1956", ta_a="1956-ஆம் ஆண்டின் நதி வாரியங்கள் சட்டத்தின் கீழ் இதுவரை எந்த நதி வாரியமும் அமைக்கப்படவில்லை",
        en_b="Cauvery River Board", ta_b="காவிரி நதி வாரியம்",
        en_c="Ganga River Basin Board", ta_c="கங்கை நதி வடிநில வாரியம்",
        en_d="Narmada Control Board", ta_d="நர்மதா கட்டுப்பாட்டு வாரியம்",
        correct_key="A",
        exp_en="Remarkably, although the River Boards Act was enacted in 1956 to establish river boards for regulation and development of inter-state rivers, not a single river board has ever been set up under this Act till date due to resistance from state governments.",
        exp_ta="வியக்கத்தக்க வகையில், நதி வாரியங்கள் சட்டம் 1956 இல் இயற்றப்பட்டாலும், மாநில அரசுகளின் எதிர்ப்பு காரணமாக இந்தச் சட்டத்தின் கீழ் இன்றுவரை ஒரு நதி வாரியம் கூட அமைக்கப்படவில்லை.",
        why_a_en="Option A is correct; zero river boards have been constituted under the 1956 Act.",
        why_a_ta="விருப்பம் A சரியானது; 1956 சட்டத்தின் கீழ் ஒரு நதி வாரியம் கூட அமைக்கப்படவில்லை.",
        why_b_en="Option B is incorrect; Cauvery has CWMA, which was set up under IRWD Act / Supreme Court orders.",
        why_b_ta="விருப்பம் B தவறானது; காவிரிக்கு CWMA உள்ளது.",
        why_c_en="Option C is incorrect; NMCG was set up under EPA 1986.",
        why_c_ta="விருப்பம் C தவறானது; NMCG சுற்றுச்சூழல் பாதுகாப்புச் சட்டத்தின் கீழ் உள்ளது.",
        why_d_en="Option D is incorrect; Narmada Control Authority was set up under tribunal orders.",
        why_d_ta="விருப்பம் D தவறானது; நர்மதா கட்டுப்பாட்டு ஆணையம் தீர்ப்பாய ஆணையின் கீழ் அமைக்கப்பட்டது.",
        tip_en="TNPSC Classic Trap: The River Boards Act, 1956 exists on the statute book, but NOT A SINGLE board has ever been constituted under it!",
        tip_ta="TNPSC முக்கிய பொறி: நதி வாரியங்கள் சட்டம் 1956 நடைமுறையில் உள்ளது, ஆனால் அதன் கீழ் ஒரு வாரியம் கூட இதுவரை அமைக்கப்படவில்லை!",
        fact_en="Instead of the River Boards Act, river authorities in India have been created either through tribunal awards or under specific separate statutes.",
        fact_ta="நதி வாரியங்கள் சட்டத்திற்குப் பதிலாக, தீர்ப்பாயத் தீர்ப்புகள் அல்லது குறிப்பிட்ட தனித்தனி சட்டங்கள் மூலமே இந்தியாவில் நதி அதிகார அமைப்புகள் உருவாக்கப்பட்டுள்ளன."
    ))

    return qs

if __name__ == "__main__":
    b1 = get_batch1()
    print(f"Batch 1 count: {len(b1)}")
    from collections import Counter
    print("Keys:", Counter([q["correct_answer"] for q in b1]))
    print("Diffs:", Counter([q["difficulty"] for q in b1]))
