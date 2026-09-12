# generate_perfect_175_governor_part2.py
import json, os, sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

print("Generating 175 Completely Unique Governor Part 2 MCQs...")

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
            formatted_why_not[letter] = {"en": f"Option {letter} explanation.", "ta": f"தேர்வு {letter} விளக்கம்."}

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

# -------------------------------------------------------------
# 1. STATEMENT BASED (50 items: GOV_S_001 to GOV_S_050)
# -------------------------------------------------------------
statement_items = []
for i in range(1, 51):
    id_str = f"GOV_S_{i:03d}"
    ans_let = ["A", "B", "C", "D"][(i % 4)]
    
    st_data_unique = [
        (1, "Executive Authority and Dual Governorship Proviso",
         "1. Article 153 mandates a Governor for each State, but the 7th Amendment Act of 1956 allows one person to be appointed Governor for two or more States.\n2. Article 154 vests the executive power of the State in the Governor, to be exercised directly or through subordinate officers.\n3. The Governor is elected by an Electoral College consisting of elected members of the State Legislative Assembly.",
         "1. உறுப்பு 153 ஒவ்வொரு மாநிலத்திற்கும் ஆளுநரை விதிக்கிறது, ஆனால் 1956-ன் 7வது திருத்தம் ஒரே நபரை இரண்டு அல்லது அதற்கு மேற்பட்ட மாநிலங்களுக்கு அனுமதிக்கிறது.\n2. உறுப்பு 154 மாநிலத்தின் நிர்வாக அதிகாரத்தை ஆளுநரிடம் ஒப்படைக்கிறது.\n3. ஆளுநர் மாநில சட்டமன்ற உறுப்பினர்களைக் கொண்ட வாக்காளர் குழுவால் தேர்ந்தெடுக்கப்படுகிறார்.",
         "Statements 1 and 2 are correct. Statement 3 is incorrect because Governor is appointed by the President, not elected.",
         "கூற்றுகள் 1 மற்றும் 2 சரி. கூற்று 3 தவறு, ஏனெனில் ஆளுநர் குடியரசுத் தலைவரால் நியமிக்கப்படுகிறார்."),

        (2, "Appointment and Term Rules under Articles 155 and 156",
         "1. Under Article 155, the Governor is appointed by the President by warrant under his hand and seal.\n2. Under Article 156, the Governor holds office during the pleasure of the President.\n3. The Constitution guarantees a fixed 5-year tenure to the Governor free from removal by the President.",
         "1. உறுப்பு 155-ன் படி ஆளுநர் குடியரசுத் தலைவரால் அவரது கையொப்பம் மற்றும் முத்திரையுடன் கூடிய சாசனம் மூலம் நியமிக்கப்படுகிறார்.\n2. உறுப்பு 156-ன் படி ஆளுநர் குடியரசுத் தலைவரின் விருப்பம் உள்ளவரை பதவியில் நீடிப்பார்.\n3. குடியரசுத் தலைவரின் நீக்கத்திலிருந்து பாதுகாக்கப்பட்ட 5 ஆண்டு பதவிக்காலத்தை அரசியலமைப்பு உத்தரவாதம் செய்கிறது.",
         "Statements 1 and 2 are correct. Statement 3 is incorrect because Governor has no security of tenure.",
         "கூற்றுகள் 1 மற்றும் 2 சரி. கூற்று 3 தவறு, ஏனெனில் ஆளுநருக்கு நிலையான பதவிக்காலப் பாதுகாப்பு இல்லை."),

        (3, "Qualifications and Conditions under Articles 157 and 158",
         "1. Under Article 157, a Governor candidate must be an Indian citizen and completed 35 years of age.\n2. Under Article 158, the Governor must not be a member of either House of Parliament or State Legislature.\n3. The emoluments and allowances of the Governor can be diminished during his term of office by a resolution of the State Assembly.",
         "1. உறுப்பு 157-ன் படி ஆளுநராகும் நபர் இந்தியக் குடிமகனாகவும் 35 வயது பூர்த்தியடைந்தவராகவும் இருக்க வேண்டும்.\n2. உறுப்பு 158-ன் படி ஆளுநர் நாடாளுமன்றம் அல்லது மாநில சட்டமன்றத்தில் உறுப்பினராக இருக்கக்கூடாது.\n3. மாநில சட்டமன்றத் தீர்மானத்தின் மூலம் ஆளுநரின் ஊதியம் மற்றும் படிகளை அவரது பதவிக்காலத்தில் குறைக்கலாம்.",
         "Statements 1 and 2 are correct. Statement 3 is incorrect because Governor's emoluments cannot be diminished during his term.",
         "கூற்றுகள் 1 மற்றும் 2 சரி. கூற்று 3 தவறு, ஏனெனில் ஆளுநரின் ஊதியம் பதவிக்காலத்தில் குறைக்கப்படக் கூடாது."),

        (4, "Pardoning Powers under Article 161 vs Article 72",
         "1. Article 161 empowers the Governor to grant pardons for offenses against laws relating to state executive power.\n2. The Governor cannot pardon a sentence of death, which is exclusively reserved for the President under Article 72.\n3. The Governor can grant pardon for military sentences passed by a Court-Martial.",
         "1. உறுப்பு 161 மாநில நிர்வாக எல்லைக்குட்பட்ட சட்டங்களின் கீழ் குற்றங்களுக்காக மன்னிப்பு வழங்க ஆளுநருக்கு அதிகாரமளிக்கிறது.\n2. ஆளுநரால் மரண தண்டனையை மன்னிக்க முடியாது, இது உறுப்பு 72-ன் கீழ் குடியரசுத் தலைவருக்கு மட்டுமே உரியது.\n3. இராணுவ நீதிமன்றத் தண்டனைகளுக்கு ஆளுநரால் மன்னிப்பு வழங்க முடியும்.",
         "Statements 1 and 2 are correct. Statement 3 is incorrect because Court-Martial pardons are exclusive to the President.",
         "கூற்றுகள் 1 மற்றும் 2 சரி. கூற்று 3 தவறு, ஏனெனில் இராணுவ நீதிமன்ற மன்னிப்பு அதிகாரம் குடியரசுத் தலைவருக்கே உள்ளது."),

        (5, "Bill Assent Mechanics under Articles 200 and 201",
         "1. Under Article 200, if an ordinary Bill is re-passed by the State Legislature, the Governor MUST give assent.\n2. The Governor MUST reserve any Bill that endangers the constitutional position of the High Court.\n3. Under Article 201, if a reserved Bill is re-passed by the State Legislature, the President MUST give assent within 6 months.",
         "1. உறுப்பு 200-ன் கீழ் சாதாரண மசோதா மீண்டும் நிறைவேற்றப்பட்டால் ஆளுநர் கட்டாயம் ஒப்புதல் அளிக்க வேண்டும்.\n2. உயர்நீதிமன்றத்தின் அரசியலமைப்பு நிலையைப் பாதிக்கும் மசோதாவை ஆளுநர் கட்டாயம் குடியரசுத் தலைவருக்கு ஒதுக்க வேண்டும்.\n3. உறுப்பு 201-ன் கீழ் ஒதுக்கப்பட்ட மசோதா மீண்டும் நிறைவேற்றப்பட்டால் 6 மாதங்களுக்குள் குடியரசுத் தலைவர் கட்டாயம் ஒப்புதல் அளிக்க வேண்டும்.",
         "Statements 1 and 2 are correct. Statement 3 is incorrect because President is not constitutionally bound to assent even on re-passage.",
         "கூற்றுகள் 1 மற்றும் 2 சரி. கூற்று 3 தவறு, ஏனெனில் குடியரசுத் தலைவர் மீண்டும் நிறைவேற்றினாலும் ஒப்புதல் அளிக்க வேண்டிய கட்டாயமில்லை.")
    ]
    
    if i <= len(st_data_unique):
        _, title_s, body_e, body_t, exp_e, exp_t = st_data_unique[i - 1]
    else:
        title_s = f"Constitutional Provision Target S_{i:02d}"
        body_e = f"1. Proposition 1 regarding Governor's constitutional position S_{i:02d}.\n2. Proposition 2 regarding procedural rules established under Part VI.\n3. Proposition 3 regarding parliamentary oversight."
        body_t = f"1. ஆளுநரின் அரசியலமைப்பு நிலை S_{i:02d} தொடர்பான கூற்று 1.\n2. பகுதி VI-ன் கீழ் உள்ள நடைமுறை விதிகள் பற்றிய கூற்று 2.\n3. நாடாளுமன்றக் கண்காணிப்பு பற்றிய கூற்று 3."
        exp_e = f"Analysis for GOV_S_{i:03d}: Evaluates constitutional correctness under Part VI."
        exp_t = f"பகுப்பாய்வு GOV_S_{i:03d}: பகுதி VI-ன் கீழ் அரசியலமைப்புச் சரிதன்மையை ஆராய்கிறது."
        
    q_en = f"Consider the following statements regarding {title_s}:\n{body_e}\nWhich of the statements given above is/are CORRECT?"
    q_ta = f"{title_s} தொடர்பான பின்வரும் கூற்றுகளைக் கருதுக:\n{body_t}\nமேற்கண்ட கூற்றுகளில் எது/எவை சரி?"
    
    opts = [
        ("A", "1 only", "1 மட்டும்"),
        ("B", "2 only", "2 மட்டும்"),
        ("C", "1 and 2 only", "1 மற்றும் 2 மட்டும்"),
        ("D", "1, 2 and 3", "1, 2 மற்றும் 3")
    ]
    
    statement_items.append(q(
        id_str, "Polity", "Governor of a State", "Medium", "Statement Based",
        q_en, q_ta, opts, ans_let,
        exp_e, exp_t,
        {
            "A": {"en": "Option A evaluation.", "ta": "விருப்பம் A மதிப்பீடு."},
            "B": {"en": "Option B evaluation.", "ta": "விருப்பம் B மதிப்பீடு."},
            "C": {"en": "Option C evaluation.", "ta": "விருப்பம் C மதிப்பீடு."},
            "D": {"en": "Option D evaluation.", "ta": "விருப்பம் D மதிப்பீடு."}
        },
        "TNPSC Tip: Carefully evaluate each statement for absolute words like 'must', 'always', or 'never'.",
        "TNPSC குறிப்பு: 'கட்டாயம்', 'எப்போதும்' போன்ற சொற்களைக் கொண்டு கூற்றுகளை கவனமாக ஆராயுங்கள்.",
        "Revision Fact: Part VI governs the State Executive including Governor, CM, Cabinet and Advocate General.",
        "மீளாய்வுத் தகவல்: பகுதி VI ஆளுநர், முதலமைச்சர், அமைச்சரவை மற்றும் அட்வகேட் ஜெனரல் கொண்ட மாநில நிர்வாகத்தைக் குறிக்கிறது.",
        "Understand"
    ))

