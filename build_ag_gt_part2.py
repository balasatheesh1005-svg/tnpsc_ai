# -*- coding: utf-8 -*-
"""
Grand Test Part 2 for Attorney General of India (50 Questions: AG_GT_051 to AG_GT_100).
- 10 Statement-based MCQs (AG_GT_051 to AG_GT_060)
- 15 Assertion-Reason MCQs (AG_GT_061 to AG_GT_075)
- 15 Match the Following MCQs (AG_GT_076 to AG_GT_090)
- 10 Chronology MCQs (AG_GT_091 to AG_GT_100)
Strictly avoids collision with the 325 Core questions.
"""

from ag_mcq_helper import make_ag_q
import random

def get_gt_part2_questions():
    questions = []

    # -------------------------------------------------------------
    # 10 Statement-based MCQs (AG_GT_051 to AG_GT_060)
    # -------------------------------------------------------------

    # 51
    questions.append(make_ag_q(
        qid="AG_GT_051",
        diff="Medium",
        qtype="Statement Based",
        subtopic="Constitutional Comparison",
        en_stem="Consider the following statements regarding the Union Council of Ministers and the Attorney General of India:\n1. The Council of Ministers advises the President on political and executive policy.\n2. The Attorney General advises the Government of India on legal and constitutional matters.\n3. The Attorney General is collective responsible to the Lok Sabha along with the Council of Ministers.\nWhich of the statements given above are correct?",
        ta_stem="மத்திய அமைச்சரவை மற்றும் இந்திய தலைமை வழக்கறிஞர் குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. அமைச்சரவை அரசியல் மற்றும் நிர்வாகக் கொள்கைகளில் குடியரசுத் தலைவருக்கு ஆலோசிக்கிறது.\n2. தலைமை வழக்கறிஞர் சட்ட மற்றும் அரசியலமைப்பு விவகாரங்களில் இந்திய அரசுக்கு ஆலோசிக்கிறார்.\n3. அமைச்சரவையுடன் சேர்ந்து தலைமை வழக்கறிஞரும் மக்களவைக்குக் கூட்டுப் பொறுப்புடையவர் ஆவார்.\nமேற்கூறிய கூற்றுகளில் சரியானவை எவை?",
        en_a="1 and 2 only", ta_a="1 மற்றும் 2 மட்டுமே",
        en_b="2 and 3 only", ta_b="2 மற்றும் 3 மட்டுமே",
        en_c="1 and 3 only", ta_c="1 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3", ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statements 1 and 2 are correct. Statement 3 is incorrect because under Article 75(3), only the Council of Ministers is collectively responsible to the House of the People; the AG is an independent non-member officer not subject to collective ministerial responsibility.",
        exp_ta="கூற்றுகள் 1 மற்றும் 2 சரியானவை. சரத்து 75(3)-ன் கீழ் அமைச்சரவை மட்டுமே மக்களவைக்குக் கூட்டுப் பொறுப்புடையது; AG ஓர் அமைச்சரவை உறுப்பினர் அல்ல என்பதால் கூட்டுப் பொறுப்பு இவருக்குப் பொருந்தாது; எனவே கூற்று 3 தவறு.",
        why_a_en="Option A is correct: Statements 1 and 2 are true; AG is not collectively responsible to Lok Sabha.",
        why_a_ta="தெரிவு A சரி: கூற்றுகள் 1 மற்றும் 2 சரி; AG மக்களவைக்குக் கூட்டுப் பொறுப்புடையவர் அல்ல.",
        why_b_en="Option B is incorrect: Statement 3 is false.",
        why_b_ta="தெரிவு B தவறு: கூற்று 3 தவறானது.",
        why_c_en="Option C is incorrect.", why_c_ta="தெரிவு C தவறானது.",
        why_d_en="Option D is incorrect.", why_d_ta="தெரிவு D தவறானது.",
        tip_en="Collective responsibility under Article 75(3) applies ONLY to Ministers, NOT to the Attorney General.",
        tip_ta="சரத்து 75(3)-ன் கூட்டுப் பொறுப்பு அமைச்சர்களுக்கு மட்டுமே உரியது, தலைமை வழக்கறிஞருக்கு அல்ல.",
        fact_en="The Attorney General is accountable directly to the President and the Constitution.",
        fact_ta="தலைமை வழக்கறிஞர் நேரடியாக குடியரசுத் தலைவருக்கும் அரசியலமைப்பிற்கும் பொறுப்புடையவர்.",
        tags=["polity", "attorney_general", "collective_responsibility"]
    ))

    # 52
    questions.append(make_ag_q(
        qid="AG_GT_052",
        diff="Hard",
        qtype="Statement Based",
        subtopic="Constitutional Immunity",
        en_stem="Consider the following statements regarding the Attorney General's legal standing in international arbitration:\n1. The Attorney General can lead India's legal representation before international commercial arbitral tribunals.\n2. The Attorney General can enter into international sovereign treaties on behalf of India without cabinet authorization.\n3. Sovereign treaty ratification power is an executive prerogative exercised under Article 73.\nWhich of the statements given above are correct?",
        ta_stem="சர்வதேச நடுவர் தீர்ப்பாயங்களில் தலைமை வழக்கறிஞரின் சட்டப்பூர்வ நிலை குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. சர்வதேச வணிக நடுவர் தீர்ப்பாயங்களில் இந்தியாவின் சட்டப் பிரதிநிதித்துவத்தை தலைமை வழக்கறிஞர் வழிநடத்த முடியும்.\n2. அமைச்சரவை ஒப்புதல் இன்றியே இந்தியாவின் சார்பில் சர்வதேச இறையாண்மை உடன்படிக்கைகளை தலைமை வழக்கறிஞரால் கையெழுத்திட முடியும்.\n3. சர்வதேச உடன்படிக்கைகளை அங்கீகரிக்கும் அதிகாரம் சரத்து 73-ன் கீழ் செயல்படுத்தப்படும் ஓர் நிர்வாக அதிகாரமாகும்.\nமேற்கூறிய கூற்றுகளில் சரியானவை எவை?",
        en_a="1 and 3 only", ta_a="1 மற்றும் 3 மட்டுமே",
        en_b="1 and 2 only", ta_b="1 மற்றும் 2 மட்டுமே",
        en_c="2 and 3 only", ta_c="2 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3", ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statements 1 and 3 are correct. Statement 2 is incorrect because treaty-making is an exclusive sovereign power of the Union Executive requiring Cabinet approval and diplomatic credentials; the AG has no independent power to bind India in treaties.",
        exp_ta="கூற்றுகள் 1 மற்றும் 3 சரியானவை. சர்வதேச உடன்படிக்கைகளை மேற்கொள்வது மத்திய அமைச்சரவையின் நிர்வாக அதிகாரம்; AG தன்னிச்சையாக உடன்படிக்கைகளில் கையெழுத்திட முடியாது என்பதால் கூற்று 2 தவறு.",
        why_a_en="Option A is correct: Statements 1 and 3 are constitutionally valid.",
        why_a_ta="தெரிவு A சரி: கூற்றுகள் 1 மற்றும் 3 அரசியலமைப்பு ரீதியாக சரியானவை.",
        why_b_en="Option B is incorrect: Statement 2 is false.",
        why_b_ta="தெரிவு B தவறு: கூற்று 2 தவறானது.",
        why_c_en="Option C is incorrect.", why_c_ta="தெரிவு C தவறானது.",
        why_d_en="Option D is incorrect.", why_d_ta="தெரிவு D தவறானது.",
        tip_en="Treaty making is an executive function of the Union under Article 73 and Entry 14 List I.",
        tip_ta="உடன்படிக்கை மேற்கொள்ளும் அதிகாரம் சரத்து 73 மற்றும் பட்டியல் I பிரிவு 14-ன் கீழ் மத்திய அரசின் நிர்வாகப் பணியாகும்.",
        fact_en="The Attorney General provides legal counsel on the constitutional implications of international treaties.",
        fact_ta="சர்வதேச உடன்படிக்கைகளின் அரசியலமைப்பு தாக்கங்கள் குறித்து தலைமை வழக்கறிஞர் சட்ட ஆலோசனை வழங்குகிறார்.",
        tags=["polity", "attorney_general", "international_law"]
    ))

    # 53
    questions.append(make_ag_q(
        qid="AG_GT_053",
        diff="Medium",
        qtype="Statement Based",
        subtopic="Parliamentary Debates",
        en_stem="Consider the following statements regarding the Attorney General addressing Parliament on a Constitutional Amendment Bill:\n1. The Attorney General can address the Lok Sabha explaining the legal intricacies of the proposed amendment.\n2. The Attorney General can respond to constitutional questions raised by Members of Parliament.\n3. The Attorney General can move official amendments to the clauses of the Bill on the floor of the House.\nWhich of the statements given above are correct?",
        ta_stem="அரசியலமைப்பு திருத்த மசோதா குறித்து நாடாளுமன்றத்தில் தலைமை வழக்கறிஞர் உரையாற்றுவது தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. உத்தேச திருத்தத்தின் சட்ட நுணுக்கங்களை விளக்கி மக்களவையில் தலைமை வழக்கறிஞர் உரையாற்ற முடியும்.\n2. நாடாளுமன்ற உறுப்பினர்கள் எழுப்பும் அரசியலமைப்பு ரீதியான கேள்விகளுக்கு தலைமை வழக்கறிஞர் பதிலளிக்க முடியும்.\n3. அவையில் மசோதாவின் பிரிவுகள் மீது அதிகாரப்பூர்வ திருத்தங்களை தலைமை வழக்கறிஞரால் கொண்டுவர முடியும்.\nமேற்கூறிய கூற்றுகளில் சரியானவை எவை?",
        en_a="1 and 2 only", ta_a="1 மற்றும் 2 மட்டுமே",
        en_b="2 and 3 only", ta_b="2 மற்றும் 3 மட்டுமே",
        en_c="1 and 3 only", ta_c="1 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3", ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statements 1 and 2 are correct. Statement 3 is incorrect because only Members of Parliament can move amendments to bills under the Rules of Procedure; non-members (including the AG) cannot move legislative motions or amendments.",
        exp_ta="கூற்றுகள் 1 மற்றும் 2 சரியானவை. நாடாளுமன்ற நடைமுறை விதிகளின்படி எம்பிக்கள் மட்டுமே திருத்தங்களை முன்மொழிய முடியும்; உறுப்பினரல்லாத AG திருத்தங்களை முன்மொழிய முடியாது என்பதால் கூற்று 3 தவறு.",
        why_a_en="Option A is correct: AG can speak and answer questions, but cannot move legislative amendments.",
        why_a_ta="தெரிவு A சரி: AG பேசலாம், கேள்விகளுக்குப் பதிலளிக்கலாம்; ஆனால் திருத்தங்களை முன்மொழிய முடியாது.",
        why_b_en="Option B is incorrect: Statement 3 is false.",
        why_b_ta="தெரிவு B தவறு: கூற்று 3 தவறானது.",
        why_c_en="Option C is incorrect.", why_c_ta="தெரிவு C தவறானது.",
        why_d_en="Option D is incorrect.", why_d_ta="தெரிவு D தவறானது.",
        tip_en="AG can speak and clarify law in Parliament, but CANNOT move motions or vote on bills.",
        tip_ta="AG நாடாளுமன்றத்தில் சட்டத்தை விளக்கலாம்; ஆனால் பிரேரணைகளை முன்மொழியவோ வாக்களிக்கவோ முடியாது.",
        fact_en="Attorney General Daphtary addressed the Lok Sabha in 1963 clarifying the Official Languages Bill.",
        fact_ta="1963-ல் அலுவல் மொழிகள் மசோதா குறித்து தலைமை வழக்கறிஞர் தப்தாரி மக்களவையில் விளக்கமளித்தார்.",
        tags=["polity", "attorney_general", "legislative_procedure"]
    ))

    # 54
    questions.append(make_ag_q(
        qid="AG_GT_054",
        diff="Hard",
        qtype="Statement Based",
        subtopic="Federal Jurisprudence",
        en_stem="Consider the following statements regarding the Attorney General and Centre-State water dispute tribunals:\n1. Under Article 262, the jurisdiction of all courts, including the Supreme Court, can be barred in inter-state river disputes.\n2. The Attorney General represents the Union Ministry of Jal Shakti before the tribunal.\n3. The Attorney General's legal advice binds the Inter-State River Water Disputes Tribunal.\nWhich of the statements given above is/are correct?",
        ta_stem="மத்திய-மாநில நதிநீர் தகராறு தீர்ப்பாயங்கள் மற்றும் தலைமை வழக்கறிஞர் குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. சரத்து 262-ன் கீழ் மாநிலங்களுக்கு இடையேயான நதிநீர் தகராறுகளில் உச்ச நீதிமன்றம் உள்ளிட்ட அனைத்து நீதிமன்றங்களின் அதிகார வரம்பையும் தடை செய்ய முடியும்.\n2. நதிநீர் தீர்ப்பாயத்தின் முன் மத்திய ஜல் சக்தி அமைச்சகத்தின் சார்பில் தலைமை வழக்கறிஞர் ஆஜராகிறார்.\n3. தலைமை வழக்கறிஞரின் சட்ட ஆலோசனை நதிநீர் தகராறு தீர்ப்பாயத்தைக் கட்டுப்படுத்தும்.\nமேற்கூறிய கூற்றுகளில் சரியானது/சரியானவை எது/எவை?",
        en_a="1 and 2 only", ta_a="1 மற்றும் 2 மட்டுமே",
        en_b="1 only", ta_b="1 மட்டுமே",
        en_c="2 and 3 only", ta_c="2 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3", ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statements 1 and 2 are correct. Statement 3 is incorrect because water dispute tribunals are independent quasi-judicial adjudicatory bodies whose decisions are not bound by the opinion of the Union's counsel.",
        exp_ta="கூற்றுகள் 1 மற்றும் 2 சரியானவை. நதிநீர் தீர்ப்பாயங்கள் தன்னாட்சி பெற்ற அரை-நீதிமன்ற அமைப்புகள்; அரசு வழக்கறிஞரான AG-யின் ஆலோசனை தீர்ப்பாயத்தைக் கட்டுப்படுத்தாது என்பதால் கூற்று 3 தவறு.",
        why_a_en="Option A is correct: Tribunals are independent adjudicators, not bound by AG opinion.",
        why_a_ta="தெரிவு A சரி: தீர்ப்பாயங்கள் தன்னாட்சி அமைப்புகள், AG ஆலோசனை அவற்றைக் கட்டுப்படுத்தாது.",
        why_b_en="Option B is incorrect: Statement 2 is also correct.",
        why_b_ta="தெரிவு B தவறு: கூற்று 2-ம் சரியானது.",
        why_c_en="Option C is incorrect.", why_c_ta="தெரிவு C தவறானது.",
        why_d_en="Option D is incorrect.", why_d_ta="தெரிவு D தவறானது.",
        tip_en="Article 262 excludes court jurisdiction in inter-state river disputes; AG represents Union interests before tribunals.",
        tip_ta="சரத்து 262 நதிநீர் தகராறுகளில் நீதிமன்ற வரம்பைத் தடுக்கிறது; தீர்ப்பாயங்களில் மத்திய அரசுக்காக AG ஆஜராகிறார்.",
        fact_en="The Inter-State River Water Disputes Act, 1956 implements Article 262.",
        fact_ta="1956 மாநிலங்களுக்கு இடையேயான நதிநீர் தகராறுகள் சட்டம் சரத்து 262-ஐ நடைமுறைப்படுத்துகிறது.",
        tags=["polity", "attorney_general", "water_tribunals"]
    ))

    # 55
    questions.append(make_ag_q(
        qid="AG_GT_055",
        diff="Medium",
        qtype="Statement Based",
        subtopic="Constitutional Comparison",
        en_stem="Consider the following statements regarding the Attorney General of India and the Advocate General of a State:\n1. Both hold office during the pleasure of their respective appointing authorities.\n2. Both can be removed by impeachment in Parliament.\n3. Both must be citizens of India.\nWhich of the statements given above are correct?",
        ta_stem="இந்திய தலைமை வழக்கறிஞர் மற்றும் மாநில அட்வகேட் ஜெனரல் குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இருவருமே தங்களை நியமிக்கும் அதிகார அமைப்பின் விருப்பம் உள்ளவரை பதவியில் நீடிக்கின்றனர்.\n2. இருவருமே நாடாளுமன்றத்தில் சிறப்புத் தீர்மானம் (impeachment) மூலம் நீக்கப்படலாம்.\n3. இருவருமே இந்தியக் குடிமக்களாக இருக்க வேண்டும்.\nமேற்கூறிய கூற்றுகளில் சரியானவை எவை?",
        en_a="1 and 3 only", ta_a="1 மற்றும் 3 மட்டுமே",
        en_b="1 and 2 only", ta_b="1 மற்றும் 2 மட்டுமே",
        en_c="2 and 3 only", ta_c="2 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3", ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statements 1 and 3 are correct. Statement 2 is incorrect because neither the AG nor the Advocate General is removed by impeachment; both serve at pleasure (President's pleasure for AG, Governor's pleasure for Advocate General).",
        exp_ta="கூற்றுகள் 1 மற்றும் 3 சரியானவை. AG அல்லது அட்வகேட் ஜெனரல் எவருக்குமே பதவி நீக்கத் தீர்மானம் (impeachment) கிடையாது; இருவருமே விருப்பக் கோட்பாட்டின் கீழ் செயல்படுவதால் கூற்று 2 தவறு.",
        why_a_en="Option A is correct: Statements 1 and 3 are true; neither is removed by impeachment.",
        why_a_ta="தெரிவு A சரி: கூற்றுகள் 1 மற்றும் 3 சரி; எவருக்கும் பதவி நீக்கத் தீர்மானம் கிடையாது.",
        why_b_en="Option B is incorrect: Statement 2 is false.",
        why_b_ta="தெரிவு B தவறு: கூற்று 2 தவறானது.",
        why_c_en="Option C is incorrect.", why_c_ta="தெரிவு C தவறானது.",
        why_d_en="Option D is incorrect.", why_d_ta="தெரிவு D தவறானது.",
        tip_en="Neither AG nor Advocate General has an impeachment procedure; both serve strictly at pleasure.",
        tip_ta="AG அல்லது அட்வகேட் ஜெனரலுக்கு பதவி நீக்க நடைமுறை இல்லை; இருவரும் விருப்பப்படி பதவி வகிக்கின்றனர்.",
        fact_en="Impeachment is reserved for the President, Judges of SC/HC, CAG, and CEC.",
        fact_ta="குடியரசுத் தலைவர், நீதிபதிகள், சிஏஜி மற்றும் சிஇசி ஆகியோருக்கு மட்டுமே நாடாளுமன்ற நீக்க நடைமுறை உண்டு.",
        tags=["polity", "attorney_general", "removal_comparison"]
    ))

    # 56
    questions.append(make_ag_q(
        qid="AG_GT_056",
        diff="Hard",
        qtype="Statement Based",
        subtopic="Election Law & RPA 1951",
        en_stem="Consider the following statements regarding the Attorney General and the Representation of the People Act, 1951:\n1. The Attorney General defends the constitutional validity of provisions of the RPA 1951 when challenged in Supreme Court.\n2. The Attorney General is an ex-officio member of the Election Commission of India.\n3. The Attorney General can appear as private counsel for a candidate in an election petition challenging an MP's election without government permission.\nWhich of the statements given above is/are correct?",
        ta_stem="மக்கள் பிரதிநிதித்துவச் சட்டம், 1951 மற்றும் தலைமை வழக்கறிஞர் குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. உச்ச நீதிமன்றத்தில் மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவுகள் சவாலுக்கு வரும் போது அதன் அரசியலமைப்புச் செல்லுபடியை AG ஆதரித்து வாதிடுகிறார்.\n2. இந்தியத் தேர்தல் ஆணையத்தின் பதவி வழி உறுப்பினர் தலைமை வழக்கறிஞர் ஆவார்.\n3. எம்பி தேர்தல் தொடர்பான வழக்கில் ஒரு வேட்பாளருக்கான தனியார் வழக்கறிஞராக அரசின் அனுமதியின்றி AG ஆஜராக முடியும்.\nமேற்கூறிய கூற்றுகளில் சரியானது/சரியானவை எது/எவை?",
        en_a="1 only", ta_a="1 மட்டுமே",
        en_b="1 and 2 only", ta_b="1 மற்றும் 2 மட்டுமே",
        en_c="1 and 3 only", ta_c="1 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3", ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statement 1 is correct. Statement 2 is incorrect because the ECI consists solely of the CEC and ECs under Article 324. Statement 3 is incorrect because election petitions against MPs often involve governmental authorities, creating conflicts of interest requiring clearance.",
        exp_ta="கூற்று 1 மட்டுமே சரியானது. சரத்து 324-ன் கீழ் தேர்தல் ஆணையத்தில் தேர்தல் ஆணையர்கள் மட்டுமே உள்ளனர் (AG உறுப்பினர் அல்ல) என்பதால் கூற்று 2 தவறு. தேர்தல் வழக்குகளில் அரசின் அனுமதி இன்றி ஆஜராக முடியாது என்பதால் கூற்று 3 தவறு.",
        why_a_en="Option A is correct: Only Statement 1 is constitutionally accurate.",
        why_a_ta="தெரிவு A சரி: கூற்று 1 மட்டுமே அரசியலமைப்பு ரீதியாக சரியானது.",
        why_b_en="Option B is incorrect: Statement 2 is false.",
        why_b_ta="தெரிவு B தவறு: கூற்று 2 தவறானது.",
        why_c_en="Option C is incorrect: Statement 3 is false.",
        why_c_ta="தெரிவு C தவறு: கூற்று 3 தவறானது.",
        why_d_en="Option D is incorrect.", why_d_ta="தெரிவு D தவறானது.",
        tip_en="AG defends parliamentary election laws before the Supreme Court; he has no role inside the ECI.",
        tip_ta="உச்ச நீதிமன்றத்தில் தேர்தல் சட்டங்களை AG ஆதரித்து வாதிடுகிறார்; தேர்தல் ஆணையத்தில் அவருக்குப் பங்கு இல்லை.",
        fact_en="Association for Democratic Reforms cases regularly saw the AG defending electoral laws.",
        fact_ta="ADR வழக்குகளில் தேர்தல் சட்டங்களை தலைமை வழக்கறிஞரே தொடர்ந்து ஆதரித்து வாதிட்டார்.",
        tags=["polity", "attorney_general", "rpa_1951"]
    ))

    # 57
    questions.append(make_ag_q(
        qid="AG_GT_057",
        diff="Medium",
        qtype="Statement Based",
        subtopic="Bar Council Disciplinary Powers",
        en_stem="Consider the following statements regarding the Attorney General and disciplinary proceedings against advocates:\n1. The Attorney General can address the Disciplinary Committee of the Bar Council of India in matters of public interest.\n2. The Attorney General is an ex-officio member of the Bar Council of India under Section 4 of the Advocates Act.\n3. The Attorney General can personally revoke the sanad (enrollment certificate) of any advocate.\nWhich of the statements given above are correct?",
        ta_stem="தலைமை வழக்கறிஞர் மற்றும் வழக்கறிஞர்கள் மீதான ஒழுங்கு நடவடிக்கைகள் குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. பொது நலன் சார்ந்த விவகாரங்களில் இந்திய பார் கவுன்சிலின் ஒழுங்கு நடவடிக்கைக் குழுவில் தலைமை வழக்கறிஞர் தனது கருத்தை முன்வைக்கலாம்.\n2. வழக்கறிஞர்கள் சட்டம் பிரிவு 4-ன் கீழ் இந்திய பார் கவுன்சிலின் பதவி வழி உறுப்பினர் AG ஆவார்.\n3. எந்தவொரு வழக்கறிஞரின் சனத் (பதிவுச் சான்றிதழ்) உரிமத்தையும் தலைமை வழக்கறிஞர் நேரில் ரத்து செய்ய முடியும்.\nமேற்கூறிய கூற்றுகளில் சரியானவை எவை?",
        en_a="1 and 2 only", ta_a="1 மற்றும் 2 மட்டுமே",
        en_b="2 and 3 only", ta_b="2 மற்றும் 3 மட்டுமே",
        en_c="1 and 3 only", ta_c="1 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3", ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statements 1 and 2 are correct. Statement 3 is incorrect because revoking an advocate's enrollment is a quasi-judicial power vested solely in the Disciplinary Committee of the Bar Council under Section 35, not the AG personally.",
        exp_ta="கூற்றுகள் 1 மற்றும் 2 சரியானவை. வழக்கறிஞரின் பதிவுச் சான்றிதழை ரத்து செய்யும் அதிகாரம் பார் கவுன்சிலின் ஒழுங்கு நடவடிக்கைக் குழுவிற்கே (பிரிவு 35) உண்டு; AG-க்கு இந்த அதிகாரம் தனிப்பட்ட முறையில் இல்லை என்பதால் கூற்று 3 தவறு.",
        why_a_en="Option A is correct: Statements 1 and 2 are true; Disciplinary Committee revokes licenses.",
        why_a_ta="தெரிவு A சரி: கூற்றுகள் 1 மற்றும் 2 சரி; ஒழுங்கு நடவடிக்கைக் குழுவே உரிமத்தை ரத்து செய்யும்.",
        why_b_en="Option B is incorrect: Statement 3 is false.",
        why_b_ta="தெரிவு B தவறு: கூற்று 3 தவறானது.",
        why_c_en="Option C is incorrect.", why_c_ta="தெரிவு C தவறானது.",
        why_d_en="Option D is incorrect.", why_d_ta="தெரிவு D தவறானது.",
        tip_en="License revocation belongs to Bar Council Disciplinary Committees under Section 35, not the AG.",
        tip_ta="உரிமம் ரத்து செய்யும் அதிகாரம் பார் கவுன்சில் குழுவிற்கே உண்டு, AG-க்கு அல்ல.",
        fact_en="Section 35 of the Advocates Act governs misconduct proceedings against advocates.",
        fact_ta="வழக்கறிஞர்கள் சட்டம் பிரிவு 35 தொழில்முறை தவறுகள் மீதான ஒழுங்கு நடவடிக்கையை நிர்வகிக்கிறது.",
        tags=["polity", "attorney_general", "bar_council_powers"]
    ))

    # 58
    questions.append(make_ag_q(
        qid="AG_GT_058",
        diff="Hard",
        qtype="Statement Based",
        subtopic="Constitutional Amendments",
        en_stem="Consider the following statements regarding the Attorney General's appearance in the NJAC judgment (2015):\n1. Attorney General Mukul Rohatgi led the defense of the 99th Constitutional Amendment Act.\n2. The Attorney General submitted that the Collegium system was an extra-constitutional creation.\n3. The Supreme Court in a unanimous 5:0 verdict struck down the NJAC Act.\nWhich of the statements given above are correct?",
        ta_stem="NJAC தீர்ப்பில் (2015) தலைமை வழக்கறிஞர் ஆஜரானது குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 99-வது அரசியலமைப்புத் திருத்தச் சட்டத்தை ஆதரித்து தலைமை வழக்கறிஞர் முகுல் ரோஹத்கி வாதாடினார்.\n2. கொலீஜியம் முறை அரசியலமைப்பிற்கு அப்பாற்பட்ட ஒரு உருவாக்கம் என்று தலைமை வழக்கறிஞர் வாதிட்டார்.\n3. 5:0 என்ற ஒருமனதான தீர்ப்பில் உச்ச நீதிமன்றம் NJAC சட்டத்தை ரத்து செய்தது.\nமேற்கூறிய கூற்றுகளில் சரியானவை எவை?",
        en_a="1 and 2 only", ta_a="1 மற்றும் 2 மட்டுமே",
        en_b="2 and 3 only", ta_b="2 மற்றும் 3 மட்டுமே",
        en_c="1 and 3 only", ta_c="1 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3", ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statements 1 and 2 are correct. Statement 3 is incorrect because the NJAC verdict was NOT unanimous; it was a 4:1 majority decision, with Justice J. Chelameswar dissenting and upholding the NJAC Act.",
        exp_ta="கூற்றுகள் 1 மற்றும் 2 சரியானவை. NJAC தீர்ப்பு ஒருமனதான தீர்ப்பல்ல; நீதிபதி ஜே. செலமேஸ்வர் NJAC சட்டத்தை ஆதரித்து மாறுபட்ட தீர்ப்பு வழங்கியதால், 4:1 என்ற பெரும்பான்மையிலேயே சட்டம் ரத்து செய்யப்பட்டது; எனவே கூற்று 3 தவறு.",
        why_a_en="Option A is correct: Statements 1 and 2 are true; NJAC decision was 4:1, not 5:0.",
        why_a_ta="தெரிவு A சரி: கூற்றுகள் 1 மற்றும் 2 சரி; NJAC தீர்ப்பு 4:1 பெரும்பான்மை தீர்ப்பாகும்.",
        why_b_en="Option B is incorrect: Statement 3 is false.",
        why_b_ta="தெரிவு B தவறு: கூற்று 3 தவறானது.",
        why_c_en="Option C is incorrect.", why_c_ta="தெரிவு C தவறானது.",
        why_d_en="Option D is incorrect.", why_d_ta="தெரிவு D தவறானது.",
        tip_en="In NJAC case (2015), the bench struck down the amendment 4:1 with Justice Chelameswar dissenting.",
        tip_ta="NJAC வழக்கில் (2015) நீதிபதி செலமேஸ்வர் மாறுபட, 4:1 என்ற பெரும்பான்மையில் சட்டம் ரத்து செய்யப்பட்டது.",
        fact_en="Justice J.S. Khehar, J. Chelameswar, M.B. Lokur, Kurian Joseph, and A.K. Goel constituted the 5-judge bench.",
        fact_ta="நீதிபதிகள் கேஹர், செலமேஸ்வர், லோகூர், குரியன் ஜோசப், மற்றும் ஏ.கே. கோயல் ஆகியோர் அமர்வில் இருந்தனர்.",
        tags=["polity", "attorney_general", "njac_case"]
    ))

    # 59
    questions.append(make_ag_q(
        qid="AG_GT_059",
        diff="Medium",
        qtype="Statement Based",
        subtopic="Pre-audience Nuances",
        en_stem="Consider the following statements regarding the right of pre-audience under Section 23 of the Advocates Act:\n1. The Attorney General takes precedence over the Solicitor General.\n2. The Solicitor General takes precedence over the Additional Solicitors General.\n3. An Advocate General of a State takes precedence over the Attorney General when appearing in that State's High Court.\nWhich of the statements given above are correct?",
        ta_stem="வழக்கறிஞர்கள் சட்டம் பிரிவு 23-ன் கீழ் முதன்மை வழக்காடும் உரிமை குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. தலைமை வழக்கறிஞர் சொலிசிட்டர் ஜெனரலை விட முன்னுரிமை பெறுகிறார்.\n2. சொலிசிட்டர் ஜெனரல் கூடுதல் சொலிசிட்டர் ஜெனரல்களை விட முன்னுரிமை பெறுகிறார்.\n3. ஒரு மாநில உயர் நீதிமன்றத்தில் ஆஜராகும் போது, தலைமை வழக்கறிஞரை விட அந்த மாநிலத்தின் அட்வகேட் ஜெனரல் முன்னுரிமை பெறுகிறார்.\nமேற்கூறிய கூற்றுகளில் சரியானவை எவை?",
        en_a="1 and 2 only", ta_a="1 மற்றும் 2 மட்டுமே",
        en_b="2 and 3 only", ta_b="2 மற்றும் 3 மட்டுமே",
        en_c="1 and 3 only", ta_c="1 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3", ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statements 1 and 2 are correct. Statement 3 is incorrect because under Section 23(1), the Attorney General has right of pre-audience over ALL other advocates in ALL courts in India, including High Courts.",
        exp_ta="கூற்றுகள் 1 மற்றும் 2 சரியானவை. பிரிவு 23(1)-ன் கீழ் உயர் நீதிமன்றங்கள் உட்பட இந்தியாவின் அனைத்து நீதிமன்றங்களிலும் பிற அனைத்து வழக்கறிஞர்களை விடவும் தலைமை வழக்கறிஞருக்கே முதலிடம் என்பதால் கூற்று 3 தவறு.",
        why_a_en="Option A is correct: AG holds top precedence even in state High Courts.",
        why_a_ta="தெரிவு A சரி: மாநில உயர் நீதிமன்றங்களிலும் AG-க்கே முதல் முன்னுரிமை.",
        why_b_en="Option B is incorrect: Statement 3 is false.",
        why_b_ta="தெரிவு B தவறு: கூற்று 3 தவறானது.",
        why_c_en="Option C is incorrect.", why_c_ta="தெரிவு C தவறானது.",
        why_d_en="Option D is incorrect.", why_d_ta="தெரிவு D தவறானது.",
        tip_en="Section 23 order: AG > SG > ASG > State Advocate General (in that state's High Court).",
        tip_ta="பிரிவு 23 வரிசை: AG > SG > ASG > மாநில அட்வகேட் ஜெனரல்.",
        fact_en="Section 23(2) gives the Advocate General precedence over other advocates in their High Court, but subject to Section 23(1).",
        fact_ta="பிரிவு 23(2) அட்வகேட் ஜெனரலுக்கு முன்னுரிமை அளித்தாலும் அது பிரிவு 23(1)-ன் AG அதிகாரத்திற்கு உட்பட்டது.",
        tags=["polity", "attorney_general", "pre_audience_hierarchy"]
    ))

    # 60
    questions.append(make_ag_q(
        qid="AG_GT_060",
        diff="Hard",
        qtype="Statement Based",
        subtopic="Article 370 Verdict",
        en_stem="Consider the following statements regarding the Supreme Court's Article 370 verdict (December 2023) where the AG argued:\n1. The 5-judge bench unanimously upheld Constitutional Orders 272 and 273 abrogating Article 370.\n2. The Supreme Court accepted the AG's submission that Jammu and Kashmir retained no internal sovereignty after accession.\n3. The Supreme Court validated the permanent conversion of Jammu and Kashmir into a Union Territory without restoration of statehood.\nWhich of the statements given above are correct?",
        ta_stem="AG வாதிட்ட உச்ச நீதிமன்றத்தின் சரத்து 370 தீர்ப்பு (டிசம்பர் 2023) குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. சரத்து 370-ஐ ரத்து செய்த அரசியலமைப்பு உத்தரவுகள் 272 மற்றும் 273-ஐ 5 நீதிபதிகள் அமர்வு ஒருமனதாக உறுதி செய்தது.\n2. இணைப்பிற்குப் பிறகு ஜம்மு காஷ்மீருக்கு எந்த உள்நாட்டு இறையாண்மையும் எஞ்சியிருக்கவில்லை என்ற AG-யின் வாதத்தை உச்ச நீதிமன்றம் ஏற்றுக்கொண்டது.\n3. ஜம்மு காஷ்மீர் மாநில அந்தஸ்தை மீண்டும் வழங்காமல் நிரந்தரமாக யூனியன் பிரதேசமாக மாற்றியதை உச்ச நீதிமன்றம் உறுதி செய்தது.\nமேற்கூறிய கூற்றுகளில் சரியானவை எவை?",
        en_a="1 and 2 only", ta_a="1 மற்றும் 2 மட்டுமே",
        en_b="2 and 3 only", ta_b="2 மற்றும் 3 மட்டுமே",
        en_c="1 and 3 only", ta_c="1 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3", ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statements 1 and 2 are correct. Statement 3 is incorrect because the Supreme Court directed the Union to restore statehood to Jammu and Kashmir as earliest as possible and hold assembly elections by September 30, 2024.",
        exp_ta="கூற்றுகள் 1 மற்றும் 2 சரியானவை. ஜம்மு காஷ்மீருக்கு விரைவில் மாநில அந்தஸ்தை மீண்டும் வழங்க வேண்டும் என்றும் செப்டம்பர் 30, 2024-க்குள் சட்டமன்றத் தேர்தலை நடத்த வேண்டும் என்றும் உச்ச நீதிமன்றம் உத்தரவிட்டதால் கூற்று 3 தவறு.",
        why_a_en="Option A is correct: Statements 1 and 2 are true; SC ordered restoration of statehood.",
        why_a_ta="தெரிவு A சரி: கூற்றுகள் 1 மற்றும் 2 சரி; மாநில அந்தஸ்தை மீண்டும் வழங்க நீதிமன்றம் உத்தரவிட்டது.",
        why_b_en="Option B is incorrect: Statement 3 is false.",
        why_b_ta="தெரிவு B தவறு: கூற்று 3 தவறானது.",
        why_c_en="Option C is incorrect.", why_c_ta="தெரிவு C தவறானது.",
        why_d_en="Option D is incorrect.", why_d_ta="தெரிவு D தவறானது.",
        tip_en="In the Art 370 verdict (Dec 11, 2023), SC upheld abrogation but directed restoration of statehood at the earliest.",
        tip_ta="சரத்து 370 தீர்ப்பில் ரத்து செய்யப்பட்டது உறுதியானது, ஆனால் மாநில அந்தஸ்தை உடனே மீட்க உத்தரவிடப்பட்டது.",
        fact_en="The bench was headed by CJI D.Y. Chandrachud.",
        fact_ta="தலைமை நீதிபதி டி.ஒய். சந்திரசூட் இந்த அமர்வுக்குத் தலைமை தாங்கினார்.",
        tags=["polity", "attorney_general", "article_370"]
    ))

    # -------------------------------------------------------------
    # 15 Assertion & Reason MCQs (AG_GT_061 to AG_GT_075)
    # -------------------------------------------------------------

    OPTIONS_AR = [
        ("Both (A) and (R) are true and (R) is the correct explanation of (A)", "(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-வின் சரியான விளக்கமாகும்"),
        ("Both (A) and (R) are true but (R) is not the correct explanation of (A)", "(A) மற்றும் (R) இரண்டும் சரி, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல"),
        ("(A) is true but (R) is false", "(A) சரி ஆனால் (R) தவறு"),
        ("(A) is false but (R) is true", "(A) தவறு ஆனால் (R) சரி")
    ]

    ar_data = [
        # 61
        ("Assertion (A): The Attorney General of India is not debarred from private legal practice.\nReason (R): The Attorney General is not a full-time salaried government servant.",
         "கூற்று (A): இந்திய தலைமை வழக்கறிஞர் தனியார் சட்டப் பயிற்சி மேற்கொள்வதிலிருந்து தடை செய்யப்படவில்லை.\nகாரணம் (R): தலைமை வழக்கறிஞர் முழுநேர ஊதியம் பெறும் அரசு ஊழியர் அல்ல.",
         0, "Both true and R explains A. Because AG is not a civil servant, he retains private practice rights subject to ethics rules.",
         "இரண்டும் சரி மற்றும் R சரியான விளக்கம். AG அரசு ஊழியர் அல்லாததால் நிபந்தனைகளுடன் தனியார் பயிற்சி செய்யலாம்.", "Private Practice"),

        # 62
        ("Assertion (A): The Attorney General cannot vote in Parliament under Article 88.\nReason (R): The Attorney General is not an elected Member of Parliament representing a constituency.",
         "கூற்று (A): சரத்து 88-ன் கீழ் நாடாளுமன்றத்தில் தலைமை வழக்கறிஞர் வாக்களிக்க முடியாது.\nகாரணம் (R): தலைமை வழக்கறிஞர் ஒரு தொகுதியைப் பிரதிநிதித்துவப்படுத்தும் தேர்ந்தெடுக்கப்பட்ட நாடாளுமன்ற உறுப்பினர் அல்ல.",
         0, "Both true and R explains A. Voting is a democratic prerogative reserved for MPs.",
         "இரண்டும் சரி மற்றும் R சரியான விளக்கம். வாக்குரிமை என்பது எம்பிக்களுக்கு மட்டுமே உரிய மக்களாட்சி உரிமையாகும்.", "Voting Prohibition"),

        # 63
        ("Assertion (A): The Attorney General can be removed from office at any time without any inquiry.\nReason (R): Under Article 76(4), the Attorney General holds office during the pleasure of the President.",
         "கூற்று (A): எந்த விசாரணையுமின்றி எப்போது வேண்டுமானாலும் தலைமை வழக்கறிஞரைப் பதவியிலிருந்து நீக்க முடியும்.\nகாரணம் (R): சரத்து 76(4)-ன் கீழ் தலைமை வழக்கறிஞர் குடியரசுத் தலைவரின் விருப்பம் உள்ளவரை பதவியில் நீடிக்கிறார்.",
         0, "Both true and R explains A. The doctrine of pleasure gives plenary removal power.",
         "இரண்டும் சரி மற்றும் R சரியான விளக்கம். விருப்பக் கோட்பாடு நிர்வாகத்திற்கு முழுமையான நீக்கும் அதிகாரத்தை அளிக்கிறது.", "Doctrine of Pleasure"),

        # 64
        ("Assertion (A): The Attorney General of India is a member of the Union Cabinet.\nReason (R): The Attorney General gives legal advice to the Government of India on matters referred by the President.",
         "கூற்று (A): இந்திய தலைமை வழக்கறிஞர் மத்திய அமைச்சரவையில் ஓர் உறுப்பினர் ஆவார்.\nகாரணம் (R): குடியரசுத் தலைவரால் குறிப்பிடப்படும் விவகாரங்களில் தலைமை வழக்கறிஞர் இந்திய அரசுக்கு சட்ட ஆலோசனை வழங்குகிறார்.",
         3, "A is false but R is true. AG is NOT a member of the Cabinet in India; Art 76(2) duty to advise is true.",
         "(A) தவறு ஆனால் (R) சரி. இந்தியாவில் AG அமைச்சரவை உறுப்பினர் அல்ல; ஆனால் சரத்து 76(2)-ன் படி ஆலோசனை வழங்குவது உண்மை.", "Cabinet Status"),

        # 65
        ("Assertion (A): The advice of the Attorney General is legally binding on the Government of India.\nReason (R): The Attorney General is the highest law officer in the country.",
         "கூற்று (A): இந்திய தலைமை வழக்கறிஞரின் ஆலோசனை இந்திய அரசை சட்டப்பூர்வமாகக் கட்டுப்படுத்தும்.\nகாரணம் (R): தலைமை வழக்கறிஞர் நாட்டின் மிக உயர்ந்த சட்ட அதிகாரி ஆவார்.",
         3, "A is false but R is true. The advice is advisory, not binding, though AG is indeed the highest law officer.",
         "(A) தவறு ஆனால் (R) சரி. ஆலோசனை கட்டுப்படுத்தாது, ஆனால் AG நாட்டின் தலைமை சட்ட அதிகாரி என்பது உண்மையாகும்.", "Advisory Status"),

        # 66
        ("Assertion (A): The Attorney General cannot advise or hold a brief against the Government of India.\nReason (R): An advocate owes a paramount fiduciary duty of loyalty to their client.",
         "கூற்று (A): இந்திய அரசுக்கு எதிராக ஆலோசிக்கவோ வாதாடவோ தலைமை வழக்கறிஞரால் முடியாது.\nகாரணம் (R): ஒரு வழக்கறிஞர் தனது வாடிக்கையாளருக்கு முழுமையான தொழில்முறை விசுவாசத்தைக் கொண்டிருக்க வேண்டும்.",
         0, "Both true and R explains A. The conflict of interest rule prevents appearing against one's own client.",
         "இரண்டும் சரி மற்றும் R சரியான விளக்கம். தனது சொந்த வாடிக்கையாளருக்கு எதிராக வாதாடுவது நலன் முரண்பாட்டை உருவாக்கும்.", "Fiduciary Duty"),

        # 67
        ("Assertion (A): The Attorney General must have the qualifications required to be appointed as a Judge of the High Court.\nReason (R): The qualifications for appointment as Advocate General of a State are specified in Article 165.",
         "கூற்று (A): இந்திய தலைமை வழக்கறிஞராக நியமிக்கப்படுவதற்கு உயர் நீதிமன்ற நீதிபதியாகத் தகுதி பெற்றிருக்க வேண்டும்.\nகாரணம் (R): மாநில அட்வகேட் ஜெனரலாக நியமிக்கப்படுவதற்கான தகுதிகள் சரத்து 165-ல் குறிப்பிடப்பட்டுள்ளன.",
         3, "A is false but R is true. AG requires Supreme Court Judge qualifications under Article 76(1), not High Court.",
         "(A) தவறு ஆனால் (R) சரி. AG-க்கு உச்ச நீதிமன்ற நீதிபதி தகுதி தேவை, உயர் நீதிமன்றம் அல்ல; சரத்து 165 மாநில அட்வகேட் ஜெனரலைக் குறிப்பது உண்மை.", "Qualifications"),

        # 68
        ("Assertion (A): Communications between the Attorney General and the Government of India are privileged under Section 126 of the Evidence Act.\nReason (R): The relationship between the Attorney General and the Union Government is that of a counsel and client.",
         "கூற்று (A): தலைமை வழக்கறிஞருக்கும் அரசுக்கும் இடையிலான ஆலோசனைகள் சாட்சியச் சட்டம் பிரிவு 126-ன் கீழ் ரகசியப் பாதுகாப்பு பெறுகின்றன.\nகாரணம் (R): தலைமை வழக்கறிஞருக்கும் மத்திய அரசுக்கும் இடையிலான உறவு வழக்கறிஞர்-வாடிக்கையாளர் உறவாகும்.",
         0, "Both true and R explains A. Section 126 protects professional legal consultations.",
         "இரண்டும் சரி மற்றும் R சரியான விளக்கம். பிரிவு 126 வழக்கறிஞர்-வாடிக்கையாளர் ஆலோசனைகளைப் பாதுகாக்கிறது.", "Evidence Act"),

        # 69
        ("Assertion (A): The Attorney General is placed above the Solicitor General in the order of pre-audience.\nReason (R): Under Section 23 of the Advocates Act, the Attorney General has the first right of pre-audience over all other advocates.",
         "கூற்று (A): முதன்மை வழக்காடும் வரிசையில் சொலிசிட்டர் ஜெனரலை விட தலைமை வழக்கறிஞர் முன்னிலையில் வைக்கப்பட்டுள்ளார்.\nகாரணம் (R): வழக்கறிஞர்கள் சட்டம் பிரிவு 23-ன் கீழ், மற்ற அனைத்து வழக்கறிஞர்களை விடவும் AG முதல் முன்னுரிமை பெறுகிறார்.",
         0, "Both true and R explains A. Section 23 establishes the statutory hierarchy of pre-audience.",
         "இரண்டும் சரி மற்றும் R சரியான விளக்கம். பிரிவு 23 இந்த சட்டப்பூர்வ முன்னுரிமை வரிசையை நிறுவுகிறது.", "Pre-audience"),

        # 70
        ("Assertion (A): The Attorney General can enter a nolle prosequi to unilaterally terminate any criminal proceeding in an Indian trial court.\nReason (R): The Attorney General is the first law officer of the Government of India under Article 76.",
         "கூற்று (A): இந்திய விசாரணை நீதிமன்றங்களில் எந்தவொரு குற்றவியல் வழக்கையும் தன்னிச்சையாக ரத்து செய்யும் அதிகாரம் (nolle prosequi) AG-க்கு உண்டு.\nகாரணம் (R): சரத்து 76-ன் கீழ் தலைமை வழக்கறிஞர் இந்திய அரசாங்கத்தின் முதல் சட்ட அதிகாரி ஆவார்.",
         3, "A is false but R is true. Indian AG has no common-law nolle prosequi power; Sec 321 CrPC governs withdrawal by Public Prosecutor.",
         "(A) தவறு ஆனால் (R) சரி. இந்திய AG-க்கு nolle prosequi அதிகாரம் கிடையாது; பிரிவு 321-ன் படி அரசு வழக்கறிஞரே வழக்கை திரும்பப் பெறலாம்.", "Criminal Procedure"),

        # 71
        ("Assertion (A): The Attorney General of India has right of audience in all courts throughout India under Article 76(3).\nReason (R): The Attorney General represents the Union of India and must be able to assist any court where Union interests are involved.",
         "கூற்று (A): சரத்து 76(3)-ன் கீழ் இந்தியா முழுவதும் உள்ள அனைத்து நீதிமன்றங்களிலும் தலைமை வழக்கறிஞருக்கு வழக்காடும் உரிமை உண்டு.\nகாரணம் (R): இந்திய ஒன்றியத்தைப் பிரதிநிதித்துவப்படுத்தும் AG, ஒன்றிய அரசின் நலன் உள்ள எந்த நீதிமன்றத்திற்கும் உதவ வேண்டியுள்ளது.",
         0, "Both true and R explains A. Article 76(3) right of audience supports his nationwide constitutional duties.",
         "இரண்டும் சரி மற்றும் R சரியான விளக்கம். அகில இந்திய அளவில் ஒன்றிய அரசின் நலன்களைப் பாதுகாக்க சரத்து 76(3) உதவுகிறது.", "Right of Audience"),

        # 72
        ("Assertion (A): The Attorney General of India is entitled to parliamentary privileges under Article 105(4).\nReason (R): The Attorney General is an elected Member of the Lok Sabha.",
         "கூற்று (A): சரத்து 105(4)-ன் கீழ் தலைமை வழக்கறிஞருக்கு நாடாளுமன்ற சிறப்புரிமைகள் உண்டு.\nகாரணம் (R): தலைமை வழக்கறிஞர் மக்களவையின் தேர்ந்தெடுக்கப்பட்ட உறுப்பினர் ஆவார்.",
         2, "A is true but R is false. AG enjoys privileges under Art 105(4), but is NOT an elected MP.",
         "(A) சரி ஆனால் (R) தவறு. சரத்து 105(4)-ன் கீழ் சலுகைகள் உண்டு, ஆனால் அவர் தேர்ந்தெடுக்கப்பட்ட எம்பி அல்ல.", "Privileges"),

        # 73
        ("Assertion (A): The remuneration of the Attorney General is not charged upon the Consolidated Fund of India.\nReason (R): The remuneration of the Attorney General is determined by the President under Article 76(4) rather than being fixed in the Second Schedule.",
         "கூற்று (A): தலைமை வழக்கறிஞரின் ஊதியம் இந்திய ஒருங்கிணைந்த நிதியின் மீது கட்டாயச் செலவாக (charged) வைக்கப்படவில்லை.\nகாரணம் (R): தலைமை வழக்கறிஞரின் ஊதியம் 2-வது அட்டவணையில் நிர்ணயிக்கப்படாமல், சரத்து 76(4)-ன் கீழ் குடியரசுத் தலைவரால் தீர்மானிக்கப்படுகிறது.",
         0, "Both true and R explains A. Because remuneration is determined by presidential order, it is not charged expenditure.",
         "இரண்டும் சரி மற்றும் R சரியான விளக்கம். குடியரசுத் தலைவர் உத்தரவால் தீர்மானிக்கப்படுவதால் இது கட்டாயச் செலவு அல்ல.", "Remuneration"),

        # 74
        ("Assertion (A): The Attorney General conventionally submits his resignation when a new Government takes office.\nReason (R): The Attorney General is appointed on the advice of the Council of Ministers and must enjoy the confidence of the Government in power.",
         "கூற்று (A): புதிய அரசு பதவியேற்கும் போது தலைமை வழக்கறிஞர் தனது ராஜினாமாவை சமர்ப்பிப்பது மரபாகும்.\nகாரணம் (R): அமைச்சரவையின் ஆலோசனையின் பேரில் நியமிக்கப்படுவதால், ஆளும் அரசின் நம்பிக்கையைப் பெற்றவராக அவர் இருக்க வேண்டும்.",
         0, "Both true and R explains A. The resignation convention preserves mutual trust between executive and counsel.",
         "இரண்டும் சரி மற்றும் R சரியான விளக்கம். நிர்வாகத்திற்கும் சட்ட ஆலோசகருக்கும் இடையேயான நம்பிக்கையை இந்த மரபு உறுதி செய்கிறது.", "Convention"),

        # 75
        ("Assertion (A): The Supreme Court can transfer cases from one High Court to another on an application by the Attorney General under Article 139A.\nReason (R): Article 139A was enacted to prevent conflicting judgments on substantial questions of general importance across High Courts.",
         "கூற்று (A): சரத்து 139A-ன் கீழ் AG விண்ணப்பத்தின் பேரில் வழக்குகளை மாற்ற உச்ச நீதிமன்றத்திற்கு அதிகாரம் உண்டு.\nகாரணம் (R): முக்கிய பொது வினாக்களில் பல்வேறு உயர் நீதிமன்றங்கள் முரண்பட்ட தீர்ப்புகள் வழங்குவதைத் தவிர்க்க சரத்து 139A இயற்றப்பட்டது.",
         0, "Both true and R explains A. Article 139A avoids inter-court conflict by centralizing constitutional adjudication.",
         "இரண்டும் சரி மற்றும் R சரியான விளக்கம். சட்ட ஒற்றுமையை நிலைநாட்ட சரத்து 139A வழக்குகளை உச்ச நீதிமன்றத்திற்கு மாற்றுகிறது.", "Article 139A")
    ]

    for i, item in enumerate(ar_data):
        qid = f"AG_GT_{61+i:03d}"
        stem_en, stem_ta, c_idx, exp_en, exp_ta, subtopic = item
        c_key = ["A", "B", "C", "D"][c_idx]

        why_en = {}
        why_ta = {}
        for idx, key in enumerate(["A", "B", "C", "D"]):
            if idx == c_idx:
                why_en[key] = f"Option {key} correctly reflects the truth values and logical relation between Assertion (A) and Reason (R)."
                why_ta[key] = f"கூற்று (A) மற்றும் காரணம் (R) ஆகியவற்றின் உண்மைத் தன்மை மற்றும் தர்க்கரீதியான தொடர்பை தெரிவு {key} சரியாகக் குறிக்கிறது."
            else:
                why_en[key] = f"Option {key} is incorrect."
                why_ta[key] = f"தெரிவு {key} தவறானது."

        q = make_ag_q(
            qid=qid,
            diff="Medium",
            qtype="Assertion and Reason",
            subtopic=subtopic,
            en_stem=stem_en,
            ta_stem=stem_ta,
            en_a=OPTIONS_AR[0][0], ta_a=OPTIONS_AR[0][1],
            en_b=OPTIONS_AR[1][0], ta_b=OPTIONS_AR[1][1],
            en_c=OPTIONS_AR[2][0], ta_c=OPTIONS_AR[2][1],
            en_d=OPTIONS_AR[3][0], ta_d=OPTIONS_AR[3][1],
            correct_key=c_key,
            exp_en=exp_en, exp_ta=exp_ta,
            why_a_en=why_en["A"], why_a_ta=why_ta["A"],
            why_b_en=why_en["B"], why_b_ta=why_ta["B"],
            why_c_en=why_en["C"], why_c_ta=why_ta["C"],
            why_d_en=why_en["D"], why_d_ta=why_ta["D"],
            tip_en="Assertion-Reason questions test both factual accuracy and causal relationship.",
            tip_ta="கூற்று-காரண வினாக்கள் உண்மைத் தன்மை மற்றும் காரணத் தொடர்பு இரண்டையும் சோதிக்கின்றன.",
            fact_en="Standard UPSC/TNPSC format for constitutional functionaries.",
            fact_ta="அரசியலமைப்பு அலுவலர்களுக்கான நிலையான TNPSC வடிவமைப்பு.",
            tags=["polity", "attorney_general", "assertion_reason"]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 15 Match the Following MCQs (AG_GT_076 to AG_GT_090)
    # -------------------------------------------------------------

    match_items = [
        # 76: Four Articles
        ("Articles of Part V",
         "Match List-I (Constitutional Article) with List-II (Subject Matter):",
         "பட்டியல்-I-ஐ (அரசியலமைப்புச் சரத்து) பட்டியல்-II உடன் (பொருள்) பொருத்துக:",
         [("a. Article 76", "1. Attorney General of India"),
          ("b. Article 88", "2. Rights of Ministers and AG in Parliament"),
          ("c. Article 105", "3. Powers and privileges of Parliament and AG"),
          ("d. Article 143", "4. Advisory jurisdiction of Supreme Court")],
         [("a. சரத்து 76", "1. இந்திய தலைமை வழக்கறிஞர்"),
          ("b. சரத்து 88", "2. நாடாளுமன்றத்தில் அமைச்சர்கள் மற்றும் AG உரிமைகள்"),
          ("c. சரத்து 105", "3. நாடாளுமன்றம் மற்றும் AG-யின் சலுகைகள்"),
          ("d. சரத்து 143", "4. உச்ச நீதிமன்றத்தின் ஆலோசனை அதிகார வரம்பு")]),

        # 77: Parallel State Articles
        ("Union and State Parallels",
         "Match List-I (Union Article) with List-II (Corresponding State Article):",
         "பட்டியல்-I-ஐ (மத்திய அரசு சரத்து) பட்டியல்-II உடன் (இணையான மாநில அரசு சரத்து) பொருத்துக:",
         [("a. Article 76 (Attorney General)", "1. Article 165 (Advocate General)"),
          ("b. Article 88 (Right to address Parliament)", "2. Article 177 (Right to address Legislature)"),
          ("c. Article 105 (Parliamentary privileges)", "3. Article 194 (Legislative privileges)"),
          ("d. Article 74 (Union Council of Ministers)", "4. Article 163 (State Council of Ministers)")],
         [("a. சரத்து 76 (தலைமை வழக்கறிஞர்)", "1. சரத்து 165 (அட்வகேட் ஜெனரல்)"),
          ("b. சரத்து 88 (நாடாளுமன்றத்தில் பேசும் உரிமை)", "2. சரத்து 177 (சட்டமன்றத்தில் பேசும் உரிமை)"),
          ("c. சரத்து 105 (நாடாளுமன்ற சலுகைகள்)", "3. சரத்து 194 (சட்டமன்ற சலுகைகள்)"),
          ("d. சரத்து 74 (மத்திய அமைச்சரவை)", "4. சரத்து 163 (மாநில அமைச்சரவை)")]),

        # 78: Key Sections
        ("Statutory Sections",
         "Match List-I (Act and Section) with List-II (Core Provision):",
         "பட்டியல்-I-ஐ (சட்டம் மற்றும் பிரிவு) பட்டியல்-II உடன் (முதன்மை விதி) பொருத்துக:",
         [("a. Section 23, Advocates Act 1961", "1. Pre-audience of Attorney General"),
          ("b. Section 4, Advocates Act 1961", "2. Bar Council of India ex-officio membership"),
          ("c. Section 15, Contempt of Courts Act 1971", "3. Written consent for criminal contempt in SC"),
          ("d. Section 126, Evidence Act 1872", "4. Professional privilege protecting legal advice")],
         [("a. பிரிவு 23, வழக்கறிஞர்கள் சட்டம்", "1. தலைமை வழக்கறிஞரின் முதன்மை வழக்காடும் உரிமை"),
          ("b. பிரிவு 4, வழக்கறிஞர்கள் சட்டம்", "2. பார் கவுன்சில் பதவி வழி உறுப்பினர் பதவி"),
          ("c. பிரிவு 15, நீதிமன்ற அவமதிப்புச் சட்டம்", "3. SC குற்றவியல் அவமதிப்புக்கான எழுத்துப்பூர்வ ஒப்புதல்"),
          ("d. பிரிவு 126, சாட்சியச் சட்டம்", "4. சட்ட ஆலோசனையைப் பாதுகாக்கும் தொழில்முறை ரகசியம்")]),

        # 79: Historic AGs
        ("Historic Attorneys General",
         "Match List-I (Attorney General) with List-II (Distinguished Attribute):",
         "பட்டியல்-I-ஐ (தலைமை வழக்கறிஞர்) பட்டியல்-II உடன் (தனித்துவமான பண்பு) பொருத்துக:",
         [("a. M.C. Setalvad", "1. First AG and longest tenure (1950–1963)"),
          ("b. Niren De", "2. Argued Kesavananda Bharati and ADM Jabalpur"),
          ("c. K. Parasaran", "3. Former Advocate General of Tamil Nadu and Pitamaha of Bar"),
          ("d. R. Venkataramani", "4. Current 16th Attorney General appointed in 2022")],
         [("a. எம்.சி. செடல்வாட்", "1. முதல் AG மற்றும் மிக நீண்ட பதவிக்காலம் (1950-1963)"),
          ("b. நீரேன் டே", "2. கேசவானந்த பாரதி மற்றும் ஜபல்பூர் வழக்குகளில் வாதாடியவர்"),
          ("c. கே. பராசரன்", "3. தமிழக முன்னாள் அட்வகேட் ஜெனரல் மற்றும் வழக்கறிஞர் பிதாமகர்"),
          ("d. ஆர். வெங்கடரமணி", "4. 2022-ல் நியமிக்கப்பட்ட தற்போதைய 16-வது AG")]),

        # 80: Modern Cases & AGs
        ("Modern Cases and AGs",
         "Match List-I (Landmark Case) with List-II (Attorney General representing Union):",
         "பட்டியல்-I-ஐ (முக்கிய வழக்கு) பட்டியல்-II உடன் (மத்திய அரசுக்காக வாதாடிய தலைமை வழக்கறிஞர்) பொருத்துக:",
         [("a. NJAC Case (2015)", "1. Mukul Rohatgi"),
          ("b. Aadhaar Validity Case (2018)", "2. K.K. Venugopal"),
          ("c. Article 370 Challenge (2023)", "3. R. Venkataramani"),
          ("d. 2G Reference (2012)", "4. G.E. Vahanvati")],
         [("a. NJAC வழக்கு (2015)", "1. முகுல் ரோஹத்கி"),
          ("b. ஆதார் வழக்கு (2018)", "2. கே.கே. வேணுகோபால்"),
          ("c. சரத்து 370 வழக்கு (2023)", "3. ஆர். வெங்கடரமணி"),
          ("d. 2G குறிப்புரை (2012)", "4. ஜி.இ. வாகனவதி")]),

        # 81: Law Officers
        ("Law Officers of the Union",
         "Match List-I (Law Officer) with List-II (Constitutional / Administrative Status):",
         "பட்டியல்-I-ஐ (சட்ட அதிகாரி) பட்டியல்-II உடன் (அரசியலமைப்பு / நிர்வாக அந்தஸ்து) பொருத்துக:",
         [("a. Attorney General of India", "1. Constitutional office under Article 76"),
          ("b. Solicitor General of India", "2. Statutory executive post assisting the AG"),
          ("c. Additional Solicitor General", "3. Non-constitutional law officer assisting SG and AG"),
          ("d. Advocate General of State", "4. Constitutional office under Article 165")],
         [("a. இந்திய தலைமை வழக்கறிஞர்", "1. சரத்து 76-ன் கீழ் அரசியலமைப்புப் பதவி"),
          ("b. இந்திய சொலிசிட்டர் ஜெனரல்", "2. AG-க்கு உதவும் நிர்வாக சட்டப் பதவி"),
          ("c. கூடுதல் சொலிசிட்டர் ஜெனரல்", "3. AG மற்றும் SG-க்கு உதவும் சட்ட அதிகாரி"),
          ("d. மாநில அட்வகேட் ஜெனரல்", "4. சரத்து 165-ன் கீழ் அரசியலமைப்புப் பதவி")]),

        # 82: Historical Eras
        ("Historical Eras",
         "Match List-I (Statute / Charter) with List-II (Chief Law Officer Created):",
         "பட்டியல்-I-ஐ (சட்டம் / பட்டயம்) பட்டியல்-II உடன் (உருவாக்கப்பட்ட தலைமை சட்ட அதிகாரி) பொருத்துக:",
         [("a. East India Company (1684)", "1. Advocate-General of Bengal"),
          ("b. Government of India Act 1935", "2. Advocate-General for the Federation"),
          ("c. Constitution of India 1950", "3. Attorney General of India"),
          ("d. Advocates Act 1961", "4. Pre-audience under Section 23")],
         [("a. கிழக்கிந்திய கம்பெனி (1684)", "1. வங்காள அட்வகேட்-ஜெனரல்"),
          ("b. இந்திய அரசுச் சட்டம் 1935", "2. கூட்டாட்சிக்கான அட்வகேட்-ஜெனரல்"),
          ("c. இந்திய அரசியலமைப்பு 1950", "3. இந்திய தலைமை வழக்கறிஞர்"),
          ("d. வழக்கறிஞர்கள் சட்டம் 1961", "4. பிரிவு 23-ன் கீழ் முதன்மை வாதாடல்")]),

        # 83: Prime Ministers and AGs
        ("Prime Ministers and AG Appointments",
         "Match List-I (Prime Minister) with List-II (Attorney General Appointed):",
         "பட்டியல்-I-ஐ (பிரதமர்) பட்டியல்-II உடன் (அவர் காலத்தில் நியமிக்கப்பட்ட AG) பொருத்துக:",
         [("a. Jawaharlal Nehru", "1. M.C. Setalvad (1950)"),
          ("b. Morarji Desai", "2. S.V. Gupte (1977)"),
          ("c. Atal Bihari Vajpayee", "3. Soli Sorabjee (2nd term, 1998)"),
          ("d. Narendra Modi", "4. Mukul Rohatgi (2014)")],
         [("a. ஜவஹர்லால் நேரு", "1. எம்.சி. செடல்வாட் (1950)"),
          ("b. மொரார்ஜி தேசாய்", "2. எஸ்.வி. குப்தே (1977)"),
          ("c. அடல் பிகாரி வாஜ்பாய்", "3. சோலி சொராப்ஜி (2-வது முறை, 1998)"),
          ("d. நரேந்திர மோடி", "4. முகுல் ரோஹத்கி (2014)")]),

        # 84: Remuneration Authorities
        ("Remuneration Authorities",
         "Match List-I (Post) with List-II (Determining Authority for Remuneration):",
         "பட்டியல்-I-ஐ (பதவி) பட்டியல்-II உடன் (ஊதியத்தை நிர்ணயிக்கும் அதிகாரம்) பொருத்துக:",
         [("a. Attorney General of India", "1. Determined by President of India"),
          ("b. Advocate General of a State", "2. Determined by Governor of the State"),
          ("c. Supreme Court Judge", "3. Determined by Parliament by law"),
          ("d. High Court Judge", "4. Determined by Parliament by law")],
         [("a. இந்திய தலைமை வழக்கறிஞர்", "1. இந்தியக் குடியரசுத் தலைவரால் நிர்ணயிக்கப்படுகிறது"),
          ("b. மாநில அட்வகேட் ஜெனரல்", "2. மாநில ஆளுநரால் நிர்ணயிக்கப்படுகிறது"),
          ("c. உச்ச நீதிமன்ற நீதிபதி", "3. நாடாளுமன்றச் சட்டத்தால் நிர்ணயிக்கப்படுகிறது"),
          ("d. உயர் நீதிமன்ற நீதிபதி", "4. நாடாளுமன்றச் சட்டத்தால் நிர்ணயிக்கப்படுகிறது")]),

        # 85: Legal Maxims
        ("Maxims & Doctrine",
         "Match List-I (Legal Doctrine) with List-II (Application to Attorney General):",
         "பட்டியல்-I-ஐ (சட்டக் கோட்பாடு) பட்டியல்-II உடன் (தலைமை வழக்கறிஞருக்கான பயன்பாடு) பொருத்துக:",
         [("a. Doctrine of Pleasure", "1. Governs tenure under Article 76(4)"),
          ("b. Amicus Curiae", "2. Assisting court as objective neutral friend"),
          ("c. Pre-audience", "3. Priority in addressing benches over other counsel"),
          ("d. Nolle Prosequi", "4. Power to withdraw prosecution (not held by AG in India)")],
         [("a. விருப்பக் கோட்பாடு", "1. சரத்து 76(4)-ன் கீழ் பதவிக்காலத்தை நிர்வகிக்கிறது"),
          ("b. நீதிமன்ற நண்பர் (Amicus)", "2. நடுநிலையான ஆலோசகராக நீதிமன்றத்திற்கு உதவுதல்"),
          ("c. முதன்மை வாதாடல்", "3. பிற வழக்கறிஞர்களை விட முதலில் வாதாடும் முன்னுரிமை"),
          ("d. Nolle Prosequi", "4. வழக்கை ரத்து செய்யும் அதிகாரம் (இந்திய AG-க்கு இல்லை)")]),

        # 86: Tenure Characteristics
        ("Tenure Comparison",
         "Match List-I (Office) with List-II (Nature of Tenure):",
         "பட்டியல்-I-ஐ (பதவி) பட்டியல்-II உடன் (பதவிக்காலத்தின் தன்மை) பொருத்துக:",
         [("a. Attorney General of India", "1. Pleasure of President (no fixed term)"),
          ("b. Comptroller and Auditor General", "2. 6 years or 65 years of age"),
          ("c. Member of UPSC", "3. 6 years or 65 years of age"),
          ("d. Chief Election Commissioner", "4. 6 years or 65 years of age")],
         [("a. இந்திய தலைமை வழக்கறிஞர்", "1. குடியரசுத் தலைவரின் விருப்பம் (நிலையான காலம் இல்லை)"),
          ("b. இந்திய தலைமை கணக்குத் தணிக்கையாளர்", "2. 6 ஆண்டுகள் அல்லது 65 வயது"),
          ("c. UPSC உறுப்பினர்", "3. 6 ஆண்டுகள் அல்லது 65 வயது"),
          ("d. தலைமைத் தேர்தல் ஆணையர்", "4. 6 ஆண்டுகள் அல்லது 65 வயது")]),

        # 87: CPC & Supreme Court Rules
        ("Procedural Codes",
         "Match List-I (Procedural Provision) with List-II (Operation for Law Officers):",
         "பட்டியல்-I-ஐ (நடைமுறைச் சட்ட விதி) பட்டியல்-II உடன் (சட்ட அதிகாரிகளுக்கான செயல்பாடு) பொருத்துக:",
         [("a. Order XXVII CPC", "1. Suits by or against the Government"),
          ("b. Order XXVIIA CPC", "2. Notice to AG when Central Act validity is challenged"),
          ("c. Order IV SC Rules", "3. Exemption of AG from Advocate-on-Record rules"),
          ("d. Order XXXVIII SC Rules", "4. AG notice in Presidential election petitions")],
         [("a. உத்தரவு XXVII CPC", "1. அரசு தொடுக்கும் அல்லது அரசுக்கு எதிரான வழக்குகள்"),
          ("b. உத்தரவு XXVIIA CPC", "2. மத்திய சட்டத்தின் செல்லுபடி சவாலுக்கு வரும்போது AG-க்கு நோட்டீஸ்"),
          ("c. உத்தரவு IV SC விதிகள்", "3. AoR விதிகளிலிருந்து AG-க்கு விலக்கு"),
          ("d. உத்தரவு XXXVIII SC விதிகள்", "4. குடியரசுத் தலைவர் தேர்தல் வழக்குகளில் AG-க்கு நோட்டீஸ்")]),

        # 88: Landmark Amendments
        ("Constitutional Amendments Defended",
         "Match List-I (Constitutional Amendment) with List-II (Case where AG Defended it):",
         "பட்டியல்-I-ஐ (அரசியலமைப்புத் திருத்தம்) பட்டியல்-II உடன் (AG அதை ஆதரித்து வாதாடிய வழக்கு) பொருத்துக:",
         [("a. 1st Amendment Act, 1951", "1. Shankari Prasad v. Union of India"),
          ("b. 24th & 25th Amendments, 1971", "2. Kesavananda Bharati v. State of Kerala"),
          ("c. 39th Amendment Act, 1975", "3. Indira Nehru Gandhi v. Raj Narain"),
          ("d. 99th Amendment Act, 2014", "4. Supreme Court Advocates-on-Record Association (NJAC)")],
         [("a. 1-வது திருத்தச் சட்டம், 1951", "1. சங்கரி பிரசாத் எதிர் இந்திய ஒன்றியம்"),
          ("b. 24 & 25-வது திருத்தங்கள், 1971", "2. கேசவானந்த பாரதி எதிர் கேரள அரசு"),
          ("c. 39-வது திருத்தச் சட்டம், 1975", "3. இந்திரா நேரு காந்தி எதிர் ராஜ் நாராயணன்"),
          ("d. 99-வது திருத்தச் சட்டம், 2014", "4. SCAORA வழக்கு (NJAC வழக்கு)")]),

        # 89: Decades of AGs
        ("Decades of Service",
         "Match List-I (Decade) with List-II (Prominent Attorney General):",
         "பட்டியல்-I-ஐ (பத்தாண்டு காலம்) பட்டியல்-II உடன் (முக்கிய தலைமை வழக்கறிஞர்) பொருத்துக:",
         [("a. 1950s", "1. M.C. Setalvad"),
          ("b. 1970s", "2. Niren De"),
          ("c. 1980s", "3. K. Parasaran"),
          ("d. 2020s", "4. R. Venkataramani")],
         [("a. 1950-கள்", "1. எம்.சி. செடல்வாட்"),
          ("b. 1970-கள்", "2. நீரேன் டே"),
          ("c. 1980-கள்", "3. கே. பராசரன்"),
          ("d. 2020-கள்", "4. ஆர். வெங்கடரமணி")]),

        # 90: Disciplinary & Professional Bodies
        ("Professional Bodies",
         "Match List-I (Body / Office) with List-II (Statutory Role):",
         "பட்டியல்-I-ஐ (அமைப்பு / அலுவலகம்) பட்டியல்-II உடன் (சட்டப்பூர்வப் பங்கு) பொருத்துக:",
         [("a. Bar Council of India", "1. Apex statutory regulator of legal profession"),
          ("b. Attorney General of India", "2. Statutory ex-officio member of BCI and leader of Bar"),
          ("c. Central Agency Section", "3. Administrative litigation arm in Supreme Court"),
          ("d. Department of Legal Affairs", "4. Ministry department coordinating legal advice")],
         [("a. இந்திய பார் கவுன்சில்", "1. வழக்கறிஞர் தொழிலின் உச்சக்கட்ட சட்ட ஒழுங்குமுறை அமைப்பு"),
          ("b. இந்திய தலைமை வழக்கறிஞர்", "2. பார் கவுன்சிலின் பதவி வழி உறுப்பினர் மற்றும் பார் தலைவர்"),
          ("c. மத்திய ஏஜென்சி பிரிவு", "3. உச்ச நீதிமன்றத்தில் வழக்குகளை நடத்தும் நிர்வாகப் பிரிவு"),
          ("d. சட்ட விவகாரங்கள் துறை", "4. சட்ட ஆலோசனைகளை ஒருங்கிணைக்கும் அமைச்சகத் துறை")])
    ]

    for i, item in enumerate(match_items):
        qid = f"AG_GT_{76+i:03d}"
        subtopic, t_en, t_ta, l1_en, l1_ta = item

        stem_en = f"{t_en}\nList-I:\n" + "\n".join(f"{a}" for a, b in l1_en) + "\nList-II:\n" + "\n".join(f"{b}" for a, b in l1_en)
        stem_ta = f"{t_ta}\nபட்டியல்-I:\n" + "\n".join(f"{a}" for a, b in l1_ta) + "\nபட்டியல்-II:\n" + "\n".join(f"{b}" for a, b in l1_ta)

        opts_perms = [
            "a-1, b-2, c-3, d-4",
            "a-2, b-1, c-4, d-3",
            "a-3, b-4, c-1, d-2",
            "a-4, b-3, c-2, d-1"
        ]

        why_en = {
            "A": "Option A correctly matches all pairs between List-I and List-II.",
            "B": "Option B contains mismatched pairs.",
            "C": "Option C contains mismatched pairs.",
            "D": "Option D contains mismatched pairs."
        }
        why_ta = {
            "A": "தெரிவு A பட்டியல்-I மற்றும் பட்டியல்-II இடையிலான அனைத்து இணைகளையும் சரியாகப் பொருத்துகிறது.",
            "B": "தெரிவு B தவறாகப் பொருத்தப்பட்ட இணைகளைக் கொண்டுள்ளது.",
            "C": "தெரிவு C தவறாகப் பொருத்தப்பட்ட இணைகளைக் கொண்டுள்ளது.",
            "D": "தெரிவு D தவறாகப் பொருத்தப்பட்ட இணைகளைக் கொண்டுள்ளது."
        }

        q = make_ag_q(
            qid=qid,
            diff="Medium",
            qtype="Match the Following",
            subtopic=subtopic,
            en_stem=stem_en, ta_stem=stem_ta,
            en_a=opts_perms[0], ta_a=opts_perms[0],
            en_b=opts_perms[1], ta_b=opts_perms[1],
            en_c=opts_perms[2], ta_c=opts_perms[2],
            en_d=opts_perms[3], ta_d=opts_perms[3],
            correct_key="A",
            exp_en=f"Correct matching is a-1, b-2, c-3, d-4 based on constitutional provisions and statutory frameworks.",
            exp_ta=f"அரசியலமைப்பு மற்றும் சட்ட விதிகளின்படி சரியான பொருத்தம் a-1, b-2, c-3, d-4 ஆகும்.",
            why_a_en=why_en["A"], why_a_ta=why_ta["A"],
            why_b_en=why_en["B"], why_b_ta=why_ta["B"],
            why_c_en=why_en["C"], why_c_ta=why_ta["C"],
            why_d_en=why_en["D"], why_d_ta=why_ta["D"],
            tip_en="Check matching pairs systematically to identify the unique correct code.",
            tip_ta="பொருத்தங்களை முறையாகச் சரிபார்த்து சரியான குறியீட்டைத் தேர்வு செய்யவும்.",
            fact_en="Standard TNPSC matching format.",
            fact_ta="நிலையான TNPSC பொருத்த வடிவமைப்பு.",
            tags=["polity", "attorney_general", "match_the_following"]
        )
        questions.append(q)

    # -------------------------------------------------------------
    # 10 Chronology MCQs (AG_GT_091 to AG_GT_100)
    # -------------------------------------------------------------

    chron_items = [
        # 91: Early AGs
        ("Early AG Appointments",
         "Arrange the appointments of the following early Attorneys General in chronological order:",
         "பின்வரும் ஆரம்பகால தலைமை வழக்கறிஞர்களின் நியமனங்களை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
         [("M.C. Setalvad appointed as AG", "எம்.சி. செடல்வாட் AG-யாக நியமிக்கப்படுதல்", 1950),
          ("C.K. Daphtary appointed as AG", "சி.கே. தப்தாரி AG-யாக நியமிக்கப்படுதல்", 1963),
          ("Niren De appointed as AG", "நீரேன் டே AG-யாக நியமிக்கப்படுதல்", 1968),
          ("S.V. Gupte appointed as AG", "எஸ்.வி. குப்தே AG-யாக நியமிக்கப்படுதல்", 1977)],
         [3, 1, 4, 2]), # 1968, 1950, 1977, 1963 -> sorted: 1950(2), 1963(4), 1968(1), 1977(3) -> 2 - 4 - 1 - 3

        # 92: 1980s AGs
        ("1980s AG Appointments",
         "Arrange the following Attorneys General in chronological order of appointment:",
         "பின்வரும் தலைமை வழக்கறிஞர்களை அவர்கள் நியமிக்கப்பட்ட காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
         [("L.N. Sinha appointed as AG", "எல்.என். சின்ஹா AG-யாக நியமிக்கப்படுதல்", 1979),
          ("K. Parasaran appointed as AG", "கே. பராசரன் AG-யாக நியமிக்கப்படுதல்", 1983),
          ("Soli Sorabjee appointed as AG (1st term)", "சோலி சொராப்ஜி (முதல் முறை) AG-யாக நியமிக்கப்படுதல்", 1989),
          ("G. Ramaswamy appointed as AG", "ஜி. ராமசுவாமி AG-யாக நியமிக்கப்படுதல்", 1990)],
         [2, 4, 1, 3]), # 1983, 1990, 1979, 1989 -> sorted: 1979(3), 1983(1), 1989(4), 1990(2) -> 3 - 1 - 4 - 2

        # 93: 1990s-2000s AGs
        ("1990s-2000s AG Appointments",
         "Arrange the tenures of the following Attorneys General in chronological order:",
         "பின்வரும் தலைமை வழக்கறிஞர்களின் பதவிக்காலங்களை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
         [("Ashok Desai appointed as AG", "அசோக் தேசாய் AG-யாக நியமிக்கப்படுதல்", 1996),
          ("Soli Sorabjee appointed as AG (2nd term)", "சோலி சொராப்ஜி (2-வது முறை) AG-யாக நியமிக்கப்படுதல்", 1998),
          ("Milon K. Banerjee appointed as AG (2nd term)", "மிலன் கே. பானர்ஜி (2-வது முறை) AG-யாக நியமிக்கப்படுதல்", 2004),
          ("G.E. Vahanvati appointed as AG", "ஜி.இ. வாகனவதி AG-யாக நியமிக்கப்படுதல்", 2009)],
         [3, 1, 4, 2]), # 2004, 1996, 2009, 1998 -> sorted: 1996(2), 1998(4), 2004(1), 2009(3) -> 2 - 4 - 1 - 3

        # 94: Modern AGs
        ("Modern AG Appointments (2009-2022)",
         "Arrange the appointments of the following modern Attorneys General in chronological order:",
         "பின்வரும் நவீன தலைமை வழக்கறிஞர்களின் நியமனங்களை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
         [("G.E. Vahanvati appointed as AG", "ஜி.இ. வாகனவதி AG-யாக நியமிக்கப்படுதல்", 2009),
          ("Mukul Rohatgi appointed as AG", "முகுல் ரோஹத்கி AG-யாக நியமிக்கப்படுதல்", 2014),
          ("K.K. Venugopal appointed as AG", "கே.கே. வேணுகோபால் AG-யாக நியமிக்கப்படுதல்", 2017),
          ("R. Venkataramani appointed as AG", "ஆர். வெங்கடரமணி AG-யாக நியமிக்கப்படுதல்", 2022)],
         [4, 2, 1, 3]), # 2022, 2014, 2009, 2017 -> sorted: 2009(3), 2014(2), 2017(4), 2022(1) -> 3 - 2 - 4 - 1

        # 95: Constitutional Cases (1950-1973)
        ("Landmark Cases (1950-1973)",
         "Arrange the following landmark Supreme Court cases argued by early Attorneys General in chronological order:",
         "ஆரம்பகால தலைமை வழக்கறிஞர்களால் வாதிடப்பட்ட பின்வரும் வரலாற்று வழக்குகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
         [("A.K. Gopalan v. State of Madras", "ஏ.கே. கோபாலன் எதிர் மதராஸ் மாகாணம்", 1950),
          ("In re Berubari Union Reference", "பெருபாரி யூனியன் குறிப்புரை", 1960),
          ("Golaknath v. State of Punjab", "கோலாக்நாத் எதிர் பஞ்சாப் அரசு", 1967),
          ("Kesavananda Bharati v. State of Kerala", "கேசவானந்த பாரதி எதிர் கேரள அரசு", 1973)],
         [4, 1, 3, 2]), # 1973, 1950, 1967, 1960 -> sorted: 1950(2), 1960(4), 1967(3), 1973(1) -> 2 - 4 - 3 - 1

        # 96: Landmark Cases (1975-1994)
        ("Landmark Cases (1975-1994)",
         "Arrange the following historic cases involving the Union of India in chronological order:",
         "மத்திய அரசு சம்பந்தப்பட்ட பின்வரும் வரலாற்று வழக்குகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
         [("Indira Gandhi v. Raj Narain (Election case)", "இந்திரா காந்தி எதிர் ராஜ் நாராயணன் (தேர்தல் வழக்கு)", 1975),
          ("ADM Jabalpur v. Shivkant Shukla (Habeas Corpus case)", "ஏ.டி.எம். ஜபல்பூர் எதிர் சிவகாந்த் சுக்லா (ஆட்கொணர்வு வழக்கு)", 1976),
          ("Minerva Mills v. Union of India", "மினர்வா மில்ஸ் எதிர் இந்திய ஒன்றியம்", 1980),
          ("S.R. Bommai v. Union of India", "எஸ்.ஆர். பொம்மை எதிர் இந்திய ஒன்றியம்", 1994)],
         [2, 4, 1, 3]), # 1976, 1994, 1975, 1980 -> sorted: 1975(3), 1976(1), 1980(4), 1994(2) -> 3 - 1 - 4 - 2

        # 97: Article 143 References
        ("Presidential References",
         "Arrange the following Presidential references under Article 143 in chronological order:",
         "சரத்து 143-ன் கீழ் உள்ள பின்வரும் குடியரசுத் தலைவர் குறிப்புரைகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
         [("In re Delhi Laws Act Reference", "தில்லி சட்டங்கள் சட்டம் குறிப்புரை", 1951),
          ("In re Berubari Union Reference", "பெருபாரி யூனியன் குறிப்புரை", 1960),
          ("In re Special Courts Bill Reference", "சிறப்பு நீதிமன்றங்கள் மசோதா குறிப்புரை", 1978),
          ("In re 2G Spectrum Allocation Reference", "2ஜி அலைக்கற்றை ஒதுக்கீடு குறிப்புரை", 2012)],
         [3, 1, 4, 2]), # 1978, 1951, 2012, 1960 -> sorted: 1951(2), 1960(4), 1978(1), 2012(3) -> 2 - 4 - 1 - 3

        # 98: Emergency to Privacy Evolution
        ("Emergency to Privacy Evolution",
         "Arrange the following constitutional milestones regarding Article 21 in chronological order:",
         "சரத்து 21 தொடர்பான பின்வரும் அரசியலமைப்பு மைல்கற்களை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
         [("Internal Emergency proclaimed under Article 352", "சரத்து 352-ன் கீழ் உள்நாட்டு அவசரநிலை பிரகடனம்", 1975),
          ("ADM Jabalpur ruling upholding Article 21 suspension", "சரத்து 21 இடைநிறுத்தத்தை உறுதி செய்த ஜபல்பூர் தீர்ப்பு", 1976),
          ("44th Amendment Act protecting Article 21 from suspension", "சரத்து 21-ஐப் பாதுகாக்கும் 44-வது திருத்தச் சட்டம்", 1978),
          ("K.S. Puttaswamy judgment overruling ADM Jabalpur", "ஜபல்பூர் தீர்ப்பை ரத்து செய்த புட்டசாமி தீர்ப்பு", 2017)],
         [4, 2, 1, 3]), # 2017, 1976, 1975, 1978 -> sorted: 1975(3), 1976(2), 1978(4), 2017(1) -> 3 - 2 - 4 - 1

        # 99: Statutory Milestones
        ("Statutory & Institutional Milestones",
         "Arrange the following institutional events in chronological order:",
         "பின்வரும் நிறுவன நிகழ்வுகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
         [("Establishment of the First Law Commission under M.C. Setalvad", "எம்.சி. செடல்வாட் தலைமையில் முதலாவது சட்ட ஆணையம் அமைத்தல்", 1955),
          ("Enactment of the Advocates Act granting pre-audience", "முதன்மை வாதாடும் உரிமை வழங்கும் வழக்கறிஞர்கள் சட்டம் இயற்றப்படுதல்", 1961),
          ("Enactment of the Contempt of Courts Act requiring AG consent", "AG ஒப்புதலைக் கட்டாயமாக்கும் நீதிமன்ற அவமதிப்புச் சட்டம் இயற்றப்படுதல்", 1971),
          ("Notification of the Law Officers (Conditions of Service) Rules", "சட்ட அதிகாரிகள் (பணி நிபந்தனைகள்) விதிகள் அறிவிக்கப்படுதல்", 1987)],
         [3, 4, 1, 2]), # 1971, 1987, 1955, 1961 -> sorted: 1955(3), 1961(4), 1971(1), 1987(2) -> 3 - 4 - 1 - 2

        # 100: Verdicts under R. Venkataramani
        ("Verdicts under R. Venkataramani (2022-2024)",
         "Arrange the following landmark Supreme Court Constitution Bench verdicts in chronological order:",
         "பின்வரும் முக்கிய உச்ச நீதிமன்ற அரசியலமைப்பு அமர்வு தீர்ப்புகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
         [("Janki Janhit verdict upholding 103rd Amendment (EWS Quota)", "103-வது திருத்தத்தை (EWS) உறுதி செய்த ஜன்கி ஜன்ஹித் தீர்ப்பு", 2022),
          ("Supriyo verdict on Same-Sex Marriage", "ஒரே பாலின திருமணம் தொடர்பான சுப்ரியோ தீர்ப்பு", 2023),
          ("Verdict unanimously upholding Abrogation of Article 370", "சரத்து 370 ரத்தை ஒருமனதாக உறுதி செய்த தீர்ப்பு", 2023),
          ("Association for Democratic Reforms verdict striking down Electoral Bonds", "தேர்தல் பத்திரங்களை ரத்து செய்த ADR தீர்ப்பு", 2024)],
         [4, 1, 3, 2]) # 2024, 2022, 2023(Dec), 2023(Oct) -> sorted: 2022(2), Oct 2023(4), Dec 2023(3), Feb 2024(1) -> 2 - 4 - 3 - 1
    ]

    all_perms = [
        [1, 2, 3, 4], [1, 2, 4, 3], [1, 3, 2, 4], [1, 3, 4, 2], [1, 4, 2, 3], [1, 4, 3, 2],
        [2, 1, 3, 4], [2, 1, 4, 3], [2, 3, 1, 4], [2, 3, 4, 1], [2, 4, 1, 3], [2, 4, 3, 1],
        [3, 1, 2, 4], [3, 1, 4, 2], [3, 2, 1, 4], [3, 2, 4, 1], [3, 4, 1, 2], [3, 4, 2, 1],
        [4, 1, 2, 3], [4, 1, 3, 2], [4, 2, 1, 3], [4, 2, 3, 1], [4, 3, 1, 2], [4, 3, 2, 1]
    ]

    for i, c_item in enumerate(chron_items):
        qid = f"AG_GT_{91+i:03d}"
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
        random.seed(100 + i)
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
        for step in sorted_meta:
            exp_lines_en.append(f"{step[0]}. {step[2]} ({step[4]})")
            exp_lines_ta.append(f"{step[0]}. {step[3]} ({step[4]})")

        exp_en = "\n".join(exp_lines_en)
        exp_ta = "\n".join(exp_lines_ta)

        why_en = {
            "A": f"Option A ({en_options[0]}) accurately reflects the historical progression: {' -> '.join(str(d) for d in correct_seq)}.",
            "B": f"Option B ({en_options[1]}) is incorrect.",
            "C": f"Option C ({en_options[2]}) is incorrect.",
            "D": f"Option D ({en_options[3]}) is incorrect."
        }
        why_ta = {
            "A": f"தெரிவு A ({ta_options[0]}) வரலாற்று வரிசையைத் துல்லியமாகப் பிரதிபலிக்கிறது: {' -> '.join(str(d) for d in correct_seq)}.",
            "B": f"தெரிவு B ({ta_options[1]}) தவறானது.",
            "C": f"தெரிவு C ({ta_options[2]}) தவறானது.",
            "D": f"தெரிவு D ({ta_options[3]}) தவறானது."
        }

        q = make_ag_q(
            qid=qid,
            diff="Hard",
            qtype="Chronology",
            subtopic=subtopic,
            en_stem=stem_en, ta_stem=stem_ta,
            en_a=en_options[0], ta_a=ta_options[0],
            en_b=en_options[1], ta_b=ta_options[1],
            en_c=en_options[2], ta_c=ta_options[2],
            en_d=en_options[3], ta_d=ta_options[3],
            correct_key="A",
            exp_en=exp_en, exp_ta=exp_ta,
            why_a_en=why_en["A"], why_a_ta=why_ta["A"],
            why_b_en=why_en["B"], why_b_ta=why_ta["B"],
            why_c_en=why_en["C"], why_c_ta=why_ta["C"],
            why_d_en=why_en["D"], why_d_ta=why_ta["D"],
            tip_en="Always memorize the sequential tenures and landmark constitutional cases of Attorneys General!",
            tip_ta="தலைமை வழக்கறிஞர்களின் தொடர்ச்சியான பதவிக்காலங்கள் மற்றும் முக்கிய வழக்குகளை எப்போதும் நினைவில் வையுங்கள்!",
            fact_en=f"Sequence: {' -> '.join(str(d) for d in correct_seq)} reflects historical progression.",
            fact_ta=f"வரிசை: {' -> '.join(str(d) for d in correct_seq)} வரலாற்று முன்னேற்றத்தைக் காட்டுகிறது.",
            tags=["polity", "attorney_general", "chronology"]
        )
        questions.append(q)

    return questions
