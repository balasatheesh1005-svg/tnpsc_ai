# -*- coding: utf-8 -*-
"""
Builder for 25 Municipalities Match the Following MCQs (MUN_MF_001 to MUN_MF_025).
Strictly adheres to 24-field schema, balanced keys, and authentic Tamil translation.
"""
import json
import os
from mun_mcq_helper import make_mun_q
from rebalance_mun_helper import balance_question_keys

def get_match_25():
    questions = []

    def make_mf_q(qid, subtopic, l1_title, l2_title, l1_items_en, l1_items_ta, l2_items_en, l2_items_ta, opt_tuples, correct_key, exp_en, exp_ta, tip_en, tip_ta, fact_en, fact_ta, tags):
        # Format stem
        stem_en = f"Match List-I ({l1_title}) with List-II ({l2_title}) and select the correct answer using the code below:\nList-I:\n"
        for code, text in l1_items_en:
            stem_en += f"{code}. {text}\n"
        stem_en += "List-II:\n"
        for num, text in l2_items_en:
            stem_en += f"{num}. {text}\n"
        stem_en += "Select the correct code:"

        stem_ta = f"பட்டியல்-I ({l1_title}) ஐ பட்டியல்-II ({l2_title}) உடன் பொருத்தி, கீழ்க்கண்ட குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\nபட்டியல்-I:\n"
        for code, text in l1_items_ta:
            stem_ta += f"{code}. {text}\n"
        stem_ta += "பட்டியல்-II:\n"
        for num, text in l2_items_ta:
            stem_ta += f"{num}. {text}\n"
        stem_ta += "சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:"

        # opt_tuples is a list of 4 tuples: [("A", "a-1, b-2..."), ("B", ...), ...]
        en_opts = [t[1] for t in opt_tuples]
        ta_opts = [t[1] for t in opt_tuples]

        # Build why_not_others
        why_dict = {}
        for idx, key in enumerate(["A", "B", "C", "D"]):
            if key == correct_key:
                why_dict[f"why_{key.lower()}_en"] = f"Option {key} ({en_opts[idx]}) is correct. It accurately matches each item of List-I with its counterpart in List-II."
                why_dict[f"why_{key.lower()}_ta"] = f"விருப்பம் {key} ({en_opts[idx]}) சரியானது. இது பட்டியல்-I-ன் அனைத்து கூறுகளையும் பட்டியல்-II உடன் சரியாகப் பொருத்துகிறது."
            else:
                why_dict[f"why_{key.lower()}_en"] = f"Option {key} ({en_opts[idx]}) is incorrect due to mismatched pairings."
                why_dict[f"why_{key.lower()}_ta"] = f"விருப்பம் {key} ({en_opts[idx]}) தவறானது, தவறான இணைப்பைக் கொண்டுள்ளது."

        return make_mun_q(
            qid=qid,
            diff="Medium",
            qtype="Match the following",
            subtopic=subtopic,
            en_stem=stem_en,
            ta_stem=stem_ta,
            en_a=en_opts[0],
            ta_a=ta_opts[0],
            en_b=en_opts[1],
            ta_b=ta_opts[1],
            en_c=en_opts[2],
            ta_c=ta_opts[2],
            en_d=en_opts[3],
            ta_d=ta_opts[3],
            correct_key=correct_key,
            exp_en=exp_en,
            exp_ta=exp_ta,
            why_a_en=why_dict["why_a_en"],
            why_a_ta=why_dict["why_a_ta"],
            why_b_en=why_dict["why_b_en"],
            why_b_ta=why_dict["why_b_ta"],
            why_c_en=why_dict["why_c_en"],
            why_c_ta=why_dict["why_c_ta"],
            why_d_en=why_dict["why_d_en"],
            why_d_ta=why_dict["why_d_ta"],
            tip_en=tip_en,
            tip_ta=tip_ta,
            fact_en=fact_en,
            fact_ta=fact_ta,
            tags=tags
        )

    # MF01: Articles 243P to 243S
    questions.append(make_mf_q(
        qid="MUN_MF_001",
        subtopic="Constitutional Articles Set 1",
        l1_title="Constitutional Articles",
        l2_title="Subject Matter",
        l1_items_en=[("a", "Article 243P"), ("b", "Article 243Q"), ("c", "Article 243R"), ("d", "Article 243S")],
        l1_items_ta=[("a", "உறுப்பு 243P"), ("b", "உறுப்பு 243Q"), ("c", "உறுப்பு 243R"), ("d", "உறுப்பு 243S")],
        l2_items_en=[("1", "Definitions"), ("2", "Constitution of Municipalities (3 tiers)"), ("3", "Composition of Municipalities"), ("4", "Constitution and composition of Wards Committees")],
        l2_items_ta=[("1", "வரைவிலக்கணங்கள்"), ("2", "நகராட்சிகள் அமைத்தல் (3 அடுக்குகள்)"), ("3", "நகராட்சிகளின் கட்டமைப்பு"), ("4", "வார்டு குழுக்கள் அமைத்தல் மற்றும் கட்டமைப்பு")],
        opt_tuples=[("A", "a-1, b-2, c-3, d-4"), ("B", "a-2, b-1, c-4, d-3"), ("C", "a-3, b-4, c-1, d-2"), ("D", "a-4, b-3, c-2, d-1")],
        correct_key="A",
        exp_en="Accurate matching:\nArticle 243P - Definitions [1]\nArticle 243Q - Constitution of Municipalities [2]\nArticle 243R - Composition of Municipalities [3]\nArticle 243S - Wards Committees [4].",
        exp_ta="சரியான பொருத்தம்:\nஉறுப்பு 243P - வரைவிலக்கணங்கள் [1]\nஉறுப்பு 243Q - நகராட்சிகள் அமைத்தல் [2]\nஉறுப்பு 243R - நகராட்சிகளின் கட்டமைப்பு [3]\nஉறுப்பு 243S - வார்டு குழுக்கள் [4].",
        tip_en="P = Principles/Definitions; Q = Quantity (3 tiers); R = Representation; S = Sub-wards.",
        tip_ta="P = வரைவிலக்கணம்; Q = 3 அடுக்குகள்; R = கட்டமைப்பு; S = வார்டு குழுக்கள்.",
        fact_en="Articles 243P through 243S form the foundational structural provisions of Part IXA.",
        fact_ta="உறுப்புகள் 243P முதல் 243S வரை பகுதி IXA-ன் அடிப்படை கட்டமைப்பு விதிகளாகும்.",
        tags=["articles_243p_243s", "match_the_following", "constitution"]
    ))

    # MF02: Articles 243T to 243W
    questions.append(make_mf_q(
        qid="MUN_MF_002",
        subtopic="Constitutional Articles Set 2",
        l1_title="Constitutional Articles",
        l2_title="Subject Matter",
        l1_items_en=[("a", "Article 243T"), ("b", "Article 243U"), ("c", "Article 243V"), ("d", "Article 243W")],
        l1_items_ta=[("a", "உறுப்பு 243T"), ("b", "உறுப்பு 243U"), ("c", "உறுப்பு 243V"), ("d", "உறுப்பு 243W")],
        l2_items_en=[("1", "Reservation of seats"), ("2", "Duration of Municipalities"), ("3", "Disqualifications for membership"), ("4", "Powers, authority and responsibilities (12th Schedule)")],
        l2_items_ta=[("1", "இடஒதுக்கீடு"), ("2", "நகராட்சிகளின் பதவிக்காலம்"), ("3", "உறுப்பினர் தகுதிநீக்கங்கள்"), ("4", "அதிகாரங்கள் மற்றும் பொறுப்புகள் (12-வது அட்டவணை)")],
        opt_tuples=[("A", "a-1, b-2, c-3, d-4"), ("B", "a-2, b-1, c-4, d-3"), ("C", "a-4, b-3, c-2, d-1"), ("D", "a-3, b-4, c-1, d-2")],
        correct_key="A",
        exp_en="Accurate matching:\nArticle 243T - Reservation of seats [1]\nArticle 243U - Duration (5 years) [2]\nArticle 243V - Disqualifications [3]\nArticle 243W - Powers & 12th Schedule [4].",
        exp_ta="சரியான பொருத்தம்:\nஉறுப்பு 243T - இடஒதுக்கீடு [1]\nஉறுப்பு 243U - பதவிக்காலம் (5 ஆண்டுகள்) [2]\nஉறுப்பு 243V - தகுதிநீக்கங்கள் [3]\nஉறுப்பு 243W - அதிகாரங்கள் மற்றும் 12-வது அட்டவணை [4].",
        tip_en="T = Targeted reservation; U = Unlimited/5-year duration; V = Void/Disqualifications; W = Work/12th Schedule.",
        tip_ta="T = இடஒதுக்கீடு; U = 5 ஆண்டு பதவிக்காலம்; V = தகுதிநீக்கம்; W = பணிகள்.",
        fact_en="Article 243W is the direct parent article for the Twelfth Schedule.",
        fact_ta="உறுப்பு 243W என்பது 12-வது அட்டவணையை இயக்கும் நேரடித் தாய்க் கூறு ஆகும்.",
        tags=["articles_243t_243w", "match_the_following", "constitution"]
    ))

    # MF03: Articles 243X to 243ZA
    questions.append(make_mf_q(
        qid="MUN_MF_003",
        subtopic="Constitutional Articles Set 3",
        l1_title="Constitutional Articles",
        l2_title="Subject Matter",
        l1_items_en=[("a", "Article 243X"), ("b", "Article 243Y"), ("c", "Article 243Z"), ("d", "Article 243ZA")],
        l1_items_ta=[("a", "உறுப்பு 243X"), ("b", "உறுப்பு 243Y"), ("c", "உறுப்பு 243Z"), ("d", "உறுப்பு 243ZA")],
        l2_items_en=[("1", "Power to impose taxes, and Funds"), ("2", "Finance Commission"), ("3", "Audit of accounts of Municipalities"), ("4", "Elections to the Municipalities")],
        l2_items_ta=[("1", "வரி விதிக்கும் அதிகாரம் மற்றும் நிதிகள்"), ("2", "நிதி ஆணையம்"), ("3", "நகராட்சிகளின் கணக்குகள் தணிக்கை"), ("4", "நகராட்சிகளுக்கான தேர்தல்கள்")],
        opt_tuples=[("A", "a-1, b-2, c-3, d-4"), ("B", "a-3, b-4, c-1, d-2"), ("C", "a-2, b-1, c-4, d-3"), ("D", "a-4, b-3, c-2, d-1")],
        correct_key="A",
        exp_en="Accurate matching:\nArticle 243X - Taxes and Funds [1]\nArticle 243Y - Finance Commission [2]\nArticle 243Z - Audit of accounts [3]\nArticle 243ZA - Elections to Municipalities [4].",
        exp_ta="சரியான பொருத்தம்:\nஉறுப்பு 243X - வரிகள் மற்றும் நிதிகள் [1]\nஉறுப்பு 243Y - நிதி ஆணையம் [2]\nஉறுப்பு 243Z - கணக்குகள் தணிக்கை [3]\nஉறுப்பு 243ZA - நகராட்சித் தேர்தல்கள் [4].",
        tip_en="X = Tax; Y = Yearly Finance Commission; Z = Zero-error Audit; ZA = Ballot/Elections.",
        tip_ta="X = வரி; Y = நிதி ஆணையம்; Z = தணிக்கை; ZA = தேர்தல்.",
        fact_en="Article 243ZA vests election conduct in the State Election Commission.",
        fact_ta="உறுப்பு 243ZA தேர்தல்களை நடத்தும் அதிகாரத்தை மாநில தேர்தல் ஆணையத்திடம் ஒப்படைக்கிறது.",
        tags=["articles_243x_243za", "match_the_following", "constitution"]
    ))

    # MF04: Articles 243ZB to 243ZG
    questions.append(make_mf_q(
        qid="MUN_MF_004",
        subtopic="Constitutional Articles Set 4",
        l1_title="Constitutional Articles",
        l2_title="Subject Matter",
        l1_items_en=[("a", "Article 243ZB"), ("b", "Article 243ZD"), ("c", "Article 243ZE"), ("d", "Article 243ZG")],
        l1_items_ta=[("a", "உறுப்பு 243ZB"), ("b", "உறுப்பு 243ZD"), ("c", "உறுப்பு 243ZE"), ("d", "உறுப்பு 243ZG")],
        l2_items_en=[("1", "Application to Union Territories"), ("2", "Committee for District Planning (DPC)"), ("3", "Committee for Metropolitan Planning (MPC)"), ("4", "Bar to interference by courts in electoral matters")],
        l2_items_ta=[("1", "ஒன்றியப் பிரதேசங்களுக்குப் பொருந்துதல்"), ("2", "மாவட்ட திட்டக் குழு (DPC)"), ("3", "பெருநகர திட்டக் குழு (MPC)"), ("4", "தேர்தல் விவகாரங்களில் நீதிமன்றங்கள் தலையிடத் தடை")],
        opt_tuples=[("A", "a-1, b-2, c-3, d-4"), ("B", "a-4, b-3, c-2, d-1"), ("C", "a-2, b-1, c-4, d-3"), ("D", "a-3, b-4, c-1, d-2")],
        correct_key="A",
        exp_en="Accurate matching:\nArticle 243ZB - Application to UTs [1]\nArticle 243ZD - District Planning Committee [2]\nArticle 243ZE - Metropolitan Planning Committee [3]\nArticle 243ZG - Bar to interference by courts [4].",
        exp_ta="சரியான பொருத்தம்:\nஉறுப்பு 243ZB - யூனியன் பிரதேசங்கள் [1]\nஉறுப்பு 243ZD - மாவட்ட திட்டக் குழு [2]\nஉறுப்பு 243ZE - பெருநகர திட்டக் குழு [3]\nஉறுப்பு 243ZG - நீதிமன்றத் தலையீட்டிற்குத் தடை [4].",
        tip_en="ZD = District Planning; ZE = Extra-large/Metropolitan Planning; ZG = Gate closed to courts.",
        tip_ta="ZD = மாவட்ட திட்டமிடல்; ZE = பெருநகர திட்டமிடல்; ZG = நீதிமன்றங்களுக்குத் தடை.",
        fact_en="Article 243ZG is the closing article of Part IXA.",
        fact_ta="உறுப்பு 243ZG என்பது பகுதி IXA-ன் இறுதி உறுப்பாகும்.",
        tags=["articles_243zb_243zg", "match_the_following", "constitution"]
    ))

    # MF05: 12th Schedule Items Set 1
    questions.append(make_mf_q(
        qid="MUN_MF_005",
        subtopic="Twelfth Schedule Functional Items 1",
        l1_title="12th Schedule Item Number",
        l2_title="Functional Subject",
        l1_items_en=[("a", "Item 1"), ("b", "Item 2"), ("c", "Item 3"), ("d", "Item 4")],
        l1_items_ta=[("a", "இனம் 1"), ("b", "இனம் 2"), ("c", "இனம் 3"), ("d", "இனம் 4")],
        l2_items_en=[("1", "Urban planning including town planning"), ("2", "Regulation of land use and construction of buildings"), ("3", "Planning for economic and social development"), ("4", "Roads and bridges")],
        l2_items_ta=[("1", "நகர திட்டமிடல் உட்பட நகர்ப்புற திட்டமிடல்"), ("2", "நிலப் பயன்பாடு மற்றும் கட்டிடக் கட்டுமானத்தை ஒழுங்குபடுத்துதல்"), ("3", "பொருளாதார மற்றும் சமூக வளர்ச்சிக்கான திட்டமிடல்"), ("4", "சாலைகள் மற்றும் பாலங்கள்")],
        opt_tuples=[("A", "a-1, b-2, c-3, d-4"), ("B", "a-2, b-1, c-4, d-3"), ("C", "a-3, b-4, c-1, d-2"), ("D", "a-4, b-3, c-2, d-1")],
        correct_key="A",
        exp_en="The first 4 items of the Twelfth Schedule are:\nItem 1: Urban planning including town planning\nItem 2: Regulation of land use and construction of buildings\nItem 3: Planning for economic and social development\nItem 4: Roads and bridges.",
        exp_ta="12-வது அட்டவணையின் முதல் 4 பணிகள்:\nஇனம் 1: நகர்ப்புற திட்டமிடல்\nஇனம் 2: நிலப் பயன்பாடு ஒழுங்குமுறை\nஇனம் 3: பொருளாதார மற்றும் சமூக வளர்ச்சி திட்டமிடல்\nஇனம் 4: சாலைகள் மற்றும் பாலங்கள்.",
        tip_en="Items 1 to 4 focus on physical infrastructure and physical planning.",
        tip_ta="இனங்கள் 1 முதல் 4 வரை உள்கட்டமைப்பு மற்றும் திட்டமிடலில் கவனம் செலுத்துகின்றன.",
        fact_en="Item 5 is water supply for domestic, industrial, and commercial purposes.",
        fact_ta="இனம் 5 என்பது குடிநீர் மற்றும் தொழிற்துறை நீர் விநியோகமாகும்.",
        tags=["12th_schedule", "items_1_to_4", "match_the_following"]
    ))

    # MF06: 12th Schedule Items Set 2
    questions.append(make_mf_q(
        qid="MUN_MF_006",
        subtopic="Twelfth Schedule Functional Items 2",
        l1_title="12th Schedule Functional Domain",
        l2_title="Specific Constitutional Entry",
        l1_items_en=[("a", "Public Health & Sanitation"), ("b", "Fire Services"), ("c", "Urban Forestry"), ("d", "Protection of Weaker Sections")],
        l1_items_ta=[("a", "பொது சுகாதாரம் மற்றும் துப்புரவு"), ("b", "தீயணைப்பு சேவைகள்"), ("c", "நகர்ப்புற வனவியல்"), ("d", "பின்தங்கிய பிரிவினரின் பாதுகாப்பு")],
        l2_items_en=[("1", "Item 6"), ("2", "Item 7"), ("3", "Item 8"), ("4", "Item 9")],
        l2_items_ta=[("1", "இனம் 6"), ("2", "இனம் 7"), ("3", "இனம் 8"), ("4", "இனம் 9")],
        opt_tuples=[("A", "a-1, b-2, c-3, d-4"), ("B", "a-4, b-3, c-2, d-1"), ("C", "a-2, b-1, c-4, d-3"), ("D", "a-3, b-4, c-1, d-2")],
        correct_key="A",
        exp_en="Accurate matching in the Twelfth Schedule:\nItem 6: Public health, sanitation, conservancy, and solid waste management\nItem 7: Fire services\nItem 8: Urban forestry, protection of the environment\nItem 9: Safeguarding interests of weaker sections including the handicapped and mentally retarded.",
        exp_ta="12-வது அட்டவணையில் சரியான பொருத்தம்:\nஇனம் 6: பொது சுகாதாரம் மற்றும் திடக்கழிவு மேலாண்மை\nஇனம் 7: தீயணைப்பு சேவைகள்\nஇனம் 8: நகர்ப்புற வனவியல் மற்றும் சுற்றுச்சூழல்\nஇனம் 9: மாற்றுத்திறனாளிகள் உட்பட நலிந்த பிரிவினரின் பாதுகாப்பு.",
        tip_en="Health = 6; Fire = 7; Forestry = 8; Weaker sections = 9.",
        tip_ta="சுகாதாரம் = 6; தீயணைப்பு = 7; வனவியல் = 8; நலிந்த பிரிவினர் = 9.",
        fact_en="Solid waste management under Item 6 is enforced via Solid Waste Management Rules, 2016.",
        fact_ta="இனம் 6-ன் கீழ் திடக்கழிவு மேலாண்மை 2016 விதிகளின்படி செயல்படுத்தப்படுகிறது.",
        tags=["12th_schedule", "items_6_to_9", "match_the_following"]
    ))

    # MF07: 12th Schedule Items Set 3
    questions.append(make_mf_q(
        qid="MUN_MF_007",
        subtopic="Twelfth Schedule Functional Items 3",
        l1_title="Social & Urban Amenity",
        l2_title="12th Schedule Item Number",
        l1_items_en=[("a", "Slum improvement and upgradation"), ("b", "Urban poverty alleviation"), ("c", "Parks, gardens, playgrounds"), ("d", "Burials and cremation grounds")],
        l1_items_ta=[("a", "சேரிப் பகுதிகள் மேம்பாடு"), ("b", "நகர்ப்புற வறுமை ஒழிப்பு"), ("c", "பூங்காக்கள், தோட்டங்கள், விளையாட்டு மைதானங்கள்"), ("d", "மயானங்கள் மற்றும் இடுகாடுகள்")],
        l2_items_en=[("1", "Item 10"), ("2", "Item 11"), ("3", "Item 12"), ("4", "Item 14")],
        l2_items_ta=[("1", "இனம் 10"), ("2", "இனம் 11"), ("3", "இனம் 12"), ("4", "இனம் 14")],
        opt_tuples=[("A", "a-1, b-2, c-3, d-4"), ("B", "a-2, b-1, c-4, d-3"), ("C", "a-3, b-4, c-1, d-2"), ("D", "a-4, b-3, c-2, d-1")],
        correct_key="A",
        exp_en="Accurate matching:\nSlum improvement - Item 10\nUrban poverty alleviation - Item 11\nProvision of urban amenities (parks, playgrounds) - Item 12\nBurials, burial grounds, cremations - Item 14 (Item 13 is cultural, educational and aesthetic aspects).",
        exp_ta="சரியான பொருத்தம்:\nசேரி மேம்பாடு - இனம் 10\nநகர்ப்புற வறுமை ஒழிப்பு - இனம் 11\nபூங்காக்கள், விளையாட்டு மைதானங்கள் - இனம் 12\nமயானங்கள் - இனம் 14.",
        tip_en="Slum improvement (10) and Urban poverty alleviation (11) are key welfare items.",
        tip_ta="சேரி மேம்பாடு (10) மற்றும் வறுமை ஒழிப்பு (11) முக்கிய நலத் திட்டப் பணிகளாகும்.",
        fact_en="DAY-NULM operates under Item 11 for urban livelihoods.",
        fact_ta="நகர்ப்புற வாழ்வாதார இயக்கம் இனம் 11-ன் கீழ் செயல்படுகிறது.",
        tags=["12th_schedule", "items_10_to_14", "match_the_following"]
    ))

    # MF08: 12th Schedule Items Set 4
    questions.append(make_mf_q(
        qid="MUN_MF_008",
        subtopic="Twelfth Schedule Functional Items 4",
        l1_title="Regulatory & Civic Duty",
        l2_title="12th Schedule Item Number",
        l1_items_en=[("a", "Cattle pounds; prevention of cruelty to animals"), ("b", "Vital statistics including registration of births and deaths"), ("c", "Public amenities including street lighting, parking, bus stops"), ("d", "Regulation of slaughter houses and tanneries")],
        l1_items_ta=[("a", "கால்நடை தொழுவங்கள்; விலங்குகள் வதை தடுப்பு"), ("b", "பிறப்பு மற்றும் இறப்பு பதிவு உள்ளிட்ட புள்ளிவிவரங்கள்"), ("c", "தெருவிளக்கு, வாகன நிறுத்துமிடம், பேருந்து நிறுத்தங்கள்"), ("d", "கசாப்புக் கடைகள் மற்றும் தோல் பதனிடும் ஆலைகள் ஒழுங்குமுறை")],
        l2_items_en=[("1", "Item 15"), ("2", "Item 16"), ("3", "Item 17"), ("4", "Item 18")],
        l2_items_ta=[("1", "இனம் 15"), ("2", "இனம் 16"), ("3", "இனம் 17"), ("4", "இனம் 18")],
        opt_tuples=[("A", "a-1, b-2, c-3, d-4"), ("B", "a-4, b-3, c-2, d-1"), ("C", "a-3, b-1, c-4, d-2"), ("D", "a-2, b-4, c-1, d-3")],
        correct_key="A",
        exp_en="The concluding 4 items of the Twelfth Schedule are:\nItem 15: Cattle pounds; prevention of cruelty to animals\nItem 16: Vital statistics including registration of births and deaths\nItem 17: Public amenities including street lighting, parking lots, bus stops and public conveniences\nItem 18: Regulation of slaughter houses and tanneries.",
        exp_ta="12-வது அட்டவணையின் இறுதி 4 பணிகள்:\nஇனம் 15: கால்நடை தொழுவங்கள்\nஇனம் 16: பிறப்பு மற்றும் இறப்பு பதிவு\nஇனம் 17: தெருவிளக்குகள் மற்றும் பொது வசதிகள்\nஇனம் 18: கசாப்புக் கடைகள் ஒழுங்குமுறை.",
        tip_en="Item 18 is the final entry: Slaughter houses and tanneries.",
        tip_ta="12-வது அட்டவணையின் இறுதி இனம் 18: கசாப்புக் கடைகள் ஒழுங்குமுறை.",
        fact_en="Registration of births and deaths is mandatory under the Central RBD Act, 1969.",
        fact_ta="பிறப்பு/இறப்பு பதிவு 1969 மத்திய சட்டத்தின் கீழ் கட்டாயமாக்கப்பட்டுள்ளது.",
        tags=["12th_schedule", "items_15_to_18", "match_the_following"]
    ))

    # MF09: Early Post-Independence Committees
    questions.append(make_mf_q(
        qid="MUN_MF_009",
        subtopic="Urban Local Bodies Committees 1",
        l1_title="Committee Name / Chairman",
        l2_title="Year of Appointment",
        l1_items_en=[("a", "Local Finance Enquiry Committee (P.K. Wattal)"), ("b", "Taxation Enquiry Commission (John Matthai)"), ("c", "Committee on Training of Municipal Employees (Nur-ud-din Ahmed)"), ("d", "Augmentation of Financial Resources of ULBs (Dr. Zakaria)")],
        l1_items_ta=[("a", "உள்ளாட்சி நிதி ஆய்வுக் குழு (பி.கே. வாட்டல்)"), ("b", "வரிவிதிப்பு ஆய்வுக் குழு (ஜான் மத்தாய்)"), ("c", "நகராட்சிப் பணியாளர் பயிற்சிக் குழு (நூர்-உத்-தின் அகமது)"), ("d", "நகர்ப்புற உள்ளாட்சி நிதி ஆதாரப் பெருக்கக் குழு (டாக்டர் ஜகாரியா)")],
        l2_items_en=[("1", "1949"), ("2", "1953"), ("3", "1963"), ("4", "1963")],
        l2_items_ta=[("1", "1949"), ("2", "1953"), ("3", "1963"), ("4", "1963")],
        opt_tuples=[("A", "a-1, b-2, c-3, d-4"), ("B", "a-2, b-1, c-4, d-3"), ("C", "a-3, b-4, c-1, d-2"), ("D", "a-4, b-3, c-2, d-1")],
        correct_key="A",
        exp_en="Accurate chronological pairing:\nWattal Committee - 1949-51 [1]\nJohn Matthai Commission - 1953-54 [2]\nNur-ud-din Ahmed Committee - 1963 [3]\nDr. Rafiq Zakaria Committee - 1963 [4].",
        exp_ta="சரியான பொருத்தம்:\nவாட்டல் குழு - 1949-51 [1]\nஜான் மத்தாய் குழு - 1953-54 [2]\nநூர்-உத்-தின் அகமது குழு - 1963 [3]\nடாக்டர் ரபீக் ஜகாரியா குழு - 1963 [4].",
        tip_en="Wattal (1949) was the first major municipal finance committee in independent India.",
        tip_ta="வாட்டல் குழு (1949) சுதந்திர இந்தியாவின் முதல் பெரிய நகராட்சி நிதிக் குழுவாகும்.",
        fact_en="Zakaria Committee established physical norms for drinking water and sewerage per capita.",
        fact_ta="ஜகாரியா குழு தனிநபர் குடிநீர் மற்றும் கழிவுநீர் தேவைகளுக்கான தரநிலைகளை வகுத்தது.",
        tags=["committees", "post_independence", "match_the_following"]
    ))

    # MF10: Late 20th Century Committees
    questions.append(make_mf_q(
        qid="MUN_MF_010",
        subtopic="Urban Local Bodies Committees 2",
        l1_title="Committee / Commission",
        l2_title="Key Mandate / Report",
        l1_items_en=[("a", "Rural-Urban Relationship Committee (1963)"), ("b", "National Commission on Urbanisation (1985)"), ("c", "P.K. Thungon Committee (1988)"), ("d", "Second Administrative Reforms Commission (2007)")],
        l1_items_ta=[("a", "கிராமப்புற-நகர்ப்புற உறவுக் குழு (1963)"), ("b", "தேசிய நகரமயமாக்கல் ஆணையம் (1985)"), ("c", "பி.கே. துங்கன் குழு (1988)"), ("d", "இரண்டாவது நிர்வாக சீர்திருத்த ஆணையம் (2007)")],
        l2_items_en=[("1", "Criteria for defining urban areas and rural-urban integration"), ("2", "First comprehensive national urban policy roadmap (Charles Correa)"), ("3", "Recommended constitutional recognition for local bodies"), ("4", "Report on Local Governance: An Inspiring Journey into the Future")],
        l2_items_ta=[("1", "நகர்ப்புற பகுதிகளை வரையறுத்தல் மற்றும் ஊரக-நகர்ப்புற ஒருங்கிணைப்பு"), ("2", "முதல் விரிவான தேசிய நகர்ப்புற கொள்கை வரைபடம் (சார்லஸ் கொரியா)"), ("3", "உள்ளாட்சி அமைப்புகளுக்கு அரசியலமைப்பு அங்கீகாரம் பரிந்துரைத்தது"), ("4", "உள்ளாட்சி நிர்வாகம்: எதிர்காலத்திற்கான ஒரு ஊக்கமளிக்கும் பயணம் அறிக்கை")],
        opt_tuples=[("A", "a-1, b-2, c-3, d-4"), ("B", "a-3, b-4, c-1, d-2"), ("C", "a-2, b-1, c-4, d-3"), ("D", "a-4, b-3, c-2, d-1")],
        correct_key="A",
        exp_en="Accurate matching:\nRural-Urban Relationship - Criteria for urban areas [1]\nNational Commission on Urbanisation - National urban roadmap under Correa [2]\nThungon Committee - Constitutional status recommendation [3]\n2nd ARC (6th Report) - Local Governance report [4].",
        exp_ta="சரியான பொருத்தம்:\nகிராமப்புற-நகர்ப்புற உறவு - நகர்ப்புற வரையறை அளவுகோல்கள் [1]\nதேசிய நகரமயமாக்கல் ஆணையம் - சார்லஸ் கொரியா அறிக்கை [2]\nதுங்கன் குழு - அரசியலமைப்பு அந்தஸ்து [3]\n2-வது ARC - உள்ளாட்சி நிர்வாக அறிக்கை [4].",
        tip_en="2nd ARC's 6th Report is dedicated exclusively to Local Governance.",
        tip_ta="2-வது நிர்வாக சீர்திருத்த ஆணையத்தின் 6-வது அறிக்கை உள்ளாட்சி நிர்வாகத்திற்கு அர்ப்பணிக்கப்பட்டது.",
        fact_en="Charles Correa was a legendary architect who planned Navi Mumbai.",
        fact_ta="சார்லஸ் கொரியா நவி மும்பையை திட்டமிட்ட புகழ்பெற்ற கட்டிடக் கலைஞர் ஆவார்.",
        tags=["committees_2", "national_urban_policy", "match_the_following"]
    ))

    # MF11: Types of ULBs 1
    questions.append(make_mf_q(
        qid="MUN_MF_011",
        subtopic="Types of Urban Local Bodies 1",
        l1_title="Urban Local Body Type",
        l2_title="Defining Characteristic",
        l1_items_en=[("a", "Municipal Corporation"), ("b", "Municipality (Municipal Council)"), ("c", "Notified Area Committee"), ("d", "Town Area Committee")],
        l1_items_ta=[("a", "மாநகராட்சி"), ("b", "நகர்மன்றம் (நகராட்சி)"), ("c", "அறிவிக்கப்பட்ட பகுதி குழு"), ("d", "நகரப் பகுதி குழு")],
        l2_items_en=[("1", "Established for large cities by special Acts of State Legislature"), ("2", "Constituted for smaller urban areas"), ("3", "Created by gazette notification for fast industrializing towns"), ("4", "Constituted by separate act for small towns with limited functions")],
        l2_items_ta=[("1", "மாநில சட்டமன்றத்தின் சிறப்புச் சட்டம் மூலம் பெரிய நகரங்களுக்கு அமைக்கப்படுகிறது"), ("2", "சிறிய நகர்ப்புற பகுதிகளுக்காக அமைக்கப்படுகிறது"), ("3", "விரைவாக தொழில்மயமாகும் நகரங்களுக்கு அரசிதழ் அறிவிப்பு மூலம் உருவாக்கப்படுகிறது"), ("4", "வரையறுக்கப்பட்ட பணிகளுடன் சிறிய நகரங்களுக்கு அமைக்கப்படுகிறது")],
        opt_tuples=[("A", "a-1, b-2, c-3, d-4"), ("B", "a-2, b-1, c-4, d-3"), ("C", "a-3, b-4, c-1, d-2"), ("D", "a-4, b-3, c-2, d-1")],
        correct_key="A",
        exp_en="Accurate matching:\nMunicipal Corporation - Large cities under special statutes [1]\nMunicipality - Smaller urban areas [2]\nNotified Area Committee - Fast industrializing towns via gazette [3]\nTown Area Committee - Small towns with limited functions [4].",
        exp_ta="சரியான பொருத்தம்:\nமாநகராட்சி - பெரிய நகரங்கள் [1]\nநகராட்சி - சிறிய நகரங்கள் [2]\nஅறிவிக்கப்பட்ட பகுதி - தொழில்மய நகரங்கள் [3]\nநகரப் பகுதி குழு - சிறிய நகரங்கள் [4].",
        tip_en="Corporation = Million+ / Large; Municipality = Medium; Notified = Fast industrial; Town Area = Small semi-municipal.",
        tip_ta="மாநகராட்சி = பெரிய நகரம்; நகராட்சி = நடுத்தர நகரம்; அறிவிக்கப்பட்ட பகுதி = தொழிற்பகுதி; நகரப் பகுதி = சிறிய நகரம்.",
        fact_en="Notified Area Committees have all nominated members.",
        fact_ta="அறிவிக்கப்பட்ட பகுதி குழுக்கள் அனைத்தும் நியமன உறுப்பினர்களைக் கொண்டவை.",
        tags=["types_of_ulbs", "classification", "match_the_following"]
    ))

    # MF12: Types of ULBs 2
    questions.append(make_mf_q(
        qid="MUN_MF_012",
        subtopic="Types of Urban Local Bodies 2",
        l1_title="Special Urban Body Type",
        l2_title="Administrative Governing Authority",
        l1_items_en=[("a", "Cantonment Board"), ("b", "Township"), ("c", "Port Trust"), ("d", "Special Purpose Agency")],
        l1_items_ta=[("a", "பாசறை வாரியம்"), ("b", "நகரியம் (Township)"), ("c", "துறைமுகப் பொறுப்புக் கழகம்"), ("d", "தனி நோக்க முகமை")],
        l2_items_en=[("1", "Union Ministry of Defence (Cantonments Act, 2006)"), ("2", "Public sector undertaking / industrial enterprise management"), ("3", "Act of Parliament for major maritime port township"), ("4", "Statutory parastatal for single function (e.g. water board, housing board)")],
        l2_items_ta=[("1", "மத்திய பாதுகாப்பு அமைச்சகம் (பாசறைகள் சட்டம், 2006)"), ("2", "பொதுத்துறை நிறுவனம் / தொழிற்துறை நிர்வாகம்"), ("3", "முக்கிய கடல் துறைமுக நகரியத்திற்கான நாடாளுமன்ற சட்டம்"), ("4", "ஒற்றைப் பணிக்கான சட்டப்பூர்வ வாரியம் (குடிநீர் வாரியம் போன்றவை)")],
        opt_tuples=[("A", "a-1, b-2, c-3, d-4"), ("B", "a-4, b-3, c-2, d-1"), ("C", "a-2, b-1, c-4, d-3"), ("D", "a-3, b-4, c-1, d-2")],
        correct_key="A",
        exp_en="Accurate matching:\nCantonment Board - Ministry of Defence [1]\nTownship - PSU / Industrial enterprise [2]\nPort Trust - Major ports under Parliamentary Act [3]\nSpecial Purpose Agency - Functional parastatals [4].",
        exp_ta="சரியான பொருத்தம்:\nபாசறை வாரியம் - பாதுகாப்பு அமைச்சகம் [1]\nநகரியம் - பொதுத்துறை நிறுவனம் [2]\nதுறைமுக அறக்கட்டளை - நாடாளுமன்ற சட்டம் [3]\nதனி நோக்க முகமை - சட்டப்பூர்வ வாரியங்கள் [4].",
        tip_en="Cantonment = Defence; Port Trust = Shipping/Ports; Township = Industry PSU; SPA = Function-specific.",
        tip_ta="பாசறை = பாதுகாப்பு; துறைமுகம் = கப்பல் போக்குவரத்து; நகரியம் = PSU; சிறப்பு முகமை = ஒற்றைப் பணி.",
        fact_en="BHEL Ranipet and Neyveli Lignite Township are classic examples of industrial townships in TN.",
        fact_ta="நெய்வேலி நிலக்கரி நகரியம் தமிழ்நாட்டில் உள்ள நகரியத்திற்கு சிறந்த உதாரணமாகும்.",
        tags=["special_ulbs", "port_trust_cantonment", "match_the_following"]
    ))

    # MF13: Historical Milestones
    questions.append(make_mf_q(
        qid="MUN_MF_013",
        subtopic="Historical Landmarks",
        l1_title="Historical Landmark",
        l2_title="Significance",
        l1_items_en=[("a", "Madras Royal Charter (1687)"), ("b", "Mayor's Courts Charter (1726)"), ("c", "Lord Mayo's Resolution (1870)"), ("d", "Lord Ripon's Resolution (1882)")],
        l1_items_ta=[("a", "மெட்ராஸ் அரச பட்டயம் (1687)"), ("b", "மேயர் நீதிமன்ற பட்டயம் (1726)"), ("c", "மேயோ பிரபுவின் தீர்மானம் (1870)"), ("d", "ரிப்பன் பிரபுவின் தீர்மானம் (1882)")],
        l2_items_en=[("1", "First Municipal Corporation in India and the Commonwealth outside Britain"), ("2", "Established uniform municipal corporations and judicial Mayor's Courts in 3 Presidencies"), ("3", "Initiated financial decentralization and local taxation powers"), ("4", "Magna Carta of Local Self-Government introducing elected non-official majority")],
        l2_items_ta=[("1", "இந்தியாவில் மற்றும் பிரிட்டனுக்கு வெளியே காமன்வெல்த்தின் முதல் மாநகராட்சி"), ("2", "3 மாகாணங்களிலும் ஒரே மாதிரியான மாநகராட்சிகள் மற்றும் மேயர் நீதிமன்றங்களை அமைத்தது"), ("3", "நிதிப் பரவலாக்கம் மற்றும் உள்ளூர் வரி விதிப்பு அதிகாரங்களைத் தொடங்கியது"), ("4", "தேர்ந்தெடுக்கப்பட்ட அதிகாரப்பூர்வமற்ற பெரும்பான்மையை அறிமுகப்படுத்திய உள்ளாட்சியின் மகா சாசனம்")],
        opt_tuples=[("A", "a-1, b-2, c-3, d-4"), ("B", "a-2, b-1, c-4, d-3"), ("C", "a-4, b-3, c-2, d-1"), ("D", "a-3, b-4, c-1, d-2")],
        correct_key="A",
        exp_en="Accurate historical matching:\n1687 - Madras Corporation chartered [1]\n1726 - Mayor's Courts in Bombay, Calcutta, Madras [2]\n1870 - Financial decentralization under Mayo [3]\n1882 - Magna Carta of Local Self-Government under Ripon [4].",
        exp_ta="சரியான வரலாற்றுப் பொருத்தம்:\n1687 - மெட்ராஸ் மாநகராட்சி பட்டயம் [1]\n1726 - மூன்று மாகாணங்களிலும் மேயர் நீதிமன்றங்கள் [2]\n1870 - மேயோவின் நிதிப் பரவலாக்கம் [3]\n1882 - ரிப்பனின் உள்ளாட்சி மகா சாசனம் [4].",
        tip_en="Chronology: 1687 -> 1726 -> 1870 -> 1882.",
        tip_ta="காலவரிசை: 1687 -> 1726 -> 1870 -> 1882.",
        fact_en="The 1726 Charter made corporations institutions of the British Crown rather than Company creations.",
        fact_ta="1726 பட்டயம் மாநகராட்சிகளை கம்பெனிக்கு பதிலாக பிரிட்டிஷ் அரச மகுடத்தின் அமைப்புகளாக மாற்றியது.",
        tags=["historical_landmarks", "mayo_ripon", "match_the_following"]
    ))

    # MF14: Key Population & Ratio Thresholds
    questions.append(make_mf_q(
        qid="MUN_MF_014",
        subtopic="Constitutional Thresholds",
        l1_title="Institutional Structure",
        l2_title="Constitutional Threshold / Ratio",
        l1_items_en=[("a", "Wards Committees (Article 243S)"), ("b", "Metropolitan Area (Article 243P(c))"), ("c", "District Planning Committee elected proportion"), ("d", "Metropolitan Planning Committee elected proportion")],
        l1_items_ta=[("a", "வார்டு குழுக்கள் (உறுப்பு 243S)"), ("b", "பெருநகரப் பகுதி (உறுப்பு 243P(c))"), ("c", "மாவட்ட திட்டக் குழு தேர்ந்தெடுக்கப்படும் விகிதம்"), ("d", "பெருநகர திட்டக் குழு தேர்ந்தெடுக்கப்படும் விகிதம்")],
        l2_items_en=[("1", "Population of 3 lakhs or more"), ("2", "Population of 10 lakhs (one million) or more"), ("3", "Not less than four-fifths (4/5)"), ("4", "Not less than two-thirds (2/3)")],
        l2_items_ta=[("1", "3 லட்சம் அல்லது அதற்கு மேற்பட்ட மக்கள் தொகை"), ("2", "10 லட்சம் (ஒரு மில்லியன்) அல்லது அதற்கு மேற்பட்ட மக்கள் தொகை"), ("3", "ஐந்தில் நான்கு பங்குக்கு குறையாமல் (4/5)"), ("4", "மூன்றில் இரண்டு பங்குக்கு குறையாமல் (2/3)")],
        opt_tuples=[("A", "a-1, b-2, c-3, d-4"), ("B", "a-2, b-1, c-4, d-3"), ("C", "a-3, b-4, c-1, d-2"), ("D", "a-4, b-3, c-2, d-1")],
        correct_key="A",
        exp_en="Accurate matching of thresholds:\nWards Committees - 3 lakhs or more [1]\nMetropolitan Area - 10 lakhs or more [2]\nDPC elected proportion - Not less than 4/5 [3]\nMPC elected proportion - Not less than 2/3 [4].",
        exp_ta="சரியான அளவுகோல் பொருத்தம்:\nவார்டு குழுக்கள் - 3 லட்சம் அல்லது அதற்கு மேல் [1]\nபெருநகரப் பகுதி - 10 லட்சம் அல்லது அதற்கு மேல் [2]\nDPC தேர்தல் விகிதம் - 4/5 பங்கு [3]\nMPC தேர்தல் விகிதம் - 2/3 பங்கு [4].",
        tip_en="3 Lakhs = Wards Committee; 10 Lakhs = Metropolitan; 4/5 = DPC; 2/3 = MPC.",
        tip_ta="3 லட்சம் = வார்டு குழு; 10 லட்சம் = பெருநகரம்; 4/5 = DPC; 2/3 = MPC.",
        fact_en="Memorize these 4 numbers: 3 lakhs, 10 lakhs, 4/5, and 2/3.",
        fact_ta="இந்த நான்கு எண்களை நினைவில் கொள்ளுங்கள்: 3 லட்சம், 10 லட்சம், 4/5, மற்றும் 2/3.",
        tags=["thresholds", "ratios", "match_the_following"]
    ))

    # MF15: Municipal Revenue Types
    questions.append(make_mf_q(
        qid="MUN_MF_015",
        subtopic="Municipal Finances Revenue Sources",
        l1_title="Revenue Category",
        l2_title="Specific Revenue Stream",
        l1_items_en=[("a", "Direct Property Tax"), ("b", "Profession Tax"), ("c", "Non-Tax Own Revenue"), ("d", "Fiscal Transfer")],
        l1_items_ta=[("a", "நேரடி சொத்துவரி"), ("b", "தொழில் வரி"), ("c", "வரி அல்லாத சொந்த வருவாய்"), ("d", "நிதிப் பகிர்வு / மாற்றங்கள்")],
        l2_items_en=[("1", "Tax on land and buildings based on annual rental value"), ("2", "Tax on professions, trades, and employments capped at Rs 2,500/year"), ("3", "Water charges, building plan fees, market lease rentals"), ("4", "Devolution from State Net Tax Revenue recommended by SFC")],
        l2_items_ta=[("1", "ஆண்டு வாடகை மதிப்பின் அடிப்படையில் நிலம் மற்றும் கட்டிடங்கள் மீதான வரி"), ("2", "ஆண்டுக்கு அதிகபட்சம் ரூ 2,500 வரை விதிக்கப்படும் தொழில்கள் மீதான வரி"), ("3", "குடிநீர்க் கட்டணம், கட்டிட அனுமதி கட்டணம், சந்தைக் குத்தகை"), ("4", "SFC பரிந்துரைப்படி மாநில நிகர வரி வருவாயிலிருந்து ஒதுக்கீடு")],
        opt_tuples=[("A", "a-1, b-2, c-3, d-4"), ("B", "a-2, b-1, c-4, d-3"), ("C", "a-3, b-4, c-1, d-2"), ("D", "a-4, b-3, c-2, d-1")],
        correct_key="A",
        exp_en="Accurate revenue matching:\nProperty tax - Tax on lands and buildings [1]\nProfession tax - Article 276 tax capped at Rs 2,500 [2]\nNon-tax revenue - Fees, fines, water charges, leases [3]\nFiscal transfer - State tax devolution via SFC [4].",
        exp_ta="சரியான வருவாய் பொருத்தம்:\nசொத்துவரி - நிலம் மற்றும் கட்டிடங்கள் மீதான வரி [1]\nதொழில் வரி - அதிகபட்சம் ரூ 2,500 வரம்பிற்குட்பட்ட வரி [2]\nவரி அல்லாத வருவாய் - கட்டணங்கள், குடிநீர் கட்டணம் [3]\nநிதிப் பகிர்வு - SFC பரிந்துரைத்த வரிப் பகிர்வு [4].",
        tip_en="Article 276 caps Profession Tax at Rs. 2,500 per person per annum.",
        tip_ta="உறுப்பு 276 தொழில் வரியை ஆண்டுக்கு அதிகபட்சம் ரூ 2,500 என வரம்பிடுகிறது.",
        fact_en="5th SFC in Tamil Nadu recommended devolving 10% of state own tax revenue to local bodies.",
        fact_ta="தமிழ்நாட்டின் 5-வது மாநில நிதி ஆணையம் 10% வரிப் பகிர்வை பரிந்துரைத்தது.",
        tags=["municipal_revenue", "property_tax", "profession_tax", "match_the_following"]
    ))

    # MF16: Authorities in Municipal Corporation
    questions.append(make_mf_q(
        qid="MUN_MF_016",
        subtopic="Municipal Authorities Corporation",
        l1_title="Municipal Corporation Authority",
        l2_title="Core Role & Function",
        l1_items_en=[("a", "The Council"), ("b", "The Mayor"), ("c", "Standing Committees"), ("d", "The Municipal Commissioner")],
        l1_items_ta=[("a", "மாநகராட்சி மன்றம்"), ("b", "மேயர்"), ("c", "நிலைக்குழுக்கள்"), ("d", "மாநகராட்சி ஆணையர்")],
        l2_items_en=[("1", "Deliberative and legislative body representing all wards"), ("2", "First citizen and presiding officer of the corporation council"), ("3", "Specialized committees dealing with taxation, health, works, accounts"), ("4", "Chief executive officer implementing council resolutions and administration")],
        l2_items_ta=[("1", "அனைத்து வார்டுகளையும் பிரதிநிதித்துவப்படுத்தும் சட்டமியற்றும் மற்றும் விவாத மன்றம்"), ("2", "நகரத்தின் முதல் குடிமகன் மற்றும் மன்றக் கூட்டங்களின் தலைவர்"), ("3", "வரிவிதிப்பு, சுகாதாரம், பணிகள், கணக்குகளைக் கவனிக்கும் சிறப்புக் குழுக்கள்"), ("4", "மன்றத் தீர்மானங்கள் மற்றும் நிர்வாகத்தை செயல்படுத்தும் முதன்மை நிர்வாக அதிகாரி")],
        opt_tuples=[("A", "a-1, b-2, c-3, d-4"), ("B", "a-2, b-1, c-4, d-3"), ("C", "a-4, b-3, c-2, d-1"), ("D", "a-3, b-4, c-1, d-2")],
        correct_key="A",
        exp_en="Accurate matching of municipal authorities:\nCouncil - Deliberative body [1]\nMayor - First Citizen & Presiding Officer [2]\nStanding Committees - Functional working committees [3]\nCommissioner - Chief Executive Officer [4].",
        exp_ta="சரியான பொருத்தம்:\nமன்றம் - விவாத மற்றும் கொள்கை அமைப்பு [1]\nமேயர் - முதல் குடிமகன் & கூட்டத் தலைவர் [2]\nநிலைக்குழுக்கள் - குறிப்பிட்ட பணிக் குழுக்கள் [3]\nஆணையர் - முதன்மை நிர்வாக அதிகாரி [4].",
        tip_en="Council + Standing Committees + Mayor = Deliberative Wing; Commissioner = Executive Wing.",
        tip_ta="மன்றம் + நிலைக்குழுக்கள் + மேயர் = விவாதப் பிரிவு; ஆணையர் = நிர்வாகப் பிரிவு.",
        fact_en="Chennai Corporation has 6 statutory Standing Committees.",
        fact_ta="சென்னை மாநகராட்சி 6 சட்டப்பூர்வ நிலைக்குழுக்களைக் கொண்டுள்ளது.",
        tags=["municipal_authorities", "corporation", "match_the_following"]
    ))

    # MF17: Oldest Municipal Corporations of Tamil Nadu
    questions.append(make_mf_q(
        qid="MUN_MF_017",
        subtopic="Tamil Nadu Corporations Chronology",
        l1_title="Municipal Corporation in TN",
        l2_title="Year of Elevation to Corporation",
        l1_items_en=[("a", "Madras (Chennai)"), ("b", "Madurai"), ("c", "Coimbatore"), ("d", "Tiruchirappalli")],
        l1_items_ta=[("a", "சென்னை"), ("b", "மதுரை"), ("c", "கோயம்புத்தூர்"), ("d", "திருச்சிராப்பள்ளி")],
        l2_items_en=[("1", "1688"), ("2", "1971"), ("3", "1981"), ("4", "1994")],
        l2_items_ta=[("1", "1688"), ("2", "1971"), ("3", "1981"), ("4", "1994")],
        opt_tuples=[("A", "a-1, b-2, c-3, d-4"), ("B", "a-2, b-1, c-4, d-3"), ("C", "a-3, b-4, c-1, d-2"), ("D", "a-4, b-3, c-2, d-1")],
        correct_key="A",
        exp_en="Accurate chronological pairing of early Tamil Nadu Corporations:\nChennai - 1688 (first)\nMadurai - 1971 (second)\nCoimbatore - 1981 (third)\nTiruchirappalli - 1994 (fourth, along with Salem).",
        exp_ta="தமிழ்நாட்டின் முதல் 4 மாநகராட்சிகள்:\nசென்னை - 1688 (முதல்)\nமதுரை - 1971 (இரண்டாவது)\nகோயம்புத்தூர் - 1981 (மூன்றாவது)\nதிருச்சிராப்பள்ளி - 1994 (நான்காவது, சேலத்துடன் இணைந்து).",
        tip_en="Order of first 4 Corporations in TN: Chennai (1688) -> Madurai (1971) -> Coimbatore (1981) -> Tiruchirappalli/Salem (1994).",
        tip_ta="தமிழ்நாட்டின் முதல் 4 மாநகராட்சிகள்: சென்னை (1688) -> மதுரை (1971) -> கோவை (1981) -> திருச்சி (1994).",
        fact_en="Tamil Nadu currently has 21 Municipal Corporations.",
        fact_ta="தமிழ்நாட்டில் தற்போது 21 மாநகராட்சிகள் உள்ளன.",
        tags=["tn_corporations", "madras_madurai_coimbatore", "match_the_following"]
    ))

    # MF18: Recent Corporations in TN
    questions.append(make_mf_q(
        qid="MUN_MF_018",
        subtopic="Recent Tamil Nadu Corporations",
        l1_title="City Corporation",
        l2_title="Year Established as Corporation",
        l1_items_en=[("a", "Tiruppur & Erode"), ("b", "Dindigul & Thanjavur"), ("c", "Hosur & Nagercoil"), ("d", "Tambaram & Kanchipuram")],
        l1_items_ta=[("a", "திருப்பூர் & ஈரோடு"), ("b", "திண்டுக்கல் & தஞ்சாவூர்"), ("c", "ஓசூர் & நாகர்கோவில்"), ("d", "தாம்பரம் & காஞ்சிபுரம்")],
        l2_items_en=[("1", "2008"), ("2", "2014"), ("3", "2019"), ("4", "2021")],
        l2_items_ta=[("1", "2008"), ("2", "2014"), ("3", "2019"), ("4", "2021")],
        opt_tuples=[("A", "a-1, b-2, c-3, d-4"), ("B", "a-4, b-3, c-2, d-1"), ("C", "a-2, b-1, c-4, d-3"), ("D", "a-3, b-4, c-1, d-2")],
        correct_key="A",
        exp_en="Accurate matching of newer Tamil Nadu Corporations:\nTiruppur & Erode - 2008 [1]\nDindigul & Thanjavur - 2014 [2]\nHosur & Nagercoil - 2019 (along with Avadi) [3]\nTambaram, Kanchipuram, Karur, Cuddalore, Sivakasi - 2021 [4].",
        exp_ta="சரியான பொருத்தம்:\nதிருப்பூர் & ஈரோடு - 2008 [1]\nதிண்டுக்கல் & தஞ்சாவூர் - 2014 [2]\nஓசூர் & நாகர்கோவில் - 2019 [3]\nதாம்பரம், காஞ்சிபுரம், கரூர், கடலூர், சிவகாசி - 2021 [4].",
        tip_en="2008: Tiruppur, Erode, Vellore, Thoothukudi; 2014: Dindigul, Thanjavur; 2019: Hosur, Nagercoil, Avadi; 2021: Tambaram, Kanchipuram, Karur, Cuddalore, Sivakasi.",
        tip_ta="2008, 2014, 2019, 2021 ஆகிய ஆண்டுகளில் புதிய மாநகராட்சிகள் அறிவிக்கப்பட்டன.",
        fact_en="Tambaram is the second Municipal Corporation in the Chennai Metropolitan Area after GCC.",
        fact_ta="தாம்பரம் சென்னை பெருநகரப் பகுதியில் அமைந்துள்ள இரண்டாவது மாநகராட்சியாகும்.",
        tags=["recent_corporations", "tamil_nadu_polity", "match_the_following"]
    ))

    # MF19: Central Urban Missions
    questions.append(make_mf_q(
        qid="MUN_MF_019",
        subtopic="Central Urban Schemes",
        l1_title="Central Urban Scheme",
        l2_title="Core Objective",
        l1_items_en=[("a", "AMRUT (Atal Mission for Rejuvenation and Urban Transformation)"), ("b", "Smart Cities Mission"), ("c", "PMAY-Urban (Pradhan Mantri Awas Yojana)"), ("d", "Swachh Bharat Mission (Urban)")],
        l1_items_ta=[("a", "அம்ருத் (AMRUT) திட்டம்"), ("b", "ஸ்மார்ட் சிட்டீஸ் திட்டம்"), ("c", "பிரதமர் ஆவாஸ் திட்டம் (நகர்ப்புறம்)"), ("d", "தூய்மை இந்தியா இயக்கம் (நகர்ப்புறம்)")],
        l2_items_en=[("1", "Universal tap water supply and sewerage connections in 500 cities"), ("2", "Promoting cities with core infrastructure and smart digital solutions in 100 cities"), ("3", "Housing for all urban poor through pucca houses"), ("4", "Open defecation free cities and 100% scientific solid waste management")],
        l2_items_ta=[("1", "500 நகரங்களில் அனைவருக்கும் குழாய் குடிநீர் மற்றும் கழிவுநீர் இணைப்பு"), ("2", "100 நகரங்களில் நவீன உள்கட்டமைப்பு மற்றும் ஸ்மார்ட் டிஜிட்டல் தீர்வுகள்"), ("3", "நகர்ப்புற ஏழைகள் அனைவருக்கும் நிரந்தர கான்கிரீட் வீடுகள்"), ("4", "திறந்தவெளிக் கழிப்பிடமற்ற நகரங்கள் மற்றும் 100% அறிவியல் பூர்வ திடக்கழிவு மேலாண்மை")],
        opt_tuples=[("A", "a-1, b-2, c-3, d-4"), ("B", "a-2, b-1, c-4, d-3"), ("C", "a-3, b-4, c-1, d-2"), ("D", "a-4, b-3, c-2, d-1")],
        correct_key="A",
        exp_en="Accurate matching of flagship urban missions:\nAMRUT - Water supply and sewerage in 500 cities [1]\nSmart Cities - 100 lighthouse cities with smart technology [2]\nPMAY-U - Pucca housing for urban poor [3]\nSBM-U - ODF status and solid waste processing [4].",
        exp_ta="முக்கிய நகர்ப்புற திட்டங்கள் பொருத்தம்:\nஅம்ருத் - 500 நகரங்களில் குடிநீர் மற்றும் கழிவுநீர் [1]\nஸ்மார்ட் சிட்டீஸ் - 100 நகரங்களில் டிஜிட்டல் தீர்வுகள் [2]\nPMAY-U - நகர்ப்புற ஏழைகளுக்கு வீடுகள் [3]\nSBM-U - திறந்தவெளிக் கழிப்பிடமற்ற நகரங்கள் [4].",
        tip_en="AMRUT launched in 2015 replaces JNNURM for basic water/sewerage infrastructure.",
        tip_ta="அம்ருத் 2015-ல் தொடங்கப்பட்டு அடிப்படை குடிநீர் வசதிகளை மேம்படுத்துகிறது.",
        fact_en="All these schemes operate under the Union Ministry of Housing and Urban Affairs (MoHUA).",
        fact_ta="இத்திட்டங்கள் அனைத்தும் மத்திய வீட்டுவசதி மற்றும் நகர்ப்புற விவகாரங்கள் அமைச்சகத்தின் கீழ் இயங்குகின்றன.",
        tags=["urban_missions", "amrut_smart_cities", "match_the_following"]
    ))

    # MF20: Constitutional Commissions Comparison
    questions.append(make_mf_q(
        qid="MUN_MF_020",
        subtopic="Constitutional Bodies Comparison",
        l1_title="Constitutional Body",
        l2_title="Governing Constitutional Article",
        l1_items_en=[("a", "State Finance Commission for Municipalities"), ("b", "State Election Commission for Municipalities"), ("c", "Union Finance Commission"), ("d", "Election Commission of India")],
        l1_items_ta=[("a", "நகராட்சிகளுக்கான மாநில நிதி ஆணையம்"), ("b", "நகராட்சிகளுக்கான மாநில தேர்தல் ஆணையம்"), ("c", "மத்திய நிதி ஆணையம்"), ("d", "இந்தியத் தேர்தல் ஆணையம்")],
        l2_items_en=[("1", "Article 243Y (read with 243-I)"), ("2", "Article 243ZA (read with 243K)"), ("3", "Article 280"), ("4", "Article 324")],
        l2_items_ta=[("1", "உறுப்பு 243Y (உறுப்பு 243-I உடன் இணைத்து)"), ("2", "உறுப்பு 243ZA (உறுப்பு 243K உடன் இணைத்து)"), ("3", "உறுப்பு 280"), ("4", "உறுப்பு 324")],
        opt_tuples=[("A", "a-1, b-2, c-3, d-4"), ("B", "a-2, b-1, c-4, d-3"), ("C", "a-3, b-4, c-1, d-2"), ("D", "a-4, b-3, c-2, d-1")],
        correct_key="A",
        exp_en="Accurate article matching:\nSFC for Municipalities - Article 243Y [1]\nSEC for Municipalities - Article 243ZA [2]\nUnion Finance Commission - Article 280 [3]\nElection Commission of India - Article 324 [4].",
        exp_ta="சரியான உறுப்புகள் பொருத்தம்:\nநகராட்சி மாநில நிதி ஆணையம் - உறுப்பு 243Y [1]\nநகராட்சி மாநில தேர்தல் ஆணையம் - உறுப்பு 243ZA [2]\nமத்திய நிதி ஆணையம் - உறுப்பு 280 [3]\nஇந்திய தேர்தல் ஆணையம் - உறுப்பு 324 [4].",
        tip_en="SFC: 243-I (Panchayat), 243Y (Municipality); SEC: 243K (Panchayat), 243ZA (Municipality).",
        tip_ta="SFC: 243-I, 243Y; SEC: 243K, 243ZA.",
        fact_en="Under Article 280(3)(c), the Union Finance Commission recommends measures to augment state consolidated funds based on SFC inputs.",
        fact_ta="உறுப்பு 280(3)(c)-ன் கீழ் மத்திய நிதி ஆணையம் நகராட்சிகளுக்கான கூடுதல் நிதி நடவடிக்கைகளை பரிந்துரைக்கிறது.",
        tags=["constitutional_commissions", "articles_matching", "match_the_following"]
    ))

    # MF21: Pre-Independence British Acts
    questions.append(make_mf_q(
        qid="MUN_MF_021",
        subtopic="Colonial Urban Acts",
        l1_title="Colonial Enactment",
        l2_title="Key Provision for Local Government",
        l1_items_en=[("a", "Act XXVI of 1850"), ("b", "Towns Improvement Act, 1865"), ("c", "Madras Local Boards Act, 1884"), ("d", "Government of India Act, 1935")],
        l1_items_ta=[("a", "1850-ஆம் ஆண்டின் சட்டம் XXVI"), ("b", "1865-ஆம் ஆண்டின் நகர மேம்பாட்டுச் சட்டம்"), ("c", "1884-ஆம் ஆண்டின் மெட்ராஸ் உள்ளாட்சி வாரியங்கள் சட்டம்"), ("d", "1935-ஆம் ஆண்டின் இந்திய அரசுச் சட்டம்")],
        l2_items_en=[("1", "First permissive all-India act authorizing municipal committees on resident petition"), ("2", "Authorized creation of mofussil municipalities in Madras Presidency including Walajah"), ("3", "Created 2-tier rural boards and formalized Ripon's local self-government principles in Madras"), ("4", "Placed Local Self-Government entirely in Provincial Legislative List (List II)")],
        l2_items_ta=[("1", "பொதுமக்கள் கோரிக்கையின் பேரில் நகராட்சிக் குழுக்களை அமைக்க அனுமதித்த முதல் அகில இந்திய சட்டம்"), ("2", "வாலாஜா உட்பட மெட்ராஸ் மாகாணத்தில் புறநகர் நகராட்சிகளை உருவாக்க வழிவகுத்தது"), ("3", "மெட்ராஸில் 2 அடுக்கு வாரியங்களை உருவாக்கி ரிப்பனின் உள்ளாட்சி கோட்பாடுகளை நடைமுறைப்படுத்தியது"), ("4", "உள்ளாட்சி சுயஅரசாங்கத்தை முழுமையாக மாகாண சட்டமன்றப் பட்டியலில் (பட்டியல் II) வைத்தது")],
        opt_tuples=[("A", "a-1, b-2, c-3, d-4"), ("B", "a-4, b-3, c-2, d-1"), ("C", "a-2, b-1, c-4, d-3"), ("D", "a-3, b-4, c-1, d-2")],
        correct_key="A",
        exp_en="Accurate matching of historical colonial statutes:\nAct XXVI of 1850 - Permissive all-India municipal act [1]\nTowns Improvement Act 1865 - Madras Presidency mofussil municipalities [2]\nMadras Local Boards Act 1884 - Followed Ripon's resolution in Madras [3]\nGoI Act 1935 - Provincial Autonomy and Provincial List for local gov [4].",
        exp_ta="சரியான பொருத்தம்:\n1850 சட்டம் - அனுமதித்த முதல் அகில இந்திய சட்டம் [1]\n1865 நகர மேம்பாட்டுச் சட்டம் - மெட்ராஸ் புறநகர் நகராட்சிகள் [2]\n1884 உள்ளாட்சி வாரியங்கள் சட்டம் - ரிப்பனின் தீர்மானத்தை செயல்படுத்தியது [3]\n1935 இந்திய அரசுச் சட்டம் - உள்ளாட்சி மாகாணப் பட்டியலில் சேர்க்கப்பட்டது [4].",
        tip_en="1919 Act = Transferred subject; 1935 Act = Provincial List subject.",
        tip_ta="1919 சட்டம் = மாற்றப்பட்ட துறை; 1935 சட்டம் = மாகாணப் பட்டியல் துறை.",
        fact_en="List II, Entry 5 of Seventh Schedule in the present Constitution traces directly to GoI Act 1935.",
        fact_ta="தற்போதைய அரசியலமைப்பின் 7-வது அட்டவணை மாநிலப் பட்டியல் பதிவு 5 நேரடியாக 1935 சட்டத்திலிருந்து வந்தது.",
        tags=["colonial_acts", "history", "match_the_following"]
    ))

    # MF22: Municipal Grades in Tamil Nadu
    questions.append(make_mf_q(
        qid="MUN_MF_022",
        subtopic="TN Municipal Classification Criteria",
        l1_title="Municipality Grade in Tamil Nadu",
        l2_title="Annual Income / Revenue Criterion",
        l1_items_en=[("a", "Special Grade Municipality"), ("b", "Selection Grade Municipality"), ("c", "Grade I Municipality"), ("d", "Grade II Municipality")],
        l1_items_ta=[("a", "சிறப்பு நிலை நகராட்சி (Special Grade)"), ("b", "தேர்வு நிலை நகராட்சி (Selection Grade)"), ("c", "முதல் நிலை நகராட்சி (Grade I)"), ("d", "இரண்டாம் நிலை நகராட்சி (Grade II)")],
        l2_items_en=[("1", "Annual income exceeding Rs 10 Crores"), ("2", "Annual income between Rs 6 Crores and Rs 10 Crores"), ("3", "Annual income between Rs 4 Crores and Rs 6 Crores"), ("4", "Annual income below Rs 4 Crores")],
        l2_items_ta=[("1", "ஆண்டு வருமானம் ரூ 10 கோடிக்கு மேல்"), ("2", "ஆண்டு வருமானம் ரூ 6 கோடி முதல் ரூ 10 கோடி வரை"), ("3", "ஆண்டு வருமானம் ரூ 4 கோடி முதல் ரூ 6 கோடி வரை"), ("4", "ஆண்டு வருமானம் ரூ 4 கோடிக்கு கீழ்")],
        opt_tuples=[("A", "a-1, b-2, c-3, d-4"), ("B", "a-2, b-1, c-4, d-3"), ("C", "a-4, b-3, c-2, d-1"), ("D", "a-3, b-4, c-1, d-2")],
        correct_key="A",
        exp_en="Classification of Municipalities in Tamil Nadu based on annual income:\nSpecial Grade: Income > Rs 10 Crores [1]\nSelection Grade: Income Rs 6 to 10 Crores [2]\nGrade I: Income Rs 4 to 6 Crores [3]\nGrade II: Income below Rs 4 Crores [4].",
        exp_ta="தமிழ்நாட்டில் ஆண்டு வருவாய் அடிப்படையில் நகராட்சிகளின் வகைப்பாடு:\nசிறப்பு நிலை: ஆண்டு வருமானம் ரூ 10 கோடிக்கு மேல் [1]\nதேர்வு நிலை: ரூ 6 முதல் 10 கோடி வரை [2]\nமுதல் நிலை: ரூ 4 முதல் 6 கோடி வரை [3]\nஇரண்டாம் நிலை: ரூ 4 கோடிக்கு கீழ் [4].",
        tip_en="Grades in descending order: Special (>10 Cr) -> Selection (6-10 Cr) -> Grade I (4-6 Cr) -> Grade II (<4 Cr).",
        tip_ta="படிநிலைகள்: சிறப்பு நிலை (>10 கோடி) -> தேர்வு நிலை (6-10 கோடி) -> முதல் நிலை (4-6 கோடி) -> இரண்டாம் நிலை (<4 கோடி).",
        fact_en="Upgradation allows municipalities to employ higher-ranking municipal commissioners and engineers.",
        fact_ta="தரம் உயர்த்துதல் உயர்நிலை நகராட்சி ஆணையர்கள் மற்றும் பொறியாளர்களை நியமிக்க உதவுகிறது.",
        tags=["tn_municipal_grades", "revenue_criteria", "match_the_following"]
    ))

    # MF23: Cantonment Board Classes
    questions.append(make_mf_q(
        qid="MUN_MF_023",
        subtopic="Cantonment Boards Classification",
        l1_title="Cantonment Category (2006 Act)",
        l2_title="Civilian Population Criterion",
        l1_items_en=[("a", "Category I"), ("b", "Category II"), ("c", "Category III"), ("d", "Category IV")],
        l1_items_ta=[("a", "வகை I பாசறை"), ("b", "வகை II பாசறை"), ("c", "வகை III பாசறை"), ("d", "வகை IV பாசறை")],
        l2_items_en=[("1", "Civilian population exceeding 50,000"), ("2", "Civilian population between 10,000 and 50,000"), ("3", "Civilian population between 2,500 and 10,000"), ("4", "Civilian population below 2,500")],
        l2_items_ta=[("1", "பொதுமக்கள் தொகை 50,000-க்கு மேல்"), ("2", "பொதுமக்கள் தொகை 10,000 முதல் 50,000 வரை"), ("3", "பொதுமக்கள் தொகை 2,500 முதல் 10,000 வரை"), ("4", "பொதுமக்கள் தொகை 2,500-க்கு கீழ்")],
        opt_tuples=[("A", "a-1, b-2, c-3, d-4"), ("B", "a-2, b-1, c-4, d-3"), ("C", "a-3, b-4, c-1, d-2"), ("D", "a-4, b-3, c-2, d-1")],
        correct_key="A",
        exp_en="Classification under the Cantonments Act, 2006:\nCategory I: Civilian population > 50,000\nCategory II: Civilian population 10,000 to 50,000\nCategory III: Civilian population 2,500 to 10,000\nCategory IV: Civilian population < 2,500.",
        exp_ta="2006 பாசறை சட்டத்தின் கீழ் வகைப்பாடு:\nவகை I: மக்கள் தொகை 50,000-க்கு மேல்\nவகை II: 10,000 முதல் 50,000 வரை\nவகை III: 2,500 முதல் 10,000 வரை\nவகை IV: 2,500-க்கு கீழ்.",
        tip_en="Cantonment populations: 50K -> 10K -> 2.5K.",
        tip_ta="பாசறை மக்கள் தொகை: 50,000 -> 10,000 -> 2,500.",
        fact_en="Cantonment Boards have equal numbers of elected civilian members and nominated military officials.",
        fact_ta="பாசறை வாரியங்கள் சம எண்ணிக்கையிலான தேர்ந்தெடுக்கப்பட்ட மக்கள் பிரதிநிதிகள் மற்றும் இராணுவ அதிகாரிகளைக் கொண்டுள்ளன.",
        tags=["cantonment_categories", "cantonments_act_2006", "match_the_following"]
    ))

    # MF24: Planning Agencies in Tamil Nadu
    questions.append(make_mf_q(
        qid="MUN_MF_024",
        subtopic="TN Urban Planning Bodies",
        l1_title="Urban Development Agency",
        l2_title="Functional Jurisdiction",
        l1_items_en=[("a", "CMDA (Chennai Metropolitan Development Authority)"), ("b", "DTCP (Directorate of Town and Country Planning)"), ("c", "TNUHDB (TN Urban Habitat Development Board)"), ("d", "TNSCB (Historical predecessor to TNUHDB)")],
        l1_items_ta=[("a", "CMDA (சென்னை பெருநகர வளர்ச்சிக் குழுமம்)"), ("b", "DTCP (நகர் மற்றும் ஊரமைப்பு இயக்ககம்)"), ("c", "TNUHDB (தமிழ்நாடு நகர்ப்புற வாழ்விட மேம்பாட்டு வாரியம்)"), ("d", "TNSCB (முந்தைய தமிழ்நாடு குடிசை மாற்று வாரியம்)")],
        l2_items_en=[("1", "Master planning and statutory land use regulation for Chennai Metropolitan Area"), ("2", "Town and country planning regulation for areas outside Chennai Metropolitan Area"), ("3", "Affordable housing and slum rehabilitation across all urban areas in TN"), ("4", "First statutory Slum Clearance Board in India established in 1970")],
        l2_items_ta=[("1", "சென்னை பெருநகரப் பகுதிக்கான பெருந்திட்டமிடல் மற்றும் நிலப் பயன்பாட்டு ஒழுங்குமுறை"), ("2", "சென்னை பெருநகர பகுதிக்கு வெளியே உள்ள பகுதிகளுக்கான நகர் மற்றும் ஊரமைப்பு ஒழுங்குமுறை"), ("3", "தமிழ்நாட்டின் அனைத்து நகர்ப்புறங்களிலும் கட்டுப்படியாகக்கூடிய வீட்டுவசதி மற்றும் சேரி மறுவாழ்வு"), ("4", "1970-ல் அமைக்கப்பட்ட இந்தியாவின் முதல் சட்டப்பூர்வ குடிசை மாற்று வாரியம்")],
        opt_tuples=[("A", "a-1, b-2, c-3, d-4"), ("B", "a-2, b-1, c-4, d-3"), ("C", "a-4, b-3, c-2, d-1"), ("D", "a-3, b-4, c-1, d-2")],
        correct_key="A",
        exp_en="Accurate matching of Tamil Nadu planning bodies:\nCMDA - Chennai Metropolitan Area planning [1]\nDTCP - Rest of Tamil Nadu planning [2]\nTNUHDB - Slum housing and rehabilitation [3]\nTNSCB - Historic 1970 body renamed TNUHDB in 2021 [4].",
        exp_ta="சரியான பொருத்தம்:\nCMDA - சென்னை பெருநகர திட்டமிடல் [1]\nDTCP - தமிழகத்தின் பிற பகுதி திட்டமிடல் [2]\nTNUHDB - சேரி மறுவாழ்வு வீட்டுவசதி [3]\nTNSCB - 1970-ல் உருவாக்கப்பட்ட முன்னோடி அமைப்பு [4].",
        tip_en="In September 2021, Tamil Nadu Slum Clearance Board was renamed Tamil Nadu Urban Habitat Development Board.",
        tip_ta="2021 செப்டம்பரில் தமிழ்நாடு குடிசை மாற்று வாரியம் 'தமிழ்நாடு நகர்ப்புற வாழ்விட மேம்பாட்டு வாரியம்' என பெயர் மாற்றப்பட்டது.",
        fact_en="Tamil Nadu was the first state in India to establish a dedicated Slum Clearance Board in 1970.",
        fact_ta="1970-ல் பிரத்யேக குடிசை மாற்று வாரியத்தை அமைத்த இந்தியாவின் முதல் மாநிலம் தமிழ்நாடு ஆகும்.",
        tags=["planning_agencies", "cmda_dtcp_tnuhdb", "match_the_following"]
    ))

    # MF25: Landmark Supreme Court Judgments
    questions.append(make_mf_q(
        qid="MUN_MF_025",
        subtopic="Landmark Judicial Rulings",
        l1_title="Landmark Supreme Court Case",
        l2_title="Constitutional Ruling on Local Government",
        l1_items_en=[("a", "Kishan Singh Tomar v. Municipal Corporation of Ahmedabad (2006)"), ("b", "K. Krishna Murthy v. Union of India (2010)"), ("c", "Vikas Kishanrao Gawali v. State of Maharashtra (2021)"), ("d", "Suresh Mahajan v. State of Madhya Pradesh (2022)")],
        l1_items_ta=[("a", "கிஷன் சிங் தோமர் எதிர் அகமதாபாத் மாநகராட்சி (2006)"), ("b", "கே. கிருஷ்ண மூர்த்தி எதிர் இந்திய யூனியன் (2010)"), ("c", "விகாஸ் கிஷன்ராவ் கவாலி எதிர் மகாராஷ்டிர அரசு (2021)"), ("d", "சுரேஷ் மகாஜன் எதிர் மத்தியப் பிரதேச அரசு (2022)")],
        l2_items_en=[("1", "Held that five-year municipal term is inviolable and SEC must complete elections before expiry"), ("2", "Upheld constitutional validity of women reservation and OBC quota in local bodies"), ("3", "Enforced the 'Triple Test' criteria for OBC reservation in local bodies capped at 50% overall"), ("4", "Ruled that election process cannot be delayed on ground of delimitation or pending OBC surveys")],
        l2_items_ta=[("1", "5 ஆண்டு பதவிக்காலம் மீற முடியாதது; முடிவதற்குள் SEC தேர்தல் நடத்த வேண்டும் என தீர்ப்பளித்தது"), ("2", "உள்ளாட்சி அமைப்புகளில் பெண்களுக்கான இடஒதுக்கீடு மற்றும் OBC ஒதுக்கீட்டின் அரசியலமைப்புச் செல்லுபடியை உறுதி செய்தது"), ("3", "உள்ளாட்சித் தேர்தலில் OBC ஒதுக்கீட்டிற்கு 'மும்மை சோதனை' (Triple Test) கட்டாயம் என தீர்ப்பளித்தது"), ("4", "மறுவரையறை அல்லது OBC கணக்கெடுப்பைக் காரணம் காட்டி உள்ளாட்சித் தேர்தலை தாமதிக்க முடியாது என உத்தரவிட்டது")],
        opt_tuples=[("A", "a-1, b-2, c-3, d-4"), ("B", "a-2, b-1, c-4, d-3"), ("C", "a-4, b-3, c-2, d-1"), ("D", "a-3, b-4, c-1, d-2")],
        correct_key="A",
        exp_en="Accurate matching of landmark local government jurisprudence:\nKishan Singh Tomar (2006) - Mandatory 5-year election completion [1]\nK. Krishna Murthy (2010) - Upheld reservation under Articles 243D & 243T [2]\nVikas Kishanrao Gawali (2021) - Triple test for local body OBC quota [3]\nSuresh Mahajan (2022) - Bar on stalling elections for delimitation/OBC surveys [4].",
        exp_ta="சரியான தீர்ப்புகள் பொருத்தம்:\nகிஷன் சிங் தோமர் (2006) - 5 ஆண்டுக்குள் கட்டாயத் தேர்தல் [1]\nகே. கிருஷ்ண மூர்த்தி (2010) - உள்ளாட்சி இடஒதுக்கீடு செல்லும் [2]\nவிகாஸ் கவாலி (2021) - மும்மை சோதனை வரம்பு [3]\nசுரேஷ் மகாஜன் (2022) - காரணங்களை கூறி தேர்தலை தள்ளிப்போடக் கூடாது [4].",
        tip_en="Kishan Singh Tomar (2006) is the landmark ruling on State Election Commission powers.",
        tip_ta="கிஷன் சிங் தோமர் (2006) தீர்ப்பு மாநில தேர்தல் ஆணையத்தின் அதிகாரத்தை நிலைநாட்டியது.",
        fact_en="The Supreme Court equated the SEC's constitutional powers with those of the Election Commission of India under Article 324.",
        fact_ta="உச்ச நீதிமன்றம் மாநில தேர்தல் ஆணையத்தின் அதிகாரங்களை இந்திய தேர்தல் ஆணையத்திற்கு இணையாக வைத்தது.",
        tags=["supreme_court_judgments", "case_law", "match_the_following"]
    ))

    return questions

def main():
    questions = get_match_25()
    assert len(questions) == 25, f"Expected 25 questions, got {len(questions)}"
    
    # Balance keys across A, B, C, D
    balanced = balance_question_keys(questions)
    
    out_dir = os.path.join("data", "questions", "polity")
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "municipalities_match_the_following.json")
    
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(balanced, f, ensure_ascii=False, indent=2)
        
    print(f"[SUCCESS] Wrote {len(balanced)} Match the Following MCQs to {out_file}")

if __name__ == "__main__":
    main()