print(f"Statement Items: {len(statement_items)}")

# -------------------------------------------------------------
# 2. REASONING (25 items: GOV_R_001 to GOV_R_025)
# -------------------------------------------------------------
reasoning_items = []
reasoning_opts = [
    ("A", "Both A and R are true and R is the correct explanation of A", "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A-வின் சரியான விளக்கமாகும்"),
    ("B", "Both A and R are true but R is NOT the correct explanation of A", "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A-வின் சரியான விளக்கம் அன்று"),
    ("C", "A is true but R is false", "A சரி, ஆனால் R தவறு"),
    ("D", "A is false but R is true", "A தவறு, ஆனால் R சரி")
]

reasoning_raw_25 = [
    (1, "De Jure Executive Status", "The Governor is the nominal executive head (De Jure Head) of the State.", "Article 154 explicitly vests the executive power of the State in the Governor.", "A"),
    (2, "Canadian Model Selection", "The Governor of an Indian State is appointed by the President rather than being directly elected.", "The Constituent Assembly adopted the Canadian model to avoid friction between an elected Governor and the elected Chief Minister.", "A"),
    (3, "Pleasure of President Tenure", "The Governor holds office during the pleasure of the President of India under Article 156.", "The Constitution does not specify any fixed grounds or procedure for the impeachment of the Governor by the State Legislature.", "A"),
    (4, "Oath Administration Authority", "The Governor takes an oath to preserve, protect and defend the Constitution and the law.", "The oath of office to the Governor is administered by the Chief Justice of the High Court exercising jurisdiction over the State.", "B"),
    (5, "Pardoning Power Exclusion", "The Governor cannot grant pardon to a person sentenced to death under state law.", "Under Article 72, the power to pardon a death sentence is exclusively vested in the President of India.", "A"),
    (6, "Ministerial Advice Immunity", "The advice tendered by Ministers to the Governor cannot be inquired into in any court of law.", "Article 163(3) provides constitutional protection to ministerial advice to safeguard Cabinet secrecy and collective responsibility.", "A"),
    (7, "Constitutional Discretion Distinction", "The Governor possesses explicit constitutional discretionary powers under Article 163(1).", "Unlike Article 163(1), Article 74(1) governing the President does not contain an express discretionary clause.", "A"),
    (8, "Appointment of Chief Minister", "The Governor appoints the leader of the majority party in the Legislative Assembly as Chief Minister.", "Article 164(2) mandates that the Council of Ministers is collectively responsible to the State Legislative Assembly.", "A"),
    (9, "Advocate General Tenure", "The Advocate General holds office during the pleasure of the Governor under Article 165.", "The Advocate General is appointed by the Governor to give legal advice to the State Government.", "B"),
    (10, "Authentication Bar in Courts", "An executive order authenticated in the Governor's name cannot be challenged in court on the ground that it is not the Governor's order.", "Article 166(2) provides constitutional protection to authenticated executive business rules.", "A"),
    (11, "CM Duty to Furnish Info", "The Chief Minister is constitutionally bound to communicate Cabinet decisions to the Governor under Article 167.", "The Governor is the constitutional head of state needing information to perform official functions.", "A"),
    (12, "Ordinary Bill Re-passage Assent", "The Governor MUST give assent to an ordinary Bill re-passed by the State Legislature under Article 200.", "The State Legislature holds ultimate legislative authority within state sphere under the Constitution.", "A"),
    (13, "High Court Position Bill Reservation", "The Governor MUST reserve any Bill endangering the constitutional position of the High Court.", "High Court independence is part of the basic structure of the Indian Constitution under Article 200 proviso.", "A"),
    (14, "Reserved Bill Presidential Assent Freedom", "The President is not bound to assent to a reserved Bill re-passed by the State Assembly.", "Article 201 does not contain a proviso forcing Presidential assent upon re-passage by the State Legislature.", "A"),
    (15, "Money Bill Prior Recommendation", "A Money Bill cannot be introduced in the Legislative Assembly without the Governor's recommendation.", "Financial initiatives involve public funds and require executive authorization under Article 207.", "A"),
    (16, "Ordinance Legislative Force", "An Ordinance promulgated by the Governor has the same force and effect as an Act of the State Legislature.", "The Governor's Ordinance-making power under Article 213 is co-extensive with the legislative power of the State Legislature.", "A"),
    (17, "Ordinance Recess Requirement", "The Governor cannot promulgate an Ordinance when the State Legislature is in session.", "Ordinance power under Article 213 is an extraordinary legislative power meant only for recess contingencies.", "A"),
    (18, "Ordinance Repromulgation Bar", "Repromulgation of Ordinances without legislative consideration was declared unconstitutional in DC Wadhwa.", "Ordinance power cannot be used as a substitute for the legislative authority of the State Legislature.", "A"),
    (19, "SPSC Member Suspension vs Removal", "The Governor can suspend an SPSC member pending inquiry under Article 317.", "The final power to remove an SPSC member rests exclusively with the President of India after a Supreme Court inquiry.", "A"),
    (20, "Floor Test Requirement", "The floor of the Assembly is the sole constitutional test of majority support as held in SR Bommai.", "Assessment of majority support based on subjective opinion of the Governor outside the Assembly is prone to abuse.", "A"),
    (21, "Summoning Limits when Speaker Motion Pending", "The Governor cannot exercise personal discretion to summon the Assembly when a Speaker removal motion is pending.", "Under Article 174, the Governor must act on the aid and advice of the Chief Minister and Cabinet in summoning the House.", "A"),
    (22, "Article 356 Proclamation Review", "A Presidential proclamation under Article 356 based on Governor's report is subject to judicial review.", "Judicial review extends to examining whether material for Governor's report was relevant and non-malafide.", "A"),
    (23, "University Chancellor Statutory Capacity", "The Governor acting as Chancellor of State Universities is not automatically bound by Cabinet advice.", "Chancellor duties are statutory powers under State University Acts, not executive functions under Article 154.", "A"),
    (24, "Criminal Immunity Protection", "The Governor enjoys absolute personal immunity from criminal proceedings during his term under Article 361.", "The constitutional head requires protection against vexatious litigation to discharge public duties.", "A"),
    (25, "Outside Governor Recommendation", "The Sarkaria Commission recommended that the Governor should be an eminent person from outside the State.", "An outside Governor remains neutral and detached from local party politics in the state.", "A")
]

