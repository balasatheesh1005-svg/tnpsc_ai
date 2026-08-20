# preamble_easy_q1_25.py
from scratch_preamble_easy_helper import make_q

def get_q1_25():
    qs = []

    # Q1 - Direct - Ans A
    qs.append(make_q(
        q_id="PRE_E_001", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Easy", question_type="Direct",
        q_en="Which country was the first in the world to begin its Constitution with a Preamble?",
        q_ta="உலகிலேயே தனது அரசியலமைப்பை முகவுரையுடன் தொடங்கிய முதல் நாடு எது?",
        opts_en=["United States of America", "United Kingdom", "France", "Ireland"],
        opts_ta=["அமெரிக்க ஐக்கிய நாடுகள்", "ஐக்கிய இராச்சியம் (பிரிட்டன்)", "பிரான்ஸ்", "அயர்லாந்து"],
        correct_ans="A",
        exp_en="The American Constitution was the first in the world to begin with a Preamble. India followed this constitutional precedent.",
        exp_ta="அமெரிக்க அரசியலமைப்புதான் உலகிலேயே முதன்முதலில் முகவுரையுடன் தொடங்கியது. இந்தியா இந்த முன்மாதிரியைப் பின்பற்றியது.",
        wno_dict={
            "A": {"en": "Correct. USA was the first nation to introduce a Preamble.", "ta": "சரி. அமெரிக்காவே முதன்முதலில் முகவுரையை அறிமுகப்படுத்திய நாடு."},
            "B": {"en": "Incorrect. UK has an unwritten Constitution.", "ta": "தவறு. பிரிட்டன் எழுதப்படாத அரசியலமைப்பைக் கொண்டுள்ளது."},
            "C": {"en": "Incorrect. France adopted a preamble later.", "ta": "தவறு. பிரான்ஸ் பின்னர் முகவுரையை ஏற்றுக்கொண்டது."},
            "D": {"en": "Incorrect. Ireland also adopted it later.", "ta": "தவறு. அயர்லாந்தும் பின்னரே ஏற்றுக்கொண்டது."}
        },
        tip_en="Preamble practice started with the US Constitution (1787).",
        tip_ta="முகவுரை நடைமுறை அமெரிக்க அரசியலமைப்பில் (1787) தொடங்கியது.",
        rev_en="First country to have a Preamble = USA.",
        rev_ta="முகவுரையைக் கொண்ட முதல் நாடு = அமெரிக்கா.",
        sources=["Preamble Notes Part 1", "M. Laxmikanth"],
        bloom="Remember", est_sec=30, pyq_sim="High", tags=["Preamble", "USA", "Origin"]
    ))

    # Q2 - Direct - Ans B
    qs.append(make_q(
        q_id="PRE_E_002", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Easy", question_type="Direct",
        q_en="The Preamble to the Indian Constitution is based on which historic resolution moved in the Constituent Assembly?",
        q_ta="இந்திய அரசியலமைப்பின் முகவுரை அரசியலமைப்புச் சபையில் முன்மொழியப்பட்ட எந்த வரலாற்றுச் சிறப்புமிக்க தீர்மானத்தின் அடிப்படையில் அமைக்கப்பட்டது?",
        opts_en=["Quit India Resolution", "Objectives Resolution", "Cabinet Mission Plan", "Independence Resolution"],
        opts_ta=["வெள்ளையனே வெளியேறு தீர்மானம்", "குறிக்கோள் தீர்மானம் (Objectives Resolution)", "அமைச்சரவை தூதுக்குழு திட்டம்", "சுதந்திரத் தீர்மானம்"],
        correct_ans="B",
        exp_en="The Preamble is based on the 'Objectives Resolution', drafted and moved by Pandit Jawaharlal Nehru on December 13, 1946.",
        exp_ta="முகவுரை 1946 டிசம்பர் 13 அன்று பண்டிட் ஜவஹர்லால் நேருவால் உருவாக்கப்பட்டு முன்மொழியப்பட்ட 'குறிக்கோள் தீர்மானத்தின்' அடிப்படையில் அமைந்தது.",
        wno_dict={
            "A": {"en": "Incorrect. Quit India Resolution was passed in 1942.", "ta": "தவறு. வெள்ளையனே வெளியேறு தீர்மானம் 1942 இல் நிறைவேற்றப்பட்டது."},
            "B": {"en": "Correct. Objectives Resolution moved by Nehru in 1946 formed the basis of Preamble.", "ta": "சரி. 1946 இல் நேருவால் முன்மொழியப்பட்ட குறிக்கோள் தீர்மானம் முகவுரைக்கு அடிப்படையாக அமைந்தது."},
            "C": {"en": "Incorrect. Cabinet Mission Plan formed Constituent Assembly structure.", "ta": "தவறு. அமைச்சரவை தூதுக்குழு திட்டம் அரசியலமைப்புச் சபை அமைப்பை உருவாக்கியது."},
            "D": {"en": "Incorrect. Independence Resolution was separate.", "ta": "தவறு. சுதந்திரத் தீர்மானம் தனியானது."}
        },
        tip_en="Objectives Resolution moved on Dec 13, 1946 and adopted on Jan 22, 1947.",
        tip_ta="குறிக்கோள் தீர்மானம் முன்மொழியப்பட்ட நாள்: டிசம்பர் 13, 1946; ஏற்றுக்கொள்ளப்பட்ட நாள்: ஜனவரி 22, 1947.",
        rev_en="Preamble source = Objectives Resolution (Jawaharlal Nehru).",
        rev_ta="முகவுரையின் மூலம் = குறிக்கோள் தீர்மானம் (ஜவஹர்லால் நேரு).",
        sources=["Preamble Notes Part 1"],
        bloom="Remember", est_sec=30, pyq_sim="Direct PYQ", tags=["Objectives Resolution", "Jawaharlal Nehru"]
    ))

    # Q3 - Conceptual - Ans C
    qs.append(make_q(
        q_id="PRE_E_003", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Easy", question_type="Conceptual",
        q_en="Who among the following constitutional experts described the Preamble as the 'Identity Card of the Constitution'?",
        q_ta="பின்வரும் அரசியலமைப்பு நிபுணர்களில் யார் முகவுரையை 'அரசியலமைப்பின் அடையாள அட்டை' என்று விவரித்தார்?",
        opts_en=["Dr. B.R. Ambedkar", "K.M. Munshi", "N.A. Palkhivala", "Sir Alladi Krishnaswami Ayyar"],
        opts_ta=["டாக்டர் பி.ஆர். அம்பேத்கர்", "கே.எம். முன்ஷி", "என்.ஏ. பால்கிவாலா", "சர் அல்லாடி கிருஷ்ணசாமி ஐயர்"],
        correct_ans="C",
        exp_en="Eminent jurist and constitutional expert N.A. Palkhivala called the Preamble the 'Identity Card of the Constitution'.",
        exp_ta="பிரபல சட்ட நிபுணர் என்.ஏ. பால்கிவாலா முகவுரையை 'அரசியலமைப்பின் அடையாள அட்டை' என்று அழைத்தார்.",
        wno_dict={
            "A": {"en": "Incorrect. Dr. Ambedkar called Article 32 the Heart and Soul of Constitution.", "ta": "தவறு. டாக்டர் அம்பேத்கர் உறுப்பு 32 ஐ அரசியலமைப்பின் இதயம் மற்றும் ஆன்மா என்றார்."},
            "B": {"en": "Incorrect. K.M. Munshi called it the Horoscope of Sovereign Democratic Republic.", "ta": "தவறு. கே.எம். முன்ஷி அதை இறையாண்மை ஜனநாயகக் குடியரசின் ஜாதகம் என்றார்."},
            "C": {"en": "Correct. N.A. Palkhivala coined 'Identity Card of the Constitution'.", "ta": "சரி. என்.ஏ. பால்கிவாலா 'அரசியலமைப்பின் அடையாள அட்டை' என்று குறிப்பிட்டவர்."},
            "D": {"en": "Incorrect. Alladi Krishnaswami Ayyar remarked it reflects what we dreamed so long.", "ta": "தவறு. அல்லாடி கிருஷ்ணசாமி ஐயர் நாம் கனவு கண்டதை முகவுரை வெளிப்படுத்துகிறது என்றார்."}
        },
        tip_en="Palkhivala = Identity Card; K.M. Munshi = Horoscope; Thakur Das Bhargava = Soul/Jewel.",
        tip_ta="பால்கிவாலா = அடையாள அட்டை; கே.எம். முன்ஷி = ஜாதகம்; பார்கவா = ஆன்மா/மாணிக்கம்.",
        rev_en="Identity Card of Constitution = N.A. Palkhivala.",
        rev_ta="அரசியலமைப்பின் அடையாள அட்டை = என்.ஏ. பால்கிவாலா.",
        sources=["Preamble Notes Part 1"],
        bloom="Remember", est_sec=30, pyq_sim="High", tags=["Palkhivala", "Identity Card", "Preamble Quotes"]
    ))

    # Q4 - Direct - Ans D
    qs.append(make_q(
        q_id="PRE_E_004", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Easy", question_type="Direct",
        q_en="On which date was the Constitution of India adopted by the Constituent Assembly as mentioned in the Preamble?",
        q_ta="முகவுரையில் குறிப்பிடப்பட்டுள்ளவாறு இந்திய அரசியலமைப்புச் சபையால் அரசியலமைப்பு ஏற்றுக்கொள்ளப்பட்ட நாள் எது?",
        opts_en=["26th January 1950", "15th August 1947", "26th January 1949", "26th November 1949"],
        opts_ta=["26 ஜனவரி 1950", "15 ஆகஸ்ட் 1947", "26 ஜனவரி 1949", "26 நவம்பர் 1949"],
        correct_ans="D",
        exp_en="The Preamble explicitly mentions 26th November 1949 as the date on which the people of India adopted, enacted, and gave to themselves the Constitution.",
        exp_ta="இந்திய மக்கள் அரசியலமைப்பை ஏற்றுக்கொண்டு, இயற்றி, தங்களுக்குத்தானே வழங்கிய நாளாக 26 நவம்பர் 1949 என்பதை முகவுரை வெளிப்படையாகக் குறிப்பிடுகிறது.",
        wno_dict={
            "A": {"en": "Incorrect. 26th January 1950 is the date of commencement (Republic Day).", "ta": "தவறு. 26 ஜனவரி 1950 என்பது நடைமுறைக்கு வந்த நாள் (குடியரசு தினம்)."},
            "B": {"en": "Incorrect. 15th August 1947 is Independence Day.", "ta": "தவறு. 15 ஆகஸ்ட் 1947 என்பது சுதந்திர தினம்."},
            "C": {"en": "Incorrect. Incorrect date.", "ta": "தவறு. தவறான நாள்."},
            "D": {"en": "Correct. 26th November 1949 is the Date of Adoption mentioned in the Preamble.", "ta": "சரி. 26 நவம்பர் 1949 என்பது முகவுரையில் உள்ள ஏற்றுக்கொள்ளப்பட்ட நாளாகும்."}
        },
        tip_en="TNPSC Trap: Adoption Date = 26 Nov 1949; Commencement Date = 26 Jan 1950.",
        tip_ta="TNPSC பொறி: ஏற்றுக்கொள்ளப்பட்ட நாள் = 26 நவம்பர் 1949; நடைமுறைக்கு வந்த நாள் = 26 ஜனவரி 1950.",
        rev_en="Date of Adoption in Preamble = 26th November 1949.",
        rev_ta="முகவுரையில் உள்ள ஏற்றுக்கொள்ளப்பட்ட நாள் = 26 நவம்பர் 1949.",
        sources=["Preamble Notes Part 1"],
        bloom="Remember", est_sec=30, pyq_sim="Direct PYQ", tags=["Date of Adoption", "26 November 1949"]
    ))

    # Q5 - Term / Meaning - Ans A
    qs.append(make_q(
        q_id="PRE_E_005", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Easy", question_type="Term / Meaning",
        q_en="What does the opening phrase 'WE, THE PEOPLE OF INDIA' in the Preamble signify?",
        q_ta="முகவுரையில் உள்ள 'இந்திய மக்களாகிய நாம்' என்ற தொடக்கத் தொடர் எதனைக் குறிக்கிறது?",
        opts_en=[
            "Popular Sovereignty (Ultimate power resides in the people)",
            "Parliamentary Sovereignty (Parliament is supreme)",
            "Judicial Supremacy (Supreme Court is ultimate source)",
            "Presidential Authority (President is absolute ruler)"
        ],
        opts_ta=[
            "மக்களின் இறையாண்மை (இறுதி அதிகாரம் மக்களிடம் உள்ளது)",
            "பாராளுமன்ற இறையாண்மை (பாராளுமன்றமே உயர்ந்தது)",
            "நீதித்துறை மேலாதிக்கம் (உச்ச நீதிமன்றமே மூலம்)",
            "குடியரசுத் தலைவர் அதிகாரம் (குடியரசுத் தலைவரே சர்வாதிகாரி)"
        ],
        correct_ans="A",
        exp_en="'WE, THE PEOPLE OF INDIA' signifies Popular Sovereignty — that the Constitution derives its authority directly from the people of India.",
        exp_ta="'இந்திய மக்களாகிய நாம்' என்பது மக்களின் இறையாண்மையைக் குறிக்கிறது — அதாவது அரசியலமைப்பு தனது அதிகாரத்தை மக்களிடமிருந்தே நேரடியாகப் பெறுகிறது.",
        wno_dict={
            "A": {"en": "Correct. It embodies Popular Sovereignty.", "ta": "சரி. இது மக்களின் இறையாண்மையை வெளிப்படுத்துகிறது."},
            "B": {"en": "Incorrect. Parliament is created by the Constitution, not the source of authority.", "ta": "தவறு. நாடாளுமன்றம் அரசியலமைப்பால் உருவாக்கப்பட்டது, அதிகார மூலம் அல்ல."},
            "C": {"en": "Incorrect. Judiciary is an organ under Constitution.", "ta": "தவறு. நீதித்துறை அரசியலமைப்பின் ஒரு உறுப்பு."},
            "D": {"en": "Incorrect. President is a constitutional position.", "ta": "தவறு. குடியரசுத் தலைவர் ஓர் அரசியலமைப்புப் பதவி."}
        },
        tip_en="Source of Authority in India = The People (NOT Parliament/President).",
        tip_ta="இந்தியாவில் அதிகாரத்தின் மூலம் = பொதுமக்கள் (நாடாளுமன்றம்/குடியரசுத் தலைவர் அல்ல).",
        rev_en="'We, the People' = Popular Sovereignty.",
        rev_ta="'மக்களாகிய நாம்' = மக்களின் இறையாண்மை.",
        sources=["Preamble Notes Part 1"],
        bloom="Understand", est_sec=30, pyq_sim="High", tags=["We the People", "Popular Sovereignty"]
    ))

    # Q6 - Direct - Ans B
    qs.append(make_q(
        q_id="PRE_E_006", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Easy", question_type="Direct",
        q_en="What is the correct sequential order of words declaring the Nature of the Indian State in the Preamble?",
        q_ta="முகவுரையில் இந்திய அரசின் தன்மையை விவரிக்கும் சொற்களின் சரியான வரிசை எது?",
        opts_en=[
            "Socialist, Secular, Sovereign, Democratic, Republic",
            "Sovereign, Socialist, Secular, Democratic, Republic",
            "Sovereign, Democratic, Republic, Socialist, Secular",
            "Secular, Socialist, Sovereign, Democratic, Republic"
        ],
        opts_ta=[
            "சமதர்ம, மதச்சார்பற்ற, இறையாண்மை, ஜனநாயக, குடியரசு",
            "இறையாண்மை, சமதர்ம, மதச்சார்பற்ற, ஜனநாயக, குடியரசு",
            "இறையாண்மை, ஜனநாயக, குடியரசு, சமதர்ம, மதச்சார்பற்ற",
            "மதச்சார்பற்ற, சமதர்ம, இறையாண்மை, ஜனநாயக, குடியரசு"
        ],
        correct_ans="B",
        exp_en="The correct sequence of Nature of State in the Preamble is: Sovereign, Socialist, Secular, Democratic, Republic (S-S-S-D-R).",
        exp_ta="முகவுரையில் உள்ள அரசின் தன்மையின் சரியான வரிசை: இறையாண்மை, சமதர்ம, மதச்சார்பற்ற, ஜனநாயக, குடியரசு.",
        wno_dict={
            "A": {"en": "Incorrect. Sovereign must come first.", "ta": "தவறு. இறையாண்மை முதன்மையாக வர வேண்டும்."},
            "B": {"en": "Correct. Sovereign -> Socialist -> Secular -> Democratic -> Republic.", "ta": "சரி. இறையாண்மை -> சமதர்ம -> மதச்சார்பற்ற -> ஜனநாயக -> குடியரசு."},
            "C": {"en": "Incorrect. This was the pre-1976 partial order without Socialist and Secular.", "ta": "தவறு. இது 1976க்கு முந்தைய சமதர்ம, மதச்சார்பற்ற இல்லாத வரிசை."},
            "D": {"en": "Incorrect. Secular cannot come first.", "ta": "தவறு. மதச்சார்பற்ற முதன்மையாக வர முடியாது."}
        },
        tip_en="Memory Formula: S-S-S-D-R (Sovereign, Socialist, Secular, Democratic, Republic).",
        tip_ta="நினைவுச் சூத்திரம்: S-S-S-D-R (இறையாண்மை, சமதர்ம, மதச்சார்பற்ற, ஜனநாயக, குடியரசு).",
        rev_en="Nature Order = Sovereign, Socialist, Secular, Democratic, Republic.",
        rev_ta="அரசின் தன்மை வரிசை = இறையாண்மை, சமதர்ம, மதச்சார்பற்ற, ஜனநாயக, குடியரசு.",
        sources=["Preamble Notes Part 1"],
        bloom="Remember", est_sec=30, pyq_sim="Direct PYQ", tags=["Nature of State", "Sequence"]
    ))

    # Q7 - Direct - Ans C
    qs.append(make_q(
        q_id="PRE_E_007", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Easy", question_type="Direct",
        q_en="What is the correct sequential order of the noble Objectives specified in the Preamble?",
        q_ta="முகவுரையில் குறிப்பிடப்பட்டுள்ள உன்னத இலக்குகளின் சரியான வரிசை எது?",
        opts_en=[
            "Liberty, Equality, Fraternity, Justice",
            "Equality, Justice, Liberty, Fraternity",
            "Justice, Liberty, Equality, Fraternity",
            "Fraternity, Liberty, Equality, Justice"
        ],
        opts_ta=[
            "சுதந்திரம், சமத்துவம், சகோதரத்துவம், நீதி",
            "சமத்துவம், நீதி, சுதந்திரம், சகோதரத்துவம்",
            "நீதி, சுதந்திரம், சமத்துவம், சகோதரத்துவம்",
            "சகோதரத்துவம், சுதந்திரம், சமத்துவம், நீதி"
        ],
        correct_ans="C",
        exp_en="The correct sequence of Objectives in the Preamble is: Justice, Liberty, Equality, Fraternity (J-L-E-F).",
        exp_ta="முகவுரையில் உள்ள இலக்குகளின் சரியான வரிசை: நீதி, சுதந்திரம், சமத்துவம், சகோதரத்துவம்.",
        wno_dict={
            "A": {"en": "Incorrect. Justice is first.", "ta": "தவறு. நீதி முதன்மையானது."},
            "B": {"en": "Incorrect. Equality is not first.", "ta": "தவறு. சமத்துவம் முதன்மையானது அல்ல."},
            "C": {"en": "Correct. Justice -> Liberty -> Equality -> Fraternity.", "ta": "சரி. நீதி -> சுதந்திரம் -> சமத்துவம் -> சகோதரத்துவம்."},
            "D": {"en": "Incorrect. Fraternity comes last.", "ta": "தவறு. சகோதரத்துவம் இறுதியில் வருகிறது."}
        },
        tip_en="Memory Formula: J-L-E-F (Justice, Liberty, Equality, Fraternity).",
        tip_ta="நினைவுச் சூத்திரம்: J-L-E-F (நீதி, சுதந்திரம், சமத்துவம், சகோதரத்துவம்).",
        rev_en="Objectives Order = Justice, Liberty, Equality, Fraternity.",
        rev_ta="இலக்குகளின் வரிசை = நீதி, சுதந்திரம், சமத்துவம், சகோதரத்துவம்.",
        sources=["Preamble Notes Part 1"],
        bloom="Remember", est_sec=30, pyq_sim="High", tags=["Objectives", "Sequence"]
    ))

    # Q8 - Term / Meaning - Ans D
    qs.append(make_q(
        q_id="PRE_E_008", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Easy", question_type="Term / Meaning",
        q_en="What does the term 'Sovereign' mean in the context of the Indian Constitution?",
        q_ta="இந்திய அரசியலமைப்பின் சூழலில் 'இறையாண்மை' (Sovereign) என்ற சொல்லின் பொருள் என்ன?",
        opts_en=[
            "India is subject to British Crown authority.",
            "India cannot acquire foreign territories.",
            "India is bound by military orders of the United Nations.",
            "India is an independent state free from external control in internal and external affairs."
        ],
        opts_ta=[
            "இந்தியா பிரிட்டிஷ் முடிசூட்டு அதிகாரத்திற்கு உட்பட்டது.",
            "இந்தியா வெளிநாட்டு நிலப்பரப்புகளைக் கையகப்படுத்த முடியாது.",
            "இந்தியா ஐக்கிய நாடுகளின் இராணுவ உத்தரவுகளுக்கு கட்டுப்பட்டது.",
            "இந்தியா தனது உள்நாட்டு மற்றும் வெளிநாட்டு விவகாரங்களில் வெளிப்புற கட்டுப்பாட்டிலிருந்து சுதந்திரமாக செயல்படும் ஒரு சுதந்திரமான நாடாகும்."
        ],
        correct_ans="D",
        exp_en="'Sovereign' means India is completely independent and free from any external control in both its internal and external administration.",
        exp_ta="'இறையாண்மை' என்பது இந்தியா தனது உள்நாட்டு மற்றும் வெளிநாட்டு நிர்வாகத்தில் எந்தவொரு வெளிப்புற கட்டுப்பாட்டிலிருந்தும் முற்றிலும் சுதந்திரமானது என்பதைக் குறிக்கிறது.",
        wno_dict={
            "A": {"en": "Incorrect. India ceased to be a British dominion on 26 Jan 1950.", "ta": "தவறு. 26 ஜனவரி 1950 இல் பிரிட்டன் டொமினியன் நிலை முடிவுக்கு வந்தது."},
            "B": {"en": "Incorrect. A sovereign state CAN acquire foreign territories.", "ta": "தவறு. இறையாண்மை நாடு வெளிநாட்டு நிலப்பரப்பைக் கையகப்படுத்த முடியும்."},
            "C": {"en": "Incorrect. UN membership does not affect national sovereignty.", "ta": "தவறு. ஐ.நா உறுப்பினர் தகுதி தேசிய இறையாண்மையைப் பாதிக்காது."},
            "D": {"en": "Correct. Free internally and externally.", "ta": "சரி. உள்நாட்டிலும் வெளிநாட்டிலும் சுதந்திரமானது."}
        },
        tip_en="Sovereign = No foreign power above India.",
        tip_ta="இறையாண்மை = இந்தியாவிற்கு மேலே வெளிநாட்டு அதிகாரம் எதுவுமில்லை.",
        rev_en="Sovereign = Free from external control.",
        rev_ta="இறையாண்மை = வெளிப்புற கட்டுப்பாட்டிலிருந்து சுதந்திரமானது.",
        sources=["Preamble Notes Part 1"],
        bloom="Understand", est_sec=30, pyq_sim="High", tags=["Sovereign", "Meaning"]
    ))

    # Q9 - Direct - Ans A
    qs.append(make_q(
        q_id="PRE_E_009", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Easy", question_type="Direct",
        q_en="Which Constitutional Amendment Act added the words 'Socialist', 'Secular', and 'Integrity' to the Preamble?",
        q_ta="எந்த அரசியலமைப்பு திருத்தச் சட்டம் முகவுரையில் 'சமதர்ம', 'மதச்சார்பற்ற' மற்றும் 'ஒருமைப்பாடு' ஆகிய சொற்களைச் சேர்த்தது?",
        opts_en=[
            "42nd Constitutional Amendment Act, 1976",
            "44th Constitutional Amendment Act, 1978",
            "86th Constitutional Amendment Act, 2002",
            "91st Constitutional Amendment Act, 2003"
        ],
        opts_ta=[
            "42வது அரசியலமைப்பு திருத்தச் சட்டம், 1976",
            "44வது அரசியலமைப்பு திருத்தச் சட்டம், 1978",
            "86வது அரசியலமைப்பு திருத்தச் சட்டம், 2002",
            "91வது அரசியலமைப்பு திருத்தச் சட்டம், 2003"
        ],
        correct_ans="A",
        exp_en="The 42nd Constitutional Amendment Act, 1976 inserted three new words in the Preamble: 'Socialist', 'Secular', and 'Integrity'.",
        exp_ta="42வது அரசியலமைப்பு திருத்தச் சட்டம், 1976 முகவுரையில் மூன்று புதிய சொற்களைச் சேர்த்தது: 'சமதர்ம', 'மதச்சார்பற்ற' மற்றும் 'ஒருமைப்பாடு'.",
        wno_dict={
            "A": {"en": "Correct. 42nd Amendment Act 1976 added these 3 words.", "ta": "சரி. 42வது திருத்தச் சட்டம் 1976 இந்த 3 சொற்களைச் சேர்த்தது."},
            "B": {"en": "Incorrect. 44th Amendment modified emergency rules and right to property.", "ta": "தவறு. 44வது திருத்தம் அவசரக்கால விதிகள் மற்றும் சொத்து உரிமையை மாற்றியது."},
            "C": {"en": "Incorrect. 86th Amendment added Right to Education.", "ta": "தவறு. 86வது திருத்தம் கல்வி உரிமையைச் சேர்த்தது."},
            "D": {"en": "Incorrect. 91st Amendment capped Council of Ministers size.", "ta": "தவறு. 91வது திருத்தம் அமைச்சரவை அளவைக் கட்டுப்படுத்தியது."}
        },
        tip_en="Remember the 3 words added in 1976: Socialist, Secular, Integrity.",
        tip_ta="1976 இல் சேர்க்கப்பட்ட 3 சொற்கள்: சமதர்ம, மதச்சார்பற்ற, ஒருமைப்பாடு.",
        rev_en="42nd Amendment 1976 = Socialist, Secular, Integrity added.",
        rev_ta="42வது திருத்தம் 1976 = சமதர்ம, மதச்சார்பற்ற, ஒருமைப்பாடு சேர்க்கப்பட்டன.",
        sources=["Preamble Notes Part 1 & 2"],
        bloom="Remember", est_sec=30, pyq_sim="Direct PYQ", tags=["42nd Amendment", "Socialist", "Secular", "Integrity"]
    ))

    # Q10 - Conceptual - Ans B
    qs.append(make_q(
        q_id="PRE_E_010", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Easy", question_type="Conceptual",
        q_en="What form of Socialism is adopted by the Indian Constitution as reflected in its Preamble and DPSPs?",
        q_ta="இந்திய அரசியலமைப்பின் முகவுரை மற்றும் DPSP இல் பிரதிபலிப்பது போல இந்தியா ஏற்றுக்கொண்ட சமதர்ம வடிவம் எது?",
        opts_en=[
            "Communistic Socialism (State monopoly of all property)",
            "Democratic Socialism (Mixed Economy with public & private sectors)",
            "Marxist-Leninist Command Socialism",
            "Feudal Socialism"
        ],
        opts_ta=[
            "கம்யூனிச சமதர்மம் (அனைத்து சொத்துக்களையும் அரசுமயமாக்கல்)",
            "ஜனநாயக சமதர்மம் (பொது மற்றும் தனியார் துறைகள் கொண்ட கலப்பு பொருளாதாரம்)",
            "மார்க்சிஸ்ட் கட்டளைச் சமதர்மம்",
            "நிலப்பிரபுத்துவ சமதர்மம்"
        ],
        correct_ans="B",
        exp_en="India adopted Democratic Socialism, which aims to end poverty, disease, and inequality through a Mixed Economy where public and private sectors co-exist.",
        exp_ta="இந்தியா ஜனநாயக சமதர்மத்தை ஏற்றுக்கொண்டது, இது பொது மற்றும் தனியார் துறைகள் இணைந்து செயல்படும் கலப்பு பொருளாதாரம் மூலம் வறுமை மற்றும் சமத்துவமின்மையை ஒழிப்பதை நோக்கமாகக் கொண்டுள்ளது.",
        wno_dict={
            "A": {"en": "Incorrect. India rejected complete state monopoly of property.", "ta": "தவறு. இந்தியா அனைத்து சொத்துக்களையும் அரசுமயமாக்குவதை நிராகரித்தது."},
            "B": {"en": "Correct. Democratic Socialism & Mixed Economy.", "ta": "சரி. ஜனநாயக சமதர்மம் & கலப்பு பொருளாதாரம்."},
            "C": {"en": "Incorrect. India did not follow Soviet command model.", "ta": "தவறு. இந்தியா சோவியத் மாதிரியைப் பின்பற்றவில்லை."},
            "D": {"en": "Incorrect. Irrelevant term.", "ta": "தவறு. பொருத்தமற்ற சொல்."}
        },
        tip_en="Indian Socialism = Democratic Socialism = Mixed Economy.",
        tip_ta="இந்திய சமதர்மம் = ஜனநாயக சமதர்மம் = கலப்பு பொருளாதாரம்.",
        rev_en="Socialism in India = Democratic Socialism & Mixed Economy.",
        rev_ta="இந்தியாவில் சமதர்மம் = ஜனநாயக சமதர்மம் & கலப்பு பொருளாதாரம்.",
        sources=["Preamble Notes Part 1"],
        bloom="Understand", est_sec=30, pyq_sim="High", tags=["Socialist", "Democratic Socialism", "Mixed Economy"]
    ))

    # Q11 - Conceptual - Ans C
    qs.append(make_q(
        q_id="PRE_E_011", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Easy", question_type="Conceptual",
        q_en="What does 'Positive Secularism' in the Indian constitutional context mean?",
        q_ta="இந்திய அரசியலமைப்புச் சூழலில் 'நேர்மறை மதச்சார்பின்மை' (Positive Secularism) என்பது எதனைக் குறிக்கிறது?",
        opts_en=[
            "Complete state hostility towards all religious practices.",
            "Establishment of Hinduism as the official state religion.",
            "Equal respect and equal constitutional protection for all religions (Sarva Dharma Sambhava).",
            "Ban on all religious festivals in public places."
        ],
        opts_ta=[
            "அனைத்து மத நடைமுறைகளுக்கும் எதிரான அரசின் கடுமையான எதிர்ப்பு.",
            "இந்து மதத்தை அதிகாரப்பூர்வ அரசு மதமாக நிறுவுதல்.",
            "அனைத்து மதங்களுக்கும் சமமான மரியாதை மற்றும் அரசியலமைப்பு பாதுகாப்பு (சர்வ தர்ம சம்பவ).",
            "பொது இடங்களில் அனைத்து மதப் பண்டிகைகளையும் தடை செய்தல்."
        ],
        correct_ans="C",
        exp_en="Indian secularism is positive, embodying 'Sarva Dharma Sambhava' — all religions in India receive equal respect, protection, and support from the State.",
        exp_ta="இந்திய மதச்சார்பின்மை நேர்மறையானது, அதாவது 'சர்வ தர்ம சம்பவ' — இந்தியாவில் உள்ள அனைத்து மதங்களுக்கும் அரசிடமிருந்து சமமான மரியாதை, பாதுகாப்பு மற்றும் ஆதரவு வழங்கப்படுகிறது.",
        wno_dict={
            "A": {"en": "Incorrect. Western secularism involves strict separation/exclusion, not hostility.", "ta": "தவறு. மேற்கத்திய மதச்சார்பின்மை பிரிவினையைக் குறிக்கிறது."},
            "B": {"en": "Incorrect. India has NO official state religion.", "ta": "தவறு. இந்தியாவிற்கு அதிகாரப்பூர்வ அரசு மதம் எதுவுமில்லை."},
            "C": {"en": "Correct. Equal respect and protection for all religions.", "ta": "சரி. அனைத்து மதங்களுக்கும் சமமான மரியாதை மற்றும் பாதுகாப்பு."},
            "D": {"en": "Incorrect. Religious freedom is protected under Articles 25-28.", "ta": "தவறு. மத சுதந்திரம் உறுப்புகள் 25-28 இன் கீழ் பாதுகாக்கப்படுகிறது."}
        },
        tip_en="Indian Secularism = Positive concept = Equal respect for all religions.",
        tip_ta="இந்திய மதச்சார்பின்மை = நேர்மறைக் கருத்து = அனைத்து மதங்களுக்கும் சம மரியாதை.",
        rev_en="Positive Secularism = Equal respect to all religions (Sarva Dharma Sambhava).",
        rev_ta="நேர்மறை மதச்சார்பின்மை = அனைத்து மதங்களுக்கும் சம மரியாதை.",
        sources=["Preamble Notes Part 1"],
        bloom="Understand", est_sec=30, pyq_sim="High", tags=["Secular", "Positive Secularism"]
    ))

    # Q12 - Direct - Ans D
    qs.append(make_q(
        q_id="PRE_E_012", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Easy", question_type="Direct",
        q_en="Under which Article of the Indian Constitution is Universal Adult Franchise guaranteed?",
        q_ta="இந்திய அரசியலமைப்பின் எந்த உறுப்பின் கீழ் உலகளாவிய வயதுவந்தோர் வாக்குரிமை உத்தரவாதம் அளிக்கப்பட்டுள்ளது?",
        opts_en=["Article 324", "Article 325", "Article 352", "Article 326"],
        opts_ta=["உறுப்பு 324", "உறுப்பு 325", "உறுப்பு 352", "உறுப்பு 326"],
        correct_ans="D",
        exp_en="Article 326 of the Constitution guarantees Universal Adult Franchise for elections to Lok Sabha and State Legislative Assemblies.",
        exp_ta="அரசியலமைப்பின் உறுப்பு 326 மக்களவை மற்றும் மாநில சட்டமன்றத் தேர்தல்களுக்கு உலகளாவிய வயதுவந்தோர் வாக்குரிமையை உத்தரவாதம் செய்கிறது.",
        wno_dict={
            "A": {"en": "Incorrect. Article 324 deals with Election Commission powers.", "ta": "தவறு. உறுப்பு 324 தேர்தல் ஆணைய அதிகாரங்கள் பற்றியது."},
            "B": {"en": "Incorrect. Article 325 deals with non-discrimination in electoral rolls.", "ta": "தவறு. உறுப்பு 325 வாக்காளர் பட்டியலில் பாகுபாடின்மை பற்றியது."},
            "C": {"en": "Incorrect. Article 352 deals with National Emergency.", "ta": "தவறு. உறுப்பு 352 தேசிய அவசரநிலை பற்றியது."},
            "D": {"en": "Correct. Article 326 guarantees Universal Adult Franchise.", "ta": "சரி. உறுப்பு 326 வயதுவந்தோர் வாக்குரிமையை உத்தரவாதம் செய்கிறது."}
        },
        tip_en="Article 326 = Universal Adult Franchise (voting age reduced to 18 by 61st Amendment 1988).",
        tip_ta="உறுப்பு 326 = வயதுவந்தோர் வாக்குரிமை (61வது திருத்தம் 1988 மூலம் வாக்கு வயது 18 ஆகக் குறைக்கப்பட்டது).",
        rev_en="Article 326 = Universal Adult Franchise.",
        rev_ta="உறுப்பு 326 = உலகளாவிய வயதுவந்தோர் வாக்குரிமை.",
        sources=["Preamble Notes Part 1"],
        bloom="Remember", est_sec=30, pyq_sim="Direct PYQ", tags=["Article 326", "Adult Franchise"]
    ))

    # Q13 - TNPSC Trap - Ans A
    qs.append(make_q(
        q_id="PRE_E_013", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Easy", question_type="TNPSC Trap",
        q_en="What is the key defining feature of a 'Republic' that distinguishes it from a 'Constitutional Monarchy'?",
        q_ta="ஒரு 'குடியரசு' (Republic) என்பதை 'அரசியலமைப்பு முடியாட்சி'யிலிருந்து வேறுபடுத்தும் முதன்மை அம்சம் எது?",
        opts_en=[
            "Head of State is ELECTED for a fixed tenure instead of a hereditary monarch.",
            "Presence of an elected Prime Minister.",
            "Existence of a written Constitution.",
            "Conduct of periodic parliamentary elections."
        ],
        opts_ta=[
            "பரம்பரை மன்னருக்குப் பதிலாக நிலையான காலத்திற்கு தேர்ந்தெடுக்கப்பட்ட நாட்டின் தலைவர் இருப்பது.",
            "தேர்ந்தெடுக்கப்பட்ட பிரதமர் இருப்பது.",
            "எழுதப்பட்ட அரசியலமைப்பு இருப்பது.",
            "காலமுறை நாடாளுமன்றத் தேர்தல்கள் நடத்துவது."
        ],
        correct_ans="A",
        exp_en="A Republic specifically means an ELECTED Head of State (President) for a fixed tenure. UK has elections and a PM, but is a Monarchy because its head of state is hereditary.",
        exp_ta="குடியரசு என்பது நிலையான காலத்திற்கு தேர்ந்தெடுக்கப்பட்ட நாட்டின் தலைவரைக் (குடியரசுத் தலைவர்) குறிக்கும். இங்கிலாந்தில் தேர்தல்களும் பிரதமரும் உள்ளனர், ஆனால் நாட்டின் தலைவர் பரம்பரை வழியினர் என்பதால் அது முடியாட்சியாகும்.",
        wno_dict={
            "A": {"en": "Correct. Republic = Elected Head of State (President).", "ta": "சரி. குடியரசு = தேர்ந்தெடுக்கப்பட்ட நாட்டின் தலைவர்."},
            "B": {"en": "Incorrect. UK has an elected PM but is a Monarchy.", "ta": "தவறு. இங்கிலாந்தில் தேர்ந்தெடுக்கப்பட்ட பிரதமர் உள்ளார் ஆனால் அது முடியாட்சி."},
            "C": {"en": "Incorrect. Constitutional monarchies can also have written constitutions.", "ta": "தவறு. அரசியலமைப்பு முடியாட்சிகளிலும் எழுதப்பட்ட அரசியலமைப்பு இருக்கலாம்."},
            "D": {"en": "Incorrect. Elections indicate democracy, not republic specifically.", "ta": "தவறு. தேர்தல்கள் ஜனநாயகத்தைக் குறிக்கும், குடியரசை மட்டுமல்ல."}
        },
        tip_en="TNPSC Trap: Democracy and Republic are NOT synonyms! Republic = Elected Head of State.",
        tip_ta="TNPSC பொறி: ஜனநாயகமும் குடியரசும் இணையான சொற்கள் அல்ல! குடியரசு = தேர்ந்தெடுக்கப்பட்ட நாட்டின் தலைவர்.",
        rev_en="Republic = Elected Head of State (President) vs Hereditary Monarch.",
        rev_ta="குடியரசு = தேர்ந்தெடுக்கப்பட்ட நாட்டின் தலைவர் (குடியரசுத் தலைவர்).",
        sources=["Preamble Notes Part 1"],
        bloom="Understand", est_sec=45, pyq_sim="High", tags=["Republic", "Democracy vs Republic", "TNPSC Trap"]
    ))

    # Q14 - Direct - Ans B
    qs.append(make_q(
        q_id="PRE_E_014", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Easy", question_type="Direct",
        q_en="From which historic event were the ideals of 'Justice — Social, Economic, and Political' in the Preamble borrowed?",
        q_ta="முகவுரையில் உள்ள 'நீதி — சமூக, பொருளாதார மற்றும் அரசியல்' என்ற தத்துவங்கள் எந்த வரலாற்று நிகழ்விலிருந்து பெறப்பட்டன?",
        opts_en=["French Revolution (1789)", "Russian Revolution (1917)", "American War of Independence (1776)", "Glorious Revolution (1688)"],
        opts_ta=["பிரெஞ்சுப் புரட்சி (1789)", "ரஷ்யப் புரட்சி (1917)", "அமெரிக்க சுதந்திரப் போர் (1776)", "மகிமைமிக்க புரட்சி (1688)"],
        correct_ans="B",
        exp_en="The ideals of Justice (Social, Economic, and Political) in the Preamble were derived from the Russian Revolution of 1917.",
        exp_ta="முகவுரையில் உள்ள நீதி (சமூக, பொருளாதார மற்றும் அரசியல்) தத்துவங்கள் 1917 ஆம் ஆண்டின் ரஷ்யப் புரட்சியிலிருந்து பெறப்பட்டவை.",
        wno_dict={
            "A": {"en": "Incorrect. French Revolution inspired Liberty, Equality, and Fraternity.", "ta": "தவறு. பிரெஞ்சுப் புரட்சி சுதந்திரம், சமத்துவம், சகோதரத்துவத்தைத் தந்தது."},
            "B": {"en": "Correct. Russian Revolution (1917) inspired Social, Economic, Political Justice.", "ta": "சரி. ரஷ்யப் புரட்சி (1917) சமூக, பொருளாதார, அரசியல் நீதியைத் தந்தது."},
            "C": {"en": "Incorrect. American Revolution inspired Bill of Rights.", "ta": "தவறு. அமெரிக்கப் புரட்சி உரிமைகள் மசோதாவைத் தந்தது."},
            "D": {"en": "Incorrect. Glorious Revolution inspired Bill of Rights 1689.", "ta": "தவறு. மகிமைமிக்க புரட்சி 1689 உரிமைகள் மசோதாவைத் தந்தது."}
        },
        tip_en="Justice (Social, Economic, Political) = Russian Revolution (1917).",
        tip_ta="நீதி (சமூக, பொருளாதார, அரசியல்) = ரஷ்யப் புரட்சி (1917).",
        rev_en="Justice source = Russian Revolution (1917).",
        rev_ta="நீதியின் மூலம் = ரஷ்யப் புரட்சி (1917).",
        sources=["Preamble Notes Part 1"],
        bloom="Remember", est_sec=30, pyq_sim="High", tags=["Justice", "Russian Revolution", "Sources"]
    ))

    # Q15 - Direct - Ans C
    qs.append(make_q(
        q_id="PRE_E_015", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Easy", question_type="Direct",
        q_en="From which historic Revolution were the ideals of 'Liberty, Equality, and Fraternity' in the Preamble borrowed?",
        q_ta="முகவுரையில் உள்ள 'சுதந்திரம், சமத்துவம் மற்றும் சகோதரத்துவம்' என்ற தத்துவங்கள் எந்த வரலாற்றுப் புரட்சியிலிருந்து பெறப்பட்டன?",
        opts_en=["Russian Revolution (1917)", "Industrial Revolution", "French Revolution (1789-1799)", "Chinese Revolution (1949)"],
        opts_ta=["ரஷ்யப் புரட்சி (1917)", "தொழிற்புரட்சி", "பிரெஞ்சுப் புரட்சி (1789-1799)", "சீனப் புரட்சி (1949)"],
        correct_ans="C",
        exp_en="The ideals of Liberty, Equality, and Fraternity in the Preamble were borrowed from the French Revolution (1789-1799).",
        exp_ta="முகவுரையில் உள்ள சுதந்திரம், சமத்துவம் மற்றும் சகோதரத்துவம் என்ற தத்துவங்கள் பிரெஞ்சுப் புரட்சியிலிருந்து (1789-1799) பெறப்பட்டவை.",
        wno_dict={
            "A": {"en": "Incorrect. Russian Revolution gave Justice ideals.", "ta": "தவறு. ரஷ்யப் புரட்சி நீதி தத்துவங்களைத் தந்தது."},
            "B": {"en": "Incorrect. Industrial Revolution was an economic shift.", "ta": "தவறு. தொழிற்புரட்சி ஒரு பொருளாதார மாற்றம்."},
            "C": {"en": "Correct. French Revolution gave Liberty, Equality, Fraternity.", "ta": "சரி. பிரெஞ்சுப் புரட்சி சுதந்திரம், சமத்துவம், சகோதரத்துவத்தைத் தந்தது."},
            "D": {"en": "Incorrect. Chinese revolution was 1949.", "ta": "தவறு. சீனப் புரட்சி 1949."}
        },
        tip_en="Liberty, Equality, Fraternity = French Revolution (1789-1799).",
        tip_ta="சுதந்திரம், சமத்துவம், சகோதரத்துவம் = பிரெஞ்சுப் புரட்சி (1789-1799).",
        rev_en="Liberty, Equality, Fraternity = French Revolution.",
        rev_ta="சுதந்திரம், சமத்துவம், சகோதரத்துவம் = பிரெஞ்சுப் புரட்சி.",
        sources=["Preamble Notes Part 1"],
        bloom="Remember", est_sec=30, pyq_sim="Direct PYQ", tags=["Liberty Equality Fraternity", "French Revolution"]
    ))

    # Q16 - Term / Meaning - Ans D
    qs.append(make_q(
        q_id="PRE_E_016", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Easy", question_type="Term / Meaning",
        q_en="What does 'Distributive Justice' in constitutional terminology stand for?",
        q_ta="அரசியலமைப்புச் சொல்லாடலில் 'விநியோக நீதி' (Distributive Justice) என்பது எதனைக் குறிக்கிறது?",
        opts_en=[
            "Social Justice only",
            "Economic Justice only",
            "Political Justice + Legal Justice",
            "Social Justice + Economic Justice"
        ],
        opts_ta=[
            "சமூக நீதி மட்டுமே",
            "பொருளாதார நீதி மட்டுமே",
            "அரசியல் நீதி + சட்ட நீதி",
            "சமூக நீதி + பொருளாதார நீதி"
        ],
        correct_ans="D",
        exp_en="Distributive Justice is the combination of Social Justice and Economic Justice aimed at creating an egalitarian welfare society.",
        exp_ta="விநியோக நீதி என்பது சமூக நீதி மற்றும் பொருளாதார நீதியின் சேர்க்கையாகும், இது ஒரு சமத்துவ நலன்புரி சமுதாயத்தை உருவாக்குவதை நோக்கமாகக் கொண்டுள்ளது.",
        wno_dict={
            "A": {"en": "Incorrect. Includes economic justice too.", "ta": "தவறு. பொருளாதார நீதியும் இதில் அடங்கும்."},
            "B": {"en": "Incorrect. Includes social justice too.", "ta": "தவறு. சமூக நீதியும் இதில் அடங்கும்."},
            "C": {"en": "Incorrect. Political justice is distinct.", "ta": "தவறு. அரசியல் நீதி தனியானது."},
            "D": {"en": "Correct. Distributive Justice = Social Justice + Economic Justice.", "ta": "சரி. விநியோக நீதி = சமூக நீதி + பொருளாதார நீதி."}
        },
        tip_en="Distributive Justice = Social Justice + Economic Justice.",
        tip_ta="விநியோக நீதி = சமூக நீதி + பொருளாதார நீதி.",
        rev_en="Distributive Justice = Social Justice + Economic Justice.",
        rev_ta="விநியோக நீதி = சமூக நீதி + பொருளாதார நீதி.",
        sources=["Preamble Notes Part 1"],
        bloom="Understand", est_sec=30, pyq_sim="High", tags=["Distributive Justice", "Social & Economic"]
    ))

    # Q17 - Conceptual - Ans A
    qs.append(make_q(
        q_id="PRE_E_017", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Easy", question_type="Conceptual",
        q_en="Which of the following is TRUE regarding 'Liberty' as expressed in the Preamble of India?",
        q_ta="இந்திய முகவுரையில் வெளிப்படுத்தப்பட்டுள்ள 'சுதந்திரம்' தொடர்பாக பின்வருவனவற்றில் எது சரி?",
        opts_en=[
            "Liberty is NOT absolute; it is qualified and subject to reasonable constitutional restrictions.",
            "Liberty is absolute and allows citizens to act without any legal limitations.",
            "Liberty is enforceable only during National Emergencies.",
            "Liberty applies only to economic transactions."
        ],
        opts_ta=[
            "சுதந்திரம் வரம்பற்றது (absolute) அல்ல; இது தகுதிவாய்ந்தது மற்றும் நியாயமான அரசியலமைப்புக் கட்டுப்பாடுகளுக்கு உட்பட்டது.",
            "சுதந்திரம் வரம்பற்றது மற்றும் குடிமக்கள் எவ்வித சட்ட வரம்புகளுமின்றி செயல்பட அனுமதிக்கிறது.",
            "சுதந்திரம் தேசிய அவசரநிலைகளின் போது மட்டுமே அமல்படுத்தப்படும்.",
            "சுதந்திரம் பொருளாதார பரிவர்த்தனைகளுக்கு மட்டுமே பொருந்தும்."
        ],
        correct_ans="A",
        exp_en="Liberty in the Preamble is NOT absolute; it is qualified and must be enjoyed within the limitations conceived in the Constitution (e.g. Article 19(2)).",
        exp_ta="முகவுரையில் உள்ள சுதந்திரம் வரம்பற்றது அல்ல; இது தகுதிவாய்ந்தது மற்றும் அரசியலமைப்பில் உள்ள வரம்புகளுக்குள் (எ.கா. உறுப்பு 19(2)) அனுபவிக்கப்பட வேண்டும்.",
        wno_dict={
            "A": {"en": "Correct. Liberty is qualified and subject to reasonable restrictions.", "ta": "சரி. சுதந்திரம் தகுதிவாய்ந்தது மற்றும் நியாயமான கட்டுப்பாடுகளுக்கு உட்பட்டது."},
            "B": {"en": "Incorrect. Absolute liberty leads to anarchy.", "ta": "தவறு. வரம்பற்ற சுதந்திரம் அராஜகத்திற்கு வழிவகுக்கும்."},
            "C": {"en": "Incorrect. Fundamental Rights can be restricted during emergency, not created.", "ta": "தவறு. அவசரநிலையின் போது உரிமைகள் கட்டுப்படுத்தப்படலாம்."},
            "D": {"en": "Incorrect. Includes thought, expression, belief, faith, worship.", "ta": "தவறு. சிந்தனை, வெளிப்பாடு, நம்பிக்கை, வழிபாடும் அடங்கும்."}
        },
        tip_en="TNPSC Trap: Preamble Liberty is NOT absolute (it is qualified).",
        tip_ta="TNPSC பொறி: முகவுரை சுதந்திரம் வரம்பற்றது அல்ல (கட்டுப்பாடுகளுக்கு உட்பட்டது).",
        rev_en="Liberty = Qualified (Subject to Reasonable Restrictions).",
        rev_ta="சுதந்திரம் = கட்டுப்பாடுகளுக்கு உட்பட்டது.",
        sources=["Preamble Notes Part 1"],
        bloom="Understand", est_sec=30, pyq_sim="High", tags=["Liberty", "Reasonable Restrictions"]
    ))

    # Q18 - Direct - Ans B
    qs.append(make_q(
        q_id="PRE_E_018", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Easy", question_type="Direct",
        q_en="How many types of Liberty are specified in the Preamble of the Indian Constitution?",
        q_ta="இந்திய அரசியலமைப்பின் முகவுரையில் எத்தனை வகையான சுதந்திரங்கள் குறிப்பிடப்பட்டுள்ளன?",
        opts_en=["3 types", "5 types", "7 types", "2 types"],
        opts_ta=["3 வகைகள்", "5 வகைகள்", "7 வகைகள்", "2 வகைகள்"],
        correct_ans="B",
        exp_en="The Preamble specifies FIVE types of Liberty: Liberty of Thought, Expression, Belief, Faith, and Worship.",
        exp_ta="முகவுரையில் 5 வகையான சுதந்திரங்கள் குறிப்பிடப்பட்டுள்ளன: சிந்தனை, வெளிப்பாடு, நம்பிக்கை, சமயம் மற்றும் வழிபாட்டுச் சுதந்திரம்.",
        wno_dict={
            "A": {"en": "Incorrect. 3 specifies Justice types (Social, Economic, Political).", "ta": "தவறு. 3 என்பது நீதியின் வகைகளைக் குறிக்கும்."},
            "B": {"en": "Correct. 5 types of Liberty (Thought, Expression, Belief, Faith, Worship).", "ta": "சரி. 5 வகையான சுதந்திரம் (சிந்தனை, வெளிப்பாடு, நம்பிக்கை, சமயம், வழிபாடு)."},
            "C": {"en": "Incorrect. 7 was original FR count.", "ta": "தவறு. 7 என்பது அசல் அடிப்படை உரிமைகள் எண்ணிக்கை."},
            "D": {"en": "Incorrect. 2 specifies Equality types (Status & Opportunity).", "ta": "தவறு. 2 என்பது சமத்துவத்தின் வகைகளைக் குறிக்கும்."}
        },
        tip_en="5 Liberties = Thought, Expression, Belief, Faith, Worship.",
        tip_ta="5 சுதந்திரங்கள் = சிந்தனை, வெளிப்பாடு, நம்பிக்கை, சமயம், வழிபாடு.",
        rev_en="5 Liberties in Preamble.",
        rev_ta="முகவுரையில் 5 சுதந்திரங்கள்.",
        sources=["Preamble Notes Part 1"],
        bloom="Remember", est_sec=30, pyq_sim="High", tags=["Liberty Types", "Preamble"]
    ))

    # Q19 - Direct - Ans C
    qs.append(make_q(
        q_id="PRE_E_019", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Easy", question_type="Direct",
        q_en="Which two dimensions of Equality are explicitly mentioned in the Preamble?",
        q_ta="முகவுரையில் வெளிப்படையாகக் குறிப்பிடப்பட்டுள்ள இரண்டு சமத்துவ பரிமாணங்கள் எவை?",
        opts_en=[
            "Equality of Income and Equality of Property",
            "Equality of Religion and Equality of Race",
            "Equality of Status and Equality of Opportunity",
            "Equality of Education and Equality of Employment"
        ],
        opts_ta=[
            "வருமான சமத்துவம் மற்றும் சொத்து சமத்துவம்",
            "மத சமத்துவம் மற்றும் இன சமத்துவம்",
            "தகுதி சமத்துவம் (Status) மற்றும் வாய்ப்பு சமத்துவம் (Opportunity)",
            "கல்வி சமத்துவம் மற்றும் வேலைவாய்ப்பு சமத்துவம்"
        ],
        correct_ans="C",
        exp_en="The Preamble explicitly guarantees TWO dimensions of Equality: 'Equality of status and of opportunity'.",
        exp_ta="முகவுரை இரண்டு சமத்துவ பரிமாணங்களை வெளிப்படையாக உத்தரவாதம் செய்கிறது: 'தகுதி சமத்துவம் மற்றும் வாய்ப்பு சமத்துவம்'.",
        wno_dict={
            "A": {"en": "Incorrect. Economic equality is part of DPSP, not preamble exact words.", "ta": "தவறு. முகவுரைச் சொற்கள் அல்ல."},
            "B": {"en": "Incorrect. Covered under Art 15.", "ta": "தவறு. உறுப்பு 15 இன் கீழ் வருவது."},
            "C": {"en": "Correct. Status and Opportunity.", "ta": "சரி. தகுதி மற்றும் வாய்ப்பு சமத்துவம்."},
            "D": {"en": "Incorrect. Covered under Articles 16 and 21A.", "ta": "தவறு. உறுப்புகள் 16, 21A இன் கீழ் வருவது."}
        },
        tip_en="Equality in Preamble = Equality of Status & Opportunity.",
        tip_ta="முகவுரையில் சமத்துவம் = தகுதி சமத்துவம் & வாய்ப்பு சமத்துவம்.",
        rev_en="2 Equalities = Status & Opportunity.",
        rev_ta="2 சமத்துவங்கள் = தகுதி & வாய்ப்பு.",
        sources=["Preamble Notes Part 1"],
        bloom="Remember", est_sec=30, pyq_sim="High", tags=["Equality", "Status and Opportunity"]
    ))

    # Q20 - Direct - Ans D
    qs.append(make_q(
        q_id="PRE_E_020", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Easy", question_type="Direct",
        q_en="What two key aspects does 'Fraternity' in the Preamble assure to every Indian citizen?",
        q_ta="முகவுரையில் உள்ள 'சகோதரத்துவம்' (Fraternity) ஒவ்வொரு இந்தியக் குடிமகனுக்கும் உறுதி செய்யும் இரண்டு முக்கிய அம்சங்கள் யாவை?",
        opts_en=[
            "Freedom of Speech and Freedom of Religion",
            "Right to Work and Right to Livelihood",
            "Equality of Income and Eradication of Poverty",
            "Dignity of the Individual and Unity & Integrity of the Nation"
        ],
        opts_ta=[
            "பேச்சு சுதந்திரம் மற்றும் மத சுதந்திரம்",
            "வேலை உரிமை மற்றும் வாழ்வாதார உரிமை",
            "வருமான சமத்துவம் மற்றும் வறுமை ஒழிப்பு",
            "தனிமனித கண்ணியம் (Dignity of Individual) மற்றும் தேசத்தின் ஒற்றுமையும் ஒருமைப்பாடும் (Unity & Integrity)"
        ],
        correct_ans="D",
        exp_en="Fraternity in the Preamble assures two things: Dignity of the Individual and Unity and Integrity of the Nation.",
        exp_ta="முகவுரையில் உள்ள சகோதரத்துவம் இரண்டு விஷயங்களை உறுதி செய்கிறது: தனிமனித கண்ணியம் மற்றும் தேசத்தின் ஒற்றுமையும் ஒருமைப்பாடும்.",
        wno_dict={
            "A": {"en": "Incorrect. These are Fundamental Rights under Art 19 & 25.", "ta": "தவறு. இவை உறுப்புகள் 19 & 25 இன் கீழ் உள்ள உரிமைகள்."},
            "B": {"en": "Incorrect. Covered under DPSP Part IV.", "ta": "தவறு. பகுதி IV DPSP இன் கீழ் வருவது."},
            "C": {"en": "Incorrect. Economic goals.", "ta": "தவறு. பொருளாதார இலக்குகள்."},
            "D": {"en": "Correct. Dignity of Individual + Unity & Integrity of Nation.", "ta": "சரி. தனிமனித கண்ணியம் + தேசத்தின் ஒற்றுமையும் ஒருமைப்பாடும்."}
        },
        tip_en="Fraternity assures: 1. Dignity of Individual, 2. Unity & Integrity of Nation.",
        tip_ta="சகோதரத்துவம் உறுதி செய்வது: 1. தனிமனித கண்ணியம், 2. தேசத்தின் ஒற்றுமையும் ஒருமைப்பாடும்.",
        rev_en="Fraternity = Dignity of Individual + Unity & Integrity of Nation.",
        rev_ta="சகோதரத்துவம் = தனிமனித கண்ணியம் + தேசத்தின் ஒருமைப்பாடு.",
        sources=["Preamble Notes Part 1"],
        bloom="Remember", est_sec=30, pyq_sim="High", tags=["Fraternity", "Dignity", "Integrity"]
    ))

    # Q21 - Direct - Ans A
    qs.append(make_q(
        q_id="PRE_E_021", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Easy", question_type="Direct",
        q_en="What was the Supreme Court's ruling regarding the Preamble in the Berubari Union Case (1960)?",
        q_ta="பெருபாரி யூனியன் வழக்கில் (1960) முகவுரை தொடர்பாக உச்ச நீதிமன்றத்தின் தீர்ப்பு என்ன?",
        opts_en=[
            "Preamble is NOT a part of the Constitution.",
            "Preamble is an integral part of the Constitution.",
            "Preamble is an independent source of legislative power.",
            "Preamble cannot be used for constitutional interpretation."
        ],
        opts_ta=[
            "முகவுரை அரசியலமைப்பின் ஒரு பகுதி அல்ல.",
            "முகவுரை அரசியலமைப்பின் ஒரு ஒருங்கிணைந்த பகுதி ஆகும்.",
            "முகவுரை சட்டமன்றத்தின் சுதந்திரமான அதிகார மூலம் ஆகும்.",
            "முகவுரையை அரசியலமைப்பு விளக்கத்திற்கு பயன்படுத்த முடியாது."
        ],
        correct_ans="A",
        exp_en="In the Berubari Union Case (1960), the Supreme Court explicitly held that the Preamble is NOT a part of the Constitution. (This was later overruled in 1973).",
        exp_ta="பெருபாரி யூனியன் வழக்கில் (1960), உச்ச நீதிமன்றம் முகவுரை அரசியலமைப்பின் ஒரு பகுதி அல்ல என்று வெளிப்படையாகத் தீர்ப்பளித்தது. (இது பின்னர் 1973 இல் ரத்து செய்யப்பட்டது).",
        wno_dict={
            "A": {"en": "Correct. Berubari 1960 held Preamble is NOT part of Constitution.", "ta": "சரி. பெருபாரி 1960 முகவுரை அரசியலமைப்பின் பகுதி அல்ல என்றது."},
            "B": {"en": "Incorrect. This was held in Kesavananda Bharati (1973) and LIC (1995).", "ta": "தவறு. இது கேசவாநந்தா (1973) மற்றும் எல்ஐசி (1995) வழக்குகளில் கூறப்பட்டது."},
            "C": {"en": "Incorrect. SC held it is NOT a source of power.", "ta": "தவறு. இது அதிகார மூலம் அல்ல என்று கூறியது."},
            "D": {"en": "Incorrect. SC allowed it as key to framers' mind during ambiguity.", "ta": "தவறு. தெளிவற்ற நிலையில் பயன்படுத்த அனுமதித்தது."}
        },
        tip_en="Berubari Union Case 1960 = Historical view: Preamble is NOT part of Constitution.",
        tip_ta="பெருபாரி யூனியன் வழக்கு 1960 = வரலாற்று நிலை: முகவுரை அரசியலமைப்பின் பகுதி அல்ல.",
        rev_en="Berubari Case 1960 = Preamble NOT part of Constitution.",
        rev_ta="பெருபாரி வழக்கு 1960 = முகவுரை அரசியலமைப்பின் பகுதி அல்ல.",
        sources=["Preamble Notes Part 2"],
        bloom="Remember", est_sec=30, pyq_sim="Direct PYQ", tags=["Berubari Case", "1960", "Constitutional Status"]
    ))

    # Q22 - Direct - Ans B
    qs.append(make_q(
        q_id="PRE_E_022", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Easy", question_type="Direct",
        q_en="Which landmark Supreme Court case overruled the Berubari opinion and held that the Preamble IS a part of the Constitution?",
        q_ta="பெருபாரி அபிப்ராயத்தை ரத்து செய்து முகவுரை அரசியலமைப்பின் ஒரு பகுதி தான் என்று தீர்ப்பளித்த வரலாற்றுச் சிறப்புமிக்க உச்ச நீதிமன்ற வழக்கு எது?",
        opts_en=[
            "Golaknath Case (1967)",
            "Kesavananda Bharati Case (1973)",
            "Minerva Mills Case (1980)",
            "A.K. Gopalan Case (1950)"
        ],
        opts_ta=[
            "கோலக்நாத் வழக்கு (1967)",
            "கேசவாநந்த பாரதி வழக்கு (1973)",
            "மினர்வா மில்ஸ் வழக்கு (1980)",
            "ஏ.கே. கோபாலன் வழக்கு (1950)"
        ],
        correct_ans="B",
        exp_en="In Kesavananda Bharati Case (1973), a 13-judge bench overruled Berubari Case and held that the Preamble IS a part of the Constitution.",
        exp_ta="கேசவாநந்த பாரதி வழக்கில் (1973), 13 நீதிபதிகள் கொண்ட அமர்வு பெருபாரி வழக்கை ரத்து செய்து முகவுரை அரசியலமைப்பின் ஒரு பகுதி தான் என்று தீர்ப்பளித்தது.",
        wno_dict={
            "A": {"en": "Incorrect. Golaknath case restricted fundamental rights amendment.", "ta": "தவறு. கோலக்நாத் வழக்கு அடிப்படை உரிமை திருத்தத்தை வரம்பிற்குட்படுத்தியது."},
            "B": {"en": "Correct. Kesavananda Bharati (1973) held Preamble IS part of Constitution.", "ta": "சரி. கேசவாநந்த பாரதி (1973) முகவுரை அரசியலமைப்பின் ஒரு பகுதி என்றது."},
            "C": {"en": "Incorrect. Minerva Mills reaffirmed basic structure.", "ta": "தவறு. மினர்வா மில்ஸ் அடிப்படை அமைப்பை மீண்டும் உறுதிப்படுத்தியது."},
            "D": {"en": "Incorrect. AK Gopalan was preventive detention case.", "ta": "தவறு. ஏகே கோபாலன் தடுப்புக் காவல் வழக்கு."}
        },
        tip_en="Kesavananda Bharati Case (1973): Preamble IS part of Constitution & Basic Structure Doctrine born.",
        tip_ta="கேசவாநந்த பாரதி வழக்கு (1973): முகவுரை அரசியலமைப்பின் ஒரு பகுதி & அடிப்படை கட்டமைப்பு கோட்பாடு பிறந்தது.",
        rev_en="Kesavananda Bharati 1973 = Preamble IS part of Constitution.",
        rev_ta="கேசவாநந்த பாரதி 1973 = முகவுரை அரசியலமைப்பின் ஒரு பகுதி.",
        sources=["Preamble Notes Part 2"],
        bloom="Remember", est_sec=30, pyq_sim="Direct PYQ", tags=["Kesavananda Bharati", "1973", "Landmark Case"]
    ))

    # Q23 - Direct - Ans C
    qs.append(make_q(
        q_id="PRE_E_023", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Easy", question_type="Direct",
        q_en="How many times has the Preamble of the Indian Constitution been amended so far?",
        q_ta="இந்திய அரசியலமைப்பின் முகவுரை இதுவரை எத்தனை முறை திருத்தப்பட்டுள்ளது?",
        opts_en=["Three times", "Two times", "Only ONCE", "Never amended"],
        opts_ta=["மூன்று முறை", "இரண்டு முறை", "ஒரே ஒரு முறை மட்டுமே", "ஒருபோதும் திருத்தப்படவில்லை"],
        correct_ans="C",
        exp_en="The Preamble has been amended ONLY ONCE in Indian history, by the 42nd Constitutional Amendment Act of 1976.",
        exp_ta="இந்திய வரலாற்றில் முகவுரை ஒரே ஒரு முறை மட்டுமே 1976 இன் 42வது அரசியலமைப்பு திருத்தச் சட்டத்தின் மூலம் திருத்தப்பட்டுள்ளது.",
        wno_dict={
            "A": {"en": "Incorrect. 3 words were added, but amended only once.", "ta": "தவறு. 3 சொற்கள் சேர்க்கப்பட்டன, ஆனால் திருத்தப்பட்டது ஒரு முறை தான்."},
            "B": {"en": "Incorrect. Not twice.", "ta": "தவறு. இரண்டு முறை அல்ல."},
            "C": {"en": "Correct. Amended ONLY ONCE in 1976.", "ta": "சரி. 1976 இல் ஒரே ஒரு முறை மட்டுமே திருத்தப்பட்டது."},
            "D": {"en": "Incorrect. It WAS amended in 1976.", "ta": "தவறு. 1976 இல் திருத்தப்பட்டது."}
        },
        tip_en="TNPSC Trap: Preamble was amended ONLY ONCE (1976) adding 3 words.",
        tip_ta="TNPSC பொறி: முகவுரை ஒரே ஒரு முறை மட்டுமே திருத்தப்பட்டது (1976).",
        rev_en="Preamble amended = ONLY ONCE (42nd Amendment 1976).",
        rev_ta="முகவுரை திருத்தப்பட்டது = ஒரே ஒரு முறை (42வது திருத்தம் 1976).",
        sources=["Preamble Notes Part 2"],
        bloom="Remember", est_sec=30, pyq_sim="Direct PYQ", tags=["Preamble Amendment", "Only Once"]
    ))

    # Q24 - Conceptual - Ans D
    qs.append(make_q(
        q_id="PRE_E_024", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Easy", question_type="Conceptual",
        q_en="Can the Preamble be amended under Article 368 of the Indian Constitution?",
        q_ta="இந்திய அரசியலமைப்பின் உறுப்பு 368 இன் கீழ் முகவுரையைத் திருத்த முடியுமா?",
        opts_en=[
            "No, because Preamble is not a part of the Constitution.",
            "No, Parliament has no power over the Preamble.",
            "Yes, Parliament has unlimited power to delete any part of the Preamble.",
            "Yes, provided the 'Basic Structure' or basic features embodied in it are not destroyed."
        ],
        opts_ta=[
            "இல்லை, ஏனெனில் முகவுரை அரசியலமைப்பின் ஒரு பகுதி அல்ல.",
            "இல்லை, முகவுரை மீது நாடாளுமன்றத்திற்கு அதிகாரம் இல்லை.",
            "ஆம், முகவுரையின் எந்தப் பகுதியையும் நீக்க நாடாளுமன்றத்திற்கு வரம்பற்ற அதிகாரம் உள்ளது.",
            "ஆம், முகவுரையில் உள்ள 'அடிப்படை கட்டமைப்பு' அல்லது அடிப்படை அம்சங்கள் அழிக்கப்படாத வரையில் திருத்தலாம்."
        ],
        correct_ans="D",
        exp_en="Yes, Preamble can be amended under Article 368 because it is part of the Constitution, but subject to the limitation that the Basic Structure cannot be destroyed.",
        exp_ta="ஆம், முகவுரை அரசியலமைப்பின் ஒரு பகுதி என்பதால் உறுப்பு 368 இன் கீழ் திருத்தப்படலாம், ஆனால் அடிப்படை கட்டமைப்பு அழிக்கப்படக்கூடாது என்ற வரம்பிற்கு உட்பட்டது.",
        wno_dict={
            "A": {"en": "Incorrect. Preamble IS part of Constitution since 1973.", "ta": "தவறு. 1973 முதல் முகவுரை அரசியலமைப்பின் பகுதி ஆகும்."},
            "B": {"en": "Incorrect. Parliament has amendment power under Art 368.", "ta": "தவறு. நாடாளுமன்றத்திற்கு உறுப்பு 368 இன் கீழ் திருத்த அதிகாரம் உள்ளது."},
            "C": {"en": "Incorrect. Power is limited by Basic Structure Doctrine.", "ta": "தவறு. அதிகாரம் அடிப்படை கட்டமைப்பு கோட்பாட்டால் கட்டுப்படுத்தப்பட்டது."},
            "D": {"en": "Correct. Can be amended subject to Basic Structure limitation.", "ta": "சரி. அடிப்படை கட்டமைப்பு வரம்பிற்கு உட்பட்டு திருத்தப்படலாம்."}
        },
        tip_en="Article 368 = Amendment Power; Limitation = Basic Structure Doctrine.",
        tip_ta="உறுப்பு 368 = திருத்த அதிகாரம்; வரம்பு = அடிப்படை கட்டமைப்பு கோட்பாடு.",
        rev_en="Preamble Amendable under Art 368 subject to Basic Structure Doctrine.",
        rev_ta="அடிப்படை கட்டமைப்பு வரம்பிற்கு உட்பட்டு உறுப்பு 368 இன் கீழ் முகவுரை திருத்தப்படலாம்.",
        sources=["Preamble Notes Part 2"],
        bloom="Understand", est_sec=30, pyq_sim="High", tags=["Article 368", "Basic Structure", "Amendability"]
    ))

    # Q25 - Direct - Ans A
    qs.append(make_q(
        q_id="PRE_E_025", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Easy", question_type="Direct",
        q_en="Which Supreme Court case reaffirmed in 1995 that 'The Preamble is an integral part of the Constitution'?",
        q_ta="1995 இல் 'முகவுரை என்பது அரசியலமைப்பின் ஒரு ஒருங்கிணைந்த பகுதி' என்று மீண்டும் உறுதிப்படுத்திய உச்ச நீதிமன்ற வழக்கு எது?",
        opts_en=[
            "LIC of India Case (1995)",
            "Minerva Mills Case (1980)",
            "Maneka Gandhi Case (1978)",
            "Shankari Prasad Case (1951)"
        ],
        opts_ta=[
            "எல்ஐசி (LIC of India) வழக்கு (1995)",
            "மினர்வா மில்ஸ் வழக்கு (1980)",
            "மேனகா காந்தி வழக்கு (1978)",
            "சங்கரி பிரசாத் வழக்கு (1951)"
        ],
        correct_ans="A",
        exp_en="In the LIC of India Case (1995), the Supreme Court once again held that the Preamble is an integral part of the Constitution.",
        exp_ta="எல்ஐசி வழக்கில் (1995), உச்ச நீதிமன்றம் மீண்டும் முகவுரை என்பது அரசியலமைப்பின் ஒரு ஒருங்கிணைந்த பகுதி என்று தீர்ப்பளித்தது.",
        wno_dict={
            "A": {"en": "Correct. LIC of India case 1995 reaffirmed Preamble is an integral part.", "ta": "சரி. 1995 எல்ஐசி வழக்கு முகவுரை ஒருங்கிணைந்த பகுதி என்பதை மீண்டும் உறுதிப்படுத்தியது."},
            "B": {"en": "Incorrect. Minerva Mills was 1980.", "ta": "தவறு. மினர்வா மில்ஸ் 1980."},
            "C": {"en": "Incorrect. Maneka Gandhi was 1978.", "ta": "தவறு. மேனகா காந்தி 1978."},
            "D": {"en": "Incorrect. Shankari Prasad was 1951.", "ta": "தவறு. சங்கரி பிரசாத் 1951."}
        },
        tip_en="LIC of India Case 1995 = Reaffirmed Preamble is integral part.",
        tip_ta="எல்ஐசி வழக்கு 1995 = முகவுரை ஒரு ஒருங்கிணைந்த பகுதி என மீண்டும் உறுதி செய்தது.",
        rev_en="LIC Case 1995 = Preamble is integral part of Constitution.",
        rev_ta="எல்ஐசி வழக்கு 1995 = முகவுரை அரசியலமைப்பின் ஒரு பகுதி.",
        sources=["Preamble Notes Part 2"],
        bloom="Remember", est_sec=30, pyq_sim="High", tags=["LIC Case", "1995", "Integral Part"]
    ))

    return qs
