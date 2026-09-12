# -*- coding: utf-8 -*-
"""
Emergency Provisions Grand Test - Batch 2 (Questions 26 to 50)
Prefix: EP_GT_
Keys: A: 6, B: 7, C: 6, D: 6 (Total: 25)
"""

from ep_mcq_helper import make_ep_q

PREFIX = "EP_GT_"

def get_gt_batch2():
    qs = []

    # 026 - Key B
    qs.append(make_ep_q(
        PREFIX, 26, "Hard", "Judicial Precedent", "S.R. Bommai Landmark Ratio",
        "Which of the following was NOT laid down by the Supreme Court in the landmark S.R. Bommai v. Union of India case (1994)?",
        "எஸ்.ஆர். பொம்மை எதிர் மத்திய அரசு (1994) மைல்கல் வழக்கில் உச்ச நீதிமன்றத்தால் வகுக்கப்படாத விதி எது?",
        "Presidential proclamation under Article 356 is subject to judicial review", "சரத்து 356-ன் கீழான குடியரசுத் தலைவர் பிரகடனம் நீதி மறுஆய்வுக்கு உட்பட்டது",
        "The President can dissolve the Legislative Assembly immediately upon issuing the proclamation without waiting for parliamentary approval", "பாராளுமன்ற ஒப்புதலுக்காகக் காத்திருக்காமல் பிரகடனம் வெளியிட்ட உடனேயே குடியரசுத் தலைவர் சட்டமன்றத்தைக் கலைத்துவிடலாம்",
        "Secularism is a basic feature of the Constitution, and anti-secular policies warrant Article 356", "மதச்சார்பின்மை என்பது அரசியலமைப்பின் அடிப்படைக் கட்டமைப்பு, மதச்சார்பற்ற கொள்கைகளுக்கு எதிரான செயல் சரத்து 356-ஐத் தூண்டும்",
        "The floor of the Assembly is the only place to test the majority of the ministry", "சட்டமன்ற அவையே அமைச்சரவையின் பெரும்பான்மையைச் சோதிப்பதற்கான ஒரே இடமாகும்",
        "B",
        "In the Bommai case, the Supreme Court specifically held that the Assembly should NOT be dissolved until Parliament approves the proclamation under Article 356; it should only be kept in suspended animation initially.",
        "பொம்மை வழக்கில் உச்ச நீதிமன்றம், பாராளுமன்றம் சரத்து 356-க்கு ஒப்புதல் அளிக்கும் வரை சட்டமன்றத்தைக் கலைக்கக் கூடாது என்றும், ஆரம்பத்தில் அதை இடைநிறுத்தப்பட்ட நிலையில் மட்டுமே வைக்க வேண்டும் என்றும் தெளிவாகத் தீர்ப்பளித்தது.",
        "Option A was expressly affirmed in Bommai.", "விருப்பம் A பொம்மை வழக்கில் வெளிப்படையாக உறுதிப்படுத்தப்பட்டது.",
        "Option B is correct as the FALSE statement; Bommai prohibited premature dissolution.", "விருப்பம் B தவறான கூற்றாக இருப்பதால் சரியான விடை; அவசரக் கலைப்பை பொம்மை தடை செய்தது.",
        "Option C was a core holding regarding the dismissals in MP, Rajasthan, and HP.", "விருப்பம் C மதச்சார்பின்மை குறித்த முக்கியத் தீர்ப்பாகும்.",
        "Option D is the celebrated 'floor test' rule established in Bommai.", "விருப்பம் D பொம்மை வழக்கில் நிறுவப்பட்ட புகழ்பெற்ற 'நம்பிக்கை வாக்கெடுப்பு' விதியாகும்.",
        "TNPSC Landmark Ratio: In S.R. Bommai (1994), Supreme Court held that Legislative Assembly CANNOT be dissolved before Parliamentary approval.",
        "TNPSC மைல்கல் தீர்ப்பு: எஸ்.ஆர். பொம்மை (1994) வழக்கில், பாராளுமன்ற ஒப்புதலுக்கு முன்பாக சட்டமன்றத்தைக் கலைக்க முடியாது என உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
        "Prior to Bommai, state assemblies were routinely dissolved on the very day Article 356 was proclaimed.",
        "பொம்மை வழக்கிற்கு முன், சரத்து 356 அறிவிக்கப்பட்ட அன்றே சட்டமன்றங்கள் கலைக்கப்படுவது வழக்கமாக இருந்தது."
    ))

    # 027 - Key A
    qs.append(make_ep_q(
        PREFIX, 27, "Hard", "Constitutional Procedure", "Status of Assembly pending Parliamentary Approval",
        "According to constitutional principles established post-Bommai, what should be the status of the State Legislative Assembly before Parliament approves the Article 356 proclamation?",
        "பொம்மை வழக்கிற்குப் பிந்தைய அரசியலமைப்பு கோட்பாடுகளின்படி, பாராளுமன்றம் சரத்து 356 பிரகடனத்திற்கு ஒப்புதல் அளிக்கும் முன் மாநில சட்டமன்றத்தின் நிலை என்னவாக இருக்க வேண்டும்?",
        "It must be kept in suspended animation only, and cannot be dissolved", "அது இடைநிறுத்தப்பட்ட நிலையில் (suspended animation) மட்டுமே வைக்கப்பட வேண்டும், கலைக்கப்படக் கூடாது",
        "It is dissolved automatically by operation of law", "அது சட்டத்தின் செயல்பாட்டால் தானாகவே கலைக்கப்படுகிறது",
        "It continues its legislative sessions under the direction of the Governor", "ஆளுநரின் வழிகாட்டுதலின் கீழ் அது தனது சட்டமன்றக் கூட்டங்களைத் தொடர்ந்து நடத்துகிறது",
        "It is temporarily merged with the Parliament of India", "அது தற்காலிகமாக இந்தியப் பாராளுமன்றத்துடன் இணைக்கப்படுகிறது",
        "A",
        "Following the S.R. Bommai judgment, the Legislative Assembly can only be placed under suspended animation until both Houses of Parliament approve the proclamation. Dissolution can happen only AFTER parliamentary approval.",
        "எஸ்.ஆர். பொம்மை தீர்ப்பைத் தொடர்ந்து, பாராளுமன்றத்தின் இரு அவைகளும் ஒப்புதல் அளிக்கும் வரை சட்டமன்றத்தை இடைநிறுத்த மட்டுமே முடியும். பாராளுமன்ற ஒப்புதலுக்குப் பின்னரே கலைப்பு சாத்தியமாகும்.",
        "Option A is correct; suspended animation is the mandatory pre-approval status.", "விருப்பம் A சரியானது; ஒப்புதலுக்கு முந்தைய கட்டாய நிலை இடைநிறுத்தமே ஆகும்.",
        "Option B describes the erroneous pre-1994 practice.", "விருப்பம் B 1994-க்கு முந்தைய தவறான நடைமுறையைக் குறிக்கிறது.",
        "Option C is wrong because the assembly cannot function while suspended.", "விருப்பம் C தவறு, ஏனெனில் இடைநிறுத்தத்தின் போது சட்டமன்றம் இயங்க முடியாது.",
        "Option D is constitutional nonsense.", "விருப்பம் D அரசியலமைப்பில் இல்லாதது.",
        "Bommai Safeguard: If Parliament fails to approve the proclamation within 2 months, the suspended assembly and dismissed government automatically revive!",
        "பொம்மை பாதுகாப்பு: பாராளுமன்றம் 2 மாதங்களில் ஒப்புதல் அளிக்காவிட்டால், இடைநிறுத்தப்பட்ட சட்டமன்றமும் கலைக்கப்பட்ட அரசும் தானாகவே மீண்டும் உயிர்பெறும்!",
        "This safeguard eliminated the fait accompli trick where assemblies were dissolved to make court relief meaningless.",
        "நீதிமன்ற நிவாரணத்தை அர்த்தமற்றதாக்குவதற்காக சட்டமன்றங்களைக் கலைத்துவிடும் தந்திரத்தை இந்தப் பாதுகாப்பு முறியடித்தது."
    ))

    # 028 - Key C
    qs.append(make_ep_q(
        PREFIX, 28, "Hard", "Legislative Powers", "Article 357 Lawmaking Powers",
        "Under Article 357(1)(a), when the powers of the State Legislature are declared exercisable by Parliament under Article 356, what can Parliament do?",
        "சரத்து 357(1)(a)-ன் கீழ், சரத்து 356-ல் மாநில சட்டமன்ற அதிகாரங்களைப் பாராளுமன்றம் செயல்படுத்தலாம் என அறிவிக்கப்படும் போது, பாராளுமன்றம் என்ன செய்ய முடியும்?",
        "Direct the Governor to summon a constitutional convention", "அரசியலமைப்பு மாநாட்டைக் கூட்டுமாறு ஆளுநருக்கு உத்தரவிடலாம்",
        "Transfer all State List subjects to the Union List permanently", "மாநிலப் பட்டியலின் அனைத்து விவகாரங்களையும் நிரந்தரமாக மத்தியப் பட்டியலுக்கு மாற்றலாம்",
        "Confer on the President the power of the State Legislature to make laws, and authorize him to delegate such power", "சட்டங்களை இயற்றுவதற்கான மாநில சட்டமன்றத்தின் அதிகாரத்தைக் குடியரசுத் தலைவருக்கு வழங்கலாம், மேலும் அந்த அதிகாரத்தைப் பிறருக்கு வழங்கவும் குடியரசுத் தலைவரை அனுமதிக்கலாம்",
        "Abolish the Legislative Assembly permanently and make the state a Union Territory", "மாநில சட்டமன்றத்தை நிரந்தரமாக ரத்து செய்துவிட்டு மாநிலத்தை யூனியன் பிரதேசமாக மாற்றலாம்",
        "C",
        "Under Article 357(1)(a), Parliament is competent to confer on the President the power of the Legislature of the State to make laws, and to authorize the President to delegate, subject to specified conditions, the power so conferred to any other authority.",
        "சரத்து 357(1)(a)-ன் கீழ், சட்டங்களை இயற்றுவதற்கான மாநில சட்டமன்றத்தின் அதிகாரத்தைக் குடியரசுத் தலைவருக்கு வழங்கவும், குறிப்பிட்ட நிபந்தனைகளுக்கு உட்பட்டு அந்த அதிகாரத்தை வேறு எந்தவொரு அதிகார அமைப்பிற்கும் வழங்குமாறு குடியரசுத் தலைவரை அனுமதிக்கவும் பாராளுமன்றத்திற்கு அதிகாரம் உண்டு.",
        "Option A is incorrect.", "விருப்பம் A தவறானது.",
        "Option B is false; subjects cannot be permanently transferred.", "விருப்பம் B தவறு; விவகாரங்களை நிரந்தரமாக மாற்ற முடியாது.",
        "Option C is correct; Parliament delegates state lawmaking power to the President.", "விருப்பம் C சரியானது; பாராளுமன்றம் மாநில சட்டமியற்றும் அதிகாரத்தைக் குடியரசுத் தலைவருக்கு வழங்குகிறது.",
        "Option D requires a separate constitutional amendment / reorganization act.", "விருப்பம் D தனி மறுசீரமைப்புச் சட்டத்தைக் கோருகிறது.",
        "Article 357 Delegation: Parliament confers state lawmaking power on President -> President enacts 'President's Acts'.",
        "சரத்து 357 அதிகாரப் பகிர்வு: பாராளுமன்றம் மாநில சட்டமன்ற அதிகாரத்தைக் குடியரசுத் தலைவருக்கு வழங்குகிறது -> குடியரசுத் தலைவர் 'குடியரசுத் தலைவர் சட்டங்களை' இயற்றுகிறார்.",
        "The President consults members of Parliament representing that state before enacting such legislation.",
        "அத்தகைய சட்டங்களை இயற்றுவதற்கு முன், அந்த மாநிலத்தைப் பிரதிநிதித்துவப்படுத்தும் பாராளுமன்ற உறுப்பினர்களுடன் குடியரசுத் தலைவர் கலந்தாலோசிக்கிறார்."
    ))

    # 029 - Key D
    qs.append(make_ep_q(
        PREFIX, 29, "Hard", "Constitutional Amendment", "Article 357(2) Post-44th Amendment Validity",
        "Under Article 357(2) as amended by the 44th Constitutional Amendment Act, 1978, what is the fate of laws made by Parliament or the President for a state under President's Rule after the proclamation ceases?",
        "1978-ன் 44-வது திருத்தச் சட்டத்தால் திருத்தப்பட்ட சரத்து 357(2)-ன் கீழ், குடியரசுத் தலைவர் ஆட்சி முடிவுக்கு வந்த பிறகு, பாராளுமன்றம் அல்லது குடியரசுத் தலைவரால் இயற்றப்பட்ட சட்டங்களின் நிலை என்ன?",
        "They cease to have effect immediately upon revocation of the proclamation", "பிரகடனம் ரத்து செய்யப்பட்ட உடனேயே அவை செயல்படுவதை நிறுத்திவிடுகின்றன",
        "They lapse automatically after one year unless re-enacted by the State Legislature", "மாநில சட்டமன்றத்தால் மீண்டும் இயற்றப்படாவிட்டால் அவை ஓராண்டிற்குப் பிறகு தானாகவே காலாவதியாகிவிடும்",
        "They lapse after six months like laws under Article 250", "சரத்து 250-ன் கீழான சட்டங்களைப் போல ஆறு மாதங்களுக்குப் பிறகு அவை காலாவதியாகிவிடும்",
        "They continue in force until altered, repealed, or amended by a competent Legislature of the State", "மாநிலத்தின் தகுதிவாய்ந்த சட்டமன்றத்தால் மாற்றப்படும் வரை, ரத்து செய்யப்படும் வரை அல்லது திருத்தப்படும் வரை அவை தொடர்ந்து நடைமுறையில் இருக்கும்",
        "D",
        "Under Article 357(2), as amended by the 44th CAA 1978, any law made in exercise of the power of the State Legislature by Parliament or the President shall continue in force after the proclamation has ceased until altered or repealed or amended by a competent Legislature or other authority. (Prior to 1978, such laws expired one year after the emergency ceased).",
        "1978-ன் 44-வது திருத்தச் சட்டத்தால் திருத்தப்பட்ட சரத்து 357(2)-ன் கீழ், பாராளுமன்றம் அல்லது குடியரசுத் தலைவரால் இயற்றப்பட்ட எந்தவொரு சட்டமும், பிரகடனம் முடிவுக்கு வந்த பின்னரும், தகுதிவாய்ந்த மாநில சட்டமன்றத்தால் மாற்றப்படும் வரை, ரத்து செய்யப்படும் வரை அல்லது திருத்தப்படும் வரை தொடர்ந்து நடைமுறையில் இருக்கும். (1978-க்கு முன், அவை 1 வருடத்தில் காலாவதியாகின).",
        "Option A is incorrect; laws do not lapse immediately.", "விருப்பம் A தவறு; சட்டங்கள் உடனடியாகக் காலாவதியாவதில்லை.",
        "Option B was the pre-1978 position, which was amended.", "விருப்பம் B என்பது 1978-க்கு முந்தைய நிலையாகும் (திருத்தப்பட்டுவிட்டது).",
        "Option C describes Article 250 laws under National Emergency.", "விருப்பம் C தேசிய அவசரநிலையின் கீழான சரத்து 250 சட்டங்களை விவரிக்கிறது.",
        "Option D is correct; they continue indefinitely until altered/repealed by the State Legislature.", "விருப்பம் D சரியானது; மாநில சட்டமன்றம் மாற்றும் வரை அவை காலவரையின்றித் தொடரும்.",
        "Contrast 250 vs 357(2): Article 250 laws lapse 6 MONTHS after emergency ends; Article 357(2) laws CONTINUE until altered/repealed by the State Legislature.",
        "250 vs 357(2) ஒப்பீடு: சரத்து 250 சட்டங்கள் அவசரநிலை முடிந்த 6 மாதங்களில் காலாவதியாகும்; சரத்து 357(2) சட்டங்கள் மாநில சட்டமன்றம் மாற்றும் வரை தொடரும்.",
        "This ensures legal continuity so that thousands of day-to-day laws enacted for the state do not suddenly vanish upon revocation.",
        "குடியரசுத் தலைவர் ஆட்சி ரத்தானவுடன் மாநிலத்தில் இயற்றப்பட்ட அன்றாடச் சட்டங்கள் திடீரென மறைந்துவிடாமல் சட்டத் தொடர்ச்சியை இது உறுதி செய்கிறது."
    ))

    # 030 - Key B
    qs.append(make_ep_q(
        PREFIX, 30, "Medium", "Judicial Doctrine", "Floor Test Mandatory Rule in Bommai",
        "In S.R. Bommai v. Union of India (1994), what did the Supreme Court hold regarding testing whether a Chief Minister enjoys the confidence of the House?",
        "எஸ்.ஆர். பொம்மை எதிர் மத்திய அரசு (1994) வழக்கில், ஒரு முதலமைச்சர் அவையின் நம்பிக்கையைப் பெற்றுள்ளாரா என்பதைச் சோதிப்பது குறித்து உச்ச நீதிமன்றம் என்ன தீர்ப்பளித்தது?",
        "The subjective satisfaction of the Governor based on private consultations is final", "தனிப்பட்ட ஆலோசனைகளின் அடிப்படையிலான ஆளுநரின் அகநிலை திருப்தியே இறுதியானது",
        "The floor of the Assembly is the only constitutionally valid forum to test majority, and not the Governor's subjective assessment", "சட்டமன்ற அவையே பெரும்பான்மையைச் சோதிப்பதற்கான ஒரே அரசியலமைப்பு தளம் ஆகும், மாறாக ஆளுநரின் அகநிலை மதிப்பீடு அல்ல",
        "The Election Commission must conduct an inquiry to verify legislative strength", "சட்டமன்ற பலத்தைச் சரிபார்க்க தேர்தல் ஆணையம் விசாரணை நடத்த வேண்டும்",
        "A referendum among the voters of the State must be held", "மாநில வாக்காளர்களிடையே பொது வாக்கெடுப்பு நடத்தப்பட வேண்டும்",
        "B",
        "The Supreme Court in S.R. Bommai ruled that the floor of the Legislative Assembly is the only constitutional place to test whether the Council of Ministers enjoys majority support. The Governor cannot decide majority based on subjective opinion or private parades of MLAs at Raj Bhavan.",
        "பொம்மை வழக்கில் உச்ச நீதிமன்றம், அமைச்சரவை பெரும்பான்மை ஆதரவைப் பெற்றுள்ளதா என்பதைச் சோதிப்பதற்கான ஒரே அரசியலமைப்பு தளம் சட்டமன்ற அவையே என்று தீர்ப்பளித்தது. ஆளுநர் தனது அகநிலை கருத்து அல்லது ராஜ்பவனில் நடக்கும் அணிவகுப்புகளின் அடிப்படையில் பெரும்பான்மையைத் தீர்மானிக்க முடியாது.",
        "Option A was explicitly rejected by the Supreme Court.", "விருப்பம் A உச்ச நீதிமன்றத்தால் வெளிப்படையாக நிராகரிக்கப்பட்டது.",
        "Option B is correct; the mandatory 'floor test' doctrine.", "விருப்பம் B சரியானது; கட்டாய 'நம்பிக்கை வாக்கெடுப்பு' கோட்பாடு.",
        "Option C is incorrect; Election Commission has no role in assembly floor tests.", "விருப்பம் C தவறு; வாக்கெடுப்பில் தேர்தல் ஆணையத்திற்குப் பங்கில்லை.",
        "Option D is constitutionally baseless.", "விருப்பம் D அரசியலமைப்பு ஆதாரமற்றது.",
        "Bommai Floor Test Rule: Raj Bhavan is NOT the assembly; majority MUST be tested on the floor of the House.",
        "பொம்மை வாக்கெடுப்பு விதி: ராஜ்பவன் சட்டமன்றம் அல்ல; பெரும்பான்மை அவையிலேயே சோதிக்கப்பட வேண்டும்.",
        "This ruling curbed the rampant practice of Governors dismissing governments based on backroom political intrigues.",
        "திரைக்குப் பின்னால் நடக்கும் அரசியல் சூழ்ச்சிகளின் அடிப்படையில் ஆளுநர்கள் அரசுகளைக் கலைக்கும் போக்கிற்கு இத்தீர்ப்பு முற்றுப்புள்ளி வைத்தது."
    ))

    # 031 - Key A
    qs.append(make_ep_q(
        PREFIX, 31, "Hard", "Constitutional Doctrine", "Secularism as Basic Structure in Bommai",
        "In the S.R. Bommai case, why did the Supreme Court uphold the dismissal of state governments in Madhya Pradesh, Rajasthan, and Himachal Pradesh?",
        "எஸ்.ஆர். பொம்மை வழக்கில், மத்தியப் பிரதேசம், ராஜஸ்தான் மற்றும் இமாச்சலப் பிரதேச மாநில அரசுகள் கலைக்கப்பட்டதை உச்ச நீதிமன்றம் ஏன் உறுதி செய்தது?",
        "Because secularism is part of the Basic Structure, and their state policies were found to be anti-secular", "மதச்சார்பின்மை என்பது அடிப்படைக் கட்டமைப்பின் ஒரு பகுதி என்பதால், அவற்றின் மாநிலக் கொள்கைகள் மதச்சார்பின்மைக்கு எதிராக இருந்தன",
        "Because they had refused to implement five-year plan projects", "அவை ஐந்தாண்டுத் திட்டப் பணிகளைச் செயல்படுத்த மறுத்ததால்",
        "Because the Chief Ministers had failed to attend the National Development Council", "முதலமைச்சர்கள் தேசிய வளர்ச்சிக் குழு கூட்டத்தில் கலந்துகொள்ளத் தவறியதால்",
        "Because their state budgets had run into severe deficits", "அவற்றின் மாநில வரவு-செலவுத் திட்டங்கள் கடுமையான பற்றாக்குறையைச் சந்தித்ததால்",
        "A",
        "In the Bommai case, the nine-judge bench unanimously held that Secularism is a part of the Basic Structure of the Indian Constitution. If any state government acts in violation of secularism or pursues anti-secular activities, it constitutes a failure of constitutional machinery justifying Article 356.",
        "பொம்மை வழக்கில், ஒன்பது நீதிபதிகள் கொண்ட அமர்வு மதச்சார்பின்மை என்பது இந்திய அரசியலமைப்பின் அடிப்படைக் கட்டமைப்பின் ஒரு பகுதி என்று ஒருமனதாகத் தீர்ப்பளித்தது. எந்தவொரு மாநில அரசும் மதச்சார்பின்மைக்கு எதிராகச் செயல்பட்டால், அது அரசியலமைப்பு இயந்திரத்தின் தோல்வியாகும், இதனால் சரத்து 356 நியாயப்படுத்தப்படுகிறது.",
        "Option A is correct; secularism is part of basic structure justifying dismissal.", "விருப்பம் A சரியானது; மதச்சார்பின்மை அடிப்படைக் கட்டமைப்பாக இருப்பதால் கலைப்பு உறுதி செய்யப்பட்டது.",
        "Option B is not a valid constitutional ground.", "விருப்பம் B சரியான அரசியலமைப்பு காரணம் அல்ல.",
        "Option C has no constitutional sanction.", "விருப்பம் C-க்கு அரசியலமைப்பு அதிகாரம் இல்லை.",
        "Option D pertains to Article 360, not Article 356.", "விருப்பம் D சரத்து 360 தொடர்பானது, 356 அல்ல.",
        "Bommai Milestone: Secularism is basic structure; religious politics violating secularism permits President's Rule.",
        "பொம்மை மைல்கல்: மதச்சார்பின்மை அடிப்படைக் கட்டமைப்பு; அதை மீறும் மத அரசியல் குடியரசுத் தலைவர் ஆட்சிக்கு வழிவகுக்கும்.",
        "However, in the same judgment, the court struck down the earlier dismissals of governments in Karnataka, Meghalaya, and Nagaland as unconstitutional.",
        "இருப்பினும், அதே தீர்ப்பில், கர்நாடகா, மேகாலயா மற்றும் நாகாலாந்து அரசுகள் முன்னதாகக் கலைக்கப்பட்டது அரசியலமைப்புக்கு முரணானது என நீதிமன்றம் ரத்து செய்தது."
    ))

    # 032 - Key C
    qs.append(make_ep_q(
        PREFIX, 32, "Medium", "Procedural", "Revocation of Article 356",
        "How can a proclamation of President's Rule under Article 356 be revoked before its normal expiration?",
        "சரத்து 356-ன் கீழான குடியரசுத் தலைவர் ஆட்சிப் பிரகடனம் அதன் இயல்பான காலாவதிக்கு முன்பாக எவ்வாறு ரத்து செய்யப்படலாம்?",
        "Only by a resolution passed by a special majority of Parliament", "பாராளுமன்றத்தின் சிறப்புப் பெரும்பான்மை தீர்மானத்தால் மட்டுமே",
        "Only by an order of the Supreme Court of India", "இந்திய உச்ச நீதிமன்றத்தின் உத்தரவால் மட்டுமே",
        "By the President at any time by a subsequent proclamation, which does NOT require parliamentary approval", "பிந்தைய பிரகடனத்தின் மூலம் எந்த நேரத்திலும் குடியரசுத் தலைவரால்; இதற்கு பாராளுமன்ற ஒப்புதல் தேவையில்லை",
        "By a resolution passed by the State Legislative Assembly", "மாநில சட்டமன்றத்தால் நிறைவேற்றப்படும் தீர்மானத்தின் மூலம்",
        "C",
        "Under Article 356(2), any proclamation issued under Article 356 may be revoked or varied by a subsequent proclamation by the President. Such a revocation does NOT require any parliamentary approval.",
        "சரத்து 356(2)-ன் கீழ், சரத்து 356-ன் கீழ் வெளியிடப்பட்ட எந்தவொரு பிரகடனமும் குடியரசுத் தலைவரால் பிந்தைய பிரகடனம் மூலம் ரத்து செய்யப்படலாம் அல்லது மாற்றப்படலாம். இத்தகைய ரத்திற்கு பாராளுமன்ற ஒப்புதல் எதுவும் தேவையில்லை.",
        "Option A describes approval, not revocation.", "விருப்பம் A ஒப்புதலை விவரிக்கிறது, ரத்தை அல்ல.",
        "Option B is incorrect; courts may declare it void, but presidential revocation is executive.", "விருப்பம் B தவறு; நீதிமன்றங்கள் செல்லாது எனலாம், ஆனால் ரத்து செய்வது நிர்வாகத்தின் செயல்.",
        "Option C is correct; President can revoke at any time without parliamentary approval.", "விருப்பம் C சரியானது; பாராளுமன்ற ஒப்புதலின்றி எந்த நேரத்திலும் குடியரசுத் தலைவர் ரத்து செய்யலாம்.",
        "Option D is wrong; the state assembly has no power to revoke Article 356.", "விருப்பம் D தவறு; சட்டமன்றத்திற்கு சரத்து 356-ஐ ரத்து செய்யும் அதிகாரம் இல்லை.",
        "Universal Revocation Rule: Presidential revocation requires NO parliamentary approval for ANY type of emergency (352, 356, or 360).",
        "பொதுவான ரத்து விதி: எந்தவொரு அவசரநிலையாக இருந்தாலும் (352, 356, 360), குடியரசுத் தலைவர் அதை ரத்து செய்ய பாராளுமன்ற ஒப்புதல் தேவையில்லை.",
        "When fresh elections are held and a new government takes oath, President's Rule is formally revoked under Article 356(2).",
        "புதிய தேர்தல்கள் நடத்தப்பட்டு புதிய அரசு பதவியேற்கும் போது, சரத்து 356(2)-ன் கீழ் குடியரசுத் தலைவர் ஆட்சி முறைப்படி ரத்து செய்யப்படுகிறது."
    ))

    # 033 - Key D
    qs.append(make_ep_q(
        PREFIX, 33, "Hard", "Judicial Precedent", "State of Rajasthan v. UOI (1977)",
        "In State of Rajasthan v. Union of India (1977), what was the Supreme Court's ruling regarding the Janata Government's mass dissolution of nine Congress-ruled state assemblies?",
        "ராஜஸ்தான் மாநிலம் எதிர் மத்திய அரசு (1977) வழக்கில், ஜனதா அரசு ஒன்பது காங்கிரஸ் ஆளும் மாநில சட்டமன்றங்களை ஒட்டுமொத்தமாகக் கலைத்தது குறித்து உச்ச நீதிமன்றத்தின் தீர்ப்பு என்ன?",
        "It declared all nine dissolutions unconstitutional and reinstated the ministries", "ஒன்பது கலைப்புகளையும் அரசியலமைப்புக்கு முரணானது என அறிவித்து அமைச்சரவைகளை மீண்டும் பதவியில் அமர்த்தியது",
        "It ruled that Article 356 cannot be invoked during post-election transitions", "தேர்தலுக்குப் பிந்தைய மாற்றங்களின் போது சரத்து 356-ஐப் பயன்படுத்த முடியாது என்று தீர்ப்பளித்தது",
        "It referred the entire matter to the International Court of Justice", "முழு விவகாரத்தையும் சர்வதேச நீதிமன்றத்திற்குப் பரிந்துரைத்தது",
        "It upheld the dissolutions, holding that a decisive shift in national electoral verdict could indicate loss of constitutional mandate by state governments", "தேசியத் தேர்தல் தீர்ப்பில் ஏற்பட்ட தீர்க்கமான மாற்றம் மாநில அரசுகளின் அரசியலமைப்பு ஆணையை இழந்ததைக் குறிக்கலாம் எனக் கூறி கலைப்புகளை உறுதி செய்தது",
        "D",
        "In State of Rajasthan v. UOI (1977), a seven-judge bench of the Supreme Court upheld the dismissal of the nine Congress-ruled state governments, holding that the satisfaction of the President could be based on the total rout of the ruling party in parliamentary elections reflecting a loss of public support.",
        "ராஜஸ்தான் மாநிலம் எதிர் மத்திய அரசு (1977) வழக்கில், உச்ச நீதிமன்றத்தின் ஏழு நீதிபதிகள் கொண்ட அமர்வு ஒன்பது காங்கிரஸ் அரசுகளின் கலைப்பை உறுதி செய்தது; பாராளுமன்றத் தேர்தலில் ஆளும் கட்சி அடைந்த படுதோல்வி மக்கள் ஆதரவை இழந்ததைக் காட்டுவதால் குடியரசுத் தலைவர் திருப்தியடைய அது காரணமாகலாம் எனத் தீர்ப்பளித்தது.",
        "Option A describes what happened later in Bommai, not in Rajasthan 1977.", "விருப்பம் A பின்னர் பொம்மை வழக்கில் நடந்ததை விவரிக்கிறது.",
        "Option B was not the ruling; the court allowed it.", "விருப்பம் B நீதிமன்றத் தீர்ப்பு அல்ல; நீதிமன்றம் அதை அனுமதித்தது.",
        "Option C is legally impossible for domestic constitutional matters.", "விருப்பம் C உள்நாட்டு விவகாரங்களுக்குச் சாத்தியமற்றது.",
        "Option D is correct; the 1977 bench upheld the dissolutions (later criticized and overruled in spirit by Bommai 1994).", "விருப்பம் D சரியானது; 1977 அமர்வு கலைப்புகளை உறுதி செய்தது (பின்னர் பொம்மை 1994-ல் இது விமர்சிக்கப்பட்டது).",
        "Historical Shift: 1977 (Rajasthan case upheld mass dissolution) -> 1994 (Bommai case outlawed political dissolution).",
        "வரலாற்று மாற்றம்: 1977 (ராஜஸ்தான் வழக்கு ஒட்டுமொத்தக் கலைப்பை உறுதி செய்தது) -> 1994 (பொம்மை வழக்கு அரசியல் கலைப்பைத் தடை செய்தது).",
        "In Bommai (1994), the Supreme Court held that the defeat of a party in Lok Sabha elections is NOT a ground for imposing President's Rule in states.",
        "பொம்மை (1994) வழக்கில், மக்களவைத் தேர்தலில் ஒரு கட்சி தோல்வியடைவது மாநிலங்களில் குடியரசுத் தலைவர் ஆட்சியை விதிப்பதற்கான காரணம் அல்ல என்று உச்ச நீதிமன்றம் தெளிவுபடுத்தியது."
    ))

    # 034 - Key B
    qs.append(make_ep_q(
        PREFIX, 34, "Hard", "Judicial Precedent", "Rameshwar Prasad v. UOI (2006)",
        "In Rameshwar Prasad v. Union of India (2006), why did the Supreme Court declare the dissolution of the Bihar Legislative Assembly unconstitutional?",
        "ராமேஷ்வர் பிரசாத் எதிர் மத்திய அரசு (2006) வழக்கில், பீகார் சட்டமன்றக் கலைப்பு அரசியலமைப்புக்கு முரணானது என்று உச்ச நீதிமன்றம் ஏன் அறிவித்தது?",
        "Because the Chief Minister had not completed his 5-year tenure", "முதலமைச்சர் தனது 5 ஆண்டு பதவிக்காலத்தை முடிக்காததால்",
        "Because the Governor's recommendation to dissolve the newly elected assembly before its first meeting to prevent a political party from forming government was held mala fide", "ஒரு அரசியல் கட்சி ஆட்சியமைப்பதைத் தடுப்பதற்காக, புதிதாகத் தேர்ந்தெடுக்கப்பட்ட சட்டமன்றத்தை அதன் முதல் கூட்டத்திற்கு முன்பே கலைக்க ஆளுநர் அளித்த பரிந்துரை தவறான உள்நோக்கம் (mala fide) கொண்டது எனக் கருதப்பட்டதால்",
        "Because the Election Commission had refused to conduct elections", "தேர்தல் ஆணையம் தேர்தலை நடத்த மறுத்ததால்",
        "Because Article 356 was invoked without the consent of the Chief Justice of Patna High Court", "பாட்னா உயர் நீதிமன்றத் தலைமை நீதிபதியின் ஒப்புதலின்றி சரத்து 356 பயன்படுத்தப்பட்டதால்",
        "B",
        "In Rameshwar Prasad (2006), the Supreme Court struck down the dissolution of the Bihar Assembly recommended by Governor Buta Singh, holding that preventing a political party from claiming majority by dissolving the assembly before it even met was based on extraneous and mala fide considerations.",
        "ராமேஷ்வர் பிரசாத் (2006) வழக்கில், ஆளுநர் பூட்டா சிங் பரிந்துரைத்த பீகார் சட்டமன்றக் கலைப்பை உச்ச நீதிமன்றம் ரத்து செய்தது; ஒரு அரசியல் கட்சி பெரும்பான்மையைக் கோருவதைத் தடுப்பதற்காக, சட்டமன்றம் கூடுவதற்கே முன்பாக அதைக் கலைத்தது தேவையற்ற மற்றும் தவறான உள்நோக்கம் கொண்டது என்று நீதிமன்றம் தீர்ப்பளித்தது.",
        "Option A is irrelevant to Article 356.", "விருப்பம் A சரத்து 356-க்கு தொடர்பற்றது.",
        "Option B is correct; Governor Buta Singh's mala fide report was struck down.", "விருப்பம் B சரியானது; ஆளுநர் பூட்டா சிங்கின் தவறான அறிக்கை ரத்து செய்யப்பட்டது.",
        "Option C is factually incorrect.", "விருப்பம் C தவறானது.",
        "Option D is wrong; High Court consent is never part of Article 356.", "விருப்பம் D தவறு; உயர் நீதிமன்ற ஒப்புதல் தேவையில்லை.",
        "Rameshwar Prasad Landmark: Governor cannot act as an agent of the ruling party at the Centre to preempt government formation.",
        "ராமேஷ்வர் பிரசாத் மைல்கல்: ஆட்சியை அமைப்பதைத் தடுக்க ஆளுநர் மத்தியில் ஆளும் கட்சியின் முகவராகச் செயல்பட முடியாது.",
        "Although the dissolution was held unconstitutional, fresh elections were allowed to proceed because election notifications had already been issued.",
        "கலைப்பு அரசியலமைப்புக்கு முரணானது என அறிவிக்கப்பட்ட போதிலும், தேர்தல் அறிவிக்கைகள் ஏற்கனவே வெளியிடப்பட்டுவிட்டதால் புதிய தேர்தல்கள் நடைபெற அனுமதிக்கப்பட்டன."
    ))

    # 035 - Key A
    qs.append(make_ep_q(
        PREFIX, 35, "Easy", "Historical", "First Imposition of Article 356",
        "In which State was President's Rule under Article 356 imposed for the very first time in independent India?",
        "சுதந்திர இந்தியாவில் சரத்து 356-ன் கீழான குடியரசுத் தலைவர் ஆட்சி முதன்முதலில் எந்த மாநிலத்தில் விதிக்கப்பட்டது?",
        "Punjab (East Punjab) in June 1951", "பஞ்சாப் (கிழக்கு பஞ்சாப்) ஜூன் 1951-ல்",
        "Kerala in July 1959", "கேரளா ஜூலை 1959-ல்",
        "Tamil Nadu in January 1976", "தமிழ்நாடு ஜனவரி 1976-ல்",
        "Uttar Pradesh in February 1968", "உத்தரப் பிரதேசம் பிப்ரவரி 1968-ல்",
        "A",
        "President's Rule under Article 356 was imposed for the very first time in Punjab (then East Punjab) in June 1951, due to factional infighting within the ruling Congress party leading to the resignation of Chief Minister Gopichand Bhargava.",
        "சுதந்திர இந்தியாவில் முதன்முதலில் சரத்து 356-ன் கீழான குடியரசுத் தலைவர் ஆட்சி ஜூன் 1951-ல் பஞ்சாபில் (அப்போது கிழக்கு பஞ்சாப்) விதிக்கப்பட்டது; ஆளும் காங்கிரஸ் கட்சியினரிடையேயான உள்கட்சி மோதலால் முதலமைச்சர் கோபிசந்த் பார்கவா ராஜினாமா செய்ததால் இது நிகழ்ந்தது.",
        "Option A is correct; Punjab in June 1951 was the historic first.", "விருப்பம் A சரியானது; ஜூன் 1951-ல் பஞ்சாப் முதல் மாநிலமாகும்.",
        "Option B (Kerala 1959) was the first dismissal of an elected communist state government.", "விருப்பம் B (கேரளா 1959) தேர்ந்தெடுக்கப்பட்ட கம்யூனிஸ்ட் அரசு கலைக்கப்பட்ட முதல் நிகழ்வாகும்.",
        "Option C (Tamil Nadu 1976) was during the National Emergency.", "விருப்பம் C (தமிழ்நாடு 1976) தேசிய அவசரநிலையின் போது நிகழ்ந்தது.",
        "Option D (UP 1968) occurred much later.", "விருப்பம் D (உ.பி 1968) மிகவும் பிந்தையது.",
        "TNPSC Standard PYQ: First state under Article 356 = Punjab (1951).",
        "TNPSC நிலையான வினா: சரத்து 356-ன் கீழ் முதல் மாநிலம் = பஞ்சாப் (1951).",
        "Dr. Rajendra Prasad was the President and Jawaharlal Nehru was the Prime Minister when Article 356 was first used.",
        "சரத்து 356 முதன்முதலில் பயன்படுத்தப்பட்ட போது டாக்டர் ராஜேந்திர பிரசாத் குடியரசுத் தலைவராகவும், ஜவஹர்லால் நேரு பிரதமராகவும் இருந்தனர்."
    ))

    # 036 - Key C
    qs.append(make_ep_q(
        PREFIX, 36, "Medium", "Historical", "Longest Spell of Article 356",
        "Which State experienced the longest continuous spell of President's Rule in Indian constitutional history?",
        "இந்திய அரசியலமைப்பு வரலாற்றில் மிக நீண்ட தொடர்ச்சியான குடியரசுத் தலைவர் ஆட்சியை எதிர்கொண்ட மாநிலம் எது?",
        "Jammu and Kashmir (1990–1996)", "ஜம்மு காஷ்மீர் (1990-1996)",
        "Assam (1980–1985)", "அசாம் (1980-1985)",
        "Punjab (May 1987 to February 1992)", "பஞ்சாப் (மே 1987 முதல் பிப்ரவரி 1992 வரை)",
        "Manipur (1993–1998)", "மணிப்பூர் (1993-1998)",
        "C",
        "Punjab experienced the longest continuous spell of President's Rule under Article 356, lasting for nearly 5 years from May 11, 1987 to February 25, 1992. Multiple constitutional amendments (48th, 59th, 64th, 67th, and 68th CAAs) had to be passed to repeatedly extend it beyond the 3-year ceiling.",
        "பஞ்சாப் மாநிலம் மே 11, 1987 முதல் பிப்ரவரி 25, 1992 வரை கிட்டத்தட்ட 5 ஆண்டுகள் சரத்து 356-ன் கீழான மிக நீண்ட தொடர்ச்சியான குடியரசுத் தலைவர் ஆட்சியை எதிர்கொண்டது. 3 ஆண்டு உச்சவரம்பிற்கு அப்பால் நீட்டிக்க பல அரசியலமைப்பு திருத்தங்கள் (48, 59, 64, 67 மற்றும் 68-வது திருத்தங்கள்) இயற்றப்பட்டன.",
        "Option A was under Governor's Rule followed by President's Rule under J&K special status, but Punjab is the record under pure Article 356.", "விருப்பம் A ஜம்மு காஷ்மீர் சிறப்பு விதிகளின் கீழ் அமைந்தது.",
        "Option B is incorrect.", "விருப்பம் B தவறானது.",
        "Option C is correct; Punjab (1987-1992) for nearly 5 continuous years.", "விருப்பம் C சரியானது; பஞ்சாப் (1987-1992) கிட்டத்தட்ட 5 தொடர்ச்சியான ஆண்டுகள்.",
        "Option D is incorrect.", "விருப்பம் D தவறானது.",
        "Punjab Constitutional Record: 5 years continuous (1987-1992), requiring the 68th CAA 1991 to extend to 5 years.",
        "பஞ்சாப் அரசியலமைப்பு சாதனை: 5 ஆண்டுகள் தொடர்ச்சியாக (1987-1992), 5 ஆண்டுகள் வரை நீட்டிக்க 1991-ன் 68-வது திருத்தம் தேவைப்பட்டது.",
        "President's Rule in Punjab finally ended in February 1992 when democratic elections were held and Beant Singh became Chief Minister.",
        "பிப்ரவரி 1992-ல் ஜனநாயகத் தேர்தல்கள் நடத்தப்பட்டு பியாந்த் சிங் முதலமைச்சரான போது பஞ்சாபில் குடியரசுத் தலைவர் ஆட்சி முடிவுக்கு வந்தது."
    ))

    # 037 - Key D
    qs.append(make_ep_q(
        PREFIX, 37, "Easy", "General Knowledge", "States without President's Rule",
        "In which of the following States has President's Rule under Article 356 NEVER been imposed since their creation?",
        "உருவாக்கப்பட்டதிலிருந்து பின்வரும் எந்த மாநிலங்களில் சரத்து 356-ன் கீழான குடியரசுத் தலைவர் ஆட்சி ஒருமுறை கூட விதிக்கப்படவில்லை?",
        "Goa and Sikkim", "கோவா மற்றும் சிக்கிம்",
        "Uttarakhand and Jharkhand", "உத்தரகாண்ட் மற்றும் ஜார்க்கண்ட்",
        "Tripura and Mizoram", "திரிபுரா மற்றும் மிசோரம்",
        "Chhattisgarh and Telangana", "சத்தீஸ்கர் மற்றும் தெலங்கானா",
        "D",
        "Chhattisgarh (formed in 2000) and Telangana (formed in 2014) are the only two Indian states where President's Rule under Article 356 has never been proclaimed to date.",
        "2000-ல் உருவாக்கப்பட்ட சத்தீஸ்கர் மற்றும் 2014-ல் உருவாக்கப்பட்ட தெலங்கானா ஆகிய இரண்டு மாநிலங்களில் மட்டுமே இதுவரை சரத்து 356-ன் கீழான குடியரசுத் தலைவர் ஆட்சி ஒருமுறை கூட பிரகடனப்படுத்தப்படவில்லை.",
        "Option A is incorrect; both Goa and Sikkim have experienced Article 356.", "விருப்பம் A தவறு; கோவா, சிக்கிம் இரண்டும் எதிர்கொண்டுள்ளன.",
        "Option B is incorrect; Uttarakhand (2016) and Jharkhand (2009, 2010, 2013) have had President's Rule.", "விருப்பம் B தவறு; உத்தரகாண்ட் மற்றும் ஜார்க்கண்ட் எதிர்கொண்டுள்ளன.",
        "Option C is incorrect; both Tripura and Mizoram have had Article 356.", "விருப்பம் C தவறு; திரிபுரா, மிசோரம் இரண்டும் எதிர்கொண்டுள்ளன.",
        "Option D is correct; Chhattisgarh and Telangana have ZERO instances.", "விருப்பம் D சரியானது; சத்தீஸ்கர் மற்றும் தெலங்கானா பூஜ்ஜிய முறை.",
        "TNPSC High-Yield Fact: Chhattisgarh and Telangana are the ONLY two states where Article 356 has never been imposed.",
        "TNPSC உயர்-விளைச்சல் தகவல்: சரத்து 356 ஒருமுறை கூட விதிக்கப்படாத ஒரே இரண்டு மாநிலங்கள் சத்தீஸ்கர் மற்றும் தெலங்கானா மட்டுமே.",
        "All other 26 states of India have experienced President's Rule at least once.",
        "இந்தியாவின் மற்ற அனைத்து 26 மாநிலங்களும் குறைந்தது ஒரு முறையாவது குடியரசுத் தலைவர் ஆட்சியை எதிர்கொண்டுள்ளன."
    ))

    # 038 - Key B
    qs.append(make_ep_q(
        PREFIX, 38, "Hard", "Constitutional Wording", "Article 356 'Or Otherwise' Clause",
        "Under Article 356(1), the President can issue a proclamation upon receipt of a report from the Governor of a State 'or otherwise'. What does 'or otherwise' mean constitutionally?",
        "சரத்து 356(1)-ன் கீழ், ஒரு மாநில ஆளுநரிடமிருந்து அறிக்கை பெறப்பட்டவுடன் 'அல்லது பிற வழிகளில்' (or otherwise) குடியரசுத் தலைவர் பிரகடனத்தை வெளியிடலாம். அரசியலமைப்பு ரீதியாக 'பிற வழிகளில்' என்பது எதனைக் குறிக்கிறது?",
        "Only upon the order of the Chief Justice of India", "இந்தியத் தலைமை நீதிபதியின் உத்தரவின் பேரில் மட்டுமே",
        "The President can act on information received from sources other than the Governor's report, including the Union Cabinet or intelligence reports", "ஆளுநரின் அறிக்கை தவிர மத்திய அமைச்சரவை அல்லது உளவுத்துறை அறிக்கைகள் உள்ளிட்ட பிற ஆதாரங்களிலிருந்து பெறப்பட்ட தகவல்களின் அடிப்படையில் குடியரசுத் தலைவர் செயல்படலாம்",
        "Only after a statewide referendum demands dismissal", "மாநில அளவிலான பொது வாக்கெடுப்பு கலைப்பைக் கோரிய பிறகே",
        "Only when the Governor has resigned from office", "ஆளுநர் தனது பதவியை ராஜினாமா செய்திருக்கும் போது மட்டுமே",
        "B",
        "The phrase 'or otherwise' in Article 356(1) empowers the President to proclaim President's Rule even in the ABSENCE of a report from the Governor, if satisfied from other credible sources (such as Union Cabinet advice, Central intelligence, or factual events).",
        "சரத்து 356(1)-ல் உள்ள 'அல்லது பிற வழிகளில்' என்ற சொற்றொடர், ஆளுநரிடமிருந்து அறிக்கை இல்லாத போதிலும் கூட, பிற நம்பகமான ஆதாரங்களின் (மத்திய அமைச்சரவை ஆலோசனை, உளவுத்துறை அல்லது கள நிகழ்வுகள்) அடிப்படையில் திருப்தியடைந்தால் குடியரசுத் தலைவர் ஆட்சியை அறிவிக்க குடியரசுத் தலைவருக்கு அதிகாரமளிக்கிறது.",
        "Option A is incorrect; the judiciary cannot trigger Article 356.", "விருப்பம் A தவறு; நீதித்துறை சரத்து 356-ஐத் தூண்ட முடியாது.",
        "Option B is correct; enables action without a Governor's report.", "விருப்பம் B சரியானது; ஆளுநர் அறிக்கையின்றி செயல்பட அனுமதியளிக்கிறது.",
        "Option C is baseless.", "விருப்பம் C ஆதாரமற்றது.",
        "Option D is incorrect.", "விருப்பம் D தவறானது.",
        "Tamil Nadu 1991 Precedent: In 1991, Governor Surjit Singh Barnala refused to recommend the dismissal of the DMK government; the Centre invoked Article 356 'otherwise'!",
        "தமிழக 1991 முன்னுதாரணம்: 1991-ல் ஆளுநர் சுர்ஜித் சிங் பர்னாலா திமுக அரசைக் கலைக்கப் பரிந்துரைக்க மறுத்த போது, மத்திய அரசு 'பிற வழிகளில்' சரத்து 356-ஐப் பயன்படுத்தியது!",
        "Dr. B.R. Ambedkar defended the 'or otherwise' phrase in the Constituent Assembly to ensure the Union is not paralyzed if a partisan Governor suppresses the real situation.",
        "ஒரு சார்புடைய ஆளுநர் உண்மையான நிலையை மறைத்தால் மத்திய அரசு முடங்கிவிடக் கூடாது என்பதற்காகவே 'பிற வழிகளில்' என்ற சொற்றொடரை அம்பேத்கர் அரசியலமைப்பு நிர்ணய சபையில் ஆதரித்தார்."
    ))

    # 039 - Key A
    qs.append(make_ep_q(
        PREFIX, 39, "Hard", "Financial Mechanism", "Article 357(1)(c) Expenditure Authorization",
        "During President's Rule under Article 356, when the Lok Sabha is not in session, who can authorize expenditure from the Consolidated Fund of the State pending parliamentary sanction?",
        "சரத்து 356-ன் கீழான குடியரசுத் தலைவர் ஆட்சியின் போது, மக்களவை கூட்டத்தொடரில் இல்லாத போது, பாராளுமன்ற ஒப்புதலுக்காகக் காத்திருக்கும் நிலையில் மாநிலத் தொகுப்பு நிதியிலிருந்து செலவினத்தை யார் அனுமதிக்க முடியும்?",
        "The President of India under Article 357(1)(c)", "சரத்து 357(1)(c)-ன் கீழ் இந்தியக் குடியரசுத் தலைவர்",
        "The Governor of the State on his personal discretion", "மாநில ஆளுநர் தனது தனிப்பட்ட விருப்பத்தின் பேரில்",
        "The Comptroller and Auditor General of India (CAG)", "இந்தியக் கணக்குத் தணிக்கைத் தலைவர் (CAG)",
        "The Secretary-General of the Lok Sabha", "மக்களவையின் பொதுச் செயலாளர்",
        "A",
        "Under Article 357(1)(c), when the Lok Sabha is not in session, the President is authorized to sanction expenditure from the Consolidated Fund of the State pending sanction of such expenditure by Parliament.",
        "சரத்து 357(1)(c)-ன் கீழ், மக்களவை கூட்டத்தொடரில் இல்லாத போது, பாராளுமன்றத்தால் அத்தகைய செலவினத்திற்கு ஒப்புதல் அளிக்கப்படும் வரை, மாநிலத்தின் தொகுப்பு நிதியிலிருந்து செலவினத்தை அனுமதிக்கக் குடியரசுத் தலைவருக்கு அதிகாரம் உண்டு.",
        "Option A is correct; President under Article 357(1)(c).", "விருப்பம் A சரியானது; சரத்து 357(1)(c)-ன் கீழ் குடியரசுத் தலைவர்.",
        "Option B is incorrect; the Governor has no independent constitutional power to authorize fund expenditure without legislative sanction.", "விருப்பம் B தவறு; ஆளுநருக்கு சட்டமன்ற அனுமதியின்றி நிதியை அனுமதிக்கும் அதிகாரம் இல்லை.",
        "Option C audits accounts; does not authorize expenditure.", "விருப்பம் C கணக்குகளைத் தணிக்கை செய்கிறது, செலவை அனுமதிப்பதில்லை.",
        "Option D is an administrative officer with no financial appropriating powers.", "விருப்பம் D நிதி ஒதுக்கும் அதிகாரமற்ற நிர்வாக அதிகாரி.",
        "Financial Continuity: When Lok Sabha is not in session, Article 357(1)(c) prevents state governance from freezing by allowing the President to sanction funds.",
        "நிதித் தொடர்ச்சி: மக்களவை கூடாத போது, குடியரசுத் தலைவர் நிதியை அனுமதிக்க வகை செய்வதன் மூலம் மாநில நிர்வாகம் முடங்குவதை சரத்து 357(1)(c) தடுக்கிறது.",
        "When the Lok Sabha resumes its session, the state budget and all expenditures must be placed before Parliament for formal approval.",
        "மக்களவை மீண்டும் கூடும் போது, மாநில வரவு-செலவுத் திட்டம் மற்றும் அனைத்துச் செலவினங்களும் பாராளுமன்றத்தின் முன் வைக்கப்பட்டு முறைப்படி ஒப்புதல் பெறப்பட வேண்டும்."
    ))

    # 040 - Key C
    qs.append(make_ep_q(
        PREFIX, 40, "Medium", "Institutional Machinery", "President's Acts Consultation",
        "When Parliament delegates lawmaking powers for a State under President's Rule to the President under Article 357(1)(a), whom does the President usually consult?",
        "சரத்து 357(1)(a)-ன் கீழ் குடியரசுத் தலைவர் ஆட்சியிலுள்ள மாநிலத்திற்கான சட்டமியற்றும் அதிகாரத்தைப் பாராளுமன்றம் குடியரசுத் தலைவருக்கு வழங்கும் போது, குடியரசுத் தலைவர் வழக்கமாக யாரைக் கலந்தாலோசிக்கிறார்?",
        "The Chief Justice of the State High Court", "மாநில உயர் நீதிமன்றத் தலைமை நீதிபதியை",
        "A panel of retired Governors", "ஓய்வுபெற்ற ஆளுநர்களின் குழுவை",
        "A Parliamentary Consultative Committee consisting of Members of Parliament from that State", "அந்த மாநிலத்தைச் சேர்ந்த பாராளுமன்ற உறுப்பினர்களைக் கொண்ட பாராளுமன்ற ஆலோசனைக் குழுவை",
        "The State Public Service Commission", "மாநில அரசுப் பணியாளர் தேர்வாணையத்தை",
        "C",
        "When lawmaking power is delegated to the President under Article 357(1)(a), the delegating Act of Parliament usually provides for the constitution of a Parliamentary Consultative Committee comprising members of both Houses representing that State, whom the President consults before enacting 'President's Acts'.",
        "சரத்து 357(1)(a)-ன் கீழ் சட்டமியற்றும் அதிகாரம் குடியரசுத் தலைவருக்கு வழங்கப்படும் போது, அந்த மாநிலத்தைப் பிரதிநிதித்துவப்படுத்தும் இரு அவைகளின் உறுப்பினர்களைக் கொண்ட ஒரு பாராளுமன்ற ஆலோசனைக் குழுவை அமைக்க பாராளுமன்றச் சட்டம் வழிவகை செய்கிறது; 'குடியரசுத் தலைவர் சட்டங்களை' இயற்றுவதற்கு முன் குடியரசுத் தலைவர் இக்குழுவைக் கலந்தாலோசிக்கிறார்.",
        "Option A is incorrect; High Court judges are not consulted on political legislation.", "விருப்பம் A தவறு; உயர் நீதிமன்ற நீதிபதிகள் கலந்தாலோசிக்கப்படுவதில்லை.",
        "Option B is baseless.", "விருப்பம் B ஆதாரமற்றது.",
        "Option C is correct; Parliamentary Consultative Committee of MPs from the State.", "விருப்பம் C சரியானது; மாநில எம்.பி.க்களைக் கொண்ட பாராளுமன்ற ஆலோசனைக் குழு.",
        "Option D handles recruitment, not legislation.", "விருப்பம் D ஆளெடுப்பை மட்டுமே கையாள்கிறது.",
        "President's Acts Convention: The President enacts laws called 'President's Acts' in consultation with the state's MPs committee.",
        "குடியரசுத் தலைவர் சட்ட நடைமுறை: மாநில எம்.பி.க்கள் குழுவுடன் கலந்தாலோசித்து குடியரசுத் தலைவர் 'குடியரசுத் தலைவர் சட்டங்களை' இயற்றுகிறார்.",
        "These President's Acts are subsequently laid before each House of Parliament.",
        "இந்தக் குடியரசுத் தலைவர் சட்டங்கள் பின்னர் பாராளுமன்றத்தின் இரு அவைகளிலும் வைக்கப்படுகின்றன."
    ))

    # 041 - Key D
    qs.append(make_ep_q(
        PREFIX, 41, "Hard", "Sarkaria Commission", "Proper Grounds for Article 356",
        "According to the Sarkaria Commission (1988) and the S.R. Bommai judgment (1994), which of the following is considered a PROPER and constitutionally valid ground for imposing President's Rule?",
        "சர்க்காரியா ஆணையம் (1988) மற்றும் எஸ்.ஆர். பொம்மை தீர்ப்பின் (1994) படி, பின்வருவனவற்றில் எது குடியரசுத் தலைவர் ஆட்சியை விதிப்பதற்கான முறையான மற்றும் அரசியலமைப்பு ரீதியாகச் செல்லுபடியாகும் காரணமாகக் கருதப்படுகிறது?",
        "Defeat of the ruling state party in Lok Sabha general elections", "மக்களவைப் பொதுத்தேர்தலில் ஆளும் மாநிலக் கட்சி படுதோல்வி அடைவது",
        "Internal instability within the ruling party where ministry still retains assembly majority", "அமைச்சரவை இன்னமும் சட்டமன்றப் பெரும்பான்மையைத் தக்கவைத்திருக்கும் நிலையில் ஆளும் கட்சிக்குள் நிலவும் உள்கட்சி பூசல்",
        "Allegations of corruption or maladministration against the state ministry without assembly breakdown", "சட்டமன்ற முறிவின்றி மாநில அமைச்சரவை மீது சுமத்தப்படும் ஊழல் அல்லது தவறான நிர்வாகக் குற்றச்சாட்டுகள்",
        "A hung assembly where after general elections, no party or coalition is able to secure a majority to form a government", "பொதுத்தேர்தலுக்குப் பிறகு எந்தக் கட்சியும் அல்லது கூட்டணியும் ஆட்சியமைக்க பெரும்பான்மையைப் பெற முடியாத ஒரு தொங்கு சட்டமன்ற நிலை",
        "D",
        "Both the Sarkaria Commission and the Supreme Court in Bommai explicitly classified a hung assembly after general elections where no party or coalition can form a government as a PROPER ground for invoking Article 356. Defeat in Lok Sabha polls, internal party wrangling, and mere allegations of corruption were classified as IMPROPER grounds.",
        "பொதுத்தேர்தலுக்குப் பிறகு எந்தக் கட்சியும் அல்லது கூட்டணியும் ஆட்சியமைக்க முடியாத 'தொங்கு சட்டமன்றம்' உருவாவதை சரத்து 356-ஐப் பயன்படுத்துவதற்கான முறையான காரணமாக சர்க்காரியா ஆணையமும் உச்ச நீதிமன்றமும் வகைப்படுத்தின. மக்களவைத் தேர்தல் தோல்வி, உள்கட்சி மோதல் மற்றும் வெறும் ஊழல் குற்றச்சாட்டுகள் முறையற்ற காரணங்களாக வகைப்படுத்தப்பட்டன.",
        "Option A was declared improper in Bommai.", "விருப்பம் A பொம்மை வழக்கில் முறையற்றது என அறிவிக்கப்பட்டது.",
        "Option B is improper as long as ministry has floor majority.", "விருப்பம் B அவையில் பெரும்பான்மை இருக்கும் வரை முறையற்றது.",
        "Option C is improper; corruption must be dealt with by criminal law, not by dismissing government.", "விருப்பம் C முறையற்றது; ஊழலை குற்றவியல் சட்டத்தால் கையாள வேண்டும், அரசைக் கலைக்கக் கூடாது.",
        "Option D is correct; hung assembly with no viable government is an undisputed proper ground.", "விருப்பம் D சரியானது; ஆட்சியமைக்க முடியாத தொங்கு சட்டமன்றம் ஒரு முறையான காரணமாகும்.",
        "Proper vs Improper Grounds: Proper = Hung assembly, floor defeat without alternative, defiance of Art 365, anti-secular policies.",
        "முறையான vs முறையற்ற காரணங்கள்: முறையான = தொங்கு சட்டமன்றம், மாற்று இன்றி அவையில் தோல்வி, சரத்து 365 மீறல், மதச்சார்பின்மைக்கு எதிரான செயல்.",
        "Improper = Lok Sabha poll defeat, Governor's personal displeasure, corruption allegations, internal party rivalries.",
        "முறையற்றவை = மக்களவைத் தேர்தல் தோல்வி, ஆளுநரின் தனிப்பட்ட அதிருப்தி, ஊழல் குற்றச்சாட்டுகள், உள்கட்சி மோதல்கள்."
    ))

    # 042 - Key B
    qs.append(make_ep_q(
        PREFIX, 42, "Hard", "Sarkaria Commission", "Physical Breakdown Category",
        "How did the Sarkaria Commission define 'Physical Breakdown' as a ground for Article 356?",
        "சரத்து 356-ற்கான காரணமாக 'உடல்/இயல்பு முடக்கம்' (Physical Breakdown) என்பதை சர்க்காரியா ஆணையம் எவ்வாறு வரையறுத்தது?",
        "When all state ministers resign simultaneously", "அனைத்து மாநில அமைச்சர்களும் ஒரே நேரத்தில் ராஜினாமா செய்யும் போது",
        "Where a situation of widespread internal violence, paralyzing insurgency, or natural calamity renders the state government incapable of functioning", "பரவலான உள்நாட்டு வன்முறை, முடக்கும் கிளர்ச்சி அல்லது இயற்கை பேரழிவு ஆகியவற்றால் மாநில அரசு செயல்பட முடியாத நிலைக்குத் தள்ளப்படும் போது",
        "When the state treasury runs out of cash", "மாநில கருவூலத்தில் பணம் தீர்ந்து போகும் போது",
        "When the Governor falls critically ill", "ஆளுநர் தீவிர உடல்நலக்குறைவுக்கு ஆளாகும் போது",
        "B",
        "The Sarkaria Commission defined 'Physical Breakdown' as a situation where widespread internal violence, terrorism, or rebellion paralyzes the state government to the extent that it is physically impossible to carry on governance in accordance with the Constitution.",
        "சர்க்காரியா ஆணையம் 'உடல்/இயல்பு முடக்கம்' (Physical Breakdown) என்பதை, பரவலான உள்நாட்டு வன்முறை, பயங்கரவாதம் அல்லது கிளர்ச்சியால் மாநில அரசு முற்றிலும் முடங்கி, அரசியலமைப்பு விதிகளின்படி நிர்வாகத்தை முன்னெடுப்பது நடைமுறையில் சாத்தியமற்றதாக மாறும் சூழ்நிலை என வரையறுத்தது.",
        "Option A describes political breakdown.", "விருப்பம் A அரசியல் முடக்கத்தை விவரிக்கிறது.",
        "Option B is correct; physical paralysis due to violence or insurgency.", "விருப்பம் B சரியானது; வன்முறை அல்லது கிளர்ச்சியால் நிர்வாகம் இயற்பியல் ரீதியாக முடங்குதல்.",
        "Option C describes financial emergency under Article 360.", "விருப்பம் C சரத்து 360 நிதி அவசரநிலையைக் குறிக்கிறது.",
        "Option D is handled by appointing an acting Governor under Article 160.", "விருப்பம் D சரத்து 160-ன் கீழ் தற்காலிக ஆளுநரை நியமிப்பதன் மூலம் கையாளப்படுகிறது.",
        "Sarkaria 4-Fold Breakdown: Political (hung assembly), Constitutional (Art 365 defiance), Physical (insurgency/violence paralysis).",
        "சர்க்காரியாவின் 4 மடங்கு முடக்கம்: அரசியல் (தொங்கு சபை), அரசியலமைப்பு (சரத்து 365 மீறல்), இயல்பு/உடல் முடக்கம் (கிளர்ச்சி/வன்முறை முடக்கம்).",
        "The Commission emphasized that even during physical breakdown, central forces should be deployed first before contemplating dismissal of the state government.",
        "இயல்பு முடக்கத்தின் போது கூட, மாநில அரசைக் கலைப்பதற்கு முன் மத்தியப் படைகளை அனுப்புவதே முதல் நடவடிக்கையாக இருக்க வேண்டும் என்று ஆணையம் வலியுறுத்தியது."
    ))

    # 043 - Key A
    qs.append(make_ep_q(
        PREFIX, 43, "Hard", "Judicial Precedent", "Judicial Revival of Assemblies in Bommai",
        "Under the S.R. Bommai doctrine, what extraordinary power does the judiciary possess if it holds an Article 356 proclamation unconstitutional?",
        "எஸ்.ஆர். பொம்மை கோட்பாட்டின் கீழ், சரத்து 356 பிரகடனம் அரசியலமைப்புக்கு முரணானது என்று தீர்ப்பளித்தால் நீதித்துறைக்கு என்ன அசாதாரண அதிகாரம் உள்ளது?",
        "The power to revive the dissolved Legislative Assembly and reinstate the dismissed Council of Ministers", "கலைக்கப்பட்ட சட்டமன்றத்தை மீண்டும் உயிர்ப்பிக்கவும், பதவி நீக்கம் செய்யப்பட்ட அமைச்சரவையை மீண்டும் பதவியில் அமர்த்தவும் உள்ள அதிகாரம்",
        "The power to award financial damages to the dismissed Chief Minister from the Union Consolidated Fund", "மத்தியத் தொகுப்பு நிதியிலிருந்து பதவி நீக்கம் செய்யப்பட்ட முதலமைச்சருக்கு நிதி இழப்பீடு வழங்கும் அதிகாரம்",
        "The power to disqualify the Prime Minister from contesting future elections", "எதிர்காலத் தேர்தல்களில் போட்டியிடுவதிலிருந்து பிரதமரைத் தகுதி நீக்கம் செய்யும் அதிகாரம்",
        "The power to place the State under direct United Nations administration", "மாநிலத்தை ஐக்கிய நாடுகள் சபையின் நேரடி நிர்வாகத்தின் கீழ் கொண்டுவரும் அதிகாரம்",
        "A",
        "In the Bommai case, the Supreme Court established the doctrine of 'Judicial Revival': if the proclamation is held mala fide or unconstitutional, the court has the power to restore status quo ante, reviving the dissolved Legislative Assembly and reinstating the dismissed Ministry.",
        "பொம்மை வழக்கில் உச்ச நீதிமன்றம் 'நீதித்துறை உயிர்ப்பித்தல்' (Judicial Revival) கோட்பாட்டை நிறுவியது: பிரகடனம் தவறான உள்நோக்கம் கொண்டது அல்லது அரசியலமைப்புக்கு முரணானது எனக் கண்டறியப்பட்டால், நீதிமன்றம் பழைய நிலையை மீட்டெடுக்கலாம், கலைக்கப்பட்ட சட்டமன்றத்தை உயிர்ப்பிக்கலாம் மற்றும் பதவி நீக்கப்பட்ட அமைச்சரவையை மீண்டும் பதவியில் அமர்த்தலாம்.",
        "Option A is correct; the historic power of judicial revival of assemblies.", "விருப்பம் A சரியானது; சட்டமன்றங்களை நீதித்துறை உயிர்ப்பிக்கும் வரலாற்று அதிகாரம்.",
        "Option B is incorrect; damages are not awarded in constitutional review of Art 356.", "விருப்பம் B தவறு; சரத்து 356 ஆய்வில் இழப்பீடுகள் வழங்கப்படுவதில்லை.",
        "Option C is baseless.", "விருப்பம் C ஆதாரமற்றது.",
        "Option D is impossible under Indian sovereignty.", "விருப்பம் D சாத்தியமற்றது.",
        "Landmark Milestone: The power of judicial revival was applied in Arunachal Pradesh in Nabam Rebia (2016) and Uttarakhand (2016).",
        "மைல்கல் நிகழ்வு: நபம் ரெபியா (2016) வழக்கில் அருணாச்சலப் பிரதேசத்திலும், 2016-ல் உத்தரகாண்டிலும் சட்டமன்றத்தை மீண்டும் உயிர்ப்பிக்கும் இந்த அதிகாரம் பயன்படுத்தப்பட்டது.",
        "Before Bommai, once an assembly was dissolved, the court could not undo the dissolution even if it was clearly illegal.",
        "பொம்மை வழக்கிற்கு முன், ஒருமுறை சட்டமன்றம் கலைக்கப்பட்டால், அது சட்டவிரோதமானது என்றாலும் நீதிமன்றத்தால் அதை மாற்ற முடியாத நிலை இருந்தது."
    ))

    # 044 - Key C
    qs.append(make_ep_q(
        PREFIX, 44, "Medium", "Constitutional Safeguards", "Rajya Sabha Role when Lok Sabha Dissolved under 356",
        "If a proclamation of President's Rule is issued when the Lok Sabha is dissolved, how long does the proclamation survive if the Rajya Sabha approves it within two months?",
        "மக்களவை கலைக்கப்பட்டிருக்கும் போது குடியரசுத் தலைவர் ஆட்சிப் பிரகடனம் வெளியிடப்பட்டால், மாநிலங்களவை இரண்டு மாதங்களுக்குள் அதற்கு ஒப்புதல் அளித்தால் அப்பிரகடனம் எவ்வளவு காலம் நீடிக்கும்?",
        "Indefinitely without needing Lok Sabha approval", "மக்களவை ஒப்புதல் தேவையின்றி காலவரையின்றி",
        "For six months automatically", "தானாகவே ஆறு மாதங்கள்",
        "Until thirty days from the first sitting of the reconstituted Lok Sabha", "புதிதாக அமைக்கப்பட்ட மக்களவையின் முதல் கூட்டத்திலிருந்து முப்பது நாட்கள் வரை",
        "Only for fourteen days from the declaration of general election results", "பொதுத்தேர்தல் முடிவுகள் அறிவிக்கப்பட்டதிலிருந்து பதினான்கு நாட்கள் மட்டுமே",
        "C",
        "Under the proviso to Article 356(3), if Lok Sabha dissolution takes place before approval, the proclamation ceases at the expiration of thirty days from the first sitting of the reconstituted Lok Sabha, unless approved by a resolution of the new Lok Sabha within those thirty days.",
        "சரத்து 356(3)-ன் வரம்புரையின் கீழ், ஒப்புதலுக்கு முன் மக்களவை கலைக்கப்பட்டால், புதிய மக்களவை கூடிய முதல் அமர்விலிருந்து முப்பது நாட்களுக்குள் ஒப்புதல் தீர்மானத்தை நிறைவேற்றாவிட்டால் அப்பிரகடனம் காலாவதியாகிவிடும்.",
        "Option A is wrong because Lok Sabha must also approve within 30 days.", "விருப்பம் A தவறு, ஏனெனில் புதிய மக்களவையும் 30 நாட்களில் ஒப்புதல் அளிக்க வேண்டும்.",
        "Option B is incorrect.", "விருப்பம் B தவறானது.",
        "Option C is correct; thirty days from the first sitting of the new Lok Sabha.", "விருப்பம் C சரியானது; புதிய மக்களவையின் முதல் கூட்டத்திலிருந்து முப்பது நாட்கள்.",
        "Option D is wrong.", "விருப்பம் D தவறானது.",
        "TNPSC 30-Day Rule: Same 30-day rule applies to all three emergency proclamations (Articles 352, 356, and 360) during Lok Sabha dissolution.",
        "TNPSC 30 நாள் விதி: மக்களவை கலைக்கப்பட்டிருக்கும் போது மூன்று அவசரநிலைப் பிரகடனங்களுக்கும் (சரத்துகள் 352, 356, 360) இதே 30 நாள் விதி பொருந்தும்.",
        "This ensures that the permanent chamber (Rajya Sabha) sustains the proclamation until the new popular chamber can scrutinize it.",
        "புதிய மக்கள் பிரதிநிதிகள் அவை அதை ஆய்வு செய்யும் வரை நிரந்தர அவையான மாநிலங்களவை பிரகடனத்தைத் தக்கவைப்பதை இது உறுதி செய்கிறது."
    ))

    # 045 - Key D
    qs.append(make_ep_q(
        PREFIX, 45, "Hard", "Sarkaria Commission", "Article 356 as Measure of Last Resort",
        "What warning or prior steps did the Sarkaria Commission recommend before Article 356 is invoked against a State?",
        "ஒரு மாநிலத்திற்கு எதிராக சரத்து 356-ஐப் பயன்படுத்துவதற்கு முன்பு என்ன எச்சரிக்கை அல்லது முன் நடவடிக்கைகளை சர்க்காரியா ஆணையம் பரிந்துரைத்தது?",
        "Conducting a mandatory referendum in the state capital", "மாநிலத் தலைநகரில் கட்டாய பொது வாக்கெடுப்பு நடத்துவது",
        "Securing written consent from all neighbouring State Governors", "அனைத்து அண்டை மாநில ஆளுநர்களிடமிருந்தும் எழுத்துப்பூர்வ சம்மதம் பெறுவது",
        "Imposing financial sanctions and stopping central tax devolution", "நிதித் தடைகளை விதிப்பது மற்றும் மத்திய வரிப் பகிர்வை நிறுத்துவது",
        "Issuing a prior warning to the State Government and giving it an opportunity to correct its course, unless extreme urgency precludes it", "மாநில அரசுக்கு முன் எச்சரிக்கை விடுத்து, தனது போக்கைச் சரிசெய்து கொள்ள அதற்கு வாய்ப்பளிப்பது (அவசர சூழல் தவிர)",
        "D",
        "The Sarkaria Commission strongly recommended that Article 356 must be used as a measure of last resort. Before invoking it, the Union should issue a formal warning to the errant State pointing out the constitutional infraction and giving it a fair opportunity to rectify the situation.",
        "சரத்து 356 இறுதி நடவடிக்கையாக மட்டுமே பயன்படுத்தப்பட வேண்டும் என்று சர்க்காரியா ஆணையம் கடுமையாகப் பரிந்துரைத்தது. அதனைப் பயன்படுத்துவதற்கு முன், அரசியலமைப்பு மீறலைச் சுட்டிக்காட்டி நிலைமையைச் சரிசெய்து கொள்ள நியாயமான வாய்ப்பளிக்கும் முறையான எச்சரிக்கையை மத்திய அரசு அந்த மாநிலத்திற்கு வழங்க வேண்டும்.",
        "Option A has no constitutional sanction in India.", "விருப்பம் A-க்கு அரசியலமைப்பு அதிகாரம் இல்லை.",
        "Option B is irrelevant.", "விருப்பம் B தொடர்பற்றது.",
        "Option C would unconstitutionally paralyze state finances.", "விருப்பம் C மாநில நிதியை அரசியலமைப்புக்கு முரணாக முடக்கும்.",
        "Option D is correct; prior warning and opportunity to rectify.", "விருப்பம் D சரியானது; முன் எச்சரிக்கை மற்றும் திருத்திக் கொள்ள வாய்ப்பளித்தல்.",
        "Sarkaria Golden Principle: Warning -> Opportunity to rectify -> Use of alternative remedies -> Article 356 as the absolute last resort.",
        "சர்க்காரியாவின் பொன் விதி: எச்சரிக்கை -> திருத்த வாய்ப்பு -> மாற்று வழிகளைப் பயன்படுத்துதல் -> இறுதிக் கட்டமாக சரத்து 356.",
        "The Supreme Court in S.R. Bommai explicitly incorporated this Sarkaria recommendation into constitutional jurisprudence.",
        "எஸ்.ஆர். பொம்மை வழக்கில் உச்ச நீதிமன்றம் சர்க்காரியாவின் இந்தப் பரிந்துரையை அரசியலமைப்பு சட்டக் கோட்பாடுகளில் வெளிப்படையாக இணைத்தது."
    ))

    # 046 - Key B
    qs.append(make_ep_q(
        PREFIX, 46, "Medium", "Punchhi Commission", "Localized Emergency Concept",
        "Which commission on Centre-State relations recommended the concept of 'Localised Emergency' under Articles 355 and 356?",
        "மத்திய-மாநில உறவுகள் குறித்த எந்த ஆணையம் சரத்துகள் 355 மற்றும் 356-ன் கீழ் 'உள்ளூர்மயமாக்கப்பட்ட அவசரநிலை' (Localised Emergency) என்ற கருத்தைப் பரிந்துரைத்தது?",
        "Sarkaria Commission (1988)", "சர்க்காரியா ஆணையம் (1988)",
        "Punchhi Commission (2010)", "பூஞ்சி ஆணையம் (2010)",
        "Rajamannar Committee (1971)", "ராஜமன்னார் குழு (1971)",
        "Kothari Commission (1966)", "கோத்தாரி ஆணையம் (1966)",
        "B",
        "The Punchhi Commission on Centre-State Relations (headed by former CJI M.M. Punchhi, 2010) recommended amending Articles 355 and 356 to permit 'Localised Emergency' — allowing the Centre to intervene in specific troubled areas or districts for not more than three months without dismissing the entire State Government or dissolving the Assembly.",
        "மத்திய-மாநில உறவுகளுக்கான பூஞ்சி ஆணையம் (முன்னாள் இந்திய தலைமை நீதிபதி எம்.எம். பூஞ்சி தலைமையில், 2010) சரத்துகள் 355 மற்றும் 356-ஐத் திருத்தி 'உள்ளூர்மயமாக்கப்பட்ட அவசரநிலையை' அறிமுகப்படுத்த பரிந்துரைத்தது — அதாவது முழு மாநில அரசைக் கலைக்காமல் அல்லது சட்டமன்றத்தைக் கலைக்காமல், குறிப்பிட்ட பாதிக்கப்பட்ட பகுதிகளில் மட்டும் அதிகபட்சமாக மூன்று மாதங்களுக்கு மத்திய அரசு தலையிட அனுமதிக்கலாம்.",
        "Option A recommended sparing use as last resort, but not localized emergency.", "விருப்பம் A இறுதி நடவடிக்கையாகப் பயன்படுத்தப் பரிந்துரைத்தது.",
        "Option B is correct; Punchhi Commission (2010) pioneered the Localised Emergency doctrine.", "விருப்பம் B சரியானது; பூஞ்சி ஆணையம் (2010) உள்ளூர்மயமாக்கப்பட்ட அவசரநிலைக் கோட்பாட்டை முன்மொழிந்தது.",
        "Option C recommended complete abolition of Articles 356 and 357.", "விருப்பம் C சரத்துகள் 356, 357-ஐ முற்றிலும் நீக்கப் பரிந்துரைத்தது.",
        "Option D was an education commission.", "விருப்பம் D கல்வி ஆணையம்.",
        "TNPSC Landmark Concept: 'Localised Emergency' = Punchhi Commission (2010).",
        "TNPSC மைல்கல் கருத்து: 'உள்ளூர்மயமாக்கப்பட்ட அவசரநிலை' = பூஞ்சி ஆணையம் (2010).",
        "This recommendation aimed to prevent the total disruption of state democracy when violence or unrest is localized to a single district or pocket.",
        "வன்முறை அல்லது அமைதியின்மை ஒரு குறிப்பிட்ட மாவட்டம் அல்லது பகுதிக்குள் இருக்கும் போது ஒட்டுமொத்த மாநில ஜனநாயகமும் முடங்குவதைத் தடுப்பதே இதன் நோக்கமாகும்."
    ))

    # 047 - Key A
    qs.append(make_ep_q(
        PREFIX, 47, "Hard", "Constitutional Duty", "Article 355 Union Duty",
        "What dual duty is imposed on the Union of India under Article 355 of the Constitution?",
        "அரசியலமைப்பின் சரத்து 355-ன் கீழ் இந்திய மத்திய அரசுக்கு என்ன இரட்டை கடமை விதிக்கப்பட்டுள்ளது?",
        "To protect every State against external aggression and internal disturbance, AND to ensure governance is carried on in accordance with the Constitution", "வெளிநாட்டு ஆக்கிரமிப்பு மற்றும் உள்நாட்டு அமைதியின்மையிலிருந்து ஒவ்வொரு மாநிலத்தையும் பாதுகாப்பது, மற்றும் அரசியலமைப்பு விதிகளின்படி ஆட்சி நடைபெறுவதை உறுதி செய்வது",
        "To balance state budgets and maintain uniform police forces", "மாநில வரவு-செலவுத் திட்டங்களைச் சமப்படுத்துவது மற்றும் சீரான காவல் படைகளைப் பராமரிப்பது",
        "To appoint Governors and fix ministers' salaries", "ஆளுநர்களை நியமிப்பது மற்றும் அமைச்சர்களின் ஊதியங்களை நிர்ணயிப்பது",
        "To conduct municipal elections and manage inter-state rivers", "நகராட்சித் தேர்தல்களை நடத்துவது மற்றும் மாநிலங்களுக்கு இடையேயான நதிகளை நிர்வகிப்பது",
        "A",
        "Article 355 explicitly states: 'It shall be the duty of the Union to protect every State against external aggression and internal disturbance and to ensure that the government of every State is carried on in accordance with the provisions of this Constitution.'",
        "சரத்து 355 தெளிவாகக் கூறுகிறது: 'வெளிநாட்டு ஆக்கிரமிப்பு மற்றும் உள்நாட்டு அமைதியின்மையிலிருந்து ஒவ்வொரு மாநிலத்தையும் பாதுகாப்பதும், ஒவ்வொரு மாநிலத்தின் அரசும் இந்த அரசியலமைப்பின் விதிகளுக்கு இணங்க நடத்தப்படுவதை உறுதி செய்வதும் மத்திய அரசின் கடமையாகும்.'",
        "Option A is correct; exact dual mandate of Article 355.", "விருப்பம் A சரியானது; சரத்து 355-ன் துல்லியமான இரட்டை ஆணை.",
        "Option B is incorrect.", "விருப்பம் B தவறானது.",
        "Option C mentions other constitutional provisions.", "விருப்பம் C பிற அரசியலமைப்பு விதிகளைக் குறிப்பிடுகிறது.",
        "Option D refers to state elections and Article 262.", "விருப்பம் D மாநிலத் தேர்தல் மற்றும் சரத்து 262 தொடர்பானது.",
        "Constitutional Anchor: Article 355 is the foundational duty that justifies Union intervention under Article 352, 356, and deployment of armed forces.",
        "அரசியலமைப்பு நங்கூரம்: சரத்து 352, 356 மற்றும் ஆயுதப்படைகளை அனுப்புதல் போன்ற மத்திய தலையீடுகளை நியாயப்படுத்தும் அடிப்படைக் கடமையே சரத்து 355 ஆகும்.",
        "Article 355 provides the constitutional justification for the imposition of President's Rule under Article 356.",
        "சரத்து 356-ன் கீழ் குடியரசுத் தலைவர் ஆட்சியை விதிப்பதற்கான அரசியலமைப்பு நியாயத்தை சரத்து 355 வழங்குகிறது."
    ))

    # 048 - Key C
    qs.append(make_ep_q(
        PREFIX, 48, "Medium", "Historical", "Kerala 1959 Communist Dismissal",
        "In July 1959, the elected government of Chief Minister E.M.S. Namboodiripad in Kerala was dismissed under Article 356. What made this event historically momentous?",
        "ஜூலை 1959-ல், கேரளாவில் முதலமைச்சர் இ.எம்.எஸ். நம்பூதிரிபாட் தலைமையிலான தேர்ந்தெடுக்கப்பட்ட அரசு சரத்து 356-ன் கீழ் கலைக்கப்பட்டது. இந்த நிகழ்வு வரலாற்று ரீதியாக ஏன் முக்கியத்துவம் வாய்ந்தது?",
        "It was the first time an emergency was declared on grounds of war", "போர் காரணமாக அவசரநிலை அறிவிக்கப்பட்ட முதல் நிகழ்வு இதுவாகும்",
        "It was the first time Financial Emergency was declared in India", "இந்தியாவில் நிதி அவசரநிலை அறிவிக்கப்பட்ட முதல் நிகழ்வு இதுவாகும்",
        "It was the first dismissal of a democratically elected Communist state government with assembly majority on political grounds", "சட்டமன்றப் பெரும்பான்மை கொண்ட ஜனநாயக ரீதியாகத் தேர்ந்தெடுக்கப்பட்ட கம்யூனிஸ்ட் மாநில அரசு அரசியல் காரணங்களுக்காகக் கலைக்கப்பட்ட முதல் நிகழ்வு இதுவாகும்",
        "It was the first time the Supreme Court intervened to overturn Article 356", "சரத்து 356-ஐ ரத்து செய்ய உச்ச நீதிமன்றம் தலையிட்ட முதல் நிகழ்வு இதுவாகும்",
        "C",
        "The dismissal of the EMS Namboodiripad communist government in Kerala in July 1959 was historic as the first time Article 356 was invoked to unseat a democratically elected state government enjoying a majority in the assembly, driven by political agitation (Vimochana Samaram / Liberation Struggle).",
        "ஜூலை 1959-ல் கேரளாவில் இ.எம்.எஸ். நம்பூதிரிபாட் கம்யூனிஸ்ட் அரசு கலைக்கப்பட்டது வரலாற்று முக்கியத்துவம் வாய்ந்தது; சட்டமன்றத்தில் பெரும்பான்மை ஆதரவு பெற்ற ஒரு ஜனநாயக அரசை, அரசியல் போராட்டத்தின் (விமோசன சமரம் / விடுதலைப் போராட்டம்) தூண்டுதலால் சரத்து 356-ஐப் பயன்படுத்திக் கலைத்த முதல் நிகழ்வு இதுவாகும்.",
        "Option A describes Article 352 in 1962.", "விருப்பம் A 1962 சரத்து 352-ஐ விவரிக்கிறது.",
        "Option B is false; Financial Emergency has never been declared.", "விருப்பம் B தவறு; நிதி அவசரநிலை ஒருபோதும் அறிவிக்கப்படவில்லை.",
        "Option C is correct; dismissal of the historic first communist ministry in Kerala.", "விருப்பம் C சரியானது; கேரளாவின் வரலாற்றுச் சிறப்புமிக்க முதல் கம்யூனிஸ்ட் அமைச்சரவை கலைப்பு.",
        "Option D is wrong; courts did not overturn Article 356 in 1959.", "விருப்பம் D தவறு; 1959-ல் நீதிமன்றங்கள் தலையிடவில்லை.",
        "TNPSC Landmark Event: EMS Namboodiripad ministry in Kerala (elected in 1957) was dismissed under Article 356 on July 31, 1959.",
        "TNPSC மைல்கல் நிகழ்வு: கேரளாவில் இ.எம்.எஸ். நம்பூதிரிபாட் அமைச்சரவை (1957-ல் தேர்ந்தெடுக்கப்பட்டது) ஜூலை 31, 1959 அன்று சரத்து 356-ன் கீழ் கலைக்கப்பட்டது.",
        "This set a controversial precedent for the political misuse of Article 356 by central governments over subsequent decades.",
        "அடுத்தடுத்த பத்தாண்டுகளில் மத்திய அரசுகள் சரத்து 356-ஐ அரசியல் ரீதியாகத் தவறாகப் பயன்படுத்துவதற்கு இது ஒரு சர்ச்சைக்குரிய முன்னுதாரணத்தை அமைத்தது."
    ))

    # 049 - Key D
    qs.append(make_ep_q(
        PREFIX, 49, "Hard", "Constitutional Amendment", "44th CAA Restoration of 356 Judicial Review",
        "The 38th Constitutional Amendment Act, 1975 had inserted clause (5) in Article 356 making the satisfaction of the President final and non-justiciable. Which Amendment deleted this clause to restore judicial review?",
        "1975-ன் 38-வது அரசியலமைப்பு திருத்தச் சட்டம் சரத்து 356-ல் பிரிவு (5)-ஐ இணைத்து, குடியரசுத் தலைவரின் திருப்தியை இறுதியானது மற்றும் நீதிமன்ற விசாரணைக்கு அப்பாற்பட்டது என ஆக்கியது. நீதி மறுஆய்வை மீட்டெடுக்க இந்தப் பிரிவை நீக்கிய திருத்தச் சட்டம் எது?",
        "42nd Constitutional Amendment Act, 1976", "42-வது அரசியலமைப்பு திருத்தச் சட்டம், 1976",
        "43rd Constitutional Amendment Act, 1977", "43-வது அரசியலமைப்பு திருத்தச் சட்டம், 1977",
        "45th Constitutional Amendment Act, 1980", "45-வது அரசியலமைப்பு திருத்தச் சட்டம், 1980",
        "44th Constitutional Amendment Act, 1978", "44-வது அரசியலமைப்பு திருத்தச் சட்டம், 1978",
        "D",
        "The 44th Constitutional Amendment Act of 1978 deleted clause (5) of Article 356 (which had been inserted by the 38th CAA in 1975), thereby fully restoring the jurisdiction of the Supreme Court and High Courts to examine whether the proclamation under Article 356 is based on mala fide or extraneous grounds.",
        "1978-ன் 44-வது அரசியலமைப்பு திருத்தச் சட்டம் சரத்து 356-ன் பிரிவு (5)-ஐ (1975-ல் 38-வது திருத்தத்தால் சேர்க்கப்பட்டது) நீக்கியது; இதன் மூலம் சரத்து 356 பிரகடனம் தவறான உள்நோக்கம் அல்லது தேவையற்ற காரணங்களின் அடிப்படையில் உள்ளதா என்பதை ஆய்வு செய்யும் உச்ச நீதிமன்றம் மற்றும் உயர் நீதிமன்றங்களின் அதிகார வரம்பை முழுமையாக மீட்டெடுத்தது.",
        "Option A (42nd CAA) extended the period of President's Rule from 6 months to 1 year.", "விருப்பம் A (42-வது திருத்தம்) குடியரசுத் தலைவர் ஆட்சிக் காலத்தை 6 மாதத்திலிருந்து 1 ஆண்டாக உயர்த்தியது.",
        "Option B dealt with other civil liberties.", "விருப்பம் B பிற சிவில் உரிமைகளைக் கையாண்டது.",
        "Option C extended SC/ST reservations.", "விருப்பம் C இடஒதுக்கீட்டை நீட்டித்தது.",
        "Option D is correct; the 44th CAA restored judicial review by deleting Article 356(5).", "விருப்பம் D சரியானது; 44-வது திருத்தம் சரத்து 356(5)-ஐ நீக்கி நீதி மறுஆய்வை மீட்டெடுத்தது.",
        "TNPSC Amendment History: 38th CAA (1975) barred judicial review of Art 352 & 356; 44th CAA (1978) restored judicial review of BOTH.",
        "TNPSC திருத்த வரலாறு: 38-வது திருத்தம் (1975) சரத்துகள் 352, 356-ன் நீதி மறுஆய்வைத் தடுத்தது; 44-வது திருத்தம் (1978) இரண்டின் நீதி மறுஆய்வையும் மீட்டெடுத்தது.",
        "Following this deletion, the Supreme Court laid down comprehensive review guidelines in S.R. Bommai (1994).",
        "இந்த நீக்கத்தைத் தொடர்ந்து, உச்ச நீதிமன்றம் எஸ்.ஆர். பொம்மை (1994) வழக்கில் விரிவான நீதி மறுஆய்வு வழிகாட்டுதல்களை வகுத்தது."
    ))

    # 050 - Key B
    qs.append(make_ep_q(
        PREFIX, 50, "Hard", "Comparative Polity", "Core Differences between 352 and 356",
        "Which of the following represents a fundamental constitutional distinction between a National Emergency (Article 352) and President's Rule (Article 356)?",
        "தேசிய அவசரநிலை (சரத்து 352) மற்றும் குடியரசுத் தலைவர் ஆட்சி (சரத்து 356) ஆகியவற்றுக்கு இடையேயான அடிப்படை அரசியலமைப்பு வேறுபாட்டைப் பின்வருவனவற்றில் எது சரியாகப் பிரதிபலிக்கிறது?",
        "Article 352 affects Fundamental Rights, whereas Article 356 affects them even more drastically", "சரத்து 352 அடிப்படை உரிமைகளைப் பாதிக்கிறது, ஆனால் சரத்து 356 அவற்றை இன்னும் தீவிரமாகப் பாதிக்கிறது",
        "Under Article 352, the State Legislature is NOT dissolved, whereas under Article 356, the State Legislature is either suspended or dissolved", "சரத்து 352-ன் கீழ் மாநில சட்டமன்றம் கலைக்கப்படுவதில்லை, ஆனால் சரத்து 356-ன் கீழ் மாநில சட்டமன்றம் இடைநிறுத்தப்படுகிறது அல்லது கலைக்கப்படுகிறது",
        "Article 352 requires a simple majority, while Article 356 requires a special majority", "சரத்து 352-க்கு எளிய பெரும்பான்மை தேவை, ஆனால் சரத்து 356-க்கு சிறப்புப் பெரும்பான்மை தேவை",
        "Article 352 can last for maximum 3 years, while Article 356 can last indefinitely", "சரத்து 352 அதிகபட்சம் 3 ஆண்டுகள் நீடிக்கும், ஆனால் சரத்து 356 காலவரையின்றி நீடிக்கும்",
        "B",
        "Under Article 352, the State Legislature and State Executive continue to function (though under overriding Union concurrent control). Under Article 356, the State Executive is dismissed and the State Legislature is suspended or dissolved. Additionally, Article 356 has NO effect on Fundamental Rights whatsoever.",
        "சரத்து 352-ன் கீழ், மாநில சட்டமன்றமும் மாநில நிர்வாகமும் தொடர்ந்து இயங்குகின்றன (மத்திய அரசின் மேலோங்கும் கட்டுப்பாட்டின் கீழ்). சரத்து 356-ன் கீழ், மாநில நிர்வாகம் கலைக்கப்படுகிறது மற்றும் மாநில சட்டமன்றம் இடைநிறுத்தப்படுகிறது அல்லது கலைக்கப்படுகிறது. மேலும் சரத்து 356 அடிப்படை உரிமைகளை எந்த வகையிலும் பாதிக்காது.",
        "Option A is false; Article 356 has ZERO impact on Fundamental Rights.", "விருப்பம் A தவறு; சரத்து 356 அடிப்படை உரிமைகளில் எந்தப் பாதிப்பையும் ஏற்படுத்தாது.",
        "Option B is correct; crucial operational distinction regarding state organs.", "விருப்பம் B சரியானது; மாநில அங்கங்கள் மீதான முக்கியமான செயல்பாட்டு வேறுபாடு.",
        "Option C inverts the required majorities (352 needs Special; 356 needs Simple).", "விருப்பம் C பெரும்பான்மைகளைத் தலைகீழாக மாற்றுகிறது.",
        "Option D inverts the duration limits (352 can be indefinite; 356 has a 3-year ceiling).", "விருப்பம் D கால வரம்புகளைத் தலைகீழாக மாற்றுகிறது.",
        "Golden Comparison: Article 352 = State government continues; affects FRs. Article 356 = State government dismissed; does NOT affect FRs.",
        "பொன் ஒப்பீடு: சரத்து 352 = மாநில அரசு நீடிக்கிறது, உரிமைகள் பாதிக்கப்படுகின்றன. சரத்து 356 = மாநில அரசு கலைக்கப்படுகிறது, உரிமைகள் பாதிக்கப்படுவதில்லை.",
        "Understanding this sharp contrast is one of the most frequently tested areas in TNPSC Group 1 and UPSC Prelims.",
        "இந்தக் கூர்மையான வேறுபாட்டைப் புரிந்துகொள்வது TNPSC குரூப் 1 மற்றும் UPSC தேர்வுகளில் அடிக்கடி கேட்கப்படும் முதன்மையான பகுதியாகும்."
    ))

    return qs

print("Batch 2 (Q026-Q050) ready.")
