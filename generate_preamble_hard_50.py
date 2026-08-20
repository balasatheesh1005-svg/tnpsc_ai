import json
import os

def build_question_item(
    q_id, q_type, q_en, q_ta,
    opt_a_en, opt_a_ta,
    opt_b_en, opt_b_ta,
    opt_c_en, opt_c_ta,
    opt_d_en, opt_d_ta,
    correct_ans,
    exp_en, exp_ta,
    why_a_en, why_a_ta,
    why_b_en, why_b_ta,
    why_c_en, why_c_ta,
    why_d_en, why_d_ta,
    tip_en, tip_ta,
    fact_en, fact_ta,
    tags, bloom="Analyze", time_sec=75
):
    options = [
        {"id": "A", "en": opt_a_en, "ta": opt_a_ta},
        {"id": "B", "en": opt_b_en, "ta": opt_b_ta},
        {"id": "C", "en": opt_c_en, "ta": opt_c_ta},
        {"id": "D", "en": opt_d_en, "ta": opt_d_ta}
    ]
    
    opts_en_list = [opt_a_en, opt_b_en, opt_c_en, opt_d_en]
    opts_ta_list = [opt_a_ta, opt_b_ta, opt_c_ta, opt_d_ta]
    
    return {
        "id": q_id,
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India",
        "difficulty": "Hard",
        "question_type": q_type,
        "question": {"en": q_en, "ta": q_ta},
        "options": options,
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
        "source_reference": ["Preamble Notes Part 1", "Preamble Notes Part 2", "M. Laxmikanth"],
        "bloom_level": bloom,
        "estimated_time_sec": time_sec,
        "pyq_similarity": "High",
        "tags": tags,
        # Flat compatibility fields
        "question_en": q_en,
        "question_ta": q_ta,
        "options_en": opts_en_list,
        "options_ta": opts_ta_list,
        "answer": correct_ans.lower(),
        "explanation_en": exp_en,
        "explanation_ta": exp_ta
    }

questions_list = []

