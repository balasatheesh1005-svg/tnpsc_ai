# -*- coding: utf-8 -*-
"""
Builder for Inter-State Relations Part 1 — Hard MCQs (50 Questions)
IDs: ISR_H_001 to ISR_H_050
"""

import json
import os
import sys
from pathlib import Path

def make_q(qid, qtype, stem_en, stem_ta, opt_a_en, opt_a_ta, opt_b_en, opt_b_ta, opt_c_en, opt_c_ta, opt_d_en, opt_d_ta,
           correct_ans, exp_en, exp_ta, wno_a_en, wno_a_ta, wno_b_en, wno_b_ta, wno_c_en, wno_c_ta, wno_d_en, wno_d_ta,
           tip_en, tip_ta, rev_en, rev_ta, bloom="Analyze", est_time=75, tags=None):
    opts = [
        {"id": "A", "en": opt_a_en, "ta": opt_a_ta},
        {"id": "B", "en": opt_b_en, "ta": opt_b_ta},
        {"id": "C", "en": opt_c_en, "ta": opt_c_ta},
        {"id": "D", "en": opt_d_en, "ta": opt_d_ta}
    ]
    return {
        "id": qid,
        "subject": "Polity",
        "topic": "Inter-State Relations",
        "difficulty": "Hard",
        "question_type": qtype,
        "question": {"en": stem_en, "ta": stem_ta},
        "question_en": stem_en,
        "question_ta": stem_ta,
        "options": opts,
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
        "source_reference": ["M. Laxmikanth - Indian Polity", "NCERT Class XI", "Samacheer Kalvi"],
        "bloom_level": bloom,
        "estimated_time_sec": est_time,
        "pyq_similarity": "High",
        "tags": tags or ["Inter-State Relations", "Analytical", "Landmark Jurisprudence"]
    }

