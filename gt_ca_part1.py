# Grand Test Constitutional Amendments - Part 1 (Q1 to Q25)
# Balanced Answer Key: 6 A, 6 B, 6 C, 7 D = 25 Total

part1_questions = []

def add_p1(q_id, difficulty, q_type, q_en, q_ta,
           opt_a_en, opt_a_ta, opt_b_en, opt_b_ta, opt_c_en, opt_c_ta, opt_d_en, opt_d_ta,
           correct_ans, exp_en, exp_ta,
           why_a_en, why_a_ta, why_b_en, why_b_ta, why_c_en, why_c_ta, why_d_en, why_d_ta,
           tip_en, tip_ta, fact_en, fact_ta, bloom, pyq_sim, tags):
    part1_questions.append({
        "id": q_id,
        "subject": "Polity",
        "topic": "Constitutional Amendments",
        "difficulty": difficulty,
        "question_type": q_type,
        "question": {"en": q_en, "ta": q_ta},
        "options": [
            {"id": "A", "en": opt_a_en, "ta": opt_a_ta},
            {"id": "B", "en": opt_b_en, "ta": opt_b_ta},
            {"id": "C", "en": opt_c_en, "ta": opt_c_ta},
            {"id": "D", "en": opt_d_en, "ta": opt_d_ta}
        ],
        "correct_answer": correct_ans,
        "explanation": {"en": exp_en, "ta": exp_ta},
        "why_not_others": {
            "A": {"en": why_a_en, "ta": why_a_ta},
            "B": {"en": why_b_en, "ta": why_b_ta},
            "C": {"en": why_c_en, "ta": why_c_ta},
            "D": {"en": why_d_en, "ta": why_d_ta}
        },
        "tnpsc_tip": {"en": tip_en, "ta": tip_ta},
        "revision_fact": {"en": fact_en, "ta": fact_ta},
        "source_reference": [
            "M. Laxmikanth — Indian Polity (Constitutional Amendments)",
            "TNPSC Nova AI Notes — Constitutional Amendments (Part 1)",
            "NCERT Class XI - Indian Constitution at Work"
        ],
        "bloom_level": bloom,
        "estimated_time_sec": 60,
        "pyq_similarity": pyq_sim,
        "tags": tags
    })

# Q1 - Ans: B
add_p1(
    "polity_amendments_gt_001", "Easy", "single_choice",
    "Which Part and Article of the Constitution of India deal exclusively with the power of Parliament to amend the Constitution and its procedure?",
    "இந்திய அரசியலமைப்பின் எந்தப் பகுதியும் சரத்தும் அரசியலமைப்பைத் திருத்துவதற்கான நாடாளுமன்றத்தின் அதிகாரம் மற்றும் அதன் நடைமுறையைக் பிரத்யேகமாகக் குறிப்பிடுகின்றன?",
    "Part XIX, Article 356", "பகுதி XIX, சரத்து 356",
    "Part XX, Article 368", "பகுதி XX, சரத்து 368",
    "Part XXI, Article 370", "பகுதி XXI, சரத்து 370",
    "Part XXII, Article 395", "பகுதி XXII, சரத்து 395",
    "B",
    "📚 Core Explanation:\nPart XX, Article 368 of the Indian Constitution deals exclusively with the power of Parliament to amend the Constitution and the procedure therefor. Borrowed from the South African Constitution, Article 368 grants constituent power to Parliament.",
    "📚 முதன்மை விளக்கம்:\nஇந்திய அரசியலமைப்பின் பகுதி XX, சரத்து 368 ஆகியவை அரசியலமைப்பைத் திருத்துவதற்கான நாடாளுமன்றத்தின் அதிகாரம் மற்றும் நடைமுறையைக் குறிப்பிடுகின்றன. தென்னாப்பிரிக்க அரசியலமைப்பிலிருந்து பெறப்பட்ட சரத்து 368, நாடாளுமன்றத்திற்கு அரசியலமைப்பு ஆக்கல் அதிகாரத்தை வழங்குகிறது.",
    "Option A is incorrect because Part XIX deals with Miscellaneous provisions.",
    "விருப்பம் A தவறானது.",
    "Option B is correct as Part XX, Article 368 prescribes the amendment procedure.",
    "விருப்பம் B சரியானது.",
    "Option C is incorrect because Part XXI deals with Temporary provisions.",
    "விருப்பம் C தவறானது.",
    "Option D is incorrect because Part XXII deals with Short Title.",
    "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: Remember that Article 368 was borrowed from South Africa. Part XX contains only one single Article (Article 368).",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: சரத்து 368 தென்னாப்பிரிக்காவிலிருந்து பெறப்பட்டது என்பதை நினைவில் கொள்க.",
    "📖 Revision Fact: The 24th Amendment Act, 1971 amended Article 368 to clarify constituent power.",
    "📖 திருத்தல் செய்தி: 1971-ன் 24-வது சட்டத்திருத்தம் சரத்து 368-ஐத் திருத்தியது.",
    "Remember", "High", ["Article 368", "Part XX", "Procedure"]
)

# Q2 - Ans: C
add_p1(
    "polity_amendments_gt_002", "Easy", "single_choice",
    "Who among the following has the authority to introduce a Constitutional Amendment Bill in the Parliament of India?",
    "இந்திய நாடாளுமன்றத்தில் அரசியலமைப்பு திருத்த மசோதாவை அறிமுகப்படுத்தும் அதிகாரம் பெற்றவர் யார்?",
    "Only a Cabinet Minister with prior permission of the President", "குடியரசுத் தலைவரின் முன் அனுமதியுடன் கூடிய அமைச்சரவை அமைச்சர் மட்டுமே",
    "Only the Prime Minister or the Law Minister", "பிரதம அமைச்சர் அல்லது சட்ட அமைச்சர் மட்டுமே",
    "Either a Minister or a Private Member, without prior recommendation of the President", "குடியரசுத் தலைவரின் முன் பரிந்துரை இல்லாமல், ஒரு அமைச்சர் அல்லது தனிநபர் உறுப்பினர் எவரும்",
    "Only a member of the Lok Sabha with Speaker's approval", "சபாநாயகரின் ஒப்புதலுடன் மக்களவை உறுப்பினர் மட்டுமே",
    "C",
    "📚 Core Explanation:\nA Constitutional Amendment Bill can be introduced in either House of Parliament by either a Minister or a Private Member (non-minister MP). Importantly, prior permission or recommendation of the President is NOT required for its introduction.",
    "📚 முதன்மை விளக்கம்:\nஅரசியலமைப்பு திருத்த மசோதாவை நாடாளுமன்றத்தின் எந்த அவையிலும் ஒரு அமைச்சர் அல்லது தனிநபர் உறுப்பினர் (அமைச்சர் அல்லாத எம்பி) அறிமுகப்படுத்தலாம். முக்கியமாக, இத அறிமுகப்படுத்த குடியரசுத் தலைவரின் முன் அனுமதி தேவையில்லை.",
    "Option A is incorrect because private members can also introduce it.",
    "விருப்பம் A தவறானது.",
    "Option B is incorrect because any minister or MP can introduce it.",
    "விருப்பம் B தவறானது.",
    "Option C is correct as per Article 368 introducing procedure.",
    "விருப்பம் C சரியானது.",
    "Option D is incorrect because it can be introduced in Rajya Sabha as well.",
    "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: Unlike Money Bills (Art 110), Constitutional Amendment Bills do NOT require prior recommendation of the President.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: அரசியலமைப்பு திருத்த மசோதாவிற்கு குடியரசுத் தலைவரின் முன் பரிந்துரை தேவையில்லை.",
    "📖 Revision Fact: Private members can introduce Constitutional Amendment Bills.",
    "📖 திருத்தல் செய்தி: தனிநபர் உறுப்பினர்களும் அரசியலமைப்பு திருத்த மசோதாக்களை அறிமுகப்படுத்தலாம்.",
    "Understand", "High", ["Bill Introduction", "Private Member", "President Assent"]
)

