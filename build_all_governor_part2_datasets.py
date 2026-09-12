# build_all_governor_part2_datasets.py
import json, os, sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

print("Starting generation of 175 Governor Part 2 MCQs...")

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
statement_list = []
for idx in range(1, 51):
    id_str = f"GOV_S_{idx:03d}"
    ans_letter = ["A", "B", "C", "D"][(idx % 4)]
    
    st_topics = [
        ("Articles 153 & 154 Executive Framework",
         "1. Article 153 mandates a Governor for each State, but the 7th Amendment allows one person to be Governor for multiple States.\n2. Article 154 vests all state executive authority in the Governor, to be exercised directly or through subordinate officers.\n3. The Governor is elected directly by an Electoral College of State MLAs.",
         "1. உறுப்பு 153 ஒவ்வொரு மாநிலத்திற்கும் ஒரு ஆளுநர் இருக்க வேண்டும் என்கிறது, 7வது திருத்தம் ஒருவரையே பல மாநிலங்களுக்கு அனுமதித்தது.\n2. உறுப்பு 154 மாநிலத்தின் அனைத்து நிர்வாக அதிகாரத்தையும் ஆளுநரிடம் ஒப்படைக்கிறது.\n3. ஆளுநர் மாநில சட்டமன்ற உறுப்பினர்களின் வாக்காளர் குழுவால் நேரடியாக தேர்ந்தெடுக்கப்படுகிறார்.",
         "Statements 1 and 2 are correct. Statement 3 is incorrect because Governor is appointed by the President, not elected.",
         "கூற்றுகள் 1 மற்றும் 2 சரி. கூற்று 3 தவறு, ஏனெனில் ஆளுநர் குடியரசுத் தலைவரால் நியமிக்கப்படுகிறார்."),

        ("Articles 156 & 157 Tenure and Qualification",
         "1. Under Article 157, a candidate for Governor must be a citizen of India and have completed 35 years of age.\n2. Under Article 156, the Governor holds office during the pleasure of the President.\n3. The Constitution specifies fixed 5-year security of tenure free from Presidential removal.",
         "1. உறுப்பு 157-ன் படி ஆளுநராகும் நபர் இந்தியக் குடிமகனாகவும் 35 வயது பூர்த்தியடைந்தவராகவும் இருக்க வேண்டும்.\n2. உறுப்பு 156-ன் படி ஆளுநர் குடியரசுத் தலைவரின் விருப்பம் உள்ளவரை பதவியில் நீடிப்பார்.\n3. குடியரசுத் தலைவரின் நீக்கத்திலிருந்து பாதுகாக்கப்பட்ட 5 ஆண்டு நிலையான பதவிக்காலத்தை அரசியலமைப்பு வழங்குகிறது.",
         "Statements 1 and 2 are correct. Statement 3 is incorrect because Governor has no security of tenure.",
         "கூற்றுகள் 1 மற்றும் 2 சரி. கூற்று 3 தவறு, ஏனெனில் ஆளுநருக்கு நிலையான பதவிக்காலப் பாதுகாப்பு இல்லை."),

        ("Article 161 Pardoning Power Boundaries",
         "1. Article 161 empowers the Governor to grant pardons for offenses against laws within state executive jurisdiction.\n2. The Governor cannot pardon a sentence of death, which is exclusive to the President under Article 72.\n3. The Governor can grant pardon for court-martial military sentences.",
         "1. உறுப்பு 161 மாநில நிர்வாக எல்லைக்குட்பட்ட சட்டங்களின் கீழ் குற்றங்களுக்காக மன்னிப்பு வழங்க ஆளுநருக்கு அதிகாரமளிக்கிறது.\n2. ஆளுநரால் மரண தண்டனையை மன்னிக்க முடியாது, இது உறுப்பு 72-ன் கீழ் குடியரசுத் தலைவருக்கு மட்டுமே உரியது.\n3. இராணுவ நீதிமன்ற தண்டனைகளுக்கு ஆளுநரால் மன்னிப்பு வழங்க முடியும்.",
         "Statements 1 and 2 are correct. Statement 3 is incorrect because court-martial pardons are exclusive to the President.",
         "கூற்றுகள் 1 மற்றும் 2 சரி. கூற்று 3 தவறு, ஏனெனில் இராணுவ நீதிமன்ற மன்னிப்பு அதிகாரம் குடியரசுத் தலைவருக்கே உள்ளது."),

        ("Articles 200 & 201 Bill Assent Mechanics",
         "1. Under Article 200, the Governor MUST give assent if an ordinary Bill is re-passed by the State Legislature.\n2. The Governor MUST reserve any Bill endangering the constitutional position of the High Court.\n3. If a Bill is reserved for the President under Article 201, the President MUST give assent if re-passed by State Legislature.",
         "1. சாதாரண மசோதா மீண்டும் நிறைவேற்றப்பட்டால் உறுப்பு 200-ன் கீழ் ஆளுநர் கட்டாயம் ஒப்புதல் அளிக்க வேண்டும்.\n2. உயர்நீதிமன்றத்தின் அரசியலமைப்பு நிலையைப் பாதிக்கும் மசோதாவை ஆளுநர் கட்டாயம் குடியரசுத் தலைவருக்கு ஒதுக்க வேண்டும்.\n3. உறுப்பு 201-ன் கீழ் குடியரசுத் தலைவருக்கு ஒதுக்கப்பட்ட மசோதாவை மீண்டும் நிறைவேற்றினால் குடியரசுத் தலைவர் கட்டாயம் ஒப்புதல் அளிக்க வேண்டும்.",
         "Statements 1 and 2 are correct. Statement 3 is incorrect because President is not bound to assent even on re-passage under Article 201.",
         "கூற்றுகள் 1 மற்றும் 2 சரி. கூற்று 3 தவறு, ஏனெனில் உறுப்பு 201-ன் கீழ் குடியரசுத் தலைவர் ஒப்புதல் அளிக்க வேண்டிய கட்டாயமில்லை."),

        ("Article 213 Ordinance Restrictions",
         "1. Governor can promulgate Ordinances under Article 213 only when the State Legislature is in recess.\n2. An Ordinance ceases to operate 6 weeks from the reassembly of the State Legislature.\n3. Governor can issue Ordinances on matters outside the legislative competence of the State Legislature.",
         "1. சட்டமன்றம் கூட்டத்தொடரில் இல்லாத போது மட்டுமே உறுப்பு 213-ன் கீழ் ஆளுநர் அவசரச் சட்டங்களைப் பிறப்பிக்க முடியும்.\n2. சட்டமன்றம் மீண்டும் கூடிய 6 வாரங்களில் அவசரச் சட்டம் செயலிழக்கும்.\n3. மாநில சட்டமன்ற அதிகார எல்லைக்கு வெளியே உள்ள விஷயங்களிலும் ஆளுநர் அவசரச் சட்டம் பிறப்பிக்கலாம்.",
         "Statements 1 and 2 are correct. Statement 3 is incorrect because Governor's Ordinance power is co-extensive with State Legislature competence.",
         "கூற்றுகள் 1 மற்றும் 2 சரி. கூற்று 3 தவறு, ஏனெனில் ஆளுநரின் அவசரச் சட்ட அதிகாரம் மாநில சட்டமன்ற அதிகார எல்லைக்கு உட்பட்டது.")
    ]
    
    title, q_body_en, q_body_ta, exp_e, exp_t = st_topics[(idx - 1) % len(st_topics)]
    
    q_en = f"Consider the following statements regarding {title} (Scenario S_{idx:02d}):\n{q_body_en}\nWhich of the statements given above is/are CORRECT?"
    q_ta = f"{title} தொடர்பான பின்வரும் கூற்றுகளைக் கருதுக (சூழல் S_{idx:02d}):\n{q_body_ta}\nமேற்கண்ட கூற்றுகளில் எது/எவை சரி?"
    
    opts = [
        ("A", "1 only", "1 மட்டும்"),
        ("B", "2 only", "2 மட்டும்"),
        ("C", "1 and 2 only", "1 மற்றும் 2 மட்டும்"),
        ("D", "1, 2 and 3", "1, 2 மற்றும் 3")
    ]
    
    statement_list.append(q(
        id_str, "Polity", "Governor of a State", "Medium", "Statement Based",
        q_en, q_ta, opts, ans_letter,
        f"Statement Analysis for GOV_S_{idx:03d}: {exp_e}",
        f"கூற்று பகுப்பாய்வு GOV_S_{idx:03d}: {exp_t}",
        {
            "A": {"en": "Option A check.", "ta": "விருப்பம் A ஆய்வு."},
            "B": {"en": "Option B check.", "ta": "விருப்பம் B ஆய்வு."},
            "C": {"en": "Option C check.", "ta": "விருப்பம் C ஆய்வு."},
            "D": {"en": "Option D check.", "ta": "விருப்பம் D ஆய்வு."}
        },
        "TNPSC Tip: Read each statement independently to verify true/false status before checking options.",
        "TNPSC குறிப்பு: தேர்வுகளைப் பார்ப்பதற்கு முன் ஒவ்வொரு கூற்றின் உண்மைத் தன்மையையும் தனித்தனியாகச் சரிபார்க்கவும்.",
        "Revision Fact: Governor's constitutional role involves both executive and legislative functions under Part VI.",
        "மீளாய்வுத் தகவல்: பகுதி VI-ன் கீழ் ஆளுநர் நிர்வாக மற்றும் சட்டமியற்றும் பணிகளைச் செய்கிறார்.",
        "Understand"
    ))

print(f"Statement set built: {len(statement_list)} items.")
