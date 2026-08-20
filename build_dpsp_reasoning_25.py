import json
import os

q_data = []

def make_q(q_id, difficulty, qtype, q_en, q_ta, options_list, ca, exp_en, exp_ta, wno_dict, trap_en, trap_ta, fact_en, fact_ta, assertion_dict=None, reason_dict=None, bloom="Analyze", est_time=60, pyq="High", tags=None):
    if tags is None:
        tags = ["Polity", "Directive Principles of State Policy", "Reasoning"]
        
    options = []
    options_en = []
    options_ta = []
    for opt_id, (opt_en, opt_ta) in zip(["A", "B", "C", "D"], options_list):
        options.append({"id": opt_id, "en": opt_en, "ta": opt_ta})
        options_en.append(opt_en)
        options_ta.append(opt_ta)
        
    wno = {}
    for letter in ["A", "B", "C", "D"]:
        wno[letter] = {
            "en": wno_dict[letter][0],
            "ta": wno_dict[letter][1]
        }
        
    obj = {
        "id": q_id,
        "subject": "Polity",
        "topic": "Directive Principles of State Policy",
        "difficulty": difficulty,
        "question_type": qtype,
        "question": {"en": q_en, "ta": q_ta},
        "assertion": assertion_dict if assertion_dict else {},
        "reason": reason_dict if reason_dict else {},
        "options": options,
        "correct_answer": ca,
        "explanation": {"en": exp_en, "ta": exp_ta},
        "why_not_others": wno,
        "tnpsc_tip": {"en": f"TNPSC Trap: {trap_en}", "ta": f"TNPSC பொறி: {trap_ta}"},
        "revision_fact": {"en": fact_en, "ta": fact_ta},
        "source_reference": ["M. Laxmikanth - Indian Polity", "NCERT", "Samacheer Kalvi"],
        "bloom_level": bloom,
        "estimated_time_sec": est_time,
        "pyq_similarity": pyq,
        "tags": tags,
        "question_en": q_en,
        "question_ta": q_ta,
        "options_en": options_en,
        "options_ta": options_ta,
        "answer": ca.lower(),
        "explanation_en": exp_en,
        "explanation_ta": exp_ta
    }
    return obj

# Q1 (Medium, Type 5: Assertion & Reason, Answer: A)
q_data.append(make_q(
    "DPSP_R_001", "Medium", "Assertion & Reason",
    "Assertion (A): Although Directive Principles of State Policy are non-justiciable and cannot be directly enforced by courts, they are declared fundamental in the governance of the country.\nReason (R): Article 37 explicitly imposes a duty on the State (Legislature and Executive) to apply these principles in making laws.",
    "கூற்று (A): அரசு நெறிமுறைப்படுத்தும் கோட்பாடுகள் நீதிமன்றத்தால் நேரடியாக அமல்படுத்தப்பட முடியாதவை என்றாலும், நாட்டின் ஆட்சியில் அவை அடிப்படைத் தன்மையானவை என அறிவிக்கப்பட்டுள்ளன.\nகாரணம் (R): சட்டங்களை இயற்றும் போது இக்கோட்பாடுகளைப் பயன்படுத்துவது அரசுக்கு (சட்டமன்றம் மற்றும் நிர்வாகம்) அரசியலமைப்பு விதிக்கப்பட்ட கடமையாகும் என பிரிவு 37 தெளிவாக விதிக்கிறது.",
    [
        ("Both A and R are correct and R is the correct explanation of A", "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்."),
        ("Both A and R are correct but R is NOT the correct explanation of A", "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல."),
        ("A is correct but R is incorrect", "A சரி, ஆனால் R தவறு."),
        ("A is incorrect but R is correct", "A தவறு, ஆனால் R சரி.")
    ],
    "A",
    "Both Assertion and Reason are true, and Reason is the correct explanation. Article 37 explicitly states that while DPSPs are non-justiciable, they are 'fundamental in the governance of the country and it shall be the duty of the State to apply these principles in making laws.'",
    "கூற்று A மற்றும் காரணம் R இரண்டும் சரி, மேலும் R என்பது A-விற்கு சரியான விளக்கம். பிரிவு 37 நெறிமுறைகள் நீதிமன்றத்தால் அமல்படுத்தப்பட முடியாதவை என்றாலும், அவை 'நாட்டின் ஆட்சியில் அடிப்படைத் தன்மையானவை மற்றும் சட்டங்களை இயற்றும் போது இக்கோட்பாடுகளைப் பயன்படுத்துவது அரசின் கடமை' எனத் தெளிவாகக் குறிப்பிடுகிறது.",
    {
        "A": ("Correct. Article 37 is the exact constitutional source that declares DPSP fundamental in governance while making it non-justiciable.", "சரி. பிரிவு 37 என்பது DPSP-ஐ ஆட்சியில் அடிப்படை என அறிவிக்கும் அதே வேளையில் நீதிமன்றத்தால் அமல்படுத்த முடியாததாக மாற்றும் அரசியலமைப்பு ஆதாரமாகும்."),
        "B": ("Incorrect. Reason directly explains why DPSP are fundamental in governance.", "தவறு. காரணம் நெறிமுறைகள் ஆட்சியில் ஏன் அடிப்படைத் தன்மையானவை என்பதை நேரடியாக விளக்குகிறது."),
        "C": ("Incorrect. Reason is factually and constitutionally true under Article 37.", "தவறு. காரணம் பிரிவு 37-ன் கீழ் சரியானது."),
        "D": ("Incorrect. Assertion is factually true as per Article 37.", "தவறு. கூற்று பிரிவு 37-ன் படி சரியானது.")
    },
    "Do not confuse non-justiciability with lack of constitutional importance. Non-justiciable means a citizen cannot file a writ petition demanding their direct implementation, but the State is constitutionally bound to apply them in legislation.",
    "நீதிமன்றத்தால் அமல்படுத்த முடியாதது என்பதால் அரசியலமைப்பு முக்கியத்துவம் இல்லாதது என்று கருதக் கூடாது. குடிமக்கள் நேரடியாக அமல்படுத்த வழக்கு தொடர முடியாது, ஆனால் அரசு அவற்றைச் சட்டமியற்றுவதில் பயன்படுத்தக் கடமைப்பட்டுள்ளது.",
    "Dr. B.R. Ambedkar called DPSP a 'novel feature' of the Indian Constitution.",
    "டாக்டர் பி.ஆர். அம்பேத்கர் DPSP-ஐ இந்திய அரசியலமைப்பின் 'புதுமையான அம்சம்' என்று அழைத்தார்.",
    assertion_dict={"en": "Although Directive Principles of State Policy are non-justiciable, they are declared fundamental in the governance of the country.", "ta": "அரசு நெறிமுறைப்படுத்தும் கோட்பாடுகள் நீதிமன்றத்தால் அமல்படுத்தப்பட முடியாதவை என்றாலும், நாட்டின் ஆட்சியில் அவை அடிப்படைத் தன்மையானவை என அறிவிக்கப்பட்டுள்ளன."},
    reason_dict={"en": "Article 37 explicitly imposes a duty on the State to apply these principles in making laws.", "ta": "சட்டங்களை இயற்றும் போது இக்கோட்பாடுகளைப் பயன்படுத்துவது அரசுக்கு விதிக்கப்பட்ட கடமையாகும் என பிரிவு 37 தெளிவாக விதிக்கிறது."}
))

# Q2 (Medium, Type 1: Situation/Application, Answer: B)
q_data.append(make_q(
    "DPSP_R_002", "Medium", "Reasoning",
    "SITUATION: An employee working on a daily-wage basis performs identical duties, working hours, and responsibilities as a permanent regular employee in a government department, but receives significantly lower pay without any valid job distinction.\n\nQUESTION: Which constitutional Directive Principle, when read with Article 14, empowers courts to strike down such pay discrimination as established in Randhir Singh v. Union of India (1982)?",
    "சூழல்: அரசுத் துறையில் தற்காலிக தினக்கூலிப் பணியாளர் ஒருவர் நிரந்தரப் பணியாளருக்கு இணையான வேலை நேரம், பொறுப்புகள் மற்றும் பணிகளைச் செய்கிறார், ஆனால் எவ்வித நியாயமான காரணமும் இன்றி மிகக் குறைந்த ஊதியம் பெறுகிறார்.\n\nகேள்வி: ரந்தீர் சிங் (1982) வழக்கின்படி, பிரிவு 14 உடன் இணைந்து இத்தகைய ஊதியப் பாகுபாட்டை ரத்து செய்ய நீதிமன்றங்களுக்கு அதிகாரமளிக்கும் அரசு நெறிமுறைப் பிரிவு எது?",
    [
        ("Article 38(1)", "பிரிவு 38(1)"),
        ("Article 39(d)", "பிரிவு 39(d)"),
        ("Article 43A", "பிரிவு 43A"),
        ("Article 46", "பிரிவு 46")
    ],
    "B",
    "Correct Answer: Article 39(d). In Randhir Singh v. Union of India (1982), the Supreme Court held that 'Equal Pay for Equal Work' under Article 39(d) is not a mere directive slogan, but a constitutional goal enforceable through Article 14 and Article 21.",
    "சரியான பதில்: பிரிவு 39(d). ரந்தீர் சிங் எதிராக இந்திய யூனியன் (1982) வழக்கில், பிரிவு 39(d)-ன் கீழ் உள்ள 'சம வேலைக்கு சம ஊதியம்' என்பது வெறும் முழக்கம் அல்ல, அது பிரிவு 14 மற்றும் 21 மூலம் அமல்படுத்தப்பட வேண்டிய அரசியலமைப்பு இலக்கு என உச்சநீதிமன்றம் தீர்ப்பளித்தது.",
    {
        "A": ("Incorrect. Article 38(1) deals broadly with promoting social welfare through a just social order.", "தவறு. பிரிவு 38(1) சமூக நலனை மேம்படுத்துவதைக் கையாள்கிறது."),
        "B": ("Correct. Article 39(d) specifically directs that there is equal pay for equal work for both men and women.", "சரி. பிரிவு 39(d) ஆண், பெண் இருபாலருக்கும் சம வேலைக்கு சம ஊதியம் வழங்குவதை பிரத்யேகமாக பணிக்கிறது."),
        "C": ("Incorrect. Article 43A deals with participation of workers in management of industries.", "தவறு. பிரிவு 43A தொழிற்துறை மேலாண்மையில் தொழிலாளர் பங்கேற்பைக் கையாள்கிறது."),
        "D": ("Incorrect. Article 46 deals with promoting educational and economic interests of SCs, STs, and weaker sections.", "தவறு. பிரிவு 46 பட்டியல் சாதியினர், பழங்குடியினரின் பொருளாதார நலன்களைக் கையாள்கிறது.")
    },
    "Do not confuse Article 39(d) (Equal pay for equal work) with Article 16 (Equal opportunity in public employment). Equal pay is a DPSP goal read into Fundamental Rights by judicial interpretation.",
    "பிரிவு 39(d) (சம வேலைக்கு சம ஊதியம்) மற்றும் பிரிவு 16 (பொது வேலைவாய்ப்பில் சம வாய்ப்பு) ஆகியவற்றை குழப்பிக் கொள்ளக் கூடாது. சம ஊதியம் என்பது நீதித்துறை விளக்கத்தால் அடிப்படை உரிமைகளில் இணைக்கப்பட்ட நெறிமுறையாகும்.",
    "Equal Remuneration Act 1976 was enacted by Parliament to operationalize Article 39(d).",
    "பிரிவு 39(d)-ஐச் செயல்படுத்த நாடாளுமன்றத்தால் 1976-ல் சம ஊதியச் சட்டம் இயற்றப்பட்டது."
))

