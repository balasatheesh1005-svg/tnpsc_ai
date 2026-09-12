# -*- coding: utf-8 -*-
"""
Builder for Inter-State Relations Part 1 — Easy MCQs (50 Questions)
IDs: ISR_E_001 to ISR_E_050
"""

import json
import os
import sys
from pathlib import Path

def make_q(qid, qtype, stem_en, stem_ta, opt_a_en, opt_a_ta, opt_b_en, opt_b_ta, opt_c_en, opt_c_ta, opt_d_en, opt_d_ta,
           correct_ans, exp_en, exp_ta, wno_a_en, wno_a_ta, wno_b_en, wno_b_ta, wno_c_en, wno_c_ta, wno_d_en, wno_d_ta,
           tip_en, tip_ta, rev_en, rev_ta, bloom="Remember", est_time=45, tags=None):
    opts = [
        {"id": "A", "en": opt_a_en, "ta": opt_a_ta},
        {"id": "B", "en": opt_b_en, "ta": opt_b_ta},
        {"id": "C", "en": opt_c_en, "ta": opt_c_ta},
        {"id": "D", "en": opt_d_en, "ta": opt_d_ta}
    ]
    return {
        "id": qid,
        "subject": "Polity",
        "topic": "Inter-State Relations",
        "difficulty": "Easy",
        "question_type": qtype,
        "question": {"en": stem_en, "ta": stem_ta},
        "question_en": stem_en,
        "question_ta": stem_ta,
        "options": opts,
        "options_en": [opt_a_en, opt_b_en, opt_c_en, opt_d_en],
        "options_ta": [opt_a_ta, opt_b_ta, opt_c_ta, opt_d_ta],
        "correct_answer": correct_ans,
        "answer": correct_ans.lower(),
        "explanation": {"en": exp_en, "ta": exp_ta},
        "explanation_en": exp_en,
        "explanation_ta": exp_ta,
        "why_not_others": {
            "A": {"en": wno_a_en, "ta": wno_a_ta},
            "B": {"en": wno_b_en, "ta": wno_b_ta},
            "C": {"en": wno_c_en, "ta": wno_c_ta},
            "D": {"en": wno_d_en, "ta": wno_d_ta}
        },
        "tnpsc_tip": {"en": tip_en, "ta": tip_ta},
        "revision_fact": {"en": rev_en, "ta": rev_ta},
        "source_reference": ["M. Laxmikanth - Indian Polity", "NCERT Class XI", "Samacheer Kalvi"],
        "bloom_level": bloom,
        "estimated_time_sec": est_time,
        "pyq_similarity": "High",
        "tags": tags or ["Inter-State Relations", "Indian Polity", "Article 261-263"]
    }