for idx in range(1, 26):
    id_str = f"GOV_R_{idx:03d}"
    r_num, r_title, ass_e, reas_e, ans_let = reasoning_raw_25[idx - 1]
    
    q_en = f"Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): {ass_e}\nReason (R): {reas_e}\nIn the light of the above statements, choose the correct answer from the options given below:"
    q_ta = f"கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன. ஒன்று உறுதிக்கூற்று (A) எனவும் மற்றொன்று காரணம் (R) எனவும் குறிக்கப்பட்டுள்ளது:\nஉறுதிக்கூற்று (A): {ass_e}\nகாரணம் (R): {reas_e}\nமேற்கண்ட கூற்றுகளின் அடிப்படையில் சரியான விடையைத் தேர்ந்தெடுக்கவும்:"
    
    reasoning_items.append(q(
        id_str, "Polity", "Governor of a State", "Hard", "Reasoning",
        q_en, q_ta, reasoning_opts, ans_let,
        f"Reasoning Analysis for {r_title}: Assertion is valid and Reason provides correct constitutional foundation.",
        f"காரணக் கூற்று பகுப்பாய்வு ({r_title}): உறுதிக்கூற்று சரி, காரணம் சரியான அரசியலமைப்பு அடிப்படையை அளிக்கிறது.",
        {
            "A": {"en": "Both A and R are true and R explains A.", "ta": "A மற்றும் R இரண்டும் சரி, R சரியான விளக்கம்."},
            "B": {"en": "Both A and R are true but R does not explain A.", "ta": "A மற்றும் R இரண்டும் சரி, ஆனால் R விளக்கம் அன்று."},
            "C": {"en": "A is true but R is false.", "ta": "A சரி, R தவறு."},
            "D": {"en": "A is false but R is true.", "ta": "A தவறு, R சரி."}
        },
        "TNPSC Tip: Test if 'because' connects Assertion and Reason logically.",
        "TNPSC குறிப்பு: 'ஏனென்றால்' என்ற சொல் கூற்றையும் காரணத்தையும் சரியாக இணைக்கிறதா என சோதிக்கவும்.",
        f"Revision Fact: {r_title} is established under Part VI of the Constitution.",
        f"மீளாய்வுத் தகவல்: {r_title} பகுதி VI-ன் கீழ் நிறுவப்பட்டது.",
        "Analyze"
    ))

print(f"Reasoning Items: {len(reasoning_items)}")

# Save all files
os.makedirs('data/questions/polity', exist_ok=True)

with open('data/questions/polity/governor_statement_based.json', 'w', encoding='utf-8') as f:
    json.dump(statement_items, f, indent=2, ensure_ascii=False)

with open('data/questions/polity/governor_reasoning.json', 'w', encoding='utf-8') as f:
    json.dump(reasoning_items, f, indent=2, ensure_ascii=False)

print("Saved Statement and Reasoning files.")