# Q3 (Medium, Type 3: Three-Statement Reasoning, Answer: C)
q_data.append(make_q(
    "DPSP_R_003", "Medium", "Reasoning",
    "Consider the following statements regarding the constitutional transformation of Article 45:\n\n1. Originally, Article 45 in Part IV directed the State to provide free and compulsory education for all children until they complete the age of 14 years within 10 years.\n2. The 86th Constitutional Amendment Act 2002 substituted Article 45 to focus strictly on early childhood care and education for children below the age of 6 years.\n3. Free and compulsory education for children between 6 and 14 years was made a Fundamental Right by inserting Article 21A into Part III.\n\nWhich of the above statements are correct?",
    "பிரிவு 45-ன் அரசியலமைப்பு மாற்றம் பற்றிய பின்வரும் கூற்றுகளை ஆராய்க:\n\n1. மூல பிரிவு 45 அரசியலமைப்பு நடைமுறைக்கு வந்த 10 ஆண்டுகளுக்குள் 14 வயது வரையிலான குழந்தைகளுக்கு இலவச கட்டாயக் கல்வி வழங்க அரசைப் பணித்தது.\n2. 86-வது திருத்தச் சட்டம் 2002 பிரிவு 45-ஐ 6 வயதிற்குட்பட்ட குழந்தைகளுக்கான ஆரம்பகால பராமரிப்பு மற்றும் கல்வியாக மாற்றியமைத்தது.\n3. 6 முதல் 14 வயது வரையிலான குழந்தைகளுக்கான இலவச கட்டாயக் கல்வி உரிமை பகுதி III-ல் பிரிவு 21A ஆகச் சேர்க்கப்பட்டு அடிப்படை உரிமையாக்கப்பட்டது.\n\nமேற்கண்ட கூற்றுகளில் எவை சரியானவை?",
    [
        ("1 and 2 only", "1 மற்றும் 2 மட்டும்"),
        ("2 and 3 only", "2 மற்றும் 3 மட்டும்"),
        ("1, 2 and 3", "1, 2 மற்றும் 3"),
        ("1 and 3 only", "1 மற்றும் 3 மட்டும்")
    ],
    "C",
    "Correct Answer: 1, 2 and 3. All three statements are factually and constitutionally correct regarding the 86th Amendment Act 2002 which reshaped Article 45 and inserted Article 21A.",
    "சரியான பதில்: 1, 2 மற்றும் 3. 86-வது திருத்தச் சட்டம் 2002 மூலம் பிரிவு 45 மாற்றியமைக்கப்பட்டு பிரிவு 21A சேர்க்கப்பட்டதைக் குறித்த மூன்று கூற்றுகளும் சரியானவை.",
    {
        "A": ("Incorrect. Statement 3 is also correct because Article 21A was inserted by the same 86th Amendment Act 2002.", "தவறு. கூற்று 3-ம் சரியானது ஏனெனில் பிரிவு 21A அதே 86-வது திருத்தத்தால் சேர்க்கப்பட்டது."),
        "B": ("Incorrect. Statement 1 is also correct regarding the original 1950 text of Article 45.", "தவறு. கூற்று 1-ம் 1950 மூல பிரிவு 45 பற்றிய சரியான தகவலாகும்."),
        "C": ("Correct. All three statements accurately trace the evolution of educational provisions under Part IV and Part III.", "சரி. மூன்று கூற்றுகளும் கல்வி தொடர்பான பிரிவுகளின் வளர்ச்சியைத் துல்லியமாகக் குறிப்பிடுகின்றன."),
        "D": ("Incorrect. Statement 2 is also correct as Article 45 now applies only to children below 6 years.", "தவறு. கூற்று 2-ம் சரியானது ஏனெனில் பிரிவு 45 தற்போது 6 வயதிற்குட்பட்ட குழந்தைகளுக்கே பொருந்தும்.")
    },
    "Pay close attention to age groups: Present Article 45 covers children BELOW 6 years (DPSP), whereas Article 21A covers children aged 6 to 14 years (Fundamental Right).",
    "வயதுப் பிரிவுகளைக் கவனியுங்கள்: தற்போதைய பிரிவு 45 6 வயதிற்குட்பட்ட குழந்தைகளைக் குறிக்கிறது (DPSP), அதே சமயம் பிரிவு 21A 6 முதல் 14 வயது வரையிலான குழந்தைகளைக் குறிக்கிறது (அடிப்படை உரிமை).",
    "Unni Krishnan Judgment (1993) derived the right to education up to age 14 from Article 45, which directly inspired the 86th Amendment Act 2002.",
    "உன்னிகிருஷ்ணன் வழக்கு (1993) பிரிவு 45-லிருந்து கல்வி உரிமையைப் பெற்றது, இது 86-வது திருத்தச் சட்டம் 2002-க்கு நேரடித் தூண்டுதலாக அமைந்தது."
))

# Q4 (Hard, Type 5: Assertion & Reason, Answer: D)
q_data.append(make_q(
    "DPSP_R_004", "Hard", "Assertion & Reason",
    "Assertion (A): Parliament can completely exclude judicial review and nullify all Fundamental Rights in Part III by enacting any law under the guise of implementing any Directive Principle in Part IV.\nReason (R): In Minerva Mills v. Union of India (1980), the Supreme Court held that harmony and balance between Part III and Part IV is an essential feature of the Basic Structure of the Constitution.",
    "கூற்று (A): பகுதி IV-ல் உள்ள எந்தவொரு நெறிமுறையையும் அமல்படுத்துவதாகக் கூறி சட்டம் இயற்றுவதன் மூலம் நீதிமன்ற ஆய்வை முழுமையாகத் தடுத்து பகுதி III-ல் உள்ள அனைத்து அடிப்படை உரிமைகளையும் நாடாளுமன்றத்தால் ரத்து செய்ய முடியும்.\nகாரணம் (R): மினர்வா மில்ஸ் வழக்கில் (1980), பகுதி III மற்றும் பகுதி IV இடையேயான இணக்கமும் சமநிலையும் அரசியலமைப்பின் அடிப்படை அமைப்பின் முக்கிய அம்சம் என உச்சநீதிமன்றம் தீர்ப்பளித்தது.",
    [
        ("Both A and R are correct and R is the correct explanation of A", "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்."),
        ("Both A and R are correct but R is NOT the correct explanation of A", "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல."),
        ("A is correct but R is incorrect", "A சரி, ஆனால் R தவறு."),
        ("A is incorrect but R is correct", "A தவறு, ஆனால் R சரி.")
    ],
    "D",
    "Assertion (A) is incorrect and Reason (R) is correct. In Minerva Mills (1980), the Supreme Court struck down Section 4 of the 42nd Amendment Act 1976 which tried to give immunity to laws implementing ALL Directive Principles over Articles 14 and 19. The SC held that giving absolute primacy to DPSP over FR destroys the Basic Structure.",
    "கூற்று A தவறு, காரணம் R சரி. மினர்வா மில்ஸ் (1980) வழக்கில், அனைத்து நெறிமுறைகளுக்கும் அடிப்படை உரிமைகளுக்கு மேல் முதன்மை அளிக்க முயன்ற 42-வது திருத்தத்தின் பிரிவு 4-ஐ உச்சநீதிமன்றம் ரத்து செய்தது.",
    {
        "A": ("Incorrect. Assertion is wrong because Parliament cannot destroy Basic Structure by giving absolute primacy to DPSP.", "தவறு. DPSP-க்கு முழு முதன்மை அளித்து அடிப்படை அமைப்பை நாடாளுமன்றம் சிதைக்க முடியாது என்பதால் கூற்று தவறானது."),
        "B": ("Incorrect. Assertion is constitutionally invalid post-Minerva Mills.", "தவறு. மினர்வா மில்ஸ் வழக்கிற்குப் பின் கூற்று செல்லாதது."),
        "C": ("Incorrect. Reason is a celebrated Basic Structure ruling of the Supreme Court.", "தவறு. காரணம் உச்சநீதிமன்றத்தின் புகழ்பெற்ற அடிப்படை அமைப்புத் தீர்ப்பாகும்."),
        "D": ("Correct. Assertion is false because DPSP cannot override Basic Structure; Reason is true.", "சரி. நெறிமுறைகள் அடிப்படை அமைப்பை மீற முடியாது என்பதால் கூற்று தவறு; காரணம் சரி.")
    },
    "Remember that currently Article 31C protection applies ONLY to laws implementing Article 39(b) and Article 39(c), NOT all Directive Principles.",
    "தற்போது பிரிவு 31C பாதுகாப்பு பிரிவு 39(b) மற்றும் 39(c)-ஐ அமல்படுத்தும் சட்டங்களுக்கு மட்டுமே பொருந்தும், அனைத்து நெறிமுறைகளுக்கும் அல்ல என்பதை நினைவில் கொள்க.",
    "Minerva Mills case (1980) famously declared: 'Part III and Part IV are like two wheels of a chariot; to give primacy to one over the other is to disrupt the balance.'",
    "மினர்வா மில்ஸ் வழக்கில் (1980): 'பகுதி III மற்றும் பகுதி IV ஆகியவை ஒரு தேரின் இரு சக்கரங்கள் போன்றவை' என்று பிரகடனம் செய்யப்பட்டது.",
    assertion_dict={"en": "Parliament can completely exclude judicial review and nullify all Fundamental Rights by enacting laws implementing any Directive Principle.", "ta": "எந்தவொரு நெறிமுறையையும் அமல்படுத்துவதாகக் கூறி சட்டம் இயற்றுவதன் மூலம் அடிப்படை உரிமைகளை நாடாளுமன்றத்தால் முழுமையாக ரத்து செய்ய முடியும்."},
    reason_dict={"en": "In Minerva Mills (1980), the SC held that harmony between Part III and Part IV is part of the Basic Structure.", "ta": "மினர்வா மில்ஸ் வழக்கில் (1980), பகுதி III மற்றும் IV இடையேயான இணக்கம் அடிப்படை அமைப்பின் பகுதி என உச்சநீதிமன்றம் தீர்ப்பளித்தது."}
))

# Q5 (Easy-Medium, Type 2: Two-Statement Reasoning, Answer: A)
q_data.append(make_q(
    "DPSP_R_005", "Easy-Medium", "Reasoning",
    "Consider the following statements regarding socialist Directives under Article 39:\n\n1. Article 39(b) directs the State to ensure that the ownership and control of the material resources of the community are distributed to best subserve the common good.\n2. Article 39(c) explicitly directs the State to nationalise all private commercial banks automatically without paying any compensation to shareholders.\n\nWhich of the above statements is/are correct?",
    "பிரிவு 39-ன் கீழ் உள்ள சோசலிச நெறிமுறைகள் பற்றிய பின்வரும் கூற்றுகளை ஆராய்க:\n\n1. பொது நலனுக்குச் சிறந்த முறையில் பயன்படும் வகையில் சமுதாயத்தின் பருப்பொருள் வளங்களின் உரிமையும் கட்டுப்பாடும் விநியோகிக்கப்பட வேண்டும் என பிரிவு 39(b) பணிக்கிறது.\n2. பிரிவு 39(c) நாட்டில் உள்ள அனைத்து தனியார் வணிக வங்கிகளையும் பங்குதாரர்களுக்கு எவ்வித இழப்பீடும் இன்றி தானாகவே தேசியமயமாக்க அரசைப் பணிக்கிறது.\n\nமேற்கண்ட கூற்றுகளில் எது/எவை சரியானவை?",
    [
        ("1 only", "1 மட்டும்"),
        ("2 only", "2 மட்டும்"),
        ("Both 1 and 2", "1 மற்றும் 2 இரண்டும்"),
        ("Neither 1 nor 2", "1 மற்றும் 2 இரண்டும் இல்லை")
    ],
    "A",
    "Statement 1 is correct and Statement 2 is incorrect. Article 39(c) directs that the operation of the economic system does not result in the concentration of wealth and means of production to the common detriment. It does not mandate automatic uncompensated nationalization of all private banks.",
    "கூற்று 1 சரி, கூற்று 2 தவறு. பிரிவு 39(c) பொருளாதார அமைப்பு இயங்குவது செல்வம் மற்றும் உற்பத்தி சாதனங்கள் பொது நலனுக்குத் தீங்கான முறையில் குவிவதற்கு வழிவகுக்கக் கூடாது என்றே பணிக்கிறது.",
    {
        "A": ("Correct. Statement 1 accurately quotes Article 39(b), while Statement 2 misrepresents Article 39(c).", "சரி. கூற்று 1 பிரிவு 39(b)-ஐ துல்லியமாக மேற்கோள் காட்டுகிறது, ஆனால் கூற்று 2 பிரிவு 39(c)-ஐ தவறாகக் குறிப்பிடுகிறது."),
        "B": ("Incorrect. Statement 2 is factually false.", "தவறு. கூற்று 2 தவறானது."),
        "C": ("Incorrect. Statement 2 contains an incorrect assertion regarding automatic uncompensated nationalization.", "தவறு. கூற்று 2 இழப்பீடற்ற தானியங்கி தேசியமயமாக்கல் பற்றி தவறான தகவலைக் கொண்டுள்ளது."),
        "D": ("Incorrect. Statement 1 is correct.", "தவறு. கூற்று 1 சரியானது.")
    },
    "Article 39(b) deals with distribution of material resources, whereas Article 39(c) deals with preventing concentration of wealth.",
    "பிரிவு 39(b) பருப்பொருள் வளங்களின் விநியோகத்தைக் கையாள்கிறது, அதே வேளையில் பிரிவு 39(c) செல்வம் குவிவதைத் தடுப்பதைக் கையாள்கிறது.",
    "Laws implementing Article 39(b) and 39(c) are protected under Article 31C from challenge under Articles 14 and 19.",
    "பிரிவு 39(b) மற்றும் 39(c)-ஐ அமல்படுத்தும் சட்டங்கள் பிரிவு 31C-ன் கீழ் பிரிவுகள் 14 மற்றும் 19-லிருந்து பாதுகாப்பு பெறுகின்றன."
))