# --- 1 TO 10 ---
questions_list.append(build_question_item(
    "PRE_H_001", "Advanced Conceptual",
    "The phrase 'We, the People of India' in the Preamble establishes the doctrine of 'Popular Sovereignty'. Which of the following is the most precise constitutional implication of this doctrine in the Indian legal framework?",
    "முகவுரையில் உள்ள 'இந்திய மக்களாகிய நாம்' என்ற தொடர் 'மக்களின் இறையாண்மை' கோட்பாட்டை நிறுவுகிறது. இந்திய சட்ட அமைப்பில் இக்கோட்பாட்டின் மிகத் துல்லியமான அரசியலமைப்பு விளைவு எது?",
    "The ultimate source of constitutional authority resides in the collective political sovereignty of the people, making the Constitution supreme over all organs created by it.",
    "அரசியலமைப்பு அதிகாரத்தின் இறுதி மூலம் மக்களின் கூட்டு அரசியல் இறையாண்மையில் உள்ளது; இதனால் அரசியலமைப்பு அது உருவாக்கிய அனைத்து உறுப்புகளை விடவும் மேலானது.",
    "Parliament possesses absolute legal sovereignty, permitting it to alter any provision of the Constitution without judicial interference.",
    "பாராளுமன்றம் முழுமையான சட்ட இறையாண்மையைக் கொண்டுள்ளது; இதனால் நீதித்துறை தலையீடின்றி அரசியலமைப்பின் எந்த விதியையும் மாற்ற அனுமதிக்கிறது.",
    "The legal validity of the Constitution is derived entirely from the Indian Independence Act, 1947 passed by the British Parliament.",
    "அரசியலமைப்பின் சட்டபூர்வ செல்லுபடியாகும் தன்மை முற்றிலும் பிரிட்டிஷ் பாராளுமன்றத்தால் நிறைவேற்றப்பட்ட 1947 இந்திய சுதந்திரச் சட்டத்திலிருந்து பெறப்பட்டது.",
    "Laws enacted by Parliament automatically supersede constitutional provisions if supported by a two-thirds referendum of voters.",
    "வாக்காளர்களின் மூன்றில் இரண்டு பங்கு பொதுவாக்கெடுப்பு ஆதரித்தால், பாராளுமன்றத்தால் இயற்றப்பட்ட சட்டங்கள் தானாகவே அரசியலமைப்பு விதிகளை விட மேலோங்கும்.",
    "A",
    "Popular Sovereignty signifies that the Constitution derives its authority, legitimacy, and sanction from the people of India. Consequently, the Constitution—not Parliament or the Executive—is the supreme law of the land (Constitutional Supremacy), and all organs function within its limits.",
    "மக்களின் இறையாண்மை என்பது அரசியலமைப்பு தனது அதிகாரம், சட்டபூர்வத்தன்மை மற்றும் அனுமதியை இந்திய மக்களிடமிருந்தே பெறுகிறது என்பதைக் குறிக்கிறது. இதன் விளைவாக, நாடாளுமன்றமோ அல்லது நிர்வாகமோ அல்ல, அரசியலமைப்பே நாட்டின் உயர்ந்த சட்டமாகும் (அரசியலமைப்பு மேலாதிக்கம்).",
    "Correct. Popular Sovereignty grounds Constitutional Supremacy over all three organs of State.", "சரி. மக்களின் இறையாண்மை அரசின் மூன்று உறுப்புகளையும் விட அரசியலமைப்பு மேலாதிக்கத்தை நிறுவுகிறது.",
    "Incorrect. India has Constitutional Supremacy, not British-style Parliamentary Sovereignty.", "தவறு. இந்தியாவில் அரசியலமைப்பு மேலாதிக்கம் உள்ளது, பிரிட்டிஷ் பாணி பாராளுமன்ற இறையாண்மை இல்லை.",
    "Incorrect. The Constituent Assembly repealed the Indian Independence Act 1947 under Art 395; authority derives from the people.", "தவறு. அரசியலமைப்புச் சபை 1947 இந்திய சுதந்திரச் சட்டத்தை உறுப்பு 395 இன் கீழ் ரத்து செய்தது; அதிகாரம் மக்களிடமிருந்தே பெறப்படுகிறது.",
    "Incorrect. The Indian Constitution does not provide for national referendums to override constitutional provisions.", "தவறு. இந்திய அரசியலமைப்பு விதிகளை மேலோங்குவதற்கு தேசிய பொதுவாக்கெடுப்புக்கு வழிகோலவில்லை.",
    "Popular Sovereignty = Source of authority is 'The People'. It leads to Constitutional Supremacy (NOT Parliamentary Supremacy).",
    "மக்களின் இறையாண்மை = அதிகாரத்தின் மூலம் 'மக்களே'. இது அரசியலமைப்பு மேலாதிக்கத்திற்கு வழிவகுக்கிறது (பாராளுமன்ற மேலாதிக்கம் அல்ல).",
    "Art 395 of the Constitution repealed the Indian Independence Act, 1947 and the Government of India Act, 1935, cementing popular sovereignty.",
    "அரசியலமைப்பின் உறுப்பு 395 இந்திய சுதந்திரச் சட்டம் 1947 மற்றும் இந்திய அரசுச் சட்டம் 1935 ஆகியவற்றை ரத்து செய்து மக்களின் இறையாண்மையை உறுதிப்படுத்தியது.",
    ["Preamble", "Popular Sovereignty", "We the People", "Constitutional Supremacy"]
))