# Q3 - Ans: D
add_p1(
    "polity_amendments_gt_003", "Easy", "single_choice",
    "What is the position regarding a Joint Sitting of both Houses of Parliament in case of a disagreement over a Constitutional Amendment Bill?",
    "அரசியலமைப்பு திருத்த மசோதா தொடர்பாக இரு அவைகளுக்கும் இடையே கருத்து வேறுபாடு ஏற்பட்டால், கூட்டு அமர்வு குறித்த நிலை என்ன?",
    "The President can summon a Joint Sitting under Article 108.", "குடியரசுத் தலைவர் சரத்து 108-ன் கீழ் கூட்டு அமர்வைக் கூட்டலாம்.",
    "The Prime Minister decides whether a Joint Sitting will be held.", "கூட்டு அமர்வு நடத்தப்படுமா என்பதை பிரதம அமைச்சர் தீர்மானிக்கிறார்.",
    "A Joint Sitting is automatically summoned after 6 months of disagreement.", "கருத்து வேறுபாடு ஏற்பட்டு 6 மாதங்களுக்குப் பிறகு தானாகவே கூட்டு அமர்வு கூட்டப்படும்.",
    "There is NO provision for a Joint Sitting to resolve deadlock over a Constitutional Amendment Bill.", "அரசியலமைப்பு திருத்த மசோதாவின் முட்டுக்கட்டையைத் தீர்க்க கூட்டு அமர்விற்கு எந்த விதியும் இல்லை.",
    "D",
    "📚 Core Explanation:\nEach House of Parliament must pass a Constitutional Amendment Bill separately by the required special majority. There is NO provision for holding a Joint Sitting under Article 108 for resolving a deadlock over a Constitutional Amendment Bill. If one House rejects the bill, the bill lapses.",
    "📚 முதன்மை விளக்கம்:\nஅரசியலமைப்பு திருத்த மசோதாவை நாடாளுமன்றத்தின் ஒவ்வொரு அவையும் தனித்தனியாக சிறப்பு பெரும்பான்மையுடன் நிறைவேற்ற வேண்டும். அரசியலமைப்பு திருத்த மசோதா மீதான முட்டுக்கட்டையைத் தீர்க்க சரத்து 108-ன் கீழ் கூட்டு அமர்வு நடத்த வழிவகை இல்லை.",
    "Option A is incorrect because Article 108 applies only to Ordinary and Financial Bills.",
    "விருப்பம் A தவறானது.",
    "Option B is incorrect because PM has no power to summon joint sittings.",
    "விருப்பம் B தவறானது.",
    "Option C is incorrect because automatic joint sitting does not exist.",
    "விருப்பம் C தவறானது.",
    "Option D is correct because no joint sitting is allowed for constitutional amendment bills.",
    "விருப்பம் D சரியானது.",
    "💡 TNPSC Tip: Joint Sitting (Art 108) is disallowed for Money Bills and Constitutional Amendment Bills.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: பண மசோதாக்கள் மற்றும் அரசியலமைப்பு திருத்த மசோதாக்களுக்கு கூட்டு அமர்வு நடத்த முடியாது.",
    "📖 Revision Fact: Rajya Sabha has an effective veto over Constitutional Amendment Bills.",
    "📖 திருத்தல் செய்தி: அரசியலமைப்பைத் திருத்துவதில் இரு அவைகளுக்கும் சம அதிகாரம் உள்ளது.",
    "Understand", "High", ["Joint Sitting", "Article 108", "Deadlock"]
)

# Q4 - Ans: A
add_p1(
    "polity_amendments_gt_004", "Easy", "single_choice",
    "Which Constitutional Amendment Act made it mandatory for the President of India to give assent to a Constitutional Amendment Bill?",
    "அரசியலமைப்பு திருத்த மசோதாவிற்கு குடியரசுத் தலைவர் கட்டாயமாக ஒப்புதல் அளிக்க வேண்டும் என்பதை எந்த அரசியலமைப்பு திருத்தச் சட்டம் கட்டாயமாக்கியது?",
    "24th Constitutional Amendment Act, 1971", "24-வது அரசியலமைப்பு திருத்தச் சட்டம், 1971",
    "42nd Constitutional Amendment Act, 1976", "42-வது அரசியலமைப்பு திருத்தச் சட்டம், 1976",
    "44th Constitutional Amendment Act, 1978", "44-வது அரசியலமைப்பு திருத்தச் சட்டம், 1978",
    "52nd Constitutional Amendment Act, 1985", "52-வது அரசியலமைப்பு திருத்தச் சட்டம், 1985",
    "A",
    "📚 Core Explanation:\nThe 24th Constitutional Amendment Act, 1971 amended Article 368 to make it obligatory/mandatory for the President to give assent to a Constitutional Amendment Bill presented after passage by both Houses.",
    "📚 முதன்மை விளக்கம்:\n1971-ஆம் ஆண்டின் 24-வது அரசியலமைப்பு திருத்தச் சட்டம் சரத்து 368-ஐத் திருத்தி, இரு அவைகளாலும் நிறைவேற்றப்பட்ட அரசியலமைப்பு திருத்த மசோதாவிற்கு குடியரசுத் தலைவர் கட்டாயமாக ஒப்புதல் அளிக்க வேண்டும் என மாற்றியது.",
    "Option A is correct as the 24th Amendment Act, 1971 made Presidential assent mandatory.",
    "விருப்பம் A சரியானது.",
    "Option B is incorrect; 42nd Amendment dealt with Mini-Constitution changes.",
    "விருப்பம் B தவறானது.",
    "Option C is incorrect; 44th Amendment restored democratic provisions.",
    "விருப்பம் C தவறானது.",
    "Option D is incorrect; 52nd Amendment introduced Anti-Defection Law.",
    "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: Prior to 1971, President had discretion. 24th Amendment made assent obligatory.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: 24-வது திருத்தம் ஒப்புதலைக் கட்டாயமாக்கியது.",
    "📖 Revision Fact: President cannot exercise Suspensive Veto or Pocket Veto on a Constitutional Amendment Bill.",
    "📖 திருத்தல் செய்தி: அரசியலமைப்பு திருத்த மசோதாவில் குடியரசுத் தலைவர் வீட்டோவைப் பயன்படுத்த முடியாது.",
    "Remember", "High", ["24th Amendment", "President Assent", "Article 368"]
)

# Q5 - Ans: D
add_p1(
    "polity_amendments_gt_005", "Easy", "single_choice",
    "What constitutes the 'Special Majority' required under Article 368 for passing a Constitutional Amendment Bill in a House of Parliament?",
    "நாடாளுமன்ற அவையில் அரசியலமைப்பு திருத்த மசோதாவை நிறைவேற்றுவதற்கு சரத்து 368-ன் கீழ் தேவைப்படும் 'சிறப்பு பெரும்பான்மை' என்பது எது?",
    "Simple majority of total membership of the House", "அவையின் மொத்த உறுப்பினர்களின் எளிய பெரும்பான்மை",
    "Three-fourths majority of total membership of the House", "அவையின் மொத்த உறுப்பினர்களில் முக்கால் பங்கு பெரும்பான்மை",
    "Two-thirds majority of members present and voting only, regardless of total strength", "மொத்த வலிமையைப் பொருட்படுத்தாமல், வந்திருந்து வாக்களிக்கும் உறுப்பினர்களில் 2/3 பங்கு பெரும்பான்மை மட்டுமே",
    "Majority of total membership of the House AND a majority of not less than two-thirds of members present and voting", "அவையின் மொத்த உறுப்பினர்களின் பெரும்பான்மை மற்றும் வந்திருந்து வாக்களிக்கும் உறுப்பினர்களில் 2/3 பங்கு குறையாத பெரும்பான்மை",
    "D",
    "📚 Core Explanation:\nUnder Article 368, Special Majority requires TWO conditions satisfied simultaneously in each House:\n1. Absolute Majority: More than 50% of the total membership of the House.\n2. 2/3rd Majority: Not less than two-thirds of the members present and voting.",
    "📚 முதன்மை விளக்கம்:\nசரத்து 368-ன் கீழ் சிறப்பு பெரும்பான்மை என்பது இரு நிபந்தனைகளைப் பூர்த்தி செய்ய வேண்டும்:\n1. அவையின் மொத்த உறுப்பினர்களின் எண்ணிக்கையில் 50%-க்கும் அதிகமான பெரும்பான்மை.\n2. அவைக்கு வருகை தந்து வாக்களிக்கும் உறுப்பினர்களில் 2/3 பங்கு குறையாத பெரும்பான்மை.",
    "Option A is incorrect because simple majority alone is insufficient.",
    "விருப்பம் A தவறானது.",
    "Option B is incorrect because 3/4th majority is not prescribed.",
    "விருப்பம் B தவறானது.",
    "Option C is incorrect because total membership condition must be met.",
    "விருப்பம் C தவறானது.",
    "Option D is correct as it accurately specifies both conditions of Article 368.",
    "விருப்பம் D சரியானது.",
    "💡 TNPSC Tip: Total membership includes ALL seats in the House, including vacancies and absentees.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: மொத்த உறுப்பினர்கள் என்பது காலியிடங்கள் மற்றும் வராதவர்களையும் உள்ளடக்கும்.",
    "📖 Revision Fact: In Lok Sabha (543 seats), total membership majority threshold is at least 272 members.",
    "📖 திருத்தல் செய்தி: மக்களவையில் மொத்த உறுப்பினர் பெரும்பான்மை வரம்பு 272 உறுப்பினர்கள் ஆகும்.",
    "Understand", "High", ["Special Majority", "Article 368", "Voting Threshold"]
)