# Q6 (Medium, Type 6: Situation → Constitutional Principle, Answer: B)
q_data.append(make_q(
    "DPSP_R_006", "Medium", "Reasoning",
    "SITUATION: An impoverished undertrial prisoner, who cannot afford to engage a defense advocate, has been languishing in jail for years without any legal representation or trial.\n\nQUESTION: Which Directive Principle of State Policy, added by the 42nd Constitutional Amendment Act 1976 and operationalized by the Legal Services Authorities Act 1987, directly addresses this situation?",
    "சூழல்: வறுமையில் வாடும் விசாரணை கைதி ஒருவர் வழக்கறிஞரை நியமிக்க முடியாமல் பல ஆண்டுகளாக நீதிமன்ற உதவி அல்லது விசாரணையின்றி சிறையில் வாடுகிறார்.\n\nகேள்வி: 42-வது திருத்தச் சட்டத்தால் சேர்க்கப்பட்டு 1987-ம் ஆண்டின் சட்டப் பணிகள் ஆணைக்குழுச் சட்டம் மூலம் அமல்படுத்தப்பட்ட எந்த அரசு நெறிமுறைப் பிரிவு இச்சூழலை நேரடியாக நிவர்த்தி செய்கிறது?",
    [
        ("Article 39(f)", "பிரிவு 39(f)"),
        ("Article 39A", "பிரிவு 39A"),
        ("Article 43", "பிரிவு 43"),
        ("Article 50", "பிரிவு 50")
    ],
    "B",
    "Correct Answer: Article 39A. Article 39A obligates the State to promote equal justice and provide free legal aid to the poor by suitable legislation or schemes. This was implemented by passing the Legal Services Authorities Act 1987 which created NALSA and Lok Adalats.",
    "சரியான பதில்: பிரிவு 39A. பிரிவு 39A ஏழைகளுக்கு இலவச சட்ட உதவி வழங்கி சம நீதியை மேம்படுத்த அரசைப் பணிக்கிறது. இது 1987-ம் ஆண்டின் சட்டப் பணிகள் ஆணைக்குழுச் சட்டம் மற்றும் NALSA மூலம் அமல்படுத்தப்பட்டது.",
    {
        "A": ("Incorrect. Article 39(f) deals with healthy development of children.", "தவறு. பிரிவு 39(f) குழந்தைகளின் ஆரோக்கியமான வளர்ச்சியைக் கையாள்கிறது."),
        "B": ("Correct. Article 39A specifies 'Equal justice and free legal aid'.", "சரி. பிரிவு 39A 'சம நீதி மற்றும் இலவச சட்ட உதவி'யைக் குறிப்பிடுகிறது."),
        "C": ("Incorrect. Article 43 deals with living wage for workers.", "தவறு. பிரிவு 43 தொழிலாளர்களின் வாழ்வாதார ஊதியத்தைக் கையாள்கிறது."),
        "D": ("Incorrect. Article 50 deals with separation of judiciary from executive.", "தவறு. பிரிவு 50 நீதித்துறையை நிர்வாகத்திலிருந்து பிரிப்பதைக் கையாள்கிறது.")
    },
    "In Hussainara Khatoon v. Home Secretary, Bihar (1979), the Supreme Court ruled that right to free legal aid under Article 39A is an integral part of Fundamental Right to life and personal liberty under Article 21.",
    "ஹுசைனாரா கதூன் (1979) வழக்கில், பிரிவு 39A-ன் கீழ் இலவச சட்ட உதவி பெறுவது பிரிவு 21-ன் வாழ்வுரிமையின் ஒருங்கிணைந்த பகுதி என உச்சநீதிமன்றம் தீர்ப்பளித்தது.",
    "NALSA (National Legal Services Authority) was constituted on November 9, 1995.",
    "தேசிய சட்டப் பணிகள் ஆணைக்குழு (NALSA) நவம்பர் 9, 1995 அன்று அமைக்கப்பட்டது."
))

# Q7 (Medium, Type 4: Correct/Incorrect, Answer: C)
q_data.append(make_q(
    "DPSP_R_007", "Medium", "Reasoning",
    "Which of the following statements regarding the constitutional relationship between Article 40 and Panchayati Raj is CORRECT?",
    "பிரிவு 40 மற்றும் பஞ்சாயத்து ராஜ் இடையேயான அரசியலமைப்புத் தொடர்பு குறித்து பின்வருவனவற்றில் எது சரியானது?",
    [
        ("Article 40 was added to Part IV by the 73rd Constitutional Amendment Act 1992.", "73-வது அரசியலமைப்பு திருத்தச் சட்டம் 1992 மூலம் பிரிவு 40 பகுதி IV-ல் சேர்க்கப்பட்டது."),
        ("Article 40 is a justiciable fundamental right allowing citizens to file writ petitions if panchayats are not held.", "கிராம பஞ்சாயத்துகள் அமைக்கப்படாவிட்டால் குடிமக்கள் வழக்கு தொடர வழிவகுக்கும் அடிப்படை உரிமை பிரிவு 40 ஆகும்."),
        ("Article 40 contained the original non-justiciable directive for village panchayats, which received a statutory constitutional framework through Part IX added by the 73rd Amendment Act 1992.", "பிரிவு 40 கிராம பஞ்சாயத்துகளுக்கான மூல நெறிமுறையைக் கொண்டிருந்தது, அதற்கு 73-வது திருத்தச் சட்டம் 1992 மூலம் பகுதி IX சேர்க்கப்பட்டு அரசியலமைப்பு அந்தஸ்து வழங்கப்பட்டது."),
        ("Article 40 mandates a rigid 2-tier Panchayati Raj structure in all States regardless of population.", "அனைத்து மாநிலங்களிலும் மக்கள் தொகையைப் பொருட்படுத்தாமல் 2 அடுக்கு பஞ்சாயத்து ராஜ் முறையை பிரிவு 40 கட்டாயமாக்குகிறது.")
    ],
    "C",
    "Statement C is correct. Article 40 was present in the original 1950 Constitution as a Gandhian Directive Principle directing the State to organise village panchayats. The 73rd Constitutional Amendment Act 1992 operationalized this directive by inserting Part IX and Eleventh Schedule.",
    "கூற்று C சரியானது. பிரிவு 40 1950 மூல அரசியலமைப்பிலேயே கிராம பஞ்சாயத்துகளை அமைக்கப் பணிக்கும் காந்திய நெறிமுறையாக இருந்தது. 73-வது திருத்தச் சட்டம் 1992 பகுதி IX மற்றும் 11-வது அட்டவணையைச் சேர்த்து இதற்கு அரசியலமைப்பு அந்தஸ்தை வழங்கியது.",
    {
        "A": ("Incorrect. Article 40 was in the original 1950 Constitution, not added by the 73rd Amendment.", "தவறு. பிரிவு 40 1950 மூல அரசியலமைப்பிலேயே இருந்தது."),
        "B": ("Incorrect. Article 40 is a non-justiciable Directive Principle in Part IV.", "தவறு. பிரிவு 40 நீதிமன்றத்தால் அமல்படுத்த முடியாத பகுதி IV நெறிமுறையாகும்."),
        "C": ("Correct. Article 40 set the directive vision in 1950 which Part IX codified into constitutional law in 1992.", "சரி. 1950-ல் பிரிவு 40 அமைத்த இலக்கை 1992-ல் பகுதி IX அரசியலமைப்புச் சட்டமாக மாற்றியது."),
        "D": ("Incorrect. The 73rd Amendment established a 3-tier system (with an exception for States under 20 lakh population), not Article 40.", "தவறு. 73-வது திருத்தம் 3 அடுக்கு முறையை நிறுவியது.")
    },
    "Balwant Rai Mehta Committee (1957) was the first committee to recommend a 3-tier Panchayati Raj system to implement Article 40.",
    "பிரிவு 40-ஐ அமல்படுத்த 3 அடுக்கு பஞ்சாயத்து ராஜ் முறையைப் பரிந்துரைத்த முதல் குழு பல்வந்த் ராய் மேத்தா குழு (1957) ஆகும்.",
    "April 24 is celebrated as National Panchayati Raj Day in India.",
    "ஏப்ரல் 24 இந்தியாவில் தேசிய பஞ்சாயத்து ராஜ் தினமாகக் கொண்டாடப்படுகிறது."
))

# Q8 (Hard, Type 5: Assertion & Reason, Answer: D)
q_data.append(make_q(
    "DPSP_R_008", "Hard", "Assertion & Reason",
    "Assertion (A): Article 48A imposes an enforceable legal duty directly on individual citizens to protect and improve forests, lakes, rivers, and wildlife.\nReason (R): Article 48A is a Directive Principle addressed to the State, whereas Article 51A(g) is a Fundamental Duty addressed to every citizen of India.",
    "கூற்று (A): காடுகள், ஏரிகள், ஆறுகள் மற்றும் வனவிலங்குகளைப் பாதுகாத்து மேம்படுத்த பிரிவு 48A தனிப்பட்ட குடிமக்களுக்கு நேரடியாக அமல்படுத்தக்கூடிய சட்டப்பூர்வ கடமையை விதிக்கிறது.\nகாரணம் (R): பிரிவு 48A என்பது அரசுக்கு வழங்கப்பட்ட நெறிமுறையாகும், அதே வேளையில் பிரிவு 51A(g) என்பது இந்தியாவின் ஒவ்வொரு குடிமகனுக்கும் வழங்கப்பட்ட அடிப்படைக் கடமையாகும்.",
    [
        ("Both A and R are correct and R is the correct explanation of A", "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்."),
        ("Both A and R are correct but R is NOT the correct explanation of A", "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல."),
        ("A is correct but R is incorrect", "A சரி, ஆனால் R தவறு."),
        ("A is incorrect but R is correct", "A தவறு, ஆனால் R சரி.")
    ],
    "D",
    "Assertion (A) is incorrect and Reason (R) is correct. Article 48A (Part IV DPSP) is a directive addressed to the State ('The State shall endeavour to protect...'). Individual obligation to protect environment is prescribed under Article 51A(g) (Part IVA Fundamental Duties).",
    "கூற்று A தவறு, காரணம் R சரி. பிரிவு 48A (DPSP) அரசுக்கான நெறிமுறையாகும் ('அரசு முயல வேண்டும்...'). குடிமக்களுக்கான கடமை பிரிவு 51A(g)-ல் உள்ளது.",
    {
        "A": ("Incorrect. Assertion confuses Article 48A (State directive) with Article 51A(g) (Citizen duty).", "தவறு. கூற்று பிரிவு 48A-ஐ பிரிவு 51A(g) உடன் குழப்பிக் கொள்கிறது."),
        "B": ("Incorrect. Assertion is factually wrong.", "தவறு. கூற்று தவறானது."),
        "C": ("Incorrect. Reason is factually correct.", "தவறு. காரணம் சரியானது."),
        "D": ("Correct. Article 48A applies to the State, while Article 51A(g) applies to citizens.", "சரி. பிரிவு 48A அரசுக்கும், பிரிவு 51A(g) குடிமக்களுக்கும் பொருந்தும்.")
    },
    "Notice the constitutional pairing: Article 48A (State obligation for environment) works together with Article 51A(g) (Citizen duty for environment). Both were added by the 42nd Amendment Act 1976.",
    "அரசியலமைப்பு இணைப்பைக் கவனியுங்கள்: பிரிவு 48A (சுற்றுச்சூழலுக்கான அரசின் கடமை) மற்றும் பிரிவு 51A(g) (குடிமகனின் கடமை) இரண்டும் 1976-ல் 42-வது திருத்தத்தால் சேர்க்கப்பட்டவை.",
    "M.C. Mehta environmental public interest litigations invoked both Article 48A and Article 51A(g) to enforce environmental protection.",
    "எம்.சி. மேத்தா சுற்றுச்சூழல் பொதுநல வழக்குகள் பிரிவு 48A மற்றும் 51A(g) இரண்டையும் பயன்படுத்தின.",
    assertion_dict={"en": "Article 48A imposes an enforceable duty directly on individual citizens to protect wildlife.", "ta": "வனவிலங்குகளைப் பாதுகாக்க பிரிவு 48A தனிப்பட்ட குடிமக்களுக்கு நேரடியாக அமல்படுத்தக்கூடிய கடமையை விதிக்கிறது."},
    reason_dict={"en": "Article 48A is a DPSP addressed to the State, while Article 51A(g) is a Fundamental Duty of citizens.", "ta": "பிரிவு 48A என்பது அரசுக்கான நெறிமுறையாகும், அதே வேளையில் பிரிவு 51A(g) என்பது குடிமகனின் கடமையாகும்."}
))

# Q9 (Easy-Medium, Type 1: Situation/Application, Answer: A)
q_data.append(make_q(
    "DPSP_R_009", "Easy-Medium", "Reasoning",
    "SITUATION: A female employee working in a private garment manufacturing enterprise is denied paid maternity leave and threatened with summary dismissal upon reporting her pregnancy.\n\nQUESTION: Which Directive Principle of State Policy specifically mandates that the State shall make provision for securing just and humane conditions of work and for maternity relief?",
    "சூழல்: தனியார் ஆடைத் தயாரிப்பு நிறுவனத்தில் பணிபுரியும் பெண் தொழிலாளிக்கு கர்ப்ப காலத்தில் ஊதியத்துடன் கூடிய மகப்பேறு விடுப்பு மறுக்கப்பட்டு பணிநீக்கம் செய்யப்படுவதாக அச்சுறுத்தப்படுகிறார்.\n\nகேள்வி: நியாயமான மற்றும் மனிதத்தன்மையான பணிச்சூழலையும் மகப்பேறு உதவியையும் உறுதி செய்ய அரசு வழிவகை செய்ய வேண்டும் என பிரத்யேகமாகப் பணிக்கும் அரசு நெறிமுறைப் பிரிவு எது?",
    [
        ("Article 42", "பிரிவு 42"),
        ("Article 41", "பிரிவு 41"),
        ("Article 43", "பிரிவு 43"),
        ("Article 47", "பிரிவு 47")
    ],
    "A",
    "Correct Answer: Article 42. Article 42 explicitly states: 'The State shall make provision for securing just and humane conditions of work and for maternity relief.' This directive was implemented by Parliament by enacting the Maternity Benefit Act 1961.",
    "சரியான பதில்: பிரிவு 42. பிரிவு 42: 'நியாயமான மற்றும் மனிதத்தன்மையான பணிச்சூழலையும் மகப்பேறு உதவியையும் உறுதி செய்ய அரசு வழிவகை செய்ய வேண்டும்' எனக் கூறுகிறது. இது 1961 மகப்பேறு நலச் சட்டம் மூலம் அமல்படுத்தப்பட்டது.",
    {
        "A": ("Correct. Article 42 contains the explicit constitutional directive for maternity relief and humane work conditions.", "சரி. பிரிவு 42 மகப்பேறு உதவி மற்றும் மனிதத்தன்மையான பணிச்சூழலுக்கான நேரடி நெறிமுறையைக் கொண்டுள்ளது."),
        "B": ("Incorrect. Article 41 deals with right to work, education, and public assistance in cases of unemployment, old age, sickness.", "தவறு. பிரிவு 41 வேலை உரிமை, கல்வி மற்றும் பொது உதவியைக் கையாள்கிறது."),
        "C": ("Incorrect. Article 43 deals with living wage and decent standard of life for workers.", "தவறு. பிரிவு 43 வாழ்வாதார ஊதியத்தைக் கையாள்கிறது."),
        "D": ("Incorrect. Article 47 deals with public health, nutrition, and prohibition.", "தவறு. பிரிவு 47 பொது சுகாதாரம் மற்றும் மதுவிலக்கைக் கையாள்கிறது.")
    },
    "Do not confuse Article 42 (Maternity relief & humane work conditions) with Article 41 (Right to work and public assistance) or Article 43 (Living wage).",
    "பிரிவு 42 (மகப்பேறு உதவி) மற்றும் பிரிவு 41 (வேலை உரிமை) அல்லது பிரிவு 43 (வாழ்வாதார ஊதியம்) ஆகியவற்றை குழப்பிக் கொள்ளக் கூடாது.",
    "Maternity Benefit Amendment Act 2017 increased paid maternity leave from 12 weeks to 26 weeks for working women.",
    "2017 மகப்பேறு நலத் திருத்தச் சட்டம் ஊதியத்துடன் கூடிய மகப்பேறு விடுப்பை 12 வாரங்களிலிருந்து 26 வாரங்களாக உயர்த்தியது."
))

