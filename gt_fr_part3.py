# gt_fr_part3.py
# Questions 71 to 100: Articles 25 - 35, Article 300A, Writs, FR vs DPSP, Basic Structure & Integration

def get_part3_questions():
    questions = [
        # Q71: Direct MCQ - Article 25 Freedom of Religion grounds of restriction
        {
            "id": "FR_GT_071",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Easy",
            "question_type": "Direct MCQ",
            "question": {
                "en": "Under Article 25(1) of the Constitution of India, the freedom of conscience and the right freely to profess, practise and propagate religion is subject to which of the following?",
                "ta": "இந்திய அரசியலமைப்பின் 25(1) பிரிவின் கீழ், மனசாட்சி சுதந்திரம் மற்றும் மதத்தைப் பின்பற்றும், பரப்பும் உரிமை பின்வருவனவற்றுள் எவற்றிற்கு உட்பட்டது?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "Public order, morality, health, and other provisions of Part III",
                    "ta": "பொது ஒழுங்கு, ஒழுக்கம், சுகாதாரம் மற்றும் பகுதி III-ன் பிற விதிகள்"
                },
                {
                    "id": "B",
                    "en": "Sovereignty and integrity of India only",
                    "ta": "இந்தியாவின் இறையாண்மை மற்றும் ஒருமைப்பாடு மட்டுமே"
                },
                {
                    "id": "C",
                    "en": "Decency, defamation, and contempt of court only",
                    "ta": "கண்ணியம், அவதூறு மற்றும் நீதிமன்ற அவமதிப்பு மட்டுமே"
                },
                {
                    "id": "D",
                    "en": "Security of the State and friendly relations with foreign States only",
                    "ta": "அரசின் பாதுகாப்பு மற்றும் வெளிநாடுகளுடனான நட்புறவு மட்டுமே"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "Article 25(1) explicitly guarantees freedom of conscience and profession, practice, propagation of religion 'Subject to public order, morality and health and to the other provisions of this Part'.",
                "ta": "பிரிவு 25(1) மனசாட்சி சுதந்திரம் மற்றும் மதத்தைப் பரப்பும் உரிமையைப் 'பொது ஒழுங்கு, ஒழுக்கம் மற்றும் சுகாதாரம் மற்றும் பகுதி III-ன் பிற விதிகளுக்கு உட்பட்டு' உத்தரவாதம் அளிக்கிறது."
            },
            "why_not_others": {
                "A": {"en": "Correct. Public order, morality, health, and Part III provisions restrict Article 25.", "ta": "சரி. பொது ஒழுங்கு, ஒழுக்கம், சுகாதாரம் மற்றும் பகுதி III விதிகள் பிரிவு 25-ஐக் கட்டுப்படுத்துகின்றன."},
                "B": {"en": "Incorrect. Sovereignty is an Art 19 restriction ground, not specified in 25(1).", "ta": "தவறு. இறையாண்மை 19-ன் கீழ் வருகிறது."},
                "C": {"en": "Incorrect. Defamation and contempt belong to Art 19(2).", "ta": "தவறு. அவதூறு மற்றும் அவமதிப்பு 19(2)-ல் உள்ளன."},
                "D": {"en": "Incorrect. State security belongs to Art 19(2).", "ta": "தவறு. அரசின் பாதுகாப்பு 19(2)-ல் உள்ளது."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: In Rev Stainislaus v. State of MP (1977), Supreme Court held that 'propagation' under Article 25 DOES NOT include the right to forcibly convert another person to one's own religion.",
                "ta": "TNPSC குறிப்பு: ஸ்டேனிஸ்லாஸ் வழக்கில் (1977) பிரிவு 25-ன் கீழ் மதத்தைப் பரப்புவது என்பது ஒருவரைத் தனது மதத்திற்குப் பலவந்தமாக மாற்றுவதற்கான உரிமையை உள்ளடக்காது எனப்பட்டது."
            },
            "revision_fact": {
                "en": "Explanation II to Article 25 specifies that reference to 'Hindus' includes persons professing Sikh, Jaina or Buddhist religion.",
                "ta": "பிரிவு 25-ன் விளக்கம் II-ன் படி 'இந்துக்கள்' என்பதில் சீக்கியர்கள், ஜைனர்கள், பௌத்தர்கள் அடங்குவர்."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Remember",
            "estimated_time_sec": 35,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 25", "Freedom of Religion", "Grand Test"]
        },

        # Q72: Conceptual MCQ - Article 26 Freedom to Manage Religious Affairs
        {
            "id": "FR_GT_072",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Medium",
            "question_type": "Conceptual MCQ",
            "question": {
                "en": "Which of the following conditions must be satisfied for a group to qualify as a 'Religious Denomination' under Article 26 of the Constitution of India?",
                "ta": "இந்திய அரசியலமைப்பின் 26-வது பிரிவின் கீழ் ஒரு குழு 'மதப் பிரிவு' (Religious Denomination) எனக் கருதப்பட பின்வரும் எந்த நிபந்தனைகள் நிறைவு செய்யப்பட வேண்டும்?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "System of beliefs conducive to spiritual well-being, common organization, and a distinctive name",
                    "ta": "ஆன்மீக நலனுக்கு உகந்த நம்பிக்கை முறை, பொதுவான அமைப்பு மற்றும் தனித்துவமான பெயர்"
                },
                {
                    "id": "B",
                    "en": "Recognition by the Election Commission of India as a political party",
                    "ta": "இந்தியத் தேர்தல் ஆணையத்தால் அரசியல் கட்சியாக அங்கீகரிக்கப்பட்டிருத்தல்"
                },
                {
                    "id": "C",
                    "en": "Presence of adherents in at least 15 States of India",
                    "ta": "இந்தியாவின் குறைந்தபட்சம் 15 மாநிலங்களில் பின்பற்றுபவர்கள் இருத்தல்"
                },
                {
                    "id": "D",
                    "en": "Financial funding directly provided by the Union Government",
                    "ta": "மத்திய அரசால் நேரடியாக வழங்கப்பட்ட நிதி உதவி"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "In Commr, Hindu Religious Endowments Madras v. Sri Lakshmindra Thirtha Swamiar of Sri Shirur Mutt (1954) and SP Mittal (1983), SC laid down 3 conditions for a Religious Denomination: (1) System of beliefs (doctrines), (2) Common organization, (3) Distinctive name. Ramakrishna Mission and Anand Marga are denominations; Aurobindo Society is not.",
                "ta": "ஷிரூர் மடம் வழக்கு (1954) மற்றும் எஸ்.பி மிட்டல் வழக்கில் (1983) மதப் பிரிவிற்கான 3 நிபந்தனைகள்: (1) கோட்பாடுகள், (2) பொது அமைப்பு, (3) தனித்துவ பெயர். ராமகிருஷ்ணா மடம் மதப்பிரிவு; அரவிந்தோ சங்கம் மதப்பிரிவு அல்ல."
            },
            "why_not_others": {
                "A": {"en": "Correct. The 3 Shirur Mutt test criteria define a Religious Denomination.", "ta": "சரி. ஷிரூர் மட வழக்கின் 3 அளவுகோல்கள் மதப் பிரிவை வரையறுக்கின்றன."},
                "B": {"en": "Incorrect. Election Commission recognition is irrelevant.", "ta": "தவறு. தேர்தல் ஆணைய அங்கீகாரம் தொடர்பற்றது."},
                "C": {"en": "Incorrect. Geographical spread across 15 states is not required.", "ta": "தவறு. 15 மாநிலப் பரவல் தேவையில்லை."},
                "D": {"en": "Incorrect. Government funding is not required.", "ta": "தவறு. அரசு நிதி தேவையில்லை."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: Article 26 rights belong to a 'Religious Denomination' (collective right), whereas Article 25 guarantees rights to an 'Individual'.",
                "ta": "TNPSC குறிப்பு: பிரிவு 26 உரிமைகள் 'மதப் பிரிவிற்கு' (கூட்டு உரிமை) உரியது, பிரிவு 25 'தனிநபருக்கு' உரியது."
            },
            "revision_fact": {
                "en": "Article 26 is subject to Public Order, Morality, and Health, but NOT subject to other Fundamental Rights (unlike Article 25).",
                "ta": "பிரிவு 26 பொது ஒழுங்கு, ஒழுக்கம், சுகாதாரத்திற்கு உட்பட்டது, ஆனால் பிற அடிப்படை உரிமைகளுக்கு உட்பட்டது அல்ல."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Understand",
            "estimated_time_sec": 45,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 26", "Religious Denomination", "Shirur Mutt", "Grand Test"]
        },

        # Q73: Direct MCQ - Article 27 Freedom from Tax for Religion
        {
            "id": "FR_GT_073",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Easy",
            "question_type": "Direct MCQ",
            "question": {
                "en": "Article 27 of the Constitution prohibits the State from compelling any person to pay taxes for the promotion of any particular religion. What does Article 27 NOT prohibit?",
                "ta": "அரசியலமைப்பின் 27-வது பிரிவு எந்தவொரு குறிப்பிட்ட மதத்தையும் பரப்புவதற்காக வரிகளைச் செலுத்துமாறு மக்களைக் கட்டாயப்படுத்துவதைத் தடை செய்கிறது. பிரிவு 27 எதைத் தடை செய்யவில்லை?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "Levy of a FEE by the State to provide secular regulation or safety services to pilgrims",
                    "ta": "யாத்ரீகர்களுக்கு மதச்சார்பற்ற கட்டுப்பாடு அல்லது பாதுகாப்புச் சேவைகளை வழங்க அரசு கட்டணம் (FEE) விதிப்பது"
                },
                {
                    "id": "B",
                    "en": "Levy of a special religious TAX allocated exclusively to a majority religion",
                    "ta": "பெரும்பான்மை மதத்திற்கு மட்டும் பிரத்யேகமாக ஒதுக்கப்படும் சிறப்பு மத வரியை (TAX) விதிப்பது"
                },
                {
                    "id": "C",
                    "en": "Compulsory collection of tithes for building state temples",
                    "ta": "அரசு கோயில்களைக் கட்டக் கட்டாயமாக மத வரி வசூலிப்பது"
                },
                {
                    "id": "D",
                    "en": "Utilizing state revenues exclusively for the maintenance of one particular sect",
                    "ta": "ஒரு குறிப்பிட்ட பிரிவின் பராமரிப்பிற்காக மட்டும் அரசு வருவாயைப் பயன்படுத்துவது"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "Article 27 prohibits the levy of a TAX where proceeds are specifically appropriated for promoting a religion. However, it does NOT prohibit the levy of a FEE for secular services, safety, or regulation of religious institutions (Shirur Mutt case).",
                "ta": "பிரிவு 27 மதத்தைப் பரப்ப வரி (TAX) விதிப்பதை மட்டுமே தடை செய்கிறது. ஆனால் பாதுகாப்பு அல்லது மதச்சார்பற்ற சேவைகளுக்குக் கட்டணம் (FEE) விதிப்பதைத் தடை செய்யவில்லை."
            },
            "why_not_others": {
                "A": {"en": "Correct. Levy of a fee for secular services is NOT prohibited under Art 27.", "ta": "சரி. மதச்சார்பற்ற சேவைகளுக்கான கட்டணம் பிரிவு 27-ன் கீழ் தடை செய்யப்படவில்லை."},
                "B": {"en": "Incorrect. Special religious tax is explicitly prohibited.", "ta": "தவறு. மத வரி வெளிப்படையாகத் தடை செய்யப்பட்டுள்ளது."},
                "C": {"en": "Incorrect. Compulsory tax for temples is prohibited.", "ta": "தவறு. கோயில் கட்டாய வரி தடை செய்யப்பட்டுள்ளது."},
                "D": {"en": "Incorrect. State revenues cannot be used exclusively for one sect.", "ta": "தவறு. ஒரு பிரிவிற்கு மட்டும் அரசு வருவாய் பயன்படுத்தப்பட முடியாது."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: Distinction between Tax and Fee: Tax is a compulsory contribution for general public revenue without specific quid pro quo. Fee is a payment for a specific service rendered (quid pro quo).",
                "ta": "TNPSC குறிப்பு: வரிக்கும் கட்டணத்திற்கும் உள்ள வேறுபாடு: வரி என்பது பொது வருவாய்க்கான கட்டாயப் பங்களிப்பு (பதிலுதவி இல்லை). கட்டணம் என்பது குறிப்பிட்ட சேவைக்கான தொகை (பதிலுதவி உண்டு)."
            },
            "revision_fact": {
                "en": "State can spend public money for the promotion or maintenance of ALL religions equally, but not for ONE religion exclusively.",
                "ta": "அனைத்து மதங்களையும் சீராக உயர்த்த அரசு நிதி செலவிடலாம், ஒரு மதத்திற்கு மட்டும் செலவிடக் கூடாது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Remember",
            "estimated_time_sec": 35,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 27", "Tax vs Fee", "Grand Test"]
        },

        # Q74: Conceptual MCQ - Article 28 Four Categories of Educational Institutions
        {
            "id": "FR_GT_074",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Hard",
            "question_type": "Conceptual MCQ",
            "question": {
                "en": "Under Article 28 of the Constitution regarding religious instruction in educational institutions, in which category of institution is religious instruction COMPLETELY PROHIBITED?",
                "ta": "கல்வி நிறுவனங்களில் மத போதனை தொடர்பான அரசியலமைப்பின் 28-வது பிரிவின் கீழ், எந்த வகை நிறுவனத்தில் மத போதனை முற்றிலும் தடை செய்யப்பட்டுள்ளது?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "Institutions wholly maintained out of State funds",
                    "ta": "முழுமையாக அரசு நிதியிலிருந்து பராமரிக்கப்படும் நிறுவனங்கள்"
                },
                {
                    "id": "B",
                    "en": "Institutions administered by the State but established under a trust or endowment requiring religious instruction",
                    "ta": "அரசால் நிர்வகிக்கப்படும் ஆனால் மத போதனையைக் கோரும் அறக்கட்டளையின் கீழ் அமைக்கப்பட்ட நிறுவனங்கள்"
                },
                {
                    "id": "C",
                    "en": "Institutions recognized by the State",
                    "ta": "அரசால் அங்கீகரிக்கப்பட்ட நிறுவனங்கள்"
                },
                {
                    "id": "D",
                    "en": "Institutions receiving aid out of State funds",
                    "ta": "அரசு நிதியிலிருந்து மானியம்/உதவி பெறும் நிறுவனங்கள்"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "Article 28 divides institutions into 4 categories: (1) Wholly maintained by State -> Religious instruction TOTALLY PROHIBITED. (2) Administered by State but established under trust -> PERMITTED. (3) Recognized by State -> PERMITTED ON VOLUNTARY BASIS. (4) Receiving aid from State -> PERMITTED ON VOLUNTARY BASIS.",
                "ta": "பிரிவு 28 4 வகைகளாகப் பிரிக்கிறது: (1) முழுமையான அரசு நிதி -> மத போதனை முற்றிலும் தடை. (2) அரசால் நிர்வகிக்கப்படும் அறக்கட்டளை -> அனுமதி உண்டு. (3) அரசால் அங்கீகரிக்கப்பட்டது -> தன்னார்வ அடிப்படையில் அனுமதி. (4) அரசு உதவி பெறுவது -> தன்னார்வ அடிப்படையில் அனுமதி."
            },
            "why_not_others": {
                "A": {"en": "Correct. Wholly state-funded institutions face absolute prohibition of religious instruction.", "ta": "சரி. முழுமையான அரசு உதவி நிறுவனங்களில் மத போதனை முற்றிலும் தடை செய்யப்பட்டுள்ளது."},
                "B": {"en": "Incorrect. Trust-established state-administered institutions permit religious instruction.", "ta": "தவறு. அறக்கட்டளை நிறுவனங்களில் அனுமதி உண்டு."},
                "C": {"en": "Incorrect. State recognized institutions permit voluntary attendance.", "ta": "தவறு. அங்கீகரிக்கப்பட்ட நிறுவனங்களில் தன்னார்வ அனுமதி உண்டு."},
                "D": {"en": "Incorrect. State aided institutions permit voluntary attendance.", "ta": "தவறு. உதவிபெறும் நிறுவனங்களில் தன்னார்வ அனுமதி உண்டு."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: For recognized or aided institutions (Categories 3 & 4), no person can be compelled to attend religious instruction without their consent (or parent's consent if a minor).",
                "ta": "TNPSC குறிப்பு: அங்கீகரிக்கப்பட்ட/உதவிபெறும் நிறுவனங்களில் சம்மதமின்றி (மைனர் என்றால் பெற்றோர் சம்மதம்) மத போதனையில் கலந்துகொள்ளக் கட்டாயப்படுத்த முடியாது."
            },
            "revision_fact": {
                "en": "Article 28(1) states: 'No religious instruction shall be provided in any educational institution wholly maintained out of State funds'.",
                "ta": "பிரிவு 28(1): 'முழுமையாக அரசு நிதியிலிருந்து பராமரிக்கப்படும் எந்தவொரு கல்வி நிறுவனத்திலும் மத போதனை வழங்கப்படக்கூடாது'."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Analyze",
            "estimated_time_sec": 50,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 28", "Religious Instruction", "Grand Test"]
        },

        # Q75: Statement-Based - Articles 29 & 30 Minority Rights
        {
            "id": "FR_GT_075",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Hard",
            "question_type": "Statement-Based",
            "question": {
                "en": "Consider the following statements regarding Cultural and Educational Rights under Articles 29 and 30:\n1. Article 29 protects the rights of both religious and linguistic minorities, as well as any section of citizens residing in India having a distinct language, script or culture.\n2. Article 30 guarantees rights EXCLUSIVELY to religious and linguistic minorities to establish and administer educational institutions.\n3. In TMA Pai Foundation v. State of Karnataka (2002), the Supreme Court ruled that the unit for determining religious or linguistic minority status is the State, NOT the entire nation.\nWhich of the statements given above are correct?",
                "ta": "பிரிவுகள் 29 மற்றும் 30-ன் கீழ் உள்ள பண்பாட்டு மற்றும் கல்வி உரிமைகள் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. பிரிவு 29 மத மற்றும் மொழிச் சிறுபான்மையினரின் உரிமைகளையும், தனித்துவமான மொழி, எழுத்து அல்லது பண்பாட்டைக் கொண்ட குடிமக்களின் பிரிவினரின் உரிமைகளையும் பாதுகாக்கிறது.\n2. பிரிவு 30 கல்வி நிறுவனங்களை நிறுவவும் நிர்வகிக்கவும் மத மற்றும் மொழிச் சிறுபான்மையினருக்கு மட்டுமே பிரத்யேகமாக உரிமைகளை உத்தரவாதம் செய்கிறது.\n3. TMA பை அறக்கட்டளை வழக்கில் (2002), மத அல்லது மொழிச் சிறுபான்மையினர் அந்தஸ்தைத் தீர்மானிப்பதற்கான அலகு மாநிலமே தவிர, ஒட்டுமொத்த நாடும் அல்ல என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?"
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
                "en": "All three statements are correct. Art 29 scope covers any section of citizens (broader). Art 30 is restricted to religious & linguistic minorities only. TMA Pai Foundation (2002) 11-judge bench held minority status must be determined State-wise since reorganization of states was on linguistic basis.",
                "ta": "மூன்று கூற்றுகளும் சரியானவை. பிரிவு 29 அனைத்துக் குடிமக்கள் பிரிவிற்கும் பொருந்தும். பிரிவு 30 மத/மொழிச் சிறுபான்மையினருக்கு மட்டுமே. TMA பை வழக்கின்படி (2002) சிறுபான்மையினர் அந்தஸ்து மாநில அளவிலேயே தீர்மானிக்கப்படும்."
            },
            "why_not_others": {
                "A": {"en": "Incorrect because statement 3 is also correct.", "ta": "தவறு, ஏனெனில் கூற்று 3-ம் சரியானது."},
                "B": {"en": "Incorrect because statement 1 is also correct.", "ta": "தவறு, ஏனெனில் கூற்று 1-ம் சரியானது."},
                "C": {"en": "Incorrect because statement 2 is also correct.", "ta": "தவறு, ஏனெனில் கூற்று 2-ம் சரியானது."},
                "D": {"en": "Correct. Statements 1, 2 and 3 are all factually true.", "ta": "சரி. கூற்றுகள் 1, 2 மற்றும் 3 அனைத்தும் சரியானவை."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Trap: Crucial Difference: Article 29 applies to 'any section of citizens' (majority or minority). Article 30 applies ONLY to 'minorities' (religious or linguistic). Neither article defines 'minority'!",
                "ta": "TNPSC பொறி: முக்கிய வேறுபாடு: பிரிவு 29 'எந்தவொரு குடிமக்கள் பிரிவிற்கும்' பொருந்தும். பிரிவு 30 'சிறுபான்மையினருக்கு' மட்டுமே பொருந்தும். இரண்டும் 'சிறுபான்மையினர்' என்ற சொல்லை வரையறுக்கவில்லை!"
            },
            "revision_fact": {
                "en": "44th Constitutional Amendment Act 1978 inserted Article 30(1A) ensuring that full compensation is paid when minority institution property is compulsorily acquired.",
                "ta": "44-வது திருத்தச் சட்டம் 1978 பிரிவு 30(1A)-ஐ இணைத்து சிறுபான்மை நிறுவனச் சொத்து கையகப்படுத்தப்பட்டால் முழு இழப்பீடு வழங்குவதை உறுதிசெய்தது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Analyze",
            "estimated_time_sec": 60,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 29", "Article 30", "Minority Rights", "TMA Pai", "Grand Test"]
        },

        # Q76: Direct MCQ - Right to Property 44th Amendment Act 1978
        {
            "id": "FR_GT_076",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Easy",
            "question_type": "Direct MCQ",
            "question": {
                "en": "Which Constitutional Amendment Act abolished the Right to Property as a Fundamental Right under Articles 19(1)(f) and 31, and re-enacted it as a legal/constitutional right under Article 300A in Part XII?",
                "ta": "பிரிவுகள் 19(1)(f) மற்றும் 31-ன் கீழ் உள்ள சொத்துரிமையை அடிப்படை உரிமையிலிருந்து நீக்கி, பகுதி XII-ல் பிரிவு 300A-ன் கீழ் அதை ஒரு சட்டப்பூர்வ/அரசியலமைப்பு உரிமையாக மீண்டும் இயற்றிய அரசியலமைப்புத் திருத்தச் சட்டம் எது?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "44th Constitutional Amendment Act, 1978",
                    "ta": "1978-ன் 44-வது அரசியலமைப்புத் திருத்தச் சட்டம்"
                },
                {
                    "id": "B",
                    "en": "42nd Constitutional Amendment Act, 1976",
                    "ta": "1976-ன் 42-வது அரசியலமைப்புத் திருத்தச் சட்டம்"
                },
                {
                    "id": "C",
                    "en": "25th Constitutional Amendment Act, 1971",
                    "ta": "1971-ன் 25-வது அரசியலமைப்புத் திருத்தச் சட்டம்"
                },
                {
                    "id": "D",
                    "en": "1st Constitutional Amendment Act, 1951",
                    "ta": "1951-ன் 1-வது அரசியலமைப்புத் திருத்தச் சட்டம்"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "The 44th Amendment Act 1978 passed by Janata Party Government under Morarji Desai repealed Article 19(1)(f) and Article 31 from Part III and inserted Article 300A in Part XII stating: 'No person shall be deprived of his property save by authority of law'.",
                "ta": "1978-ன் 44-வது திருத்தச் சட்டம் மொரார்ஜி தேசாய் ஆட்சியில் 19(1)(f) மற்றும் 31-ஐ பகுதி III-லிருந்து நீக்கி பகுதி XII-ல் பிரிவு 300A-ஐ இணைத்தது."
            },
            "why_not_others": {
                "A": {"en": "Correct. 44th Amendment Act 1978 deleted Right to Property from Part III.", "ta": "சரி. 44-வது திருத்தச் சட்டம் 1978 சொத்துரிமையை பகுதி III-லிருந்து நீக்கியது."},
                "B": {"en": "Incorrect. 42nd Amendment did not delete right to property.", "ta": "தவறு. 42-வது திருத்தம் சொத்துரிமையை நீக்கவில்லை."},
                "C": {"en": "Incorrect. 25th Amendment substituted 'amount' for 'compensation' in Art 31.", "ta": "தவறு. 25-வது திருத்தம் இழப்பீடு என்ற சொல்லை மாற்றியது."},
                "D": {"en": "Incorrect. 1st Amendment added 31A and 31B, but did not abolish the FR.", "ta": "தவறு. 1-வது திருத்தம் 31A, 31B-ஐ இணைத்தது."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: Implications of Property becoming a Legal Right under Art 300A: (1) Can be regulated/curtailed by ordinary law without constitutional amendment, (2) No direct writ petition to Supreme Court under Article 32 (must go to High Court under Article 226).",
                "ta": "TNPSC குறிப்பு: 300A சட்ட உரிமையானதன் விளைவு: (1) சாதாரண சட்டம் மூலம் மாற்றலாம், (2) பிரிவு 32-ன் கீழ் நேரடியாக உச்ச நீதிமன்றம் செல்ல முடியாது (226-ன் கீழ் உயர் நீதிமன்றம் செல்லலாம்)."
            },
            "revision_fact": {
                "en": "Two exceptions where compensation is still constitutionally guaranteed for property acquisition: (1) Acquisition of land held by a person under personal cultivation within ceiling limit (Art 31A proviso), (2) Property of minority educational institution (Art 30(1A)).",
                "ta": "இழப்பீடு இன்னும் கட்டாயமாக உள்ள 2 சந்தர்ப்பங்கள்: (1) உச்சவரம்பிற்குட்பட்ட சொந்தச் சாகுபடி நிலம் (31A), (2) சிறுபான்மை நிறுவனச் சொத்து (30(1A))."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Remember",
            "estimated_time_sec": 35,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 300A", "Right to Property", "44th Amendment", "Grand Test"]
        },

        # Q77: Conceptual MCQ - Article 32 Heart and Soul
        {
            "id": "FR_GT_077",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Medium",
            "question_type": "Conceptual MCQ",
            "question": {
                "en": "Why did Dr. B.R. Ambedkar describe Article 32 (Right to Constitutional Remedies) as 'the very soul of the Constitution and the very heart of it'?",
                "ta": "டாக்டர் பி.ஆர். அம்பேத்கர் பிரிவு 32-ஐ (அரசியலமைப்புச் பரிகார உரிமை) 'அரசியலமைப்பின் ஆன்மா மற்றும் அதன் இதயம்' என்று ஏன் வர்ணித்தார்?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "Because a fundamental right without an effective remedy for its enforcement is meaningless, and Article 32 is itself a Fundamental Right",
                    "ta": "ஏனெனில் அமல்படுத்துவதற்கான பயனுள்ள பரிகாரம் இல்லாத அடிப்படை உரிமை அர்த்தமற்றது, மேலும் பிரிவு 32 নিজেই ஒரு அடிப்படை உரிமையாகும்"
                },
                {
                    "id": "B",
                    "en": "Because Article 32 gives the President power to override decisions of Parliament",
                    "ta": "ஏனெனில் பிரிவு 32 குடியரசுத் தலைவருக்கு நாடாளுமன்ற முடிவுகளை மாற்றும் அதிகாரத்தை அளிக்கிறது"
                },
                {
                    "id": "C",
                    "en": "Because Article 32 applies only during National Emergency to suspend state laws",
                    "ta": "ஏனெனில் பிரிவு 32 மாநிலச் சட்டங்களை ரத்து செய்ய அவசரநிலையின் போது மட்டுமே பொருந்தும்"
                },
                {
                    "id": "D",
                    "en": "Because Article 32 cannot be amended even by a unanimous Parliament",
                    "ta": "ஏனெனில் ஒருமனதான நாடாளுமன்றத்தாலும் பிரிவு 32-ஐத் திருத்த முடியாது"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "Dr. Ambedkar stated: 'If I was asked to name any particular article in this Constitution as the most important—an article without which this Constitution would be a nullity—I could not refer to any other article except this one. It is the very soul of the Constitution and the very heart of it'. Article 32 makes rights real.",
                "ta": "அம்பேத்கர் கூறினார்: 'அரசியலமைப்பின் மிக முக்கியமான பிரிவைக் குறிப்பிடச் சொன்னால், அது இல்லாமல் அரசியலமைப்புச் செல்லாததாகும் என்றால், நான் இந்த ஒரு பிரிவையே குறிப்பிடுவேன். இது ஆன்மாவும் இதயமும் ஆகும்'."
            },
            "why_not_others": {
                "A": {"en": "Correct. Art 32 guarantees effective enforcement of FRs and is itself an FR under Part III.", "ta": "சரி. பிரிவு 32 அடிப்படை உரிமைகளின் அமலாக்கத்தை உறுதி செய்கிறது, அதுவே ஒரு அடிப்படை உரிமை."},
                "B": {"en": "Incorrect. Art 32 is judicial remedy, not presidential override.", "ta": "தவறு. பிரிவு 32 நீதித்துறைப் பரிகாரம்."},
                "C": {"en": "Incorrect. Art 32 operates at all times.", "ta": "தவறு. பிரிவு 32 எப்போதும் செயல்படும்."},
                "D": {"en": "Incorrect. Art 32 can be amended subject to Basic Structure.", "ta": "தவறு. பிரிவு 32 அடிப்படை அமைப்பிற்கு உட்பட்டு திருத்தப்படலாம்."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: Supreme Court CANNOT refuse to entertain an Article 32 petition because Art 32 is a guaranteed Fundamental Right. High Court under Art 226 has discretionary jurisdiction and can refuse if alternate remedy exists.",
                "ta": "TNPSC குறிப்பு: பிரிவு 32 மனுவை விசாரிக்க உச்ச நீதிமன்றம் மறுக்க முடியாது (ஏனெனில் அது அடிப்படை உரிமை). பிரிவு 226-ன் கீழ் உயர் நீதிமன்றத்திற்கு விருப்ப அதிகாரம் உண்டு."
            },
            "revision_fact": {
                "en": "Fertilizer Corporation Kamgar Union v. UOI (1981) confirmed that Article 32 is an integral part of Basic Structure of the Constitution.",
                "ta": "ஃபெர்ட்டிலைசர் கார்ப்பரேஷன் வழக்கில் (1981) பிரிவு 32 அடிப்படை அமைப்பின் ஒருங்கிணைந்த பகுதி என உறுதி செய்யப்பட்டது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Understand",
            "estimated_time_sec": 45,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 32", "Ambedkar", "Heart and Soul", "Grand Test"]
        },

        # Q78: Match the Following - Five Writs & Meanings
        {
            "id": "FR_GT_078",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Medium",
            "question_type": "Match the Following",
            "question": {
                "en": "Match List-I (Writ) with List-II (Literal Meaning / Purpose):\nList-I:\na. Habeas Corpus\nb. Mandamus\nc. Prohibition\nd. Quo-Warranto\n\nList-II:\n1. 'We Command' - To perform a mandatory public duty\n2. 'By what authority or warrant' - To prevent illegal usurpation of public office\n3. 'To have the body of' - To release a person illegally detained\n4. 'To forbid' - Issued by higher court to lower court to prevent exceeding jurisdiction",
                "ta": "பட்டியல்-I-ஐ (நீதிப் பேராணை) பட்டியல்-II-உடன் (நேரடிப் பொருள் / நோக்கம்) பொருத்துக:\nபட்டியல்-I:\na. ஆட்கொணர் நீதிப் பேராணை (Habeas Corpus)\nb. கட்டளையிடும் நீதிப் பேராணை (Mandamus)\nc. தடுத்துநிறுத்தும் நீதிப் பேராணை (Prohibition)\nd. தகுதி வினவும் நீதிப் பேராணை (Quo-Warranto)\n\nபட்டியல்-II:\n1. 'நாம் கட்டளையிடுகிறோம்' - பொதுக் கடமையைச் செய்யப் பணித்தல்\n2. 'எந்த அதிகாரத்தின் கீழ்' - பொதுப் பதவியைச் சட்டவிரோதமாக ஆக்கிரமிப்பதைத் தடுத்தல்\n3. 'நபரை ஆஜர்படுத்துங்கள்' - சட்டவிரோதமாகக் கைதானவரை விடுவித்தல்\n4. 'தடை செய்தல்' - கீழ் நீதிமன்றம் அதிகார வரம்பை மீறுவதைத் தடுக்க உயர் நீதிமன்றம் பிறப்பிப்பது"
            },
            "options": [
                {
                    "id": "A",
                    "en": "a-3, b-1, c-4, d-2",
                    "ta": "a-3, b-1, c-4, d-2"
                },
                {
                    "id": "B",
                    "en": "a-1, b-3, c-2, d-4",
                    "ta": "a-1, b-3, c-2, d-4"
                },
                {
                    "id": "C",
                    "en": "a-3, b-4, c-1, d-2",
                    "ta": "a-3, b-4, c-1, d-2"
                },
                {
                    "id": "D",
                    "en": "a-2, b-1, c-4, d-3",
                    "ta": "a-2, b-1, c-4, d-3"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "Correct match: Habeas Corpus -> 'To have the body of' (3); Mandamus -> 'We Command' (1); Prohibition -> 'To forbid' (4); Quo-Warranto -> 'By what authority' (2).",
                "ta": "சரியான பொருத்தம்: ஆட்கொணர் பேராணை -> 'ஆஜர்படுத்துங்கள்' (3); கட்டளையிடும் பேராணை -> 'நாம் கட்டளையிடுகிறோம்' (1); தடுத்துநிறுத்தும் பேராணை -> 'தடை செய்தல்' (4); தகுதி வினவும் பேராணை -> 'எந்த அதிகாரத்தின் கீழ்' (2)."
            },
            "why_not_others": {
                "A": {"en": "Correct match: a-3, b-1, c-4, d-2.", "ta": "சரியான பொருத்தம்: a-3, b-4, c-1, d-2."},
                "B": {"en": "Incorrect mapping.", "ta": "தவறான பொருத்தம்."},
                "C": {"en": "Incorrect mapping.", "ta": "தவறான பொருத்தம்."},
                "D": {"en": "Incorrect mapping.", "ta": "தவறான பொருத்தம்."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: Fifth writ Certiorari means 'To be certified' or 'To be informed'. It is both preventive AND curative, quashing existing illegal orders.",
                "ta": "TNPSC குறிப்பு: 5-வது பேராணையான சான்றளிப்பு பேராணை (Certiorari) என்பது 'சான்றளிக்கப்படுவது' எனக் குறிக்கும். இது த தடுக்கும் மற்றும் குணப்படுத்தும் இரு தன்மைகளையும் கொண்டது."
            },
            "revision_fact": {
                "en": "Quo-Warranto can be sought by ANY interested person, unlike other writs where Locus Standi (personal injury) is required.",
                "ta": "தகுதி வினவும் பேராணையைப் பாதிக்கப்பட்டவர் மட்டுமின்றி எந்தவொரு ஆர்வமுள்ள நபரும் கோர முடியும் (Locus Standi தளர்வு)."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Analyze",
            "estimated_time_sec": 60,
            "pyq_similarity": "High",
            "tags": ["Polity", "Writs", "Article 32", "Match the Following", "Grand Test"]
        },

        # Q79: Conceptual MCQ - Comparison of SC Art 32 vs HC Art 226 Writs
        {
            "id": "FR_GT_079",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Hard",
            "question_type": "Conceptual MCQ",
            "question": {
                "en": "Which of the following statements correctly compares the Writ Jurisdiction of the Supreme Court under Article 32 with that of High Courts under Article 226?",
                "ta": "பிரிவு 32-ன் கீழ் உள்ள உச்ச நீதிமன்றத்தின் பேராணை அதிகாரத்தையும் பிரிவு 226-ன் கீழ் உள்ள உயர் நீதிமன்றத்தின் பேராணை அதிகாரத்தையும் பின்வரும் கூற்றுகளில் எது சரியாக ஒப்பிடுகிறது?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "High Court writ jurisdiction under Article 226 is WIDER than Supreme Court under Article 32 because High Courts can issue writs for both Fundamental Rights and ordinary legal rights",
                    "ta": "பிரிவு 226-ன் கீழ் உயர் நீதிமன்றத்தின் பேராணை அதிகாரம் பிரிவு 32-ன் கீழ் உச்ச நீதிமன்றத்தை விடப் பரந்தது, ஏனெனில் உயர் நீதிமன்றங்கள் அடிப்படை உரிமைகள் மற்றும் சாதாரண சட்ட உரிமைகள் இரண்டிற்கும் பேராணைகளை வெளியிட முடியும்"
                },
                {
                    "id": "B",
                    "en": "Supreme Court writ jurisdiction under Article 32 is wider in territorial reach and subject matter than High Courts",
                    "ta": "பிரிவு 32-ன் கீழ் உச்ச நீதிமன்றத்தின் பேராணை அதிகாரம் புவியியல் மற்றும் பொருள் எல்லை இரண்டிலும் உயர் நீதிமன்றங்களை விடப் பரந்தது"
                },
                {
                    "id": "C",
                    "en": "High Courts cannot issue writs against the Union Government under Article 226",
                    "ta": "பிரிவு 226-ன் கீழ் உயர் நீதிமன்றங்கள் மத்திய அரசுக்கு எதிராகப் பேராணைகளை வெளியிட முடியாது"
                },
                {
                    "id": "D",
                    "en": "Supreme Court under Article 32 can issue writs for enforcement of Directive Principles of State Policy",
                    "ta": "பிரிவு 32-ன் கீழ் உச்ச நீதிமன்றம் அரசு வழிகாட்டு நெறிமுறைகளை அமல்படுத்தப் பேராணைகளை வெளியிட முடியும்"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "High Court's writ jurisdiction under Art 226 is wider in SCOPE (FRs + ordinary legal rights) than SC under Art 32 (ONLY FRs). However, SC's writ jurisdiction is wider in TERRAIN (entire India vs state territory).",
                "ta": "பொருள் எல்லையில் (SCOPE) 226-ன் கீழ் உயர் நீதிமன்ற அதிகாரம் பரந்தது (அடிப்படை உரிமை + சட்ட உரிமை). ஆனால் புவியியல் எல்லையில் உச்ச நீதிமன்றம் பரந்தது (இந்தியா முழுவதும்)."
            },
            "why_not_others": {
                "A": {"en": "Correct. Art 226 covers FRs and ordinary legal rights, making its subject scope wider than Art 32.", "ta": "சரி. பிரிவு 226 அடிப்படை உரிமைகள் மற்றும் சாதாரண சட்ட உரிமைகளை உள்ளடக்குவதால் பரந்தது."},
                "B": {"en": "Incorrect. SC is wider in territorial reach, but NOT in subject matter scope.", "ta": "தவறு. உச்ச நீதிமன்றம் புவியியல் எல்லையில் மட்டுமே பரந்தது."},
                "C": {"en": "Incorrect. High Courts CAN issue writs against Union Govt under 226(2) if cause of action arises in state.", "ta": "தவறு. வழக்குக் காரணம் மாநிலத்தில் எழுந்தால் உயர் நீதிமன்றம் மத்திய அரசுக்கு எதிராகப் பேராணை பிறப்பிக்கலாம்."},
                "D": {"en": "Incorrect. DPSPs are non-justiciable and cannot be enforced by writs.", "ta": "தவறு. DPSP-களைப் பேராணை மூலம் அமல்படுத்த முடியாது."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: Article 32 is itself a Fundamental Right (guaranteed remedy). Article 226 is a constitutional right (discretionary remedy). High Court can refuse 226 petition if alternate remedy exists.",
                "ta": "TNPSC குறிப்பு: பிரிவு 32 தானே ஒரு அடிப்படை உரிமை (உத்தரவாதமளிக்கப்பட்ட பரிகாரம்). பிரிவு 226 ஒரு அரசியலமைப்பு உரிமை (விருப்பப் பரிகாரம்)."
            },
            "revision_fact": {
                "en": "In Chandra Kumar v. UOI (1997), Supreme Court held that writ jurisdiction under Articles 32 and 226 is part of the Basic Structure of the Constitution.",
                "ta": "சந்திரகுமார் வழக்கில் (1997) பிரிவு 32 மற்றும் 226 பேராணை அதிகாரம் அடிப்படை அமைப்பின் பகுதி எனப்பட்டது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Analyze",
            "estimated_time_sec": 55,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 32", "Article 226", "Writ Jurisdiction Comparison", "Grand Test"]
        },

        # Q80: Statement-Based - Specific Writ Applicability (Mandamus vs Quo-Warranto)
        {
            "id": "FR_GT_080",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Hard",
            "question_type": "Statement-Based",
            "question": {
                "en": "Consider the following statements regarding the availability of Writs in India:\n1. Mandamus CANNOT be issued against a private individual, a departmental instruction lacking statutory force, or the President/State Governors.\n2. Prohibition and Certiorari can be issued ONLY against judicial and quasi-judicial bodies, as well as administrative authorities affecting rights of individuals.\n3. Quo-Warranto can be issued to prevent illegal usurpation of a public office created by the Constitution or a Statute.\nWhich of the statements given above are correct?",
                "ta": "இந்தியாவில் பேராணைகள் கிடைப்பது பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. தனியார் தனிநபர், சட்டப்பூர்வ ஆதரவற்ற துறை வழிகாட்டுதல் அல்லது குடியரசுத் தலைவர்/ஆளுநர்களுக்கு எதிராகக் கட்டளையிடும் பேராணையை (Mandamus) வெளியிட முடியாது.\n2. தடுத்துநிறுத்தும் (Prohibition) மற்றும் சான்றளிப்பு (Certiorari) பேராணைகள் நீதித்துறை, நீதித்துறை போன்ற அமைப்புகள் மற்றும் நபர்களின் உரிமைகளைப் பாதிக்கும் நிர்வாக அதிகாரிகளுக்கு எதிராக வெளியிடப்படலாம்.\n3. அரசியலமைப்பு அல்லது சட்டத்தால் உருவாக்கப்பட்ட பொதுப் பதவியைச் சட்டவிரோதமாக ஆக்கிரமிப்பதைத் தடுக்கத் தகுதி வினவும் பேராணையை (Quo-Warranto) வெளியிடலாம்.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?"
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
                "en": "All three statements are correct. Mandamus lies only against public mandatory duties, not private/discretionary/presidential acts. Certiorari extended to administrative bodies (Kraipak case 1970). Quo-Warranto applies to public statutory offices.",
                "ta": "மூன்று கூற்றுகளும் சரியானவை. கட்டளையிடும் பேராணை தனியாருக்கு எதிராக வராது. சான்றளிப்பு பேராணை நிர்வாக அமைப்புகளுக்கும் நீட்டிக்கப்பட்டது. தகுதி வினவும் பேராணை பொதுச் சட்டப்பூர்வ பதவிகளுக்குப் பொருந்தும்."
            },
            "why_not_others": {
                "A": {"en": "Incorrect because statement 3 is also correct.", "ta": "தவறு, ஏனெனில் கூற்று 3-ம் சரியானது."},
                "B": {"en": "Incorrect because statement 1 is also correct.", "ta": "தவறு, ஏனெனில் கூற்று 1-ம் சரியானது."},
                "C": {"en": "Incorrect because statement 2 is also correct.", "ta": "தவறு, ஏனெனில் கூற்று 2-ம் சரியானது."},
                "D": {"en": "Correct. Statements 1, 2 and 3 are all factually true.", "ta": "சரி. கூற்றுகள் 1, 2 மற்றும் 3 அனைத்தும் சரியானவை."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Trap: Key difference between Prohibition and Certiorari: Prohibition is PREVENTIVE only (issued while proceeding is pending). Certiorari is PREVENTIVE and CURATIVE (issued after order is passed to quash it).",
                "ta": "TNPSC பொறி: தடுத்துநிறுத்தும் மற்றும் சான்றளிப்பு பேராணைகளுக்கு இடையிலான வேறுபாடு: தடுத்துநிறுத்தும் பேராணை தடுக்கும் (வழக்கு நிலுவையில் உள்ள போது). சான்றளிப்பு பேராணை தடுக்கும் மற்றும் குணப்படுத்தும் (உத்தரவு வந்த பின் ரத்து செய்ய)."
            },
            "revision_fact": {
                "en": "A.K. Kraipak v. Union of India (1970) extended Certiorari and Principles of Natural Justice to administrative proceedings affecting rights.",
                "ta": "ஏ.கே. கிரைபக் வழக்கில் (1970) சான்றளிப்பு பேராணை மற்றும் இயற்கை நீதி முறைகள் நிர்வாக நடவடிக்கைகளுக்கும் நீட்டிக்கப்பட்டன."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Analyze",
            "estimated_time_sec": 60,
            "pyq_similarity": "High",
            "tags": ["Polity", "Writs", "Mandamus", "Certiorari", "Quo Warranto", "Grand Test"]
        },

        # Q81: Direct MCQ - Article 33 Armed Forces FR Restrictions
        {
            "id": "FR_GT_081",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Easy",
            "question_type": "Direct MCQ",
            "question": {
                "en": "Who among the following has the exclusive constitutional power under Article 33 to restrict or abrogate the Fundamental Rights of members of the Armed Forces, Paramilitary forces, police forces, and intelligence agencies?",
                "ta": "ஆயுதப்படைகள், துணைராணுவப் படைகள், காவல் படைகள் மற்றும் உளவு அமைப்புகளின் உறுப்பினர்களின் அடிப்படை உரிமைகளைக் கட்டுப்படுத்த அல்லது நீக்கப் பிரிவு 33-ன் கீழ் பிரத்யேக அரசியலமைப்பு அதிகாரம் பெற்றவர் யார்?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "Parliament of India alone",
                    "ta": "இந்திய நாடாளுமன்றம் மட்டுமே"
                },
                {
                    "id": "B",
                    "en": "The President of India acting as Commander-in-Chief",
                    "ta": "முப்படைத் தளபதியாகச் செயல்படும் இந்தியக் குடியரசுத் தலைவர்"
                },
                {
                    "id": "C",
                    "en": "The concerned State Legislative Assembly",
                    "ta": "தொடர்புடைய மாநில சட்டமன்றம்"
                },
                {
                    "id": "D",
                    "en": "Chief of Defence Staff (CDS)",
                    "ta": "பாதுகாப்புப் படைத் தலைவர் (CDS)"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "Under Article 33, ONLY Parliament (by law) has power to restrict or modify the application of Fundamental Rights to members of Armed Forces, police forces, intelligence agencies, and telecommunication personnel. Laws made under Art 33 cannot be challenged in court for FR violation.",
                "ta": "பிரிவு 33-ன் கீழ், ஆயுதப்படைகள், காவல் படைகள், உளவு அமைப்புகளின் அடிப்படை உரிமைகளைக் கட்டுப்படுத்த நாடாளுமன்றத்திற்கு மட்டுமே (சட்டம் மூலம்) அதிகாரம் உண்டு. இச்சட்டங்களை நீதிமன்றத்தில் சவால் செய்ய முடியாது."
            },
            "why_not_others": {
                "A": {"en": "Correct. Article 33 read with Article 35(a)(i) confers exclusive power on Parliament.", "ta": "சரி. பிரிவு 33 மற்றும் 35(a)(i)-ன் படி நாடாளுமன்றத்திற்கு மட்டுமே அதிகாரம் உண்டு."},
                "B": {"en": "Incorrect. President cannot restrict FRs without parliamentary legislation under Art 33.", "ta": "தவறு. நாடாளுமன்றச் சட்டமின்றி குடியரசுத் தலைவர் கட்டுப்படுத்த முடியாது."},
                "C": {"en": "Incorrect. State Assemblies have no power under Art 33.", "ta": "தவறு. மாநில சட்டமன்றங்களுக்கு அதிகாரம் இல்லை."},
                "D": {"en": "Incorrect. CDS is a military post, not a legislative organ.", "ta": "தவறு. CDS ஒரு ராணுவப் பதவி, சட்டமன்றம் அல்ல."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: Army Act 1950, Navy Act 1950, Air Force Act 1950, Police Forces (Restriction of Rights) Act 1966 were enacted by Parliament under Article 33.",
                "ta": "TNPSC குறிப்பு: ராணுவச் சட்டம் 1950, கடற்படைச் சட்டம் 1950, விமானப்படைச் சட்டம் 1950, காவல் படை (உரிமைகள் கட்டுப்பாடு) சட்டம் 1966 ஆகியவை பிரிவு 33-ன் கீழ் நாடாளுமன்றத்தால் இயற்றப்பட்டன."
            },
            "revision_fact": {
                "en": "Article 33 covers non-combatant employees of armed forces like cooks, carpenters, mechanics, tailors, and signal personnel as well.",
                "ta": "பிரிவு 33 சமையல்காரர்கள், தச்சர்கள், மெக்கானிக்குகள் போன்ற சண்டையிடாத ஆயுதப்படை ஊழியர்களையும் உள்ளடக்கியது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Remember",
            "estimated_time_sec": 35,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 33", "Armed Forces Rights", "Grand Test"]
        },

        # Q82: Conceptual MCQ - Article 34 Martial Law vs National Emergency
        {
            "id": "FR_GT_082",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Medium",
            "question_type": "Conceptual MCQ",
            "question": {
                "en": "Which of the following correctly distinguishes Martial Law under Article 34 from National Emergency under Article 352?",
                "ta": "பிரிவு 34-ன் கீழ் உள்ள ராணுவ ஆட்சி (Martial Law) மற்றும் பிரிவு 352-ன் கீழ் உள்ள தேசிய அவசரநிலை (National Emergency) ஆகியவற்றை பின்வருவனவற்றுள் எது சரியாக வேறுபடுத்துகிறது?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "Martial Law affects only Fundamental Rights in a specific area where military rule is enforced, whereas National Emergency affects Fundamental Rights, Centre-State relations, and legislative powers across the nation",
                    "ta": "ராணுவ ஆட்சி ராணுவ விதி அமல்படுத்தப்படும் குறிப்பிட்ட பகுதியில் அடிப்படை உரிமைகளை மட்டுமே பாதிக்கிறது, அதேவேளையில் தேசிய அவசரநிலை நாடு முழுவதும் அடிப்படை உரிமைகள், மத்திய-மாநில உறவுகள் மற்றும் சட்ட அதிகாரங்களைப் பாதிக்கிறது"
                },
                {
                    "id": "B",
                    "en": "Martial Law is explicitly defined in detail in Article 34, whereas National Emergency is not defined",
                    "ta": "ராணுவ ஆட்சி பிரிவு 34-ல் விரிவாக வரையறுக்கப்பட்டுள்ளது, ஆனால் தேசிய அவசரநிலை வரையறுக்கப்படவில்லை"
                },
                {
                    "id": "C",
                    "en": "Martial Law can be declared only by State Governors, whereas National Emergency is declared by Parliament",
                    "ta": "ராணுவ ஆட்சியை மாநில ஆளுநர்கள் மட்டுமே அறிவிக்க முடியும், ஆனால் தேசிய அவசரநிலையை நாடாளுமன்றம் அறிவிக்கிறது"
                },
                {
                    "id": "D",
                    "en": "Martial Law suspends Article 21, whereas National Emergency can never affect Article 19",
                    "ta": "ராணுவ ஆட்சி பிரிவு 21-ஐ இடைநிறுத்துகிறது, ஆனால் தேசிய அவசரநிலை பிரிவு 19-ஐ ஒருபோதும் பாதிக்காது"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "Martial Law (Art 34) suspends ordinary law & government courts in a specific area under military control to restore order. National Emergency (Art 352) has wider impact across nation affecting Centre-State relations, revenue distribution, and FRs.",
                "ta": "ராணுவ ஆட்சி (பிரிவு 34) ஒரு குறிப்பிட்ட பகுதியில் சாதாரண சட்டத்தை இடைநிறுத்தி ராணுவக் கட்டுப்பாட்டைக் கொண்டுவருகிறது. தேசிய அவசரநிலை (352) மத்திய-மாநில உறவுகள், நிதிப் பகிர்வு என நாடு முழுவதும் பரந்த தாக்கம் கொண்டது."
            },
            "why_not_others": {
                "A": {"en": "Correct. Martial law is localized affecting FRs; National emergency is nationwide affecting constitutional machinery.", "ta": "சரி. ராணுவ ஆட்சி குறிப்பிட்ட பகுதி சார்ந்தது; தேசிய அவசரநிலை நாடு தழுவியது."},
                "B": {"en": "Incorrect. 'Martial Law' is NOT defined anywhere in the Constitution of India.", "ta": "தவறு. 'ராணுவ ஆட்சி' என்ற சொல் அரசியலமைப்பில் வரையறுக்கப்படவில்லை."},
                "C": {"en": "Incorrect. Declaration is not by Governors.", "ta": "தவறு. ஆளுநர்களால் அறிவிக்கப்படுவதில்லை."},
                "D": {"en": "Incorrect. Article 21 cannot be suspended even under Martial law without due process.", "ta": "தவறு. 21-ஐ தன்னிச்சையாக இடைநிறுத்த முடியாது."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Trap: 'Martial Law' has been borrowed from English Common Law. The Constitution provides for Indemnity Acts passed by Parliament to validate acts done by military personnel during martial law (Art 34).",
                "ta": "TNPSC பொறி: 'ராணுவ ஆட்சி' என்ற கருத்து ஆங்கில பொதுச் சட்டத்திலிருந்து பெறப்பட்டது. ராணுவ ஆட்சியின் போது செய்த செயல்களுக்குப் பாதுகாப்பு அளிக்கப் பாராளுமன்றம் இழப்பீட்டுச் சட்டங்களை (Indemnity Acts) இயற்றலாம் (பிரிவு 34)."
            },
            "revision_fact": {
                "en": "Martial law results in suspension of ordinary law and continuance of military tribunals, distinct from Military Law (Army Act).",
                "ta": "ராணுவ ஆட்சி சாதாரண சட்டத்தின் இடைநிறுத்தத்திற்கும் ராணுவ தீர்ப்பாயங்களின் செயல்பாட்டிற்கும் வழிவகுக்கிறது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Understand",
            "estimated_time_sec": 45,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 34", "Martial Law", "National Emergency", "Grand Test"]
        },

        # Q83: Direct MCQ - Article 35 Exclusive Power of Parliament
        {
            "id": "FR_GT_083",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Easy",
            "question_type": "Direct MCQ",
            "question": {
                "en": "Article 35 of the Constitution lays down that the power to make laws to give effect to specified Fundamental Rights (such as Articles 16(3), 32(3), 33, 34, 17, and 23) rests EXCLUSIVELY with which authority?",
                "ta": "குறிப்பிட்ட அடிப்படை உரிமைகளுக்குச் (பிரிவுகள் 16(3), 32(3), 33, 34, 17, மற்றும் 23 போன்றவை) செயலாக்கம் அளிக்கச் சட்டங்களை இயற்றும் அதிகாரம் பிரத்யேகமாக யாருக்கு மட்டுமே உண்டு எனப் பிரிவு 35 கூறுகிறது?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "Parliament of India only",
                    "ta": "இந்திய நாடாளுமன்றம் மட்டுமே"
                },
                {
                    "id": "B",
                    "en": "State Legislative Assemblies only",
                    "ta": "மாநில சட்டமன்றங்கள் மட்டுமே"
                },
                {
                    "id": "C",
                    "en": "Both Parliament and State Legislatures concurrently",
                    "ta": "நாடாளுமன்றம் மற்றும் மாநில சட்டமன்றங்கள் இரண்டும் இணைந்து"
                },
                {
                    "id": "D",
                    "en": "Law Commission of India in consultation with Bar Council",
                    "ta": "இந்தியச் சட்ட ஆணையம் மற்றும் வழக்குரைஞர் மன்றம்"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "Article 35 lays down that Parliament SHALL have, and the Legislature of a State shall NOT have, power to make laws with respect to prescribing residence under 16(3), empowering courts under 32(3), armed forces under 33, martial law indemnity under 34, and prescribing punishment for offences under Art 17 & 23, to ensure UNIFORMITY throughout India.",
                "ta": "பிரிவு 35 கூறுகிறது: இந்தியா முழுவதும் சீரான தன்மையை உறுதிசெய்ய 16(3), 32(3), 33, 34, 17, 23 ஆகிய பிரிவுகளுக்குச் சட்டங்களை இயற்றும் அதிகாரம் நாடாளுமன்றத்திற்கு மட்டுமே உண்டு, மாநில சட்டமன்றங்களுக்கு இல்லை."
            },
            "why_not_others": {
                "A": {"en": "Correct. Article 35 explicitly reserves this power exclusively for Parliament.", "ta": "சரி. பிரிவு 35 இந்த அதிகாரத்தை நாடாளுமன்றத்திற்கு மட்டுமே அளிக்கிறது."},
                "B": {"en": "Incorrect. State Legislatures are explicitly denied this power under Art 35.", "ta": "தவறு. மாநில சட்டமன்றங்களுக்கு இந்த அதிகாரம் மறுக்கப்பட்டுள்ளது."},
                "C": {"en": "Incorrect. It is not a concurrent power.", "ta": "தவறு. இது பொதுவான அதிகாரம் அல்ல."},
                "D": {"en": "Incorrect. Law Commission is an advisory body.", "ta": "தவறு. சட்ட ஆணையம் ஓர் ஆலோசனைக் குழு."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: Article 35 ensures that punishments for untouchability (Art 17) or forced labour (Art 23) are UNIFORM across all States in India, rather than varying state to state.",
                "ta": "TNPSC குறிப்பு: பிரிவு 35 தீண்டாமை (17) மற்றும் கட்டாய வேலைக்கான (23) தண்டனைகள் மாநிலத்திற்கு மாநிலம் மாறாமல் இந்தியா முழுவதும் சீராக இருப்பதை உறுதி செய்கிறது."
            },
            "revision_fact": {
                "en": "Any law in force at the commencement of the Constitution regarding punishments for Art 17/23 continues until altered or repealed by Parliament under Article 35.",
                "ta": "அரசியலமைப்புத் தொடக்கத்தின் போது இருந்த குற்றவியல் சட்டங்கள் நாடாளுமன்றம் மாற்றும் வரை நீடிக்கும்."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Remember",
            "estimated_time_sec": 35,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 35", "Parliament Exclusive Power", "Grand Test"]
        },

        # Q84: Conceptual MCQ - FR vs DPSP Conflict Evolution
        {
            "id": "FR_GT_084",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Medium",
            "question_type": "Conceptual MCQ",
            "question": {
                "en": "How did the Supreme Court resolve the constitutional conflict between Fundamental Rights (Part III) and Directive Principles of State Policy (Part IV) in Minerva Mills v. Union of India (1980)?",
                "ta": "மினர்வா மில்ஸ் எதிர் இந்திய யூனியன் (1980) வழக்கில் அடிப்படை உரிமைகளுக்கும் (பகுதி III) அரசு வழிகாட்டு நெறிமுறைகளுக்கும் (பகுதி IV) இடையிலான அரசியலமைப்பு மோதலை உச்ச நீதிமன்றம் எவ்வாறு தீர்த்தது?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "By declaring that the Indian Constitution is founded on the bedrock of the balance between Part III and Part IV, and giving total primacy to one over the other destroys the Basic Structure",
                    "ta": "இந்திய அரசியலமைப்பு பகுதி III மற்றும் பகுதி IV இடையிலான சமநிலையின் அடித்தளத்தில் அமைந்துள்ளது என்றும், ஒன்றிற்கு மற்றொன்றை விட முழு முதன்மை அளிப்பது அடிப்படை அமைப்பை அழிப்பதாகும் என்றும் அறிவித்ததன் மூலம்"
                },
                {
                    "id": "B",
                    "en": "By declaring that Directive Principles are absolute and completely supersede Fundamental Rights under all circumstances",
                    "ta": "வழிகாட்டு நெறிமுறைகள் முற்றுமுழுதானவை மற்றும் அனைத்துச் சூழ்நிலைகளிலும் அடிப்படை உரிமைகளை முற்றிலும் மிஞ்சும் என்று அறிவித்ததன் மூலம்"
                },
                {
                    "id": "C",
                    "en": "By declaring that Fundamental Rights are completely unamendable by Parliament under any section",
                    "ta": "அடிப்படை உரிமைகளை நாடாளுமன்றத்தால் எந்தப் பிரிவின் கீழும் முற்றிலும் திருத்த முடியாது என்று அறிவித்ததன் மூலம்"
                },
                {
                    "id": "D",
                    "en": "By abolishing Directive Principles from Part IV of the Constitution",
                    "ta": "அரசியலமைப்பின் பகுதி IV-லிருந்து வழிகாட்டு நெறிமுறைகளை ஒழித்ததன் மூலம்"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "In Minerva Mills (1980), SC held: 'The Indian Constitution is founded on the bedrock of the balance between Part III and Part IV. To give absolute primacy to one over the other is to disturb the harmony of the Constitution. This harmony is a basic feature'.",
                "ta": "மினர்வா மில்ஸ் வழக்கில் (1980) உச்ச நீதிமன்றம் கூறியது: 'இந்திய அரசியலமைப்பு பகுதி III மற்றும் பகுதி IV இடையிலான சமநிலையின் அடித்தளத்தில் நிறுவப்பட்டுள்ளது. இந்த இணக்கமே அடிப்படை அம்சமாகும்'."
            },
            "why_not_others": {
                "A": {"en": "Correct. Harmony and balance between FRs and DPSPs was declared a Basic Structure feature.", "ta": "சரி. FR மற்றும் DPSP இடையிலான இணக்கம் மற்றும் சமநிலை அடிப்படை அமைப்பு எனப்பட்டது."},
                "B": {"en": "Incorrect. SC struck down 42nd Amendment expansion giving total primacy to all DPSPs.", "ta": "தவறு. அனைத்து DPSP-களுக்கும் முதன்மை தந்த 42-வது திருத்தப் பிரிவை SC ரத்து செய்தது."},
                "C": {"en": "Incorrect. FRs can be amended without damaging basic structure.", "ta": "தவறு. அடிப்படை அமைப்பைச் சிதைக்காமல் FR-களைத் திருத்தலாம்."},
                "D": {"en": "Incorrect. DPSPs were not abolished.", "ta": "தவறு. DPSP-கள் ஒழிக்கப்படவில்லை."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: Evolution of FR vs DPSP Relationship: Champakam Dorairajan (1951 - FRs superior) -> Re Kerala Education Bill (1958 - Harmonious Construction) -> 25th Amendment 1971 (31C inserted) -> Kesavananda Bharati (1973 - 31C part 1 valid) -> Minerva Mills (1980 - Balance is Basic Structure).",
                "ta": "TNPSC குறிப்பு: FR vs DPSP உறவின் வளர்ச்சி: செண்பகம் துரைராஜன் (1951 - FR மேலானது) -> கேரளா கல்வி மசோதா (1958 - இணக்கமான விளக்கம்) -> 25-வது திருத்தம் 1971 -> கேசவாநந்த பாரதி (1973) -> மினர்வா மில்ஸ் (1980 - சமநிலையே அடிப்படை அமைப்பு)."
            },
            "revision_fact": {
                "en": "Article 31C saves laws enforcing DPSP 39(b) and 39(c) from being invalidated under Article 14 and Article 19.",
                "ta": "பிரிவு 31C என்பது DPSP 39(b) மற்றும் 39(c)-ஐ செயல்படுத்தும் சட்டங்களைப் பிரிவு 14, 19-லிருந்து பாதுகாக்கிறது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Understand",
            "estimated_time_sec": 45,
            "pyq_similarity": "High",
            "tags": ["Polity", "FR vs DPSP", "Minerva Mills", "Basic Structure", "Grand Test"]
        },

        # Q85: Statement-Based - Basic Structure & Kesavananda Bharati Case
        {
            "id": "FR_GT_085",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Hard",
            "question_type": "Statement-Based",
            "question": {
                "en": "Consider the following statements regarding the landmark Kesavananda Bharati v. State of Kerala (1973) judgment:\n1. A 13-judge Constitution Bench by a 7:6 majority held that Parliament has the power to amend any part of the Constitution under Article 368, including Fundamental Rights.\n2. The Supreme Court laid down the 'Basic Structure Doctrine', ruling that Parliament cannot alter the basic features or fundamental framework of the Constitution.\n3. The judgment overruled the earlier Golak Nath judgment (1967) which had placed Fundamental Rights beyond the amending power of Parliament.\nWhich of the statements given above are correct?",
                "ta": "முக்கியத்துவமிக்க கேசவாநந்த பாரதி எதிர் கேரளா அரசு (1973) தீர்ப்பு பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 13 நீதிபதிகள் கொண்ட அரசியலமைப்பு அமர்வு 7:6 பெரும்பான்மையில், அடிப்படை உரிமைகள் உட்பட அரசியலமைப்பின் எந்தப் பகுதியையும் பிரிவு 368-ன் கீழ் திருத்த நாடாளுமன்றத்திற்கு அதிகாரம் உண்டு என்று தீர்ப்பளித்தது.\n2. நாடாளுமன்றம் அரசியலமைப்பின் அடிப்படை அம்சங்களை அல்லது அடிப்படை கட்டமைப்பை மாற்ற முடியாது என்று தீர்ப்பளித்து உச்ச நீதிமன்றம் 'அடிப்படை அமைப்புக் கோட்பாட்டை' வகுத்தது.\n3. அடிப்படை உரிமைகளை நாடாளுமன்றத்தின் திருத்தும் அதிகாரத்திற்கு அப்பாற்பட்டதாக வைத்த முந்தைய கோலக் நாத் தீர்ப்பை (1967) இத்தீர்ப்பு ரத்து செய்தது.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?"
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
                "en": "All three statements are correct. Kesavananda Bharati judgment (24th April 1973 - largest 13-judge bench) overruled Golak Nath (1967), affirmed Parliament's power to amend Part III, but created the Basic Structure limitation on amending power.",
                "ta": "மூன்று கூற்றுகளும் சரியானவை. கேசவாநந்த பாரதி தீர்ப்பு (24 ஏப்ரல் 1973 - 13 நீதிபதிகள் அமர்வு) கோலக் நாத் தீர்ப்பை ரத்து செய்தது, பகுதி III-ஐத் திருத்தும் அதிகாரத்தை உறுதி செய்து அடிப்படை அமைப்புக் கோட்பாட்டை உருவாக்கியது."
            },
            "why_not_others": {
                "A": {"en": "Incorrect because statement 3 is also correct.", "ta": "தவறு, ஏனெனில் கூற்று 3-ம் சரியானது."},
                "B": {"en": "Incorrect because statement 1 is also correct.", "ta": "தவறு, ஏனெனில் கூற்று 1-ம் சரியானது."},
                "C": {"en": "Incorrect because statement 2 is also correct.", "ta": "தவறு, ஏனெனில் கூற்று 2-ம் சரியானது."},
                "D": {"en": "Correct. All statements 1, 2 and 3 are factually accurate.", "ta": "சரி. கூற்றுகள் 1, 2 மற்றும் 3 அனைத்தும் சரியானவை."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: Chief Justice S.M. Sikri headed the 13-judge bench in Kesavananda Bharati case. The judgment was delivered on April 24, 1973.",
                "ta": "TNPSC குறிப்பு: தலைமை நீதிபதி எஸ்.எம். சிக்ரி கேசவாநந்த பாரதி வழக்கின் 13 நீதிபதிகள் அமர்வுக்குத் தலைமை தாங்கினார். தீர்ப்பு ஏப்ரல் 24, 1973 அன்று வழங்கப்பட்டது."
            },
            "revision_fact": {
                "en": "Basic structure is NOT defined in the Constitution. The Supreme Court determines what constitutes basic structure on a case-by-case basis.",
                "ta": "அடிப்படை அமைப்பு அரசியலமைப்பில் வரையறுக்கப்படவில்லை. உச்ச நீதிமன்றமே வழக்கு வாரியாக அதைத் தீர்மானிக்கிறது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Analyze",
            "estimated_time_sec": 60,
            "pyq_similarity": "High",
            "tags": ["Polity", "Kesavananda Bharati", "Basic Structure", "Golak Nath", "Grand Test"]
        },

        # Q86: PYQ Pattern - Writs Locus Standi Exemption
        {
            "id": "FR_GT_086",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Easy",
            "question_type": "PYQ Pattern",
            "question": {
                "en": "In which of the following writs is the traditional rule of 'Locus Standi' (that only an aggrieved person whose rights are injured can approach the court) relaxed, allowing ANY public-spirited citizen or interested person to file a petition?",
                "ta": "பின்வரும் எந்தப் பேராணையில் 'Locus Standi' (பாதிக்கப்பட்ட நபர் மட்டுமே நீதிமன்றத்தை அணுக முடியும்) என்ற பாரம்பரிய விதி தளர்த்தப்பட்டு, எந்தவொரு பொதுநலக் குடிமகனும் அல்லது ஆர்வமுள்ள நபரும் மனு தாக்கல் செய்ய அனுமதிக்கப்படுகிறார்?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "Quo-Warranto and Habeas Corpus",
                    "ta": "தகுதி வினவும் பேராணை மற்றும் ஆட்கொணர் பேராணை"
                },
                {
                    "id": "B",
                    "en": "Prohibition only",
                    "ta": "தடுத்துநிறுத்தும் பேராணை மட்டுமே"
                },
                {
                    "id": "C",
                    "en": "Certiorari only",
                    "ta": "சான்றளிப்பு பேராணை மட்டுமே"
                },
                {
                    "id": "D",
                    "en": "Mandamus only",
                    "ta": "கட்டளையிடும் பேராணை மட்டுமே"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "Locus standi is relaxed for Quo-Warranto (any interested person can challenge unauthorized occupancy of public office) and Habeas Corpus (a friend, relative, or public citizen can file on behalf of a detained person). Public Interest Litigation (PIL) further relaxed locus standi generally.",
                "ta": "தகுதி வினவும் பேராணை (யார் வேண்டுமானாலும் பொதுப் பதவி ஆக்கிரமிப்பைச் சவால் செய்யலாம்) மற்றும் ஆட்கொணர் பேராணையில் (நண்பர்/உறவினர் தாக்கல் செய்யலாம்) Locus Standi விதி தளர்த்தப்பட்டுள்ளது."
            },
            "why_not_others": {
                "A": {"en": "Correct. Quo-Warranto and Habeas Corpus permit non-aggrieved interested persons to file.", "ta": "சரி. தகுதி வினவும் மற்றும் ஆட்கொணர் பேராணைகள் பாதிக்கப்பட்டவர் அல்லாதோரை அனுமதிக்கின்றன."},
                "B": {"en": "Incorrect. Prohibition requires an aggrieved party or pending judicial proceeding.", "ta": "தவறு. தடுத்துநிறுத்தும் பேராணைக்கு பாதிக்கப்பட்ட தரப்பு தேவை."},
                "C": {"en": "Incorrect. Certiorari requires an aggrieved party.", "ta": "தவறு. சான்றளிப்பு பேராணைக்கு பாதிக்கப்பட்ட தரப்பு தேவை."},
                "D": {"en": "Incorrect. Mandamus generally requires a person with legal right to performance of duty.", "ta": "தவறு. கட்டளையிடும் பேராணைக்குச் சட்டப்பூர்வ உரிமை தேவை."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: Quo-Warranto is unique because it CANNOT be issued against a ministerial office or private office; it lies ONLY against a substantive public office created by statute or Constitution.",
                "ta": "TNPSC குறிப்பு: தகுதி வினவும் பேராணை அமைச்சரவைப் பதவிக்கோ அல்லது தனியார் பதவிக்கோ எதிராக வர முடியாது; சட்டப்பூர்வ பொதுப் பதவிக்கு மட்டுமே வரும்."
            },
            "revision_fact": {
                "en": "SP Gupta v. Union of India (1981) (First Judges Case) formalized the relaxation of Locus Standi in Indian jurisprudence giving birth to modern PIL.",
                "ta": "எஸ்.பி. குப்தா வழக்கின் மூலம் (1981) Locus Standi தளர்வு முறைப்படுத்தப்பட்டு நவீன PIL உருவானது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Remember",
            "estimated_time_sec": 35,
            "pyq_similarity": "High",
            "tags": ["Polity", "Quo Warranto", "Habeas Corpus", "Locus Standi", "Grand Test"]
        },

        # Q87: Hard / Analytical - 25th Amendment Act & Article 31C
        {
            "id": "FR_GT_087",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Hard",
            "question_type": "Hard / Analytical",
            "question": {
                "en": "The 25th Constitutional Amendment Act, 1971 introduced Article 31C containing two parts. What did the Supreme Court decide regarding Article 31C in the Kesavananda Bharati case (1973)?",
                "ta": "1971-ன் 25-வது அரசியலமைப்புத் திருத்தச் சட்டம் இரு பகுதிகளைக் கொண்ட பிரிவு 31C-ஐ அறிமுகப்படுத்தியது. கேசவாநந்த பாரதி வழக்கில் (1973) பிரிவு 31C தொடர்பாக உச்ச நீதிமன்றம் என்ன தீர்ப்பு அளித்தது?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "Upheld the first part of Article 31C (saving laws giving effect to DPSP 39(b) and (c) from Art 14 & 19), but struck down the second part which attempted to bar judicial review",
                    "ta": "பிரிவு 31C-ன் முதல் பகுதியை (DPSP 39(b), (c)-ஐ செயல்படுத்தும் சட்டங்களை 14 & 19-லிருந்து காப்பாற்றுதல்) உறுதி செய்தது, ஆனால் நீதித்துறை மறுஆய்வைத் தடுக்க முயன்ற 2-வது பகுதியை ரத்து செய்தது"
                },
                {
                    "id": "B",
                    "en": "Struck down the entire Article 31C as unconstitutional",
                    "ta": "பிரிவு 31C முழுவதையும் அரசியலமைப்புக்கு முரணானது என ரத்து செய்தது"
                },
                {
                    "id": "C",
                    "en": "Upheld both parts of Article 31C completely without any modification",
                    "ta": "பிரிவு 31C-ன் இரு பகுதிகளையும் எந்த மாற்றமும் இன்றி முழுமையாக உறுதி செய்தது"
                },
                {
                    "id": "D",
                    "en": "Replaced Article 31C with Article 300A",
                    "ta": "பிரிவு 31C-க்கு பதிலாக பிரிவு 300A-ஐ மாற்றியது"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "In Kesavananda Bharati (1973), SC upheld 31C part 1 (saving laws carrying out DPSP 39(b) & (c) from Art 14 & 19 violation). But it struck down part 2 ('no law containing a declaration that it gives effect to such policy shall be called in question in any court') because Judicial Review is a basic feature.",
                "ta": "கேசவாநந்த பாரதி வழக்கில் (1973) 31C முதல் பகுதி (DPSP 39(b), (c) பாதுகாப்பு) உறுதி செய்யப்பட்டது. ஆனால் நீதித்துறை மறுஆய்வைத் தடுக்கும் 2-வது பகுதி ரத்து செய்யப்பட்டது."
            },
            "why_not_others": {
                "A": {"en": "Correct. Part 1 was upheld; Part 2 excluding judicial review was struck down.", "ta": "சரி. பகுதி 1 உறுதி செய்யப்பட்டது; நீதித்துறை மறுஆய்வைத் தடுத்த பகுதி 2 ரத்து செய்யப்பட்டது."},
                "B": {"en": "Incorrect. 31C was not struck down entirely.", "ta": "தவறு. 31C முற்றிலும் ரத்து செய்யப்படவில்லை."},
                "C": {"en": "Incorrect. Part 2 was struck down.", "ta": "தவறு. பகுதி 2 ரத்து செய்யப்பட்டது."},
                "D": {"en": "Incorrect. 300A was added by 44th Amendment in 1978.", "ta": "தவறு. 300A 1978-ல் 44-வது திருத்தத்தால் சேர்க்கப்பட்டது."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: Famous dictum regarding Article 31C: 'Where Article 31C comes in, Article 14 goes out'.",
                "ta": "TNPSC குறிப்பு: பிரிவு 31C பற்றிய புகழ்பெற்ற கூற்று: 'பிரிவு 31C நுழையும் இடத்தில், பிரிவு 14 வெளியேறுகிறது'."
            },
            "revision_fact": {
                "en": "42nd Amendment Act 1976 attempted to extend Article 31C protection to ALL DPSPs, but Minerva Mills (1980) struck down that extension, restoring 31C protection ONLY to DPSP 39(b) and 39(c).",
                "ta": "42-வது திருத்தம் 31C-ஐ அனைத்து DPSP-களுக்கும் நீட்டிக்க முயன்றது, ஆனால் மினர்வா மில்ஸ் (1980) அதை ரத்து செய்து 39(b), 39(c)-க்கு மட்டும் மீண்டும் நிலைநிறுத்தியது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Analyze",
            "estimated_time_sec": 60,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 31C", "25th Amendment", "Kesavananda Bharati", "Grand Test"]
        },

        # Q88: Conceptual MCQ - Fundamental Rights Available Only to Citizens
        {
            "id": "FR_GT_088",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Medium",
            "question_type": "Conceptual MCQ",
            "question": {
                "en": "Which set of Articles under Part III of the Constitution of India guarantees Fundamental Rights exclusively to Citizens of India and NOT to foreigners?",
                "ta": "இந்திய அரசியலமைப்பின் பகுதி III-ன் கீழ் எந்தப் பிரிவுகளின்த் தொகுதி அடிப்படை உரிமைகளை வெளிநாட்டினருக்கு வழங்காமல் இந்தியக் குடிமக்களுக்கு மட்டுமே பிரத்யேகமாக உத்தரவாதம் அளிக்கிறது?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "Articles 15, 16, 19, 29 and 30",
                    "ta": "பிரிவுகள் 15, 16, 19, 29 மற்றும் 30"
                },
                {
                    "id": "B",
                    "en": "Articles 14, 20, 21, 21A and 22",
                    "ta": "பிரிவுகள் 14, 20, 21, 21A மற்றும் 22"
                },
                {
                    "id": "C",
                    "en": "Articles 23, 24, 25, 26 and 27",
                    "ta": "பிரிவுகள் 23, 24, 25, 26 மற்றும் 27"
                },
                {
                    "id": "D",
                    "en": "Articles 14, 19, 21, 25 and 32",
                    "ta": "பிரிவுகள் 14, 19, 21, 25 மற்றும் 32"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "Fundamental Rights available ONLY to Citizens: (1) Art 15 (Non-discrimination), (2) Art 16 (Equal opportunity in public employment), (3) Art 19 (Six freedoms), (4) Art 29 (Protection of language/culture), (5) Art 30 (Minority educational institutions). All other FRs apply to citizens and non-citizens.",
                "ta": "குடிமக்களுக்கு மட்டுமே உரிய அடிப்படை உரிமைகள்: 15, 16, 19, 29, மற்றும் 30. மற்ற அனைத்து உரிமைகளும் குடிமக்கள் மற்றும் வெளிநாட்டினருக்குப் பொருந்தும்."
            },
            "why_not_others": {
                "A": {"en": "Correct. Articles 15, 16, 19, 29, 30 are citizen-exclusive FRs.", "ta": "சரி. பிரிவுகள் 15, 16, 19, 29, 30 குடிமக்களுக்கு மட்டுமே உரியவை."},
                "B": {"en": "Incorrect. Articles 14, 20, 21, 21A, 22 apply to all persons (citizens & foreigners).", "ta": "தவறு. 14, 20, 21, 21A, 22 அனைவருக்கும் பொருந்தும்."},
                "C": {"en": "Incorrect. Articles 23, 24, 25, 26, 27 apply to all persons.", "ta": "தவறு. 23, 24, 25, 26, 27 அனைவருக்கும் பொருந்தும்."},
                "D": {"en": "Incorrect. 14, 21, 25 apply to all persons.", "ta": "தவறு. 14, 21, 25 அனைவருக்கும் பொருந்தும்."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: Enemy aliens (citizens of a country at war with India) do NOT enjoy protection against arrest and detention under Article 22, nor do they enjoy Article 14/21 during war.",
                "ta": "TNPSC குறிப்பு: எதிரி நாட்டினருக்குப் பிரிவு 22-ன் கீழ் உள்ள பாதுகாப்புகள் கிடைக்காது."
            },
            "revision_fact": {
                "en": "Fundamental Rights conferred on all persons include equality before law (14), protection of life (21), right to education (21A), freedom of religion (25-28).",
                "ta": "அனைத்து நபர்களுக்கும் உள்ள உரிமைகளில் 14, 20, 21, 21A, 22, 23, 24, 25, 26, 27, 28 ஆகியவை அடங்கும்."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Understand",
            "estimated_time_sec": 40,
            "pyq_similarity": "High",
            "tags": ["Polity", "Citizen Rights", "Article 15 16 19 29 30", "Grand Test"]
        },

        # Q89: Chronology - Fundamental Rights Evolution Cases
        {
            "id": "FR_GT_089",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Hard",
            "question_type": "Chronology",
            "question": {
                "en": "Arrange the following landmark Supreme Court cases on Constitutional Amending Power and Fundamental Rights in chronological sequence:\n1. Shankari Prasad v. Union of India\n2. Sajjan Singh v. State of Rajasthan\n3. I.C. Golak Nath v. State of Punjab\n4. Kesavananda Bharati v. State of Kerala",
                "ta": "அரசியலமைப்புத் திருத்தும் அதிகாரம் மற்றும் அடிப்படை உரிமைகள் தொடர்பான பின்வரும் உச்ச நீதிமன்ற வழக்குகளைச் சரியான காலவரிசையில் அமைக்கவும்:\n1. சங்கரி பிரசாத் எதிர் இந்திய யூனியன்\n2. சஜ்ஜன் சிங் எதிர் ராஜஸ்தான் அரசு\n3. I.C. கோலக் நாத் எதிர் பஞ்சாப் அரசு\n4. கேசவாநந்த பாரதி எதிர் கேரளா அரசு"
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
                "en": "Correct chronological sequence: (1) Shankari Prasad case (1951 - 1st Amendment upheld); (2) Sajjan Singh case (1965 - 17th Amendment upheld); (3) Golak Nath case (1967 - FRs non-amendable); (4) Kesavananda Bharati case (1973 - Basic Structure doctrine).",
                "ta": "சரியான காலவரிசை: (1) சங்கரி பிரசாத் (1951); (2) சஜ்ஜன் சிங் (1965); (3) கோலக் நாத் (1967); (4) கேசவாநந்த பாரதி (1973)."
            },
            "why_not_others": {
                "A": {"en": "Correct sequence: 1951 -> 1965 -> 1967 -> 1973.", "ta": "சரியான வரிசை: 1951 -> 1965 -> 1967 -> 1973."},
                "B": {"en": "Incorrect sequence.", "ta": "தவறான வரிசை."},
                "C": {"en": "Incorrect sequence.", "ta": "தவறான வரிசை."},
                "D": {"en": "Incorrect sequence.", "ta": "தவறான வரிசை."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: In Shankari Prasad (1951) and Sajjan Singh (1965), Supreme Court held that Parliament CAN amend Fundamental Rights under Art 368. Golak Nath (1967) reversed this. Kesavananda (1973) restored amending power subject to Basic Structure.",
                "ta": "TNPSC குறிப்பு: சங்கரி பிரசாத் (1951) மற்றும் சஜ்ஜன் சிங் (1965) வழக்குகளில் FR-களைத் திருத்தலாம் எனப்பட்டது. கோலக் நாத் (1967) இதை மாற்றியது. கேசவாநந்த பாரதி (1973) அடிப்படை அமைப்புக்கு உட்பட்டுத் திருத்தலாம் என்றது."
            },
            "revision_fact": {
                "en": "Justice H.R. Khanna's vote in the 7:6 majority in Kesavananda Bharati case was crucial in establishing the Basic Structure doctrine.",
                "ta": "கேசவாநந்த பாரதி வழக்கின் 7:6 பெரும்பான்மையில் நீதிபதி எச்.ஆர். கன்னாவின் வாக்கு அடிப்படை அமைப்பை நிறுவுவதில் தீர்க்கமானதாக இருந்தது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Analyze",
            "estimated_time_sec": 55,
            "pyq_similarity": "High",
            "tags": ["Polity", "Amending Power", "Chronology", "Grand Test"]
        },

        # Q90: TNPSC Trap - Writ of Certiorari vs Prohibition
        {
            "id": "FR_GT_090",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Medium",
            "question_type": "TNPSC Trap",
            "question": {
                "en": "Regarding the Writ of Certiorari, which of the following statements is INCORRECT?",
                "ta": "சான்றளிப்பு நீதிப் பேராணை (Writ of Certiorari) பற்றிய பின்வரும் கூற்றுகளில் எது தவறானது?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "Certiorari can be issued against legislative bodies and private individuals to quash unconstitutional statutes",
                    "ta": "அரசியலமைப்புக்கு முரணான சட்டங்களை ரத்து செய்ய சட்டமன்ற அமைப்புகள் மற்றும் தனியார் நபர்களுக்கு எதிராகச் சான்றளிப்பு பேராணையை வெளியிட முடியும்"
                },
                {
                    "id": "B",
                    "en": "Certiorari is issued by a higher court to a lower court or tribunal to quash an order passed in excess of jurisdiction",
                    "ta": "அதிகார வரம்பை மீறி பிறப்பிக்கப்பட்ட உத்தரவை ரத்து செய்ய உயர் நீதிமன்றத்தால் கீழ் நீதிமன்றம் அல்லது தீர்ப்பாயத்திற்குச் சான்றளிப்பு பேராணை பிறப்பிக்கப்படுகிறது"
                },
                {
                    "id": "C",
                    "en": "Unlike Prohibition, Certiorari is both preventive and curative",
                    "ta": "தடுத்துநிறுத்தும் பேராணையைப் போலன்றி, சான்றளிப்பு பேராணை தடுக்கும் மற்றும் குணப்படுத்தும் இரு தன்மைகளையும் கொண்டது"
                },
                {
                    "id": "D",
                    "en": "In 1991, the Supreme Court ruled that Certiorari can be issued even against administrative authorities affecting individual rights",
                    "ta": "1991-ல் நபர்களின் உரிமைகளைப் பாதிக்கும் நிர்வாக அதிகாரிகளுக்கு எதிராகவும் சான்றளிப்பு பேராணையை வெளியிடலாம் என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "Statement A is INCORRECT (making it the correct answer). Like Prohibition, Certiorari is NOT available against legislative bodies and private individuals or bodies.",
                "ta": "கூற்று A தவறானது (எனவே இது சரியான விடை). தடுத்துநிறுத்தும் பேராணையைப் போலவே சான்றளிப்பு பேராணையும் சட்டமன்ற அமைப்புகள் மற்றும் தனியார் நபர்களுக்கு எதிராக வெளியிடப்பட முடியாது."
            },
            "why_not_others": {
                "A": {"en": "Correct answer (incorrect statement). Certiorari CANNOT be issued against legislative bodies or private persons.", "ta": "சரியான விடை (தவறான கூற்று). சான்றளிப்பு பேராணை சட்டமன்றங்கள் அல்லது தனியாருக்கு எதிராக வராது."},
                "B": {"en": "Incorrect answer (correct statement). Certiorari quashes lower court orders.", "ta": "தவறான விடை (சரியான கூற்று). சான்றளிப்பு பேராணை உத்தரவை ரத்து செய்கிறது."},
                "C": {"en": "Incorrect answer (correct statement). Certiorari is preventive and curative.", "ta": "தவறான விடை (சரியான கூற்று). சான்றளிப்பு பேராணை தடுக்கும் மற்றும் குணப்படுத்தும்."},
                "D": {"en": "Incorrect answer (correct statement). In 1991 SC extended Certiorari to administrative authorities.", "ta": "தவறான விடை (சரியான கூற்று). 1991-ல் நிர்வாக அதிகாரிகளுக்கும் நீட்டிக்கப்பட்டது."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Trap: Certiorari is issued on grounds of: (1) Excess/lack of jurisdiction, (2) Error of law apparent on the face of record, (3) Violation of natural justice.",
                "ta": "TNPSC பொறி: சான்றளிப்பு பேராணை வழங்கப்படும் அடிப்படைகள்: (1) அதிகார வரம்பு மீறல், (2) வெளிப்படையான சட்டப் பிழை, (3) இயற்கை நீதி மீறல்."
            },
            "revision_fact": {
                "en": "Prohibition is issued when proceedings are PENDING in lower court. Certiorari is issued AFTER the lower court has delivered its order.",
                "ta": "வழக்கு நிலுவையில் உள்ள போது தடுத்துநிறுத்தும் பேராணையும், உத்தரவு வந்த பின் சான்றளிப்பு பேராணையும் பிறப்பிக்கப்படும்."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Understand",
            "estimated_time_sec": 45,
            "pyq_similarity": "High",
            "tags": ["Polity", "Writs", "Certiorari", "TNPSC Trap", "Grand Test"]
        },

        # Q91: Hard / Analytical - Suspension of FRs Art 358 vs 359
        {
            "id": "FR_GT_091",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Hard",
            "question_type": "Hard / Analytical",
            "question": {
                "en": "Which of the following correctly distinguishes the operation of Article 358 from Article 359 during a National Emergency?",
                "ta": "தேசிய அவசரநிலையின் போது பிரிவு 358-ன் செயல்பாட்டைப் பிரிவு 359-ன் செயல்பாட்டிலிருந்து பின்வருவனவற்றுள் எது சரியாக வேறுபடுத்துகிறது?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "Article 358 automatically suspends Article 19 freedoms throughout India upon External Emergency, whereas Article 359 suspends only the RIGHT TO MOVE COURT for enforcement of specified FRs by Presidential Order",
                    "ta": "வெளிப்புற அவசரநிலையின் போது பிரிவு 358 இந்தியா முழுவதும் பிரிவு 19 சுதந்திரங்களைத் தானாகவே இடைநிறுத்துகிறது, அதேவேளையில் பிரிவு 359 குடியரசுத் தலைவரின் உத்தரவு மூலம் குறிப்பிட்ட உரிமைகளை அமல்படுத்த நீதிமன்றம் செல்லும் உரிமையை மட்டுமே இடைநிறுத்துகிறது"
                },
                {
                    "id": "B",
                    "en": "Article 358 applies to all Fundamental Rights, whereas Article 359 applies only to Article 21",
                    "ta": "பிரிவு 358 அனைத்து அடிப்படை உரிமைகளுக்கும் பொருந்தும், ஆனால் பிரிவு 359 பிரிவு 21-க்கு மட்டுமே பொருந்தும்"
                },
                {
                    "id": "C",
                    "en": "Article 358 requires approval of Parliament within 1 month, whereas Article 359 requires no parliamentary approval",
                    "ta": "பிரிவு 358-க்கு 1 மாதத்திற்குள் நாடாளுமன்ற ஒப்புதல் தேவை, ஆனால் பிரிவு 359-க்கு ஒப்புதல் தேவையில்லை"
                },
                {
                    "id": "D",
                    "en": "Article 358 operates during Armed Rebellion, whereas Article 359 operates only during War",
                    "ta": "பிரிவு 358 ஆயுதமேந்திய கிளர்ச்சியின் போது செயல்படுகிறது, ஆனால் பிரிவு 359 போரின் போது மட்டுமே செயல்படுகிறது"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "Article 358 automatically suspends Art 19 (only during External Emergency - War/External Aggression). Article 359 does NOT suspend FRs directly; it suspends their ENFORCEMENT in courts by Presidential Order for specified rights (excluding Arts 20 & 21).",
                "ta": "பிரிவு 358 வெளிப்புற அவசரநிலையின் போது பிரிவு 19-ஐத் தானாகவே இடைநிறுத்துகிறது. பிரிவு 359 உரிமைகளை நேரடியாக இடைநிறுத்தாமல், குறிப்பிட்ட உரிமைகளை நீதிமன்றத்தில் அமல்படுத்துவதை மட்டுமே குடியரசுத் தலைவர் உத்தரவு மூலம் இடைநிறுத்துகிறது (பிரிவுகள் 20, 21 தவிர)."
            },
            "why_not_others": {
                "A": {"en": "Correct. Art 358 suspends Art 19 directly; Art 359 suspends enforcement of specified FRs via presidential order.", "ta": "சரி. பிரிவு 358 நேரடியாக 19-ஐ இடைநிறுத்தும்; 359 நீதிமன்ற அமலாக்கத்தை இடைநிறுத்தும்."},
                "B": {"en": "Incorrect. Art 358 applies only to Art 19.", "ta": "தவறு. 358 பிரிவு 19-க்கு மட்டுமே பொருந்தும்."},
                "C": {"en": "Incorrect. Parliamentary approval of emergency declaration covers both.", "ta": "தவறு. அவசரநிலை ஒப்புதல் இரண்டிற்கும் பொருந்தும்."},
                "D": {"en": "Incorrect. Art 358 does NOT operate during Armed Rebellion (44th Amendment).", "ta": "தவறு. 358 ஆயுதமேந்திய கிளர்ச்சியின் போது செயல்படாது."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: Two main differences: (1) Art 358 is confined to Art 19 only; Art 359 extends to specified FRs (except 20 & 21). (2) Art 358 operates automatically throughout India; Art 359 operates via Presidential Order for whole or part of India.",
                "ta": "TNPSC குறிப்பு: இரு முக்கிய வேறுபாடுகள்: (1) 358 பிரிவு 19-க்கு மட்டுமே; 359 குறிப்பிடப்பட்ட உரிமைகளுக்கு (20, 21 தவிர). (2) 358 தானாகவே செயல்படும்; 359 குடியரசுத் தலைவர் உத்தரவு மூலம் செயல்படும்."
            },
            "revision_fact": {
                "en": "44th Amendment Act 1978 inserted proviso to Art 358 stating that Art 19 is suspended ONLY when Emergency is declared on ground of War or External Aggression.",
                "ta": "44-வது திருத்தச் சட்டம் 1978 போர் அல்லது வெளிநாட்டு ஆக்கிரமிப்பின் போது மட்டுமே பிரிவு 19 இடைநிறுத்தப்படும் என 358-ல் நிபந்தனை இணைத்தது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Analyze",
            "estimated_time_sec": 60,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 358", "Article 359", "Suspension of Rights", "Grand Test"]
        },

        # Q92: Direct MCQ - Writ of Habeas Corpus Scope
        {
            "id": "FR_GT_092",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Easy",
            "question_type": "Direct MCQ",
            "question": {
                "en": "Against whom can the Writ of Habeas Corpus ('To have the body of') be issued by the Supreme Court or High Courts?",
                "ta": "ஆட்கொணர் நீதிப் பேராணை (Habeas Corpus) உச்ச நீதிமன்றம் அல்லது உயர் நீதிமன்றங்களால் யாருக்கு எதிராக வெளியிடப்பட முடியும்?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "Both Public Authorities and Private Individuals",
                    "ta": "அரசு அதிகார அமைப்புகள் மற்றும் தனியார் தனிநபர்கள் ஆகிய இருவருக்கு எதிராகவும்"
                },
                {
                    "id": "B",
                    "en": "Public Authorities only",
                    "ta": "அரசு அதிகார அமைப்புகளுக்கு எதிராக மட்டுமே"
                },
                {
                    "id": "C",
                    "en": "Private Individuals only",
                    "ta": "தனியார் தனிநபர்களுக்கு எதிராக மட்டுமே"
                },
                {
                    "id": "D",
                    "en": "Judicial Officers and Magistrates only",
                    "ta": "நீதித்துறை அதிகாரிகள் மற்றும் நீதிபதிகளுக்கு எதிராக மட்டுமே"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "Habeas Corpus can be issued against BOTH public authorities and private individuals who illegally detain a person. It is a bulwark of individual liberty against arbitrary detention.",
                "ta": "ஆட்கொணர் பேராணை ஒரு நபரைச் சட்டவிரோதமாகக் காவலில் வைக்கும் அரசு அதிகாரிகள் மற்றும் தனியார் தனிநபர்கள் ஆகிய இருவருக்கு எதிராகவும் வெளியிடப்படலாம்."
            },
            "why_not_others": {
                "A": {"en": "Correct. Habeas Corpus is available against both public state authorities and private actors.", "ta": "சரி. ஆட்கொணர் பேராணை அரசு மற்றும் தனியார் இருவருக்கு எதிராகவும் கிடைக்கும்."},
                "B": {"en": "Incorrect. Mandamus is public only, but Habeas Corpus extends to private individuals.", "ta": "தவறு. கட்டளையிடும் பேராணை மட்டுமே அரசு சார்ந்ததற்கு உரியது."},
                "C": {"en": "Incorrect. It applies to public authorities as well.", "ta": "தவறு. அரசு அதிகாரிகளுக்கும் பொருந்தும்."},
                "D": {"en": "Incorrect. It is not restricted to judicial officers.", "ta": "தவறு. நீதித்துறை அதிகாரிகளுக்கு மட்டும் கட்டுப்பட்டதல்ல."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: Habeas Corpus CANNOT be issued where: (1) Detention is lawful, (2) Proceeding is for contempt of court or legislature, (3) Detention is by competent court, (4) Detention is outside court jurisdiction.",
                "ta": "TNPSC குறிப்பு: ஆட்கொணர் பேராணை பின்வருபவற்றிற்கு வராது: (1) காவல் சட்டப்பூர்வமானது, (2) நீதிமன்ற/சட்டமன்ற அவமதிப்பு வழக்கு, (3) தகுதியான நீதிமன்றக் காவல், (4) எல்லைக்கு வெளியே உள்ள காவல்."
            },
            "revision_fact": {
                "en": "Sunil Batra v. Delhi Administration (1980) extended Habeas Corpus to protect prisoners from inhuman treatment inside jail.",
                "ta": "சுனில் பத்ரா வழக்கில் (1980) சிறைக்குள் நடக்கும் மனிதத்தன்மையற்ற நடத்தையிலிருந்து சிறைவாசிகளைப் பாதுகாக்க ஆட்கொணர் பேராணை நீட்டிக்கப்பட்டது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Remember",
            "estimated_time_sec": 35,
            "pyq_similarity": "High",
            "tags": ["Polity", "Writs", "Habeas Corpus", "Grand Test"]
        },

        # Q93: Conceptual MCQ - Fundamental Rights vs Fundamental Duties
        {
            "id": "FR_GT_093",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Medium",
            "question_type": "Conceptual MCQ",
            "question": {
                "en": "Which of the following correctly describes the constitutional relationship between Fundamental Rights (Part III) and Fundamental Duties (Part IV-A)?",
                "ta": "அடிப்படை உரிமைகளுக்கும் (பகுதி III) அடிப்படைக்கடமைகளுக்கும் (பகுதி IV-A) இடையிலான அரசியலமைப்பு உறவை பின்வருவனவற்றுள் எது சரியாக விவரிக்கிறது?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "Rights and Duties are correlative and inseparable; enjoyment of rights requires fulfillment of duties to maintain social order",
                    "ta": "உரிமைகளும் கடமைகளும் ஒன்றுக்கொன்று தொடர்புடையவை மற்றும் பிரிக்க முடியாதவை; சமூக ஒழுங்கைப் பேண உரிமைகளை அனுபவிப்பது கடமைகளை நிறைவேற்றுவதைக் கோருகிறது"
                },
                {
                    "id": "B",
                    "en": "Fundamental Duties supersede Fundamental Rights under all circumstances",
                    "ta": "அனைத்துச் சூழ்நிலைகளிலும் அடிப்படைக் கடமைகள் அடிப்படை உரிமைகளை மிஞ்சுகின்றன"
                },
                {
                    "id": "C",
                    "en": "Fundamental Duties are legally enforceable by writs under Article 32 just like Fundamental Rights",
                    "ta": "அடிப்படை உரிமைகளைப் போலவே அடிப்படைக் கடமைகளும் பிரிவு 32-ன் கீழ் பேராணைகள் மூலம் சட்டப்பூர்வமாக அமல்படுத்தப்படக் கூடியவை"
                },
                {
                    "id": "D",
                    "en": "Fundamental Rights apply only to citizens, whereas Fundamental Duties apply to all foreigners in India",
                    "ta": "அடிப்படை உரிமைகள் குடிமக்களுக்கு மட்டுமே பொருந்தும், ஆனால் அடிப்படைக் கடமைகள் இந்தியாவில் உள்ள அனைத்து வெளிநாட்டினருக்கும் பொருந்தும்"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "Rights and duties are correlative. In AIIMS Students Union v. AIIMS (2002), SC held that Fundamental Duties under Art 51A, though non-justiciable directly, must be used to interpret constitutional statutes and balance Fundamental Rights.",
                "ta": "உரிமைகளும் கடமைகளும் ஒன்றுக்கொன்று தொடர்புடையவை. AIIMS மாணவர்கள் சங்க வழக்கில் (2002) பிரிவு 51A அடிப்படைக் கடமைகள் அரசியலமைப்புச் சட்டங்களை விளக்கவும் உரிமைகளைச் சமநிலைப்படுத்தவும் பயன்பட வேண்டும் எனப்பட்டது."
            },
            "why_not_others": {
                "A": {"en": "Correct. Rights and duties are inalienable correlative concepts in constitutional law.", "ta": "சரி. உரிமைகளும் கடமைகளும் அரசியலமைப்புச் சட்டத்தில் தொடர்புள்ள கருத்துக்கள்."},
                "B": {"en": "Incorrect. Duties do not supersede Rights.", "ta": "தவறு. கடமைகள் உரிமைகளை மிஞ்சாது."},
                "C": {"en": "Incorrect. Fundamental Duties are non-justiciable and cannot be enforced directly under Art 32.", "ta": "தவறு. அடிப்படைக் கடமைகளை 32-ன் கீழ் நேரடியாக அமல்படுத்த முடியாது."},
                "D": {"en": "Incorrect. Fundamental Duties under Art 51A apply ONLY to citizens of India.", "ta": "தவறு. 51A அடிப்படைக் கடமைகள் இந்தியக் குடிமக்களுக்கு மட்டுமே பொருந்தும்."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: Fundamental Duties were added to the Constitution by the 42nd Amendment Act 1976 on the recommendation of the Swaran Singh Committee. 11th duty (51A(k) parent's duty for education) was added by 86th Amendment Act 2002.",
                "ta": "TNPSC குறிப்பு: 42-வது திருத்தச் சட்டம் 1976 ஸ்வரன் சிங் குழுவின் பரிந்துரையால் அடிப்படைக் கடமைகளை இணைத்தது. 11-வது கடமை (51A(k)) 86-வது திருத்தச் சட்டம் 2002 மூலம் சேர்க்கப்பட்டது."
            },
            "revision_fact": {
                "en": "Verma Committee (1999) identified existing legal provisions for enforcement of certain Fundamental Duties (e.g. Prevention of Insults to National Honour Act 1971).",
                "ta": "வர்மா குழு (1999) சில அடிப்படைக் கடமைகளை அமல்படுத்துவதற்கான நடைமுறையிலுள்ள சட்டங்களை அடையாளம் கண்டது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Understand",
            "estimated_time_sec": 45,
            "pyq_similarity": "High",
            "tags": ["Polity", "FR vs FD", "Article 51A", "Swaran Singh", "Grand Test"]
        },

        # Q94: Statement-Based - Landmark Case Ratio Decidendi
        {
            "id": "FR_GT_094",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Hard",
            "question_type": "Statement-Based",
            "question": {
                "en": "Match the landmark judgments with their correct constitutional holdings:\n1. Romesh Thappar v. State of Madras (1950) -> Freedom of speech includes freedom of circulation of newspapers.\n2. Kharak Singh v. State of UP (1963) -> Domiciliary visits by police at night violate personal liberty under Article 21.\n3. E.P. Royappa v. State of Tamil Nadu (1974) -> Equality is a dynamic concept and arbitrariness is antithetical to Article 14.\nWhich of the matches given above are correct?",
                "ta": "முக்கியத் தீர்ப்புகளை அவற்றின் சரியான அரசியலமைப்பு விதிகளுடன் பொருத்துக:\n1. ரமேஷ் தாப்பர் எதிர் மதராஸ் மாநிலம் (1950) -> பேச்சுரிமையில் செய்தித்தாளை விநியோகிக்கும் சுதந்திரமும் அடங்கும்.\n2. கரக் சிங் எதிர் உ.பி அரசு (1963) -> இரவில் காவல்துறை மேற்கொள்ளும் வீட்டுச் சோதனைகள் பிரிவு 21-ன் கீழ் தனிநபர் சுதந்திரத்தை மீறுகின்றன.\n3. ஈ.பி. ராயப்பா எதிர் தமிழ்நாடு அரசு (1974) -> சமத்துவம் ஒரு துடிப்பான கருத்து, தன்னிச்சையான தன்மை பிரிவு 14-க்கு எதிரானது.\nமேற்கூறிய பொருத்தங்களில் எவை சரியானவை?"
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
                "en": "All three matches are correct. Romesh Thappar (1950) established freedom of circulation as part of free press. Kharak Singh (1963) struck down police night visits (domiciliary surveillance) under UP Regulations as violating Art 21. E.P. Royappa (1974) established arbitrariness test under Art 14.",
                "ta": "மூன்று பொருத்தங்களும் சரியானவை. ரமேஷ் தாப்பர் (1950) விநியோக சுதந்திரத்தை பத்திரிகை சுதந்திரமாக்கியது. கரக் சிங் (1963) இரவுக் காவல் சோதனையைப் பிரிவு 21 மீறல் என்றது. ராயப்பா (1974) தன்னிச்சையான சோதனையை நிறுவியது."
            },
            "why_not_others": {
                "A": {"en": "Incorrect because match 3 is also correct.", "ta": "தவறு, ஏனெனில் பொருத்தம் 3-ம் சரியானது."},
                "B": {"en": "Incorrect because match 1 is also correct.", "ta": "தவறு, ஏனெனில் பொருத்தம் 1-ம் சரியானது."},
                "C": {"en": "Incorrect because match 2 is also correct.", "ta": "தவறு, ஏனெனில் பொருத்தம் 2-ம் சரியானது."},
                "D": {"en": "Correct. Matches 1, 2 and 3 are all factually true.", "ta": "சரி. பொருத்தங்கள் 1, 2 மற்றும் 3 அனைத்தும் சரியானவை."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: Romesh Thappar case (1950) led to the 1st Constitutional Amendment Act 1951 adding 'Public Order' as a ground of restriction under Article 19(2).",
                "ta": "TNPSC குறிப்பு: ரமேஷ் தாப்பர் வழக்கு (1950) 1-வது திருத்தச் சட்டம் 1951 மூலம் 19(2)-ல் 'பொது ஒழுங்கு' என்ற கட்டுப்பாட்டுச் சொல்லைச் சேர்க்க வழிவகுத்தது."
            },
            "revision_fact": {
                "en": "Kharak Singh judgment held that 'life' in Article 21 means something more than mere animal existence.",
                "ta": "கரக் சிங் தீர்ப்பு பிரிவு 21-ல் 'வாழ்வு' என்பது வெறும் மிருகத்தனமான வாழ்வை விட மேலானது எனக் கூறியது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Analyze",
            "estimated_time_sec": 60,
            "pyq_similarity": "High",
            "tags": ["Polity", "Landmark Cases", "Romesh Thappar", "Kharak Singh", "Royappa", "Grand Test"]
        },

        # Q95: Direct MCQ - Article 32 Supreme Court Power
        {
            "id": "FR_GT_095",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Easy",
            "question_type": "Direct MCQ",
            "question": {
                "en": "Under Article 32(3), who can empower any other court (e.g. Subordinate Courts) to exercise within its local limits the power to issue writs for the enforcement of Fundamental Rights?",
                "ta": "அடிப்படை உரிமைகளை அமல்படுத்துவதற்கான பேராணைகளை வெளியிடும் அதிகாரத்தைத் தனது உள்ளூர் எல்லைக்குள் பயன்படுத்தப் பிற நீதிமன்றங்களுக்குப் (எ.கா. கீழ் நீதிமன்றங்கள்) பிரிவு 32(3)-ன் கீழ் அதிகாரம் அளிக்கக்கூடியவர் யார்?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "Parliament of India by law",
                    "ta": "சட்டம் மூலம் இந்திய நாடாளுமன்றம்"
                },
                {
                    "id": "B",
                    "en": "Chief Justice of India independently",
                    "ta": "சுயாதீனமாக இந்தியத் தலைமை நீதிபதி"
                },
                {
                    "id": "C",
                    "en": "State Governor in consultation with High Court",
                    "ta": "உயர் நீதிமன்றத்தைக் கலந்தாலோசித்து மாநில ஆளுநர்"
                },
                {
                    "id": "D",
                    "en": "Bar Council of India",
                    "ta": "இந்திய வழக்கறிஞர் மன்றம்"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "Under Article 32(3), Parliament may by law empower any other court to exercise within the local limits of its jurisdiction all or any of the powers exercisable by the Supreme Court under Article 32(2), without prejudice to Supreme Court powers.",
                "ta": "பிரிவு 32(3)-ன் கீழ், உச்ச நீதிமன்ற அதிகாரத்திற்குப் பாதகமின்றிப் பேராணைகளை வெளியிடும் அதிகாரத்தைப் பிற நீதிமன்றங்களுக்கும் வழங்க நாடாளுமன்றம் சட்டம் மூலம் அதிகாரம் அளிக்க முடியும்."
            },
            "why_not_others": {
                "A": {"en": "Correct. Parliament alone can empower subordinate courts under Art 32(3).", "ta": "சரி. பிரிவு 32(3)-ன் கீழ் நாடாளுமன்றம் மட்டுமே கீழ் நீதிமன்றங்களுக்கு அதிகாரம் அளிக்க முடியும்."},
                "B": {"en": "Incorrect. CJI cannot empower courts without Parliamentary legislation.", "ta": "தவறு. நாடாளுமன்றச் சட்டமின்றி CJI அதிகாரம் அளிக்க முடியாது."},
                "C": {"en": "Incorrect. Governor has no power under Art 32(3).", "ta": "தவறு. ஆளுநருக்கு அதிகாரம் இல்லை."},
                "D": {"en": "Incorrect. Bar Council is a professional body.", "ta": "தவறு. பார் கவுன்சில் ஒரு தொழில்சார் அமைப்பு."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: Has Parliament enacted any law under Art 32(3) empowering lower courts to issue writs? NO. So far, ONLY the Supreme Court (Art 32) and High Courts (Art 226) can issue writs in India.",
                "ta": "TNPSC குறிப்பு: கீழ் நீதிமன்றங்களுக்குப் பேராணை அதிகாரம் அளித்துப் பாராளுமன்றம் சட்டம் இயற்றியுள்ளதா? இல்லை. இதுவரை உச்ச நீதிமன்றம் (32) மற்றும் உயர் நீதிமன்றங்கள் (226) மட்டுமே பேராணை பிறப்பிக்க முடியும்."
            },
            "revision_fact": {
                "en": "Before 1950, only High Courts of Calcutta, Bombay and Madras possessed writ jurisdiction in India.",
                "ta": "1950-க்கு முன் கல்கத்தா, பம்பாய், மெட்ராஸ் உயர் நீதிமன்றங்களுக்கு மட்டுமே பேராணை அதிகாரம் இருந்தது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Remember",
            "estimated_time_sec": 35,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 32(3)", "Subordinate Courts Writs", "Grand Test"]
        },

        # Q96: Conceptual MCQ - Prohibition vs Certiorari Distinction
        {
            "id": "FR_GT_096",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Medium",
            "question_type": "Conceptual MCQ",
            "question": {
                "en": "What is the primary operational difference between the Writ of Prohibition and the Writ of Certiorari?",
                "ta": "தடுத்துநிறுத்தும் பேராணைக்கும் (Prohibition) சான்றளிப்பு பேராணைக்கும் (Certiorari) இடையிலான முதன்மையான செயல்பாட்டு வேறுபாடு என்ன?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "Prohibition is issued while proceedings are pending to prevent excess of jurisdiction, whereas Certiorari is issued after an order is passed to quash the illegal decision",
                    "ta": "அதிகார வரம்பு மீறலைத் தடுக்க வழக்கு நிலுவையில் உள்ள போது தடுத்துநிறுத்தும் பேராணை பிறப்பிக்கப்படுகிறது, அதேவேளையில் சட்டவிரோத முடிவை ரத்து செய்ய உத்தரவு வந்த பிறகு சான்றளிப்பு பேராணை பிறப்பிக்கப்படுகிறது"
                },
                {
                    "id": "B",
                    "en": "Prohibition applies to private individuals, whereas Certiorari applies only to the President",
                    "ta": "தடுத்துநிறுத்தும் பேராணை தனியார் தனிநபர்களுக்குப் பொருந்தும், ஆனால் சான்றளிப்பு பேராணை குடியரசுத் தலைவருக்கு மட்டுமே பொருந்தும்"
                },
                {
                    "id": "C",
                    "en": "Prohibition can be issued by District Courts, whereas Certiorari can be issued only by Parliament",
                    "ta": "தடுத்துநிறுத்தும் பேராணையை மாவட்ட நீதிமன்றங்கள் பிறப்பிக்கலாம், ஆனால் சான்றளிப்பு பேராணையை நாடாளுமன்றம் மட்டுமே பிறப்பிக்க முடியும்"
                },
                {
                    "id": "D",
                    "en": "Prohibition is a criminal remedy, whereas Certiorari is a civil contract remedy",
                    "ta": "தடுத்துநிறுத்தும் பேராணை ஒரு குற்றவியல் பரிகாரம், ஆனால் சான்றளிப்பு பேராணை ஒரு உரிமையியல் ஒப்பந்தப் பரிகாரம்"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "Prohibition is purely PREVENTIVE (issued during trial to stop lower court from exceeding jurisdiction). Certiorari is both PREVENTIVE and CURATIVE (issued after order is delivered to quash it and transfer case to higher court).",
                "ta": "தடுத்துநிறுத்தும் பேராணை முற்றிலும் தடுக்கும் தன்மையுடையது (விசாரணை நிலுவையில் உள்ள போது). சான்றளிப்பு பேராணை தடுக்கும் மற்றும் குணப்படுத்தும் இரு தன்மைகளையும் கொண்டது (உத்தரவு வந்த பின் ரத்து செய்ய)."
            },
            "why_not_others": {
                "A": {"en": "Correct. Prohibition operates during pendency (preventive); Certiorari operates post-decision (curative).", "ta": "சரி. தடுத்துநிறுத்தும் பேராணை வழக்கு நிலுவையில் உள்ளபோதும், சான்றளிப்பு பேராணை முடிவிற்குப் பின்பும் செயல்படும்."},
                "B": {"en": "Incorrect. Neither applies to private individuals or President.", "ta": "தவறு. இரண்டும் தனியாருக்குப் பொருந்தாது."},
                "C": {"en": "Incorrect. Both are issued by SC/HC.", "ta": "தவறு. இரண்டும் SC/HC மூலம் பிறப்பிக்கப்படும்."},
                "D": {"en": "Incorrect. Both are public constitutional writ remedies.", "ta": "தவறு. இரண்டும் பொது அரசியலமைப்புப் பரிகாரங்கள்."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: Remember the mnemonic: Prohibition = 'Prevention is better than cure' (stops trial before judgment). Certiorari = 'Cure after disease' (quashes judgment after delivery).",
                "ta": "TNPSC குறிப்பு: நினைவுச் சூத்திரம்: தடுத்துநிறுத்தும் பேராணை = 'வரும் முன் காத்தல்' (தீர்ப்பிற்கு முன் தடுத்தல்). சான்றளிப்பு பேராணை = 'வந்த பின் குணப்படுத்தல்' (தீர்ப்பை ரத்து செய்தல்)."
            },
            "revision_fact": {
                "en": "In Hari Vishnu Kamath v. Ahmad Ishaque (1955), SC laid down principles governing Certiorari for quashing tribunal orders.",
                "ta": "ஹரி விஷ்ணு காமத் வழக்கில் (1955) தீர்ப்பாய உத்தரவுகளை ரத்து செய்ய சான்றளிப்பு பேராணைக்கான விதிகள் வகுக்கப்பட்டன."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Understand",
            "estimated_time_sec": 45,
            "pyq_similarity": "High",
            "tags": ["Polity", "Prohibition", "Certiorari", "Writ Comparison", "Grand Test"]
        },

        # Q97: Statement-Based - Basic Structure Evolution & Major Cases
        {
            "id": "FR_GT_097",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Hard",
            "question_type": "Statement-Based",
            "question": {
                "en": "Consider the following statements regarding the addition of features to the Basic Structure Doctrine:\n1. Judicial Review was declared part of Basic Structure in Kesavananda Bharati (1973), Indira Nehru Gandhi (1975), and L. Chandra Kumar (1997).\n2. Harmony and Balance between Part III and Part IV was declared part of Basic Structure in Minerva Mills (1980).\n3. Free and Fair Elections was declared part of Basic Structure in Indira Nehru Gandhi v. Raj Narain (1975).\nWhich of the statements given above are correct?",
                "ta": "அடிப்படை அமைப்புக் கோட்பாட்டில் அம்சங்கள் சேர்க்கப்பட்டது பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. கேசவாநந்த பாரதி (1973), இந்திரா காந்தி (1975) மற்றும் எல். சந்திரகுமார் (1997) வழக்குகளில் 'நீதித்துறை மறுஆய்வு' அடிப்படை அமைப்பின் பகுதி என அறிவிக்கப்பட்டது.\n2. பகுதி III மற்றும் பகுதி IV இடையிலான 'இணக்கம் மற்றும் சமநிலை' மினர்வா மில்ஸ் (1980) வழக்கில் அடிப்படை அமைப்பின் பகுதி என அறிவிக்கப்பட்டது.\n3. 'சுதந்திரமான மற்றும் நேர்மையான தேர்தல்கள்' இந்திரா நேரு காந்தி வழக்கில் (1975) அடிப்படை அமைப்பின் பகுதி என அறிவிக்கப்பட்டது.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?"
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
                "en": "All three statements are correct. Judicial review, harmony between Part III & IV, and free & fair elections were established as Basic Structure in the respective landmark cases.",
                "ta": "மூன்று கூற்றுகளும் சரியானவை. நீதித்துறை மறுஆய்வு, பகுதி III & IV இணக்கம், சுதந்திரமான தேர்தல் ஆகியவை குறிப்பிட்ட வழக்குகளில் அடிப்படை அமைப்பாக அறிவிக்கப்பட்டன."
            },
            "why_not_others": {
                "A": {"en": "Incorrect because statement 3 is also correct.", "ta": "தவறு, ஏனெனில் கூற்று 3-ம் சரியானது."},
                "B": {"en": "Incorrect because statement 1 is also correct.", "ta": "தவறு, ஏனெனில் கூற்று 1-ம் சரியானது."},
                "C": {"en": "Incorrect because statement 2 is also correct.", "ta": "தவறு, ஏனெனில் கூற்று 2-ம் சரியானது."},
                "D": {"en": "Correct. Statements 1, 2 and 3 are all factually true.", "ta": "சரி. கூற்றுகள் 1, 2 மற்றும் 3 அனைத்தும் சரியானவை."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: In S.R. Bommai v. Union of India (1994), Secularism and Federalism were declared essential features of the Basic Structure of the Constitution.",
                "ta": "TNPSC குறிப்பு: எஸ்.ஆர். பொம்மை வழக்கில் (1994) மதச்சார்பின்மை மற்றும் கூட்டாட்சி தத்துவம் ஆகியவை அடிப்படை அமைப்பின் முக்கிய அம்சங்களாக அறிவிக்கப்பட்டன."
            },
            "revision_fact": {
                "en": "Kihoto Hollohan v. Zachillhu (1992) declared that democracy and free & fair elections are basic structure elements while upholding 52nd Amendment Anti-Defection law.",
                "ta": "கிஹோட்டோ ஹோலோஹான் வழக்கில் (1992) 52-வது திருத்தக் கட்சித் தாவல் தடையைச் சரிபார்த்து ஜனநாயகம் அடிப்படை அமைப்பு எனப்பட்டது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Analyze",
            "estimated_time_sec": 60,
            "pyq_similarity": "High",
            "tags": ["Polity", "Basic Structure Features", "SR Bommai", "Minerva Mills", "Grand Test"]
        },

        # Q98: Direct MCQ - Fundamental Right Suspension Conditions Art 358
        {
            "id": "FR_GT_098",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Easy",
            "question_type": "Direct MCQ",
            "question": {
                "en": "Under Article 358 of the Constitution, the six fundamental freedoms under Article 19 are automatically suspended ONLY when a National Emergency is proclaimed on which ground?",
                "ta": "அரசியலமைப்பின் 358-வது பிரிவின் கீழ், எந்த அடிப்படையில் தேசிய அவசரநிலை அறிவிக்கப்படும் போது மட்டுமே பிரிவு 19-ன் கீழ் உள்ள ஆறு அடிப்படை சுதந்திரங்கள் தானாகவே இடைநிறுத்தப்படுகின்றன?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "War or External Aggression",
                    "ta": "போர் அல்லது வெளிநாட்டு ஆக்கிரமிப்பு"
                },
                {
                    "id": "B",
                    "en": "Armed Rebellion within India",
                    "ta": "இந்தியாவிற்குள் ஆயுதமேந்திய கிளர்ச்சி"
                },
                {
                    "id": "C",
                    "en": "Financial Instability under Article 360",
                    "ta": "பிரிவு 360-ன் கீழ் நிதி சீர்குலைவு"
                },
                {
                    "id": "D",
                    "en": "Failure of Constitutional Machinery in a State under Article 356",
                    "ta": "பிரிவு 356-ன் கீழ் மாநில அரசியலமைப்பு முடக்கம்"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "44th Amendment Act 1978 inserted a proviso to Article 358 stating that Article 19 is automatically suspended ONLY when Emergency is proclaimed on grounds of War or External Aggression (External Emergency). It is NOT suspended when Emergency is declared on ground of Armed Rebellion (Internal Emergency).",
                "ta": "44-வது திருத்தச் சட்டம் 1978 பிரிவு 358-ல் நிபந்தனையை இணைத்தது. இதன்படி போர் அல்லது வெளிநாட்டு ஆக்கிரமிப்பு (வெளிப்புற அவசரநிலை) அடிப்படையில் அவசரநிலை அறிவிக்கப்படும் போது மட்டுமே பிரிவு 19 தானாக இடைநிறுத்தப்படும்."
            },
            "why_not_others": {
                "A": {"en": "Correct. External Emergency (War/External Aggression) triggers automatic suspension of Art 19 under 358.", "ta": "சரி. வெளிப்புற அவசரநிலை மட்டுமே பிரிவு 358-ன் கீழ் 19-ஐத் தானாக இடைநிறுத்தும்."},
                "B": {"en": "Incorrect. Armed Rebellion (Internal Emergency) does NOT suspend Art 19 under Art 358.", "ta": "தவறு. ஆயுதமேந்திய கிளர்ச்சி பிரிவு 358-ன் கீழ் 19-ஐ இடைநிறுத்தாது."},
                "C": {"en": "Incorrect. Financial Emergency does not suspend Art 19.", "ta": "தவறு. நிதி அவசரநிலை 19-ஐ இடைநிறுத்தாது."},
                "D": {"en": "Incorrect. President's Rule does not suspend Art 19.", "ta": "தவறு. குடியரசுத் தலைவர் ஆட்சி 19-ஐ இடைநிறுத்தாது."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: Difference between Art 358 & Art 359 regarding duration: Laws made under Art 358 protection cease to have effect as soon as Emergency expires. Laws protected under Art 359 cease when Presidential Order expires.",
                "ta": "TNPSC குறிப்பு: 358-ன் கீழ் இயற்றப்படும் சட்டங்கள் அவசரநிலை முடிந்தவுடன் காலாவதியாகும். 359-ன் கீழ் சட்டங்கள் குடியரசுத் தலைவர் உத்தரவு முடிந்தவுடன் காலாவதியாகும்."
            },
            "revision_fact": {
                "en": "Before 44th Amendment 1978, Article 19 was automatically suspended during Internal Emergency as well.",
                "ta": "44-வது திருத்தத்திற்கு முன் உள்நாட்டு அவசரநிலையின் போதும் பிரிவு 19 தானாகவே இடைநிறுத்தப்பட்டது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Remember",
            "estimated_time_sec": 35,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 358", "Article 19 Suspension", "External Emergency", "Grand Test"]
        },

        # Q99: Conceptual MCQ - Public Interest Litigation (PIL) and Article 32
        {
            "id": "FR_GT_099",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Medium",
            "question_type": "Conceptual MCQ",
            "question": {
                "en": "Which of the following is NOT a permissible subject matter for filing a Public Interest Litigation (PIL) under Article 32 in the Supreme Court?",
                "ta": "உச்ச நீதிமன்றத்தில் பிரிவு 32-ன் கீழ் பொதுநல வழக்கு (PIL) தாக்கல் செய்வதற்கு அனுமதிக்கப்பட்ட பொருள் அல்லாதது எது?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "Landlord-tenant disputes and private contractual claims between individuals",
                    "ta": "வீட்டு உரிமையாளர்-வாடகைதாரர் தகராறுகள் மற்றும் தனிநபர்களுக்கிடையேயான தனியார் ஒப்பந்தக் கோரிக்கைகள்"
                },
                {
                    "id": "B",
                    "en": "Matters relating to bonded labour and exploitation of helpless workers",
                    "ta": "கொத்தடிமை வேலை மற்றும் ஆதரவற்ற தொழிலாளர்களின் சுரண்டல் தொடர்பான விவகாரங்கள்"
                },
                {
                    "id": "C",
                    "en": "Environmental pollution and protection of ecology/wildlife",
                    "ta": "சுற்றுச்சூழல் மாசுபாடு மற்றும் சூழலியல்/வனவிலங்கு பாதுகாப்பு"
                },
                {
                    "id": "D",
                    "en": "Custodial violence, illegal detention, and police atrocities",
                    "ta": "காவல் மரணம்/சித்திரவதை, சட்டவிரோதக் காவல் மற்றும் காவல்துறையின் அத்துமீறல்கள்"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "Under Supreme Court Guidelines for PIL (1988/2003), private landlord-tenant disputes, service matters, admission to educational institutions, and private contractual disputes are NOT entertained as PIL. PIL is meant for public injury, vulnerable groups, bonded labor, environment, and state atrocities.",
                "ta": "உச்ச நீதிமன்ற PIL வழிகாட்டுதல்களின்படி, தனியார் நில உரிமையாளர்-வாடகைதாரர் தகராறுகள், தனியார் ஒப்பந்த வழக்குகள் PIL ஆக ஏற்றுக்கொள்ளப்பட மாட்டாது."
            },
            "why_not_others": {
                "A": {"en": "Correct. Private landlord-tenant disputes are excluded from PIL scope.", "ta": "சரி. தனியார் வாடகைதாரர் தகராறுகள் PIL வரம்பிலிருந்து விலக்கப்பட்டுள்ளன."},
                "B": {"en": "Incorrect. Bonded labour is a classic PIL category.", "ta": "தவறு. கொத்தடிமை வேலை PIL-ல் ஏற்றுக்கொள்ளப்படும்."},
                "C": {"en": "Incorrect. Environmental issues are accepted as PIL.", "ta": "தவறு. சுற்றுச்சூழல் பிரச்சினைகள் PIL-ல் ஏற்றுக்கொள்ளப்படும்."},
                "D": {"en": "Incorrect. Police atrocities are accepted as PIL.", "ta": "தவறு. காவல் அத்துமீறல்கள் PIL-ல் ஏற்றுக்கொள்ளப்படும்."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: Justice P.N. Bhagwati and Justice V.R. Krishna Iyer are recognized as the pioneers of Judicial Activism and PIL in India.",
                "ta": "TNPSC குறிப்பு: நீதிபதி பி.என். பகவதி மற்றும் நீதிபதி வி.ஆர். கிருஷ்ணய்யர் ஆகியோர் இந்தியாவில் நீதித்துறை விழிப்புணர்வு (Judicial Activism) மற்றும் PIL-ன் முன்னோடிகளாவர்."
            },
            "revision_fact": {
                "en": "Epistolary Jurisdiction refers to the power of the Supreme Court to convert letters or postcards written by disadvantaged citizens into PIL writ petitions.",
                "ta": "கடிதங்கள் அல்லது அஞ்சல் அட்டைகளை PIL பேராணை மனுக்களாக மாற்றும் உச்ச நீதிமன்ற அதிகாரத்திற்கு Epistolary Jurisdiction என்று பெயர்."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Understand",
            "estimated_time_sec": 45,
            "pyq_similarity": "High",
            "tags": ["Polity", "PIL", "Article 32", "Public Interest Litigation", "Grand Test"]
        },

        # Q100: Statement-Based - Comprehensive Fundamental Rights Synthesis
        {
            "id": "FR_GT_100",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Hard",
            "question_type": "Statement-Based",
            "question": {
                "en": "Consider the following comprehensive statements regarding Part III of the Constitution of India:\n1. Fundamental Rights are defended and guaranteed by the Supreme Court under Article 32.\n2. Fundamental Rights are not sacrosanct or permanent; Parliament can curtail or repeal them by a Constitutional Amendment Act under Article 368 without altering the Basic Structure.\n3. All Fundamental Rights are directly self-executory and do not require any legislation to give effect to them.\nWhich of the statements given above are correct?",
                "ta": "இந்திய அரசியலமைப்பின் பகுதி III பற்றிய பின்வரும் விரிவான கூற்றுகளைக் கவனியுங்கள்:\n1. அடிப்படை உரிமைகள் பிரிவு 32-ன் கீழ் உச்ச நீதிமன்றத்தால் பாதுகாக்கப்பட்டு உத்தரவாதம் அளிக்கப்படுகின்றன.\n2. அடிப்படை உரிமைகள் மாற்ற முடியாதவை அல்லது நிரந்தரமானவை அல்ல; அடிப்படை அமைப்பை மாற்றாமல் பிரிவு 368-ன் கீழ் அரசியலமைப்புத் திருத்தச் சட்டம் மூலம் நாடாளுமன்றம் அவற்றைக் குறைக்கவோ அல்லது நீக்கவோ முடியும்.\n3. அனைத்து அடிப்படை உரிமைகளும் நேரடியாகத் தாமே செயல்படக் கூடியவை, அவற்றை அமல்படுத்த எந்தச் சட்டமும் தேவையில்லை.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?"
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
                "en": "Statements 1 and 2 are correct. Statement 3 is INCORRECT: Most FRs are directly self-executory, but SOME FRs (like Articles 17, 21A, 23, 24) require parliamentary legislation under Article 35 to enforce offences and prescribe punishments.",
                "ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது: பெரும்பாலான அடிப்படை உரிமைகள் தாமே செயல்படுபவை, ஆனால் சில உரிமைகளுக்கு (பிரிவுகள் 17, 21A, 23, 24) பிரிவு 35-ன் கீழ் நாடாளுமன்றச் சட்டம் தேவைப்படுகிறது."
            },
            "why_not_others": {
                "A": {"en": "Correct. Statements 1 and 2 are true; statement 3 is false because some FRs need enabling law under Art 35.", "ta": "சரி. கூற்றுகள் 1 மற்றும் 2 சரியானவை; சில உரிமைகளுக்கு பிரிவு 35-ன் கீழ் சட்டம் தேவை என்பதால் கூற்று 3 தவறானது."},
                "B": {"en": "Incorrect because statement 3 is false.", "ta": "தவறு, ஏனெனில் கூற்று 3 தவறானது."},
                "C": {"en": "Incorrect because statement 3 is false.", "ta": "தவறு, ஏனெனில் கூற்று 3 தவறானது."},
                "D": {"en": "Incorrect because statement 3 is false.", "ta": "தவறு, ஏனெனில் கூற்று 3 தவறானது."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: Fundamental Rights are negative obligations on the State (most rights prohibit State from doing certain acts), whereas Directive Principles (Part IV) are positive obligations on the State.",
                "ta": "TNPSC குறிப்பு: அடிப்படை உரிமைகள் அரசின் மீதான எதிர்மறைக் கடமைகள் (செயல்களைத் தடுப்பவை), ஆனால் வழிகாட்டு நெறிமுறைகள் அரசின் மீதான நேர்மறைக் கடமைகள்."
            },
            "revision_fact": {
                "en": "Part III of the Indian Constitution is rightly described as the 'Magna Carta of India'.",
                "ta": "இந்திய அரசியலமைப்பின் பகுதி III நியாயமாக 'இந்தியாவின் மகாசாசனம்' (Magna Carta of India) என வர்ணிக்கப்படுகிறது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity", "NCERT Class XI - Indian Constitution at Work"],
            "bloom_level": "Analyze",
            "estimated_time_sec": 60,
            "pyq_similarity": "High",
            "tags": ["Polity", "Fundamental Rights", "Synthesis", "Magna Carta", "Grand Test"]
        }
    ]
    return questions
