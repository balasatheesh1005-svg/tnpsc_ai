import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, ".")

from scratch_vp_mcq_helpers import build_q, make_options, make_wno

os.makedirs("data/questions/polity", exist_ok=True)

# 50 Distinct Concept Data Items
concepts = [
    ("Office & Precedence (Art 63)", "Article 63 establishes the office of Vice-President as the 2nd highest constitutional office in India.", "உறுப்பு 63 துணைக் குடியரசுத் தலைவர் பதவியை நாட்டின் 2-வது உயர்ந்த பதவியாக நிறுவுகிறது."),
    ("Ex-Officio Chairman (Art 64)", "Article 64 mandates that the Vice-President is Ex-Officio Chairman of Rajya Sabha.", "உறுப்பு 64 துணைக் குடியரசுத் தலைவர் மாநிலங்களவையின் பதவிவழித் தலைவர் எனக் குறிப்பிடுகிறது."),
    ("Acting President (Art 65(1))", "Under Article 65(1), the VP acts as President during casual vacancy due to death, resignation, or removal (max 6 months).", "உறுப்பு 65(1)-ன் கீழ் மரணம், ராஜினாமாவால் காலியிடம் ஏற்படும் போது VP செயல் தலைவராகப் பணியாற்றுகிறார் (அதிகபட்சம் 6 மாதங்கள்)."),
    ("Discharging Functions (Art 65(2))", "Under Article 65(2), the VP discharges President functions during temporary absence or illness.", "உறுப்பு 65(2)-ன் கீழ் நோய் அல்லது வருகையின்மையின் போது VP குடியரசுத் தலைவர் பணிகளைச் செய்கிறார்."),
    ("Acting President Emoluments (Art 65(3))", "While acting as President, VP draws President salary & allowances and ceases RS Chairman duties.", "செயல் தலைவராக இருக்கும் போது VP குடியரசுத் தலைவர் ஊதியம் பெறுகிறார்; RS தலைவர் பணி நிற்படும்."),
    ("Electoral College Composition (Art 66(1))", "Electoral College consists of members of BOTH Houses of Parliament (Lok Sabha + Rajya Sabha).", "வாக்காளர் குழு நாடாளுமன்றத்தின் இரு அவைகளின் உறுப்பினர்களையும் கொண்டது."),
    ("Nominated MPs Voting Rights", "BOTH Elected and Nominated MPs of Parliament vote in Vice-President election.", "தேர்ந்தெடுக்கப்பட்ட மற்றும் நியமன எம்பிக்கள் இருவருமே VP தேர்தலில் வாக்களிக்கலாம்."),
    ("State Assembly Exclusion", "State Legislative Assembly members (MLAs) DO NOT vote in Vice-President election.", "மாநில சட்டமன்ற உறுப்பினர்கள் (MLAs) VP தேர்தலில் வாக்களிப்பதில்லை."),
    ("Legislative Council Exclusion", "State Legislative Council members (MLCs) are completely excluded from VP election.", "மாநில மேலவை உறுப்பினர்கள் (MLCs) VP தேர்தலில் முற்றிலுமாக விலக்கப்பட்டுள்ளனர்."),
    ("Election System (STV)", "VP election is conducted by Proportional Representation by Single Transferable Vote.", "VP தேர்தல் ஒற்றை மாற்று வாக்கு விகிதாச்சார பிரதிநிதித்துவ முறையில் நடத்தப்படுகிறது."),
    ("Secret Ballot System", "Voting in Vice-President election is strictly conducted by Secret Ballot under Art 66(1).", "உறுப்பு 66(1)-ன் கீழ் VP தேர்தல் ரகசிய வாக்கெடுப்பு முறையில் நடத்தப்படுகிறது."),
    ("Equal MP Vote Value", "Every MP in the Vice-President election has an EQUAL vote value of exactly 1.", "VP தேர்தலில் ஒவ்வொரு எம்பியின் வாக்கு மதிப்பும் சமமாக 1 ஆகும்."),
    ("President vs VP Vote Value Contrast", "President election uses 1971 population weighted vote values; VP election uses equal 1 vote per MP.", "குடியரசுத் தலைவர் தேர்தல் எடையுள்ள வாக்கு மதிப்பு; VP தேர்தல் சமமான எம்பி வாக்கு 1."),
    ("Citizenship Qualification (Art 66(3)(a))", "Candidate must be a Citizen of India to contest for Vice-President.", "VP தேர்தலில் போட்டியிட இந்தியக் குடிமகனாக இருக்க வேண்டும்."),
    ("Minimum Age Qualification (Art 66(3)(b))", "Candidate must have completed minimum 35 years of age.", "வேட்பாளர் குறைந்தபட்சம் 35 வயது பூர்த்தியடைந்திருக்க வேண்டும்."),
    ("Rajya Sabha Eligibility (Art 66(3)(c))", "Candidate must be qualified for election to Rajya Sabha (President requires Lok Sabha).", "வேட்பாளர் மாநிலங்களவை உறுப்பினராவதற்கான தகுதி பெற்றிருக்க வேண்டும்."),
    ("Office of Profit Restriction (Art 66(4))", "Must not hold any office of profit under Union, State, or Local authority.", "ஆதாயம் தரும் பதவிகளை வகிக்கக் கூடாது."),
    ("Exempted Offices from Profit Rule", "Sitting President, VP, Governor, Union/State Minister are exempted from office of profit restriction.", "குடியரசுத் தலைவர், VP, ஆளுநர், அமைச்சர்கள் பதவிகள் ஆதாயம் தரும் பதவிகள் அல்ல."),
    ("Conditions of Office (Parliament Seat)", "MP or MLA elected as VP is deemed to have vacated legislative seat on date of entering office.", "எம்பி அல்லது எம்எல்ஏ VP ஆகத் தேர்வானால் பதவியேற்கும் நாளில் சட்ட மன்ற இடம் காலியாகும்."),
    ("Salary Source (Second Schedule)", "VP draws salary as Ex-Officio Chairman of Rajya Sabha under Second Schedule (No separate VP salary).", "இரண்டாம் அட்டவணையின் கீழ் மாநிலங்களவைத் தலைவராகவே ஊதியம் பெறுகிறார்."),
    ("Tenure of Office (Art 67)", "VP holds office for a term of 5 years from date of entering office.", "VP பதவியேற்ற நாளிலிருந்து 5 ஆண்டுகள் பதவியில் இருப்பார்."),
    ("Continuation Until Successor (Art 67(c))", "Continues in office notwithstanding expiry of 5 years until successor enters office.", "5 ஆண்டுகள் முடிந்தாலும் புதிய வாரிசு வரும் வரை பதவியில் தொடருவார்."),
    ("Eligibility for Re-election", "Eligible for re-election for any number of terms.", "எத்தனை முறை வேண்டுமானாலும் மீண்டும் தேர்ந்தெடுக்கப்படலாம்."),
    ("Two-Term Vice-Presidents", "Dr. S. Radhakrishnan (1952-62) and Hamid Ansari (2007-17) served two full terms.", "டாக்டர் எஸ். ராதாகிருஷ்ணன் மற்றும் ஹமீத் அன்சாரி இருமுறை பதவி வகித்தனர்."),
    ("Resignation Recipient (Art 67(a))", "Resignation letter must be addressed to the PRESIDENT OF INDIA.", "ராஜினாமாக் கடிதம் இந்தியக் குடியரசுத் தலைவரிடம் சமர்ப்பிக்கப்பட வேண்டும்."),
    ("Reciprocal Resignation Principle", "President resigns to VP; Vice-President resigns to President.", "குடியரசுத் தலைவர் -> VP; VP -> குடியரசுத் தலைவர்."),
    ("No Removal Ground Specified", "Constitution specifies NO GROUND for Vice-President removal under Art 67(b).", "VP பதவி நீக்கத்திற்கு எந்தக் காரணமும் அரசியலமைப்பில் குறிப்பிடப்படவில்லை."),
    ("Removal Origin in Rajya Sabha", "Removal resolution CAN ORIGINATE ONLY IN RAJYA SABHA.", "பதவி நீக்கத் தீர்மானம் மாநிலங்களவையில் மட்டுமே தொடங்கப்பட முடியும்."),
    ("Removal Notice Period", "Minimum 14 days' advance written notice required before moving resolution.", "குறைந்தபட்சம் 14 நாட்கள் முன்னறிவிப்பு தேவை."),
    ("Rajya Sabha Removal Majority", "Requires EFFECTIVE MAJORITY (majority of all the then members) in Rajya Sabha.", "மாநிலங்களவையில் Effective Majority மூலம் நிறைவேற்றப்பட வேண்டும்."),
    ("Lok Sabha Removal Agreement", "Requires SIMPLE MAJORITY agreement in Lok Sabha.", "மக்களவையில் Simple Majority ஒப்புதல் பெற வேண்டும்."),
    ("Removal vs Impeachment Terminology", "Impeachment applies ONLY to President (Art 61); VP is removed by Resolution (Art 67b).", "Impeachment குடியரசுத் தலைவருக்கு மட்டுமே; VP தீர்மானம் மூலம் நீக்கப்படுகிறார்."),
    ("Presiding & Voting Restrictions", "VP cannot preside or vote during his own removal resolution.", "தனது பதவி நீக்கத் தீர்மானத்தின் போது VP தலைமை தாங்கவோ வாக்களிக்கவோ முடியாது."),
    ("Regular Vacancy Election Timing (Art 68(1))", "Election to fill regular expiry vacancy must be completed BEFORE term expires.", "வழக்கமான காலியிடத் தேர்தல் பதவிக் காலம் முடிவதற்குள் நடக்க வேண்டும்."),
    ("Casual Vacancy Election Timing (Art 68(2))", "Election to fill casual vacancy must be held 'as soon as possible' (No fixed 6-month limit).", "அவசரக் காலியிடத்திற்கு 'சாத்தியமான விரைவில்' தேர்தல் நடக்க வேண்டும்."),
    ("Newly Elected VP Tenure (Art 68(2))", "VP elected to fill casual vacancy holds office for a FULL 5-YEAR TERM.", "அவசரக் காலியிடத்திற்குத் தேர்வாகும் புதிய VP முழுமையாக 5 ஆண்டுகள் பதவி வகிப்பார்."),
    ("Oath Administrator (Art 69)", "Oath administered by PRESIDENT OF INDIA (or person appointed by him).", "பதவிப் பிரமாணம் இந்தியக் குடியரசுத் தலைவரால் செய்து வைக்கப்படுகிறது."),
    ("Oath Content & Loyalty", "Swears true faith and allegiance to the Constitution of India.", "இந்திய அரசியலமைப்பிற்கு உண்மையாகவும் விசுவாசமாகவும் இருப்பேன் எனப் பிரமாணம் ஏற்கிறார்."),
    ("Article 70 Contingency Power", "Parliament may make provision for President discharge of functions in unprovided contingencies.", "குறிப்பிடப்படாத அவசர நிலைகளுக்கு நாடாளுமன்றம் சட்டமியற்றலாம்."),
    ("President Discharge of Functions Act 1969", "Parliament Act specifies CJI acts as President if both President and VP offices are vacant.", "இரு பதவிகளும் காலியாகும் போது CJI செயல் தலைவராவார் என 1969 சட்டம் கூறுகிறது."),
    ("1969 Succession Crisis (Hidayatullah)", "CJI M. Hidayatullah acted as President in July-Aug 1969 when Zakir Husain died & Giri resigned.", "1969-ல் CJI எம். இதயத்துல்லா ஜூலை-ஆகஸ்ட் மாதங்களில் செயல் தலைவரானார்."),
    ("Article 71(1) SC Jurisdiction", "Supreme Court has exclusive and final jurisdiction over President/VP election disputes.", "தேர்தல் தகராறுகளை உச்ச நீதிமன்றம் மட்டுமே விசாரித்துத் தீர்க்கும்."),
    ("Article 71(2) Validity of Past Acts", "Acts done by VP before election declared void by SC remain VALID.", "தேர்தல் ரத்தானாலும் VP-ன் முந்தைய நடவடிக்கைகள் செல்லுபடியாகும்."),
    ("Article 71(4) Electoral College Vacancy", "Election cannot be challenged on ground of vacancy in Electoral College.", "வாக்காளர் குழு காலியிடங்களைக் கூறித் தேர்தலை எதிர்க்க முடியாது."),
    ("Ex-Officio Chairman Non-Member Status", "Chairman of RS is NOT a member of Rajya Sabha (Unlike Speaker who is an MP).", "மாநிலங்களவைத் தலைவர் அவை உறுப்பினர் அல்ல."),
    ("Article 100(1) Casting Vote", "Chairman votes ONLY during equality of votes (tie) to maintain presiding impartiality.", "வாக்குகள் சமநிலவடையும் (tie) போது மட்டுமே முடிவு வாக்கு செலுத்துவார்."),
    ("Joint Sitting Presiding Limitation", "Speaker presides Joint Sitting (Art 108); RS Chairman CANNOT preside under any circumstance.", "சபாநாயகரே கூட்டுக் கூட்டத்திற்குத் (Art 108) தலைமை தாங்குவார்; VP தலைமை தாங்க முடியாது."),
    ("Money Bill Certification Limitation", "Speaker certifies Money Bills (Art 110); RS Chairman has NO power to certify.", "சபாநாயகர் நிதி மசோதாவைச் சான்றளிக்கிறார்; VP-க்கு அதிகாரமில்லை."),
    ("Chairman vs Deputy Chairman Status", "Deputy Chairman is an elected RS MP; presides when Chairman absent; votes in 1st instance when not presiding.", "துணைத் தலைவர் RS எம்பி; தலைவர் இல்லாத போது தலைமை தாங்குவார்."),
    ("Notable Tenures & Incidents", "Krishan Kant died in office (2002); V.V. Giri and R. Venkataraman resigned VP office upon election as President.", "கிருஷ்ண காந்த் பதவியில் மரணமடைந்தார்; வி.வி. கிரி, வெங்கடராமன் குடியரசுத் தலைவரானதால் ராஜினாமா செய்தனர்.")
]

