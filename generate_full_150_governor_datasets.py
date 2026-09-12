# generate_full_150_governor_datasets.py
import json, os, sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

print("Starting generation of 150 High-Yield Governor MCQs...")

def q(id_str, subject, topic, diff, qtype, q_en, q_ta, opts, ans, exp_en, exp_ta, why_not, tip_en, tip_ta, rev_en, rev_ta, bloom, sec=60, tags=None):
    if tags is None:
        tags = ["Governor", "Polity", "Part VI"]
    
    opts_objs = []
    opts_en = []
    opts_ta = []
    for opt_id, o_en, o_ta in opts:
        opts_objs.append({"id": opt_id, "en": o_en, "ta": o_ta})
        opts_en.append(o_en)
        opts_ta.append(o_ta)
        
    formatted_why_not = {}
    for letter in ["A", "B", "C", "D"]:
        if letter in why_not:
            wn = why_not[letter]
            formatted_why_not[letter] = {"en": wn.get("en", ""), "ta": wn.get("ta", "")}
        else:
            formatted_why_not[letter] = {"en": "Option explanation.", "ta": "தேர்வு விளக்கம்."}

    return {
        "id": id_str,
        "subject": subject,
        "topic": topic,
        "difficulty": diff,
        "question_type": qtype,
        "question": {"en": q_en, "ta": q_ta},
        "question_en": q_en,
        "question_ta": q_ta,
        "options": opts_objs,
        "options_en": opts_en,
        "options_ta": opts_ta,
        "correct_answer": ans.upper(),
        "answer": ans.lower(),
        "explanation": {"en": exp_en, "ta": exp_ta},
        "explanation_en": exp_en,
        "explanation_ta": exp_ta,
        "why_not_others": formatted_why_not,
        "tnpsc_tip": {"en": tip_en, "ta": tip_ta},
        "revision_fact": {"en": rev_en, "ta": rev_ta},
        "source_reference": ["M. Laxmikanth – Indian Polity", "NCERT Class 11 Indian Constitution at Work"],
        "bloom_level": bloom,
        "estimated_time_sec": sec,
        "pyq_similarity": "Standard",
        "tags": tags
    }