# Q6 - Ans: A
add_p1(
    "polity_amendments_gt_006", "Medium", "statement",
    "Consider the following statements regarding state ratification of a Constitutional Amendment Bill:\n1. Ratification by state legislatures requires a simple majority of members present and voting in the state assembly.\n2. The Constitution specifies a strict 6-month time limit for state legislatures to ratify or reject an amendment bill.\nWhich of the statements given above is/are correct?",
    "அரசியலமைப்பு திருத்த மசோதாவிற்கான மாநிலங்களின் ஒப்புதல் குறித்த பின்வரும் கூற்றுகளை ஆராய்க:\n1. மாநில சட்டமன்றங்களின் ஒப்புதலுக்கு சட்டமன்றத்தில் வந்து வாக்களிக்கும் உறுப்பினர்களின் எளிய பெரும்பான்மை போதுமானது.\n2. மாநில சட்டமன்றங்கள் திருத்த மசோதாவை ஏற்க அல்லது நிராகரிக்க 6 மாத காலக்கெடுவை அரசியலமைப்பு தெளிவாக வரையறுத்துள்ளது.\nமேற்கூறிய கூற்றுகளில் எது/எவை சரியானது?",
    "1 only", "1 மட்டுமே",
    "2 only", "2 மட்டுமே",
    "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
    "Neither 1 nor 2", "1 அல்லது 2 இரண்டும் இல்லை",
    "A",
    "📚 Core Explanation:\nStatement 1 is CORRECT: State ratification requires a simple majority in state assemblies.\nStatement 2 is INCORRECT: The Constitution does NOT prescribe any time limit within which state legislatures must ratify or reject an amendment bill.",
    "📚 முதன்மை விளக்கம்:\nகூற்று 1 சரி: கூட்டாட்சி தொடர்பான திருத்த மசோதாக்களுக்கு மாநில சட்டமன்றங்களில் எளிய பெரும்பான்மையுடன் ஒப்புதல் அளிக்கப்பட வேண்டும்.\nகூற்று 2 தவறு: மாநில சட்டமன்றங்களுக்கு அரசியலமைப்பில் எந்தவொரு குறிப்பிட்ட காலக்கெடுவும் வரையறுக்கப்படவில்லை.",
    "Option A is correct because statement 1 is true and statement 2 is false.",
    "விருப்பம் A சரியானது.",
    "Option B is incorrect because statement 2 is false.",
    "விருப்பம் B தவறானது.",
    "Option C is incorrect because statement 2 is false.",
    "விருப்பம் C தவறானது.",
    "Option D is incorrect because statement 1 is true.",
    "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: Remember: Half of the states (14 out of 28 states) are required to ratify. States cannot initiate amendment bills.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: பாதியளவு மாநிலங்களின் (14/28) ஒப்புதல் தேவை. மாநிலங்களால் அரசியலமைப்பு திருத்த மசோதாவைத் தொடங்க முடியாது.",
    "📖 Revision Fact: Absence of a time limit for state ratification is a lacuna in Article 368.",
    "📖 திருத்தல் செய்தி: மாநில ஒப்புதலுக்கு காலக்கெடு இல்லாதது சரத்து 368-ன் குறைபாடாகும்.",
    "Understand", "High", ["State Ratification", "Time Limit Trap", "Simple Majority"]
)

# Q7 - Ans: B
add_p1(
    "polity_amendments_gt_007", "Easy", "single_choice",
    "Which of the following matters requires a Special Majority under Article 368 ALONG WITH Ratification by at least half of the State Legislatures?",
    "பின்வருவனவற்றில் எது சரத்து 368-ன் கீழ் சிறப்பு பெரும்பான்மையுடன் குறைந்தபட்சம் பாதியளவு மாநில சட்டமன்றங்களின் ஒப்புதலையும் கோருகிறது?",
    "Abolition or creation of Legislative Councils in States (Article 169)", "மாநிலங்களில் சட்ட மேலவைகளை ஒழித்தல் அல்லது உருவாக்குதல் (சரத்து 169)",
    "Representation of States in Parliament (4th Schedule)", "நாடாளுமன்றத்தில் மாநிலங்களின் பிரதிநிதித்துவம் (4-வது அட்டவணை)",
    "Conferment of more jurisdiction on the Supreme Court", "உச்சநீதிமன்றத்திற்கு கூடுதல் அதிகார வரம்பை வழங்குதல்",
    "Use of Official Language in Parliament", "நாடாளுமன்றத்தில் அலுவல் மொழியைப் பயன்படுத்துதல்",
    "B",
    "📚 Core Explanation:\nRepresentation of States in Parliament (4th Schedule) affects the federal structure. Hence, amending it requires a Special Majority in Parliament along with Ratification by at least half of the state legislatures.",
    "📚 முதன்மை விளக்கம்:\nநாடாளுமன்றத்தில் மாநிலங்களின் பிரதிநிதித்துவம் (4-வது அட்டவணை) கூட்டாட்சி அமைப்பைப் பாதிப்பதாகும். எனவே, இதை திருத்துவதற்கு நாடாளுமன்றத்தில் சிறப்பு பெரும்பான்மையும், பாதியளவு மாநில சட்டமன்றங்களின் ஒப்புதலும் தேவை.",
    "Option A is incorrect because Article 169 is amended by simple majority.",
    "விருப்பம் A தவறானது.",
    "Option B is correct because Representation of States in Parliament is a federal provision.",
    "விருப்பம் B சரியானது.",
    "Option C is incorrect because conferring extra jurisdiction on SC is done by simple majority.",
    "விருப்பம் C தவறானது.",
    "Option D is incorrect because official language rules are amended by simple majority.",
    "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: Federal matters requiring state ratification include: Election of President, SC & HCs, 7th Schedule, 4th Schedule, Art 368.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: மாநில ஒப்புதல் தேவைப்படும் கூட்டாட்சி விஷயங்கள்: குடியரசுத் தலைவர் தேர்தல், SC & HC, 7-வது அட்டவணை, 4-வது அட்டவணை, சரத்து 368.",
    "📖 Revision Fact: Amending Article 368 itself requires ratification by state legislatures.",
    "📖 திருத்தல் செய்தி: சரத்து 368-ஐத் திருத்துவதற்கே மாநிலங்களின் ஒப்புதல் தேவைப்படுகிறது.",
    "Understand", "High", ["Federal Structure", "State Ratification", "4th Schedule"]
)

# Q8 - Ans: B
add_p1(
    "polity_amendments_gt_008", "Medium", "statement",
    "Consider the following provisions of the Indian Constitution:\n1. Admission or establishment of new States (Article 2)\n2. Fundamental Rights (Part III)\n3. Directive Principles of State Policy (Part IV)\nWhich of the above provisions CANNOT be amended by a simple majority of Parliament?",
    "இந்திய அரசியலமைப்பின் பின்வரும் விதிகளைக் கருதுக:\n1. புதிய மாநிலங்களைச் சேர்ப்பது அல்லது உருவாக்குவது (சரத்து 2)\n2. அடிப்படை உரிமைகள் (பகுதி III)\n3. அரசு நெறிமுறையுறுத்தும் கோட்பாடுகள் (பகுதி IV)\nமேற்கண்டவற்றில் எவற்றை நாடாளுமன்றத்தின் எளிய பெரும்பான்மையால் திருத்த முடியாது?",
    "1 only", "1 மட்டுமே",
    "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
    "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "B",
    "📚 Core Explanation:\n- Article 2 is amended by SIMPLE MAJORITY outside Article 368.\n- Fundamental Rights (Part III) and DPSPs (Part IV) require a SPECIAL MAJORITY under Article 368. They CANNOT be amended by simple majority.",
    "📚 முதன்மை விளக்கம்:\n- சரத்து 2 எளிய பெரும்பான்மையால் திருத்தப்படுகிறது.\n- அடிப்படை உரிமைகள் (பகுதி III) மற்றும் DPSP (பகுதி IV) ஆகியவை சரத்து 368-ன் கீழ் சிறப்பு பெரும்பான்மையால் மட்டுமே திருத்தப்பட முடியும்.",
    "Option A is incorrect because 1 CAN be amended by simple majority.",
    "விருப்பம் A தவறானது.",
    "Option B is correct because 2 and 3 CANNOT be amended by simple majority.",
    "விருப்பம் B சரியானது.",
    "Option C is incorrect because 1 is amended by simple majority.",
    "விருப்பம் C தவறானது.",
    "Option D is incorrect because 1 can be amended by simple majority.",
    "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: Amendments under Articles 2, 3, 4, 169 are NOT amendments under Article 368.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: சரத்து 2, 3, 4, 169 ஆகியவை சரத்து 368-ன் கீழ் திருத்தங்களாகக் கருதப்பட மாட்டா.",
    "📖 Revision Fact: Fundamental Rights and DPSP are amended by Special Majority of Parliament alone.",
    "📖 திருத்தல் செய்தி: அடிப்படை உரிமைகள் மற்றும் DPSP நாடாளுமன்றத்தின் சிறப்பு பெரும்பான்மையால் திருத்தப்படுகின்றன.",
    "Understand", "High", ["Simple Majority", "Special Majority", "Article 2"]
)

