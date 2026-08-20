# preamble_medium_q1_25.py
from scratch_preamble_medium_helper import make_medium_q

def get_medium_q1_25():
    qs = []

    # Q1 - Conceptual Distinction - Ans A
    qs.append(make_medium_q(
        q_id="PRE_M_001", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Medium", question_type="Conceptual Distinction",
        q_en="Which statement correctly distinguishes 'Popular Sovereignty' as expressed in the Preamble from 'Parliamentary Sovereignty' as found in the United Kingdom?",
        q_ta="முகவுரையில் வெளிப்படுத்தப்பட்டுள்ள 'மக்களின் இறையாண்மை' என்பதை ஐக்கிய இராச்சியத்தில் காணப்படும் 'பாராளுமன்ற இறையாண்மை'யிலிருந்து சரியாக வேறுபடுத்தும் கூற்று எது?",
        opts_en=[
            "Under Popular Sovereignty, the people are the ultimate source of constitutional authority, whereas under Parliamentary Sovereignty, Parliament can make or unmake any law without constitutional limits.",
            "Under Popular Sovereignty, Parliament is supreme and above judicial review, whereas under Parliamentary Sovereignty, courts can strike down any parliamentary law.",
            "Popular Sovereignty exists only during presidential elections, whereas Parliamentary Sovereignty is continuous.",
            "Popular Sovereignty applies only to State Legislatures, whereas Parliamentary Sovereignty applies to the Union."
        ],
        opts_ta=[
            "மக்களின் இறையாண்மையில், மக்களே அரசியலமைப்பு அதிகாரத்தின் இறுதி மூலமாவர்; ஆனால் பாராளுமன்ற இறையாண்மையில், அரசியலமைப்பு வரம்புகளின்றி பாராளுமன்றம் எந்தச் சட்டத்தையும் ஆக்கவோ அழிக்கவோ முடியும்.",
            "மக்களின் இறையாண்மையில், பாராளுமன்றமே உயர்ந்தது மற்றும் நீதிப் புனராய்விற்கு அப்பாற்பட்டது; ஆனால் பாராளுமன்ற இறையாண்மையில், நீதிமன்றங்கள் எந்தப் பாராளுமன்றச் சட்டத்தையும் ரத்து செய்ய முடியும்.",
            "மக்களின் இறையாண்மை குடியரசுத் தலைவர் தேர்தலின் போது மட்டுமே நிலவுகிறது; ஆனால் பாராளுமன்ற இறையாண்மை தொடர்ச்சியானது.",
            "மக்களின் இறையாண்மை மாநில சட்டமன்றங்களுக்கு மட்டுமே பொருந்தும்; ஆனால் பாராளுமன்ற இறையாண்மை ஒன்றியத்திற்குப் பொருந்தும்."
        ],
        correct_ans="A",
        exp_en="Popular Sovereignty ('We, the People') means ultimate authority resides in the people who created the Constitution. UK's Parliamentary Sovereignty means Parliament is supreme and unrestrained by a written constitution.",
        exp_ta="மக்களின் இறையாண்மை ('மக்களாகிய நாம்') என்பது அரசியலமைப்பை உருவாக்கிய மக்களிடமே இறுதி அதிகாரம் உள்ளது என்பதாகும். இங்கிலாந்தின் பாராளுமன்ற இறையாண்மை என்பது எழுதப்பட்ட அரசியலமைப்பின் கட்டுப்பாடின்றி பாராளுமன்றமே உயர்ந்தது என்பதாகும்.",
        wno_dict={
            "A": {"en": "Correct. Popular Sovereignty places ultimate power with the people.", "ta": "சரி. மக்களின் இறையாண்மை இறுதி அதிகாரத்தை மக்களிடம் வைக்கிறது."},
            "B": {"en": "Incorrect. Reverses the judicial review concepts.", "ta": "தவறு. நீதிப் புனராய்வுக் கருத்துக்களைத் தலைகீழாக மாற்றுகிறது."},
            "C": {"en": "Incorrect. Popular Sovereignty is a permanent constitutional principle.", "ta": "தவறு. மக்களின் இறையாண்மை நிரந்தரமானது."},
            "D": {"en": "Incorrect. Applies to the entire constitutional system.", "ta": "தவறு. முழு அமைப்பிற்கும் பொருந்தும்."}
        },
        tip_en="India has Constitutional Supremacy derived from Popular Sovereignty (NOT Parliamentary Supremacy).",
        tip_ta="இந்தியாவில் மக்களின் இறையாண்மையிலிருந்து பெறப்பட்ட அரசியலமைப்பு மேலாதிக்கம் உள்ளது (பாராளுமன்ற மேலாதிக்கம் அல்ல).",
        rev_en="Popular Sovereignty = Ultimate authority resides with the People.",
        rev_ta="மக்களின் இறையாண்மை = இறுதி அதிகாரம் மக்களிடம் உள்ளது.",
        sources=["Preamble Notes Part 1"],
        bloom="Understand", est_sec=45, pyq_sim="High", tags=["Popular Sovereignty", "Parliamentary Sovereignty"]
    ))

    # Q2 - Case-law - Ans B
    qs.append(make_medium_q(
        q_id="PRE_M_002", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Medium", question_type="Case-law Based",
        q_en="What was the primary constitutional flaw in the Supreme Court's reasoning in the Berubari Union Case (1960), which was subsequently rectified in the Kesavananda Bharati Case (1973)?",
        q_ta="1960 பெருபாரி யூனியன் வழக்கில் உச்ச நீதிமன்றத்தின் தர்க்கத்தில் இருந்த முதன்மை அரசியலமைப்பு குறைபாடு எது, அது பின்னர் 1973 கேசவாநந்த பாரதி வழக்கில் சரிசெய்யப்பட்டது?",
        opts_en=[
            "The Court failed to recognize that the Preamble was adopted before Article 1 of the Constitution.",
            "The Court overlooked the fact that the Preamble was explicitly voted upon and passed as a part of the Constitution by the Constituent Assembly.",
            "The Court incorrectly held that Article 368 gives unlimited power to cede Indian territory to foreign nations.",
            "The Court treated the Preamble as a justiciable Fundamental Right."
        ],
        opts_ta=[
            "அரசியலமைப்பின் உறுப்பு 1 க்கு முன்பே முகவுரை ஏற்றுக்கொள்ளப்பட்டது என்பதை நீதிமன்றம் அங்கீகரிக்கத் தவறியது.",
            "முகவுரை அரசியலமைப்புச் சபையால் வாக்களிக்கப்பட்டு அரசியலமைப்பின் ஒரு பகுதியாக நிறைவேற்றப்பட்டது என்ற உண்மையை நீதிமன்றம் கவனிக்கத் தவறியது.",
            "உறுப்பு 368 வெளிநாட்டு நாடுகளுக்கு இந்திய நிலப்பரப்பை விட்டுக்கொடுக்க வரம்பற்ற அதிகாரம் அளிக்கிறது என்று நீதிமன்றம் தவறாகக் கூறியது.",
            "நீதிமன்றம் முகவுரையை நிலைநிறுத்தக்கூடிய அடிப்படை உரிமையாக நடத்தியது."
        ],
        correct_ans="B",
        exp_en="In 1973, the SC realized that in Berubari (1960), the Court had overlooked the historical record showing that the Constituent Assembly had explicitly voted: 'The Preamble stands part of the Constitution.'",
        exp_ta="1973 இல், 1960 பெருபாரி வழக்கில் அரசியலமைப்புச் சபை 'முகவுரை அரசியலமைப்பின் ஒரு பகுதியாக அமைகிறது' என்று வெளிப்படையாக வாக்களித்த வரலாற்றுப் பதிவை நீதிமன்றம் கவனிக்கத் தவறியதை உணர்ந்தது.",
        wno_dict={
            "A": {"en": "Incorrect. Preamble was enacted after the rest of the Constitution.", "ta": "தவறு. முகவுரை அரசியலமைப்பின் மற்ற பகுதிகளுக்குப் பின்னரே இயற்றப்பட்டது."},
            "B": {"en": "Correct. Berubari ignored the Assembly voting record where Preamble was passed as part of the Constitution.", "ta": "சரி. பெருபாரி சபை வாக்களிப்பு பதிவைப் புறக்கணித்தது."},
            "C": {"en": "Incorrect. Article 3 requires constitutional amendment for ceding territory.", "ta": "தவறு. நிலப்பரப்பை விட்டுக்கொடுக்க திருத்தம் தேவை."},
            "D": {"en": "Incorrect. Berubari did not treat Preamble as justiciable.", "ta": "தவறு. பெருபாரி முகவுரையை நிலைநிறுத்தக்கூடியதாக நடத்தவில்லை."}
        },
        tip_en="Kesavananda (1973) corrected Berubari by referring to the Constituent Assembly motion passed by Dr. Rajendra Prasad.",
        tip_ta="கேசவாநந்தா (1973) டாக்டர் ராஜேந்திர பிரசாத்தால் நிறைவேற்றப்பட்ட அரசியலமைப்புச் சபை தீர்மானத்தைக் குறிப்பிட்டு பெருபாரியைச் சரிசெய்தது.",
        rev_en="Assembly motion proved Preamble was voted as part of Constitution.",
        rev_ta="சபை தீர்மானம் முகவுரை அரசியலமைப்பின் பகுதியாக வாக்களிக்கப்பட்டதை நிரூபித்தது.",
        sources=["Preamble Notes Part 2"],
        bloom="Understand", est_sec=45, pyq_sim="High", tags=["Berubari Case", "Kesavananda Bharati", "Assembly Voting"]
    ))

    # Q3 - Amendment / Status - Ans C
    qs.append(make_medium_q(
        q_id="PRE_M_003", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Medium", question_type="Amendment / Status",
        q_en="Which statement correctly explains the relationship between Article 368 and the Preamble as settled by the Supreme Court?",
        q_ta="உச்ச நீதிமன்றத்தால் தீர்க்கப்பட்டபடி உறுப்பு 368 மற்றும் முகவுரைக்கு இடையிலான தொடர்பைச் சரியாக விவரிக்கும் கூற்று எது?",
        opts_en=[
            "Preamble cannot be amended under Article 368 because it is not part of the text.",
            "Parliament has absolute power under Article 368 to rewrite or delete any clause of the Preamble.",
            "Preamble can be amended under Article 368, but its basic features embodying the Basic Structure cannot be destroyed.",
            "Preamble can only be amended if three-fourths of the State Assemblies ratify the amendment."
        ],
        opts_ta=[
            "முகவுரை உரைப்பகுதி அல்ல என்பதால் உறுப்பு 368 இன் கீழ் அதைத் திருத்த முடியாது.",
            "உறுப்பு 368 இன் கீழ் முகவுரையின் எந்தப் பகுதியையும் மாற்றி எழுதவோ நீக்கவோ நாடாளுமன்றத்திற்கு பூரண அதிகாரம் உள்ளது.",
            "முகவுரை உறுப்பு 368 இன் கீழ் திருத்தப்படலாம், ஆனால் அதன் அடிப்படை கட்டமைப்பைக் கொண்டுள்ள அடிப்படை அம்சங்களை அழிக்க முடியாது.",
            "மூன்றில் மூன்று பங்கு மாநில சட்டமன்றங்கள் ஒப்புதல் அளித்தால் மட்டுமே முகவுரையைத் திருத்த முடியும்."
        ],
        correct_ans="C",
        exp_en="Parliament can amend the Preamble under Article 368 because it is part of the Constitution (Kesavananda 1973), but the amendment power is limited by the Basic Structure Doctrine.",
        exp_ta="முகவுரை அரசியலமைப்பின் ஒரு பகுதி என்பதால் நாடாளுமன்றம் உறுப்பு 368 இன் கீழ் முகவுரையைத் திருத்தலாம் (கேசவாநந்தா 1973), ஆனால் திருத்த அதிகாரம் அடிப்படை கட்டமைப்பு கோட்பாட்டால் வரம்பிற்குட்பட்டது.",
        wno_dict={
            "A": {"en": "Incorrect. Preamble IS part of Constitution.", "ta": "தவறு. முகவுரை அரசியலமைப்பின் பகுதி."},
            "B": {"en": "Incorrect. Power is not absolute; bounded by Basic Structure.", "ta": "தவறு. அதிகாரம் பூரணமானது அல்ல; அடிப்படை அமைப்பால் வரம்பிற்குட்பட்டது."},
            "C": {"en": "Correct. Preamble is amendable subject to Basic Structure restriction.", "ta": "சரி. அடிப்படை கட்டமைப்பு வரம்பிற்கு உட்பட்டு முகவுரை திருத்தப்படலாம்."},
            "D": {"en": "Incorrect. State ratification is not required unless affecting federal structure.", "ta": "தவறு. மாநில ஒப்புதல் தேவையில்லை."}
        },
        tip_en="Article 368 applies to Preamble, but cannot alter its Basic Structure core.",
        tip_ta="உறுப்பு 368 முகவுரைக்கு பொருந்தும், ஆனால் அதன் அடிப்படை அமைப்பை மாற்ற முடியாது.",
        rev_en="Preamble amendable under Art 368 subject to Basic Structure doctrine.",
        rev_ta="அடிப்படை கட்டமைப்புக்கு உட்பட்டு உறுப்பு 368 இன் கீழ் முகவுரை திருத்தப்படலாம்.",
        sources=["Preamble Notes Part 2"],
        bloom="Understand", est_sec=45, pyq_sim="High", tags=["Article 368", "Amendability", "Basic Structure"]
    ))

    # Q4 - Constitutional Relationship - Ans D
    qs.append(make_medium_q(
        q_id="PRE_M_004", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Medium", question_type="Constitutional Relationship",
        q_en="How does the objective of 'Justice — Social, Economic, and Political' in the Preamble find practical implementation across Parts III and IV of the Constitution?",
        q_ta="முகவுரையில் உள்ள 'நீதி — சமூக, பொருளாதார மற்றும் அரசியல்' என்ற இலக்கு அரசியலமைப்பின் பகுதி III மற்றும் IV இல் எவ்வாறு நடைமுறைப்படுத்தப்படுகிறது?",
        opts_en=[
            "Social Justice is implemented exclusively through Article 32 writs.",
            "Economic Justice is guaranteed as an enforceable Fundamental Right under Article 19.",
            "Political Justice is restricted to Cabinet Ministers under Article 74.",
            "Social Justice is protected via Fundamental Rights (Arts 14-18) while Social & Economic Justice goals are directed to the State through DPSPs (Arts 38 & 39)."
        ],
        opts_ta=[
            "சமூக நீதி உறுப்பு 32 பேராணைகள் மூலம் மட்டுமே அமல்படுத்தப்படுகிறது.",
            "பொருளாதார நீதி உறுப்பு 19 இன் கீழ் நிலைநிறுத்தக்கூடிய அடிப்படை உரிமையாக உத்தரவாதம் அளிக்கப்பட்டுள்ளது.",
            "அரசியல் நீதி உறுப்பு 74 இன் கீழ் அமைச்சரவை அமைச்சர்களுக்கு மட்டுமே கட்டுப்படுத்தப்பட்டுள்ளது.",
            "சமூக நீதி அடிப்படை உரிமைகள் (உறுப்புகள் 14-18) மூலம் பாதுகாக்கப்படுகிறது, அதே வேளையில் சமூக & பொருளாதார நீதி இலக்குகள் DPSP (உறுப்புகள் 38 & 39) மூலம் அரசிற்கு வழிகாட்டப்படுகின்றன."
        ],
        correct_ans="D",
        exp_en="Social Justice is operationalized via Part III (prohibition of discrimination, abolition of untouchability, titles) and combined socio-economic justice (Distributive Justice) is mandated via Part IV DPSPs (Arts 38, 39).",
        exp_ta="சமூக நீதி பகுதி III (பாகுபாடின்மை, தீண்டாமை ஒழிப்பு) மூலம் நடைமுறைப்படுத்தப்படுகிறது மற்றும் ஒருங்கிணைந்த சமூக-பொருளாதார நீதி (விநியோக நீதி) பகுதி IV DPSP (உறுப்புகள் 38, 39) மூலம் அரசிற்கு ஆணையிடப்படுகிறது.",
        wno_dict={
            "A": {"en": "Incorrect. Part IV DPSP also implements social justice.", "ta": "தவறு. பகுதி IV DPSP உம் சமூக நீதியை அமல்படுத்துகிறது."},
            "B": {"en": "Incorrect. Economic justice is primarily in DPSP (non-justiciable).", "ta": "தவறு. பொருளாதார நீதி முதன்மையாக DPSP இல் உள்ளது."},
            "C": {"en": "Incorrect. Political justice applies to all adult citizens.", "ta": "தவறு. அரசியல் நீதி அனைத்து வயதுவந்த குடிமக்களுக்கும் பொருந்தும்."},
            "D": {"en": "Correct. FRs provide immediate protection while DPSPs mandate socio-economic welfare policy.", "ta": "சரி. அடிப்படை உரிமைகள் உடனடி பாதுகாப்பு தருகின்றன, DPSP கொள்கை வழிகாட்டுகிறது."}
        },
        tip_en="Distributive Justice = Social Justice (Part III & IV) + Economic Justice (Part IV DPSP).",
        tip_ta="விநியோக நீதி = சமூக நீதி (பகுதி III & IV) + பொருளாதார நீதி (பகுதி IV DPSP).",
        rev_en="Justice implemented via Part III (FRs) & Part IV (DPSPs).",
        rev_ta="நீதி பகுதி III (FR) & பகுதி IV (DPSP) மூலம் அமல்படுத்தப்படுகிறது.",
        sources=["Preamble Notes Part 1 & 2"],
        bloom="Analyze", est_sec=45, pyq_sim="High", tags=["Justice", "Part III", "Part IV DPSP"]
    ))

    # Q5 - Conceptual Distinction - Ans A
    qs.append(make_medium_q(
        q_id="PRE_M_005", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Medium", question_type="Conceptual Distinction",
        q_en="Which statement accurately reflects the constitutional distinction between 'Democracy' and 'Republic' as embodied in the Indian polity?",
        q_ta="இந்திய அரசமைப்பில் பொதிந்துள்ள 'ஜனநாயகம்' மற்றும் 'குடியரசு' ஆகியவற்றிற்கு இடையிலான அரசியலமைப்பு வேறுபாட்டைச் சரியாக வெளிப்படுத்தும் கூற்று எது?",
        opts_en=[
            "Democracy signifies rule by the elected representatives of the people, whereas Republic signifies that the Head of State (President) is elected for a fixed term rather than holding office hereditarily.",
            "Democracy applies only to Parliament, whereas Republic applies only to State Legislatures.",
            "Democracy means complete absence of laws, whereas Republic means strict rule of law.",
            "Democracy guarantees economic equality, whereas Republic guarantees political rights only."
        ],
        opts_ta=[
            "ஜனநாயகம் என்பது மக்களால் தேர்ந்தெடுக்கப்பட்ட பிரதிநிதிகளின் ஆட்சியைக் குறிக்கிறது; ஆனால் குடியரசு என்பது நாட்டின் தலைவர் (குடியரசுத் தலைவர்) பரம்பரையாகப் பதவியில் இருப்பதற்குப் பதிலாக நிலையான காலத்திற்குத் தேர்ந்தெடுக்கப்படுவதைக் குறிக்கிறது.",
            "ஜனநாயகம் பாராளுமன்றத்திற்கு மட்டுமே பொருந்தும்; ஆனால் குடியரசு மாநில சட்டமன்றங்களுக்கு மட்டுமே பொருந்தும்.",
            "ஜனநாயகம் என்பது சட்டங்கள் முற்றிலும் இல்லாத நிலை; ஆனால் குடியரசு என்பது கடுமையான சட்டத்தின் ஆட்சியைக் குறிக்கிறது.",
            "ஜனநாயகம் பொருளாதார சமத்துவத்தை உத்தரவாதம் செய்கிறது; ஆனால் குடியரசு அரசியல் உரிமைகளை மட்டுமே உத்தரவாதம் செய்கிறது."
        ],
        correct_ans="A",
        exp_en="Democracy denotes supreme power vested in people exercised directly or indirectly through representatives. Republic specifically means an elected Head of State (President) with no hereditary monarch.",
        exp_ta="ஜனநாயகம் என்பது மக்களிடம் உள்ள உச்ச அதிகாரம் பிரதிநிதிகள் மூலம் பயன்படுத்தப்படுவதைக் குறிக்கிறது. குடியரசு என்பது பரம்பரை மன்னரின்றி தேர்ந்தெடுக்கப்பட்ட நாட்டின் தலைவரைக் குறிக்கிறது.",
        wno_dict={
            "A": {"en": "Correct. Democracy = Representative rule; Republic = Elected Head of State.", "ta": "சரி. ஜனநாயகம் = பிரதிநிதி ஆட்சி; குடியரசு = தேர்ந்தெடுக்கப்பட்ட நாட்டின் தலைவர்."},
            "B": {"en": "Incorrect. Both apply to the entire Union of India.", "ta": "தவறு. இரண்டும் முழு இந்திய ஒன்றியத்திற்கும் பொருந்தும்."},
            "C": {"en": "Incorrect. Democracy functions under Rule of Law.", "ta": "தவறு. ஜனநாயகம் சட்டத்தின் ஆட்சியின் கீழ் செயல்படுகிறது."},
            "D": {"en": "Incorrect. Incorrect characterization.", "ta": "தவறு. தவறான சித்தரிப்பு."}
        },
        tip_en="UK is Democratic but NOT a Republic (it is a Monarchy). India is BOTH Democratic and Republic.",
        tip_ta="இங்கிலாந்து ஜனநாயக நாடாகும் ஆனால் குடியரசு அல்ல (முடியாட்சி). இந்தியா ஜனநாயகம் மற்றும் குடியரசு இரண்டும் ஆகும்.",
        rev_en="Democracy = Representative rule; Republic = Elected Head of State.",
        rev_ta="ஜனநாயகம் = பிரதிநிதி ஆட்சி; குடியரசு = தேர்ந்தெடுக்கப்பட்ட நாட்டின் தலைவர்.",
        sources=["Preamble Notes Part 1"],
        bloom="Understand", est_sec=45, pyq_sim="High", tags=["Democracy vs Republic", "Constitutional Distinction"]
    ))

    # Q6 - Application / Inference - Ans B
    qs.append(make_medium_q(
        q_id="PRE_M_006", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Medium", question_type="Application / Inference",
        q_en="Suppose a law enacted by Parliament is worded in ambiguous language capable of two different interpretations. How does the Supreme Court apply the Preamble in such a scenario?",
        q_ta="நாடாளுமன்றத்தால் இயற்றப்பட்ட ஒரு சட்டம் இரண்டு வெவ்வேறு விளக்கங்களுக்கு இடமளிக்கும் தெளிவற்ற மொழியில் உள்ளதாகக் கொள்வோம். இத்தகைய சூழலில் உச்ச நீதிமன்றம் முகவுரையை எவ்வாறு பயன்படுத்துகிறது?",
        opts_en=[
            "The Court automatically strikes down the ambiguous law as unconstitutional without reading further.",
            "The Court adopts the interpretation that aligns with the noble goals and philosophy expressed in the Preamble.",
            "The Court substitutes the law with the exact wording of the Preamble.",
            "The Court refers the law to the British Privy Council for final clarification."
        ],
        opts_ta=[
            "நீதிமன்றம் மேலும் படிக்காமல் தெளிவற்ற சட்டத்தை அரசியலமைப்பிற்கு முரணானது என தானாகவே ரத்து செய்கிறது.",
            "முகவுரையில் வெளிப்படுத்தப்பட்டுள்ள உன்னதமான இலக்குகள் மற்றும் தத்துவத்துடன் ஒத்துப்போகும் விளக்கத்தை நீதிமன்றம் ஏற்றுக்கொள்கிறது.",
            "நீதிமன்றம் சட்டத்தை முகவுரையின் துல்லியமான சொற்களால் மாற்றீடு செய்கிறது.",
            "இறுதித் தெளிவுபடுத்துதலுக்காக நீதிமன்றம் சட்டத்தை பிரிட்டிஷ் பிரிவி கவுன்சிலுக்கு அனுப்புகிறது."
        ],
        correct_ans="B",
        exp_en="The Supreme Court uses the Preamble as an 'Interpretive Guide'. When statutory or constitutional text is ambiguous, courts adopt the construction that furthers Preamble objectives.",
        exp_ta="உச்ச நீதிமன்றம் முகவுரையை ஒரு 'விளக்கமளிக்கும் வழிகாட்டி'யாகப் பயன்படுத்துகிறது. சட்ட அல்லது அரசியலமைப்பு உரை தெளிவற்றதாக இருக்கும் போது, முகவுரை இலக்குகளை ஊக்குவிக்கும் விளக்கத்தை நீதிமன்றங்கள் ஏற்கின்றன.",
        wno_dict={
            "A": {"en": "Incorrect. Courts try to preserve constitutionality by interpretation.", "ta": "தவறு. நீதிமன்றங்கள் விளக்கமளித்து சட்டத்தைக் காப்பாற்ற முயல்கின்றன."},
            "B": {"en": "Correct. Preamble is used to resolve textual ambiguity in favor of constitutional vision.", "ta": "சரி. உரை தெளிவற்ற நிலையைத் தீர்க்க முகவுரை பயன்படுத்தப்படுகிறது."},
            "C": {"en": "Incorrect. Judiciary cannot rewrite statutes.", "ta": "தவறு. நீதித்துறை சட்டங்களை மாற்றியமைக்க முடியாது."},
            "D": {"en": "Incorrect. Privy Council appeals were abolished in 1949.", "ta": "தவறு. பிரிவி கவுன்சில் மேல்முறையீடுகள் 1949 இல் ஒழிக்கப்பட்டன."}
        },
        tip_en="Preamble is an Interpretive Aid used during textual ambiguity.",
        tip_ta="உரை தெளிவற்றதாக இருக்கும் போது முகவுரை விளக்கமளிக்கும் உதவியாகப் பயன்படுகிறது.",
        rev_en="Interpretive Aid = Resolves ambiguity in alignment with Preamble vision.",
        rev_ta="விளக்கமளிக்கும் உதவி = முகவுரை தொலைநோக்கிற்கு ஏற்ப தெளிவற்ற நிலையைத் தீர்க்கிறது.",
        sources=["Preamble Notes Part 2"],
        bloom="Apply", est_sec=45, pyq_sim="High", tags=["Interpretive Guide", "Ambiguity", "Judicial Application"]
    ))

    # Q7 - Case-law - Ans C
    qs.append(make_medium_q(
        q_id="PRE_M_007", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Medium", question_type="Case-law Based",
        q_en="What was the constitutional significance of the S.R. Bommai Case (1994) regarding the Preamble's concept of 'Secularism'?",
        q_ta="முகவுரையின் 'மதச்சார்பின்மை' தத்துவம் குறித்து எஸ்.ஆர். பொம்மை வழக்கில் (1994) வெளிவந்த அரசியலமைப்பு முக்கியத்துவம் என்ன?",
        opts_en=[
            "The Court ruled that Secularism is non-essential and can be removed by simple majority.",
            "The Court ruled that State governments can establish official state religions.",
            "The Court held that Secularism is part of the Basic Structure, upholding President's Rule (Art 356) against state governments engaging in unsecular policies.",
            "The Court held that Secularism applies only to central government institutions."
        ],
        opts_ta=[
            "மதச்சார்பின்மை அவசியமற்றது மற்றும் சாதாரண பெரும்பான்மையால் நீக்கப்படலாம் என நீதிமன்றம் தீர்ப்பளித்தது.",
            "மாநில அரசுகள் அதிகாரப்பூர்வ மாநில மதங்களை நிறுவலாம் என நீதிமன்றம் தீர்ப்பளித்தது.",
            "மதச்சார்பின்மை அடிப்படை அமைப்பின் ஒரு பகுதி என நீதிமன்றம் தீர்ப்பளித்தது, மதச்சார்பற்ற கொள்கைகளில் ஈடுபடும் மாநில அரசுகளுக்கு எதிராக குடியரசுத் தலைவர் ஆட்சியை (உறுப்பு 356) உறுதி செய்தது.",
            "மதச்சார்பின்மை மத்திய அரசு நிறுவனங்களுக்கு மட்டுமே பொருந்தும் என நீதிமன்றம் கூறியது."
        ],
        correct_ans="C",
        exp_en="In S.R. Bommai (1994), SC declared Secularism as a Basic Structure feature of the Constitution, establishing that anti-secular policies by a state government warrant dismissal under Article 356.",
        exp_ta="எஸ்.ஆர். பொம்மை (1994) வழக்கில், உச்ச நீதிமன்றம் மதச்சார்பின்மையை அரசியலமைப்பின் அடிப்படை அமைப்பாக அறிவித்தது, மாநில அரசின் மதச்சார்பற்ற கொள்கைகள் உறுப்பு 356 இன் கீழ் பணிநீக்கம் செய்ய வழிவகுக்கும் என நிறுவியது.",
        wno_dict={
            "A": {"en": "Incorrect. Secularism is part of untouchable Basic Structure.", "ta": "தவறு. மதச்சார்பின்மை அடிப்படை அமைப்பின் ஒரு பகுதி."},
            "B": {"en": "Incorrect. India prohibits state religions.", "ta": "தவறு. இந்தியா அரசு மதங்களைத் தடை செய்கிறது."},
            "C": {"en": "Correct. Secularism is Basic Structure; Art 356 upheld for unsecular acts.", "ta": "சரி. மதச்சார்பின்மை அடிப்படை அமைப்பு; உறுப்பு 356 உறுதி செய்யப்பட்டது."},
            "D": {"en": "Incorrect. Secularism binds both Centre and States.", "ta": "தவறு. மதச்சார்பின்மை மத்திய, மாநில இரு அரசுகளையும் கட்டுப்படுத்தும்."}
        },
        tip_en="SR Bommai (1994) = Secularism & Federalism are Basic Structure.",
        tip_ta="எஸ்.ஆர். பொம்மை (1994) = மதச்சார்பின்மை & கூட்டாட்சி ஆகியவை அடிப்படை அமைப்பாகும்.",
        rev_en="S.R. Bommai 1994 = Secularism is Basic Structure.",
        rev_ta="எஸ்.ஆர். பொம்மை 1994 = மதச்சார்பின்மை அடிப்படை அமைப்பாகும்.",
        sources=["Preamble Notes Part 1 & 2"],
        bloom="Understand", est_sec=45, pyq_sim="High", tags=["SR Bommai Case", "Secularism", "Article 356"]
    ))

    # Q8 - Amendment / Status - Ans D
    qs.append(make_medium_q(
        q_id="PRE_M_008", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Medium", question_type="Amendment / Status",
        q_en="What was the exact textual transformation made to the Fraternity section of the Preamble by the 42nd Constitutional Amendment Act of 1976?",
        q_ta="1976 இன் 42வது அரசியலமைப்பு திருத்தச் சட்டத்தின் மூலம் முகவுரையின் சகோதரத்துவப் பகுதியில் செய்யப்பட்ட துல்லியமான உரை மாற்றம் எது?",
        opts_en=[
            "Changed 'fraternity among citizens' to 'fraternity among all nations'.",
            "Changed 'dignity of the individual' to 'supremacy of the state'.",
            "Changed 'unity of the individual' to 'sovereignty of the people'.",
            "Changed 'unity of the Nation' to 'unity and integrity of the Nation'."
        ],
        opts_ta=[
            "'குடிமக்களிடையே சகோதரத்துவம்' என்பதை 'அனைத்து நாடுகளிடையேயான சகோதரத்துவம்' என மாற்றியது.",
            "'தனிமனித கண்ணியம்' என்பதை 'அரசின் மேலாதிக்கம்' என மாற்றியது.",
            "'தனிமனித ஒற்றுமை' என்பதை 'மக்களின் இறையாண்மை' என மாற்றியது.",
            "'தேசத்தின் ஒற்றுமை' (unity of the Nation) என்பதை 'தேசத்தின் ஒற்றுமையும் ஒருமைப்பாடும்' (unity and integrity of the Nation) என மாற்றியது."
        ],
        correct_ans="D",
        exp_en="The 42nd Amendment Act 1976 inserted the word 'integrity' into the Preamble, transforming 'unity of the Nation' into 'unity and integrity of the Nation'.",
        exp_ta="42வது திருத்தச் சட்டம் 1976 முகவுரையில் 'ஒருமைப்பாடு' என்ற சொல்லைச் சேர்த்து, 'தேசத்தின் ஒற்றுமை' என்பதை 'தேசத்தின் ஒற்றுமையும் ஒருமைப்பாடும்' என மாற்றியது.",
        wno_dict={
            "A": {"en": "Incorrect. Irrelevant phrase.", "ta": "தவறு. தொடர்பற்ற தொடர்."},
            "B": {"en": "Incorrect. Dignity of individual remains intact.", "ta": "தவறு. தனிமனித கண்ணியம் அப்படியே உள்ளது."},
            "C": {"en": "Incorrect. Incorrect wording.", "ta": "தவறு. தவறான சொற்றொடர்."},
            "D": {"en": "Correct. Replaced 'unity of the Nation' with 'unity and integrity of the Nation'.", "ta": "சரி. 'தேசத்தின் ஒற்றுமை' என்பதை 'தேசத்தின் ஒற்றுமையும் ஒருமைப்பாடும்' என மாற்றியது."}
        },
        tip_en="TNPSC Trap: Word 'Integrity' was added to Fraternity section, NOT Nature section.",
        tip_ta="TNPSC பொறி: 'ஒருமைப்பாடு' என்ற சொல் சகோதரத்துவப் பகுதியில் சேர்க்கப்பட்டது, அரசின் தன்மையில் அல்ல.",
        rev_en="42nd Amend 1976 = Added 'Integrity' to 'Unity and Integrity of Nation'.",
        rev_ta="42வது திருத்தம் 1976 = 'தேசத்தின் ஒற்றுமையும் ஒருமைப்பாடும்' என ஒருமைப்பாட்டைச் சேர்த்தது.",
        sources=["Preamble Notes Part 1 & 2"],
        bloom="Remember", est_sec=45, pyq_sim="High", tags=["42nd Amendment", "Integrity", "Fraternity"]
    ))

    # Q9 - TNPSC Trap - Ans A
    qs.append(make_medium_q(
        q_id="PRE_M_009", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Medium", question_type="TNPSC Trap",
        q_en="Which of the following is a COMMON MISCONCEPTION regarding the non-justiciable character of the Preamble?",
        q_ta="முகவுரையின் நீதிமன்றத்தால் நிலைநிறுத்த முடியாத (non-justiciable) தன்மை தொடர்பான பின்வரும் தவறான எண்ணங்களில் எது பொதுவானது?",
        opts_en=[
            "Believing that because the Preamble is non-justiciable, it has zero legal or interpretive significance in constitutional adjudication.",
            "Understanding that citizens cannot file a writ petition solely for enforcement of the Preamble.",
            "Recognizing that Preamble is not an independent source of legislative power.",
            "Acknowledging that clear constitutional provisions prevail over Preamble during direct conflict."
        ],
        opts_ta=[
            "முகவுரை நீதிமன்றத்தால் நிலைநிறுத்த முடியாதது என்பதால், அரசியலமைப்புத் தீர்ப்புகளில் அதற்கு பூஜ்ஜிய சட்ட அல்லது விளக்கமளிக்கும் முக்கியத்துவம் மட்டுமே உள்ளது என நம்புவது.",
            "முகவுரையை மட்டும் அமல்படுத்துவதற்காகக் குடிமக்கள் நேரடியாகப் பேராணை மனு தாக்கல் செய்ய முடியாது என்பதைப் புரிந்துகொள்வது.",
            "முகவுரை சட்டமன்ற அதிகாரத்திற்கான ஒரு சுதந்திரமான மூலம் அல்ல என்பதை அங்கீகரிப்பது.",
            "நேரடி மோதலின் போது தெளிவான அரசியலமைப்பு விதிகள் முகவுரையை மேலெழும் என்பதை ஏற்றுக்கொள்வது."
        ],
        correct_ans="A",
        exp_en="It is a misconception that non-justiciability renders Preamble useless. While non-enforceable directly, Preamble holds tremendous interpretive value as a guide to constitutional vision and Basic Structure.",
        exp_ta="நிலைநிறுத்த முடியாது என்பதால் முகவுரை பயனற்றது என நினைப்பது தவறான எண்ணமாகும். நேரடியாக அமல்படுத்த முடியாது என்றாலும், அரசியலமைப்புத் தொலைநோக்கு மற்றும் அடிப்படை அமைப்பிற்கு முகவுரை மிகுந்த விளக்கமளிக்கும் மதிப்புடையது.",
        wno_dict={
            "A": {"en": "Correct. Believing Preamble has zero legal value is a misconception.", "ta": "சரி. முகவுரைக்கு சட்ட மதிப்பு இல்லை என நம்புவது தவறான கருத்து."},
            "B": {"en": "Incorrect. This is a true legal fact, not a misconception.", "ta": "தவறு. இது உண்மையான சட்ட உண்மை."},
            "C": {"en": "Incorrect. True legal principle established in Berubari and Kesavananda.", "ta": "தவறு. நிறுவப்பட்ட உண்மை சட்டக் கோட்பாடு."},
            "D": {"en": "Incorrect. Operative provisions prevail when clear.", "ta": "தவறு. தெளிவான விதிகள் வெல்லும் என்பது உண்மை."}
        },
        tip_en="Non-justiciable DOES NOT mean legally useless. It acts as an Interpretive Compass.",
        tip_ta="நிலைநிறுத்த முடியாதது என்றால் பயனற்றது என்று அர்த்தமல்ல. இது ஒரு விளக்கமளிக்கும் திசைகாட்டியாக செயல்படுகிறது.",
        rev_en="Preamble is non-justiciable BUT holds immense interpretive value.",
        rev_ta="முகவுரை நிலைநிறுத்த முடியாதது ஆனால் மிகுந்த விளக்கமளிக்கும் மதிப்புடையது.",
        sources=["Preamble Notes Part 2"],
        bloom="Analyze", est_sec=45, pyq_sim="High", tags=["Non-Justiciable", "Interpretive Compass", "TNPSC Trap"]
    ))

    # Q10 - Constitutional Relationship - Ans B
    qs.append(make_medium_q(
        q_id="PRE_M_010", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Medium", question_type="Constitutional Relationship",
        q_en="In what manner does Part IVA (Article 51A - Fundamental Duties) reinforce the Preamble's goal of 'Fraternity'?",
        q_ta="பகுதி IVA (உறுப்பு 51A - அடிப்படை கடமைகள்) முகவுரையின் 'சகோதரத்துவம்' என்ற இலக்கை எவ்வாறு வலுப்படுத்துகிறது?",
        opts_en=[
            "Article 51A makes voting mandatory for all citizens under threat of imprisonment.",
            "Article 51A(e) explicitly enjoins citizens to promote harmony and the spirit of common brotherhood amongst all people of India transcending religious, linguistic, and regional diversities.",
            "Article 51A grants executive power to local police to enforce religious rituals.",
            "Article 51A authorizes Parliament to revoke citizenship for non-payment of taxes."
        ],
        opts_ta=[
            "உறுப்பு 51A சிறைத்தண்டனை அச்சுறுத்தலின் கீழ் அனைத்து குடிமக்களுக்கும் வாக்களிப்பைக் கட்டாயமாக்குகிறது.",
            "உறுப்பு 51A(e) மதம், மொழி மற்றும் பிராந்திய வேறுபாடுகளைக் கடந்து இந்திய மக்கள் அனைவரிடையேயும் நல்லிணக்கத்தையும் பொதுவான சகோதரத்துவ உணர்வையும் வளர்க்கக் குடிமக்களை வெளிப்படையாகப் பணிக்கிறது.",
            "உறுப்பு 51A மதச்சடங்குகளை அமல்படுத்த உள்ளூர் காவல் துறைக்கு நிர்வாக அதிகாரம் அளிக்கிறது.",
            "உறுப்பு 51A வரி செலுத்தாததற்காகக் குடியுரிமையை ரத்து செய்ய நாடாளுமன்றத்திற்கு அதிகாரம் அளிக்கிறது."
        ],
        correct_ans="B",
        exp_en="Article 51A(e) in Part IVA directly operationalizes Fraternity by making it a duty of every citizen to promote harmony and common brotherhood transcending all diversities.",
        exp_ta="பகுதி IVA இல் உள்ள உறுப்பு 51A(e) அனைத்து வேறுபாடுகளையும் கடந்து நல்லிணக்கத்தையும் பொதுவான சகோதரத்துவத்தையும் வளர்ப்பதை ஒவ்வொரு குடிமகனின் கடமையாக்கி சகோதரத்துவத்தை நேரடியாக நடைமுறைப்படுத்துகிறது.",
        wno_dict={
            "A": {"en": "Incorrect. Voting is not a mandatory duty under Art 51A.", "ta": "தவறு. வாக்களிப்பது கட்டாயக் கடமை அல்ல."},
            "B": {"en": "Correct. Art 51A(e) promotes common brotherhood transcending diversities.", "ta": "சரி. உறுப்பு 51A(e) பொதுவான சகோதரத்துவத்தை ஊக்குவிக்கிறது."},
            "C": {"en": "Incorrect. Fundamental duties are non-enforceable by police.", "ta": "தவறு. கடமைகளைக் காவல்துறை அமல்படுத்த முடியாது."},
            "D": {"en": "Incorrect. Citizenship is governed by Part II Articles 5-11.", "ta": "தவறு. குடியுரிமை பகுதி II ஆல் ஆளப்படுகிறது."}
        },
        tip_en="Fraternity link: Preamble goal -> Single Citizenship (Part II) + Fundamental Duty Art 51A(e).",
        tip_ta="சகோதரத்துவ இணைப்பு: முகவுரை இலக்கு -> ஒற்றைக் குடியுரிமை (பகுதி II) + அடிப்படை கடமை உறுப்பு 51A(e).",
        rev_en="Article 51A(e) promotes fraternity and common brotherhood.",
        rev_ta="உறுப்பு 51A(e) சகோதரத்துவத்தையும் பொது சகோதர உணர்வையும் ஊக்குவிக்கிறது.",
        sources=["Preamble Notes Part 1 & 2"],
        bloom="Understand", est_sec=45, pyq_sim="High", tags=["Fraternity", "Fundamental Duties", "Article 51Ae"]
    ))

    # Q11 - Conceptual Distinction - Ans C
    qs.append(make_medium_q(
        q_id="PRE_M_011", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Medium", question_type="Conceptual Distinction",
        q_en="Which statement correctly distinguishes the 'Western Model of Secularism' from the 'Indian Model of Secularism'?",
        q_ta="மேற்கத்திய மதச்சார்பின்மை மாதிரியை' 'இந்திய மதச்சார்பின்மை மாதிரி'யிலிருந்து சரியாக வேறுபடுத்தும் கூற்று எது?",
        opts_en=[
            "Western model encourages state funding of all religions, whereas Indian model bans religion entirely.",
            "Western model allows State interference only in minority religions, whereas Indian model protects only majority religion.",
            "Western model involves strict water-tight separation between State and Religion (mutual exclusion), whereas Indian model practices 'Equal Respect to All Religions' (Sarva Dharma Sambhava) with state intervention for social reform.",
            "Western model is non-justiciable, whereas Indian secularism is an absolute fundamental right under Article 32."
        ],
        opts_ta=[
            "மேற்கத்திய மாதிரி அனைத்து மதங்களுக்கும் அரசு நிதியுதவியை ஊக்குவிக்கிறது; ஆனால் இந்திய மாதிரி மதத்தை முற்றிலும் தடை செய்கிறது.",
            "மேற்கத்திய மாதிரி சிறுபான்மை மதங்களில் மட்டுமே அரசு தலையீட்டை அனுமதிக்கிறது; ஆனால் இந்திய மாதிரி பெரும்பான்மை மதத்தை மட்டுமே பாதுகாக்கிறது.",
            "மேற்கத்திய மாதிரி அரசிற்கும் மதத்திற்கும் இடையே கடுமையான நீர்ப்புகா பிரிவினையைக் குறிக்கிறது (பரஸ்பர விலக்கல்); ஆனால் இந்திய மாதிரி சமூக சீர்திருத்தத்திற்கான அரசு தலையீட்டுடன் 'அனைத்து மதங்களுக்கும் சம மரியாதை' (சர்வ தர்ம சம்பவ) கொள்கையைப் பின்பற்றுகிறது.",
            "மேற்கத்திய மாதிரி நிலைநிறுத்த முடியாதது; ஆனால் இந்திய மதச்சார்பின்மை உறுப்பு 32 இன் கீழ் ஒரு பூரண அடிப்படை உரிமையாகும்."
        ],
        correct_ans="C",
        exp_en="Western secularism implies strict wall of separation (state does not support or reform any religion). Indian secularism is positive (equal respect Sarva Dharma Sambhava) permitting state reform (e.g. Art 17 untouchability).",
        exp_ta="மேற்கத்திய மதச்சார்பின்மை கடுமையான பிரிவினையைக் குறிக்கிறது. இந்திய மதச்சார்பின்மை நேர்மறையானது (சர்வ தர்ம சம்பவ) மேலும் சமூக சீர்திருத்தத்திற்கான அரசு தலையீட்டை (எ.கா. உறுப்பு 17 தீண்டாமை ஒழிப்பு) அனுமதிக்கிறது.",
        wno_dict={
            "A": {"en": "Incorrect. Reverses real principles.", "ta": "தவறு. உண்மைக் கோட்பாடுகளைத் தலைகீழாக மாற்றுகிறது."},
            "B": {"en": "Incorrect. Indian secularism protects all religions equally.", "ta": "தவறு. இந்திய மதச்சார்பின்மை அனைத்து மதங்களையும் சமமாகப் பாதுகாக்கிறது."},
            "C": {"en": "Correct. Western = Water-tight separation; Indian = Equal respect + Social reform capability.", "ta": "சரி. மேற்கத்திய = கடுமையான பிரிவினை; இந்திய = சம மரியாதை + சமூக சீர்திருத்த திறன்."},
            "D": {"en": "Incorrect. Secularism is a basic structure principle, not a single FR article.", "ta": "தவறு. மதச்சார்பின்மை ஒரு அடிப்படை அமைப்புக் கோட்பாடு."}
        },
        tip_en="Indian Secularism = Positive Concept = Sarva Dharma Sambhava (Equal respect to all religions).",
        tip_ta="இந்திய மதச்சார்பின்மை = நேர்மறைக் கருத்து = சர்வ தர்ம சம்பவ (அனைத்து மதங்களுக்கும் சம மரியாதை).",
        rev_en="Indian Secularism = Positive equal respect (Sarva Dharma Sambhava).",
        rev_ta="இந்திய மதச்சார்பின்மை = நேர்மறை சம மரியாதை (சர்வ தர்ம சம்பவ).",
        sources=["Preamble Notes Part 1"],
        bloom="Understand", est_sec=45, pyq_sim="High", tags=["Secularism", "Western vs Indian Secularism"]
    ))

    # Q12 - Application / Inference - Ans D
    qs.append(make_medium_q(
        q_id="PRE_M_012", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Medium", question_type="Application / Inference",
        q_en="India continues to be a member of the Commonwealth of Nations and the United Nations. How does this international association align with the Preamble's declaration of India as a 'Sovereign' state?",
        q_ta="இந்தியா காமன்வெல்த் நாடுகள் மற்றும் ஐக்கிய நாடுகளில் தொடர்ந்து உறுப்பினராக உள்ளது. இந்த சர்வதேச சேர்க்கை இந்தியாவை 'இறையாண்மை' கொண்ட நாடாக முகவுரை பிரகடனம் செய்வதோடு எவ்வாறு ஒத்துப்போகிறது?",
        opts_en=[
            "Commonwealth membership legally subordinates Indian Parliament to the British Crown.",
            "UN membership deprives India of its right to maintain an independent foreign policy.",
            "International memberships reduce India to a British Dominion status.",
            "Commonwealth and UN memberships are voluntary extra-legal declarations that do not limit or diminish India's supreme constitutional sovereignty in any manner."
        ],
        opts_ta=[
            "காமன்வெல்த் உறுப்பினர் தகுதி இந்திய நாடாளுமன்றத்தைப் பிரிட்டிஷ் முடிசூட்டு அதிகாரத்திற்குச் சட்டப்பூர்வமாகக் கீழ்ப்படுத்துகிறது.",
            "ஐ.நா உறுப்பினர் தகுதி இந்தியாவின் சுதந்திரமான வெளியுறவுக் கொள்கையைப் பராமரிக்கும் உரிமையைப் பறிக்கிறது.",
            "சர்வதேச உறுப்பினர் தகுதிகள் இந்தியாவைப் பிரிட்டிஷ் டொமினியன் நிலைக்குக் குறைக்கின்றன.",
            "காமன்வெல்த் மற்றும் ஐ.நா உறுப்பினர் தகுதிகள் இந்தியாவின் உச்ச அரசியலமைப்பு இறையாண்மையை எந்த வகையிலும் கட்டுப்படுத்தவோ குறைக்கவோ செய்யாத தன்னார்வ சட்டத்திற்கு அப்பாற்பட்ட பிரகடனங்கள் ஆகும்."
        ],
        correct_ans="D",
        exp_en="Constituent Assembly explicitly clarified that India's voluntary membership of Commonwealth/UN is an extra-legal association that does not compromise India's full external and internal sovereignty.",
        exp_ta="அரசியலமைப்புச் சபை காமன்வெல்த்/ஐ.நா வில் இந்தியாவின் தன்னார்வ உறுப்பினர் தகுதி சட்டத்திற்கு அப்பாற்பட்ட சேர்க்கை என்றும் அது இந்தியாவின் முழுமையான வெளிநாட்டு மற்றும் உள்நாட்டு இறையாண்மையை சமரசம் செய்யாது என்றும் தெளிவுபடுத்தியது.",
        wno_dict={
            "A": {"en": "Incorrect. Dominion status ended on Jan 26, 1950.", "ta": "தவறு. டொமினியன் நிலை 26 ஜனவரி 1950 இல் முடிந்தது."},
            "B": {"en": "Incorrect. India maintains completely independent foreign policy.", "ta": "தவறு. இந்தியா சுதந்திரமான வெளியுறவுக் கொள்கையைப் பராமரிக்கிறது."},
            "C": {"en": "Incorrect. India is a full Republic, not a Dominion.", "ta": "தவறு. இந்தியா ஒரு முழுமையான குடியரசு."},
            "D": {"en": "Correct. Voluntary memberships do not impair national sovereignty.", "ta": "சரி. தன்னார்வ உறுப்பினர் தகுதிகள் தேசிய இறையாண்மையைப் பாதிக்காது."}
        },
        tip_en="Commonwealth membership = Voluntary association; DOES NOT affect Sovereignty.",
        tip_ta="காமன்வெல்த் உறுப்பினர் தகுதி = தன்னார்வச் சேர்க்கை; இறையாண்மையைப் பாதிக்காது.",
        rev_en="UN/Commonwealth membership does not limit Indian Sovereignty.",
        rev_ta="ஐ.நா/காமன்வெல்த் உறுப்பினர் தகுதி இந்திய இறையாண்மையைக் குறைக்காது.",
        sources=["Preamble Notes Part 1"],
        bloom="Analyze", est_sec=45, pyq_sim="High", tags=["Sovereign", "Commonwealth", "Sovereignty Limits"]
    ))

    # Q13 - Case-law - Ans A
    qs.append(make_medium_q(
        q_id="PRE_M_013", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Medium", question_type="Case-law Based",
        q_en="In the landmark Kesavananda Bharati Case (1973), how did the Supreme Court view the relationship between the Preamble and the Basic Structure Doctrine?",
        q_ta="வரலாற்றுச் சிறப்புமிக்க கேசவாநந்த பாரதி வழக்கில் (1973), முகவுரைக்கும் அடிப்படை கட்டமைப்பு கோட்பாட்டிற்கும் இடையே உள்ள தொடர்பை உச்ச நீதிமன்றம் எவ்வாறு கருதியது?",
        opts_en=[
            "The SC held that the noble vision and objectives outlined in the Preamble constitute the core reservoir from which elements of the Basic Structure are identified.",
            "The SC held that the Basic Structure replaces the Preamble entirely.",
            "The SC held that the Preamble is subordinate to ordinary statutory laws.",
            "The SC held that only Article 368 contains the Basic Structure, not the Preamble."
        ],
        opts_ta=[
            "முகவுரையில் கோடிட்டுக் காட்டப்பட்டுள்ள உன்னதமான தொலைநோக்கு மற்றும் இலக்குகள் அடிப்படை கட்டமைப்பின் கூறுகள் அடையாளம் காணப்படும் முக்கிய நீர்த்தேக்கமாக அமைகின்றன என உச்ச நீதிமன்றம் கருதியது.",
            "அடிப்படை கட்டமைப்பு முகவுரையை முற்றிலும் மாற்றீடு செய்கிறது என உச்ச நீதிமன்றம் கருதியது.",
            "முகவுரை சாதாரண சட்டப்பூர்வ சட்டங்களுக்குக் கீழ்ப்பட்டது என உச்ச நீதிமன்றம் கருதியது.",
            "உறுப்பு 368 மட்டுமே அடிப்படை அமைப்பைக் கொண்டுள்ளது, முகவுரை அல்ல என உச்ச நீதிமன்றம் கருதியது."
        ],
        correct_ans="A",
        exp_en="In Kesavananda Bharati (1973), the SC observed that the Preamble embodies the grand blueprint of constitutional philosophy; hence key Preamble goals (Sovereignty, Democracy, Secularism) form the Basic Structure.",
        exp_ta="கேசவாநந்த பாரதி (1973) வழக்கில், முகவுரை அரசியலமைப்பு தத்துவத்தின் பெரும் நீலவரைபடத்தைக் கொண்டுள்ளது என உச்ச நீதிமன்றம் குறிப்பிட்டது; எனவே முக்கிய முகவுரை இலக்குகள் அடிப்படை அமைப்பை உருவாக்குகின்றன.",
        wno_dict={
            "A": {"en": "Correct. Preamble is the primary source/reservoir of Basic Structure elements.", "ta": "சரி. முகவுரை அடிப்படை கட்டமைப்பு கூறுகளின் முதன்மை மூலம்/நீர்த்தேக்கம்."},
            "B": {"en": "Incorrect. Basic Structure reinforces Preamble vision.", "ta": "தவறு. அடிப்படை கட்டமைப்பு முகவுரை தொலைநோக்கை வலுப்படுத்துகிறது."},
            "C": {"en": "Incorrect. Preamble is part of the supreme Constitution.", "ta": "தவறு. முகவுரை உச்ச அரசியலமைப்பின் பகுதி."},
            "D": {"en": "Incorrect. Article 368 is subject to Basic Structure derived from Preamble.", "ta": "தவறு. உறுப்பு 368 முகவுரையிலிருந்து பெறப்பட்ட அடிப்படை அமைப்புக்கு உட்பட்டது."}
        },
        tip_en="Kesavananda Bharati (1973) used Preamble as the foundation to build Basic Structure Doctrine.",
        tip_ta="கேசவாநந்த பாரதி (1973) முகவுரையை அடிப்படை கட்டமைப்பு கோட்பாட்டை உருவாக்க அடித்தளமாகப் பயன்படுத்தியது.",
        rev_en="Preamble = Core reservoir of Basic Structure principles.",
        rev_ta="முகவுரை = அடிப்படை கட்டமைப்பு கோட்பாடுகளின் முக்கிய நீர்த்தேக்கம்.",
        sources=["Preamble Notes Part 2"],
        bloom="Understand", est_sec=45, pyq_sim="High", tags=["Kesavananda Bharati", "Basic Structure", "Preamble Vision"]
    ))

    # Q14 - Constitutional Relationship - Ans B
    qs.append(make_medium_q(
        q_id="PRE_M_014", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Medium", question_type="Constitutional Relationship",
        q_en="What is the precise constitutional distinction between the Preamble and Part III (Fundamental Rights) regarding court enforcement?",
        q_ta="நீதிமன்ற அமலாக்கம் தொடர்பாக முகவுரைக்கும் பகுதி III (அடிப்படை உரிமைகள்) க்கும் இடையே உள்ள துல்லியமான அரசியலமைப்பு வேறுபாடு எது?",
        opts_en=[
            "Preamble is justiciable under Article 32, whereas Fundamental Rights are non-justiciable.",
            "Preamble is non-justiciable and cannot be enforced directly in court, whereas Fundamental Rights are justiciable and enforceable via Article 32 and Article 226 writs.",
            "Both Preamble and Fundamental Rights are non-justiciable.",
            "Fundamental Rights apply only to aliens, whereas Preamble applies only to citizens."
        ],
        opts_ta=[
            "முகவுரை உறுப்பு 32 இன் கீழ் நிலைநிறுத்தக்கூடியது; ஆனால் அடிப்படை உரிமைகள் நிலைநிறுத்த முடியாதவை.",
            "முகவுரை நிலைநிறுத்த முடியாதது மற்றும் நீதிமன்றத்தில் நேரடியாக அமல்படுத்த முடியாது; ஆனால் அடிப்படை உரிமைகள் நிலைநிறுத்தக்கூடியவை மற்றும் உறுப்பு 32 மற்றும் உறுப்பு 226 பேராணைகள் மூலம் அமல்படுத்தத்தக்கவை.",
            "முகவுரை மற்றும் அடிப்படை உரிமைகள் இரண்டும் நிலைநிறுத்த முடியாதவை.",
            "அடிப்படை உரிமைகள் அந்நியர்களுக்கு மட்டுமே பொருந்தும்; ஆனால் முகவுரை குடிமக்களுக்கு மட்டுமே பொருந்தும்."
        ],
        correct_ans="B",
        exp_en="Fundamental Rights in Part III are justiciable (citizens can move Supreme Court under Art 32 for enforcement). Preamble is non-justiciable (no direct writ remedy for Preamble violation alone).",
        exp_ta="பகுதி III இல் உள்ள அடிப்படை உரிமைகள் நிலைநிறுத்தக்கூடியவை (குடிமக்கள் அமலாக்கத்திற்கு உறுப்பு 32 இன் கீழ் உச்ச நீதிமன்றத்தை அணுகலாம்). முகவுரை நிலைநிறுத்த முடியாதது (முகவுரை மீறலுக்கு மட்டும் நேரடியாகப் பேராணைத் தீர்வு இல்லை).",
        wno_dict={
            "A": {"en": "Incorrect. Reverses justiciability attributes.", "ta": "தவறு. நிலைநிறுத்தும் பண்புகளைத் தலைகீழாக மாற்றுகிறது."},
            "B": {"en": "Correct. Preamble = Non-justiciable; FRs = Justiciable (Arts 32/226).", "ta": "சரி. முகவுரை = நிலைநிறுத்த முடியாதது; FR = நிலைநிறுத்தக்கூடியது."},
            "C": {"en": "Incorrect. FRs are justiciable.", "ta": "தவறு. அடிப்படை உரிமைகள் நிலைநிறுத்தக்கூடியவை."},
            "D": {"en": "Incorrect. FRs apply to citizens and aliens (certain articles).", "ta": "தவறு. அடிப்படை உரிமைகள் குடிமக்களுக்கும் அந்நியர்களுக்கும் பொருந்தும்."}
        },
        tip_en="Preamble is NON-JUSTICIABLE; Fundamental Rights (Part III) are JUSTICIABLE.",
        tip_ta="முகவுரை நிலைநிறுத்த முடியாதது; அடிப்படை உரிமைகள் (பகுதி III) நிலைநிறுத்தக்கூடியவை.",
        rev_en="Preamble = Non-justiciable vs Part III FRs = Justiciable.",
        rev_ta="முகவுரை = நிலைநிறுத்த முடியாதது vs பகுதி III FR = நிலைநிறுத்தக்கூடியது.",
        sources=["Preamble Notes Part 1 & 2"],
        bloom="Understand", est_sec=45, pyq_sim="High", tags=["Justiciability", "Part III", "Article 32"]
    ))

    # Q15 - Conceptual Distinction - Ans C
    qs.append(make_medium_q(
        q_id="PRE_M_015", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Medium", question_type="Conceptual Distinction",
        q_en="Which statement correctly explains why 'Democratic Socialism' adopted in India differs from traditional 'Communistic Socialism'?",
        q_ta="இந்தியாவில் ஏற்றுக்கொள்ளப்பட்ட 'ஜனநாயக சமதர்மம்' பாரம்பரிய 'கம்யூனிச சமதர்மத்தி'லிருந்து ஏன் வேறுபடுகிறது என்பதைச் சரியாக விவரிக்கும் கூற்று எது?",
        opts_en=[
            "Democratic Socialism abolishes all private property immediately, whereas Communistic Socialism allows private enterprise.",
            "Democratic Socialism rejects democratic elections, whereas Communistic Socialism relies on adult franchise.",
            "Democratic Socialism believes in a 'Mixed Economy' where public and private sectors co-exist side-by-side, whereas Communistic Socialism involves complete nationalization of all production means and abolition of private property.",
            "Democratic Socialism applies only to rural agriculture, whereas Communistic Socialism applies to urban industries."
        ],
        opts_ta=[
            "ஜனநாயக சமதர்மம் அனைத்துத் தனியார் சொத்துக்களையும் உடனடியாக ஒழிக்கிறது; ஆனால் கம்யூனிச சமதர்மம் தனியார் நிறுவனங்களை அனுமதிக்கிறது.",
            "ஜனநாயக சமதர்மம் ஜனநாயகத் தேர்தல்களை நிராகரிக்கிறது; ஆனால் கம்யூனிச சமதர்மம் வயதுவந்தோர் வாக்குரிமையை நம்பியுள்ளது.",
            "ஜனநாயக சமதர்மம் பொது மற்றும் தனியார் துறைகள் பக்கவாட்டில் இணைந்து செயல்படும் 'கலப்பு பொருளாதாரத்தை' நம்புகிறது; ஆனால் கம்யூனிச சமதர்மம் அனைத்து உற்பத்திச் சாதனங்களையும் முற்றிலும் அரசுமயமாக்குதலையும் தனியார் சொத்து ஒழிப்பையும் உள்ளடக்கியது.",
            "ஜனநாயக சமதர்மம் கிராமப்புற விவசாயத்திற்கு மட்டுமே பொருந்தும்; ஆனால் கம்யூனிச சமதர்மம் நகர்ப்புற தொழில்களுக்குப் பொருந்தும்."
        ],
        correct_ans="C",
        exp_en="Democratic Socialism (India) holds faith in a Mixed Economy where private and public sectors co-exist to eliminate poverty and inequality. Communistic (State) Socialism nationalizes all property completely.",
        exp_ta="ஜனநாயக சமதர்மம் (இந்தியா) வறுமை மற்றும் சமத்துவமின்மையை ஒழிக்க தனியார் மற்றும் பொதுத் துறைகள் இணைந்து செயல்படும் கலப்பு பொருளாதாரத்தை நம்புகிறது. கம்யூனிச சமதர்மம் அனைத்து சொத்துக்களையும் முற்றிலும் அரசுமயமாக்குகிறது.",
        wno_dict={
            "A": {"en": "Incorrect. Reverses the property ownership concepts.", "ta": "தவறு. சொத்து உரிமை கருத்துக்களைத் தலைகீழாக மாற்றுகிறது."},
            "B": {"en": "Incorrect. Democratic socialism relies on democratic processes.", "ta": "தவறு. ஜனநாயக சமதர்மம் ஜனநாயக முறைகளை நம்புகிறது."},
            "C": {"en": "Correct. Democratic Socialism = Mixed Economy; Communistic Socialism = State Monopoly.", "ta": "சரி. ஜனநாயக சமதர்மம் = கலப்பு பொருளாதாரம்; கம்யூனிச சமதர்மம் = அரசு ஏகபோகம்."},
            "D": {"en": "Incorrect. Applies across the entire national economy.", "ta": "தவறு. தேசிய பொருளாதாரம் முழுமைக்கும் பொருந்தும்."}
        },
        tip_en="Indian Socialism = Democratic Socialism = Blend of Marxism and Gandhism leaning heavily towards Gandhian Socialism.",
        tip_ta="இந்திய சமதர்மம் = ஜனநாயக சமதர்மம் = காந்திய சமதர்மத்தை நோக்கி சாய்ந்த மார்க்சியம் மற்றும் காந்தியத்தின் கலவை.",
        rev_en="Democratic Socialism = Mixed Economy co-existence.",
        rev_ta="ஜனநாயக சமதர்மம் = கலப்பு பொருளாதார இணைந்திருத்தல்.",
        sources=["Preamble Notes Part 1"],
        bloom="Understand", est_sec=45, pyq_sim="High", tags=["Democratic Socialism", "Mixed Economy", "Communistic Socialism"]
    ))

    # Q16 - Application / Inference - Ans D
    qs.append(make_medium_q(
        q_id="PRE_M_016", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Medium", question_type="Application / Inference",
        q_en="Suppose a litigation challenges a reservation policy under Article 16(4) claiming it violates 'Equality of Opportunity' in the Preamble. How does constitutional jurisprudence resolve this issue?",
        q_ta="உறுப்பு 16(4) இன் கீழ் உள்ள ஒரு இடஒதுக்கீட்டுக் கொள்கை முகவுரையில் உள்ள 'வாய்ப்பு சமத்துவத்தை' மீறுகிறது என்று கூறி ஒரு வழக்கு சவாலுக்கு உட்படுத்தப்படுகிறது எனக் கொள்வோம். அரசியலமைப்பு வழக்கியல் இந்தப் பிரச்சனையை எவ்வாறு தீர்க்கிறது?",
        opts_en=[
            "The Court strikes down Article 16(4) because Preamble overrides Part III.",
            "The Court declares reservation unconstitutional because Equality means identical treatment without exception.",
            "The Court holds that Preamble cannot be read along with Fundamental Rights.",
            "The Court holds that Equality of Opportunity permits reasonable classification and affirmative action (Art 16(4)) to achieve real socio-economic equality for backward classes."
        ],
        opts_ta=[
            "முகவுரை பகுதி III ஐ மேலெழுதுவதால் நீதிமன்றம் உறுப்பு 16(4) ஐ ரத்து செய்கிறது.",
            "சமத்துவம் என்பது எவ்வித விதிவிலக்கும் இன்றி ஒரே மாதிரியான நடையைக் குறிக்கும் என்பதால் இடஒதுக்கீடு அரசியலமைப்பிற்கு முரணானது என நீதிமன்றம் அறிவிக்கிறது.",
            "முகவுரையை அடிப்படை உரிமைகளுடன் சேர்த்துப் படிக்க முடியாது என நீதிமன்றம் கருதுகிறது.",
            "பிற்படுத்தப்பட்ட வகுப்பினருக்கு உண்மையான சமூக-பொருளாதார சமத்துவத்தை அடைய வாய்ப்பு சமத்துவம் நியாயமான வகைப்பாட்டையும் சாதகமான நடவடிக்கையையும் (உறுப்பு 16(4)) அனுமதிக்கிறது என நீதிமன்றம் கருதுகிறது."
        ],
        correct_ans="D",
        exp_en="Constitutional Equality does not mean identical treatment in all circumstances. It permits reasonable classification and protective discrimination (affirmative action under Arts 15(4) & 16(4)) to achieve true equality of opportunity.",
        exp_ta="அரசியலமைப்பு சமத்துவம் என்பது அனைத்து சூழல்களிலும் ஒரே மாதிரியான நடத்துதலைக் குறிக்காது. உண்மையான வாய்ப்பு சமத்துவத்தை அடைய இது நியாயமான வகைப்பாட்டையும் பாதுகாப்பு பாகுபாட்டையும் (உறுப்புகள் 15(4) & 16(4)) அனுமதிக்கிறது.",
        wno_dict={
            "A": {"en": "Incorrect. Preamble cannot override clear constitutional text.", "ta": "தவறு. முகவுரை தெளிவான உரையை மேலெழுத முடியாது."},
            "B": {"en": "Incorrect. Equality in India is substantive, not formal identicalness.", "ta": "தவறு. சமத்துவம் என்பது பொருள்சார்ந்தது, முறையான ஒரே மாதிரி அல்ல."},
            "C": {"en": "Incorrect. Preamble and FRs must be read harmoniously.", "ta": "தவறு. முகவுரையும் FR உம் சீராகப் படிக்கப்பட வேண்டும்."},
            "D": {"en": "Correct. Equality permits reasonable classification for backward classes.", "ta": "சரி. சமத்துவம் பிற்படுத்தப்பட்ட வகுப்பினருக்கு நியாயமான வகைப்பாட்டை அனுமதிக்கிறது."}
        },
        tip_en="Equality in Preamble allows Protective Discrimination / Reservation under Articles 15(4) & 16(4).",
        tip_ta="முகவுரையில் உள்ள சமத்துவம் உறுப்புகள் 15(4) & 16(4) இன் கீழ் பாதுகாப்பு பாகுபாடு / இடஒதுக்கீட்டை அனுமதிக்கிறது.",
        rev_en="Equality permits reasonable classification for protective discrimination.",
        rev_ta="சமத்துவம் பாதுகாப்பு பாகுபாட்டிற்கு நியாயமான வகைப்பாட்டை அனுமதிக்கிறது.",
        sources=["Preamble Notes Part 1"],
        bloom="Apply", est_sec=45, pyq_sim="High", tags=["Equality of Opportunity", "Reservation", "Article 16(4)"]
    ))

    # Q17 - Direct - Ans A
    qs.append(make_medium_q(
        q_id="PRE_M_017", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Medium", question_type="Direct",
        q_en="Which Supreme Court judgment first observed that harmony and balance between Fundamental Rights (Part III) and Directive Principles (Part IV) is an essential feature of the Basic Structure, carrying out Preamble objectives?",
        q_ta="அடிப்படை உரிமைகள் (பகுதி III) மற்றும் வழிகாட்டு நெறிமுறைகள் (பகுதி IV) இடையேயான நல்லிணக்கமும் சமநிலையும் முகவுரை இலக்குகளை நிறைவேற்றும் அடிப்படை அமைப்பின் இன்றியமையாத அம்சமாகும் என்று முதன்முதலில் குறிப்பிட்ட உச்ச நீதிமன்ற தீர்ப்பு எது?",
        opts_en=[
            "Minerva Mills Case (1980)",
            "Golaknath Case (1967)",
            "Shankari Prasad Case (1951)",
            "Champakam Dorairajan Case (1951)"
        ],
        opts_ta=[
            "மினர்வா மில்ஸ் வழக்கு (1980)",
            "கோலக்நாத் வழக்கு (1967)",
            "சங்கரி பிரசாத் வழக்கு (1951)",
            "செம்பகம் துரைராஜன் வழக்கு (1951)"
        ],
        correct_ans="A",
        exp_en="In Minerva Mills Case (1980), the SC held that the harmony and balance between Part III and Part IV is an essential feature of the Basic Structure, fulfilling the socio-economic vision of the Preamble.",
        exp_ta="மினர்வா மில்ஸ் வழக்கில் (1980), பகுதி III மற்றும் பகுதி IV இடையேயான நல்லிணக்கமும் சமநிலையும் முகவுரையின் சமூக-பொருளாதார தொலைநோக்கை நிறைவேற்றும் அடிப்படை அமைப்பின் இன்றியமையாத அம்சமாகும் என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
        wno_dict={
            "A": {"en": "Correct. Minerva Mills 1980 established harmony between Part III & IV as Basic Structure.", "ta": "சரி. மினர்வா மில்ஸ் 1980 பகுதி III & IV நல்லிணக்கத்தை அடிப்படை அமைப்பாக நிறுவியது."},
            "B": {"en": "Incorrect. Golaknath 1967 gave primacy to FRs.", "ta": "தவறு. கோலக்நாத் 1967 FR க்கு முதன்மை அளித்தது."},
            "C": {"en": "Incorrect. Shankari Prasad 1951 allowed FR amendment.", "ta": "தவறு. சங்கரி பிரசாத் 1951 FR திருத்தத்தை அனுமதித்தது."},
            "D": {"en": "Incorrect. Champakam Dorairajan 1951 made DPSP subordinate to FR.", "ta": "தவறு. செம்பகம் துரைராஜன் 1951 DPSP ஐ FR க்கு கீழ்ப்படுத்தியது."}
        },
        tip_en="Minerva Mills (1980) = Harmony between Part III (FR) and Part IV (DPSP) is Basic Structure.",
        tip_ta="மினர்வா மில்ஸ் (1980) = பகுதி III (FR) மற்றும் பகுதி IV (DPSP) இடையேயான நல்லிணக்கம் அடிப்படை அமைப்பாகும்.",
        rev_en="Minerva Mills 1980 = Harmony of Part III & Part IV is Basic Structure.",
        rev_ta="மினர்வா மில்ஸ் 1980 = பகுதி III & பகுதி IV நல்லிணக்கம் அடிப்படை அமைப்பாகும்.",
        sources=["Preamble Notes Part 1 & 2"],
        bloom="Remember", est_sec=45, pyq_sim="High", tags=["Minerva Mills", "Basic Structure", "Harmony FR DPSP"]
    ))

    # Q18 - Conceptual Distinction - Ans B
    qs.append(make_medium_q(
        q_id="PRE_M_018", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Medium", question_type="Conceptual Distinction",
        q_en="Which statement correctly distinguishes between 'Civic Equality', 'Political Equality', and 'Economic Equality' as reflected in the Constitution?",
        q_ta="அரசியலமைப்பில் பிரதிபலிப்பது போல 'குடிமைச் சமத்துவம்', 'அரசியல் சமத்துவம்' மற்றும் 'பொருளாதாரச் சமத்துவம்' ஆகியவற்றைச் சரியாக வேறுபடுத்தும் கூற்று எது?",
        opts_en=[
            "Civic Equality is found in DPSP, Political Equality in Part III, and Economic Equality in Preamble.",
            "Civic Equality is secured through Articles 14-18 (Fundamental Rights), Political Equality through Articles 325-326 (Electoral Rolls & Adult Franchise), and Economic Equality through Article 39 (DPSP policy directives).",
            "Civic Equality applies only to aliens, Political Equality to ministers, and Economic Equality to foreign investors.",
            "Civic Equality was added by 42nd Amendment, Political Equality by 44th Amendment, and Economic Equality by 86th Amendment."
        ],
        opts_ta=[
            "குடிமைச் சமத்துவம் DPSP இலும், அரசியல் சமத்துவம் பகுதி III இலும், பொருளாதாரச் சமத்துவம் முகவுரையிலும் காணப்படுகிறது.",
            "குடிமைச் சமத்துவம் உறுப்புகள் 14-18 (அடிப்படை உரிமைகள்) மூலமும், அரசியல் சமத்துவம் உறுப்புகள் 325-326 (வாக்காளர் பட்டியல் & வயதுவந்தோர் வாக்குரிமை) மூலமும், பொருளாதாரச் சமத்துவம் உறுப்பு 39 (DPSP கொள்கை வழிகாட்டுதல்கள்) மூலமும் பாதுகாக்கப்படுகிறது.",
            "குடிமைச் சமத்துவம் அந்நியர்களுக்கு மட்டுமே பொருந்தும், அரசியல் சமத்துவம் அமைச்சர்களுக்கு, பொருளாதாரச் சமத்துவம் வெளிநாட்டு முதலீட்டாளர்களுக்கு.",
            "குடிமைச் சமத்துவம் 42வது திருத்தத்தாலும், அரசியல் சமத்துவம் 44வது திருத்தத்தாலும், பொருளாதாரச் சமத்துவம் 86வது திருத்தத்தாலும் சேர்க்கப்பட்டன."
        ],
        correct_ans="B",
        exp_en="Civic Equality = Articles 14-18 (Part III). Political Equality = Article 325 (no electoral roll discrimination) & Article 326 (Adult Franchise). Economic Equality = Article 39 (DPSP equal livelihood & wealth distribution).",
        exp_ta="குடிமைச் சமத்துவம் = உறுப்புகள் 14-18 (பகுதி III). அரசியல் சமத்துவம் = உறுப்பு 325 (வாக்காளர் பட்டியல் பாகுபாடின்மை) & உறுப்பு 326 (வயதுவந்தோர் வாக்குரிமை). பொருளாதாரச் சமத்துவம் = உறுப்பு 39 (DPSP சம வாழ்வாதாரம் & செல்வ விநியோகம்).",
        wno_dict={
            "A": {"en": "Incorrect. Misplaces the constitutional chapters.", "ta": "தவறு. அரசியலமைப்பு அத்தியாயங்களை தவறாக வைக்கிறது."},
            "B": {"en": "Correct. Maps Civic (Arts 14-18), Political (Arts 325-326), and Economic (Art 39) equality accurately.", "ta": "சரி. குடிமை, அரசியல், பொருளாதார சமத்துவங்களைத் துல்லியமாகக் காட்டுகிறது."},
            "C": {"en": "Incorrect. Completely absurd options.", "ta": "தவறு. முற்றிலும் பொருத்தமற்ற விருப்பங்கள்."},
            "D": {"en": "Incorrect. These amendments did not introduce these equality categories.", "ta": "தவறு. இந்தத் திருத்தங்கள் இவைகளை அறிமுகப்படுத்தவில்லை."}
        },
        tip_en="Civic Equality = Arts 14-18; Political Equality = Arts 325, 326; Economic Equality = Art 39.",
        tip_ta="குடிமைச் சமத்துவம் = உறுப்புகள் 14-18; அரசியல் சமத்துவம் = உறுப்புகள் 325, 326; பொருளாதாரச் சமத்துவம் = உறுப்பு 39.",
        rev_en="Civic = Arts 14-18; Political = Arts 325-326; Economic = Art 39 DPSP.",
        rev_ta="குடிமை = உறுப்புகள் 14-18; அரசியல் = உறுப்புகள் 325-326; பொருளாதாரம் = உறுப்பு 39 DPSP.",
        sources=["Preamble Notes Part 1"],
        bloom="Understand", est_sec=45, pyq_sim="High", tags=["Equality Dimensions", "Civic Political Economic"]
    ))

    # Q19 - TNPSC Trap - Ans C
    qs.append(make_medium_q(
        q_id="PRE_M_019", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Medium", question_type="TNPSC Trap",
        q_en="Which of the following statements is INCORRECT regarding the 42nd Constitutional Amendment Act 1976 and the Preamble?",
        q_ta="1976 இன் 42வது அரசியலமைப்பு திருத்தச் சட்டம் மற்றும் முகவுரை தொடர்பாக பின்வரும் கூற்றுகளில் எது தவறானது?",
        opts_en=[
            "The 42nd Amendment Act added three words: Socialist, Secular, and Integrity.",
            "The 42nd Amendment Act was enacted during the Prime Ministership of Mrs. Indira Gandhi.",
            "The word 'Secular' was added to the Fraternity section of the Preamble.",
            "The Preamble has been amended only once in history so far."
        ],
        opts_ta=[
            "42வது திருத்தச் சட்டம் மூன்று சொற்களைச் சேர்த்தது: சமதர்ம, மதச்சார்பற்ற மற்றும் ஒருமைப்பாடு.",
            "42வது திருத்தச் சட்டம் திருமதி இந்திரா காந்தி பிரதமராக இருந்தபோது இயற்றப்பட்டது.",
            "மதச்சார்பற்ற' (Secular) என்ற சொல் முகவுரையின் சகோதரத்துவப் பகுதியில் சேர்க்கப்பட்டது.",
            "முகவுரை வரலாற்றில் இதுவரை ஒரே ஒரு முறை மட்டுமே திருத்தப்பட்டுள்ளது."
        ],
        correct_ans="C",
        exp_en="Statement C is INCORRECT because 'Secular' was added to the NATURE of State section ('Sovereign Socialist Secular Democratic Republic'). 'Integrity' was added to the Fraternity section.",
        exp_ta="கூற்று C தவறானது, ஏனெனில் 'மதச்சார்பற்ற' என்ற சொல் அரசின் தன்மையில் சேர்க்கப்பட்டது ('இறையாண்மை சமதர்ம மதச்சார்பற்ற ஜனநாயக குடியரசு'). 'ஒருமைப்பாடு' என்ற சொல்லே சகோதரத்துவப் பகுதியில் சேர்க்கப்பட்டது.",
        wno_dict={
            "A": {"en": "Incorrect statement choice. Statement A is TRUE.", "ta": "தவறு. கூற்று A சரி."},
            "B": {"en": "Incorrect statement choice. Statement B is TRUE.", "ta": "தவறு. கூற்று B சரி."},
            "C": {"en": "Correct statement choice (this statement is FALSE). Secular was added to Nature section, not Fraternity.", "ta": "சரி (இந்தக் கூற்று தவறானது). மதச்சார்பற்ற அரசின் தன்மையில் சேர்க்கப்பட்டது."},
            "D": {"en": "Incorrect statement choice. Statement D is TRUE.", "ta": "தவறு. கூற்று D சரி."}
        },
        tip_en="TNPSC Trap: 'Socialist' and 'Secular' belong to Nature section; 'Integrity' belongs to Fraternity section.",
        tip_ta="TNPSC பொறி: 'சமதர்ம' மற்றும் 'மதச்சார்பற்ற' அரசின் தன்மையைக் குறிக்கும்; 'ஒருமைப்பாடு' சகோதரத்துவத்தைக் குறிக்கும்.",
        rev_en="Socialist & Secular = Nature section; Integrity = Fraternity section.",
        rev_ta="சமதர்ம & மதச்சார்பற்ற = அரசின் தன்மை; ஒருமைப்பாடு = சகோதரத்துவம்.",
        sources=["Preamble Notes Part 1 & 2"],
        bloom="Analyze", est_sec=45, pyq_sim="High", tags=["42nd Amendment", "Secular", "TNPSC Trap"]
    ))

    # Q20 - Direct - Ans D
    qs.append(make_medium_q(
        q_id="PRE_M_020", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Medium", question_type="Direct",
        q_en="What is the historical significance of 24th April 1973 in Indian constitutional law?",
        q_ta="இந்திய அரசியலமைப்புச் சட்டத்தில் 24 ஏப்ரல் 1973 இன் வரலாற்று முக்கியத்துவம் என்ன?",
        opts_en=[
            "It was the day the 42nd Amendment Act came into force.",
            "It was the day the Constituent Assembly adopted the Preamble.",
            "It was the day the Berubari Union judgment was delivered.",
            "It was the day the Supreme Court delivered the landmark Kesavananda Bharati judgment declaring the Basic Structure Doctrine and holding Preamble as part of the Constitution."
        ],
        opts_ta=[
            "இது 42வது திருத்தச் சட்டம் அமலுக்கு வந்த நாளாகும்.",
            "இது அரசியலமைப்புச் சபை முகவுரையை ஏற்ற நாளாகும்.",
            "இது பெருபாரி யூனியன் தீர்ப்பு வழங்கப்பட்ட நாளாகும்.",
            "இது உச்ச நீதிமன்றம் அடிப்படை கட்டமைப்பு கோட்பாட்டை அறிவித்து முகவுரை அரசியலமைப்பின் ஒரு பகுதி எனத் தீர்ப்பளித்த வரலாற்றுச் சிறப்புமிக்க கேசவாநந்த பாரதி தீர்ப்பை வழங்கிய நாளாகும்."
        ],
        correct_ans="D",
        exp_en="On 24th April 1973, the 13-judge bench delivered the landmark Kesavananda Bharati judgment, creating the Basic Structure Doctrine and overruling Berubari to hold Preamble as part of the Constitution.",
        exp_ta="24 ஏப்ரல் 1973 அன்று, 13 நீதிபதிகள் கொண்ட அமர்வு வரலாற்றுச் சிறப்புமிக்க கேசவாநந்த பாரதி தீர்ப்பை வழங்கி, அடிப்படை கட்டமைப்பு கோட்பாட்டை உருவாக்கி முகவுரை அரசியலமைப்பின் பகுதி எனத் தீர்ப்பளித்தது.",
        wno_dict={
            "A": {"en": "Incorrect. 42nd Amendment enforcement was Jan 3, 1977.", "ta": "தவறு. 42வது திருத்தம் அமலானது 3 ஜனவரி 1977."},
            "B": {"en": "Incorrect. Adoption date was Nov 26, 1949.", "ta": "தவறு. ஏற்றுக்கொள்ளப்பட்ட நாள் 26 நவம்பர் 1949."},
            "C": {"en": "Incorrect. Berubari was 1960.", "ta": "தவறு. பெருபாரி 1960."},
            "D": {"en": "Correct. 24 April 1973 = Kesavananda Bharati Judgment day.", "ta": "சரி. 24 ஏப்ரல் 1973 = கேசவாநந்த பாரதி தீர்ப்பு நாள்."}
        },
        tip_en="24 April 1973 = Kesavananda Bharati Judgment Day (Basic Structure Doctrine born).",
        tip_ta="24 ஏப்ரல் 1973 = கேசவாநந்த பாரதி தீர்ப்பு நாள் (அடிப்படை கட்டமைப்பு கோட்பாடு பிறந்தது).",
        rev_en="24th April 1973 = Kesavananda Bharati Judgment.",
        rev_ta="24 ஏப்ரல் 1973 = கேசவாநந்த பாரதி தீர்ப்பு.",
        sources=["Preamble Notes Part 2"],
        bloom="Remember", est_sec=30, pyq_sim="High", tags=["Kesavananda Bharati", "24 April 1973", "Basic Structure"]
    ))

    # Q21 - Conceptual Distinction - Ans A
    qs.append(make_medium_q(
        q_id="PRE_M_021", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Medium", question_type="Conceptual Distinction",
        q_en="Which statement correctly contrasts the legal enforceability of Fundamental Rights (Part III) with Directive Principles (Part IV) and the Preamble?",
        q_ta="அடிப்படை உரிமைகள் (பகுதி III), வழிகாட்டு நெறிமுறைகள் (பகுதி IV) மற்றும் முகவுரை ஆகியவற்றின் சட்டப்பூர்வ அமலாக்கத்தை சரியாக வேறுபடுத்தும் கூற்று எது?",
        opts_en=[
            "Part III (FRs) is justiciable; Part IV (DPSPs) and the Preamble are non-justiciable.",
            "Preamble and Part IV are justiciable; Part III is non-justiciable.",
            "All three (Part III, Part IV, Preamble) are equally justiciable under Article 32.",
            "All three (Part III, Part IV, Preamble) are completely non-justiciable."
        ],
        opts_ta=[
            "பகுதி III (FR) நிலைநிறுத்தக்கூடியது; பகுதி IV (DPSP) மற்றும் முகவுரை நிலைநிறுத்த முடியாதவை.",
            "முகவுரை மற்றும் பகுதி IV நிலைநிறுத்தக்கூடியவை; பகுதி III நிலைநிறுத்த முடியாதது.",
            "மூன்றும் (பகுதி III, பகுதி IV, முகவுரை) உறுப்பு 32 இன் கீழ் சமமாக நிலைநிறுத்தக்கூடியவை.",
            "மூன்றும் (பகுதி III, பகுதி IV, முகவுரை) முற்றிலும் நிலைநிறுத்த முடியாதவை."
        ],
        correct_ans="A",
        exp_en="Part III FRs are justiciable (enforceable by courts under Art 32/226). Part IV DPSPs (Art 37) and the Preamble are non-justiciable (not enforceable by courts directly).",
        exp_ta="பகுதி III FR நிலைநிறுத்தக்கூடியவை (உறுப்புகள் 32/226 இன் கீழ் அமல்படுத்தத்தக்கவை). பகுதி IV DPSP (உறுப்பு 37) மற்றும் முகவுரை நிலைநிறுத்த முடியாதவை (நீதிமன்றங்களால் நேரடியாக அமல்படுத்த முடியாது).",
        wno_dict={
            "A": {"en": "Correct. FRs = Justiciable; DPSPs & Preamble = Non-justiciable.", "ta": "சரி. FR = நிலைநிறுத்தக்கூடியது; DPSP & முகவுரை = நிலைநிறுத்த முடியாதவை."},
            "B": {"en": "Incorrect. Reverses real legal positions.", "ta": "தவறு. சட்ட நிலைகளை தலைகீழாக மாற்றுகிறது."},
            "C": {"en": "Incorrect. DPSPs and Preamble are not enforceable via Art 32.", "ta": "தவறு. DPSP மற்றும் முகவுரை உறுப்பு 32 மூலம் அமல்படுத்த முடியாது."},
            "D": {"en": "Incorrect. Part III is justiciable.", "ta": "தவறு. பகுதி III நிலைநிறுத்தக்கூடியது."}
        },
        tip_en="Justiciable: Part III (FRs) ONLY. Non-Justiciable: Preamble, Part IV (DPSPs), Part IVA (FDs).",
        tip_ta="நிலைநிறுத்தக்கூடியது: பகுதி III (FR) மட்டுமே. நிலைநிறுத்த முடியாதவை: முகவுரை, பகுதி IV (DPSP), பகுதி IVA (FD).",
        rev_en="Justiciable = Part III FRs only. Non-justiciable = Preamble & DPSPs.",
        rev_ta="நிலைநிறுத்தக்கூடியது = பகுதி III FR மட்டுமே. நிலைநிறுத்த முடியாதவை = முகவுரை & DPSP.",
        sources=["Preamble Notes Part 1 & 2"],
        bloom="Understand", est_sec=45, pyq_sim="High", tags=["Justiciability", "FR DPSP Preamble", "Article 37"]
    ))

    # Q22 - Application / Inference - Ans B
    qs.append(make_medium_q(
        q_id="PRE_M_022", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Medium", question_type="Application / Inference",
        q_en="Suppose a petitioner files a writ petition under Article 32 requesting the Supreme Court to issue a mandamus compelling Parliament to enact a law implementing 'Economic Justice' mentioned in the Preamble. How will the Supreme Court respond?",
        q_ta="முகவுரையில் குறிப்பிடப்பட்டுள்ள 'பொருளாதார நீதியை' அமல்படுத்தும் சட்டத்தை இயற்றுமாறு நாடாளுமன்றத்திற்கு உத்தரவிடக் கோரி ஒரு மனுதாரர் உறுப்பு 32 இன் கீழ் உச்ச நீதிமன்றத்தில் பேராணை மனு தாக்கல் செய்கிறார் எனக் கொள்வோம். உச்ச நீதிமன்றம் எவ்வாறு பதிலளிக்கும்?",
        opts_en=[
            "The Court will issue a mandamus because Preamble overrides legislative discretion.",
            "The Court will dismiss the petition because Preamble is non-justiciable and cannot independently confer a cause of action or compel legislative law-making.",
            "The Court will arrest the Prime Minister for contempt.",
            "The Court will refer the case to the Election Commission."
        ],
        opts_ta=[
            "முகவுரை சட்டமன்ற விருப்ப அதிகாரத்தை மேலெழுதுவதால் நீதிமன்றம் பேராணை பிறப்பிக்கும்.",
            "முகவுரை நிலைநிறுத்த முடியாதது என்பதால் மனுவை நீதிமன்றம் தள்ளுபடி செய்யும், மேலும் இது சுதந்திரமாக ஒரு வழக்காடு மூலத்தை வழங்கவோ சட்டமன்றச் சட்டமாக்கத்தைக் கட்டாயப்படுத்தவோ முடியாது.",
            "நீதிமன்ற அவமதிப்பிற்காக நீதிமன்றம் பிரதமரைக் கைது செய்யும்.",
            "நீதிமன்றம் இந்த வழக்கை தேர்தல் ஆணையத்திற்கு அனுப்பும்."
        ],
        correct_ans="B",
        exp_en="The Supreme Court will dismiss the petition because the Preamble is non-justiciable and confers NO independent source of legislative power nor does it allow courts to compel Parliament to legislate.",
        exp_ta="முகவுரை நிலைநிறுத்த முடியாதது மற்றும் நாடாளுமன்றத்தைச் சட்டமியற்றக் கட்டாயப்படுத்த நீதிமன்றங்களுக்கு அதிகாரம் அளிக்காது என்பதால் உச்ச நீதிமன்றம் மனுவைத் தள்ளுபடி செய்யும்.",
        wno_dict={
            "A": {"en": "Incorrect. Mandamus cannot be issued for non-justiciable Preamble.", "ta": "தவறு. நிலைநிறுத்த முடியாத முகவுரைக்கு பேராணை பிறப்பிக்க முடியாது."},
            "B": {"en": "Correct. Preamble is non-justiciable; cannot compel legislation.", "ta": "சரி. முகவுரை நிலைநிறுத்த முடியாதது; சட்டமாக்கத்தைக் கட்டாயப்படுத்த முடியாது."},
            "C": {"en": "Incorrect. Absurd option.", "ta": "தவறு. பொருத்தமற்ற விருப்பம்."},
            "D": {"en": "Incorrect. Election commission has no role in legislative mandamus.", "ta": "தவறு. தேர்தல் ஆணையத்திற்கு இதில் பங்கில்லை."}
        },
        tip_en="Writ of Mandamus CANNOT be issued to enforce Preamble goals directly.",
        tip_ta="முகவுரை இலக்குகளை நேரடியாக அமல்படுத்த கட்டளைப் பேராணை பிறப்பிக்க முடியாது.",
        rev_en="Preamble is non-justiciable; no writ lies solely for Preamble enforcement.",
        rev_ta="முகவுரை நிலைநிறுத்த முடியாதது; முகவுரை அமலாக்கத்திற்கு மட்டும் பேராணை முடியாது.",
        sources=["Preamble Notes Part 2"],
        bloom="Apply", est_sec=45, pyq_sim="High", tags=["Mandamus", "Non-Justiciable", "Article 32"]
    ))

    # Q23 - Case-law - Ans C
    qs.append(make_medium_q(
        q_id="PRE_M_023", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Medium", question_type="Case-law Based",
        q_en="How did the Supreme Court utilize the Preamble's concepts of 'Liberty' and 'Justice' in the landmark Maneka Gandhi Case (1978)?",
        q_ta="வரலாற்றுச் சிறப்புமிக்க மேனகா காந்தி வழக்கில் (1978) உச்ச நீதிமன்றம் முகவுரையின் 'சுதந்திரம்' மற்றும் 'நீதி' தத்துவங்களை எவ்வாறு பயன்படுத்தியது?",
        opts_en=[
            "To hold that passport impoundment requires no legal procedure.",
            "To abolish the right to travel abroad entirely.",
            "To expand Article 21 (Personal Liberty) by reading 'Procedure established by law' as requiring a procedure that is just, fair, and reasonable (Due Process).",
            "To declare Article 21 non-justiciable."
        ],
        opts_ta=[
            "பாஸ்போர்ட் பறிமுதல் செய்ய சட்டப்பூர்வ நடைமுறை தேவையில்லை எனக் கூற.",
            "வெளிநாடு செல்லும் உரிமையை முற்றிலும் ஒழிக்க.",
            "சட்டத்தால் நிறுவப்பட்ட நடைமுறை' என்பதை நீதி, நியாயமான மற்றும் ரீதியிலான நடைமுறையாக (சட்டத்தின் உரிய நடைமுறை) தேவைப்படுத்துவதாக ஓதி உறுப்பு 21 ஐ (தனிநபர் சுதந்திரம்) விரிவாக்க.",
            "உறுப்பு 21 ஐ நிலைநிறுத்த முடியாதது என அறிவிக்க."
        ],
        correct_ans="C",
        exp_en="In Maneka Gandhi (1978), SC drew upon Preamble's vision of Liberty and Justice to hold that 'procedure established by law' in Art 21 must be just, fair, and reasonable (incorporating American Due Process).",
        exp_ta="மேனகா காந்தி (1978) வழக்கில், உச்ச நீதிமன்றம் உறுப்பு 21 இல் உள்ள 'சட்டத்தால் நிறுவப்பட்ட நடைமுறை' என்பது நீதியான, நியாயமான மற்றும் ரீதியான நடைமுறையாக இருக்க வேண்டும் எனக் கூறி முகவுரையின் சுதந்திரம் மற்றும் நீதியைப் பயன்படுத்தியது.",
        wno_dict={
            "A": {"en": "Incorrect. Court required fair procedure.", "ta": "தவறு. நீதிமன்றம் நியாயமான நடைமுறையைக் கோரியது."},
            "B": {"en": "Incorrect. Travel abroad was held part of Personal Liberty under Art 21.", "ta": "தவறு. வெளிநாடு செல்லும் உரிமை உறுப்பு 21 இன் பகுதியாக அறிவிக்கப்பட்டது."},
            "C": {"en": "Correct. Expanded Art 21 procedure to be just, fair, and reasonable using Preamble ideals.", "ta": "சரி. உறுப்பு 21 நடைமுறையை நீதியான மற்றும் நியாயமானதாக விரிவாக்கியது."},
            "D": {"en": "Incorrect. Art 21 is a core justiciable FR.", "ta": "தவறு. உறுப்பு 21 ஒரு முக்கிய அடிப்படை உரிமை."}
        },
        tip_en="Maneka Gandhi (1978) used Preamble Liberty/Justice to read 'Just, Fair, Reasonable' procedure into Article 21.",
        tip_ta="மேனகா காந்தி (1978) உறுப்பு 21 இல் 'நீதியான, நியாயமான' நடைமுறையை இணைக்க முகவுரையைப் பயன்படுத்தியது.",
        rev_en="Maneka Gandhi 1978 = Preamble ideals expanded Article 21 scope.",
        rev_ta="மேனகா காந்தி 1978 = முகவுரை தத்துவங்கள் உறுப்பு 21 எல்லையை விரிவாக்கின.",
        sources=["Preamble Notes Part 2"],
        bloom="Understand", est_sec=45, pyq_sim="High", tags=["Maneka Gandhi Case", "Article 21", "Due Process"]
    ))

    # Q24 - Conceptual Distinction - Ans D
    qs.append(make_medium_q(
        q_id="PRE_M_024", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Medium", question_type="Conceptual Distinction",
        q_en="Which statement accurately contrasts the scope of 'Liberty' in the Preamble with 'Equality' in the Preamble?",
        q_ta="முகவுரையில் உள்ள 'சுதந்திரத்தின்' எல்லையை முகவுரையில் உள்ள 'சமத்துவத்துடன்' சரியாக வேறுபடுத்தும் கூற்று எது?",
        opts_en=[
            "Liberty applies only to economic rights, whereas Equality applies only to religious worship.",
            "Liberty is absolute without restrictions, whereas Equality applies only during war.",
            "Liberty is non-justiciable, whereas Equality is justiciable directly from Preamble.",
            "Liberty guarantees freedom of thought, expression, belief, faith, and worship; whereas Equality guarantees equality of status and opportunity to all citizens."
        ],
        opts_ta=[
            "சுதந்திரம் பொருளாதார உரிமைகளுக்கு மட்டுமே பொருந்தும்; ஆனால் சமத்துவம் மத வழிபாட்டிற்கு மட்டுமே பொருந்தும்.",
            "சுதந்திரம் கட்டுப்பாடுகளின்றி பூரணமானது; ஆனால் சமத்துவம் போர்க்காலத்தில் மட்டுமே பொருந்தும்.",
            "சுதந்திரம் நிலைநிறுத்த முடியாதது; ஆனால் சமத்துவம் முகவுரையிலிருந்து நேரடியாக நிலைநிறுத்தக்கூடியது.",
            "சுதந்திரம் சிந்தனை, வெளிப்பாடு, நம்பிக்கை, சமயம் மற்றும் வழிபாட்டுச் சுதந்திரத்தை உத்தரவாதம் செய்கிறது; ஆனால் சமத்துவம் அனைத்து குடிமக்களுக்கும் தகுதி மற்றும் வாய்ப்பு சமத்துவத்தை உத்தரவாதம் செய்கிறது."
        ],
        correct_ans="D",
        exp_en="Liberty encompasses 5 mental and spiritual freedoms (thought, expression, belief, faith, worship). Equality encompasses 2 dimensions (status and opportunity).",
        exp_ta="சுதந்திரம் 5 மன மற்றும் ஆன்மீக சுதந்திரங்களை உள்ளடக்கியது (சிந்தனை, வெளிப்பாடு, நம்பிக்கை, சமயம், வழிபாடு). சமத்துவம் 2 பரிமாணங்களை உள்ளடக்கியது (தகுதி மற்றும் வாய்ப்பு).",
        wno_dict={
            "A": {"en": "Incorrect. Misidentifies the domains of liberty and equality.", "ta": "தவறு. சுதந்திரம் மற்றும் சமத்துவ களங்களை தவறாக அடையாளம் காண்கிறது."},
            "B": {"en": "Incorrect. Liberty is qualified, not absolute.", "ta": "தவறு. சுதந்திரம் தகுதிவாய்ந்தது."},
            "C": {"en": "Incorrect. Both Preamble goals are non-justiciable.", "ta": "தவறு. இரு முகவுரை இலக்குகளும் நிலைநிறுத்த முடியாதவை."},
            "D": {"en": "Correct. Accurately maps the 5 Liberties and 2 Equalities specified in Preamble text.", "ta": "சரி. முகவுரையில் உள்ள 5 சுதந்திரங்களையும் 2 சமத்துவங்களையும் துல்லியமாகக் காட்டுகிறது."}
        },
        tip_en="Preamble specifies 5 Liberties (Thought, Expression, Belief, Faith, Worship) and 2 Equalities (Status, Opportunity).",
        tip_ta="முகவுரை 5 சுதந்திரங்களையும் (சிந்தனை, வெளிப்பாடு, நம்பிக்கை, சமயம், வழிபாடு) 2 சமத்துவங்களையும் (தகுதி, வாய்ப்பு) குறிப்பிடுகிறது.",
        rev_en="5 Liberties + 2 Equalities specified in Preamble.",
        rev_ta="முகவுரையில் 5 சுதந்திரங்கள் + 2 சமத்துவங்கள் குறிப்பிடப்பட்டுள்ளன.",
        sources=["Preamble Notes Part 1"],
        bloom="Understand", est_sec=45, pyq_sim="High", tags=["Liberty", "Equality", "Preamble Text"]
    ))

    # Q25 - Direct - Ans A
    qs.append(make_medium_q(
        q_id="PRE_M_025", subject="Polity", topic="Preamble of the Constitution of India",
        difficulty="Medium", question_type="Direct",
        q_en="In which year was the 42nd Constitutional Amendment Act passed and in which year did it come into force?",
        q_ta="42வது அரசியலமைப்பு திருத்தச் சட்டம் எந்த ஆண்டில் நிறைவேற்றப்பட்டது மற்றும் எந்த ஆண்டில் நடைமுறைக்கு வந்தது?",
        opts_en=[
            "Passed in 1976; Came into force in 1977 (3rd January)",
            "Passed in 1975; Came into force in 1976",
            "Passed in 1978; Came into force in 1979",
            "Passed in 1973; Came into force in 1974"
        ],
        opts_ta=[
            "1976 இல் நிறைவேற்றப்பட்டது; 1977 இல் (3 ஜனவரி) நடைமுறைக்கு வந்தது",
            "1975 இல் நிறைவேற்றப்பட்டது; 1976 இல் நடைமுறைக்கு வந்தது",
            "1978 இல் நிறைவேற்றப்பட்டது; 1979 இல் நடைமுறைக்கு வந்தது",
            "1973 இல் நிறைவேற்றப்பட்டது; 1974 இல் நடைமுறைக்கு வந்தது"
        ],
        correct_ans="A",
        exp_en="The 42nd Constitutional Amendment Act was enacted in 1976, but most of its provisions (including Preamble amendments) came into force on 3rd January 1977.",
        exp_ta="42வது அரசியலமைப்பு திருத்தச் சட்டம் 1976 இல் இயற்றப்பட்டது, ஆனால் அதன் பெரும்பான்மையான விதிகள் (முகவுரை திருத்தங்கள் உட்பட) 3 ஜனவரி 1977 அன்று நடைமுறைக்கு வந்தன.",
        wno_dict={
            "A": {"en": "Correct. Enactment year = 1976; Enforcement year = 1977.", "ta": "சரி. இயற்றப்பட்ட ஆண்டு = 1976; அமலான ஆண்டு = 1977."},
            "B": {"en": "Incorrect. Emergency declared in 1975, amendment passed in 1976.", "ta": "தவறு. திருத்தம் 1976 இல் நிறைவேற்றப்பட்டது."},
            "C": {"en": "Incorrect. 44th Amendment was 1978.", "ta": "தவறு. 44வது திருத்தம் 1978."},
            "D": {"en": "Incorrect. Kesavananda was 1973.", "ta": "தவறு. கேசவாநந்தா 1973."}
        },
        tip_en="TNPSC Trap: 42nd Amendment Act is dated 1976, but enforced on 3rd January 1977.",
        tip_ta="TNPSC பொறி: 42வது திருத்தச் சட்டம் 1976 எனக் குறிப்பிடப்படும், ஆனால் 3 ஜனவரி 1977 இல் அமலானது.",
        rev_en="42nd Amendment = Passed 1976, Enforced 3 Jan 1977.",
        rev_ta="42வது திருத்தம் = 1976 இல் நிறைவேற்றம், 3 ஜனவரி 1977 இல் அமல்.",
        sources=["Preamble Notes Part 1 & 2"],
        bloom="Remember", est_sec=30, pyq_sim="High", tags=["42nd Amendment", "Enactment vs Enforcement"]
    ))

    return qs
