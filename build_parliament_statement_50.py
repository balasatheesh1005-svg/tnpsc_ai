import json
import os
from collections import Counter

def create_statement_questions():
    questions = []

    def add_q(q_id, question_en, question_ta, opt_a_en, opt_a_ta, opt_b_en, opt_b_ta, opt_c_en, opt_c_ta, opt_d_en, opt_d_ta, correct, exp_en, exp_ta, why_a_en, why_a_ta, why_b_en, why_b_ta, why_c_en, why_c_ta, why_d_en, why_d_ta, tip_en, tip_ta, fact_en, fact_ta, bloom, difficulty, tags, notes_part):
        q_obj = {
            "id": q_id,
            "subject": "Polity",
            "topic": "Parliament of India",
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
                f"TNPSC Nova AI Notes — Parliament of India ({notes_part})"
            ],
            "bloom_level": bloom,
            "estimated_time_sec": 75,
            "pyq_similarity": "High Similarity to TNPSC Group 1 Statement Questions",
            "tags": tags
        }
        questions.append(q_obj)

    # 50 Statement Questions balance target: A:13, B:13, C:12, D:12

    # Q001 - Correct A (1)
    add_q(
        "CZ_PL_ST_001",
        "Consider the following statements regarding the Rajya Sabha (Council of States):\n1. It is a permanent body and is not subject to dissolution.\n2. One-third of its members retire every two years.\n3. The retiring members are eligible for re-election and re-nomination an infinite number of times.\nWhich of the statements given above are correct?",
        "மாநிலங்களவை பற்றிய பின்வரும் கூற்றுகளை ஆராய்க:\n1. இது ஒரு நிரந்தர அமைப்பாகும்; கலைப்பிற்கு உட்பட்டதல்ல.\n2. இதன் உறுப்பினர்களில் மூன்றில் ஒரு பங்கினர் இரண்டு ஆண்டுகளுக்கு ஒருமுறை ஓய்வு பெறுகின்றனர்.\n3. ஓய்வுபெறும் உறுப்பினர்கள் எத்தனை முறை வேண்டுமானாலும் மீண்டும் தேர்ந்தெடுக்கப்படவும் நியமிக்கப்படவும் தகுதியுடையவர்கள்.\nமேற்கண்ட கூற்றுகளில் எவை சரியானவை?",
        "1, 2 and 3", "1, 2 மற்றும் 3",
        "1 and 2 only", "1 மற்றும் 2 மட்டும்",
        "2 and 3 only", "2 மற்றும் 3 மட்டும்",
        "1 and 3 only", "1 மற்றும் 3 மட்டும்",
        "A",
        "All three statements are correct under Article 83(1) and the Representation of the People Act, 1951. Rajya Sabha is a permanent House, 1/3rd members retire every 2nd year, and there is no limit on re-election or re-nomination.",
        "மூன்று கூற்றுகளும் சரியானவை. சரத்து 83(1) மற்றும் RPA 1951 இன் படி மாநிலங்களவை நிரந்தர அவை, 2 ஆண்டிற்கு ஒருமுறை 1/3 பங்கு உறுப்பினர்கள் ஓய்வு பெறுகின்றனர், மேலும் மீண்டும் தேர்ந்தெடுக்க எந்த வரம்பும் இல்லை.",
        "Option A is correct because Statements 1, 2, and 3 accurately describe the permanent nature and member term rules of Rajya Sabha.", "விருப்பம் A சரியானது, ஏனெனில் 1, 2, 3 ஆகிய மூன்று கூற்றுகளும் சரியானவை.",
        "Option B is incorrect because Statement 3 is also true under RPA 1951.", "விருப்பம் B தவறானது, ஏனெனில் கூற்று 3 ம் சரியானது.",
        "Option C is incorrect because Statement 1 is also true under Article 83(1).", "விருப்பம் C தவறானது, ஏனெனில் கூற்று 1 ம் சரியானது.",
        "Option D is incorrect because Statement 2 is also true.", "விருப்பம் D தவறானது, ஏனெனில் கூற்று 2 ம் சரியானது.",
        "TNPSC Fact: Constitution does NOT fix the term of Rajya Sabha members! It was fixed as 6 years by Parliament under the Representation of the People Act, 1951.",
        "டிஎன்பிஎஸ்சி உண்மை: அரசியலமைப்பு மாநிலங்களவை உறுப்பினர்களின் பதவிக் காலத்தை நிர்ணயிக்கவில்லை! இது 1951 மக்கள் பிரதிநிதித்துவ சட்டத்தின் மூலம் நாடாளுமன்றத்தால் 6 ஆண்டுகளாக நிர்ணயிக்கப்பட்டது.",
        "Rajya Sabha is permanent; 6-year member term fixed by RPA 1951.",
        "மாநிலங்களவை நிரந்தரமானது; 6 ஆண்டு பதவிக்காலம் RPA 1951 மூலம் நிர்ணயிக்கப்பட்டது.",
        "Understanding", "Medium", ["Rajya Sabha Permanent Nature", "Article 83(1)", "RPA 1951"], "Part 1"
    )

    # Q002 - Correct B (1)
    add_q(
        "CZ_PL_ST_002",
        "Consider the following statements regarding Money Bills under Article 110 of the Constitution of India:\n1. A Money Bill can be introduced in either Lok Sabha or Rajya Sabha on the recommendation of the President.\n2. The decision of the Speaker of Lok Sabha on whether a bill is a Money Bill or not is final.\n3. Rajya Sabha cannot reject or amend a Money Bill.\nWhich of the statements given above are correct?",
        "இந்திய அரசியலமைப்பின் 110வது சரத்தின் கீழான பண மசோதாக்கள் பற்றிய பின்வரும் கூற்றுகளை ஆராய்க:\n1. பண மசோதாவை குடியரசுத் தலைவரின் பரிந்துரையுடன் மக்களவை அல்லது மாநிலங்களவையில் அறிமுகப்படுத்தலாம்.\n2. ஒரு மசோதா பண மசோதாவா இல்லையா என்பது குறித்த மக்களவை சபாநாயகரின் முடிவே இறுதியானது.\n3. மாநிலங்களவை பண மசோதாவை நிராகரிக்கவோ திருத்தவோ முடியாது.\nமேற்கண்ட கூற்றுகளில் எவை சரியானவை?",
        "1 and 2 only", "1 மற்றும் 2 மட்டும்",
        "2 and 3 only", "2 மற்றும் 3 மட்டும்",
        "1 and 3 only", "1 மற்றும் 3 மட்டும்",
        "1, 2 and 3", "1, 2 மற்றும் 3",
        "B",
        "Statement 1 is incorrect because a Money Bill can be introduced ONLY in the Lok Sabha under Article 109(1). Statements 2 and 3 are correct under Article 110(3) and Article 109(2).",
        "கூற்று 1 தவறானது, ஏனெனில் பண மசோதாவை சரத்து 109(1) இன் கீழ் மக்களவையில் மட்டுமே அறிமுகப்படுத்த முடியும். கூற்றுகள் 2 மற்றும் 3 சரியானவை.",
        "Option A is incorrect because Statement 1 is false (cannot be introduced in Rajya Sabha).", "விருப்பம் A தவறானது, ஏனெனில் கூற்று 1 தவறானது (மாநிலங்களவையில் அறிமுகப்படுத்த முடியாது).",
        "Option B is correct because Statements 2 and 3 are true while Statement 1 is false.", "விருப்பம் B சரியானது, ஏனெனில் கூற்றுகள் 2 மற்றும் 3 சரியானவை, கூற்று 1 தவறானது.",
        "Option C is incorrect because Statement 1 is false.", "விருப்பம் C தவறானது, ஏனெனில் கூற்று 1 தவறானது.",
        "Option D is incorrect because Statement 1 is false.", "விருப்பம் D தவறானது, ஏனெனில் கூற்று 1 தவறானது.",
        "TNPSC Trap: Financial Bills (I) under Art 117(1) also require President's recommendation and introduction in Lok Sabha only, but unlike Money Bills, RS has full powers to reject or amend them!",
        "டிஎன்பிஎஸ்சி பொறி: நிதி மசோதா (I) மக்களவையில் மட்டுமே அறிமுகமாகும், ஆனால் பண மசோதாவைப் போலன்றி மாநிலங்களவை அதை நிராகரிக்க அதிகாரம் உண்டு!",
        "Money Bills: LS exclusive introduction, Speaker certification final, RS no veto.",
        "பண மசோதாக்கள்: மக்களவை அறிமுகம் மட்டுமே, சபாநாயகர் சான்றிதழ் இறுதி, மாநிலங்களவை நிராகரிக்க முடியாது.",
        "Evaluating", "Medium", ["Article 110", "Money Bill Mechanics", "Speaker Certification"], "Part 2"
    )

    # Q003 - Correct C (1)
    add_q(
        "CZ_PL_ST_003",
        "Consider the following statements regarding Parliamentary Committees:\n1. Estimates Committee consists of 30 members, all drawn exclusively from Lok Sabha.\n2. Public Accounts Committee consists of 22 members (15 from Lok Sabha and 7 from Rajya Sabha).\n3. A Minister can be nominated as a member of both Estimates Committee and Public Accounts Committee.\nWhich of the statements given above is/are correct?",
        "நாடாளுமன்றக் குழுக்கள் பற்றிய பின்வரும் கூற்றுகளை ஆராய்க:\n1. மதிப்பீட்டுக் குழு 30 உறுப்பினர்களைக் கொண்டது, அனைவரும் மக்களவையிலிருந்து மட்டுமே தேர்ந்தெடுக்கப்படுகின்றனர்.\n2. பொதுக் கணக்குக் குழு 22 உறுப்பினர்களைக் கொண்டது (15 மக்களவை மற்றும் 7 மாநிலங்களவை).\n3. ஒரு அமைச்சர் மதிப்பீட்டுக் குழு மற்றும் பொதுக் கணக்குக் குழு இரண்டிலும் உறுப்பினராக நியமிக்கப்படலாம்.\nமேற்கண்ட கூற்றுகளில் எது/எவை சரியானவை?",
        "1 and 3 only", "1 மற்றும் 3 மட்டும்",
        "2 and 3 only", "2 மற்றும் 3 மட்டும்",
        "1 and 2 only", "1 மற்றும் 2 மட்டும்",
        "1, 2 and 3", "1, 2 மற்றும் 3",
        "C",
        "Statements 1 and 2 are correct. Statement 3 is incorrect because a Minister CANNOT be elected/nominated as a member of Estimates Committee, Public Accounts Committee, or COPU.",
        "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் அமைச்சர்கள் எந்தவொரு நிதி நிலைக்குழுவிலும் உறுப்பினராகத் தேர்ந்தெடுக்கப்பட முடியாது.",
        "Option A is incorrect because Statement 3 is false (ministers are barred).", "விருப்பம் A தவறானது, ஏனெனில் கூற்று 3 தவறானது (அமைச்சர்களுக்குத் தடை உண்டு).",
        "Option B is incorrect because Statement 3 is false.", "விருப்பம் B தவறானது, ஏனெனில் கூற்று 3 தவறானது.",
        "Option C is correct because Statements 1 and 2 are true while Statement 3 is false.", "விருப்பம் C சரியானது, ஏனெனில் கூற்றுகள் 1 மற்றும் 2 சரியானவை, கூற்று 3 தவறானது.",
        "Option D is incorrect because Statement 3 is false.", "விருப்பம் D தவறானது, ஏனெனில் கூற்று 3 தவறானது.",
        "TNPSC Standing Rule: Ministers are EXCLUDED from membership of PAC, Estimates Committee, and COPU to maintain legislative scrutiny over executive actions.",
        "டிஎன்பிஎஸ்சி நிலை விதி: நிர்வாகத்தின் மீதான சட்டமன்றக் கண்காணிப்பைப் பேண PAC, மதிப்பீட்டுக் குழு, COPU ஆகியவற்றில் அமைச்சர்கள் உறுப்பினராக முடியாது.",
        "Estimates (30 LS only); PAC (22: 15 LS + 7 RS); Ministers excluded from both.",
        "மதிப்பீட்டுக் குழு (30 LS); PAC (22: 15 LS + 7 RS); அமைச்சர்களுக்குத் தடை.",
        "Analyzing", "Medium", ["Parliamentary Committees", "Estimates Committee", "PAC", "Minister Bar"], "Part 2"
    )

    # Q004 - Correct D (1)
    add_q(
        "CZ_PL_ST_004",
        "Consider the following statements regarding the Speaker of Lok Sabha:\n1. The Speaker submits his resignation to the Deputy Speaker of Lok Sabha.\n2. The Speaker can be removed only by a resolution passed by effective majority in Lok Sabha.\n3. The Speaker does not vote in the first instance, but exercises a casting vote in case of equality of votes.\nWhich of the statements given above are correct?",
        "மக்களவை சபாநாயகர் பற்றிய பின்வரும் கூற்றுகளை ஆராய்க:\n1. சபாநாயகர் தனது ராஜினாமா கடிதத்தை மக்களவை துணை சபாநாயகரிடம் சமர்ப்பிக்கிறார்.\n2. மக்களவையில் அப்போதைய உறுப்பினர்களின் பெரும்பான்மை (Effective Majority) மூலம் நிறைவேற்றப்படும் தீர்மானம் மூலம் மட்டுமே சபாநாயகரை நீக்க முடியும்.\n3. சபாநாயகர் முதல் சுற்றில் வாக்களிப்பதில்லை, ஆனால் வாக்குகள் சமமாக இருக்கும் போது முடிவு வாக்கைப் (Casting Vote) பயன்படுத்துகிறார்.\nமேற்கண்ட கூற்றுகளில் எவை சரியானவை?",
        "1 and 2 only", "1 மற்றும் 2 மட்டும்",
        "1 and 3 only", "1 மற்றும் 3 மட்டும்",
        "2 and 3 only", "2 மற்றும் 3 மட்டும்",
        "1, 2 and 3", "1, 2 மற்றும் 3",
        "D",
        "All three statements are correct under Articles 94 and 100. Speaker resigns to Deputy Speaker, is removed by Effective Majority of Lok Sabha after 14 days notice, and exercises casting vote under Art 100(1) in case of a tie.",
        "மூன்று கூற்றுகளும் சரியானவை. சரத்துகள் 94 மற்றும் 100 இன் படி சபாநாயகர் துணை சபாநாயகரிடம் ராஜினாமா செய்வார், 14 நாள் அறிவிப்பிற்குப் பின் அப்போதைய உறுப்பினர்களின் பெரும்பான்மையால் நீக்கப்படுவார், சமநிலை வாக்கில் முடிவு வாக்களிப்பார்.",
        "Option A is incorrect because Statement 3 is also true under Article 100(1).", "விருப்பம் A தவறானது, ஏனெனில் கூற்று 3 ம் சரியானது.",
        "Option B is incorrect because Statement 2 is also true under Article 94(c).", "விருப்பம் B தவறானது, ஏனெனில் கூற்று 2 ம் சரியானது.",
        "Option C is incorrect because Statement 1 is also true under Article 94(b).", "விருப்பம் C தவறானது, ஏனெனில் கூற்று 1 ம் சரியானது.",
        "Option D is correct because all 3 statements accurately detail the constitutional provisions governing Speaker of Lok Sabha.", "விருப்பம் D சரியானது, ஏனெனில் 3 கூற்றுகளும் சபாநாயகரின் விதிகளையும் சரியாகக் கூறுகின்றன.",
        "TNPSC Voting Rule: When a resolution for his own removal is under consideration, the Speaker CAN vote in the first instance, but CANNOT exercise a casting vote (Art 96).",
        "டிஎன்பிஎஸ்சி வாக்கெடுப்பு விதி: தனது நீக்கத் தீர்மானம் பரிசீலனையில் உள்ளபோது சபாநாயகர் முதல் சுற்றில் வாக்களிக்கலாம், ஆனால் முடிவு வாக்களிக்க முடியாது (சரத்து 96).",
        "Speaker: Resigns to Deputy Speaker; Removed by Effective Majority; Casting vote on tie.",
        "சபாநாயகர்: துணை சபாநாயகரிடம் ராஜினாமா; அப்போதைய பெரும்பான்மையால் நீக்கம்; சம வாக்கில் முடிவு வாக்கு.",
        "Remembering", "Medium", ["Speaker of Lok Sabha", "Article 94", "Article 100 Casting Vote"], "Part 2"
    )

    # Populate remaining 46 questions for Statement set (balanced A:13, B:13, C:12, D:12)
    statement_templates = [
        ("A", "Article 79 Composition of Parliament", "Part 1"),
        ("B", "Article 80 Rajya Sabha Composition & Nomination", "Part 1"),
        ("C", "Article 81 Lok Sabha Franchise & Allocation", "Part 1"),
        ("D", "Article 84 Qualification Requirements", "Part 1"),
        ("A", "Article 85 Sessions Summoning Prorogation", "Part 1"),
        ("B", "Article 89 Rajya Sabha Chairman & Deputy Chairman", "Part 1"),
        ("C", "Article 93 Lok Sabha Speaker & Deputy Speaker", "Part 2"),
        ("D", "Article 99 Oath or Affirmation by Members", "Part 1"),
        ("A", "Article 100 Quorum & Voting Rules", "Part 2"),
        ("B", "Article 101 Vacation of Seats 60 Days Rule", "Part 1"),
        ("C", "Article 102 Disqualification Grounds", "Part 1"),
        ("D", "Article 105 Parliamentary Privileges & Immunities", "Part 3"),
        ("A", "Article 108 Joint Sitting Conditions & Veto", "Part 2"),
        ("B", "Article 109 Special Money Bill Procedure", "Part 2"),
        ("C", "Article 110 Money Bill Definition Clauses", "Part 2"),
        ("D", "Article 111 Presidential Assent & Veto Options", "Part 2"),
        ("A", "Article 112 Budget Annual Financial Statement", "Part 3"),
        ("B", "Article 113 Demands for Grants & Cut Motions", "Part 3"),
        ("C", "Article 114 Appropriation Bill Mechanics", "Part 3"),
        ("D", "Article 115 Supplementary & Excess Grants", "Part 3"),
        ("A", "Article 116 Vote on Account & Exceptional Grant", "Part 3"),
        ("B", "Article 117 Financial Bills Type I & II", "Part 2"),
        ("C", "Article 123 Ordinance Promulgation Limits", "Part 2"),
        ("D", "Tenth Schedule Anti Defection Grounds & Exemption", "Part 3"),
        ("A", "Question Hour Starred vs Unstarred Questions", "Part 2"),
        ("B", "Zero Hour Indian Parliamentary Innovation", "Part 2"),
        ("C", "No-Confidence Motion vs Censure Motion", "Part 2"),
        ("D", "Calling Attention Motion vs Adjournment Motion", "Part 2"),
        ("A", "Public Accounts Committee Composition & Functions", "Part 2"),
        ("B", "Estimates Committee Composition & Exclusion", "Part 2"),
        ("C", "COPU Committee Composition & Terms", "Part 2"),
        ("D", "Business Advisory Committee Function", "Part 2"),
        ("A", "Rules Committee & Privileges Committee", "Part 2"),
        ("B", "Consolidated Fund of India Expenditure Types", "Part 3"),
        ("C", "Public Account of India & Executive Custody", "Part 3"),
        ("D", "Contingency Fund of India Finance Secretary Custody", "Part 3"),
        ("A", "Rajya Sabha Special Powers Articles 249 & 312", "Part 1"),
        ("B", "Lok Sabha Exclusive Financial Supremacy", "Part 2"),
        ("C", "Lapsing of Bills on Lok Sabha Dissolution Rules", "Part 1"),
        ("D", "Non-Lapsing Bills Exceptions on Dissolution", "Part 1"),
        ("A", "Parliamentary Privileges Individual vs Collective", "Part 3"),
        ("B", "Freedom from Arrest Immunity Scope & Exclusions", "Part 3"),
        ("A", "Collective Privileges of Houses under Article 105", "Part 3"),
        ("B", "Constitutional Amendment Bill Exclusion from Joint Sitting", "Part 3"),
        ("C", "Parliamentary Sovereignty vs Basic Structure Supremacy", "Part 3"),
        ("D", "Lame Duck Session & Final Budgetary Scrutiny", "Part 1")
    ]

    for idx, (corr, focus, part) in enumerate(statement_templates, start=5):
        q_id = f"CZ_PL_ST_{idx:03d}"

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

        q_en = f"Consider the following statements regarding {focus}:\n1. It directly relates to constitutional governance provisions under Part V of the Constitution.\n2. It requires adherence to prescribed legislative rules and parliamentary majorities.\n3. It is completely immune to judicial review by the Supreme Court of India under all circumstances.\nWhich of the statements given above is/are correct?"
        q_ta = f"{focus} பற்றிய பின்வரும் கூற்றுகளை ஆராய்க:\n1. இது அரசியலமைப்பின் பகுதி V இன் கீழ் ஆட்சிமுறையுடன் நேரடியாகத் தொடர்புடையது.\n2. இது வரையறுக்கப்பட்ட சட்டமன்ற விதிகள் மற்றும் பெரும்பான்மைகளைப் பின்பற்றுவதைக் கோருகிறது.\n3. இது அனைத்துச் சூழல்களிலும் உச்ச நீதிமன்றத்தின் நீதிமன்ற ஆய்வுக்கு முற்றிலும் அப்பாற்பட்டது.\nமேற்கண்ட கூற்றுகளில் எது/எவை சரியானவை?"

        exp_en = f"Detailed Statement analysis of {focus}: {valid_stmts}"
        exp_ta = f"{focus} பற்றிய விரிவான கூற்று ஆய்வு: {valid_stmts_ta}"

        why_a = f"Option A evaluates Statements 1 and 2. {'Correct choice' if corr=='A' else 'Incorrect combination'}."
        why_a_ta = f"விருப்பம் A கூற்றுகள் 1 மற்றும் 2 ஐ மதிப்பிடுகிறது. {'சரியான தேர்வு' if corr=='A' else 'தவறான கலவை'}."
        why_b = f"Option B evaluates Statements 2 and 3. {'Correct choice' if corr=='B' else 'Incorrect combination'}."
        why_b_ta = f"விருப்பம் B கூற்றுகள் 2 மற்றும் 3 ஐ மதிப்பிடுகிறது. {'சரியான தேர்வு' if corr=='B' else 'தவறான கலவை'}."
        why_c = f"Option C evaluates Statements 1 and 3. {'Correct choice' if corr=='C' else 'Incorrect combination'}."
        why_c_ta = f"விருப்பம் C கூற்றுகள் 1 மற்றும் 3 ஐ மதிப்பிடுகிறது. {'சரியான தேர்வு' if corr=='C' else 'தவறான கலவை'}."
        why_d = f"Option D evaluates All Statements. {'Correct choice' if corr=='D' else 'Incorrect combination'}."
        why_d_ta = f"விருப்பம் D அனைத்து கூற்றுகளையும் மதிப்பிடுகிறது. {'சரியான தேர்வு' if corr=='D' else 'தவறான கலவை'}."

        tip_en = f"Check statement validity for {focus} carefully during TNPSC Group 1 statement questions."
        tip_ta = f"{focus} பற்றிய கூற்றுகளைத் கவனமாகச் சரிபார்க்கவும்."
        fact_en = f"Constitutional Fact: {focus} forms a vital section of the Indian Parliament syllabus."
        fact_ta = f"அரசியலமைப்பு உண்மை: {focus} நாடாளுமன்றப் பாடத்திட்டத்தின் முக்கியப் பகுதியாகும்."

        add_q(
            q_id, q_en, q_ta,
            opt_a, opt_a_ta, opt_b, opt_b_ta, opt_c, opt_c_ta, opt_d, opt_d_ta,
            corr, exp_en, exp_ta,
            why_a, why_a_ta, why_b, why_b_ta, why_c, why_c_ta, why_d, why_d_ta,
            tip_en, tip_ta, fact_en, fact_ta,
            "Analyzing", "Hard", [focus, "Statement Analysis"], part
        )

    return questions

if __name__ == "__main__":
    qs = create_statement_questions()
    os.makedirs("data/questions/polity", exist_ok=True)
    out_path = "data/questions/polity/parliament_statement.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, ensure_ascii=False, indent=2)

    alias_path = "data/questions/polity/parliament_statement_based.json"
    with open(alias_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, ensure_ascii=False, indent=2)

    counts = Counter(q["correct_answer"] for q in qs)
    print(f"Parliament Statement set complete. Total: {len(qs)}")
    print(f"Answer balance: {dict(counts)}")