questions_list.append(build_question_item(
    "PRE_H_002", "Advanced Conceptual",
    "Regarding the term 'Sovereign' in the Preamble, which of the following statements correctly reconciles India's membership in international bodies (like the Commonwealth or United Nations) with its constitutional sovereignty?",
    "முகவுரையில் உள்ள 'இறையாண்மை' என்ற சொல் தொடர்பாக, சர்வதேச அமைப்புகளில் (காமன்வெல்த் அல்லது ஐக்கிய நாடுகள் சபை போன்றவை) இந்தியாவின் உறுப்பினர்தன்மையை அதன் அரசியலமைப்பு இறையாண்மையுடன் சரியாக ஒப்பிட்டு சரிபார்க்கும் கூற்று எது?",
    "India surrendered a portion of its external sovereignty to the British Crown upon joining the Commonwealth in 1949.",
    "1949 இல் காமன்வெல்த்தில் சேர்ந்ததன் மூலம் இந்தியா தனது வெளி இறையாண்மையின் ஒரு பகுதியை பிரிட்டிஷ் மகுடத்திடம் ஒப்படைத்தது.",
    "Membership in international bodies is a voluntary extra-constitutional association that does not restrict India's supreme legal authority to legislate or govern internally and externally.",
    "சர்வதேச அமைப்புகளில் உறுப்பினராக இருப்பது ஒரு தன்னார்வ அரசியலமைப்புக்கு அப்பாற்பட்ட தொடர்பாகும்; இது உள்நாட்டிலும் வெளிநாட்டிலும் சட்டமியற்றவோ அல்லது நிர்வகிக்கவோ இந்தியாவின் உயர்ந்த சட்ட அதிகாரத்தைக் கட்டுப்படுத்தாது.",
    "UN Security Council resolutions automatically repeal inconsistent Indian Parliamentary statutes without requiring domestic legislation.",
    "ஐநா பாதுகாப்பு கவுன்சில் தீர்மானங்கள் உள்நாட்டு சட்டங்கள் ஏதுமின்றி முரண்பாடான இந்திய நாடாளுமன்ற சட்டங்களை தானாகவே ரத்து செய்கின்றன.",
    "Sovereignty requires complete political isolation, rendering any binding international treaty unconstitutional per se.",
    "இறையாண்மைக்கு முழுமையான அரசியல் தனிமைப்படுத்தல் தேவைப்படுகிறது; இதனால் பிணைப்புறுத்தும் எந்தவொரு சர்வதேச ஒப்பந்தமும் அரசியலமைப்புக்கு முரணானது.",
    "B",
    "India is a sovereign state—it is neither a dependency nor a dominion of any other nation. Although India accepted the King as Head of the Commonwealth in 1949, this declaration was a voluntary agreement outside the Constitution and does not impair India's full internal and external sovereignty.",
    "இந்தியா ஒரு இறையாண்மையுள்ள அரசு - அது வேறு எந்த நாட்டின் கட்டுப்பாட்டிலோ அல்லது டொமினியனாகவோ இல்லை. 1949 இல் காமன்வெல்த்தின் தலைவராக மன்னரை இந்தியா ஏற்றுக்கொண்ட போதிலும், இந்த அறிவிப்பு அரசியலமைப்புக்கு அப்பாற்பட்ட தன்னார்வ ஒப்பந்தமாகும்; இது இந்தியாவின் முழுமையான உள் மற்றும் வெளி இறையாண்மையைப் பாதிக்காது.",
    "Incorrect. India did not surrender any sovereignty; the Crown is merely a symbolic head of the association.", "தவறு. இந்தியா எந்த இறையாண்மையையும் ஒப்படைக்கவில்லை; மன்னர் காமன்வெல்த்தின் குறியீட்டுத் தலைவர் மட்டுமே.",
    "Correct. Commonwealth/UN membership is voluntary and does not legally curtail state sovereignty.", "சரி. காமன்வெல்த்/ஐநா உறுப்பினர்தன்மை தன்னார்வமானது, நாட்டின் இறையாண்மையை சட்டப்பூர்வமாக சுருக்காது.",
    "Incorrect. International treaties/resolutions require domestic enabling legislation under Article 253 to be enforceable in Indian courts.", "தவறு. சர்வதேச ஒப்பந்தங்கள் இந்திய நீதிமன்றங்களில் அமல்படுத்தப்பட உறுப்பு 253 இன் கீழ் உள்நாட்டுச் சட்டம் தேவை.",
    "Incorrect. Sovereignty includes the positive power to enter treaties and international agreements voluntarily.", "தவறு. இறையாண்மை என்பது தன்னார்வமாக ஒப்பந்தங்களை மேற்கொள்ளும் நேர்மறை அதிகாரத்தையும் உள்ளடக்கியது.",
    "Commonwealth membership (1949) does NOT affect Indian Sovereignty. Being sovereign means India can acquire foreign territory or cede territory to a foreign state.",
    "காமன்வெல்த் உறுப்பினர்தன்மை (1949) இந்திய இறையாண்மையைப் பாதிக்காது. இறையாண்மை என்பது அந்நிய நிலப்பரப்பைக் கையகப்படுத்த அல்லது விட்டுக் கொடுக்க அதிகாரமளிக்கிறது.",
    "As a sovereign state, India can either acquire a foreign territory or cede a part of its territory in favour of a foreign state.",
    "ஒரு இறையாண்மையுள்ள அரசாக, இந்தியா ஒரு அயல்நாட்டு நிலப்பரப்பைக் கையகப்படுத்தலாம் அல்லது தனது நிலப்பரப்பின் ஒரு பகுதியை அயல்நாட்டிற்கு விட்டுக் கொடுக்கலாம்.",
    ["Preamble", "Sovereign", "Commonwealth", "External Sovereignty"]
))