# Q10 (Medium, Type 2: Two-Statement Reasoning, Answer: B)
q_data.append(make_q(
    "DPSP_R_010", "Medium", "Reasoning",
    "Consider the following statements regarding the constitutional concept of 'Living Wage' under Article 43:\n\n1. Under Article 43, 'living wage' is defined as the bare subsistence minimum wage necessary only to keep a worker alive at starvation levels.\n2. 'Living wage' is an economic concept higher than 'minimum wage' and 'fair wage', aimed at ensuring for workers a decent standard of life, full enjoyment of leisure, and social-cultural opportunities.\n\nWhich of the above statements is/are correct?",
    "பிரிவு 43-ன் கீழ் உள்ள 'வாழ்வாதார ஊதியம்' பற்றிய பின்வரும் கூற்றுகளை ஆராய்க:\n\n1. பிரிவு 43-ன் கீழ் 'வாழ்வாதார ஊதியம்' என்பது தொழிலாளி பட்டினியின்றி உயிர்வாழ்வதற்கு மட்டுமே தேவையான குறைந்தபட்ச அடிப்படை ஊதியத்தைக் குறிக்கிறது.\n2. 'வாழ்வாதார ஊதியம்' என்பது குறைந்தபட்ச ஊதியம் மற்றும் நியாயமான ஊதியத்தை விட உயர்வான பொருளாதாரக் கருத்தாகும், இது தொழிலாளர்களுக்கு கண்ணியமான வாழ்க்கைத்தரம் மற்றும் சமூக-பண்பாட்டு வாய்ப்புகளை உறுதி செய்வதை நோக்கமாகக் கொண்டது.\n\nமேற்கண்ட கூற்றுகளில் எது/எவை சரியானவை?",
    [
        ("1 only", "1 மட்டும்"),
        ("2 only", "2 மட்டும்"),
        ("Both 1 and 2", "1 மற்றும் 2 இரண்டும்"),
        ("Neither 1 nor 2", "1 மற்றும் 2 இரண்டும் இல்லை")
    ],
    "B",
    "Statement 1 is incorrect and Statement 2 is correct. In constitutional law, 'living wage' goes far beyond bare subsistence; it includes provision for education of children, health protection, insurance, and social security, ensuring a decent standard of life as directed by Article 43.",
    "கூற்று 1 தவறு, கூற்று 2 சரி. பிரிவு 43-ன் கீழ் 'வாழ்வாதார ஊதியம்' என்பது வெறும் பட்டினித் தவிர்ப்பு ஊதியம் அல்ல; அது குழந்தைகள் கல்வி, சுகாதாரம் மற்றும் காப்பீடு உட்பட கண்ணியமான வாழ்க்கையை உறுதி செய்வதாகும்.",
    {
        "A": ("Incorrect. Statement 1 describes bare subsistence wage, not living wage.", "தவறு. கூற்று 1 வெறும் அடிப்படை ஊதியத்தை மட்டுமே விவரிக்கிறது."),
        "B": ("Correct. Statement 2 accurately defines the constitutional scope of Living Wage under Article 43.", "சரி. கூற்று 2 பிரிவு 43-ன் கீழ் வாழ்வாதார ஊதியத்தின் சரியான வரம்பை விவரிக்கிறது."),
        "C": ("Incorrect. Statement 1 is factually wrong.", "தவறு. கூற்று 1 தவறானது."),
        "D": ("Incorrect. Statement 2 is correct.", "தவறு. கூற்று 2 சரியானது.")
    },
    "Hierarchy of Wages in Indian Labor Law: Bare Subsistence Wage < Minimum Wage < Fair Wage < Living Wage. Article 43 targets the highest ideal: Living Wage.",
    "இந்திய தொழிலாளர் சட்டத்தில் ஊதிய வரிசை: அடிப்படை ஊதியம் < குறைந்தபட்ச ஊதியம் < நியாயமான ஊதியம் < வாழ்வாதார ஊதியம். பிரிவு 43 வாழ்வாதார ஊதியத்தையே இலக்காகக் கொண்டுள்ளது.",
    "Minimum Wages Act 1948 was enacted to secure at least minimum wages as a step towards living wages.",
    "வாழ்வாதார ஊதியத்தை நோக்கிய முதல் படியாக குறைந்தபட்ச ஊதியச் சட்டம் 1948 இயற்றப்பட்டது."
))

# Q11 (Hard, Type 3: Three-Statement Reasoning, Answer: C)
q_data.append(make_q(
    "DPSP_R_011", "Hard", "Reasoning",
    "Consider the following statements regarding the Directive Principles added to Part IV by the 42nd Constitutional Amendment Act 1976:\n\n1. Added Article 39A directing the State to provide free legal aid to the poor.\n2. Added Article 43A directing the State to take steps to secure the participation of workers in the management of undertakings.\n3. Added Article 48A directing the State to protect and improve the environment and safeguard forests and wildlife.\n\nWhich of the above statements are correct?",
    "1976-ம் ஆண்டின் 42-வது அரசியலமைப்பு திருத்தச் சட்டத்தால் பகுதி IV-ல் சேர்க்கப்பட்ட அரசு நெறிமுறைப்படுத்தும் கோட்பாடுகள் பற்றிய கூற்றுகளை ஆராய்க:\n\n1. ஏழைகளுக்கு இலவச சட்ட உதவி வழங்க பிரிவு 39A சேர்க்கப்பட்டது.\n2. தொழிற்துறை மேலாண்மையில் தொழிலாளர்களின் பங்கேற்பை உறுதி செய்ய பிரிவு 43A சேர்க்கப்பட்டது.\n3. சுற்றுச்சூழலைப் பாதுகாக்கவும் மேம்படுத்தவும் வனவிலங்குகளைப் பாதுகாக்கவும் பிரிவு 48A சேர்க்கப்பட்டது.\n\nமேற்கண்ட கூற்றுகளில் எவை சரியானவை?",
    [
        ("1 and 2 only", "1 மற்றும் 2 மட்டும்"),
        ("2 and 3 only", "2 மற்றும் 3 மட்டும்"),
        ("1, 2 and 3", "1, 2 மற்றும் 3"),
        ("1 and 3 only", "1 மற்றும் 3 மட்டும்")
    ],
    "C",
    "Correct Answer: 1, 2 and 3. The 42nd Amendment Act 1976 added FOUR new DPSP provisions: Article 39(f) (healthy development of children), Article 39A (free legal aid), Article 43A (workers' participation in management), and Article 48A (environment and wildlife protection).",
    "சரியான பதில்: 1, 2 மற்றும் 3. 42-வது திருத்தச் சட்டம் 1976 நான்கு புதிய நெறிமுறைகளைச் சேர்த்தது: பிரிவு 39(f), 39A, 43A மற்றும் 48A.",
    {
        "A": ("Incorrect. Statement 3 is also correct.", "தவறு. கூற்று 3-ம் சரியானது."),
        "B": ("Incorrect. Statement 1 is also correct.", "தவறு. கூற்று 1-ம் சரியானது."),
        "C": ("Correct. All three listed provisions were inserted into Part IV by the 42nd Amendment 1976.", "சரி. பட்டியலிடப்பட்ட மூன்று பிரிவுகளும் 42-வது திருத்தம் 1976 மூலம் சேர்க்கப்பட்டவை."),
        "D": ("Incorrect. Statement 2 is also correct.", "தவறு. கூற்று 2-ம் சரியானது.")
    },
    "Memorise the 4 DPSP provisions added by 42nd Amendment (1976): 39(f), 39A, 43A, 48A. (Note: Article 38(2) was added by 44th Amendment 1978, and Article 43B by 97th Amendment 2011).",
    "42-வது திருத்தத்தால் (1976) சேர்க்கப்பட்ட 4 நெறிமுறைகளை நினைவில் கொள்க: 39(f), 39A, 43A, 48A. (பிரிவு 38(2) 44-வது திருத்தத்தாலும், பிரிவு 43B 97-வது திருத்தத்தாலும் சேர்க்கப்பட்டன).",
    "The 42nd Amendment Act 1976 is often referred to as the 'Mini-Constitution'.",
    "42-வது திருத்தச் சட்டம் 1976 'குறு அரசியலமைப்பு' என்று அழைக்கப்படுகிறது."
))

# Q12 (Easy-Medium, Type 6: Situation → Constitutional Principle, Answer: D)
q_data.append(make_q(
    "DPSP_R_012", "Easy-Medium", "Reasoning",
    "SITUATION: The Parliament considers enacting a single uniform code governing civil matters such as marriage, divorce, maintenance, adoption, and succession applicable to all citizens throughout India irrespective of religion.\n\nQUESTION: Which constitutional Directive Principle forms the explicit basis for formulating a Uniform Civil Code?",
    "சூழல்: மதம் பாராமல் இந்தியாவில் உள்ள அனைத்து குடிமக்களுக்கும் ஒரே மாதிரியான திருமணம், விவாகரத்து, ஜீவனாம்சம், தத்தெடுப்பு மற்றும் வாரிசுரிமை சட்டங்களை இயற்ற நாடாளுமன்றம் பரிசீலிக்கிறது.\n\nகேள்வி: பொது சிவில் சட்டத்தை உருவாக்குவதற்கு நேரடி அடிப்படையாக அமையும் அரசியலமைப்பு அரசு நெறிமுறைப் பிரிவு எது?",
    [
        ("Article 38", "பிரிவு 38"),
        ("Article 40", "பிரிவு 40"),
        ("Article 43", "பிரிவு 43"),
        ("Article 44", "பிரிவு 44")
    ],
    "D",
    "Correct Answer: Article 44. Article 44 states: 'The State shall endeavour to secure for the citizens a Uniform Civil Code throughout the territory of India.' Goa is the only State in India that has a Uniform Civil Code (Goa Civil Code 1867).",
    "சரியான பதில்: பிரிவு 44. பிரிவு 44: 'இந்தியா முழுவதிலும் உள்ள குடிமக்களுக்கு ஒரே மாதிரியான சிவில் சட்டத்தை உறுதி செய்ய அரசு முயல வேண்டும்' எனக் கூறுகிறது. கோவா இந்தியாவில் பொது சிவில் சட்டம் உள்ள ஒரே மாநிலமாகும்.",
    {
        "A": ("Incorrect. Article 38 deals with social order and minimising inequalities.", "தவறு. பிரிவு 38 சமூக நலன் மற்றும் ஏற்றத்தாழ்வுகளைக் குறைப்பதைக் கையாள்கிறது."),
        "B": ("Incorrect. Article 40 deals with organisation of village panchayats.", "தவறு. பிரிவு 40 கிராம பஞ்சாயத்துகளை அமைப்பதைக் கையாள்கிறது."),
        "C": ("Incorrect. Article 43 deals with living wages for workers.", "தவறு. பிரிவு 43 தொழிலாளர் வாழ்வாதார ஊதியத்தைக் கையாள்கிறது."),
        "D": ("Correct. Article 44 explicitly directs the implementation of a Uniform Civil Code.", "சரி. பிரிவு 44 பொது சிவில் சட்டத்தை அமல்படுத்துவதை பிரத்யேகமாகப் பணிக்கிறது.")
    },
    "Article 44 is classified under Liberal-Intellectual Principles. In Shah Bano case (1985) and Sarla Mudgal case (1995), Supreme Court advocated implementation of Article 44.",
    "பிரிவு 44 தாராளமய-அறிவுசார் கோட்பாடுகளின் கீழ் வகைப்படுத்தப்பட்டுள்ளது. ஷா பானோ (1985) மற்றும் சர்லா முத்கல் (1995) வழக்குகளில் பிரிவு 44-ஐ அமல்படுத்த உச்சநீதிமன்றம் வலியுறுத்தியது.",
    "Article 44 applies to civil personal laws, NOT criminal laws (which are already uniform across India under BNS/IPC).",
    "பிரிவு 44 சிவில் தனிநபர் சட்டங்களுக்கு மட்டுமே பொருந்தும், குற்றவியல் சட்டங்களுக்கு அல்ல."
))