# Q9 - Ans: C
add_p1(
    "polity_amendments_gt_009", "Easy", "single_choice",
    "Which Constitutional Amendment Act added the 10th Schedule to the Indian Constitution, establishing the Anti-Defection Law?",
    "கட்சித் தாவல் தடைச் சட்டத்தை நிறுவி, இந்திய அரசியலமைப்பில் 10-வது அட்டவணையைச் சேர்த்த அரசியலமைப்பு திருத்தச் சட்டம் எது?",
    "42nd Constitutional Amendment Act, 1976", "42-வது அரசியலமைப்பு திருத்தச் சட்டம், 1976",
    "44th Constitutional Amendment Act, 1978", "44-வது அரசியலமைப்பு திருத்தச் சட்டம், 1978",
    "52nd Constitutional Amendment Act, 1985", "52-வது அரசியலமைப்பு திருத்தச் சட்டம், 1985",
    "61st Constitutional Amendment Act, 1988", "61-வது அரசியலமைப்பு திருத்தச் சட்டம், 1988",
    "C",
    "📚 Core Explanation:\nThe 52nd Constitutional Amendment Act, 1985 introduced the 10th Schedule to disqualify MPs and MLAs on grounds of defection (Anti-Defection Law).",
    "📚 முதன்மை விளக்கம்:\n1985-ஆம் ஆண்டின் 52-வது அரசியலமைப்பு திருத்தச் சட்டம் கட்சித் தாவல் காரணமாக எம்பி மற்றும் எம்எல்ஏக்களை தகுதிநீக்கம் செய்ய 10-வது அட்டவணையை (கட்சித் தாவல் தடைச் சட்டம்) அறிமுகப்படுத்தியது.",
    "Option A is incorrect; 42nd Amendment is Mini-Constitution.",
    "விருப்பம் A தவறானது.",
    "Option B is incorrect; 44th Amendment reversed emergency provisions.",
    "விருப்பம் B தவறானது.",
    "Option C is correct as 52nd Amendment introduced 10th Schedule.",
    "விருப்பம் C சரியானது.",
    "Option D is incorrect; 61st Amendment lowered voting age to 18.",
    "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: Anti-Defection Law was later modified by 91st Amendment Act 2003.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: கட்சித் தாவல் தடைச் சட்டம் பின்னர் 91-வது திருத்தச் சட்டத்தால் மாற்றியமைக்கப்பட்டது.",
    "📖 Revision Fact: 52nd Amendment came into effect on 1st March 1985.",
    "📖 திருத்தல் செய்தி: 52-வது திருத்தம் மார்ச் 1, 1985 அன்று அமலுக்கு வந்தது.",
    "Remember", "High", ["52nd Amendment", "10th Schedule", "Anti-Defection"]
)

# Q10 - Ans: B
add_p1(
    "polity_amendments_gt_010", "Easy", "single_choice",
    "By which Constitutional Amendment Act was the voting age reduced from 21 years to 18 years for Lok Sabha and State Legislative Assembly elections?",
    "எந்த அரசியலமைப்பு திருத்தச் சட்டத்தின் மூலம் மக்களவை மற்றும் மாநில சட்டப்பேரவை தேர்தல்களுக்கான வாக்குரிமை வயது 21 லிருந்து 18 ஆகக் குறைக்கப்பட்டது?",
    "44th Constitutional Amendment Act, 1978", "44-வது அரசியலமைப்பு திருத்தச் சட்டம், 1978",
    "61st Constitutional Amendment Act, 1988", "61-வது அரசியலமைப்பு திருத்தச் சட்டம், 1988",
    "69th Constitutional Amendment Act, 1991", "69-வது அரசியலமைப்பு திருத்தச் சட்டம், 1991",
    "73rd Constitutional Amendment Act, 1992", "73-வது அரசியலமைப்பு திருத்தச் சட்டம், 1992",
    "B",
    "📚 Core Explanation:\nThe 61st Constitutional Amendment Act, 1988 amended Article 326 of the Constitution to lower the voting age from 21 years to 18 years.",
    "📚 முதன்மை விளக்கம்:\n1988-ஆம் ஆண்டின் 61-வது அரசியலமைப்பு திருத்தச் சட்டம் வாக்குரிமை வயதை 21-லிருந்து 18 ஆகக் குறைக்க சரத்து 326-ஐத் திருத்தியது.",
    "Option A is incorrect; 44th Amendment restored civil rights.",
    "விருப்பம் A தவறானது.",
    "Option B is correct as 61st Amendment lowered voting age to 18.",
    "விருப்பம் B சரியானது.",
    "Option C is incorrect; 69th Amendment granted special status to Delhi.",
    "விருப்பம் C தவறானது.",
    "Option D is incorrect; 73rd Amendment constitutionalized Panchayati Raj.",
    "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: Article 326 deals with Adult Suffrage. PM was Rajiv Gandhi.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: சரத்து 326 வயதுவந்தோர் வாக்குரிமையைக் கையாள்கிறது.",
    "📖 Revision Fact: 61st Amendment came into force on March 28, 1989.",
    "📖 திருத்தல் செய்தி: 61-வது திருத்தம் மார்ச் 28, 1989 அன்று அமலுக்கு வந்தது.",
    "Remember", "High", ["61st Amendment", "Voting Age", "Article 326"]
)

# Q11 - Ans: A
add_p1(
    "polity_amendments_gt_011", "Medium", "match_the_following",
    "Match List-I (Constitutional Amendment Act) with List-II (Key Provision) and select the correct code:\nList-I:\nA. 1st Amendment Act, 1951\nB. 7th Amendment Act, 1956\nC. 36th Amendment Act, 1975\nD. 69th Amendment Act, 1991\nList-II:\n1. Sikkim made a full-fledged State of India\n2. Special status to Union Territory of Delhi\n3. Added Ninth Schedule to protect land reform laws\n4. Reorganisation of States on linguistic basis",
    "பட்டியல்-I (அரசியலமைப்பு திருத்தச் சட்டம்) பட்டியல்-II (முக்கிய விதி) உடன் பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்க:\nபட்டியல்-I:\nA. 1-வது திருத்தச் சட்டம், 1951\nB. 7-வது திருத்தச் சட்டம், 1956\nC. 36-வது திருத்தச் சட்டம், 1975\nD. 69-வது திருத்தச் சட்டம், 1991\nபட்டியல்-II:\n1. சிக்கிம் இந்தியாவின் முழுமையான மாநிலமாகாக்கப்பட்டது\n2. தில்லி ஒன்றிய பிரதேசத்திற்கு சிறப்பு அந்தஸ்து\n3. நிலசீர்திருத்த சட்டங்களைப் பாதுகாக்க 9-வது அட்டவணை சேர்க்கப்பட்டது\n4. மொழிவாரியாக மாநிலங்கள் மறுசீரமைப்பு",
    "A-3, B-4, C-1, D-2", "A-3, B-4, C-1, D-2",
    "A-4, B-3, C-2, D-1", "A-4, B-3, C-2, D-1",
    "A-3, B-1, C-4, D-2", "A-3, B-1, C-4, D-2",
    "A-1, B-4, C-3, D-2", "A-1, B-4, C-3, D-2",
    "A",
    "📚 Core Explanation:\n- 1st Amendment Act (1951) added 9th Schedule (A-3).\n- 7th Amendment Act (1956) implemented State Reorganisation (B-4).\n- 36th Amendment Act (1975) made Sikkim 22nd state (C-1).\n- 69th Amendment Act (1991) granted special status to Delhi (D-2).",
    "📚 முதன்மை விளக்கம்:\n- 1-வது திருத்தம் (1951) 9-வது அட்டவணை (A-3).\n- 7-வது திருத்தம் (1956) மாநில மறுசீரமைப்பு (B-4).\n- 36-வது திருத்தம் (1975) சிக்கிம் முழு மாநிலம் (C-1).\n- 69-வது திருத்தம் (1991) தில்லி சிறப்பு அந்தஸ்து (D-2).",
    "Option A is correct as all matches correspond accurately.",
    "விருப்பம் A சரியானது.",
    "Option B is incorrect.", "விருப்பம் B தவறானது.",
    "Option C is incorrect.", "விருப்பம் C தவறானது.",
    "Option D is incorrect.", "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: 1st Amendment = 9th Schedule, 7th = Reorganisation, 36th = Sikkim, 69th = Delhi NCT.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: 1-வது = 9-வது அட்டவணை, 7-வது = மறுசீரமைப்பு, 36-வது = சிக்கிம், 69-வது = தில்லி.",
    "📖 Revision Fact: 35th Amendment made Sikkim an Associate State; 36th made it a full state.",
    "📖 திருத்தல் செய்தி: 35-வது திருத்தம் இணை மாநிலம்; 36-வது திருத்தம் முழு மாநிலம்.",
    "Understand", "High", ["Match the Following", "1st Amendment", "7th Amendment", "36th Amendment"]
)