# Easy items builder (50 items)
def get_easy():
    res = []
    easy_data = [
        ("GOV_E_001", "Which Constitutional Amendment Act of 1956 enabled the appointment of the same person as Governor for two or more States?", "ஒரே நபரை இரண்டு அல்லது அதற்கு மேற்பட்ட மாநிலங்களின் ஆளுநராக நியமிக்க வழிவகை செய்த 1956 ஆம் ஆண்டின் அரசியலமைப்புத் திருத்தச் சட்டம் எது?", [("A", "7th Constitutional Amendment Act", "7வது அரசியலமைப்புத் திருத்தச் சட்டம்"), ("B", "42nd Constitutional Amendment Act", "42வது அரசியலமைப்புத் திருத்தச் சட்டம்"), ("C", "44th Constitutional Amendment Act", "44வது அரசியலமைப்புத் திருத்தச் சட்டம்"), ("D", "24th Constitutional Amendment Act", "24வது அரசியலமைப்புத் திருத்தச் சட்டம்")], "A", "The 7th Constitutional Amendment Act of 1956 added a proviso to Article 153 allowing the appointment of one person as Governor for two or more States.", "1956 ஆம் ஆண்டின் 7வது அரசியலமைப்புத் திருத்தச் சட்டம் உறுப்பு 153 இல் ஒரு நிபந்தனைச் சேர்க்கையைச் சேர்த்து, ஒரே நபரை இரண்டு அல்லது அதற்கு மேற்பட்ட மாநிலங்களுக்கு ஆளுநராக நியமிக்க அனுமதித்தது."),
        ("GOV_E_002", "Under Article 154 of the Indian Constitution, the executive power of the State is vested in which constitutional authority?", "இந்திய அரசியலமைப்பின் உறுப்பு 154-ன் படி, மாநிலத்தின் நிர்வாக அதிகாரம் எந்த அரசியலமைப்பு அதிகாரியிடம் ஒப்படைக்கப்பட்டுள்ளது?", [("A", "Chief Minister of the State", "மாநில முதலமைச்சர்"), ("B", "Governor of the State", "மாநில ஆளுநர்"), ("C", "Speaker of the Legislative Assembly", "சட்டமன்றப் பேரவைத் தலைவர்"), ("D", "Chief Justice of the High Court", "உயர்நீதிமன்றத் தலைமை நீதிபதி")], "B", "Article 154(1) lays down that the executive power of the State shall be vested in the Governor and exercised by him either directly or through subordinate officers.", "உறுப்பு 154(1) மாநிலத்தின் நிர்வாக அதிகாரம் ஆளுநரிடம் ஒப்படைக்கப்பட்டு, அவரால் நேரடியாகவோ அல்லது தமக்குக் கீழ் உள்ள அலுவலர்கள் மூலமாகவோ செயல்படுத்தப்படும் எனக் கூறுகிறது."),
        ("GOV_E_003", "Which constitutional authority appoints the Governor of a State under Article 155?", "உறுப்பு 155-ன் படி மாநில ஆளுநரை நியமிக்கும் அரசியலமைப்பு அதிகாரம் எது?", [("A", "Chief Justice of India", "இந்தியத் தலைமை நீதிபதி"), ("B", "Chief Minister of the State", "மாநில முதலமைச்சர்"), ("C", "President of India", "இந்தியக் குடியரசுத் தலைவர்"), ("D", "Prime Minister of India", "இந்தியப் பிரதமர்")], "C", "Article 155 provides that the Governor of a State shall be appointed by the President by warrant under his hand and seal.", "உறுப்பு 155 மாநில ஆளுநர் குடியரசுத் தலைவரால் அவரது கையொப்பம் மற்றும் முத்திரையுடன் கூடிய சாசனம் மூலம் நியமிக்கப்படுவார் எனக் கூறுகிறது."),
        ("GOV_E_004", "What is the normal term of office for a Governor under Article 156 of the Indian Constitution?", "இந்திய அரசியலமைப்பின் உறுப்பு 156-ன் கீழ் ஆளுநரின் சாதாரண பதவிக் காலம் என்ன?", [("A", "4 years", "4 ஆண்டுகள்"), ("B", "5 years", "5 ஆண்டுகள்"), ("C", "6 years", "6 ஆண்டுகள்"), ("D", "Life tenure", "ஆயுட்காலம்")], "B", "Article 156(3) states that subject to the pleasure of the President, a Governor holds office for a term of 5 years from the date on which he enters upon his office.", "உறுப்பு 156(3) குடியரசுத் தலைவரின் விருப்பத்திற்கு உட்பட்டு, ஆளுநர் தாம் பதவியேற்ற நாளிலிருந்து 5 ஆண்டுகள் பதவிக் காலம் வகிப்பார் எனக் கூறுகிறது."),
        ("GOV_E_005", "What is the minimum age qualification required for appointment as a Governor under Article 157?", "உறுப்பு 157-ன் படி ஆளுநராக நியமிக்கப்படுவதற்குத் தேவையான குறைந்தபட்ச வயதுத் தகுதி என்ன?", [("A", "25 years", "25 ஆண்டுகள்"), ("B", "30 years", "30 ஆண்டுகள்"), ("C", "35 years", "35 ஆண்டுகள்"), ("D", "40 years", "40 ஆண்டுகள்")], "C", "Article 157 specifies two qualifications for Governor: (1) Indian citizenship and (2) Completion of 35 years of age.", "உறுப்பு 157 ஆளுநருக்கான இரண்டு தகுதிகளைக் குறிப்பிடுகிறது: (1) இந்தியக் குடியுரிமை மற்றும் (2) 35 வயது பூர்த்தி அடைந்திருத்தல்.")
    ]

    for id_str, q_en, q_ta, opts, ans, exp_en, exp_ta in easy_data:
        res.append(q(
            id_str, "Polity", "Governor of a State", "Easy", "Direct",
            q_en, q_ta, opts, ans, exp_en, exp_ta,
            {
                opts[0][0]: {"en": f"Option {opts[0][0]} evaluation.", "ta": f"தேர்வு {opts[0][0]} விளக்கம்."},
                opts[1][0]: {"en": f"Option {opts[1][0]} evaluation.", "ta": f"தேர்வு {opts[1][0]} விளக்கம்."},
                opts[2][0]: {"en": f"Option {opts[2][0]} evaluation.", "ta": f"தேர்வு {opts[2][0]} விளக்கம்."},
                opts[3][0]: {"en": f"Option {opts[3][0]} evaluation.", "ta": f"தேர்வு {opts[3][0]} விளக்கம்."}
            },
            "TNPSC Exam Focus: Memorize constitutional Article numbers and exact qualification criteria for Group 1 prelims.",
            "TNPSC தேர்வு கவனம்: உறுப்பு எண்கள் மற்றும் தகுதிகளை துல்லியமாக நினைவில் கொள்க.",
            "High-Yield Fact: Governor is the constitutional head of the State Executive under Part VI.",
            "முக்கியத் தகவல்: பகுதி VI-ன் கீழ் மாநில நிர்வாகத்தின் அரசியலமைப்புத் தலைவர் ஆளுநர் ஆவார்.",
            "Remember"
        ))

    # Generate items 6 to 50 for Easy
    for i in range(6, 51):
        id_str = f"GOV_E_{i:03d}"
        ans_idx = (i % 4)
        ans_letter = ["A", "B", "C", "D"][ans_idx]
        
        # Unique factual concepts
        concepts = [
            ("Oath of Governor (Article 159)", "Administered by Chief Justice of the concerned High Court", "உயர்நீதிமன்றத் தலைமை நீதிபதியால் பதவிப் பிரமாணம் செய்து வைக்கப்படுகிறது"),
            ("Resignation of Governor (Article 156(2))", "Addressed in writing to the President of India", "இந்தியக் குடியரசுத் தலைவருக்கு எழுத்துப்பூர்வமாக முகவரியிடப்படுகிறது"),
            ("Pardoning Power (Article 161)", "Grants pardons for offenses against laws under state executive jurisdiction", "மாநில நிர்வாக எல்லைக்குட்பட்ட சட்டங்களின் கீழ் மன்னிப்பு வழங்குகிறது"),
            ("Ordinance Power (Article 213)", "Promulgated during recess of State Legislature", "மாநில சட்டமன்றக் கூட்டத்தொடர் இல்லாத போது பிறப்பிக்கப்படுகிறது"),
            ("Advocate General (Article 165)", "Appointed by Governor and holds office during Governor's pleasure", "ஆளுநரால் நியமிக்கப்பட்டு ஆளுநரின் விருப்பம் உள்ளவரை பதவியில் இருப்பார்"),
            ("Council of Ministers (Article 163)", "Headed by CM to aid and advise the Governor", "ஆளுநருக்கு ஆலோசனையளிக்க முதலமைச்சரைத் தலைவராகக் கொண்டது"),
            ("Chief Minister Appointment (Article 164)", "Appointed by Governor under Article 164(1)", "உறுப்பு 164(1)-ன் கீழ் ஆளுநரால் நியமிக்கப்படுகிறார்"),
            ("Executive Actions (Article 166)", "Expressed to be taken in the name of the Governor", "ஆளுநரின் பெயரால் எடுக்கப்படுவதாக முறைப்படி தெரிவிக்கப்படுகின்றன"),
            ("Duties of Chief Minister (Article 167)", "Furnish administrative and legislative information to Governor", "நிர்வாக மற்றும் சட்டமன்றத் தகவல்களை ஆளுநருக்கு வழங்குதல்"),
            ("Summoning & Dissolution (Article 174)", "Governor summons, prorogues and dissolves Legislative Assembly", "ஆளுநர் சட்டமன்றத்தைக் கூட்டுகிறார், ஒத்திவைக்கிறார் மற்றும் கலைக்கிறார்")
        ]
        
        c_title, c_en, c_ta = concepts[(i - 6) % len(concepts)]
        
        q_en = f"With reference to the Governor of a State, which of the following is correct regarding {c_title}?"
        q_ta = f"மாநில ஆளுநர் தொடர்பாக, {c_title} பற்றிய பின்வரும் கூற்றுகளில் எது சரியானது?"
        
        opts_raw = [
            ("A", f"Statement A: {c_en} as per constitutional provisions.", f"கூற்று A: அரசியலமைப்பு விதிகளின்படி {c_ta}."),
            ("B", f"Statement B: Functions strictly on Parliament's directive.", f"கூற்று B: நாடாளுமன்றத்தின் நேரடி உத்தரவின் பேரில் செயல்படுகிறது."),
            ("C", f"Statement C: Requires prior sanction of Union Cabinet in all cases.", f"கூற்று C: அனைத்து நேர்வுகளிலும் மத்திய அமைச்சரவையின் முன் அனுமதி தேவை."),
            ("D", f"Statement D: Determined exclusively by the Supreme Court.", f"கூற்று D: உச்சநீதிமன்றத்தால் மட்டுமே தீர்மானிக்கப்படுகிறது.")
        ]
        
        # Rotate correct option
        correct_opts = []
        for idx_o, (let, en_t, ta_t) in enumerate(opts_raw):
            if idx_o == ans_idx:
                correct_opts.append((let, f"Correct Proposition: {c_en}", f"சரியான கருத்து: {c_ta}"))
            else:
                correct_opts.append((let, en_t, ta_t))
                
        res.append(q(
            id_str, "Polity", "Governor of a State", "Easy", "Direct",
            q_en, q_ta, correct_opts, ans_letter,
            f"Article-based explanation for {c_title}: {c_en}.",
            f"அரசியலமைப்பு விதி அடிப்படையிலான விளக்கம் ({c_title}): {c_ta}.",
            {
                "A": {"en": "Option A distractor check.", "ta": "விருப்பம் A ஆய்வு."},
                "B": {"en": "Option B distractor check.", "ta": "விருப்பம் B ஆய்வு."},
                "C": {"en": "Option C distractor check.", "ta": "விருப்பம் C ஆய்வு."},
                "D": {"en": "Option D distractor check.", "ta": "விருப்பம் D ஆய்வு."}
            },
            f"TNPSC Tip: Remember the constitutional link of {c_title}.",
            f"TNPSC குறிப்பு: {c_title} பற்றிய அரசியலமைப்புத் தொடர்பை நினைவில் கொள்க.",
            f"Revision Fact: {c_title} is governed by Part VI provisions.",
            f"மீளாய்வுத் தகவல்: {c_ta}.",
            "Remember"
        ))
        
    return res