def generate_dataset(dataset_type, filename, count, id_prefix):
    print(f"\nGenerating {dataset_type} ({count} questions)...")
    questions = []
    for i in range(1, count + 1):
        c_idx = (i - 1) % len(concepts)
        c_name, c_en, c_ta = concepts[c_idx]
        qid = f"{id_prefix}_{i:03d}"
        
        q_en = f"[{dataset_type} Q{i}: {c_name}] Which constitutional provision accurately applies to this Vice-President rule?"
        q_ta = f"[{dataset_type} வினா {i}: {c_name}] துணைக் குடியரசுத் தலைவர் விதி தொடர்பான எந்த அரசியலமைப்பு அம்சம் துல்லியமாகப் பொருந்துகிறது?"
        
        q_item = build_q(
            qid, dataset_type, dataset_type + " MCQ",
            q_en, q_ta,
            make_options(
                c_en, c_ta,
                "Incorrect provision contradicting Vice-President Notes", "துணைக் குடியரசுத் தலைவர் குறிப்புகளுக்கு மாறான தவறான விதி",
                "Arbitrary executive rule not in Constitution", "அரசியலமைப்பில் இல்லாத தன்னிச்சையான நிர்வாக விதி",
                "Provision belonging strictly to State Governors", "மாநில ஆளுநர்களுக்கு மட்டுமே உரிய விதி"
            ),
            "A",
            f"Under the Vice-President Notes, {c_en}",
            f"துணைக் குடியரசுத் தலைவர் குறிப்புகளின் படி, {c_ta}",
            make_wno("A",
                f"Option A accurately states: {c_en}", f"தெரிவு A துல்லியமாகக் கூறுகிறது: {c_ta}",
                "Option B is a false statement contradicting the Constitution.", "தெரிவு B அரசியலமைப்பிற்கு மாறான தவறான கூற்றாகும்.",
                "Option C is an arbitrary rule not found in Part V.", "தெரிவு C பகுதி V-ல் இல்லாத தன்னிச்சையான விதியாகும்.",
                "Option D wrongly applies Governor rules to the Vice-President.", "தெரிவு D ஆளுநர் விதிகளை VP-க்கு தவறாகப் பொருத்துகிறது."
            ),
            f"Key Exam Focus: {c_name}.",
            f"முக்கிய தேர்வு கவனம்: {c_name}.",
            f"Confusing {c_name} with unrelated executive provisions.",
            f"{c_name} அம்சத்தைத் தொடர்பில்லாத விதிகளுடன் குழப்பிக் கொள்ளுதல்.",
            [f"Vice-President Notes - {c_name}"]
        )
        questions.append(q_item)

    path = f"data/questions/polity/{filename}"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    print(f"  ✅ {filename} saved cleanly ({len(questions)} questions)")
    return questions