# Q13 (Easy-Medium, Type 4: Correct/Incorrect, Answer: A)
q_data.append(make_q(
    "DPSP_R_013", "Easy-Medium", "Reasoning",
    "Which of the following Directive Principles is correctly classified as a **Gandhian Principle** based on Mahatma Gandhi's programme of reconstruction?",
    "பின்வரும் அரசு நெறிமுறைக் கோட்பாடுகளில் எது மகாத்மா காந்தியின் தத்துவத்தின் அடிப்படையில் **காந்தியக் கோட்பாடு** என சரியாக வகைப்படுத்தப்பட்டுள்ளது?",
    [
        ("Article 40 (Village Panchayats) & Article 47 (Prohibition of intoxicating drinks)", "பிரிவு 40 (கிராம பஞ்சாயத்துகள்) & பிரிவு 47 (மதுவிலக்கு)"),
        ("Article 39A (Free legal aid) & Article 43A (Workers' participation in management)", "பிரிவு 39A (இலவச சட்ட உதவி) & பிரிவு 43A (மேலாண்மையில் தொழிலாளர் பங்கேற்பு)"),
        ("Article 44 (Uniform Civil Code) & Article 48A (Environment protection)", "பிரிவு 44 (பொது சிவில் சட்டம்) & பிரிவு 48A (சுற்றுச்சூழல் பாதுகாப்பு)"),
        ("Article 38 (Minimising inequalities) & Article 39(d) (Equal pay for equal work)", "பிரிவு 38 (ஏற்றத்தாழ்வுகளைக் குறைத்தல்) & பிரிவு 39(d) (சம வேலைக்கு சம ஊதியம்)")
    ],
    "A",
    "Correct Answer: Option A. Gandhian Principles reflect Gandhi's ideology of rural reconstruction and cottage industries. They include Article 40 (Panchayats), Article 43 (Cottage industries), Article 43B (Co-operatives), Article 46 (Educational interests of SC/ST), Article 47 (Prohibition of liquor), and Article 48 (Prohibition of slaughter of cows).",
    "சரியான பதில்: விருப்பம் A. காந்தியக் கோட்பாடுகள் காந்தியின் கிராமப்புற சீரமைப்பு தத்துவத்தைப் பிரதிபலிக்கின்றன. பிரிவு 40, 43, 43B, 46, 47 (மதுவிலக்கு) மற்றும் 48 (பசு வதை தடை) ஆகியவை இதில் அடங்கும்.",
    {
        "A": ("Correct. Articles 40 and 47 (prohibition) are classic Gandhian Directives.", "சரி. பிரிவுகள் 40 மற்றும் 47 (மதுவிலக்கு) காந்திய நெறிமுறைகளாகும்."),
        "B": ("Incorrect. Articles 39A and 43A are Socialistic Principles.", "தவறு. பிரிவுகள் 39A மற்றும் 43A சோசலிசக் கோட்பாடுகளாகும்."),
        "C": ("Incorrect. Articles 44 and 48A are Liberal-Intellectual Principles.", "தவறு. பிரிவுகள் 44 மற்றும் 48A தாராளமய-அறிவுசார் கோட்பாடுகளாகும்."),
        "D": ("Incorrect. Articles 38 and 39(d) are Socialistic Principles.", "தவறு. பிரிவுகள் 38 மற்றும் 39(d) சோசலிசக் கோட்பாடுகளாகும்.")
    },
    "Classify DPSP carefully into 3 broad categories: 1. Socialistic (Art 38, 39, 39A, 41, 42, 43, 43A, 47 nutrition), 2. Gandhian (Art 40, 43, 43B, 46, 47 prohibition, 48 cow slaughter), 3. Liberal-Intellectual (Art 44, 45, 48, 48A, 49, 50, 51).",
    "DPSP-ஐ 3 பிரிவுகளாக வகைப்படுத்துங்கள்: 1. சோசலிசக் கோட்பாடுகள், 2. காந்தியக் கோட்பாடுகள், 3. தாராளமய-அறிவுசார் கோட்பாடுகள்.",
    "The Constitution itself does not contain any formal classification of DPSP; this tripartite classification is done by constitutional experts.",
    "அரசியலமைப்பில் DPSP வகைப்படுத்தப்படவில்லை; இந்த வகைப்பாடு அரசியலமைப்பு வல்லுநர்களால் செய்யப்பட்டது."
))

# Q14 (Hard, Type 5: Assertion & Reason, Answer: B)
q_data.append(make_q(
    "DPSP_R_014", "Hard", "Assertion & Reason",
    "Assertion (A): Article 50 directs the State to take steps to separate the judiciary from the executive in the public services of the State.\nReason (R): The Code of Criminal Procedure, 1973 (CrPC) effected a structural separation of judicial functions from Executive Magistrates by placing Judicial Magistrates under the direct control of the High Court.",
    "கூற்று (A): மாநிலத்தின் பொதுப்பணிகளில் நீதித்துறையை நிர்வாகத்துறையிலிருந்து பிரிக்க அரசு நடவடிக்கை எடுக்க வேண்டும் என பிரிவு 50 பணிக்கிறது.\nகாரணம் (R): குற்றவியல் நடைமுறைச் சட்டம், 1973 (CrPC) நீதித்துறை நடுவர்களை உயர்நீதிமன்றத்தின் நேரடிக் கட்டுப்பாட்டின் கீழ் கொண்டு வந்ததன் மூலம் நிர்வாக நடுவர்களிடமிருந்து நீதித்துறை பணிகளைப் பிரித்தது.",
    [
        ("Both A and R are correct and R is the correct explanation of A", "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்."),
        ("Both A and R are correct but R is NOT the correct explanation of A", "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல."),
        ("A is correct but R is incorrect", "A சரி, ஆனால் R தவறு."),
        ("A is incorrect but R is correct", "A தவறு, ஆனால் R சரி.")
    ],
    "B",
    "Both Assertion and Reason are true, but Reason is a statutory implementation of Article 50, not its conceptual explanation. Article 50 is a Liberal-Intellectual Directive aimed at ensuring judicial independence from executive influence. Parliament implemented this directive by revising the CrPC in 1973.",
    "கூற்று A மற்றும் காரணம் R இரண்டும் சரி, ஆனால் R என்பது A-வின் சட்டப்பூர்வ அமலாக்கமே தவிர அதன் கோட்பாட்டு விளக்கம் அல்ல. பிரிவு 50 நீதித்துறை சுதந்திரத்தை உறுதி செய்வதை நோக்கமாகக் கொண்டது.",
    {
        "A": ("Incorrect. CrPC 1973 is an executive/statutory implementation of Article 50, not the constitutional justification for why separation of powers is required.", "தவறு. CrPC 1973 என்பது பிரிவு 50-ன் சட்டப்பூர்வ அமலாக்கமே தவிர கோட்பாட்டு விளக்கம் அல்ல."),
        "B": ("Correct. Both statements are factually and constitutionally true, but R describes statutory implementation rather than logical derivation.", "சரி. இரண்டு கூற்றுகளும் உண்மையானவை, ஆனால் R அமலாக்கத்தை மட்டுமே விவரிக்கிறது."),
        "C": ("Incorrect. Reason is factually correct under CrPC 1973.", "தவறு. காரணம் CrPC 1973-ன் கீழ் சரியானது."),
        "D": ("Incorrect. Assertion is a direct text of Article 50.", "தவறு. கூற்று பிரிவு 50-ன் நேரடிப் உரையாகும்.")
    },
    "Separation of Judiciary from Executive (Article 50) protects rule of law and judicial independence, which is part of the Basic Structure.",
    "நீதித்துறையை நிர்வாகத்திலிருந்து பிரிப்பது (பிரிவு 50) சட்டத்தின் ஆட்சியையும் நீதித்துறை சுதந்திரத்தையும் பாதுகாக்கிறது.",
    "Prior to CrPC 1973, District Collectors and Executive Magistrates possessed both administrative and judicial trial powers.",
    "CrPC 1973-க்கு முன்பு, மாவட்ட ஆட்சியர்கள் நிர்வாக மற்றும் நீதித்துறை விசாரணை அதிகாரங்கள் இரண்டையும் கொண்டிருந்தனர்.",
    assertion_dict={"en": "Article 50 directs the State to separate judiciary from executive in public services.", "ta": "மாநிலத்தின் பொதுப்பணிகளில் நீதித்துறையை நிர்வாகத்துறையிலிருந்து பிரிக்க அரசு நடவடிக்கை எடுக்க வேண்டும் என பிரிவு 50 பணிக்கிறது."},
    reason_dict={"en": "CrPC 1973 created Judicial Magistrates under High Court control to perform judicial functions.", "ta": "CrPC 1973 உயர்நீதிமன்ற கட்டுப்பாட்டின் கீழ் நீதித்துறை நடுவர்களை உருவாக்கி நீதித்துறை பணிகளை வழங்கியது."}
))

# Q15 (Medium, Type 1: Situation/Application, Answer: C)
q_data.append(make_q(
    "DPSP_R_015", "Medium", "Reasoning",
    "SITUATION: A State government enacts a total statutory ban on the slaughter of cows, calves, and draft cattle of all ages to preserve agricultural animals and improve breeds.\n\nQUESTION: In State of Gujarat v. Mirzapur Moti Kureshi Kassab Jamat (2005), the Supreme Court upheld such a ban as a reasonable restriction on trade under Article 19(6) primarily by harmonising Fundamental Rights with which Directive Principle?",
    "சூழல்: வேளாண்மை மற்றும் கால்நடை வளர்ப்பைப் பாதுகாப்பதற்காக பசுக்கள், கன்றுகள் மற்றும் வேலைக் கால்நடைகளை வதை செய்ய மாநில அரசு முழுமையான சட்டப்பூர்வ தடை விதிக்கிறது.\n\nகேள்வி: மிர்சாபூர் மோதி குரேஷி (2005) வழக்கில், பிரிவு 19-ஐ எந்த அரசு நெறிமுறையுடன் இணைத்து இத்தடையை உச்சநீதிமன்றம் நியாயமான கட்டுப்பாடாக உறுதி செய்தது?",
    [
        ("Article 43", "பிரிவு 43"),
        ("Article 46", "பிரிவு 46"),
        ("Article 48", "பிரிவு 48"),
        ("Article 51", "பிரிவு 51")
    ],
    "C",
    "Correct Answer: Article 48. Article 48 directs the State to organise agriculture and animal husbandry on modern scientific lines and take steps for preserving and improving breeds, and prohibiting the slaughter of cows and calves and other milch and draught cattle.",
    "சரியான பதில்: பிரிவு 48. பிரிவு 48 வேளாண்மை மற்றும் கால்நடை வளர்ப்பை நவீன அறிவியல் முறையில் அமைக்கவும், பசுக்கள் மற்றும் கன்றுகளை வதை செய்வதைத் தடுக்கவும் அரசைப் பணிக்கிறது.",
    {
        "A": ("Incorrect. Article 43 deals with living wage and cottage industries.", "தவறு. பிரிவு 43 வாழ்வாதார ஊதியத்தைக் கையாள்கிறது."),
        "B": ("Incorrect. Article 46 deals with weaker sections education and economic interests.", "தவறு. பிரிவு 46 நலிவடைந்த பிரிவினரின் நலன்களைக் கையாள்கிறது."),
        "C": ("Correct. Article 48 specifically contains the directive prohibiting cow slaughter.", "சரி. பிரிவு 48 பசு வதைத் தடையை பிரத்யேகமாகக் கொண்டுள்ளது."),
        "D": ("Incorrect. Article 51 deals with international peace.", "தவறு. பிரிவு 51 சர்வதேச அமைதியைக் கையாள்கிறது.")
    },
    "Notice the shift in judicial approach: In 1958 (Quareshi case), SC allowed slaughter of aged cattle. But in 2005 (Mirzapur Moti Kureshi case), SC 7-judge bench upheld TOTAL ban under Article 48 & 48A.",
    "நீதிமன்ற அணுகுமுறை மாற்றத்தைக் கவனியுங்கள்: 1958-ல் வயது முதிர்ந்த கால்நடைகளை வதை செய்ய அனுமதிக்கப்பட்டது. ஆனால் 2005-ல் 7 நீதிபதிகள் அமர்வு பிரிவு 48 & 48A-ன் கீழ் முழுத் தடையை உறுதி செய்தது.",
    "Article 48 contains both Liberal-Intellectual (modern agriculture) and Gandhian (cow slaughter prohibition) elements.",
    "பிரிவு 48 தாராளமய மற்றும் காந்திய கூறுகள் இரண்டையும் கொண்டுள்ளது."
))