def get_easy_questions():
    q = []
    
    # 001 - Ans A
    q.append(make_q(
        "ISR_E_001", "Direct Factual",
        "Which Article of the Indian Constitution provides for 'Full Faith and Credit' to public acts, records, and judicial proceedings of the Union and every State?",
        "இந்திய அரசியலமைப்பின் எந்த உறுப்பு ஒன்றியம் மற்றும் ஒவ்வொரு மாநிலத்தின் பொதுச் சட்டங்கள், பதிவேடுகள் மற்றும் நீதித்துறை நடவடிக்கைகளுக்கு 'முழு நம்பிக்கையும் சான்றும்' வழங்க வகை செய்கிறது?",
        "Article 261", "உறுப்பு 261",
        "Article 262", "உறுப்பு 262",
        "Article 263", "உறுப்பு 263",
        "Article 264", "உறுப்பு 264",
        "A",
        "Article 261 mandates that full faith and credit shall be given throughout the territory of India to public acts, records, and judicial proceedings of the Union and of every State.",
        "உறுப்பு 261, இந்தியா முழுவதும் ஒன்றியம் மற்றும் ஒவ்வொரு மாநிலத்தின் பொதுச் சட்டங்கள், பதிவேடுகள் மற்றும் நீதித்துறை நடவடிக்கைகளுக்கு முழு நம்பிக்கையும் சான்றும் அளிக்கப்பட வேண்டும் எனக் கூறுகிறது.",
        "Article 261 is the correct constitutional provision for Full Faith and Credit.", "உறுப்பு 261 முழு நம்பிக்கையும் சான்றும் விதிக்குரிய சரியான அரசியலமைப்பு உறுப்பாகும்.",
        "Article 262 deals with adjudication of inter-State water disputes.", "உறுப்பு 262 மாநிலங்களுக்கு இடையேயான நதிநீர் தகராறுகளின் தீர்ப்பைக் கையாள்கிறது.",
        "Article 263 provides for the establishment of an Inter-State Council.", "உறுப்பு 263 மாநிலங்களுக்கு இடையிலான மன்றத்தை நிறுவ வகை செய்கிறது.",
        "Article 264 relates to finance provisions and interpretation.", "உறுப்பு 264 நிதி விதிகள் மற்றும் விளக்கங்கள் பற்றியதாகும்.",
        "Remember the sequence: Art 261 (Full Faith), Art 262 (Water Disputes), Art 263 (Inter-State Council).",
        "வரிசையை நினைவில் கொள்க: உறுப்பு 261 (முழு நம்பிக்கை), உறுப்பு 262 (நதிநீர் சிக்கல்கள்), உறுப்பு 263 (மாநிலங்களுக்கு இடையிலான மன்றம்).",
        "Article 261 applies to public acts, records, and judicial proceedings throughout India.",
        "உறுப்பு 261 இந்தியா முழுவதும் பொதுச் சட்டங்கள், பதிவேடுகள் மற்றும் நீதித்துறை நடவடிக்கைகளுக்குப் பொருந்தும்.",
        tags=["Article 261", "Full Faith and Credit"]
    ))

    # 002 - Ans B
    q.append(make_q(
        "ISR_E_002", "Direct Factual",
        "Under Article 261(3) of the Constitution, final judgments or orders delivered by which category of courts are capable of execution anywhere in India?",
        "அரசியலமைப்பு உறுப்பு 261(3)-ன் கீழ், எந்த வகை நீதிமன்றங்களால் வழங்கப்பட்ட இறுதித் தீர்ப்புகள் அல்லது ஆணைகள் இந்தியா முழுவதும் நிறைவேற்றப்படத் தக்கவை?",
        "Criminal courts only", "குற்றவியல் நீதிமன்றங்கள் மட்டுமே",
        "Civil courts only", "உரிமையியல் நீதிமன்றங்கள் மட்டுமே",
        "Revenue courts only", "வருவாய் நீதிமன்றங்கள் மட்டுமே",
        "Military tribunals only", "இராணுவத் தீர்ப்பாயங்கள் மட்டுமே",
        "B",
        "Article 261(3) specifically provides that final judgments or orders delivered or passed by civil courts in any part of the territory of India shall be capable of execution anywhere within that territory.",
        "உறுப்பு 261(3), இந்தியாவின் எந்தப் பகுதியிலும் உள்ள உரிமையியல் நீதிமன்றங்களால் (Civil courts) பிறப்பிக்கப்பட்ட இறுதித் தீர்ப்புகள் அல்லது ஆணைகள் இந்தியா முழுவதிலும் நிறைவேற்றப்படத் தக்கவை எனக் குறிப்பிடுகிறது.",
        "Criminal judgments are excluded from automatic inter-State execution under Art 261(3).", "உறுப்பு 261(3)-ன் கீழ் குற்றவியல் தீர்ப்புகள் தானாக நிறைவேற்றப்படுவதிலிருந்து விலக்கப்பட்டுள்ளன.",
        "Article 261(3) explicitly mentions civil courts, not criminal courts.", "உறுப்பு 261(3) தெளிவாக உரிமையியல் நீதிமன்றங்களைக் குறிப்பிடுகிறது.",
        "Revenue court penal orders do not qualify for execution under Art 261(3).", "வருவாய் நீதிமன்ற தண்டனை ஆணைகள் உறுப்பு 261(3)-ன் கீழ் நிறைவேற்றப்படத் தக்கவை அல்ல.",
        "Military tribunals operate under specialized military law, not under Article 261(3).", "இராணுவத் தீர்ப்பாயங்கள் இராணுவச் சட்டத்தின் கீழ் இயங்குகின்றன, உறுப்பு 261(3)-ன் கீழ் அல்ல.",
        "TNPSC Trap: Article 261(3) applies strictly to CIVIL court decrees, NOT criminal sentences or penal laws.",
        "TNPSC பொறி: உறுப்பு 261(3) உரிமையியல் நீதிமன்றத் தீர்ப்புகளுக்கு மட்டுமே பொருந்தும், குற்றவியல் தண்டனைகளுக்கு அல்ல.",
        "Execution of decrees across state borders under Art 261(3) is confined to civil judgments.",
        "உறுப்பு 261(3)-ன் கீழ் மாநில எல்லைகளைக் கடந்து தீர்ப்புகளை நிறைவேற்றுவது உரிமையியல் தீர்ப்புகளுக்கு மட்டுமே உரித்தானது.",
        tags=["Article 261", "Civil Decrees"]
    ))

    # 003 - Ans C
    q.append(make_q(
        "ISR_E_003", "Direct Factual",
        "Which Article of the Constitution empowers Parliament to provide for the adjudication of disputes relating to the waters of inter-State rivers or river valleys?",
        "மாநிலங்களுக்கு இடையிலான நதிகள் அல்லது நதிப் பள்ளத்தாக்குகளின் நீர் தொடர்பான தகராறுகளுக்குத் தீர்வு காண நாடாளுமன்றத்திற்கு அதிகாரம் அளிக்கும் அரசியலமைப்பு உறுப்பு எது?",
        "Article 260", "உறுப்பு 260",
        "Article 261", "உறுப்பு 261",
        "Article 262", "உறுப்பு 262",
        "Article 265", "உறுப்பு 265",
        "C",
        "Article 262(1) states that Parliament may by law provide for the adjudication of any dispute or complaint with respect to the use, distribution, or control of the waters of, or in, any inter-State river or river valley.",
        "உறுப்பு 262(1), மாநிலங்களுக்கு இடையேயான நதிகள் அல்லது நதிப் பள்ளத்தாக்குகளின் நீரின் பயன்பாடு, பகிர்வு அல்லது கட்டுப்பாடு தொடர்பான தகராறுகளுக்குச் சட்டம் மூலம் தீர்ப்பளிக்க நாடாளுமன்றத்திற்கு அதிகாரம் அளிக்கிறது.",
        "Article 260 deals with jurisdiction of the Union in relation to territories outside India.", "உறுப்பு 260 இந்தியாவிற்கு வெளியிலுள்ள பகுதிகள் மீதான ஒன்றியத்தின் அதிகார வரம்பைக் கையாள்கிறது.",
        "Article 261 deals with Full Faith and Credit.", "உறுப்பு 261 முழு நம்பிக்கையும் சான்றும் விதியைக் கையாள்கிறது.",
        "Article 262 specifically empowers Parliament regarding inter-State water dispute adjudication.", "உறுப்பு 262 மாநிலங்களுக்கு இடையிலான நதிநீர் தகராறுகளின் தீர்ப்பு குறித்து நாடாளுமன்றத்திற்கு அதிகாரம் அளிக்கிறது.",
        "Article 265 mandates that taxes not be imposed save by authority of law.", "உறுப்பு 265 சட்டத்தின் அதிகாரமின்றி வரிகள் விதிக்கப்படக் கூடாது எனக் கூறுகிறது.",
        "Article 262 is the exclusive constitutional source for inter-State water dispute laws.",
        "மாநிலங்களுக்கு இடையிலான நதிநீர் தகராறு சட்டங்களுக்கான பிரத்யேக அரசியலமைப்பு ஆதாரம் உறுப்பு 262 ஆகும்.",
        "Article 262 empowers Parliament to enact water dispute adjudication laws.",
        "உறுப்பு 262 நதிநீர் தகராறுகளைத் தீர்ப்பதற்கான சட்டங்களை இயற்ற நாடாளுமன்றத்திற்கு அதிகாரமளிக்கிறது.",
        tags=["Article 262", "Water Disputes"]
    ))

    # 004 - Ans D
    q.append(make_q(
        "ISR_E_004", "Direct Factual",
        "In which year did Parliament enact the Inter-State River Water Disputes Act under Article 262 of the Constitution?",
        "அரசியலமைப்பு உறுப்பு 262-ன் கீழ் நாடாளுமன்றம் எந்த ஆண்டில் மாநிலங்களுக்கு இடையேயான நதிநீர் தகராறுகள் சட்டத்தை இயற்றியது?",
        "1950", "1950",
        "1952", "1952",
        "1954", "1954",
        "1956", "1956",
        "D",
        "Under Article 262, Parliament enacted the Inter-State River Water Disputes Act in 1956 (Act No. 33 of 1956).",
        "உறுப்பு 262-ன் கீழ், நாடாளுமன்றம் 1956 ஆம் ஆண்டில் மாநிலங்களுக்கு இடையேயான நதிநீர் தகராறுகள் சட்டத்தை (1956-ன் சட்டம் எண் 33) இயற்றியது.",
        "1950 is the year the Constitution of India commenced.", "1950 என்பது இந்திய அரசியலமைப்பு நடைமுறைக்கு வந்த ஆண்டாகும்.",
        "1952 was the year of the first General Elections.", "1952 என்பது முதலாவது பொதுத்தேர்தல் நடைபெற்ற ஆண்டாகும்.",
        "1954 saw early water pact discussions, but the Act was enacted in 1956.", "1954-ல் நதிநீர் பேச்சுவார்த்தைகள் நடந்தன, ஆனால் சட்டம் 1956-ல் இயற்றப்பட்டது.",
        "1956 was the watershed year when the IRWD Act was enacted.", "1956 என்பது மாநிலங்களுக்கு இடையேயான நதிநீர் தகராறுகள் சட்டம் இயற்றப்பட்ட ஆண்டாகும்.",
        "Both the Inter-State River Water Disputes Act and the River Boards Act were passed in 1956.",
        "மாநிலங்களுக்கு இடையேயான நதிநீர் தகராறுகள் சட்டம் மற்றும் நதி வாரியங்கள் சட்டம் ஆகிய இரண்டும் 1956-ல் இயற்றப்பட்டன.",
        "The Inter-State River Water Disputes Act was enacted in 1956.",
        "மாநிலங்களுக்கு இடையேயான நதிநீர் தகராறுகள் சட்டம் 1956 இல் இயற்றப்பட்டது.",
        tags=["IRWD Act 1956", "Article 262"]
    ))

    # 005 - Ans A
    q.append(make_q(
        "ISR_E_005", "Direct Factual",
        "Which Article of the Constitution provides for the establishment of an Inter-State Council to effect coordination between States?",
        "மாநிலங்களுக்கு இடையே ஒருங்கிணைப்பை ஏற்படுத்த மாநிலங்களுக்கு இடையிலான மன்றத்தை அமைக்க வகை செய்யும் அரசியலமைப்பு உறுப்பு எது?",
        "Article 263", "உறுப்பு 263",
        "Article 262", "உறுப்பு 262",
        "Article 261", "உறுப்பு 261",
        "Article 268", "உறுப்பு 268",
        "A",
        "Article 263 provides for the establishment of an Inter-State Council by Presidential order to inquire into disputes, discuss subjects of common interest, and make policy recommendations.",
        "உறுப்பு 263, மாநிலங்களுக்கிடையேயான தகராறுகளை விசாரிக்கவும், பொதுவான நலன் சார்ந்த விஷயங்களை விவாதிக்கவும், கொள்கைப் பரிந்துரைகளை வழங்கவும் குடியரசுத் தலைவர் ஆணை மூலம் மாநிலங்களுக்கு இடையிலான மன்றத்தை அமைக்க வகை செய்கிறது.",
        "Article 263 is the specific constitutional provision for the Inter-State Council.", "உறுப்பு 263 மாநிலங்களுக்கு இடையிலான மன்றத்திற்கான பிரத்யேக விதியாகும்.",
        "Article 262 deals with inter-State water disputes.", "உறுப்பு 262 நதிநீர் தகராறுகளைக் கையாள்கிறது.",
        "Article 261 deals with Full Faith and Credit.", "உறுப்பு 261 முழு நம்பிக்கையும் சான்றும் விதியைக் கையாள்கிறது.",
        "Article 268 deals with duties levied by the Union but collected and appropriated by the States.", "உறுப்பு 268 ஒன்றியத்தால் விதிக்கப்பட்டு மாநிலங்களால் வசூலிக்கப்படும் வரிகளைக் கையாள்கிறது.",
        "Article 263 allows the President to establish the council whenever public interest warrants it.",
        "பொது நலன் கருதும் போது குடியரசுத் தலைவர் இந்த மன்றத்தை அமைக்க உறுப்பு 263 அனுமதிக்கிறது.",
        "Article 263 = Inter-State Council.",
        "உறுப்பு 263 = மாநிலங்களுக்கு இடையிலான மன்றம்.",
        tags=["Article 263", "Inter-State Council"]
    ))

    # 006 - Ans B
    q.append(make_q(
        "ISR_E_006", "Direct Factual",
        "Who is constitutionally empowered under Article 263 to establish an Inter-State Council by order?",
        "அரசியலமைப்பு உறுப்பு 263-ன் கீழ் ஆணை பிறப்பித்து மாநிலங்களுக்கு இடையிலான மன்றத்தை நிறுவ அரசியலமைப்பு ரீதியாக அதிகாரம் பெற்றவர் யார்?",
        "The Prime Minister", "பிரதம அமைச்சர்",
        "The President of India", "இந்தியக் குடியரசுத் தலைவர்",
        "The Parliament of India", "இந்திய நாடாளுமன்றம்",
        "The Chief Justice of India", "இந்தியத் தலைமை நீதிபதி",
        "B",
        "Article 263 states: 'If at any time it appears to the President that the public interest would be served... it shall be lawful for the President by order to establish such a Council.'",
        "உறுப்பு 263, 'பொது நலன் கருதி இத்தகைய மன்றத்தை அமைப்பது உகந்தது என்று எந்த நேரத்திலும் குடியரசுத் தலைவருக்குத் தோன்றினால், ஆணை பிறப்பித்து அத்தகைய மன்றத்தை அவர் நிறுவுவது சட்டப்பூர்வமானது' எனக் கூறுகிறது.",
        "The Prime Minister chairs the Council, but the Council is established by the President.", "பிரதமர் மன்றத்தின் தலைவராக இருக்கிறார், ஆனால் மன்றத்தை அமைப்பது குடியரசுத் தலைவரே.",
        "The President of India is explicitly empowered to establish the Council under Article 263.", "உறுப்பு 263-ன் கீழ் மன்றத்தை நிறுவ இந்தியக் குடியரசுத் தலைவருக்கு வெளிப்படையாக அதிகாரம் அளிக்கப்பட்டுள்ளது.",
        "Parliament does not establish the Council under Art 263; it is done by Presidential Order.", "நாடாளுமன்றம் உறுப்பு 263-ன் கீழ் மன்றத்தை நிறுவுவதில்லை; அது குடியரசுத் தலைவர் ஆணை மூலம் செய்யப்படுகிறது.",
        "The Chief Justice of India has no role in establishing the Inter-State Council.", "இந்தியத் தலைமை நீதிபதிக்கு இந்த மன்றத்தை அமைப்பதில் எந்தப் பங்கும் இல்லை.",
        "Trap: While the PM chairs the Inter-State Council, it is ESTABLISHED by the PRESIDENT by order.",
        "பொறி: பிரதமர் இக்குழுவின் தலைவராக இருந்தாலும், இதனை ஆணை மூலம் நிறுவுபவர் குடியரசுத் தலைவர் ஆவார்.",
        "The President establishes the Inter-State Council under Article 263.",
        "உறுப்பு 263-ன் கீழ் குடியரசுத் தலைவர் மாநிலங்களுக்கு இடையிலான மன்றத்தை நிறுவுகிறார்.",
        tags=["Article 263", "President", "Inter-State Council"]
    ))

    # 007 - Ans C
    q.append(make_q(
        "ISR_E_007", "Direct Factual",
        "Who serves as the ex-officio Chairman of the Inter-State Council established under Article 263?",
        "உறுப்பு 263-ன் கீழ் அமைக்கப்பட்ட மாநிலங்களுக்கு இடையிலான மன்றத்தின் பதவிவழித் தலைவராகப் பணியாற்றுபவர் யார்?",
        "The President of India", "இந்தியக் குடியரசுத் தலைவர்",
        "The Union Home Minister", "மத்திய உள்துறை அமைச்சர்",
        "The Prime Minister of India", "இந்தியப் பிரதம அமைச்சர்",
        "The Vice-President of India", "இந்தியக் குடியரசுத் துணைத் தலைவர்",
        "C",
        "The Prime Minister of India is the Chairman of the Inter-State Council as established by the Presidential Order of 1990.",
        "1990 ஆம் ஆண்டின் குடியரசுத் தலைவர் ஆணையின்படி அமைக்கப்பட்ட மாநிலங்களுக்கு இடையிலான மன்றத்தின் தலைவராக இந்தியப் பிரதம அமைச்சர் செயல்படுகிறார்.",
        "The President establishes the Council, but does not chair its meetings.", "குடியரசுத் தலைவர் மன்றத்தை நிறுவுகிறார், ஆனால் அதன் கூட்டங்களுக்குத் தலைமை தாங்குவதில்லை.",
        "The Union Home Minister chairs the Standing Committee and Zonal Councils, not the full Inter-State Council.", "மத்திய உள்துறை அமைச்சர் நிலைக் குழு மற்றும் மண்டலக் குழுக்களுக்குத் தலைமை தாங்குகிறார், முழு மன்றத்திற்கு அல்ல.",
        "The Prime Minister of India is the Chairman of the Inter-State Council.", "இந்தியப் பிரதமர் மாநிலங்களுக்கு இடையிலான மன்றத்தின் தலைவர் ஆவார்.",
        "The Vice-President chairs the Rajya Sabha, not the Inter-State Council.", "குடியரசுத் துணைத் தலைவர் மாநிலங்களவைக்குத் தலைமை தாங்குகிறார், இம்மன்றத்திற்கு அல்ல.",
        "Chairman of Inter-State Council = Prime Minister; Chairman of Standing Committee = Home Minister.",
        "மாநிலங்களுக்கு இடையிலான மன்றத்தின் தலைவர் = பிரதமர்; அதன் நிலைக் குழுவின் தலைவர் = உள்துறை அமைச்சர்.",
        "The Prime Minister chairs the Inter-State Council.",
        "பிரதம அமைச்சர் மாநிலங்களுக்கு இடையிலான மன்றத்திற்குத் தலைமை தாங்குகிறார்.",
        tags=["Inter-State Council", "Prime Minister"]
    ))

    # 008 - Ans D
    q.append(make_q(
        "ISR_E_008", "Direct Factual",
        "Under which of the following Acts were Zonal Councils established in India?",
        "இந்தியாவில் மண்டலக் குழுக்கள் பின்வரும் எந்தச் சட்டத்தின் கீழ் நிறுவப்பட்டன?",
        "Inter-State Council Act, 1990", "மாநிலங்களுக்கு இடையிலான மன்றச் சட்டம், 1990",
        "Government of India Act, 1935", "இந்திய அரசுச் சட்டம், 1935",
        "Constitution (Seventh Amendment) Act, 1956", "அரசியலமைப்பு (7-வது திருத்தச்) சட்டம், 1956",
        "States Reorganisation Act, 1956", "மாநில மறுசீரமைப்புச் சட்டம், 1956",
        "D",
        "Zonal Councils are statutory bodies established under Part III of the States Reorganisation Act, 1956, not under the Constitution.",
        "மண்டலக் குழுக்கள் அரசியலமைப்பின் கீழ் அல்லாமல், 1956 ஆம் ஆண்டின் மாநில மறுசீரமைப்புச் சட்டத்தின் பகுதி III-ன் கீழ் அமைக்கப்பட்ட சட்டப்பூர்வ அமைப்புகளாகும்.",
        "There is no Inter-State Council Act 1990; the Council was formed by Presidential Order.", "1990-ல் தனிச் சட்டம் எதுவும் இல்லை; மன்றம் குடியரசுத் தலைவர் ஆணை மூலம் அமைக்கப்பட்டது.",
        "The 1935 Act did not create Zonal Councils.", "1935 சட்டம் மண்டலக் குழுக்களை உருவாக்கவில்லை.",
        "The 7th Amendment reorganized states constitutionally, but the Councils were established by the States Reorganisation Act.", "7-வது திருத்தம் மாநிலங்களை மறுசீரமைத்தது, ஆனால் மண்டலக் குழுக்கள் மாநில மறுசீரமைப்புச் சட்டத்தால் உருவாக்கப்பட்டன.",
        "The States Reorganisation Act 1956 created the five original Zonal Councils.", "1956 மாநில மறுசீரமைப்புச் சட்டம் ஐந்து அசல் மண்டலக் குழுக்களை உருவாக்கியது.",
        "High-Yield: Zonal Councils are STATUTORY (1956 Act), NOT constitutional bodies.",
        "முக்கியக் குறிப்பு: மண்டலக் குழுக்கள் சட்டப்பூர்வ அமைப்புகள் (1956 சட்டம்), அரசியலமைப்பு அமைப்புகள் அல்ல.",
        "Zonal Councils were established by the States Reorganisation Act, 1956.",
        "மண்டலக் குழுக்கள் 1956 ஆம் ஆண்டின் மாநில மறுசீரமைப்புச் சட்டத்தால் அமைக்கப்பட்டன.",
        tags=["Zonal Councils", "States Reorganisation Act 1956"]
    ))

    # 009 - Ans A
    q.append(make_q(
        "ISR_E_009", "Direct Factual",
        "How many Zonal Councils were originally created in India under the States Reorganisation Act of 1956?",
        "1956 ஆம் ஆண்டின் மாநில மறுசீரமைப்புச் சட்டத்தின் கீழ் இந்தியாவில் முதலில் எத்தனை மண்டலக் குழுக்கள் உருவாக்கப்பட்டன?",
        "5", "5",
        "6", "6",
        "7", "7",
        "8", "8",
        "A",
        "The States Reorganisation Act of 1956 divided the country into five zones and created five Zonal Councils: Northern, Central, Eastern, Western, and Southern.",
        "1956 ஆம் ஆண்டின் மாநில மறுசீரமைப்புச் சட்டம் நாட்டை ஐந்து மண்டலங்களாகப் பிரித்து ஐந்து மண்டலக் குழுக்களை உருவாக்கியது: வடக்கு, மத்திய, கிழக்கு, மேற்கு மற்றும் தெற்கு மண்டலங்கள்.",
        "Five Zonal Councils were originally established by the 1956 Act.", "1956 சட்டத்தால் முதலில் ஐந்து மண்டலக் குழுக்கள் அமைக்கப்பட்டன.",
        "Six includes the North Eastern Council, which was created later under a separate Act in 1971.", "ஆறு என்பது 1971-ல் தனிச் சட்டத்தால் உருவாக்கப்பட்ட வடகிழக்கு கவுன்சிலையும் உள்ளடக்கியதாகும்.",
        "Seven is an incorrect count.", "ஏழு என்பது தவறான எண்ணிக்கை.",
        "Eight is the number of states in the North Eastern Council, not the number of Zonal Councils.", "எட்டு என்பது வடகிழக்கு கவுன்சிலில் உள்ள மாநிலங்களின் எண்ணிக்கை, மண்டலக் குழுக்களின் எண்ணிக்கை அல்ல.",
        "The original 1956 Act created exactly 5 Zonal Councils (North, South, East, West, Central).",
        "அசல் 1956 சட்டம் சரியாக 5 மண்டலக் குழுக்களை உருவாக்கியது (வடக்கு, தெற்கு, கிழக்கு, மேற்கு, மத்திய).",
        "Original Zonal Councils under 1956 Act = 5.",
        "1956 சட்டத்தின் கீழ் அமைக்கப்பட்ட அசல் மண்டலக் குழுக்கள் = 5.",
        tags=["Zonal Councils", "5 Zones"]
    ))

    # 010 - Ans B
    q.append(make_q(
        "ISR_E_010", "Direct Factual",
        "Who acts as the common Chairman of all the five Zonal Councils established under the States Reorganisation Act, 1956?",
        "1956 ஆம் ஆண்டின் மாநில மறுசீரமைப்புச் சட்டத்தின் கீழ் அமைக்கப்பட்ட ஐந்து மண்டலக் குழுக்களுக்கும் பொதுவான தலைவராகச் செயல்படுபவர் யார்?",
        "The Prime Minister of India", "இந்தியப் பிரதம அமைச்சர்",
        "The Union Home Minister", "மத்திய உள்துறை அமைச்சர்",
        "The Governor of the host State", "நடத்தும் மாநிலத்தின் ஆளுநர்",
        "The Minister of Parliamentary Affairs", "நாடாளுமன்ற விவகாரங்கள் அமைச்சர்",
        "B",
        "The Union Minister of Home Affairs is the common Chairman of all five Zonal Councils established under the States Reorganisation Act, 1956.",
        "1956 மாநில மறுசீரமைப்புச் சட்டத்தின் கீழ் அமைக்கப்பட்ட ஐந்து மண்டலக் குழுக்களுக்கும் மத்திய உள்துறை அமைச்சரே பொதுவான தலைவராகச் செயல்படுகிறார்.",
        "The Prime Minister chairs the Inter-State Council, not the Zonal Councils.", "பிரதமர் மாநிலங்களுக்கு இடையிலான மன்றத்திற்குத் தலைமை தாங்குகிறார், மண்டலக் குழுக்களுக்கு அல்ல.",
        "The Union Home Minister is the statutory Chairman of all Zonal Councils.", "மத்திய உள்துறை அமைச்சர் அனைத்து மண்டலக் குழுக்களின் சட்டப்பூர்வ தலைவர் ஆவார்.",
        "The Governor does not chair the Zonal Council.", "ஆளுநர் மண்டலக் குழுவிற்குத் தலைமை தாங்குவதில்லை.",
        "The Minister of Parliamentary Affairs has no statutory role in Zonal Councils.", "நாடாளுமன்ற விவகார அமைச்சருக்கு மண்டலக் குழுக்களில் சட்டப்பூர்வப் பங்கு இல்லை.",
        "Crucial distinction: Inter-State Council -> Chaired by PM; Zonal Councils -> Chaired by Home Minister.",
        "முக்கிய வேறுபாடு: மாநிலங்களுக்கு இடையிலான மன்றம் -> பிரதமர் தலைமை; மண்டலக் குழுக்கள் -> உள்துறை அமைச்சர் தலைமை.",
        "The Union Home Minister is the Chairman of all Zonal Councils.",
        "மத்திய உள்துறை அமைச்சர் அனைத்து மண்டலக் குழுக்களுக்கும் தலைவராக உள்ளார்.",
        tags=["Zonal Councils", "Union Home Minister"]
    ))

    # 011 - Ans C
    q.append(make_q(
        "ISR_E_011", "Direct Factual",
        "What is the tenure of a Chief Minister as the Vice-Chairman of a Zonal Council under the States Reorganisation Act, 1956?",
        "1956 ஆம் ஆண்டின் மாநில மறுசீரமைப்புச் சட்டத்தின் கீழ் ஒரு மண்டலக் குழுவின் துணைத் தலைவராக ஒரு முதலமைச்சரின் பதவிக்காலம் என்ன?",
        "6 months", "6 மாதங்கள்",
        "2 years", "2 ஆண்டுகள்",
        "1 year", "1 ஆண்டு",
        "3 years", "3 ஆண்டுகள்",
        "C",
        "Under the States Reorganisation Act 1956, the Chief Ministers of the States included in each zone act as Vice-Chairman of the Council by annual rotation, holding office for a period of one year at a time.",
        "1956 மாநில மறுசீரமைப்புச் சட்டத்தின் கீழ், ஒவ்வொரு மண்டலத்திலும் உள்ள மாநிலங்களின் முதலமைச்சர்கள் சுழற்சி முறையில் தலா ஒரு வருட காலத்திற்கு துணைத் தலைவராகப் பதவி வகிக்கின்றனர்.",
        "Six months is too short; the statutory term is one year.", "ஆறு மாதங்கள் தவறானது; சட்டப்பூர்வ காலம் ஒரு ஆண்டாகும்.",
        "Two years is incorrect; rotation occurs annually.", "இரண்டு ஆண்டுகள் தவறானது; சுழற்சி ஆண்டுதோறும் நடைபெறுகிறது.",
        "One year is the exact tenure of the Vice-Chairman by rotation.", "ஒரு ஆண்டு என்பது சுழற்சி முறையிலான துணைத் தலைவரின் சரியான பதவிக்காலமாகும்.",
        "Three years is incorrect.", "மூன்று ஆண்டுகள் தவறானது.",
        "CMs of the member states rotate annually as Vice-Chairman of the Zonal Council.",
        "உறுப்பினர் மாநிலங்களின் முதலமைச்சர்கள் ஆண்டுதோறும் சுழற்சி முறையில் மண்டலக் குழுவின் துணைத் தலைவராகப் பதவி வகிக்கின்றனர்.",
        "Vice-Chairman of Zonal Council = Chief Minister of a member state for 1 year by rotation.",
        "மண்டலக் குழு துணைத் தலைவர் = உறுப்பினர் மாநில முதலமைச்சர், சுழற்சி முறையில் 1 ஆண்டு.",
        tags=["Zonal Councils", "Vice-Chairman", "Tenure"]
    ))

    # 012 - Ans D
    q.append(make_q(
        "ISR_E_012", "Direct Factual",
        "Where is the permanent headquarters of the Southern Zonal Council located?",
        "தென் மண்டலக் குழுவின் நிரந்தரத் தலைமையகம் எங்கு அமைந்துள்ளது?",
        "Bengaluru", "பெங்களூரு",
        "Hyderabad", "ஹைதராபாத்",
        "Thiruvananthapuram", "திருவனந்தபுரம்",
        "Chennai", "சென்னை",
        "D",
        "The headquarters of the Southern Zonal Council is located at Chennai. The Southern Zone includes Andhra Pradesh, Karnataka, Kerala, Tamil Nadu, Telangana, and the UT of Puducherry.",
        "தென் மண்டலக் குழுவின் தலைமையகம் சென்னையில் அமைந்துள்ளது. தென் மண்டலத்தில் ஆந்திரப் பிரதேசம், கர்நாடகா, கேரளா, தமிழ்நாடு, தெலுங்கானா மற்றும் புதுச்சேரி யூனியன் பிரதேசம் ஆகியவை அடங்கும்.",
        "Bengaluru is the capital of Karnataka, but not the headquarters of the Southern Zonal Council.", "பெங்களூரு கர்நாடகாவின் தலைநகரம், ஆனால் தென் மண்டலக் குழுவின் தலைமையகம் அல்ல.",
        "Hyderabad is the capital of Telangana, not the headquarters.", "ஹைதராபாத் தெலுங்கானாவின் தலைநகரம், தலைமையகம் அல்ல.",
        "Thiruvananthapuram is the capital of Kerala, not the headquarters.", "திருவனந்தபுரம் கேரளாவின் தலைநகரம், தலைமையகம் அல்ல.",
        "Chennai is the designated headquarters of the Southern Zonal Council.", "சென்னை தென் மண்டலக் குழுவின் தலைமையகமாக நியமிக்கப்பட்டுள்ளது.",
        "Southern Zonal Council includes Tamil Nadu, Kerala, Karnataka, Andhra Pradesh, Telangana, Puducherry; HQ is Chennai.",
        "தென் மண்டலக் குழுவில் தமிழ்நாடு, கேரளா, கர்நாடகா, ஆந்திரா, தெலுங்கானா, புதுச்சேரி உள்ளன; தலைமையகம் சென்னை.",
        "Southern Zonal Council headquarters = Chennai.",
        "தென் மண்டலக் குழு தலைமையகம் = சென்னை.",
        tags=["Southern Zonal Council", "Headquarters", "Chennai"]
    ))

    # 013 - Ans A
    q.append(make_q(
        "ISR_E_013", "Direct Factual",
        "Where is the headquarters of the Central Zonal Council located?",
        "மத்திய மண்டலக் குழுவின் தலைமையகம் எங்கு அமைந்துள்ளது?",
        "Prayagraj (Allahabad)", "பிரயாக்ராஜ் (அலகாபாத்)",
        "Bhopal", "போபால்",
        "Lucknow", "லக்னோ",
        "Raipur", "ராய்ப்பூர்",
        "A",
        "The headquarters of the Central Zonal Council is located at Prayagraj (Allahabad). The Central Zone comprises Uttar Pradesh, Uttarakhand, Madhya Pradesh, and Chhattisgarh.",
        "மத்திய மண்டலக் குழுவின் தலைமையகம் பிரயாக்ராஜில் (அலகாபாத்) அமைந்துள்ளது. மத்திய மண்டலத்தில் உத்தரப் பிரதேசம், உத்தராகண்ட், மத்தியப் பிரதேசம் மற்றும் சத்தீஸ்கர் ஆகியவை அடங்கும்.",
        "Prayagraj is the official headquarters of the Central Zonal Council.", "பிரயாக்ராஜ் மத்திய மண்டலக் குழுவின் அதிகாரப்பூர்வ தலைமையகம் ஆகும்.",
        "Bhopal is the capital of MP, not the Zonal Council HQ.", "போபால் மத்தியப் பிரதேசத்தின் தலைநகரம், தலைமையகம் அல்ல.",
        "Lucknow is the capital of UP, but Prayagraj is the Council HQ.", "லக்னோ உ.பி.யின் தலைநகரம், ஆனால் பிரயாக்ராஜ் தலைமையகம் ஆகும்.",
        "Raipur is the capital of Chhattisgarh, not the HQ.", "ராய்ப்பூர் சத்தீஸ்கரின் தலைநகரம், தலைமையகம் அல்ல.",
        "Central Zonal Council covers UP, MP, Uttarakhand, Chhattisgarh; HQ is Prayagraj (Allahabad).",
        "மத்திய மண்டலக் குழு உ.பி, ம.பி, உத்தராகண்ட், சத்தீஸ்கர் ஆகியவற்றை உள்ளடக்கியது; தலைமையகம் பிரயாக்ராஜ்.",
        "Central Zonal Council headquarters = Prayagraj (Allahabad).",
        "மத்திய மண்டலக் குழு தலைமையகம் = பிரயாக்ராஜ் (அலகாபாத்).",
        tags=["Central Zonal Council", "Headquarters"]
    ))

    # 014 - Ans B
    q.append(make_q(
        "ISR_E_014", "Direct Factual",
        "Under which statutory enactment was the North Eastern Council established to address regional developmental issues?",
        "பிராந்திய வளர்ச்சிப் பிரச்சினைகளைக் கையாள வடகிழக்கு கவுன்சில் எந்தச் சட்டப்பூர்வ நடவடிக்கையின் கீழ் நிறுவப்பட்டது?",
        "States Reorganisation Act, 1956", "மாநில மறுசீரமைப்புச் சட்டம், 1956",
        "North Eastern Council Act, 1971", "வடகிழக்கு கவுன்சில் சட்டம், 1971",
        "North-Eastern Areas (Reorganisation) Act, 1971", "வடகிழக்குப் பகுதிகள் (மறுசீரமைப்புச்) சட்டம், 1971",
        "Assam Reorganisation Act, 1969", "அசாம் மறுசீரமைப்புச் சட்டம், 1969",
        "B",
        "The North Eastern Council was established under a separate dedicated parliamentary statute, namely the North Eastern Council Act, 1971.",
        "வடகிழக்கு கவுன்சில் 1971 ஆம் ஆண்டின் வடகிழக்கு கவுன்சில் சட்டம் என்ற தனி நாடாளுமன்றச் சட்டத்தின் கீழ் நிறுவப்பட்டது.",
        "States Reorganisation Act 1956 created the 5 Zonal Councils, not the North Eastern Council.", "1956 சட்டம் 5 மண்டலக் குழுக்களை உருவாக்கியது, வடகிழக்கு கவுன்சிலை அல்ல.",
        "The North Eastern Council Act, 1971 is the specific statutory basis of this council.", "1971 வடகிழக்கு கவுன்சில் சட்டம் இக்கவுன்சிலின் குறிப்பிட்ட சட்டப்பூர்வ அடிப்படையாகும்.",
        "The North-Eastern Areas (Reorganisation) Act 1971 granted statehood to Manipur, Meghalaya, Tripura, but did not set up the Council.", "1971 வடகிழக்குப் பகுதிகள் மறுசீரமைப்புச் சட்டம் மாநில அந்தஸ்தை வழங்கியது, ஆனால் கவுன்சிலை அமைக்கவில்லை.",
        "The Assam Reorganisation Act 1969 created Meghalaya as an autonomous sub-state, not the Council.", "1969 அசாம் சட்டம் மேகாலயாவைத் தன்னாட்சிப் பகுதியாக உருவாக்கியது, கவுன்சிலை அல்ல.",
        "NEC is NOT created under the States Reorganisation Act 1956; it was created by the North Eastern Council Act 1971.",
        "வடகிழக்கு கவுன்சில் 1956 சட்டத்தின் கீழ் உருவாக்கப்படவில்லை; இது 1971 வடகிழக்கு கவுன்சில் சட்டத்தால் உருவாக்கப்பட்டது.",
        "North Eastern Council was set up under the North Eastern Council Act, 1971.",
        "வடகிழக்கு கவுன்சில் 1971 வடகிழக்கு கவுன்சில் சட்டத்தின் கீழ் அமைக்கப்பட்டது.",
        tags=["North Eastern Council", "NEC Act 1971"]
    ))

    # 015 - Ans C
    q.append(make_q(
        "ISR_E_015", "Direct Factual",
        "In which year was Sikkim formally inducted as the eighth member state of the North Eastern Council?",
        "சிக்கிம் எந்த ஆண்டில் முறைப்படி வடகிழக்கு கவுன்சிலின் எட்டாவது உறுப்பினர் மாநிலமாக இணைக்கப்பட்டது?",
        "1975", "1975",
        "1990", "1990",
        "2002", "2002",
        "2014", "2014",
        "C",
        "Sikkim was included as the eighth member of the North Eastern Council following the amendment of the North Eastern Council Act in 2002.",
        "2002 ஆம் ஆண்டில் வடகிழக்கு கவுன்சில் சட்டம் திருத்தப்பட்டதைத் தொடர்ந்து, சிக்கிம் வடகிழக்கு கவுன்சிலின் எட்டாவது உறுப்பினராகச் சேர்க்கப்பட்டது.",
        "1975 was when Sikkim became the 22nd State of India via the 36th Amendment Act.", "1975 என்பது 36-வது திருத்தச் சட்டம் மூலம் சிக்கிம் இந்தியாவின் 22-வது மாநிலமாக மாறிய ஆண்டாகும்.",
        "1990 was when the Inter-State Council was set up, not Sikkim's inclusion in NEC.", "1990 என்பது மாநிலங்களுக்கு இடையிலான மன்றம் அமைக்கப்பட்ட ஆண்டாகும்.",
        "2002 is the exact year of the amendment making Sikkim the 8th member of NEC.", "2002 என்பது சிக்கிமை 8-வது உறுப்பினராக மாற்றிய திருத்தம் செய்யப்பட்ட ஆண்டாகும்.",
        "2014 was when Telangana was formed, unrelated to Sikkim NEC inclusion.", "2014 என்பது தெலுங்கானா உருவான ஆண்டாகும்.",
        "Sikkim joined the Indian Union in 1975, but joined the North Eastern Council in 2002.",
        "சிக்கிம் இந்திய ஒன்றியத்தில் 1975 இல் இணைந்தது, ஆனால் வடகிழக்கு கவுன்சிலில் 2002 இல் இணைந்தது.",
        "Sikkim became the 8th member of NEC in 2002.",
        "சிக்கிம் 2002 இல் வடகிழக்கு கவுன்சிலின் 8-வது உறுப்பினரானது.",
        tags=["North Eastern Council", "Sikkim", "2002 Amendment"]
    ))

    # 016 - Ans D
    q.append(make_q(
        "ISR_E_016", "Direct Factual",
        "Which landmark Commission on Centre-State Relations (1983-1988) recommended setting up a permanent Inter-State Council under Article 263?",
        "மத்திய-மாநில உறவுகள் குறித்த எந்த வரலாற்றுச் சிறப்புமிக்க ஆணையம் (1983-1988) உறுப்பு 263-ன் கீழ் ஒரு நிரந்தர மாநிலங்களுக்கு இடையிலான மன்றத்தை அமைக்கப் பரிந்துரைத்தது?",
        "Rajamannar Committee", "இராஜமன்னார் குழு",
        "Punchhi Commission", "பூஞ்சி ஆணையம்",
        "Kothari Commission", "கோத்தாரி ஆணையம்",
        "Sarkaria Commission", "சர்க்காரியா ஆணையம்",
        "D",
        "The Sarkaria Commission on Centre-State Relations (submitted 1988) strongly recommended establishing a permanent Inter-State Council under Article 263, which led to its creation in 1990.",
        "மத்திய-மாநில உறவுகள் குறித்த சர்க்காரியா ஆணையம் (1988-ல் அறிக்கை சமர்ப்பித்தது), உறுப்பு 263-ன் கீழ் நிரந்தர மாநிலங்களுக்கு இடையிலான மன்றத்தை அமைக்கப் பரிந்துரைத்தது; இதன் தொடர்ச்சியாக 1990-ல் இம்மன்றம் அமைக்கப்பட்டது.",
        "Rajamannar Committee (1969, TN Govt) made several federal proposals, but the 1990 body directly implemented the Sarkaria Commission report.", "இராஜமன்னார் குழு பல கூட்டாட்சிப் பரிந்துரைகளை வழங்கியது, ஆனால் 1990 மன்றம் சர்க்காரியா ஆணைய அறிக்கையின்படி அமைக்கப்பட்டது.",
        "Punchhi Commission was set up later in 2007 (reported 2010).", "பூஞ்சி ஆணையம் பின்னர் 2007-ல் அமைக்கப்பட்டது (2010-ல் அறிக்கை).",
        "Kothari Commission dealt with education reforms (1964-66).", "கோத்தாரி ஆணையம் கல்விச் சீர்திருத்தங்கள் பற்றியதாகும்.",
        "The Sarkaria Commission directly led to the 1990 Presidential Order creating the Inter-State Council.", "சர்க்காரியா ஆணையமே 1990-ல் மாநிலங்களுக்கு இடையிலான மன்றம் உருவாவதற்குக் காரணமானது.",
        "Sarkaria Commission recommended establishing the Inter-State Council (calling it Inter-Governmental Council).",
        "சர்க்காரியா ஆணையம் மாநிலங்களுக்கு இடையிலான மன்றத்தை அமைக்கப் பரிந்துரைத்தது.",
        "Sarkaria Commission (1988) recommended the Inter-State Council.",
        "சர்க்காரியா ஆணையம் (1988) மாநிலங்களுக்கு இடையிலான மன்றத்தைப் பரிந்துரைத்தது.",
        tags=["Sarkaria Commission", "Inter-State Council"]
    ))

    # 017 - Ans A
    q.append(make_q(
        "ISR_E_017", "Direct Factual",
        "In which year was the Inter-State Council formally established by a Presidential Order under the V.P. Singh Government?",
        "வி.பி. சிங் அரசாங்கத்தின் கீழ் குடியரசுத் தலைவர் ஆணை மூலம் மாநிலங்களுக்கு இடையிலான மன்றம் எந்த ஆண்டில் முறைப்படி அமைக்கப்பட்டது?",
        "1990", "1990",
        "1988", "1988",
        "1992", "1992",
        "1996", "1996",
        "A",
        "The Inter-State Council was formally established by a Presidential Order on 28 May 1990 under the Prime Ministership of V.P. Singh.",
        "மாநிலங்களுக்கு இடையிலான மன்றம் 1990 ஆம் ஆண்டு மே 28 அன்று வி.பி. சிங் பிரதமராக இருந்தபோது குடியரசுத் தலைவர் ஆணை மூலம் முறைப்படி அமைக்கப்பட்டது.",
        "1990 is the exact year of the Presidential Order setting up the Inter-State Council.", "1990 என்பது மாநிலங்களுக்கு இடையிலான மன்றத்தை அமைத்த குடியரசுத் தலைவர் ஆணையின் சரியான ஆண்டாகும்.",
        "1988 was the year the Sarkaria Commission submitted its report.", "1988 என்பது சர்க்காரியா ஆணையம் தனது அறிக்கையைச் சமர்ப்பித்த ஆண்டாகும்.",
        "1992 saw the 73rd and 74th Amendments, not the Inter-State Council setup.", "1992 என்பது 73 மற்றும் 74-வது திருத்தங்கள் இயற்றப்பட்ட ஆண்டாகும்.",
        "1996 was the year the Standing Committee of the Inter-State Council was set up.", "1996 என்பது மாநிலங்களுக்கு இடையிலான மன்றத்தின் நிலைக் குழு அமைக்கப்பட்ட ஆண்டாகும்.",
        "Inter-State Council was notified on 28 May 1990 by President R. Venkataraman.",
        "மாநிலங்களுக்கு இடையிலான மன்றம் 1990 மே 28 அன்று குடியரசுத் தலைவர் ஆர். வெங்கட்ராமனால் அறிவிக்கப்பட்டது.",
        "Inter-State Council established = 1990.",
        "மாநிலங்களுக்கு இடையிலான மன்றம் அமைக்கப்பட்டது = 1990.",
        tags=["Inter-State Council", "1990"]
    ))

    # 018 - Ans B
    q.append(make_q(
        "ISR_E_018", "Direct Factual",
        "Which Article of the Indian Constitution declares that trade, commerce, and intercourse throughout the territory of India shall be free?",
        "இந்திய எல்லை முழுவதும் வர்த்தகம், வாணிபம் மற்றும் தொடர்பு ஆகியவை சுதந்திரமாக இருக்க வேண்டும் என்று பிரகடனப்படுத்தும் இந்திய அரசியலமைப்பு உறுப்பு எது?",
        "Article 300A", "உறுப்பு 300A",
        "Article 301", "உறுப்பு 301",
        "Article 302", "உறுப்பு 302",
        "Article 303", "உறுப்பு 303",
        "B",
        "Article 301 provides that subject to the other provisions of Part XIII, trade, commerce, and intercourse throughout the territory of India shall be free.",
        "உறுப்பு 301, பகுதி XIII-ன் பிற விதிகளுக்கு உட்பட்டு, இந்திய எல்லை முழுவதும் வர்த்தகம், வாணிபம் மற்றும் தொடர்பு சுதந்திரமாக இருக்க வேண்டும் என்று கூறுகிறது.",
        "Article 300A relates to the right to property as a legal right.", "உறுப்பு 300A சட்டப்பூர்வ உரிமையாக சொத்துரிமையைக் கையாள்கிறது.",
        "Article 301 is the foundational declaration of freedom of trade and commerce.", "உறுப்பு 301 வர்த்தகம் மற்றும் வணிகச் சுதந்திரத்தின் அடிப்படைப் பிரகடனமாகும்.",
        "Article 302 empowers Parliament to impose restrictions in public interest.", "உறுப்பு 302 பொது நலன் கருதி கட்டுப்பாடுகளை விதிக்க நாடாளுமன்றத்திற்கு அதிகாரம் அளிக்கிறது.",
        "Article 303 prohibits preference or discrimination.", "உறுப்பு 303 முன்னுரிமை அல்லது பாகுபாட்டைத் தடை செய்கிறது.",
        "Article 301 guarantees both inter-state (between states) and intra-state (within states) trade freedom.",
        "உறுப்பு 301 மாநிலங்களுக்கு இடையிலான மற்றும் மாநிலத்திற்கு உட்பட்ட வர்த்தக சுதந்திரத்திற்கு உத்தரவாதம் அளிக்கிறது.",
        "Article 301 = Freedom of Trade, Commerce, and Intercourse.",
        "உறுப்பு 301 = வர்த்தகம், வாணிபம் மற்றும் தொடர்பின் சுதந்திரம்.",
        tags=["Article 301", "Part XIII"]
    ))

    # 019 - Ans C
    q.append(make_q(
        "ISR_E_019", "Direct Factual",
        "Under which Article of the Constitution can Parliament impose restrictions on the freedom of trade and commerce in the public interest?",
        "அரசியலமைப்பின் எந்த உறுப்பின் கீழ் நாடாளுமன்றம் பொது நலன் கருதி வர்த்தகம் மற்றும் வணிகச் சுதந்திரத்தின் மீது கட்டுப்பாடுகளை விதிக்க முடியும்?",
        "Article 300", "உறுப்பு 300",
        "Article 301", "உறுப்பு 301",
        "Article 302", "உறுப்பு 302",
        "Article 305", "உறுப்பு 305",
        "C",
        "Article 302 states that Parliament may by law impose such restrictions on the freedom of trade, commerce, or intercourse between one State and another or within any part of the territory of India as may be required in the public interest.",
        "உறுப்பு 302, பொது நலன் கருதி தேவைப்படக்கூடிய வகையில், ஒரு மாநிலத்திற்கும் மற்றொரு மாநிலத்திற்கும் இடையே அல்லது இந்தியப் பகுதியின் எந்தவொரு பகுதியிலும் வர்த்தகம், வாணிபம் அல்லது தொடர்புச் சுதந்திரத்தின் மீது நாடாளுமன்றம் சட்டம் மூலம் கட்டுப்பாடுகளை விதிக்கலாம் எனக் கூறுகிறது.",
        "Article 300 deals with suits and proceedings by or against the Government.", "உறுப்பு 300 அரசாங்கத்தின் மீதான வழக்குகளைக் கையாள்கிறது.",
        "Article 301 declares general freedom of trade, not restrictions.", "உறுப்பு 301 வர்த்தக சுதந்திரத்தைப் பிரகடனம் செய்கிறது, கட்டுப்பாடுகளை அல்ல.",
        "Article 302 grants Parliament the power to impose public interest restrictions.", "உறுப்பு 302 நாடாளுமன்றத்திற்குப் பொது நலக் கட்டுப்பாடுகளை விதிக்கும் அதிகாரத்தை வழங்குகிறது.",
        "Article 305 saves existing laws and state monopolies.", "உறுப்பு 305 நடைமுறையிலுள்ள சட்டங்களையும் அரசு ஏகபோகங்களையும் பாதுகாக்கிறது.",
        "Note: Parliament under Article 302 does NOT need previous Presidential sanction, unlike States under Art 304(b).",
        "குறிப்பு: உறுப்பு 302-ன் கீழ் நாடாளுமன்றத்திற்கு குடியரசுத் தலைவரின் முன் அனுமதி தேவையில்லை.",
        "Article 302 empowers Parliament to restrict trade in public interest.",
        "உறுப்பு 302 பொது நலன் கருதி வர்த்தகத்தைக் கட்டுப்படுத்த நாடாளுமன்றத்திற்கு அதிகாரமளிக்கிறது.",
        tags=["Article 302", "Parliament Restrictions"]
    ))

    # 020 - Ans D
    q.append(make_q(
        "ISR_E_020", "Direct Factual",
        "Which Article of the Constitution prohibits both Parliament and State Legislatures from making laws that give preference to one State over another in trade matters?",
        "வர்த்தக விவகாரங்களில் ஒரு மாநிலத்திற்கு மற்றொரு மாநிலத்தை விட முன்னுரிமை அளிக்கும் சட்டங்களை நாடாளுமன்றமும் மாநில சட்டமன்றங்களும் இயற்றுவதைத் தடை செய்யும் அரசியலமைப்பு உறுப்பு எது?",
        "Article 300A", "உறுப்பு 300A",
        "Article 301", "உறுப்பு 301",
        "Article 302", "உறுப்பு 302",
        "Article 303", "உறுப்பு 303",
        "D",
        "Article 303(1) prohibits both Parliament and State Legislatures from making any law giving preference to one State over another or making any discrimination between States by virtue of any entry relating to trade and commerce.",
        "உறுப்பு 303(1), வர்த்தகம் மற்றும் வணிகம் தொடர்பான எந்தவொரு பதிவின் மூலமாகவும் ஒரு மாநிலத்திற்கு மற்றொரு மாநிலத்தை விட முன்னுரிமை அளிக்கும் அல்லது பாகுபாடு காட்டும் எந்தவொரு சட்டத்தையும் நாடாளுமன்றமும் மாநில சட்டமன்றமும் இயற்றக் கூடாது எனத் தடை செய்கிறது.",
        "Article 300A is about property rights.", "உறுப்பு 300A சொத்துரிமை பற்றியது.",
        "Article 301 declares trade freedom.", "உறுப்பு 301 வர்த்தக சுதந்திரத்தைப் பிரகடனம் செய்கிறது.",
        "Article 302 permits restrictions in public interest.", "உறுப்பு 302 பொது நலக் கட்டுப்பாடுகளை அனுமதிக்கிறது.",
        "Article 303 specifically bars preference and discrimination among States.", "உறுப்பு 303 மாநிலங்களுக்கிடையே முன்னுரிமை மற்றும் பாகுபாட்டைத் தெளிவாகத் தடை செய்கிறது.",
        "Article 303 prohibits discriminatory trade legislation between states.",
        "உறுப்பு 303 மாநிலங்களுக்கிடையேயான பாகுபாடான வர்த்தகச் சட்டங்களைத் தடை செய்கிறது.",
        "Article 303 = Prohibition of preference and discrimination in trade.",
        "உறுப்பு 303 = வர்த்தகத்தில் முன்னுரிமை மற்றும் பாகுபாட்டிற்குத் தடை.",
        tags=["Article 303", "Non-Discrimination"]
    ))

    # 021 - Ans A
    q.append(make_q(
        "ISR_E_021", "Direct Factual",
        "Which constitutional clause enables a State Legislature to impose a non-discriminatory tax on goods imported from other States or Union Territories?",
        "பிற மாநிலங்கள் அல்லது யூனியன் பிரதேசங்களிலிருந்து இறக்குமதி செய்யப்படும் பொருட்களின் மீது பாகுபாடற்ற வரியை விதிக்க ஒரு மாநில சட்டமன்றத்திற்கு அதிகாரம் அளிக்கும் அரசியலமைப்புப் பிரிவு எது?",
        "Article 304(a)", "உறுப்பு 304(a)",
        "Article 304(b)", "உறுப்பு 304(b)",
        "Article 302", "உறுப்பு 302",
        "Article 307", "உறுப்பு 307",
        "A",
        "Article 304(a) allows a State Legislature to impose on goods imported from other States or UTs any tax to which similar goods manufactured or produced in that State are subject, so as not to discriminate between imported and locally produced goods.",
        "உறுப்பு 304(a), உள்ளூரில் உற்பத்தி செய்யப்படும் பொருட்களுக்கு விதிக்கப்படும் அதே வரியை, பிற மாநிலங்களிலிருந்து இறக்குமதி செய்யப்படும் பொருட்களுக்கும் பாகுபாடின்றி விதிக்க மாநில சட்டமன்றத்திற்கு அனுமதியளிக்கிறது.",
        "Article 304(a) is the exact provision for non-discriminatory taxation on imported goods.", "உறுப்பு 304(a) இறக்குமதி செய்யப்படும் பொருட்கள் மீதான பாகுபாடற்ற வரிவிதிப்பிற்குரிய துல்லியமான விதியாகும்.",
        "Article 304(b) deals with reasonable restrictions requiring previous Presidential sanction.", "உறுப்பு 304(b) குடியரசுத் தலைவரின் முன் அனுமதியுடன் நியாயமான கட்டுப்பாடுகளை விதிப்பதைக் கையாள்கிறது.",
        "Article 302 applies to Parliament, not State Legislatures.", "உறுப்பு 302 நாடாளுமன்றத்திற்குப் பொருந்தும், மாநில சட்டமன்றங்களுக்கு அல்ல.",
        "Article 307 enables the appointment of an authority.", "உறுப்பு 307 ஓர் அதிகார அமைப்பை நியமிக்க வகை செய்கிறது.",
        "Article 304(a) ensures fiscal parity: tax on imported goods must NOT exceed tax on similar local goods.",
        "உறுப்பு 304(a) நிதி சமத்துவத்தை உறுதி செய்கிறது: இறக்குமதி பொருட்களுக்கான வரி உள்ளூர் பொருட்களை விட அதிகமாக இருக்கக்கூடாது.",
        "Article 304(a) permits non-discriminatory taxes on imported goods.",
        "உறுப்பு 304(a) இறக்குமதி செய்யப்படும் பொருட்கள் மீது பாகுபாடற்ற வரி விதிக்க அனுமதிக்கிறது.",
        tags=["Article 304(a)", "Taxation"]
    ))

    # 022 - Ans B
    q.append(make_q(
        "ISR_E_022", "Direct Factual",
        "Under the proviso to Article 304(b), whose previous sanction is mandatory before introducing a Bill imposing reasonable restrictions on trade in a State Legislature?",
        "உறுப்பு 304(b)-ன் நிபந்தனையின்படி, ஒரு மாநில சட்டமன்றத்தில் வர்த்தகத்தின் மீது நியாயமான கட்டுப்பாடுகளை விதிக்கும் மசோதாவை அறிமுகப்படுத்துவதற்கு முன் யாருடைய முன் அனுமதி கட்டாயமாகும்?",
        "The Governor of the State", "மாநில ஆளுநர்",
        "The President of India", "இந்தியக் குடியரசுத் தலைவர்",
        "The Chief Justice of the High Court", "உயர் நீதிமன்றத் தலைமை நீதிபதி",
        "The Inter-State Council", "மாநிலங்களுக்கு இடையிலான மன்றம்",
        "B",
        "The proviso to Article 304(b) mandates that no Bill or amendment for imposing reasonable restrictions shall be introduced or moved in the Legislature of a State without the previous sanction of the President.",
        "உறுப்பு 304(b)-ன் நிபந்தனை, குடியரசுத் தலைவரின் முன் அனுமதியின்றி நியாயமான கட்டுப்பாடுகளை விதிக்கும் எந்தவொரு மசோதாவோ அல்லது திருத்தமோ மாநில சட்டமன்றத்தில் அறிமுகப்படுத்தப்படவோ அல்லது கொண்டுவரப்படவோ கூடாது எனக் கட்டாயமாக்குகிறது.",
        "The Governor grants assent after passage, but previous sanction for introduction must come from the President.", "ஆளுநர் ஒப்புதல் அளிக்கலாம், ஆனால் அறிமுகத்திற்கான முன் அனுமதி குடியரசுத் தலைவரிடமிருந்து வரவேண்டும்.",
        "The President's previous sanction is strictly required under the proviso to Article 304(b).", "உறுப்பு 304(b)-ன் நிபந்தனையின் கீழ் குடியரசுத் தலைவரின் முன் அனுமதி கண்டிப்பாகத் தேவைப்படுகிறது.",
        "The High Court Chief Justice plays no role in legislative introduction.", "சட்டமன்ற மசோதா அறிமுகத்தில் உயர் நீதிமன்றத் தலைமை நீதிபதிக்குப் பங்கில்லை.",
        "The Inter-State Council is an advisory body with no statutory bill sanction powers.", "மாநிலங்களுக்கு இடையிலான மன்றத்திற்கு மசோதாக்களுக்கு அனுமதி அளிக்கும் அதிகாரம் இல்லை.",
        "TNPSC Trap: Previous sanction under 304(b) is required from the PRESIDENT, not the Governor!",
        "TNPSC பொறி: 304(b)-ன் கீழ் முன் அனுமதி குடியரசுத் தலைவரிடம் பெறப்பட வேண்டும், ஆளுநரிடம் அல்ல!",
        "Article 304(b) requires previous sanction of the President.",
        "உறுப்பு 304(b) குடியரசுத் தலைவரின் முன் அனுமதியைக் கோருகிறது.",
        tags=["Article 304(b)", "Presidential Sanction"]
    ))

    # 023 - Ans C
    q.append(make_q(
        "ISR_E_023", "Direct Factual",
        "Which Article of the Constitution relating to trade restrictions by Part B States was repealed by the Constitution (Seventh Amendment) Act, 1956?",
        "பகுதி B மாநிலங்களின் வர்த்தகக் கட்டுப்பாடுகள் தொடர்பான அரசியலமைப்பின் எந்த உறுப்பு 1956 ஆம் ஆண்டின் (7-வது திருத்தச்) சட்டத்தால் நீக்கப்பட்டது?",
        "Article 304", "உறுப்பு 304",
        "Article 305", "உறுப்பு 305",
        "Article 306", "உறுப்பு 306",
        "Article 307", "உறுப்பு 307",
        "C",
        "Article 306, which empowered certain Part B States to levy taxes and restrictions on trade and commerce, was repealed by the Constitution (Seventh Amendment) Act, 1956 when the distinction between Part A and Part B States was abolished.",
        "பகுதி A மற்றும் பகுதி B மாநிலங்களுக்கு இடையிலான வேறுபாடு ஒழிக்கப்பட்டபோது, சில பகுதி B மாநிலங்கள் வர்த்தகத்தின் மீது வரிகள் மற்றும் கட்டுப்பாடுகளை விதிக்க அதிகாரம் அளித்த உறுப்பு 306, 1956-ன் 7-வது அரசியலமைப்புத் திருத்தச் சட்டத்தால் நீக்கப்பட்டது.",
        "Article 304 remains active in the Constitution.", "உறுப்பு 304 அரசியலமைப்பில் தொடர்ந்து நடைமுறையில் உள்ளது.",
        "Article 305 remains active and saves existing laws.", "உறுப்பு 305 நடைமுறையில் உள்ள சட்டங்களைப் பாதுகாக்கிறது.",
        "Article 306 was specifically repealed by the 7th Constitutional Amendment Act, 1956.", "உறுப்பு 306 குறிப்பாக 1956-ன் 7-வது அரசியலமைப்புத் திருத்தச் சட்டத்தால் நீக்கப்பட்டது.",
        "Article 307 remains active enabling the appointment of an authority.", "உறுப்பு 307 தொடர்ந்து நடைமுறையில் உள்ளது.",
        "Article 306 was repealed because Part B States ceased to exist after the 7th Amendment 1956.",
        "1956-ன் 7-வது திருத்தத்திற்குப் பிறகு பகுதி B மாநிலங்கள் இல்லாமல் போனதால் உறுப்பு 306 நீக்கப்பட்டது.",
        "Article 306 was repealed by the 7th Amendment Act, 1956.",
        "உறுப்பு 306 ஆனது 1956 ஆம் ஆண்டின் 7-வது திருத்தச் சட்டத்தால் நீக்கப்பட்டது.",
        tags=["Article 306", "Repealed", "7th Amendment"]
    ))

    # 024 - Ans D
    q.append(make_q(
        "ISR_E_024", "Direct Factual",
        "Which Article of the Indian Constitution empowers Parliament to appoint an authority for carrying out the purposes of Articles 301, 302, 303, and 304?",
        "உறுப்புகள் 301, 302, 303 மற்றும் 304-ன் நோக்கங்களை நிறைவேற்றுவதற்காக ஓர் அதிகார அமைப்பை நியமிக்க நாடாளுமன்றத்திற்கு அதிகாரம் அளிக்கும் இந்திய அரசியலமைப்பு உறுப்பு எது?",
        "Article 300", "உறுப்பு 300",
        "Article 304", "உறுப்பு 304",
        "Article 305", "உறுப்பு 305",
        "Article 307", "உறுப்பு 307",
        "D",
        "Article 307 empowers Parliament by law to appoint such authority as it considers appropriate for carrying out the purposes of Articles 301, 302, 303, and 304.",
        "உறுப்பு 307, உறுப்புகள் 301, 302, 303 மற்றும் 304 ஆகியவற்றின் நோக்கங்களை நிறைவேற்றுவதற்காகத் தான் பொருத்தமானது எனக் கருதும் ஓர் அதிகார அமைப்பைச் சட்டம் மூலம் நியமிக்க நாடாளுமன்றத்திற்கு அதிகாரம் அளிக்கிறது.",
        "Article 300 deals with legal suits by or against the government.", "உறுப்பு 300 அரசாங்கத்தின் மீதான வழக்குகளைக் கையாள்கிறது.",
        "Article 304 relates to state legislative powers on trade.", "உறுப்பு 304 வர்த்தகம் மீதான மாநில சட்டமன்ற அதிகாரங்களைக் கையாள்கிறது.",
        "Article 305 saves existing laws and state monopolies.", "உறுப்பு 305 நடைமுறையிலுள்ள சட்டங்களைப் பாதுகாக்கிறது.",
        "Article 307 specifically provides for the appointment of a trade authority by Parliament.", "உறுப்பு 307 நாடாளுமன்றத்தால் ஒரு வர்த்தக அதிகார அமைப்பை நியமிக்க வெளிப்படையாக வகை செய்கிறது.",
        "Fact: No authority has ever been appointed by Parliament under Article 307.",
        "உண்மை: உறுப்பு 307-ன் கீழ் நாடாளுமன்றத்தால் இதுவரை எந்த ஓர் அதிகார அமைப்பும் நியமிக்கப்படவில்லை.",
        "Article 307 empowers Parliament to appoint an authority for trade freedom purposes.",
        "உறுப்பு 307 வர்த்தக சுதந்திர நோக்கங்களுக்காக ஓர் அதிகார அமைப்பை நியமிக்க நாடாளுமன்றத்திற்கு அதிகாரமளிக்கிறது.",
        tags=["Article 307", "Trade Authority"]
    ))

    # 025 - Ans A
    q.append(make_q(
        "ISR_E_025", "Direct Factual",
        "In which Part of the Constitution of India are provisions relating to 'Trade, Commerce and Intercourse within the Territory of India' situated?",
        "இந்திய அரசியலமைப்பின் எந்தப் பகுதியில் 'இந்திய எல்லைக்குள் வர்த்தகம், வாணிபம் மற்றும் தொடர்பு' தொடர்பான விதிகள் அமைந்துள்ளன?",
        "Part XIII", "பகுதி XIII",
        "Part XI", "பகுதி XI",
        "Part XII", "பகுதி XII",
        "Part XIV", "பகுதி XIV",
        "A",
        "Trade, Commerce, and Intercourse within the Territory of India is contained in Part XIII of the Constitution (Articles 301 to 307).",
        "இந்திய எல்லைக்குள் வர்த்தகம், வாணிபம் மற்றும் தொடர்பு ஆகியவை அரசியலமைப்பின் பகுதி XIII-ல் (உறுப்புகள் 301 முதல் 307 வரை) அடங்கியுள்ளன.",
        "Part XIII exclusively covers trade, commerce, and intercourse (Articles 301–307).", "பகுதி XIII வர்த்தகம், வாணிபம் மற்றும் தொடர்பை உள்ளடக்கியது (உறுப்புகள் 301–307).",
        "Part XI deals with Relations between the Union and the States (Articles 245–263).", "பகுதி XI மத்திய-மாநில உறவுகளைக் கையாள்கிறது (உறுப்புகள் 245–263).",
        "Part XII deals with Finance, Property, Contracts and Suits (Articles 264–300A).", "பகுதி XII நிதி, சொத்து, ஒப்பந்தங்கள் மற்றும் வழக்குகளைக் கையாள்கிறது (உறுப்புகள் 264–300A).",
        "Part XIV deals with Services under the Union and the States (Articles 308–323).", "பகுதி XIV மத்திய-மாநிலப் பணிகளைக் கையாள்கிறது (உறுப்புகள் 308–323).",
        "Part XI = Inter-State Relations (261-263); Part XIII = Inter-State Trade (301-307).",
        "பகுதி XI = மாநிலங்களுக்கு இடையிலான உறவுகள் (261-263); பகுதி XIII = வர்த்தகம் மற்றும் வாணிபம் (301-307).",
        "Freedom of Trade and Commerce is in Part XIII.",
        "வர்த்தகம் மற்றும் வணிகச் சுதந்திரம் பகுதி XIII இல் உள்ளது.",
        tags=["Part XIII", "Trade and Commerce"]
    ))

    # 026 - Ans B
    q.append(make_q(
        "ISR_E_026", "Direct Factual",
        "Under which Part of the Indian Constitution are the provisions governing Inter-State Relations (Articles 261 to 263) located?",
        "மாநிலங்களுக்கு இடையிலான உறவுகளை ஒழுங்குபடுத்தும் விதிகள் (உறுப்புகள் 261 முதல் 263 வரை) இந்திய அரசியலமைப்பின் எந்தப் பகுதியில் அமைந்துள்ளன?",
        "Part X", "பகுதி X",
        "Part XI", "பகுதி XI",
        "Part XII", "பகுதி XII",
        "Part XIV", "பகுதி XIV",
        "B",
        "Articles 261 to 263 are located in Chapter II (Administrative Relations) of Part XI of the Constitution.",
        "உறுப்புகள் 261 முதல் 263 வரை அரசியலமைப்பின் பகுதி XI-ன் அத்தியாயம் II-ல் (நிர்வாக உறவுகள்) அமைந்துள்ளன.",
        "Part X covers Scheduled and Tribal Areas (Articles 244–244A).", "பகுதி X அட்டவணைப்படுத்தப்பட்ட மற்றும் பழங்குடியினர் பகுதிகளைக் கையாள்கிறது.",
        "Part XI covers Union-State and Inter-State Relations (Articles 245–263).", "பகுதி XI மத்திய-மாநில மற்றும் மாநிலங்களுக்கிடையேயான உறவுகளைக் கையாள்கிறது.",
        "Part XII covers Finance, Property, and Contracts.", "பகுதி XII நிதி, சொத்து மற்றும் ஒப்பந்தங்களைக் கையாள்கிறது.",
        "Part XIV covers Public Services.", "பகுதி XIV பொதுப் பணிகளைக் கையாள்கிறது.",
        "Part XI, Chapter II contains provisions on inter-State cooperation and water disputes.",
        "பகுதி XI, அத்தியாயம் II மாநிலங்களுக்கிடையேயான ஒத்துழைப்பு மற்றும் நதிநீர் தகராறுகள் பற்றிய விதிகளைக் கொண்டுள்ளது.",
        "Inter-State Relations provisions (Arts 261-263) are in Part XI.",
        "மாநிலங்களுக்கு இடையிலான உறவுகள் விதிகள் (உறுப்புகள் 261-263) பகுதி XI இல் உள்ளன.",
        tags=["Part XI", "Constitutional Framework"]
    ))

    # 027 - Ans C
    q.append(make_q(
        "ISR_E_027", "Direct Factual",
        "Who is responsible for nominating the Chairman and judicial members of an Inter-State Water Disputes Tribunal under the IRWD Act, 1956?",
        "1956 ஆம் ஆண்டின் மாநிலங்களுக்கு இடையேயான நதிநீர் தகராறுகள் சட்டத்தின் கீழ் ஒரு நதிநீர் தகராறு தீர்ப்பாயத்தின் தலைவர் மற்றும் நீதித்துறை உறுப்பினர்களைப் பரிந்துரைக்கப் பொறுப்பானவர் யார்?",
        "The President of India", "இந்தியக் குடியரசுத் தலைவர்",
        "The Prime Minister of India", "இந்தியப் பிரதம அமைச்சர்",
        "The Chief Justice of India", "இந்தியத் தலைமை நீதிபதி",
        "The Union Minister of Jal Shakti", "மத்திய ஜல் சக்தி அமைச்சர்",
        "C",
        "Under Section 4(2) of the Inter-State River Water Disputes Act 1956, the Chairman and other members of a water disputes tribunal are nominated by the Chief Justice of India from among sitting judges of the Supreme Court or High Courts.",
        "1956 நதிநீர் தகராறுகள் சட்டத்தின் பிரிவு 4(2)-ன் கீழ், தீர்ப்பாயத்தின் தலைவர் மற்றும் உறுப்பினர்கள் உச்ச நீதிமன்றம் அல்லது உயர் நீதிமன்றங்களின் பணியிலிருக்கும் நீதிபதிகளிலிருந்து இந்தியத் தலைமை நீதிபதியால் பரிந்துரைக்கப்படுகின்றனர்.",
        "The Central Government officially appoints them, but the nomination is strictly made by the Chief Justice of India.", "மத்திய அரசு அதிகாரப்பூர்வமாக நியமிக்கிறது, ஆனால் பரிந்துரை செய்வது இந்தியத் தலைமை நீதிபதியே.",
        "The Prime Minister does not select judicial members of tribunals.", "பிரதமர் தீர்ப்பாய நீதித்துறை உறுப்பினர்களைத் தேர்ந்தெடுப்பதில்லை.",
        "The Chief Justice of India nominates sitting judges to head the tribunal.", "இந்தியத் தலைமை நீதிபதி தீர்ப்பாயத்திற்குத் தலைமை தாங்க பணியிலிருக்கும் நீதிபதிகளைப் பரிந்துரைக்கிறார்.",
        "The Jal Shakti Minister handles water governance, but has no judicial nomination power.", "ஜல் சக்தி அமைச்சர் நதிநீர் நிர்வாகத்தைக் கையாள்கிறார், நீதித்துறை நியமன அதிகாரம் இல்லை.",
        "Tribunal members are nominated by the CJI from sitting judges of the Supreme Court or High Courts.",
        "தீர்ப்பாய உறுப்பினர்கள் உச்ச அல்லது உயர் நீதிமன்றப் பணியிலிருக்கும் நீதிபதிகளிலிருந்து இந்தியத் தலைமை நீதிபதியால் பரிந்துரைக்கப்படுகின்றனர்.",
        "CJI nominates members of water dispute tribunals under IRWD Act 1956.",
        "1956 சட்டத்தின் கீழ் தலைமை நீதிபதி நதிநீர் தீர்ப்பாய உறுப்பினர்களைப் பரிந்துரைக்கிறார்.",
        tags=["IRWD Act 1956", "Chief Justice of India"]
    ))

    # 028 - Ans D
    q.append(make_q(
        "ISR_E_028", "Direct Factual",
        "Under Section 11 of the Inter-State River Water Disputes Act, 1956, the jurisdiction of which court is explicitly barred regarding referred water disputes?",
        "1956 ஆம் ஆண்டின் மாநிலங்களுக்கு இடையேயான நதிநீர் தகராறுகள் சட்டத்தின் பிரிவு 11-ன் கீழ், தீர்ப்பாயத்திற்கு அனுப்பப்பட்ட நதிநீர் தகராறுகள் குறித்து எந்த நீதிமன்றத்தின் அதிகார வரம்பு வெளிப்படையாகத் தடுக்கப்பட்டுள்ளது?",
        "Subordinate Courts only", "சார்பு நீதிமன்றங்கள் மட்டுமே",
        "District Courts only", "மாவட்ட நீதிமன்றங்கள் மட்டுமே",
        "High Courts only", "உயர் நீதிமன்றங்கள் மட்டுமே",
        "The Supreme Court and all other courts", "உச்ச நீதிமன்றம் மற்றும் பிற அனைத்து நீதிமன்றங்களும்",
        "D",
        "Section 11 of the IRWD Act 1956 explicitly enacts the bar permitted under Article 262(2): neither the Supreme Court nor any other court shall have or exercise jurisdiction in respect of any water dispute referred to a tribunal.",
        "1956 நதிநீர் தகராறுகள் சட்டத்தின் பிரிவு 11, உறுப்பு 262(2)-ன் கீழ் அனுமதிக்கப்பட்ட தடையை நடைமுறைப்படுத்துகிறது: தீர்ப்பாயத்திற்கு அனுப்பப்பட்ட எந்தவொரு நதிநீர் தகராறு குறித்தும் உச்ச நீதிமன்றமோ அல்லது பிற நீதிமன்றமோ அதிகார வரம்பைக் கொண்டிருக்கக் கூடாது.",
        "Subordinate courts are barred, but not alone.", "சார்பு நீதிமன்றங்கள் தடுக்கப்பட்டுள்ளன, ஆனால் அவை மட்டுமே அல்ல.",
        "District courts are barred along with all courts.", "மாவட்ட நீதிமன்றங்கள் அனைத்து நீதிமன்றங்களுடன் சேர்ந்து தடுக்கப்பட்டுள்ளன.",
        "High courts are barred, but Supreme Court is also explicitly barred.", "உயர் நீதிமன்றங்கள் தடுக்கப்பட்டுள்ளன, ஆனால் உச்ச நீதிமன்றமும் தெளிவாகத் தடுக்கப்பட்டுள்ளது.",
        "Both the Supreme Court and all other courts are completely barred by Section 11.", "பிரிவு 11-ன் மூலம் உச்ச நீதிமன்றம் மற்றும் பிற அனைத்து நீதிமன்றங்களும் முழுமையாகத் தடுக்கப்பட்டுள்ளன.",
        "Section 11 of IRWD Act 1956 bars Supreme Court and all courts under the authority of Art 262(2).",
        "1956 சட்டத்தின் பிரிவு 11, உறுப்பு 262(2)-ன் அதிகாரத்தின் கீழ் உச்ச நீதிமன்றம் மற்றும் அனைத்து நீதிமன்றங்களையும் தடுக்கிறது.",
        "Section 11 of IRWD Act bars Supreme Court and all other courts.",
        "1956 சட்டத்தின் பிரிவு 11 உச்ச நீதிமன்றம் மற்றும் பிற அனைத்து நீதிமன்றங்களையும் தடுக்கிறது.",
        tags=["Section 11", "Bar of Jurisdiction", "IRWD Act"]
    ))

    # 029 - Ans A
    q.append(make_q(
        "ISR_E_029", "Direct Factual",
        "In which year was the River Boards Act passed by Parliament to facilitate the regulation and development of inter-State rivers and river valleys?",
        "மாநிலங்களுக்கு இடையிலான நதிகள் மற்றும் நதிப் பள்ளத்தாக்குகளின் ஒழுங்குமுறை மற்றும் வளர்ச்சியை எளிதாக்க நாடாளுமன்றத்தால் நதி வாரியங்கள் சட்டம் எந்த ஆண்டில் நிறைவேற்றப்பட்டது?",
        "1956", "1956",
        "1960", "1960",
        "1964", "1964",
        "1970", "1970",
        "A",
        "The River Boards Act was passed by Parliament in 1956 (under Entry 56 of the Union List and Article 262) to establish river boards for the regulation and development of inter-State rivers.",
        "மாநிலங்களுக்கு இடையேயான நதிகளை ஒழுங்குபடுத்தவும் மேம்படுத்தவும் நதி வாரியங்களை நிறுவ 1956 ஆம் ஆண்டில் (மத்திய பட்டியல் பதிவு 56 மற்றும் உறுப்பு 262-ன் கீழ்) நாடாளுமன்றத்தால் நதி வாரியங்கள் சட்டம் நிறைவேற்றப்பட்டது.",
        "1956 is the exact year of the River Boards Act (Act No. 49 of 1956).", "1956 என்பது நதி வாரியங்கள் சட்டம் இயற்றப்பட்ட சரியான ஆண்டாகும் (1956-ன் சட்டம் 49).",
        "1960 was the year of the Indus Waters Treaty, not the River Boards Act.", "1960 என்பது சிந்து நதிநீர் ஒப்பந்தத்தின் ஆண்டு.",
        "1964 is incorrect.", "1964 தவறானது.",
        "1970 is incorrect.", "1970 தவறானது.",
        "Both the IRWD Act (Act 33) and River Boards Act (Act 49) were enacted in 1956.",
        "நதிநீர் தகராறுகள் சட்டம் (சட்டம் 33) மற்றும் நதி வாரியங்கள் சட்டம் (சட்டம் 49) ஆகிய இரண்டும் 1956-ல் இயற்றப்பட்டன.",
        "River Boards Act was passed in 1956.",
        "நதி வாரியங்கள் சட்டம் 1956 இல் நிறைவேற்றப்பட்டது.",
        tags=["River Boards Act", "1956"]
    ))

    # 030 - Ans B
    q.append(make_q(
        "ISR_E_030", "Direct Factual",
        "What is the statutory nature of the River Boards provided for under the River Boards Act, 1956?",
        "1956 ஆம் ஆண்டின் நதி வாரியங்கள் சட்டத்தின் கீழ் வழங்கப்பட்டுள்ள நதி வாரியங்களின் சட்டப்பூர்வ தன்மை என்ன?",
        "Binding judicial tribunals", "கட்டுப்படுத்தும் நீதித்துறைத் தீர்ப்பாயங்கள்",
        "Advisory bodies to the Central Government", "மத்திய அரசிற்கு ஆலோசனை வழங்கும் அமைப்புகள்",
        "Constitutional arbitration councils", "அரசியலமைப்பு நடுவர் மன்றங்கள்",
        "Subordinate benches of the High Court", "உயர் நீதிமன்றத்தின் சார்பு அமர்வுகள்",
        "B",
        "Under the River Boards Act 1956, River Boards are purely advisory bodies established to advise the Central and State Governments on the regulation and development of inter-State rivers.",
        "1956 நதி வாரியங்கள் சட்டத்தின் கீழ், நதி வாரியங்கள் என்பது மாநிலங்களுக்கு இடையேயான நதிகளை ஒழுங்குபடுத்துதல் மற்றும் மேம்படுத்துதல் குறித்து மத்திய மற்றும் மாநில அரசுகளுக்கு ஆலோசனை வழங்கும் முற்றிலும் ஆலோசனை அமைப்புகளாகும்.",
        "River Boards are not judicial tribunals; water dispute tribunals are under the IRWD Act.", "நதி வாரியங்கள் நீதித்துறை தீர்ப்பாயங்கள் அல்ல; அவை IRWD சட்டத்தின் கீழ் வருகின்றன.",
        "River Boards are purely advisory bodies.", "நதி வாரியங்கள் முற்றிலும் ஆலோசனை வழங்கும் அமைப்புகளாகும்.",
        "River Boards are statutory under an Act of 1956, not constitutional councils.", "நதி வாரியங்கள் 1956 சட்டத்தின் கீழான சட்டப்பூர்வ அமைப்புகள், அரசியலமைப்பு அமைப்புகள் அல்ல.",
        "They are not benches of any High Court.", "அவை எந்த உயர் நீதிமன்றத்தின் அமர்வுகளும் அல்ல.",
        "Crucial Fact: In practice, not a single River Board has ever been established under the River Boards Act, 1956.",
        "முக்கிய உண்மை: நடைமுறையில், 1956 ஆம் ஆண்டின் நதி வாரியங்கள் சட்டத்தின் கீழ் இதுவரை ஒரு நதி வாரியம் கூட அமைக்கப்படவில்லை.",
        "River Boards are advisory bodies under the 1956 Act.",
        "நதி வாரியங்கள் 1956 சட்டத்தின் கீழ் ஆலோசனை அமைப்புகளாகும்.",
        tags=["River Boards Act 1956", "Advisory Body"]
    ))

    # 031 - Ans C
    q.append(make_q(
        "ISR_E_031", "Direct Factual",
        "In which year was the first water disputes tribunal (the Krishna Water Disputes Tribunal I) constituted under the IRWD Act, 1956?",
        "1956 ஆம் ஆண்டின் IRWD சட்டத்தின் கீழ் முதல் நதிநீர் தகராறுகள் தீர்ப்பாயம் (கிருஷ்ணா நதிநீர் தகராறுகள் தீர்ப்பாயம் I) எந்த ஆண்டில் அமைக்கப்பட்டது?",
        "1956", "1956",
        "1962", "1962",
        "1969", "1969",
        "1975", "1975",
        "C",
        "The first water disputes tribunals under the 1956 Act—the Krishna Water Disputes Tribunal and the Godavari Water Disputes Tribunal—were both constituted in April 1969.",
        "1956 சட்டத்தின் கீழ் முதலாவது நதிநீர் தகராறுகள் தீர்ப்பாயங்களான கிருஷ்ணா நதிநீர் தீர்ப்பாயம் மற்றும் கோதாவரி நதிநீர் தீர்ப்பாயம் ஆகிய இரண்டும் 1969 ஏப்ரலில் அமைக்கப்பட்டன.",
        "1956 was the year the Act was enacted, but the first tribunal was constituted in 1969.", "1956 என்பது சட்டம் இயற்றப்பட்ட ஆண்டு, ஆனால் முதல் தீர்ப்பாயம் 1969-ல் அமைக்கப்பட்டது.",
        "1962 is incorrect.", "1962 தவறானது.",
        "1969 is the year Krishna and Godavari water tribunals were set up under Justice R.S. Bachawat.", "1969 என்பது நீதிபதி ஆர்.எஸ். பச்சாவத் தலைமையில் கிருஷ்ணா மற்றும் கோதாவரி தீர்ப்பாயங்கள் அமைக்கப்பட்ட ஆண்டாகும்.",
        "1975 was the year the Godavari agreement was entered.", "1975 என்பது கோதாவரி ஒப்பந்தம் எட்டப்பட்ட ஆண்டாகும்.",
        "The Krishna Tribunal I and Godavari Tribunal were both constituted in 1969 under Justice Bachawat.",
        "கிருஷ்ணா தீர்ப்பாயம் I மற்றும் கோதாவரி தீர்ப்பாயம் இரண்டும் 1969 இல் நீதிபதி பச்சாவத் தலைமையில் அமைக்கப்பட்டன.",
        "First Water Disputes Tribunal was constituted in 1969.",
        "முதல் நதிநீர் தகராறுகள் தீர்ப்பாயம் 1969 இல் அமைக்கப்பட்டது.",
        tags=["Krishna Tribunal", "IRWD Act 1956", "1969"]
    ))

    # 032 - Ans D
    q.append(make_q(
        "ISR_E_032", "Direct Factual",
        "The Narmada Water Disputes Tribunal constituted in 1969 was established to adjudicate water sharing disputes among which group of States?",
        "1969-ல் அமைக்கப்பட்ட நர்மதா நதிநீர் தகராறுகள் தீர்ப்பாயம் எந்த மாநிலக் குழுக்களுக்கிடையேயான நீர் பகிர்வு தகராறுகளைத் தீர்க்க நிறுவப்பட்டது?",
        "Maharashtra, Karnataka, and Andhra Pradesh", "மகாராஷ்டிரா, கர்நாடகா மற்றும் ஆந்திரப் பிரதேசம்",
        "Punjab, Haryana, and Rajasthan", "பஞ்சாப், ஹரியானா மற்றும் ராஜஸ்தான்",
        "Tamil Nadu, Karnataka, and Kerala", "தமிழ்நாடு, கர்நாடகா மற்றும் கேரளா",
        "Gujarat, Madhya Pradesh, Maharashtra, and Rajasthan", "குஜராத், மத்தியப் பிரதேசம், மகாராஷ்டிரா மற்றும் ராஜஸ்தான்",
        "D",
        "The Narmada Water Disputes Tribunal (headed by Justice V. Ramaswami) was constituted in 1969 to resolve disputes among Gujarat, Madhya Pradesh, Maharashtra, and Rajasthan.",
        "1969-ல் அமைக்கப்பட்ட நர்மதா நதிநீர் தகராறுகள் தீர்ப்பாயம் (நீதிபதி வி. ராமசுவாமி தலைமையில்) குஜராத், மத்தியப் பிரதேசம், மகாராஷ்டிரா மற்றும் ராஜஸ்தான் ஆகிய மாநிலங்களுக்கிடையேயான தகராறுகளைத் தீர்க்க அமைக்கப்பட்டது.",
        "Maharashtra, Karnataka, and Andhra Pradesh were parties to the Krishna Tribunal.", "மகாராஷ்டிரா, கர்நாடகா மற்றும் ஆந்திரா ஆகியவை கிருஷ்ணா தீர்ப்பாயத்தின் தரப்பினராக இருந்தன.",
        "Punjab, Haryana, and Rajasthan were parties to the Ravi-Beas Tribunal.", "பஞ்சாப், ஹரியானா மற்றும் ராஜஸ்தான் ஆகியவை ராவி-பியாஸ் தீர்ப்பாயத்தின் தரப்பினராக இருந்தன.",
        "Tamil Nadu, Karnataka, and Kerala were parties to the Cauvery Tribunal.", "தமிழ்நாடு, கர்நாடகா மற்றும் கேரளா ஆகியவை காவிரி தீர்ப்பாயத்தின் தரப்பினராக இருந்தன.",
        "Narmada dispute involved Gujarat, MP, Maharashtra, and Rajasthan.", "நர்மதா தகராறில் குஜராத், மத்தியப் பிரதேசம், மகாராஷ்டிரா மற்றும் ராஜஸ்தான் ஆகியவை ஈடுபட்டன.",
        "Narmada river basin states involved in the 1969 tribunal: Gujarat, MP, Maharashtra, and Rajasthan.",
        "1969 நர்மதா தீர்ப்பாயத்தில் தொடர்புடைய நதிப் படுகை மாநிலங்கள்: குஜராத், ம.பி, மகாராஷ்டிரா மற்றும் ராஜஸ்தான்.",
        "Narmada Tribunal states = Gujarat, MP, Maharashtra, Rajasthan.",
        "நர்மதா தீர்ப்பாய மாநிலங்கள் = குஜராத், ம.பி, மகாராஷ்டிரா, ராஜஸ்தான்.",
        tags=["Narmada Tribunal", "River Basin States"]
    ))

    # 033 - Ans A
    q.append(make_q(
        "ISR_E_033", "Direct Factual",
        "In which year was the Cauvery Water Disputes Tribunal (CWDT) constituted by the Central Government following a direction from the Supreme Court?",
        "உச்ச நீதிமன்றத்தின் உத்தரவைத் தொடர்ந்து மத்திய அரசால் காவிரி நதிநீர் தகராறுகள் தீர்ப்பாயம் (CWDT) எந்த ஆண்டில் அமைக்கப்பட்டது?",
        "1990", "1990",
        "1980", "1980",
        "1974", "1974",
        "2007", "2007",
        "A",
        "The Cauvery Water Disputes Tribunal (CWDT) was constituted by the Central Government on 2 June 1990 under the Chairmanship of Justice Chittatosh Mookerjee following Supreme Court directions.",
        "உச்ச நீதிமன்ற உத்தரவுகளைத் தொடர்ந்து 1990 ஜூன் 2 அன்று மத்திய அரசால் நீதிபதி சிட்டாடோஷ் முகர்ஜி தலைமையில் காவிரி நதிநீர் தகராறுகள் தீர்ப்பாயம் (CWDT) அமைக்கப்பட்டது.",
        "1990 is the exact year CWDT was constituted.", "1990 என்பது CWDT அமைக்கப்பட்ட சரியான ஆண்டாகும்.",
        "1980 is incorrect.", "1980 தவறானது.",
        "1974 was the year when the 1924 agreement's 50-year period lapsed.", "1974 என்பது 1924 ஒப்பந்தத்தின் 50 ஆண்டு காலம் முடிவடைந்த ஆண்டாகும்.",
        "2007 was the year the final award was pronounced by CWDT, not its constitution.", "2007 என்பது CWDT இறுதித் தீர்ப்பை வழங்கிய ஆண்டாகும், அது அமைக்கப்பட்ட ஆண்டு அல்ல.",
        "TNPSC Focus: CWDT was constituted on 2 June 1990; final award given in February 2007.",
        "TNPSC முக்கியத்துவம்: CWDT 1990 ஜூன் 2 அன்று அமைக்கப்பட்டது; இறுதித் தீர்ப்பு 2007 பிப்ரவரியில் வழங்கப்பட்டது.",
        "Cauvery Water Disputes Tribunal constituted in 1990.",
        "காவிரி நதிநீர் தகராறுகள் தீர்ப்பாயம் 1990 இல் அமைக்கப்பட்டது.",
        tags=["Cauvery Tribunal", "1990", "CWDT"]
    ))

    # 034 - Ans B
    q.append(make_q(
        "ISR_E_034", "Direct Factual",
        "How many Union Cabinet Ministers are nominated by the Prime Minister to serve as members of the Inter-State Council?",
        "மாநிலங்களுக்கு இடையிலான மன்றத்தின் உறுப்பினர்களாகப் பணியாற்ற பிரதம அமைச்சரால் எத்தனை மத்திய அமைச்சரவை அமைச்சர்கள் நியமிக்கப்படுகிறார்கள்?",
        "4", "4",
        "6", "6",
        "8", "8",
        "10", "10",
        "B",
        "The composition of the Inter-State Council includes six Union Cabinet Ministers nominated by the Prime Minister, in addition to all State Chief Ministers and UT administrators.",
        "மாநிலங்களுக்கு இடையிலான மன்றத்தின் அமைப்பில் அனைத்து மாநில முதல்வர்கள் மற்றும் யூனியன் பிரதேச நிர்வாகிகளுடன் கூடுதலாக பிரதம அமைச்சரால் பரிந்துரைக்கப்படும் ஆறு மத்திய அமைச்சரவை அமைச்சர்கள் அடங்குவர்.",
        "Four is incorrect.", "நான்கு தவறானது.",
        "Six Union Cabinet Ministers are nominated as members by the Prime Minister.", "ஆறு மத்திய அமைச்சரவை அமைச்சர்கள் பிரதம அமைச்சரால் உறுப்பினர்களாக நியமிக்கப்படுகின்றனர்.",
        "Eight is incorrect.", "எட்டு தவறானது.",
        "Ten is incorrect.", "பத்து தவறானது.",
        "Composition: PM (Chairman) + All State CMs + CMs of UTs with Assemblies + Administrators of other UTs + 6 Union Cabinet Ministers.",
        "அமைப்பு: பிரதமர் (தலைவர்) + அனைத்து மாநில முதல்வர்கள் + சட்டமன்றம் கொண்ட யூ.பி முதல்வர்கள் + பிற யூ.பி நிர்வாகிகள் + 6 மத்திய அமைச்சரவை அமைச்சர்கள்.",
        "6 Union Cabinet Ministers are members of the Inter-State Council.",
        "6 மத்திய அமைச்சரவை அமைச்சர்கள் மாநிலங்களுக்கு இடையிலான மன்றத்தின் உறுப்பினர்கள் ஆவர்.",
        tags=["Inter-State Council", "Composition"]
    ))

    # 035 - Ans C
    q.append(make_q(
        "ISR_E_035", "Direct Factual",
        "In which year was the Standing Committee of the Inter-State Council formally constituted to ensure continuous consultation among the federal partners?",
        "கூட்டாட்சிப் பங்காளிகளிடையே தொடர்ச்சியான ஆலோசனையை உறுதி செய்வதற்காக மாநிலங்களுக்கு இடையிலான மன்றத்தின் நிலைக் குழு எந்த ஆண்டில் முறைப்படி அமைக்கப்பட்டது?",
        "1990", "1990",
        "1992", "1992",
        "1996", "1996",
        "2000", "2000",
        "C",
        "The Standing Committee of the Inter-State Council was constituted in 1996 for continuous consultation and processing of matters before consideration by the full Council.",
        "முழு மன்றத்தின் பரிசீலனைக்கு முன்னதாக தொடர்ச்சியான ஆலோசனை மற்றும் விஷயங்களை ஒழுங்குபடுத்துவதற்காக 1996 ஆம் ஆண்டில் மாநிலங்களுக்கு இடையிலான மன்றத்தின் நிலைக் குழு அமைக்கப்பட்டது.",
        "1990 was the year the main Inter-State Council was established.", "1990 என்பது பிரதான மாநிலங்களுக்கு இடையிலான மன்றம் அமைக்கப்பட்ட ஆண்டாகும்.",
        "1992 is incorrect.", "1992 தவறானது.",
        "1996 is the exact year the Standing Committee was constituted.", "1996 என்பது நிலைக் குழு அமைக்கப்பட்ட சரியான ஆண்டாகும்.",
        "2000 is incorrect.", "2000 தவறானது.",
        "The Standing Committee of the Inter-State Council was established in 1996.",
        "மாநிலங்களுக்கு இடையிலான மன்றத்தின் நிலைக் குழு 1996 இல் நிறுவப்பட்டது.",
        "Standing Committee of ISC was set up in 1996.",
        "ISC-ன் நிலைக் குழு 1996 இல் அமைக்கப்பட்டது.",
        tags=["Standing Committee", "Inter-State Council", "1996"]
    ))

    # 036 - Ans D
    q.append(make_q(
        "ISR_E_036", "Direct Factual",
        "Who presides as the Chairman of the Standing Committee of the Inter-State Council?",
        "மாநிலங்களுக்கு இடையிலான மன்றத்தின் நிலைக் குழுவின் தலைவராகத் தலைமை தாங்குபவர் யார்?",
        "The Prime Minister of India", "இந்தியப் பிரதம அமைச்சர்",
        "The Cabinet Secretary", "மத்திய அமைச்சரவைச் செயலாளர்",
        "The Deputy Chairman of NITI Aayog", "நிதி ஆயோக்கின் துணைத் தலைவர்",
        "The Union Home Minister", "மத்திய உள்துறை அமைச்சர்",
        "D",
        "The Union Home Minister is the Chairman of the Standing Committee of the Inter-State Council. The committee also consists of five Union Cabinet Ministers and nine Chief Ministers.",
        "மத்திய உள்துறை அமைச்சர் மாநிலங்களுக்கு இடையிலான மன்றத்தின் நிலைக் குழுவின் தலைவர் ஆவார். இக்குழுவில் ஐந்து மத்திய அமைச்சரவை அமைச்சர்கள் மற்றும் ஒன்பது முதலமைச்சர்களும் உள்ளனர்.",
        "The Prime Minister chairs the full Council, but the Home Minister chairs the Standing Committee.", "பிரதமர் முழு மன்றத்திற்குத் தலைமை தாங்குகிறார், ஆனால் உள்துறை அமைச்சர் நிலைக் குழுவிற்குத் தலைமை தாங்குகிறார்.",
        "The Cabinet Secretary is a civil servant, not the chairman.", "அமைச்சரவைச் செயலாளர் அரசு ஊழியர், தலைவர் அல்ல.",
        "NITI Aayog Deputy Chairman has no role as chairman of this committee.", "நிதி ஆயோக் துணைத் தலைவருக்கு இக்குழுவின் தலைவராக எந்தப் பங்கும் இல்லை.",
        "The Union Home Minister is the Chairman of the Standing Committee.", "மத்திய உள்துறை அமைச்சரே நிலைக் குழுவின் தலைவர் ஆவார்.",
        "Trap: Inter-State Council = Chaired by PM; Standing Committee of ISC = Chaired by Home Minister.",
        "பொறி: மாநிலங்களுக்கு இடையிலான மன்றம் = பிரதமர் தலைமை; அதன் நிலைக் குழு = உள்துறை அமைச்சர் தலைமை.",
        "Union Home Minister chairs the Standing Committee of the Inter-State Council.",
        "மத்திய உள்துறை அமைச்சர் மாநிலங்களுக்கு இடையிலான மன்றத்தின் நிலைக் குழுவிற்குத் தலைமை தாங்குகிறார்.",
        tags=["Standing Committee", "Union Home Minister"]
    ))

    # 037 - Ans A
    q.append(make_q(
        "ISR_E_037", "Direct Factual",
        "According to the 1990 Presidential Order, how many times in a year is the Inter-State Council mandated to meet at a minimum?",
        "1990 ஆம் ஆண்டின் குடியரசுத் தலைவர் ஆணையின்படி, மாநிலங்களுக்கு இடையிலான மன்றம் ஒரு ஆண்டில் குறைந்தபட்சம் எத்தனை முறை கூட வேண்டும் என்று கட்டாயப்படுத்தப்பட்டுள்ளது?",
        "At least thrice a year", "ஆண்டிற்கு குறைந்தது மூன்று முறை",
        "At least twice a year", "ஆண்டிற்கு குறைந்தது இரண்டு முறை",
        "At least four times a year", "ஆண்டிற்கு குறைந்தது நான்கு முறை",
        "At least once a year", "ஆண்டிற்கு குறைந்தது ஒரு முறை",
        "A",
        "The 1990 Presidential Order mandates that the Inter-State Council shall meet at least thrice in a year, and its meetings shall be held in camera.",
        "1990 குடியரசுத் தலைவர் ஆணை, மாநிலங்களுக்கு இடையிலான மன்றம் ஒரு ஆண்டில் குறைந்தது மூன்று முறை கூட வேண்டும் என்றும், அதன் கூட்டங்கள் இரகசியமாக நடத்தப்பட வேண்டும் என்றும் கட்டாயப்படுத்துகிறது.",
        "At least thrice a year is the explicit requirement of the 1990 Order.", "ஆண்டிற்கு குறைந்தது மூன்று முறை என்பது 1990 ஆணையின் வெளிப்படையான தேவையாகும்.",
        "Twice a year is incorrect.", "ஆண்டிற்கு இரண்டு முறை என்பது தவறானது.",
        "Four times a year is incorrect.", "ஆண்டிற்கு நான்கு முறை என்பது தவறானது.",
        "Once a year is incorrect.", "ஆண்டிற்கு ஒரு முறை என்பது தவறானது.",
        "The Punchhi Commission (2010) also emphasized following the mandate of meeting 3 times a year.",
        "பூஞ்சி ஆணையமும் (2010) ஆண்டில் 3 முறை கூடும் ஆணையைப் பின்பற்றுவதை வலியுறுத்தியது.",
        "Inter-State Council mandated to meet at least thrice a year.",
        "மாநிலங்களுக்கு இடையிலான மன்றம் ஆண்டில் குறைந்தது மூன்று முறை கூட வேண்டும்.",
        tags=["Inter-State Council", "Meetings Frequency"]
    ))

    # 038 - Ans B
    q.append(make_q(
        "ISR_E_038", "Direct Factual",
        "Where is the headquarters of the Eastern Zonal Council located?",
        "கிழக்கு மண்டலக் குழுவின் தலைமையகம் எங்கு அமைந்துள்ளது?",
        "Bhubaneswar", "புவனேஸ்வர்",
        "Kolkata", "கொல்கத்தா",
        "Patna", "பாட்னா",
        "Ranchi", "ராஞ்சி",
        "B",
        "The headquarters of the Eastern Zonal Council is located at Kolkata. The Eastern Zone includes the States of Bihar, Jharkhand, Odisha, and West Bengal.",
        "கிழக்கு மண்டலக் குழுவின் தலைமையகம் கொல்கத்தாவில் அமைந்துள்ளது. கிழக்கு மண்டலத்தில் பீகார், ஜார்க்கண்ட், ஒடிசா மற்றும் மேற்கு வங்காளம் ஆகிய மாநிலங்கள் அடங்கும்.",
        "Bhubaneswar is the capital of Odisha, not the Zonal HQ.", "புவனேஸ்வர் ஒடிசாவின் தலைநகரம், தலைமையகம் அல்ல.",
        "Kolkata is the official headquarters of the Eastern Zonal Council.", "கொல்கத்தா கிழக்கு மண்டலக் குழுவின் அதிகாரப்பூர்வ தலைமையகம் ஆகும்.",
        "Patna is the capital of Bihar, not the Zonal HQ.", "பாட்னா பீகாரின் தலைநகரம், தலைமையகம் அல்ல.",
        "Ranchi is the capital of Jharkhand, not the Zonal HQ.", "ராஞ்சி ஜார்க்கண்டின் தலைநகரம், தலைமையகம் அல்ல.",
        "Eastern Zonal Council covers West Bengal, Bihar, Jharkhand, Odisha; HQ is Kolkata.",
        "கிழக்கு மண்டலக் குழு மேற்கு வங்கம், பீகார், ஜார்க்கண்ட், ஒடிசா ஆகியவற்றை உள்ளடக்கியது; தலைமையகம் கொல்கத்தா.",
        "Eastern Zonal Council headquarters = Kolkata.",
        "கிழக்கு மண்டலக் குழு தலைமையகம் = கொல்கத்தா.",
        tags=["Eastern Zonal Council", "Headquarters"]
    ))

    # 039 - Ans C
    q.append(make_q(
        "ISR_E_039", "Direct Factual",
        "Where is the permanent headquarters of the Western Zonal Council located?",
        "மேற்கு மண்டலக் குழுவின் நிரந்தரத் தலைமையகம் எங்கு அமைந்துள்ளது?",
        "Gandhinagar", "காந்திநகர்",
        "Panaji", "பனாஜி",
        "Mumbai", "மும்பை",
        "Ahmedabad", "அகமதாபாத்",
        "C",
        "The headquarters of the Western Zonal Council is located at Mumbai. The Western Zone comprises Goa, Gujarat, Maharashtra, and the Union Territory of Dadra and Nagar Haveli and Daman and Diu.",
        "மேற்கு மண்டலக் குழுவின் தலைமையகம் மும்பையில் அமைந்துள்ளது. மேற்கு மண்டலத்தில் கோவா, குஜராத், மகாராஷ்டிரா மற்றும் தாத்ரா & நகர் ஹவேலி மற்றும் தாமன் & டையூ யூனியன் பிரதேசம் ஆகியவை அடங்கும்.",
        "Gandhinagar is the capital of Gujarat, not the Zonal HQ.", "காந்திநகர் குஜராத்தின் தலைநகரம், தலைமையகம் அல்ல.",
        "Panaji is the capital of Goa, not the Zonal HQ.", "பனாஜி கோவாவின் தலைநகரம், தலைமையகம் அல்ல.",
        "Mumbai is the designated headquarters of the Western Zonal Council.", "மும்பை மேற்கு மண்டலக் குழுவின் நியமிக்கப்பட்ட தலைமையகம் ஆகும்.",
        "Ahmedabad is a major city in Gujarat, not the HQ.", "அகமதாபாத் குஜராத்தின் முக்கிய நகரம், தலைமையகம் அல்ல.",
        "Western Zonal Council includes Maharashtra, Gujarat, Goa, DNH & DD; HQ is Mumbai.",
        "மேற்கு மண்டலக் குழுவில் மகாராஷ்டிரா, குஜராத், கோவா, தாத்ரா & தாமன் ஆகியவை உள்ளன; தலைமையகம் மும்பை.",
        "Western Zonal Council headquarters = Mumbai.",
        "மேற்கு மண்டலக் குழு தலைமையகம் = மும்பை.",
        tags=["Western Zonal Council", "Headquarters"]
    ))

    # 040 - Ans D
    q.append(make_q(
        "ISR_E_040", "Direct Factual",
        "Where is the permanent headquarters of the Northern Zonal Council located?",
        "வடக்கு மண்டலக் குழுவின் நிரந்தரத் தலைமையகம் எங்கு அமைந்துள்ளது?",
        "Chandigarh", "சண்டிகர்",
        "Jaipur", "ஜெய்ப்பூர்",
        "Shimla", "சிம்லா",
        "New Delhi", "புது தில்லி",
        "D",
        "The headquarters of the Northern Zonal Council is located at New Delhi. The Northern Zone comprises Haryana, Himachal Pradesh, Jammu and Kashmir, Punjab, Rajasthan, NCT of Delhi, Chandigarh, and Ladakh.",
        "வடக்கு மண்டலக் குழுவின் தலைமையகம் புது தில்லியில் அமைந்துள்ளது. வடக்கு மண்டலத்தில் ஹரியானா, இமாச்சலப் பிரதேசம், ஜம்மு-காஷ்மீர், பஞ்சாப், ராஜஸ்தான், தில்லி, சண்டிகர் மற்றும் லடாக் ஆகியவை அடங்கும்.",
        "Chandigarh is a member UT/capital, not the headquarters.", "சண்டிகர் ஓர் உறுப்பினர் பகுதி, தலைமையகம் அல்ல.",
        "Jaipur is the capital of Rajasthan, not the headquarters.", "ஜெய்ப்பூர் ராஜஸ்தானின் தலைநகரம், தலைமையகம் அல்ல.",
        "Shimla is the capital of HP, not the headquarters.", "சிம்லா இமாச்சலப் பிரதேசத்தின் தலைநகரம், தலைமையகம் அல்ல.",
        "New Delhi is the official headquarters of the Northern Zonal Council.", "புது தில்லி வடக்கு மண்டலக் குழுவின் அதிகாரப்பூர்வ தலைமையகம் ஆகும்.",
        "Northern Zonal Council covers Haryana, HP, J&K, Ladakh, Punjab, Rajasthan, Delhi, Chandigarh; HQ is New Delhi.",
        "வடக்கு மண்டலக் குழு ஹரியானா, இ.பி, ஜம்மு-காஷ்மீர், லடாக், பஞ்சாப், ராஜஸ்தான், தில்லி, சண்டிகர் ஆகியவற்றை உள்ளடக்கியது; தலைமையகம் புது தில்லி.",
        "Northern Zonal Council headquarters = New Delhi.",
        "வடக்கு மண்டலக் குழு தலைமையகம் = புது தில்லி.",
        tags=["Northern Zonal Council", "Headquarters"]
    ))

    # 041 - Ans A
    q.append(make_q(
        "ISR_E_041", "Direct Factual",
        "Which of the following Union Territories is an official member of the Southern Zonal Council?",
        "பின்வரும் யூனியன் பிரதேசங்களில் எது தென் மண்டலக் குழுவின் அதிகாரப்பூர்வ உறுப்பினராக உள்ளது?",
        "Puducherry", "புதுச்சேரி",
        "Lakshadweep", "லட்சத்தீவு",
        "Andaman and Nicobar Islands", "அந்தமான் மற்றும் நிக்கோபார் தீவுகள்",
        "Dadra and Nagar Haveli", "தாத்ரா மற்றும் நகர் ஹவேலி",
        "A",
        "Puducherry is an official member of the Southern Zonal Council along with Andhra Pradesh, Karnataka, Kerala, Tamil Nadu, and Telangana. (Andaman & Nicobar Islands and Lakshadweep are not members of any Zonal Council).",
        "ஆந்திரா, கர்நாடகா, கேரளா, தமிழ்நாடு மற்றும் தெலுங்கானா ஆகியவற்றுடன் புதுச்சேரி தென் மண்டலக் குழுவின் அதிகாரப்பூர்வ உறுப்பினராக உள்ளது. (அந்தமான் & நிக்கோபார் மற்றும் லட்சத்தீவு எந்த மண்டலக் குழுவிலும் உறுப்பினர்கள் அல்ல).",
        "Puducherry is the member UT in the Southern Zone.", "புதுச்சேரி தென் மண்டலத்தின் உறுப்பினர் யூனியன் பிரதேசம் ஆகும்.",
        "Lakshadweep is not a member of any Zonal Council, though it may be an invitee.", "லட்சத்தீவு எந்த மண்டலக் குழுவிலும் உறுப்பினர் அல்ல.",
        "Andaman and Nicobar Islands is not a regular member of any Zonal Council.", "அந்தமான் நிக்கோபார் தீவுகள் எந்த மண்டலக் குழுவிலும் வழக்கமான உறுப்பினர் அல்ல.",
        "Dadra and Nagar Haveli is a member of the Western Zonal Council.", "தாத்ரா மற்றும் நகர் ஹவேலி மேற்கு மண்டலக் குழுவின் உறுப்பினர் ஆகும்.",
        "Southern Zonal Council: Andhra Pradesh, Karnataka, Kerala, Tamil Nadu, Telangana, Puducherry.",
        "தென் மண்டலக் குழு: ஆந்திரப் பிரதேசம், கர்நாடகா, கேரளா, தமிழ்நாடு, தெலுங்கானா, புதுச்சேரி.",
        "Puducherry is part of the Southern Zonal Council.",
        "புதுச்சேரி தென் மண்டலக் குழுவின் ஒரு பகுதியாகும்.",
        tags=["Southern Zonal Council", "Puducherry"]
    ))

    # 042 - Ans B
    q.append(make_q(
        "ISR_E_042", "Direct Factual",
        "By what method or principle are decisions primarily arrived at during the meetings of the Inter-State Council?",
        "மாநிலங்களுக்கு இடையிலான மன்றத்தின் கூட்டங்களின் போது முடிவுகள் முக்கியமாக எந்த முறை அல்லது கொள்கையின் மூலம் எட்டப்படுகின்றன?",
        "Simple majority voting", "சாதாரண பெரும்பான்மை வாக்குப்பதிவு",
        "Consensus", "ஒருமித்த கருத்து (Consensus)",
        "Two-thirds weighted majority", "மூன்றில் இரண்டு பங்கு எடையிடப்பட்ட பெரும்பான்மை",
        "Unilateral decision of the Chairman", "தலைவரின் ஒருதலைப்பட்ச முடிவு",
        "B",
        "Under the procedural rules governing the Inter-State Council, all questions are decided by consensus, reflecting the cooperative federal nature of the body.",
        "மாநிலங்களுக்கு இடையிலான மன்றத்தை ஒழுங்குபடுத்தும் நடைமுறை விதிகளின் கீழ், அனைத்து விவகாரங்களும் கூட்டாட்சித் தன்மையைப் பிரதிபலிக்கும் வகையில் 'ஒருமித்த கருத்து' (Consensus) மூலமே தீர்மானிக்கப்படுகின்றன.",
        "Voting is not used; decisions are taken by consensus.", "வாக்கெடுப்பு பயன்படுத்தப்படுவதில்லை; முடிவுகள் ஒருமித்த கருத்து மூலம் எடுக்கப்படுகின்றன.",
        "Consensus is the established decision-making mechanism in the Inter-State Council.", "ஒருமித்த கருத்து என்பது மாநிலங்களுக்கு இடையிலான மன்றத்தில் நிறுவப்பட்ட முடிவெடுக்கும் முறையாகும்.",
        "Two-thirds weighted majority is characteristic of the GST Council, not the Inter-State Council.", "மூன்றில் இரண்டு பங்கு எடையிடப்பட்ட பெரும்பான்மை ஜிஎஸ்டி கவுன்சிலுக்குரியது, இம்மன்றத்திற்கு அல்ல.",
        "The Chairman cannot unilaterally impose decisions; consensus of members is sought.", "தலைவர் ஒருதலைப்பட்சமாக முடிவுகளைத் திணிக்க முடியாது; உறுப்பினர்களின் ஒருமித்த கருத்து பெறப்படுகிறது.",
        "Contrast: Inter-State Council = Consensus; GST Council = 3/4th weighted majority voting.",
        "வேறுபாடு: மாநிலங்களுக்கு இடையிலான மன்றம் = ஒருமித்த கருத்து; ஜிஎஸ்டி கவுன்சில் = 3/4 பங்கு எடையிடப்பட்ட வாக்குப்பதிவு.",
        "Decisions in the Inter-State Council are arrived at by consensus.",
        "மாநிலங்களுக்கு இடையிலான மன்றத்தில் முடிவுகள் ஒருமித்த கருத்து மூலம் எட்டப்படுகின்றன.",
        tags=["Inter-State Council", "Consensus"]
    ))

    # 043 - Ans C
    q.append(make_q(
        "ISR_E_043", "Direct Factual",
        "The constitutional guarantee of freedom of trade, commerce, and intercourse in Article 301 was largely inspired by the Constitution of which country?",
        "உறுப்பு 301-ல் உள்ள வர்த்தகம், வாணிபம் மற்றும் தொடர்பின் சுதந்திரம் குறித்த அரசியலமைப்பு உத்தரவாதம் பெருமளவில் எந்த நாட்டின் அரசியலமைப்பால் ஈர்க்கப்பட்டது?",
        "United States of America", "அமெரிக்க ஐக்கிய நாடுகள்",
        "Canada", "கனடா",
        "Australia", "ஆஸ்திரேலியா",
        "South Africa", "தென்னாப்பிரிக்கா",
        "C",
        "Article 301 of the Indian Constitution was inspired by Section 92 of the Australian Constitution, which provides that trade, commerce, and intercourse among the States shall be absolutely free.",
        "இந்திய அரசியலமைப்பின் உறுப்பு 301, மாநிலங்களுக்கிடையேயான வர்த்தகம், வாணிபம் மற்றும் தொடர்பு முற்றிலும் சுதந்திரமாக இருக்க வேண்டும் என்று கூறும் ஆஸ்திரேலிய அரசியலமைப்பின் பிரிவு 92-ஆல் ஈர்க்கப்பட்டது.",
        "The US Commerce Clause (Article I, Section 8) grants federal power, but Art 301 phrasing mirrors Australia Section 92.", "அமெரிக்க வர்த்தக விதி கூட்டாட்சி அதிகாரத்தை அளிக்கிறது, ஆனால் உறுப்பு 301 ஆஸ்திரேலிய விதியைப் போன்றது.",
        "Canada uses different language in the BNA Act 1867.", "கனடா வேறுபட்ட சொல்லாடலைப் பயன்படுத்துகிறது.",
        "Australia Section 92 provided the exact model for Article 301.", "ஆஸ்திரேலியாவின் பிரிவு 92 உறுப்பு 301-க்கு துல்லியமான முன்மாதிரியை வழங்கியது.",
        "South Africa's constitution was not the source for Part XIII.", "தென்னாப்பிரிக்க அரசியலமைப்பு பகுதி XIII-ன் மூலம் அல்ல.",
        "Source of Art 301: Section 92 of the Australian Constitution ('trade, commerce, and intercourse... shall be free').",
        "உறுப்பு 301-ன் ஆதாரம்: ஆஸ்திரேலிய அரசியலமைப்பின் பிரிவு 92 ('வர்த்தகம், வாணிபம் மற்றும் தொடர்பு... சுதந்திரமாக இருக்க வேண்டும்').",
        "Article 301 was inspired by the Australian Constitution.",
        "உறுப்பு 301 ஆஸ்திரேலிய அரசியலமைப்பால் ஈர்க்கப்பட்டது.",
        tags=["Article 301", "Australian Constitution"]
    ))

    # 044 - Ans D
    q.append(make_q(
        "ISR_E_044", "Direct Factual",
        "Which Article of the Constitution saves existing pre-constitutional laws and laws providing for State monopolies from being invalidated by Article 301?",
        "அரசியலமைப்பு நடைமுறைக்கு வருவதற்கு முந்தைய சட்டங்களையும், அரசு ஏகபோகங்களை வழங்கும் சட்டங்களையும் உறுப்பு 301-ஆல் செல்லாததாக்கப்படுவதிலிருந்து பாதுகாக்கும் அரசியலமைப்பு உறுப்பு எது?",
        "Article 301", "உறுப்பு 301",
        "Article 302", "உறுப்பு 302",
        "Article 304", "உறுப்பு 304",
        "Article 305", "உறுப்பு 305",
        "D",
        "Article 305 saves existing laws (laws in force before the commencement of the Constitution) and laws providing for State monopolies from the operation of Articles 301 and 303.",
        "உறுப்பு 305, நடைமுறையிலுள்ள சட்டங்களையும் (அரசியலமைப்பு தொடங்குவதற்கு முன் நடைமுறையில் இருந்தவை), அரசு ஏகபோகங்களை வழங்கும் சட்டங்களையும் உறுப்புகள் 301 மற்றும் 303-ன் செயல்பாட்டிலிருந்து பாதுகாக்கிறது.",
        "Article 301 is the general freedom clause.", "உறுப்பு 301 பொது சுதந்திர விதியாகும்.",
        "Article 302 permits Parliamentary restrictions.", "உறுப்பு 302 நாடாளுமன்றக் கட்டுப்பாடுகளை அனுமதிக்கிறது.",
        "Article 304 permits State restrictions.", "உறுப்பு 304 மாநிலக் கட்டுப்பாடுகளை அனுமதிக்கிறது.",
        "Article 305 specifically saves existing laws and state monopolies.", "உறுப்பு 305 குறிப்பாக நடைமுறையிலுள்ள சட்டங்களையும் அரசு ஏகபோகங்களையும் பாதுகாக்கிறது.",
        "State monopolies created under Art 19(6)(ii) are saved from Art 301 challenge by Article 305.",
        "உறுப்பு 19(6)(ii)-ன் கீழ் உருவாக்கப்பட்ட அரசு ஏகபோகங்கள் உறுப்பு 305-ஆல் பாதுகாக்கப்படுகின்றன.",
        "Article 305 saves existing laws and state monopolies.",
        "உறுப்பு 305 நடைமுறையிலுள்ள சட்டங்களையும் அரசு ஏகபோகங்களையும் பாதுகாக்கிறது.",
        tags=["Article 305", "State Monopolies"]
    ))

    # 045 - Ans A
    q.append(make_q(
        "ISR_E_045", "Direct Factual",
        "Under the 2002 amendment to the Inter-State River Water Disputes Act 1956, within what timeframe must the Central Government refer a water dispute to a tribunal after receiving a request from a State?",
        "1956 ஆம் ஆண்டின் நதிநீர் தகராறுகள் சட்டத்தின் 2002 ஆம் ஆண்டு திருத்தத்தின்படி, ஒரு மாநிலத்திடமிருந்து கோரிக்கையைப் பெற்ற பிறகு மத்திய அரசு எந்தக் காலக்கெடுவிற்குள் நதிநீர் தகராறை ஒரு தீர்ப்பாயத்திற்கு அனுப்ப வேண்டும்?",
        "Within 1 year", "1 ஆண்டிற்குள்",
        "Within 2 years", "2 ஆண்டுகளுக்குள்",
        "Within 3 years", "3 ஆண்டுகளுக்குள்",
        "Within 6 months", "6 மாதங்களுக்குள்",
        "A",
        "The Inter-State Water Disputes (Amendment) Act 2002 mandated that if a dispute cannot be resolved through negotiations, the Central Government must refer it to a tribunal within one year of receiving the request.",
        "2002 ஆம் ஆண்டின் நதிநீர் தகராறுகள் திருத்தச் சட்டம், பேச்சுவார்த்தைகள் மூலம் தகராறைத் தீர்க்க முடியாவிட்டால், கோரிக்கையைப் பெற்ற ஒரு ஆண்டிற்குள் மத்திய அரசு அதை ஒரு தீர்ப்பாயத்திற்கு அனுப்ப வேண்டும் எனக் கட்டாயமாக்கியது.",
        "One year is the statutory deadline introduced by the 2002 amendment.", "ஒரு ஆண்டு என்பது 2002 திருத்தத்தால் அறிமுகப்படுத்தப்பட்ட சட்டப்பூர்வ காலக்கெடுவாகும்.",
        "Two years is incorrect.", "இரண்டு ஆண்டுகள் தவறானது.",
        "Three years is the time given to the tribunal to deliver its award, not for reference.", "மூன்று ஆண்டுகள் என்பது தீர்ப்பாயம் தீர்ப்பு வழங்குவதற்கான காலமாகும், பரிந்துரைப்பதற்கான காலம் அல்ல.",
        "Six months is incorrect.", "ஆறு மாதங்கள் தவறானது.",
        "2002 Amendment Timelines: 1 year for Central Govt to refer to tribunal; 3 years for tribunal to deliver award (+2 yrs extension).",
        "2002 திருத்தக் காலக்கெடு: தீர்ப்பாயத்திற்கு அனுப்ப மத்திய அரசுக்கு 1 ஆண்டு; தீர்ப்பளிக்க தீர்ப்பாயத்திற்கு 3 ஆண்டுகள் (+2 ஆண்டுகள் நீட்டிப்பு).",
        "Central Government must refer water dispute to tribunal within 1 year.",
        "மத்திய அரசு நதிநீர் தகராறை 1 ஆண்டிற்குள் தீர்ப்பாயத்திற்கு அனுப்ப வேண்டும்.",
        tags=["IRWD Act 2002 Amendment", "1 Year Deadline"]
    ))

    # 046 - Ans B
    q.append(make_q(
        "ISR_E_046", "Direct Factual",
        "Under the 2002 amendment to the IRWD Act, once the decision of a water dispute tribunal is published in the Official Gazette, it has the same force as what?",
        "IRWD சட்டத்தின் 2002 திருத்தத்தின் கீழ், நதிநீர் தகராறு தீர்ப்பாயத்தின் முடிவு அதிகாரப்பூர்வ அரசிதழில் வெளியிடப்பட்டவுடன், அது எதற்கு இணையான ஆற்றலைக் கொண்டுள்ளது?",
        "An Act of Parliament", "நாடாளுமன்றத்தின் ஒரு சட்டம்",
        "An order or decree of the Supreme Court", "உச்ச நீதிமன்றத்தின் ஆணை அல்லது தீர்ப்பாணை",
        "A constitutional amendment", "ஓர் அரசியலமைப்புத் திருத்தம்",
        "A policy resolution of the Inter-State Council", "மாநிலங்களுக்கு இடையிலான மன்றத்தின் ஒரு கொள்கைத் தீர்மானம்",
        "B",
        "Section 6(2) of the IRWD Act (inserted by the 2002 amendment) provides that upon publication in the Official Gazette, the decision of the Tribunal shall have the same force as an order or decree of the Supreme Court.",
        "IRWD சட்டத்தின் பிரிவு 6(2) (2002 திருத்தத்தால் சேர்க்கப்பட்டது), அதிகாரப்பூர்வ அரசிதழில் வெளியிடப்பட்டவுடன், தீர்ப்பாயத்தின் முடிவு உச்ச நீதிமன்றத்தின் ஆணை அல்லது தீர்ப்பாணைக்கு (order or decree of Supreme Court) இணையான அதே ஆற்றலைக் கொண்டிருக்கும் என்று கூறுகிறது.",
        "It has the force of an order/decree of the Supreme Court, not an Act of Parliament.", "இது உச்ச நீதிமன்றத்தின் ஆணைக்கு இணையானது, நாடாளுமன்றச் சட்டத்திற்கு இணையானது அல்ல.",
        "An order or decree of the Supreme Court is the exact statutory equivalence.", "உச்ச நீதிமன்றத்தின் ஆணை அல்லது தீர்ப்பாணை என்பது சரியான சட்டப்பூர்வ இணைப்பாகும்.",
        "It is not a constitutional amendment.", "இது அரசியலமைப்புத் திருத்தம் அல்ல.",
        "It is far superior to a mere policy resolution of the Inter-State Council.", "இது மாநிலங்களுக்கு இடையிலான மன்றத்தின் வெறும் தீர்மானத்தை விடப் பல மடங்கு உயர்ந்தது.",
        "Gazetted Water Dispute Award = Force of Supreme Court Order/Decree (Sec 6(2) IRWD Act).",
        "அரசிதழில் வெளியிடப்பட்ட நதிநீர் தீர்ப்பு = உச்ச நீதிமன்ற ஆணை/தீர்ப்பாணையின் ஆற்றல் கொண்டது.",
        "A gazetted tribunal award has the force of a Supreme Court decree.",
        "அரசிதழில் வெளியிடப்பட்ட தீர்ப்பாய முடிவு உச்ச நீதிமன்றத் தீர்ப்பாணையின் ஆற்றலைக் கொண்டுள்ளது.",
        tags=["Gazetted Award", "Supreme Court Decree"]
    ))

    # 047 - Ans C
    q.append(make_q(
        "ISR_E_047", "Direct Factual",
        "In which year did the Supreme Court deliver its landmark verdict modifying the Cauvery Water Disputes Tribunal's final award and declaring river waters a national asset?",
        "காவிரி நதிநீர் தகராறுகள் தீர்ப்பாயத்தின் இறுதித் தீர்ப்பை மாற்றியமைத்து, நதிநீரை ஒரு தேசியச் சொத்தாகப் பிரகடனப்படுத்தி உச்ச நீதிமன்றம் தனது வரலாற்றுச் சிறப்புமிக்க தீர்ப்பை எந்த ஆண்டில் வழங்கியது?",
        "2014", "2014",
        "2016", "2016",
        "2018", "2018",
        "2020", "2020",
        "C",
        "On 16 February 2018, a three-judge bench of the Supreme Court delivered the landmark final judgment in the Cauvery water dispute, slightly modifying the 2007 CWDT award and declaring that inter-State waters are a national asset.",
        "2018 பிப்ரவரி 16 அன்று, உச்ச நீதிமன்றத்தின் மூன்று நீதிபதிகள் கொண்ட அமர்வு காவிரி நதிநீர் தகராறில் வரலாற்றுத் தீர்ப்பை வழங்கியது; 2007 CWDT தீர்ப்பை சற்று மாற்றியமைத்து, மாநிலங்களுக்கு இடையேயான நதிகள் 'தேசியச் சொத்து' என்று அறிவித்தது.",
        "2014 was when interlocutory applications were heard.", "2014 என்பது இடைக்கால மனுக்கள் விசாரிக்கப்பட்ட ஆண்டாகும்.",
        "2016 was when the court affirmed maintainability under Art 136.", "2016 என்பது உறுப்பு 136-ன் கீழ் வழக்கு செல்லும் என உறுதிப்படுத்திய ஆண்டாகும்.",
        "2018 is the exact year of the final Cauvery judgment of the Supreme Court.", "2018 என்பது உச்ச நீதிமன்றத்தின் இறுதி காவிரித் தீர்ப்பு வழங்கப்பட்ட ஆண்டாகும்.",
        "2020 is incorrect.", "2020 தவறானது.",
        "The Supreme Court's final Cauvery judgment was delivered in February 2018.",
        "உச்ச நீதிமன்றத்தின் இறுதி காவிரித் தீர்ப்பு 2018 பிப்ரவரியில் வழங்கப்பட்டது.",
        "Supreme Court final Cauvery verdict = 2018.",
        "உச்ச நீதிமன்ற இறுதி காவிரித் தீர்ப்பு = 2018.",
        tags=["Cauvery Dispute", "Supreme Court", "2018"]
    ))

    # 048 - Ans D
    q.append(make_q(
        "ISR_E_048", "Direct Factual",
        "Which statutory implementation authority was officially constituted by the Central Government in June 2018 pursuant to the Supreme Court's Cauvery judgment?",
        "உச்ச நீதிமன்றத்தின் காவிரித் தீர்ப்பைத் தொடர்ந்து ஜூன் 2018-ல் மத்திய அரசால் முறைப்படி அமைக்கப்பட்ட சட்டப்பூர்வ அமலாக்க அமைப்பு எது?",
        "Cauvery River Basin Board", "காவிரி நதிப் படுகை வாரியம்",
        "National Water Commission", "தேசிய நீர் ஆணையம்",
        "Cauvery Monitoring Board", "காவிரி கண்காணிப்பு வாரியம்",
        "Cauvery Water Management Authority (CWMA)", "காவிரி நீர் மேலாண்மை ஆணையம் (CWMA)",
        "D",
        "In June 2018, the Central Government framed the Cauvery Water Management Scheme, 2018 under Section 6A of the IRWD Act, constituting the Cauvery Water Management Authority (CWMA) and the Cauvery Water Regulation Committee (CWRC).",
        "ஜூன் 2018-ல், மத்திய அரசு IRWD சட்டத்தின் பிரிவு 6A-ன் கீழ் காவிரி நீர் மேலாண்மைத் திட்டம் 2018-ஐ உருவாக்கி, காவிரி நீர் மேலாண்மை ஆணையம் (CWMA) மற்றும் காவிரி நீர் ஒழுங்குமுறைக் குழு (CWRC) ஆகியவற்றை அமைத்தது.",
        "Cauvery River Basin Board is not the name of the statutory body.", "காவிரி நதிப் படுகை வாரியம் என்பது அதன் பெயரல்ல.",
        "National Water Commission is a different advisory proposal.", "தேசிய நீர் ஆணையம் என்பது வேறொரு திட்டமாகும்.",
        "Cauvery Monitoring Board was the earlier suggested nomenclature, but CWMA was the official body established.", "காவிரி கண்காணிப்பு வாரியம் என்பது ஆரம்பத்தில் முன்மொழியப்பட்ட பெயர், ஆனால் CWMA அதிகாரப்பூர்வமாக அமைக்கப்பட்டது.",
        "Cauvery Water Management Authority (CWMA) was officially notified in June 2018.", "காவிரி நீர் மேலாண்மை ஆணையம் (CWMA) ஜூன் 2018-ல் அதிகாரப்பூர்வமாக அறிவிக்கப்பட்டது.",
        "CWMA was constituted under Section 6A of the IRWD Act, 1956 on 1 June 2018.",
        "CWMA ஆனது 1956 IRWD சட்டத்தின் பிரிவு 6A-ன் கீழ் 2018 ஜூன் 1 அன்று அமைக்கப்பட்டது.",
        "CWMA was established in June 2018.",
        "காவிரி நீர் மேலாண்மை ஆணையம் (CWMA) ஜூன் 2018 இல் அமைக்கப்பட்டது.",
        tags=["CWMA", "Cauvery", "2018 Scheme"]
    ))

    # 049 - Ans A
    q.append(make_q(
        "ISR_E_049", "Direct Factual",
        "In which year was the First Administrative Reforms Commission (ARC) appointed, which was the first to recommend setting up an Inter-State Council under Article 263?",
        "உறுப்பு 263-ன் கீழ் மாநிலங்களுக்கு இடையிலான மன்றத்தை அமைக்க முதன்முதலில் பரிந்துரைத்த முதலாவது நிர்வாகச் சீர்திருத்த ஆணையம் (ARC) எந்த ஆண்டில் நியமிக்கப்பட்டது?",
        "1966", "1966",
        "1969", "1969",
        "1972", "1972",
        "1983", "1983",
        "A",
        "The First Administrative Reforms Commission (ARC) was appointed in January 1966 (initially chaired by Morarji Desai, later K. Hanumanthaiah) and was the first official body to recommend setting up an Inter-State Council under Article 263.",
        "முதலாவது நிர்வாகச் சீர்திருத்த ஆணையம் (ARC) 1966 ஜனவரியில் நியமிக்கப்பட்டது (முதலில் மொரார்ஜி தேசாய், பின்னர் கே. ஹனுமந்தையா தலைமை); இதுவே உறுப்பு 263-ன் கீழ் மாநிலங்களுக்கு இடையிலான மன்றத்தை அமைக்க முதலில் பரிந்துரைத்த அதிகாரப்பூர்வ அமைப்பாகும்.",
        "1966 is the year the First ARC was appointed.", "1966 என்பது முதலாவது ARC நியமிக்கப்பட்ட ஆண்டாகும்.",
        "1969 was when the First ARC submitted its report on Centre-State relationships.", "1969 என்பது முதலாவது ARC தனது அறிக்கையைச் சமர்ப்பித்த ஆண்டாகும்.",
        "1972 is incorrect.", "1972 தவறானது.",
        "1983 was when the Sarkaria Commission was appointed.", "1983 என்பது சர்க்காரியா ஆணையம் அமைக்கப்பட்ட ஆண்டாகும்.",
        "First ARC (1966) first recommended an Inter-State Council under Article 263; Sarkaria Commission (1988) reaffirmed it.",
        "முதலாவது ARC (1966) உறுப்பு 263-ன் கீழ் மன்றத்தை முதலில் பரிந்துரைத்தது; சர்க்காரியா ஆணையம் (1988) அதை மீண்டும் வலியுறுத்தியது.",
        "First Administrative Reforms Commission was appointed in 1966.",
        "முதலாவது நிர்வாகச் சீர்திருத்த ஆணையம் 1966 இல் நியமிக்கப்பட்டது.",
        tags=["First ARC", "1966", "Inter-State Council"]
    ))

    # 050 - Ans B
    q.append(make_q(
        "ISR_E_050", "Direct Factual",
        "What is the fundamental constitutional distinction between the Inter-State Council and the Zonal Councils?",
        "மாநிலங்களுக்கு இடையிலான மன்றத்திற்கும் மண்டலக் குழுக்களுக்கும் இடையிலான அடிப்படை அரசியலமைப்பு வேறுபாடு என்ன?",
        "Both are established under Article 263", "இரண்டும் உறுப்பு 263-ன் கீழ் நிறுவப்பட்டுள்ளன",
        "Inter-State Council is constitutional (Article 263); Zonal Councils are statutory (1956 Act)", "மாநிலங்களுக்கு இடையிலான மன்றம் அரசியலமைப்பு ரீதியானது (உறுப்பு 263); மண்டலக் குழுக்கள் சட்டப்பூர்வமானவை (1956 சட்டம்)",
        "Both are statutory bodies under the States Reorganisation Act", "இரண்டும் மாநில மறுசீரமைப்புச் சட்டத்தின் கீழான சட்டப்பூர்வ அமைப்புகளாகும்",
        "Zonal Councils are constitutional; Inter-State Council is extra-constitutional", "மண்டலக் குழுக்கள் அரசியலமைப்பு ரீதியானவை; மாநிலங்களுக்கு இடையிலான மன்றம் அரசியலமைப்புக்கு அப்பாற்பட்டது",
        "B",
        "The Inter-State Council is a constitutional body established under Article 263 of the Constitution, whereas the Zonal Councils are statutory bodies created by Parliament under the States Reorganisation Act, 1956.",
        "மாநிலங்களுக்கு இடையிலான மன்றம் அரசியலமைப்பின் உறுப்பு 263-ன் கீழ் அமைக்கப்பட்ட ஓர் அரசியலமைப்பு அமைப்பாகும், அதே சமயம் மண்டலக் குழுக்கள் 1956 ஆம் ஆண்டின் மாநில மறுசீரமைப்புச் சட்டத்தின் கீழ் நாடாளுமன்றத்தால் உருவாக்கப்பட்ட சட்டப்பூர்வ அமைப்புகளாகும்.",
        "Zonal Councils are not under Article 263; only the Inter-State Council is under Art 263.", "மண்டலக் குழுக்கள் உறுப்பு 263-ன் கீழ் இல்லை; மாநிலங்களுக்கு இடையிலான மன்றம் மட்டுமே உறுப்பு 263-ன் கீழ் உள்ளது.",
        "Inter-State Council is constitutional, while Zonal Councils are statutory.", "மாநிலங்களுக்கு இடையிலான மன்றம் அரசியலமைப்பு ரீதியானது, மண்டலக் குழுக்கள் சட்டப்பூர்வமானவை.",
        "Inter-State Council is not under the States Reorganisation Act.", "மாநிலங்களுக்கு இடையிலான மன்றம் மாநில மறுசீரமைப்புச் சட்டத்தின் கீழ் இல்லை.",
        "This completely reverses their constitutional status.", "இது அவற்றின் அரசியலமைப்பு நிலையை முற்றிலும் தலைகீழாக மாற்றுகிறது.",
        "High-Yield Distinction: ISC = Constitutional (Art 263); Zonal Councils = Statutory (SRA 1956).",
        "முக்கிய வேறுபாடு: ISC = அரசியலமைப்பு சார்ந்தது (உறுப்பு 263); மண்டலக் குழுக்கள் = சட்டப்பூர்வமானது (SRA 1956).",
        "Inter-State Council is constitutional; Zonal Councils are statutory.",
        "மாநிலங்களுக்கு இடையிலான மன்றம் அரசியலமைப்பு அமைப்பு; மண்டலக் குழுக்கள் சட்டப்பூர்வ அமைப்புகள்.",
        tags=["Constitutional vs Statutory", "Inter-State Council", "Zonal Councils"]
    ))

    return q

if __name__ == "__main__":
    easy_qs = get_easy_questions()
    print(f"Total Easy Questions generated: {len(easy_qs)}")
    
    # Check answer key distribution
    from collections import Counter
    cnt = Counter(q["correct_answer"] for q in easy_qs)
    print("Easy Answer Key Distribution:", dict(cnt))
    
    out_dir = Path(r"c:\Users\Home\Desktop\tnpsc_ai\data\questions\polity")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "inter_state_relations_easy.json"
    
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(easy_qs, f, indent=2, ensure_ascii=False)
    print(f"Saved to {out_file}")