questions_list.append(build_question_item(
    "PRE_H_003", "Advanced Conceptual",
    "The Preamble envisions a 'Socialist' state. How does Indian 'Democratic Socialism' fundamentally differ from classic 'State/Marxist Socialism'?",
    "முகவுரை ஒரு 'சமதர்ம' அரசை முன்மொழிகிறது. இந்திய 'ஜனநாயக சோசலிசம்' பாரம்பரிய 'அரசு/மார்க்சிய சோசலிசத்திலிருந்து' எவ்வாறு அடிப்படையில் வேறுபடுகிறது?",
    "Indian Democratic Socialism favors a complete abolition of private property and total state monopoly over all means of production.",
    "இந்திய ஜனநாயக சோசலிசம் தனியார் சொத்துரிமையை முற்றிலும் ஒழிப்பதையும் உற்பத்தி சாதனங்கள் அனைத்தின் மீதும் முழுமையான அரசு ஏகபோகத்தையும் ஆதரிக்கிறது.",
    "Marxist Socialism emphasizes parliamentary democratic means, whereas Democratic Socialism relies on violent proletarian revolution.",
    "மார்க்சிய சோசலிசம் பாராளுமன்ற ஜனநாயக வழிகளை வலியுறுத்துகிறது, ஆனால் ஜனநாயக சோசலிசம் வன்முறை பாட்டாளி வர்க்கப் புரட்சியை நம்பியுள்ளது.",
    "Indian Democratic Socialism envisions a mixed economy where public and private sectors co-exist side-by-side to end poverty, ignorance, and inequality.",
    "இந்திய ஜனநாயக சோசலிசம் வறுமை, அறியாமை மற்றும் சமத்துவமின்மையை ஒழிக்க பொது மற்றும் தனியார் துறைகள் அருகருகே இணைந்து செயல்படும் கலப்பு பொருளாதாரத்தை முன்மொழிகிறது.",
    "Democratic Socialism applies exclusively to agrarian land reforms, leaving industrial sectors entirely unregulated.",
    "ஜனநாயக சோசலிசம் வேளாண் நில சீர்திருத்தங்களுக்கு மட்டுமே பொருந்தும், தொழில்துறை துறைகளை முற்றிலும் ஒழுங்குபடுத்தாமல் விடுகிறது.",
    "C",
    "Indian socialism is 'democratic socialism' and not 'state socialism' (Marxist socialism). Democratic socialism holds faith in a 'mixed economy' where both public and private sectors co-exist. As the Supreme Court observed, democratic socialism aims to end poverty, ignorance, disease, and inequality of opportunity, leaning heavily towards Gandhian socialism.",
    "இந்திய சோசலிசம் 'ஜனநாயக சோசலிசம்' ஆகும், 'அரசு சோசலிசம்' (மார்க்சிய சோசலிசம்) அல்ல. ஜனநாயக சோசலிசம் பொது மற்றும் தனியார் துறைகள் இரண்டும் இணைந்து வாழும் 'கலப்பு பொருளாதாரம்' மீது நம்பிக்கை கொண்டுள்ளது. இது காந்திய சோசலிசத்தை நோக்கி அதிக சாய்வைக் கொண்டுள்ளது.",
    "Incorrect. Abolition of private property and total state monopoly characterize State/Marxist socialism, not Indian mixed economy socialism.", "தவறு. தனியார் சொத்து ஒழிப்பு மற்றும் முழு அரசு ஏகபோகம் அரசு/மார்க்சிய சோசலிசத்தின் பண்புகளாகும், இந்திய கலப்பு பொருளாதாரத்தின் பண்புகள் அல்ல.",
    "Incorrect. Reverses the two concepts: Democratic Socialism uses parliamentary peaceful means, while Marxist socialism originally relied on class struggle/revolution.", "தவறு. இரு கருத்துக்களையும் தலைகீழாக மாற்றுகிறது.",
    "Correct. Democratic socialism believes in a mixed economy co-existing with private enterprise.", "சரி. ஜனநாயக சோசலிசம் தனியார் நிறுவனங்களுடன் இணைந்த கலப்பு பொருளாதாரத்தை நம்புகிறது.",
    "Incorrect. Democratic socialism applies across economic sectors through welfare planning and directive principles.", "தவறு. ஜனநாயக சோசலிசம் நலத்திட்டமிடல் மற்றும் வழிகாட்டு நெறிமுறைகள் மூலம் அனைத்து பொருளாதாரத் துறைகளுக்கும் பொருந்தும்.",
    "Indian Socialism = Democratic Socialism = Mixed Economy (Public + Private). Blends Marxism & Gandhian socialism, leaning heavily towards Gandhian socialism.",
    "இந்திய சோசலிசம் = ஜனநாயக சோசலிசம் = கலப்பு பொருளாதாரம் (பொது + தனியார்). மார்க்சியம் மற்றும் காந்திய சோசலிசத்தின் கலவை, காந்திய சோசலிசத்தை நோக்கி அதிக சாய்வு கொண்டது.",
    "Supreme Court in Excel Wear (1978) affirmed that addition of 'Socialist' did not imply total state ownership or nationalization of private businesses.",
    "எக்செல் வேர் வழக்கின் (1978) உச்ச நீதிமன்றத் தீர்ப்பு 'சமதர்ம' என்ற சொல் சேர்க்கப்பட்டது தனியார் வணிகங்களை முழுமையாக அரசுடைமையாக்குவதைக் குறிக்காது என்று உறுதிப்படுத்தியது.",
    ["Preamble", "Socialist", "Democratic Socialism", "Mixed Economy"]
))

