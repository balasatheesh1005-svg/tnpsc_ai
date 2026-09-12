# -*- coding: utf-8 -*-
"""
Builder for Inter-State Relations PYQ Practice Part 2 (ISR_PYQ_026 to ISR_PYQ_050)
"""
import json
from build_isr_pyq_part1 import make_pyq

def get_pyq_part2():
    q = []

    # 026 - Ans B (TNPSC Group 1 2017)
    q.append(make_pyq(
        "ISR_PYQ_026", "Medium",
        "[TNPSC Group 1] In which year did the Supreme Court deliver the historic Automobile Transport (Rajasthan) v. State of Rajasthan judgment introducing the compensatory tax doctrine?",
        "[TNPSC குரூப் 1] ஈட்டு வரிக் கோட்பாட்டை (compensatory tax doctrine) அறிமுகப்படுத்திய வரலாற்றுச் சிறப்புமிக்க ஆட்டோமொபைல் டிரான்ஸ்போர்ட் (ராஜஸ்தான்) எதிர் ராஜஸ்தான் மாநிலம் வழக்கில் உச்ச நீதிமன்றம் எந்த ஆண்டு தீர்ப்பளித்தது?",
        "1960", "1960",
        "1962", "1962",
        "1965", "1965",
        "1970", "1970",
        "B",
        "The 7-judge Constitution Bench of the Supreme Court delivered the landmark Automobile Transport (Rajasthan) Ltd. v. State of Rajasthan judgment in 1962 (AIR 1962 SC 1406), upholding compensatory taxes under Article 301.",
        "உச்ச நீதிமன்றத்தின் 7 நீதிபதிகள் கொண்ட அரசியலமைப்பு அமர்வு 1962-ல் ஆட்டோமொபைல் டிரான்ஸ்போர்ட் (ராஜஸ்தான்) வழக்கில் தீர்ப்பளித்தது; இதில் உறுப்பு 301-ன் கீழ் வர்த்தகத்தை எளிதாக்கும் ஈட்டு வரிகள் செல்லும் என அறிவித்தது.",
        "Option A is incorrect because 1960 was before the 7-judge bench ruling.", "1960 தீர்ப்பிற்கு முந்தைய ஆண்டு என்பதால் விருப்பம் A தவறு.",
        "Option B is correct because the landmark judgment was rendered in 1962.", "வரலாற்றுத் தீர்ப்பு 1962-ல் வழங்கப்பட்டதால் விருப்பம் B சரி.",
        "Option C is incorrect because 1965 was later.", "1965 பிந்தைய ஆண்டு என்பதால் விருப்பம் C தவறு.",
        "Option D is incorrect because 1970 is inaccurate.", "1970 தவறான ஆண்டு என்பதால் விருப்பம் D தவறு.",
        "Remember the landmark trade cases: Atiabari (1961) -> Automobile Transport (1962) -> Jindal Stainless (2017).",
        "முக்கிய வர்த்தக வழக்குகளை நினைவில் கொள்க: அத்தியாபாரி (1961) -> ஆட்டோமொபைல் டிரான்ஸ்போர்ட் (1962) -> ஜிண்டால் ஸ்டெயின்லெஸ் (2017).",
        "Automobile Transport (Rajasthan) judgment establishing the compensatory tax doctrine was delivered in 1962.",
        "ஈட்டு வரிக் கோட்பாட்டை நிறுவிய ஆட்டோமொபைல் டிரான்ஸ்போர்ட் தீர்ப்பு 1962-ல் வழங்கப்பட்டது.",
        tags=["Automobile Transport 1962", "Compensatory Tax", "TNPSC PYQ"]
    ))

    # 027 - Ans C (TNPSC Group 1 2022)
    q.append(make_pyq(
        "ISR_PYQ_027", "Hard",
        "[TNPSC Group 1] In 2017, a 9-judge Constitution Bench of the Supreme Court overruled the 'compensatory tax doctrine' and upheld the validity of State entry taxes in which case?",
        "[TNPSC குரூப் 1] 2017-ல், உச்ச நீதிமன்றத்தின் 9 நீதிபதிகள் கொண்ட அரசியலமைப்பு அமர்வு 'ஈட்டு வரிக் கோட்பாட்டை' ரத்து செய்து மாநில நுழைவு வரிகளின் செல்லுபடியாகும் தன்மையை எந்த வழக்கில் உறுதி செய்தது?",
        "Kesavananda Bharati v. State of Kerala", "கேசவாநந்த பாரதி எதிர் கேரள மாநிலம்",
        "S.R. Bommai v. Union of India", "எஸ்.ஆர். பொம்மை எதிர் இந்திய ஒன்றியம்",
        "Jindal Stainless Ltd. v. State of Haryana", "ஜிண்டால் ஸ்டெயின்லெஸ் லிமிடெட் எதிர் ஹரியானா மாநிலம்",
        "I.R. Coelho v. State of Tamil Nadu", "ஐ.ஆர். கோயல்ஹோ எதிர் தமிழ்நாடு மாநிலம்",
        "C",
        "In Jindal Stainless Ltd. v. State of Haryana (2017), a 9-judge Constitution Bench headed by CJI T.S. Thakur overruled the 1962 Automobile Transport compensatory tax test by a 7:2 majority, ruling that non-discriminatory entry tax under Article 304(a) does not violate Article 301.",
        "ஜிண்டால் ஸ்டெயின்லெஸ் லிமிடெட் எதிர் ஹரியானா மாநிலம் (2017) வழக்கில், தலைமை நீதிபதி டி.எஸ். தாக்கூர் தலைமையிலான 9 நீதிபதிகள் அமர்வு 1962 ஆட்டோமொபைல் தீர்ப்பை ரத்து செய்தது; பாகுபாடற்ற நுழைவு வரி உறுப்பு 301-ஐ மீறாது என்று தீர்ப்பளித்தது.",
        "Option A is incorrect because Kesavananda Bharati (1973) established the Basic Structure doctrine.", "கேசவாநந்த பாரதி அடிப்படை கட்டமைப்புக் கோட்பாட்டிற்குரியது என்பதால் விருப்பம் A தவறு.",
        "Option B is incorrect because S.R. Bommai (1994) dealt with Article 356 federalism.", "எஸ்.ஆர். பொம்மை உறுப்பு 356-க்குரியது என்பதால் விருப்பம் B தவறு.",
        "Option C is correct because Jindal Stainless (2017) is the historic 9-judge bench ruling on entry tax and Article 301.", "ஜிண்டால் ஸ்டெயின்லெஸ் வழக்கே நுழைவு வரி மற்றும் உறுப்பு 301 குறித்த 9 நீதிபதிகள் அமர்வு தீர்ப்பாகும் என்பதால் விருப்பம் C சரி.",
        "Option D is incorrect because I.R. Coelho (2007) dealt with the Ninth Schedule.", "ஐ.ஆர். கோயல்ஹோ ஒன்பதாவது அட்டவணைக்குரியது என்பதால் விருப்பம் D தவறு.",
        "Jindal Stainless Ltd. (2017): 9-judge bench discarded compensatory tax doctrine, upholding entry tax under Article 304(a).",
        "ஜிண்டால் ஸ்டெயின்லெஸ் (2017): 9 நீதிபதிகள் அமர்வு ஈட்டு வரிக் கோட்பாட்டை ரத்து செய்து, உறுப்பு 304(a)-ன் கீழ் நுழைவு வரியை உறுதி செய்தது.",
        "Jindal Stainless (2017) 9-judge bench discarded the compensatory tax test and upheld entry taxes.",
        "ஜிண்டால் ஸ்டெயின்லெஸ் (2017) வழக்கில் 9 நீதிபதிகள் அமர்வு ஈட்டு வரிக் கோட்பாட்டை ரத்து செய்து நுழைவு வரியை உறுதி செய்தது.",
        tags=["Jindal Stainless 2017", "9-Judge Bench", "Entry Tax Landmark"]
    ))

    # 028 - Ans D (TNPSC Group 1 2019)
    q.append(make_pyq(
        "ISR_PYQ_028", "Medium",
        "[TNPSC Group 1] Which Commission on Centre-State Relations recommended that the Inter-State Council should be renamed as the 'Inter-Governmental Council'?",
        "[TNPSC குரூப் 1] மாநிலங்களுக்கு இடையிலான மன்றத்தை 'அரசாங்கங்களுக்கு இடையிலான மன்றம்' (Inter-Governmental Council) என்று பெயர் மாற்ற வேண்டும் என்று பரிந்துரைத்த மத்திய-மாநில உறவுகள் ஆணையம் எது?",
        "Kothari Commission", "கோத்தாரி ஆணையம்",
        "Mandal Commission", "மண்டல் ஆணையம்",
        "Verma Commission", "வர்மா ஆணையம்",
        "Sarkaria Commission", "சர்க்காரியா ஆணையம்",
        "D",
        "The Sarkaria Commission on Centre-State Relations (1988) explicitly recommended that the council to be established under Article 263 should be called the 'Inter-Governmental Council' to distinguish it from other councils created under that Article.",
        "மத்திய-மாநில உறவுகள் குறித்த சர்க்காரியா ஆணையம் (1988), உறுப்பு 263-ன் கீழ் பிற விவகாரங்களுக்காக அமைக்கப்பட்ட பிற மன்றங்களிலிருந்து வேறுபடுத்திக் காட்ட இதற்கு 'அரசாங்கங்களுக்கு இடையிலான மன்றம்' என்று பெயரிட வேண்டும் எனப் பரிந்துரைத்தது.",
        "Option A is incorrect because Kothari Commission was on Education (1964-66).", "கோத்தாரி ஆணையம் கல்விக்கானது என்பதால் விருப்பம் A தவறு.",
        "Option B is incorrect because Mandal Commission was on Backward Classes (1979-80).", "மண்டல் ஆணையம் பிற்படுத்தப்பட்ட வகுப்பினருக்கானது என்பதால் விருப்பம் B தவறு.",
        "Option C is incorrect because Verma Commission dealt with electoral laws / criminal law amendments.", "வர்மா ஆணையம் குற்றவியல் சட்டங்களுக்கானது என்பதால் விருப்பம் C தவறு.",
        "Option D is correct because the Sarkaria Commission recommended the name 'Inter-Governmental Council'.", "சர்க்காரியா ஆணையமே 'அரசாங்கங்களுக்கு இடையிலான மன்றம்' என்ற பெயரைப் பரிந்துரைத்தது என்பதால் விருப்பம் D சரி.",
        "Sarkaria Commission recommended: Set up permanent council under Article 263 and call it 'Inter-Governmental Council'.",
        "சர்க்காரியா ஆணைய பரிந்துரை: உறுப்பு 263-ன் கீழ் நிரந்தர மன்றத்தை அமைத்து, அதற்கு 'அரசாங்கங்களுக்கு இடையிலான மன்றம்' எனப் பெயரிடுக.",
        "Sarkaria Commission suggested designating the Inter-State Council as the Inter-Governmental Council.",
        "சர்க்காரியா ஆணையம் மாநிலங்களுக்கு இடையிலான மன்றத்தை அரசாங்கங்களுக்கு இடையிலான மன்றம் எனப் பெயரிடப் பரிந்துரைத்தது.",
        tags=["Sarkaria Commission", "Inter-Governmental Council", "TNPSC PYQ"]
    ))

    # 029 - Ans A (TNPSC Group 2 2018)
    q.append(make_pyq(
        "ISR_PYQ_029", "Easy",
        "[TNPSC Group 2] In which of the following years was the River Boards Act passed by the Parliament of India?",
        "[TNPSC குரூப் 2] பின்வரும் எந்த ஆண்டில் இந்திய நாடாளுமன்றத்தால் நதி வாரியங்கள் சட்டம் இயற்றப்பட்டது?",
        "1956", "1956",
        "1960", "1960",
        "1965", "1965",
        "1972", "1972",
        "A",
        "The River Boards Act, 1956 was enacted by Parliament under Entry 56 of the Union List (List I) for the regulation and development of inter-State rivers and river valleys on request of State governments.",
        "மாநிலங்களுக்கு இடையிலான நதிகள் மற்றும் நதிப் பள்ளத்தாக்குகளை ஒழுங்குபடுத்தவும் மேம்படுத்தவும் மத்தியப் பட்டியல் பதிவு 56-ன் கீழ் 1956-ஆம் ஆண்டில் நதி வாரியங்கள் சட்டம் நாடாளுமன்றத்தால் இயற்றப்பட்டது.",
        "Option A is correct because the River Boards Act was passed in 1956 alongside the IRWD Act.", "IRWD சட்டத்துடன் சேர்த்து நதி வாரியங்கள் சட்டமும் 1956-ல் இயற்றப்பட்டதால் விருப்பம் A சரி.",
        "Option B is incorrect because 1960 was the year of the Indus Waters Treaty.", "1960 சிந்து நதி ஒப்பந்த ஆண்டு என்பதால் விருப்பம் B தவறு.",
        "Option C is incorrect because 1965 is inaccurate.", "1965 தவறான ஆண்டு என்பதால் விருப்பம் C தவறு.",
        "Option D is incorrect because 1972 was the Wildlife Protection Act.", "1972 வனவிலங்கு பாதுகாப்புச் சட்டம் இயற்றப்பட்ட ஆண்டு என்பதால் விருப்பம் D தவறு.",
        "Parliament passed two crucial inter-state water statutes in 1956: IRWD Act (Art 262) and River Boards Act (Entry 56).",
        "1956-ல் இரண்டு முக்கிய நதிநீர்ச் சட்டங்கள் இயற்றப்பட்டன: IRWD சட்டம் (உறுப்பு 262) மற்றும் நதி வாரியங்கள் சட்டம் (பதிவு 56).",
        "River Boards Act was enacted in 1956 under Entry 56 of the Union List.",
        "மத்தியப் பட்டியல் பதிவு 56-ன் கீழ் 1956-ல் நதி வாரியங்கள் சட்டம் இயற்றப்பட்டது.",
        tags=["River Boards Act 1956", "Entry 56", "TNPSC PYQ"]
    ))

    # 030 - Ans B (TNPSC Group 1 2017)
    q.append(make_pyq(
        "ISR_PYQ_030", "Medium",
        "[TNPSC Group 1] Which of the following river water disputes tribunals was the earliest to be constituted in India?",
        "[TNPSC குரூப் 1] இந்தியாவில் முதன்முதலில் அமைக்கப்பட்ட நதிநீர் தகராறுகள் தீர்ப்பாயம் பின்வருவனவற்றில் எது?",
        "Cauvery Water Disputes Tribunal", "காவிரி நதிநீர் தகராறுகள் தீர்ப்பாயம்",
        "Krishna Water Disputes Tribunal (KWDT-I)", "கிருஷ்ணா நதிநீர் தகராறுகள் தீர்ப்பாயம் (KWDT-I)",
        "Ravi and Beas Waters Tribunal", "ராவி மற்றும் பியாஸ் நதிநீர் தீர்ப்பாயம்",
        "Mahanadi Water Disputes Tribunal", "மகாநதி நதிநீர் தகராறுகள் தீர்ப்பாயம்",
        "B",
        "The Krishna Water Disputes Tribunal (along with Godavari and Narmada) was constituted in April 1969, making it among the earliest. By contrast, Ravi-Beas was set up in 1986, Cauvery in 1990, and Mahanadi in 2018.",
        "கிருஷ்ணா நதிநீர் தீர்ப்பாயம் (கோதாவரி மற்றும் நர்மதாவுடன்) 1969 ஏப்ரலில் அமைக்கப்பட்டது; இதுவே மிக முந்தையதாகும். ராவி-பியாஸ் 1986-லும், காவிரி 1990-லும், மகாநதி 2018-லும் அமைக்கப்பட்டன.",
        "Option A is incorrect because Cauvery Tribunal was constituted in 1990.", "காவிரி தீர்ப்பாயம் 1990-ல் அமைக்கப்பட்டதால் விருப்பம் A தவறு.",
        "Option B is correct because Krishna Tribunal-I was constituted in April 1969.", "முதல் கிருஷ்ணா தீர்ப்பாயம் 1969 ஏப்ரலில் அமைக்கப்பட்டதால் விருப்பம் B சரி.",
        "Option C is incorrect because Ravi & Beas Tribunal was formed in 1986.", "ராவி-பியாஸ் தீர்ப்பாயம் 1986-ல் அமைக்கப்பட்டதால் விருப்பம் C தவறு.",
        "Option D is incorrect because Mahanadi Tribunal was formed in 2018.", "மகாநதி தீர்ப்பாயம் 2018-ல் அமைக்கப்பட்டதால் விருப்பம் D தவறு.",
        "Earliest tribunals (1969): Krishna (Bachawat), Godavari (Bachawat), Narmada (Ramaswami).",
        "முந்தைய தீர்ப்பாயங்கள் (1969): கிருஷ்ணா (பச்சாவத்), கோதாவரி (பச்சாவத்), நர்மதா (ராமசுவாமி).",
        "Krishna Water Disputes Tribunal (KWDT-I) was constituted in April 1969 under Justice R.S. Bachawat.",
        "முதல் கிருஷ்ணா நதிநீர் தீர்ப்பாயம் 1969 ஏப்ரலில் நீதிபதி ஆர்.எஸ். பச்சாவத் தலைமையில் அமைக்கப்பட்டது.",
        tags=["Earliest Tribunal 1969", "Krishna Tribunal", "TNPSC PYQ"]
    ))

    # 031 - Ans C (TNPSC Group 1 2021)
    q.append(make_pyq(
        "ISR_PYQ_031", "Hard",
        "[TNPSC Group 1] In 2018, which inter-State water dispute tribunal was constituted under the chairmanship of Justice A.M. Khanwilkar?",
        "[TNPSC குரூப் 1] 2018-ல், நீதிபதி ஏ.எம். கான்வில்கர் தலைமையில் அமைக்கப்பட்ட மாநிலங்களுக்கு இடையேயான நதிநீர் தகராறுகள் தீர்ப்பாயம் எது?",
        "Mahadayi Water Disputes Tribunal", "மகதாயி நதிநீர் தகராறுகள் தீர்ப்பாயம்",
        "Vansadhara Water Disputes Tribunal", "வம்சதாரா நதிநீர் தகராறுகள் தீர்ப்பாயம்",
        "Mahanadi Water Disputes Tribunal", "மகாநதி நதிநீர் தகராறுகள் தீர்ப்பாயம்",
        "Cauvery Water Disputes Tribunal", "காவிரி நதிநீர் தகராறுகள் தீர்ப்பாயம்",
        "C",
        "The Mahanadi Water Disputes Tribunal was constituted by the Central Government on 12th March 2018 under Justice A.M. Khanwilkar (Supreme Court judge) to resolve the river dispute between Odisha and Chhattisgarh.",
        "ஒடிசா மற்றும் சத்தீஸ்கர் இடையேயான நதிநீர் தகராறைத் தீர்க்க உச்ச நீதிமன்ற நீதிபதி ஏ.எம். கான்வில்கர் தலைமையில் 2018 மார்ச் 12 அன்று மகாநதி நதிநீர் தீர்ப்பாயம் அமைக்கப்பட்டது.",
        "Option A is incorrect because Mahadayi Tribunal was formed in 2010 under Justice J.M. Panchal.", "மகதாயி தீர்ப்பாயம் 2010-ல் நீதிபதி பஞ்சால் தலைமையில் அமைக்கப்பட்டதால் விருப்பம் A தவறு.",
        "Option B is incorrect because Vansadhara Tribunal was formed in 2010 under Justice Mukundakam Sharma.", "வம்சதாரா தீர்ப்பாயம் 2010-ல் நீதிபதி சர்மா தலைமையில் அமைக்கப்பட்டதால் விருப்பம் B தவறு.",
        "Option C is correct because the Mahanadi Tribunal was constituted in 2018 under Justice Khanwilkar.", "மகாநதி தீர்ப்பாயம் 2018-ல் நீதிபதி கான்வில்கர் தலைமையில் அமைக்கப்பட்டதால் விருப்பம் C சரி.",
        "Option D is incorrect because Cauvery Tribunal was constituted in 1990 under Justice Chittatosh Mookerjee.", "காவிரி தீர்ப்பாயம் 1990-ல் அமைக்கப்பட்டதால் விருப்பம் D தவறு.",
        "Recent Tribunal: Mahanadi Tribunal (2018) headed by Justice A.M. Khanwilkar (Odisha vs Chhattisgarh).",
        "சமீபத்திய தீர்ப்பாயம்: மகாநதி தீர்ப்பாயம் (2018) நீதிபதி ஏ.எம். கான்வில்கர் தலைமையில் (ஒடிசா vs சத்தீஸ்கர்).",
        "Mahanadi Tribunal was constituted in March 2018 chaired by Justice A.M. Khanwilkar.",
        "மகாநதி தீர்ப்பாயம் 2018 மார்ச்சில் நீதிபதி ஏ.எம். கான்வில்கர் தலைமையில் அமைக்கப்பட்டது.",
        tags=["Mahanadi Tribunal 2018", "Justice Khanwilkar", "TNPSC PYQ"]
    ))

    # 032 - Ans D (TNPSC Group 1 2015)
    q.append(make_pyq(
        "ISR_PYQ_032", "Medium",
        "[TNPSC Group 1] Which Article of the Indian Constitution empowers Parliament to impose restrictions on the freedom of trade, commerce, and intercourse in the public interest?",
        "[TNPSC குரூப் 1] பொது நலன் கருதி வர்த்தகம், வணிகம் மற்றும் தொடர்பு சுதந்திரத்தின் மீது கட்டுப்பாடுகளை விதிக்க நாடாளுமன்றத்திற்கு அதிகாரம் அளிக்கும் இந்திய அரசியலமைப்பு உறுப்பு எது?",
        "Article 300A", "உறுப்பு 300A",
        "Article 301", "உறுப்பு 301",
        "Article 303", "உறுப்பு 303",
        "Article 302", "உறுப்பு 302",
        "D",
        "Article 302 of the Indian Constitution provides that 'Parliament may by law impose such restrictions on the freedom of trade, commerce or intercourse between one State and another or within any part of the territory of India as may be required in the public interest'.",
        "இந்திய அரசியலமைப்பின் 302-வது உறுப்பு, பொது நலனுக்குத் தேவைப்படும் பட்சத்தில் மாநிலங்களுக்கு இடையேயான அல்லது இந்தியாவின் எந்தப் பகுதிக்குள்ளான வர்த்தகம், வணிகம் அல்லது தொடர்பு சுதந்திரத்தின் மீது நாடாளுமன்றம் சட்டத்தின் மூலம் கட்டுப்பாடுகளை விதிக்கலாம் என்று கூறுகிறது.",
        "Option A is incorrect because Article 300A relates to the right to property.", "உறுப்பு 300A சொத்துரிமைக்குரியது என்பதால் விருப்பம் A தவறு.",
        "Option B is incorrect because Article 301 declares the freedom of trade, not parliamentary restrictions.", "உறுப்பு 301 வர்த்தக சுதந்திரத்தை அறிவிக்கிறது, கட்டுப்பாடுகளை அல்ல என்பதால் விருப்பம் B தவறு.",
        "Option C is incorrect because Article 303 forbids preference between states.", "உறுப்பு 303 பாகுபாடு காட்டுவதைத் தடை செய்கிறது என்பதால் விருப்பம் C தவறு.",
        "Option D is correct because Article 302 directly empowers Parliament to impose public interest restrictions.", "உறுப்பு 302 பொது நலன் கருதி நாடாளுமன்றத்திற்கு வர்த்தகக் கட்டுப்பாட்டு அதிகாரம் அளிப்பதால் விருப்பம் D சரி.",
        "Article 301 grants trade freedom; Article 302 permits Parliament to impose public interest restrictions.",
        "உறுப்பு 301 வர்த்தக சுதந்திரம் அளிக்கிறது; உறுப்பு 302 நாடாளுமன்றம் பொது நலன் கருதி கட்டுப்பாடுகள் விதிக்க அனுமதிக்கிறது.",
        "Article 302 empowers Parliament to enact laws restricting trade in the public interest.",
        "பொது நலன் கருதி வர்த்தகத்தைக் கட்டுப்படுத்தும் சட்டங்களை இயற்ற உறுப்பு 302 நாடாளுமன்றத்திற்கு அதிகாரம் அளிக்கிறது.",
        tags=["Article 302", "Parliamentary Restriction", "Public Interest"]
    ))

    # 033 - Ans A (UPSC CSE 2011 / TNPSC 2018)
    q.append(make_pyq(
        "ISR_PYQ_033", "Hard",
        "[UPSC CSE / TNPSC Group 1] Which Article of the Constitution of India provides for the appointment of an authority for carrying out the purposes of Articles 301 to 304 relating to trade and commerce?",
        "[UPSC CSE / TNPSC குரூப் 1] வர்த்தகம் மற்றும் வணிகம் தொடர்பான உறுப்புகள் 301 முதல் 304 வரையிலான நோக்கங்களை நிறைவேற்ற ஓர் அதிகார அமைப்பை நியமிக்க இந்திய அரசியலமைப்பின் எந்த உறுப்பு வகை செய்கிறது?",
        "Article 307", "உறுப்பு 307",
        "Article 306", "உறுப்பு 306",
        "Article 305", "உறுப்பு 305",
        "Article 263", "உறுப்பு 263",
        "A",
        "Article 307 empowers Parliament by law to appoint such authority as it considers appropriate for carrying out the purposes of Articles 301, 302, 303 and 304, and confer on that authority such powers and duties as it thinks necessary.",
        "உறுப்புகள் 301 முதல் 304 வரையிலான நோக்கங்களை நிறைவேற்ற பொருத்தமான ஓர் அதிகார அமைப்பை நாடாளுமன்றம் சட்டத்தின் மூலம் நியமிக்கலாம் என்று உறுப்பு 307 கூறுகிறது.",
        "Option A is correct because Article 307 is the trade authority appointment provision.", "உறுப்பு 307 வர்த்தக அதிகார அமைப்பை நியமிக்கும் விதி என்பதால் விருப்பம் A சரி.",
        "Option B is incorrect because Article 306 was repealed by the Constitution (Seventh Amendment) Act, 1956.", "உறுப்பு 306 ஏழாவது திருத்தத்தால் நீக்கப்பட்டது என்பதால் விருப்பம் B தவறு.",
        "Option C is incorrect because Article 305 relates to saving of state monopolies.", "உறுப்பு 305 அரசு ஏகபோகங்களைப் பாதுகாப்பதால் விருப்பம் C தவறு.",
        "Option D is incorrect because Article 263 relates to the Inter-State Council.", "உறுப்பு 263 மாநிலங்களுக்கு இடையிலான மன்றத்திற்குரியது என்பதால் விருப்பம் D தவறு.",
        "Article 307 is the constitutional basis for an Inter-State Trade and Commerce Authority (analogous to the US ICC).",
        "உறுப்பு 307 மாநிலங்களுக்கு இடையிலான வர்த்தக அதிகார அமைப்பிற்கான அரசியலமைப்பு அடிப்படையாகும்.",
        "Article 307 allows Parliament to establish a statutory authority to enforce trade and commerce provisions.",
        "வர்த்தக விதிகளை அமல்படுத்த ஓர் அதிகார அமைப்பை நியமிக்க நாடாளுமன்றத்திற்கு உறுப்பு 307 அதிகாரம் அளிக்கிறது.",
        tags=["Article 307", "Trade Authority", "TNPSC PYQ"]
    ))

    # 034 - Ans B (TNPSC Group 1 2017)
    q.append(make_pyq(
        "ISR_PYQ_034", "Medium",
        "[TNPSC Group 1] The Ravi and Beas Waters Tribunal was constituted in 1986 in accordance with which historic accord?",
        "[TNPSC குரூப் 1] 1986-ல் ராவி மற்றும் பியாஸ் நதிநீர் தீர்ப்பாயம் எந்த வரலாற்றுச் சிறப்புமிக்க ஒப்பந்தத்தின் அடிப்படையில் அமைக்கப்பட்டது?",
        "Indus Waters Treaty (1960)", "சிந்து நதிநீர் ஒப்பந்தம் (1960)",
        "Rajiv–Longowal Accord (Punjab Accord, 1985)", "ராஜீவ்-லாங்கோவால் ஒப்பந்தம் (பஞ்சாப் ஒப்பந்தம், 1985)",
        "Ganga Water Treaty (1996)", "கங்கை நதிநீர் ஒப்பந்தம் (1996)",
        "Assam Accord (1985)", "அசாம் ஒப்பந்தம் (1985)",
        "B",
        "Clause 9 of the historic Punjab Accord (Rajiv-Longowal Accord) signed on 24 July 1985 provided for the verification of water claims of Punjab and Haryana by a Supreme Court judge. In pursuance of this accord, the Eradi Tribunal was constituted in April 1986.",
        "1985 ஜூலை 24 அன்று கையெழுத்தான வரலாற்றுச் சிறப்புமிக்க பஞ்சாப் ஒப்பந்தத்தின் (ராஜீவ்-லாங்கோவால் ஒப்பந்தம்) பிரிவு 9-ன் படி, உச்ச நீதிமன்ற நீதிபதி தலைமையில் பஞ்சாப்-ஹரியானா நீர் உரிமைகளை ஆராய எராடி தீர்ப்பாயம் 1986 ஏப்ரலில் அமைக்கப்பட்டது.",
        "Option A is incorrect because the Indus Waters Treaty was between India and Pakistan.", "சிந்து நதி ஒப்பந்தம் இந்தியா-பாகிஸ்தான் இடையேயானது என்பதால் விருப்பம் A தவறு.",
        "Option B is correct because the Rajiv-Longowal Accord was the direct genesis of the 1986 Tribunal.", "ராஜீவ்-லாங்கோவால் ஒப்பந்தமே 1986 தீர்ப்பாயத்தின் நேரடித் தோற்றம் என்பதால் விருப்பம் B சரி.",
        "Option C is incorrect because the Ganga Water Treaty was with Bangladesh.", "கங்கை ஒப்பந்தம் வங்காளதேசத்துடனானது என்பதால் விருப்பம் C தவறு.",
        "Option D is incorrect because the Assam Accord dealt with foreigners/citizenship issues in Assam.", "அசாம் ஒப்பந்தம் வெளிநாட்டினர் பிரச்சினைக்குரியது என்பதால் விருப்பம் D தவறு.",
        "Ravi-Beas Waters Tribunal (1986, Eradi) was born out of the Rajiv-Longowal Punjab Accord of 1985.",
        "ராவி-பியாஸ் தீர்ப்பாயம் (1986, எராடி) 1985-ன் ராஜீவ்-லாங்கோவால் பஞ்சாப் ஒப்பந்தத்தின் மூலம் உருவானது.",
        "The Rajiv-Longowal Accord of 1985 mandated the constitution of the Ravi & Beas Waters Tribunal.",
        "1985-ன் ராஜீவ்-லாங்கோவால் ஒப்பந்தம் ராவி-பியாஸ் நதிநீர் தீர்ப்பாயத்தை அமைக்க உத்தரவிட்டது.",
        tags=["Rajiv Longowal Accord", "Ravi Beas Tribunal", "Eradi Commission"]
    ))

    # 035 - Ans C (TNPSC Group 1 2021)
    q.append(make_pyq(
        "ISR_PYQ_035", "Hard",
        "[TNPSC Group 1] In 2010, the Mahadayi Water Disputes Tribunal was constituted under the chairmanship of which judge?",
        "[TNPSC குரூப் 1] 2010-ல், எந்த நீதிபதியின் தலைமையில் மகதாயி நதிநீர் தகராறுகள் தீர்ப்பாயம் அமைக்கப்பட்டது?",
        "Justice Chittatosh Mookerjee", "நீதிபதி சிட்டதோஷ் முகர்ஜி",
        "Justice Brijesh Kumar", "நீதிபதி பிரிஜேஷ் குமார்",
        "Justice J.M. Panchal", "நீதிபதி ஜே.எம். பஞ்சால்",
        "Justice Mukundakam Sharma", "நீதிபதி முகுந்தகம் சர்மா",
        "C",
        "The Mahadayi Water Disputes Tribunal was constituted on 16th November 2010 under the chairmanship of Justice J.M. Panchal (Supreme Court judge) to resolve the water dispute between Goa, Karnataka, and Maharashtra.",
        "கோவா, கர்நாடகா மற்றும் மகாராஷ்டிரா இடையேயான நதிநீர் தகராறைத் தீர்க்க உச்ச நீதிமன்ற நீதிபதி ஜே.எம். பஞ்சால் தலைமையில் 2010 நவம்பர் 16 அன்று மகதாயி தீர்ப்பாயம் அமைக்கப்பட்டது.",
        "Option A is incorrect because Justice Chittatosh Mookerjee chaired the Cauvery Tribunal (1990).", "நீதிபதி முகர்ஜி காவிரி தீர்ப்பாயத்திற்குத் (1990) தலைமை தாங்கினார் என்பதால் விருப்பம் A தவறு.",
        "Option B is incorrect because Justice Brijesh Kumar chaired KWDT-II (2004).", "நீதிபதி பிரிஜேஷ் குமார் இரண்டாவது கிருஷ்ணா தீர்ப்பாயத்திற்குத் (2004) தலைமை தாங்கினார் என்பதால் விருப்பம் B தவறு.",
        "Option C is correct because Justice J.M. Panchal chaired the Mahadayi Tribunal.", "நீதிபதி ஜே.எம். பஞ்சால் மகதாயி தீர்ப்பாயத்திற்குத் தலைமை தாங்கியதால் விருப்பம் C சரி.",
        "Option D is incorrect because Justice Mukundakam Sharma chaired the Vansadhara Tribunal (2010).", "நீதிபதி முகுந்தகம் சர்மா வம்சதாரா தீர்ப்பாயத்திற்குத் தலைமை தாங்கினார் என்பதால் விருப்பம் D தவறு.",
        "Chairpersons match: Cauvery = Mookerjee; Krishna-II = Brijesh Kumar; Mahadayi = Panchal; Vansadhara = Sharma.",
        "தலைவர்கள் பொருத்துக: காவிரி = முகர்ஜி; கிருஷ்ணா-II = பிரிஜேஷ் குமார்; மகதாயி = பஞ்சால்; வம்சதாரா = சர்மா.",
        "Mahadayi Water Disputes Tribunal was chaired by Justice J.M. Panchal (constituted 2010).",
        "மகதாயி நதிநீர் தீர்ப்பாயம் நீதிபதி ஜே.எம். பஞ்சால் தலைமையில் 2010-ல் அமைக்கப்பட்டது.",
        tags=["Mahadayi Tribunal", "Justice Panchal", "TNPSC PYQ"]
    ))

    # 036 - Ans C (TNPSC Group 1 2019)
    q.append(make_pyq(
        "ISR_PYQ_036", "Medium",
        "[TNPSC Group 1] Which of the following States is a member of the Central Zonal Council?",
        "[TNPSC குரூப் 1] பின்வரும் மாநிலங்களில் மத்திய மண்டலக் குழுவின் உறுப்பினர் எது?",
        "Bihar", "பீகார்",
        "Jharkhand", "ஜார்க்கண்ட்",
        "Chhattisgarh", "சத்தீஸ்கர்",
        "Odisha", "ஒடிசா",
        "C",
        "The Central Zonal Council comprises Uttar Pradesh, Madhya Pradesh, Uttarakhand, and Chhattisgarh. Bihar, Jharkhand, and Odisha are members of the Eastern Zonal Council.",
        "மத்திய மண்டலக் குழுவில் உத்தரப் பிரதேசம், மத்தியப் பிரதேசம், உத்தராகண்ட் மற்றும் சத்தீஸ்கர் ஆகியவை உறுப்பினர்களாக உள்ளன. பீகார், ஜார்க்கண்ட், ஒடிசா ஆகியவை கிழக்கு மண்டலக் குழுவில் உள்ளன.",
        "Option A is incorrect because Bihar belongs to the Eastern Zone.", "பீகார் கிழக்கு மண்டலத்தைச் சேர்ந்தது என்பதால் விருப்பம் A தவறு.",
        "Option B is incorrect because Jharkhand belongs to the Eastern Zone.", "ஜார்க்கண்ட் கிழக்கு மண்டலத்தைச் சேர்ந்தது என்பதால் விருப்பம் B தவறு.",
        "Option C is correct because Chhattisgarh is a member of the Central Zonal Council.", "சத்தீஸ்கர் மத்திய மண்டலக் குழுவின் உறுப்பினர் என்பதால் விருப்பம் C சரி.",
        "Option D is incorrect because Odisha belongs to the Eastern Zone.", "ஒடிசா கிழக்கு மண்டலத்தைச் சேர்ந்தது என்பதால் விருப்பம் D தவறு.",
        "Central Zone States (4): UP, MP, Uttarakhand, Chhattisgarh. Eastern Zone States (4): Bihar, Jharkhand, Odisha, WB.",
        "மத்திய மண்டல மாநிலங்கள் (4): உ.பி., ம.பி., உத்தராகண்ட், சத்தீஸ்கர். கிழக்கு மண்டல மாநிலங்கள் (4): பீகார், ஜார்க்கண்ட், ஒடிசா, மேற்கு வங்காளம்.",
        "Chhattisgarh is a member of the Central Zonal Council headquartered at Prayagraj.",
        "பிரயாக்ராஜைத் தலைமையகமாகக் கொண்ட மத்திய மண்டலக் குழுவில் சத்தீஸ்கர் உறுப்பினராக உள்ளது.",
        tags=["Central Zonal Council", "Chhattisgarh", "TNPSC PYQ"]
    ))

    # 037 - Ans D (TNPSC Group 1 2017)
    q.append(make_pyq(
        "ISR_PYQ_037", "Hard",
        "[TNPSC Group 1] In 2010, the Vansadhara Water Disputes Tribunal was constituted to resolve water sharing disputes between which two States?",
        "[TNPSC குரூப் 1] 2010-ல், எந்த இரண்டு மாநிலங்களுக்கு இடையேயான நதிநீர்ப் பகிர்வு தகராறைத் தீர்க்க வம்சதாரா நதிநீர் தகராறுகள் தீர்ப்பாயம் அமைக்கப்பட்டது?",
        "Tamil Nadu and Karnataka", "தமிழ்நாடு மற்றும் கர்நாடகா",
        "Karnataka and Maharashtra", "கர்நாடகா மற்றும் மகாராஷ்டிரா",
        "Goa and Karnataka", "கோவா மற்றும் கர்நாடகா",
        "Andhra Pradesh and Odisha", "ஆந்திரப் பிரதேசம் மற்றும் ஒடிசா",
        "D",
        "The Vansadhara Water Disputes Tribunal was constituted in February 2010 to adjudicate the dispute between Andhra Pradesh and Odisha over the sharing of Vansadhara river waters and the construction of the Neradi Barrage.",
        "வம்சதாரா நதிநீர்ப் பகிர்வு மற்றும் நேரடி அணை கட்டுவது தொடர்பாக ஆந்திரப் பிரதேசம் மற்றும் ஒடிசா இடையே உள்ள தகராறைத் தீர்க்க 2010 பிப்ரவரியில் வம்சதாரா தீர்ப்பாயம் அமைக்கப்பட்டது.",
        "Option A is incorrect because TN and Karnataka fought over Cauvery.", "தமிழ்நாடு-கர்நாடகா காவிரி விவகாரத்தில் ஈடுபட்டதால் விருப்பம் A தவறு.",
        "Option B is incorrect because Karnataka and Maharashtra dispute Krishna/Mahadayi.", "கர்நாடகா-மகாராஷ்டிரா கிருஷ்ணா/மகதாயி விவகாரத்தில் உள்ளதால் விருப்பம் B தவறு.",
        "Option C is incorrect because Goa and Karnataka dispute Mahadayi.", "கோவா-கர்நாடகா மகதாயி விவகாரத்தில் உள்ளதால் விருப்பம் C தவறு.",
        "Option D is correct because Andhra Pradesh and Odisha are the two contending riparians of river Vansadhara.", "ஆந்திரப் பிரதேசம் மற்றும் ஒடிசா ஆகியவையே வம்சதாரா நதியின் இரண்டு வடிநில மாநிலங்கள் என்பதால் விருப்பம் D சரி.",
        "Vansadhara = Andhra Pradesh + Odisha; constituted in 2010 under Justice Mukundakam Sharma.",
        "வம்சதாரா = ஆந்திரப் பிரதேசம் + ஒடிசா; 2010-ல் நீதிபதி முகுந்தகம் சர்மா தலைமையில் அமைக்கப்பட்டது.",
        "Vansadhara Tribunal was constituted in 2010 for Andhra Pradesh and Odisha.",
        "வம்சதாரா தீர்ப்பாயம் ஆந்திரா மற்றும் ஒடிசாவிற்காக 2010-ல் அமைக்கப்பட்டது.",
        tags=["Vansadhara Tribunal", "AP and Odisha", "TNPSC PYQ"]
    ))

    # 038 - Ans A (TNPSC Group 1 2022)
    q.append(make_pyq(
        "ISR_PYQ_038", "Medium",
        "[TNPSC Group 1] In which year did the 2002 amendment to the Inter-State River Water Disputes Act, 1956 come into force?",
        "[TNPSC குரூப் 1] 1956-ஆம் ஆண்டின் மாநிலங்களுக்கு இடையேயான நதிநீர் தகராறுகள் சட்டத்திற்கான 2002-ஆம் ஆண்டு திருத்தம் எந்த ஆண்டு முதல் நடைமுறைக்கு வந்தது?",
        "2002", "2002",
        "2004", "2004",
        "2006", "2006",
        "2010", "2010",
        "A",
        "The Inter-State Water Disputes (Amendment) Act, 2002 (Act 14 of 2002) was passed by Parliament and came into force on 6th August 2002, introducing fixed timelines for tribunal constitution and award delivery.",
        "1956 நதிநீர் தகராறுகள் சட்டத்தில் திருத்தம் செய்த 2002-ஆம் ஆண்டின் திருத்தச் சட்டம் 2002 ஆகஸ்ட் 6 முதல் நடைமுறைக்கு வந்தது; இது தீர்ப்பாயம் அமைக்கவும் தீர்ப்பு வழங்கவும் கால வரம்புகளை அறிமுகப்படுத்தியது.",
        "Option A is correct because the amendment came into force in 2002.", "இத்திருத்தம் 2002-ல் நடைமுறைக்கு வந்ததால் விருப்பம் A சரி.",
        "Option B is incorrect because 2004 was the year KWDT-II was constituted under the amended law.", "2004 திருத்தப்பட்ட சட்டத்தின் கீழ் இரண்டாவது கிருஷ்ணா தீர்ப்பாயம் அமைக்கப்பட்ட ஆண்டு என்பதால் விருப்பம் B தவறு.",
        "Option C is incorrect because 2006 is inaccurate.", "2006 தவறான ஆண்டு என்பதால் விருப்பம் C தவறு.",
        "Option D is incorrect because 2010 is much later.", "2010 பிந்தைய ஆண்டு என்பதால் விருப்பம் D தவறு.",
        "2002 Amendment to IRWD Act mandated: 1 year for tribunal referral, 3 years for award (+2 years max).",
        "2002 திருத்தம்: தீர்ப்பாயத்திற்கு அனுப்ப 1 ஆண்டு, தீர்ப்பு வழங்க 3 ஆண்டுகள் (+2 ஆண்டுகள் அதிகபட்சம்).",
        "The IRWD Amendment Act came into force in August 2002.",
        "நதிநீர் தகராறுகள் திருத்தச் சட்டம் 2002 ஆகஸ்டில் நடைமுறைக்கு வந்தது.",
        tags=["2002 Amendment", "IRWD Timelines", "TNPSC PYQ"]
    ))

    # 039 - Ans B (TNPSC Group 1 2019)
    q.append(make_pyq(
        "ISR_PYQ_039", "Hard",
        "[TNPSC Group 1] In 1996, the Inter-State Council established which internal body for continuous consultation and processing of matters between full meetings?",
        "[TNPSC குரூப் 1] 1996-ல், முழு அமர்வுகளுக்கு இடைப்பட்ட காலத்தில் தொடர் ஆலோசனை மற்றும் பணிகளைச் செயல்படுத்த மாநிலங்களுக்கு இடையிலான மன்றம் எந்த உள் அமைப்பை நிறுவியது?",
        "Dispute Resolution Committee", "தகராறு தீர்வு குழு",
        "Standing Committee of the Inter-State Council", "மாநிலங்களுக்கு இடையிலான மன்றத்தின் நிலைக்குழு",
        "Zonal Coordination Cell", "மண்டல ஒருங்கிணைப்பு பிரிவு",
        "Federal Arbitration Board", "கூட்டாட்சி நடுவர் வாரியம்",
        "B",
        "The Standing Committee of the Inter-State Council was constituted in 1996 under the chairmanship of the Union Home Minister to ensure continuous consultation and process matters for the consideration of the full Council.",
        "முழு மன்றத்தின் பரிசீலனைக்குரிய விஷயங்களைத் தொடர்ந்து ஆலோசிக்கவும் செயல்படுத்தவும் 1996-ல் மத்திய உள்துறை அமைச்சர் தலைமையில் மாநிலங்களுக்கு இடையிலான மன்றத்தின் நிலைக்குழு அமைக்கப்பட்டது.",
        "Option A is incorrect because Dispute Resolution Committee is a mechanism under the 2019 River Disputes Bill.", "DRC என்பது 2019 நதிநீர் மசோதாவின் கீழ் உள்ள அமைப்பு என்பதால் விருப்பம் A தவறு.",
        "Option B is correct because the Standing Committee was established in 1996.", "நிலைக்குழு 1996-ல் அமைக்கப்பட்டதால் விருப்பம் B சரி.",
        "Option C is incorrect because no such cell was created.", "அத்தகைய பிரிவு எதுவும் உருவாக்கப்படவில்லை என்பதால் விருப்பம் C தவறு.",
        "Option D is incorrect because no arbitration board exists.", "நடுவர் வாரியம் எதுவும் இல்லை என்பதால் விருப்பம் D தவறு.",
        "ISC Standing Committee (1996): Chaired by Union Home Minister + 5 Union Cabinet Ministers + 9 CMs.",
        "மன்றத்தின் நிலைக்குழு (1996): மத்திய உள்துறை அமைச்சர் தலைவர் + 5 மத்திய அமைச்சர்கள் + 9 முதலமைச்சர்கள்.",
        "The Standing Committee of the Inter-State Council was constituted in 1996.",
        "மாநிலங்களுக்கு இடையிலான மன்றத்தின் நிலைக்குழு 1996-ல் அமைக்கப்பட்டது.",
        tags=["Standing Committee 1996", "Home Minister Chair", "TNPSC PYQ"]
    ))

    # 040 - Ans C (TNPSC Group 1 2021)
    q.append(make_pyq(
        "ISR_PYQ_040", "Medium",
        "[TNPSC Group 1] Under Article 261(3) of the Constitution of India, final judgments or orders passed by which courts are capable of execution anywhere in the territory of India?",
        "[TNPSC குரூப் 1] இந்திய அரசியலமைப்பின் 261(3) உறுப்பின் கீழ், எந்த நீதிமன்றங்களால் வழங்கப்படும் இறுதித் தீர்ப்புகள் அல்லது ஆணைகள் இந்தியாவில் எங்கு வேண்டுமானாலும் நிறைவேற்றப்படலாம்?",
        "Criminal courts only", "குற்றவியல் நீதிமன்றங்கள் மட்டுமே",
        "Revenue courts only", "வருவாய் நீதிமன்றங்கள் மட்டுமே",
        "Civil courts", "உரிமையியல் நீதிமன்றங்கள்",
        "Military courts only", "இராணுவ நீதிமன்றங்கள் மட்டுமே",
        "C",
        "Article 261(3) explicitly specifies that final judgments or orders delivered or passed by 'civil courts' in any part of the territory of India shall be capable of execution anywhere within that territory according to law.",
        "இந்திய அரசியலமைப்பின் 261(3) உறுப்பு, இந்தியாவின் எந்தப் பகுதியிலும் உள்ள 'உரிமையியல் நீதிமன்றங்களால்' (Civil courts) வழங்கப்படும் இறுதித் தீர்ப்புகள் அல்லது ஆணைகள் சட்டப்படி இந்தியாவில் எங்கு வேண்டுமானாலும் நிறைவேற்றப்படலாம் என்று தெளிவாகக் கூறுகிறது.",
        "Option A is incorrect because criminal decrees are excluded from Article 261(3).", "குற்றவியல் தீர்ப்புகள் உறுப்பு 261(3)-லிருந்து விலக்கப்பட்டுள்ளதால் விருப்பம் A தவறு.",
        "Option B is incorrect because it is not limited to revenue courts.", "வருவாய் நீதிமன்றங்களுக்கு மட்டுமே உரியது அல்ல என்பதால் விருப்பம் B தவறு.",
        "Option C is correct because Article 261(3) expressly applies to Civil Courts.", "உறுப்பு 261(3) உரிமையியல் நீதிமன்றங்களுக்குப் பிரத்யேகமாகப் பொருந்துவதால் விருப்பம் C சரி.",
        "Option D is incorrect because military courts do not fall under this provision.", "இராணுவ நீதிமன்றங்களுக்கு இது பொருந்தாது என்பதால் விருப்பம் D தவறு.",
        "Core rule: Article 261(3) execution applies strictly to CIVIL COURTS, never to criminal or penal judgments.",
        "முக்கிய விதி: உறுப்பு 261(3) உரிமையியல் நீதிமன்றங்களுக்கு மட்டுமே பொருந்தும், குற்றவியல் தீர்ப்புகளுக்கு அல்ல.",
        "Article 261(3) decrees of civil courts can be executed throughout India.",
        "உறுப்பு 261(3)-ன் கீழ் உரிமையியல் நீதிமன்றத் தீர்ப்பாணைகள் இந்தியா முழுவதும் நிறைவேற்றப்படலாம்.",
        tags=["Article 261(3)", "Civil Courts", "Full Faith and Credit"]
    ))

    # 041 - Ans D (TNPSC Group 1 2017)
    q.append(make_pyq(
        "ISR_PYQ_041", "Hard",
        "[TNPSC Group 1] In which year did the Supreme Court deliver the advisory opinion on the Cauvery Water Disputes Tribunal (Special Reference No. 1 of 1991), holding that an ordinance issued by Karnataka overriding the Tribunal's interim order was unconstitutional?",
        "[TNPSC குரூப் 1] காவிரி தீர்ப்பாயத்தின் இடைக்கால உத்தரவை ரத்து செய்து கர்நாடகா பிறப்பித்த அவசரச் சட்டம் அரசியலமைப்பிற்கு முரணானது என்று கூறி, எந்த ஆண்டு உச்ச நீதிமன்றம் காவிரி ஆலோசனைக் கருத்தை (1991-ன் சிறப்பு குறிப்பு எண் 1) வழங்கியது?",
        "1988", "1988",
        "1989", "1989",
        "1990", "1990",
        "1991", "1991",
        "D",
        "In November 1991, in Special Reference No. 1 of 1991 under Article 143, a 5-judge Constitution Bench held that the Karnataka Cauvery Basin Irrigation Protection Ordinance, 1991 was unconstitutional as it nullified the interim order of the Cauvery Water Disputes Tribunal and violated the rule of law.",
        "நவம்பர் 1991-ல், உறுப்பு 143-ன் கீழான சிறப்பு குறிப்பு எண் 1-ல், காவிரி தீர்ப்பாயத்தின் இடைக்கால உத்தரவை ரத்து செய்ய கர்நாடகா பிறப்பித்த அவசரச் சட்டம் அரசியலமைப்பிற்கு முரணானது மற்றும் சட்டத்தின் ஆட்சியை மீறுவது என 5 நீதிபதிகள் அமர்வு தீர்ப்பளித்தது.",
        "Option A is incorrect because 1988 is prior to tribunal constitution.", "1988 தீர்ப்பாயம் அமைவதற்கு முந்தையது என்பதால் விருப்பம் A தவறு.",
        "Option B is incorrect because 1989 is inaccurate.", "1989 தவறான ஆண்டு என்பதால் விருப்பம் B தவறு.",
        "Option C is incorrect because 1990 was the year the Cauvery Tribunal was constituted.", "1990 தீர்ப்பாயம் அமைக்கப்பட்ட ஆண்டு என்பதால் விருப்பம் C தவறு.",
        "Option D is correct because the landmark Article 143 advisory opinion was delivered in November 1991.", "வரலாற்றுச் சிறப்புமிக்க உறுப்பு 143 ஆலோசனைக் கருத்து 1991 நவம்பரில் வழங்கப்பட்டதால் விருப்பம் D சரி.",
        "1991 Cauvery Reference: A State cannot pass an ordinance to nullify an inter-state water tribunal's award!",
        "1991 காவிரி தீர்ப்பு: நதிநீர் தீர்ப்பாயத்தின் உத்தரவை ரத்து செய்ய எந்த மாநிலமும் அவசரச் சட்டம் இயற்ற முடியாது!",
        "Supreme Court ruled in 1991 (Special Reference 1) that State ordinances overriding tribunal orders are void.",
        "தீர்ப்பாய உத்தரவுகளை ரத்து செய்யும் மாநில அவசரச் சட்டங்கள் செல்லாது என 1991-ல் உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
        tags=["Cauvery Reference 1991", "Article 143", "Ordinance Invalidated"]
    ))

    # 042 - Ans A (TNPSC Group 1 2019)
    q.append(make_pyq(
        "ISR_PYQ_042", "Easy",
        "[TNPSC Group 1] Which constitutional amendment added the Goods and Services Tax Council (GST Council) under Article 279A, establishing a premier institution for fiscal cooperative federalism?",
        "[TNPSC குரூப் 1] நிதிசார் கூட்டுறவு கூட்டாட்சிக்கான முதன்மை அமைப்பான சரக்கு மற்றும் சேவை வரி மன்றத்தை (GST மன்றம்) உறுப்பு 279A-ன் கீழ் சேர்த்த அரசியலமைப்புத் திருத்தம் எது?",
        "101st Constitutional Amendment Act, 2016", "101-வது அரசியலமைப்புத் திருத்தச் சட்டம், 2016",
        "102nd Constitutional Amendment Act, 2018", "102-வது அரசியலமைப்புத் திருத்தச் சட்டம், 2018",
        "103rd Constitutional Amendment Act, 2019", "103-வது அரசியலமைப்புத் திருத்தச் சட்டம், 2019",
        "104th Constitutional Amendment Act, 2020", "104-வது அரசியலமைப்புத் திருத்தச் சட்டம், 2020",
        "A",
        "The 101st Constitutional Amendment Act, 2016 inserted Article 279A, which empowered the President to constitute the GST Council, creating a cooperative federal body comprising Union and State representatives to decide on national indirect taxation.",
        "101-வது அரசியலமைப்புத் திருத்தச் சட்டம் 2016, உறுப்பு 279A-ஐச் சேர்த்தது; இது மறைமுக வரிகள் குறித்து முடிவெடுக்க ஒன்றியம் மற்றும் மாநிலப் பிரதிநிதிகளைக் கொண்ட கூட்டுறவு கூட்டாட்சி அமைப்பான ஜிஎஸ்டி மன்றத்தைக் குடியரசுத் தலைவர் அமைக்க வழிவகுத்தது.",
        "Option A is correct because the 101st Amendment introduced the GST Council under Article 279A.", "101-வது திருத்தம் உறுப்பு 279A-ன் கீழ் ஜிஎஸ்டி மன்றத்தை உருவாக்கியதால் விருப்பம் A சரி.",
        "Option B is incorrect because the 102nd Amendment gave constitutional status to the National Commission for Backward Classes (Article 338B).", "102-வது திருத்தம் NCBC-க்கு அரசியலமைப்பு அந்தஸ்து அளித்தது என்பதால் விருப்பம் B தவறு.",
        "Option C is incorrect because the 103rd Amendment introduced 10% EWS reservation.", "103-வது திருத்தம் EWS இடஒதுக்கீட்டிற்குரியது என்பதால் விருப்பம் C தவறு.",
        "Option D is incorrect because the 104th Amendment extended SC/ST reservations in legislatures.", "104-வது திருத்தம் சட்டமன்றங்களில் SC/ST இடஒதுக்கீட்டை நீடித்தது என்பதால் விருப்பம் D தவறு.",
        "GST Council (Article 279A) was introduced by the 101st Amendment (2016) as a federal fiscal decision-making body.",
        "ஜிஎஸ்டி மன்றம் (உறுப்பு 279A) கூட்டாட்சி நிதி முடிவெடுக்கும் அமைப்பாக 101-வது திருத்தத்தால் (2016) உருவாக்கப்பட்டது.",
        "The 101st Amendment Act, 2016 established the GST Council under Article 279A.",
        "101-வது திருத்தச் சட்டம் 2016 உறுப்பு 279A-ன் கீழ் ஜிஎஸ்டி மன்றத்தை நிறுவியது.",
        tags=["101st Amendment", "GST Council", "Fiscal Federalism"]
    ))

    # 043 - Ans B (TNPSC Group 2 2015)
    q.append(make_pyq(
        "ISR_PYQ_043", "Medium",
        "[TNPSC Group 2] In which city is the headquarters of the Western Zonal Council located?",
        "[TNPSC குரூப் 2] மேற்கு மண்டலக் குழுவின் தலைமையகம் எந்த நகரத்தில் அமைந்துள்ளது?",
        "Ahmedabad", "அகமதாபாத்",
        "Mumbai", "மும்பை",
        "Panaji", "பனாஜி",
        "Pune", "புனே",
        "B",
        "The headquarters of the Western Zonal Council (comprising Maharashtra, Gujarat, Goa, and UT of Dadra and Nagar Haveli and Daman and Diu) is situated at Mumbai.",
        "மகாராஷ்டிரா, குஜராத், கோவா மற்றும் தாத்ரா & நகர் ஹவேலி மற்றும் டாமன் & டையூ யூனியன் பிரதேசத்தை உள்ளடக்கிய மேற்கு மண்டலக் குழுவின் தலைமையகம் மும்பையில் அமைந்துள்ளது.",
        "Option A is incorrect because Ahmedabad is not the headquarters.", "அகமதாபாத் தலைமையகம் அல்ல என்பதால் விருப்பம் A தவறு.",
        "Option B is correct because Mumbai is the statutory headquarters of the Western Zonal Council.", "மும்பை மேற்கு மண்டலக் குழுவின் தலைமையகம் என்பதால் விருப்பம் B சரி.",
        "Option C is incorrect because Panaji is the capital of Goa.", "பனாஜி கோவாவின் தலைநகர் என்பதால் விருப்பம் C தவறு.",
        "Option D is incorrect because Pune is not the headquarters.", "புனே தலைமையகம் அல்ல என்பதால் விருப்பம் D தவறு.",
        "Western Zonal Council = Mumbai; Southern = Chennai; Eastern = Kolkata; Central = Prayagraj; Northern = New Delhi.",
        "மேற்கு மண்டலம் = மும்பை; தெற்கு = சென்னை; கிழக்கு = கொல்கத்தா; மத்திய = பிரயாக்ராஜ்; வடக்கு = புதுதில்லி.",
        "Western Zonal Council is headquartered in Mumbai.",
        "மேற்கு மண்டலக் குழு மும்பையில் தலைமையகத்தைக் கொண்டுள்ளது.",
        tags=["Western Zonal Council", "Mumbai HQ", "TNPSC PYQ"]
    ))

    # 044 - Ans C (TNPSC Group 1 2019)
    q.append(make_pyq(
        "ISR_PYQ_044", "Hard",
        "[TNPSC Group 1] In 1990, the V.P. Singh Government established the Inter-State Council through a Presidential Order issued on which exact date?",
        "[TNPSC குரூப் 1] 1990-ல், வி.பி. சிங் அரசு எந்த துல்லியமான தேதியில் வெளியிடப்பட்ட குடியரசுத் தலைவர் ஆணையின் மூலம் மாநிலங்களுக்கு இடையிலான மன்றத்தை நிறுவியது?",
        "26th January 1990", "1990 ஜனவரி 26",
        "15th August 1990", "1990 ஆகஸ்ட் 15",
        "28th May 1990", "1990 மே 28",
        "2nd October 1990", "1990 அக்டோபர் 2",
        "C",
        "The Presidential Order establishing the Inter-State Council was signed by President R. Venkataraman and notified in the Gazette of India on 28th May 1990.",
        "மாநிலங்களுக்கு இடையிலான மன்றத்தை நிறுவும் குடியரசுத் தலைவரின் ஆணை குடியரசுத் தலைவர் ஆர். வெங்கட்ராமனால் கையெழுத்திடப்பட்டு 1990 மே 28 அன்று இந்திய அரசிதழில் வெளியிடப்பட்டது.",
        "Option A is incorrect because January 26 was Republic Day, not the notification date.", "ஜனவரி 26 குடியரசு தினம், அறிவிப்பு தேதி அல்ல என்பதால் விருப்பம் A தவறு.",
        "Option B is incorrect because August 15 is Independence Day.", "ஆகஸ்ட் 15 சுதந்திர தினம் என்பதால் விருப்பம் B தவறு.",
        "Option C is correct because May 28, 1990 is the exact historic date of notification.", "1990 மே 28 என்பது அரசிதழில் வெளியான சரியான வரலாற்றுத் தேதி என்பதால் விருப்பம் C சரி.",
        "Option D is incorrect because October 2 is Gandhi Jayanti.", "அக்டோபர் 2 காந்தி ஜெயந்தி என்பதால் விருப்பம் D தவறு.",
        "High-precision TNPSC question: 28th May 1990 is the establishment date of the Inter-State Council.",
        "துல்லியமான TNPSC வினா: 1990 மே 28 என்பது மாநிலங்களுக்கு இடையிலான மன்றம் நிறுவப்பட்ட தேதியாகும்.",
        "Inter-State Council was notified by Presidential Order on 28th May 1990.",
        "1990 மே 28 அன்று குடியரசுத் தலைவரின் ஆணை மூலம் மாநிலங்களுக்கு இடையிலான மன்றம் அறிவிக்கப்பட்டது.",
        tags=["28 May 1990", "Inter-State Council Notification", "TNPSC PYQ"]
    ))

    # 045 - Ans D (TNPSC Group 1 2021)
    q.append(make_pyq(
        "ISR_PYQ_045", "Medium",
        "[TNPSC Group 1] In which year did the Inter-State Council Secretariat (ISCS) formally begin functioning as the Secretariat to all the Zonal Councils as well?",
        "[TNPSC குரூப் 1] அனைத்து மண்டலக் குழுக்களுக்குமான செயலகமாகவும் மாநிலங்களுக்கு இடையிலான மன்றச் செயலகம் (ISCS) எந்த ஆண்டு முதல் முறைப்படி செயல்படத் தொடங்கியது?",
        "1991", "1991",
        "2002", "2002",
        "2007", "2007",
        "2011", "2011",
        "D",
        "In April 2011, the Government of India integrated administrative arrangements and notified that the Inter-State Council Secretariat (ISCS) would also function as the Secretariat to the Zonal Councils.",
        "ஏப்ரல் 2011-ல், மத்திய அரசு நிர்வாகக் கட்டமைப்புகளை ஒருங்கிணைத்து, மாநிலங்களுக்கு இடையிலான மன்றச் செயலகம் (ISCS) மண்டலக் குழுக்களுக்குமான செயலகமாகவும் செயல்படும் என அறிவித்தது.",
        "Option A is incorrect because 1991 was when the ISCS was originally established for the Inter-State Council only.", "1991-ல் செயலகம் மன்றத்திற்கு மட்டுமே அமைக்கப்பட்டது என்பதால் விருப்பம் A தவறு.",
        "Option B is incorrect because 2002 is inaccurate.", "2002 தவறான ஆண்டு என்பதால் விருப்பம் B தவறு.",
        "Option C is incorrect because 2007 is inaccurate.", "2007 தவறான ஆண்டு என்பதால் விருப்பம் C தவறு.",
        "Option D is correct because ISCS assumed responsibility for Zonal Councils in April 2011.", "ஏப்ரல் 2011 முதல் மண்டலக் குழுக்களுக்கும் செயலகமாகச் செயல்படத் தொடங்கியதால் விருப்பம் D சரி.",
        "Administrative milestone: Since April 2011, the Inter-State Council Secretariat serves both ISC and Zonal Councils.",
        "நிர்வாக மைல்கல்: ஏப்ரல் 2011 முதல் மாநிலங்களுக்கு இடையிலான மன்றச் செயலகம் மன்றம் மற்றும் மண்டலக் குழுக்கள் இரண்டிற்கும் சேவையாற்றுகிறது.",
        "Inter-State Council Secretariat functions as the Secretariat to Zonal Councils since April 2011.",
        "ஏப்ரல் 2011 முதல் மண்டலக் குழுக்களின் செயலகமாகவும் மன்றச் செயலகம் செயல்படுகிறது.",
        tags=["ISCS 2011", "Zonal Councils Secretariat", "Administrative Integration"]
    ))

    # 046 - Ans D (TNPSC Group 1 2017)
    q.append(make_pyq(
        "ISR_PYQ_046", "Easy",
        "[TNPSC Group 1] The River Boards Act, 1956 was enacted by Parliament under which of the following legislative entries?",
        "[TNPSC குரூப் 1] 1956-ஆம் ஆண்டின் நதி வாரியங்கள் சட்டம் பின்வரும் எந்தச் சட்டப் பதிவின் கீழ் நாடாளுமன்றத்தால் இயற்றப்பட்டது?",
        "Entry 17 of List II (State List)", "பட்டியல் II-ன் (மாநிலப் பட்டியல்) பதிவு 17",
        "Entry 20 of List III (Concurrent List)", "பட்டியல் III-ன் (பொதுப் பட்டியல்) பதிவு 20",
        "Entry 97 of List I (Residuary Powers)", "பட்டியல் I-ன் (எஞ்சிய அதிகாரங்கள்) பதிவு 97",
        "Entry 56 of List I (Union List)", "பட்டியல் I-ன் (மத்தியப் பட்டியல்) பதிவு 56",
        "D",
        "The River Boards Act, 1956 was enacted under Entry 56 of the Union List (List I) of the Seventh Schedule, which authorizes Parliament to regulate and develop inter-State rivers and river valleys in the public interest.",
        "பொது நலன் கருதி மாநிலங்களுக்கு இடையிலான நதிகள் மற்றும் நதிப் பள்ளத்தாக்குகளை ஒழுங்குபடுத்தவும் மேம்படுத்தவும் நாடாளுமன்றத்திற்கு அதிகாரம் அளிக்கும் ஏழாவது அட்டவணையின் மத்தியப் பட்டியல் (பட்டியல் I) பதிவு 56-ன் கீழ் நதி வாரியங்கள் சட்டம் 1956 இயற்றப்பட்டது.",
        "Option A is incorrect because Entry 17 of List II is the State List entry for water, which is subject to Entry 56.", "மாநிலப் பட்டியல் பதிவு 17 மத்தியப் பட்டியல் பதிவு 56-க்கு உட்பட்டது என்பதால் விருப்பம் A தவறு.",
        "Option B is incorrect because Entry 20 of List III is social planning.", "பொதுப் பட்டியல் பதிவு 20 திட்டமிடலுக்குரியது என்பதால் விருப்பம் B தவறு.",
        "Option C is incorrect because Entry 97 is residuary powers.", "பதிவு 97 எஞ்சிய அதிகாரங்களுக்குரியது என்பதால் விருப்பம் C தவறு.",
        "Option D is correct because Entry 56 of List I is the specific constitutional foundation of the River Boards Act.", "மத்தியப் பட்டியல் பதிவு 56 நதி வாரியங்கள் சட்டத்தின் அரசியலமைப்பு அடிப்படை என்பதால் விருப்பம் D சரி.",
        "Remember: IRWD Act 1956 is enacted under Article 262; River Boards Act 1956 is enacted under List I Entry 56.",
        "நினைவில் கொள்க: 1956 நதிநீர் தகராறுகள் சட்டம் உறுப்பு 262-ன் கீழும்; 1956 நதி வாரியங்கள் சட்டம் மத்தியப் பட்டியல் பதிவு 56-ன் கீழும் இயற்றப்பட்டன.",
        "River Boards Act 1956 was enacted under Entry 56 of the Union List.",
        "மத்தியப் பட்டியல் பதிவு 56-ன் கீழ் 1956 நதி வாரியங்கள் சட்டம் இயற்றப்பட்டது.",
        tags=["River Boards Act", "Entry 56 List I", "Seventh Schedule"]
    ))

    # 047 - Ans A (TNPSC Group 1 2019)
    q.append(make_pyq(
        "ISR_PYQ_047", "Medium",
        "[TNPSC Group 1] Which of the following is the primary objective of establishing Zonal Councils under the States Reorganisation Act, 1956?",
        "[TNPSC குரூப் 1] 1956-ஆம் ஆண்டின் மாநில மறுசீரமைப்புச் சட்டத்தின் கீழ் மண்டலக் குழுக்களை நிறுவியதன் முதன்மை நோக்கம் பின்வருவனவற்றில் எது?",
        "To promote emotional integration, cooperative federalism, and resolve inter-State friction", "உணர்ச்சிபூர்வமான ஒருமைப்பாடு, கூட்டுறவு கூட்டாட்சியை ஊக்குவித்தல் மற்றும் மாநிலங்களுக்கு இடையேயான உராய்வுகளைத் தீர்த்தல்",
        "To replace the legislative powers of State Assemblies in regional affairs", "பிராந்திய விவகாரங்களில் மாநில சட்டமன்றங்களின் சட்டமியற்றும் அதிகாரத்தை மாற்றுதல்",
        "To collect regional customs duties on interstate movement of goods", "மாநிலங்களுக்கு இடையேயான பொருட்களின் போக்குவரத்திற்குப் பிராந்திய சுங்க வரிகளை வசூலித்தல்",
        "To administer Union Territories directly under military control", "யூனியன் பிரதேசங்களை ராணுவக் கட்டுப்பாட்டின் கீழ் நேரடியாக நிர்வகித்தல்",
        "A",
        "Pandit Jawaharlal Nehru conceived Zonal Councils to counteract regionalism, foster inter-state habits of cooperative deliberation, arrest the growth of acute state-consciousness, and assist in executing joint developmental projects.",
        "பண்டித ஜவஹர்லால் நேரு தீவிர பிராந்தியவாதத்தைத் தடுக்கவும், மாநிலங்களுக்கு இடையே கூட்டுறவு ஆலோசனை பழக்கத்தை வளர்க்கவும், உணர்ச்சிபூர்வமான ஒருமைப்பாட்டை ஏற்படுத்தவும், கூட்டு வளர்ச்சித் திட்டங்களைச் செயல்படுத்தவும் மண்டலக் குழுக்களை உருவாக்கினார்.",
        "Option A is correct because emotional integration and cooperative inter-state collaboration are the foundational aims.", "உணர்ச்சிபூர்வ ஒருமைப்பாடு மற்றும் கூட்டுறவு ஒத்துழைப்பே இதன் அடிப்படைக் குறிக்கோள்கள் என்பதால் விருப்பம் A சரி.",
        "Option B is incorrect because Zonal Councils cannot usurp state legislative powers.", "மாநில சட்டமன்ற அதிகாரங்களை மண்டலக் குழுக்கள் மாற்ற முடியாது என்பதால் விருப்பம் B தவறு.",
        "Option C is incorrect because internal customs are unconstitutional under Article 301.", "உள்நாட்டு சுங்க வரிகள் உறுப்பு 301-க்கு முரணானவை என்பதால் விருப்பம் C தவறு.",
        "Option D is incorrect because Zonal Councils have no military functions.", "மண்டலக் குழுக்களுக்கு ராணுவப் பணி எதுவும் இல்லை என்பதால் விருப்பம் D தவறு.",
        "Nehru's vision: Zonal Councils were designed to foster 'emotional integration' and develop the habit of cooperative working.",
        "நேருவின் பார்வை: மண்டலக் குழுக்கள் 'உணர்ச்சிபூர்வ ஒருமைப்பாட்டை' வளர்க்கவும் கூட்டுறவுப் பணியை உருவாக்கவும் வடிவமைக்கப்பட்டன.",
        "Zonal Councils aim to promote emotional integration and cooperative federalism across States.",
        "மண்டலக் குழுக்கள் மாநிலங்களிடையே உணர்ச்சிபூர்வ ஒருமைப்பாட்டையும் கூட்டுறவு கூட்டாட்சியையும் வளர்ப்பதை நோக்கமாகக் கொண்டுள்ளன.",
        tags=["Zonal Councils Objective", "Emotional Integration", "Cooperative Federalism"]
    ))

    # 048 - Ans B (TNPSC Group 1 2022)
    q.append(make_pyq(
        "ISR_PYQ_048", "Hard",
        "[TNPSC Group 1] Under Article 304(a) of the Constitution, a State legislature can impose taxes on goods imported from other States subject to which indispensable condition?",
        "[TNPSC குரூப் 1] அரசியலமைப்பின் 304(a) உறுப்பின் கீழ், பிற மாநிலங்களிலிருந்து இறக்குமதி செய்யப்படும் பொருட்களின் மீது எந்த அத்தியாவசிய நிபந்தனைக்கு உட்பட்டு மாநில சட்டமன்றம் வரிகளை விதிக்க முடியும்?",
        "The tax must be 50% higher than the rate applicable to locally manufactured goods", "உள்ளூரில் உற்பத்தி செய்யப்படும் பொருட்களுக்குப் பொருந்தும் விகிதத்தை விட வரி 50% அதிகமாக இருக்க வேண்டும்",
        "Similar goods manufactured or produced in that State must be subjected to non-discriminatory identical taxation", "அந்த மாநிலத்தில் உற்பத்தி செய்யப்படும் ஒத்த பொருட்கள் மீது பாகுபாடற்ற சமமான வரி விதிக்கப்பட வேண்டும்",
        "The revenue collected must be directly remitted to the Consolidated Fund of India", "வசூலிக்கப்படும் வருவாய் நேரடியாக இந்தியத் தொகுப்பு நிதியில் செலுத்தப்பட வேண்டும்",
        "The State must obtain prior approval of the GST Council before passing the law", "சட்டத்தை இயற்றுவதற்கு முன் மாநிலம் ஜிஎஸ்டி மன்றத்தின் முன் ஒப்புதலைப் பெற வேண்டும்",
        "B",
        "Article 304(a) allows a State Legislature to impose taxes on goods imported from other States or Union Territories, provided that similar goods manufactured or produced in that State are subjected to the same tax, so as not to discriminate between goods so imported and goods so manufactured or produced.",
        "உறுப்பு 304(a)-ன் கீழ் பிற மாநிலங்களிலிருந்து இறக்குமதி செய்யப்படும் பொருட்கள் மீது மாநிலம் வரி விதிக்கலாம்; ஆனால் அந்த மாநிலத்தில் உற்பத்தி செய்யப்படும் ஒத்த பொருட்களுக்கு என்ன வரி விதிக்கப்படுகிறதோ அதே வரி பாகுபாடின்றி விதிக்கப்பட வேண்டும் என்ற நிபந்தனைக்கு உட்பட்டே இதைச் செய்ய முடியும்.",
        "Option A is incorrect because discriminatory higher tax is strictly prohibited.", "அதிக வரி விதிப்பது முற்றிலும் தடை செய்யப்பட்டுள்ளதால் விருப்பம் A தவறு.",
        "Option B is correct because Article 304(a) enforces the non-discrimination parity rule.", "உறுப்பு 304(a) பாகுபாடற்ற சமநிலைக் கோட்பாட்டை அமல்படுத்துவதால் விருப்பம் B சரி.",
        "Option C is incorrect because state tax proceeds go to the Consolidated Fund of the State.", "மாநில வரி வருவாய் மாநிலத் தொகுப்பு நிதிக்குச் செல்கிறது என்பதால் விருப்பம் C தவறு.",
        "Option D is incorrect because Article 304(a) is an independent constitutional power.", "இது சுதந்திரமான அரசியலமைப்பு அதிகாரம் என்பதால் விருப்பம் D தவறு.",
        "Parity rule under Article 304(a): Imported goods cannot be subjected to a tax higher than locally manufactured goods.",
        "உறுப்பு 304(a) சமநிலை விதி: உள்ளூர் பொருட்களை விட இறக்குமதி செய்யப்படும் பொருட்கள் மீது அதிக வரி விதிக்க முடியாது.",
        "Article 304(a) permits taxes on imported goods only on a non-discriminatory basis with local goods.",
        "உள்ளூர் பொருட்களுடன் பாகுபாடற்ற அடிப்படையில் மட்டுமே இறக்குமதிப் பொருட்கள் மீது வரி விதிக்க உறுப்பு 304(a) அனுமதிக்கிறது.",
        tags=["Article 304(a)", "Tax Parity", "Non-Discrimination"]
    ))

    # 049 - Ans C (TNPSC Group 1 2021)
    q.append(make_pyq(
        "ISR_PYQ_049", "Medium",
        "[TNPSC Group 1] In 2018, which Authority was established under Section 6A of the Inter-State River Water Disputes Act, 1956 to give effect to the Cauvery Tribunal's award as modified by the Supreme Court?",
        "[TNPSC குரூப் 1] 2018-ல், உச்ச நீதிமன்றத்தால் மாற்றியமைக்கப்பட்ட காவிரி தீர்ப்பாயத்தின் தீர்ப்பை அமல்படுத்த 1956 நதிநீர் தகராறுகள் சட்டம் பிரிவு 6A-ன் கீழ் எந்த ஆணையம் நிறுவப்பட்டது?",
        "Cauvery River Board", "காவிரி நதி வாரியம்",
        "Cauvery Development Council", "காவிரி மேம்பாட்டு மன்றம்",
        "Cauvery Water Management Authority (CWMA)", "காவிரி நீர் மேலாண்மை ஆணையம் (CWMA)",
        "Cauvery Dispute Settlement Tribunal", "காவிரி தகராறு தீர்வு தீர்ப்பாயம்",
        "C",
        "The Central Government framed the Cauvery Water Management Scheme, 2018 under Section 6A of the IRWD Act, 1956, establishing the Cauvery Water Management Authority (CWMA) to regulate water storage, reservoir releases, and apportion water among TN, KA, KL, and Puducherry.",
        "1956 IRWD சட்டம் பிரிவு 6A-ன் கீழ் மத்திய அரசு காவிரி நீர் மேலாண்மைத் திட்டம் 2018-ஐ உருவாக்கி, தமிழ்நாடு, கர்நாடகா, கேரளா மற்றும் புதுச்சேரி இடையே நீர்ப் பகிர்வு மற்றும் அணைகளில் இருந்து நீர் திறப்பைக் கண்காணிக்க காவிரி நீர் மேலாண்மை ஆணையத்தை (CWMA) நிறுவியது.",
        "Option A is incorrect because no River Board was created under the 1956 River Boards Act.", "நதி வாரியம் எதுவும் உருவாக்கப்படவில்லை என்பதால் விருப்பம் A தவறு.",
        "Option B is incorrect because Development Council is not the statutory name.", "மேம்பாட்டு மன்றம் என்பது சட்டப்பூர்வ பெயர் அல்ல என்பதால் விருப்பம் B தவறு.",
        "Option C is correct because CWMA is the exact statutory authority notified under Section 6A.", "பிரிவு 6A-ன் கீழ் அறிவிக்கப்பட்ட அமைப்பு CWMA என்பதால் விருப்பம் C சரி.",
        "Option D is incorrect because the Tribunal had completed its task in 2007.", "தீர்ப்பாயம் 2007-லேயே பணியை முடித்துவிட்டதால் விருப்பம் D தவறு.",
        "Section 6A of IRWD Act empowers the Central Government to frame schemes to implement awards (e.g., CWMA in 2018).",
        "தீர்ப்புகளை அமல்படுத்த திட்டங்களை வகுக்க மத்திய அரசுக்கு IRWD சட்டப் பிரிவு 6A அதிகாரம் அளிக்கிறது (2018-ல் CWMA).",
        "Cauvery Water Management Authority (CWMA) was constituted in 2018 under Section 6A of the IRWD Act.",
        "1956 IRWD சட்டம் பிரிவு 6A-ன் கீழ் 2018-ல் காவிரி நீர் மேலாண்மை ஆணையம் (CWMA) அமைக்கப்பட்டது.",
        tags=["CWMA", "Section 6A IRWD Act", "Cauvery Scheme 2018"]
    ))

    # 050 - Ans C (TNPSC Group 1 2019)
    q.append(make_pyq(
        "ISR_PYQ_050", "Hard",
        "[TNPSC Group 1] Which of the following is the correct structural summary of inter-State coordination mechanisms established in the Indian Constitution and related statutes?",
        "[TNPSC குரூப் 1] இந்திய அரசியலமைப்பு மற்றும் தொடர்புடைய சட்டங்களில் நிறுவப்பட்டுள்ள மாநிலங்களுக்கு இடையிலான ஒருங்கிணைப்பு அமைப்புகளின் சரியான கட்டமைப்பு சுருக்கம் பின்வருவனவற்றில் எது?",
        "All inter-state dispute bodies in India are judicial courts established under Article 131 with no statutory or advisory components", "இந்தியாவில் உள்ள அனைத்து மாநிலங்களுக்கு இடையேயான தகராறு அமைப்புகளும் உறுப்பு 131-ன் கீழ் அமைக்கப்பட்ட நீதிமன்றங்களே தவிர எந்தச் சட்டப்பூர்வ அல்லது ஆலோசனைக் கூறுகளும் இல்லை",
        "Inter-State Council is statutory under 1956 Act while Zonal Councils are constitutional under Article 263", "மாநிலங்களுக்கு இடையிலான மன்றம் 1956 சட்டத்தின் கீழ் சட்டப்பூர்வமானது, ஆனால் மண்டலக் குழுக்கள் உறுப்பு 263-ன் கீழ் அரசியலமைப்பு சார்ந்தது",
        "Inter-State Council is constitutional under Article 263, Zonal Councils are statutory under the 1956 Act, and Water Disputes Tribunals are statutory bodies under Article 262 laws", "மாநிலங்களுக்கு இடையிலான மன்றம் உறுப்பு 263-ன் கீழ் அரசியலமைப்பு சார்ந்தது, மண்டலக் குழுக்கள் 1956 சட்டத்தின் கீழ் சட்டப்பூர்வமானது மற்றும் நதிநீர் தீர்ப்பாயங்கள் உறுப்பு 262 சட்டங்களின் கீழான சட்டப்பூர்வ அமைப்புகளாகும்",
        "The Constitution prohibits any multi-state coordination forums outside the Union Parliament", "நாடாளுமன்றத்திற்கு வெளியே பல மாநிலங்கள் கூடும் ஒருங்கிணைப்பு மன்றங்களை அரசியலமைப்பு தடை செய்கிறது",
        "C",
        "The Indian federal framework establishes a balanced multi-tier architecture: Article 263 provides the constitutional foundation for the Inter-State Council; the States Reorganisation Act 1956 provides the statutory basis for the 5 Zonal Councils; and Article 262 along with the IRWD Act 1956 governs inter-State river water tribunals.",
        "இந்தியக் கூட்டாட்சி அமைப்பு ஒரு சமநிலையான பல அடுக்கு கட்டமைப்பைக் கொண்டுள்ளது: உறுப்பு 263 மாநிலங்களுக்கு இடையிலான மன்றத்திற்கு அரசியலமைப்பு அடிப்படையை அளிக்கிறது; 1956 மாநில மறுசீரமைப்புச் சட்டம் 5 மண்டலக் குழுக்களுக்குச் சட்டப்பூர்வ அடிப்படையை அளிக்கிறது; உறுப்பு 262 மற்றும் 1956 IRWD சட்டம் நதிநீர் தீர்ப்பாயங்களை நிர்வகிக்கின்றன.",
        "Option A is incorrect because diverse advisory and tribunal mechanisms exist outside Article 131.", "உறுப்பு 131-க்கு வெளியே பல ஆலோசனைக் குழுக்கள் மற்றும் தீர்ப்பாயங்கள் உள்ளதால் விருப்பம் A தவறு.",
        "Option B is incorrect because it reverses the constitutional and statutory status of the bodies.", "மன்றம் மற்றும் மண்டலக் குழுக்களின் நிலைகளை இது தலைகீழாகக் குறிப்பிடுவதால் விருப்பம் B தவறு.",
        "Option C is correct because it accurately captures the constitutional status of ISC, statutory status of Zonal Councils, and tribunal nature under Article 262.", "மன்றத்தின் அரசியலமைப்பு நிலை, மண்டலக் குழுக்களின் சட்டப்பூர்வ நிலை மற்றும் நதிநீர் தீர்ப்பாயங்களின் நிலையைச் சரியாகக் குறிப்பிடுவதால் விருப்பம் C சரி.",
        "Option D is incorrect because multiple multi-state bodies are explicitly authorized.", "பல மாநில ஒருங்கிணைப்பு அமைப்புகள் வெளிப்படையாக அனுமதிக்கப்படுவதால் விருப்பம் D தவறு.",
        "Master architectural summary: ISC = Constitutional (Art 263); Zonal Councils = Statutory (1956 Act); Tribunals = Art 262 + 1956 Act.",
        "முக்கிய கட்டமைப்பு சுருக்கம்: மன்றம் = அரசியலமைப்பு சார்ந்தது (263); மண்டலக் குழுக்கள் = சட்டப்பூர்வமானது (1956); தீர்ப்பாயங்கள் = உறுப்பு 262 + 1956 சட்டம்.",
        "Inter-State coordination relies on constitutional Article 263, statutory Zonal Councils, and Article 262 water tribunals.",
        "மாநிலங்களுக்கு இடையிலான ஒருங்கிணைப்பு அரசியலமைப்பு உறுப்பு 263, சட்டப்பூர்வ மண்டலக் குழுக்கள் மற்றும் 262 தீர்ப்பாயங்களை அடிப்படையாகக் கொண்டது.",
        tags=["Federal Architecture", "Synthesis Summary", "TNPSC PYQ Core"]
    ))

    return q