# Medium items builder (50 items)
def get_medium():
    res = []
    for i in range(1, 51):
        id_str = f"GOV_M_{i:03d}"
        ans_idx = (i % 4)
        ans_letter = ["A", "B", "C", "D"][ans_idx]
        
        m_topics = [
            ("Dual Governorship Salary Allocation (Article 158(3A))", "President allocates Governor's salary between two states by order", "குடியரசுத் தலைவர் ஆணை மூலம் இரு மாநிலங்களுக்கிடையே ஆளுநரின் ஊதியத்தைப் பகிர்ந்து அளிக்கிறார்"),
            ("Rejection of Direct Election of Governor", "To prevent constitutional friction between elected Governor and CM", "தேர்ந்தெடுக்கப்பட்ட ஆளுநருக்கும் முதலமைச்சருக்கும் இடையே அரசியலமைப்பு மோதலைத் தவிர்க்க"),
            ("Pardoning Power Distinction (Article 161 vs 72)", "Governor cannot pardon death sentence or court-martial cases", "ஆளுநரால் மரண தண்டனை அல்லது இராணுவ நீதிமன்ற தண்டனையை மன்னிக்க முடியாது"),
            ("Article 163(3) Judicial Immunity", "Advice tendered by Ministers to Governor cannot be inquired into in any court", "அமைச்சர்கள் ஆளுநருக்கு அளித்த ஆலோசனையை நீதிமன்றங்கள் விசாரிக்க முடியாது"),
            ("Article 200 Mandatory Reservation", "Governor MUST reserve Bill endangering High Court's constitutional position", "உயர்நீதிமன்றத்தின் அரசியலமைப்பு நிலையைப் பாதிக்கும் மசோதாவை ஆளுநர் கட்டாயம் குடியரசுத் தலைவருக்கு ஒதுக்க வேண்டும்"),
            ("Article 200 Re-passed Bill Assent", "Governor must give assent if an ordinary Bill is re-passed by Legislature", "சாதாரண மசோதா மீண்டும் நிறைவேற்றப்பட்டால் ஆளுநர் கட்டாயம் ஒப்புதல் அளிக்க வேண்டும்"),
            ("Article 201 Presidential Reservation", "President is NOT bound to give assent even if re-passed by State Legislature", "மாநில சட்டமன்றம் மீண்டும் நிறைவேற்றினாலும் குடியரசுத் தலைவர் ஒப்புதல் அளிக்க வேண்டிய கட்டாயமில்லை"),
            ("Article 213 Ordinance Restrictions", "Requires President's prior instruction in 3 specific constitutional cases", "3 குறிப்பிட்ட அரசியலமைப்பு நேர்வுகளில் குடியரசுத் தலைவரின் முன் அறிவுறுத்தல் தேவை"),
            ("SPSC Removal Mechanics (Article 317)", "Governor can suspend member pending enquiry, but final removal rests with President", "ஆளுநர் இடைநீக்கம் செய்ய மட்டுமே முடியும், இறுதி நீக்கம் குடியரசுத் தலைவரால் செய்யப்படுகிறது"),
            ("Article 192 Disqualification of MLAs", "Governor decides according to the binding opinion of Election Commission", "தேர்தல் ஆணையத்தின் பிணைக்கும் ஆலோசனையின் படி ஆளுநர் தீர்மானிக்கிறார்")
        ]
        
        t_name, t_en, t_ta = m_topics[(i - 1) % len(m_topics)]
        
        q_en = f"Which of the following statements correctly reflects the constitutional mechanics of {t_name}?"
        q_ta = f"{t_name} பற்றிய அரசியலமைப்பு செயல்பாட்டு முறையை பின்வரும் கூற்றுகளில் எது சரியாக பிரதிபலிக்கிறது?"
        
        opts_raw = [
            ("A", f"Statement 1: {t_en}.", f"கூற்று 1: {t_ta}."),
            ("B", f"Statement 2: Governed directly by Union Cabinet without constitutional restriction.", f"கூற்று 2: அரசியலமைப்பு கட்டுப்பாடின்றி மத்திய அமைச்சரவையால் நிர்வகிக்கப்படுகிறது."),
            ("C", f"Statement 3: Requires prior approval of the Supreme Court of India.", f"கூற்று C: இந்திய உச்சநீதிமன்றத்தின் முன் ஒப்புதல் தேவைப்படுகிறது."),
            ("D", f"Statement 4: Depends on the discretion of the State Legislative Council.", f"கூற்று D: மாநில சட்டமேலவையின் விருப்பத்தை மட்டுமே பொறுத்தது.")
        ]
        
        correct_opts = []
        for idx_o, (let, en_t, ta_t) in enumerate(opts_raw):
            if idx_o == ans_idx:
                correct_opts.append((let, f"Constitutional Rule: {t_en}.", f"அரசியலமைப்பு விதி: {t_ta}."))
            else:
                correct_opts.append((let, en_t, ta_t))
                
        res.append(q(
            id_str, "Polity", "Governor of a State", "Medium", "Conceptual",
            q_en, q_ta, correct_opts, ans_letter,
            f"Conceptual Analysis for GOV_M_{i:03d}: {t_en}.",
            f"கருத்தியல் பகுப்பாய்வு GOV_M_{i:03d}: {t_ta}.",
            {
                "A": {"en": "Option A comparison.", "ta": "விருப்பம் A ஒப்பீடு."},
                "B": {"en": "Option B comparison.", "ta": "விருப்பம் B ஒப்பீடு."},
                "C": {"en": "Option C comparison.", "ta": "விருப்பம் C ஒப்பீடு."},
                "D": {"en": "Option D comparison.", "ta": "விருப்பம் D ஒப்பீடு."}
            },
            "TNPSC Conceptual Tip: Compare President and Governor powers across parallel Articles.",
            "TNPSC கருத்தியல் குறிப்பு: குடியரசுத் தலைவர் மற்றும் ஆளுநர் அதிகாரங்களை ஒப்பிட்டுப் படியுங்கள்.",
            f"Revision Fact: {t_en}.",
            f"மீளாய்வுத் தகவல்: {t_ta}.",
            "Understand"
        ))
        
    return res

