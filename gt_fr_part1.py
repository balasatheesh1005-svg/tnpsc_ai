# gt_fr_part1.py
# Questions 1 to 35: Articles 12 - 18 (Definition of State, Article 13, Equality Rights, Reservations, Untouchability, Titles)

def get_part1_questions():
    questions = [
        # Q1: Direct MCQ - Art 12 State definition
        {
            "id": "FR_GT_001",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Easy",
            "question_type": "Direct MCQ",
            "question": {
                "en": "Which of the following is explicitly included in the definition of 'State' under Article 12 of the Constitution of India?",
                "ta": "இந்திய அரசியலமைப்பின் 12-வது பிரிவின் கீழ் 'அரசு' என்ற வரையறையில் பின்வருவனவற்றுள் எது வெளிப்படையாகச் சேர்க்கப்பட்டுள்ளது?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "Government and Parliament of India",
                    "ta": "இந்திய அரசும் நாடாளுமன்றமும்"
                },
                {
                    "id": "B",
                    "en": "Only the Supreme Court and High Courts acting judicially",
                    "ta": "நீதித்துறை பணிகளைச் செய்யும் உச்ச நீதிமன்றம் மற்றும் உயர் நீதிமன்றங்கள் மட்டுமே"
                },
                {
                    "id": "C",
                    "en": "Private educational institutions receiving no government aid",
                    "ta": "அரசு உதவி பெறாத தனியார் கல்வி நிறுவனங்கள்"
                },
                {
                    "id": "D",
                    "en": "International non-governmental organizations operating in India",
                    "ta": "இந்தியாவில் செயல்படும் சர்வதேச அரசுசாரா அமைப்புகள்"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "Article 12 defines 'State' for Part III to include: (1) Executive and Legislative organs of Union Government, (2) Executive and Legislative organs of State Governments, (3) All local authorities, and (4) Other statutory or non-statutory authorities under the control of Government of India.",
                "ta": "பிரிவு 12 பகுதி III-க்காக 'அரசு' என்பதை வரையறுக்கிறது: (1) மத்திய அரசின் நிர்வாக மற்றும் சட்டமன்ற உறுப்புகள், (2) மாநில அரசுகளின் நிர்வாக மற்றும் சட்டமன்ற உறுப்புகள், (3) அனைத்து உள்ளாட்சி அமைப்புகள், (4) இந்திய அரசின் கட்டுப்பாட்டில் உள்ள பிற சட்டப்பூர்வ அல்லது சட்டப்பூர்வமற்ற அதிகார அமைப்புகள்."
            },
            "why_not_others": {
                "A": {"en": "Correct. Union Government and Parliament are explicitly named in Article 12.", "ta": "சரி. மத்திய அரசும் நாடாளுமன்றமும் பிரிவு 12-ல் வெளிப்படையாகக் குறிப்பிடப்பட்டுள்ளன."},
                "B": {"en": "Incorrect. Judiciary in its purely judicial capacity is generally excluded from Art 12 definition.", "ta": "தவறு. தூய நீதித்துறைப் பணியில் உள்ள நீதித்துறை பிரிவு 12-லிருந்து விலக்கப்பட்டுள்ளது."},
                "C": {"en": "Incorrect. Unaided private institutions without State control do not fall under Art 12.", "ta": "தவறு. அரசு கட்டுப்பாடற்ற உதவி பெறாத தனியார் நிறுவனங்கள் பிரிவு 12-ன் கீழ் வராது."},
                "D": {"en": "Incorrect. International NGOs are private bodies and not instrumentalities of the Indian State.", "ta": "தவறு. சர்வதேச அரசுசாரா அமைப்புகள் தனியார் அமைப்புகளாகும், அவை இந்திய அரசின் உறுப்புகள் அல்ல."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Trap: Article 12 specifically lists Government & Parliament of India, Government & Legislature of States, Local Authorities, and Other Authorities. Judiciary in non-judicial administrative duties can be State, but not in judicial decisions.",
                "ta": "TNPSC பொறி: பிரிவு 12 மத்திய அரசு, நாடாளுமன்றம், மாநில அரசு, சட்டமன்றம், உள்ளாட்சி மற்றும் பிற அதிகார அமைப்புகளைக் குறிப்பிடுகிறது. நீதித்துறையின் நிர்வாகப் பணிகள் 'அரசு' ஆகும், ஆனால் நீதித் தீர்ப்புகள் அல்ல."
            },
            "revision_fact": {
                "en": "Statutory bodies like LIC, ONGC, and SAIL are treated as 'State' under Article 12 under the agency/instrumentality test laid down in Ajay Hasia v. Khalid Mujib (1981).",
                "ta": "அஜய் ஹாசியா எதிர் காலித் முஜீப் (1981) வழக்கின்படி, எல்.ஐ.சி, ஓ.என்.ஜி.சி, சேல் போன்ற சட்டப்பூர்வ அமைப்புகள் பிரிவு 12-ன் கீழ் 'அரசு' எனக் கருதப்படுகின்றன."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity", "NCERT Class XI - Indian Constitution at Work"],
            "bloom_level": "Remember",
            "estimated_time_sec": 40,
            "pyq_similarity": "High",
            "tags": ["Polity", "Fundamental Rights", "Article 12", "Grand Test"]
        },

        # Q2: Conceptual MCQ - Doctrine of Eclipse
        {
            "id": "FR_GT_002",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Medium",
            "question_type": "Conceptual MCQ",
            "question": {
                "en": "The 'Doctrine of Eclipse' under Article 13(1) of the Indian Constitution implies that a pre-constitutional law inconsistent with a Fundamental Right:",
                "ta": "இந்திய அரசியலமைப்பின் 13(1) பிரிவின் கீழ் உள்ள 'மறைப்புக் கோட்பாடு' (Doctrine of Eclipse), அடிப்படை உரிமையுடன் முரண்படும் அரசியலமைப்புக்கு முந்தைய ஒரு சட்டத்தைப் பற்றி என்ன கூறுகிறது?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "Is completely dead and void ab initio for all past and future purposes",
                    "ta": "கடந்த கால மற்றும் எதிர்கால நோக்கங்களுக்காக ஆரம்பத்திலிருந்தே முற்றிலும் செல்லாததாகி இறந்துவிடுகிறது"
                },
                {
                    "id": "B",
                    "en": "Remains dormant and unenforceable against citizens, but can become active again if the relevant Fundamental Right is amended",
                    "ta": "குடிமக்களுக்கு எதிராகச் செயல்படாமல் முடங்கிக் கிடக்கும், ஆனால் தொடர்புடைய அடிப்படை உரிமை திருத்தப்பட்டால் மீண்டும் செயலுக்கு வரும்"
                },
                {
                    "id": "C",
                    "en": "Applies automatically to post-constitutional laws that violate Article 13(2)",
                    "ta": "பிரிவு 13(2)-ஐ மீறும் அரசியலமைப்புக்குப் பிந்தைய சட்டங்களுக்குத் தானாகவே பொருந்தும்"
                },
                {
                    "id": "D",
                    "en": "Can be declared constitutional only by a Special Majority of Parliament",
                    "ta": "நாடாளுமன்றத்தின் சிறப்பு பெரும்பான்மையால் மட்டுமே அரசியலமைப்புக்கு உட்பட்டதாக அறிவிக்க முடியும்"
                }
            ],
            "correct_answer": "B",
            "explanation": {
                "en": "Under Bhikaji Narain v. State of MP (1955), a pre-constitutional law inconsistent with FRs is not void ab initio; it remains in a dormant state overshadowed by the FR (eclipse). If the FR is amended to remove the shadow, the law becomes enforceable again.",
                "ta": "பிகாஜி நரேன் எதிர் மத்தியப் பிரதேச அரசு (1955) வழக்கின்படி, அரசியலமைப்புக்கு முந்தைய சட்டம் அடிப்படை உரிமையுடன் முரண்பட்டால் ஆரம்பத்திலிருந்தே செல்லாதது அல்ல; அது அடிப்படை உரிமையால் மறைக்கப்பட்டு முடங்கி இருக்கும். அத்தடை நீக்கப்பட்டால் அச்சட்டம் மீண்டும் செயலுக்கு வரும்."
            },
            "why_not_others": {
                "A": {"en": "Incorrect. Pre-constitutional laws are not dead ab initio; they remain valid for pre-1950 transactions.", "ta": "தவறு. அரசியலமைப்புக்கு முந்தைய சட்டங்கள் முற்றிலும் அழிவதில்லை; 1950-க்கு முந்தைய நிகழ்வுகளுக்கு அவை செல்லும்."},
                "B": {"en": "Correct. The law remains dormant and revives when the shadow of the FR is removed.", "ta": "சரி. சட்டம் முடங்கி இருக்கும், அடிப்படை உரிமை மறைப்பு நீங்கும்போது மீண்டும் உயிர்பெறும்."},
                "C": {"en": "Incorrect. Post-constitutional laws violating Art 13(2) are stillborn and void ab initio (Deep Chand case).", "ta": "தவறு. பிரிவு 13(2)-ஐ மீறும் அரசியலமைப்புக்குப் பிந்தைய சட்டங்கள் பிறப்பிலேயே செல்லாதவை."},
                "D": {"en": "Incorrect. Parliament cannot validate unconstitutional laws without constitutional amendment.", "ta": "தவறு. அரசியலமைப்புத் திருத்தமின்றி நாடாளுமன்றம் அரசியலமைப்பற்ற சட்டங்களைச் செல்லுபடியாக்கவும் முடியாது."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Trap: Doctrine of Eclipse applies primarily to pre-constitutional laws under Art 13(1). Post-constitutional laws violating Art 13(2) are void ab initio and cannot be revived by eclipse (Deep Chand v. State of UP).",
                "ta": "TNPSC பொறி: மறைப்புக் கோட்பாடு முக்கியமாக பிரிவு 13(1)-ன் கீழ் உள்ள அரசியலமைப்புக்கு முந்தைய சட்டங்களுக்கே பொருந்தும். பிரிவு 13(2)-ன் கீழ் உள்ள பிந்தைய சட்டங்கள் ஆரம்பத்திலிருந்தே செல்லாதவை."
            },
            "revision_fact": {
                "en": "Landmark Case: Bhikaji Narain v. State of MP (1955) formulated the Doctrine of Eclipse.",
                "ta": "முக்கிய வழக்கு: பிகாஜி நரேன் எதிர் மத்தியப் பிரதேச அரசு (1955) வழக்கு மறைப்புக் கோட்பாட்டை உருவாக்கியது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Understand",
            "estimated_time_sec": 50,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 13", "Doctrine of Eclipse", "Grand Test"]
        },

        # Q3: Statement-Based - Doctrine of Severability & Waiver
        {
            "id": "FR_GT_003",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Hard",
            "question_type": "Statement-Based",
            "question": {
                "en": "Consider the following statements regarding Article 13 and doctrines of judicial review:\n1. Under the Doctrine of Severability, if an invalid provision of a law can be separated from the valid portion, only the invalid portion is declared void.\n2. In Basheshar Nath v. CIT (1959), the Supreme Court ruled that a citizen can voluntarily waive their Fundamental Rights under Part III.\n3. Constitutional Amendment Acts under Article 368 were held NOT to be 'law' under Article 13(2) in the Kesavananda Bharati case.\nWhich of the statements given above is/are correct?",
                "ta": "பிரிவு 13 மற்றும் நீதித்துறை மறுஆய்வுக் கோட்பாடுகள் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. பிரிக்கக்கூடிய கோட்பாட்டின் (Doctrine of Severability) கீழ், ஒரு சட்டத்தின் செல்லாத பகுதியைச் செல்லுபடியாகும் பகுதியிலிருந்து பிரிக்க முடிந்தால், செல்லாத பகுதி மட்டுமே செல்லாது என அறிவிக்கப்படும்.\n2. பஷேஷர் நாத் எதிர் வருமான வரி ஆணையர் (1959) வழக்கில், ஒரு குடிமகன் தனது அடிப்படை உரிமைகளைத் தாமாகவே முன்வந்து துறக்க முடியும் (Waiver) என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது.\n3. கேசவாநந்த பாரதி வழக்கில் பிரிவு 368-ன் கீழ் செய்யப்படும் அரசியலமைப்புத் திருத்தச் சட்டங்கள் பிரிவு 13(2)-ன் கீழ் 'சட்டம்' அல்ல என்று தீர்ப்பளிக்கப்பட்டது.\nமேற்கூறிய கூற்றுகளில் எது/எவை சரியானவை?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "1 and 2 only",
                    "ta": "1 மற்றும் 2 மட்டுமே"
                },
                {
                    "id": "B",
                    "en": "1 and 3 only",
                    "ta": "1 மற்றும் 3 மட்டுமே"
                },
                {
                    "id": "C",
                    "en": "2 and 3 only",
                    "ta": "2 மற்றும் 3 மட்டுமே"
                },
                {
                    "id": "D",
                    "en": "1, 2 and 3",
                    "ta": "1, 2 மற்றும் 3"
                }
            ],
            "correct_answer": "B",
            "explanation": {
                "en": "Statement 1 is correct (R.M.D. Chamarbaugwalla case). Statement 2 is INCORRECT: In Basheshar Nath case (1959), SC held that a citizen CANNOT waive their Fundamental Rights, as they are mandatory public policy protections. Statement 3 is correct: Kesavananda Bharati (1973) held Constitutional Amendments under Art 368 are not 'law' under Art 13(2), though they cannot alter basic structure.",
                "ta": "கூற்று 1 சரி (R.M.D. சாமர்பாகவாலா வழக்கு). கூற்று 2 தவறு: பஷேஷர் நாத் வழக்கில் (1959) குடிமக்கள் தங்களது அடிப்படை உரிமைகளைத் துறக்க முடியாது என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது. கூற்று 3 சரி: கேசவாநந்த பாரதி வழக்கில் பிரிவு 368 திருத்தங்கள் பிரிவு 13(2)-ன் கீழ் 'சட்டம்' அல்ல என உறுதியானது."
            },
            "why_not_others": {
                "A": {"en": "Incorrect because statement 2 is false; FRs cannot be waived in India.", "ta": "தவறு, ஏனெனில் கூற்று 2 தவறானது; இந்தியாவில் அடிப்படை உரிமைகளைத் துறக்க முடியாது."},
                "B": {"en": "Correct. Statements 1 and 3 are factually correct, statement 2 is wrong.", "ta": "சரி. கூற்றுகள் 1 மற்றும் 3 சரியானவை, கூற்று 2 தவறானது."},
                "C": {"en": "Incorrect because statement 2 is false.", "ta": "தவறு, ஏனெனில் கூற்று 2 தவறானது."},
                "D": {"en": "Incorrect because statement 2 is false.", "ta": "தவறு, ஏனெனில் கூற்று 2 தவறானது."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Trap: Unlike the US Constitution where rights can be waived, in India, Fundamental Rights CANNOT be waived by any individual (Basheshar Nath case 1959).",
                "ta": "TNPSC பொறி: அமெரிக்க அரசியலமைப்பைப் போல் அல்லாமல், இந்தியாவில் எந்தவொரு நபரும் தனது அடிப்படை உரிமைகளைத் துறக்க முடியாது (பஷேஷர் நாத் வழக்கு 1959)."
            },
            "revision_fact": {
                "en": "24th Constitutional Amendment Act 1971 inserted Article 13(4), clarifying that Article 13 does not apply to constitutional amendments made under Article 368.",
                "ta": "1971-ன் 24-வது அரசியலமைப்புத் திருத்தச் சட்டம் பிரிவு 13(4)-ஐ இணைத்து, பிரிவு 368-ன் கீழ் செய்யப்படும் திருத்தங்களுக்குப் பிரிவு 13 பொருந்தாது என்பதைத் தெளிவுபடுத்தியது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Analyze",
            "estimated_time_sec": 65,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 13", "Severability", "Waiver", "Grand Test"]
        },

        # Q4: Conceptual MCQ - Equality before Law vs Equal Protection of Laws
        {
            "id": "FR_GT_004",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Medium",
            "question_type": "Conceptual MCQ",
            "question": {
                "en": "Which of the following correctly distinguishes 'Equality before Law' from 'Equal Protection of the Laws' under Article 14?",
                "ta": "பிரிவு 14-ன் கீழ் உள்ள 'சட்டத்தின் முன் சமம்' மற்றும் 'சட்டத்தின் சமமான பாதுகாப்பு' ஆகியவற்றை பின்வருவனவற்றுள் எது சரியாக வேறுபடுத்துகிறது?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "'Equality before Law' is a negative concept of British origin, whereas 'Equal Protection of Laws' is a positive concept of American origin",
                    "ta": "'சட்டத்தின் முன் சமம்' என்பது பிரிட்டிஷ் மூலத்தைக் கொண்ட எதிர்மறையான கருத்தாகும், அதேவேளையில் 'சட்டத்தின் சமமான பாதுகாப்பு' என்பது அமெரிக்க மூலத்தைக் கொண்ட நேர்மறையான கருத்தாகும்"
                },
                {
                    "id": "B",
                    "en": "'Equality before Law' allows affirmative action, whereas 'Equal Protection of Laws' forbids class legislation",
                    "ta": "'சட்டத்தின் முன் சமம்' நேர்மறை நடவடிக்கைகளை அனுமதிக்கிறது, ஆனால் 'சட்டத்தின் சமமான பாதுகாப்பு' வகுப்புவாத சட்டங்களைத் தடை செய்கிறது"
                },
                {
                    "id": "C",
                    "en": "'Equality before Law' applies only to foreigners, whereas 'Equal Protection of Laws' applies only to Indian citizens",
                    "ta": "'சட்டத்தின் முன் சமம்' வெளிநாட்டினருக்கு மட்டுமே பொருந்தும், ஆனால் 'சட்டத்தின் சமமான பாதுகாப்பு' இந்தியக் குடிமக்களுக்கு மட்டுமே பொருந்தும்"
                },
                {
                    "id": "D",
                    "en": "Both concepts are borrowed from the Irish Constitution and mean identical legal principles",
                    "ta": "இரண்டு கருத்துக்களும் அயர்லாந்து அரசியலமைப்பிலிருந்து பெறப்பட்டு ஒரே மாதிரியான சட்டக் கோட்பாடுகளைக் குறிக்கின்றன"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "'Equality before law' (British origin) implies absence of special privileges and equal subjection of all to ordinary law (negative concept). 'Equal protection of laws' (American origin - 14th Amendment) implies equal treatment under equal circumstances and permits reasonable classification (positive concept).",
                "ta": "'சட்டத்தின் முன் சமம்' (பிரிட்டிஷ்) என்பது சிறப்புச் சலுகைகள் இல்லாத நிலைக் குறிக்கும் எதிர்மறைக் கருத்தாகும். 'சட்டத்தின் சமமான பாதுகாப்பு' (அமெரிக்கா) என்பது சமமான சூழ்நிலைகளில் சமமான நடத்தையைக் குறிக்கும் நேர்மறைக் கருத்தாகும்."
            },
            "why_not_others": {
                "A": {"en": "Correct. Equality before law is British (negative) and Equal protection is American (positive).", "ta": "சரி. சட்டத்தின் முன் சமம் பிரிட்டிஷ் (எதிர்மறை), சமமான பாதுகாப்பு அமெரிக்கா (நேர்மறை)."},
                "B": {"en": "Incorrect. Equal protection of laws is what permits reasonable classification and affirmative action.", "ta": "தவறு. சட்டத்தின் சமமான பாதுகாப்பே நியாயமான பாகுபாட்டையும் நேர்மறை நடவடிக்கைகளையும் அனுமதிக்கிறது."},
                "C": {"en": "Incorrect. Both concepts under Article 14 apply to citizens and non-citizens alike.", "ta": "தவறு. பிரிவு 14-ன் இரு கருத்துக்களும் குடிமக்கள் மற்றும் வெளிநாட்டினர் இருவருக்கும் பொருந்தும்."},
                "D": {"en": "Incorrect. They are borrowed from UK and USA respectively, not Ireland.", "ta": "தவறு. அவை முறையே இங்கிலாந்து மற்றும் அமெரிக்காவிலிருந்து பெறப்பட்டவை."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: Article 14 applies to 'any person' (citizens, foreigners, legal persons like corporations). It embodies A.V. Dicey's Rule of Law.",
                "ta": "TNPSC குறிப்பு: பிரிவு 14 'எந்தவொரு நபருக்கும்' (குடிமக்கள், வெளிநாட்டினர், கார்ப்பரேஷன்கள்) பொருந்தும். இது ஏ.வி. டைசியின் சட்டத்தின் ஆட்சியைக் கொண்டுள்ளது."
            },
            "revision_fact": {
                "en": "The Supreme Court in E.P. Royappa v. State of Tamil Nadu (1974) introduced the 'New Doctrine of Equality' stating that equality is a dynamic concept and arbitrariness is antithetical to Article 14.",
                "ta": "ஈ.பி. ராயப்பா எதிர் தமிழ்நாடு அரசு (1974) வழக்கில் உச்ச நீதிமன்றம் 'புதிய சமத்துவக் கோட்பாட்டை' அறிமுகப்படுத்தியது, அதில் தன்னிச்சையான தன்மை பிரிவு 14-க்கு எதிரானது எனப்பட்டது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Understand",
            "estimated_time_sec": 45,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 14", "Equality", "Grand Test"]
        },

        # Q5: Direct MCQ - Exception to Rule of Law
        {
            "id": "FR_GT_005",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Easy",
            "question_type": "Direct MCQ",
            "question": {
                "en": "Which Article of the Constitution of India provides immunity to the President and State Governors from criminal proceedings during their term of office as an exception to Article 14?",
                "ta": "பிரிவு 14-க்கு விதிவிலக்காக, குடியரசுத் தலைவர் மற்றும் மாநில ஆளுநர்களுக்கு அவர்களது பதவிக் காலத்தில் குற்றவியல் நடவடிக்கைகளிலிருந்து விலக்களிக்கும் இந்திய அரசியலமைப்புப் பிரிவு எது?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "Article 361",
                    "ta": "பிரிவு 361"
                },
                {
                    "id": "B",
                    "en": "Article 368",
                    "ta": "பிரிவு 368"
                },
                {
                    "id": "C",
                    "en": "Article 356",
                    "ta": "பிரிவு 356"
                },
                {
                    "id": "D",
                    "en": "Article 300",
                    "ta": "பிரிவு 300"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "Article 361 provides constitutional immunity to the President and Governors: (1) Not answerable to any court for exercise of powers, (2) No criminal proceedings during term, (3) No process for arrest, (4) Civil proceedings require 2 months prior written notice.",
                "ta": "பிரிவு 361 குடியரசுத் தலைவர் மற்றும் ஆளுநர்களுக்குப் பாதுகாப்பு அளிக்கிறது: (1) நீதிமன்றங்களுக்குப் பதிலளிக்கத் தேவையில்லை, (2) பதவிக் காலத்தில் குற்றவியல் நடவடிக்கை இல்லை, (3) கைது செய்ய முடியாது, (4) உரிமையியல் நடவடிக்கைக்கு 2 மாத முன்அறிவிப்பு தேவை."
            },
            "why_not_others": {
                "A": {"en": "Correct. Article 361 grants official immunity to President and Governors.", "ta": "சரி. பிரிவு 361 குடியரசுத் தலைவர் மற்றும் ஆளுநர்களுக்கு அதிகாரப்பூர்வ விலக்களிக்கிறது."},
                "B": {"en": "Incorrect. Article 368 deals with Constitutional Amendment procedure.", "ta": "தவறு. பிரிவு 368 அரசியலமைப்புத் திருத்த நடைமுறை பற்றியது."},
                "C": {"en": "Incorrect. Article 356 deals with President's Rule in States.", "ta": "தவறு. பிரிவு 356 மாநிலங்களில் குடியரசுத் தலைவர் ஆட்சி பற்றியது."},
                "D": {"en": "Incorrect. Article 300 deals with Suits and Proceedings by/against Government.", "ta": "தவறு. பிரிவு 300 அரசுக்கு எதிரான வழக்கைக் கையாள்கிறது."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Trap: Civil proceedings CAN be instituted against President/Governor for personal acts during term, but ONLY after giving 2 months written notice (Art 361(4)). Criminal proceedings are completely barred.",
                "ta": "TNPSC பொறி: குடியரசுத் தலைவர்/ஆளுநர் மீது தனிப்பட்ட செயல்களுக்காக உரிமையியல் வழக்குத் தொடர 2 மாத முன்னறிவிப்பு கட்டாயம். குற்றவியல் வழக்குகள் முற்றிலும் தடை செய்யப்பட்டுள்ளன."
            },
            "revision_fact": {
                "en": "Article 31C is also an exception to Article 14: Laws saved under 31C (enforcing DPSP 39(b) and 39(c)) cannot be challenged for violating Article 14.",
                "ta": "பிரிவு 31C-யும் பிரிவு 14-க்கு விதிவிலக்காகும்: DPSP 39(b) மற்றும் 39(c)-ஐ செயல்படுத்தும் சட்டங்களை பிரிவு 14-ஐ மீறுகிறது எனச் சவால் செய்ய முடியாது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Remember",
            "estimated_time_sec": 35,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 14", "Article 361", "Grand Test"]
        },

        # Q6: Conceptual MCQ - Grounds of Non-Discrimination Art 15 vs Art 16
        {
            "id": "FR_GT_006",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Medium",
            "question_type": "Conceptual MCQ",
            "question": {
                "en": "Which two additional grounds of non-discrimination are included in Article 16(2) for public employment that are NOT present in Article 15(1)?",
                "ta": "பொது வேலைவாய்ப்பு தொடர்பான பிரிவு 16(2)-ல் பாகுபாடற்ற தன்மையைக் குறிக்கப் புதிதாகச் சேர்க்கப்பட்ட, ஆனால் பிரிவு 15(1)-ல் இல்லாத இரு கூடுதல் அடிப்படைகள் எவை?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "Descent and Residence",
                    "ta": "வம்சாவளி மற்றும் இருப்பிடம்"
                },
                {
                    "id": "B",
                    "en": "Caste and Sex",
                    "ta": "சாதி மற்றும் பாலினம்"
                },
                {
                    "id": "C",
                    "en": "Religion and Place of Birth",
                    "ta": "மதம் மற்றும் பிறந்த இடம்"
                },
                {
                    "id": "D",
                    "en": "Language and Race",
                    "ta": "மொழி மற்றும் இனக் குழு"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "Article 15(1) prohibits discrimination on 5 grounds ONLY: Religion, Race, Caste, Sex, Place of birth. Article 16(2) prohibits discrimination in public employment on 7 grounds: Religion, Race, Caste, Sex, Place of birth, DESCENT, and RESIDENCE.",
                "ta": "பிரிவு 15(1) 5 அடிப்படைகளில் மட்டுமே பாகுபாட்டைத் தடை செய்கிறது: மதம், இனம், சாதி, பாலினம், பிறந்த இடம். பிரிவு 16(2) பொது வேலைவாய்ப்பில் 7 அடிப்படைகளில் தடை செய்கிறது: மதம், இனம், சாதி, பாலினம், பிறந்த இடம், வம்சாவளி மற்றும் இருப்பிடம்."
            },
            "why_not_others": {
                "A": {"en": "Correct. Descent and Residence are present in 16(2) but absent in 15(1).", "ta": "சரி. வம்சாவளியும் இருப்பிடமும் 16(2)-ல் உள்ளன, ஆனால் 15(1)-ல் இல்லை."},
                "B": {"en": "Incorrect. Caste and Sex are present in both 15(1) and 16(2).", "ta": "தவறு. சாதியும் பாலினமும் இரண்டிலும் உள்ளன."},
                "C": {"en": "Incorrect. Religion and Place of Birth are present in both 15(1) and 16(2).", "ta": "தவறு. மதமும் பிறந்த இடமும் இரண்டிலும் உள்ளன."},
                "D": {"en": "Incorrect. Language is not a ground in 15(1) or 16(2); it appears in 29(2).", "ta": "தவறு. மொழி 15(1) அல்லது 16(2)-ல் இல்லை; அது 29(2)-ல் வருகிறது."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Trap: Remember the mnemonic: Art 15 has 5 grounds (RRCSP), Art 16 has 7 grounds (RRCSP + Descent + Residence). Language is NEVER a ground in Art 15 or 16!",
                "ta": "TNPSC பொறி: பிரிவு 15-ல் 5 அடிப்படைகள், பிரிவு 16-ல் 7 அடிப்படைகள் (கூடுதல்: வம்சாவளி, இருப்பிடம்). மொழி பிரிவு 15 அல்லது 16-ல் இடம்பெறவில்லை!"
            },
            "revision_fact": {
                "en": "Under Article 16(3), ONLY Parliament (not state legislatures) can prescribe residence as a condition for certain public employment.",
                "ta": "பிரிவு 16(3)-ன் கீழ், சில பொது வேலைவாய்ப்புகளுக்கு இருப்பிடத்தைக் கட்டாய நிபந்தனையாகப் பாராளுமன்றம் மட்டுமே (மாநில சட்டமன்றம் அல்ல) விதிக்க முடியும்."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Understand",
            "estimated_time_sec": 45,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 15", "Article 16", "Grand Test"]
        },

        # Q7: Chronology - Reservation Landmark Cases
        {
            "id": "FR_GT_007",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Hard",
            "question_type": "Chronology",
            "question": {
                "en": "Arrange the following landmark Supreme Court judgments on Reservation and Equality in correct chronological order:\n1. Champakam Dorairajan v. State of Madras\n2. Indra Sawhney v. Union of India (Mandal Case)\n3. M. Nagaraj v. Union of India\n4. Jarnail Singh v. Lachhmi Narain Gupta",
                "ta": "இடஒதுக்கீடு மற்றும் சமத்துவம் தொடர்பான பின்வரும் உச்ச நீதிமன்றத் தீர்ப்புகளைச் சரியான காலவரிசையில் அமைக்கவும்:\n1. செண்பகம் துரைராஜன் எதிர் மதராஸ் மாநிலம்\n2. இந்திரா சாஹ்னி எதிர் இந்திய யூனியன் (மண்டல் வழக்கு)\n3. எம். நாகராஜ் எதிர் இந்திய யூனியன்\n4. ஜர்னைல் சிங் எதிர் லச்ச்மி நரேன் குப்தா"
            },
            "options": [
                {
                    "id": "A",
                    "en": "1 - 2 - 3 - 4",
                    "ta": "1 - 2 - 3 - 4"
                },
                {
                    "id": "B",
                    "en": "2 - 1 - 4 - 3",
                    "ta": "2 - 1 - 4 - 3"
                },
                {
                    "id": "C",
                    "en": "1 - 3 - 2 - 4",
                    "ta": "1 - 3 - 2 - 4"
                },
                {
                    "id": "D",
                    "en": "3 - 1 - 2 - 4",
                    "ta": "3 - 1 - 2 - 4"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "Correct chronological sequence: (1) Champakam Dorairajan case (1951) -> led to 1st Amendment Act 1951 adding Art 15(4); (2) Indra Sawhney case (1992) -> 50% reservation cap & creamy layer rule; (3) M. Nagaraj case (2006) -> quantifiable data rule for SC/ST promotion; (4) Jarnail Singh case (2018) -> applied creamy layer to SC/ST promotions.",
                "ta": "சரியான காலவரிசை: (1) செண்பகம் துரைராஜன் வழக்கு (1951) -> 1-வது திருத்தச் சட்டம் பிரிவு 15(4); (2) இந்திரா சாஹ்னி வழக்கு (1992) -> 50% உச்சவரம்பு மற்றும் கிரீமிலேயர்; (3) எம். நாகராஜ் வழக்கு (2006) -> பதவி உயர்வில் அளவிடக்கூடிய தரவு; (4) ஜர்னைல் சிங் வழக்கு (2018) -> SC/ST பதவி உயர்வில் கிரீமிலேயர்."
            },
            "why_not_others": {
                "A": {"en": "Correct. 1951 -> 1992 -> 2006 -> 2018.", "ta": "சரி. 1951 -> 1992 -> 2006 -> 2018."},
                "B": {"en": "Incorrect. Champakam Dorairajan (1951) precedes Indra Sawhney (1992).", "ta": "தவறு. செண்பகம் துரைராஜன் (1951) வழக்கு இந்திரா சாஹ்னிக்கு (1992) முந்தையது."},
                "C": {"en": "Incorrect. M. Nagaraj (2006) comes after Indra Sawhney (1992).", "ta": "தவறு. நாகராஜ் வழக்கு (2006) இந்திரா சாஹ்னிக்கு பிந்தையது."},
                "D": {"en": "Incorrect. Champakam Dorairajan is the earliest 1951 judgment.", "ta": "தவறு. செண்பகம் துரைராஜன் வழக்கு மிக முந்தைய 1951 வழக்காகும்."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: Champakam Dorairajan (1951) struck down Madras Communal G.O., prompting Jawaharlal Nehru to enact the 1st Constitutional Amendment Act 1951 (Art 15(4)).",
                "ta": "TNPSC குறிப்பு: செண்பகம் துரைராஜன் வழக்கு (1951) மெட்ராஸ் வகுப்புவாத அரசாணையை ரத்து செய்தது, இது ஜவஹர்லால் நேருவை 1-வது திருத்தச் சட்டம் (15(4)) இயற்றத் தூண்டியது."
            },
            "revision_fact": {
                "en": "103rd Constitutional Amendment Act 2019 added Articles 15(6) and 16(6) providing up to 10% reservation for Economically Weaker Sections (EWS), upheld in Janhit Abhiyan v. UOI (2022).",
                "ta": "2019-ன் 103-வது திருத்தச் சட்டம் EWS-க்கு 10% இடஒதுக்கீடு வழங்கி 15(6), 16(6) இணைத்தது, இது ஜன்ஹித் அபியான் (2022) வழக்கில் உறுதி செய்யப்பட்டது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Analyze",
            "estimated_time_sec": 60,
            "pyq_similarity": "High",
            "tags": ["Polity", "Reservation", "Chronology", "Grand Test"]
        },

        # Q8: Match the Following - Amendments & FR Provisions
        {
            "id": "FR_GT_008",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Medium",
            "question_type": "Match the Following",
            "question": {
                "en": "Match List-I (Constitutional Amendment Act) with List-II (Inserted FR Provision):\nList-I:\na. 1st Amendment Act, 1951\nb. 77th Amendment Act, 1995\nc. 81st Amendment Act, 2000\nd. 93rd Amendment Act, 2005\n\nList-II:\n1. Article 16(4B) - Carry forward rule & 50% cap bypass for backlog vacancies\n2. Article 15(5) - Reservation in private educational institutions\n3. Article 15(4) - Special provisions for SEBCs, SCs and STs\n4. Article 16(4A) - Reservation in promotion for SCs and STs",
                "ta": "பட்டியல்-I-ஐ (அரசியலமைப்புத் திருத்தச் சட்டம்) பட்டியல்-II-உடன் (இணைக்கப்பட்ட அடிப்படை உரிமைப் பிரிவு) பொருத்துக:\nபட்டியல்-I:\na. 1-வது திருத்தச் சட்டம், 1951\nb. 77-வது திருத்தச் சட்டம், 1995\nc. 81-வது திருத்தச் சட்டம், 2000\nd. 93-வது திருத்தச் சட்டம், 2005\n\nபட்டியல்-II:\n1. பிரிவு 16(4B) - விடுபட்ட காலிப்பணியிடங்களுக்கு 50% உச்சவரம்பு விலக்கு\n2. பிரிவு 15(5) - தனியார் கல்வி நிறுவனங்களில் இடஒதுக்கீடு\n3. பிரிவு 15(4) - பிற்படுத்தப்பட்டோர், SC/ST சிறப்பு விதிகள்\n4. பிரிவு 16(4A) - SC/ST பிரிவினருக்குப் பதவி உயர்வில் இடஒதுக்கீடு"
            },
            "options": [
                {
                    "id": "A",
                    "en": "a-3, b-4, c-1, d-2",
                    "ta": "a-3, b-4, c-1, d-2"
                },
                {
                    "id": "B",
                    "en": "a-4, b-3, c-2, d-1",
                    "ta": "a-4, b-3, c-2, d-1"
                },
                {
                    "id": "C",
                    "en": "a-3, b-1, c-4, d-2",
                    "ta": "a-3, b-1, c-4, d-2"
                },
                {
                    "id": "D",
                    "en": "a-2, b-4, c-1, d-3",
                    "ta": "a-2, b-4, c-1, d-3"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "Correct match: 1st Amendment (1951) inserted Art 15(4); 77th Amendment (1995) inserted Art 16(4A) for reservation in promotion; 81st Amendment (2000) inserted Art 16(4B) for backlog vacancies carrying forward bypassing 50% ceiling; 93rd Amendment (2005) inserted Art 15(5) for private educational institutions.",
                "ta": "சரியான பொருத்தம்: 1-வது திருத்தம் (1951) -> 15(4); 77-வது திருத்தம் (1995) -> 16(4A) பதவி உயர்வு; 81-வது திருத்தம் (2000) -> 16(4B) விடுபட்ட காலிப்பணியிடங்கள்; 93-வது திருத்தம் (2005) -> 15(5) தனியார் கல்வி நிறுவனங்கள்."
            },
            "why_not_others": {
                "A": {"en": "Correct match: a-3, b-4, c-1, d-2.", "ta": "சரியான பொருத்தம்: a-3, b-4, c-1, d-2."},
                "B": {"en": "Incorrect mapping for all amendments.", "ta": "அனைத்து திருத்தங்களுக்கும் தவறான பொருத்தம்."},
                "C": {"en": "Incorrect mapping for 77th and 81st amendments.", "ta": "77 மற்றும் 81-வது திருத்தங்களுக்குத் தவறான பொருத்தம்."},
                "D": {"en": "Incorrect mapping for 1st and 93rd amendments.", "ta": "1 மற்றும் 93-வது திருத்தங்களுக்குத் தவறான பொருத்தம்."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: Remember 85th Amendment Act (2001) gave 'consequential seniority' to SC/ST employees promoted under reservation (Art 16(4A)).",
                "ta": "TNPSC குறிப்பு: 85-வது திருத்தச் சட்டம் (2001) இடஒதுக்கீட்டில் பதவி உயர்வு பெறும் SC/ST ஊழியர்களுக்கு 'தொடர் பணி மூப்பு' (consequential seniority) வழங்கியது."
            },
            "revision_fact": {
                "en": "In Pramati Educational and Cultural Trust v. UOI (2014), the Supreme Court upheld the validity of 93rd Amendment Act (Art 15(5)) except for minority institutions under Art 30(1).",
                "ta": "பிரமதி கல்வி அறக்கட்டளை வழக்கில் (2014) 93-வது திருத்தச் சட்டம் பிரிவு 15(5) செல்லுபடியாகும் என உச்ச நீதிமன்றம் உறுதி செய்தது (பிரிவு 30(1) சிறுபான்மை நிறுவனங்கள் தவிர)."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Analyze",
            "estimated_time_sec": 65,
            "pyq_similarity": "High",
            "tags": ["Polity", "Amendments", "Match the Following", "Grand Test"]
        },

        # Q9: TNPSC Trap - Article 17 Untouchability
        {
            "id": "FR_GT_009",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Medium",
            "question_type": "TNPSC Trap",
            "question": {
                "en": "Regarding Article 17 of the Constitution of India (Abolition of Untouchability), which of the following statements is INCORRECT?",
                "ta": "இந்திய அரசியலமைப்பின் 17-வது பிரிவு (தீண்டாமை ஒழிப்பு) பற்றிய பின்வரும் கூற்றுகளில் எது தவறானது?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "The term 'Untouchability' is explicitly defined in Article 17 of the Constitution",
                    "ta": "'தீண்டாமை' என்ற சொல் அரசியலமைப்பின் 17-வது பிரிவில் வெளிப்படையாக வரையறுக்கப்பட்டுள்ளது"
                },
                {
                    "id": "B",
                    "en": "The right under Article 17 is available against both the State and private individuals",
                    "ta": "பிரிவு 17-ன் கீழ் உள்ள உரிமை அரசு மற்றும் தனியார் தனிநபர்கள் ஆகிய இருவருக்கு எதிராகவும் கிடைக்கிறது"
                },
                {
                    "id": "C",
                    "en": "It is an absolute Fundamental Right that admits no exceptions",
                    "ta": "இது எந்த விதிவிலக்குகளும் இல்லாத ஒரு முற்றுமுழுதான (Absolute) அடிப்படை உரிமையாகும்"
                },
                {
                    "id": "D",
                    "en": "The Untouchability (Offences) Act 1955 was renamed as Protection of Civil Rights Act 1955 in 1976",
                    "ta": "தீண்டாமை (குற்றங்கள்) சட்டம் 1955, 1976-ல் குடிமை உரிமைகள் பாதுகாப்புச் சட்டம் 1955 எனப் பெயர் மாற்றப்பட்டது"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "Statement A is INCORRECT (making it the correct answer). Neither the Constitution nor any Act of Parliament defines the term 'Untouchability'. The Mysore High Court in Devarajiah case clarified it refers to historical social practice, not literal touch.",
                "ta": "கூற்று A தவறானது (எனவே இது சரியான விடை). அரசியலமைப்பிலோ அல்லது நாடாளுமன்றச் சட்டத்திலோ 'தீண்டாமை' என்ற சொல் வரையறுக்கப்படவில்லை. மைசூர் உயர் நீதிமன்றம் தேவராஜையா வழக்கில் இது வரலாற்று ரீதியான சமூகப் பழக்கத்தையே குறிக்கிறது எனத் தெளிவுபடுத்தியது."
            },
            "why_not_others": {
                "A": {"en": "Correct answer (incorrect statement). 'Untouchability' is NOT defined anywhere in Constitution.", "ta": "சரியான விடை (தவறான கூற்று). 'தீண்டாமை' அரசியலமைப்பில் எங்கும் வரையறுக்கப்படவில்லை."},
                "B": {"en": "Incorrect answer (correct statement). Art 17 is enforceable against private persons (People's Union for Democratic Rights case).", "ta": "தவறான விடை (சரியான கூற்று). பிரிவு 17 தனியாருக்கு எதிராகவும் செயல்படும்."},
                "C": {"en": "Incorrect answer (correct statement). Article 17 is absolute without reasonable restrictions.", "ta": "தவறான விடை (சரியான கூற்று). பிரிவு 17 எந்த நியாயமான கட்டுப்பாடுகளும் இல்லாதது."},
                "D": {"en": "Incorrect answer (correct statement). The 1955 Act was amended and renamed in 1976.", "ta": "தவறான விடை (சரியான கூற்று). 1955 சட்டம் 1976-ல் பெயர் மாற்றப்பட்டது."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Trap: 'Untouchability' and 'Minority' are TWO terms widely used in Part III that are NOT defined in the Indian Constitution!",
                "ta": "TNPSC பொறி: 'தீண்டாமை' மற்றும் 'சிறுபான்மையினர்' ஆகிய இரண்டும் பகுதி III-ல் பயன்படுத்தப்பட்ட போதிலும் அரசியலமைப்பில் வரையறுக்கப்படாத சொற்களாகும்!"
            },
            "revision_fact": {
                "en": "Offences under Article 17 / Protection of Civil Rights Act 1955 are cognizable and non-bailable.",
                "ta": "பிரிவு 17 / குடிமை உரிமைகள் பாதுகாப்புச் சட்டம் 1955-ன் கீழ் உள்ள குற்றங்கள் பிணையில் வர முடியாத கடுமையான குற்றங்களாகும்."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Understand",
            "estimated_time_sec": 45,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 17", "TNPSC Trap", "Grand Test"]
        },

        # Q10: Hard / Analytical - Article 18 Titles
        {
            "id": "FR_GT_010",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Hard",
            "question_type": "Hard / Analytical",
            "question": {
                "en": "In Balaji Raghavan v. Union of India (1996), the Supreme Court upheld the constitutional validity of National Awards (Bharat Ratna, Padma Vibhushan, Padma Bhushan, Padma Shri) under Article 18. What was the central ratio decidendi of this judgment?",
                "ta": "பாலாஜி ராகவன் எதிர் இந்திய யூனியன் (1996) வழக்கில், தேசிய விருதுகள் (பாரத ரத்னா, பத்ம விபூஷன், பத்ம பூஷன், பத்மஸ்ரீ) பிரிவு 18-ன் கீழ் செல்லுபடியாகும் என உச்ச நீதிமன்றம் உறுதி செய்தது. இதன் முதன்மையான தீர்ப்பு அடிநாதம் (Ratio Decidendi) என்ன?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "National awards are titles of nobility explicitly permitted under Article 18(2)",
                    "ta": "தேசிய விருதுகள் பிரிவு 18(2)-ன் கீழ் வெளிப்படையாக அனுமதிக்கப்பட்ட பிரபுத்துவப் பட்டங்கள் ஆகும்"
                },
                {
                    "id": "B",
                    "en": "National awards denote merit and excellence, not hereditary titles of nobility, but recipient cannot use them as prefix or suffix to their names",
                    "ta": "தேசிய விருதுகள் தகுதியையும் சிறப்பையும் குறிக்கின்றனவே தவிர பரம்பரைப் பட்டங்கள் அல்ல, ஆனால் பெறுபவர் தன் பெயருக்கு முன்னொட்டாகவோ பின்னொட்டாகவோ பயன்படுத்தக் கூடாது"
                },
                {
                    "id": "C",
                    "en": "National awards are state privileges that can be conferred only on members of the Armed Forces",
                    "ta": "தேசிய விருதுகள் ஆயுதப்படை உறுப்பினர்களுக்கு மட்டுமே வழங்கப்படக் கூடிய அரசு சலுகைகள் ஆகும்"
                },
                {
                    "id": "D",
                    "en": "Article 18 applies only to foreign titles and does not restrict the Indian State from conferring any title",
                    "ta": "பிரிவு 18 வெளிநாட்டுப் பட்டங்களுக்கு மட்டுமே பொருந்தும், இந்திய அரசு எந்தப் பட்டத்தையும் வழங்குவதைத் தடுக்காது"
                }
            ],
            "correct_answer": "B",
            "explanation": {
                "en": "In Balaji Raghavan case (1996), 5-judge bench held National Awards do not violate Art 18 as equality does not mean mandate of equal status without recognizing merit. However, using them as prefixes/suffixes violates the rule and leads to forfeiture of award.",
                "ta": "பாலாஜி ராகவன் வழக்கில் (1996) 5 நீதிபதிகள் அமர்வு தேசிய விருதுகள் பிரிவு 18-ஐ மீறவில்லை எனத் தீர்ப்பளித்தது, ஏனெனில் தகுதியை அங்கீகரிப்பது சமத்துவத்திற்கு எதிரானது அல்ல. இருப்பினும் பெயருக்கு முன்/பின் பயன்படுத்தினால் விருது திரும்பப் பெறப்படும்."
            },
            "why_not_others": {
                "A": {"en": "Incorrect. Article 18 prohibits titles of nobility.", "ta": "தவறு. பிரிவு 18 பிரபுத்துவப் பட்டங்களைத் தடை செய்கிறது."},
                "B": {"en": "Correct. National awards recognize merit, but cannot be used as prefixes/suffixes.", "ta": "சரி. தேசிய விருதுகள் திறமையை அங்கீகரிக்கின்றன, ஆனால் பெயருக்கு முன்/பின் பயன்படுத்தக் கூடாது."},
                "C": {"en": "Incorrect. Military and academic distinctions are explicitly exempted under Art 18(1), but civilian awards are given to all citizens.", "ta": "தவறு. ராணுவம் மற்றும் கல்விச் சிறப்புகள் 18(1)-ல் விலக்களிக்கப்பட்டுள்ளன."},
                "D": {"en": "Incorrect. Article 18(1) explicitly bars the Indian State from conferring titles.", "ta": "தவறு. பிரிவு 18(1) இந்திய அரசு பட்டங்கள் வழங்குவதைத் தடை செய்கிறது."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: Article 18(1) allows ONLY Military and Academic distinctions to be conferred by the State. Bharat Ratna is a decoration of honor, not a title.",
                "ta": "TNPSC குறிப்பு: பிரிவு 18(1) ராணுவ மற்றும் கல்விச் சிறப்புகளை மட்டுமே அரசு வழங்க அனுமதிக்கிறது. பாரத ரத்னா ஒரு கௌரவ விருது, பட்டம் அல்ல."
            },
            "revision_fact": {
                "en": "Under Article 18(2), no citizen of India shall accept any title from any foreign State.",
                "ta": "பிரிவு 18(2)-ன் கீழ், இந்தியக் குடிமகன் எவரும் எந்தவொரு வெளிநாட்டிலிருந்தும் பட்டங்களை ஏற்றுக்கொள்ளக் கூடாது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Analyze",
            "estimated_time_sec": 55,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 18", "Titles", "Grand Test"]
        },

        # Q11: Direct MCQ - EWS Reservation 103rd Amendment
        {
            "id": "FR_GT_011",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Easy",
            "question_type": "Direct MCQ",
            "question": {
                "en": "The 103rd Constitutional Amendment Act, 2019 introduced reservation for Economically Weaker Sections (EWS) by inserting which articles into Part III of the Constitution?",
                "ta": "2019-ன் 103-வது அரசியலமைப்புத் திருத்தச் சட்டம், பகுதி III-ல் எந்தப் பிரிவுகளை இணைப்பதன் மூலம் பொருளாதாரத்தில் பின்தங்கிய பிரிவினருக்கு (EWS) இடஒதுக்கீட்டை அறிமுகப்படுத்தியது?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "Articles 15(6) and 16(6)",
                    "ta": "பிரிவுகள் 15(6) மற்றும் 16(6)"
                },
                {
                    "id": "B",
                    "en": "Articles 15(5) and 16(5)",
                    "ta": "பிரிவுகள் 15(5) மற்றும் 16(5)"
                },
                {
                    "id": "C",
                    "en": "Articles 15(4) and 16(4)",
                    "ta": "பிரிவுகள் 15(4) மற்றும் 16(4)"
                },
                {
                    "id": "D",
                    "en": "Articles 19(6) and 21A",
                    "ta": "பிரிவுகள் 19(6) மற்றும் 21A"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "103rd Amendment Act 2019 inserted Article 15(6) (EWS reservation up to 10% in educational institutions including private unaided) and Article 16(6) (EWS reservation up to 10% in public employment) for citizens not covered under 15(4), 15(5), 16(4).",
                "ta": "103-வது திருத்தச் சட்டம் 2019 பிரிவு 15(6) (கல்வி நிறுவனங்களில் EWS-க்கு 10% வரை இடஒதுக்கீடு) மற்றும் பிரிவு 16(6) (பொது வேலைவாய்ப்பில் 10% EWS இடஒதுக்கீடு) ஆகியவற்றை இணைத்தது."
            },
            "why_not_others": {
                "A": {"en": "Correct. Articles 15(6) and 16(6) were inserted by 103rd Amendment Act 2019.", "ta": "சரி. பிரிவுகள் 15(6) மற்றும் 16(6) 103-வது திருத்தச் சட்டத்தால் இணைக்கப்பட்டன."},
                "B": {"en": "Incorrect. 15(5) was inserted by 93rd Amendment 2005; 16(5) relates to religious office incumbent.", "ta": "தவறு. 15(5) 93-வது திருத்தத்தால் சேர்க்கப்பட்டது."},
                "C": {"en": "Incorrect. 15(4) was inserted by 1st Amendment 1951; 16(4) was in original Constitution.", "ta": "தவறு. 15(4) 1-வது திருத்தத்தால் சேர்க்கப்பட்டது."},
                "D": {"en": "Incorrect. 21A relates to Right to Education inserted by 86th Amendment 2002.", "ta": "தவறு. 21A 86-வது திருத்தத்தால் சேர்க்கப்பட்ட கல்வி உரிமை."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: Janhit Abhiyan v. Union of India (2022) 5-judge Supreme Court bench by 3:2 majority upheld the 103rd Amendment Act as constitutional.",
                "ta": "TNPSC குறிப்பு: ஜன்ஹித் அபியான் எதிர் இந்திய யூனியன் (2022) வழக்கில் 5 நீதிபதிகள் கொண்ட அமர்வு 3:2 பெரும்பான்மையில் 103-வது திருத்தச் சட்டத்தை உறுதி செய்தது."
            },
            "revision_fact": {
                "en": "EWS reservation is over and above the existing 50% reservation cap, meant specifically for non-SC/ST/OBC poor.",
                "ta": "EWS இடஒதுக்கீடு ஏற்கனவே உள்ள 50% இடஒதுக்கீட்டு உச்சவரம்பிற்கு அப்பாற்பட்டது, இது SC/ST/OBC அல்லாத ஏழைகளுக்கானது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Remember",
            "estimated_time_sec": 35,
            "pyq_similarity": "High",
            "tags": ["Polity", "103rd Amendment", "EWS", "Grand Test"]
        },

        # Q12: Conceptual MCQ - Judicial Review & Basic Structure
        {
            "id": "FR_GT_012",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Medium",
            "question_type": "Conceptual MCQ",
            "question": {
                "en": "The power of Judicial Review over legislation in India flows fundamentally from which constitutional provision?",
                "ta": "இந்தியாவில் சட்டமியற்றலின் மீதான 'நீதித்துறை மறுஆய்வு' அதிகாரம் முதன்மையாக எந்த அரசியலமைப்புப் பிரிவிலிருந்து வெளிப்படுகிறது?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "Article 13 read with Articles 32 and 226",
                    "ta": "பிரிவுகள் 32 மற்றும் 226 உடன் இணைந்த பிரிவு 13"
                },
                {
                    "id": "B",
                    "en": "Article 368 read with Article 143",
                    "ta": "பிரிவு 143 உடன் இணைந்த பிரிவு 368"
                },
                {
                    "id": "C",
                    "en": "Article 245 read with Article 246",
                    "ta": "பிரிவு 246 உடன் இணைந்த பிரிவு 245"
                },
                {
                    "id": "D",
                    "en": "Article 74 read with Article 75",
                    "ta": "பிரிவு 75 உடன் இணைந்த பிரிவு 74"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "Article 13 expressly provides for the unconstitutionality of laws violating FRs, while Articles 32 (Supreme Court) and 226 (High Courts) confer the remedy and power to issue writs/orders, forming the bedrock of Judicial Review in India.",
                "ta": "அடிப்படை உரிமைகளை மீறும் சட்டங்கள் செல்லாதவை என்று பிரிவு 13 கூறுகிறது. பிரிவுகள் 32 (உச்ச நீதிமன்றம்) மற்றும் 226 (உயர் நீதிமன்றங்கள்) நீதிப் பேராணைகளை வெளியிட்டு மறுஆய்வு செய்யும் அதிகாரத்தை வழங்குகின்றன."
            },
            "why_not_others": {
                "A": {"en": "Correct. Article 13 provides substantive restriction, 32 & 226 provide enforcement forums.", "ta": "சரி. பிரிவு 13 கட்டுப்பாட்டை அளிக்கிறது, 32 மற்றும் 226 அமலாக்க நீதிமன்றங்களை வழங்குகின்றன."},
                "B": {"en": "Incorrect. Article 368 is amendment power; 143 is advisory jurisdiction of President.", "ta": "தவறு. 368 திருத்தும் அதிகாரம்; 143 குடியரசுத் தலைவரின் ஆலோசனை எல்லை."},
                "C": {"en": "Incorrect. 245 & 246 deal with legislative distribution of powers, not judicial review of FRs.", "ta": "தவறு. 245 மற்றும் 246 சட்டமியற்றும் அதிகாரப் பகிர்வு பற்றியவை."},
                "D": {"en": "Incorrect. 74 & 75 deal with Council of Ministers.", "ta": "தவறு. 74 மற்றும் 75 அமைச்சரவை பற்றியவை."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: In L. Chandra Kumar v. Union of India (1997), judicial review under Art 32 and Art 226 was declared part of the Basic Structure of the Constitution.",
                "ta": "TNPSC குறிப்பு: எல். சந்திரகுமார் எதிர் இந்திய யூனியன் (1997) வழக்கில், பிரிவு 32 மற்றும் 226-ன் கீழ் உள்ள நீதித்துறை மறுஆய்வு அரசியலமைப்பின் அடிப்படை அமைப்பின் ஒரு பகுதி என அறிவிக்கப்பட்டது."
            },
            "revision_fact": {
                "en": "The term 'Judicial Review' is NOT explicitly defined in the Constitution of India, though the power is expressly conferred by Articles 13, 32, 226, 136, 141, etc.",
                "ta": "'நீதித்துறை மறுஆய்வு' என்ற சொல் அரசியலமைப்பில் வெளிப்படையாக வரையறுக்கப்படவில்லை, இருப்பினும் அதிகாரம் வழங்கப்பட்டுள்ளது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Understand",
            "estimated_time_sec": 45,
            "pyq_similarity": "High",
            "tags": ["Polity", "Judicial Review", "Article 13", "Grand Test"]
        },

        # Q13: Assertion & Reason - Rule of Law & Art 14
        {
            "id": "FR_GT_013",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Hard",
            "question_type": "Assertion & Reason",
            "question": {
                "en": "Assertion (A): Article 14 permits reasonable classification of persons, objects and transactions by law for legitimate state ends.\nReason (R): Article 14 forbids class legislation, which makes improper discrimination by conferring particular privileges upon a class of persons arbitrarily selected.",
                "ta": "கூற்று (A): பிரிவு 14 முறையான அரசு நோக்கங்களுக்காக நபர்கள், பொருட்கள் மற்றும் பரிவர்த்தனைகளை நியாயமான முறையில் வகைப்படுத்துவதை அனுமதிக்கிறது.\nகாரணம் (R): பிரிவு 14 வகுப்புவாத சட்டங்களைத் தடை செய்கிறது, ஏனெனில் அது தன்னிச்சையாகத் தேர்ந்தெடுக்கப்பட்ட ஒரு குறிப்பிட்ட வகுப்பிற்குச் சலுகைகளை வழங்கி தவறான பாகுபாட்டை உருவாக்குகிறது."
            },
            "options": [
                {
                    "id": "A",
                    "en": "Both (A) and (R) are true and (R) is the correct explanation of (A)",
                    "ta": "(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-வின் சரியான விளக்கமாகும்"
                },
                {
                    "id": "B",
                    "en": "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)",
                    "ta": "(A) மற்றும் (R) இரண்டும் சரி, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல"
                },
                {
                    "id": "C",
                    "en": "(A) is true but (R) is false",
                    "ta": "(A) சரி, ஆனால் (R) தவறு"
                },
                {
                    "id": "D",
                    "en": "(A) is false but (R) is true",
                    "ta": "(A) தவறு, ஆனால் (R) சரி"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "Both statements are true. Article 14 forbids 'class legislation' (arbitrary discrimination), but permits 'reasonable classification' to treat equals equally and unequals unequally (State of West Bengal v. Anwar Ali Sarkar). Hence R correctly explains A.",
                "ta": "இரண்டு கூற்றுகளும் சரியானவை. பிரிவு 14 வகுப்புவாதச் சட்டங்களைத் (தன்னிச்சையான பாகுபாடு) தடை செய்கிறது, ஆனால் சமமானவர்களைச் சமமாகவும் சமமற்றவர்களைச் சமமின்றியும் நடத்த 'நியாயமான வகைப்பாட்டை' அனுமதிக்கிறது."
            },
            "why_not_others": {
                "A": {"en": "Correct. (R) directly provides the constitutional logic why classification is permitted while class legislation is forbidden.", "ta": "சரி. வகுப்புவாத சட்டம் தடுக்கப்பட்டு வகைப்பாடு ஏன் அனுமதிக்கப்படுகிறது என்ற காரணத்தை (R) விளக்குகிறது."},
                "B": {"en": "Incorrect because (R) is indeed the correct logical explanation of (A).", "ta": "தவறு, ஏனெனில் (R) என்பது (A)-ன் சரியான விளக்கமாகும்."},
                "C": {"en": "Incorrect because both statements are true.", "ta": "தவறு, ஏனெனில் இரண்டு கூற்றுகளும் சரியானவை."},
                "D": {"en": "Incorrect because both statements are true.", "ta": "தவறு, ஏனெனில் இரண்டு கூற்றுகளும் சரியானவை."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: Two conditions for Reasonable Classification (Ram Krishna Dalmia v. Justice Tendolkar): (1) Classification must be founded on an intelligible differentia, (2) Differentia must have a rational nexus to the object sought to be achieved.",
                "ta": "TNPSC குறிப்பு: நியாயமான வகைப்பாட்டின் இரு நிபந்தனைகள்: (1) புத்திசாலித்தனமான வேறுபாடு (intelligible differentia), (2) அடைய வேண்டிய நோக்கத்துடன் கூடிய நியாயமான தொடர்பு (rational nexus)."
            },
            "revision_fact": {
                "en": "Equal protection of laws under Art 14 means 'like should be treated alike and not that unlike should be treated alike'.",
                "ta": "பிரிவு 14-ன் கீழ் சட்டங்களின் சமமான பாதுகாப்பு என்பது 'ஒத்தவை ஒத்தபடியே நடத்தப்பட வேண்டும், ஒவ்வாதவை ஒத்தபடி நடத்தப்படக் கூடாது' என்பதாகும்."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Analyze",
            "estimated_time_sec": 60,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 14", "Assertion Reason", "Grand Test"]
        },

        # Q14: Direct MCQ - Creamy Layer Concept
        {
            "id": "FR_GT_014",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Easy",
            "question_type": "Direct MCQ",
            "question": {
                "en": "Which Committee was appointed by the Union Government in 1993 to identify the 'Creamy Layer' among the Other Backward Classes (OBCs)?",
                "ta": "இதர பிற்படுத்தப்பட்ட வகுப்பினரிடையே (OBC) 'கிரீமிலேயர்' (பாலாடை அடுக்கு) பிரிவினரை அடையாளம் காண 1993-ல் மத்திய அரசால் அமைக்கப்பட்ட குழு எது?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "Ram Nandan Committee",
                    "ta": "ராம் நந்தன் குழு"
                },
                {
                    "id": "B",
                    "en": "Mandal Commission",
                    "ta": "மண்டல் ஆணையம்"
                },
                {
                    "id": "C",
                    "en": "Kaka Kalelkar Commission",
                    "ta": "காக்கா கலேல்கர் ஆணையம்"
                },
                {
                    "id": "D",
                    "en": "Sarkaria Commission",
                    "ta": "சர்க்காரியா ஆணையம்"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "Following the Indra Sawhney judgment (1992), the Ram Nandan Committee was appointed in 1993 to identify the creamy layer among OBCs. Its report was submitted and accepted in 1993.",
                "ta": "இந்திரா சாஹ்னி தீர்ப்பைத் தொடர்ந்து (1992), OBC-களில் உள்ள கிரீமிலேயரைக் கண்டறிய 1993-ல் ராம் நந்தன் குழு அமைக்கப்பட்டது. அதன் அறிக்கை 1993-ல் ஏற்றுக்கொள்ளப்பட்டது."
            },
            "why_not_others": {
                "A": {"en": "Correct. Ram Nandan Committee identified creamy layer in 1993.", "ta": "சரி. ராம் நந்தன் குழு 1993-ல் கிரீமிலேயரை அடையாளம் கண்டது."},
                "B": {"en": "Incorrect. Mandal Commission (Second Backward Classes Commission) was set up in 1979 under B.P. Mandal.", "ta": "தவறு. மண்டல் ஆணையம் 1979-ல் அமைக்கப்பட்ட 2-வது பிற்படுத்தப்பட்டோர் ஆணையம்."},
                "C": {"en": "Incorrect. Kaka Kalelkar Commission was the First Backward Classes Commission (1953).", "ta": "தவறு. காக்கா கலேல்கர் ஆணையம் முதல் பிற்படுத்தப்பட்டோர் ஆணையம் (1953)."},
                "D": {"en": "Incorrect. Sarkaria Commission (1983) dealt with Centre-State Relations.", "ta": "தவறு. சர்க்காரியா ஆணையம் (1983) மத்திய-மாநில உறவுகள் பற்றியது."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: National Commission for Backward Classes (NCBC) was established as a statutory body in 1993 and given Constitutional status under Article 338B by 102nd Amendment Act 2018.",
                "ta": "TNPSC குறிப்பு: தேசிய பிற்படுத்தப்பட்டோர் ஆணையத்திற்கு (NCBC) 2018-ன் 102-வது திருத்தச் சட்டத்தின் மூலம் பிரிவு 338B-ன் கீழ் அரசியலமைப்பு அந்தஸ்து வழங்கப்பட்டது."
            },
            "revision_fact": {
                "en": "Creamy layer exclusion principle applies ONLY to OBCs in direct recruitment, and to SCs/STs in reservation in promotion (Jarnail Singh case 2018).",
                "ta": "கிரீமிலேயர் விலக்குக் கொள்கை நேரடி நியமனத்தில் OBC-களுக்கும், பதவி உயர்வு இடஒதுக்கீட்டில் SC/ST-களுக்கும் பொருந்தும் (ஜர்னைல் சிங் வழக்கு 2018)."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Remember",
            "estimated_time_sec": 35,
            "pyq_similarity": "High",
            "tags": ["Polity", "Creamy Layer", "Indra Sawhney", "Grand Test"]
        },

        # Q15: Statement-Based - Reservations in Public Employment
        {
            "id": "FR_GT_015",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Medium",
            "question_type": "Statement-Based",
            "question": {
                "en": "Consider the following statements regarding reservation provisions under Article 16:\n1. Article 16(4) empowers the State to make reservation for any backward class of citizens which is not adequately represented in the services under the State.\n2. The Supreme Court in Indra Sawhney (1992) held that reservation under Article 16(4) should not exceed 50% except under extraordinary situations.\n3. The 81st Amendment Act 2000 introduced Article 16(4B) allowing backlog vacancies to be treated as a separate class not subject to the 50% cap.\nWhich of the statements given above are correct?",
                "ta": "பிரிவு 16-ன் கீழ் உள்ள இடஒதுக்கீட்டு விதிகள் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. அரசுப் பணிகளில் போதுமான பிரதிநிதித்துவம் பெறாத பிற்படுத்தப்பட்ட குடிமக்களுக்கு இடஒதுக்கீடு வழங்க பிரிவு 16(4) அரசிற்கு அதிகாரம் அளிக்கிறது.\n2. இந்திரா சாஹ்னி (1992) வழக்கில் பிரிவு 16(4)-ன் கீழ் இடஒதுக்கீடு அசாதாரண சூழ்நிலைகளைத் தவிர 50%-க்கு மிகாமல் இருக்க வேண்டும் என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது.\n3. 81-வது திருத்தச் சட்டம் 2000, பிரிவு 16(4B)-ஐ இணைத்து விடுபட்ட காலிப்பணியிடங்களை 50% உச்சவரம்பிற்கு உட்படாத தனி வகுப்பாகக் கருத அனுமதித்தது.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "1 and 2 only",
                    "ta": "1 மற்றும் 2 மட்டுமே"
                },
                {
                    "id": "B",
                    "en": "2 and 3 only",
                    "ta": "2 மற்றும் 3 மட்டுமே"
                },
                {
                    "id": "C",
                    "en": "1 and 3 only",
                    "ta": "1 மற்றும் 3 மட்டுமே"
                },
                {
                    "id": "D",
                    "en": "1, 2 and 3",
                    "ta": "1, 2 மற்றும் 3"
                }
            ],
            "correct_answer": "D",
            "explanation": {
                "en": "All three statements are correct. Statement 1 reflects Art 16(4). Statement 2 reflects Indra Sawhney 50% ceiling rule. Statement 3 reflects 81st Amendment Act 2000 which added Art 16(4B) enabling carry-forward of unfilled backlog vacancies without counting towards the 50% limit of current year vacancies.",
                "ta": "மூன்று கூற்றுகளும் சரியானவை. கூற்று 1 பிரிவு 16(4)-ன் வரம்பு. கூற்று 2 இந்திரா சாஹ்னி 50% எல்லை. கூற்று 3 81-வது திருத்தத்தின்படி பிரிவு 16(4B) விடுபட்ட காலிப்பணியிடங்களை 50% வரம்பின்றி நிரப்ப வழிசெய்கிறது."
            },
            "why_not_others": {
                "A": {"en": "Incorrect because statement 3 is also correct.", "ta": "தவறு, ஏனெனில் கூற்று 3-ம் சரியானது."},
                "B": {"en": "Incorrect because statement 1 is also correct.", "ta": "தவறு, ஏனெனில் கூற்று 1-ம் சரியானது."},
                "C": {"en": "Incorrect because statement 2 is also correct.", "ta": "தவறு, ஏனெனில் கூற்று 2-ம் சரியானது."},
                "D": {"en": "Correct. All statements 1, 2 and 3 are factually true.", "ta": "சரி. கூற்றுகள் 1, 2 மற்றும் 3 அனைத்தும் சரியானவை."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: Tamil Nadu's 69% reservation law was passed in 1993 (TN Backward Classes Act 1993) and placed in Ninth Schedule by 76th Constitutional Amendment Act 1994 to protect it from judicial challenge.",
                "ta": "TNPSC குறிப்பு: தமிழ்நாட்டின் 69% இடஒதுக்கீட்டுச் சட்டம் 1993-ல் இயற்றப்பட்டு, 76-வது அரசியலமைப்புத் திருத்தச் சட்டம் 1994 மூலம் 9-வது அட்டவணையில் சேர்க்கப்பட்டுப் பாதுகாக்கப்பட்டது."
            },
            "revision_fact": {
                "en": "I.R. Coelho v. State of Tamil Nadu (2007) held that all laws placed in Ninth Schedule after April 24, 1973 are open to judicial review if they violate basic structure.",
                "ta": "ஐ.ஆர். கொயல்ஹோ வழக்கில் (2007) ஏப்ரல் 24, 1973-க்கு பின் 9-வது அட்டவணையில் சேர்க்கப்பட்ட சட்டங்கள் அடிப்படை அமைப்பை மீறினால் நீதித்துறை மறுஆய்வுக்கு உட்பட்டவை எனக் கூறப்பட்டது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Analyze",
            "estimated_time_sec": 55,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 16", "Reservations", "Grand Test"]
        },

        # Q16: PYQ Pattern - Definition of Law under Art 13
        {
            "id": "FR_GT_016",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Medium",
            "question_type": "PYQ Pattern",
            "question": {
                "en": "Which of the following is NOT included in the expression 'Law' under Article 13(3) of the Indian Constitution?",
                "ta": "இந்திய அரசியலமைப்பின் 13(3) பிரிவின் கீழ் 'சட்டம்' என்ற வெளிப்பாட்டில் பின்வருவனவற்றுள் எது சேர்க்கப்படவில்லை?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "Ordinances issued by the President or State Governors",
                    "ta": "குடியரசுத் தலைவர் அல்லது மாநில ஆளுநர்களால் பிறப்பிக்கப்படும் அவசரச் சட்டங்கள்"
                },
                {
                    "id": "B",
                    "en": "Custom or usage having in the territory of India the force of law",
                    "ta": "இந்தியப் பகுதியில் சட்டத்தின் நடைமுறையைக் கொண்டுள்ள பாரம்பரிய வழக்கம் அல்லது நடைமுறை"
                },
                {
                    "id": "C",
                    "en": "Non-statutory administrative executive instructions lacking statutory force",
                    "ta": "சட்டப்பூர்வ அதிகாரம் இல்லாத சட்டப்பூர்வமற்ற நிர்வாகக் கட்டளைகள்"
                },
                {
                    "id": "D",
                    "en": "Statutory rules, regulations, notifications and bye-laws",
                    "ta": "சட்டப்பூர்வ விதிகள், நெறிமுறைகள், அறிவிக்கைகள் மற்றும் துணைச் விதிகள்"
                }
            ],
            "correct_answer": "C",
            "explanation": {
                "en": "Article 13(3) defines 'law' to include: (a) Permanent laws by Parliament/State legislatures, (b) Temporary laws like Ordinances, (c) Delegated legislation (rules, regulations, notifications, bye-laws), and (d) Non-legislative sources like custom or usage. Non-statutory administrative instructions do NOT constitute 'law' under Art 13.",
                "ta": "பிரிவு 13(3) 'சட்டம்' என்பதை வரையறுக்கிறது: நிரந்தரச் சட்டங்கள், அவசரச் சட்டங்கள், துணைச் சட்டங்கள் (விதிகள், அறிவிக்கைகள்), பாரம்பரிய வழக்கங்கள். சட்டப்பூர்வ அதிகாரமற்ற நிர்வாகக் கட்டளைகள் பிரிவு 13-ன் கீழ் 'சட்டம்' ஆகாது."
            },
            "why_not_others": {
                "A": {"en": "Incorrect. Ordinances are temporary laws and fall under Art 13 definition of law.", "ta": "தவறு. அவசரச் சட்டங்கள் பிரிவு 13-ன் கீழ் சட்டமாகக் கருதப்படும்."},
                "B": {"en": "Incorrect. Customs having force of law are explicitly named in Art 13(3)(a).", "ta": "தவறு. சட்டத்தின் பலன் கொண்ட வழக்கங்கள் பிரிவு 13(3)-ல் குறிப்பிடப்பட்டுள்ளன."},
                "C": {"en": "Correct. Non-statutory administrative instructions are NOT law under Article 13.", "ta": "சரி. சட்டப்பூர்வ அதிகாரமற்ற நிர்வாகக் கட்டளைகள் பிரிவு 13-ன் கீழ் சட்டம் அல்ல."},
                "D": {"en": "Incorrect. Delegated statutory instruments are included under Art 13.", "ta": "தவறு. துணைச் சட்டக் கருவிகள் பிரிவு 13-ல் அடங்கும்."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: Personal laws (like Hindu Law, Muslim Personal Law) have been held by courts not to fall strictly under 'law' defined in Art 13(3) (State of Bombay v. Narasu Appa Mali 1952).",
                "ta": "TNPSC குறிப்பு: தனிநபர் சட்டங்கள் (இந்து சட்டம், முஸ்லீம் தனிநபர் சட்டம்) பிரிவு 13(3)-ன் 'சட்டம்' என்பதன் கீழ் நேரடியாக வராது எனத் தீர்ப்பளிக்கப்பட்டுள்ளது (நரசு அப்பா மாலி வழக்கு 1952)."
            },
            "revision_fact": {
                "en": "Article 13 ensures the supremacy of Fundamental Rights over both legislative statutes and executive delegated orders.",
                "ta": "பிரிவு 13 சட்டங்கள் மற்றும் நிர்வாக உத்தரவுகள் இரண்டையும் விட அடிப்படை உரிமைகளின் மேலாதிக்கத்தை உறுதி செய்கிறது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Understand",
            "estimated_time_sec": 45,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 13", "Definition of Law", "Grand Test"]
        },

        # Q17: Conceptual MCQ - Instrumentality of State Test
        {
            "id": "FR_GT_017",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Hard",
            "question_type": "Conceptual MCQ",
            "question": {
                "en": "In which landmark judgment did the Supreme Court lay down tests (such as deep and pervasive State control, financial dominance, and monopoly status) to determine whether an entity is an 'instrumentality or agency of State' under Article 12?",
                "ta": "ஒரு அமைப்பு பிரிவு 12-ன் கீழ் 'அரசின் உறுப்பு அல்லது முகமையா' என்பதைத் தீர்மானிக்க உச்ச நீதிமன்றம் எந்த முக்கிய வழக்கில் சோதனைகளை (அரசின் ஆழமான கட்டுப்பாடு, நிதி ஆதிக்கம், முற்றுரிமை நிலை) வகுத்தது?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "Ajay Hasia v. Khalid Mujib (1981)",
                    "ta": "அஜய் ஹாசியா எதிர் காலித் முஜீப் (1981)"
                },
                {
                    "id": "B",
                    "en": "Kharak Singh v. State of UP (1963)",
                    "ta": "கரக் சிங் எதிர் உத்தரப் பிரதேச அரசு (1963)"
                },
                {
                    "id": "C",
                    "en": "Minerva Mills v. Union of India (1980)",
                    "ta": "மினர்வா மில்ஸ் எதிர் இந்திய யூனியன் (1980)"
                },
                {
                    "id": "D",
                    "en": "A.K. Gopalan v. State of Madras (1950)",
                    "ta": "ஏ.கே. கோபாலன் எதிர் மதராஸ் மாநிலம் (1950)"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "In Ajay Hasia v. Khalid Mujib (1981), Justice P.N. Bhagwati summarized the 6 tests originally indicated in R.D. Shetty v. Airport Authority of India (1979) to determine if a body is an instrumentality of State under Art 12.",
                "ta": "அஜய் ஹாசியா எதிர் காலித் முஜீப் (1981) வழக்கில், நீதிபதி பி.என். பகவதி ஆர்.டி. ஷெட்டி வழக்கில் கூறப்பட்ட 6 சோதனைகளைத் தொகுத்து ஒரு அமைப்பு பிரிவு 12-ன் கீழ் அரசின் உறுப்பா என்பதைத் தீர்மானிக்க உதவியாக அளித்தார்."
            },
            "why_not_others": {
                "A": {"en": "Correct. Ajay Hasia case laid down the definitive 6 tests for Art 12 instrumentality.", "ta": "சரி. அஜய் ஹாசியா வழக்கு பிரிவு 12-ன் 6 சோதனைகளை வகுத்தது."},
                "B": {"en": "Incorrect. Kharak Singh case dealt with police surveillance and Article 21.", "ta": "தவறு. கரக் சிங் வழக்கு காவல் கண்காணிப்பு மற்றும் பிரிவு 21 பற்றியது."},
                "C": {"en": "Incorrect. Minerva Mills case dealt with Basic Structure and 42nd Amendment.", "ta": "தவறு. மினர்வா மில்ஸ் வழக்கு அடிப்படை அமைப்பு பற்றியது."},
                "D": {"en": "Incorrect. A.K. Gopalan case dealt with preventive detention and procedure established by law.", "ta": "தவறு. ஏ.கே. கோபாலன் வழக்கு தடுப்புக் காவல் பற்றியது."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: BCCI (Board of Control for Cricket in India) was held NOT to be 'State' under Article 12 in Zee Telefilms v. UOI (2005) as it lacks deep and pervasive State control, though it performs public functions.",
                "ta": "TNPSC குறிப்பு: ஜீ டெலிஃபிலிம்ஸ் வழக்கில் (2005) பி.சி.சி.ஐ (BCCI) பொதுப் பணிகளைச் செய்தபோதிலும் அரசின் ஆழமான கட்டுப்பாடு இல்லாததால் பிரிவு 12-ன் கீழ் 'அரசு' அல்ல எனத் தீர்ப்பளிக்கப்பட்டது."
            },
            "revision_fact": {
                "en": "NCERT, CSIR, and Registered Societies can be treated as State if they satisfy the Ajay Hasia tests.",
                "ta": "NCERT, CSIR மற்றும் பதிவுசெய்யப்பட்ட சங்கங்கள் அஜய் ஹாசியா சோதனைகளை நிறைவு செய்தால் 'அரசு' எனக் கருதப்படலாம்."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Analyze",
            "estimated_time_sec": 50,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 12", "Instrumentality of State", "Grand Test"]
        },

        # Q18: Direct MCQ - Exception to Untouchability & Civil Rights Act
        {
            "id": "FR_GT_018",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Easy",
            "question_type": "Direct MCQ",
            "question": {
                "en": "Under the Protection of Civil Rights Act, 1955 (enacted under Article 17), a person convicted of an offence of 'untouchability' is disqualified from contesting elections to Parliament or State Legislature for how many years?",
                "ta": "பிரிவு 17-ன் கீழ் இயற்றப்பட்ட குடிமை உரிமைகள் பாதுகாப்புச் சட்டம் 1955-ன் கீழ், 'தீண்டாமை' குற்றத்திற்காகத் தண்டிக்கப்பட்ட ஒருவர் நாடாளுமன்ற அல்லது மாநில சட்டமன்றத் தேர்தல்களில் போட்டியிடுவதிலிருந்து எத்தனை ஆண்டுகளுக்குத் தகுதிநீக்கம் செய்யப்படுகிறார்?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "6 years from the date of conviction",
                    "ta": "தண்டனை விதிக்கப்பட்ட தேதியிலிருந்து 6 ஆண்டுகள்"
                },
                {
                    "id": "B",
                    "en": "3 years from the date of conviction",
                    "ta": "தண்டனை விதிக்கப்பட்ட தேதியிலிருந்து 3 ஆண்டுகள்"
                },
                {
                    "id": "C",
                    "en": "Life long permanent disqualification",
                    "ta": "ஆயுள் முழுவதுமான நிரந்தரத் தகுதிநீக்கம்"
                },
                {
                    "id": "D",
                    "en": "No disqualification applies unless imprisonment exceeds 5 years",
                    "ta": "சிறைத்தண்டனை 5 ஆண்டுகளுக்கு மேல் இருந்தாலன்றி தகுதிநீக்கம் இல்லை"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "Under Section 8 of Representation of the People Act 1951 read with Protection of Civil Rights Act 1955, a person convicted of any offence under Untouchability law is disqualified for contesting elections for 6 years.",
                "ta": "மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 பிரிவு 8 மற்றும் குடிமை உரிமைகள் பாதுகாப்புச் சட்டம் 1955-ன் கீழ், தீண்டாமைக் குற்றத்திற்காகத் தண்டிக்கப்பட்டவர் 6 ஆண்டுகளுக்குத் தேர்தலில் போட்டியிடத் தகுதியற்றவர் ஆகிறார்."
            },
            "why_not_others": {
                "A": {"en": "Correct. Disqualification period is 6 years under election law.", "ta": "சரி. தேர்தல் சட்டத்தின் கீழ் தகுதிநீக்கக் காலம் 6 ஆண்டுகள்."},
                "B": {"en": "Incorrect. 3 years is wrong.", "ta": "தவறு. 3 ஆண்டுகள் என்பது தவறானது."},
                "C": {"en": "Incorrect. It is not lifelong disqualification.", "ta": "தவறு. இது ஆயுள் முழுவதுமான தகுதிநீக்கம் அல்ல."},
                "D": {"en": "Incorrect. Any conviction under PCR Act disqualifies regardless of sentence length.", "ta": "தவறு. தண்டனைக் காலத்தைப் பொருட்படுத்தாமல் எந்தவொரு தண்டனையும் தகுதிநீக்கம் செய்யும்."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: Article 35 of the Constitution confers exclusive power on Parliament to prescribe punishments for offences under Article 17 and Article 23.",
                "ta": "TNPSC குறிப்பு: பிரிவு 17 மற்றும் 23-ன் கீழ் உள்ள குற்றங்களுக்குத் தண்டனைகளை நிர்ணயிக்கும் பிரத்யேக அதிகாரத்தைப் பிரிவு 35 நாடாளுமன்றத்திற்கு மட்டுமே வழங்குகிறது."
            },
            "revision_fact": {
                "en": "Protection of Civil Rights Act 1955 puts the burden of proof on the accused, reversing standard criminal jurisprudence.",
                "ta": "குடிமை உரிமைகள் பாதுகாப்புச் சட்டம் 1955 குற்றஞ்சாட்டப்பட்டவர் மீதே நிரூபிக்கும் பொறுப்பைச் சுமத்துகிறது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Remember",
            "estimated_time_sec": 35,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 17", "Disqualification", "Grand Test"]
        },

        # Q19: Conceptual MCQ - Equality vs Special Provisions
        {
            "id": "FR_GT_019",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Medium",
            "question_type": "Conceptual MCQ",
            "question": {
                "en": "Article 15(3) empowers the State to make special provisions for women and children. This provision serves as a constitutional exception to which fundamental prohibition?",
                "ta": "பிரிவு 15(3) பெண்கள் மற்றும் குழந்தைகளுக்காகச் சிறப்பு விதிகளை உருவாக்க அரசிற்கு அதிகாரம் அளிக்கிறது. இந்த விதி எந்த அடிப்படைத் தடைக்கு அரசியலமைப்பு விதிவிலக்காகச் செயல்படுகிறது?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "Prohibition of discrimination on grounds ONLY of sex under Article 15(1)",
                    "ta": "பிரிவு 15(1)-ன் கீழ் பாலினத்தின் அடிப்படையில் மட்டுமே பாகுபாடு காட்டுவதற்கெதிரான தடை"
                },
                {
                    "id": "B",
                    "en": "Prohibition of untouchability under Article 17",
                    "ta": "பிரிவு 17-ன் கீழ் உள்ள தீண்டாமைத் தடை"
                },
                {
                    "id": "C",
                    "en": "Prohibition of titles under Article 18",
                    "ta": "பிரிவு 18-ன் கீழ் உள்ள பட்டங்கள் அளிப்பதற்கான தடை"
                },
                {
                    "id": "D",
                    "en": "Prohibition of ex-post facto laws under Article 20(1)",
                    "ta": "பிரிவு 20(1)-ன் கீழ் உள்ள பின்னோக்கிய சட்டங்களுக்கான தடை"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "Article 15(1) prohibits discrimination against citizens on grounds ONLY of religion, race, caste, sex, place of birth. Article 15(3) is an exception permitting protective discrimination / affirmative action in favor of women and children.",
                "ta": "பிரிவு 15(1) பாலினம் உள்ளிட்ட 5 அடிப்படைகளில் மட்டுமே பாகுபாட்டைத் தடை செய்கிறது. பிரிவு 15(3) பெண்கள் மற்றும் குழந்தைகளின் பாதுகாப்பிற்காகச் சாதகமான பாகுபாட்டை (protective discrimination) அனுமதிக்கிறது."
            },
            "why_not_others": {
                "A": {"en": "Correct. Article 15(3) enables protective discrimination for women & children.", "ta": "சரி. பிரிவு 15(3) பெண்களுக்கும் குழந்தைகளுக்கும் பாதுகாப்பான பாகுபாட்டை அளிக்கிறது."},
                "B": {"en": "Incorrect. Article 17 relates to untouchability.", "ta": "தவறு. பிரிவு 17 தீண்டாமை பற்றியது."},
                "C": {"en": "Incorrect. Article 18 relates to titles.", "ta": "தவறு. பிரிவு 18 பட்டங்கள் பற்றியது."},
                "D": {"en": "Incorrect. Article 20(1) relates to criminal ex-post facto law.", "ta": "தவறு. பிரிவு 20(1) குற்றவியல் சட்டங்கள் பற்றியது."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: Free education for girls, maternity benefits, and reservation of seats for women in local bodies (Art 243D/243T) are backed by Article 15(3).",
                "ta": "TNPSC குறிப்பு: பெண்களுக்கான இலவசக் கல்வி, மகப்பேறு சலுகைகள், உள்ளாட்சி அமைப்புகளில் பெண்களுக்கான இடஒதுக்கீடு ஆகியவை பிரிவு 15(3)-ன் ஆதரவைப் பெற்றுள்ளன."
            },
            "revision_fact": {
                "en": "Yusuf Abdul Aziz v. State of Bombay (1954) upheld Section 497 IPC (adultery penalizing only men) under Article 15(3), though Section 497 was later struck down in Joseph Shine v. UOI (2018).",
                "ta": "யூசுப் அப்துல் அஜீஸ் வழக்கில் (1954) 15(3)-ன் கீழ் 497 IPC உறுதி செய்யப்பட்டது, பின்னர் ஜோசப் ஷைன் வழக்கில் (2018) அது ரத்து செய்யப்பட்டது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Understand",
            "estimated_time_sec": 45,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 15", "Women Rights", "Grand Test"]
        },

        # Q20: Direct MCQ - 93rd Amendment Act 2005
        {
            "id": "FR_GT_020",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Easy",
            "question_type": "Direct MCQ",
            "question": {
                "en": "Under Article 15(5) inserted by the 93rd Amendment Act 2005, which category of educational institutions is EXEMPTED from reservation for SEBCs, SCs, and STs?",
                "ta": "93-வது திருத்தச் சட்டம் 2005 மூலம் இணைக்கப்பட்ட பிரிவு 15(5)-ன் கீழ், SEBC, SC, ST இடஒதுக்கீட்டிலிருந்து விலக்களிக்கப்பட்ட கல்வி நிறுவன வகை எது?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "Minority Educational Institutions referred to in Article 30(1)",
                    "ta": "பிரிவு 30(1)-ல் குறிப்பிடப்பட்டுள்ள சிறுபான்மை கல்வி நிறுவனங்கள்"
                },
                {
                    "id": "B",
                    "en": "Private Unaided Non-Minority Higher Educational Institutions",
                    "ta": "தனியார் சுயநிதி சிறுபான்மையற்ற உயர் கல்வி நிறுவனங்கள்"
                },
                {
                    "id": "C",
                    "en": "Government Aided Professional Colleges",
                    "ta": "அரசு உதவிபெறும் தொழிற்கல்லூரிகள்"
                },
                {
                    "id": "D",
                    "en": "Deemed Universities established under Central Acts",
                    "ta": "மத்தியச் சட்டங்களின் கீழ் அமைக்கப்பட்ட நிகர்நிலைப் பல்கலைக்கழகங்கள்"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "Article 15(5) enables reservation for OBCs/SCs/STs in all educational institutions (aided or unaided) EXCEPT minority educational institutions referred to in Article 30(1).",
                "ta": "பிரிவு 15(5) அனைத்துக் கல்வி நிறுவனங்களிலும் (அரசு மற்றும் தனியார் சுயநிதி) OBC/SC/ST இடஒதுக்கீட்டை அனுமதிக்கிறது, ஆனால் பிரிவு 30(1)-ன் கீழ் உள்ள சிறுபான்மை நிறுவனங்களுக்கு விலக்களிக்கிறது."
            },
            "why_not_others": {
                "A": {"en": "Correct. Minority institutions under Art 30(1) are explicitly exempted under Art 15(5).", "ta": "சரி. பிரிவு 30(1) சிறுபான்மை நிறுவனங்கள் பிரிவு 15(5)-லிருந்து வெளிப்படையாக விலக்கப்பட்டுள்ளன."},
                "B": {"en": "Incorrect. Private unaided non-minority institutions ARE covered under Art 15(5).", "ta": "தவறு. தனியார் சுயநிதி நிறுவனங்கள் 15(5)-ன் கீழ் அடங்கும்."},
                "C": {"en": "Incorrect. Government aided colleges are covered under Art 15(5).", "ta": "தவறு. அரசு உதவிபெறும் கல்லூரிகள் 15(5)-ன் கீழ் அடங்கும்."},
                "D": {"en": "Incorrect. Deemed universities are covered under Art 15(5).", "ta": "தவறு. நிகர்நிலைப் பல்கலைக்கழகங்கள் 15(5)-ன் கீழ் அடங்கும்."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: Central Educational Institutions (Reservation in Admission) Act 2006 implemented 27% OBC reservation in IITs, IIMs, AIIMS, and Central Universities under Art 15(5), upheld in Ashok Kumar Thakur v. UOI (2008).",
                "ta": "TNPSC குறிப்பு: 2006-ன் மத்தியக் கல்வி நிறுவனங்கள் சட்டத்தின் மூலம் IIT, IIM-களில் 27% OBC இடஒதுக்கீடு 15(5)-ன் கீழ் கொண்டுவரப்பட்டு அசோக் குமார் தாக்கூர் வழக்கில் (2008) உறுதி செய்யப்பட்டது."
            },
            "revision_fact": {
                "en": "Pramati Educational Trust v. UOI (2014) reaffirmed that excluding minority institutions from Art 15(5) does not violate Basic Structure.",
                "ta": "பிரமதி கல்வி அறக்கட்டளை வழக்கு (2014) பிரிவு 15(5)-லிருந்து சிறுபான்மை நிறுவனங்களை விலக்குவது அடிப்படை அமைப்பை மீறாது என்பதை மீண்டும் உறுதிப்படுத்தியது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Remember",
            "estimated_time_sec": 40,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 15(5)", "Minority Institutions", "Grand Test"]
        },

        # Q21: Hard / Analytical - Carry Forward Rule & 50% Limit
        {
            "id": "FR_GT_021",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Hard",
            "question_type": "Hard / Analytical",
            "question": {
                "en": "In Devadasan v. Union of India (1964), the Supreme Court struck down the 'Carry Forward Rule' because it led to reservation exceeding 50% in a given year. How did Parliament constitutionally nullify the effect of this judgment?",
                "ta": "தேவதாசன் எதிர் இந்திய யூனியன் (1964) வழக்கில், ஒரு குறிப்பிட்ட ஆண்டில் இடஒதுக்கீடு 50%-க்கு மேல் செல்லக் காரணமான 'கொண்டு செல்லும் விதியை' (Carry Forward Rule) உச்ச நீதிமன்றம் ரத்து செய்தது. இந்தத் தீர்ப்பின் விளைவை நாடாளுமன்றம் எவ்வாறு அரசியலமைப்பு ரீதியாகச் செல்லாததாக்கியது?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "By passing the 81st Constitutional Amendment Act 2000 inserting Article 16(4B)",
                    "ta": "2000-ன் 81-வது அரசியலமைப்புத் திருத்தச் சட்டத்தை இயற்றி பிரிவு 16(4B)-ஐ இணைத்ததன் மூலம்"
                },
                {
                    "id": "B",
                    "en": "By passing the 42nd Constitutional Amendment Act 1976 placing reservation in Ninth Schedule",
                    "ta": "1976-ன் 42-வது திருத்தச் சட்டத்தின் மூலம் இடஒதுக்கீட்டை 9-வது அட்டவணையில் சேர்த்ததன் மூலம்"
                },
                {
                    "id": "C",
                    "en": "By enacting an Ordinary Act under Article 35 bypassing judicial review",
                    "ta": "நீதித்துறை மறுஆய்வைத் தவிர்த்து பிரிவு 35-ன் கீழ் ஒரு சாதாரணச் சட்டத்தை இயற்றியதன் மூலம்"
                },
                {
                    "id": "D",
                    "en": "By amending Article 368 to restrict Supreme Court's writ jurisdiction under Article 32",
                    "ta": "பிரிவு 32-ன் கீழ் உச்ச நீதிமன்றத்தின் பேராணை அதிகாரத்தைக் குறைக்க பிரிவு 368-ஐத் திருத்தியதன் மூலம்"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "81st Amendment Act 2000 inserted Article 16(4B) providing that unfilled reserved backlog vacancies of a year shall be considered as a separate class of vacancies to be filled in any succeeding year and shall NOT be considered together with the vacancies of the year in determining the 50% ceiling.",
                "ta": "81-வது திருத்தச் சட்டம் 2000 பிரிவு 16(4B)-ஐ இணைத்தது. இதன்படி விடுபட்ட காலிப்பணியிடங்கள் அடுத்த ஆண்டுகளில் நிரப்பப்படும்போது தனி வகுப்பாகக் கருதப்படும், அ ஆண்டின் 50% வரம்போடு கணக்கிடப்படாது."
            },
            "why_not_others": {
                "A": {"en": "Correct. 81st Amendment Act 2000 added Art 16(4B) to override Devadasan decision limit.", "ta": "சரி. 81-வது திருத்தச் சட்டம் 16(4B)-ஐ இணைத்து தேவதாசன் தீர்ப்பை மாற்றியது."},
                "B": {"en": "Incorrect. 42nd Amendment did not address carry forward rule.", "ta": "தவறு. 42-வது திருத்தம் கொண்டு செல்லும் விதியைத் தொடவில்லை."},
                "C": {"en": "Incorrect. Ordinary law cannot bypass constitutional limits set by SC.", "ta": "தவறு. சாதாரணச் சட்டத்தால் அரசியலமைப்பு வரம்பை மீற முடியாது."},
                "D": {"en": "Incorrect. Parliament cannot restrict SC writ jurisdiction under Art 32.", "ta": "தவறு. பிரிவு 32 பேராணை அதிகாரத்தை நாடாளுமன்றம் குறைக்க முடியாது."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: In M. Nagaraj v. UOI (2006), the Supreme Court upheld the constitutional validity of 77th, 81st, 82nd, and 85th Amendment Acts.",
                "ta": "TNPSC குறிப்பு: எம். நாகராஜ் வழக்கில் (2006) 77, 81, 82, மற்றும் 85-வது திருத்தச் சட்டங்களின் செல்லுபடியாகும் தன்மை உச்ச நீதிமன்றத்தால் உறுதி செய்யப்பட்டது."
            },
            "revision_fact": {
                "en": "82nd Constitutional Amendment Act 2000 inserted a proviso to Article 335 allowing relaxation in qualifying marks or lowering standards of evaluation for SC/STs in promotion.",
                "ta": "82-வது திருத்தச் சட்டம் 2000 பிரிவு 335-ல் நிபந்தனையை இணைத்து SC/ST பிரிவினருக்குப் பதவி உயர்வுத் தேர்வுகளில் மதிப்பெண் தளர்வு வழங்க அனுமதித்தது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Analyze",
            "estimated_time_sec": 60,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 16(4B)", "81st Amendment", "Grand Test"]
        },

        # Q22: Direct MCQ - Fundamental Right against Exploitation / Untouchability
        {
            "id": "FR_GT_022",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Easy",
            "question_type": "Direct MCQ",
            "question": {
                "en": "Which Fundamental Right under Part III is directly enforced against private individuals as well as the State without requiring any further legislative enactment for its constitutional declaration?",
                "ta": "பகுதி III-ன் கீழ் உள்ள எந்த அடிப்படை உரிமை, அரசியலமைப்பு அறிவிப்பிற்கு மேலதிகச் சட்டங்கள் தேவையின்றி தனியாருக்கும் அரசிற்கும் எதிராக நேரடியாக அமல்படுத்தப்படக் கூடியது?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "Article 17 (Abolition of Untouchability)",
                    "ta": "பிரிவு 17 (தீண்டாமை ஒழிப்பு)"
                },
                {
                    "id": "B",
                    "en": "Article 19(1)(a) (Freedom of Speech)",
                    "ta": "பிரிவு 19(1)(a) (பேச்சுரிமை)"
                },
                {
                    "id": "C",
                    "en": "Article 14 (Equality before Law)",
                    "ta": "பிரிவு 14 (சட்டத்தின் முன் சமம்)"
                },
                {
                    "id": "D",
                    "en": "Article 30 (Right of Minorities to establish institutions)",
                    "ta": "பிரிவு 30 (சிறுபான்மையினர் நிறுவனங்களை நிறுவும் உரிமை)"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "Articles 15(2), 17, 23, and 24 are directly enforceable against private individuals. Article 17 specifically creates an absolute right enforceable horizontally against non-state private actors.",
                "ta": "பிரிவுகள் 15(2), 17, 23 மற்றும் 24 ஆகியவை தனியாருக்கு எதிராகவும் நேரடியாகச் செயல்படக் கூடியவை. பிரிவு 17 அரசுசாரா தனியார் நபர்களுக்கு எதிராக முற்றுமுழுதான உரிமையை உருவாக்குகிறது."
            },
            "why_not_others": {
                "A": {"en": "Correct. Article 17 is enforceable against both State and private actors.", "ta": "சரி. பிரிவு 17 அரசு மற்றும் தனியார் இருவருக்கும் எதிராக அமல்படுத்தப்படும்."},
                "B": {"en": "Incorrect. Article 19 is primarily enforceable against State action.", "ta": "தவறு. பிரிவு 19 முதன்மையாக அரசு நடவடிக்கைக்கு எதிரானது."},
                "C": {"en": "Incorrect. Article 14 is enforced against State action.", "ta": "தவறு. பிரிவு 14 அரசு நடவடிக்கைக்கு எதிரானது."},
                "D": {"en": "Incorrect. Article 30 guarantees rights against State interference in minority institutions.", "ta": "தவறு. பிரிவு 30 அரசுத் தலையீட்டிற்கு எதிரான உரிமை."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: Fundamental Rights that operate against private individuals: Art 15(2) (access to shops/public places), Art 17 (untouchability), Art 23 (begar/forced labor), Art 24 (child labor).",
                "ta": "TNPSC குறிப்பு: தனியாருக்கு எதிராகச் செயல்படும் அடிப்படை உரிமைகள்: 15(2) (கடைகள்/பொது இடப் பயன்பாடு), 17 (தீண்டாமை), 23 (கொத்தடிமை/கட்டாய வேலை), 24 (குழந்தைத் தொழிலாளர்)."
            },
            "revision_fact": {
                "en": "In People's Union for Democratic Rights v. Union of India (Asiad Workers case 1982), Supreme Court held that Article 23 is enforceable against private contractors as well.",
                "ta": "ஆசியட் தொழிலாளர்கள் வழக்கில் (1982) பிரிவு 23 தனியார் ஒப்பந்தக்காரர்களுக்கு எதிராகவும் செயல்படும் என உச்ச நீதிமன்றம் தீர்ப்பளித்தது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Remember",
            "estimated_time_sec": 35,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 17", "Horizontal Rights", "Grand Test"]
        },

        # Q23: Conceptual MCQ - Scope of Law under Art 13
        {
            "id": "FR_GT_023",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Medium",
            "question_type": "Conceptual MCQ",
            "question": {
                "en": "What is the legal status of an unconstitutional post-constitutional law enacted by Parliament that violates Part III of the Constitution under Article 13(2)?",
                "ta": "இந்திய அரசியலமைப்பின் 13(2) பிரிவின் கீழ் பகுதி III-ஐ மீறி நாடாளுமன்றத்தால் இயற்றப்படும் அரசியலமைப்புக்கு முரணான பிந்தைய சட்டத்தின் சட்டப்பூர்வ நிலை என்ன?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "It is void ab initio (stillborn) and completely unenforceable from its inception",
                    "ta": "இது ஆரம்பத்திலிருந்தே (void ab initio / stillborn) முற்றிலும் செல்லாதது மற்றும் நடைமுறைப்படுத்த முடியாதது"
                },
                {
                    "id": "B",
                    "en": "It remains valid until the President formally revokes it under Article 123",
                    "ta": "குடியரசுத் தலைவர் பிரிவு 123-ன் கீழ் அதிகாரப்பூர்வமாக அதைத் திரும்பப் பெறும் வரை செல்லுபடியாகும்"
                },
                {
                    "id": "C",
                    "en": "It remains dormant and revives automatically after 5 years",
                    "ta": "இது முடங்கிக் கிடந்து 5 ஆண்டுகளுக்குப் பிறகு தானாகவே உயிர்பெறும்"
                },
                {
                    "id": "D",
                    "en": "It applies only to non-citizens and foreign legal entities",
                    "ta": "இது குடிமக்கள் அல்லாதோர் மற்றும் வெளிநாட்டு நிறுவனங்களுக்கு மட்டுமே பொருந்தும்"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "Under Deep Chand v. State of UP (1959) and Mahendra Lal Jaini v. State of UP (1963), a post-constitutional law violating Art 13(2) is void ab initio (stillborn). The Doctrine of Eclipse does NOT apply to post-constitutional laws against citizens.",
                "ta": "தீப் சந்த் எதிர் உ.பி அரசு (1959) வழக்கின்படி, பிரிவு 13(2)-ஐ மீறும் அரசியலமைப்புக்குப் பிந்தைய சட்டம் பிறப்பிலேயே செல்லாதது (void ab initio). மறைப்புக் கோட்பாடு குடிமக்களுக்கு எதிரான பிந்தைய சட்டங்களுக்குப் பொருந்தாது."
            },
            "why_not_others": {
                "A": {"en": "Correct. Post-constitutional laws violating Art 13(2) are stillborn and void ab initio.", "ta": "சரி. பிரிவு 13(2)-ஐ மீறும் பிந்தைய சட்டங்கள் பிறப்பிலேயே செல்லாதவை."},
                "B": {"en": "Incorrect. Executive or presidential revocation is not needed; courts declare it void.", "ta": "தவறு. நீதிமன்றமே செல்லாது என அறிவிக்கும், குடியரசுத் தலைவர் ரத்து தேவை இல்லை."},
                "C": {"en": "Incorrect. Stillborn laws cannot revive automatically without re-enactment after constitutional amendment.", "ta": "தவறு. இறந்து பிறந்த சட்டங்கள் தானாக உயிர்பெற முடியாது."},
                "D": {"en": "Incorrect. Unconstitutional laws violating Part III are void.", "ta": "தவறு. பகுதி III-ஐ மீறும் சட்டங்கள் முழுமையாகச் செல்லாதவை."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Trap: Key distinction: Pre-constitutional laws violating Art 13(1) are eclipsed (dormant). Post-constitutional laws violating Art 13(2) are stillborn (void ab initio).",
                "ta": "TNPSC பொறி: முக்கிய வேறுபாடு: 13(1)-ன் கீழ் உள்ள முந்தைய சட்டங்கள் மறைக்கப்படும் (முடங்கும்). 13(2)-ன் கீழ் உள்ள பிந்தைய சட்டங்கள் பிறப்பிலேயே செல்லாதவை."
            },
            "revision_fact": {
                "en": "Article 13(2) explicitly commands: 'The State shall not make any law which takes away or abridges the rights conferred by this Part'.",
                "ta": "பிரிவு 13(2) வெளிப்படையாகக் கட்டளையிடுகிறது: 'இந்தப் பகுதியில் வழங்கப்பட்டுள்ள உரிமைகளைப் பறிக்கும் அல்லது குறைக்கும் எந்தவொரு சட்டத்தையும் அரசு இயற்றக்கூடாது'."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Understand",
            "estimated_time_sec": 45,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 13(2)", "Void Ab Initio", "Grand Test"]
        },

        # Q24: Statement-Based - Article 15 Exceptions
        {
            "id": "FR_GT_024",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Medium",
            "question_type": "Statement-Based",
            "question": {
                "en": "Consider the following statements regarding the exceptions to Article 15:\n1. Article 15(3) permits special provisions for women and children.\n2. Article 15(4) was added by the 1st Constitutional Amendment Act 1951 following the Champakam Dorairajan case.\n3. Article 15(5) permits reservation in educational institutions including minority educational institutions covered under Article 30(1).\nWhich of the statements given above are correct?",
                "ta": "பிரிவு 15-ன் விதிவிலக்குகள் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. பிரிவு 15(3) பெண்கள் மற்றும் குழந்தைகளுக்கான சிறப்பு விதிகளை அனுமதிக்கிறது.\n2. செண்பகம் துரைராஜன் வழக்கைத் தொடர்ந்து 1951-ன் 1-வது அரசியலமைப்புத் திருத்தச் சட்டத்தின் மூலம் பிரிவு 15(4) சேர்க்கப்பட்டது.\n3. பிரிவு 15(5) பிரிவு 30(1)-ன் கீழ் உள்ள சிறுபான்மைக் கல்வி நிறுவனங்கள் உட்பட அனைத்துக் கல்வி நிறுவனங்களிலும் இடஒதுக்கீட்டை அனுமதிக்கிறது.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "1 and 2 only",
                    "ta": "1 மற்றும் 2 மட்டுமே"
                },
                {
                    "id": "B",
                    "en": "2 and 3 only",
                    "ta": "2 மற்றும் 3 மட்டுமே"
                },
                {
                    "id": "C",
                    "en": "1 and 3 only",
                    "ta": "1 மற்றும் 3 மட்டுமே"
                },
                {
                    "id": "D",
                    "en": "1, 2 and 3",
                    "ta": "1, 2 மற்றும் 3"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "Statements 1 and 2 are correct. Statement 3 is INCORRECT: Article 15(5) explicitly EXCLUDES minority educational institutions referred to in Article 30(1) from reservation requirements.",
                "ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது: பிரிவு 15(5) பிரிவு 30(1)-ன் கீழ் உள்ள சிறுபான்மைக் கல்வி நிறுவனங்களை இடஒதுக்கீட்டிலிருந்து வெளிப்படையாக விலக்குகிறது."
            },
            "why_not_others": {
                "A": {"en": "Correct. Statements 1 and 2 are true; statement 3 is false.", "ta": "சரி. கூற்றுகள் 1 மற்றும் 2 சரியானவை; கூற்று 3 தவறானது."},
                "B": {"en": "Incorrect because statement 3 is false.", "ta": "தவறு, ஏனெனில் கூற்று 3 தவறானது."},
                "C": {"en": "Incorrect because statement 3 is false.", "ta": "தவறு, ஏனெனில் கூற்று 3 தவறானது."},
                "D": {"en": "Incorrect because statement 3 is false.", "ta": "தவறு, ஏனெனில் கூற்று 3 தவறானது."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Trap: Minority educational institutions under Art 30(1) enjoy immunity from Art 15(5) reservations, but NOT from general academic standards and teacher qualification regulations.",
                "ta": "TNPSC பொறி: சிறுபான்மை நிறுவனங்களுக்கு பிரிவு 15(5) இடஒதுக்கீட்டிலிருந்து மட்டுமே விலக்கு உண்டு, பொதுக் கல்வித் தரம் மற்றும் ஆசிரியர் தகுதி விதிகளிலிருந்து விலக்கு இல்லை."
            },
            "revision_fact": {
                "en": "1st Constitutional Amendment 1951 introduced Article 15(4) enabling special provisions for socially and educationally backward classes (SEBCs) or SCs/STs.",
                "ta": "1-வது அரசியலமைப்புத் திருத்தம் 1951, சமூக ரீதியாகவும் கல்வி ரீதியாகவும் பின்தங்கிய வகுப்பினருக்காக (SEBC) பிரிவு 15(4)-ஐ அறிமுகப்படுத்தியது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Analyze",
            "estimated_time_sec": 50,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 15", "Minority Exemption", "Grand Test"]
        },

        # Q25: Direct MCQ - Mandal Case 50% Rule
        {
            "id": "FR_GT_025",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Easy",
            "question_type": "Direct MCQ",
            "question": {
                "en": "In the landmark Mandal Case (Indra Sawhney v. Union of India, 1992), what total percentage cap was laid down by the Supreme Court on reservations in public services under normal circumstances?",
                "ta": "முக்கியத்துவமிக்க மண்டல் வழக்கில் (இந்திரா சாஹ்னி எதிர் இந்திய யூனியன், 1992), சாதாரண சூழ்நிலைகளில் பொதுப் பணிகளிலான இடஒதுக்கீட்டிற்கு உச்ச நீதிமன்றம் விதித்த மொத்த சதவீத உச்சவரம்பு என்ன?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "50%",
                    "ta": "50%"
                },
                {
                    "id": "B",
                    "en": "27%",
                    "ta": "27%"
                },
                {
                    "id": "C",
                    "en": "69%",
                    "ta": "69%"
                },
                {
                    "id": "D",
                    "en": "33%",
                    "ta": "33%"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "In Indra Sawhney case (1992), a 9-judge bench ruled by 6:3 majority that total reservation under Article 16(4) should not exceed 50% of seats/posts in a year, except in extraordinary cases for remote/far-flung areas.",
                "ta": "இந்திரா சாஹ்னி வழக்கில் (1992) 9 நீதிபதிகள் கொண்ட அமர்வு 6:3 பெரும்பான்மையில் பிரிவு 16(4)-ன் கீழ் மொத்த இடஒதுக்கீடு 50%-க்கு மிகக்கூடாது எனத் தீர்ப்பளித்தது (தூரப் பகுதிகளுக்கான அசாதாரண சூழ்நிலைகளைத் தவிர)."
            },
            "why_not_others": {
                "A": {"en": "Correct. 50% total reservation ceiling was established in Indra Sawhney.", "ta": "சரி. 50% மொத்த இடஒதுக்கீட்டு உச்சவரம்பு இந்திரா சாஹ்னியில் நிறுவப்பட்டது."},
                "B": {"en": "Incorrect. 27% is the quota specifically allocated for OBCs.", "ta": "தவறு. 27% என்பது OBC-களுக்கான குறிப்பிட்ட இடஒதுக்கீடு ஆகும்."},
                "C": {"en": "Incorrect. 69% is Tamil Nadu's specific reservation law protected under Ninth Schedule.", "ta": "தவறு. 69% என்பது 9-வது அட்டவணையில் உள்ள தமிழ்நாட்டின் இடஒதுக்கீடு ஆகும்."},
                "D": {"en": "Incorrect. 33% is the proposed quota for women in legislatures.", "ta": "தவறு. 33% என்பது சட்டமன்றங்களில் பெண்களுக்கான முன்மொழியப்பட்ட இடஒதுக்கீடு."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: Indra Sawhney judgment also held: (1) No reservation in promotion under 16(4), (2) Executive orders can grant reservation, (3) Backward classes must be identified primarily by social backwardness.",
                "ta": "TNPSC குறிப்பு: இந்திரா சாஹ்னி தீர்ப்பு மேலும் கூறியது: (1) 16(4)-ன் கீழ் பதவி உயர்வில் இடஒதுக்கீடு இல்லை, (2) நிர்வாக உத்தரவுகள் மூலம் இடஒதுக்கீடு வழங்கலாம்."
            },
            "revision_fact": {
                "en": "77th Constitutional Amendment Act 1995 was passed to override the prohibition of reservation in promotion laid down in Indra Sawhney case.",
                "ta": "இந்திரா சாஹ்னி வழக்கில் விதிக்கப்பட்ட பதவி உயர்வு இடஒதுக்கீட்டுத் தடையை நீக்க 77-வது திருத்தச் சட்டம் 1995 இயற்றப்பட்டது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Remember",
            "estimated_time_sec": 35,
            "pyq_similarity": "High",
            "tags": ["Polity", "Indra Sawhney", "50 Percent Rule", "Grand Test"]
        },

        # Q26: Conceptual MCQ - Reasonable Restrictions on Equality
        {
            "id": "FR_GT_026",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Medium",
            "question_type": "Conceptual MCQ",
            "question": {
                "en": "Which of the following is NOT a permissible ground for reasonable classification or exception under Article 15?",
                "ta": "பிரிவு 15-ன் கீழ் நியாயமான வகைப்பாடு அல்லது விதிவிலக்கிற்கான அனுமதிக்கப்பட்ட அடிப்படை அல்லாதது எது?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "Classification based purely on political party affiliation",
                    "ta": "அரசியல் கட்சிச் சார்பின் அடிப்படையில் மட்டுமே செய்யப்படும் வகைப்பாடு"
                },
                {
                    "id": "B",
                    "en": "Special provisions for advancement of socially and educationally backward classes",
                    "ta": "சமூக ரீதியாகவும் கல்வி ரீதியாகவும் பின்தங்கிய வகுப்பினரின் முன்னேற்றத்திற்கான சிறப்பு விதிகள்"
                },
                {
                    "id": "C",
                    "en": "Special provisions for women and children",
                    "ta": "பெண்கள் மற்றும் குழந்தைகளுக்கான சிறப்பு விதிகள்"
                },
                {
                    "id": "D",
                    "en": "Special provisions for Economically Weaker Sections of citizens",
                    "ta": "பொருளாதாரத்தில் பின்தங்கிய குடிமக்களுக்கான சிறப்பு விதிகள்"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "Article 15 permits special provisions for women, children, SEBCs, SCs, STs (15(3), 15(4), 15(5)) and EWS (15(6)). Arbitrary classification based solely on political party affiliation is unconstitutional and violates Article 14 & 15.",
                "ta": "பிரிவு 15 பெண்கள், குழந்தைகள், SEBC, SC, ST, EWS ஆகியோருக்குச் சிறப்பு விதிகளை அனுமதிக்கிறது. அரசியல் கட்சிச் சார்பின் அடிப்படையில் மட்டுமே செய்யப்படும் பாகுபாடு அரசியலமைப்புக்கு முரணானது."
            },
            "why_not_others": {
                "A": {"en": "Correct. Political party affiliation is an impermissible ground for discrimination.", "ta": "சரி. அரசியல் கட்சிச் சார்பு என்பது அனுமதிக்கப்படாத பாகுபாட்டின் அடிப்படையாகும்."},
                "B": {"en": "Incorrect. SEBC advancement is explicitly allowed under Art 15(4) and 15(5).", "ta": "தவறு. SEBC முன்னேற்றம் 15(4) மற்றும் 15(5)-ல் அனுமதிக்கப்பட்டுள்ளது."},
                "C": {"en": "Incorrect. Women & children special provisions are allowed under Art 15(3).", "ta": "தவறு. பெண்கள் & குழந்தைகள் சிறப்பு விதிகள் 15(3)-ல் அனுமதிக்கப்பட்டுள்ளன."},
                "D": {"en": "Incorrect. EWS provisions are explicitly allowed under Art 15(6).", "ta": "தவறு. EWS விதிகள் 15(6)-ல் அனுமதிக்கப்பட்டுள்ளன."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: Discrimination is prohibited under Art 15 ONLY on 5 grounds (Religion, Race, Caste, Sex, Place of birth). Discrimination on OTHER grounds (like domicile/residence or income) is not barred by 15(1).",
                "ta": "TNPSC குறிப்பு: பிரிவு 15(1)-ல் 5 குறிப்பிட்ட அடிப்படைகளில் மட்டுமே பாகுபாடு தடை செய்யப்பட்டுள்ளது. பிற அடிப்படையில் (இருப்பிடம், வருமானம்) பாகுபாடு காட்டுவது 15(1)-ல் தடையல்ல."
            },
            "revision_fact": {
                "en": "State of Rajasthan v. Pratap Singh (1960) held that levying cost of additional police force on inhabitants of a locality based on religion/caste violated Article 15(1).",
                "ta": "ராஜஸ்தான் அரசு வழக்கில் (1960) மதம்/சாதி அடிப்படையில் கூடுதல் காவல் செலவை ஒரு குறிப்பிட்ட பகுதி வாழ் மக்கள் மீது விதிப்பது பிரிவு 15(1)-ஐ மீறுகிறது எனப்பட்டது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Understand",
            "estimated_time_sec": 45,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 15", "Non Discrimination", "Grand Test"]
        },

        # Q27: Direct MCQ - Article 16(3) Residence Requirement
        {
            "id": "FR_GT_027",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Medium",
            "question_type": "Direct MCQ",
            "question": {
                "en": "Who among the following has the constitutional authority under Article 16(3) to prescribe residence as a requirement for employment or appointment in a State or Union Territory?",
                "ta": "ஒரு மாநிலம் அல்லது யூனியன் பிரதேசத்தில் வேலைவாய்ப்பு அல்லது பணிநியமனத்திற்கு இருப்பிடத்தைக் கட்டாய நிபந்தனையாக நிர்ணயிக்கப் பிரிவு 16(3)-ன் கீழ் அரசியலமைப்பு அதிகாரம் பெற்றவர் யார்?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "Parliament of India alone",
                    "ta": "இந்திய நாடாளுமன்றம் மட்டுமே"
                },
                {
                    "id": "B",
                    "en": "The concerned State Legislature",
                    "ta": "தொடர்புடைய மாநில சட்டமன்றம்"
                },
                {
                    "id": "C",
                    "en": "The Governor of the State in consultation with High Court",
                    "ta": "உயர் நீதிமன்றத்தைக் கலந்தாலோசித்து மாநில ஆளுநர்"
                },
                {
                    "id": "D",
                    "en": "Union Public Service Commission (UPSC)",
                    "ta": "மத்திய அரசுப் பணியாளர் தேர்வாணையம் (UPSC)"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "Under Article 16(3), ONLY Parliament (by law) can prescribe residence as a requirement within a State or Union Territory for specified public employment. State Legislatures CANNOT enact such laws.",
                "ta": "பிரிவு 16(3)-ன் கீழ், குறிப்பிட்ட பொது வேலைவாய்ப்பிற்கு ஒரு மாநிலம்/யூனியன் பிரதேசத்தில் இருப்பிடத்தைக் கட்டாய நிபந்தனையாகப் பாராளுமன்றம் மட்டுமே (சட்டம் மூலம்) விதிக்க முடியும். மாநில சட்டமன்றங்களுக்கு இந்த அதிகாரம் இல்லை."
            },
            "why_not_others": {
                "A": {"en": "Correct. Parliament alone possesses power under Art 16(3) read with Art 35(a)(i).", "ta": "சரி. பிரிவு 16(3) மற்றும் 35(a)(i)-ன் படி நாடாளுமன்றத்திற்கு மட்டுமே அதிகாரம் உண்டு."},
                "B": {"en": "Incorrect. State Legislature has no power to prescribe residence requirement under Art 16(3).", "ta": "தவறு. மாநில சட்டமன்றத்திற்கு இந்த அதிகாரம் இல்லை."},
                "C": {"en": "Incorrect. Governor has no independent legislative power to alter employment grounds.", "ta": "தவறு. ஆளுநருக்கு இந்த அதிகாரம் இல்லை."},
                "D": {"en": "Incorrect. UPSC is an advisory/recruiting body, not a legislative body.", "ta": "தவறு. UPSC ஒரு ஆலோசனைக் குழுவே தவிர சட்டமன்றம் அல்ல."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Trap: Parliament enacted the Public Employment (Requirement as to Residence) Act 1957. Currently, special residence provisions exist for Andhra Pradesh and Telangana under Article 371D.",
                "ta": "TNPSC பொறி: நாடாளுமன்றம் 1957-ல் பொது வேலைவாய்ப்பு (இருப்பிட நிபந்தனை) சட்டத்தை இயற்றியது. தற்போது ஆந்திரா மற்றும் தெலங்கானாவிற்கு பிரிவு 371D-ன் கீழ் சிறப்பு இருப்பிட விதிகள் உள்ளன."
            },
            "revision_fact": {
                "en": "A.V.S. Narasimha Rao v. State of AP (1969) held that residence requirement under Art 16(3) can be prescribed for an entire State, but NOT for a specific region within a State.",
                "ta": "நரசிம்ம ராவ் வழக்கில் (1969) பிரிவு 16(3) இருப்பிட நிபந்தனை ஒரு மாநிலம் முழுவதற்கும் விதிக்கப்படலாம், ஆனால் மாநிலத்திற்குள் ஒரு குறிப்பிட்ட பகுதிக்கு மட்டும் விதிக்கப்படக் கூடாது எனப்பட்டது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Remember",
            "estimated_time_sec": 40,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 16(3)", "Residence Requirement", "Grand Test"]
        },

        # Q28: Chronology - Constitutional Amendments on Reservations
        {
            "id": "FR_GT_028",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Hard",
            "question_type": "Chronology",
            "question": {
                "en": "Arrange the following Constitutional Amendment Acts relating to Fundamental Rights in chronological sequence:\n1. 77th Amendment Act (Reservation in promotion for SCs/STs)\n2. 86th Amendment Act (Right to Education Art 21A)\n3. 93rd Amendment Act (OBC reservation in private educational institutions)\n4. 103rd Amendment Act (10% EWS reservation)",
                "ta": "அடிப்படை உரிமைகள் தொடர்பான பின்வரும் அரசியலமைப்புத் திருத்தச் சட்டங்களைச் சரியான காலவரிசையில் அமைக்கவும்:\n1. 77-வது திருத்தச் சட்டம் (SC/ST-க்கு பதவி உயர்வில் இடஒதுக்கீடு)\n2. 86-வது திருத்தச் சட்டம் (கல்வி உரிமை பிரிவு 21A)\n3. 93-வது திருத்தச் சட்டம் (தனியார் கல்வி நிறுவனங்களில் OBC இடஒதுக்கீடு)\n4. 103-வது திருத்தச் சட்டம் (10% EWS இடஒதுக்கீடு)"
            },
            "options": [
                {
                    "id": "A",
                    "en": "1 - 2 - 3 - 4",
                    "ta": "1 - 2 - 3 - 4"
                },
                {
                    "id": "B",
                    "en": "2 - 1 - 4 - 3",
                    "ta": "2 - 1 - 4 - 3"
                },
                {
                    "id": "C",
                    "en": "1 - 3 - 2 - 4",
                    "ta": "1 - 3 - 2 - 4"
                },
                {
                    "id": "D",
                    "en": "3 - 1 - 2 - 4",
                    "ta": "3 - 1 - 2 - 4"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "Correct chronological order: (1) 77th Amendment Act (1995) -> Art 16(4A); (2) 86th Amendment Act (2002) -> Art 21A; (3) 93rd Amendment Act (2005) -> Art 15(5); (4) 103rd Amendment Act (2019) -> Art 15(6) and 16(6).",
                "ta": "சரியான காலவரிசை: (1) 77-வது திருத்தம் (1995) -> 16(4A); (2) 86-வது திருத்தம் (2002) -> 21A; (3) 93-வது திருத்தம் (2005) -> 15(5); (4) 103-வது திருத்தம் (2019) -> 15(6), 16(6)."
            },
            "why_not_others": {
                "A": {"en": "Correct sequence: 1995 -> 2002 -> 2005 -> 2019.", "ta": "சரியான வரிசை: 1995 -> 2002 -> 2005 -> 2019."},
                "B": {"en": "Incorrect sequence.", "ta": "தவறான வரிசை."},
                "C": {"en": "Incorrect sequence.", "ta": "தவறான வரிசை."},
                "D": {"en": "Incorrect sequence.", "ta": "தவறான வரிசை."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: Memorize years of key FR Amendments: 1st (1951), 24th (1971), 25th (1971), 44th (1978), 77th (1995), 81st (2000), 86th (2002), 93rd (2005), 103rd (2019).",
                "ta": "TNPSC குறிப்பு: முக்கியத் திருத்தங்களின் ஆண்டுகள்: 1-வது (1951), 24-வது (1971), 44-வது (1978), 77-வது (1995), 86-வது (2002), 93-வது (2005), 103-வது (2019)."
            },
            "revision_fact": {
                "en": "103rd Amendment Act 2019 was enacted during the tenure of Prime Minister Narendra Modi.",
                "ta": "103-வது திருத்தச் சட்டம் 2019 பிரதமர் நரேந்திர மோடியின் ஆட்சிக் காலத்தில் இயற்றப்பட்டது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Analyze",
            "estimated_time_sec": 55,
            "pyq_similarity": "High",
            "tags": ["Polity", "Amendments", "Chronology", "Grand Test"]
        },

        # Q29: Match the Following - Doctrines of Constitutional Law
        {
            "id": "FR_GT_029",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Medium",
            "question_type": "Match the Following",
            "question": {
                "en": "Match List-I (Constitutional Doctrine) with List-II (Landmark Supreme Court Case):\nList-I:\na. Doctrine of Severability\nb. Doctrine of Eclipse\nc. Doctrine of Waiver of Rights\nd. New Doctrine of Equality (Arbitrariness test)\n\nList-II:\n1. E.P. Royappa v. State of Tamil Nadu (1974)\n2. Basheshar Nath v. CIT (1959)\n3. R.M.D. Chamarbaugwalla v. Union of India (1957)\n4. Bhikaji Narain v. State of MP (1955)",
                "ta": "பட்டியல்-I-ஐ (அரசியலமைப்புப் கோட்பாடு) பட்டியல்-II-உடன் (முக்கிய உச்ச நீதிமன்ற வழக்கு) பொருத்துக:\nபட்டியல்-I:\na. பிரிக்கக்கூடிய கோட்பாடு (Severability)\nb. மறைப்புக் கோட்பாடு (Eclipse)\nc. உரிமைகளைத் துறக்கும் கோட்பாடு (Waiver)\nd. புதிய சமத்துவக் கோட்பாடு (தன்னிச்சையான சோதனை)\n\nபட்டியல்-II:\n1. ஈ.பி. ராயப்பா எதிர் தமிழ்நாடு அரசு (1974)\n2. பஷேஷர் நாத் எதிர் வருமான வரி ஆணையர் (1959)\n3. R.M.D. சாமர்பாகவாலா எதிர் இந்திய யூனியன் (1957)\n4. பிகாஜி நரேன் எதிர் மத்தியப் பிரதேச அரசு (1955)"
            },
            "options": [
                {
                    "id": "A",
                    "en": "a-3, b-4, c-2, d-1",
                    "ta": "a-3, b-4, c-2, d-1"
                },
                {
                    "id": "B",
                    "en": "a-4, b-3, c-1, d-2",
                    "ta": "a-4, b-3, c-1, d-2"
                },
                {
                    "id": "C",
                    "en": "a-3, b-2, c-4, d-1",
                    "ta": "a-3, b-2, c-4, d-1"
                },
                {
                    "id": "D",
                    "en": "a-1, b-4, c-2, d-3",
                    "ta": "a-1, b-4, c-2, d-3"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "Correct matching: Severability -> R.M.D. Chamarbaugwalla (1957); Eclipse -> Bhikaji Narain (1955); Waiver -> Basheshar Nath (1959); New Doctrine of Equality -> E.P. Royappa (1974).",
                "ta": "சரியான பொருத்தம்: பிரிக்கக்கூடிய கோட்பாடு -> சாமர்பாகவாலா (1957); மறைப்புக் கோட்பாடு -> பிகாஜி நரேன் (1955); உரிமைகளைத் துறத்தல் -> பஷேஷர் நாத் (1959); புதிய சமத்துவக் கோட்பாடு -> ராயப்பா (1974)."
            },
            "why_not_others": {
                "A": {"en": "Correct match: a-3, b-4, c-2, d-1.", "ta": "சரியான பொருத்தம்: a-3, b-4, c-2, d-1."},
                "B": {"en": "Incorrect mapping.", "ta": "தவறான பொருத்தம்."},
                "C": {"en": "Incorrect mapping.", "ta": "தவறான பொருத்தம்."},
                "D": {"en": "Incorrect mapping.", "ta": "தவறான பொருத்தம்."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: Maneka Gandhi v. UOI (1978) adopted the E.P. Royappa arbitrariness test and integrated Article 14, 19, and 21 into the 'Golden Triangle' of the Constitution.",
                "ta": "TNPSC குறிப்பு: மேனகா காந்தி வழக்கு (1978) ராயப்பா வழக்கின் தன்னிச்சையான சோதனையை ஏற்றுக்கொண்டு 14, 19, 21-ஐ அரசியலமைப்பின் 'பொன் முக்கோணம்' ஆக்கியது."
            },
            "revision_fact": {
                "en": "In Maneka Gandhi case, Supreme Court held that procedure established by law under Art 21 must not be arbitrary, fanciful or oppressive, but just, fair and reasonable.",
                "ta": "மேனகா காந்தி வழக்கில், பிரிவு 21-ன் கீழ் சட்டம் அமைத்த நடைமுறை தன்னிச்சையானதாக இருக்கக்கூடாது, நியாயமானதாக இருக்க வேண்டும் எனக் கூறப்பட்டது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Analyze",
            "estimated_time_sec": 60,
            "pyq_similarity": "High",
            "tags": ["Polity", "Doctrines", "Match the Following", "Grand Test"]
        },

        # Q30: TNPSC Trap - Article 18 Military vs Civilian Awards
        {
            "id": "FR_GT_030",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Medium",
            "question_type": "TNPSC Trap",
            "question": {
                "en": "Which of the following distinctions is explicitly permitted under Article 18(1) of the Constitution of India?",
                "ta": "இந்திய அரசியலமைப்பின் 18(1) பிரிவின் கீழ் வெளிப்படையாக அனுமதிக்கப்பட்ட வேறுபாடு/சிறப்பு எது?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "Military and Academic distinctions",
                    "ta": "ராணுவ மற்றும் கல்விச் சிறப்புகள்"
                },
                {
                    "id": "B",
                    "en": "Hereditary titles conferred by princely states",
                    "ta": "சுதேச சமஸ்தானங்களால் வழங்கப்பட்ட பரம்பரைப் பட்டங்கள்"
                },
                {
                    "id": "C",
                    "en": "Titles conferred by foreign governments on Indian diplomats",
                    "ta": "இந்திய ராஜதந்திரிகளுக்கு வெளிநாட்டு அரசாங்கங்களால் வழங்கப்படும் பட்டங்கள்"
                },
                {
                    "id": "D",
                    "en": "Zamindari and Raiyatwari landed titles",
                    "ta": "ஜமீன்தாரி மற்றும் ராயத்வாரி நிலப் பட்டங்கள்"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "Article 18(1) states: 'No title, not being a military or academic distinction, shall be conferred by the State'. Thus, Military distinctions (e.g. Param Vir Chakra, Major) and Academic distinctions (e.g. Doctorate, Professor) are explicitly permitted.",
                "ta": "பிரிவு 18(1) கூறுகிறது: 'ராணுவ அல்லது கல்விச் சிறப்பு அல்லாத வேறு எந்தப் பட்டத்தையும் அரசு வழங்கக் கூடாது'. எனவே ராணுவ மற்றும் கல்விச் சிறப்புகள் வெளிப்படையாக அனுமதிக்கப்படுகின்றன."
            },
            "why_not_others": {
                "A": {"en": "Correct. Military and Academic distinctions are explicitly allowed under Art 18(1).", "ta": "சரி. ராணுவ மற்றும் கல்விச் சிறப்புகள் பிரிவு 18(1)-ல் வெளிப்படையாக அனுமதிக்கப்பட்டுள்ளன."},
                "B": {"en": "Incorrect. Hereditary titles are completely abolished by Art 18.", "ta": "தவறு. பரம்பரைப் பட்டங்கள் முற்றிலும் ஒழிக்கப்பட்டுவிட்டன."},
                "C": {"en": "Incorrect. Article 18(2) prohibits citizens from accepting titles from foreign States.", "ta": "தவறு. பிரிவு 18(2) வெளிநாட்டுப் பட்டங்களை ஏற்பதைத் தடை செய்கிறது."},
                "D": {"en": "Incorrect. Landed feudal titles are abolished.", "ta": "தவறு. நிலப் பிரபுத்துவப் பட்டங்கள் ஒழிக்கப்பட்டுவிட்டன."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Trap: While military titles (like General, Captain) can be used as prefix to a name, National Awards (like Bharat Ratna, Padma Shri) CANNOT be used as prefix or suffix!",
                "ta": "TNPSC பொறி: ராணுவப் பட்டங்களைப் (ஜெனரல், கேப்டன்) பெயருக்கு முன் பயன்படுத்தலாம், ஆனால் பாரத ரத்னா போன்ற தேசிய விருதுகளை பெயருக்கு முன்/பின் பயன்படுத்தக் கூடாது!"
            },
            "revision_fact": {
                "en": "Article 18(3) and 18(4) prohibit non-citizens holding office of profit under the State from accepting foreign titles or presents without the consent of the President.",
                "ta": "பிரிவு 18(3) மற்றும் 18(4) அரசுப் பதவியில் உள்ள வெளிநாட்டினர் குடியரசுத் தலைவரின் ஒப்புதலின்றி வெளிநாட்டுப் பரிசுகள்/பட்டங்களை ஏற்பதைத் தடை செய்கின்றன."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Understand",
            "estimated_time_sec": 40,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 18", "Military Distinction", "Grand Test"]
        },

        # Q31: Conceptual MCQ - Reservation in Promotion & Consequential Seniority
        {
            "id": "FR_GT_031",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Hard",
            "question_type": "Conceptual MCQ",
            "question": {
                "en": "The concept of 'Consequential Seniority' in reservation in promotion for SC/ST employees was constitutionally incorporated by which Amendment Act?",
                "ta": "SC/ST ஊழியர்களுக்குப் பதவி உயர்வு இடஒதுக்கீட்டில் 'தொடர் பணி மூப்பு' (Consequential Seniority) என்ற கருத்து எந்த அரசியலமைப்புத் திருத்தச் சட்டத்தின் மூலம் இணைக்கப்பட்டது?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "85th Constitutional Amendment Act, 2001",
                    "ta": "2001-ன் 85-வது அரசியலமைப்புத் திருத்தச் சட்டம்"
                },
                {
                    "id": "B",
                    "en": "77th Constitutional Amendment Act, 1995",
                    "ta": "1995-ன் 77-வது அரசியலமைப்புத் திருத்தச் சட்டம்"
                },
                {
                    "id": "C",
                    "en": "81st Constitutional Amendment Act, 2000",
                    "ta": "2000-ன் 81-வது அரசியலமைப்புத் திருத்தச் சட்டம்"
                },
                {
                    "id": "D",
                    "en": "82nd Constitutional Amendment Act, 2000",
                    "ta": "2000-ன் 82-வது அரசியலமைப்புத் திருத்தச் சட்டம்"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "77th Amendment (1995) introduced reservation in promotion (Art 16(4A)). 85th Amendment (2001) amended Art 16(4A) with retrospective effect from June 1995 to give 'consequential seniority' to SC/ST candidates promoted through reservation, overriding Catch-Up rule.",
                "ta": "77-வது திருத்தம் (1995) பதவி உயர்வு இடஒதுக்கீட்டைக் கொண்டுவந்தது. 85-வது திருத்தம் (2001) 16(4A)-ல் 'தொடர் பணி மூப்பு' (consequential seniority) என்பதை 1995 ஜூன் முதல் முன் தேதியிட்டு இணைத்தது."
            },
            "why_not_others": {
                "A": {"en": "Correct. 85th Amendment Act 2001 added consequential seniority into Art 16(4A).", "ta": "சரி. 85-வது திருத்தச் சட்டம் 2001 தொடர் பணி மூப்பை இணைத்தது."},
                "B": {"en": "Incorrect. 77th Amendment 1995 introduced reservation in promotion, but not consequential seniority.", "ta": "தவறு. 77-வது திருத்தம் 1995 பதவி உயர்வு இடஒதுக்கீட்டை மட்டும் தந்தது."},
                "C": {"en": "Incorrect. 81st Amendment 2000 dealt with carry-forward backlog vacancies.", "ta": "தவறு. 81-வது திருத்தம் விடுபட்ட பணியிடங்கள் பற்றியது."},
                "D": {"en": "Incorrect. 82nd Amendment 2000 dealt with relaxation of qualifying marks under Art 335.", "ta": "தவறு. 82-வது திருத்தம் தகுதி மதிப்பெண் தளர்வு பற்றியது."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: Union of India v. Virpal Singh Chauhan (1995) originally laid down the 'Catch-Up Rule' (general candidates catch up on seniority after promotion), which was negated by 85th Amendment.",
                "ta": "TNPSC குறிப்பு: விப்பால் சிங் சவுகான் வழக்கில் (1995) கூறப்பட்ட 'கேட்ச்-அப் விதியை' 85-வது திருத்தச் சட்டம் நீக்கியது."
            },
            "revision_fact": {
                "en": "M. Nagaraj (2006) upheld 85th Amendment but laid down 3 mandatory conditions: (1) Backwardness data, (2) Inadequacy of representation, (3) Maintenance of overall administrative efficiency (Art 335).",
                "ta": "எம். நாகராஜ் (2006) 85-வது திருத்தத்தை உறுதி செய்தது ஆனால் 3 நிபந்தனைகளை விதித்தது: பின்தங்கிய நிலை, போதிய பிரதிநிதித்துவமின்மை, நிர்வாகத் திறன் (பிரிவு 335)."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Analyze",
            "estimated_time_sec": 55,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 16(4A)", "85th Amendment", "Grand Test"]
        },

        # Q32: Direct MCQ - Fundamental Right against Forced Labour
        {
            "id": "FR_GT_032",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Easy",
            "question_type": "Direct MCQ",
            "question": {
                "en": "Under Article 23(2), the State is permitted to impose compulsory service for public purposes (like military service). On which ground is discrimination PROHIBITED when imposing such compulsory service?",
                "ta": "பிரிவு 23(2)-ன் கீழ், பொது நோக்கங்களுக்காகக் (ராணுவ சேவை போன்றவை) கட்டாயச் சேவையை விதிக்க அரசிற்கு அனுமதி உண்டு. இத்தகைய கட்டாயச் சேவையை விதிக்கும் போது எந்த அடிப்படையில் பாகுபாடு காட்டுவது தடை செய்யப்பட்டுள்ளது?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "Only on grounds of Religion, Race, Caste or Class",
                    "ta": "மதம், இனம், சாதி அல்லது வகுப்பு ஆகிய அடிப்படைகளில் மட்டுமே"
                },
                {
                    "id": "B",
                    "en": "Only on grounds of Sex, Domicile, and Language",
                    "ta": "பாலினம், இருப்பிடம் மற்றும் மொழி ஆகிய அடிப்படைகளில் மட்டுமே"
                },
                {
                    "id": "C",
                    "en": "On all 7 grounds listed under Article 16(2)",
                    "ta": "பிரிவு 16(2)-ன் கீழ் உள்ள 7 அடிப்படைகள் அனைத்திலும்"
                },
                {
                    "id": "D",
                    "en": "On grounds of age and physical fitness only",
                    "ta": "வயது மற்றும் உடற்தகுதி அடிப்படைகளில் மட்டுமே"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "Article 23(2) states that in imposing compulsory service for public purposes, the State shall NOT make any discrimination on grounds ONLY of religion, race, caste or class (or any of them). Note: 'Sex' is NOT listed in Art 23(2).",
                "ta": "பிரிவு 23(2) கூறுகிறது: பொது நோக்கங்களுக்காகக் கட்டாயச் சேவையை விதிக்கும் போது, மதம், இனம், சாதி அல்லது வகுப்பு ஆகிய அடிப்படைகளில் மட்டுமே அரசு பாகுபாடு காட்டக்கூடாது. குறிப்பு: 'பாலினம்' 23(2)-ல் குறிப்பிடப்படவில்லை."
            },
            "why_not_others": {
                "A": {"en": "Correct. Article 23(2) specifies 4 grounds: Religion, Race, Caste, Class.", "ta": "சரி. பிரிவு 23(2) 4 அடிப்படைகளைக் குறிப்பிடுகிறது: மதம், இனம், சாதி, வகுப்பு."},
                "B": {"en": "Incorrect. Sex is absent in Art 23(2).", "ta": "தவறு. பாலினம் 23(2)-ல் இல்லை."},
                "C": {"en": "Incorrect. It does not use Art 16(2) grounds.", "ta": "தவறு. பிரிவு 16(2) அடிப்படைகள் பயன்படுத்தப்படவில்லை."},
                "D": {"en": "Incorrect. Age and fitness are not constitutional non-discrimination grounds.", "ta": "தவறு. வயது மற்றும் உடற்தகுதி அரசியலமைப்பு அடிப்படையல்ல."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Trap: Notice that 'Sex' is omitted from Article 23(2). This means the State can compel military service exclusively for men without violating Article 23(2)!",
                "ta": "TNPSC பொறி: பிரிவு 23(2)-லிருந்து 'பாலினம்' விடுக்கப்பட்டுள்ளது. இதனால் ஆண்களுக்கு மட்டும் கட்டாய ராணுவச் சேவையை அரசு விதிக்க முடியும்!"
            },
            "revision_fact": {
                "en": "Bonded Labour System (Abolition) Act was enacted in 1976 to give effect to Article 23.",
                "ta": "பிரிவு 23-ஐ அமல்படுத்த 1976-ல் கொத்தடிமை முறை (ஒழிப்பு) சட்டம் இயற்றப்பட்டது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Remember",
            "estimated_time_sec": 40,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 23(2)", "Compulsory Service", "Grand Test"]
        },

        # Q33: Conceptual MCQ - Equality & Basic Structure
        {
            "id": "FR_GT_033",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Medium",
            "question_type": "Conceptual MCQ",
            "question": {
                "en": "In Indira Nehru Gandhi v. Raj Narain (1975), which aspect of Article 14 was declared by the Supreme Court to be a part of the Basic Structure of the Constitution?",
                "ta": "இந்திரா நேரு காந்தி எதிர் ராஜ் நரேன் (1975) வழக்கில், பிரிவு 14-ன் எந்த அம்சம் அரசியலமைப்பின் அடிப்படை அமைப்பின் ஒரு பகுதி என உச்ச நீதிமன்றத்தால் அறிவிக்கப்பட்டது?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "Rule of Law and Equality before Law",
                    "ta": "சட்டத்தின் ஆட்சி மற்றும் சட்டத்தின் முன் சமத்துவம்"
                },
                {
                    "id": "B",
                    "en": "Absolute prohibition of reservation in public posts",
                    "ta": "பொதுப் பணிகளில் இடஒதுக்கீட்டிற்கான முற்றுமுழுதான தடை"
                },
                {
                    "id": "C",
                    "en": "Right to property under Article 31",
                    "ta": "பிரிவு 31-ன் கீழ் உள்ள சொத்துரிமை"
                },
                {
                    "id": "D",
                    "en": "Exclusive legislative competence of Parliament over fundamental rights",
                    "ta": "அடிப்படை உரிமைகள் மீது நாடாளுமன்றத்தின் பிரத்யேக சட்ட அதிகாரம்"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "In Indira Nehru Gandhi v. Raj Narain (1975), the Supreme Court struck down 39th Amendment Act clause (4) (which removed election of PM from judicial review) holding that Rule of Law and Equality under Art 14 are basic features of the Constitution.",
                "ta": "இந்திரா காந்தி வழக்கில் (1975) 39-வது திருத்தச் சட்டப் பிரிவு (4) ரத்து செய்யப்பட்டது, ஏனெனில் சட்டத்தின் ஆட்சியும் சமத்துவமும் அரசியலமைப்பின் அடிப்படை அம்சங்களாகும்."
            },
            "why_not_others": {
                "A": {"en": "Correct. Rule of Law under Article 14 is part of Basic Structure.", "ta": "சரி. பிரிவு 14-ன் கீழ் உள்ள சட்டத்தின் ஆட்சி அடிப்படை அமைப்பின் பகுதியாகும்."},
                "B": {"en": "Incorrect. Reservation is permitted as affirmative action under 15 & 16.", "ta": "தவறு. இடஒதுக்கீடு அனுமதிக்கப்பட்ட ஒன்றாகும்."},
                "C": {"en": "Incorrect. Right to property was repealed as FR in 1978.", "ta": "தவறு. சொத்துரிமை 1978-ல் அடிப்படை உரிமையிலிருந்து நீக்கப்பட்டது."},
                "D": {"en": "Incorrect. Parliament does not have unlimited power over FRs.", "ta": "தவறு. நாடாளுமன்றத்திற்கு வரம்பற்ற அதிகாரம் இல்லை."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: In Minerva Mills case (1980), Supreme Court held that harmony and balance between Fundamental Rights (Part III) and Directive Principles (Part IV) is an essential feature of Basic Structure.",
                "ta": "TNPSC குறிப்பு: மினர்வா மில்ஸ் வழக்கில் (1980) அடிப்படை உரிமைகளுக்கும் வழிகாட்டு நெறிமுறைகளுக்கும் இடையிலான சமநிலை அடிப்படை அமைப்பின் அம்சம் எனப்பட்டது."
            },
            "revision_fact": {
                "en": "A.V. Dicey's Rule of Law has 3 elements: (1) Absence of arbitrary power, (2) Equality before law, (3) Primacy of rights of individual. India accepted first two.",
                "ta": "ஏ.வி. டைசியின் சட்டத்தின் ஆட்சி 3 கூறுகளைக் கொண்டது: (1) தன்னிச்சையான அதிகாரமின்மை, (2) சட்டத்தின் முன் சமம், (3) தனிநபர் உரிமைகளின் முதன்மை. இந்தியா முதல் இரண்டை ஏற்றது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Understand",
            "estimated_time_sec": 45,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 14", "Basic Structure", "Grand Test"]
        },

        # Q34: Statement-Based - Article 16 Reservation Rules
        {
            "id": "FR_GT_034",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Hard",
            "question_type": "Statement-Based",
            "question": {
                "en": "Which of the following statements regarding the 50% reservation ceiling is/are correct?\n1. The 50% reservation limit was first recommended as a general rule in M.R. Balaji v. State of Mysore (1963).\n2. The 50% cap was reaffirmed as a binding constitutional rule by a 9-judge bench in Indra Sawhney (1992).\n3. The Supreme Court in Janhit Abhiyan (2022) held that 10% EWS reservation under Article 16(6) does NOT violate the 50% limit as the 50% limit applies only to SEBC/SC/ST reservations.\nSelect the correct answer using the code given below:",
                "ta": "50% இடஒதுக்கீட்டு உச்சவரம்பு பற்றிய பின்வரும் கூற்றுகளில் எது/எவை சரியானவை?\n1. 50% இடஒதுக்கீட்டு வரம்பு முதன்முதலில் எம்.ஆர். பாலாஜி எதிர் மைசூர் மாநிலம் (1963) வழக்கில் பொது விதியாகப் பரிந்துரைக்கப்பட்டது.\n2. 50% வரம்பு இந்திரா சாஹ்னி (1992) வழக்கில் 9 நீதிபதிகள் கொண்ட அமர்வால் பிணைக்கப்படும் விதியாக மீண்டும் உறுதிப்படுத்தப்பட்டது.\n3. ஜன்ஹித் அபியான் (2022) வழக்கில் பிரிவு 16(6)-ன் கீழ் உள்ள 10% EWS இடஒதுக்கீடு 50% வரம்பை மீறவில்லை, ஏனெனில் 50% வரம்பு SEBC/SC/ST இடஒதுக்கீடுகளுக்கு மட்டுமே பொருந்தும் என உச்ச நீதிமன்றம் தீர்ப்பளித்தது.\nகீழே கொடுக்கப்பட்டுள்ள குறியீட்டைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:"
            },
            "options": [
                {
                    "id": "A",
                    "en": "1 and 2 only",
                    "ta": "1 மற்றும் 2 மட்டுமே"
                },
                {
                    "id": "B",
                    "en": "2 and 3 only",
                    "ta": "2 மற்றும் 3 மட்டுமே"
                },
                {
                    "id": "C",
                    "en": "1 and 3 only",
                    "ta": "1 மற்றும் 3 மட்டுமே"
                },
                {
                    "id": "D",
                    "en": "1, 2 and 3",
                    "ta": "1, 2 மற்றும் 3"
                }
            ],
            "correct_answer": "D",
            "explanation": {
                "en": "All three statements are correct. Balaji case (1963) first suggested reservation should be less than 50%. Indra Sawhney (1992) solidified it to 50%. Janhit Abhiyan (2022) held that 10% EWS reservation under 15(6)/16(6) is additional and does not breach the 50% cap meant for backward classes.",
                "ta": "மூன்று கூற்றுகளும் சரியானவை. பாலாஜி வழக்கு (1963) 50%-க்கு குறைவாக இருக்க வேண்டும் என்றது. இந்திரா சாஹ்னி (1992) 50%-ஐ உறுதியாக்கியது. ஜன்ஹித் அபியான் (2022) EWS 10% இடஒதுக்கீடு 50% வரம்பை மீறாது என்றது."
            },
            "why_not_others": {
                "A": {"en": "Incorrect because statement 3 is also correct.", "ta": "தவறு, ஏனெனில் கூற்று 3-ம் சரியானது."},
                "B": {"en": "Incorrect because statement 1 is also correct.", "ta": "தவறு, ஏனெனில் கூற்று 1-ம் சரியானது."},
                "C": {"en": "Incorrect because statement 2 is also correct.", "ta": "தவறு, ஏனெனில் கூற்று 2-ம் சரியானது."},
                "D": {"en": "Correct. All statements 1, 2 and 3 are factually accurate.", "ta": "சரி. கூற்றுகள் 1, 2 மற்றும் 3 அனைத்தும் சரியானவை."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: M.R. Balaji (1963) also held that classification based ONLY on caste is unconstitutional, and social backwardness cannot be determined exclusively by caste.",
                "ta": "TNPSC குறிப்பு: பாலாஜி வழக்கு (1963) சாதி அடிப்படையில் மட்டுமே வகைப்படுத்துவது அரசியலமைப்புக்கு முரணானது என்றும் கூறியது."
            },
            "revision_fact": {
                "en": "In Maratha Reservation case (Jaishri Laxmanrao Patil v. Chief Minister Maharashtra 2021), 5-judge SC bench struck down Maharashtra's SEBC reservation for exceeding 50% cap without extraordinary circumstances.",
                "ta": "மராத்தா இடஒதுக்கீட்டு வழக்கில் (2021) 50% வரம்பை மீறிய மகாராஷ்டிராவின் SEBC இடஒதுக்கீட்டை உச்ச நீதிமன்றம் ரத்து செய்தது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Analyze",
            "estimated_time_sec": 65,
            "pyq_similarity": "High",
            "tags": ["Polity", "Reservation Ceiling", "Mandal Case", "Grand Test"]
        },

        # Q35: Direct MCQ - Article 13(4) 24th Amendment
        {
            "id": "FR_GT_035",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Easy",
            "question_type": "Direct MCQ",
            "question": {
                "en": "Which Constitutional Amendment Act inserted Article 13(4) to state that nothing in Article 13 shall apply to any amendment of the Constitution made under Article 368?",
                "ta": "பிரிவு 368-ன் கீழ் செய்யப்படும் எந்தவொரு அரசியலமைப்புத் திருத்தத்திற்கும் பிரிவு 13-ல் உள்ள எதுவும் பொருந்தாது என்று கூற பிரிவு 13(4)-ஐ இணைத்த அரசியலமைப்புத் திருத்தச் சட்டம் எது?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "24th Constitutional Amendment Act, 1971",
                    "ta": "1971-ன் 24-வது அரசியலமைப்புத் திருத்தச் சட்டம்"
                },
                {
                    "id": "B",
                    "en": "42nd Constitutional Amendment Act, 1976",
                    "ta": "1976-ன் 42-வது அரசியலமைப்புத் திருத்தச் சட்டம்"
                },
                {
                    "id": "C",
                    "en": "44th Constitutional Amendment Act, 1978",
                    "ta": "1978-ன் 44-வது அரசியலமைப்புத் திருத்தச் சட்டம்"
                },
                {
                    "id": "D",
                    "en": "1st Constitutional Amendment Act, 1951",
                    "ta": "1951-ன் 1-வது அரசியலமைப்புத் திருத்தச் சட்டம்"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "The 24th Amendment Act 1971 inserted Article 13(4) and Article 368(3) to nullify the Golak Nath judgment (1967) and clarify that Parliament has power to amend any part of Part III via constitutional amendment under Article 368.",
                "ta": "24-வது திருத்தச் சட்டம் 1971 கோலக் நாத் தீர்ப்பை (1967) மாற்றி, பிரிவு 368-ன் கீழ் பகுதி III உட்பட அரசியலமைப்பின் எந்தப் பகுதியையும் திருத்த நாடாளுமன்றத்திற்கு அதிகாரம் உண்டு எனத் தெளிவுபடுத்த பிரிவு 13(4)-ஐ இணைத்தது."
            },
            "why_not_others": {
                "A": {"en": "Correct. 24th Amendment Act 1971 inserted Article 13(4).", "ta": "சரி. 24-வது திருத்தச் சட்டம் 1971 பிரிவு 13(4)-ஐ இணைத்தது."},
                "B": {"en": "Incorrect. 42nd Amendment added 368(4) and (5) which were later struck down in Minerva Mills.", "ta": "தவறு. 42-வது திருத்தம் 368(4), (5)-ஐ இணைத்தது, அவை பின்னர் ரத்து செய்யப்பட்டன."},
                "C": {"en": "Incorrect. 44th Amendment restored civil liberties after Emergency.", "ta": "தவறு. 44-வது திருத்தம் அவசரநிலைக்குப் பின் உரிமைகளை மீட்டது."},
                "D": {"en": "Incorrect. 1st Amendment added 31A, 31B, 15(4).", "ta": "தவறு. 1-வது திருத்தம் 31A, 31B, 15(4)-ஐ இணைத்தது."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: In Kesavananda Bharati (1973), the Supreme Court UPHELD the validity of 24th Amendment Act 1971, subject to the Basic Structure Doctrine.",
                "ta": "TNPSC குறிப்பு: கேசவாநந்த பாரதி வழக்கில் (1973) 24-வது திருத்தச் சட்டம் 1971 செல்லுபடியாகும் என உச்ச நீதிமன்றம் உறுதி செய்தது (அடிப்படை அமைப்பு கோட்பாட்டிற்கு உட்பட்டு)."
            },
            "revision_fact": {
                "en": "In I.C. Golak Nath v. State of Punjab (1967), an 11-judge SC bench held by 6:5 majority that Parliament cannot amend Fundamental Rights under Art 368.",
                "ta": "கோலக் நாத் வழக்கில் (1967) 11 நீதிபதிகள் அமர்வு 6:5 பெரும்பான்மையில் நாடாளுமன்றம் பிரிவு 368-ன் கீழ் அடிப்படை உரிமைகளைத் திருத்த முடியாது என்றது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Remember",
            "estimated_time_sec": 35,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 13(4)", "24th Amendment", "Grand Test"]
        }
    ]
    return questions
