# -*- coding: utf-8 -*-
"""
Builder for Inter-State Relations PYQ Practice Part 1 (ISR_PYQ_001 to ISR_PYQ_025)
"""
import json

def make_pyq(qid, diff, stem_en, stem_ta,
             opt_a_en, opt_a_ta, opt_b_en, opt_b_ta, opt_c_en, opt_c_ta, opt_d_en, opt_d_ta,
             correct_ans, exp_en, exp_ta,
             wno_a_en, wno_a_ta, wno_b_en, wno_b_ta, wno_c_en, wno_c_ta, wno_d_en, wno_d_ta,
             tip_en, tip_ta, rev_en, rev_ta, bloom="Remember", est_time=60, tags=None):
    return {
        "id": qid,
        "subject": "Polity",
        "topic": "Inter-State Relations",
        "difficulty": diff,
        "question_type": "PYQ Practice",
        "question": {"en": stem_en, "ta": stem_ta},
        "question_en": stem_en,
        "question_ta": stem_ta,
        "options": [
            {"id": "A", "en": opt_a_en, "ta": opt_a_ta},
            {"id": "B", "en": opt_b_en, "ta": opt_b_ta},
            {"id": "C", "en": opt_c_en, "ta": opt_c_ta},
            {"id": "D", "en": opt_d_en, "ta": opt_d_ta}
        ],
        "options_en": [opt_a_en, opt_b_en, opt_c_en, opt_d_en],
        "options_ta": [opt_a_ta, opt_b_ta, opt_c_ta, opt_d_ta],
        "correct_answer": correct_ans,
        "answer": correct_ans.lower(),
        "explanation": {"en": exp_en, "ta": exp_ta},
        "explanation_en": exp_en,
        "explanation_ta": exp_ta,
        "why_not_others": {
            "A": {"en": wno_a_en, "ta": wno_a_ta},
            "B": {"en": wno_b_en, "ta": wno_b_ta},
            "C": {"en": wno_c_en, "ta": wno_c_ta},
            "D": {"en": wno_d_en, "ta": wno_d_ta}
        },
        "tnpsc_tip": {"en": tip_en, "ta": tip_ta},
        "revision_fact": {"en": rev_en, "ta": rev_ta},
        "source_reference": ["TNPSC Group 1 Prelims (2017, 2019, 2022)", "UPSC CSE Prelims", "M. Laxmikanth - Indian Polity"],
        "bloom_level": bloom,
        "estimated_time_sec": est_time,
        "pyq_similarity": "High",
        "tags": tags or ["Inter-State Relations", "PYQ Practice", "TNPSC Standard"]
    }

