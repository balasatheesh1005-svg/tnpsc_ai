import json
import os

questions = [
    # 1. Advanced Conceptual - Popular Sovereignty
    {
        "id": "PRE_H_001",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Advanced Conceptual",
        "question": {
            "en": "The phrase 'We, the People of India' in the Preamble establishes the doctrine of 'Popular Sovereignty'. Which of the following is the most precise constitutional implication of this doctrine in the Indian legal framework?",
            "ta": "முகவுரையில் உள்ள 'இந்திய மக்களாகிய நாம்' என்ற தொடர் 'மக்களின் இறையாண்மை' கோட்பாட்டை நிறுவுகிறது. இந்திய சட்ட அமைப்பில் இக்கோட்பாட்டின் மிகத் துல்லியமான அரசியலமைப்பு விளைவு எது?"
        },
        "options": [
            {
                "id": "A",
                "en": "The ultimate source of constitutional authority resides in the collective political sovereignty of the people, making the Constitution supreme over all organs created by it.",
                "ta": "அரசியலமைப்பு அதிகாரத்தின் இறுதி மூலம் மக்களின் கூட்டு அரசியல் இறையாண்மையில் உள்ளது; இதனால் அரசியலமைப்பு அது உருவாக்கிய அனைத்து உறுப்புகளை விடவும் மேலானது."
            },
            {
                "id": "B",
                "en": "Parliament possesses absolute legal sovereignty, permitting it to alter any provision of the Constitution without judicial interference.",
                "ta": "பாராளுமன்றம் முழுமையான சட்ட இறையாண்மையைக் கொண்டுள்ளது; இதனால் நீதித்துறை தலையீடின்றி அரசியலமைப்பின் எந்த விதியையும் மாற்ற அனுமதிக்கிறது."
            },
            {
                "id": "C",
                "en": "The legal validity of the Constitution is derived entirely from the Indian Independence Act, 1947 passed by the British Parliament.",
                "ta": "அரசியலமைப்பின் சட்டபூர்வ செல்லுபடியாகும் தன்மை முற்றிலும் பிரிட்டிஷ் பாராளுமன்றத்தால் நிறைவேற்றப்பட்ட 1947 இந்திய சுதந்திரச் சட்டத்திலிருந்து பெறப்பட்டது."
            },
            {
                "id": "D",
                "en": "Laws enacted by Parliament automatically supersede constitutional provisions if supported by a two-thirds referendum of voters.",
                "ta": "வாக்காளர்களின் மூன்றில் இரண்டு பங்கு பொதுவாக்கெடுப்பு ஆதரித்தால், பாராளுமன்றத்தால் இயற்றப்பட்ட சட்டங்கள் தானாகவே அரசியலமைப்பு விதிகளை விட மேலோங்கும்."
            }
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Popular Sovereignty signifies that the Constitution derives its authority, legitimacy, and sanction from the people of India. Consequently, the Constitution—not Parliament or the Executive—is the supreme law of the land (Constitutional Supremacy), and all organs function within its limits.",
            "ta": "மக்களின் இறையாண்மை என்பது அரசியலமைப்பு தனது அதிகாரம், சட்டபூர்வத்தன்மை மற்றும் அனுமதியை இந்திய மக்களிடமிருந்தே பெறுகிறது என்பதைக் குறிக்கிறது. இதன் விளைவாக, நாடாளுமன்றமோ அல்லது நிர்வாகமோ அல்ல, அரசியலமைப்பே நாட்டின் உயர்ந்த சட்டமாகும் (அரசியலமைப்பு மேலாதிக்கம்)."
        },
        "why_not_others": {
            "A": {"en": "Correct. Popular Sovereignty grounds Constitutional Supremacy over all three organs of State.", "ta": "சரி. மக்களின் இறையாண்மை அரசின் மூன்று உறுப்புகளையும் விட அரசியலமைப்பு மேலாதிக்கத்தை நிறுவுகிறது."},
            "B": {"en": "Incorrect. India has Constitutional Supremacy, not British-style Parliamentary Sovereignty.", "ta": "தவறு. இந்தியாவில் அரசியலமைப்பு மேலாதிக்கம் உள்ளது, பிரிட்டிஷ் பாணி பாராளுமன்ற இறையாண்மை இல்லை."},
            "C": {"en": "Incorrect. The Constituent Assembly repealed the Indian Independence Act 1947 under Art 395; authority derives from the people.", "ta": "தவறு. அரசியலமைப்புச் சபை 1947 இந்திய சுதந்திரச் சட்டத்தை உறுப்பு 395 இன் கீழ் ரத்து செய்தது; அதிகாரம் மக்களிடமிருந்தே பெறப்படுகிறது."},
            "D": {"en": "Incorrect. The Indian Constitution does not provide for national referendums to override constitutional provisions.", "ta": "தவறு. இந்திய அரசியலமைப்பு விதிகளை மேலோங்குவதற்கு தேசிய பொதுவாக்கெடுப்புக்கு வழிகோலவில்லை."}
        },
        "tnpsc_tip": {"en": "Popular Sovereignty = Source of authority is 'The People'. It leads to Constitutional Supremacy (NOT Parliamentary Supremacy).", "ta": "மக்களின் இறையாண்மை = அதிகாரத்தின் மூலம் 'மக்களே'. இது அரசியலமைப்பு மேலாதிக்கத்திற்கு வழிவகுக்கிறது (பாராளுமன்ற மேலாதிக்கம் அல்ல)."},
        "revision_fact": {"en": "Art 395 of the Constitution repealed the Indian Independence Act, 1947 and the Government of India Act, 1935, cementing popular sovereignty.", "ta": "அரசியலமைப்பின் உறுப்பு 395 இந்திய சுதந்திரச் சட்டம் 1947 மற்றும் இந்திய அரசுச் சட்டம் 1935 ஆகியவற்றை ரத்து செய்து மக்களின் இறையாண்மையை உறுதிப்படுத்தியது."},
        "source_reference": ["Preamble Notes Part 1", "M. Laxmikanth"],
        "bloom_level": "Analyze",
        "estimated_time_sec": 75,
        "pyq_similarity": "High",
        "tags": ["Preamble", "Popular Sovereignty", "We the People", "Constitutional Supremacy"]
    },

    # 2. Advanced Conceptual - Internal vs External Sovereignty
    {
        "id": "PRE_H_002",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Advanced Conceptual",
        "question": {
            "en": "Regarding the term 'Sovereign' in the Preamble, which of the following statements correctly reconciles India's membership in international bodies (like the Commonwealth or United Nations) with its constitutional sovereignty?",
            "ta": "முகவுரையில் உள்ள 'இறையாண்மை' என்ற சொல் தொடர்பாக, சர்வதேச அமைப்புகளில் (காமன்வெல்த் அல்லது ஐக்கிய நாடுகள் சபை போன்றவை) இந்தியாவின் உறுப்பினர்தன்மையை அதன் அரசியலமைப்பு இறையாண்மையுடன் சரியாக ஒப்பிட்டு சரிபார்க்கும் கூற்று எது?"
        },
        "options": [
            {
                "id": "A",
                "en": "Membership in international bodies is a voluntary extra-constitutional association that does not restrict India's supreme legal authority to legislate or govern internally and externally.",
                "ta": "சர்வதேச அமைப்புகளில் உறுப்பினராக இருப்பது ஒரு தன்னார்வ அரசியலமைப்புக்கு அப்பாற்பட்ட தொடர்பாகும்; இது உள்நாட்டிலும் வெளிநாட்டிலும் சட்டமியற்றவோ அல்லது நிர்வகிக்கவோ இந்தியாவின் உயர்ந்த சட்ட அதிகாரத்தைக் கட்டுப்படுத்தாது."
            },
            {
                "id": "B",
                "en": "India surrendered a portion of its external sovereignty to the British Crown upon joining the Commonwealth in 1949.",
                "ta": "1949 இல் காமன்வெல்த்தில் சேர்ந்ததன் மூலம் இந்தியா தனது வெளி இறையாண்மையின் ஒரு பகுதியை பிரிட்டிஷ் மகுடத்திடம் ஒப்படைத்தது."
            },
            {
                "id": "C",
                "en": "UN Security Council resolutions automatically repeal inconsistent Indian Parliamentary statutes without requiring domestic legislation.",
                "ta": "ஐநா பாதுகாப்பு கவுன்சில் தீர்மானங்கள் உள்நாட்டு சட்டங்கள் ஏதுமின்றி முரண்பாடான இந்திய நாடாளுமன்ற சட்டங்களை தானாகவே ரத்து செய்கின்றன."
            },
            {
                "id": "D",
                "en": "Sovereignty requires complete political isolation, rendering any binding international treaty unconstitutional per se.",
                "ta": "இறையாண்மைக்கு முழுமையான அரசியல் தனிமைப்படுத்தல் தேவைப்படுகிறது; இதனால் பிணைப்புறுத்தும் எந்தவொரு சர்வதேச ஒப்பந்தமும் அரசியலமைப்புக்கு முரணானது."
            }
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "India is a sovereign state—it is neither a dependency nor a dominion of any other nation. Although India accepted the King as Head of the Commonwealth in 1949, this declaration was a voluntary agreement outside the Constitution and does not impair India's full internal and external sovereignty.",
            "ta": "இந்தியா ஒரு இறையாண்மையுள்ள அரசு - அது வேறு எந்த நாட்டின் கட்டுப்பாட்டிலோ அல்லது டொமினியனாகவோ இல்லை. 1949 இல் காமன்வெல்த்தின் தலைவராக மன்னரை இந்தியா ஏற்றுக்கொண்ட போதிலும், இந்த அறிவிப்பு அரசியலமைப்புக்கு அப்பாற்பட்ட தன்னார்வ ஒப்பந்தமாகும்; இது இந்தியாவின் முழுமையான உள் மற்றும் வெளி இறையாண்மையைப் பாதிக்காது."
        },
        "why_not_others": {
            "A": {"en": "Correct. Commonwealth/UN membership is voluntary and does not legally curtail state sovereignty.", "ta": "சரி. காமன்வெல்த்/ஐநா உறுப்பினர்தன்மை தன்னார்வமானது, நாட்டின் இறையாண்மையை சட்டப்பூர்வமாக சுருக்காது."},
            "B": {"en": "Incorrect. India did not surrender any sovereignty; the Crown is merely a symbolic head of the association.", "ta": "தவறு. இந்தியா எந்த இறையாண்மையையும் ஒப்படைக்கவில்லை; மன்னர் காமன்வெல்த்தின் குறியீட்டுத் தலைவர் மட்டுமே."},
            "C": {"en": "Incorrect. International treaties/resolutions require domestic enabling legislation under Article 253 to be enforceable in Indian courts.", "ta": "தவறு. சர்வதேச ஒப்பந்தங்கள் இந்திய நீதிமன்றங்களில் அமல்படுத்தப்பட உறுப்பு 253 இன் கீழ் உள்நாட்டுச் சட்டம் தேவை."},
            "D": {"en": "Incorrect. Sovereignty includes the positive power to enter treaties and international agreements voluntarily.", "ta": "தவறு. இறையாண்மை என்பது தன்னார்வமாக ஒப்பந்தங்களை மேற்கொள்ளும் நேர்மறை அதிகாரத்தையும் உள்ளடக்கியது."}
        },
        "tnpsc_tip": {"en": "Commonwealth membership (1949) does NOT affect Indian Sovereignty. Being sovereign means India can acquire foreign territory or cede territory to a foreign state.", "ta": "காமன்வெல்த் உறுப்பினர்தன்மை (1949) இந்திய இறையாண்மையைப் பாதிக்காது. இறையாண்மை என்பது அந்நிய நிலப்பரப்பைக் கையகப்படுத்த அல்லது விட்டுக் கொடுக்க அதிகாரமளிக்கிறது."},
        "revision_fact": {"en": "As a sovereign state, India can either acquire a foreign territory or cede a part of its territory in favour of a foreign state.", "ta": "ஒரு இறையாண்மையுள்ள அரசாக, இந்தியா ஒரு அயல்நாட்டு நிலப்பரப்பைக் கையகப்படுத்தலாம் அல்லது தனது நிலப்பரப்பின் ஒரு பகுதியை அயல்நாட்டிற்கு விட்டுக் கொடுக்கலாம்."},
        "source_reference": ["Preamble Notes Part 1", "M. Laxmikanth"],
        "bloom_level": "Analyze",
        "estimated_time_sec": 75,
        "pyq_similarity": "High",
        "tags": ["Preamble", "Sovereign", "Commonwealth", "External Sovereignty"]
    },

    # 3. Advanced Conceptual - Democratic Socialism vs Marxist Socialism
    {
        "id": "PRE_H_003",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Advanced Conceptual",
        "question": {
            "en": "The Preamble envisions a 'Socialist' state. How does Indian 'Democratic Socialism' fundamentally differ from classic 'State/Marxist Socialism'?",
            "ta": "முகவுரை ஒரு 'சமதர்ம' அரசை முன்மொழிகிறது. இந்திய 'ஜனநாயக சோசலிசம்' பாரம்பரிய 'அரசு/மார்க்சிய சோசலிசத்திலிருந்து' எவ்வாறு அடிப்படையில் வேறுபடுகிறது?"
        },
        "options": [
            {
                "id": "A",
                "en": "Indian Democratic Socialism favors a complete abolition of private property and total state monopoly over all means of production.",
                "ta": "இந்திய ஜனநாயக சோசலிசம் தனியார் சொத்துரிமையை முற்றிலும் ஒழிப்பதையும் உற்பத்தி சாதனங்கள் அனைத்தின் மீதும் முழுமையான அரசு ஏகபோகத்தையும் ஆதரிக்கிறது."
            },
            {
                "id": "B",
                "en": "Indian Democratic Socialism envisions a mixed economy where public and private sectors co-exist side-by-side to end poverty, ignorance, and inequality.",
                "ta": "இந்திய ஜனநாயக சோசலிசம் வறுமை, அறியாமை மற்றும் சமத்துவமின்மையை ஒழிக்க பொது மற்றும் தனியார் துறைகள் அருகருகே இணைந்து செயல்படும் கலப்பு பொருளாதாரத்தை முன்மொழிகிறது."
            },
            {
                "id": "C",
                "en": "Marxist Socialism emphasizes parliamentary democratic means, whereas Democratic Socialism relies on violent proletarian revolution.",
                "ta": "மார்க்சிய சோசலிசம் பாராளுமன்ற ஜனநாயக வழிகளை வலியுறுத்துகிறது, ஆனால் ஜனநாயக சோசலிசம் வன்முறை பாட்டாளி வர்க்கப் புரட்சியை நம்பியுள்ளது."
            },
            {
                "id": "D",
                "en": "Democratic Socialism applies exclusively to agrarian land reforms, leaving industrial sectors entirely unregulated.",
                "ta": "ஜனநாயக சோசலிசம் வேளாண் நில சீர்திருத்தங்களுக்கு மட்டுமே பொருந்தும், தொழில்துறை துறைகளை முற்றிலும் ஒழுங்குபடுத்தாமல் விடுகிறது."
            }
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "Indian socialism is 'democratic socialism' and not 'state socialism' (Marxist socialism). Democratic socialism holds faith in a 'mixed economy' where both public and private sectors co-exist. As the Supreme Court observed, democratic socialism aims to end poverty, ignorance, disease, and inequality of opportunity, leaning heavily towards Gandhian socialism.",
            "ta": "இந்திய சோசலிசம் 'ஜனநாயக சோசலிசம்' ஆகும், 'அரசு சோசலிசம்' (மார்க்சிய சோசலிசம்) அல்ல. ஜனநாயக சோசலிசம் பொது மற்றும் தனியார் துறைகள் இரண்டும் இணைந்து வாழும் 'கலப்பு பொருளாதாரம்' மீது நம்பிக்கை கொண்டுள்ளது. இது காந்திய சோசலிசத்தை நோக்கி அதிக சாய்வைக் கொண்டுள்ளது."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Abolition of private property and total state monopoly characterize State/Marxist socialism, not Indian mixed economy socialism.", "ta": "தவறு. தனியார் சொத்து ஒழிப்பு மற்றும் முழு அரசு ஏகபோகம் அரசு/மார்க்சிய சோசலிசத்தின் பண்புகளாகும், இந்திய கலப்பு பொருளாதாரத்தின் பண்புகள் அல்ல."},
            "B": {"en": "Correct. Democratic socialism believes in a mixed economy co-existing with private enterprise.", "ta": "சரி. ஜனநாயக சோசலிசம் தனியார் நிறுவனங்களுடன் இணைந்த கலப்பு பொருளாதாரத்தை நம்புகிறது."},
            "C": {"en": "Incorrect. Reverses the two concepts: Democratic Socialism uses parliamentary peaceful means, while Marxist socialism originally relied on class struggle/revolution.", "ta": "தவறு. இரு கருத்துக்களையும் தலைகீழாக மாற்றுகிறது."},
            "D": {"en": "Incorrect. Democratic socialism applies across economic sectors through welfare planning and directive principles.", "ta": "தவறு. ஜனநாயக சோசலிசம் நலத்திட்டமிடல் மற்றும் வழிகாட்டு நெறிமுறைகள் மூலம் அனைத்து பொருளாதாரத் துறைகளுக்கும் பொருந்தும்."}
        },
        "tnpsc_tip": {"en": "Indian Socialism = Democratic Socialism = Mixed Economy (Public + Private). Blends Marxism & Gandhian socialism, leaning heavily towards Gandhian socialism.", "ta": "இந்திய சோசலிசம் = ஜனநாயக சோசலிசம் = கலப்பு பொருளாதாரம் (பொது + தனியார்). மார்க்சியம் மற்றும் காந்திய சோசலிசத்தின் கலவை, காந்திய சோசலிசத்தை நோக்கி அதிக சாய்வு கொண்டது."},
        "revision_fact": {"en": "Supreme Court in Excel Wear (1978) affirmed that addition of 'Socialist' did not imply total state ownership or nationalization of private businesses.", "ta": "எக்செல் வேர் வழக்கின் (1978) உச்ச நீதிமன்றத் தீர்ப்பு 'சமதர்ம' என்ற சொல் சேர்க்கப்பட்டது தனியார் வணிகங்களை முழுமையாக அரசுடைமையாக்குவதைக் குறிக்காது என்று உறுதிப்படுத்தியது."},
        "source_reference": ["Preamble Notes Part 1", "M. Laxmikanth"],
        "bloom_level": "Analyze",
        "estimated_time_sec": 75,
        "pyq_similarity": "High",
        "tags": ["Preamble", "Socialist", "Democratic Socialism", "Mixed Economy"]
    },

    # 4. Advanced Conceptual - Positive Secularism vs Western Negative Secularism
    {
        "id": "PRE_H_004",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Advanced Conceptual",
        "question": {
            "en": "Indian constitutional secularism is characterized as 'Positive Secularism'. Which of the following correctly highlights its distinction from the Western model of secularism?",
            "ta": "இந்திய அரசியலமைப்பு மதச்சார்பின்மை 'நேர்மறை மதச்சார்பின்மை' என விவரிக்கப்படுகிறது. மேற்கத்திய மதச்சார்பின்மை மாதிரியிலிருந்து இதன் வேறுபாட்டைச் சரியாக சுட்டிக்காட்டும் கூற்று எது?"
        },
        "options": [
            {
                "id": "A",
                "en": "Western secularism requires strict wall of separation and mutual exclusion between State and religion, whereas Indian positive secularism accords equal respect and equal protection to all religions (Sarva Dharma Sambhava).",
                "ta": "மேற்கத்திய மதச்சார்பின்மை அரசுக்கும் மதத்திற்கும் இடையே கடுமையான பிரிவினையையும் பரஸ்பர விலக்கலையும் கோருகிறது; ஆனால் இந்திய நேர்மறை மதச்சார்பின்மை அனைத்து மதங்களுக்கும் சமமான மரியாதையையும் சமமான பாதுகாப்பையும் அளிக்கிறது (சர்வ தர்ம சம்பவ)."
            },
            {
                "id": "B",
                "en": "Indian secularism establishes Hinduism as the official state religion while granting minority tolerance, whereas Western secularism is completely atheistic.",
                "ta": "இந்திய மதச்சார்பின்மை சிறுபான்மையினருக்கு சகிப்புத்தன்மையை அளிக்கும் அதே வேளையில் இந்து மதத்தை உத்தியோகபூர்வ அரசு மதமாக நிறுவுகிறது; ஆனால் மேற்கத்திய மதச்சார்பின்மை முற்றிலும் நாத்திகமானது."
            },
            {
                "id": "C",
                "en": "Western secularism allows the State to financial fund dominant religious institutions, whereas Indian secularism prohibits any citizen from practicing religion publicly.",
                "ta": "மேற்கத்திய மதச்சார்பின்மை ஆதிக்கம் செலுத்தும் மத நிறுவனங்களுக்கு அரசு நிதி உதவி செய்ய அனுமதிக்கிறது; ஆனால் இந்திய மதச்சார்பின்மை எந்தவொரு குடிமகனும் பகிரங்கமாக மதத்தைப் பின்பற்றுவதைத் தடுக்கிறது."
            },
            {
                "id": "D",
                "en": "Indian positive secularism was created for the first time by the 42nd Amendment Act of 1976 and had no constitutional existence prior to that.",
                "ta": "இந்திய நேர்மறை மதச்சார்பின்மை 1976 இன் 42வது திருத்தச் சட்டத்தால் முதன்முறையாக உருவாக்கப்பட்டது, அதற்கு முன் அரசியலமைப்பு ரீதியாக அதற்கு अस्तित्वம் இல்லை."
            }
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "The Indian Constitution embodies the positive concept of secularism: all religions in our country (irrespective of their strength) have the same status and support from the State (Sarva Dharma Sambhava). In contrast, Western secularism implies a rigid, negative separation between the State and religion.",
            "ta": "இந்திய அரசியலமைப்பு மதச்சார்பின்மையின் நேர்மறையான கருத்தை உள்ளடக்கியுள்ளது: நம் நாட்டில் உள்ள அனைத்து மதங்களும் (அவற்றின் பலத்தைப் பொருட்படுத்தாமல்) அரசுக்கு முன் ஒரே மாதிரியான தகுதியையும் ஆதரவையும் கொண்டுள்ளன (சர்வ தர்ம சம்பவ). மாறாக, மேற்கத்திய மதச்சார்பின்மை அரசுக்கும் மதத்திற்கும் இடையே கடுமையான எதிர்மறைப் பிரிவினையைக் குறிக்கிறது."
        },
        "why_not_others": {
            "A": {"en": "Correct. Positive Secularism = Equal respect and protection for all religions (Articles 25-28).", "ta": "சரி. நேர்மறை மதச்சார்பின்மை = அனைத்து மதங்களுக்கும் சமமான மரியாதை மற்றும் பாதுகாப்பு (உறுப்புகள் 25-28)."},
            "B": {"en": "Incorrect. India has NO official state religion; all religions are treated equally under the Constitution.", "ta": "தவறு. இந்தியாவுக்கு உத்தியோகபூர்வ அரசு மதம் எதுவுமில்லை; அரசியலமைப்பின் கீழ் அனைத்து மதங்களும் சமமாக நடத்தப்படுகின்றன."},
            "C": {"en": "Incorrect. Article 25 guarantees public freedom of conscience and religious practice; Article 27 restricts religious taxation.", "ta": "தவறு. உறுப்பு 25 பகிரங்க மனசாட்சி மற்றும் மதப் பழக்க சுதந்திரத்திற்கு உத்தரவாதம் அளிக்கிறது."},
            "D": {"en": "Incorrect. Articles 25-28 already embodied secular principles since 1950; 42nd Amendment only rendered it explicit.", "ta": "தவறு. உறுப்புகள் 25-28 1950 முதல் மதச்சார்பற்றக் கொள்கைகளை உள்ளடக்கியிருந்தன; 42வது திருத்தம் அதை வெளிப்படையாக்கியது மட்டுமே."}
        },
        "tnpsc_tip": {"en": "Indian Secularism = Positive concept (Sarva Dharma Sambhava). Western Secularism = Negative concept (Rigid wall of separation).", "ta": "இந்திய மதச்சார்பின்மை = நேர்மறைக் கருத்து (சர்வ தர்ம சம்பவ). மேற்கத்திய மதச்சார்பின்மை = எதிர்மறைக் கருத்து (கடுமையான தடுப்புச் சுவர்)."},
        "revision_fact": {"en": "In S.R. Bommai case (1994), the Supreme Court held that Secularism is a Basic Feature of the Indian Constitution.", "ta": "எஸ்.ஆர். பொம்மை வழக்கில் (1994), மதச்சார்பின்மை இந்திய அரசியலமைப்பின் அடிப்படை கட்டமைப்பு என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது."},
        "source_reference": ["Preamble Notes Part 1", "M. Laxmikanth"],
        "bloom_level": "Analyze",
        "estimated_time_sec": 75,
        "pyq_similarity": "High",
        "tags": ["Preamble", "Secular", "Positive Secularism", "Sarva Dharma Sambhava"]
    },

    # 5. Advanced Conceptual - Democratic vs Republic
    {
        "id": "PRE_H_005",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Advanced Conceptual",
        "question": {
            "en": "The terms 'Democratic' and 'Republic' appear sequentially in the Preamble. Which of the following correctly explains why the framers used BOTH terms instead of treating them as synonymous?",
            "ta": "முகவுரையில் 'ஜனநாயக' மற்றும் 'குடியரசு' ஆகிய சொற்கள் வரிசையாக வருகின்றன. இவ்விரு சொற்களையும் ஒத்த சொற்களாகக் கருதாமல் சிற்பிகள் இரண்டையும் ஏன் பயன்படுத்தினர் என்பதைச் சரியாக விளக்கும் கூற்று எது?"
        },
        "options": [
            {
                "id": "A",
                "en": "'Democratic' refers to popular sovereignty and representative governance, whereas 'Republic' specifically indicates that the Head of State is elected (not hereditary) and public offices are open to all citizens without privilege.",
                "ta": "'ஜனநாயக' என்பது மக்களின் இறையாண்மை மற்றும் பிரதிநிதித்துவ ஆட்சியைக் குறிக்கிறது; ஆனால் 'குடியரசு' என்பது நாட்டின் தலைவர் தேர்ந்தெடுக்கப்படுபவர் (பரம்பரை அல்ல) என்பதையும், பொதுப் பதவிகள் சலுகையின்றி அனைத்து குடிமக்களுக்கும் திறந்திருக்கும் என்பதையும் குறிக்கிறது."
            },
            {
                "id": "B",
                "en": "'Democratic' applies only to Union Executive elections, whereas 'Republic' applies exclusively to State Panchayats.",
                "ta": "'ஜனநாயக' என்பது ஒன்றிய நிர்வாகத் தேர்தல்களுக்கு மட்டுமே பொருந்தும், ஆனால் 'குடியரசு' என்பது மாநில பஞ்சாயத்துகளுக்கு மட்டுமே பொருந்தும்."
            },
            {
                "id": "C",
                "en": "A nation can be a Republic only if it practices direct democracy through referendums and recall.",
                "ta": "பொதுவாக்கெடுப்பு மற்றும் திரும்ப அழைத்தல் மூலம் நேரடி ஜனநாயகத்தைப் பயிற்சி செய்தால் மட்டுமே ஒரு நாடு குடியரசாக இருக்க முடியும்."
            },
            {
                "id": "D",
                "en": "The United Kingdom is both a Democratic nation and a Republic, whereas India is a Democratic nation but not a Republic.",
                "ta": "ஐக்கிய இராச்சியம் ஒரு ஜனநாயக நாடு மற்றும் குடியரசு ஆகும்; ஆனால் இந்தியா ஒரு ஜனநாயக நாடு ஆனால் குடியரசு அல்ல."
            }
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "A democratic polity can be classified into two categories—monarchy and republic. In a monarchy (like UK), the head of state enjoys a hereditary position. In a republic (like India), the head of state is always elected directly or indirectly for a fixed period. Republic also means vesting political sovereignty in the people and the absence of any privileged class.",
            "ta": "ஒரு ஜனநாயக அமைப்பை இரு வகைகளாகப் பிரிக்கலாம் - முடியாட்சி மற்றும் குடியரசு. முடியாட்சியில் (பிரிட்டன் போல்), நாட்டின் தலைவர் பரம்பரைப் பதவியைக் கொண்டுள்ளார். குடியரசில் (இந்தியா போல்), நாட்டின் தலைவர் எப்போதும் நேரடியாகவோ மறைமுகமாகவோ குறிப்பிட்ட காலத்திற்குத் தேர்ந்தெடுக்கப்படுகிறார். குடியரசு என்பது சலுகை பெற்ற வர்க்கமின்மையையும் குறிக்கிறது."
        },
        "why_not_others": {
            "A": {"en": "Correct. Democracy = popular mandate/governance; Republic = elected Head of State & absence of hereditary privileges.", "ta": "சரி. ஜனநாயகம் = மக்கள் பிரதிநிதித்துவ ஆட்சி; குடியரசு = தேர்ந்தெடுக்கப்பட்ட நாட்டின் தலைவர் & பரம்பரைச் சலுகையின்மை."},
            "B": {"en": "Incorrect. Both concepts apply globally across Union and State levels.", "ta": "தவறு. இரு கருத்துக்களும் ஒன்றியம் மற்றும் மாநில நிலைகளில் முழுமையாகப் பொருந்தும்."},
            "C": {"en": "Incorrect. India is an indirect representative republic; direct democracy mechanisms (referendum/recall) are not required for a republic.", "ta": "தவறு. இந்தியா ஒரு மறைமுகப் பிரதிநிதித்துவக் குடியரசு; குடியரசுக்கு நேரடி ஜனநாயக வழிமுறைகள் கட்டாயமில்லை."},
            "D": {"en": "Incorrect. UK is a constitutional Monarchy (democratic but not a republic); India is a Democratic Republic.", "ta": "தவறு. பிரிட்டன் ஒரு அரசியலமைப்பு முடியாட்சி (ஜனநாயகக் குடியரசு அல்ல); இந்தியா ஒரு ஜனநாயகக் குடியரசு."}
        },
        "tnpsc_tip": {"en": "Republic = 2 key features: (1) Elected Head of State (President for 5 yrs), (2) Vesting of political sovereignty in people + Absence of privileged class.", "ta": "குடியரசு = 2 முக்கிய அம்சங்கள்: (1) தேர்ந்தெடுக்கப்பட்ட நாட்டின் தலைவர் (5 ஆண்டுகளுக்கு குடியரசுத் தலைவர்), (2) மக்களிடம் அரசியல் இறையாண்மை + சலுகை பெற்ற வர்க்கமின்மை."},
        "revision_fact": {"en": "The ideals of Liberty, Equality, and Fraternity in our Preamble were taken from the French Revolution (1789–1799), which established a Republic.", "ta": "நமது முகவுரையில் உள்ள சுதந்திரம், சமத்துவம், சகோதரத்துவம் ஆகிய இலட்சியங்கள் குடியரசை நிறுவிய பிரெஞ்சுப் புரட்சியிலிருந்து (1789-1799) எடுக்கப்பட்டன."},
        "source_reference": ["Preamble Notes Part 1", "M. Laxmikanth"],
        "bloom_level": "Analyze",
        "estimated_time_sec": 75,
        "pyq_similarity": "High",
        "tags": ["Preamble", "Democratic", "Republic", "Constitutional Philosophy"]
    },

    # 6. Advanced Conceptual - Multi-dimensional Justice
    {
        "id": "PRE_H_006",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Advanced Conceptual",
        "question": {
            "en": "The Preamble secures 'Justice—social, economic and political'. Which of the following constitutional combinations correctly reflects the concept of 'Distributive Justice' as recognized by the Supreme Court?",
            "ta": "முகவுரை 'நீதி—சமூக, பொருளாதார மற்றும் அரசியல்' பாதுகாக்கிறது. உச்ச நீதிமன்றத்தால் அங்கீகரிக்கப்பட்ட 'பகிர்வு நீதி' (Distributive Justice) கருத்தை எந்த அரசியலமைப்பு சேர்க்கை சரியாகப் பிரதிபலிக்கிறது?"
        },
        "options": [
            {
                "id": "A",
                "en": "Social Justice + Economic Justice",
                "ta": "சமூக நீதி + பொருளாதார நீதி"
            },
            {
                "id": "B",
                "en": "Economic Justice + Political Justice",
                "ta": "பொருளாதார நீதி + அரசியல் நீதி"
            },
            {
                "id": "C",
                "en": "Social Justice + Political Justice",
                "ta": "சமூக நீதி + அரசியல் நீதி"
            },
            {
                "id": "D",
                "en": "Legal Justice + Administrative Justice",
                "ta": "சட்ட நீதி + நிர்வாக நீதி"
            }
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "The term 'justice' in the Preamble embraces three distinct forms—social, economic and political, secured through Fundamental Rights and Directive Principles. Social justice and economic justice together constitute what is known as 'distributive justice'—removing social discrimination and economic inequalities to achieve a welfare state.",
            "ta": "முகவுரையில் உள்ள 'நீதி' என்ற சொல் மூன்று வடிவங்களை உள்ளடக்கியது—சமூக, பொருளாதார மற்றும் அரசியல். சமூக நீதியும் பொருளாதார நீதியும் இணைந்து 'பகிர்வு நீதி' (Distributive Justice) என்று அழைக்கப்படுவதை உருவாக்குகின்றன - சமூகப் பாகுபாடு மற்றும் பொருளாதார ஏற்றத்தாழ்வுகளை அகற்றி ஒரு நல அரசை அடைதல்."
        },
        "why_not_others": {
            "A": {"en": "Correct. Social Justice + Economic Justice = Distributive Justice.", "ta": "சரி. சமூக நீதி + பொருளாதார நீதி = பகிர்வு நீதி."},
            "B": {"en": "Incorrect. Political justice refers to equal political rights (voting, contesting), not distributive justice.", "ta": "தவறு. அரசியல் நீதி என்பது சமமான அரசியல் உரிமைகளைக் குறிக்கிறது (வாக்களித்தல், போட்டியிடுதல்)."},
            "C": {"en": "Incorrect. Does not capture the economic wealth distribution component of distributive justice.", "ta": "தவறு. பகிர்வு நீதியின் பொருளாதார விநியோகக் கூறைக் கைப்பற்றவில்லை."},
            "D": {"en": "Incorrect. Legal and administrative justice are procedural subsets, not the Preamble's distributive combination.", "ta": "தவறு. சட்ட மற்றும் நிர்வாக நீதி என்பது நடைமுறை துணைக் கூறுகளாகும்."}
        },
        "tnpsc_tip": {"en": "Distributive Justice = Social Justice + Economic Justice. Ideal of Justice (Social, Economic, Political) was taken from the Russian Revolution (1917).", "ta": "பகிர்வு நீதி = சமூக நீதி + பொருளாதார நீதி. நீதியின் இலட்சியம் (சமூக, பொருளாதார, அரசியல்) 1917 ரஷ்யப் புரட்சியிலிருந்து பெறப்பட்டது."},
        "revision_fact": {"en": "Preamble secures Social, Economic and Political justice. Russian Revolution (1917) inspired the inclusion of these three forms of justice.", "ta": "முகவுரை சமூக, பொருளாதார மற்றும் அரசியல் நீதியைப் பாதுகாக்கிறது. ரஷ்யப் புரட்சி (1917) இந்த மூன்று வகையான நீதிகளைச் சேர்ப்பதற்குத் தூண்டுகோலாக அமைந்தது."},
        "source_reference": ["Preamble Notes Part 1", "M. Laxmikanth"],
        "bloom_level": "Analyze",
        "estimated_time_sec": 60,
        "pyq_similarity": "High",
        "tags": ["Preamble", "Justice", "Distributive Justice", "Russian Revolution"]
    },

    # 7. Advanced Conceptual - Non-Absolute Nature of Liberty
    {
        "id": "PRE_H_007",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Advanced Conceptual",
        "question": {
            "en": "The Preamble promises 'Liberty of thought, expression, belief, faith and worship'. How does the constitutional scheme regulate this liberty to prevent it from degenerating into license or anarchy?",
            "ta": "முகவுரை 'எண்ணம், வெளிப்பாடு, நம்பிக்கை, சமயம் மற்றும் வழிபாட்டு சுதந்திரத்திற்கு' வாக்குறுதி அளிக்கிறது. இச்சுதந்திரம் உரிமைகேடாகவோ அல்லது அராஜகமாகவோ சீரழிவதைத் தடுக்க அரசியலமைப்பு திட்டம் இதை எவ்வாறு ஒழுங்குபடுத்துகிறது?"
        },
        "options": [
            {
                "id": "A",
                "en": "Liberty granted in the Preamble is absolute and unrestrictable by any statute enacted by Parliament.",
                "ta": "முகவுரையில் வழங்கப்பட்டுள்ள சுதந்திரம் வரம்பற்றது மற்றும் பாராளுமன்றத்தால் இயற்றப்பட்ட எந்தவொரு சட்டத்தாலும் கட்டுப்படுத்த முடியாதது."
            },
            {
                "id": "B",
                "en": "Preamble liberty is operationalized through Part III Fundamental Rights, which explicitly subject these freedoms to reasonable restrictions specified in Articles 19(2)-(6) and Articles 25-26.",
                "ta": "முகவுரை சுதந்திரம் பகுதி III அடிப்படை உரிமைகள் மூலம் நடைமுறைப்படுத்தப்படுகிறது; அவை உறுப்புகள் 19(2)-(6) மற்றும் உறுப்புகள் 25-26 இல் குறிப்பிடப்பட்டுள்ள நியாயமான கட்டுப்பாடுகளுக்கு உட்பட்டவை."
            },
            {
                "id": "C",
                "en": "Liberty can be suspended permanently by an executive order of the President without legislative sanction.",
                "ta": "சட்டமன்ற அனுமதியின்றி குடியரசுத் தலைவரின் நிர்வாக உத்தரவால் சுதந்திரத்தை நிரந்தரமாக நிறுத்தி வைக்க முடியும்."
            },
            {
                "id": "D",
                "en": "Liberty of belief and worship applies exclusively to registered citizens owning real estate property.",
                "ta": "நம்பிக்கை மற்றும் வழிபாட்டு சுதந்திரம் அசையா சொத்துக்களை வைத்திருக்கக்கூடிய பதிவுசெய்த குடிமக்களுக்கு மட்டுமே பொருந்தும்."
            }
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "The term 'liberty' means the absence of restraints on the activities of individuals, and at the same time, providing opportunities for the development of individual personalities. However, liberty conceived by the Preamble is NOT absolute but qualified. It must be enjoyed within the limitations mentioned in the Constitution itself (e.g. reasonable restrictions under Part III).",
            "ta": "முகவுரையில் கூறப்பட்டுள்ள சுதந்திரம் 'வரம்பற்றது' அல்ல, மாறாக நிபந்தனைக்குட்பட்டது (qualified). இது அரசியலமைப்பிலேயே குறிப்பிடப்பட்டுள்ள வரம்புகளுக்குள் (பகுதி III இன் கீழ் உள்ள நியாயமான கட்டுப்பாடுகள்) அனுபவிக்கப்பட வேண்டும்."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Liberty in the Preamble is NOT absolute; absolute liberty leads to anarchy.", "ta": "தவறு. முகவுரையில் உள்ள சுதந்திரம் வரம்பற்றது அல்ல; வரம்பற்ற சுதந்திரம் அராஜகத்திற்கு வழிவகுக்கும்."},
            "B": {"en": "Correct. Liberty is qualified by reasonable restrictions in Fundamental Rights (Part III).", "ta": "சரி. சுதந்திரம் பகுதி III அடிப்படை உரிமைகளில் நியாயமான கட்டுப்பாடுகளால் வரம்பிற்குட்படுத்தப்பட்டுள்ளது."},
            "C": {"en": "Incorrect. Permanent executive suspension without constitutional mandate violates the rule of law.", "ta": "தவறு. அரசியலமைப்பு ஆணை இன்றி நிரந்தர நிர்வாக இடைநிறுத்தம் சட்டத்தின் ஆட்சியை மீறுகிறது."},
            "D": {"en": "Incorrect. Liberty applies to all persons/citizens regardless of property ownership.", "ta": "தவறு. சொத்துரிமையைப் பொருட்படுத்தாமல் அனைத்து நபர்களுக்கும்/குடிமக்களுக்கும் சுதந்திரம் பொருந்தும்."}
        },
        "tnpsc_tip": {"en": "Preamble Liberty = 5 types (Thought, Expression, Belief, Faith, Worship). It is NOT absolute, but subject to constitutional reasonable restrictions.", "ta": "முகவுரை சுதந்திரம் = 5 வகைகள் (எண்ணம், வெளிப்பாடு, நம்பிக்கை, சமயம், வழிபாடு). இது வரம்பற்றது அல்ல, அரசியலமைப்பு நியாயமான கட்டுப்பாடுகளுக்கு உட்பட்டது."},
        "revision_fact": {"en": "Liberty, Equality, and Fraternity are an indivisible trinity. Dr. Ambedkar noted that without equality, liberty would produce the supremacy of the few over the many.", "ta": "சுதந்திரம், சமத்துவம், சகோதரத்துவம் ஆகியவை பிரிக்க முடியாத முத்துவமாகும். சமத்துவம் இல்லாமல் சுதந்திரம் ஒரு சிலரின் ஆதிக்கத்தை உருவாக்கும் என்று டாக்டர் அம்பேத்கர் குறிப்பிட்டார்."}
    },

    # 8. Advanced Conceptual - Equality of Status and Opportunity
    {
        "id": "PRE_H_008",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Advanced Conceptual",
        "question": {
            "en": "The Preamble guarantees 'Equality of status and of opportunity'. Which of the following correctly analyzes how positive discrimination (affirmative action) under Articles 15(4) and 16(4) aligns with this Preamble ideal?",
            "ta": "முகவுரை 'தகுதி மற்றும் வாய்ப்பில் சமத்துவத்திற்கு' உத்தரவாதம் அளிக்கிறது. உறுப்புகள் 15(4) மற்றும் 16(4) இன் கீழ் உள்ள நேர்மறை பாகுபாடு (இடஒதுக்கீடு) இந்த முகவுரை இலட்சியத்துடன் எவ்வாறு ஒத்துப் போகிறது என்பதைச் சரியாக பகுப்பாய்வு செய்யும் கூற்று எது?"
        },
        "options": [
            {
                "id": "A",
                "en": "Affirmative action violates Preamble equality by treating citizens differently based on social background.",
                "ta": "சமூகப் பின்னணியின் அடிப்படையில் குடிமக்களை வித்தியாசமாக நடத்துவதன் மூலம் இடஒதுக்கீடு முகவுரை சமத்துவத்தை மீறுகிறது."
            },
            {
                "id": "B",
                "en": "Affirmative action is an instrument to achieve substantive equality by placing unequals on an equal footing, thereby fulfilling 'Equality of Opportunity' for historically disadvantaged classes.",
                "ta": "இடஒதுக்கீடு என்பது சமமற்றவர்களை சமமான நிலையில் வைப்பதன் மூலம் நடைமுறைச் சமத்துவத்தை அடைவதற்கான ஒரு கருவியாகும், இதன் மூலம் வரலாற்று ரீதியாக பின்தங்கிய வகுப்பினருக்கு 'வாய்ப்பில் சமத்துவத்தை' நிறைவேற்றுகிறது."
            },
            {
                "id": "C",
                "en": "Equality in the Preamble strictly guarantees identical mathematical outcomes for all individuals regardless of merit or need.",
                "ta": "முகவுரையில் உள்ள சமத்துவம் தகுதி அல்லது தேவையைப் பொருட்படுத்தாமல் அனைத்து நபர்களுக்கும் ஒரே மாதிரியான கணித முடிவுகளுக்கு கடுமையான உத்தரவாதம் அளிக்கிறது."
            },
            {
                "id": "D",
                "en": "Articles 15(4) and 16(4) were held unconstitutional by the Supreme Court for conflicting with the Preamble.",
                "ta": "உறுப்புகள் 15(4) மற்றும் 16(4) முகவுரையுடன் முரண்படுவதாக உச்ச நீதிமன்றத்தால் அரசியலமைப்புக்கு முரணானது என அறிவிக்கப்பட்டது."
            }
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "Equality means the absence of special privileges to any section of the society, and the provision of adequate opportunities for all individuals without any discrimination. True equality requires equal treatment among equals; treating unequal unequals equally perpetuates inequality. Affirmative action (Articles 15(4), 16(4)) ensures substantive equality of opportunity for disadvantaged groups.",
            "ta": "உண்மையான சமத்துவம் என்பது சமமானவர்களிடையே சமமான சிகிச்சையைக் கோருகிறது; சமமற்றவர்களை சமமாக நடத்துவது சமத்துவமின்மையை நீடிக்கச் செய்யும். நேர்மறை நடவடிக்கைகள் (உறுப்புகள் 15(4), 16(4)) பின்தங்கிய குழுக்களுக்கு நடைமுறைச் சமத்துவத்தை உறுதி செய்கின்றன."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Formal mathematical equality is not the constitutional test; substantive equality allows protective discrimination.", "ta": "தவறு. முறையான கணிதச் சமத்துவம் அரசியலமைப்பு சோதனையல்ல; நடைமுறைச் சமத்துவம் பாதுகாப்பு பாகுபாட்டை அனுமதிக்கிறது."},
            "B": {"en": "Correct. Affirmative action achieves substantive equality of status and opportunity.", "ta": "சரி. நேர்மறை நடவடிக்கை தகுதி மற்றும் வாய்ப்பில் நடைமுறைச் சமத்துவத்தை அடைகிறது."},
            "C": {"en": "Incorrect. Preamble equality provides equality of opportunity, not identical forced outcomes.", "ta": "தவறு. முகவுரை சமத்துவம் வாய்ப்பில் சமத்துவத்தை வழங்குகிறது, கட்டாய முடிவுகளில் அல்ல."},
            "D": {"en": "Incorrect. Supreme Court repeatedly upheld protective discrimination as a facet of basic structure equality.", "ta": "தவறு. உச்ச நீதிமன்றம் பாதுகாப்பு பாகுபாட்டை சமத்துவத்தின் ஒரு பகுதியாக பலமுறை உறுதிப்படுத்தியுள்ளது."}
        },
        "tnpsc_tip": {"en": "Equality in Preamble embraces 3 dimensions: Civic (Art 14-18), Political (Art 325-326), and Economic (Art 39 DPSP).", "ta": "முகவுரையில் உள்ள சமத்துவம் 3 பரிமாணங்களை உள்ளடக்கியது: குடிமை (உறுப்புகள் 14-18), அரசியல் (உறுப்புகள் 325-326), மற்றும் பொருளாதாரம் (உறுப்பு 39 DPSP)."}
    },

    # 9. Advanced Conceptual - Fraternity & Dual Assurance
    {
        "id": "PRE_H_009",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Advanced Conceptual",
        "question": {
            "en": "Fraternity in the Preamble assures two vital things: 'the dignity of the individual and the unity and integrity of the Nation'. Which of the following best captures the constitutional relationship between individual dignity and national unity?",
            "ta": "முகவுரையில் உள்ள சகோதரத்துவம் இரண்டு முக்கிய விஷயங்களை உறுதிப்படுத்துகிறது: 'நபரின் கண்ணியம் மற்றும் நாட்டின் பிளவுபடாத ஒருமைப்பாடு'. தனிமனிதக் கண்ணியத்திற்கும் தேசிய ஒருமைப்பாட்டிற்கும் இடையிலான அரசியலமைப்பு தொடர்பை மிகச்சரியாக வெளிப்படுத்தும் கூற்று எது?"
        },
        "options": [
            {
                "id": "A",
                "en": "National unity can only be sustained when the personal dignity of every individual citizen is recognized, protected, and respected as sacred.",
                "ta": "ஒவ்வொரு தனிப்பட்ட குடிமகனின் தனிப்பட்ட கண்ணியமும் புனிதமானதாக அங்கீகரிக்கப்பட்டு, பாதுகாக்கப்பட்டு, மதிக்கப்படும் போது மட்டுமே தேசிய ஒருமைப்பாட்டைப் பேண முடியும்."
            },
            {
                "id": "B",
                "en": "The State may suppress individual dignity entirely in the pursuit of national integration during peacetime.",
                "ta": "அமைதி காலத்தில் தேசிய ஒருமைப்பாட்டைப் பின்தொடர்வதற்காக அரசு தனிமனிதக் கண்ணியத்தை முற்றிலும் அடக்கலாம்."
            },
            {
                "id": "C",
                "en": "Fraternity is a purely moral concept without any operational connection to Fundamental Rights or Fundamental Duties.",
                "ta": "சகோதரத்துவம் என்பது அடிப்படை உரிமைகள் அல்லது அடிப்படை கடமைகளுடன் எந்தவித நடைமுறைத் தொடர்பும் இல்லாத முற்றிலும் ஒரு ஒழுக்கநெறிக் கருத்தாகும்."
            },
            {
                "id": "D",
                "en": "'Integrity' was removed from the Preamble by the 44th Constitutional Amendment Act to protect state rights.",
                "ta": "'ஒருமைப்பாடு' என்ற சொல் மாநில உரிமைகளைப் பாதுகாக்க 44வது அரசியலமைப்பு திருத்தச் சட்டத்தால் முகவுரையிலிருந்து நீக்கப்பட்டது."
            }
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "As K.M. Munshi observed, the phrase 'dignity of the individual' signifies that the Constitution not only ensures material development but recognizes that the personality of every individual is sacred. National unity and integrity cannot be achieved by suppressing individual personality; fraternity seamlessly fuses individual dignity with collective national integration.",
            "ta": "கே.எம். முன்ஷி குறிப்பிட்டது போல, 'நபரின் கண்ணியம்' என்ற தொடர், அரசியலமைப்பு பொருள்சார் வளர்ச்சியை உறுதி செய்வது மட்டுமல்லாமல், ஒவ்வொரு நபரின் ஆளுமையும் புனிதமானது என்பதை அங்கீகரிக்கிறது. தனிமனித ஆளுமையை அடக்குவதன் மூலம் தேசிய ஒற்றுமையை அடைய முடியாது."
        },
        "why_not_others": {
            "A": {"en": "Correct. Individual dignity and national unity are mutually reinforcing components of Fraternity.", "ta": "சரி. தனிமனிதக் கண்ணியமும் தேசிய ஒருமைப்பாடும் சகோதரத்துவத்தின் பரஸ்பரம் வலுவூட்டும் கூறுகளாகும்."},
            "B": {"en": "Incorrect. Individual dignity is protected under Article 21 and cannot be arbitrarily suppressed.", "ta": "தவறு. தனிமனிதக் கண்ணியம் உறுப்பு 21 இன் கீழ் பாதுகாக்கப்படுகிறது, அதை தன்னிச்சையாக அடக்க முடியாது."},
            "C": {"en": "Incorrect. Fraternity is operationalized through single citizenship and Article 51A(e) Fundamental Duty.", "ta": "தவறு. சகோதரத்துவம் ஒற்றைக் குடியுரிமை மற்றும் உறுப்பு 51A(e) அடிப்படை கடமை மூலம் நடைமுறைப்படுத்தப்படுகிறது."},
            "D": {"en": "Incorrect. 'Integrity' was ADDED (not removed) by the 42nd Amendment Act, 1976.", "ta": "தவறு. 'ஒருமைப்பாடு' என்ற சொல் 1976 இன் 42வது திருத்தச் சட்டத்தால் சேர்க்கப்பட்டது (நீக்கப்படவில்லை)."}
        },
        "tnpsc_tip": {"en": "Fraternity promotes: (1) Dignity of the Individual, (2) Unity and Integrity of the Nation. 'Integrity' was added by 42nd Amendment 1976.", "ta": "சகோதரத்துவம் ஊக்குவிப்பது: (1) நபரின் கண்ணியம், (2) நாட்டின் பிளவுபடாத ஒருமைப்பாடு. 'ஒருமைப்பாடு' 1976 இன் 42வது திருத்தத்தால் சேர்க்கப்பட்டது."}
    },

    # 10. Advanced Conceptual - Non-Justiciable Nature & Interpretive Value
    {
        "id": "PRE_H_010",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Advanced Conceptual",
        "question": {
            "en": "The Preamble is described as 'non-justiciable and non-enforceable in a court of law'. What is the precise legal significance of this characterization?",
            "ta": "முகவுரை 'நீதிமன்றத்தால் நிலைநிறுத்த முடியாதது மற்றும் அமல்படுத்த முடியாதது' என விவரிக்கப்படுகிறது. இந்த இயல்புறுத்தலின் துல்லியமான சட்ட முக்கியத்துவம் யாது?"
        },
        "options": [
            {
                "id": "A",
                "en": "A citizen cannot file a writ petition claiming a standalone remedy based solely on a violation of the Preamble, yet courts can use it as an interpretive guide to resolve ambiguities in statutory or constitutional provisions.",
                "ta": "முகவுரையை மீறியதற்காக மட்டுமே ஒரு குடிமகன் தனித்த தீர்வை க்ளைம் செய்து பேராணை மனு தாக்கல் செய்ய முடியாது; இருப்பினும், சட்டப்பூர்வ அல்லது அரசியலமைப்பு விதிகளில் உள்ள தெளிவின்மைகளைத் தீர்க்க நீதிமன்றங்கள் அதை ஒரு விளக்கமளிக்கும் வழிகாட்டியாகப் பயன்படுத்தலாம்."
            },
            {
                "id": "B",
                "en": "The Preamble is completely devoid of any legal value and must be ignored by judges in constitutional interpretation.",
                "ta": "முகவுரை முற்றிலும் எந்தச் சட்ட மதிப்பும் அற்றது, அரசியலமைப்பு விளக்கத்தின் போது நீதிபதிகள் அதைப் புறக்கணிக்க வேண்டும்."
            },
            {
                "id": "C",
                "en": "Non-justiciability means Parliament can enact laws directly contradicting the Preamble without judicial review.",
                "ta": "நீதிமன்றத்தால் நிலைநிறுத்த முடியாத தன்மை என்றால், நீதிப் புனராய்வு இன்றி முகவுரைக்கு நேரடியாக முரண்படும் சட்டங்களைப் பாராளுமன்றம் இயற்றலாம்."
            },
            {
                "id": "D",
                "en": "The Preamble becomes enforceable only during a Proclamation of National Emergency under Article 352.",
                "ta": "உறுப்பு 352 இன் கீழ் தேசிய அவசரநிலை பிரகடனத்தின் போது மட்டுமே முகவுரை அமல்படுத்தக்கூடியதாக மாறுகிறது."
            }
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Like the Directive Principles of State Policy, the Preamble is non-justiciable—its provisions are not enforceable in courts of law for their violation. However, as the Supreme Court ruled in Kesavananda Bharati, the Preamble is of extreme importance and the Constitution should be read and interpreted in the light of the grand and noble vision expressed in the Preamble.",
            "ta": "அரசு கொள்கை வழிகாட்டு நெறிமுறைகளைப் போல, முகவுரையும் நீதிமன்றங்களால் நிலைநிறுத்த முடியாதது - அதன் விதிகளை மீறியதற்காக நீதிமன்றங்களில் நேரடியாக அமல்படுத்த முடியாது. இருப்பினும், கேசவாநந்த பாரதி வழக்கில் உச்ச நீதிமன்றம் தீர்ப்பளித்தது போல, அரசியலமைப்பை முகவுரையின் பார்வையில் படித்து விளக்க வேண்டும்."
        },
        "why_not_others": {
            "A": {"en": "Correct. Non-justiciable = cannot be independently enforced, but acts as a key interpretive guide.", "ta": "சரி. நீதிமன்றத்தால் நிலைநிறுத்த முடியாதது = நேரடியாக அமல்படுத்த முடியாது, ஆனால் விளக்கமளிக்கும் வழிகாட்டியாக செயல்படுகிறது."},
            "B": {"en": "Incorrect. Preamble is the key to open the mind of makers and reflects the Basic Structure.", "ta": "தவறு. முகவுரை அரசியலமைப்பு சிற்பிகளின் மனதைத் திறக்கும் சாவியாகும், அடிப்படை கட்டமைப்பைப் பிரதிபலிப்பதாகும்."},
            "C": {"en": "Incorrect. Laws violating Basic Structure principles (embodied in Preamble) can be struck down.", "ta": "தவறு. முகவுரையில் உள்ள அடிப்படை கட்டமைப்பு தத்துவங்களை மீறும் சட்டங்கள் ரத்து செய்யப்படலாம்."},
            "D": {"en": "Incorrect. Emergency does not convert non-justiciable preambular text into an enforceable right.", "ta": "தவறு. அவசரநிலை முகவுரையை அமல்படுத்தக்கூடிய உரிமையாக மாற்றாது."}
        },
        "tnpsc_tip": {"en": "Two Key Notes on Preamble: (1) It is NEITHER a source of power NOR a prohibition on power. (2) It is non-justiciable (not enforceable in courts).", "ta": "முகவுரை பற்றிய 2 முக்கிய குறிப்புகள்: (1) இது அதிகாரம் அளிக்கும் மூலமும் அல்ல, அதிகாரத் தடையும் அல்ல. (2) இது நீதிமன்றத்தால் நிலைநிறுத்த முடியாதது."}
    },

    # 11. Advanced Conceptual - Omission of Socialist/Secular in 1946
    {
        "id": "PRE_H_011",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Advanced Conceptual",
        "question": {
            "en": "Why did Pandit Jawaharlal Nehru deliberately omit the words 'Socialist' and 'Secular' from the Objectives Resolution moved on December 13, 1946, despite his personal socialist convictions?",
            "ta": "பண்டித ஜவஹர்லால் நேரு தனது தனிப்பட்ட சோசலிச நம்பிக்கைகளுக்கு மத்தியிலும், டிசம்பர் 13, 1946 அன்று முன்மொழியப்பட்ட குறிக்கோள்கள் தீர்மானத்தில் 'சமதர்ம' மற்றும் 'மதச்சார்பற்ற' ஆகிய வார்த்தைகளை ஏன் வேண்டுமென்றே தவிர்த்தார்?"
        },
        "options": [
            {
                "id": "A",
                "en": "To maintain maximum unity and consensus across diverse political elements in the Constituent Assembly, avoiding rigid dogmatic labels while embedding their substantive principles in social and economic justice.",
                "ta": "அரசியலமைப்புச் சபையில் உள்ள பல்வேறு அரசியல் கூறுகளிடையே அதிகபட்ச ஒற்றுமையையும் ஒருமித்த கருத்தையும் பேணவும், விறைப்பான கோட்பாட்டு லேபிள்களைத் தவிர்க்கும் அதே வேளையில் அவற்றின் சாரப் கொள்கைகளை சமூக மற்றும் பொருளாதார நீதியில் பொதிக்கவும்."
            },
            {
                "id": "B",
                "en": "Because the Cabinet Mission Plan prohibited the Assembly from adopting economic policies.",
                "ta": "கேபினட் தூதுக்குழு திட்டம் சபை பொருளாதாரக் கொள்கைகளை ஏற்பதைத் தடை செய்திருந்ததால்."
            },
            {
                "id": "C",
                "en": "Dr. B.R. Ambedkar explicitly vetoed the inclusion of any socio-economic provisions in the Preamble.",
                "ta": "முகவுரையில் எந்தவொரு சமூக-பொருளாதார விதிகளையும் சேர்ப்பதை டாக்டர் பி.ஆர். அம்பேத்கர் வெளிப்படையாக வீட்டோ செய்தார்."
            },
            {
                "id": "D",
                "en": "The terms were considered unconstitutional under British Indian common law.",
                "ta": "பிரிட்டிஷ் இந்திய பொதுச்சட்டத்தின் கீழ் இவ்வார்த்தைகள் அரசியலமைப்புக்கு முரணானவையாகக் கருதப்பட்டன."
            }
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Nehru pointed out that introducing dogmatic ideological terms like 'Socialist' might cause premature political divisions in the Assembly. Instead, he preferred to state the substance of democracy—namely, social, economic, and political justice—leaving the detailed future socio-economic structure to be determined by elected democratic parliaments.",
            "ta": "நேரு 'சமதர்ம' போன்ற கோட்பாட்டுச் சொற்களை அறிமுகப்படுத்துவது அவையில் முதிர்ச்சியற்ற அரசியல் பிளவுகளை ஏற்படுத்தக்கூடும் என்று சுட்டிக்காட்டினார். அதற்குப் பதிலாக, ஜனநாயகத்தின் சாரத்தை (சமூக, பொருளாதார மற்றும் அரசியல் நீதி) குறிப்பிட விரும்பினார்."
        },
        "why_not_others": {
            "A": {"en": "Correct. Omitted to secure broad consensus across diverse Assembly factions without imposing rigid labels.", "ta": "சரி. விறைப்பான லேபிள்களைச் சுமத்தாமல் அவையின் பல்வேறு பிரிவுகளிடையே பரந்த ஒருமித்த கருத்தைப் பெறத் தவிர்க்கப்பட்டது."},
            "B": {"en": "Incorrect. Cabinet Mission Plan did not restrict socio-economic vision declarations.", "ta": "தவறு. கேபினட் தூதுக்குழு திட்டம் சமூக-பொருளாதார தொலைநோக்கு அறிவிப்புகளைக் கட்டுப்படுத்தவில்லை."},
            "C": {"en": "Incorrect. Dr. Ambedkar supported socio-economic justice, though agreeing on consensus.", "ta": "தவறு. டாக்டர் அம்பேத்கர் சமூக-பொருளாதார நீதியை ஆதரித்தார்."},
            "D": {"en": "Incorrect. British common law had no bearing on Constituent Assembly's resolution terminology.", "ta": "தவறு. பிரிட்டிஷ் பொதுச்சட்டத்திற்கு அரசியலமைப்புச் சபையின் தீர்மானச் சொற்களுடன் எவ்விதத் தொடர்பும் இல்லை."}
        },
        "tnpsc_tip": {"en": "Objectives Resolution moved Dec 13, 1946; adopted Jan 22, 1947. 'Socialist' and 'Secular' were added later by 42nd Amendment 1976.", "ta": "குறிக்கோள் தீர்மானம் முன்மொழியப்பட்டது டிசம்பர் 13, 1946; ஏற்றுக்கொள்ளப்பட்டது ஜனவரி 22, 1947. 'சமதர்ம' மற்றும் 'மதச்சார்பற்ற' பின்னர் 1976 இன் 42வது திருத்தத்தால் சேர்க்கப்பட்டன."}
    },

    # 12. Advanced Conceptual - Preamble as Source of Power
    {
        "id": "PRE_H_012",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Advanced Conceptual",
        "question": {
            "en": "In constitutional law, what is the precise relationship between the Preamble and the legislative powers of Parliament?",
            "ta": "அரசியலமைப்புச் சட்டத்தில், முகவுரைக்கும் பாராளுமன்றத்தின் சட்டமியற்றும் அதிகாரங்களுக்கும் இடையிலான துல்லியமான உறவு யாது?"
        },
        "options": [
            {
                "id": "A",
                "en": "The Preamble is NEITHER a source of power to the legislature NOR a prohibition upon the powers of the legislature.",
                "ta": "முகவுரை சட்டமன்றத்திற்கு அதிகாரம் அளிக்கும் மூலமும் அல்ல, சட்டமன்ற அதிகாரங்கள் மீதான தடையும் அல்ல."
            },
            {
                "id": "B",
                "en": "The Preamble grants Parliament inherent residual legislative power over all unlisted subjects.",
                "ta": "பட்டியலிடப்படாத அனைத்து பாடங்கள் மீதும் நாடாளுமன்றத்திற்கு உள்ளார்ந்த எஞ்சிய சட்ட அதிகாரத்தை முகவுரை வழங்குகிறது."
            },
            {
                "id": "C",
                "en": "The Preamble acts as an enforceable negative covenant prohibiting Parliament from imposing taxes.",
                "ta": "பாராளுமன்றம் வரிகளை விதிப்பதைத் தடுக்கும் ஒரு அமல்படுத்தக்கூடிய எதிர்மறை ஒப்பந்தமாக முகவுரை செயல்படுகிறது."
            },
            {
                "id": "D",
                "en": "The Preamble explicitly supersedes express constitutional provisions whenever a conflict arises.",
                "ta": "ஒரு முரண்பாடு எழும்போதெல்லாம் வெளிப்படையான அரசியலமைப்பு விதிகளை முகவுரை வெளிப்படையாக மேலோங்குகிறது."
            }
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Two essential points must be noted regarding the Preamble: (1) The Preamble is neither a source of power to legislature nor a prohibition upon the powers of legislature. (2) It is non-justiciable, that is, its provisions are not enforceable in courts of law.",
            "ta": "முகவுரை குறித்து 2 அவசியமான புள்ளிகளைக் கவனிக்க வேண்டும்: (1) முகவுரை சட்டமன்றத்திற்கு அதிகாரம் அளிக்கும் மூலமும் அல்ல, சட்டமன்ற அதிகாரங்கள் மீதான தடையும் அல்ல. (2) இது நீதிமன்றத்தால் நிலைநிறுத்த முடியாதது."
        },
        "why_not_others": {
            "A": {"en": "Correct. Fundamental rule: Preamble is neither a source of power nor a limitation on power.", "ta": "சரி. அடிப்படை விதி: முகவுரை அதிகாரத்தின் மூலமும் அல்ல, அதிகார வரம்பும் அல்ல."},
            "B": {"en": "Incorrect. Residuary powers are granted under Article 248 and Entry 97 List I, not Preamble.", "ta": "தவறு. எஞ்சிய அதிகாரங்கள் உறுப்பு 248 இன் கீழ் வழங்கப்பட்டுள்ளன, முகவுரையில் அல்ல."},
            "C": {"en": "Incorrect. Taxing powers derive from Article 265 and Seventh Schedule.", "ta": "தவறு. வரி விதிக்கும் அதிகாரங்கள் உறுப்பு 265 மற்றும் ஏழாவது அட்டவணையிலிருந்து பெறப்படுகின்றன."},
            "D": {"en": "Incorrect. Preamble cannot override clear, express text of constitutional Articles.", "ta": "தவறு. முகவுரை அரசியலமைப்பு உறுப்புகளின் தெளிவான உரையை மேலோங்க முடியாது."}
        },
        "tnpsc_tip": {"en": "Preamble is NOT a source of power, NOR a limitation on power. It is an interpretive preamble/preface.", "ta": "முகவுரை அதிகாரம் அளிக்கும் மூலமும் அல்ல, அதிகார வரம்பும் அல்ல. இது ஒரு விளக்கமளிக்கும் முகவுரையாகும்."}
    },

    # 13. Multi-statement Analytical - We, the People & Legitimacy
    {
        "id": "PRE_H_013",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Multi-statement Analytical",
        "question": {
            "en": "Consider the following statements regarding the constitutional legitimacy and source of the Preamble:\n1. The Constituent Assembly adopted, enacted, and gave the Constitution to the people of India on 26th November 1949.\n2. Popular sovereignty implies that all political power originates from and rests ultimately with the people.\n3. The legal validity of the Indian Constitution today remains subordinate to the Indian Independence Act, 1947.\n4. The Preamble explicitly records November 26, 1949, as the date of adoption and enactment.\nWhich of the statements given above are CORRECT?",
            "ta": "முகவுரையின் அரசியலமைப்பு சட்டபூர்வத்தன்மை மற்றும் மூலம் பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. அரசியலமைப்புச் சபை 1949 நவம்பர் 26 அன்று அரசியலமைப்பை ஏற்று, இயற்றி, இந்திய மக்களுக்கு அளித்தது.\n2. மக்களின் இறையாண்மை என்பது அனைத்து அரசியல் அதிகாரமும் மக்களிடமிருந்தே தோன்றுகிறது மற்றும் இறுதியில் மக்களிடமே உள்ளது என்பதைக் குறிக்கிறது.\n3. இந்திய அரசியலமைப்பின் சட்டபூர்வ செல்லுபடியாகும் தன்மை இன்று 1947 இந்திய சுதந்திரச் சட்டத்திற்கு உட்பட்டதாக உள்ளது.\n4. முகவுரை நவம்பர் 26, 1949 ஐ ஏற்றுக்கொள்ளப்பட்ட மற்றும் இயற்றப்பட்ட நாளாக வெளிப்படையாகப் பதிவு செய்கிறது.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?"
        },
        "options": [
            {
                "id": "A",
                "en": "1, 2 and 4 only",
                "ta": "1, 2 மற்றும் 4 மட்டுமே"
            },
            {
                "id": "B",
                "en": "1 and 3 only",
                "ta": "1 மற்றும் 3 மட்டுமே"
            },
            {
                "id": "C",
                "en": "2, 3 and 4 only",
                "ta": "2, 3 மற்றும் 4 மட்டுமே"
            },
            {
                "id": "D",
                "en": "1, 2, 3 and 4",
                "ta": "அனைத்தும் (1, 2, 3 மற்றும் 4)"
            }
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Statements 1, 2, and 4 are correct. Statement 3 is incorrect because Article 395 of the Constitution explicitly repealed the Indian Independence Act, 1947 and the Government of India Act, 1935. The Constitution derives supreme authority from 'We, the People', not from British statutes.",
            "ta": "கூற்றுகள் 1, 2 மற்றும் 4 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் அரசியலமைப்பின் உறுப்பு 395 இந்திய சுதந்திரச் சட்டம் 1947 ஐ வெளிப்படையாக ரத்து செய்தது. அரசியலமைப்பு தனது உயர்ந்த அதிகாரத்தை பிரிட்டிஷ் சட்டங்களிலிருந்து அல்ல, 'மக்களாகிய நம்மிடம்' இருந்தே பெறுகிறது."
        },
        "why_not_others": {
            "A": {"en": "Correct. Statements 1, 2, and 4 accurately describe adoption date, popular sovereignty, and preambular record.", "ta": "சரி. கூற்றுகள் 1, 2 மற்றும் 4 ஏற்றுக்கொள்ளப்பட்ட நாள், மக்களின் இறையாண்மை மற்றும் முகவுரைப் பதிவைத் துல்லியமாக விவரிக்கின்றன."},
            "B": {"en": "Incorrect. Statement 3 is wrong (repealed by Art 395).", "ta": "தவறு. கூற்று 3 தவறானது (உறுப்பு 395 ஆல் ரத்து செய்யப்பட்டது)."},
            "C": {"en": "Incorrect. Includes statement 3 which is false.", "ta": "தவறு. தவறான கூற்று 3 ஐ உள்ளடக்கியுள்ளது."},
            "D": {"en": "Incorrect. Statement 3 is false.", "ta": "தவறு. கூற்று 3 தவறானது."}
        },
        "tnpsc_tip": {"en": "Date in Preamble = 26th November 1949 (Adoption/Enactment). Date of Commencement = 26th January 1950. Indian Independence Act 1947 was repealed by Art 395.", "ta": "முகவுரையில் உள்ள நாள் = 26 நவம்பர் 1949 (ஏற்றுக்கொள்ளப்பட்ட நாள்). நடைமுறைக்கு வந்த நாள் = 26 ஜனவரி 1950. 1947 சுதந்திரச் சட்டம் உறுப்பு 395 ஆல் ரத்து செய்யப்பட்டது."}
    },

    # 14. Multi-statement Analytical - 42nd Amendment Act 1976
    {
        "id": "PRE_H_014",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Multi-statement Analytical",
        "question": {
            "en": "Consider the following statements regarding the 42nd Constitutional Amendment Act, 1976 in relation to the Preamble:\n1. It added three new words: 'Socialist', 'Secular', and 'Integrity'.\n2. 'Socialist' and 'Secular' were inserted between 'Sovereign' and 'Democratic'.\n3. 'Integrity' was added after 'Unity and' in the Fraternity section.\n4. The Preamble has been amended twice in Indian constitutional history.\nWhich of the statements given above are CORRECT?",
            "ta": "முகவுரை தொடர்பான 1976 இன் 42வது அரசியலமைப்பு திருத்தச் சட்டம் பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. இது மூன்று புதிய சொற்களைச் சேர்த்தது: 'சமதர்ம', 'மதச்சார்பற்ற' மற்றும் 'ஒருமைப்பாடு'.\n2. 'சமதர்ம' மற்றும் 'மதச்சார்பற்ற' ஆகியவை 'இறையாண்மை' மற்றும் 'ஜனநாயக' ஆகியவற்றிற்கு இடையில் செருகப்பட்டன.\n3. சகோதரத்துவப் பகுதியில் 'ஒற்றுமை மற்றும்' என்பதற்குப் பின் 'ஒருமைப்பாடு' சேர்க்கப்பட்டது.\n4. இந்திய அரசியலமைப்பு வரலாற்றில் முகவுரை இதுவரை இரண்டு முறை திருத்தப்பட்டுள்ளது.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?"
        },
        "options": [
            {
                "id": "A",
                "en": "1, 2 and 3 only",
                "ta": "1, 2 மற்றும் 3 மட்டுமே"
            },
            {
                "id": "B",
                "en": "1 and 4 only",
                "ta": "1 மற்றும் 4 மட்டுமே"
            },
            {
                "id": "C",
                "en": "2 and 4 only",
                "ta": "2 மற்றும் 4 மட்டுமே"
            },
            {
                "id": "D",
                "en": "1, 2, 3 and 4",
                "ta": "அனைத்தும் (1, 2, 3 மற்றும் 4)"
            }
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Statements 1, 2, and 3 are correct. Statement 4 is incorrect because the Preamble has been amended ONLY ONCE so far—by the 42nd Constitutional Amendment Act, 1976.",
            "ta": "கூற்றுகள் 1, 2 மற்றும் 3 சரியானவை. கூற்று 4 தவறானது, ஏனெனில் முகவுரை இதுவரை ஒரே ஒரு முறை மட்டுமே (1976 இன் 42வது திருத்தச் சட்டத்தால்) திருத்தப்பட்டுள்ளது."
        },
        "why_not_others": {
            "A": {"en": "Correct. Statements 1, 2, and 3 accurately specify the 3 words and their exact textual placement.", "ta": "சரி. கூற்றுகள் 1, 2 மற்றும் 3 மூன்று சொற்களையும் அவற்றின் துல்லியமான இடத்தையும் குறிப்பிடுகின்றன."},
            "B": {"en": "Incorrect. Statement 4 is false; Preamble amended only ONCE, not twice.", "ta": "தவறு. கூற்று 4 தவறானது; முகவுரை இருமுறை அல்ல, ஒரே ஒரு முறை திருத்தப்பட்டது."},
            "C": {"en": "Incorrect. Statement 4 is false.", "ta": "தவறு. கூற்று 4 தவறானது."},
            "D": {"en": "Incorrect. Statement 4 is false.", "ta": "தவறு. கூற்று 4 தவறானது."}
        },
        "tnpsc_tip": {"en": "Preamble amended ONLY ONCE (42nd CAA 1976). Added 3 words: Socialist, Secular, Integrity. S-S-S-D-R order; 'Unity and Integrity of the Nation'.", "ta": "முகவுரை திருத்தப்பட்டது ஒரே ஒரு முறை மட்டுமே (42வது CAA 1976). சேர்க்கப்பட்ட 3 சொற்கள்: சமதர்ம, மதச்சார்பற்ற, ஒருமைப்பாடு."}
    },

    # 15. Multi-statement Analytical - Republic & Democracy
    {
        "id": "PRE_H_015",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Multi-statement Analytical",
        "question": {
            "en": "Consider the following statements comparing Democratic and Republican polities:\n1. In a Republic, political sovereignty is vested in the people and there is an absence of any privileged class.\n2. In a democratic polity, the Head of State is always directly elected by universal adult suffrage.\n3. The President of India is an indirectly elected Head of State for a fixed tenure of five years.\n4. All democratic nations are automatically Republics.\nWhich of the statements given above are CORRECT?",
            "ta": "ஜனநாயக மற்றும் குடியரசு அமைப்புகளை ஒப்பிடும் பின்வரும் கூற்றுகளைக் கருதுக:\n1. ஒரு குடியரசில், அரசியல் இறையாண்மை மக்களிடம் உள்ளது மற்றும் சலுகை பெற்ற வர்க்கம் எதுவும் இல்லை.\n2. ஒரு ஜனநாயக அமைப்பில், நாட்டின் தலைவர் எப்போதும் உலகளாவிய வயதுவந்தோர் வாக்குரிமை மூலம் நேரடியாகத் தேர்ந்தெடுக்கப்படுகிறார்.\n3. இந்தியக் குடியரசுத் தலைவர் ஐந்து ஆண்டுகள் குறிப்பிட்ட காலத்திற்கு மறைமுகமாகத் தேர்ந்தெடுக்கப்பட்ட நாட்டின் தலைவராவார்.\n4. அனைத்து ஜனநாயக நாடுகளும் தானாகவே குடியரசுகளாகும்.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?"
        },
        "options": [
            {
                "id": "A",
                "en": "1 and 3 only",
                "ta": "1 மற்றும் 3 மட்டுமே"
            },
            {
                "id": "B",
                "en": "1, 2 and 3 only",
                "ta": "1, 2 மற்றும் 3 மட்டுமே"
            },
            {
                "id": "C",
                "en": "2 and 4 only",
                "ta": "2 மற்றும் 4 மட்டுமே"
            },
            {
                "id": "D",
                "en": "1, 3 and 4 only",
                "ta": "1, 3 மற்றும் 4 மட்டுமே"
            }
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Statements 1 and 3 are correct. Statement 2 is incorrect because the Head of State can be indirectly elected (like in India) or hereditary (like in UK monarchy). Statement 4 is incorrect because Britain is a democracy but not a republic (it is a constitutional monarchy).",
            "ta": "கூற்றுகள் 1 மற்றும் 3 சரியானவை. கூற்று 2 தவறானது, ஏனெனில் நாட்டின் தலைவர் மறைமுகமாகத் தேர்ந்தெடுக்கப்படலாம் (இந்தியா போல்) அல்லது பரம்பரையாக இருக்கலாம் (பிரிட்டன் போல்). கூற்று 4 தவறானது, ஏனெனில் பிரிட்டன் ஒரு ஜனநாயகம் ஆனால் குடியரசு அல்ல (அது ஒரு அரசியலமைப்பு முடியாட்சி)."
        },
        "why_not_others": {
            "A": {"en": "Correct. Statements 1 and 3 correctly state republic features and Indian President's election.", "ta": "சரி. கூற்றுகள் 1 மற்றும் 3 குடியரசு அம்சங்களையும் இந்தியக் குடியரசுத் தலைவர் தேர்தலையும் சரியாகக் கூறுகின்றன."},
            "B": {"en": "Incorrect. Statement 2 is false (Head of State can be indirectly elected or hereditary).", "ta": "தவறு. கூற்று 2 தவறானது."},
            "C": {"en": "Incorrect. Statements 2 and 4 are both false.", "ta": "தவறு. கூற்றுகள் 2 மற்றும் 4 இரண்டும் தவறானவை."},
            "D": {"en": "Incorrect. Statement 4 is false (UK is democratic but a Monarchy, not a Republic).", "ta": "தவறு. கூற்று 4 தவறானது."}
        },
        "tnpsc_tip": {"en": "Democracy can be Monarchy (UK) or Republic (India/USA). Republic = Elected Head of State (Direct or Indirect) + No privileged class.", "ta": "ஜனநாயகம் முடியாட்சியாகவோ (பிரிட்டன்) அல்லது குடியரசாகவோ (இந்தியா/அமெரிக்கா) இருக்கலாம். குடியரசு = தேர்ந்தெடுக்கப்பட்ட நாட்டின் தலைவர் (நேரடி அல்லது மறைமுக) + சலுகை பெற்ற வர்க்கமின்மை."}
    },

    # 16. Multi-statement Analytical - Liberty in Preamble vs Part III
    {
        "id": "PRE_H_016",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Multi-statement Analytical",
        "question": {
            "en": "Consider the following statements regarding 'Liberty' in the Preamble:\n1. The Preamble promises liberty of thought, expression, belief, faith, and worship.\n2. Freedom of speech and expression under Article 19(1)(a) operationalizes liberty of thought and expression.\n3. Freedom of conscience and practice under Articles 25 to 28 operationalizes liberty of belief, faith, and worship.\n4. Liberty in the Preamble is absolute and cannot be subjected to reasonable restrictions.\nWhich of the statements given above are CORRECT?",
            "ta": "முகவுரையில் உள்ள 'சுதந்திரம்' பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. முகவுரை எண்ணம், வெளிப்பாடு, நம்பிக்கை, சமயம் மற்றும் வழிபாட்டு சுதந்திரத்திற்கு வாக்குறுதி அளிக்கிறது.\n2. உறுப்பு 19(1)(a) இன் கீழ் உள்ள பேச்சு மற்றும் கருத்து வெளிப்பாட்டு சுதந்திரம் எண்ணம் மற்றும் வெளிப்பாட்டு சுதந்திரத்தை நடைமுறைப்படுத்துகிறது.\n3. உறுப்புகள் 25 முதல் 28 வரையிலான மனசாட்சி மற்றும் மதப் பழக்க சுதந்திரம் நம்பிக்கை, சமயம் மற்றும் வழிபாட்டு சுதந்திரத்தை நடைமுறைப்படுத்துகிறது.\n4. முகவுரையில் உள்ள சுதந்திரம் வரம்பற்றது மற்றும் நியாயமான கட்டுப்பாடுகளுக்கு உட்படுத்த முடியாது.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?"
        },
        "options": [
            {
                "id": "A",
                "en": "1, 2 and 3 only",
                "ta": "1, 2 மற்றும் 3 மட்டுமே"
            },
            {
                "id": "B",
                "en": "1 and 4 only",
                "ta": "1 மற்றும் 4 மட்டுமே"
            },
            {
                "id": "C",
                "en": "2 and 4 only",
                "ta": "2 மற்றும் 4 மட்டுமே"
            },
            {
                "id": "D",
                "en": "1, 2, 3 and 4",
                "ta": "அனைத்தும் (1, 2, 3 மற்றும் 4)"
            }
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Statements 1, 2, and 3 are correct. Statement 4 is incorrect because liberty in the Preamble is not absolute but qualified; it is subject to reasonable restrictions specified in Part III of the Constitution.",
            "ta": "கூற்றுகள் 1, 2 மற்றும் 3 சரியானவை. கூற்று 4 தவறானது, ஏனெனில் முகவுரையில் உள்ள சுதந்திரம் வரம்பற்றது அல்ல, மாறாக நிபந்தனைக்குட்பட்டது; இது அரசியலமைப்பின் பகுதி III இல் குறிப்பிடப்பட்டுள்ள நியாயமான கட்டுப்பாடுகளுக்கு உட்பட்டது."
        },
        "why_not_others": {
            "A": {"en": "Correct. Statements 1, 2, and 3 accurately link Preamble liberty to Articles 19 and 25-28.", "ta": "சரி. கூற்றுகள் 1, 2 மற்றும் 3 முகவுரை சுதந்திரத்தை உறுப்புகள் 19 மற்றும் 25-28 உடன் துல்லியமாக இணைக்கின்றன."},
            "B": {"en": "Incorrect. Statement 4 is false (liberty is qualified, not absolute).", "ta": "தவறு. கூற்று 4 தவறானது."},
            "C": {"en": "Incorrect. Statement 4 is false.", "ta": "தவறு. கூற்று 4 தவறானது."},
            "D": {"en": "Incorrect. Statement 4 is false.", "ta": "தவறு. கூற்று 4 தவறானது."}
        },
        "tnpsc_tip": {"en": "5 types of Liberty in Preamble: Thought, Expression, Belief, Faith, Worship. Liberty is QUALIFIED (subject to reasonable restrictions under Art 19/25).", "ta": "முகவுரையில் 5 வகையான சுதந்திரங்கள் உள்ளன. சுதந்திரம் வரம்பிற்குட்பட்டது (உறுப்புகள் 19/25 இன் கீழ் நியாயமான கட்டுப்பாடுகளுக்கு உட்பட்டது)."}
    },

    # 17. Multi-statement Analytical - Equality Provisions
    {
        "id": "PRE_H_017",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Multi-statement Analytical",
        "question": {
            "en": "Consider the following statements regarding the dimensions of 'Equality' in the Preamble:\n1. Civic equality is secured by Articles 14 to 18 in Part III.\n2. Political equality is secured by Article 325 (non-discriminatory electoral rolls) and Article 326 (adult suffrage).\n3. Economic equality is promoted through Directive Principles under Article 39 (equal pay and prevention of wealth concentration).\n4. Preamble equality mandates identical mathematical treatment of all citizens regardless of socio-economic inequality.\nWhich of the statements given above are CORRECT?",
            "ta": "முகவுரையில் உள்ள 'சமத்துவத்தின்' பரிமாணங்கள் பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. குடிமை சமத்துவம் பகுதி III இல் உள்ள உறுப்புகள் 14 முதல் 18 வரை பாதுகாக்கப்படுகிறது.\n2. அரசியல் சமத்துவம் உறுப்பு 325 (பாகுபாடற்ற வாக்காளர் பட்டியல்) மற்றும் உறுப்பு 326 (வயதுவந்தோர் வாக்குரிமை) மூலம் பாதுகாக்கப்படுகிறது.\n3. பொருளாதார சமத்துவம் உறுப்பு 39 இன் கீழ் உள்ள வழிகாட்டு நெறிமுறைகள் மூலம் (சம வேலைக்கு சம ஊதியம் மற்றும் செல்வக் குவிப்பு தடுப்பு) ஊக்குவிக்கப்படுகிறது.\n4. முகவுரை சமத்துவம் சமூக-பொருளாதார ஏற்றத்தாழ்வுகளைப் பொருட்படுத்தாமல் அனைத்து குடிமக்களுக்கும் ஒரே மாதிரியான கணித சிகிச்சையைக் கட்டாயமாக்குகிறது.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?"
        },
        "options": [
            {
                "id": "A",
                "en": "1, 2 and 3 only",
                "ta": "1, 2 மற்றும் 3 மட்டுமே"
            },
            {
                "id": "B",
                "en": "1 and 4 only",
                "ta": "1 மற்றும் 4 மட்டுமே"
            },
            {
                "id": "C",
                "en": "2, 3 and 4 only",
                "ta": "2, 3 மற்றும் 4 மட்டுமே"
            },
            {
                "id": "D",
                "en": "1, 2, 3 and 4",
                "ta": "அனைத்தும் (1, 2, 3 மற்றும் 4)"
            }
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Statements 1, 2, and 3 are correct. Statement 4 is incorrect because constitutional equality demands equal treatment among equals (substantive equality), allowing protective discrimination/affirmative action (Articles 15(4) & 16(4)) to uplift disadvantaged classes.",
            "ta": "கூற்றுகள் 1, 2 மற்றும் 3 சரியானவை. கூற்று 4 தவறானது, ஏனெனில் அரசியலமைப்பு சமத்துவம் சமமானவர்களிடையே சமமான சிகிச்சையைக் கோருகிறது (நடைமுறைச் சமத்துவம்); இது பின்தங்கிய வகுப்பினரை உயர்த்த பாதுகாப்பு பாகுபாட்டை (உறுப்புகள் 15(4) & 16(4)) அனுமதிக்கிறது."
        },
        "why_not_others": {
            "A": {"en": "Correct. Statements 1, 2, and 3 accurately categorize Civic, Political, and Economic equality provisions.", "ta": "சரி. கூற்றுகள் 1, 2 மற்றும் 3 குடிமை, அரசியல் மற்றும் பொருளாதார சமத்துவ விதிகளைத் துல்லியமாக வகைப்படுத்துகின்றன."},
            "B": {"en": "Incorrect. Statement 4 is false (ignores substantive equality).", "ta": "தவறு. கூற்று 4 தவறானது."},
            "C": {"en": "Incorrect. Statement 4 is false.", "ta": "தவறு. கூற்று 4 தவறானது."},
            "D": {"en": "Incorrect. Statement 4 is false.", "ta": "தவறு. கூற்று 4 தவறானது."}
        },
        "tnpsc_tip": {"en": "3 Dimensions of Equality in Preamble: Civic (Art 14-18), Political (Art 325-326), Economic (Art 39 DPSP).", "ta": "முகவுரையில் சமத்துவத்தின் 3 பரிமாணங்கள்: குடிமை (உறுப்புகள் 14-18), அரசியல் (உறுப்புகள் 325-326), பொருளாதாரம் (உறுப்பு 39 DPSP)."}
    },

    # 18. Multi-statement Analytical - Fraternity & Fundamental Duties
    {
        "id": "PRE_H_018",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Multi-statement Analytical",
        "question": {
            "en": "Consider the following statements regarding 'Fraternity' and constitutional provisions promoting it:\n1. The system of single citizenship under the Constitution fosters a feeling of oneness and brotherhood.\n2. Article 51A(e) makes it a Fundamental Duty of every citizen to promote harmony and the spirit of common brotherhood.\n3. K.M. Munshi observed that 'dignity of the individual' means that every human personality is sacred.\n4. 'Integrity' was part of the original Preamble text adopted on 26th November 1949.\nWhich of the statements given above are CORRECT?",
            "ta": "முகவுரையில் உள்ள 'சகோதரத்துவம்' மற்றும் அதை ஊக்குவிக்கும் அரசியலமைப்பு விதிகள் பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. அரசியலமைப்பின் கீழ் உள்ள ஒற்றைக் குடியுரிமை முறை மக்களிடையே ஒற்றுமை மற்றும் சகோதரத்துவ உணர்வை வளர்க்கிறது.\n2. உறுப்பு 51A(e) நல்லிணக்கத்தையும் பொதுவான சகோதரத்துவ உணர்வையும் ஊக்குவிப்பதை ஒவ்வொரு குடிமகனின் அடிப்படை கடமையாக்குகிறது.\n3. 'நபரின் கண்ணியம்' என்பது ஒவ்வொரு மனித ஆளுமையும் புனிதமானது என்று பொருள் தருவதாக கே.எம். முன்ஷி குறிப்பிட்டார்.\n4. 'ஒருமைப்பாடு' என்பது 26 நவம்பர் 1949 அன்று ஏற்றுக்கொள்ளப்பட்ட மூல முகவுரை உரையின் ஒரு பகுதியாகும்.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?"
        },
        "options": [
            {
                "id": "A",
                "en": "1, 2 and 3 only",
                "ta": "1, 2 மற்றும் 3 மட்டுமே"
            },
            {
                "id": "B",
                "en": "1 and 4 only",
                "ta": "1 மற்றும் 4 மட்டுமே"
            },
            {
                "id": "C",
                "en": "2 and 4 only",
                "ta": "2 மற்றும் 4 மட்டுமே"
            },
            {
                "id": "D",
                "en": "1, 2, 3 and 4",
                "ta": "அனைத்தும் (1, 2, 3 மற்றும் 4)"
            }
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Statements 1, 2, and 3 are correct. Statement 4 is incorrect because 'Integrity' was NOT part of the original Preamble in 1949; it was added by the 42nd Constitutional Amendment Act of 1976.",
            "ta": "கூற்றுகள் 1, 2 மற்றும் 3 சரியானவை. கூற்று 4 தவறானது, ஏனெனில் 'ஒருமைப்பாடு' 1949 இல் மூல முகவுரையின் பகுதியாக இருக்கவில்லை; இது 1976 இன் 42வது திருத்தச் சட்டத்தால் சேர்க்கப்பட்டது."
        },
        "why_not_others": {
            "A": {"en": "Correct. Statements 1, 2, and 3 accurately describe fraternity mechanisms and Munshi's quote.", "ta": "சரி. கூற்றுகள் 1, 2 மற்றும் 3 சகோதரத்துவ வழிமுறைகளையும் முன்ஷியின் கருத்தையும் துல்லியமாக விவரிக்கின்றன."},
            "B": {"en": "Incorrect. Statement 4 is false ('Integrity' added in 1976).", "ta": "தவறு. கூற்று 4 தவறானது."},
            "C": {"en": "Incorrect. Statement 4 is false.", "ta": "தவறு. கூற்று 4 தவறானது."},
            "D": {"en": "Incorrect. Statement 4 is false.", "ta": "தவறு. கூற்று 4 தவறானது."}
        },
        "tnpsc_tip": {"en": "Fraternity is strengthened by: (1) Single Citizenship (Art 5-11), (2) Fundamental Duty Art 51A(e). 'Integrity' added in 1976.", "ta": "சகோதரத்துவம் வலுப்படுத்தப்படுவது: (1) ஒற்றைக் குடியுரிமை, (2) அடிப்படை கடமை உறுப்பு 51A(e). 'ஒருமைப்பாடு' 1976 இல் சேர்க்கப்பட்டது."}
    },

    # 19. Multi-statement Analytical - Social and Economic Justice & DPSP
    {
        "id": "PRE_H_019",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Multi-statement Analytical",
        "question": {
            "en": "Consider the following statements regarding 'Justice—social, economic and political' in the Preamble:\n1. Social justice denotes equal treatment of all citizens without social distinction based on caste, race, religion, or sex.\n2. Economic justice denotes non-discrimination between citizens on the basis of wealth, income, or property.\n3. Distributive justice is achieved by combining social justice and economic justice.\n4. Social and economic justice are enforceable as standalone Fundamental Rights under Article 32 without enabling legislation.\nWhich of the statements given above are CORRECT?",
            "ta": "முகவுரையில் உள்ள 'நீதி—சமூக, பொருளாதார மற்றும் அரசியல்' பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. சமூக நீதி என்பது சாதி, இனம், மதம் அல்லது பாலினத்தின் அடிப்படையில் எந்தச் சமூக பாகுபாடும் இன்றி அனைத்து குடிமக்களையும் சமமாக நடத்துவதைக் குறிக்கிறது.\n2. பொருளாதார நீதி என்பது செல்வம், வருமானம் அல்லது சொத்தின் அடிப்படையில் குடிமக்களிடையே பாகுபாடு காட்டாததைக் குறிக்கிறது.\n3. சமூக நீதியும் பொருளாதார நீதியும் இணைந்து 'பகிர்வு நீதியை' அடைகின்றன.\n4. சமூக மற்றும் பொருளாதார நீதி ஆகியவை சட்டம் ஏதுமின்றி உறுப்பு 32 இன் கீழ் தனித்த அடிப்படை உரிமைகளாக நேரடியாக அமல்படுத்தக்கூடியவை.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?"
        },
        "options": [
            {
                "id": "A",
                "en": "1, 2 and 3 only",
                "ta": "1, 2 மற்றும் 3 மட்டுமே"
            },
            {
                "id": "B",
                "en": "1 and 4 only",
                "ta": "1 மற்றும் 4 மட்டுமே"
            },
            {
                "id": "C",
                "en": "2 and 4 only",
                "ta": "2 மற்றும் 4 மட்டுமே"
            },
            {
                "id": "D",
                "en": "1, 2, 3 and 4",
                "ta": "அனைத்தும் (1, 2, 3 மற்றும் 4)"
            }
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Statements 1, 2, and 3 are correct. Statement 4 is incorrect because Preamble objectives (and Directive Principles in Part IV which operationalize socio-economic justice) are non-justiciable and cannot be enforced directly via Article 32 writs without statutory backing.",
            "ta": "கூற்றுகள் 1, 2 மற்றும் 3 சரியானவை. கூற்று 4 தவறானது, ஏனெனில் முகவுரை இலக்குகள் (மற்றும் பகுதி IV வழிகாட்டு நெறிமுறைகள்) நீதிமன்றத்தால் நிலைநிறுத்த முடியாதவை; சட்டப்பூர்வ ஆதரவின்றி உறுப்பு 32 பேராணைகள் மூலம் நேரடியாக அமல்படுத்த முடியாது."
        },
        "why_not_others": {
            "A": {"en": "Correct. Statements 1, 2, and 3 correctly define Social, Economic, and Distributive justice.", "ta": "சரி. கூற்றுகள் 1, 2 மற்றும் 3 சமூக, பொருளாதார மற்றும் பகிர்வு நீதியைச் சரியாக வரையறுக்கின்றன."},
            "B": {"en": "Incorrect. Statement 4 is false (Preamble objectives are non-justiciable).", "ta": "தவறு. கூற்று 4 தவறானது."},
            "C": {"en": "Incorrect. Statement 4 is false.", "ta": "தவறு. கூற்று 4 தவறானது."},
            "D": {"en": "Incorrect. Statement 4 is false.", "ta": "தவறு. கூற்று 4 தவறானது."}
        },
        "tnpsc_tip": {"en": "Social + Economic Justice = Distributive Justice. Inspired by Russian Revolution (1917). Implemented through DPSP (Part IV).", "ta": "சமூக + பொருளாதார நீதி = பகிர்வு நீதி. ரஷ்யப் புரட்சியால் (1917) தூண்டப்பட்டது. DPSP (பகுதி IV) மூலம் செயல்படுத்தப்படுகிறது."}
    },

    # 20. Multi-statement Analytical - Preamble in Judicial Interpretation of Rights
    {
        "id": "PRE_H_020",
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": "Multi-statement Analytical",
        "question": {
            "en": "Consider the following statements regarding the judicial evolution of the Preamble's constitutional status:\n1. In Berubari Union case (1960), the Supreme Court held that the Preamble is NOT a part of the Constitution.\n2. In Kesavananda Bharati case (1973), the Supreme Court rejected the Berubari opinion and held that the Preamble IS a part of the Constitution.\n3. In LIC of India case (1995), the Supreme Court again held that the Preamble is an integral part of the Constitution.\n4. The Preamble can independently override express provisions of Article 19 in case of ambiguity.\nWhich of the statements given above are CORRECT?",
            "ta": "முகவுரையின் அரசியலமைப்பு அந்தஸ்தின் நீதித்துறை வளர்ச்சி பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. பெருபாரி யூனியன் வழக்கில் (1960), முகவுரை அரசியலமைப்பின் ஒரு பகுதி அல்ல என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது.\n2. கேசவாநந்த பாரதி வழக்கில் (1973), உச்ச நீதிமன்றம் பெருபாரி கருத்தை நிராகரித்து, முகவுரை அரசியலமைப்பின் ஒரு பகுதியாகும் என்று தீர்ப்பளித்தது.\n3. எல்ஐசி வழக்கில் (1995), முகவுரை அரசியலமைப்பின் ஒருங்கிணைந்த பகுதி என்று உச்ச நீதிமன்றம் மீண்டும் தீர்ப்பளித்தது.\n4. தெளிவின்மை எழும் போது முகவுரை உறுப்பு 19 இன் வெளிப்படையான விதிகளைத் தனிச்சையாக மேலோங்க முடியும்.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?"
        },
        "options": [
            {
                "id": "A",
                "en": "1, 2 and 3 only",
                "ta": "1, 2 மற்றும் 3 மட்டுமே"
            },
            {
                "id": "B",
                "en": "1 and 4 only",
                "ta": "1 மற்றும் 4 மட்டுமே"
            },
            {
                "id": "C",
                "en": "2 and 4 only",
                "ta": "2 மற்றும் 4 மட்டுமே"
            },
            {
                "id": "D",
                "en": "1, 2, 3 and 4",
                "ta": "அனைத்தும் (1, 2, 3 மற்றும் 4)"
            }
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Statements 1, 2, and 3 are correct. Statement 4 is incorrect because while the Preamble aids interpretation, it CANNOT independently override or supersede clear, express provisions of the Constitution.",
            "ta": "கூற்றுகள் 1, 2 மற்றும் 3 சரியானவை. கூற்று 4 தவறானது, ஏனெனில் முகவுரை விளக்கத்திற்கு உதவும் என்றாலும், அரசியலமைப்பின் தெளிவான, வெளிப்படையான விதிகளை சுயாதீனமாக மேலோங்க முடியாது."
        },
        "why_not_others": {
            "A": {"en": "Correct. Statements 1, 2, and 3 accurately trace Berubari (1960) -> Kesavananda (1973) -> LIC (1995).", "ta": "சரி. கூற்றுகள் 1, 2 மற்றும் 3 பெருபாரி (1960) -> கேசவாநந்த (1973) -> எல்ஐசி (1995) நீதித்துறை வளர்ச்சியைத் துல்லியமாகக் காட்டுகின்றன."},
            "B": {"en": "Incorrect. Statement 4 is false (Preamble cannot override clear express text).", "ta": "தவறு. கூற்று 4 தவறானது."},
            "C": {"en": "Incorrect. Statement 4 is false.", "ta": "தவறு. கூற்று 4 தவறானது."},
            "D": {"en": "Incorrect. Statement 4 is false.", "ta": "தவறு. கூற்று 4 தவறானது."}
        },
        "tnpsc_tip": {"en": "Judicial History: Berubari (1960) = NOT part. Kesavananda (1973) = IS part (Overruled Berubari). LIC of India (1995) = Integral part.", "ta": "நீதித்துறை வரலாறு: பெருபாரி (1960) = பகுதி அல்ல. கேசவாநந்த (1973) = பகுதி (பெருபாரியை ரத்து செய்தது). எல்ஐசி (1995) = ஒருங்கிணைந்த பகுதி."}
    }
]

print("Script base populated with 20 questions.")