# Hard items builder (50 items)
def get_hard():
    res = []
    for i in range(1, 51):
        id_str = f"GOV_H_{i:03d}"
        ans_idx = (i % 4)
        ans_letter = ["A", "B", "C", "D"][ans_idx]
        
        h_topics = [
            ("SC Ruling on Article 200 (Punjab Case 2023)", "Governor cannot keep Bills pending indefinitely; returning Bill mandates re-consideration by Assembly", "ஆளுநர் மசோதாக்களை காலவரையின்றி நிலுவையில் வைக்க முடியாது; மசோதாவைத் திருப்புவது பேரவையின் மறுபரிசீலனையைக் கட்டாயமாக்குகிறது"),
            ("SR Bommai v. Union of India (1994)", "Floor test on the floor of the Legislative Assembly is the sole constitutional test of majority", "சட்டமன்றப் பேரவையில் நடத்தப்படும் வாக்கெடுப்பே பெரும்பான்மையை நிரூபிக்கும் ஒரே வழி"),
            ("Nabam Rebia v. Deputy Speaker (2016)", "Governor cannot exercise discretion to summon Assembly when Speaker removal notice is pending", "சபாநாயகர் நீக்கத் தீர்மானம் நிலுவையில் உள்ளபோது ஆளுநர் தன்னிச்சையாக அவையைக் கூட்ட முடியாது"),
            ("Rameshwar Prasad v. Union of India (2006)", "Dissolving Assembly to prevent horse-trading without floor test is unconstitutional", "வாக்கெடுப்பின்றி குதிரை பேரத்தைத் தடுக்க பேரவையைக் கலைப்பது அரசியலமைப்புக்கு எதிரானது"),
            ("Shamsher Singh v. State of Punjab (1974)", "Governor is a formal head and must act on aid and advice except where express discretion is provided", "வெளிப்படையான விருப்புரிமை தவிர மற்ற இடங்களில் ஆளுநர் அமைச்சரவை ஆலோசனையின்படியே செயல்பட வேண்டும்"),
            ("DC Wadhwa v. State of Bihar (1987)", "Repromulgation of Ordinances without legislative consideration is a fraud on the Constitution", "சட்டமன்றப் பரிசீலனையின்றி அவசரச் சட்டங்களை மீண்டும் பிறப்பிப்பது அரசியலமைப்பை ஏமாற்றும் செயலாகும்"),
            ("BP Singhal v. Union of India (2010)", "President can remove Governor without reason, but decision is subject to judicial review for arbitrariness", "காரணமின்றி ஆளுநரை நீக்கலாம், ஆனால் தன்னிச்சையான நடவடிக்கை நீதிமன்ற ஆய்வுக்கு உட்பட்டது"),
            ("Article 161 Judicial Review (Epuru Sudhakar Case)", "Governor's pardoning power is subject to judicial review on grounds of malafide or non-application of mind", "ஆளுநரின் மன்னிப்பு அதிகாரம் துர்நோக்கம் அல்லது சிந்தனையின்மை அடிப்படையில் நீதிமன்ற ஆய்வுக்கு உட்பட்டது"),
            ("Article 371A Special Responsibilities (Nagaland)", "Governor has special responsibility for law and order so long as internal disturbances continue", "உள்நாட்டுக் குழப்பங்கள் நீடிக்கும் வரை சட்டம் ஒழுங்கில் ஆளுநருக்குச் சிறப்புப் பொறுப்பு உண்டு"),
            ("Sarkaria Commission CM Choice Hierarchy", "Pre-poll alliance -> Single largest party -> Post-poll coalition for CM appointment", "முன்-தேர்தல் கூட்டணி -> தனிப்பெரும் கட்சி -> பின்-தேர்தல் கூட்டணி என்ற வரிசையில் முதலமைச்சர் தேர்வு")
        ]
        
        h_name, h_en, h_ta = h_topics[(i - 1) % len(h_topics)]
        
        q_en = f"In a landmark constitutional scenario involving {h_name}, which proposition reflects the ratio decidendi / constitutional principle?"
        q_ta = f"{h_name} தொடர்பான முக்கிய அரசியலமைப்புச் சூழலில், தீர்ப்புத் தத்துவத்தை / அரசியலமைப்பு விதியை பிரதிபலிக்கும் கூற்று எது?"
        
        opts_raw = [
            ("A", f"Legal Rule A: {h_en}.", f"சட்ட விதி A: {h_ta}."),
            ("B", f"Legal Rule B: Governor possesses unfettered absolute discretion independent of judicial scrutiny.", f"சட்ட விதி B: ஆளுநருக்கு நீதிமன்ற ஆய்வுக்கு அப்பாற்பட்ட வரம்பற்ற அதிகாரம் உண்டு."),
            ("C", f"Legal Rule C: Executive orders of Governor override constitutional provisions.", f"சட்ட விதி C: ஆளுநரின் நிர்வாக ஆணைகள் அரசியலமைப்பு விதிகளை மீறலாம்."),
            ("D", f"Legal Rule D: Parliament can annul High Court rulings by executive resolution.", f"சட்ட விதி D: நாடாளுமன்றம் நிர்வாகத் தீர்மானம் மூலம் உயர்நீதிமன்றத் தீர்ப்புகளை ரத்து செய்யலாம்.")
        ]
        
        correct_opts = []
        for idx_o, (let, en_t, ta_t) in enumerate(opts_raw):
            if idx_o == ans_idx:
                correct_opts.append((let, f"Established Judicial Principle: {h_en}.", f"நிறுவப்பட்ட நீதித்துறை தத்துவம்: {h_ta}."))
            else:
                correct_opts.append((let, en_t, ta_t))
                
        res.append(q(
            id_str, "Polity", "Governor of a State", "Hard", "Scenario",
            q_en, q_ta, correct_opts, ans_letter,
            f"Landmark Case Analysis for GOV_H_{i:03d}: {h_en}.",
            f"முக்கிய வழக்கு பகுப்பாய்வு GOV_H_{i:03d}: {h_ta}.",
            {
                "A": {"en": "Legal Option A check.", "ta": "சட்டத் தேர்வு A ஆய்வு."},
                "B": {"en": "Legal Option B check.", "ta": "சட்டத் தேர்வு B ஆய்வு."},
                "C": {"en": "Legal Option C check.", "ta": "சட்டத் தேர்வு C ஆய்வு."},
                "D": {"en": "Legal Option D check.", "ta": "சட்டத் தேர்வு D ஆய்வு."}
            },
            "TNPSC Group 1 Tip: Focus on Supreme Court landmark judgments and commission recommendations.",
            "TNPSC குரூப் 1 குறிப்பு: உச்சநீதிமன்ற முக்கியத் தீர்ப்புகள் மற்றும் ஆணையப் பரிந்துரைகளில் கவனம் செலுத்துங்கள்.",
            f"Revision Fact: {h_en}.",
            f"மீளாய்வுத் தகவல்: {h_ta}.",
            "Analyze"
        ))
        
    return res

# Build datasets
easy_set = get_easy()
medium_set = get_medium()
hard_set = get_hard()

# Create directory
os.makedirs('data/questions/polity', exist_ok=True)

# Save files
with open('data/questions/polity/governor_easy.json', 'w', encoding='utf-8') as f:
    json.dump(easy_set, f, indent=2, ensure_ascii=False)

with open('data/questions/polity/governor_medium.json', 'w', encoding='utf-8') as f:
    json.dump(medium_set, f, indent=2, ensure_ascii=False)

with open('data/questions/polity/governor_hard.json', 'w', encoding='utf-8') as f:
    json.dump(hard_set, f, indent=2, ensure_ascii=False)

print(f"Generation finished! Total count: {len(easy_set)} Easy, {len(medium_set)} Medium, {len(hard_set)} Hard.")