# Q16 (Easy-Medium, Type 2: Two-Statement Reasoning, Answer: D)
q_data.append(make_q(
    "DPSP_R_016", "Easy-Medium", "Reasoning",
    "Consider the following statements regarding Article 46:\n\n1. Article 46 directs the State to promote with special care the educational and economic interests of the weaker sections of the people, and in particular, of the Scheduled Castes and the Scheduled Tribes.\n2. Article 46 explicitly prohibits the State from implementing any reservation policies in educational institutions or public employment.\n\nWhich of the above statements is/are correct?",
    "பிரிவு 46 பற்றிய பின்வரும் கூற்றுகளை ஆராய்க:\n\n1. மக்கள் தொகையில் நலிவடைந்த பிரிவினர், குறிப்பாக பட்டியல் சாதியினர் மற்றும் பழங்குடியினரின் கல்வி மற்றும் பொருளாதார நலன்களை சிறப்பு கவனத்துடன் மேம்படுத்த பிரிவு 46 அரசைப் பணிக்கிறது.\n2. கல்வி நிறுவனங்கள் அல்லது பொது வேலைவாய்ப்பில் அரசு எவ்வித இடஒதுக்கீட்டுக் கொள்கையையும் அமல்படுத்துவதை பிரிவு 46 வெளிப்படையாகத் தடை செய்கிறது.\n\nமேற்கண்ட கூற்றுகளில் எது/எவை சரியானவை?",
    [
        ("2 only", "2 மட்டும்"),
        ("Both 1 and 2", "1 மற்றும் 2 இரண்டும்"),
        ("Neither 1 nor 2", "1 மற்றும் 2 இரண்டும் இல்லை"),
        ("1 only", "1 மட்டும்")
    ],
    "D",
    "Statement 1 is correct and Statement 2 is incorrect. Article 46 is a major Directive Principle supporting affirmative action and protective discrimination. Article 15(4) and Article 16(4) in Part III were enacted precisely to enable the State to fulfill Article 46 directives.",
    "கூற்று 1 சரி, கூற்று 2 தவறு. பிரிவு 46 இடஒதுக்கீடு மற்றும் பாதுகாப்புப் பாகுபாட்டிற்கு ஆதரவளிக்கும் முக்கிய நெறிமுறையாகும்.",
    {
        "A": ("Incorrect. Statement 2 is false as Article 46 promotes social justice and special measures.", "தவறு. கூற்று 2 தவறானது."),
        "B": ("Incorrect. Statement 2 is false.", "தவறு. கூற்று 2 தவறானது."),
        "C": ("Incorrect. Statement 1 is correct.", "தவறு. கூற்று 1 சரியானது."),
        "D": ("Correct. Statement 1 accurately states Article 46, while Statement 2 is false.", "சரி. கூற்று 1 பிரிவு 46-ஐ துல்லியமாகக் குறிப்பிடுகிறது, ஆனால் கூற்று 2 தவறானது.")
    },
    "In Champakam Dorairajan case (1951), SC struck down communal G.O. for lacking explicit Part III provision. Parliament immediately passed 1st Amendment Act 1951 inserting Article 15(4) to give effect to Article 46.",
    "செம்பகம் துரைராஜன் வழக்கில் (1951) வகுப்புவாத அரசாணை ரத்து செய்யப்பட்டது. அதற்குப் பின் 1-வது திருத்தச் சட்டம் 1951 மூலம் பிரிவு 46-ஐ நிறைவேற்ற பிரிவு 15(4) சேர்க்கப்பட்டது.",
    "Article 46 also instructs the State to protect SC/ST from social injustice and all forms of exploitation.",
    "பிரிவு 46 பட்டியல் சாதியினர்/பழங்குடியினரை சமூக அநீதியிலிருந்தும் சுரண்டலிலிருந்தும் பாதுகாக்க அரசைப் பணிக்கிறது."
))

# Q17 (Hard, Type 3: Three-Statement Reasoning, Answer: A)
q_data.append(make_q(
    "DPSP_R_017", "Hard", "Reasoning",
    "Consider the following statements regarding Article 38(2) inserted by the 44th Constitutional Amendment Act 1978:\n\n1. Article 38(2) directs the State to strive to minimise inequalities in income, and endeavour to eliminate inequalities in status, facilities, and opportunities.\n2. Article 38(2) mandates that this elimination of inequality applies not only amongst individuals but also amongst groups of people residing in different areas or engaged in different vocations.\n3. Article 38(2) was part of the original 1950 text of the Constitution of India drafted by the Constituent Assembly.\n\nWhich of the above statements are correct?",
    "1978-ம் ஆண்டின் 44-வது அரசியலமைப்பு திருத்தச் சட்டத்தால் சேர்க்கப்பட்ட பிரிவு 38(2) பற்றிய கூற்றுகளை ஆராய்க:\n\n1. வருமானத்தில் உள்ள ஏற்றத்தாழ்வுகளைக் குறைக்கவும், அந்தஸ்து, வசதிகள் மற்றும் வாய்ப்புகளில் உள்ள ஏற்றத்தாழ்வுகளை ஒழிக்கவும் அரசு முயல வேண்டும் என பிரிவு 38(2) பணிக்கிறது.\n2. இந்த ஏற்றத்தாழ்வு ஒழிப்பு தனிநபர்களுக்கு மட்டுமல்லாமல், வெவ்வேறு பகுதிகளில் வாழும் அல்லது வெவ்வேறு தொழில்களில் ஈடுபட்டுள்ள மக்கள் குழுக்களுக்கும் பொருந்தும் என பிரிவு 38(2) பணிக்கிறது.\n3. பிரிவு 38(2) என்பது 1950-ம் ஆண்டின் மூல அரசியலமைப்பிலேயே இடம்பெற்றிருந்த பிரிவாகும்.\n\nமேற்கண்ட கூற்றுகளில் எவை சரியானவை?",
    [
        ("1 and 2 only", "1 மற்றும் 2 மட்டும்"),
        ("2 and 3 only", "2 மற்றும் 3 மட்டும்"),
        ("1 and 3 only", "1 மற்றும் 3 மட்டும்"),
        ("1, 2 and 3", "1, 2 மற்றும் 3")
    ],
    "A",
    "Statements 1 and 2 are correct, but Statement 3 is incorrect. Article 38(2) was NOT part of the original 1950 Constitution; it was added by the 44th Constitutional Amendment Act in 1978.",
    "கூற்றுகள் 1 மற்றும் 2 சரியானவை, ஆனால் கூற்று 3 தவறானது. பிரிவு 38(2) 1950 மூல அரசியலமைப்பில் இல்லை; அது 1978-ல் 44-வது திருத்தச் சட்டத்தால் சேர்க்கப்பட்டது.",
    {
        "A": ("Correct. Statements 1 and 2 correctly capture the text of Article 38(2), while Statement 3 is wrong about its origin.", "சரி. கூற்றுகள் 1 மற்றும் 2 பிரிவு 38(2)-ன் உரையைச் சரியாகக் குறிப்பிடுகின்றன."),
        "B": ("Incorrect. Statement 3 is false.", "தவறு. கூற்று 3 தவறானது."),
        "C": ("Incorrect. Statement 3 is false.", "தவறு. கூற்று 3 தவறானது."),
        "D": ("Incorrect. Statement 3 is false.", "தவறு. கூற்று 3 தவறானது.")
    },
    "Note the distinction: Article 38(1) (social order for welfare) was in the original 1950 Constitution, but Article 38(2) (minimising income/status inequalities) was added by the 44th Amendment Act 1978.",
    "வேறுபாட்டைக் கவனியுங்கள்: பிரிவு 38(1) 1950 மூல அரசியலமைப்பில் இருந்தது, ஆனால் பிரிவு 38(2) 1978-ல் 44-வது திருத்தத்தால் சேர்க்கப்பட்டது.",
    "The 44th Amendment Act 1978 was enacted by the Janata Party Government headed by Morarji Desai.",
    "44-வது திருத்தச் சட்டம் 1978 மொரார்ஜி தேசாய் தலைமையிலான ஜனதா கட்சி அரசாங்கத்தால் இயற்றப்பட்டது."
))

# Q18 (Medium, Type 6: Situation → Constitutional Principle, Answer: B)
q_data.append(make_q(
    "DPSP_R_018", "Medium", "Reasoning",
    "SITUATION: India signs an international treaty on climate control and maritime law, committing to foster respect for international law and treaty obligations, and to encourage settlement of international disputes by arbitration.\n\nQUESTION: Which Directive Principle of State Policy under Article 51 explicitly embodies these principles of international peace and security?",
    "சூழல்: காலநிலை மாற்றம் மற்றும் கடல்சார் சட்டம் தொடர்பான சர்வதேச ஒப்பந்தத்தில் இந்தியா கையெழுத்திடுகிறது, இது சர்வதேச சட்டத்தை மதிப்பது மற்றும் சர்வதேச தகராறுகளை மத்தியஸ்தம் மூலம் தீர்ப்பதை ஊக்குவிப்பதை நோக்கமாகக் கொண்டுள்ளது.\n\nகேள்வி: சர்வதேச அமைதி மற்றும் பாதுகாப்பிற்கான இந்த நெறிமுறைகளை வெளிப்படுத்தும் பிரிவு 51-ன் கீழ் உள்ள அரசு நெறிமுறை எது?",
    [
        ("Article 49", "பிரிவு 49"),
        ("Article 51", "பிரிவு 51"),
        ("Article 48A", "பிரிவு 48A"),
        ("Article 37", "பிரிவு 37")
    ],
    "B",
    "Correct Answer: Article 51. Article 51 directs the State to: (a) promote international peace and security, (b) maintain just and honourable relations between nations, (c) foster respect for international law and treaty obligations, and (d) encourage settlement of international disputes by arbitration.",
    "சரியான பதில்: பிரிவு 51. பிரிவு 51: சர்வதேச அமைதியைப் பேணவும், நாடுகளுக்கிடையே நியாயமான உறவுகளைப் பராமரிக்கவும், சர்வதேச சட்டத்தை மதிக்கவும், தகராறுகளை மத்தியஸ்தம் மூலம் தீர்க்கவும் அரசைப் பணிக்கிறது.",
    {
        "A": ("Incorrect. Article 49 deals with protection of monuments and places of national importance.", "தவறு. பிரிவு 49 தேசிய முக்கியத்துவம் வாய்ந்த சின்னங்களைப் பாதுகாப்பதைக் கையாள்கிறது."),
        "B": ("Correct. Article 51 contains the explicit constitutional directive for international peace and treaties.", "சரி. பிரிவு 51 சர்வதேச அமைதி மற்றும் ஒப்பந்தங்களுக்கான நேரடி நெறிமுறையைக் கொண்டுள்ளது."),
        "C": ("Incorrect. Article 48A deals with environment and wildlife protection.", "தவறு. பிரிவு 48A சுற்றுச்சூழல் பாதுகாப்பைக் கையாள்கிறது."),
        "D": ("Incorrect. Article 37 deals with non-justiciability of DPSP.", "தவறு. பிரிவு 37 நெறிமுறைகளின் அமலாக்கத்தன்மையைக் கையாள்கிறது.")
    },
    "Article 51 is the LAST Directive Principle in Part IV (Articles 36 to 51). It forms the constitutional basis of India's Foreign Policy.",
    "பிரிவு 51 என்பது பகுதி IV-ல் உள்ள கடைசி நெறிமுறையாகும் (பிரிவுகள் 36 முதல் 51). இது இந்தியாவின் வெளியுறவுக் கொள்கையின் அரசியலமைப்பு அடிப்படையாகும்.",
    "Directive Principles under Article 51 are classified under Liberal-Intellectual Principles.",
    "பிரிவு 51-ன் கீழ் உள்ள நெறிமுறைகள் தாராளமய-அறிவுசார் கோட்பாடுகளின் கீழ் வகைப்படுத்தப்பட்டுள்ளன."
))

# Q19 (Hard, Type 5: Assertion & Reason, Answer: C)
q_data.append(make_q(
    "DPSP_R_019", "Hard", "Assertion & Reason",
    "Assertion (A): Laws enacted by Parliament to implement the Directive Principles contained in Article 39(b) and Article 39(c) cannot be declared void on the ground that they violate Fundamental Rights under Article 14 or Article 19.\nReason (R): In Kesavananda Bharati case (1973), the Supreme Court completely invalidated Article 31C in its entirety and held that no Directive Principle can ever override any Fundamental Right.",
    "கூற்று (A): பிரிவு 39(b) மற்றும் 39(c) நெறிமுறைகளை அமல்படுத்த இயற்றப்படும் சட்டங்கள் பிரிவு 14 அல்லது 19-ஐ மீறுகின்றன என்ற அடிப்படையில் செல்லாது என அறிவிக்க முடியாது.\nகாரணம் (R): கேசவாநந்த பாரதி வழக்கில் (1973) உச்சநீதிமன்றம் பிரிவு 31C முழுவதையும் ரத்து செய்து, எந்தவொரு நெறிமுறையும் அடிப்படை உரிமையை மீற முடியாது எனத் தீர்ப்பளித்தது.",
    [
        ("Both A and R are correct and R is the correct explanation of A", "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்."),
        ("Both A and R are correct but R is NOT the correct explanation of A", "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல."),
        ("A is correct but R is incorrect", "A சரி, ஆனால் R தவறு."),
        ("A is incorrect but R is correct", "A தவறு, ஆனால் R சரி.")
    ],
    "C",
    "Assertion (A) is correct and Reason (R) is incorrect. In Kesavananda Bharati (1973), the Supreme Court UPHELD the first part of Article 31C (protecting laws giving effect to Article 39(b) & (c) from Articles 14, 19, and 31). The SC struck down ONLY the second part of Article 31C which excluded judicial review.",
    "கூற்று A சரி, காரணம் R தவறு. கேசவாநந்த பாரதி வழக்கில் (1973) உச்சநீதிமன்றம் பிரிவு 31C-ன் முதல் பகுதியை (பிரிவு 39(b) & (c)-ஐப் பாதுகாக்கும் பகுதி) உறுதி செய்தது.",
    {
        "A": ("Incorrect. Reason is false because Kesavananda Bharati upheld the 1st clause of Article 31C.", "தவறு. கேசவாநந்த பாரதி வழக்கு பிரிவு 31C-ன் 1-வது பகுதியை உறுதி செய்ததால் காரணம் தவறானது."),
        "B": ("Incorrect. Reason is factually false.", "தவறு. காரணம் தவறானது."),
        "C": ("Correct. Assertion is true under Article 31C; Reason is false because only the 2nd part of Art 31C was struck down.", "சரி. பிரிவு 31C-ன் கீழ் கூற்று உண்மை; காரணம் தவறு ஏனெனில் 2-வது பகுதி மட்டுமே ரத்து செய்யப்பட்டது."),
        "D": ("Incorrect. Assertion is true.", "தவறு. கூற்று சரியானது.")
    },
    "Understand the famous dictum: 'Where Article 31C comes in, Article 14 goes out' (restricted strictly to laws implementing Article 39(b) and 39(c)).",
    "புகழ்பெற்ற பொன்மொழியைப் புரிந்து கொள்ளுங்கள்: 'எங்கு பிரிவு 31C வருகிறதோ, அங்கு பிரிவு 14 வெளியேறுகிறது' (பிரிவு 39(b) மற்றும் 39(c)-க்கு மட்டுமே பொருந்தும்).",
    "Article 31C was inserted into the Constitution by the 25th Constitutional Amendment Act 1971.",
    "பிரிவு 31C 1971-ல் 25-வது அரசியலமைப்பு திருத்தச் சட்டத்தால் அரசியலமைப்பில் சேர்க்கப்பட்டது.",
    assertion_dict={"en": "Laws enacted to implement Art 39(b) and 39(c) cannot be declared void for violating Art 14 or 19.", "ta": "பிரிவு 39(b) மற்றும் 39(c)-ஐ அமல்படுத்த இயற்றப்படும் சட்டங்கள் பிரிவு 14 அல்லது 19-ஐ மீறுகின்றன என செல்லாது என அறிவிக்க முடியாது."},
    reason_dict={"en": "In Kesavananda Bharati (1973), the SC completely invalidated Article 31C in its entirety.", "ta": "கேசவாநந்த பாரதி வழக்கில் (1973) உச்சநீதிமன்றம் பிரிவு 31C முழுவதையும் ரத்து செய்தது."}
))

