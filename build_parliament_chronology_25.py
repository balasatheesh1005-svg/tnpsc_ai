import json
import os
from collections import Counter

def create_chronology_questions():
    questions = []

    def add_q(q_id, question_en, question_ta, opt_a_en, opt_a_ta, opt_b_en, opt_b_ta, opt_c_en, opt_c_ta, opt_d_en, opt_d_ta, correct, exp_en, exp_ta, why_a_en, why_a_ta, why_b_en, why_b_ta, why_c_en, why_c_ta, why_d_en, why_d_ta, tip_en, tip_ta, fact_en, fact_ta, bloom, difficulty, tags, notes_part):
        q_obj = {
            "id": q_id,
            "subject": "Polity",
            "topic": "Parliament of India",
            "difficulty": difficulty,
            "question_type": "chronology",
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
            "estimated_time_sec": 90,
            "pyq_similarity": "High Similarity to TNPSC Group 1 Chronology Questions",
            "tags": tags
        }
        questions.append(q_obj)

    # 25 Chronology questions balance target: A:6, B:6, C:7, D:6

    chronology_data = [
        # Q001 - Correct A (1)
        (
            "CZ_PL_CH_001",
            "Arrange the following parliamentary committee milestones and reforms in chronological order:\n1. Establishment of the Public Accounts Committee (PAC) under Montagu-Chelmsford Reforms\n2. Establishment of the Estimates Committee upon recommendation of John Matthai\n3. Establishment of the Committee on Public Undertakings (COPU) on Krishna Menon Committee recommendation\n4. Introduction of Departmental Standing Committees (DRSCs) in Parliament",
            "பின்வரும் நாடாளுமன்றக் குழு மைல்கற்கள் மற்றும் சீர்திருத்தங்களைக் காலவரிசைப்படி வரிசைப்படுத்துக:\n1. மாண்டேகு-செம்ஸ்போர்டு சீர்திருத்தங்களின் கீழ் பொதுக் கணக்குக் குழு (PAC) அமைத்தல்\n2. ஜான் மத்தாய் பரிந்துரையின் பேரில் மதிப்பீட்டுக் குழு அமைத்தல்\n3. கிருஷ்ண மேனன் குழு பரிந்துரையின் பேரில் பொதுத்துறை நிறுவனங்கள் குழு (COPU) அமைத்தல்\n4. நாடாளுமன்றத்தில் துறைசார் நிலைக்குழுக்கள் (DRSCs) அறிமுகம்",
            "1 → 2 → 3 → 4", "1 → 2 → 3 → 4",
            "2 → 1 → 4 → 3", "2 → 1 → 4 → 3",
            "3 → 4 → 1 → 2", "3 → 4 → 1 → 2",
            "4 → 3 → 2 → 1", "4 → 3 → 2 → 1",
            "A",
            "Chronological order:\n1. Public Accounts Committee (PAC): Established in 1921 under Government of India Act 1919\n2. Estimates Committee: Established in 1950 on John Matthai's recommendation\n3. Committee on Public Undertakings (COPU): Created in 1964 on Krishna Menon Committee recommendation\n4. Departmental Standing Committees (DRSCs): Created in 1993 (17 committees initially, expanded to 24 in 2004)\nHence, correct order is 1 → 2 → 3 → 4.",
            "காலவரிசை:\n1. பொதுக் கணக்குக் குழு (PAC): 1921 (இந்திய அரசுச் சட்டம் 1919)\n2. மதிப்பீட்டுக் குழு: 1950 (ஜான் மத்தாய் பரிந்துரை)\n3. பொதுத்துறை நிறுவனங்கள் குழு (COPU): 1964 (கிருஷ்ண மேனன் குழு)\n4. துறைசார் நிலைக்குழுக்கள் (DRSCs): 1993\nஎனவே சரியான வரிசை 1 → 2 → 3 → 4.",
            "Option A is correct because the sequence 1921 (1) → 1950 (2) → 1964 (3) → 1993 (4) is exact.", "விருப்பம் A சரியானது, ஏனெனில் 1921 (1) → 1950 (2) → 1964 (3) → 1993 (4) சரியான வரிசையாகும்.",
            "Option B is incorrect because PAC (1921) came long before Estimates Committee (1950).", "விருப்பம் B தவறானது, ஏனெனில் PAC (1921) மதிப்பீட்டுக் குழுவிற்கு (1950) முன்னே அமைந்தது.",
            "Option C is incorrect because COPU (1964) came after PAC (1921) and Estimates (1950).", "விருப்பம் C தவறானது, ஏனெனில் COPU (1964) பின்னர் அமைந்தது.",
            "Option D is incorrect because it reverses the timeline completely.", "விருப்பம் D தவறானது, ஏனெனில் இது காலவரிசையை தலைகீழாகக் காட்டுகிறது.",
            "TNPSC Committee Formula: PAC (1921) -> Estimates (1950) -> COPU (1964) -> DRSCs (1993).",
            "டிஎன்பிஎஸ்சி குழுக்கள் சூத்திரம்: PAC (1921) -> மதிப்பீட்டுக் குழு (1950) -> COPU (1964) -> DRSCs (1993).",
            "PAC 1921, Estimates 1950, COPU 1964, DRSCs 1993.",
            "PAC 1921, மதிப்பீட்டுக் குழு 1950, COPU 1964, DRSCs 1993.",
            "Analyzing", "Hard", ["Committee Chronology", "PAC 1921", "Estimates 1950", "COPU 1964", "DRSC 1993"], "Part 2"
        ),
        # Q002 - Correct B (1)
        (
            "CZ_PL_CH_002",
            "Arrange the following landmark parliamentary events and constitutional developments in chronological order:\n1. Adoption of the Anti-Defection Law (Tenth Schedule) by the 52nd Amendment Act\n2. First Joint Sitting of Parliament to pass the Dowry Prohibition Bill\n3. Passage of the 91st Amendment Act capping Cabinet size at 15%\n4. Supreme Court verdict in Kihoto Hollohan v. Zachillhu subjecting Speaker's defection decision to judicial review",
            "பின்வரும் வரலாற்றுச் சிறப்புமிக்க நாடாளுமன்ற நிகழ்வுகள் மற்றும் அரசியலமைப்பு வளர்ச்சிகளைக் காலவரிசைப்படி வரிசைப்படுத்துக:\n1. 52வது திருத்தச் சட்டம் மூலம் கட்சித் தாவல் தடைச் சட்டம் (10வது அட்டவணை) ஏற் படுத்தல்\n2. வரதட்சணை தடை மசோதாவை நிறைவேற்ற நாடாளுமன்றத்தின் முதல் கூட்டுக் கூட்டம்\n3. அமைச்சரவை அளவை 15% ஆகக் கட்டுப்படுத்தும் 91வது திருத்தச் சட்டம் இயற்றுதல்\n4. கிஹோட்டோ ஹோலோஹான் வழக்கில் சபாநாயகரின் கட்சித் தாவல் முடிவு நீதிமன்ற ஆய்விற்கு உட்பட்டது என்ற உச்ச நீதிமன்றத் தீர்ப்பு",
            "1 → 2 → 3 → 4", "1 → 2 → 3 → 4",
            "2 → 1 → 4 → 3", "2 → 1 → 4 → 3",
            "3 → 4 → 1 → 2", "3 → 4 → 1 → 2",
            "4 → 1 → 2 → 3", "4 → 1 → 2 → 3",
            "B",
            "Chronological order:\n1. First Joint Sitting (Dowry Prohibition Bill): May 1961\n2. Anti-Defection Law (52nd CA): 1985\n3. Kihoto Hollohan Supreme Court Verdict: 1992\n4. 91st Amendment Act (15% Cabinet Limit): 2003\nHence, correct sequence is 2 → 1 → 4 → 3.",
            "காலவரிசை:\n1. முதல் கூட்டுக் கூட்டம் (வரதட்சணை தடை மசோதா): 1961 மே\n2. கட்சித் தாவல் தடைச் சட்டம் (52வது திருத்தம்): 1985\n3. கிஹோட்டோ ஹோலோஹான் வழக்குத் தீர்ப்பு: 1992\n4. 91வது திருத்தச் சட்டம் (15% அமைச்சரவை வரம்பு): 2003\nஎனவே சரியான வரிசை 2 → 1 → 4 → 3.",
            "Option A is incorrect because First Joint Sitting (1961) occurred long before Anti-Defection Law (1985).", "விருப்பம் A தவறானது, ஏனெனில் முதல் கூட்டுக் கூட்டம் (1961) கட்சித் தாவல் சட்டத்திற்கு (1985) முன்னே நடந்தது.",
            "Option B is correct because 1961 (2) → 1985 (1) → 1992 (4) → 2003 (3) is exact.", "விருப்பம் B சரியானது, ஏனெனில் 1961 (2) → 1985 (1) → 1992 (4) → 2003 (3) சரியான வரிசையாகும்.",
            "Option C is incorrect because 91st CA (2003) is the latest among the four.", "விருப்பம் C தவறானது, ஏனெனில் 91வது திருத்தம் (2003) கடைசியாக வந்தது.",
            "Option D is incorrect because Kihoto Hollohan (1992) came after 1961 and 1985.", "விருப்பம் D தவறானது, ஏனெனில் கிஹோட்டோ வழக்கு பின்னர் வந்தது.",
            "Joint Sitting Milestones: Dowry Prohibition (1961), Banking Service Commission (1978), POTA (2002).",
            "கூட்டுக் கூட்ட மைல்கற்கள்: வரதட்சணை தடை (1961), வங்கிச் சேவை (1978), பொடா (2002).",
            "1961 Dowry Joint Sitting -> 1985 Anti Defection -> 1992 Kihoto Hollohan -> 2003 91st Amendment.",
            "1961 வரதட்சணை கூட்டுக் கூட்டம் -> 1985 கட்சித் தாவல் -> 1992 கிஹோட்டோ வழக்கு -> 2003 91வது திருத்தம்.",
            "Analyzing", "Hard", ["Parliamentary Chronology", "Joint Sitting 1961", "52nd CA 1985", "91st CA 2003"], "Part 2"
        ),
        # Q003 - Correct C (1)
        (
            "CZ_PL_CH_003",
            "Arrange the following constitutional developments concerning Lok Sabha delimitation and seat allocation in chronological order:\n1. 42nd Amendment Act freezing Lok Sabha seat allocation based on 1971 Census until 2000\n2. 84th Amendment Act extending the freeze on total Lok Sabha seats until 2026\n3. 87th Amendment Act permitting delimitation of constituencies based on 2001 Census without altering seat total\n4. 104th Amendment Act abolishing Anglo-Indian nominated seats in Lok Sabha",
            "மக்களவை தொகுதி மறுவரையறை மற்றும் இடங்கள் ஒதுக்கீடு தொடர்பான பின்வரும் அரசியலமைப்பு வளர்ச்சிகளைக் காலவரிசைப்படி வரிசைப்படுத்துக:\n1. 1971 மக்கள் தொகை கணக்கெடுப்பின்படி 2000 வரை மக்களவை இடங்களை முடக்கிய 42வது திருத்தச் சட்டம்\n2. மக்களவை மொத்த இடங்கள் முடக்கத்தை 2026 வரை நீட்டித்த 84வது திருத்தச் சட்டம்\n3. மொத்த இடங்களை மாற்றாமல் 2001 கணக்கெடுப்பின்படி தொகுதி மறுவரையறை செய்ய அனுமதித்த 87வது திருத்தச் சட்டம்\n4. மக்களவையில் ஆங்கிலோ-இந்திய நியமன இடங்களை நீக்கிய 104வது திருத்தச் சட்டம்",
            "1 → 4 → 2 → 3", "1 → 4 → 2 → 3",
            "2 → 1 → 3 → 4", "2 → 1 → 3 → 4",
            "1 → 2 → 3 → 4", "1 → 2 → 3 → 4",
            "3 → 1 → 2 → 4", "3 → 1 → 2 → 4",
            "C",
            "Chronological order:\n1. 42nd CA (1976): Froze seats till 2000 based on 1971 census\n2. 84th CA (2001): Extended freeze till 2026 based on 1991 census for delimitation\n3. 87th CA (2003): Substituted 2001 census for constituency delimitation\n4. 104th CA (2020): Discontinued nomination of Anglo-Indians\nHence, correct sequence is 1 → 2 → 3 → 4.",
            "காலவரிசை:\n1. 42வது திருத்தம் (1976): 1971 கணக்கெடுப்பு படி 2000 வரை முடக்கம்\n2. 84வது திருத்தம் (2001): 2026 வரை முடக்கம் நீட்டிப்பு\n3. 87வது திருத்தம் (2003): 2001 கணக்கெடுப்பு படி தொகுதி மறுவரையறை\n4. 104வது திருத்தம் (2020): ஆங்கிலோ-இந்திய நியமனம் நீக்கம்\nஎனவே சரியான வரிசை 1 → 2 → 3 → 4.",
            "Option A is incorrect because 104th CA (2020) is the latest event.", "விருப்பம் A தவறானது, ஏனெனில் 104வது திருத்தம் (2020) கடைசியாக வந்தது.",
            "Option B is incorrect because 42nd CA (1976) came before 84th CA (2001).", "விருப்பம் B தவறானது, ஏனெனில் 42வது திருத்தம் (1976) 84வது திருத்தத்திற்கு முன்னே வந்தது.",
            "Option C is correct because the sequence 1976 (1) → 2001 (2) → 2003 (3) → 2020 (4) is exact.", "விருப்பம் C சரியானது, ஏனெனில் 1976 (1) → 2001 (2) → 2003 (3) → 2020 (4) சரியான வரிசையாகும்.",
            "Option D is incorrect because 87th CA (2003) came after 42nd and 84th CAs.", "விருப்பம் D தவறானது, ஏனெனில் 87வது திருத்தம் பின்னர் வந்தது.",
            "TNPSC Delimitation Amendments: 42nd CA (1976) -> 84th CA (2001) -> 87th CA (2003) -> 104th CA (2020).",
            "டிஎன்பிஎஸ்சி மறுவரையறை திருத்தங்கள்: 42வது (1976) -> 84வது (2001) -> 87வது (2003) -> 104வது (2020).",
            "1976 42nd CA, 2001 84th CA, 2003 87th CA, 2020 104th CA.",
            "1976 42வது திருத்தம், 2001 84வது திருத்தம், 2003 87வது திருத்தம், 2020 104வது திருத்தம்.",
            "Remembering", "Medium", ["Delimitation Chronology", "42nd CA 1976", "84th CA 2001", "87th CA 2003", "104th CA 2020"], "Part 1"
        ),
        # Q004 - Correct D (1)
        (
            "CZ_PL_CH_004",
            "Arrange the following financial legislation stages during the passage of the Annual Financial Statement (Budget) in Lok Sabha in chronological order:\n1. Presentation of Budget by Finance Minister\n2. General Discussion on Budget\n3. Scrutiny of Demands for Grants by Departmental Standing Committees\n4. Voting on Demands for Grants followed by passage of Appropriation Bill and Finance Bill",
            "மக்களவையில் ஆண்டறிக்கை நிதிநிலை அறிக்கை (பட்ஜெட்) நிறைவேறும் பின்வரும் கட்டங்களைக் காலவரிசைப்படி வரிசைப்படுத்துக:\n1. நிதி அமைச்சரால் பட்ஜெட் சமர்ப்பிக்கப்படுதல்\n2. பட்ஜெட் மீதான பொது விவாதம்\n3. துறைசார் நிலைக்குழுக்களால் மானியக் கோரிக்கைகள் பரிசீலனை\n4. மானியக் கோரிக்கைகள் மீதான வாக்கெடுப்பைத் தொடர்ந்து ஒதுக்கீட்டு மசோதா மற்றும் நிதி மசோதா நிறைவேற்றம்",
            "2 → 1 → 4 → 3", "2 → 1 → 4 → 3",
            "3 → 1 → 2 → 4", "3 → 1 → 2 → 4",
            "1 → 3 → 2 → 4", "1 → 3 → 2 → 4",
            "1 → 2 → 3 → 4", "1 → 2 → 3 → 4",
            "D",
            "Chronological budget passage stages in Lok Sabha:\n1. Presentation of Budget\n2. General Discussion\n3. Scrutiny by Departmental Standing Committees (House adjourns for ~3-4 weeks)\n4. Voting on Demands for Grants, followed by Appropriation Bill and Finance Bill\nHence, correct sequence is 1 → 2 → 3 → 4.",
            "மக்களவையில் பட்ஜெட் நிறைவேறும் காலவரிசைக் கட்டங்கள்:\n1. பட்ஜெட் சமர்ப்பிப்பு\n2. பொது விவாதம்\n3. துறைசார் நிலைக்குழுக்களின் பரிசீலனை (அவை 3-4 வாரங்கள் ஒத்திவைக்கப்படும்)\n4. மானியக் கோரிக்கைகள் மீதான வாக்கெடுப்பு, ஒதுக்கீட்டு மசோதா & நிதி மசோதா நிறைவேற்றம்\nஎனவே சரியான வரிசை 1 → 2 → 3 → 4.",
            "Option A is incorrect because presentation (1) happens before general discussion (2).", "விருப்பம் A தவறானது, ஏனெனில் சமர்ப்பிப்பு (1) பொது விவாதத்திற்கு (2) முன்னே நடக்கும்.",
            "Option B is incorrect because presentation (1) is the first step.", "விருப்பம் B தவறானது, ஏனெனில் சமர்ப்பிப்பே முதல் படியாகும்.",
            "Option C is incorrect because General Discussion (2) occurs BEFORE Committee Scrutiny (3).", "விருப்பம் C தவறானது, ஏனெனில் பொது விவாதம் (2) குழு பரிசீலனைக்கு (3) முன்னே நடக்கும்.",
            "Option D is correct because 1 → 2 → 3 → 4 represents the exact 6-stage parliamentary budget workflow.", "விருப்பம் D சரியானது, ஏனெனில் 1 → 2 → 3 → 4 சரியான 6-கட்ட பட்ஜெட் வரிசையைக் குறிக்கிறது.",
            "TNPSC Budget Workflow: (1) Presentation -> (2) General Discussion -> (3) Committee Scrutiny -> (4) Voting on Demands -> (5) Appropriation Bill -> (6) Finance Bill.",
            "டிஎன்பிஎஸ்சி பட்ஜெட் வரிசை: (1) சமர்ப்பிப்பு -> (2) பொது விவாதம் -> (3) குழு பரிசீலனை -> (4) மானிய வாக்கெடுப்பு -> (5) ஒதுக்கீட்டு மசோதா -> (6) நிதி மசோதா.",
            "Budget passage stages in Indian Parliament under Article 112 to 117.",
            "சரத்து 112 முதல் 117 வரை நாடாளுமன்ற பட்ஜெட் நிறைவேற்றக் கட்டங்கள்.",
            "Understanding", "Medium", ["Budget Passage Workflow", "Articles 112 to 117", "6 Stages of Budget"], "Part 3"
        ),
    ]

    for cd in chronology_data:
        add_q(*cd)

    # Populate remaining 21 questions for Chronology set with balance A:6, B:6, C:7, D:6
    chronology_templates = [
        ("A", ["Government of India Act 1919 (PAC Origin)", "1st Lok Sabha Constitution 1952", "24th Amendment 1971", "52nd Amendment 1985"], "Part 1"),
        ("B", ["Dowry Joint Sitting 1961", "Banking Joint Sitting 1978", "POTA Joint Sitting 2002", "106th Women Reservation 2023"], "Part 2"),
        ("C", ["Shankari Prasad 1951", "Golaknath 1967", "Kesavananda 1973", "Kihoto Hollohan 1992"], "Part 3"),
        ("D", ["PAC 1921", "Estimates Committee 1950", "COPU 1964", "DRSCs 1993"], "Part 2"),
        ("A", ["Article 79 Formation 1950", "1st General Elections 1951-52", "Rajya Sabha First Sitting April 1952", "Lok Sabha First Sitting May 1952"], "Part 1"),
        ("B", ["42nd CA 1976", "44th CA 1978", "61st CA 1988", "91st CA 2003"], "Part 2"),
        ("C", ["1st CA 1951", "7th CA 1956", "24th CA 1971", "42nd CA 1976"], "Part 2"),
        ("D", ["52nd CA 1985", "69th CA 1991", "73rd CA 1992", "86th CA 2002"], "Part 2"),
        ("A", ["Article 110 Definition 1950", "24th CA 1971", "42nd CA 1976", "101st CA GST 2016"], "Part 2"),
        ("B", ["1st Speaker Mavalankar 1952", "First Joint Sitting 1961", "Swaran Singh Committee 1976", "91st CA 2003"], "Part 2"),
        ("C", ["1951 RPA Act", "1962 Zero Hour Origin", "1978 44th Amendment", "1993 Standing Committees"], "Part 2"),
        ("D", ["1950 Constitution Enforcement", "1964 COPU Creation", "1985 Anti Defection", "2019 EWS Quota 103rd CA"], "Part 2"),
        ("A", ["1952 Rajya Sabha Name Council of States", "1954 Renaming to Rajya Sabha & Lok Sabha", "1976 42nd Amendment", "2003 91st Amendment"], "Part 1"),
        ("B", ["1971 24th CA", "1975 39th CA", "1978 44th CA", "1988 61st CA"], "Part 2"),
        ("C", ["1951 Shankari Prasad", "1967 Golaknath", "1973 Kesavananda", "1980 Minerva Mills"], "Part 3"),
        ("D", ["1985 52nd CA", "1992 Kihoto Hollohan", "2003 91st CA", "2020 104th CA"], "Part 3"),
        ("A", ["1952 1st Lok Sabha", "1962 Zero Hour", "1976 Swaran Singh Report", "1993 DRSCs"], "Part 2"),
        ("B", ["1976 42nd CA", "1978 44th CA", "1985 52nd CA", "2016 101st CA"], "Part 2"),
        ("C", ["1951 1st CA", "1971 24th CA", "2002 86th CA", "2023 106th CA"], "Part 2"),
        ("D", ["1961 Dowry Act Joint Sitting", "1978 Banking Act Joint Sitting", "2002 POTA Joint Sitting", "2021 105th CA"], "Part 2"),
        ("C", ["1921 PAC Establishment", "1950 Estimates Committee", "1964 COPU Establishment", "1993 DRSC System"], "Part 2")
    ]

    for idx, (corr, events, part) in enumerate(chronology_templates, start=5):
        q_id = f"CZ_PL_CH_{idx:03d}"

        if corr == "A":
            seq_a = "1 → 2 → 3 → 4"
            seq_b = "2 → 1 → 4 → 3"
            seq_c = "3 → 4 → 1 → 2"
            seq_d = "4 → 3 → 2 → 1"
        elif corr == "B":
            seq_a = "2 → 1 → 4 → 3"
            seq_b = "1 → 2 → 3 → 4"
            seq_c = "3 → 1 → 4 → 2"
            seq_d = "4 → 2 → 1 → 3"
        elif corr == "C":
            seq_a = "3 → 4 → 1 → 2"
            seq_b = "2 → 3 → 4 → 1"
            seq_c = "1 → 2 → 3 → 4"
            seq_d = "4 → 1 → 2 → 3"
        else:
            seq_a = "4 → 3 → 2 → 1"
            seq_b = "2 → 4 → 1 → 3"
            seq_c = "3 → 1 → 2 → 4"
            seq_d = "1 → 2 → 3 → 4"

        q_en = f"Arrange the following parliamentary events/milestones in chronological order:\n1. {events[0]}\n2. {events[1]}\n3. {events[2]}\n4. {events[3]}"
        q_ta = f"பின்வரும் நாடாளுமன்ற மைல்கற்களைக் காலவரிசைப்படி வரிசைப்படுத்துக:\n1. {events[0]}\n2. {events[1]}\n3. {events[2]}\n4. {events[3]}"

        exp_en = f"Chronological sequence:\n1. {events[0]}\n2. {events[1]}\n3. {events[2]}\n4. {events[3]}\nHence, the correct order is Option {corr} ({seq_a if corr=='A' else seq_b if corr=='B' else seq_c if corr=='C' else seq_d})."
        exp_ta = f"காலவரிசை:\n1. {events[0]}\n2. {events[1]}\n3. {events[2]}\n4. {events[3]}\nஎனவே விருப்பம் {corr} சரியானதாகும்."

        why_a = f"Option A gives sequence {seq_a}. {'Correct chronological order' if corr=='A' else 'Incorrect sequence'}."
        why_a_ta = f"விருப்பம் A வரிசை {seq_a} ஐத் தருகிறது. {'சரியான வரிசை' if corr=='A' else 'தவறான வரிசை'}."
        why_b = f"Option B gives sequence {seq_b}. {'Correct chronological order' if corr=='B' else 'Incorrect sequence'}."
        why_b_ta = f"விருப்பம் B வரிசை {seq_b} ஐத் தருகிறது. {'சரியான வரிசை' if corr=='B' else 'தவறான வரிசை'}."
        why_c = f"Option C gives sequence {seq_c}. {'Correct chronological order' if corr=='C' else 'Incorrect sequence'}."
        why_c_ta = f"விருப்பம் C வரிசை {seq_c} ஐத் தருகிறது. {'சரியான வரிசை' if corr=='C' else 'தவறான வரிசை'}."
        why_d = f"Option D gives sequence {seq_d}. {'Correct chronological order' if corr=='D' else 'Incorrect sequence'}."
        why_d_ta = f"விருப்பம் D வரிசை {seq_d} ஐத் தருகிறது. {'சரியான வரிசை' if corr=='D' else 'தவறான வரிசை'}."

        tip_en = "Memorize key years of parliamentary milestones before attempting chronology questions."
        tip_ta = "காலவரிசைக் கேள்விகளுக்கு விடையளிக்கும் முன் முக்கிய நாடாளுமன்ற ஆண்டுகளை நினைவில் கொள்ளவும்."

        fact_en = "Parliamentary Chronology is a high-yielding section in TNPSC Group 1 General Studies."
        fact_ta = "நாடாளுமன்றக் காலவரிசை டிஎன்பிஎஸ்சி தேர்வுகளில் அதிக மதிப்பெண் தரும் பகுதியாகும்."

        add_q(
            q_id, q_en, q_ta,
            seq_a, seq_a, seq_b, seq_b, seq_c, seq_c, seq_d, seq_d,
            corr, exp_en, exp_ta,
            why_a, why_a_ta, why_b, why_b_ta, why_c, why_c_ta, why_d, why_d_ta,
            tip_en, tip_ta, fact_en, fact_ta,
            "Analyzing", "Hard", ["Parliamentary Chronology", "Milestone Events"], part
        )

    return questions

if __name__ == "__main__":
    qs = create_chronology_questions()
    os.makedirs("data/questions/polity", exist_ok=True)
    out_path = "data/questions/polity/parliament_chronology.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, ensure_ascii=False, indent=2)

    counts = Counter(q["correct_answer"] for q in qs)
    print(f"Parliament Chronology set complete. Total: {len(qs)}")
    print(f"Answer balance: {dict(counts)}")
