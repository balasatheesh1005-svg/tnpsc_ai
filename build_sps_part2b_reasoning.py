# -*- coding: utf-8 -*-
"""
Special Provisions for States - Part 2B Reasoning MCQs Generator (25 MCQs: SPS_R_001 to SPS_R_025)
Strictly adheres to:
- 24 required fields schema
- Assertion (A) and Reason (R) structure
- Authentic Tamil translations
- Specific why_not_others for A, B, C, D
- Balanced answer keys (6-7 per option)
- ContentValidator & Audit pass
"""
import json
import os
from special_provisions_states_mcq_helper import make_sps_q
from tools.nova_content_engine.answer_randomizer import randomize_and_balance_dataset
from tools.nova_content_engine.validator import ContentValidator

def get_reasoning_questions():
    raw_data = [
        # 1
        {
            "subtopic": "Part XXI Title Nature",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): The title of Part XXI of the Constitution was amended in 1962 to include the word 'Special'.\nReason (R): Article 371A was inserted by the 13th Amendment Act to grant permanent constitutional protections for the customary laws and identity of Nagaland.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): பகுதி XXI-ன் தலைப்பு 1962-ல் 'சிறப்பு' என்ற வார்த்தையை உள்ளடக்கும் வகையில் திருத்தப்பட்டது.\nகாரணம் (R): நாகாலாந்தின் மரபுச் சட்டங்கள் மற்றும் அடையாளத்திற்கு நிரந்தர அரசியலமைப்புப் பாதுகாப்புகளை வழங்க 13வது திருத்தச் சட்டம் மூலம் சரத்து 371A சேர்க்கப்பட்டது.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) is the correct explanation of (A). Part XXI originally covered 'Temporary and Transitional Provisions'. When permanent safeguards were introduced for Nagaland via Article 371A by the 13th Amendment 1962, the words 'and Special' were added to the title to reflect its expanded permanent character.",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம். பகுதி XXI முதலில் 'தற்காலிக மற்றும் இடைமாற்ற ஏற்பாடுகளை' மட்டுமே கொண்டிருந்தது. 13வது திருத்தம் 1962 மூலம் சரத்து 371A-வின் கீழ் நாகாலாந்திற்கு நிரந்தரப் பாதுகாப்புகள் வழங்கப்பட்டபோது, அதன் தன்மையைப் பிரதிபலிக்க தலைப்பில் 'மற்றும் சிறப்பு' என்ற சொற்கள் சேர்க்கப்பட்டன.",
            "why_a_en": "Both statements are factually accurate and R logically justifies the textual change in A.",
            "why_a_ta": "இரண்டு கூற்றுகளும் உண்மையானவை மற்றும் R என்பது A-ல் உள்ள தலைப்பு மாற்றத்தை தர்க்கரீதியாக விளக்குகிறது.",
            "why_b_en": "R is indeed the direct historical explanation for A.",
            "why_b_ta": "R என்பது உண்மையில் A-க்கான நேரடி வரலாற்று விளக்கம் ஆகும்.",
            "why_c_en": "R is true.",
            "why_c_ta": "R உண்மை.",
            "why_d_en": "A is true.",
            "why_d_ta": "A உண்மை.",
            "tip_en": "The 13th Constitutional Amendment Act, 1962 altered the chapter title permanently.",
            "tip_ta": "13வது அரசியலமைப்பு திருத்தச் சட்டம் 1962 அத்தியாயத்தின் தலைப்பை நிரந்தரமாக மாற்றியது.",
            "fact_en": "Before 1962, Part XXI was strictly understood as an impermanent transitional chapter.",
            "fact_ta": "1962-க்கு முன்பு பகுதி XXI முற்றிலும் தற்காலிக இடைக்கால அத்தியாயமாக மட்டுமே புரிந்து கொள்ளப்பட்டது."
        },
        # 2
        {
            "subtopic": "Article 371 Development Boards Governor",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Under Article 371(2), the Governor of Maharashtra has a special responsibility for setting up development boards for Vidarbha and Marathwada.\nReason (R): In discharging this special responsibility, the Governor is not bound to act on the aid and advice of the Council of Ministers.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): சரத்து 371(2)-ன் கீழ், விதர்பா மற்றும் மராத்வாடாவிற்கு வளர்ச்சி வாரியங்களை அமைப்பதில் மகாராஷ்டிர ஆளுநருக்குச் சிறப்புப் பொறுப்பு உண்டு.\nகாரணம் (R): இந்தச் சிறப்புப் பொறுப்பை நிறைவேற்றுவதில், ஆளுநர் அமைச்சரவையின் உதவி மற்றும் ஆலோசனையின்படி செயல்படக் கட்டுப்பட்டவர் அல்ல.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "B",
            "exp_en": "Both (A) and (R) are true, but (R) is not the causal explanation of (A). (A) describes the substantive constitutional provision under Article 371(2), while (R) correctly states the legal principle affirmed by the Supreme Court that 'special responsibility' entails personal discretion subject to Presidential directions, independent of the ministry. (R) states the nature of power, not why the provision was created.",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல. (A) சரத்து 371(2)-ன் கீழான அரசியலமைப்பு விதியை விவரிக்கிறது. 'சிறப்புப் பொறுப்பு' என்பது குடியரசுத் தலைவரின் உத்தரவுகளுக்கு உட்பட்டு அமைச்சரவையின் ஆலோசனையைச் சாராமல் ஆளுநர் தனிப்பட்ட விருப்புரிமையுடன் செயல்படுவதைக் குறிக்கிறது என்று (R) சரியாகக் கூறுகிறது. ஆனால் இது A உருவாக்கப்பட்டதற்கான காரணம் அல்ல.",
            "why_a_en": "R explains the constitutional nature of the Governor's power, but not the historical/substantive reason for creating development boards in A.",
            "why_a_ta": "R என்பது ஆளுநரின் அதிகாரத்தின் தன்மையை விளக்குகிறது, ஆனால் A-ல் வளர்ச்சி வாரியங்கள் உருவாக்கப்பட்டதற்கான காரணமல்ல.",
            "why_b_en": "Both statements are independently true as per constitutional jurisprudence.",
            "why_b_ta": "அரசியலமைப்பு சட்டக் கோட்பாட்டின்படி இரண்டு கூற்றுகளும் தனித்தனியாக சரியானவை.",
            "why_c_en": "R is true as held by the Supreme Court in Shamsher Singh case.",
            "why_c_ta": "ஷம்ஷேர் சிங் வழக்கில் உச்ச நீதிமன்றம் கூறியபடி R சரியானது.",
            "why_d_en": "A is true under Art 371(2).",
            "why_d_ta": "சரத்து 371(2)-ன் படி A உண்மை.",
            "tip_en": "Where the Constitution confers 'special responsibility', the Governor acts in individual judgment.",
            "tip_ta": "அரசியலமைப்பு 'சிறப்புப் பொறுப்பை' வழங்கும் இடங்களில் ஆளுநர் தனது தனிப்பட்ட முடிவின்படி செயல்படுகிறார்.",
            "fact_en": "The development boards were created to redress regional imbalances in Maharashtra and Gujarat.",
            "fact_ta": "மகாராஷ்டிரா மற்றும் குஜராத்தில் பிராந்திய ஏற்றத்தாழ்வுகளைக் களைய வளர்ச்சி வாரியங்கள் உருவாக்கப்பட்டன."
        },
        # 3
        {
            "subtopic": "Article 371A Parliamentary Immunity",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Central laws regarding ownership and transfer of land in Nagaland do not automatically apply to the State.\nReason (R): Under Article 371A, an Act of Parliament on land ownership applies to Nagaland only if the State Legislative Assembly so decides by a resolution.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): நாகாலாந்தில் நிலத்தின் உரிமை மற்றும் பரிமாற்றம் தொடர்பான மத்திய சட்டங்கள் தானாகவே மாநிலத்திற்குப் பொருந்தாது.\nகாரணம் (R): சரத்து 371A-ன் கீழ், நில உரிமை தொடர்பான நாடாளுமன்றச் சட்டம் மாநில சட்டமன்றம் தீர்மானம் நிறைவேற்றினால் மட்டுமே நாகாலாந்திற்குப் பொருந்தும்.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) is the exact constitutional explanation of (A). Article 371A(1)(a)(iv) explicitly conditions the application of Parliamentary legislation regarding ownership and transfer of land upon a resolution passed by the Nagaland Legislative Assembly.",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம். சரத்து 371A(1)(a)(iv) நிலத்தின் உரிமை மற்றும் பரிமாற்றம் தொடர்பான நாடாளுமன்ற சட்டங்கள் நாகாலாந்து சட்டமன்றத்தில் தீர்மானம் நிறைவேற்றப்பட்ட பின்னரே பொருந்தும் என வெளிப்படையாகக் கட்டாயமாக்குகிறது.",
            "why_a_en": "R directly cites the constitutional mechanism that causes and explains A.",
            "why_a_ta": "R என்பது A-ஐ உருவாக்கும் மற்றும் விளக்கும் அரசியலமைப்பு வழிமுறையை நேரடியாகக் குறிப்பிடுகிறது.",
            "why_b_en": "R is the direct explanation of A.",
            "why_b_ta": "R என்பது A-ன் நேரடி விளக்கம் ஆகும்.",
            "why_c_en": "R is true.",
            "why_c_ta": "R உண்மை.",
            "why_d_en": "A is true.",
            "why_d_ta": "A உண்மை.",
            "tip_en": "Article 371A gives the Nagaland Assembly a legislative veto over specific central laws.",
            "tip_ta": "சரத்து 371A குறிப்பிட்ட மத்திய சட்டங்கள் மீது நாகாலாந்து சட்டமன்றத்திற்கு ஒரு சட்டமன்ற வீட்டோ அதிகாரத்தை வழங்குகிறது.",
            "fact_en": "A similar safeguard on land and customary practices exists for Mizoram under Article 371G.",
            "fact_ta": "மிசோரமிற்கும் சரத்து 371G-ன் கீழ் நிலம் மற்றும் மரபு நடைமுறைகள் மீது இதே போன்ற பாதுகாப்பு உள்ளது."
        },
        # 4
        {
            "subtopic": "Article 371B Assam Sixth Schedule Distinction",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Article 371B applies to the whole State of Assam including the Brahmaputra Valley.\nReason (R): Article 371B provides for a committee of the Assam Legislative Assembly consisting of members elected from tribal areas.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): சரத்து 371B பிரம்மபுத்திரா பள்ளத்தாக்கு உட்பட முழு அசாம் மாநிலத்திற்கும் பொருந்தும்.\nகாரணம் (R): சரத்து 371B பழங்குடியினர் பகுதிகளிலிருந்து தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்களைக் கொண்ட அசாம் சட்டமன்றக் குழுவிற்கு வகை செய்கிறது.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை."),
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு.")
            ],
            "correct_key": "A",
            "exp_en": "Assertion (A) is false because Article 371B specifically focuses on the tribal areas of Assam (specified in Part I of the table to paragraph 20 of the Sixth Schedule), not the general administration of the whole state or Brahmaputra Valley. Reason (R) is true as it correctly defines the scope of the committee under Article 371B.",
            "exp_ta": "கூற்று (A) தவறானது, ஏனெனில் சரத்து 371B பிரம்மபுத்திரா பள்ளத்தாக்கு அல்லது முழு மாநிலப் பொது நிர்வாகத்திற்கானதல்ல, ஆறாவது அட்டவணையின் பத்தி 20-ல் குறிப்பிடப்பட்டுள்ள அசாமின் பழங்குடியினர் பகுதிகளை மட்டுமே மையமாகக் கொண்டது. காரணம் (R) சரத்து 371B-ன் கீழ் குழுவின் நோக்கத்தைச் சரியாக வரையறுப்பதால் உண்மை.",
            "why_a_en": "A is false because 371B is specialized for tribal areas; R is an accurate statement of Art 371B.",
            "why_a_ta": "371B பழங்குடியினர் பகுதிகளுக்கான சிறப்பு விதியாகும் என்பதால் A தவறு; R என்பது சரத்து 371B-ன் துல்லியமான கூற்று.",
            "why_b_en": "A is false.",
            "why_b_ta": "A தவறானது.",
            "why_c_en": "A is false.",
            "why_c_ta": "A தவறானது.",
            "why_d_en": "A is false and R is true.",
            "why_d_ta": "A தவறு மற்றும் R உண்மை.",
            "tip_en": "Watch out for statements claiming special tribal articles apply uniformly across general non-tribal areas.",
            "tip_ta": "பழங்குடியினருக்கான சிறப்பு சரத்துகள் பொதுவான பழங்குடியினர் அல்லாத பகுதிகளுக்கும் பொருந்தும் என்ற கூற்றுகளை கவனியுங்கள்.",
            "fact_en": "Assam's tribal areas under 371B currently include Karbi Anglong, Dima Hasao, and Bodoland.",
            "fact_ta": "371B-ன் கீழ் அசாமின் பழங்குடியினர் பகுதிகள் தற்போது கர்பி அங்லாங், திமா ஹசாவோ மற்றும் போடோலாந்து ஆகியவற்றை உள்ளடக்கியது."
        },
        # 5
        {
            "subtopic": "Article 371C Manipur Union Directions",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): The Union Government can issue binding executive directions to Manipur regarding the administration of the Hill Areas.\nReason (R): Under Article 371C(2), the executive power of the Union extends to giving directions to the State of Manipur as to the administration of the Hill Areas.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): மலைப்பகுதிகளின் நிர்வாகம் தொடர்பாக மணிப்பூருக்கு மத்திய அரசு கட்டுப்படுத்தும் நிர்வாக வழிகாட்டுதல்களை வழங்க முடியும்.\nகாரணம் (R): சரத்து 371C(2)-ன் கீழ், மணிப்பூர் மலைப்பகுதிகளின் நிர்வாகம் குறித்து மாநிலத்திற்கு வழிகாட்டுதல்களை வழங்க ஒன்றியத்தின் நிர்வாக அதிகாரம் நீட்டிக்கப்படுகிறது.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) directly explains (A). Article 371C(2) specifically provides that the executive power of the Union extends to the giving of directions to the State Government as to the administration of the Hill Areas, making Union directives legally binding.",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம். சரத்து 371C(2) மலைப்பகுதிகளின் நிர்வாகம் குறித்து மாநில அரசுக்கு வழிகாட்டுதல்களை வழங்க ஒன்றியத்தின் நிர்வாக அதிகாரம் நீட்டிக்கப்படுகிறது என்று வெளிப்படையாகக் கூறுவதால் மத்திய அரசின் வழிகாட்டுதல்கள் சட்டப்பூர்வமாக கட்டுப்படுத்துகின்றன.",
            "why_a_en": "R is the exact constitutional authorization that gives the Union executive direction powers in A.",
            "why_a_ta": "R என்பது A-ல் உள்ள ஒன்றிய நிர்வாக வழிகாட்டுதல் அதிகாரங்களை வழங்கும் சரியான அரசியலமைப்பு விதியாகும்.",
            "why_b_en": "R is the direct explanation of A.",
            "why_b_ta": "R என்பது A-ன் நேரடி விளக்கம்.",
            "why_c_en": "R is true.",
            "why_c_ta": "R உண்மை.",
            "why_d_en": "A is true.",
            "why_d_ta": "A உண்மை.",
            "tip_en": "Article 371C is one of the rare constitutional provisions explicitly expanding Union executive power over state subjects.",
            "tip_ta": "மாநிலப் பாடங்கள் மீது ஒன்றிய நிர்வாக அதிகாரத்தை வெளிப்படையாக விரிவாக்கும் அரிய அரசியலமைப்பு விதிகளில் சரத்து 371C ஒன்றாகும்.",
            "fact_en": "Non-compliance with such directions could attract Article 365 (President's Rule).",
            "fact_ta": "இத்தகைய வழிகாட்டுதல்களைப் பின்பற்றத் தவறினால் சரத்து 365 (குடியரசுத் தலைவர் ஆட்சி) ஈர்க்கப்படலாம்."
        },
        # 6
        {
            "subtopic": "Article 371D Clause 5 Judicial Review",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): The Supreme Court struck down Article 371D, clause (5) in the P. Sambamurthy case (1987).\nReason (R): Judicial review is a basic feature of the Constitution and no executive government can be given the power to annul orders of a judicial tribunal.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): பி. சாம்பமூர்த்தி வழக்கில் (1987) சரத்து 371D, பிரிவு (5)-ஐ உச்ச நீதிமன்றம் ரத்து செய்தது.\nகாரணம் (R): நீதித்துறை மறுஆய்வு என்பது அரசியலமைப்பின் அடிப்படைக் கட்டமைப்பாகும், மேலும் ஒரு நீதித்துறை தீர்ப்பாயத்தின் உத்தரவுகளை ரத்து செய்யும் அதிகாரத்தை எந்தவொரு நிர்வாக அரசுக்கும் வழங்க முடியாது.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) is the constitutional rationale for (A). In P. Sambamurthy (1987), the Supreme Court struck down clause (5) because giving the state government the power to annul the Administrative Tribunal's decisions violated judicial review and the rule of law.",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம். பி. சாம்பமூர்த்தி (1987) வழக்கில், நிர்வாகத் தீர்ப்பாயத்தின் முடிவுகளை ரத்து செய்ய மாநில அரசுக்கு அதிகாரம் அளிப்பது நீதித்துறை மறுஆய்வு மற்றும் சட்டத்தின் ஆட்சியை மீறுவதாகும் என்பதால் பிரிவு (5)-ஐ உச்ச நீதிமன்றம் ரத்து செய்தது.",
            "why_a_en": "R gives the exact constitutional foundation on which the Supreme Court based its ruling in A.",
            "why_a_ta": "A-ல் உச்ச நீதிமன்றம் தனது தீர்ப்பை அடிப்படையாகக் கொண்ட சரியான அரசியலமைப்பு காரணத்தை R வழங்குகிறது.",
            "why_b_en": "R directly explains A.",
            "why_b_ta": "R நேரடியாக A-வை விளக்குகிறது.",
            "why_c_en": "R is true.",
            "why_c_ta": "R உண்மை.",
            "why_d_en": "A is true.",
            "why_d_ta": "A உண்மை.",
            "tip_en": "This verdict applied the Basic Structure Doctrine established in Kesavananda Bharati (1973).",
            "tip_ta": "இத்தீர்ப்பு கேசவானந்த பாரதி (1973) வழக்கில் நிறுவப்பட்ட அடிப்படைக் கட்டமைப்புக் கோட்பாட்டைப் பயன்படுத்தியது.",
            "fact_en": "The remainder of Article 371D was held severable and survived the invalidation.",
            "fact_ta": "சரத்து 371D-ன் மீதமுள்ள பகுதிகள் பிரிக்கக்கூடியதாகக் கருதப்பட்டு செல்லுபடியாகும் நிலையில் நீடித்தன."
        },
        # 7
        {
            "subtopic": "Article 371D Telangana Continuation",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Article 371D continues to apply to both Andhra Pradesh and Telangana even after the bifurcation in 2014.\nReason (R): The Andhra Pradesh Reorganisation Act, 2014 amended Article 371D to substitute 'State of Andhra Pradesh and the State of Telangana' for 'State of Andhra Pradesh'.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): 2014-ல் பிரிக்கப்பட்ட பின்னரும் சரத்து 371D ஆந்திரப் பிரதேசம் மற்றும் தெலங்கானா ஆகிய இரண்டு மாநிலங்களுக்கும் தொடர்ந்து பொருந்துகிறது.\nகாரணம் (R): ஆந்திரப் பிரதேச மறுசீரமைப்புச் சட்டம், 2014 சரத்து 371D-ல் 'ஆந்திரப் பிரதேச மாநிலம்' என்பதற்குப் பதிலாக 'ஆந்திரப் பிரதேச மாநிலம் மற்றும் தெலங்கானா மாநிலம்' என மாற்றியமைத்தது.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) explains why (A) remains legally operative. Section 97 of the Andhra Pradesh Reorganisation Act, 2014 expressly amended Article 371D to include both successor States.",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A) ஏன் சட்டப்பூர்வமாக நீடிக்கிறது என்பதை விளக்குகிறது. ஆந்திரப் பிரதேச மறுசீரமைப்புச் சட்டம் 2014-ன் பிரிவு 97, இரண்டு மாநிலங்களையும் உள்ளடக்கும் வகையில் சரத்து 371D-ஐ வெளிப்படையாகத் திருத்தியது.",
            "why_a_en": "R provides the statutory amendment mechanism that caused A.",
            "why_a_ta": "R என்பது A-வை ஏற்படுத்திய சட்டப்பூர்வ திருத்த வழிமுறையை வழங்குகிறது.",
            "why_b_en": "R directly explains A.",
            "why_b_ta": "R நேரடியாக A-வை விளக்குகிறது.",
            "why_c_en": "R is true.",
            "why_c_ta": "R உண்மை.",
            "why_d_en": "A is true.",
            "why_d_ta": "A உண்மை.",
            "tip_en": "Parliament used its power under Article 4 to adapt constitutional provisions during state reorganisation.",
            "tip_ta": "மாநில மறுசீரமைப்பின் போது அரசியலமைப்பு விதிகளை மாற்றியமைக்க சரத்து 4-ன் கீழ் உள்ள அதிகாரத்தை நாடாளுமன்றம் பயன்படுத்தியது.",
            "fact_en": "Telangana has since issued its own presidential order organizing 7 zones and 2 multi-zones in 2018.",
            "fact_ta": "தெலங்கானா பின்னர் 2018-ல் 7 மண்டலங்கள் மற்றும் 2 பல-மண்டலங்களை ஒழுங்கமைத்து தனது சொந்த குடியரசுத் தலைவர் உத்தரவை வெளியிட்டது."
        },
        # 8
        {
            "subtopic": "Article 371F Sikkim Pre-merger Laws Basic Structure",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Pre-merger laws of Sikkim protected under Article 371F(k) are completely immune from judicial review by Indian courts.\nReason (R): Article 371F(m) bars the jurisdiction of the Supreme Court in respect of disputes arising out of pre-merger treaties and agreements relating to Sikkim.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): சரத்து 371F(k)-ன் கீழ் பாதுகாக்கப்பட்ட சிக்கிமின் இணைப்பிற்கு முந்தைய சட்டங்கள் இந்திய நீதிமன்றங்களின் நீதித்துறை மறுஆய்விலிருந்து முற்றிலும் விலக்கு பெற்றுள்ளன.\nகாரணம் (R): சரத்து 371F(m) இணைப்புக்கு முந்தைய ஒப்பந்தங்கள் தொடர்பான தகராறுகளில் உச்ச நீதிமன்றத்தின் அதிகார வரம்பைத் தடுக்கிறது.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை."),
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு.")
            ],
            "correct_key": "A",
            "exp_en": "Assertion (A) is false because in Association of Old Settlers of Sikkim (2023) and RC Poudyal (1994), the Supreme Court clarified that pre-merger laws protected by 371F(k) cannot violate fundamental rights or the basic structure. Reason (R) is true because Article 371F(m) does indeed contain a jurisdictional bar regarding pre-merger treaties and political engagements.",
            "exp_ta": "கூற்று (A) தவறானது, ஏனெனில் ஓல்ட் செட்லர்ஸ் ஆஃப் சிக்கிம் (2023) மற்றும் ஆர்.சி. பௌடியால் (1994) வழக்குகளில் 371F(k)-ஆல் பாதுகாக்கப்பட்ட பழைய சட்டங்கள் அடிப்படை உரிமைகளையோ அல்லது அடிப்படைக் கட்டமைப்பையோ மீற முடியாது என்று உச்ச நீதிமன்றம் தெளிவுபடுத்தியது. காரணம் (R) உண்மை, ஏனெனில் சரத்து 371F(m) முந்தைய உடன்படிக்கைகள் மற்றும் அரசியல் ஒப்பந்தங்கள் தொடர்பான தகராறுகளில் நீதிமன்ற அதிகார வரம்பிற்குத் தடை விதிக்கிறது.",
            "why_a_en": "A is false due to established Supreme Court precedent; R correctly cites Art 371F(m).",
            "why_a_ta": "உச்ச நீதிமன்றத் தீர்ப்புகளின்படி A தவறு; R சரத்து 371F(m)-ஐச் சரியாகக் குறிப்பிடுகிறது.",
            "why_b_en": "A is false.",
            "why_b_ta": "A தவறானது.",
            "why_c_en": "A is false.",
            "why_c_ta": "A தவறானது.",
            "why_d_en": "A is false and R is true.",
            "why_d_ta": "A தவறு மற்றும் R உண்மை.",
            "tip_en": "Constitutional immunity clauses never protect violations of the basic structure or Article 14 arbitrary discriminations.",
            "tip_ta": "அரசியலமைப்புப் பாதுகாப்பு விதிகள் ஒருபோதும் அடிப்படைக் கட்டமைப்பு மீறல்கள் அல்லது சரத்து 14 தன்னிச்சையான பாகுபாடுகளைப் பாதுகாக்காது.",
            "fact_en": "In 2023, the Supreme Court struck down Section 10(26AAA) IT Act exclusion of Indian-origin old settlers in Sikkim.",
            "fact_ta": "2023-ல் உச்ச நீதிமன்றம் சிக்கிமில் உள்ள இந்திய வம்சாவளி பழைய குடியேறிகளை விலக்கிய வருமான வரிச் சட்டத்தின் பிரிவு 10(26AAA)-ஐ ரத்து செய்தது."
        },
        # 9
        {
            "subtopic": "Article 371F Sangha Seat Justification",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): The reservation of a seat for the Buddhist Sangha in the Sikkim Legislative Assembly does not violate the secular character of the Indian Constitution.\nReason (R): In RC Poudyal (1994), the Supreme Court held that the Sangha historically represented an established political and social institution, not merely a religious denomination, in Sikkim.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): சிக்கிம் சட்டமன்றத்தில் பௌத்த சங்காவிற்கு ஒரு இடம் ஒதுக்கீடு செய்யப்படுவது இந்திய அரசியலமைப்பின் மதச்சார்பற்ற தன்மையை மீறாது.\nகாரணம் (R): ஆர்.சி. பௌடியால் (1994) வழக்கில், சங்கா வரலாற்று ரீதியாக வெறும் மதப் பிரிவை மட்டுமல்லாமல், சிக்கிமில் நிறுவப்பட்ட அரசியல் மற்றும் சமூக நிறுவனத்தையே பிரதிநிதித்துவப்படுத்தியது என்று உச்ச நீதிமன்றம் கூறியது.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) is the exact judicial reasoning adopted by the Supreme Court in RC Poudyal v. Union of India (1994) to uphold the Sangha seat under Article 371F(f).",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம். ஆர்.சி. பௌடியால் எதிர் இந்திய ஒன்றியம் (1994) வழக்கில் சரத்து 371F(f)-ன் கீழ் சங்கா இடத்தை உறுதி செய்ய உச்ச நீதிமன்றம் கையாண்ட சரியான நீதித்துறை காரணம் இதுவாகும்.",
            "why_a_en": "R directly provides the legal ratio decidendi that validates A.",
            "why_a_ta": "A-வை உறுதிப்படுத்தும் சட்டப்பூர்வ தீர்ப்புக் காரணத்தை R நேரடியாக வழங்குகிறது.",
            "why_b_en": "R directly explains A.",
            "why_b_ta": "R நேரடியாக A-வை விளக்குகிறது.",
            "why_c_en": "R is true.",
            "why_c_ta": "R உண்மை.",
            "why_d_en": "A is true.",
            "why_d_ta": "A உண்மை.",
            "tip_en": "The Sangha seat represents an accommodation of historical treaty rights during accession.",
            "tip_ta": "சங்கா தொகுதி என்பது இணைப்பின் போது வரலாற்று ஒப்பந்த உரிமைகளை ஏற்றுக்கொண்டதை பிரதிபலிக்கிறது.",
            "fact_en": "Sikkim's Chogyal system was a theocratic monarchy where Buddhist monasteries played a constitutional role.",
            "fact_ta": "சிக்கிமின் சோக்யால் அமைப்பு ஒரு மதகுரு மன்னராட்சியாக இருந்தது, அங்கு புத்த மடாலயங்கள் அரசியலமைப்பு ரீதியான பங்கைக் கொண்டிருந்தன."
        },
        # 10
        {
            "subtopic": "Article 371G Mizoram Assembly Resolution",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Central laws regulating the religious practices of the Mizos do not automatically take effect in Mizoram.\nReason (R): Article 371G requires a resolution of the Legislative Assembly of the State of Mizoram for such laws to become applicable.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): மிசோக்களின் மத நடைமுறைகளை ஒழுங்குபடுத்தும் மத்திய சட்டங்கள் தானாகவே மிசோரமில் நடைமுறைக்கு வராது.\nகாரணம் (R): சரத்து 371G அத்தகைய சட்டங்கள் பொருந்தக்கூடியதாக மாறுவதற்கு மிசோரம் மாநில சட்டமன்றத்தின் தீர்மானத்தைக் கட்டாயமாக்குகிறது.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) correctly explains (A). Under Article 371G(a)(i), no Act of Parliament in respect of religious or social practices of the Mizos shall apply to the State of Mizoram unless the Legislative Assembly of the State of Mizoram by a resolution so decides.",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம். சரத்து 371G(a)(i)-ன் கீழ், மிசோரம் மாநில சட்டமன்றம் தீர்மானம் நிறைவேற்றினால் தவிர, மிசோக்களின் மத அல்லது சமூக நடைமுறைகள் தொடர்பான எந்தவொரு நாடாளுமன்றச் சட்டமும் மிசோரம் மாநிலத்திற்குப் பொருந்தாது.",
            "why_a_en": "R directly provides the constitutional rule that creates and explains the situation in A.",
            "why_a_ta": "A-ல் உள்ள நிலையை உருவாக்கும் மற்றும் விளக்கும் அரசியலமைப்பு விதியை R நேரடியாக வழங்குகிறது.",
            "why_b_en": "R is the direct explanation of A.",
            "why_b_ta": "R என்பது A-ன் நேரடி விளக்கம்.",
            "why_c_en": "R is true.",
            "why_c_ta": "R உண்மை.",
            "why_d_en": "A is true.",
            "why_d_ta": "A உண்மை.",
            "tip_en": "The wording of 371G(a) mirrors Article 371A(1)(a) verbatim.",
            "tip_ta": "சரத்து 371G(a)-ன் வாசகங்கள் சரத்து 371A(1)(a)-ன் வாசகங்களை அப்படியே ஒத்திருக்கின்றன.",
            "fact_en": "Mizoram was the only Union Territory transformed into a state under the 1986 accord.",
            "fact_ta": "1986 அமைதி ஒப்பந்தத்தின் கீழ் மாநிலமாக மாற்றப்பட்ட ஒரே யூனியன் பிரதேசம் மிசோரம் ஆகும்."
        },
        # 11
        {
            "subtopic": "Article 371H Arunachal Pradesh Governor Discretion",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): The Governor of Arunachal Pradesh exercises personal judgment in matters of law and order without consulting the Council of Ministers.\nReason (R): Article 371H requires the Governor to consult the Council of Ministers before taking action on law and order in his individual judgment.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): அருணாச்சலப் பிரதேச ஆளுநர் அமைச்சரவையைக் கலந்தாலோசிக்காமல் சட்டம் ஒழுங்கு விவகாரங்களில் தனது தனிப்பட்ட முடிவைப் பயன்படுத்துகிறார்.\nகாரணம் (R): சரத்து 371H ஆளுநர் தனது தனிப்பட்ட முடிவின் கீழ் சட்டம் ஒழுங்கில் நடவடிக்கை எடுப்பதற்கு முன்பு அமைச்சரவையைக் கலந்தாலோசிக்க வேண்டும் என்று கட்டாயமாக்குகிறது.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை."),
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு.")
            ],
            "correct_key": "A",
            "exp_en": "Assertion (A) is false because Article 371H(a) explicitly mandates that the Governor shall exercise individual judgment 'after consulting the Council of Ministers'. The Governor cannot bypass consultation. Reason (R) is true as it accurately states the constitutional requirement.",
            "exp_ta": "கூற்று (A) தவறானது, ஏனெனில் சரத்து 371H(a) ஆளுநர் 'அமைச்சரவையைக் கலந்தாலோசித்த பிறகே' தனது தனிப்பட்ட முடிவைப் பயன்படுத்த வேண்டும் என்று வெளிப்படையாகக் கட்டாயமாக்குகிறது. ஆளுநர் ஆலோசனையைத் தவிர்க்க முடியாது. காரணம் (R) அரசியலமைப்புத் தேவையைச் சரியாகக் கூறுவதால் உண்மை.",
            "why_a_en": "A is false because consultation is mandatory under Art 371H; R correctly states the constitutional rule.",
            "why_a_ta": "சரத்து 371H-ன் கீழ் கலந்தாலோசிப்பது கட்டாயம் என்பதால் A தவறு; R அரசியலமைப்பு விதியைச் சரியாகக் கூறுகிறது.",
            "why_b_en": "A is false.",
            "why_b_ta": "A தவறானது.",
            "why_c_en": "A is false.",
            "why_c_ta": "A தவறானது.",
            "why_d_en": "A is false and R is true.",
            "why_d_ta": "A தவறு மற்றும் R உண்மை.",
            "tip_en": "Subtle distinction: 'Individual judgment' requires prior consultation; 'sole discretion' does not require consultation.",
            "tip_ta": "நுணுக்கமான வேறுபாடு: 'தனிப்பட்ட முடிவு' என்பது முன்கூட்டியே கலந்தாலோசிப்பதைக் கோருகிறது; 'முழு விருப்புரிமை' ஆலோசனை கோருவதில்லை.",
            "fact_en": "Article 371H was heavily debated during the Nabam Rebia case (2016) regarding governor's powers.",
            "fact_ta": "ஆளுநரின் அதிகாரங்கள் தொடர்பான நபம் ரேபியா வழக்கில் (2016) சரத்து 371H விரிவாக விவாதிக்கப்பட்டது."
        },
        # 12
        {
            "subtopic": "Article 371I Goa Assembly Strength Exception",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): The Legislative Assembly of Goa consists of 40 members, which is fewer than the 60 members prescribed by Article 170.\nReason (R): Article 371I creates an express constitutional exception allowing Goa's Assembly to have not less than 30 members.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): கோவா சட்டமன்றம் 40 உறுப்பினர்களைக் கொண்டுள்ளது, இது சரத்து 170-ல் பரிந்துரைக்கப்பட்ட 60 உறுப்பினர்களை விடக் குறைவு.\nகாரணம் (R): சரத்து 371I கோவா சட்டமன்றத்தில் 30 உறுப்பினர்களுக்குக் குறையாமல் இருக்க அனுமதிக்கும் வெளிப்படையான அரசியலமைப்பு விதிவிலக்கை உருவாக்குகிறது.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) provides the constitutional justification for (A). Under Article 170(1), states must have between 60 and 500 members, but Article 371I overrides this for Goa by starting with 'Notwithstanding anything in this Constitution... not less than thirty members'.",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-க்கான அரசியலமைப்பு நியாயத்தை வழங்குகிறது. சரத்து 170(1)-ன் கீழ் மாநிலங்கள் 60 முதல் 500 உறுப்பினர்களைக் கொண்டிருக்க வேண்டும், ஆனால் சரத்து 371I 'இந்த அரசியலமைப்பில் என்ன கூறப்பட்டிருந்தாலும்... முப்பது உறுப்பினர்களுக்குக் குறையாமல்' என்று கோவாவிற்கு விதிவிலக்கு அளிக்கிறது.",
            "why_a_en": "R directly provides the constitutional non-obstante justification for A.",
            "why_a_ta": "A-க்கான அரசியலமைப்பு முரண்பாடற்ற நியாயத்தை R நேரடியாக வழங்குகிறது.",
            "why_b_en": "R directly explains A.",
            "why_b_ta": "R நேரடியாக A-வை விளக்குகிறது.",
            "why_c_en": "R is true.",
            "why_c_ta": "R உண்மை.",
            "why_d_en": "A is true.",
            "why_d_ta": "A உண்மை.",
            "tip_en": "Goa, Mizoram, Sikkim, and Arunachal Pradesh all have constitutional assembly strength below 60.",
            "tip_ta": "கோவா, மிசோரம், சிக்கிம் மற்றும் அருணாச்சலப் பிரதேசம் ஆகிய அனைத்தும் 60-க்கு குறைவான சட்டமன்ற பலத்தைக் கொண்டுள்ளன.",
            "fact_en": "Goa became India's 25th state on 30 May 1987.",
            "fact_ta": "கோவா 1987 மே 30 அன்று இந்தியாவின் 25வது மாநிலமாக மாறியது."
        },
        # 13
        {
            "subtopic": "Article 371J Socio-Economic Rationale",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Article 371J was inserted into the Constitution to provide special quotas in public employment and education for residents of Kalyana Karnataka.\nReason (R): The region had suffered historic developmental neglect, as highlighted by the High Power Committee on Redressal of Regional Imbalances headed by Dr. D.M. Nanjundappa.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): கல்யாண கர்நாடகாவில் வசிப்பவர்களுக்கு பொது வேலைவாய்ப்பு மற்றும் கல்வியில் சிறப்பு இடஒதுக்கீடு வழங்க சரத்து 371J அரசியலமைப்பில் சேர்க்கப்பட்டது.\nகாரணம் (R): டாக்டர் டி.எம். நஞ்சுண்டப்பா தலைமையிலான பிராந்திய ஏற்றத்தாழ்வுகளைக் களைவதற்கான உயர்மட்டக் குழு சுட்டிக்காட்டியபடி, இப்பகுதி வரலாற்று ரீதியான வளர்ச்சி புறக்கணிப்பை எதிர்கொண்டிருந்தது.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) provides the foundational socio-economic and policy reason for (A). The Nanjundappa Committee Report (2002) documented acute regional imbalances in the Hyderabad-Karnataka region, leading Parliament to pass the 98th Constitutional Amendment Act, 2012.",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-க்கான அடிப்படைக் கொள்கை மற்றும் சமூக-பொருளாதாரக் காரணத்தை வழங்குகிறது. நஞ்சுண்டப்பா கமிட்டி அறிக்கை (2002) ஹைதராபாத்-கர்நாடகா பகுதியின் கடுமையான பின்தங்கிய நிலையை ஆவணப்படுத்தியது, இது 98வது திருத்தச் சட்டம் 2012-ஐ நாடாளுமன்றம் நிறைவேற்ற வழிவகுத்தது.",
            "why_a_en": "R explains the official empirical justification and impetus for inserting Article 371J.",
            "why_a_ta": "சரத்து 371J-ஐச் சேர்ப்பதற்கான அதிகாரப்பூர்வ அனுபவ நியாயத்தையும் உந்துதலையும் R விளக்குகிறது.",
            "why_b_en": "R directly explains A.",
            "why_b_ta": "R நேரடியாக A-வை விளக்குகிறது.",
            "why_c_en": "R is true.",
            "why_c_ta": "R உண்மை.",
            "why_d_en": "A is true.",
            "why_d_ta": "A உண்மை.",
            "tip_en": "Nanjundappa Committee = Karnataka Regional Imbalance (Article 371J).",
            "tip_ta": "நஞ்சுண்டப்பா கமிட்டி = கர்நாடக பிராந்திய ஏற்றத்தாழ்வு (சரத்து 371J).",
            "fact_en": "The committee submitted its report in 2002 identifying 39 most backward taluks in the state.",
            "fact_ta": "இக்குழு 2002-ல் தனது அறிக்கையை சமர்ப்பித்து மாநிலத்தில் மிகவும் பின்தங்கிய 39 தாலுகாக்களை அடையாளம் கண்டது."
        },
        # 14
        {
            "subtopic": "Article 370 Temporary Asymmetric Integration",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): The Supreme Court in 2023 held that Jammu and Kashmir did not retain any element of sovereignty after signing the Instrument of Accession.\nReason (R): Article 1 of the Indian Constitution declares India as a 'Union of States', and Jammu and Kashmir was listed as a State under the First Schedule.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): இணைப்பு ஆவணத்தில் கையெழுத்திட்ட பிறகு ஜம்மு காஷ்மீர் எந்தவொரு இறையாண்மை அம்சத்தையும் தக்க வைத்துக் கொள்ளவில்லை என்று 2023-ல் உச்ச நீதிமன்றம் தீர்ப்பளித்தது.\nகாரணம் (R): இந்திய அரசியலமைப்பின் சரத்து 1 இந்தியாவை ஒரு 'மாநிலங்களின் ஒன்றியம்' என்று அறிவிக்கிறது, மேலும் ஜம்மு காஷ்மீர் முதல் அட்டவணையின் கீழ் ஒரு மாநிலமாக பட்டியலிடப்பட்டது.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) is the constitutional rationale for (A). In In Re: Article 370 (2023), the 5-judge Constitution Bench held that Maharaja Hari Singh's proclamation and the integration into Article 1 and the First Schedule extinguished any internal or external sovereignty of J&K.",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-க்கான அரசியலமைப்பு காரணத்தை வழங்குகிறது. சரத்து 370 வழக்கில் (2023), மகாராஜா ஹரி சிங்கின் பிரகடனம் மற்றும் சரத்து 1 மற்றும் முதல் அட்டவணையில் இணைக்கப்பட்டது ஆகியவை ஜம்மு காஷ்மீரின் அனைத்து உள் மற்றும் வெளி இறையாண்மையையும் முடிவுக்குக் கொண்டுவந்தன என்று உச்ச நீதிமன்றம் கூறியது.",
            "why_a_en": "R directly provides the legal grounding used by the CJI in affirming A.",
            "why_a_ta": "A-வை உறுதிப்படுத்துவதில் தலைமை நீதிபதி பயன்படுத்திய சட்டப்பூர்வ அடிப்படையை R நேரடியாக வழங்குகிறது.",
            "why_b_en": "R directly explains A.",
            "why_b_ta": "R நேரடியாக A-வை விளக்குகிறது.",
            "why_c_en": "R is true.",
            "why_c_ta": "R உண்மை.",
            "why_d_en": "A is true.",
            "why_d_ta": "A உண்மை.",
            "tip_en": "J&K Constitution's Section 3 also affirmed that J&K is and shall be an integral part of India.",
            "tip_ta": "ஜம்மு காஷ்மீர் அரசியலமைப்பின் பிரிவு 3-ம் ஜம்மு காஷ்மீர் இந்தியாவின் ஒருங்கிணைந்த பகுதியாகும் என்பதை உறுதி செய்தது.",
            "fact_en": "Yuvraj Karan Singh issued the proclamation on 25 November 1949 accepting the Indian Constitution.",
            "fact_ta": "யுவராஜ் கரண் சிங் 1949 நவம்பர் 25 அன்று இந்திய அரசியலமைப்பை ஏற்று பிரகடனத்தை வெளியிட்டார்."
        },
        # 15
        {
            "subtopic": "Article 371 vs Article 371D Differences",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Article 371 provides for the establishment of separate development boards, whereas Article 371D provides for local cadres and quotas in public employment.\nReason (R): Article 371 addresses regional imbalances in Maharashtra and Gujarat, whereas Article 371D resolved regional conflicts within Andhra Pradesh.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): சரத்து 371 தனி வளர்ச்சி வாரியங்களை அமைக்க வகை செய்கிறது, அதே சமயம் சரத்து 371D பொது வேலைவாய்ப்பில் உள்ளூர் பணிகளையும் இடஒதுக்கீடுகளையும் வழங்குகிறது.\nகாரணம் (R): சரத்து 371 மகாராஷ்டிரா மற்றும் குஜராத்தில் உள்ள பிராந்திய ஏற்றத்தாழ்வுகளைக் கையாள்கிறது, ஆனால் சரத்து 371D ஆந்திரப் பிரதேசத்திற்குள் நிலவிய பிராந்திய மோதல்களைத் தீர்த்தது.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "B",
            "exp_en": "Both (A) and (R) are true, but (R) is a statement of context rather than the direct causal explanation of the legal mechanisms stated in (A). Both provisions represent tailor-made asymmetric federal arrangements addressing distinct historical challenges.",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-ல் கூறப்பட்டுள்ள சட்ட வழிமுறைகளின் நேரடி காரண விளக்கம் அல்ல, மாறாக அதன் பின்னணி சூழலைக் கூறுகிறது. இரண்டு விதிகளும் தனித்துவமான வரலாற்று சவால்களை எதிர்கொள்ள உருவாக்கப்பட்ட சமச்சீரற்ற கூட்டாட்சி ஏற்பாடுகள் ஆகும்.",
            "why_a_en": "R describes geographical context, but not why the constitutional drafting differs mechanically.",
            "why_a_ta": "R புவியியல் சூழலை விவரிக்கிறது, ஆனால் அரசியலமைப்பு வரைவு ஏன் வேறுபடுகிறது என்பதற்கான நேரடி காரணமல்ல.",
            "why_b_en": "Both statements are factually and conceptually true.",
            "why_b_ta": "இரண்டு கூற்றுகளும் உண்மையானவை மற்றும் கருத்தியல் ரீதியாக சரியானவை.",
            "why_c_en": "R is true.",
            "why_c_ta": "R உண்மை.",
            "why_d_en": "A is true.",
            "why_d_ta": "A உண்மை.",
            "tip_en": "371 focuses on Development Boards; 371D focuses on Local Reservations and Tribunals.",
            "tip_ta": "371 வளர்ச்சி வாரியங்களில் கவனம் செலுத்துகிறது; 371D உள்ளூர் இடஒதுக்கீடு மற்றும் தீர்ப்பாயங்களில் கவனம் செலுத்துகிறது.",
            "fact_en": "Article 371 was substituted in 1956/1960; Article 371D was added in 1973.",
            "fact_ta": "சரத்து 371 1956/1960-ல் மாற்றியமைக்கப்பட்டது; சரத்து 371D 1973-ல் சேர்க்கப்பட்டது."
        },
        # 16
        {
            "subtopic": "Article 371E Central University Legislative Competence",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): A Central University cannot be established in Andhra Pradesh under Article 371E merely through an executive notification of the Union Ministry of Education.\nReason (R): Article 371E expressly mandates that Parliament must provide for the establishment of the university 'by law'.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): மத்திய கல்வி அமைச்சகத்தின் நிர்வாக அறிவிக்கை மூலம் மட்டுமே சரத்து 371E-ன் கீழ் ஆந்திரப் பிரதேசத்தில் ஒரு மத்தியப் பல்கலைக்கழகத்தை நிறுவ முடியாது.\nகாரணம் (R): சரத்து 371E நாடாளுமன்றம் 'சட்டத்தின் மூலம்' மட்டுமே இப்பல்கலைக்கழகத்தை நிறுவ வேண்டும் என்று வெளிப்படையாகக் கட்டாயமாக்குகிறது.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) is the correct explanation of (A). Because Article 371E uses the phrase 'Parliament may by law provide', an executive order or notification is insufficient; a statutory enactment by Parliament is constitutionally mandatory.",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம். சரத்து 371E 'நாடாளுமன்றம் சட்டத்தின் மூலம் வகை செய்யலாம்' என்ற சொற்றொடரைப் பயன்படுத்துவதால், ஒரு நிர்வாக உத்தரவு போதுமானதல்ல; நாடாளுமன்றத்தின் சட்டப்பூர்வ சட்டமியற்றல் கட்டாயமாகும்.",
            "why_a_en": "R directly provides the constitutional text ('by law') that explains why executive action in A is invalid.",
            "why_a_ta": "A-ல் நிர்வாக நடவடிக்கை ஏன் போதாது என்பதை விளக்கும் அரசியலமைப்பு வாசகத்தை ('சட்டத்தின் மூலம்') R நேரடியாக வழங்குகிறது.",
            "why_b_en": "R is the direct explanation of A.",
            "why_b_ta": "R என்பது A-ன் நேரடி விளக்கம்.",
            "why_c_en": "R is true.",
            "why_c_ta": "R உண்மை.",
            "why_d_en": "A is true.",
            "why_d_ta": "A உண்மை.",
            "tip_en": "Distinguish between provisions requiring 'law by Parliament' and those executed by 'Order of the President'.",
            "tip_ta": "'நாடாளுமன்றச் சட்டம்' தேவைப்படும் விதிகளையும், 'குடியரசுத் தலைவரின் உத்தரவால்' செயல்படுத்தப்படும் விதிகளையும் வேறுபடுத்திப் பார்க்கவும்.",
            "fact_en": "Central Universities (Amendment) Act, 2019 was passed to fulfill this mandate.",
            "fact_ta": "இக்கட்டளையை நிறைவேற்ற மத்தியப் பல்கலைக்கழகங்கள் (திருத்தச்) சட்டம் 2019 நிறைவேற்றப்பட்டது."
        },
        # 17
        {
            "subtopic": "Asymmetric Federalism Constitutional Legitimacy",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Asymmetric federal provisions in Articles 371 to 371-J violate the principle of federal equality of States.\nReason (R): The Supreme Court has held that asymmetric federalism is a valid feature of the Indian Constitution designed to accommodate historical diversities and integration needs.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): சரத்துகள் 371 முதல் 371-J வரையிலான சமச்சீரற்ற கூட்டாட்சி ஏற்பாடுகள் மாநிலங்களின் கூட்டாட்சி சமத்துவக் கொள்கையை மீறுகின்றன.\nகாரணம் (R): வரலாற்று பன்முகத்தன்மைகள் மற்றும் ஒருங்கிணைப்புத் தேவைகளை ஏற்கும் வகையில் வடிவமைக்கப்பட்ட சமச்சீரற்ற கூட்டாட்சி இந்திய அரசியலமைப்பின் செல்லுபடியாகும் அம்சம் என்று உச்ச நீதிமன்றம் கூறியுள்ளது.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை."),
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு.")
            ],
            "correct_key": "A",
            "exp_en": "Assertion (A) is false because asymmetric federalism does NOT violate the Constitution; it is an acknowledged, legitimate constitutional design affirmed by the Supreme Court in RC Poudyal (1994) and In Re: Article 370 (2023). Reason (R) is true and represents settled constitutional jurisprudence.",
            "exp_ta": "கூற்று (A) தவறானது, ஏனெனில் சமச்சீரற்ற கூட்டாட்சி அரசியலமைப்பை மீறவில்லை; இது ஆர்.சி. பௌடியால் (1994) மற்றும் சரத்து 370 (2023) வழக்குகளில் உச்ச நீதிமன்றத்தால் உறுதி செய்யப்பட்ட சட்டப்பூர்வ அரசியலமைப்பு வடிவமைப்பாகும். காரணம் (R) உண்மை மற்றும் நிறுவப்பட்ட சட்டக் கோட்பாடாகும்.",
            "why_a_en": "A is false because asymmetric provisions are constitutional; R is a true statement of law.",
            "why_a_ta": "சமச்சீரற்ற ஏற்பாடுகள் அரசியலமைப்புக்கு உட்பட்டவை என்பதால் A தவறு; R என்பது சரியான சட்டக் கூற்று.",
            "why_b_en": "A is false.",
            "why_b_ta": "A தவறானது.",
            "why_c_en": "A is false.",
            "why_c_ta": "A தவறானது.",
            "why_d_en": "A is false and R is true.",
            "why_d_ta": "A தவறு மற்றும் R உண்மை.",
            "tip_en": "Indian federalism accommodates diverse sub-national identities through differential constitutional guarantees.",
            "tip_ta": "இந்தியக் கூட்டாட்சி மாறுபட்ட அரசியலமைப்பு உத்தரவாதங்கள் மூலம் பல்வேறு துணை தேசிய அடையாளங்களை ஒருங்கிணைக்கிறது.",
            "fact_en": "Asymmetric federalism also exists in other democracies like Canada (Quebec) and Spain (Catalonia).",
            "fact_ta": "கனடா (கியூபெக்) மற்றும் ஸ்பெயின் (கேடலோனியா) போன்ற பிற ஜனநாயக நாடுகளிலும் சமச்சீரற்ற கூட்டாட்சி உள்ளது."
        },
        # 18
        {
            "subtopic": "Article 371A Mineral Rights Dispute",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): The Nagaland Legislative Assembly claims exclusive competence to regulate oil and mineral exploration in the State.\nReason (R): Article 371A(1)(a)(iv) provides that no Act of Parliament regarding ownership and transfer of land and its resources shall apply to Nagaland without the Assembly's resolution.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): நாகாலாந்து சட்டமன்றம் மாநிலத்தில் எண்ணெய் மற்றும் கனிம ஆய்வுகளை ஒழுங்குபடுத்த பிரத்யேக அதிகாரம் கோருகிறது.\nகாரணம் (R): சரத்து 371A(1)(a)(iv) நிலம் மற்றும் அதன் வளங்களின் உரிமை மற்றும் பரிமாற்றம் தொடர்பான எந்தவொரு நாடாளுமன்றச் சட்டமும் சட்டமன்றத் தீர்மானமின்றி நாகாலாந்திற்குப் பொருந்தாது என்று வகை செய்கிறது.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) provides the constitutional text relied upon by the State to make the claim in (A). The Nagaland Assembly interprets 'and its resources' to encompass petroleum and subsoil minerals, though the Union contests this citing Union List Entry 53.",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-ல் மாநில அரசு கோரும் உரிமைக்கான அரசியலமைப்பு வாசகத்தை வழங்குகிறது. 'மற்றும் அதன் வளங்கள்' என்ற சொற்றொடர் பெட்ரோலியம் மற்றும் கனிமங்களை உள்ளடக்கியது என நாகாலாந்து சட்டமன்றம் கூறுகிறது, ஆனால் மத்தியப் பட்டியல் பதிவு 53-ஐக் குறிப்பிட்டு மத்திய அரசு இதை மறுக்கிறது.",
            "why_a_en": "R directly provides the textual basis under Art 371A on which the claim in A is grounded.",
            "why_a_ta": "A-ல் உள்ள கோரிக்கைக்கு அடிப்படையான சரத்து 371A-ன் கீழான உரை அடிப்படையை R நேரடியாக வழங்குகிறது.",
            "why_b_en": "R directly explains A.",
            "why_b_ta": "R நேரடியாக A-வை விளக்குகிறது.",
            "why_c_en": "R is true.",
            "why_c_ta": "R உண்மை.",
            "why_d_en": "A is true.",
            "why_d_ta": "A உண்மை.",
            "tip_en": "The dispute centers on Entry 53 of List I (Regulation of oilfields and mineral oil) vs Article 371A(1)(a)(iv).",
            "tip_ta": "பட்டியல் I-ன் பதிவு 53 (எண்ணெய் வயல்கள் ஒழுங்குமுறை) vs சரத்து 371A(1)(a)(iv) இடையே இந்த சர்ச்சை நிலவுகிறது.",
            "fact_en": "The Nagaland Assembly passed the Nagaland Petroleum and Natural Gas Rules in 2012.",
            "fact_ta": "நாகாலாந்து சட்டமன்றம் 2012-ல் நாகாலாந்து பெட்ரோலியம் மற்றும் இயற்கை எரிவாயு விதிகளை நிறைவேற்றியது."
        },
        # 19
        {
            "subtopic": "Article 371F Governor Special Responsibility Peace",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): The Governor of Sikkim has special responsibility for peace and for ensuring equitable socio-economic advancement of different sections of the population.\nReason (R): Under Article 371F(g), the Governor of Sikkim in discharge of this special responsibility acts subject to such directions as the President may issue.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): அமைதி மற்றும் பல்வேறு பிரிவு மக்களின் சமமான சமூக-பொருளாதார முன்னேற்றத்தை உறுதி செய்வதில் சிக்கிம் ஆளுநருக்குச் சிறப்புப் பொறுப்பு உண்டு.\nகாரணம் (R): சரத்து 371F(g)-ன் கீழ், இந்தச் சிறப்புப் பொறுப்பை நிறைவேற்றுவதில் சிக்கிம் ஆளுநர் குடியரசுத் தலைவர் பிறப்பிக்கும் வழிகாட்டுதல்களுக்கு உட்பட்டு செயல்படுகிறார்.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "B",
            "exp_en": "Both (A) and (R) are true, but (R) explains the subordination to Presidential directions rather than being the reason why the special responsibility was conferred in (A). The special responsibility was instituted to safeguard communal harmony among Bhutia, Lepcha, and Nepali communities.",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது ஆளுநர் குடியரசுத் தலைவரின் வழிகாட்டுதலுக்கு உட்பட்டவர் என்பதைக் கூறுகிறது, மாறாக (A)-ல் சிறப்புப் பொறுப்பு வழங்கப்பட்டதற்கான வரலாற்று காரணமல்ல. பூட்டியா, லெப்சா மற்றும் நேபாளி சமூகங்களுக்கிடையேயான நல்லிணக்கத்தைப் பாதுகாக்கவே இச்சிறப்புப் பொறுப்பு வழங்கப்பட்டது.",
            "why_a_en": "R explains the operational control, not the historical/substantive reason for conferring the power in A.",
            "why_a_ta": "R நிர்வாகக் கட்டுப்பாட்டை விளக்குகிறது, ஆனால் A-ல் அதிகாரம் வழங்கப்பட்டதற்கான காரணமல்ல.",
            "why_b_en": "Both statements correctly state the provisions of Article 371F(g).",
            "why_b_ta": "இரண்டு கூற்றுகளும் சரத்து 371F(g)-ன் விதிகளைச் சரியாகக் கூறுகின்றன.",
            "why_c_en": "R is true.",
            "why_c_ta": "R உண்மை.",
            "why_d_en": "A is true.",
            "why_d_ta": "A உண்மை.",
            "tip_en": "Article 371F(g) gives the Governor discretionary judgment subject to Presidential oversight.",
            "tip_ta": "சரத்து 371F(g) ஆளுநருக்குக் குடியரசுத் தலைவரின் கண்காணிப்புக்கு உட்பட்ட விருப்புரிமைத் தீர்ப்பை வழங்குகிறது.",
            "fact_en": "Sikkim's population comprises Nepali majority alongside indigenous Lepchas and Bhutias.",
            "fact_ta": "சிக்கிமின் மக்கள் தொகையில் பூர்வீக லெப்சாக்கள் மற்றும் பூட்டியாக்களுடன் நேபாளி பெரும்பான்மையினரும் உள்ளனர்."
        },
        # 20
        {
            "subtopic": "Article 371D Presidential Order Zone Classification",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Residential qualifications for public employment under Article 371D are constitutionally immune from being challenged under Article 16(2).\nReason (R): Article 371D(10) contains a non-obstante clause providing that its provisions and orders made thereunder have effect notwithstanding anything in the Constitution.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): சரத்து 371D-ன் கீழ் பொது வேலைவாய்ப்பிற்கான குடியிருப்புத் தகுதிகள் சரத்து 16(2)-ன் கீழ் சவால் செய்யப்படுவதிலிருந்து அரசியலமைப்பு ரீதியாகப் பாதுகாக்கப்படுகின்றன.\nகாரணம் (R): சரத்து 371D(10) அரசியலமைப்பில் என்ன கூறப்பட்டிருந்தாலும் அதன் விதிகளும் அதன் கீழ் பிறப்பிக்கப்படும் உத்தரவுகளும் நடைமுறையில் இருக்கும் என்ற முரண்பாடற்ற விதியைக் கொண்டுள்ளது.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) provides the constitutional shield explaining (A). Article 16(2) prohibits discrimination based on residence, but the non-obstante clause in Article 371D(10) specifically insulates local reservation schemes from being invalidated under Article 16(2).",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வை விளக்கும் அரசியலமைப்புப் பாதுகாப்பை வழங்குகிறது. சரத்து 16(2) வசிப்பிடத்தின் அடிப்படையில் பாகுபாடு காட்டுவதைத் தடை செய்கிறது, ஆனால் சரத்து 371D(10)-ல் உள்ள முரண்பாடற்ற விதி உள்ளூர் இடஒதுக்கீட்டுத் திட்டங்களை சரத்து 16(2)-ன் கீழான சவால்களிலிருந்து பாதுகாக்கிறது.",
            "why_a_en": "R directly provides the constitutional overriding provision that produces A.",
            "why_a_ta": "A-வை உருவாக்கும் அரசியலமைப்பு மேலெழுதும் விதியை R நேரடியாக வழங்குகிறது.",
            "why_b_en": "R directly explains A.",
            "why_b_ta": "R நேரடியாக A-வை விளக்குகிறது.",
            "why_c_en": "R is true.",
            "why_c_ta": "R உண்மை.",
            "why_d_en": "A is true.",
            "why_d_ta": "A உண்மை.",
            "tip_en": "Article 16(3) also allows Parliament to prescribe residence requirements, but 371D provides region-specific constitutional sanction.",
            "tip_ta": "சரத்து 16(3) நாடாளுமன்றத்திற்கு குடியிருப்புத் தேவைகளை விதிக்க அனுமதிக்கிறது, ஆனால் 371D பிராந்தியம் சார்ந்த அரசியலமைப்பு அங்கீகாரத்தை வழங்குகிறது.",
            "fact_en": "Supreme Court upheld this immunity in Dr. B. Sudhakar v. Union of India (1995).",
            "fact_ta": "டாக்டர் பி. சுதாகர் எதிர் இந்திய ஒன்றியம் (1995) வழக்கில் உச்ச நீதிமன்றம் இந்த பாதுகாப்பை உறுதி செய்தது."
        },
        # 21
        {
            "subtopic": "Special Provisions Statehood Sequence Timing",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Nagaland was granted statehood before Sikkim, Mizoram, and Goa.\nReason (R): The 13th Amendment was passed in 1962, whereas Sikkim, Mizoram, and Goa attained statehood via the 36th (1975), 53rd (1986), and 56th (1987) Amendments respectively.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): சிக்கிம், மிசோரம் மற்றும் கோவாவிற்கு முன்பாகவே நாகாலாந்திற்கு மாநில அந்தஸ்து வழங்கப்பட்டது.\nகாரணம் (R): 13வது திருத்தம் 1962-ல் நிறைவேற்றப்பட்டது, ஆனால் சிக்கிம், மிசோரம் மற்றும் கோவா முறையே 36வது (1975), 53வது (1986) மற்றும் 56வது (1987) திருத்தங்கள் மூலம் மாநில அந்தஸ்தைப் பெற்றன.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) provides the constitutional chronology that verifies and explains (A). Nagaland became a state in 1963 (13th CAA), Sikkim in 1975 (36th CAA), Mizoram in 1987 (53rd CAA), and Goa in 1987 (56th CAA).",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வைச் சரிபார்த்து விளக்கும் அரசியலமைப்பு காலவரிசையை வழங்குகிறது. நாகாலாந்து 1963-ல் (13வது திருத்தம்), சிக்கிம் 1975-ல் (36வது திருத்தம்), மிசோரம் 1987-ல் (53வது திருத்தம்), மற்றும் கோவா 1987-ல் (56வது திருத்தம்) மாநிலங்களாயின.",
            "why_a_en": "R accurately dates the constitutional enactments confirming the order in A.",
            "why_a_ta": "A-ல் உள்ள வரிசையை உறுதிப்படுத்தும் அரசியலமைப்பு சட்டங்களின் தேதிகளை R துல்லியமாக வழங்குகிறது.",
            "why_b_en": "R directly explains A.",
            "why_b_ta": "R நேரடியாக A-வை விளக்குகிறது.",
            "why_c_en": "R is true.",
            "why_c_ta": "R உண்மை.",
            "why_d_en": "A is true.",
            "why_d_ta": "A உண்மை.",
            "tip_en": "State numbers: Nagaland = 16th, Sikkim = 22nd, Mizoram = 23rd, Goa = 25th.",
            "tip_ta": "மாநில எண்கள்: நாகாலாந்து = 16வது, சிக்கிம் = 22வது, மிசோரம் = 23வது, கோவா = 25வது.",
            "fact_en": "Arunachal Pradesh was the 24th state, between Mizoram and Goa in February 1987.",
            "fact_ta": "அருணாச்சலப் பிரதேசம் 1987 பிப்ரவரியில் மிசோரம் மற்றும் கோவாவிற்கு இடையே 24வது மாநிலமாக உருவானது."
        },
        # 22
        {
            "subtopic": "Special Provisions and Fundamental Rights",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Special affirmative action provisions under Article 371J cannot be struck down merely because they violate general equality principles under Article 14.\nReason (R): Article 371J is a constitutional amendment and enjoys substantive presumption of validity, acting as an exceptional classification scheme sanctioned by the Constitution itself.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): சரத்து 14-ன் கீழ் உள்ள பொதுவான சமத்துவக் கொள்கைகளை மீறுகிறது என்ற காரணத்திற்காக மட்டுமே சரத்து 371J-ன் கீழான சிறப்பு சாதகமான நடவடிக்கை விதிகளை ரத்து செய்ய முடியாது.\nகாரணம் (R): சரத்து 371J ஒரு அரசியலமைப்புத் திருத்தமாகும், மேலும் அரசியலமைப்பாலேயே அங்கீகரிக்கப்பட்ட விதிவிலக்கான வகைப்பாடு திட்டமாகச் செயல்பட்டு, செல்லுபடியாகும் தன்மையைக் கொண்டுள்ளது.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) explains (A). Constitutional amendments creating region-specific affirmative action enjoy equal constitutional status with Part III, and harmonize with Article 14's concept of substantive/real equality rather than formal equality.",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வை விளக்குகிறது. பிராந்தியம் சார்ந்த சாதகமான நடவடிக்கைகளை உருவாக்கும் அரசியலமைப்புத் திருத்தங்கள் பகுதி III-க்கு இணையான அரசியலமைப்பு அந்தஸ்தைப் பெற்றுள்ளன, மேலும் சரத்து 14-ன் சமத்துவக் கோட்பாட்டோடு இணங்கிச் செல்கின்றன.",
            "why_a_en": "R provides the jurisprudential doctrine that sustains the validity of A.",
            "why_a_ta": "A-ன் செல்லுபடியாகும் தன்மையைத் தாங்கும் சட்டக் கோட்பாட்டை R வழங்குகிறது.",
            "why_b_en": "R directly explains A.",
            "why_b_ta": "R நேரடியாக A-வை விளக்குகிறது.",
            "why_c_en": "R is true.",
            "why_c_ta": "R உண்மை.",
            "why_d_en": "A is true.",
            "why_d_ta": "A உண்மை.",
            "tip_en": "Substantive equality accommodates differential treatment for historically underprivileged regions.",
            "tip_ta": "உண்மையான சமத்துவம் வரலாற்று ரீதியாகப் பின்தங்கிய பகுதிகளுக்கான மாறுபட்ட சிகிச்சையை ஏற்றுக்கொள்கிறது.",
            "fact_en": "Karnataka High Court upheld the validity of rules framed under Article 371J in 2015.",
            "fact_ta": "கர்நாடக உயர் நீதிமன்றம் 2015-ல் சரத்து 371J-ன் கீழ் உருவாக்கப்பட்ட விதிகளின் செல்லுபடியாகும் தன்மையை உறுதி செய்தது."
        },
        # 23
        {
            "subtopic": "Fifth Schedule vs Article 371A Difference",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): In Fifth Schedule areas, the Governor can unilaterally direct that an Act of Parliament does not apply.\nReason (R): Under Article 371A, an Act of Parliament on protected subjects applies to Nagaland only if the State Legislative Assembly passes a resolution.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): ஐந்தாவது அட்டவணைப் பகுதிகளில், ஒரு நாடாளுமன்றச் சட்டம் பொருந்தாது என்று ஆளுநர் ஒருதலைப்பட்சமாக உத்தரவிட முடியும்.\nகாரணம் (R): சரத்து 371A-ன் கீழ், பாதுகாக்கப்பட்ட பாடங்கள் மீதான நாடாளுமன்றச் சட்டம் மாநில சட்டமன்றம் தீர்மானம் நிறைவேற்றினால் மட்டுமே நாகாலாந்திற்குப் பொருந்தும்.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, but (R) is a comparison point rather than the explanation of (A). (A) describes the Governor's notification power under Para 5(1) of the Fifth Schedule, while (R) correctly describes the democratic assembly resolution power under Article 371A.",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-ன் விளக்கம் அல்ல, மாறாக ஒரு ஒப்பீட்டுப் புள்ளியாகும். (A) ஐந்தாவது அட்டவணையின் பத்தி 5(1)-ன் கீழ் ஆளுநரின் அறிவிக்கை அதிகாரத்தை விவரிக்கிறது, அதே சமயம் (R) சரத்து 371A-ன் கீழ் சட்டமன்றத் தீர்மான அதிகாரத்தைச் சரியாக விவரிக்கிறது.",
            "why_a_en": "Both statements accurately contrast executive discretion in Sch 5 with legislative autonomy in Art 371A.",
            "why_a_ta": "இரண்டு கூற்றுகளும் அட்டவணை 5-ன் நிர்வாக விருப்புரிமையையும் சரத்து 371A-ன் சட்டமன்ற சுயாட்சியையும் துல்லியமாக ஒப்பிடுகின்றன.",
            "why_b_en": "R is not the cause/explanation of A.",
            "why_b_ta": "R என்பது A-க்கான காரணமல்ல/விளக்கமல்ல.",
            "why_c_en": "R is true.",
            "why_c_ta": "R உண்மை.",
            "why_d_en": "A is true.",
            "why_d_ta": "A உண்மை.",
            "tip_en": "5th Schedule = Governor's notification; Article 371A = Legislative Assembly's resolution.",
            "tip_ta": "5வது அட்டவணை = ஆளுநரின் அறிவிக்கை; சரத்து 371A = சட்டமன்றத்தின் தீர்மானம்.",
            "fact_en": "Article 371A provides higher democratic autonomy because power is vested in elected representatives.",
            "fact_ta": "தேர்ந்தெடுக்கப்பட்ட மக்கள் பிரதிநிதிகளிடம் அதிகாரம் வழங்கப்பட்டுள்ளதால் சரத்து 371A உயர்ந்த ஜனநாயக சுயாட்சியை வழங்குகிறது."
        },
        # 24
        {
            "subtopic": "Article 371E Law by Parliament vs Executive Order",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Article 371E and Article 371D were both added to the Constitution by the 32nd Amendment Act, 1973.\nReason (R): Article 371D is implemented by Orders of the President, whereas Article 371E requires an Act of Parliament.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): சரத்து 371E மற்றும் சரத்து 371D ஆகிய இரண்டுமே 32வது திருத்தச் சட்டம் 1973 மூலம் அரசியலமைப்பில் சேர்க்கப்பட்டன.\nகாரணம் (R): சரத்து 371D குடியரசுத் தலைவரின் உத்தரவுகளால் செயல்படுத்தப்படுகிறது, ஆனால் சரத்து 371E நாடாளுமன்றத்தின் சட்டத்தைக் கோருகிறது.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, but (R) is an operational comparison rather than the causal explanation of (A). Both articles originated together from the 32nd CAA 1973 following the Six-Point Formula.",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது ஒரு செயல்பாட்டு ஒப்பீடு மட்டுமே தவிர (A)-க்கான நேரடி காரண விளக்கம் அல்ல. இரண்டு சரத்துகளுமே ஆறு அம்ச சூத்திரத்தைத் தொடர்ந்து 32வது திருத்தம் 1973 மூலம் ஒன்றாகத் தோன்றின.",
            "why_a_en": "Both statements are independently true as per constitutional text and history.",
            "why_a_ta": "அரசியலமைப்பு உரை மற்றும் வரலாற்றின்படி இரண்டு கூற்றுகளும் தனித்தனியாக சரியானவை.",
            "why_b_en": "R does not explain why the amendment added both articles in A.",
            "why_b_ta": "திருத்தம் ஏன் இரண்டு சரத்துகளையும் சேர்த்தது என்பதை R விளக்கவில்லை.",
            "why_c_en": "R is true.",
            "why_c_ta": "R உண்மை.",
            "why_d_en": "A is true.",
            "why_d_ta": "A உண்மை.",
            "tip_en": "Remember: 32nd Amendment 1973 inserted BOTH 371D and 371E.",
            "tip_ta": "நினைவில் கொள்க: 32வது திருத்தம் 1973 சரத்துகள் 371D மற்றும் 371E இரண்டையுமே சேர்த்தது.",
            "fact_en": "The Six-Point Formula covered educational infrastructure (Art 371E) alongside employment (Art 371D).",
            "fact_ta": "ஆறு அம்ச சூத்திரம் வேலைவாய்ப்போடு (சரத்து 371D) கல்வி உள்கட்டமைப்பையும் (சரத்து 371E) உள்ளடக்கியது."
        },
        # 25
        {
            "subtopic": "Special Provisions Master Summary Reasoning",
            "stem_en": "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Articles 371 to 371-J constitute a crucial mechanism of Indian federalism to maintain national unity and integration.\nReason (R): These provisions flexibly accommodate regional aspirations, protect tribal identity, and redress historical economic backwardness across diverse states.\nIn the context of the above, which one of the following is correct?",
            "stem_ta": "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nகூற்று (A): சரத்துகள் 371 முதல் 371-J வரை தேசிய ஒற்றுமை மற்றும் ஒருமைப்பாட்டைப் பேணுவதற்கான இந்தியக் கூட்டாட்சியின் மிக முக்கிய வழிமுறையாகும்.\nகாரணம் (R): இந்த ஏற்பாடுகள் பிராந்திய விருப்பங்களை நெகிழ்வுடன் ஏற்றுக்கொள்கின்றன, பழங்குடியினரின் அடையாளத்தைப் பாதுகாக்கின்றன மற்றும் பல்வேறு மாநிலங்களின் வரலாற்றுப் பொருளாதாரப் பின்தங்கிய நிலையைக் களைய உதவுகின்றன.\nமேற்கண்டவற்றின் சூழலில், பின்வருவனவற்றில் எது சரியானது?",
            "options": [
                ("Both (A) and (R) are true, and (R) is the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-வின் சரியான விளக்கம்."),
                ("Both (A) and (R) are true, but (R) is not the correct explanation of (A).", "(A) மற்றும் (R) இரண்டும் உண்மை, ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல."),
                ("Assertion (A) is true, but Reason (R) is false.", "கூற்று (A) உண்மை, ஆனால் காரணம் (R) தவறு."),
                ("Assertion (A) is false, but Reason (R) is true.", "கூற்று (A) தவறு, ஆனால் காரணம் (R) உண்மை.")
            ],
            "correct_key": "A",
            "exp_en": "Both (A) and (R) are true, and (R) provides the substantive philosophical and political explanation for (A). Part XXI's asymmetric framework succeeds in holding India together precisely by granting customized protections and economic support tailored to specific regional challenges.",
            "exp_ta": "(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-க்கான தத்துவார்த்த மற்றும் அரசியல் விளக்கத்தை வழங்குகிறது. பகுதி XXI-ன் சமச்சீரற்ற கட்டமைப்பு குறிப்பிட்ட பிராந்திய சவால்களுக்கு ஏற்ப வடிவமைக்கப்பட்ட பாதுகாப்புகள் மற்றும் பொருளாதார ஆதரவை வழங்குவதன் மூலமே இந்தியாவை ஒருங்கிணைப்பதில் வெற்றி பெறுகிறது.",
            "why_a_en": "R directly justifies why Articles 371 to 371-J preserve national unity in A.",
            "why_a_ta": "சரத்துகள் 371 முதல் 371-J வரை A-ல் எவ்வாறு தேசிய ஒற்றுமையைப் பாதுகாக்கின்றன என்பதை R நேரடியாக நியாயப்படுத்துகிறது.",
            "why_b_en": "R is the direct explanation of A.",
            "why_b_ta": "R என்பது A-ன் நேரடி விளக்கம்.",
            "why_c_en": "R is true.",
            "why_c_ta": "R உண்மை.",
            "why_d_en": "A is true.",
            "why_d_ta": "A உண்மை.",
            "tip_en": "This overarching theme is frequently tested in TNPSC Mains Paper 2 as well as Prelims conceptual questions.",
            "tip_ta": "இந்த முதன்மைக் கருத்து TNPSC முதன்மைத் தேர்வு தாள் 2 மற்றும் முதல்நிலை கருத்தியல் வினாக்களில் அடிக்கடி கேட்கப்படுகிறது.",
            "fact_en": "Granville Austin hailed the Indian Constitution's flexibility in managing sub-national identities without Balkanization.",
            "fact_ta": "கிரான்வில் ஆஸ்டின் பிளவுபடாமல் துணை தேசிய அடையாளங்களை நிர்வகிப்பதில் இந்திய அரசியலமைப்பின் நெகிழ்வுத்தன்மையைப் பாராட்டினார்."
        }
    ]

    questions = []
    for i, item in enumerate(raw_data, 1):
        qid = f"SPS_R_{i:03d}"
        opts = item["options"]
        correct_key = item["correct_key"]
        q = make_sps_q(
            qid=qid,
            diff="Hard",
            qtype="Assertion and Reason",
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
            correct_key=correct_key,
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
            tags=["polity", "special_provisions_states", "reasoning", item["subtopic"].lower().replace(" ", "_")]
        )
        questions.append(q)
    return questions

def build_reasoning_file():
    qs = get_reasoning_questions()
    print(f"Generated {len(qs)} raw Reasoning questions for Special Provisions for States.")
    balanced = randomize_and_balance_dataset(qs, seed=42)
    
    out_dir = os.path.join("data", "questions", "polity")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "special_provisions_states_reasoning.json")
    alias_path = os.path.join(out_dir, "special_provisions_states_assertion_reason.json")
    
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(balanced, f, ensure_ascii=False, indent=2)
    with open(alias_path, "w", encoding="utf-8") as f:
        json.dump(balanced, f, ensure_ascii=False, indent=2)
    print(f"Saved balanced Reasoning MCQs to {out_path} and alias {alias_path}")
    
    rep = ContentValidator.validate_file(out_path, expected_count=25, expected_prefix="SPS_R_")
    print(f"Validation: {'PASS' if rep.is_valid else 'FAIL'} | Total: {rep.total_audited}")
    print(f"Keys: {rep.key_distribution}")
    if not rep.is_valid:
        for iss in rep.issues:
            print("  Issue:", iss.severity, iss.field_name, iss.message)
    return rep.is_valid

if __name__ == "__main__":
    build_reasoning_file()