# Q20 (Medium, Type 1: Situation/Application, Answer: D)
q_data.append(make_q(
    "DPSP_R_020", "Medium", "Reasoning",
    "SITUATION: An ancient fort complex of historic and national importance is facing severe structural damage and disfigurement due to unauthorized quarrying and commercial encroachment nearby.\n\nQUESTION: Under which Directive Principle of State Policy is the State under an obligation to protect every monument, place, or object of artistic or historic interest from spoliation or destruction?",
    "சூழல்: தேசிய முக்கியத்துவம் வாய்ந்த பழங்காலக் கோட்டை வளாகம் அருகில் நடைபெறும் சட்டவிரோத கல் குவாரிப் பணிகளால் பலத்த சேதமடைந்து சிதைக்கப்படுகிறது.\n\nகேள்வி: வரலாற்று அல்லது கலைச் சிறப்புமிக்க ஒவ்வொரு சின்னத்தையும் இடத்தையும் பாதுகாப்பது அரசின் கடமை எனக் கூறும் அரசு நெறிமுறைப் பிரிவு எது?",
    [
        ("Article 47", "பிரிவு 47"),
        ("Article 48", "பிரிவு 48"),
        ("Article 48A", "பிரிவு 48A"),
        ("Article 49", "பிரிவு 49")
    ],
    "D",
    "Correct Answer: Article 49. Article 49 states: 'It shall be the obligation of the State to protect every monument or place or object of artistic or historic interest, declared by or under law made by Parliament to be of national importance, from spoliation, disfigurement, destruction, removal, disposal or export.'",
    "சரியான பதில்: பிரிவு 49. பிரிவு 49: நாடாளுமன்றச் சட்டத்தால் தேசிய முக்கியத்துவம் வாய்ந்தது என அறிவிக்கப்பட்ட வரலாற்று அல்லது கலைச் சிறப்புமிக்க ஒவ்வொரு சின்னத்தையும் இடத்தையும் சேதத்திலிருந்தும் அழிவிலிருந்தும் பாதுகாப்பது அரசின் கடமை எனக் கூறுகிறது.",
    {
        "A": ("Incorrect. Article 47 deals with public health, nutrition, and prohibition.", "தவறு. பிரிவு 47 பொது சுகாதாரத்தைக் கையாள்கிறது."),
        "B": ("Incorrect. Article 48 deals with agriculture and animal husbandry.", "தவறு. பிரிவு 48 வேளாண்மை மற்றும் கால்நடை வளர்ப்பைக் கையாள்கிறது."),
        "C": ("Incorrect. Article 48A deals with environment, forests, and wildlife.", "தவறு. பிரிவு 48A சுற்றுச்சூழல் மற்றும் வனவிலங்குகளைக் கையாள்கிறது."),
        "D": ("Correct. Article 49 specifically mandates protection of monuments and historic places.", "சரி. பிரிவு 49 வரலாற்றுச் சின்னங்கள் மற்றும் இடங்களைப் பாதுகாப்பதை பிரத்யேகமாகப் பணிக்கிறது.")
    },
    "Do not confuse Article 48A (Protection of environment, forests & wildlife) with Article 49 (Protection of monuments, places & objects of national importance).",
    "பிரிவு 48A (சுற்றுச்சூழல் & வனவிலங்கு பாதுகாப்பு) மற்றும் பிரிவு 49 (தேசிய வரலாற்றுச் சின்னங்கள் பாதுகாப்பு) ஆகியவற்றை குழப்பிக் கொள்ளக் கூடாது.",
    "Ancient Monuments and Archaeological Sites and Remains Act 1958 was passed to implement Article 49.",
    "பிரிவு 49-ஐ அமல்படுத்த பழங்காலச் சின்னங்கள் மற்றும் தொல்பொருள் இடங்கள் சட்டம் 1958 இயற்றப்பட்டது."
))

# Q21 (Hard, Type 2: Two-Statement Reasoning, Answer: A)
q_data.append(make_q(
    "DPSP_R_021", "Hard", "Reasoning",
    "Consider the following statements regarding Article 43B:\n\n1. Article 43B was inserted into Part IV by the 97th Constitutional Amendment Act 2011 to direct the State to promote voluntary formation, autonomous functioning, democratic control, and professional management of co-operative societies.\n2. Article 43B was part of the original 1950 Constitution of India drafted under the chairmanship of Dr. B.R. Ambedkar.\n\nWhich of the above statements is/are correct?",
    "பிரிவு 43B பற்றிய பின்வரும் கூற்றுகளை ஆராய்க:\n\n1. கூட்டுறவு சங்கங்களின் தன்னாட்சி, ஜனநாயகக் கட்டுப்பாடு மற்றும் தொழில்முறை மேலாண்மையை ஊக்குவிக்க 2011-ம் ஆண்டின் 97-வது திருத்தச் சட்டத்தால் பிரிவு 43B பகுதி IV-ல் சேர்க்கப்பட்டது.\n2. பிரிவு 43B என்பது 1950-ம் ஆண்டின் மூல அரசியலமைப்பிலேயே சேர்க்கப்பட்ட பகுதியாகும்.\n\nமேற்கண்ட கூற்றுகளில் எது/எவை சரியானவை?",
    [
        ("1 only", "1 மட்டும்"),
        ("2 only", "2 மட்டும்"),
        ("Both 1 and 2", "1 மற்றும் 2 இரண்டும்"),
        ("Neither 1 nor 2", "1 மற்றும் 2 இரண்டும் இல்லை")
    ],
    "A",
    "Statement 1 is correct and Statement 2 is incorrect. Article 43B was NOT part of the original 1950 Constitution; it was added to Part IV by the 97th Constitutional Amendment Act 2011.",
    "கூற்று 1 சரி, கூற்று 2 தவறு. பிரிவு 43B 1950 மூல அரசியலமைப்பில் இல்லை; அது 2011-ல் 97-வது திருத்தச் சட்டத்தால் சேர்க்கப்பட்டது.",
    {
        "A": ("Correct. Statement 1 accurately describes Article 43B and its 97th Amendment origin, while Statement 2 is false.", "சரி. கூற்று 1 பிரிவு 43B மற்றும் அதன் 97-வது திருத்தத் தோற்றத்தைச் சரியாக விவரிக்கிறது."),
        "B": ("Incorrect. Statement 2 is false.", "தவறு. கூற்று 2 தவறானது."),
        "C": ("Incorrect. Statement 2 is false.", "தவறு. கூற்று 2 தவறானது."),
        "D": ("Incorrect. Statement 1 is correct.", "தவறு. கூற்று 1 சரியானது.")
    },
    "The 97th Amendment Act 2011 made three changes: 1. Made right to form co-operatives a Fundamental Right (Art 19(1)(c)), 2. Added DPSP for co-operatives (Art 43B), 3. Added Part IXB for Co-operative Societies.",
    "97-வது திருத்தம் 2011 மூன்று மாற்றங்களைச் செய்தது: 1. கூட்டுறவு சங்கம் அமைக்கும் உரிமை (பிரிவு 19(1)(c)), 2. நெறிமுறைப் பிரிவு (43B), 3. பகுதி IXB சேர்க்கப்பட்டது.",
    "In 2021, the Supreme Court struck down Part IXB in so far as it applied to state co-operative societies for lack of state ratification, but Article 43B as a Directive Principle remains valid.",
    "2021-ல் உச்சநீதிமன்றம் பகுதி IXB-ன் சில விதிகளை ரத்து செய்தது, ஆனால் நெறிமுறையான பிரிவு 43B செல்லுபடியாகும்."
))

# Q22 (Medium, Type 3: Three-Statement Reasoning, Answer: B)
q_data.append(make_q(
    "DPSP_R_022", "Medium", "Reasoning",
    "Consider the following statements highlighting the essential distinctions between Fundamental Rights (Part III) and Directive Principles (Part IV):\n\n1. Fundamental Rights operate as negative obligations prohibiting the State from taking certain actions, whereas Directive Principles operate as positive directives requiring the State to take specific policy measures.\n2. Fundamental Rights are justiciable in court, whereas Directive Principles are non-justiciable.\n3. Fundamental Rights aim at establishing political democracy, whereas Directive Principles aim at establishing social and economic democracy.\n\nWhich of the above statements are correct?",
    "அடிப்படை உரிமைகள் (பகுதி III) மற்றும் அரசு நெறிமுறைப்படுத்தும் கோட்பாடுகளுக்கு (பகுதி IV) இடையேயான வேறுபாடுகள் பற்றிய கூற்றுகளை ஆராய்க:\n\n1. அடிப்படை உரிமைகள் எதிர்மறை கடமைகள், ஆனால் நெறிமுறைக் கோட்பாடுகள் அரசு நடவடிக்கை எடுக்கப் பணிக்கும் நேர்மறை நெறிமுறைகள்.\n2. அடிப்படை உரிமைகள் நீதிமன்றத்தால் அமல்படுத்தக்கூடியவை, ஆனால் நெறிமுறைக் கோட்பாடுகள் நீதிமன்றத்தால் அமல்படுத்த முடியாதவை.\n3. அடிப்படை உரிமைகள் அரசியல் ஜனநாயகத்தை நிறுவ முயல்கின்றன, ஆனால் நெறிமுறைக் கோட்பாடுகள் சமூக மற்றும் பொருளாதார ஜனநாயகத்தை நிறுவ முயல்கின்றன.\n\nமேற்கண்ட கூற்றுகளில் எவை சரியானவை?",
    [
        ("1 and 2 only", "1 மற்றும் 2 மட்டும்"),
        ("1, 2 and 3", "1, 2 மற்றும் 3"),
        ("2 and 3 only", "2 மற்றும் 3 மட்டும்"),
        ("1 and 3 only", "1 மற்றும் 3 மட்டும்")
    ],
    "B",
    "Correct Answer: 1, 2 and 3. All three statements accurately state the classic constitutional distinctions between Fundamental Rights and Directive Principles of State Policy.",
    "சரியான பதில்: 1, 2 மற்றும் 3. அடிப்படை உரிமைகள் மற்றும் அரசு நெறிமுறைப்படுத்தும் கோட்பாடுகளுக்கு இடையேயான மூன்று முக்கிய அரசியலமைப்பு வேறுபாடுகளும் சரியானவை.",
    {
        "A": ("Incorrect. Statement 3 is also correct regarding political vs social-economic democracy.", "தவறு. கூற்று 3-ம் சரியானது."),
        "B": ("Correct. All three statements represent fundamental comparative doctrines of constitutional law.", "சரி. மூன்று கூற்றுகளும் அரசியலமைப்புச் சட்டத்தின் அடிப்படை ஒப்பீட்டுக் கோட்பாடுகளைப் பிரதிபலிக்கின்றன."),
        "C": ("Incorrect. Statement 1 is also correct.", "தவறு. கூற்று 1-ம் சரியானது."),
        "D": ("Incorrect. Statement 2 is also correct.", "தவறு. கூற்று 2-ம் சரியானது.")
    },
    "Remember the core vision: Part III (Fundamental Rights) creates Political Democracy; Part IV (Directive Principles) creates Social and Economic Democracy, forming a Welfare State.",
    "முக்கிய பார்வையை நினைவில் கொள்க: பகுதி III அரசியல் ஜனநாயகத்தையும்; பகுதி IV சமூக மற்றும் பொருளாதார ஜனநாயகத்தையும் (நல அரசு) உருவாக்குகின்றன.",
    "Sir B.N. Rau (Constitutional Advisor) recommended dividing individual rights into two categories: justiciable (Part III) and non-justiciable (Part IV).",
    "சர் பி.என். ராவ் உரிமைகளை இரண்டு வகைகளாகப் பிரிக்க பரிந்துரைத்தார்: அமல்படுத்தக்கூடியவை (பகுதி III) மற்றும் அமல்படுத்த முடியாதவை (பகுதி IV)."
))

