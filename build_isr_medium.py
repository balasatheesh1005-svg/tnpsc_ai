# -*- coding: utf-8 -*-
"""
Builder for Inter-State Relations Part 1 — Medium MCQs (50 Questions)
IDs: ISR_M_001 to ISR_M_050
"""

import json
import os
import sys
from pathlib import Path

def make_q(qid, qtype, stem_en, stem_ta, opt_a_en, opt_a_ta, opt_b_en, opt_b_ta, opt_c_en, opt_c_ta, opt_d_en, opt_d_ta,
           correct_ans, exp_en, exp_ta, wno_a_en, wno_a_ta, wno_b_en, wno_b_ta, wno_c_en, wno_c_ta, wno_d_en, wno_d_ta,
           tip_en, tip_ta, rev_en, rev_ta, bloom="Understand", est_time=60, tags=None):
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
        "difficulty": "Medium",
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
        "tags": tags or ["Inter-State Relations", "Conceptual Comparison", "Indian Polity"]
    }

def get_medium_questions():
    q = []

    # 001 - Ans A
    q.append(make_q(
        "ISR_M_001", "Two-Statement",
        "Consider the following statements regarding the 'Full Faith and Credit' clause under Article 261 of the Constitution:\n1. Full faith and credit is accorded throughout India to public acts, records, and judicial proceedings of both the Union and States.\n2. Final judgments delivered by criminal courts of one State are directly capable of execution anywhere in India without fresh proceedings.\nWhich of the statements given above is/are correct?",
        "அரசியலமைப்பு உறுப்பு 261-ன் கீழ் உள்ள 'முழு நம்பிக்கையும் சான்றும்' விதி தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. ஒன்றியம் மற்றும் மாநிலங்கள் இரண்டின் பொதுச் சட்டங்கள், பதிவேடுகள் மற்றும் நீதித்துறை நடவடிக்கைகளுக்கும் இந்தியா முழுவதும் முழு நம்பிக்கையும் சான்றும் அளிக்கப்படுகிறது.\n2. ஒரு மாநிலத்தின் குற்றவியல் நீதிமன்றங்களால் வழங்கப்பட்ட இறுதித் தீர்ப்புகள் புதிய நடைமுறைகள் ஏதுமின்றி இந்தியா முழுவதும் நேரடியாக நிறைவேற்றப்படத் தக்கவை.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது சரியானது/சரியானவை?",
        "1 only", "1 மட்டும்",
        "2 only", "2 மட்டும்",
        "Both 1 and 2", "1 மற்றும் 2 இரண்டும்",
        "Neither 1 nor 2", "1-ம் அல்ல 2-ம் அல்ல",
        "A",
        "Statement 1 is correct: Article 261(1) accords full faith and credit to public acts, records, and judicial proceedings of the Union and States. Statement 2 is incorrect: Article 261(3) applies strictly to civil courts; penal and criminal judgments of one State are NOT automatically executable in another State without separate proceedings under the Code of Criminal Procedure.",
        "கூற்று 1 சரியானது: உறுப்பு 261(1) ஒன்றியம் மற்றும் மாநிலங்களின் பொதுச் சட்டங்கள், பதிவேடுகள் மற்றும் நீதித்துறை நடவடிக்கைகளுக்கு முழு நம்பிக்கையும் சான்றும் அளிக்கிறது. கூற்று 2 தவறானது: உறுப்பு 261(3) உரிமையியல் நீதிமன்றங்களுக்கு மட்டுமே பொருந்தும்; ஒரு மாநிலத்தின் குற்றவியல் தீர்ப்புகள் பிற மாநிலங்களில் தானாக நிறைவேற்றப்பட மாட்டாது.",
        "Statement 1 correctly reflects Article 261(1).", "கூற்று 1 உறுப்பு 261(1)-ஐச் சரியாகப் பிரதிபலிக்கிறது.",
        "Statement 2 is incorrect because Article 261(3) applies strictly to civil judgments, not criminal sentences.", "கூற்று 2 தவறானது, ஏனெனில் உறுப்பு 261(3) உரிமையியல் தீர்ப்புகளுக்கு மட்டுமே பொருந்தும், குற்றவியல் தீர்ப்புகளுக்கு அல்ல.",
        "Both cannot be correct as statement 2 is factually false.", "கூற்று 2 தவறானது என்பதால் இரண்டும் சரியாக இருக்க முடியாது.",
        "Statement 1 is constitutionally sound, so neither is incorrect.", "கூற்று 1 அரசியலமைப்பு ரீதியாகச் சரியானது.",
        "Civil court decrees are executable nationwide under Art 261(3); criminal laws/penal decrees are strictly excluded.",
        "உறுப்பு 261(3)-ன் கீழ் உரிமையியல் நீதிமன்றத் தீர்ப்புகள் மட்டுமே நாடு முழுவதும் நிறைவேற்றப்படத் தக்கவை; குற்றவியல் தீர்ப்புகள் விலக்கப்பட்டுள்ளன.",
        "Article 261(3) covers civil court decrees only.",
        "உறுப்பு 261(3) உரிமையியல் நீதிமன்றத் தீர்ப்புகளை மட்டுமே உள்ளடக்கியது.",
        tags=["Article 261", "Full Faith and Credit", "Civil vs Criminal"]
    ))

    # 002 - Ans B
    q.append(make_q(
        "ISR_M_002", "Comparison",
        "How does the constitutional dispute resolution mechanism for inter-State river waters under Article 262 differ from the Supreme Court's Original Jurisdiction under Article 131?",
        "உறுப்பு 262-ன் கீழ் உள்ள மாநிலங்களுக்கு இடையிலான நதிநீர் தகராறு தீர்வு முறைமையானது, உறுப்பு 131-ன் கீழ் உள்ள உச்ச நீதிமன்றத்தின் மூல அதிகார வரம்பிலிருந்து எவ்வாறு வேறுபடுகிறது?",
        "Article 131 excludes disputes between States, while Article 262 exclusively hears State disputes.", "உறுப்பு 131 மாநிலங்களுக்கிடையேயான தகராறுகளை விலக்குகிறது, ஆனால் உறுப்பு 262 மாநில தகராறுகளை மட்டுமே விசாரிக்கிறது.",
        "Article 262 empowers Parliament to exclude the Supreme Court's jurisdiction over water disputes, superseding ordinary Article 131 jurisdiction.", "உறுப்பு 262 நதிநீர் தகராறுகளில் உச்ச நீதிமன்றத்தின் அதிகார வரம்பை விலக்க நாடாளுமன்றத்திற்கு அதிகாரம் அளித்து, சாதாரண உறுப்பு 131 வரம்பை விஞ்சுகிறது.",
        "Decisions under Article 262 are purely advisory, whereas Article 131 judgments are binding.", "உறுப்பு 262-ன் கீழ் உள்ள முடிவுகள் முற்றிலும் ஆலோசனையானவை, ஆனால் உறுப்பு 131 தீர்ப்புகள் கட்டுப்படுத்துபவை.",
        "Article 262 requires a unanimous resolution of both Houses, whereas Article 131 operates by executive notification.", "உறுப்பு 262 இரு அவைகளின் ஒருமனதான தீர்மானத்தைக் கோருகிறது, ஆனால் உறுப்பு 131 நிர்வாக அறிவிப்பால் இயங்குகிறது.",
        "B",
        "While Article 131 provides original and exclusive jurisdiction to the Supreme Court for inter-governmental legal disputes, Article 262 is a non-obstante provision ('Notwithstanding anything in this Constitution...') empowering Parliament by law to bar both the Supreme Court and all other courts from exercising jurisdiction over inter-State river water disputes.",
        "அரசாங்கங்களுக்கிடையேயான சட்டத் தகராறுகளுக்கு உறுப்பு 131 உச்ச நீதிமன்றத்திற்கு மூல அதிகார வரம்பை வழங்கினாலும், உறுப்பு 262 ('இந்த அரசியலமைப்பில் என்ன கூறப்பட்டிருப்பினும்...') நதிநீர் தகராறுகளில் உச்ச நீதிமன்றம் மற்றும் பிற நீதிமன்றங்களின் அதிகார வரம்பை நாடாளுமன்றம் சட்டம் மூலம் விலக்க வழிவகுக்கிறது.",
        "Article 131 specifically covers disputes between States, so option A is incorrect.", "உறுப்பு 131 மாநிலங்களுக்கிடையேயான தகராறுகளை உள்ளடக்கியது.",
        "Option B precisely explains the constitutional override of Article 131 by Article 262.", "விருப்பம் B உறுப்பு 131-ஐ உறுப்பு 262 எவ்வாறு விலக்குகிறது என்பதைத் துல்லியமாக விளக்குகிறது.",
        "Tribunal decisions under Article 262 are binding and have decree status, not purely advisory.", "உறுப்பு 262-ன் கீழான தீர்ப்பாய முடிவுகள் கட்டுப்படுத்தும் தன்மையுடையவை, வெறும் ஆலோசனைகள் அல்ல.",
        "Article 262 laws require ordinary legislative procedure, not unanimous resolutions.", "உறுப்பு 262 சட்டங்கள் சாதாரண சட்டமியற்றும் நடைமுறையையே பின்பற்றுகின்றன.",
        "Article 262 contains a non-obstante clause that overrides the Supreme Court's Article 131 original jurisdiction.",
        "உறுப்பு 262 ஒரு 'விதிவிலக்கு வாசகத்தைக்' (non-obstante clause) கொண்டு உச்ச நீதிமன்றத்தின் உறுப்பு 131 மூல அதிகார வரம்பை விஞ்சுகிறது.",
        "Article 262 empowers Parliament to bar Article 131 jurisdiction for river waters.",
        "உறுப்பு 262 நதிநீர் விவகாரங்களில் உறுப்பு 131 அதிகார வரம்பைத் தடுக்க நாடாளுமன்றத்திற்கு அதிகாரமளிக்கிறது.",
        tags=["Article 262", "Article 131", "Supreme Court Jurisdiction"]
    ))

    # 003 - Ans C
    q.append(make_q(
        "ISR_M_003", "Conceptual Comparison",
        "Which of the following represents a key structural difference between the Inter-State Council and the Zonal Councils?",
        "மாநிலங்களுக்கு இடையிலான மன்றத்திற்கும் மண்டலக் குழுக்களுக்கும் இடையிலான ஒரு முக்கிய கட்டமைப்பு வேறுபாட்டைப் பின்வருவனவற்றில் எது குறிக்கிறது?",
        "Inter-State Council is chaired by the President, while Zonal Councils are chaired by the Prime Minister.", "மாநிலங்களுக்கு இடையிலான மன்றத்திற்கு குடியரசுத் தலைவர் தலைமை தாங்குகிறார், மண்டலக் குழுக்களுக்கு பிரதமர் தலைமை தாங்குகிறார்.",
        "Inter-State Council is a statutory body, while Zonal Councils are constitutional bodies.", "மாநிலங்களுக்கு இடையிலான மன்றம் சட்டப்பூர்வ அமைப்பு, ஆனால் மண்டலக் குழுக்கள் அரசியலமைப்பு அமைப்புகளாகும்.",
        "Inter-State Council is chaired by the Prime Minister, whereas Zonal Councils are chaired by the Union Home Minister.", "மாநிலங்களுக்கு இடையிலான மன்றத்திற்குப் பிரதமர் தலைமை தாங்குகிறார், ஆனால் மண்டலக் குழுக்களுக்கு மத்திய உள்துறை அமைச்சர் தலைமை தாங்குகிறார்.",
        "Decisions of the Inter-State Council are legally binding on States, whereas Zonal Council decisions are purely advisory.", "மாநிலங்களுக்கு இடையிலான மன்றத்தின் முடிவுகள் மாநிலங்களைச் சட்டப்பூர்வமாகக் கட்டுப்படுத்துகின்றன, ஆனால் மண்டலக் குழு முடிவுகள் ஆலோசனையானவை.",
        "C",
        "The Inter-State Council (constitutional under Art 263) is chaired by the Prime Minister, while all Zonal Councils (statutory under States Reorganisation Act 1956) are chaired by the Union Home Minister. Both bodies are advisory in nature.",
        "மாநிலங்களுக்கு இடையிலான மன்றத்திற்கு (உறுப்பு 263) பிரதமர் தலைமை தாங்குகிறார், அதே சமயம் அனைத்து மண்டலக் குழுக்களுக்கும் (1956 சட்டம்) மத்திய உள்துறை அமைச்சர் தலைமை தாங்குகிறார். இரண்டுமே ஆலோசனை அமைப்புகளாகும்.",
        "The President does not chair the Inter-State Council.", "குடியரசுத் தலைவர் மாநிலங்களுக்கு இடையிலான மன்றத்திற்குத் தலைமை தாங்குவதில்லை.",
        "This reverses their legal status: ISC is constitutional, Zonal Councils are statutory.", "இது அவற்றின் சட்ட நிலையை மாற்றிக் கூறுகிறது: ISC அரசியலமைப்பு ரீதியானது, மண்டலக் குழுக்கள் சட்டப்பூர்வமானவை.",
        "Option C correctly identifies the distinct chairmanships of the two institutions.", "விருப்பம் C இவ்விரு அமைப்புகளின் தலைமைத்துவ வேறுபாட்டைச் சரியாகக் குறிப்பிடுகிறது.",
        "Neither body delivers legally binding awards; both are deliberative and advisory.", "எந்த அமைப்பும் சட்டப்பூர்வமாகக் கட்டுப்படுத்தும் தீர்ப்புகளை வழங்குவதில்லை; இரண்டுமே ஆலோசனைக் குழுக்களாகும்.",
        "ISC Chairman = Prime Minister; Zonal Council Chairman = Union Home Minister.",
        "ISC தலைவர் = பிரதமர்; மண்டலக் குழுத் தலைவர் = மத்திய உள்துறை அமைச்சர்.",
        "Inter-State Council is chaired by PM; Zonal Councils by Home Minister.",
        "மாநிலங்களுக்கு இடையிலான மன்றத்திற்குப் பிரதமரும், மண்டலக் குழுக்களுக்கு உள்துறை அமைச்சரும் தலைமை தாங்குகின்றனர்.",
        tags=["Inter-State Council", "Zonal Councils", "Chairmanship"]
    ))

    # 004 - Ans D
    q.append(make_q(
        "ISR_M_004", "Conceptual Comparison",
        "What is the fundamental legal distinction between the freedom of trade guaranteed under Article 301 and the right to practice any profession or trade under Article 19(1)(g)?",
        "உறுப்பு 301-ன் கீழ் உத்தரவாதம் அளிக்கப்பட்ட வர்த்தக சுதந்திரத்திற்கும், உறுப்பு 19(1)(g)-ன் கீழ் எந்தவொரு தொழிலையும் அல்லது வர்த்தகத்தையும் செய்யும் உரிமைக்கும் இடையிலான அடிப்படைச் சட்ட வேறுபாடு என்ன?",
        "Article 301 is a Fundamental Right, while Article 19(1)(g) is an ordinary constitutional right.", "உறுப்பு 301 ஒரு அடிப்படை உரிமை, ஆனால் உறுப்பு 19(1)(g) ஒரு சாதாரண அரசியலமைப்பு உரிமை.",
        "Article 19(1)(g) applies to foreign nationals, whereas Article 301 is restricted to Indian citizens.", "உறுப்பு 19(1)(g) வெளிநாட்டினருக்குப் பொருந்தும், ஆனால் உறுப்பு 301 இந்தியக் குடிமக்களுக்கு மட்டுமே பொருந்தும்.",
        "Article 301 can never be restricted under any circumstances, whereas Article 19(1)(g) can be suspended.", "உறுப்பு 301-ஐ எந்தச் சூழ்நிலையிலும் கட்டுப்படுத்த முடியாது, ஆனால் உறுப்பு 19(1)(g)-ஐ இடைநிறுத்தம் செய்யலாம்.",
        "Article 19(1)(g) is a Fundamental Right available exclusively to citizens, whereas Article 301 is a constitutional right available to all persons, corporations, and States.", "உறுப்பு 19(1)(g) குடிமக்களுக்கு மட்டுமே கிடைக்கும் ஓர் அடிப்படை உரிமை, ஆனால் உறுப்பு 301 என்பது அனைத்து நபர்கள், நிறுவனங்கள் மற்றும் மாநிலங்களுக்கும் கிடைக்கக்கூடிய அரசியலமைப்பு உரிமை.",
        "D",
        "Article 19(1)(g) is in Part III and is available ONLY to citizens of India (subject to reasonable restrictions under Art 19(6)). Article 301 in Part XIII is a constitutional right that protects the free flow of trade and is available to citizens, non-citizens, corporations, and States alike.",
        "உறுப்பு 19(1)(g) பகுதி III-ல் உள்ள ஓர் அடிப்படை உரிமை மற்றும் இந்தியக் குடிமக்களுக்கு மட்டுமே கிடைக்கிறது. பகுதி XIII-ல் உள்ள உறுப்பு 301 என்பது வர்த்தகத்தின் தடையற்ற ஓட்டத்தைப் பாதுகாக்கும் ஓர் அரசியலமைப்பு உரிமை மற்றும் இது குடிமக்கள், குடிமக்கள் அல்லாதவர்கள், பெருநிறுவனங்கள் மற்றும் மாநிலங்கள் அனைவருக்கும் கிடைக்கிறது.",
        "Article 19(1)(g) is the Fundamental Right, not Article 301.", "உறுப்பு 19(1)(g) தான் அடிப்படை உரிமை, உறுப்பு 301 அல்ல.",
        "Article 19(1)(g) is strictly restricted to citizens, not foreign nationals.", "உறுப்பு 19(1)(g) குடிமக்களுக்கு மட்டுமே உரித்தானது.",
        "Article 301 is subject to numerous constitutional restrictions in Articles 302 to 305.", "உறுப்பு 301 உறுப்புகள் 302 முதல் 305 வரையிலான பல அரசியலமைப்புக் கட்டுப்பாடுகளுக்கு உட்பட்டது.",
        "Option D accurately outlines the citizenship and constitutional scope distinction.", "விருப்பம் D குடியுரிமை மற்றும் அரசியலமைப்பு வரம்பு வேறுபாட்டைத் துல்லியமாக விளக்குகிறது.",
        "Art 19(1)(g) = Part III, Citizens only; Art 301 = Part XIII, protects the flow of trade generally (citizens, non-citizens, companies).",
        "உறுப்பு 19(1)(g) = பகுதி III, குடிமக்களுக்கு மட்டுமே; உறுப்பு 301 = பகுதி XIII, வர்த்தகப் போக்குவரத்தைப் பொதுவில் பாதுகாக்கிறது.",
        "Article 19(1)(g) is citizen-specific; Article 301 protects general trade flow.",
        "உறுப்பு 19(1)(g) குடிமக்களுக்கு மட்டுமே; உறுப்பு 301 வர்த்தகப் போக்குவரத்தைப் பாதுகாக்கிறது.",
        tags=["Article 301", "Article 19(1)(g)", "Fundamental Rights"]
    ))

    # 005 - Ans A
    q.append(make_q(
        "ISR_M_005", "Comparison",
        "Regarding the power to impose trade restrictions in the public interest, how does Parliament's power under Article 302 differ from a State Legislature's power under Article 304(b)?",
        "பொது நலன் கருதி வர்த்தகக் கட்டுப்பாடுகளை விதிக்கும் அதிகாரத்தில், உறுப்பு 302-ன் கீழ் நாடாளுமன்றத்தின் அதிகாரம் உறுப்பு 304(b)-ன் கீழ் மாநில சட்டமன்றத்தின் அதிகாரத்திலிருந்து எவ்வாறு வேறுபடுகிறது?",
        "Parliament can impose restrictions without previous presidential sanction, whereas a State Bill requires previous presidential sanction to be introduced.", "நாடாளுமன்றம் குடியரசுத் தலைவரின் முன் அனுமதியின்றி கட்டுப்பாடுகளை விதிக்க முடியும், ஆனால் மாநில மசோதாவை அறிமுகப்படுத்த குடியரசுத் தலைவரின் முன் அனுமதி தேவைப்படுகிறது.",
        "State Legislatures can ban inter-State trade completely, while Parliament can only levy import duties.", "மாநில சட்டமன்றங்கள் மாநிலங்களுக்கிடையேயான வர்த்தகத்தை முற்றிலும் தடை செய்யலாம், ஆனால் நாடாளுமன்றம் இறக்குமதி வரிகளை மட்டுமே விதிக்க முடியும்.",
        "Parliamentary restrictions require a special majority of two-thirds, whereas State restrictions require simple majority.", "நாடாளுமன்றக் கட்டுப்பாடுகளுக்கு மூன்றில் இரண்டு பங்கு சிறப்புப் பெரும்பான்மை தேவைப்படுகிறது, ஆனால் மாநிலக் கட்டுப்பாடுகளுக்குச் சாதாரண பெரும்பான்மை போதுமானது.",
        "Parliament can restrict trade only during a financial emergency, while States can restrict at any time.", "நிதி நெருக்கடியின் போது மட்டுமே நாடாளுமன்றம் வர்த்தகத்தைக் கட்டுப்படுத்த முடியும், ஆனால் மாநிலங்கள் எந்த நேரத்திலும் கட்டுப்படுத்தலாம்.",
        "A",
        "Under Article 302, Parliament may impose restrictions in the public interest by ordinary legislation without needing any prior Presidential sanction. Conversely, under the proviso to Article 304(b), a State Legislature CANNOT introduce a bill imposing reasonable restrictions without the PREVIOUS SANCTION of the President.",
        "உறுப்பு 302-ன் கீழ், நாடாளுமன்றம் குடியரசுத் தலைவரின் முன் அனுமதியின்றி சாதாரண சட்டம் மூலம் பொது நலக் கட்டுப்பாடுகளை விதிக்கலாம். ஆனால், உறுப்பு 304(b)-ன் நிபந்தனையின் கீழ், குடியரசுத் தலைவரின் முன் அனுமதியின்றி மாநில சட்டமன்றத்தில் அத்தகைய மசோதாவை அறிமுகப்படுத்த முடியாது.",
        "Option A precisely captures the procedural difference regarding Presidential sanction.", "விருப்பம் A குடியரசுத் தலைவரின் முன் அனுமதி தொடர்பான நடைமுறை வேறுபாட்டைத் துல்லியமாகக் காட்டுகிறது.",
        "State legislatures cannot completely ban interstate trade arbitrarily.", "மாநில சட்டமன்றங்கள் தன்னிச்சையாக வர்த்தகத்தை முற்றிலும் தடை செய்ய முடியாது.",
        "Neither body requires a two-thirds majority; both use ordinary legislative process.", "இரண்டு அமைப்புகளுக்கும் மூன்றில் இரண்டு பங்கு பெரும்பான்மை தேவையில்லை.",
        "Article 302 is not tied to financial emergencies.", "உறுப்பு 302 நிதி நெருக்கடியுடன் தொடர்புடையது அல்ல.",
        "Key Distinction: Art 302 (Parliament) = No prior presidential sanction; Art 304(b) (State) = Prior presidential sanction mandatory.",
        "முக்கிய வேறுபாடு: உறுப்பு 302 (நாடாளுமன்றம்) = முன் அனுமதி தேவையில்லை; உறுப்பு 304(b) (மாநிலம்) = குடியரசுத் தலைவரின் முன் அனுமதி கட்டாயம்.",
        "Parliament needs no prior sanction under Art 302, unlike States under Art 304(b).",
        "உறுப்பு 302-ன் கீழ் நாடாளுமன்றத்திற்கு முன் அனுமதி தேவையில்லை, ஆனால் மாநிலங்களுக்கு 304(b)-ன் கீழ் தேவை.",
        tags=["Article 302", "Article 304(b)", "Presidential Sanction"]
    ))

    # 006 - Ans B
    q.append(make_q(
        "ISR_M_006", "Exception Analysis",
        "Under Article 303 of the Constitution, what is the specific exception to the general prohibition against discriminatory trade laws, and to whom is this exception available?",
        "அரசியலமைப்பு உறுப்பு 303-ன் கீழ், பாகுபாடான வர்த்தகச் சட்டங்களுக்கு எதிரான பொதுவான தடைக்குரிய குறிப்பிட்ட விதிவிலக்கு என்ன, மேலும் இந்த விதிவிலக்கு யாருக்குக் கிடைக்கிறது?",
        "Protecting indigenous handicraft industries; available to both Parliament and State Legislatures", "உள்நாட்டு கைவினைத் தொழில்களைப் பாதுகாத்தல்; நாடாளுமன்றம் மற்றும் மாநில சட்டமன்றங்கள் இரண்டிற்கும் கிடைக்கிறது",
        "Dealing with a situation arising from scarcity of goods; available ONLY to Parliament", "பொருட்களின் பற்றாக்குறையால் எழும் சூழ்நிலையைக் கையாளுதல்; நாடாளுமன்றத்திற்கு மட்டுமே கிடைக்கிறது",
        "Compensating for natural disaster losses; available ONLY to State Legislatures", "இயற்கைப் பேரிடர் இழப்புகளுக்கு ஈடுசெய்தல்; மாநில சட்டமன்றங்களுக்கு மட்டுமே கிடைக்கிறது",
        "Promoting exports to landlocked States; available exclusively to the Inter-State Council", "நிலத்தால் சூழப்பட்ட மாநிலங்களுக்கு ஏற்றுமதியை ஊக்குவித்தல்; மாநிலங்களுக்கு இடையிலான மன்றத்திற்கு மட்டுமே கிடைக்கிறது",
        "B",
        "Article 303(2) provides an exclusive exception: Parliament (and NOT State Legislatures) may make a law giving preference or making discrimination IF it is declared by such law that it is necessary to do so for the purpose of dealing with a situation arising from SCARCITY OF GOODS in any part of the territory of India.",
        "உறுப்பு 303(2) ஒரு பிரத்யேக விதிவிலக்கை வழங்குகிறது: இந்தியாவின் எந்தப் பகுதியிலும் பொருட்களின் பற்றாக்குறையால் (scarcity of goods) எழும் சூழ்நிலையைக் கையாள்வதற்காகத் தேவைப்பட்டால் நாடாளுமன்றம் (மாநில சட்டமன்றங்கள் அல்ல) பாகுபாடு காட்டும் அல்லது முன்னுரிமை அளிக்கும் சட்டத்தை இயற்றலாம்.",
        "Handicraft protection is not an exception to Art 303 non-discrimination.", "கைவினைப் பாதுகாப்பு உறுப்பு 303-ன் விதிவிலக்கு அல்ல.",
        "Article 303(2) explicitly grants the scarcity exception strictly to Parliament.", "உறுப்பு 303(2) பற்றாக்குறை விதிவிலக்கை நாடாளுமன்றத்திற்கு மட்டுமே வெளிப்படையாக வழங்குகிறது.",
        "State Legislatures do not enjoy the scarcity exception under Article 303(2).", "மாநில சட்டமன்றங்களுக்கு உறுப்பு 303(2)-ன் கீழ் பற்றாக்குறை விதிவிலக்கு இல்லை.",
        "The Inter-State Council does not have legislative law-making powers.", "மாநிலங்களுக்கு இடையிலான மன்றத்திற்குச் சட்டமியற்றும் அதிகாரம் இல்லை.",
        "TNPSC Trap: The scarcity exception under Article 303(2) is available EXCLUSIVELY to Parliament, never to States!",
        "TNPSC பொறி: உறுப்பு 303(2)-ன் கீழான பற்றாக்குறை விதிவிலக்கு நாடாளுமன்றத்திற்கு மட்டுமே உரியது, மாநிலங்களுக்கு அல்ல!",
        "Article 303(2) scarcity exception is available only to Parliament.",
        "உறுப்பு 303(2) பற்றாக்குறை விதிவிலக்கு நாடாளுமன்றத்திற்கு மட்டுமே கிடைக்கிறது.",
        tags=["Article 303(2)", "Scarcity Exception"]
    ))

    # 007 - Ans C
    q.append(make_q(
        "ISR_M_007", "Conceptual Comparison",
        "What is the primary difference in constitutional scope between Article 304(a) and Article 304(b) regarding State legislative powers?",
        "மாநில சட்டமன்ற அதிகாரங்கள் தொடர்பாக உறுப்பு 304(a) மற்றும் உறுப்பு 304(b) ஆகியவற்றிற்கு இடையிலான அரசியலமைப்பு நோக்கத்தின் முதன்மை வேறுபாடு என்ன?",
        "Article 304(a) applies to intra-state trade, while Article 304(b) applies to foreign trade.", "உறுப்பு 304(a) மாநிலத்திற்கு உட்பட்ட வர்த்தகத்திற்குப் பொருந்தும், ஆனால் 304(b) வெளிநாட்டு வர்த்தகத்திற்குப் பொருந்தும்.",
        "Article 304(a) requires prior Presidential sanction, while Article 304(b) requires Governor's approval only.", "உறுப்பு 304(a)-க்கு குடியரசுத் தலைவரின் முன் அனுமதி தேவை, ஆனால் 304(b)-க்கு ஆளுநரின் ஒப்புதல் மட்டுமே தேவை.",
        "Article 304(a) deals with non-discriminatory taxation on imported goods, while Article 304(b) deals with reasonable regulatory restrictions in the public interest.", "உறுப்பு 304(a) இறக்குமதி பொருட்கள் மீதான பாகுபாடற்ற வரிவிதிப்பைக் கையாள்கிறது, ஆனால் 304(b) பொது நலன் கருதிய நியாயமான ஒழுங்குமுறைக் கட்டுப்பாடுகளைக் கையாள்கிறது.",
        "Article 304(a) is an emergency provision, whereas Article 304(b) operates during peacetime.", "உறுப்பு 304(a) ஒரு அவசரகால விதி, ஆனால் 304(b) அமைதிக் காலத்தில் இயங்குகிறது.",
        "C",
        "Article 304(a) empowers a State to levy taxes on goods imported from other States, provided the tax does not discriminate against imported goods vis-a-vis local goods (fiscal equality). Article 304(b) empowers a State to impose non-fiscal reasonable restrictions in the public interest with previous sanction of the President.",
        "உறுப்பு 304(a) உள்ளூர் பொருட்களுக்கு இணையாக பிற மாநிலப் பொருட்கள் மீது பாகுபாடற்ற வரிகளை விதிக்க மாநிலத்திற்கு அதிகாரமளிக்கிறது (நிதி சமத்துவம்). உறுப்பு 304(b) குடியரசுத் தலைவரின் முன் அனுமதியுடன் பொது நலன் கருதி நியாயமான கட்டுப்பாடுகளை விதிக்க அதிகாரமளிக்கிறது.",
        "Neither article deals with foreign trade; foreign trade is exclusively in the Union List (Entry 41).", "எந்த உறுப்பும் வெளிநாட்டு வர்த்தகத்தைக் கையாளவில்லை; அது மத்தியப் பட்டியலில் (பதிவு 41) உள்ளது.",
        "Article 304(a) does NOT require prior presidential sanction; Article 304(b) DOES require it.", "உறுப்பு 304(a)-க்கு முன் அனுமதி தேவையில்லை; 304(b)-க்கு கட்டாயம் தேவை.",
        "Option C correctly contrasts non-discriminatory taxation with public interest reasonable restrictions.", "விருப்பம் C பாகுபாடற்ற வரிவிதிப்பையும் பொது நலக் கட்டுப்பாடுகளையும் சரியாக ஒப்பிடுகிறது.",
        "Neither provision is an emergency provision.", "எந்த விதியும் அவசரகால விதி அல்ல.",
        "Art 304(a) = Non-discriminatory tax (no prior sanction needed); Art 304(b) = Reasonable restriction (prior presidential sanction mandatory).",
        "உறுப்பு 304(a) = பாகுபாடற்ற வரி (முன் அனுமதி தேவையில்லை); உறுப்பு 304(b) = நியாயமான கட்டுப்பாடு (குடியரசுத் தலைவர் முன் அனுமதி கட்டாயம்).",
        "Article 304(a) governs taxation; Article 304(b) governs regulatory restrictions.",
        "உறுப்பு 304(a) வரிவிதிப்பையும், உறுப்பு 304(b) ஒழுங்குமுறைக் கட்டுப்பாடுகளையும் நிர்வகிக்கிறது.",
        tags=["Article 304(a)", "Article 304(b)", "State Powers"]
    ))

    # 008 - Ans D
    q.append(make_q(
        "ISR_M_008", "Constitutional Application",
        "If a State Legislature enacts a law imposing trade restrictions under Article 304(b) WITHOUT obtaining the previous sanction of the President, how can that defect be constitutionally cured?",
        "ஒரு மாநில சட்டமன்றம் உறுப்பு 304(b)-ன் கீழ் குடியரசுத் தலைவரின் முன் அனுமதியைப் பெறாமல் வர்த்தகக் கட்டுப்பாடுகளை விதிக்கும் சட்டத்தை இயற்றினால், அந்த குறைபாட்டை அரசியலமைப்பு ரீதியாக எவ்வாறு சரிசெய்ய முடியும்?",
        "By obtaining the retrospective approval of the State Cabinet", "மாநில அமைச்சரவையின் பின்னேற்பு ஒப்புதலைப் பெறுவதன் மூலம்",
        "By securing a ratification resolution from the Inter-State Council", "மாநிலங்களுக்கு இடையிலான மன்றத்தின் ஏற்புத் தீர்மானத்தைப் பெறுவதன் மூலம்",
        "The defect can never be cured and the Act is void ab initio", "இக்குறையை ஒருபோதும் சரிசெய்ய முடியாது மற்றும் அச்சட்டம் ஆரம்பத்திலிருந்தே செல்லாது",
        "By obtaining the subsequent assent of the President under Article 255", "உறுப்பு 255-ன் கீழ் குடியரசுத் தலைவரின் பிந்தைய ஒப்புதலைப் பெறுவதன் மூலம்",
        "D",
        "Under Article 255 of the Constitution, no Act of a State Legislature is invalid merely by reason that a required recommendation or previous sanction was not given, provided assent to that Act was subsequently given by the President.",
        "அரசியலமைப்பு உறுப்பு 255-ன் கீழ், தேவைப்படும் பரிந்துரை அல்லது முன் அனுமதி வழங்கப்படவில்லை என்ற ஒரே காரணத்திற்காக ஒரு மாநிலச் சட்டம் செல்லாததாகாது; எனினும், அச்சட்டத்திற்குப் பின்னர் குடியரசுத் தலைவரால் ஒப்புதல் அளிக்கப்பட்டிருக்க வேண்டும்.",
        "State Cabinet approval cannot cure a constitutional defect under the Constitution.", "மாநில அமைச்சரவை ஒப்புதலால் அரசியலமைப்புக் குறையைச் சரிசெய்ய முடியாது.",
        "The Inter-State Council has no constitutional power to ratify state legislation.", "மாநிலச் சட்டங்களை அங்கீகரிக்கும் அதிகாரம் மாநிலங்களுக்கு இடையிலான மன்றத்திற்கு இல்லை.",
        "The defect is NOT fatal because Article 255 specifically provides a constitutional cure.", "உறுப்பு 255 ஒரு குறிப்பிட்ட அரசியலமைப்புத் தீர்வை வழங்குவதால் இக்குறைபாடு மாற்ற முடியாதது அல்ல.",
        "Article 255 explicitly validates the Act if subsequent Presidential assent is received.", "பிந்தைய குடியரசுத் தலைவர் ஒப்புதல் பெறப்பட்டால் உறுப்பு 255 வெளிப்படையாக அச்சட்டத்தைச் செல்லுபடியாக்குகிறது.",
        "Cure Principle (Article 255): Lack of previous sanction under Art 304(b) is cured if the Act subsequently receives the President's assent.",
        "தீர்வு விதி (உறுப்பு 255): உறுப்பு 304(b)-ன் கீழான முன் அனுமதி குறைபாடு, அச்சட்டம் பின்னர் குடியரசுத் தலைவரின் ஒப்புதலைப் பெற்றால் சரியாகிவிடும்.",
        "Article 255 cures lack of prior sanction if subsequent presidential assent is given.",
        "உறுப்பு 255 பிந்தைய குடியரசுத் தலைவர் ஒப்புதல் மூலம் முன் அனுமதி இல்லாமையைச் சரிசெய்கிறது.",
        tags=["Article 255", "Article 304(b)", "Cure Principle"]
    ))

    # 009 - Ans A
    q.append(make_q(
        "ISR_M_009", "Composition Analysis",
        "Which of the following officials participate in the meetings of a Zonal Council as Advisors, and what is the nature of their voting power?",
        "பின்வரும் அதிகாரிகளில் யார் ஒரு மண்டலக் குழுவின் கூட்டங்களில் 'ஆலோசகர்களாக' (Advisors) பங்கேற்கிறார்கள், மேலும் அவர்களின் வாக்குரிமையின் தன்மை என்ன?",
        "A person nominated by NITI Aayog and the Chief Secretaries of member States; they have NO right to vote", "நிதி ஆயோக்கால் பரிந்துரைக்கப்பட்ட ஒரு நபர் மற்றும் உறுப்பினர் மாநிலங்களின் தலைமைச் செயலாளர்கள்; அவர்களுக்கு வாக்களிக்கும் உரிமை இல்லை",
        "The Chief Justices of the respective High Courts; they possess a casting vote", "அந்தந்த உயர் நீதிமன்றங்களின் தலைமை நீதிபதிகள்; அவர்கள் முடிவாக்கும் வாக்கைக் கொண்டுள்ளனர்",
        "The Advocates General of member States; they enjoy equal voting rights with Ministers", "உறுப்பினர் மாநிலங்களின் அட்வகேட் ஜெனரல்கள்; அவர்கள் அமைச்சர்களுக்கு இணையான வாக்குரிமையைப் பெற்றுள்ளனர்",
        "The Secretaries of the Union Ministry of Finance; they possess veto power over resolutions", "மத்திய நிதி அமைச்சகத்தின் செயலாளர்கள்; அவர்கள் தீர்மானங்கள் மீது வீட்டோ அதிகாரத்தைக் கொண்டுள்ளனர்",
        "A",
        "Under Section 16(1) of the States Reorganisation Act 1956, one person nominated by NITI Aayog (formerly Planning Commission), the Chief Secretary to the Government of each member State, and the Development Commissioner of each member State are associated as Advisors, but they have NO right to vote.",
        "1956 மாநில மறுசீரமைப்புச் சட்டத்தின் பிரிவு 16(1)-ன் கீழ், நிதி ஆயோக்கால் பரிந்துரைக்கப்படும் ஒரு நபர், ஒவ்வொரு உறுப்பினர் மாநிலத்தின் தலைமைச் செயலாளர் மற்றும் வளர்ச்சி ஆணையர் ஆகியோர் ஆலோசகர்களாக இணைக்கப்படுகிறார்கள், ஆனால் அவர்களுக்கு வாக்களிக்கும் உரிமை கிடையாது.",
        "Option A accurately lists the statutory advisors and their non-voting status.", "விருப்பம் A சட்டப்பூர்வ ஆலோசகர்களையும் அவர்களது வாக்களிக்கும் உரிமையற்ற நிலையையும் சரியாகக் குறிப்பிடுகிறது.",
        "Judges do not attend Zonal Council meetings.", "நீதிபதிகள் மண்டலக் குழு கூட்டங்களில் கலந்துகொள்வதில்லை.",
        "Advocates General are not statutory members of Zonal Councils.", "அட்வகேட் ஜெனரல்கள் மண்டலக் குழுக்களின் சட்டப்பூர்வ உறுப்பினர்கள் அல்ல.",
        "Finance Ministry secretaries do not possess veto power over Zonal Councils.", "நிதி அமைச்சகச் செயலாளர்களுக்கு வீட்டோ அதிகாரம் இல்லை.",
        "Zonal Council Advisors: NITI Aayog nominee + State Chief Secretaries + Development Commissioners (NO voting rights).",
        "மண்டலக் குழு ஆலோசகர்கள்: நிதி ஆயோக் பரிந்துரைத்தவர் + மாநிலத் தலைமைச் செயலாளர்கள் + வளர்ச்சி ஆணையர்கள் (வாக்குரிமை இல்லை).",
        "Zonal Council Advisors have no right to vote.",
        "மண்டலக் குழு ஆலோசகர்களுக்கு வாக்களிக்கும் உரிமை இல்லை.",
        tags=["Zonal Councils", "Advisors", "NITI Aayog"]
    ))

    # 010 - Ans B
    q.append(make_q(
        "ISR_M_010", "Comparison",
        "How does the North Eastern Council (NEC) differ fundamentally in its institutional mandate from the five standard Zonal Councils?",
        "வடகிழக்கு கவுன்சில் (NEC) அதன் நிறுவனப் பணிகளில் ஐந்து நிலையான மண்டலக் குழுக்களிலிருந்து எவ்வாறு அடிப்படையில் வேறுபடுகிறது?",
        "The NEC has constitutional status under Article 263, while Zonal Councils are non-statutory.", "NEC உறுப்பு 263-ன் கீழ் அரசியலமைப்பு அந்தஸ்தைக் கொண்டுள்ளது, ஆனால் மண்டலக் குழுக்கள் சட்டப்பூர்வமற்றவை.",
        "The NEC functions as a regional planning body with its own budget allocation, unlike the purely advisory and coordinating Zonal Councils.", "தூய ஆலோசனை மற்றும் ஒருங்கிணைப்பு அமைப்புகளான மண்டலக் குழுக்களைப் போலன்றி, NEC தனக்கென நிதி ஒதுக்கீட்டைக் கொண்ட ஒரு பிராந்திய திட்டமிடல் அமைப்பாகச் செயல்படுகிறது.",
        "The NEC is chaired by the Prime Minister directly, whereas Zonal Councils are chaired by Governors.", "NEC-க்கு பிரதமர் நேரடியாகத் தலைமை தாங்குகிறார், ஆனால் மண்டலக் குழுக்களுக்கு ஆளுநர்கள் தலைமை தாங்குகின்றனர்.",
        "The NEC excludes Chief Ministers and includes only Members of Parliament from the region.", "NEC முதலமைச்சர்களை விலக்கி, அப்பகுதியின் நாடாளுமன்ற உறுப்பினர்களை மட்டுமே உள்ளடக்கியுள்ளது.",
        "B",
        "While the 5 Zonal Councils are purely deliberative and advisory forums for inter-state harmony, the North Eastern Council (under NEC Act 1971) functions as a comprehensive regional planning body that formulates and finances regional developmental infrastructure projects across the 8 northeastern States.",
        "5 மண்டலக் குழுக்கள் மாநிலங்களுக்கிடையேயான இணக்கத்திற்கான தூய ஆலோசனை அமைப்புகளாக இருக்கும் வேளையில், வடகிழக்கு கவுன்சில் (1971 சட்டம்) 8 வடகிழக்கு மாநிலங்களில் பிராந்திய வளர்ச்சித் திட்டங்களை உருவாக்கி நிதியளிக்கும் ஒரு விரிவான திட்டமிடல் அமைப்பாகச் செயல்படுகிறது.",
        "Both NEC and Zonal Councils are statutory, neither is under Article 263.", "NEC மற்றும் மண்டலக் குழுக்கள் இரண்டுமே சட்டப்பூர்வமானவை, எதுவும் உறுப்பு 263-ன் கீழ் இல்லை.",
        "Option B correctly identifies NEC's unique regional planning and funding role.", "விருப்பம் B NEC-ன் தனித்துவமான திட்டமிடல் மற்றும் நிதிப் பங்கைச் சரியாகக் காட்டுகிறது.",
        "Union Home Minister chairs the NEC as well (since 2018 amendment), not the PM.", "NEC-க்கும் மத்திய உள்துறை அமைச்சரே தலைமை தாங்குகிறார் (2018 முதல்), பிரதமர் அல்ல.",
        "All 8 Chief Ministers and Governors of the northeastern states are members of the NEC.", "அனைத்து 8 வடகிழக்கு முதல்வர்களும் ஆளுநர்களும் NEC-ன் உறுப்பினர்கள் ஆவர்.",
        "NEC is not merely an advisory forum; it is a regional planning and project-financing agency for the 8 NE States.",
        "NEC என்பது வெறும் ஆலோசனைக் குழு மட்டுமல்ல; இது 8 வடகிழக்கு மாநிலங்களுக்கான பிராந்திய திட்டமிடல் மற்றும் திட்ட-நிதி முகமையாகும்.",
        "NEC acts as a regional planning and financing body.",
        "வடகிழக்கு கவுன்சில் ஒரு பிராந்திய திட்டமிடல் மற்றும் நிதி அமைப்பாகச் செயல்படுகிறது.",
        tags=["North Eastern Council", "Regional Planning"]
    ))

    # 011 - Ans C
    q.append(make_q(
        "ISR_M_011", "Statutory Analysis",
        "Why has the River Boards Act, 1956 remained practically inoperative since its enactment?",
        "1956 ஆம் ஆண்டின் நதி வாரியங்கள் சட்டம் இயற்றப்பட்டதிலிருந்து நடைமுறையில் செயல்படாமல் போனதற்குக் காரணம் என்ன?",
        "The Supreme Court declared the entire River Boards Act unconstitutional in 1960.", "1960-ல் உச்ச நீதிமன்றம் நதி வாரியங்கள் சட்டம் முழுவதையும் அரசியலமைப்பிற்கு முரணானது என்று அறிவித்தது.",
        "The Act requires approval from all neighboring international countries before creating a board.", "ஒரு வாரியத்தை உருவாக்குவதற்கு முன் அனைத்து அண்டை சர்வதேச நாடுகளின் ஒப்புதலையும் இச்சட்டம் கோருகிறது.",
        "River Boards are purely advisory and can be established only upon request from interested State Governments, which States avoided out of fear of losing control over water.", "நதி வாரியங்கள் முற்றிலும் ஆலோசனையானவை மற்றும் ஆர்வமுள்ள மாநில அரசுகளின் கோரிக்கையின் பேரில் மட்டுமே நிறுவப்பட முடியும்; நீர் மீதான கட்டுப்பாட்டை இழக்க நேரிடும் என்ற அச்சத்தால் மாநிலங்கள் இக்கோரிக்கையைத் தவிர்த்தன.",
        "The Constitution does not contain any legislative entry supporting River Boards.", "நதி வாரியங்களை ஆதரிக்கும் எந்தவொரு சட்டமன்றப் பதிவும் அரசியலமைப்பில் இல்லை.",
        "C",
        "The River Boards Act 1956 provides that the Central Government may establish a board on a request from a State Government. Because water is primarily a State subject (Entry 17, List II) and the boards are purely advisory, State Governments preferred bilateral negotiations or tribunals rather than inviting central boards.",
        "1956 நதி வாரியங்கள் சட்டம், மாநில அரசின் கோரிக்கையின் பேரில் மத்திய அரசு ஒரு வாரியத்தை நிறுவலாம் என்று கூறுகிறது. நீர் முதன்மையாக மாநிலப் பட்டியலில் (பதிவு 17) இருப்பதாலும், வாரியங்கள் முற்றிலும் ஆலோசனை அமைப்புகளாக இருப்பதாலும், மாநிலங்கள் மத்திய வாரியங்களை அழைப்பதை விட இருதரப்பு பேச்சுவார்த்தைகள் அல்லது தீர்ப்பாயங்களையே விரும்பின.",
        "The Act was never struck down by the Supreme Court.", "இச்சட்டம் உச்ச நீதிமன்றத்தால் ஒருபோதும் ரத்து செய்யப்படவில்லை.",
        "International approval is not a condition in the Act.", "சர்வதேச நாடுகளின் ஒப்புதல் இச்சட்டத்தின் நிபந்தனை அல்ல.",
        "Option C correctly highlights the state-consent barrier and advisory limitation.", "விருப்பம் C மாநில ஒப்புதல் தடையையும் ஆலோசனை வரம்பையும் சரியாகக் குறிப்பிடுகிறது.",
        "Entry 56 of the Union List explicitly supports regulation and development of inter-State rivers.", "மத்தியப் பட்டியலின் பதிவு 56 மாநிலங்களுக்கு இடையேயான நதிகள் ஒழுங்குமுறையை வெளிப்படையாக ஆதரிக்கிறது.",
        "Reality of River Boards Act: States never requested boards under Section 4, rendering the Act a dead letter.",
        "நதி வாரியங்கள் சட்டத்தின் உண்மை: மாநிலங்கள் பிரிவு 4-ன் கீழ் வாரியங்களை ஒருபோதும் கோராததால், இச்சட்டம் நடைமுறையற்றுப் போனது.",
        "River Boards Act remained inoperative due to requirement of state request and purely advisory role.",
        "மாநிலக் கோரிக்கை நிபந்தனை மற்றும் வெறும் ஆலோசனைப் பங்கு காரணமாக நதி வாரியங்கள் சட்டம் செயல்படாமல் போனது.",
        tags=["River Boards Act 1956", "Inoperative"]
    ))

    # 012 - Ans D
    q.append(make_q(
        "ISR_M_012", "Statutory Timelines",
        "Under the Inter-State Water Disputes (Amendment) Act, 2002, what is the statutory time limit within which a water disputes tribunal must give its decision, and what is the maximum permissible extension?",
        "2002 ஆம் ஆண்டின் நதிநீர் தகராறுகள் திருத்தச் சட்டத்தின் கீழ், ஒரு நதிநீர் தீர்ப்பாயம் தனது முடிவை வழங்க வேண்டிய சட்டப்பூர்வ கால வரம்பு என்ன, மேலும் அனுமதிக்கப்பட்ட அதிகபட்ச நீட்டிப்பு என்ன?",
        "Decision within 1 year; extension up to 6 months", "1 ஆண்டிற்குள் முடிவு; 6 மாதங்கள் வரை நீட்டிப்பு",
        "Decision within 2 years; extension up to 1 year", "2 ஆண்டுகளுக்குள் முடிவு; 1 ஆண்டு வரை நீட்டிப்பு",
        "Decision within 5 years; no extension permissible", "5 ஆண்டுகளுக்குள் முடிவு; நீட்டிப்பு எதுவும் அனுமதிக்கப்படாது",
        "Decision within 3 years; extension up to 2 years", "3 ஆண்டுகளுக்குள் முடிவு; 2 ஆண்டுகள் வரை நீட்டிப்பு",
        "D",
        "The 2002 amendment to Section 5(2) of the IRWD Act 1956 mandates that the Tribunal shall investigate the matters referred to it and forward to the Central Government its report within a period of THREE YEARS. The Central Government may extend this period for a further period NOT EXCEEDING TWO YEARS.",
        "1956 IRWD சட்டத்தின் பிரிவு 5(2)-க்கான 2002 திருத்தம், தீர்ப்பாயம் தனக்கு அனுப்பப்பட்ட விஷயங்களை விசாரித்து தனது அறிக்கையை மூன்று ஆண்டுகளுக்குள் (3 years) மத்திய அரசுக்கு அனுப்ப வேண்டும் எனக் கட்டாயப்படுத்துகிறது. மத்திய அரசு இக்காலத்தை மேலும் இரண்டு ஆண்டுகளுக்கு மிகாமல் (2 years) நீட்டிக்கலாம்.",
        "One year is the deadline for reference by the Central Government, not for the award.", "ஒரு ஆண்டு என்பது மத்திய அரசு தீர்ப்பாயத்திற்கு அனுப்புவதற்கான காலக்கெடுவாகும்.",
        "Two years is incorrect.", "இரண்டு ஆண்டுகள் தவறானது.",
        "Five years total without extension is inaccurate.", "நீட்டிப்பின்றி ஐந்து ஆண்டுகள் என்பது தவறானது.",
        "Option D accurately reflects the 3 years + up to 2 years extension formula.", "விருப்பம் D '3 ஆண்டுகள் + 2 ஆண்டுகள் வரை நீட்டிப்பு' என்ற விதியைத் துல்லியமாகக் காட்டுகிறது.",
        "2002 IRWD Amendment timelines: Tribunal must submit report within 3 years (extendable by up to 2 years by Central Govt).",
        "2002 IRWD திருத்தக் காலக்கெடு: தீர்ப்பாயம் 3 ஆண்டுகளுக்குள் அறிக்கையைச் சமர்ப்பிக்க வேண்டும் (மத்திய அரசால் 2 ஆண்டுகள் வரை நீட்டிக்கப்படலாம்).",
        "Tribunal timeline = 3 years + up to 2 years extension.",
        "தீர்ப்பாயக் காலக்கெடு = 3 ஆண்டுகள் + 2 ஆண்டுகள் வரை நீட்டிப்பு.",
        tags=["IRWD Act 2002 Amendment", "Timelines"]
    ))

    # 013 - Ans A
    q.append(make_q(
        "ISR_M_013", "Constitutional Analysis",
        "What is the precise constitutional scope of the Inter-State Council's function under Article 263(a) when inquiring into disputes between States?",
        "மாநிலங்களுக்கிடையேயான தகராறுகளை விசாரிக்கும் போது, உறுப்பு 263(a)-ன் கீழ் மாநிலங்களுக்கு இடையிலான மன்றத்தின் பணியின் துல்லியமான அரசியலமைப்பு வரம்பு என்ன?",
        "Its function is strictly advisory and recommendatory; it cannot deliver a legally binding verdict like a court.", "இதன் பணி முற்றிலும் ஆலோசனையானது மற்றும் பரிந்துரைக்கத்தக்கது; நீதிமன்றத்தைப் போலச் சட்டப்பூர்வமாகக் கட்டுப்படுத்தும் தீர்ப்பை வழங்க முடியாது.",
        "It acts as a court of record with full contempt and execution powers.", "இது முழு அவமதிப்பு மற்றும் நிறைவேற்று அதிகாரங்களைக் கொண்ட ஒரு பதிவு நீதிமன்றமாகச் செயல்படுகிறது.",
        "Its decisions automatically overrule conflicting judgments of the High Courts.", "இதன் முடிவுகள் உயர் நீதிமன்றங்களின் முரண்பட்ட தீர்ப்புகளைத் தானாகவே ரத்து செய்கின்றன.",
        "It functions as an appellate arbitral tribunal whose decisions can be appealed only to the President.", "இது ஒரு மேல்முறையீட்டு நடுவர் மன்றமாகச் செயல்படுகிறது, இதன் முடிவுகள் மீது குடியரசுத் தலைவரிடம் மட்டுமே மேல்முறையீடு செய்ய முடியும்.",
        "A",
        "Article 263(a) empowers the Council to 'inquire into and advise upon disputes which may have arisen between States'. Unlike the Supreme Court under Article 131, the Inter-State Council has no judicial or adjudicatory power; its recommendations are purely advisory and cannot deliver binding legal determinations.",
        "உறுப்பு 263(a), 'மாநிலங்களுக்கிடையே எழுந்திருக்கக்கூடிய தகராறுகளை விசாரித்து ஆலோசனை வழங்குவதற்கு' மன்றத்திற்கு அதிகாரம் அளிக்கிறது. உறுப்பு 131-ன் கீழ் உச்ச நீதிமன்றத்தைப் போலன்றி, மாநிலங்களுக்கு இடையிலான மன்றத்திற்கு நீதித்துறை அல்லது தீர்ப்பளிக்கும் அதிகாரம் இல்லை; அதன் பரிந்துரைகள் முற்றிலும் ஆலோசனையானவை.",
        "Option A accurately states the non-adjudicatory and purely advisory nature of the Council.", "விருப்பம் A மன்றத்தின் ஆலோசனையான தன்மையைத் துல்லியமாகக் கூறுகிறது.",
        "The Council is not a court of record under the Constitution.", "மன்றம் அரசியலமைப்பின் கீழ் ஒரு பதிவு நீதிமன்றம் அல்ல.",
        "The Council cannot overrule High Court decisions.", "மன்றம் உயர் நீதிமன்றத் தீர்ப்புகளை ரத்து செய்ய முடியாது.",
        "It is not an appellate arbitral tribunal.", "இது ஒரு மேல்முறையீட்டு நடுவர் மன்றம் அல்ல.",
        "Article 263 is an administrative and political coordination mechanism, completely distinct from Article 131 judicial adjudication.",
        "உறுப்பு 263 என்பது நிர்வாக மற்றும் அரசியல் ஒருங்கிணைப்பு முறைமையாகும், இது உறுப்பு 131 நீதித்துறைத் தீர்ப்பிலிருந்து முற்றிலும் மாறுபட்டது.",
        "Inter-State Council's dispute inquiry role under Art 263(a) is purely advisory.",
        "உறுப்பு 263(a)-ன் கீழ் மன்றத்தின் தகராறு விசாரணைப் பணி முற்றிலும் ஆலோசனையானது.",
        tags=["Article 263(a)", "Advisory Nature"]
    ))

    # 014 - Ans B
    q.append(make_q(
        "ISR_M_014", "Composition Analysis",
        "Regarding the representation of Union Territories in the Inter-State Council, which of the following statements is correct?",
        "மாநிலங்களுக்கு இடையிலான மன்றத்தில் யூனியன் பிரதேசங்களின் பிரதிநிதித்துவம் தொடர்பாக, பின்வரும் கூற்றுகளில் எது சரியானது?",
        "Union Territories have no representation in the Inter-State Council.", "யூனியன் பிரதேசங்களுக்கு மாநிலங்களுக்கு இடையிலான மன்றத்தில் பிரதிநிதித்துவம் இல்லை.",
        "Chief Ministers represent UTs having legislative assemblies, while Administrators represent UTs without legislative assemblies.", "சட்டமன்றம் கொண்ட யூனியன் பிரதேசங்களை முதலமைச்சர்களும், சட்டமன்றம் இல்லாத யூனியன் பிரதேசங்களை நிர்வாகிகளும் பிரதிநிதித்துவப்படுத்துகின்றனர்.",
        "All Union Territories are represented solely by the Union Home Minister.", "அனைத்து யூனியன் பிரதேசங்களும் மத்திய உள்துறை அமைச்சரால் மட்டுமே பிரதிநிதித்துவப்படுத்தப்படுகின்றன.",
        "Only the National Capital Territory of Delhi is permitted to attend as an observer.", "தில்லி தேசிய தலைநகர் பகுதி மட்டுமே பார்வையாளராகக் கலந்துகொள்ள அனுமதிக்கப்படுகிறது.",
        "B",
        "The 1990 Presidential Order specifies that the Inter-State Council includes the Chief Ministers of Union Territories having a Legislative Assembly (e.g., Delhi, Puducherry, J&K) and Administrators of Union Territories not having a Legislative Assembly.",
        "1990 ஆம் ஆண்டின் குடியரசுத் தலைவர் ஆணை, சட்டமன்றம் கொண்ட யூனியன் பிரதேசங்களின் (எ.கா., தில்லி, புதுச்சேரி, ஜம்மு-காஷ்மீர்) முதலமைச்சர்களும், சட்டமன்றம் இல்லாத யூனியன் பிரதேசங்களின் நிர்வாகிகளும் மாநிலங்களுக்கு இடையிலான மன்றத்தில் இடம்பெறுவர் என்று குறிப்பிடுகிறது.",
        "Union Territories are fully represented in the Council.", "யூனியன் பிரதேசங்கள் மன்றத்தில் முழுமையாகப் பிரதிநிதித்துவப்படுத்தப்படுகின்றன.",
        "Option B correctly distinguishes representation between UTs with assemblies (CMs) and without assemblies (Administrators).", "விருப்பம் B சட்டமன்றம் உள்ள (முதல்வர்கள்) மற்றும் சட்டமன்றம் இல்லாத (நிர்வாகிகள்) யூனியன் பிரதேசப் பிரதிநிதித்துவத்தைச் சரியாக வேறுபடுத்துகிறது.",
        "The Home Minister does not represent UTs individually in place of their heads.", "உள்துறை அமைச்சர் அந்தந்தப் பகுதித் தலைவர்களுக்குப் பதிலாகத் தனித்தனியாகப் பிரதிநிதித்துவப்படுத்துவதில்லை.",
        "Other UTs are full members, not mere observers.", "பிற யூனியன் பிரதேசங்கள் முழு உறுப்பினர்கள், வெறும் பார்வையாளர்கள் அல்ல.",
        "ISC Membership: CMs of States + CMs of UTs with Assemblies + Administrators of other UTs.",
        "ISC உறுப்பினர் சேர்க்கை: மாநில முதல்வர்கள் + சட்டமன்றம் உள்ள யூ.பி முதல்வர்கள் + பிற யூ.பி நிர்வாகிகள்.",
        "UTs with assemblies send CMs; UTs without assemblies send Administrators to ISC.",
        "சட்டமன்றம் உள்ள யூ.பி-க்கள் முதல்வர்களையும், இல்லாதவை நிர்வாகிகளையும் ISC-க்கு அனுப்புகின்றன.",
        tags=["Inter-State Council", "Union Territories Representation"]
    ))

    # 015 - Ans C
    q.append(make_q(
        "ISR_M_015", "Composition Analysis",
        "What is the total ministerial composition of the Standing Committee of the Inter-State Council as established in 1996?",
        "1996 ஆம் ஆண்டில் அமைக்கப்பட்ட மாநிலங்களுக்கு இடையிலான மன்றத்தின் நிலைக் குழுவின் மொத்த அமைச்சரவை அமைப்பு என்ன?",
        "Prime Minister + 10 Chief Ministers", "பிரதம அமைச்சர் + 10 முதலமைச்சர்கள்",
        "Union Home Minister + 28 Chief Ministers", "மத்திய உள்துறை அமைச்சர் + 28 முதலமைச்சர்கள்",
        "Union Home Minister (Chairman) + 5 Union Cabinet Ministers + 9 Chief Ministers", "மத்திய உள்துறை அமைச்சர் (தலைவர்) + 5 மத்திய அமைச்சரவை அமைச்சர்கள் + 9 முதலமைச்சர்கள்",
        "Finance Minister (Chairman) + all State Finance Ministers", "நிதி அமைச்சர் (தலைவர்) + அனைத்து மாநில நிதி அமைச்சர்கள்",
        "C",
        "The Standing Committee of the Inter-State Council consists of: Union Home Minister as Chairman; five Union Cabinet Ministers nominated by the PM; and nine Chief Ministers nominated by the PM.",
        "மாநிலங்களுக்கு இடையிலான மன்றத்தின் நிலைக் குழுவில்: தலைவராக மத்திய உள்துறை அமைச்சர்; பிரதமரால் நியமிக்கப்படும் ஐந்து மத்திய அமைச்சரவை அமைச்சர்கள்; மற்றும் ஒன்பது முதலமைச்சர்கள் ஆகியோர் அடங்குவர்.",
        "The Prime Minister does not chair the Standing Committee.", "பிரதமர் நிலைக் குழுவிற்குத் தலைமை தாங்குவதில்லை.",
        "Not all 28 CMs are on the Standing Committee; only 9 CMs serve on it.", "அனைத்து 28 முதல்வர்களும் நிலைக் குழுவில் இல்லை; 9 முதல்வர்கள் மட்டுமே உள்ளனர்.",
        "Option C gives the precise official composition of the Standing Committee (Home Minister + 5 Union Ministers + 9 CMs = 15 members).", "விருப்பம் C நிலைக் குழுவின் துல்லியமான அதிகாரப்பூர்வ அமைப்பைக் குறிப்பிடுகிறது (உள்துறை அமைச்சர் + 5 மத்திய அமைச்சர்கள் + 9 முதல்வர்கள் = 15 உறுப்பினர்கள்).",
        "Finance Minister and State Finance Ministers constitute the GST Council, not the ISC Standing Committee.", "நிதி அமைச்சரும் மாநில நிதி அமைச்சர்களும் ஜிஎஸ்டி கவுன்சிலை உருவாக்குகின்றனர், நிலைக் குழுவை அல்ல.",
        "ISC Standing Committee: Union Home Minister (Chairman) + 5 Union Cabinet Ministers + 9 Chief Ministers (Total 15 members).",
        "ISC நிலைக் குழு: மத்திய உள்துறை அமைச்சர் (தலைவர்) + 5 மத்திய அமைச்சர்கள் + 9 முதலமைச்சர்கள் (மொத்தம் 15 உறுப்பினர்கள்).",
        "Standing Committee composition = Home Minister + 5 Cabinet Ministers + 9 CMs.",
        "நிலைக் குழு அமைப்பு = உள்துறை அமைச்சர் + 5 மத்திய அமைச்சர்கள் + 9 முதல்வர்கள்.",
        tags=["Standing Committee", "Composition", "Inter-State Council"]
    ))

    # 016 - Ans D
    q.append(make_q(
        "ISR_M_016", "Institutional Linkage",
        "Since May 2011, which major inter-governmental bodies have been officially serviced by the Inter-State Council Secretariat (ISCS)?",
        "மே 2011 முதல், மாநிலங்களுக்கு இடையிலான மன்றச் செயலகத்தால் (ISCS) அதிகாரப்பூர்வமாகப் பணிவிடை செய்யப்படும் முக்கிய அரசுகளுக்கிடையேயான அமைப்புகள் எவை?",
        "Finance Commission and GST Council", "நிதி ஆணையம் மற்றும் ஜிஎஸ்டி கவுன்சில்",
        "National Development Council and NITI Aayog", "தேசிய வளர்ச்சிக் குழு மற்றும் நிதி ஆயோக்",
        "Law Commission of India and Delimitation Commission", "இந்தியச் சட்ட ஆணையம் மற்றும் தொகுதி மறுவரையறை ஆணையம்",
        "The Inter-State Council and all the Zonal Councils", "மாநிலங்களுக்கு இடையிலான மன்றம் மற்றும் அனைத்து மண்டலக் குழுக்களும்",
        "D",
        "Since May 2011, the Inter-State Council Secretariat (ISCS), set up in 1991 and headed by a Secretary to the Government of India, has been entrusted with the administrative and secretarial functions of both the Inter-State Council and all the Zonal Councils.",
        "1991-ல் அமைக்கப்பட்டு இந்திய அரசின் செயலாளரைத் தலைவராகக் கொண்ட மாநிலங்களுக்கு இடையிலான மன்றச் செயலகம் (ISCS), மே 2011 முதல் மாநிலங்களுக்கு இடையிலான மன்றம் மற்றும் அனைத்து மண்டலக் குழுக்கள் இரண்டின் நிர்வாக மற்றும் செயலகப் பணிகளையும் கவனித்து வருகிறது.",
        "Finance Commission has its own separate secretariat; GST Council has GST Council Secretariat.", "நிதி ஆணையத்திற்கும் ஜிஎஸ்டி கவுன்சிலுக்கும் தனித்தனிச் செயலகங்கள் உள்ளன.",
        "NDC and NITI Aayog have distinct secretariats.", "NDC மற்றும் நிதி ஆயோக் தனிச் செயலகங்களைக் கொண்டுள்ளன.",
        "Law Commission is under Ministry of Law and Justice.", "சட்ட ஆணையம் சட்டம் மற்றும் நீதி அமைச்சகத்தின் கீழ் உள்ளது.",
        "Option D correctly notes that ISCS serves both the constitutional Inter-State Council and the statutory Zonal Councils.", "விருப்பம் D ISCS ஆனது அரசியலமைப்பு மன்றம் மற்றும் சட்டப்பூர்வ மண்டலக் குழுக்கள் இரண்டிற்கும் சேவையாற்றுகிறது என்பதைக் குறிப்பிடுகிறது.",
        "Since 2011, the Inter-State Council Secretariat (ISCS) services both the Inter-State Council and all Zonal Councils.",
        "2011 முதல், மாநிலங்களுக்கு இடையிலான மன்றச் செயலகம் (ISCS) மன்றம் மற்றும் அனைத்து மண்டலக் குழுக்கள் இரண்டிற்கும் பணியாற்றுகிறது.",
        "ISCS services both Inter-State Council and Zonal Councils.",
        "ISCS மாநிலங்களுக்கு இடையிலான மன்றத்திற்கும் மண்டலக் குழுக்களுக்கும் சேவையாற்றுகிறது.",
        tags=["Inter-State Council Secretariat", "Zonal Councils", "ISCS"]
    ))

    # 017 - Ans A
    q.append(make_q(
        "ISR_M_017", "Comparison",
        "How does the decision-making rule in the Inter-State Council (Article 263) fundamentally differ from that in the GST Council (Article 279A)?",
        "மாநிலங்களுக்கு இடையிலான மன்றத்தில் (உறுப்பு 263) முடிவெடுக்கும் விதி, ஜிஎஸ்டி கவுன்சிலில் (உறுப்பு 279A) உள்ள முடிவெடுக்கும் விதியிலிருந்து எவ்வாறு அடிப்படையில் வேறுபடுகிறது?",
        "Inter-State Council decides by consensus, whereas GST Council decides by a 3/4th weighted majority voting formula.", "மாநிலங்களுக்கு இடையிலான மன்றம் ஒருமித்த கருத்து மூலம் முடிவெடுக்கிறது, ஆனால் ஜிஎஸ்டி கவுன்சில் 3/4 பங்கு எடையிடப்பட்ட பெரும்பான்மை வாக்குப்பதிவு சூத்திரம் மூலம் முடிவெடுக்கிறது.",
        "Inter-State Council requires a 2/3rd majority of States, while GST Council decisions require Prime Ministerial approval.", "மாநிலங்களுக்கு இடையிலான மன்றத்திற்கு மாநிலங்களின் 2/3 பங்கு பெரும்பான்மை தேவை, ஆனால் ஜிஎஸ்டி கவுன்சில் முடிவுகளுக்குப் பிரதமரின் ஒப்புதல் தேவை.",
        "Inter-State Council decisions are decided by secret ballot, while GST Council decisions are unanimous.", "மாநிலங்களுக்கு இடையிலான மன்ற முடிவுகள் இரகசிய வாக்கெடுப்பு மூலம் தீர்மானிக்கப்படுகின்றன, ஆனால் ஜிஎஸ்டி கவுன்சில் முடிவுகள் ஒருமனதானவை.",
        "Inter-State Council decisions are binding by law, while GST Council recommendations are voluntary.", "மாநிலங்களுக்கு இடையிலான மன்ற முடிவுகள் சட்டத்தால் கட்டுப்படுத்துகின்றன, ஆனால் ஜிஎஸ்டி கவுன்சில் பரிந்துரைகள் விருப்பத்திற்குரியவை.",
        "A",
        "The Inter-State Council operates strictly on the principle of consensus with no formal voting. In contrast, Article 279A(9) provides a rigid weighted voting formula for the GST Council: the Central Government has 1/3rd of the total weight, all States combined have 2/3rd, and decisions require a 3/4th weighted majority.",
        "மாநிலங்களுக்கு இடையிலான மன்றம் முறையான வாக்கெடுப்பு இன்றி முற்றிலும் 'ஒருமித்த கருத்து' (consensus) கொள்கையின் அடிப்படையில் செயல்படுகிறது. இதற்கு மாறாக, உறுப்பு 279A(9) ஜிஎஸ்டி கவுன்சிலுக்கு கடுமையான எடையிடப்பட்ட வாக்குப்பதிவு முறையை வழங்குகிறது: மத்திய அரசுக்கு 1/3 பங்கு, அனைத்து மாநிலங்களுக்கும் சேர்த்து 2/3 பங்கு, மற்றும் முடிவுகளுக்கு 3/4 பங்கு பெரும்பான்மை தேவை.",
        "Option A accurately highlights the consensus versus 3/4th weighted majority distinction.", "விருப்பம் A ஒருமித்த கருத்து vs 3/4 எடையிடப்பட்ட பெரும்பான்மை வேறுபாட்டைத் துல்லியமாக விளக்குகிறது.",
        "The PM does not decide GST Council voting outcomes.", "பிரதமர் ஜிஎஸ்டி கவுன்சில் வாக்கு முடிவுகளைத் தீர்மானிப்பதில்லை.",
        "Secret ballot is not used in the Inter-State Council.", "மாநிலங்களுக்கு இடையிலான மன்றத்தில் இரகசிய வாக்கெடுப்பு இல்லை.",
        "Inter-State Council decisions are advisory, not legally binding by law.", "மன்றத்தின் முடிவுகள் ஆலோசனையானவை, சட்டத்தால் கட்டுப்படுத்துபவை அல்ல.",
        "Inter-State Council = Consensus-based deliberation; GST Council = Weighted voting (Centre 1/3, States 2/3; 3/4 majority to pass).",
        "மாநிலங்களுக்கு இடையிலான மன்றம் = ஒருமித்த கருத்து; ஜிஎஸ்டி கவுன்சில் = எடையிடப்பட்ட வாக்குப்பதிவு (மத்திய அரசு 1/3, மாநிலங்கள் 2/3; 3/4 பெரும்பான்மை).",
        "Inter-State Council decides by consensus; GST Council by 3/4th weighted voting.",
        "மாநிலங்களுக்கு இடையிலான மன்றம் ஒருமித்த கருத்தாலும், ஜிஎஸ்டி கவுன்சில் 3/4 எடையிடப்பட்ட வாக்காலும் முடிவெடுக்கின்றன.",
        tags=["Inter-State Council", "GST Council", "Decision Making"]
    ))

    # 018 - Ans B
    q.append(make_q(
        "ISR_M_018", "Case Law & Reference",
        "In the 1991 Presidential Reference concerning the Cauvery Water Disputes Tribunal's interim order, what was the ruling of the Supreme Court regarding the Karnataka Cauvery Basin Irrigation Protection Ordinance?",
        "காவிரி நதிநீர் தகராறுகள் தீர்ப்பாயத்தின் இடைக்கால உத்தரவு தொடர்பான 1991 குடியரசுத் தலைவர் குறிப்பில் (Presidential Reference), கர்நாடக காவிரிப் படுகை பாசனப் பாதுகாப்பு அவசரச் சட்டம் குறித்து உச்ச நீதிமன்றத்தின் தீர்ப்பு என்ன?",
        "The State Ordinance was upheld as a valid exercise of State legislative power under Entry 17.", "மாநில அவசரச் சட்டம் பதிவு 17-ன் கீழான மாநில சட்டமன்ற அதிகாரத்தின் செல்லுபடியாகும் நடவடிக்கையாக உறுதி செய்யப்பட்டது.",
        "The State Ordinance was held unconstitutional and ultra vires as it sought to nullify a valid tribunal order passed under a central law enacted pursuant to Article 262.", "உறுப்பு 262-ன் கீழ் இயற்றப்பட்ட மத்தியச் சட்டத்தின்படி பிறப்பிக்கப்பட்ட செல்லுபடியாகும் தீர்ப்பாய ஆணையை ரத்து செய்ய முயன்றதால், அந்த மாநில அவசரச் சட்டம் அரசியலமைப்பிற்கு முரணானது மற்றும் அதிகார வரம்பை மீறியது என அறிவிக்கப்பட்டது.",
        "The Supreme Court held that the Tribunal had no power to pass any interim order.", "இடைக்கால உத்தரவு எதையும் பிறப்பிக்க தீர்ப்பாயத்திற்கு அதிகாரம் இல்லை என உச்ச நீதிமன்றம் கூறியது.",
        "The dispute was transferred directly to the International Court of Justice.", "தகராறு நேரடியாக சர்வதேச நீதிமன்றத்திற்கு மாற்றப்பட்டது.",
        "B",
        "In Re Cauvery Water Disputes Tribunal (AIR 1992 SC 522), the Supreme Court held that the Karnataka Ordinance nullifying the interim award of the CWDT was unconstitutional. A State Legislature cannot pass an Ordinance or law to overturn an order of a tribunal constituted under an Act of Parliament enacted under Article 262.",
        "காவிரி நதிநீர் தீர்ப்பாய விவகாரத்தில் (AIR 1992 SC 522), CWDT-ன் இடைக்காலத் தீர்ப்பை ரத்து செய்யும் கர்நாடக அரசின் அவசரச் சட்டம் அரசியலமைப்பிற்கு முரணானது என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது. உறுப்பு 262-ன் கீழ் நாடாளுமன்றச் சட்டத்தால் அமைக்கப்பட்ட ஒரு தீர்ப்பாயத்தின் உத்தரவை ரத்து செய்ய ஒரு மாநில சட்டமன்றத்திற்கு அதிகாரமில்லை.",
        "The Ordinance was struck down, not upheld.", "அவசரச் சட்டம் ரத்து செய்யப்பட்டது, உறுதி செய்யப்படவில்லை.",
        "Option B correctly describes the unconstitutionality of the state ordinance overturning the tribunal's order.", "விருப்பம் B தீர்ப்பாய உத்தரவை ரத்து செய்த மாநில அவசரச் சட்டத்தின் அரசியலமைப்பு முரண்பாட்டைச் சரியாக விவரிக்கிறது.",
        "The Supreme Court affirmed that the Tribunal DID have the incidental power to grant interim relief.", "இடைக்கால நிவாரணம் வழங்க தீர்ப்பாயத்திற்கு அதிகாரம் உண்டு என்பதை உச்ச நீதிமன்றம் உறுதி செய்தது.",
        "ICJ has no jurisdiction over domestic inter-state river disputes.", "உள்நாட்டு மாநில நதிநீர் தகராறுகளில் ICJ-க்கு அதிகார வரம்பு இல்லை.",
        "Rule of Law principle: A State cannot enact legislation or issue an ordinance to nullify an order passed by an inter-State water disputes tribunal.",
        "சட்டத்தின் ஆட்சி விதி: ஒரு மாநில நதிநீர் தீர்ப்பாயம் பிறப்பித்த உத்தரவை ரத்து செய்ய எந்தவொரு மாநிலமும் சட்டம் அல்லது அவசரச் சட்டம் இயற்ற முடியாது.",
        "Karnataka Ordinance nullifying CWDT interim order held unconstitutional.",
        "CWDT இடைக்கால உத்தரவை ரத்து செய்த கர்நாடக அவசரச் சட்டம் அரசியலமைப்பிற்கு முரணானது எனத் தீர்ப்பளிக்கப்பட்டது.",
        tags=["Cauvery Dispute", "1991 Presidential Reference", "Article 262"]
    ))

    # 019 - Ans C
    q.append(make_q(
        "ISR_M_019", "Tribunals & Basin States",
        "Which of the following sets of States was involved as riparian parties before the Krishna Water Disputes Tribunal II (constituted in 2004 under Justice Brijesh Kumar)?",
        "2004 ஆம் ஆண்டில் நீதிபதி பிரிஜேஷ் குமார் தலைமையில் அமைக்கப்பட்ட கிருஷ்ணா நதிநீர் தகராறுகள் தீர்ப்பாயம் II-ன் முன் எந்த மாநிலக் குழுக்கள் நதிப் படுகைப் பங்காளிகளாகப் பங்கேற்றன?",
        "Karnataka, Tamil Nadu, and Kerala", "கர்நாடகா, தமிழ்நாடு மற்றும் கேரளா",
        "Madhya Pradesh, Gujarat, and Rajasthan", "மத்தியப் பிரதேசம், குஜராத் மற்றும் ராஜஸ்தான்",
        "Maharashtra, Karnataka, and Andhra Pradesh (including Telangana)", "மகாராஷ்டிரா, கர்நாடகா மற்றும் ஆந்திரப் பிரதேசம் (தெலுங்கானா உட்பட)",
        "Odisha, Chhattisgarh, and Jharkhand", "ஒடிசா, சத்தீஸ்கர் மற்றும் ஜார்க்கண்ட்",
        "C",
        "The Krishna Water Disputes Tribunal II (KWDT-II) was constituted in April 2004 to adjudicate water sharing among Maharashtra, Karnataka, and Andhra Pradesh. Post-2014, the reorganized State of Telangana became an additional successor party to Andhra Pradesh's share.",
        "2004 ஏப்ரலில் அமைக்கப்பட்ட கிருஷ்ணா நதிநீர் தகராறுகள் தீர்ப்பாயம் II (KWDT-II), மகாராஷ்டிரா, கர்நாடகா மற்றும் ஆந்திரப் பிரதேசம் ஆகியவற்றுக்கு இடையே நீர் பகிர்வைத் தீர்மானிக்க அமைக்கப்பட்டது. 2014-க்குப் பிறகு, மறுசீரமைக்கப்பட்ட தெலுங்கானா மாநிலமும் ஆந்திராவின் பங்கில் கூடுதல் தரப்பினரானது.",
        "Karnataka, Tamil Nadu, and Kerala are parties to the Cauvery dispute, not Krishna.", "கர்நாடகா, தமிழ்நாடு மற்றும் கேரளா காவிரி தகராறின் தரப்பினர்கள்.",
        "MP, Gujarat, and Rajasthan were parties to the Narmada dispute.", "ம.பி, குஜராத் மற்றும் ராஜஸ்தான் நர்மதா தகராறின் தரப்பினர்கள்.",
        "Maharashtra, Karnataka, and Andhra Pradesh are the true riparian states of the Krishna basin.", "மகாராஷ்டிரா, கர்நாடகா மற்றும் ஆந்திரா ஆகியவை கிருஷ்ணா படுகையின் உண்மையான மாநிலங்கள் ஆகும்.",
        "Odisha, Chhattisgarh, and Jharkhand are in the Mahanadi/Damodar basins.", "ஒடிசா, சத்தீஸ்கர் மற்றும் ஜார்க்கண்ட் மகாநதி/தாமோதர் படுகைகளில் உள்ளன.",
        "Krishna River basin states: Maharashtra, Karnataka, Andhra Pradesh, and Telangana.",
        "கிருஷ்ணா நதிப் படுகை மாநிலங்கள்: மகாராஷ்டிரா, கர்நாடகா, ஆந்திரப் பிரதேசம் மற்றும் தெலுங்கானா.",
        "Krishna Water Disputes Tribunal II = Maharashtra, Karnataka, Andhra Pradesh.",
        "கிருஷ்ணா நதிநீர் தகராறுகள் தீர்ப்பாயம் II = மகாராஷ்டிரா, கர்நாடகா, ஆந்திரப் பிரதேசம்.",
        tags=["Krishna Tribunal II", "Basin States"]
    ))

    # 020 - Ans D
    q.append(make_q(
        "ISR_M_020", "Tribunals & Basin States",
        "The Mahadayi (Mandovi) Water Disputes Tribunal constituted in 2010 resolved water allocation disputes among which three riparian States?",
        "2010 ஆம் ஆண்டில் அமைக்கப்பட்ட மகதாயி (மாண்டோவி) நதிநீர் தகராறுகள் தீர்ப்பாயம் எந்த மூன்று நதிப் படுகை மாநிலங்களுக்கிடையேயான நீர் ஒதுக்கீட்டுத் தகராறுகளைத் தீர்த்தது?",
        "Gujarat, Rajasthan, and Madhya Pradesh", "குஜராத், ராஜஸ்தான் மற்றும் மத்தியப் பிரதேசம்",
        "Odisha, Andhra Pradesh, and Chhattisgarh", "ஒடிசா, ஆந்திரப் பிரதேசம் மற்றும் சத்தீஸ்கர்",
        "Tamil Nadu, Kerala, and Karnataka", "தமிழ்நாடு, கேரளா மற்றும் கர்நாடகா",
        "Goa, Karnataka, and Maharashtra", "கோவா, கர்நாடகா மற்றும் மகாராஷ்டிரா",
        "D",
        "The Mahadayi Water Disputes Tribunal (headed by Justice J.M. Panchal) was constituted in November 2010 to adjudicate disputes over the Mahadayi/Mandovi river among Goa, Karnataka, and Maharashtra (particularly regarding the Kalasa-Banduri project).",
        "2010 நவம்பரில் அமைக்கப்பட்ட மகதாயி நதிநீர் தகராறுகள் தீர்ப்பாயம் (நீதிபதி ஜே.எம். பஞ்சால் தலைமையில்), கோவா, கர்நாடகா மற்றும் மகாராஷ்டிரா ஆகியவற்றுக்கிடையே மகதாயி/மாண்டோவி நதி நீர் தொடர்பான தகராறுகளை (குறிப்பாக கலசா-பண்டூரி திட்டம்) தீர்க்க அமைக்கப்பட்டது.",
        "Gujarat, Rajasthan, and MP are involved in Narmada/Sabarmati, not Mahadayi.", "குஜராத், ராஜஸ்தான், ம.பி நர்மதா தொடர்புடையவை.",
        "Odisha, AP, and Chhattisgarh are involved in Vansadhara/Mahanadi.", "ஒடிசா, ஆந்திரா, சத்தீஸ்கர் வம்சதாரா/மகாநதி தொடர்புடையவை.",
        "Tamil Nadu, Kerala, and Karnataka are involved in Cauvery.", "தமிழ்நாடு, கேரளா, கர்நாடகா காவிரி தொடர்புடையவை.",
        "Goa, Karnataka, and Maharashtra are the riparian States of the Mahadayi river.", "கோவா, கர்நாடகா மற்றும் மகாராஷ்டிரா ஆகியவை மகதாயி நதியின் படுகை மாநிலங்கள் ஆகும்.",
        "Mahadayi dispute centers on Karnataka's proposal to divert water to Malaprabha basin, opposed by Goa.",
        "மகதாயி தகராறு மலபிரபா படுகைக்குத் தண்ணீரைத் திருப்ப கர்நாடகா முன்மொழிந்ததை கோவா எதிர்த்ததை மையமாகக் கொண்டது.",
        "Mahadayi Water Disputes Tribunal = Goa, Karnataka, Maharashtra.",
        "மகதாயி நதிநீர் தகராறுகள் தீர்ப்பாயம் = கோவா, கர்நாடகா, மகாராஷ்டிரா.",
        tags=["Mahadayi Tribunal", "Goa", "Karnataka", "Maharashtra"]
    ))

    # 021 - Ans A
    q.append(make_q(
        "ISR_M_021", "Tribunals & Basin States",
        "The Vansadhara Water Disputes Tribunal, constituted in 2010, was tasked with resolving the water sharing dispute between which two States?",
        "2010-ல் அமைக்கப்பட்ட வம்சதாரா நதிநீர் தகராறுகள் தீர்ப்பாயத்திடம் எந்த இரு மாநிலங்களுக்கு இடையிலான நீர் பகிர்வு தகராறைத் தீர்க்கும் பணி ஒப்படைக்கப்பட்டது?",
        "Odisha and Andhra Pradesh", "ஒடிசா மற்றும் ஆந்திரப் பிரதேசம்",
        "Chhattisgarh and Odisha", "சத்தீஸ்கர் மற்றும் ஒடிசா",
        "Telangana and Andhra Pradesh", "தெலுங்கானா மற்றும் ஆந்திரப் பிரதேசம்",
        "Karnataka and Kerala", "கர்நாடகா மற்றும் கேரளா",
        "A",
        "The Vansadhara Water Disputes Tribunal was constituted in February 2010 to adjudicate the dispute between Odisha and Andhra Pradesh regarding the construction of the Neradi barrage and Katragada side weir.",
        "நேரடி அணைக்கட்டு மற்றும் கத்ரகடா பக்கவாட்டு தடுப்பணை கட்டுமானம் தொடர்பாக ஒடிசா மற்றும் ஆந்திரப் பிரதேசம் இடையே எழுந்த தகராறைத் தீர்க்க 2010 பிப்ரவரியில் வம்சதாரா நதிநீர் தகராறுகள் தீர்ப்பாயம் அமைக்கப்பட்டது.",
        "Odisha and Andhra Pradesh are the two disputing states in the Vansadhara basin.", "ஒடிசா மற்றும் ஆந்திரப் பிரதேசம் வம்சதாரா படுகையின் தகராறுக்குரிய இரு மாநிலங்கள் ஆகும்.",
        "Chhattisgarh and Odisha are the disputing states for the Mahanadi river.", "சத்தீஸ்கரும் ஒடிசாவும் மகாநதி நதிக்கான தகராறு மாநிலங்கள்.",
        "Telangana and Andhra Pradesh dispute Krishna and Godavari waters under the AP Reorganisation Act 2014.", "தெலுங்கானாவும் ஆந்திராவும் கிருஷ்ணா, கோதாவரி நீரைப் பகிர்வதில் தகராறு கொண்டுள்ளன.",
        "Karnataka and Kerala dispute Cauvery waters.", "கர்நாடகாவும் கேரளாவும் காவிரி நதிநீரில் தகராறு கொண்டுள்ளன.",
        "Vansadhara River originates in Odisha and flows into Andhra Pradesh before joining the Bay of Bengal.",
        "வம்சதாரா நதி ஒடிசாவில் உற்பத்தியாகி ஆந்திரப் பிரதேசம் வழியாக வங்காள விரிகுடாவில் கலக்கிறது.",
        "Vansadhara Water Disputes Tribunal = Odisha and Andhra Pradesh.",
        "வம்சதாரா நதிநீர் தகராறுகள் தீர்ப்பாயம் = ஒடிசா மற்றும் ஆந்திரப் பிரதேசம்.",
        tags=["Vansadhara Tribunal", "Odisha", "Andhra Pradesh"]
    ))

    # 022 - Ans B
    q.append(make_q(
        "ISR_M_022", "Tribunals & Basin States",
        "The Mahanadi Water Disputes Tribunal, constituted in March 2018 under Justice A.M. Khanwilkar, addresses the river water dispute between which two States?",
        "நீதிபதி ஏ.எம். கான்வில்கர் தலைமையில் மார்ச் 2018-ல் அமைக்கப்பட்ட மகாநதி நதிநீர் தகராறுகள் தீர்ப்பாயம், எந்த இரு மாநிலங்களுக்கு இடையேயான நதிநீர் தகராறை விசாரிக்கிறது?",
        "Madhya Pradesh and Odisha", "மத்தியப் பிரதேசம் மற்றும் ஒடிசா",
        "Chhattisgarh and Odisha", "சத்தீஸ்கர் மற்றும் ஒடிசா",
        "Jharkhand and West Bengal", "ஜார்க்கண்ட் மற்றும் மேற்கு வங்காளம்",
        "Odisha and West Bengal", "ஒடிசா மற்றும் மேற்கு வங்காளம்",
        "B",
        "The Mahanadi Water Disputes Tribunal was constituted by the Central Government on 12 March 2018 following a Supreme Court directive to resolve the water sharing conflict between Chhattisgarh (upper riparian) and Odisha (lower riparian).",
        "மேல்மட்ட மாநிலமான சத்தீஸ்கர் மற்றும் கீழ்மட்ட மாநிலமான ஒடிசா ஆகியவற்றுக்கு இடையேயான நதிநீர் பகிர்வு மோதலைத் தீர்க்க உச்ச நீதிமன்ற உத்தரவைத் தொடர்ந்து 2018 மார்ச் 12 அன்று மத்திய அரசால் மகாநதி நதிநீர் தகராறுகள் தீர்ப்பாயம் அமைக்கப்பட்டது.",
        "Madhya Pradesh is not a primary disputing party in the Mahanadi tribunal.", "மத்தியப் பிரதேசம் மகாநதி தீர்ப்பாயத்தின் முதன்மைத் தரப்பினர் அல்ல.",
        "Chhattisgarh and Odisha are the two core parties to the Mahanadi dispute.", "சத்தீஸ்கர் மற்றும் ஒடிசா மகாநதி தகராறின் இரு முக்கியத் தரப்பினர்கள் ஆவர்.",
        "Jharkhand and West Bengal dispute Damodar/Subarnarekha waters, not Mahanadi.", "ஜார்க்கண்ட் மற்றும் மேற்கு வங்கம் தாமோதர்/சுவர்ணரேகா நதிகளுடன் தொடர்புடையவை.",
        "Odisha and West Bengal do not dispute Mahanadi waters.", "ஒடிசாவும் மேற்கு வங்கமும் மகாநதி நீரில் தகராறு கொண்டிருக்கவில்லை.",
        "Mahanadi dispute arose over Chhattisgarh constructing barrages upstream, reducing water flow to Odisha's Hirakud dam.",
        "சத்தீஸ்கர் மேல்நோக்கி தடுப்பணைகளைக் கட்டியதால் ஒடிசாவின் ஹிராகுட் அணைக்கு நீர்வரத்து குறைந்ததால் மகாநதி தகராறு எழுந்தது.",
        "Mahanadi Water Disputes Tribunal (2018) = Chhattisgarh and Odisha.",
        "மகாநதி நதிநீர் தகராறுகள் தீர்ப்பாயம் (2018) = சத்தீஸ்கர் மற்றும் ஒடிசா.",
        tags=["Mahanadi Tribunal", "Chhattisgarh", "Odisha", "2018"]
    ))

    # 023 - Ans C
    q.append(make_q(
        "ISR_M_023", "Zonal Councils Procedure",
        "Under Section 17 of the States Reorganisation Act 1956, how are joint meetings of two or more Zonal Councils conducted?",
        "1956 ஆம் ஆண்டின் மாநில மறுசீரமைப்புச் சட்டத்தின் பிரிவு 17-ன் கீழ், இரண்டு அல்லது அதற்கு மேற்பட்ட மண்டலக் குழுக்களின் கூட்டுக் கூட்டங்கள் எவ்வாறு நடத்தப்படுகின்றன?",
        "They are presided over by the Chief Justice of India", "அவை இந்தியத் தலைமை நீதிபதியால் தலைமை தாங்கப்படுகின்றன",
        "The Chief Ministers of all attending States act as co-chairmen jointly", "பங்கேற்கும் அனைத்து மாநிலங்களின் முதலமைச்சர்களும் கூட்டாக இணைத் தலைவர்களாகச் செயல்படுகின்றனர்",
        "They are presided over by the Union Home Minister, who is the common Chairman", "அவை பொதுவான தலைவரான மத்திய உள்துறை அமைச்சரால் தலைமை தாங்கப்படுகின்றன",
        "Joint meetings of Zonal Councils are legally prohibited under the Act", "மண்டலக் குழுக்களின் கூட்டுக் கூட்டங்கள் சட்டத்தின் கீழ் சட்டப்பூர்வமாகத் தடை செய்யப்பட்டுள்ளன",
        "C",
        "Section 17 of the States Reorganisation Act 1956 explicitly provides that where two or more Zonal Councils desire to discuss matters in which they have a joint interest, they may hold a joint meeting, and such meeting shall be presided over by the Chairman of the Zonal Councils (the Union Home Minister).",
        "1956 மாநில மறுசீரமைப்புச் சட்டத்தின் பிரிவு 17, இரண்டு அல்லது அதற்கு மேற்பட்ட மண்டலக் குழுக்கள் பொதுவான நலன் சார்ந்த விஷயங்களை விவாதிக்க விரும்பினால், அவை ஒரு கூட்டுக் கூட்டத்தை நடத்தலாம் என்றும், அத்தகைய கூட்டத்திற்கு மண்டலக் குழுக்களின் தலைவரான மத்திய உள்துறை அமைச்சர் தலைமை தாங்குவார் என்றும் வெளிப்படையாகக் கூறுகிறது.",
        "The CJI has no statutory role in Zonal Councils.", "CJI-க்கு மண்டலக் குழுக்களில் சட்டப்பூர்வப் பங்கு இல்லை.",
        "Chief Ministers do not co-chair joint meetings.", "முதலமைச்சர்கள் கூட்டுக் கூட்டங்களுக்கு இணைத் தலைமை தாங்குவதில்லை.",
        "The Union Home Minister presides over all joint meetings of Zonal Councils.", "மத்திய உள்துறை அமைச்சர் மண்டலக் குழுக்களின் அனைத்துக் கூட்டுக் கூட்டங்களுக்கும் தலைமை தாங்குகிறார்.",
        "Joint meetings are explicitly permitted by Section 17, not prohibited.", "கூட்டுக் கூட்டங்கள் பிரிவு 17-ஆல் வெளிப்படையாக அனுமதிக்கப்பட்டுள்ளன.",
        "Section 17 SRA 1956 permits joint meetings of Zonal Councils, presided over by the Union Home Minister.",
        "1956 சட்டத்தின் பிரிவு 17 மண்டலக் குழுக்களின் கூட்டுக் கூட்டங்களை அனுமதிக்கிறது; உள்துறை அமைச்சர் தலைமை தாங்குகிறார்.",
        "Joint meetings of Zonal Councils are presided over by the Union Home Minister.",
        "மண்டலக் குழுக்களின் கூட்டுக் கூட்டங்களுக்கு மத்திய உள்துறை அமைச்சர் தலைமை தாங்குகிறார்.",
        tags=["Zonal Councils", "Joint Meetings", "Section 17"]
    ))

    # 024 - Ans D
    q.append(make_q(
        "ISR_M_024", "Original Jurisdiction Analysis",
        "In State of West Bengal v. Union of India (1963), what did the Supreme Court determine regarding the nature of disputes maintainable under Article 131?",
        "மேற்கு வங்காள மாநிலம் vs இந்திய ஒன்றியம் (1963) வழக்கில், உறுப்பு 131-ன் கீழ் ஏற்றுக்கொள்ளப்படத் தக்க தகராறுகளின் தன்மை குறித்து உச்ச நீதிமன்றம் என்ன தீர்மானித்தது?",
        "Any political or policy dispute between parties can be adjudicated under Article 131.", "கட்சிகளுக்கிடையேயான எந்தவொரு அரசியல் அல்லது கொள்கைத் தகராறையும் உறுப்பு 131-ன் கீழ் விசாரிக்கலாம்.",
        "A private corporation can join a State as a co-plaintiff under Article 131.", "ஒரு தனியார் கழகம் உறுப்பு 131-ன் கீழ் ஒரு மாநிலத்துடன் இணைந்து வாதியாகச் சேரலாம்.",
        "The dispute must relate solely to boundary delimitations between States.", "தகராறு மாநிலங்களுக்கிடையேயான எல்லை நிர்ணயம் தொடர்பாக மட்டுமே இருக்க வேண்டும்.",
        "The dispute must involve a question of law or fact on which the existence or extent of a legal right depends; purely political disputes are excluded.", "தகராறானது ஒரு சட்ட உரிமையின் இருப்பு அல்லது எல்லையைத் தீர்மானிக்கும் சட்ட அல்லது உண்மை கேள்வியைக் கொண்டிருக்க வேண்டும்; முற்றிலும் அரசியல் தகராறுகள் விலக்கப்படுகின்றன.",
        "D",
        "In State of West Bengal v. UOI (1963), the Supreme Court clarified that for a dispute to be maintainable under Article 131, it must involve a question of law or fact on which the existence or extent of a LEGAL RIGHT depends. Purely political disagreements or non-legal policy disputes between political parties cannot be entertained under Article 131.",
        "மேற்கு வங்காளம் vs இந்திய ஒன்றியம் (1963) வழக்கில், உறுப்பு 131-ன் கீழ் ஒரு வழக்கு ஏற்றுக்கொள்ளப்பட வேண்டுமெனில், அது ஒரு சட்ட உரிமையின் (legal right) இருப்பு அல்லது எல்லையைத் தீர்மானிக்கும் சட்ட அல்லது உண்மை கேள்வியைக் கொண்டிருக்க வேண்டும் என்று உச்ச நீதிமன்றம் தெளிவுபடுத்தியது. வெறும் அரசியல் கருத்து வேறுபாடுகள் உறுப்பு 131-ன் கீழ் ஏற்றுக்கொள்ளப்பட மாட்டாது.",
        "Pure political disputes without legal rights are strictly barred under Art 131.", "சட்ட உரிமையற்ற வெறும் அரசியல் தகராறுகள் உறுப்பு 131-ன் கீழ் கண்டிப்பாகத் தடை செய்யப்பட்டுள்ளன.",
        "Private corporations CANNOT be parties to an Article 131 suit.", "தனியார் நிறுவனங்கள் உறுப்பு 131 வழக்கில் தரப்பினராக இருக்க முடியாது.",
        "Disputes are not restricted to boundaries; any dispute involving a legal right qualifies.", "தகராறுகள் எல்லைகளுக்கு மட்டுமே மட்டுப்படுத்தப்பட்டவை அல்ல.",
        "Option D correctly highlights the mandatory requirement of an existing 'legal right'.", "விருப்பம் D ஓர் 'சட்ட உரிமை' இருக்க வேண்டும் என்ற கட்டாயத் தேவையைச் சரியாக விளக்குகிறது.",
        "Article 131 requires a dispute involving a LEGAL RIGHT (State of West Bengal v. UOI 1963); political questions are non-justiciable.",
        "உறுப்பு 131 ஒரு 'சட்ட உரிமை' சார்ந்த தகராறைக் கோருகிறது; அரசியல் விவகாரங்கள் விசாரிக்கப்படத் தக்கவை அல்ல.",
        "Article 131 requires a question on which a legal right depends.",
        "உறுப்பு 131 ஒரு சட்ட உரிமை சார்ந்த கேள்வியைக் கொண்டிருக்க வேண்டும்.",
        tags=["Article 131", "Legal Right", "West Bengal v. UOI"]
    ))

    # 025 - Ans A
    q.append(make_q(
        "ISR_M_025", "Scope of Article 301",
        "Does the freedom of trade, commerce, and intercourse guaranteed by Article 301 apply only to movement between different States or also to movement within a State?",
        "உறுப்பு 301-ன் கீழ் உத்தரவாதம் அளிக்கப்பட்ட வர்த்தகம், வாணிபம் மற்றும் தொடர்பின் சுதந்திரம் வெவ்வேறு மாநிலங்களுக்கு இடையேயான இயக்கத்திற்கு மட்டுமே பொருந்துமா அல்லது ஒரு மாநிலத்திற்கு உட்பட்ட இயக்கத்திற்கும் பொருந்துமா?",
        "It applies to both inter-State trade (between States) and intra-State trade (within a State).", "இது மாநிலங்களுக்கு இடையிலான வர்த்தகம் (States between) மற்றும் மாநிலத்திற்கு உட்பட்ட வர்த்தகம் (intra-State) ஆகிய இரண்டிற்கும் பொருந்தும்.",
        "It applies exclusively to inter-State trade; intra-State trade is governed solely by State law.", "இது மாநிலங்களுக்கு இடையிலான வர்த்தகத்திற்கு மட்டுமே பொருந்தும்; மாநிலத்திற்கு உட்பட்ட வர்த்தகம் மாநிலச் சட்டத்தால் மட்டுமே நிர்வகிக்கப்படுகிறது.",
        "It applies only to cross-border movement involving international ports.", "இது சர்வதேச துறைமுகங்களை உள்ளடக்கிய எல்லை தாண்டிய இயக்கத்திற்கு மட்டுமே பொருந்தும்.",
        "It applies to Union Territories only, not to autonomous States.", "இது யூனியன் பிரதேசங்களுக்கு மட்டுமே பொருந்தும், தன்னாட்சி மாநிலங்களுக்குப் பொருந்தாது.",
        "A",
        "The words 'throughout the territory of India' in Article 301 clearly extend the freedom to both inter-State trade (movement from one State to another) and intra-State trade (movement from one place to another within the same State). Trade barriers within a State are equally violative of Article 301 unless constitutionally saved.",
        "உறுப்பு 301-ல் உள்ள 'இந்தியா முழுவதும்' (throughout the territory of India) என்ற சொற்கள், மாநிலங்களுக்கு இடையிலான வர்த்தகம் மற்றும் மாநிலத்திற்கு உட்பட்ட வர்த்தகம் ஆகிய இரண்டிற்கும் இச்சுதந்திரத்தை விரிவுபடுத்துகின்றன. ஒரு மாநிலத்திற்குள்ளேயே வர்த்தகத் தடைகளை ஏற்படுத்துவதும் உறுப்பு 301-ஐ மீறுவதாகும்.",
        "Option A correctly states the dual application of Article 301 to inter-State and intra-State trade.", "விருப்பம் A உறுப்பு 301 மாநிலங்களுக்கு இடையிலான மற்றும் மாநிலத்திற்கு உட்பட்ட வர்த்தகத்திற்குப் பொருந்தும் என்பதைச் சரியாகக் கூறுகிறது.",
        "Limiting it only to inter-State trade is a common misconception; the text says 'throughout the territory of India'.", "மாநிலங்களுக்கு இடையே மட்டுமே என வரம்பிடுவது தவறானது; அரசியலமைப்பு உரை 'இந்தியா முழுவதும்' எனக் கூறுகிறது.",
        "International trade is outside the scope of Part XIII (governed by Entry 41, Union List).", "சர்வதேச வர்த்தகம் பகுதி XIII-ன் வரம்பிற்கு அப்பாற்பட்டது.",
        "It applies to the entire territory of India (all States and UTs).", "இது இந்தியாவின் அனைத்துப் பகுதிகளுக்கும் (அனைத்து மாநிலங்கள் மற்றும் யூ.பி-க்கள்) பொருந்தும்.",
        "Article 301 applies 'throughout the territory of India' — covering BOTH inter-State and intra-State trade.",
        "உறுப்பு 301 'இந்தியா முழுவதும்' பொருந்தும் — மாநிலங்களுக்கு இடையேயான மற்றும் மாநிலத்திற்கு உட்பட்ட வர்த்தகம் இரண்டையும் உள்ளடக்கியது.",
        "Article 301 covers both inter-State and intra-State trade freedom.",
        "உறுப்பு 301 மாநிலங்களுக்கு இடையிலான மற்றும் மாநிலத்திற்கு உட்பட்ட வர்த்தக சுதந்திரத்தை உள்ளடக்கியது.",
        tags=["Article 301", "Inter-State vs Intra-State"]
    ))

    # 026 - Ans B
    q.append(make_q(
        "ISR_M_026", "Constitutional Saving Clause",
        "How does Article 305 protect State monopolies created by the Government in commercial activities from being challenged under Article 301?",
        "வணிக நடவடிக்கைகளில் அரசாங்கத்தால் உருவாக்கப்படும் அரசு ஏகபோகங்களை உறுப்பு 301-ன் கீழ் கேள்விக்குள்ளாக்குவதிலிருந்து உறுப்பு 305 எவ்வாறு பாதுகாக்கிறது?",
        "By empowering the Supreme Court to grant exemptions to Public Sector Undertakings.", "பொதுத்துறை நிறுவனங்களுக்கு விலக்கு அளிக்க உச்ச நீதிமன்றத்திற்கு அதிகாரம் அளிப்பதன் மூலம்.",
        "By explicitly providing that nothing in Article 301 shall affect any law relating to the carrying on of any trade, business, industry, or service by the State or a State-owned corporation to the exclusion of citizens.", "குடிமக்களை விலக்கி, அரசு அல்லது அரசுக்குச் சொந்தமான கழகத்தால் எந்தவொரு வர்த்தகம், வணிகம், தொழில் அல்லது சேவையை நடத்துவது தொடர்பான எந்தவொரு சட்டத்தையும் உறுப்பு 301 பாதிக்காது என்று வெளிப்படையாகக் கூறுவதன் மூலம்.",
        "By requiring State monopolies to be approved by a 2/3rd majority of the Inter-State Council.", "அரசு ஏகபோகங்களுக்கு மாநிலங்களுக்கு இடையிலான மன்றத்தின் 2/3 பங்கு பெரும்பான்மை ஒப்புதல் தேவைப்படுவதன் மூலம்.",
        "By declaring that State monopolies are Fundamental Rights under Article 19.", "அரசு ஏகபோகங்கள் உறுப்பு 19-ன் கீழ் அடிப்படை உரிமைகள் என்று அறிவிப்பதன் மூலம்.",
        "B",
        "Article 305 (as amended by the 4th Amendment Act 1955) expressly saves laws creating State monopolies (whether to the complete or partial exclusion of citizens) from the operation of Article 301. Consequently, nationalization of transport or industries by the Union or States cannot be challenged as an infringement of trade freedom under Article 301.",
        "உறுப்பு 305 (1955-ன் 4-வது திருத்தச் சட்டத்தால் திருத்தப்பட்டது), அரசு ஏகபோகங்களை உருவாக்கும் சட்டங்களை உறுப்பு 301-ன் செயல்பாட்டிலிருந்து வெளிப்படையாகப் பாதுகாக்கிறது. எனவே, ஒன்றியம் அல்லது மாநிலங்களால் போக்குவரத்து அல்லது தொழில்களைத் தேசியமயமாக்குவதை வர்த்தக சுதந்திரத்தை மீறுவதாக உறுப்பு 301-ன் கீழ் சவால் செய்ய முடியாது.",
        "The Supreme Court does not grant discretionary exemptions under Article 305.", "உச்ச நீதிமன்றம் உறுப்பு 305-ன் கீழ் தன்னிச்சையான விலக்குகளை வழங்குவதில்லை.",
        "Option B accurately captures the constitutional text and protection of State monopolies under Article 305.", "விருப்பம் B உறுப்பு 305-ன் கீழான அரசு ஏகபோகங்களின் பாதுகாப்பைத் துல்லியமாக விளக்குகிறது.",
        "The Inter-State Council has no approval power over State monopolies.", "மாநிலங்களுக்கு இடையிலான மன்றத்திற்கு அரசு ஏகபோகங்கள் மீது ஒப்புதல் அளிக்கும் அதிகாரம் இல்லை.",
        "State monopolies are not fundamental rights; they are exceptions created under Art 19(6)(ii) and saved by Art 305.", "அரசு ஏகபோகங்கள் அடிப்படை உரிமைகள் அல்ல; அவை விதிவிலக்குகளாகும்.",
        "Article 305 completely insulates State trading monopolies (Central or State) from challenge under Article 301.",
        "உறுப்பு 305 அரசு வணிக ஏகபோகங்களை உறுப்பு 301-ன் கீழ் சவால் செய்யப்படுவதிலிருந்து முழுமையாகப் பாதுகாக்கிறது.",
        "Article 305 saves laws creating State monopolies from Article 301.",
        "உறுப்பு 305 அரசு ஏகபோகங்களை உருவாக்கும் சட்டங்களை உறுப்பு 301 இலிருந்து பாதுகாக்கிறது.",
        tags=["Article 305", "State Monopolies"]
    ))

    # 027 - Ans C
    q.append(make_q(
        "ISR_M_027", "Commission Recommendations",
        "What specific structural recommendation did the Sarkaria Commission on Centre-State Relations (1988) make regarding Article 307 of the Constitution?",
        "அரசியலமைப்பு உறுப்பு 307 தொடர்பாக மத்திய-மாநில உறவுகள் குறித்த சர்க்காரியா ஆணையம் (1988) என்ன குறிப்பிட்ட கட்டமைப்புப் பரிந்துரையை வழங்கியது?",
        "Article 307 should be immediately repealed as obsolete.", "உறுப்பு 307 பயனற்றதாகிவிட்டதால் உடனடியாக நீக்கப்பட வேண்டும்.",
        "The power under Article 307 should be transferred entirely to the Reserve Bank of India.", "உறுப்பு 307-ன் கீழான அதிகாரம் முழுவதும் இந்திய ரிசர்வ் வங்கிக்கு மாற்றப்பட வேண்டும்.",
        "An expert statutory authority called the 'Inter-State Trade and Commerce Commission' should be appointed under Article 307 to monitor and resolve inter-State trade barriers.", "மாநிலங்களுக்கிடையேயான வர்த்தகத் தடைகளைக் கண்காணிக்கவும் தீர்க்கவும் உறுப்பு 307-ன் கீழ் 'மாநிலங்களுக்கு இடையிலான வர்த்தகம் மற்றும் வணிக ஆணையம்' என்ற நிபுணர் சட்டப்பூர்வ அமைப்பு நியமிக்கப்பட வேண்டும்.",
        "Article 307 should be amended to merge trade regulatory powers with the Goods and Services Tax Network.", "வர்த்தக ஒழுங்குமுறை அதிகாரங்களை ஜிஎஸ்டி நெட்வொர்க்குடன் இணைக்க உறுப்பு 307 திருத்தப்பட வேண்டும்.",
        "C",
        "The Sarkaria Commission strongly recommended setting up an autonomous expert authority under Article 307, to be designated as the 'Inter-State Trade and Commerce Commission', with both advisory and dispute-settling functions to maintain an unhindered common economic market.",
        "சர்க்காரியா ஆணையம், தடையற்ற பொதுவான பொருளாதாரச் சந்தையைப் பேணுவதற்காக ஆலோசனை மற்றும் தகராறு தீர்க்கும் பணிகளுடன், 'மாநிலங்களுக்கு இடையிலான வர்த்தகம் மற்றும் வணிக ஆணையம்' என்ற தன்னாட்சி நிபுணர் அதிகார அமைப்பை உறுப்பு 307-ன் கீழ் அமைக்க வலுவாகப் பரிந்துரைத்தது.",
        "Sarkaria did not recommend repealing Article 307; it recommended actually implementing it.", "சர்க்காரியா ஆணையம் உறுப்பு 307-ஐ நீக்கப் பரிந்துரைக்கவில்லை; அதைச் செயல்படுத்தவே பரிந்துரைத்தது.",
        "RBI is a monetary authority, not a general trade commission.", "ஆர்பிஐ பணவியல் அமைப்பு, பொது வர்த்தக ஆணையம் அல்ல.",
        "Option C reflects Sarkaria Commission's famous recommendation under Article 307.", "விருப்பம் C சர்க்காரியா ஆணையத்தின் உறுப்பு 307-ன் கீழான புகழ்பெற்ற பரிந்துரையைப் பிரதிபலிக்கிறது.",
        "GST was introduced decades later; this was not part of the 1988 report.", "ஜிஎஸ்டி பல தசாப்தங்களுக்குப் பின்னரே அறிமுகப்படுத்தப்பட்டது.",
        "Sarkaria Commission recommended establishing an Inter-State Trade and Commerce Commission under Article 307.",
        "சர்க்காரியா ஆணையம் உறுப்பு 307-ன் கீழ் மாநிலங்களுக்கு இடையிலான வர்த்தக மற்றும் வணிக ஆணையத்தை அமைக்கப் பரிந்துரைத்தது.",
        "Sarkaria Commission recommended an Inter-State Trade and Commerce Commission under Art 307.",
        "சர்க்காரியா ஆணையம் உறுப்பு 307-ன் கீழ் வர்த்தக ஆணையத்தை அமைக்கப் பரிந்துரைத்தது.",
        tags=["Sarkaria Commission", "Article 307", "Trade Commission"]
    ))

    # 028 - Ans D
    q.append(make_q(
        "ISR_M_028", "Commission Recommendations",
        "What major structural reform did the Punchhi Commission on Centre-State Relations (2010) recommend to energize the Inter-State Council?",
        "மாநிலங்களுக்கு இடையிலான மன்றத்தை உற்சாகப்படுத்த மத்திய-மாநில உறவுகள் குறித்த பூஞ்சி ஆணையம் (2010) என்ன முக்கிய கட்டமைப்புச் சீர்திருத்தத்தைப் பரிந்துரைத்தது?",
        "Dissolve the Inter-State Council and replace it with a Judicial Water Council.", "மாநிலங்களுக்கு இடையிலான மன்றத்தைக் கலைத்துவிட்டு அதற்குப் பதிலாக ஒரு நீதித்துறை நீர் மன்றத்தை அமைத்தல்.",
        "Transfer the Inter-State Council directly under the administrative control of the NITI Aayog.", "மாநிலங்களுக்கு இடையிலான மன்றத்தை நேரடியாக நிதி ஆயோக்கின் நிர்வாகக் கட்டுப்பாட்டின் கீழ் மாற்றுதல்.",
        "Abolish the Standing Committee and hold monthly open parliamentary debates.", "நிலைக் குழுவை ஒழித்துவிட்டு மாதாந்திர திறந்த நாடாளுமன்ற விவாதங்களை நடத்துதல்.",
        "The Inter-State Council must meet at least thrice a year, its Secretariat should be substantially strengthened, and it should act as a vibrant forum for national consensus on federal policies.", "மாநிலங்களுக்கு இடையிலான மன்றம் ஆண்டில் குறைந்தது மூன்று முறையாவது கூட வேண்டும், அதன் செயலகம் கணிசமாக பலப்படுத்தப்பட வேண்டும், மேலும் கூட்டாட்சிக் கொள்கைகளில் தேசிய ஒருமித்த கருத்திற்கான துடிப்பான மன்றமாக அது செயல்பட வேண்டும்.",
        "D",
        "The Punchhi Commission (2010) observed that the Inter-State Council had not been utilized effectively and recommended: (i) strict adherence to the mandate of holding at least 3 meetings annually; (ii) strengthening the Secretariat of the ISC with professional staff; and (iii) using it for prior consultation on federal legislation.",
        "பூஞ்சி ஆணையம் (2010) மாநிலங்களுக்கு இடையிலான மன்றம் திறம்படப் பயன்படுத்தப்படவில்லை என்று குறிப்பிட்டது: (i) ஆண்டுக்கு குறைந்தது 3 கூட்டங்கள் நடத்தும் விதியை கண்டிப்பாகப் பின்பற்றுதல்; (ii) மன்றத்தின் செயலகத்தை நிபுணத்துவ ஊழியர்களுடன் பலப்படுத்துதல்; (iii) கூட்டாட்சிச் சட்டங்களில் முன் ஆலோசனைக்கு இதைப் பயன்படுத்துதல் எனப் பரிந்துரைத்தது.",
        "Punchhi Commission did not recommend dissolving the ISC.", "பூஞ்சி ஆணையம் மன்றத்தைக் கலைக்கப் பரிந்துரைக்கவில்லை.",
        "It did not recommend placing it under NITI Aayog.", "அதை நிதி ஆயோக்கின் கீழ் வைக்கப் பரிந்துரைக்கவில்லை.",
        "It supported maintaining and empowering the Standing Committee, not abolishing it.", "அது நிலைக் குழுவை ஒழிக்கப் பரிந்துரைக்கவில்லை.",
        "Option D accurately outlines Punchhi Commission's core recommendations for strengthening the Inter-State Council.", "விருப்பம் D மாநிலங்களுக்கு இடையிலான மன்றத்தைப் பலப்படுத்துவதற்கான பூஞ்சி ஆணையத்தின் முக்கியப் பரிந்துரைகளை விளக்குகிறது.",
        "Punchhi Commission (2010) on ISC: Mandate 3 meetings a year, strengthen the Secretariat, and consult ISC before introducing concurrent list bills.",
        "பூஞ்சி ஆணையம் (2010): ஆண்டில் 3 கூட்டங்கள், பலமான செயலகம், மற்றும் பொதுப் பட்டியல் மசோதாக்களுக்கு முன் ISC-ல் ஆலோசனை.",
        "Punchhi Commission recommended strengthening ISC with at least 3 meetings a year.",
        "பூஞ்சி ஆணையம் ஆண்டில் குறைந்தது 3 கூட்டங்களுடன் ISC-ஐப் பலப்படுத்தப் பரிந்துரைத்தது.",
        tags=["Punchhi Commission", "Inter-State Council"]
    ))

    # 029 - Ans A
    q.append(make_q(
        "ISR_M_029", "Commission Terminology",
        "What specific nomenclature did the Sarkaria Commission (1988) suggest for the permanent council to be set up under Article 263 to differentiate it from temporary advisory bodies?",
        "தற்காலிக ஆலோசனை அமைப்புகளிலிருந்து வேறுபடுத்துவதற்காக உறுப்பு 263-ன் கீழ் அமைக்கப்பட வேண்டிய நிரந்தர மன்றத்திற்கு சர்க்காரியா ஆணையம் (1988) என்ன குறிப்பிட்ட பெயரைப் பரிந்துரைத்தது?",
        "Inter-Governmental Council", "அரசுகளுக்கிடையேயான மன்றம் (Inter-Governmental Council)",
        "National Federal Tribunal", "தேசியக் கூட்டாட்சித் தீர்ப்பாயம்",
        "Council of States Coordination", "மாநிலங்கள் ஒருங்கிணைப்பு மன்றம்",
        "Inter-State Administrative Chamber", "மாநிலங்களுக்கு இடையிலான நிர்வாக அறை",
        "A",
        "To distinguish the permanent body from ad hoc councils set up under Article 263 for specific subjects (such as Central Council of Health, Central Council of Local Self-Government), the Sarkaria Commission recommended that the general council be named the 'Inter-Governmental Council'. However, the 1990 Presidential Order retained the title 'Inter-State Council'.",
        "குறிப்பிட்ட பாடங்களுக்காக உறுப்பு 263-ன் கீழ் அமைக்கப்பட்ட தற்காலிக மன்றங்களிலிருந்து (மத்திய சுகாதார கவுன்சில், உள்ளாட்சி கவுன்சில் போன்றவை) நிரந்தர அமைப்பை வேறுபடுத்துவதற்காக, பொது மன்றத்திற்கு 'அரசுகளுக்கிடையேயான மன்றம்' (Inter-Governmental Council) என்று பெயரிட சர்க்காரியா ஆணையம் பரிந்துரைத்தது.",
        "Option A represents the exact term recommended by the Sarkaria Commission.", "விருப்பம் A சர்க்காரியா ஆணையத்தால் பரிந்துரைக்கப்பட்ட சரியான சொல்லாகும்.",
        "It was not named National Federal Tribunal.", "தேசியக் கூட்டாட்சித் தீர்ப்பாயம் என்று பெயரிடப்படவில்லை.",
        "Council of States Coordination is incorrect.", "மாநிலங்கள் ஒருங்கிணைப்பு மன்றம் என்பது தவறானது.",
        "Inter-State Administrative Chamber is incorrect.", "மாநிலங்களுக்கு இடையிலான நிர்வாக அறை என்பது தவறானது.",
        "Sarkaria Commission recommended the name 'Inter-Governmental Council' under Article 263, though it was notified as 'Inter-State Council'.",
        "சர்க்காரியா ஆணையம் 'அரசுகளுக்கிடையேயான மன்றம்' என்ற பெயரைப் பரிந்துரைத்தது, இருப்பினும் 'மாநிலங்களுக்கு இடையிலான மன்றம்' என்றே அறிவிக்கப்பட்டது.",
        "Sarkaria Commission suggested the name 'Inter-Governmental Council'.",
        "சர்க்காரியா ஆணையம் 'அரசுகளுக்கிடையேயான மன்றம்' என்ற பெயரைப் பரிந்துரைத்தது.",
        tags=["Sarkaria Commission", "Inter-Governmental Council"]
    ))

    # 030 - Ans B
    q.append(make_q(
        "ISR_M_030", "Evolution of Councils",
        "Which of the following ad hoc consultative councils was established by the President under Article 263 prior to the creation of the permanent Inter-State Council in 1990?",
        "1990-ல் நிரந்தர மாநிலங்களுக்கு இடையிலான மன்றம் உருவாக்கப்படுவதற்கு முன்பே, குடியரசுத் தலைவரால் உறுப்பு 263-ன் கீழ் அமைக்கப்பட்ட தற்காலிக ஆலோசனைக் குழுக்களில் எது ஒன்றாகும்?",
        "National Water Resources Council", "தேசிய நீர் வளக் குழு",
        "Central Council of Health and Family Welfare", "மத்திய சுகாதாரம் மற்றும் குடும்ப நலக் குழு",
        "Goods and Services Tax Council", "சரக்கு மற்றும் சேவை வரிக் குழு",
        "Monetary Policy Committee", "பணவியல் கொள்கைக் குழு",
        "B",
        "Before the comprehensive Inter-State Council was formed in 1990, the President had invoked Article 263 to set up specialized sectoral councils, most notably the Central Council of Health (established in 1952, later renamed Central Council of Health and Family Welfare) and Central Council of Local Self-Government (1954).",
        "1990-ல் விரிவான மாநிலங்களுக்கு இடையிலான மன்றம் உருவாக்கப்படுவதற்கு முன்பே, குடியரசுத் தலைவர் உறுப்பு 263-ஐப் பயன்படுத்தி குறிப்பிட்ட துறைசார் மன்றங்களை அமைத்தார்; குறிப்பாக மத்திய சுகாதாரக் குழு (1952-ல் அமைக்கப்பட்டது, பின்னர் மத்திய சுகாதாரம் மற்றும் குடும்ப நலக் குழு எனப் பெயர் மாற்றப்பட்டது) மற்றும் மத்திய உள்ளாட்சிக் குழு (1954) ஆகியவை அடங்கும்.",
        "National Water Resources Council was established by an executive resolution in 1983, not under Article 263.", "தேசிய நீர் வளக் குழு 1983-ல் நிர்வாகத் தீர்மானத்தால் அமைக்கப்பட்டது, உறுப்பு 263-ன் கீழ் அல்ல.",
        "Central Council of Health (1952) was set up by Presidential Order under Article 263.", "மத்திய சுகாதாரக் குழு (1952) உறுப்பு 263-ன் கீழ் குடியரசுத் தலைவர் ஆணை மூலம் அமைக்கப்பட்டது.",
        "GST Council is a constitutional body under Article 279A, not Article 263.", "ஜிஎஸ்டி கவுன்சில் உறுப்பு 279A-ன் கீழான அமைப்பு, 263 அல்ல.",
        "Monetary Policy Committee is statutory under the RBI Act 1934.", "பணவியல் கொள்கைக் குழு ரிசர்வ் வங்கி சட்டத்தின் கீழான அமைப்பாகும்.",
        "Article 263 was used in 1952 to set up the Central Council of Health and in 1954 to set up the Central Council of Local Self-Government.",
        "உறுப்பு 263 ஆனது 1952-ல் மத்திய சுகாதாரக் குழுவையும், 1954-ல் மத்திய உள்ளாட்சிக் குழுவையும் அமைக்கப் பயன்படுத்தப்பட்டது.",
        "Central Council of Health was established under Article 263 in 1952.",
        "மத்திய சுகாதாரக் குழு 1952 இல் உறுப்பு 263 இன் கீழ் அமைக்கப்பட்டது.",
        tags=["Article 263", "Central Council of Health"]
    ))

    # 031 - Ans C
    q.append(make_q(
        "ISR_M_031", "Zonal Councils Composition",
        "Why were the Andaman and Nicobar Islands and Lakshadweep excluded from the regular membership of the five Zonal Councils created under the States Reorganisation Act, 1956?",
        "1956 ஆம் ஆண்டின் மாநில மறுசீரமைப்புச் சட்டத்தின் கீழ் உருவாக்கப்பட்ட ஐந்து மண்டலக் குழுக்களின் வழக்கமான உறுப்பினர் சேர்க்கையிலிருந்து அந்தமான் & நிக்கோபார் தீவுகளும் லட்சத்தீவுகளும் ஏன் விலக்கப்பட்டன?",
        "They were declared foreign territories until the 12th Amendment.", "அவை 12-வது திருத்தம் வரை வெளிநாட்டுப் பகுதிகளாக அறிவிக்கப்பட்டிருந்தன.",
        "They possessed independent High Courts with sovereign dispute mechanisms.", "அவை இறையாண்மை கொண்ட தகராறு முறைமைகளுடன் கூடிய சுயாதீன உயர் நீதிமன்றங்களைக் கொண்டிருந்தன.",
        "Being geographically isolated island territories with unique administrative needs, they were not attached to any mainland zone, though they may be invited as special invitees.", "புவியியல் ரீதியாக தனிமைப்படுத்தப்பட்ட தீவுப் பகுதிகளாகவும், தனித்துவமான நிர்வாகத் தேவைகளைக் கொண்டதாகவும் இருந்ததால், அவை எந்த நிலப்பரப்பு மண்டலத்துடனும் இணைக்கப்படவில்லை; எனினும் அவை சிறப்பு அழைப்பாளர்களாக அழைக்கப்படலாம்.",
        "They were governed directly by the Chief of Defence Staff.", "அவை நேரடியாக பாதுகாப்புப் படைகளின் தலைமைத் தளபதியால் நிர்வகிக்கப்பட்டன.",
        "C",
        "Under the States Reorganisation Act 1956, Andaman & Nicobar Islands and Lakshadweep were not included in any of the five zones due to their geographical detachment from the mainland. However, administrators or representatives are often invited to attend meetings of relevant zones as special invitees.",
        "1956 மாநில மறுசீரமைப்புச் சட்டத்தின் கீழ், அந்தமான் & நிக்கோபார் தீவுகள் மற்றும் லட்சத்தீவு ஆகியவை நிலப்பரப்பில் இருந்து புவியியல் ரீதியாகப் பிரிந்திருப்பதன் காரணமாக ஐந்து மண்டலங்களில் எதிலும் சேர்க்கப்படவில்லை. எனினும், அவற்றின் நிர்வாகிகள் சிறப்பு அழைப்பாளர்களாகக் கலந்துகொள்ள அழைக்கப்படுகின்றனர்.",
        "They were Part D territories or UTs, not foreign territories.", "அவை இந்திய யூனியன் பிரதேசங்கள், வெளிநாட்டுப் பகுதிகள் அல்ல.",
        "They do not have independent High Courts (A&N is under Calcutta HC; Lakshadweep is under Kerala HC).", "அவற்றுக்குத் தனி உயர் நீதிமன்றங்கள் இல்லை (அந்தமான் கொல்கத்தா HC கீழ்; லட்சத்தீவு கேரளா HC கீழ் உள்ளது).",
        "Option C accurately explains their geographical isolation and exclusion from standard mainland zones.", "விருப்பம் C அவற்றின் புவியியல் தனிமை மற்றும் விலக்குதலைச் சரியாக விளக்குகிறது.",
        "Chief of Defence Staff post was created in 2019, completely irrelevant to 1956.", "CDS பதவி 2019-ல் உருவாக்கப்பட்டது, 1956-க்கு தொடர்பற்றது.",
        "Neither Andaman & Nicobar nor Lakshadweep is a regular member of any Zonal Council.",
        "அந்தமான் & நிக்கோபார் அல்லது லட்சத்தீவு எந்த மண்டலக் குழுவிலும் வழக்கமான உறுப்பினர்கள் அல்ல.",
        "Island UTs were excluded from regular Zonal Councils due to geographical isolation.",
        "தீவு யூனியன் பிரதேசங்கள் புவியியல் தனிமை காரணமாக வழக்கமான மண்டலக் குழுக்களிலிருந்து விலக்கப்பட்டன.",
        tags=["Zonal Councils", "Island UTs", "Exclusion"]
    ))

    # 032 - Ans D
    q.append(make_q(
        "ISR_M_032", "Zonal Councils Composition",
        "Following the bifurcation of Andhra Pradesh in 2014, which of the following represents the complete and correct list of full members in the Southern Zonal Council?",
        "2014-ல் ஆந்திரப் பிரதேசம் பிரிக்கப்பட்டதைத் தொடர்ந்து, தென் மண்டலக் குழுவில் உள்ள முழு உறுப்பினர்களின் முழுமையான மற்றும் சரியான பட்டியல் எது?",
        "Tamil Nadu, Kerala, Karnataka, Andhra Pradesh, and Goa", "தமிழ்நாடு, கேரளா, கர்நாடகா, ஆந்திரப் பிரதேசம் மற்றும் கோவா",
        "Tamil Nadu, Kerala, Karnataka, Andhra Pradesh, and Odisha", "தமிழ்நாடு, கேரளா, கர்நாடகா, ஆந்திரப் பிரதேசம் மற்றும் ஒடிசா",
        "Tamil Nadu, Karnataka, Andhra Pradesh, Telangana, and Maharashtra", "தமிழ்நாடு, கர்நாடகா, ஆந்திரப் பிரதேசம், தெலுங்கானா மற்றும் மகாராஷ்டிரா",
        "Andhra Pradesh, Karnataka, Kerala, Tamil Nadu, Telangana, and the Union Territory of Puducherry", "ஆந்திரப் பிரதேசம், கர்நாடகா, கேரளா, தமிழ்நாடு, தெலுங்கானா மற்றும் புதுச்சேரி யூனியன் பிரதேசம்",
        "D",
        "The Southern Zonal Council comprises five States—Andhra Pradesh, Karnataka, Kerala, Tamil Nadu, and Telangana (added post-2014 bifurcation)—and the Union Territory of Puducherry. Its permanent headquarters is in Chennai.",
        "தென் மண்டலக் குழுவில் ஐந்து மாநிலங்கள்—ஆந்திரப் பிரதேசம், கர்நாடகா, கேரளா, தமிழ்நாடு மற்றும் தெலுங்கானா (2014 பிரிவினைக்குப் பிறகு சேர்க்கப்பட்டது)—மற்றும் புதுச்சேரி யூனியன் பிரதேசம் ஆகியவை அடங்கும். இதன் நிரந்தரத் தலைமையகம் சென்னையில் உள்ளது.",
        "Goa is in the Western Zonal Council, not Southern.", "கோவா மேற்கு மண்டலக் குழுவில் உள்ளது, தெற்கில் அல்ல.",
        "Odisha is in the Eastern Zonal Council, not Southern.", "ஒடிசா கிழக்கு மண்டலக் குழுவில் உள்ளது, தெற்கில் அல்ல.",
        "Maharashtra is in the Western Zonal Council, not Southern.", "மகாராஷ்டிரா மேற்கு மண்டலக் குழுவில் உள்ளது, தெற்கில் அல்ல.",
        "Option D provides the complete and accurate current membership of the Southern Zonal Council.", "விருப்பம் D தென் மண்டலக் குழுவின் தற்போதைய முழுமையான மற்றும் துல்லியமான உறுப்பினர் பட்டியலை வழங்குகிறது.",
        "Southern Zonal Council: AP, Karnataka, Kerala, TN, Telangana, and UT of Puducherry (HQ: Chennai).",
        "தென் மண்டலக் குழு: ஆந்திரா, கர்நாடகா, கேரளா, தமிழ்நாடு, தெலுங்கானா, புதுச்சேரி (தலைமையகம்: சென்னை).",
        "Southern Zonal Council has 5 States and 1 UT.",
        "தென் மண்டலக் குழுவில் 5 மாநிலங்கள் மற்றும் 1 யூனியன் பிரதேசம் உள்ளன.",
        tags=["Southern Zonal Council", "Bifurcation 2014", "Telangana"]
    ))

    # 033 - Ans A
    q.append(make_q(
        "ISR_M_033", "Zonal Councils Composition",
        "Which of the following groups of States constitutes the complete membership of the Central Zonal Council?",
        "பின்வரும் மாநிலக் குழுக்களில் எது மத்திய மண்டலக் குழுவின் முழுமையான உறுப்பினர் சேர்க்கையை உருவாக்குகிறது?",
        "Chhattisgarh, Madhya Pradesh, Uttarakhand, and Uttar Pradesh", "சத்தீஸ்கர், மத்தியப் பிரதேசம், உத்தராகண்ட் மற்றும் உத்தரப் பிரதேசம்",
        "Rajasthan, Madhya Pradesh, Uttar Pradesh, and Bihar", "ராஜஸ்தான், மத்தியப் பிரதேசம், உத்தரப் பிரதேசம் மற்றும் பீகார்",
        "Uttar Pradesh, Bihar, Jharkhand, and Madhya Pradesh", "உத்தரப் பிரதேசம், பீகார், ஜார்க்கண்ட் மற்றும் மத்தியப் பிரதேசம்",
        "Madhya Pradesh, Maharashtra, Chhattisgarh, and Gujarat", "மத்தியப் பிரதேசம், மகாராஷ்டிரா, சத்தீஸ்கர் மற்றும் குஜராத்",
        "A",
        "The Central Zonal Council comprises four States: Chhattisgarh, Madhya Pradesh, Uttarakhand, and Uttar Pradesh. Its headquarters is located at Prayagraj (Allahabad).",
        "மத்திய மண்டலக் குழுவில் நான்கு மாநிலங்கள் உள்ளன: சத்தீஸ்கர், மத்தியப் பிரதேசம், உத்தராகண்ட் மற்றும் உத்தரப் பிரதேசம். இதன் தலைமையகம் பிரயாக்ராஜில் (அலகாபாத்) அமைந்துள்ளது.",
        "Option A accurately lists all four States of the Central Zone.", "விருப்பம் A மத்திய மண்டலத்தின் நான்கு மாநிலங்களையும் துல்லியமாகப் பட்டியலிடுகிறது.",
        "Rajasthan is in the Northern Zone; Bihar is in the Eastern Zone.", "ராஜஸ்தான் வடக்கிலும், பீகார் கிழக்கிலும் உள்ளன.",
        "Bihar and Jharkhand are in the Eastern Zone.", "பீகாரும் ஜார்க்கண்டும் கிழக்கு மண்டலத்தில் உள்ளன.",
        "Maharashtra and Gujarat are in the Western Zone.", "மகாராஷ்டிராவும் குஜராத்தும் மேற்கு மண்டலத்தில் உள்ளன.",
        "Central Zonal Council states: UP, MP, Uttarakhand, Chhattisgarh (HQ: Prayagraj).",
        "மத்திய மண்டலக் குழு மாநிலங்கள்: உ.பி, ம.பி, உத்தராகண்ட், சத்தீஸ்கர் (தலைமையகம்: பிரயாக்ராஜ்).",
        "Central Zonal Council = Chhattisgarh, MP, Uttarakhand, UP.",
        "மத்திய மண்டலக் குழு = சத்தீஸ்கர், ம.பி, உத்தராகண்ட், உ.பி.",
        tags=["Central Zonal Council", "Members"]
    ))

    # 034 - Ans B
    q.append(make_q(
        "ISR_M_034", "Zonal Councils Composition",
        "Which of the following represents the correct composition of the Western Zonal Council?",
        "பின்வருவனவற்றில் மேற்கு மண்டலக் குழுவின் சரியான அமைப்பைக் குறிப்பது எது?",
        "Rajasthan, Gujarat, Maharashtra, and Goa", "ராஜஸ்தான், குஜராத், மகாராஷ்டிரா மற்றும் கோவா",
        "Goa, Gujarat, Maharashtra, and the Union Territory of Dadra and Nagar Haveli and Daman and Diu", "கோவா, குஜராத், மகாராஷ்டிரா மற்றும் தாத்ரா & நகர் ஹவேலி மற்றும் தாமன் & டையூ யூனியன் பிரதேசம்",
        "Maharashtra, Karnataka, Goa, and Gujarat", "மகாராஷ்டிரா, கர்நாடகா, கோவா மற்றும் குஜராத்",
        "Gujarat, Madhya Pradesh, Maharashtra, and Goa", "குஜராத், மத்தியப் பிரதேசம், மகாராஷ்டிரா மற்றும் கோவா",
        "B",
        "The Western Zonal Council comprises the States of Goa, Gujarat, and Maharashtra, and the Union Territory of Dadra and Nagar Haveli and Daman and Diu. Its headquarters is located at Mumbai.",
        "மேற்கு மண்டலக் குழுவில் கோவா, குஜராத் மற்றும் மகாராஷ்டிரா ஆகிய மாநிலங்களும், தாத்ரா மற்றும் நகர் ஹவேலி மற்றும் தாமன் மற்றும் டையூ யூனியன் பிரதேசமும் அடங்கும். இதன் தலைமையகம் மும்பையில் அமைந்துள்ளது.",
        "Rajasthan is in the Northern Zonal Council, not Western.", "ராஜஸ்தான் வடக்கு மண்டலக் குழுவில் உள்ளது, மேற்கில் அல்ல.",
        "Option B correctly lists all members of the Western Zonal Council.", "விருப்பம் B மேற்கு மண்டலக் குழுவின் அனைத்து உறுப்பினர்களையும் சரியாகக் குறிப்பிடுகிறது.",
        "Karnataka is in the Southern Zonal Council, not Western.", "கர்நாடகா தென் மண்டலக் குழுவில் உள்ளது, மேற்கில் அல்ல.",
        "Madhya Pradesh is in the Central Zonal Council, not Western.", "மத்தியப் பிரதேசம் மத்திய மண்டலக் குழுவில் உள்ளது, மேற்கில் அல்ல.",
        "Western Zonal Council: Goa, Gujarat, Maharashtra, and UT of DNH & DD (HQ: Mumbai).",
        "மேற்கு மண்டலக் குழு: கோவா, குஜராத், மகாராஷ்டிரா, தாத்ரா & தாமன் (தலைமையகம்: மும்பை).",
        "Western Zonal Council = Goa, Gujarat, Maharashtra, DNH & DD.",
        "மேற்கு மண்டலக் குழு = கோவா, குஜராத், மகாராஷ்டிரா, தாத்ரா & தாமன்.",
        tags=["Western Zonal Council", "Members"]
    ))

    # 035 - Ans C
    q.append(make_q(
        "ISR_M_035", "Zonal Councils Composition",
        "Which of the following States is an official member of the Eastern Zonal Council?",
        "பின்வரும் மாநிலங்களில் எது கிழக்கு மண்டலக் குழுவின் அதிகாரப்பூர்வ உறுப்பினராக உள்ளது?",
        "Sikkim", "சிக்கிம்",
        "Assam", "அசாம்",
        "Jharkhand", "ஜார்க்கண்ட்",
        "Meghalaya", "மேகாலயா",
        "C",
        "The Eastern Zonal Council comprises the States of Bihar, Jharkhand, Odisha, and West Bengal (headquartered at Kolkata). Sikkim is NOT a member of the Eastern Zonal Council; it is an official member of the North Eastern Council.",
        "கிழக்கு மண்டலக் குழுவில் பீகார், ஜார்க்கண்ட், ஒடிசா மற்றும் மேற்கு வங்காளம் ஆகிய மாநிலங்கள் அடங்கும் (தலைமையகம் கொல்கத்தா). சிக்கிம் கிழக்கு மண்டலக் குழுவில் உறுப்பினர் அல்ல; அது வடகிழக்கு கவுன்சிலின் அதிகாரப்பூர்வ உறுப்பினர் ஆகும்.",
        "Sikkim is in the North Eastern Council (added in 2002), not the Eastern Zonal Council.", "சிக்கிம் வடகிழக்கு கவுன்சிலில் உள்ளது (2002-ல் சேர்க்கப்பட்டது), கிழக்கு மண்டலத்தில் அல்ல.",
        "Assam is in the North Eastern Council.", "அசாம் வடகிழக்கு கவுன்சிலில் உள்ளது.",
        "Jharkhand is an official member of the Eastern Zonal Council.", "ஜார்க்கண்ட் கிழக்கு மண்டலக் குழுவின் அதிகாரப்பூர்வ உறுப்பினர் ஆகும்.",
        "Meghalaya is in the North Eastern Council.", "மேகாலயா வடகிழக்கு கவுன்சிலில் உள்ளது.",
        "TNPSC Trap: Sikkim is part of the North Eastern Council (since 2002), NOT the Eastern Zonal Council!",
        "TNPSC பொறி: சிக்கிம் வடகிழக்கு கவுன்சிலின் ஒரு பகுதியாகும் (2002 முதல்), கிழக்கு மண்டலக் குழுவின் பகுதி அல்ல!",
        "Eastern Zonal Council includes Bihar, Jharkhand, Odisha, West Bengal.",
        "கிழக்கு மண்டலக் குழுவில் பீகார், ஜார்க்கண்ட், ஒடிசா, மேற்கு வங்கம் ஆகியவை உள்ளன.",
        tags=["Eastern Zonal Council", "Jharkhand", "Sikkim Trap"]
    ))

    # 036 - Ans D
    q.append(make_q(
        "ISR_M_036", "Zonal Councils Composition",
        "Following the Jammu and Kashmir Reorganisation Act, 2019, which of the following represents the updated status of Jammu & Kashmir and Ladakh in the Northern Zonal Council?",
        "2019 ஆம் ஆண்டின் ஜம்மு-காஷ்மீர் மறுசீரமைப்புச் சட்டத்தைத் தொடர்ந்து, வடக்கு மண்டலக் குழுவில் ஜம்மு-காஷ்மீர் மற்றும் லடாக்கின் புதுப்பிக்கப்பட்ட நிலையைக் குறிப்பது எது?",
        "They were removed from the Northern Zonal Council and placed under the North Eastern Council.", "அவை வடக்கு மண்டலக் குழுவிலிருந்து நீக்கப்பட்டு வடகிழக்கு கவுன்சிலின் கீழ் வைக்கப்பட்டன.",
        "Only Jammu and Kashmir remains a member; Ladakh was attached to the Central Zone.", "ஜம்மு-காஷ்மீர் மட்டுமே உறுப்பினராக உள்ளது; லடாக் மத்திய மண்டலத்துடன் இணைக்கப்பட்டது.",
        "Both were shifted to a newly created Himalayan Zonal Council.", "இரண்டும் புதிதாக உருவாக்கப்பட்ட இமயமலை மண்டலக் குழுவிற்கு மாற்றப்பட்டன.",
        "Both Union Territories (Jammu & Kashmir, and Ladakh) are full participating members of the Northern Zonal Council.", "இரு யூனியன் பிரதேசங்களும் (ஜம்மு & காஷ்மீர் மற்றும் லடாக்) வடக்கு மண்டலக் குழுவின் முழு பங்கேற்பு உறுப்பினர்களாக உள்ளன.",
        "D",
        "Following the 2019 reorganization, both the newly formed Union Territory of Jammu & Kashmir and the Union Territory of Ladakh continue to be members of the Northern Zonal Council along with Haryana, Himachal Pradesh, Punjab, Rajasthan, NCT of Delhi, and Chandigarh.",
        "2019 மறுசீரமைப்பைத் தொடர்ந்து, புதிதாக உருவாக்கப்பட்ட ஜம்மு & காஷ்மீர் யூனியன் பிரதேசம் மற்றும் லடாக் யூனியன் பிரதேசம் ஆகிய இரண்டுமே ஹரியானா, இமாச்சலப் பிரதேசம், பஞ்சாப், ராஜஸ்தான், தில்லி மற்றும் சண்டிகர் ஆகியவற்றுடன் வடக்கு மண்டலக் குழுவின் உறுப்பினர்களாகத் தொடர்கின்றன.",
        "They were not shifted to the North Eastern Council.", "அவை வடகிழக்கு கவுன்சிலுக்கு மாற்றப்படவில்லை.",
        "Ladakh is not attached to the Central Zone.", "லடாக் மத்திய மண்டலத்துடன் இணைக்கப்படவில்லை.",
        "No Himalayan Zonal Council was created.", "இமயமலை மண்டலக் குழு எதுவும் உருவாக்கப்படவில்லை.",
        "Option D correctly captures the continuation of both UTs in the Northern Zonal Council.", "விருப்பம் D இரு யூனியன் பிரதேசங்களும் வடக்கு மண்டலக் குழுவில் தொடர்வதைச் சரியாகக் குறிப்பிடுகிறது.",
        "Northern Zonal Council includes: Haryana, HP, Punjab, Rajasthan, Delhi, Chandigarh, J&K (UT), and Ladakh (UT).",
        "வடக்கு மண்டலக் குழு: ஹரியானா, இ.பி, பஞ்சாப், ராஜஸ்தான், தில்லி, சண்டிகர், ஜம்மு-காஷ்மீர் (UT), லடாக் (UT).",
        "Both J&K and Ladakh UTs are members of the Northern Zonal Council.",
        "ஜம்மு-காஷ்மீர் மற்றும் லடாக் யூனியன் பிரதேசங்கள் இரண்டும் வடக்கு மண்டலக் குழுவின் உறுப்பினர்கள் ஆவர்.",
        tags=["Northern Zonal Council", "J&K", "Ladakh"]
    ))

    # 037 - Ans A
    q.append(make_q(
        "ISR_M_037", "Statutory Qualifications",
        "Under Section 4 of the Inter-State River Water Disputes Act 1956, what are the mandatory qualifications for a person to be appointed as Chairman or Member of a Water Disputes Tribunal?",
        "1956 ஆம் ஆண்டின் நதிநீர் தகராறுகள் சட்டத்தின் பிரிவு 4-ன் கீழ், நதிநீர் தகராறுகள் தீர்ப்பாயத்தின் தலைவர் அல்லது உறுப்பினராக நியமிக்கப்படுவதற்கான கட்டாயத் தகுதிகள் யாவை?",
        "Must be a person who is a sitting Judge of the Supreme Court or of a High Court at the time of appointment", "நியமனத்தின் போது உச்ச நீதிமன்றம் அல்லது உயர் நீதிமன்றத்தின் பணியிலிருக்கும் நீதிபதியாக இருக்க வேண்டும்",
        "Must be a retired Chief Justice of India", "ஓய்வு பெற்ற இந்தியத் தலைமை நீதிபதியாக இருக்க வேண்டும்",
        "Must be an advocate of at least 20 years standing in an inter-State river case", "மாநிலங்களுக்கு இடையேயான நதி வழக்கில் குறைந்தது 20 ஆண்டுகள் அனுபவமுள்ள வழக்கறிஞராக இருக்க வேண்டும்",
        "Must be a retired Secretary to the Ministry of Water Resources", "நீர்வள அமைச்சகத்தின் ஓய்வு பெற்ற செயலாளராக இருக்க வேண்டும்",
        "A",
        "Section 4(2) of the IRWD Act 1956 mandates that the Tribunal shall consist of a Chairman and two other members nominated by the Chief Justice of India from among persons who at the time of such nomination are Judges of the Supreme Court or of a High Court.",
        "1956 IRWD சட்டத்தின் பிரிவு 4(2), தீர்ப்பாயத்தின் தலைவர் மற்றும் பிற இரு உறுப்பினர்கள் நியமனத்தின் போது உச்ச நீதிமன்றம் அல்லது உயர் நீதிமன்றத்தின் பணியிலிருக்கும் நீதிபதிகளாக உள்ள நபர்களிலிருந்து இந்தியத் தலைமை நீதிபதியால் பரிந்துரைக்கப்பட வேண்டும் எனக் கட்டாயப்படுத்துகிறது.",
        "Option A accurately states the statutory requirement of being a sitting SC or HC judge at appointment.", "விருப்பம் A நியமனத்தின் போது உச்ச அல்லது உயர் நீதிமன்றப் பணியிலிருக்கும் நீதிபதியாக இருக்க வேண்டும் என்ற சட்டத் தகுதியைச் சரியாகக் கூறுகிறது.",
        "Retired CJI is not the requirement; sitting judges are nominated.", "ஓய்வு பெற்ற தலைமை நீதிபதி என்பது தேவையில்லை; பணியிலிருக்கும் நீதிபதிகள் நியமிக்கப்படுகின்றனர்.",
        "Advocates are not appointed as tribunal judges under Section 4.", "வழக்கறிஞர்கள் தீர்ப்பாய நீதிபதிகளாக நியமிக்கப்படுவதில்லை.",
        "Civil servants cannot be members of the judicial tribunal.", "அரசு ஊழியர்கள் நீதித்துறை தீர்ப்பாயத்தில் உறுப்பினர்களாக முடியாது.",
        "Statutory qualification: Must be a SITTING judge of the Supreme Court or a High Court when nominated by the CJI.",
        "சட்டப்பூர்வத் தகுதி: தலைமை நீதிபதியால் பரிந்துரைக்கப்படும் போது உச்ச அல்லது உயர் நீதிமன்றப் பணியிலிருக்கும் நீதிபதியாக இருக்க வேண்டும்.",
        "Tribunal members must be sitting judges of Supreme Court or High Courts.",
        "தீர்ப்பாய உறுப்பினர்கள் உச்ச அல்லது உயர் நீதிமன்றத்தின் பணியிலிருக்கும் நீதிபதிகளாக இருக்க வேண்டும்.",
        tags=["IRWD Act 1956", "Qualifications", "Sitting Judges"]
    ))

    # 038 - Ans B
    q.append(make_q(
        "ISR_M_038", "Scheme Implementation",
        "Under Section 6A of the Inter-State River Water Disputes Act 1956, what is the legal power of the Central Government regarding the implementation of a water disputes tribunal award?",
        "1956 ஆம் ஆண்டின் நதிநீர் தகராறுகள் சட்டத்தின் பிரிவு 6A-ன் கீழ், நதிநீர் தகராறுகள் தீர்ப்பாயத் தீர்ப்பை செயல்படுத்துவது தொடர்பாக மத்திய அரசிற்கு உள்ள சட்டப்பூர்வ அதிகாரம் என்ன?",
        "It can modify the award with the concurrence of the Planning Commission.", "திட்டக் குழுவின் ஒப்புதலுடன் தீர்ப்பை மாற்றியமைக்கலாம்.",
        "It may frame a scheme or establish an authority (such as CWMA) for giving effect to the decision of the tribunal.", "தீர்ப்பாயத்தின் முடிவைச் செயல்படுத்துவதற்காக ஒரு திட்டத்தை (scheme) உருவாக்கலாம் அல்லது ஓர் அதிகார அமைப்பை (CWMA போன்ற) நிறுவலாம்.",
        "It can suspend the award indefinitely if requested by any one basin State.", "ஏதேனும் ஒரு படுகை மாநிலம் கோரினால் தீர்ப்பை காலவரையின்றி நிறுத்தி வைக்கலாம்.",
        "It can refer the award to the International Court of Arbitration for validation.", "செல்லுபடியாகும் தன்மையை உறுதிப்படுத்த தீர்ப்பை சர்வதேச நடுவர் மன்றத்திற்கு அனுப்பலாம்.",
        "B",
        "Section 6A of the IRWD Act 1956 empowers the Central Government to frame a scheme or schemes for giving effect to the decision of a Tribunal, including the constitution of an authority (such as the Cauvery Water Management Authority framed in June 2018).",
        "1956 IRWD சட்டத்தின் பிரிவு 6A, தீர்ப்பாயத்தின் முடிவைச் செயல்படுத்துவதற்காக ஓர் அதிகார அமைப்பை (2018 ஜூன் மாதம் அமைக்கப்பட்ட காவிரி நீர் மேலாண்மை ஆணையம் போன்றவை) நிறுவுவது உட்பட ஒரு திட்டம் அல்லது திட்டங்களை உருவாக்க மத்திய அரசிற்கு அதிகாரம் அளிக்கிறது.",
        "The Central Government cannot alter or modify the judicial award on its own.", "மத்திய அரசு தானாகவே நீதித்துறைத் தீர்ப்பை மாற்ற முடியாது.",
        "Option B correctly identifies the power to frame implementation schemes (such as the 2018 Cauvery Management Scheme).", "விருப்பம் B அமலாக்கத் திட்டங்களை உருவாக்கும் அதிகாரத்தைச் சரியாகக் குறிப்பிடுகிறது.",
        "A single State cannot compel indefinite suspension of a gazetted award.", "ஒரு தனி மாநிலம் அரசிதழில் வெளியிடப்பட்ட தீர்ப்பை நிறுத்தி வைக்க முடியாது.",
        "International Court of Arbitration has no domestic jurisdiction.", "சர்வதேச நடுவர் மன்றத்திற்கு உள்நாட்டு அதிகார வரம்பு இல்லை.",
        "Section 6A was the statutory basis under which the Cauvery Water Management Scheme 2018 and CWMA were established.",
        "பிரிவு 6A என்பது காவிரி நீர் மேலாண்மைத் திட்டம் 2018 மற்றும் CWMA அமைக்கப்பட்ட சட்டப்பூர்வ அடிப்படையாகும்.",
        "Section 6A empowers the Centre to frame an implementation scheme.",
        "பிரிவு 6A அமலாக்கத் திட்டத்தை உருவாக்க மத்திய அரசுக்கு அதிகாரமளிக்கிறது.",
        tags=["Section 6A", "CWMA", "Implementation Scheme"]
    ))

    # 039 - Ans C
    q.append(make_q(
        "ISR_M_039", "Constitutional Terminology",
        "In the phrase 'trade, commerce, and intercourse' in Article 301, what specific meaning has been assigned to the word 'intercourse' by judicial interpretation?",
        "உறுப்பு 301-ல் உள்ள 'வர்த்தகம், வாணிபம் மற்றும் தொடர்பு' என்ற சொற்றொடரில், 'தொடர்பு' (intercourse) என்ற சொல்லுக்கு நீதித்துறை விளக்கம் மூலம் என்ன குறிப்பிட்ட பொருள் வழங்கப்பட்டுள்ளது?",
        "Only electronic and telecommunication exchanges between governments", "அரசாங்கங்களுக்கிடையேயான மின்னணு மற்றும் தொலைத்தொடர்பு பரிமாற்றங்கள் மட்டுமே",
        "Spiritual and religious journeys to holy places across States", "மாநிலங்கள் முழுவதும் புனித தலங்களுக்கான ஆன்மீக மற்றும் மதப் பயணங்கள்",
        "Non-commercial movement of persons, movement of private vehicles, and non-trade communications across state borders", "மாநில எல்லைகளைக் கடந்த நபர்களின் வர்த்தகம் சாராத இயக்கம், தனியார் வாகனங்களின் இயக்கம் மற்றும் வணிகம் அல்லாத தொடர்புகள்",
        "Diplomatic correspondence between State Governors and the Union Home Minister", "மாநில ஆளுநர்களுக்கும் மத்திய உள்துறை அமைச்சருக்கும் இடையிலான தூதரகத் தொடர்புகள்",
        "C",
        "While 'trade' and 'commerce' refer to buying, selling, and transportation of merchandise for profit, the term 'intercourse' has a wider scope: it encompasses non-commercial movement of persons from one State to another, movement of private vehicles, and transmission of information and social communication across borders without a profit motive.",
        "'வர்த்தகம்' மற்றும் 'வாணிபம்' ஆகியவை லாபத்திற்காகப் பொருட்களை வாங்குதல், விற்றல் மற்றும் கொண்டு செல்வதைக் குறிக்கும் அதே வேளையில், 'தொடர்பு' (intercourse) என்ற சொல் பரந்த நோக்கத்தைக் கொண்டுள்ளது: இது ஒரு மாநிலத்திலிருந்து மற்றொரு மாநிலத்திற்கு நபர்களின் வணிகம் சாராத இயக்கம், தனியார் வாகனங்களின் இயக்கம் மற்றும் லாப நோக்கமின்றி எல்லைகளைக் கடந்து தகவல் மற்றும் சமூகப் பரிமாற்றங்களை உள்ளடக்கியது.",
        "Intercourse is not restricted to telecommunications.", "தொடர்பு என்பது தொலைத்தொடர்புக்கு மட்டுமே மட்டுப்படுத்தப்பட்டது அல்ல.",
        "It is not limited to religious pilgrimages.", "இது மத வழிபாடுகளுக்கு மட்டுமே மட்டுப்படுத்தப்பட்டது அல்ல.",
        "Option C accurately describes the non-commercial movement of persons and communications covered by 'intercourse'.", "விருப்பம் C 'தொடர்பு' என்ற சொல்லால் உள்ளடக்கப்பட்ட நபர்களின் வணிகம் சாராத இயக்கத்தைச் சரியாக விவரிக்கிறது.",
        "It does not refer to diplomatic correspondence of Governors.", "இது ஆளுநர்களின் தூதரகத் தொடர்புகளைக் குறிக்கவில்லை.",
        "Trade/Commerce = commercial buying/selling/transport; Intercourse = non-commercial movement and communication of persons across state borders.",
        "வர்த்தகம்/வாணிபம் = வணிக ரீதியான வாங்குதல்/விற்றல்; தொடர்பு = எல்லை கடந்த நபர்களின் வணிகம் சாராத இயக்கம் மற்றும் தொடர்பு.",
        "'Intercourse' in Art 301 includes non-commercial movement of persons across states.",
        "உறுப்பு 301-ல் உள்ள 'தொடர்பு' என்பது நபர்களின் வணிகம் சாராத மாநில எல்லை கடந்த இயக்கத்தை உள்ளடக்கியது.",
        tags=["Article 301", "Intercourse", "Judicial Interpretation"]
    ))

    # 040 - Ans D
    q.append(make_q(
        "ISR_M_040", "Taxation Principles",
        "Under Article 304(a), what essential condition must be satisfied by a State Legislature when imposing a tax on goods imported from other States?",
        "உறுப்பு 304(a)-ன் கீழ், பிற மாநிலங்களிலிருந்து இறக்குமதி செய்யப்படும் பொருட்களின் மீது வரி விதிக்கும் போது ஒரு மாநில சட்டமன்றத்தால் என்ன அத்தியாவசிய நிபந்தனை பூர்த்தி செய்யப்பட வேண்டும்?",
        "The tax rate must be at least 5% higher than the local manufacturing tax to protect local artisans.", "உள்ளூர் கைவினைஞர்களைப் பாதுகாக்க வரி விகிதம் உள்ளூர் உற்பத்தி வரியை விட குறைந்தது 5% அதிகமாக இருக்க வேண்டும்.",
        "The revenue collected must be remitted directly to the Inter-State Council.", "வசூலிக்கப்படும் வருவாய் நேரடியாக மாநிலங்களுக்கு இடையிலான மன்றத்திற்கு அனுப்பப்பட வேண்டும்.",
        "The imported goods must have been manufactured in a Special Economic Zone.", "இறக்குமதி செய்யப்படும் பொருட்கள் ஒரு சிறப்புப் பொருளாதார மண்டலத்தில் உற்பத்தி செய்யப்பட்டிருக்க வேண்டும்.",
        "The tax must not discriminate between goods so imported and similar goods manufactured or produced within that State.", "இறக்குமதி செய்யப்படும் பொருட்களுக்கும் அந்த மாநிலத்திற்குள் உற்பத்தி செய்யப்படும் அல்லது தயாரிக்கப்படும் அதே போன்ற பொருட்களுக்கும் இடையே வரி பாகுபாடு காட்டக் கூடாது.",
        "D",
        "Article 304(a) allows a State Legislature to impose on goods imported from other States or UTs any tax to which similar goods manufactured or produced in that State are subject, SO, HOWEVER, AS NOT TO DISCRIMINATE between goods so imported and goods so manufactured or produced.",
        "உறுப்பு 304(a), ஒரு மாநிலத்திற்குள் உற்பத்தி செய்யப்படும் அதே போன்ற பொருட்களுக்கு விதிக்கப்படும் வரிக்கு இணையாக பிற மாநிலங்களிலிருந்து இறக்குமதி செய்யப்படும் பொருட்களுக்கும் வரி விதிக்க அனுமதிக்கிறது; எனினும், இறக்குமதி செய்யப்படும் பொருட்களுக்கும் உள்ளூரில் உற்பத்தி செய்யப்படும் பொருட்களுக்கும் இடையே பாகுபாடு காட்டக் கூடாது (not to discriminate) என்ற நிபந்தனைக்கு உட்பட்டது.",
        "A State cannot levy a higher protective tariff on imported goods; doing so violates Art 304(a).", "இறக்குமதி பொருட்களுக்கு அதிக பாதுகாப்பு வரி விதிக்க முடியாது; அவ்வாறு செய்வது 304(a)-ஐ மீறுவதாகும்.",
        "Tax revenues belong to the State, not the Inter-State Council.", "வரி வருவாய் மாநிலத்திற்கே உரியது.",
        "SEZ manufacture is irrelevant to general Article 304(a) provisions.", "SEZ உற்பத்தி என்பது பொதுவான உறுப்பு 304(a)-க்கு தொடர்பற்றது.",
        "Option D directly cites the non-discrimination requirement in Article 304(a).", "விருப்பம் D உறுப்பு 304(a)-ல் உள்ள பாகுபாடற்ற தேவையை நேரடியாகக் குறிப்பிடுகிறது.",
        "Fiscal Parity: Article 304(a) permits taxation of imported goods only if identical local goods bear the same tax burden without discrimination.",
        "நிதிச் சமநிலை: உள்ளூர் பொருட்கள் அதே வரிச் சுமையைச் சுமக்கும் போது மட்டுமே இறக்குமதி பொருட்கள் மீது பாகுபாடின்றி வரி விதிக்க உறுப்பு 304(a) அனுமதிக்கிறது.",
        "Article 304(a) mandates non-discrimination between imported and local goods.",
        "உறுப்பு 304(a) இறக்குமதி மற்றும் உள்ளூர் பொருட்களுக்கு இடையே பாகுபாடின்மையை கட்டாயமாக்குகிறது.",
        tags=["Article 304(a)", "Non-Discrimination", "Taxation"]
    ))

    # 041 - Ans A
    q.append(make_q(
        "ISR_M_041", "Zonal Councils Functions",
        "Under Section 21 of the States Reorganisation Act 1956, which of the following subjects is explicitly listed as a matter on which a Zonal Council may discuss and make recommendations?",
        "1956 ஆம் ஆண்டின் மாநில மறுசீரமைப்புச் சட்டத்தின் பிரிவு 21-ன் கீழ், ஒரு மண்டலக் குழு விவாதித்துப் பரிந்துரைகளை வழங்கக்கூடிய விவகாரமாகப் பின்வருவனவற்றில் எது வெளிப்படையாகப் பட்டியலிடப்பட்டுள்ளது?",
        "Any matter concerning border disputes, linguistic minorities, or inter-State transport", "எல்லைத் தகராறுகள், மொழிச் சிறுபான்மையினர் அல்லது மாநிலங்களுக்கு இடையிலான போக்குவரத்து தொடர்பான எந்தவொரு விஷயமும்",
        "Determination of income tax surcharge sharing ratios", "வருமான வரி கூடுதல் கட்டணப் பகிர்வு விகிதங்களைத் தீர்மானித்தல்",
        "Declaration of President's Rule in member States under Article 356", "உறுப்பு 356-ன் கீழ் உறுப்பினர் மாநிலங்களில் குடியரசுத் தலைவர் ஆட்சியைப் பிரகடனம் செய்தல்",
        "Negotiation of external commercial borrowings with foreign governments", "வெளிநாட்டு அரசாங்கங்களுடன் வெளிநாட்டு வணிகக் கடன்களைப் பேச்சுவார்த்தை நடத்துதல்",
        "A",
        "Section 21(2) of the States Reorganisation Act 1956 states that a Zonal Council may discuss and advise upon: (a) any matter of common interest in the field of economic and social planning; (b) any matter concerning border disputes, linguistic minorities, or inter-State transport; and (c) any matter connected with the reorganisation of the States under the Act.",
        "1956 மாநில மறுசீரமைப்புச் சட்டத்தின் பிரிவு 21(2), ஒரு மண்டலக் குழு பின்வருவனவற்றை விவாதித்து ஆலோசனை வழங்கலாம் எனக் கூறுகிறது: (a) பொருளாதார மற்றும் சமூகத் திட்டமிடல்; (b) எல்லைத் தகராறுகள், மொழிச் சிறுபான்மையினர் அல்லது மாநிலங்களுக்கு இடையிலான போக்குவரத்து; (c) மாநில மறுசீரமைப்புடன் தொடர்புடைய விஷயங்கள்.",
        "Option A precisely reflects the statutory subjects under Section 21(2)(b) of the Act.", "விருப்பம் A சட்டத்தின் பிரிவு 21(2)(b)-ன் கீழான சட்டப்பூர்வப் பாடங்களைத் துல்லியமாகப் பிரதிபலிக்கிறது.",
        "Tax sharing is the constitutional domain of the Finance Commission under Article 280.", "வரிப் பகிர்வு என்பது உறுப்பு 280-ன் கீழ் நிதி ஆணையத்தின் வரம்பாகும்.",
        "President's Rule is an executive power under Article 356, completely outside Zonal Council purview.", "குடியரசுத் தலைவர் ஆட்சி மண்டலக் குழுவின் வரம்பிற்கு அப்பாற்பட்டது.",
        "States cannot negotiate external borrowings (Entry 37, Union List).", "மாநிலங்கள் வெளிநாட்டுக் கடன்களைப் பேச்சுவார்த்தை நடத்த முடியாது.",
        "Zonal Council statutory mandate: Economic/social planning, border disputes, linguistic minorities, and inter-State transport.",
        "மண்டலக் குழுவின் சட்டப்பூர்வ பணி: திட்டமிடல், எல்லைத் தகராறுகள், மொழிச் சிறுபான்மையினர் மற்றும் மாநிலங்களுக்கு இடையிலான போக்குவரத்து.",
        "Zonal Councils discuss border disputes, linguistic minorities, and inter-State transport.",
        "மண்டலக் குழுக்கள் எல்லைத் தகராறுகள், மொழிச் சிறுபான்மையினர் மற்றும் போக்குவரத்தை விவாதிக்கின்றன.",
        tags=["Zonal Councils", "Section 21", "Functions"]
    ))

    # 042 - Ans B
    q.append(make_q(
        "ISR_M_042", "Constitutional Seventh Schedule",
        "How is legislative competence over water divided between the Union and the States under the Seventh Schedule of the Indian Constitution?",
        "இந்திய அரசியலமைப்பின் ஏழாவது அட்டவணையின் கீழ் நீர் மீதான சட்டமன்ற அதிகாரம் ஒன்றியத்திற்கும் மாநிலங்களுக்கும் இடையே எவ்வாறு பிரிக்கப்பட்டுள்ளது?",
        "Water is exclusively in the Concurrent List (Entry 20).", "நீர் பிரத்யேகமாகப் பொதுப் பட்டியலில் (பதிவு 20) உள்ளது.",
        "Water supplies, irrigation, canals, and drainage are in Entry 17 of the State List, but this is subject to Entry 56 of the Union List (regulation and development of inter-State rivers declared by Parliament by law).", "நீர் வழங்கல், பாசனம், கால்வாய்கள் மற்றும் வடிகால் ஆகியவை மாநிலப் பட்டியலின் பதிவு 17-ல் உள்ளன; ஆனால் இது மத்தியப் பட்டியலின் பதிவு 56-க்கு (நாடாளுமன்றச் சட்டத்தால் அறிவிக்கப்பட்ட மாநிலங்களுக்கு இடையேயான நதிகள் ஒழுங்குமுறை) உட்பட்டது.",
        "Water is in the Union List exclusively, and States have no legislative power over rivers.", "நீர் முற்றிலும் மத்தியப் பட்டியலில் உள்ளது, மேலும் நதிகள் மீது மாநிலங்களுக்குச் சட்டமன்ற அதிகாரம் இல்லை.",
        "Water is a residuary power falling exclusively under Article 248.", "நீர் என்பது உறுப்பு 248-ன் கீழ் முற்றிலும் நாடாளுமன்றத்தின் எஞ்சிய அதிகாரமாகும்.",
        "B",
        "Entry 17 of List II (State List) covers 'Water, that is to say, water supplies, irrigation and canals, drainage and embankments, water storage and water power, subject to the provisions of Entry 56 of List I'. Entry 56 of List I (Union List) empowers Parliament to regulate and develop inter-State rivers and river valleys to the extent declared by Parliament by law to be expedient in the public interest.",
        "மாநிலப் பட்டியலின் (பட்டியல் II) பதிவு 17 'நீர், அதாவது நீர் வழங்கல், பாசனம், கால்வாய்கள், வடிகால், நீர் சேமிப்பு மற்றும் நீர் சக்தி ஆகியவற்றைக் குறிக்கிறது; இது பட்டியல் I-ன் பதிவு 56-ன் விதிகளுக்கு உட்பட்டது'. மத்தியப் பட்டியலின் பதிவு 56 மாநிலங்களுக்கு இடையேயான நதிகளை ஒழுங்குபடுத்தவும் மேம்படுத்தவும் நாடாளுமன்றத்திற்கு அதிகாரம் அளிக்கிறது.",
        "Water is not an entry in the Concurrent List.", "நீர் பொதுப் பட்டியலில் உள்ள ஒரு பதிவு அல்ல.",
        "Option B correctly outlines the interplay between Entry 17 (State List) and Entry 56 (Union List).", "விருப்பம் B மாநிலப் பட்டியல் பதிவு 17 மற்றும் மத்தியப் பட்டியல் பதிவு 56 ஆகியவற்றுக்கு இடையிலான தொடர்பைச் சரியாக விளக்குகிறது.",
        "States have extensive powers over water under Entry 17.", "பதிவு 17-ன் கீழ் மாநிலங்களுக்கு நீர் மீது விரிவான அதிகாரங்கள் உள்ளன.",
        "Water is an enumerated subject, not a residuary power.", "நீர் பட்டியலிடப்பட்ட ஒரு பாடம், எஞ்சிய அதிகாரம் அல்ல.",
        "Constitutional formula: State List Entry 17 is SUBORDINATED to Union List Entry 56 for inter-State rivers.",
        "அரசியலமைப்புச் சூத்திரம்: மாநிலப் பட்டியல் பதிவு 17, மாநிலங்களுக்கு இடையேயான நதிகளுக்கு மத்தியப் பட்டியல் பதிவு 56-க்கு உட்பட்டதாகும்.",
        "State List Entry 17 (Water) is subject to Union List Entry 56 (Inter-State rivers).",
        "மாநிலப் பட்டியல் பதிவு 17 (நீர்) மத்தியப் பட்டியல் பதிவு 56-க்கு (மாநில நதிகள்) உட்பட்டது.",
        tags=["Seventh Schedule", "Entry 17", "Entry 56", "Water"]
    ))

    # 043 - Ans C
    q.append(make_q(
        "ISR_M_043", "Clause Analysis",
        "Under Article 261(2) of the Constitution, who is empowered to determine by law the manner in which public acts, records, and judicial proceedings shall be proved, and the effect thereof?",
        "அரசியலமைப்பு உறுப்பு 261(2)-ன் கீழ், பொதுச் சட்டங்கள், பதிவேடுகள் மற்றும் நீதித்துறை நடவடிக்கைகள் நிரூபிக்கப்பட வேண்டிய முறை மற்றும் அவற்றின் விளைவுகளைச் சட்டம் மூலம் தீர்மானிக்க அதிகாரம் பெற்றவர் யார்?",
        "The Supreme Court of India", "இந்திய உச்ச நீதிமன்றம்",
        "The State Legislatures concurrently", "மாநில சட்டமன்றங்கள் ஒரே நேரத்தில்",
        "The Parliament of India", "இந்திய நாடாளுமன்றம்",
        "The Law Commission of India", "இந்தியச் சட்ட ஆணையம்",
        "C",
        "Article 261(2) explicitly states: 'The manner in which and the conditions under which the acts, records and proceedings referred to in clause (1) shall be proved and the effect thereof shall be determined by law made by Parliament.' (e.g., provisions in the Indian Evidence Act and Code of Civil Procedure).",
        "உறுப்பு 261(2) வெளிப்படையாகக் கூறுகிறது: 'பிரிவு (1)-ல் குறிப்பிடப்பட்டுள்ள சட்டங்கள், பதிவேடுகள் மற்றும் நடவடிக்கைகள் நிரூபிக்கப்பட வேண்டிய முறை, நிபந்தனைகள் மற்றும் அவற்றின் விளைவு ஆகியவை நாடாளுமன்றத்தால் இயற்றப்படும் சட்டம் மூலம் தீர்மானிக்கப்படும்.'",
        "Supreme Court interprets laws, but Parliament enacts the procedural evidentiary statute under 261(2).", "உச்ச நீதிமன்றம் சட்டங்களை விளக்குகிறது, ஆனால் நாடாளுமன்றமே சட்டத்தை இயற்றுகிறது.",
        "State Legislatures do not have the power under Article 261(2); it is exclusive to Parliament.", "மாநில சட்டமன்றங்களுக்கு உறுப்பு 261(2)-ன் கீழ் அதிகாரம் இல்லை; அது நாடாளுமன்றத்திற்கு மட்டுமே உரியது.",
        "Parliament of India is explicitly designated in Article 261(2).", "இந்திய நாடாளுமன்றம் உறுப்பு 261(2)-ல் வெளிப்படையாகக் குறிப்பிடப்பட்டுள்ளது.",
        "Law Commission is an advisory body.", "சட்ட ஆணையம் ஓர் ஆலோசனை அமைப்பு.",
        "Article 261(2) empowers Parliament exclusively to lay down rules of evidence and proof for inter-state public acts and records.",
        "உறுப்பு 261(2) மாநிலங்களுக்கிடையேயான பொதுச் சட்டங்கள் மற்றும் பதிவேடுகளுக்கான சான்றளிக்கும் விதிகளை வகுக்க நாடாளுமன்றத்திற்கு மட்டுமே அதிகாரமளிக்கிறது.",
        "Parliament determines the manner of proof under Article 261(2).",
        "நாடாளுமன்றம் உறுப்பு 261(2)-ன் கீழ் நிரூபிக்கும் முறையைத் தீர்மானிக்கிறது.",
        tags=["Article 261(2)", "Parliament", "Rules of Evidence"]
    ))

    # 044 - Ans D
    q.append(make_q(
        "ISR_M_044", "Constitutional Scope",
        "Under Article 303(1), by virtue of entries relating to trade and commerce in which of the Seventh Schedule Legislative Lists are Parliament and State Legislatures prohibited from discriminating between States?",
        "உறுப்பு 303(1)-ன் கீழ், ஏழாவது அட்டவணையின் எந்தச் சட்டமன்றப் பட்டியல்களில் உள்ள வர்த்தகம் மற்றும் வணிகம் தொடர்பான பதிவுகளின் அடிப்படையில் மாநிலங்களுக்கிடையே பாகுபாடு காட்டுவது நாடாளுமன்றத்திற்கும் மாநில சட்டமன்றங்களுக்கும் தடை செய்யப்பட்டுள்ளது?",
        "Union List only", "மத்தியப் பட்டியல் மட்டுமே",
        "State List only", "மாநிலப் பட்டியல் மட்டுமே",
        "Concurrent List only", "பொதுப் பட்டியல் மட்டுமே",
        "Any of the Lists in the Seventh Schedule", "ஏழாவது அட்டவணையில் உள்ள பட்டியல்களில் ஏதேனும் ஒன்றில்",
        "D",
        "Article 303(1) states: '...neither Parliament nor the Legislature of a State shall have power to make any law giving... any preference... or making... any discrimination... by virtue of any entry relating to trade and commerce in ANY OF THE LISTS in the Seventh Schedule.'",
        "உறுப்பு 303(1) கூறுகிறது: '...ஏழாவது அட்டவணையில் உள்ள பட்டியல்களில் ஏதேனும் ஒன்றில் (ANY OF THE LISTS in the Seventh Schedule) வர்த்தகம் மற்றும் வணிகம் தொடர்பான எந்தவொரு பதிவின் மூலமாகவும் எந்தவொரு முன்னுரிமையையும் அளிக்கவோ அல்லது பாகுபாட்டை ஏற்படுத்தவோ நாடாளுமன்றத்திற்கோ அல்லது மாநில சட்டமன்றத்திற்கோ அதிகாரம் இருக்காது.'",
        "Not confined to Union List alone.", "மத்தியப் பட்டியலுக்கு மட்டுமே மட்டுப்படுத்தப்படவில்லை.",
        "Not confined to State List alone.", "மாநிலப் பட்டியலுக்கு மட்டுமே மட்டுப்படுத்தப்படவில்லை.",
        "Not confined to Concurrent List alone.", "பொதுப் பட்டியலுக்கு மட்டுமே மட்டுப்படுத்தப்படவில்லை.",
        "The prohibition applies across 'any of the Lists in the Seventh Schedule'.", "இத்தடை 'ஏழாவது அட்டவணையில் உள்ள எந்தவொரு பட்டியலிலும்' உள்ள பதிவுகளுக்குப் பொருந்தும்.",
        "Constitutional Text: Article 303(1) explicitly bars discriminatory laws under 'any of the Lists in the Seventh Schedule'.",
        "அரசியலமைப்பு உரை: உறுப்பு 303(1) 'ஏழாவது அட்டவணையில் உள்ள எந்தவொரு பட்டியலின்' கீழும் பாகுபாடான சட்டங்களைத் தடை செய்கிறது.",
        "Article 303(1) non-discrimination applies to entries across all three Lists.",
        "உறுப்பு 303(1) பாகுபாடின்மை மூன்று பட்டியல்களிலும் உள்ள பதிவுகளுக்குப் பொருந்தும்.",
        tags=["Article 303(1)", "Seventh Schedule", "All Lists"]
    ))

    # 045 - Ans A
    q.append(make_q(
        "ISR_M_045", "Inter-Institutional Comparison",
        "How does the constitutional status of the Inter-State Council differ from that of the National Development Council (NDC)?",
        "மாநிலங்களுக்கு இடையிலான மன்றத்தின் அரசியலமைப்பு நிலை, தேசிய வளர்ச்சிக் குழுவின் (NDC) நிலையிலிருந்து எவ்வாறு வேறுபடுகிறது?",
        "Inter-State Council is established under Article 263 of the Constitution, whereas the NDC was an extra-constitutional body set up by an executive resolution of the Union Cabinet.", "மாநிலங்களுக்கு இடையிலான மன்றம் அரசியலமைப்பின் உறுப்பு 263-ன் கீழ் நிறுவப்பட்டது, ஆனால் NDC என்பது மத்திய அமைச்சரவையின் நிர்வாகத் தீர்மானத்தால் அமைக்கப்பட்ட ஓர் அரசியலமைப்புக்கு அப்பாற்பட்ட அமைப்பாகும்.",
        "Inter-State Council is an executive committee, while the NDC was created by an Act of Parliament.", "மாநிலங்களுக்கு இடையிலான மன்றம் ஒரு நிர்வாகக் குழு, ஆனால் NDC நாடாளுமன்றச் சட்டத்தால் உருவாக்கப்பட்டது.",
        "Both are constitutional bodies under Part XI of the Constitution.", "இரண்டுமே அரசியலமைப்பின் பகுதி XI-ன் கீழான அரசியலமைப்பு அமைப்புகளாகும்.",
        "Both are statutory bodies created by the States Reorganisation Act 1956.", "இரண்டுமே 1956 மாநில மறுசீரமைப்புச் சட்டத்தால் உருவாக்கப்பட்ட சட்டப்பூர்வ அமைப்புகளாகும்.",
        "A",
        "The Inter-State Council is a constitutional body provided for under Article 263 and established by Presidential Order. The National Development Council (NDC), established in August 1952, was neither constitutional nor statutory; it was an extra-constitutional body created by an executive resolution of the Government of India.",
        "மாநிலங்களுக்கு இடையிலான மன்றம் உறுப்பு 263-ன் கீழ் வழங்கப்பட்டு குடியரசுத் தலைவர் ஆணை மூலம் அமைக்கப்பட்ட ஓர் அரசியலமைப்பு அமைப்பாகும். 1952 ஆகஸ்டில் அமைக்கப்பட்ட தேசிய வளர்ச்சிக் குழு (NDC), அரசியலமைப்பு அமைப்பும் அல்ல சட்டப்பூர்வ அமைப்பும் அல்ல; இது இந்திய அரசாங்கத்தின் நிர்வாகத் தீர்மானத்தால் உருவாக்கப்பட்ட அரசியலமைப்புக்கு அப்பாற்பட்ட ஓர் அமைப்பாகும்.",
        "Option A accurately distinguishes the constitutional basis of ISC from the extra-constitutional executive origin of NDC.", "விருப்பம் A ISC-ன் அரசியலமைப்பு அடிப்படையையும் NDC-ன் நிர்வாகத் தீர்மான தோற்றத்தையும் சரியாக வேறுபடுத்துகிறது.",
        "NDC was not created by an Act of Parliament.", "NDC நாடாளுமன்றச் சட்டத்தால் உருவாக்கப்படவில்லை.",
        "NDC is not in Part XI or anywhere in the constitutional text.", "NDC பகுதி XI-ல் அல்லது அரசியலமைப்பில் எங்குமில்லை.",
        "Neither body was created by the States Reorganisation Act (that Act created Zonal Councils).", "எந்த அமைப்பும் மாநில மறுசீரமைப்புச் சட்டத்தால் உருவாக்கப்படவில்லை.",
        "Institutional Status: Inter-State Council = Constitutional (Art 263); NDC / NITI Aayog = Non-constitutional executive resolution bodies.",
        "நிறுவன நிலை: மாநிலங்களுக்கு இடையிலான மன்றம் = அரசியலமைப்பு சார்ந்தது (உறுப்பு 263); NDC / நிதி ஆயோக் = நிர்வாகத் தீர்மான அமைப்புகள்.",
        "Inter-State Council is constitutional; NDC was an extra-constitutional body.",
        "மாநிலங்களுக்கு இடையிலான மன்றம் அரசியலமைப்பு அமைப்பு; NDC அரசியலமைப்புக்கு அப்பாற்பட்ட அமைப்பு.",
        tags=["Inter-State Council", "NDC", "Constitutional vs Extra-Constitutional"]
    ))

    # 046 - Ans B
    q.append(make_q(
        "ISR_M_046", "Judicial Review Scope",
        "In State of Karnataka v. State of Tamil Nadu (2018), how did the Supreme Court reconcile the statutory bar under Article 262 / Section 11 of the IRWD Act with its own appellate jurisdiction under Article 136?",
        "கர்நாடக மாநிலம் vs தமிழ்நாடு மாநிலம் (2018) வழக்கில், உறுப்பு 262 / IRWD சட்டத்தின் பிரிவு 11-ன் கீழான சட்டப்பூர்வத் தடையை, உறுப்பு 136-ன் கீழான தனது சொந்த மேல்முறையீட்டு அதிகார வரம்போடு உச்ச நீதிமன்றம் எவ்வாறு இணக்கமாக்கியது?",
        "The Supreme Court declared Section 11 of the IRWD Act unconstitutional and invalid.", "உச்ச நீதிமன்றம் IRWD சட்டத்தின் பிரிவு 11-ஐ அரசியலமைப்பிற்கு முரணானது மற்றும் செல்லாதது என்று அறிவித்தது.",
        "The Court held that the bar of jurisdiction applies to ordinary suits under Article 131, but cannot override the extraordinary constitutional power of the Supreme Court under Article 136 to grant special leave against tribunal decisions.", "அதிகார வரம்புத் தடையானது உறுப்பு 131-ன் கீழான சாதாரண வழக்குகளுக்கு மட்டுமே பொருந்தும் என்றும், தீர்ப்பாய முடிவுகளுக்கு எதிராக சிறப்பு விடுப்பு வழங்கும் உறுப்பு 136-ன் கீழான உச்ச நீதிமன்றத்தின் அசாதாரண அரசியலமைப்பு அதிகாரத்தை அது விஞ்ச முடியாது என்றும் நீதிமன்றம் கூறியது.",
        "The Court held that Article 136 can be invoked only if all basin States submit a joint written application.", "அனைத்து நதிப் படுகை மாநிலங்களும் கூட்டாக எழுத்துப்பூர்வ விண்ணப்பத்தைச் சமர்ப்பித்தால் மட்டுமே உறுப்பு 136-ஐப் பயன்படுத்த முடியும் என்று நீதிமன்றம் கூறியது.",
        "The Court held that water tribunals are subordinate to High Courts, which must hear appeals before the Supreme Court.", "நதிநீர் தீர்ப்பாயங்கள் உயர் நீதிமன்றங்களுக்குக் கீழானவை என்றும், உச்ச நீதிமன்றத்திற்கு முன் உயர் நீதிமன்றங்கள் மேல்முறையீடுகளை விசாரிக்க வேண்டும் என்றும் நீதிமன்றம் கூறியது.",
        "B",
        "A three-judge bench of the Supreme Court in State of Karnataka v. State of Tamil Nadu (2018) affirmed that while Section 11 of the IRWD Act bars suits under Article 131 and before civil courts, an inter-State water tribunal is a 'tribunal' within the meaning of Article 136. The constitutional power under Article 136 is part of the basic structure and cannot be ousted by statutory enactment.",
        "கர்நாடக மாநிலம் vs தமிழ்நாடு மாநிலம் (2018) வழக்கில், IRWD சட்டத்தின் பிரிவு 11 உறுப்பு 131-ன் கீழான வழக்குகளைத் தடுத்தாலும், ஒரு நதிநீர் தீர்ப்பாயம் என்பது உறுப்பு 136-ன் பொருள் வரையறைக்குள் வரும் ஒரு 'தீர்ப்பாயம்' என்று உச்ச நீதிமன்றத்தின் மூன்று நீதிபதிகள் அமர்வு உறுதிப்படுத்தியது. உறுப்பு 136-ன் கீழான அதிகாரம் அடிப்படை அமைப்பின் ஒரு பகுதியாகும் மற்றும் அதைச் சட்டத்தால் பறிக்க முடியாது.",
        "Section 11 was not declared unconstitutional; its scope was reconciled with Art 136.", "பிரிவு 11 அரசியலமைப்பிற்கு முரணானது என அறிவிக்கப்படவில்லை; அதன் நோக்கம் உறுப்பு 136-டன் இணக்கப்பட்டது.",
        "Option B correctly captures the landmark constitutional reconciliation between Article 262 and Article 136.", "விருப்பம் B உறுப்பு 262 மற்றும் உறுப்பு 136 ஆகியவற்றுக்கு இடையேயான வரலாற்றுச் சிறப்புமிக்க இணக்கத்தைத் துல்லியமாகக் காட்டுகிறது.",
        "Joint application is not required under Article 136.", "கூட்டு விண்ணப்பம் உறுப்பு 136-ன் கீழ் தேவையில்லை.",
        "High Courts have no appellate jurisdiction over water dispute tribunals.", "நதிநீர் தீர்ப்பாயங்கள் மீது உயர் நீதிமன்றங்களுக்கு மேல்முறையீட்டு அதிகாரம் இல்லை.",
        "Supreme Court in 2018: Art 262 bars Art 131 original suits, but Article 136 Special Leave Petition remains maintainable against tribunal awards.",
        "2018-ல் உச்ச நீதிமன்றம்: உறுப்பு 262 உறுப்பு 131 மூல வழக்குகளைத் தடுக்கிறது, ஆனால் உறுப்பு 136 சிறப்பு விடுப்பு மனு தீர்ப்பாய முடிவுகளுக்கு எதிராக செல்லும்.",
        "Article 136 jurisdiction remains available against water dispute tribunal awards.",
        "நதிநீர் தீர்ப்பாய முடிவுகளுக்கு எதிராக உறுப்பு 136 அதிகார வரம்பு தொடர்ந்து கிடைக்கும்.",
        tags=["Article 136", "Article 262", "Karnataka v. TN 2018"]
    ))

    # 047 - Ans C
    q.append(make_q(
        "ISR_M_047", "Statutory Process",
        "Under Section 4(1) of the Inter-State River Water Disputes Act 1956, what condition must the Central Government satisfy before constituting a Water Disputes Tribunal?",
        "1956 ஆம் ஆண்டின் நதிநீர் தகராறுகள் சட்டத்தின் பிரிவு 4(1)-ன் கீழ், ஒரு நதிநீர் தகராறுகள் தீர்ப்பாயத்தை அமைப்பதற்கு முன் மத்திய அரசு என்ன நிபந்தனையை நிறைவு செய்ய வேண்டும்?",
        "It must secure an affirmative resolution from both Houses of Parliament by special majority.", "நாடாளுமன்றத்தின் இரு அவைகளிலும் சிறப்புப் பெரும்பான்மையுடன் நேர்மறையான தீர்மானத்தைப் பெற வேண்டும்.",
        "It must obtain prior written approval from the Inter-State Council.", "மாநிலங்களுக்கு இடையிலான மன்றத்திடமிருந்து முன் எழுத்துப்பூர்வ ஒப்புதலைப் பெற வேண்டும்.",
        "It must be of the opinion that the water dispute cannot be settled by negotiations between the concerned States.", "சம்பந்தப்பட்ட மாநிலங்களுக்கிடையேயான பேச்சுவார்த்தைகள் மூலம் நதிநீர் தகராறைத் தீர்க்க முடியாது என்ற கருத்தை அது கொண்டிருக்க வேண்டும்.",
        "It must conduct a referendum among the residents of the affected river basin.", "பாதிக்கப்பட்ட நதிப் படுகையின் மக்களிடையே ஒரு பொது வாக்கெடுப்பை நடத்த வேண்டும்.",
        "C",
        "Section 4(1) of the IRWD Act 1956 provides that when a request is received from a State Government, if the Central Government is of the opinion that the water dispute CANNOT BE SETTLED BY NEGOTIATIONS, the Central Government shall by notification constitute a Water Disputes Tribunal.",
        "1956 IRWD சட்டத்தின் பிரிவு 4(1), ஒரு மாநில அரசிடமிருந்து கோரிக்கை பெறப்படும் போது, சம்பந்தப்பட்ட மாநிலங்களுக்கிடையேயான பேச்சுவார்த்தைகள் மூலம் நதிநீர் தகராறைத் தீர்க்க முடியாது என்று மத்திய அரசு கருதினால், மத்திய அரசு அறிவிக்கை மூலம் ஒரு நதிநீர் தீர்ப்பாயத்தை அமைக்க வேண்டும் என்று கூறுகிறது.",
        "Parliamentary special majority is not required.", "நாடாளுமன்றச் சிறப்புப் பெரும்பான்மை தேவையில்லை.",
        "Approval of Inter-State Council is not required under the Act.", "மாநிலங்களுக்கு இடையிலான மன்றத்தின் ஒப்புதல் சட்டத்தின் கீழ் தேவையில்லை.",
        "Option C states the exact statutory condition precedent: failure of negotiated settlement.", "விருப்பம் C சரியான சட்டப்பூர்வ நிபந்தனையைக் குறிப்பிடுகிறது: பேச்சுவார்த்தை மூலம் தீர்க்க இயலாமை.",
        "Referendums are unknown to the Indian statutory water dispute process.", "இந்திய நதிநீர் தகராறு நடைமுறையில் பொது வாக்கெடுப்பு கிடையாது.",
        "Condition precedent for constituting an IRWD tribunal: Central Government's opinion that the dispute cannot be settled through negotiations.",
        "IRWD தீர்ப்பாயம் அமைப்பதற்கான முன் நிபந்தனை: பேச்சுவார்த்தைகள் மூலம் தகராறைத் தீர்க்க முடியாது என்ற மத்திய அரசின் கருத்து.",
        "Tribunal is constituted when dispute cannot be settled by negotiations.",
        "பேச்சுவார்த்தைகள் மூலம் தகராறைத் தீர்க்க முடியாத போது தீர்ப்பாயம் அமைக்கப்படுகிறது.",
        tags=["Section 4", "Negotiations", "IRWD Act 1956"]
    ))

    # 048 - Ans D
    q.append(make_q(
        "ISR_M_048", "Composition Analysis",
        "Who among the following may be nominated by the Prime Minister as Permanent Invitees to the Inter-State Council?",
        "மாநிலங்களுக்கு இடையிலான மன்றத்திற்குப் பிரதம அமைச்சரால் 'நிரந்தர அழைப்பாளர்களாக' (Permanent Invitees) பின்வருவனவற்றில் யார் நியமிக்கப்படலாம்?",
        "Leaders of Opposition in both Houses of Parliament", "நாடாளுமன்றத்தின் இரு அவைகளின் எதிர்க்கட்சித் தலைவர்கள்",
        "The Chief Election Commissioner and CAG", "தலைமைத் தேர்தல் ஆணையர் மற்றும் சி.ஏ.ஜி",
        "Former Chief Justices of India", "முன்னாள் இந்தியத் தலைமை நீதிபதிகள்",
        "Five Union Cabinet Ministers or Ministers of State (Independent Charge)", "ஐந்து மத்திய அமைச்சரவை அமைச்சர்கள் அல்லது இணை அமைச்சர்கள் (தனிப் பொறுப்பு)",
        "D",
        "Under the 1990 Presidential Order governing the Inter-State Council, the Prime Minister may nominate five Ministers of the Union (Cabinet Ministers or Ministers of State with Independent Charge) as Permanent Invitees to the Council.",
        "மாநிலங்களுக்கு இடையிலான மன்றத்தை நிர்வகிக்கும் 1990 குடியரசுத் தலைவர் ஆணையின் கீழ், பிரதம அமைச்சர் ஒன்றியத்தின் ஐந்து அமைச்சர்களை (அமைச்சரவை அமைச்சர்கள் அல்லது தனிப் பொறுப்புள்ள இணை அமைச்சர்கள்) மன்றத்தின் நிரந்தர அழைப்பாளர்களாக நியமிக்கலாம்.",
        "Leaders of Opposition are not designated permanent invitees to the ISC.", "எதிர்க்கட்சித் தலைவர்கள் ISC-ன் நிரந்தர அழைப்பாளர்கள் அல்ல.",
        "CEC and CAG are independent constitutional authorities, not invitees to the Council.", "CEC மற்றும் CAG தன்னாட்சி அமைப்புகள், மன்றத்தின் அழைப்பாளர்கள் அல்ல.",
        "Former CJIs have no role in the Inter-State Council.", "முன்னாள் தலைமை நீதிபதிகளுக்கு இம்மன்றத்தில் எந்தப் பங்கும் இல்லை.",
        "Option D correctly specifies the 5 Union Ministers nominated as permanent invitees by the PM.", "விருப்பம் D பிரதமரால் நிரந்தர அழைப்பாளர்களாக நியமிக்கப்படும் 5 மத்திய அமைச்சர்களைச் சரியாகக் குறிப்பிடுகிறது.",
        "Inter-State Council Permanent Invitees: 5 Ministers of the Union nominated by the PM (in addition to the 6 Cabinet Minister members).",
        "ISC நிரந்தர அழைப்பாளர்கள்: பிரதமரால் நியமிக்கப்படும் 5 மத்திய அமைச்சர்கள் (6 அமைச்சரவை உறுப்பினர் அமைச்சர்களுடன் கூடுதலாக).",
        "5 Union Ministers can be nominated as permanent invitees to the ISC.",
        "5 மத்திய அமைச்சர்கள் ISC-க்கு நிரந்தர அழைப்பாளர்களாக நியமிக்கப்படலாம்.",
        tags=["Inter-State Council", "Permanent Invitees"]
    ))

    # 049 - Ans A
    q.append(make_q(
        "ISR_M_049", "Constitutional Tests",
        "For a State law imposing restrictions on trade under Article 304(b) to be constitutionally valid, which of the following cumulative tests must be satisfied?",
        "உறுப்பு 304(b)-ன் கீழ் வர்த்தகத்தின் மீது கட்டுப்பாடுகளை விதிக்கும் ஒரு மாநிலச் சட்டம் அரசியலமைப்பு ரீதியாகச் செல்லுபடியாக வேண்டுமெனில், பின்வரும் எந்தக் கூட்டுத் தேர்வுகள் (cumulative tests) பூர்த்தி செய்யப்பட வேண்டும்?",
        "The restriction must be reasonable, in the public interest, and the bill must have received the previous sanction of the President", "கட்டுப்பாடு நியாயமானதாகவும், பொது நலன் சார்ந்ததாகவும் இருக்க வேண்டும், மேலும் மசோதா குடியரசுத் தலைவரின் முன் அனுமதியைப் பெற்றிருக்க வேண்டும்",
        "The restriction must be approved by a 3/4th majority of the State Legislative Assembly", "கட்டுப்பாட்டிற்கு மாநில சட்டமன்றத்தின் 3/4 பங்கு பெரும்பான்மை ஒப்புதல் அளிக்கப்பட வேண்டும்",
        "The restriction must apply only to goods imported from foreign nations", "கட்டுப்பாடு வெளிநாடுகளிலிருந்து இறக்குமதி செய்யப்படும் பொருட்களுக்கு மட்டுமே பொருந்த வேண்டும்",
        "The restriction must be ratified by at least half of the other State Legislatures", "கட்டுப்பாட்டிற்கு மற்ற மாநில சட்டமன்றங்களில் குறைந்தது பாதியளவு ஒப்புதல் அளிக்க வேண்டும்",
        "A",
        "To pass constitutional muster under Article 304(b), three cumulative requirements must be met: (1) The restriction must be 'reasonable'; (2) It must be required in the 'public interest'; and (3) The bill must be introduced with the 'previous sanction of the President' (or saved subsequently under Article 255).",
        "உறுப்பு 304(b)-ன் கீழ் ஒரு மாநிலச் சட்டம் செல்லுபடியாக மூன்று கூட்டுத் தேவைகள் பூர்த்தி செய்யப்பட வேண்டும்: (1) கட்டுப்பாடு 'நியாயமானதாக' (reasonable) இருக்க வேண்டும்; (2) அது 'பொது நலன்' (public interest) கருதி தேவைப்பட வேண்டும்; (3) மசோதா 'குடியரசுத் தலைவரின் முன் அனுமதியுடன்' (previous sanction) அறிமுகப்படுத்தப்பட வேண்டும் (அல்லது உறுப்பு 255-ன் கீழ் சரிசெய்யப்பட வேண்டும்).",
        "Option A precisely outlines the three constitutional tests of Article 304(b).", "விருப்பம் A உறுப்பு 304(b)-ன் மூன்று அரசியலமைப்புத் தேர்வுகளைத் துல்லியமாக விளக்குகிறது.",
        "A 3/4th majority is not required; ordinary simple majority applies.", "3/4 பங்கு பெரும்பான்மை தேவையில்லை; சாதாரண பெரும்பான்மையே போதுமானது.",
        "Article 304(b) applies to inter-State and intra-State domestic trade, not foreign trade.", "உறுப்பு 304(b) உள்நாட்டு வர்த்தகத்திற்குப் பொருந்தும், வெளிநாட்டு வர்த்தகத்திற்கு அல்ல.",
        "Ratification by other State Legislatures is not required.", "பிற மாநில சட்டமன்றங்களின் ஏற்பு தேவையில்லை.",
        "Article 304(b) Triple Test: Reasonable restriction + Public interest + Prior presidential sanction.",
        "உறுப்பு 304(b) முப்பெரும் சோதனை: நியாயமான கட்டுப்பாடு + பொது நலன் + குடியரசுத் தலைவரின் முன் அனுமதி.",
        "Article 304(b) requires reasonable restriction, public interest, and prior presidential sanction.",
        "உறுப்பு 304(b) நியாயமான கட்டுப்பாடு, பொது நலன் மற்றும் முன் அனுமதியைக் கோருகிறது.",
        tags=["Article 304(b)", "Triple Test", "Reasonable Restrictions"]
    ))

    # 050 - Ans B
    q.append(make_q(
        "ISR_M_050", "Statutory Evolution",
        "Through which amendment act was the North Eastern Council Act, 1971 amended to include Sikkim and restructure the role of the Council?",
        "சிக்கிமை இணைக்கவும் கவுன்சிலின் பங்கை மறுசீரமைக்கவும் 1971 ஆம் ஆண்டின் வடகிழக்கு கவுன்சில் சட்டம் எந்தத் திருத்தச் சட்டத்தின் மூலம் திருத்தப்பட்டது?",
        "North Eastern Council (Amendment) Act, 1990", "வடகிழக்கு கவுன்சில் (திருத்தச்) சட்டம், 1990",
        "North Eastern Council (Amendment) Act, 2002", "வடகிழக்கு கவுன்சில் (திருத்தச்) சட்டம், 2002",
        "States Reorganisation (Amendment) Act, 2002", "மாநில மறுசீரமைப்பு (திருத்தச்) சட்டம், 2002",
        "North-Eastern Areas (Amendment) Act, 2014", "வடகிழக்குப் பகுதிகள் (திருத்தச்) சட்டம், 2014",
        "B",
        "The North Eastern Council Act, 1971 was formally amended by the North Eastern Council (Amendment) Act, 2002 (Act No. 68 of 2002). This landmark amendment added Sikkim as the eighth member of the Council and repositioned the NEC as a regional planning body for the northeastern region.",
        "1971 ஆம் ஆண்டின் வடகிழக்கு கவுன்சில் சட்டம், 2002 ஆம் ஆண்டின் வடகிழக்கு கவுன்சில் (திருத்தச்) சட்டம் (2002-ன் சட்டம் எண் 68) மூலம் முறைப்படி திருத்தப்பட்டது. இந்த வரலாற்றுத் திருத்தம் சிக்கிமை எட்டாவது உறுப்பினராகச் சேர்த்ததுடன், வடகிழக்குப் பகுதிக்கான பிராந்திய திட்டமிடல் அமைப்பாக NEC-ஐ மறுசீரமைத்தது.",
        "1990 is incorrect.", "1990 தவறானது.",
        "2002 North Eastern Council (Amendment) Act is the exact statute that added Sikkim.", "2002 வடகிழக்கு கவுன்சில் (திருத்தச்) சட்டம் என்பது சிக்கிமைச் சேர்த்த சரியான சட்டமாகும்.",
        "It was not amended under the States Reorganisation Act.", "இது மாநில மறுசீரமைப்புச் சட்டத்தின் கீழ் திருத்தப்படவில்லை.",
        "2014 is incorrect.", "2014 தவறானது.",
        "Sikkim was added to NEC by the North Eastern Council (Amendment) Act, 2002.",
        "2002 ஆம் ஆண்டின் வடகிழக்கு கவுன்சில் (திருத்தச்) சட்டம் மூலம் சிக்கிம் NEC-ல் சேர்க்கப்பட்டது.",
        "North Eastern Council Act was amended in 2002 to add Sikkim.",
        "சிக்கிமைச் சேர்க்க வடகிழக்கு கவுன்சில் சட்டம் 2002 இல் திருத்தப்பட்டது.",
        tags=["NEC Act", "2002 Amendment", "Sikkim"]
    ))

    return q

if __name__ == "__main__":
    med_qs = get_medium_questions()
    print(f"Total Medium Questions generated: {len(med_qs)}")
    
    from collections import Counter
    cnt = Counter(q["correct_answer"] for q in med_qs)
    print("Medium Answer Key Distribution:", dict(cnt))
    
    out_dir = Path(r"c:\Users\Home\Desktop\tnpsc_ai\data\questions\polity")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "inter_state_relations_medium.json"
    
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(med_qs, f, indent=2, ensure_ascii=False)
    print(f"Saved to {out_file}")