def get_pyq_part1():
    q = []

    # 001 - Ans A (TNPSC Group 1 2019 adapted)
    q.append(make_pyq(
        "ISR_PYQ_001", "Easy",
        "[TNPSC Group 1 Prelims] Under which Article of the Constitution of India is the Inter-State Council established by the President?",
        "[TNPSC குரூப் 1 முதல்நிலை] இந்திய அரசியலமைப்பின் எந்த உறுப்பின் கீழ் குடியரசுத் தலைவரால் மாநிலங்களுக்கு இடையிலான மன்றம் அமைக்கப்படுகிறது?",
        "Article 263", "உறுப்பு 263",
        "Article 262", "உறுப்பு 262",
        "Article 261", "உறுப்பு 261",
        "Article 280", "உறுப்பு 280",
        "A",
        "Article 263 provides for the establishment of an Inter-State Council by the President to investigate and discuss subjects in which States have a common interest.",
        "மாநிலங்களுக்கு இடையே பொதுவான நலன் சார்ந்த விஷயங்களை ஆராய்ந்து விவாதிக்க குடியரசுத் தலைவரால் மாநிலங்களுக்கு இடையிலான மன்றம் அமைக்கப்பட உறுப்பு 263 வகை செய்கிறது.",
        "Option A is correct because Article 263 explicitly governs the Inter-State Council.", "உறுப்பு 263 மாநிலங்களுக்கு இடையிலான மன்றத்தைக் குறிப்பிடுவதால் விருப்பம் A சரி.",
        "Option B is incorrect because Article 262 deals with inter-State river water disputes.", "உறுப்பு 262 நதிநீர் தகராறுகளுக்குரியது என்பதால் விருப்பம் B தவறு.",
        "Option C is incorrect because Article 261 relates to Full Faith and Credit.", "உறுப்பு 261 முழு நம்பிக்கையும் சான்றும் விதிக்குரியது என்பதால் விருப்பம் C தவறு.",
        "Option D is incorrect because Article 280 governs the Finance Commission.", "உறுப்பு 280 நிதி ஆணையத்திற்குரியது என்பதால் விருப்பம் D தவறு.",
        "Frequently repeated in TNPSC: Art 261 = Full Faith & Credit; Art 262 = River Water Disputes; Art 263 = Inter-State Council.",
        "TNPSC-ல் அடிக்கடி கேட்கப்படும் வினா: உறுப்பு 261 = முழு நம்பிக்கை; உறுப்பு 262 = நதிநீர் தகராறுகள்; உறுப்பு 263 = மாநிலங்களுக்கு இடையிலான மன்றம்.",
        "Article 263 empowers the President to establish an Inter-State Council for cooperative federalism.",
        "கூட்டுறவு கூட்டாட்சியை மேம்படுத்த உறுப்பு 263-ன் கீழ் குடியரசுத் தலைவர் மாநிலங்களுக்கு இடையிலான மன்றத்தை அமைக்கிறார்.",
        tags=["TNPSC PYQ", "Article 263", "Inter-State Council"]
    ))

    # 002 - Ans B (UPSC CSE 2013 / TNPSC 2017)
    q.append(make_pyq(
        "ISR_PYQ_002", "Medium",
        "[UPSC CSE / TNPSC Group 1] Who among the following is the Chairman of the Inter-State Council?",
        "[UPSC CSE / TNPSC குரூப் 1] பின்வருபவர்களில் மாநிலங்களுக்கு இடையிலான மன்றத்தின் தலைவர் யார்?",
        "The President of India", "இந்தியக் குடியரசுத் தலைவர்",
        "The Prime Minister of India", "இந்தியப் பிரதமர்",
        "The Union Home Minister", "மத்திய உள்துறை அமைச்சர்",
        "The Chief Justice of India", "இந்தியத் தலைமை நீதிபதி",
        "B",
        "The Prime Minister of India is the ex-officio Chairman of the Inter-State Council established under Article 263.",
        "உறுப்பு 263-ன் கீழ் நிறுவப்பட்ட மாநிலங்களுக்கு இடையிலான மன்றத்தின் அலுவல்சார் தலைவராக இந்தியப் பிரதமர் செயல்படுகிறார்.",
        "Option A is incorrect because the President establishes the Council, but does not chair it.", "குடியரசுத் தலைவர் மன்றத்தை நிறுவுகிறாரே தவிர, தலைமை தாங்குவதில்லை என்பதால் விருப்பம் A தவறு.",
        "Option B is correct because the Prime Minister chairs the Inter-State Council.", "பிரதமரே மாநிலங்களுக்கு இடையிலான மன்றத்தின் தலைவர் என்பதால் விருப்பம் B சரி.",
        "Option C is incorrect because the Union Home Minister chairs the Standing Committee and Zonal Councils.", "உள்துறை அமைச்சர் நிலைக்குழு மற்றும் மண்டலக் குழுக்களுக்குத் தலைமை தாங்குவதால் விருப்பம் C தவறு.",
        "Option D is incorrect because the Chief Justice of India has no role in the Inter-State Council.", "தலைமை நீதிபதிக்கு இதில் பங்கு இல்லை என்பதால் விருப்பம் D தவறு.",
        "Classic trap: The President establishes the Inter-State Council by order, but the PRIME MINISTER chairs it.",
        "பொறி: குடியரசுத் தலைவர் மன்றத்தை ஆணை மூலம் நிறுவுகிறார், ஆனால் பிரதமர் அதற்குத் தலைமை தாங்குகிறார்.",
        "The Prime Minister of India serves as the Chairman of the Inter-State Council.",
        "இந்தியப் பிரதமர் மாநிலங்களுக்கு இடையிலான மன்றத்தின் தலைவராகச் செயல்படுகிறார்.",
        tags=["ISC Chairman", "Prime Minister", "TNPSC PYQ"]
    ))

    # 003 - Ans C (TNPSC Group 2 2018)
    q.append(make_pyq(
        "ISR_PYQ_003", "Easy",
        "[TNPSC Group 2] In which year was the Inter-State Council formally established by a Presidential Order on the recommendation of the Sarkaria Commission?",
        "[TNPSC குரூப் 2] சர்க்காரியா ஆணையத்தின் பரிந்துரையின் பேரில் குடியரசுத் தலைவரின் ஆணை மூலம் மாநிலங்களுக்கு இடையிலான மன்றம் எந்த ஆண்டு முறைப்படி நிறுவப்பட்டது?",
        "1988", "1988",
        "1989", "1989",
        "1990", "1990",
        "1992", "1992",
        "C",
        "The Inter-State Council was set up on 28th May 1990 by a Presidential Order issued by the V.P. Singh National Front Government, implementing the recommendation of the Sarkaria Commission (1988).",
        "சர்க்காரியா ஆணையத்தின் (1988) பரிந்துரையை ஏற்று, வி.பி. சிங் தலைமையிலான தேசிய முன்னணி அரசாங்கத்தால் 1990 மே 28 அன்று குடியரசுத் தலைவர் ஆணை மூலம் மாநிலங்களுக்கு இடையிலான மன்றம் நிறுவப்பட்டது.",
        "Option A is incorrect because 1988 was the year the Sarkaria Commission submitted its final report.", "1988 சர்க்காரியா ஆணையம் அறிக்கை அளித்த ஆண்டு என்பதால் விருப்பம் A தவறு.",
        "Option B is incorrect because 1989 did not see the notification.", "1989-ல் மன்றம் அறிவிக்கப்படவில்லை என்பதால் விருப்பம் B தவறு.",
        "Option C is correct because the historic Presidential notification was issued on May 28, 1990.", "1990 மே 28 அன்று குடியரசுத் தலைவர் ஆணை வெளியிடப்பட்டதால் விருப்பம் C சரி.",
        "Option D is incorrect because 1992 was later than the establishment date.", "1992 நிறுவப்பட்ட ஆண்டை விடப் பிந்தையது என்பதால் விருப்பம் D தவறு.",
        "Remember the landmark date: May 28, 1990 (V.P. Singh Government created the Inter-State Council).",
        "முக்கிய தேதியை நினைவில் கொள்க: மே 28, 1990 (வி.பி. சிங் அரசு மன்றத்தை அமைத்தது).",
        "Inter-State Council was formally constituted on 28 May 1990 based on the Sarkaria Commission report.",
        "சர்க்காரியா ஆணைய அறிக்கையின்படி 1990 மே 28 அன்று மாநிலங்களுக்கு இடையிலான மன்றம் முறைப்படி அமைக்கப்பட்டது.",
        tags=["1990 Presidential Order", "Sarkaria Commission", "TNPSC PYQ"]
    ))

    # 004 - Ans D (TNPSC Combined Civil Services 2021)
    q.append(make_pyq(
        "ISR_PYQ_004", "Medium",
        "[TNPSC Group 1] Which of the following bodies in India are statutory bodies and NOT constitutional bodies?",
        "[TNPSC குரூப் 1] இந்தியாவில் உள்ள பின்வரும் அமைப்புகளில் எவை சட்டப்பூர்வ அமைப்புகளே தவிர அரசியலமைப்பு அமைப்புகள் அல்ல?",
        "Finance Commission", "நிதி ஆணையம்",
        "Inter-State Council", "மாநிலங்களுக்கு இடையிலான மன்றம்",
        "Goods and Services Tax Council", "சரக்கு மற்றும் சேவை வரி மன்றம்",
        "Zonal Councils", "மண்டலக் குழுக்கள்",
        "D",
        "Zonal Councils are statutory bodies established under Part III of the States Reorganisation Act, 1956. By contrast, the Finance Commission (Art 280), Inter-State Council (Art 263), and GST Council (Art 279A) are all constitutional bodies.",
        "மண்டலக் குழுக்கள் 1956 மாநில மறுசீரமைப்புச் சட்டத்தின் கீழ் அமைக்கப்பட்ட சட்டப்பூர்வ அமைப்புகள் ஆகும். நிதி ஆணையம் (உறுப்பு 280), மாநிலங்களுக்கு இடையிலான மன்றம் (உறுப்பு 263) மற்றும் ஜிஎஸ்டி மன்றம் (உறுப்பு 279A) ஆகியவை அரசியலமைப்பு அமைப்புகளாகும்.",
        "Option A is incorrect because the Finance Commission is constitutional under Article 280.", "நிதி ஆணையம் உறுப்பு 280-ன் கீழ் அரசியலமைப்பு அமைப்பு என்பதால் விருப்பம் A தவறு.",
        "Option B is incorrect because the Inter-State Council is constitutional under Article 263.", "மாநிலங்களுக்கு இடையிலான மன்றம் உறுப்பு 263-ன் கீழ் அரசியலமைப்பு அமைப்பு என்பதால் விருப்பம் B தவறு.",
        "Option C is incorrect because the GST Council is constitutional under Article 279A.", "ஜிஎஸ்டி மன்றம் உறுப்பு 279A-ன் கீழ் அரசியலமைப்பு அமைப்பு என்பதால் விருப்பம் C தவறு.",
        "Option D is correct because Zonal Councils are statutory creations of the 1956 Act.", "மண்டலக் குழுக்கள் 1956 சட்டத்தால் உருவாக்கப்பட்ட சட்டப்பூர்வ அமைப்புகள் என்பதால் விருப்பம் D சரி.",
        "High-yield distinction: Zonal Councils = Statutory (1956 Act); Inter-State Council = Constitutional (Art 263).",
        "முக்கிய வேறுபாடு: மண்டலக் குழுக்கள் = சட்டப்பூர்வமானது (1956 சட்டம்); மாநிலங்களுக்கு இடையிலான மன்றம் = அரசியலமைப்பு சார்ந்தது (உறுப்பு 263).",
        "Zonal Councils are statutory bodies established under the States Reorganisation Act of 1956.",
        "மண்டலக் குழுக்கள் 1956-ஆம் ஆண்டின் மாநில மறுசீரமைப்புச் சட்டத்தின் கீழ் உருவாக்கப்பட்ட சட்டப்பூர்வ அமைப்புகளாகும்.",
        tags=["Zonal Councils", "Statutory vs Constitutional", "TNPSC PYQ"]
    ))

    # 005 - Ans A (UPSC CSE 2013 / TNPSC 2015)
    q.append(make_pyq(
        "ISR_PYQ_005", "Easy",
        "[UPSC CSE / TNPSC Group 1] Who serves as the common Chairman of all the five Zonal Councils in India?",
        "[UPSC CSE / TNPSC குரூப் 1] இந்தியாவில் உள்ள ஐந்து மண்டலக் குழுக்களுக்கும் பொதுவான தலைவராகச் செயல்படுபவர் யார்?",
        "Union Home Minister", "மத்திய உள்துறை அமைச்சர்",
        "Prime Minister", "பிரதமர்",
        "President of India", "இந்தியக் குடியரசுத் தலைவர்",
        "Union Minister of Law and Justice", "மத்திய சட்டம் மற்றும் நீதித்துறை அமைச்சர்",
        "A",
        "Under Section 16 of the States Reorganisation Act, 1956, the Union Home Minister is designated as the common Chairman of all five Zonal Councils.",
        "1956 மாநில மறுசீரமைப்புச் சட்டம் பிரிவு 16-ன் படி, மத்திய உள்துறை அமைச்சர் ஐந்து மண்டலக் குழுக்களுக்கும் பொதுவான தலைவராகச் செயல்படுகிறார்.",
        "Option A is correct because the Union Home Minister chairs all Zonal Councils.", "மத்திய உள்துறை அமைச்சரே அனைத்து மண்டலக் குழுக்களுக்கும் தலைவர் என்பதால் விருப்பம் A சரி.",
        "Option B is incorrect because the Prime Minister chairs the Inter-State Council, not Zonal Councils.", "பிரதமர் மாநிலங்களுக்கு இடையிலான மன்றத்திற்குத் தலைமை தாங்குகிறார் என்பதால் விருப்பம் B தவறு.",
        "Option C is incorrect because the President does not chair Zonal Councils.", "குடியரசுத் தலைவர் தலைமை தாங்குவதில்லை என்பதால் விருப்பம் C தவறு.",
        "Option D is incorrect because the Law Minister has no ex-officio role in Zonal Councils.", "சட்ட அமைச்சருக்கு இதில் பதவிவழிப் பொறுப்பு இல்லை என்பதால் விருப்பம் D தவறு.",
        "Memorize: PM = Inter-State Council Chairman; Home Minister = Zonal Councils Chairman.",
        "நினைவில் கொள்க: பிரதமர் = மாநிலங்களுக்கு இடையிலான மன்றத் தலைவர்; உள்துறை அமைச்சர் = மண்டலக் குழுக்களின் தலைவர்.",
        "The Union Home Minister serves as the common Chairman of all five Zonal Councils.",
        "மத்திய உள்துறை அமைச்சர் ஐந்து மண்டலக் குழுக்களுக்கும் பொதுத் தலைவராகச் செயல்படுகிறார்.",
        tags=["Zonal Council Chairman", "Union Home Minister", "States Reorganisation Act"]
    ))

    # 006 - Ans B (TNPSC Group 1 2022)
    q.append(make_pyq(
        "ISR_PYQ_006", "Medium",
        "[TNPSC Group 1 Prelims 2022] The headquarters of the Southern Zonal Council is located at which of the following cities?",
        "[TNPSC குரூப் 1 முதல்நிலை 2022] தெற்கு மண்டலக் குழுவின் தலைமையகம் பின்வரும் எந்த நகரத்தில் அமைந்துள்ளது?",
        "Bengaluru", "பெங்களூரு",
        "Chennai", "சென்னை",
        "Hyderabad", "ஹைதராபாத்",
        "Thiruvananthapuram", "திருவனந்தபுரம்",
        "B",
        "The headquarters of the Southern Zonal Council (comprising Tamil Nadu, Andhra Pradesh, Karnataka, Kerala, Telangana, and Puducherry) is situated at Chennai.",
        "தமிழ்நாடு, ஆந்திரா, கர்நாடகா, கேரளா, தெலுங்கானா மற்றும் புதுச்சேரியை உள்ளடக்கிய தெற்கு மண்டலக் குழுவின் தலைமையகம் சென்னையில் அமைந்துள்ளது.",
        "Option A is incorrect because Bengaluru is not the zonal headquarters.", "பெங்களூரு தலைமையகம் அல்ல என்பதால் விருப்பம் A தவறு.",
        "Option B is correct because Chennai is the statutory headquarters of the Southern Zonal Council.", "சென்னை தெற்கு மண்டலக் குழுவின் தலைமையகம் என்பதால் விருப்பம் B சரி.",
        "Option C is incorrect because Hyderabad is not the headquarters.", "ஹைதராபாத் தலைமையகம் அல்ல என்பதால் விருப்பம் C தவறு.",
        "Option D is incorrect because Thiruvananthapuram is not the headquarters.", "திருவனந்தபுரம் தலைமையகம் அல்ல என்பதால் விருப்பம் D தவறு.",
        "TNPSC favorite: Southern Zonal Council HQ = Chennai.",
        "TNPSC-ன் முக்கிய வினா: தெற்கு மண்டலக் குழுவின் தலைமையகம் = சென்னை.",
        "Southern Zonal Council is headquartered in Chennai.",
        "தெற்கு மண்டலக் குழு சென்னையில் தலைமையகத்தைக் கொண்டுள்ளது.",
        tags=["Southern Zonal Council", "Chennai", "TNPSC 2022"]
    ))

    # 007 - Ans C (TNPSC Group 1 2017)
    q.append(make_pyq(
        "ISR_PYQ_007", "Medium",
        "[TNPSC Group 1] In which year was Sikkim included as the eighth member state of the North-Eastern Council (NEC)?",
        "[TNPSC குரூப் 1] வடகிழக்குக் குழுவின் (NEC) எட்டாவது உறுப்பு மாநிலமாக சிக்கிம் எந்த ஆண்டு சேர்க்கப்பட்டது?",
        "1971", "1971",
        "1975", "1975",
        "2002", "2002",
        "2014", "2014",
        "C",
        "The North-Eastern Council was originally established in 1971 with seven member states ('Seven Sisters'). In December 2002, the North-Eastern Council (Amendment) Act, 2002 formally incorporated Sikkim as the eighth member State.",
        "வடகிழக்குக் குழு 1971-ல் ஏழு வடகிழக்கு மாநிலங்களுடன் உருவாக்கப்பட்டது. 2002 டிசம்பரில் வடகிழக்குக் குழு (திருத்தச்) சட்டம் 2002 மூலம் சிக்கிம் எட்டாவது உறுப்பினராக முறைப்படி சேர்க்கப்பட்டது.",
        "Option A is incorrect because 1971 was the year of the parent NEC Act when Sikkim was not a member.", "1971 சட்டம் இயற்றப்பட்ட போது சிக்கிம் உறுப்பினராக இல்லை என்பதால் விருப்பம் A தவறு.",
        "Option B is incorrect because 1975 was the year Sikkim became a full state of the Indian Union (36th Amendment).", "1975-ல் சிக்கிம் முழு மாநிலமானது, ஆனால் NEC-ல் அப்போது சேர்க்கப்படவில்லை என்பதால் விருப்பம் B தவறு.",
        "Option C is correct because Sikkim was inducted into the NEC through the 2002 amendment.", "2002 சட்டத் திருத்தத்தின் மூலம் சிக்கிம் சேர்க்கப்பட்டதால் விருப்பம் C சரி.",
        "Option D is incorrect because 2002 is the definitive year.", "2002-ல் சேர்க்கப்பட்டதால் விருப்பம் D தவறு.",
        "Trap: Sikkim became an Indian State in 1975 (36th Amendment), but joined the North-Eastern Council in 2002!",
        "பொறி: சிக்கிம் 1975-ல் இந்திய மாநிலமானது (36-வது திருத்தம்), ஆனால் வடகிழக்குக் குழுவில் 2002-ல் இணைந்தது!",
        "Sikkim became the 8th member of the North-Eastern Council in 2002 via statutory amendment.",
        "சட்டத் திருத்தத்தின் மூலம் 2002-ல் வடகிழக்குக் குழுவின் 8-வது மாநிலமாக சிக்கிம் இணைந்தது.",
        tags=["Sikkim", "North-Eastern Council", "TNPSC PYQ"]
    ))

    # 008 - Ans D (UPSC CSE / TNPSC 2019)
    q.append(make_pyq(
        "ISR_PYQ_008", "Hard",
        "[UPSC CSE / TNPSC Group 1] Which of the following Articles of the Constitution provides for 'Full Faith and Credit' to public acts, records, and judicial proceedings throughout India?",
        "[UPSC CSE / TNPSC குரூப் 1] இந்தியா முழுவதும் பொதுச் சட்டங்கள், பதிவேடுகள் மற்றும் நீதித்துறை நடவடிக்கைகளுக்கு 'முழு நம்பிக்கையும் சான்றும்' வழங்க அரசியலமைப்பின் எந்த உறுப்பு வகை செய்கிறது?",
        "Article 263", "உறுப்பு 263",
        "Article 262", "உறுப்பு 262",
        "Article 260", "உறுப்பு 260",
        "Article 261", "உறுப்பு 261",
        "D",
        "Article 261 of the Indian Constitution contains the 'Full Faith and Credit' clause, mandating that full faith and credit shall be given throughout the territory of India to public acts, records, and judicial proceedings of the Union and of every State.",
        "இந்திய அரசியலமைப்பின் 261-வது உறுப்பு 'முழு நம்பிக்கையும் சான்றும்' விதியைக் கொண்டுள்ளது; இது ஒன்றியம் மற்றும் மாநிலங்களின் பொது நடவடிக்கைகள், பதிவேடுகள் மற்றும் தீர்ப்புகளுக்கு நாடு முழுவதும் அங்கீகாரம் அளிக்கிறது.",
        "Option A is incorrect because Article 263 relates to the Inter-State Council.", "உறுப்பு 263 மாநிலங்களுக்கு இடையிலான மன்றத்திற்குரியது என்பதால் விருப்பம் A தவறு.",
        "Option B is incorrect because Article 262 deals with river water disputes.", "உறுப்பு 262 நதிநீர் தகராறுகளுக்குரியது என்பதால் விருப்பம் B தவறு.",
        "Option C is incorrect because Article 260 deals with jurisdiction over foreign territories.", "உறுப்பு 260 வெளிநாட்டுப் பகுதிகளின் அதிகார வரம்பிற்குரியது என்பதால் விருப்பம் C தவறு.",
        "Option D is correct because Article 261 embodies the Full Faith and Credit provision.", "உறுப்பு 261 முழு நம்பிக்கையும் சான்றும் விதியை உள்ளடக்கியுள்ளதால் விருப்பம் D சரி.",
        "Constitutional trinity: Article 261 (Full Faith & Credit), Article 262 (Water Disputes), Article 263 (Inter-State Council).",
        "அரசியலமைப்பு மும்மை: உறுப்பு 261 (முழு நம்பிக்கை), உறுப்பு 262 (நதிநீர் தகராறு), உறுப்பு 263 (மாநிலங்களுக்கு இடையிலான மன்றம்).",
        "Article 261 provides for Full Faith and Credit to public acts, records, and judicial proceedings.",
        "உறுப்பு 261 பொதுச் சட்டங்கள், பதிவேடுகள் மற்றும் நீதித்துறை நடவடிக்கைகளுக்கு முழு நம்பிக்கையும் சான்றும் வழங்குகிறது.",
        tags=["Article 261", "Full Faith and Credit", "TNPSC PYQ"]
    ))

    # 009 - Ans A (TNPSC Group 1 2015)
    q.append(make_pyq(
        "ISR_PYQ_009", "Medium",
        "[TNPSC Group 1] Under Article 262 of the Constitution, which institution is empowered to adjudicate disputes relating to the waters of inter-State rivers or river valleys?",
        "[TNPSC குரூப் 1] அரசியலமைப்பின் 262-வது உறுப்பின் கீழ், மாநிலங்களுக்கு இடையேயான நதிகள் அல்லது நதிப் பள்ளத்தாக்குகளின் நீர் தொடர்பான தகராறுகளைத் தீர்க்கும் அதிகார அமைப்பை உருவாக்க யாருக்கு அதிகாரம் உண்டு?",
        "Parliament by law", "சட்டத்தின் மூலம் நாடாளுமன்றத்திற்கு",
        "The President by Ordinance", "அவசரச் சட்டத்தின் மூலம் குடியரசுத் தலைவருக்கு",
        "The Supreme Court under Original Jurisdiction", "மூல அதிகார வரம்பின் கீழ் உச்ச நீதிமன்றத்திற்கு",
        "The Inter-State Council", "மாநிலங்களுக்கு இடையிலான மன்றத்திற்கு",
        "A",
        "Article 262(1) explicitly provides that 'Parliament may by law provide for the adjudication of any dispute or complaint with respect to the use, distribution or control of the waters of, or in, any inter-State river or river valley'.",
        "உறுப்பு 262(1) மாநிலங்களுக்கு இடையேயான நதி அல்லது நதிப் பள்ளத்தாக்கின் நீர்ப் பகிர்வு மற்றும் கட்டுப்பாடு குறித்த தகராறுகளைத் தீர்க்க நாடாளுமன்றம் சட்டத்தின் மூலம் வகை செய்யலாம் என்று தெளிவாகக் கூறுகிறது.",
        "Option A is correct because Parliament has the sole authority to legislate adjudication mechanisms under Article 262.", "நாடாளுமன்றத்திற்கே சட்டத்தின் மூலம் இத்தகைய அமைப்பை ஏற்படுத்த அதிகாரம் உள்ளதால் விருப்பம் A சரி.",
        "Option B is incorrect because Article 262 requires parliamentary statute.", "நாடாளுமன்றச் சட்டம் தேவைப்படுவதால் விருப்பம் B தவறு.",
        "Option C is incorrect because Parliament can actually exclude the Supreme Court's jurisdiction under Article 262(2).", "உச்ச நீதிமன்றத்தின் அதிகார வரம்பையே நாடாளுமன்றம் விலக்க முடியும் என்பதால் விருப்பம் C தவறு.",
        "Option D is incorrect because the Inter-State Council is purely advisory.", "மாநிலங்களுக்கு இடையிலான மன்றம் ஆலோசனைக் குழு மட்டுமே என்பதால் விருப்பம் D தவறு.",
        "Article 262 empowers PARLIAMENT BY LAW to create water dispute tribunals and bar court jurisdiction.",
        "நதிநீர் தீர்ப்பாயங்களை அமைக்கவும் நீதிமன்ற வரம்பைத் தடுக்கவும் உறுப்பு 262 நாடாளுமன்றத்திற்குச் சட்ட அதிகாரம் அளிக்கிறது.",
        "Parliament by law provides for adjudication of inter-state water disputes under Article 262.",
        "உறுப்பு 262-ன் கீழ் நதிநீர் தகராறுகளைத் தீர்க்கும் முறையை நாடாளுமன்றம் சட்டத்தின் மூலம் உருவாக்குகிறது.",
        tags=["Article 262", "Parliamentary Authority", "Water Disputes"]
    ))

    # 010 - Ans B (TNPSC Group 2 2015)
    q.append(make_pyq(
        "ISR_PYQ_010", "Easy",
        "[TNPSC Group 2] In which year was the Inter-State River Water Disputes (IRWD) Act enacted by the Indian Parliament?",
        "[TNPSC குரூப் 2] இந்திய நாடாளுமன்றத்தால் மாநிலங்களுக்கு இடையேயான நதிநீர் தகராறுகள் சட்டம் (IRWD Act) எந்த ஆண்டு இயற்றப்பட்டது?",
        "1950", "1950",
        "1956", "1956",
        "1969", "1969",
        "1976", "1976",
        "B",
        "The Inter-State River Water Disputes Act was enacted by Parliament in 1956 under the powers conferred by Article 262 of the Constitution.",
        "அரசியலமைப்பின் உறுப்பு 262 வழங்கிய அதிகாரங்களின் கீழ் 1956-ஆம் ஆண்டில் நாடாளுமன்றத்தால் மாநிலங்களுக்கு இடையேயான நதிநீர் தகராறுகள் சட்டம் இயற்றப்பட்டது.",
        "Option A is incorrect because 1950 was the commencement of the Constitution.", "1950 அரசியலமைப்பு நடைமுறைக்கு வந்த ஆண்டு என்பதால் விருப்பம் A தவறு.",
        "Option B is correct because the IRWD Act was passed in 1956.", "IRWD சட்டம் 1956-ல் இயற்றப்பட்டதால் விருப்பம் B சரி.",
        "Option C is incorrect because 1969 was when the first tribunals (Krishna, Godavari, Narmada) were constituted.", "1969 முதல் தீர்ப்பாயங்கள் அமைக்கப்பட்ட ஆண்டு என்பதால் விருப்பம் C தவறு.",
        "Option D is incorrect because 1976 was later.", "1976 பிந்தைய ஆண்டு என்பதால் விருப்பம் D தவறு.",
        "Twin 1956 Water Acts: Inter-State River Water Disputes Act, 1956 and River Boards Act, 1956.",
        "1956-ன் இரட்டை நீர்ச் சட்டங்கள்: நதிநீர் தகராறுகள் சட்டம் (1956) மற்றும் நதி வாரியங்கள் சட்டம் (1956).",
        "Inter-State River Water Disputes Act was enacted in 1956 under Article 262.",
        "உறுப்பு 262-ன் கீழ் மாநிலங்களுக்கு இடையேயான நதிநீர் தகராறுகள் சட்டம் 1956-ல் இயற்றப்பட்டது.",
        tags=["IRWD Act 1956", "Article 262", "TNPSC PYQ"]
    ))

    # 011 - Ans C (TNPSC Group 1 2019)
    q.append(make_pyq(
        "ISR_PYQ_011", "Medium",
        "[TNPSC Group 1] In which year was the Cauvery Water Disputes Tribunal (CWDT) constituted by the Government of India?",
        "[TNPSC குரூப் 1] இந்திய அரசால் காவிரி நதிநீர் தகராறுகள் தீர்ப்பாயம் (CWDT) எந்த ஆண்டு அமைக்கப்பட்டது?",
        "1986", "1986",
        "1988", "1988",
        "1990", "1990",
        "1998", "1998",
        "C",
        "The Cauvery Water Disputes Tribunal was constituted by the Central Government on 2nd June 1990 under the chairmanship of Justice Chittatosh Mookerjee, pursuant to Supreme Court directions.",
        "உச்ச நீதிமன்ற உத்தரவைத் தொடர்ந்து, நீதிபதி சிட்டதோஷ் முகர்ஜி தலைமையில் 1990 ஜூன் 2 அன்று மத்திய அரசால் காவிரி நதிநீர் தீர்ப்பாயம் அமைக்கப்பட்டது.",
        "Option A is incorrect because 1986 was the constitution of the Ravi & Beas Tribunal.", "1986 ராவி-பியாஸ் தீர்ப்பாயம் அமைக்கப்பட்ட ஆண்டு என்பதால் விருப்பம் A தவறு.",
        "Option B is incorrect because 1988 was the Sarkaria Commission submission year.", "1988 சர்க்காரியா அறிக்கை ஆண்டு என்பதால் விருப்பம் B தவறு.",
        "Option C is correct because the Cauvery Tribunal was constituted in June 1990.", "காவிரி தீர்ப்பாயம் 1990 ஜூன் மாதத்தில் அமைக்கப்பட்டதால் விருப்பம் C சரி.",
        "Option D is incorrect because 1998 was when the Cauvery River Authority was constituted.", "1998 காவிரி நதி ஆணையம் அமைக்கப்பட்ட ஆண்டு என்பதால் விருப்பம் D தவறு.",
        "Historical Cauvery dates: Tribunal constituted in 1990; Final Award in 2007; Award Gazetted in 2013; CWMA constituted in 2018.",
        "காவிரி முக்கிய ஆண்டுகள்: தீர்ப்பாயம் அமைப்பு = 1990; இறுதித் தீர்ப்பு = 2007; அரசிதழ் வெளியீடு = 2013; CWMA அமைப்பு = 2018.",
        "Cauvery Water Disputes Tribunal was constituted in 1990 under Justice Chittatosh Mookerjee.",
        "காவிரி நதிநீர் தீர்ப்பாயம் 1990-ல் நீதிபதி சிட்டதோஷ் முகர்ஜி தலைமையில் அமைக்கப்பட்டது.",
        tags=["Cauvery Tribunal 1990", "Justice Chittatosh Mookerjee", "TNPSC PYQ"]
    ))

    # 012 - Ans D (TNPSC Group 1 2021)
    q.append(make_pyq(
        "ISR_PYQ_012", "Medium",
        "[TNPSC Group 1] In which year did the Union Government notify the Cauvery Water Management Scheme, establishing the Cauvery Water Management Authority (CWMA)?",
        "[TNPSC குரூப் 1] காவிரி நீர் மேலாண்மை ஆணையத்தை (CWMA) நிறுவி காவிரி நீர் மேலாண்மைத் திட்டத்தை மத்திய அரசு எந்த ஆண்டு அறிவித்தது?",
        "2014", "2014",
        "2016", "2016",
        "2017", "2017",
        "2018", "2018",
        "D",
        "Following the landmark verdict of the Supreme Court in February 2018, the Ministry of Water Resources gazetted the Cauvery Water Management Scheme on 1st June 2018, creating the CWMA and CWRC.",
        "பிப்ரவரி 2018-ல் உச்ச நீதிமன்றம் வழங்கிய வரலாற்றுச் சிறப்புமிக்க தீர்ப்பைத் தொடர்ந்து, 2018 ஜூன் 1 அன்று மத்திய அரசு காவிரி நீர் மேலாண்மைத் திட்டத்தை அரசிதழில் வெளியிட்டு CWMA மற்றும் CWRC அமைப்புகளை நிறுவியது.",
        "Option A is incorrect because 2014 is too early.", "2014 முந்தைய ஆண்டு என்பதால் விருப்பம் A தவறு.",
        "Option B is incorrect because 2016 was during the peak of Supreme Court litigation.", "2016 உச்ச நீதிமன்ற வழக்கு நடந்த காலம் என்பதால் விருப்பம் B தவறு.",
        "Option C is incorrect because 2017 was prior to the final judgment.", "2017 இறுதித் தீர்ப்பிற்கு முந்தையது என்பதால் விருப்பம் C தவறு.",
        "Option D is correct because the notification was issued in June 2018.", "ஜூன் 2018-ல் இத்திட்டம் அறிவிக்கப்பட்டதால் விருப்பம் D சரி.",
        "Milestone year: 2018 (Supreme Court Final Judgment & CWMA notification).",
        "முக்கிய ஆண்டு: 2018 (உச்ச நீதிமன்ற இறுதித் தீர்ப்பு & CWMA அறிவிப்பு).",
        "Cauvery Water Management Authority (CWMA) was notified by the Centre in June 2018.",
        "காவிரி நீர் மேலாண்மை ஆணையம் (CWMA) மத்திய அரசால் ஜூன் 2018-ல் அறிவிக்கப்பட்டது.",
        tags=["CWMA 2018", "Cauvery Scheme", "TNPSC 2021"]
    ))

    # 013 - Ans A (UPSC CSE 2007 / TNPSC 2014)
    q.append(make_pyq(
        "ISR_PYQ_013", "Medium",
        "[UPSC CSE / TNPSC] Freedom of trade, commerce, and intercourse guaranteed under Article 301 of the Indian Constitution was inspired by which country's constitution?",
        "[UPSC CSE / TNPSC] இந்திய அரசியலமைப்பின் 301-வது உறுப்பின் கீழ் உத்தரவாதம் அளிக்கப்பட்டுள்ள வர்த்தகம், வணிகம் மற்றும் தொடர்பு சுதந்திரம் எந்த நாட்டின் அரசியலமைப்பால் ஈர்க்கப்பட்டது?",
        "Australia", "ஆஸ்திரேலியா",
        "United States of America", "அமெரிக்க ஐக்கிய நாடுகள்",
        "Canada", "கனடா",
        "Ireland", "அயர்லாந்து",
        "A",
        "Part XIII (Articles 301 to 307) of the Indian Constitution, ensuring freedom of trade, commerce, and intercourse throughout the territory of India, was primarily inspired by Section 92 of the Australian Constitution.",
        "இந்திய அரசியலமைப்பின் பகுதி XIII (உறுப்புகள் 301 முதல் 307 வரை) வர்த்தகம் மற்றும் வணிகச் சுதந்திரத்தை உறுதி செய்வது முக்கியமாக ஆஸ்திரேலிய அரசியலமைப்பின் பிரிவு 92-ன் தாக்கத்தால் ஈர்க்கப்பட்டது.",
        "Option A is correct because the Australian Constitution Section 92 provided the architectural inspiration.", "ஆஸ்திரேலிய அரசியலமைப்பின் பிரிவு 92 இதன் மூலமாக அமைந்ததால் விருப்பம் A சரி.",
        "Option B is incorrect because the US Constitution has a Commerce Clause (Article I, Section 8), but the wording and concept of Article 301 was derived from Australia.", "அமெரிக்காவில் வணிக விதி இருந்தாலும், உறுப்பு 301-ன் கட்டமைப்பு ஆஸ்திரேலியாவிலிருந்து பெறப்பட்டது என்பதால் விருப்பம் B தவறு.",
        "Option C is incorrect because Canadian trade provisions are differently structured.", "கனடா வர்த்தக விதிகள் வேறுபட்டவை என்பதால் விருப்பம் C தவறு.",
        "Option D is incorrect because Ireland inspired DPSP, not trade freedom.", "அயர்லாந்து DPSP-க்கு மூலமாக இருந்ததால் விருப்பம் D தவறு.",
        "Constitutional Source: Article 301 trade freedom = Australian Constitution (Section 92).",
        "அரசியலமைப்பு மூலம்: உறுப்பு 301 வர்த்தக சுதந்திரம் = ஆஸ்திரேலிய அரசியலமைப்பு (பிரிவு 92).",
        "Freedom of trade and commerce under Article 301 was inspired by the Australian Constitution.",
        "உறுப்பு 301-ன் கீழான வர்த்தகச் சுதந்திரம் ஆஸ்திரேலிய அரசியலமைப்பின் தாக்கத்தால் உருவாக்கப்பட்டது.",
        tags=["Article 301", "Australian Constitution", "Source of Constitution"]
    ))

    # 014 - Ans B (TNPSC Group 1 2017)
    q.append(make_pyq(
        "ISR_PYQ_014", "Hard",
        "[TNPSC Group 1] Which Article of the Indian Constitution requires the 'previous sanction of the President' for introducing a State Bill that imposes reasonable restrictions on the freedom of trade and commerce?",
        "[TNPSC குரூப் 1] வர்த்தகம் மற்றும் வணிகச் சுதந்திரத்தின் மீது நியாயமான கட்டுப்பாடுகளை விதிக்கும் மாநில மசோதாவை அறிமுகப்படுத்த 'குடியரசுத் தலைவரின் முன் அனுமதி' தேவை என்று இந்திய அரசியலமைப்பின் எந்த உறுப்பு கூறுகிறது?",
        "Article 302", "உறுப்பு 302",
        "Article 304(b)", "உறுப்பு 304(b)",
        "Article 303(1)", "உறுப்பு 303(1)",
        "Article 305", "உறுப்பு 305",
        "B",
        "Under the proviso to Article 304(b), no Bill or amendment imposing reasonable restrictions on trade, commerce, or intercourse shall be introduced or moved in the Legislature of a State without the previous sanction of the President.",
        "உறுப்பு 304(b)-ன் வரம்புரையின் கீழ், வர்த்தகத்தின் மீது நியாயமான கட்டுப்பாடுகளை விதிக்கும் எந்தவொரு மசோதாவையும் குடியரசுத் தலைவரின் முன் அனுமதியின்றி மாநில சட்டமன்றத்தில் அறிமுகப்படுத்த முடியாது.",
        "Option A is incorrect because Article 302 governs Parliament's power, not State Legislatures.", "உறுப்பு 302 நாடாளுமன்றத்தின் அதிகாரத்தைக் குறிப்பிடுவதால் விருப்பம் A தவறு.",
        "Option B is correct because Article 304(b) proviso mandates Presidential previous sanction.", "உறுப்பு 304(b) குடியரசுத் தலைவரின் முன் அனுமதியைக் கட்டாயமாக்குவதால் விருப்பம் B சரி.",
        "Option C is incorrect because Article 303 relates to non-discrimination.", "உறுப்பு 303 பாகுபாடற்ற விதிக்குரியது என்பதால் விருப்பம் C தவறு.",
        "Option D is incorrect because Article 305 saves existing laws and state monopolies.", "உறுப்பு 305 அரசு ஏகபோகங்களைப் பாதுகாப்பதால் விருப்பம் D தவறு.",
        "Key exam fact: State legislature trade restrictions under Article 304(b) require PRIOR Presidential sanction.",
        "முக்கியத் தேர்வு உண்மை: உறுப்பு 304(b)-ன் கீழான மாநில வர்த்தகக் கட்டுப்பாடுகளுக்குக் குடியரசுத் தலைவரின் முன் அனுமதி அவசியம்.",
        "Article 304(b) mandates prior Presidential sanction for State legislation restricting trade freedom.",
        "வர்த்தக சுதந்திரத்தைக் கட்டுப்படுத்தும் மாநில மசோதாக்களுக்கு உறுப்பு 304(b) குடியரசுத் தலைவரின் முன் அனுமதியைக் கட்டாயமாக்குகிறது.",
        tags=["Article 304(b)", "Presidential Prior Sanction", "TNPSC PYQ"]
    ))

    # 015 - Ans C (TNPSC Group 1 2011 / 2019)
    q.append(make_pyq(
        "ISR_PYQ_015", "Easy",
        "[TNPSC Group 1] In which year did the Tamil Nadu Government appoint the Rajamannar Committee to inquire into Centre-State and Inter-State relations?",
        "[TNPSC குரூப் 1] மத்திய-மாநில மற்றும் மாநிலங்களுக்கு இடையிலான உறவுகளை ஆராய தமிழ்நாடு அரசு எந்த ஆண்டு ராஜமன்னார் குழுவை அமைத்தது?",
        "1967", "1967",
        "1968", "1968",
        "1969", "1969",
        "1971", "1971",
        "C",
        "The DMK Government in Tamil Nadu, headed by Chief Minister M. Karunanidhi, appointed the 3-member Rajamannar Committee on 22nd September 1969 (chaired by Dr. P.V. Rajamannar). The committee submitted its report in 1971.",
        "தமிழ்நாட்டில் முதல்வர் மு. கருணாநிதி தலைமையிலான திமுக அரசு, டாக்டர் பி.வி. ராஜமன்னார் தலைமையில் 1969 செப்டம்பர் 22 அன்று 3 பேர் கொண்ட ராஜமன்னார் குழுவை அமைத்தது. இக்குழு 1971-ல் தனது அறிக்கையைச் சமர்ப்பித்தது.",
        "Option A is incorrect because 1967 was when the DMK first assumed office.", "1967 திமுக முதலில் ஆட்சிக்கு வந்த ஆண்டு என்பதால் விருப்பம் A தவறு.",
        "Option B is incorrect because 1968 is one year prior to constitution.", "1968 குழு அமைக்கப்படுவதற்கு முந்தைய ஆண்டு என்பதால் விருப்பம் B தவறு.",
        "Option C is correct because the Rajamannar Committee was appointed in 1969.", "ராஜமன்னார் குழு 1969-ல் அமைக்கப்பட்டதால் விருப்பம் C சரி.",
        "Option D is incorrect because 1971 was when the report was submitted, not appointed.", "1971 அறிக்கை சமர்ப்பிக்கப்பட்ட ஆண்டு என்பதால் விருப்பம் D தவறு.",
        "Rajamannar Committee: Appointed in 1969; Report submitted in 1971. First committee by a State on federal relations.",
        "ராஜமன்னார் குழு: அமைக்கப்பட்டது = 1969; அறிக்கை சமர்ப்பித்தது = 1971. கூட்டாட்சி உறவுகள் குறித்து ஒரு மாநில அரசால் அமைக்கப்பட்ட முதல் குழு.",
        "The Rajamannar Committee was appointed by Tamil Nadu in 1969 to examine Centre-State and inter-state relations.",
        "மத்திய-மாநில மற்றும் மாநிலங்களுக்கு இடையேயான உறவுகளை ஆராய 1969-ல் தமிழ்நாடு அரசால் ராஜமன்னார் குழு அமைக்கப்பட்டது.",
        tags=["Rajamannar Committee 1969", "Tamil Nadu Polity", "TNPSC PYQ"]
    ))

    # 016 - Ans D (UPSC CSE 2013 / TNPSC 2022)
    q.append(make_pyq(
        "ISR_PYQ_016", "Medium",
        "[UPSC CSE / TNPSC Group 1] Which of the following is NOT a member of the Inter-State Council?",
        "[UPSC CSE / TNPSC குரூப் 1] பின்வருபவர்களில் யார் மாநிலங்களுக்கு இடையிலான மன்றத்தின் உறுப்பினர் அல்ல?",
        "Chief Ministers of all States", "அனைத்து மாநிலங்களின் முதலமைச்சர்கள்",
        "Chief Ministers of Union Territories having legislative assemblies", "சட்டமன்றங்களைக் கொண்ட யூனியன் பிரதேசங்களின் முதலமைச்சர்கள்",
        "Six Union Cabinet Ministers nominated by the Prime Minister", "பிரதமரால் நியமிக்கப்படும் ஆறு மத்திய அமைச்சரவை அமைச்சர்கள்",
        "Governors of all States", "அனைத்து மாநிலங்களின் ஆளுநர்கள்",
        "D",
        "The Inter-State Council consists of the Prime Minister (Chairman), Chief Ministers of all States and UTs with assemblies, Administrators of UTs without assemblies, and 6 Union Cabinet Ministers. Governors of States are NOT members (except when a State is under President's Rule under Article 356).",
        "மாநிலங்களுக்கு இடையிலான மன்றத்தில் பிரதமர், அனைத்து மாநில முதலமைச்சர்கள், சட்டமன்றம் உள்ள யூனியன் பிரதேச முதலமைச்சர்கள், யூனியன் பிரதேச நிர்வாகிகள் மற்றும் 6 மத்திய அமைச்சர்கள் உள்ளனர். மாநில ஆளுநர்கள் இதன் உறுப்பினர்கள் அல்ல (குடியரசுத் தலைவர் ஆட்சியின் போது மட்டுமே ஆளுநர் பங்கேற்கிறார்).",
        "Option A is incorrect because all State Chief Ministers are core members.", "மாநில முதலமைச்சர்கள் இதன் உறுப்பினர்கள் என்பதால் விருப்பம் A தவறு.",
        "Option B is incorrect because UT Chief Ministers (Delhi, Puducherry, J&K) are members.", "யூனியன் பிரதேச முதலமைச்சர்கள் உறுப்பினர்கள் என்பதால் விருப்பம் B தவறு.",
        "Option C is incorrect because 6 Union Cabinet Ministers nominated by the PM are members.", "பிரதமரால் நியமிக்கப்படும் 6 மத்திய அமைச்சர்கள் உறுப்பினர்கள் என்பதால் விருப்பம் C தவறு.",
        "Option D is correct because Governors of States are normally excluded from Council membership.", "சாதாரண சூழ்நிலைகளில் மாநில ஆளுநர்கள் இதில் உறுப்பினர்கள் அல்ல என்பதால் விருப்பம் D சரி.",
        "ISC Membership trap: Chief Ministers are members, Governors are NOT (unless under President's Rule).",
        "மன்ற உறுப்பினர் பொறி: முதலமைச்சர்களே உறுப்பினர்கள்; ஆளுநர்கள் உறுப்பினர் அல்ல (குடியரசுத் தலைவர் ஆட்சி தவிர).",
        "Governors are not members of the Inter-State Council; Chief Ministers represent the States.",
        "மாநிலங்களுக்கு இடையிலான மன்றத்தில் ஆளுநர்கள் உறுப்பினர்கள் அல்ல; முதலமைச்சர்களே மாநிலங்களைப் பிரதிநிதித்துவப்படுத்துகின்றனர்.",
        tags=["ISC Membership", "No Governors", "TNPSC PYQ"]
    ))

    # 017 - Ans A (TNPSC Group 1 2019)
    q.append(make_pyq(
        "ISR_PYQ_017", "Hard",
        "[TNPSC Group 1] The landmark Supreme Court judgment in State of Karnataka v. State of Tamil Nadu (2018) on the Cauvery dispute held that river waters are:",
        "[TNPSC குரூப் 1] காவிரி தகராறு தொடர்பான கர்நாடக மாநிலம் எதிர் தமிழ்நாடு மாநிலம் (2018) வழக்கில் உச்ச நீதிமன்றத்தின் வரலாற்றுத் தீர்ப்பு நதிநீரை எவ்வாறு அறிவித்தது?",
        "A national asset in which no single state can claim exclusive ownership", "எந்தவொரு தனி மாநிலமும் பிரத்யேக உரிமை கோர முடியாத ஒரு தேசியச் சொத்து",
        "The absolute private property of the upper riparian State", "மேல் வடிநில மாநிலத்தின் முழுமையான தனிச்சொத்து",
        "Exclusively subject to the territorial sovereignty of the originating State", "நதி உற்பத்தியாகும் மாநிலத்தின் பிராந்திய இறையாண்மைக்கு மட்டுமே உட்பட்டது",
        "A commodity subject to unrestricted commercial exploitation by riparians", "வடிநில மாநிலங்களால் தடையற்ற வணிகச் சுரண்டலுக்கு உட்படுத்தப்பட வேண்டிய ஒரு பொருள்",
        "A",
        "In February 2018, a 3-judge bench of the Supreme Court headed by CJI Dipak Misra affirmed the doctrine that waters of an inter-State river are a 'national asset' and no individual State can claim exclusive proprietary rights under the Harmon Doctrine.",
        "பிப்ரவரி 2018-ல் தலைமை நீதிபதி தீபக் மிஸ்ரா தலைமையிலான உச்ச நீதிமன்ற அமர்வு, மாநிலங்களுக்கு இடையேயான நதிநீர் என்பது ஒரு 'தேசியச் சொத்து' (National Asset) என்றும், ஹார்மன் கோட்பாட்டின்படி எந்தவொரு தனி மாநிலமும் நதிநீரின் மீது முழுக் கட்டுப்பாடு கோர முடியாது என்றும் தீர்ப்பளித்தது.",
        "Option A is correct because the Supreme Court declared inter-state river waters to be a national asset.", "நதிநீர் ஒரு தேசியச் சொத்து என உச்ச நீதிமன்றம் அறிவித்ததால் விருப்பம் A சரி.",
        "Option B is incorrect because the upper riparian territorial sovereignty claim (Harmon doctrine) was completely rejected.", "மேல் மாநிலத்தின் முழு உரிமை கோரிக்கை நிராகரிக்கப்பட்டதால் விருப்பம் B தவறு.",
        "Option C is incorrect because territorial ownership was denied.", "பிராந்திய உரிமை மறுக்கப்பட்டதால் விருப்பம் C தவறு.",
        "Option D is incorrect because water was recognized as a shared public trust resource.", "நீர் பொதுப் பயன்பாட்டு வளமாக அங்கீகரிக்கப்பட்டதால் விருப்பம் D தவறு.",
        "Harmon Doctrine (absolute territorial sovereignty) is REJECTED in India; inter-state river water is a NATIONAL ASSET.",
        "இந்தியாவில் ஹார்மன் கோட்பாடு நிராகரிக்கப்பட்டது; மாநிலங்களுக்கு இடையேயான நதிநீர் என்பது ஒரு 'தேசியச் சொத்து'.",
        "Supreme Court declared in 2018 that inter-state river water is a national asset, rejecting exclusive state ownership.",
        "மாநிலங்களுக்கு இடையிலான நதிநீர் ஒரு தேசியச் சொத்து என்று 2018-ல் உச்ச நீதிமன்றம் அறிவித்தது.",
        tags=["Cauvery Judgment 2018", "National Asset", "Harmon Doctrine Rejected"]
    ))

    # 018 - Ans B (TNPSC Group 2 2018)
    q.append(make_pyq(
        "ISR_PYQ_018", "Medium",
        "[TNPSC Group 2] How many Zonal Councils were established in India originally under the States Reorganisation Act, 1956?",
        "[TNPSC குரூப் 2] 1956-ஆம் ஆண்டின் மாநில மறுசீரமைப்புச் சட்டத்தின் கீழ் இந்தியாவில் முதலில் எத்தனை மண்டலக் குழுக்கள் நிறுவப்பட்டன?",
        "4", "4",
        "5", "5",
        "6", "6",
        "8", "8",
        "B",
        "The States Reorganisation Act, 1956 established five Zonal Councils: Northern, Central, Eastern, Western, and Southern. The North-Eastern Council was established separately under the NEC Act, 1971.",
        "1956 மாநில மறுசீரமைப்புச் சட்டம் வடக்கு, மத்திய, கிழக்கு, மேற்கு மற்றும் தெற்கு என ஐந்து மண்டலக் குழுக்களை நிறுவியது. வடகிழக்குக் குழு 1971 சட்டத்தின் கீழ் தனியாக அமைக்கப்பட்டது.",
        "Option A is incorrect because four is an undercount.", "நான்கு என்பது தவறான எண்ணிக்கை என்பதால் விருப்பம் A தவறு.",
        "Option B is correct because exactly five Zonal Councils were established in 1956.", "1956-ல் சரியாக ஐந்து மண்டலக் குழுக்கள் அமைக்கப்பட்டதால் விருப்பம் B சரி.",
        "Option C is incorrect because the sixth council (NEC) was created in 1971 under a different Act.", "ஆறாவது குழு (NEC) 1971-ல் தனிச் சட்டத்தால் உருவாக்கப்பட்டதால் விருப்பம் C தவறு.",
        "Option D is incorrect because eight is the number of states in the NEC.", "எட்டு என்பது NEC-ல் உள்ள மாநிலங்களின் எண்ணிக்கை என்பதால் விருப்பம் D தவறு.",
        "Remember: 1956 Act = 5 Zonal Councils; 1971 Act = North-Eastern Council.",
        "நினைவில் கொள்க: 1956 சட்டம் = 5 மண்டலக் குழுக்கள்; 1971 சட்டம் = வடகிழக்குக் குழு.",
        "Five Zonal Councils were created under the States Reorganisation Act of 1956.",
        "1956 மாநில மறுசீரமைப்புச் சட்டத்தின் கீழ் ஐந்து மண்டலக் குழுக்கள் உருவாக்கப்பட்டன.",
        tags=["Five Zonal Councils", "States Reorganisation Act 1956", "TNPSC PYQ"]
    ))

    # 019 - Ans C (TNPSC Group 1 2017)
    q.append(make_pyq(
        "ISR_PYQ_019", "Hard",
        "[TNPSC Group 1] In the landmark Atiabari Tea Co. v. State of Assam (1961) case, the Supreme Court interpreted which Article of the Constitution?",
        "[TNPSC குரூப் 1] வரலாற்றுச் சிறப்புமிக்க அத்தியாபாரி டீ கம்பெனி எதிர் அசாம் மாநிலம் (1961) வழக்கில், உச்ச நீதிமன்றம் அரசியலமைப்பின் எந்த உறுப்பை விளக்கியது?",
        "Article 262", "உறுப்பு 262",
        "Article 263", "உறுப்பு 263",
        "Article 301", "உறுப்பு 301",
        "Article 356", "உறுப்பு 356",
        "C",
        "In Atiabari Tea Co. v. State of Assam (1961), the Constitution Bench interpreted Article 301 and held that taxing laws that impose direct and immediate restrictions on the movement of goods violate the freedom of trade and commerce.",
        "அத்தியாபாரி டீ கம்பெனி எதிர் அசாம் மாநிலம் (1961) வழக்கில், உச்ச நீதிமன்ற அரசியலமைப்பு அமர்வு உறுப்பு 301-ஐ விளக்கியது; பொருட்களின் போக்குவரத்தைத் நேரடியாகத் தடுக்கும் வரிச் சட்டங்கள் வர்த்தகச் சுதந்திரத்தை மீறுவதாகத் தீர்ப்பளித்தது.",
        "Option A is incorrect because Article 262 relates to water disputes.", "உறுப்பு 262 நதிநீர் தகராறுகளுக்குரியது என்பதால் விருப்பம் A தவறு.",
        "Option B is incorrect because Article 263 relates to the Inter-State Council.", "உறுப்பு 263 மாநிலங்களுக்கு இடையிலான மன்றத்திற்குரியது என்பதால் விருப்பம் B தவறு.",
        "Option C is correct because Atiabari is the foundational case on Article 301 freedom of trade and commerce.", "அத்தியாபாரி வழக்கு உறுப்பு 301 வர்த்தக சுதந்திரத்திற்கான அடிப்படை வழக்கு என்பதால் விருப்பம் C சரி.",
        "Option D is incorrect because Article 356 relates to President's Rule.", "உறுப்பு 356 குடியரசுத் தலைவர் ஆட்சிக்குரியது என்பதால் விருப்பம் D தவறு.",
        "Atiabari Tea Co. (1961) and Automobile Transport (1962) are the two pillars of Article 301 jurisprudence.",
        "அத்தியாபாரி (1961) மற்றும் ஆட்டோமொபைல் டிரான்ஸ்போர்ட் (1962) ஆகியவை உறுப்பு 301 சட்டக் கோட்பாட்டின் இரு தூண்கள்.",
        "Atiabari Tea Co. v. State of Assam (1961) is the landmark judgment defining the scope of Article 301.",
        "அத்தியாபாரி டீ கம்பெனி வழக்கு (1961) உறுப்பு 301-ன் வரம்பை வரையறுத்த வரலாற்றுத் தீர்ப்பாகும்.",
        tags=["Atiabari Case", "Article 301", "TNPSC PYQ"]
    ))

    # 020 - Ans D (TNPSC Group 1 2019)
    q.append(make_pyq(
        "ISR_PYQ_020", "Medium",
        "[TNPSC Group 1] In which year was the first Administrative Reforms Commission (ARC) appointed that recommended the establishment of an Inter-State Council under Article 263?",
        "[TNPSC குரூப் 1] உறுப்பு 263-ன் கீழ் மாநிலங்களுக்கு இடையிலான மன்றத்தை அமைக்கப் பரிந்துரைத்த முதல் நிர்வாகச் சீர்திருத்த ஆணையம் (ARC) எந்த ஆண்டு அமைக்கப்பட்டது?",
        "1956", "1956",
        "1962", "1962",
        "1964", "1964",
        "1966", "1966",
        "D",
        "The first Administrative Reforms Commission was appointed in January 1966 (initially chaired by Morarji Desai, and later by K. Hanumanthaiah). In its 1969 report on Centre-State Relations, it recommended the setting up of an Inter-State Council under Article 263.",
        "முதல் நிர்வாகச் சீர்திருத்த ஆணையம் 1966 ஜனவரியில் அமைக்கப்பட்டது (முதலில் மொரார்ஜி தேசாய், பின்னர் கே. ஹனுமந்தையா தலைவராக இருந்தனர்). 1969-ல் சமர்ப்பிக்கப்பட்ட மத்திய-மாநில உறவுகள் குறித்த தனது அறிக்கையில், உறுப்பு 263-ன் கீழ் மாநிலங்களுக்கு இடையிலான மன்றத்தை அமைக்க இது பரிந்துரைத்தது.",
        "Option A is incorrect because 1956 was the year of the States Reorganisation Act.", "1956 மாநில மறுசீரமைப்புச் சட்டம் இயற்றப்பட்ட ஆண்டு என்பதால் விருப்பம் A தவறு.",
        "Option B is incorrect because 1962 was the year of the Sino-Indian War.", "1962 இந்திய-சீனப் போர் நடந்த ஆண்டு என்பதால் விருப்பம் B தவறு.",
        "Option C is incorrect because 1964 was the year the Santhanam Committee reported on corruption.", "1964 சந்தானம் குழு அறிக்கை சமர்ப்பித்த ஆண்டு என்பதால் விருப்பம் C தவறு.",
        "Option D is correct because the First ARC was appointed in 1966.", "முதல் நிர்வாகச் சீர்திருத்த ஆணையம் 1966-ல் அமைக்கப்பட்டதால் விருப்பம் D சரி.",
        "First ARC (1966) recommended the Inter-State Council long before the Sarkaria Commission (1988) reiterated it.",
        "சர்க்காரியா ஆணையத்திற்கு (1988) முன்னரே, முதல் நிர்வாகச் சீர்திருத்த ஆணையம் (1966) மன்றத்தை அமைக்கப் பரிந்துரைத்தது.",
        "First ARC was appointed in 1966 and recommended an Inter-State Council in its 1969 report.",
        "முதல் நிர்வாகச் சீர்திருத்த ஆணையம் 1966-ல் அமைக்கப்பட்டு, 1969 அறிக்கையில் மாநிலங்களுக்கு இடையிலான மன்றத்தைப் பரிந்துரைத்தது.",
        tags=["First ARC 1966", "Morarji Desai", "Inter-State Council Recommendation"]
    ))

    # 021 - Ans A (TNPSC Group 1 2021)
    q.append(make_pyq(
        "ISR_PYQ_021", "Medium",
        "[TNPSC Group 1] In which year was the Second Commission on Centre-State Relations (Punchhi Commission) appointed by the Government of India?",
        "[TNPSC குரூப் 1] மத்திய-மாநில உறவுகள் குறித்த இரண்டாவது ஆணையம் (பூஞ்சி ஆணையம்) இந்திய அரசால் எந்த ஆண்டு அமைக்கப்பட்டது?",
        "2007", "2007",
        "2004", "2004",
        "2010", "2010",
        "2014", "2014",
        "A",
        "The Second Commission on Centre-State Relations was set up in April 2007 under the chairmanship of Justice Madan Mohan Punchhi (former Chief Justice of India). It submitted its report in March 2010.",
        "மத்திய-மாநில உறவுகள் குறித்த இரண்டாவது ஆணையம் 2007 ஏப்ரலில் முன்னாள் இந்தியத் தலைமை நீதிபதி மதன் மோகன் பூஞ்சி தலைமையில் அமைக்கப்பட்டது. இது 2010 மார்ச்சில் தனது அறிக்கையைச் சமர்ப்பித்தது.",
        "Option A is correct because the Punchhi Commission was constituted in April 2007.", "பூஞ்சி ஆணையம் 2007 ஏப்ரலில் அமைக்கப்பட்டதால் விருப்பம் A சரி.",
        "Option B is incorrect because 2004 was when the Second Krishna Tribunal was formed.", "2004 இரண்டாவது கிருஷ்ணா தீர்ப்பாயம் அமைக்கப்பட்ட ஆண்டு என்பதால் விருப்பம் B தவறு.",
        "Option C is incorrect because 2010 was when the Punchhi Commission submitted its report.", "2010 அறிக்கை சமர்ப்பிக்கப்பட்ட ஆண்டு என்பதால் விருப்பம் C தவறு.",
        "Option D is incorrect because 2014 is much later.", "2014 பிந்தைய ஆண்டு என்பதால் விருப்பம் D தவறு.",
        "Commissions timeline: Rajamannar (1969), Sarkaria (1983-1988), Punchhi (2007-2010).",
        "ஆணையங்களின் காலவரிசை: ராஜமன்னார் (1969), சர்க்காரியா (1983-1988), பூஞ்சி (2007-2010).",
        "Punchhi Commission on Centre-State relations was appointed in 2007 and reported in 2010.",
        "மத்திய-மாநில உறவுகள் குறித்த பூஞ்சி ஆணையம் 2007-ல் அமைக்கப்பட்டு 2010-ல் அறிக்கை சமர்ப்பித்தது.",
        tags=["Punchhi Commission 2007", "Centre-State Relations", "TNPSC PYQ"]
    ))

    # 022 - Ans B (TNPSC Group 2 2015)
    q.append(make_pyq(
        "ISR_PYQ_022", "Easy",
        "[TNPSC Group 2] Where is the headquarters of the Eastern Zonal Council situated?",
        "[TNPSC குரூப் 2] கிழக்கு மண்டலக் குழுவின் தலைமையகம் எங்கு அமைந்துள்ளது?",
        "Bhubaneswar", "புவனேஸ்வர்",
        "Kolkata", "கொல்கத்தா",
        "Patna", "பாட்னா",
        "Ranchi", "ராஞ்சி",
        "B",
        "The headquarters of the Eastern Zonal Council (comprising Bihar, Jharkhand, Odisha, and West Bengal) is located at Kolkata.",
        "பீகார், ஜார்க்கண்ட், ஒடிசா மற்றும் மேற்கு வங்காளத்தை உள்ளடக்கிய கிழக்கு மண்டலக் குழுவின் தலைமையகம் கொல்கத்தாவில் அமைந்துள்ளது.",
        "Option A is incorrect because Bhubaneswar is the capital of Odisha, not the zonal headquarters.", "புவனேஸ்வர் ஒடிசாவின் தலைநகர், மண்டலத் தலைமையகம் அல்ல என்பதால் விருப்பம் A தவறு.",
        "Option B is correct because Kolkata is the statutory headquarters of the Eastern Zonal Council.", "கொல்கத்தா கிழக்கு மண்டலக் குழுவின் தலைமையகம் என்பதால் விருப்பம் B சரி.",
        "Option C is incorrect because Patna is the capital of Bihar.", "பாட்னா பீகாரின் தலைநகர் என்பதால் விருப்பம் C தவறு.",
        "Option D is incorrect because Ranchi is the capital of Jharkhand.", "ராஞ்சி ஜார்க்கண்டின் தலைநகர் என்பதால் விருப்பம் D தவறு.",
        "Zonal HQs summary: Northern = New Delhi, Central = Prayagraj, Eastern = Kolkata, Western = Mumbai, Southern = Chennai.",
        "மண்டலத் தலைமையகங்கள்: வடக்கு = புதுதில்லி, மத்திய = பிரயாக்ராஜ், கிழக்கு = கொல்கத்தா, மேற்கு = மும்பை, தெற்கு = சென்னை.",
        "Eastern Zonal Council is headquartered in Kolkata.",
        "கிழக்கு மண்டலக் குழு கொல்கத்தாவில் தலைமையகத்தைக் கொண்டுள்ளது.",
        tags=["Eastern Zonal Council", "Kolkata HQ", "TNPSC PYQ"]
    ))

    # 023 - Ans C (TNPSC Group 1 2022)
    q.append(make_pyq(
        "ISR_PYQ_023", "Medium",
        "[TNPSC Group 1] Which Section of the Inter-State River Water Disputes Act, 1956 explicitly bars the jurisdiction of the Supreme Court and all other courts in respect of a referred water dispute?",
        "[TNPSC குரூப் 1] 1956-ஆம் ஆண்டின் மாநிலங்களுக்கு இடையேயான நதிநீர் தகராறுகள் சட்டத்தின் எந்தப் பிரிவு உச்ச நீதிமன்றம் மற்றும் பிற அனைத்து நீதிமன்றங்களின் அதிகார வரம்பையும் தெளிவாகத் தடுக்கிறது?",
        "Section 4", "பிரிவு 4",
        "Section 6", "பிரிவு 6",
        "Section 11", "பிரிவு 11",
        "Section 14", "பிரிவு 14",
        "C",
        "Section 11 of the Inter-State River Water Disputes Act, 1956 explicitly enacts the bar of jurisdiction, providing that neither the Supreme Court nor any other court shall have or exercise jurisdiction in respect of any water dispute referred to a Tribunal.",
        "1956 நதிநீர் தகராறுகள் சட்டம் பிரிவு 11, தீர்ப்பாயத்திற்கு அனுப்பப்பட்ட எந்தவொரு நதிநீர் தகராறு குறித்தும் உச்ச நீதிமன்றமோ அல்லது பிற எந்த நீதிமன்றமோ அதிகார வரம்பைச் செலுத்தக் கூடாது எனத் தெளிவாகத் தடுக்கிறது.",
        "Option A is incorrect because Section 4 relates to the constitution of the Tribunal.", "பிரிவு 4 தீர்ப்பாயம் அமைப்பதற்குரியது என்பதால் விருப்பம் A தவறு.",
        "Option B is incorrect because Section 6 deals with publication of the Tribunal's decision.", "பிரிவு 6 தீர்ப்பாய முடிவை வெளியிடுவதற்குரியது என்பதால் விருப்பம் B தவறு.",
        "Option C is correct because Section 11 is the statutory ouster/bar of judicial jurisdiction.", "பிரிவு 11 நீதிமன்ற அதிகார வரம்பை விலக்கும் பிரிவு என்பதால் விருப்பம் C சரி.",
        "Option D is incorrect because Section 14 is not the ouster clause.", "பிரிவு 14 அதிகார விலக்கு பிரிவு அல்ல என்பதால் விருப்பம் D தவறு.",
        "Core statutory clause: Section 11 of the 1956 Act implements Article 262(2) court exclusion.",
        "முக்கிய சட்டப் பிரிவு: 1956 சட்டத்தின் பிரிவு 11 உறுப்பு 262(2)-ன் நீதிமன்ற வரம்பு விலக்கை நடைமுறைப்படுத்துகிறது.",
        "Section 11 of the IRWD Act, 1956 bars the jurisdiction of the Supreme Court and other courts.",
        "1956 IRWD சட்டத்தின் பிரிவு 11 உச்ச நீதிமன்றம் மற்றும் பிற நீதிமன்றங்களின் அதிகார வரம்பைத் தடுக்கிறது.",
        tags=["Section 11 IRWD Act", "Jurisdiction Bar", "TNPSC PYQ"]
    ))

    # 024 - Ans D (TNPSC Group 1 2017)
    q.append(make_pyq(
        "ISR_PYQ_024", "Hard",
        "[TNPSC Group 1] In which Schedule and Entry of the Constitution of India is 'Regulation and development of inter-State rivers and river valleys' placed?",
        "[TNPSC குரூப் 1] இந்திய அரசியலமைப்பின் எந்த அட்டவணை மற்றும் பதிவில் 'மாநிலங்களுக்கு இடையிலான நதிகள் மற்றும் நதிப் பள்ளத்தாக்குகளின் ஒழுங்குமுறை மற்றும் மேம்பாடு' வைக்கப்பட்டுள்ளது?",
        "Seventh Schedule, List II (State List), Entry 17", "ஏழாவது அட்டவணை, பட்டியல் II (மாநிலப் பட்டியல்), பதிவு 17",
        "Seventh Schedule, List III (Concurrent List), Entry 20", "ஏழாவது அட்டவணை, பட்டியல் III (பொதுப் பட்டியல்), பதிவு 20",
        "Seventh Schedule, List I (Union List), Entry 54", "ஏழாவது அட்டவணை, பட்டியல் I (மத்தியப் பட்டியல்), பதிவு 54",
        "Seventh Schedule, List I (Union List), Entry 56", "ஏழாவது அட்டவணை, பட்டியல் I (மத்தியப் பட்டியல்), பதிவு 56",
        "D",
        "Entry 56 of the Union List (List I) in the Seventh Schedule empowers the Union to regulate and develop inter-State rivers and river valleys to the extent declared by Parliament by law to be expedient in the public interest. State List Entry 17 (water) is expressly subject to Entry 56 of List I.",
        "ஏழாவது அட்டவணையின் மத்தியப் பட்டியல் (பட்டியல் I) பதிவு 56, பொது நலன் கருதி நாடாளுமன்றம் அறிவிக்கும் அளவிற்கு மாநிலங்களுக்கு இடையிலான நதிகள் மற்றும் நதிப் பள்ளத்தாக்குகளை ஒழுங்குபடுத்த ஒன்றியத்திற்கு அதிகாரம் அளிக்கிறது. மாநிலப் பட்டியல் பதிவு 17 இதற்கு உட்பட்டது.",
        "Option A is incorrect because Entry 17 of State List covers water, but is subject to Entry 56 of List I.", "மாநிலப் பட்டியல் பதிவு 17 நீர் பற்றியது என்றாலும், அது மத்தியப் பட்டியல் 56-க்கு உட்பட்டது என்பதால் விருப்பம் A தவறு.",
        "Option B is incorrect because Entry 20 of List III relates to economic and social planning.", "பொதுப் பட்டியல் பதிவு 20 பொருளாதாரத் திட்டமிடலுக்குரியது என்பதால் விருப்பம் B தவறு.",
        "Option C is incorrect because Entry 54 of List I relates to regulation of mines and mineral development.", "மத்தியப் பட்டியல் பதிவு 54 சுரங்கங்கள் மற்றும் கனிமங்களுக்குரியது என்பதால் விருப்பம் C தவறு.",
        "Option D is correct because Entry 56 of the Union List specifically governs inter-State rivers.", "மத்தியப் பட்டியல் பதிவு 56 மாநிலங்களுக்கு இடையிலான நதிகளை நிர்வகிப்பதால் விருப்பம் D சரி.",
        "Seventh Schedule Water code: List I Entry 56 (Inter-State Rivers) overrides List II Entry 17 (State Water).",
        "ஏழாவது அட்டவணை நதி விதி: பட்டியல் I பதிவு 56 (மாநிலங்களுக்கு இடையிலான நதிகள்) பட்டியல் II பதிவு 17-ஐ விட மேலோங்குகிறது.",
        "Entry 56 of the Union List in the Seventh Schedule governs inter-State rivers and river valleys.",
        "ஏழாவது அட்டவணையின் மத்தியப் பட்டியல் பதிவு 56 மாநிலங்களுக்கு இடையிலான நதிகளை நிர்வகிக்கிறது.",
        tags=["Seventh Schedule", "Entry 56 Union List", "Inter-State Rivers"]
    ))

    # 025 - Ans A (UPSC CSE 2015 / TNPSC 2019)
    q.append(make_pyq(
        "ISR_PYQ_025", "Medium",
        "[UPSC CSE / TNPSC Group 1] Who serves as the Chairman of the Standing Committee of the Inter-State Council?",
        "[UPSC CSE / TNPSC குரூப் 1] மாநிலங்களுக்கு இடையிலான மன்றத்தின் நிலைக்குழுவின் தலைவராகச் செயல்படுபவர் யார்?",
        "Union Home Minister", "மத்திய உள்துறை அமைச்சர்",
        "Prime Minister", "பிரதமர்",
        "Cabinet Secretary", "அமைச்சரவைச் செயலாளர்",
        "Union Finance Minister", "மத்திய நிதி அமைச்சர்",
        "A",
        "The Standing Committee of the Inter-State Council, constituted in 1996 for continuous consultation, is chaired by the Union Home Minister. It consists of the Union Home Minister (Chairman), 5 Union Cabinet Ministers, and 9 Chief Ministers.",
        "தொடர் ஆலோசனைக்காக 1996-ல் உருவாக்கப்பட்ட மாநிலங்களுக்கு இடையிலான மன்றத்தின் நிலைக்குழுவிற்கு மத்திய உள்துறை அமைச்சர் தலைமை தாங்குகிறார். இதில் உள்துறை அமைச்சர் (தலைவர்), 5 மத்திய அமைச்சர்கள் மற்றும் 9 முதலமைச்சர்கள் உள்ளனர்.",
        "Option A is correct because the Union Home Minister is the Chairman of the Standing Committee.", "மத்திய உள்துறை அமைச்சரே நிலைக்குழுவின் தலைவர் என்பதால் விருப்பம் A சரி.",
        "Option B is incorrect because the Prime Minister chairs the full Inter-State Council, not the Standing Committee.", "பிரதமர் முழு மன்றத்திற்குத் தலைமை தாங்குகிறார், நிலைக்குழுவிற்கு அல்ல என்பதால் விருப்பம் B தவறு.",
        "Option C is incorrect because the Cabinet Secretary is not the chair.", "கேபினட் செயலாளர் தலைவர் அல்ல என்பதால் விருப்பம் C தவறு.",
        "Option D is incorrect because the Finance Minister is only an ordinary member.", "நிதி அமைச்சர் ஒரு உறுப்பினர் மட்டுமே என்பதால் விருப்பம் D தவறு.",
        "Golden rule: Inter-State Council = Chaired by PM; ISC Standing Committee = Chaired by Union Home Minister.",
        "பொன்விதி: மாநிலங்களுக்கு இடையிலான மன்றம் = பிரதமர் தலைவர்; மன்றத்தின் நிலைக்குழு = மத்திய உள்துறை அமைச்சர் தலைவர்.",
        "The Union Home Minister chairs the Standing Committee of the Inter-State Council.",
        "மத்திய உள்துறை அமைச்சர் மாநிலங்களுக்கு இடையிலான மன்றத்தின் நிலைக்குழுவிற்குத் தலைமை தாங்குகிறார்.",
        tags=["Standing Committee", "Home Minister", "TNPSC PYQ"]
    ))

    return q
