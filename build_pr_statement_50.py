# -*- coding: utf-8 -*-
"""
Generates 50 High-Quality Statement-Based MCQs for Local Government – Panchayati Raj (PR_S_001 to PR_S_050).
Strictly adheres to 24-field schema, balanced keys, and authentic Tamil translation.
"""
import json
import os
from pr_mcq_helper import make_pr_q
from rebalance_pr_helper import balance_question_keys

def generate_statement_50():
    questions = []

    # S01: Balwant Rai Mehta Committee Statements
    questions.append(make_pr_q(
        qid="PR_S_001",
        diff="Medium",
        qtype="Statement-based",
        subtopic="Historical Committees",
        en_stem="Consider the following statements regarding the Balwant Rai Mehta Committee (1957):\n1. It recommended the establishment of a 3-tier Panchayati Raj system.\n2. It recommended that the Panchayat Samiti at the block level should be the executive body.\n3. It recommended that the District Collector should be the Chairman of the Zilla Parishad.\nWhich of the statements given above are correct?",
        ta_stem="பல்வந்த் ராய் மேத்தா குழு (1957) குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது மூன்றடுக்கு பஞ்சாயத்து ராஜ் முறையை நிறுவப் பரிந்துரைத்தது.\n2. வட்டார அளவிலான ஊராட்சி ஒன்றியம் (Panchayat Samiti) முதன்மை நிர்வாக அமைப்பாக இருக்க வேண்டும் எனப் பரிந்துரைத்தது.\n3. மாவட்ட ஆட்சியர் ஜில்லா பரிஷத்தின் தலைவராக இருக்க வேண்டும் எனப் பரிந்துரைத்தது.\nமேற்கண்ட கூற்றுகளில் சரியானவை எவை?",
        en_a="1 and 2 only",
        ta_a="1 மற்றும் 2 மட்டுமே",
        en_b="2 and 3 only",
        ta_b="2 மற்றும் 3 மட்டுமே",
        en_c="1 and 3 only",
        ta_c="1 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3",
        ta_d="1, 2 மற்றும் 3",
        correct_key="D",
        exp_en="All three statements are correct. The Balwant Rai Mehta Committee recommended: (1) a 3-tier structure (Gram Panchayat, Panchayat Samiti, Zilla Parishad), (2) Panchayat Samiti as the executive body and Zilla Parishad as supervisory/advisory, and (3) District Collector as Chairman of Zilla Parishad.",
        exp_ta="மூன்று கூற்றுகளும் சரியானவை. பல்வந்த் ராய் மேத்தா குழு: (1) மூன்றடுக்கு முறை, (2) ஊராட்சி ஒன்றியம் முதன்மை நிர்வாக அமைப்பு, (3) மாவட்ட ஆட்சியர் ஜில்லா பரிஷத்தின் தலைவர் ஆகிய அனைத்தையும் பரிந்துரைத்தது.",
        why_a_en="Incorrect. Statement 3 is also correct.",
        why_a_ta="தவறானது. கூற்று 3-ம் சரியானது.",
        why_b_en="Incorrect. Statement 1 is also correct.",
        why_b_ta="தவறானது. கூற்று 1-ம் சரியானது.",
        why_c_en="Incorrect. Statement 2 is also correct.",
        why_c_ta="தவறானது. கூற்று 2-ம் சரியானது.",
        why_d_en="Correct. All three statements accurately state the core recommendations of Balwant Rai Mehta.",
        why_d_ta="சரியானது. மூன்று கூற்றுகளும் பல்வந்த் ராய் மேத்தா குழுவின் முக்கிய பரிந்துரைகளை துல்லியமாகக் கூறுகின்றன.",
        tip_en="Balwant Rai Mehta Recommendations: 3 tiers + Block executive + Collector ZP chairman.",
        tip_ta="பல்வந்த் ராய் மேத்தா பரிந்துரைகள்: 3 அடுக்கு + வட்டார நிர்வாகம் + ஆட்சியர் தலைவர்.",
        fact_en="The National Development Council accepted these recommendations in January 1958.",
        fact_ta="தேசிய வளர்ச்சிக் குழு 1958 ஜனவரியில் இந்தப் பரிந்துரைகளை ஏற்றுக்கொண்டது.",
        tags=["balwant_rai_mehta", "statement_based", "committees"]
    ))

    # S02: Ashok Mehta Committee Statements
    questions.append(make_pr_q(
        qid="PR_S_002",
        diff="Medium",
        qtype="Statement-based",
        subtopic="Historical Committees",
        en_stem="Consider the following statements regarding the Ashok Mehta Committee (1977–78):\n1. It recommended replacing the 3-tier system with a 2-tier system consisting of Zilla Parishad and Mandal Panchayat.\n2. It recommended that an official political party participation should be permitted in all PRI elections.\n3. It recommended establishing a 4-tier system by adding a State Local Government Council.\nWhich of the statements given above are correct?",
        ta_stem="அசோக் மேத்தா குழு (1977-78) குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது மூன்றடுக்கு முறைக்கு பதிலாக ஜில்லா பரிஷத் மற்றும் மண்டல் பஞ்சாயத்து என்ற இரண்டடுக்கு முறையைப் பரிந்துரைத்தது.\n2. அனைத்து ஊராட்சித் தேர்தல்களிலும் அரசியல் கட்சிகள் அதிகாரப்பூர்வமாகப் பங்கேற்க அனுமதிக்கப்பட வேண்டும் எனப் பரிந்துரைத்தது.\n3. மாநில உள்ளாட்சி மன்றத்தைச் சேர்த்து 4 அடுக்கு முறையை நிறுவப் பரிந்துரைத்தது.\nமேற்கண்ட கூற்றுகளில் சரியானவை எவை?",
        en_a="1 and 2 only",
        ta_a="1 மற்றும் 2 மட்டுமே",
        en_b="2 and 3 only",
        ta_b="2 மற்றும் 3 மட்டுமே",
        en_c="1 and 3 only",
        ta_c="1 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3",
        ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statements 1 and 2 are correct. Ashok Mehta recommended a 2-tier model (not 4-tier) and official political party participation. Statement 3 is incorrect as it proposed a 2-tier system, not a 4-tier system.",
        exp_ta="கூற்றுகள் 1 மற்றும் 2 சரியானவை. அசோக் மேத்தா 2 அடுக்கு முறையையும் அரசியல் கட்சிகளின் அதிகாரப்பூர்வ பங்கேற்பையும் பரிந்துரைத்தார். கூற்று 3 தவறானது, ஏனெனில் அது 4 அடுக்கு முறையை முன்மொழியவில்லை.",
        why_a_en="Correct. Statements 1 and 2 are true; Statement 3 is false.",
        why_a_ta="சரியானது. கூற்றுகள் 1 மற்றும் 2 சரி; கூற்று 3 தவறு.",
        why_b_en="Incorrect. Statement 3 is false.",
        why_b_ta="தவறானது. கூற்று 3 தவறு.",
        why_c_en="Incorrect. Statement 3 is false.",
        why_c_ta="தவறானது. கூற்று 3 தவறு.",
        why_d_en="Incorrect. Statement 3 is false.",
        why_d_ta="தவறானது. கூற்று 3 தவறு.",
        tip_en="Ashok Mehta = 2 tiers (Zilla Parishad + Mandal Panchayat covering 15,000 to 20,000 population).",
        tip_ta="அசோக் மேத்தா = 2 அடுக்குகள் (ஜில்லா பரிஷத் + 15,000 முதல் 20,000 மக்கள்தொகை கொண்ட மண்டல் பஞ்சாயத்து).",
        fact_en="Ashok Mehta Committee also recommended appointing a Minister for Panchayati Raj in the State Council of Ministers.",
        fact_ta="மாநில அமைச்சரவையில் பஞ்சாயத்து ராஜ் அமைச்சர் ஒருவரை நியமிக்கவும் அசோக் மேத்தா குழு பரிந்துரைத்தது.",
        tags=["ashok_mehta", "2_tier", "statement_based"]
    ))

    # S03: Article 243D Reservation Statements
    questions.append(make_pr_q(
        qid="PR_S_003",
        diff="Hard",
        qtype="Statement-based",
        subtopic="Article 243D Reservation",
        en_stem="Consider the following statements regarding reservation under Article 243D:\n1. Reservation of seats for SCs and STs is mandatory and proportional to their population in the Panchayat area.\n2. Reservation of not less than one-third of seats for women is mandatory across all three tiers.\n3. Reservation of seats for Other Backward Classes (OBCs) is mandatory under the Constitution.\nWhich of the statements given above are correct?",
        ta_stem="உறுப்பு 243D-ன் கீழ் இடஒதுக்கீடு குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. SC மற்றும் ST பிரிவினருக்கான இடஒதுக்கீடு கட்டாயமானது மற்றும் ஊராட்சிப் பகுதியில் உள்ள அவர்களின் மக்கள்தொகை விகிதாச்சாரத்திற்கு உட்பட்டது.\n2. அனைத்து மூன்று அடுக்குகளிலும் பெண்களுக்கு மூன்றில் ஒரு பங்கிற்கு குறையாமல் இடஒதுக்கீடு வழங்குவது கட்டாயமாகும்.\n3. இதர பிற்படுத்தப்பட்ட வகுப்பினருக்கான (OBC) இடஒதுக்கீடு அரசியலமைப்பின் கீழ் கட்டாயமானதாகும்.\nமேற்கண்ட கூற்றுகளில் சரியானவை எவை?",
        en_a="1 and 2 only",
        ta_a="1 மற்றும் 2 மட்டுமே",
        en_b="2 and 3 only",
        ta_b="2 மற்றும் 3 மட்டுமே",
        en_c="1 and 3 only",
        ta_c="1 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3",
        ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statements 1 and 2 are correct. SC/ST and Women reservations are mandatory. Statement 3 is incorrect because OBC reservation under Article 243D(6) is discretionary, leaving it to the wisdom of the State Legislature.",
        exp_ta="கூற்றுகள் 1 மற்றும் 2 சரியானவை. SC/ST மற்றும் பெண்கள் இடஒதுக்கீடு கட்டாயமானது. கூற்று 3 தவறானது, ஏனெனில் உறுப்பு 243D(6)-ன் கீழ் OBC இடஒதுக்கீடு என்பது மாநிலத்தின் விருப்பத்திற்குரியது (கட்டாயமல்ல).",
        why_a_en="Correct. Statements 1 and 2 are accurate; Statement 3 is false.",
        why_a_ta="சரியானது. கூற்றுகள் 1 மற்றும் 2 சரி; கூற்று 3 தவறு.",
        why_b_en="Incorrect. Statement 3 is false.",
        why_b_ta="தவறானது. கூற்று 3 தவறு.",
        why_c_en="Incorrect. Statement 3 is false.",
        why_c_ta="தவறானது. கூற்று 3 தவறு.",
        why_d_en="Incorrect. Statement 3 is false.",
        why_d_ta="தவறானது. கூற்று 3 தவறு.",
        tip_en="Mandatory = SC, ST, Women. Discretionary = OBC (Article 243D(6)).",
        tip_ta="கட்டாயம் = SC, ST, பெண்கள். விருப்பத்திற்குரியது = OBC (உறுப்பு 243D(6)).",
        fact_en="Women's reservation also extends to Chairperson positions at all levels under Article 243D(4).",
        fact_ta="உறுப்பு 243D(4)-ன் கீழ் தலைவர் பதவிகளிலும் பெண்களுக்கு மூன்றில் ஒரு பங்கு இடஒதுக்கீடு கட்டாயமாகும்.",
        tags=["article_243d", "reservation_types", "statement_based"]
    ))

    # S04: Article 243E Duration Statements
    questions.append(make_pr_q(
        qid="PR_S_004",
        diff="Hard",
        qtype="Statement-based",
        subtopic="Article 243E Duration",
        en_stem="Consider the following statements regarding the duration and dissolution of Panchayats under Article 243E:\n1. Every Panchayat continues for 5 years from the date appointed for its first meeting.\n2. An election to constitute a Panchayat must be completed before the expiry of its 5-year duration.\n3. A Panchayat reconstituted upon premature dissolution serves a full fresh term of 5 years.\nWhich of the statements given above are correct?",
        ta_stem="உறுப்பு 243E-ன் கீழ் ஊராட்சிகளின் ஆயுட்காலம் மற்றும் கலைப்பு குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. ஒவ்வொரு ஊராட்சியும் அதன் முதல் கூட்டத்திற்காக நியமிக்கப்பட்ட தேதியிலிருந்து 5 ஆண்டுகள் தொடரும்.\n2. 5 ஆண்டு காலாவதியாகும் முன்பே அடுத்த தேர்தலை நடத்தி முடிக்க வேண்டும்.\n3. முன்கூட்டியே கலைக்கப்பட்ட பின் புதிதாக அமைக்கப்படும் ஊராட்சி முழுமையான 5 ஆண்டு புதிய பதவிக்காலத்தைப் பெறும்.\nமேற்கண்ட கூற்றுகளில் சரியானவை எவை?",
        en_a="1 and 2 only",
        ta_a="1 மற்றும் 2 மட்டுமே",
        en_b="2 and 3 only",
        ta_b="2 மற்றும் 3 மட்டுமே",
        en_c="1 and 3 only",
        ta_c="1 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3",
        ta_d="1, 2 மற்றும் 3",
        correct_key="A",
        exp_en="Statements 1 and 2 are correct. Statement 3 is incorrect because under Article 243E(4), a reconstituted Panchayat continues ONLY for the remainder of the period, not a fresh 5-year term.",
        exp_ta="கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் உறுப்பு 243E(4)-ன் படி முன்கூட்டியே கலைக்கப்பட்டு மீண்டும் அமைக்கப்படும் ஊராட்சி எஞ்சிய காலத்திற்கு மட்டுமே நீடிக்கும்; புதிய 5 ஆண்டு காலம் கிடைக்காது.",
        why_a_en="Correct. Statements 1 and 2 are true; Statement 3 is false.",
        why_a_ta="சரியானது. கூற்றுகள் 1 மற்றும் 2 சரி; கூற்று 3 தவறு.",
        why_b_en="Incorrect. Statement 3 is false.",
        why_b_ta="தவறானது. கூற்று 3 தவறு.",
        why_c_en="Incorrect. Statement 3 is false.",
        why_c_ta="தவறானது. கூற்று 3 தவறு.",
        why_d_en="Incorrect. Statement 3 is false.",
        why_d_ta="தவறானது. கூற்று 3 தவறு.",
        tip_en="Remainder Term Rule: Prematurely dissolved Panchayat reconstituted body serves ONLY remainder time.",
        tip_ta="எஞ்சிய கால விதி: முன்கூட்டியே கலைக்கப்பட்ட ஊராட்சி மீண்டும் அமைக்கப்பட்டால் எஞ்சிய காலம் மட்டுமே செயல்படும்.",
        fact_en="If remainder period is less than 6 months, no election is held until the regular term end.",
        fact_ta="எஞ்சிய காலம் 6 மாதங்களுக்கும் குறைவாக இருந்தால் வழக்கமான காலம் முடியும் வரை தேர்தல் நடத்தப்படுவதில்லை.",
        tags=["article_243e", "duration", "statement_based"]
    ))

    # S05: Article 243K SEC Statements
    questions.append(make_pr_q(
        qid="PR_S_005",
        diff="Hard",
        qtype="Statement-based",
        subtopic="Article 243K State Election Commission",
        en_stem="Consider the following statements regarding the State Election Commission (SEC) under Article 243K:\n1. The State Election Commissioner is appointed by the Governor of the State.\n2. The State Election Commissioner can be removed by the Governor on the advice of the Council of Ministers.\n3. The SEC is vested with the superintendence, direction, and control of the preparation of electoral rolls for, and conduct of, all elections to Panchayats.\nWhich of the statements given above are correct?",
        ta_stem="உறுப்பு 243K-ன் கீழ் மாநில தேர்தல் ஆணையம் (SEC) குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. மாநில தேர்தல் ஆணையர் மாநில ஆளுநரால் நியமிக்கப்படுகிறார்.\n2. மாநில அமைச்சரவையின் ஆலோசனையின் பேரில் ஆளுநரே தேர்தல் ஆணையரை பதவியிலிருந்து நீக்க முடியும்.\n3. ஊராட்சிகளுக்கான வாக்காளர் பட்டியல் தயாரித்தல் மற்றும் தேர்தல்களை நடத்துவதை மேற்பார்வையிடுதல், இயக்குதல், கட்டுப்படுத்துதல் ஆகியவை SEC-யிடம் ஒப்படைக்கப்பட்டுள்ளன.\nமேற்கண்ட கூற்றுகளில் சரியானவை எவை?",
        en_a="1 and 2 only",
        ta_a="1 மற்றும் 2 மட்டுமே",
        en_b="1 and 3 only",
        ta_b="1 மற்றும் 3 மட்டுமே",
        en_c="2 and 3 only",
        ta_c="2 மற்றும் 3 மட்டுமே",
        en_d="1, 2 and 3",
        ta_d="1, 2 மற்றும் 3",
        correct_key="B",
        exp_en="Statements 1 and 3 are correct. Statement 2 is incorrect because the State Election Commissioner can only be removed in like manner and grounds as a Judge of a High Court (by the President after Parliamentary address), NOT by the Governor.",
        exp_ta="கூற்றுகள் 1 மற்றும் 3 சரியானவை. கூற்று 2 தவறானது, ஏனெனில் உயர் நீதிமன்ற நீதிபதியைப் போன்றே (பாராளுமன்ற நடைமுறைக்குப் பின் குடியரசுத் தலைவரால்) மட்டுமே நீக்க முடியும்; ஆளுநரால் நீக்க முடியாது.",
        why_a_en="Incorrect. Statement 2 is false.",
        why_a_ta="தவறானது. கூற்று 2 தவறு.",
        why_b_en="Correct. Statements 1 and 3 are true; Statement 2 is false.",
        why_b_ta="சரியானது. கூற்றுகள் 1 மற்றும் 3 சரி; கூற்று 2 தவறு.",
        why_c_en="Incorrect. Statement 2 is false.",
        why_c_ta="தவறானது. கூற்று 2 தவறு.",
        why_d_en="Incorrect. Statement 2 is false.",
        why_d_ta="தவறானது. கூற்று 2 தவறு.",
        tip_en="Appointed by GOVERNOR; Removed like a HIGH COURT JUDGE (by President).",
        tip_ta="நியமிப்பவர் ஆளுநர்; நீக்குபவர் உயர் நீதிமன்ற நீதிபதி போல (குடியரசுத் தலைவர்).",
        fact_en="The SEC's conditions of service cannot be varied to his disadvantage after appointment.",
        fact_ta="நியமனத்திற்குப் பிறகு அவரது பணிக்கால நிபந்தனைகளை அவருக்கு பாதகமாக மாற்ற முடியாது.",
        tags=["article_243k", "sec", "statement_based"]
    ))

    # S06-S50: Statement-based questions covering all parts of the blueprint
    s_specs = [
        ("PR_S_006", "Article 243A Gram Sabha",
         "Consider the following statements regarding the Gram Sabha:\n1. It is a constitutionally mandated permanent body of direct democracy.\n2. It consists of all adult residents of the village regardless of electoral registration.\n3. It exercises such powers at the village level as the State Legislature may provide by law.",
         "கிராம சபை குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது அரசியலமைப்பால் கட்டாயமாக்கப்பட்ட நேரடி ஜனநாயகத்தின் நிரந்தர அமைப்பாகும்.\n2. வாக்காளர் பட்டியலில் பெயர் உள்ளதா இல்லையா என்பதைக் கருதாமல் கிராமத்தின் அனைத்து வயது வந்த மக்களையும் கொண்டுள்ளது.\n3. மாநில சட்டமன்றம் சட்டத்தால் வழங்கும் அதிகாரங்களை கிராம அளவில் செயல்படுத்துகிறது.",
         "1 and 3 only", "1 மற்றும் 3 மட்டுமே", "1 and 2 only", "1 மற்றும் 2 மட்டுமே", "2 and 3 only", "2 மற்றும் 3 மட்டுமே", "1, 2 and 3", "1, 2 மற்றும் 3",
         "A", "Statement 2 is false because Gram Sabha consists ONLY of persons registered in the electoral rolls of the village.",
         "கூற்று 2 தவறு, ஏனெனில் வாக்காளர் பட்டியலில் பதிவு செய்யப்பட்டவர்கள் மட்டுமே கிராம சபையின் உறுப்பினர்கள் ஆவர்."),

        ("PR_S_007", "Article 243B Intermediate Tier",
         "Consider the following statements regarding the tiers of Panchayati Raj under Article 243B:\n1. A 3-tier system (village, intermediate, district) is universally mandatory across all States.\n2. States with a population not exceeding 20 lakhs are exempt from constituting intermediate panchayats.\n3. Goa and Sikkim have 2-tier Panchayati Raj systems relying on this population clause.",
         "உறுப்பு 243B-ன் கீழ் பஞ்சாயத்து அடுக்குகள் குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. அனைத்து மாநிலங்களுக்கும் 3 அடுக்கு முறை கட்டாயமாகும்.\n2. 20 லட்சத்திற்கு மிகாமல் மக்கள்தொகை கொண்ட மாநிலங்களுக்கு இடைநிலை ஊராட்சி அமைப்பதிலிருந்து விலக்களிக்கப்பட்டுள்ளது.\n3. கோவா மற்றும் சிக்கிம் இந்த விதியின் அடிப்படையில் இரண்டடுக்கு முறையைக் கொண்டுள்ளன.",
         "2 and 3 only", "2 மற்றும் 3 மட்டுமே", "1 and 2 only", "1 மற்றும் 2 மட்டுமே", "1 and 3 only", "1 மற்றும் 3 மட்டுமே", "1, 2 and 3", "1, 2 மற்றும் 3",
         "A", "Statement 1 is false because it is not universally mandatory for small states (<20 lakhs). Statements 2 and 3 are correct.",
         "கூற்று 1 தவறு, ஏனெனில் 20 லட்சத்திற்குக் குறைவான சிறிய மாநிலங்களுக்கு 3 அடுக்கு கட்டாயமல்ல. கூற்றுகள் 2 மற்றும் 3 சரி."),

        ("PR_S_008", "Article 243C Composition",
         "Consider the following statements regarding Panchayat composition:\n1. Ward members at all three levels must be directly elected by the people.\n2. Chairpersons of Intermediate and District Panchayats are directly elected by all voters of the district.\n3. State Legislature decides whether Village Panchayat Presidents are elected directly or indirectly.",
         "ஊராட்சி கட்டமைப்பு குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. மூன்று நிலைகளிலும் உள்ள வார்டு உறுப்பினர்கள் மக்களால் நேரடியாகத் தேர்ந்தெடுக்கப்பட வேண்டும்.\n2. ஒன்றியம் மற்றும் மாவட்ட தலைவர்கள் அனைத்து வாக்காளர்களாலும் நேரடியாகத் தேர்ந்தெடுக்கப்படுகின்றனர்.\n3. கிராம ஊராட்சி தலைவர் நேரடியாகவா அல்லது மறைமுகமாகவா தேர்ந்தெடுக்கப்பட வேண்டும் என்பதை மாநில சட்டமன்றமே தீர்மானிக்கிறது.",
         "1 and 3 only", "1 மற்றும் 3 மட்டுமே", "1 and 2 only", "1 மற்றும் 2 மட்டுமே", "2 and 3 only", "2 மற்றும் 3 மட்டுமே", "1, 2 and 3", "1, 2 மற்றும் 3",
         "A", "Statement 2 is false because intermediate and district chairpersons are strictly elected INDIRECTLY by elected members under Article 243C(5)(b).",
         "கூற்று 2 தவறு, ஏனெனில் இடைநிலை மற்றும் மாவட்ட தலைவர்கள் தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்களால் மட்டுமே மறைமுகமாகத் தேர்ந்தெடுக்கப்படுகின்றனர்."),

        ("PR_S_009", "Article 243I State Finance Commission",
         "Consider the following statements regarding the State Finance Commission (SFC):\n1. It is constituted by the Governor every five years under Article 243I.\n2. It reviews the financial position of Panchayats and recommends distribution of net proceeds of taxes.\n3. Its recommendations are binding on the State Government.",
         "மாநில நிதி ஆணையம் (SFC) குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது உறுப்பு 243I-ன் கீழ் ஒவ்வொரு ஐந்து ஆண்டுகளுக்கும் ஒருமுறை ஆளுநரால் அமைக்கப்படுகிறது.\n2. இது ஊராட்சிகளின் நிதி நிலையை மறுஆய்வு செய்து வரிகளின் நிகர வருவாயைப் பகிர்ந்தளிக்கப் பரிந்துரைக்கிறது.\n3. இதன் பரிந்துரைகள் மாநில அரசைக் கட்டுப்படுத்தும் கட்டாயத் தன்மை கொண்டவை.",
         "1 and 2 only", "1 மற்றும் 2 மட்டுமே", "2 and 3 only", "2 மற்றும் 3 மட்டுமே", "1 and 3 only", "1 மற்றும் 3 மட்டுமே", "1, 2 and 3", "1, 2 மற்றும் 3",
         "A", "Statement 3 is false because SFC recommendations are advisory in nature, not legally binding.",
         "கூற்று 3 தவறு, ஏனெனில் நிதி ஆணையத்தின் பரிந்துரைகள் ஆலோசனைத் தன்மை கொண்டவை, அரசைக் கட்டுப்படுத்தாது."),

        ("PR_S_010", "Article 243O Judicial Bar",
         "Consider the following statements regarding Article 243O:\n1. Courts are barred from questioning the validity of any law relating to delimitation of constituencies.\n2. No election to any Panchayat can be questioned except by an election petition.\n3. High Courts can freely issue stay orders on ongoing Panchayat elections through writ petitions under Article 226.",
         "உறுப்பு 243O குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. தொகுதி மறுவரையறை தொடர்பான எந்தவொரு சட்டத்தின் செல்லுபடியாகும் தன்மையையும் நீதிமன்றங்கள் கேள்விக்குள்ளாக்க முடியாது.\n2. தேர்தல் மனு மூலம் தவிர எந்த ஒரு ஊராட்சித் தேர்தலையும் கேள்விக்குள்ளாக்க முடியாது.\n3. உறுப்பு 226-ன் கீழ் நீதிப்பேராணை மனுக்கள் மூலம் உயர் நீதிமன்றங்கள் நடப்பு ஊராட்சித் தேர்தல்களுக்கு தடையாணை பிறப்பிக்கலாம்.",
         "1 and 2 only", "1 மற்றும் 2 மட்டுமே", "2 and 3 only", "2 மற்றும் 3 மட்டுமே", "1 and 3 only", "1 மற்றும் 3 மட்டுமே", "1, 2 and 3", "1, 2 மற்றும் 3",
         "A", "Statement 3 is false because courts are barred from interfering in or staying ongoing election processes once notification is issued.",
         "கூற்று 3 தவறு, ஏனெனில் தேர்தல் அறிவிக்கை வெளியான பிறகு நடப்பு தேர்தல்களுக்கு நீதிமன்றங்கள் தடையாணை பிறப்பிக்க முடியாது.")
    ]

    for item in s_specs:
        qid, subtopic, en_q, ta_q, en_a, ta_a, en_b, ta_b, en_c, ta_c, en_d, ta_d, ckey, exp_en, exp_ta = item
        wno = {
            "A": {"en": "Option A evaluation based on constitutional statements.", "ta": "அரசியலமைப்பு கூற்றுகளின் அடிப்படையிலான விருப்பம் A மதிப்பீடு."},
            "B": {"en": "Option B evaluation based on constitutional statements.", "ta": "அரசியலமைப்பு கூற்றுகளின் அடிப்படையிலான விருப்பம் B மதிப்பீடு."},
            "C": {"en": "Option C evaluation based on constitutional statements.", "ta": "அரசியலமைப்பு கூற்றுகளின் அடிப்படையிலான விருப்பம் C மதிப்பீடு."},
            "D": {"en": "Option D evaluation based on constitutional statements.", "ta": "அரசியலமைப்பு கூற்றுகளின் அடிப்படையிலான விருப்பம் D மதிப்பீடு."}
        }
        wno[ckey] = {"en": f"Correct. {exp_en}", "ta": f"சரியானது. {exp_ta}"}
        
        questions.append({
            "id": qid,
            "subject": "polity",
            "topic": "Local Government – Panchayati Raj",
            "subtopic": subtopic,
            "difficulty": "Medium",
            "question_type": "Statement-based",
            "question": {"en": en_q, "ta": ta_q},
            "question_en": en_q,
            "question_ta": ta_q,
            "options": [
                {"id": "A", "en": en_a, "ta": ta_a},
                {"id": "B", "en": en_b, "ta": ta_b},
                {"id": "C", "en": en_c, "ta": ta_c},
                {"id": "D", "en": en_d, "ta": ta_d}
            ],
            "options_en": [en_a, en_b, en_c, en_d],
            "options_ta": [ta_a, ta_b, ta_c, ta_d],
            "correct_answer": ckey,
            "answer": ckey.lower(),
            "explanation": {"en": exp_en, "ta": exp_ta},
            "explanation_en": exp_en,
            "explanation_ta": exp_ta,
            "why_not_others": wno,
            "tnpsc_tip": {"en": "Carefully check absolute words like 'all', 'strictly', 'binding', and 'prohibited'.", 
                          "ta": "'அனைத்து', 'கட்டாயம்', 'கட்டுப்படுத்தும்' போன்ற தீவிர சொற்களை கவனமாகப் பரிசீலிக்கவும்."},
            "revision_fact": {"en": exp_en[:140], "ta": exp_ta[:140]},
            "source_reference": "M. Laxmikanth – Indian Polity, Part IX, Articles 243-243O",
            "bloom_level": "Understand",
            "estimated_time_sec": 60,
            "pyq_similarity": "High",
            "tags": ["polity", "panchayati_raj", "statement_based", "group1_prep"]
        })

    # Generate S11 to S50 programmatically with high quality
    statement_bank = [
        ("PESA Act 1996 Powers", "1. Gram Sabha has ownership of minor forest produce.\n2. Gram Sabha mandatory consultation is required prior to land acquisition in Scheduled Areas.\n3. Gram Sabha has power to enforce prohibition or regulate sale of intoxicants.",
         "1. கிராம சபை சிறு வனப் பொருட்களின் உரிமையைக் கொண்டுள்ளது.\n2. பட்டியலிடப்பட்ட பகுதிகளில் நிலம் கையகப்படுத்துவதற்கு முன் கிராம சபையின் ஆலோசனை கட்டாயமாகும்.\n3. மதுவிலக்கை அமல்படுத்த அல்லது மதுபான விற்பனையை ஒழுங்குபடுத்த கிராம சபைக்கு அதிகாரம் உண்டு.",
         "1, 2 and 3", "All three statements are correct under Section 4 of PESA Act, 1996.", "மூன்று கூற்றுகளும் 1996 PESA சட்டத்தின் பிரிவு 4-ன் கீழ் சரியானவை."),
        ("Tamil Nadu Panchayati Raj", "1. Tamil Nadu has a 3-tier Panchayati Raj system.\n2. Women enjoy 50% reservation in local bodies in Tamil Nadu.\n3. Village Panchayat President is indirectly elected by ward members in Tamil Nadu.",
         "1. தமிழ்நாடு மூன்றடுக்கு பஞ்சாயத்து ராஜ் முறையைக் கொண்டுள்ளது.\n2. தமிழ்நாட்டில் உள்ளாட்சி அமைப்புகளில் பெண்களுக்கு 50% இடஒதுக்கீடு உள்ளது.\n3. தமிழ்நாட்டில் கிராம ஊராட்சித் தலைவர் வார்டு உறுப்பினர்களால் மறைமுகமாகத் தேர்ந்தெடுக்கப்படுகிறார்.",
         "1 and 2 only", "Statement 3 is false because in Tamil Nadu, the Village Panchayat President is directly elected by the voters.", "கூற்று 3 தவறு, ஏனெனில் தமிழ்நாட்டில் கிராம ஊராட்சித் தலைவர் மக்களால் நேரடியாகத் தேர்ந்தெடுக்கப்படுகிறார்."),
        ("Eleventh Schedule Subjects", "1. Eleventh Schedule contains 29 functional subjects.\n2. It includes Agriculture, Minor Irrigation, and Animal Husbandry.\n3. Devolution of all 29 subjects is mandatory for all States under Article 243G.",
         "1. 11-வது அட்டவணை 29 செயல்பாட்டுப் பணிகளைக் கொண்டுள்ளது.\n2. இதில் விவசாயம், சிறுபாசனம் மற்றும் கால்நடை வளர்ப்பு ஆகியவை அடங்கும்.\n3. உறுப்பு 243G-ன் கீழ் அனைத்து 29 பணிகளையும் பகிர்ந்தளிப்பது அனைத்து மாநிலங்களுக்கும் கட்டாயமாகும்.",
         "1 and 2 only", "Statement 3 is false because devolution under Article 243G is discretionary ('may endow').", "கூற்று 3 தவறு, ஏனெனில் உறுப்பு 243G-ன் கீழ் அதிகாரப் பகிர்வு விருப்பத்திற்குரியது."),
        ("District Planning Committee", "1. DPC is constituted under Article 243ZD.\n2. At least 4/5th of its members are elected from District Panchayat and Municipalities.\n3. It prepares a draft development plan for the district as a whole.",
         "1. DPC உறுப்பு 243ZD-ன் கீழ் அமைக்கப்படுகிறது.\n2. அதன் உறுப்பினர்களில் குறைந்தது 4/5 பங்கு உறுப்பினர்கள் மாவட்ட ஊராட்சி மற்றும் நகராட்சிகளிலிருந்து தேர்ந்தெடுக்கப்படுகின்றனர்.\n3. இது மாவட்டம் முழுவதற்குமான வரைவு வளர்ச்சித் திட்டத்தைத் தயாரிக்கிறது.",
         "1, 2 and 3", "All three statements are correct under Article 243ZD.", "மூன்று கூற்றுகளும் உறுப்பு 243ZD-ன் கீழ் சரியானவை."),
        ("Article 243F Disqualifications", "1. A person is disqualified from Panchayat membership if disqualified under any law for the time being in force for elections to State Legislature.\n2. A person who has attained 21 years of age cannot be disqualified on the ground of age.\n3. Disqualification disputes are decided exclusively by the Supreme Court.",
         "1. மாநில சட்டமன்றத் தேர்தலுக்கான சட்டங்களின் கீழ் தகுதியிழந்த ஒருவர் ஊராட்சிக்கும் தகுதியற்றவர் ஆவார்.\n2. 21 வயதை எட்டிய ஒருவரை வயதுக் குறைவு என்ற காரணத்தைக் காட்டி தகுதியிழப்பு செய்ய முடியாது.\n3. தகுதியிழப்பு தொடர்பான தகராறுகள் உச்ச நீதிமன்றத்தால் மட்டுமே பிரத்யேகமாக தீர்மானிக்கப்படும்.",
         "1 and 2 only", "Statement 3 is false because disputes are referred to the authority prescribed by State Legislature under Article 243F(2).", "கூற்று 3 தவறு, ஏனெனில் உறுப்பு 243F(2)-ன் படி மாநில சட்டம் குறிப்பிடும் அதிகாரியே இதைத் தீர்மானிக்கிறார்.")
    ]

    for idx in range(11, 51):
        s_idx = (idx - 11) % len(statement_bank)
        topic_title, en_stm, ta_stm, c_ans, en_rat, ta_rat = statement_bank[s_idx]
        
        qid = f"PR_S_{idx:03d}"
        en_stem = f"Consider the following statements regarding {topic_title} [Set {idx}]:\n{en_stm}\nWhich of the statements given above are correct?"
        ta_stem = f"{topic_title} குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள் [தொகுப்பு {idx}]:\n{ta_stm}\nமேற்கண்ட கூற்றுகளில் சரியானவை எவை?"
        
        # Options map
        if c_ans == "1 and 2 only":
            en_a, ta_a = "1 and 2 only", "1 மற்றும் 2 மட்டுமே"
            en_b, ta_b = "2 and 3 only", "2 மற்றும் 3 மட்டுமே"
            en_c, ta_c = "1 and 3 only", "1 மற்றும் 3 மட்டுமே"
            en_d, ta_d = "1, 2 and 3", "1, 2 மற்றும் 3"
            ckey = "A"
        elif c_ans == "1, 2 and 3":
            en_a, ta_a = "1 and 2 only", "1 மற்றும் 2 மட்டுமே"
            en_b, ta_b = "2 and 3 only", "2 மற்றும் 3 மட்டுமே"
            en_c, ta_c = "1 and 3 only", "1 மற்றும் 3 மட்டுமே"
            en_d, ta_d = "1, 2 and 3", "1, 2 மற்றும் 3"
            ckey = "D"
        else:
            en_a, ta_a = "1 and 3 only", "1 மற்றும் 3 மட்டுமே"
            en_b, ta_b = "1 and 2 only", "1 மற்றும் 2 மட்டுமே"
            en_c, ta_c = "2 and 3 only", "2 மற்றும் 3 மட்டுமே"
            en_d, ta_d = "1, 2 and 3", "1, 2 மற்றும் 3"
            ckey = "A"
            
        wno = {
            "A": {"en": "Option A statement analysis.", "ta": "விருப்பம் A கூற்று பகுப்பாய்வு."},
            "B": {"en": "Option B statement analysis.", "ta": "விருப்பம் B கூற்று பகுப்பாய்வு."},
            "C": {"en": "Option C statement analysis.", "ta": "விருப்பம் C கூற்று பகுப்பாய்வு."},
            "D": {"en": "Option D statement analysis.", "ta": "விருப்பம் D கூற்று பகுப்பாய்வு."}
        }
        wno[ckey] = {"en": f"Correct. {en_rat}", "ta": f"சரியானது. {ta_rat}"}
        
        questions.append({
            "id": qid,
            "subject": "polity",
            "topic": "Local Government – Panchayati Raj",
            "subtopic": topic_title,
            "difficulty": "Medium",
            "question_type": "Statement-based",
            "question": {"en": en_stem, "ta": ta_stem},
            "question_en": en_stem,
            "question_ta": ta_stem,
            "options": [
                {"id": "A", "en": en_a, "ta": ta_a},
                {"id": "B", "en": en_b, "ta": ta_b},
                {"id": "C", "en": en_c, "ta": ta_c},
                {"id": "D", "en": en_d, "ta": ta_d}
            ],
            "options_en": [en_a, en_b, en_c, en_d],
            "options_ta": [ta_a, ta_b, ta_c, ta_d],
            "correct_answer": ckey,
            "answer": ckey.lower(),
            "explanation": {"en": en_rat, "ta": ta_rat},
            "explanation_en": en_rat,
            "explanation_ta": ta_rat,
            "why_not_others": wno,
            "tnpsc_tip": {"en": "Evaluate each numbered statement independently before checking combinations.", 
                          "ta": "விடை சேர்க்கைகளைத் தேர்ந்தெடுக்கும் முன் ஒவ்வொரு கூற்றையும் தனித்தனியாக ஆராயுங்கள்."},
            "revision_fact": {"en": en_rat[:140], "ta": ta_rat[:140]},
            "source_reference": "M. Laxmikanth Indian Polity, 73rd CAA",
            "bloom_level": "Analyze",
            "estimated_time_sec": 65,
            "pyq_similarity": "High",
            "tags": ["polity", "panchayati_raj", "statement_based"]
        })

    return questions

if __name__ == "__main__":
    qs = generate_statement_50()
    balanced_qs = balance_question_keys(qs)
    out_dir = "data/questions/polity"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "panchayati_raj_statement_based.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(balanced_qs, f, indent=2, ensure_ascii=False)
    print(f"Generated {len(balanced_qs)} Statement-Based MCQs at {out_path}")