# Q23 (Medium, Type 4: Correct/Incorrect, Answer: C)
q_data.append(make_q(
    "DPSP_R_023", "Medium", "Reasoning",
    "Which of the following statements is **INCORRECT** regarding Article 47 of the Constitution of India?",
    "இந்திய அரசியலமைப்பின் பிரிவு 47 குறித்து பின்வருவனவற்றில் எது **தவறானது**?",
    [
        ("Article 47 imposes a primary duty on the State to raise the level of nutrition and the standard of living of its people and the improvement of public health.", "மக்களின் ஊட்டச்சத்து நிலை, வாழ்க்கைத்தரம் மற்றும் பொது சுகாதாரத்தை உயர்த்துவது அரசின் முதன்மைக் கடமை என பிரிவு 47 விதிக்கிறது."),
        ("In State of Bombay v. F.N. Balsara (1951), the Supreme Court upheld statutory liquor prohibition as a reasonable restriction under Article 19(6) based on Article 47 directive.", "பால்சாரா (1951) வழக்கில், பிரிவு 47 நெறிமுறையின் அடிப்படையில் சட்டப்பூர்வ மதுவிலக்கை பிரிவு 19(6)-ன் கீழ் நியாயமான கட்டுப்பாடாக உச்சநீதிமன்றம் உறுதி செய்தது."),
        ("Article 47 grants an enforceable fundamental right to every citizen to file a writ petition demanding immediate total prohibition of medicinal liquor containing alcohol.", "மதுபானம் அடங்கிய மருத்துவப் பொருட்களுக்கு உடனடியாக முழுத் தடை கோரி வழக்கு தொடர பிரிவு 47 ஒவ்வொரு குடிமகனுக்கும் அமல்படுத்தக்கூடிய அடிப்படை உரிமையை வழங்குகிறது."),
        ("Article 47 explicitly instructs the State to endeavour to bring about prohibition of the consumption except for medicinal purposes of intoxicating drinks and of drugs harmful to health.", "மருத்துவ நோக்கங்களைத் தவிர ஆரோக்கியத்திற்கு தீங்கு விளைவிக்கும் மதுபானங்கள் மற்றும் போதைமருந்துகளைப் பயன்படுத்துவததைத் தடுக்க அரசு முயல வேண்டும் என பிரிவு 47 பணிக்கிறது.")
    ],
    "C",
    "Statement C is INCORRECT (and therefore the correct answer). Article 47 is a non-justiciable Directive Principle in Part IV, not an enforceable Fundamental Right. Citizens cannot file a writ petition demanding immediate total prohibition of medicinal alcohol.",
    "கூற்று C தவறானது (எனவே இதுவே சரியான பதில்). பிரிவு 47 நீதிமன்றத்தால் அமல்படுத்த முடியாத பகுதி IV நெறிமுறையாகும், அது அமல்படுத்தக்கூடிய அடிப்படை உரிமை அல்ல.",
    {
        "A": ("Incorrect statement choice (Factually True). Article 47 primary duties include nutrition and public health.", "தவறான விருப்பத் தேர்வு (உண்மையில் சரி). பிரிவு 47 ஊட்டச்சத்து மற்றும் பொது சுகாதாரத்தை உள்ளடக்கியது."),
        "B": ("Incorrect statement choice (Factually True). F.N. Balsara (1951) upheld prohibition under Article 47.", "தவறான விருப்பத் தேர்வு (உண்மையில் சரி). பால்சாரா வழக்கு மதுவிலக்கை உறுதி செய்தது."),
        "C": ("Correct Answer. Statement C falsely claims Article 47 is an enforceable Fundamental Right.", "சரியான பதில். கூற்று C பிரிவு 47-ஐ அமல்படுத்தக்கூடிய அடிப்படை உரிமை எனக் கூறுவது தவறானது."),
        "D": ("Incorrect statement choice (Factually True). Article 47 permits alcohol consumption strictly for medicinal purposes.", "தவறான விருப்பத் தேர்வு (உண்மையில் சரி). பிரிவு 47 மருத்துவ நோக்கங்களுக்கு மட்டுமே மதுவை அனுமதிக்கிறது.")
    },
    "Notice the exception in Article 47: Prohibition of intoxicating drinks and harmful drugs applies EXCEPT for medicinal purposes.",
    "பிரிவு 47-ல் உள்ள விலக்கைக் கவனியுங்கள்: மருத்துவ நோக்கங்களைத் தவிர மற்ற பயன்பாட்டிற்கு மதுவிலக்கு பொருந்தும்.",
    "Article 47 incorporates both Socialistic (nutrition, public health) and Gandhian (liquor prohibition) directive aspects.",
    "பிரிவு 47 சோசலிச மற்றும் காந்திய அம்சங்கள் இரண்டையும் உள்ளடக்கியது."
))

# Q24 (Hard, Type 6: Situation → Constitutional Principle, Answer: D)
q_data.append(make_q(
    "DPSP_R_024", "Hard", "Reasoning",
    "SITUATION: Children below the age of 14 are subjected to hazardous forced labor in brick kilns and match factories, depriving them of health, dignity, and education.\n\nQUESTION: In Bandhua Mukti Morcha v. Union of India (1984), the Supreme Court ruled that the Fundamental Right to live with human dignity under Article 21 derives its life breath from which Directive Principles guarding childhood and worker health?",
    "சூழல்: 14 வயதிற்குட்பட்ட குழந்தைகள் செங்கல் சூளைகள் மற்றும் தீப்பெட்டித் தொழிற்சாலைகளில் ஆபத்தான கட்டாய வேலைக்கு உட்படுத்தப்பட்டு ஆரோக்கியம் மற்றும் கல்வியை இழக்கின்றனர்.\n\nகேள்வி: பந்துவா முக்தி மோர்ச்சா (1984) வழக்கில், பிரிவு 21-ன் கீழ் கண்ணியமான வாழ்வுரிமை எந்த அரசு நெறிமுறைகளிலிருந்து உயிர் பெறுகிறது என உச்சநீதிமன்றம் தீர்ப்பளித்தது?",
    [
        ("Article 38(2) & Article 40", "பிரிவு 38(2) & பிரிவு 40"),
        ("Article 43B & Article 44", "பிரிவு 43B & பிரிவு 44"),
        ("Article 48 & Article 50", "பிரிவு 48 & பிரிவு 50"),
        ("Article 39(e) & Article 39(f)", "பிரிவு 39(e) & பிரிவு 39(f)")
    ],
    "D",
    "Correct Answer: Article 39(e) & Article 39(f). In Bandhua Mukti Morcha (1984), Justice P.N. Bhagwati held that the right to live with human dignity enshrined in Article 21 must derive its life breath from the Directive Principles, particularly Articles 39(e) and 39(f) protecting health of workers and childhood against exploitation.",
    "சரியான பதில்: பிரிவு 39(e) & பிரிவு 39(f). பந்துவா முக்தி மோர்ச்சா (1984) வழக்கில், பிரிவு 21-ன் கீழ் கண்ணியமான வாழ்வுரிமை தொழிலாளர் ஆரோக்கியம் மற்றும் குழந்தை பருவத்தைப் பாதுகாக்கும் பிரிவு 39(e) மற்றும் 39(f) நெறிமுறைகளிலிருந்தே உயிர் பெறுகிறது என உச்சநீதிமன்றம் தீர்ப்பளித்தது.",
    {
        "A": ("Incorrect. Article 38(2) deals with income inequality and Article 40 with Panchayats.", "தவறு. பிரிவு 38(2) வருமான ஏற்றத்தாழ்வைக் கையாள்கிறது."),
        "B": ("Incorrect. Article 43B deals with co-operatives and Article 44 with Uniform Civil Code.", "தவறு. பிரிவு 43B கூட்டுறவு சங்கங்களைக் கையாள்கிறது."),
        "C": ("Incorrect. Article 48 deals with agriculture and Article 50 with judiciary separation.", "தவறு. பிரிவு 48 வேளாண்மையைக் கையாள்கிறது."),
        "D": ("Correct. Articles 39(e) and 39(f) specifically safeguard worker health and prevent abuse of tender age of children.", "சரி. பிரிவுகள் 39(e) மற்றும் 39(f) தொழிலாளர் ஆரோக்கியத்தையும் குழந்தைகள் சுரண்டப்படுவதையும் தடுக்கின்றன.")
    },
    "Article 39(e) protects health and strength of workers and tender age of children from abuse, while Article 39(f) directs that children are given opportunities to develop in a healthy manner and protected against exploitation.",
    "பிரிவு 39(e) தொழிலாளர் ஆரோக்கியத்தையும் குழந்தைகளின் பிஞ்சு வயதையும் பாதுகாக்கிறது, பிரிவு 39(f) குழந்தைகள் ஆரோக்கியமாக வளர வாய்ப்புகளை அளிக்கிறது.",
    "Child Labour (Prohibition and Regulation) Act 1986 was enacted to fulfill Articles 24, 39(e), and 39(f).",
    "குழந்தைகள் தொழிலாளர் சட்டம் 1986 பிரிவுகள் 24, 39(e) மற்றும் 39(f)-ஐ நிறைவேற்ற இயற்றப்பட்டது."
))

# Q25 (Hard, Type 5: Assertion & Reason, Answer: D)
q_data.append(make_q(
    "DPSP_R_025", "Hard", "Assertion & Reason",
    "Assertion (A): The definition of 'the State' for Part IV (Directive Principles) is completely different and distinct from the definition of 'the State' used for Part III (Fundamental Rights) under Article 12.\nReason (R): Article 36 explicitly provides that unless the context otherwise requires, 'the State' in Part IV has the same meaning as defined in Part III under Article 12.",
    "கூற்று (A): பகுதி IV (DPSP)-க்கான 'அரசு' என்பதன் வரையறை, பிரிவு 12-ன் கீழ் பகுதி III (அடிப்படை உரிமைகள்)-க்கு பயன்படுத்தப்படும் 'அரசு' வரையறையிலிருந்து முற்றிலும் வேறுபட்டது.\nகாரணம் (R): பிரிவு 36, பகுதி IV-ல் உள்ள 'அரசு' என்பது பகுதி III (பிரிவு 12)-ல் உள்ள அதே பொருளைக் கொண்டது எனத் தெளிவாகக் குறிப்பிடுகிறது.",
    [
        ("Both A and R are correct and R is the correct explanation of A", "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்."),
        ("Both A and R are correct but R is NOT the correct explanation of A", "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல."),
        ("A is correct but R is incorrect", "A சரி, ஆனால் R தவறு."),
        ("A is incorrect but R is correct", "A தவறு, ஆனால் R சரி.")
    ],
    "D",
    "Assertion (A) is incorrect and Reason (R) is correct. Article 36 explicitly states: 'In this Part, unless the context otherwise requires, \"the State\" has the same meaning as in Part III.' Therefore, 'State' in Part IV includes the GOI, Parliament, State Governments, State Legislatures, and local/other authorities under Article 12.",
    "கூற்று A தவறு, காரணம் R சரி. பிரிவு 36: 'இப்பகுதியில் \"அரசு\" என்பது பகுதி III-ல் (பிரிவு 12) வரையறுக்கப்பட்டுள்ள அதே பொருளைக் கொண்டது' எனக் கூறுகிறது. எனவே 'அரசு' என்பதில் மத்திய, மாநில அரசுகள் மற்றும் உள்ளாட்சி அமைப்புகள் அடங்கும்.",
    {
        "A": ("Incorrect. Assertion is false because Part IV uses the EXACT same definition of State as Article 12 in Part III.", "தவறு. பகுதி IV பகுதி III-ன் அதே அரசு வரையறையைப் பயன்படுத்துவதால் கூற்று தவறானது."),
        "B": ("Incorrect. Assertion is factually wrong.", "தவறு. கூற்று தவறானது."),
        "C": ("Incorrect. Reason is factually correct as per Article 36.", "தவறு. காரணம் பிரிவு 36-ன் படி சரியானது."),
        "D": ("Correct. Assertion is false because Article 36 equates State definition to Article 12; Reason is true.", "சரி. பிரிவு 36 அரசு வரையறையை பிரிவு 12 உடன் சமன்படுத்துவதால் கூற்று தவறு; காரணம் சரி.")
    },
    "Remember the opening Articles of Part IV: Article 36 defines 'State' (by referencing Article 12), and Article 37 declares non-justiciability and fundamental nature in governance.",
    "பகுதி IV-ன் தொடக்கப் பிரிவுகளை நினைவில் கொள்க: பிரிவு 36 'அரசை' வரையறுக்கிறது (பிரிவு 12-ஐக் குறிப்பிட்டு), பிரிவு 37 ஆட்சியில் அதன் அடிப்படைத் தன்மையை அறிவிக்கிறது.",
    "Therefore, all Directive Principles are addressed to the Union Government, State Governments, Panchayats, Municipalities, and all public authorities.",
    "எனவே, அனைத்து அரசு நெறிமுறைப்படுத்தும் கோட்பாடுகளும் மத்திய, மாநில அரசுகள், பஞ்சாயத்துகள் மற்றும் நகராட்சிகளுக்கு வழங்கப்பட்ட அறிவுறுத்தல்களாகும்.",
    assertion_dict={"en": "Definition of 'State' for Part IV is completely different from definition of 'State' in Part III under Article 12.", "ta": "பகுதி IV-க்கான 'அரசு' வரையறை, பிரிவு 12-ன் கீழ் பகுதி III-க்கான 'அரசு' வரையறையிலிருந்து முற்றிலும் வேறுபட்டது."},
    reason_dict={"en": "Article 36 explicitly provides that 'the State' in Part IV has the same meaning as defined in Article 12.", "ta": "பிரிவு 36, பகுதி IV-ல் உள்ள 'அரசு' என்பது பிரிவு 12-ல் வரையறுக்கப்பட்டுள்ள அதே பொருளைக் கொண்டது எனக் குறிப்பிடுகிறது."}
))

out_path_1 = 'data/questions/polity/directive_principles_reasoning.json'
out_path_2 = 'data/questions/polity/directive_principles_assertion_reason.json'

os.makedirs(os.path.dirname(out_path_1), exist_ok=True)

with open(out_path_1, 'w', encoding='utf-8') as f:
    json.dump(q_data, f, ensure_ascii=False, indent=2)

with open(out_path_2, 'w', encoding='utf-8') as f:
    json.dump(q_data, f, ensure_ascii=False, indent=2)

print(f"Successfully generated {len(q_data)} questions in {out_path_1} and {out_path_2}.")