questions_list.append(build_question_item(
    "PRE_H_004", "Advanced Conceptual",
    "Indian constitutional secularism is characterized as 'Positive Secularism'. Which of the following correctly highlights its distinction from the Western model of secularism?",
    "இந்திய அரசியலமைப்பு மதச்சார்பின்மை 'நேர்மறை மதச்சார்பின்மை' என விவரிக்கப்படுகிறது. மேற்கத்திய மதச்சார்பின்மை மாதிரியிலிருந்து இதன் வேறுபாட்டைச் சரியாக சுட்டிக்காட்டும் கூற்று எது?",
    "Indian secularism establishes Hinduism as the official state religion while granting minority tolerance, whereas Western secularism is completely atheistic.",
    "இந்திய மதச்சார்பின்மை சிறுபான்மையினருக்கு சகிப்புத்தன்மையை அளிக்கும் அதே வேளையில் இந்து மதத்தை உத்தியோகபூர்வ அரசு மதமாக நிறுவுகிறது; ஆனால் மேற்கத்திய மதச்சார்பின்மை முற்றிலும் நாத்திகமானது.",
    "Western secularism allows the State to financial fund dominant religious institutions, whereas Indian secularism prohibits any citizen from practicing religion publicly.",
    "மேற்கத்திய மதச்சார்பின்மை ஆதிக்கம் செலுத்தும் மத நிறுவனங்களுக்கு அரசு நிதி உதவி செய்ய அனுமதிக்கிறது; ஆனால் இந்திய மதச்சார்பின்மை எந்தவொரு குடிமகனும் பகிரங்கமாக மதத்தைப் பின்பற்றுவதைத் தடுக்கிறது.",
    "Indian positive secularism was created for the first time by the 42nd Amendment Act of 1976 and had no constitutional existence prior to that.",
    "இந்திய நேர்மறை மதச்சார்பின்மை 1976 இன் 42வது திருத்தச் சட்டத்தால் முதன்முறையாக உருவாக்கப்பட்டது, அதற்கு முன் அரசியலமைப்பு ரீதியாக அதற்கு अस्तित्वம் இல்லை.",
    "Western secularism requires strict wall of separation and mutual exclusion between State and religion, whereas Indian positive secularism accords equal respect and equal protection to all religions (Sarva Dharma Sambhava).",
    "மேற்கத்திய மதச்சார்பின்மை அரசுக்கும் மதத்திற்கும் இடையே கடுமையான பிரிவினையையும் பரஸ்பர விலக்கலையும் கோருகிறது; ஆனால் இந்திய நேர்மறை மதச்சார்பின்மை அனைத்து மதங்களுக்கும் சமமான மரியாதையையும் சமமான பாதுகாப்பையும் அளிக்கிறது (சர்வ தர்ம சம்பவ).",
    "D",
    "The Indian Constitution embodies the positive concept of secularism: all religions in our country (irrespective of their strength) have the same status and support from the State (Sarva Dharma Sambhava). In contrast, Western secularism implies a rigid, negative separation between the State and religion.",
    "இந்திய அரசியலமைப்பு மதச்சார்பின்மையின் நேர்மறையான கருத்தை உள்ளடக்கியுள்ளது: நம் நாட்டில் உள்ள அனைத்து மதங்களும் (அவற்றின் பலத்தைப் பொருட்படுத்தாமல்) அரசுக்கு முன் ஒரே மாதிரியான தகுதியையும் ஆதரவையும் கொண்டுள்ளன (சர்வ தர்ம சம்பவ). மாறாக, மேற்கத்திய மதச்சார்பின்மை அரசுக்கும் மதத்திற்கும் இடையே கடுமையான எதிர்மறைப் பிரிவினையைக் குறிக்கிறது.",
    "Incorrect. India has NO official state religion; all religions are treated equally under the Constitution.", "தவறு. இந்தியாவுக்கு உத்தியோகபூர்வ அரசு மதம் எதுவுமில்லை; அரசியலமைப்பின் கீழ் அனைத்து மதங்களும் சமமாக நடத்தப்படுகின்றன.",
    "Incorrect. Article 25 guarantees public freedom of conscience and religious practice; Article 27 restricts religious taxation.", "தவறு. உறுப்பு 25 பகிரங்க மனசாட்சி மற்றும் மதப் பழக்க சுதந்திரத்திற்கு உத்தரவாதம் அளிக்கிறது.",
    "Incorrect. Articles 25-28 already embodied secular principles since 1950; 42nd Amendment only rendered it explicit.", "தவறு. உறுப்புகள் 25-28 1950 முதல் மதச்சார்பற்றக் கொள்கைகளை உள்ளடக்கியிருந்தன; 42வது திருத்தம் அதை வெளிப்படையாக்கியது மட்டுமே.",
    "Correct. Positive Secularism = Equal respect and protection for all religions (Articles 25-28).", "சரி. நேர்மறை மதச்சார்பின்மை = அனைத்து மதங்களுக்கும் சமமான மரியாதை மற்றும் பாதுகாப்பு (உறுப்புகள் 25-28).",
    "Indian Secularism = Positive concept (Sarva Dharma Sambhava). Western Secularism = Negative concept (Rigid wall of separation).",
    "இந்திய மதச்சார்பின்மை = நேர்மறைக் கருத்து (சர்வ தர்ம சம்பவ). மேற்கத்திய மதச்சார்பின்மை = எதிர்மறைக் கருத்து (கடுமையான தடுப்புச் சுவர்).",
    "In S.R. Bommai case (1994), the Supreme Court held that Secularism is a Basic Feature of the Indian Constitution.",
    "எஸ்.ஆர். பொம்மை வழக்கில் (1994), மதச்சார்பின்மை இந்திய அரசியலமைப்பின் அடிப்படை கட்டமைப்பு என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
    ["Preamble", "Secular", "Positive Secularism", "Sarva Dharma Sambhava"]
))

# Save current file to check
with open("data/questions/polity/preamble_hard.json", "w", encoding="utf-8") as f:
    json.dump(questions_list, f, ensure_ascii=False, indent=2)

print("Sample test batch created successfully.")
