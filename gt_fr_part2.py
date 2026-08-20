# gt_fr_part2.py
# Questions 36 to 70: Articles 19 - 24 (Six Freedoms, Reasonable Restrictions, Article 20, Article 21, Article 21A, Article 22, Articles 23-24)

def get_part2_questions():
    questions = [
        # Q36: Direct MCQ - Article 19(1) Freedoms available only to citizens
        {
            "id": "FR_GT_036",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Easy",
            "question_type": "Direct MCQ",
            "question": {
                "en": "The six freedoms guaranteed under Article 19(1) of the Constitution of India are available to which of the following?",
                "ta": "இந்திய அரசியலமைப்பின் 19(1) பிரிவின் கீழ் உத்தரவாதம் அளிக்கப்பட்ட ஆறு சுதந்திரங்கள் பின்வருவனவற்றுள் யாருக்குக் கிடைக்கின்றன?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "Citizens of India only (natural persons)",
                    "ta": "இந்தியக் குடிமக்களுக்கு மட்டுமே (இயற்கையான நபர்கள்)"
                },
                {
                    "id": "B",
                    "en": "All persons residing in India including foreigners",
                    "ta": "வெளிநாட்டினர் உட்பட இந்தியாவில் வசிக்கும் அனைத்து நபர்களுக்கும்"
                },
                {
                    "id": "C",
                    "en": "Foreign corporations and international companies",
                    "ta": "வெளிநாட்டு கார்ப்பரேஷன்கள் மற்றும் சர்வதேச நிறுவனங்களுக்கு"
                },
                {
                    "id": "D",
                    "en": "Statutory legal corporations created under state acts",
                    "ta": "மாநிலச் சட்டங்களின் கீழ் உருவாக்கப்பட்ட சட்டப்பூர்வ கார்ப்பரேஷன்களுக்கு"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "Article 19 rights are available ONLY to citizens of India (natural persons). They are not available to foreigners, non-citizens, or legal entities like companies/corporations (STC v. CTO 1963). However, shareholders can challenge state action affecting company rights through citizen rights.",
                "ta": "பிரிவு 19 உரிமைகள் இந்தியக் குடிமக்களுக்கு மட்டுமே (இயற்கையான நபர்கள்) கிடைக்கின்றன. வெளிநாட்டினர், நிறுவனங்கள் அல்லது கார்ப்பரேஷன்களுக்கு இவை கிடைக்காது (STC வழக்கு 1963)."
            },
            "why_not_others": {
                "A": {"en": "Correct. Article 19 rights are exclusively for citizens of India.", "ta": "சரி. பிரிவு 19 உரிமைகள் இந்தியக் குடிமக்களுக்கு மட்டுமே உரியது."},
                "B": {"en": "Incorrect. Foreigners cannot claim Article 19 freedoms.", "ta": "தவறு. வெளிநாட்டினர் பிரிவு 19 சுதந்திரங்களைக் கோர முடியாது."},
                "C": {"en": "Incorrect. Corporations are not citizens under Article 19.", "ta": "தவறு. கார்ப்பரேஷன்கள் பிரிவு 19-ன் கீழ் குடிமக்கள் அல்ல."},
                "D": {"en": "Incorrect. Statutory corporations do not enjoy Article 19 rights.", "ta": "தவறு. சட்டப்பூர்வ கார்ப்பரேஷன்களுக்கு பிரிவு 19 உரிமைகள் இல்லை."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: Five Articles are available ONLY to citizens: Articles 15, 16, 19, 29, and 30. All other FRs (14, 20, 21, 21A, 22, 23, 24, 25, 26, 27, 28) apply to all persons.",
                "ta": "TNPSC குறிப்பு: 5 பிரிவுகள் குடிமக்களுக்கு மட்டுமே உரியவை: 15, 16, 19, 29, மற்றும் 30. மற்றவை அனைத்து நபர்களுக்கும் பொருந்தும்."
            },
            "revision_fact": {
                "en": "State Trading Corporation of India v. CTO (1963) established that a company registered under Companies Act is not a 'citizen' under Article 19.",
                "ta": "ஸ்டேட் டிரேடிங் கார்ப்பரேஷன் வழக்கில் (1963) நிறுவனச் சட்டத்தின்கீழ் பதிவு செய்யப்பட்ட நிறுவனம் பிரிவு 19-ன் கீழ் 'குடிமகன்' அல்ல எனப்பட்டது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Remember",
            "estimated_time_sec": 35,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 19", "Citizenship", "Grand Test"]
        },

        # Q37: Conceptual MCQ - Grounds of Restriction under Article 19(2)
        {
            "id": "FR_GT_037",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Medium",
            "question_type": "Conceptual MCQ",
            "question": {
                "en": "How many reasonable grounds of restriction are explicitly specified under Article 19(2) to limit Freedom of Speech and Expression under Article 19(1)(a)?",
                "ta": "பிரிவு 19(1)(a)-ன் கீழ் உள்ள பேச்சு மற்றும் வெளிப்பாட்டுச் சுதந்திரத்தைக் கட்டுப்படுத்த பிரிவு 19(2)-ன் கீழ் வெளிப்படையாகக் குறிப்பிடப்பட்டுள்ள நியாயமான கட்டுப்பாட்டு அடிப்படைகள் எத்தனை?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "8 grounds",
                    "ta": "8 அடிப்படைகள்"
                },
                {
                    "id": "B",
                    "en": "5 grounds",
                    "ta": "5 அடிப்படைகள்"
                },
                {
                    "id": "C",
                    "en": "6 grounds",
                    "ta": "6 அடிப்படைகள்"
                },
                {
                    "id": "D",
                    "en": "10 grounds",
                    "ta": "10 அடிப்படைகள்"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "Article 19(2) specifies 8 grounds of restriction: (1) Sovereignty and Integrity of India, (2) Security of the State, (3) Friendly relations with foreign States, (4) Public order, (5) Decency or morality, (6) Contempt of court, (7) Defamation, (8) Incitement to an offence.",
                "ta": "பிரிவு 19(2) 8 கட்டுப்பாட்டு அடிப்படைகளைக் குறிப்பிடுகிறது: (1) இந்தியாவின் இறையாண்மை மற்றும் ஒருமைப்பாடு, (2) அரசின் பாதுகாப்பு, (3) வெளிநாடுகளுடனான நட்புறவு, (4) பொது ஒழுங்கு, (5) கண்ணியம் அல்லது ஒழுக்கம், (6) நீதிமன்ற அவமதிப்பு, (7) அவதூறு, (8) குற்றத்திற்குத் தூண்டுதல்."
            },
            "why_not_others": {
                "A": {"en": "Correct. Exactly 8 grounds are specified in Article 19(2).", "ta": "சரி. பிரிவு 19(2)-ல் சரியாக 8 அடிப்படைகள் உள்ளன."},
                "B": {"en": "Incorrect. 5 grounds is wrong.", "ta": "தவறு. 5 அடிப்படைகள் என்பது தவறானது."},
                "C": {"en": "Incorrect. 6 freedoms exist under 19(1), but 8 grounds under 19(2).", "ta": "தவறு. 19(1)-ல் 6 சுதந்திரங்கள் உள்ளன, ஆனால் 19(2)-ல் 8 கட்டுப்பாடுகள் உள்ளன."},
                "D": {"en": "Incorrect. 10 grounds is wrong.", "ta": "தவறு. 10 அடிப்படைகள் என்பது தவறானது."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: 'Sovereignty and Integrity of India' was added as a ground of restriction under Art 19(2) by the 16th Constitutional Amendment Act 1963.",
                "ta": "TNPSC குறிப்பு: 'இந்தியாவின் இறையாண்மை மற்றும் ஒருமைப்பாடு' என்ற கட்டுப்பாடு 1963-ன் 16-வது திருத்தச் சட்டத்தின் மூலம் 19(2)-ல் சேர்க்கப்பட்டது."
            },
            "revision_fact": {
                "en": "'Public order' and 'Friendly relations with foreign States' were added to Article 19(2) by the 1st Constitutional Amendment Act 1951 following the Romesh Thappar case.",
                "ta": "ரமேஷ் தாப்பர் வழக்கைத் தொடர்ந்து 1-வது திருத்தச் சட்டம் 1951 மூலம் 'பொது ஒழுங்கு' மற்றும் 'வெளிநாடுகளுடனான நட்புறவு' 19(2)-ல் சேர்க்கப்பட்டன."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Understand",
            "estimated_time_sec": 45,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 19(2)", "Reasonable Restrictions", "Grand Test"]
        },

        # Q38: Hard / Analytical - Freedom of Press & Commercial Speech Cases
        {
            "id": "FR_GT_038",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Hard",
            "question_type": "Hard / Analytical",
            "question": {
                "en": "Match the implicitly recognized rights under Article 19(1)(a) with their landmark Supreme Court judgments:\n1. Freedom of Press -> a. Tata Press Ltd. v. MTNL (1995)\n2. Right to Silence (National Anthem) -> b. Romesh Thappar v. State of Madras (1950)\n3. Right to Commercial Speech/Advertisement -> c. Bijoe Emmanuel v. State of Kerala (1986)\n4. Right to Information (voter background) -> d. Union of India v. Association for Democratic Reforms (2002)",
                "ta": "பிரிவு 19(1)(a)-ன் கீழ் மறைமுகமாக அங்கீகரிக்கப்பட்ட உரிமைகளை அவற்றின் முக்கிய உச்ச நீதிமன்றத் தீர்ப்புகளுடன் பொருத்துக:\n1. பத்திரிகை சுதந்திரம் -> a. டாடா பிரஸ் எல்டிடி எதிர் எம்.டி.என்.எல் (1995)\n2. அமைதி காக்கும் உரிமை (தேசிய கீதம்) -> b. ரமேஷ் தாப்பர் எதிர் மதராஸ் மாநிலம் (1950)\n3. வணிகப் பேச்சு/விளம்பர உரிமை -> c. பிஜோய் இம்மானுவேல் எதிர் கேரளா அரசு (1986)\n4. தகவல் அறியும் உரிமை (வேட்பாளர் பின்னணி) -> d. இந்திய யூனியன் எதிர் ஜனநாயக சீர்திருத்தங்களுக்கான சங்கம் (2002)"
            },
            "options": [
                {
                    "id": "A",
                    "en": "1-b, 2-c, 3-a, 4-d",
                    "ta": "1-b, 2-c, 3-a, 4-d"
                },
                {
                    "id": "B",
                    "en": "1-a, 2-c, 3-b, 4-d",
                    "ta": "1-a, 2-c, 3-b, 4-d"
                },
                {
                    "id": "C",
                    "en": "1-b, 2-a, 3-c, 4-d",
                    "ta": "1-b, 2-a, 3-c, 4-d"
                },
                {
                    "id": "D",
                    "en": "1-d, 2-c, 3-a, 4-b",
                    "ta": "1-d, 2-c, 3-a, 4-b"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "Correct match: Freedom of Press -> Romesh Thappar (1950); Right to Silence -> Bijoe Emmanuel (1986); Commercial Speech -> Tata Press (1995); Right to Information -> ADR case (2002).",
                "ta": "சரியான பொருத்தம்: பத்திரிகை சுதந்திரம் -> ரமேஷ் தாப்பர் (1950); அமைதி காக்கும் உரிமை -> பிஜோய் இம்மானுவேல் (1986); வணிக விளம்பரம் -> டாடா பிரஸ் (1995); தகவல் அறியும் உரிமை -> ADR வழக்கு (2002)."
            },
            "why_not_others": {
                "A": {"en": "Correct match: 1-b, 2-c, 3-a, 4-d.", "ta": "சரியான பொருத்தம்: 1-b, 2-c, 3-a, 4-d."},
                "B": {"en": "Incorrect mapping for press freedom and commercial speech.", "ta": "தவறான பொருத்தம்."},
                "C": {"en": "Incorrect mapping for right to silence.", "ta": "தவறான பொருத்தம்."},
                "D": {"en": "Incorrect mapping for press freedom.", "ta": "தவறான பொருத்தம்."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: Sakal Papers v. UOI (1962) held that fixing price and number of pages of a newspaper infringes Freedom of Press under Art 19(1)(a).",
                "ta": "TNPSC குறிப்பு: சகால் பேப்பர்ஸ் வழக்கில் (1962) செய்தித்தாளின் விலை மற்றும் பக்கங்களை நிர்ணயிப்பது 19(1)(a) பத்திரிகை சுதந்திரத்தை மீறுகிறது எனப்பட்டது."
            },
            "revision_fact": {
                "en": "Bijoe Emmanuel case (1986) protected Jehovah's Witness students who respectfully stood up during National Anthem but did not sing.",
                "ta": "பிஜோய் இம்மானுவேல் வழக்கில் (1986) தேசிய கீதத்தின் போது மரியாதையுடன் நின்ற ஆனால் பாடாத யெகோவாவின் சாட்சிகள் மாணவர்கள் பாதுகாக்கப்பட்டனர்."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Analyze",
            "estimated_time_sec": 60,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 19(1)(a)", "Implied Rights", "Grand Test"]
        },

        # Q39: Statement-Based - Article 19 Freedom of Movement & Residence
        {
            "id": "FR_GT_039",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Medium",
            "question_type": "Statement-Based",
            "question": {
                "en": "Consider the following statements regarding freedom of movement under Article 19(1)(d):\n1. Internal movement within the territory of India is guaranteed under Article 19(1)(d).\n2. The right to move OUT of India (go abroad) is protected under Article 21, NOT Article 19(1)(d).\n3. Restrictions on freedom of movement under Article 19(5) can be imposed on grounds of protecting the interests of any Scheduled Tribe.\nWhich of the statements given above are correct?",
                "ta": "பிரிவு 19(1)(d)-ன் கீழ் உள்ள நடமாடும் சுதந்திரம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இந்தியப் பகுதிக்குள் உள்நாட்டு நடமாட்டம் பிரிவு 19(1)(d)-ன் கீழ் உத்தரவாதம் அளிக்கப்படுகிறது.\n2. இந்தியாவை விட்டு வெளியே செல்லும் உரிமை (வெளிநாடு செல்லுதல்) பிரிவு 21-ன் கீழ் பாதுகாக்கப்படுகிறது, பிரிவு 19(1)(d)-ல் அல்ல.\n3. அட்டவணைப்படுத்தப்பட்ட பழங்குடியினரின் நலன்களைப் பாதுகாப்பதற்காகப் பிரிவு 19(5)-ன் கீழ் நடமாட்டச் சுதந்திரத்திற்கு வரம்புகள் விதிக்கப்படலாம்.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?"
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
                "en": "All three statements are correct. Art 19(1)(d) protects right to move freely throughout India (internal movement). Maneka Gandhi case (1978) settled that right to go abroad is part of personal liberty under Art 21. Art 19(5) permits restrictions in general public interest or to protect Scheduled Tribes.",
                "ta": "மூன்று கூற்றுகளும் சரியானவை. பிரிவு 19(1)(d) உள்நாட்டு நடமாட்டத்தைப் பாதுகாக்கிறது. வெளிநாடு செல்லும் உரிமை பிரிவு 21-ன் கீழ் வருகிறது (மேனகா காந்தி வழக்கு 1978). பிரிவு 19(5) பழங்குடியினர் நலனுக்காகக் கட்டுப்பாடுகளை அனுமதிக்கிறது."
            },
            "why_not_others": {
                "A": {"en": "Incorrect because statement 3 is also correct.", "ta": "தவறு, ஏனெனில் கூற்று 3-ம் சரியானது."},
                "B": {"en": "Incorrect because statement 1 is also correct.", "ta": "தவறு, ஏனெனில் கூற்று 1-ம் சரியானது."},
                "C": {"en": "Incorrect because statement 2 is also correct.", "ta": "தவறு, ஏனெனில் கூற்று 2-ம் சரியானது."},
                "D": {"en": "Correct. All statements 1, 2 and 3 are factually accurate.", "ta": "சரி. கூற்றுகள் 1, 2 மற்றும் 3 அனைத்தும் சரியானவை."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Trap: Distinguish clearly: Internal Movement = Art 19(1)(d). Foreign Travel = Art 21. Supreme Court affirmed this distinction in Satwant Singh Sawhney v. Assistant Passport Officer (1967) and Maneka Gandhi (1978).",
                "ta": "TNPSC பொறி: தெளிவான வேறுபாடு: உள்நாட்டு நடமாட்டம் = 19(1)(d). வெளிநாட்டுப் பயணம் = பிரிவு 21. சத்வந்த் சிங் சாவ்னி மற்றும் மேனகா காந்தி வழக்குகளில் இது உறுதி செய்யப்பட்டது."
            },
            "revision_fact": {
                "en": "State of Uttar Pradesh v. Kaushaliya (1964) held that movement of prostitutes can be restricted on grounds of public health and morality under Art 19(5).",
                "ta": "கௌசல்யா வழக்கில் (1964) பொது சுகாதாரம் மற்றும் ஒழுக்கத்தின் அடிப்படையில் விபச்சாரிகளின் நடமாட்டத்தைக் கட்டுப்படுத்தலாம் எனக் கூறப்பட்டது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Analyze",
            "estimated_time_sec": 55,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 19(1)(d)", "Article 21", "Grand Test"]
        },

        # Q40: Direct MCQ - Cooperative Societies 97th Amendment
        {
            "id": "FR_GT_040",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Easy",
            "question_type": "Direct MCQ",
            "question": {
                "en": "Which Constitutional Amendment Act added the word 'co-operative societies' into Article 19(1)(c), thereby making the right to form co-operative societies a Fundamental Right?",
                "ta": "பிரிவு 19(1)(c)-ல் 'கூட்டுறவுச் சங்கங்கள்' என்ற சொல்லைச் சேர்த்து, கூட்டுறவுச் சங்கங்களை அமைக்கும் உரிமையை அடிப்படை உரிமையாக்கிய அரசியலமைப்புத் திருத்தச் சட்டம் எது?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "97th Constitutional Amendment Act, 2011",
                    "ta": "2011-ன் 97-வது அரசியலமைப்புத் திருத்தச் சட்டம்"
                },
                {
                    "id": "B",
                    "en": "91st Constitutional Amendment Act, 2003",
                    "ta": "2003-ன் 91-வது அரசியலமைப்புத் திருத்தச் சட்டம்"
                },
                {
                    "id": "C",
                    "en": "86th Constitutional Amendment Act, 2002",
                    "ta": "2002-ன் 86-வது அரசியலமைப்புத் திருத்தச் சட்டம்"
                },
                {
                    "id": "D",
                    "en": "44th Constitutional Amendment Act, 1978",
                    "ta": "1978-ன் 44-வது அரசியலமைப்புத் திருத்தச் சட்டம்"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "97th Amendment Act 2011 made three changes: (1) Added 'co-operative societies' in Art 19(1)(c), (2) Added Art 43B in DPSP, and (3) Added Part IX-B (Articles 243ZH to 243ZT). Note: In Union of India v. Rajendra N Shah (2021), SC struck down Part IX-B for multi-state co-ops lack of state ratification, but left Art 19(1)(c) amendment intact.",
                "ta": "97-வது திருத்தச் சட்டம் 2011 3 மாற்றங்களைச் செய்தது: (1) 19(1)(c)-ல் கூட்டுறவுச் சங்கங்கள், (2) DPSP-ல் 43B, (3) பகுதி IX-B. ராஜேந்திர என் ஷா வழக்கில் (2021) பகுதி IX-B ரத்து செய்யப்பட்டது, ஆனால் 19(1)(c) திருத்தம் நீடிக்கிறது."
            },
            "why_not_others": {
                "A": {"en": "Correct. 97th Amendment Act 2011 added co-operative societies into Art 19(1)(c).", "ta": "சரி. 97-வது திருத்தச் சட்டம் 2011 கூட்டுறவுச் சங்கங்களை 19(1)(c)-ல் சேர்த்தது."},
                "B": {"en": "Incorrect. 91st Amendment 2003 limited ministry size to 15% and tightened anti-defection.", "ta": "தவறு. 91-வது திருத்தம் 2003 அமைச்சரவை அளவை 15%-ஆகக் கட்டுப்படுத்தியது."},
                "C": {"en": "Incorrect. 86th Amendment 2002 added Art 21A.", "ta": "தவறு. 86-வது திருத்தம் 2002 பிரிவு 21A-வை இணைத்தது."},
                "D": {"en": "Incorrect. 44th Amendment 1978 repealed Art 19(1)(f).", "ta": "தவறு. 44-வது திருத்தம் 1978 பிரிவு 19(1)(f)-ஐ நீக்கியது."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: Article 19(1)(c) covers freedom to form associations, unions, OR co-operative societies. Reasonable restrictions on 19(1)(c) under 19(4) can be imposed on grounds of public order, morality, or sovereignty & integrity of India.",
                "ta": "TNPSC குறிப்பு: 19(1)(c)-ன் கீழ் உள்ள சங்கங்கள் அமைக்கும் உரிமைக்கான கட்டுப்பாட்டு அடிப்படைகள்: பொது ஒழுங்கு, ஒழுக்கம், அல்லது இந்தியாவின் இறையாண்மை மற்றும் ஒருமைப்பாடு (பிரிவு 19(4))."
            },
            "revision_fact": {
                "en": "Right to form association does NOT guarantee the right to achieve the objects for which the association was formed, nor does it guarantee the right to strike (T.K. Rangarajan v. Government of TN 2003).",
                "ta": "சங்கம் அமைக்கும் உரிமை சங்கத்தின் நோக்கங்களை அடைவதற்கான உரிமையையோ அல்லது வேலைநிறுத்தம் செய்யும் உரிமையையோ உத்தரவாதம் செய்யாது (டி.கே. ரங்கராஜன் வழக்கு 2003)."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Remember",
            "estimated_time_sec": 35,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 19(1)(c)", "97th Amendment", "Grand Test"]
        },

        # Q41: Conceptual MCQ - Protection in respect of conviction for offences Art 20
        {
            "id": "FR_GT_041",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Medium",
            "question_type": "Conceptual MCQ",
            "question": {
                "en": "Which of the following protections guaranteed under Article 20 applies ONLY to criminal laws and NOT to civil or tax liabilities?",
                "ta": "பிரிவு 20-ன் கீழ் உத்தரவாதம் அளிக்கப்பட்ட பின்வரும் பாதுகாப்புகளில் எது குற்றவியல் சட்டங்களுக்கு மட்டுமே பொருந்தும், உரிமையியல் அல்லது வரிப் பொறுப்புகளுக்குப் பொருந்தாது?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "Protection against Ex-Post Facto Law under Article 20(1)",
                    "ta": "பிரிவு 20(1)-ன் கீழ் உள்ள பின்னோக்கிய குற்றவியல் சட்டத்திற்கு எதிரான பாதுகாப்பு"
                },
                {
                    "id": "B",
                    "en": "Protection against Double Jeopardy under Article 20(2)",
                    "ta": "பிரிவு 20(2)-ன் கீழ் உள்ள இரட்டைத் தண்டனைக்கு எதிரான பாதுகாப்பு"
                },
                {
                    "id": "C",
                    "en": "Protection against Self-Incrimination under Article 20(3)",
                    "ta": "பிரிவு 20(3)-ன் கீழ் உள்ள தமக்குத் தாமே சாட்சியமளிப்பதற்கு எதிரான பாதுகாப்பு"
                },
                {
                    "id": "D",
                    "en": "All three protections under Article 20 apply equally to civil and criminal laws",
                    "ta": "பிரிவு 20-ன் கீழ் உள்ள மூன்று பாதுகாப்புகளும் உரிமையியல் மற்றும் குற்றவியல் சட்டங்களுக்குச் சமமாகப் பொருந்தும்"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "Article 20(1) (Ex-post facto law prohibition) prohibits enacting retrospective CRIMINAL laws or increasing penalties retrospectively. Parliament CAN enact retrospective CIVIL laws or TAX laws (Hathising Manufacturing Co. v. UOI).",
                "ta": "பிரிவு 20(1) பின்னோக்கிய குற்றவியல் சட்டங்களை இயற்றுவதை மட்டுமே தடை செய்கிறது. நாடாளுமன்றம் பின்னோக்கிய உரிமையியல் அல்லது வரிச் சட்டங்களை இயற்ற முடியும்."
            },
            "why_not_others": {
                "A": {"en": "Correct. Immunity against ex-post facto laws under 20(1) applies exclusively to criminal offences.", "ta": "சரி. பிரிவு 20(1)-ன் கீழ் உள்ள பாதுகாப்பு குற்றவியல் சட்டங்களுக்கு மட்டுமே பொருந்தும்."},
                "B": {"en": "Incorrect. Double jeopardy protects against judicial prosecution, but does not distinguish tax/civil retroactivity.", "ta": "தவறு. இரட்டைத் தண்டனை நீதிமன்றத் தொடரலுக்கு எதிரானது."},
                "C": {"en": "Incorrect. Self-incrimination applies to accused of criminal offence.", "ta": "தவறு. சுய சாட்சிய விலக்கு குற்றஞ்சாட்டப்பட்ட நபருக்கு பொருந்தும்."},
                "D": {"en": "Incorrect. Article 20 protections are specifically targeted at criminal proceedings.", "ta": "தவறு. பிரிவு 20 குற்றவியல் நடவடிக்கைகளைக் குறிவைக்கிறது."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Trap: Ex-post facto protection under 20(1) applies ONLY to conviction or sentence, NOT to trial procedure or preventive detention laws!",
                "ta": "TNPSC பொறி: பிரிவு 20(1)-ன் கீழ் பின்னோக்கிய சட்டப் பாதுகாப்பு தண்டனைக்கு மட்டுமே பொருந்தும், விசாரணை நடைமுறைக்கோ அல்லது தடுப்புக் காவல் சட்டங்களுக்கோ பொருந்தாது!"
            },
            "revision_fact": {
                "en": "Kedar Nath v. State of West Bengal (1953) held that enhancing punishment for an offence retrospectively violates Article 20(1).",
                "ta": "கேதார் நாத் வழக்கில் (1953) ஒரு குற்றத்திற்கான தண்டனையைப் பின்னோக்கி அதிகரிப்பது பிரிவு 20(1)-ஐ மீறுகிறது எனக் கூறப்பட்டது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Understand",
            "estimated_time_sec": 45,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 20(1)", "Ex-Post Facto", "Grand Test"]
        },

        # Q42: Hard / Analytical - Selvi Case Narcoanalysis & Art 20(3)
        {
            "id": "FR_GT_042",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Hard",
            "question_type": "Hard / Analytical",
            "question": {
                "en": "In Selvi v. State of Karnataka (2010), the Supreme Court ruled that compulsory administration of Narcoanalysis, Polygraph test, and Brain Electrical Activation Profile (BEAP) violates which constitutional provisions?",
                "ta": "செல்வி எதிர் கர்நாடக அரசு (2010) வழக்கில், நவாக்கோ அனாலிசிஸ், பாலிகிராஃப் சோதனை மற்றும் மூளை மின் அதிர்வு சுயவிவர சோதனைகளைக் கட்டாயமாக நடத்துவது எந்த அரசியலமைப்புப் பிரிவுகளை மீறுகிறது என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "Article 20(3) (Self-Incrimination) and Article 21 (Right to Privacy & Personal Liberty)",
                    "ta": "பிரிவு 20(3) (சுய சாட்சிய விலக்கு) மற்றும் பிரிவு 21 (தனியுரிமை & தனிநபர் சுதந்திரம்)"
                },
                {
                    "id": "B",
                    "en": "Article 14 (Equality) and Article 19(1)(a) (Freedom of Speech)",
                    "ta": "பிரிவு 14 (சமத்துவம்) மற்றும் பிரிவு 19(1)(a) (பேச்சுரிமை)"
                },
                {
                    "id": "C",
                    "en": "Article 22(1) (Right to Legal Counsel) and Article 23 (Forced Labour)",
                    "ta": "பிரிவு 22(1) (வழக்கறிஞர் ஆலோசனையுரிமை) மற்றும் பிரிவு 23 (கட்டாய வேலை)"
                },
                {
                    "id": "D",
                    "en": "Article 17 (Untouchability) and Article 20(2) (Double Jeopardy)",
                    "ta": "பிரிவு 17 (தீண்டாமை) மற்றும் பிரிவு 20(2) (இரட்டைத் தண்டனை)"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "In Selvi v. State of Karnataka (2010), a 3-judge bench held that non-consensual narcoanalysis, polygraph, and brain mapping violate Art 20(3) (right against self-incrimination) and Art 21 (right to personal liberty & mental privacy). Voluntary tests are permitted if safeguard guidelines are met.",
                "ta": "செல்வி வழக்கில் (2010) சம்மதமின்றி நடத்தப்படும் நார்ஃபோ அனாலிசிஸ், பாலிகிராஃப் மற்றும் மூளை வரைபட சோதனைகள் பிரிவு 20(3) மற்றும் 21-ஐ மீறுகின்றன எனப்பட்டது. தாமாக முன்வந்து செய்யும் சோதனைகள் அனுமதிக்கப்படும்."
            },
            "why_not_others": {
                "A": {"en": "Correct. Selvi case linked Art 20(3) self-incrimination with Art 21 mental privacy.", "ta": "சரி. செல்வி வழக்கு பிரிவு 20(3) மற்றும் பிரிவு 21 மனத் தனியுரிமையை இணைத்தது."},
                "B": {"en": "Incorrect. Article 14 & 19 were not the primary grounds.", "ta": "தவறு. 14 & 19 முதன்மை அடிப்படைகள் அல்ல."},
                "C": {"en": "Incorrect. Article 23 relates to forced labour.", "ta": "தவறு. 23 கட்டாய வேலை பற்றியது."},
                "D": {"en": "Incorrect. Article 17 relates to untouchability.", "ta": "தவறு. 17 தீண்டாமை பற்றியது."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: State of Bombay v. Kathi Kalu Oghad (1961) held that taking physical samples (thumb impression, handwriting, blood sample) DOES NOT violate Article 20(3) as it is non-testimonial evidence.",
                "ta": "TNPSC குறிப்பு: கதி காலு ஓகத் வழக்கில் (1961) கைரேகை, கையெழுத்து, ரத்த மாதிரி எடுப்பது பிரிவு 20(3)-ஐ மீறாது எனப்பட்டது (அவை சாட்சிய உரை அல்ல)."
            },
            "revision_fact": {
                "en": "Protection against self-incrimination under Art 20(3) extends to both oral and documentary evidence, but ONLY to persons accused of an offence.",
                "ta": "பிரிவு 20(3)-ன் கீழ் சுய சாட்சிய விலக்கு வாய்மொழி மற்றும் ஆவணச் சான்றுகளுக்குப் பொருந்தும், ஆனால் குற்றஞ்சாட்டப்பட்ட நபர்களுக்கு மட்டுமே."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Analyze",
            "estimated_time_sec": 60,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 20(3)", "Selvi Case", "Grand Test"]
        },

        # Q43: Direct MCQ - Article 21 Evolution Gopalan vs Maneka
        {
            "id": "FR_GT_043",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Medium",
            "question_type": "Direct MCQ",
            "question": {
                "en": "In which landmark 1978 judgment did the Supreme Court overrule A.K. Gopalan case (1950) and read the American concept of 'Due Process of Law' into Article 21, requiring procedure to be 'just, fair, and reasonable'?",
                "ta": "1978-ல் எந்த முக்கிய வழக்கில் உச்ச நீதிமன்றம் ஏ.கே. கோபாலன் வழக்கைத் (1950) தலைகீழாக மாற்றி, அமெரிக்கக் கருத்தான 'சட்டத்தின் உரிய நடைமுறையை' (Due Process of Law) பிரிவு 21-ல் இணைத்து, நடைமுறை 'நியாயமானதாக, நேர்மையானதாக' இருக்க வேண்டும் என்று கூறியது?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "Maneka Gandhi v. Union of India (1978)",
                    "ta": "மேனகா காந்தி எதிர் இந்திய யூனியன் (1978)"
                },
                {
                    "id": "B",
                    "en": "Minerva Mills v. Union of India (1980)",
                    "ta": "மினர்வா மில்ஸ் எதிர் இந்திய யூனியன் (1980)"
                },
                {
                    "id": "C",
                    "en": "Sunil Batra v. Delhi Administration (1978)",
                    "ta": "சுனில் பத்ரா எதிர் டெல்லி நிர்வாகம் (1978)"
                },
                {
                    "id": "D",
                    "en": "Hussainara Khatoon v. Home Secretary, State of Bihar (1979)",
                    "ta": "ஹுசைனாரா கத்தூன் எதிர் பீகார் அரசு (1979)"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "In Maneka Gandhi case (1978), SC widened the scope of Art 21. It held that 'procedure established by law' must satisfy tests of reasonableness, fairness, and justice (Due Process), protecting citizens against both arbitrary executive AND legislative action.",
                "ta": "மேனகா காந்தி வழக்கில் (1978) உச்ச நீதிமன்றம் பிரிவு 21-ன் எல்லையை விரிவுபடுத்தியது. 'சட்டம் அமைத்த நடைமுறை' என்பது நியாயமானதாக இருக்க வேண்டும் என்று கூறி தன்னிச்சையான நிர்வாக மற்றும் சட்டமன்ற நடவடிக்கைகளுக்கு எதிராகப் பாதுகாத்தது."
            },
            "why_not_others": {
                "A": {"en": "Correct. Maneka Gandhi case introduced Due Process into Article 21.", "ta": "சரி. மேனகா காந்தி வழக்கு பிரிவு 21-ல் Due Process-ஐ அறிமுகப்படுத்தியது."},
                "B": {"en": "Incorrect. Minerva Mills dealt with basic structure and DPSP balance.", "ta": "தவறு. மினர்வா மில்ஸ் அடிப்படை அமைப்பு பற்றியது."},
                "C": {"en": "Incorrect. Sunil Batra case dealt with solitary confinement and prisoners' rights.", "ta": "தவறு. சுனில் பத்ரா வழக்கு சிறைவாசிகளின் உரிமை பற்றியது."},
                "D": {"en": "Incorrect. Hussainara Khatoon case established Right to Speedy Trial under Art 21.", "ta": "தவறு. ஹுசைனாரா கத்தூன் வழக்கு விரைவு விசாரணை உரிமை பற்றியது."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: In A.K. Gopalan case (1950), SC gave narrow view protecting Art 21 ONLY against arbitrary executive action, not legislative action. Maneka Gandhi (1978) extended protection against legislative action too.",
                "ta": "TNPSC குறிப்பு: கோபாலன் வழக்கில் (1950) பிரிவு 21 நிர்வாக நடவடிக்கைக்கு மட்டுமே எதிரானது எனப்பட்டது. மேனகா காந்தி (1978) சட்டமன்ற நடவடிக்கைக்கும் எதிராக விரிவுபடுத்தியது."
            },
            "revision_fact": {
                "en": "The Golden Triangle of the Constitution consists of Articles 14, 19, and 21 inter-linked together.",
                "ta": "அரசியலமைப்பின் பொன் முக்கோணம் என்பது பிரிவுகள் 14, 19, மற்றும் 21 ஆகியவை ஒன்றோடொன்று இணைக்கப்பட்டதாகும்."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Remember",
            "estimated_time_sec": 40,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 21", "Maneka Gandhi", "Grand Test"]
        },

        # Q44: Conceptual MCQ - Right to Privacy Puttaswamy Judgment
        {
            "id": "FR_GT_044",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Medium",
            "question_type": "Conceptual MCQ",
            "question": {
                "en": "In Justice K.S. Puttaswamy (Retd.) v. Union of India (2017), a unanimous 9-judge Constitution Bench declared the Right to Privacy as an intrinsic part of which Fundamental Right?",
                "ta": "நீதிபதி கே.எஸ். புட்டசுவாமி (ஓய்வு) எதிர் இந்திய யூனியன் (2017) வழக்கில், ஒருமனதான 9 நீதிபதிகள் அரசியலமைப்பு அமர்வு தனியுரிமையை (Right to Privacy) எந்த அடிப்படை உரிமையின் உள்ளார்ந்த பகுதியாக அறிவித்தது?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "Right to Life and Personal Liberty under Article 21",
                    "ta": "பிரிவு 21-ன் கீழ் உள்ள வாழ்வு மற்றும் தனிநபர் சுதந்திர உரிமை"
                },
                {
                    "id": "B",
                    "en": "Freedom of Speech and Expression under Article 19(1)(a)",
                    "ta": "பிரிவு 19(1)(a)-ன் கீழ் உள்ள பேச்சு மற்றும் வெளிப்பாட்டுச் சுதந்திரம்"
                },
                {
                    "id": "C",
                    "en": "Equality before Law under Article 14",
                    "ta": "பிரிவு 14-ன் கீழ் உள்ள சட்டத்தின் முன் சமத்துவம்"
                },
                {
                    "id": "D",
                    "en": "Freedom of Conscience under Article 25",
                    "ta": "பிரிவு 25-ன் கீழ் உள்ள மனசாட்சி சுதந்திரம்"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "In Puttaswamy judgment (2017), 9-judge bench unanimously held Right to Privacy is a Fundamental Right guaranteed under Article 21 and Part III, overruling M.P. Sharma (1954) and Kharak Singh (1963) to the extent they held privacy was not an FR.",
                "ta": "புட்டசுவாமி தீர்ப்பில் (2017) 9 நீதிபதிகள் அமர்வு தனியுரிமை என்பது பிரிவு 21 மற்றும் பகுதி III-ன் கீழ் உத்தரவாதம் அளிக்கப்பட்ட அடிப்படை உரிமை எனத் தீர்ப்பளித்தது."
            },
            "why_not_others": {
                "A": {"en": "Correct. Right to Privacy is protected primarily under Article 21.", "ta": "சரி. தனியுரிமை முதன்மையாக பிரிவு 21-ன் கீழ் பாதுகாக்கப்படுகிறது."},
                "B": {"en": "Incorrect. Although linked to Art 19 & Part III freedoms, its primary core rests in Art 21.", "ta": "தவறு. 19-டன் தொடர்புடையது எனினும் முதன்மை மையம் பிரிவு 21-லேயே உள்ளது."},
                "C": {"en": "Incorrect. Article 14 is equality.", "ta": "தவறு. பிரிவு 14 சமத்துவம்."},
                "D": {"en": "Incorrect. Article 25 is religion freedom.", "ta": "தவறு. பிரிவு 25 மதச் சுதந்திரம்."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: Three-fold test for state interference with privacy laid down in Puttaswamy: (1) Legality (backed by law), (2) Legitimate State Aim, (3) Proportionality (proportional means to end).",
                "ta": "TNPSC குறிப்பு: புட்டசுவாமி வழக்கில் தனியுரிமையில் தலையிட 3 நிபந்தனைகள்: (1) சட்டப்பூர்வத் தன்மை, (2) அரசின் முறையான நோக்கம், (3) விகிதாசாரத் தன்மை (Proportionality)."
            },
            "revision_fact": {
                "en": "Puttaswamy bench overruled M.P. Sharma (1954 - 8 judges) and Kharak Singh (1963 - 6 judges) regarding privacy.",
                "ta": "புட்டசுவாமி அமர்வு எம்.பி. சர்மா (1954) மற்றும் கரக் சிங் (1963) தீர்ப்புகளைத் தனியுரிமை தொடர்பாக ரத்து செய்தது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Understand",
            "estimated_time_sec": 45,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 21", "Right to Privacy", "Puttaswamy", "Grand Test"]
        },

        # Q45: Direct MCQ - Article 21A 86th Constitutional Amendment Act
        {
            "id": "FR_GT_045",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Easy",
            "question_type": "Direct MCQ",
            "question": {
                "en": "The 86th Constitutional Amendment Act, 2002 made free and compulsory education a Fundamental Right under Article 21A for children of which age group?",
                "ta": "2002-ன் 86-வது அரசியலமைப்புத் திருத்தச் சட்டம், எந்த வயதுடைய குழந்தைகளுக்குப் பிரிவு 21A-ன் கீழ் இலவச மற்றும் கட்டாயக் கல்வியை அடிப்படை உரிமையாக்கியது?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "6 to 14 years",
                    "ta": "6 முதல் 14 ஆண்டுகள்"
                },
                {
                    "id": "B",
                    "en": "0 to 6 years",
                    "ta": "0 முதல் 6 ஆண்டுகள்"
                },
                {
                    "id": "C",
                    "en": "6 to 18 years",
                    "ta": "6 முதல் 18 ஆண்டுகள்"
                },
                {
                    "id": "D",
                    "en": "14 to 18 years",
                    "ta": "14 முதல் 18 ஆண்டுகள்"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "Article 21A mandates the State to provide free and compulsory education to all children of the age group 6 to 14 years in such manner as the State may, by law, determine. Enacted via Right to Education (RTE) Act 2009 w.e.f. April 1, 2010.",
                "ta": "பிரிவு 21A 6 முதல் 14 வயதுடைய அனைத்துக் குழந்தைகளுக்கும் இலவச மற்றும் கட்டாயக் கல்வியை அரசு வழங்கக் கட்டளையிடுகிறது. இது 2009-ன் கல்வி உரிமைச் சட்டம் மூலம் 2010 ஏப்ரல் 1 முதல் அமலுக்கு வந்தது."
            },
            "why_not_others": {
                "A": {"en": "Correct. 6 to 14 years is the age group specified in Article 21A.", "ta": "சரி. 6 முதல் 14 ஆண்டுகள் என்பது பிரிவு 21A-ல் குறிப்பிடப்பட்ட வயது வரம்பாகும்."},
                "B": {"en": "Incorrect. Early childhood care (0-6 years) is covered under DPSP Article 45.", "ta": "தவறு. 0-6 ஆண்டுகள் DPSP பிரிவு 45-ன் கீழ் வருகிறது."},
                "C": {"en": "Incorrect. 6 to 18 is wrong.", "ta": "தவறு. 6 முதல் 18 என்பது தவறானது."},
                "D": {"en": "Incorrect. 14 to 18 is wrong.", "ta": "தவறு. 14 முதல் 18 என்பது தவறானது."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: The 86th Amendment Act 2002 modified THREE parts of the Constitution: (1) Added Art 21A in Part III, (2) Substituted Art 45 in Part IV (0-6 years care), (3) Added Art 51A(k) in Part IV-A (duty of parent/guardian).",
                "ta": "TNPSC குறிப்பு: 86-வது திருத்தச் சட்டம் 2002 அரசியலமைப்பின் 3 பகுதிகளை மாற்றியது: (1) பகுதி III-ல் 21A, (2) பகுதி IV-ல் 45, (3) பகுதி IV-A-ல் 51A(k)."
            },
            "revision_fact": {
                "en": "In Unni Krishnan v. State of AP (1993), Supreme Court held education up to 14 years is a FR under Art 21, which prompted the 86th Amendment Act 2002.",
                "ta": "உன்னிகிருஷ்ணன் வழக்கில் (1993) 14 வயது வரையிலான கல்வி பிரிவு 21-ன் கீழ் அடிப்படை உரிமை எனத் தீர்ப்பளிக்கப்பட்டது, இது 86-வது திருத்தத்திற்கு வழிவகுத்தது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Remember",
            "estimated_time_sec": 35,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 21A", "86th Amendment", "RTE Act", "Grand Test"]
        },

        # Q46: Conceptual MCQ - Rights under Article 22 Punitive vs Preventive
        {
            "id": "FR_GT_046",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Medium",
            "question_type": "Conceptual MCQ",
            "question": {
                "en": "Which of the following procedural safeguards available under Article 22(1) and 22(2) for punitive arrest is NOT available to a person detained under a Preventive Detention law?",
                "ta": "குற்றவியல் கைதுக்காகப் பிரிவு 22(1) மற்றும் 22(2)-ன் கீழ் உள்ள பின்வரும் நடைமுறைப் பாதுகாப்புகளில் எது தடுப்புக் காவல் சட்டத்தின் கீழ் கைது செய்யப்படும் நபருக்குக் கிடைக்காது?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "Right to be produced before the nearest Magistrate within 24 hours of arrest",
                    "ta": "கைது செய்யப்பட்ட 24 மணி நேரத்திற்குள் அருகிலுள்ள நீதிபதி முன் ஆஜர்படுத்தப்படும் உரிமை"
                },
                {
                    "id": "B",
                    "en": "Right to be informed of the grounds of detention as soon as may be",
                    "ta": "கைதுக்கான காரணங்களை முடிந்தவரை விரைவில் அறிந்துகொள்ளும் உரிமை"
                },
                {
                    "id": "C",
                    "en": "Right to make a representation against the detention order at the earliest opportunity",
                    "ta": "தடுப்புக் காவல் உத்தரவுக்கு எதிராக மிக விரைவில் மேல்முறையீடு செய்யும் உரிமை"
                },
                {
                    "id": "D",
                    "en": "Right to review of detention by an Advisory Board",
                    "ta": "ஆலோசனைக் குழுவால் தடுப்புக் காவலை மறுஆய்வு செய்யும் உரிமை"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "Article 22(3) explicitly states that the rights under Art 22(1) & 22(2) (right to be informed of grounds of arrest, right to consult legal practitioner, right to be produced before magistrate within 24 hours) DO NOT apply to enemy aliens or persons detained under preventive detention laws.",
                "ta": "பிரிவு 22(3) தெளிவாகக் கூறுகிறது: 22(1) & 22(2)-ன் கீழ் உள்ள உரிமைகள் (24 மணி நேரத்திற்குள் நீதிபதி முன் ஆஜர்படுத்துதல், வழக்கறிஞர் கலந்தாய்வு) எதிரி நாட்டினருக்கோ அல்லது தடுப்புக் காவலில் உள்ளவர்களுக்கோ பொருந்தாது."
            },
            "why_not_others": {
                "A": {"en": "Correct. The 24-hour magistrate production rule under Art 22(2) is denied to preventive detainees.", "ta": "சரி. 24 மணி நேர நீதிபதி ஆஜர் விதி தடுப்புக் காவலில் உள்ளவர்களுக்குக் கிடைக்காது."},
                "B": {"en": "Incorrect. Grounds must be communicated to preventive detainees under Art 22(5).", "ta": "தவறு. 22(5)-ன் கீழ் தடுப்புக் காவலில் உள்ளவர்களுக்கும் காரணங்கள் தெரிவிக்கப்பட வேண்டும்."},
                "C": {"en": "Incorrect. Right to make representation is guaranteed under Art 22(5).", "ta": "தவறு. 22(5)-ன் கீழ் மேல்முறையீட்டு உரிமை உண்டு."},
                "D": {"en": "Incorrect. Advisory Board review is a constitutional requirement for preventive detention under Art 22(4).", "ta": "தவறு. 22(4)-ன் கீழ் ஆலோசனைக் குழு மறுஆய்வு கட்டாயமானது."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Trap: For ordinary punitive arrests under Art 22(2), the 24-hour limit excludes the time necessary for the journey from place of arrest to Magistrate's court.",
                "ta": "TNPSC பொறி: சாதாரணக் கைதில் 24 மணி நேரக் கணக்கீட்டில் கைதான இடத்திலிருந்து நீதிமன்றத்திற்குச் செல்லும் பயண நேரம் விலக்கப்படும்."
            },
            "revision_fact": {
                "en": "Preventive detention without Advisory Board opinion cannot exceed 3 months under Article 22(4). (Though 44th Amendment reduced it to 2 months, that provision has not been brought into force).",
                "ta": "ஆலோசனைக் குழுவின் அபிப்பிராயமின்றி தடுப்புக் காவல் 3 மாதங்களுக்கு மிகக்கூடாது (44-வது திருத்தம் 2 மாதங்களாகக் குறைத்த போதிலும், அப்பிரிவு நடைமுறைக்கு வரவில்லை)."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Understand",
            "estimated_time_sec": 45,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 22", "Preventive Detention", "Grand Test"]
        },

        # Q47: Statement-Based - Article 22 Preventive Detention Rules
        {
            "id": "FR_GT_047",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Hard",
            "question_type": "Statement-Based",
            "question": {
                "en": "Consider the following statements regarding Preventive Detention laws in India:\n1. Both Parliament and State Legislatures have concurrent power to enact preventive detention laws for reasons connected with public order and maintenance of essential supplies.\n2. Parliament has exclusive power to enact preventive detention laws for reasons connected with Defence, Foreign Affairs, or Security of India.\n3. Under Article 22(6), the State is obligated to disclose ALL facts to the detainee even if such disclosure is considered against public interest.\nWhich of the statements given above are correct?",
                "ta": "இந்தியாவில் உள்ள தடுப்புக் காவல் சட்டங்கள் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. பொது ஒழுங்கு மற்றும் அத்தியாவசியப் பொருட்கள் பராமரிப்பு தொடர்பான காரணங்களுக்காகத் தடுப்புக் காவல் சட்டங்களை இயற்ற நாடாளுமன்றம் மற்றும் மாநில சட்டமன்றங்கள் இரண்டிற்கும் பொதுவான (Concurrent) அதிகாரம் உண்டு.\n2. பாதுகாப்பு, வெளியுறவு அல்லது இந்தியாவின் பாதுகாப்பு தொடர்பான காரணங்களுக்காகத் தடுப்புக் காவல் சட்டங்களை இயற்ற நாடாளுமன்றத்திற்கு மட்டுமே பிரத்யேக அதிகாரம் உண்டு.\n3. பிரிவு 22(6)-ன் கீழ், பொது நலனுக்கு எதிரானது எனக் கருதப்பட்டாலும் அனைத்து உண்மைகளையும் தடுப்புக் காவலில் உள்ளவருக்கு அரசு கட்டாயம் வெளிப்படுத்த வேண்டும்.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?"
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
                "en": "Statements 1 and 2 are correct (reflecting legislative list division for preventive detention). Statement 3 is INCORRECT: Article 22(6) states that the authority is NOT required to disclose facts which such authority considers to be against the public interest to disclose.",
                "ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது: பிரிவு 22(6)-ன் கீழ் பொது நலனுக்கு எதிரானது எனக் கருதப்படும் உண்மைகளை வெளிப்படுத்த அரசுக்குக் கட்டாயமில்லை."
            },
            "why_not_others": {
                "A": {"en": "Correct. Statements 1 and 2 are true; statement 3 is false.", "ta": "சரி. கூற்றுகள் 1 மற்றும் 2 சரியானவை; கூற்று 3 தவறானது."},
                "B": {"en": "Incorrect because statement 3 is false.", "ta": "தவறு, ஏனெனில் கூற்று 3 தவறானது."},
                "C": {"en": "Incorrect because statement 3 is false.", "ta": "தவறு, ஏனெனில் கூற்று 3 தவறானது."},
                "D": {"en": "Incorrect because statement 3 is false.", "ta": "தவறு, ஏனெனில் கூற்று 3 தவறானது."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Trap: India is unique among major democratic Constitutions in making Preventive Detention an integral part of the Fundamental Rights chapter (Part III Article 22).",
                "ta": "TNPSC பொறி: முக்கிய ஜனநாயக அரசியலமைப்புகளில் தடுப்புக் காவலை அடிப்படை உரிமைகள் அத்தியாயத்தின் (பகுதி III பிரிவு 22) ஒரு பகுதியாகக் கொண்ட ஒரே நாடு இந்தியா மட்டுமே."
            },
            "revision_fact": {
                "en": "Famous past Preventive Detention Acts: MISA (1971), NASA (1980), TADA (1985), POTA (2002). National Security Act (NASA) 1980 is still in force.",
                "ta": "புகழ்பெற்ற தடுப்புக் காவல் சட்டங்கள்: MISA (1971), NASA (1980), TADA (1985), POTA (2002). தேசியப் பாதுகாப்புச் சட்டம் (NASA) 1980 இன்னும் நடைமுறையில் உள்ளது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Analyze",
            "estimated_time_sec": 60,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 22", "Preventive Detention Laws", "Grand Test"]
        },

        # Q48: Direct MCQ - Article 24 Child Labour Prohibition
        {
            "id": "FR_GT_048",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Easy",
            "question_type": "Direct MCQ",
            "question": {
                "en": "Under Article 24 of the Constitution of India, employment of children below what age is completely prohibited in any factory, mine or other hazardous employment?",
                "ta": "இந்திய அரசியலமைப்பின் 24-வது பிரிவின் கீழ், எந்த வயதிற்குட்பட்ட குழந்தைகளைத் தொழிற்சாலை, சுரங்கம் அல்லது பிற அபாயகரமான வேலைகளில் ஈடுபடுத்துவது முற்றிலும் தடை செய்யப்பட்டுள்ளது?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "Below 14 years",
                    "ta": "14 வயதிற்குட்பட்டோர்"
                },
                {
                    "id": "B",
                    "en": "Below 18 years",
                    "ta": "18 வயதிற்குட்பட்டோர்"
                },
                {
                    "id": "C",
                    "en": "Below 16 years",
                    "ta": "16 வயதிற்குட்பட்டோர்"
                },
                {
                    "id": "D",
                    "en": "Below 12 years",
                    "ta": "12 வயதிற்குட்பட்டோர்"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "Article 24 prohibits employment of children below the age of 14 years in any factory, mine or other hazardous engagement. Under Child Labour (Prohibition & Regulation) Amendment Act 2016, employment of children below 14 in ALL occupations is banned.",
                "ta": "பிரிவு 24 14 வயதிற்குட்பட்ட குழந்தைகளைத் தொழிற்சாலை, சுரங்கம் அல்லது அபாயகரமான பணிகளில் ஈடுபடுத்துவதைத் தடை செய்கிறது. 2016 திருத்தச் சட்டம் அனைத்து வேலைகளிலும் 14 வயதுக்குட்பட்டோர் பணியைத் தடை செய்தது."
            },
            "why_not_others": {
                "A": {"en": "Correct. Article 24 explicitly sets the age limit as below 14 years.", "ta": "சரி. பிரிவு 24 வெளிப்படையாக 14 வயதிற்குட்பட்டோர் என நிர்ணயிக்கிறது."},
                "B": {"en": "Incorrect. 18 years applies to adolescents (14-18) in hazardous occupations under 2016 Amendment Act.", "ta": "தவறு. 18 வயது என்பது 2016 சட்டத்தில் இளம் பருவத்தினருக்கு (14-18) அபாயகரமான தொழில்களுக்குப் பொருந்தும்."},
                "C": {"en": "Incorrect. 16 years is wrong.", "ta": "தவறு. 16 என்பது தவறானது."},
                "D": {"en": "Incorrect. 12 years is wrong.", "ta": "தவறு. 12 என்பது தவறானது."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: Child Labour Amendment Act 2016 created a new category called 'Adolescent' (14 to 18 years) and prohibited their employment in hazardous occupations and processes.",
                "ta": "TNPSC குறிப்பு: 2016 குழந்தை தொழிலாளர் திருத்தச் சட்டம் 'இளம் பருவத்தினர்' (14 முதல் 18 வயது) என்ற புதிய பிரிவை உருவாக்கி அவர்களை அபாயகரமான தொழில்களில் ஈடுபடுத்துவதைத் தடை செய்தது."
            },
            "revision_fact": {
                "en": "In M.C. Mehta v. State of Tamil Nadu (1996) (Sivakasi Case), Supreme Court directed creation of Child Labour Rehabilitation Welfare Fund.",
                "ta": "எம்.சி. மேத்தா எதிர் தமிழ்நாடு அரசு வழக்கில் (1996) (சிவகாசி வழக்கு) குழந்தைகள் पुनரமைப்பு நல நிதியை உருவாக்க உச்ச நீதிமன்றம் உத்தரவிட்டது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Remember",
            "estimated_time_sec": 35,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 24", "Child Labour", "Grand Test"]
        },

        # Q49: Conceptual MCQ - Right to Life Expanded Aspects
        {
            "id": "FR_GT_049",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Medium",
            "question_type": "Conceptual MCQ",
            "question": {
                "en": "Which landmark judgment of the Supreme Court recognized the 'Right to Die with Dignity' by declaring passive euthanasia and advance medical directives (living wills) permissible under Article 21?",
                "ta": "பிரிவு 21-ன் கீழ் செயலற்ற கருணைக்கொலை (passive euthanasia) மற்றும் முன்அட்வான்ஸ் மருத்துவ வழிகாட்டுதல்கள் (living wills) அனுமதிக்கத்தக்கவை என்று கூறி 'கண்ணியமாக இறக்கும் உரிமையை' அங்கீகரித்த உச்ச நீதிமன்றத்தின் முக்கியத் தீர்ப்பு எது?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "Common Cause (A Regd. Society) v. Union of India (2018)",
                    "ta": "காமன் காஸ் (பதிவுபெற்ற சங்கம்) எதிர் இந்திய யூனியன் (2018)"
                },
                {
                    "id": "B",
                    "en": "Gian Kaur v. State of Punjab (1996)",
                    "ta": "கியான் கவுர் எதிர் பஞ்சாப் அரசு (1996)"
                },
                {
                    "id": "C",
                    "en": "P. Rathinam v. Union of India (1994)",
                    "ta": "பி. ரத்தினம் எதிர் இந்திய யூனியன் (1994)"
                },
                {
                    "id": "D",
                    "en": "Parmanand Katara v. Union of India (1989)",
                    "ta": "பரமானந்த் கதாரா எதிர் இந்திய யூனியன் (1989)"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "In Common Cause case (2018), a 5-judge Constitution Bench held that Right to Life with dignity under Art 21 includes the 'Right to Die with Dignity', legalizing passive euthanasia and living wills. (Gian Kaur 1996 had earlier clarified that right to life does not include right to commit suicide).",
                "ta": "காமன் காஸ் வழக்கில் (2018) 5 நீதிபதிகள் அமர்வு கண்ணியமாக வாழும் உரிமையில் 'கண்ணியமாக இறக்கும் உரிமையும்' அடங்கும் என செயலற்ற கருணைக்கொலையை சட்டப்பூர்வமாக்கியது."
            },
            "why_not_others": {
                "A": {"en": "Correct. Common Cause (2018) judgment recognized passive euthanasia and living wills under Art 21.", "ta": "சரி. காமன் காஸ் (2018) தீர்ப்பு செயலற்ற கருணைக்கொலையை அங்கீகரித்தது."},
                "B": {"en": "Incorrect. Gian Kaur (1996) held suicide is unlawful under Section 309 IPC, but noted dying with dignity in terminal illness.", "ta": "தவறு. கியான் கவுர் (1996) தற்கொலை சட்டவிரோதமானது என்றது."},
                "C": {"en": "Incorrect. P. Rathinam (1994) struck down Sec 309 IPC, which was later overruled in Gian Kaur.", "ta": "தவறு. ரத்தினம் வழக்கு தற்கொலை சட்டத்தைச் செல்லாது என்றது, பின்னர் அது மாற்றப்பட்டது."},
                "D": {"en": "Incorrect. Parmanand Katara (1989) established every doctor's duty to save life without procedural delay.", "ta": "தவறு. பரமானந்த் கதாரா வழக்கு மருத்துவரின் அவசர சிகிச்சைக் கடமை பற்றியது."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: Parmanand Katara v. UOI (1989) held that it is the professional obligation of every medical doctor to attend to an injured person immediately to preserve life, without waiting for police formalities.",
                "ta": "TNPSC குறிப்பு: பரமானந்த் கதாரா வழக்கில் (1989) காயமடைந்தவரைக் காவல் நடைமுறைகளுக்குக் காத்திராமல் உடனடியாகக் குணப்படுத்துவது மருத்துவரின் கடமை எனப்பட்டது."
            },
            "revision_fact": {
                "en": "Aruna Shanbaug case (2011) first permitted passive euthanasia in India under strict High Court supervision.",
                "ta": "அருணா ஷான்பாக் வழக்கில் (2011) இந்தியாவில் உயர் நீதிமன்றக் கண்காணிப்பின் கீழ் செயலற்ற கருணைக்கொலை முதன்முதலில் அனுமதிக்கப்பட்டது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Understand",
            "estimated_time_sec": 50,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 21", "Right to Die", "Grand Test"]
        },

        # Q50: Chronology - Landmarks of Article 21 Expansion
        {
            "id": "FR_GT_050",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Hard",
            "question_type": "Chronology",
            "question": {
                "en": "Arrange the following landmark Supreme Court judgments expanding the horizons of Article 21 in correct chronological order:\n1. A.K. Gopalan v. State of Madras (Procedure established by law)\n2. Maneka Gandhi v. Union of India (Due process / fair procedure)\n3. Olga Tellis v. Bombay Municipal Corporation (Right to livelihood)\n4. K.S. Puttaswamy v. Union of India (Right to Privacy)",
                "ta": "பிரிவு 21-ன் எல்லைகளை விரிவுபடுத்திய பின்வரும் உச்ச நீதிமன்றத் தீர்ப்புகளைச் சரியான காலவரிசையில் அமைக்கவும்:\n1. ஏ.கே. கோபாலன் எதிர் மதராஸ் மாநிலம் (சட்டம் அமைத்த நடைமுறை)\n2. மேனகா காந்தி எதிர் இந்திய யூனியன் (சட்டத்தின் உரிய நடைமுறை)\n3. ஓல்கா டெல்லிஸ் எதிர் பம்பாய் மாநகராட்சி (வாழ்வாதார உரிமை)\n4. கே.எஸ். புட்டசுவாமி எதிர் இந்திய யூனியன் (தனியுரிமை)"
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
                "en": "Correct chronological sequence: (1) A.K. Gopalan case (1950); (2) Maneka Gandhi case (1978); (3) Olga Tellis case (1985 - pavement dwellers livelihood); (4) K.S. Puttaswamy case (2017 - right to privacy).",
                "ta": "சரியான காலவரிசை: (1) கோபாலன் வழக்கு (1950); (2) மேனகா காந்தி வழக்கு (1978); (3) ஓல்கா டெல்லிஸ் வழக்கு (1985 - நடைபாதைவாசி வாழ்வாதாரம்); (4) புட்டசுவாமி வழக்கு (2017 - தனியுரிமை)."
            },
            "why_not_others": {
                "A": {"en": "Correct order: 1950 -> 1978 -> 1985 -> 2017.", "ta": "சரியான வரிசை: 1950 -> 1978 -> 1985 -> 2017."},
                "B": {"en": "Incorrect sequence.", "ta": "தவறான வரிசை."},
                "C": {"en": "Incorrect sequence.", "ta": "தவறான வரிசை."},
                "D": {"en": "Incorrect sequence.", "ta": "தவறான வரிசை."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: Olga Tellis v. BMC (1985) held that Right to Life under Art 21 includes Right to Livelihood because no person can live without the means of living.",
                "ta": "TNPSC குறிப்பு: ஓல்கா டெல்லிஸ் வழக்கில் (1985) பிரிவு 21 வாழ்வு உரிமையில் வாழ்வாதார உரிமையும் அடங்கும் எனக் கூறப்பட்டது."
            },
            "revision_fact": {
                "en": "Hussainara Khatoon v. Home Secretary Bihar (1979) established the Right to Speedy Trial and free legal aid for undertrial prisoners under Art 21.",
                "ta": "ஹுசைனாரா கத்தூன் வழக்கில் (1979) விசாரணை கைதிகளுக்கான விரைவு விசாரணை மற்றும் இலவச சட்ட உதவி உரிமை நிறுவப்பட்டது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Analyze",
            "estimated_time_sec": 55,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 21", "Chronology", "Grand Test"]
        },

        # Q51: Direct MCQ - Article 19(1)(g) Trade & State Monopoly
        {
            "id": "FR_GT_051",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Easy",
            "question_type": "Direct MCQ",
            "question": {
                "en": "Under Article 19(6), the State is empowered to create a complete or partial monopoly in any trade, business, industry or service. How can such a State monopoly be created?",
                "ta": "பிரிவு 19(6)-ன் கீழ், எந்தவொரு வர்த்தகம், வணிகம் அல்லது சேவையில் முழுமையான அல்லது பகுதி முற்றுரிமையை உருவாக்க அரசிற்கு அதிகாரம் உண்டு. இத்தகைய அரசு முற்றுரிமையை எவ்வாறு உருவாக்க முடியும்?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "By a law enacted by Parliament or State Legislature",
                    "ta": "நாடாளுமன்றம் அல்லது மாநில சட்டமன்றத்தால் இயற்றப்பட்ட சட்டம் மூலம்"
                },
                {
                    "id": "B",
                    "en": "By a mere executive order issued without statutory backing",
                    "ta": "சட்டப்பூர்வ ஆதரவின்றி பிறப்பிக்கப்படும் வெறும் நிர்வாக உத்தரவு மூலம்"
                },
                {
                    "id": "C",
                    "en": "Only by a Constitutional Amendment under Article 368",
                    "ta": "பிரிவு 368-ன் கீழ் செய்யப்படும் அரசியலமைப்புத் திருத்தம் மூலம் மட்டுமே"
                },
                {
                    "id": "D",
                    "en": "Only with the prior approval of the Supreme Court",
                    "ta": "உச்ச நீதிமன்றத்தின் முன்அனுமதியுடன் மட்டுமே"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "1st Constitutional Amendment Act 1951 amended Article 19(6) to enable the State to create a complete or partial monopoly in any trade or business BY LAW. No citizen can question such monopoly law on ground of violating 19(1)(g).",
                "ta": "1-வது அரசியலமைப்புத் திருத்தச் சட்டம் 1951 பிரிவு 19(6)-ஐ திருத்தி சட்டம் மூலம் அரசு முற்றுரிமையை உருவாக்க அனுமதித்தது. இச்சட்டத்தை 19(1)(g)-ஐ மீறுகிறது எனச் சவால் செய்ய முடியாது."
            },
            "why_not_others": {
                "A": {"en": "Correct. State monopoly must be created by a statute/law enacted by legislature.", "ta": "சரி. அரசு முற்றுரிமை சட்டமன்றத்தால் இயற்றப்பட்ட சட்டம் மூலம் உருவாக்கப்பட வேண்டும்."},
                "B": {"en": "Incorrect. Executive orders without statutory backing cannot create monopoly.", "ta": "தவறு. சட்ட ஆதரவற்ற நிர்வாக உத்தரவால் முற்றுரிமையை உருவாக்க முடியாது."},
                "C": {"en": "Incorrect. Ordinary legislation is sufficient; constitutional amendment is not required.", "ta": "தவறு. சாதாரண சட்டமே போதுமானது, அரசியலமைப்புத் திருத்தம் தேவையில்லை."},
                "D": {"en": "Incorrect. Court approval is not required to pass legislation.", "ta": "தவறு. நீதிமன்ற முன்அனுமதி தேவையில்லை."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: Article 19(1)(g) does NOT guarantee the right to carry on dangerous or immoral trades (like betting, gambling, dealing in liquor or harmful drugs). State can totally prohibit them.",
                "ta": "TNPSC குறிப்பு: ஆபத்தான அல்லது ஒழுக்கக்கேடான தொழில்களை (சூதாட்டம், மது வர்த்தகம்) செய்யும் உரிமை 19(1)(g)-ன் கீழ் வராது. அரசு அவற்றை முற்றிலும் தடை செய்ய முடியும்."
            },
            "revision_fact": {
                "en": "Chintaman Rao v. State of MP (1951) held that total ban on bidi manufacturing during agricultural season violated Article 19(1)(g) as it was an unreasonable restriction.",
                "ta": "சிந்தாமன் ராவ் வழக்கில் (1951) விவசாயக் காலத்தில் பீடி தயாரிப்பிற்கு முழுத் தடை விதிப்பது 19(1)(g)-ஐ மீறும் நியாயமற்ற கட்டுப்பாடு எனப்பட்டது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Remember",
            "estimated_time_sec": 35,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 19(1)(g)", "State Monopoly", "Grand Test"]
        },

        # Q52: Conceptual MCQ - Double Jeopardy Art 20(2)
        {
            "id": "FR_GT_052",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Medium",
            "question_type": "Conceptual MCQ",
            "question": {
                "en": "The protection against 'Double Jeopardy' under Article 20(2) ('No person shall be prosecuted and punished for the same offence more than once') applies ONLY before which forum?",
                "ta": "பிரிவு 20(2)-ன் கீழ் உள்ள 'இரட்டைத் தண்டனைக்கு' எதிரான பாதுகாப்பு ('எந்தவொரு நபரும் ஒரே குற்றத்திற்காக ஒன்றுக்கு மேற்பட்ட முறை வழக்குத் தொடரப்பட்டுத் தண்டிக்கப்படக் கூடாது') எந்த மன்றத்தின் முன் மட்டுமே பொருந்தும்?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "Courts of Law or Judicial Tribunals",
                    "ta": "நீதிமன்றங்கள் அல்லது நீதித்துறை தீர்ப்பாயங்கள்"
                },
                {
                    "id": "B",
                    "en": "Departmental and Administrative Inquiry Bodies",
                    "ta": "துறை மற்றும் நிர்வாக விசாரணை அமைப்புகள்"
                },
                {
                    "id": "C",
                    "en": "Customs authorities confiscating goods",
                    "ta": "பொருட்களைப் பறிமுதல் செய்யும் சுங்க அதிகாரிகள்"
                },
                {
                    "id": "D",
                    "en": "Private employer disciplinary committees",
                    "ta": "தனியார் நிறுவன ஒழுங்கு நடவடிக்கைக் குழுக்கள்"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "Under S.A. Venkataraman v. Union of India (1954) and Maqbool Hussain v. State of Bombay (1953), protection under Art 20(2) is available ONLY in proceedings before a court of law or judicial tribunal. It does NOT bar departmental/administrative proceedings or customs confiscation.",
                "ta": "வெங்கடராமன் வழக்கில் (1954) 20(2) பாதுகாப்பு நீதிமன்றங்கள் அல்லது நீதித்துறை தீர்ப்பாயங்கள் முன்னிலையில் நடைபெறும் நடவடிக்கைகளுக்கு மட்டுமே பொருந்தும் எனக் கூறப்பட்டது. துறை விசாரணைகளுக்கு இது தடையல்ல."
            },
            "why_not_others": {
                "A": {"en": "Correct. Double jeopardy operates strictly in judicial prosecutions before court/tribunal.", "ta": "சரி. இரட்டைத் தண்டனை நீதிமன்ற/தீர்ப்பாய விசாரணைக்கு மட்டுமே பொருந்தும்."},
                "B": {"en": "Incorrect. Departmental enquiry followed by court trial is valid and not barred by Art 20(2).", "ta": "தவறு. துறை விசாரணைக்குப் பின் நீதிமன்ற வழக்குத் தொடர்வது செல்லும்."},
                "C": {"en": "Incorrect. Customs proceedings are administrative, not judicial trial.", "ta": "தவறு. சுங்க நடவடிக்கைகள் நிர்வாக ரீதியானவை."},
                "D": {"en": "Incorrect. Private employer disciplinary action is non-judicial.", "ta": "தவறு. தனியார் நிறுவன ஒழுங்கு நடவடிக்கை நீதித்துறை சார்ந்தது அல்ல."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Trap: For Article 20(2) to apply, the person must have been BOTH prosecuted AND punished in the earlier proceedings. Mere prosecution without punishment does not bar a second trial!",
                "ta": "TNPSC பொறி: பிரிவு 20(2) பொருந்த முந்தைய விசாரணையில் நபர் வழக்குத் தொடரப்பட்டிருக்கவும் வேண்டும் தண்டிக்கப்பட்டிருக்கவும் வேண்டும். தண்டனையின்றி வழக்கு நிலுவையில் இருந்தால் 2-வது வழக்கு செல்லுபடியாகும்!"
            },
            "revision_fact": {
                "en": "The doctrine of Double Jeopardy is based on the Latin maxim 'Nemo debet bis vexari pro una et eadem causa' (no man should be twice vexed for one and the same cause).",
                "ta": "இரட்டைத் தண்டனைக் கோட்பாடு 'ஒரே காரணத்திற்காக எந்த மனிதனும் இருமுறை அலைக்கழிக்கப்படக் கூடாது' என்ற இலத்தீன் பொன்மொழியை அடிப்படையாகக் கொண்டது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Understand",
            "estimated_time_sec": 45,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 20(2)", "Double Jeopardy", "Grand Test"]
        },

        # Q53: Statement-Based - Article 21 Rights Expansion
        {
            "id": "FR_GT_053",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Medium",
            "question_type": "Statement-Based",
            "question": {
                "en": "Which of the following rights have been declared by the Supreme Court as integral parts of Article 21 (Right to Life and Personal Liberty)?\n1. Right to clean environment and pollution-free water/air\n2. Right to free legal aid for poor accused persons\n3. Right against solitary confinement\n4. Right to shelter and housing\nSelect the correct answer using the code given below:",
                "ta": "பின்வரும் உரிமைகளில் எவற்றை பிரிவு 21-ன் (வாழ்வு மற்றும் தனிநபர் சுதந்திர உரிமை) ஒருங்கிணைந்த பகுதியாக உச்ச நீதிமன்றம் அறிவித்துள்ளது?\n1. தூய்மையான சுற்றுச்சூழல் மற்றும் மாசு இல்லாத நீர்/ காற்று உரிமை\n2. ஏழை குற்றஞ்சாட்டப்பட்ட நபர்களுக்கு இலவச சட்ட உதவி உரிமை\n3. தனிமைச் சிறை தண்டனைக்கு எதிரான உரிமை\n4. இருப்பிடம் மற்றும் வீட்டுவசதி உரிமை\nகீழே கொடுக்கப்பட்டுள்ள குறியீட்டைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:"
            },
            "options": [
                {
                    "id": "A",
                    "en": "1 and 2 only",
                    "ta": "1 மற்றும் 2 மட்டுமே"
                },
                {
                    "id": "B",
                    "en": "1, 2 and 3 only",
                    "ta": "1, 2 மற்றும் 3 மட்டுமே"
                },
                {
                    "id": "C",
                    "en": "2, 3 and 4 only",
                    "ta": "2, 3 மற்றும் 4 மட்டுமே"
                },
                {
                    "id": "D",
                    "en": "1, 2, 3 and 4",
                    "ta": "1, 2, 3 மற்றும் 4"
                }
            ],
            "correct_answer": "D",
            "explanation": {
                "en": "All four rights are parts of Art 21: (1) Clean environment (M.C. Mehta cases / Subhash Kumar 1991), (2) Free legal aid (Khatri 1981 / M.H. Hoskot 1978), (3) Against solitary confinement (Sunil Batra 1978), (4) Right to shelter (Chameli Singh 1996 / Shantistar Builders 1990).",
                "ta": "நான்கு உரிமைகளும் பிரிவு 21-ன் பகுதிகளாகும்: (1) தூய்மையான சுற்றுச்சூழல் (எம்.சி. மேத்தா வழக்கு), (2) இலவச சட்ட உதவி (ஹோஸ்காட் வழக்கு), (3) தனிமைச் சிறை எதிர்ப்பு (சுனில் பத்ரா வழக்கு), (4) இருப்பிட உரிமை (சமேலி சிங் வழக்கு)."
            },
            "why_not_others": {
                "A": {"en": "Incorrect because 3 and 4 are also included.", "ta": "தவறு, ஏனெனில் 3 மற்றும் 4-ம் அடங்கும்."},
                "B": {"en": "Incorrect because 4 is also included.", "ta": "தவறு, ஏனெனில் 4-ம் அடங்கும்."},
                "C": {"en": "Incorrect because 1 is also included.", "ta": "தவறு, ஏனெனில் 1-ம் அடங்கும்."},
                "D": {"en": "Correct. All four rights 1, 2, 3 and 4 are held under Article 21.", "ta": "சரி. 1, 2, 3 மற்றும் 4 நான்கு உரிமைகளும் பிரிவு 21-ன் கீழ் வருகின்றன."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: Right to Free Legal Aid is also a Directive Principle under Article 39A (added by 42nd Amendment 1976), implemented through Legal Services Authorities Act 1987 (NALSA).",
                "ta": "TNPSC குறிப்பு: இலவச சட்ட உதவி உரிமை DPSP பிரிவு 39A-லும் உள்ளது (42-வது திருத்தம் 1976), இது NALSA சட்டம் 1987 மூலம் அமல்படுத்தப்படுகிறது."
            },
            "revision_fact": {
                "en": "In Consumer Education and Research Centre (CERC) v. UOI (1995), Supreme Court held that Right to Health and medical care is a fundamental right under Article 21.",
                "ta": "CERC வழக்கில் (1995) சுகாதார உரிமை மற்றும் மருத்துவப் பராமரிப்பு உரிமை பிரிவு 21-ன் கீழ் அடிப்படை உரிமை எனப்பட்டது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Analyze",
            "estimated_time_sec": 55,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 21", "Expanded Rights", "Grand Test"]
        },

        # Q54: Match the Following - Article 19 Freedoms & Restrictions
        {
            "id": "FR_GT_054",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Medium",
            "question_type": "Match the Following",
            "question": {
                "en": "Match List-I (Article 19 Freedom) with List-II (Corresponding Restriction Clause):\nList-I:\na. Freedom of Speech and Expression (19(1)(a))\nb. Freedom of Peaceable Assembly (19(1)(b))\nc. Freedom of Association (19(1)(c))\nd. Freedom of Movement and Residence (19(1)(d) & (e))\n\nList-II:\n1. Article 19(3) - Public order, sovereignty and integrity\n2. Article 19(5) - General public interest & protection of Scheduled Tribes\n3. Article 19(2) - 8 grounds including security of State and decency\n4. Article 19(4) - Public order, morality, sovereignty and integrity",
                "ta": "பட்டியல்-I-ஐ (பிரிவு 19 சுதந்திரம்) பட்டியல்-II-உடன் (தொடர்புடைய கட்டுப்பாட்டுப் பிரிவு) பொருத்துக:\nபட்டியல்-I:\na. பேச்சு மற்றும் வெளிப்பாட்டுச் சுதந்திரம் (19(1)(a))\nb. அமைதியான கூட்ட சுதந்திரம் (19(1)(b))\nc. சங்கம் அமைக்கும் சுதந்திரம் (19(1)(c))\nd. நடமாடும் மற்றும் இருப்பிடச் சுதந்திரம் (19(1)(d) & (e))\n\nபட்டியல்-II:\n1. பிரிவு 19(3) - பொது ஒழுங்கு, இறையாண்மை மற்றும் ஒருமைப்பாடு\n2. பிரிவு 19(5) - பொது நலன் & பழங்குடியினர் பாதுகாப்பு\n3. பிரிவு 19(2) - அரசின் பாதுகாப்பு, ஒழுக்கம் உட்பட 8 அடிப்படைகள்\n4. பிரிவு 19(4) - பொது ஒழுங்கு, ஒழுக்கம், இறையாண்மை மற்றும் ஒருமைப்பாடு"
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
                "en": "Correct match: 19(1)(a) restricted by 19(2) (8 grounds); 19(1)(b) restricted by 19(3) (public order, sovereignty); 19(1)(c) restricted by 19(4) (public order, morality, sovereignty); 19(1)(d)/(e) restricted by 19(5) (public interest, ST protection).",
                "ta": "சரியான பொருத்தம்: 19(1)(a) -> 19(2) (8 அடிப்படைகள்); 19(1)(b) -> 19(3) (பொது ஒழுங்கு); 19(1)(c) -> 19(4) (பொது ஒழுங்கு, ஒழுக்கம்); 19(1)(d)/(e) -> 19(5) (பொது நலன், பழங்குடியினர்)."
            },
            "why_not_others": {
                "A": {"en": "Correct match: a-3, b-1, c-4, d-2.", "ta": "சரியான பொருத்தம்: a-3, b-1, c-4, d-2."},
                "B": {"en": "Incorrect mapping.", "ta": "தவறான பொருத்தம்."},
                "C": {"en": "Incorrect mapping.", "ta": "தவறான பொருத்தம்."},
                "D": {"en": "Incorrect mapping.", "ta": "தவறான பொருத்தம்."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: Notice that Article 19(1)(f) (Right to Property) and its restriction 19(5) were repealed by the 44th Constitutional Amendment Act 1978.",
                "ta": "TNPSC குறிப்பு: 19(1)(f) (சொத்துரிமை) மற்றும் அதன் கட்டுப்பாடு 19(5) ஆகியவை 44-வது திருத்தச் சட்டம் 1978 மூலம் நீக்கப்பட்டன."
            },
            "revision_fact": {
                "en": "Under Article 19(1)(b), assembly must be peaceable and WITHOUT ARMS. Right to strike or right to hold public meetings on private property without permission is not included.",
                "ta": "19(1)(b)-ன் கீழ் கூட்டம் அமைதியாகவும் ஆயுதமின்றியும் இருக்க வேண்டும். வேலைநிறுத்த உரிமை இதில் அடங்காது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Analyze",
            "estimated_time_sec": 60,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 19", "Match the Following", "Grand Test"]
        },

        # Q55: TNPSC Trap - Article 20 Suspension during Emergency
        {
            "id": "FR_GT_055",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Medium",
            "question_type": "TNPSC Trap",
            "question": {
                "en": "Following the 44th Constitutional Amendment Act 1978, which two Fundamental Rights CANNOT be suspended even during a National Emergency declared under Article 352?",
                "ta": "1978-ன் 44-வது அரசியலமைப்புத் திருத்தச் சட்டத்தைத் தொடர்ந்து, பிரிவு 352-ன் கீழ் தேசிய அவசரநிலை அறிவிக்கப்பட்டாலும் எந்த இரு அடிப்படை உரிமைகளை இடைநிறுத்தம் செய்ய முடியாது?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "Articles 20 and 21",
                    "ta": "பிரிவுகள் 20 மற்றும் 21"
                },
                {
                    "id": "B",
                    "en": "Articles 14 and 19",
                    "ta": "பிரிவுகள் 14 மற்றும் 19"
                },
                {
                    "id": "C",
                    "en": "Articles 21A and 22",
                    "ta": "பிரிவுகள் 21A மற்றும் 22"
                },
                {
                    "id": "D",
                    "en": "Articles 25 and 32",
                    "ta": "பிரிவுகள் 25 மற்றும் 32"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "44th Amendment Act 1978 amended Article 359 so that the President CANNOT suspend the right to move any court for the enforcement of Fundamental Rights under Articles 20 and 21 during Emergency. Thus, Arts 20 & 21 remain enforceable at all times.",
                "ta": "44-வது திருத்தச் சட்டம் 1978 பிரிவு 359-ஐ திருத்தியது, இதன் மூலம் அவசரநிலையின் போதும் பிரிவுகள் 20 மற்றும் 21-ன் கீழ் உள்ள உரிமைகளை அமல்படுத்தும் நீதிமன்ற உரிமை இடைநிறுத்தம் செய்யப்பட முடியாது."
            },
            "why_not_others": {
                "A": {"en": "Correct. Articles 20 and 21 can NEVER be suspended during National Emergency.", "ta": "சரி. பிரிவுகள் 20 மற்றும் 21 அவசரநிலையிலும் ஒருபோதும் இடைநிறுத்தப்பட முடியாது."},
                "B": {"en": "Incorrect. Article 19 is automatically suspended under Art 358 during War/External Aggression.", "ta": "தவறு. பிரிவு 19 போரின் போது தானாகவே இடைநிறுத்தப்படும் (பிரிவு 358)."},
                "C": {"en": "Incorrect. Article 22 can be suspended under Art 359 presidential order.", "ta": "தவறு. பிரிவு 22 இடைநிறுத்தப்படலாம்."},
                "D": {"en": "Incorrect. Article 32 enforcement can be suspended for other rights under Art 359 order.", "ta": "தவறு. பிரிவு 32 இடைநிறுத்தப்படலாம்."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Trap: Article 358 suspends Article 19 ONLY when Emergency is declared on grounds of War or External Aggression, NOT on Armed Rebellion!",
                "ta": "TNPSC பொறி: பிரிவு 358 போர் அல்லது வெளிநாட்டு ஆக்கிரமிப்பு காரணத்திற்காக அவசரநிலை அறிவிக்கப்பட்டால் மட்டுமே பிரிவு 19-ஐத் தானாக இடைநிறுத்தும், ஆயுதமேந்திய கிளர்ச்சியின் போது அல்ல!"
            },
            "revision_fact": {
                "en": "ADM Jabalpur v. Shivkant Shukla (1976) (Habeas Corpus case) famously held during Emergency that even Art 21 could be suspended, which was later remedied by 44th Amendment 1978 and formally overruled in K.S. Puttaswamy (2017).",
                "ta": "ஏ.டி.எம். ஜபல்பூர் வழக்கின் (1976) தவறான நிலை 44-வது திருத்தம் 1978 மூலமும் புட்டசுவாமி (2017) வழக்கிலும் சரிசெய்யப்பட்டது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Understand",
            "estimated_time_sec": 40,
            "pyq_similarity": "High",
            "tags": ["Polity", "Emergency", "Article 20", "Article 21", "Grand Test"]
        },

        # Q56: PYQ Pattern - Article 23 Traffic in Human Beings & Begar
        {
            "id": "FR_GT_056",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Easy",
            "question_type": "PYQ Pattern",
            "question": {
                "en": "What does the term 'Begar' under Article 23(1) of the Indian Constitution specifically mean?",
                "ta": "இந்திய அரசியலமைப்பின் 23(1) பிரிவின் கீழ் உள்ள 'பெகார்' (Begar) என்ற சொல் குறிப்பான எதனைக் குறிக்கிறது?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "Compulsory work performed without any remuneration or payment",
                    "ta": "எந்தவித ஊதியமும் அல்லது தொகையும் வழங்கப்படாமல் செய்யப்படும் கட்டாய வேலை"
                },
                {
                    "id": "B",
                    "en": "Work performed by prisoners serving rigorous imprisonment",
                    "ta": "கடுங்காவல் தண்டனை அனுபவிக்கும் சிறைவாசிகளால் செய்யப்படும் வேலை"
                },
                {
                    "id": "C",
                    "en": "Overtime work performed beyond 8 hours a day",
                    "ta": "ஒரு நாளில் 8 மணி நேரத்திற்கு மேல் செய்யப்படும் கூடுதல் நேர வேலை"
                },
                {
                    "id": "D",
                    "en": "Voluntary community service done without expecting reward",
                    "ta": "எதிர்பார்ப்பின்றி செய்யப்படும் தன்னார்வச் சமூக சேவை"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "'Begar' is an indigenous Indian practice where a person is compelled to work for a master or zamindar without any remuneration/payment. Article 23(1) prohibits begar, traffic in human beings, and other similar forms of forced labour.",
                "ta": "'பெகார்' என்பது எந்த ஊதியமும் இன்றி ஒரு நபரை கட்டாயப்படுத்தி வேலை வாங்கும் பழக்கமாகும். பிரிவு 23(1) பெகார், மனித வர்த்தகம் மற்றும் கட்டாய வேலையைத் தடை செய்கிறது."
            },
            "why_not_others": {
                "A": {"en": "Correct. Begar means compulsory unremunerated labour.", "ta": "சரி. பெகார் என்பது ஊதியமற்ற கட்டாய வேலை."},
                "B": {"en": "Incorrect. Prison labour paid minimum wages is lawful.", "ta": "தவறு. குறைந்தபட்ச ஊதியம் பெறும் சிறை வேலை சட்டப்பூர்வமானது."},
                "C": {"en": "Incorrect. Overtime work with wages is regulated by labour law.", "ta": "தவறு. ஊதியத்துடன் கூடிய கூடுதல் பணி சட்டம் சார்ந்தது."},
                "D": {"en": "Incorrect. Voluntary service is not forced labour.", "ta": "தவறு. தன்னார்வ சேவை கட்டாய வேலை அல்ல."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: In People's Union for Democratic Rights v. UOI (Asiad Workers 1982), SC held that paying LESS than minimum wage also amounts to 'forced labour' under Article 23.",
                "ta": "TNPSC குறிப்பு: ஆசியட் தொழிலாளர்கள் வழக்கில் (1982) குறைந்தபட்ச ஊதியத்தை விடக் குறைவாக வழங்குவதும் பிரிவு 23-ன் கீழ் 'கட்டாய வேலை' ஆகும் எனப்பட்டது."
            },
            "revision_fact": {
                "en": "Immoral Traffic (Prevention) Act 1956 gives effect to the prohibition of traffic in human beings under Article 23.",
                "ta": "பிரிவு 23-ன் கீழ் மனித வர்த்தகத் தடையை அமல்படுத்த 1956-ல் பாலியல் தொழில் ஒழிப்புச் சட்டம் இயற்றப்பட்டது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Remember",
            "estimated_time_sec": 35,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 23", "Begar", "Forced Labour", "Grand Test"]
        },

        # Q57: Hard / Analytical - Article 21A & RTE Act 2009 Reservations
        {
            "id": "FR_GT_057",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Hard",
            "question_type": "Hard / Analytical",
            "question": {
                "en": "In Society for Unaided Private Schools of Rajasthan v. Union of India (2012), the Supreme Court upheld Section 12(1)(c) of the RTE Act 2009 (mandating 25% reservation for weaker sections in entry class). Which category of private schools was declared EXEMPTED from this 25% mandate?",
                "ta": "ராஜஸ்தான் தனியார் சுயநிதிக் பள்ளிகள் சங்கம் வழக்கில் (2012), RTE சட்டம் 2009-ன் பிரிவு 12(1)(c)-ஐ (சேர்க்கை வகுப்பில் 25% EWS இடஒதுக்கீடு) உச்ச நீதிமன்றம் உறுதி செய்தது. இந்த 25% கட்டாயத்திலிருந்து விலக்களிக்கப்பட்ட தனியார் பள்ளி வகை எது?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "Unaided Minority Educational Institutions under Article 30(1)",
                    "ta": "பிரிவு 30(1)-ன் கீழ் உள்ள உதவி பெறாத சிறுபான்மை கல்வி நிறுவனங்கள்"
                },
                {
                    "id": "B",
                    "en": "Unaided Non-Minority Private Schools",
                    "ta": "உதவி பெறாத சிறுபான்மையற்ற தனியார் பள்ளிகள்"
                },
                {
                    "id": "C",
                    "en": "Government Aided Boarding Schools",
                    "ta": "அரசு உதவி பெறும் விடுதிப் பள்ளிகள்"
                },
                {
                    "id": "D",
                    "en": "International Baccalaureate (IB) Schools",
                    "ta": "சர்வதேச இளங்கலை (IB) பள்ளிகள்"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "In Society for Unaided Private Schools case (2012) and Pramati Educational Trust case (2014), Supreme Court held that Section 12(1)(c) of RTE Act (25% free seats for disadvantaged children) applies to government, aided, and unaided non-minority private schools, but NOT to unaided or aided minority schools under Art 30(1).",
                "ta": "2012 மற்றும் 2014 தீர்ப்புகளில் RTE சட்டத்தின் 25% இடஒதுக்கீடு அரசு, அரசு உதவி பெறும் மற்றும் சுயநிதி சிறுபான்மையற்ற பள்ளிகளுக்குப் பொருந்தும், ஆனால் பிரிவு 30(1) சிறுபான்மைப் பள்ளிகளுக்குப் பொருந்தாது எனப்பட்டது."
            },
            "why_not_others": {
                "A": {"en": "Correct. Minority institutions under Art 30(1) are exempted from RTE 25% quota.", "ta": "சரி. பிரிவு 30(1) சிறுபான்மை நிறுவனங்கள் RTE 25% ஒதுக்கீட்டிலிருந்து விலக்கப்பட்டுள்ளன."},
                "B": {"en": "Incorrect. Unaided non-minority schools are strictly bound by 25% quota.", "ta": "தவறு. சுயநிதி சிறுபான்மையற்ற பள்ளிகளுக்கு 25% இடஒதுக்கீடு கட்டாயம்."},
                "C": {"en": "Incorrect. Government aided schools are bound.", "ta": "தவறு. அரசு உதவி பெறும் பள்ளிகளுக்குக் கட்டாயம்."},
                "D": {"en": "Incorrect. Curriculum board does not grant exemption under RTE Act.", "ta": "தவறு. பாடத்திட்ட வாரியம் விலக்கு அளிக்காது."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: RTE Act 2009 came into force on 1st April 2010. India became one of 135 countries to make education a fundamental right of every child.",
                "ta": "TNPSC குறிப்பு: RTE சட்டம் 2009 ஏப்ரல் 1, 2010 முதல் அமலுக்கு வந்தது. கல்வியை அடிப்படை உரிமையாக்கிய 135 நாடுகளில் இந்தியாவும் ஒன்று."
            },
            "revision_fact": {
                "en": "Article 21A covers primary education (ages 6-14), not higher or professional education.",
                "ta": "பிரிவு 21A தொடக்கக் கல்வியை மட்டுமே (6-14 வயது) குறிக்கிறது, உயர் கல்வியை அல்ல."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Analyze",
            "estimated_time_sec": 60,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 21A", "RTE Act", "Minority Exemption", "Grand Test"]
        },

        # Q58: Conceptual MCQ - Right to Silence vs Art 20(3)
        {
            "id": "FR_GT_058",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Medium",
            "question_type": "Conceptual MCQ",
            "question": {
                "en": "The right against self-incrimination under Article 20(3) extends to which of the following stages of criminal proceedings?",
                "ta": "பிரிவு 20(3)-ன் கீழ் உள்ள சுய சாட்சிய விலக்கு உரிமை குற்றவியல் நடவடிக்கைகளின் எந்த நிலைகளுக்குப் பொருந்தும்?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "Both police investigation stage and judicial trial stage",
                    "ta": "காவல் விசாரணை நிலை மற்றும் நீதிமன்ற விசாரணை நிலை ஆகிய இரண்டும்"
                },
                {
                    "id": "B",
                    "en": "Judicial trial stage before Magistrate only",
                    "ta": "நீதிபதி முன் நடைபெறும் நீதிமன்ற விசாரணை நிலை மட்டுமே"
                },
                {
                    "id": "C",
                    "en": "Police interrogation stage before FIR registration only",
                    "ta": "முதல் தகவல் அறிக்கை பதிவுக்கு முந்தைய காவல் விசாரணை நிலை மட்டுமே"
                },
                {
                    "id": "D",
                    "en": "Civil court cross-examination proceedings only",
                    "ta": "உரிமையியல் நீதிமன்றக் குறுக்கு விசாரணை நிலை மட்டுமே"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "In M.P. Sharma v. Satish Chandra (1954) and Nandini Satpathy v. P.L. Dani (1978), the Supreme Court ruled that protection under Art 20(3) is available at BOTH the stage of police investigation/interrogation and trial in court, whenever a person is accused of an offence.",
                "ta": "நந்தினி சத்பதி வழக்கில் (1978) பிரிவு 20(3) பாதுகாப்பு காவல் விசாரணை நிலை மற்றும் நீதிமன்ற விசாரணை நிலை ஆகிய இரண்டிலுமே குற்றஞ்சாட்டப்பட்ட நபருக்குக் கிடைக்கும் எனத் தீர்ப்பளிக்கப்பட்டது."
            },
            "why_not_others": {
                "A": {"en": "Correct. Art 20(3) protects an accused during both police interrogation and court trial.", "ta": "சரி. பிரிவு 20(3) காவல் விசாரணை மற்றும் நீதிமன்ற விசாரணை இரண்டிலும் பாதுகாக்கிறது."},
                "B": {"en": "Incorrect. Restricting it only to court trial is wrong.", "ta": "தவறு. நீதிமன்ற விசாரணைக்கு மட்டும் கட்டுப்படுத்துவது தவறானது."},
                "C": {"en": "Incorrect. Restricting it only to police interrogation is wrong.", "ta": "தவறு. காவல் விசாரணைக்கு மட்டும் கட்டுப்படுத்துவது தவறானது."},
                "D": {"en": "Incorrect. Art 20(3) applies to criminal proceedings, not civil cases.", "ta": "தவறு. பிரிவு 20(3) குற்றவியல் வழக்குகளுக்கு மட்டுமே பொருந்தும்."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: Nandini Satpathy v. P.L. Dani (1978) held that an accused person has a 'Right to Silence' during police interrogation if answering would expose them to criminal charge.",
                "ta": "TNPSC குறிப்பு: நந்தினி சத்பதி வழக்கில் (1978) காவல் விசாரணையின் போது குற்றச்சாட்டை உறுதிப்படுத்தும் கேள்விகளுக்குப் பதிலளிக்காமல் 'அமைதி காக்கும் உரிமை' குற்றஞ்சாட்டப்பட்டவருக்கு உண்டு எனப்பட்டது."
            },
            "revision_fact": {
                "en": "Under Section 161(2) CrPC, a person is bound to answer police questions truthfully, EXCEPT those which would have a tendency to expose them to a criminal charge.",
                "ta": "CrPC பிரிவு 161(2)-ன் படி குற்றவியல் குற்றச்சாட்டை உருவாக்கும் கேள்விகளைத் தவிர பிற கேள்விகளுக்கு உண்மையான பதிலளிக்க நபர் கடமைப்பட்டவர்."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Understand",
            "estimated_time_sec": 45,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 20(3)", "Right to Silence", "Grand Test"]
        },

        # Q59: Statement-Based - Reasonable Restrictions on Assembly Art 19(1)(b)
        {
            "id": "FR_GT_059",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Medium",
            "question_type": "Statement-Based",
            "question": {
                "en": "Consider the following statements regarding freedom of assembly under Article 19(1)(b):\n1. The right to assemble peaceably and without arms includes the right to hold public meetings and processions on public streets.\n2. The right to assemble does NOT include the right to strike work.\n3. Section 144 of the Code of Criminal Procedure (CrPC) allows a Magistrate to restrain an assembly if there is risk of obstruction, annoyance or danger to human life.\nWhich of the statements given above are correct?",
                "ta": "பிரிவு 19(1)(b)-ன் கீழ் உள்ள கூட்ட சுதந்திரம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. அமைதியாகவும் ஆயுதமின்றியும் கூடும் உரிமை, பொதுத் தெருக்களில் பொதுக் கூட்டங்கள் மற்றும் ஊர்வலங்களை நடத்தும் உரிமையை உள்ளடக்கியது.\n2. கூடும் உரிமையில் வேலைநிறுத்தம் செய்யும் உரிமை சேர்க்கப்படவில்லை.\n3. மனித உயிருக்கு ஆபத்து, இடையூறு ஏற்படும் அபாயம் இருந்தால் ஒரு கூட்டத்தைக் கட்டுப்படுத்தக் குற்றவியல் நடைமுறைச் சட்டப் (CrPC) பிரிவு 144 நீதிபதிக்கு அனுமதி அளிக்கிறது.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?"
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
                "en": "All three statements are correct. Assembly under 19(1)(b) must be peaceful & unarmed. It includes processions, but NOT strikes (TK Rangarajan case 2003). Section 144 CrPC / Section 129 BNSS permits reasonable magistrate orders to prevent public disorder (Babulal Parate 1961 / Ramlila Maidan 2012).",
                "ta": "மூன்று கூற்றுகளும் சரியானவை. 19(1)(b) கூட்டம் அமைதியாகவும் ஆயுதமின்றியும் இருக்க வேண்டும். ஊர்வலம் அடங்கும், வேலைநிறுத்தம் அடங்காது. CrPC 144-வது பிரிவு பொது அமைதியைக் காக்க நீதிபதிக்கு அதிகாரம் அளிக்கிறது."
            },
            "why_not_others": {
                "A": {"en": "Incorrect because statement 3 is also correct.", "ta": "தவறு, ஏனெனில் கூற்று 3-ம் சரியானது."},
                "B": {"en": "Incorrect because statement 1 is also correct.", "ta": "தவறு, ஏனெனில் கூற்று 1-ம் சரியானது."},
                "C": {"en": "Incorrect because statement 2 is also correct.", "ta": "தவறு, ஏனெனில் கூற்று 2-ம் சரியானது."},
                "D": {"en": "Correct. All statements 1, 2 and 3 are factually accurate.", "ta": "சரி. கூற்றுகள் 1, 2 மற்றும் 3 அனைத்தும் சரியானவை."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: In Himat Lal v. Police Commissioner Ahmedabad (1973), Supreme Court held that citizens have a right to hold public meetings on public streets, subject to reasonable traffic regulations.",
                "ta": "TNPSC குறிப்பு: ஹிமத் லால் வழக்கில் (1973) பொது வீதிகளில் போக்குவரத்துக் கட்டுப்பாடுகளுக்கு உட்பட்டுப் பொதுக் கூட்டங்களை நடத்தக் குடிமக்களுக்கு உரிமை உண்டு எனப்பட்டது."
            },
            "revision_fact": {
                "en": "Section 141 of IPC makes an assembly of 5 or more persons unlawful if its object is to commit an offence or resist execution of law.",
                "ta": "IPC பிரிவு 141 ஐந்து அல்லது அதற்கு மேற்பட்ட நபர்கள் கூடும் கூட்டத்தின் நோக்கம் குற்றஞ்செய்வதாக இருந்தால் அதைச் சட்டவிரோதக் கூட்டமாக்குகிறது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Analyze",
            "estimated_time_sec": 55,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 19(1)(b)", "Freedom of Assembly", "Grand Test"]
        },

        # Q60: Direct MCQ - Fundamental Right against Human Trafficking
        {
            "id": "FR_GT_060",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Easy",
            "question_type": "Direct MCQ",
            "question": {
                "en": "Which Article of the Constitution of India prohibits traffic in human beings, begar and other similar forms of forced labour?",
                "ta": "இந்திய அரசியலமைப்பின் எந்தப் பிரிவு மனித வர்த்தகம், பெகார் மற்றும் இதர கட்டாய வேலைகளைத் தடை செய்கிறது?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "Article 23",
                    "ta": "பிரிவு 23"
                },
                {
                    "id": "B",
                    "en": "Article 24",
                    "ta": "பிரிவு 24"
                },
                {
                    "id": "C",
                    "en": "Article 21",
                    "ta": "பிரிவு 21"
                },
                {
                    "id": "D",
                    "en": "Article 17",
                    "ta": "பிரிவு 17"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "Article 23 explicitly prohibits traffic in human beings, begar, and other similar forms of forced labour. Article 24 specifically prohibits child labour below 14 in factories/mines.",
                "ta": "பிரிவு 23 மனித வர்த்தகம், பெகார் மற்றும் கட்டாய வேலைகளை வெளிப்படையாகத் தடை செய்கிறது. பிரிவு 24 14 வயதுக்குட்பட்ட குழந்தை தொழிலாளர் முறையைத் தடை செய்கிறது."
            },
            "why_not_others": {
                "A": {"en": "Correct. Article 23 guarantees Right against Exploitation regarding forced labour & trafficking.", "ta": "சரி. பிரிவு 23 கட்டாய வேலை மற்றும் மனித வர்த்தகத்திற்கு எதிரான சுரண்டல் எதிர்ப்பு உரிமை."},
                "B": {"en": "Incorrect. Article 24 deals with prohibition of child labour in hazardous occupations.", "ta": "தவறு. பிரிவு 24 குழந்தைத் தொழிலாளர் ஒழிப்பு பற்றியது."},
                "C": {"en": "Incorrect. Article 21 deals with protection of life and personal liberty.", "ta": "தவறு. பிரிவு 21 வாழ்வுரிமை பற்றியது."},
                "D": {"en": "Incorrect. Article 17 deals with abolition of untouchability.", "ta": "தவறு. பிரிவு 17 தீண்டாமை ஒழிப்பு பற்றியது."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: 'Traffic in human beings' under Article 23 includes selling and buying of men, women and children like goods, immoral traffic in women and children, and devadasi system.",
                "ta": "TNPSC குறிப்பு: பிரிவு 23-ன் கீழ் 'மனித வர்த்தகம்' என்பது ஆண்கள், பெண்கள், குழந்தைகளைப் பொருட்களைப் போல விற்பது/வாங்குவது, தேவதாசி முறை போன்றவற்றை உள்ளடக்கியது."
            },
            "revision_fact": {
                "en": "Sanjit Roy v. State of Rajasthan (1983) held that paying less than minimum wage to workers employed in famine relief work violates Article 23.",
                "ta": "சஞ்ஜித் ராய் வழக்கில் (1983) வறட்சி நிவாரணப் பணியில் உள்ள பணியாளர்களுக்குக் குறைந்தபட்ச ஊதியத்தை விடக் குறைவாக வழங்குவது பிரிவு 23-ஐ மீறுகிறது எனப்பட்டது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Remember",
            "estimated_time_sec": 30,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 23", "Exploitation", "Grand Test"]
        },

        # Q61: Conceptual MCQ - Reasonable Restrictions Test Chintaman Rao
        {
            "id": "FR_GT_061",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Hard",
            "question_type": "Conceptual MCQ",
            "question": {
                "en": "What test did the Supreme Court lay down in Chintaman Rao v. State of MP (1951) to determine whether a restriction imposed by the legislature on Article 19 freedoms is 'reasonable'?",
                "ta": "பிரிவு 19 சுதந்திரங்கள் மீது சட்டமன்றத்தால் விதிக்கப்படும் கட்டுப்பாடு 'நியாயமானதா' என்பதைத் தீர்மானிக்க சிந்தாமன் ராவ் எதிர் மத்தியப் பிரதேச அரசு (1951) வழக்கில் உச்ச நீதிமன்றம் எந்த சோதனையை வகுத்தது?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "The restriction must strike a proper balance between the freedom guaranteed and the social control required, and must not be arbitrary or excessive",
                    "ta": "கட்டுப்பாடு உத்தரவாதம் அளிக்கப்பட்ட சுதந்திரத்திற்கும் தேவைப்படும் சமூகக் கட்டுப்பாட்டிற்கும் இடையே சரியான சமநிலையை ஏற்படுத்த வேண்டும், மேலும் தன்னிச்சையானதாகவோ அளவுக்கு அதிகமானதாகவோ இருக்கக்கூடாது"
                },
                {
                    "id": "B",
                    "en": "The restriction must be approved by two-thirds majority of state legislature",
                    "ta": "கட்டுப்பாடு மாநில சட்டமன்றத்தின் மூன்றில் இரண்டு பங்கு பெரும்பான்மையால் அங்கீகரிக்கப்பட வேண்டும்"
                },
                {
                    "id": "C",
                    "en": "The restriction must be endorsed by the President of India",
                    "ta": "கட்டுப்பாடு இந்தியக் குடியரசுத் தலைவரால் ஒப்புதல் அளிக்கப்பட வேண்டும்"
                },
                {
                    "id": "D",
                    "en": "The restriction must apply uniformly across all Asian countries",
                    "ta": "கட்டுப்பாடு அனைத்து ஆசிய நாடுகளிலும் சீராகப் பொருந்த வேண்டும்"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "In Chintaman Rao v. State of MP (1951), SC held that 'reasonable restriction' implies intelligent care and deliberation, choice of a course which reason dictates. An arbitrary or excessive restriction going beyond the requirement of interest of general public is unconstitutional.",
                "ta": "சிந்தாமன் ராவ் வழக்கில் (1951) 'நியாயமான கட்டுப்பாடு' என்பது அறிவுபூர்வமான அக்கறையையும், பொது நலனுக்குத் தேவையான அளவிற்கு மிகாமல் தன்னிச்சையின்றி இருப்பதையும் குறிக்கும் எனப்பட்டது."
            },
            "why_not_others": {
                "A": {"en": "Correct. Test of reasonableness requires proper balance without excessiveness.", "ta": "சரி. நியாயத்தன்மையின் சோதனை அளவுக்கு அதிகமான கட்டுப்பாடின்றி சமநிலையைக் கேட்கிறது."},
                "B": {"en": "Incorrect. Legislative majority does not determine reasonableness.", "ta": "தவறு. சட்டமன்ற பெரும்பான்மை நியாயத்தன்மையை நிர்ணயிக்காது."},
                "C": {"en": "Incorrect. Presidential approval is irrelevant to judicial review of reasonableness.", "ta": "தவறு. குடியரசுத் தலைவர் ஒப்புதல் நீதித்துறை மறுஆய்விற்குப் பொருந்தாது."},
                "D": {"en": "Incorrect. International uniformity is irrelevant.", "ta": "தவறு. சர்வதேசச் சீர்மை தொடர்பற்றது."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: The determination of 'reasonableness' of a restriction under Article 19 is a JUDICIAL function. The opinion of the legislature is not final; the Supreme Court/High Court is the ultimate judge.",
                "ta": "TNPSC குறிப்பு: பிரிவு 19-ன் கீழ் ஒரு கட்டுப்பாட்டின் 'நியாயத்தன்மையை' தீர்மானிப்பது நீதித்துறைப் பணியாகும். சட்டமன்றத்தின் முடிவு இறுதியானது அல்ல."
            },
            "revision_fact": {
                "en": "Reasonableness of a restriction is judged from both substantive and procedural aspects (State of Madras v. V.G. Row 1952).",
                "ta": "கட்டுப்பாட்டின் நியாயத்தன்மை அதன் பொருள் மற்றும் நடைமுறை ஆகிய இரு அம்சங்களிலிருந்தும் மதிப்பிடப்படுகிறது (வி.ஜி. ராவ் வழக்கு 1952)."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Analyze",
            "estimated_time_sec": 55,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 19", "Reasonable Restriction Test", "Grand Test"]
        },

        # Q62: Direct MCQ - Article 22 Detention Period Limits
        {
            "id": "FR_GT_062",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Medium",
            "question_type": "Direct MCQ",
            "question": {
                "en": "Under Article 22(4) of the Constitution of India, what is the maximum period for which a person can be held under preventive detention without obtaining the opinion of an Advisory Board?",
                "ta": "இந்திய அரசியலமைப்பின் 22(4) பிரிவின் கீழ், ஓர் ஆலோசனைக் குழுவின் (Advisory Board) அபிப்பிராயத்தைப் பெறாமல் ஒரு நபரை அதிகபட்சமாக எவ்வளவு காலம் தடுப்புக் காவலில் வைக்க முடியும்?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "3 months",
                    "ta": "3 மாதங்கள்"
                },
                {
                    "id": "B",
                    "en": "6 months",
                    "ta": "6 மாதங்கள்"
                },
                {
                    "id": "C",
                    "en": "2 months",
                    "ta": "2 மாதங்கள்"
                },
                {
                    "id": "D",
                    "en": "1 month",
                    "ta": "1 மாதம்"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "Under Article 22(4), no law providing for preventive detention shall authorize detention for a period longer than 3 months unless an Advisory Board (consisting of persons qualified to be High Court judges) reports sufficient cause for extended detention before expiry of 3 months.",
                "ta": "பிரிவு 22(4)-ன் கீழ், உயர் நீதிமன்ற நீதிபதியாகத் தகுதியுடையோரைக் கொண்ட ஆலோசனைக் குழு 3 மாதங்களுக்குள் போதுமான காரணம் உள்ளது என அறிக்கை அளிக்காவிட்டால் தடுப்புக் காவல் 3 மாதங்களுக்கு மிகக்கூடாது."
            },
            "why_not_others": {
                "A": {"en": "Correct. 3 months is the current enforceable limit under Article 22(4).", "ta": "சரி. 3 மாதங்கள் என்பது பிரிவு 22(4)-ன் கீழ் தற்போதைய நடைமுறை வரம்பாகும்."},
                "B": {"en": "Incorrect. 6 months is wrong.", "ta": "தவறு. 6 மாதங்கள் என்பது தவறானது."},
                "C": {"en": "Incorrect. Although 44th Amendment 1978 passed a provision to reduce it to 2 months, that provision HAS NOT BEEN BROUGHT INTO FORCE yet!", "ta": "தவறு. 44-வது திருத்தம் 2 மாதங்களாகக் குறைக்க வழிசெய்த போதிலும் அப்பிரிவு இன்னும் நடைமுறைக்கு வரவில்லை!"},
                "D": {"en": "Incorrect. 1 month is wrong.", "ta": "தவறு. 1 மாதம் என்பது தவறானது."}
            },
            "tnpsc_tip": {
                "en": "TNPSC TRAP: The 44th Amendment Act 1978 proposed reducing the maximum period from 3 months to 2 months under Art 22(4). However, this specific amendment HAS NOT been notified/enforced by government, so 3 MONTHS REMAINS THE IN-FORCE LEGAL LIMIT!",
                "ta": "TNPSC பொறி: 44-வது திருத்தச் சட்டம் 1978 தடுப்புக் காவல் வரம்பை 3-லிருந்து 2 மாதங்களாகக் குறைக்க முன்மொழிந்தது. ஆனால் அந்தத் திருத்தம் இன்னும் அமல்படுத்தப்படவில்லை, எனவே 3 மாதங்களே சட்டப்பூர்வ வரம்பாக நீடிக்கிறது!"
            },
            "revision_fact": {
                "en": "Advisory Board under Art 22(4) consists of persons who are, or have been, or are qualified to be appointed as Judges of a High Court.",
                "ta": "ஆலோசனைக் குழுவில் உயர் நீதிமன்ற நீதிபதியாக உள்ள, இருந்த அல்லது தகுதியுடைய நபர்கள் இடம்பெறுவர்."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Understand",
            "estimated_time_sec": 45,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 22(4)", "Preventive Detention Limit", "Grand Test"]
        },

        # Q63: Conceptual MCQ - Right to Silence vs Art 19(1)(a)
        {
            "id": "FR_GT_063",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Medium",
            "question_type": "Conceptual MCQ",
            "question": {
                "en": "Which of the following is correct regarding the 'Right to Silence' under the Constitution of India?",
                "ta": "இந்திய அரசியலமைப்பின் கீழ் உள்ள 'அமைதி காக்கும் உரிமை' (Right to Silence) குறித்து பின்வருவனவற்றுள் எது சரியானது?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "It is derived from both Article 19(1)(a) (Freedom of Speech includes right not to speak) and Article 20(3) (Protection against Self-Incrimination)",
                    "ta": "இது பிரிவு 19(1)(a) (பேச்சுரிமையில் பேசாமல் இருக்கும் உரிமையும் அடங்கும்) மற்றும் பிரிவு 20(3) (சுய சாட்சிய விலக்கு) ஆகிய இரண்டிலிருந்தும் பெறப்பட்டது"
                },
                {
                    "id": "B",
                    "en": "It is derived exclusively from Article 17 and Article 18",
                    "ta": "இது பிரிவு 17 மற்றும் பிரிவு 18-லிருந்து மட்டுமே பெறப்பட்டது"
                },
                {
                    "id": "C",
                    "en": "It is explicitly mentioned in Article 22(4) as a non-bailable right",
                    "ta": "இது பிரிவு 22(4)-ல் பிணையில் வர முடியாத உரிமையாக வெளிப்படையாகக் குறிப்பிடப்பட்டுள்ளது"
                },
                {
                    "id": "D",
                    "en": "It applies only to Members of Parliament during parliamentary debates under Article 105",
                    "ta": "இது பிரிவு 105-ன் கீழ் நாடாளுமன்ற விவாதங்களின் போது நாடாளுமன்ற உறுப்பினர்களுக்கு மட்டுமே பொருந்தும்"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "Right to silence has two dimensions: (1) Freedom of speech under Art 19(1)(a) includes freedom NOT to speak or express (Bijoe Emmanuel case), (2) In criminal law, Art 20(3) protects an accused from being compelled to testify against himself (Nandini Satpathy case).",
                "ta": "அமைதி காக்கும் உரிமை இரு பரிமாணங்களைக் கொண்டது: (1) 19(1)(a)-ல் பேசாமல் இருக்கும் சுதந்திரமும் அடங்கும் (பிஜோய் இம்மானுவேல் வழக்கு), (2) குற்றவியல் சட்டத்தில் 20(3) சுய சாட்சியத்திலிருந்து குற்றஞ்சாட்டப்பட்டவரைப் பாதுகாக்கிறது."
            },
            "why_not_others": {
                "A": {"en": "Correct. Right to silence derives from both 19(1)(a) free speech and 20(3) self-incrimination.", "ta": "சரி. அமைதி காக்கும் உரிமை 19(1)(a) மற்றும் 20(3) ஆகிய இரண்டிலிருந்தும் பெறப்பட்டது."},
                "B": {"en": "Incorrect. Articles 17 & 18 deal with untouchability and titles.", "ta": "தவறு. 17 & 18 தீண்டாமை மற்றும் பட்டங்கள் பற்றியவை."},
                "C": {"en": "Incorrect. Article 22(4) deals with preventive detention limit.", "ta": "தவறு. 22(4) தடுப்புக் காவல் வரம்பு பற்றியது."},
                "D": {"en": "Incorrect. Right to silence is available to all citizens.", "ta": "தவறு. அமைதி காக்கும் உரிமை அனைத்துக் குடிமக்களுக்கும் உண்டு."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: In Bijoe Emmanuel v. State of Kerala (1986), Supreme Court held that expulsion of 3 Jehovah's Witness students for standing up silently during National Anthem violated Article 19(1)(a) and Article 25.",
                "ta": "TNPSC குறிப்பு: பிஜோய் இம்மானுவேல் வழக்கில் (1986) தேசிய கீதத்தின் போது மரியாதையுடன் அமைதியாக நின்ற 3 மாணவர்கள் நீக்கப்பட்டது பிரிவு 19(1)(a) மற்றும் 25-ஐ மீறுகிறது எனப்பட்டது."
            },
            "revision_fact": {
                "en": "Proper respect is shown to the National Anthem by standing at attention. Compelling a person to sing against religious conscience violates Art 19(1)(a) and 25.",
                "ta": "தேசிய கீதத்திற்கு மரியாதையுடன் நிமிர்ந்து நிற்பதே போதுமானது. சம்மதமின்றி பாடக் கட்டாயப்படுத்துவது உரிமையை மீறும்."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Understand",
            "estimated_time_sec": 45,
            "pyq_similarity": "High",
            "tags": ["Polity", "Right to Silence", "Article 19(1)(a)", "Article 20(3)", "Grand Test"]
        },

        # Q64: Statement-Based - Article 21 Privacy & Telephone Tapping
        {
            "id": "FR_GT_064",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Medium",
            "question_type": "Statement-Based",
            "question": {
                "en": "Consider the following statements regarding telephone tapping and privacy under Article 21:\n1. In PUCL v. Union of India (1997), the Supreme Court held that telephone tapping infringes Article 21 (Right to Privacy) unless conducted under procedural safeguards.\n2. Telephone tapping also infringes Article 19(1)(a) (Freedom of Speech and Expression) unless covered by restrictions under Article 19(2).\n3. Government can tap telephones arbitrarily without written authorization during peacetime.\nWhich of the statements given above are correct?",
                "ta": "பிரிவு 21-ன் கீழ் தொலைபேசி ஒட்டுக் கேட்டல் மற்றும் தனியுரிமை பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. PUCL எதிர் இந்திய யூனியன் (1997) வழக்கில், நடைமுறைப் பாதுகாப்புகளின்றித் தொலைபேசியை ஒட்டுக் கேட்பது பிரிவு 21-ஐ (தனியுரிமை) மீறுகிறது என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது.\n2. பிரிவு 19(2)-ன் கீழ் கட்டுப்பாடுகளுக்குள் வராதவரை தொலைபேசி ஒட்டுக் கேட்டல் பிரிவு 19(1)(a)-ஐயும் (பேச்சுரிமை) மீறுகிறது.\n3. அமைதி காலத்தில் எழுத்துப்பூர்வ அனுமதியின்றி அரசாங்கம் தன்னிச்சையாகத் தொலைபேசியை ஒட்டுக் கேட்க முடியும்.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?"
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
                "en": "Statements 1 and 2 are correct. In PUCL case (1997), SC held phone tapping violates Art 21 & Art 19(1)(a) unless authorized under Section 5(2) of Indian Telegraph Act 1885 during public emergency or public safety. Statement 3 is INCORRECT: Arbitrary phone tapping is unconstitutional.",
                "ta": "கூற்றுகள் 1 மற்றும் 2 சரியானவை. PUCL வழக்கில் (1997) சட்டப்பூர்வ நடைமுறையின்றித் தொலைபேசி ஒட்டுக் கேட்பது பிரிவு 21 & 19(1)(a)-ஐ மீறுகிறது எனப்பட்டது. கூற்று 3 தவறானது: தன்னிச்சையான ஒட்டுக் கேட்டல் அரசியலமைப்புக்கு முரணானது."
            },
            "why_not_others": {
                "A": {"en": "Correct. Statements 1 and 2 are true; statement 3 is false.", "ta": "சரி. கூற்றுகள் 1 மற்றும் 2 சரியானவை; கூற்று 3 தவறானது."},
                "B": {"en": "Incorrect because statement 3 is false.", "ta": "தவறு, ஏனெனில் கூற்று 3 தவறானது."},
                "C": {"en": "Incorrect because statement 3 is false.", "ta": "தவறு, ஏனெனில் கூற்று 3 தவறானது."},
                "D": {"en": "Incorrect because statement 3 is false.", "ta": "தவறு, ஏனெனில் கூற்று 3 தவறானது."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: PUCL Telephone Tapping judgment (1997) mandated a Review Committee headed by Cabinet Secretary (Union) or Chief Secretary (State) to review phone tapping orders every 2 months.",
                "ta": "TNPSC குறிப்பு: PUCL தொலைபேசி ஒட்டுக் கேட்டல் தீர்ப்பு (1997) மத்திய அமைச்சரவைச் செயலாளர் / மாநிலத் தலைமைச் செயலாளர் தலைமையிலான மறுஆய்வுக் குழுவை அமைத்து உத்தரவுகளை 2 மாதங்களுக்கு ஒருமுறை மறுஆய்வு செய்யக் கட்டளையிட்டது."
            },
            "revision_fact": {
                "en": "Right to Privacy was upheld as a fundamental right under Article 21 by 9-judge bench in Puttaswamy (2017), affirming the PUCL decision.",
                "ta": "தனியுரிமை பிரிவு 21-ன் கீழ் அடிப்படை உரிமை என புட்டசுவாமி (2017) வழக்கில் 9 நீதிபதிகள் அமர்வால் உறுதி செய்யப்பட்டது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Analyze",
            "estimated_time_sec": 50,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 21", "Phone Tapping", "PUCL Case", "Grand Test"]
        },

        # Q65: Direct MCQ - Article 22 Right to Legal Practitioner
        {
            "id": "FR_GT_065",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Easy",
            "question_type": "Direct MCQ",
            "question": {
                "en": "Under Article 22(1) of the Constitution of India, an arrested person has the fundamental right to consult and be defended by a legal practitioner of their choice. From what moment does this right begin?",
                "ta": "இந்திய அரசியலமைப்பின் 22(1) பிரிவின் கீழ், கைது செய்யப்பட்ட ஒருவருக்குத் தான் விரும்பும் வழக்கறிஞரைக் கலந்தாலோசிக்கவும் அவர் மூலம் வாதாடவும் அடிப்படை உரிமை உண்டு. இந்த உரிமை எந்தக் கணத்திலிருந்து தொடங்குகிறது?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "From the moment of arrest",
                    "ta": "கைது செய்யப்பட்ட கணத்திலிருந்து"
                },
                {
                    "id": "B",
                    "en": "Only after charge sheet is filed in court",
                    "ta": "நீதிமன்றத்தில் குற்றப்பத்திரிகை தாக்கல் செய்யப்பட்ட பிறகு மட்டுமே"
                },
                {
                    "id": "C",
                    "en": "Only after the Magistrate grants bail",
                    "ta": "நீதிபதி பிணை வழங்கிய பிறகு மட்டுமே"
                },
                {
                    "id": "D",
                    "en": "Only after trial commences in Sessions Court",
                    "ta": "அமர்வு நீதிமன்றத்தில் விசாரணை தொடங்கிய பிறகு மட்டுமே"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "Under Article 22(1), the right to consult and be defended by a legal practitioner of choice begins immediately upon arrest. In D.K. Basu v. State of West Bengal (1997), SC laid down mandatory guidelines for arrest including right to meet lawyer during interrogation.",
                "ta": "பிரிவு 22(1)-ன் கீழ் வழக்கறிஞரைக் கலந்தாலோசித்து வாதாடும் உரிமை கைது செய்யப்பட்ட கணத்திலிருந்தே தொடங்குகிறது. டி.கே. பாசு வழக்கில் (1997) விசாரணையின் போது வழக்கறிஞரைச் சந்திக்கும் உரிமை உறுதி செய்யப்பட்டது."
            },
            "why_not_others": {
                "A": {"en": "Correct. Right to legal counsel begins immediately from the moment of arrest.", "ta": "சரி. வழக்கறிஞர் ஆலோசனை உரிமை கைது செய்யப்பட்ட கணத்திலிருந்தே தொடங்குகிறது."},
                "B": {"en": "Incorrect. Waiting for charge sheet denies prompt legal aid.", "ta": "தவறு. குற்றப்பத்திரிகை வரை காத்திருப்பது சட்ட உதவியை மறுப்பதாகும்."},
                "C": {"en": "Incorrect. Legal counsel is needed to apply for bail in the first place.", "ta": "தவறு. பிணை விண்ணப்பிக்கவே வழக்கறிஞர் தேவை."},
                "D": {"en": "Incorrect. Right applies during pre-trial detention as well.", "ta": "தவறு. விசாரணைக்கு முந்தைய காவலுக்கும் பொருந்தும்."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: D.K. Basu v. State of West Bengal (1996/1997) laid down 11 mandatory guidelines to be followed by police during arrest and detention to prevent custodial violence.",
                "ta": "TNPSC குறிப்பு: டி.கே. பாசு எதிர் மேற்கு வங்க அரசு வழக்கில் (1997) காவல் மரணங்களைத் தடுக்கக் கைதின் போது பின்பற்றப்பட வேண்டிய 11 கட்டாய வழிகாட்டுதல்கள் வகுக்கப்பட்டன."
            },
            "revision_fact": {
                "en": "Section 41D of CrPC explicitly gives an arrested person the right to meet an advocate of their choice during interrogation.",
                "ta": "CrPC பிரிவு 41D கைது செய்யப்பட்டவருக்கு விசாரணையின் போது தனது வழக்கறிஞரைச் சந்திக்கும் உரிமையை வழங்குகிறது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Remember",
            "estimated_time_sec": 35,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 22(1)", "Right to Lawyer", "DK Basu", "Grand Test"]
        },

        # Q66: Conceptual MCQ - Right against Exploitation Begar vs Compulsory Service
        {
            "id": "FR_GT_066",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Medium",
            "question_type": "Conceptual MCQ",
            "question": {
                "en": "Which of the following is an EXemption to Article 23 (Right against Exploitation / Forced Labour)?",
                "ta": "பிரிவு 23-க்கு (சுரண்டலுக்கு எதிரான உரிமை / கட்டாய வேலை) விதிவிலக்காக உள்ள பின்வருவனவற்றுள் எது?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "Compulsory military service or social service imposed by the State for public purposes under Article 23(2)",
                    "ta": "பிரிவு 23(2)-ன் கீழ் பொது நோக்கங்களுக்காக அரசால் விதிக்கப்படும் கட்டாய ராணுவ சேவை அல்லது சமூக சேவை"
                },
                {
                    "id": "B",
                    "en": "Forced labour imposed by private landlords on agricultural workers for debt recovery",
                    "ta": "கடன் வசூலுக்காக விவசாயத் தொழிலாளர்கள் மீது தனியார் நிலக்கிழார்களால் விதிக்கப்படும் கட்டாய வேலை"
                },
                {
                    "id": "C",
                    "en": "Unpaid domestic servitude mandated by local village panchayats",
                    "ta": "உள்ளூர் கிராம பஞ்சாயத்துகளால் கட்டாயப்படுத்தப்படும் ஊதியமற்ற வீட்டு வேலை"
                },
                {
                    "id": "D",
                    "en": "Forced human trafficking of women for commercial exploitation",
                    "ta": "வணிகச் சுரண்டலுக்காக பெண்களைக் கட்டாயமாக மனித வர்த்தகம் செய்தல்"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "Article 23(2) is the sole constitutional exception to Article 23(1). It permits the State to impose compulsory service for public purposes (like military conscription or national disaster relief) without discrimination on grounds ONLY of religion, race, caste or class.",
                "ta": "பிரிவு 23(2) பிரிவு 23(1)-ற்கான ஒரே அரசியலமைப்பு விதிவிலக்காகும். இது பொது நோக்கங்களுக்காகக் (ராணுவ சேவை, பேரிடர் நிவாரணம்) கட்டாயச் சேவையை விதிக்க அரசை அனுமதிக்கிறது."
            },
            "why_not_others": {
                "A": {"en": "Correct. State compulsory service for public purposes under 23(2) is a valid exception.", "ta": "சரி. பொது நோக்கங்களுக்காக அரசின் கட்டாயச் சேவை 23(2)-ன் கீழ் செல்லுபடியாகும் விதிவிலக்கு."},
                "B": {"en": "Incorrect. Debt bondage forced labour is strictly illegal under Bonded Labour System Act 1976.", "ta": "தவறு. கடனுக்கான கொத்தடிமை வேலை முற்றிலும் சட்டவிரோதமானது."},
                "C": {"en": "Incorrect. Panchayats cannot compel unpaid servitude.", "ta": "தவறு. பஞ்சாயத்துகள் ஊதியமற்ற வேலையைக் கட்டாயப்படுத்த முடியாது."},
                "D": {"en": "Incorrect. Human trafficking is a severely punishable offence.", "ta": "தவறு. மனித வர்த்தகம் கடுமையான குற்றமாகும்."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: When compulsory service is imposed under Art 23(2), the State is NOT bound to pay remuneration, provided it does not discriminate on forbidden grounds.",
                "ta": "TNPSC குறிப்பு: பிரிவு 23(2)-ன் கீழ் கட்டாய சேவை விதிக்கப்படும் போது, தடை செய்யப்பட்ட அடிப்படைகளில் பாகுபாடு காட்டாதவரை அரசு ஊதியம் வழங்கக் கடமைப்பட்டிருக்கவில்லை."
            },
            "revision_fact": {
                "en": "Article 23 protects individuals against both the State and private persons, unlike Article 19 which operates against the State.",
                "ta": "பிரிவு 23 அரசு மற்றும் தனியார் தனிநபர்கள் இருவருக்கு எதிராகவும் நபர்களைப் பாதுகாக்கிறது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Understand",
            "estimated_time_sec": 45,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 23(2)", "Compulsory Military Service", "Grand Test"]
        },

        # Q67: Hard / Analytical - Freedom of Speech & Contempt of Court
        {
            "id": "FR_GT_067",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Hard",
            "question_type": "Hard / Analytical",
            "question": {
                "en": "Regarding 'Contempt of Court' as a reasonable restriction under Article 19(2) and Articles 129/215, which of the following statements is INCORRECT?",
                "ta": "பிரிவு 19(2) மற்றும் பிரிவுகள் 129/215-ன் கீழ் உள்ள நியாயமான கட்டுப்பாடான 'நீதிமன்ற அவமதிப்பு' பற்றி பின்வரும் கூற்றுகளில் எது தவறானது?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "Truth was introduced as a valid defense in criminal contempt by the Contempt of Courts (Amendment) Act 2006, provided it is in public interest and bona fide",
                    "ta": "2006-ன் நீதிமன்ற அவமதிப்பு (திருத்தச்) சட்டத்தின் மூலம் பொது நலன் மற்றும் நன்னம்பிக்கை இருந்தால் 'உண்மை' என்பது குற்றவியல் அவமதிப்பில் செல்லுபடியாகும் தற்காப்பாக அறிமுகப்படுத்தப்பட்டது"
                },
                {
                    "id": "B",
                    "en": "Fair and reasonable criticism of a judicial act does NOT constitute contempt of court",
                    "ta": "நீதிமன்ற நடவடிக்கையை நேர்மையாகவும் நியாயமாகவும் விமர்சிப்பது நீதிமன்ற அவமதிப்பாகாது"
                },
                {
                    "id": "C",
                    "en": "The Supreme Court and High Courts derive their power to punish for contempt directly from Articles 129 and 215 of the Constitution respectively",
                    "ta": "உச்ச நீதிமன்றமும் உயர் நீதிமன்றங்களும் அவமதிப்புக்குத் தண்டிக்கும் அதிகாரத்தை முறையே அரசியலமைப்பின் 129 மற்றும் 215 பிரிவுகளிலிருந்து நேரடியாகப் பெறுகின்றன"
                },
                {
                    "id": "D",
                    "en": "The expression 'Contempt of Court' is explicitly defined in detail within Article 19(2) of the Constitution",
                    "ta": "'நீதிமன்ற அவமதிப்பு' என்ற சொற்றொடர் அரசியலமைப்பின் 19(2) பிரிவுக்குள் விரிவாக வெளிப்படையாக வரையறுக்கப்பட்டுள்ளது"
                }
            ],
            "correct_answer": "D",
            "explanation": {
                "en": "Statement D is INCORRECT (making it the correct answer). The term 'Contempt of Court' is NOT defined in the Constitution. It is defined in the Contempt of Courts Act, 1971 into Civil Contempt and Criminal Contempt.",
                "ta": "கூற்று D தவறானது (எனவே இது சரியான விடை). 'நீதிமன்ற அவமதிப்பு' என்ற சொல் அரசியலமைப்பில் வரையறுக்கப்படவில்லை. இது 1971-ன் நீதிமன்ற அவமதிப்புச் சட்டத்தில்தான் வரையறுக்கப்பட்டுள்ளது."
            },
            "why_not_others": {
                "A": {"en": "Incorrect answer (correct statement). 2006 Amendment Act allowed Truth as a valid defense under Section 13(b).", "ta": "தவறான விடை (சரியான கூற்று). 2006 திருத்தச் சட்டம் உண்மையை ஒரு தற்காப்பாக அனுமதித்தது."},
                "B": {"en": "Incorrect answer (correct statement). Fair criticism of judgment is not contempt.", "ta": "தவறான விடை (சரியான கூற்று). நியாயமான விமர்சனம் அவமதிப்பல்ல."},
                "C": {"en": "Incorrect answer (correct statement). SC (Art 129) and HC (Art 215) are courts of record with inherent contempt power.", "ta": "தவறான விடை (சரியான கூற்று). 129 மற்றும் 215 பிரிவுகள் பதிவு நீதிமன்றங்களாக அவமதிப்பு அதிகாரம் அளிக்கின்றன."},
                "D": {"en": "Correct answer (incorrect statement). Contempt of Court is NOT defined in the Constitution.", "ta": "சரியான விடை (தவறான கூற்று). நீதிமன்ற அவமதிப்பு அரசியலமைப்பில் வரையறுக்கப்படவில்லை."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Trap: Contempt of Courts Act 1971 divides contempt into Civil Contempt (willful disobedience of court order) and Criminal Contempt (scandalizing court, prejudicing judicial proceeding, interfering with administration of justice).",
                "ta": "TNPSC பொறி: 1971 அவமதிப்புச் சட்டம் அவமதிப்பை உரிமையியல் அவமதிப்பு (உத்தரவை மீறுதல்) மற்றும் குற்றவியல் அவமதிப்பு (நீதிமன்றத்தைக் சிறுமைப்படுத்துதல்) என இருவகையாகப் பிரிக்கிறது."
            },
            "revision_fact": {
                "en": "In Prashant Bhushan Contempt Case (2020), Supreme Court reaffirmed its power under Article 129 as a Court of Record.",
                "ta": "பிரசாந்த் பூஷண் அவமதிப்பு வழக்கில் (2020) உச்ச நீதிமன்றம் பிரிவு 129-ன் கீழ் தனது பதிவேட்டு நீதிமன்ற அதிகாரத்தை மீண்டும் உறுதிப்படுத்தியது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Analyze",
            "estimated_time_sec": 60,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 19(2)", "Contempt of Court", "Grand Test"]
        },

        # Q68: Direct MCQ - Right to Speedy Trial Art 21
        {
            "id": "FR_GT_068",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Easy",
            "question_type": "Direct MCQ",
            "question": {
                "en": "In which landmark public interest litigation case did the Supreme Court declare the 'Right to Speedy Trial' to be a Fundamental Right implicit under Article 21 for undertrial prisoners?",
                "ta": "விசாரணை கைதிகளுக்குப் பிரிவு 21-ன் கீழ் 'விரைவு விசாரணை உரிமை' என்பது ஒரு மறைமுகமான அடிப்படை உரிமை என்று உச்ச நீதிமன்றம் எந்த முக்கிய பொதுநல வழக்குத் தீர்ப்பில் அறிவித்தது?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "Hussainara Khatoon v. Home Secretary, State of Bihar (1979)",
                    "ta": "ஹுசைனாரா கத்தூன் எதிர் பீகார் உள்துறைச் செயலாளர் (1979)"
                },
                {
                    "id": "B",
                    "en": "A.K. Roy v. Union of India (1982)",
                    "ta": "ஏ.கே. ராய் எதிர் இந்திய யூனியன் (1982)"
                },
                {
                    "id": "C",
                    "en": "Prem Shankar Shukla v. Delhi Administration (1980)",
                    "ta": "பிரேம் சங்கர் சுக்லா எதிர் டெல்லி நிர்வாகம் (1980)"
                },
                {
                    "id": "D",
                    "en": "Bachan Singh v. State of Punjab (1980)",
                    "ta": "பச்சன் சிங் எதிர் பஞ்சாப் அரசு (1980)"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "In Hussainara Khatoon v. Home Secretary Bihar (1979), PIL filed by Kapila Hingorani led to SC declaring right to speedy trial as a fundamental right under Art 21, resulting in the release of over 40,000 undertrial prisoners.",
                "ta": "ஹுசைனாரா கத்தூன் வழக்கில் (1979) கபிலா ஹிங்கோராணி தாக்கல் செய்த PIL மூலம் உச்ச நீதிமன்றம் விரைவு விசாரணை உரிமையைப் பிரிவு 21-ன் கீழ் அடிப்படை உரிமையாக்கியது, 40,000-க்கும் மேற்பட்ட விசாரணை கைதிகள் விடுவிக்கப்பட்டனர்."
            },
            "why_not_others": {
                "A": {"en": "Correct. Hussainara Khatoon case established Right to Speedy Trial.", "ta": "சரி. ஹுசைனாரா கத்தூன் வழக்கு விரைவு விசாரணை உரிமையை நிறுவியது."},
                "B": {"en": "Incorrect. A.K. Roy case dealt with National Security Act 1980.", "ta": "தவறு. ஏ.கே. ராய் வழக்கு தேசியப் பாதுகாப்புச் சட்டம் பற்றியது."},
                "C": {"en": "Incorrect. Prem Shankar Shukla case dealt with prohibition of handcuffing prisoners.", "ta": "தவறு. பிரேம் சங்கர் சுக்லா வழக்கு கைவிலங்கு போடுவதற்கு எதிரான உரிமை பற்றியது."},
                "D": {"en": "Incorrect. Bachan Singh case established 'Rarest of Rare cases' doctrine for death penalty.", "ta": "தவறு. பச்சன் சிங் வழக்கு மரண தண்டனைக்கான 'அரிதிலும் அரிதான வழக்கு' கோட்பாடு பற்றியது."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: Kapila Hingorani is known as the 'Mother of Public Interest Litigation (PIL)' in India for filing the Hussainara Khatoon petition.",
                "ta": "TNPSC குறிப்பு: ஹுசைனாரா கத்தூன் மனுவைத் தாக்கல் செய்த கபிலா ஹிங்கோராணி இந்தியாவில் 'பொதுநல வழக்கின் தாய்' (Mother of PIL) என அழைக்கப்படுகிறார்."
            },
            "revision_fact": {
                "en": "Bachan Singh v. State of Punjab (1980) held that death penalty does not violate Article 21 if awarded in the 'rarest of rare cases'.",
                "ta": "பச்சன் சிங் வழக்கில் (1980) 'அரிதிலும் அரிதான வழக்குகளில்' வழங்கப்படும் மரண தண்டனை பிரிவு 21-ஐ மீறாது எனக் கூறப்பட்டது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Remember",
            "estimated_time_sec": 35,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 21", "Speedy Trial", "PIL", "Grand Test"]
        },

        # Q69: Conceptual MCQ - Right against Handcuffing Art 21
        {
            "id": "FR_GT_069",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Medium",
            "question_type": "Conceptual MCQ",
            "question": {
                "en": "In Prem Shankar Shukla v. Delhi Administration (1980), the Supreme Court held that routinely handcuffing prisoners violates Article 21. Under what exceptional circumstances is handcuffing legally permissible?",
                "ta": "பிரேம் சங்கர் சுக்லா எதிர் டெல்லி நிர்வாகம் (1980) வழக்கில், சிறைவாசிகளுக்கு வழக்கமாகக் கைவிலங்கு போடுவது பிரிவு 21-ஐ மீறுகிறது என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது. எந்த விதிவிலக்கான சூழ்நிலைகளில் கைவிலங்கு போடுவது சட்டப்பூர்வமாக அனுமதிக்கப்படுகிறது?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "Only when there is a clear and present danger of the prisoner escaping or resorting to violence, with reasons recorded in writing",
                    "ta": "சிறைவாசி தப்பிச் செல்ல அல்லது வன்முறையில் ஈடுபடத் தெளிவான மற்றும் உடனடி அபாயம் இருந்து, அதற்கான காரணங்கள் எழுத்துப்பூர்வமாகப் பதிவு செய்யப்படும் போது மட்டுமே"
                },
                {
                    "id": "B",
                    "en": "Whenever the police officer in charge deems it convenient during transit",
                    "ta": "பயணத்தின் போது காவல் அதிகாரி வசதியானது எனக் கருதும்போதெல்லாம்"
                },
                {
                    "id": "C",
                    "en": "For all persons accused of non-bailable offences automatically",
                    "ta": "பிணையில் வர முடியாத குற்றங்களில் கைதான அனைத்து நபர்களுக்கும் தானாகவே"
                },
                {
                    "id": "D",
                    "en": "Whenever the prisoner belongs to a particular political party",
                    "ta": "சிறைவாசி ஒரு குறிப்பிட்ட அரசியல் கட்சியைச் சேர்ந்தவராக இருக்கும்போதெல்லாம்"
                }
            ],
            "correct_answer": "A",
            "explanation": {
                "en": "In Prem Shankar Shukla (1980) and Citizen for Democracy v. State of Assam (1995), SC held that handcuffing is prima facie inhuman and unreasonable under Art 21. It can be used ONLY when there is clear risk of escape or violence, recorded in writing and approved by Magistrate.",
                "ta": "பிரேம் சங்கர் சுக்லா வழக்கில் (1980) கைவிலங்கு போடுவது பிரிவு 21-க்கு எதிரானது எனப்பட்டது. தப்பிக்கும் அல்லது வன்முறை அபாயம் இருந்து எழுத்துப்பூர்வமாகப் பதிவு செய்யப்பட்டு நீதிபதியால் ஒப்புதல் அளிக்கப்பட்டால் மட்டுமே இடலாம்."
            },
            "why_not_others": {
                "A": {"en": "Correct. Handcuffing requires recorded reasons of escape risk and judicial scrutiny.", "ta": "சரி. தப்பிக்கும் அபாயம் பற்றிய எழுத்துப்பூர்வக் காரணம் தேவை."},
                "B": {"en": "Incorrect. Police convenience is not a valid ground for handcuffing.", "ta": "தவறு. காவல்துறை வசதி செல்லுபடியாகும் காரணமல்ல."},
                "C": {"en": "Incorrect. Automatic handcuffing for non-bailable offences is unconstitutional.", "ta": "தவறு. தானியங்கி கைவிலங்கு அரசியலமைப்புக்கு முரணானது."},
                "D": {"en": "Incorrect. Political affiliation is irrelevant.", "ta": "தவறு. அரசியல் சார்பு தொடர்பற்றது."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Tip: Sunil Batra v. Delhi Administration (1978) held that putting bar fetters (leg irons) on prisoners without justification violates Article 21.",
                "ta": "TNPSC குறிப்பு: சுனில் பத்ரா வழக்கில் (1978) சிறைவாசிகளுக்குக் காரணமின்றி கால் விலங்கு போடுவது பிரிவு 21-ஐ மீறுகிறது எனப்பட்டது."
            },
            "revision_fact": {
                "en": "Human dignity is the core value underlying Article 21, protecting prisoners from torture and degrading treatment.",
                "ta": "மனிதக் கண்ணியமே பிரிவு 21-ன் அடிப்படை மதிப்பீடாகும், இது சித்திரவதையிலிருந்து சிறைவாசிகளைப் பாதுகாக்கிறது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Understand",
            "estimated_time_sec": 45,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 21", "Handcuffing", "Prisoners Rights", "Grand Test"]
        },

        # Q70: Statement-Based - Article 20 Self-Incrimination Scope
        {
            "id": "FR_GT_070",
            "subject": "Polity",
            "topic": "Fundamental Rights",
            "difficulty": "Hard",
            "question_type": "Statement-Based",
            "question": {
                "en": "Consider the following statements regarding the protection against self-incrimination under Article 20(3):\n1. Article 20(3) protects a person accused of an offence from being compelled to give oral or written testimony against themselves.\n2. Compelling an accused to give specimen handwriting, signature, or blood samples violates Article 20(3).\n3. Protection under Article 20(3) extends to civil proceedings as well as administrative tax inquiries.\nWhich of the statements given above is/are correct?",
                "ta": "பிரிவு 20(3)-ன் கீழ் உள்ள சுய சாட்சிய விலக்கு பாதுகாப்பு பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. குற்றஞ்சாட்டப்பட்ட ஒரு நபர் தனக்கு எதிராகத் தானே வாய்மொழி அல்லது எழுத்துப்பூர்வச் சாட்சியம் அளிப்பதற்குக் கட்டாயப்படுத்துவதிலிருந்து பிரிவு 20(3) பாதுகாக்கிறது.\n2. குற்றஞ்சாட்டப்பட்ட நபரை மாதிரி கையெழுத்து, ஒப்பம் அல்லது ரத்த மாதிரி அளிக்கக் கட்டாயப்படுத்துவது பிரிவு 20(3)-ஐ மீறுகிறது.\n3. பிரிவு 20(3)-ன் கீழ் உள்ள பாதுகாப்பு உரிமையியல் வழக்குகள் மற்றும் நிர்வாக வரி விசாரணைகளுக்கும் பொருந்தும்.\nமேற்கூறிய கூற்றுகளில் எது/எவை சரியானவை?"
            },
            "options": [
                {
                    "id": "A",
                    "en": "1 only",
                    "ta": "1 மட்டுமே"
                },
                {
                    "id": "B",
                    "en": "1 and 2 only",
                    "ta": "1 மற்றும் 2 மட்டுமே"
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
            "correct_answer": "A",
            "explanation": {
                "en": "Statement 1 is correct. Statement 2 is INCORRECT: In Kathi Kalu Oghad (1961), SC held specimen handwriting, signatures, or physical samples do NOT violate Art 20(3). Statement 3 is INCORRECT: Art 20(3) applies ONLY to persons accused of criminal offences, NOT to civil cases or administrative inquiries (such as under Customs or Income Tax Acts).",
                "ta": "கூற்று 1 மட்டுமே சரி. கூற்று 2 தவறு: கதி காலு ஓகத் வழக்கில் (1961) மாதிரி கையெழுத்து, ரத்த மாதிரி அளிப்பது பிரிவு 20(3)-ஐ மீறாது எனப்பட்டது. கூற்று 3 தவறு: பிரிவு 20(3) குற்றவியல் வழக்குகளுக்கு மட்டுமே பொருந்தும், உரிமையியல்/சுங்க/வரி விசாரணைகளுக்குப் பொருந்தாது."
            },
            "why_not_others": {
                "A": {"en": "Correct. Statement 1 is true; statements 2 and 3 are false.", "ta": "சரி. கூற்று 1 மட்டுமே சரியானது; கூற்றுகள் 2 மற்றும் 3 தவறானவை."},
                "B": {"en": "Incorrect because statement 2 is false.", "ta": "தவறு, ஏனெனில் கூற்று 2 தவறானது."},
                "C": {"en": "Incorrect because statements 2 and 3 are false.", "ta": "தவறு, ஏனெனில் கூற்றுகள் 2 மற்றும் 3 தவறானவை."},
                "D": {"en": "Incorrect because statements 2 and 3 are false.", "ta": "தவறு, ஏனெனில் கூற்றுகள் 2 மற்றும் 3 தவறானவை."}
            },
            "tnpsc_tip": {
                "en": "TNPSC Trap: Three requirements for Article 20(3) protection: (1) Person must be accused of an offence, (2) There must be compulsion, (3) Compulsion must be to give testimony against oneself.",
                "ta": "TNPSC பொறி: பிரிவு 20(3) பாதுகாப்பிற்கான 3 நிபந்தனைகள்: (1) நபர் குற்றஞ்சாட்டப்பட்டிருக்க வேண்டும், (2) கட்டாயப்படுத்தப்பட்டிருக்க வேண்டும், (3) கட்டாயம் தனக்கெதிரான சாட்சியத்திற்கு இருக்க வேண்டும்."
            },
            "revision_fact": {
                "en": "State of Bombay v. Kathi Kalu Oghad (1961) distinguished between 'to be a witness' (testimonial evidence) and furnishing material/physical evidence.",
                "ta": "கதி காலு ஓகத் வழக்கின் மூலம் 'சாட்சியாக இருப்பது' (வாய்மொழி சாட்சியம்) மற்றும் உடற்பொருள்களை வழங்குவது வேறுபடுத்தப்பட்டது."
            },
            "source_reference": ["M. Laxmikanth - Indian Polity"],
            "bloom_level": "Analyze",
            "estimated_time_sec": 65,
            "pyq_similarity": "High",
            "tags": ["Polity", "Article 20(3)", "Self Incrimination", "Grand Test"]
        }
    ]
    return questions
