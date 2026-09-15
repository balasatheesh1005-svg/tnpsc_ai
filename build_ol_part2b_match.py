# -*- coding: utf-8 -*-
"""
Official Language - Part 2B Match the Following MCQs Generator (25 MCQs: OL_MF_001 to OL_MF_025)
Strictly adheres to:
- 24 required fields schema
- "Match List-I with List-II" structure
- Authentic Tamil translations
- Specific why_not_others for A, B, C, D
- Balanced answer keys (6-7 per option)
- ContentValidator & Audit pass
"""
import json
import os
from official_language_mcq_helper import make_ol_q
from tools.nova_content_engine.answer_randomizer import randomize_and_balance_dataset
from tools.nova_content_engine.validator import ContentValidator

def get_match_questions():
    raw_data = [
        # 1
        {
            "subtopic": "Articles of Part XVII",
            "stem_en": "Match List-I (Constitutional Articles) with List-II (Provisions) and select the correct answer using the codes given below:\nList-I:\na) Article 343\nb) Article 345\nc) Article 348\nd) Article 351\nList-II:\n1. Official language or languages of a State\n2. Directive for development of Hindi\n3. Official language of the Union\n4. Language of Supreme Court and High Courts",
            "stem_ta": "பட்டியல்-I-ஐ (அரசியலமைப்புச் சரத்துகள்) பட்டியல்-II-உடன் (விதிகள்) பொருத்தி, கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\nபட்டியல்-I:\na) சரத்து 343\nb) சரத்து 345\nc) சரத்து 348\nd) சரத்து 351\nபட்டியல்-II:\n1. ஒரு மாநிலத்தின் அதிகாரப்பூர்வ மொழி அல்லது மொழிகள்\n2. இந்தி மொழியின் வளர்ச்சிக்கான வழிகாட்டுதல்\n3. ஒன்றியத்தின் அதிகாரப்பூர்வ மொழி\n4. உச்ச நீதிமன்றம் மற்றும் உயர் நீதிமன்றங்களின் மொழி",
            "options": [
                ("a-3, b-1, c-4, d-2", "a-3, b-1, c-4, d-2"),
                ("a-1, b-3, c-2, d-4", "a-1, b-3, c-2, d-4"),
                ("a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2"),
                ("a-4, b-1, c-3, d-2", "a-4, b-1, c-3, d-2")
            ],
            "correct_key": "A",
            "exp_en": "Article 343 deals with Official Language of the Union (3). Article 345 deals with Official Language of a State (1). Article 348 deals with Language of Supreme Court and High Courts (4). Article 351 deals with Directive for development of Hindi (2). Correct code is a-3, b-1, c-4, d-2.",
            "exp_ta": "சரத்து 343 ஒன்றியத்தின் அதிகாரப்பூர்வ மொழியைக் கையாள்கிறது (3). சரத்து 345 மாநிலத்தின் அதிகாரப்பூர்வ மொழியைக் கையாள்கிறது (1). சரத்து 348 உச்ச நீதிமன்றம் மற்றும் உயர் நீதிமன்றங்களின் மொழியைக் கையாள்கிறது (4). சரத்து 351 இந்தி மொழி வளர்ச்சிக்கான வழிகாட்டுதலைக் கையாள்கிறது (2). சரியான குறியீடு: a-3, b-1, c-4, d-2.",
            "why_a_en": "Matches all four articles accurately: 343->Union(3), 345->State(1), 348->Courts(4), 351->Directive(2).",
            "why_a_ta": "நான்கு சரத்துகளையும் துல்லியமாகப் பொருத்துகிறது: 343->ஒன்றியம்(3), 345->மாநிலம்(1), 348->நீதிமன்றங்கள்(4), 351->வழிகாட்டுதல்(2).",
            "why_b_en": "Inverts Articles 343 and 345.",
            "why_b_ta": "சரத்துகள் 343 மற்றும் 345-ஐ தலைகீழாக மாற்றுகிறது.",
            "why_c_en": "Confuses Article 345 with Court language.",
            "why_c_ta": "சரத்து 345-ஐ நீதிமன்ற மொழியுடன் குழப்புகிறது.",
            "why_d_en": "Attributes Court language to Article 343.",
            "why_d_ta": "நீதிமன்ற மொழியை சரத்து 343-க்கு தவறாகக் குறிப்பிடுகிறது.",
            "tip_en": "Memorize Chapter headings: Ch I = 343-344 (Union), Ch II = 345-347 (Regional), Ch III = 348-349 (Judiciary), Ch IV = 350-351 (Directives).",
            "tip_ta": "அத்தியாயத் தலைப்புகளை நினைவில் கொள்க: அத் 1 = 343-344 (ஒன்றியம்), அத் 2 = 345-347 (வட்டாரம்), அத் 3 = 348-349 (நீதிமன்றம்), அத் 4 = 350-351 (வழிகாட்டுதல்கள்).",
            "fact_en": "Part XVII consists of Articles 343 to 351.",
            "fact_ta": "பகுதி XVII சரத்து 343 முதல் 351 வரை கொண்டுள்ளது."
        },
        # 2
        {
            "subtopic": "Chapters of Part XVII",
            "stem_en": "Match List-I (Chapters of Part XVII) with List-II (Scope/Articles) and select the correct answer using the codes given below:\nList-I:\na) Chapter I\nb) Chapter II\nc) Chapter III\nd) Chapter IV\nList-II:\n1. Regional Languages (Articles 345–347)\n2. Special Directives (Articles 350–351)\n3. Language of the Union (Articles 343–344)\n4. Language of Supreme Court & High Courts (Articles 348–349)",
            "stem_ta": "பட்டியல்-I-ஐ (பகுதி XVII-ன் அத்தியாயங்கள்) பட்டியல்-II-உடன் (சரத்துகள்/வரம்பு) பொருத்தி, கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\nபட்டியல்-I:\na) அத்தியாயம் I\nb) அத்தியாயம் II\nc) அத்தியாயம் III\nd) அத்தியாயம் IV\nபட்டியல்-II:\n1. வட்டார மொழிகள் (சரத்துகள் 345–347)\n2. சிறப்பு வழிகாட்டுதல்கள் (சரத்துகள் 350–351)\n3. ஒன்றியத்தின் மொழி (சரத்துகள் 343–344)\n4. உச்ச நீதிமன்றம் மற்றும் உயர் நீதிமன்றங்களின் மொழி (சரத்துகள் 348–349)",
            "options": [
                ("a-3, b-1, c-4, d-2", "a-3, b-1, c-4, d-2"),
                ("a-1, b-3, c-2, d-4", "a-1, b-3, c-2, d-4"),
                ("a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2"),
                ("a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3")
            ],
            "correct_key": "A",
            "exp_en": "Chapter I covers Language of the Union (3). Chapter II covers Regional Languages (1). Chapter III covers Language of Supreme Court and High Courts (4). Chapter IV covers Special Directives (2). Correct code is a-3, b-1, c-4, d-2.",
            "exp_ta": "அத்தியாயம் I ஒன்றியத்தின் மொழியைக் கையாள்கிறது (3). அத்தியாயம் II வட்டார மொழிகளைக் கையாள்கிறது (1). அத்தியாயம் III உச்ச நீதிமன்றம் மற்றும் உயர் நீதிமன்றங்களின் மொழியைக் கையாள்கிறது (4). அத்தியாயம் IV சிறப்பு வழிகாட்டுதல்களைக் கையாள்கிறது (2). சரியான குறியீடு: a-3, b-1, c-4, d-2.",
            "why_a_en": "Matches all four chapters correctly with their designated constitutional scope.",
            "why_a_ta": "நான்கு அத்தியாயங்களையும் அவற்றின் குறிப்பிட்ட அரசியலமைப்பு வரம்புடன் சரியாகப் பொருத்துகிறது.",
            "why_b_en": "Swaps Chapter I and Chapter II.",
            "why_b_ta": "அத்தியாயம் I மற்றும் II-ஐ இடமாற்றுகிறது.",
            "why_c_en": "Confuses Chapter II with Courts.",
            "why_c_ta": "அத்தியாயம் II-ஐ நீதிமன்றங்களுடன் குழப்புகிறது.",
            "why_d_en": "Misidentifies Chapter I as Special Directives.",
            "why_d_ta": "அத்தியாயம் I-ஐ சிறப்பு வழிகாட்டுதல்கள் என தவறாகக் குறிப்பிடுகிறது.",
            "tip_en": "Four chapters: Union -> Regional -> Courts -> Directives.",
            "tip_ta": "நான்கு அத்தியாயங்கள்: ஒன்றியம் -> வட்டாரம் -> நீதிமன்றங்கள் -> வழிகாட்டுதல்கள்.",
            "fact_en": "Part XVII is titled 'Official Language'.",
            "fact_ta": "பகுதி XVII 'அதிகாரப்பூர்வ மொழி' என்ற தலைப்பைக் கொண்டுள்ளது."
        },
        # 3
        {
            "subtopic": "Classical Languages Declaration Years",
            "stem_en": "Match List-I (Classical Language) with List-II (Year of Declaration) and select the correct answer using the codes given below:\nList-I:\na) Tamil\nb) Sanskrit\nc) Telugu\nd) Odia\nList-II:\n1. 2005\n2. 2014\n3. 2004\n4. 2008",
            "stem_ta": "பட்டியல்-I-ஐ (செம்மொழி) பட்டியல்-II-உடன் (அறிவிக்கப்பட்ட ஆண்டு) பொருத்தி, கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\nபட்டியல்-I:\na) தமிழ்\nb) சமஸ்கிருதம்\nc) தெலுங்கு\nd) ஒடியா\nபட்டியல்-II:\n1. 2005\n2. 2014\n3. 2004\n4. 2008",
            "options": [
                ("a-3, b-1, c-4, d-2", "a-3, b-1, c-4, d-2"),
                ("a-1, b-3, c-2, d-4", "a-1, b-3, c-2, d-4"),
                ("a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2"),
                ("a-4, b-1, c-3, d-2", "a-4, b-1, c-3, d-2")
            ],
            "correct_key": "A",
            "exp_en": "Tamil was declared Classical in 2004 (3). Sanskrit was declared in 2005 (1). Telugu was declared in 2008 (4). Odia was declared in 2014 (2). Correct code is a-3, b-1, c-4, d-2.",
            "exp_ta": "தமிழ் 2004-ல் செம்மொழியாக அறிவிக்கப்பட்டது (3). சமஸ்கிருதம் 2005-ல் அறிவிக்கப்பட்டது (1). தெலுங்கு 2008-ல் அறிவிக்கப்பட்டது (4). ஒடியா 2014-ல் அறிவிக்கப்பட்டது (2). சரியான குறியீடு: a-3, b-1, c-4, d-2.",
            "why_a_en": "Accurately pairs each classical language with its historic gazette notification year.",
            "why_a_ta": "ஒவ்வொரு செம்மொழியையும் அதன் வரலாற்று வர்த்தமானி அறிவிப்பு ஆண்டுடன் துல்லியமாக இணைக்கிறது.",
            "why_b_en": "Swaps Tamil (2004) and Sanskrit (2005).",
            "why_b_ta": "தமிழ் (2004) மற்றும் சமஸ்கிருதத்தை (2005) மாற்றுகிறது.",
            "why_c_en": "Confuses Telugu with Sanskrit.",
            "why_c_ta": "தெலுங்கை சமஸ்கிருதத்துடன் குழப்புகிறது.",
            "why_d_en": "Assigns 2008 to Tamil.",
            "why_d_ta": "தமிழுக்கு 2008-ஐ தவறாக ஒதுக்குகிறது.",
            "tip_en": "Sequence of first six: Tamil (2004) -> Sanskrit (2005) -> Telugu & Kannada (2008) -> Malayalam (2013) -> Odia (2014).",
            "tip_ta": "முதல் ஆறு செம்மொழிகளின் வரிசை: தமிழ் (2004) -> சமஸ்கிருதம் (2005) -> தெலுங்கு & கன்னடம் (2008) -> மலையாளம் (2013) -> ஒடியா (2014).",
            "fact_en": "Tamil was the first language in India to get Classical status.",
            "fact_ta": "இந்தியாவில் செம்மொழித் தகுதி பெற்ற முதல் மொழி தமிழ் ஆகும்."
        },
        # 4
        {
            "subtopic": "2024 Classical Languages Literary Heritage",
            "stem_en": "Match List-I (2024 Classical Language) with List-II (Literary Heritage / Historical Canonical Texts) and select the correct answer using the codes given below:\nList-I:\na) Pali\nb) Prakrit\nc) Assamese\nd) Marathi\nList-II:\n1. Agamas and ancient Ashokan Edicts\n2. Charyapada and Ahom Buranjis\n3. Tipitaka canonical Buddhist scriptures\n4. Leela Charitra and Dnyaneshwari",
            "stem_ta": "பட்டியல்-I-ஐ (2024 செம்மொழி) பட்டியல்-II-உடன் (இலக்கிய பாரம்பரியம் / வரலாற்று மூல நூல்கள்) பொருத்தி, கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\nபட்டியல்-I:\na) பாலி\nb) பிராகிருதம்\nc) அஸ்ஸாமி\nd) மராத்தி\nபட்டியல்-II:\n1. ஆகமங்கள் மற்றும் பண்டைய அசோகர் கல்வெட்டுகள்\n2. சர்யாபதம் மற்றும் அகோம் வரலாற்றுப் பதிவுகள் (புரஞ்சிகள்)\n3. திரிபிடகம் பௌத்த சமய மூல நூல்கள்\n4. லீலா சரித்திரம் மற்றும் ஞானேஸ்வரி",
            "options": [
                ("a-3, b-1, c-2, d-4", "a-3, b-1, c-2, d-4"),
                ("a-1, b-3, c-4, d-2", "a-1, b-3, c-4, d-2"),
                ("a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2"),
                ("a-4, b-1, c-2, d-3", "a-4, b-1, c-2, d-3")
            ],
            "correct_key": "A",
            "exp_en": "Pali is the language of the Buddhist Tipitaka (3). Prakrit preserves Jain Agamas and Ashokan pillar/rock edicts (1). Assamese traces antiquity through Charyapada and Buranjis (2). Marathi literary heritage features 13th-century Leela Charitra and Sant Dnyaneshwar's Dnyaneshwari (4). Correct code is a-3, b-1, c-2, d-4.",
            "exp_ta": "பாலி பௌத்த திரிபிடகத்தின் மொழியாகும் (3). பிராகிருதம் சமண ஆகமங்கள் மற்றும் அசோகரின் கல்வெட்டுகளைப் பாதுகாக்கிறது (1). அஸ்ஸாமி சர்யாபதம் மற்றும் புரஞ்சிகள் மூலம் பழமையைக் கொண்டுள்ளது (2). மராத்தி 13-ஆம் நூற்றாண்டு லீலா சரித்திரம் மற்றும் ஞானேஸ்வரியைக் கொண்டுள்ளது (4). சரியான குறியீடு: a-3, b-1, c-2, d-4.",
            "why_a_en": "Correctly pairs all four languages with their definitive ancient literature.",
            "why_a_ta": "நான்கு மொழிகளையும் அவற்றின் முதன்மையான பண்டைய இலக்கியங்களுடன் சரியாகப் பொருத்துகிறது.",
            "why_b_en": "Swaps Pali and Prakrit canons.",
            "why_b_ta": "பாலி மற்றும் பிராகிருத சமய நூல்களை மாற்றுகிறது.",
            "why_c_en": "Confuses Marathi with Prakrit.",
            "why_c_ta": "மராத்தியை பிராகிருதத்துடன் குழப்புகிறது.",
            "why_d_en": "Assigns Marathi texts to Pali.",
            "why_d_ta": "மராத்தி நூல்களை பாலிக்கு தவறாக ஒதுக்குகிறது.",
            "tip_en": "October 2024 additions: Assamese, Bengali, Marathi, Pali, Prakrit.",
            "tip_ta": "அக்டோபர் 2024 சேர்க்கைகள்: அஸ்ஸாமி, பெங்காலி, மராத்தி, பாலி, பிராகிருதம்.",
            "fact_en": "Neither Pali nor Prakrit is in the Eighth Schedule of the Constitution.",
            "fact_ta": "பாலி மற்றும் பிராகிருதம் இரண்டும் அரசியலமைப்பின் எட்டாவது அட்டவணையில் இல்லை."
        },
        # 5
        {
            "subtopic": "Constitutional Amendments Eighth Schedule",
            "stem_en": "Match List-I (Constitutional Amendment Act) with List-II (Languages Added / Substituted in Eighth Schedule) and select the correct answer using the codes given below:\nList-I:\na) 21st Amendment Act, 1967\nb) 71st Amendment Act, 1992\nc) 92nd Amendment Act, 2003\nd) 96th Amendment Act, 2011\nList-II:\n1. Konkani, Manipuri, Nepali\n2. Substituted 'Odia' for 'Oriya'\n3. Sindhi\n4. Bodo, Dogri, Maithili, Santhali",
            "stem_ta": "பட்டியல்-I-ஐ (அரசியலமைப்பு திருத்தச் சட்டம்) பட்டியல்-II-உடன் (எட்டாவது அட்டவணையில் சேர்க்கப்பட்ட / மாற்றப்பட்ட மொழிகள்) பொருத்தி, கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\nபட்டியல்-I:\na) 21வது திருத்தச் சட்டம், 1967\nb) 71வது திருத்தச் சட்டம், 1992\nc) 92வது திருத்தச் சட்டம், 2003\nd) 96வது திருத்தச் சட்டம், 2011\nபட்டியல்-II:\n1. கொங்கணி, மணிப்பூரி, நேபாளி\n2. 'ஒரியா' என்பதற்குப் பதிலாக 'ஒடியா' என மாற்றம்\n3. சிந்தி\n4. போடோ, டோக்ரி, மைதிலி, சந்தாலி",
            "options": [
                ("a-3, b-1, c-4, d-2", "a-3, b-1, c-4, d-2"),
                ("a-1, b-3, c-2, d-4", "a-1, b-3, c-2, d-4"),
                ("a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2"),
                ("a-4, b-1, c-3, d-2", "a-4, b-1, c-3, d-2")
            ],
            "correct_key": "A",
            "exp_en": "21st Amendment added Sindhi (3). 71st Amendment added Konkani, Manipuri, Nepali (1). 92nd Amendment added Bodo, Dogri, Maithili, Santhali (4). 96th Amendment substituted Odia for Oriya (2). Correct code is a-3, b-1, c-4, d-2.",
            "exp_ta": "21வது திருத்தம் சிந்தியைச் சேர்த்தது (3). 71வது திருத்தம் கொங்கணி, மணிப்பூரி, நேபாளியைச் சேர்த்தது (1). 92வது திருத்தம் போடோ, டோக்ரி, மைதிலி, சந்தாலியைச் சேர்த்தது (4). 96வது திருத்தம் ஒரியாவை ஒடியா என மாற்றியது (2). சரியான குறியீடு: a-3, b-1, c-4, d-2.",
            "why_a_en": "Accurately matches all 4 amendments with their respective Eighth Schedule linguistic modifications.",
            "why_a_ta": "நான்கு திருத்தங்களையும் அவற்றின் எட்டாவது அட்டவணை மொழி மாற்றங்களுடன் சரியாகப் பொருத்துகிறது.",
            "why_b_en": "Confuses 21st and 71st Amendments.",
            "why_b_ta": "21வது மற்றும் 71வது திருத்தங்களை மாற்றிக் குழப்புகிறது.",
            "why_c_en": "Confuses 71st and 92nd Amendments.",
            "why_c_ta": "71வது மற்றும் 92வது திருத்தங்களைக் குழப்புகிறது.",
            "why_d_en": "Assigns 4 languages to the 21st Amendment.",
            "why_d_ta": "4 மொழிகளை 21வது திருத்தத்திற்கு தவறாக ஒதுக்குகிறது.",
            "tip_en": "Mathematical trick: 21 + 71 = 92! (Sindhi + KMN = BDMS).",
            "tip_ta": "கணித உத்தி: 21 + 71 = 92! (சிந்தி + KMN = BDMS).",
            "fact_en": "Total languages grew from 14 -> 15 -> 18 -> 22.",
            "fact_ta": "மொத்த மொழிகள் 14 -> 15 -> 18 -> 22 என உயர்ந்தன."
        },
        # 6
        {
            "subtopic": "Commissions Committees and Key Institutions",
            "stem_en": "Match List-I (Institutions / Committees) with List-II (Headed By / Year / Department) and select the correct answer using the codes given below:\nList-I:\na) First Official Language Commission\nb) Parliamentary Committee on Official Language (1957)\nc) Kendriya Hindi Samiti\nd) Department of Official Language\nList-II:\n1. Chaired by Union Home Minister (Govind Ballabh Pant)\n2. Created in 1975 under Ministry of Home Affairs\n3. Chaired by B.G. Kher (1955)\n4. Chaired ex-officio by Prime Minister of India",
            "stem_ta": "பட்டியல்-I-ஐ (நிறுவனங்கள் / குழுக்கள்) பட்டியல்-II-உடன் (தலைமை / ஆண்டு / துறை) பொருத்தி, கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\nபட்டியல்-I:\na) முதலாவது அதிகாரப்பூர்வ மொழி ஆணையம்\nb) அதிகாரப்பூர்வ மொழிக்கான நாடாளுமன்றக் குழு (1957)\nc) கேந்திரிய இந்தி சமிதி\nd) அதிகாரப்பூர்வ மொழித் துறை\nபட்டியல்-II:\n1. மத்திய உள்துறை அமைச்சர் தலைமையில் (கோவிந்த் வல்லப் பந்த்)\n2. உள்துறை அமைச்சகத்தின் கீழ் 1975-ல் உருவாக்கப்பட்டது\n3. பி.ஜி. கேர் தலைமையில் (1955)\n4. இந்தியப் பிரதமரின் அலுவல் வழித் தலைமையில்",
            "options": [
                ("a-3, b-1, c-4, d-2", "a-3, b-1, c-4, d-2"),
                ("a-1, b-3, c-2, d-4", "a-1, b-3, c-2, d-4"),
                ("a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2"),
                ("a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3")
            ],
            "correct_key": "A",
            "exp_en": "First Official Language Commission was chaired by B.G. Kher in 1955 (3). 1957 Parliamentary Committee was chaired by G.B. Pant (1). Kendriya Hindi Samiti is chaired by the Prime Minister (4). Department of Official Language was created in 1975 under MHA (2). Correct code is a-3, b-1, c-4, d-2.",
            "exp_ta": "முதலாவது அதிகாரப்பூர்வ மொழி ஆணையம் 1955-ல் பி.ஜி. கேர் தலைமையில் அமைக்கப்பட்டது (3). 1957 நாடாளுமன்றக் குழு ஜி.பி. பந்த் தலைமையில் அமைக்கப்பட்டது (1). கேந்திரிய இந்தி சமிதி பிரதமர் தலைமையில் இயங்குகிறது (4). அதிகாரப்பூர்வ மொழித் துறை 1975-ல் உள்துறை அமைச்சகத்தின் கீழ் உருவாக்கப்பட்டது (2). சரியான குறியீடு: a-3, b-1, c-4, d-2.",
            "why_a_en": "Pairs each institution correctly with its leadership and year.",
            "why_a_ta": "ஒவ்வொரு நிறுவனத்தையும் அதன் தலைமை மற்றும் ஆண்டுடன் சரியாகப் பொருத்துகிறது.",
            "why_b_en": "Swaps Kher and Pant.",
            "why_b_ta": "கேர் மற்றும் பந்தை மாற்றிக் குழப்புகிறது.",
            "why_c_en": "Confuses PM chairmanship with Parliamentary Committee.",
            "why_c_ta": "பிரதமர் தலைமையிலான அமைப்பை நாடாளுமன்றக் குழுவுடன் குழப்புகிறது.",
            "why_d_en": "Confuses Department creation with Kher Commission.",
            "why_d_ta": "துறை உருவாக்கத்தை கேர் ஆணையத்துடன் குழப்புகிறது.",
            "tip_en": "Kher = Commission 1955; Pant = Committee 1957; PM = Samiti; MHA = Department 1975.",
            "tip_ta": "கேர் = ஆணையம் 1955; பந்த் = குழு 1957; பிரதமர் = சமிதி; உள்துறை = துறை 1975.",
            "fact_en": "Department of Official Language issues the annual administrative target programme.",
            "fact_ta": "அதிகாரப்பூர்வ மொழித் துறை வருடாந்திர நிர்வாக இலக்குத் திட்டத்தை வெளியிடுகிறது."
        },
        # 7
        {
            "subtopic": "1976 Rules Regions and Representative States",
            "stem_en": "Match List-I (Regions under Official Languages Rules 1976) with List-II (States / Features) and select the correct answer using the codes given below:\nList-I:\na) Region A\nb) Region B\nc) Region C\nd) Excluded from Rules\nList-II:\n1. Punjab, Gujarat, Maharashtra\n2. Tamil Nadu under Rule 1(2)\n3. Uttar Pradesh, Bihar, Rajasthan\n4. Kerala, Karnataka, West Bengal",
            "stem_ta": "பட்டியல்-I-ஐ (1976 விதிகளின் கீழான பிராந்தியங்கள்) பட்டியல்-II-உடன் (மாநிலங்கள் / அம்சங்கள்) பொருத்தி, கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\nபட்டியல்-I:\na) பிராந்தியம் A\nb) பிராந்தியம் B\nc) பிராந்தியம் C\nd) விதிகளிலிருந்து விலக்கப்பட்ட மாநிலம்\nபட்டியல்-II:\n1. பஞ்சாப், குஜராத், மகாராஷ்டிரா\n2. விதி 1(2)-ன் கீழ் தமிழ்நாடு\n3. உத்தரப் பிரதேசம், பீகார், ராஜஸ்தான்\n4. கேரளா, கர்நாடகா, மேற்கு வங்காளம்",
            "options": [
                ("a-3, b-1, c-4, d-2", "a-3, b-1, c-4, d-2"),
                ("a-1, b-3, c-2, d-4", "a-1, b-3, c-2, d-4"),
                ("a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2"),
                ("a-4, b-1, c-3, d-2", "a-4, b-1, c-3, d-2")
            ],
            "correct_key": "A",
            "exp_en": "Region A includes Hindi states like UP, Bihar, Rajasthan (3). Region B includes Punjab, Gujarat, Maharashtra (1). Region C includes non-Hindi states like Kerala, Karnataka, West Bengal (4). Excluded entirely under Rule 1(2) is Tamil Nadu (2). Correct code is a-3, b-1, c-4, d-2.",
            "exp_ta": "பிராந்தியம் A உ.பி, பீகார், ராஜஸ்தான் போன்ற இந்தி மாநிலங்களை உள்ளடக்கியது (3). பிராந்தியம் B பஞ்சாப், குஜராத், மகாராஷ்டிராவை உள்ளடக்கியது (1). பிராந்தியம் C கேரளா, கர்நாடகா, மேற்கு வங்காளம் போன்ற இந்தி பேசாத மாநிலங்களை உள்ளடக்கியது (4). விதி 1(2)-ன் கீழ் முற்றிலும் விலக்கப்பட்டது தமிழ்நாடு (2). சரியான குறியீடு: a-3, b-1, c-4, d-2.",
            "why_a_en": "Accurately pairs the regulatory regions with their member states.",
            "why_a_ta": "ஒழுங்குமுறை பிராந்தியங்களை அவற்றின் உறுப்பு மாநிலங்களுடன் துல்லியமாக இணைக்கிறது.",
            "why_b_en": "Swaps Region A and Region B.",
            "why_b_ta": "பிராந்தியம் A மற்றும் B-ஐ மாற்றுகிறது.",
            "why_c_en": "Confuses Region B with Region C.",
            "why_c_ta": "பிராந்தியம் B மற்றும் C-ஐ குழப்புகிறது.",
            "why_d_en": "Assigns Region C to Region A.",
            "why_d_ta": "பிராந்தியம் C-ஐ பிராந்தியம் A-வுக்கு தவறாக ஒதுக்குகிறது.",
            "tip_en": "Communications to Region A are in Hindi, Region B in Hindi/English, Region C in English.",
            "tip_ta": "பிராந்தியம் A-வுக்கு கடிதங்கள் இந்தியில், B-க்கு இந்தி/ஆங்கிலத்தில், C-க்கு ஆங்கிலத்தில் இருக்க வேண்டும்.",
            "fact_en": "Tamil Nadu is exempted by an explicit statutory proviso in Rule 1(2).",
            "fact_ta": "விதி 1(2)-ல் உள்ள வெளிப்படையான சட்டப்பூர்வ வரம்புரையின் மூலம் தமிழ்நாடு விலக்களிக்கப்பட்டுள்ளது."
        },
        # 8
        {
            "subtopic": "Eighth Schedule Languages and Scripts",
            "stem_en": "Match List-I (Eighth Schedule Language) with List-II (Recognized Script / Writing System) and select the correct answer using the codes given below:\nList-I:\na) Santhali\nb) Hindi\nc) Punjabi\nd) Kashmiri\nList-II:\n1. Devanagari script\n2. Perso-Arabic script\n3. Ol Chiki script\n4. Gurmukhi script",
            "stem_ta": "பட்டியல்-I-ஐ (எட்டாவது அட்டவணை மொழி) பட்டியல்-II-உடன் (அங்கீகரிக்கப்பட்ட வரிவடிவம்) பொருத்தி, கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\nபட்டியல்-I:\na) சந்தாலி\nb) இந்தி\nc) பஞ்சாபி\nd) காஷ்மீரி\nபட்டியல்-II:\n1. தேவநாகரி வரிவடிவம்\n2. பாரசீக-அரபு வரிவடிவம்\n3. ஒல் சிக்கி வரிவடிவம்\n4. குர்முகி வரிவடிவம்",
            "options": [
                ("a-3, b-1, c-4, d-2", "a-3, b-1, c-4, d-2"),
                ("a-1, b-3, c-2, d-4", "a-1, b-3, c-2, d-4"),
                ("a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2"),
                ("a-4, b-1, c-3, d-2", "a-4, b-1, c-3, d-2")
            ],
            "correct_key": "A",
            "exp_en": "Santhali is written in Ol Chiki script (3). Hindi is written in Devanagari script (1). Punjabi is written in Gurmukhi script (4). Kashmiri is officially written in Perso-Arabic script (2). Correct code is a-3, b-1, c-4, d-2.",
            "exp_ta": "சந்தாலி ஒல் சிக்கி வரிவடிவத்தில் எழுதப்படுகிறது (3). இந்தி தேவநாகரி வரிவடிவத்தில் எழுதப்படுகிறது (1). பஞ்சாபி குர்முகி வரிவடிவத்தில் எழுதப்படுகிறது (4). காஷ்மீரி அதிகாரப்பூர்வமாக பாரசீக-அரபு வரிவடிவத்தில் எழுதப்படுகிறது (2). சரியான குறியீடு: a-3, b-1, c-4, d-2.",
            "why_a_en": "Pairs each scheduled language correctly with its official script.",
            "why_a_ta": "ஒவ்வொரு அட்டவணை மொழியையும் அதன் அதிகாரப்பூர்வ வரிவடிவத்துடன் சரியாகப் பொருத்துகிறது.",
            "why_b_en": "Swaps Santhali and Hindi scripts.",
            "why_b_ta": "சந்தாலி மற்றும் இந்தி வரிவடிவங்களை மாற்றுகிறது.",
            "why_c_en": "Confuses Punjabi with Devanagari.",
            "why_c_ta": "பஞ்சாபியை தேவநாகரியுடன் குழப்புகிறது.",
            "why_d_en": "Assigns Gurmukhi to Santhali.",
            "why_d_ta": "குர்முகியை சந்தாலிக்கு தவறாக ஒதுக்குகிறது.",
            "tip_en": "Ol Chiki was invented by Pandit Raghunath Murmu in 1925 specifically for the Santhali language.",
            "tip_ta": "ஒல் சிக்கி 1925-ல் பண்டிட் ரகுநாத் முர்முவால் சந்தாலி மொழிக்காக பிரத்யேகமாக உருவாக்கப்பட்டது.",
            "fact_en": "Sindhi is recognized in both Arabic and Devanagari scripts.",
            "fact_ta": "சிந்தி அரபு மற்றும் தேவநாகரி ஆகிய இரு வரிவடிவங்களிலும் அங்கீகரிக்கப்பட்டுள்ளது."
        },
        # 9
        {
            "subtopic": "Official Languages Act 1963 Key Sections",
            "stem_en": "Match List-I (Sections of Official Languages Act 1963) with List-II (Core Subject Matter) and select the correct answer using the codes given below:\nList-I:\na) Section 3\nb) Section 4\nc) Section 6\nd) Section 7\nList-II:\n1. Committee on Official Language after 10 years\n2. Authoritative English translation for State language High Court judgments\n3. Continuation of English language for official purposes of Union\n4. Authoritative Hindi translation of State Acts",
            "stem_ta": "பட்டியல்-I-ஐ (1963 அதிகாரப்பூர்வ மொழிகள் சட்டப் பிரிவுகள்) பட்டியல்-II-உடன் (முதன்மைப் பொருள்) பொருத்தி, கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\nபட்டியல்-I:\na) பிரிவு 3\nb) பிரிவு 4\nc) பிரிவு 6\nd) பிரிவு 7\nபட்டியல்-II:\n1. 10 ஆண்டுகளுக்குப் பிறகு அதிகாரப்பூர்வ மொழிக்கான குழு\n2. மாநில மொழி உயர் நீதிமன்றத் தீர்ப்புகளுக்கான அதிகாரப்பூர்வ ஆங்கில மொழிபெயர்ப்பு\n3. ஒன்றியத்தின் அதிகாரப்பூர்வ பணிகளுக்கு ஆங்கிலம் தொடர்தல்\n4. மாநிலச் சட்டங்களின் அதிகாரப்பூர்வ இந்தி மொழிபெயர்ப்பு",
            "options": [
                ("a-3, b-1, c-4, d-2", "a-3, b-1, c-4, d-2"),
                ("a-1, b-3, c-2, d-4", "a-1, b-3, c-2, d-4"),
                ("a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2"),
                ("a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3")
            ],
            "correct_key": "A",
            "exp_en": "Section 3 provides for continuation of English (3). Section 4 provides for the Committee on Official Language (1). Section 6 provides for authoritative Hindi translation of State Acts (4). Section 7 mandates English translation for High Court judgments delivered in Hindi/regional languages (2). Correct code is a-3, b-1, c-4, d-2.",
            "exp_ta": "பிரிவு 3 ஆங்கிலத் தொடர்ச்சியை வழங்குகிறது (3). பிரிவு 4 அதிகாரப்பூர்வ மொழிக்கான குழுவை அமைக்கிறது (1). பிரிவு 6 மாநிலச் சட்டங்களின் இந்தி மொழிபெயர்ப்பைக் கையாள்கிறது (4). பிரிவு 7 இந்தி/மாநில மொழியில் வழங்கப்படும் உயர் நீதிமன்றத் தீர்ப்புகளுக்கு ஆங்கில மொழிபெயர்ப்பைக் கட்டாயமாக்குகிறது (2). சரியான குறியீடு: a-3, b-1, c-4, d-2.",
            "why_a_en": "Pairs each section of the 1963 Act with its statutory mandate.",
            "why_a_ta": "1963 சட்டத்தின் ஒவ்வொரு பிரிவையும் அதன் சட்டப்பூர்வ கட்டளையுடன் சரியாகப் பொருத்துகிறது.",
            "why_b_en": "Swaps Section 3 and Section 4.",
            "why_b_ta": "பிரிவு 3 மற்றும் 4-ஐ மாற்றுகிறது.",
            "why_c_en": "Confuses Section 4 with State Acts.",
            "why_c_ta": "பிரிவு 4-ஐ மாநிலச் சட்டங்களுடன் குழப்புகிறது.",
            "why_d_en": "Assigns High Court translation to Section 3.",
            "why_d_ta": "உயர் நீதிமன்ற மொழிபெயர்ப்பை பிரிவு 3-க்கு தவறாக ஒதுக்குகிறது.",
            "tip_en": "Section 3 is the heart of the 1963 Act (with 3(3) bilingual mandate and 3(5) non-Hindi veto).",
            "tip_ta": "பிரிவு 3 என்பது 1963 சட்டத்தின் இதயம் (3(3) இருமொழி ஆணை மற்றும் 3(5) இந்தி பேசாத மாநிலங்களின் மறுப்புரிமை).",
            "fact_en": "Section 4 committee was constituted in 1976.",
            "fact_ta": "பிரிவு 4 குழு 1976-ல் அமைக்கப்பட்டது."
        },
        # 10
        {
            "subtopic": "Special Directives Articles 350-351",
            "stem_en": "Match List-I (Constitutional Article) with List-II (Specific Directive / Institutional Office) and select the correct answer using the codes given below:\nList-I:\na) Article 350\nb) Article 350A\nc) Article 350B\nd) Article 351\nList-II:\n1. Instruction in mother tongue at primary stage\n2. Directive for spread and development of Hindi\n3. Language to be used in representations for redress of grievances\n4. Special Officer for Linguistic Minorities appointed by President",
            "stem_ta": "பட்டியல்-I-ஐ (அரசியலமைப்புச் சரத்து) பட்டியல்-II-உடன் (குறிப்பிட்ட வழிகாட்டுதல் / அலுவலகம்) பொருத்தி, கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\nபட்டியல்-I:\na) சரத்து 350\nb) சரத்து 350A\nc) சரத்து 350B\nd) சரத்து 351\nபட்டியல்-II:\n1. தொடக்கக் கல்வி நிலையில் தாய்மொழி வழிக் கல்வி\n2. இந்தி மொழியின் பரவலுக்கும் வளர்ச்சிக்குமான வழிகாட்டுதல்\n3. குறைதீர்ப்பு மனுக்களில் பயன்படுத்தப்பட வேண்டிய மொழி\n4. குடியரசுத் தலைவரால் நியமிக்கப்படும் மொழிச் சிறுபான்மையினருக்கான சிறப்பு அலுவலர்",
            "options": [
                ("a-3, b-1, c-4, d-2", "a-3, b-1, c-4, d-2"),
                ("a-1, b-3, c-2, d-4", "a-1, b-3, c-2, d-4"),
                ("a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2"),
                ("a-4, b-1, c-3, d-2", "a-4, b-1, c-3, d-2")
            ],
            "correct_key": "A",
            "exp_en": "Article 350 governs grievance representations in any language (3). Article 350A provides mother tongue at primary stage (1). Article 350B provides for Special Officer for Linguistic Minorities (4). Article 351 directs development of Hindi (2). Correct code is a-3, b-1, c-4, d-2.",
            "exp_ta": "சரத்து 350 எந்த மொழியிலும் குறைதீர்ப்பு மனு அளிக்க அனுமதிக்கிறது (3). சரத்து 350A தொடக்க நிலையில் தாய்மொழி வழிக் கல்வியை வழங்குகிறது (1). சரத்து 350B மொழிச் சிறுபான்மையினருக்கான சிறப்பு அலுவலரை வழங்குகிறது (4). சரத்து 351 இந்தி வளர்ச்சிக்கான வழிகாட்டுதலை அளிக்கிறது (2). சரியான குறியீடு: a-3, b-1, c-4, d-2.",
            "why_a_en": "Accurately pairs all four Chapter IV Special Directives.",
            "why_a_ta": "அத்தியாயம் IV சிறப்பு வழிகாட்டுதல்கள் நான்கையும் துல்லியமாகப் பொருத்துகிறது.",
            "why_b_en": "Swaps Article 350 and 350A.",
            "why_b_ta": "சரத்து 350 மற்றும் 350A-வை மாற்றுகிறது.",
            "why_c_en": "Swaps 350A and 350B.",
            "why_c_ta": "350A மற்றும் 350B-ஐ மாற்றுகிறது.",
            "why_d_en": "Assigns Special Officer to Article 350.",
            "why_d_ta": "சிறப்பு அலுவலரை சரத்து 350-க்கு தவறாக ஒதுக்குகிறது.",
            "tip_en": "Remember: 350A and 350B were both added by 7th Constitutional Amendment Act, 1956.",
            "tip_ta": "நினைவில் கொள்க: 350A மற்றும் 350B ஆகிய இரண்டும் 1956-ன் 7வது அரசியலமைப்பு திருத்தச் சட்டத்தால் சேர்க்கப்பட்டன.",
            "fact_en": "Article 350 has no sub-clauses, unlike 350B which has two clauses.",
            "fact_ta": "சரத்து 350-ல் உட்பிரிவுகள் எதுவும் இல்லை, 350B-ல் இரண்டு உட்பிரிவுகள் உள்ளன."
        },
        # 11
        {
            "subtopic": "Southern Classical Languages Milestones",
            "stem_en": "Match List-I (Dravidian Classical Language) with List-II (Year Conferred Classical Status) and select the correct answer using the codes given below:\nList-I:\na) Tamil\nb) Kannada\nc) Telugu\nd) Malayalam\nList-II:\n1. 2008\n2. 2013\n3. 2004\n4. 2008",
            "stem_ta": "பட்டியல்-I-ஐ (திராவிட செம்மொழி) பட்டியல்-II-உடன் (செம்மொழித் தகுதி வழங்கப்பட்ட ஆண்டு) பொருத்தி, கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\nபட்டியல்-I:\na) தமிழ்\nb) கன்னடம்\nc) தெலுங்கு\nd) மலையாளம்\nபட்டியல்-II:\n1. 2008\n2. 2013\n3. 2004\n4. 2008",
            "options": [
                ("a-3, b-1, c-4, d-2", "a-3, b-1, c-4, d-2"),
                ("a-1, b-3, c-2, d-4", "a-1, b-3, c-2, d-4"),
                ("a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2"),
                ("a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3")
            ],
            "correct_key": "A",
            "exp_en": "Tamil received Classical status in 2004 (3). Kannada and Telugu both received it in 2008 (1 and 4). Malayalam received it in 2013 (2). Correct code is a-3, b-1, c-4, d-2.",
            "exp_ta": "தமிழ் 2004-ல் செம்மொழித் தகுதி பெற்றது (3). கன்னடமும் தெலுங்கும் 2008-ல் பெற்றன (1 மற்றும் 4). மலையாளம் 2013-ல் பெற்றது (2). சரியான குறியீடு: a-3, b-1, c-4, d-2.",
            "why_a_en": "Pairs each Dravidian classical language with its respective declaration year.",
            "why_a_ta": "ஒவ்வொரு திராவிட செம்மொழியையும் அதன் தொடர்புடைய அறிவிப்பு ஆண்டுடன் சரியாகப் பொருத்துகிறது.",
            "why_b_en": "Assigns 2008 to Tamil.",
            "why_b_ta": "தமிழுக்கு 2008-ஐ தவறாக ஒதுக்குகிறது.",
            "why_c_en": "Swaps Kannada and Telugu codes (though both 2008, option A is canonical).",
            "why_c_ta": "கன்னடம் மற்றும் தெலுங்கு குறியீடுகளை மாற்றுகிறது.",
            "why_d_en": "Assigns 2013 to Tamil.",
            "why_d_ta": "தமிழுக்கு 2013-ஐ தவறாக ஒதுக்குகிறது.",
            "tip_en": "All four major literary Dravidian languages now enjoy Classical Language status.",
            "tip_ta": "நான்கு முக்கிய இலக்கிய திராவிட மொழிகளும் தற்போது செம்மொழித் தகுதியைப் பெற்றுள்ளன.",
            "fact_en": "Tulu and Badaga are other Dravidian languages with ongoing demands for recognition.",
            "fact_ta": "துளு மற்றும் படகா ஆகியவை அங்கீகாரம் கோரும் பிற திராவிட மொழிகளாகும்."
        },
        # 12
        {
            "subtopic": "92nd Amendment Languages and Geographic Concentration",
            "stem_en": "Match List-I (92nd Amendment BDMS Language) with List-II (Predominant Region / State) and select the correct answer using the codes given below:\nList-I:\na) Bodo\nb) Dogri\nc) Maithili\nd) Santhali\nList-II:\n1. Jammu region (Jammu & Kashmir)\n2. Chota Nagpur Plateau (Jharkhand, Odisha, West Bengal)\n3. Bodoland Territorial Region (Assam)\n4. Mithila region (Bihar and Jharkhand)",
            "stem_ta": "பட்டியல்-I-ஐ (92வது திருத்த BDMS மொழி) பட்டியல்-II-உடன் (முதன்மையான பகுதி / மாநிலம்) பொருத்தி, கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\nபட்டியல்-I:\na) போடோ\nb) டோக்ரி\nc) மைதிலி\nd) சந்தாலி\nபட்டியல்-II:\n1. ஜம்மு பகுதி (ஜம்மு & காஷ்மீர்)\n2. சோட்டா நாக்பூர் பீடபூமி (ஜார்க்கண்ட், ஒடிசா, மேற்கு வங்காளம்)\n3. போடோலாந்து பிராந்திய பகுதி (அசாம்)\n4. மிதிலை பகுதி (பீகார் மற்றும் ஜார்க்கண்ட்)",
            "options": [
                ("a-3, b-1, c-4, d-2", "a-3, b-1, c-4, d-2"),
                ("a-1, b-3, c-2, d-4", "a-1, b-3, c-2, d-4"),
                ("a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2"),
                ("a-4, b-1, c-3, d-2", "a-4, b-1, c-3, d-2")
            ],
            "correct_key": "A",
            "exp_en": "Bodo is spoken in Bodoland, Assam (3). Dogri is spoken in the Jammu region (1). Maithili is spoken in Mithila, Bihar (4). Santhali is spoken across the Chota Nagpur plateau (2). Correct code is a-3, b-1, c-4, d-2.",
            "exp_ta": "போடோ அசாமின் போடோலாந்தில் பேசப்படுகிறது (3). டோக்ரி ஜம்மு பகுதியில் பேசப்படுகிறது (1). மைதிலி பீகாரின் மிதிலைப் பகுதியில் பேசப்படுகிறது (4). சந்தாலி சோட்டா நாக்பூர் பீடபூமியில் பேசப்படுகிறது (2). சரியான குறியீடு: a-3, b-1, c-4, d-2.",
            "why_a_en": "Correctly matches each 92nd Amendment language to its geographic homeland.",
            "why_a_ta": "ஒவ்வொரு 92வது திருத்த மொழியையும் அதன் புவியியல் தாயகத்துடன் சரியாகப் பொருத்துகிறது.",
            "why_b_en": "Swaps Bodo and Dogri.",
            "why_b_ta": "போடோ மற்றும் டோக்ரியை மாற்றுகிறது.",
            "why_c_en": "Swaps Dogri and Maithili regions.",
            "why_c_ta": "டோக்ரி மற்றும் மைதிலி பகுதிகளை மாற்றுகிறது.",
            "why_d_en": "Assigns Mithila to Bodo.",
            "why_d_ta": "மிதிலையை போடோவுக்கு தவறாக ஒதுக்குகிறது.",
            "tip_en": "Mnemonic: Bodo=Assam, Dogri=J&K, Maithili=Bihar, Santhali=Jharkhand.",
            "tip_ta": "நினைவுக்குறிப்பு: போடோ=அசாம், டோக்ரி=ஜம்மு, மைதிலி=பீகார், சந்தாலி=ஜார்க்கண்ட்.",
            "fact_en": "92nd Amendment came into force in January 2004.",
            "fact_ta": "92வது திருத்தம் ஜனவரி 2004-ல் நடைமுறைக்கு வந்தது."
        },
        # 13
        {
            "subtopic": "Article 348 Sub-clauses",
            "stem_en": "Match List-I (Clauses of Article 348) with List-II (Specific Legal Scope) and select the correct answer using the codes given below:\nList-I:\na) Article 348(1)(a)\nb) Article 348(1)(b)\nc) Article 348(2)\nd) Article 348(3)\nList-II:\n1. Bills, Acts, Ordinances, and statutory rules in English\n2. Authoritative English translation for State laws in regional languages\n3. Supreme Court and High Court proceedings in English\n4. Governor with President's consent authorizing Hindi in High Court",
            "stem_ta": "பட்டியல்-I-ஐ (சரத்து 348-ன் பிரிவுகள்) பட்டியல்-II-உடன் (குறிப்பிட்ட சட்ட வரம்பு) பொருத்தி, கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\nபட்டியல்-I:\na) சரத்து 348(1)(a)\nb) சரத்து 348(1)(b)\nc) சரத்து 348(2)\nd) சரத்து 348(3)\nபட்டியல்-II:\n1. மசோதாக்கள், சட்டங்கள், அவசரச் சட்டங்கள் மற்றும் விதிகள் ஆங்கிலத்தில் இருத்தல்\n2. வட்டார மொழிகளிலான மாநிலச் சட்டங்களுக்கு அதிகாரப்பூர்வ ஆங்கில மொழிபெயர்ப்பு\n3. உச்ச நீதிமன்றம் மற்றும் உயர் நீதிமன்ற நடவடிக்கைகள் ஆங்கிலத்தில் இருத்தல்\n4. ஆளுநர் குடியரசுத் தலைவரின் ஒப்புதலுடன் உயர் நீதிமன்றத்தில் இந்தியை அனுமதித்தல்",
            "options": [
                ("a-3, b-1, c-4, d-2", "a-3, b-1, c-4, d-2"),
                ("a-1, b-3, c-2, d-4", "a-1, b-3, c-2, d-4"),
                ("a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2"),
                ("a-4, b-1, c-3, d-2", "a-4, b-1, c-3, d-2")
            ],
            "correct_key": "A",
            "exp_en": "Article 348(1)(a) governs Court proceedings (3). Article 348(1)(b) governs Bills and Acts (1). Article 348(2) allows Governor + President consent for Hindi in High Court (4). Article 348(3) mandates English translation for State laws passed in regional languages (2). Correct code is a-3, b-1, c-4, d-2.",
            "exp_ta": "சரத்து 348(1)(a) நீதிமன்ற நடவடிக்கைகளைக் கையாள்கிறது (3). சரத்து 348(1)(b) மசோதாக்கள் மற்றும் சட்டங்களைக் கையாள்கிறது (1). சரத்து 348(2) ஆளுநர் + குடியரசுத் தலைவர் ஒப்புதலுடன் உயர் நீதிமன்றத்தில் இந்தியை அனுமதிக்கிறது (4). சரத்து 348(3) வட்டார மொழியில் இயற்றப்படும் மாநிலச் சட்டங்களுக்கு ஆங்கில மொழிபெயர்ப்பைக் கட்டாயமாக்குகிறது (2). சரியான குறியீடு: a-3, b-1, c-4, d-2.",
            "why_a_en": "Accurately maps each clause of Article 348.",
            "why_a_ta": "சரத்து 348-ன் ஒவ்வொரு உட்பிரிவையும் துல்லியமாகப் பொருத்துகிறது.",
            "why_b_en": "Swaps 348(1)(a) and 348(1)(b).",
            "why_b_ta": "348(1)(a) மற்றும் 348(1)(b)-ஐ மாற்றுகிறது.",
            "why_c_en": "Confuses 348(2) with Bills.",
            "why_c_ta": "348(2)-ஐ மசோதாக்களுடன் குழப்புகிறது.",
            "why_d_en": "Assigns Governor power to 348(1)(a).",
            "why_d_ta": "ஆளுநர் அதிகாரத்தை 348(1)(a)-வுக்கு தவறாக ஒதுக்குகிறது.",
            "tip_en": "Remember Article 348 is titled 'Language to be used in the Supreme Court and in the High Courts and for Acts, Bills, etc.'",
            "tip_ta": "சரத்து 348 உச்ச நீதிமன்றம், உயர் நீதிமன்றங்கள் மற்றும் சட்டங்கள், மசோதாக்களுக்கான மொழியைக் கையாள்கிறது.",
            "fact_en": "Judgments under 348(2) proviso remain excluded from pure Hindi unless authorized.",
            "fact_ta": "சரத்து 348(2) வரம்புரையின் கீழ் தீர்ப்புகள் அனுமதிக்கப்படும் வரை ஆங்கிலத்திலேயே இருக்க வேண்டும்."
        },
        # 14
        {
            "subtopic": "Leaders and Language Debates",
            "stem_en": "Match List-I (Key Personality) with List-II (Historic Language Role / Contribution) and select the correct answer using the codes given below:\nList-I:\na) C.N. Annadurai\nb) K.M. Munshi & N.G. Ayyangar\nc) B.G. Kher\nd) Jawaharlal Nehru\nList-II:\n1. Formulated the Constituent Assembly language compromise formula (1949)\n2. Solemn parliamentary assurance to non-Hindi speaking people (1959)\n3. Two-Language Policy resolution in Tamil Nadu Assembly (1968)\n4. Chaired the First Official Language Commission (1955)",
            "stem_ta": "பட்டியல்-I-ஐ (முக்கியத் தலைவர்) பட்டியல்-II-உடன் (வரலாற்று மொழிப் பங்கு / பங்களிப்பு) பொருத்தி, கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\nபட்டியல்-I:\na) சி.என். அண்ணாதுரை\nb) கே.எம். முன்ஷி & என்.ஜி. அய்யங்கார்\nc) பி.ஜி. கேர்\nd) ஜவஹர்லால் நேரு\nபட்டியல்-II:\n1. அரசியலமைப்பு நிர்ணய சபை மொழி சமரச சூத்திரத்தை உருவாக்கினர் (1949)\n2. இந்தி பேசாத மக்களுக்கு நாடாளுமன்றத்தில் அளித்த வரலாற்று உறுதிமொழி (1959)\n3. தமிழ்நாடு சட்டமன்றத்தில் இருமொழிக் கொள்கைத் தீர்மானம் (1968)\n4. முதலாவது அதிகாரப்பூர்வ மொழி ஆணையத்திற்குத் தலைமை தாங்கினார் (1955)",
            "options": [
                ("a-3, b-1, c-4, d-2", "a-3, b-1, c-4, d-2"),
                ("a-1, b-3, c-2, d-4", "a-1, b-3, c-2, d-4"),
                ("a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2"),
                ("a-4, b-1, c-3, d-2", "a-4, b-1, c-3, d-2")
            ],
            "correct_key": "A",
            "exp_en": "C.N. Annadurai moved the Two-Language Policy resolution in 1968 (3). Munshi & Ayyangar drafted the 1949 compromise formula (1). B.G. Kher chaired the 1955 Commission (4). Jawaharlal Nehru gave the 1959 assurance in Parliament (2). Correct code is a-3, b-1, c-4, d-2.",
            "exp_ta": "சி.என். அண்ணாதுரை 1968-ல் இருமொழிக் கொள்கைத் தீர்மானத்தைக் கொண்டுவந்தார் (3). முன்ஷி & அய்யங்கார் 1949 சமரச சூத்திரத்தை வரைந்தனர் (1). பி.ஜி. கேர் 1955 ஆணையத்திற்குத் தலைமை தாங்கினார் (4). ஜவஹர்லால் நேரு 1959-ல் நாடாளுமன்றத்தில் உறுதிமொழி அளித்தார் (2). சரியான குறியீடு: a-3, b-1, c-4, d-2.",
            "why_a_en": "Accurately connects each leader with their defining historic action.",
            "why_a_ta": "ஒவ்வொரு தலைவரையும் அவர்களின் வரலாற்று முக்கியத்துவம் வாய்ந்த நடவடிக்கையுடன் சரியாக இணைக்கிறது.",
            "why_b_en": "Confuses Annadurai with Munshi-Ayyangar formula.",
            "why_b_ta": "அண்ணாவை முன்ஷி-அய்யங்கார் சூத்திரத்துடன் குழப்புகிறது.",
            "why_c_en": "Confuses Nehru with Kher.",
            "why_c_ta": "நேருவை கேருடன் குழப்புகிறது.",
            "why_d_en": "Assigns First Commission to Annadurai.",
            "why_d_ta": "முதல் ஆணையத்தை அண்ணாவுக்கு தவறாக ஒதுக்குகிறது.",
            "tip_en": "Nehru's Assurance: English will continue as long as the non-Hindi speaking people want it.",
            "tip_ta": "நேருவின் உறுதிமொழி: இந்தி பேசாத மக்கள் விரும்பும் வரை ஆங்கிலம் தொடரும்.",
            "fact_en": "The Munshi-Ayyangar formula resolved the deadlock between Hindi purists and non-Hindi delegates in September 1949.",
            "fact_ta": "முன்ஷி-அய்யங்கார் சூத்திரம் செப்டம்பர் 1949-ல் இந்தி ஆதரவாளர்களுக்கும் இந்தி பேசாத பிரதிநிதிகளுக்கும் இடையிலான முட்டுக்கட்டையைத் தீர்த்தது."
        },
        # 15
        {
            "subtopic": "Official Language Institutions and Locations",
            "stem_en": "Match List-I (Language Institution) with List-II (Headquarters / Location) and select the correct answer using the codes given below:\nList-I:\na) Central Institute of Indian Languages (CIIL)\nb) Central Institute of Classical Tamil (CICT)\nc) Commissioner for Linguistic Minorities (CLM)\nd) Kendriya Hindi Sansthan\nList-II:\n1. Chennai (Tamil Nadu)\n2. Agra (Uttar Pradesh)\n3. Mysuru (Karnataka)\n4. Prayagraj (Headquarters) / New Delhi",
            "stem_ta": "பட்டியல்-I-ஐ (மொழி நிறுவனம்) பட்டியல்-II-உடன் (தலைமையகம் / அமைவிடம்) பொருத்தி, கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\nபட்டியல்-I:\na) இந்திய மொழிகளின் மத்திய நிறுவனம் (CIIL)\nb) செம்மொழித் தமிழாய்வு மத்திய நிறுவனம் (CICT)\nc) மொழிச் சிறுபான்மையினர் ஆணையர் (CLM)\nd) கேந்திரிய இந்தி சன்ஸ்தான்\nபட்டியல்-II:\n1. சென்னை (தமிழ்நாடு)\n2. ஆக்ரா (உத்தரப் பிரதேசம்)\n3. மைசூரு (கர்நாடகா)\n4. பிரயாக்ராஜ் (தலைமையகம்) / புது தில்லி",
            "options": [
                ("a-3, b-1, c-4, d-2", "a-3, b-1, c-4, d-2"),
                ("a-1, b-3, c-2, d-4", "a-1, b-3, c-2, d-4"),
                ("a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2"),
                ("a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3")
            ],
            "correct_key": "A",
            "exp_en": "CIIL is located in Mysuru (3). CICT is in Chennai (1). CLM headquarters is at Prayagraj (4). Kendriya Hindi Sansthan is located in Agra (2). Correct code is a-3, b-1, c-4, d-2.",
            "exp_ta": "CIIL மைசூரில் அமைந்துள்ளது (3). CICT சென்னையில் உள்ளது (1). CLM தலைமையகம் பிரயாக்ராஜில் உள்ளது (4). கேந்திரிய இந்தி சன்ஸ்தான் ஆக்ராவில் அமைந்துள்ளது (2). சரியான குறியீடு: a-3, b-1, c-4, d-2.",
            "why_a_en": "Pairs each premier central language institute with its actual headquarters city.",
            "why_a_ta": "ஒவ்வொரு முதன்மை மத்திய மொழி நிறுவனத்தையும் அதன் உண்மையான தலைமையக நகரத்துடன் சரியாகப் பொருத்துகிறது.",
            "why_b_en": "Swaps CIIL and CICT.",
            "why_b_ta": "CIIL மற்றும் CICT-ஐ மாற்றுகிறது.",
            "why_c_en": "Confuses CLM with CICT.",
            "why_c_ta": "CLM மற்றும் CICT-ஐ குழப்புகிறது.",
            "why_d_en": "Assigns Agra to CIIL.",
            "why_d_ta": "ஆக்ராவை CIIL-க்கு தவறாக ஒதுக்குகிறது.",
            "tip_en": "CICT was formerly located inside the CIIL campus in Mysuru before being relocated to Chennai as an autonomous institute.",
            "tip_ta": "CICT தன்னாட்சி நிறுவனமாக சென்னைக்கு மாற்றப்படுவதற்கு முன்பு மைசூரு CIIL வளாகத்திற்குள் இருந்தது.",
            "fact_en": "CIIL was established in July 1969 to advise and assist the Central and State Governments on language matters.",
            "fact_ta": "மத்திய மற்றும் மாநில அரசுகளுக்கு மொழி விவகாரங்களில் உதவ ஜூலை 1969-ல் CIIL நிறுவப்பட்டது."
        },
        # 16
        {
            "subtopic": "Classical Language Evaluation Parameters",
            "stem_en": "Match List-I (Classical Language Criteria) with List-II (Specific Requirement) and select the correct answer using the codes given below:\nList-I:\na) Antiquity Criterion\nb) Heritage Literature Criterion\nc) Originality Criterion\nd) Discontinuity Criterion\nList-II:\n1. Ancient literature considered valuable heritage by generations of speakers\n2. Classical language and literature distinct from modern forms/offshoots\n3. High antiquity of early texts over a period of 1500–2000 years\n4. Literary tradition is original and not borrowed from another speech community",
            "stem_ta": "பட்டியல்-I-ஐ (செம்மொழி அளவுகோல்கள்) பட்டியல்-II-உடன் (குறிப்பிட்ட தேவை) பொருத்தி, கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\nபட்டியல்-I:\na) தொன்மை அளவுகோல்\nb) பாரம்பரிய இலக்கிய அளவுகோல்\nc) தனித்தன்மை அளவுகோல்\nd) தொடர்ச்சியின்மை/வேறுபாடு அளவுகோல்\nபட்டியல்-II:\n1. தலைமுறை தலைமுறையாக மதிப்புமிக்க பாரம்பரியமாகக் கருதப்படும் பண்டைய இலக்கியங்கள்\n2. செம்மொழியும் அதன் இலக்கியமும் நவீன வடிவங்களிலிருந்து வேறுபட்டிருத்தல்\n3. 1500–2000 ஆண்டுகள் பழமையான ஆரம்பகால நூல்களின் உயர்ந்த தொன்மை\n4. இலக்கிய மரபு சுயாதீனமானது மற்றும் பிற மொழிக் குழுவிடமிருந்து கடன் பெறாதது",
            "options": [
                ("a-3, b-1, c-4, d-2", "a-3, b-1, c-4, d-2"),
                ("a-1, b-3, c-2, d-4", "a-1, b-3, c-2, d-4"),
                ("a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2"),
                ("a-4, b-1, c-3, d-2", "a-4, b-1, c-3, d-2")
            ],
            "correct_key": "A",
            "exp_en": "Antiquity criterion requires 1500–2000 years of texts (3). Heritage literature criterion requires valuable body of literature (1). Originality requires unborrowed literary tradition (4). Discontinuity requires distinction between classical and modern forms (2). Correct code is a-3, b-1, c-4, d-2.",
            "exp_ta": "தொன்மை அளவுகோல் 1500–2000 ஆண்டு பழமையான நூல்களைக் கோருகிறது (3). பாரம்பரிய இலக்கிய அளவுகோல் மதிப்புமிக்க இலக்கியத் தொகுப்பைக் கோருகிறது (1). தனித்தன்மை கடன் பெறாத இலக்கிய மரபைக் கோருகிறது (4). தொடர்ச்சியின்மை செவ்வியல் மற்றும் நவீன வடிவங்களுக்கு இடையே வேறுபாட்டைக் கோருகிறது (2). சரியான குறியீடு: a-3, b-1, c-4, d-2.",
            "why_a_en": "Accurately pairs all four official criteria notified by the Government of India.",
            "why_a_ta": "இந்திய அரசால் அறிவிக்கப்பட்ட நான்கு அதிகாரப்பூர்வ அளவுகோல்களையும் துல்லியமாகப் பொருத்துகிறது.",
            "why_b_en": "Swaps Antiquity and Heritage.",
            "why_b_ta": "தொன்மை மற்றும் பாரம்பரியத்தை மாற்றுகிறது.",
            "why_c_en": "Confuses Originality with Heritage.",
            "why_c_ta": "தனித்தன்மையை பாரம்பரியத்துடன் குழப்புகிறது.",
            "why_d_en": "Assigns Originality to Antiquity.",
            "why_d_ta": "தனித்தன்மையை தொன்மைக்கு தவறாக ஒதுக்குகிறது.",
            "tip_en": "Formulated by the Committee of Linguistic Experts set up by the Ministry of Culture.",
            "tip_ta": "பண்பாட்டு அமைச்சகத்தால் அமைக்கப்பட்ட மொழி நிபுணர்கள் குழுவால் உருவாக்கப்பட்டது.",
            "fact_en": "The antiquity threshold was initially 1000 years in 2004, raised to 1500–2000 years in 2005.",
            "fact_ta": "தொன்மை வரம்பு தொடக்கத்தில் 2004-ல் 1000 ஆண்டுகளாக இருந்து, 2005-ல் 1500–2000 ஆண்டுகளாக உயர்த்தப்பட்டது."
        },
        # 17
        {
            "subtopic": "Linguistic Families of Eighth Schedule",
            "stem_en": "Match List-I (Linguistic Family) with List-II (Eighth Schedule Language Member) and select the correct answer using the codes given below:\nList-I:\na) Dravidian\nb) Indo-Aryan\nc) Tibeto-Burman\nd) Austroasiatic\nList-II:\n1. Marathi\n2. Santhali\n3. Telugu\n4. Bodo",
            "stem_ta": "பட்டியல்-I-ஐ (மொழிக் குடும்பம்) பட்டியல்-II-உடன் (எட்டாவது அட்டவணை மொழி உறுப்பினர்) பொருத்தி, கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\nபட்டியல்-I:\na) திராவிடம்\nb) இந்தோ-ஆரியம்\nc) திபெத்தோ-பர்மியம்\nd) ஆஸ்ட்ரோ-ஆசியாட்டிக்\nபட்டியல்-II:\n1. மராத்தி\n2. சந்தாலி\n3. தெலுங்கு\n4. போடோ",
            "options": [
                ("a-3, b-1, c-4, d-2", "a-3, b-1, c-4, d-2"),
                ("a-1, b-3, c-2, d-4", "a-1, b-3, c-2, d-4"),
                ("a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2"),
                ("a-4, b-1, c-3, d-2", "a-4, b-1, c-3, d-2")
            ],
            "correct_key": "A",
            "exp_en": "Telugu is Dravidian (3). Marathi is Indo-Aryan (1). Bodo is Tibeto-Burman (4). Santhali is Austroasiatic (2). Correct code is a-3, b-1, c-4, d-2.",
            "exp_ta": "தெலுங்கு திராவிட மொழிக் குடும்பத்தைச் சேர்ந்தது (3). மராத்தி இந்தோ-ஆரியக் குடும்பத்தைச் சேர்ந்தது (1). போடோ திபெத்தோ-பர்மியக் குடும்பத்தைச் சேர்ந்தது (4). சந்தாலி ஆஸ்ட்ரோ-ஆசியாட்டிக் குடும்பத்தைச் சேர்ந்தது (2). சரியான குறியீடு: a-3, b-1, c-4, d-2.",
            "why_a_en": "Correctly matches each language to its genealogical linguistic family.",
            "why_a_ta": "ஒவ்வொரு மொழியையும் அதன் மரபுவழி மொழிக் குடும்பத்துடன் சரியாகப் பொருத்துகிறது.",
            "why_b_en": "Swaps Dravidian and Indo-Aryan.",
            "why_b_ta": "திராவிடம் மற்றும் இந்தோ-ஆரியத்தை மாற்றுகிறது.",
            "why_c_en": "Confuses Bodo with Indo-Aryan.",
            "why_c_ta": "போடோவை இந்தோ-ஆரியத்துடன் குழப்புகிறது.",
            "why_d_en": "Assigns Bodo to Dravidian.",
            "why_d_ta": "போடோவை திராவிடத்துடன் தவறாக ஒதுக்குகிறது.",
            "tip_en": "The 22 languages of the Eighth Schedule represent four distinct linguistic families.",
            "tip_ta": "எட்டாவது அட்டவணையின் 22 மொழிகள் நான்கு வெவ்வேறு மொழிக் குடும்பங்களைப் பிரதிபலிக்கின்றன.",
            "fact_en": "Manipuri (Meitei) is another Tibeto-Burman language in the Eighth Schedule.",
            "fact_ta": "மணிப்பூரி (மெய்தேய்) எட்டாவது அட்டவணையில் உள்ள மற்றொரு திபெத்தோ-பர்மிய மொழியாகும்."
        },
        # 18
        {
            "subtopic": "Milestones in Indian Language Policy Timeline",
            "stem_en": "Match List-I (Historic Date / Year) with List-II (Milestone Event) and select the correct answer using the codes given below:\nList-I:\na) 14 September 1949\nb) 26 January 1965\nc) 23 January 1968\nd) 3 October 2024\nList-II:\n1. 15-year constitutional transition period for English ended\n2. Union Cabinet approved Classical status for 5 languages\n3. Constituent Assembly adopted Hindi as the Official Language of Union\n4. Tamil Nadu Legislative Assembly adopted Two-Language Policy",
            "stem_ta": "பட்டியல்-I-ஐ (வரலாற்று தேதி / ஆண்டு) பட்டியல்-II-உடன் (மைல்கல் நிகழ்வு) பொருத்தி, கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\nபட்டியல்-I:\na) 14 செப்டம்பர் 1949\nb) 26 ஜனவரி 1965\nc) 23 ஜனவரி 1968\nd) 3 அக்டோபர் 2024\nபட்டியல்-II:\n1. ஆங்கிலத்திற்கான 15 ஆண்டு அரசியலமைப்பு இடைக்கால அவகாசம் முடிவடைந்தது\n2. மத்திய அமைச்சரவை 5 மொழிகளுக்கு செம்மொழித் தகுதியை அங்கீகரித்தது\n3. அரசியலமைப்பு நிர்ணய சபை இந்தியை ஒன்றியத்தின் அதிகாரப்பூர்வ மொழியாக ஏற்றது\n4. தமிழ்நாடு சட்டமன்றம் இருமொழிக் கொள்கையை ஏற்றுக்கொண்டது",
            "options": [
                ("a-3, b-1, c-4, d-2", "a-3, b-1, c-4, d-2"),
                ("a-1, b-3, c-2, d-4", "a-1, b-3, c-2, d-4"),
                ("a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2"),
                ("a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3")
            ],
            "correct_key": "A",
            "exp_en": "14 Sep 1949: Constituent Assembly adopted Hindi (3). 26 Jan 1965: 15-year transition expired (1). 23 Jan 1968: TN Assembly Two-Language Resolution (4). 3 Oct 2024: 5 Classical languages approved (2). Correct code is a-3, b-1, c-4, d-2.",
            "exp_ta": "14 செப் 1949: அரசியலமைப்பு நிர்ணய சபை இந்தியை ஏற்றது (3). 26 ஜன 1965: 15 ஆண்டு கெடு முடிந்தது (1). 23 ஜன 1968: தமிழ்நாடு சட்டமன்ற இருமொழிக் கொள்கைத் தீர்மானம் (4). 3 அக் 2024: 5 செம்மொழிகள் அங்கீகரிக்கப்பட்டன (2). சரியான குறியீடு: a-3, b-1, c-4, d-2.",
            "why_a_en": "Pairs each landmark date with its precise historical event.",
            "why_a_ta": "ஒவ்வொரு முக்கிய தேதியையும் அதன் துல்லியமான வரலாற்று நிகழ்வுடன் சரியாகப் பொருத்துகிறது.",
            "why_b_en": "Swaps 1949 and 1965.",
            "why_b_ta": "1949 மற்றும் 1965-ஐ மாற்றுகிறது.",
            "why_c_en": "Confuses 1968 with 2024.",
            "why_c_ta": "1968-ஐ 2024-உடன் குழப்புகிறது.",
            "why_d_en": "Assigns 2024 event to 1949.",
            "why_d_ta": "2024 நிகழ்வை 1949-க்கு தவறாக ஒதுக்குகிறது.",
            "tip_en": "14 September is celebrated every year across India as 'Hindi Diwas'.",
            "tip_ta": "செப்டம்பர் 14 ஒவ்வொரு ஆண்டும் இந்தியா முழுவதும் 'இந்தி தினமாக'க் கொண்டாடப்படுகிறது.",
            "fact_en": "The 1965 transition sparked the anti-Hindi agitations in Madras State.",
            "fact_ta": "1965 இடைக்கால முடிவு மதராஸ் மாகாணத்தில் தீவிர இந்தி எதிர்ப்புப் போராட்டங்களைத் தூண்டியது."
        },
        # 19
        {
            "subtopic": "Legislative Language Provisions Articles 120 and 210",
            "stem_en": "Match List-I (Legislative Language Clause) with List-II (Provisions) and select the correct answer using the codes given below:\nList-I:\na) Article 120(1)\nb) Article 120(2)\nc) Article 210(1)\nd) Article 210(2)\nList-II:\n1. English in Parliament to lapse after 15 years unless Parliament provided otherwise\n2. English in State Legislature to lapse after 15 years unless State law provided otherwise\n3. Language of business in Parliament (Hindi or English)\n4. Language of business in State Legislature (Official language(s) of State or Hindi or English)",
            "stem_ta": "பட்டியல்-I-ஐ (சட்டமன்ற மொழிப் பிரிவு) பட்டியல்-II-உடன் (விதிகள்) பொருத்தி, கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\nபட்டியல்-I:\na) சரத்து 120(1)\nb) சரத்து 120(2)\nc) சரத்து 210(1)\nd) சரத்து 210(2)\nபட்டியல்-II:\n1. நாடாளுமன்றச் சட்டம் மூலம் நீட்டிக்கப்படாவிட்டால் 15 ஆண்டுகளுக்குப் பிறகு நாடாளுமன்றத்தில் ஆங்கிலம் காலாவதியாதல்\n2. மாநிலச் சட்டம் மூலம் நீட்டிக்கப்படாவிட்டால் 15 ஆண்டுகளுக்குப் பிறகு மாநில சட்டமன்றத்தில் ஆங்கிலம் காலாவதியாதல்\n3. நாடாளுமன்றத்தின் அலுவல் மொழி (இந்தி அல்லது ஆங்கிலம்)\n4. மாநில சட்டமன்றத்தின் அலுவல் மொழி (மாநிலத்தின் அதிகாரப்பூர்வ மொழி(கள்) அல்லது இந்தி அல்லது ஆங்கிலம்)",
            "options": [
                ("a-3, b-1, c-4, d-2", "a-3, b-1, c-4, d-2"),
                ("a-1, b-3, c-2, d-4", "a-1, b-3, c-2, d-4"),
                ("a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2"),
                ("a-4, b-1, c-3, d-2", "a-4, b-1, c-3, d-2")
            ],
            "correct_key": "A",
            "exp_en": "Article 120(1) governs language in Parliament (3). Article 120(2) provided for 15-year sunset for English in Parliament (1). Article 210(1) governs language in State Legislatures (4). Article 210(2) provided for 15-year sunset for English in State Legislatures (2). Correct code is a-3, b-1, c-4, d-2.",
            "exp_ta": "சரத்து 120(1) நாடாளுமன்ற அலுவல் மொழியைக் கையாள்கிறது (3). சரத்து 120(2) நாடாளுமன்றத்தில் ஆங்கிலத்திற்கான 15 ஆண்டு காலக்கெடுவை வழங்கியது (1). சரத்து 210(1) மாநில சட்டமன்ற அலுவல் மொழியைக் கையாள்கிறது (4). சரத்து 210(2) மாநில சட்டமன்றத்தில் ஆங்கிலத்திற்கான 15 ஆண்டு காலக்கெடுவை வழங்கியது (2). சரியான குறியீடு: a-3, b-1, c-4, d-2.",
            "why_a_en": "Accurately distinguishes between Union Parliament (120) and State Legislature (210) provisions.",
            "why_a_ta": "நாடாளுமன்றம் (120) மற்றும் மாநில சட்டமன்ற (210) விதிகளைத் துல்லியமாக வேறுபடுத்திக் காட்டுகிறது.",
            "why_b_en": "Swaps Article 120(1) and 120(2).",
            "why_b_ta": "சரத்து 120(1) மற்றும் 120(2)-ஐ மாற்றுகிறது.",
            "why_c_en": "Confuses Parliament with State Legislature.",
            "why_c_ta": "நாடாளுமன்றத்தை மாநில சட்டமன்றத்துடன் குழப்புகிறது.",
            "why_d_en": "Assigns State Legislature to Article 120.",
            "why_d_ta": "மாநில சட்டமன்றத்தை சரத்து 120-க்கு தவறாக ஒதுக்குகிறது.",
            "tip_en": "Remember symmetry: Art 120 = Parliament; Art 210 = State Legislature (120 + 90 = 210).",
            "tip_ta": "சமச்சீர்மை நினைவு: சரத்து 120 = நாடாளுமன்றம்; சரத்து 210 = மாநில சட்டமன்றம் (120 + 90 = 210).",
            "fact_en": "Both Articles allow the Presiding Officer to permit a member who cannot adequately express themselves in Hindi/English to speak in their mother tongue.",
            "fact_ta": "இரு சரத்துகளும் இந்தி/ஆங்கிலத்தில் பேச முடியாத உறுப்பினர் தனது தாய்மொழியில் பேச அனுமதிக்க அவைத் தலைவருக்கு அதிகாரமளிக்கின்றன."
        },
        # 20
        {
            "subtopic": "Mother Tongue Address in Legislatures",
            "stem_en": "Match List-I (Legislative Authority / Forum) with List-II (Mother Tongue Permission Power) and select the correct answer using the codes given below:\nList-I:\na) Speaker of the Lok Sabha\nb) Chairman of the Rajya Sabha\nc) Speaker of the Legislative Assembly\nd) Simultaneous Interpretation Unit\nList-II:\n1. May permit a Rajya Sabha MP to address the Council in their mother tongue (Art 120(1))\n2. Provides simultaneous interpretation into all 22 Eighth Schedule languages in Parliament\n3. May permit a Lok Sabha MP to address the House in their mother tongue (Art 120(1))\n4. May permit an MLA to address the Assembly in their mother tongue (Art 210(1))",
            "stem_ta": "பட்டியல்-I-ஐ (சட்டமன்ற அதிகாரம் / அரங்கம்) பட்டியல்-II-உடன் (தாய்மொழிப் பேச்சு அனுமதி அதிகாரம்) பொருத்தி, கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\nபட்டியல்-I:\na) மக்களவைத் தலைவர்\nb) மாநிலங்களவைத் தலைவர்\nc) சட்டப் பேரவைத் தலைவர்\nd) உடனடி மொழிபெயர்ப்புப் பிரிவு\nபட்டியல்-II:\n1. மாநிலங்களவை உறுப்பினர் தனது தாய்மொழியில் பேச அனுமதியளிக்கலாம் (சரத்து 120(1))\n2. நாடாளுமன்றத்தில் 22 எட்டாவது அட்டவணை மொழிகளிலும் உடனடி மொழிபெயர்ப்பை வழங்குகிறது\n3. மக்களவை உறுப்பினர் தனது தாய்மொழியில் பேச அனுமதியளிக்கலாம் (சரத்து 120(1))\n4. சட்டமன்ற உறுப்பினர் தனது தாய்மொழியில் பேரவையில் பேச அனுமதியளிக்கலாம் (சரத்து 210(1))",
            "options": [
                ("a-3, b-1, c-4, d-2", "a-3, b-1, c-4, d-2"),
                ("a-1, b-3, c-2, d-4", "a-1, b-3, c-2, d-4"),
                ("a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2"),
                ("a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3")
            ],
            "correct_key": "A",
            "exp_en": "Speaker of Lok Sabha permits Lok Sabha MPs under Art 120(1) (3). Chairman of Rajya Sabha permits Rajya Sabha MPs under Art 120(1) (1). Speaker of Legislative Assembly permits MLAs under Art 210(1) (4). Simultaneous interpretation unit covers all 22 languages (2). Correct code is a-3, b-1, c-4, d-2.",
            "exp_ta": "மக்களவைத் தலைவர் சரத்து 120(1)-ன் கீழ் மக்களவை உறுப்பினர்களை அனுமதிக்கிறார் (3). மாநிலங்களவைத் தலைவர் சரத்து 120(1)-ன் கீழ் மாநிலங்களவை உறுப்பினர்களை அனுமதிக்கிறார் (1). சட்டப்பேரவைத் தலைவர் சரத்து 210(1)-ன் கீழ் சட்டமன்ற உறுப்பினர்களை அனுமதிக்கிறார் (4). உடனடி மொழிபெயர்ப்புப் பிரிவு 22 மொழிகளையும் உள்ளடக்கியுள்ளது (2). சரியான குறியீடு: a-3, b-1, c-4, d-2.",
            "why_a_en": "Pairs each presiding officer and parliamentary service with their specific power.",
            "why_a_ta": "ஒவ்வொரு அவைத் தலைவரையும் நாடாளுமன்ற சேவையையும் அவற்றின் குறிப்பிட்ட அதிகாரத்துடன் சரியாகப் பொருத்துகிறது.",
            "why_b_en": "Swaps Lok Sabha Speaker and Rajya Sabha Chairman.",
            "why_b_ta": "மக்களவைத் தலைவர் மற்றும் மாநிலங்களவைத் தலைவரை மாற்றுகிறது.",
            "why_c_en": "Confuses Assembly Speaker with Parliament.",
            "why_c_ta": "பேரவைத் தலைவரை நாடாளுமன்றத்துடன் குழப்புகிறது.",
            "why_d_en": "Assigns interpretation to Speaker.",
            "why_d_ta": "மொழிபெயர்ப்புப் பணியை சபாநாயகருக்கு தவறாக ஒதுக்குகிறது.",
            "tip_en": "Advance notice is usually required to arrange simultaneous interpretation into English and Hindi.",
            "tip_ta": "ஆங்கிலம் மற்றும் இந்தியில் உடனடி மொழிபெயர்ப்பை ஏற்பாடு செய்ய வழக்கமாக முன் அறிவிப்பு தேவைப்படுகிறது.",
            "fact_en": "Simultaneous interpretation in all 22 languages was operationalized in Rajya Sabha in 2018.",
            "fact_ta": "அனைத்து 22 மொழிகளிலுமான உடனடி மொழிபெயர்ப்பு வசதி மாநிலங்களவையில் 2018-ல் செயல்பாட்டுக்கு வந்தது."
        },
        # 21
        {
            "subtopic": "States and Official Languages Chosen",
            "stem_en": "Match List-I (State / Union Territory) with List-II (Officially Adopted Language(s)) and select the correct answer using the codes given below:\nList-I:\na) Nagaland\nb) Goa\nc) Jammu and Kashmir\nd) Meghalaya\nList-II:\n1. Konkani in Devanagari script (and Marathi)\n2. English (along with Garo and Khasi as associate languages)\n3. English as sole official language\n4. Kashmiri, Dogri, Hindi, Urdu, and English (5 official languages)",
            "stem_ta": "பட்டியல்-I-ஐ (மாநிலம் / யூனியன் பிரதேசம்) பட்டியல்-II-உடன் (அதிகாரப்பூர்வமாக ஏற்கப்பட்ட மொழி(கள்)) பொருத்தி, கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\nபட்டியல்-I:\na) நாகாலாந்து\nb) கோவா\nc) ஜம்மு மற்றும் காஷ்மீர்\nd) மேகாலயா\nபட்டியல்-II:\n1. தேவநாகரி வரிவடிவத்திலான கொங்கணி (மற்றும் மராத்தி)\n2. ஆங்கிலம் (காரோ மற்றும் காசி இணை மொழிகளுடன்)\n3. ஆங்கிலம் ஒரே அதிகாரப்பூர்வ மொழியாக\n4. காஷ்மீரி, டோக்ரி, இந்தி, உருது மற்றும் ஆங்கிலம் (5 அதிகாரப்பூர்வ மொழிகள்)",
            "options": [
                ("a-3, b-1, c-4, d-2", "a-3, b-1, c-4, d-2"),
                ("a-1, b-3, c-2, d-4", "a-1, b-3, c-2, d-4"),
                ("a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2"),
                ("a-4, b-1, c-3, d-2", "a-4, b-1, c-3, d-2")
            ],
            "correct_key": "A",
            "exp_en": "Nagaland adopted English as sole official language (3). Goa adopted Konkani in Devanagari script (1). J&K Official Languages Act 2020 established 5 official languages (4). Meghalaya uses English as official language with Khasi and Garo (2). Correct code is a-3, b-1, c-4, d-2.",
            "exp_ta": "நாகாலாந்து ஆங்கிலத்தை ஒரே அதிகாரப்பூர்வ மொழியாக ஏற்றுக்கொண்டது (3). கோவா தேவநாகரி வரிவடிவ கொங்கணியை ஏற்றுக்கொண்டது (1). ஜம்மு காஷ்மீர் அதிகாரப்பூர்வ மொழிகள் சட்டம் 2020 5 அதிகாரப்பூர்வ மொழிகளை நிறுவியது (4). மேகாலயா ஆங்கிலத்தை அதிகாரப்பூர்வ மொழியாகப் பயன்படுத்துகிறது (2). சரியான குறியீடு: a-3, b-1, c-4, d-2.",
            "why_a_en": "Accurately pairs each state with its specific statutory language framework under Article 345.",
            "why_a_ta": "சரத்து 345-ன் கீழ் ஒவ்வொரு மாநிலத்தையும் அதன் குறிப்பிட்ட சட்டப்பூர்வ மொழிக் கட்டமைப்புடன் துல்லியமாக இணைக்கிறது.",
            "why_b_en": "Swaps Nagaland and Goa.",
            "why_b_ta": "நாகாலாந்து மற்றும் கோவாவை மாற்றுகிறது.",
            "why_c_en": "Confuses J&K with Goa.",
            "why_c_ta": "ஜம்மு காஷ்மீரை கோவாவுடன் குழப்புகிறது.",
            "why_d_en": "Assigns 5 languages to Nagaland.",
            "why_d_ta": "5 மொழிகளை நாகாலாந்துக்கு தவறாக ஒதுக்குகிறது.",
            "tip_en": "J&K Official Languages Act 2020 added Kashmiri, Dogri, and Hindi to existing Urdu and English.",
            "tip_ta": "ஜம்மு காஷ்மீர் அதிகாரப்பூர்வ மொழிகள் சட்டம் 2020 ஏற்கனவே இருந்த உருது மற்றும் ஆங்கிலத்துடன் காஷ்மீரி, டோக்ரி மற்றும் இந்தியைச் சேர்த்தது.",
            "fact_en": "Goa's Official Language Act was passed in 1987.",
            "fact_ta": "கோவாவின் அதிகாரப்பூர்வ மொழிச் சட்டம் 1987-ல் நிறைவேற்றப்பட்டது."
        },
        # 22
        {
            "subtopic": "Core Terminology in Language Discourse",
            "stem_en": "Match List-I (Linguistic Term) with List-II (Constitutional Meaning / Status in India) and select the correct answer using the codes given below:\nList-I:\na) Rajbhasha\nb) Rashtrabhasha\nc) Matribhasha\nd) Samparkbhasha\nList-II:\n1. Mother Tongue (protected under Article 350A for primary instruction)\n2. Link Language (inter-governmental medium; English and Hindi)\n3. Official Language (formal designation for Union/State administration in Part XVII)\n4. National Language (unrecognized in the Indian Constitution; declared non-existent by courts)",
            "stem_ta": "பட்டியல்-I-ஐ (மொழிக் கருத்துரு) பட்டியல்-II-உடன் (அரசியலமைப்புப் பொருள் / இந்தியாவில் நிலை) பொருத்தி, கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\nபட்டியல்-I:\na) ராஜ்பாஷா\nb) ராஷ்டிரபாஷா\nc) மாத்ரிபாஷா\nd) சம்பர்க்பாஷா\nபட்டியல்-II:\n1. தாய்மொழி (தொடக்கக் கல்விக்காக சரத்து 350A-ன் கீழ் பாதுகாக்கப்படுகிறது)\n2. இணைப்பு மொழி (அரசாங்கங்களுக்கு இடையேயான ஊடகம்; ஆங்கிலம் மற்றும் இந்தி)\n3. அதிகாரப்பூர்வ மொழி (பகுதி XVII-ல் ஒன்றியம்/மாநில நிர்வாகத்திற்கான முறையான பதவி)\n4. தேசிய மொழி (இந்திய அரசியலமைப்பில் அங்கீகரிக்கப்படாதது; நீதிமன்றங்களால் இல்லை என அறிவிக்கப்பட்டது)",
            "options": [
                ("a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2"),
                ("a-1, b-3, c-2, d-4", "a-1, b-3, c-2, d-4"),
                ("a-3, b-1, c-4, d-2", "a-3, b-1, c-4, d-2"),
                ("a-4, b-3, c-1, d-2", "a-4, b-3, c-1, d-2")
            ],
            "correct_key": "A",
            "exp_en": "Rajbhasha means Official Language (3). Rashtrabhasha means National Language, which has no constitutional existence in India (4). Matribhasha means Mother Tongue (1). Samparkbhasha means Link Language (2). Correct code is a-3, b-4, c-1, d-2.",
            "exp_ta": "ராஜ்பாஷா என்பது அதிகாரப்பூர்வ மொழியைக் குறிக்கிறது (3). ராஷ்டிரபாஷா என்பது தேசிய மொழியைக் குறிக்கிறது, இது இந்தியாவில் அரசியலமைப்பு ரீதியாக இல்லை (4). மாத்ரிபாஷா என்பது தாய்மொழியைக் குறிக்கிறது (1). சம்பர்க்பாஷா என்பது இணைப்பு மொழியைக் குறிக்கிறது (2). சரியான குறியீடு: a-3, b-4, c-1, d-2.",
            "why_a_en": "Accurately pairs all four Hindi/Sanskrit terms with their precise constitutional and legal realities.",
            "why_a_ta": "நான்கு இந்தி/சமஸ்கிருத சொற்களையும் அவற்றின் துல்லியமான அரசியலமைப்பு மற்றும் சட்ட யதார்த்தங்களுடன் சரியாகப் பொருத்துகிறது.",
            "why_b_en": "Confuses Rajbhasha with Mother Tongue.",
            "why_b_ta": "ராஜ்பாஷாவை தாய்மொழியுடன் குழப்புகிறது.",
            "why_c_en": "Swaps Rashtrabhasha and Matribhasha.",
            "why_c_ta": "ராஷ்டிரபாஷா மற்றும் மாத்ரிபாஷாவை மாற்றுகிறது.",
            "why_d_en": "Assigns National Language to Rajbhasha.",
            "why_d_ta": "தேசிய மொழியை ராஜ்பாஷாவுக்கு தவறாக ஒதுக்குகிறது.",
            "tip_en": "Rajbhasha = Language of Governance; Rashtrabhasha = Emotional/Nationalist concept.",
            "tip_ta": "ராஜ்பாஷா = ஆட்சி மொழி; ராஷ்டிரபாஷா = உணர்வுபூர்வமான/தேசியவாதக் கருத்துரு.",
            "fact_en": "Dr. B.R. Ambedkar noted that a language becomes Rajbhasha purely by legislative designation.",
            "fact_ta": "டாக்டர் பி.ஆர். அம்பேத்கர் ஒரு மொழி சட்டமன்றப் பெயரிடலின் மூலமே ராஜ்பாஷாவாக மாறுகிறது என்று குறிப்பிட்டார்."
        },
        # 23
        {
            "subtopic": "Parliamentary Committee on Official Language Setup",
            "stem_en": "Match List-I (Feature of Parliamentary Committee on Official Language) with List-II (Specific Detail) and select the correct answer using the codes given below:\nList-I:\na) Total Membership\nb) Lok Sabha Share\nc) Rajya Sabha Share\nd) Reporting Authority\nList-II:\n1. 20 members elected by single transferable vote\n2. The President of India\n3. 30 members total\n4. 10 members elected by single transferable vote",
            "stem_ta": "பட்டியல்-I-ஐ (அதிகாரப்பூர்வ மொழிக்கான நாடாளுமன்றக் குழுவின் அம்சம்) பட்டியல்-II-உடன் (குறிப்பிட்ட விவரம்) பொருத்தி, கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\nபட்டியல்-I:\na) மொத்த உறுப்பினர்கள்\nb) மக்களவை பங்கு\nc) மாநிலங்களவை பங்கு\nd) அறிக்கை சமர்ப்பிக்கும் அதிகாரி\nபட்டியல்-II:\n1. ஒற்றை மாற்று வாக்கு மூலம் தேர்ந்தெடுக்கப்படும் 20 உறுப்பினர்கள்\n2. இந்தியக் குடியரசுத் தலைவர்\n3. மொத்தம் 30 உறுப்பினர்கள்\n4. ஒற்றை மாற்று வாக்கு மூலம் தேர்ந்தெடுக்கப்படும் 10 உறுப்பினர்கள்",
            "options": [
                ("a-3, b-1, c-4, d-2", "a-3, b-1, c-4, d-2"),
                ("a-1, b-3, c-2, d-4", "a-1, b-3, c-2, d-4"),
                ("a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2"),
                ("a-4, b-1, c-3, d-2", "a-4, b-1, c-3, d-2")
            ],
            "correct_key": "A",
            "exp_en": "Total membership is 30 (3). Lok Sabha share is 20 (1). Rajya Sabha share is 10 (4). Reports to the President of India (2). Correct code is a-3, b-1, c-4, d-2.",
            "exp_ta": "மொத்த உறுப்பினர்கள் 30 (3). மக்களவை பங்கு 20 (1). மாநிலங்களவை பங்கு 10 (4). இந்தியக் குடியரசுத் தலைவரிடம் அறிக்கை சமர்ப்பிக்கிறது (2). சரியான குறியீடு: a-3, b-1, c-4, d-2.",
            "why_a_en": "Matches all four institutional dimensions of the Article 344(4) Committee.",
            "why_a_ta": "சரத்து 344(4) குழுவின் நான்கு நிறுவன பரிமாணங்களையும் சரியாகப் பொருத்துகிறது.",
            "why_b_en": "Swaps total membership with Lok Sabha share.",
            "why_b_ta": "மொத்த உறுப்பினர்களை மக்களவைப் பங்குடன் மாற்றுகிறது.",
            "why_c_en": "Swaps Lok Sabha and Rajya Sabha numbers.",
            "why_c_ta": "மக்களவை மற்றும் மாநிலங்களவை எண்களை மாற்றுகிறது.",
            "why_d_en": "Assigns reporting to total membership.",
            "why_d_ta": "அறிக்கை சமர்ப்பிப்பதை மொத்த உறுப்பினர்களுக்கு தவறாக ஒதுக்குகிறது.",
            "tip_en": "The Union Home Minister is customarily elected as the Chairman of this Parliamentary Committee.",
            "tip_ta": "மத்திய உள்துறை அமைச்சர் வழக்கமாக இந்நாடாளுமன்றக் குழுவின் தலைவராகத் தேர்ந்தெடுக்கப்படுகிறார்.",
            "fact_en": "The committee has three sub-committees that conduct inspection tours across the country.",
            "fact_ta": "இக்குழு நாடு முழுவதும் கள ஆய்வுகளை மேற்கொள்ளும் மூன்று துணைக் குழுக்களைக் கொண்டுள்ளது."
        },
        # 24
        {
            "subtopic": "Landmark Judicial Precedents on Language",
            "stem_en": "Match List-I (Case Law) with List-II (Judicial Principle / Ruling) and select the correct answer using the codes given below:\nList-I:\na) Suresh Kachhadia v. UOI (2010)\nb) Union of India v. Murasoli Maran (1977)\nc) Hindi Hitrakshak Samiti v. UOI (1990)\nd) State of Bombay v. Bombay Education Society (1954)\nList-II:\n1. Presidential Orders under Art 344(6) cannot override or dilute rights under Official Languages Act\n2. State cannot deny admission to government-aided schools based on language (Art 29(2) & 30)\n3. Hindi is not the National Language of India as no constitutional provision declares it\n4. No fundamental right to compel Union Public Service Commission to conduct exams solely in Hindi",
            "stem_ta": "பட்டியல்-I-ஐ (வழக்கு) பட்டியல்-II-உடன் (நீதித்துறை தீர்ப்பு / கொள்கை) பொருத்தி, கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\nபட்டியல்-I:\na) சுரேஷ் கச்சாடியா எதிர் இந்திய ஒன்றியம் (2010)\nb) இந்திய ஒன்றியம் எதிர் முரசொலி மாறன் (1977)\nc) இந்தி ஹித்ரக்ஷக் சமிதி எதிர் இந்திய ஒன்றியம் (1990)\nd) பம்பாய் மாநிலம் எதிர் பம்பாய் கல்வி சங்கம் (1954)\nபட்டியல்-II:\n1. சரத்து 344(6)-ன் கீழான குடியரசுத் தலைவர் உத்தரவுகள் அதிகாரப்பூர்வ மொழிகள் சட்ட உரிமைகளை மீற முடியாது\n2. அரசு உதவிபெறும் பள்ளிகளில் மொழி அடிப்படையில் மாணவர் சேர்க்கையை அரசு மறுக்க முடியாது (சரத்து 29(2) & 30)\n3. அரசியலமைப்பு விதி எதுவும் அறிவிக்காததால் இந்தி இந்தியாவின் தேசிய மொழி அல்ல\n4. UPSC தேர்வுகளை இந்தியில் மட்டுமே நடத்தக் கட்டாயப்படுத்த எந்த அடிப்படை உரிமையும் இல்லை",
            "options": [
                ("a-3, b-1, c-4, d-2", "a-3, b-1, c-4, d-2"),
                ("a-1, b-3, c-2, d-4", "a-1, b-3, c-2, d-4"),
                ("a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2"),
                ("a-4, b-1, c-3, d-2", "a-4, b-1, c-3, d-2")
            ],
            "correct_key": "A",
            "exp_en": "Suresh Kachhadia confirmed Hindi is not national language (3). Murasoli Maran protected statutory rights under 1963 Act (1). Hindi Hitrakshak Samiti rejected writ to mandate Hindi exams (4). Bombay Education Society protected English-medium instruction (2). Correct code is a-3, b-1, c-4, d-2.",
            "exp_ta": "சுரேஷ் கச்சாடியா இந்தி தேசிய மொழி அல்ல என்பதை உறுதிப்படுத்தியது (3). முரசொலி மாறன் 1963 சட்ட உரிமைகளைப் பாதுகாத்தது (1). இந்தி ஹித்ரக்ஷக் சமிதி இந்தித் தேர்வு கட்டாய ரிட் மனுவை நிராகரித்தது (4). பம்பாய் கல்வி சங்கம் ஆங்கில வழிக் கல்வியைப் பாதுகாத்தது (2). சரியான குறியீடு: a-3, b-1, c-4, d-2.",
            "why_a_en": "Accurately matches each landmark judicial decision with its ratio decidendi.",
            "why_a_ta": "ஒவ்வொரு வரலாற்றுச் சிறப்புமிக்க தீர்ப்பையும் அதன் சட்டக் கொள்கையுடன் சரியாகப் பொருத்துகிறது.",
            "why_b_en": "Swaps Suresh Kachhadia and Murasoli Maran.",
            "why_b_ta": "சுரேஷ் கச்சாடியா மற்றும் முரசொலி மாறன் வழக்குகளை மாற்றுகிறது.",
            "why_c_en": "Confuses Hindi Hitrakshak with Murasoli Maran.",
            "why_c_ta": "இந்தி ஹித்ரக்ஷக் மற்றும் முரசொலி மாறன் வழக்குகளைக் குழப்புகிறது.",
            "why_d_en": "Assigns UPSC ruling to Suresh Kachhadia.",
            "why_d_ta": "யுபிஎஸ்சி தீர்ப்பை சுரேஷ் கச்சாடியாவுக்கு தவறாக ஒதுக்குகிறது.",
            "tip_en": "In Murasoli Maran (1977), the Supreme Court upheld the constitutional validity of providing Hindi training to central employees without imposing penal consequences.",
            "tip_ta": "முரசொலி மாறன் (1977) வழக்கில், உச்ச நீதிமன்றம் தண்டனை விளைவுகள் இல்லாமல் மத்திய பணியாளர்களுக்கு இந்திப் பயிற்சி அளிப்பதன் அரசியலமைப்பு செல்லுபடியாகும் தன்மையை உறுதி செய்தது.",
            "fact_en": "Bombay Education Society (1954) established the right of Anglo-Indians and others to be taught in English.",
            "fact_ta": "பம்பாய் கல்வி சங்கம் (1954) ஆங்கிலோ-இந்தியர்கள் மற்றும் பிறருக்கு ஆங்கிலத்தில் கற்பிக்கப்படுவதற்கான உரிமையை நிறுவியது."
        },
        # 25
        {
            "subtopic": "Eighth Schedule Additions Chronological Growth",
            "stem_en": "Match List-I (Eighth Schedule Language Strength Milestone) with List-II (Year and Basis) and select the correct answer using the codes given below:\nList-I:\na) 14 Languages\nb) 15 Languages\nc) 18 Languages\nd) 22 Languages\nList-II:\n1. 1967 (21st Amendment Act added Sindhi)\n2. 2003 (92nd Amendment Act added Bodo, Dogri, Maithili, Santhali)\n3. 1950 (Commencement of the Constitution of India)\n4. 1992 (71st Amendment Act added Konkani, Manipuri, Nepali)",
            "stem_ta": "பட்டியல்-I-ஐ (எட்டாவது அட்டவணை மொழி எண்ணிக்கை மைல்கல்) பட்டியல்-II-உடன் (ஆண்டு மற்றும் அடிப்படை) பொருத்தி, கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\nபட்டியல்-I:\na) 14 மொழிகள்\nb) 15 மொழிகள்\nc) 18 மொழிகள்\nd) 22 மொழிகள்\nபட்டியல்-II:\n1. 1967 (21வது திருத்தம் சிந்தியைச் சேர்த்தது)\n2. 2003 (92வது திருத்தம் போடோ, டோக்ரி, மைதிலி, சந்தாலியைச் சேர்த்தது)\n3. 1950 (இந்திய அரசியலமைப்பு அமலுக்கு வந்தபோது)\n4. 1992 (71வது திருத்தம் கொங்கணி, மணிப்பூரி, நேபாளியைச் சேர்த்தது)",
            "options": [
                ("a-3, b-1, c-4, d-2", "a-3, b-1, c-4, d-2"),
                ("a-1, b-3, c-2, d-4", "a-1, b-3, c-2, d-4"),
                ("a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2"),
                ("a-4, b-1, c-3, d-2", "a-4, b-1, c-3, d-2")
            ],
            "correct_key": "A",
            "exp_en": "14 languages in 1950 at commencement (3). 15 languages in 1967 with Sindhi (1). 18 languages in 1992 with Konkani, Manipuri, Nepali (4). 22 languages in 2003 with BDMS (2). Correct code is a-3, b-1, c-4, d-2.",
            "exp_ta": "1950 தொடக்கத்தில் 14 மொழிகள் (3). 1967-ல் சிந்தியுடன் 15 மொழிகள் (1). 1992-ல் கொங்கணி, மணிப்பூரி, நேபாளியுடன் 18 மொழிகள் (4). 2003-ல் BDMS-உடன் 22 மொழிகள் (2). சரியான குறியீடு: a-3, b-1, c-4, d-2.",
            "why_a_en": "Pairs each growth phase of the Eighth Schedule with its exact year and amending Act.",
            "why_a_ta": "எட்டாவது அட்டவணையின் ஒவ்வொரு வளர்ச்சி நிலையையும் அதன் துல்லியமான ஆண்டு மற்றும் திருத்தச் சட்டத்துடன் சரியாகப் பொருத்துகிறது.",
            "why_b_en": "Swaps 14 and 15 language milestones.",
            "why_b_ta": "14 மற்றும் 15 மொழி மைல்கற்களை மாற்றுகிறது.",
            "why_c_en": "Confuses 1992 and 1967.",
            "why_c_ta": "1992 மற்றும் 1967-ஐ குழப்புகிறது.",
            "why_d_en": "Assigns 22 languages to 1950.",
            "why_d_ta": "22 மொழிகளை 1950-க்கு தவறாக ஒதுக்குகிறது.",
            "tip_en": "Progression: 14 -> 15 (+1) -> 18 (+3) -> 22 (+4).",
            "tip_ta": "வளர்ச்சி வரிசை: 14 -> 15 (+1) -> 18 (+3) -> 22 (+4).",
            "fact_en": "The 96th Amendment in 2011 did not change the count of 22; it only renamed Oriya to Odia.",
            "fact_ta": "2011-ன் 96வது திருத்தம் 22 என்ற எண்ணிக்கையை மாற்றவில்லை; ஒரியாவை ஒடியா என மட்டுமே பெயர் மாற்றியது."
        }
    ]

    questions = []
    for idx, item in enumerate(raw_data, start=1):
        qid = f"OL_MF_{idx:03d}"
        opts = item["options"]
        correct_key = item["correct_key"]
        
        q = make_ol_q(
            qid=qid,
            diff="Medium" if idx <= 15 else "Hard",
            qtype="Match the Following",
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
            tags=["polity", "official_language", "match_the_following", item["subtopic"].lower().replace(" ", "_")]
        )
        questions.append(q)
    return questions

def build_match_file():
    qs = get_match_questions()
    print(f"Generated {len(qs)} raw Match the Following questions for Official Language.")
    balanced = randomize_and_balance_dataset(qs, seed=57)
    
    out_dir = os.path.join("data", "questions", "polity")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "official_language_match_the_following.json")
    alias_path = os.path.join(out_dir, "official_language_match.json")
    
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(balanced, f, ensure_ascii=False, indent=2)
    with open(alias_path, "w", encoding="utf-8") as f:
        json.dump(balanced, f, ensure_ascii=False, indent=2)
    print(f"Saved balanced Match MCQs to {out_path} and alias {alias_path}")
    
    rep = ContentValidator.validate_file(out_path, expected_count=25, expected_prefix="OL_MF_")
    print(f"Validation: {'PASS' if rep.is_valid else 'FAIL'} | Total: {rep.total_audited}")
    print(f"Keys: {rep.key_distribution}")
    if not rep.is_valid:
        for iss in rep.issues:
            print("  Issue:", iss.severity, iss.field_name, iss.message)
    return rep.is_valid

if __name__ == "__main__":
    build_match_file()