# Q12 - Ans: C
add_p1(
    "polity_amendments_gt_012", "Hard", "reasoning",
    "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): The Supreme Court in Kesavananda Bharati Case (1973) held that Parliament cannot alter or destroy the 'Basic Structure' of the Constitution.\nReason (R): Article 368 grants absolute, unrestricted, and unlimited constituent power to Parliament to amend any part of the Constitution without judicial scrutiny.\nIn light of the above statements, choose the correct option:",
    "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன. ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிக்கப்பட்டுள்ளது:\nகூற்று (A): கேசவாநந்த பாரதி வழக்கில் (1973) அரசியலமைப்பின் 'அடிப்படை கட்டமைப்பை' நாடாளுமன்றம் மாற்றவோ அழிக்கவோ முடியாது என்று உச்சநீதிமன்றம் தீர்ப்பளித்தது.\nகாரணம் (R): நீதிமன்ற ஆய்வின்றி அரசியலமைப்பின் எந்தப் பகுதியையும் திருத்துவதற்கு நாடாளுமன்றத்திற்கு சரத்து 368 வரம்பற்ற அரசியலமைப்பு ஆக்கல் அதிகாரத்தை வழங்குகிறது.\nமேற்கண்ட கூற்றுகளின் அடிப்படையில் சரியான விருப்பத்தைத் தேர்ந்தெடுக்கவும்:",
    "Both (A) and (R) are true and (R) is the correct explanation of (A)", "(A) மற்றும் (R) இரண்டும் உண்மை மற்றும் (R) என்பது (A)-வின் சரியான விளக்கமாகும்",
    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)", "(A) மற்றும் (R) இரண்டும் உண்மை ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல",
    "(A) is true but (R) is false", "(A) உண்மை ஆனால் (R) தவறு",
    "(A) is false but (R) is true", "(A) தவறு ஆனால் (R) உண்மை",
    "C",
    "📚 Core Explanation:\nAssertion (A) is TRUE: Kesavananda Bharati (1973) formulated Basic Structure doctrine.\nReason (R) is FALSE: Parliament does NOT have absolute power; amending power is limited by judicial review and basic structure.",
    "📚 முதன்மை விளக்கம்:\nகூற்று (A) உண்மை: கேசவாநந்த பாரதி வழக்கில் அடிப்படை கட்டமைப்பு கோட்பாடு உருவாக்கப்பட்டது.\nகாரணம் (R) தவறு: நாடாளுமன்றத்திற்கு வரம்பற்ற அதிகாரம் இல்லை.",
    "Option A is incorrect because R is false.", "விருப்பம் A தவறானது.",
    "Option B is incorrect because R is false.", "விருப்பம் B தவறானது.",
    "Option C is correct because A is true and R is false.", "விருப்பம் C சரியானது.",
    "Option D is incorrect because A is true.", "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: In Minerva Mills case (1980), SC ruled that limited amending power itself is a basic feature.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: மினெர்வா மில்ஸ் வழக்கில் வரம்பிற்குட்பட்ட திருத்தும் அதிகாரமே அடிப்படை அம்சம் என தீர்ப்பளிக்கப்பட்டது.",
    "📖 Revision Fact: 42nd Amendment added Art 368(4)&(5) claiming unlimited power, struck down in 1980.",
    "📖 திருத்தல் செய்தி: 42-வது திருத்தம் சேர்த்த சரத்து 368(4),(5) 1980-ல் ரத்து செய்யப்பட்டது.",
    "Analyze", "High", ["Kesavananda Bharati", "Basic Structure", "Minerva Mills"]
)

# Q13 - Ans: A
add_p1(
    "polity_amendments_gt_013", "Medium", "chronology",
    "Arrange the following landmark Supreme Court judgments regarding Constitutional Amending Power in correct chronological order:\n1. Golaknath v. State of Punjab\n2. Shankari Prasad v. Union of India\n3. Kesavananda Bharati v. State of Kerala\n4. Minerva Mills v. Union of India\nSelect the correct code:",
    "அரசியலமைப்பு திருத்தும் அதிகாரம் தொடர்பான பின்வரும் உச்சநீதிமன்றத்தின் முக்கிய தீர்ப்புகளை சரியான காலவரிசைப்படி அமைக்கவும்:\n1. கோலக்நாத் எதிர் பஞ்சாப் மாநிலம்\n2. சங்கரி பிரசாத் எதிர் இந்திய ஒன்றியம்\n3. கேசவாநந்த பாரதி எதிர் கேரள மாநிலம்\n4. மினெர்வா மில்ஸ் எதிர் இந்திய ஒன்றியம்\nசரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
    "2 - 1 - 3 - 4", "2 - 1 - 3 - 4",
    "1 - 2 - 3 - 4", "1 - 2 - 3 - 4",
    "2 - 3 - 1 - 4", "2 - 3 - 1 - 4",
    "3 - 2 - 1 - 4", "3 - 2 - 1 - 4",
    "A",
    "📚 Core Explanation:\n1. Shankari Prasad (1951)\n2. Golaknath (1967)\n3. Kesavananda Bharati (1973)\n4. Minerva Mills (1980)\nHence, correct order is 2 - 1 - 3 - 4.",
    "📚 முதன்மை விளக்கம்:\n1. சங்கரி பிரசாத் (1951)\n2. கோலக்நாத் (1967)\n3. கேசவாநந்த பாரதி (1973)\n4. மினெர்வா மில்ஸ் (1980)\nசரியான வரிசை 2 - 1 - 3 - 4.",
    "Option A is correct as 2 (1951) -> 1 (1967) -> 3 (1973) -> 4 (1980).",
    "விருப்பம் A சரியானது.",
    "Option B is incorrect.", "விருப்பம் B தவறானது.",
    "Option C is incorrect.", "விருப்பம் C தவறானது.",
    "Option D is incorrect.", "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: Timeline: Shankari Prasad (1951) -> Golaknath (1967) -> Kesavananda (1973) -> Minerva Mills (1980).",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: சங்கரி பிரசாத் (1951) -> கோலக்நாத் (1967) -> கேசவாநந்தா (1973) -> மினெர்வா மில்ஸ் (1980).",
    "📖 Revision Fact: Kesavananda Bharati (1973) was a 13-judge bench (largest ever).",
    "📖 திருத்தல் செய்தி: கேசவாநந்த பாரதி 13 நீதிபதிகள் அமர்வு.",
    "Apply", "High", ["Chronology", "Landmark Cases", "Judicial Review"]
)

# Q14 - Ans: B
add_p1(
    "polity_amendments_gt_014", "Medium", "single_choice",
    "Which Constitutional Amendment Act is known as the 'Mini-Constitution' because of the comprehensive and overarching changes it introduced in 1976?",
    "1976-இல் கொண்டுவரப்பட்ட விரிவான மாற்றங்கள் காரணமாக 'சிறிய அரசியலமைப்பு' (Mini-Constitution) என்று அழைக்கப்படும் அரசியலமைப்பு திருத்தச் சட்டம் எது?",
    "24th Constitutional Amendment Act, 1971", "24-வது அரசியலமைப்பு திருத்தச் சட்டம், 1971",
    "42nd Constitutional Amendment Act, 1976", "42-வது அரசியலமைப்பு திருத்தச் சட்டம், 1976",
    "44th Constitutional Amendment Act, 1978", "44-வது அரசியலமைப்பு திருத்தச் சட்டம், 1978",
    "73rd Constitutional Amendment Act, 1992", "73-வது அரசியலமைப்பு திருத்தச் சட்டம், 1992",
    "B",
    "📚 Core Explanation:\nThe 42nd Constitutional Amendment Act, 1976, enacted during Emergency, is popularly known as the 'Mini-Constitution' due to its comprehensive changes.",
    "📚 முதன்மை விளக்கம்:\n1976-ஆம் ஆண்டின் 42-வது அரசியலமைப்பு திருத்தச் சட்டம் 'சிறிய அரசியலமைப்பு' என்று அழைக்கப்படுகிறது.",
    "Option A is incorrect.", "விருப்பம் A தவறானது.",
    "Option B is correct; 42nd Amendment is called Mini-Constitution.", "விருப்பம் B சரியானது.",
    "Option C is incorrect.", "விருப்பம் C தவறானது.",
    "Option D is incorrect.", "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: 42nd Amendment was based on Swaran Singh Committee recommendations.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: 42-வது திருத்தம் ஸ்வரன் சிங் குழுவின் பரிந்துரைகளின் அடிப்படையிலானது.",
    "📖 Revision Fact: Words 'Socialist', 'Secular', 'Integrity' inserted into Preamble by 42nd Amendment.",
    "📖 திருத்தல் செய்தி: 'சமதர்ம', 'சமயச்சார்பற்ற', 'ஒருமைப்பாடு' வார்த்தைகள் 42-வது திருத்தத்தால் சேர்க்கப்பட்டன.",
    "Remember", "High", ["42nd Amendment", "Mini Constitution", "Swaran Singh Committee"]
)

# Q15 - Ans: D
add_p1(
    "polity_amendments_gt_015", "Hard", "statement",
    "Consider the following statements regarding the 44th Constitutional Amendment Act, 1978:\n1. It deleted the Right to Property from Part III (Fundamental Rights) and made it a legal right under Article 300A.\n2. It provided that Fundamental Rights under Articles 20 and 21 cannot be suspended even during a National Emergency.\n3. It replaced the phrase 'internal disturbance' with 'armed rebellion' for declaring National Emergency under Article 352.\nWhich of the statements given above are correct?",
    "1978-ஆம் ஆண்டின் 44-வது அரசியலமைப்பு திருத்தச் சட்டம் குறித்த பின்வரும் கூற்றுகளை ஆராய்க:\n1. இது சொத்துரிமையை பகுதி III-லிருந்து நீக்கி, சரத்து 300A-ன் கீழ் ஒரு சட்டப்பூர்வ உரிமையாக ஆக்கியது.\n2. சரத்து 20 மற்றும் 21-ன் கீழ் உள்ள அடிப்படை உரிமைகளை தேசிய அவசரநிலையின் போதும் இடைநீக்கம் செய்ய முடியாது என்று இது வகைசெய்தது.\n3. சரத்து 352-ன் கீழ் தேசிய அவசரநிலையை அறிவிப்பதற்காக 'உள்நாட்டு அமைதியின்மை' என்பதற்குப் பதிலாக 'ஆயுதமேந்திய கிளர்ச்சி' என மாற்றியது.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?",
    "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
    "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
    "1 and 3 only", "1 மற்றும் 3 மட்டுமே",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "D",
    "📚 Core Explanation:\nAll three statements are CORRECT regarding the 44th Constitutional Amendment Act, 1978 (Morarji Desai Janata Party Government).",
    "📚 முதன்மை விளக்கம்:\n1978-ஆம் ஆண்டின் 44-வது அரசியலமைப்பு திருத்தச் சட்டம் தொடர்பான மூன்று கூற்றுகளும் சரியானவை.",
    "Option A is incomplete.", "விருப்பம் A அரைகுறையானது.",
    "Option B is incomplete.", "விருப்பம் B அரைகுறையானது.",
    "Option C is incomplete.", "விருப்பம் C அரைகுறையானது.",
    "Option D is correct as statements 1, 2, and 3 are all true.", "விருப்பம் D சரியானது.",
    "💡 TNPSC Tip: 44th Amendment empowered President to return Cabinet advice ONCE for reconsideration.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: 44-வது திருத்தம் அமைச்சரவை ஆலோசனையை ஒருமுறை திரும்ப்பியனுப்ப அதிகாரம் அளித்தது.",
    "📖 Revision Fact: Right to Property was originally under Art 19(1)(f) and Art 31.",
    "📖 திருத்தல் செய்தி: சொத்துரிமை முதலில் சரத்து 19(1)(f) மற்றும் 31-ல் இருந்தது.",
    "Analyze", "High", ["44th Amendment", "Right to Property", "Articles 20 and 21"]
)

