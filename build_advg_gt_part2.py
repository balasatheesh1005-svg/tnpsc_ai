# -*- coding: utf-8 -*-
"""
Grand Test Part 2 for Advocate General of a State (50 Questions: ADVG_GT_051 to ADVG_GT_100).
- 10 Statement-based MCQs (ADVG_GT_051 to ADVG_GT_060)
- 15 Assertion-Reason MCQs (ADVG_GT_061 to ADVG_GT_075)
- 15 Match the Following MCQs (ADVG_GT_076 to ADVG_GT_090)
- 10 Chronology MCQs (ADVG_GT_091 to ADVG_GT_100)
Strictly avoids collision with the 325 Core questions.
"""

from advg_mcq_helper import make_advg_q
import random

def get_gt_part2_questions():
    questions = []

    # -------------------------------------------------------------
    # 10 Statement-based MCQs (ADVG_GT_051 to ADVG_GT_060)
    # -------------------------------------------------------------

    # 51
    questions.append(make_advg_q(
        qid="ADVG_GT_051",
        diff="Medium",
        qtype="Statement Based",
        subtopic="Collective Responsibility",
        en_stem="Consider the following statements regarding the Council of Ministers and the Advocate General:\n1. The Council of Ministers is collectively responsible to the State Legislative Assembly under Article 164(2).\n2. The Advocate General is collectively responsible to the Legislative Assembly along with the Ministers.\n3. The Advocate General is an independent constitutional adviser, not a political member of the Ministry.\nWhich of the statements given above are correct?",
        ta_stem="அமைச்சரவை மற்றும் அட்வகேட் ஜெனரல் தொடர்பான பின்வரும் கூற்றுகளைக் கருதுக:\n1. சரத்து 164(2)-ன் கீழ் அமைச்சரவை மாநில சட்டமன்றப் பேரவைக்குக் கூட்டுப் பொறுப்புடையது.\n2. அமைச்சர்களுடன் சேர்ந்து அட்வகேட் ஜெனரலும் சட்டமன்றப் பேரவைக்குக் கூட்டுப் பொறுப்புடையவர் ஆவார்.\n3. அட்வகேட் ஜெனரல் ஒரு சுயாதீன அரசியலமைப்பு ஆலோசகர், அமைச்சரவையின் அரசியல் உறுப்பினர் அல்ல.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?",
        en_a="1 and 3 only", ta_a="1 மற்றும் 3 மட்டுமே",
        en_b="1 and 2 only", ta_b="1 மற்றும் 2 மட்டுமே",
        en_c="2 and 3 only", ta_c="2 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3", ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statements 1 and 3 are correct. Statement 2 is incorrect because collective ministerial responsibility under Article 164(2) applies strictly to the Council of Ministers, not the Advocate General.",
        exp_ta="கூற்றுகள் 1 மற்றும் 3 சரியானவை. கூற்று 2 தவறானது, ஏனெனில் சரத்து 164(2)-ன் கீழான கூட்டுப் பொறுப்பு அமைச்சர்களுக்கு மட்டுமே உரியது, அட்வகேட் ஜெனரலுக்கு அல்ல.",
        why_a_en="Option A is correct: Statements 1 and 3 are true; AG is not collectively responsible to the Assembly.",
        why_a_ta="தெரிவு A சரி: 1 மற்றும் 3 சரி; AG சட்டமன்றத்திற்கு கூட்டுப் பொறுப்புடையவர் அல்ல.",
        why_b_en="Option B is incorrect: Statement 2 is false.",
        why_b_ta="தெரிவு B தவறு: கூற்று 2 தவறு.",
        why_c_en="Option C is incorrect: Statement 2 is false.",
        why_c_ta="தெரிவு C தவறு: கூற்று 2 தவறு.",
        why_d_en="Option D is incorrect: Statement 2 is false.",
        why_d_ta="தெரிவு D தவறு: கூற்று 2 தவறு.",
        tip_en="Article 164(2) collective responsibility applies ONLY to Ministers, never to the Advocate General.",
        tip_ta="சரத்து 164(2) கூட்டுப் பொறுப்பு அமைச்சர்களுக்கு மட்டுமே பொருந்தும், அட்வகேட் ஜெனரலுக்கு அல்ல.",
        fact_en="The Advocate General is accountable directly to the Constitution and the Governor.",
        fact_ta="அட்வகேட் ஜெனரல் நேரடியாக அரசியலமைப்புக்கும் ஆளுநருக்கும் மட்டுமே பொறுப்புடையவர்.",
        tags=["polity", "advocate_general", "collective_responsibility"]
    ))

    # 52
    questions.append(make_advg_q(
        qid="ADVG_GT_052",
        diff="Hard",
        qtype="Statement Based",
        subtopic="Governor's Assent and AG Role",
        en_stem="Consider the following statements regarding the Advocate General's role in the legislative process under Article 200:\n1. The Governor can seek the formal legal opinion of the Advocate General when deciding whether to grant assent or reserve a bill for the President under Article 200.\n2. The Advocate General's advice is constitutionally binding on the Governor, compelling him to grant assent.\n3. The Advocate General can draft constitutional references for the Governor.\nWhich of the statements given above are correct?",
        ta_stem="சரத்து 200-ன் கீழான சட்டமியற்றும் நடைமுறையில் அட்வகேட் ஜெனரலின் பங்கு குறித்த பின்வரும் கூற்றுகளைக் கருதுக:\n1. சரத்து 200-ன் கீழ் ஒரு சட்டமுன்வடிவுக்கு ஒப்புதல் அளிப்பதா அல்லது குடியரசுத் தலைவருக்கு ஒதுக்குவதா என்பதை முடிவு செய்ய ஆளுநர் அட்வகேட் ஜெனரலின் சட்ட ஆலோசனையைக் கோரலாம்.\n2. அட்வகேட் ஜெனரலின் ஆலோசனை ஆளுநரைக் கட்டுப்படுத்தும், ஒப்புதல் அளிக்க கட்டாயப்படுத்தும்.\n3. ஆளுநருக்கான அரசியலமைப்பு குறிப்புரைகளை அட்வகேட் ஜெனரலால் வரைவு செய்ய முடியும்.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?",
        en_a="1 and 3 only", ta_a="1 மற்றும் 3 மட்டுமே",
        en_b="1 and 2 only", ta_b="1 மற்றும் 2 மட்டுமே",
        en_c="2 and 3 only", ta_c="2 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3", ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statements 1 and 3 are correct. Statement 2 is incorrect because the legal advice of the Advocate General is advisory in nature and not binding on the Governor.",
        exp_ta="கூற்றுகள் 1 மற்றும் 3 சரியானவை. கூற்று 2 தவறானது, ஏனெனில் அட்வகேட் ஜெனரலின் ஆலோசனை வழிகாட்டும் தன்மையுடையதே தவிர ஆளுநரைக் கட்டுப்படுத்தாது.",
        why_a_en="Option A is correct: Statements 1 and 3 are accurate; Statement 2 is false.",
        why_a_ta="தெரிவு A சரி: 1 மற்றும் 3 சரியானவை; கூற்று 2 தவறானது.",
        why_b_en="Option B is incorrect: Statement 2 is false.",
        why_b_ta="தெரிவு B தவறு: கூற்று 2 தவறு.",
        why_c_en="Option C is incorrect: Statement 2 is false.",
        why_c_ta="தெரிவு C தவறு: கூற்று 2 தவறு.",
        why_d_en="Option D is incorrect: Statement 2 is false.",
        why_d_ta="தெரிவு D தவறு: கூற்று 2 தவறு.",
        tip_en="Article 200 governs Governor's assent to bills; AG advises on legislative competence and central conflicts.",
        tip_ta="சரத்து 200 மசோதாக்களுக்கு ஆளுநரின் ஒப்புதலை நிர்வகிக்கிறது; சட்டமன்ற அதிகாரம் குறித்து AG ஆலோசிக்கிறார்.",
        fact_en="Governor's power to reserve bills for President's consideration is governed by Articles 200 and 201.",
        fact_ta="குடியரசுத் தலைவரின் பரிசீலனைக்கு மசோதாக்களை ஒதுக்கும் ஆளுநரின் அதிகாரம் சரத்துகள் 200 மற்றும் 201-ல் உள்ளது.",
        tags=["polity", "advocate_general", "article_200"]
    ))

    # 53
    questions.append(make_advg_q(
        qid="ADVG_GT_053",
        diff="Hard",
        qtype="Statement Based",
        subtopic="Pre-Audience Hierarchy",
        en_stem="Consider the following statements regarding the right of pre-audience:\n1. Section 23(2) of the Advocates Act, 1961 gives the Advocate General pre-audience over all advocates in the High Court of the State.\n2. The Advocate General's pre-audience applies in all subordinate civil and criminal courts within the State.\n3. In the Supreme Court, the Advocate General of a State has pre-audience over the Attorney General of India.\nWhich of the statements given above are correct?",
        ta_stem="முதன்மை வாதாடும் உரிமை (Pre-audience) குறித்த பின்வரும் கூற்றுகளைக் கருதுக:\n1. வழக்கறிஞர்கள் சட்டம் 1961 பிரிவு 23(2) மாநில உயர் நீதிமன்றத்தில் உள்ள அனைத்து வழக்கறிஞர்களை விடவும் அட்வகேட் ஜெனரலுக்கு முதன்மை வாதாடும் உரிமையை வழங்குகிறது.\n2. அட்வகேட் ஜெனரலின் முதன்மை வாதாடும் உரிமை மாநிலத்திற்குள் உள்ள அனைத்து சார்நிலை சிவில் மற்றும் குற்றவியல் நீதிமன்றங்களிலும் பொருந்தும்.\n3. உச்ச நீதிமன்றத்தில் இந்திய தலைமை வழக்கறிஞரை விடவும் மாநில அட்வகேட் ஜெனரலுக்கு முதன்மை வாதாடும் உரிமை உண்டு.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?",
        en_a="1 and 2 only", ta_a="1 மற்றும் 2 மட்டுமே",
        en_b="2 and 3 only", ta_b="2 மற்றும் 3 மட்டுமே",
        en_c="1 and 3 only", ta_c="1 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3", ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statements 1 and 2 are correct. Statement 3 is incorrect because the Attorney General of India has statutory rank 1 and pre-audience over ALL advocates throughout India, including all Advocates General.",
        exp_ta="கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் இந்திய தலைமை வழக்கறிஞரே உச்ச நீதிமன்றத்திலும் இந்தியா முழுவதிலும் முதலிடம் வகிக்கிறார்.",
        why_a_en="Option A is correct: Statements 1 and 2 are accurate; Statement 3 is false.",
        why_a_ta="தெரிவு A சரி: 1 மற்றும் 2 சரியானவை; கூற்று 3 தவறானது.",
        why_b_en="Option B is incorrect: Statement 3 is false.",
        why_b_ta="தெரிவு B தவறு: கூற்று 3 தவறு.",
        why_c_en="Option C is incorrect: Statement 3 is false.",
        why_c_ta="தெரிவு C தவறு: கூற்று 3 தவறு.",
        why_d_en="Option D is incorrect: Statement 3 is false.",
        why_d_ta="தெரிவு D தவறு: கூற்று 3 தவறு.",
        tip_en="Supreme Court rank 1 = Attorney General of India; State Courts rank 1 = Advocate General of that State.",
        tip_ta="உச்ச நீதிமன்றத்தில் முதலிடம் = இந்திய தலைமை வழக்கறிஞர்; மாநில நீதிமன்றங்களில் முதலிடம் = அந்த மாநில அட்வகேட் ஜெனரல்.",
        fact_en="Section 23 of the Advocates Act governs pre-audience nationwide.",
        fact_ta="வழக்கறிஞர்கள் சட்டம் பிரிவு 23 நாடு முழுவதும் முதன்மை வாதாடலை ஒழுங்குபடுத்துகிறது.",
        tags=["polity", "advocate_general", "advocates_act"]
    ))

    # 54
    questions.append(make_advg_q(
        qid="ADVG_GT_054",
        diff="Hard",
        qtype="Statement Based",
        subtopic="Contempt of Courts Act",
        en_stem="Consider the following statements regarding the Contempt of Courts Act, 1971:\n1. Section 15(1)(b) allows criminal contempt to be moved on the motion of the Advocate General.\n2. Under Section 15(3), in relation to a High Court, 'Advocate-General' means the Advocate-General of the State for which the High Court is established.\n3. The High Court cannot take suo motu cognizance of criminal contempt without the Advocate General's approval.\nWhich of the statements given above are correct?",
        ta_stem="நீதிமன்ற அவமதிப்புச் சட்டம் 1971 குறித்த பின்வரும் கூற்றுகளைக் கருதுக:\n1. பிரிவு 15(1)(b) அட்வகேட் ஜெனரலின் மனுவின் பேரில் குற்றவியல் அவமதிப்பு நடவடிக்கை எடுக்க அனுமதிக்கிறது.\n2. பிரிவு 15(3)-ன் கீழ், ஒரு உயர் நீதிமன்றத்தைப் பொறுத்தவரை 'அட்வகேட்-ஜெனரல்' என்பது அந்த உயர் நீதிமன்றம் நிறுவப்பட்டுள்ள மாநிலத்தின் அட்வகேட்-ஜெனரலைக் குறிக்கும்.\n3. அட்வகேட் ஜெனரலின் ஒப்புதல் இன்றி உயர் நீதிமன்றம் தானாக முன்வந்து (suo motu) குற்றவியல் அவமதிப்பு வழக்கை எடுக்க முடியாது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?",
        en_a="1 and 2 only", ta_a="1 மற்றும் 2 மட்டுமே",
        en_b="2 and 3 only", ta_b="2 மற்றும் 3 மட்டுமே",
        en_c="1 and 3 only", ta_c="1 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3", ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statements 1 and 2 are correct. Statement 3 is incorrect because under Section 15(1)(a) and Article 215, the High Court has inherent power to take suo motu cognizance of contempt without requiring the Advocate General's approval.",
        exp_ta="கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் பிரிவு 15(1)(a) மற்றும் சரத்து 215-ன் கீழ் உயர் நீதிமன்றம் AG அனுமதியின்றி தானாக முன்வந்து (suo motu) அவமதிப்பு நடவடிக்கை எடுக்க முழு அதிகாரம் கொண்டுள்ளது.",
        why_a_en="Option A is correct: Statements 1 and 2 are true; High Court's suo motu power is independent of AG.",
        why_a_ta="தெரிவு A சரி: 1 மற்றும் 2 சரி; உயர் நீதிமன்றத்தின் suo motu அதிகாரம் AG ஒப்புதலைச் சார்ந்திருக்கவில்லை.",
        why_b_en="Option B is incorrect: Statement 3 is false.",
        why_b_ta="தெரிவு B தவறு: கூற்று 3 தவறு.",
        why_c_en="Option C is incorrect: Statement 3 is false.",
        why_c_ta="தெரிவு C தவறு: கூற்று 3 தவறு.",
        why_d_en="Option D is incorrect: Statement 3 is false.",
        why_d_ta="தெரிவு D தவறு: கூற்று 3 தவறு.",
        tip_en="High Court Suo Motu contempt = NO consent needed. Private motion = AG consent MANDATORY.",
        tip_ta="உயர் நீதிமன்றம் தானாக எடுத்தால் = ஒப்புதல் தேவையில்லை. தனிநபர் மனு = AG ஒப்புதல் கட்டாயம்.",
        fact_en="Article 215 declares every High Court to be a court of record with inherent contempt powers.",
        fact_ta="சரத்து 215 ஒவ்வொரு உயர் நீதிமன்றத்தையும் பதிவேட்டு நீதிமன்றமாகவும் அவமதிப்புத் தண்டிக்கும் அதிகாரம் கொண்டதாகவும் அறிவிக்கிறது.",
        tags=["polity", "advocate_general", "contempt_of_court"]
    ))

    # 55
    questions.append(make_advg_q(
        qid="ADVG_GT_055",
        diff="Hard",
        qtype="Statement Based",
        subtopic="Advocates Act Section 16 & 23",
        en_stem="Consider the following statements regarding the Advocate General and Senior Advocates:\n1. Under Section 16 of the Advocates Act, 1961, there are two classes of advocates: Senior Advocates and other advocates.\n2. The Advocate General automatically enjoys pre-audience by virtue of office under Section 23, regardless of whether he was designated Senior Advocate before appointment.\n3. When the Advocate General steps down, he loses the designation of advocate and must apply afresh for Bar enrolment.\nWhich of the statements given above are correct?",
        ta_stem="அட்வகேட் ஜெனரல் மற்றும் மூத்த வழக்கறிஞர்கள் தொடர்பான பின்வரும் கூற்றுகளைக் கருதுக:\n1. வழக்கறிஞர்கள் சட்டம் 1961 பிரிவு 16-ன் கீழ் வழக்கறிஞர்கள் இரு வகைப்படுவர்: மூத்த வழக்கறிஞர்கள் மற்றும் பிற வழக்கறிஞர்கள்.\n2. நியமனத்திற்கு முன் மூத்த வழக்கறிஞராக அறிவிக்கப்பட்டிருந்தாலும் இல்லாவிட்டாலும், பிரிவு 23-ன் கீழ் அட்வகேட் ஜெனரல் தனது பதவியின் காரணமாக முதன்மை வாதாடும் உரிமையைப் பெறுகிறார்.\n3. அட்வகேட் ஜெனரல் பதவியிலிருந்து விலகும்போது, வழக்கறிஞர் அந்தஸ்தை இழக்கிறார், மீண்டும் புதிதாகப் பதிவு செய்ய வேண்டும்.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?",
        en_a="1 and 2 only", ta_a="1 மற்றும் 2 மட்டுமே",
        en_b="2 and 3 only", ta_b="2 மற்றும் 3 மட்டுமே",
        en_c="1 and 3 only", ta_c="1 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3", ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statements 1 and 2 are correct. Statement 3 is incorrect because his enrollment on the State Bar roll is continuous; he simply returns to private practice (typically designated as Senior Advocate).",
        exp_ta="கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் அவரது பார் கவுன்சில் பதிவு தொடர்கிறது; அவர் மீண்டும் தனியார் வழக்கறிஞராகத் தொடர்கிறார்.",
        why_a_en="Option A is correct: Statements 1 and 2 are true; Statement 3 is false.",
        why_a_ta="தெரிவு A சரி: 1 மற்றும் 2 சரியானவை; கூற்று 3 தவறானது.",
        why_b_en="Option B is incorrect: Statement 3 is false.",
        why_b_ta="தெரிவு B தவறு: கூற்று 3 தவறு.",
        why_c_en="Option C is incorrect: Statement 3 is false.",
        why_c_ta="தெரிவு C தவறு: கூற்று 3 தவறு.",
        why_d_en="Option D is incorrect: Statement 3 is false.",
        why_d_ta="தெரிவு D தவறு: கூற்று 3 தவறு.",
        tip_en="Pre-audience attaches to the CONSTITUTIONAL OFFICE under Section 23.",
        tip_ta="முதன்மை வாதாடும் உரிமை பிரிவு 23-ன் கீழ் அரசியலமைப்புப் பதவிக்கு இயல்பாகவே கிடைக்கிறது.",
        fact_en="Section 16 recognizes two tiers: Senior Advocates and other Advocates.",
        fact_ta="பிரிவு 16 வழக்கறிஞர்களை மூத்த வழக்கறிஞர்கள் மற்றும் பிற வழக்கறிஞர்கள் என இரு வகையாகப் பிரிக்கிறது.",
        tags=["polity", "advocate_general", "advocates_act"]
    ))

    # 56
    questions.append(make_advg_q(
        qid="ADVG_GT_056",
        diff="Hard",
        qtype="Statement Based",
        subtopic="Article 163 and Advice",
        en_stem="Consider the following statements regarding legal advice given to the Governor:\n1. Article 163(3) prohibits courts from inquiring into whether any, and if so what, advice was tendered by Ministers to the Governor.\n2. Legal opinions rendered by the Advocate General to the Council of Ministers form part of the advice-formulating process protected from forced disclosure.\n3. The High Court can issue a writ ordering the Advocate General to alter his legal opinion to match the Governor's personal preference.\nWhich of the statements given above are correct?",
        ta_stem="ஆளுநருக்கு வழங்கப்படும் சட்ட ஆலோசனைகள் குறித்த பின்வரும் கூற்றுகளைக் கருதுக:\n1. அமைச்சர்கள் ஆளுநருக்கு ஏதேனும் ஆலோசனை வழங்கினார்களா, என்ன ஆலோசனை வழங்கினார்கள் என்பதை எந்த நீதிமன்றமும் விசாரிக்க சரத்து 163(3) தடை விதிக்கிறது.\n2. அமைச்சரவைக்கு அட்வகேட் ஜெனரல் வழங்கும் சட்ட ஆலோசனைகள் கட்டாய வெளிப்படுத்தலில் இருந்து பாதுகாக்கப்பட்ட ஆலோசனை உருவாக்க நடைமுறையின் அங்கமாகும்.\n3. ஆளுநரின் தனிப்பட்ட விருப்பத்திற்கு ஏற்ப தனது சட்டக் கருத்தை மாற்றுமாறு அட்வகேட் ஜெனரலுக்கு உயர் நீதிமன்றம் பேராணை பிறப்பிக்க முடியும்.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?",
        en_a="1 and 2 only", ta_a="1 மற்றும் 2 மட்டுமே",
        en_b="2 and 3 only", ta_b="2 மற்றும் 3 மட்டுமே",
        en_c="1 and 3 only", ta_c="1 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3", ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statements 1 and 2 are correct. Statement 3 is incorrect because the courts cannot dictate or mandamus what legal advice a constitutional law officer should render.",
        exp_ta="கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் ஒரு அரசியலமைப்பு சட்ட அதிகாரி என்ன சட்ட ஆலோசனை வழங்க வேண்டும் என்று நீதிமன்றங்கள் உத்தரவிட முடியாது.",
        why_a_en="Option A is correct: Statements 1 and 2 are accurate; Statement 3 violates judicial separation of powers.",
        why_a_ta="தெரிவு A சரி: 1 மற்றும் 2 சரியானவை; கூற்று 3 அதிகாரப் பகிர்வை மீறுகிறது.",
        why_b_en="Option B is incorrect: Statement 3 is false.",
        why_b_ta="தெரிவு B தவறு: கூற்று 3 தவறு.",
        why_c_en="Option C is incorrect: Statement 3 is false.",
        why_c_ta="தெரிவு C தவறு: கூற்று 3 தவறு.",
        why_d_en="Option D is incorrect: Statement 3 is false.",
        why_d_ta="தெரிவு D தவறு: கூற்று 3 தவறு.",
        tip_en="Article 163(3) bars judicial scrutiny into ministerial advice tendered to the Governor.",
        tip_ta="சரத்து 163(3) ஆளுநருக்கு அமைச்சர்கள் அளித்த ஆலோசனையை நீதிமன்றங்கள் ஆராய்வதைத் தடுக்கிறது.",
        fact_en="An advocate's independent professional opinion cannot be commanded by a writ of Mandamus.",
        fact_ta="வழக்கறிஞரின் சுயாதீன தொழில்முறைக் கருத்தை கட்டளை நீதிப்பேராணை மூலம் மாற்ற முடியாது.",
        tags=["polity", "advocate_general", "article_163"]
    ))

    # 57
    questions.append(make_advg_q(
        qid="ADVG_GT_057",
        diff="Hard",
        qtype="Statement Based",
        subtopic="CPC Section 92 Public Charities",
        en_stem="Consider the following statements regarding suits under Section 92 of the Code of Civil Procedure, 1908:\n1. The Advocate General can institute a suit to remove any trustee of a public charitable trust.\n2. The Advocate General can institute a suit for settling a scheme for the administration of a public religious trust.\n3. Section 92 applies equally to purely private family trusts where the public has no beneficial interest.\nWhich of the statements given above are correct?",
        ta_stem="உரிமையியல் நடைமுறைச் சட்டம் 1908 பிரிவு 92-ன் கீழான வழக்குகள் குறித்த பின்வரும் கூற்றுகளைக் கருதுக:\n1. ஒரு பொது அறக்கட்டளையின் அறங்காவலரை நீக்குவதற்கு அட்வகேட் ஜெனரல் வழக்கு தொடரலாம்.\n2. ஒரு பொது சமய அறக்கட்டளையின் நிர்வாகத்திற்கான திட்டத்தை வகுக்க அட்வகேட் ஜெனரல் வழக்கு தொடரலாம்.\n3. பொதுமக்களுக்கு எந்தப் பயனும் இல்லாத முற்றிலும் தனிப்பட்ட குடும்ப அறக்கட்டளைகளுக்கும் பிரிவு 92 சமமாகப் பொருந்தும்.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?",
        en_a="1 and 2 only", ta_a="1 மற்றும் 2 மட்டுமே",
        en_b="2 and 3 only", ta_b="2 மற்றும் 3 மட்டுமே",
        en_c="1 and 3 only", ta_c="1 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3", ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statements 1 and 2 are correct. Statement 3 is incorrect because Section 92 applies strictly to PUBLIC trusts created for public charitable or religious purposes, not private family trusts.",
        exp_ta="கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் பிரிவு 92 பொது அறக்கட்டளைகளுக்கு மட்டுமே பொருந்தும், தனிப்பட்ட குடும்ப அறக்கட்டளைகளுக்குப் பொருந்தாது.",
        why_a_en="Option A is correct: Statements 1 and 2 accurately reflect CPC 92; private trusts are excluded.",
        why_a_ta="தெரிவு A சரி: 1 மற்றும் 2 சரியானவை; தனியார் குடும்ப அறக்கட்டளைகள் இதில் வராது.",
        why_b_en="Option B is incorrect: Statement 3 is false.",
        why_b_ta="தெரிவு B தவறு: கூற்று 3 தவறு.",
        why_c_en="Option C is incorrect: Statement 3 is false.",
        why_c_ta="தெரிவு C தவறு: கூற்று 3 தவறு.",
        why_d_en="Option D is incorrect: Statement 3 is false.",
        why_d_ta="தெரிவு D தவறு: கூற்று 3 தவறு.",
        tip_en="CPC Section 92: Applies strictly to PUBLIC charitable and religious trusts, NOT private trusts.",
        tip_ta="CPC பிரிவு 92: பொது அறக்கட்டளைகளுக்கு மட்டுமே பொருந்தும், தனியார் அறக்கட்டளைகளுக்கு அல்ல.",
        fact_en="Under Section 92, the court can remove trustees, direct accounts, and settle management schemes.",
        fact_ta="பிரிவு 92-ன் கீழ் நீதிமன்றம் அறங்காவலர்களை நீக்கலாம், கணக்குகளைக் கோரலாம், நிர்வாகத் திட்டங்களை வகுக்கலாம்.",
        tags=["polity", "advocate_general", "cpc"]
    ))

    # 58
    questions.append(make_advg_q(
        qid="ADVG_GT_058",
        diff="Hard",
        qtype="Statement Based",
        subtopic="Section 321 CrPC",
        en_stem="Consider the following statements regarding withdrawal from prosecution under Section 321 of CrPC:\n1. The Public Prosecutor in charge of a case can withdraw from prosecution with the consent of the court.\n2. The decision to withdraw must be based on the independent mind of the Public Prosecutor, though government policy can be considered.\n3. The Advocate General can unilaterally withdraw any prosecution without seeking the consent of the trying court.\nWhich of the statements given above are correct?",
        ta_stem="CrPC பிரிவு 321-ன் கீழ் வழக்கை திரும்பப் பெறுவது குறித்த பின்வரும் கூற்றுகளைக் கருதுக:\n1. நீதிமன்றத்தின் அனுமதியுடன் வழக்கை நடத்தும் அரசு வழக்கறிஞர் வழக்கைத் திரும்பப் பெறலாம்.\n2. அரசின் கொள்கையைக் கருத்தில் கொண்டாலும், வழக்கைத் திரும்பப் பெறும் முடிவு அரசு வழக்கறிஞரின் சுயாதீன சிந்தனையின் அடிப்படையில் இருக்க வேண்டும்.\n3. விசாரணை நீதிமன்றத்தின் அனுமதியைப் பெறாமலேயே அட்வகேட் ஜெனரல் எந்தவொரு வழக்கையும் தன்னிச்சையாகத் திரும்பப் பெற முடியும்.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?",
        en_a="1 and 2 only", ta_a="1 மற்றும் 2 மட்டுமே",
        en_b="2 and 3 only", ta_b="2 மற்றும் 3 மட்டுமே",
        en_c="1 and 3 only", ta_c="1 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3", ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statements 1 and 2 are correct. Statement 3 is incorrect because Section 321 mandatorily requires the 'consent of the court'. Neither the Advocate General nor the Government can bypass the court.",
        exp_ta="கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் பிரிவு 321-ன் கீழ் 'நீதிமன்றத்தின் ஒப்புதல்' கட்டாயம்; நீதிமன்றத்தைத் தவிர்த்து யாராலும் வழக்கைத் திரும்பப் பெற முடியாது.",
        why_a_en="Option A is correct: Statements 1 and 2 are accurate; Court consent is mandatory under Section 321.",
        why_a_ta="தெரிவு A சரி: 1 மற்றும் 2 சரியானவை; பிரிவு 321-ன் கீழ் நீதிமன்ற அனுமதி கட்டாயம்.",
        why_b_en="Option B is incorrect: Statement 3 is false.",
        why_b_ta="தெரிவு B தவறு: கூற்று 3 தவறு.",
        why_c_en="Option C is incorrect: Statement 3 is false.",
        why_c_ta="தெரிவு C தவறு: கூற்று 3 தவறு.",
        why_d_en="Option D is incorrect: Statement 3 is false.",
        why_d_ta="தெரிவு D தவறு: கூற்று 3 தவறு.",
        tip_en="Section 321 CrPC: Withdrawal requires the independent mind of the prosecutor AND consent of the court.",
        tip_ta="CrPC பிரிவு 321: வழக்கைத் திரும்பப் பெற வழக்கறிஞரின் சுயாதீன முடிவும் நீதிமன்றத்தின் அனுமதியும் அவசியம்.",
        fact_en="The Supreme Court affirmed in Sheonandan Paswan (1987) that the court acts in a judicial supervisory capacity under Sec 321.",
        fact_ta="ஷியோநந்தன் பஸ்வான் (1987) வழக்கில் நீதிமன்றம் பிரிவு 321-ன் கீழ் நீதித்துறை மேற்பார்வையாளராகச் செயல்படுகிறது எனத் தீர்ப்பளிக்கப்பட்டது.",
        tags=["polity", "advocate_general", "crpc"]
    ))

    # 59
    questions.append(make_advg_q(
        qid="ADVG_GT_059",
        diff="Hard",
        qtype="Statement Based",
        subtopic="State Law Officers Rules",
        en_stem="Consider the following statements regarding the service conditions of the Advocate General:\n1. The Advocate General is entitled to a monthly retainer fee determined by the Governor.\n2. The Advocate General is provided with secretarial staff and an official chamber in the High Court.\n3. The Advocate General is entitled to become a sitting High Court Judge automatically after three years of service.\nWhich of the statements given above are correct?",
        ta_stem="அட்வகேட் ஜெனரலின் பணி நிபந்தனைகள் குறித்த பின்வரும் கூற்றுகளைக் கருதுக:\n1. ஆளுநரால் நிர்ணயிக்கப்படும் மாதாந்திர தக்கவைப்புக் கட்டணத்தைப் பெற அட்வகேட் ஜெனரலுக்கு உரிமை உண்டு.\n2. அட்வகேட் ஜெனரலுக்கு உயர் நீதிமன்றத்தில் அதிகாரப்பூர்வ அலுவலக அறை மற்றும் செயலகப் பணியாளர்கள் வழங்கப்படுகிறார்கள்.\n3. மூன்று ஆண்டுகள் பணியாற்றிய பிறகு அவர் தானாகவே ஒரு உயர் நீதிமன்ற நீதிபதியாக ஆகிவிட முடியும்.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?",
        en_a="1 and 2 only", ta_a="1 மற்றும் 2 மட்டுமே",
        en_b="2 and 3 only", ta_b="2 மற்றும் 3 மட்டுமே",
        en_c="1 and 3 only", ta_c="1 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3", ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statements 1 and 2 are correct. Statement 3 is incorrect because there is no automatic absorption or elevation into the High Court Bench; HC Judge appointments follow the separate collegium procedure under Article 217.",
        exp_ta="கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் உயர் நீதிமன்ற நீதிபதியாக தானாக மாற முடியாது; சரத்து 217 கொலீஜியம் நடைமுறை மூலமே நீதிபதிகள் நியமிக்கப்படுகின்றனர்.",
        why_a_en="Option A is correct: Statements 1 and 2 are accurate; Statement 3 is completely false.",
        why_a_ta="தெரிவு A சரி: 1 மற்றும் 2 சரியானவை; கூற்று 3 முற்றிலும் தவறானது.",
        why_b_en="Option B is incorrect: Statement 3 is false.",
        why_b_ta="தெரிவு B தவறு: கூற்று 3 தவறு.",
        why_c_en="Option C is incorrect: Statement 3 is false.",
        why_c_ta="தெரிவு C தவறு: கூற்று 3 தவறு.",
        why_d_en="Option D is incorrect: Statement 3 is false.",
        why_d_ta="தெரிவு D தவறு: கூற்று 3 தவறு.",
        tip_en="Advocate General receives retainer and infrastructure, but has no right to become a judge automatically.",
        tip_ta="அட்வகேட் ஜெனரலுக்கு அலுவலக வசதிகள் உண்டு, ஆனால் தானாக நீதிபதியாகும் உரிமை கிடையாது.",
        fact_en="Many Advocates General decline elevation to the Bench preferring the active challenges of the Bar.",
        fact_ta="பல அட்வகேட் ஜெனரல்கள் வழக்கறிஞர் தொழிலின் சவால்களை விரும்பி நீதிபதி பதவியை ஏற்க மறுத்துள்ளனர்.",
        tags=["polity", "advocate_general", "service_conditions"]
    ))

    # 60
    questions.append(make_advg_q(
        qid="ADVG_GT_060",
        diff="Hard",
        qtype="Statement Based",
        subtopic="Constitutional Comparison",
        en_stem="Consider the following statements regarding the Advocate General in the constitutional hierarchy:\n1. In the Table of Precedence within the State, the Advocate General holds a high protocol status among legal dignitaries.\n2. He is placed above the Chief Justice of the High Court in the State Table of Precedence.\n3. His status reflects his position as the constitutional head of the State legal apparatus.\nWhich of the statements given above are correct?",
        ta_stem="அரசியலமைப்பு முன்னுரிமைப் படிநிலையில் (Table of Precedence) அட்வகேட் ஜெனரல் குறித்த பின்வரும் கூற்றுகளைக் கருதுக:\n1. மாநிலத்திற்குள் உள்ள முன்னுரிமைப் பட்டியலில், அட்வகேட் ஜெனரல் சட்டப் பிரமுகர்களிடையே உயர்ந்த நெறிமுறை அந்தஸ்தைக் கொண்டுள்ளார்.\n2. மாநில முன்னுரிமைப் பட்டியலில் உயர் நீதிமன்றத் தலைமை நீதிபதிக்கு மேலாக அவர் வைக்கப்பட்டுள்ளார்.\n3. அவரது அந்தஸ்து மாநில சட்ட அமைப்பின் அரசியலமைப்புத் தலைவர் என்ற அவரது நிலையைப் பிரதிபலிக்கிறது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?",
        en_a="1 and 3 only", ta_a="1 மற்றும் 3 மட்டுமே",
        en_b="1 and 2 only", ta_b="1 மற்றும் 2 மட்டுமே",
        en_c="2 and 3 only", ta_c="2 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3", ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statements 1 and 3 are correct. Statement 2 is incorrect because the Chief Justice of the High Court ranks much higher (along with Chief Ministers and Governors) in the Table of Precedence.",
        exp_ta="கூற்றுகள் 1 மற்றும் 3 சரியானவை. கூற்று 2 தவறானது, ஏனெனில் முன்னுரிமைப் பட்டியலில் உயர் நீதிமன்றத் தலைமை நீதிபதி அட்வகேட் ஜெனரலை விட மிக உயர்ந்த இடத்தில் உள்ளார்.",
        why_a_en="Option A is correct: Statements 1 and 3 are true; Chief Justice ranks far above the Advocate General.",
        why_a_ta="தெரிவு A சரி: 1 மற்றும் 3 சரி; தலைமை நீதிபதி AG-ஐ விட மிக உயர்ந்த இடத்தில் உள்ளார்.",
        why_b_en="Option B is incorrect: Statement 2 is false.",
        why_b_ta="தெரிவு B தவறு: கூற்று 2 தவறு.",
        why_c_en="Option C is incorrect: Statement 2 is false.",
        why_c_ta="தெரிவு C தவறு: கூற்று 2 தவறு.",
        why_d_en="Option D is incorrect: Statement 2 is false.",
        why_d_ta="தெரிவு D தவறு: கூற்று 2 தவறு.",
        tip_en="Chief Justice of High Court ranks far above the Advocate General in official State protocol.",
        tip_ta="அரசு நெறிமுறைப் பட்டியலில் உயர் நீதிமன்ற தலைமை நீதிபதி அட்வகேட் ஜெனரலை விட பல படிகள் மேலே உள்ளார்.",
        fact_en="Protocol orders are maintained and notified by the State Public Department.",
        fact_ta="முன்னுரிமை நெறிமுறைப் பட்டியல் மாநில பொதுத்துறையால் பராமரிக்கப்பட்டு அறிவிக்கப்படுகிறது.",
        tags=["polity", "advocate_general", "protocol"]
    ))

    # -------------------------------------------------------------
    # 15 Assertion-Reason MCQs (ADVG_GT_061 to ADVG_GT_075)
    # -------------------------------------------------------------

    ar_data = [
        # 61: Pleasure doctrine
        {
            "sub": "Doctrine of Pleasure",
            "a_en": "The Advocate General of a State holds office during the pleasure of the Governor.",
            "a_ta": "ஒரு மாநிலத்தின் அட்வகேட் ஜெனரல் ஆளுநரின் விருப்பம் உள்ளவரை பதவி வகிக்கிறார்.",
            "r_en": "The Advocate General is the government's chief legal adviser whose views must inspire political and legal confidence in the ruling Ministry.",
            "r_ta": "அட்வகேட் ஜெனரல் அரசின் முதன்மை சட்ட ஆலோசகர் என்பதால் அவரது கருத்துக்கள் ஆளும் அமைச்சரவைக்கு சட்ட மற்றும் அரசியல் நம்பிக்கையை அளிக்க வேண்டும்.",
            "c_key": "A",
            "exp_en": "Both A and R are true, and R is the correct explanation of A. Tenure is tied to executive pleasure to ensure the government is advised by a lawyer it trusts.",
            "exp_ta": "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A-வின் சரியான விளக்கமாகும். அரசு தனக்கு நம்பிக்கையான வழக்கறிஞரை நியமிக்க ஏதுவாகவே பதவிக்காலம் விருப்பத்தின் அடிப்படையில் உள்ளது.",
            "tip_en": "Article 165(3) = Pleasure of the Governor.", "tip_ta": "சரத்து 165(3) = ஆளுநரின் விருப்பம்."
        },
        # 62: No voting in Assembly
        {
            "sub": "Article 177 Rights",
            "a_en": "The Advocate General cannot vote in the State Legislative Assembly.",
            "a_ta": "அட்வகேட் ஜெனரலால் மாநில சட்டமன்றப் பேரவையில் வாக்களிக்க முடியாது.",
            "r_en": "Article 177 expressly excludes the right to vote because the Advocate General is not a democratically elected representative of the people.",
            "r_ta": "அட்வகேட் ஜெனரல் மக்களால் தேர்ந்தெடுக்கப்பட்ட பிரதிநிதி அல்ல என்பதால் சரத்து 177 வெளிப்படையாக வாக்களிக்கும் உரிமையை மறுக்கிறது.",
            "c_key": "A",
            "exp_en": "Both A and R are true, and R is the correct explanation of A. Democratic representation preserves voting for elected members.",
            "exp_ta": "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A-வின் சரியான விளக்கமாகும். ஜனநாயக முறைப்படி வாக்களிக்கும் உரிமை தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்களுக்கு மட்டுமே உரியது.",
            "tip_en": "Article 177: Audience yes, Vote NO.", "tip_ta": "சரத்து 177: பேசலாம், ஆனால் வாக்களிக்க முடியாது."
        },
        # 63: Age limit 62 Karkare
        {
            "sub": "Age Limit & Eligibility",
            "a_en": "A retired High Court Judge who has reached 62 years can be appointed Advocate General of a State.",
            "a_ta": "62 வயதை அடைந்த ஒரு ஓய்வுபெற்ற உயர் நீதிமன்ற நீதிபதியை ஒரு மாநிலத்தின் அட்வகேட் ஜெனரலாக நியமிக்க முடியும்.",
            "r_en": "The retirement age of 62 years applies only to the tenure of High Court judges under Article 217(1), not to eligibility for Advocate General under Article 165(1).",
            "r_ta": "62 வயது ஓய்வு வரம்பு சரத்து 217(1)-ன் கீழ் உயர் நீதிமன்ற நீதிபதிகளின் பதவிக்காலத்திற்கானது மட்டுமே, சரத்து 165(1)-ன் கீழ் அட்வகேட் ஜெனரல் தகுதிக்கு அல்ல.",
            "c_key": "A",
            "exp_en": "Both A and R are true, and R is the correct explanation of A. Settled by Nagpur HC in Karkare (1952) and SC in Atlas Cycle (1962).",
            "exp_ta": "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A-வின் சரியான விளக்கம். கார்கரே (1952) மற்றும் அட்லஸ் சைக்கிள் (1962) தீர்ப்புகளால் இது உறுதி செய்யப்பட்டுள்ளது.",
            "tip_en": "Karkare case: 62-year limit applies to tenure, NOT eligibility.", "tip_ta": "கார்கரே வழக்கு: 62 வயது வரம்பு பதவிக்காலத்திற்கானது, தகுதிக்கு அல்ல."
        },
        # 64: Contempt Mandamus
        {
            "sub": "Contempt Consent & Mandamus",
            "a_en": "A writ of Mandamus cannot be issued by the High Court to compel the Advocate General to grant consent under Section 15 of the Contempt of Courts Act.",
            "a_ta": "நீதிமன்ற அவமதிப்புச் சட்டம் பிரிவு 15-ன் கீழ் ஒப்புதல் அளிக்க அட்வகேட் ஜெனரலைக் கட்டாயப்படுத்தி உயர் நீதிமன்றத்தால் கட்டளை நீதிப்பேராணை பிறப்பிக்க முடியாது.",
            "r_en": "Granting consent under Section 15 is a quasi-judicial function involving the exercise of independent statutory discretion.",
            "r_ta": "பிரிவு 15-ன் கீழ் ஒப்புதல் அளிப்பது சுயாதீன சட்டப்பூர்வ விருப்ப உரிமையைப் பயன்படுத்தும் ஒரு நீதித்துறை போன்ற பணியாகும் (quasi-judicial).",
            "c_key": "A",
            "exp_en": "Both A and R are true, and R is the correct explanation of A (P.N. Duda v. P. Shiv Shanker, 1988).",
            "exp_ta": "A மற்றும் R இரண்டும் சரி, மற்றும் R என்பது A-ன் சரியான விளக்கமாகும் (பி.என். தூடா வழக்கு, 1988).",
            "tip_en": "Quasi-judicial discretion cannot be controlled by Mandamus.", "tip_ta": "Quasi-judicial விருப்ப அதிகாரத்தை கட்டளை நீதிப்பேராணை மூலம் கட்டுப்படுத்த முடியாது."
        },
        # 65: M.T. Khan singular post
        {
            "sub": "Singular Constitutional Office",
            "a_en": "Article 165 of the Constitution does not permit the appointment of multiple Advocates General for a single State.",
            "a_ta": "அரசியலமைப்பின் சரத்து 165 ஒரு மாநிலத்திற்கு பல அட்வகேட் ஜெனரல்களை நியமிப்பதை அனுமதிக்கவில்லை.",
            "r_en": "The Supreme Court in M.T. Khan (2004) ruled that the constitutional office of Advocate General is singular, and Additional Advocates General are executive appointments under Article 162.",
            "r_ta": "எம்.டி. கான் (2004) வழக்கில் அட்வகேட் ஜெனரல் பதவி ஒற்றையானது என்றும், கூடுதல் AG சரத்து 162-ன் கீழ் செய்யப்படும் நிர்வாக நியமனம் என்றும் உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
            "c_key": "A",
            "exp_en": "Both A and R are true, and R is the correct explanation of A. Article 165 creates one Advocate General per State.",
            "exp_ta": "A மற்றும் R இரண்டும் சரி, மற்றும் R என்பது A-ன் சரியான விளக்கமாகும். சரத்து 165 மாநிலத்திற்கு ஒரு AG-ஐ மட்டுமே உருவாக்குகிறது.",
            "tip_en": "M.T. Khan (2004): Only ONE Advocate General per State.", "tip_ta": "எம்.டி. கான் (2004): ஒரு மாநிலத்திற்கு ஒரு AG மட்டுமே."
        },
        # 66: Article 311 Civil Servant
        {
            "sub": "Civil Service Protection",
            "a_en": "The Advocate General is not a civil servant under Article 311 of the Constitution.",
            "a_ta": "அரசியலமைப்பின் சரத்து 311-ன் கீழ் அட்வகேட் ஜெனரல் ஒரு அரசு ஊழியர் அல்ல.",
            "r_en": "The Advocate General is a constitutional law officer holding office during pleasure without permanent civil service cadre protection.",
            "r_ta": "அட்வகேட் ஜெனரல் நிரந்தர சிவில் சர்வீஸ் பாதுகாப்பு இன்றி விருப்பத்தின் அடிப்படையில் பதவி வகிக்கும் அரசியலமைப்பு சட்ட அதிகாரி ஆவார்.",
            "c_key": "A",
            "exp_en": "Both A and R are true, and R correctly explains A. Article 311 applies to members of civil services, not pleasure-based constitutional officers.",
            "exp_ta": "A மற்றும் R இரண்டும் சரி, மற்றும் R என்பது A-ன் சரியான விளக்கமாகும். சரத்து 311 சிவில் பணியாளர்களுக்கு மட்டுமே பொருந்தும்.",
            "tip_en": "Article 311 protection does NOT apply to the Advocate General.", "tip_ta": "சரத்து 311 பாதுகாப்பு அட்வகேட் ஜெனரலுக்குப் பொருந்தாது."
        },
        # 67: Conflict of Interest
        {
            "sub": "Fiduciary Obligations",
            "a_en": "An Advocate General cannot brief or advise a private litigant against the State Government in any court.",
            "a_ta": "எந்தவொரு நீதிமன்றத்திலும் மாநில அரசுக்கு எதிராக ஒரு தனியார் தரப்பினருக்கு அட்வகேட் ஜெனரல் வழக்காடவோ ஆலோசனையளிக்கவோ முடியாது.",
            "r_en": "A fiduciary relationship of high public trust exists between the State and its chief law officer, strictly prohibiting conflicts of interest.",
            "r_ta": "அரசுக்கும் அதன் தலைமை சட்ட அதிகாரிக்கும் இடையே பொது நம்பிக்கை கொண்ட விசுவாசப் பொறுப்பு நிலவுவதால் நலன் முரண்பாடுகள் கண்டிப்பாகத் தடுக்கப்படுகின்றன.",
            "c_key": "A",
            "exp_en": "Both A and R are true, and R correctly explains A. Fiduciary duty prohibits taking briefs adverse to the client/State.",
            "exp_ta": "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A-ன் சரியான விளக்கமாகும். விசுவாசப் பொறுப்பு அரசுக்கு எதிராக வழக்காடுவதைத் தடுக்கிறது.",
            "tip_en": "Fiduciary duty bars brief against the State.", "tip_ta": "விசுவாசக் கடமை அரசுக்கு எதிராக வழக்காடுவதைத் தடுக்கிறது."
        },
        # 68: Bar Council Ex-officio
        {
            "sub": "State Bar Council Link",
            "a_en": "The Advocate General is an ex-officio member of the Bar Council of the State.",
            "a_ta": "அட்வகேட் ஜெனரல் மாநில பார் கவுன்சிலின் பதவி வழி உறுப்பினர் ஆவார்.",
            "r_en": "Section 3(2)(c) of the Advocates Act, 1961 statutorily recognizes the Advocate General as an ex-officio member to link the legal profession with the State.",
            "r_ta": "வழக்கறிஞர்கள் சட்டம் 1961 பிரிவு 3(2)(c) சட்டத்துறையையும் அரசையும் இணைப்பதற்காக அட்வகேட் ஜெனரலை பதவி வழி உறுப்பினராக சட்டப்பூர்வமாக அங்கீகரிக்கிறது.",
            "c_key": "A",
            "exp_en": "Both A and R are true, and R is the correct explanation of A.",
            "exp_ta": "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A-ன் சரியான விளக்கமாகும்.",
            "tip_en": "Advocates Act Sec 3(2)(c) = Advocate General is ex-officio member.", "tip_ta": "வழக்கறிஞர்கள் சட்டம் 3(2)(c) = AG பதவி வழி உறுப்பினர்."
        },
        # 69: Absolute Parliamentary Immunity
        {
            "sub": "Article 194 Privileges",
            "a_en": "The Advocate General enjoys absolute immunity from civil and criminal court proceedings for statements made in the State Legislative Assembly.",
            "a_ta": "மாநில சட்டமன்றப் பேரவையில் பேசிய பேச்சுகளுக்காக உரிமையியல் மற்றும் குற்றவியல் நீதிமன்ற நடவடிக்கைகளிலிருந்து அட்வகேட் ஜெனரலுக்கு முழுமையான பாதுகாப்பு உண்டு.",
            "r_en": "Article 194(4) extends the legislative speech immunities of Article 194(2) to all persons who have the right to speak in the Legislature.",
            "r_ta": "சரத்து 194(4) சட்டமன்றத்தில் பேச உரிமை பெற்ற அனைத்து நபர்களுக்கும் சரத்து 194(2)-ன் பேச்சுரிமைப் பாதுகாப்பை நீட்டிக்கிறது.",
            "c_key": "A",
            "exp_en": "Both A and R are true, and R correctly explains A. Article 194(4) explicitly extends MLA speech privileges to the Advocate General.",
            "exp_ta": "A மற்றும் R இரண்டும் சரி, மற்றும் R என்பது A-ன் சரியான விளக்கமாகும். சரத்து 194(4) எம்.எல்.ஏ சலுகைகளை AG-க்கும் நீட்டிக்கிறது.",
            "tip_en": "Article 194(2) + 194(4) = Absolute speech immunity.", "tip_ta": "சரத்து 194(2) + 194(4) = முழுமையான பேச்சுரிமைப் பாதுகாப்பு."
        },
        # 70: Distinguished Jurist
        {
            "sub": "Qualifications Criteria",
            "a_en": "A distinguished jurist cannot be appointed as the Advocate General of a State.",
            "a_ta": "ஒரு புகழ்பெற்ற சட்ட வல்லுநரை ஒரு மாநிலத்தின் அட்வகேட் ஜெனரலாக நியமிக்க முடியாது.",
            "r_en": "Unlike Article 124(3)(c) for Supreme Court judges, Article 217(2) does not include the category of 'distinguished jurist' for High Court eligibility.",
            "r_ta": "உச்ச நீதிமன்ற நீதிபதிகளுக்கான சரத்து 124(3)(c) போலன்றி, உயர் நீதிமன்றத் தகுதிக்கான சரத்து 217(2)-ல் 'புகழ்பெற்ற சட்ட வல்லுநர்' பிரிவு சேர்க்கப்படவில்லை.",
            "c_key": "A",
            "exp_en": "Both A and R are true, and R is the correct explanation of A. Article 217(2) only recognizes judicial service or High Court practice.",
            "exp_ta": "A மற்றும் R இரண்டும் சரி, மற்றும் R என்பது A-ன் சரியான விளக்கமாகும். சரத்து 217(2) நீதித்துறை பணி அல்லது வழக்கறிஞர் அனுபவத்தை மட்டுமே அங்கீகரிக்கிறது.",
            "tip_en": "Distinguished jurist: SC YES, HC NO.", "tip_ta": "புகழ்பெற்ற சட்ட வல்லுநர்: உச்ச நீதிமன்றத்திற்கு உண்டு, உயர் நீதிமன்றத்திற்கு இல்லை."
        },
        # 71: Quorum Trap (A true, R false)
        {
            "sub": "Quorum and Voting",
            "a_en": "The presence of the Advocate General in the State Legislative Assembly does not count towards the quorum required under Article 189(3).",
            "a_ta": "சரத்து 189(3)-ன் கீழ் தேவைப்படும் குறைந்தபட்ச உறுப்பினர் எண்ணிக்கையில் (Quorum) அட்வகேட் ஜெனரலின் இருப்பு கணக்கிடப்படாது.",
            "r_en": "The Advocate General has the constitutional right to vote on money bills in the Legislative Assembly.",
            "r_ta": "சட்டமன்றப் பேரவையில் நிதி முன்வடிவுகள் மீது வாக்களிக்கும் அரசியலமைப்பு உரிமை அட்வகேட் ஜெனரலுக்கு உண்டு.",
            "c_key": "C",
            "exp_en": "Assertion A is true (AG presence does not count for quorum). Reason R is FALSE because Article 177 explicitly denies the Advocate General the right to vote on ANY bill.",
            "exp_ta": "கூற்று A சரி (கோரத்தில் கணக்கிடப்பட மாட்டார்). காரணம் R தவறு, ஏனெனில் சரத்து 177 எந்த ஒரு மசோதாவின் மீதும் வாக்களிக்கும் உரிமையை AG-க்கு மறுக்கிறது.",
            "tip_en": "Advocate General has NO vote on any bill, including Money Bills.", "tip_ta": "நிதி மசோதா உட்பட எதிலும் AG வாக்களிக்க முடியாது."
        },
        # 72: Both false (Criminal defense)
        {
            "sub": "Ethical Restrictions",
            "a_en": "The Advocate General can defend any accused person in a murder trial without seeking permission from the State Government.",
            "a_ta": "மாநில அரசிடம் அனுமதி பெறாமலேயே கொலை வழக்கில் குற்றம் சாட்டப்பட்ட எந்தவொரு நபரையும் அட்வகேட் ஜெனரல் பாதுகாக்க முடியும்.",
            "r_en": "Private criminal defense practice is unconditionally guaranteed to the Advocate General by the Advocates Act, 1961.",
            "r_ta": "தனியார் குற்றவியல் வழக்குகளில் ஆஜராகும் உரிமை வழக்கறிஞர்கள் சட்டம் 1961-ஆல் அட்வகேட் ஜெனரலுக்கு நிபந்தனையின்றி உத்தரவாதம் அளிக்கப்பட்டுள்ளது.",
            "c_key": "D",
            "exp_en": "Both Assertion A and Reason R are false. State Law Officers rules strictly prohibit defending accused persons in criminal cases without prior government sanction.",
            "exp_ta": "கூற்று A மற்றும் காரணம் R ஆகிய இரண்டுமே தவறானவை. அரசின் அனுமதியின்றி குற்றவியல் வழக்குகளில் குற்றவாளிகளைப் பாதுகாப்பது கடுமையான தடையாகும்.",
            "tip_en": "Criminal defense without permission is strictly prohibited.", "tip_ta": "அனுமதியின்றி குற்றவாளிகளைப் பாதுகாப்பது கண்டிப்பாக தடைசெய்யப்பட்டுள்ளது."
        },
        # 73: Both false (Charged expenditure)
        {
            "sub": "Remuneration Status",
            "a_en": "The remuneration of the Advocate General is an expenditure charged on the Consolidated Fund of the State.",
            "a_ta": "அட்வகேட் ஜெனரலின் ஊதியம் மாநிலத் திரட்டப்பட்ட நிதியில் சார்ஜ் செய்யப்பட்ட செலவினமாகும்.",
            "r_en": "High constitutional officers cannot have their remuneration subjected to the annual vote of the State Legislative Assembly.",
            "r_ta": "உயரிய அரசியலமைப்பு அதிகாரிகளின் ஊதியம் மாநில சட்டமன்றத்தின் வருடாந்திர வாக்கெடுப்புக்கு உட்படுத்தப்பட முடியாது.",
            "c_key": "D",
            "exp_en": "Both Assertion A and Reason R are false. The remuneration of the Advocate General is determined by the Governor under Article 165(3) and is NOT a charged expenditure under Article 202(3); it is voted as part of the Law Department budget.",
            "exp_ta": "கூற்று A மற்றும் காரணம் R இரண்டும் தவறானவை. அட்வகேட் ஜெனரலின் ஊதியம் சரத்து 202(3)-ல் சார்ஜ் செய்யப்படுவதில்லை; இது சட்டமன்றத்தால் வாக்களிக்கப்படுகிறது.",
            "tip_en": "Advocate General's salary is NOT charged on the Consolidated Fund.", "tip_ta": "அட்வகேட் ஜெனரலின் ஊதியம் திரட்டப்பட்ட நிதியில் சார்ஜ் செய்யப்படுவதில்லை."
        },
        # 74: Both false (Cabinet presidency)
        {
            "sub": "Executive Separation",
            "a_en": "The Advocate General presides over the meetings of the State Cabinet whenever a constitutional amendment bill is discussed.",
            "a_ta": "அரசியலமைப்பு திருத்த மசோதா விவாதிக்கப்படும் போதெல்லாம் அட்வகேட் ஜெனரலே மாநில அமைச்சரவைக் கூட்டத்திற்குத் தலைமை தாங்குகிறார்.",
            "r_en": "The Advocate General is an ex-officio member of the State Cabinet under Article 163.",
            "r_ta": "சரத்து 163-ன் கீழ் அட்வகேட் ஜெனரல் மாநில அமைச்சரவையின் பதவி வழி உறுப்பினர் ஆவார்.",
            "c_key": "D",
            "exp_en": "Both Assertion A and Reason R are false. The Chief Minister presides over Cabinet meetings. The Advocate General is NOT a member of the Cabinet.",
            "exp_ta": "கூற்று A மற்றும் காரணம் R இரண்டும் தவறானவை. முதலமைச்சரே அமைச்சரவைக்குத் தலைமை தாங்குகிறார். அட்வகேட் ஜெனரல் அமைச்சரவை உறுப்பினரே அல்ல.",
            "tip_en": "Advocate General is NOT a Cabinet member; Chief Minister presides over Cabinet.", "tip_ta": "AG அமைச்சரவை உறுப்பினர் அல்ல; முதலமைச்சரே அமைச்சரவைக்குத் தலைமை தாங்குகிறார்."
        },
        # 75: Both false (Chief Justice concurrence)
        {
            "sub": "Appointment Power",
            "a_en": "The Governor must obtain the written concurrence of the Chief Justice of the High Court before appointing the Advocate General under Article 165.",
            "a_ta": "சரத்து 165-ன் கீழ் அட்வகேட் ஜெனரலை நியமிப்பதற்கு முன் ஆளுநர் உயர் நீதிமன்றத் தலைமை நீதிபதியின் எழுத்துப்பூர்வ ஒப்புதலைப் பெற வேண்டும்.",
            "r_en": "High Court Judge qualifications must be verified by the High Court Collegium for all constitutional appointments in the State.",
            "r_ta": "மாநிலத்தின் அனைத்து அரசியலமைப்பு நியமனங்களுக்கும் உயர் நீதிமன்ற நீதிபதி தகுதியை உயர் நீதிமன்ற கொலீஜியம் சரிபார்க்க வேண்டும்.",
            "c_key": "D",
            "exp_en": "Both Assertion A and Reason R are false. The Governor appoints the Advocate General solely on the aid and advice of the Council of Ministers (Art 163); consultation with the Chief Justice is not required.",
            "exp_ta": "கூற்று A மற்றும் காரணம் R இரண்டும் தவறானவை. அமைச்சரவையின் ஆலோசனையின் பேரில் மட்டுமே ஆளுநர் நியமிக்கிறார்; தலைமை நீதிபதியிடம் ஆலோசனை தேவையில்லை.",
            "tip_en": "No High Court Chief Justice consultation is required for Advocate General appointment.", "tip_ta": "அட்வகேட் ஜெனரல் நியமனத்திற்கு தலைமை நீதிபதியிடம் ஆலோசனை தேவையில்லை."
        }
    ]

    for i, ar in enumerate(ar_data):
        qid = f"ADVG_GT_{61+i:03d}"
        stem_en = f"Given below are two statements, one labelled as Assertion (A) and the other as Reason (R):\nAssertion (A): {ar['a_en']}\nReason (R): {ar['r_en']}\nIn the context of the above two statements, which of the following is correct?"
        stem_ta = f"கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): {ar['a_ta']}\nகாரணம் (R): {ar['r_ta']}\nமேற்கண்ட இரு கூற்றுகளின் அடிப்படையில், பின்வருவனவற்றுள் எது சரியானது?"

        opt_a_en = "Both (A) and (R) are true, and (R) is the correct explanation of (A)"
        opt_a_ta = "(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-வின் சரியான விளக்கமாகும்"
        opt_b_en = "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)"
        opt_b_ta = "(A) மற்றும் (R) இரண்டும் சரி, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல"
        opt_c_en = "(A) is true, but (R) is false"
        opt_c_ta = "(A) சரி, ஆனால் (R) தவறு"
        opt_d_en = "Both (A) and (R) are false"
        opt_d_ta = "(A) மற்றும் (R) இரண்டும் தவறு"

        why_dict = {
            "A": {"en": "Option A is correct: Both assertion and reason are constitutionally true, and reason correctly explains the assertion.", "ta": "தெரிவு A சரி: கூற்று மற்றும் காரணம் இரண்டும் சரியானவை, காரணம் கூற்றை விளக்குகிறது."},
            "B": {"en": "Option B is incorrect.", "ta": "தெரிவு B தவறானது."},
            "C": {"en": "Option C is correct: The assertion is true but the reason is factually and constitutionally false.", "ta": "தெரிவு C சரி: கூற்று சரியானது ஆனால் காரணம் தவறானது."},
            "D": {"en": "Option D is correct: Both the assertion and the reason are factually and constitutionally false.", "ta": "தெரிவு D சரி: கூற்று மற்றும் காரணம் ஆகிய இரண்டுமே தவறானவை."}
        }

        correct_key = ar["c_key"]

        q = make_advg_q(
            qid=qid,
            diff="Hard",
            qtype="Assertion-Reasoning",
            subtopic=ar["sub"],
            en_stem=stem_en,
            ta_stem=stem_ta,
            en_a=opt_a_en, ta_a=opt_a_ta,
            en_b=opt_b_en, ta_b=opt_b_ta,
            en_c=opt_c_en, ta_c=opt_c_ta,
            en_d=opt_d_en, ta_d=opt_d_ta,
            correct_key=correct_key,
            exp_en=ar["exp_en"],
            exp_ta=ar["exp_ta"],
            why_a_en=why_dict["A"]["en"] if correct_key == "A" else "Option A is incorrect.",
            why_a_ta=why_dict["A"]["ta"] if correct_key == "A" else "தெரிவு A தவறானது.",
            why_b_en=why_dict["B"]["en"] if correct_key == "B" else "Option B is incorrect.",
            why_b_ta=why_dict["B"]["ta"] if correct_key == "B" else "தெரிவு B தவறானது.",
            why_c_en=why_dict["C"]["en"] if correct_key == "C" else "Option C is incorrect.",
            why_c_ta=why_dict["C"]["ta"] if correct_key == "C" else "தெரிவு C தவறானது.",
            why_d_en=why_dict["D"]["en"] if correct_key == "D" else "Option D is incorrect.",
            why_d_ta=why_dict["D"]["ta"] if correct_key == "D" else "தெரிவு D தவறானது.",
            tip_en=ar["tip_en"],
            tip_ta=ar["tip_ta"],
            fact_en=f"Assertion-Reasoning question analyzing {ar['sub']}.",
            fact_ta=f"{ar['sub']} தொடர்பான கூற்று-காரணக் கேள்வி.",
            tags=["polity", "advocate_general", "assertion_reasoning"]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 15 Match the Following MCQs (ADVG_GT_076 to ADVG_GT_090)
    # -------------------------------------------------------------

    match_gt_data = [
        # 76: Constitutional Articles
        {
            "sub": "Constitutional Articles",
            "t_en": "Match List-I (Constitutional Articles) with List-II (Subject concerning Advocate General):",
            "t_ta": "பட்டியல்-I-ஐ (அரசியலமைப்புச் சரத்துகள்) பட்டியல்-II உடன் (அட்வகேட் ஜெனரல் தொடர்பான பொருள்) பொருத்துக:",
            "l1_en": [("a. Article 165(1)", "1. Appointment & qualifications of Advocate General"),
                      ("b. Article 165(2)", "2. Duties to advise State Government on legal matters"),
                      ("c. Article 165(3)", "3. Tenure during pleasure of Governor and remuneration"),
                      ("d. Article 177", "4. Right to speak in State Legislature without vote")],
            "l1_ta": [("a. சரத்து 165(1)", "1. அட்வகேட் ஜெனரலின் நியமனம் & தகுதிகள்"),
                      ("b. சரத்து 165(2)", "2. மாநில அரசுக்கு சட்ட ஆலோசனை வழங்கும் கடமைகள்"),
                      ("c. சரத்து 165(3)", "3. ஆளுநரின் விருப்பப்படி பதவிக்காலம் மற்றும் ஊதியம்"),
                      ("d. சரத்து 177", "4. வாக்களிக்கும் உரிமையின்றி சட்டமன்றத்தில் பேசும் உரிமை")],
            "opts": ["a-1, b-2, c-3, d-4", "a-2, b-1, c-4, d-3", "a-3, b-4, c-1, d-2", "a-4, b-3, c-2, d-1"]
        },
        # 77: Statutory Enactments
        {
            "sub": "Statutory Enactments",
            "t_en": "Match List-I (Statutory Enactments) with List-II (Advocate General's Authority):",
            "t_ta": "பட்டியல்-I-ஐ (சட்டங்கள்) பட்டியல்-II உடன் (அட்வகேட் ஜெனரலின் அதிகாரம்) பொருத்துக:",
            "l1_en": [("a. Section 23, Advocates Act 1961", "1. Statutory pre-audience over all advocates in the State"),
                      ("b. Section 15, Contempt of Courts Act 1971", "2. Prior written consent for criminal contempt in High Court"),
                      ("c. Section 91, Code of Civil Procedure 1908", "3. Instituting civil suits for public nuisance"),
                      ("d. Section 301, Code of Criminal Procedure 1973", "4. Appearance in criminal courts without vakalatnama")],
            "l1_ta": [("a. பிரிவு 23, வழக்கறிஞர்கள் சட்டம் 1961", "1. மாநிலத்தில் உள்ள அனைத்து வழக்கறிஞர்களையும் விட முதன்மை வாதாடும் உரிமை"),
                      ("b. பிரிவு 15, நீதிமன்ற அவமதிப்புச் சட்டம் 1971", "2. உயர் நீதிமன்ற குற்றவியல் அவமதிப்புக்கு முன் எழுத்துப்பூர்வ ஒப்புதல்"),
                      ("c. பிரிவு 91, உரிமையியல் நடைமுறைச் சட்டம் 1908", "3. பொதுத்தொல்லைக்காக உரிமையியல் வழக்கு தொடருதல்"),
                      ("d. பிரிவு 301, குற்றவியல் நடைமுறைச் சட்டம் 1973", "4. வக்காலத்து இன்றி குற்றவியல் நீதிமன்றங்களில் முன்னிலையாதல்")],
            "opts": ["a-1, b-2, c-3, d-4", "a-3, b-4, c-1, d-2", "a-2, b-1, c-4, d-3", "a-4, b-2, c-1, d-3"]
        },
        # 78: Landmark Cases
        {
            "sub": "Landmark Decisions",
            "t_en": "Match List-I (Landmark Judicial Cases) with List-II (Principle Laid Down):",
            "t_ta": "பட்டியல்-I-ஐ (முக்கிய வழக்குகள்) பட்டியல்-II உடன் (வகுக்கப்பட்ட கொள்கை) பொருத்துக:",
            "l1_en": [("a. G.D. Karkare v. T.L. Shevde (1952)", "1. 62-year retirement age does not apply to Advocate General"),
                      ("b. M.T. Khan v. Govt. of A.P. (2004)", "2. Only one constitutional AG per State; Addl AG is executive"),
                      ("c. P.N. Duda v. P. Shiv Shanker (1988)", "3. Contempt consent is quasi-judicial; no Mandamus lies"),
                      ("d. State of UP v. UP Law Officers (1994)", "4. Law officers hold positions of public trust, not mere hirelings")],
            "l1_ta": [("a. ஜி.டி. கார்கரே எதிர் டி.எல். ஷேவ்டே (1952)", "1. 62 வயது ஓய்வு வரம்பு அட்வகேட் ஜெனரலுக்குப் பொருந்தாது"),
                      ("b. எம்.டி. கான் எதிர் ஆந்திர அரசு (2004)", "2. ஒரு மாநிலத்திற்கு ஒரு AG மட்டுமே; கூடுதல் AG நிர்வாகப் பதவி"),
                      ("c. பி.என். தூடா எதிர் பி. சிவ சங்கர் (1988)", "3. அவமதிப்பு ஒப்புதல் quasi-judicial; கட்டளை நீதிப்பேராணை பிறப்பிக்க முடியாது"),
                      ("d. உ.பி. அரசு எதிர் உ.பி. சட்ட அதிகாரிகள் (1994)", "4. சட்ட அதிகாரிகள் பொது நம்பிக்கை பதவிகளை வகிக்கின்றனர்")],
            "opts": ["a-1, b-2, c-3, d-4", "a-2, b-1, c-4, d-3", "a-4, b-3, c-2, d-1", "a-3, b-4, c-1, d-2"]
        },
        # 79: Historical Milestones
        {
            "sub": "Historical Charters",
            "t_en": "Match List-I (Historical Charters & Enactments) with List-II (Institutional Evolution):",
            "t_ta": "பட்டியல்-I-ஐ (வரலாற்று சாசனங்கள் & சட்டங்கள்) பட்டியல்-II உடன் (நிறுவன வளர்ச்சி) பொருத்துக:",
            "l1_en": [("a. Charter of 1800", "1. Supreme Court of Judicature established at Madras"),
                      ("b. Indian Councils Act, 1861", "2. Advocate General given right to speak in Governor's Council"),
                      ("c. Government of India Act, 1935 (Sec 55)", "3. Formalized provincial Advocate-General appointment by Governor"),
                      ("d. Constitution of India, 1950 (Art 165)", "4. Constitutional status of Advocate General of the State")],
            "l1_ta": [("a. 1800 சாசனம்", "1. மெட்ராஸில் உச்ச நீதிமன்ற நீதித்துறை அமைப்பு நிறுவப்பட்டது"),
                      ("b. இந்திய கவுன்சில்கள் சட்டம், 1861", "2. ஆளுநர் கவுன்சிலில் பேச அட்வகேட் ஜெனரலுக்கு உரிமை வழங்கப்பட்டது"),
                      ("c. இந்திய அரசுச் சட்டம், 1935 (பிரிவு 55)", "3. ஆளுநரால் மாகாண அட்வகேட்-ஜெனரல் நியமிக்கப்படுவதை முறைப்படுத்தியது"),
                      ("d. இந்திய அரசியலமைப்பு, 1950 (சரத்து 165)", "4. மாநில அட்வகேட் ஜெனரலின் அரசியலமைப்பு அந்தஸ்து")],
            "opts": ["a-1, b-2, c-3, d-4", "a-2, b-1, c-4, d-3", "a-3, b-4, c-1, d-2", "a-4, b-3, c-2, d-1"]
        },
        # 80: State Law Officers
        {
            "sub": "Law Officers Hierarchy",
            "t_en": "Match List-I (State Law Officers) with List-II (Constitutional / Statutory Base):",
            "t_ta": "பட்டியல்-I-ஐ (மாநில சட்ட அதிகாரிகள்) பட்டியல்-II உடன் (அரசியலமைப்பு / சட்ட அடிப்படை) பொருத்துக:",
            "l1_en": [("a. Advocate General", "1. Article 165 of the Constitution"),
                      ("b. Additional Advocate General", "2. Article 162 executive power of the State"),
                      ("c. Public Prosecutor", "3. Section 24 of the Code of Criminal Procedure"),
                      ("d. Government Pleader", "4. Order XXVII Rule 8B of the Code of Civil Procedure")],
            "l1_ta": [("a. அட்வகேட் ஜெனரல்", "1. அரசியலமைப்பின் சரத்து 165"),
                      ("b. கூடுதல் அட்வகேட் ஜெனரல்", "2. மாநிலத்தின் சரத்து 162 நிர்வாக அதிகாரம்"),
                      ("c. அரசு குற்றவியல் வழக்கறிஞர்", "3. குற்றவியல் நடைமுறைச் சட்டம் பிரிவு 24"),
                      ("d. அரசு பிளீடர்", "4. உரிமையியல் நடைமுறைச் சட்டம் கட்டளை XXVII விதி 8B")],
            "opts": ["a-1, b-2, c-3, d-4", "a-3, b-4, c-1, d-2", "a-2, b-1, c-4, d-3", "a-4, b-2, c-1, d-3"]
        },
        # 81: Disqualifications
        {
            "sub": "Disqualifications",
            "t_en": "Match List-I (Constitutional & Professional Limitations) with List-II (Constitutional/Ethical Source):",
            "t_ta": "பட்டியல்-I-ஐ (கட்டுப்பாடுகள்) பட்டியல்-II உடன் (சட்ட மூலம்) பொருத்துக:",
            "l1_en": [("a. Barred from voting in State Assembly", "1. Article 177 explicit prohibition"),
                      ("b. Barred from contesting elections as office of profit", "2. Article 191(1)(a) disqualification"),
                      ("c. Barred from briefing against the State", "3. Fiduciary duty and conflict of interest"),
                      ("d. Barred from corporate directorship without permission", "4. State Law Officers conditions of service")],
            "l1_ta": [("a. சட்டமன்றத்தில் வாக்களிக்கத் தடை", "1. சரத்து 177 வெளிப்படையான தடை"),
                      ("b. ஆதாயப் பதவி காரணமாக தேர்தலில் போட்டியிடத் தடை", "2. சரத்து 191(1)(a) தகுதியிழப்பு"),
                      ("c. அரசுக்கு எதிராக வாதாடத் தடை", "3. விசுவாசக் கடமை மற்றும் நலன் முரண்பாடு"),
                      ("d. அனுமதியின்றி நிறுவன இயக்குநர் பதவி ஏற்கத் தடை", "4. மாநில சட்ட அதிகாரிகள் பணி நிபந்தனைகள்")],
            "opts": ["a-1, b-2, c-3, d-4", "a-2, b-1, c-4, d-3", "a-4, b-3, c-2, d-1", "a-3, b-4, c-1, d-2"]
        },
        # 82: Authorities Relation
        {
            "sub": "Constitutional Authorities",
            "t_en": "Match List-I (Constitutional Functionaries) with List-II (Relation with Advocate General):",
            "t_ta": "பட்டியல்-I-ஐ (அரசியலமைப்பு அதிகாரிகள்) பட்டியல்-II உடன் (அட்வகேட் ஜெனரலுடனான தொடர்பு) பொருத்துக:",
            "l1_en": [("a. Governor of the State", "1. Appoints AG and determines remuneration at pleasure"),
                      ("b. Chief Minister of the State", "2. Recommends selection and resignation of AG"),
                      ("c. Speaker of the Assembly", "3. Presides when AG participates in legislative debates"),
                      ("d. Chief Justice of High Court", "4. Heads the judicial institution where AG is leader of Bar")],
            "l1_ta": [("a. மாநில ஆளுநர்", "1. AG-ஐ நியமித்து விருப்பப்படி ஊதியம் நிர்ணயிக்கிறார்"),
                      ("b. மாநில முதலமைச்சர்", "2. AG தேர்வு மற்றும் ராஜினாமாவைப் பரிந்துரைக்கிறார்"),
                      ("c. சட்டமன்ற சபாநாயகர்", "3. AG விவாதங்களில் பங்கேற்கும் போது தலைமை தாங்குகிறார்"),
                      ("d. உயர் நீதிமன்ற தலைமை நீதிபதி", "4. AG பார் தலைவராக உள்ள நீதிமன்றத்திற்கு தலைமை தாங்குகிறார்")],
            "opts": ["a-1, b-2, c-3, d-4", "a-3, b-4, c-1, d-2", "a-2, b-1, c-4, d-3", "a-4, b-2, c-1, d-3"]
        },
        # 83: Pre-Audience Ranks
        {
            "sub": "Pre-Audience Hierarchy",
            "t_en": "Match List-I (Pre-Audience Hierarchy under Section 23) with List-II (Designated Law Officers):",
            "t_ta": "பட்டியல்-I-ஐ (பிரிவு 23 முன்னுரிமை வரிசை) பட்டியல்-II உடன் (சட்ட அதிகாரிகள்) பொருத்துக:",
            "l1_en": [("a. National Rank 1 (all courts)", "1. Attorney General of India"),
                      ("b. National Rank 2 (Supreme Court)", "2. Solicitor General of India"),
                      ("c. National Rank 3 (Supreme Court)", "3. Additional Solicitor General of India"),
                      ("d. State Rank 1 (courts in the State)", "4. Advocate General of that State")],
            "l1_ta": [("a. தேசிய தரம் 1 (அனைத்து நீதிமன்றங்கள்)", "1. இந்திய தலைமை வழக்கறிஞர்"),
                      ("b. தேசிய தரம் 2 (உச்ச நீதிமன்றம்)", "2. இந்திய சொலிசிட்டர் ஜெனரல்"),
                      ("c. தேசிய தரம் 3 (உச்ச நீதிமன்றம்)", "3. இந்திய கூடுதல் சொலிசிட்டர் ஜெனரல்"),
                      ("d. மாநில தரம் 1 (மாநில நீதிமன்றங்கள்)", "4. அந்த மாநில அட்வகேட் ஜெனரல்")],
            "opts": ["a-1, b-2, c-3, d-4", "a-2, b-1, c-4, d-3", "a-4, b-3, c-2, d-1", "a-3, b-4, c-1, d-2"]
        },
        # 84: Historic Madras AGs
        {
            "sub": "Historic Madras AGs",
            "t_en": "Match List-I (Distinguished Madras Advocates General) with List-II (Historic Contribution):",
            "t_ta": "பட்டியல்-I-ஐ (மெட்ராஸ் அட்வகேட் ஜெனரல்கள்) பட்டியல்-II உடன் (வரலாற்று பங்களிப்பு) பொருத்துக:",
            "l1_en": [("a. Sir V. Bhashyam Aiyangar", "1. First Indian Advocate General of Madras (1899/1900)"),
                      ("b. S. Srinivasa Iyengar", "2. Resigned post to become INC President at Gauhati (1926)"),
                      ("c. Sir Alladi Krishnaswamy Iyer", "3. Madras AG for 15 years; Constitution Drafting Committee Member"),
                      ("d. K. Rajah Iyer", "4. First Advocate General of post-independence Madras State (1947)")],
            "l1_ta": [("a. சர் வி. பாஷ்யம் ஐயங்கார்", "1. மெட்ராஸின் முதல் இந்திய அட்வகேட் ஜெனரல் (1899/1900)"),
                      ("b. எஸ். சீனிவாச ஐயங்கார்", "2. பதவியை ராஜினாமா செய்து 1926 கவுகாத்தி காங்கிரஸ் தலைவர் ஆனார்"),
                      ("c. சர் அல்லாடி கிருஷ்ணசுவாமி ஐயர்", "3. 15 ஆண்டுகள் மெட்ராஸ் AG; வரைவுக் குழு உறுப்பினர்"),
                      ("d. கே. ராஜா ஐயர்", "4. சுதந்திரத்திற்குப் பிந்தைய மெட்ராஸ் மாநிலத்தின் முதல் AG (1947)")],
            "opts": ["a-1, b-2, c-3, d-4", "a-3, b-4, c-1, d-2", "a-2, b-1, c-4, d-3", "a-4, b-2, c-1, d-3"]
        },
        # 85: Procedural Powers
        {
            "sub": "Procedural Powers",
            "t_en": "Match List-I (Procedural Sections) with List-II (Nature of Proceeding):",
            "t_ta": "பட்டியல்-I-ஐ (நடைமுறைப் பிரிவுகள்) பட்டியல்-II உடன் (நடவடிக்கையின் தன்மை) பொருத்துக:",
            "l1_en": [("a. Section 91, CPC", "1. Public Nuisance declaration and injunction"),
                      ("b. Section 92, CPC", "2. Breach of trust in Public Charities and religious trusts"),
                      ("c. Section 301, CrPC", "3. Conduct of prosecution without written authority"),
                      ("d. Section 321, CrPC", "4. Withdrawal from criminal prosecution with court consent")],
            "l1_ta": [("a. பிரிவு 91, CPC", "1. பொதுத்தொல்லை விளம்புரிமை மற்றும் தடை உத்தரவு"),
                      ("b. பிரிவு 92, CPC", "2. பொது அறக்கட்டளைகளில் நம்பிக்கை மீறல் வழக்கு"),
                      ("c. பிரிவு 301, CrPC", "3. எழுத்துப்பூர்வ அதிகாரமின்றி வழக்கை நடத்துதல்"),
                      ("d. பிரிவு 321, CrPC", "4. நீதிமன்ற அனுமதியுடன் குற்ற வழக்கைத் திரும்பப் பெறுதல்")],
            "opts": ["a-1, b-2, c-3, d-4", "a-2, b-1, c-4, d-3", "a-4, b-3, c-2, d-1", "a-3, b-4, c-1, d-2"]
        },
        # 86: Contempt Act Sections
        {
            "sub": "Contempt of Courts Act",
            "t_en": "Match List-I (Contempt of Courts Act Sections) with List-II (Subject Matter):",
            "t_ta": "பட்டியல்-I-ஐ (அவமதிப்புச் சட்டப் பிரிவுகள்) பட்டியல்-II உடன் (பொருள்) பொருத்துக:",
            "l1_en": [("a. Section 2(c)", "1. Definition of Criminal Contempt"),
                      ("b. Section 14", "2. Procedure where contempt is in the face of the Supreme Court or High Court"),
                      ("c. Section 15(1)(b)", "3. Criminal contempt on motion brought by Advocate General"),
                      ("d. Section 20", "4. Limitation period of one year for initiating contempt proceedings")],
            "l1_ta": [("a. பிரிவு 2(c)", "1. குற்றவியல் அவமதிப்பின் வரையறை"),
                      ("b. பிரிவு 14", "2. நீதிமன்றத்தின் முன்னிலையில் நடக்கும் அவமதிப்புக்கான நடைமுறை"),
                      ("c. பிரிவு 15(1)(b)", "3. அட்வகேட் ஜெனரலின் மனுவின் பேரில் குற்றவியல் அவமதிப்பு"),
                      ("d. பிரிவு 20", "4. அவமதிப்பு நடவடிக்கைகளுக்கான ஒரு வருட கால வரம்பு")],
            "opts": ["a-1, b-2, c-3, d-4", "a-3, b-4, c-1, d-2", "a-2, b-1, c-4, d-3", "a-4, b-2, c-1, d-3"]
        },
        # 87: Removal Authorities
        {
            "sub": "Removal Authorities",
            "t_en": "Match List-I (State Functionaries) with List-II (Removal Authority & Mechanism):",
            "t_ta": "பட்டியல்-I-ஐ (மாநிலப் பதவிகள்) பட்டியல்-II உடன் (நீக்கும் அதிகாரம் & நடைமுறை) பொருத்துக:",
            "l1_en": [("a. Advocate General of the State", "1. Removed by Governor at pleasure without showing cause"),
                      ("b. High Court Judge", "2. Removed by President on address by Parliament with special majority"),
                      ("c. State Election Commissioner", "3. Removed by President in like manner as a High Court Judge"),
                      ("d. Chairman, State PSC", "4. Removed by President on grounds of misbehaviour after SC inquiry")],
            "l1_ta": [("a. மாநில அட்வகேட் ஜெனரல்", "1. காரணம் கூறாமல் ஆளுநரால் விருப்பப்படி நீக்கப்படுகிறார்"),
                      ("b. உயர் நீதிமன்ற நீதிபதி", "2. நாடாளுமன்ற சிறப்பு பெரும்பான்மைத் தீர்மானத்தின் பேரில் குடியரசுத் தலைவரால் நீக்கம்"),
                      ("c. மாநில தேர்தல் ஆணையர்", "3. உயர் நீதிமன்ற நீதிபதி போல குடியரசுத் தலைவரால் நீக்கப்படுகிறார்"),
                      ("d. தலைவர், மாநில TNPSC", "4. உச்ச நீதிமன்ற விசாரணைக்குப் பின் குடியரசுத் தலைவரால் நீக்கப்படுகிறார்")],
            "opts": ["a-1, b-2, c-3, d-4", "a-2, b-1, c-4, d-3", "a-4, b-3, c-2, d-1", "a-3, b-4, c-1, d-2"]
        },
        # 88: Doctrines
        {
            "sub": "Legal Doctrines",
            "t_en": "Match List-I (Legal Doctrines) with List-II (Application to Advocate General):",
            "t_ta": "பட்டியல்-I-ஐ (சட்டக் கோட்பாடுகள்) பட்டியல்-II உடன் (அட்வகேட் ஜெனரலுக்கான பயன்பாடு) பொருத்துக:",
            "l1_en": [("a. Doctrine of Pleasure", "1. Article 165(3) tenure terminable without cause"),
                      ("b. Parens Patriae Jurisdiction", "2. Protective guardian of public charitable trusts under CPC Sec 92"),
                      ("c. Quasi-Judicial Function", "3. Independent screening of criminal contempt consent petitions"),
                      ("d. Parliamentary Immunity", "4. Article 194(2) absolute protection for speeches in legislature")],
            "l1_ta": [("a. விருப்பக் கோட்பாடு", "1. காரணம் கூறாமல் நீக்கப்படக்கூடிய சரத்து 165(3) பதவிக்காலம்"),
                      ("b. Parens Patriae அதிகாரம்", "2. CPC 92-ன் கீழ் பொது அறக்கட்டளைகளின் சட்டப்பூர்வ பாதுகாவலர்"),
                      ("c. Quasi-Judicial பணி", "3. குற்றவியல் அவமதிப்பு மனுக்களை நடுநிலையோடு பரிசீலித்தல்"),
                      ("d. சட்டமன்றப் பாதுகாப்பு", "4. சரத்து 194(2) அவைப் பேச்சுக்களுக்கான முழுமையான பாதுகாப்பு")],
            "opts": ["a-1, b-2, c-3, d-4", "a-3, b-4, c-1, d-2", "a-2, b-1, c-4, d-3", "a-4, b-2, c-1, d-3"]
        },
        # 89: Constitutional Phrases
        {
            "sub": "Constitutional Vocabulary",
            "t_en": "Match List-I (Constitutional Phrases in Article 165/177) with List-II (Specific Meaning):",
            "t_ta": "பட்டியல்-I-ஐ (சரத்து 165/177 சொற்றொடர்கள்) பட்டியல்-II உடன் (குறிப்பிட்ட பொருள்) பொருத்துக:",
            "l1_en": [("a. 'During the pleasure of the Governor'", "1. Tenure without fixed term, terminable at executive will"),
                      ("b. 'Right of audience in all courts'", "2. Right to appear in all courts within the territory of the State"),
                      ("c. 'Without the right to vote'", "3. Article 177 explicit prohibition in Legislative Assembly"),
                      ("d. 'Remuneration as Governor may determine'", "4. Financial compensation not fixed by Legislature Act")],
            "l1_ta": [("a. 'ஆளுநரின் விருப்பம் உள்ளவரை'", "1. நிலையான காலமின்றி நிர்வாக விருப்பப்படி நீக்கப்படக்கூடிய பதவி"),
                      ("b. 'அனைத்து நீதிமன்றங்களிலும் வாதாடும் உரிமை'", "2. மாநில எல்லைக்குள் உள்ள அனைத்து நீதிமன்றங்களிலும் ஆஜராகும் உரிமை"),
                      ("c. 'வாக்களிக்கும் உரிமையின்றி'", "3. சட்டமன்றப் பேரவையில் சரத்து 177 விதிக்கும் வெளிப்படையான தடை"),
                      ("d. 'ஆளுநர் நிர்ணயிக்கும் ஊதியம்'", "4. சட்டமன்ற சட்டத்தால் நிர்ணயிக்கப்படாத நிதி ஊதியம்")],
            "opts": ["a-1, b-2, c-3, d-4", "a-2, b-1, c-4, d-3", "a-4, b-3, c-2, d-1", "a-3, b-4, c-1, d-2"]
        },
        # 90: Historical Milestones
        {
            "sub": "Madras Legal Milestones",
            "t_en": "Match List-I (Milestone Years in Madras Legal History) with List-II (Historic Event):",
            "t_ta": "பட்டியல்-I-ஐ (மெட்ராஸ் சட்ட வரலாற்றின் ஆண்டுகள்) பட்டியல்-II உடன் (வரலாற்று நிகழ்வு) பொருத்துக:",
            "l1_en": [("a. 1801", "1. Supreme Court of Judicature established at Madras"),
                      ("b. 1862", "2. High Court of Madras established under Letters Patent"),
                      ("c. 1935", "3. Section 55 GOI Act created Provincial Advocate-General"),
                      ("d. 1950", "4. Article 165 established Advocate General in Constitution of India")],
            "l1_ta": [("a. 1801", "1. மெட்ராஸில் உச்ச நீதிமன்ற நீதித்துறை அமைப்பு நிறுவப்பட்டது"),
                      ("b. 1862", "2. காப்புரிமை கடிதங்களின் கீழ் மெட்ராஸ் உயர் நீதிமன்றம் நிறுவப்பட்டது"),
                      ("c. 1935", "3. 1935 சட்டம் பிரிவு 55 மாகாண அட்வகேட்-ஜெனரலை உருவாக்கியது"),
                      ("d. 1950", "4. இந்திய அரசியலமைப்பில் சரத்து 165 அட்வகேட் ஜெனரலை நிறுவியது")],
            "opts": ["a-1, b-2, c-3, d-4", "a-3, b-4, c-1, d-2", "a-2, b-1, c-4, d-3", "a-4, b-2, c-1, d-3"]
        }
    ]

    for i, m_item in enumerate(match_gt_data):
        qid = f"ADVG_GT_{76+i:03d}"
        stem_en_lines = [m_item["t_en"], "List-I:"]
        for a, b in m_item["l1_en"]:
            stem_en_lines.append(f"{a}")
        stem_en_lines.append("List-II:")
        for a, b in m_item["l1_en"]:
            stem_en_lines.append(f"{b}")

        stem_ta_lines = [m_item["t_ta"], "பட்டியல்-I:"]
        for a, b in m_item["l1_ta"]:
            stem_ta_lines.append(f"{a}")
        stem_ta_lines.append("பட்டியல்-II:")
        for a, b in m_item["l1_ta"]:
            stem_ta_lines.append(f"{b}")

        stem_en = "\n".join(stem_en_lines)
        stem_ta = "\n".join(stem_ta_lines)

        opts = m_item["opts"]
        correct_key = "A"

        why_en = {
            "A": f"Option A ({opts[0]}) correctly matches all four items in List-I with List-II.",
            "B": f"Option B ({opts[1]}) contains mismatched pairs.",
            "C": f"Option C ({opts[2]}) contains mismatched pairs.",
            "D": f"Option D ({opts[3]}) contains mismatched pairs."
        }
        why_ta = {
            "A": f"தெரிவு A ({opts[0]}) பட்டியல்-I-ல் உள்ள நான்கு கூறுகளையும் பட்டியல்-II உடன் சரியாகப் பொருத்துகிறது.",
            "B": f"தெரிவு B ({opts[1]}) தவறாகப் பொருத்தப்பட்ட இணைகளைக் கொண்டுள்ளது.",
            "C": f"தெரிவு C ({opts[2]}) தவறாகப் பொருத்தப்பட்ட இணைகளைக் கொண்டுள்ளது.",
            "D": f"தெரிவு D ({opts[3]}) தவறாகப் பொருத்தப்பட்ட இணைகளைக் கொண்டுள்ளது."
        }

        q = make_advg_q(
            qid=qid,
            diff="Medium",
            qtype="Match the Following",
            subtopic=m_item["sub"],
            en_stem=stem_en,
            ta_stem=stem_ta,
            en_a=opts[0], ta_a=opts[0],
            en_b=opts[1], ta_b=opts[1],
            en_c=opts[2], ta_c=opts[2],
            en_d=opts[3], ta_d=opts[3],
            correct_key=correct_key,
            exp_en=f"Matching analysis for {m_item['sub']}: Option A provides the accurate pairs.",
            exp_ta=f"{m_item['sub']} பொருத்துதல் விளக்கம்: தெரிவு A சரியான இணைகளை வழங்குகிறது.",
            why_a_en=why_en["A"], why_a_ta=why_ta["A"],
            why_b_en=why_en["B"], why_b_ta=why_ta["B"],
            why_c_en=why_en["C"], why_c_ta=why_ta["C"],
            why_d_en=why_en["D"], why_d_ta=why_ta["D"],
            tip_en=f"Review key pairings in {m_item['sub']}.",
            tip_ta=f"{m_item['sub']} தொடர்பான முக்கிய இணைகளை நினைவில் வையுங்கள்.",
            fact_en=f"Essential matching pairs covering {m_item['sub']}.",
            fact_ta=f"{m_item['sub']} தொடர்பான முக்கிய பொருத்துதல் உண்மைகள்.",
            tags=["polity", "advocate_general", "match_the_following"]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 10 Chronology MCQs (ADVG_GT_091 to ADVG_GT_100)
    # -------------------------------------------------------------

    chron_items = [
        # 91: Madras Legal Foundations
        ("Madras Legal Foundations",
         "Arrange the following historical milestones in the legal history of Madras in chronological order:",
         "மெட்ராஸ் சட்ட வரலாற்றின் பின்வரும் வரலாற்று மைல்கற்களை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
         [("Letters Patent establishing the Supreme Court of Judicature at Madras", "மெட்ராஸ் உச்ச நீதிமன்ற நீதித்துறை அமைப்பை நிறுவிய காப்புரிமை கடிதங்கள்", 1800),
          ("Indian Councils Act granting speaking rights in Governor's Council", "ஆளுநர் கவுன்சிலில் பேசும் உரிமை வழங்கிய இந்திய கவுன்சில்கள் சட்டம்", 1861),
          ("Letters Patent establishing the High Court of Madras", "மெட்ராஸ் உயர் நீதிமன்றத்தை நிறுவிய காப்புரிமை கடிதங்கள்", 1862),
          ("Government of India Act Section 55 establishing Provincial Advocate-General", "மாகாண அட்வகேட்-ஜெனரலை நிறுவிய இந்திய அரசுச் சட்டம் பிரிவு 55", 1935)],
         [3, 1, 4, 2]), # 1862, 1800, 1935, 1861 -> sorted: 1800(2), 1861(4), 1862(1), 1935(3) -> 2 - 4 - 1 - 3

        # 92: Pre-Independence Madras AGs
        ("Pre-Independence Madras AGs",
         "Arrange the following distinguished historic Advocates General of Madras in chronological order of their assumption of office:",
         "மெட்ராஸின் புகழ்பெற்ற வரலாற்று அட்வகேட் ஜெனரல்களை அவர்கள் பதவியேற்ற காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
         [("Sir V. Bhashyam Aiyangar assumed office as first Indian Advocate General", "முதல் இந்திய அட்வகேட் ஜெனரலாக சர் வி. பாஷ்யம் ஐயங்கார் பதவியேற்றல்", 1900),
          ("Sir P.S. Sivaswami Iyer assumed office as Advocate General", "சர் பி.எஸ். சிவசுவாமி ஐயர் அட்வகேட் ஜெனரலாகப் பதவியேற்றல்", 1907),
          ("S. Srinivasa Iyengar assumed office as Advocate General", "எஸ். சீனிவாச ஐயங்கார் அட்வகேட் ஜெனரலாகப் பதவியேற்றல்", 1916),
          ("Sir Alladi Krishnaswamy Iyer assumed office as Advocate General", "சர் அல்லாடி கிருஷ்ணசுவாமி ஐயர் அட்வகேட் ஜெனரலாகப் பதவியேற்றல்", 1929)],
         [4, 1, 3, 2]), # 1929, 1900, 1916, 1907 -> sorted: 1900(2), 1907(4), 1916(3), 1929(1) -> 2 - 4 - 3 - 1

        # 93: Landmark Judicial Decisions
        ("Landmark Judicial Decisions",
         "Arrange the following landmark judicial rulings regarding the Advocate General in chronological order:",
         "அட்வகேட் ஜெனரல் தொடர்பான பின்வரும் முக்கிய நீதிமன்றத் தீர்ப்புகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
         [("Nagpur High Court ruling in G.D. Karkare v. T.L. Shevde", "ஜி.டி. கார்கரே வழக்கில் நாக்பூர் உயர் நீதிமன்றத் தீர்ப்பு", 1952),
          ("Supreme Court judgment in Atlas Cycle Industries v. Their Workmen", "அட்லஸ் சைக்கிள் இன்டஸ்ட்ரீஸ் வழக்கில் உச்ச நீதிமன்றத் தீர்ப்பு", 1962),
          ("Supreme Court ruling in P.N. Duda v. P. Shiv Shanker", "பி.என். தூடா வழக்கில் உச்ச நீதிமன்றத் தீர்ப்பு", 1988),
          ("Supreme Court ruling in M.T. Khan v. Govt. of A.P.", "எம்.டி. கான் வழக்கில் உச்ச நீதிமன்றத் தீர்ப்பு", 2004)],
         [2, 4, 1, 3]), # 1962, 2004, 1952, 1988 -> sorted: 1952(3), 1962(1), 1988(4), 2004(2) -> 3 - 1 - 4 - 2

        # 94: Key Statutory Enactments
        ("Key Statutory Enactments",
         "Arrange the following legislative enactments impacting state law officers in chronological order:",
         "மாநில சட்ட அதிகாரிகளைப் பாதிக்கும் பின்வரும் சட்டங்களை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
         [("Enactment of the Code of Civil Procedure (Sections 91 and 92)", "உரிமையியல் நடைமுறைச் சட்டம் இயற்றப்படுதல் (பிரிவுகள் 91 மற்றும் 92)", 1908),
          ("Enactment of the Advocates Act (Section 23 Pre-audience)", "வழக்கறிஞர்கள் சட்டம் இயற்றப்படுதல் (பிரிவு 23 முதன்மை வாதாடல்)", 1961),
          ("Enactment of the Contempt of Courts Act (Section 15 Consent)", "நீதிமன்ற அவமதிப்புச் சட்டம் இயற்றப்படுதல் (பிரிவு 15 ஒப்புதல்)", 1971),
          ("Enactment of the Code of Criminal Procedure (Sections 301 and 321)", "குற்றவியல் நடைமுறைச் சட்டம் இயற்றப்படுதல் (பிரிவுகள் 301 மற்றும் 321)", 1973)],
         [3, 1, 4, 2]), # 1971, 1908, 1973, 1961 -> sorted: 1908(2), 1961(4), 1971(1), 1973(3) -> 2 - 4 - 1 - 3

        # 95: Constitutional Amendments
        ("Constitutional Amendments",
         "Arrange the following constitutional amendments affecting State executives and courts in chronological order:",
         "மாநில நிர்வாகம் மற்றும் நீதிமன்றங்களைப் பாதித்த பின்வரும் அரசியலமைப்புத் திருத்தங்களை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
         [("7th Constitutional Amendment Act reorganizing States", "மாநிலங்களை மறுசீரமைத்த 7-வது அரசியலமைப்புத் திருத்தச் சட்டம்", 1956),
          ("42nd Constitutional Amendment Act modifying administrative provisions", "நிர்வாக விதிகளை மாற்றிய 42-வது அரசியலமைப்புத் திருத்தச் சட்டம்", 1976),
          ("44th Constitutional Amendment Act restoring constitutional balances", "அரசியலமைப்பு சமநிலையை மீட்டெடுத்த 44-வது அரசியலமைப்புத் திருத்தச் சட்டம்", 1978),
          ("State Law Officers Rules promulgated across Indian States", "மாநில சட்ட அதிகாரிகள் பணி விதிகள் அறிவிக்கப்படுதல்", 1987)],
         [4, 2, 1, 3]), # 1987, 1976, 1956, 1978 -> sorted: 1956(3), 1976(2), 1978(4), 1987(1) -> 3 - 2 - 4 - 1

        # 96: Fiduciary Jurisprudence
        ("Fiduciary Jurisprudence",
         "Arrange the following landmark judgments regarding state public offices in chronological order:",
         "மாநில பொது அலுவலகங்கள் தொடர்பான பின்வரும் வரலாற்றுத் தீர்ப்புகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
         [("Supreme Court ruling in P.N. Duda v. P. Shiv Shanker", "பி.என். தூடா வழக்கில் உச்ச நீதிமன்றத் தீர்ப்பு", 1988),
          ("Supreme Court ruling in Kumari Shrilekha Vidyarthi v. State of UP", "குமாரி ஸ்ரீலேகா வித்யார்த்தி வழக்கில் உச்ச நீதிமன்றத் தீர்ப்பு", 1991),
          ("Supreme Court ruling in State of UP v. UP Law Officers Association", "உ.பி. சட்ட அதிகாரிகள் சங்க வழக்கில் உச்ச நீதிமன்றத் தீர்ப்பு", 1994),
          ("Supreme Court Constitution Bench ruling in B.P. Singhal v. Union of India", "பி.பி. சிங்கால் வழக்கில் அரசியலமைப்பு அமர்வுத் தீர்ப்பு", 2010)],
         [3, 4, 1, 2]), # 1994, 2010, 1988, 1991 -> sorted: 1988(3), 1991(4), 1994(1), 2010(2) -> 3 - 4 - 1 - 2

        # 97: Post-Independence Milestones
        ("Post-Independence Milestones",
         "Arrange the following milestones in Indian legal and constitutional history in chronological order:",
         "இந்திய சட்ட மற்றும் அரசியலமைப்பு வரலாற்றின் பின்வரும் மைல்கற்களை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
         [("Enforcement of Article 165 in the Constitution of India", "இந்திய அரசியலமைப்பில் சரத்து 165 நடைமுறைக்கு வருதல்", 1950),
          ("Establishment of the First Law Commission of Independent India", "சுதந்திர இந்தியாவின் முதலாவது சட்ட ஆணையம் அமைக்கப்படுதல்", 1955),
          ("Enactment of the Advocates Act creating unified Indian Bar", "ஒருங்கிணைந்த இந்திய பார் கவுன்சிலை உருவாக்கிய வழக்கறிஞர்கள் சட்டம்", 1961),
          ("Enactment of the Contempt of Courts Act requiring AG consent", "AG ஒப்புதலைக் கட்டாயமாக்கிய நீதிமன்ற அவமதிப்புச் சட்டம்", 1971)],
         [4, 1, 3, 2]), # 1971, 1950, 1961, 1955 -> sorted: 1950(2), 1955(4), 1961(3), 1971(1) -> 2 - 4 - 3 - 1

        # 98: Chartered Eras of Madras
        ("Chartered Eras of Madras",
         "Arrange the following statutory and constitutional charters of the Madras judiciary in chronological order:",
         "மெட்ராஸ் நீதித்துறையின் பின்வரும் சாசனங்களை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
         [("Charter establishing Supreme Court of Judicature at Madras", "மெட்ராஸ் உச்ச நீதிமன்றத்தை நிறுவிய அரச சாசனம்", 1801),
          ("Letters Patent establishing High Court of Judicature at Madras", "மெட்ராஸ் உயர் நீதிமன்றத்தை நிறுவிய காப்புரிமை கடிதங்கள்", 1862),
          ("Indian Bar Councils Act recognizing leadership of Advocate General", "அட்வகேட் ஜெனரலின் தலைமைத்துவத்தை அங்கீகரித்த இந்திய பார் கவுன்சில்கள் சட்டம்", 1926),
          ("Constitution of India conferring constitutional status on Advocate General", "அட்வகேட் ஜெனரலுக்கு அரசியலமைப்பு அந்தஸ்து வழங்கிய இந்திய அரசியலமைப்பு", 1950)],
         [2, 4, 1, 3]), # 1862, 1950, 1801, 1926 -> sorted: 1801(3), 1862(1), 1926(4), 1950(2) -> 3 - 1 - 4 - 2

        # 99: Procedural Milestones
        ("Procedural Milestones",
         "Arrange the following procedural and contempt milestones in chronological order:",
         "பின்வரும் நடைமுறை மற்றும் அவமதிப்பு மைல்கற்களை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
         [("Contempt of Courts Act enacted with Section 15 consent provisions", "பிரிவு 15 ஒப்புதல் விதிகளுடன் நீதிமன்ற அவமதிப்புச் சட்டம் இயற்றப்படுதல்", 1971),
          ("Code of Criminal Procedure enacted with Section 301 law officer provisions", "பிரிவு 301 சட்ட அதிகாரி விதிகளுடன் குற்றவியல் நடைமுறைச் சட்டம் இயற்றப்படுதல்", 1973),
          ("Code of Civil Procedure amended modifying Sections 91 and 92", "பிரிவுகள் 91 மற்றும் 92-ஐ திருத்திய உரிமையியல் நடைமுறைச் சட்ட திருத்தம்", 1976),
          ("Supreme Court verdict in Pallav Sheth v. Custodian on Section 20 limitation", "பிரிவு 20 கால வரம்பு தொடர்பான பல்லவ் ஷேத் உச்ச நீதிமன்றத் தீர்ப்பு", 2001)],
         [3, 1, 4, 2]), # 1976, 1971, 2001, 1973 -> sorted: 1971(2), 1973(4), 1976(1), 2001(3) -> 2 - 4 - 1 - 3

        # 100: Supreme Court Doctrines on State Executive
        ("Supreme Court Doctrines on State Executive",
         "Arrange the following landmark Supreme Court rulings on State executive power in chronological order:",
         "மாநில நிர்வாக அதிகாரம் தொடர்பான பின்வரும் வரலாற்று உச்ச நீதிமன்றத் தீர்ப்புகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
         [("Nagpur High Court doctrine in G.D. Karkare (affirmed by SC)", "கார்கரே வழக்கில் வகுக்கப்பட்ட கோட்பாடு", 1952),
          ("Kesavananda Bharati verdict establishing Basic Structure Doctrine", "அடிப்படை கட்டமைப்பு கோட்பாட்டை நிறுவிய கேசவானந்த பாரதி தீர்ப்பு", 1973),
          ("S.R. Bommai v. Union of India limiting Article 356 dismissals", "சரத்து 356 நீக்கங்களைக் கட்டுப்படுத்திய எஸ்.ஆர். பொம்மை தீர்ப்பு", 1994),
          ("B.P. Singhal v. Union of India defining limits of Doctrine of Pleasure", "விருப்பக் கோட்பாட்டின் வரம்புகளை வரையறுத்த பி.பி. சிங்கால் தீர்ப்பு", 2010)],
         [4, 1, 3, 2]) # 2010, 1952, 1994, 1973 -> sorted: 1952(2), 1973(4), 1994(3), 2010(1) -> 2 - 4 - 3 - 1
    ]

    all_perms = [
        [1, 2, 3, 4], [1, 2, 4, 3], [1, 3, 2, 4], [1, 3, 4, 2], [1, 4, 2, 3], [1, 4, 3, 2],
        [2, 1, 3, 4], [2, 1, 4, 3], [2, 3, 1, 4], [2, 3, 4, 1], [2, 4, 1, 3], [2, 4, 3, 1],
        [3, 1, 2, 4], [3, 1, 4, 2], [3, 2, 1, 4], [3, 2, 4, 1], [3, 4, 1, 2], [3, 4, 2, 1],
        [4, 1, 2, 3], [4, 1, 3, 2], [4, 2, 1, 3], [4, 2, 3, 1], [4, 3, 1, 2], [4, 3, 2, 1]
    ]

    for i, c_item in enumerate(chron_items):
        qid = f"ADVG_GT_{91+i:03d}"
        subtopic, t_en, t_ta, events, s_order = c_item

        presented_en = []
        presented_ta = []
        presented_meta = []

        for p_idx, orig_1_idx in enumerate(s_order):
            orig_0_idx = orig_1_idx - 1
            lbl_en, lbl_ta, yr = events[orig_0_idx]
            presented_en.append(f"{p_idx + 1}. {lbl_en}")
            presented_ta.append(f"{p_idx + 1}. {lbl_ta}")
            presented_meta.append((p_idx + 1, orig_0_idx, lbl_en, lbl_ta, yr))

        stem_en = f"{t_en}\n" + "\n".join(presented_en)
        stem_ta = f"{t_ta}\n" + "\n".join(presented_ta)

        sorted_meta = sorted(presented_meta, key=lambda x: (x[4], x[1]))
        correct_seq = [x[0] for x in sorted_meta]

        assert correct_seq != [1, 2, 3, 4], f"Chronology already in order in {qid}!"

        # Distractors
        filtered = [p for p in all_perms if p != correct_seq and p != [1, 2, 3, 4]]
        random.seed(200 + i)
        random.shuffle(filtered)
        opts_perms = [correct_seq] + filtered[:3]

        en_options = [" - ".join(str(d) for d in p) for p in opts_perms]
        ta_options = [" - ".join(str(d) for d in p) for p in opts_perms]

        exp_lines_en = [
            f"The correct chronological order is: {' -> '.join(str(d) for d in correct_seq)}.",
            "Progression of events with years:"
        ]
        exp_lines_ta = [
            f"சரியான காலவரிசை ஒழுங்கு: {' -> '.join(str(d) for d in correct_seq)}.",
            "நிகழ்வுகளின் காலவரிசை:"
        ]
        for m in sorted_meta:
            exp_lines_en.append(f"- Event {m[0]}: {m[2]} ({m[4]})")
            exp_lines_ta.append(f"- நிகழ்வு {m[0]}: {m[3]} ({m[4]})")

        exp_en = "\n".join(exp_lines_en)
        exp_ta = "\n".join(exp_lines_ta)

        why_en = {
            "A": f"Option A ({en_options[0]}) correctly identifies the historical timeline: {' -> '.join(str(d) for d in correct_seq)}.",
            "B": f"Option B ({en_options[1]}) is incorrect because the chronological sequence is misordered.",
            "C": f"Option C ({en_options[2]}) is incorrect because the events are out of order.",
            "D": f"Option D ({en_options[3]}) is incorrect because the sequence of events is inverted."
        }
        why_ta = {
            "A": f"தெரிவு A ({ta_options[0]}) வரலாற்று காலவரிசையைச் சரியாகக் காட்டுகிறது: {' -> '.join(str(d) for d in correct_seq)}.",
            "B": f"தெரிவு B ({ta_options[1]}) தவறானது ஏனெனில் நிகழ்வுகளின் வரிசை மாறியுள்ளது.",
            "C": f"தெரிவு C ({ta_options[2]}) தவறானது ஏனெனில் நிகழ்வுகள் காலவரிசையில் இல்லை.",
            "D": f"தெரிவு D ({ta_options[3]}) தவறானது ஏனெனில் நிகழ்வுகளின் வரிசை முரணாக உள்ளது."
        }

        q = make_advg_q(
            qid=qid,
            diff="Hard",
            qtype="Chronology",
            subtopic=subtopic,
            en_stem=stem_en,
            ta_stem=stem_ta,
            en_a=en_options[0], ta_a=ta_options[0],
            en_b=en_options[1], ta_b=ta_options[1],
            en_c=en_options[2], ta_c=ta_options[2],
            en_d=en_options[3], ta_d=ta_options[3],
            correct_key="A",
            exp_en=exp_en,
            exp_ta=exp_ta,
            why_a_en=why_en["A"], why_a_ta=why_ta["A"],
            why_b_en=why_en["B"], why_b_ta=why_ta["B"],
            why_c_en=why_en["C"], why_c_ta=why_ta["C"],
            why_d_en=why_en["D"], why_d_ta=why_ta["D"],
            tip_en=f"Note key historical milestone years for {subtopic}.",
            tip_ta=f"{subtopic} தொடர்பான முக்கிய வரலாற்று மைல்கல் ஆண்டுகளைக் கவனத்தில் வையுங்கள்.",
            fact_en=f"Chronological sequence for {subtopic}.",
            fact_ta=f"{subtopic} தொடர்பான வரலாற்று நிகழ்வுகளின் காலவரிசை.",
            tags=["polity", "advocate_general", "chronology"]
        )
        questions.append(q)

    return questions