def get_hard_questions():
    q = []

    # 001 - Ans A
    q.append(make_q(
        "ISR_H_001", "Landmark Case Analysis",
        "In the landmark case of Atiabari Tea Co. Ltd. v. State of Assam (1961), what critical constitutional test did the Supreme Court formulate to determine whether a tax violates the freedom of trade guaranteed under Article 301?",
        "அதியபாரி டீ கம்பெனி லிமிடெட் vs அசாம் மாநிலம் (1961) என்ற வரலாற்றுச் சிறப்புமிக்க வழக்கில், ஒரு வரி உறுப்பு 301-ன் கீழ் உத்தரவாதம் அளிக்கப்பட்ட வர்த்தக சுதந்திரத்தை மீறுகிறதா என்பதைத் தீர்மானிக்க உச்ச நீதிமன்றம் உருவாக்கிய முக்கியமான அரசியலமைப்புத் தேர்வு எது?",
        "Taxes that directly and immediately restrict or impede the free movement or transport of goods violate Article 301 unless saved by Article 304(b).", "சரக்குகளின் தடையற்ற இயக்கம் அல்லது போக்குவரத்தை நேரடியாகவும் உடனடியாகவும் கட்டுப்படுத்தும் அல்லது தடுக்கும் வரிகள், உறுப்பு 304(b)-ஆல் பாதுகாக்கப்படாவிட்டால், உறுப்பு 301-ஐ மீறுவதாகும்.",
        "Any tax whatsoever levied by a State Legislature on goods is per se unconstitutional under Article 301.", "பொருட்கள் மீது ஒரு மாநில சட்டமன்றத்தால் விதிக்கப்படும் எந்தவொரு வரியும் உறுப்பு 301-ன் கீழ் தன்னிச்சையாகவே அரசியலமைப்பிற்கு முரணானது.",
        "Only customs duties imposed at international boundaries fall within the prohibition of Article 301.", "சர்வதேச எல்லைகளில் விதிக்கப்படும் சுங்க வரிகள் மட்டுமே உறுப்பு 301-ன் தடையின் கீழ் வருகின்றன.",
        "Taxes violate Article 301 only if enacted during a proclaimed state of national financial emergency.", "தேசிய நிதி நெருக்கடி நிலைப் பிரகடனத்தின் போது இயற்றப்பட்டால் மட்டுமே வரிகள் உறுப்பு 301-ஐ மீறுகின்றன.",
        "A",
        "In Atiabari Tea Co. (1961), a Constitution Bench held that the freedom guaranteed by Article 301 is a freedom from all restrictions on trade and commerce, whether intra-State or inter-State. The majority ruled that taxes which DIRECTLY AND IMMEDIATELY impede the free movement of trade violate Article 301 unless saved by compliance with Article 304(b) (including previous presidential sanction).",
        "அதியபாரி டீ கம்பெனி (1961) வழக்கில், அரசியலமைப்பு அமர்வு, உறுப்பு 301-ன் கீழான சுதந்திரம் வர்த்தக இயக்கத்தின் மீதான அனைத்துக் கட்டுப்பாடுகளிலிருந்தும் விடுபடுவதாகும் என்று கூறியது. வர்த்தகத்தின் தடையற்ற இயக்கத்தை 'நேரடியாகவும் உடனடியாகவும்' (directly and immediately) தடுக்கும் வரிகள், உறுப்பு 304(b)-ன் கீழ் (குடியரசுத் தலைவர் முன் அனுமதி உட்பட) பாதுகாக்கப்படாவிட்டால், உறுப்பு 301-ஐ மீறுவதாக பெரும்பான்மை அமர்வு தீர்ப்பளித்தது.",
        "Option A precisely articulates the 'direct and immediate impediment' test laid down in Atiabari.", "விருப்பம் A அதியபாரி வழக்கில் உருவாக்கப்பட்ட 'நேரடி மற்றும் உடனடித் தடை' சோதனையைத் துல்லியமாக விளக்குகிறது.",
        "Taxes per se are not unconstitutional; only those directly impeding movement violate Art 301.", "வரிகள் இயல்பாகவே அரசியலமைப்பு முரணானவை அல்ல; இயக்கத்தை நேரடியாகத் தடுப்பவை மட்டுமே 301-ஐ மீறுகின்றன.",
        "Customs duties at international borders fall under Entry 83 (Union List), outside Part XIII domestic trade.", "சர்வதேச சுங்க வரிகள் மத்தியப் பட்டியல் பதிவு 83-ன் கீழ் வருகின்றன.",
        "Article 301 operates during ordinary peacetime, not restricted to financial emergency.", "உறுப்பு 301 சாதாரண அமைதிக் காலத்தில் இயங்குகிறது, நிதி நெருக்கடிக்கு மட்டுப்படுத்தப்பட்டதல்ல.",
        "Atiabari Doctrine (1961): Direct and immediate restriction on the movement of goods violates Article 301.",
        "அதியபாரி கோட்பாடு (1961): பொருட்களின் இயக்கத்தின் மீதான நேரடி மற்றும் உடனடித் தடை உறுப்பு 301-ஐ மீறுகிறது.",
        "Atiabari test: Direct and immediate impediment to trade violates Article 301.",
        "அதியபாரி தேர்வு: வர்த்தகத்திற்கு நேரடி மற்றும் உடனடித் தடையாக இருப்பது உறுப்பு 301 ஐ மீறுகிறது.",
        tags=["Atiabari Tea Co.", "Article 301", "Direct and Immediate Test"]
    ))

    # 002 - Ans B
    q.append(make_q(
        "ISR_H_002", "Judicial Doctrine Evolution",
        "In Automobile Transport (Rajasthan) Ltd. v. State of Rajasthan (1962), how did the 7-judge bench modify the Atiabari doctrine regarding the validity of State taxation under Article 301?",
        "ஆட்டோமொபைல் டிரான்ஸ்போர்ட் (ராஜஸ்தான்) லிமிடெட் vs ராஜஸ்தான் மாநிலம் (1962) வழக்கில், 7 நீதிபதிகள் கொண்ட அமர்வு உறுப்பு 301-ன் கீழான மாநில வரிவிதிப்பின் செல்லுபடியாகும் தன்மை குறித்து அதியபாரி கோட்பாட்டை எவ்வாறு மாற்றியமைத்தது?",
        "It completely prohibited States from levying road taxes on motor vehicles.", "மோட்டார் வாகனங்கள் மீது சாலை வரி விதிப்பதை மாநிலங்களுக்கு முற்றிலும் தடை செய்தது.",
        "It formulated the 'Compensatory Tax Doctrine', holding that regulatory measures or compensatory taxes levied for providing facilities (like roads and bridges) do not infringe Article 301.", "இது 'ஈட்டு வரிக் கோட்பாட்டை' (Compensatory Tax Doctrine) உருவாக்கியது; வசதிகளை (சாலைகள், பாலங்கள்) வழங்குவதற்காக விதிக்கப்படும் ஒழுங்குமுறை நடவடிக்கைகள் அல்லது ஈட்டு வரிகள் உறுப்பு 301-ஐ மீறாது என்று தீர்ப்பளித்தது.",
        "It held that only Parliament has the legislative competence to levy any transportation tax.", "எந்தவொரு போக்குவரத்து வரியையும் விதிக்க நாடாளுமன்றத்திற்கு மட்டுமே சட்டமன்ற அதிகாரம் உள்ளது என்று கூறியது.",
        "It declared that all inter-State vehicular taxes must receive prior approval from the Zonal Councils.", "அனைத்து மாநிலங்களுக்கு இடையிலான வாகன வரிகளும் மண்டலக் குழுக்களின் முன் ஒப்புதலைப் பெற வேண்டும் என்று அறிவித்தது.",
        "B",
        "In Automobile Transport (1962), a 7-judge Constitution Bench introduced the 'Compensatory Tax Doctrine': taxes which are compensatory in character (i.e., levied as a recompense for facilities provided, such as road maintenance) or purely regulatory do not constitute an impediment under Article 301 and therefore do not need to satisfy the requirements of Article 304(b).",
        "ஆட்டோமொபைல் டிரான்ஸ்போர்ட் (1962) வழக்கில், 7 நீதிபதிகள் கொண்ட அரசியலமைப்பு அமர்வு 'ஈட்டு வரிக் கோட்பாட்டை' அறிமுகப்படுத்தியது: வர்த்தக வசதிகளுக்கு (சாலைப் பராமரிப்பு போன்றவை) ஈடாக விதிக்கப்படும் அல்லது ஒழுங்குமுறை சார்ந்த வரிகள் உறுப்பு 301-ன் கீழ் தடையாகக் கருதப்படாது; எனவே அவை உறுப்பு 304(b)-ன் நிபந்தனைகளை நிறைவு செய்ய வேண்டிய அவசியமில்லை என்று கூறியது.",
        "State motor vehicle road taxes were upheld as compensatory, not prohibited.", "மாநில மோட்டார் வாகன சாலை வரிகள் ஈட்டு வரிகளாக உறுதி செய்யப்பட்டன, தடை செய்யப்படவில்லை.",
        "Option B correctly describes the formulation of the compensatory tax theory in Automobile Transport (1962).", "விருப்பம் B ஆட்டோமொபைல் டிரான்ஸ்போர்ட் (1962) வழக்கில் ஈட்டு வரிக் கோட்பாடு உருவாக்கப்பட்டதைச் சரியாக விவரிக்கிறது.",
        "States possess independent taxing power under Entry 57 (vehicles) and Entry 56 (goods and passengers) of List II.", "பட்டியல் II-ன் பதிவு 57 மற்றும் 56-ன் கீழ் மாநிலங்களுக்கு சுயாதீன வரி அதிகாரங்கள் உள்ளன.",
        "Zonal Councils have no taxation approval powers.", "மண்டலக் குழுக்களுக்கு வரி ஒப்புதல் அதிகாரங்கள் இல்லை.",
        "Automobile Transport (1962): Compensatory and regulatory taxes for trading facilities do not violate Article 301.",
        "ஆட்டோமொபைல் டிரான்ஸ்போர்ட் (1962): வர்த்தக வசதிகளுக்கான ஈட்டு மற்றும் ஒழுங்குமுறை வரிகள் உறுப்பு 301-ஐ மீறாது.",
        "Automobile Transport (1962) introduced the Compensatory Tax Doctrine.",
        "ஆட்டோமொபைல் டிரான்ஸ்போர்ட் (1962) ஈட்டு வரிக் கோட்பாட்டை அறிமுகப்படுத்தியது.",
        tags=["Automobile Transport", "Compensatory Tax", "Article 301"]
    ))

    # 003 - Ans C
    q.append(make_q(
        "ISR_H_003", "Overruling Jurisprudence",
        "What was the historic constitutional holding of the 9-judge Constitution Bench of the Supreme Court in Jindal Stainless Ltd. v. State of Haryana (2016) regarding freedom of trade under Part XIII?",
        "பகுதி XIII-ன் கீழான வர்த்தக சுதந்திரம் தொடர்பாக ஜின்டால் ஸ்டெயின்லெஸ் லிமிடெட் vs ஹரியானா மாநிலம் (2016) வழக்கில் உச்ச நீதிமன்றத்தின் 9 நீதிபதிகள் கொண்ட அரசியலமைப்பு அமர்வின் வரலாற்றுச் சிறப்புமிக்க தீர்ப்பு என்ன?",
        "States have no power to levy entry tax on goods entering from other States under any entry in List II.", "பட்டியல் II-ல் உள்ள எந்தவொரு பதிவின் கீழும் பிற மாநிலங்களிலிருந்து நுழையும் பொருட்களின் மீது நுழைவு வரி விதிக்க மாநிலங்களுக்கு அதிகாரம் இல்லை.",
        "The President alone can determine whether a State tax is compensatory or non-compensatory.", "ஒரு மாநில வரி ஈட்டு வரியா அல்லது ஈடு செய்யாத வரியா என்பதை குடியரசுத் தலைவர் மட்டுமே தீர்மானிக்க முடியும்.",
        "The Compensatory Tax Doctrine formulated in Automobile Transport was expressly overruled; taxes under Article 304(a) are valid as long as they are non-discriminatory, without having to prove compensatory benefit.", "ஆட்டோமொபைல் டிரான்ஸ்போர்ட் வழக்கில் உருவாக்கப்பட்ட ஈட்டு வரிக் கோட்பாடு வெளிப்படையாக ரத்து செய்யப்பட்டது; உறுப்பு 304(a)-ன் கீழான வரிகள் பாகுபாடற்றவையாக இருக்கும் வரை செல்லுபடியாகும், அதற்கு ஈட்டு நன்மையை நிரூபிக்க வேண்டியதில்லை.",
        "Goods and Services Tax was declared void for violating the basic federal structure of Article 301.", "உறுப்பு 301-ன் அடிப்படைக் கூட்டாட்சிக் கட்டமைப்பை மீறியதற்காக சரக்கு மற்றும் சேவை வரி செல்லாது என அறிவிக்கப்பட்டது.",
        "C",
        "In Jindal Stainless (2016, 9-judge bench), the Supreme Court formally OVERRULED the concept of compensatory tax developed in Automobile Transport. The Court held that taxes are levies for general public revenue and cannot be tested on a compensatory basis. As long as a State entry tax under Article 304(a) treats local goods and imported goods uniformly without discrimination, it does not infringe Article 301.",
        "ஜின்டால் ஸ்டெயின்லெஸ் (2016, 9 நீதிபதிகள் அமர்வு) வழக்கில், ஆட்டோமொபைல் டிரான்ஸ்போர்ட் வழக்கில் உருவாக்கப்பட்ட 'ஈட்டு வரிக் கோட்பாட்டை' உச்ச நீதிமன்றம் வெளிப்படையாக ரத்து செய்தது. வரிகள் பொது வருவாய்க்கானவை, அவற்றை ஈட்டு அடிப்படையில் சோதிக்க முடியாது என்று நீதிமன்றம் கூறியது. உறுப்பு 304(a)-ன் கீழான ஒரு மாநில நுழைவு வரி உள்ளூர் மற்றும் இறக்குமதி பொருட்களைப் பாகுபாடின்றி ஒரே மாதிரியாக நடத்தும் வரை, அது உறுப்பு 301-ஐ மீறாது.",
        "State entry taxes were upheld subject to non-discrimination, not struck down wholesale.", "மாநில நுழைவு வரிகள் பாகுபாடின்மை நிபந்தனைக்கு உட்பட்டு உறுதி செய்யப்பட்டன.",
        "The President does not categorize taxes under Jindal Stainless.", "குடியரசுத் தலைவர் வரிகளை வகைப்படுத்துவதில்லை.",
        "Option C precisely captures the 9-judge bench overruling of the compensatory tax doctrine.", "விருப்பம் C 9 நீதிபதிகள் அமர்வு ஈட்டு வரிக் கோட்பாட்டை ரத்து செய்ததை மிகத் துல்லியமாக விவரிக்கிறது.",
        "GST was not declared void; Jindal Stainless resolved entry tax disputes under pre-GST and post-GST constitutional balance.", "ஜிஎஸ்டி செல்லாது என அறிவிக்கப்படவில்லை.",
        "Jindal Stainless (2016, 9-judge bench): Overruled the Compensatory Tax Theory; affirmed that non-discriminatory tax under Art 304(a) is valid per se.",
        "ஜின்டால் ஸ்டெயின்லெஸ் (2016, 9 நீதிபதிகள்): ஈட்டு வரிக் கோட்பாட்டை ரத்து செய்தது; உறுப்பு 304(a)-ன் கீழான பாகுபாடற்ற வரி செல்லுபடியாகும் என உறுதிப்படுத்தியது.",
        "Jindal Stainless (2016) overruled the Compensatory Tax Doctrine.",
        "ஜின்டால் ஸ்டெயின்லெஸ் (2016) ஈட்டு வரிக் கோட்பாட்டை ரத்து செய்தது.",
        tags=["Jindal Stainless 2016", "9-Judge Bench", "Overruled Compensatory Tax"]
    ))

    # 004 - Ans D
    q.append(make_q(
        "ISR_H_004", "Assertion-Reason",
        "Given below are two statements, one labelled as Assertion (A) and the other as Reason (R):\nAssertion (A): A State Legislature can enact a law under Article 304(a) imposing a tax on goods imported from other States without obtaining the previous sanction of the President.\nReason (R): Article 304(a) is governed by the principle of non-discrimination and does not contain a proviso requiring the previous sanction of the President, which is attached solely to Article 304(b).\nSelect the correct answer using the codes given below:",
        "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று உறுதிமொழி (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nஉறுதிமொழி (A): குடியரசுத் தலைவரின் முன் அனுமதியைப் பெறாமல், பிற மாநிலங்களிலிருந்து இறக்குமதி செய்யப்படும் பொருட்கள் மீது வரி விதிக்கும் சட்டத்தை உறுப்பு 304(a)-ன் கீழ் ஒரு மாநில சட்டமன்றம் இயற்ற முடியும்.\nகாரணம் (R): உறுப்பு 304(a) பாகுபாடின்மைக் கொள்கையால் நிர்வகிக்கப்படுகிறது மற்றும் குடியரசுத் தலைவரின் முன் அனுமதியைக் கோரும் நிபந்தனையைக் கொண்டிருக்கவில்லை; அந்த நிபந்தனை உறுப்பு 304(b)-க்கு மட்டுமே இணைக்கப்பட்டுள்ளது.\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-க்கான சரியான விளக்கம் அல்ல.",
        "(A) is true, but (R) is false.", "(A) உண்மை, ஆனால் (R) தவறு.",
        "(A) is false, but (R) is true.", "(A) தவறு, ஆனால் (R) உண்மை.",
        "Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மேலும் (R) என்பது (A)-க்கான சரியான விளக்கமாகும்.",
        "D",
        "Assertion (A) is true: Article 304(a) empowers a State to levy non-discriminatory taxes on imported goods, and this power does NOT require previous Presidential sanction. Reason (R) is also true and correctly explains (A): the mandatory proviso requiring previous sanction of the President applies exclusively to Article 304(b) (regulatory reasonable restrictions), not to Article 304(a) (taxation).",
        "உறுதிமொழி (A) உண்மை: உறுப்பு 304(a) இறக்குமதி பொருட்கள் மீது பாகுபாடற்ற வரிகளை விதிக்க மாநிலத்திற்கு அதிகாரமளிக்கிறது, இதற்கு குடியரசுத் தலைவரின் முன் அனுமதி தேவையில்லை. காரணம் (R) உண்மை மற்றும் (A)-வைச் சரியாக விளக்குகிறது: குடியரசுத் தலைவரின் முன் அனுமதியைக் கோரும் கட்டாய நிபந்தனை உறுப்பு 304(b)-க்கு மட்டுமே பொருந்தும், உறுப்பு 304(a)-க்கு அல்ல.",
        "Reason (R) is directly the logical basis of Assertion (A).", "காரணம் (R) நேரடியாக உறுதிமொழி (A)-க்கான தர்க்கரீதியான அடிப்படையாகும்.",
        "Reason (R) is entirely true.", "காரணம் (R) முற்றிலும் உண்மை.",
        "Assertion (A) is completely true under constitutional text.", "உறுதிமொழி (A) அரசியலமைப்பு உரையின்படி முற்றிலும் உண்மை.",
        "Option D correctly confirms both statements are true and (R) explains (A).", "விருப்பம் D இரண்டும் உண்மை மற்றும் (R) என்பது (A)-க்கான சரியான விளக்கம் என்பதை உறுதிப்படுத்துகிறது.",
        "Crucial Constitutional Structure: Proviso requiring prior presidential sanction applies ONLY to Article 304(b), NOT Article 304(a).",
        "முக்கிய அரசியலமைப்புக் கட்டமைப்பு: முன் அனுமதியைக் கோரும் நிபந்தனை உறுப்பு 304(b)-க்கு மட்டுமே பொருந்தும், உறுப்பு 304(a)-க்கு அல்ல.",
        "Article 304(a) requires no prior presidential sanction, unlike 304(b).",
        "உறுப்பு 304(b) போலன்றி, உறுப்பு 304(a)-க்கு குடியரசுத் தலைவர் முன் அனுமதி தேவையில்லை.",
        tags=["Assertion-Reason", "Article 304(a)", "Article 304(b)"]
    ))

    # 005 - Ans A
    q.append(make_q(
        "ISR_H_005", "Constitutional Mechanics",
        "Under Article 255(c) of the Constitution, what is the precise legal effect when the President gives assent to an Act of a State Legislature that was originally introduced without the 'previous sanction' required under the proviso to Article 304(b)?",
        "அரசியலமைப்பு உறுப்பு 255(c)-ன் கீழ், உறுப்பு 304(b)-ன் நிபந்தனையின் கீழ் தேவைப்படும் 'முன் அனுமதி' இன்றி முதலில் அறிமுகப்படுத்தப்பட்ட ஒரு மாநிலச் சட்டமன்றச் சட்டத்திற்கு குடியரசுத் தலைவர் ஒப்புதல் அளிக்கும் போது ஏற்படும் துல்லியமான சட்ட விளைவு என்ன?",
        "The lack of previous sanction is fully cured and the Act is treated as validly enacted from the date of Presidential assent.", "முன் அனுமதி இல்லாத குறைபாடு முழுமையாகச் சரிசெய்யப்பட்டு, குடியரசுத் தலைவர் ஒப்புதல் அளித்த தேதியிலிருந்து அச்சட்டம் செல்லுபடியாக இயற்றப்பட்டதாகக் கருதப்படுகிறது.",
        "The Act remains unconstitutional and can be struck down because procedural constitutional requirements are mandatory and non-curable.", "அரசியலமைப்பு நடைமுறைத் தேவைகள் கட்டாயமானவை மற்றும் சரிசெய்ய முடியாதவை என்பதால், அச்சட்டம் அரசியலமைப்பிற்கு முரணானதாகவே நீடித்து ரத்து செய்யப்படலாம்.",
        "The Act is valid for a maximum period of six months only, after which a re-enactment is required.", "அச்சட்டம் அதிகபட்சம் ஆறு மாத காலத்திற்கு மட்டுமே செல்லும், அதன் பிறகு மறுசீரமைப்பு தேவைப்படுகிறது.",
        "The Act requires additional ratification by a majority of the Zonal Council members to become enforceable.", "அச்சட்டம் அமலாக்கப்பட மண்டலக் குழு உறுப்பினர்களின் பெரும்பான்மையினரின் கூடுதல் ஏற்பு தேவைப்படுகிறது.",
        "A",
        "Article 255 explicitly states that no Act of Parliament or of a State Legislature shall be invalid merely by reason that some recommendation or previous sanction was not given, if assent to that Act was given by the President (where previous sanction of the President was required). Subsequent Presidential assent retroactively cures the procedural defect of omitting previous sanction under Art 304(b).",
        "உறுப்பு 255 தெளிவாகக் கூறுகிறது: குடியரசுத் தலைவரின் முன் அனுமதி தேவைப்படும் இடங்களில், அச்சட்டத்திற்குப் பின்னர் குடியரசுத் தலைவரால் ஒப்புதல் அளிக்கப்பட்டிருந்தால், முன் அனுமதி பெறப்படவில்லை என்ற காரணத்திற்காக எந்தவொரு நாடாளுமன்ற அல்லது மாநிலச் சட்டம் செல்லாததாகாது. பிந்தைய குடியரசுத் தலைவர் ஒப்புதல் 304(b)-ன் கீழான முன் அனுமதி பெறாத நடைமுறைக் குறையை முழுமையாகச் சரிசெய்கிறது.",
        "Option A precisely reflects the constitutional curing operation of Article 255.", "விருப்பம் A உறுப்பு 255-ன் அரசியலமைப்புத் தீர்வுப் பணியைத் துல்லியமாகப் பிரதிபலிக்கிறது.",
        "The defect is explicitly curable by the plain text of Article 255.", "உறுப்பு 255-ன் நேரடி உரையின் மூலம் இக்குறைபாடு வெளிப்படையாகச் சரிசெய்யப்படக் கூடியதாகும்.",
        "No six-month limitation exists in Article 255.", "உறுப்பு 255-ல் ஆறு மாத வரம்பு எதுவும் இல்லை.",
        "Zonal Council ratification is completely foreign to Article 255.", "மண்டலக் குழுவின் ஏற்பு உறுப்பு 255-க்கு முற்றிலும் தொடர்பற்றது.",
        "Article 255 cures the procedural defect of lack of previous sanction under Art 304(b) once the President accords subsequent assent.",
        "குடியரசுத் தலைவர் பிந்தைய ஒப்புதலை வழங்கியவுடன், உறுப்பு 255 ஆனது 304(b)-ன் கீழான முன் அனுமதி குறைபாட்டைச் சரிசெய்கிறது.",
        "Article 255 cures lack of prior sanction under Art 304(b).",
        "உறுப்பு 255 ஆனது உறுப்பு 304(b)-ன் கீழான முன் அனுமதி இல்லாமையைச் சரிசெய்கிறது.",
        tags=["Article 255", "Article 304(b)", "Curing Effect"]
    ))

    # 006 - Ans B
    q.append(make_q(
        "ISR_H_006", "Scenario Analysis",
        "Due to severe drought, State X experiences an acute shortage of food grains. To protect its local population, the Legislature of State X passes an Act prohibiting the export and transport of food grains from State X to neighboring State Y. Is this law constitutionally valid?",
        "கடும் வறட்சி காரணமாக, மாநிலம் X கடுமையான உணவு தானியப் பற்றாக்குறையை எதிர்கொள்கிறது. தனது உள்ளூர் மக்களைப் பாதுகாக்க, மாநிலம் X-ன் சட்டமன்றம் அண்டை மாநிலமான Y-க்கு உணவு தானியங்களை ஏற்றுமதி செய்வதையும் கொண்டு செல்வதையும் தடை செய்யும் ஒரு சட்டத்தை இயற்றுகிறது. இந்தச் சட்டம் அரசியலமைப்பு ரீதியாகச் செல்லுபடியாகுமா?",
        "Yes, because under Article 303(2), any State Legislature can pass discriminatory laws to deal with a scarcity of goods.", "ஆம், ஏனெனில் உறுப்பு 303(2)-ன் கீழ், எந்தவொரு மாநில சட்டமன்றமும் பொருட்களின் பற்றாக்குறையைக் கையாள பாகுபாடான சட்டங்களை இயற்ற முடியும்.",
        "No, because the scarcity exception under Article 303(2) is available EXCLUSIVELY to Parliament; State Legislatures have no power to create discriminatory inter-State trade barriers even during scarcity.", "இல்லை, ஏனெனில் உறுப்பு 303(2)-ன் கீழான பற்றாக்குறை விதிவிலக்கு நாடாளுமன்றத்திற்கு மட்டுமே பிரத்யேகமாகக் கிடைக்கிறது; பற்றாக்குறையின் போது கூட மாநில சட்டமன்றங்களுக்கு பாகுபாடான மாநில வர்த்தகத் தடைகளை உருவாக்க அதிகாரம் இல்லை.",
        "Yes, provided the Governor of State X issued an Ordinance declaring a severe regional calamity.", "ஆம், மாநிலம் X-ன் ஆளுநர் கடுமையான பிராந்தியப் பேரழிவைப் பிரகடனம் செய்து அவசரச் சட்டம் பிறப்பித்திருந்தால் செல்லும்.",
        "Yes, because fundamental rights are suspended automatically whenever food shortages occur.", "ஆம், உணவுப் பற்றாக்குறை ஏற்படும் போதெல்லாம் அடிப்படை உரிமைகள் தானாகவே இடைநிறுத்தப்படுவதால் செல்லும்.",
        "B",
        "Article 303(1) prohibits both Parliament and State Legislatures from discriminating between States. Article 303(2) carves out an exception for dealing with scarcity of goods, but this power is conferred SOLELY on PARLIAMENT ('nothing in clause (1) shall prevent Parliament from making any law...'). A State Legislature has NO constitutional authority under Article 303(2) to ban exports to other States on the grounds of scarcity.",
        "உறுப்பு 303(1) மாநிலங்களுக்கிடையே பாகுபாடு காட்டுவதை நாடாளுமன்றத்திற்கும் மாநில சட்டமன்றங்களுக்கும் தடை செய்கிறது. உறுப்பு 303(2) பொருட்களின் பற்றாக்குறையைக் கையாள்வதற்கான விதிவிலக்கை வழங்குகிறது, ஆனால் இந்த அதிகாரம் 'நாடாளுமன்றத்திற்கு மட்டுமே' (solely to Parliament) வழங்கப்பட்டுள்ளது. பற்றாக்குறையைக் காரணம் காட்டி பிற மாநிலங்களுக்கான ஏற்றுமதியைத் தடை செய்ய மாநில சட்டமன்றத்திற்கு உறுப்பு 303(2)-ன் கீழ் எந்த அரசியலமைப்பு அதிகாரமும் இல்லை.",
        "State Legislatures CANNOT invoke Article 303(2); it is an exclusive Parliamentary power.", "மாநில சட்டமன்றங்கள் உறுப்பு 303(2)-ஐப் பயன்படுத்த முடியாது; அது பிரத்யேக நாடாளுமன்ற அதிகாரம்.",
        "Option B correctly identifies that the scarcity exception belongs exclusively to Parliament.", "விருப்பம் B பற்றாக்குறை விதிவிலக்கு நாடாளுமன்றத்திற்கு மட்டுமே உரியது என்பதைச் சரியாகக் குறிப்பிடுகிறது.",
        "A Governor's Ordinance cannot expand State legislative competence beyond constitutional limits.", "ஆளுநரின் அவசரச் சட்டம் மாநில அதிகார வரம்பை அரசியலமைப்பு வரம்புகளுக்கு அப்பால் விரிவுபடுத்த முடியாது.",
        "Fundamental rights are never suspended due to food shortages.", "உணவுப் பற்றாக்குறையால் அடிப்படை உரிமைகள் ஒருபோதும் இடைநிறுத்தப்படுவதில்லை.",
        "Crucial TNPSC Trap: Article 303(2) scarcity exception belongs EXCLUSIVELY to Parliament. States cannot block exports to other states.",
        "முக்கியமான TNPSC பொறி: உறுப்பு 303(2) பற்றாக்குறை விதிவிலக்கு நாடாளுமன்றத்திற்கு மட்டுமே உரியது. பிற மாநிலங்களுக்கான ஏற்றுமதியை மாநிலங்கள் தடுக்க முடியாது.",
        "Scarcity exception under Art 303(2) is available exclusively to Parliament, not States.",
        "உறுப்பு 303(2)-ன் கீழான பற்றாக்குறை விதிவிலக்கு நாடாளுமன்றத்திற்கு மட்டுமே உரியது, மாநிலங்களுக்கு அல்ல.",
        tags=["Article 303(2)", "Scarcity Exception", "Scenario"]
    ))

    # 007 - Ans C
    q.append(make_q(
        "ISR_H_007", "Constitutional Synthesis",
        "Consider the following statements regarding the legal status of an award of an Inter-State Water Disputes Tribunal:\n1. Once published in the Official Gazette by the Central Government, the award acquires the same force as an order or decree of the Supreme Court under Section 6(2) of the IRWD Act.\n2. Notwithstanding the bar in Section 11 of the IRWD Act, the Supreme Court has held that an appeal against the tribunal's decision is maintainable under Article 136 of the Constitution.\n3. A State Legislature can pass an Act to modify or nullify the award within its own territorial jurisdiction.\nWhich of the statements given above are correct?",
        "மாநிலங்களுக்கு இடையிலான நதிநீர் தகராறுகள் தீர்ப்பாயத்தின் தீர்ப்பின் சட்ட நிலை தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. மத்திய அரசால் அதிகாரப்பூர்வ அரசிதழில் வெளியிடப்பட்டவுடன், அத்தீர்ப்பு IRWD சட்டத்தின் பிரிவு 6(2)-ன் கீழ் உச்ச நீதிமன்றத்தின் ஆணை அல்லது தீர்ப்பாணைக்கு இணையான அதே ஆற்றலைப் பெறுகிறது.\n2. IRWD சட்டத்தின் பிரிவு 11-ல் தடை உள்ளபோதிலும், அரசியலமைப்பின் உறுப்பு 136-ன் கீழ் தீர்ப்பாயத்தின் முடிவுக்கு எதிரான மேல்முறையீடு செல்லும் என்று உச்ச நீதிமன்றம் தீர்ப்பளித்துள்ளது.\n3. ஒரு மாநில சட்டமன்றம் தனது சொந்த எல்லைக்குள் அத்தீர்ப்பை மாற்றியமைக்கவோ அல்லது ரத்து செய்யவோ ஒரு சட்டத்தை இயற்ற முடியும்.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?",
        "1 and 3 only", "1 மற்றும் 3 மட்டும்",
        "2 and 3 only", "2 மற்றும் 3 மட்டும்",
        "1 and 2 only", "1 மற்றும் 2 மட்டும்",
        "1, 2, and 3", "1, 2 மற்றும் 3",
        "C",
        "Statements 1 and 2 are correct: (1) Under Section 6(2) of the IRWD Act (2002 amendment), a gazetted award has the force of a Supreme Court decree; (2) In State of Karnataka v. State of Tamil Nadu (2018), the Supreme Court held that Article 136 appeals against tribunal awards are maintainable as part of the basic structure. Statement 3 is incorrect: As established in Re Cauvery Water Disputes Tribunal (1991), a State cannot legislate to nullify or modify an inter-state tribunal award.",
        "கூற்றுகள் 1 மற்றும் 2 சரியானவை: (1) IRWD சட்டத்தின் பிரிவு 6(2)-ன் கீழ் (2002 திருத்தம்), அரசிதழில் வெளியிடப்பட்ட தீர்ப்பு உச்ச நீதிமன்றத் தீர்ப்பாணையின் ஆற்றலைப் பெறுகிறது; (2) கர்நாடகா vs தமிழ்நாடு (2018) வழக்கில், உறுப்பு 136-ன் கீழான மேல்முறையீடு செல்லும் என உச்ச நீதிமன்றம் தீர்ப்பளித்தது. கூற்று 3 தவறானது: காவிரி விவகாரத்தில் (1991) நிறுவப்பட்டபடி, ஒரு மாநில நதிநீர் தீர்ப்பாயத் தீர்ப்பை ரத்து செய்யவோ மாற்றவோ எந்த மாநிலமும் சட்டம் இயற்ற முடியாது.",
        "Statement 3 is unconstitutional, making option A incorrect.", "கூற்று 3 அரசியலமைப்பிற்கு முரணானது என்பதால் விருப்பம் A தவறானது.",
        "Statement 3 is unconstitutional, making option B incorrect.", "கூற்று 3 தவறானது என்பதால் விருப்பம் B தவறானது.",
        "Statements 1 and 2 are both constitutionally sound and supported by statute and precedent.", "கூற்றுகள் 1 மற்றும் 2 இரண்டும் சட்டம் மற்றும் முன்மாதிரிகளால் ஆதரிக்கப்பட்ட சரியான கூற்றுகள் ஆகும்.",
        "Statement 3 is false, so all three cannot be correct.", "கூற்று 3 தவறு என்பதால் அனைத்தும் சரியாக இருக்க முடியாது.",
        "A State cannot legislate away an inter-State river water tribunal award; the award equals a Supreme Court decree and is subject only to Art 136 review.",
        "ஒரு மாநில நதிநீர் தீர்ப்பாயத் தீர்ப்பை ஒரு மாநிலச் சட்டம் ரத்து செய்ய முடியாது; அத்தீர்ப்பு உச்ச நீதிமன்றத் தீர்ப்பாணைக்கு இணையானது மற்றும் உறுப்பு 136 மறுஆய்வுக்கு மட்டுமே உட்பட்டது.",
        "Gazetted tribunal award = SC decree; Art 136 review maintainable; States cannot nullify.",
        "அரசிதழ் தீர்ப்பு = உச்ச நீதிமன்றத் தீர்ப்பாணை; உறுப்பு 136 மறுஆய்வு செல்லும்; மாநிலங்கள் ரத்து செய்ய முடியாது.",
        tags=["Water Disputes", "Tribunal Award", "Cauvery Precedent"]
    ))

    # 008 - Ans D
    q.append(make_q(
        "ISR_H_008", "Multi-Statement",
        "Consider the following statements regarding the Zonal Councils established under the States Reorganisation Act, 1956:\n1. The Prime Minister of India serves as the common Chairman of all Zonal Councils.\n2. The Chief Ministers of member States act as Vice-Chairman by annual rotation for a period of one year.\n3. Advisors nominated by NITI Aayog and the Chief Secretaries of member States have the right to vote in all Council decisions.\n4. Zonal Councils are deliberative and advisory bodies with no statutory executive power to enforce their recommendations.\nWhich of the statements given above are correct?",
        "1956 ஆம் ஆண்டின் மாநில மறுசீரமைப்புச் சட்டத்தின் கீழ் அமைக்கப்பட்ட மண்டலக் குழுக்கள் தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இந்தியப் பிரதம அமைச்சர் அனைத்து மண்டலக் குழுக்களுக்கும் பொதுவான தலைவராகச் செயல்படுகிறார்.\n2. உறுப்பினர் மாநிலங்களின் முதலமைச்சர்கள் சுழற்சி முறையில் தலா ஒரு வருட காலத்திற்கு துணைத் தலைவராகச் செயல்படுகின்றனர்.\n3. நிதி ஆயோக்கால் பரிந்துரைக்கப்பட்ட ஆலோசகர்கள் மற்றும் உறுப்பினர் மாநிலங்களின் தலைமைச் செயலாளர்கள் அனைத்து மன்ற முடிவுகளிலும் வாக்களிக்கும் உரிமையைக் கொண்டுள்ளனர்.\n4. மண்டலக் குழுக்கள் என்பவை தங்கள் பரிந்துரைகளை அமல்படுத்த சட்டப்பூர்வ நிர்வாக அதிகாரம் இல்லாத ஆலோசனைக் குழுக்களாகும்.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?",
        "1 and 3 only", "1 மற்றும் 3 மட்டும்",
        "2 and 3 only", "2 மற்றும் 3 மட்டும்",
        "1, 2, and 4 only", "1, 2 மற்றும் 4 மட்டும்",
        "2 and 4 only", "2 மற்றும் 4 மட்டும்",
        "D",
        "Statement 1 is incorrect: The UNION HOME MINISTER, not the Prime Minister, is the Chairman of Zonal Councils. Statement 2 is correct: Chief Ministers rotate annually as Vice-Chairman. Statement 3 is incorrect: Advisors (NITI Aayog nominee, Chief Secretaries) have NO right to vote under Section 16(1). Statement 4 is correct: Zonal Councils are purely advisory bodies under Section 21 of the Act.",
        "கூற்று 1 தவறானது: மண்டலக் குழுக்களுக்கு பிரதமரல்ல, மத்திய உள்துறை அமைச்சரே தலைவராக உள்ளார். கூற்று 2 சரியானது: முதலமைச்சர்கள் ஆண்டுதோறும் சுழற்சி முறையில் துணைத் தலைவராகப் பணியாற்றுகின்றனர். கூற்று 3 தவறானது: பிரிவு 16(1)-ன் கீழ் ஆலோசகர்களுக்கு (நிதி ஆயோக், தலைமைச் செயலாளர்கள்) வாக்களிக்கும் உரிமை இல்லை. கூற்று 4 சரியானது: மண்டலக் குழுக்கள் பிரிவு 21-ன் கீழ் முற்றிலும் ஆலோசனை அமைப்புகளாகும்.",
        "Statements 1 and 3 are both false.", "கூற்றுகள் 1 மற்றும் 3 இரண்டும் தவறானவை.",
        "Statement 3 is false because advisors have no voting rights.", "ஆலோசகர்களுக்கு வாக்குரிமை இல்லாததால் கூற்று 3 தவறானது.",
        "Statement 1 is false because the Home Minister chairs the Councils.", "உள்துறை அமைச்சர் தலைமை தாங்குவதால் கூற்று 1 தவறானது.",
        "Statements 2 and 4 are strictly accurate under the States Reorganisation Act 1956.", "கூற்றுகள் 2 மற்றும் 4 ஆகியவை 1956 மாநில மறுசீரமைப்புச் சட்டத்தின் கீழ் துல்லியமாகச் சரியானவை.",
        "Zonal Councils: Chaired by Home Minister; CMs rotate as Vice-Chairman (1 yr); Advisors have NO vote; purely advisory mandate.",
        "மண்டலக் குழுக்கள்: உள்துறை அமைச்சர் தலைமை; முதலமைச்சர்கள் துணைத் தலைவர் (1 ஆண்டு); ஆலோசகர்களுக்கு வாக்குரிமை இல்லை; வெறும் ஆலோசனைப் பணி.",
        "Zonal Councils: Statements 2 and 4 are correct.",
        "மண்டலக் குழுக்கள்: கூற்றுகள் 2 மற்றும் 4 சரியானவை.",
        tags=["Zonal Councils", "Multi-Statement", "SRA 1956"]
    ))

    # 009 - Ans A
    q.append(make_q(
        "ISR_H_009", "Constitutional Distinction",
        "Which of the following statements accurately explains why the Constitution provides a specialized tribunal mechanism under Article 262 instead of leaving river water disputes to the Supreme Court under Article 131?",
        "நதிநீர் தகராறுகளை உறுப்பு 131-ன் கீழ் உச்ச நீதிமன்றத்திடம் விடுவதற்குப் பதிலாக, அரசியலமைப்பு உறுப்பு 262-ன் கீழ் ஒரு சிறப்புத் தீர்ப்பாய முறைமையை ஏன் வழங்குகிறது என்பதைப் பின்வரும் கூற்றுகளில் எது துல்லியமாக விளக்குகிறது?",
        "River water disputes involve complex agro-economic, engineering, and equitable apportionment considerations that are better suited for specialized adjudication assisted by technical assessors rather than strict adversarial legalism.", "நதிநீர் தகராறுகள் சிக்கலான வேளாண்-பொருளாதார, பொறியியல் மற்றும் சமத்துவப் பகிர்வு பரிசீலனைகளை உள்ளடக்கியுள்ளன; அவை கடுமையான முரண்பட்ட சட்டவாதத்தை விட, தொழில்நுட்ப மதிப்பீட்டாளர்களின் உதவியுடன் கூடிய சிறப்புத் தீர்ப்பிற்கு மிகவும் பொருத்தமானவை.",
        "The Supreme Court requested the Constituent Assembly to relieve it of all inter-governmental disputes.", "அரசாங்கங்களுக்கிடையேயான அனைத்துத் தகராறுகளிலிருந்தும் தனக்கு விலக்கு அளிக்குமாறு உச்ச நீதிமன்றம் அரசியலமைப்பு நிர்ணய சபையைக் கேட்டுக்கொண்டது.",
        "Under the Government of India Act 1935, water disputes were decided by the Privy Council, which abolished all court jurisdiction permanently.", "1935 இந்திய அரசுச் சட்டத்தின் கீழ், நதிநீர் தகராறுகள் பிரிவி கவுன்சிலால் தீர்மானிக்கப்பட்டன, அது அனைத்து நீதிமன்ற அதிகார வரம்பையும் நிரந்தரமாக ஒழித்தது.",
        "River waters belong exclusively to the Central Government under Entry 56, leaving courts with no locus standi.", "பதிவு 56-ன் கீழ் நதிநீர் மத்திய அரசிற்கு மட்டுமே சொந்தமானது, இதனால் நீதிமன்றங்களுக்கு எந்த அதிகாரமும் இல்லை.",
        "A",
        "The framers of the Constitution recognized that inter-State river water sharing is not merely an adversarial dispute over legal rights, but involves complex hydrological, ecological, engineering, and socio-economic equities. Under Article 262 and the IRWD Act, tribunals can co-opt technical assessors, examine river basin data, and apply international principles of equitable apportionment (e.g., Helsinki Rules) far more flexibly than a regular court of law.",
        "மாநிலங்களுக்கு இடையேயான நதிநீர் பகிர்வு என்பது வெறும் சட்ட உரிமைகள் மீதான முரண்பட்ட தகராறு மட்டுமல்ல, சிக்கலான நீரியல், சுற்றுச்சூழல், பொறியியல் மற்றும் சமூக-பொருளாதாரக் கூறுகளை உள்ளடக்கியது என்பதை அரசியலமைப்பை உருவாக்கியவர்கள் உணர்ந்தனர். உறுப்பு 262 மற்றும் IRWD சட்டத்தின் கீழ், தீர்ப்பாயங்கள் தொழில்நுட்ப மதிப்பீட்டாளர்களை இணைத்து, நதிப் படுகைத் தரவுகளை ஆய்வு செய்து, வழக்கமான நீதிமன்றத்தை விட மிகவும் நெகிழ்வாக சமத்துவப் பகிர்வு சர்வதேசக் கொள்கைகளை (ஹெல்சின்கி விதிகள் போன்றவை) பயன்படுத்த முடியும்.",
        "Option A precisely articulates the institutional rationale for Article 262 tribunals.", "விருப்பம் A உறுப்பு 262 தீர்ப்பாயங்களுக்கான நிறுவனக் காரணத்தை மிகத் துல்லியமாக விளக்குகிறது.",
        "The Supreme Court made no such request.", "உச்ச நீதிமன்றம் அத்தகைய கோரிக்கை எதையும் வைக்கவில்லை.",
        "Privy Council history did not permanently abolish court jurisdiction.", "பிரிவி கவுன்சில் நீதிமன்ற அதிகார வரம்பை நிரந்தரமாக ஒழிக்கவில்லை.",
        "River waters do not belong exclusively to the Centre; water is primarily Entry 17 in the State List.", "நதிநீர் மத்திய அரசிற்கு மட்டுமே சொந்தமானது அல்ல; நீர் முதன்மையாக மாநிலப் பட்டியலில் உள்ளது.",
        "Article 262 rationale: Technical and equitable apportionment of water is better resolved by specialized tribunals with expert assessors than ordinary courts.",
        "உறுப்பு 262 நோக்கம்: தொழில்நுட்ப மற்றும் சமத்துவ நீர் பகிர்வு என்பது சாதாரண நீதிமன்றங்களை விட நிபுணத்துவ மதிப்பீட்டாளர்களைக் கொண்ட சிறப்புத் தீர்ப்பாயங்களால் சிறப்பாகத் தீர்க்கப்படுகிறது.",
        "Article 262 rationale: Specialized adjudication of complex technical water disputes.",
        "உறுப்பு 262 நோக்கம்: சிக்கலான தொழில்நுட்ப நதிநீர் தகராறுகளின் சிறப்புத் தீர்ப்பு.",
        tags=["Article 262", "Constitutional Rationale", "Equitable Apportionment"]
    ))

    # 010 - Ans B
    q.append(make_q(
        "ISR_H_010", "Complex Scenario",
        "State A enacts a statute imposing an 'Environmental Cess' on the transportation of coal passing through its territory from State B to State C. The cess is levied strictly on coal in transit and no corresponding cess is levied on coal mined and consumed within State A. What is the constitutional validity of this cess under Part XIII?",
        "மாநிலம் B-யிலிருந்து மாநிலம் C-க்கு தனது பகுதி வழியாகச் செல்லும் நிலக்கரிப் போக்குவரத்தின் மீது மாநிலம் A 'சுற்றுச்சூழல் வரி' (Environmental Cess) விதிக்கும் ஒரு சட்டத்தை இயற்றுகிறது. இந்த வரி போக்குவரத்தில் உள்ள நிலக்கரி மீது மட்டுமே விதிக்கப்படுகிறது, மேலும் மாநிலம் A-க்குள் வெட்டப்பட்டு நுகரப்படும் நிலக்கரி மீது அத்தகைய வரி எதுவும் விதிக்கப்படவில்லை. பகுதி XIII-ன் கீழ் இந்த வரியின் அரசியலமைப்புச் செல்லுபடியாகும் தன்மை என்ன?",
        "The cess is valid because environmental protection under Article 48A overrides all provisions of Part XIII.", "உறுப்பு 48A-ன் கீழான சுற்றுச்சூழல் பாதுகாப்பு பகுதி XIII-ன் அனைத்து விதிகளையும் விஞ்சுவதால் இந்த வரி செல்லுபடியாகும்.",
        "The cess is unconstitutional as it directly and discriminatory impedes inter-State transit under Article 301, violating Article 304(a) by discriminating against transit goods vis-a-vis local goods without satisfying Article 304(b).", "உள்ளூர் பொருட்களுடன் ஒப்பிடும் போது போக்குவரத்துப் பொருட்கள் மீது பாகுபாடு காட்டி, உறுப்பு 304(b)-ஐ நிறைவு செய்யாமல் உறுப்பு 304(a)-ஐ மீறி, உறுப்பு 301-ன் கீழான மாநிலங்களுக்கு இடையிலான போக்குவரத்தை நேரடியாகவும் பாகுபாடாகவும் தடுப்பதால் இந்த வரி அரசியலமைப்பிற்கு முரணானது.",
        "The cess is valid provided the proceeds are shared equally with the Inter-State Council.", "வரி வருவாய் மாநிலங்களுக்கு இடையிலான மன்றத்துடன் சமமாகப் பகிர்ந்து கொள்ளப்பட்டால் இந்த வரி செல்லும்.",
        "The cess is valid because Article 301 applies only to agricultural commodities, not to minerals.", "உறுப்பு 301 விவசாயப் பொருட்களுக்கு மட்டுமே பொருந்தும், கனிமங்களுக்குப் பொருந்தாது என்பதால் இந்த வரி செல்லும்.",
        "B",
        "A transit fee or cess that singles out goods in inter-State transit while exempting locally mined and consumed coal is inherently discriminatory and violates Article 304(a). Furthermore, because it directly restricts the free flow of inter-State transit without meeting the non-discrimination requirement or obtaining presidential sanction under Article 304(b), it constitutes an unconstitutional barrier under Article 301 (as established in Atiabari and Jindal Stainless).",
        "உள்ளூரில் வெட்டி நுகரப்படும் நிலக்கரிக்கு விலக்கு அளித்து, மாநிலங்களுக்கு இடையிலான போக்குவரத்தில் உள்ள பொருட்களை மட்டுமே குறிவைக்கும் போக்குவரத்து வரி இயல்பாகவே பாகுபாடானது மற்றும் உறுப்பு 304(a)-ஐ மீறுகிறது. மேலும், இது பாகுபாடற்ற தேவையை நிறைவு செய்யாமலும், உறுப்பு 304(b)-ன் கீழ் குடியரசுத் தலைவர் அனுமதியைப் பெறாமலும் மாநிலங்களுக்கு இடையேயான வர்த்தகத்தின் தடையற்ற ஓட்டத்தை நேரடியாகத் தடுப்பதால், உறுப்பு 301-ன் கீழ் அரசியலமைப்பிற்கு முரணான தடையாகும்.",
        "Article 48A (Directive Principles) cannot authorize violation of constitutional guarantees without valid legislative competence and procedure.", "உறுப்பு 48A அரசியலமைப்பு உத்தரவாதங்களை மீற அனுமதிக்க முடியாது.",
        "Option B correctly identifies the discriminatory transit barrier violating both Article 301 and Article 304.", "விருப்பம் B உறுப்பு 301 மற்றும் 304 ஆகிய இரண்டையும் மீறும் பாகுபாடான வர்த்தகத் தடையைச் சரியாக விளக்குகிறது.",
        "Sharing proceeds with the Inter-State Council is legally irrelevant.", "வருவாயைப் பகிர்வது சட்டத்திற்குப் பொருத்தமற்றது.",
        "Article 301 applies to all trade, commerce, and merchandise, including coal and minerals.", "உறுப்பு 301 நிலக்கரி மற்றும் கனிமங்கள் உட்பட அனைத்து வர்த்தகப் பொருட்களுக்கும் பொருந்தும்.",
        "Discriminatory transit taxes that target cross-border movement while sparing local production violate Article 301 and Article 304(a).",
        "உள்ளூர் உற்பத்தியை விட்டுவிட்டு எல்லை கடந்த போக்குவரத்தைக் குறிவைக்கும் பாகுபாடான வரிகள் உறுப்பு 301 மற்றும் 304(a)-ஐ மீறுகின்றன.",
        "Discriminatory transit cess violates Articles 301 and 304(a).",
        "பாகுபாடான போக்குவரத்து வரி உறுப்புகள் 301 மற்றும் 304(a) ஐ மீறுகிறது.",
        tags=["Part XIII", "Transit Tax", "Discriminatory Barrier", "Scenario"]
    ))

    # 011 - Ans C
    q.append(make_q(
        "ISR_H_011", "Inter-State Agreements",
        "What was the historical constitutional significance of the 1892 and 1924 agreements between the Madras Presidency and the Princely State of Mysore in the Cauvery water dispute?",
        "காவிரி நதிநீர் தகராறில் மெட்ராஸ் மாகாணத்திற்கும் மைசூர் சமஸ்தானத்திற்கும் இடையே ஏற்பட்ட 1892 மற்றும் 1924 உடன்படிக்கைகளின் வரலாற்றுச் சிறப்புமிக்க அரசியலமைப்பு முக்கியத்துவம் என்ன?",
        "They were declared void ab initio by the Government of India Act 1935.", "அவை 1935 இந்திய அரசுச் சட்டத்தால் ஆரம்பத்திலிருந்தே செல்லாதவை என அறிவிக்கப்பட்டன.",
        "They applied only to maritime navigation, not to agricultural irrigation.", "அவை கடல்வழிப் போக்குவரத்திற்கு மட்டுமே பொருந்தின, விவசாயப் பாசனத்திற்கு அல்ல.",
        "They established recognized historical prescriptive water allocations and principles of prior appropriation between an upper riparian state (Mysore) and a lower riparian territory (Madras), which survived the adoption of the Constitution under Article 363 / pre-constitutional treaty jurisprudence until modified by the Tribunal and Supreme Court.", "அவை மேல்மட்ட மாநிலமான மைசூர் மற்றும் கீழ்மட்டப் பகுதியான மெட்ராஸ் ஆகியவற்றுக்கிடையே அங்கீகரிக்கப்பட்ட வரலாற்று நீர் ஒதுக்கீடுகளையும், முந்தைய பயன்பாட்டுக் கொள்கைகளையும் நிறுவின; அவை தீர்ப்பாயம் மற்றும் உச்ச நீதிமன்றத்தால் மாற்றியமைக்கப்படும் வரை அரசியலமைப்பு நடைமுறைக்கு வந்த பின்னரும் தொடர்ந்தன.",
        "They were bilateral commercial contracts governed by English private contract law, having no relevance to modern Indian federal water rights.", "அவை ஆங்கிலேயத் தனியார் ஒப்பந்தச் சட்டத்தால் நிர்வகிக்கப்படும் இருதரப்பு வணிக ஒப்பந்தங்கள், நவீன இந்தியக் கூட்டாட்சி நீர் உரிமைகளுக்குத் தொடர்பற்றவை.",
        "C",
        "The 1892 Rules and 1924 Agreement between Madras and Mysore formed the foundational framework of equitable sharing in the Cauvery basin. The Supreme Court in 2018 affirmed that these pre-constitutional agreements were valid and established prescriptive rights and basin allocation baselines that formed the legal context for adjudication under the IRWD Act, 1956.",
        "மெட்ராஸ் மற்றும் மைசூர் இடையேயான 1892 விதிகள் மற்றும் 1924 ஒப்பந்தம் ஆகியவை காவிரிப் படுகையில் சமத்துவப் பகிர்வின் அடிப்படை கட்டமைப்பை உருவாக்கின. 2018-ல் உச்ச நீதிமன்றம், இந்த அரசியலமைப்புக்கு முந்தைய உடன்படிக்கைகள் செல்லுபடியாகும் என்றும், அவை 1956 IRWD சட்டத்தின் கீழான தீர்ப்பிற்கு சட்டக் சூழலை அமைத்துக் கொடுத்தன என்றும் உறுதிப்படுத்தியது.",
        "They were not declared void by the 1935 Act; they continued in operation.", "அவை 1935 சட்டத்தால் ரத்து செய்யப்படவில்லை; தொடர்ந்து இயங்கின.",
        "They applied directly to irrigation storage (e.g., Krishnarajasagar dam) and irrigation flows.", "அவை பாசன சேமிப்பு மற்றும் பாசன நீரோட்டங்களுக்கு நேரடியாகப் பொருந்தின.",
        "Option C accurately captures their historical and constitutional role in defining riparian rights.", "விருப்பம் C நதிப் படுகை உரிமைகளை வரையறுப்பதில் அவற்றின் வரலாற்று மற்றும் அரசியலமைப்புப் பங்கைச் சரியாக விவரிக்கிறது.",
        "They were inter-governmental agreements between sovereign/provincial entities, not private commercial contracts.", "அவை அரசுகளுக்கிடையேயான உடன்படிக்கைகள், தனியார் வணிக ஒப்பந்தங்கள் அல்ல.",
        "The 1892 and 1924 Madras-Mysore Agreements recognized lower riparian prescriptive rights, forming the historical bedrock of the Cauvery dispute.",
        "1892 மற்றும் 1924 மெட்ராஸ்-மைசூர் உடன்படிக்கைகள் கீழ்மட்ட நதிப் படுகை உரிமைகளை அங்கீகரித்தன; இதுவே காவிரி தகராறின் வரலாற்று அடித்தளமாகும்.",
        "1892 and 1924 Cauvery agreements established foundational riparian rights.",
        "1892 மற்றும் 1924 காவிரி உடன்படிக்கைகள் அடிப்படை நதிப் படுகை உரிமைகளை நிறுவின.",
        tags=["Cauvery Dispute", "1892 Agreement", "1924 Agreement"]
    ))

    # 012 - Ans D
    q.append(make_q(
        "ISR_H_012", "Commission Comparison",
        "Comparing the recommendations of the First Administrative Reforms Commission (1966) and the Sarkaria Commission (1988) on Article 263, what was the crucial difference regarding the proposed composition of the Inter-State Council?",
        "உறுப்பு 263 குறித்த முதலாவது நிர்வாகச் சீர்திருத்த ஆணையம் (1966) மற்றும் சர்க்காரியா ஆணையம் (1988) ஆகியவற்றின் பரிந்துரைகளை ஒப்பிடுகையில், மாநிலங்களுக்கு இடையிலான மன்றத்தின் முன்மொழியப்பட்ட அமைப்பில் இருந்த முக்கிய வேறுபாடு என்ன?",
        "First ARC recommended that the Council be chaired by the President, whereas Sarkaria recommended the Chief Justice of India.", "முதல் ARC குடியரசுத் தலைவர் தலைமையில் மன்றம் அமைய வேண்டும் என்று பரிந்துரைத்தது, ஆனால் சர்க்காரியா இந்தியத் தலைமை நீதிபதியைப் பரிந்துரைத்தது.",
        "First ARC recommended a purely non-governmental council of civil society experts, whereas Sarkaria recommended an all-bureaucratic council.", "முதல் ARC குடிமைச் சமூக நிபுணர்களின் அரசு சாரா மன்றத்தைப் பரிந்துரைத்தது, ஆனால் சர்க்காரியா முழுக்க அதிகாரத்துவ மன்றத்தைப் பரிந்துரைத்தது.",
        "First ARC recommended excluding Chief Ministers, whereas Sarkaria recommended only Chief Ministers.", "முதல் ARC முதலமைச்சர்களை விலக்கப் பரிந்துரைத்தது, ஆனால் சர்க்காரியா முதலமைச்சர்களை மட்டுமே பரிந்துரைத்தது.",
        "First ARC proposed a compact council of the PM and five central ministers plus five Chief Ministers, whereas Sarkaria recommended an inclusive, representative council comprising the PM, all State Chief Ministers, UT heads, and six Union Cabinet Ministers.", "முதல் ARC பிரதமர், ஐந்து மத்திய அமைச்சர்கள் மற்றும் ஐந்து முதலமைச்சர்களைக் கொண்ட ஒரு சிறிய மன்றத்தை முன்மொழிந்தது; ஆனால் சர்க்காரியா பிரதமர், அனைத்து மாநில முதல்வர்கள், யூ.பி தலைவர்கள் மற்றும் ஆறு மத்திய அமைச்சர்களைக் கொண்ட அனைவரையும் உள்ளடக்கிய பிரதிநிதித்துவ மன்றத்தைப் பரிந்துரைத்தது.",
        "D",
        "The First ARC (1966) recommended a small, compact body consisting of the Prime Minister, Home Minister, Finance Minister, Leader of the Opposition in Lok Sabha, and five Chief Ministers representing Zonal Councils. The Sarkaria Commission (1988) rejected this limited representation and recommended a fully inclusive national forum comprising the Prime Minister as Chairman, Chief Ministers of ALL States and UTs with assemblies, administrators of other UTs, and six Union Cabinet Ministers.",
        "முதலாவது ARC (1966) பிரதமர், உள்துறை அமைச்சர், நிதி அமைச்சர், மக்களவை எதிர்க்கட்சித் தலைவர் மற்றும் மண்டலக் குழுக்களைப் பிரதிநிதித்துவப்படுத்தும் ஐந்து முதலமைச்சர்களைக் கொண்ட ஒரு சிறிய அமைப்பைப் பரிந்துரைத்தது. சர்க்காரியா ஆணையம் (1988) இந்த வரம்புக்குட்பட்ட பிரதிநிதித்துவத்தை நிராகரித்து, பிரதமர் தலைமையில் அனைத்து மாநில முதல்வர்கள், சட்டமன்றம் கொண்ட யூ.பி தலைவர்கள், பிற யூ.பி நிர்வாகிகள் மற்றும் ஆறு மத்திய அமைச்சர்களைக் கொண்ட அனைவரையும் உள்ளடக்கிய தேசிய மன்றத்தைப் பரிந்துரைத்தது.",
        "Neither commission recommended the CJI as chairman.", "எந்த ஆணையமும் தலைமை நீதிபதியைத் தலைவராகப் பரிந்துரைக்கவில்லை.",
        "Neither commission suggested a purely civil society or bureaucratic council.", "எந்த ஆணையமும் அரசு சாரா அல்லது அதிகாரத்துவ மன்றத்தைப் பரிந்துரைக்கவில்லை.",
        "Neither commission excluded Chief Ministers.", "எந்த ஆணையமும் முதலமைச்சர்களை விலக்கவில்லை.",
        "Option D accurately contrasts the First ARC's rotational 5-CM proposal with Sarkaria's all-inclusive CMs model.", "விருப்பம் D முதல் ARC-ன் 5 முதல்வர்கள் மாதிரியையும், சர்க்காரியாவின் அனைத்து முதல்வர்கள் மாதிரியையும் சரியாக ஒப்பிடுகிறது.",
        "Sarkaria Model (adopted in 1990): Inclusive federal forum comprising ALL Chief Ministers + PM + 6 Union Cabinet Ministers.",
        "சர்க்காரியா மாதிரி (1990-ல் ஏற்கப்பட்டது): அனைத்து முதலமைச்சர்கள் + பிரதமர் + 6 மத்திய அமைச்சர்களைக் கொண்ட முழுமையான கூட்டாட்சி அரங்கம்.",
        "First ARC proposed 5 CMs; Sarkaria proposed all State Chief Ministers in ISC.",
        "முதல் ARC 5 முதல்வர்களை முன்மொழிந்தது; சர்க்காரியா அனைத்து மாநில முதல்வர்களையும் ISC-ல் முன்மொழிந்தது.",
        tags=["First ARC", "Sarkaria Commission", "Inter-State Council Composition"]
    ))

    # 013 - Ans A
    q.append(make_q(
        "ISR_H_013", "Judicial Precedent Analysis",
        "In the celebrated 9-judge bench decision of Jindal Stainless Ltd. v. State of Haryana (2016), on what constitutional rationale did the Supreme Court hold that non-discriminatory taxes under Article 304(a) do not violate Article 301?",
        "ஜின்டால் ஸ்டெயின்லெஸ் லிமிடெட் vs ஹரியானா மாநிலம் (2016) என்ற புகழ்பெற்ற 9 நீதிபதிகள் அமர்வுத் தீர்ப்பில், உறுப்பு 304(a)-ன் கீழான பாகுபாடற்ற வரிகள் உறுப்பு 301-ஐ மீறாது என்று உச்ச நீதிமன்றம் எந்த அரசியலமைப்புத் தர்க்கத்தின் அடிப்படையில் தீர்ப்பளித்தது?",
        "Taxation is an inherent sovereign power essential for state existence; Article 301 guarantees freedom from trade barriers, not freedom from taxation, and as long as local and imported goods bear the same tax burden, trade flow is not impeded.", "வரிவிதிப்பு என்பது அரசு இருப்பதற்கு இன்றியமையாத உள்ளார்ந்த இறையாண்மை அதிகாரம்; உறுப்பு 301 வர்த்தகத் தடைகளிலிருந்து சுதந்திரத்திற்கு உத்தரவாதம் அளிக்கிறதே தவிர, வரிவிதிப்பிலிருந்து சுதந்திரத்திற்கு அல்ல; உள்ளூர் மற்றும் இறக்குமதி செய்யப்பட்ட பொருட்கள் ஒரே வரிச் சுமையைச் சுமக்கும் வரை, வர்த்தகப் போக்குவரத்து பாதிக்கப்படுவதில்லை.",
        "Part XIII applies only to administrative regulations, completely excluding fiscal statutes from judicial review.", "பகுதி XIII நிர்வாக ஒழுங்குமுறைகளுக்கு மட்டுமே பொருந்தும், நிதிச் சட்டங்களை நீதித்துறை மறுஆய்விலிருந்து முற்றிலும் விலக்குகிறது.",
        "State Legislatures possess unrestricted sovereign power to tax inter-State trade superior to Parliament.", "நாடாளுமன்றத்தை விட உயர்ந்ததாக மாநிலங்களுக்கு இடையிலான வர்த்தகத்தின் மீது வரிகளை விதிக்க மாநில சட்டமன்றங்களுக்கு தடையற்ற இறையாண்மை அதிகாரம் உள்ளது.",
        "Taxes are deemed non-discriminatory if approved by the Finance Commission under Article 280.", "உறுப்பு 280-ன் கீழ் நிதி ஆணையத்தால் அங்கீகரிக்கப்பட்டால் வரிகள் பாகுபாடற்றவையாகக் கருதப்படுகின்றன.",
        "A",
        "The 9-judge bench in Jindal Stainless (2016) held that the power of taxation is an inherent attribute of sovereignty. Article 301 aims to prevent economic balkanization and discriminatory trade barriers, NOT to grant tax immunity to traders. Therefore, non-discriminatory taxes levied under Article 304(a) do not restrict trade flow and do not violate Article 301, rendering the artificial 'compensatory tax' test obsolete.",
        "ஜின்டால் ஸ்டெயின்லெஸ் (2016) 9 நீதிபதிகள் அமர்வு, வரிவிதிக்கும் அதிகாரம் என்பது இறையாண்மையின் உள்ளார்ந்த பண்பு என்று கூறியது. உறுப்பு 301 என்பது பொருளாதாரப் பிளவுகளையும் பாகுபாடான வர்த்தகத் தடைகளையும் தடுப்பதை நோக்கமாகக் கொண்டதே தவிர, வர்த்தகர்களுக்கு வரிவிலக்கு அளிப்பது அல்ல. எனவே, உறுப்பு 304(a)-ன் கீழ் விதிக்கப்படும் பாகுபாடற்ற வரிகள் வர்த்தகத்தைத் தடுப்பதில்லை, இதனால் 'ஈட்டு வரி' சோதனை வழக்கற்றுப் போய்விட்டது.",
        "Option A precisely reflects the constitutional core of the majority opinion in Jindal Stainless.", "விருப்பம் A ஜின்டால் ஸ்டெயின்லெஸ் வழக்கின் பெரும்பான்மைத் தீர்ப்பின் அரசியலமைப்பு மையத்தை விளக்குகிறது.",
        "Part XIII definitely applies to taxing statutes (as settled since Atiabari).", "பகுதி XIII வரிச் சட்டங்களுக்கும் பொருந்தும் (அதியபாரி வழக்கு முதல்).",
        "State legislative power is subject to constitutional limitations in Part XIII, not unrestricted.", "மாநில அதிகாரம் தடையற்றது அல்ல, அரசியலமைப்பு வரம்புகளுக்கு உட்பட்டது.",
        "The Finance Commission does not validate State tax laws under Part XIII.", "நிதி ஆணையம் பகுதி XIII-ன் கீழ் மாநில வரிச் சட்டங்களை அங்கீகரிப்பதில்லை.",
        "Jindal Stainless Rationale: Article 301 protects trade from discriminatory trade barriers, NOT from general non-discriminatory taxation.",
        "ஜின்டால் ஸ்டெயின்லெஸ் தர்க்கம்: உறுப்பு 301 வர்த்தகத்தைப் பாகுபாடான தடைகளிலிருந்து பாதுகாக்கிறதே தவிர, பொதுவான பாகுபாடற்ற வரியிலிருந்து அல்ல.",
        "Non-discriminatory tax under Art 304(a) does not impede trade flow (Jindal Stainless).",
        "உறுப்பு 304(a)-ன் கீழான பாகுபாடற்ற வரி வர்த்தகப் போக்குவரத்தைத் தடுப்பதில்லை.",
        tags=["Jindal Stainless", "Taxation Sovereign Power", "Article 301"]
    ))

    # 014 - Ans B
    q.append(make_q(
        "ISR_H_014", "Constitutional Exception",
        "Which of the following scenarios represents a constitutionally permissible exercise of discriminatory trade legislation under Part XIII of the Constitution?",
        "அரசியலமைப்பின் பகுதி XIII-ன் கீழ் பாகுபாடான வர்த்தகச் சட்டத்தை அரசியலமைப்பு ரீதியாக அனுமதிக்கப்பட்ட வகையில் செயல்படுத்துவதை பின்வரும் சூழல்களில் எது குறிக்கிறது?",
        "A State Legislature enacts a law banning the import of textiles from other States to boost local handloom weavers.", "உள்ளூர் கைத்தறி நெசவாளர்களை ஊக்குவிக்க பிற மாநிலங்களிலிருந்து ஜவுளி இறக்குமதி செய்வதைத் தடை செய்யும் சட்டத்தை ஒரு மாநில சட்டமன்றம் இயற்றுகிறது.",
        "Parliament enacts a law granting supply preference and price subsidies for essential food grains to cyclone-affected coastal States, declaring it necessary to deal with a situation arising from scarcity of goods under Article 303(2).", "புயலால் பாதிக்கப்பட்ட கடலோர மாநிலங்களுக்கு அத்தியாவசிய உணவு தானியங்களுக்கான விநியோக முன்னுரிமை மற்றும் விலைச் சலுகைகளை வழங்கும் சட்டத்தை நாடாளுமன்றம் இயற்றுகிறது, மேலும் உறுப்பு 303(2)-ன் கீழ் பொருட்களின் பற்றாக்குறையால் எழும் சூழ்நிலையைக் கையாள இது அவசியம் என்று அறிவிக்கிறது.",
        "A State Government imposes an additional 10% entry tax on cement manufactured in other States to compensate local manufacturers for higher electricity tariffs.", "உள்ளூர் உற்பத்தியாளர்களுக்கு அதிக மின் கட்டணத்தை ஈடுசெய்ய பிற மாநிலங்களில் தயாரிக்கப்படும் சிமெண்ட் மீது மாநில அரசு கூடுதல் 10% நுழைவு வரியை விதிக்கிறது.",
        "The Inter-State Council passes a resolution prohibiting inter-State movement of gold without prior permit.", "முன் அனுமதியின்றி மாநிலங்களுக்கு இடையே தங்கம் கொண்டு செல்வதைத் தடை செய்யும் தீர்மானத்தை மாநிலங்களுக்கு இடையிலான மன்றம் நிறைவேற்றுகிறது.",
        "B",
        "Under Article 303(2), Parliament alone possesses the constitutional competence to pass discriminatory or preferential trade laws, and ONLY IF it is declared by such law that it is necessary to deal with a situation arising from a scarcity of goods in any part of India. All other discriminatory trade barriers by States (options A and C) are strictly unconstitutional under Article 303(1) and Article 304(a).",
        "உறுப்பு 303(2)-ன் கீழ், இந்தியாவில் ஏதேனும் ஒரு பகுதியில் பொருட்களின் பற்றாக்குறையால் எழும் சூழ்நிலையைக் கையாள்வதற்காகத் தேவைப்பட்டால் மட்டுமே பாகுபாடான அல்லது முன்னுரிமை அளிக்கும் வர்த்தகச் சட்டங்களை இயற்ற நாடாளுமன்றத்திற்கு மட்டுமே அரசியலமைப்பு அதிகாரம் உள்ளது. மாநிலங்களால் விதிக்கப்படும் பிற பாகுபாடான தடைகள் (விருப்பங்கள் A மற்றும் C) உறுப்புகள் 303(1) மற்றும் 304(a)-ன் கீழ் அரசியலமைப்பிற்கு முரணானவை.",
        "State Legislatures cannot discriminate to protect local industry under Article 303(1).", "உள்ளூர் தொழிலைப் பாதுகாக்க மாநில சட்டமன்றங்கள் பாகுபாடு காட்ட முடியாது.",
        "Option B precisely satisfies all constitutional criteria of Article 303(2): enacted by Parliament + declared for scarcity of goods.", "விருப்பம் B உறுப்பு 303(2)-ன் அனைத்து அரசியலமைப்பு விதிகளையும் துல்லியமாக நிறைவு செய்கிறது.",
        "Discriminatory protective entry taxes violate Article 304(a) (Jindal Stainless).", "பாகுபாடான பாதுகாப்பு நுழைவு வரிகள் உறுப்பு 304(a)-ஐ மீறுகின்றன.",
        "The Inter-State Council has no law-making power to prohibit trade.", "வர்த்தகத்தைத் தடை செய்ய மாநிலங்களுக்கு இடையிலான மன்றத்திற்குச் சட்டமியற்றும் அதிகாரம் இல்லை.",
        "Permissible discrimination under Part XIII: Enacted by Parliament ONLY + Declared for dealing with scarcity of goods (Art 303(2)).",
        "பகுதி XIII-ன் கீழ் அனுமதிக்கப்பட்ட பாகுபாடு: நாடாளுமன்றத்தால் மட்டுமே இயற்றப்பட வேண்டும் + பற்றாக்குறையைக் கையாள அறிவிக்கப்பட வேண்டும் (உறுப்பு 303(2)).",
        "Article 303(2) permits Parliament to discriminate strictly for scarcity of goods.",
        "உறுப்பு 303(2) பொருட்களின் பற்றாக்குறைக்காக மட்டுமே பாகுபாடு காட்ட நாடாளுமன்றத்தை அனுமதிக்கிறது.",
        tags=["Article 303(2)", "Scarcity Exception", "Permissible Discrimination"]
    ))

    # 015 - Ans C
    q.append(make_q(
        "ISR_H_015", "Adjudicatory Limits",
        "Can a private individual, an NGO, or a farmers' association file a dispute petition directly before an Inter-State Water Disputes Tribunal constituted under the IRWD Act, 1956?",
        "1956 ஆம் ஆண்டின் IRWD சட்டத்தின் கீழ் அமைக்கப்பட்ட நதிநீர் தகராறுகள் தீர்ப்பாயத்தின் முன் ஒரு தனிநபர், ஒரு தன்னார்வ தொண்டு நிறுவனம் (NGO) அல்லது ஒரு விவசாயிகள் சங்கம் நேரடியாகத் தகராறு மனுவைத் தாக்கல் செய்ய முடியுமா?",
        "Yes, any citizen of India has locus standi to file an original petition under Section 3 of the Act.", "ஆம், இந்தியாவின் எந்தவொரு குடிமகனுக்கும் சட்டத்தின் பிரிவு 3-ன் கீழ் அசல் மனுவைத் தாக்கல் செய்ய உரிமை உண்டு.",
        "Yes, provided the petition is endorsed by at least 10 Members of Parliament.", "ஆம், மனுவிற்கு குறைந்தது 10 நாடாளுமன்ற உறுப்பினர்கள் ஒப்புதல் அளித்திருந்தால் தாக்கல் செய்யலாம்.",
        "No, because under Section 3 of the IRWD Act, only a State Government has the legal standing to raise a water dispute and request the Central Government to refer it to a tribunal.", "முடியாது, ஏனெனில் IRWD சட்டத்தின் பிரிவு 3-ன் கீழ், ஒரு மாநில அரசு மட்டுமே நதிநீர் தகராறை எழுப்பவும், அதைத் தீர்ப்பாயத்திற்கு அனுப்புமாறு மத்திய அரசிடம் கோரவும் சட்டப்பூர்வ உரிமை கொண்டுள்ளது.",
        "Yes, but only if the dispute involves drinking water rights under Article 21.", "ஆம், ஆனால் தகராறு உறுப்பு 21-ன் கீழான குடிநீர் உரிமைகளை உள்ளடக்கியிருந்தால் மட்டுமே தாக்கல் செய்யலாம்.",
        "C",
        "Under Section 3 of the Inter-State River Water Disputes Act 1956, only a State Government can complain to the Central Government that a water dispute has arisen or is likely to arise. Private citizens, associations, farmers' organizations, or corporations have NO locus standi to initiate proceedings before an IRWD Tribunal. Their remedy, if any, lies before the Supreme Court under Article 32 or High Court under Article 226 on fundamental rights grounds.",
        "1956 IRWD சட்டத்தின் பிரிவு 3-ன் கீழ், ஒரு மாநில அரசு மட்டுமே ஒரு நதிநீர் தகராறு எழுந்துள்ளது அல்லது எழக்கூடும் என்று மத்திய அரசிடம் முறையிட முடியும். தனிநபர்கள், சங்கங்கள், விவசாயிகள் அமைப்புகள் அல்லது கழகங்களுக்கு IRWD தீர்ப்பாயத்தின் முன் வழக்குகளைத் தொடங்கும் உரிமை (locus standi) இல்லை.",
        "Citizens have no locus standi under Section 3 of the IRWD Act.", "IRWD சட்டத்தின் பிரிவு 3-ன் கீழ் குடிமக்களுக்கு மனு தாக்கல் செய்ய உரிமை இல்லை.",
        "Endorsement by MPs does not confer statutory locus standi.", "எம்.பி.க்கள் ஒப்புதல் சட்டப்பூர்வ உரிமையை வழங்காது.",
        "Option C correctly states the statutory monopoly of State Governments in initiating IRWD proceedings.", "விருப்பம் C IRWD நடவடிக்கைகளைத் தொடங்குவதில் மாநில அரசுகளின் சட்டப்பூர்வ உரிமையைச் சரியாகக் கூறுகிறது.",
        "Drinking water claims must be raised by the State Government on behalf of its inhabitants before the tribunal.", "குடிநீர் கோரிக்கைகளை மாநில அரசே தனது மக்களின் சார்பாகத் தீர்ப்பாயத்தின் முன் எழுப்ப வேண்டும்.",
        "Locus Standi under IRWD Act: EXCLUSIVELY State Governments under Section 3. Private individuals/NGOs cannot initiate tribunal proceedings.",
        "IRWD சட்டத்தின் கீழ் வழக்குரைக்கும் உரிமை: பிரிவு 3-ன் கீழ் மாநில அரசுகளுக்கு மட்டுமே. தனிநபர்கள்/தன்னார்வ நிறுவனங்கள் தீர்ப்பாயத்தில் வழக்குத் தொடர முடியாது.",
        "Only State Governments can initiate water dispute proceedings under IRWD Act.",
        "மாநில அரசுகள் மட்டுமே IRWD சட்டத்தின் கீழ் நதிநீர் தகராறு நடவடிக்கைகளைத் தொடங்க முடியும்.",
        tags=["IRWD Act 1956", "Locus Standi", "Section 3"]
    ))

    # 016 - Ans D
    q.append(make_q(
        "ISR_H_016", "Constitutional Limits of Art 301",
        "In State of Bombay v. R.M.D. Chamarbaugwala (1957), what significant constitutional doctrine did the Supreme Court lay down regarding the types of activities protected under Article 301?",
        "பம்பாய் மாநிலம் vs ஆர்.எம்.டி. சாமர்பாகவாலா (1957) வழக்கில், உறுப்பு 301-ன் கீழ் பாதுகாக்கப்படும் நடவடிக்கைகளின் வகைகள் குறித்து உச்ச நீதிமன்றம் என்ன குறிப்பிடத்தக்க அரசியலரசுக் கோட்பாட்டை வகுத்தது?",
        "All profit-making activities without exception are protected as trade under Article 301.", "விதிவிலக்கின்றி அனைத்து லாப நோக்கிலான நடவடிக்கைகளும் உறுப்பு 301-ன் கீழ் வர்த்தகமாகப் பாதுகாக்கப்படுகின்றன.",
        "State lotteries enjoy absolute immunity from trade restrictions across India.", "மாநில லாட்டரிகள் இந்தியா முழுவதும் வர்த்தகக் கட்டுப்பாடுகளிலிருந்து முழுமையான விலக்கைப் பெறுகின்றன.",
        "Only traditional barter transactions are protected under Part XIII.", "பாரம்பரிய பண்டமாற்றுப் பரிவர்த்தனைகள் மட்டுமே பகுதி XIII-ன் கீழ் பாதுகாக்கப்படுகின்றன.",
        "Gambling, prize competitions, and lotteries are 'res extra commercium' (outside commerce); inherently immoral or noxious activities do not constitute 'trade, commerce, or intercourse' and enjoy no protection under Article 301.", "சூதாட்டம், பரிசுப் போட்டிகள் மற்றும் லாட்டரிகள் 'வணிகத்திற்கு அப்பாற்பட்டவை' (res extra commercium); இயல்பாகவே ஒழுக்கக்கேடான அல்லது தீங்கு விளைவிக்கும் நடவடிக்கைகள் 'வர்த்தகம், வாணிபம் அல்லது தொடர்பு' ஆகாது மற்றும் உறுப்பு 301-ன் கீழ் எந்தப் பாதுகாப்பையும் பெறாது.",
        "D",
        "In the landmark Chamarbaugwala case (1957), the Supreme Court held that activities which are criminal, immoral, or socially harmful (such as gambling, lotteries, trafficking in human beings, or illicit liquor) are 'res extra commercium' (outside the pale of commerce). Such pernicious activities do not constitute 'trade, commerce, or intercourse' within the meaning of Article 301 and can be completely banned or heavily restricted by the State without infringing Part XIII.",
        "வரலாற்றுச் சிறப்புமிக்க சாமர்பாகவாலா வழக்கில் (1957), குற்றவியல், ஒழுக்கக்கேடான அல்லது சமூகத்திற்குத் தீங்கு விளைவிக்கும் நடவடிக்கைகள் (சூதாட்டம், லாட்டரி, ஆட்கடத்தல் அல்லது கள்ளச்சாராயம் போன்றவை) 'வணிகத்திற்கு அப்பாற்பட்டவை' (res extra commercium) என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது. இத்தகைய தீங்கு விளைவிக்கும் நடவடிக்கைகள் உறுப்பு 301-ன் பொருள் வரையறைக்குள் 'வர்த்தகம், வாணிபம் அல்லது தொடர்பு' ஆகாது மற்றும் பகுதி XIII-ஐ மீறாமல் அரசால் முற்றிலும் தடை செய்யப்படலாம்.",
        "Gambling is not protected under Article 301.", "சூதாட்டம் உறுப்பு 301-ன் கீழ் பாதுகாக்கப்படவில்லை.",
        "Lotteries do not enjoy absolute immunity; they can be banned as res extra commercium.", "லாட்டரிகள் விலக்கைப் பெற முடியாது; அவை தடை செய்யப்படலாம்.",
        "Barter transactions are not the exclusive scope of Part XIII.", "பண்டமாற்றுப் பரிவர்த்தனைகள் மட்டுமே பகுதி XIII-ன் வரம்பல்ல.",
        "Option D articulates the famous 'res extra commercium' doctrine formulated in Chamarbaugwala.", "விருப்பம் D சாமர்பாகவாலா வழக்கில் உருவாக்கப்பட்ட புகழ்பெற்ற 'வணிகத்திற்கு அப்பாற்பட்டது' (res extra commercium) கோட்பாட்டை விவரிக்கிறது.",
        "Res Extra Commercium Doctrine: Gambling, trafficking, and liquor are outside trade and commerce; they receive NO protection under Article 301.",
        "வணிகத்திற்கு அப்பாற்பட்ட கோட்பாடு: சூதாட்டம், ஆட்கடத்தல் மற்றும் மது ஆகியவை வர்த்தகத்திற்கு அப்பாற்பட்டவை; அவற்றுக்கு உறுப்பு 301-ன் கீழ் எந்தப் பாதுகாப்பும் இல்லை.",
        "Gambling and noxious activities are 'res extra commercium' under Article 301.",
        "சூதாட்டம் மற்றும் தீங்கு விளைவிக்கும் நடவடிக்கைகள் உறுப்பு 301 இன் கீழ் வணிகத்திற்கு அப்பாற்பட்டவை.",
        tags=["Chamarbaugwala", "Res Extra Commercium", "Article 301"]
    ))

    # 017 - Ans A
    q.append(make_q(
        "ISR_H_017", "Inter-State Water Dispute Jurisprudence",
        "In State of Karnataka v. State of Tamil Nadu (2018), what core federal doctrine did the Supreme Court enunciate regarding the ownership of inter-State river waters?",
        "கர்நாடக மாநிலம் vs தமிழ்நாடு மாநிலம் (2018) வழக்கில், மாநிலங்களுக்கு இடையிலான நதிநீரின் உரிமை குறித்து உச்ச நீதிமன்றம் என்ன அடிப்படைக் கூட்டாட்சிக் கோட்பாட்டை அறிவித்தது?",
        "Waters of an inter-State river are a 'national asset' in which no single State can claim exclusive proprietorship or ownership; all riparian States have equitable rights of beneficial utilization.", "மாநிலங்களுக்கு இடையிலான நதியின் நீர் ஒரு 'தேசியச் சொத்து' (national asset) ஆகும், அதில் எந்தவொரு தனி மாநிலமும் பிரத்யேக உடைமையையோ அல்லது உரிமையையோ கோர முடியாது; அனைத்து நதிப் படுகை மாநிலங்களுக்கும் பயனுள்ள பயன்பாட்டிற்கான சமத்துவ உரிமைகள் உள்ளன.",
        "The upper riparian State has absolute territorial sovereignty to use all water originating in its territory under the Harmon Doctrine.", "ஹார்மன் கோட்பாட்டின் கீழ் தனது பகுதியில் உற்பத்தியாகும் அனைத்து நீரையும் பயன்படுத்த மேல்மட்ட மாநிலத்திற்கு முழுமையான பிராந்திய இறையாண்மை உள்ளது.",
        "The lower riparian State has an absolute right to receive the natural unimpeded flow of water without any upstream storage dams.", "மேல்மட்டத்தில் எந்தவொரு சேமிப்பு அணைகளும் இன்றி நதியின் இயற்கையான தடையற்ற நீரோட்டத்தைப் பெற கீழ்மட்ட மாநிலத்திற்கு முழுமையான உரிமை உண்டு.",
        "Ownership of all inter-State rivers is automatically transferred to the Prime Minister's National Relief Fund during drought.", "வறட்சியின் போது அனைத்து மாநில நதிகளின் உரிமையும் தானாகவே பிரதமரின் தேசிய நிவாரண நிதிக்கு மாற்றப்படுகிறது.",
        "A",
        "In the final Cauvery verdict (2018), Chief Justice Dipak Misra declared: 'Waters of an inter-State river are a national asset and no single State can claim exclusive ownership of its waters.' The Supreme Court emphatically rejected the Harmon Doctrine of absolute territorial sovereignty (which upper riparian States often claim) and upheld the doctrine of equitable apportionment and community of interest among basin States.",
        "இறுதி காவிரித் தீர்ப்பில் (2018), தலைமை நீதிபதி தீபக் மிஸ்ரா அறிவித்தார்: 'மாநிலங்களுக்கு இடையிலான நதியின் நீர் ஒரு தேசியச் சொத்து மற்றும் எந்தவொரு தனி மாநிலமும் அதன் நீரின் மீது பிரத்யேக உரிமை கோர முடியாது.' உச்ச நீதிமன்றம் மேல்மட்ட மாநிலங்கள் கூறும் முழுமையான பிராந்திய இறையாண்மைக் கோட்பாட்டை (ஹார்மன் கோட்பாடு) திட்டவட்டமாக நிராகரித்து, நதிப் படுகை மாநிலங்களுக்கிடையேயான சமத்துவப் பகிர்வு மற்றும் பொதுவான நலக் கோட்பாட்டை உறுதி செய்தது.",
        "Option A precisely quotes the Supreme Court's landmark declaration in the 2018 Cauvery judgment.", "விருப்பம் A 2018 காவிரித் தீர்ப்பில் உச்ச நீதிமன்றத்தின் வரலாற்றுப் பிரகடனத்தைத் துல்லியமாக மேற்கோள் காட்டுகிறது.",
        "The Harmon Doctrine was explicitly rejected by the Supreme Court.", "ஹார்மன் கோட்பாட்டை உச்ச நீதிமன்றம் வெளிப்படையாக நிராகரித்தது.",
        "Absolute natural flow doctrine is impractical and not accepted in modern equitable apportionment.", "முழுமையான இயற்கையான நீரோட்டக் கோட்பாடு நவீன சமத்துவப் பகிர்வில் ஏற்றுக்கொள்ளப்படவில்லை.",
        "PM Relief Fund has no connection with river ownership.", "பிரதமர் நிவாரண நிதிக்கு நதி உரிமையுடன் எந்தத் தொடர்பும் இல்லை.",
        "2018 Cauvery Ruling: Inter-State river waters are a 'NATIONAL ASSET'; no riparian State owns the river exclusively.",
        "2018 காவிரித் தீர்ப்பு: மாநிலங்களுக்கு இடையிலான நதிநீர் ஒரு 'தேசியச் சொத்து'; எந்தவொரு நதிப் படுகை மாநிலமும் நதியைத் தனக்கு மட்டுமே சொந்தமாகக் கோர முடியாது.",
        "Inter-State river waters are a national asset; no state owns them exclusively.",
        "மாநிலங்களுக்கு இடையிலான நதிநீர் ஒரு தேசியச் சொத்து; எந்த மாநிலமும் அதற்கு பிரத்யேக உரிமை கோர முடியாது.",
        tags=["Cauvery Verdict 2018", "National Asset", "Equitable Apportionment"]
    ))

    # 018 - Ans B
    q.append(make_q(
        "ISR_H_018", "Constitutional Mechanics",
        "Consider the following sequence of constitutional steps required when a State Legislature introduces a law imposing trade restrictions under Article 304(b):\n1. State Cabinet approves the draft Bill.\n2. The Bill is introduced in the State Legislature.\n3. The Bill is transmitted to the President for 'previous sanction' prior to introduction.\n4. Both Houses of the State Legislature pass the Bill.\n5. The Bill is presented to the Governor for assent, who reserves it for the President under Article 200.\nWhich is the correct chronological sequence of steps required by the constitutional text?",
        "உறுப்பு 304(b)-ன் கீழ் வர்த்தகக் கட்டுப்பாடுகளை விதிக்கும் ஒரு சட்டத்தை மாநில சட்டமன்றம் அறிமுகப்படுத்தும் போது தேவைப்படும் பின்வரும் அரசியலமைப்புப் படிகளின் வரிசையைக் கவனியுங்கள்:\n1. மாநில அமைச்சரவை வரைவு மசோதாவுக்கு ஒப்புதல் அளிக்கிறது.\n2. மசோதா மாநில சட்டமன்றத்தில் அறிமுகப்படுத்தப்படுகிறது.\n3. அறிமுகப்படுத்துவதற்கு முன் மசோதா 'முன் அனுமதிக்காக' குடியரசுத் தலைவருக்கு அனுப்பப்படுகிறது.\n4. மாநில சட்டமன்றத்தின் இரு அவைகளும் மசோதாவை நிறைவேற்றுகின்றன.\n5. மசோதா ஒப்புதலுக்காக ஆளுநரிடம் சமர்ப்பிக்கப்படுகிறது, அவர் அதை உறுப்பு 200-ன் கீழ் குடியரசுத் தலைவருக்கு நிறுத்தி வைக்கிறார்.\nஅரசியலமைப்பு உரையின்படி தேவைப்படும் சரியான காலவரிசை எது?",
        "1 -> 2 -> 3 -> 4 -> 5", "1 -> 2 -> 3 -> 4 -> 5",
        "1 -> 3 -> 2 -> 4 -> 5", "1 -> 3 -> 2 -> 4 -> 5",
        "3 -> 1 -> 2 -> 4 -> 5", "3 -> 1 -> 2 -> 4 -> 5",
        "1 -> 2 -> 4 -> 5 -> 3", "1 -> 2 -> 4 -> 5 -> 3",
        "B",
        "The correct constitutional sequence under Article 304(b) proviso is: First, State Cabinet approves the policy/draft Bill (1); Second, because the proviso mandates previous sanction before introduction, the Bill is sent to the President for previous sanction (3); Third, once presidential sanction is received, the Bill is introduced in the Legislature (2); Fourth, the Legislature debates and passes the Bill (4); Fifth, the Bill is presented to the Governor, who reserves it for the President's assent under Article 200/201 (5).",
        "உறுப்பு 304(b) நிபந்தனையின் கீழான சரியான அரசியலமைப்பு வரிசை: முதலாவதாக, மாநில அமைச்சரவை வரைவு மசோதாவுக்கு ஒப்புதல் அளிக்கிறது (1); இரண்டாவதாக, அறிமுகத்திற்கு முன் அனுமதி தேவைப்படுவதால், மசோதா குடியரசுத் தலைவரின் முன் அனுமதிக்காக அனுப்பப்படுகிறது (3); மூன்றாவதாக, முன் அனுமதி பெற்றவுடன் மசோதா சட்டமன்றத்தில் அறிமுகப்படுத்தப்படுகிறது (2); நான்காவதாக, சட்டமன்றம் மசோதாவை நிறைவேற்றுகிறது (4); ஐந்தாவதாக, மசோதா ஆளுநரிடம் சமர்ப்பிக்கப்பட்டு, அவர் அதை உறுப்பு 200/201-ன் கீழ் குடியரசுத் தலைவரின் ஒப்புதலுக்கு நிறுத்தி வைக்கிறார் (5).",
        "Introducing before presidential sanction (step 2 before 3) violates the procedural mandate of the proviso to 304(b).", "முன் அனுமதிக்கு முன் அறிமுகப்படுத்துவது 304(b) நிபந்தனையை மீறுவதாகும்.",
        "Option B correctly places Presidential sanction (step 3) BEFORE legislative introduction (step 2).", "விருப்பம் B குடியரசுத் தலைவரின் முன் அனுமதியை (படி 3) சட்டமன்ற அறிமுகத்திற்கு (படி 2) முன் சரியாக வைக்கிறது.",
        "Presidential sanction cannot be sought before Cabinet approval.", "அமைச்சரவை ஒப்புதலுக்கு முன் குடியரசுத் தலைவர் அனுமதியைக் கோர முடியாது.",
        "Seeking sanction after passage (step 3 at the end) describes the curative Article 255 process, not the standard prescribed sequence.", "முடிவில் அனுமதி பெறுவது உறுப்பு 255-ன் கீழான திருத்த நடைமுறையாகும், நிலையான நடைமுறை அல்ல.",
        "Constitutional Sequence under Art 304(b): Cabinet Approval -> Presidential Prior Sanction -> Legislative Introduction -> Passage -> Assent.",
        "உறுப்பு 304(b)-ன் கீழான அரசியலமைப்பு வரிசை: அமைச்சரவை ஒப்புதல் -> குடியரசுத் தலைவர் முன் அனுமதி -> சட்டமன்ற அறிமுகம் -> நிறைவேற்றம் -> ஒப்புதல்.",
        "Sequence: Cabinet Approval (1) -> Presidential Sanction (3) -> Introduction (2) -> Passage (4) -> Assent (5).",
        "வரிசை: அமைச்சரவை ஒப்புதல் (1) -> குடியரசுத் தலைவர் அனுமதி (3) -> அறிமுகம் (2) -> நிறைவேற்றம் (4) -> ஒப்புதல் (5).",
        tags=["Article 304(b)", "Legislative Sequence", "Presidential Sanction"]
    ))

    # 019 - Ans C
    q.append(make_q(
        "ISR_H_019", "Cauvery Dispute Nuance",
        "In its final judgment on the Cauvery water dispute in February 2018, on what specific equitable ground did the Supreme Court reduce Tamil Nadu's allocation by 14.75 TMC and award it to Karnataka?",
        "பிப்ரவரி 2018-ல் காவிரி நதிநீர் தகராறு குறித்த தனது இறுதித் தீர்ப்பில், எந்தக் குறிப்பிட்ட சமத்துவ அடிப்படையில் உச்ச நீதிமன்றம் தமிழ்நாட்டின் ஒதுக்கீட்டில் 14.75 TMC-ஐக் குறைத்து கர்நாடகாவிற்கு வழங்கியது?",
        "To punish Tamil Nadu for not constructing sufficient storage check-dams along the Kollidam river.", "கொள்ளிடம் நதியில் போதுமான தடுப்பணைகளைக் கட்டாததற்காகத் தமிழ்நாட்டைத் தண்டிப்பதற்காக.",
        "To facilitate hydroelectric generation for new industrial corridors in northern Karnataka.", "வட கர்நாடகாவில் புதிய தொழிற்பேட்டைகளுக்கான நீர்மின் உற்பத்தியை எளிதாக்குவதற்காக.",
        "To meet the pressing drinking water requirements of the global mega-city of Bengaluru and accounting for 10 TMC of available groundwater in the delta area of Tamil Nadu.", "பெங்களூரு என்ற உலகளாவிய பெருநகரத்தின் அவசரக் குடிநீர்த் தேவையைப் பூர்த்தி செய்வதற்காகவும், தமிழ்நாட்டின் டெல்டா பகுதியில் கிடைக்கக்கூடிய 10 TMC நிலத்தடி நீரைக் கணக்கில் எடுத்துக்கொண்டதற்காகவும்.",
        "To comply with an arbitration ruling of the World Bank under the 1892 agreement.", "1892 உடன்படிக்கையின் கீழ் உலக வங்கியின் நடுவர் தீர்ப்பிற்கு இணங்குவதற்காக.",
        "C",
        "In the 2018 judgment, the Supreme Court determined two things: (1) Bengaluru as a global mega-city has an acute drinking water requirement that must take priority over agricultural needs, awarding 4.75 TMC for Bengaluru; and (2) out of the groundwater available in Tamil Nadu's delta region, at least 10 TMC was judicially noticed as extractable without environmental harm. Thus, 14.75 TMC (4.75 + 10) was deducted from TN's share and added to Karnataka's share.",
        "2018 ஆம் ஆண்டு தீர்ப்பில், உச்ச நீதிமன்றம் இரண்டு விஷயங்களைத் தீர்மானித்தது: (1) ஒரு உலகளாவிய பெருநகரமாக பெங்களூருவின் குடிநீர்த் தேவைக்கு விவசாயத் தேவைகளை விட முன்னுரிமை அளிக்கப்பட வேண்டும் (இதற்காக 4.75 TMC வழங்கப்பட்டது); மற்றும் (2) தமிழ்நாட்டின் டெல்டா பகுதியில் உள்ள நிலத்தடி நீரில் குறைந்தது 10 TMC சுற்றுச்சூழல் பாதிப்பின்றி எடுக்கப்படக்கூடியது என நீதிமன்றம் கண்டறிந்தது. எனவே, 14.75 TMC (4.75 + 10) தமிழ்நாட்டின் பங்கிலிருந்து கழிக்கப்பட்டு கர்நாடகாவின் பங்கிற்குச் சேர்க்கப்பட்டது.",
        "Punitive reduction is alien to equitable water apportionment principles.", "தண்டனை குறைப்பு என்பது சமத்துவ நீர் பகிர்வுக் கொள்கைகளுக்கு முரணானது.",
        "Hydroelectric generation was not the basis; drinking water was the priority.", "நீர்மின் உற்பத்தி காரணமல்ல; குடிநீரே முன்னுரிமை.",
        "Option C precisely states the two judicial grounds: Bengaluru drinking water (4.75 TMC) + Delta groundwater availability (10 TMC) = 14.75 TMC.",
        "விருப்பம் C இரண்டு நீதித்துறை காரணங்களைச் சரியாகக் கூறுகிறது: பெங்களூரு குடிநீர் (4.75 TMC) + டெல்டா நிலத்தடி நீர் (10 TMC) = 14.75 TMC.",
        "The World Bank had no role in the 2018 domestic constitutional adjudication.", "2018 உள்நாட்டுத் தீர்ப்பில் உலக வங்கிக்குப் பங்கில்லை.",
        "Cauvery 2018 Award Adjustment: 14.75 TMC transferred to Karnataka for Bengaluru drinking water (4.75 TMC) and Delta groundwater credit (10 TMC).",
        "காவிரி 2018 தீர்ப்பு மாற்றம்: பெங்களூரு குடிநீர் (4.75 TMC) மற்றும் டெல்டா நிலத்தடி நீர் வரவு (10 TMC) ஆகியவற்றிற்காக 14.75 TMC கர்நாடகாவிற்கு மாற்றப்பட்டது.",
        "2018 Cauvery adjustment: Bengaluru drinking water and delta groundwater offset.",
        "2018 காவிரி மாற்றம்: பெங்களூரு குடிநீர் மற்றும் டெல்டா நிலத்தடி நீர் கணக்கீடு.",
        tags=["Cauvery Dispute", "2018 Judgment", "Bengaluru Drinking Water"]
    ))

    # 020 - Ans D
    q.append(make_q(
        "ISR_H_020", "Federal Stand-off Scenario",
        "Suppose State A and State B have a bitter dispute over an inter-State irrigation project. The Inter-State Council, during its plenary meeting, passes a resolution directing State A to immediately halt construction of the dam. What is the legal effect of this resolution on State A?",
        "மாநிலம் A மற்றும் மாநிலம் B ஆகியவற்றுக்கு இடையே மாநிலங்களுக்கு இடையிலான ஒரு பாசனத் திட்டம் தொடர்பாகக் கடுமையான தகராறு ஏற்படுகிறது. மாநிலங்களுக்கு இடையிலான மன்றம் தனது முழு அமர்வில், அணையின் கட்டுமானத்தை உடனடியாக நிறுத்துமாறு மாநிலம் A-க்கு உத்தரவிடும் ஒரு தீர்மானத்தை நிறைவேற்றுகிறது. மாநிலம் A மீது இந்தத் தீர்மானத்தின் சட்ட விளைவு என்ன?",
        "The resolution has the force of a Supreme Court decree and State A's Chief Minister faces immediate contempt if the dam is not halted.", "இத்தீர்மானம் உச்ச நீதிமன்றத் தீர்ப்பாணையின் ஆற்றலைக் கொண்டுள்ளது, மேலும் அணை நிறுத்தப்படாவிட்டால் மாநிலம் A-ன் முதல்வர் உடனடி நீதிமன்ற அவமதிப்பை எதிர்கொள்வார்.",
        "The resolution automatically freezes all consolidated funds of State A until compliance.", "இத்தீர்மானம் மாநிலம் A-ன் அனைத்துத் தொகுப்பு நிதிகளையும் அது இணங்கும் வரை தானாகவே முடக்குகிறது.",
        "The resolution operates as a binding arbitral award enforceable through the Union Home Ministry.", "இத்தீர்மானம் மத்திய உள்துறை அமைச்சகம் மூலம் செயல்படுத்தப்பட வேண்டிய ஒரு கட்டுப்படுத்தும் நடுவர் தீர்ப்பாகச் செயல்படுகிறது.",
        "The resolution is purely advisory and recommendatory in nature; it has no binding legal force to compel State A to halt construction, and any binding order can only come from a competent judicial tribunal or court.", "இத்தீர்மானம் முற்றிலும் ஆலோசனையான மற்றும் பரிந்துரைக்கத்தக்க தன்மையுடையது; கட்டுமானத்தை நிறுத்துமாறு மாநிலம் A-ஐக் கட்டாயப்படுத்த இதற்கு எந்தவொரு சட்டப்பூர்வக் கட்டுப்படுத்தும் ஆற்றலும் இல்லை, மேலும் அத்தகைய கட்டுப்படுத்தும் ஆணை தகுதிவாய்ந்த ஒரு நீதித்துறைத் தீர்ப்பாயம் அல்லது நீதிமன்றத்திலிருந்து மட்டுமே வர முடியும்.",
        "D",
        "Article 263(a) and (c) make it abundantly clear that the Inter-State Council is an advisory and deliberative body. It has NO adjudicatory, coercive, or executive power. Its resolutions cannot override statutory or constitutional rights, nor can they operate as injunctions. Only a court (under Article 136/32) or a Water Disputes Tribunal (under Article 262/IRWD Act) can issue legally binding orders or injunctions.",
        "உறுப்பு 263(a) மற்றும் (c) மாநிலங்களுக்கு இடையிலான மன்றம் ஓர் ஆலோசனை மற்றும் விவாத அமைப்பு என்பதை மிகத் தெளிவாகக் காட்டுகின்றன. இதற்கு நீதித்துறை, கட்டாயப்படுத்தும் அல்லது நிர்வாக அதிகாரம் கிடையாது. இதன் தீர்மானங்கள் சட்டப்பூர்வ அல்லது அரசியலமைப்பு உரிமைகளை மீற முடியாது, அல்லது தடையாணையாகச் செயல்பட முடியாது. ஒரு நீதிமன்றம் அல்லது நதிநீர் தீர்ப்பாயம் மட்டுமே சட்டப்பூர்வமாகக் கட்டுப்படுத்தும் உத்தரவுகளைப் பிறப்பிக்க முடியும்.",
        "The Inter-State Council cannot pass decrees or punish for contempt.", "மன்றம் தீர்ப்பாணைகளை வழங்கவோ அல்லது அவமதிப்புக்காகத் தண்டிக்கவோ முடியாது.",
        "It cannot freeze state consolidated funds.", "இது மாநிலத் தொகுப்பு நிதியை முடக்க முடியாது.",
        "It is not an arbitral tribunal with binding execution powers.", "இது கட்டுப்படுத்தும் நிறைவேற்று அதிகாரங்களைக் கொண்ட நடுவர் மன்றம் அல்ல.",
        "Option D correctly captures the constitutional advisory limit of the Inter-State Council under Article 263.", "விருப்பம் D உறுப்பு 263-ன் கீழ் மாநிலங்களுக்கு இடையிலான மன்றத்தின் அரசியலமைப்பு ஆலோசனைக் கட்டுப்பாட்டைச் சரியாக விளக்குகிறது.",
        "Constitutional Boundary: Inter-State Council = Purely advisory; cannot issue binding injunctions or stop work orders.",
        "அரசியலமைப்பு எல்லை: மாநிலங்களுக்கு இடையிலான மன்றம் = முற்றிலும் ஆலோசனையானது; கட்டுப்படுத்தும் தடையாணைகளையோ பணி நிறுத்த உத்தரவுகளையோ பிறப்பிக்க முடியாது.",
        "Inter-State Council resolutions are purely advisory with no binding legal force.",
        "மாநிலங்களுக்கு இடையிலான மன்றத் தீர்மானங்கள் சட்டப்பூர்வக் கட்டுப்பாடு இல்லாத வெறும் ஆலோசனைகளே.",
        tags=["Article 263", "Advisory Limits", "Federal Dispute"]
    ))

    # 021 - Ans A
    q.append(make_q(
        "ISR_H_021", "Judicial Precedent & Analysis",
        "In State of Madras v. N.K. Nataraja Mudaliar (1968), what did the Supreme Court clarify regarding the validity of the Central Sales Tax Act, 1956 in the context of Article 301?",
        "மெட்ராஸ் மாநிலம் vs என்.கே. நடராஜ முதலியார் (1968) வழக்கில், உறுப்பு 301-ன் சூழலில் 1956 ஆம் ஆண்டின் மத்திய விற்பனை வரிச் சட்டத்தின் செல்லுபடியாகும் தன்மை குறித்து உச்ச நீதிமன்றம் என்ன தெளிவுபடுத்தியது?",
        "Different rates of sales tax prevailing in different States under the Central Sales Tax Act do not per se violate Article 301, as the Act was enacted by Parliament in the public interest under Article 302 to prevent unfair competition.", "மத்திய விற்பனை வரிச் சட்டத்தின் கீழ் வெவ்வேறு மாநிலங்களில் நிலவும் வெவ்வேறு விற்பனை வரி விகிதங்கள் உறுப்பு 301-ஐ இயல்பாகவே மீறாது; ஏனெனில் இச்சட்டம் நியாயமற்ற போட்டியைத் தடுக்க உறுப்பு 302-ன் கீழ் பொது நலன் கருதி நாடாளுமன்றத்தால் இயற்றப்பட்டது.",
        "All forms of Central Sales Tax violate Article 301 and must be collected solely by the President's Secretariat.", "அனைத்து வகையான மத்திய விற்பனை வரிகளும் உறுப்பு 301-ஐ மீறுகின்றன, மேலும் அவை குடியரசுத் தலைவர் செயலகத்தால் மட்டுமே வசூலிக்கப்பட வேண்டும்.",
        "The Central Sales Tax Act was declared unconstitutional because it bypassed the Inter-State Council.", "மாநிலங்களுக்கு இடையிலான மன்றத்தைப் புறக்கணித்ததால் மத்திய விற்பனை வரிச் சட்டம் அரசியலமைப்பிற்கு முரணானது என அறிவிக்கப்பட்டது.",
        "Sales tax can be levied only on agricultural produce and never on manufactured industrial goods.", "விவசாய விளைபொருட்கள் மீது மட்டுமே விற்பனை வரி விதிக்கப்படலாம், தொழில்துறை உற்பத்திப் பொருட்கள் மீது ஒருபோதும் விதிக்க முடியாது.",
        "A",
        "In Nataraja Mudaliar (1968), a 5-judge Constitution Bench held that the Central Sales Tax Act 1956 is a law enacted by Parliament in the public interest under Article 302. The variation in rates of tax from State to State, resulting from the adoption of local State tax rates, does not violate Article 301 because flow of trade is not necessarily impeded by different rates enacted in the public interest.",
        "நடராஜ முதலியார் (1968) வழக்கில், 5 நீதிபதிகள் கொண்ட அரசியலமைப்பு அமர்வு, 1956-ன் மத்திய விற்பனை வரிச் சட்டம் உறுப்பு 302-ன் கீழ் பொது நலன் கருதி நாடாளுமன்றத்தால் இயற்றப்பட்ட சட்டம் என்று தீர்ப்பளித்தது. உள்ளூர் வரி விகிதங்களை ஏற்றுக்கொண்டதன் விளைவாக மாநிலத்திற்கு மாநிலம் வரி விகிதங்களில் உள்ள மாறுபாடு உறுப்பு 301-ஐ மீறாது; ஏனெனில் பொது நலன் கருதி இயற்றப்பட்ட மாறுபட்ட விகிதங்களால் வர்த்தக ஓட்டம் பாதிக்கப்படுவதில்லை.",
        "Option A accurately presents the landmark Nataraja Mudaliar constitutional principle.", "விருப்பம் A வரலாற்றுச் சிறப்புமிக்க நடராஜ முதலியார் அரசியலரசுக் கோட்பாட்டைத் துல்லியமாக விளக்குகிறது.",
        "Central Sales Tax was upheld as constitutional, not struck down.", "மத்திய விற்பனை வரி அரசியலமைப்பு ரீதியாக உறுதி செய்யப்பட்டது, ரத்து செய்யப்படவில்லை.",
        "The Act has no requirement of routing through the Inter-State Council.", "இச்சட்டத்திற்கு மாநிலங்களுக்கு இடையிலான மன்றத்தின் ஒப்புதல் தேவையில்லை.",
        "Sales tax applies to all goods (List II, Entry 54).", "விற்பனை வரி அனைத்துப் பொருட்களுக்கும் பொருந்தும்.",
        "Nataraja Mudaliar (1968): Parliament can enact varying tax rate structures across states under Art 302 if required in the public interest.",
        "நடராஜ முதலியார் (1968): பொது நலன் கருதி தேவைப்பட்டால் உறுப்பு 302-ன் கீழ் மாநிலங்கள் முழுவதும் மாறுபட்ட வரி விகிதங்களை நாடாளுமன்றம் இயற்றலாம்.",
        "Central Sales Tax Act upheld under Article 302 in Nataraja Mudaliar case.",
        "நடராஜ முதலியார் வழக்கில் உறுப்பு 302 இன் கீழ் மத்திய விற்பனை வரிச் சட்டம் உறுதி செய்யப்பட்டது.",
        tags=["Nataraja Mudaliar", "Article 302", "Central Sales Tax"]
    ))

    # 022 - Ans B
    q.append(make_q(
        "ISR_H_022", "Full Faith and Credit Nuance",
        "Does the Full Faith and Credit clause under Article 261(1) require the courts of State X to enforce a substantive civil statute of State Y that is directly contrary to the established public policy or statutory law of State X?",
        "உறுப்பு 261(1)-ன் கீழான முழு நம்பிக்கையும் சான்றும் விதியானது, மாநிலம் X-ன் நிறுவப்பட்ட பொதுக் கொள்கை அல்லது சட்டத்திற்கு நேரடியாக முரணாக இருக்கும் மாநிலம் Y-ன் ஒரு கணிசமான உரிமையியல் சட்டத்தை மாநிலம் X-ன் நீதிமன்றங்கள் அமல்படுத்த வேண்டும் எனக் கோருகிறதா?",
        "Yes, because Article 261 mandates that every State must apply the laws of every other State blindly without exception.", "ஆம், ஏனெனில் உறுப்பு 261 விதிவிலக்கின்றி ஒவ்வொரு மாநிலமும் பிற மாநிலங்களின் சட்டங்களைக் குருட்டுத்தனமாகப் பயன்படுத்த வேண்டும் எனக் கட்டாயப்படுத்துகிறது.",
        "No, because while Full Faith and Credit requires courts to recognize the authentic existence and official proof of public acts and records of another State, it does not compel a State court to apply another State's substantive statute in preference to its own forum law on matters within its own jurisdiction.", "இல்லை, ஏனெனில் முழு நம்பிக்கையும் சான்றும் விதியானது மற்றொரு மாநிலத்தின் பொதுச் சட்டங்கள் மற்றும் பதிவேடுகளின் உண்மையான இருப்பு மற்றும் அதிகாரப்பூர்வ சான்றை அங்கீகரிக்க மட்டுமே கோருகிறது; ஆனால் தனது சொந்த அதிகார வரம்பிற்குட்பட்ட விஷயங்களில் தனது சொந்த நீதிமன்றச் சட்டத்தை விட மற்றொரு மாநிலத்தின் சட்டத்தைப் பயன்படுத்த வேண்டும் என்று அது மாநில நீதிமன்றத்தைக் கட்டாயப்படுத்தாது.",
        "Yes, provided the Supreme Court issues a writ of mandamus directing universal application.", "ஆம், உச்ச நீதிமன்றம் உலகளாவிய பயன்பாட்டை வழிநடத்தும் ஒரு மாண்டமஸ் பேராணையைப் பிறப்பித்தால் அவ்வாறு செய்ய வேண்டும்.",
        "No, because Article 261 applies only to Union Territories and has no application between States.", "இல்லை, ஏனெனில் உறுப்பு 261 யூனியன் பிரதேசங்களுக்கு மட்டுமே பொருந்தும், மாநிலங்களுக்கிடையே பொருந்தாது.",
        "B",
        "Article 261(1) is an evidentiary rule of recognition, not a rule of choice of law. It mandates that public acts, records, and judicial proceedings of another State must be recognized as authentic and given full evidentiary credit without requiring independent foreign proof. However, it does not compel a State forum to enforce another State's substantive laws if they conflict with its own local laws or public policy (Private International Law principles within federalism).",
        "உறுப்பு 261(1) என்பது அங்கீகாரத்திற்கான ஒரு சான்று விதியே தவிர, சட்டத்தைத் தேர்ந்தெடுக்கும் விதி அல்ல. மற்றொரு மாநிலத்தின் பொதுச் சட்டங்கள், பதிவேடுகள் மற்றும் நீதித்துறை நடவடிக்கைகள் உண்மையானவை என அங்கீகரிக்கப்பட வேண்டும் என்று அது கட்டாயப்படுத்துகிறது. இருப்பினும், தனது சொந்த உள்ளூர் சட்டங்கள் அல்லது பொதுக் கொள்கையுடன் முரண்பட்டால் மற்றொரு மாநிலத்தின் சட்டங்களை அமல்படுத்த வேண்டும் என்று அது ஒரு மாநில நீதிமன்றத்தைக் கட்டாயப்படுத்தாது.",
        "Article 261 does not erase state legislative sovereignty or force foreign state laws onto a local court.", "உறுப்பு 261 மாநிலச் சட்டமன்ற இறையாண்மையை அழிக்காது.",
        "Option B correctly explains the evidentiary recognition vs choice of law doctrine under Article 261.", "விருப்பம் B உறுப்பு 261-ன் கீழான சான்று அங்கீகாரம் மற்றும் சட்டப் பயன்பாட்டு வேறுபாட்டைச் சரியாக விளக்குகிறது.",
        "Mandamus cannot compel a court to violate its own forum statutes.", "மாண்டமஸ் பேராணை நீதிமன்றங்களைத் தனது சட்டங்களை மீறக் கட்டாயப்படுத்த முடியாது.",
        "Article 261 applies throughout India to all States and the Union.", "உறுப்பு 261 அனைத்து மாநிலங்களுக்கும் ஒன்றியத்திற்கும் பொருந்தும்.",
        "Full Faith and Credit (Art 261) guarantees EVIDENTIARY recognition of public acts/records, but does NOT force a State court to adopt another State's substantive law over its own forum law.",
        "முழு நம்பிக்கை மற்றும் சான்று (உறுப்பு 261) பொதுச் சட்டங்களின் சான்று அங்கீகாரத்திற்கு உத்தரவாதம் அளிக்கிறது, ஆனால் மற்றொரு மாநிலச் சட்டத்தை ஏற்க கட்டாயப்படுத்தாது.",
        "Article 261 requires evidentiary recognition, not extraterritorial application of substantive law.",
        "உறுப்பு 261 சான்று அங்கீகாரத்தைக் கோருகிறது, கணிசமான சட்டத்தின் பிராந்தியத்திற்கு அப்பாற்பட்ட பயன்பாட்டை அல்ல.",
        tags=["Article 261", "Full Faith and Credit", "Private International Law"]
    ))

    # 023 - Ans C
    q.append(make_q(
        "ISR_H_023", "Statutory Reform",
        "Under the Inter-State River Water Disputes (Amendment) Bill introduced in Parliament, what is the key institutional reform proposed to replace the existing system of multiple ad hoc water dispute tribunals?",
        "நாடாளுமன்றத்தில் அறிமுகப்படுத்தப்பட்ட மாநிலங்களுக்கு இடையேயான நதிநீர் தகராறுகள் (திருத்த) மசோதாவின் கீழ், பல தற்காலிக நதிநீர் தீர்ப்பாயங்களின் தற்போதைய அமைப்பை மாற்றுவதற்கு முன்மொழியப்பட்ட முக்கிய நிறுவனச் சீர்திருத்தம் என்ன?",
        "Transferring all river disputes permanently to the International Court of Arbitration.", "அனைத்து நதித் தகராறுகளையும் நிரந்தரமாக சர்வதேச நடுவர் மன்றத்திற்கு மாற்றுதல்.",
        "Abolishing all judicial tribunals and leaving water sharing solely to bilateral agreements between Chief Ministers.", "அனைத்து நீதித்துறைத் தீர்ப்பாயங்களையும் ஒழித்துவிட்டு, நதிநீர் பகிர்வை முதலமைச்சர்களுக்கிடையேயான இருதரப்பு ஒப்பந்தங்களிடம் மட்டுமே விட்டுவிடுதல்.",
        "Establishing a single, standalone permanent Inter-State River Water Disputes Tribunal with multiple specialized benches, along with a Dispute Resolution Committee (DRC) for pre-tribunal conciliation.", "முன்-தீர்ப்பாய சமரசத்திற்கான தகராறு தீர்வு குழுவுடன் (DRC) பல சிறப்பு அமர்வுகளைக் கொண்ட ஒரு ஒற்றை நிரந்தர நதிநீர் தகராறுகள் தீர்ப்பாயத்தை நிறுவுதல்.",
        "Empowering the Governor of the downstream State to fix water release quotas unilaterally.", "கீழ்மட்ட மாநிலத்தின் ஆளுநருக்கு நீர் வெளியேற்றப் பங்கீட்டை ஒருதலைப்பட்சமாக நிர்ணயிக்க அதிகாரம் அளித்தல்.",
        "C",
        "The Inter-State River Water Disputes (Amendment) Bill seeks to streamline adjudication by replacing ad hoc tribunals with a single permanent Inter-State River Water Disputes Tribunal with multiple benches. It also introduces a Dispute Resolution Committee (DRC) headed by a Secretary-rank officer to resolve disputes through conciliation within one year (extendable by 6 months) before reference to the Tribunal.",
        "நதிநீர் தகராறுகள் (திருத்த) மசோதா, தற்காலிகத் தீர்ப்பாயங்களுக்குப் பதிலாக பல அமர்வுகளைக் கொண்ட ஒற்றை நிரந்தர நதிநீர் தகராறுகள் தீர்ப்பாயத்தை அமைப்பதன் மூலம் தீர்ப்பளிப்பதை நெறிப்படுத்த முயல்கிறது. மேலும், தீர்ப்பாயத்திற்கு அனுப்புவதற்கு முன் ஒரு வருடத்திற்குள் சமரசம் மூலம் தகராறுகளைத் தீர்க்க செயலாளர் அந்தஸ்து கொண்ட அதிகாரி தலைமையிலான தகராறு தீர்வு குழுவை (DRC) இது அறிமுகப்படுத்துகிறது.",
        "The Bill has no relation to international arbitration.", "இம்மசோதாவுக்கு சர்வதேச நடுவர் மன்றத்துடன் எந்தத் தொடர்பும் இல்லை.",
        "It does not abolish judicial resolution; it creates a single permanent tribunal.", "இது நீதித்துறைத் தீர்வை ஒழிக்கவில்லை; ஒரு நிரந்தரத் தீர்ப்பாயத்தை உருவாக்குகிறது.",
        "Option C precisely describes the single permanent tribunal + DRC conciliation architecture.", "விருப்பம் C ஒற்றை நிரந்தரத் தீர்ப்பாயம் + DRC சமரசக் கட்டமைப்பைத் துல்லியமாக விவரிக்கிறது.",
        "Governors have no statutory quota-fixing powers.", "ஆளுநர்களுக்கு நீர் பங்கீடு நிர்ணயிக்கும் அதிகாரம் இல்லை.",
        "Proposed IRWD Reform: Single permanent tribunal with multiple benches + Dispute Resolution Committee (DRC) for initial conciliation.",
        "முன்மொழியப்பட்ட IRWD சீர்திருத்தம்: பல அமர்வுகளைக் கொண்ட ஒற்றை நிரந்தரத் தீர்ப்பாயம் + ஆரம்ப சமரசத்திற்கான தகராறு தீர்வு குழு (DRC).",
        "IRWD Amendment Bill proposes a single permanent tribunal with multiple benches.",
        "IRWD திருத்த மசோதா பல அமர்வுகளைக் கொண்ட ஒற்றை நிரந்தரத் தீர்ப்பாயத்தை முன்மொழிகிறது.",
        tags=["IRWD Amendment Bill", "Single Tribunal", "DRC"]
    ))

    # 024 - Ans D
    q.append(make_q(
        "ISR_H_024", "Institutional Integration",
        "Following the 2018 restructuring of the North Eastern Council (NEC), who currently serves as the Chairman of the North Eastern Council, and who serves as the Vice-Chairman?",
        "வடகிழக்கு கவுன்சிலின் (NEC) 2018 மறுசீரமைப்பைத் தொடர்ந்து, தற்போது வடகிழக்கு கவுன்சிலின் தலைவராகச் செயல்படுபவர் யார், மேலும் துணைத் தலைவராகச் செயல்படுபவர் யார்?",
        "The Prime Minister serves as Chairman; the Minister of Defence serves as Vice-Chairman.", "பிரதமர் தலைவராகவும்; பாதுகாப்பு அமைச்சர் துணைத் தலைவராகவும் செயல்படுகின்றனர்.",
        "The Governor of Assam serves as Chairman; Chief Minister of Assam serves as Vice-Chairman.", "அசாம் ஆளுநர் தலைவராகவும்; அசாம் முதல்வர் துணைத் தலைவராகவும் செயல்படுகின்றனர்.",
        "The Chief Minister of the host State serves as Chairman; the NITI Aayog CEO serves as Vice-Chairman.", "நடத்தும் மாநில முதல்வர் தலைவராகவும்; நிதி ஆயோக் தலைமை நிர்வாக அதிகாரி துணைத் தலைவராகவும் செயல்படுகின்றனர்.",
        "The Union Minister of Home Affairs serves as the Chairman; the Minister of State (Independent Charge) for the Ministry of Development of North Eastern Region (DoNER) serves as the Vice-Chairman.", "மத்திய உள்துறை அமைச்சர் தலைவராகவும்; வடகிழக்குப் பகுதி வளர்ச்சி அமைச்சகத்தின் (DoNER) தனிப் பொறுப்பு இணை அமைச்சர் துணைத் தலைவராகவும் செயல்படுகின்றனர்.",
        "D",
        "In June 2018, the Union Cabinet approved a historic structural revision to the North Eastern Council: the Union Minister of Home Affairs was made the ex-officio Chairman of the NEC, and the Minister of State (Independent Charge), Ministry of Development of North Eastern Region (DoNER), was made the Vice-Chairman. This aligned the chairmanship of the NEC with that of the five Zonal Councils.",
        "ஜூன் 2018-ல், மத்திய அமைச்சரவை வடகிழக்கு கவுன்சிலில் ஒரு வரலாற்றுச் சீர்திருத்தத்திற்கு ஒப்புதல் அளித்தது: மத்திய உள்துறை அமைச்சர் NEC-ன் பதவிவழித் தலைவராகவும், வடகிழக்குப் பகுதி வளர்ச்சி அமைச்சகத்தின் (DoNER) இணை அமைச்சர் துணைத் தலைவராகவும் நியமிக்கப்பட்டனர். இது NEC-ன் தலைமைத்துவத்தை ஐந்து மண்டலக் குழுக்களின் தலைமைத்துவத்துடன் இணைத்தது.",
        "The Prime Minister does not chair the NEC.", "பிரதமர் NEC-க்குத் தலைமை தாங்குவதில்லை.",
        "The Governor of Assam does not hold a permanent chairmanship.", "அசாம் ஆளுநருக்கு நிரந்தரத் தலைமை கிடையாது.",
        "State Chief Ministers do not chair the NEC.", "மாநில முதல்வர்கள் NEC-க்குத் தலைமை தாங்குவதில்லை.",
        "Option D accurately reflects the 2018 Cabinet restructuring making the Union Home Minister Chairman of NEC.", "விருப்பம் D மத்திய உள்துறை அமைச்சரை NEC தலைவராக்கிய 2018 மறுசீரமைப்பைச் சரியாகக் குறிப்பிடுகிறது.",
        "NEC Leadership (since 2018): Chairman = Union Home Minister; Vice-Chairman = Minister of State for DoNER.",
        "NEC தலைமை (2018 முதல்): தலைவர் = மத்திய உள்துறை அமைச்சர்; துணைத் தலைவர் = DoNER இணை அமைச்சர்.",
        "Union Home Minister is Chairman of NEC since 2018 restructuring.",
        "2018 மறுசீரமைப்பு முதல் மத்திய உள்துறை அமைச்சர் NEC-ன் தலைவராக உள்ளார்.",
        tags=["North Eastern Council", "2018 Restructuring", "Union Home Minister"]
    ))

    # 025 - Ans A
    q.append(make_q(
        "ISR_H_025", "Regulatory vs Restrictive Measures",
        "In Indian constitutional jurisprudence on Part XIII, which of the following measures is categorized as a permissible 'regulatory measure' that does NOT infringe Article 301, rather than a restrictive barrier?",
        "பகுதி XIII மீதான இந்திய அரசியலமைப்பு நீதித்துறையில், பின்வரும் நடவடிக்கைகளில் எது வர்த்தகத் தடையாக இல்லாமல், உறுப்பு 301-ஐ மீறாத ஒரு அனுமதிக்கப்பட்ட 'ஒழுங்குமுறை நடவடிக்கை' என வகைப்படுத்தப்படுகிறது?",
        "Traffic safety regulations, vehicular emission norms, and reasonable weighbridge checks on commercial freight carriers.", "போக்குவரத்துப் பாதுகாப்பு விதிமுறைகள், வாகனப் புகை உமிழ்வுத் தரநிலைகள் மற்றும் வணிக சரக்கு வாகனங்கள் மீதான நியாயமான எடைமேடைச் சோதனைகள்.",
        "A total embargo on the movement of wheat across state borders to control regional inflation.", "பிராந்திய பணவீக்கத்தைக் கட்டுப்படுத்த மாநில எல்லைகளில் கோதுமை இயக்கத்திற்கு முழுமையான தடை விதித்தல்.",
        "A 20% protective tariff imposed exclusively on textiles manufactured outside the State.", "மாநிலத்திற்கு வெளியே தயாரிக்கப்படும் ஜவுளிகள் மீது மட்டும் விதிக்கப்படும் 20% பாதுகாப்பு வரி.",
        "A law mandating that inter-State trucks can enter the State only if owned by residents of that State.", "மாநிலத்திற்குள் நுழையும் வெளிமாநில லாரிகள் அந்த மாநிலக் குடிமக்களுக்குச் சொந்தமானதாக இருந்தால் மட்டுமே நுழைய முடியும் என்று கட்டாயப்படுத்தும் ஒரு சட்டம்.",
        "A",
        "The Supreme Court has consistently held that measures which facilitate the orderly conduct of trade (such as traffic regulations, speed limits, vehicle fitness certificates, and reasonable weight checks) are REGULATORY in nature and do not constitute an impediment under Article 301. Freedom of trade does not mean freedom from all regulation; orderly regulation promotes rather than impedes trade.",
        "வர்த்தகத்தின் ஒழுங்கான நடத்தைக்கு உதவும் நடவடிக்கைகள் (போக்குவரத்து விதிமுறைகள், வேக வரம்புகள், வாகனத் தகுதிச் சான்றிதழ்கள் மற்றும் நியாயமான எடைச் சோதனைகள் போன்றவை) இயல்பாகவே 'ஒழுங்குமுறை சார்ந்தவை' என்றும் உறுப்பு 301-ன் கீழ் தடையாக அமையாது என்றும் உச்ச நீதிமன்றம் தொடர்ந்து தீர்ப்பளித்துள்ளது. வர்த்தக சுதந்திரம் என்பது அனைத்துக் கட்டுப்பாடுகளிலிருந்தும் விடுபடுவது அல்ல; ஒழுங்குமுறை வர்த்தகத்தைத் தடுக்காமல் ஊக்குவிக்கிறது.",
        "Option A represents standard permissible regulatory measures recognized by the judiciary.", "விருப்பம் A நீதித்துறையால் அங்கீகரிக்கப்பட்ட அனுமதிக்கப்பட்ட ஒழுங்குமுறை நடவடிக்கைகளைக் குறிக்கிறது.",
        "Total embargo is a direct and absolute restriction requiring strict justification under Art 302/304(b).", "முழுத் தடை என்பது நேரடிக் கட்டுப்பாடாகும்.",
        "Protective tariffs directly violate Article 304(a) and Article 301.", "பாதுகாப்பு வரிகள் உறுப்புகள் 304(a) மற்றும் 301-ஐ நேரடியாக மீறுகின்றன.",
        "Resident-only truck ownership is blatantly discriminatory and unconstitutional.", "உள்ளூர்வாசி மட்டுமே லாரி வைத்திருக்க வேண்டும் என்பது அப்பட்டமான பாகுபாடாகும்.",
        "Regulatory vs Restrictive: Measures facilitating orderly trade (traffic rules, weight limits, health inspections) do NOT restrict trade under Article 301.",
        "ஒழுங்குமுறை vs கட்டுப்பாடு: வர்த்தகத்தை ஒழுங்குபடுத்தும் நடவடிக்கைகள் (போக்குவரத்து விதிகள், எடை வரம்புகள்) உறுப்பு 301-ஐ மீறாது.",
        "Traffic and safety regulations are permissible regulatory measures under Part XIII.",
        "போக்குவரத்து மற்றும் பாதுகாப்பு விதிமுறைகள் பகுதி XIII இன் கீழ் அனுமதிக்கப்பட்ட ஒழுங்குமுறை நடவடிக்கைகளாகும்.",
        tags=["Part XIII", "Regulatory Measures", "Article 301"]
    ))

    # 026 - Ans B
    q.append(make_q(
        "ISR_H_026", "Institutional Role Analysis",
        "What is the primary constitutional role of the Standing Committee of the Inter-State Council in relation to the full plenary Council?",
        "முழுமையான மாநிலங்களுக்கு இடையிலான மன்றத்துடன் ஒப்பிடுகையில் அதன் நிலைக் குழுவின் முதன்மை அரசியலமைப்புப் பங்கு என்ன?",
        "It acts as a final appellate body to hear appeals against decisions of the Prime Minister.", "பிரதமரின் முடிவுகளுக்கு எதிரான மேல்முறையீடுகளை விசாரிக்கும் இறுதி மேல்முறையீட்டு அமைப்பாக இது செயல்படுகிறது.",
        "It carries out continuous consultation, monitors the implementation of Council recommendations, and processes matters before they are placed for consideration before the full Council.", "இது தொடர்ச்சியான ஆலோசனைகளை மேற்கொள்கிறது, மன்றத்தின் பரிந்துரைகளைச் செயல்படுத்துவதைக் கண்காணிக்கிறது, மேலும் அவை முழு மன்றத்தின் பரிசீலனைக்கு வைக்கப்படுவதற்கு முன்பு விவகாரங்களை ஒழுங்குபடுத்துகிறது.",
        "It exercises the power to veto decisions made by the full Inter-State Council.", "முழு மாநிலங்களுக்கு இடையிலான மன்றத்தால் எடுக்கப்பட்ட முடிவுகளை வீட்டோ செய்யும் அதிகாரத்தை இது செலுத்துகிறது.",
        "It is responsible for drafting constitutional amendments under Article 368.", "உறுப்பு 368-ன் கீழ் அரசியலமைப்புத் திருத்தங்களை வரைவு செய்யும் பொறுப்பை இது கொண்டுள்ளது.",
        "B",
        "The Standing Committee of the Inter-State Council was set up in 1996 specifically to: (i) have continuous consultation and process matters for consideration of the Council; (ii) process all matters pertaining to Centre-State relations before they are taken up in the Inter-State Council; and (iii) monitor the implementation of decisions taken on the recommendations of the Council.",
        "1996-ல் அமைக்கப்பட்ட மாநிலங்களுக்கு இடையிலான மன்றத்தின் நிலைக் குழுவின் முக்கியப் பணிகள்: (i) தொடர்ச்சியான ஆலோசனைகளை மேற்கொண்டு மன்றத்தின் பரிசீலனைக்கான விஷயங்களை ஒழுங்குபடுத்துதல்; (ii) மத்திய-மாநில உறவுகள் தொடர்பான அனைத்து விஷயங்களையும் முழு மன்றத்தில் எடுப்பதற்கு முன் ஆய்வு செய்தல்; (iii) மன்றத்தின் பரிந்துரைகளின் பேரில் எடுக்கப்பட்ட முடிவுகளைச் செயல்படுத்துவதைக் கண்காணித்தல்.",
        "It is not an appellate body against the Prime Minister.", "இது பிரதமருக்கு எதிரான மேல்முறையீட்டு அமைப்பு அல்ல.",
        "Option B accurately reflects the preparatory and monitoring mandate of the Standing Committee.", "விருப்பம் B நிலைக் குழுவின் தயாரிப்பு மற்றும் கண்காணிப்புப் பணியைத் துல்லியமாக விளக்குகிறது.",
        "A subordinate committee cannot veto the plenary Council.", "ஒரு சார்புக் குழு முழு மன்றத்தை வீட்டோ செய்ய முடியாது.",
        "Drafting constitutional amendments is the function of the Union Ministry of Law and Parliament.", "அரசியலமைப்புத் திருத்தங்களை வரைவது சட்ட அமைச்சகம் மற்றும் நாடாளுமன்றத்தின் பணியாகும்.",
        "Standing Committee of ISC: Continuous consultation + Pre-processing of agenda + Monitoring implementation of ISC decisions.",
        "ISC நிலைக் குழு: தொடர்ச்சியான ஆலோசனை + நிகழ்ச்சி நிரல் தயாரிப்பு + ISC முடிவுகளைச் செயல்படுத்துவதைக் கண்காணித்தல்.",
        "Standing Committee carries out continuous consultation and monitors implementation.",
        "நிலைக் குழு தொடர்ச்சியான ஆலோசனைகளை மேற்கொண்டு முடிவுகளைக் கண்காணிக்கிறது.",
        tags=["Standing Committee", "Inter-State Council", "Functions"]
    ))

    # 027 - Ans C
    q.append(make_q(
        "ISR_H_027", "Constitutional Tests",
        "Suppose State Legislature P passes an Act imposing restrictions on inter-State trade under Article 304(b). The Bill was introduced with the prior sanction of the President. In a challenge before the High Court, the State argues that because prior presidential sanction was granted, the Court cannot review whether the restriction is 'reasonable' or in the 'public interest'. Is this contention correct?",
        "மாநில சட்டமன்றம் P உறுப்பு 304(b)-ன் கீழ் மாநிலங்களுக்கு இடையிலான வர்த்தகத்தின் மீது கட்டுப்பாடுகளை விதிக்கும் ஒரு சட்டத்தை இயற்றுகிறது. மசோதா குடியரசுத் தலைவரின் முன் அனுமதியுடன் அறிமுகப்படுத்தப்பட்டது. உயர் நீதிமன்றத்தில் தொடரப்பட்ட வழக்கில், குடியரசுத் தலைவரின் முன் அனுமதி வழங்கப்பட்டுவிட்டதால், அ his கட்டுப்பாடு 'நியாயமானதா' அல்லது 'பொது நலன்' சார்ந்ததா என்பதை நீதிமன்றம் மறுஆய்வு செய்ய முடியாது என்று மாநில அரசு வாதிடுகிறது. இந்த வாதம் சரியானதா?",
        "Yes, because Presidential sanction renders all legislative provisions non-justiciable under Article 74.", "ஆம், ஏனெனில் குடியரசுத் தலைவர் அனுமதி உறுப்பு 74-ன் கீழ் அனைத்துச் சட்டமன்ற விதிகளையும் நீதித்துறை ஆய்விற்கு அப்பாற்பட்டதாக ஆக்குகிறது.",
        "Yes, because courts cannot question economic policies of State Governments under any circumstances.", "ஆம், ஏனெனில் எந்தச் சூழ்நிலையிலும் மாநில அரசுகளின் பொருளாதாரக் கொள்கைகளை நீதிமன்றங்கள் கேள்வி கேட்க முடியாது.",
        "No, because Presidential sanction is merely a procedural condition for introduction; whether the restriction is 'reasonable' and in the 'public interest' are substantive constitutional requirements subject to judicial review.", "இல்லை, ஏனெனில் குடியரசுத் தலைவரின் அனுமதி என்பது அறிமுகப்படுத்துவதற்கான ஒரு நடைமுறை நிபந்தனை மட்டுமே; அக் கட்டுப்பாடு 'நியாயமானதா' மற்றும் 'பொது நலன்' சார்ந்ததா என்பது நீதித்துறை மறுஆய்வுக்கு உட்பட்ட கணிசமான அரசியலமைப்புத் தேவைகளாகும்.",
        "No, but the review can be performed only by the Inter-State Council, not by the High Court.", "இல்லை, ஆனால் இந்த மறுஆய்வை உயர் நீதிமன்றத்தால் செய்ய முடியாது, மாநிலங்களுக்கு இடையிலான மன்றத்தால் மட்டுமே செய்ய முடியும்.",
        "C",
        "The Supreme Court has firmly settled that Presidential sanction under the proviso to Article 304(b) is merely a condition precedent for introducing the bill. It does NOT insulate the law from judicial review. The court retains full constitutional power to independently examine whether the restriction is 'reasonable' and genuinely required in the 'public interest'. Both substantive tests must be objectively proven by the State.",
        "உறுப்பு 304(b)-ன் நிபந்தனையின் கீழான குடியரசுத் தலைவர் அனுமதி என்பது மசோதாவை அறிமுகப்படுத்துவதற்கான ஒரு முன் நிபந்தனை மட்டுமே என்று உச்ச நீதிமன்றம் திட்டவட்டமாக நிறுவியுள்ளது. அது சட்டத்தை நீதித்துறை மறுஆய்விலிருந்து பாதுகாக்காது. கட்டுப்பாடு 'நியாயமானதா' மற்றும் உண்மையாகவே 'பொது நலன்' கருதி தேவைப்படுகிறதா என்பதைச் சுயாதீனமாக ஆய்வு செய்யும் முழு அரசியலமைப்பு அதிகாரத்தை நீதிமன்றம் கொண்டுள்ளது.",
        "Presidential sanction does not oust judicial review of fundamental or constitutional rights.", "குடியரசுத் தலைவர் அனுமதி நீதித்துறை மறுஆய்வைத் தடுக்காது.",
        "Economic restrictions affecting trade freedom are subject to judicial review under Part XIII.", "பகுதி XIII-ன் கீழ் பொருளாதாரக் கட்டுப்பாடுகள் நீதித்துறை ஆய்வுக்கு உட்பட்டவை.",
        "Option C correctly explains that Presidential sanction is procedural, while reasonableness and public interest are justiciable substantive tests.", "விருப்பம் C குடியரசுத் தலைவர் அனுமதி நடைமுறை சார்ந்தது என்பதையும், நியாயத்தன்மை நீதித்துறை ஆய்வுக்கு உட்பட்டது என்பதையும் சரியாக விளக்குகிறது.",
        "High Courts possess writ jurisdiction under Article 226 to examine Part XIII violations.", "உயர் நீதிமன்றங்களுக்கு பகுதி XIII மீறல்களை ஆய்வு செய்ய உறுப்பு 226-ன் கீழ் அதிகாரம் உண்டு.",
        "Judicial Review of Art 304(b): Presidential sanction does NOT bar judicial review; Courts must still test 'reasonableness' and 'public interest'.",
        "உறுப்பு 304(b) நீதித்துறை மறுஆய்வு: குடியரசுத் தலைவர் அனுமதி நீதித்துறை மறுஆய்வைத் தடுக்காது; நீதிமன்றங்கள் 'நியாயத்தன்மை' மற்றும் 'பொது நலனை' ஆய்வு செய்ய வேண்டும்.",
        "Presidential sanction under Art 304(b) does not bar judicial review of reasonableness.",
        "உறுப்பு 304(b)-ன் கீழான குடியரசுத் தலைவர் அனுமதி நியாயத்தன்மையின் நீதித்துறை மறுஆய்வைத் தடுக்காது.",
        tags=["Article 304(b)", "Judicial Review", "Reasonableness"]
    ))

    # 028 - Ans D
    q.append(make_q(
        "ISR_H_028", "Doctrine of Territorial Nexus",
        "In the context of inter-State trade and State taxation, how does the Doctrine of Territorial Nexus apply to determine the validity of a State tax on an inter-State transaction?",
        "மாநிலங்களுக்கு இடையிலான வர்த்தகம் மற்றும் மாநில வரிவிதிப்பின் சூழலில், ஒரு மாநிலங்களுக்கிடையேயான பரிவர்த்தனை மீதான மாநில வரியின் செல்லுபடியாகும் தன்மையைத் தீர்மானிக்க 'பிராந்தியத் தொடர்பு கோட்பாடு' (Doctrine of Territorial Nexus) எவ்வாறு பொருந்துகிறது?",
        "A State can tax any transaction occurring anywhere in India regardless of connection.", "தொடர்பைப் பொருட்படுத்தாமல் இந்தியாவில் எங்கு நடக்கும் பரிவர்த்தனை மீதும் ஒரு மாநிலம் வரி விதிக்க முடியும்.",
        "A State can tax an inter-State sale only if both the buyer and seller reside in the same district.", "வாங்குபவர் மற்றும் விற்பவர் இருவரும் ஒரே மாவட்டத்தில் வசித்தால் மட்டுமே ஒரு மாநிலம் மாநிலங்களுக்கு இடையிலான விற்பனைக்கு வரி விதிக்க முடியும்.",
        "Territorial nexus applies only to maritime customs duties under Central law.", "மத்தியச் சட்டத்தின் கீழான கடல்சார் சுங்க வரிகளுக்கு மட்டுமே பிராந்தியத் தொடர்பு பொருந்தும்.",
        "There must be a real and sufficient connection between the taxing State and the subject matter of the tax (such as goods being manufactured, stored, or delivered within the State); an extraterritorial tax without such nexus is void.", "வரி விதிக்கும் மாநிலத்திற்கும் வரியின் பாடுபொருளுக்கும் இடையே உண்மையான மற்றும் போதுமான தொடர்பு இருக்க வேண்டும் (பொருட்கள் அந்த மாநிலத்திற்குள் உற்பத்தி செய்யப்படுதல், சேமிக்கப்படுதல் அல்லது வழங்கப்படுதல் போன்றவை); அத்தகைய தொடர்பில்லாத பிராந்தியத்திற்கு அப்பாற்பட்ட வரி செல்லாது.",
        "D",
        "Under the Doctrine of Territorial Nexus (applied in Tata Iron & Steel Co. v. State of Bihar and State of Bombay v. R.M.D. Chamarbaugwala), a State Legislature can tax extra-territorial aspects only if there is a real, substantial, and not illusory connection between the State and the taxable transaction or person. In the absence of a sufficient territorial nexus, the State law is ultra vires and invalid.",
        "பிராந்தியத் தொடர்பு கோட்பாட்டின் கீழ் (டாடா அயர்ன் & ஸ்டீல் கோ vs பீகார் மாநிலம் போன்றவற்றில் பயன்படுத்தப்பட்டது), மாநிலத்திற்கும் வரிவிதிப்புக்குரிய பரிவர்த்தனை அல்லது நபருக்கும் இடையே உண்மையான, கணிசமான தொடர்பு இருந்தால் மட்டுமே ஒரு மாநில சட்டமன்றம் வரி விதிக்க முடியும். போதுமான பிராந்தியத் தொடர்பு இல்லாத நிலையில், மாநிலச் சட்டம் அதிகார வரம்பை மீறியதாகவும் செல்லாததாகவும் மாறும்.",
        "States cannot tax extraterritorially without nexus.", "தொடர்பின்றி மாநிலங்கள் பிராந்தியத்திற்கு அப்பால் வரி விதிக்க முடியாது.",
        "Buyer and seller do not need to reside in the same district.", "வாங்குபவரும் விற்பவரும் ஒரே மாவட்டத்தில் வசிக்க வேண்டியதில்லை.",
        "Territorial nexus applies to all state legislative entries under Article 245.", "உறுப்பு 245-ன் கீழ் அனைத்து மாநில சட்டமன்றப் பதிவுகளுக்கும் பிராந்தியத் தொடர்பு பொருந்தும்.",
        "Option D accurately outlines the requirements of the Doctrine of Territorial Nexus in State taxation.", "விருப்பம் D மாநில வரிவிதிப்பில் பிராந்தியத் தொடர்பு கோட்பாட்டின் தேவைகளைத் துல்லியமாக விளக்குகிறது.",
        "Doctrine of Territorial Nexus: Taxing State must have a real and substantial connection with the taxed event, goods, or person.",
        "பிராந்தியத் தொடர்பு கோட்பாடு: வரி விதிக்கும் மாநிலத்திற்கும் வரி விதிக்கப்படும் நிகழ்வு, பொருள் அல்லது நபருக்கும் இடையே உண்மையான மற்றும் கணிசமான தொடர்பு இருக்க வேண்டும்.",
        "Territorial nexus requires a real and substantial connection between the State and the taxed event.",
        "பிராந்தியத் தொடர்பு என்பது மாநிலத்திற்கும் வரி விதிக்கப்பட்ட நிகழ்விற்கும் இடையே உண்மையான தொடர்பைக் கோருகிறது.",
        tags=["Territorial Nexus", "State Taxation", "Article 245"]
    ))

    # 029 - Ans A
    q.append(make_q(
        "ISR_H_029", "Jurisdiction Demarcation",
        "Why did the Supreme Court hold that the dispute between Tamil Nadu and Kerala regarding the safety and water level of the Mullaperiyar Dam fell under Article 131 rather than Article 262 of the Constitution?",
        "முல்லைப் பெரியாறு அணையின் பாதுகாப்பு மற்றும் நீர்மட்டம் தொடர்பான தமிழ்நாடு மற்றும் கேரளா இடையேயான தகராறு அரசியலமைப்பின் உறுப்பு 262-ன் கீழ் வராமல், உறுப்பு 131-ன் கீழ் வருகிறது என்று உச்ச நீதிமன்றம் ஏன் தீர்ப்பளித்தது?",
        "Because the dispute concerned the legal rights, safety, and enforcement of a lease agreement regarding an existing dam structure, rather than a dispute over the use, distribution, or control of the natural waters of an inter-State river.", "ஏனெனில் இத்தகராறு மாநிலங்களுக்கு இடையிலான நதியின் இயற்கை நீரின் பயன்பாடு, பகிர்வு அல்லது கட்டுப்பாடு தொடர்பான தகராறாக இல்லாமல், ஏற்கனவே உள்ள ஓர் அணை கட்டமைப்பின் சட்ட உரிமைகள், பாதுகாப்பு மற்றும் குத்தகை ஒப்பந்தத்தை அமல்படுத்துவது தொடர்பானதாக இருந்தது.",
        "Because Article 262 applies only to rivers flowing through northern India.", "ஏனெனில் உறுப்பு 262 வட இந்தியாவில் பாயும் நதிகளுக்கு மட்டுமே பொருந்தும்.",
        "Because neither Tamil Nadu nor Kerala was a party to the States Reorganisation Act, 1956.", "ஏனெனில் தமிழ்நாடோ அல்லது கேரளாவோ 1956 மாநில மறுசீரமைப்புச் சட்டத்தில் ஒரு தரப்பினராக இருக்கவில்லை.",
        "Because the Supreme Court had already abolished the Cauvery Water Management Authority.", "ஏனெனில் உச்ச நீதிமன்றம் ஏற்கனவே காவிரி நீர் மேலாண்மை ஆணையத்தை ஒழித்துவிட்டது.",
        "A",
        "In State of Tamil Nadu v. State of Kerala (2014, Mullaperiyar case), the Supreme Court held that the suit was maintainable under Article 131. Article 262 and the IRWD Act apply specifically to disputes regarding the 'use, distribution or control' of river waters. A dispute concerning the safety, maintenance, storage capacity, and contractual lease rights of an existing dam is a legal dispute between States falling squarely under the Original Jurisdiction of Article 131.",
        "தமிழ்நாடு vs கேரளா (2014, முல்லைப் பெரியாறு வழக்கு) வழக்கில், வழக்கு உறுப்பு 131-ன் கீழ் செல்லும் என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது. உறுப்பு 262 மற்றும் IRWD சட்டம் நதிநீரின் 'பயன்பாடு, பகிர்வு அல்லது கட்டுப்பாடு' தொடர்பான தகராறுகளுக்கு மட்டுமே பொருந்தும். ஏற்கனவே உள்ள ஓர் அணையின் பாதுகாப்பு, பராமரிப்பு, சேமிப்புத் திறன் மற்றும் ஒப்பந்தக் குத்தகை உரிமைகள் தொடர்பான தகராறு என்பது உறுப்பு 131-ன் மூல அதிகார வரம்பின் கீழ் வரும் மாநிலங்களுக்கிடையேயான சட்டத் தகராறாகும்.",
        "Option A precisely states the distinction between water distribution disputes (Art 262) and dam safety / contractual disputes (Art 131).", "விருப்பம் A நீர் பகிர்வு தகராறுகளுக்கும் (உறுப்பு 262) அணை பாதுகாப்பு / ஒப்பந்தத் தகராறுகளுக்கும் (உறுப்பு 131) இடையிலான வேறுபாட்டைச் சரியாக விளக்குகிறது.",
        "Article 262 applies to all inter-State rivers in India, north and south alike.", "உறுப்பு 262 இந்தியா முழுவதிலும் உள்ள அனைத்து மாநில நதிகளுக்கும் பொருந்தும்.",
        "Both states were created/reorganized under the States Reorganisation Act 1956.", "இரு மாநிலங்களும் 1956 சட்டத்தின் கீழ் மறுசீரமைக்கப்பட்டவை.",
        "CWMA relates to the Cauvery, not Mullaperiyar (which is on the Periyar river).", "CWMA காவிரி தொடர்பானது, பெரியாறு நதி தொடர்பானது அல்ல.",
        "Mullaperiyar Precedent: Dam safety and contractual lease disputes lie under Article 131; water distribution/sharing disputes lie under Article 262.",
        "முல்லைப் பெரியாறு முன்மாதிரி: அணை பாதுகாப்பு மற்றும் குத்தகைத் தகராறுகள் உறுப்பு 131-ன் கீழ் வருகின்றன; நீர் பகிர்வுத் தகராறுகள் உறுப்பு 262-ன் கீழ் வருகின்றன.",
        "Mullaperiyar dispute was decided under Article 131 as a legal rights dispute.",
        "முல்லைப் பெரியாறு தகராறு ஒரு சட்ட உரிமைத் தகராறாக உறுப்பு 131 இன் கீழ் தீர்க்கப்பட்டது.",
        tags=["Mullaperiyar", "Article 131 vs Article 262", "Dam Safety"]
    ))

    # 030 - Ans B
    q.append(make_q(
        "ISR_H_030", "Constitutional Wording Analysis",
        "Why does the non-obstante clause in Article 262(2)—'Notwithstanding anything in this Constitution'—have profound constitutional significance regarding federal dispute adjudication?",
        "உறுப்பு 262(2)-ல் உள்ள 'இந்த அரசியலமைப்பில் என்ன கூறப்பட்டிருப்பினும்' (Notwithstanding anything in this Constitution) என்ற விதிவிலக்கு வாசகம், கூட்டாட்சித் தகராறு தீர்ப்பில் ஏன் ஆழ்ந்த அரசியலமைப்பு முக்கியத்துவத்தைக் கொண்டுள்ளது?",
        "It permits the President to declare martial law in riparian States.", "நதிப் படுகை மாநிலங்களில் இராணுவச் சட்டத்தைப் பிரகடனம் செய்ய இது குடியரசுத் தலைவரை அனுமதிக்கிறது.",
        "It elevates Parliament's power to bar judicial jurisdiction above even Article 131 (which is expressly made 'Subject to the provisions of this Constitution'), establishing that water tribunals supersede ordinary court jurisdiction.", "இது நீதித்துறை அதிகார வரம்பைத் தடுக்கும் நாடாளுமன்றத்தின் அதிகாரத்தை உறுப்பு 131-ஐ விடவும் (இது வெளிப்படையாக 'இந்த அரசியலமைப்பின் விதிகளுக்கு உட்பட்டு' என்று கூறப்பட்டுள்ளது) உயர்த்துகிறது, மேலும் நதிநீர் தீர்ப்பாயங்கள் சாதாரண நீதிமன்ற அதிகார வரம்பை விஞ்சுகின்றன என்பதை நிறுவுகிறது.",
        "It completely immunizes the Inter-State Council from parliamentary oversight.", "இது மாநிலங்களுக்கு இடையிலான மன்றத்தை நாடாளுமன்ற மேற்பார்வையிலிருந்து முற்றிலும் பாதுகாக்கிறது.",
        "It allows State Governments to disregard all international environmental treaties.", "அனைத்து சர்வதேச சுற்றுச்சூழல் ஒப்பந்தங்களையும் புறக்கணிக்க இது மாநில அரசுகளை அனுமதிக்கிறது.",
        "B",
        "Article 131 begins with the qualifying words 'Subject to the provisions of this Constitution...', making its original jurisdiction subordinate to other constitutional provisions. In sharp contrast, Article 262(2) begins with the overriding non-obstante clause 'Notwithstanding anything in this Constitution, Parliament may by law provide that neither the Supreme Court nor any other court shall exercise jurisdiction...'. Thus, by constitutional design, Article 262(2) overrides Article 131.",
        "உறுப்பு 131 'இந்த அரசியலமைப்பின் விதிகளுக்கு உட்பட்டு...' என்ற தகுதிவாய்ந்த சொற்களுடன் தொடங்குகிறது, இதனால் அதன் மூல அதிகார வரம்பு பிற அரசியலமைப்பு விதிகளுக்குக் கீழானதாகிறது. ஆனால், உறுப்பு 262(2) 'இந்த அரசியலமைப்பில் என்ன கூறப்பட்டிருப்பினும், உச்ச நீதிமன்றமோ அல்லது வேறு எந்த நீதிமன்றமோ அதிகார வரம்பைச் செலுத்தக் கூடாது என்று நாடாளுமன்றம் சட்டம் மூலம் வகை செய்யலாம்...' என்ற விஞ்சும் வாசகத்துடன் தொடங்குகிறது. எனவே, உறுப்பு 262(2) உறுப்பு 131-ஐ விஞ்சுகிறது.",
        "It has nothing to do with martial law under Article 34.", "இதற்கும் உறுப்பு 34-ன் கீழான இராணுவச் சட்டத்திற்கும் தொடர்பில்லை.",
        "Option B correctly explains the constitutional hierarchy where Art 262(2) overrides Art 131 due to the non-obstante clause.", "விருப்பம் B விதிவிலக்கு வாசகம் காரணமாக உறுப்பு 262(2) உறுப்பு 131-ஐ எவ்வாறு விஞ்சுகிறது என்பதைச் சரியாக விளக்குகிறது.",
        "It does not relate to the Inter-State Council (which is under Art 263).", "இது மாநிலங்களுக்கு இடையிலான மன்றத்துடன் தொடர்புடையது அல்ல.",
        "States cannot disregard international treaties (Article 253).", "மாநிலங்கள் சர்வதேச ஒப்பந்தங்களைப் புறக்கணிக்க முடியாது (உறுப்பு 253).",
        "Constitutional Hierarchy: Art 131 is 'Subject to the provisions of this Constitution'; Art 262(2) is 'Notwithstanding anything in this Constitution' -> Art 262(2) prevails.",
        "அரசியலமைப்புப் படிநிலை: உறுப்பு 131 'விதிகளுக்கு உட்பட்டது'; உறுப்பு 262(2) 'என்ன கூறப்பட்டிருப்பினும் விஞ்சக்கூடியது' -> உறுப்பு 262(2) மேலோங்குகிறது.",
        "Article 262(2) non-obstante clause overrides Article 131 original jurisdiction.",
        "உறுப்பு 262(2) விதிவிலக்கு வாசகம் உறுப்பு 131 மூல அதிகார வரம்பை விஞ்சுகிறது.",
        tags=["Article 262(2)", "Article 131", "Non-obstante Clause"]
    ))

    # 031 - Ans C
    q.append(make_q(
        "ISR_H_031", "Constitutional Interplay",
        "How do Articles 19(6)(ii), 301, and 305 interact when a State Government creates an exclusive monopoly in passenger road transport services, completely excluding private bus operators?",
        "ஒரு மாநில அரசு தனியார் பேருந்து இயக்குநர்களை முற்றிலும் விலக்கி, பயணிகள் சாலைப் போக்குவரத்துச் சேவைகளில் ஒரு பிரத்யேக ஏகபோகத்தை உருவாக்கும் போது, உறுப்புகள் 19(6)(ii), 301 மற்றும் 305 ஆகியவை எவ்வாறு ஒன்றோடொன்று இணைகின்றன?",
        "The State monopoly violates Article 19(1)(g) and cannot be defended under any circumstances.", "அரசு ஏகபோகம் உறுப்பு 19(1)(g)-ஐ மீறுகிறது மற்றும் எந்தச் சூழ்நிலையிலும் பாதுகாக்கப்பட முடியாது.",
        "Private bus operators have an absolute fundamental right under Article 301 that supersedes state nationalization laws.", "தனியார் பேருந்து இயக்குநர்களுக்கு உறுப்பு 301-ன் கீழ் முழுமையான அடிப்படை உரிமை உள்ளது, இது மாநில தேசியமயமாக்கல் சட்டங்களை விஞ்சுகிறது.",
        "Article 19(6)(ii) protects the State monopoly against Article 19(1)(g), while Article 305 saves the State monopoly law from challenge under Article 301, making the nationalization constitutionally impregnable.", "உறுப்பு 19(6)(ii) அரசு ஏகபோகத்தை உறுப்பு 19(1)(g)-க்கு எதிராகப் பாதுகாக்கிறது, அதே சமயம் உறுப்பு 305 அரசு ஏகபோகச் சட்டத்தை உறுப்பு 301-ன் கீழான சவாலிலிருந்து பாதுகாக்கிறது; இதனால் தேசியமயமாக்கல் அரசியலமைப்பு ரீதியாக அசைக்க முடியாததாகிறது.",
        "State monopolies can be created only if ratified by a special resolution of the Inter-State Council.", "மாநிலங்களுக்கு இடையிலான மன்றத்தின் சிறப்புத் தீர்மானத்தால் அங்கீகரிக்கப்பட்டால் மட்டுமே அரசு ஏகபோகங்களை உருவாக்க முடியும்.",
        "C",
        "The constitutional interplay is twofold: (1) Under Article 19(6)(ii), state monopoly legislation is completely protected against the fundamental right under Article 19(1)(g) without having to prove reasonableness; (2) Under Article 305, state monopoly laws are expressly saved from the operation of Article 301. Together, these provisions grant complete constitutional immunity to State monopolies in trade, commerce, and industry.",
        "அரசியலமைப்பு இணைப்பு இரு மடங்கு ஆகும்: (1) உறுப்பு 19(6)(ii)-ன் கீழ், அரசு ஏகபோகச் சட்டம் நியாயத்தன்மையை நிரூபிக்க வேண்டிய அவசியமின்றி உறுப்பு 19(1)(g)-ன் கீழான அடிப்படை உரிமைக்கு எதிராகப் பாதுகாக்கப்படுகிறது; (2) உறுப்பு 305-ன் கீழ், அரசு ஏகபோகச் சட்டங்கள் உறுப்பு 301-ன் செயல்பாட்டிலிருந்து வெளிப்படையாகப் பாதுகாக்கப்படுகின்றன. இரண்டும் சேர்ந்து அரசு ஏகபோகங்களுக்கு முழுமையான அரசியலமைப்புப் பாதுகாப்பை வழங்குகின்றன.",
        "State monopolies are explicitly permitted by Article 19(6)(ii).", "அரசு ஏகபோகங்கள் உறுப்பு 19(6)(ii)-ஆல் வெளிப்படையாக அனுமதிக்கப்படுகின்றன.",
        "Article 301 does not override Article 305.", "உறுப்பு 301 உறுப்பு 305-ஐ விஞ்சாது.",
        "Option C accurately synthesizes the dual protection of State monopolies under Art 19(6)(ii) and Art 305.", "விருப்பம் C உறுப்புகள் 19(6)(ii) மற்றும் 305-ன் கீழ் அரசு ஏகபோகங்களின் இரட்டைப் பாதுகாப்பைத் துல்லியமாக விளக்குகிறது.",
        "The Inter-State Council has no role in approving State monopolies.", "அரசு ஏகபோகங்களை அங்கீகரிப்பதில் மாநிலங்களுக்கு இடையிலான மன்றத்திற்குப் பங்கில்லை.",
        "Dual Immunity for State Monopolies: Article 19(6)(ii) immunizes against Art 19(1)(g); Article 305 immunizes against Art 301.",
        "அரசு ஏகபோகங்களுக்கான இரட்டைப் பாதுகாப்பு: உறுப்பு 19(6)(ii) உறுப்பு 19(1)(g)-லிருந்தும்; உறுப்பு 305 உறுப்பு 301-லிருந்தும் பாதுகாக்கிறது.",
        "State monopolies are protected by Article 19(6)(ii) and Article 305.",
        "அரசு ஏகபோகங்கள் உறுப்பு 19(6)(ii) மற்றும் உறுப்பு 305 ஆல் பாதுகாக்கப்படுகின்றன.",
        tags=["State Monopolies", "Article 305", "Article 19(6)(ii)"]
    ))

    # 032 - Ans D
    q.append(make_q(
        "ISR_H_032", "Taxation Interplay",
        "How do Article 286 and Part XIII (Articles 301–304) coordinate regarding the State's power to levy sales tax on inter-State sales?",
        "மாநிலங்களுக்கு இடையிலான விற்பனையின் மீது விற்பனை வரி விதிக்கும் மாநிலத்தின் அதிகாரம் தொடர்பாக உறுப்பு 286 மற்றும் பகுதி XIII (உறுப்புகள் 301-304) எவ்வாறு ஒருங்கிணைக்கப்படுகின்றன?",
        "Article 286 allows individual States to levy unlimited sales tax on goods exiting their borders.", "உறுப்பு 286 தனிப்பட்ட மாநிலங்கள் தங்கள் எல்லைகளை விட்டு வெளியேறும் பொருட்களின் மீது வரம்பற்ற விற்பனை வரி விதிக்க அனுமதிக்கிறது.",
        "Part XIII completely strips Parliament of all power to regulate inter-State sales taxation.", "பகுதி XIII மாநிலங்களுக்கு இடையிலான விற்பனை வரிவிதிப்பை ஒழுங்குபடுத்தும் அனைத்து அதிகாரத்தையும் நாடாளுமன்றத்திடமிருந்து முற்றிலும் பறிக்கிறது.",
        "States can tax inter-State sales only if approved unanimously by the Southern Zonal Council.", "தென் மண்டலக் குழுவால் ஒருமனதாக அங்கீகரிக்கப்பட்டால் மட்டுமே மாநிலங்கள் மாநிலங்களுக்கு இடையிலான விற்பனைக்கு வரி விதிக்க முடியும்.",
        "Article 286(1) bars States from taxing sales taking place outside the State or in the course of import/export, while Article 286(2) authorizes Parliament to formulate principles defining inter-State sales, harmonizing with Part XIII's mandate of economic unity.", "உறுப்பு 286(1) மாநிலத்திற்கு வெளியே அல்லது இறக்குமதி/ஏற்றுமதியின் போது நடைபெறும் விற்பனை மீது மாநிலங்கள் வரி விதிப்பதைத் தடுக்கிறது; அதே சமயம் உறுப்பு 286(2) மாநிலங்களுக்கு இடையிலான விற்பனையை வரையறுக்கும் கொள்கைகளை உருவாக்க நாடாளுமன்றத்திற்கு அதிகாரம் அளித்து, பகுதி XIII-ன் பொருளாதார ஒற்றுமை விதியுடன் இணக்கமடைகிறது.",
        "D",
        "Article 286 acts as a constitutional barrier on State taxing power: (1) No State can tax a sale outside the State or in the course of import/export; (2) Parliament alone can declare what constitutes an inter-State sale (exercised via Central Sales Tax Act 1956). This complements Part XIII's objective of preserving India as a single common economic market without interstate tariff walls.",
        "உறுப்பு 286 மாநில வரி அதிகாரத்தின் மீது ஓர் அரசியலமைப்புத் தடையாகச் செயல்படுகிறது: (1) மாநிலத்திற்கு வெளியே அல்லது இறக்குமதி/ஏற்றுமதியின் போது நடைபெறும் விற்பனைக்கு எந்த மாநிலமும் வரி விதிக்க முடியாது; (2) மாநிலங்களுக்கு இடையிலான விற்பனை எது என்பதை நாடாளுமன்றம் மட்டுமே அறிவிக்க முடியும் (1956 மத்திய விற்பனை வரிச் சட்டம் மூலம்). இது சுங்கச் சுவர்கள் இல்லாத ஒற்றைப் பொதுச் சந்தையாக இந்தியாவைப் பேணும் பகுதி XIII-ன் நோக்கத்தை நிறைவு செய்கிறது.",
        "States cannot levy export taxes on goods exiting borders (barred by Art 286).", "மாநிலங்கள் எல்லை தாண்டும் பொருட்களுக்கு வரி விதிக்க முடியாது.",
        "Part XIII harmonizes with Parliament's regulatory power, not strip it.", "பகுதி XIII நாடாளுமன்ற அதிகாரத்துடன் இணங்குகிறது.",
        "Zonal Councils have no taxation approval authority.", "மண்டலக் குழுக்களுக்கு வரி ஒப்புதல் அதிகாரம் இல்லை.",
        "Option D accurately reflects the constitutional harmonization between Article 286 and Part XIII.", "விருப்பம் D உறுப்பு 286 மற்றும் பகுதி XIII ஆகியவற்றுக்கு இடையேயான அரசியலமைப்பு இணக்கத்தைத் துல்லியமாக விளக்குகிறது.",
        "Economic Unity Architecture: Article 286 bars State taxation of inter-State sales, complementing Part XIII freedom of trade.",
        "பொருளாதார ஒற்றுமைக் கட்டமைப்பு: உறுப்பு 286 மாநிலங்களுக்கு இடையிலான விற்பனை மீதான மாநில வரிவிதிப்பைத் தடுக்கிறது, இது பகுதி XIII வர்த்தக சுதந்திரத்தை நிறைவு செய்கிறது.",
        "Article 286 coordinates with Part XIII to maintain a single national market.",
        "உறுப்பு 286 ஒற்றைத் தேசியச் சந்தையைப் பராமரிக்க பகுதி XIII உடன் ஒருங்கிணைக்கிறது.",
        tags=["Article 286", "Part XIII", "Inter-State Sales Tax"]
    ))

    # 033 - Ans A
    q.append(make_q(
        "ISR_H_033", "Commission Recommendation",
        "What specific reform did the Sarkaria Commission (1988) recommend regarding the implementation of awards delivered by Inter-State Water Disputes Tribunals under the IRWD Act?",
        "IRWD சட்டத்தின் கீழ் நதிநீர் தகராறுகள் தீர்ப்பாயங்களால் வழங்கப்படும் தீர்ப்புகளைச் செயல்படுத்துவது தொடர்பாக சர்க்காரியா ஆணையம் (1988) என்ன குறிப்பிட்ட சீர்திருத்தத்தைப் பரிந்துரைத்தது?",
        "The tribunal award should have the same force as a decree of the Supreme Court and should become automatically effective within a specified period without requiring central executive discretion.", "தீர்ப்பாயத் தீர்ப்பு உச்ச நீதிமன்றத்தின் தீர்ப்பாணைக்கு இணையான அதே ஆற்றலைக் கொண்டிருக்க வேண்டும் மற்றும் மத்திய நிர்வாகத் தன்னிச்சையான முடிவு தேவையின்றி ஒரு குறிப்பிட்ட காலத்திற்குள் தானாகவே நடைமுறைக்கு வர வேண்டும்.",
        "The tribunal award should be subject to mandatory approval by a joint session of Parliament.", "தீர்ப்பாயத் தீர்ப்பிற்கு நாடாளுமன்றத்தின் கூட்டுக் கூட்டத்தில் கட்டாய ஒப்புதல் பெறப்பட வேண்டும்.",
        "All tribunal awards should be reviewed by the Comptroller and Auditor General before notification.", "அனைத்து தீர்ப்பாயத் தீர்ப்புகளும் அறிவிக்கப்படுவதற்கு முன் தலைமை கணக்குத் தணிக்கையாளரால் மறுஆய்வு செய்யப்பட வேண்டும்.",
        "Tribunal awards should be advisory for the first 10 years before becoming binding.", "தீர்ப்பாயத் தீர்ப்புகள் கட்டுப்படுத்துவதற்கு முன் முதல் 10 ஆண்டுகளுக்கு ஆலோசனையாக மட்டுமே இருக்க வேண்டும்.",
        "A",
        "The Sarkaria Commission recommended that the decision of a water tribunal should have the same force and effect as an order or decree of the Supreme Court, and that there should be a statutory provision for its automatic gazetting/enforcement within a fixed period, preventing the Central Government from indefinitely delaying publication of awards due to political pressure. This recommendation directly inspired the 2002 amendment to the IRWD Act (Section 6(2)).",
        "நதிநீர் தீர்ப்பாயத்தின் முடிவு உச்ச நீதிமன்றத்தின் ஆணை அல்லது தீர்ப்பாணைக்கு இணையான ஆற்றலையும் விளைவையும் கொண்டிருக்க வேண்டும் என்றும், அரசியல் அழுத்தம் காரணமாக மத்திய அரசு தீர்ப்புகளை வெளியிடுவதைத் தாமதப்படுத்துவதைத் தடுக்க ஒரு குறிப்பிட்ட காலத்திற்குள் தானாக அரசிதழில் வெளியிடப்பட்டு அமல்படுத்த சட்டப்பூர்வ விதி இருக்க வேண்டும் என்றும் சர்க்காரியா ஆணையம் பரிந்துரைத்தது. இந்தப் பரிந்துரையே 2002-ன் IRWD திருத்தத்திற்கு (பிரிவு 6(2)) வித்திட்டது.",
        "Option A directly articulates Sarkaria's recommendation which was enacted in the 2002 amendment.", "விருப்பம் A 2002 திருத்தத்தில் இயற்றப்பட்ட சர்க்காரியா ஆணையத்தின் பரிந்துரையைத் துல்லியமாக விளக்குகிறது.",
        "Parliamentary joint session approval was not recommended.", "நாடாளுமன்றக் கூட்டுக் கூட்ட ஒப்புதல் பரிந்துரைக்கப்படவில்லை.",
        "CAG has no role in judicial tribunal awards.", "நீதிமன்றத் தீர்ப்புகளில் CAG-க்கு எந்தப் பங்கும் இல்லை.",
        "Ten-year advisory delay was never proposed.", "பத்து ஆண்டு ஆலோசனைத் தாமதம் ஒருபோதும் முன்மொழியப்படவில்லை.",
        "Sarkaria Commission Recommendation: Tribunal award = Supreme Court Decree (enacted via Section 6(2) of IRWD Act in 2002).",
        "சர்க்காரியா ஆணையப் பரிந்துரை: தீர்ப்பாயத் தீர்ப்பு = உச்ச நீதிமன்றத் தீர்ப்பாணை (2002-ல் IRWD சட்டத்தின் பிரிவு 6(2) மூலம் இயற்றப்பட்டது).",
        "Sarkaria Commission recommended tribunal awards have the force of an SC decree.",
        "தீர்ப்பாயத் தீர்ப்புகள் உச்ச நீதிமன்றத் தீர்ப்பாணையின் ஆற்றலைக் கொண்டிருக்க வேண்டும் என்று சர்க்காரியா ஆணையம் பரிந்துரைத்தது.",
        tags=["Sarkaria Commission", "IRWD Act 2002", "SC Decree Equivalence"]
    ))

    # 034 - Ans B
    q.append(make_q(
        "ISR_H_034", "Multi-Forum Comparison",
        "Match the federal dispute resolution forum in Column I with its primary constitutional/statutory basis in Column II:\nColumn I:\n1. Adjudication of Legal Disputes between Union and States\n2. Adjudication of Inter-State River Water Disputes\n3. Coordination and Policy Consultation between States\n4. Regional Planning and Development of North Eastern States\nColumn II:\na. Article 263\nb. Article 131\nc. North Eastern Council Act, 1971\nd. Article 262 / IRWD Act, 1956\nWhich is the correct match?",
        "பத்தி I-ல் உள்ள கூட்டாட்சித் தகராறு தீர்வு மன்றத்தைப் பத்தி II-ல் உள்ள அதன் முதன்மை அரசியலமைப்பு/சட்டப்பூர்வ அடிப்படையுடன் பொருத்துக:\nபத்தி I:\n1. ஒன்றியம் மற்றும் மாநிலங்களுக்கிடையேயான சட்டத் தகராறுகளின் தீர்ப்பு\n2. மாநிலங்களுக்கு இடையிலான நதிநீர் தகராறுகளின் தீர்ப்பு\n3. மாநிலங்களுக்கிடையேயான ஒருங்கிணைப்பு மற்றும் கொள்கை ஆலோசனை\n4. வடகிழக்கு மாநிலங்களின் பிராந்திய திட்டமிடல் மற்றும் வளர்ச்சி\nபத்தி II:\na. உறுப்பு 263\nb. உறுப்பு 131\nc. வடகிழக்கு கவுன்சில் சட்டம், 1971\nd. உறுப்பு 262 / IRWD சட்டம், 1956\nசரியான பொருத்தம் எது?",
        "1-a, 2-d, 3-b, 4-c", "1-a, 2-d, 3-b, 4-c",
        "1-b, 2-d, 3-a, 4-c", "1-b, 2-d, 3-a, 4-c",
        "1-b, 2-a, 3-d, 4-c", "1-b, 2-a, 3-d, 4-c",
        "1-d, 2-b, 3-c, 4-a", "1-d, 2-b, 3-c, 4-a",
        "B",
        "The correct constitutional mapping is: (1) Adjudication of Legal Disputes between Union and States = Article 131 (Supreme Court Original Jurisdiction); (2) Adjudication of Inter-State River Water Disputes = Article 262 / IRWD Act 1956; (3) Coordination and Policy Consultation = Article 263 (Inter-State Council); (4) Regional Planning of North Eastern States = North Eastern Council Act, 1971. Thus, 1-b, 2-d, 3-a, 4-c.",
        "சரியான அரசியலமைப்புப் பொருத்தம்: (1) ஒன்றியம் மற்றும் மாநிலங்களுக்கிடையேயான சட்டத் தகராறுகள் = உறுப்பு 131 (உச்ச நீதிமன்ற மூல அதிகார வரம்பு); (2) நதிநீர் தகராறுகள் = உறுப்பு 262 / IRWD சட்டம் 1956; (3) ஒருங்கிணைப்பு மற்றும் கொள்கை ஆலோசனை = உறுப்பு 263 (மாநிலங்களுக்கு இடையிலான மன்றம்); (4) வடகிழக்கு மாநிலங்களின் திட்டமிடல் = வடகிழக்கு கவுன்சில் சட்டம், 1971. எனவே, 1-b, 2-d, 3-a, 4-c.",
        "Option A incorrectly pairs Art 263 with legal adjudication.", "விருப்பம் A உறுப்பு 263-ஐ சட்டத் தீர்ப்புடன் தவறாக இணைக்கிறது.",
        "Option B correctly pairs all four institutional forums with their exact constitutional/statutory authorities.", "விருப்பம் B நான்கு நிறுவனங்களையும் அவற்றின் அதிகாரங்களுடன் சரியாகப் பொருத்துகிறது.",
        "Option C incorrectly swaps Art 263 and Art 262.", "விருப்பம் C உறுப்பு 263 மற்றும் 262-ஐ மாற்றிக் காட்டுகிறது.",
        "Option D is completely inverted.", "விருப்பம் D முற்றிலும் தலைகீழானது.",
        "Federal Forums Mapping: Legal Disputes -> Art 131; Water Disputes -> Art 262; Coordination -> Art 263; Regional Planning -> NEC Act 1971.",
        "கூட்டாட்சி மன்றங்கள் பொருத்தம்: சட்டத் தகராறு -> உறுப்பு 131; நதிநீர் -> உறுப்பு 262; ஒருங்கிணைப்பு -> உறுப்பு 263; பிராந்திய திட்டமிடல் -> NEC சட்டம் 1971.",
        "Correct match: 1-b, 2-d, 3-a, 4-c.",
        "சரியான பொருத்தம்: 1-b, 2-d, 3-a, 4-c.",
        tags=["Matching", "Federal Forums", "Constitutional Articles"]
    ))

    # 035 - Ans C
    q.append(make_q(
        "ISR_H_035", "Judicial Analysis",
        "In Jindal Stainless Ltd. (2016), how did the Supreme Court interpret the concept of 'discrimination' under Article 304(a) when local goods and imported goods are subject to different tax mechanisms?",
        "ஜின்டால் ஸ்டெயின்லெஸ் லிமிடெட் (2016) வழக்கில், உள்ளூர் பொருட்களும் இறக்குமதி செய்யப்பட்ட பொருட்களும் வெவ்வேறு வரி வழிமுறைகளுக்கு உட்படுத்தப்படும் போது, உறுப்பு 304(a)-ன் கீழான 'பாகுபாடு' என்ற கருத்தை உச்ச நீதிமன்றம் எவ்வாறு விளக்கியது?",
        "Any difference in administrative collection procedure automatically proves hostile discrimination.", "நிர்வாக வசூல் நடைமுறையில் உள்ள எந்தவொரு வேறுபாடும் தானாகவே விரோதமான பாகுபாட்டை நிரூபிக்கிறது.",
        "Discrimination can be claimed only by foreign governments, not by Indian domestic traders.", "பாகுபாட்டை வெளிநாட்டு அரசாங்கங்கள் மட்டுமே கோர முடியும், இந்திய உள்நாட்டு வர்த்தகர்கள் கோர முடியாது.",
        "Discrimination must be determined by looking at the overall substantive tax burden, not merely nomenclature; if local goods bear an equivalent tax burden under other state taxes (like local sales tax/VAT), an entry tax on imported goods to equalize the tax burden does not constitute unconstitutional discrimination.", "பாகுபாடு என்பது வெறும் பெயரளவில் பார்க்கப்படாமல், ஒட்டுமொத்த கணிசமான வரிச் சுமையைப் பார்த்து தீர்மானிக்கப்பட வேண்டும்; உள்ளூர் பொருட்கள் பிற மாநில வரிகளின் கீழ் (விற்பனை வரி/வாட் போன்றவை) இணையான வரிச் சுமையைச் சுமந்தால், வரிச் சுமையை சமப்படுத்த இறக்குமதி பொருட்கள் மீது விதிக்கப்படும் நுழைவு வரி அரசியலமைப்பிற்கு முரணான பாகுபாடாக அமையாது.",
        "Discrimination is permitted if recommended by a resolution of the Zonal Council.", "மண்டலக் குழுவின் தீர்மானத்தால் பரிந்துரைக்கப்பட்டால் பாகுபாடு அனுமதிக்கப்படுகிறது.",
        "C",
        "In Jindal Stainless (2016), the 9-judge bench clarified that to determine whether an entry tax under Article 304(a) discriminates against imported goods, the court must look at the overall tax burden borne by similar local goods. If local goods bear an equal or higher tax under other state tax enactments (such as local VAT/sales tax from which imported goods were exempt at origin), levying an entry tax on imported goods merely levels the playing field and is NOT discriminatory.",
        "ஜின்டால் ஸ்டெயின்லெஸ் (2016) வழக்கில், 9 நீதிபதிகள் அமர்வு, உறுப்பு 304(a)-ன் கீழான நுழைவு வரி இறக்குமதி செய்யப்பட்ட பொருட்களுக்கு எதிராகப் பாகுபாடு காட்டுகிறதா என்பதைத் தீர்மானிக்க, உள்ளூர் பொருட்கள் சுமக்கும் ஒட்டுமொத்த வரிச் சுமையை நீதிமன்றம் பார்க்க வேண்டும் என்று தெளிவுபடுத்தியது. உள்ளூர் பொருட்கள் பிற வரிகளின் கீழ் சமமான சுமையைச் சுமக்கும் போது, இறக்குமதி பொருட்கள் மீது நுழைவு வரி விதிப்பது சமநிலையை ஏற்படுத்துவதே தவிர, பாகுபாடு அல்ல.",
        "Procedural differences alone do not establish unconstitutional discrimination.", "நடைமுறை வேறுபாடுகள் மட்டுமே அரசியலமைப்பு முரணான பாகுபாட்டை ஏற்படுத்தாது.",
        "Domestic traders have full standing under Article 304(a).", "உள்நாட்டு வர்த்தகர்களுக்கு உறுப்பு 304(a)-ன் கீழ் முழு உரிமை உண்டு.",
        "Option C accurately presents the 'overall tax burden' equalization test established in Jindal Stainless.", "விருப்பம் C ஜின்டால் ஸ்டெயின்லெஸ் வழக்கில் நிறுவப்பட்ட 'ஒட்டுமொத்த வரிச் சுமை' சமன்பாட்டுத் தேர்வைத் துல்லியமாக விளக்குகிறது.",
        "Zonal Councils cannot authorize tax discrimination.", "மண்டலக் குழுக்கள் வரிப் பாகுபாட்டை அனுமதிக்க முடியாது.",
        "Jindal Stainless (2016) Test: Substantive equivalence of tax burden. Levying entry tax to equalize tax burden with local goods is NOT discriminatory under Article 304(a).",
        "ஜின்டால் ஸ்டெயின்லெஸ் (2016) தேர்வு: வரிச் சுமையின் கணிசமான சமநிலை. உள்ளூர் பொருட்களுடன் வரிச் சுமையை சமப்படுத்த நுழைவு வரி விதிப்பது பாகுபாடு அல்ல.",
        "Equalizing tax burden does not constitute discrimination under Art 304(a).",
        "வரிச் சுமையை சமப்படுத்துவது உறுப்பு 304(a) இன் கீழ் பாகுபாடாகாது.",
        tags=["Jindal Stainless 2016", "Article 304(a)", "Substantive Equivalence"]
    ))

    # 036 - Ans D
    q.append(make_q(
        "ISR_H_036", "Statutory Implementation",
        "How has Parliament exercised its legislative power under Article 261(2) to prescribe the mode of proof for public acts and judicial records of States throughout India?",
        "இந்தியா முழுவதிலும் உள்ள மாநிலங்களின் பொதுச் சட்டங்கள் மற்றும் நீதித்துறைப் பதிவேடுகளுக்கான நிரூபிக்கும் முறையை பரிந்துரைக்க உறுப்பு 261(2)-ன் கீழான தனது சட்டமன்ற அதிகாரத்தை நாடாளுமன்றம் எவ்வாறு செயல்படுத்தியுள்ளது?",
        "By issuing executive circulars through the Inter-State Council Secretariat.", "மாநிலங்களுக்கு இடையிலான மன்றச் செயலகம் மூலம் நிர்வாகச் சுற்றறிக்கைகளை வெளியிடுவதன் மூலம்.",
        "By authorizing each High Court Chief Justice to create independent local rules.", "சுயாதீன உள்ளூர் விதிகளை உருவாக்க ஒவ்வொரு உயர் நீதிமன்றத் தலைமை நீதிபதிக்கும் அதிகாரம் அளிப்பதன் மூலம்.",
        "Parliament has not enacted any legislation under Article 261(2) till date.", "நாடாளுமன்றம் உறுப்பு 261(2)-ன் கீழ் இதுவரை எந்தச் சட்டத்தையும் இயற்றவில்லை.",
        "Through statutory enactments such as the Indian Evidence Act (provisions on public documents and judicial notice) and the Code of Civil Procedure (provisions on execution of foreign domestic decrees under Sections 43 and 44).", "இந்திய சாட்சியச் சட்டம் (பொது ஆவணங்கள் மற்றும் நீதிமன்றக் குறிப்பு மீதான விதிகள்) மற்றும் உரிமையியல் நடைமுறைச் சட்டம் (பிரிவுகள் 43 மற்றும் 44-ன் கீழ் உள்நாட்டுத் தீர்ப்புகளை நிறைவேற்றுவது தொடர்பான விதிகள்) போன்ற சட்டப்பூர்வச் சட்டங்கள் மூலம்.",
        "D",
        "Parliament fulfilled the mandate of Article 261(2) through federal procedural statutes: the Indian Evidence Act, 1872 (Sections 74-81 on public documents, legislative acts, and official gazettes of all States) and the Code of Civil Procedure, 1908 (Sections 43, 44, and Order XXI governing the execution of decrees passed by civil courts of one State across other States).",
        "நாடாளுமன்றம் உறுப்பு 261(2)-ன் ஆணையை கூட்டாட்சி நடைமுறைச் சட்டங்கள் மூலம் நிறைவேற்றியுள்ளது: இந்திய சாட்சியச் சட்டம் (பொது ஆவணங்கள், சட்டமன்றச் சட்டங்கள் மற்றும் அரசிதழ்கள் மீதான பிரிவுகள் 74-81) மற்றும் உரிமையியல் நடைமுறைச் சட்டம் (பிரிவுகள் 43, 44 மற்றும் கட்டளை XXI - ஒரு மாநிலத்தின் உரிமையியல் நீதிமன்றத் தீர்ப்புகளைப் பிற மாநிலங்களில் நிறைவேற்றுவது தொடர்பானவை).",
        "Executive circulars cannot substitute for parliamentary statutes under Art 261(2).", "நிர்வாகச் சுற்றறிக்கைகள் நாடாளுமன்றச் சட்டங்களுக்கு மாற்றாக முடியாது.",
        "Individual High Courts do not legislate evidentiary statutes for India.", "உயர் நீதிமன்றங்கள் இந்தியா முழுவதற்குமான சாட்சியச் சட்டங்களை இயற்றுவதில்லை.",
        "Parliament has enacted and adapted comprehensive procedural codes.", "நாடாளுமன்றம் விரிவான நடைமுறைச் சட்டங்களை இயற்றி மாற்றியமைத்துள்ளது.",
        "Option D accurately identifies the Indian Evidence Act and CPC as the statutory vehicles carrying out Article 261(2).", "விருப்பம் D இந்திய சாட்சியச் சட்டம் மற்றும் சிபிசி ஆகியவற்றை உறுப்பு 261(2)-ஐ நிறைவேற்றும் சட்டக் கருவிகளாகச் சரியாக அடையாளம் காட்டுகிறது.",
        "Statutory Proof under Art 261(2): Indian Evidence Act (public documents proof) + CPC (civil decree inter-state execution).",
        "உறுப்பு 261(2)-ன் கீழான சட்டப்பூர்வச் சான்று: இந்திய சாட்சியச் சட்டம் + உரிமையியல் நடைமுறைச் சட்டம் (CPC).",
        "Article 261(2) is implemented via Evidence Act and Code of Civil Procedure.",
        "உறுப்பு 261(2) சாட்சியச் சட்டம் மற்றும் உரிமையியல் நடைமுறைச் சட்டம் மூலம் செயல்படுத்தப்படுகிறது.",
        tags=["Article 261(2)", "Evidence Act", "CPC"]
    ))

    # 037 - Ans A
    q.append(make_q(
        "ISR_H_037", "Authority Powers Analysis",
        "What are the statutory powers and composition of the Cauvery Water Regulation Committee (CWRC) constituted under the Cauvery Water Management Scheme, 2018?",
        "காவிரி நீர் மேலாண்மைத் திட்டம் 2018-ன் கீழ் அமைக்கப்பட்ட காவிரி நீர் ஒழுங்குமுறைக் குழுவின் (CWRC) சட்டப்பூர்வ அதிகாரங்கள் மற்றும் அமைப்பு என்ன?",
        "It is a technical sub-body headed by a Central Water Commission officer that monitors daily water releases, rainfall, reservoir levels, and inflows, submitting periodic compliance reports to the CWMA.", "இது மத்திய நீர் ஆணைய அதிகாரியைத் தலைவராகக் கொண்ட ஒரு தொழில்நுட்பத் துணை அமைப்பாகும், இது தினசரி நீர் வெளியேற்றம், மழைப்பொழிவு, நீர்த்தேக்க அளவுகள் மற்றும் நீர்வரத்து ஆகியவற்றைக் கண்காணித்து, CWMA-விடம் அவ்வப்போது இணக்க அறிக்கைகளைச் சமர்ப்பிக்கிறது.",
        "It is an autonomous court of record with plenary power to punish defaulting Chief Ministers with imprisonment.", "இது தவறிழைக்கும் முதலமைச்சர்களைச் சிறைத்தண்டனையுடன் தண்டிக்க முழு அதிகாரம் கொண்ட ஒரு தன்னாட்சிப் பதிவு நீதிமன்றமாகும்.",
        "It is a political council composed exclusively of the Governors of the riparian States.", "இது நதிப் படுகை மாநிலங்களின் ஆளுநர்களை மட்டுமே கொண்ட ஓர் அரசியல் மன்றமாகும்.",
        "It is an environmental NGO financed entirely by international climate funds.", "இது சர்வதேச காலநிலை நிதிகளால் முழுமையாக நிதியளிக்கப்படும் ஒரு சுற்றுச்சூழல் தன்னார்வ தொண்டு நிறுவனமாகும்.",
        "A",
        "Under the Cauvery Water Management Scheme 2018 (notified under Section 6A of the IRWD Act), the Cauvery Water Regulation Committee (CWRC) was established as a technical assisting body to the CWMA. It is headed by a Chief Engineer of the Central Water Commission and comprises representatives of the riparian States and India Meteorological Department. It monitors daily inflows, reservoir storages, and discharges on the ground, advising the CWMA.",
        "காவிரி நீர் மேலாண்மைத் திட்டம் 2018-ன் கீழ் (IRWD சட்டத்தின் பிரிவு 6A-ன் கீழ் அறிவிக்கப்பட்டது), CWMA-வுக்கு தொழில்நுட்ப உதவி அமைப்பாக காவிரி நீர் ஒழுங்குமுறைக் குழு (CWRC) அமைக்கப்பட்டது. இது மத்திய நீர் ஆணையத்தின் தலைமைப் பொறியாளரைத் தலைவராகக் கொண்டு, படுகை மாநிலங்கள் மற்றும் வானிலை ஆய்வுத் துறையின் பிரதிநிதிகளை உள்ளடக்கியுள்ளது. இது தினசரி நீர்வரத்து, சேமிப்பு மற்றும் வெளியேற்றத்தைக் கண்காணித்து CWMA-வுக்கு ஆலோசனை வழங்குகிறது.",
        "Option A precisely outlines the technical role, composition, and reporting link of the CWRC to the CWMA.", "விருப்பம் A CWRC-ன் தொழில்நுட்பப் பங்கு மற்றும் CWMA-வுடனான தொடர்பைத் துல்லியமாக விளக்குகிறது.",
        "CWRC is not a court of record and cannot imprison Chief Ministers.", "CWRC ஒரு பதிவு நீதிமன்றம் அல்ல, முதலமைச்சர்களைச் சிறையில் அடைக்க முடியாது.",
        "It is not composed of Governors; it consists of technical and water engineering officials.", "இது ஆளுநர்களைக் கொண்டதல்ல; பொறியியல் அதிகாரிகளைக் கொண்டது.",
        "It is a statutory government body, not an NGO.", "இது ஒரு சட்டப்பூர்வ அரசு அமைப்பு, NGO அல்ல.",
        "CWMA Hierarchy: CWMA (apex authority headed by Chairman of CWC rank) is assisted on the ground by CWRC (technical committee monitoring daily reservoir data).",
        "காவிரி கட்டமைப்பு: CWMA (உச்ச அமைப்பு) களத்தில் CWRC-ஆல் (தினசரி நீர்த்தேக்கத் தரவுகளைக் கண்காணிக்கும் தொழில்நுட்பக் குழு) உதவப்படுகிறது.",
        "CWRC monitors daily river releases and reports to the CWMA.",
        "CWRC தினசரி நதி நீர் வெளியேற்றத்தைக் கண்காணித்து CWMA-விடம் தெரிவிக்கிறது.",
        tags=["CWRC", "CWMA", "Cauvery Scheme 2018"]
    ))

    # 038 - Ans B
    q.append(make_q(
        "ISR_H_038", "ARC Historical Nuance",
        "When the First Administrative Reforms Commission (1966) recommended the creation of an Inter-State Council under Article 263, which controversial issue did it specifically suggest should be kept OUTSIDE the purview of the Council?",
        "முதலாவது நிர்வாகச் சீர்திருத்த ஆணையம் (1966) உறுப்பு 263-ன் கீழ் மாநிலங்களுக்கு இடையிலான மன்றத்தை உருவாக்கப் பரிந்துரைத்த போது, எந்த சர்ச்சைக்குரிய விவகாரத்தை மன்றத்தின் வரம்பிற்கு வெளியே வைக்க வேண்டும் என்று குறிப்பாகப் பரிந்துரைத்தது?",
        "Border disputes and linguistic minority rights", "எல்லைத் தகராறுகள் மற்றும் மொழிச் சிறுபான்மையினர் உரிமைகள்",
        "Inter-State river water disputes, which should continue to be adjudicated by specialized judicial tribunals under Article 262", "மாநிலங்களுக்கு இடையிலான நதிநீர் தகராறுகள், அவை உறுப்பு 262-ன் கீழ் சிறப்பு நீதித்துறைத் தீர்ப்பாயங்களால் தொடர்ந்து தீர்க்கப்பட வேண்டும்",
        "All issues relating to finance and taxation", "நிதி மற்றும் வரிவிதிப்பு தொடர்பான அனைத்து விவகாரங்களும்",
        "Discussions concerning All India Services recruitment", "அகில இந்தியப் பணிகள் ஆட்சேர்ப்பு தொடர்பான விவாதங்கள்",
        "B",
        "The First ARC (1966–1969) in its report on Centre-State Relationships specifically recommended that while the Inter-State Council should discuss general policy coordination and administrative friction, inter-State river water disputes should be KEPT OUTSIDE its jurisdiction, because water disputes involve complex adversarial technical issues that require binding legal adjudication by specialized tribunals under Article 262 rather than political negotiation in a council.",
        "முதலாவது ARC (1966–1969) தனது மத்திய-மாநில உறவுகள் குறித்த அறிக்கையில், மாநிலங்களுக்கு இடையிலான மன்றம் பொதுவான கொள்கை ஒருங்கிணைப்பு மற்றும் நிர்வாக உராய்வுகளை விவாதிக்க வேண்டும் என்றாலும், மாநிலங்களுக்கு இடையேயான நதிநீர் தகராறுகளை அதன் அதிகார வரம்பிற்கு வெளியே வைக்க வேண்டும் என்று குறிப்பாகப் பரிந்துரைத்தது; ஏனெனில் நதிநீர் தகராறுகள் அரசியல் பேச்சுவார்த்தைகளை விட உறுப்பு 262-ன் கீழான சிறப்புத் தீர்ப்பாயங்களால் பிணைக்கும் சட்டப்பூர்வத் தீர்ப்பைக் கோருகின்றன.",
        "Border disputes and linguistic minorities were suggested for Zonal Councils and ISC discussion.", "எல்லைத் தகராறுகள் மற்றும் சிறுபான்மையினர் விவாதத்திற்குப் பரிந்துரைக்கப்பட்டன.",
        "Option B correctly identifies the First ARC's recommendation to insulate river water disputes from the political Inter-State Council.", "விருப்பம் B நதிநீர் தகராறுகளை அரசியல் மன்றத்திலிருந்து விலக்கி வைக்க முதல் ARC அளித்த பரிந்துரையைச் சரியாகக் குறிப்பிடுகிறது.",
        "Finance matters were not completely excluded from consultative discussion.", "நிதி விவகாரங்கள் ஆலோசனையிலிருந்து முற்றிலும் விலக்கப்படவில்லை.",
        "All India Services were considered a legitimate topic of federal coordination.", "அகில இந்தியப் பணிகள் ஒருங்கிணைப்பிற்குரிய தலைப்பாகக் கருதப்பட்டன.",
        "First ARC (1966) recommendation: Keep river water disputes OUT of the Inter-State Council; preserve Art 262 tribunals for water.",
        "முதல் ARC (1966) பரிந்துரை: நதிநீர் தகராறுகளை மாநிலங்களுக்கு இடையிலான மன்றத்திற்கு வெளியே வைக்கவும்; நீருக்கு உறுப்பு 262 தீர்ப்பாயங்களைப் பாதுகாக்கவும்.",
        "First ARC recommended keeping river water disputes outside Inter-State Council.",
        "நதிநீர் தகராறுகளை மாநிலங்களுக்கு இடையிலான மன்றத்திற்கு வெளியே வைக்க முதல் ARC பரிந்துரைத்தது.",
        tags=["First ARC", "Inter-State Council", "Exclusion of Water Disputes"]
    ))

    # 039 - Ans C
    q.append(make_q(
        "ISR_H_039", "Inter-State Water Law Principles",
        "What is the internationally recognized water apportionment principle known as the 'Helsinki Rules' (1966) that is routinely applied by Inter-State Water Disputes Tribunals in India?",
        "இந்தியாவில் உள்ள மாநிலங்களுக்கு இடையேயான நதிநீர் தகராறுகள் தீர்ப்பாயங்களால் வழக்கமாகப் பயன்படுத்தப்படும் 'ஹெல்சின்கி விதிகள்' (1966) எனப்படும் சர்வதேச அளவில் அங்கீகரிக்கப்பட்ட நீர் பகிர்வுக் கொள்கை எது?",
        "The principle of absolute territorial sovereignty granting all water to the source State.", "மூல மாநிலத்திற்கு அனைத்து நீரையும் வழங்கும் முழுமையான பிராந்திய இறையாண்மைக் கொள்கை.",
        "The principle of equal per capita mathematical division among all resident populations.", "அனைத்து மக்களுக்கும் சமமான தனிநபர் கணிதப் பகிர்வுக் கொள்கை.",
        "The principle of equitable and reasonable utilization of the waters of an international or inter-State drainage basin, taking into account all relevant hydrological, economic, and social factors.", "தொடர்புடைய அனைத்து நீரியல், பொருளாதார மற்றும் சமூகக் காரணிகளையும் கருத்தில் கொண்டு, ஒரு சர்வதேச அல்லது மாநிலங்களுக்கு இடையிலான நதிப் படுகையின் நீரைச் சமத்துவமாகவும் நியாயமாகவும் பயன்படுத்துவதற்கான கொள்கை.",
        "The principle that downstream States must purchase all water from upstream dams at market rates.", "கீழ்மட்ட மாநிலங்கள் மேல்மட்ட அணைகளில் இருந்து அனைத்து நீரையும் சந்தை விலையில் வாங்க வேண்டும் என்ற கொள்கை.",
        "C",
        "The Helsinki Rules on the Uses of the Waters of International Rivers (1966), formulated by the International Law Association, established the doctrine of 'equitable and reasonable utilization'. Under this doctrine, each basin State is entitled to a reasonable and equitable share in the beneficial uses of the waters of an international or inter-State basin, determined by weighing various factors (drainage area, contribution of water, climate, economic and social needs, population, and availability of other resources). This principle was endorsed and applied by the Krishna, Narmada, and Cauvery tribunals in India.",
        "சர்வதேச சட்டச் சங்கத்தால் உருவாக்கப்பட்ட சர்வதேச நதிகளின் நீரைப் பயன்படுத்துவதற்கான ஹெல்சின்கி விதிகள் (1966), 'சமத்துவ மற்றும் நியாயமான பயன்பாடு' (equitable and reasonable utilization) என்ற கோட்பாட்டை நிறுவியது. இக்கோட்பாட்டின் கீழ், ஒவ்வொரு படுகை மாநிலமும் நதிநீரின் பயனுள்ள பயன்பாட்டில் நியாயமான மற்றும் சமத்துவமான பங்கிற்கு உரிமையுடையது; இது பல்வேறு காரணிகளை (வடிகால் பகுதி, நீர்ப்பங்களிப்பு, காலநிலை, பொருளாதாரத் தேவைகள் போன்றவை) சீர்தூக்கிப் பார்த்து தீர்மானிக்கப்படுகிறது. இக்கொள்கையை கிருஷ்ணா, நர்மதா, காவிரி தீர்ப்பாயங்கள் ஏற்றுப் பயன்படுத்தின.",
        "Absolute territorial sovereignty (Harmon doctrine) was explicitly rejected by the Helsinki Rules.", "முழுமையான பிராந்திய இறையாண்மை ஹெல்சின்கி விதிகளால் நிராகரிக்கப்பட்டது.",
        "Equal per capita division is simplistic and ignored by international water law.", "சமமான தனிநபர் பகிர்வு சர்வதேச நீர் சட்டத்தால் நிராகரிக்கப்படுகிறது.",
        "Option C accurately outlines the doctrine of equitable and reasonable utilization under the Helsinki Rules.", "விருப்பம் C ஹெல்சின்கி விதிகளின் கீழான சமத்துவ மற்றும் நியாயமான பயன்பாட்டுக் கோட்பாட்டைத் துல்லியமாக விவரிக்கிறது.",
        "Water purchasing at market rates is completely alien to public water law.", "சந்தை விலையில் தண்ணீர் வாங்குவது பொது நீர் சட்டத்திற்கு முற்றிலும் முரணானது.",
        "Helsinki Rules (1966): Basis of Indian river tribunal awards -> 'Equitable and reasonable utilization' based on comprehensive basin factors.",
        "ஹெல்சின்கி விதிகள் (1966): இந்திய நதி தீர்ப்பாயத் தீர்ப்புகளின் அடிப்படை -> படுகைக் காரணிகளின் அடிப்படையிலான 'சமத்துவ மற்றும் நியாயமான பயன்பாடு'.",
        "Helsinki Rules establish the principle of equitable and reasonable utilization.",
        "ஹெல்சின்கி விதிகள் சமத்துவ மற்றும் நியாயமான பயன்பாட்டுக் கொள்கையை நிறுவுகின்றன.",
        tags=["Helsinki Rules", "Equitable Utilization", "Water Law"]
    ))

    # 040 - Ans D
    q.append(make_q(
        "ISR_H_040", "Assertion-Reason",
        "Given below are two statements, one labelled as Assertion (A) and the other as Reason (R):\nAssertion (A): The freedom guaranteed by Article 301 does not extend to the commercial trafficking of intoxicating liquor or gambling lottery tickets across State borders.\nReason (R): The Supreme Court has held that noxious, hazardous, or immoral activities are 'res extra commercium' and do not constitute 'trade or commerce' under the Indian Constitution.\nSelect the correct answer using the codes given below:",
        "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று உறுதிமொழி (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nஉறுதிமொழி (A): உறுப்பு 301-ன் கீழ் உத்தரவாதம் அளிக்கப்பட்ட சுதந்திரமானது, மாநில எல்லைகளைக் கடந்த போதை மதுபானங்கள் அல்லது சூதாட்ட லாட்டரி சீட்டுகளின் வணிகப் போக்குவரத்திற்குப் பொருந்தாது.\nகாரணம் (R): தீங்கு விளைவிக்கும், ஆபத்தான அல்லது ஒழுக்கக்கேடான நடவடிக்கைகள் 'வணிகத்திற்கு அப்பாற்பட்டவை' (res extra commercium) என்றும், இந்திய அரசியலமைப்பின் கீழ் 'வர்த்தகம் அல்லது வாணிபம்' ஆகாது என்றும் உச்ச நீதிமன்றம் தீர்ப்பளித்துள்ளது.\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:",
        "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-க்கான சரியான விளக்கம் அல்ல.",
        "(A) is true, but (R) is false.", "(A) உண்மை, ஆனால் (R) தவறு.",
        "(A) is false, but (R) is true.", "(A) தவறு, ஆனால் (R) உண்மை.",
        "Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மேலும் (R) என்பது (A)-க்கான சரியான விளக்கமாகும்.",
        "D",
        "Both Assertion (A) and Reason (R) are correct, and (R) is the exact constitutional explanation of (A). In State of Bombay v. R.M.D. Chamarbaugwala (1957) and subsequent liquor decisions (e.g., Khoday Distilleries), the Supreme Court ruled that activities inherently deleterious to public health, morals, and order are 'res extra commercium' (outside commerce) and cannot claim the protection of Article 301.",
        "உறுதிமொழி (A) மற்றும் காரணம் (R) இரண்டும் சரியானவை, மேலும் (R) என்பது (A)-க்கான துல்லியமான விளக்கமாகும். சாமர்பாகவாலா (1957) மற்றும் கோடே டிஸ்டில்லரீஸ் வழக்குகளில், பொது சுகாதாரம், ஒழுக்கம் மற்றும் அமைதிக்கு இயல்பாகவே தீங்கு விளைவிக்கும் நடவடிக்கைகள் 'வணிகத்திற்கு அப்பாற்பட்டவை' (res extra commercium) என்றும் உறுப்பு 301-ன் கீழ் பாதுகாப்பைக் கோர முடியாது என்றும் உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
        "Reason (R) directly explains why Assertion (A) is constitutionally valid.", "காரணம் (R) உறுதிமொழி (A) ஏன் செல்லுபடியாகும் என்பதை நேரடியாக விளக்குகிறது.",
        "Reason (R) is true, not false.", "காரணம் (R) உண்மை, தவறல்ல.",
        "Assertion (A) is completely true.", "உறுதிமொழி (A) முற்றிலும் உண்மை.",
        "Option D correctly confirms both statements are true and (R) explains (A).", "விருப்பம் D இரண்டும் உண்மை மற்றும் (R) என்பது (A)-க்கான சரியான விளக்கம் என்பதை உறுதிப்படுத்துகிறது.",
        "Res Extra Commercium: Liquor, gambling, and hazardous contraband are outside Article 301 protection because they are inherently anti-social.",
        "வணிகத்திற்கு அப்பாற்பட்டவை: மது, சூதாட்டம் மற்றும் ஆபத்தான கடத்தல் பொருட்கள் உறுப்பு 301-ன் பாதுகாப்பிற்கு வெளியே உள்ளன.",
        "Noxious activities are res extra commercium and excluded from Art 301.",
        "தீங்கு விளைவிக்கும் நடவடிக்கைகள் உறுப்பு 301 இலிருந்து விலக்கப்பட்டுள்ளன.",
        tags=["Assertion-Reason", "Res Extra Commercium", "Article 301"]
    ))

    # 041 - Ans A
    q.append(make_q(
        "ISR_H_041", "Article 303(1) Nuance",
        "Under Article 303(1), why did the framers insert the phrase 'by virtue of any entry relating to trade and commerce in any of the Lists in the Seventh Schedule'?",
        "உறுப்பு 303(1)-ன் கீழ், 'ஏழாவது அட்டவணையில் உள்ள எந்தவொரு பட்டியலிலும் வர்த்தகம் மற்றும் வணிகம் தொடர்பான எந்தவொரு பதிவின் மூலமாகவும்' என்ற சொற்றொடரை அரசியலமைப்பை உருவாக்கியவர்கள் ஏன் சேர்த்தனர்?",
        "To ensure that the non-discrimination mandate applies horizontally across all three legislative lists, preventing both Parliament and States from using any concurrent or state subject to create discriminatory trade barriers.", "பாகுபாடற்ற ஆணை மூன்று சட்டமன்றப் பட்டியல்களிலும் கிடைமட்டமாகப் பொருந்துகிறது என்பதை உறுதிப்படுத்தவும், நாடாளுமன்றமும் மாநிலங்களும் எந்தவொரு பொது அல்லது மாநிலப் பாடத்தைப் பயன்படுத்தி பாகுபாடான வர்த்தகத் தடைகளை உருவாக்குவதைத் தடுக்கவும்.",
        "To restrict the operation of Article 303 strictly to maritime customs duties under Entry 83.", "உறுப்பு 303-ன் செயல்பாட்டைப் பதிவு 83-ன் கீழான கடல்சார் சுங்க வரிகளுக்கு மட்டுமே கட்டுப்படுத்த.",
        "To grant State Legislatures paramount power over the Union List.", "மத்தியப் பட்டியலின் மீது மாநில சட்டமன்றங்களுக்கு மேலான அதிகாரத்தை வழங்க.",
        "To eliminate all sales tax exemptions granted to state public sector undertakings.", "மாநிலப் பொதுத்துறை நிறுவனங்களுக்கு வழங்கப்பட்ட அனைத்து விற்பனை வரி விலக்குகளையும் ஒழிக்க.",
        "A",
        "The expansive phrase 'by virtue of any entry relating to trade and commerce in any of the Lists in the Seventh Schedule' was chosen to ensure that neither Parliament nor a State Legislature could circumvent the prohibition against preference or discrimination by relying on diverse entries spread across List I, List II, or List III (such as Entry 42 of List I, Entry 26 of List II, or Entry 33 of List III).",
        "நாடாளுமன்றமோ அல்லது ஒரு மாநில சட்டமன்றமோ பட்டியல் I, பட்டியல் II அல்லது பட்டியல் III-ல் பரவியுள்ள பல்வேறு பதிவுகளை (பட்டியல் I-ன் பதிவு 42, பட்டியல் II-ன் பதிவு 26 அல்லது பட்டியல் III-ன் பதிவு 33 போன்றவை) நம்பி முன்னுரிமை அல்லது பாகுபாட்டிற்கு எதிரான தடையைத் தவிர்ப்பதைத் தடுக்கவே இந்த விரிவான சொற்றொடர் சேர்க்கப்பட்டது.",
        "Option A accurately explains the anti-circumvention purpose of Article 303(1) across all legislative lists.", "விருப்பம் A அனைத்து சட்டமன்றப் பட்டியல்களிலும் தடையைத் தவிர்ப்பதைத் தடுக்கும் உறுப்பு 303(1)-ன் நோக்கத்தைச் சரியாக விளக்குகிறது.",
        "It is not restricted to Entry 83 customs duties.", "இது பதிவு 83-ன் சுங்க வரிகளுக்கு மட்டுமே மட்டுப்படுத்தப்பட்டது அல்ல.",
        "States do not have paramount power over the Union List.", "மாநிலங்களுக்கு மத்தியப் பட்டியலின் மீது மேலான அதிகாரம் இல்லை.",
        "It does not relate to PSU sales tax exemptions.", "இது PSU விற்பனை வரி விலக்குகளுடன் தொடர்புடையது அல்ல.",
        "Article 303(1) operates across all three legislative lists (Union, State, and Concurrent) to prevent indirect discriminatory trade legislation.",
        "உறுப்பு 303(1) மறைமுகப் பாகுபாடான வர்த்தகச் சட்டங்களைத் தடுக்க மூன்று பட்டியல்களிலும் (மத்திய, மாநில மற்றும் பொது) செயல்படுகிறது.",
        "Article 303(1) bars discriminatory laws under trade entries across all 3 lists.",
        "உறுப்பு 303(1) 3 பட்டியல்களிலும் உள்ள வர்த்தகப் பதிவுகளின் கீழ் பாகுபாடான சட்டங்களைத் தடுக்கிறது.",
        tags=["Article 303(1)", "Seventh Schedule Entries", "Anti-Circumvention"]
    ))

    # 042 - Ans B
    q.append(make_q(
        "ISR_H_042", "Judicial Precedent & Reasoning",
        "In Automobile Transport (1962), on what rationale did the Supreme Court hold that regulatory and compensatory taxes do not violate the freedom guaranteed under Article 301?",
        "ஆட்டோமொபைல் டிரான்ஸ்போர்ட் (1962) வழக்கில், ஒழுங்குமுறை மற்றும் ஈட்டு வரிகள் உறுப்பு 301-ன் கீழ் உத்தரவாதம் அளிக்கப்பட்ட சுதந்திரத்தை மீறாது என்று உச்ச நீதிமன்றம் எந்தத் தர்க்கத்தின் அடிப்படையில் தீர்ப்பளித்தது?",
        "Because the President has inherent prerogative power to exempt any state tax from judicial review.", "ஏனெனில் எந்தவொரு மாநில வரியையும் நீதித்துறை மறுஆய்விலிருந்து விடுவிக்க குடியரசுத் தலைவருக்கு உள்ளார்ந்த சிறப்பு அதிகாரம் உள்ளது.",
        "Because regulatory measures and compensatory taxes facilitate the free flow of trade by maintaining roads and bridges; restrictions that promote the orderly operation of trade cannot be treated as an impediment to trade.", "ஏனெனில் ஒழுங்குமுறை நடவடிக்கைகள் மற்றும் ஈட்டு வரிகள் சாலைகள் மற்றும் பாலங்களைப் பராமரிப்பதன் மூலம் வர்த்தகத்தின் தடையற்ற ஓட்டத்திற்கு உதவுகின்றன; வர்த்தகத்தின் ஒழுங்கான செயல்பாட்டை ஊக்குவிக்கும் கட்டுப்பாடுகள் வர்த்தகத்திற்குத் தடையாகக் கருதப்பட முடியாது.",
        "Because taxes on motor vehicles are collected exclusively by the Reserve Bank of India.", "ஏனெனில் மோட்டார் வாகனங்கள் மீதான வரிகள் ரிசர்வ் வங்கியால் மட்டுமே வசூலிக்கப்படுகின்றன.",
        "Because Article 301 applies only to foot pedestrians and pack animals, not to motorized transport.", "ஏனெனில் உறுப்பு 301 பாதசாரிகள் மற்றும் பொதி விலங்குகளுக்கு மட்டுமே பொருந்தும், மோட்டார் போக்குவரத்திற்கு அல்ல.",
        "B",
        "In Automobile Transport (1962), the 7-judge bench reasoned that freedom of trade does not mean total absence of all regulation or fiscal contributions. A tax that is a compensatory recompense for facilities provided (such as road construction and maintenance) actually facilitates and preserves the flow of trade. Therefore, such regulatory and compensatory taxes do not constitute an impediment or restriction within the meaning of Article 301.",
        "ஆட்டோமொபைல் டிரான்ஸ்போர்ட் (1962) வழக்கில், 7 நீதிபதிகள் அமர்வு, வர்த்தக சுதந்திரம் என்பது அனைத்து ஒழுங்குமுறைகளும் அல்லது வரிகளும் இல்லாத நிலை அல்ல என்று வாதிட்டது. வழங்கப்பட்ட வசதிகளுக்கு (சாலை அமைத்தல் மற்றும் பராமரித்தல் போன்றவை) ஈட்டுத் தொகையாக இருக்கும் ஒரு வரி உண்மையில் வர்த்தகத்தின் ஓட்டத்தை எளிதாக்குகிறது மற்றும் பாதுகாக்கிறது. எனவே, அத்தகைய வரிகள் உறுப்பு 301-ன் கீழ் ஒரு தடையாக அமையாது.",
        "The President does not possess an inherent prerogative to exempt taxes.", "வரிகளுக்கு விலக்களிக்க குடியரசுத் தலைவருக்கு உள்ளார்ந்த அதிகாரம் இல்லை.",
        "Option B correctly states the judicial rationale that facilitating measures promoting trade flow do not violate Art 301.", "விருப்பம் B வர்த்தக ஓட்டத்தை ஊக்குவிக்கும் நடவடிக்கைகள் உறுப்பு 301-ஐ மீறாது என்ற நீதித்துறை தர்க்கத்தைச் சரியாகக் கூறுகிறது.",
        "Motor vehicle taxes are collected by State RTOs, not the RBI.", "மோட்டார் வாகன வரிகள் மாநில RTO-க்களால் வசூலிக்கப்படுகின்றன, ரிசர்வ் வங்கியால் அல்ல.",
        "Article 301 applies to all modes of commercial transit.", "உறுப்பு 301 அனைத்து வணிகப் போக்குவரத்து முறைகளுக்கும் பொருந்தும்.",
        "Automobile Transport Rationale: Compensatory taxes facilitate and maintain trading infrastructure; hence they do not 'restrict' trade.",
        "ஆட்டோமொபைல் டிரான்ஸ்போர்ட் தர்க்கம்: ஈட்டு வரிகள் வர்த்தகக் கட்டமைப்பைப் பராமரிக்க உதவுகின்றன; எனவே அவை வர்த்தகத்தைக் 'கட்டுப்படுத்தாது'.",
        "Compensatory taxes facilitate trade and do not restrict it under Art 301.",
        "ஈட்டு வரிகள் வர்த்தகத்தை எளிதாக்குகின்றன மற்றும் உறுப்பு 301 இன் கீழ் அதைத் தடுக்காது.",
        tags=["Automobile Transport", "Compensatory Tax Rationale", "Article 301"]
    ))

    # 043 - Ans C
    q.append(make_q(
        "ISR_H_043", "Institutional Role Analysis",
        "What unique constitutional and administrative role does the Union Home Minister play in institutional mechanisms governing Inter-State Relations in India?",
        "இந்தியாவில் மாநிலங்களுக்கு இடையிலான உறவுகளை நிர்வகிக்கும் நிறுவன வழிமுறைகளில் மத்திய உள்துறை அமைச்சர் என்ன தனித்துவமான அரசியலமைப்பு மற்றும் நிர்வாகப் பங்கை வகிக்கிறார்?",
        "He is the sole authority empowered to adjudicate river water disputes under Article 262.", "உறுப்பு 262-ன் கீழ் நதிநீர் தகராறுகளைத் தீர்க்க அதிகாரம் பெற்ற ஒரே அதிகாரி அவர் ஆவார்.",
        "He acts as the appellate judge over the decisions of the Supreme Court under Article 131.", "உறுப்பு 131-ன் கீழ் உச்ச நீதிமன்றத்தின் முடிவுகள் மீது அவர் மேல்முறையீட்டு நீதிபதியாகச் செயல்படுகிறார்.",
        "He serves as the common Chairman of all five Zonal Councils, Chairman of the Standing Committee of the Inter-State Council, and Chairman of the North Eastern Council, acting as the primary institutional pivot of federal coordination.", "அவர் ஐந்து மண்டலக் குழுக்களுக்கும் பொதுவான தலைவராகவும், மாநிலங்களுக்கு இடையிலான மன்றத்தின் நிலைக் குழுவின் தலைவராகவும், வடகிழக்கு கவுன்சிலின் தலைவராகவும் செயல்பட்டு, கூட்டாட்சி ஒருங்கிணைப்பின் முதன்மை நிறுவன அச்சாகத் திகழ்கிறார்.",
        "He is constitutionally mandated to approve all State budgets before presentation in Legislative Assemblies.", "சட்டமன்றங்களில் சமர்ப்பிக்கப்படுவதற்கு முன் அனைத்து மாநில வரவு செலவுத் திட்டங்களுக்கும் ஒப்புதல் அளிக்க அரசியலமைப்பு ரீதியாக அவர் கட்டாயப்படுத்தப்பட்டுள்ளார்.",
        "C",
        "The Union Home Minister occupies a pivotal institutional role in Indian federalism: (1) Statutory Chairman of all 5 Zonal Councils (States Reorganisation Act 1956); (2) Chairman of the Standing Committee of the Inter-State Council (since 1996); (3) Chairman of the North Eastern Council (since 2018 restructuring); and (4) Member of the full Inter-State Council. This makes the Home Minister the primary executive coordinator between the Union and States.",
        "மத்திய உள்துறை அமைச்சர் இந்தியக் கூட்டாட்சியில் ஒரு முக்கிய நிறுவனப் பங்கை வகிக்கிறார்: (1) அனைத்து 5 மண்டலக் குழுக்களின் சட்டப்பூர்வ தலைவர்; (2) மாநிலங்களுக்கு இடையிலான மன்றத்தின் நிலைக் குழுவின் தலைவர்; (3) வடகிழக்கு கவுன்சிலின் தலைவர்; மற்றும் (4) முழு மாநிலங்களுக்கு இடையிலான மன்றத்தின் உறுப்பினர். இது உள்துறை அமைச்சரை மத்திய-மாநில அரசுகளுக்கிடையேயான முதன்மை நிர்வாக ஒருங்கிணைப்பாளராக ஆக்குகிறது.",
        "Water disputes are adjudicated by judicial tribunals under Art 262, not the Home Minister.", "நதிநீர் தகராறுகள் நீதித்துறை தீர்ப்பாயங்களால் தீர்க்கப்படுகின்றன, உள்துறை அமைச்சரால் அல்ல.",
        "No executive minister can act as an appellate judge over the Supreme Court.", "எந்த அமைச்சரும் உச்ச நீதிமன்றத்திற்கு மேல் மேல்முறையீட்டு நீதிபதியாகச் செயல்பட முடியாது.",
        "Option C comprehensively articulates the Union Home Minister's triple chairmanship in Zonal Councils, ISC Standing Committee, and NEC.", "விருப்பம் C மண்டலக் குழுக்கள், ISC நிலைக் குழு மற்றும் NEC ஆகியவற்றில் மத்திய உள்துறை அமைச்சரின் மூன்று தலைமைப் பொறுப்புகளை விரிவாக விளக்குகிறது.",
        "State budgets do not require Home Ministry approval (Articles 202-207).", "மாநில வரவு செலவுத் திட்டங்களுக்கு உள்துறை அமைச்சக ஒப்புதல் தேவையில்லை.",
        "Federal Pivot: Union Home Minister chairs (1) all 5 Zonal Councils; (2) ISC Standing Committee; and (3) North Eastern Council.",
        "கூட்டாட்சி அச்சு: மத்திய உள்துறை அமைச்சர் (1) 5 மண்டலக் குழுக்கள்; (2) ISC நிலைக் குழு; (3) வடகிழக்கு கவுன்சில் ஆகியவற்றிற்குத் தலைமை தாங்குகிறார்.",
        "Union Home Minister chairs Zonal Councils, ISC Standing Committee, and NEC.",
        "மத்திய உள்துறை அமைச்சர் மண்டலக் குழுக்கள், ISC நிலைக் குழு மற்றும் NEC-க்குத் தலைமை தாங்குகிறார்.",
        tags=["Union Home Minister", "Federal Pivot", "Zonal Councils", "NEC"]
    ))

    # 044 - Ans D
    q.append(make_q(
        "ISR_H_044", "Burden of Proof",
        "When a State statute imposing trade restrictions under Article 304(b) is challenged before a constitutional court, upon whom does the burden of proof lie to establish that the restriction is 'reasonable' and required in the 'public interest'?",
        "உறுப்பு 304(b)-ன் கீழ் வர்த்தகக் கட்டுப்பாடுகளை விதிக்கும் ஒரு மாநிலச் சட்டம் ஓர் அரசியலமைப்பு நீதிமன்றத்தின் முன் சவால் செய்யப்படும் போது, அக் கட்டுப்பாடு 'நியாயமானது' மற்றும் 'பொது நலன்' கருதி தேவைப்படுகிறது என்பதை நிறுவுவதற்கான நிரூபிக்கும் சுமை (burden of proof) யார் மீது விழுகிறது?",
        "Upon the petitioner challenging the law, who must prove beyond all doubt that the law is malicious.", "சட்டத்தைச் சவால் செய்யும் மனுதாரர் மீது, அச்சட்டம் தீங்கிழைக்கும் எண்ணம் கொண்டது என்பதை அவர் சந்தேகத்திற்கு இடமின்றி நிரூபிக்க வேண்டும்.",
        "Upon the Inter-State Council Secretariat.", "மாநிலங்களுக்கு இடையிலான மன்றச் செயலகத்தின் மீது.",
        "Upon the President of India, who granted previous sanction.", "முன் அனுமதி வழங்கிய இந்தியக் குடியரசுத் தலைவர் மீது.",
        "Upon the State defending the legislation, which must place empirical material before the court demonstrating that the restriction is objectively reasonable and genuinely required in the public interest.", "சட்டத்தைப் பாதுகாக்கும் மாநில அரசின் மீது; அக் கட்டுப்பாடு புறநிலையாக நியாயமானது மற்றும் பொது நலன் கருதி உண்மையாகவே தேவைப்படுகிறது என்பதை நிரூபிக்கும் அனுபவப்பூர்வமான ஆதாரங்களை அது நீதிமன்றத்தின் முன் வைக்க வேண்டும்.",
        "D",
        "The Supreme Court has firmly held (e.g., in Khyerbari Tea Co. v. State of Assam) that once a petitioner shows that a State statute prima facie restricts the freedom of trade guaranteed under Article 301, the burden shifts entirely to the STATE to prove that the restriction satisfies the requirements of Article 304(b)—namely, that it is objectively 'reasonable' and genuinely required in the 'public interest'. The State cannot rely on mere legislative assertion.",
        "ஒரு மாநிலச் சட்டம் உறுப்பு 301-ன் கீழ் உத்தரவாதம் அளிக்கப்பட்ட வர்த்தக சுதந்திரத்தை வெளிப்படையாகக் கட்டுப்படுத்துகிறது என்பதை ஒரு மனுதாரர் காட்டியவுடன், அக் கட்டுப்பாடு உறுப்பு 304(b)-ன் தேவைகளை நிறைவு செய்கிறது என்பதை—அதாவது அது புறநிலையாக 'நியாயமானது' மற்றும் 'பொது நலன்' கருதி தேவைப்படுகிறது என்பதை—நிரூபிக்கும் சுமை முழுவதும் மாநில அரசிடமே மாறுகிறது என்று உச்ச நீதிமன்றம் (கயர்பாரி டீ கம்பெனி வழக்கில்) தீர்ப்பளித்துள்ளது.",
        "The petitioner only needs to show that movement of trade is restricted; the burden of justifying reasonableness lies on the State.", "வர்த்தகம் கட்டுப்படுத்தப்பட்டுள்ளது என்பதைக் காட்டினால் போதுமானது; நியாயத்தன்மையை நிரூபிக்கும் சுமை மாநிலத்தின் மீதே உள்ளது.",
        "The Inter-State Council has no burden in court litigation.", "மாநிலங்களுக்கு இடையிலான மன்றத்திற்கு நீதிமன்ற வழக்குகளில் சுமை இல்லை.",
        "The President does not defend legislation in court.", "குடியரசுத் தலைவர் நீதிமன்றத்தில் சட்டங்களைப் பாதுகாப்பதில்லை.",
        "Option D correctly states that the burden of proving reasonableness and public interest rests on the State.", "விருப்பம் D நியாயத்தன்மையையும் பொது நலனையும் நிரூபிக்கும் சுமை மாநில அரசிடமே உள்ளது என்பதைச் சரியாகக் கூறுகிறது.",
        "Burden of Proof under Art 304(b): The State MUST place empirical evidence proving that the trade restriction is reasonable and in the public interest.",
        "உறுப்பு 304(b)-ன் கீழான நிரூபிக்கும் சுமை: வர்த்தகக் கட்டுப்பாடு நியாயமானது மற்றும் பொது நலன் சார்ந்தது என்பதை நிரூபிக்கும் ஆதாரங்களை மாநில அரசு சமர்ப்பிக்க வேண்டும்.",
        "State bears the burden of proving reasonableness under Article 304(b).",
        "உறுப்பு 304(b)-ன் கீழ் நியாயத்தன்மையை நிரூபிக்கும் சுமையை மாநில அரசே சுமக்கிறது.",
        tags=["Article 304(b)", "Burden of Proof", "Reasonableness"]
    ))

    # 045 - Ans A
    q.append(make_q(
        "ISR_H_045", "Inter-State Water Dispute Case Law",
        "In the Krishna Water Disputes Tribunal I award (Bachawat Award, 1973/1976), what was the innovative scheme adopted regarding Scheme 'A' and Scheme 'B' water allocations?",
        "கிருஷ்ணா நதிநீர் தகராறுகள் தீர்ப்பாயம் I-ன் தீர்ப்பில் (பச்சாவத் தீர்ப்பு, 1973/1976), திட்டம் 'A' மற்றும் திட்டம் 'B' நீர் ஒதுக்கீடுகள் தொடர்பாகப் பின்பற்றப்பட்ட புதுமையான திட்டம் என்ன?",
        "Scheme A allocated water based on 75% dependable flow to Maharashtra, Karnataka, and Andhra Pradesh, while Scheme B proposed sharing surplus waters through an inter-State authority which could not take effect due to lack of consensus.", "திட்டம் A மகாராஷ்டிரா, கர்நாடகா மற்றும் ஆந்திரப் பிரதேசத்திற்கு 75% நம்பகமான நீரோட்டத்தின் அடிப்படையில் நீரை ஒதுக்கியது; அதே சமயம் திட்டம் B ஒரு மாநிலங்களுக்கு இடையிலான அதிகார அமைப்பு மூலம் உபரி நீரைப் பகிர்ந்து கொள்ள முன்மொழிந்தது, இது ஒருமித்த கருத்து இல்லாததால் நடைமுறைக்கு வர முடியவில்லை.",
        "Scheme A applied to drinking water, while Scheme B applied exclusively to nuclear reactor cooling.", "திட்டம் A குடிநீருக்கும், திட்டம் B அணு உலை குளிரூட்டலுக்கும் மட்டுமே பொருந்தியது.",
        "Scheme A transferred all Krishna water to the Godavari basin, while Scheme B transferred Godavari water to the Cauvery.", "திட்டம் A அனைத்து கிருஷ்ணா நீரையும் கோதாவரி படுகைக்கும், திட்டம் B கோதாவரி நீரை காவிரிக்கும் மாற்றியது.",
        "Scheme A abolished all existing dams, while Scheme B mandated the construction of a single mega-dam at Almatti.", "திட்டம் A அனைத்து அணைகளையும் ஒழித்தது, திட்டம் B ஆலமட்டியில் ஒரு மெகா அணையைக் கட்டக் கட்டாயப்படுத்தியது.",
        "A",
        "Under the Bachawat Award (KWDT-I), Scheme A allocated 2060 TMC of water among Maharashtra (560 TMC), Karnataka (700 TMC), and Andhra Pradesh (800 TMC) based on 75% dependability. Scheme B was a visionary scheme for sharing surplus flows above 2060 TMC through an autonomous inter-State Krishna Valley Authority, but Scheme B required unanimous agreement of all three States, which was not forthcoming, leaving Scheme A as the operating award.",
        "பச்சாவத் தீர்ப்பின் (KWDT-I) கீழ், திட்டம் A 75% நம்பகத்தன்மையின் அடிப்படையில் மகாராஷ்டிரா (560 TMC), கர்நாடகா (700 TMC) மற்றும் ஆந்திரப் பிரதேசம் (800 TMC) ஆகியவற்றுக்கு இடையே 2060 TMC நீரை ஒதுக்கியது. திட்டம் B என்பது ஒரு தன்னாட்சி கிருஷ்ணா பள்ளத்தாக்கு ஆணையம் மூலம் 2060 TMC-க்கு அதிகமான உபரி நீரைப் பகிர்வதற்கான ஒரு தொலைநோக்குத் திட்டமாகும்; ஆனால் இதற்கு மூன்று மாநிலங்களின் ஒருமனதான ஒப்புதல் தேவைப்பட்டது, அது கிடைக்காததால் திட்டம் A மட்டுமே செயல்பாட்டுத் தீர்ப்பாக நீடித்தது.",
        "Option A accurately explains the 75% dependable flow Scheme A and the surplus sharing Scheme B of the Bachawat Tribunal.", "விருப்பம் A 75% நம்பகமான திட்டம் A மற்றும் உபரி நீர் பகிர்வு திட்டம் B ஆகியவற்றைத் துல்லியமாக விளக்குகிறது.",
        "Nuclear cooling was not a category in the 1973 Bachawat award.", "அணு உலை குளிரூட்டல் 1973 பச்சாவத் தீர்ப்பின் பிரிவல்ல.",
        "It did not involve the inter-basin transfer of all Krishna water to Godavari.", "இது கிருஷ்ணா நீரை கோதாவரிக்கு முழுமையாக மாற்றவில்லை.",
        "It did not abolish existing dams.", "இது ஏற்கனவே உள்ள அணைகளை ஒழிக்கவில்லை.",
        "Bachawat Award (KWDT-I): Scheme A allocated 2060 TMC at 75% dependability; Scheme B was an unratified surplus-sharing mechanism.",
        "பச்சாவத் தீர்ப்பு (KWDT-I): திட்டம் A 75% நம்பகத்தன்மையில் 2060 TMC-ஐ ஒதுக்கியது; திட்டம் B என்பது அங்கீகரிக்கப்படாத உபரி பகிர்வு முறைமையாகும்.",
        "KWDT-I Bachawat Award: Scheme A allocated 2060 TMC; Scheme B addressed surplus water.",
        "KWDT-I பச்சாவத் தீர்ப்பு: திட்டம் A 2060 TMC ஐ ஒதுக்கியது; திட்டம் B உபரி நீரை கையாண்டது.",
        tags=["Krishna Tribunal I", "Bachawat Award", "Scheme A and B"]
    ))

    # 046 - Ans B
    q.append(make_q(
        "ISR_H_046", "Constitutional Remedy",
        "If the President refuses to grant 'previous sanction' under the proviso to Article 304(b) for introducing a State Bill imposing trade restrictions, what legal remedy is available to the State Government against such refusal?",
        "வர்த்தகக் கட்டுப்பாடுகளை விதிக்கும் ஒரு மாநில மசோதாவை அறிமுகப்படுத்துவதற்கு உறுப்பு 304(b)-ன் நிபந்தனையின் கீழ் குடியரசுத் தலைவர் 'முன் அனுமதி' வழங்க மறுத்தால், அத்தகைய மறுப்பிற்கு எதிராக மாநில அரசுக்கு என்ன சட்டப்பூர்வ தீர்வு உள்ளது?",
        "The State Government can file a petition under Article 32 before the Supreme Court seeking a writ of mandamus against the President.", "குடியரசுத் தலைவருக்கு எதிராக மாண்டமஸ் பேராணையை நாடி உச்ச நீதிமன்றத்தில் உறுப்பு 32-ன் கீழ் மாநில அரசு மனு தாக்கல் செய்யலாம்.",
        "No legal remedy lies against the President; the grant or refusal of sanction is an executive discretion exercised on the aid and advice of the Union Council of Ministers, which cannot be compelled by court writ under Article 361.", "குடியரசுத் தலைவருக்கு எதிராக எந்தவொரு சட்டப்பூர்வ தீர்வும் இல்லை; அனுமதி வழங்குவது அல்லது மறுப்பது என்பது மத்திய அமைச்சரவையின் உதவி மற்றும் ஆலோசனையின் பேரில் செயல்படுத்தப்படும் நிர்வாக அதிகாரமாகும், இதை உறுப்பு 361-ன் கீழ் நீதிமன்றப் பேராணையால் கட்டாயப்படுத்த முடியாது.",
        "The State Legislature can override the President's refusal by passing a resolution with a 3/4th majority.", "மாநில சட்டமன்றம் 3/4 பங்கு பெரும்பான்மையுடன் ஒரு தீர்மானத்தை நிறைவேற்றுவதன் மூலம் குடியரசுத் தலைவரின் மறுப்பை ரத்து செய்யலாம்.",
        "The State Government can appeal directly to the Zonal Council for a binding waiver.", "கட்டுப்படுத்தும் விலக்கு கோரி மாநில அரசு நேரடியாக மண்டலக் குழுவிடம் மேல்முறையீடு செய்யலாம்.",
        "B",
        "Under Article 361(1), the President is not answerable to any court for the exercise and performance of the powers and duties of his office. The grant of previous sanction under Article 304(b) is an executive function exercised on the aid and advice of the Union Council of Ministers under Article 74. No court can issue a mandamus to the President to grant sanction, nor can a State Legislature override such refusal.",
        "அரசியலமைப்பு உறுப்பு 361(1)-ன் கீழ், குடியரசுத் தலைவர் தனது அலுவலகத்தின் அதிகாரங்கள் மற்றும் கடமைகளைச் செயல்படுத்துவதற்கு எந்த நீதிமன்றத்திற்கும் பதிலளிக்க வேண்டியதில்லை. உறுப்பு 304(b)-ன் கீழ் முன் அனுமதி வழங்குவது என்பது உறுப்பு 74-ன் கீழ் மத்திய அமைச்சரவையின் உதவி மற்றும் ஆலோசனையின் பேரில் செயல்படுத்தப்படும் ஓர் அதிகாரமாகும். அனுமதி வழங்குமாறு குடியரசுத் தலைவருக்கு எந்த நீதிமன்றமும் மாண்டமஸ் பிறப்பிக்க முடியாது, அல்லது மாநில சட்டமன்றம் அதை ரத்து செய்ய முடியாது.",
        "Article 32 cannot be used to issue a writ to the President to grant legislative sanction.", "சட்டமன்ற அனுமதி வழங்குமாறு குடியரசுத் தலைவருக்கு உத்தரவிட உறுப்பு 32-ஐப் பயன்படுத்த முடியாது.",
        "Option B accurately reflects the constitutional immunity under Article 361 and the executive discretion of Article 74/304(b).", "விருப்பம் B உறுப்பு 361-ன் கீழான அரசியலமைப்பு விலக்கையும் உறுப்பு 74/304(b)-ன் கீழான நிர்வாக அதிகாரத்தையும் சரியாகப் பிரதிபலிக்கிறது.",
        "State Legislatures have no power to override Presidential refusal of sanction.", "குடியரசுத் தலைவரின் மறுப்பை ரத்து செய்ய மாநில சட்டமன்றங்களுக்கு அதிகாரம் இல்லை.",
        "Zonal Councils have no appellate or waiver authority over Presidential decisions.", "குடியரசுத் தலைவரின் முடிவுகள் மீது மண்டலக் குழுக்களுக்கு மேல்முறையீட்டு அதிகாரம் இல்லை.",
        "Article 361 Immunity: No court can compel the President to grant previous sanction under Article 304(b).",
        "உறுப்பு 361 விலக்கு: உறுப்பு 304(b)-ன் கீழ் முன் அனுமதி வழங்குமாறு குடியரசுத் தலைவரை எந்த நீதிமன்றமும் கட்டாயப்படுத்த முடியாது.",
        "No legal remedy lies against Presidential refusal of sanction under Art 304(b).",
        "உறுப்பு 304(b)-ன் கீழான குடியரசுத் தலைவர் அனுமதி மறுப்பிற்கு எதிராக எந்த சட்டத் தீர்வும் இல்லை.",
        tags=["Article 304(b)", "Presidential Sanction", "Article 361 Immunity"]
    ))

    # 047 - Ans C
    q.append(make_q(
        "ISR_H_047", "Constitutional Nuance",
        "What is the crucial legal distinction between the scope of inquiry under Article 263(a) and the making of recommendations under Article 263(c)?",
        "உறுப்பு 263(a)-ன் கீழான விசாரணையின் நோக்கத்திற்கும், உறுப்பு 263(c)-ன் கீழான பரிந்துரைகளை வழங்குவதற்கும் இடையிலான முக்கிய சட்ட வேறுபாடு என்ன?",
        "Article 263(a) applies only to foreign disputes, while Article 263(c) applies to domestic disputes.", "உறுப்பு 263(a) வெளிநாட்டுத் தகராறுகளுக்கு மட்டுமே பொருந்தும், ஆனால் 263(c) உள்நாட்டுத் தகராறுகளுக்குப் பொருந்தும்.",
        "Article 263(a) decisions are enforceable by the military, while Article 263(c) decisions are voluntary.", "உறுப்பு 263(a) முடிவுகள் இராணுவத்தால் செயல்படுத்தப்படக் கூடியவை, ஆனால் 263(c) முடிவுகள் விருப்பத்திற்குரியவை.",
        "Article 263(a) deals specifically with inquiring into and advising upon existing disputes that have arisen between States, whereas Article 263(c) deals proactively with making recommendations for the better co-ordination of policy and action on subjects of common interest.", "உறுப்பு 263(a) மாநிலங்களுக்கிடையே ஏற்கனவே எழுந்துள்ள தகராறுகளை விசாரித்து ஆலோசனை வழங்குவதைக் குறிக்கிறது; அதே சமயம் உறுப்பு 263(c) பொதுவான நலன் சார்ந்த விஷயங்களில் கொள்கை மற்றும் நடவடிக்கைகளின் சிறந்த ஒருங்கிணைப்பிற்காக முன்கூட்டியே பரிந்துரைகளை வழங்குவதைக் கையாள்கிறது.",
        "Article 263(a) requires a 2/3rd majority of the Lok Sabha, while Article 263(c) operates by presidential ordinance.", "உறுப்பு 263(a)-க்கு மக்களவையின் 2/3 பங்கு பெரும்பான்மை தேவை, ஆனால் 263(c) குடியரசுத் தலைவர் அவசரச் சட்டம் மூலம் இயங்குகிறது.",
        "C",
        "Article 263 has three distinct clauses: (a) relates to dispute settlement—inquiring into and advising upon actual disputes which have arisen between States; (b) relates to investigating and discussing subjects in which States or Union have a common interest; and (c) relates to positive policy coordination—making recommendations upon any such subject for better coordination of policy and action. Thus, clause (a) is dispute-oriented, while clause (c) is policy-coordination oriented.",
        "உறுப்பு 263 மூன்று வெவ்வேறு பிரிவுகளைக் கொண்டுள்ளது: (a) தகராறு தீர்வு தொடர்பானது—மாநிலங்களுக்கிடையே எழுந்துள்ள தகராறுகளை விசாரித்து ஆலோசனை வழங்குதல்; (b) ஒன்றியம் அல்லது மாநிலங்களுக்குப் பொதுவான நலன் சார்ந்த விஷயங்களை ஆராய்ந்து விவாதிப்பது; (c) ஆக்கபூர்வமான கொள்கை ஒருங்கிணைப்பு தொடர்பானது—கொள்கை மற்றும் நடவடிக்கைகளின் சிறந்த ஒருங்கிணைப்பிற்காகப் பரிந்துரைகளை வழங்குதல். எனவே, பிரிவு (a) தகராறு சார்ந்தது, பிரிவு (c) கொள்கை ஒருங்கிணைப்பு சார்ந்தது.",
        "Neither clause applies to foreign disputes.", "எந்தப் பிரிவும் வெளிநாட்டுத் தகராறுகளுக்குப் பொருந்தாது.",
        "Military enforcement is completely foreign to Article 263.", "இராணுவ அமலாக்கம் உறுப்பு 263-க்கு முற்றிலும் தொடர்பற்றது.",
        "Option C correctly articulates the distinct roles of dispute inquiry (clause a) and policy coordination (clause c).", "விருப்பம் C தகராறு விசாரணை (பிரிவு a) மற்றும் கொள்கை ஒருங்கிணைப்பு (பிரிவு c) ஆகியவற்றுக்கு இடையேயான வேறுபாட்டைச் சரியாக விளக்குகிறது.",
        "No parliamentary majority is required under either clause; the Council is established by Presidential Order.", "எந்தப் பிரிவுக்கும் நாடாளுமன்றப் பெரும்பான்மை தேவையில்லை.",
        "Article 263 Architecture: Clause (a) = Inquiring into disputes; Clause (b) = Discussing common subjects; Clause (c) = Recommending policy coordination.",
        "உறுப்பு 263 கட்டமைப்பு: பிரிவு (a) = தகராறுகளை விசாரித்தல்; பிரிவு (b) = பொதுவான தலைப்புகளை விவாதித்தல்; பிரிவு (c) = கொள்கை ஒருங்கிணைப்பைப் பரிந்துரைத்தல்.",
        "Article 263(a) concerns dispute inquiry; Article 263(c) concerns policy coordination.",
        "உறுப்பு 263(a) தகராறு விசாரணையையும், உறுப்பு 263(c) கொள்கை ஒருங்கிணைப்பையும் குறிக்கிறது.",
        tags=["Article 263", "Clause (a) vs Clause (c)", "Council Mandate"]
    ))

    # 048 - Ans D
    q.append(make_q(
        "ISR_H_048", "Environmental Interplay",
        "When a State Government restricts the inter-State transportation of hazardous bio-medical waste across its territory under the Environment (Protection) Act, 1986, how is this restriction harmonized with Article 301?",
        "ஒரு மாநில அரசு 1986 ஆம் ஆண்டின் சுற்றுச்சூழல் (பாதுகாப்பு) சட்டத்தின் கீழ் தனது பகுதி வழியாக அபாயகரமான மருத்துவக் கழிவுகளை மாநிலங்களுக்கு இடையே கொண்டு செல்வதைக் கட்டுப்படுத்தும் போது, இந்தக் கட்டுப்பாடு உறுப்பு 301 உடன் எவ்வாறு இணக்கமாக்கப்படுகிறது?",
        "The restriction is unconstitutional because Article 301 protects the absolute free movement of all materials including toxic wastes.", "அனைத்து பொருட்களின் (நச்சு கழிவுகள் உட்பட) தடையற்ற இயக்கத்தை உறுப்பு 301 பாதுகாப்பதால் இக்கட்டுப்பாடு அரசியலமைப்பிற்கு முரணானது.",
        "Bio-medical waste is declared an item of Union List Entry 83, transferring all litigation to international courts.", "மருத்துவக் கழிவுகள் மத்தியப் பட்டியல் பதிவு 83-ன் ஒரு பொருளாக அறிவிக்கப்பட்டு, அனைத்து வழக்குகளும் சர்வதேச நீதிமன்றங்களுக்கு மாற்றப்படுகின்றன.",
        "The restriction is valid only if approved in advance by the Western Zonal Council.", "மேற்கு மண்டலக் குழுவால் முன்கூட்டியே அங்கீகரிக்கப்பட்டால் மட்டுமே இக்கட்டுப்பாடு செல்லும்.",
        "The restriction is valid as a reasonable public interest regulation under parliamentary environmental law; Article 301 protects lawful commerce and does not create an untrammeled right to transport noxious hazardous substances without regulatory compliance.", "நாடாளுமன்ற சுற்றுச்சூழல் சட்டத்தின் கீழான நியாயமான பொது நல ஒழுங்குமுறையாக இக்கட்டுப்பாடு செல்லுபடியாகும்; உறுப்பு 301 சட்டப்பூர்வ வர்த்தகத்தைப் பாதுகாக்கிறது மற்றும் ஒழுங்குமுறை இணக்கமின்றி தீங்கு விளைவிக்கும் அபாயகரமான பொருட்களைக் கொண்டு செல்வதற்கான தடையற்ற உரிமையை உருவாக்காது.",
        "D",
        "Freedom of trade under Article 301 is not an anarchic right to transport dangerous, hazardous, or noxious materials that threaten public health and safety. Regulations and restrictions enacted in the public interest under central statutes (like the Environment Protection Act 1986) or valid state rules to safeguard the environment and public health are legitimate regulatory restrictions that harmonize with Part XIII.",
        "உறுப்பு 301-ன் கீழான வர்த்தக சுதந்திரம் என்பது பொது சுகாதாரம் மற்றும் பாதுகாப்பிற்கு அச்சுறுத்தலாக இருக்கும் ஆபத்தான அல்லது தீங்கு விளைவிக்கும் பொருட்களைக் கொண்டு செல்வதற்கான கட்டுப்பாடற்ற உரிமை அல்ல. சுற்றுச்சூழலையும் பொது சுகாதாரத்தையும் பாதுகாக்க மத்தியச் சட்டங்களின் கீழ் (சுற்றுச்சூழல் பாதுகாப்புச் சட்டம் 1986 போன்றவை) பொது நலன் கருதி இயற்றப்படும் விதிமுறைகளும் கட்டுப்பாடுகளும் பகுதி XIII-உடன் இணங்கும் முறையான ஒழுங்குமுறைக் கட்டுப்பாடுகளாகும்.",
        "Hazardous wastes do not enjoy unrestricted transit immunity under Article 301.", "அபாயகரமான கழிவுகள் உறுப்பு 301-ன் கீழ் தடையற்ற விலக்கைப் பெற முடியாது.",
        "Bio-medical waste is not in Entry 83 (customs duties).", "மருத்துவக் கழிவுகள் பதிவு 83-ல் இல்லை.",
        "Zonal Council approval is not required.", "மண்டலக் குழு ஒப்புதல் தேவையில்லை.",
        "Option D correctly synthesizes public health/environmental regulations with Article 301 trade freedom.", "விருப்பம் D பொது சுகாதாரம்/சுற்றுச்சூழல் விதிமுறைகளை உறுப்பு 301 வர்த்தக சுதந்திரத்துடன் சரியாக இணைக்கிறது.",
        "Environmental & Public Health Regulation: Part XIII freedom does not immunize the transit of hazardous substances from reasonable health regulations.",
        "சுற்றுச்சூழல் மற்றும் பொது சுகாதார ஒழுங்குமுறை: பகுதி XIII சுதந்திரம் அபாயகரமான பொருட்களின் போக்குவரத்தை நியாயமான சுகாதார விதிமுறைகளிலிருந்து விடுவிக்காது.",
        "Environmental health regulations on hazardous waste are valid under Part XIII.",
        "அபாயகரமான கழிவுகள் மீதான சுற்றுச்சூழல் சுகாதார விதிமுறைகள் பகுதி XIII இன் கீழ் செல்லுபடியாகும்.",
        tags=["Part XIII", "Environmental Regulation", "Bio-Medical Waste"]
    ))

    # 049 - Ans A
    q.append(make_q(
        "ISR_H_049", "Constitutional Evolution",
        "How did the 42nd Constitutional Amendment Act, 1976 impact federal inter-State coordination regarding forests and wildlife protection?",
        "1976 ஆம் ஆண்டின் 42-வது அரசியலமைப்புத் திருத்தச் சட்டம் காடுகள் மற்றும் வனவிலங்குப் பாதுகாப்பு தொடர்பான கூட்டாட்சி மாநிலங்களுக்கிடையேயான ஒருங்கிணைப்பை எவ்வாறு பாதித்தது?",
        "It transferred 'Forests' and 'Protection of wild animals and birds' from the State List (List II) to the Concurrent List (List III), empowering Parliament to enact uniform national legislation across States.", "இது 'காடுகள்' மற்றும் 'காட்டு விலங்குகள் மற்றும் பறவைகள் பாதுகாப்பு' ஆகியவற்றை மாநிலப் பட்டியலிலிருந்து (பட்டியல் II) பொதுப் பட்டியலுக்கு (பட்டியல் III) மாற்றியது, இதன் மூலம் மாநிலங்கள் முழுவதும் சீரான தேசியச் சட்டங்களை இயற்ற நாடாளுமன்றத்திற்கு அதிகாரம் அளித்தது.",
        "It transferred all national parks directly into the Union List under exclusive central ownership.", "இது அனைத்து தேசியப் பூங்காக்களையும் பிரத்யேக மத்திய உரிமையின் கீழ் நேரடியாக மத்தியப் பட்டியலுக்கு மாற்றியது.",
        "It abolished all State forest departments and replaced them with a single central forest corps.", "இது அனைத்து மாநில வனத் துறைகளையும் ஒழித்துவிட்டு, அதற்குப் பதிலாக ஒற்றை மத்திய வனப் படையை அமைத்தது.",
        "It placed all wildlife sanctuaries under the direct judicial supervision of the Inter-State Council.", "இது அனைத்து வனவிலங்கு சரணாலயங்களையும் மாநிலங்களுக்கு இடையிலான மன்றத்தின் நேரடி நீதித்துறை மேற்பார்வையின் கீழ் வைத்தது.",
        "A",
        "The 42nd Amendment Act 1976 transferred five subjects from the State List to the Concurrent List: (1) Education; (2) Forests; (3) Protection of wild animals and birds; (4) Weights and measures; and (5) Administration of justice (subordinate courts). Transferring Forests and Wildlife to List III (Entries 17A and 17B) enabled Parliament to enact uniform federal legislation (such as the Forest Conservation Act 1980) and manage inter-state ecological corridors.",
        "1976 ஆம் ஆண்டின் 42-வது திருத்தச் சட்டம் மாநிலப் பட்டியலிலிருந்து ஐந்து பாடங்களைப் பொதுப் பட்டியலுக்கு மாற்றியது: (1) கல்வி; (2) காடுகள்; (3) காட்டு விலங்குகள் மற்றும் பறவைகள் பாதுகாப்பு; (4) எடைகள் மற்றும் அளவீடுகள்; (5) நீதி நிர்வாகம். காடுகள் மற்றும் வனவிலங்குகளைப் பொதுப் பட்டியலுக்கு (பதிவுகள் 17A மற்றும் 17B) மாற்றியது, சீரான கூட்டாட்சிச் சட்டங்களை (1980 வனப் பாதுகாப்புச் சட்டம் போன்றவை) இயற்றவும் மாநிலங்களுக்கிடையேயான சுற்றுச்சூழல் தாழ்வாரங்களை நிர்வகிக்கவும் நாடாளுமன்றத்திற்கு உதவியது.",
        "Option A accurately specifies the 42nd Amendment transfer of Forests and Wildlife to List III.", "விருப்பம் A காடுகள் மற்றும் வனவிலங்குகளைப் பொதுப் பட்டியலுக்கு மாற்றிய 42-வது திருத்தத்தைச் சரியாகக் குறிப்பிடுகிறது.",
        "National parks were not transferred exclusively to the Union List.", "தேசியப் பூங்காக்கள் மத்தியப் பட்டியலுக்கு மாற்றப்படவில்லை.",
        "State forest departments were not abolished.", "மாநில வனத் துறைகள் ஒழிக்கப்படவில்லை.",
        "The Inter-State Council does not have judicial supervision over sanctuaries.", "சரணாலயங்கள் மீது மன்றத்திற்கு நீதித்துறை மேற்பார்வை இல்லை.",
        "42nd Amendment (1976): Transferred Forests (Entry 17A) and Wildlife (Entry 17B) to Concurrent List, enabling national uniform legislation.",
        "42-வது திருத்தம் (1976): காடுகள் மற்றும் வனவிலங்குகளைப் பொதுப் பட்டியலுக்கு மாற்றியது, சீரான தேசியச் சட்டங்களை இயற்ற நாடாளுமன்றத்திற்கு வழிவகுத்தது.",
        "42nd Amendment transferred Forests and Wildlife to the Concurrent List.",
        "42-வது திருத்தம் காடுகள் மற்றும் வனவிலங்குகளைப் பொதுப் பட்டியலுக்கு மாற்றியது.",
        tags=["42nd Amendment", "Concurrent List", "Forests and Wildlife"]
    ))

    # 050 - Ans B
    q.append(make_q(
        "ISR_H_050", "Synthesis & Cooperative Federalism",
        "Which of the following statements best synthesizes the institutional evolution of 'Cooperative Federalism' in Inter-State Relations in India from 1950 to the present day?",
        "1950 முதல் இன்று வரை இந்தியாவில் மாநிலங்களுக்கு இடையிலான உறவுகளில் 'கூட்டுறவு கூட்டாட்சியின்' (Cooperative Federalism) நிறுவனப் பரிணாமத்தை பின்வரும் கூற்றுகளில் எது மிகச் சிறப்பாகத் தொகுத்துக் கூறுகிறது?",
        "Indian federalism has completely abandoned all constitutional dispute mechanisms in favor of unilateral central ordinances.", "இந்தியக் கூட்டாட்சி அனைத்து அரசியலமைப்புத் தகராறு முறைமைகளையும் முற்றிலுமாக கைவிட்டுவிட்டு, ஒருதலைப்பட்ச மத்திய அவசரச் சட்டங்களை ஆதரிக்கிறது.",
        "Indian federalism has evolved from initial reliance on strict legal adjudication under Article 131 to a multi-tiered architecture combining specialized tribunals (Art 262), statutory regional deliberative councils (Zonal Councils 1956, NEC 1971), permanent constitutional consensus bodies (Inter-State Council 1990), and joint fiscal federal councils (GST Council 2016).", "இந்தியக் கூட்டாட்சியானது ஆரம்பத்தில் உறுப்பு 131-ன் கீழான கடுமையான சட்டத் தீர்ப்பைச் சார்ந்திருந்த நிலையிலிருந்து, சிறப்புத் தீர்ப்பாயங்கள் (உறுப்பு 262), சட்டப்பூர்வ பிராந்திய ஆலோசனைக் குழுக்கள் (மண்டலக் குழுக்கள் 1956, NEC 1971), நிரந்தர அரசியலமைப்பு ஒருமித்த கருத்து அமைப்புகள் (மாநிலங்களுக்கு இடையிலான மன்றம் 1990) மற்றும் கூட்டுக் கூட்டாட்சி நிதி மன்றங்கள் (ஜிஎஸ்டி கவுன்சில் 2016) ஆகியவற்றை இணைக்கும் ஒரு பல அடுக்குக் கட்டமைப்பாகப் பரிணமித்துள்ளது.",
        "All inter-State relations are now managed solely through bilateral memoranda of understanding signed by State Governors without legislative backing.", "அனைத்து மாநிலங்களுக்கு இடையிலான உறவுகளும் இப்போது சட்டமன்ற ஆதரவின்றி மாநில ஆளுநர்களால் கையெழுத்திடப்பட்ட இருதரப்பு புரிந்துணர்வு ஒப்பந்தங்கள் மூலம் மட்டுமே நிர்வகிக்கப்படுகின்றன.",
        "The Constitution has replaced the Inter-State Council with the NITI Aayog Governing Council through a constitutional amendment.", "அரசியலமைப்பு ஒரு திருத்தத்தின் மூலம் மாநிலங்களுக்கு இடையிலான மன்றத்திற்குப் பதிலாக நிதி ஆயோக் ஆளுகை மன்றத்தை மாற்றியுள்ளது.",
        "B",
        "The trajectory of Inter-State Relations demonstrates a deepening of Cooperative Federalism: beginning with formal constitutional provisions in 1950 (Articles 261-263 and 301-307), progressing through statutory regional bodies in 1956 (Zonal Councils) and 1971 (NEC), establishing the constitutional Inter-State Council in 1990, strengthening tribunal execution in 2002 (IRWD amendment), and culminating in joint decision-making bodies like the GST Council under Article 279A. This multi-layered institutional matrix balances regional diversity with national economic and administrative unity.",
        "மாநிலங்களுக்கு இடையிலான உறவுகளின் வரலாறு கூட்டுறவு கூட்டாட்சியின் ஆழமடைதலைக் காட்டுகிறது: 1950-ல் முறையான அரசியலமைப்பு விதிகளுடன் தொடங்கி (உறுப்புகள் 261-263 மற்றும் 301-307), 1956 (மண்டலக் குழுக்கள்) மற்றும் 1971 (NEC) ஆகியவற்றில் சட்டப்பூர்வ பிராந்திய அமைப்புகளாக முன்னேறி, 1990-ல் அரசியலமைப்பு மாநிலங்களுக்கு இடையிலான மன்றத்தை நிறுவி, 2002-ல் தீர்ப்பாயச் செயலாக்கத்தைப் பலப்படுத்தி, உறுப்பு 279A-ன் கீழ் ஜிஎஸ்டி கவுன்சில் போன்ற கூட்டுக் கொள்கை அமைப்புகளில் உச்சத்தை எட்டியுள்ளது. இந்த பல அடுக்குக் கட்டமைப்பு பிராந்திய பன்முகத்தன்மையையும் தேசிய ஒற்றுமையையும் சமநிலைப்படுத்துகிறது.",
        "Indian federalism has not abandoned constitutional dispute mechanisms.", "இந்தியக் கூட்டாட்சி அரசியலமைப்பு முறைமைகளைக் கைவிடவில்லை.",
        "Option B presents the comprehensive, accurate historical and institutional synthesis of Cooperative Federalism in India.", "விருப்பம் B இந்தியாவில் கூட்டுறவு கூட்டாட்சியின் விரிவான, துல்லியமான வரலாற்று மற்றும் நிறுவனத் தொகுப்பை வழங்குகிறது.",
        "Governors' MoUs do not replace constitutional architecture.", "ஆளுநர்களின் ஒப்பந்தங்கள் அரசியலமைப்புக் கட்டமைப்பிற்கு மாற்றாக முடியாது.",
        "NITI Aayog has not replaced the Inter-State Council by constitutional amendment; both exist in distinct domains.", "நிதி ஆயோக் மாநிலங்களுக்கு இடையிலான மன்றத்தை அரசியலமைப்பு ரீதியாக மாற்றவில்லை.",
        "Cooperative Federalism Synthesis: Multi-tiered federal architecture (Tribunals + Zonal Councils + Inter-State Council + GST Council) balancing state autonomy with national integration.",
        "கூட்டுறவு கூட்டாட்சித் தொகுப்பு: பல அடுக்குக் கூட்டாட்சிக் கட்டமைப்பு (தீர்ப்பாயங்கள் + மண்டலக் குழுக்கள் + மாநிலங்களுக்கு இடையிலான மன்றம் + ஜிஎஸ்டி கவுன்சில்) மாநிலத் தன்னாட்சியையும் தேசிய ஒருமைப்பாட்டையும் சமநிலைப்படுத்துகிறது.",
        "Cooperative federalism is realized through a multi-tiered institutional architecture.",
        "கூட்டுறவு கூட்டாட்சி ஒரு பல அடுக்கு நிறுவனக் கட்டமைப்பு மூலம் உணரப்படுகிறது.",
        tags=["Cooperative Federalism", "Synthesis", "Inter-State Relations Architecture"]
    ))

    return q

if __name__ == "__main__":
    hard_qs = get_hard_questions()
    print(f"Total Hard Questions generated: {len(hard_qs)}")
    
    from collections import Counter
    cnt = Counter(q["correct_answer"] for q in hard_qs)
    print("Hard Answer Key Distribution:", dict(cnt))
    
    out_dir = Path(r"c:\Users\Home\Desktop\tnpsc_ai\data\questions\polity")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "inter_state_relations_hard.json"
    
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(hard_qs, f, indent=2, ensure_ascii=False)
    print(f"Saved to {out_file}")