# Q16 - Ans: C
add_p1(
    "polity_amendments_gt_016", "Medium", "single_choice",
    "By which Constitutional Amendment Act was the size of the Council of Ministers (including the Prime Minister/Chief Minister) limited to 15% of the total strength of the Lok Sabha / State Legislative Assembly?",
    "எந்த அரசியலமைப்பு திருத்தச் சட்டத்தின் மூலம் பிரதமர்/முதலமைச்சர் உட்பட அமைச்சரவையின் அளவு மக்களவை/மாநில சட்டமன்றத்தின் மொத்த எண்ணிக்கையில் 15% ஆக வரம்பிடப்பட்டது?",
    "86th Constitutional Amendment Act, 2002", "86-வது அரசியலமைப்பு திருத்தச் சட்டம், 2002",
    "89th Constitutional Amendment Act, 2003", "89-வது அரசியலமைப்பு திருத்தச் சட்டம், 2003",
    "91st Constitutional Amendment Act, 2003", "91-வது அரசியலமைப்பு திருத்தச் சட்டம், 2003",
    "97th Constitutional Amendment Act, 2011", "97-வது அரசியலமைப்பு திருத்தச் சட்டம், 2011",
    "C",
    "📚 Core Explanation:\nThe 91st Constitutional Amendment Act, 2003 limited the total number of ministers, including PM/CM, in the Council of Ministers to 15% of Lok Sabha/Assembly strength.",
    "📚 முதன்மை விளக்கம்:\n2003-ஆம் ஆண்டின் 91-வது அரசியலமைப்பு திருத்தச் சட்டம் அமைச்சரவை அளவை 15% ஆக வரம்பிட்டது.",
    "Option A is incorrect; 86th Amendment introduced Right to Education.",
    "விருப்பம் A தவறானது.",
    "Option B is incorrect; 89th Amendment bifurcated NCST from NCSC.",
    "விருப்பம் B தவறானது.",
    "Option C is correct as 91st Amendment capped Council of Ministers at 15%.",
    "விருப்பம் C சரியானது.",
    "Option D is incorrect; 97th Amendment dealt with Co-operative Societies.",
    "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: 91st Amendment also required at least 2/3rd members for a valid merger under 10th Schedule.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: 91-வது திருத்தம் 2/3 இணைப்பு விதியைக் கொண்டுவந்தது.",
    "📖 Revision Fact: Minimum ministers threshold in Small States is 12 (including CM).",
    "📖 திருத்தல் செய்தி: சிறிய மாநிலங்களில் குறைந்தபட்ச அமைச்சர்கள் எண்ணிக்கை 12.",
    "Remember", "High", ["91st Amendment", "Council of Ministers", "15 Percent Cap"]
)

# Q17 - Ans: D
add_p1(
    "polity_amendments_gt_017", "Easy", "single_choice",
    "Which Constitutional Amendment Act inserted Article 21A into the Constitution, making free and compulsory education for children aged 6 to 14 years a Fundamental Right?",
    "6 முதல் 14 வயது வரையிலான குழந்தைகளுக்கு இலவச மற்றும் கட்டாயக் கல்வியை அடிப்படை உரிமையாக்கும் சரத்து 21A-ஐ எந்த அரசியலமைப்பு திருத்தச் சட்டம் சேர்த்தது?",
    "73rd Constitutional Amendment Act, 1992", "73-வது அரசியலமைப்பு திருத்தச் சட்டம், 1992",
    "91st Constitutional Amendment Act, 2003", "91-வது அரசியலமைப்பு திருத்தச் சட்டம், 2003",
    "103rd Constitutional Amendment Act, 2019", "103-வது அரசியலமைப்பு திருத்தச் சட்டம், 2019",
    "86th Constitutional Amendment Act, 2002", "86-வது அரசியலமைப்பு திருத்தச் சட்டம், 2002",
    "D",
    "📚 Core Explanation:\nThe 86th Constitutional Amendment Act, 2002 introduced Article 21A in Part III (Fundamental Rights) providing free and compulsory education for children aged 6 to 14.",
    "📚 முதன்மை விளக்கம்:\n2002-ன் 86-வது அரசியலமைப்பு திருத்தச் சட்டம் பகுதி III-ல் சரத்து 21A-ஐச் சேர்த்து 6-14 வயதுக் குழந்தைகளுக்கு இலவச கட்டாயக் கல்வியை அடிப்படை உரிமையாக்கியது.",
    "Option A is incorrect.", "விருப்பம் A தவறானது.",
    "Option B is incorrect.", "விருப்பம் B தவறானது.",
    "Option C is incorrect.", "விருப்பம் C தவறானது.",
    "Option D is correct; 86th Amendment introduced Right to Education (Art 21A).", "விருப்பம் D சரியானது.",
    "💡 TNPSC Tip: 86th Amendment made changes in Part III (21A), Part IV (45), and Part IVA (51A(k)).",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: 86-வது திருத்தம் பகுதி III, பகுதி IV, பகுதி IVA ஆகியவற்றில் மாற்றங்களைச் செய்தது.",
    "📖 Revision Fact: Right to Education (RTE) Act was passed in 2009 and implemented in April 2010.",
    "📖 திருத்தல் செய்தி: இலவச கட்டாயக் கல்வி உரிமைச் சட்டம் 2009-ல் இயற்றப்பட்டது.",
    "Remember", "High", ["86th Amendment", "Article 21A", "Right to Education"]
)

# Q18 - Ans: D
add_p1(
    "polity_amendments_gt_018", "Medium", "single_choice",
    "The 101st Constitutional Amendment Act, 2016 is landmark in Indian public finance because it introduced which of the following?",
    "இந்தியப் பொது நிதியில் 2016-ஆம் ஆண்டின் 101-வது அரசியலமைப்பு திருத்தச் சட்டம் முக்கிய மைல்கல்லாகக் கருதப்படுகிறது, ஏனெனில் அது எதை அறிமுகப்படுத்தியது?",
    "National Judicial Appointments Commission (NJAC)", "தேசிய நீதிபதிகள் நியமன ஆணையம் (NJAC)",
    "10% Reservation for Economically Weaker Sections (EWS)", "பொருளாதாரத்தில் நலிவடைந்த பிரிவினருக்கு (EWS) 10% இடஒதுக்கீடு",
    "Constitutional Status to National Commission for Backward Classes", "தேசிய பிற்படுத்தப்பட்டோர் ஆணையத்திற்கு அரசியலமைப்பு அந்தஸ்து",
    "Goods and Services Tax (GST) Regime", "சரக்கு மற்றும் சேவை வரி (GST) முறை",
    "D",
    "📚 Core Explanation:\nThe 101st Constitutional Amendment Act, 2016 introduced Goods and Services Tax (GST). Inserted Art 246A, Art 269A, Art 279A (GST Council).",
    "📚 முதன்மை விளக்கம்:\n2016-ஆம் ஆண்டின் 101-வது அரசியலமைப்பு திருத்தச் சட்டம் சரக்கு மற்றும் சேவை வரி (GST) முறையை அறிமுகப்படுத்தியது.",
    "Option A is incorrect.", "விருப்பம் A தவறானது.",
    "Option B is incorrect.", "விருப்பம் B தவறானது.",
    "Option C is incorrect.", "விருப்பம் C தவறானது.",
    "Option D is correct; 101st Amendment introduced GST.", "விருப்பம் D சரியானது.",
    "💡 TNPSC Tip: GST came into effect on July 1, 2017. GST Council is under Art 279A.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: ஜிஎஸ்டி ஜூலை 1, 2017 முதல் அமலுக்கு வந்தது.",
    "📖 Revision Fact: 101st Amendment required state ratification as it affected 7th Schedule tax powers.",
    "📖 திருத்தல் செய்தி: 101-வது திருத்தத்திற்கு மாநிலங்களின் ஒப்புதல் தேவைப்பட்டது.",
    "Remember", "High", ["101st Amendment", "GST", "Article 279A"]
)

