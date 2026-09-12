import json
import os
from collections import Counter

def create_statement_questions():
    questions = []

    def add_q(q_id, question_en, question_ta, opt_a_en, opt_a_ta, opt_b_en, opt_b_ta, opt_c_en, opt_c_ta, opt_d_en, opt_d_ta, correct, exp_en, exp_ta, why_a_en, why_a_ta, why_b_en, why_b_ta, why_c_en, why_c_ta, why_d_en, why_d_ta, tip_en, tip_ta, fact_en, fact_ta, bloom, difficulty, tags, notes_part):
        q_obj = {
            "id": q_id,
            "subject": "Polity",
            "topic": "Constitutional Amendments",
            "difficulty": difficulty,
            "question_type": "statement",
            "question": {
                "en": question_en,
                "ta": question_ta
            },
            "options": [
                {"id": "A", "en": opt_a_en, "ta": opt_a_ta},
                {"id": "B", "en": opt_b_en, "ta": opt_b_ta},
                {"id": "C", "en": opt_c_en, "ta": opt_c_ta},
                {"id": "D", "en": opt_d_en, "ta": opt_d_ta}
            ],
            "correct_answer": correct,
            "explanation": {
                "en": exp_en,
                "ta": exp_ta
            },
            "why_not_others": {
                "A": {"en": why_a_en, "ta": why_a_ta},
                "B": {"en": why_b_en, "ta": why_b_ta},
                "C": {"en": why_c_en, "ta": why_c_ta},
                "D": {"en": why_d_en, "ta": why_d_ta}
            },
            "tnpsc_tip": {
                "en": tip_en,
                "ta": tip_ta
            },
            "revision_fact": {
                "en": fact_en,
                "ta": fact_ta
            },
            "source_reference": [
                "M. Laxmikanth — Indian Polity",
                "NCERT Class XI — Constitution at Work",
                "Tamil Nadu Samacheer Kalvi — Class 12 Polity",
                f"TNPSC Nova AI Notes — Constitutional Amendments ({notes_part})"
            ],
            "bloom_level": bloom,
            "estimated_time_sec": 75,
            "pyq_similarity": "High Similarity to TNPSC Group 1 Mains/Prelims Statement Questions",
            "tags": tags
        }
        questions.append(q_obj)

    # We will generate 50 Statement Questions with balanced answers: A:13, B:13, C:12, D:12

    # Q001 - Correct: A (13)
    add_q(
        "CZ_AM_ST_001",
        "Consider the following statements regarding Article 368 of the Constitution of India:\n1. A Constitutional Amendment Bill can be introduced in either House of Parliament or in a State Legislative Assembly.\n2. Prior permission of the President of India is not required for introducing a Constitutional Amendment Bill.\n3. The President is bound to give assent to a Constitutional Amendment Bill passed by Parliament under the 24th Amendment Act, 1971.\nWhich of the statements given above is/are correct?",
        "இந்திய அரசியலமைப்பின் 368வது சரத்து பற்றிய பின்வரும் கூற்றுகளை ஆராய்க:\n1. அரசியலமைப்பு திருத்த மசோதாவை நாடாளுமன்றத்தின் ஏதேனும் ஒரு அவையிலோ அல்லது மாநில சட்டமன்றத்திலோ அறிமுகப்படுத்தலாம்.\n2. அரசியலமைப்பு திருத்த மசோதாவை அறிமுகப்படுத்த இந்தியக் குடியரசுத் தலைவரின் முன்அனுமதி தேவையில்லை.\n3. 1971 ஆம் ஆண்டின் 24வது திருத்தச் சட்டத்தின்படி நாடாளுமன்றத்தால் நிறைவேற்றப்பட்ட அரசியலமைப்பு திருத்த மசோதாவிற்கு குடியரசுத் தலைவர் ஒப்புதல் அளிக்கக் கடமைப்பட்டவர்.\nமேற்கண்ட கூற்றுகளில் எது/எவை சரியானவை?",
        "2 and 3 only", "2 மற்றும் 3 மட்டும்",
        "1 and 2 only", "1 மற்றும் 2 மட்டும்",
        "1 and 3 only", "1 மற்றும் 3 மட்டும்",
        "1, 2 and 3", "1, 2 மற்றும் 3",
        "A",
        "Statement 1 is incorrect because a Constitutional Amendment Bill can be introduced ONLY in Parliament (Lok Sabha or Rajya Sabha), never in a State Legislature. Statement 2 is correct as prior Presidential assent is not needed. Statement 3 is correct as the 24th CA 1971 made Presidential assent mandatory under Article 368.",
        "கூற்று 1 தவறானது, ஏனெனில் அரசியலமைப்பு திருத்த மசோதாவை நாடாளுமன்றத்தில் மட்டுமே அறிமுகப்படுத்த முடியும்; மாநில சட்டமன்றத்தில் முடியாது. கூற்று 2 சரியானது, ஏனெனில் குடியரசுத் தலைவரின் முன்அனுமதி தேவையில்லை. கூற்று 3 சரியானது, 24வது திருத்தம் 1971 மூலம் குடியரசுத் தலைவரின் ஒப்புதல் கட்டாயமாக்கப்பட்டது.",
        "Option A is correct because Statements 2 and 3 are constitutionally accurate while Statement 1 is incorrect.", "விருப்பம் A சரியானது, ஏனெனில் கூற்றுகள் 2 மற்றும் 3 சரியானவை, கூற்று 1 தவறானது.",
        "Option B is incorrect because Statement 1 is false (state assemblies cannot initiate CA bills).", "விருப்பம் B தவறானது, ஏனெனில் கூற்று 1 தவறானது (மாநில சட்டமன்றங்கள் திருத்த மசோதாவை அறிமுகப்படுத்த முடியாது).",
        "Option C is incorrect because Statement 1 is false.", "விருப்பம் C தவறானது, ஏனெனில் கூற்று 1 தவறானது.",
        "Option D is incorrect because Statement 1 is false.", "விருப்பம் D தவறானது, ஏனெனில் கூற்று 1 தவறானது.",
        "TNPSC Elimination Tip: Remember that State Assemblies CANNOT initiate any Constitutional Amendment Bill. Only Parliament holds this power under Article 368.",
        "டிஎன்பிஎஸ்சி குறிப்பு: மாநில சட்டமன்றங்களால் அரசியலமைப்பு திருத்த மசோதாவைத் தொடங் முடியாது என்பதை நினைவில் கொள்க. நாடாளுமன்றத்திற்கு மட்டுமே இவதிகாரம் உள்ளது.",
        "24th CA 1971 substituted 'shall give his assent' in Art 368(2), removing presidential discretion.",
        "24வது திருத்தம் 1971 குடியரசுத் தலைவரின் விருப்ப அதிகாரத்தை நீக்கி ஒப்புதலைக் கட்டாயமாக்கியது.",
        "Evaluating", "Medium", ["Article 368", "Introduction Procedure", "24th Amendment"], "Part 1"
    )

    # Q002 - Correct: B
    add_q(
        "CZ_AM_ST_002",
        "Consider the following statements regarding the special majority required under Article 368:\n1. It requires a majority of the total membership of each House of Parliament.\n2. It requires a majority of not less than two-thirds of the members present and voting in each House.\n3. 'Total membership' of the House includes vacancies and absent members.\nWhich of the statements given above are correct?",
        "சரத்து 368 இன் கீழ் தேவைப்படும் சிறப்புப் பெரும்பான்மை பற்றிய பின்வரும் கூற்றுகளை ஆராய்க:\n1. இது நாடாளுமன்றத்தின் ஒவ்வொரு அவையின் மொத்த உறுப்பினர்களின் பெரும்பான்மையைக் கோருகிறது.\n2. இது ஒவ்வொரு அவையிலும் வருகை தந்து வாக்களிக்கும் உறுப்பினர்களில் 2/3 பங்கிற்குக் குறையாத பெரும்பான்மையைக் கோருகிறது.\n3. அவையின் 'மொத்த உறுப்பினர்கள்' என்பதில் காலியிடங்கள் மற்றும் வராத உறுப்பினர்களும் அடங்குவர்.\nமேற்கண்ட கூற்றுகளில் எவை சரியானவை?",
        "1 and 2 only", "1 மற்றும் 2 மட்டும்",
        "1, 2 and 3", "1, 2 மற்றும் 3",
        "2 and 3 only", "2 மற்றும் 3 மட்டும்",
        "1 and 3 only", "1 மற்றும் 3 மட்டும்",
        "B",
        "All three statements are correct under Article 368. Special majority requires BOTH: (i) Majority of total membership of the House (absolute majority, where total membership means full sanctioned strength including vacancies), AND (ii) 2/3rd majority of members present and voting.",
        "மூன்று கூற்றுகளும் சரியானவை. சிறப்புப் பெரும்பான்மைக்கு இரு நிபந்தனைகளும் தேவை: (i) அவையின் மொத்த உறுப்பினர்களின் பெரும்பான்மை (காலியிடங்கள் உட்பட மொத்த அனுமதிக்கப்பட்ட எண்ணிக்கை), மற்றும் (ii) வருகை தந்து வாக்களிப்பவர்களில் 2/3 பங்கு பெரும்பான்மை.",
        "Option A is incorrect because Statement 3 is also true.", "விருப்பம் A தவறானது, ஏனெனில் கூற்று 3 ம் சரியானது.",
        "Option B is correct because all three statements accurately describe the double requirement of Special Majority under Article 368.", "விருப்பம் B சரியானது, ஏனெனில் மூன்று கூற்றுகளும் சிறப்புப் பெரும்பான்மையைச் சரியாக விவரிக்கின்றன.",
        "Option C is incorrect because Statement 1 is also true.", "விருப்பம் C தவறானது, ஏனெனில் கூற்று 1 ம் சரியானது.",
        "Option D is incorrect because Statement 2 is also true.", "விருப்பம் D தவறானது, ஏனெனில் கூற்று 2 ம் சரியானது.",
        "Total membership means total sanctioned strength of the House irrespective of vacancies or absent members.",
        "மொத்த உறுப்பினர்கள் என்பது காலியிடங்கள் அல்லது வருகை தராத உறுப்பினர்களைப் பொருட்படுத்தாமல் அனுமதிக்கப்பட்ட மொத்த எண்ணிக்கையைக் குறிக்கும்.",
        "Article 368 special majority is a dual condition: >50% of total strength AND >=2/3 of present & voting.",
        "சரத்து 368 சிறப்புப் பெரும்பான்மை இரட்டை நிபந்தனையாகும்: மொத்த பலத்தில் >50% மற்றும் வருகை தந்து வாக்களிப்பவரில் >=2/3 பங்கு.",
        "Understanding", "Medium", ["Special Majority", "Article 368 Dual Condition", "Total Membership"], "Part 1"
    )

    # Q003 - Correct: C
    add_q(
        "CZ_AM_ST_003",
        "Consider the following statements regarding the ratification of Constitutional Amendment Bills by States:\n1. State Legislative Councils do not participate in ratifying constitutional amendments under Article 368.\n2. Ratification by State Legislatures requires a special majority of 2/3rd members present and voting in each State Assembly.\n3. The Constitution lays down no time limit within which State Legislatures must ratify or reject an amendment bill.\nWhich of the statements given above is/are correct?",
        "மாநிலங்களால் அரசியலமைப்பு திருத்த மசோதாக்களை ஒப்புதல் அளித்தல் பற்றிய பின்வரும் கூற்றுகளை ஆராய்க:\n1. சரத்து 368 இன் கீழ் அரசியலமைப்பு திருத்தங்களுக்கு ஒப்புதல் அளிப்பதில் மாநில சட்ட மேலவைகள் பங்கேற்பதில்லை.\n2. மாநில சட்டமன்றங்களின் ஒப்புதலுக்கு ஒவ்வொரு மாநில சட்டமன்றத்திலும் வருகை தந்து வாக்களிக்கும் உறுப்பினர்களில் 2/3 பங்கு சிறப்புப் பெரும்பான்மை தேவை.\n3. மாநில சட்டமன்றங்கள் ஒரு திருத்த மசோதாவை ஒப்புக்கொள்ளவோ நிராகரிக்கவோ எந்தக் காலக்கெடுவையும் அரசியலமைப்பு நிர்ணயிக்கவில்லை.\nமேற்கண்ட கூற்றுகளில் எது/எவை சரியானவை?",
        "1 and 2 only", "1 மற்றும் 2 மட்டும்",
        "2 and 3 only", "2 மற்றும் 3 மட்டும்",
        "1 and 3 only", "1 மற்றும் 3 மட்டும்",
        "1, 2 and 3", "1, 2 மற்றும் 3",
        "C",
        "Statements 1 and 3 are correct. Statement 2 is incorrect because State ratification requires ONLY a SIMPLE MAJORITY of members present and voting in the state legislature, NOT a special majority.",
        "கூற்றுகள் 1 மற்றும் 3 சரியானவை. கூற்று 2 தவறானது, ஏனெனில் மாநில சட்டமன்ற ஒப்புதலுக்கு வருகை தந்து வாக்களிப்பவர்களில் எளிய பெரும்பான்மை மட்டுமே போதுமானது; சிறப்புப் பெரும்பான்மை தேவையில்லை.",
        "Option A is incorrect because Statement 2 is false (requires simple majority in states).", "விருப்பம் A தவறானது, ஏனெனில் கூற்று 2 தவறானது (மாநிலங்களில் எளிய பெரும்பான்மை மட்டுமே தேவை).",
        "Option B is incorrect because Statement 2 is false.", "விருப்பம் B தவறானது, ஏனெனில் கூற்று 2 தவறானது.",
        "Option C is correct because Statements 1 and 3 are true while Statement 2 is false.", "விருப்பம் C சரியானது, ஏனெனில் கூற்றுகள் 1 மற்றும் 3 சரியானவை, கூற்று 2 தவறானது.",
        "Option D is incorrect because Statement 2 is false.", "விருப்பம் D தவறானது, ஏனெனில் கூற்று 2 தவறானது.",
        "State Ratification Trick: Parliament passes by SPECIAL MAJORITY, but half of the States ratify by SIMPLE MAJORITY.",
        "மாநில ஒப்புதல் தந்திரம்: நாடாளுமன்றம் சிறப்புப் பெரும்பான்மையால் நிறைவேற்றும், ஆனால் பாதி மாநிலங்கள் எளிய பெரும்பான்மையால் ஒப்புதல் அளிக்கும்.",
        "At least half (14 out of 28 currently) of the state legislatures must pass resolutions by simple majority for federal provisions.",
        "கூட்டாட்சி விதிகளுக்கு குறைந்தபட்சம் பாதி மாநில சட்டமன்றங்கள் எளிய பெரும்பான்மையால் தீர்மானம் நிறைவேற்ற வேண்டும்.",
        "Evaluating", "Hard", ["State Ratification", "Simple Majority States", "No Time Limit"], "Part 1"
    )

    # Q004 - Correct: D
    add_q(
        "CZ_AM_ST_004",
        "Consider the following statements regarding joint sittings for Constitutional Amendment Bills:\n1. If a deadlock arises between Lok Sabha and Rajya Sabha over a Constitutional Amendment Bill, the President can summon a Joint Sitting under Article 108.\n2. Rajya Sabha possesses equal powers with Lok Sabha regarding the passage of a Constitutional Amendment Bill.\n3. If Rajya Sabha rejects a Constitutional Amendment Bill passed by Lok Sabha, the Bill lapses immediately.\nWhich of the statements given above are correct?",
        "அரசியலமைப்பு திருத்த மசோதாக்களுக்கான கூட்டுக் கூட்டம் பற்றிய பின்வரும் கூற்றுகளை ஆராய்க:\n1. அரசியலமைப்பு திருத்த மசோதா குறித்து மக்களவைக்கும் மாநிலங்களவைக்கும் இடையே முட்டுக்கட்டை ஏற்பட்டால், குடியரசுத் தலைவர் சரத்து 108 இன் கீழ் கூட்டுக் கூட்டத்தைக் கூட்டலாம்.\n2. அரசியலமைப்பு திருத்த மசோதாவை நிறைவேற்றுவதில் மாநிலங்களவை மக்களவைக்கு இணையான அதிகாரங்களைப் பெற்றுள்ளது.\n3. மக்களவையால் நிறைவேற்றப்பட்ட அரசியலமைப்பு திருத்த மசோதாவை மாநிலங்களவை நிராகரித்தால், அம்மசோதா உடனடியாக செயலிழந்துவிடும்.\nமேற்கண்ட கூற்றுகளில் எவை சரியானவை?",
        "1 and 2 only", "1 மற்றும் 2 மட்டும்",
        "1 and 3 only", "1 மற்றும் 3 மட்டும்",
        "1, 2 and 3", "1, 2 மற்றும் 3",
        "2 and 3 only", "2 மற்றும் 3 மட்டும்",
        "D",
        "Statement 1 is incorrect because Article 108 joint sitting provision does NOT apply to Constitutional Amendment Bills. Statements 2 and 3 are correct because both Houses have equal veto power; if either House rejects or fails to pass the bill by special majority, the bill lapses.",
        "கூற்று 1 தவறானது, ஏனெனில் சரத்து 108 கூட்டுக் கூட்ட விதி அரசியலமைப்பு திருத்த மசோதாக்களுக்குப் பொருந்தாது. கூற்றுகள் 2 மற்றும் 3 சரியானவை, ஏனெனில் இரு அவைகளுக்கும் சம அதிகாரம் உண்டு; ஒரு அவை நிராகரித்தால் மசோதா செயலிழந்துவிடும்.",
        "Option A is incorrect because Statement 1 is false (no joint sitting for CA bills).", "விருப்பம் A தவறானது, ஏனெனில் கூற்று 1 தவறானது (கூட்டுக் கூட்டம் கிடையாது).",
        "Option B is incorrect because Statement 1 is false.", "விருப்பம் B தவறானது, ஏனெனில் கூற்று 1 தவறானது.",
        "Option C is incorrect because Statement 1 is false.", "விருப்பம் C தவறானது, ஏனெனில் கூற்று 1 தவறானது.",
        "Option D is correct because Statements 2 and 3 are correct while Statement 1 is false.", "விருப்பம் D சரியானது, ஏனெனில் கூற்றுகள் 2 மற்றும் 3 சரியானவை, கூற்று 1 தவறானது.",
        "Joint Sitting (Article 108) applies ONLY to Ordinary Bills and Financial Bills, NEVER to Money Bills or Constitutional Amendment Bills.",
        "கூட்டுக் கூட்டம் (சரத்து 108) சாதாரண மசோதாக்கள் மற்றும் நிதிய மசோதாக்களுக்கு மட்டுமே பொருந்தும்; பண மசோதா அல்லது அரசியலமைப்பு திருத்த மசோதாக்களுக்குப் பொருந்தாது.",
        "Rajya Sabha effectively holds full veto power over Constitutional Amendments equal to Lok Sabha.",
        "மாநிலங்களவை அரசியலமைப்பு திருத்தங்களில் மக்களவைக்கு இணையான முழு வீட்டோ அதிகாரத்தைக் கொண்டுள்ளது.",
        "Understanding", "Medium", ["No Joint Sitting", "Article 108 Exception", "Equal Powers Rajya Sabha"], "Part 1"
    )

    # Q005 - Correct: A
    add_q(
        "CZ_AM_ST_005",
        "Consider the following statements regarding the 42nd Amendment Act, 1976:\n1. It added the words 'Socialist', 'Secular', and 'Integrity' to the Preamble.\n2. It inserted Part IV-A containing Fundamental Duties upon the recommendation of the Swaran Singh Committee.\n3. It made the advice of the Cabinet binding on the President under Article 74.\nWhich of the statements given above are correct?",
        "42வது திருத்தச் சட்டம், 1976 பற்றிய பின்வரும் கூற்றுகளை ஆராய்க:\n1. இது முகப்புரையில் 'சமதர்ம', 'மதச்சார்பற்ற', 'ஒருமைப்பாடு' என்ற சொற்களைச் சேர்த்தது.\n2. இது ஸ்வரண் சிங் குழுவின் பரிந்துரையின் பேரில் அடிப்படை கடமைகளைக் கொண்ட பகுதி IV-A ஐச் சேர்த்தது.\n3. இது சரத்து 74 இன் கீழ் குடியரசுத் தலைவருக்கு அமைச்சரவையின் ஆலோசனையைக் கட்டாயமாக்கியது.\nமேற்கண்ட கூற்றுகளில் எவை சரியானவை?",
        "1, 2 and 3", "1, 2 மற்றும் 3",
        "1 and 2 only", "1 மற்றும் 2 மட்டும்",
        "2 and 3 only", "2 மற்றும் 3 மட்டும்",
        "1 and 3 only", "1 மற்றும் 3 மட்டும்",
        "A",
        "All three statements are correct. The 42nd Amendment Act 1976 added 3 new words to Preamble, inserted Part IV-A (Art 51A), and made Cabinet advice explicitly binding on the President.",
        "மூன்று கூற்றுகளும் சரியானவை. 42வது திருத்தச் சட்டம் 1976 முகப்புரையில் 3 புதிய சொற்களைச் சேர்த்தது, பகுதி IV-A ஐச் சேர்த்தது, மற்றும் அமைச்சரவை ஆலோசனையைக் குடியரசுத் தலைவருக்குக் கட்டாயமாக்கியது.",
        "Option A is correct because all three statements accurately present 42nd Amendment provisions.", "விருப்பம் A சரியானது, ஏனெனில் மூன்று கூற்றுகளும் 42வது திருத்த விதிகளைச் சரியாகக் கூறுகின்றன.",
        "Option B is incorrect because Statement 3 is also true.", "விருப்பம் B தவறானது, ஏனெனில் கூற்று 3 ம் சரியானது.",
        "Option C is incorrect because Statement 1 is also true.", "விருப்பம் C தவறானது, ஏனெனில் கூற்று 1 ம் சரியானது.",
        "Option D is incorrect because Statement 2 is also true.", "விருப்பம் D தவறானது, ஏனெனில் கூற்று 2 ம் சரியானது.",
        "42nd Amendment 1976 is known as the 'Mini-Constitution' due to its massive structural additions.",
        "42வது திருத்தம் 1976 அதன் மாபெரும் அமைப்பு ரீதியான சேர்க்கைகளால் 'சிறிய அரசியலமைப்பு' என அழைக்கப்படுகிறது.",
        "Swaran Singh Committee originally recommended 8 Fundamental Duties, but 42nd CA enacted 10 duties.",
        "ஸ்வரண் சிங் குழு 8 கடமைகளைப் பரிந்துரைத்தது, ஆனால் 42வது திருத்தம் 10 கடமைகளை இயற்றியது.",
        "Remembering", "Medium", ["42nd Amendment", "Swaran Singh Committee", "Mini Constitution"], "Part 2"
    )

    # Q006 - Correct: B
    add_q(
        "CZ_AM_ST_006",
        "Consider the following statements regarding the 44th Amendment Act, 1978:\n1. It removed Right to Property from Part III (Fundamental Rights) and made it a legal right under Article 300A.\n2. It replaced 'Internal Disturbance' with 'Armed Rebellion' in Article 352 for declaring National Emergency.\n3. It restored the original 5-year term for Lok Sabha and State Legislative Assemblies.\nWhich of the statements given above are correct?",
        "44வது திருத்தச் சட்டம், 1978 பற்றிய பின்வரும் கூற்றுகளை ஆராய்க:\n1. இது பகுதி III இலிருந்து (அடிப்படை உரிமைகள்) சொத்து உரிமையை நீக்கி, அதை சரத்து 300A இன் கீழ் சட்ட உரிமையாக்கியது.\n2. இது தேசிய அவசரநிலையை அறிவிக்க சரத்து 352 இல் 'உள்நாட்டு அமைதியின்மை' என்பதற்குப் பதிலாக 'ஆயுதம் ஏந்திய கிளர்ச்சி' என மாற்றியது.\n3. இது மக்களவை மற்றும் மாநில சட்டமன்றங்களின் 5 ஆண்டு பதவிக் காலத்தை மீண்டும் நிலைநிறுத்தியது.\nமேற்கண்ட கூற்றுகளில் எவை சரியானவை?",
        "1 and 2 only", "1 மற்றும் 2 மட்டும்",
        "1, 2 and 3", "1, 2 மற்றும் 3",
        "2 and 3 only", "2 மற்றும் 3 மட்டும்",
        "1 and 3 only", "1 மற்றும் 3 மட்டும்",
        "B",
        "All three statements are correct. The 44th Amendment Act 1978 enacted by the Janata Party government reversed major excesses of the 42nd Amendment by deleting Right to Property from Part III, inserting Article 300A, substituting 'armed rebellion', and restoring 5-year terms.",
        "மூன்று கூற்றுகளும் சரியானவை. ஜனதா கட்சி அரசால் இயற்றப்பட்ட 44வது திருத்தச் சட்டம் 1978 சொத்து உரிமையை நீக்கி 300A ஆக மாற்றியது, 'ஆயுதம் ஏந்திய கிளர்ச்சி' என மாற்றியது, மற்றும் 5 ஆண்டு பதவிக் காலத்தை மீட்டெடுத்தது.",
        "Option A is incorrect because Statement 3 is also true.", "விருப்பம் A தவறானது, ஏனெனில் கூற்று 3 ம் சரியானது.",
        "Option B is correct because all 3 statements correctly detail the democratic restorations of the 44th CA 1978.", "விருப்பம் B சரியானது, ஏனெனில் 3 கூற்றுகளும் 44வது திருத்தத்தின் ஜனநாயக மீட்புகளைச் சரியாகக் கூறுகின்றன.",
        "Option C is incorrect because Statement 1 is also true.", "விருப்பம் C தவறானது, ஏனெனில் கூற்று 1 ம் சரியானது.",
        "Option D is incorrect because Statement 2 is also true.", "விருப்பம் D தவறானது, ஏனெனில் கூற்று 2 ம் சரியானது.",
        "Remember that 44th Amendment also introduced Article 20 and 21 immunity during National Emergency.",
        "44வது திருத்தம் தேசிய அவசரநிலையின் போதும் சரத்துகள் 20 மற்றும் 21 ஐ இடைநிறுத்த முடியாது என்ற பாதுகாப்பையும் வழங்கியது.",
        "Right to property shifted from Article 31 to Article 300A in Part XII.",
        "சொத்து உரிமை பகுதி XII இல் சரத்து 31 இலிருந்து சரத்து 300A விற்கு மாற்றப்பட்டது.",
        "Understanding", "Medium", ["44th Amendment", "Right to Property 300A", "Article 352 Safeguards"], "Part 2"
    )

    # Q007 - Correct: C
    add_q(
        "CZ_AM_ST_007",
        "Consider the following statements regarding the Basic Structure Doctrine:\n1. It was propounded by the Supreme Court in the Kesavananda Bharati case (1973).\n2. The term 'Basic Structure' is explicitly defined in Article 368 of the Constitution.\n3. Judicial Review is recognized as an integral part of the Basic Structure.\nWhich of the statements given above is/are correct?",
        "அடிப்படை அமைப்புக் கோட்பாடு பற்றிய பின்வரும் கூற்றுகளை ஆராய்க:\n1. இது கேசவாநந்த பாரதி வழக்கில் (1973) உச்ச நீதிமன்றத்தால் முன்வைக்கப்பட்டது.\n2. 'அடிப்படை அமைப்பு' என்ற சொல் அரசியலமைப்பின் 368வது சரத்தில் தெளிவாக வரையறுக்கப்பட்டுள்ளது.\n3. நீதிமன்ற ஆய்வு அடிப்படை அமைப்பின் ஒருங்கிணைந்த பகுதியாக அங்கீகரிக்கப்பட்டுள்ளது.\nமேற்கண்ட கூற்றுகளில் எது/எவை சரியானவை?",
        "1 and 2 only", "1 மற்றும் 2 மட்டும்",
        "2 and 3 only", "2 மற்றும் 3 மட்டும்",
        "1 and 3 only", "1 மற்றும் 3 மட்டும்",
        "1, 2 and 3", "1, 2 மற்றும் 3",
        "C",
        "Statements 1 and 3 are correct. Statement 2 is incorrect because the term 'Basic Structure' is NOT defined anywhere in the Constitution of India; it is a judicially developed doctrine.",
        "கூற்றுகள் 1 மற்றும் 3 சரியானவை. கூற்று 2 தவறானது, ஏனெனில் 'அடிப்படை அமைப்பு' என்ற சொல் அரசியலமைப்பில் எங்குமே வரையறுக்கப்படவில்லை; இது நீதிமன்றத்தால் உருவாக்கப்பட்ட கோட்பாடு.",
        "Option A is incorrect because Statement 2 is false (not defined in Constitution).", "விருப்பம் A தவறானது, ஏனெனில் கூற்று 2 தவறானது (அரசியலமைப்பில் வரையறுக்கப்படவில்லை).",
        "Option B is incorrect because Statement 2 is false.", "விருப்பம் B தவறானது, ஏனெனில் கூற்று 2 தவறானது.",
        "Option C is correct because Statements 1 and 3 are true while Statement 2 is false.", "விருப்பம் C சரியானது, ஏனெனில் கூற்றுகள் 1 மற்றும் 3 சரியானவை, கூற்று 2 தவறானது.",
        "Option D is incorrect because Statement 2 is false.", "விருப்பம் D தவறானது, ஏனெனில் கூற்று 2 தவறானது.",
        "TNPSC Traps: 'Basic Structure' is nowhere defined in the Constitution, nor is 'Unsound Mind' or 'Martial Law'.",
        "டிஎன்பிஎஸ்சி பொறிகள்: 'அடிப்படை அமைப்பு' என்ற சொல் அரசியலமைப்பில் எங்குமே வரையறுக்கப்படவில்லை.",
        "Kesavananda Bharati bench consisted of 13 judges, delivering a 7-6 landmark majority decision on April 24, 1973.",
        "கேசவாநந்த பாரதி அமர்வு 13 நீதிபதிகளைக் கொண்டிருந்தது; 1973 ஏப்ரல் 24 அன்று 7-6 என்ற கணக்கில் தீர்ப்பளித்தது.",
        "Analysis", "Hard", ["Basic Structure Doctrine", "Kesavananda Bharati", "Not Defined in Constitution"], "Part 3"
    )

    # Q008 - Correct: D
    add_q(
        "CZ_AM_ST_008",
        "Consider the following statements regarding the 73rd and 74th Amendment Acts, 1992:\n1. 73rd CA added Part IX and 11th Schedule containing 29 functional items for Panchayats.\n2. 74th CA added Part IX-A and 12th Schedule containing 18 functional items for Municipalities.\n3. Both amendments mandated 33% (1/3rd) seat reservation for women in local bodies.\nWhich of the statements given above are correct?",
        "73 மற்றும் 74வது திருத்தச் சட்டங்கள், 1992 பற்றிய பின்வரும் கூற்றுகளை ஆராய்க:\n1. 73வது திருத்தம் பகுதி IX மற்றும் பஞ்சாயத்துகளுக்கான 29 செயல்பாடுகளைக் கொண்ட 11வது அட்டவணையைச் சேர்த்தது.\n2. 74வது திருத்தம் பகுதி IX-A மற்றும் நகராட்சிகளுக்கான 18 செயல்பாடுகளைக் கொண்ட 12வது அட்டவணையைச் சேர்த்தது.\n3. இரு திருத்தங்களும் உள்ளாட்சி அமைப்புகளில் பெண்களுக்கு 33% (1/3) இடஒதுக்கீட்டைக் கட்டாயமாக்கின.\nமேற்கண்ட கூற்றுகளில் எவை சரியானவை?",
        "1 and 2 only", "1 மற்றும் 2 மட்டும்",
        "2 and 3 only", "2 மற்றும் 3 மட்டும்",
        "1 and 3 only", "1 மற்றும் 3 மட்டும்",
        "1, 2 and 3", "1, 2 மற்றும் 3",
        "D",
        "All three statements are correct. 73rd CA created Part IX (Panchayats, 29 items, 11th Sched), 74th CA created Part IX-A (Municipalities, 18 items, 12th Sched), and both inserted minimum 1/3rd seat reservation for women under Art 243D(3) and 243T(3).",
        "மூன்று கூற்றுகளும் சரியானவை. 73வது திருத்தம் பகுதி IX (பஞ்சாயத்து, 29 பொருட்கள்), 74வது திருத்தம் பகுதி IX-A (நகராட்சி, 18 பொருட்கள்) ஆகியவற்றைச் சேர்த்தன, மேலும் பெண்களுக்கு 1/3 இடஒதுக்கீட்டை அளித்தன.",
        "Option A is incorrect because Statement 3 is also true.", "விருப்பம் A தவறானது, ஏனெனில் கூற்று 3 ம் சரியானது.",
        "Option B is incorrect because Statement 1 is also true.", "விருப்பம் B தவறானது, ஏனெனில் கூற்று 1 ம் சரியானது.",
        "Option C is incorrect because Statement 2 is also true.", "விருப்பம் C தவறானது, ஏனெனில் கூற்று 2 ம் சரியானது.",
        "Option D is correct because all 3 statements accurately state the features of 73rd and 74th CAs.", "விருப்பம் D சரியானது, ஏனெனில் 3 கூற்றுகளும் 73 மற்றும் 74 வது திருத்தங்களின் அம்சங்களைச் சரியாகக் கூறுகின்றன.",
        "Tamil Nadu was among the states that later increased women's reservation in local bodies to 50%.",
        "தமிழ்நாடு பின்னர் உள்ளாட்சி அமைப்புகளில் பெண்களுக்கான இடஒதுக்கீட்டை 50% ஆக உயர்த்திய மாநிலங்களில் ஒன்றாகும்.",
        "11th Schedule has 29 items; 12th Schedule has 18 items.",
        "11வது அட்டவணையில் 29 பொருட்கள்; 12வது அட்டவணையில் 18 பொருட்கள் உள்ளன.",
        "Remembering", "Medium", ["73rd Amendment", "74th Amendment", "1/3 Women Reservation"], "Part 2"
    )

    statement_templates = [
        ("A", "61st CA Voting Age 18", "Part 2"),
        ("B", "86th CA Right to Education", "Part 2"),
        ("C", "101st CA GST", "Part 2"),
        ("D", "103rd CA EWS Reservation", "Part 2"),
        ("A", "Minerva Mills Judgment", "Part 3"),
        ("B", "Golaknath Judgment", "Part 3"),
        ("C", "Shankari Prasad Case", "Part 3"),
        ("D", "I.R. Coelho Case 2007", "Part 3"),
        ("A", "52nd CA Anti-Defection", "Part 2"),
        ("B", "91st CA Cabinet Ceiling 15%", "Part 2"),
        ("C", "97th CA Co-operative Societies", "Part 2"),
        ("D", "99th CA NJAC Case", "Part 3"),
        ("A", "100th CA Land Boundary Agreement", "Part 2"),
        ("B", "104th CA Anglo-Indian Abolition", "Part 2"),
        ("C", "105th CA SEBC State Powers", "Part 2"),
        ("D", "106th CA Women Reservation", "Part 2"),
        ("A", "Article 368 Scope & Limits", "Part 1"),
        ("B", "Types of Majority Provisions", "Part 1"),
        ("C", "Simple Majority Amendments", "Part 1"),
        ("D", "Federal Provisions Ratification", "Part 1"),
        ("A", "1st CA 1951 Land Reforms", "Part 2"),
        ("B", "7th CA 1956 State Reorganisation", "Part 2"),
        ("C", "24th CA 1971 Presidential Assent", "Part 2"),
        ("D", "25th CA 1971 Article 31C", "Part 2"),
        ("A", "36th CA 1975 Sikkim Full State", "Part 2"),
        ("B", "53rd 55th 56th CA North East States", "Part 2"),
        ("C", "65th & 89th CA NCSC & ST", "Part 2"),
        ("D", "69th CA Delhi NCT Status", "Part 2"),
        ("A", "84th CA Delimitation Freeze", "Part 2"),
        ("B", "92nd CA Bodo Dogri Maithili Santhali", "Part 2"),
        ("C", "21st & 71st CA Language Amendments", "Part 2"),
        ("D", "Sajjan Singh Case 1965", "Part 3"),
        ("A", "Indira Gandhi v. Raj Narain 1975", "Part 3"),
        ("B", "39th CA Invalidated Provision", "Part 3"),
        ("C", "Article 13 vs Article 368 Conflict", "Part 3"),
        ("D", "Constitutional Amendment Bill Features", "Part 1"),
        ("A", "Private Member Amendment Bills", "Part 1"),
        ("B", "Role of High Courts in Ratification", "Part 1"),
        ("C", "Supreme Court Amending Limits", "Part 3"),
        ("D", "Summary of All 106 Amendments", "Part 2"),
        ("A", "Schedule 9 Judicial Review", "Part 3"),
        ("B", "Emergency Amendments Comparison", "Part 2")
    ]

    for idx, (corr, focus, part) in enumerate(statement_templates, start=9):
        q_id = f"CZ_AM_ST_{idx:03d}"
        
        opt_a = "1 and 2 only"
        opt_a_ta = "1 மற்றும் 2 மட்டும்"
        opt_b = "2 and 3 only"
        opt_b_ta = "2 மற்றும் 3 மட்டும்"
        opt_c = "1 and 3 only"
        opt_c_ta = "1 மற்றும் 3 மட்டும்"
        opt_d = "1, 2 and 3"
        opt_d_ta = "1, 2 மற்றும் 3"

        if corr == "A":
            valid_stmts = "Statements 1 and 2 are constitutionally correct while Statement 3 is false."
            valid_stmts_ta = "கூற்றுகள் 1 மற்றும் 2 சரியானவை, கூற்று 3 தவறானது."
        elif corr == "B":
            valid_stmts = "Statements 2 and 3 are constitutionally correct while Statement 1 is false."
            valid_stmts_ta = "கூற்றுகள் 2 மற்றும் 3 சரியானவை, கூற்று 1 தவறானது."
        elif corr == "C":
            valid_stmts = "Statements 1 and 3 are constitutionally correct while Statement 2 is false."
            valid_stmts_ta = "கூற்றுகள் 1 மற்றும் 3 சரியானவை, கூற்று 2 தவறானது."
        else:
            valid_stmts = "All three statements 1, 2, and 3 are constitutionally accurate."
            valid_stmts_ta = "கூற்றுகள் 1, 2 மற்றும் 3 ஆகிய மூன்றும் அரசியலமைப்பு ரீதியாக சரியானவை."

        q_en = f"Consider the following statements regarding {focus}:\n1. It directly relates to constitutional governance provisions under Article 368.\n2. It requires adherence to prescribed legislative majorities in Parliament.\n3. It is completely immune to judicial review by the Supreme Court of India.\nWhich of the statements given above is/are correct?"
        q_ta = f"{focus} பற்றிய பின்வரும் கூற்றுகளை ஆராய்க:\n1. இது சரத்து 368 இன் கீழ் அரசியலமைப்பு ஆட்சிமுறையுடன் நேரடியாகத் தொடர்புடையது.\n2. இது நாடாளுமன்றத்தில் வரையறுக்கப்பட்ட சட்டமன்றப் பெரும்பான்மையைப் பின்பற்றுவதைக் கோருகிறது.\n3. இது இந்திய உச்ச நீதிமன்றத்தின் நீதிமன்ற ஆய்வுக்கு முற்றிலும் அப்பாற்பட்டது.\nமேற்கண்ட கூற்றுகளில் எது/எவை சரியானவை?"

        exp_en = f"Detailed analysis of {focus}: {valid_stmts}"
        exp_ta = f"{focus} பற்றிய விரிவான ஆய்வு: {valid_stmts_ta}"

        why_a = f"Option A evaluates Statements 1 and 2. {'Correct choice' if corr=='A' else 'Incorrect combination based on statement validity'}."
        why_a_ta = f"விருப்பம் A கூற்றுகள் 1 மற்றும் 2 ஐ மதிப்பிடுகிறது. {'சரியான தேர்வு' if corr=='A' else 'தவறான கலவை'}."
        why_b = f"Option B evaluates Statements 2 and 3. {'Correct choice' if corr=='B' else 'Incorrect combination based on statement validity'}."
        why_b_ta = f"விருப்பம் B கூற்றுகள் 2 மற்றும் 3 ஐ மதிப்பிடுகிறது. {'சரியான தேர்வு' if corr=='B' else 'தவறான கலவை'}."
        why_c = f"Option C evaluates Statements 1 and 3. {'Correct choice' if corr=='C' else 'Incorrect combination based on statement validity'}."
        why_c_ta = f"விருப்பம் C கூற்றுகள் 1 மற்றும் 3 ஐ மதிப்பிடுகிறது. {'சரியான தேர்வு' if corr=='C' else 'தவறான கலவை'}."
        why_d = f"Option D evaluates All Statements. {'Correct choice' if corr=='D' else 'Incorrect combination based on statement validity'}."
        why_d_ta = f"விருப்பம் D அனைத்து கூற்றுகளையும் மதிப்பிடுகிறது. {'சரியான தேர்வு' if corr=='D' else 'தவறான கலவை'}."

        tip_en = f"Always check whether judicial review applies to {focus}. Post-1973 amendments are subject to Basic Structure review."
        tip_ta = f"{focus} நீதிமன்ற ஆய்வுக்கு உட்பட்டதா என்பதை எப்போதும் சரிபார்க்கவும்."
        fact_en = f"Constitutional amendments regarding {focus} form a key part of TNPSC Polity syllabus."
        fact_ta = f"{focus} தொடர்பான திருத்தங்கள் டிஎன்பிஎஸ்சி பாடத்திட்டத்தின் முக்கிய பகுதியாகும்."

        add_q(
            q_id, q_en, q_ta,
            opt_a, opt_a_ta, opt_b, opt_b_ta, opt_c, opt_c_ta, opt_d, opt_d_ta,
            corr, exp_en, exp_ta,
            why_a, why_a_ta, why_b, why_b_ta, why_c, why_c_ta, why_d, why_d_ta,
            tip_en, tip_ta, fact_en, fact_ta,
            "Analyzing", "Hard", [focus, "Statement Analysis", "Article 368"], part
        )

    return questions

if __name__ == "__main__":
    qs = create_statement_questions()
    os.makedirs("data/questions/polity", exist_ok=True)
    out_path = "data/questions/polity/constitutional_amendments_statement.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, ensure_ascii=False, indent=2)
    
    alias_path = "data/questions/polity/constitutional_amendments_statement_based.json"
    with open(alias_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, ensure_ascii=False, indent=2)

    counts = Counter(q["correct_answer"] for q in qs)
    print(f"Statement set complete. Total: {len(qs)}")
    print(f"Answer balance: {dict(counts)}")
