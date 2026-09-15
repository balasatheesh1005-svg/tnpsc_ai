# -*- coding: utf-8 -*-
"""
Special Provisions for States - Part 1 Medium MCQs Generator (50 MCQs: SPS_M_001 to SPS_M_050)
TNPSC Nova AI Content Engine
"""
import json
import os
from special_provisions_states_mcq_helper import make_sps_q
from tools.nova_content_engine.answer_randomizer import randomize_and_balance_dataset
from tools.nova_content_engine.validator import ContentValidator

def get_medium_questions():
    raw = [
        # 1
        {
            "subtopic": "Article 371 Governor Responsibility",
            "stem_en": "Under Article 371(2), in discharging his special responsibility for establishing separate development boards in Maharashtra and Gujarat, the Governor acts:",
            "stem_ta": "சரத்து 371(2)-ன் கீழ், மகாராஷ்டிரா மற்றும் குஜராத்தில் தனி வளர்ச்சி வாரியங்களை நிறுவுவதற்கான தனது சிறப்புப் பொறுப்பை நிறைவேற்றுவதில், ஆளுநர் எவ்வாறு செயல்படுகிறார்?",
            "options": [
                ("In his individual discretion, while consulting the State Council of Ministers", "மாநில அமைச்சரவையைக் கலந்தாலோசித்து, தனது தனிப்பட்ட விருப்பத்தின்படி"),
                ("Strictly bound by the mandatory advice of the Chief Minister alone", "முதலமைச்சரின் கட்டாய ஆலோசனைக்கு மட்டுமே முழுமையாகக் கட்டுப்பட்டு"),
                ("Only after obtaining prior written concurrence from the High Court Chief Justice", "உயர் நீதிமன்றத் தலைமை நீதிபதியின் முன் எழுத்துப்பூர்வ இசைவைப் பெற்ற பிறகே"),
                ("As a purely titular representative without any independent executive role", "எந்தவொரு தன்னாட்சி நிர்வாகப் பங்கும் இல்லாத பெயரளவுப் பிரதிநிதியாக")
            ],
            "correct_key": "A",
            "exp_en": "Under Article 371(2), the President by order confers 'special responsibility' on the Governor. In constitutional jurisprudence, wherever the Governor has a 'special responsibility', he exercises his discretion while consulting the Council of Ministers.",
            "exp_ta": "சரத்து 371(2)-ன் கீழ் குடியரசுத் தலைவர் ஆளுநருக்கு 'சிறப்புப் பொறுப்பை' வழங்குகிறார். அரசியலமைப்பு சட்டவியலின்படி, ஆளுநருக்கு சிறப்புப் பொறுப்பு இருக்கும் இடங்களில், அவர் அமைச்சரவையைக் கலந்தாலோசித்து தனது விருப்பத்தின்படி முடிவெடுக்கிறார்.",
            "why_a_en": "The Governor acts in his discretion after consultation with the Council of Ministers in matters of special responsibility under Article 371.",
            "why_a_ta": "சரத்து 371-ன் கீழான சிறப்புப் பொறுப்பு விவகாரங்களில் ஆளுநர் அமைச்சரவையைக் கலந்தாலோசித்து தனது விருப்பத்தின்படி செயல்படுகிறார்.",
            "why_b_en": "Special responsibility overrides the strict binding nature of ministerial advice.",
            "why_b_ta": "சிறப்புப் பொறுப்பு என்பது அமைச்சரவை ஆலோசனையின் கட்டாயத் தன்மையை விட மேலானது.",
            "why_c_en": "High Court concurrence is not required for governor's development board responsibilities.",
            "why_c_ta": "வளர்ச்சி வாரியப் பொறுப்புகளுக்கு உயர் நீதிமன்ற இசைவு தேவையில்லை.",
            "why_d_en": "The Governor is given an active constitutional role rather than a purely ceremonial one.",
            "why_d_ta": "ஆளுநருக்கு பெயரளவுப் பங்கு அல்லாமல் செயலில் உள்ள அரசியலமைப்புப் பங்கு வழங்கப்படுகிறது.",
            "tip_en": "Key distinction: 'Special responsibility' implies discretionary judgment after consultation (unlike ordinary aid-and-advice under Article 163).",
            "tip_ta": "முக்கிய வேறுபாடு: 'சிறப்புப் பொறுப்பு' என்பது கலந்தாலோசித்த பிறகு தனிப்பட்ட முடிவை குறிக்கிறது (சரத்து 163-ன் கீழ் வழக்கமான ஆலோசனை போல் அல்ல).",
            "fact_en": "Reports on the functioning of Vidarbha, Marathwada, Saurashtra, and Kutch boards must be placed annually before the respective state assemblies.",
            "fact_ta": "இவ்வாரியங்களின் செயல்பாடு குறித்த அறிக்கைகள் ஆண்டுதோறும் அந்தந்த மாநில சட்டமன்றங்களின் முன் வைக்கப்பட வேண்டும்."
        },
        # 2
        {
            "subtopic": "Article 371 Technical Education and Employment",
            "stem_en": "Which of the following is an explicit subject matter for which equitable allocation or arrangement is mandated under Article 371(2)?",
            "stem_ta": "சரத்து 371(2)-ன் கீழ் சமமான நிதி ஒதுக்கீடு அல்லது ஏற்பாடு கட்டாயமாக்கப்பட்டுள்ள குறிப்பிட்ட விவகாரம் எது?",
            "options": [
                ("Equitable arrangement providing adequate facilities for technical education and vocational training", "தொழில்நுட்பக் கல்வி மற்றும் தொழிற்பயிற்சிக்கு போதுமான வசதிகளை வழங்கும் சமமான ஏற்பாடு"),
                ("Reservation of 50 percent seats in the State Legislative Council", "மாநில சட்ட மேலவையில் 50 சதவீத இட ஒதுக்கீடு"),
                ("Creation of an autonomous military regiment for Vidarbha and Kutch", "விதர்பா மற்றும் கட்ச் பகுதிக்கு தன்னாட்சி ராணுவப் படைப்பிரிவை உருவாக்குதல்"),
                ("Exclusive imposition of agricultural income tax by the Governor", "ஆளுநரால் மட்டுமே விவசாய வருமான வரி விதிக்கப்படுவது")
            ],
            "correct_key": "A",
            "exp_en": "Article 371(2)(b) and (c) explicitly provide for equitable allocation of funds for developmental expenditure and an equitable arrangement providing adequate facilities for technical education and vocational training, and adequate opportunities for employment in services under the State.",
            "exp_ta": "சரத்து 371(2)(b) மற்றும் (c) வளர்ச்சிச் செலவினங்களுக்கான சமமான நிதி ஒதுக்கீடு மற்றும் தொழில்நுட்பக் கல்வி, தொழிற்பயிற்சி மற்றும் அரசுப் பணிகளில் போதுமான வேலைவாய்ப்புகளை வழங்குவதற்கான சமமான ஏற்பாடுகளைத் தெளிவாகக் கூறுகின்றன.",
            "why_a_en": "Article 371(2)(c) specifically mentions technical education and vocational training facilities.",
            "why_a_ta": "சரத்து 371(2)(c) தொழில்நுட்பக் கல்வி மற்றும் தொழிற்பயிற்சி வசதிகளை தெளிவாகக் குறிப்பிடுகிறது.",
            "why_b_en": "Legislative Council composition is governed by Article 171, not Article 371.",
            "why_b_ta": "சட்ட மேலவை அமைப்பு சரத்து 171-ஆல் நிர்வகிக்கப்படுகிறது, 371-ஆல் அல்ல.",
            "why_c_en": "Military matters are exclusively Union subjects under Union List Entry 1 and 2.",
            "why_c_ta": "ராணுவ விவகாரங்கள் மத்தியப் பட்டியல் பதிவுகள் 1 மற்றும் 2-ன் கீழ் ஒன்றியத்திற்கு மட்டுமே உரியவை.",
            "why_d_en": "Taxation powers are legislative, not conferred on the Governor personally.",
            "why_d_ta": "வரி விதிக்கும் அதிகாரம் சட்டமன்றத்திற்கு உரியது, ஆளுநருக்கு தனிப்பட்ட முறையில் வழங்கப்படவில்லை.",
            "tip_en": "Three sub-mandates of Article 371(2): (1) Development boards, (2) Equitable development funds, (3) Technical education & employment opportunities.",
            "tip_ta": "சரத்து 371(2)-ன் மூன்று முக்கிய கட்டளைகள்: (1) வளர்ச்சி வாரியங்கள், (2) சமமான வளர்ச்சி நிதி, (3) தொழிற்கல்வி & வேலைவாய்ப்பு.",
            "fact_en": "Vidarbha was transferred from Central Provinces (Madhya Pradesh) to bilingual Bombay State in 1956, and later to Maharashtra in 1960.",
            "fact_ta": "விதர்பா 1956-ல் மத்திய மாகாணங்களிலிருந்து பம்பாய் மாநிலத்திற்கும், பின்னர் 1960-ல் மகாராஷ்டிராவிற்கும் மாற்றப்பட்டது."
        },
        # 3
        {
            "subtopic": "Article 371A Naga Customary Autonomy",
            "stem_en": "Which of the following matters is NOT among the four protected subjects under Article 371A(1)(a) requiring a Nagaland Assembly resolution for central laws to apply?",
            "stem_ta": "சரத்து 371A(1)(a)-ன் கீழ் மத்திய சட்டங்கள் பொருந்த நாகாலாந்து சட்டமன்றத் தீர்மானம் தேவைப்படும் நான்கு பாதுகாக்கப்பட்ட துறைகளில் இடம்பெறாதது எது?",
            "options": [
                ("Regulation of foreign direct investment and atomic energy", "நேரடி அந்நிய முதலீடு மற்றும் அணுசக்தி ஒழுங்குமுறை"),
                ("Religious or social practices of the Nagas", "நாகர்களின் மத அல்லது சமூக நடைமுறைகள்"),
                ("Naga customary law and procedure", "நாகா மரபுச் சட்டம் மற்றும் நடைமுறை"),
                ("Ownership and transfer of land and its resources", "நிலம் மற்றும் அதன் வளங்களின் உரிமை மற்றும் பரிமாற்றம்")
            ],
            "correct_key": "A",
            "exp_en": "The four protected areas under Article 371A(1)(a) are: (i) religious or social practices of Nagas, (ii) Naga customary law and procedure, (iii) administration of civil and criminal justice involving decisions according to Naga customary law, and (iv) ownership and transfer of land and its resources. Foreign direct investment and atomic energy are exclusive Union subjects.",
            "exp_ta": "சரத்து 371A(1)(a)-ன் கீழ் பாதுகாக்கப்பட்ட 4 துறைகள்: (i) மத/சமூக நடைமுறைகள், (ii) மரபுச் சட்டம், (iii) மரபுசார் நீதி நிர்வாகம், (iv) நிலம் மற்றும் வளங்களின் உரிமை/பரிமாற்றம். அந்நிய முதலீடு மற்றும் அணுசக்தி ஆகியவை ஒன்றியத்தின் தனிப்பட்ட அதிகாரங்கள்.",
            "why_a_en": "FDI and atomic energy are Union List matters and not part of Article 371A customary exemptions.",
            "why_a_ta": "FDI மற்றும் அணுசக்தி ஆகியவை மத்தியப் பட்டியல் விவகாரங்கள், சரத்து 371A மரபுசார் விலக்குகளில் இல்லை.",
            "why_b_en": "Religious/social practices is item (i) of Article 371A(1)(a).",
            "why_b_ta": "மத/சமூக நடைமுறைகள் சரத்து 371A(1)(a)-ன் முதல் பகுதியாகும்.",
            "why_c_en": "Customary law is item (ii) of Article 371A(1)(a).",
            "why_c_ta": "மரபுச் சட்டம் சரத்து 371A(1)(a)-ன் இரண்டாம் பகுதியாகும்.",
            "why_d_en": "Ownership/transfer of land is item (iv) of Article 371A(1)(a).",
            "why_d_ta": "நில உரிமை/பரிமாற்றம் சரத்து 371A(1)(a)-ன் நான்காம் பகுதியாகும்.",
            "tip_en": "Note the word 'resources' in land ownership: Nagaland claims exclusive rights over petroleum and minerals on this basis.",
            "tip_ta": "நில உரிமை என்பதில் 'வளங்கள்' என்ற சொல் அடங்கும்: இதன் அடிப்படையில் நாகாலாந்து பெட்ரோலியம் மற்றும் கனிமங்கள் மீது உரிமை கோருகிறது.",
            "fact_en": "Nagaland Legislative Assembly passed a resolution in 2012 asserting sovereign control over petroleum extraction under Art 371A.",
            "fact_ta": "சரத்து 371A-ன் கீழ் பெட்ரோலியம் எடுப்பதில் இறையாண்மை உரிமையைக் கோரி நாகாலாந்து சட்டமன்றம் 2012-ல் தீர்மானம் நிறைவேற்றியது."
        },
        # 4
        {
            "subtopic": "Article 371A Law and Order Responsibility",
            "stem_en": "Under Article 371A(1)(b), the Governor of Nagaland has special responsibility for law and order so long as internal disturbances by hostile Nagas continue. In exercising this responsibility, the Governor:",
            "stem_ta": "சரத்து 371A(1)(b)-ன் கீழ், விரோத நாகர்களின் உள்நாட்டு குழப்பங்கள் தொடரும் வரை சட்டம் ஒழுங்குக்கு ஆளுநருக்கு சிறப்புப் பொறுப்பு உண்டு. இப்பொறுப்பை நிறைவேற்றுவதில் ஆளுநர்:",
            "options": [
                ("Exercises his individual judgment after consulting the Council of Ministers, and his decision is final", "அமைச்சரவையைக் கலந்தாலோசித்து தனது தனிப்பட்ட முடிவைப் பயன்படுத்துகிறார், மேலும் அவரது முடிவே இறுதியானது"),
                ("Must take the prior concurrence of the Speaker of the Legislative Assembly", "சட்டமன்ற சபாநாயகரின் முன் இசைவைப் பெற வேண்டும்"),
                ("Cannot take any action without unanimous Cabinet resolution", "அமைச்சரவையின் ஒருமனதான தீர்மானமின்றி எந்த நடவடிக்கையும் எடுக்க முடியாது"),
                ("Acts only on the advice of the Kohima Village Council", "கோஹிமா கிராம சபையின் ஆலோசனையின் பேரில் மட்டுமே செயல்படுகிறார்")
            ],
            "correct_key": "A",
            "exp_en": "Article 371A(1)(b) states that the Governor shall, after consulting the Council of Ministers, exercise his individual judgment as to the action to be taken, and the validity of anything done by the Governor shall not be called in question.",
            "exp_ta": "சரத்து 371A(1)(b) ஆளுநர் அமைச்சரவையைக் கலந்தாலோசித்த பிறகு எடுக்கப்பட வேண்டிய நடவடிக்கை குறித்து தனது தனிப்பட்ட முடிவைப் பயன்படுத்துவார் என்றும், அவரால் செய்யப்பட்ட எதையும் கேள்விக்குள்ளாக்க முடியாது என்றும் கூறுகிறது.",
            "why_a_en": "Article 371A(1)(b) explicitly provides for consultation with ministers and exercise of individual judgment.",
            "why_a_ta": "சரத்து 371A(1)(b) அமைச்சரவை ஆலோசனையையும் தனிப்பட்ட முடிவையும் தெளிவாகக் குறிப்பிடுகிறது.",
            "why_b_en": "Speaker's concurrence is not a constitutional requirement.",
            "why_b_ta": "சபாநாயகர் இசைவு ஓர் அரசியலமைப்புத் தேவையாக இல்லை.",
            "why_c_en": "Unanimous Cabinet approval is not required; the Governor can overrule the Cabinet.",
            "why_c_ta": "அமைச்சரவையின் ஒருமனதான ஒப்புதல் தேவையில்லை; ஆளுநர் அமைச்சரவையை மீறலாம்.",
            "why_d_en": "Village councils are traditional grassroots bodies, not the constitutional advisor under Art 371A(1)(b).",
            "why_d_ta": "கிராம சபைகள் பாரம்பரிய அமைப்புகள், சரத்து 371A(1)(b)-ன் கீழான ஆலோசகர் அல்ல.",
            "tip_en": "The President may direct that the Governor shall cease to have this special responsibility if satisfied that internal disturbances have ended.",
            "tip_ta": "உள்நாட்டுக் குழப்பங்கள் முடிவுக்கு வந்துவிட்டதாக திருப்தியடைந்தால் குடியரசுத் தலைவர் இச்சிறப்புப் பொறுப்பை முடிவுக்குக் கொண்டுவர உத்தரவிடலாம்.",
            "fact_en": "This discretionary power was given due to the armed insurgency active in the Naga Hills in the 1950s and 1960s.",
            "fact_ta": "1950 மற்றும் 1960-களில் நாகா மலைப்பகுதிகளில் நிலவிய ஆயுதமேந்திய கிளர்ச்சியின் காரணமாக இந்த விருப்புரிமை அதிகாரம் வழங்கப்பட்டது."
        },
        # 5
        {
            "subtopic": "Article 371A Tuensang Regional Council",
            "stem_en": "Regarding the administration of Tuensang district under Article 371A, which of the following statements is INCORRECT?",
            "stem_ta": "சரத்து 371A-ன் கீழ் டியூன்சாங் மாவட்ட நிர்வாகம் தொடர்பாக பின்வரும் கூற்றுகளில் எது தவறானது?",
            "options": [
                ("The Deputy Commissioner of Tuensang was barred from holding any office in the Regional Council", "டியூன்சாங் துணை ஆணையர் பிராந்தியக் குழுவில் எந்தப் பதவியையும் வகிக்கத் தடை விதிக்கப்பட்டது"),
                ("The Governor had special responsibility for the administration of Tuensang district for 10 years", "டியூன்சாங் மாவட்ட நிர்வாகத்திற்கு 10 ஆண்டுகளுக்கு ஆளுநருக்கு சிறப்புப் பொறுப்பு இருந்தது"),
                ("A Minister for Tuensang Affairs was appointed from among the members representing Tuensang district", "டியூன்சாங் மாவட்டத்தைப் பிரதிநிதித்துவப்படுத்தும் உறுப்பினர்களிலிருந்து டியூன்சாங் விவகாரங்களுக்கான அமைச்சர் நியமிக்கப்பட்டார்"),
                ("No Act of the Nagaland Legislature applied to Tuensang unless recommended by the Regional Council", "பிராந்தியக் குழு பரிந்துரைக்காத வரை நாகாலாந்து சட்டமன்றத்தின் எந்தச் சட்டமும் டியூன்சாங்கிற்குப் பொருந்தாது")
            ],
            "correct_key": "A",
            "exp_en": "Under Article 371A(2)(d), the Deputy Commissioner was the ex-officio Chairman of the Regional Council of Tuensang, so stating he was barred from holding any office is factually incorrect.",
            "exp_ta": "சரத்து 371A(2)(d)-ன் கீழ், டியூன்சாங் துணை ஆணையர் பிராந்தியக் குழுவின் பதவிவழித் தலைவராக இருந்தார். எனவே அவர் எந்தப் பதவியும் வகிக்கத் தடை விதிக்கப்பட்டது என்பது தவறான கூற்றாகும்.",
            "why_a_en": "The Deputy Commissioner was actually the ex-officio Chairman of the Regional Council.",
            "why_a_ta": "துணை ஆணையர் உண்மையில் பிராந்தியக் குழுவின் பதவிவழித் தலைவராக இருந்தார்.",
            "why_b_en": "Governor indeed had special responsibility for Tuensang for 10 years (Art 371A(2)(b)).",
            "why_b_ta": "10 ஆண்டுகளுக்கு ஆளுநருக்கு சிறப்புப் பொறுப்பு இருந்தது என்பது உண்மை.",
            "why_c_en": "A Minister for Tuensang Affairs was indeed chosen from Tuensang members (Art 371A(2)(c)).",
            "why_c_ta": "டியூன்சாங் விவகாரங்களுக்கான அமைச்சர் டியூன்சாங் உறுப்பினர்களிலிருந்து தேர்ந்தெடுக்கப்பட்டார் என்பது உண்மை.",
            "why_d_en": "Acts of Nagaland Legislature required Regional Council recommendation (Art 371A(2)(f)).",
            "why_d_ta": "நாகாலாந்து சட்டமன்றச் சட்டங்களுக்கு பிராந்தியக் குழுவின் பரிந்துரை தேவைப்பட்டது என்பது உண்மை.",
            "tip_en": "Tuensang was previously an unadministered tribal area under the Frontier Tracts administration before statehood.",
            "tip_ta": "மாநில அந்தஸ்திற்கு முன்பு டியூன்சாங் எல்லைப்புறப் பகுதிகள் நிர்வாகத்தின் கீழ் நிர்வகிக்கப்படாத பழங்குடிப் பகுதியாக இருந்தது.",
            "fact_en": "Members from Tuensang were initially not chosen by direct election but elected by the Regional Council.",
            "fact_ta": "துவக்கத்தில் டியூன்சாங் உறுப்பினர்கள் நேரடித் தேர்தல் மூலம் தேர்ந்தெடுக்கப்படாமல் பிராந்தியக் குழுவால் தேர்ந்தெடுக்கப்பட்டனர்."
        },
        # 6
        {
            "subtopic": "Article 371B Assam Committee",
            "stem_en": "What is the primary role of the Committee constituted under Article 371B in the Assam Legislative Assembly?",
            "stem_ta": "அசாம் சட்டமன்றத்தில் சரத்து 371B-ன் கீழ் அமைக்கப்பட்ட குழுவின் முதன்மைப் பங்கு என்ன?",
            "options": [
                ("Safeguarding the interests of the tribal areas of Assam through a dedicated legislative committee", "ஒரு பிரத்யேக சட்டமன்றக் குழு மூலம் அசாமின் பழங்குடிப் பகுதிகளின் நலன்களைப் பாதுகாப்பது"),
                ("Regulating the international border between Assam and Bangladesh", "அசாம் மற்றும் வங்காளதேசத்திற்கு இடையிலான சர்வதேச எல்லையை ஒழுங்குபடுத்துவது"),
                ("Directly appointing judges to the Gauhati High Court", "குவஹாத்தி உயர் நீதிமன்றத்திற்கு நீதிபதிகளை நேரடியாக நியமிப்பது"),
                ("Levying independent customs duty on tea production", "தேயிலை உற்பத்தி மீது தனித்துவமான சுங்க வரி விதிப்பது")
            ],
            "correct_key": "A",
            "exp_en": "Article 371B empowers the President to provide for the constitution and functions of a committee of the Legislative Assembly of Assam consisting of members elected from tribal areas to safeguard their legislative and developmental interests.",
            "exp_ta": "சரத்து 371B, அசாம் சட்டமன்றத்தில் பழங்குடிப் பகுதிகளிலிருந்து தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்களைக் கொண்ட குழுவை அமைத்து, அவர்களின் சட்டமன்ற மற்றும் வளர்ச்சி நலன்களைப் பாதுகாக்க குடியரசுத் தலைவருக்கு அதிகாரம் அளிக்கிறது.",
            "why_a_en": "Article 371B establishes a legislative committee representing tribal area constituencies.",
            "why_a_ta": "சரத்து 371B பழங்குடித் தொகுதிகளைப் பிரதிநிதித்துவப்படுத்தும் சட்டமன்றக் குழுவை அமைக்கிறது.",
            "why_b_en": "Border regulation is an exclusive Union defense/external affairs matter.",
            "why_b_ta": "எல்லைப் பாதுகாப்பு மத்திய அரசின் பாதுகாப்புத் துறைக்கு உட்பட்டது.",
            "why_c_en": "High Court judges are appointed under Article 217 by the President.",
            "why_c_ta": "உயர் நீதிமன்ற நீதிபதிகள் சரத்து 217-ன் கீழ் குடியரசுத் தலைவரால் நியமிக்கப்படுகின்றனர்.",
            "why_d_en": "Customs duties are exclusively levied by Parliament under Union List Entry 83.",
            "why_d_ta": "சுங்க வரிகள் நாடாளுமன்றத்தால் மட்டுமே விதிக்கப்படுகின்றன.",
            "tip_en": "Article 371B connects with Sixth Schedule Autonomous Councils in Assam (Karbi Anglong, Dima Hasao, Bodoland).",
            "tip_ta": "சரத்து 371B அசாமில் உள்ள ஆறாவது அட்டவணை தன்னாட்சிக் குழுக்களுடன் (கர்பி அங்லாங், திமா ஹசாவோ, போடோலாந்து) இணைகிறது.",
            "fact_en": "Article 371B was inserted when Meghalaya was carved out as an autonomous state within Assam in 1969.",
            "fact_ta": "1969-ல் அசாமிற்குள் மேகாலயா ஒரு தன்னாட்சி மாநிலமாக உருவாக்கப்பட்டபோது சரத்து 371B சேர்க்கப்பட்டது."
        },
        # 7
        {
            "subtopic": "Article 371C Manipur Hill Areas",
            "stem_en": "Under Article 371C(2), the executive power of the Union extends to giving directions to the State of Manipur regarding:",
            "stem_ta": "சரத்து 371C(2)-ன் கீழ், எந்த விவகாரம் தொடர்பாக மணிப்பூர் மாநிலத்திற்கு வழிகாட்டுதல்களை வழங்க ஒன்றியத்தின் நிர்வாக அதிகாரம் நீடிக்கிறது?",
            "options": [
                ("The administration of the Hill Areas of Manipur", "மணிப்பூரின் மலைப்பகுதிகளின் நிர்வாகம்"),
                ("The deployment of naval forces in Loktak Lake", "லோக்டாக் ஏரியில் கடற்படையை நிலைநிறுத்துவது"),
                ("The imposition of direct income tax on valley residents", "பள்ளத்தாக்கு வாசிகள் மீது நேரடி வருமான வரி விதிப்பது"),
                ("The alteration of the boundary with Myanmar", "மியான்மர் உடனான எல்லையை மாற்றுவது")
            ],
            "correct_key": "A",
            "exp_en": "Article 371C(2) explicitly provides: 'The executive power of the Union shall extend to the giving of directions to the State as to the administration of the said areas' (the Hill Areas of Manipur).",
            "exp_ta": "சரத்து 371C(2) தெளிவாகக் கூறுகிறது: 'மணிப்பூரின் மலைப்பகுதிகளின் நிர்வாகம் தொடர்பாக மாநிலத்திற்கு வழிகாட்டுதல்களை வழங்க ஒன்றியத்தின் நிர்வாக அதிகாரம் நீடிக்கும்'.",
            "why_a_en": "Article 371C(2) gives the Union executive directive power over Hill Areas administration.",
            "why_a_ta": "சரத்து 371C(2) மலைப்பகுதிகள் நிர்வாகம் குறித்து மத்திய அரசுக்கு வழிகாட்டும் அதிகாரத்தை அளிக்கிறது.",
            "why_b_en": "Naval deployment in lakes is absurd and unconstitutional.",
            "why_b_ta": "ஏரிகளில் கடற்படை நிலைநிறுத்தம் பொருத்தமற்றது.",
            "why_c_en": "Direct tax imposition is not an Article 371C directive matter.",
            "why_c_ta": "நேரடி வரி விதிப்பு சரத்து 371C-ன் கீழ் வராது.",
            "why_d_en": "International boundary treaties are governed by Article 253 and Union List Entry 14.",
            "why_d_ta": "சர்வதேச எல்லைகள் சரத்து 253-ன் கீழ் வருகின்றன.",
            "tip_en": "The Governor must submit an annual report to the President regarding the administration of the Hill Areas under Article 371C(2).",
            "tip_ta": "சரத்து 371C(2)-ன் கீழ் மலைப்பகுதிகள் நிர்வாகம் குறித்து ஆளுநர் குடியரசுத் தலைவருக்கு ஆண்டுதோறும் அறிக்கை அனுப்ப வேண்டும்.",
            "fact_en": "The Hill Areas constitute roughly 90% of Manipur's geographical area, inhabited mostly by Naga and Kuki tribes.",
            "fact_ta": "மலைப்பகுதிகள் மணிப்பூரின் நிலப்பரப்பில் சுமார் 90% ஆகும்; இங்கு பெரும்பாலும் நாகா மற்றும் குகி பழங்குடியினர் வாழ்கின்றனர்."
        },
        # 8
        {
            "subtopic": "Article 371D Presidential Order",
            "stem_en": "Under Article 371D, the President may by order provide for equitable opportunities in public employment and education in Andhra Pradesh and Telangana by:",
            "stem_ta": "சரத்து 371D-ன் கீழ், குடியரசுத் தலைவர் ஆந்திரா மற்றும் தெலங்கானாவில் அரசு வேலைவாய்ப்பு மற்றும் கல்வியில் எவ்வாறு சம வாய்ப்புகளை வழங்கலாம்?",
            "options": [
                ("Specifying parts of the State into different local areas and local cadres for admission and direct recruitment", "சேர்க்கை மற்றும் நேரடி நியமனத்திற்காக மாநிலத்தின் பகுதிகளை வெவ்வேறு உள்ளூர் பகுதிகள் மற்றும் உள்ளூர் பணியாளர்களாகக் குறிப்பிடுவதன் மூலம்"),
                ("Abolishing all reservation policies in state universities", "மாநிலப் பல்கலைக்கழகங்களில் அனைத்து இடஒதுக்கீட்டுக் கொள்கைகளையும் ஒழிப்பதன் மூலம்"),
                ("Transferring state recruitment entirely to UPSC", "மாநிலத் தேர்வுகளை முழுமையாக UPSC-க்கு மாற்றுவதன் மூலம்"),
                ("Directly appointing all state civil servants from the Central Secretariat", "மத்திய செயலகத்திலிருந்து அனைத்து மாநில அரசு ஊழியர்களையும் நேரடியாக நியமிப்பதன் மூலம்")
            ],
            "correct_key": "A",
            "exp_en": "Article 371D(1) and (2) authorize the President to require the state government to organize civil posts into local cadres for different parts of the state and specify local areas for direct recruitment and admission to universities.",
            "exp_ta": "சரத்து 371D(1) மற்றும் (2), மாநிலத்தின் வெவ்வேறு பகுதிகளுக்கு ஏற்ப அரசுப் பதவிகளை உள்ளூர் பணியாளர்களாக ஒழுங்கமைக்கவும், பல்கலைக்கழக சேர்க்கை மற்றும் நேரடி நியமனத்திற்கு உள்ளூர் பகுதிகளைக் குறிப்பிடவும் குடியரசுத் தலைவருக்கு அதிகாரம் அளிக்கிறது.",
            "why_a_en": "Article 371D(2) explicitly provides for organizing class/classes of posts into local cadres and specifying local areas.",
            "why_a_ta": "சரத்து 371D(2) உள்ளூர் பணியாளர்கள் மற்றும் உள்ளூர் பகுதிகளை உருவாக்குவதை தெளிவாகக் குறிப்பிடுகிறது.",
            "why_b_en": "It promotes equitable regional quotas, not abolition of affirmative action.",
            "why_b_ta": "இது பிராந்திய ஒதுக்கீட்டை ஊக்குவிக்கிறது, இடஒதுக்கீட்டை ஒழிப்பதல்ல.",
            "why_c_en": "State recruitments remain under APPSC / TSPSC.",
            "why_c_ta": "மாநிலத் தேர்வுகள் APPSC / TSPSC வசமே உள்ளன.",
            "why_d_en": "State civil services are governed by Part XIV, not centrally recruited under Art 371D.",
            "why_d_ta": "மாநிலப் பணிகள் பகுதி XIV-ன் கீழ் வருகின்றன.",
            "tip_en": "Presidential Order of 1975 created local zones in Andhra Pradesh to implement Article 371D.",
            "tip_ta": "சரத்து 371D-ஐ செயல்படுத்த 1975-ன் குடியரசுத் தலைவர் ஆணை ஆந்திராவில் உள்ளூர் மண்டலங்களை உருவாக்கியது.",
            "fact_en": "Under the AP Reorganisation Act 2014, Article 371D continues to apply separately to both residual Andhra Pradesh and Telangana.",
            "fact_ta": "2014 ஆந்திர மறுசீரமைப்புச் சட்டத்தின் கீழ் சரத்து 371D ஆந்திரா மற்றும் தெலங்கானா இரண்டிற்கும் தனித்தனியாகத் தொடர்ந்து பொருந்துகிறது."
        },
        # 9
        {
            "subtopic": "Article 371D Administrative Tribunal",
            "stem_en": "Article 371D(3) empowered the President to set up an Administrative Tribunal for Andhra Pradesh. In 2019, the AP Administrative Tribunal was:",
            "stem_ta": "சரத்து 371D(3) ஆந்திராவிற்கு ஒரு நிர்வாகத் தீர்ப்பாயத்தை அமைக்க குடியரசுத் தலைவருக்கு அதிகாரம் அளித்தது. 2019 ஆம் ஆண்டில் ஆந்திர நிர்வாகத் தீர்ப்பாயம்:",
            "options": [
                ("Abolished upon notification by the Central Government at the request of the State", "மாநில அரசின் வேண்டுகோளின் பேரில் மத்திய அரசின் அறிவிப்பின் மூலம் ஒழிக்கப்பட்டது"),
                ("Elevated to the status of a permanent bench of the Supreme Court", "உச்ச நீதிமன்றத்தின் நிரந்தர அமர்வாக தரம் உயர்த்தப்பட்டது"),
                ("Merged into the Central Administrative Tribunal (CAT) permanently", "மத்திய நிர்வாகத் தீர்ப்பாயத்துடன் (CAT) நிரந்தரமாக இணைக்கப்பட்டது"),
                ("Given jurisdiction over all inter-state river disputes", "அனைத்து மாநிலங்களுக்கு இடையேயான நதிநீர் தகராறுகளின் மீதும் அதிகார வரம்பு வழங்கப்பட்டது")
            ],
            "correct_key": "A",
            "exp_en": "The Andhra Pradesh Administrative Tribunal (APAT) established under Article 371D(3) was abolished in January 2019 by a notification of the Central Government following a request from the AP State Government and High Court.",
            "exp_ta": "சரத்து 371D(3)-ன் கீழ் அமைக்கப்பட்ட ஆந்திரப் பிரதேச நிர்வாகத் தீர்ப்பாயம் (APAT), ஆந்திர அரசு மற்றும் உயர் நீதிமன்றத்தின் வேண்டுகோளைத் தொடர்ந்து 2019 ஜனவரியில் மத்திய அரசின் அறிவிப்பால் கலைக்கப்பட்டது.",
            "why_a_en": "APAT was abolished in 2019, transferring service matters back to the High Court.",
            "why_a_ta": "2019-ல் APAT ஒழிக்கப்பட்டு, வழக்குகள் உயர் நீதிமன்றத்திற்கு மாற்றப்பட்டன.",
            "why_b_en": "An administrative tribunal cannot become a bench of the Supreme Court.",
            "why_b_ta": "ஒரு நிர்வாகத் தீர்ப்பாயம் உச்ச நீதிமன்ற அமர்வாக மாற முடியாது.",
            "why_c_en": "State service disputes were not merged into CAT; CAT handles only Central Government employees.",
            "why_c_ta": "மாநிலப் பணி வழக்குகள் CAT-ல் இணைக்கப்படவில்லை; CAT மத்திய அரசு ஊழியர்களை மட்டுமே கையாள்கிறது.",
            "why_d_en": "Inter-state river disputes are governed by tribunals under Article 262.",
            "why_d_ta": "நதிநீர் தகராறுகள் சரத்து 262-ன் கீழான தீர்ப்பாயங்களால் கையாளப்படுகின்றன.",
            "tip_en": "In P. Sambamurthy v. State of AP (1987), the Supreme Court struck down Article 371D clause (5) which had allowed state government to nullify tribunal orders.",
            "tip_ta": "சாம்பமூர்த்தி வழக்கில் (1987), தீர்ப்பாயத்தின் உத்தரவுகளை ரத்து செய்ய மாநில அரசுக்கு அனுமதியளித்த சரத்து 371D உட்பிரிவு (5)-ஐ உச்ச நீதிமன்றம் செல்லாது என அறிவித்தது.",
            "fact_en": "Clause (5) of Article 371D was held unconstitutional as a violation of judicial review and basic structure.",
            "fact_ta": "சரத்து 371D உட்பிரிவு (5) நீதித்துறை மறுஆய்வு மற்றும் அடிப்படை அமைப்பை மீறியதால் அரசியலமைப்பிற்கு முரணானது எனப்பட்டது."
        },
        # 10
        {
            "subtopic": "Article 371F Sikkim Sangha Seat",
            "stem_en": "Under Article 371F(f), Parliament may provide for reservation of seats in the Sikkim Legislative Assembly for different sections of the population. One unique seat is reserved for:",
            "stem_ta": "சரத்து 371F(f)-ன் கீழ், சிக்கிம் சட்டமன்றத்தில் பல்வேறு பிரிவினருக்கு இடஒதுக்கீடு செய்ய நாடாளுமன்றம் வகைசெய்யலாம். இதில் யாருக்கு ஒரு தனித்துவமான இடம் ஒதுக்கப்பட்டுள்ளது?",
            "options": [
                ("The Buddhist Sangha (monks in monasteries)", "பௌத்த சங்கம் (மடாலயத் துறவிகள்)"),
                ("Anglo-Indians residing in Gangtok", "கேங்டாக்கில் வசிக்கும் ஆங்கிலோ-இந்தியர்கள்"),
                ("Refugees from Tibet", "திபெத்திய அகதிகள்"),
                ("Tea plantation workers from Nepal", "நேபாளத்தைச் சேர்ந்த தேயிலைத் தோட்டத் தொழிலாளர்கள்")
            ],
            "correct_key": "A",
            "exp_en": "Article 371F(f) enables reservation of seats for protecting the rights and interests of different sections of Sikkim's population. Under the Representation of the People Act 1950 (as amended for Sikkim), 1 seat in the 32-member Assembly is reserved for the 'Sangha' (monasteries/monks).",
            "exp_ta": "சரத்து 371F(f) சிக்கிம் மக்களின் பல்வேறு பிரிவினரின் உரிமைகளைப் பாதுகாக்க இடஒதுக்கீடு செய்ய வகைசெய்கிறது. இதன் கீழ் 32 இடங்களைக் கொண்ட சட்டமன்றத்தில் 1 இடம் பௌத்த 'சங்கத்திற்கு' (மடாலயத் துறவிகள்) ஒதுக்கப்பட்டுள்ளது.",
            "why_a_en": "The Sangha seat in Sikkim Assembly is a unique constitutional constituency reserved for Buddhist monks.",
            "why_a_ta": "சிக்கிம் சட்டமன்றத்தில் உள்ள சங்கத் தொகுதி பௌத்த துறவிகளுக்காக ஒதுக்கப்பட்ட ஒரு தனித்துவமான தொகுதியாகும்.",
            "why_b_en": "There is no Anglo-Indian reserved seat in Sikkim under Art 371F.",
            "why_b_ta": "சரத்து 371F-ன் கீழ் ஆங்கிலோ-இந்தியர்களுக்கு இட ஒதுக்கீடு இல்லை.",
            "why_c_en": "Non-citizens/refugees cannot hold legislative seats.",
            "why_c_ta": "அகதிகள் சட்டமன்ற இடங்களை வகிக்க முடியாது.",
            "why_d_en": "Plantation workers do not have a dedicated religious/social seat under Art 371F.",
            "why_d_ta": "தோட்டத் தொழிலாளர்களுக்கு பிரத்யேகத் தொகுதி இல்லை.",
            "tip_en": "In R.C. Poudyal v. Union of India (1993), the Supreme Court upheld the constitutional validity of the Sangha seat under Article 371F.",
            "tip_ta": "ஆர்.சி. பௌடியால் வழக்கில் (1993), உச்ச நீதிமன்றம் சரத்து 371F-ன் கீழான சங்கத் தொகுதியின் அரசியலமைப்பு செல்லுபடியாகும் தன்மையை உறுதி செய்தது.",
            "fact_en": "In the Sangha constituency, only registered monks from recognized Buddhist monasteries can contest and vote.",
            "fact_ta": "சங்கத் தொகுதியில் அங்கீகரிக்கப்பட்ட மடாலயங்களைச் சேர்ந்த பதிவுசெய்த துறவிகள் மட்டுமே போட்டியிடவும் வாக்களிக்கவும் முடியும்."
        },
        # 11
        {
            "subtopic": "Article 371F Sikkim Governor Powers",
            "stem_en": "Under Article 371F(g), the Governor of Sikkim has special responsibility for:",
            "stem_ta": "சரத்து 371F(g)-ன் கீழ், சிக்கிம் ஆளுநருக்கு எதற்காக சிறப்புப் பொறுப்பு உள்ளது?",
            "options": [
                ("Peace and an equitable arrangement for ensuring social and economic advancement of different sections of the population", "அமைதி மற்றும் பல்வேறு பிரிவினரின் சமூக, பொருளாதார முன்னேற்றத்தை உறுதி செய்வதற்கான சமமான ஏற்பாடு"),
                ("Directly commanding international military operations along the Nathu La pass", "நாதுலா கணவாய் வழியிலான சர்வதேச ராணுவ நடவடிக்கைகளை நேரடியாக வழிநடத்துவது"),
                ("Levying independent customs duty on trade with China", "சீனாவுடனான வர்த்தகத்தின் மீது தனித்துவமான சுங்க வரி விதிப்பது"),
                ("Dismissing the Chief Minister without legislative floor test", "சட்டமன்ற வாக்கெடுப்பு இல்லாமலேயே முதலமைச்சரை பணிநீக்கம் செய்வது")
            ],
            "correct_key": "A",
            "exp_en": "Article 371F(g) vests the Governor of Sikkim with special responsibility for peace and for an equitable arrangement for ensuring the social and economic advancement of different sections of the population of Sikkim, subject to presidential direction.",
            "exp_ta": "சரத்து 371F(g) அமைதியை நிலைநாட்டவும், சிக்கிம் மக்களின் பல்வேறு பிரிவினரின் சமூக, பொருளாதார முன்னேற்றத்தை உறுதி செய்யும் சமமான ஏற்பாட்டிற்கும் ஆளுநருக்கு சிறப்புப் பொறுப்பை வழங்குகிறது.",
            "why_a_en": "Article 371F(g) explicitly specifies peace and equitable arrangement for social and economic advancement.",
            "why_a_ta": "சரத்து 371F(g) அமைதி மற்றும் சமூக, பொருளாதார முன்னேற்றத்திற்கான சமமான ஏற்பாட்டை தெளிவாகக் குறிப்பிடுகிறது.",
            "why_b_en": "Military command belongs strictly to the Union Government and Armed Forces.",
            "why_b_ta": "ராணுவக் கட்டளை மத்திய அரசு மற்றும் பாதுகாப்புப் படைகளுக்கு மட்டுமே உரியது.",
            "why_c_en": "International trade tariffs are federal under Union List Entry 41.",
            "why_c_ta": "சர்வதேச வர்த்தக வரிகள் மத்தியப் பட்டியல் பதிவு 41-ன் கீழ் வருகின்றன.",
            "why_d_en": "Governor cannot arbitrarily dismiss a CM enjoying majority (S.R. Bommai doctrine).",
            "why_d_ta": "பொம்மை தீர்ப்பின்படி பெரும்பான்மை உள்ள முதலமைச்சரை ஆளுநர் தன்னிச்சையாக நீக்க முடியாது.",
            "tip_en": "In exercising this function under Art 371F(g), the Governor acts in his discretion subject to directions from the President.",
            "tip_ta": "சரத்து 371F(g)-ன் கீழ் ஆளுநர் குடியரசுத் தலைவரின் வழிகாட்டுதலுக்கு உட்பட்டு தனது விருப்பத்தின்படி செயல்படுகிறார்.",
            "fact_en": "Sikkim has only one seat in the Lok Sabha and one seat in the Rajya Sabha.",
            "fact_ta": "சிக்கிமிற்கு மக்களவையில் 1 இடமும், மாநிலங்களவையில் 1 இடமும் மட்டுமே உள்ளது."
        },
        # 12
        {
            "subtopic": "Article 371G Mizoram Assembly Strength",
            "stem_en": "Under Article 371G(b), what is the minimum constitutionally prescribed number of members in the Legislative Assembly of Mizoram?",
            "stem_ta": "சரத்து 371G(b)-ன் படி, மிசோரம் சட்டமன்றத்தில் அரசியலமைப்பு ரீதியாக நிர்ணயிக்கப்பட்ட குறைந்தபட்ச உறுப்பினர்களின் எண்ணிக்கை என்ன?",
            "options": [
                ("40 members", "40 உறுப்பினர்கள்"),
                ("30 members", "30 உறுப்பினர்கள்"),
                ("50 members", "50 உறுப்பினர்கள்"),
                ("60 members", "60 உறுப்பினர்கள்")
            ],
            "correct_key": "A",
            "exp_en": "Article 371G(b) provides that the Legislative Assembly of the State of Mizoram shall consist of not less than forty members.",
            "exp_ta": "சரத்து 371G(b) மிசோரம் மாநில சட்டமன்றம் நாற்பது உறுப்பினர்களுக்குக் குறையாமல் இருக்க வேண்டும் என்று கூறுகிறது.",
            "why_a_en": "Article 371G(b) explicitly fixes the minimum at 40 members.",
            "why_a_ta": "சரத்து 371G(b) குறைந்தபட்ச எண்ணிக்கையை 40 உறுப்பினர்கள் என தெளிவாக நிர்ணயிக்கிறது.",
            "why_b_en": "30 members is the minimum for Sikkim (Art 371F) and Goa (Art 371I).",
            "why_b_ta": "30 உறுப்பினர்கள் என்பது சிக்கிம் (371F) மற்றும் கோவாவிற்கான (371I) குறைந்தபட்ச அளவாகும்.",
            "why_c_en": "50 is not a constitutional assembly threshold in India.",
            "why_c_ta": "50 என்பது இந்தியாவில் சட்டமன்றத்திற்கான அரசியலமைப்பு வரம்பு அல்ல.",
            "why_d_en": "60 is the general rule under Article 170(1).",
            "why_d_ta": "60 என்பது சரத்து 170(1)-ன் கீழான பொது விதி.",
            "tip_en": "Comparison: Sikkim = 30; Goa = 30; Mizoram = 40. Normal states under Art 170 = 60 to 500.",
            "tip_ta": "ஒப்பீடு: சிக்கிம் = 30; கோவா = 30; மிசோரம் = 40. சாதாரண மாநிலங்கள் = 60 முதல் 500 வரை.",
            "fact_en": "Mizoram was upgraded from a Union Territory to the 23rd State on 20 February 1987.",
            "fact_ta": "1987 பிப்ரவரி 20 அன்று மிசோரம் யூனியன் பிரதேசத்திலிருந்து 23வது மாநிலமாக தரம் உயர்த்தப்பட்டது."
        },
        # 13
        {
            "subtopic": "Article 371H Arunachal Pradesh Cessation",
            "stem_en": "Under Article 371H(a), who has the power to order that the Governor of Arunachal Pradesh shall cease to have special responsibility for law and order?",
            "stem_ta": "சரத்து 371H(a)-ன் கீழ், அருணாச்சலப் பிரதேச ஆளுநரின் சட்டம் ஒழுங்கு தொடர்பான சிறப்புப் பொறுப்பு முடிவுக்கு வருவதாக உத்தரவிடும் அதிகாரம் யாருக்கு உள்ளது?",
            "options": [
                ("The President of India, on receipt of a report from the Governor or otherwise", "ஆளுநரிடமிருந்து அறிக்கை பெற்ற பிறகோ அல்லது பிற வகையிலோ இந்தியக் குடியரசுத் தலைவர்"),
                ("The Chief Minister of Arunachal Pradesh by executive notification", "அருணாச்சலப் பிரதேச முதலமைச்சர் நிர்வாக அறிவிப்பு மூலம்"),
                ("The Parliament by passing a constitutional amendment under Article 368", "சரத்து 368-ன் கீழ் அரசியலமைப்புத் திருத்தத்தை நிறைவேற்றுவதன் மூலம் நாடாளுமன்றம்"),
                ("The Inter-State Council at its annual meeting", "மாநிலங்களுக்கு இடையேயான கவுன்சில் அதன் ஆண்டு கூட்டத்தில்")
            ],
            "correct_key": "A",
            "exp_en": "The proviso to Article 371H(a) states: 'Provided that if the President on receipt of a report from the Governor or otherwise is satisfied that it is no longer necessary that the Governor should have that responsibility, he may by order direct that the Governor shall cease to have such responsibility...'",
            "exp_ta": "சரத்து 371H(a)-ன் வரம்புரை: 'ஆளுநரின் அறிக்கை மூலமாகவோ அல்லது பிற வகையிலோ குடியரசுத் தலைவர் திருப்தியடைந்தால், ஆளுநருக்கு அந்தப் பொறுப்பு இனி தேவையில்லை என்று அவர் ஓர் ஆணையின் மூலம் নির্দেশிக்கலாம்...'",
            "why_a_en": "The President is specifically vested with the power to terminate the Governor's special responsibility by order.",
            "why_a_ta": "குடியரசுத் தலைவர் ஓர் ஆணை மூலம் ஆளுநரின் சிறப்புப் பொறுப்பை முடிவுக்குக் கொண்டுவர அதிகாரம் பெற்றுள்ளார்.",
            "why_b_en": "The Chief Minister has no power to terminate a constitutional presidential mandate.",
            "why_b_ta": "அரசியலமைப்புப் பொறுப்பை முடிவுக்குக் கொண்டுவர முதலமைச்சருக்கு அதிகாரம் இல்லை.",
            "why_c_en": "No amendment under Art 368 is required; an executive presidential order suffices.",
            "why_c_ta": "சரத்து 368-ன் கீழ் திருத்தம் தேவையில்லை; குடியரசுத் தலைவர் ஆணை போதுமானது.",
            "why_d_en": "Inter-State Council has advisory powers under Article 263, not executive termination powers.",
            "why_d_ta": "மாநிலங்களுக்கு இடையேயான கவுன்சிலுக்கு ஆலோசனை அதிகாரம் மட்டுமே உள்ளது.",
            "tip_en": "Also under Art 371H(b), the Legislative Assembly of Arunachal Pradesh shall consist of not less than 30 members.",
            "tip_ta": "சரத்து 371H(b)-ன் படி அருணாச்சலப் பிரதேச சட்டமன்றம் 30 உறுப்பினர்களுக்குக் குறையாமல் இருக்க வேண்டும்.",
            "fact_en": "Arunachal Pradesh currently has 60 members in its Legislative Assembly by virtue of state reorganization laws.",
            "fact_ta": "அருணாச்சலப் பிரதேசம் தற்போது தனது சட்டமன்றத்தில் 60 உறுப்பினர்களைக் கொண்டுள்ளது."
        },
        # 14
        {
            "subtopic": "Article 371J Kalyana-Karnataka Allocation",
            "stem_en": "Article 371J mandates an equitable allocation of funds for developmental expenditure over the Hyderabad-Karnataka region, subject to the requirement that:",
            "stem_ta": "சரத்து 371J ஹைதராபாத்-கர்நாடகா பகுதிக்கு வளர்ச்சிச் செலவினங்களுக்கான சமமான நிதி ஒதுக்கீட்டை எந்த நிபந்தனைக்கு உட்பட்டு கட்டாயமாக்குகிறது?",
            "options": [
                ("A report on the working of the development board shall be placed each year before the State Legislative Assembly", "வளர்ச்சி வாரியத்தின் செயல்பாடு குறித்த அறிக்கை ஒவ்வோர் ஆண்டும் மாநில சட்டமன்றத்தின் முன் வைக்கப்பட வேண்டும்"),
                ("The region must collect its own separate income tax", "இப்பகுதி தனது சொந்த தனி வருமான வரியை வசூலிக்க வேண்டும்"),
                ("The funds must be audited exclusively by the World Bank", "நிதி உலக வங்கியால் மட்டுமே தணிக்கை செய்யப்பட வேண்டும்"),
                ("All local laws must be approved by the Union Finance Commission", "அனைத்து உள்ளூர் சட்டங்களும் மத்திய நிதி ஆணையத்தால் அங்கீகரிக்கப்பட வேண்டும்")
            ],
            "correct_key": "A",
            "exp_en": "Article 371J(1)(b) mandates equitable allocation of funds for developmental expenditure over the region, and clause (1)(c) mandates that a report on the working of the board shall be placed each year before the State Legislative Assembly.",
            "exp_ta": "சரத்து 371J(1)(b) பிராந்திய வளர்ச்சிக்கு சமமான நிதி ஒதுக்கீட்டையும், பிரிவு (1)(c) வாரியத்தின் செயல்பாடு குறித்த அறிக்கையை ஆண்டுதோறும் மாநில சட்டமன்றத்தின் முன் வைப்பதையும் கட்டாயமாக்குகிறது.",
            "why_a_en": "Article 371J(1)(c) explicitly mandates placing the annual report before the State Assembly.",
            "why_a_ta": "சரத்து 371J(1)(c) ஆண்டு அறிக்கையை சட்டமன்றத்தின் முன் வைப்பதை கட்டாயமாக்குகிறது.",
            "why_b_en": "States cannot impose independent regional income taxes.",
            "why_b_ta": "மாநிலங்கள் தனி பிராந்திய வருமான வரிகளை விதிக்க முடியாது.",
            "why_c_en": "Constitutional audit is under CAG (Article 149), not the World Bank.",
            "why_c_ta": "அரசியலமைப்பு தணிக்கை CAG-ன் கீழ் வருகிறது.",
            "why_d_en": "Finance Commission has no role in approving state legislative statutes.",
            "why_d_ta": "மாநில சட்டங்களை அங்கீகரிப்பதில் நிதி ஆணையத்திற்கு எந்தப் பங்கும் இல்லை.",
            "tip_en": "The six districts of Kalyana-Karnataka: Bidar, Kalaburagi (Gulbarga), Yadgir, Raichur, Koppal, and Ballari (plus Vijayanagara).",
            "tip_ta": "கல்யாண-கர்நாடகாவின் ஆறு மாவட்டங்கள்: பீதர், கலபுரகி, யாத்கிர், ராய்ச்சூர், கொப்பல், மற்றும் பல்லாரி (மற்றும் விஜயநகரா).",
            "fact_en": "Reservation under Article 371J extends to seats in state educational institutions and posts in the state government.",
            "fact_ta": "சரத்து 371J-ன் கீழான இடஒதுக்கீடு மாநில கல்வி நிறுவனங்கள் மற்றும் அரசுப் பணிகளுக்கும் பொருந்தும்."
        },
        # 15
        {
            "subtopic": "Part XVI Scope and Purpose",
            "stem_en": "In the structural framework of the Indian Constitution, Part XVI (Articles 330-342A) differs from Part XXI (Articles 369-392) primarily because:",
            "stem_ta": "இந்திய அரசியலமைப்பின் கட்டமைப்பில், பகுதி XVI (சரத்துகள் 330-342A) பகுதி XXI-லிருந்து (சரத்துகள் 369-392) முதன்மையாக எவ்வாறு வேறுபடுகிறது?",
            "options": [
                ("Part XVI focuses on disadvantaged classes of citizens across India, whereas Part XXI focuses on specific geographical States and territories", "பகுதி XVI இந்தியா முழுவதும் உள்ள நலிவடைந்த குடிமக்கள் பிரிவினரைக் குறிக்கிறது, பகுதி XXI குறிப்பிட்ட புவியியல் மாநிலங்கள் மற்றும் பிரதேசங்களைக் குறிக்கிறது"),
                ("Part XVI contains only emergency provisions, while Part XXI contains judicial appointments", "பகுதி XVI அவசரகால விதிகளை மட்டுமே கொண்டுள்ளது, பகுதி XXI நீதிபதிகள் நியமனத்தைக் கொண்டுள்ளது"),
                ("Part XVI applies only to Union Territories, while Part XXI applies only to Sixth Schedule areas", "பகுதி XVI யூனியன் பிரதேசங்களுக்கு மட்டுமே பொருந்தும், பகுதி XXI 6வது அட்டவணைப் பகுதிகளுக்கு மட்டுமே பொருந்தும்"),
                ("Part XVI was completely repealed by the 44th Constitutional Amendment", "பகுதி XVI 44வது அரசியலமைப்புத் திருத்தத்தால் முற்றிலும் ரத்து செய்யப்பட்டது")
            ],
            "correct_key": "A",
            "exp_en": "Part XVI provides special class-based representation and safeguards for Scheduled Castes, Scheduled Tribes, Anglo-Indians, and Backward Classes throughout the country. Part XXI provides territorial and state-specific special provisions (Articles 371 to 371J) to accommodate asymmetrical federalism.",
            "exp_ta": "பகுதி XVI நாடு முழுவதிலும் உள்ள SC, ST, ஆங்கிலோ-இந்தியர் மற்றும் பிற்படுத்தப்பட்ட வகுப்பினருக்கான சிறப்புப் பிரதிநிதித்துவத்தை வழங்குகிறது. பகுதி XXI சமச்சீரற்ற கூட்டாட்சிக்கு ஏற்ப குறிப்பிட்ட மாநிலங்களுக்கான புவியியல் சிறப்பு ஏற்பாடுகளைக் (371-371J) கொண்டுள்ளது.",
            "why_a_en": "Part XVI is class-based affirmative action, whereas Part XXI is territory-based asymmetrical federalism.",
            "why_a_ta": "பகுதி XVI என்பது வகுப்பு அடிப்படையிலான பாதுகாப்பு, பகுதி XXI என்பது பகுதி அடிப்படையிலான கூட்டாட்சி ஏற்பாடு.",
            "why_b_en": "Emergency provisions are in Part XVIII, not Part XVI.",
            "why_b_ta": "அவசரகால விதிகள் பகுதி XVIII-ல் உள்ளன.",
            "why_c_en": "Union territories are governed under Part VIII (Articles 239-242).",
            "why_c_ta": "யூனியன் பிரதேசங்கள் பகுதி VIII-ன் கீழ் நிர்வகிக்கப்படுகின்றன.",
            "why_d_en": "Part XVI is active and vital, never repealed.",
            "why_d_ta": "பகுதி XVI ரத்து செய்யப்படவில்லை, உயிர்ப்புடன் உள்ளது.",
            "tip_en": "Remember the dichotomy: Part XVI = People/Classes; Part XXI = Places/States.",
            "tip_ta": "இருமைத்தன்மையை நினைவில் கொள்க: பகுதி XVI = மக்கள்/வகுப்பினர்; பகுதி XXI = இடங்கள்/மாநிலங்கள்.",
            "fact_en": "Both parts illustrate the adaptive, pluralistic nature of the Indian Constitution.",
            "fact_ta": "இரு பகுதிகளும் இந்திய அரசியலமைப்பின் நெகிழ்வான, பன்முகத்தன்மை கொண்ட தன்மையை விளக்குகின்றன."
        },
        # 16
        {
            "subtopic": "Article 330 Population Proportion",
            "stem_en": "According to Article 330(2), the number of seats reserved in any State or Union territory for Scheduled Castes or Scheduled Tribes in the Lok Sabha shall bear, as nearly as may be:",
            "stem_ta": "சரத்து 330(2)-ன் படி, மக்களவையில் எந்தவொரு மாநிலம் அல்லது யூனியன் பிரதேசத்திலும் SC அல்லது ST பிரிவினருக்கு ஒதுக்கப்படும் இடங்களின் எண்ணிக்கை எதற்கு விகிதாசாரமாக இருக்க வேண்டும்?",
            "options": [
                ("The same proportion to the total number of seats allotted to that State/UT as their population bears to the total population of that State/UT", "அந்த மாநிலத்தின் மொத்த மக்கள் தொகையில் அவர்களின் மக்கள் தொகை விகிதத்திற்கு ஏற்ப, அந்த மாநிலத்திற்கு ஒதுக்கப்பட்ட மொத்த இடங்களில் அதே விகிதத்தில்"),
                ("An equal number of seats (50:50) regardless of population numbers", "மக்கள் தொகை எண்ணிக்கையைப் பொருட்படுத்தாமல் சம எண்ணிக்கையிலான இடங்கள் (50:50)"),
                ("A fixed percentage of 27 percent across all States uniformly", "அனைத்து மாநிலங்களிலும் ஒரே சீராக 27 சதவீத நிலையான இடம்"),
                ("The proportion determined solely by the President without any demographic census data", "மக்கள் தொகை கணக்கெடுப்பு தரவு இல்லாமல் குடியரசுத் தலைவரால் மட்டுமே தீர்மானிக்கப்படும் விகிதம்")
            ],
            "correct_key": "A",
            "exp_en": "Article 330(2) explicitly provides that the number of reserved seats shall bear, as nearly as may be, the same proportion to the total number of seats allotted to that State or Union territory as the population of the SCs or STs bears to the total population of the State or Union territory.",
            "exp_ta": "சரத்து 330(2) மாநிலத்தின் மொத்த மக்கள் தொகையில் SC அல்லது ST மக்கள் தொகை கொண்டுள்ள அதே விகிதத்தில், அந்த மாநிலத்திற்கு ஒதுக்கப்பட்ட மொத்த மக்களவை இடங்களில் இடங்கள் ஒதுக்கப்பட வேண்டும் என்று கூறுகிறது.",
            "why_a_en": "Article 330(2) mandates exact proportionality based on the state's census population.",
            "why_a_ta": "சரத்து 330(2) மக்கள் தொகை கணக்கெடுப்பின்படி துல்லியமான விகிதாசார ஒதுக்கீட்டைக் கட்டாயமாக்குகிறது.",
            "why_b_en": "Equal 50:50 seat sharing is not the constitutional formula.",
            "why_b_ta": "50:50 என்பது அரசியலமைப்பு முறை அல்ல.",
            "why_c_en": "27 percent is OBC reservation in employment, not SC/ST legislative seat proportion.",
            "why_c_ta": "27 சதவீதம் என்பது வேலைவாய்ப்பில் OBC இடஒதுக்கீடு, சட்டமன்ற இடங்கள் அல்ல.",
            "why_d_en": "Seats cannot be arbitrarily fixed; they are census-driven and demarcated by Delimitation Commission.",
            "why_d_ta": "தன்னிச்சையாக நிர்ணயிக்க முடியாது; மக்கள் தொகை கணக்கெடுப்பின்படியே தொகுதி மறுவரையறை ஆணையத்தால் செய்யப்படுகிறது.",
            "tip_en": "Same principle of demographic proportionality applies to State Assemblies under Article 332(3).",
            "tip_ta": "இதே மக்கள் தொகை விகிதாசாரக் கொள்கை சரத்து 332(3)-ன் கீழ் மாநில சட்டமன்றங்களுக்கும் பொருந்தும்.",
            "fact_en": "Under Article 330(3), reservation is also provided for autonomous districts in Assam.",
            "fact_ta": "சரத்து 330(3)-ன் கீழ் அசாமில் உள்ள தன்னாட்சி மாவட்டங்களுக்கும் இட ஒதுக்கீடு வழங்கப்படுகிறது."
        },
        # 17
        {
            "subtopic": "Article 334 Sunset Clause Extensions",
            "stem_en": "Originally in 1950, Article 334 set the reservation of seats for SCs and STs and the nomination of Anglo-Indians to cease after a period of:",
            "stem_ta": "1950-ல் இயற்றப்பட்ட போது, சரத்து 334 SC/ST இடஒதுக்கீடு மற்றும் ஆங்கிலோ-இந்திய நியமனம் எத்தனை ஆண்டுகளுக்குப் பிறகு முடிவுக்கு வர வேண்டும் என்று நிர்ணயித்தது?",
            "options": [
                ("10 years from the commencement of the Constitution", "அரசியலமைப்பு நடைமுறைக்கு வந்ததிலிருந்து 10 ஆண்டுகள்"),
                ("20 years from the commencement of the Constitution", "அரசியலமைப்பு நடைமுறைக்கு வந்ததிலிருந்து 20 ஆண்டுகள்"),
                ("25 years from the commencement of the Constitution", "அரசியலமைப்பு நடைமுறைக்கு வந்ததிலிருந்து 25 ஆண்டுகள்"),
                ("50 years from the commencement of the Constitution", "அரசியலமைப்பு நடைமுறைக்கு வந்ததிலிருந்து 50 ஆண்டுகள்")
            ],
            "correct_key": "A",
            "exp_en": "Article 334 originally specified that the provisions relating to reservation of seats for SCs and STs and representation of Anglo-Indians shall cease to have effect on the expiration of a period of ten years from the commencement of the Constitution (i.e. 26 January 1960).",
            "exp_ta": "அரசியலமைப்பு தொடங்கிய பத்தாண்டுகள் முடிவில் (1960 ஜனவரி 26) SC/ST இடஒதுக்கீடு மற்றும் ஆங்கிலோ-இந்தியப் பிரதிநிதித்துவம் முடிவுக்கு வர வேண்டும் என்று சரத்து 334 முதலில் குறிப்பிட்டிருந்தது.",
            "why_a_en": "Originally Article 334 specified 10 years (until 1960).",
            "why_a_ta": "முதலில் சரத்து 334 பத்து ஆண்டுகளைக் (1960 வரை) குறிப்பிட்டிருந்தது.",
            "why_b_en": "20 years was the extension made by the 8th Amendment Act 1959.",
            "why_b_ta": "20 ஆண்டுகள் என்பது 1959-ன் 8வது திருத்தத்தால் செய்யப்பட்ட நீட்டிப்பு.",
            "why_c_en": "25 years was not an amendment milestone for Art 334.",
            "why_c_ta": "25 ஆண்டுகள் என்பது சரத்து 334-ன் திருத்த மைல்கல் அல்ல.",
            "why_d_en": "50 years was reached via the 79th Amendment 1999 (up to 2010).",
            "why_d_ta": "50 ஆண்டுகள் என்பது 1999-ன் 79வது திருத்தம் மூலம் எட்டப்பட்டது (2010 வரை).",
            "tip_en": "Timeline of Article 334 extensions: 8th CAA (to 20 yrs), 23rd CAA (to 30 yrs), 45th CAA (to 40 yrs), 62nd CAA (to 50 yrs), 79th CAA (to 60 yrs), 95th CAA (to 70 yrs), 104th CAA (to 80 yrs, up to 2030).",
            "tip_ta": "சரத்து 334 நீட்டிப்பு வரலாறு: 8வது திருத்தம் (20 வரை), 23வது (30 வரை), 45வது (40 வரை), 62வது (50 வரை), 79வது (60 வரை), 95வது (70 வரை), 104வது (80 வரை, 2030 வரை).",
            "fact_en": "Only legislative political reservations have a sunset clause in Art 334; employment and educational reservations (Arts 15 & 16) have no sunset clause.",
            "fact_ta": "சரத்து 334-ல் உள்ள காலக்கெடு சட்டமன்ற அரசியல் இடஒதுக்கீட்டிற்கு மட்டுமே; வேலைவாய்ப்பு மற்றும் கல்வி இடஒதுக்கீட்டிற்கு (15 & 16) காலக்கெடு இல்லை."
        },
        # 18
        {
            "subtopic": "Former Article 331 Anglo-Indians",
            "stem_en": "Prior to the 104th Constitutional Amendment Act 2019, under Article 331, how many members of the Anglo-Indian community could the President nominate to the Lok Sabha?",
            "stem_ta": "2019-ன் 104வது அரசியலமைப்புத் திருத்தத்திற்கு முன்பு, சரத்து 331-ன் கீழ் குடியரசுத் தலைவர் எத்தனை ஆங்கிலோ-இந்திய உறுப்பினர்களை மக்களவைக்கு நியமிக்க முடியும்?",
            "options": [
                ("Not more than two members", "இரண்டு உறுப்பினர்களுக்கு மிகாமல்"),
                ("Exactly five members", "சரியாக ஐந்து உறுப்பினர்கள்"),
                ("One member from each Union Territory", "ஒவ்வொரு யூனியன் பிரதேசத்திலிருந்தும் ஒரு உறுப்பினர்"),
                ("Twelve members having special knowledge in arts and science", "கலை மற்றும் அறிவியலில் சிறப்பு அறிவு கொண்ட 12 உறுப்பினர்கள்")
            ],
            "correct_key": "A",
            "exp_en": "Article 331 provided that the President may, if he is of opinion that the Anglo-Indian community is not adequately represented in the House of the People, nominate not more than two members of that community to the House.",
            "exp_ta": "சரத்து 331, மக்களவையில் ஆங்கிலோ-இந்திய சமூகத்திற்கு போதுமான பிரதிநிதித்துவம் இல்லை என்று குடியரசுத் தலைவர் கருதினால், அச்சமூகத்தைச் சேர்ந்த இரண்டு உறுப்பினர்களுக்கு மிகாமல் நியமிக்கலாம் என்று கூறியிருந்தது.",
            "why_a_en": "Article 331 explicitly authorized 'not more than two members'.",
            "why_a_ta": "சரத்து 331 'இரண்டு உறுப்பினர்களுக்கு மிகாமல்' என தெளிவாகக் குறிப்பிட்டிருந்தது.",
            "why_b_en": "Five members was never the constitutional quota for Anglo-Indians.",
            "why_b_ta": "ஐந்து உறுப்பினர்கள் என்பது அரசியலமைப்பு ஒதுக்கீடு அல்ல.",
            "why_c_en": "Nomination was pan-India, not per Union Territory.",
            "why_c_ta": "நியமனம் நாடு தழுவியது, யூனியன் பிரதேசம் வாரியானது அல்ல.",
            "why_d_en": "12 members are nominated by the President to the Rajya Sabha under Article 80(3).",
            "why_d_ta": "சரத்து 80(3)-ன் கீழ் மாநிலங்களவைக்கு 12 உறுப்பினர்கள் நியமிக்கப்படுகிறார்கள்.",
            "tip_en": "Corresponding state assembly nomination was Article 333 (1 member nominated by Governor).",
            "tip_ta": "மாநில சட்டமன்றத்திற்கான தொடர்புடைய நியமன சரத்து 333 (ஆளுநரால் நியமிக்கப்படும் 1 உறுப்பினர்).",
            "fact_en": "Frank Anthony, legendary Anglo-Indian leader, was nominated to the Lok Sabha eight times.",
            "fact_ta": "பிராங்க் அந்தோனி என்ற ஆங்கிலோ-இந்தியத் தலைவர் மக்களவைக்கு எட்டு முறை நியமிக்கப்பட்டார்."
        },
        # 19
        {
            "subtopic": "Article 338 Functions and Powers",
            "stem_en": "While investigating any complaint regarding deprivation of rights and safeguards of Scheduled Castes, the National Commission for Scheduled Castes (NCSC) under Article 338(8) has all the powers of:",
            "stem_ta": "SC பிரிவினரின் உரிமைகள் மற்றும் பாதுகாப்புகள் பறிக்கப்படுவது தொடர்பான புகார்களை விசாரிக்கும் போது, சரத்து 338(8)-ன் கீழ் தேசிய ஆணையம் (NCSC) எதனுடைய அனைத்து அதிகாரங்களையும் கொண்டுள்ளது?",
            "options": [
                ("A Civil Court trying a suit under the Code of Civil Procedure, 1908", "1908 உரிமையியல் நடைமுறைச் சட்டத்தின் கீழ் ஒரு வழக்கை விசாரிக்கும் உரிமையியல் நீதிமன்றத்தின் அதிகாரங்கள்"),
                ("A Criminal Sessions Court capable of awarding imprisonment directly", "நேரடியாக சிறைத்தண்டனை விதிக்கக்கூடிய குற்றவியல் அமர்வு நீதிமன்றம்"),
                ("The Supreme Court of India exercising original jurisdiction under Article 131", "சரத்து 131-ன் கீழ் அசல் அதிகார வரம்பைப் பயன்படுத்தும் உச்ச நீதிமன்றம்"),
                ("A military court-martial under the Army Act", "ராணுவச் சட்டத்தின் கீழான ராணுவ நீதிமன்றம் (கோர்ட் மார்ஷியல்)")
            ],
            "correct_key": "A",
            "exp_en": "Under Article 338(8), the Commission has all the powers of a civil court trying a suit, including summoning witnesses, enforcing attendance, discovery and production of documents, and requisitioning public records.",
            "exp_ta": "சரத்து 338(8)-ன் கீழ், சாட்சிகளை அழைப்பது, ஆவணங்களைக் கோருவது மற்றும் பொது ஆவணங்களைப் பெறுவது உட்பட ஒரு உரிமையியல் நீதிமன்றத்தின் அனைத்து அதிகாரங்களையும் ஆணையம் கொண்டுள்ளது.",
            "why_a_en": "Article 338(8) explicitly confers all powers of a Civil Court trying a suit under CPC.",
            "why_a_ta": "சரத்து 338(8) உரிமையியல் நீதிமன்றத்தின் அனைத்து அதிகாரங்களையும் தெளிவாக வழங்குகிறது.",
            "why_b_en": "NCSC is not a criminal court; it cannot convict or sentence any person.",
            "why_b_ta": "NCSC குற்றவியல் நீதிமன்றம் அல்ல; தண்டனை விதிக்க முடியாது.",
            "why_c_en": "It does not have the constitutional powers of the Supreme Court.",
            "why_c_ta": "இதற்கு உச்ச நீதிமன்றத்தின் அதிகார வரம்பு இல்லை.",
            "why_d_en": "Court-martial powers are military, completely separate under Army Act.",
            "why_d_ta": "ராணுவ நீதிமன்ற அதிகாரங்கள் முற்றிலும் வேறுபட்டவை.",
            "tip_en": "Same civil court powers are enjoyed by NCST (Article 338A(8)) and NCBC (Article 338B(8)).",
            "tip_ta": "இதே உரிமையியல் நீதிமன்ற அதிகாரங்களை NCST (338A(8)) மற்றும் NCBC (338B(8)) அமைப்புகளும் கொண்டுள்ளன.",
            "fact_en": "The recommendations of NCSC are advisory; however, government must explain reasons if recommendations are not accepted.",
            "fact_ta": "NCSC பரிந்துரைகள் ஆலோசனைக் கூறுகள் கொண்டவை; ஏற்காவிட்டால் அரசு அதற்கான காரணத்தை விளக்க வேண்டும்."
        },
        # 20
        {
            "subtopic": "Article 338 Consultation Requirement",
            "stem_en": "Under Article 338(9), who must be consulted by the Union and every State Government on all major policy matters affecting Scheduled Castes?",
            "stem_ta": "சரத்து 338(9)-ன் படி, SC பிரிவினரைப் பாதிக்கும் அனைத்து முக்கியக் கொள்கை விவகாரங்களிலும் ஒன்றிய அரசும் ஒவ்வொரு மாநில அரசும் யாரைக் கலந்தாலோசிக்க வேண்டும்?",
            "options": [
                ("The National Commission for Scheduled Castes", "பட்டியலிடப்பட்ட சாதியினருக்கான தேசிய ஆணையம் (NCSC)"),
                ("The Law Commission of India", "இந்திய சட்ட ஆணையம்"),
                ("The Comptroller and Auditor General of India", "இந்தியக் கணக்காய்வாளர் மற்றும் தணிக்கைத் தலைவர்"),
                ("The Union Public Service Commission exclusively", "மத்திய அரசுப் பணியாளர் தேர்வாணையம் மட்டுமே")
            ],
            "correct_key": "A",
            "exp_en": "Article 338(9) provides: 'The Union and every State Government shall consult the Commission on all major policy matters affecting Scheduled Castes.'",
            "exp_ta": "சரத்து 338(9) கூறுகிறது: 'SC பிரிவினரைப் பாதிக்கும் அனைத்து முக்கியக் கொள்கை விவகாரங்களிலும் ஒன்றிய அரசும் ஒவ்வொரு மாநில அரசும் தேசிய ஆணையத்தைக் கலந்தாலோசிக்க வேண்டும்'.",
            "why_a_en": "Article 338(9) explicitly mandates consultation with the NCSC.",
            "why_a_ta": "சரத்து 338(9) NCSC உடன் ஆலோசனை செய்வதைக் கட்டாயமாக்குகிறது.",
            "why_b_en": "Law Commission advises on legal reforms, not specific SC welfare policies.",
            "why_b_ta": "சட்ட ஆணையம் பொதுவான சட்ட சீர்திருத்தங்களை மட்டுமே ஆலோசிக்கிறது.",
            "why_c_en": "CAG conducts audits of government accounts (Arts 148-151).",
            "why_c_ta": "CAG அரசு கணக்குகளை மட்டுமே தணிக்கை செய்கிறது.",
            "why_d_en": "UPSC advises on civil service recruitments and disciplinary matters (Art 320).",
            "why_d_ta": "UPSC அரசுப் பணி நியமனங்கள் மற்றும் ஒழுங்கு நடவடிக்கைகளை மட்டுமே ஆலோசிக்கிறது.",
            "tip_en": "Parallel provisions: Article 338A(9) mandates consultation with NCST for STs; Article 338B(9) mandates consultation with NCBC for SEBCs.",
            "tip_ta": "இணை விதிகள்: ST விவகாரங்களில் NCST (338A(9)), SEBC விவகாரங்களில் NCBC (338B(9)) உடன் ஆலோசனை கட்டாயம்.",
            "fact_en": "Failure of governments to consult these commissions has frequently been condemned by parliamentary committees.",
            "fact_ta": "அரசுகள் இவ்வாணையங்களைக் கலந்தாலோசிக்கத் தவறுவதை நாடாளுமன்றக் குழுக்கள் பலமுறை கண்டித்துள்ளன."
        },
        # 21
        {
            "subtopic": "Article 342A Presidential List of SEBCs",
            "stem_en": "Article 342A, inserted by the 102nd Constitutional Amendment Act 2018, empowers whom to specify the Central List of Socially and Educationally Backward Classes?",
            "stem_ta": "2018-ன் 102வது அரசியலமைப்புத் திருத்தச் சட்டத்தால் சேர்க்கப்பட்ட சரத்து 342A, சமூக மற்றும் கல்வி ரீதியாக பிற்படுத்தப்பட்ட வகுப்பினரின் மத்தியப் பட்டியலைக் குறிப்பிடும் அதிகாரத்தை யாருக்கு வழங்குகிறது?",
            "options": [
                ("The President of India", "இந்தியக் குடியரசுத் தலைவர்"),
                ("The Governor of each State independently", "ஒவ்வொரு மாநில ஆளுநருக்கும் தனித்தனியாக"),
                ("The National Commission for Backward Classes Chairman alone", "NCBC தலைவர் மட்டுமே"),
                ("The Central Vigilance Commissioner", "மத்திய ஊழல் கண்காணிப்பு ஆணையர்")
            ],
            "correct_key": "A",
            "exp_en": "Under Article 342A(1), the President may with respect to any State or Union territory, and where it is a State after consultation with the Governor, by public notification specify the socially and educationally backward classes for the Central List.",
            "exp_ta": "சரத்து 342A(1)-ன் படி, குடியரசுத் தலைவர் ஒரு மாநிலத்தைப் பொறுத்தவரை ஆளுநரைக் கலந்தாலோசித்த பிறகு மத்தியப் பட்டியலுக்கான சமூக மற்றும் கல்வி ரீதியாக பிற்படுத்தப்பட்ட வகுப்பினரை பொது அறிவிப்பின் மூலம் குறிப்பிடலாம்.",
            "why_a_en": "Article 342A(1) specifically vests this notification power in the President.",
            "why_a_ta": "சரத்து 342A(1) அறிவிக்கை வெளியிடும் அதிகாரத்தை குடியரசுத் தலைவருக்கு வழங்குகிறது.",
            "why_b_en": "Governor cannot issue the central notification; he is only consulted.",
            "why_b_ta": "ஆளுநர் மத்திய அறிவிக்கையை வெளியிட முடியாது; அவரிடம் ஆலோசனை மட்டுமே பெறப்படுகிறது.",
            "why_c_en": "NCBC advises and hears representations, but the President notifies.",
            "why_c_ta": "NCBC பரிந்துரை மட்டுமே செய்கிறது, அறிவிப்பது குடியரசுத் தலைவர்.",
            "why_d_en": "Central Vigilance Commission deals with anti-corruption integrity under CVC Act 2003.",
            "why_d_ta": "மத்திய ஊழல் கண்காணிப்பு ஆணையம் ஊழல் தடுப்பு விவகாரங்களைக் கையாள்கிறது.",
            "tip_en": "Under Art 342A(2), once the Central List is notified, only Parliament by law can include or exclude entries.",
            "tip_ta": "சரத்து 342A(2)-ன் படி, மத்தியப் பட்டியல் அறிவிக்கப்பட்ட பின் நாடாளுமன்றச் சட்டம் மூலம் மட்டுமே அதில் திருத்தம் செய்ய முடியும்.",
            "fact_en": "The 105th Amendment 2021 added clause (3) to Art 342A explicitly preserving States' powers to maintain State SEBC lists.",
            "fact_ta": "2021-ன் 105வது திருத்தம் மாநிலங்கள் சொந்தப் பட்டியலைப் பராமரிக்க சரத்து 342A-ல் பிரிவு (3)-ஐ சேர்த்தது."
        },
        # 22
        {
            "subtopic": "Indra Sawhney Case 1992",
            "stem_en": "In the landmark Indra Sawhney v. Union of India (1992) case (Mandal Case), which of the following principles was laid down by the Supreme Court?",
            "stem_ta": "வரலாற்று சிறப்புமிக்க இந்திரா சாவ்னி எதிர் இந்திய ஒன்றியம் (1992) வழக்கில் (மண்டல் வழக்கு), உச்ச நீதிமன்றத்தால் வகுக்கப்பட்ட கொள்கை எது?",
            "options": [
                ("The 'Creamy Layer' must be excluded from backward classes, and total reservation should not exceed 50 percent", "'கிரீமி லேயர்' (முன்னேறிய பிரிவினர்) பிற்படுத்தப்பட்ட வகுப்பிலிருந்து விலக்கப்பட வேண்டும், மொத்த இடஒதுக்கீடு 50 சதவீதத்தை தாண்டக்கூடாது"),
                ("Reservation must be provided in all promotions across all services up to 50 percent", "அனைத்துப் பணிகளிலும் அனைத்துப் பதவி உயர்வுகளிலும் 50 சதவீதம் வரை இடஒதுக்கீடு வழங்கப்பட வேண்டும்"),
                ("Caste cannot be used as any indicator of backwardness in India", "இந்தியாவில் சாதியை பிற்படுத்தப்பட்ட தன்மையின் எந்தவொரு குறிகாட்டியாகவும் பயன்படுத்தக் கூடாது"),
                ("Economic backwardness alone can be the sole criterion under Article 16(4)", "சரத்து 16(4)-ன் கீழ் பொருளாதாரப் பின்தங்கிய நிலை மட்டுமே ஒரே அளவுகோலாக இருக்க முடியும்")
            ],
            "correct_key": "A",
            "exp_en": "In Indra Sawhney (1992), a 9-judge bench ruled that: (1) Backward classes under Art 16(4) can be identified on the basis of caste, (2) The Creamy Layer must be excluded, (3) Total reservation should not exceed 50% except in extraordinary circumstances, (4) No reservation in promotions.",
            "exp_ta": "இந்திரா சாவ்னி வழக்கில் (1992) 9 நீதிபதிகள் கொண்ட அமர்வு தீர்ப்பளித்தது: (1) சாதி அடிப்படையில் பிற்படுத்தப்பட்ட வகுப்பினரை அடையாளம் காணலாம், (2) கிரீமி லேயர் விலக்கப்பட வேண்டும், (3) அசாதாரண சூழ்நிலைகள் தவிர மொத்த இடஒதுக்கீடு 50% தாண்டக்கூடாது, (4) பதவி உயர்வில் இடஒதுக்கீடு கூடாது.",
            "why_a_en": "Exclusion of Creamy Layer and the 50% cap are primary holdings of Indra Sawhney.",
            "why_a_ta": "கிரீமி லேயர் விலக்கு மற்றும் 50% உச்ச வரம்பு ஆகியவை இந்திரா சாவ்னி வழக்கின் முக்கிய தீர்ப்புகளாகும்.",
            "why_b_en": "The SC explicitly barred reservation in promotions in Indra Sawhney.",
            "why_b_ta": "பதவி உயர்வில் இடஒதுக்கீட்டை இந்திரா சாவ்னி வழக்கில் நீதிமன்றம் தடை செய்தது.",
            "why_c_en": "The Court upheld caste as a valid starting point to identify social backwardness.",
            "why_c_ta": "சமூகப் பின்தங்கிய நிலையை அடையாளம் காண சாதியை ஒரு சரியான தொடக்கப் புள்ளியாக நீதிமன்றம் ஏற்றது.",
            "why_d_en": "The Court struck down 10% quota based purely on economic criteria under Article 16(4).",
            "why_d_ta": "பொருளாதார அளவுகோல் மட்டுமே கொண்ட 10% இடஒதுக்கீட்டை நீதிமன்றம் ரத்து செய்தது.",
            "tip_en": "The Creamy Layer principle applies to OBCs, but does NOT apply to SCs and STs unless decided by future larger benches.",
            "tip_ta": "கிரீமி லேயர் கொள்கை OBC-களுக்குப் பொருந்தும், ஆனால் SC மற்றும் ST-களுக்கு பொருந்தாது.",
            "fact_en": "Indra Sawhney also mandated the creation of a permanent statutory body for OBCs, which led to the NCBC Act 1993.",
            "fact_ta": "இந்திரா சாவ்னி தீர்ப்பு OBC-களுக்கான நிரந்தர சட்டப்பூர்வ அமைப்பை உருவாக்க கட்டளையிட்டது; இது 1993 NCBC சட்டத்திற்கு வழிவகுத்தது."
        },
        # 23
        {
            "subtopic": "M. Nagaraj Case 2006",
            "stem_en": "In M. Nagaraj v. Union of India (2006), the Supreme Court upheld the constitutional validity of Articles 16(4A) and 16(4B) subject to the State demonstrating:",
            "stem_ta": "எம். நாகராஜ் எதிர் இந்திய ஒன்றியம் (2006) வழக்கில், மாநில அரசு எதை நிரூபிப்பதற்கு உட்பட்டு சரத்துகள் 16(4A) மற்றும் 16(4B)-ன் அரசியலமைப்பு செல்லுபடியாகும் தன்மையை உச்ச நீதிமன்றம் உறுதி செய்தது?",
            "options": [
                ("Quantifiable data showing backwardness, inadequacy of representation, and overall administrative efficiency under Article 335", "பின்தங்கிய நிலை, போதிய பிரதிநிதித்துவமின்மை மற்றும் சரத்து 335-ன் கீழ் ஒட்டுமொத்த நிர்வாகத் திறன் ஆகியவற்றைக் காட்டும் அளவிடக்கூடிய தரவுகள்"),
                ("Approval of the Governor through an extraordinary ordinance", "சிறப்பு அவசரச் சட்டம் மூலம் ஆளுநரின் ஒப்புதல்"),
                ("Unanimous resolution passed by the State Legislative Council", "மாநில சட்ட மேலவையால் நிறைவேற்றப்பட்ட ஒருமனதான தீர்மானம்"),
                ("Exemption certificate issued by the Comptroller and Auditor General", "கணக்காய்வாளர் மற்றும் தணிக்கைத் தலைவரால் வழங்கப்பட்ட விலக்குச் சான்றிதழ்")
            ],
            "correct_key": "A",
            "exp_en": "In M. Nagaraj (2006), a 5-judge bench held that the State is not bound to make promotion reservations, but if it wishes to exercise its discretion, it must collect quantifiable data demonstrating: (1) backwardness of the class, (2) inadequacy of representation, and (3) maintenance of efficiency under Article 335.",
            "exp_ta": "எம். நாகராஜ் வழக்கில் (2006), பதவி உயர்வு இடஒதுக்கீட்டை அரசு வழங்க விரும்பினால்: (1) பின்தங்கிய நிலை, (2) போதிய பிரதிநிதித்துவமின்மை, (3) சரத்து 335-ன் கீழ் நிர்வாகத் திறன் ஆகியவற்றைக் காட்டும் அளவிடக்கூடிய தரவுகளை அரசு சேகரிக்க வேண்டும் என உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
            "why_a_en": "The three constitutional controlling criteria laid down in Nagaraj are backwardness, inadequacy of representation, and efficiency.",
            "why_a_ta": "நாகராஜ் வழக்கில் வகுக்கப்பட்ட 3 கட்டுப்பாட்டு அளவுகோல்கள்: பின்தங்கிய நிலை, பிரதிநிதித்துவமின்மை மற்றும் நிர்வாகத் திறன்.",
            "why_b_en": "Governor's ordinance cannot substitute for empirical quantifiable data.",
            "why_b_ta": "ஆளுநரின் அவசரச்சட்டம் ஆய்வுத் தரவுகளுக்கு மாற்றாகாது.",
            "why_c_en": "Council resolution cannot override the need for quantifiable data.",
            "why_c_ta": "மேலவைத் தீர்மானம் ஆய்வுத் தரவுகளின் தேவையை நீக்க முடியாது.",
            "why_d_en": "CAG has no jurisdiction over reservation prerequisites.",
            "why_d_ta": "இடஒதுக்கீட்டு முன்நிபந்தனைகளில் CAG-க்கு அதிகார வரம்பு இல்லை.",
            "tip_en": "In Jarnail Singh v. Lachhmi Narain Gupta (2018), the SC removed the requirement to collect quantifiable data on backwardness for SC/STs (since they are presumed backward), but retained the inadequacy of representation requirement.",
            "tip_ta": "ஜர்னைல் சிங் வழக்கில் (2018), SC/ST-க்கான பின்தங்கிய நிலை தரவுத் தேவையை நீதிமன்றம் நீக்கியது, ஆனால் போதிய பிரதிநிதித்துவமின்மை தரவுத் தேவையைத் தக்கவைத்துக் கொண்டது.",
            "fact_en": "Nagaraj judgment protected the 'Basic Structure' while validating the 77th, 81st, 82nd, and 85th Amendments.",
            "fact_ta": "நாகராஜ் தீர்ப்பு 77, 81, 82 மற்றும் 85வது திருத்தங்களை உறுதிசெய்து அடிப்படை அமைப்பைப் பாதுகாத்தது."
        },
        # 24
        {
            "subtopic": "Tamil Nadu 69% Reservation Act",
            "stem_en": "The Tamil Nadu Backward Classes, Scheduled Castes and Scheduled Tribes (Reservation of Seats in Educational Institutions and of Appointments or Posts in the Services under the State) Act, 1993 provides for what total percentage of reservation?",
            "stem_ta": "தமிழ்நாடு பிற்படுத்தப்பட்ட வகுப்பினர், பட்டியல் சாதியினர் மற்றும் பட்டியல் பழங்குடியினர் சட்டம், 1993 மொத்தம் எத்தனை சதவீத இடஒதுக்கீட்டை வழங்குகிறது?",
            "options": [
                ("69 percent", "69 சதவீதம்"),
                ("50 percent", "50 சதவீதம்"),
                ("60 percent", "60 சதவீதம்"),
                ("75 percent", "75 சதவீதம்")
            ],
            "correct_key": "A",
            "exp_en": "The Tamil Nadu Act 45 of 1994 provides for 69% reservation in state educational admissions and public employment: BCs (30%), MBC/DNC (20%), SCs (18%), and STs (1%).",
            "exp_ta": "1994-ன் தமிழ்நாடு சட்டம் 45, கல்வி மற்றும் அரசுப் பணிகளில் 69% இடஒதுக்கீட்டை வழங்குகிறது: BC (30%), MBC/DNC (20%), SC (18%), மற்றும் ST (1%).",
            "why_a_en": "Tamil Nadu provides 69% reservation under the 1994 Act.",
            "why_a_ta": "1994 சட்டத்தின் கீழ் தமிழ்நாடு 69% இடஒதுக்கீட்டை வழங்குகிறது.",
            "why_b_en": "50% is the ceiling cap of Indra Sawhney, which TN exceeded.",
            "why_b_ta": "50% என்பது இந்திரா சாவ்னி வழக்கின் உச்ச வரம்பு.",
            "why_c_en": "60% is not the Tamil Nadu reservation figure.",
            "why_c_ta": "60% என்பது தமிழ்நாட்டின் இடஒதுக்கீட்டு அளவு அல்ல.",
            "why_d_en": "75% is incorrect.",
            "why_d_ta": "75% என்பது தவறானது.",
            "tip_en": "To protect this 69% reservation from judicial invalidation under the Indra Sawhney 50% cap, Parliament passed the 76th Constitutional Amendment Act 1994 placing the TN Act in the Ninth Schedule.",
            "tip_ta": "இந்திரா சாவ்னி 50% வரம்பிலிருந்து இந்த 69% இடஒதுக்கீட்டைப் பாதுகாக்க, 1994-ன் 76வது திருத்தச் சட்டம் மூலம் இச்சட்டம் 9வது அட்டவணையில் சேர்க்கப்பட்டது.",
            "fact_en": "Tamil Nadu was the first state in independent India to give statutory protection to a reservation quota exceeding 50%.",
            "fact_ta": "சுதந்திர இந்தியாவில் 50%-க்கு அதிகமான இடஒதுக்கீட்டிற்கு சட்டப்பூர்வ பாதுகாப்பு அளித்த முதல் மாநிலம் தமிழ்நாடு ஆகும்."
        },
        # 25
        {
            "subtopic": "76th Constitutional Amendment 1994",
            "stem_en": "The 76th Constitutional Amendment Act, 1994 was enacted specifically to:",
            "stem_ta": "1994 ஆம் ஆண்டின் 76வது அரசியலமைப்புத் திருத்தச் சட்டம் எதற்காக குறிப்பாக இயற்றப்பட்டது?",
            "options": [
                ("Place the Tamil Nadu 69% Reservation Act, 1993 into the Ninth Schedule of the Constitution", "தமிழ்நாட்டின் 69% இடஒதுக்கீட்டுச் சட்டம் 1993-ஐ அரசியலமைப்பின் ஒன்பதாவது அட்டவணையில் சேர்க்க"),
                ("Establish the National Commission for Backward Classes", "பிற்படுத்தப்பட்ட வகுப்பினருக்கான தேசிய ஆணையத்தை நிறுவ"),
                ("Bifurcate the State of Jammu and Kashmir into two Union Territories", "ஜம்மு-காஷ்மீர் மாநிலத்தை இரண்டு யூனியன் பிரதேசங்களாகப் பிரிக்க"),
                ("Introduce 10% EWS reservation in central institutions", "மத்திய நிறுவனங்களில் 10% EWS இடஒதுக்கீட்டை அறிமுகப்படுத்த")
            ],
            "correct_key": "A",
            "exp_en": "The 76th Constitutional Amendment Act, 1994 added the Tamil Nadu Reservation Act, 1993 as Entry 257A in the Ninth Schedule, granting it protection under Article 31B from judicial challenge on the grounds of violating fundamental rights.",
            "exp_ta": "1994-ன் 76வது அரசியலமைப்புத் திருத்தச் சட்டம், தமிழ்நாட்டின் 1993 இடஒதுக்கீட்டுச் சட்டத்தை ஒன்பதாவது அட்டவணையில் பதிவு 257A-ஆகச் சேர்த்து, அடிப்படை உரிமைகளை மீறியதாக நீதிமன்றத்தில் சவால் செய்யப்படுவதிலிருந்து சரத்து 31B-ன் கீழ் பாதுகாப்பு அளித்தது.",
            "why_a_en": "76th CAA 1994 specifically placed the TN 69% Reservation Act into the Ninth Schedule.",
            "why_a_ta": "76வது திருத்தம் 1994 குறிப்பாக தமிழ்நாட்டின் 69% இடஒதுக்கீட்டுச் சட்டத்தை 9வது அட்டவணையில் சேர்த்தது.",
            "why_b_en": "NCBC was established as a statutory body in 1993 and constitutional body in 2018.",
            "why_b_ta": "NCBC 1993-ல் சட்டப்பூர்வமாகவும் 2018-ல் அரசியலமைப்பு அமைப்பாகவும் உருவாக்கப்பட்டது.",
            "why_c_en": "J&K Reorganisation was enacted in 2019.",
            "why_c_ta": "ஜம்மு-காஷ்மீர் மறுசீரமைப்பு 2019-ல் இயற்றப்பட்டது.",
            "why_d_en": "EWS reservation was introduced by the 103rd Amendment in 2019.",
            "why_d_ta": "EWS இடஒதுக்கீடு 2019-ன் 103வது திருத்தத்தால் கொண்டுவரப்பட்டது.",
            "tip_en": "In I.R. Coelho v. State of Tamil Nadu (2007), the SC held that laws placed in the Ninth Schedule after 24 April 1973 are open to judicial review if they violate the Basic Structure.",
            "tip_ta": "கோயலோ வழக்கில் (2007), 1973 ஏப்ரல் 24-க்குப் பிறகு 9வது அட்டவணையில் சேர்க்கப்பட்ட சட்டங்கள் அடிப்படை அமைப்பை மீறினால் நீதித்துறை மறுஆய்வுக்கு உட்பட்டவை என உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
            "fact_en": "The 69% quota continues to be applied in Tamil Nadu under interim orders of the Supreme Court.",
            "fact_ta": "உச்ச நீதிமன்றத்தின் இடைக்கால உத்தரவுகளின் கீழ் தமிழ்நாட்டில் 69% இடஒதுக்கீடு தொடர்ந்து நடைமுறையில் உள்ளது."
        },
        # 26
        {
            "subtopic": "Article 371A Customary Justice",
            "stem_en": "Under Article 371A(1)(a)(iii), the administration of civil and criminal justice in Nagaland involving decisions according to Naga customary law is protected such that:",
            "stem_ta": "சரத்து 371A(1)(a)(iii)-ன் கீழ், நாகா மரபுச் சட்டத்தின்படியான முடிவுகளை உள்ளடக்கிய நாகாலாந்தின் உரிமையியல் மற்றும் குற்றவியல் நீதி நிர்வாகம் எவ்வாறு பாதுகாக்கப்படுகிறது?",
            "options": [
                ("No Act of Parliament on this subject applies to Nagaland unless the State Legislative Assembly so decides by resolution", "மாநில சட்டமன்றம் தீர்மானம் மூலம் அவ்வாறு முடிவு செய்யாவிட்டால், இத்துறை தொடர்பான எந்தவொரு நாடாளுமன்றச் சட்டமும் நாகாலாந்திற்குப் பொருந்தாது"),
                ("The Supreme Court has no appellate jurisdiction over any case originating in Nagaland", "நாகாலாந்தில் தோன்றும் எந்தவொரு வழக்கின் மீதும் உச்ச நீதிமன்றத்திற்கு மேல்முறையீட்டு அதிகார வரம்பு கிடையாது"),
                ("All customary disputes must be adjudicated exclusively by the Union Law Minister", "அனைத்து மரபுசார் தகராறுகளும் மத்திய சட்ட அமைச்சரால் மட்டுமே தீர்க்கப்பட வேண்டும்"),
                ("Customary laws can be modified by the Governor without consulting tribal elders", "பழங்குடி மூத்தோரைக் கலந்தாலோசிக்காமல் ஆளுநரால் மரபுச் சட்டங்களை மாற்றியமைக்க முடியும்")
            ],
            "correct_key": "A",
            "exp_en": "Article 371A(1)(a)(iii) protects the administration of civil and criminal justice involving decisions according to Naga customary law from the automatic application of Central parliamentary statutes (such as the CrPC and CPC) without state assembly approval.",
            "exp_ta": "சரத்து 371A(1)(a)(iii) நாகா மரபுச் சட்டத்தின்படியான உரிமையியல் மற்றும் குற்றவியல் நீதி நிர்வாகத்தில், மாநில சட்டமன்றத்தின் ஒப்புதல் இல்லாமல் மத்திய நாடாளுமன்றச் சட்டங்கள் (CrPC மற்றும் CPC போன்றவை) தானாகப் பொருந்துவதிலிருந்து பாதுகாப்பு அளிக்கிறது.",
            "why_a_en": "Article 371A(1)(a)(iii) explicitly shields customary civil and criminal justice procedures from automatic parliamentary legislation.",
            "why_a_ta": "சரத்து 371A(1)(a)(iii) மரபுசார் நீதி நடைமுறைகளில் மத்திய சட்டங்கள் தானாகப் பொருந்துவதைத் தடுக்கிறது.",
            "why_b_en": "The Supreme Court retains its ultimate constitutional jurisdiction under Article 136.",
            "why_b_ta": "சரத்து 136-ன் கீழ் உச்ச நீதிமன்றம் தனது இறுதி அரசியலமைப்பு அதிகார வரம்பைத் தக்க வைத்துக் கொண்டுள்ளது.",
            "why_c_en": "Union Law Minister has no adjudicatory judicial role.",
            "why_c_ta": "மத்திய சட்ட அமைச்சருக்கு நீதி வழங்கும் பங்கு இல்லை.",
            "why_d_en": "Governor cannot unilaterally alter customary law.",
            "why_d_ta": "ஆளுநர் தன்னிச்சையாக மரபுச் சட்டங்களை மாற்ற முடியாது.",
            "tip_en": "Naga customary courts operate at the village level (Dobhashi courts) deciding disputes according to uncodified traditional practices.",
            "tip_ta": "நாகா மரபுசார் நீதிமன்றங்கள் கிராம மட்டத்தில் (தோபாஷி நீதிமன்றங்கள்) பாரம்பரிய நடைமுறைகளின்படி தகராறுகளைத் தீர்க்கின்றன.",
            "fact_en": "Formal Code of Civil Procedure (CPC) 1908 does not apply in its strict technical form to tribal areas of Nagaland.",
            "fact_ta": "1908 உரிமையியல் நடைமுறைச் சட்டம் (CPC) அதன் தொழில்நுட்ப வடிவில் நாகாலாந்தின் பழங்குடிப் பகுதிகளுக்குப் பொருந்தாது."
        },
        # 27
        {
            "subtopic": "Article 371B Sixth Schedule Linkage",
            "stem_en": "Under Article 371B, the committee of the Assam Legislative Assembly is formed with members elected from tribal areas specified in which part of the table appended to paragraph 20 of the Sixth Schedule?",
            "stem_ta": "சரத்து 371B-ன் கீழ், ஆறாவது அட்டவணையின் 20வது பத்தியுடன் இணைக்கப்பட்டுள்ள அட்டவணையின் எந்தப் பகுதியில் குறிப்பிடப்பட்டுள்ள பழங்குடிப் பகுதிகளிலிருந்து தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்களுடன் அசாம் சட்டமன்றக் குழு அமைக்கப்படுகிறது?",
            "options": [
                ("Part I", "பகுதி I"),
                ("Part II", "பகுதி II"),
                ("Part III", "பகுதி III"),
                ("Part IV", "பகுதி IV")
            ],
            "correct_key": "A",
            "exp_en": "Article 371B explicitly mentions members of the Assam Assembly elected from the tribal areas specified in Part I of the table appended to paragraph 20 of the Sixth Schedule (which enumerates the tribal areas of Assam).",
            "exp_ta": "சரத்து 371B ஆறாவது அட்டவணையின் பத்தி 20-ல் உள்ள அட்டவணையின் பகுதி I-ல் குறிப்பிடப்பட்டுள்ள பழங்குடிப் பகுதிகளிலிருந்து தேர்ந்தெடுக்கப்பட்ட அசாம் சட்டமன்ற உறுப்பினர்களைக் கொண்டு இக்குழு அமைக்கப்படுவதாக தெளிவாகக் குறிப்பிடுகிறது.",
            "why_a_en": "Part I of paragraph 20 Sixth Schedule table enumerates Assam's tribal areas.",
            "why_a_ta": "பகுதி I அசாமின் பழங்குடிப் பகுதிகளைப் பட்டியலிடுகிறது.",
            "why_b_en": "Part II contains Meghalaya's autonomous districts (Khasi Hills, Jaintia Hills, Garo Hills).",
            "why_b_ta": "பகுதி II மேகாலயாவின் தன்னாட்சி மாவட்டங்களைக் கொண்டுள்ளது.",
            "why_c_en": "Part III contains Tripura Tribal Areas.",
            "why_c_ta": "பகுதி III திரிபுரா பழங்குடிப் பகுதிகளைக் கொண்டுள்ளது.",
            "why_d_en": "Part IV contains Mizoram's autonomous districts (Chakma, Mara, Lai).",
            "why_d_ta": "பகுதி IV மிசோரமின் தன்னாட்சி மாவட்டங்களைக் கொண்டுள்ளது.",
            "tip_en": "Sixth Schedule table layout: Part I = Assam; Part II = Meghalaya; Part IIA = Tripura; Part III = Mizoram.",
            "tip_ta": "6வது அட்டவணை அமைப்பு: பகுதி I = அசாம்; பகுதி II = மேகாலயா; பகுதி IIA = திரிபுரா; பகுதி III = மிசோரம்.",
            "fact_en": "Bodoland Territorial Council (BTC) was subsequently added to Sixth Schedule under the 2003 tripartite accord.",
            "fact_ta": "போடோலாந்து பிராந்தியக் குழு (BTC) பின்னர் 2003 முத்தரப்பு ஒப்பந்தத்தின் கீழ் ஆறாவது அட்டவணையில் சேர்க்கப்பட்டது."
        },
        # 28
        {
            "subtopic": "Article 371C Governor Annual Report",
            "stem_en": "Under Article 371C(2), who is constitutionally obligated to make an annual report to the President regarding the administration of the Hill Areas of Manipur?",
            "stem_ta": "சரத்து 371C(2)-ன் கீழ், மணிப்பூரின் மலைப்பகுதிகள் நிர்வாகம் குறித்து குடியரசுத் தலைவருக்கு ஆண்டுதோறும் அறிக்கை அளிக்க அரசியலமைப்பு ரீதியாக கடமைப்பட்டுள்ளவர் யார்?",
            "options": [
                ("The Governor of Manipur", "மணிப்பூர் ஆளுநர்"),
                ("The Chief Minister of Manipur", "மணிப்பூர் முதலமைச்சர்"),
                ("The Chairman of the Hill Areas Committee", "மலைப்பகுதிகள் குழுவின் தலைவர்"),
                ("The Chief Justice of the Manipur High Court", "மணிப்பூர் உயர் நீதிமன்றத் தலைமை நீதிபதி")
            ],
            "correct_key": "A",
            "exp_en": "Article 371C(2) mandates: 'The Governor shall annually, or whenever so required by the President, make a report to the President regarding the administration of the Hill Areas in the State of Manipur...'",
            "exp_ta": "சரத்து 371C(2) விதிக்கிறது: 'மணிப்பூர் மாநிலத்தின் மலைப்பகுதிகள் நிர்வாகம் குறித்து ஆளுநர் ஆண்டுதோறும் அல்லது குடியரசுத் தலைவர் கோரும் போதெல்லாம் குடியரசுத் தலைவருக்கு அறிக்கை அளிக்க வேண்டும்...'",
            "why_a_en": "Article 371C(2) places this direct obligation on the Governor of Manipur.",
            "why_a_ta": "சரத்து 371C(2) இக்கடமையை மணிப்பூர் ஆளுநரின் மீது நேரடியாக விதிக்கிறது.",
            "why_b_en": "The Chief Minister reports to the Governor, not directly an annual constitutional report to the President under Art 371C.",
            "why_b_ta": "முதலமைச்சர் ஆளுநருக்கு அறிக்கை அளிக்கிறார், சரத்து 371C-ன் கீழ் குடியரசுத் தலைவருக்கு அல்ல.",
            "why_c_en": "The Hill Areas Committee Chairman reports within the State Legislature framework.",
            "why_c_ta": "மலைப்பகுதிகள் குழுத் தலைவர் சட்டமன்றக் கட்டமைப்புக்குள் அறிக்கை அளிக்கிறார்.",
            "why_d_en": "Judiciary has no reporting duty regarding executive tribal administration under Art 371C.",
            "why_d_ta": "நீதித்துறைக்கு சரத்து 371C-ன் கீழ் நிர்வாக அறிக்கை அளிக்கும் கடமை இல்லை.",
            "tip_en": "Similar annual reporting duties exist for Governors of Fifth Schedule states under Para 3 of Fifth Schedule.",
            "tip_ta": "ஐந்தாவது அட்டவணை பத்தி 3-ன் கீழ் 5வது அட்டவணை மாநிலங்களின் ஆளுநர்களுக்கும் இதே போன்ற ஆண்டு அறிக்கை அளிக்கும் கடமை உள்ளது.",
            "fact_en": "The Hill Areas Committee must be consulted on all legislation relating to land, customary law, and hill development in Manipur.",
            "fact_ta": "மணிப்பூரில் நிலம், மரபுச் சட்டம் மற்றும் மலைப்பகுதி வளர்ச்சி தொடர்பான அனைத்து சட்டங்களிலும் மலைப்பகுதிகள் குழுவைக் கலந்தாலோசிக்க வேண்டும்."
        },
        # 29
        {
            "subtopic": "Article 371D Educational Cadres",
            "stem_en": "In what year did the President issue the landmark Andhra Pradesh Educational Institutions (Regulation of Admissions) Order under Article 371D?",
            "stem_ta": "சரத்து 371D-ன் கீழ் ஆந்திரப் பிரதேச கல்வி நிறுவனங்கள் (சேர்க்கை ஒழுங்குமுறை) உத்தரவை குடியரசுத் தலைவர் எந்த ஆண்டில் வெளியிட்டார்?",
            "options": [
                ("1974", "1974"),
                ("1971", "1971"),
                ("1980", "1980"),
                ("1992", "1992")
            ],
            "correct_key": "A",
            "exp_en": "The Andhra Pradesh Educational Institutions (Regulation of Admissions) Order was promulgated by the President in 1974 under Article 371D, dividing the state into three university areas: Andhra, Osmania, and Sri Venkateswara.",
            "exp_ta": "சரத்து 371D-ன் கீழ் 1974 ஆம் ஆண்டில் குடியரசுத் தலைவரால் ஆந்திரப் பிரதேச கல்வி நிறுவனங்கள் (சேர்க்கை ஒழுங்குமுறை) ஆணை பிறப்பிக்கப்பட்டது. இது மாநிலத்தை ஆந்திரா, உஸ்மானியா மற்றும் ஸ்ரீ வெங்கடேஸ்வரா என மூன்று பல்கலைக்கழகப் பகுதிகளாகப் பிரித்தது.",
            "why_a_en": "The Presidential Educational Order was issued in 1974 immediately following the 32nd CAA 1973.",
            "why_a_ta": "1973-ன் 32வது திருத்தத்தைத் தொடர்ந்து 1974-ல் குடியரசுத் தலைவரின் கல்வி ஆணை வெளியிடப்பட்டது.",
            "why_b_en": "1971 was prior to the enactment of the 32nd Amendment Act.",
            "why_b_ta": "1971 என்பது 32வது திருத்தச் சட்டத்திற்கு முந்தைய ஆண்டு.",
            "why_c_en": "1980 is not the year of promulgation of this foundational order.",
            "why_c_ta": "1980 என்பது இவ்வாணை பிறப்பிக்கப்பட்ட ஆண்டு அல்ல.",
            "why_d_en": "1992 was the year of 73rd/74th Amendments and Indra Sawhney case.",
            "why_d_ta": "1992 என்பது 73/74வது திருத்தங்கள் மற்றும் இந்திரா சாவ்னி வழக்கின் ஆண்டு.",
            "tip_en": "Under this 1974 Order, 85% of non-state-wide seats in higher educational institutions are reserved for 'local candidates' of each university area.",
            "tip_ta": "இந்த 1974 ஆணையின் கீழ், உயர் கல்வி நிறுவனங்களில் 85% இடங்கள் ஒவ்வொரு பல்கலைக்கழகப் பகுதியின் 'உள்ளூர் விண்ணப்பதாரர்களுக்கு' ஒதுக்கப்படுகின்றன.",
            "fact_en": "This local reservation system prevented students from one region dominating medical and engineering admissions in another region.",
            "fact_ta": "இந்த உள்ளூர் இடஒதுக்கீட்டு முறை ஒரு பிராந்திய மாணவர்கள் மற்றொரு பிராந்தியத்தில் மருத்துவம் மற்றும் பொறியியல் சேர்க்கையில் ஆதிக்கம் செலுத்துவதைத் தடுத்தது."
        },
        # 30
        {
            "subtopic": "Article 371F Lepcha-Bhutia Protection",
            "stem_en": "Under Article 371F(f), seats in the Sikkim Assembly have been reserved to protect the rights of the indigenous Bhutia-Lepcha population. Currently, how many seats out of 32 are reserved for Bhutia-Lepcha communities?",
            "stem_ta": "சரத்து 371F(f)-ன் கீழ், பூர்வீக பூட்டியா-லெப்சா மக்களின் உரிமைகளைப் பாதுகாக்க சிக்கிம் சட்டமன்றத்தில் இடங்கள் ஒதுக்கப்பட்டுள்ளன. தற்போதுள்ள 32 இடங்களில் பூட்டியா-லெப்சா சமூகத்திற்கு எத்தனை இடங்கள் ஒதுக்கப்பட்டுள்ளன?",
            "options": [
                ("12 seats", "12 இடங்கள்"),
                ("2 seats", "2 இடங்கள்"),
                ("20 seats", "20 இடங்கள்"),
                ("30 seats", "30 இடங்கள்")
            ],
            "correct_key": "A",
            "exp_en": "Under the Representation of the People Act 1950 (as modified pursuant to Article 371F), 12 seats in the 32-member Sikkim Assembly are reserved for Bhutias and Lepchas (indigenous inhabitants), 2 for Scheduled Castes, 1 for the Sangha, and 17 are General.",
            "exp_ta": "சரத்து 371F-ன் படியான மக்கள் பிரதிநிதித்துவச் சட்டத்தின் கீழ், 32 இடங்களைக் கொண்ட சிக்கிம் சட்டமன்றத்தில் 12 இடங்கள் பூட்டியா மற்றும் லெப்சா பழங்குடியினருக்கும், 2 இடங்கள் SC-க்கும், 1 இடம் சங்கத்திற்கும், 17 பொது இடங்களாகவும் ஒதுக்கப்பட்டுள்ளன.",
            "why_a_en": "Exactly 12 seats are reserved for Bhutia-Lepcha communities in the Sikkim Assembly.",
            "why_a_ta": "சிக்கிம் சட்டமன்றத்தில் பூட்டியா-லெப்சா சமூகத்திற்கு சரியாக 12 இடங்கள் ஒதுக்கப்பட்டுள்ளன.",
            "why_b_en": "2 seats are reserved for Scheduled Castes in Sikkim.",
            "why_b_ta": "சிக்கிமில் 2 இடங்கள் பட்டியலிடப்பட்ட சாதியினருக்கு (SC) ஒதுக்கப்பட்டுள்ளன.",
            "why_c_en": "20 is incorrect.",
            "why_c_ta": "20 என்பது தவறானது.",
            "why_d_en": "30 is the constitutional minimum strength under Art 371F(a), not the reserved quota.",
            "why_d_ta": "30 என்பது சரத்து 371F(a)-ன் கீழான குறைந்தபட்ச பலம், இடஒதுக்கீடு அல்ல.",
            "tip_en": "Sikkim Assembly seat formula: 12 (Bhutia-Lepcha) + 2 (SC) + 1 (Sangha) + 17 (General) = 32 seats total.",
            "tip_ta": "சிக்கிம் சட்டமன்ற இடப் பகிர்வு: 12 (பூட்டியா-லெப்சா) + 2 (SC) + 1 (சங்கம்) + 17 (பொது) = மொத்தம் 32 இடங்கள்.",
            "fact_en": "The Supreme Court in R.C. Poudyal (1993) held that this historical reservation does not violate the principle of democracy or secularism.",
            "fact_ta": "பௌடியால் வழக்கில் (1993) உச்ச நீதிமன்றம் இந்த வரலாற்று இடஒதுக்கீடு ஜனநாயகம் அல்லது மதச்சார்பின்மையை மீறவில்லை என்று தீர்ப்பளித்தது."
        },
        # 31
        {
            "subtopic": "Article 371G Mizo Accord Linkage",
            "stem_en": "The enactment of Article 371G was a direct constitutional outcome of which historic peace accord signed in 1986?",
            "stem_ta": "1986 ஆம் ஆண்டு கையெழுத்தான எந்த வரலாற்று சிறப்புமிக்க அமைதி ஒப்பந்தத்தின் நேரடி அரசியலமைப்பு விளைவாக சரத்து 371G இயற்றப்பட்டது?",
            "options": [
                ("Mizo Peace Accord signed between Union Government and Mizo National Front (MNF)", "மத்திய அரசுக்கும் மிசோரம் தேசிய முன்னணிக்கும் (MNF) இடையே கையெழுத்தான மிசோரம் அமைதி ஒப்பந்தம்"),
                ("Shillong Accord signed with Naga Federal Government", "நாகா கூட்டாட்சி அரசுடன் கையெழுத்தான ஷில்லாங் ஒப்பந்தம்"),
                ("Assam Accord signed with All Assam Students Union", "அனைத்து அசாம் மாணவர் சங்கத்துடன் கையெழுத்தான அசாம் ஒப்பந்தம்"),
                ("Bodo Accord signed with Bodo Liberation Tigers", "போடோ விடுதலைப் புலிகளுடன் கையெழுத்தான போடோ ஒப்பந்தம்")
            ],
            "correct_key": "A",
            "exp_en": "The Mizo Peace Accord was signed on 30 June 1986 between the Government of India and the Mizo National Front (led by Laldenga), ending two decades of insurgency and leading to statehood under Article 371G.",
            "exp_ta": "1986 ஜூன் 30 அன்று இந்திய அரசிற்கும் லால்தெங்கா தலைமையிலான மிசோரம் தேசிய முன்னணிக்கும் (MNF) இடையே மிசோரம் அமைதி ஒப்பந்தம் கையெழுத்தானது. இது 20 ஆண்டுகால கிளர்ச்சியை முடிவுக்குக் கொண்டுவந்து சரத்து 371G-ன் கீழ் மாநில அந்தஸ்திற்கு வழிவகுத்தது.",
            "why_a_en": "Article 371G was the constitutional implementation of the 1986 Mizo Accord.",
            "why_a_ta": "சரத்து 371G என்பது 1986 மிசோரம் ஒப்பந்தத்தின் அரசியலமைப்புச் செயல்பாடாகும்.",
            "why_b_en": "Shillong Accord (1975) was signed with Naga underground groups.",
            "why_b_ta": "ஷில்லாங் ஒப்பந்தம் (1975) நாகா குழுக்களுடன் கையெழுத்தானது.",
            "why_c_en": "Assam Accord was signed on 15 August 1985 regarding foreigners identification.",
            "why_c_ta": "அசாம் ஒப்பந்தம் வெளிநாட்டினர் அடையாளம் தொடர்பாக 1985 ஆகஸ்ட் 15 அன்று கையெழுத்தானது.",
            "why_d_en": "Bodo Accords were signed in 1993, 2003, and 2020.",
            "why_d_ta": "போடோ ஒப்பந்தங்கள் 1993, 2003 மற்றும் 2020-ல் கையெழுத்தாயின.",
            "tip_en": "Mizo Accord is widely regarded as one of the most successful peace accords in post-independence India.",
            "tip_ta": "சுதந்திரத்திற்குப் பிந்தைய இந்தியாவில் மிகவும் வெற்றிகரமான அமைதி ஒப்பந்தங்களில் ஒன்றாக மிசோரம் ஒப்பந்தம் கருதப்படுகிறது.",
            "fact_en": "Laldenga subsequently took oath as the first Chief Minister of the full State of Mizoram.",
            "fact_ta": "பின்னர் லால்தெங்கா முழு மிசோரம் மாநிலத்தின் முதல் முதலமைச்சராகப் பதவியேற்றார்."
        },
        # 32
        {
            "subtopic": "Article 371H Arunachal Council of Ministers Consultation",
            "stem_en": "Under Article 371H(a), although the Governor exercises individual judgment regarding law and order in Arunachal Pradesh, what is the mandatory procedural requirement before taking action?",
            "stem_ta": "சரத்து 371H(a)-ன் கீழ், அருணாச்சலப் பிரதேசத்தில் சட்டம் ஒழுங்கு தொடர்பாக ஆளுநர் தனது தனிப்பட்ட முடிவைப் பயன்படுத்தினாலும், நடவடிக்கை எடுப்பதற்கு முன் கட்டாய நடைமுறைத் தேவை என்ன?",
            "options": [
                ("He shall consult the Council of Ministers of the State", "அவர் மாநில அமைச்சரவையைக் கலந்தாலோசிக்க வேண்டும்"),
                ("He must obtain written permission from the Chief of Army Staff", "அவர் ராணுவத் தளபதியிடம் எழுத்துப்பூர்வ அனுமதி பெற வேண்டும்"),
                ("He must seek approval from the Guwahati High Court", "அவர் குவஹாத்தி உயர் நீதிமன்றத்தின் ஒப்புதலைப் பெற வேண்டும்"),
                ("He must table the proposed measure in the State Assembly before execution", "நடவடிக்கையை செயல்படுத்துவதற்கு முன் அதை மாநில சட்டமன்றத்தில் சமர்ப்பிக்க வேண்டும்")
            ],
            "correct_key": "A",
            "exp_en": "Article 371H(a) specifies that the Governor shall, after consulting the Council of Ministers, exercise his individual judgment as to the action to be taken. Consultation is mandatory, though the final decision rests on his individual judgment.",
            "exp_ta": "சரத்து 371H(a) ஆளுநர் அமைச்சரவையைக் கலந்தாலோசித்த பிறகு எடுக்கப்பட வேண்டிய நடவடிக்கை குறித்து தனது தனிப்பட்ட முடிவைப் பயன்படுத்துவார் என்று கூறுகிறது. ஆலோசனை கட்டாயமானது, ஆனால் இறுதி முடிவு அவரது தனிப்பட்ட முடிவே.",
            "why_a_en": "Article 371H(a) expressly states 'after consulting the Council of Ministers'.",
            "why_a_ta": "சரத்து 371H(a) 'அமைச்சரவையைக் கலந்தாலோசித்த பிறகு' என்பதை தெளிவாகக் குறிப்பிடுகிறது.",
            "why_b_en": "Military chief permission is unconstitutional in civil state governance.",
            "why_b_ta": "மாநில சிவில் நிர்வாகத்தில் ராணுவத் தளபதியின் அனுமதி என்பது அரசியலமைப்பிற்கு முரணானது.",
            "why_c_en": "High Court approval is not required for executive law and order measures.",
            "why_c_ta": "நிர்வாக சட்டம் ஒழுங்கு நடவடிக்கைகளுக்கு உயர் நீதிமன்ற ஒப்புதல் தேவையில்லை.",
            "why_d_en": "Prior legislative tabling would defeat emergency executive speed.",
            "why_d_ta": "முன் சட்டமன்ற சமர்ப்பிப்பு அவசர நிர்வாக வேகத்தைக் கெடுத்துவிடும்.",
            "tip_en": "The distinction: In matters where Governor acts 'on aid and advice', ministers' advice binds him; in 'individual judgment', he consults ministers but can overrule them.",
            "tip_ta": "வேறுபாடு: 'ஆலோசனை மற்றும் வழிகாட்டுதலின்' கீழ் அமைச்சரவை முடிவு கட்டுப்படுத்தும்; 'தனிப்பட்ட முடிவின்' கீழ் அமைச்சரவையை ஆலோசித்து ஆளுநர் அதை மீறலாம்.",
            "fact_en": "Arunachal Pradesh shares international borders with three countries: Bhutan, China (Tibet), and Myanmar.",
            "fact_ta": "அருணாச்சலப் பிரதேசம் பூட்டான், சீனா (திபெத்) மற்றும் மியான்மர் ஆகிய மூன்று நாடுகளுடன் சர்வதேச எல்லைகளைப் பகிர்ந்து கொள்கிறது."
        },
        # 33
        {
            "subtopic": "Article 371I Goa Statehood Transition",
            "stem_en": "Prior to attaining statehood under Article 371I via the 56th Amendment Act 1987, what was the administrative status of Goa?",
            "stem_ta": "1987-ன் 56வது திருத்தச் சட்டம் சரத்து 371I-ன் கீழ் மாநில அந்தஸ்தைப் பெறுவதற்கு முன்பு, கோவாவின் நிர்வாக நிலை என்னவாக இருந்தது?",
            "options": [
                ("A Union Territory along with Daman and Diu", "டாமன் மற்றும் டையூவுடன் இணைந்த ஒரு யூனியன் பிரதேசம்"),
                ("A Part B State under the original 1950 Constitution", "1950 ஆம் ஆண்டின் அசல் அரசியலமைப்பின் கீழான பகுதி B மாநிலம்"),
                ("A district under the administrative control of Maharashtra", "மகாராஷ்டிராவின் நிர்வாகக் கட்டுப்பாட்டில் இருந்த ஒரு மாவட்டம்"),
                ("A protectorate territory governed by the Ministry of External Affairs", "வெளியுறவு அமைச்சகத்தால் நிர்வகிக்கப்பட்ட ஒரு பாதுகாக்கப்பட்ட பிரதேசம்")
            ],
            "correct_key": "A",
            "exp_en": "From 1962 to 1987, Goa was part of the Union Territory of 'Goa, Daman and Diu' (constituted by the 12th Constitutional Amendment Act, 1962). Statehood was conferred only on Goa in 1987, while Daman and Diu remained a separate UT.",
            "exp_ta": "1962 முதல் 1987 வரை, கோவா 'கோவா, டாமன் மற்றும் டையூ' யூனியன் பிரதேசத்தின் பகுதியாக இருந்தது (1962-ன் 12வது திருத்தச் சட்டம் மூலம் உருவாக்கப்பட்டது). 1987-ல் கோவாவிற்கு மட்டுமே மாநில அந்தஸ்து வழங்கப்பட்டது; டாமன் & டையூ தனி யூனியன் பிரதேசமாக நீடித்தது.",
            "why_a_en": "Goa was part of the combined Union Territory of Goa, Daman and Diu until 1987.",
            "why_a_ta": "1987 வரை கோவா, டாமன் மற்றும் டையூ ஒருங்கிணைந்த யூனியன் பிரதேசத்தின் பகுதியாக இருந்தது.",
            "why_b_en": "Goa was under Portuguese rule until December 1961, so it was not a Part B state in 1950.",
            "why_b_ta": "1961 டிசம்பர் வரை கோவா போர்த்துகீசிய ஆட்சியில் இருந்தது, எனவே 1950-ல் பகுதி B மாநிலமாக இல்லை.",
            "why_c_en": "In the 1967 Goa Opinion Poll (first referendum in India), the people voted against merger with Maharashtra.",
            "why_c_ta": "1967 கோவா கருத்துக்கணிப்பில், மக்கள் மகாராஷ்டிராவுடன் இணைவதற்கு எதிராக வாக்களித்தனர்.",
            "why_d_en": "Goa was formally integrated into the Indian Union by the 12th Amendment, not kept as a protectorate.",
            "why_d_ta": "12வது திருத்தத்தால் கோவா இந்திய ஒன்றியத்தில் முறையாக இணைக்கப்பட்டது.",
            "tip_en": "1967 Goa Opinion Poll: Historic plebiscite where Goans rejected merger with Maharashtra, preserving their distinct Konkani identity.",
            "tip_ta": "1967 கோவா கருத்துக்கணிப்பு: கோவா மக்கள் மகாராஷ்டிராவுடன் இணைவதை நிராகரித்து கொங்கணி அடையாளத்தைப் பாதுகாத்த வரலாற்று நிகழ்வு.",
            "fact_en": "Goa has two Lok Sabha constituencies (North Goa and South Goa) and one Rajya Sabha seat.",
            "fact_ta": "கோவாவில் இரண்டு மக்களவைத் தொகுதிகளும் (வடக்கு மற்றும் தெற்கு கோவா) ஒரு மாநிலங்களவை இடமும் உள்ளன."
        },
        # 34
        {
            "subtopic": "Article 371J Reservation Parameters",
            "stem_en": "Under Article 371J(2), an order made by the President may provide for reservation in state government posts and educational institutions for persons who belong to the Hyderabad-Karnataka region by:",
            "stem_ta": "சரத்து 371J(2)-ன் கீழ், குடியரசுத் தலைவர் பிறப்பிக்கும் ஆணை, ஹைதராபாத்-கர்நாடகா பகுதியைச் சேர்ந்தவர்களுக்கு அரசுப் பணிகள் மற்றும் கல்வி நிறுவனங்களில் எவ்வாறு இடஒதுக்கீடு வழங்க வகைசெய்யலாம்?",
            "options": [
                ("Birth or by domicile in that region", "இப்பகுதியில் பிறந்ததன் மூலம் அல்லது இருப்பிடத்தைக் கொண்டிருப்பதன் மூலம்"),
                ("Payment of a special commercial development tax", "ஒரு சிறப்பு வணிக வளர்ச்சி வரியைச் செலுத்துவதன் மூலம்"),
                ("Membership of the Kannada Sahitya Parishad only", "கன்னட சாகித்ய பரிஷத்தின் உறுப்பினராக இருப்பதன் மூலம் மட்டுமே"),
                ("Holding agricultural land of at least 50 acres", "குறைந்தது 50 ஏக்கர் விவசாய நிலத்தை வைத்திருப்பதன் மூலம்")
            ],
            "correct_key": "A",
            "exp_en": "Article 371J(2)(b) and (c) explicitly state that reservation in educational admissions and state government employment can be provided for persons who belong to the Hyderabad-Karnataka region 'by birth or by domicile'.",
            "exp_ta": "சரத்து 371J(2)(b) மற்றும் (c) ஹைதராபாத்-கர்நாடகா பகுதியை 'பிறப்பால் அல்லது இருப்பிடத்தால்' சார்ந்த நபர்களுக்கு கல்வி சேர்க்கை மற்றும் அரசுப் பணிகளில் இடஒதுக்கீடு வழங்கப்படலாம் என்று தெளிவாகக் கூறுகிறது.",
            "why_a_en": "Article 371J(2) expressly uses the constitutional terms 'by birth or by domicile'.",
            "why_a_ta": "சரத்து 371J(2) 'பிறப்பால் அல்லது இருப்பிடத்தால்' என்ற சொற்றொடரைத் தெளிவாகப் பயன்படுத்துகிறது.",
            "why_b_en": "Tax payment is not a qualification for constitutional reservation.",
            "why_b_ta": "வரி செலுத்துவது அரசியலமைப்பு இடஒதுக்கீட்டிற்கான தகுதி அல்ல.",
            "why_c_en": "Literary body membership is irrelevant to public reservation quotas.",
            "why_c_ta": "இலக்கிய அமைப்பு உறுப்பினர் தகுதி அரசு இடஒதுக்கீட்டிற்கு தொடர்பற்றது.",
            "why_d_en": "Land ownership size is not a criterion under Article 371J.",
            "why_d_ta": "நில அளவு சரத்து 371J-ன் அளவுகோல் அல்ல.",
            "tip_en": "Article 371J is a constitutional exception to Article 16(2) which normally prohibits discrimination in public employment based on place of birth or residence.",
            "tip_ta": "சரத்து 371J என்பது வேலைவாய்ப்பில் பிறப்பிடம் அல்லது வசிப்பிடம் அடிப்படையில் பாகுபாடு காட்டுவதைத் தடை செய்யும் சரத்து 16(2)-க்கு ஓர் அரசியலமைப்பு விதிவிலக்காகும்.",
            "fact_en": "In Karnataka, 75% of posts in the region and 8% of state-level apex cadre posts are reserved for Hyderabad-Karnataka candidates.",
            "fact_ta": "கர்நாடகாவில், இப்பகுதியில் உள்ள 75% பதவிகளும், மாநில அளவிலான 8% உயர் பதவிகளும் ஹைதராபாத்-கர்நாடகா விண்ணப்பதாரர்களுக்கு ஒதுக்கப்பட்டுள்ளன."
        },
        # 35
        {
            "subtopic": "Article 335 Consequential Amendments",
            "stem_en": "Which Constitutional Amendment added a proviso to Article 335 empowering the State to relax qualifying marks in examinations or lower evaluation standards for reservation in promotions for SCs and STs?",
            "stem_ta": "SC மற்றும் ST பிரிவினருக்கு பதவி உயர்வு இடஒதுக்கீட்டிற்கான தேர்வுகளில் தகுதி மதிப்பெண்களைத் தளர்த்தவோ அல்லது மதிப்பீட்டுத் தரங்களைக் குறைக்கவோ அரசுக்கு அதிகாரமளிக்கும் வரம்புரையை சரத்து 335-ல் சேர்த்த அரசியலமைப்புத் திருத்தம் எது?",
            "options": [
                ("82nd Constitutional Amendment Act, 2000", "82வது அரசியலமைப்புத் திருத்தச் சட்டம், 2000"),
                ("77th Constitutional Amendment Act, 1995", "77வது அரசியலமைப்புத் திருத்தச் சட்டம், 1995"),
                ("81st Constitutional Amendment Act, 2000", "81வது அரசியலமைப்புத் திருத்தச் சட்டம், 2000"),
                ("85th Constitutional Amendment Act, 2001", "85வது அரசியலமைப்புத் திருத்தச் சட்டம், 2001")
            ],
            "correct_key": "A",
            "exp_en": "The 82nd Constitutional Amendment Act, 2000 added a proviso to Article 335, restoring the power of the State to provide relaxation in qualifying marks or lower standards of evaluation in matters of reservation in promotion for SCs and STs, which had been invalidated by the SC in S. Vinod Kumar (1996).",
            "exp_ta": "வினோத் குமார் வழக்கில் (1996) உச்ச நீதிமன்றத்தால் ரத்து செய்யப்பட்ட தளர்வு அதிகாரத்தை மீட்டெடுக்க, 2000-ன் 82வது அரசியலமைப்புத் திருத்தச் சட்டம் சரத்து 335-ல் ஒரு வரம்புரையைச் சேர்த்து, SC/ST-க்கு பதவி உயர்வில் தகுதி மதிப்பெண்களைத் தளர்த்த அரசுக்கு மீண்டும் அதிகாரமளித்தது.",
            "why_a_en": "82nd CAA 2000 added the proviso to Article 335 regarding lowering qualifying marks.",
            "why_a_ta": "2000-ன் 82வது திருத்தம் மதிப்பெண் தளர்வு தொடர்பான வரம்புரையை சரத்து 335-ல் சேர்த்தது.",
            "why_b_en": "77th CAA 1995 added Article 16(4A) permitting promotion reservation.",
            "why_b_ta": "1995-ன் 77வது திருத்தம் பதவி உயர்வு இடஒதுக்கீட்டை அனுமதிக்கும் சரத்து 16(4A)-ஐச் சேர்த்தது.",
            "why_c_en": "81st CAA 2000 added Article 16(4B) regarding carry-forward backlog vacancies.",
            "why_c_ta": "2000-ன் 81வது திருத்தம் நிலுவை பணியிடங்களை முன்னெடுத்துச் செல்லும் சரத்து 16(4B)-ஐச் சேர்த்தது.",
            "why_d_en": "85th CAA 2001 added consequential seniority to Article 16(4A).",
            "why_d_ta": "2001-ன் 85வது திருத்தம் தொடர் பணிமூப்பை சரத்து 16(4A)-ல் சேர்த்தது.",
            "tip_en": "Proviso to Art 335 states: 'Nothing in this article shall prevent the making of any provision in favour of the members of the SCs and STs for relaxation in qualifying marks in any examination...'",
            "tip_ta": "சரத்து 335 வரம்புரை: 'எந்தவொரு தேர்விலும் தகுதி மதிப்பெண்களில் தளர்வு அளிப்பதற்கு SC/ST பிரிவினருக்கு ஆதரவாக விதிகளை உருவாக்குவதை இச்சரத்து தடுக்காது...'",
            "fact_en": "The validity of the 82nd Amendment was tested and upheld by the Constitution Bench in M. Nagaraj (2006).",
            "fact_ta": "82வது திருத்தத்தின் செல்லுபடியாகும் தன்மை எம். நாகராஜ் வழக்கில் (2006) உச்ச நீதிமன்ற அரசியலமைப்பு அமர்வால் உறுதி செய்யப்பட்டது."
        },
        # 36
        {
            "subtopic": "Article 16(4A) Consequential Seniority",
            "stem_en": "Which Constitutional Amendment inserted the words 'with consequential seniority' into Article 16(4A) with retrospective effect from 1995?",
            "stem_ta": "1995 முதல் முன்செல்லும் தேதியிட்டு நடைமுறைக்கு வரும் வகையில், சரத்து 16(4A)-ல் 'தொடர் பணிமூப்புடன்' என்ற வார்த்தைகளைச் சேர்த்த அரசியலமைப்புத் திருத்தம் எது?",
            "options": [
                ("85th Constitutional Amendment Act, 2001", "85வது அரசியலமைப்புத் திருத்தச் சட்டம், 2001"),
                ("77th Constitutional Amendment Act, 1995", "77வது அரசியலமைப்புத் திருத்தச் சட்டம், 1995"),
                ("81st Constitutional Amendment Act, 2000", "81வது அரசியலமைப்புத் திருத்தச் சட்டம், 2000"),
                ("82nd Constitutional Amendment Act, 2000", "82வது அரசியலமைப்புத் திருத்தச் சட்டம், 2000")
            ],
            "correct_key": "A",
            "exp_en": "The 85th Constitutional Amendment Act, 2001 amended Article 16(4A) to insert the words 'with consequential seniority' with retrospective effect from 17 June 1995, negating the 'catch-up rule' laid down by the Supreme Court in Union of India v. Virpal Singh Chauhan (1995) and Ajit Singh Januja (1996).",
            "exp_ta": "வீர்பால் சிங் சவுகான் (1995) மற்றும் அஜித் சிங் வழக்குகளில் உச்ச நீதிமன்றம் வகுத்த 'கேட்ச்-அப் விதியை' முறியடிக்க, 2001-ன் 85வது அரசியலமைப்புத் திருத்தச் சட்டம் 1995 ஜூன் 17 முதல் முன்செல்லும் தேதியிட்டு சரத்து 16(4A)-ல் 'தொடர் பணிமூப்புடன்' என்ற வார்த்தைகளைச் சேர்த்தது.",
            "why_a_en": "85th CAA 2001 added 'consequential seniority' retrospectively from June 1995.",
            "why_a_ta": "2001-ன் 85வது திருத்தம் 1995 ஜூன் முதல் முன்செல்லும் வகையில் 'தொடர் பணிமூப்பை' சேர்த்தது.",
            "why_b_en": "77th CAA 1995 initially created Article 16(4A) without the consequential seniority clause.",
            "why_b_ta": "1995-ன் 77வது திருத்தம் தொடர் பணிமூப்பு வாசகம் இல்லாமல் சரத்து 16(4A)-ஐ முதலில் உருவாக்கியது.",
            "why_c_en": "81st CAA 2000 introduced carry forward rule under 16(4B).",
            "why_c_ta": "2000-ன் 81வது திருத்தம் 16(4B)-ன் கீழ் நிலுவை இட விதியை அறிமுகப்படுத்தியது.",
            "why_d_en": "82nd CAA 2000 relaxed evaluation standards under Article 335.",
            "why_d_ta": "2000-ன் 82வது திருத்தம் சரத்து 335-ன் கீழ் தகுதி மதிப்பெண் தளர்வை அளித்தது.",
            "tip_en": "Consequential seniority ensures that reserved category candidates promoted earlier retain their seniority over senior general category candidates.",
            "tip_ta": "தொடர் பணிமூப்பு என்பது முன்னதாக பதவி உயர்வு பெற்ற இடஒதுக்கீட்டுப் பிரிவு ஊழியர், பின்னர் பதவி உயர்வு பெறும் பொதுப்பிரிவு ஊழியரை விட பணிமூப்பில் முன்னிலையில் இருப்பதை உறுதி செய்கிறது.",
            "fact_en": "Upheld in B.K. Pavitra (II) v. Union of India (2019) after Karnataka collected empirical proof of representation.",
            "fact_ta": "கர்நாடக அரசு ஆய்வுத் தரவுகளைச் சேகரித்த பிறகு, 2019 பவித்ரா (II) வழக்கில் இது உச்ச நீதிமன்றத்தால் உறுதி செய்யப்பட்டது."
        },
        # 37
        {
            "subtopic": "Janhit Abhiyan Case 2022",
            "stem_en": "In Janhit Abhiyan v. Union of India (2022), the Supreme Court upheld the constitutional validity of the 103rd Amendment (EWS Quota) by a majority of:",
            "stem_ta": "ஜன்ஹித் அபியான் எதிர் இந்திய ஒன்றியம் (2022) வழக்கில், உச்ச நீதிமன்றம் 103வது திருத்தத்தின் (EWS ஒதுக்கீடு) அரசியலமைப்பு செல்லுபடியாகும் தன்மையை எந்தப் பெரும்பான்மையில் உறுதி செய்தது?",
            "options": [
                ("3:2 majority", "3:2 பெரும்பான்மை"),
                ("5:0 unanimous verdict", "5:0 ஒருமனதான தீர்ப்பு"),
                ("4:1 majority", "4:1 பெரும்பான்மை"),
                ("7:2 majority", "7:2 பெரும்பான்மை")
            ],
            "correct_key": "A",
            "exp_en": "In Janhit Abhiyan (2022), a 5-judge Constitution Bench of the Supreme Court upheld the 103rd Amendment by a 3:2 majority (Justices Dinesh Maheshwari, Bela M. Trivedi, and J.B. Pardiwala in the majority; CJI U.U. Lalit and Justice S. Ravindra Bhat dissenting).",
            "exp_ta": "ஜன்ஹித் அபியான் வழக்கில் (2022), உச்ச நீதிமன்றத்தின் 5 நீதிபதிகள் கொண்ட அரசியலமைப்பு அமர்வு 3:2 என்ற பெரும்பான்மையில் 103வது திருத்தத்தை உறுதி செய்தது (நீதிபதிகள் தினேஷ் மகேஸ்வரி, பேலா திரிவேதி, பர்திவாலா ஆதரவு; தலைமை நீதிபதி யு.யு. லலித் மற்றும் ரவீந்திர பட் எதிர்ப்பு).",
            "why_a_en": "The judgment was delivered by a 3:2 majority.",
            "why_a_ta": "இத்தீர்ப்பு 3:2 என்ற பெரும்பான்மையில் வழங்கப்பட்டது.",
            "why_b_en": "The verdict was not unanimous; there was a sharp 2-judge dissent.",
            "why_b_ta": "தீர்ப்பு ஒருமனதானது அல்ல; 2 நீதிபதிகளின் மாறுபட்ட தீர்ப்பு இருந்தது.",
            "why_c_en": "4:1 is incorrect.",
            "why_c_ta": "4:1 என்பது தவறானது.",
            "why_d_en": "The bench comprised 5 judges, not 9 judges.",
            "why_d_ta": "அமர்வு 5 நீதிபதிகளைக் கொண்டிருந்தது, 9 நீதிபதிகள் அல்ல.",
            "tip_en": "Key finding: 50% ceiling rule applies to caste-based reservations under Articles 15(4) and 16(4), and is not breached by a distinct economic classification under Arts 15(6) and 16(6).",
            "tip_ta": "முக்கிய முடிவு: 50% உச்ச வரம்பு சாதி அடிப்படையிலான இடஒதுக்கீட்டிற்கு மட்டுமே பொருந்தும், பொருளாதார அடிப்படையிலான தனிப் பிரிவுக்கு பொருந்தாது.",
            "fact_en": "The dissenting judges argued that excluding SCs, STs, and OBCs from the EWS quota violates equality and basic structure.",
            "fact_ta": "SC, ST மற்றும் OBC-களை EWS ஒதுக்கீட்டிலிருந்து விலக்குவது சமத்துவம் மற்றும் அடிப்படை அமைப்பை மீறுவதாகும் என மாறுபட்ட நீதிபதிகள் வாதிட்டனர்."
        },
        # 38
        {
            "subtopic": "Article 338 vs 338A vs 338B Composition",
            "stem_en": "What is the uniform constitutional composition of the National Commission for Scheduled Castes (Article 338), NCST (Article 338A), and NCBC (Article 338B)?",
            "stem_ta": "NCSC (சரத்து 338), NCST (சரத்து 338A) மற்றும் NCBC (சரத்து 338B) ஆகிய தேசிய ஆணையங்களின் ஒரே மாதிரியான அரசியலமைப்பு கட்டமைப்பு என்ன?",
            "options": [
                ("A Chairperson, a Vice-Chairperson, and three other Members (Total 5)", "ஒரு தலைவர், ஒரு துணைத் தலைவர் மற்றும் மூன்று பிற உறுப்பினர்கள் (மொத்தம் 5)"),
                ("A Chairman and ten full-time members (Total 11)", "ஒரு தலைவர் மற்றும் பத்து முழுநேர உறுப்பினர்கள் (மொத்தம் 11)"),
                ("A Chief Commissioner and two Assistant Commissioners (Total 3)", "ஒரு தலைமை ஆணையர் மற்றும் இரண்டு உதவி ஆணையர்கள் (மொத்தம் 3)"),
                ("A retired Chief Justice of India and four judges (Total 5)", "ஓய்வுபெற்ற இந்தியத் தலைமை நீதிபதி மற்றும் நான்கு நீதிபதிகள் (மொத்தம் 5)")
            ],
            "correct_key": "A",
            "exp_en": "All three National Commissions (NCSC under Art 338(2), NCST under Art 338A(2), and NCBC under Art 338B(2)) have an identical structure: a Chairperson, a Vice-Chairperson, and three other Members (Total 5 persons) appointed by the President by warrant under his hand and seal.",
            "exp_ta": "மூன்று தேசிய ஆணையங்களும் (NCSC, NCST, NCBC) ஒரே மாதிரியான அமைப்பைக் கொண்டுள்ளன: ஒரு தலைவர், ஒரு துணைத் தலைவர் மற்றும் மூன்று பிற உறுப்பினர்கள் (மொத்தம் 5 நபர்கள்); இவர்கள் குடியரசுத் தலைவரால் முத்திரையிடப்பட்ட ஆணை மூலம் நியமிக்கப்படுகின்றனர்.",
            "why_a_en": "Articles 338(2), 338A(2), and 338B(2) prescribe a Chairperson, Vice-Chairperson, and 3 Members.",
            "why_a_ta": "சரத்துகள் 338(2), 338A(2), 338B(2) தலைவர், துணைத்தலைவர், 3 உறுப்பினர்களைக் குறிப்பிடுகின்றன.",
            "why_b_en": "11 members is not the structure of these constitutional commissions.",
            "why_b_ta": "11 உறுப்பினர்கள் என்பது இவ்வமைப்புகளின் கட்டமைப்பு அல்ல.",
            "why_c_en": "3 members was the statutory structure of the Election Commission, not these commissions.",
            "why_c_ta": "3 உறுப்பினர்கள் தேர்தல் ஆணையத்தின் அமைப்பு, இவற்றின் அமைப்பு அல்ல.",
            "why_d_en": "Judges are not constitutionally mandated as chairpersons of NCSC or NCST.",
            "why_d_ta": "நீதிபதிகள் மட்டுமே தலைவராக இருக்க வேண்டும் என்ற கட்டாயம் இல்லை.",
            "tip_en": "The Chairperson has the rank of a Union Cabinet Minister, Vice-Chairperson has the rank of Minister of State, and Members have the rank of Secretary to the Government of India.",
            "tip_ta": "தலைவர் மத்திய அமைச்சரவை அமைச்சரின் அந்தஸ்தையும், துணைத்தலைவர் இணை அமைச்சரின் அந்தஸ்தையும், உறுப்பினர்கள் மத்திய அரசுச் செயலாளரின் அந்தஸ்தையும் கொண்டுள்ளனர்.",
            "fact_en": "Tenure of the members is fixed at 3 years by rules framed by the President under the respective articles.",
            "fact_ta": "குடியரசுத் தலைவர் வகுத்த விதிகளின்படி உறுப்பினர்களின் பதவிக்காலம் 3 ஆண்டுகள் என நிர்ணயிக்கப்பட்டுள்ளது."
        },
        # 39
        {
            "subtopic": "Article 338 Tabling of Reports",
            "stem_en": "When the National Commission for Scheduled Castes submits its annual report to the President, what is the constitutional procedure under Article 338(6)?",
            "stem_ta": "பட்டியலிடப்பட்ட சாதியினருக்கான தேசிய ஆணையம் தனது ஆண்டு அறிக்கையை குடியரசுத் தலைவரிடம் சமர்ப்பிக்கும் போது, சரத்து 338(6)-ன் கீழ் உள்ள அரசியலமைப்பு நடைமுறை என்ன?",
            "options": [
                ("The President causes it to be laid before each House of Parliament along with an Action Taken Memorandum", "குடியரசுத் தலைவர் நடவடிக்கை எடுக்கப்பட்ட குறிப்புடன் அதை நாடாளுமன்றத்தின் இரு அவைகளிலும் வைக்கச் செய்கிறார்"),
                ("The report is treated as classified and kept in the archives of the Cabinet Secretariat", "அறிக்கை ரகசியமானதாகக் கருதப்பட்டு அமைச்சரவைச் செயலக காப்பகத்தில் வைக்கப்படுகிறது"),
                ("The report is sent to the International Court of Justice for evaluation", "அறிக்கை சர்வதேச நீதிமன்றத்திற்கு மதிப்பீட்டிற்காக அனுப்பப்படுகிறது"),
                ("The President can reject the report without giving any reasons to Parliament", "நாடாளுமன்றத்திற்கு எந்தக் காரணமும் கூறாமல் குடியரசுத் தலைவர் அறிக்கையை நிராகரிக்கலாம்")
            ],
            "correct_key": "A",
            "exp_en": "Under Article 338(6), the President shall cause all such reports to be laid before each House of Parliament along with a memorandum explaining the action taken or proposed to be taken on the recommendations, and the reasons for non-acceptance, if any.",
            "exp_ta": "சரத்து 338(6)-ன் படி, பரிந்துரைகளின் மீது எடுக்கப்பட்ட அல்லது எடுக்க உத்தேசிக்கப்பட்டுள்ள நடவடிக்கை மற்றும் ஏற்கப்படாததற்கான காரணங்களை விளக்கும் குறிப்புடன் (ATR) குடியரசுத் தலைவர் அவ்வறிக்கைகளை நாடாளுமன்றத்தின் இரு அவைகளின் முன்பும் வைக்கச் செய்ய வேண்டும்.",
            "why_a_en": "Article 338(6) explicitly mandates tabling before Parliament with an explanatory memorandum.",
            "why_a_ta": "சரத்து 338(6) விளக்கக் குறிப்புடன் நாடாளுமன்றத்தின் முன் சமர்ப்பிப்பதைக் கட்டாயமாக்குகிறது.",
            "why_b_en": "Reports are public parliamentary documents, not classified secret archives.",
            "why_b_ta": "அறிக்கைகள் பொது நாடாளுமன்ற ஆவணங்கள், ரகசியமானவை அல்ல.",
            "why_c_en": "ICJ has no jurisdiction over domestic affirmative action reports.",
            "why_c_ta": "சர்வதேச நீதிமன்றத்திற்கு இதில் எந்தத் தொடர்பும் இல்லை.",
            "why_d_en": "Reasons for non-acceptance must be explicitly explained to Parliament.",
            "why_d_ta": "ஏற்காததற்கான காரணங்களை நாடாளுமன்றத்திற்கு கட்டாயம் விளக்க வேண்டும்.",
            "tip_en": "If a report relates to a State matter, the President forwards it to the Governor, who causes it to be laid before the State Legislature (Art 338(7)).",
            "tip_ta": "அறிக்கை ஒரு மாநில விவகாரம் பற்றியதாக இருந்தால், ஆளுநர் மூலம் மாநில சட்டமன்றத்தின் முன் வைக்கப்படும் (சரத்து 338(7)).",
            "fact_en": "Identical tabling provisions exist for NCST under Article 338A(6)-(7) and NCBC under Article 338B(6)-(7).",
            "fact_ta": "இதே போன்ற சமர்ப்பிப்பு விதிகள் NCST (338A(6)-(7)) மற்றும் NCBC (338B(6)-(7)) அமைப்புகளுக்கும் உள்ளன."
        },
        # 40
        {
            "subtopic": "State of Madras v. Champakam Dorairajan 1951",
            "stem_en": "In State of Madras v. Champakam Dorairajan (1951), the Supreme Court held that in case of conflict between Fundamental Rights and Directive Principles of State Policy:",
            "stem_ta": "செண்பகம் துரைராஜன் வழக்கில் (1951), அடிப்படை உரிமைகளுக்கும் அரசு வழிகாட்டு நெறிமுறைகளுக்கும் இடையே முரண்பாடு ஏற்பட்டால் உச்ச நீதிமன்றம் என்ன தீர்ப்பளித்தது?",
            "options": [
                ("Fundamental Rights shall prevail, and Directive Principles must conform to and run subsidiary to Fundamental Rights", "அடிப்படை உரிமைகளே மேலோங்கும், மேலும் வழிகாட்டு நெறிமுறைகள் அடிப்படை உரிமைகளுக்கு இணக்கமாகவும் துணையாகவும் செயல்பட வேண்டும்"),
                ("Directive Principles shall automatically override Fundamental Rights at all times", "வழிகாட்டு நெறிமுறைகள் எப்போதும் தானாக அடிப்படை உரிமைகளை விட மேலோங்கும்"),
                ("Both are completely non-justiciable and cannot be enforced by any court", "இரண்டும் முற்றிலும் நீதிமன்றங்களால் செயல்படுத்த முடியாதவை"),
                ("The Governor has the sole discretion to decide which shall prevail", "எது மேலோங்க வேண்டும் என்பதை ஆளுநரே தனது தனிப்பட்ட விருப்பத்தில் முடிவு செய்வார்")
            ],
            "correct_key": "A",
            "exp_en": "In Champakam Dorairajan (1951), the Supreme Court ruled that Fundamental Rights are sacrosanct and cannot be curtailed by Directive Principles (specifically Article 46). The Directive Principles have to conform to and run subsidiary to Chapter III (Fundamental Rights). This prompted the First Amendment adding Article 15(4).",
            "exp_ta": "செண்பகம் துரைராஜன் வழக்கில் (1951), அடிப்படை உரிமைகள் புனிதமானவை என்றும், வழிகாட்டு நெறிமுறைகளால் (குறிப்பாக சரத்து 46) அவற்றைக் குறைக்க முடியாது என்றும் உச்ச நீதிமன்றம் தீர்ப்பளித்தது. வழிகாட்டு நெறிமுறைகள் அடிப்படை உரிமைகளுக்குத் துணையாகவே இருக்க வேண்டும். இது சரத்து 15(4)-ஐ சேர்த்த முதல் திருத்தத்திற்கு வழிவகுத்தது.",
            "why_a_en": "Champakam Dorairajan famously established that DPSP run subsidiary to Fundamental Rights.",
            "why_a_ta": "வழிகாட்டு நெறிமுறைகள் அடிப்படை உரிமைகளுக்குத் துணையானவையே என செண்பகம் துரைராஜன் வழக்கு தீர்ப்பளித்தது.",
            "why_b_en": "DPSP overriding FR was only introduced much later for specific articles (Arts 39(b)-(c)) via the 25th Amendment 1971.",
            "why_b_ta": "DPSP மேலோங்குவது என்பது பின்னர் 1971-ன் 25வது திருத்தத்தால் குறிப்பிட்ட விதிகளுக்கு மட்டுமே கொண்டுவரப்பட்டது.",
            "why_c_en": "Fundamental Rights are fully justiciable under Articles 32 and 226.",
            "why_c_ta": "அடிப்படை உரிமைகள் நீதிமன்றங்களால் செயல்படுத்தக்கூடியவை.",
            "why_d_en": "The Governor has no adjudicatory power to resolve constitutional conflicts.",
            "why_d_ta": "அரசியலமைப்பு முரண்பாடுகளைத் தீர்க்க ஆளுநருக்கு அதிகாரம் இல்லை.",
            "tip_en": "Parliament reconciled this judgment by immediately amending Article 15 via the 1st Amendment 1951 to insert clause (4).",
            "tip_ta": "1951-ன் 1வது திருத்தம் மூலம் சரத்து 15(4)-ஐச் சேர்த்து நாடாளுமன்றம் இத்தீர்ப்பின் முரண்பாட்டைத் தீர்த்தது.",
            "fact_en": "Champakam Dorairajan never actually applied for admission to the medical college; she had filed the petition preemptively.",
            "fact_ta": "செண்பகம் துரைராஜன் உண்மையில் மருத்துவக் கல்லூரியில் சேர்க்கைக்கு விண்ணப்பிக்கவே இல்லை; முன்னெச்சரிக்கையாகவே மனு தாக்கல் செய்தார்."
        },
        # 41
        {
            "subtopic": "Asymmetrical Federalism Concept",
            "stem_en": "In Indian constitutional theory, the inclusion of special provisions for different states under Articles 371 to 371J is known as:",
            "stem_ta": "இந்திய அரசியலமைப்பு கோட்பாட்டில், சரத்துகள் 371 முதல் 371J வரை பல்வேறு மாநிலங்களுக்கான சிறப்பு ஏற்பாடுகளை உள்ளடக்கியிருப்பது எவ்வாறு அழைக்கப்படுகிறது?",
            "options": [
                ("Asymmetrical Federalism", "சமச்சீரற்ற கூட்டாட்சி (Asymmetrical Federalism)"),
                ("Monolithic Unitary Governance", "ஒற்றைக்கல் போன்ற ஒற்றையாட்சி முறை"),
                ("Totalitarian Centralism", "முழுமையான சர்வாதிகார மையவாதம்"),
                ("Confederal Anarchy", "கூட்டமைப்பு நிலையின்மை")
            ],
            "correct_key": "A",
            "exp_en": "Asymmetrical Federalism refers to a federal constitutional structure where different constituent states enjoy different degrees of legislative, administrative, or fiscal autonomy based on distinct historical compacts, geographical challenges, and ethnic diversities, as embodied in Articles 371 to 371J.",
            "exp_ta": "சமச்சீரற்ற கூட்டாட்சி என்பது, வரலாற்று ஒப்பந்தங்கள், புவியியல் சவால்கள் மற்றும் இனப் பன்முகத்தன்மை ஆகியவற்றின் அடிப்படையில் வெவ்வேறு மாநிலங்கள் வெவ்வேறு அளவிலான சுயாட்சியை அனுபவிக்கும் கூட்டாட்சி அரசியலமைப்பு அமைப்பைக் குறிக்கிறது; இது சரத்துகள் 371 முதல் 371J வரை வெளிப்படுத்தப்பட்டுள்ளது.",
            "why_a_en": "Asymmetrical federalism is the established constitutional doctrine describing Article 371 series.",
            "why_a_ta": "சரத்து 371 வரிசையை விவரிக்கும் அரசியலமைப்பு கோட்பாடு சமச்சீரற்ற கூட்டாட்சியாகும்.",
            "why_b_en": "Unitary governance means absence of state autonomy, which is the opposite of Art 371.",
            "why_b_ta": "ஒற்றையாட்சி என்பது மாநில சுயாட்சி இல்லாதது, இது சரத்து 371-க்கு எதிரானது.",
            "why_c_en": "Totalitarian centralism is a dictatorial concept contrary to constitutional democracy.",
            "why_c_ta": "சர்வாதிகார மையவாதம் அரசியலமைப்பு ஜனநாயகத்திற்கு முரணானது.",
            "why_d_en": "India is a Union of States, not a loose confederation.",
            "why_d_ta": "இந்தியா மாநிலங்களின் ஒன்றியம், தளர்வான கூட்டமைப்பு அல்ல.",
            "tip_en": "Unlike the US Constitution where all 50 states have symmetrical constitutional status, India adopts asymmetrical federalism to accommodate diversity.",
            "tip_ta": "அனைத்து 50 மாநிலங்களும் சமமான அந்தஸ்தைக் கொண்ட அமெரிக்காவைப் போலன்றி, இந்தியா பன்முகத்தன்மையை இணைக்க சமச்சீரற்ற கூட்டாட்சியைப் பின்பற்றுகிறது.",
            "fact_en": "Louise Tillin and Alfred Stepan have extensively documented India's asymmetrical federal design.",
            "fact_ta": "இந்தியாவின் சமச்சீரற்ற கூட்டாட்சி அமைப்பை லூயிஸ் டில்லின் போன்ற சர்வதேச அறிஞர்கள் விரிவாக ஆவணப்படுத்தியுள்ளனர்."
        },
        # 42
        {
            "subtopic": "Fifth Schedule Tribes Advisory Council",
            "stem_en": "Under Paragraph 4 of the Fifth Schedule, a Tribes Advisory Council (TAC) established in a State with Scheduled Areas shall consist of:",
            "stem_ta": "ஐந்தாவது அட்டவணையின் பத்தி 4-ன் கீழ், அட்டவணைப் பகுதிகளைக் கொண்ட ஒரு மாநிலத்தில் அமைக்கப்படும் பழங்குடியினர் ஆலோசனைக் குழு (TAC) எத்தனை உறுப்பினர்களைக் கொண்டிருக்கும்?",
            "options": [
                ("Not more than twenty members, of whom at least three-fourths shall be representatives of the STs in the State Legislative Assembly", "இருபது உறுப்பினர்களுக்கு மிகாமல், இதில் குறைந்தது நான்கில் மூன்று பங்கு உறுப்பினர்கள் மாநில சட்டமன்றத்தில் உள்ள ST பிரதிநிதிகளாக இருக்க வேண்டும்"),
                ("Exactly forty members directly nominated by the Governor", "ஆளுநரால் நேரடியாக நியமிக்கப்படும் சரியாக நாற்பது உறுப்பினர்கள்"),
                ("Only the members of Parliament representing the Scheduled Areas", "அட்டவணைப் பகுதிகளைப் பிரதிநிதித்துவப்படுத்தும் நாடாளுமன்ற உறுப்பினர்கள் மட்டுமே"),
                ("Ten civil servants headed by the Chief Secretary", "தலைமைச் செயலாளர் தலைமையிலான பத்து அரசு அதிகாரிகள்")
            ],
            "correct_key": "A",
            "exp_en": "Paragraph 4(1) of the Fifth Schedule mandates that there shall be established in each State having Scheduled Areas a Tribes Advisory Council consisting of not more than twenty members, of whom, as nearly as may be, three-fourths shall be the representatives of the Scheduled Tribes in the Legislative Assembly of the State.",
            "exp_ta": "ஐந்தாவது அட்டவணையின் பத்தி 4(1), அட்டவணைப் பகுதிகளைக் கொண்ட ஒவ்வொரு மாநிலத்திலும் 20 உறுப்பினர்களுக்கு மிகாமல் ஒரு பழங்குடியினர் ஆலோசனைக் குழு அமைக்கப்பட வேண்டும் என்றும், அதில் நான்கில் மூன்று பங்கு உறுப்பினர்கள் மாநில சட்டமன்றத்தில் உள்ள ST உறுப்பினர்களாக இருக்க வேண்டும் என்றும் கூறுகிறது.",
            "why_a_en": "Fifth Schedule Para 4 specifies not more than 20 members, with 3/4ths from ST MLAs.",
            "why_a_ta": "5வது அட்டவணை பத்தி 4 அதிகபட்சம் 20 உறுப்பினர்களையும், அதில் 3/4 பங்கு ST எம்.எல்.ஏ-க்களையும் குறிப்பிடுகிறது.",
            "why_b_en": "40 members is incorrect; the constitutional ceiling is 20.",
            "why_b_ta": "40 உறுப்பினர்கள் என்பது தவறு; உச்ச வரம்பு 20 ஆகும்.",
            "why_c_en": "It is drawn from State MLAs, not MPs.",
            "why_c_ta": "இது மாநில எம்.எல்.ஏ-க்களிலிருந்து உருவாக்கப்படுகிறது, எம்.பி-க்களிலிருந்து அல்ல.",
            "why_d_en": "It is a representative council, not a committee of bureaucrats.",
            "why_d_ta": "இது மக்கள் பிரதிநிதித்துவக் குழு, அதிகாரிகள் குழு அல்ல.",
            "tip_en": "Duty of TAC: To advise the Governor on matters pertaining to the welfare and advancement of Scheduled Tribes in the State.",
            "tip_ta": "TAC-ன் கடமை: மாநிலத்தில் பழங்குடியினரின் நலன் மற்றும் முன்னேற்றம் தொடர்பான விவகாரங்களில் ஆளுநருக்கு ஆலோசனை வழங்குவது.",
            "fact_en": "If the number of ST MLAs is less than the required three-fourths quota, the remaining seats are filled from other ST members of that State.",
            "fact_ta": "ST எம்.எல்.ஏ-க்களின் எண்ணிக்கை 3/4 பங்கிற்கு குறைவாக இருந்தால், எஞ்சிய இடங்கள் பிற ST உறுப்பினர்களால் நிரப்பப்படும்."
        },
        # 43
        {
            "subtopic": "Sixth Schedule District Councils",
            "stem_en": "Under Paragraph 2 of the Sixth Schedule, each Autonomous District Council (ADC) shall consist of not more than how many members?",
            "stem_ta": "ஆறாவது அட்டவணையின் பத்தி 2-ன் கீழ், ஒவ்வொரு தன்னாட்சி மாவட்டக் குழுவும் (ADC) எத்தனை உறுப்பினர்களுக்கு மிகாமல் இருக்க வேண்டும்?",
            "options": [
                ("Thirty members (of whom not more than four nominated by Governor and rest elected by adult suffrage)", "முப்பது உறுப்பினர்கள் (இதில் நான்கு பேருக்கு மிகாமல் ஆளுநரால் நியமிக்கப்படலாம், மீதமுள்ளவர்கள் வயதுவந்தோர் வாக்குரிமை மூலம் தேர்ந்தெடுக்கப்படுவர்)"),
                ("Twenty members (all indirectly elected by Village Panchayats)", "இருபது உறுப்பினர்கள் (அனைவரும் கிராம ஊராட்சிகளால் மறைமுகமாகத் தேர்ந்தெடுக்கப்படுவர்)"),
                ("Fifty members (half nominated by the Chief Minister)", "ஐம்பது உறுப்பினர்கள் (பாதி பேர் முதலமைச்சரால் நியமிக்கப்படுவர்)"),
                ("Sixty members (matching the State Legislative Assembly size)", "அறுபது உறுப்பினர்கள் (மாநில சட்டமன்ற அளவுக்கு சமமாக)")
            ],
            "correct_key": "A",
            "exp_en": "Paragraph 2(1) of the Sixth Schedule provides that there shall be a District Council for each autonomous district consisting of not more than thirty members, of whom not more than four persons shall be nominated by the Governor and the rest shall be elected on the basis of adult suffrage.",
            "exp_ta": "ஆறாவது அட்டவணையின் பத்தி 2(1), ஒவ்வொரு தன்னாட்சி மாவட்டத்திற்கும் 30 உறுப்பினர்களுக்கு மிகாமல் ஒரு மாவட்டக் குழு இருக்க வேண்டும் என்றும், அதில் 4 பேருக்கு மிகாமல் ஆளுநரால் நியமிக்கப்பட்டு, எஞ்சியவர்கள் வயதுவந்தோர் வாக்குரிமை அடிப்படையில் தேர்ந்தெடுக்கப்பட வேண்டும் என்றும் கூறுகிறது.",
            "why_a_en": "Paragraph 2(1) explicitly fixes the maximum at 30 members (up to 4 nominated, at least 26 elected).",
            "why_a_ta": "பத்தி 2(1) அதிகபட்ச பலத்தை 30 உறுப்பினர்கள் என நிர்ணயிக்கிறது (4 பேர் வரை நியமனம், குறைந்தது 26 பேர் தேர்தல் மூலம்).",
            "why_b_en": "20 members is the size of the Tribes Advisory Council under the Fifth Schedule.",
            "why_b_ta": "20 உறுப்பினர்கள் என்பது ஐந்தாவது அட்டவணையின் கீழான TAC பலமாகும்.",
            "why_c_en": "50 members is incorrect; Bodoland has 46 members under special amendment, but standard ADC has 30.",
            "why_c_ta": "50 உறுப்பினர்கள் என்பது தவறானது; போடோலாந்து விதிவிலக்கு தவிர வழக்கமான ADC அளவு 30 ஆகும்.",
            "why_d_en": "60 members is incorrect.",
            "why_d_ta": "60 உறுப்பினர்கள் என்பது தவறானது.",
            "tip_en": "Elected members hold office for a term of 5 years; nominated members hold office at the pleasure of the Governor.",
            "tip_ta": "தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்களின் பதவிக்காலம் 5 ஆண்டுகள்; நியமன உறுப்பினர்கள் ஆளுநரின் விருப்பம் உள்ளவரை பதவி வகிப்பர்.",
            "fact_en": "There are currently 10 Autonomous District Councils functioning under the Sixth Schedule across Assam, Meghalaya, Tripura, and Mizoram.",
            "fact_ta": "தற்போது அசாம், மேகாலயா, திரிபுரா மற்றும் மிசோரம் முழுவதும் ஆறாவது அட்டவணையின் கீழ் 10 தன்னாட்சி மாவட்டக் குழுக்கள் செயல்படுகின்றன."
        },
        # 44
        {
            "subtopic": "Article 371D Presidential Power over Civil Services",
            "stem_en": "Under Article 371D(2)(b)(iii), the President may specify the extent to which local candidates shall be given preference or reservation in direct recruitment to:",
            "stem_ta": "சரத்து 371D(2)(b)(iii)-ன் கீழ், எந்தப் பணிகளுக்கான நேரடி நியமனத்தில் உள்ளூர் விண்ணப்பதாரர்களுக்கு முன்னுரிமை அல்லது இடஒதுக்கீடு வழங்கப்பட வேண்டும் என்பதை குடியரசுத் தலைவர் குறிப்பிடலாம்?",
            "options": [
                ("Any post under the State Government or local authority within any specified local area", "குறிப்பிடப்பட்ட எந்தவொரு உள்ளூர் பகுதிக்குள்ளும் உள்ள மாநில அரசு அல்லது உள்ளாட்சி அமைப்பின் கீழான எந்தவொரு பதவி"),
                ("All-India Services such as IAS and IPS", "IAS மற்றும் IPS போன்ற அகில இந்தியப் பணிகள்"),
                ("Officers in the Indian Foreign Service posted overseas", "வெளிநாடுகளில் பணியமர்த்தப்படும் இந்திய வெளியுறவுப் பணி அதிகாரிகள்"),
                ("Judges of the Supreme Court of India", "இந்திய உச்ச நீதிமன்ற நீதிபதிகள்")
            ],
            "correct_key": "A",
            "exp_en": "Article 371D(2)(b)(iii) authorizes the President to specify the extent to which preference or reservation shall be given to local candidates in direct recruitment to any post under the Government of Andhra Pradesh/Telangana or any local authority within any local area.",
            "exp_ta": "சரத்து 371D(2)(b)(iii) ஆந்திரா/தெலங்கானா அரசு அல்லது எந்தவொரு உள்ளாட்சி அமைப்பின் கீழான பதவிகளுக்கான நேரடி நியமனத்தில் உள்ளூர் விண்ணப்பதாரர்களுக்கு முன்னுரிமை அல்லது இடஒதுக்கீடு வழங்க குடியரசுத் தலைவருக்கு அதிகாரம் அளிக்கிறது.",
            "why_a_en": "Article 371D applies to State Government civil posts and local authority posts within specified areas.",
            "why_a_ta": "சரத்து 371D மாநில அரசுப் பதவிகள் மற்றும் உள்ளாட்சி அமைப்புகளின் பதவிகளுக்குப் பொருந்தும்.",
            "why_b_en": "All-India Services are common to the Union and States under Article 312 and cannot have regional domicile quotas.",
            "why_b_ta": "அகில இந்தியப் பணிகள் சரத்து 312-ன் கீழ் பொதுவானவை, அவற்றுக்கு பிராந்திய ஒதுக்கீடு இருக்க முடியாது.",
            "why_c_en": "IFS is an exclusive Central Service.",
            "why_c_ta": "IFS என்பது மத்தியப் பணியாகும்.",
            "why_d_en": "Judicial appointments to Supreme Court are governed by Article 124.",
            "why_d_ta": "உச்ச நீதிமன்ற நீதிபதிகள் நியமனம் சரத்து 124-ன் கீழ் வருகிறது.",
            "tip_en": "This constitutional authorization overrides Article 16(2) and Article 16(3) for Andhra Pradesh and Telangana.",
            "tip_ta": "இந்த அரசியலமைப்பு அதிகாரம் ஆந்திரா மற்றும் தெலங்கானாவிற்கு சரத்து 16(2) மற்றும் 16(3)-ஐ விட மேலோங்குகிறது.",
            "fact_en": "The 2014 Andhra Pradesh Reorganisation Act preserved this presidential recruitment zoning system for both states.",
            "fact_ta": "2014 ஆந்திர மறுசீரமைப்புச் சட்டம் இரு மாநிலங்களுக்கும் இந்த குடியரசுத் தலைவர் மண்டல முறையைப் பாதுகாத்தது."
        },
        # 45
        {
            "subtopic": "Article 371F Application of Central Laws",
            "stem_en": "Under Article 371F(n), the President may by public notification extend to the State of Sikkim, with such restrictions or modifications as he thinks fit:",
            "stem_ta": "சரத்து 371F(n)-ன் கீழ், குடியரசுத் தலைவர் பொது அறிவிப்பின் மூலம் சிக்கிம் மாநிலத்திற்கு எதை தான் பொருத்தமானது எனக் கருதும் வரம்புகள் அல்லது மாற்றங்களுடன் நீட்டிக்கலாம்?",
            "options": [
                ("Any enactment which is in force in a State in India at the date of the notification", "அறிவிக்கை தேதியில் இந்தியாவில் உள்ள ஒரு மாநிலத்தில் நடைமுறையில் உள்ள எந்தவொரு சட்டத்தையும்"),
                ("Only international treaties signed by the United Nations", "ஐக்கிய நாடுகள் சபையால் கையெழுத்திடப்பட்ட சர்வதேச ஒப்பந்தங்களை மட்டுமே"),
                ("The legal codes of Nepal and Bhutan exclusively", "நேபாளம் மற்றும் பூட்டானின் சட்டத் தொகுப்புகளை மட்டுமே"),
                ("Executive regulations issued by the Governor without statutory backing", "சட்டப்பூர்வ ஆதரவு இல்லாத ஆளுநரின் நிர்வாக ஒழுங்குமுறைகளை")
            ],
            "correct_key": "A",
            "exp_en": "Article 371F(n) empowers the President by public notification to extend with restrictions or modifications to the State of Sikkim any enactment which is in force in a State in India at the date of the notification.",
            "exp_ta": "சரத்து 371F(n), அறிவிக்கை தேதியில் இந்தியாவின் ஒரு மாநிலத்தில் நடைமுறையில் உள்ள எந்தவொரு சட்டத்தையும், தான் பொருத்தமெனக் கருதும் மாற்றங்களுடன் சிக்கிமிற்கு நீட்டிக்க குடியரசுத் தலைவருக்கு அதிகாரம் அளிக்கிறது.",
            "why_a_en": "Article 371F(n) explicitly uses this formula to gradually integrate mainland Indian laws into Sikkim.",
            "why_a_ta": "சரத்து 371F(n) இந்தியச் சட்டங்களை சிக்கிமிற்கு படிப்படியாக நீட்டிக்க இந்த அதிகாரத்தை வழங்குகிறது.",
            "why_b_en": "Treaties are ratified under Article 253, not extended under Art 371F(n).",
            "why_b_ta": "சர்வதேச ஒப்பந்தங்கள் சரத்து 253-ன் கீழ் வருகின்றன.",
            "why_c_en": "Laws of foreign nations cannot be constitutionally extended to an Indian state.",
            "why_c_ta": "வெளிநாட்டுச் சட்டங்களை இந்திய மாநிலத்திற்கு நீட்டிக்க முடியாது.",
            "why_d_en": "Substantive statutory enactments are required, not arbitrary governor edicts.",
            "why_d_ta": "சட்டமன்றச் சட்டங்களே தேவை, தன்னிச்சையான ஆணைகள் அல்ல.",
            "tip_en": "This gradual extension power prevented legal chaos when Sikkim merged with India, allowing old Chogyal-era laws to be replaced systematically.",
            "tip_ta": "சிக்கிம் இணைந்தபோது சட்டக் குழப்பத்தைத் தவிர்த்து, சோக்யால் காலச் சட்டங்களை முறையாக மாற்றியமைக்க இது உதவியது.",
            "fact_en": "Over 150 Central Acts were extended to Sikkim under Article 371F(n) over the two decades following statehood.",
            "fact_ta": "மாநில அந்தஸ்திற்குப் பிந்தைய இரண்டு தசாப்தங்களில் 150-க்கும் மேற்பட்ட மத்தியச் சட்டங்கள் சரத்து 371F(n)-ன் கீழ் சிக்கிமிற்கு நீட்டிக்கப்பட்டன."
        },
        # 46
        {
            "subtopic": "Article 371G Protected Domains",
            "stem_en": "Which of the following domains is protected under Article 371G from the application of Acts of Parliament without Mizoram Assembly approval?",
            "stem_ta": "மிசோரம் சட்டமன்றத்தின் ஒப்புதல் இல்லாமல் நாடாளுமன்றச் சட்டங்கள் பொருந்தாத வகையில் சரத்து 371G-ன் கீழ் பாதுகாக்கப்பட்டுள்ள துறை எது?",
            "options": [
                ("Ownership and transfer of land", "நிலத்தின் உரிமை மற்றும் பரிமாற்றம்"),
                ("Regulation of civil aviation and airports", "விமானப் போக்குவரத்து மற்றும் விமான நிலையங்களின் ஒழுங்குமுறை"),
                ("Coinage, currency, and legal tender", "நாணயங்கள், பணவியல் மற்றும் சட்டப்பூர்வ நாணயம்"),
                ("Inter-state migration and citizenship", "மாநிலங்களுக்கு இடையேயான இடம்பெயர்வு மற்றும் குடியுரிமை")
            ],
            "correct_key": "A",
            "exp_en": "Under Article 371G(a)(iv), no Act of Parliament in respect of ownership and transfer of land shall apply to the State of Mizoram unless the Legislative Assembly of Mizoram by resolution so decides.",
            "exp_ta": "சரத்து 371G(a)(iv)-ன் படி, நிலத்தின் உரிமை மற்றும் பரிமாற்றம் தொடர்பான எந்தவொரு நாடாளுமன்றச் சட்டமும், மிசோரம் சட்டமன்றம் தீர்மானம் மூலம் முடிவு செய்யாவிட்டால், மிசோரம் மாநிலத்திற்குப் பொருந்தாது.",
            "why_a_en": "Ownership and transfer of land is one of the four protected subjects in Article 371G.",
            "why_a_ta": "நில உரிமை மற்றும் பரிமாற்றம் என்பது சரத்து 371G-ல் உள்ள நான்கு பாதுகாக்கப்பட்ட துறைகளில் ஒன்றாகும்.",
            "why_b_en": "Civil aviation is a Union List Entry 29 subject applicable across all India.",
            "why_b_ta": "விமானப் போக்குவரத்து மத்தியப் பட்டியல் பதிவு 29-ன் கீழ் வருகிறது.",
            "why_c_en": "Currency is an exclusive Union subject under Union List Entry 36.",
            "why_c_ta": "நாணயம் என்பது மத்தியப் பட்டியல் பதிவு 36-ன் கீழானது.",
            "why_d_en": "Citizenship is governed exclusively by Parliament under Article 11 and Union List Entry 17.",
            "why_d_ta": "குடியுரிமை சரத்து 11-ன் கீழ் நாடாளுமன்றத்திற்கு மட்டுமே உரியது.",
            "tip_en": "The 4 protected subjects in Art 371G (Mizoram) mirror almost exactly those in Art 371A (Nagaland).",
            "tip_ta": "சரத்து 371G (மிசோரம்) பாதுகாக்கும் 4 துறைகள் சரத்து 371A (நாகாலாந்து) பாதுகாக்கும் துறைகளை ஒத்தவை.",
            "fact_en": "Non-tribals cannot acquire tribal land in Mizoram without specialized state permissions under protective land tenure regulations.",
            "fact_ta": "பாதுகாப்பு நில விதிகளின் கீழ் சிறப்பு அனுமதியின்றி பழங்குடியினர் அல்லாதவர்கள் மிசோரமில் நிலம் வாங்க முடியாது."
        },
        # 47
        {
            "subtopic": "Article 332 Autonomous Districts of Assam",
            "stem_en": "Under Article 332(6), a person who is not a member of a Scheduled Tribe of an autonomous district of the State of Assam shall:",
            "stem_ta": "சரத்து 332(6)-ன் படி, அசாம் மாநிலத்தின் தன்னாட்சி மாவட்டத்தின் பட்டியலிடப்பட்ட பழங்குடியினராக இல்லாத ஒரு நபர்:",
            "options": [
                ("Not be eligible for election to the Legislative Assembly of the State from any constituency of that district", "அம்மாவட்டத்தின் எந்தவொரு தொகுதியிலிருந்தும் மாநில சட்டமன்றத்திற்குத் தேர்ந்தெடுக்கப்பட தகுதியற்றவர்"),
                ("Be entitled to automatic nomination by the Governor", "ஆளுநரால் தானியங்கி நியமனத்திற்கு உரிமை பெறுவார்"),
                ("Be eligible only for the office of Speaker", "சபாநாயகர் பதவிக்கு மட்டுமே தகுதி பெறுவார்"),
                ("Have dual voting power in all general elections", "அனைத்து பொதுத் தேர்தல்களிலும் இரட்டை வாக்குரிமை பெறுவார்")
            ],
            "correct_key": "A",
            "exp_en": "Article 332(6) mandates that no person who is not a member of a Scheduled Tribe of an autonomous district of the State of Assam shall be eligible for election to the Legislative Assembly of the State from any constituency of that district (with a limited exception for Bodoland).",
            "exp_ta": "சரத்து 332(6) அசாம் மாநிலத்தின் ஒரு தன்னாட்சி மாவட்டத்தின் ST உறுப்பினராக இல்லாத எந்தவொரு நபரும், அந்த மாவட்டத்தின் எந்தவொரு தொகுதியிலிருந்தும் மாநில சட்டமன்றத்திற்குத் தேர்ந்தெடுக்கப்பட தகுதியற்றவர் என்று கூறுகிறது.",
            "why_a_en": "Article 332(6) explicitly bars non-tribals from contesting Assembly seats from Assam's autonomous district constituencies.",
            "why_a_ta": "சரத்து 332(6) அசாமின் தன்னாட்சி மாவட்டத் தொகுதிகளிலிருந்து பழங்குடியினர் அல்லாதவர்கள் போட்டியிடுவதைத் தெளிவாகத் தடுக்கிறது.",
            "why_b_en": "No automatic nomination exists under Article 332(6).",
            "why_b_ta": "சரத்து 332(6)-ன் கீழ் தானியங்கி நியமனம் கிடையாது.",
            "why_c_en": "Speaker is chosen from amongst MLAs under Article 178.",
            "why_c_ta": "சபாநாயகர் எம்.எல்.ஏ-க்களிலிருந்து தேர்ந்தெடுக்கப்படுகிறார்.",
            "why_d_en": "Dual voting was abolished by the Constitution (Article 325 - single electoral roll).",
            "why_d_ta": "இரட்டை வாக்குரிமை சரத்து 325-ன் மூலம் ஒழிக்கப்பட்டது.",
            "tip_en": "Constituencies in Karbi Anglong and Dima Hasao are strictly reserved for indigenous autonomous district hill tribes under this clause.",
            "tip_ta": "கர்பி அங்லாங் மற்றும் திமா ஹசாவோ தொகுதிகள் இச்சரத்தின் கீழ் பூர்வீக மலைவாழ் பழங்குடியினருக்கு மட்டுமே ஒதுக்கப்பட்டுள்ளன.",
            "fact_en": "A 2003 amendment inserted a proviso protecting non-tribal representation rights in the Bodoland Territorial Areas District.",
            "fact_ta": "2003 திருத்தம் போடோலாந்து பகுதியில் பழங்குடியினர் அல்லாதவர்களின் பிரதிநிதித்துவத்தைப் பாதுகாக்க ஒரு வரம்புரையைச் சேர்த்தது."
        },
        # 48
        {
            "subtopic": "Article 339 Dhebar Commission",
            "stem_en": "The Scheduled Areas and Scheduled Tribes Commission appointed in 1960 under Article 339(1) of the Constitution was headed by:",
            "stem_ta": "அரசியலமைப்பின் சரத்து 339(1)-ன் கீழ் 1960 ஆம் ஆண்டு நியமிக்கப்பட்ட அட்டவணைப் பகுதிகள் மற்றும் பழங்குடியினர் ஆணையம் யார் தலைமையில் அமைக்கப்பட்டது?",
            "options": [
                ("U. N. Dhebar", "யு. என். தேபர்"),
                ("Dilip Singh Bhuria", "திலீப் சிங் பூரியா"),
                ("Verrier Elwin", "வெரியர் எல்வின்"),
                ("A. V. Thakkar (Thakkar Bapa)", "ஏ. வி. தக்கர் (தக்கர் பாபா)")
            ],
            "correct_key": "A",
            "exp_en": "Pursuant to Article 339(1), the President appointed the First Scheduled Areas and Scheduled Tribes Commission in April 1960 under the chairmanship of U. N. Dhebar (Dhebar Commission), which submitted an exhaustive report in 1961.",
            "exp_ta": "சரத்து 339(1)-ன் படி, குடியரசுத் தலைவர் 1960 ஏப்ரலில் யு. என். தேபர் தலைமையில் முதலாவது அட்டவணைப் பகுதிகள் மற்றும் பழங்குடியினர் ஆணையத்தை (தேபர் ஆணையம்) அமைத்தார்; இது 1961-ல் விரிவான அறிக்கையை சமர்ப்பித்தது.",
            "why_a_en": "U. N. Dhebar headed the 1960 Commission under Article 339(1).",
            "why_a_ta": "1960 ஆணையத்திற்கு யு. என். தேபர் தலைமை தாங்கினார்.",
            "why_b_en": "Dilip Singh Bhuria headed the Second Commission appointed in 2002.",
            "why_b_ta": "திலீப் சிங் பூரியா 2002-ல் அமைக்கப்பட்ட இரண்டாவது ஆணையத்திற்குத் தலைமை தாங்கினார்.",
            "why_c_en": "Verrier Elwin was an eminent anthropologist who advised Nehru on tribal policy (Panchsheel for Tribals).",
            "why_c_ta": "வெரியர் எல்வின் பழங்குடியினர் கொள்கை குறித்து நேருவுக்கு ஆலோசனை வழங்கிய மானுடவியலாளர் ஆவார்.",
            "why_d_en": "Thakkar Bapa chaired the Sub-Committee of Constituent Assembly on Excluded and Partially Excluded Areas.",
            "why_d_ta": "தக்கர் பாபா நிர்ணய சபையின் துணைக்குழுவின் தலைவராக இருந்தார்.",
            "tip_en": "The Dhebar Commission recommended strengthening the Tribes Advisory Councils and preventing tribal land alienation to non-tribals.",
            "tip_ta": "தேபர் ஆணையம் பழங்குடியினர் ஆலோசனைக் குழுக்களை வலுப்படுத்தவும், பழங்குடியினர் நிலம் பறிபோவதைத் தடுக்கவும் பரிந்துரைத்தது.",
            "fact_en": "Article 339(2) empowers the Union to give executive directions to states regarding schemes for the welfare of Scheduled Tribes.",
            "fact_ta": "சரத்து 339(2) பழங்குடியினர் நலத் திட்டங்கள் குறித்து மாநிலங்களுக்கு நிர்வாக வழிகாட்டுதல்களை வழங்க மத்திய அரசுக்கு அதிகாரம் அளிக்கிறது."
        },
        # 49
        {
            "subtopic": "Bhuria Commission 2002",
            "stem_en": "The Second Commission on Scheduled Areas and Scheduled Tribes appointed in 2002 under Article 339 was chaired by:",
            "stem_ta": "சரத்து 339-ன் கீழ் 2002 ஆம் ஆண்டு நியமிக்கப்பட்ட இரண்டாவது அட்டவணைப் பகுதிகள் மற்றும் பழங்குடியினர் ஆணையத்தின் தலைவர் யார்?",
            "options": [
                ("Dilip Singh Bhuria", "திலீப் சிங் பூரியா"),
                ("U. N. Dhebar", "யு. என். தேபர்"),
                ("Kaka Kalelkar", "காக்கா கலேல்கர்"),
                ("B. P. Mandal", "பி. பி. மண்டல்")
            ],
            "correct_key": "A",
            "exp_en": "The Second Scheduled Areas and Scheduled Tribes Commission was constituted by the President under Article 339 in July 2002 under the chairmanship of Dilip Singh Bhuria (Bhuria Commission), which submitted its report in 2004.",
            "exp_ta": "சரத்து 339-ன் கீழ் குடியரசுத் தலைவரால் 2002 ஜூலையில் திலீப் சிங் பூரியா தலைமையில் இரண்டாவது அட்டவணைப் பகுதிகள் மற்றும் பழங்குடியினர் ஆணையம் அமைக்கப்பட்டு, 2004-ல் தனது அறிக்கையை சமர்ப்பித்தது.",
            "why_a_en": "Dilip Singh Bhuria chaired the 2002 Commission under Article 339.",
            "why_a_ta": "2002 ஆணையத்திற்கு திலீப் சிங் பூரியா தலைமை தாங்கினார்.",
            "why_b_en": "U. N. Dhebar chaired the 1960 Commission.",
            "why_b_ta": "யு. என். தேபர் 1960 ஆணையத்திற்குத் தலைமை தாங்கினார்.",
            "why_c_en": "Kaka Kalelkar chaired the 1953 First Backward Classes Commission under Article 340.",
            "why_c_ta": "காக்கா கலேல்கர் 1953 முதல் பிற்படுத்தப்பட்டோர் ஆணையத்திற்குத் தலைமை தாங்கினார்.",
            "why_d_en": "B. P. Mandal chaired the 1979 Second Backward Classes Commission under Article 340.",
            "why_d_ta": "பி. பி. மண்டல் 1979 இரண்டாவது பிற்படுத்தப்பட்டோர் ஆணையத்திற்குத் தலைமை தாங்கினார்.",
            "tip_en": "Earlier, an expert committee headed by Bhuria in 1995 formulated the roadmap that became the PESA Act (Panchayats Extension to Scheduled Areas Act, 1996).",
            "tip_ta": "முன்னதாக, 1995-ல் பூரியா தலைமையிலான நிபுணர் குழுவின் பரிந்துரைகளே 1996 PESA சட்டம் உருவாவதற்கு வழிகாட்டின.",
            "fact_en": "The 2002-2004 Bhuria report focused heavily on forest rights, which subsequently led to the Forest Rights Act (FRA) 2006.",
            "fact_ta": "பூரியாவின் 2004 அறிக்கை வன உரிமைகள் மீது கவனம் செலுத்தியது; இது பின்னர் 2006 வன உரிமைச் சட்டத்திற்கு (FRA) வழிவகுத்தது."
        },
        # 50
        {
            "subtopic": "Article 371 to 371J Constitutional Synthesis",
            "stem_en": "Which of the following statements accurately summarizes the constitutional character of Articles 371 to 371J?",
            "stem_ta": "சரத்துகள் 371 முதல் 371J வரையிலான அரசியலமைப்புத் தன்மையை பின்வரும் கூற்றுகளில் எது துல்லியமாக சுருக்கமாகக் கூறுகிறது?",
            "options": [
                ("They provide specialized asymmetrical constitutional protections to 12 distinct States to protect local cultures, resolve historical disputes, and accelerate regional economic growth", "உள்ளூர் கலாச்சாரங்களைப் பாதுகாக்கவும், வரலாற்று தகராறுகளைத் தீர்க்கவும், பிராந்திய பொருளாதார வளர்ச்சியை விரைவுபடுத்தவும் அவை 12 வெவ்வேறு மாநிலங்களுக்கு சிறப்பு சமச்சீரற்ற அரசியலமைப்புப் பாதுகாப்புகளை வழங்குகின்றன"),
                ("They abolish all state legislatures and place the governors in direct military command", "அவை அனைத்து மாநில சட்டமன்றங்களையும் ரத்து செய்து, ஆளுநர்களை நேரடி ராணுவக் கட்டுப்பாட்டில் வைக்கின்றன"),
                ("They apply uniformly only to Union Territories administered by Lieutenant Governors", "துணைநிலை ஆளுநர்களால் நிர்வகிக்கப்படும் யூனியன் பிரதேசங்களுக்கு மட்டுமே அவை ஒரே சீராகப் பொருந்தும்"),
                ("They were designed as emergency war measures that expired after the 1971 Indo-Pak war", "1971 இந்தியா-பாகிஸ்தான் போருக்குப் பிறகு காலாவதியான அவசரகால போர் நடவடிக்கைகளாக அவை வடிவமைக்கப்பட்டன")
            ],
            "correct_key": "A",
            "exp_en": "Articles 371 to 371J embody asymmetrical federalism, extending tailor-made constitutional governance frameworks to 12 States (Maharashtra, Gujarat, Nagaland, Assam, Manipur, Andhra Pradesh, Telangana, Sikkim, Mizoram, Arunachal Pradesh, Goa, and Karnataka) to safeguard tribal cultures, redress regional disparities, and maintain national unity.",
            "exp_ta": "சரத்துகள் 371 முதல் 371J வரை சமச்சீரற்ற கூட்டாட்சியை வெளிப்படுத்துகின்றன; பழங்குடி கலாச்சாரங்களைப் பாதுகாக்கவும், பிராந்திய ஏற்றத்தாழ்வுகளைக் களையவும், தேசிய ஒருமைப்பாட்டைப் பேணவும் 12 மாநிலங்களுக்கு பிரத்யேக அரசியலமைப்பு நிர்வாகக் கட்டமைப்பை வழங்குகின்றன.",
            "why_a_en": "Accurately synthesizes the purpose and scope across the 12 covered states.",
            "why_a_ta": "12 மாநிலங்களின் நோக்கம் மற்றும் வரம்பை துல்லியமாக சுருக்கிக் கூறுகிறது.",
            "why_b_en": "Legislatures are empowered and protected, not abolished.",
            "why_b_ta": "சட்டமன்றங்கள் பாதுகாக்கப்பட்டு அதிகாரமளிக்கப்பட்டுள்ளன.",
            "why_c_en": "They apply to full States, not UTs under Part VIII.",
            "why_c_ta": "அவை முழு மாநிலங்களுக்குப் பொருந்தும், யூனியன் பிரதேசங்களுக்கு அல்ல.",
            "why_d_en": "They are permanent special provisions of the Constitution, not expired war measures.",
            "why_d_ta": "அவை அரசியலமைப்பின் நிரந்தர சிறப்பு ஏற்பாடுகள், காலாவதியானவை அல்ல.",
            "tip_en": "Remember the count: 12 States are covered under Article 371 to 371J.",
            "tip_ta": "எண்ணிக்கையை நினைவில் கொள்க: சரத்து 371 முதல் 371J வரை 12 மாநிலங்கள் உள்ளடக்கப்பட்டுள்ளன.",
            "fact_en": "The Supreme Court has consistently held that these provisions form part of the constitutional scheme to maintain unity in diversity.",
            "fact_ta": "வேற்றுமையில் ஒற்றுமையைப் பேணும் அரசியலமைப்புத் திட்டத்தின் ஒரு பகுதியாக இப்பிரிவுகள் உள்ளன என உச்ச நீதிமன்றம் தொடர்ந்து உறுதிப்படுத்தியுள்ளது."
        }
    ]

    questions = []
    for idx, item in enumerate(raw, start=1):
        qid = f"SPS_M_{idx:03d}"
        opts = item["options"]
        q = make_sps_q(
            qid=qid,
            diff="Medium",
            qtype="Direct MCQ",
            subtopic=item["subtopic"],
            en_stem=item["stem_en"],
            ta_stem=item["stem_ta"],
            en_a=opts[0][0],
            ta_a=opts[0][1],
            en_b=opts[1][0],
            ta_b=opts[1][1],
            en_c=opts[2][0],
            ta_c=opts[2][1],
            en_d=opts[3][0],
            ta_d=opts[3][1],
            correct_key=item["correct_key"],
            exp_en=item["exp_en"],
            exp_ta=item["exp_ta"],
            why_a_en=item["why_a_en"],
            why_a_ta=item["why_a_ta"],
            why_b_en=item["why_b_en"],
            why_b_ta=item["why_b_ta"],
            why_c_en=item["why_c_en"],
            why_c_ta=item["why_c_ta"],
            why_d_en=item["why_d_en"],
            why_d_ta=item["why_d_ta"],
            tip_en=item["tip_en"],
            tip_ta=item["tip_ta"],
            fact_en=item["fact_en"],
            fact_ta=item["fact_ta"],
            tags=["polity", "special_provisions_states", "medium", item["subtopic"].lower().replace(" ", "_")]
        )
        questions.append(q)
    return questions

def build_medium_file():
    qs = get_medium_questions()
    print(f"Generated {len(qs)} raw Medium questions for Special Provisions for States.")
    balanced = randomize_and_balance_dataset(qs, seed=43)
    
    out_dir = os.path.join("data", "questions", "polity")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "special_provisions_states_medium.json")
    
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(balanced, f, ensure_ascii=False, indent=2)
    print(f"Saved balanced Medium MCQs to {out_path}")
    
    rep = ContentValidator.validate_file(out_path, expected_count=50, expected_prefix="SPS_M_")
    print(f"Validation: {'PASS' if rep.is_valid else 'FAIL'} | Total: {rep.total_audited}")
    print(f"Keys: {rep.key_distribution}")
    if not rep.is_valid:
        for iss in rep.issues:
            print("  Issue:", iss.severity, iss.field_name, iss.message)
    return rep.is_valid

if __name__ == "__main__":
    success = build_medium_file()
    if not success:
        exit(1)