# Q19 - Ans: D
add_p1(
    "polity_amendments_gt_019", "Hard", "statement",
    "Consider the following statements regarding recent Constitutional Amendment Acts:\n1. The 103rd Amendment Act, 2019 inserted Articles 15(6) and 16(6) to provide up to 10% reservation for Economically Weaker Sections (EWS).\n2. The 104th Amendment Act, 2020 extended SC/ST reservation in Lok Sabha and Assemblies by 10 years and discontinued Anglo-Indian nomination.\n3. The 105th Amendment Act, 2021 restored the power of State Governments to identify and specify their own Socially and Educationally Backward Classes (SEBCs).\nWhich of the statements given above are correct?",
    "அண்மைய அரசியலமைப்பு திருத்தச் சட்டங்கள் குறித்த பின்வரும் கூற்றுகளை ஆராய்க:\n1. 103-வது திருத்தச் சட்டம் 2019, EWS பிரிவினருக்கு 10% வரை இடஒதுக்கீடு வழங்க சரத்து 15(6) மற்றும் 16(6)-ஐச் சேர்த்தது.\n2. 104-வது திருத்தச் சட்டம் 2020, SC/ST இடஒதுக்கீட்டை 10 ஆண்டுகள் நீட்டித்ததுடன் ஆங்கிலோ-இந்தியர் நியமனத்தை நிறுத்தியது.\n3. 105-வது திருத்தச் சட்டம் 2021, SEBC வகுப்பினரை அடையாளம் காணும் மாநில அரசுகளின் அதிகாரத்தை மீட்டெடுத்தது.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?",
    "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
    "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
    "1 and 3 only", "1 மற்றும் 3 மட்டுமே",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "D",
    "📚 Core Explanation:\nAll three statements are CORRECT regarding 103rd, 104th, and 105th Constitutional Amendments.",
    "📚 முதன்மை விளக்கம்:\nமூன்று கூற்றுகளும் சரியானவை: 103-வது (EWS), 104-வது (SC/ST நீட்டிப்பு), 105-வது (மாநில OBC பட்டியல் மீட்பு).",
    "Option A is incomplete.", "விருப்பம் A அரைகுறையானது.",
    "Option B is incomplete.", "விருப்பம் B அரைகுறையானது.",
    "Option C is incomplete.", "விருப்பம் C அரைகுறையானது.",
    "Option D is correct as all statements are true.", "விருப்பம் D சரியானது.",
    "💡 TNPSC Tip: 103rd = EWS, 104th = SC/ST extension + Anglo-Indian removal, 105th = State OBC list restoration, 106th = Women's reservation.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: 103-வது = EWS, 104-வது = SC/ST நீட்டிப்பு, 105-வது = மாநில OBC பட்டியல், 106-வது = மகளிர் இடஒதுக்கீடு.",
    "📖 Revision Fact: 106th Amendment Act, 2023 provides 33% reservation for women.",
    "📖 திருத்தல் செய்தி: 106-வது திருத்தச் சட்டம் மகளிருக்கு 33% இடஒதுக்கீடு வழங்குகிறது.",
    "Analyze", "High", ["103rd Amendment", "104th Amendment", "105th Amendment"]
)

# Q20 - Ans: A
add_p1(
    "polity_amendments_gt_020", "Medium", "single_choice",
    "Which landmark Supreme Court judgment declared the 99th Constitutional Amendment Act, 2014 and the National Judicial Appointments Commission (NJAC) Act unconstitutional?",
    "99-வது அரசியலமைப்பு திருத்தச் சட்டம் 2014 மற்றும் தேசிய நீதிபதிகள் நியமன ஆணைய (NJAC) சட்டத்தை அரசியலமைப்பிற்கு எதிரானது என அறிவித்த உச்சநீதிமன்றத்தின் வரலாற்றுச் சிறப்புமிக்க தீர்ப்பு எது?",
    "Fourth Judges Case (Supreme Court Advocates-on-Record Association v. Union of India, 2015)", "நான்காவது நீதிபதிகள் வழக்கு (2015)",
    "Third Judges Case (Re Special Reference, 1998)", "மூன்றாவது நீதிபதிகள் வழக்கு (1998)",
    "Minerva Mills v. Union of India (1980)", "மினெர்வா மில்ஸ் எதிர் இந்திய ஒன்றியம் (1980)",
    "S.R. Bommai v. Union of India (1994)", "எஸ்.ஆர். பொம்மை எதிர் இந்திய ஒன்றியம் (1994)",
    "A",
    "📚 Core Explanation:\nIn the Fourth Judges Case (2015), a 5-judge Constitution bench struck down the 99th Constitutional Amendment Act, 2014 and NJAC Act.",
    "📚 முதன்மை விளக்கம்:\nநான்காவது நீதிபதிகள் வழக்கில் (2015) 99-வது திருத்தச் சட்டம் மற்றும் NJAC சட்டம் ரத்து செய்யப்பட்டது.",
    "Option A is correct as 4th Judges Case struck down 99th Amendment & NJAC.", "விருப்பம் A சரியானது.",
    "Option B is incorrect.", "விருப்பம் B தவறானது.",
    "Option C is incorrect.", "விருப்பம் C தவறானது.",
    "Option D is incorrect.", "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: 99th Amendment is the ONLY amendment in Indian history completely struck down in its entirety.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: இந்திய வரலாற்றில் முழுமையாக ரத்து செய்யப்பட்ட ஒரே திருத்தம் 99-வது திருத்தம்.",
    "📖 Revision Fact: Collegium system was restored following NJAC invalidation.",
    "📖 திருத்தல் செய்தி: கொலீஜியம் முறை மீண்டும் அமலுக்கு வந்தது.",
    "Understand", "High", ["99th Amendment", "NJAC", "Fourth Judges Case"]
)

# Q21 - Ans: A
add_p1(
    "polity_amendments_gt_021", "Easy", "single_choice",
    "Which Constitutional Amendment Act incorporated Dadra and Nagar Haveli as a Union Territory of India?",
    "தாத்ரா மற்றும் நகர் ஹவேலியை இந்தியாவின் ஒன்றிய பிரதேசமாக இணைத்த அரசியலமைப்பு திருத்தச் சட்டம் எது?",
    "10th Constitutional Amendment Act, 1961", "10-வது அரசியலமைப்பு திருத்தச் சட்டம், 1961",
    "12th Constitutional Amendment Act, 1962", "12-வது அரசியலமைப்பு திருத்தச் சட்டம், 1962",
    "14th Constitutional Amendment Act, 1962", "14-வது அரசியலமைப்பு திருத்தச் சட்டம், 1962",
    "21st Constitutional Amendment Act, 1967", "21-வது அரசியலமைப்பு திருத்தச் சட்டம், 1967",
    "A",
    "📚 Core Explanation:\nThe 10th Constitutional Amendment Act, 1961 incorporated Dadra and Nagar Haveli as a Union Territory in the First Schedule.",
    "📚 முதன்மை விளக்கம்:\n1961-ஆம் ஆண்டின் 10-வது அரசியலமைப்பு திருத்தச் சட்டம் தாத்ரா மற்றும் நகர் ஹவேலியை ஒன்றிய பிரதேசமாக இணைத்தது.",
    "Option A is correct; 10th Amendment incorporated Dadra & Nagar Haveli.", "விருப்பம் A சரியானது.",
    "Option B is incorrect; 12th Amendment incorporated Goa, Daman & Diu.", "விருப்பம் B தவறானது.",
    "Option C is incorrect; 14th Amendment incorporated Puducherry.", "விருப்பம் C தவறானது.",
    "Option D is incorrect; 21st Amendment added Sindhi language.", "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: UT Integration: 10th = Dadra & Nagar Haveli, 12th = Goa, Daman & Diu, 14th = Puducherry.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: 10-வது = தாத்ரா & நகர் ஹவேலி, 12-வது = கோவா, 14-வது = புதுச்சேரி.",
    "📖 Revision Fact: In 2020, Dadra & Nagar Haveli and Daman & Diu were merged.",
    "📖 திருத்தல் செய்தி: 2020-ல் தாத்ரா & நகர் ஹவேலி மற்றும் டாமன் & டையூ இணைக்கப்பட்டன.",
    "Remember", "High", ["10th Amendment", "Dadra and Nagar Haveli", "Territorial Integration"]
)

# Q22 - Ans: C
add_p1(
    "polity_amendments_gt_022", "Medium", "single_choice",
    "Which official language was added as the 15th language in the Eighth Schedule of the Indian Constitution by the 21st Amendment Act, 1967?",
    "1967-ஆம் ஆண்டின் 21-வது திருத்தச் சட்டத்தின் மூலம் இந்திய அரசியலமைப்பின் எட்டாவது அட்டவணையில் 15-வது மொழியாகச் சேர்க்கப்பட்ட அலுவல் மொழி எது?",
    "Konkani", "கொங்கணி",
    "Manipuri", "மணிப்பூரி",
    "Sindhi", "சிந்தி",
    "Nepali", "நேபாளப் மொழி",
    "C",
    "📚 Core Explanation:\nThe 21st Constitutional Amendment Act, 1967 added Sindhi as the 15th official language in Eighth Schedule.",
    "📚 முதன்மை விளக்கம்:\n1967-ன் 21-வது திருத்தச் சட்டம் எட்டாவது அட்டவணையில் சிந்தி மொழியை 15-வது அலுவல் மொழியாகச் சேர்த்தது.",
    "Option A is incorrect; Konkani added by 71st Amendment.", "விருப்பம் A தவறானது.",
    "Option B is incorrect; Manipuri added by 71st Amendment.", "விருப்பம் B தவறானது.",
    "Option C is correct as Sindhi was added by 21st Amendment.", "விருப்பம் C சரியானது.",
    "Option D is incorrect; Nepali added by 71st Amendment.", "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: 8th Schedule language sequence: 21st -> Sindhi; 71st -> Konkani, Manipuri, Nepali; 92nd -> Bodo, Dogri, Maithili, Santhali.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: 21-வது -> சிந்தி; 71-வது -> கொங்கணி, மணிப்பூரி, நேபாளி; 92-வது -> போடோ, டோக்ரி, மைதிலி, சந்தாலி.",
    "📖 Revision Fact: Present count of official languages in 8th Schedule is 22.",
    "📖 திருத்தல் செய்தி: எட்டாவது அட்டவணையில் தற்போது 22 மொழிகள் உள்ளன.",
    "Remember", "High", ["21st Amendment", "Eighth Schedule", "Sindhi Language"]
)