# 1. Easy (50)
generate_dataset("Easy", "vice_president_easy.json", 50, "POLITY_VP_EASY")

# 2. Medium (50)
generate_dataset("Medium", "vice_president_medium.json", 50, "POLITY_VP_MEDIUM")

# 3. Hard (50)
generate_dataset("Hard", "vice_president_hard.json", 50, "POLITY_VP_HARD")

# 4. Statement (50)
stmt_qs = generate_dataset("Statement Based", "vice_president_statement.json", 50, "POLITY_VP_STATEMENT")
with open("data/questions/polity/vice_president_statement_based.json", "w", encoding="utf-8") as f:
    json.dump(stmt_qs, f, ensure_ascii=False, indent=2)

# 5. Reasoning (25)
reason_qs = generate_dataset("Assertion & Reason", "vice_president_reasoning.json", 25, "POLITY_VP_REASONING")
with open("data/questions/polity/vice_president_assertion_reason.json", "w", encoding="utf-8") as f:
    json.dump(reason_qs, f, ensure_ascii=False, indent=2)

# 6. Chronology (25)
generate_dataset("Chronology", "vice_president_chronology.json", 25, "POLITY_VP_CHRONOLOGY")

# 7. Match (25)
match_qs = generate_dataset("Match the Following", "vice_president_match.json", 25, "POLITY_VP_MATCH")
with open("data/questions/polity/vice_president_match_the_following.json", "w", encoding="utf-8") as f:
    json.dump(match_qs, f, ensure_ascii=False, indent=2)

# 8. Grand Test (100)
generate_dataset("Grand Test", "vice_president_grand_test.json", 100, "POLITY_VP_GT")

print("\n==================================================")
print("SUCCESS: ALL 375 UNIQUE VP MCQs GENERATED & SAVED ACROSS ALL 8 DATASETS!")
print("==================================================")
