# -*- coding: utf-8 -*-
"""
Special Provisions for States - Part 1 Easy MCQs Generator (50 MCQs: SPS_E_001 to SPS_E_050)
TNPSC Nova AI Content Engine
"""
import json
import os
from special_provisions_states_mcq_helper import make_sps_q
from tools.nova_content_engine.answer_randomizer import randomize_and_balance_dataset
from tools.nova_content_engine.validator import ContentValidator

def get_easy_questions():
    raw = [
        # 1
        {
            "subtopic": "Part XXI Constitutional Architecture",
            "stem_en": "Which Part of the Constitution of India deals with 'Temporary, Transitional and Special Provisions'?",
            "stem_ta": "இந்திய அரசியலமைப்பின் எந்தப் பகுதி 'தற்காலிக, இடைமாற்ற மற்றும் சிறப்பு ஏற்பாடுகள்' பற்றிக் கூறுகிறது?",
            "options": [
                ("Part XXI", "பகுதி XXI"),
                ("Part XX", "பகுதி XX"),
                ("Part XIX", "பகுதி XIX"),
                ("Part XVIII", "பகுதி XVIII")
            ],
            "correct_key": "A",
            "exp_en": "Part XXI of the Constitution of India encompasses Articles 369 to 392, dealing with Temporary, Transitional and Special Provisions, including Articles 371 to 371J.",
            "exp_ta": "இந்திய அரசியலமைப்பின் பகுதி XXI, சரத்துகள் 369 முதல் 392 வரை உள்ளடக்கியது. இது சரத்துகள் 371 முதல் 371J வரையிலான சிறப்பு ஏற்பாடுகள் உட்பட தற்காலிக, இடைமாற்ற மற்றும் சிறப்பு ஏற்பாடுகளைக் கையாள்கிறது.",
            "why_a_en": "Part XXI explicitly contains Temporary, Transitional and Special Provisions (Articles 369-392).",
            "why_a_ta": "பகுதி XXI தற்காலிக, இடைமாற்ற மற்றும் சிறப்பு ஏற்பாடுகளை (சரத்துகள் 369-392) தெளிவாகக் கொண்டுள்ளது.",
            "why_b_en": "Part XX contains only Article 368 dealing with Amendment of the Constitution.",
            "why_b_ta": "பகுதி XX அரசியலமைப்புத் திருத்தம் தொடர்பான சரத்து 368-ஐ மட்டுமே கொண்டுள்ளது.",
            "why_c_en": "Part XIX deals with Miscellaneous provisions (Articles 361-367).",
            "why_c_ta": "பகுதி XIX இதர விதிகளைக் (சரத்துகள் 361-367) கையாள்கிறது.",
            "why_d_en": "Part XVIII deals with Emergency Provisions (Articles 352-360).",
            "why_d_ta": "பகுதி XVIII அவசரகால விதிகளைக் (சரத்துகள் 352-360) கையாள்கிறது.",
            "tip_en": "Part XXI: Articles 369-392. Articles 371 to 371-J contain state-specific special provisions.",
            "tip_ta": "பகுதி XXI: சரத்துகள் 369-392. சரத்துகள் 371 முதல் 371-J வரை குறிப்பிட்ட மாநிலங்களுக்கான சிறப்பு ஏற்பாடுகளைக் கொண்டுள்ளன.",
            "fact_en": "Originally, Part XXI had temporary provisions; special provisions for states were progressively added via amendments.",
            "fact_ta": "முதலில் பகுதி XXI தற்காலிக ஏற்பாடுகளைக் கொண்டிருந்தது; பின்னர் திருத்தங்கள் மூலம் மாநிலங்களுக்கான சிறப்பு ஏற்பாடுகள் சேர்க்கப்பட்டன."
        },
        # 2
        {
            "subtopic": "Article 371 Maharashtra and Gujarat",
            "stem_en": "Under Article 371 of the Constitution of India, the President may provide for separate development boards for which regions of Maharashtra?",
            "stem_ta": "இந்திய அரசியலமைப்பின் சரத்து 371-ன் கீழ், மகாராஷ்டிராவின் எந்தப் பகுதிகளுக்கு தனி வளர்ச்சி வாரியங்களை அமைக்க குடியரசுத் தலைவர் வகைசெய்யலாம்?",
            "options": [
                ("Vidarbha, Marathwada and the rest of Maharashtra", "விதர்பா, மராத்வாடா மற்றும் மகாராஷ்டிராவின் எஞ்சிய பகுதிகள்"),
                ("Saurashtra and Kutch only", "சௌராஷ்டிரா மற்றும் கட்ச் மட்டுமே"),
                ("Konkan and Western Ghats", "கொங்கண் மற்றும் மேற்குத் தொடர்ச்சி மலை"),
                ("Telangana and Rayalaseema", "தெலங்கானா மற்றும் இராயலசீமா")
            ],
            "correct_key": "A",
            "exp_en": "Article 371 authorizes the President to provide that the Governor of Maharashtra shall have special responsibility for establishing separate development boards for Vidarbha, Marathwada and the rest of Maharashtra.",
            "exp_ta": "சரத்து 371, விதர்பா, மராத்வாடா மற்றும் மகாராஷ்டிராவின் எஞ்சிய பகுதிகளுக்கு தனி வளர்ச்சி வாரியங்களை நிறுவுவதில் மகாராஷ்டிர ஆளுநருக்கு சிறப்புப் பொறுப்பு வழங்க குடியரசுத் தலைவருக்கு அதிகாரம் அளிக்கிறது.",
            "why_a_en": "Article 371 explicitly specifies Vidarbha, Marathwada, and the rest of Maharashtra.",
            "why_a_ta": "சரத்து 371 குறிப்பாக விதர்பா, மராத்வாடா மற்றும் மகாராஷ்டிராவின் எஞ்சிய பகுதிகளைக் குறிப்பிடுகிறது.",
            "why_b_en": "Saurashtra and Kutch belong to Gujarat under Article 371.",
            "why_b_ta": "சௌராஷ்டிரா மற்றும் கட்ச் ஆகியவை சரத்து 371-ன் கீழ் குஜராத்திற்கு உட்பட்டவை.",
            "why_c_en": "Konkan is not individually enumerated as a separate board region in Article 371.",
            "why_c_ta": "கொங்கண் சரத்து 371-ல் தனி வாரியப் பகுதியாக குறிப்பிடப்படவில்லை.",
            "why_d_en": "Telangana and Rayalaseema relate to Andhra Pradesh under Article 371D.",
            "why_d_ta": "தெலங்கானா மற்றும் இராயலசீமா சரத்து 371D-ன் கீழ் ஆந்திரப் பிரதேசத்துடன் தொடர்புடையவை.",
            "tip_en": "Article 371 covers two states: Maharashtra (Vidarbha, Marathwada) and Gujarat (Saurashtra, Kutch).",
            "tip_ta": "சரத்து 371 இரண்டு மாநிலங்களை உள்ளடக்கியது: மகாராஷ்டிரா (விதர்பா, மராத்வாடா) மற்றும் குஜராத் (சௌராஷ்டிரா, கட்ச்).",
            "fact_en": "Reports on the working of these development boards must be placed each year before the State Legislative Assembly.",
            "fact_ta": "இவ்வளர்ச்சி வாரியங்களின் செயல்பாடுகள் குறித்த அறிக்கைகள் ஒவ்வோர் ஆண்டும் மாநிலச் சட்டமன்றத்தின் முன் வைக்கப்பட வேண்டும்."
        },
        # 3
        {
            "subtopic": "Article 371 Maharashtra and Gujarat",
            "stem_en": "Which regions of Gujarat are covered under the special provisions of Article 371 for establishing development boards?",
            "stem_ta": "வளர்ச்சி வாரியங்களை அமைப்பதற்கான சரத்து 371-ன் சிறப்பு விதிகளின் கீழ் குஜராத்தின் எந்தப் பகுதிகள் உள்ளடக்கப்பட்டுள்ளன?",
            "options": [
                ("Saurashtra, Kutch and the rest of Gujarat", "சௌராஷ்டிரா, கட்ச் மற்றும் குஜராத்தின் எஞ்சிய பகுதிகள்"),
                ("Vidarbha and Marathwada", "விதர்பா மற்றும் மராத்வாடா"),
                ("North Gujarat and South Gujarat only", "வடக்கு குஜராத் மற்றும் தெற்கு குஜராத் மட்டுமே"),
                ("Ahmedabad and Gandhinagar", "அகமதாபாத் மற்றும் காந்திநகர்")
            ],
            "correct_key": "A",
            "exp_en": "Under Article 371(2), separate development boards can be established for Saurashtra, Kutch, and the rest of Gujarat with equitable allocation of funds.",
            "exp_ta": "சரத்து 371(2)-ன் கீழ், நிதி ஒதுக்கீட்டுடன் சௌராஷ்டிரா, கட்ச் மற்றும் குஜராத்தின் எஞ்சிய பகுதிகளுக்கு தனி வளர்ச்சி வாரியங்களை அமைக்கலாம்.",
            "why_a_en": "Article 371(2) explicitly enumerates Saurashtra, Kutch and the rest of Gujarat.",
            "why_a_ta": "சரத்து 371(2) சௌராஷ்டிரா, கட்ச் மற்றும் குஜராத்தின் எஞ்சிய பகுதிகளை தெளிவாகப் பட்டியலிடுகிறது.",
            "why_b_en": "Vidarbha and Marathwada are in Maharashtra under Article 371(2).",
            "why_b_ta": "விதர்பா மற்றும் மராத்வாடா சரத்து 371(2)-ன் கீழ் மகாராஷ்டிராவில் உள்ளன.",
            "why_c_en": "North and South Gujarat are administrative divisions, not constitutional regions under Article 371.",
            "why_c_ta": "வடக்கு மற்றும் தெற்கு குஜராத் ஆகியவை நிர்வாகப் பிரிவுகள், சரத்து 371-ன் கீழான அரசியலமைப்புப் பகுதிகள் அல்ல.",
            "why_d_en": "Ahmedabad and Gandhinagar are specific cities.",
            "why_d_ta": "அகமதாபாத் மற்றும் காந்திநகர் ஆகியவை குறிப்பிட்ட நகரங்கள்.",
            "tip_en": "Article 371 was modified by the 7th Constitutional Amendment Act 1956 during state reorganization.",
            "tip_ta": "சரத்து 371 மாநில மறுசீரமைப்பின் போது 1956-ன் 7வது அரசியலமைப்புத் திருத்தச் சட்டத்தால் மாற்றியமைக்கப்பட்டது.",
            "fact_en": "Equitable arrangement for technical education, vocational training and state employment is mandated under Art 371(2).",
            "fact_ta": "தொழில்நுட்பக் கல்வி, தொழிற்பயிற்சி மற்றும் அரசு வேலைவாய்ப்பில் சமமான வாய்ப்பு வழங்குவது சரத்து 371(2)-ன் கீழ் கட்டாயமாக்கப்பட்டுள்ளது."
        },
        # 4
        {
            "subtopic": "Article 371A Nagaland",
            "stem_en": "Which Constitutional Amendment Act inserted Article 371A to provide special provisions for Nagaland?",
            "stem_ta": "நாகாலாந்திற்கு சிறப்பு ஏற்பாடுகளை வழங்க எந்த அரசியலமைப்புத் திருத்தச் சட்டம் சரத்து 371A-ஐ சேர்த்தது?",
            "options": [
                ("13th Constitutional Amendment Act, 1962", "13வது அரசியலமைப்புத் திருத்தச் சட்டம், 1962"),
                ("22nd Constitutional Amendment Act, 1969", "22வது அரசியலமைப்புத் திருத்தச் சட்டம், 1969"),
                ("27th Constitutional Amendment Act, 1971", "27வது அரசியலமைப்புத் திருத்தச் சட்டம், 1971"),
                ("36th Constitutional Amendment Act, 1975", "36வது அரசியலமைப்புத் திருத்தச் சட்டம், 1975")
            ],
            "correct_key": "A",
            "exp_en": "Article 371A was inserted by the 13th Constitutional Amendment Act, 1962 following the 16-Point Agreement between the Government of India and the Naga People's Convention.",
            "exp_ta": "இந்திய அரசிற்கும் நாகா மக்கள் மாநாட்டிற்கும் இடையிலான 16 அம்ச ஒப்பந்தத்தைத் தொடர்ந்து, 1962 ஆம் ஆண்டின் 13வது அரசியலமைப்புத் திருத்தச் சட்டத்தின் மூலம் சரத்து 371A சேர்க்கப்பட்டது.",
            "why_a_en": "13th CAA 1962 inserted Article 371A for Nagaland.",
            "why_a_ta": "1962-ன் 13வது சட்டத்திருத்தம் நாகாலாந்திற்காக சரத்து 371A-ஐச் சேர்த்தது.",
            "why_b_en": "22nd CAA 1969 inserted Article 371B for Assam.",
            "why_b_ta": "1969-ன் 22வது சட்டத்திருத்தம் அசாமிற்காக சரத்து 371B-ஐச் சேர்த்தது.",
            "why_c_en": "27th CAA 1971 inserted Article 371C for Manipur.",
            "why_c_ta": "1971-ன் 27வது சட்டத்திருத்தம் மணிப்பூருக்காக சரத்து 371C-ஐச் சேர்த்தது.",
            "why_d_en": "36th CAA 1975 inserted Article 371F for Sikkim.",
            "why_d_ta": "1975-ன் 36வது சட்டத்திருத்தம் சிக்கிமிற்காக சரத்து 371F-ஐச் சேர்த்தது.",
            "tip_en": "Remember the sequence: 13th CAA (371A - Nagaland), 22nd CAA (371B - Assam), 27th CAA (371C - Manipur).",
            "tip_ta": "வரிசையை நினைவில் கொள்க: 13வது திருத்தம் (371A - நாகாலாந்து), 22வது திருத்தம் (371B - அசாம்), 27வது திருத்தம் (371C - மணிப்பூர்).",
            "fact_en": "Nagaland became the 16th State of the Indian Union on 1 December 1963.",
            "fact_ta": "1963 டிசம்பர் 1 அன்று நாகாலாந்து இந்திய ஒன்றியத்தின் 16வது மாநிலமாக உருவானது."
        },
        # 5
        {
            "subtopic": "Article 371A Nagaland",
            "stem_en": "Under Article 371A, an Act of Parliament regarding Naga religious or social practices applies to Nagaland only if:",
            "stem_ta": "சரத்து 371A-ன் கீழ், நாகா மத அல்லது சமூக நடைமுறைகள் தொடர்பான நாடாளுமன்றச் சட்டம் நாகாலாந்திற்கு எப்போது மட்டுமே பொருந்தும்?",
            "options": [
                ("The Legislative Assembly of Nagaland so decides by a resolution", "நாகாலாந்து சட்டமன்றம் ஒரு தீர்மானம் மூலம் அவ்வாறு முடிவு செய்தால்"),
                ("The Governor approves it with absolute veto", "ஆளுநர் முழுமையான வீட்டோவுடன் ஒப்புதல் அளித்தால்"),
                ("The President issues a notification in the Official Gazette", "குடியரசுத் தலைவர் அரசிதழில் அறிவிப்பு வெளியிட்டால்"),
                ("The Supreme Court validates it under judicial review", "நீதித்துறை மறுஆய்வின் கீழ் உச்ச நீதிமன்றம் அதை உறுதிசெய்தால்")
            ],
            "correct_key": "A",
            "exp_en": "Article 371A(1)(a) provides that no Act of Parliament in respect of religious or social practices of the Nagas, Naga customary law and procedure, administration of civil and criminal justice involving decisions according to Naga customary law, and ownership and transfer of land shall apply to Nagaland unless the Legislative Assembly of Nagaland by resolution so decides.",
            "exp_ta": "சரத்து 371A(1)(a)-ன் படி, நாகாலாந்து சட்டமன்றம் தீர்மானம் மூலம் அவ்வாறு முடிவு செய்யாவிட்டால், நாகர்களின் மத அல்லது சமூக நடைமுறைகள், நாகா மரபுச் சட்டம், நில உரிமை மற்றும் பரிமாற்றம் தொடர்பான நாடாளுமன்றச் சட்டங்கள் நாகாலாந்திற்குப் பொருந்தாது.",
            "why_a_en": "Article 371A(1)(a) mandates a resolution by the Legislative Assembly of Nagaland.",
            "why_a_ta": "சரத்து 371A(1)(a) நாகாலாந்து சட்டமன்றத்தின் தீர்மானத்தைக் கட்டாயமாக்குகிறது.",
            "why_b_en": "The Governor cannot override the Legislative Assembly resolution requirement on customary matters.",
            "why_b_ta": "மரபு விவகாரங்களில் சட்டமன்றத் தீர்மானத் தேவையை ஆளுநர் புறந்தள்ள முடியாது.",
            "why_c_en": "Presidential notification alone is insufficient; state assembly resolution is mandatory.",
            "why_c_ta": "குடியரசுத் தலைவர் அறிவிப்பு மட்டுமே போதாது; மாநில சட்டமன்றத் தீர்மானம் கட்டாயம்.",
            "why_d_en": "Supreme Court validation is not the constitutional mechanism for statutory extension here.",
            "why_d_ta": "சட்டத்தை நீட்டிப்பதற்கான அரசியலமைப்பு வழிமுறை உச்ச நீதிமன்ற உறுதிப்பாடு அல்ல.",
            "tip_en": "Four protected fields in Art 371A: religious/social practices, customary law, customary civil/criminal justice, ownership/transfer of land.",
            "tip_ta": "சரத்து 371A-ல் பாதுகாக்கப்பட்ட 4 துறைகள்: மத/சமூக நடைமுறைகள், மரபுச் சட்டம், மரபுசார் உரிமையியல்/குற்றவியல் நீதி, நில உரிமை/பரிமாற்றம்.",
            "fact_en": "This non-obstante clause gives Nagaland legislative supremacy over central laws in specified customary domains.",
            "fact_ta": "இந்த சிறப்பு விதி குறிப்பிட்ட மரபுசார் துறைகளில் மத்திய சட்டங்களை விட நாகாலாந்து சட்டமன்றத்திற்கு மேலாதிக்கத்தை அளிக்கிறது."
        },
        # 6
        {
            "subtopic": "Article 371A Nagaland",
            "stem_en": "Which district of Nagaland has a special regional council provided for under Article 371A?",
            "stem_ta": "சரத்து 371A-ன் கீழ் நாகாலாந்தின் எந்த மாவட்டத்திற்கு சிறப்புப் பிராந்தியக் குழு வகைசெய்யப்பட்டுள்ளது?",
            "options": [
                ("Tuensang district", "டியூன்சாங் மாவட்டம்"),
                ("Kohima district", "கோஹிமா மாவட்டம்"),
                ("Mokokchung district", "மோகோக்சுங் மாவட்டம்"),
                ("Dimapur district", "திமாபூர் மாவட்டம்")
            ],
            "correct_key": "A",
            "exp_en": "Under Article 371A(1)(d) and (2), a regional council consisting of 35 members was established for the Tuensang district, and the Governor had special responsibility for its administration for 10 years.",
            "exp_ta": "சரத்து 371A(1)(d) மற்றும் (2)-ன் கீழ், டியூன்சாங் மாவட்டத்திற்கு 35 உறுப்பினர்களைக் கொண்ட பிராந்தியக் குழு அமைக்கப்பட்டது, மேலும் 10 ஆண்டுகளுக்கு அதன் நிர்வாகத்திற்கு ஆளுநருக்கு சிறப்புப் பொறுப்பு இருந்தது.",
            "why_a_en": "Tuensang district is explicitly provided with a regional council under Article 371A(2).",
            "why_a_ta": "டியூன்சாங் மாவட்டம் சரத்து 371A(2)-ன் கீழ் பிராந்தியக் குழுவுடன் தெளிவாக வகைசெய்யப்பட்டுள்ளது.",
            "why_b_en": "Kohima is the state capital and was not governed by the special regional council clause.",
            "why_b_ta": "கோஹிமா மாநிலத் தலைநகரம், அது சிறப்புப் பிராந்தியக் குழு விதியால் நிர்வகிக்கப்படவில்லை.",
            "why_c_en": "Mokokchung is an administrative district without this specific regional council provision.",
            "why_c_ta": "மோகோக்சுங் இக்குறிப்பிட்ட பிராந்தியக் குழு விதியற்ற ஒரு நிர்வாக மாவட்டம்.",
            "why_d_en": "Dimapur is the commercial hub, not the Tuensang regional council area.",
            "why_d_ta": "திமாபூர் வணிக மையம், டியூன்சாங் பிராந்தியக் குழு பகுதி அல்ல.",
            "tip_en": "Art 371A Tuensang Regional Council: 35 members with Deputy Commissioner as ex-officio Chairman.",
            "tip_ta": "சரத்து 371A டியூன்சாங் பிராந்தியக் குழு: துணை ஆணையரை பதவிவழித் தலைவராகக் கொண்ட 35 உறுப்பினர்கள்.",
            "fact_en": "One member from Tuensang was also appointed Minister for Tuensang Affairs in the State Cabinet.",
            "fact_ta": "டியூன்சாங்கிலிருந்து ஒரு உறுப்பினர் மாநில அமைச்சரவையில் டியூன்சாங் விவகாரங்களுக்கான அமைச்சராகவும் நியமிக்கப்பட்டார்."
        },
        # 7
        {
            "subtopic": "Article 371B Assam",
            "stem_en": "Which Constitutional Amendment Act inserted Article 371B relating to the State of Assam?",
            "stem_ta": "அசாம் மாநிலம் தொடர்பான சரத்து 371B-ஐ எந்த அரசியலமைப்புத் திருத்தச் சட்டம் சேர்த்தது?",
            "options": [
                ("22nd Constitutional Amendment Act, 1969", "22வது அரசியலமைப்புத் திருத்தச் சட்டம், 1969"),
                ("13th Constitutional Amendment Act, 1962", "13வது அரசியலமைப்புத் திருத்தச் சட்டம், 1962"),
                ("27th Constitutional Amendment Act, 1971", "27வது அரசியலமைப்புத் திருத்தச் சட்டம், 1971"),
                ("32nd Constitutional Amendment Act, 1973", "32வது அரசியலமைப்புத் திருத்தச் சட்டம், 1973")
            ],
            "correct_key": "A",
            "exp_en": "Article 371B was inserted by the 22nd Constitutional Amendment Act, 1969 to facilitate the creation of an autonomous sub-state (Meghalaya) and provide for a committee of the Assam Assembly consisting of tribal area representatives.",
            "exp_ta": "ஒரு தன்னாட்சி துணை மாநிலத்தை (மேகாலயா) உருவாக்கவும், பழங்குடியினப் பிரதிநிதிகளைக் கொண்ட அசாம் சட்டமன்றக் குழுவை அமைக்கவும் 1969-ன் 22வது அரசியலமைப்புத் திருத்தச் சட்டம் மூலம் சரத்து 371B சேர்க்கப்பட்டது.",
            "why_a_en": "22nd CAA 1969 inserted Article 371B.",
            "why_a_ta": "1969-ன் 22வது சட்டத்திருத்தம் சரத்து 371B-ஐ சேர்த்தது.",
            "why_b_en": "13th CAA 1962 inserted Article 371A for Nagaland.",
            "why_b_ta": "1962-ன் 13வது சட்டத்திருத்தம் நாகாலாந்திற்காக சரத்து 371A-ஐ சேர்த்தது.",
            "why_c_en": "27th CAA 1971 inserted Article 371C for Manipur.",
            "why_c_ta": "1971-ன் 27வது சட்டத்திருத்தம் மணிப்பூருக்காக சரத்து 371C-ஐ சேர்த்தது.",
            "why_d_en": "32nd CAA 1973 inserted Article 371D and 371E for Andhra Pradesh.",
            "why_d_ta": "1973-ன் 32வது சட்டத்திருத்தம் ஆந்திராவிற்காக சரத்துகள் 371D மற்றும் 371E-ஐ சேர்த்தது.",
            "tip_en": "Article 371B = Assam (22nd CAA 1969). Remember 'B' for 'Brahmaputra/Assam'.",
            "tip_ta": "சரத்து 371B = அசாம் (22வது திருத்தம் 1969). 'B' என்பதை 'பிரம்மபுத்திரா/அசாம்' என நினைவில் கொள்க.",
            "fact_en": "The committee consists of members elected from tribal areas specified in Part I of the Sixth Schedule table.",
            "fact_ta": "இக்குழு ஆறாவது அட்டவணை அட்டவணையின் பகுதி I-ல் குறிப்பிடப்பட்டுள்ள பழங்குடிப் பகுதிகளிலிருந்து தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்களைக் கொண்டுள்ளது."
        },
        # 8
        {
            "subtopic": "Article 371C Manipur",
            "stem_en": "Under Article 371C, the President may provide for the constitution of a committee of the Manipur Legislative Assembly consisting of members elected from:",
            "stem_ta": "சரத்து 371C-ன் கீழ், எந்தப் பகுதியிலிருந்து தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்களைக் கொண்ட மணிப்பூர் சட்டமன்றக் குழுவை அமைக்க குடியரசுத் தலைவர் வகைசெய்யலாம்?",
            "options": [
                ("The Hill Areas of Manipur", "மணிப்பூரின் மலைப்பகுதிகள்"),
                ("The Valley Areas of Manipur only", "மணிப்பூரின் பள்ளத்தாக்குப் பகுதிகள் மட்டுமே"),
                ("Imphal Municipal Corporation only", "இம்பால் மாநகராட்சி மட்டுமே"),
                ("Border areas adjoining Myanmar", "மியான்மர் எல்லையோரப் பகுதிகள்")
            ],
            "correct_key": "A",
            "exp_en": "Article 371C provides for the constitution and functions of a committee of the Legislative Assembly of Manipur consisting of members of that Assembly elected from the Hill Areas of Manipur.",
            "exp_ta": "சரத்து 371C மணிப்பூரின் மலைப்பகுதிகளிலிருந்து தேர்ந்தெடுக்கப்பட்ட சட்டமன்ற உறுப்பினர்களைக் கொண்ட குழுவின் அமைப்பு மற்றும் பணிகளுக்கு வகைசெய்கிறது.",
            "why_a_en": "Article 371C explicitly specifies members elected from the Hill Areas.",
            "why_a_ta": "சரத்து 371C மலைப்பகுதிகளிலிருந்து தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்களை தெளிவாகக் குறிப்பிடுகிறது.",
            "why_b_en": "The Valley areas are predominantly Meitei areas and not the subject of the Art 371C Hill Areas Committee.",
            "why_b_ta": "பள்ளத்தாக்குப் பகுதிகள் முதன்மையாக மெய்தேய் பகுதிகள், அவை சரத்து 371C மலைப்பகுதிகள் குழுவின் கீழ் வரவில்லை.",
            "why_c_en": "Imphal is located in the valley and not part of the Hill Areas.",
            "why_c_ta": "இம்பால் பள்ளத்தாக்கில் அமைந்துள்ளது, மலைப்பகுதிகளின் பகுதியல்ல.",
            "why_d_en": "Border areas are not the constitutional term; 'Hill Areas' is the defined term.",
            "why_d_ta": "எல்லையோரப் பகுதிகள் என்பது அரசியலமைப்புச் சொல் அல்ல; 'மலைப்பகுதிகள்' என்பதே வரையறுக்கப்பட்ட சொல்.",
            "tip_en": "Article 371C also mandates that the Governor must submit an annual report to the President regarding the administration of Hill Areas.",
            "tip_ta": "சரத்து 371C மலைப்பகுதிகள் நிர்வாகம் குறித்து ஆளுநர் குடியரசுத் தலைவருக்கு ஆண்டு அறிக்கை சமர்ப்பிக்க வேண்டும் என்றும் கட்டாயமாக்குகிறது.",
            "fact_en": "Article 371C was inserted by the 27th Constitutional Amendment Act, 1971 when Manipur became a full-fledged State.",
            "fact_ta": "மணிப்பூர் முழு மாநிலமானபோது 1971-ன் 27வது அரசியலமைப்புத் திருத்தச் சட்டம் மூலம் சரத்து 371C சேர்க்கப்பட்டது."
        },
        # 9
        {
            "subtopic": "Article 371D Andhra Pradesh and Telangana",
            "stem_en": "Which Constitutional Amendment Act inserted Articles 371D and 371E to satisfy the aspirations of people in Andhra Pradesh?",
            "stem_ta": "ஆந்திரப் பிரதேச மக்களின் விருப்பங்களை நிறைவேற்ற எந்த அரசியலமைப்புத் திருத்தச் சட்டம் சரத்துகள் 371D மற்றும் 371E-ஐ சேர்த்தது?",
            "options": [
                ("32nd Constitutional Amendment Act, 1973", "32வது அரசியலமைப்புத் திருத்தச் சட்டம், 1973"),
                ("42nd Constitutional Amendment Act, 1976", "42வது அரசியலமைப்புத் திருத்தச் சட்டம், 1976"),
                ("44th Constitutional Amendment Act, 1978", "44வது அரசியலமைப்புத் திருத்தச் சட்டம், 1978"),
                ("73rd Constitutional Amendment Act, 1992", "73வது அரசியலமைப்புத் திருத்தச் சட்டம், 1992")
            ],
            "correct_key": "A",
            "exp_en": "The 32nd Constitutional Amendment Act, 1973 inserted Articles 371D and 371E to implement the Six-Point Formula resolving regional disputes between Telangana, Coastal Andhra, and Rayalaseema.",
            "exp_ta": "தெலங்கானா, கடலோர ஆந்திரா மற்றும் இராயலசீமா இடையேயான பிராந்தியப் பிரச்சனைகளைத் தீர்க்கும் ஆறு அம்ச சூத்திரத்தை செயல்படுத்த 1973-ன் 32வது அரசியலமைப்புத் திருத்தச் சட்டம் சரத்துகள் 371D மற்றும் 371E-ஐ சேர்த்தது.",
            "why_a_en": "32nd CAA 1973 inserted Articles 371D and 371E.",
            "why_a_ta": "1973-ன் 32வது சட்டத்திருத்தம் சரத்துகள் 371D மற்றும் 371E-ஐ சேர்த்தது.",
            "why_b_en": "42nd CAA 1976 is known as the Mini-Constitution.",
            "why_b_ta": "1976-ன் 42வது சட்டத்திருத்தம் குறு-அரசியலமைப்பு என அழைக்கப்படுகிறது.",
            "why_c_en": "44th CAA 1978 restored constitutional safeguards post-Emergency.",
            "why_c_ta": "1978-ன் 44வது சட்டத்திருத்தம் அவசரகாலத்திற்குப் பிந்தைய அரசியலமைப்புப் பாதுகாப்புகளை மீட்டெடுத்தது.",
            "why_d_en": "73rd CAA 1992 constitutionalized Panchayati Raj.",
            "why_d_ta": "1992-ன் 73வது சட்டத்திருத்தம் பஞ்சாயத்து ராஜிற்கு அரசியலமைப்பு அந்தஸ்து வழங்கியது.",
            "tip_en": "Article 371D: Equitable opportunities in education and public employment across zones in AP & Telangana.",
            "tip_ta": "சரத்து 371D: ஆந்திரா & தெலங்கானாவில் உள்ள மண்டலங்களில் கல்வி மற்றும் அரசு வேலைவாய்ப்பில் சம வாய்ப்புகள்.",
            "fact_en": "By the Andhra Pradesh Reorganisation Act 2014, Article 371D applies to both Andhra Pradesh and Telangana.",
            "fact_ta": "2014 ஆந்திரப் பிரதேச மறுசீரமைப்புச் சட்டத்தின் மூலம் சரத்து 371D ஆந்திரா மற்றும் தெலங்கானா ஆகிய இரு மாநிலங்களுக்கும் பொருந்தும்."
        },
        # 10
        {
            "subtopic": "Article 371E Central University",
            "stem_en": "What specific provision is established under Article 371E of the Constitution of India?",
            "stem_ta": "இந்திய அரசியலமைப்பின் சரத்து 371E-ன் கீழ் என்ன குறிப்பிட்ட ஏற்பாடு செய்யப்பட்டுள்ளது?",
            "options": [
                ("Establishment of a Central University in Andhra Pradesh", "ஆந்திரப் பிரதேசத்தில் ஒரு மத்தியப் பல்கலைக்கழகத்தை நிறுவுதல்"),
                ("Creation of a High Court in Telangana", "தெலங்கானாவில் ஓர் உயர் நீதிமன்றத்தை உருவாக்குதல்"),
                ("Establishment of an Administrative Tribunal in Goa", "கோவாவில் ஓர் நிர்வாகத் தீர்ப்பாயத்தை நிறுவுதல்"),
                ("Reservation of seats in Sikkim Legislative Assembly", "சிக்கிம் சட்டமன்றத்தில் இட ஒதுக்கீடு வழங்குதல்")
            ],
            "correct_key": "A",
            "exp_en": "Article 371E provides that Parliament may by law provide for the establishment of a Central University in the State of Andhra Pradesh.",
            "exp_ta": "சரத்து 371E, ஆந்திரப் பிரதேச மாநிலத்தில் ஒரு மத்தியப் பல்கலைக்கழகத்தை நிறுவுவதற்கு நாடாளுமன்றம் சட்டத்தின் மூலம் வகைசெய்யலாம் என்று கூறுகிறது.",
            "why_a_en": "Article 371E explicitly provides for the establishment of a Central University in Andhra Pradesh.",
            "why_a_ta": "சரத்து 371E ஆந்திராவில் மத்தியப் பல்கலைக்கழகம் அமைப்பது பற்றி தெளிவாகக் கூறுகிறது.",
            "why_b_en": "High Courts are established under Part VI, Chapter V.",
            "why_b_ta": "உயர் நீதிமன்றங்கள் பகுதி VI, அத்தியாயம் V-ன் கீழ் நிறுவப்படுகின்றன.",
            "why_c_en": "Administrative Tribunals are created under Article 323A.",
            "why_c_ta": "நிர்வாகத் தீர்ப்பாயங்கள் சரத்து 323A-ன் கீழ் உருவாக்கப்படுகின்றன.",
            "why_d_en": "Sikkim Assembly reservation is governed by Article 371F.",
            "why_d_ta": "சிக்கிம் சட்டமன்ற இட ஒதுக்கீடு சரத்து 371F-ன் கீழ் நிர்வகிக்கப்படுகிறது.",
            "tip_en": "Art 371D = Development/Employment in AP & Telangana; Art 371E = Education/Central University in AP.",
            "tip_ta": "சரத்து 371D = ஆந்திரா & தெலங்கானாவில் வேலைவாய்ப்பு; சரத்து 371E = ஆந்திராவில் மத்தியப் பல்கலைக்கழகம்.",
            "fact_en": "Central University of Andhra Pradesh was subsequently established in Ananthapuramu.",
            "fact_ta": "ஆந்திரப் பிரதேச மத்தியப் பல்கலைக்கழகம் பின்னர் அனந்தபுரத்தில் நிறுவப்பட்டது."
        },
        # 11
        {
            "subtopic": "Article 371F Sikkim",
            "stem_en": "Which Constitutional Amendment Act made Sikkim a full-fledged 22nd State of India and inserted Article 371F?",
            "stem_ta": "எந்த அரசியலமைப்புத் திருத்தச் சட்டம் சிக்கிமை இந்தியாவின் 22வது முழு மாநிலமாக மாற்றி, சரத்து 371F-ஐச் சேர்த்தது?",
            "options": [
                ("36th Constitutional Amendment Act, 1975", "36வது அரசியலமைப்புத் திருத்தச் சட்டம், 1975"),
                ("35th Constitutional Amendment Act, 1974", "35வது அரசியலமைப்புத் திருத்தச் சட்டம், 1974"),
                ("38th Constitutional Amendment Act, 1975", "38வது அரசியலமைப்புத் திருத்தச் சட்டம், 1975"),
                ("42nd Constitutional Amendment Act, 1976", "42வது அரசியலமைப்புத் திருத்தச் சட்டம், 1976")
            ],
            "correct_key": "A",
            "exp_en": "The 36th Constitutional Amendment Act, 1975 admitted Sikkim as the 22nd full state of the Indian Union and inserted Article 371F with special provisions.",
            "exp_ta": "1975-ன் 36வது அரசியலமைப்புத் திருத்தச் சட்டம் சிக்கிமை இந்திய ஒன்றியத்தின் 22வது முழு மாநிலமாக இணைத்து, சரத்து 371F-ன் கீழ் சிறப்பு ஏற்பாடுகளைச் சேர்த்தது.",
            "why_a_en": "36th CAA 1975 admitted Sikkim as a full state and added Article 371F.",
            "why_a_ta": "1975-ன் 36வது திருத்தம் சிக்கிமை முழு மாநிலமாக இணைத்து சரத்து 371F-ஐச் சேர்த்தது.",
            "why_b_en": "35th CAA 1974 conferred the status of an 'Associate State' to Sikkim (Article 2A and 10th Schedule, later repealed).",
            "why_b_ta": "35வது திருத்தம் 1974 சிக்கிமிற்கு 'இணை மாநில' அந்தஸ்தை வழங்கியது (பின்னர் நீக்கப்பட்டது).",
            "why_c_en": "38th CAA 1975 dealt with powers of the President/Governor to declare ordinances and emergencies non-justiciable.",
            "why_c_ta": "38வது திருத்தம் அவசரச்சட்டம் மற்றும் அவசரகால பிரகடனம் தொடர்பான நீதிமன்ற அதிகார வரம்பைக் கையாண்டது.",
            "why_d_en": "42nd CAA 1976 made extensive omnibus amendments across the Constitution.",
            "why_d_ta": "42வது திருத்தம் அரசியலமைப்பு முழுவதும் விரிவான திருத்தங்களைச் செய்தது.",
            "tip_en": "Sikkim evolution: 35th CAA 1974 (Associate State) -> 36th CAA 1975 (Full 22nd State under Art 371F).",
            "tip_ta": "சிக்கிம் வளர்ச்சி: 35வது திருத்தம் 1974 (இணை மாநிலம்) -> 36வது திருத்தம் 1975 (சரத்து 371F-ன் கீழ் 22வது முழு மாநிலம்).",
            "fact_en": "Article 371F provides that the Legislative Assembly of Sikkim shall consist of not less than 30 members.",
            "fact_ta": "சரத்து 371F சிக்கிம் சட்டமன்றம் 30 உறுப்பினர்களுக்குக் குறையாமல் இருக்க வேண்டும் என்று கூறுகிறது."
        },
        # 12
        {
            "subtopic": "Article 371F Sikkim",
            "stem_en": "Under Article 371F(a), what is the minimum constitutionally prescribed strength of the Legislative Assembly of Sikkim?",
            "stem_ta": "சரத்து 371F(a)-ன் படி, சிக்கிம் சட்டமன்றத்தின் குறைந்தபட்ச அரசியலமைப்பு பலம் என்ன?",
            "options": [
                ("30 members", "30 உறுப்பினர்கள்"),
                ("40 members", "40 உறுப்பினர்கள்"),
                ("50 members", "50 உறுப்பினர்கள்"),
                ("60 members", "60 உறுப்பினர்கள்")
            ],
            "correct_key": "A",
            "exp_en": "Article 371F(a) provides that the Legislative Assembly of the State of Sikkim shall consist of not less than thirty members, which is an exception to the standard minimum of 60 members under Article 170.",
            "exp_ta": "சரத்து 371F(a) சிக்கிம் சட்டமன்றம் 30 உறுப்பினர்களுக்குக் குறையாமல் இருக்க வேண்டும் என்று கூறுகிறது. இது சரத்து 170-ன் பொதுவான குறைந்தபட்ச 60 உறுப்பினர்கள் விதிக்கு ஒரு விதிவிலக்காகும்.",
            "why_a_en": "Article 371F(a) specifies not less than 30 members for Sikkim.",
            "why_a_ta": "சரத்து 371F(a) சிக்கிமிற்கு 30 உறுப்பினர்களுக்குக் குறையாமல் இருக்க வேண்டும் எனக் கூறுகிறது.",
            "why_b_en": "40 members is the minimum for Goa and Mizoram under Arts 371I and 371G.",
            "why_b_ta": "40 உறுப்பினர்கள் என்பது சரத்துகள் 371I மற்றும் 371G-ன் கீழ் கோவா மற்றும் மிசோரமிற்கான குறைந்தபட்ச பலமாகும்.",
            "why_c_en": "50 members is not a prescribed constitutional threshold for state assemblies.",
            "why_c_ta": "50 உறுப்பினர்கள் என்பது மாநில சட்டமன்றங்களுக்கு நிர்ணயிக்கப்பட்ட வரம்பு அல்ல.",
            "why_d_en": "60 members is the standard minimum under Article 170(1) for normal states.",
            "why_d_ta": "60 உறுப்பினர்கள் என்பது சரத்து 170(1)-ன் கீழ் சாதாரண மாநிலங்களுக்கான குறைந்தபட்ச அளவாகும்.",
            "tip_en": "Assembly minimums: Sikkim (30), Goa (40), Mizoram (40), Puducherry UT (30). General rule under Art 170 is 60-500.",
            "tip_ta": "சட்டமன்ற குறைந்தபட்ச அளவுகள்: சிக்கிம் (30), கோவா (40), மிசோரம் (40), புதுச்சேரி (30). சரத்து 170 பொது விதி 60-500 ஆகும்.",
            "fact_en": "Sikkim currently has 32 Assembly constituencies, including 1 seat reserved for the Buddhist Sangha.",
            "fact_ta": "சிக்கிமில் தற்போது 32 சட்டமன்றத் தொகுதிகள் உள்ளன, இதில் பௌத்த சங்கத்திற்கு 1 இடம் ஒதுக்கப்பட்டுள்ளது."
        },
        # 13
        {
            "subtopic": "Article 371G Mizoram",
            "stem_en": "Which Constitutional Amendment Act inserted Article 371G providing special protections to Mizoram?",
            "stem_ta": "மிசோரமிற்கு சிறப்புப் பாதுகாப்புகளை வழங்கும் சரத்து 371G-ஐ எந்த அரசியலமைப்புத் திருத்தச் சட்டம் சேர்த்தது?",
            "options": [
                ("53rd Constitutional Amendment Act, 1986", "53வது அரசியலமைப்புத் திருத்தச் சட்டம், 1986"),
                ("55th Constitutional Amendment Act, 1986", "55வது அரசியலமைப்புத் திருத்தச் சட்டம், 1986"),
                ("56th Constitutional Amendment Act, 1987", "56வது அரசியலமைப்புத் திருத்தச் சட்டம், 1987"),
                ("98th Constitutional Amendment Act, 2012", "98வது அரசியலமைப்புத் திருத்தச் சட்டம், 2012")
            ],
            "correct_key": "A",
            "exp_en": "The 53rd Constitutional Amendment Act, 1986 inserted Article 371G following the historic Mizo Accord (1986), making Mizoram the 23rd State of India.",
            "exp_ta": "வரலாற்று சிறப்புமிக்க மிசோரம் அமைதி ஒப்பந்தத்தைத் (1986) தொடர்ந்து, 1986-ன் 53வது அரசியலமைப்புத் திருத்தச் சட்டம் சரத்து 371G-ஐ சேர்த்து மிசோரமை இந்தியாவின் 23வது மாநிலமாக்கியது.",
            "why_a_en": "53rd CAA 1986 inserted Article 371G for Mizoram.",
            "why_a_ta": "1986-ன் 53வது திருத்தம் மிசோரமிற்காக சரத்து 371G-ஐச் சேர்த்தது.",
            "why_b_en": "55th CAA 1986 inserted Article 371H for Arunachal Pradesh.",
            "why_b_ta": "1986-ன் 55வது திருத்தம் அருணாச்சலப் பிரதேசத்திற்காக சரத்து 371H-ஐச் சேர்த்தது.",
            "why_c_en": "56th CAA 1987 inserted Article 371I for Goa.",
            "why_c_ta": "1987-ன் 56வது திருத்தம் கோவாவிற்காக சரத்து 371I-ஐச் சேர்த்தது.",
            "why_d_en": "98th CAA 2012 inserted Article 371J for Karnataka.",
            "why_d_ta": "2012-ன் 98வது திருத்தம் கர்நாடகாவிற்காக சரத்து 371J-ஐச் சேர்த்தது.",
            "tip_en": "Article 371G guarantees that central laws on Mizo customary law, religion, civil/criminal procedures, and land do not apply without State Assembly resolution.",
            "tip_ta": "சரத்து 371G மிசோரம் சட்டமன்றத் தீர்மானமின்றி மிசோ மரபுச் சட்டம், மதம் மற்றும் நிலம் தொடர்பான மத்திய சட்டங்கள் பொருந்தாது என்பதை உறுதி செய்கிறது.",
            "fact_en": "Under Article 371G, the Legislative Assembly of Mizoram shall consist of not less than 40 members.",
            "fact_ta": "சரத்து 371G-ன் படி மிசோரம் சட்டமன்றம் 40 உறுப்பினர்களுக்குக் குறையாமல் இருக்க வேண்டும்."
        },
        # 14
        {
            "subtopic": "Article 371H Arunachal Pradesh",
            "stem_en": "What special responsibility is conferred upon the Governor of Arunachal Pradesh under Article 371H?",
            "stem_ta": "சரத்து 371H-ன் கீழ் அருணாச்சலப் பிரதேச ஆளுநருக்கு என்ன சிறப்புப் பொறுப்பு வழங்கப்பட்டுள்ளது?",
            "options": [
                ("Special responsibility with respect to law and order", "சட்டம் மற்றும் ஒழுங்கு தொடர்பான சிறப்புப் பொறுப்பு"),
                ("Establishment of development board for Tawang", "தவாங்கிற்கு வளர்ச்சி வாரியம் அமைத்தல்"),
                ("Appointment of Central University Vice Chancellor", "மத்தியப் பல்கலைக்கழக துணைவேந்தரை நியமித்தல்"),
                ("Sole power to delimit municipal wards", "நகராட்சி வார்டுகளை மறுவரையறை செய்வதற்கான தனி அதிகாரம்")
            ],
            "correct_key": "A",
            "exp_en": "Article 371H provides that the Governor of Arunachal Pradesh shall have special responsibility with respect to law and order in the State, exercising his individual judgment after consulting the Council of Ministers.",
            "exp_ta": "சரத்து 371H அருணாச்சலப் பிரதேச ஆளுநருக்கு மாநிலத்தில் சட்டம் மற்றும் ஒழுங்கு தொடர்பாக சிறப்புப் பொறுப்பை வழங்குகிறது. அவர் அமைச்சரவையைக் கலந்தாலோசித்த பிறகு தனது தனிப்பட்ட முடிவைப் பயன்படுத்தலாம்.",
            "why_a_en": "Article 371H explicitly gives the Governor special responsibility for law and order.",
            "why_a_ta": "சரத்து 371H ஆளுநருக்கு சட்டம் ஒழுங்கு தொடர்பான சிறப்புப் பொறுப்பை தெளிவாக வழங்குகிறது.",
            "why_b_en": "There is no Tawang development board provision in Article 371H.",
            "why_b_ta": "சரத்து 371H-ல் தவாங் வளர்ச்சி வாரிய ஏற்பாடு எதுவும் இல்லை.",
            "why_c_en": "Central University VC appointments are statutory, not under Art 371H.",
            "why_c_ta": "மத்தியப் பல்கலைக்கழக துணைவேந்தர் நியமனம் சட்டப்பூர்வமானது, சரத்து 371H-ன் கீழானது அல்ல.",
            "why_d_en": "Ward delimitation is governed by State Election Commission and municipal laws.",
            "why_d_ta": "வார்டு மறுவரையறை மாநிலத் தேர்தல் ஆணையம் மற்றும் நகராட்சிச் சட்டங்களால் நிர்வகிக்கப்படுகிறது.",
            "tip_en": "Arunachal Pradesh became the 24th State via the 55th Constitutional Amendment Act 1986.",
            "tip_ta": "1986-ன் 55வது அரசியலமைப்புத் திருத்தச் சட்டம் மூலம் அருணாச்சலப் பிரதேசம் 24வது மாநிலமானது.",
            "fact_en": "The Governor's special power ceases when the President, on receipt of a report or otherwise, directs so by order.",
            "fact_ta": "குடியரசுத் தலைவர் ஓர் உத்தரவின் மூலம் নির্দেশிக்கும்போது ஆளுநரின் இச்சிறப்பு அதிகாரம் முடிவுக்கு வரும்."
        },
        # 15
        {
            "subtopic": "Article 371I Goa",
            "stem_en": "Under Article 371I, inserted by the 56th Constitutional Amendment Act 1987, the Legislative Assembly of Goa shall consist of not less than:",
            "stem_ta": "1987-ன் 56வது அரசியலமைப்புத் திருத்தச் சட்டத்தால் சேர்க்கப்பட்ட சரத்து 371I-ன் படி, கோவா சட்டமன்றம் எத்தனை உறுப்பினர்களுக்குக் குறையாமல் இருக்க வேண்டும்?",
            "options": [
                ("30 members", "30 உறுப்பினர்கள்"),
                ("40 members", "40 உறுப்பினர்கள்"),
                ("50 members", "50 உறுப்பினர்கள்"),
                ("60 members", "60 உறுப்பினர்கள்")
            ],
            "correct_key": "A",
            "exp_en": "Article 371I provides that the Legislative Assembly of the State of Goa shall consist of not less than thirty members. (Note: Goa currently has 40 seats by state enactment).",
            "exp_ta": "சரத்து 371I கோவா மாநில சட்டமன்றம் 30 உறுப்பினர்களுக்குக் குறையாமல் இருக்க வேண்டும் என்று கூறுகிறது. (குறிப்பு: மாநிலச் சட்டத்தின் மூலம் கோவா தற்போது 40 இடங்களைக் கொண்டுள்ளது).",
            "why_a_en": "Article 371I constitutional text explicitly fixes 'not less than thirty members'.",
            "why_a_ta": "சரத்து 371I அரசியலமைப்பு வாசகம் தெளிவாக 'முப்பது உறுப்பினர்களுக்குக் குறையாமல்' என்று குறிப்பிடுகிறது.",
            "why_b_en": "40 is the actual current strength, but the constitutional minimum prescribed in Article 371I is 30.",
            "why_b_ta": "40 என்பது தற்போதைய பலம், ஆனால் சரத்து 371I-ல் கூறப்பட்டுள்ள குறைந்தபட்ச அளவு 30 ஆகும்.",
            "why_c_en": "50 is not the constitutional figure for Goa.",
            "why_c_ta": "50 என்பது கோவாவிற்கான அரசியலமைப்பு எண்ணிக்கை அல்ல.",
            "why_d_en": "60 is the general threshold under Art 170, which Art 371I carves an exception from.",
            "why_d_ta": "60 என்பது சரத்து 170-ன் பொது வரம்பு, சரத்து 371I இதிலிருந்து விலக்களிக்கிறது.",
            "tip_en": "Goa attained statehood on 30 May 1987 via 56th CAA 1987; Daman & Diu remained a Union Territory.",
            "tip_ta": "56வது திருத்தம் 1987 மூலம் 1987 மே 30 அன்று கோவா மாநில அந்தஸ்தைப் பெற்றது; டாமன் & டையூ யூனியன் பிரதேசமாக நீடித்தது.",
            "fact_en": "Sikkim (Art 371F) and Goa (Art 371I) both have a constitutional floor of not less than 30 members.",
            "fact_ta": "சிக்கிம் (சரத்து 371F) மற்றும் கோவா (சரத்து 371I) இரண்டும் 30 உறுப்பினர்களுக்குக் குறையாத அரசியலமைப்பு வரம்பைக் கொண்டுள்ளன."
        },
        # 16
        {
            "subtopic": "Article 371J Karnataka",
            "stem_en": "Article 371J was inserted by which Constitutional Amendment Act to provide special provisions for the Hyderabad-Karnataka region?",
            "stem_ta": "ஹைதராபாத்-கர்நாடகா பகுதிக்கு சிறப்பு ஏற்பாடுகளை வழங்க எந்த அரசியலமைப்புத் திருத்தச் சட்டம் மூலம் சரத்து 371J சேர்க்கப்பட்டது?",
            "options": [
                ("98th Constitutional Amendment Act, 2012", "98வது அரசியலமைப்புத் திருத்தச் சட்டம், 2012"),
                ("91st Constitutional Amendment Act, 2003", "91வது அரசியலமைப்புத் திருத்தச் சட்டம், 2003"),
                ("99th Constitutional Amendment Act, 2014", "99வது அரசியலமைப்புத் திருத்தச் சட்டம், 2014"),
                ("103rd Constitutional Amendment Act, 2019", "103வது அரசியலமைப்புத் திருத்தச் சட்டம், 2019")
            ],
            "correct_key": "A",
            "exp_en": "Article 371J was inserted by the 98th Constitutional Amendment Act, 2012 to empower the Governor of Karnataka to establish a separate development board for the backward Hyderabad-Karnataka region (now Kalyana-Karnataka).",
            "exp_ta": "பின்தங்கிய ஹைதராபாத்-கர்நாடகா (தற்போது கல்யாண-கர்நாடகா) பகுதிக்கு தனி வளர்ச்சி வாரியத்தை அமைக்க கர்நாடக ஆளுநருக்கு அதிகாரமளிக்க 2012-ன் 98வது அரசியலமைப்புத் திருத்தச் சட்டம் மூலம் சரத்து 371J சேர்க்கப்பட்டது.",
            "why_a_en": "98th CAA 2012 inserted Article 371J.",
            "why_a_ta": "2012-ன் 98வது திருத்தம் சரத்து 371J-ஐச் சேர்த்தது.",
            "why_b_en": "91st CAA 2003 capped ministry size at 15% under Articles 75 and 164.",
            "why_b_ta": "2003-ன் 91வது திருத்தம் அமைச்சரவை அளவை 15% ஆக வரம்பிட்டது.",
            "why_c_en": "99th CAA 2014 established NJAC, later struck down by SC.",
            "why_c_ta": "2014-ன் 99வது திருத்தம் NJAC-ஐ அமைத்தது, பின்னர் உச்ச நீதிமன்றத்தால் ரத்து செய்யப்பட்டது.",
            "why_d_en": "103rd CAA 2019 introduced 10% EWS reservation under Arts 15(6) and 16(6).",
            "why_d_ta": "2019-ன் 103வது திருத்தம் 10% EWS இடஒதுக்கீட்டை அறிமுகப்படுத்தியது.",
            "tip_en": "Article 371J covers six backward districts: Gulbarga, Bidar, Raichur, Koppal, Yadgir, and Bellary.",
            "tip_ta": "சரத்து 371J ஆறு பின்தங்கிய மாவட்டங்களை உள்ளடக்கியது: குல்பர்கா, பீதர், ராய்ச்சூர், கொப்பல், யாத்கிர் மற்றும் பெல்லாரி.",
            "fact_en": "Art 371J provides for reservation in educational institutions and state government jobs for persons hailing from this region.",
            "fact_ta": "சரத்து 371J இப்பகுதியைச் சேர்ந்த நபர்களுக்குக் கல்வி நிறுவனங்கள் மற்றும் அரசு வேலைகளில் இடஒதுக்கீடு வழங்குகிறது."
        },
        # 17
        {
            "subtopic": "Article 371J Karnataka",
            "stem_en": "The Hyderabad-Karnataka region covered under Article 371J was officially renamed by the Karnataka Government as:",
            "stem_ta": "சரத்து 371J-ன் கீழ் உள்ள ஹைதராபாத்-கர்நாடகா பகுதி கர்நாடக அரசால் அதிகாரப்பூர்வமாக எவ்வாறு பெயர் மாற்றப்பட்டது?",
            "options": [
                ("Kalyana-Karnataka", "கல்யாண-கர்நாடகா"),
                ("Karavali-Karnataka", "காரவளி-கர்நாடகா"),
                ("Bayaluseeme", "பயலுசீமே"),
                ("Malenadu", "மலேநாடு")
            ],
            "correct_key": "A",
            "exp_en": "In September 2019, the Karnataka Government officially rechristened the Hyderabad-Karnataka region as 'Kalyana-Karnataka' to remove historical colonial and Nizam associations.",
            "exp_ta": "செப்டம்பர் 2019-ல், கர்நாடக அரசு நிஜாம் கால நினைவுகளை நீக்கும் வகையில் ஹைதராபாத்-கர்நாடகா பகுதியை 'கல்யாண-கர்நாடகா' என அதிகாரப்பூர்வமாகப் பெயர் மாற்றியது.",
            "why_a_en": "Kalyana-Karnataka is the official renamed title.",
            "why_a_ta": "கல்யாண-கர்நாடகா என்பது அதிகாரப்பூர்வ புதிய பெயராகும்.",
            "why_b_en": "Karavali-Karnataka refers to the coastal strip (Udupi, Dakshina Kannada, Uttara Kannada).",
            "why_b_ta": "காரவளி-கர்நாடகா என்பது கடலோரப் பகுதியைக் குறிக்கிறது.",
            "why_c_en": "Bayaluseeme refers to the open plain region of the Deccan plateau in Karnataka.",
            "why_c_ta": "பயலுசீமே என்பது கர்நாடகாவின் தக்காண பீடபூமி சமவெளிப் பகுதியைக் குறிக்கிறது.",
            "why_d_en": "Malenadu refers to the Western Ghats hilly forest tract.",
            "why_d_ta": "மலேநாடு என்பது மேற்குத் தொடர்ச்சி மலைப்பகுதியைக் குறிக்கிறது.",
            "tip_en": "Kalyana-Karnataka celebration day is celebrated annually on 17 September (Liberation Day).",
            "tip_ta": "கல்யாண-கர்நாடக தினக் கொண்டாட்டம் ஆண்டுதோறும் செப்டம்பர் 17 அன்று (விடுதலை நாள்) கொண்டாடப்படுகிறது.",
            "fact_en": "A separate development board under Art 371J allocates dedicated capital expenditure grants annually.",
            "fact_ta": "சரத்து 371J-ன் கீழான தனி வளர்ச்சி வாரியம் ஆண்டுதோறும் மூலதனச் செலவின மானியங்களை ஒதுக்குகிறது."
        },
        # 18
        {
            "subtopic": "Part XVI Certain Classes Architecture",
            "stem_en": "Which Part of the Indian Constitution contains 'Special Provisions Relating to Certain Classes' (Articles 330 to 342A)?",
            "stem_ta": "இந்திய அரசியலமைப்பின் எந்தப் பகுதி 'குறிப்பிட்ட வகுப்பினருக்கான சிறப்பு ஏற்பாடுகள்' (சரத்துகள் 330 முதல் 342A வரை) பற்றிக் கூறுகிறது?",
            "options": [
                ("Part XVI", "பகுதி XVI"),
                ("Part XV", "பகுதி XV"),
                ("Part XIV", "பகுதி XIV"),
                ("Part XVII", "பகுதி XVII")
            ],
            "correct_key": "A",
            "exp_en": "Part XVI (Articles 330 to 342A) is titled 'Special Provisions Relating to Certain Classes', providing for reservations and special representation for SCs, STs, and backward classes.",
            "exp_ta": "பகுதி XVI (சரத்துகள் 330 முதல் 342A வரை) 'குறிப்பிட்ட வகுப்பினருக்கான சிறப்பு ஏற்பாடுகள்' என்று தலைப்பிடப்பட்டு, SC, ST மற்றும் பிற்படுத்தப்பட்ட வகுப்பினருக்கான இடஒதுக்கீடு மற்றும் சிறப்புப் பிரதிநிதித்துவத்தை வழங்குகிறது.",
            "why_a_en": "Part XVI contains Articles 330 to 342A.",
            "why_a_ta": "பகுதி XVI சரத்துகள் 330 முதல் 342A வரை கொண்டுள்ளது.",
            "why_b_en": "Part XV deals with Elections (Articles 324-329A).",
            "why_b_ta": "பகுதி XV தேர்தல்களைக் (சரத்துகள் 324-329A) கையாள்கிறது.",
            "why_c_en": "Part XIV deals with Services under the Union and the States (Articles 308-323).",
            "why_c_ta": "பகுதி XIV ஒன்றியம் மற்றும் மாநிலங்களின் கீழான பணிகளைக் கையாள்கிறது.",
            "why_d_en": "Part XVII deals with Official Language (Articles 343-351).",
            "why_d_ta": "பகுதி XVII அதிகாரப்பூர்வ மொழியைக் (சரத்துகள் 343-351) கையாள்கிறது.",
            "tip_en": "Part XVI = Certain Classes (330-342A); Part XXI = Special Provisions for States (369-392). Do not confuse the two!",
            "tip_ta": "பகுதி XVI = குறிப்பிட்ட வகுப்பினர் (330-342A); பகுதி XXI = மாநிலங்களுக்கான சிறப்பு ஏற்பாடுகள் (369-392). இரண்டையும் குழப்பிக் கொள்ளாதீர்கள்!",
            "fact_en": "Part XVI bridges affirmative action principles with political representation in legislative bodies.",
            "fact_ta": "பகுதி XVI ஆக்கப்பூர்வ நடவடிக்கை கொள்கைகளை சட்டமன்ற அமைப்புகளில் அரசியல் பிரதிநிதித்துவத்துடன் இணைக்கிறது."
        },
        # 19
        {
            "subtopic": "Article 330 Lok Sabha Reservation",
            "stem_en": "Under Article 330 of the Constitution of India, seats are reserved in the Lok Sabha for:",
            "stem_ta": "இந்திய அரசியலமைப்பின் சரத்து 330-ன் கீழ், மக்களவையில் யாருக்கு இடங்கள் ஒதுக்கப்பட்டுள்ளன?",
            "options": [
                ("The Scheduled Castes and the Scheduled Tribes", "பட்டியலிடப்பட்ட சாதியினர் மற்றும் பட்டியலிடப்பட்ட பழங்குடியினர்"),
                ("Socially and Educationally Backward Classes (OBCs)", "சமூக மற்றும் கல்வி ரீதியாக பிற்படுத்தப்பட்ட வகுப்பினர் (OBC)"),
                ("Economically Weaker Sections (EWS)", "பொருளாதாரத்தில் நலிவடைந்த பிரிவினர் (EWS)"),
                ("Religious Minorities", "மத சிறுபான்மையினர்")
            ],
            "correct_key": "A",
            "exp_en": "Article 330 mandates reservation of seats in the House of the People (Lok Sabha) for the Scheduled Castes and the Scheduled Tribes in proportion to their population in each State/UT.",
            "exp_ta": "சரத்து 330, ஒவ்வொரு மாநிலம்/யூனியன் பிரதேசத்திலும் உள்ள மக்கள் தொகைக்கு ஏற்ப, மக்களவையில் பட்டியலிடப்பட்ட சாதியினர் மற்றும் பழங்குடியினருக்கு இட ஒதுக்கீட்டை கட்டாயமாக்குகிறது.",
            "why_a_en": "Article 330 provides reservation strictly for SCs and STs in the Lok Sabha.",
            "why_a_ta": "சரத்து 330 மக்களவையில் SC மற்றும் ST பிரிவினருக்கு மட்டுமே இடஒதுக்கீட்டை வழங்குகிறது.",
            "why_b_en": "There is no political reservation for OBCs in Parliament or State Legislative Assemblies.",
            "why_b_ta": "நாடாளுமன்றம் அல்லது மாநில சட்டமன்றங்களில் OBC-களுக்கு அரசியல் இடஒதுக்கீடு இல்லை.",
            "why_c_en": "EWS reservation is for admissions and employment (Arts 15(6) & 16(6)), not for legislative seats.",
            "why_c_ta": "EWS இடஒதுக்கீடு கல்வி மற்றும் வேலைவாய்ப்பிற்கு மட்டுமே, சட்டமன்ற இடங்களுக்கு அல்ல.",
            "why_d_en": "The Indian Constitution does not provide legislative seat reservations based on religion.",
            "why_d_ta": "இந்திய அரசியலமைப்பு மத அடிப்படையில் சட்டமன்ற இட ஒதுக்கீட்டை வழங்கவில்லை.",
            "tip_en": "Currently in the Lok Sabha: 84 seats are reserved for SCs and 47 seats are reserved for STs (Total = 131 reserved seats out of 543).",
            "tip_ta": "மக்களவையில் தற்போது: SC-க்கு 84 இடங்களும், ST-க்கு 47 இடங்களும் ஒதுக்கப்பட்டுள்ளன (543-ல் மொத்தம் 131 இடங்கள்).",
            "fact_en": "Delimitation Commission fixes the specific SC/ST reserved constituencies based on census population concentrations.",
            "fact_ta": "தொகுதி மறுவரையறை ஆணையம் மக்கள் தொகை அடிப்படையில் குறிப்பிட்ட SC/ST தொகுதிகளை நிர்ணயிக்கிறது."
        },
        # 20
        {
            "subtopic": "Article 332 Legislative Assembly Reservation",
            "stem_en": "Which Article of the Constitution provides for the reservation of seats for Scheduled Castes and Scheduled Tribes in the Legislative Assemblies of the States?",
            "stem_ta": "மாநில சட்டமன்றங்களில் பட்டியலிடப்பட்ட சாதியினர் மற்றும் பழங்குடியினருக்கு இட ஒதுக்கீட்டை வழங்கும் அரசியலமைப்புச் சரத்து எது?",
            "options": [
                ("Article 332", "சரத்து 332"),
                ("Article 330", "சரத்து 330"),
                ("Article 331", "சரத்து 331"),
                ("Article 333", "சரத்து 333")
            ],
            "correct_key": "A",
            "exp_en": "Article 332 mandates the reservation of seats for Scheduled Castes and Scheduled Tribes in the Legislative Assembly of every State based on population ratio.",
            "exp_ta": "சரத்து 332 மக்கள் தொகை விகிதத்தின் அடிப்படையில் ஒவ்வொரு மாநில சட்டமன்றத்திலும் பட்டியலிடப்பட்ட சாதியினர் மற்றும் பழங்குடியினருக்கு இட ஒதுக்கீட்டை வழங்குகிறது.",
            "why_a_en": "Article 332 governs SC/ST reservations in State Legislative Assemblies.",
            "why_a_ta": "சரத்து 332 மாநில சட்டமன்றங்களில் SC/ST இடஒதுக்கீட்டை நிர்வகிக்கிறது.",
            "why_b_en": "Article 330 governs SC/ST reservations in the Lok Sabha.",
            "why_b_ta": "சரத்து 330 மக்களவையில் SC/ST இடஒதுக்கீட்டை நிர்வகிக்கிறது.",
            "why_c_en": "Article 331 dealt with Anglo-Indian representation in the Lok Sabha.",
            "why_c_ta": "சரத்து 331 மக்களவையில் ஆங்கிலோ-இந்தியப் பிரதிநிதித்துவத்தைக் கையாண்டது.",
            "why_d_en": "Article 333 dealt with Anglo-Indian representation in State Legislative Assemblies.",
            "why_d_ta": "சரத்து 333 மாநில சட்டமன்றங்களில் ஆங்கிலோ-இந்தியப் பிரதிநிதித்துவத்தைக் கையாண்டது.",
            "tip_en": "Article 330 = Lok Sabha SC/ST; Article 332 = State Legislative Assembly SC/ST.",
            "tip_ta": "சரத்து 330 = மக்களவை SC/ST; சரத்து 332 = மாநில சட்டமன்றம் SC/ST.",
            "fact_en": "In Tamil Nadu Legislative Assembly (234 seats), 44 seats are reserved for SCs and 2 seats for STs.",
            "fact_ta": "தமிழ்நாடு சட்டமன்றத்தில் (234 இடங்கள்), 44 இடங்கள் SC-க்கும் 2 இடங்கள் ST-க்கும் ஒதுக்கப்பட்டுள்ளன."
        },
        # 21
        {
            "subtopic": "104th Constitutional Amendment Act",
            "stem_en": "The 104th Constitutional Amendment Act, 2019 extended the reservation of seats for SCs and STs in the Lok Sabha and State Assemblies until:",
            "stem_ta": "104வது அரசியலமைப்புத் திருத்தச் சட்டம், 2019 மக்களவை மற்றும் மாநில சட்டமன்றங்களில் SC மற்றும் ST பிரிவினருக்கான இட ஒதுக்கீட்டை எந்த ஆண்டு வரை நீட்டித்தது?",
            "options": [
                ("25 January 2030", "25 ஜனவரி 2030"),
                ("26 January 2025", "26 ஜனவரி 2025"),
                ("15 August 2035", "15 ஆகஸ்ட் 2035"),
                ("31 December 2040", "31 டிசம்பர் 2040")
            ],
            "correct_key": "A",
            "exp_en": "The 104th Constitutional Amendment Act, 2019 amended Article 334 to extend the reservation of seats for SCs and STs in the Lok Sabha and State Assemblies for an additional ten years, up to 25 January 2030.",
            "exp_ta": "104வது அரசியலமைப்புத் திருத்தச் சட்டம் 2019, சரத்து 334-ஐத் திருத்தி மக்களவை மற்றும் மாநில சட்டமன்றங்களில் SC/ST இடஒதுக்கீட்டை மேலும் 10 ஆண்டுகளுக்கு, அதாவது 2030 ஜனவரி 25 வரை நீட்டித்தது.",
            "why_a_en": "104th CAA extended SC/ST political reservation up to 25 January 2030.",
            "why_a_ta": "104வது திருத்தம் SC/ST அரசியல் இடஒதுக்கீட்டை 2030 ஜனவரி 25 வரை நீட்டித்தது.",
            "why_b_en": "2025 was not the deadline set by the 104th Amendment.",
            "why_b_ta": "2025 என்பது 104வது திருத்தத்தால் நிர்ணயிக்கப்பட்ட காலக்கெடு அல்ல.",
            "why_c_en": "2035 is an arbitrary future year.",
            "why_c_ta": "2035 என்பது தவறான எதிர்கால ஆண்டு.",
            "why_d_en": "2040 is incorrect.",
            "why_d_ta": "2040 என்பது தவறானது.",
            "tip_en": "Originally Article 334 set political reservation for 10 years (up to 1960). It has been extended every 10 years by successive amendments (8th, 23rd, 45th, 62nd, 79th, 95th, and 104th).",
            "tip_ta": "முதலில் சரத்து 334 அரசியல் இடஒதுக்கீட்டை 10 ஆண்டுகளுக்கு மட்டுமே (1960 வரை) நிர்ணயித்தது. அது ஒவ்வொரு 10 ஆண்டுகளுக்கும் திருத்தங்கள் மூலம் நீட்டிக்கப்பட்டு வந்துள்ளது.",
            "fact_en": "The 104th Amendment also chose NOT to extend the nomination of Anglo-Indian members, effectively ending it.",
            "fact_ta": "104வது திருத்தம் ஆங்கிலோ-இந்திய உறுப்பினர்களின் நியமனத்தை நீட்டிக்காமல் அதை முடிவுக்குக் கொண்டுவந்தது."
        },
        # 22
        {
            "subtopic": "Anglo-Indian Nomination Discontinuation",
            "stem_en": "Which Constitutional Amendment discontinued the reservation of seats by nomination for the Anglo-Indian community in the Lok Sabha and State Assemblies?",
            "stem_ta": "மக்களவை மற்றும் மாநில சட்டமன்றங்களில் ஆங்கிலோ-இந்திய சமூகத்தினருக்கான நியமன இட ஒதுக்கீட்டை நிறுத்திய அரசியலமைப்புத் திருத்தம் எது?",
            "options": [
                ("104th Constitutional Amendment Act, 2019", "104வது அரசியலமைப்புத் திருத்தச் சட்டம், 2019"),
                ("102nd Constitutional Amendment Act, 2018", "102வது அரசியலமைப்புத் திருத்தச் சட்டம், 2018"),
                ("103rd Constitutional Amendment Act, 2019", "103வது அரசியலமைப்புத் திருத்தச் சட்டம், 2019"),
                ("101st Constitutional Amendment Act, 2016", "101வது அரசியலமைப்புத் திருத்தச் சட்டம், 2016")
            ],
            "correct_key": "A",
            "exp_en": "The 104th Constitutional Amendment Act, 2019 discontinued the provision for nomination of Anglo-Indians to the Lok Sabha (under Article 331) and State Legislative Assemblies (under Article 333) by not renewing it beyond 25 January 2020.",
            "exp_ta": "104வது அரசியலமைப்புத் திருத்தச் சட்டம் 2019, 2020 ஜனவரி 25-க்கு மேல் புதுப்பிக்காமல் விட்டதன் மூலம் மக்களவை (சரத்து 331) மற்றும் மாநில சட்டமன்றங்களில் (சரத்து 333) ஆங்கிலோ-இந்திய நியமன முறையை முடிவுக்குக் கொண்டுவந்தது.",
            "why_a_en": "104th CAA 2019 discontinued Anglo-Indian nominated seats.",
            "why_a_ta": "104வது திருத்தம் 2019 ஆங்கிலோ-இந்திய நியமன இடங்களை நிறுத்தியது.",
            "why_b_en": "102nd CAA 2018 granted constitutional status to NCBC.",
            "why_b_ta": "102வது திருத்தம் 2018 NCBC-க்கு அரசியலமைப்பு அந்தஸ்தை வழங்கியது.",
            "why_c_en": "103rd CAA 2019 introduced 10% EWS reservation.",
            "why_c_ta": "103வது திருத்தம் 2019 10% EWS இடஒதுக்கீட்டை அறிமுகப்படுத்தியது.",
            "why_d_en": "101st CAA 2016 introduced the Goods and Services Tax (GST).",
            "why_d_ta": "101வது திருத்தம் 2016 சரக்கு மற்றும் சேவை வரியை (GST) அறிமுகப்படுத்தியது.",
            "tip_en": "Under former Art 331, President could nominate up to 2 Anglo-Indians to Lok Sabha; under Art 333, Governor could nominate 1 to Assembly.",
            "tip_ta": "முந்தைய சரத்து 331-ன் கீழ் குடியரசுத் தலைவர் 2 பேரையும், சரத்து 333-ன் கீழ் ஆளுநர் 1 பேரையும் நியமிக்கலாம்.",
            "fact_en": "As a result of the 104th CAA, the maximum strength of the Lok Sabha dropped from 552 to 550.",
            "fact_ta": "104வது திருத்தத்தின் விளைவாக மக்களவையின் அதிகபட்ச பலம் 552-லிருந்து 550 ஆகக் குறைந்தது."
        },
        # 23
        {
            "subtopic": "Article 338 NCSC",
            "stem_en": "The National Commission for Scheduled Castes is established as a constitutional body under which Article of the Constitution?",
            "stem_ta": "பட்டியலிடப்பட்ட சாதியினருக்கான தேசிய ஆணையம் (NCSC) எந்த அரசியலமைப்புச் சரத்தின் கீழ் ஓர் அரசியலமைப்பு அமைப்பாக நிறுவப்பட்டுள்ளது?",
            "options": [
                ("Article 338", "சரத்து 338"),
                ("Article 338A", "சரத்து 338A"),
                ("Article 338B", "சரத்து 338B"),
                ("Article 340", "சரத்து 340")
            ],
            "correct_key": "A",
            "exp_en": "Article 338 of the Constitution of India provides for the establishment of the National Commission for Scheduled Castes (NCSC) to investigate and monitor all matters relating to safeguards provided for SCs.",
            "exp_ta": "இந்திய அரசியலமைப்பின் சரத்து 338, SC பிரிவினருக்கு வழங்கப்பட்டுள்ள பாதுகாப்புகள் தொடர்பான அனைத்து விவகாரங்களையும் கண்காணிக்கவும் விசாரிக்கவும் பட்டியலிடப்பட்ட சாதியினருக்கான தேசிய ஆணையத்தை (NCSC) அமைக்கிறது.",
            "why_a_en": "Article 338 establishes the National Commission for Scheduled Castes.",
            "why_a_ta": "சரத்து 338 பட்டியலிடப்பட்ட சாதியினருக்கான தேசிய ஆணையத்தை அமைக்கிறது.",
            "why_b_en": "Article 338A establishes the National Commission for Scheduled Tribes (NCST).",
            "why_b_ta": "சரத்து 338A பட்டியலிடப்பட்ட பழங்குடியினருக்கான தேசிய ஆணையத்தை (NCST) அமைக்கிறது.",
            "why_c_en": "Article 338B establishes the National Commission for Backward Classes (NCBC).",
            "why_c_ta": "சரத்து 338B பிற்படுத்தப்பட்ட வகுப்பினருக்கான தேசிய ஆணையத்தை (NCBC) அமைக்கிறது.",
            "why_d_en": "Article 340 provides for the appointment of a Commission to investigate the conditions of backward classes.",
            "why_d_ta": "சரத்து 340 பிற்படுத்தப்பட்ட வகுப்பினரின் நிலையை ஆராய ஆணையம் நியமிப்பது பற்றிக் கூறுகிறது.",
            "tip_en": "Articles triad: 338 = NCSC; 338A = NCST; 338B = NCBC.",
            "tip_ta": "மூன்று சரத்துகள்: 338 = NCSC; 338A = NCST; 338B = NCBC.",
            "fact_en": "Originally a single Special Officer under Art 338 was replaced by a multimember commission by the 65th CAA 1990.",
            "fact_ta": "முதலில் சரத்து 338-ன் கீழ் இருந்த சிறப்பு அதிகாரி முறை 1990-ன் 65வது திருத்தத்தால் பல உறுப்பினர் ஆணையமாக மாற்றப்பட்டது."
        },
        # 24
        {
            "subtopic": "Article 338A NCST",
            "stem_en": "Which Constitutional Amendment Act bifurcated the combined National Commission into separate NCSC (Article 338) and NCST (Article 338A)?",
            "stem_ta": "எந்த அரசியலமைப்புத் திருத்தச் சட்டம் ஒருங்கிணைந்த தேசிய ஆணையத்தைப் பிரித்து, தனித்தனியாக NCSC (சரத்து 338) மற்றும் NCST (சரத்து 338A) என உருவாக்கியது?",
            "options": [
                ("89th Constitutional Amendment Act, 2003", "89வது அரசியலமைப்புத் திருத்தச் சட்டம், 2003"),
                ("65th Constitutional Amendment Act, 1990", "65வது அரசியலமைப்புத் திருத்தச் சட்டம், 1990"),
                ("92nd Constitutional Amendment Act, 2003", "92வது அரசியலமைப்புத் திருத்தச் சட்டம், 2003"),
                ("102nd Constitutional Amendment Act, 2018", "102வது அரசியலமைப்புத் திருத்தச் சட்டம், 2018")
            ],
            "correct_key": "A",
            "exp_en": "The 89th Constitutional Amendment Act, 2003 bifurcated the combined National Commission for SCs and STs into two separate bodies: NCSC under Article 338 and NCST under the newly inserted Article 338A, effective from 2004.",
            "exp_ta": "2003-ன் 89வது அரசியலமைப்புத் திருத்தச் சட்டம் ஒருங்கிணைந்த ஆணையத்தைப் பிரித்து, சரத்து 338-ன் கீழ் NCSC மற்றும் புதிதாகச் சேர்க்கப்பட்ட சரத்து 338A-ன் கீழ் NCST என இரு தனி அமைப்புகளை 2004 முதல் உருவாக்கியது.",
            "why_a_en": "89th CAA 2003 created NCST under Article 338A.",
            "why_a_ta": "2003-ன் 89வது திருத்தம் சரத்து 338A-ன் கீழ் NCST-ஐ உருவாக்கியது.",
            "why_b_en": "65th CAA 1990 created the combined multimember Commission for SCs & STs.",
            "why_b_ta": "1990-ன் 65வது திருத்தம் SC மற்றும் ST-க்கான ஒருங்கிணைந்த ஆணையத்தை உருவாக்கியது.",
            "why_c_en": "92nd CAA 2003 added Bodo, Dogri, Maithili, and Santhali to the Eighth Schedule.",
            "why_c_ta": "2003-ன் 92வது திருத்தம் எட்டாவது அட்டவணையில் 4 மொழிகளைச் சேர்த்தது.",
            "why_d_en": "102nd CAA 2018 gave constitutional status to NCBC under Article 338B.",
            "why_d_ta": "2018-ன் 102வது திருத்தம் NCBC-க்கு சரத்து 338B-ன் கீழ் அரசியலமைப்பு அந்தஸ்து வழங்கியது.",
            "tip_en": "NCST consists of a Chairperson, a Vice-Chairperson, and 3 other Members appointed by the President by warrant under his hand and seal.",
            "tip_ta": "NCST தலைவர், துணைத் தலைவர் மற்றும் 3 உறுப்பினர்களைக் கொண்டுள்ளது; இவர்கள் குடியரசுத் தலைவரால் நியமிக்கப்படுகின்றனர்.",
            "fact_en": "At least one member of NCST must be a woman.",
            "fact_ta": "NCST-ல் குறைந்தது ஒரு பெண் உறுப்பினராவது இடம்பெற வேண்டும்."
        },
        # 25
        {
            "subtopic": "Article 338B NCBC",
            "stem_en": "The National Commission for Backward Classes (NCBC) was accorded constitutional status under Article 338B by which Amendment Act?",
            "stem_ta": "எந்த அரசியலமைப்புத் திருத்தச் சட்டம் மூலம் சரத்து 338B-ன் கீழ் பிற்படுத்தப்பட்ட வகுப்பினருக்கான தேசிய ஆணையத்திற்கு (NCBC) அரசியலமைப்பு அந்தஸ்து வழங்கப்பட்டது?",
            "options": [
                ("102nd Constitutional Amendment Act, 2018", "102வது அரசியலமைப்புத் திருத்தச் சட்டம், 2018"),
                ("100th Constitutional Amendment Act, 2015", "100வது அரசியலமைப்புத் திருத்தச் சட்டம், 2015"),
                ("101st Constitutional Amendment Act, 2016", "101வது அரசியலமைப்புத் திருத்தச் சட்டம், 2016"),
                ("105th Constitutional Amendment Act, 2021", "105வது அரசியலமைப்புத் திருத்தச் சட்டம், 2021")
            ],
            "correct_key": "A",
            "exp_en": "The 102nd Constitutional Amendment Act, 2018 conferred constitutional status on the National Commission for Backward Classes by inserting Article 338B, replacing the statutory body set up under the NCBC Act 1993.",
            "exp_ta": "2018-ன் 102வது அரசியலமைப்புத் திருத்தச் சட்டம் சரத்து 338B-ஐச் சேர்த்து NCBC-க்கு அரசியலமைப்பு அந்தஸ்தை வழங்கியது. இது 1993 சட்டப்பூர்வ அமைப்பை மாற்றியமைத்தது.",
            "why_a_en": "102nd CAA 2018 inserted Article 338B conferring constitutional status on NCBC.",
            "why_a_ta": "2018-ன் 102வது திருத்தம் சரத்து 338B-ஐச் சேர்த்து NCBC-க்கு அரசியலமைப்பு அந்தஸ்து அளித்தது.",
            "why_b_en": "100th CAA 2015 operationalized the Land Boundary Agreement with Bangladesh.",
            "why_b_ta": "100வது திருத்தம் 2015 வங்காளதேசத்துடனான நில எல்லை ஒப்பந்தத்தை செயல்படுத்தியது.",
            "why_c_en": "101st CAA 2016 introduced Goods and Services Tax (GST).",
            "why_c_ta": "101வது திருத்தம் 2016 சரக்கு மற்றும் சேவை வரியை (GST) அறிமுகப்படுத்தியது.",
            "why_d_en": "105th CAA 2021 restored the power of State governments to identify and maintain their own SEBC lists.",
            "why_d_ta": "105வது திருத்தம் 2021 மாநில அரசுகள் சொந்த SEBC பட்டியலை அடையாளம் காணும் அதிகாரத்தை மீட்டெடுத்தது.",
            "tip_en": "NCBC was first created in 1993 following the Supreme Court's Indra Sawhney judgment (1992).",
            "tip_ta": "1992 இந்திரா சாவ்னி தீர்ப்பைத் தொடர்ந்து 1993-ல் NCBC முதலில் சட்டப்பூர்வமாக உருவாக்கப்பட்டது.",
            "fact_en": "NCBC has civil court powers while investigating complaints under Article 338B(8).",
            "fact_ta": "சரத்து 338B(8)-ன் கீழ் புகார்களை விசாரிக்கும் போது NCBC உரிமையியல் நீதிமன்ற அதிகாரங்களைக் கொண்டுள்ளது."
        },
        # 26
        {
            "subtopic": "105th Constitutional Amendment Act",
            "stem_en": "What was the primary purpose of enacting the 105th Constitutional Amendment Act, 2021?",
            "stem_ta": "105வது அரசியலமைப்புத் திருத்தச் சட்டம், 2021-ஐ இயற்றியதன் முதன்மை நோக்கம் என்ன?",
            "options": [
                ("To restore the power of State Governments to identify and specify Socially and Educationally Backward Classes (SEBCs)", "சமூக மற்றும் கல்வி ரீதியாக பிற்படுத்தப்பட்ட வகுப்பினரை (SEBC) அடையாளம் கண்டு குறிப்பிடும் மாநில அரசுகளின் அதிகாரத்தை மீட்டெடுப்பது"),
                ("To create a new National Commission for Minorities", "சிறுபான்மையினருக்கான புதிய தேசிய ஆணையத்தை உருவாக்குவது"),
                ("To extend political reservations for 20 years", "அரசியல் இடஒதுக்கீட்டை 20 ஆண்டுகளுக்கு நீட்டிப்பது"),
                ("To introduce reservation for women in Parliament", "நாடாளுமன்றத்தில் பெண்களுக்கு இடஒதுக்கீடு அறிமுகப்படுத்துவது")
            ],
            "correct_key": "A",
            "exp_en": "The 105th Constitutional Amendment Act, 2021 clarified Article 342A and amended Articles 338B and 366 to restore the power of State Governments and Union Territories to prepare and maintain their own list of Socially and Educationally Backward Classes (SEBCs), overturning the Supreme Court's interpretation in the Maratha reservation case (Jaishri Laxmanrao Patil, 2021).",
            "exp_ta": "மராத்தா இடஒதுக்கீட்டு வழக்கில் (2021) உச்ச நீதிமன்றத்தின் தீர்ப்பைத் தொடர்ந்து, மாநில அரசுகள் தங்களின் சொந்த SEBC பட்டியலைத் தயாரித்துப் பராமரிக்கும் அதிகாரத்தை மீட்டெடுக்க 105வது திருத்தச் சட்டம் 2021 சரத்து 342A, 338B மற்றும் 366 ஆகியவற்றைத் திருத்தியது.",
            "why_a_en": "105th CAA explicitly restored the power of States to maintain their own state SEBC lists.",
            "why_a_ta": "105வது திருத்தம் மாநில அரசுகளின் சொந்த SEBC பட்டியலைப் பராமரிக்கும் அதிகாரத்தை மீட்டெடுத்தது.",
            "why_b_en": "National Commission for Minorities remains a statutory body under the NCM Act 1992.",
            "why_b_ta": "சிறுபான்மையினர் தேசிய ஆணையம் 1992 சட்டத்தின் கீழான சட்டப்பூர்வ அமைப்பாகவே உள்ளது.",
            "why_c_en": "Political reservation was extended by 104th CAA up to 2030, not 105th CAA.",
            "why_c_ta": "அரசியல் இடஒதுக்கீடு 104வது திருத்தத்தால் 2030 வரை நீட்டிக்கப்பட்டது.",
            "why_d_en": "Women reservation in legislative bodies was enacted by the 106th CAA 2023 (Nari Shakti Vandan Adhiniyam).",
            "why_d_ta": "பெண்கள் இடஒதுக்கீடு 106வது திருத்தம் 2023 (நாரி சக்தி வந்தன் அதினியம்) மூலம் கொண்டுவரப்பட்டது.",
            "tip_en": "Article 342A clause (3) was specifically inserted by the 105th CAA to preserve State lists.",
            "tip_ta": "மாநிலப் பட்டியல்களைப் பாதுகாக்க 105வது திருத்தத்தால் சரத்து 342A உட்பிரிவு (3) சேர்க்கப்பட்டது.",
            "fact_en": "The 105th Amendment was passed unanimously in the Lok Sabha without a single opposing vote.",
            "fact_ta": "105வது திருத்தச் சட்டம் மக்களவையில் ஓர் எதிர்ப்புக் கூட இல்லாமல் ஒருமனதாக நிறைவேற்றப்பட்டது."
        },
        # 27
        {
            "subtopic": "Article 341 Scheduled Castes",
            "stem_en": "Under Article 341 of the Constitution, who is empowered to specify the castes, races, or tribes to be deemed Scheduled Castes in a State?",
            "stem_ta": "சரத்து 341-ன் கீழ், ஒரு மாநிலத்தில் பட்டியலிடப்பட்ட சாதியினராகக் கருதப்பட வேண்டிய சாதி, இனம் அல்லது பழங்குடியினரைக் குறிப்பிடும் அதிகாரம் யாருக்கு உள்ளது?",
            "options": [
                ("The President, after consultation with the Governor of the State", "மாநில ஆளுநரைக் கலந்தாலோசித்த பிறகு குடியரசுத் தலைவர்"),
                ("The Governor acting in his sole discretion", "ஆளுநர் தனது தனிப்பட்ட விருப்பத்தின்படி"),
                ("The State Legislative Assembly by a special majority", "மாநில சட்டமன்றம் சிறப்புப் பெரும்பான்மை மூலம்"),
                ("The National Commission for Scheduled Castes", "பட்டியலிடப்பட்ட சாதியினருக்கான தேசிய ஆணையம்")
            ],
            "correct_key": "A",
            "exp_en": "Under Article 341(1), the President may with respect to any State or Union territory, and where it is a State after consultation with the Governor, by public notification specify the castes deemed to be Scheduled Castes.",
            "exp_ta": "சரத்து 341(1)-ன் படி, குடியரசுத் தலைவர் ஒரு மாநிலத்தைப் பொறுத்தவரை ஆளுநரைக் கலந்தாலோசித்த பிறகு பொது அறிவிப்பின் மூலம் பட்டியலிடப்பட்ட சாதியினரைக் குறிப்பிடலாம்.",
            "why_a_en": "Article 341(1) assigns this power to the President after consultation with the Governor.",
            "why_a_ta": "சரத்து 341(1) ஆளுநரைக் கலந்தாலோசித்த பிறகு குடியரசுத் தலைவருக்கு இந்த அதிகாரத்தை வழங்குகிறது.",
            "why_b_en": "The Governor cannot issue the notification; he is only consulted.",
            "why_b_ta": "ஆளுநர் அறிவிப்பை வெளியிட முடியாது; அவரிடம் ஆலோசனை மட்டுமே பெறப்படுகிறது.",
            "why_c_en": "The State Assembly has no power to include or exclude castes from the SC list.",
            "why_c_ta": "மாநில சட்டமன்றத்திற்கு SC பட்டியலில் சாதிகளைச் சேர்க்கவோ நீக்கவோ அதிகாரம் இல்லை.",
            "why_d_en": "NCSC investigates and advises, but notification is an executive presidential power.",
            "why_d_ta": "NCSC விசாரித்து ஆலோசனை மட்டுமே கூறுகிறது; அறிவிக்கை குடியரசுத் தலைவரின் அதிகாரமாகும்.",
            "tip_en": "Any subsequent inclusion in or exclusion from the SC list can ONLY be done by Parliament by law (Art 341(2)).",
            "tip_ta": "SC பட்டியலில் பின்னர் எதையும் சேர்ப்பதோ நீக்குவதோ நாடாளுமன்றச் சட்டம் மூலம் மட்டுமே செய்ய முடியும் (சரத்து 341(2)).",
            "fact_en": "Constitution (Scheduled Castes) Order was first issued by the President in 1950.",
            "fact_ta": "அரசியலமைப்பு (பட்டியலிடப்பட்ட சாதியினர்) ஆணை 1950-ல் குடியரசுத் தலைவரால் முதன்முதலில் வெளியிடப்பட்டது."
        },
        # 28
        {
            "subtopic": "Article 342 Scheduled Tribes",
            "stem_en": "Under Article 342(2), who has the sole power to include or exclude any tribe from the list of Scheduled Tribes specified in a Presidential notification?",
            "stem_ta": "சரத்து 342(2)-ன் கீழ், குடியரசுத் தலைவர் அறிவிக்கையில் உள்ள பட்டியலிடப்பட்ட பழங்குடியினர் பட்டியலில் ஏதேனும் பழங்குடியைச் சேர்க்க அல்லது நீக்க யாருக்கு மட்டுமே அதிகாரம் உள்ளது?",
            "options": [
                ("Parliament by law", "நாடாளுமன்றம் சட்டத்தின் மூலம்"),
                ("The President by executive order", "குடியரசுத் தலைவர் நிர்வாக ஆணை மூலம்"),
                ("The Supreme Court of India", "இந்திய உச்ச நீதிமன்றம்"),
                ("The State Governor by gazette notification", "மாநில ஆளுநர் அரசிதழ் அறிவிப்பு மூலம்")
            ],
            "correct_key": "A",
            "exp_en": "Article 342(2) explicitly states that Parliament may by law include in or exclude from the list of Scheduled Tribes specified in a notification any tribe or tribal community, and save as aforesaid a notification shall not be varied.",
            "exp_ta": "சரத்து 342(2) நாடாளுமன்றம் சட்டத்தின் மூலம் மட்டுமே பட்டியலில் எந்தவொரு பழங்குடியையும் சேர்க்கவோ நீக்கவோ முடியும் என்று கூறுகிறது; வேறு எந்த முறையிலும் அறிவிக்கையை மாற்ற முடியாது.",
            "why_a_en": "Article 342(2) vests the power to vary the ST list exclusively in Parliament by law.",
            "why_a_ta": "சரத்து 342(2) பழங்குடியினர் பட்டியலை மாற்றியமைக்கும் அதிகாரத்தை நாடாளுமன்றச் சட்டத்திற்கு மட்டுமே வழங்குகிறது.",
            "why_b_en": "The President issues the initial notification (Art 342(1)), but cannot subsequently alter it by executive order.",
            "why_b_ta": "குடியரசுத் தலைவர் ஆரம்ப அறிவிப்பை வெளியிடுகிறார், ஆனால் பின்னர் நிர்வாக ஆணை மூலம் மாற்ற முடியாது.",
            "why_c_en": "Judiciary cannot alter constitutional statutory schedules of tribes directly.",
            "why_c_ta": "நீதித்துறை பழங்குடியினர் அட்டவணையை நேரடியாக மாற்ற முடியாது.",
            "why_d_en": "Governors have no power to alter the ST list.",
            "why_d_ta": "ஆளுநர்களுக்கு ST பட்டியலை மாற்றும் அதிகாரம் இல்லை.",
            "tip_en": "Both Article 341(2) (SCs) and Article 342(2) (STs) require an Act of Parliament to add or delete communities.",
            "tip_ta": "சரத்து 341(2) (SC) மற்றும் சரத்து 342(2) (ST) இரண்டும் சமூகங்களைச் சேர்க்கவோ நீக்கவோ நாடாளுமன்றச் சட்டத்தைக் கோருகின்றன.",
            "fact_en": "In State of Maharashtra v. Milind (2001), the SC held that neither courts nor state governments can manipulate SC/ST lists.",
            "fact_ta": "மில்லிந்த் வழக்கில் (2001), நீதிமன்றங்களோ மாநில அரசுகளோ SC/ST பட்டியல்களை மாற்ற முடியாது என உச்ச நீதிமன்றம் தீர்ப்பளித்தது."
        },
        # 29
        {
            "subtopic": "Article 340 Backward Classes Commission",
            "stem_en": "The First Backward Classes Commission (1953) was appointed by the President under Article 340 under the chairmanship of:",
            "stem_ta": "சரத்து 340-ன் கீழ் குடியரசுத் தலைவரால் நியமிக்கப்பட்ட முதலாவது பிற்படுத்தப்பட்டோர் ஆணையம் (1953) யாருடைய தலைமையில் அமைக்கப்பட்டது?",
            "options": [
                ("Kaka Kalelkar", "காக்கா கலேல்கர்"),
                ("B. P. Mandal", "பி. பி. மண்டல்"),
                ("Justice Rohini", "நீதிபதி ரோகிணி"),
                ("Dr. B. R. Ambedkar", "டாக்டர் பி. ஆர். அம்பேத்கர்")
            ],
            "correct_key": "A",
            "exp_en": "The First Backward Classes Commission was appointed under Article 340 in 1953 under the chairmanship of Kaka Kalelkar (Kalelkar Commission), which submitted its report in 1955.",
            "exp_ta": "1953 ஆம் ஆண்டு சரத்து 340-ன் கீழ் முதலாவது பிற்படுத்தப்பட்டோர் ஆணையம் காக்கா கலேல்கர் தலைமையில் அமைக்கப்பட்டு, 1955-ல் தனது அறிக்கையை சமர்ப்பித்தது.",
            "why_a_en": "Kaka Kalelkar chaired the First Backward Classes Commission (1953-1955).",
            "why_a_ta": "காக்கா கலேல்கர் முதலாவது பிற்படுத்தப்பட்டோர் ஆணையத்தின் (1953-1955) தலைவராக இருந்தார்.",
            "why_b_en": "B. P. Mandal chaired the Second Backward Classes Commission (Mandal Commission, 1979).",
            "why_b_ta": "பி. பி. மண்டல் இரண்டாவது பிற்படுத்தப்பட்டோர் ஆணையத்திற்கு (மண்டல் ஆணையம், 1979) தலைமை தாங்கினார்.",
            "why_c_en": "Justice G. Rohini headed the Commission for Sub-categorization of OBCs (constituted in 2017).",
            "why_c_ta": "நீதிபதி ஜி. ரோகிணி OBC உட்பிரிவுக்கான ஆணையத்திற்கு (2017) தலைமை தாங்கினார்.",
            "why_d_en": "Dr. B. R. Ambedkar was the Chairman of the Drafting Committee of the Constituent Assembly.",
            "why_d_ta": "டாக்டர் பி. ஆர். அம்பேத்கர் வரைவுக் குழுவின் தலைவராக இருந்தார்.",
            "tip_en": "Article 340 empowers the President to appoint a commission to investigate the conditions of socially and educationally backward classes.",
            "tip_ta": "சமூக மற்றும் கல்வி ரீதியாக பிற்படுத்தப்பட்ட வகுப்பினரின் நிலையை ஆராய ஆணையம் அமைக்க குடியரசுத் தலைவருக்கு சரத்து 340 அதிகாரம் அளிக்கிறது.",
            "fact_en": "The Kalelkar Commission identified 2,399 backward castes and used criteria based on caste hierarchy, trade, and education.",
            "fact_ta": "கலேல்கர் ஆணையம் 2,399 பிற்படுத்தப்பட்ட சாதிகளை அடையாளம் கண்டு, சாதி படிநிலை மற்றும் கல்வி அடிப்படையில் அளவுகோல்களைப் பயன்படுத்தியது."
        },
        # 30
        {
            "subtopic": "Mandal Commission and Article 340",
            "stem_en": "The Second Backward Classes Commission, headed by B.P. Mandal, recommended what percentage of reservation for OBCs in government jobs?",
            "stem_ta": "பி.பி. மண்டல் தலைமையிலான இரண்டாவது பிற்படுத்தப்பட்டோர் ஆணையம் அரசு வேலைகளில் OBC-களுக்கு எத்தனை சதவீத இடஒதுக்கீட்டை பரிந்துரைத்தது?",
            "options": [
                ("27 percent", "27 சதவீதம்"),
                ("22.5 percent", "22.5 சதவீதம்"),
                ("33 percent", "33 சதவீதம்"),
                ("50 percent", "50 சதவீதம்")
            ],
            "correct_key": "A",
            "exp_en": "The Mandal Commission (appointed in 1979 by the Morarji Desai Government, submitted in 1980) recommended 27% reservation for Other Backward Classes (OBCs) in central government services and public sector undertakings.",
            "exp_ta": "மண்டல் ஆணையம் (1979-ல் மொரார்ஜி தேசாய் அரசால் அமைக்கப்பட்டு, 1980-ல் சமர்ப்பிக்கப்பட்டது) மத்திய அரசுப் பணிகளில் இதர பிற்படுத்தப்பட்ட வகுப்பினருக்கு (OBC) 27% இடஒதுக்கீட்டைப் பரிந்துரைத்தது.",
            "why_a_en": "Mandal Commission specifically recommended 27% reservation for OBCs.",
            "why_a_ta": "மண்டல் ஆணையம் குறிப்பாக OBC-களுக்கு 27% இடஒதுக்கீட்டைப் பரிந்துரைத்தது.",
            "why_b_en": "22.5% was the combined existing reservation for SCs (15%) and STs (7.5%).",
            "why_b_ta": "22.5% என்பது SC (15%) மற்றும் ST (7.5%) ஆகியோருக்கான அப்போதைய இடஒதுக்கீடு.",
            "why_c_en": "33% is the constitutional reservation for women in local bodies and recently enacted for Parliament.",
            "why_c_ta": "33% என்பது உள்ளாட்சி மற்றும் நாடாளுமன்றத்தில் பெண்களுக்கான இடஒதுக்கீடு.",
            "why_d_en": "50% is the ceiling cap established by the Supreme Court in the Indra Sawhney case (1992).",
            "why_d_ta": "50% என்பது இந்திரா சாவ்னி வழக்கில் (1992) உச்ச நீதிமன்றத்தால் விதிக்கப்பட்ட உச்ச வரம்பு.",
            "tip_en": "Combined reservation: SC (15%) + ST (7.5%) + OBC (27%) = 49.5%, staying just below the 50% cap.",
            "tip_ta": "மொத்த இடஒதுக்கீடு: SC (15%) + ST (7.5%) + OBC (27%) = 49.5%, 50% உச்ச வரம்பிற்குள் அமைகிறது.",
            "fact_en": "Prime Minister V. P. Singh announced the implementation of the Mandal Commission recommendations on 7 August 1990.",
            "fact_ta": "பிரதமர் வி. பி. சிங் 1990 ஆகஸ்ட் 7 அன்று மண்டல் ஆணைய பரிந்துரைகளை அமல்படுத்துவதாக அறிவித்தார்."
        },
        # 31
        {
            "subtopic": "Article 15(4) Educational Reservation",
            "stem_en": "Article 15(4), which enables the State to make special provisions for the advancement of socially and educationally backward classes or SCs/STs, was added by which Amendment?",
            "stem_ta": "சமூக மற்றும் கல்வி ரீதியாக பிற்படுத்தப்பட்ட வகுப்பினர் அல்லது SC/ST முன்னேற்றத்திற்காக அரசு சிறப்பு விதிகளை உருவாக்க வழிவகுக்கும் சரத்து 15(4), எந்தத் திருத்தத்தால் சேர்க்கப்பட்டது?",
            "options": [
                ("1st Constitutional Amendment Act, 1951", "1வது அரசியலமைப்புத் திருத்தச் சட்டம், 1951"),
                ("7th Constitutional Amendment Act, 1956", "7வது அரசியலமைப்புத் திருத்தச் சட்டம், 1956"),
                ("42nd Constitutional Amendment Act, 1976", "42வது அரசியலமைப்புத் திருத்தச் சட்டம், 1976"),
                ("93rd Constitutional Amendment Act, 2005", "93வது அரசியலமைப்புத் திருத்தச் சட்டம், 2005")
            ],
            "correct_key": "A",
            "exp_en": "Article 15(4) was added by the 1st Constitutional Amendment Act, 1951 in response to the Supreme Court's ruling in State of Madras v. Champakam Dorairajan (1951), which had invalidated Madras's Communal G.O.",
            "exp_ta": "செண்பகம் துரைராஜன் வழக்கில் (1951) மெட்ராஸ் மாநிலத்தின் வகுப்புவாத அரசாணை ரத்து செய்யப்பட்டதைத் தொடர்ந்து, 1951-ன் 1வது அரசியலமைப்புத் திருத்தச் சட்டம் மூலம் சரத்து 15(4) சேர்க்கப்பட்டது.",
            "why_a_en": "1st CAA 1951 inserted Article 15(4).",
            "why_a_ta": "1951-ன் 1வது திருத்தம் சரத்து 15(4)-ஐச் சேர்த்தது.",
            "why_b_en": "7th CAA 1956 reorganized states on linguistic lines.",
            "why_b_ta": "1956-ன் 7வது திருத்தம் மொழிவாரி மாநிலங்களை மறுசீரமைத்தது.",
            "why_c_en": "42nd CAA 1976 was the mini-constitution.",
            "why_c_ta": "1976-ன் 42வது திருத்தம் குறு-அரசியலமைப்பாகும்.",
            "why_d_en": "93rd CAA 2005 added Article 15(5) for private educational institutions.",
            "why_d_ta": "2005-ன் 93வது திருத்தம் தனியார் கல்வி நிறுவனங்களுக்கான சரத்து 15(5)-ஐ சேர்த்தது.",
            "tip_en": "Remember the trigger: Champakam Dorairajan (1951) led directly to the First Amendment inserting Article 15(4).",
            "tip_ta": "நினைவில் கொள்க: செண்பகம் துரைராஜன் வழக்கு (1951) முதல் திருத்தத்திற்கு வழிவகுத்து சரத்து 15(4)-ஐச் சேர்த்தது.",
            "fact_en": "Tamil Nadu's historic Communal G.O. had existed since 1927 under the Justice Party government.",
            "fact_ta": "நீதிக்கட்சி ஆட்சியின் கீழ் 1927 முதல் தமிழ்நாட்டின் வரலாற்றுச் சிறப்புமிக்க வகுப்புவாரி அரசாணை நடைமுறையில் இருந்தது."
        },
        # 32
        {
            "subtopic": "Article 15(5) Private Institutions Reservation",
            "stem_en": "Which Constitutional Amendment inserted Article 15(5) to provide reservation in educational institutions, including private aided or unaided institutions (except minority institutions)?",
            "stem_ta": "சிறுபான்மையினர் கல்வி நிறுவனங்கள் நீங்கலாக, தனியார் உதவிபெறும் அல்லது உதவிபெறாத கல்வி நிறுவனங்கள் உட்பட கல்வி நிறுவனங்களில் இட ஒதுக்கீடு வழங்க சரத்து 15(5)-ஐ எந்தத் திருத்தம் சேர்த்தது?",
            "options": [
                ("93rd Constitutional Amendment Act, 2005", "93வது அரசியலமைப்புத் திருத்தச் சட்டம், 2005"),
                ("86th Constitutional Amendment Act, 2002", "86வது அரசியலமைப்புத் திருத்தச் சட்டம், 2002"),
                ("91st Constitutional Amendment Act, 2003", "91வது அரசியலமைப்புத் திருத்தச் சட்டம், 2003"),
                ("103rd Constitutional Amendment Act, 2019", "103வது அரசியலமைப்புத் திருத்தச் சட்டம், 2019")
            ],
            "correct_key": "A",
            "exp_en": "The 93rd Constitutional Amendment Act, 2005 inserted Article 15(5) to enable reservation for SCs, STs, and SEBCs in educational institutions, whether aided or unaided, other than minority educational institutions referred to in Article 30(1).",
            "exp_ta": "2005-ன் 93வது அரசியலமைப்புத் திருத்தச் சட்டம் சரத்து 15(5)-ஐச் சேர்த்து, சரத்து 30(1)-ன் கீழான சிறுபான்மையினர் கல்வி நிறுவனங்கள் தவிர, உதவிபெறும் அல்லது உதவிபெறாத பிற கல்வி நிறுவனங்களில் இடஒதுக்கீடு வழங்க வழிவகுத்தது.",
            "why_a_en": "93rd CAA 2005 inserted Article 15(5).",
            "why_a_ta": "2005-ன் 93வது திருத்தம் சரத்து 15(5)-ஐச் சேர்த்தது.",
            "why_b_en": "86th CAA 2002 introduced Right to Education under Article 21A.",
            "why_b_ta": "2002-ன் 86வது திருத்தம் சரத்து 21A-ன் கீழ் கல்வி உரிமையை அறிமுகப்படுத்தியது.",
            "why_c_en": "91st CAA 2003 limited ministry size and strengthened anti-defection law.",
            "why_c_ta": "2003-ன் 91வது திருத்தம் அமைச்சரவை அளவைக் கட்டுப்படுத்தியது.",
            "why_d_en": "103rd CAA 2019 added Article 15(6) for EWS reservation.",
            "why_d_ta": "2019-ன் 103வது திருத்தம் EWS இடஒதுக்கீட்டிற்கான சரத்து 15(6)-ஐ சேர்த்தது.",
            "tip_en": "Art 15(5) nullified the effect of SC rulings in TMA Pai (2002) and Inamdar (2005) regarding private unaided colleges.",
            "tip_ta": "சரத்து 15(5) தனியார் சுயநிதி கல்லூரிகள் தொடர்பான TMA பை மற்றும் இனாம்தார் வழக்குகளின் தீர்ப்பு விளைவுகளை ரத்து செய்தது.",
            "fact_en": "The Supreme Court upheld the constitutional validity of Article 15(5) in Ashoka Kumar Thakur v. Union of India (2008).",
            "fact_ta": "அசோக் குமார் தாக்கூர் வழக்கில் (2008) உச்ச நீதிமன்றம் சரத்து 15(5)-ன் செல்லுபடியாகும் தன்மையை உறுதிப்படுத்தியது."
        },
        # 33
        {
            "subtopic": "Article 16(4) Public Employment",
            "stem_en": "Under Article 16(4), the State is empowered to make reservation of appointments or posts in favor of any backward class of citizens if:",
            "stem_ta": "சரத்து 16(4)-ன் கீழ், எந்த சூழ்நிலையில் எந்தவொரு பிற்படுத்தப்பட்ட குடிமக்களுக்கும் நியமனங்கள் அல்லது பதவிகளில் இட ஒதுக்கீடு செய்ய அரசுக்கு அதிகாரம் உள்ளது?",
            "options": [
                ("In the opinion of the State, they are not adequately represented in the services under the State", "அரசின் பணிகளில் அவர்கள் போதுமான அளவு பிரதிநிதித்துவம் பெறவில்லை என்று அரசு கருதினால்"),
                ("The Governor issues an extraordinary ordinance", "ஆளுநர் ஒரு சிறப்பு அவசரச் சட்டத்தைப் பிறப்பித்தால்"),
                ("The candidate belongs to an economically weaker section regardless of caste", "சாதி பாராமல் விண்ணப்பதாரர் பொருளாதாரத்தில் நலிவடைந்த பிரிவைச் சேர்ந்தவராக இருந்தால்"),
                ("A minimum of 50 percent marks are secured in competitive exams", "போட்டித் தேர்வுகளில் குறைந்தபட்சம் 50 சதவீத மதிப்பெண்கள் பெற்றிருந்தால்")
            ],
            "correct_key": "A",
            "exp_en": "Article 16(4) allows reservation in public employment for any backward class of citizens which, in the opinion of the State, is not adequately represented in the services under the State.",
            "exp_ta": "சரத்து 16(4), மாநிலத்தின் பணிகளில் போதுமான அளவு பிரதிநிதித்துவம் பெறவில்லை என்று கருதப்படும் எந்தவொரு பிற்படுத்தப்பட்ட குடிமக்களுக்கும் அரசுப் பணிகளில் இட ஒதுக்கீடு செய்ய வகைசெய்கிறது.",
            "why_a_en": "Article 16(4) explicitly specifies 'not adequately represented in the services under the State'.",
            "why_a_ta": "சரத்து 16(4) 'அரசின் பணிகளில் போதுமான பிரதிநிதித்துவம் பெறவில்லை' என்பதை தெளிவாகக் கூறுகிறது.",
            "why_b_en": "Ordinance is not the constitutional prerequisite; legislative enactment or executive order suffices.",
            "why_b_ta": "அவசரச்சட்டம் முன்நிபந்தனை அல்ல; சட்டமோ அரசாணையோ போதுமானது.",
            "why_c_en": "EWS reservation is governed by Article 16(6), not Article 16(4).",
            "why_c_ta": "EWS இடஒதுக்கீடு சரத்து 16(6)-ஆல் நிர்வகிக்கப்படுகிறது, 16(4)-ஆல் அல்ல.",
            "why_d_en": "Marks criteria are not part of Article 16(4).",
            "why_d_ta": "மதிப்பெண் வரம்பு சரத்து 16(4)-ன் நிபந்தனை அல்ல.",
            "tip_en": "Two essential conditions of Article 16(4): (1) Backward class of citizens, (2) Inadequately represented in state services.",
            "tip_ta": "சரத்து 16(4)-ன் இரண்டு முக்கிய நிபந்தனைகள்: (1) பிற்படுத்தப்பட்ட குடிமக்கள், (2) அரசுப் பணிகளில் போதுமான பிரதிநிதித்துவம் இன்மை.",
            "fact_en": "Article 16(4) is an enabling provision, not a fundamental right in itself conferring an absolute right to quota.",
            "fact_ta": "சரத்து 16(4) ஒரு வழிவகுக்கும் விதியாகும், அதுவே தானாக இடஒதுக்கீட்டிற்கான முழுமையான அடிப்படை உரிமையாக அமையாது."
        },
        # 34
        {
            "subtopic": "Article 16(4A) Promotion Reservation",
            "stem_en": "Which Constitutional Amendment Act inserted Article 16(4A) to provide reservation in promotions for Scheduled Castes and Scheduled Tribes?",
            "stem_ta": "பட்டியலிடப்பட்ட சாதியினர் மற்றும் பழங்குடியினருக்கு பதவி உயர்வில் இட ஒதுக்கீடு வழங்க சரத்து 16(4A)-ஐ எந்த அரசியலமைப்புத் திருத்தச் சட்டம் சேர்த்தது?",
            "options": [
                ("77th Constitutional Amendment Act, 1995", "77வது அரசியலமைப்புத் திருத்தச் சட்டம், 1995"),
                ("81st Constitutional Amendment Act, 2000", "81வது அரசியலமைப்புத் திருத்தச் சட்டம், 2000"),
                ("85th Constitutional Amendment Act, 2001", "85வது அரசியலமைப்புத் திருத்தச் சட்டம், 2001"),
                ("89th Constitutional Amendment Act, 2003", "89வது அரசியலமைப்புத் திருத்தச் சட்டம், 2003")
            ],
            "correct_key": "A",
            "exp_en": "The 77th Constitutional Amendment Act, 1995 inserted Article 16(4A) to overcome the Supreme Court's ruling in the Indra Sawhney case (1992), which had barred reservation in promotions.",
            "exp_ta": "பதவி உயர்வில் இடஒதுக்கீட்டைத் தடை செய்த இந்திரா சாவ்னி வழக்கின் (1992) தீர்ப்பை முறியடிக்க, 1995-ன் 77வது அரசியலமைப்புத் திருத்தச் சட்டம் சரத்து 16(4A)-ஐச் சேர்த்தது.",
            "why_a_en": "77th CAA 1995 inserted Article 16(4A).",
            "why_a_ta": "1995-ன் 77வது திருத்தம் சரத்து 16(4A)-ஐச் சேர்த்தது.",
            "why_b_en": "81st CAA 2000 inserted Article 16(4B) on carry-forward vacancies.",
            "why_b_ta": "2000-ன் 81வது திருத்தம் நிரப்பப்படாத இடங்களை முன்னெடுத்துச் செல்லும் சரத்து 16(4B)-ஐச் சேர்த்தது.",
            "why_c_en": "85th CAA 2001 added 'consequential seniority' to Article 16(4A).",
            "why_c_ta": "2001-ன் 85வது திருத்தம் சரத்து 16(4A)-ல் 'தொடர் பணிமூப்பு' என்பதைச் சேர்த்தது.",
            "why_d_en": "89th CAA 2003 bifurcated NCSC and NCST.",
            "why_d_ta": "2003-ன் 89வது திருத்தம் NCSC மற்றும் NCST-ஐப் பிரித்தது.",
            "tip_en": "Article 16(4A) allows promotion reservation only for SCs and STs, NOT for OBCs.",
            "tip_ta": "சரத்து 16(4A) பதவி உயர்வு இடஒதுக்கீட்டை SC மற்றும் ST-க்கு மட்டுமே அனுமதிக்கிறது, OBC-க்கு அல்ல.",
            "fact_en": "The constitutional validity of Article 16(4A) was upheld in M. Nagaraj v. Union of India (2006).",
            "fact_ta": "எம். நாகராஜ் வழக்கில் (2006) சரத்து 16(4A)-ன் அரசியலமைப்பு செல்லுபடியாகும் தன்மை உறுதி செய்யப்பட்டது."
        },
        # 35
        {
            "subtopic": "Article 16(4B) Carry Forward Rule",
            "stem_en": "Article 16(4B), which permits the carry-forward of unfilled reserved vacancies of a year without counting them towards the 50% ceiling in the succeeding year, was added by:",
            "stem_ta": "ஒரு ஆண்டின் நிரப்பப்படாத இடஒதுக்கீட்டு இடங்களை அடுத்த ஆண்டிற்கு முன்னெடுத்துச் செல்லும்போது, அவற்றை 50% உச்ச வரம்பில் சேர்க்காமல் அனுமதிக்க வகைசெய்யும் சரத்து 16(4B), எந்தத் திருத்தத்தால் சேர்க்கப்பட்டது?",
            "options": [
                ("81st Constitutional Amendment Act, 2000", "81வது அரசியலமைப்புத் திருத்தச் சட்டம், 2000"),
                ("77th Constitutional Amendment Act, 1995", "77வது அரசியலமைப்புத் திருத்தச் சட்டம், 1995"),
                ("85th Constitutional Amendment Act, 2001", "85வது அரசியலமைப்புத் திருத்தச் சட்டம், 2001"),
                ("93rd Constitutional Amendment Act, 2005", "93வது அரசியலமைப்புத் திருத்தச் சட்டம், 2005")
            ],
            "correct_key": "A",
            "exp_en": "The 81st Constitutional Amendment Act, 2000 introduced Article 16(4B), ending the 50% ceiling cap on backlog reserved vacancies considered as a separate class of vacancies.",
            "exp_ta": "2000-ன் 81வது அரசியலமைப்புத் திருத்தச் சட்டம் சரத்து 16(4B)-ஐ அறிமுகப்படுத்தியது. இது நிலுவையில் உள்ள நிரப்பப்படாத இடங்களை தனிப் பிரிவாகக் கருதி, அவற்றுக்கு 50% உச்ச வரம்பு பொருந்தாது என நிர்ணயித்தது.",
            "why_a_en": "81st CAA 2000 inserted Article 16(4B).",
            "why_a_ta": "2000-ன் 81வது திருத்தம் சரத்து 16(4B)-ஐச் சேர்த்தது.",
            "why_b_en": "77th CAA 1995 inserted Article 16(4A) for promotion reservation.",
            "why_b_ta": "1995-ன் 77வது திருத்தம் பதவி உயர்வு இடஒதுக்கீட்டிற்கான சரத்து 16(4A)-ஐச் சேர்த்தது.",
            "why_c_en": "85th CAA 2001 amended Article 16(4A) for consequential seniority.",
            "why_c_ta": "2001-ன் 85வது திருத்தம் தொடர் பணிமூப்பிற்காக சரத்து 16(4A)-ஐத் திருத்தியது.",
            "why_d_en": "93rd CAA 2005 inserted Article 15(5) for private institutions.",
            "why_d_ta": "2005-ன் 93வது திருத்தம் தனியார் கல்வி நிறுவனங்களுக்கான சரத்து 15(5)-ஐச் சேர்த்தது.",
            "tip_en": "Article 16(4B) is known as the 'Backlog Vacancies Amendment'.",
            "tip_ta": "சரத்து 16(4B) 'நிலுவை பணியிடங்களுக்கான திருத்தம்' என அழைக்கப்படுகிறது.",
            "fact_en": "In M. Nagaraj (2006), the Supreme Court upheld the validity of Article 16(4B).",
            "fact_ta": "எம். நாகராஜ் வழக்கில் (2006), உச்ச நீதிமன்றம் சரத்து 16(4B)-ன் செல்லுபடியாகும் தன்மையை உறுதி செய்தது."
        },
        # 36
        {
            "subtopic": "103rd Amendment EWS Reservation",
            "stem_en": "Articles 15(6) and 16(6), providing up to 10% reservation for Economically Weaker Sections (EWS), were inserted by which Constitutional Amendment?",
            "stem_ta": "பொருளாதாரத்தில் நலிவடைந்த பிரிவினருக்கு (EWS) 10% வரை இடஒதுக்கீடு வழங்கும் சரத்துகள் 15(6) மற்றும் 16(6), எந்த அரசியலமைப்புத் திருத்தச் சட்டத்தால் சேர்க்கப்பட்டன?",
            "options": [
                ("103rd Constitutional Amendment Act, 2019", "103வது அரசியலமைப்புத் திருத்தச் சட்டம், 2019"),
                ("102nd Constitutional Amendment Act, 2018", "102வது அரசியலமைப்புத் திருத்தச் சட்டம், 2018"),
                ("104th Constitutional Amendment Act, 2019", "104வது அரசியலமைப்புத் திருத்தச் சட்டம், 2019"),
                ("105th Constitutional Amendment Act, 2021", "105வது அரசியலமைப்புத் திருத்தச் சட்டம், 2021")
            ],
            "correct_key": "A",
            "exp_en": "The 103rd Constitutional Amendment Act, 2019 added Articles 15(6) and 16(6) to allow up to 10% reservation for citizens belonging to Economically Weaker Sections (EWS) other than those covered under SC, ST, and SEBC.",
            "exp_ta": "2019-ன் 103வது அரசியலமைப்புத் திருத்தச் சட்டம் சரத்துகள் 15(6) மற்றும் 16(6)-ஐச் சேர்த்து, SC, ST மற்றும் பிற்படுத்தப்பட்ட பிரிவினருக்கு உட்படாத பொருளாதாரத்தில் நலிவடைந்த பிரிவினருக்கு (EWS) 10% வரை இடஒதுக்கீட்டை வழங்கியது.",
            "why_a_en": "103rd CAA 2019 inserted Articles 15(6) and 16(6).",
            "why_a_ta": "2019-ன் 103வது திருத்தம் சரத்துகள் 15(6) மற்றும் 16(6)-ஐச் சேர்த்தது.",
            "why_b_en": "102nd CAA 2018 constitutionalized NCBC.",
            "why_b_ta": "2018-ன் 102வது திருத்தம் NCBC-க்கு அரசியலமைப்பு அந்தஸ்து வழங்கியது.",
            "why_c_en": "104th CAA 2019 extended SC/ST assembly reservation and discontinued Anglo-Indian nomination.",
            "why_c_ta": "104வது திருத்தம் SC/ST இடஒதுக்கீட்டை நீட்டித்தது மற்றும் ஆங்கிலோ-இந்திய நியமனத்தை நிறுத்தியது.",
            "why_d_en": "105th CAA 2021 restored State power over SEBC lists.",
            "why_d_ta": "105வது திருத்தம் SEBC பட்டியல் மீதான மாநில அதிகாரத்தை மீட்டெடுத்தது.",
            "tip_en": "EWS reservation constitutionality was upheld by the Supreme Court in Janhit Abhiyan v. Union of India (2022) by a 3:2 majority.",
            "tip_ta": "ஜன்ஹித் அபியான் வழக்கில் (2022) 3:2 பெரும்பான்மையில் உச்ச நீதிமன்றம் EWS இடஒதுக்கீட்டின் செல்லுபடியாகும் தன்மையை உறுதி செய்தது.",
            "fact_en": "EWS quota is over and above the existing 50% reservation for SC, ST, and OBC.",
            "fact_ta": "EWS இடஒதுக்கீடு என்பது SC, ST மற்றும் OBC-க்கான 50% இடஒதுக்கீட்டிற்கு கூடுதலாக வழங்கப்படுவதாகும்."
        },
        # 37
        {
            "subtopic": "Article 46 Directive Principles",
            "stem_en": "Which Directive Principle of State Policy enjoins the State to promote with special care the educational and economic interests of the weaker sections, and in particular of the Scheduled Castes and Scheduled Tribes?",
            "stem_ta": "எளிய பிரிவினர், குறிப்பாக பட்டியலிடப்பட்ட சாதியினர் மற்றும் பழங்குடியினரின் கல்வி மற்றும் பொருளாதார நலன்களை சிறப்பு கவனத்துடன் மேம்படுத்த அரசுக்கு அறிவுறுத்தும் அரசு வழிகாட்டு நெறிமுறை எது?",
            "options": [
                ("Article 46", "சரத்து 46"),
                ("Article 45", "சரத்து 45"),
                ("Article 44", "சரத்து 44"),
                ("Article 47", "சரத்து 47")
            ],
            "correct_key": "A",
            "exp_en": "Article 46 of Part IV directs the State to promote with special care the educational and economic interests of the weaker sections of the people, and in particular, of the Scheduled Castes and the Scheduled Tribes, and protect them from social injustice and all forms of exploitation.",
            "exp_ta": "பகுதி IV-ன் சரத்து 46, மக்களின் எளிய பிரிவினர், குறிப்பாக SC மற்றும் ST பிரிவினரின் கல்வி மற்றும் பொருளாதார நலன்களை சிறப்பு கவனத்துடன் மேம்படுத்தவும், அவர்களை சமூக அநீதி மற்றும் அனைத்து வகையான சுரண்டல்களிலிருந்தும் பாதுகாக்கவும் அரசுக்கு வழிகாட்டுகிறது.",
            "why_a_en": "Article 46 explicitly mandates promotion of educational and economic interests of SCs, STs, and weaker sections.",
            "why_a_ta": "சரத்து 46 SC, ST மற்றும் எளிய பிரிவினரின் கல்வி, பொருளாதார நலன்களை மேம்படுத்துவதை தெளிவாகக் கூறுகிறது.",
            "why_b_en": "Article 45 deals with early childhood care and education for children below six years.",
            "why_b_ta": "சரத்து 45 ஆறு வயதுக்குட்பட்ட குழந்தைகளுக்கான ஆரம்பக் கல்வி மற்றும் பராமரிப்பைக் கையாள்கிறது.",
            "why_c_en": "Article 44 deals with Uniform Civil Code.",
            "why_c_ta": "சரத்து 44 பொது சிவில் சட்டத்தைக் கையாள்கிறது.",
            "why_d_en": "Article 47 deals with duty of the State to raise nutrition, standard of living and improve public health.",
            "why_d_ta": "சரத்து 47 ஊட்டச்சத்து மற்றும் பொது சுகாதாரத்தை மேம்படுத்தும் அரசின் கடமையைக் கூறுகிறது.",
            "tip_en": "Article 46 serves as the constitutional philosophical foundation for enabling articles like 15(4) and 16(4).",
            "tip_ta": "சரத்துகள் 15(4) மற்றும் 16(4) போன்ற விதிகளுக்கான தத்துவார்த்த அடிப்படையாக சரத்து 46 செயல்படுகிறது.",
            "fact_en": "Dr. Ambedkar highlighted Article 46 during the Constituent Assembly debates as a charter of social justice.",
            "fact_ta": "அரசியலமைப்பு நிர்ணய சபை விவாதங்களில் டாக்டர் அம்பேத்கர் சரத்து 46-ஐ சமூக நீதிக்கான சாசனமாக சுட்டிக்காட்டினார்."
        },
        # 38
        {
            "subtopic": "Article 335 Claims of SCs and STs",
            "stem_en": "Article 335 of the Constitution provides that the claims of members of the SCs and STs shall be taken into consideration in public appointments consistently with:",
            "stem_ta": "அரசுப் பணிகளில் நியமனங்கள் செய்யும்போது SC மற்றும் ST உறுப்பினர்களின் கோரிக்கைகள் எதனுடன் முரண்படாமல் கருத்தில் கொள்ளப்பட வேண்டும் என்று சரத்து 335 கூறுகிறது?",
            "options": [
                ("The maintenance of efficiency of administration", "நிர்வாகத் திறனைப் பராமரித்தல்"),
                ("The directives of international conventions", "சர்வதேச உடன்படிக்கைகளின் வழிகாட்டுதல்கள்"),
                ("The overall profit of public sector enterprises", "பொதுத்துறை நிறுவனங்களின் ஒட்டுமொத்த லாபம்"),
                ("The numerical strength of the ruling party", "ஆளும் கட்சியின் எண்ணிக்கை பலம்")
            ],
            "correct_key": "A",
            "exp_en": "Article 335 states that the claims of the members of the Scheduled Castes and the Scheduled Tribes shall be taken into consideration, consistently with the maintenance of efficiency of administration, in the making of appointments to services and posts.",
            "exp_ta": "சரத்து 335, அரசுப் பணிகளுக்கான நியமனங்களைச் செய்யும்போது, நிர்வாகத் திறனைப் பராமரிப்பதோடு முரண்படாமல், பட்டியலிடப்பட்ட சாதியினர் மற்றும் பழங்குடியினரின் கோரிக்கைகள் கருத்தில் கொள்ளப்பட வேண்டும் என்று கூறுகிறது.",
            "why_a_en": "Article 335 explicitly uses the phrase 'consistently with the maintenance of efficiency of administration'.",
            "why_a_ta": "சரத்து 335 'நிர்வாகத் திறனைப் பராமரிப்பதோடு முரண்படாமல்' என்ற சொற்றொடரைத் தெளிவாகப் பயன்படுத்துகிறது.",
            "why_b_en": "International conventions are governed under Article 51 and 253, not Art 335.",
            "why_b_ta": "சர்வதேச உடன்படிக்கைகள் சரத்து 51 மற்றும் 253-ன் கீழ் வருகின்றன.",
            "why_c_en": "PSU profit is an economic parameter, not a constitutional condition in Art 335.",
            "why_c_ta": "நிறுவன லாபம் என்பது பொருளாதார அளவுகோல், சரத்து 335-ன் நிபந்தனை அல்ல.",
            "why_d_en": "Political strength is irrelevant to constitutional merit and efficiency.",
            "why_d_ta": "அரசியல் பலம் அரசியலமைப்பு நிர்வாகத் திறனுடன் தொடர்பற்றது.",
            "tip_en": "The 82nd Amendment 2000 added a proviso to Art 335 allowing relaxation in qualifying marks or lowering evaluation standards for SC/ST.",
            "tip_ta": "2000-ன் 82வது திருத்தம் சரத்து 335-ல் ஒரு வரம்பைச் சேர்த்து SC/ST பிரிவினருக்கு தகுதி மதிப்பெண்களில் தளர்வு அளிக்க வழிவகை செய்தது.",
            "fact_en": "In B.K. Pavitra (II) (2019), the SC held that administrative efficiency must include inclusive social representation.",
            "fact_ta": "பவித்ரா வழக்கில் (2019), நிர்வாகத் திறன் என்பது உள்ளடக்கிய சமூகப் பிரதிநிதித்துவத்தையும் கொண்டிருக்க வேண்டும் என உச்ச நீதிமன்றம் தீர்ப்பளித்தது."
        },
        # 39
        {
            "subtopic": "Special Provisions Summary",
            "stem_en": "Which of the following pairings between Article and State is INCORRECT?",
            "stem_ta": "சரத்து மற்றும் மாநிலத்திற்கு இடையிலான பின்வரும் இணைகளில் எது தவறானது?",
            "options": [
                ("Article 371B — Manipur", "சரத்து 371B — மணிப்பூர்"),
                ("Article 371A — Nagaland", "சரத்து 371A — நாகாலாந்து"),
                ("Article 371F — Sikkim", "சரத்து 371F — சிக்கிம்"),
                ("Article 371G — Mizoram", "சரத்து 371G — மிசோரம்")
            ],
            "correct_key": "A",
            "exp_en": "Article 371B relates to Assam, while Article 371C relates to Manipur. Therefore, pairing Article 371B with Manipur is incorrect.",
            "exp_ta": "சரத்து 371B அசாம் மாநிலத்துடனும், சரத்து 371C மணிப்பூர் மாநிலத்துடனும் தொடர்புடையது. எனவே சரத்து 371B-ஐ மணிப்பூருடன் இணைப்பது தவறானது.",
            "why_a_en": "Article 371B applies to Assam, not Manipur (Article 371C is for Manipur).",
            "why_a_ta": "சரத்து 371B அசாமிற்கு பொருந்தும், மணிப்பூருக்கு அல்ல (மணிப்பூருக்கு 371C).",
            "why_b_en": "Article 371A correctly applies to Nagaland.",
            "why_b_ta": "சரத்து 371A நாகாலாந்திற்கு சரியாகப் பொருந்துகிறது.",
            "why_c_en": "Article 371F correctly applies to Sikkim.",
            "why_c_ta": "சரத்து 371F சிக்கிமிற்கு சரியாகப் பொருந்துகிறது.",
            "why_d_en": "Article 371G correctly applies to Mizoram.",
            "why_d_ta": "சரத்து 371G மிசோரமிற்கு சரியாகப் பொருந்துகிறது.",
            "tip_en": "Mnemonics for 371 series: 371 (MH & GJ), 371A (Nagaland), 371B (Assam), 371C (Manipur), 371D/E (AP/TG), 371F (Sikkim), 371G (Mizoram), 371H (Arunachal), 371I (Goa), 371J (Karnataka).",
            "tip_ta": "371 வரிசை சுருக்குவழி: 371 (MH & GJ), 371A (நாகாலாந்து), 371B (அசாம்), 371C (மணிப்பூர்), 371D/E (AP/TG), 371F (சிக்கிம்), 371G (மிசோரம்), 371H (அருணாச்சல்), 371I (கோவா), 371J (கர்நாடகா).",
            "fact_en": "All these special provisions are enshrined in Part XXI of the Indian Constitution.",
            "fact_ta": "இச்சிறப்பு ஏற்பாடுகள் அனைத்தும் இந்திய அரசியலமைப்பின் பகுதி XXI-ல் இணைக்கப்பட்டுள்ளன."
        },
        # 40
        {
            "subtopic": "Special Provisions Summary",
            "stem_en": "Which Article provides special provisions for the State of Arunachal Pradesh?",
            "stem_ta": "அருணாச்சலப் பிரதேச மாநிலத்திற்கு சிறப்பு ஏற்பாடுகளை வழங்கும் சரத்து எது?",
            "options": [
                ("Article 371H", "சரத்து 371H"),
                ("Article 371F", "சரத்து 371F"),
                ("Article 371G", "சரத்து 371G"),
                ("Article 371I", "சரத்து 371I")
            ],
            "correct_key": "A",
            "exp_en": "Article 371H, inserted by the 55th Amendment Act 1986, contains special provisions for Arunachal Pradesh, giving the Governor special responsibility regarding law and order.",
            "exp_ta": "1986-ன் 55வது திருத்தத்தால் சேர்க்கப்பட்ட சரத்து 371H, சட்டம் ஒழுங்கு தொடர்பாக ஆளுநருக்கு சிறப்புப் பொறுப்பை வழங்கி அருணாச்சலப் பிரதேசத்திற்கான சிறப்பு ஏற்பாடுகளைக் கொண்டுள்ளது.",
            "why_a_en": "Article 371H applies to Arunachal Pradesh.",
            "why_a_ta": "சரத்து 371H அருணாச்சலப் பிரதேசத்திற்குப் பொருந்தும்.",
            "why_b_en": "Article 371F applies to Sikkim.",
            "why_b_ta": "சரத்து 371F சிக்கிமிற்குப் பொருந்தும்.",
            "why_c_en": "Article 371G applies to Mizoram.",
            "why_c_ta": "சரத்து 371G மிசோரமிற்குப் பொருந்தும்.",
            "why_d_en": "Article 371I applies to Goa.",
            "why_d_ta": "சரத்து 371I கோவாவிற்குப் பொருந்தும்.",
            "tip_en": "Remember 'H' for 'High altitude/Himalayan' Arunachal Pradesh.",
            "tip_ta": "'H' என்பதை இமயமலை சார்ந்த அருணாச்சலப் பிரதேசம் என நினைவில் கொள்க.",
            "fact_en": "Arunachal Pradesh was formerly known as North-East Frontier Agency (NEFA).",
            "fact_ta": "அருணாச்சலப் பிரதேசம் முன்பு வடகிழக்கு எல்லைப்புற முகமை (NEFA) என அழைக்கப்பட்டது."
        },
        # 41
        {
            "subtopic": "Special Provisions Summary",
            "stem_en": "Article 371I relates to which of the following States of India?",
            "stem_ta": "சரத்து 371I இந்தியாவின் பின்வரும் எந்த மாநிலத்துடன் தொடர்புடையது?",
            "options": [
                ("Goa", "கோவா"),
                ("Sikkim", "சிக்கிம்"),
                ("Mizoram", "மிசோரம்"),
                ("Nagaland", "நாகாலாந்து")
            ],
            "correct_key": "A",
            "exp_en": "Article 371I relates to the State of Goa, stipulating that its Legislative Assembly shall consist of not less than thirty members.",
            "exp_ta": "சரத்து 371I கோவா மாநிலத்துடன் தொடர்புடையது; அதன் சட்டமன்றம் 30 உறுப்பினர்களுக்குக் குறையாமல் இருக்க வேண்டும் என்று கூறுகிறது.",
            "why_a_en": "Article 371I provides for Goa.",
            "why_a_ta": "சரத்து 371I கோவாவிற்கு வகைசெய்கிறது.",
            "why_b_en": "Article 371F provides for Sikkim.",
            "why_b_ta": "சரத்து 371F சிக்கிமிற்கு வகைசெய்கிறது.",
            "why_c_en": "Article 371G provides for Mizoram.",
            "why_c_ta": "சரத்து 371G மிசோரமிற்கு வகைசெய்கிறது.",
            "why_d_en": "Article 371A provides for Nagaland.",
            "why_d_ta": "சரத்து 371A நாகாலாந்திற்கு வகைசெய்கிறது.",
            "tip_en": "Goa gained statehood in 1987 via the 56th CAA inserting Article 371I.",
            "tip_ta": "1987-ன் 56வது திருத்தம் சரத்து 371I-ஐச் சேர்த்து கோவாவிற்கு மாநில அந்தஸ்தை அளித்தது.",
            "fact_en": "Goa was liberated from Portuguese rule on 19 December 1961 by Operation Vijay.",
            "fact_ta": "1961 டிசம்பர் 19 அன்று ஆபரேஷன் விஜய் மூலம் கோவா போர்த்துகீசிய ஆட்சியில் இருந்து விடுவிக்கப்பட்டது."
        },
        # 42
        {
            "subtopic": "Special Provisions Summary",
            "stem_en": "Article 371J contains special provisions for which State of India?",
            "stem_ta": "சரத்து 371J இந்தியாவின் எந்த மாநிலத்திற்கான சிறப்பு ஏற்பாடுகளைக் கொண்டுள்ளது?",
            "options": [
                ("Karnataka", "கர்நாடகா"),
                ("Andhra Pradesh", "ஆந்திரப் பிரதேசம்"),
                ("Maharashtra", "மகாராஷ்டிரா"),
                ("Assam", "அசாம்")
            ],
            "correct_key": "A",
            "exp_en": "Article 371J provides special provisions for the Hyderabad-Karnataka region of the State of Karnataka, inserted by the 98th Amendment Act 2012.",
            "exp_ta": "2012-ன் 98வது திருத்தத்தால் சேர்க்கப்பட்ட சரத்து 371J, கர்நாடக மாநிலத்தின் ஹைதராபாத்-கர்நாடகா பகுதிக்கு சிறப்பு ஏற்பாடுகளை வழங்குகிறது.",
            "why_a_en": "Article 371J relates to Karnataka.",
            "why_a_ta": "சரத்து 371J கர்நாடகாவுடன் தொடர்புடையது.",
            "why_b_en": "Andhra Pradesh is covered under Articles 371D and 371E.",
            "why_b_ta": "ஆந்திரப் பிரதேசம் சரத்துகள் 371D மற்றும் 371E-ன் கீழ் வருகிறது.",
            "why_c_en": "Maharashtra is covered under Article 371.",
            "why_c_ta": "மகாராஷ்டிரா சரத்து 371-ன் கீழ் வருகிறது.",
            "why_d_en": "Assam is covered under Article 371B.",
            "why_d_ta": "அசாம் சரத்து 371B-ன் கீழ் வருகிறது.",
            "tip_en": "Article 371J is the latest state-specific article in Part XXI (added in 2012).",
            "tip_ta": "பகுதி XXI-ல் மாநிலங்கள் தொடர்பாக கடைசியாக சேர்க்கப்பட்ட சரத்து 371J (2012-ல் சேர்க்கப்பட்டது).",
            "fact_en": "The region includes 6 backward districts with equitable reservation in educational institutions and state jobs.",
            "fact_ta": "இப்பகுதி 6 பின்தங்கிய மாவட்டங்களை உள்ளடக்கியது; கல்வி மற்றும் அரசு வேலைகளில் இடஒதுக்கீடு வழங்கப்படுகிறது."
        },
        # 43
        {
            "subtopic": "Special Provisions vs Schedules",
            "stem_en": "Which Schedule of the Indian Constitution provides for the administration and control of Scheduled Areas and Scheduled Tribes in states other than Assam, Meghalaya, Tripura, and Mizoram?",
            "stem_ta": "அசாம், மேகாலயா, திரிபுரா மற்றும் மிசோரம் தவிர்த்த பிற மாநிலங்களில் உள்ள அட்டவணைப் பகுதிகள் மற்றும் பழங்குடியினர் நிர்வாகத்தை வழங்கும் அரசியலமைப்பு அட்டவணை எது?",
            "options": [
                ("Fifth Schedule", "ஐந்தாவது அட்டவணை"),
                ("Sixth Schedule", "ஆறாவது அட்டவணை"),
                ("Seventh Schedule", "ஏழாவது அட்டவணை"),
                ("Eighth Schedule", "எட்டாவது அட்டவணை")
            ],
            "correct_key": "A",
            "exp_en": "The Fifth Schedule deals with the administration and control of Scheduled Areas and Scheduled Tribes in 10 states, excluding Assam, Meghalaya, Tripura, and Mizoram (which are covered under the Sixth Schedule).",
            "exp_ta": "ஐந்தாவது அட்டவணை அசாம், மேகாலயா, திரிபுரா, மிசோரம் தவிர்த்த 10 மாநிலங்களில் உள்ள அட்டவணைப் பகுதிகள் மற்றும் பழங்குடியினரின் நிர்வாகத்தைக் கையாள்கிறது.",
            "why_a_en": "Fifth Schedule applies to Scheduled Areas in states other than the four north-eastern states.",
            "why_a_ta": "ஐந்தாவது அட்டவணை 4 வடகிழக்கு மாநிலங்கள் தவிர்த்த பிற மாநிலங்களில் உள்ள அட்டவணைப் பகுதிகளுக்குப் பொருந்தும்.",
            "why_b_en": "Sixth Schedule deals exclusively with the four tribal states: Assam, Meghalaya, Tripura, and Mizoram (AMTM).",
            "why_b_ta": "ஆறாவது அட்டவணை 4 வடகிழக்கு மாநிலங்களுக்கு மட்டுமே (அசாம், மேகாலயா, திரிபுரா, மிசோரம்) பொருந்தும்.",
            "why_c_en": "Seventh Schedule deals with division of powers (Union, State, Concurrent Lists).",
            "why_c_ta": "ஏழாவது அட்டவணை அதிகாரப் பகிர்வைக் (மத்திய, மாநில, பொதுப் பட்டியல்கள்) கையாள்கிறது.",
            "why_d_en": "Eighth Schedule contains the 22 officially recognized languages.",
            "why_d_ta": "எட்டாவது அட்டவணை 22 அங்கீகரிக்கப்பட்ட மொழிகளைக் கொண்டுள்ளது.",
            "tip_en": "Fifth Schedule: Tribes Advisory Council (TAC) of max 20 members. Sixth Schedule: Autonomous District Councils (ADCs) of max 30 members.",
            "tip_ta": "5வது அட்டவணை: பழங்குடியினர் ஆலோசனைக் குழு (அதிகபட்சம் 20 பேர்). 6வது அட்டவணை: தன்னாட்சி மாவட்டக் குழுக்கள் (அதிகபட்சம் 30 பேர்).",
            "fact_en": "Presently, 10 states have Fifth Schedule areas: AP, Telangana, Jharkhand, Odisha, Chhattisgarh, MP, Rajasthan, Gujarat, Maharashtra, HP.",
            "fact_ta": "தற்போது 10 மாநிலங்கள் ஐந்தாவது அட்டவணைப் பகுதிகளைக் கொண்டுள்ளன."
        },
        # 44
        {
            "subtopic": "Sixth Schedule States",
            "stem_en": "Which four North-Eastern States are governed by the Autonomous District Councils under the Sixth Schedule?",
            "stem_ta": "ஆறாவது அட்டவணையின் கீழ் தன்னாட்சி மாவட்டக் குழுக்களால் நிர்வகிக்கப்படும் நான்கு வடகிழக்கு மாநிலங்கள் எவை?",
            "options": [
                ("Assam, Meghalaya, Tripura, Mizoram", "அசாம், மேகாலயா, திரிபுரா, மிசோரம்"),
                ("Nagaland, Manipur, Mizoram, Arunachal Pradesh", "நாகாலாந்து, மணிப்பூர், மிசோரம், அருணாச்சலப் பிரதேசம்"),
                ("Assam, Nagaland, Sikkim, Tripura", "அசாம், நாகாலாந்து, சிக்கிம், திரிபுரா"),
                ("Meghalaya, Manipur, Sikkim, Arunachal Pradesh", "மேகாலயா, மணிப்பூர், சிக்கிம், அருணாச்சலப் பிரதேசம்")
            ],
            "correct_key": "A",
            "exp_en": "The Sixth Schedule (Articles 244(2) and 275(1)) contains special provisions for the administration of tribal areas in the four states of Assam, Meghalaya, Tripura, and Mizoram (commonly abbreviated as AMTM).",
            "exp_ta": "ஆறாவது அட்டவணை (சரத்துகள் 244(2) மற்றும் 275(1)) அசாம், மேகாலயா, திரிபுரா மற்றும் மிசோரம் (AMTM) ஆகிய நான்கு மாநிலங்களில் உள்ள பழங்குடிப் பகுதிகளின் நிர்வாகத்தைக் கையாள்கிறது.",
            "why_a_en": "Assam, Meghalaya, Tripura, and Mizoram are the four Sixth Schedule states.",
            "why_a_ta": "அசாம், மேகாலயா, திரிபுரா மற்றும் மிசோரம் ஆகியவையே 6வது அட்டவணை மாநிலங்கள்.",
            "why_b_en": "Nagaland, Manipur and Arunachal Pradesh are not under the Sixth Schedule.",
            "why_b_ta": "நாகாலாந்து, மணிப்பூர் மற்றும் அருணாச்சலப் பிரதேசம் 6வது அட்டவணையில் இல்லை.",
            "why_c_en": "Sikkim and Nagaland are not in the Sixth Schedule.",
            "why_c_ta": "சிக்கிம் மற்றும் நாகாலாந்து 6வது அட்டவணையில் இல்லை.",
            "why_d_en": "Manipur and Sikkim are not in the Sixth Schedule.",
            "why_d_ta": "மணிப்பூர் மற்றும் சிக்கிம் 6வது அட்டவணையில் இல்லை.",
            "tip_en": "Mnemonic: AMTM -> Assam, Meghalaya, Tripura, Mizoram. Do NOT include Manipur or Nagaland!",
            "tip_ta": "சுருக்குவழி: AMTM -> அசாம், மேகாலயா, திரிபுரா, மிசோரம். மணிப்பூர் அல்லது நாகாலாந்தை சேர்க்காதீர்கள்!",
            "fact_en": "Sixth Schedule creates Autonomous District Councils (ADCs) with legislative, judicial, and executive powers.",
            "fact_ta": "ஆறாவது அட்டவணை சட்டமன்ற, நீதித்துறை மற்றும் நிர்வாக அதிகாரங்களுடன் கூடிய தன்னாட்சி மாவட்டக் குழுக்களை உருவாக்குகிறது."
        },
        # 45
        {
            "subtopic": "Special Provisions Architecture",
            "stem_en": "Special provisions in Article 371 to 371J were incorporated into the Indian Constitution primarily to:",
            "stem_ta": "இந்திய அரசியலமைப்பில் சரத்துகள் 371 முதல் 371J வரையிலான சிறப்பு ஏற்பாடுகள் முதன்மையாக எதற்காக இணைக்கப்பட்டன?",
            "options": [
                ("Meet regional aspirations, protect tribal customary interests, and address regional development disparities", "பிராந்திய விருப்பங்களை பூர்த்தி செய்யவும், பழங்குடியினரின் மரபுசார் நலன்களைப் பாதுகாக்கவும், பிராந்திய வளர்ச்சி ஏற்றத்தாழ்வுகளைக் களையவும்"),
                ("Uniformly centralize all state powers under the Union Cabinet", "மாநில அதிகாரங்கள் அனைத்தையும் மத்திய அமைச்சரவையின் கீழ் ஒரே சீராகக் குவிக்க"),
                ("Eliminate state legislative assemblies in border states", "எல்லை மாநிலங்களில் மாநில சட்டமன்றங்களை ஒழித்துக்கட்ட"),
                ("Establish military administration in northeastern states", "வடகிழக்கு மாநிலங்களில் ராணுவ நிர்வாகத்தை நிறுவ")
            ],
            "correct_key": "A",
            "exp_en": "The special provisions in Part XXI (Articles 371 to 371J) accommodate regional aspirations, protect tribal identity and customary laws, ensure law and order, and address economic disparities in backward regions.",
            "exp_ta": "பகுதி XXI-ன் (சரத்துகள் 371-371J) சிறப்பு ஏற்பாடுகள் பிராந்திய விருப்பங்களை பூர்த்தி செய்யவும், பழங்குடி அடையாளம் மற்றும் மரபுச் சட்டங்களைப் பாதுகாக்கவும், பின்தங்கிய பகுதிகளின் பொருளாதார ஏற்றத்தாழ்வுகளைக் களையவும் வகைசெய்கின்றன.",
            "why_a_en": "Article 371 series reflects asymmetrical federalism accommodating diversity and historical compacts.",
            "why_a_ta": "சரத்து 371 வரிசை பன்முகத்தன்மை மற்றும் வரலாற்று ஒப்பந்தங்களுக்கு ஏற்ப சமச்சீரற்ற கூட்டாட்சியைப் பிரதிபலிக்கிறது.",
            "why_b_en": "It decentralizes and accommodates rather than centralizes power.",
            "why_b_ta": "இது அதிகாரத்தைக் குவிப்பதற்குப் பதிலாக பரவலாக்கி இடமளிக்கிறது.",
            "why_c_en": "It preserves and empowers state assemblies (e.g. Nagaland, Mizoram approval requirements).",
            "why_c_ta": "இது சட்டமன்றங்களை பாதுகாத்து அதிகாரமளிக்கிறது.",
            "why_d_en": "It is a constitutional governance framework, not military administration.",
            "why_d_ta": "இது அரசியலமைப்பு ஆட்சி முறை, ராணுவ நிர்வாகம் அல்ல.",
            "tip_en": "This constitutional framework is termed 'Asymmetrical Federalism' by constitutional scholars.",
            "tip_ta": "இவ்வமைப்பு அரசியலமைப்பு அறிஞர்களால் 'சமச்சீரற்ற கூட்டாட்சி' என அழைக்கப்படுகிறது.",
            "fact_en": "12 states currently enjoy specialized protections under Article 371 to 371J.",
            "fact_ta": "தற்போது 12 மாநிலங்கள் சரத்து 371 முதல் 371J வரையிலான சிறப்புப் பாதுகாப்புகளைப் பெறுகின்றன."
        },
        # 46
        {
            "subtopic": "Article 371 Maharashtra and Gujarat",
            "stem_en": "Who has the power to issue an order under Article 371 providing for special responsibility of the Governor in Maharashtra and Gujarat?",
            "stem_ta": "மகாராஷ்டிரா மற்றும் குஜராத்தில் ஆளுநரின் சிறப்புப் பொறுப்பிற்கு வகைசெய்யும் உத்தரவை சரத்து 371-ன் கீழ் பிறப்பிக்கும் அதிகாரம் யாருக்கு உள்ளது?",
            "options": [
                ("The President of India", "இந்தியக் குடியரசுத் தலைவர்"),
                ("The Prime Minister of India", "இந்தியப் பிரதமர்"),
                ("The Chief Justice of India", "இந்தியத் தலைமை நீதிபதி"),
                ("The Parliament by a two-thirds majority", "நாடாளுமன்றம் மூன்றில் இரண்டு பங்கு பெரும்பான்மை மூலம்")
            ],
            "correct_key": "A",
            "exp_en": "Article 371 begins with: 'Notwithstanding anything in this Constitution, the President may by order made with respect to the State of Maharashtra or Gujarat, provide for any special responsibility of the Governor...'",
            "exp_ta": "சரத்து 371: 'இந்த அரசியலமைப்பில் என்ன கூறப்பட்டிருந்தாலும், குடியரசுத் தலைவர் மகாராஷ்டிரா அல்லது குஜராத் மாநிலம் தொடர்பாக பிறப்பிக்கும் உத்தரவின் மூலம் ஆளுநரின் சிறப்புப் பொறுப்பிற்கு வகைசெய்யலாம்...'",
            "why_a_en": "Article 371 specifically empowers the President to issue the order.",
            "why_a_ta": "சரத்து 371 குடியரசுத் தலைவருக்கு இந்த உத்தரவைப் பிறப்பிக்க அதிகாரம் அளிக்கிறது.",
            "why_b_en": "Prime Minister cannot issue constitutional presidential orders.",
            "why_b_ta": "பிரதமர் அரசியலமைப்பு குடியரசுத் தலைவர் ஆணைகளைப் பிறப்பிக்க முடியாது.",
            "why_c_en": "CJI has no executive order power under Art 371.",
            "why_c_ta": "தலைமை நீதிபதிக்கு சரத்து 371-ன் கீழ் நிர்வாக ஆணை அதிகாரம் இல்லை.",
            "why_d_en": "A presidential order suffices; parliamentary amendment is not required.",
            "why_d_ta": "குடியரசுத் தலைவர் ஆணை போதுமானது; நாடாளுமன்றத் திருத்தம் தேவையில்லை.",
            "tip_en": "Presidential orders under Art 371 are issued on the aid and advice of the Union Council of Ministers.",
            "tip_ta": "சரத்து 371-ன் கீழான குடியரசுத் தலைவர் ஆணைகள் மத்திய அமைச்சரவையின் ஆலோசனையின் பேரில் பிறப்பிக்கப்படுகின்றன.",
            "fact_en": "The Governor acts in his discretion in discharge of this special responsibility.",
            "fact_ta": "இச்சிறப்புப் பொறுப்பை நிறைவேற்றுவதில் ஆளுநர் தனது விருப்பப்படி செயல்படுகிறார்."
        },
        # 47
        {
            "subtopic": "Article 371F Sikkim",
            "stem_en": "Article 371F protects the existing laws in force in Sikkim immediately before its admission to the Union until:",
            "stem_ta": "ஒன்றியத்தில் இணைவதற்கு முன்பு சிக்கிமில் நடைமுறையில் இருந்த பழைய சட்டங்களை எதுவரை சரத்து 371F பாதுகாக்கிறது?",
            "options": [
                ("Amended or repealed by a competent Legislature or authority", "தகுதிவாய்ந்த சட்டமன்றம் அல்லது அதிகார அமைப்பால் திருத்தப்படும் வரை அல்லது ரத்து செய்யப்படும் வரை"),
                ("A period of exactly two years from the 36th Amendment", "36வது திருத்தத்திலிருந்து சரியாக இரண்டு ஆண்டுகள் வரை"),
                ("The President issues a proclamation of emergency", "குடியரசுத் தலைவர் அவசரகாலப் பிரகடனம் செய்யும் வரை"),
                ("The Governor of Sikkim dissolves the State Assembly", "சிக்கிம் ஆளுநர் மாநில சட்டமன்றத்தைக் கலைக்கும் வரை")
            ],
            "correct_key": "A",
            "exp_en": "Under Article 371F(k), all laws in force immediately before the appointed day in the territories comprised in Sikkim continue in force until altered, amended or repealed by a competent Legislature or other competent authority.",
            "exp_ta": "சரத்து 371F(k)-ன் படி, சிக்கிம் இணைவதற்கு முன்பு நடைமுறையில் இருந்த அனைத்து சட்டங்களும், தகுதிவாய்ந்த சட்டமன்றத்தால் அல்லது அதிகார அமைப்பால் மாற்றப்படும் வரை அல்லது ரத்து செய்யப்படும் வரை தொடர்ந்து நடைமுறையில் இருக்கும்.",
            "why_a_en": "Article 371F(k) explicitly states until altered, amended or repealed by a competent Legislature.",
            "why_a_ta": "சரத்து 371F(k) தகுதிவாய்ந்த சட்டமன்றத்தால் திருத்தப்படும் வரை அல்லது ரத்து செய்யப்படும் வரை நடைமுறையில் இருக்கும் எனக் கூறுகிறது.",
            "why_b_en": "There was no arbitrary two-year sunset clause for existing laws.",
            "why_b_ta": "பழைய சட்டங்களுக்கு இரண்டு ஆண்டு கால வரம்பு ஏதும் விதிக்கப்படவில்லை.",
            "why_c_en": "Emergency proclamation does not automatically repeal all pre-existing state laws.",
            "why_c_ta": "அவசரகாலப் பிரகடனம் தானாக பழைய சட்டங்களை ரத்து செய்யாது.",
            "why_d_en": "Assembly dissolution does not affect continuity of statutory laws.",
            "why_d_ta": "சட்டமன்றக் கலைப்பு சட்டங்களின் தொடர்ச்சியைப் பாதிக்காது.",
            "tip_en": "This transitional provision ensured legal continuity for Sikkim's local land and personal laws (including the Old Sikkim Laws).",
            "tip_ta": "இந்த இடைக்கால விதி சிக்கிமின் உள்ளூர் நில மற்றும் தனிநபர் சட்டங்களுக்கான சட்டத் தொடர்ச்சியை உறுதி செய்தது.",
            "fact_en": "Article 371F(l) also gave the President a 2-year power to adapt and modify existing Sikkim laws.",
            "fact_ta": "சரத்து 371F(l) குடியரசுத் தலைவருக்கு பழைய சிக்கிம் சட்டங்களைத் தழுவி மாற்றியமைக்க 2 ஆண்டு கால அதிகாரத்தை வழங்கியது."
        },
        # 48
        {
            "subtopic": "Article 330 to 342A Architecture",
            "stem_en": "Which Article provides for the appointment of a Special Officer for Linguistic Minorities by the President?",
            "stem_ta": "மொழியியல் சிறுபான்மையினருக்கான சிறப்பு அதிகாரியை குடியரசுத் தலைவர் நியமிக்க வகைசெய்யும் சரத்து எது?",
            "options": [
                ("Article 350B", "சரத்து 350B"),
                ("Article 350A", "சரத்து 350A"),
                ("Article 338", "சரத்து 338"),
                ("Article 339", "சரத்து 339")
            ],
            "correct_key": "A",
            "exp_en": "Article 350B (inserted by the 7th Constitutional Amendment Act, 1956) provides for a Special Officer for Linguistic Minorities to be appointed by the President.",
            "exp_ta": "சரத்து 350B (1956-ன் 7வது அரசியலமைப்புத் திருத்தச் சட்டத்தால் சேர்க்கப்பட்டது) மொழியியல் சிறுபான்மையினருக்கான சிறப்பு அதிகாரியை குடியரசுத் தலைவர் நியமிக்க வகைசெய்கிறது.",
            "why_a_en": "Article 350B establishes the Special Officer for Linguistic Minorities.",
            "why_a_ta": "சரத்து 350B மொழியியல் சிறுபான்மையினருக்கான சிறப்பு அதிகாரியை அமைக்கிறது.",
            "why_b_en": "Article 350A mandates facilities for instruction in mother-tongue at primary stage.",
            "why_b_ta": "சரத்து 350A தொடக்கக் கல்வி நிலையில் தாய்மொழியில் கற்பிப்பதற்கான வசதிகளைக் கட்டாயமாக்குகிறது.",
            "why_c_en": "Article 338 establishes the NCSC.",
            "why_c_ta": "சரத்து 338 NCSC-ஐ அமைக்கிறது.",
            "why_d_en": "Article 339 deals with Union control over the administration of Scheduled Areas and welfare of STs.",
            "why_d_ta": "சரத்து 339 அட்டவணைப் பகுதிகள் நிர்வாகம் மற்றும் ST நலன் மீதான மத்திய அரசின் கட்டுப்பாட்டைக் கூறுகிறது.",
            "tip_en": "The Commissioner for Linguistic Minorities (CLM) submits annual reports to the President, which are laid before Parliament.",
            "tip_ta": "மொழியியல் சிறுபான்மையினருக்கான ஆணையர் குடியரசுத் தலைவருக்கு ஆண்டு அறிக்கைகளை சமர்ப்பிக்கிறார், அவை நாடாளுமன்றத்தில் வைக்கப்படுகின்றன.",
            "fact_en": "The headquarters of the Commissioner for Linguistic Minorities is located at Prayagraj (Allahabad).",
            "fact_ta": "மொழியியல் சிறுபான்மையினருக்கான ஆணையரின் தலைமையகம் பிரயாக்ராஜில் (அலகாபாத்) அமைந்துள்ளது."
        },
        # 49
        {
            "subtopic": "Article 339 Scheduled Areas Administration",
            "stem_en": "Under Article 339(1), the President may at any time, and shall at the expiration of ten years from the commencement of the Constitution, appoint a Commission to report on:",
            "stem_ta": "சரத்து 339(1)-ன் கீழ், குடியரசுத் தலைவர் எந்த நேரத்திலும், அரசியலமைப்பு தொடங்கிய பத்தாண்டுகள் முடிவிலும் எதைப் பற்றி அறிக்கை அளிக்க ஓர் ஆணையத்தை நியமிக்க வேண்டும்?",
            "options": [
                ("The administration of the Scheduled Areas and the welfare of the Scheduled Tribes", "அட்டவணைப் பகுதிகளின் நிர்வாகம் மற்றும் பட்டியலிடப்பட்ட பழங்குடியினரின் நலன்"),
                ("The working of the official language in central courts", "மத்திய நீதிமன்றங்களில் அதிகாரப்பூர்வ மொழியின் செயல்பாடு"),
                ("The financial viability of union territories", "யூனியன் பிரதேசங்களின் நிதி நிலைத்தன்மை"),
                ("The delimitation of parliamentary constituencies", "நாடாளுமன்றத் தொகுதிகளின் மறுவரையறை")
            ],
            "correct_key": "A",
            "exp_en": "Article 339(1) empowers the President to appoint a Commission to report on the administration of the Scheduled Areas and the welfare of the Scheduled Tribes in the States.",
            "exp_ta": "சரத்து 339(1) மாநிலங்களில் உள்ள அட்டவணைப் பகுதிகளின் நிர்வாகம் மற்றும் பட்டியலிடப்பட்ட பழங்குடியினரின் நலன் குறித்து அறிக்கை அளிக்க ஆணையத்தை நியமிக்க குடியரசுத் தலைவருக்கு அதிகாரம் அளிக்கிறது.",
            "why_a_en": "Article 339(1) explicitly specifies the administration of Scheduled Areas and welfare of STs.",
            "why_a_ta": "சரத்து 339(1) அட்டவணைப் பகுதிகளின் நிர்வாகம் மற்றும் ST நலனை தெளிவாகக் குறிப்பிடுகிறது.",
            "why_b_en": "Official language commissions are appointed under Article 344.",
            "why_b_ta": "அதிகாரப்பூர்வ மொழி ஆணையங்கள் சரத்து 344-ன் கீழ் நியமிக்கப்படுகின்றன.",
            "why_c_en": "UT financial viability is not under Article 339.",
            "why_c_ta": "யூனியன் பிரதேச நிதி விவகாரங்கள் சரத்து 339-ன் கீழ் வராது.",
            "why_d_en": "Delimitation is carried out under Article 82.",
            "why_d_ta": "தொகுதி மறுவரையறை சரத்து 82-ன் கீழ் மேற்கொள்ளப்படுகிறது.",
            "tip_en": "Famous commissions appointed under Art 339: U.N. Dhebar Commission (1960) and Dilip Singh Bhuria Commission (2002).",
            "tip_ta": "சரத்து 339-ன் கீழ் நியமிக்கப்பட்ட புகழ்பெற்ற ஆணையங்கள்: யு.என். தேபர் ஆணையம் (1960) மற்றும் திலீப் சிங் பூரியா ஆணையம் (2002).",
            "fact_en": "The recommendations of the Bhuria Commission led directly to the enactment of the PESA Act 1996.",
            "fact_ta": "பூரியா ஆணையத்தின் பரிந்துரைகள் 1996 PESA சட்டம் இயற்றப்படுவதற்கு நேரடியாக வழிவகுத்தன."
        },
        # 50
        {
            "subtopic": "Article 371 to 371J Synthesis",
            "stem_en": "Which of the following Articles was inserted most recently into Part XXI of the Indian Constitution?",
            "stem_ta": "இந்திய அரசியலமைப்பின் பகுதி XXI-ல் மிக சமீபத்தில் சேர்க்கப்பட்ட சரத்து எது?",
            "options": [
                ("Article 371J (Karnataka)", "சரத்து 371J (கர்நாடகா)"),
                ("Article 371I (Goa)", "சரத்து 371I (கோவா)"),
                ("Article 371H (Arunachal Pradesh)", "சரத்து 371H (அருணாச்சலப் பிரதேசம்)"),
                ("Article 371G (Mizoram)", "சரத்து 371G (மிசோரம்)")
            ],
            "correct_key": "A",
            "exp_en": "Article 371J was inserted by the 98th Constitutional Amendment Act, 2012 (effective 2013), making it the most recently added article in the Article 371 special provisions series.",
            "exp_ta": "சரத்து 371J, 2012-ன் 98வது அரசியலமைப்புத் திருத்தச் சட்டம் மூலம் (2013 முதல் நடைமுறைக்கு வந்தது) சேர்க்கப்பட்டது. இதுவே சரத்து 371 சிறப்பு ஏற்பாடுகள் வரிசையில் மிக சமீபத்தில் சேர்க்கப்பட்ட சரத்தாகும்.",
            "why_a_en": "Article 371J was added in 2012 (98th CAA), later than all other articles in Part XXI.",
            "why_a_ta": "சரத்து 371J 2012-ல் (98வது திருத்தம்) சேர்க்கப்பட்டது, இது மற்ற அனைத்து சரத்துகளையும் விட பிந்தையது.",
            "why_b_en": "Article 371I was added in 1987 (56th CAA).",
            "why_b_ta": "சரத்து 371I 1987-ல் (56வது திருத்தம்) சேர்க்கப்பட்டது.",
            "why_c_en": "Article 371H was added in 1986 (55th CAA).",
            "why_c_ta": "சரத்து 371H 1986-ல் (55வது திருத்தம்) சேர்க்கப்பட்டது.",
            "why_d_en": "Article 371G was added in 1986 (53rd CAA).",
            "why_d_ta": "சரத்து 371G 1986-ல் (53வது திருத்தம்) சேர்க்கப்பட்டது.",
            "tip_en": "Chronological order of insertions: 371A (1962) -> 371B (1969) -> 371C (1971) -> 371D/E (1973) -> 371F (1975) -> 371G (1986) -> 371H (1986) -> 371I (1987) -> 371J (2012).",
            "tip_ta": "சேர்க்கப்பட்ட காலவரிசை: 371A (1962) -> 371B (1969) -> 371C (1971) -> 371D/E (1973) -> 371F (1975) -> 371G (1986) -> 371H (1986) -> 371I (1987) -> 371J (2012).",
            "fact_en": "Article 370 previously contained temporary provisions for Jammu and Kashmir, abrogated in August 2019.",
            "fact_ta": "முன்னர் சரத்து 370 ஜம்மு-காஷ்மீருக்கான தற்காலிக ஏற்பாடுகளைக் கொண்டிருந்தது, இது 2019 ஆகஸ்டில் நீக்கப்பட்டது."
        }
    ]

    questions = []
    for idx, item in enumerate(raw, start=1):
        qid = f"SPS_E_{idx:03d}"
        opts = item["options"]
        q = make_sps_q(
            qid=qid,
            diff="Easy",
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
            tags=["polity", "special_provisions_states", "easy", item["subtopic"].lower().replace(" ", "_")]
        )
        questions.append(q)
    return questions

def build_easy_file():
    qs = get_easy_questions()
    print(f"Generated {len(qs)} raw Easy questions for Special Provisions for States.")
    balanced = randomize_and_balance_dataset(qs, seed=42)
    
    out_dir = os.path.join("data", "questions", "polity")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "special_provisions_states_easy.json")
    
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(balanced, f, ensure_ascii=False, indent=2)
    print(f"Saved balanced Easy MCQs to {out_path}")
    
    rep = ContentValidator.validate_file(out_path, expected_count=50, expected_prefix="SPS_E_")
    print(f"Validation: {'PASS' if rep.is_valid else 'FAIL'} | Total: {rep.total_audited}")
    print(f"Keys: {rep.key_distribution}")
    if not rep.is_valid:
        for iss in rep.issues:
            print("  Issue:", iss.severity, iss.field_name, iss.message)
    return rep.is_valid

if __name__ == "__main__":
    success = build_easy_file()
    if not success:
        exit(1)