# Q23 - Ans: B
add_p1(
    "polity_amendments_gt_023", "Hard", "statement",
    "Consider the following statements regarding the 97th Constitutional Amendment Act, 2011 and the Supreme Court judgment in Union of India v. Rajendra N. Shah (2021):\n1. The 97th Amendment gave constitutional status to Co-operative Societies by adding Part IX-B and Article 43B.\n2. In 2021, the Supreme Court invalidated Part IX-B for state co-operative societies because the amendment bill was NOT ratified by half of the State Legislatures.\nWhich of the statements given above is/are correct?",
    "2011-ஆம் ஆண்டின் 97-வது அரசியலமைப்பு திருத்தச் சட்டம் மற்றும் ராஜேந்திர என். ஷா வழக்கில் (2021) உச்சநீதிமன்றத்தின் தீர்ப்பு குறித்த பின்வரும் கூற்றுகளை ஆராய்க:\n1. 97-வது திருத்தம் பகுதி IX-B மற்றும் சரத்து 43B-ஐச் சேர்த்து கூட்டுறவு சங்கங்களுக்கு அரசியலமைப்பு அந்தஸ்து வழங்கியது.\n2. 2021-ல் மாநில கூட்டுறவு சங்கங்கள் தொடர்பான பகுதி IX-B-ஐ உச்சநீதிமன்றம் ரத்து செய்தது, ஏனெனில் திருத்த மசோதாவிற்கு பாதியளவு மாநில சட்டமன்றங்கள் ஒப்புதல் அளிக்கவில்லை.\nமேற்கூறிய கூற்றுகளில் எது/எவை சரியானது?",
    "1 only", "1 மட்டுமே",
    "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
    "2 only", "2 மட்டுமே",
    "Neither 1 nor 2", "1 அல்லது 2 இரண்டும் இல்லை",
    "B",
    "📚 Core Explanation:\nBoth statements 1 and 2 are CORRECT. 97th Amendment added Part IX-B. In 2021, SC invalidated Part IX-B for state co-operative societies due to lack of Art 368 state ratification.",
    "📚 முதன்மை விளக்கம்:\n1 மற்றும் 2 ஆகிய இரு கூற்றுகளும் சரியானவை.",
    "Option A is incomplete.", "விருப்பம் A அரைகுறையானது.",
    "Option B is correct as both statements 1 and 2 are true.", "விருப்பம் B சரியானது.",
    "Option C is incomplete.", "விருப்பம் C அரைகுறையானது.",
    "Option D is incorrect.", "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: Co-operative Societies is Entry 32 in State List (List II).",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: கூட்டுறவு சங்கங்கள் மாநிலப் பட்டியலின் 32-வது பதிவாகும்.",
    "📖 Revision Fact: Multi-State Co-operative provisions of 97th Amendment were upheld by Supreme Court.",
    "📖 திருத்தல் செய்தி: பல மாநில கூட்டுறவு சங்கங்கள் தொடர்பான விதிகள் உச்சநீதிமன்றத்தால் உறுதியளிக்கப்பட்டன.",
    "Analyze", "High", ["97th Amendment", "Co-operative Societies", "Rajendra N Shah Case"]
)

# Q24 - Ans: B
add_p1(
    "polity_amendments_gt_024", "Easy", "single_choice",
    "Which Constitutional Amendment Act added Part IX-A to the Constitution, providing constitutional status and protection to Municipalities (Urban Local Bodies)?",
    "நகராட்சிகளுக்கு (நகர்ப்புற உள்ளாட்சி அமைப்புகள்) அரசியலமைப்பு அந்தஸ்து மற்றும் பாதுகாப்பை வழங்கும் பகுதி IX-A-ஐ அரசியலமைப்பில் சேர்த்த திருத்தச் சட்டம் எது?",
    "73rd Constitutional Amendment Act, 1992", "73-வது அரசியலமைப்பு திருத்தச் சட்டம், 1992",
    "74th Constitutional Amendment Act, 1992", "74-வது அரசியலமைப்பு திருத்தச் சட்டம், 1992",
    "77th Constitutional Amendment Act, 1995", "77-வது அரசியலமைப்பு திருத்தச் சட்டம், 1995",
    "81st Constitutional Amendment Act, 2000", "81-வது அரசியலமைப்பு திருத்தச் சட்டம், 2000",
    "B",
    "📚 Core Explanation:\nThe 74th Constitutional Amendment Act, 1992 added Part IX-A and 12th Schedule to constitutionalize Municipalities.",
    "📚 முதன்மை விளக்கம்:\n1992-ஆம் ஆண்டின் 74-வது அரசியலமைப்பு திருத்தச் சட்டம் பகுதி IX-A மற்றும் 12-வது அட்டவணையைச் சேர்த்தது.",
    "Option A is incorrect; 73rd Amendment added Part IX and 11th Schedule.", "விருப்பம் A தவறானது.",
    "Option B is correct; 74th Amendment added Part IX-A for Municipalities.", "விருப்பம் B சரியானது.",
    "Option C is incorrect; 77th Amendment related to reservation in promotion.", "விருப்பம் C தவறானது.",
    "Option D is incorrect; 81st Amendment related to backlog vacancies.", "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: 73rd = Panchayati Raj (Part IX, 11th Schedule); 74th = Municipalities (Part IX-A, 12th Schedule).",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: 73-வது = பஞ்சாயத்து ராஜ், 74-வது = நகராட்சிகள்.",
    "📖 Revision Fact: 74th Amendment Act came into force on June 1, 1993.",
    "📖 திருத்தல் செய்தி: 74-வது திருத்தச் சட்டம் ஜூன் 1, 1993 அன்று அமலுக்கு வந்தது.",
    "Remember", "High", ["74th Amendment", "Municipalities", "12th Schedule"]
)

# Q25 - Ans: C
add_p1(
    "polity_amendments_gt_025", "Medium", "single_choice",
    "Which Constitutional Amendment Act bifurcated the combined National Commission for Scheduled Castes and Scheduled Tribes into TWO separate constitutional commissions?",
    "பட்டியல் சாதிகள் மற்றும் பட்டியல் பழங்குடியினருக்கான ஒருங்கிணைந்த தேசிய ஆணையத்தை இரண்டு தனித்தனி அரசியலமைப்பு ஆணையங்களாகப் பிரித்த அரசியலமைப்பு திருத்தச் சட்டம் எது?",
    "65th Constitutional Amendment Act, 1990", "65-வது அரசியலமைப்பு திருத்தச் சட்டம், 1990",
    "77th Constitutional Amendment Act, 1995", "77-வது அரசியலமைப்பு திருத்தச் சட்டம், 1995",
    "89th Constitutional Amendment Act, 2003", "89-வது அரசியலமைப்பு திருத்தச் சட்டம், 2003",
    "102nd Constitutional Amendment Act, 2018", "102-வது அரசியலமைப்பு திருத்தச் சட்டம், 2018",
    "C",
    "📚 Core Explanation:\nThe 89th Constitutional Amendment Act, 2003 bifurcated the combined National Commission into NCSC (Article 338) and NCST (Article 338A).",
    "📚 முதன்மை விளக்கம்:\n2003-ஆம் ஆண்டின் 89-வது அரசியலமைப்பு திருத்தச் சட்டம் NCSC (சரத்து 338) மற்றும் NCST (சரத்து 338A) என இரு ஆணையங்களாகப் பிரித்தது.",
    "Option A is incorrect; 65th Amendment created combined commission.", "விருப்பம் A தவறானது.",
    "Option B is incorrect; 77th Amendment provided reservation in promotion.", "விருப்பம் B தவறானது.",
    "Option C is correct as 89th Amendment bifurcated NCSC and NCST.", "விருப்பம் C சரியானது.",
    "Option D is incorrect; 102nd Amendment created NCBC (Art 338B).", "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: Art 338 = NCSC, Art 338A = NCST (89th Amendment), Art 338B = NCBC (102nd Amendment).",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: சரத்து 338 = NCSC, 338A = NCST, 338B = NCBC.",
    "📖 Revision Fact: Separate NCSC and NCST came into existence in February 2004.",
    "📖 திருத்தல் செய்தி: பிப்ரவரி 2004-ல் தனித்தனி அமைப்புகளாக இயங்கத் தொடங்கின.",
    "Understand", "High", ["89th Amendment", "NCSC and NCST", "Article 338A"]
)

print("Part 1 questions Q1 to Q25 loaded completely with exact answer keys.")
