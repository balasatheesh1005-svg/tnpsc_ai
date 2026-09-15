# -*- coding: utf-8 -*-
"""
Official Language - Part 1 Easy MCQs Generator (50 MCQs: OL_E_001 to OL_E_050)
Strictly adheres to:
- 24 required fields schema
- Authentic Tamil translations
- Specific why_not_others for A, B, C, D
- Balanced answer keys (12-13 per option)
- ContentValidator pass
"""
import json
import os
from official_language_mcq_helper import make_ol_q
from tools.nova_content_engine.answer_randomizer import randomize_and_balance_dataset
from tools.nova_content_engine.validator import ContentValidator

def get_easy_questions():
    raw_data = [
        # 1
        {
            "subtopic": "Part XVII Constitutional Architecture",
            "stem_en": "Which Part of the Constitution of India contains provisions relating to the Official Language?",
            "stem_ta": "இந்திய அரசியலமைப்பின் எந்தப் பகுதி அதிகாரப்பூர்வ மொழி தொடர்பான விதிகளைக் கொண்டுள்ளது?",
            "options": [
                ("Part XVII", "பகுதி XVII"),
                ("Part XV", "பகுதி XV"),
                ("Part XVI", "பகுதி XVI"),
                ("Part XVIII", "பகுதி XVIII")
            ],
            "correct_key": "A",
            "exp_en": "Part XVII of the Constitution of India (Articles 343 to 351) deals with the Official Language across four dedicated chapters.",
            "exp_ta": "இந்திய அரசியலமைப்பின் பகுதி XVII (சரத்துகள் 343 முதல் 351 வரை) நான்கு அத்தியாயங்களின் கீழ் அதிகாரப்பூர்வ மொழியைக் கையாள்கிறது.",
            "why_a_en": "Part XVII exclusively contains Articles 343-351 governing Official Language.",
            "why_a_ta": "பகுதி XVII மட்டுமே அதிகாரப்பூர்வ மொழி தொடர்பான சரத்துகள் 343-351-ஐக் கொண்டுள்ளது.",
            "why_b_en": "Part XV deals with Elections (Articles 324-329A).",
            "why_b_ta": "பகுதி XV தேர்தல்களைக் கையாள்கிறது (சரத்துகள் 324-329A).",
            "why_c_en": "Part XVI deals with Special Provisions Relating to Certain Classes (Articles 330-342A).",
            "why_c_ta": "பகுதி XVI குறிப்பிட்ட வகுப்பினருக்கான சிறப்பு விதிகளைக் கையாள்கிறது (சரத்துகள் 330-342A).",
            "why_d_en": "Part XVIII deals with Emergency Provisions (Articles 352-360).",
            "why_d_ta": "பகுதி XVIII அவசரகால விதிகளைக் கையாள்கிறது (சரத்துகள் 352-360).",
            "tip_en": "Part XVII: Official Language; Chapter I: Union, Chapter II: Regional, Chapter III: Judiciary/Bills, Chapter IV: Special Directives.",
            "tip_ta": "பகுதி XVII: அதிகாரப்பூர்வ மொழி; அத்தியாயம் 1: ஒன்றியம், அத்தியாயம் 2: வட்டார மொழிகள், அத்தியாயம் 3: நீதிமன்றங்கள்/சட்டங்கள், அத்தியாயம் 4: சிறப்பு வழிகாட்டுதல்கள்.",
            "fact_en": "Part XVII comprises nine articles from Article 343 to Article 351.",
            "fact_ta": "பகுதி XVII சரத்து 343 முதல் சரத்து 351 வரை ஒன்பது சரத்துகளைக் கொண்டுள்ளது."
        },
        # 2
        {
            "subtopic": "Official Language of the Union",
            "stem_en": "According to Article 343(1) of the Constitution of India, what is the official language of the Union?",
            "stem_ta": "இந்திய அரசியலமைப்பின் சரத்து 343(1)-ன் படி, ஒன்றியத்தின் அதிகாரப்பூர்வ மொழி எது?",
            "options": [
                ("Hindi in Devanagari script", "தேவநாகரி வரிவடிவத்திலான இந்தி"),
                ("English in Roman script", "ரோமன் வரிவடிவத்திலான ஆங்கிலம்"),
                ("Hindustani in both scripts", "இரண்டு வரிவடிவங்களிலும் உள்ள இந்துஸ்தானி"),
                ("Sanskrit in Devanagari script", "தேவநாகரி வரிவடிவத்திலான சமஸ்கிருதம்")
            ],
            "correct_key": "A",
            "exp_en": "Article 343(1) provides that the official language of the Union shall be Hindi in Devanagari script, with international form of Indian numerals.",
            "exp_ta": "சரத்து 343(1)-ன் படி ஒன்றியத்தின் அதிகாரப்பூர்வ மொழி தேவநாகரி வரிவடிவத்திலான இந்தியாகும், எண்கள் இந்திய எண்களின் பன்னாட்டு வடிவமாக இருக்கும்.",
            "why_a_en": "Article 343(1) explicitly specifies Hindi in Devanagari script as the official language of the Union.",
            "why_a_ta": "சரத்து 343(1) தேவநாகரி வரிவடிவத்திலான இந்தியை ஒன்றியத்தின் அதிகாரப்பூர்வ மொழியாகத் தெளிவாகக் குறிப்பிடுகிறது.",
            "why_b_en": "English was permitted as an associate official language for a 15-year transition period under Article 343(2).",
            "why_b_ta": "சரத்து 343(2)-ன் கீழ் 15 ஆண்டு இடைக்காலத்திற்கு ஆங்கிலம் கூடுதல் மொழியாக அனுமதிக்கப்பட்டது.",
            "why_c_en": "Hindustani was proposed during Constituent Assembly debates but rejected in the Munshi-Ayyangar formula.",
            "why_c_ta": "இந்துஸ்தானி அரசியல் நிர்ணய சபை விவாதங்களில் முன்மொழியப்பட்டது, ஆனால் முன்ஷி-அய்யங்கார் சூத்திரத்தில் நிராகரிக்கப்பட்டது.",
            "why_d_en": "Sanskrit is an Eighth Schedule and Classical language, not the Union official language.",
            "why_d_ta": "சமஸ்கிருதம் எட்டாவது அட்டவணை மற்றும் செம்மொழி ஆகும், ஒன்றியத்தின் அதிகாரப்பூர்வ மொழி அல்ல.",
            "tip_en": "Remember: The Constitution specifies 'Official Language of the Union', NOT 'National Language'.",
            "tip_ta": "நினைவில் கொள்க: அரசியலமைப்பு 'ஒன்றியத்தின் அதிகாரப்பூர்வ மொழி' என்றே குறிப்பிடுகிறது, 'தேசிய மொழி' என்று அல்ல.",
            "fact_en": "The Munshi-Ayyangar Formula resolved the official language deadlock in September 1949.",
            "fact_ta": "முன்ஷி-அய்யங்கார் சூத்திரம் 1949 செப்டம்பரில் அதிகாரப்பூர்வ மொழி தொடர்பான முட்டுக்கட்டையைத் தீர்த்தது."
        },
        # 3
        {
            "subtopic": "Numerals in Official Language",
            "stem_en": "What form of numerals is prescribed by Article 343(1) for the official purposes of the Union?",
            "stem_ta": "ஒன்றியத்தின் அதிகாரப்பூர்வ பணிகளுக்காக சரத்து 343(1)-ல் பரிந்துரைக்கப்பட்டுள்ள எண்களின் வடிவம் எது?",
            "options": [
                ("The international form of Indian numerals", "இந்திய எண்களின் பன்னாட்டு வடிவம்"),
                ("Devanagari numerals exclusively", "தேவநாகரி எண்கள் மட்டுமே"),
                ("Roman numerals exclusively", "ரோமன் எண்கள் மட்டுமே"),
                ("Any regional script numerals", "எந்தவொரு வட்டார வரிவடிவ எண்களும்")
            ],
            "correct_key": "A",
            "exp_en": "Article 343(1) mandates that the form of numerals to be used for official purposes of the Union shall be the international form of Indian numerals (1, 2, 3...).",
            "exp_ta": "சரத்து 343(1)-ன் படி ஒன்றியத்தின் அதிகாரப்பூர்வ பணிகளுக்கான எண்கள் இந்திய எண்களின் பன்னாட்டு வடிவமாக (1, 2, 3...) இருக்க வேண்டும்.",
            "why_a_en": "Article 343(1) expressly mandates the international form of Indian numerals.",
            "why_a_ta": "சரத்து 343(1) வெளிப்படையாக இந்திய எண்களின் பன்னாட்டு வடிவத்தை கட்டாயமாக்குகிறது.",
            "why_b_en": "Devanagari numerals are permitted only by specific Presidential order under Article 343(2) proviso.",
            "why_b_ta": "சரத்து 343(2) விதியின் கீழ் குடியரசுத் தலைவரின் சிறப்பு ஆணை மூலம் மட்டுமே தேவநாகரி எண்கள் அனுமதிக்கப்படலாம்.",
            "why_c_en": "Roman numerals are not the constitutional standard for official Union calculations.",
            "why_c_ta": "ரோமன் எண்கள் அதிகாரப்பூர்வ ஒன்றிய பயன்பாட்டிற்கான அரசியலமைப்பு வடிவம் அல்ல.",
            "why_d_en": "Regional scripts are not designated for Union-wide official numerals.",
            "why_d_ta": "வட்டார வரிவடிவங்கள் ஒன்றியம் முழுமைக்குமான எண்களாக குறிப்பிடப்படவில்லை.",
            "tip_en": "Article 343(1): Script is Devanagari; Numerals are International Form of Indian Numerals.",
            "tip_ta": "சரத்து 343(1): வரிவடிவம் தேவநாகரி; எண்கள் இந்திய எண்களின் பன்னாட்டு வடிவம்.",
            "fact_en": "The international form of Indian numerals corresponds to Arabic numerals (1, 2, 3, 4...).",
            "fact_ta": "இந்திய எண்களின் பன்னாட்டு வடிவம் என்பது உலகளவில் பயன்படும் (1, 2, 3, 4...) அரபு எண்களையே குறிக்கிறது."
        },
        # 4
        {
            "subtopic": "Initial Transition Period for English",
            "stem_en": "For how many years from the commencement of the Constitution did Article 343(2) permit the continued use of the English language for all official purposes of the Union?",
            "stem_ta": "அரசியலமைப்பு அமலுக்கு வந்ததிலிருந்து எத்தனை ஆண்டுகளுக்கு ஒன்றியத்தின் அனைத்து அதிகாரப்பூர்வ பணிகளுக்கும் ஆங்கில மொழியின் பயன்பாட்டை சரத்து 343(2) அனுமதித்தது?",
            "options": [
                ("15 years", "15 ஆண்டுகள்"),
                ("10 years", "10 ஆண்டுகள்"),
                ("20 years", "20 ஆண்டுகள்"),
                ("5 years", "5 ஆண்டுகள்")
            ],
            "correct_key": "A",
            "exp_en": "Article 343(2) provided that for a period of fifteen years from the commencement of the Constitution (until January 25, 1965), English shall continue to be used.",
            "exp_ta": "அரசியலமைப்பு அமலுக்கு வந்ததிலிருந்து பதினைந்து ஆண்டுகள் வரை (1965 ஜனவரி 25 வரை) ஆங்கிலம் தொடர்ந்து பயன்படுத்தப்படும் என்று சரத்து 343(2) வழங்கியது.",
            "why_a_en": "The initial transition period was exactly 15 years (January 26, 1950 to January 25, 1965).",
            "why_a_ta": "தொடக்க இடைக்காலம் சரியாக 15 ஆண்டுகள் (1950 ஜனவரி 26 முதல் 1965 ஜனவரி 25 வரை).",
            "why_b_en": "10 years was the period for Article 344(1) second commission appointment, not the overall transition.",
            "why_b_ta": "10 ஆண்டுகள் என்பது சரத்து 344(1)-ன் கீழ் இரண்டாவது ஆணையத்திற்கான காலம், இடைக்காலம் அல்ல.",
            "why_c_en": "20 years was not provided in Article 343(2).",
            "why_c_ta": "20 ஆண்டுகள் என்பது சரத்து 343(2)-ல் வழங்கப்படவில்லை.",
            "why_d_en": "5 years was the timeline for the first Official Language Commission under Article 344(1).",
            "why_d_ta": "5 ஆண்டுகள் என்பது சரத்து 344(1)-ன் கீழ் முதல் அதிகாரப்பூர்வ மொழி ஆணையத்திற்கான கால அவகாசம்.",
            "tip_en": "Article 343(2) transition period = 15 years (1950 to 1965).",
            "tip_ta": "சரத்து 343(2) இடைக்காலம் = 15 ஆண்டுகள் (1950 முதல் 1965 வரை).",
            "fact_en": "The 15-year period expired on January 25, 1965, leading to massive anti-Hindi agitations in Tamil Nadu.",
            "fact_ta": "15 ஆண்டு காலம் 1965 ஜனவரி 25-ல் காலாவதியானது, இது தமிழகத்தில் பெரும் இந்தி எதிர்ப்புப் போராட்டத்திற்கு வழிவகுத்தது."
        },
        # 5
        {
            "subtopic": "Parliamentary Power to Extend English",
            "stem_en": "Which clause of Article 343 empowers Parliament to provide by law for the continued use of English beyond the 15-year period?",
            "stem_ta": "15 ஆண்டு காலத்திற்குப் பிறகும் ஆங்கிலத்தின் பயன்பாட்டைச் சட்டத்தின் மூலம் நீட்டிக்க நாடாளுமன்றத்திற்கு அதிகாரமளிக்கும் சரத்து 343-ன் உட்பிரிவு எது?",
            "options": [
                ("Article 343(3)", "சரத்து 343(3)"),
                ("Article 343(1)", "சரத்து 343(1)"),
                ("Article 343(2)", "சரத்து 343(2)"),
                ("Article 344(1)", "சரத்து 344(1)")
            ],
            "correct_key": "A",
            "exp_en": "Under Article 343(3), Parliament may by law provide for the use, after the said period of fifteen years, of the English language for specified official purposes.",
            "exp_ta": "சரத்து 343(3)-ன் கீழ் நாடாளுமன்றம் சட்டமியற்றுவதன் மூலம், குறிப்பிட்ட பணிகளுக்காக 15 ஆண்டுகளுக்குப் பிறகும் ஆங்கில மொழி பயன்பாட்டைத் தொடர வகை செய்யலாம்.",
            "why_a_en": "Article 343(3) is the constitutional enabling clause under which the Official Languages Act, 1963 was enacted.",
            "why_a_ta": "சரத்து 343(3) என்பது அதிகாரப்பூர்வ மொழிகள் சட்டம், 1963 இயற்றப்பட்ட அரசியல் சாசன அதிகாரப் பிரிவாகும்.",
            "why_b_en": "Article 343(1) defines the official language as Hindi in Devanagari script.",
            "why_b_ta": "சரத்து 343(1) தேவநாகரி இந்தியை அதிகாரப்பூர்வ மொழியாக வரையறுக்கிறது.",
            "why_c_en": "Article 343(2) specifies the initial 15-year transitional use of English.",
            "why_c_ta": "சரத்து 343(2) தொடக்க 15 ஆண்டுகால இடைக்கால பயன்பாட்டைக் குறிப்பிடுகிறது.",
            "why_d_en": "Article 344(1) deals with appointment of the Official Language Commission.",
            "why_d_ta": "சரத்து 344(1) அதிகாரப்பூர்வ மொழி ஆணையம் அமைப்பதைக் கையாள்கிறது.",
            "tip_en": "Official Languages Act, 1963 draws legislative competence directly from Article 343(3).",
            "tip_ta": "அதிகாரப்பூர்வ மொழிகள் சட்டம், 1963 நேரடியாக சரத்து 343(3)-லிருந்தே சட்டமியற்றும் அதிகாரத்தைப் பெறுகிறது.",
            "fact_en": "Without Article 343(3), the continued use of English after January 26, 1965 would have been unconstitutional.",
            "fact_ta": "சரத்து 343(3) இல்லையென்றால் 1965 ஜனவரி 26-க்குப் பிறகு ஆங்கிலத்தைப் பயன்படுத்துவது அரசியலமைப்புக்கு எதிரானதாகியிருக்கும்."
        },
        # 6
        {
            "subtopic": "Official Language Commission Appointment",
            "stem_en": "Under Article 344(1), who is empowered to constitute the Commission on Official Language?",
            "stem_ta": "சரத்து 344(1)-ன் கீழ் அதிகாரப்பூர்வ மொழிக்கான ஆணையத்தை அமைக்கும் அதிகாரம் யாரிடம் உள்ளது?",
            "options": [
                ("The President of India", "இந்தியக் குடியரசுத் தலைவர்"),
                ("The Prime Minister of India", "இந்தியப் பிரதமர்"),
                ("The Speaker of Lok Sabha", "மக்களவைத் தலைவர்"),
                ("The Chief Justice of India", "இந்தியத் தலைமை நீதிபதி")
            ],
            "correct_key": "A",
            "exp_en": "Article 344(1) provides that the President shall, at the expiration of 5 years and thereafter 10 years from the commencement of the Constitution, constitute a Commission on Official Language.",
            "exp_ta": "சரத்து 344(1)-ன் படி, அரசியலமைப்பு அமலுக்கு வந்த 5 ஆண்டுகள் முடிவிலும், பின்னர் 10 ஆண்டுகள் முடிவிலும் குடியரசுத் தலைவர் அதிகாரப்பூர்வ மொழி ஆணையத்தை அமைக்க வேண்டும்.",
            "why_a_en": "Article 344(1) explicitly vests the power to appoint the Commission in the President.",
            "why_a_ta": "சரத்து 344(1) மொழி ஆணையத்தை நியமிக்கும் அதிகாரத்தை வெளிப்படையாகக் குடியரசுத் தலைவரிடம் ஒப்படைக்கிறது.",
            "why_b_en": "The Prime Minister heads the Cabinet but does not constitutionally appoint the Commission.",
            "why_b_ta": "பிரதமர் அமைச்சரவையின் தலைவர், ஆனால் அரசியலமைப்பு ரீதியாக ஆணையத்தை நியமிப்பவர் அல்ல.",
            "why_c_en": "The Speaker presides over Lok Sabha and has no power to constitute this Commission.",
            "why_c_ta": "மக்களவைத் தலைவர் மக்களவைக்குத் தலைமை தாங்குபவர், இந்த ஆணையத்தை அமைக்கும் அதிகாரம் அவருக்கு இல்லை.",
            "why_d_en": "The Chief Justice of India heads the judiciary with no executive appointing role here.",
            "why_d_ta": "இந்தியத் தலைமை நீதிபதி நீதித்துறையின் தலைவர், இங்கு அவருக்கு நியமனப் பங்கு இல்லை.",
            "tip_en": "Article 344 Commission: Appointed by President after 5 years (1955) and 10 years (1960).",
            "tip_ta": "சரத்து 344 ஆணையம்: 5 ஆண்டுகள் (1955) மற்றும் 10 ஆண்டுகள் (1960) முடிவில் குடியரசுத் தலைவரால் நியமிக்கப்படுகிறது.",
            "fact_en": "The first commission under Article 344 was appointed in 1955 under B.G. Kher.",
            "fact_ta": "சரத்து 344-ன் கீழ் முதல் ஆணையம் 1955-ல் பி.ஜி. கெர் தலைமையில் அமைக்கப்பட்டது."
        },
        # 7
        {
            "subtopic": "First Official Language Commission Chairman",
            "stem_en": "Who was appointed as the Chairman of the First Official Language Commission constituted in 1955?",
            "stem_ta": "1955-ல் அமைக்கப்பட்ட முதலாவது அதிகாரப்பூர்வ மொழி ஆணையத்தின் தலைவராக நியமிக்கப்பட்டவர் யார்?",
            "options": [
                ("B.G. Kher", "பி.ஜி. கெர்"),
                ("Gobind Ballabh Pant", "கோவிந்த் வல்லப் பந்த்"),
                ("H.N. Kunzru", "எச்.என். குன்ஸ்ரு"),
                ("Fazl Ali", "பசல் அலி")
            ],
            "correct_key": "A",
            "exp_en": "The first Official Language Commission was appointed by President Dr. Rajendra Prasad in June 1955 under the chairmanship of B.G. Kher.",
            "exp_ta": "முதலாவது அதிகாரப்பூர்வ மொழி ஆணையம் 1955 ஜூன் மாதம் குடியரசுத் தலைவர் டாக்டர் ராஜேந்திர பிரசாத்தால் பி.ஜி. கெர் தலைமையில் அமைக்கப்பட்டது.",
            "why_a_en": "B.G. Kher was the former Chief Minister of Bombay and Chairman of the 1955 Commission.",
            "why_a_ta": "பி.ஜி. கெர் பம்பாயின் முன்னாள் முதலமைச்சர் மற்றும் 1955 மொழி ஆணையத்தின் தலைவராவார்.",
            "why_b_en": "G.B. Pant chaired the Parliamentary Committee constituted in 1957 to review the Kher report.",
            "why_b_ta": "ஜி.பி. பந்த் 1957-ல் கெர் அறிக்கையை ஆய்வு செய்ய அமைக்கப்பட்ட நாடாளுமன்றக் குழுவின் தலைவராக இருந்தார்.",
            "why_c_en": "H.N. Kunzru was a member of the States Reorganisation Commission, not chairman of this Commission.",
            "why_c_ta": "எச்.என். குன்ஸ்ரு மாநில மறுசீரமைப்பு ஆணையத்தின் உறுப்பினர் ஆவார்.",
            "why_d_en": "Fazl Ali headed the States Reorganisation Commission (1953-1955).",
            "why_d_ta": "பசல் அலி மாநில மறுசீரமைப்பு ஆணையத்திற்கு (1953-1955) தலைமை தாங்கினார்.",
            "tip_en": "1955 Commission = B.G. Kher; 1957 Parliamentary Committee = G.B. Pant.",
            "tip_ta": "1955 ஆணையம் = பி.ஜி. கெர்; 1957 நாடாளுமன்றக் குழு = ஜி.பி. பந்த்.",
            "fact_en": "The Kher Commission submitted its comprehensive report in 1956.",
            "fact_ta": "கெர் ஆணையம் தனது விரிவான அறிக்கையை 1956-ல் சமர்ப்பித்தது."
        },
        # 8
        {
            "subtopic": "Parliamentary Committee on Official Language Membership",
            "stem_en": "How many total members constitute the Committee of Parliament on Official Language under Article 344(4)?",
            "stem_ta": "சரத்து 344(4)-ன் கீழ் அதிகாரப்பூர்வ மொழிக்கான நாடாளுமன்றக் குழுவில் உள்ள மொத்த உறுப்பினர்கள் எத்தனை பேர்?",
            "options": [
                ("30 members", "30 உறுப்பினர்கள்"),
                ("22 members", "22 உறுப்பினர்கள்"),
                ("15 members", "15 உறுப்பினர்கள்"),
                ("45 members", "45 உறுப்பினர்கள்")
            ],
            "correct_key": "A",
            "exp_en": "Article 344(4) specifies that the Committee shall consist of 30 members: 20 from the House of the People (Lok Sabha) and 10 from the Council of States (Rajya Sabha).",
            "exp_ta": "சரத்து 344(4)-ன் படி அக்குழுவில் 30 உறுப்பினர்கள் இருப்பர்: மக்களவையிலிருந்து 20 உறுப்பினர்கள் மற்றும் மாநிலங்களவையிலிருந்து 10 உறுப்பினர்கள்.",
            "why_a_en": "The Committee is fixed by Article 344(4) at exactly 30 members (20 Lok Sabha + 10 Rajya Sabha).",
            "why_a_ta": "சரத்து 344(4)-ன் படி இக்குழு சரியாக 30 உறுப்பினர்களைக் கொண்டது (20 மக்களவை + 10 மாநிலங்களவை).",
            "why_b_en": "22 members is the size of the Public Accounts Committee and Committee on Public Undertakings (15 LS + 7 RS).",
            "why_b_ta": "22 உறுப்பினர்கள் என்பது பொதுக் கணக்குக் குழு மற்றும் பொதுத்துறை நிறுவனங்கள் குழுவின் எண்ணிக்கை (15 மக்களவை + 7 மாநிலங்களவை).",
            "why_c_en": "15 members is the size of various standing or select committees.",
            "why_c_ta": "15 உறுப்பினர்கள் என்பது பல்வேறு நிலைக்குழுக்களின் எண்ணிக்கை.",
            "why_d_en": "45 members is not the strength of any official language committee.",
            "why_d_ta": "45 உறுப்பினர்கள் என்பது எந்தவொரு மொழிக்குழுவின் பலமும் அல்ல.",
            "tip_en": "Article 344(4) Committee Ratio = 2:1 (20 Lok Sabha : 10 Rajya Sabha).",
            "tip_ta": "சரத்து 344(4) குழு விகிதம் = 2:1 (20 மக்களவை : 10 மாநிலங்களவை).",
            "fact_en": "Members are elected by proportional representation by means of the single transferable vote.",
            "fact_ta": "உறுப்பினர்கள் ஒற்றை மாற்று வாக்கு முறை மூலம் விகிதாச்சாரப் பிரதிநிதித்துவ அடிப்படையில் தேர்ந்தெடுக்கப்படுகிறார்கள்."
        },
        # 9
        {
            "subtopic": "Election Method of Article 344(4) Committee",
            "stem_en": "By what system are the members of the Parliamentary Committee on Official Language elected?",
            "stem_ta": "அதிகாரப்பூர்வ மொழிக்கான நாடாளுமன்றக் குழுவின் உறுப்பினர்கள் எந்த தேர்தல் முறை மூலம் தேர்ந்தெடுக்கப்படுகிறார்கள்?",
            "options": [
                ("Proportional representation by means of the single transferable vote", "ஒற்றை மாற்று வாக்கு மூலம் விகிதாச்சாரப் பிரதிநிதித்துவ முறை"),
                ("Simple majority vote in joint sitting", "கூட்டுக் கூட்டத்தில் எளிய பெரும்பான்மை வாக்கு"),
                ("Direct nomination by the Prime Minister", "பிரதமரால் நேரடியாக நியமனம்"),
                ("First-past-the-post voting in each House", "ஒவ்வொரு அவையிலும் அதிக வாக்குகள் பெறும் முறை"),
            ],
            "correct_key": "A",
            "exp_en": "Under Article 344(4), members are elected respectively by the members of Lok Sabha and Rajya Sabha in accordance with the system of proportional representation by means of the single transferable vote.",
            "exp_ta": "சரத்து 344(4)-ன் கீழ், மக்களவை மற்றும் மாநிலங்களவை உறுப்பினர்களால் ஒற்றை மாற்று வாக்கு மூலம் விகிதாச்சாரப் பிரதிநிதித்துவ முறையில் உறுப்பினர்கள் தேர்ந்தெடுக்கப்படுகின்றனர்.",
            "why_a_en": "Article 344(4) mandates proportional representation with single transferable vote to ensure minority party representation.",
            "why_a_ta": "சிறுபான்மை கட்சிகளின் பிரதிநிதித்துவத்தை உறுதி செய்ய சரத்து 344(4) ஒற்றை மாற்று வாக்கு விகிதாச்சார முறையைக் கட்டாயமாக்குகிறது.",
            "why_b_en": "Joint sitting is not convened for electing this committee.",
            "why_b_ta": "இக்குழுவைத் தேர்ந்தெடுப்பதற்கு கூட்டுக் கூட்டம் கூட்டப்படுவதில்லை.",
            "why_c_en": "Members are elected by Parliament, not nominated by the Prime Minister.",
            "why_c_ta": "உறுப்பினர்கள் நாடாளுமன்றத்தால் தேர்ந்தெடுக்கப்படுகிறார்கள், பிரதமரால் நியமிக்கப்படுவதில்லை.",
            "why_d_en": "First-past-the-post is used for general elections to Lok Sabha, not for this committee.",
            "why_d_ta": "அதிக வாக்குகள் பெறும் முறை மக்களவைப் பொதுத் தேர்தலுக்குப் பயன்படுகிறது, இக்குழுவிற்கு அல்ல.",
            "tip_en": "Like Presidential/Rajya Sabha elections, this committee uses PR with STV.",
            "tip_ta": "குடியரசுத் தலைவர்/மாநிலங்களவைத் தேர்தல் போன்று, இக்குழுவும் ஒற்றை மாற்று வாக்கு விகிதாச்சார முறையைப் பயன்படுத்துகிறது.",
            "fact_en": "Conventionally, the Union Home Minister is elected as the Chairman of this Committee.",
            "fact_ta": "வழக்கமாக, ஒன்றிய உள்துறை அமைச்சர் இக்குழுவின் தலைவராகத் தேர்ந்தெடுக்கப்படுகிறார்."
        },
        # 10
        {
            "subtopic": "Official Language of a State",
            "stem_en": "Which Article of the Constitution empowers the Legislature of a State to adopt one or more languages in use in the State or Hindi as its official language?",
            "stem_ta": "மாநிலத்தில் பயன்பாட்டில் உள்ள ஒன்று அல்லது அதற்கு மேற்பட்ட மொழிகளையோ அல்லது இந்தியையோ மாநிலத்தின் அதிகாரப்பூர்வ மொழியாக ஏற்றுக்கொள்ள மாநில சட்டமன்றத்திற்கு அதிகாரமளிக்கும் சரத்து எது?",
            "options": [
                ("Article 345", "சரத்து 345"),
                ("Article 343", "சரத்து 343"),
                ("Article 346", "சரத்து 346"),
                ("Article 347", "சரத்து 347")
            ],
            "correct_key": "A",
            "exp_en": "Article 345 provides that the Legislature of a State may by law adopt any one or more of the languages in use in the State or Hindi as the language or languages to be used for all or any of the official purposes of that State.",
            "exp_ta": "சரத்து 345-ன் படி, மாநில சட்டமன்றம் சட்டத்தின் மூலம் மாநிலத்தில் பயன்பாட்டில் உள்ள ஏதேனும் ஒன்று அல்லது அதற்கு மேற்பட்ட மொழிகளையோ அல்லது இந்தியையோ அம்மாநிலத்தின் அதிகாரப்பூர்வ மொழியாக ஏற்றுக்கொள்ளலாம்.",
            "why_a_en": "Article 345 is the core provision granting language autonomy to State Legislatures.",
            "why_a_ta": "சரத்து 345 என்பது மாநில சட்டமன்றங்களுக்கு மொழி சுயாட்சியை வழங்கும் முக்கிய விதியாகும்.",
            "why_b_en": "Article 343 deals with the official language of the Union, not States.",
            "why_b_ta": "சரத்து 343 ஒன்றியத்தின் அதிகாரப்பூர்வ மொழியைக் கையாள்கிறது, மாநிலங்களை அல்ல.",
            "why_c_en": "Article 346 deals with inter-state communication language.",
            "why_c_ta": "சரத்து 346 மாநிலங்களுக்கு இடையேயான தொடர்பு மொழியைக் கையாள்கிறது.",
            "why_d_en": "Article 347 deals with Presidential recognition of languages spoken by a section of a State population.",
            "why_d_ta": "சரத்து 347 மாநிலத்தின் ஒரு பகுதியினரால் பேசப்படும் மொழிகளுக்கான குடியரசுத் தலைவரின் அங்கீகாரத்தைக் கையாள்கிறது.",
            "tip_en": "Article 345 = State Official Language(s); A State is NOT bound to choose an Eighth Schedule language.",
            "tip_ta": "சரத்து 345 = மாநில அதிகாரப்பூர்வ மொழி(கள்); ஒரு மாநிலம் எட்டாவது அட்டவணை மொழியையே தேர்ந்தெடுக்க வேண்டும் என்ற கட்டாயமில்லை.",
            "fact_en": "Nagaland and Meghalaya adopted English as their official language under Article 345.",
            "fact_ta": "நாகாலாந்து மற்றும் மேகாலயா மாநிலங்கள் சரத்து 345-ன் கீழ் ஆங்கிலத்தைத் தங்கள் அதிகாரப்பூர்வ மொழியாக ஏற்றுக்கொண்டன."
        },
        # 11
        {
            "subtopic": "Inter-State Communication Language",
            "stem_en": "Under Article 346, what is the default language for communication between one State and another State, and between a State and the Union?",
            "stem_ta": "சரத்து 346-ன் படி, ஒரு மாநிலத்திற்கும் மற்றொரு மாநிலத்திற்கும் இடையேயும், ஒரு மாநிலத்திற்கும் ஒன்றியத்திற்கும் இடையேயும் தொடர்புக்கான இயல்புநிலை மொழி எது?",
            "options": [
                ("The language authorized for use in the Union for official purposes", "ஒன்றியத்தின் அதிகாரப்பூர்வ பணிகளுக்குப் பயன்படுத்த அங்கீகரிக்கப்பட்ட மொழி"),
                ("Hindi in Devanagari script exclusively", "தேவநாகரி வரிவடிவ இந்தி மட்டுமே"),
                ("The official language of the sender State", "அனுப்பும் மாநிலத்தின் அதிகாரப்பூர்வ மொழி"),
                ("Sanskrit language exclusively", "சமஸ்கிருத மொழி மட்டுமே")
            ],
            "correct_key": "A",
            "exp_en": "Article 346 specifies that the language for the time being authorized for use in the Union for official purposes shall be the official language for communication between States and between a State and the Union.",
            "exp_ta": "சரத்து 346-ன் படி, ஒன்றியத்தின் அதிகாரப்பூர்வ பயன்பாட்டிற்காக அந்த நேரத்தில் அங்கீகரிக்கப்பட்டுள்ள மொழியே மாநிலங்களுக்கு இடையேயும், மாநிலத்திற்கும் ஒன்றியத்திற்கும் இடையேயான தொடர்பு மொழியாக இருக்கும்.",
            "why_a_en": "Article 346 links the inter-state communication language directly to whatever language is authorized for Union purposes (currently English and Hindi).",
            "why_a_ta": "சரத்து 346 தொடர்பு மொழியை ஒன்றியத்தின் பணிகளுக்கு அங்கீகரிக்கப்பட்ட மொழியுடன் நேரடியாக இணைக்கிறது (தற்போது ஆங்கிலம் மற்றும் இந்தி).",
            "why_b_en": "Hindi is not the exclusive compulsory inter-state language under Article 346.",
            "why_b_ta": "சரத்து 346-ன் கீழ் இந்தி மட்டுமே கட்டாய தொடர்பு மொழி அல்ல.",
            "why_c_en": "The sender State cannot unilaterally impose its regional language on other States.",
            "why_c_ta": "அனுப்பும் மாநிலம் தனது வட்டார மொழியை மற்ற மாநிலங்களின் மீது ஒருதலைப்பட்சமாக திணிக்க முடியாது.",
            "why_d_en": "Sanskrit has never been the inter-state administrative language of the Republic of India.",
            "why_d_ta": "சமஸ்கிருதம் இந்தியக் குடியரசின் மாநிலங்களுக்கு இடையேயான நிர்வாக மொழியாக இருந்ததில்லை.",
            "tip_en": "Article 346 proviso: Two or more States can agree to use Hindi for communication between themselves.",
            "tip_ta": "சரத்து 346 விதிவிலக்கு: இரண்டு அல்லது அதற்கு மேற்பட்ட மாநிலங்கள் தங்களுக்கு இடையே இந்தியைத் தொடர்பு மொழியாகப் பயன்படுத்த ஒப்புக்கொள்ளலாம்.",
            "fact_en": "Non-Hindi states communicate with the Union in English under the Official Languages Act, 1963.",
            "fact_ta": "இந்தி பேசாத மாநிலங்கள் அதிகாரப்பூர்வ மொழிகள் சட்டம், 1963-ன் கீழ் ஒன்றியத்துடன் ஆங்கிலத்தில் தொடர்பு கொள்கின்றன."
        },
        # 12
        {
            "subtopic": "Agreement Between States on Language",
            "stem_en": "Under the proviso to Article 346, what language may two or more States agree to use for communication between themselves?",
            "stem_ta": "சரத்து 346-ன் விதிவிலக்கின் கீழ், இரண்டு அல்லது அதற்கு மேற்பட்ட மாநிலங்கள் தங்களுக்கு இடையேயான தொடர்புக்கு எந்த மொழியைப் பயன்படுத்த ஒப்புக்கொள்ளலாம்?",
            "options": [
                ("Hindi", "இந்தி"),
                ("English only", "ஆங்கிலம் மட்டும்"),
                ("Sanskrit only", "சமஸ்கிருதம் மட்டும்"),
                ("Any foreign language", "எந்தவொரு வெளிநாட்டு மொழி")
            ],
            "correct_key": "A",
            "exp_en": "The proviso to Article 346 provides that if two or more States agree that the Hindi language should be the official language for communication between such States, that language may be used.",
            "exp_ta": "சரத்து 346-ன் விதிவிலக்கின் படி, இரண்டு அல்லது அதற்கு மேற்பட்ட மாநிலங்கள் தங்களுக்கு இடையேயான தொடர்பு மொழியாக இந்தி இருக்க வேண்டும் என ஒப்புக்கொண்டால், அந்த மொழியைப் பயன்படுத்தலாம்.",
            "why_a_en": "Article 346 proviso specifically provides for voluntary inter-State agreement on Hindi.",
            "why_a_ta": "சரத்து 346 விதிவிலக்கு குறிப்பாக இந்தி தொடர்பான மாநிலங்களுக்கிடையேயான தன்னார்வ உடன்படிக்கைக்கு வகை செய்கிறது.",
            "why_b_en": "English is already the default link language; the proviso creates a specific enabling window for Hindi.",
            "why_b_ta": "ஆங்கிலம் ஏற்கனவே இயல்புநிலை தொடர்பு மொழியாக உள்ளது; விதிவிலக்கு இந்திக்கான சிறப்பு வசதியை உருவாக்குகிறது.",
            "why_c_en": "Sanskrit is not mentioned in Article 346 proviso.",
            "why_c_ta": "சரத்து 346 விதிவிலக்கில் சமஸ்கிருதம் குறிப்பிடப்படவில்லை.",
            "why_d_en": "Foreign languages cannot be chosen for domestic inter-state official communication.",
            "why_d_ta": "உள்நாட்டு மாநிலங்களுக்கிடையேயான அதிகாரப்பூர்வ தொடர்புக்கு வெளிநாட்டு மொழிகளைத் தேர்ந்தெடுக்க முடியாது.",
            "tip_en": "Hindi States (e.g. UP, MP, Bihar, Rajasthan) use Hindi under this proviso.",
            "tip_ta": "இந்தி பேசும் மாநிலங்கள் (எ.கா. உ.பி, ம.பி, பீகார், ராஜஸ்தான்) இந்த விதிவிலக்கின் கீழ் இந்தியைப் பயன்படுத்துகின்றன.",
            "fact_en": "The agreement requires mutual consent between the participating States.",
            "fact_ta": "இந்த உடன்படிக்கைக்கு சம்பந்தப்பட்ட மாநிலங்களின் பரஸ்பர சம்மதம் தேவைப்படுகிறது."
        },
        # 13
        {
            "subtopic": "Special Provision for Spoken Languages",
            "stem_en": "Which Article of the Constitution empowers the President to direct that a language spoken by a section of the population of a State be officially recognized throughout that State or in any part thereof?",
            "stem_ta": "ஒரு மாநிலத்தின் குறிப்பிட்ட பகுதியினரால் பேசப்படும் மொழியை அந்த மாநிலம் முழுவதும் அல்லது ஏதேனும் ஒரு பகுதியில் அதிகாரப்பூர்வமாக அங்கீகரிக்க வழிகாட்டும் அதிகாரத்தை குடியரசுத் தலைவருக்கு வழங்கும் அரசியலமைப்பு சரத்து எது?",
            "options": [
                ("Article 347", "சரத்து 347"),
                ("Article 345", "சரத்து 345"),
                ("Article 348", "சரத்து 348"),
                ("Article 350", "சரத்து 350")
            ],
            "correct_key": "A",
            "exp_en": "Article 347 empowers the President, on a demand being made, if satisfied that a substantial proportion of the population of a State desire the use of any language spoken by them, to direct its official recognition.",
            "exp_ta": "சரத்து 347-ன் படி, கோரிக்கை விடுக்கப்படும்போது, ஒரு மாநிலத்தின் மக்கட்தொகையில் கணிசமான பகுதியினர் தாங்கள் பேசும் மொழியைப் பயன்படுத்த விரும்புகிறார்கள் என்பதில் திருப்தியடைந்தால், குடியரசுத் தலைவர் அதனை அதிகாரப்பூர்வமாக அங்கீகரிக்க உத்தரவிடலாம்.",
            "why_a_en": "Article 347 is the dedicated provision protecting linguistic minorities within a State through Presidential direction.",
            "why_a_ta": "சரத்து 347 என்பது குடியரசுத் தலைவரின் உத்தரவு மூலம் மாநிலத்திற்குள் உள்ள மொழிச் சிறுபான்மையினரைப் பாதுகாக்கும் பிரத்யேக விதியாகும்.",
            "why_b_en": "Article 345 empowers the State Legislature, not the President.",
            "why_b_ta": "சரத்து 345 குடியரசுத் தலைவருக்கு அல்ல, மாநில சட்டமன்றத்திற்கு அதிகாரமளிக்கிறது.",
            "why_c_en": "Article 348 deals with language of the Supreme Court, High Courts, and Acts.",
            "why_c_ta": "சரத்து 348 உச்ச நீதிமன்றம், உயர் நீதிமன்றங்கள் மற்றும் சட்டங்களின் மொழியைக் கையாள்கிறது.",
            "why_d_en": "Article 350 deals with language used in representations for redress of grievances.",
            "why_d_ta": "சரத்து 350 குறைகளைத் தீர்ப்பதற்கான மனுக்களில் பயன்படுத்தப்படும் மொழியைக் கையாள்கிறது.",
            "tip_en": "Article 347 protects minority spoken languages from majoritarian suppression by State Legislatures.",
            "tip_ta": "சரத்து 347 மாநில சட்டமன்றங்களின் பெரும்பான்மைவாத ஒடுக்குமுறையிலிருந்து சிறுபான்மையினர் பேசும் மொழிகளைப் பாதுகாக்கிறது.",
            "fact_en": "Presidential direction under Article 347 requires satisfaction that a 'substantial proportion' desires it.",
            "fact_ta": "சரத்து 347-ன் கீழ் குடியரசுத் தலைவரின் உத்தரவுக்கு 'கணிசமான பகுதியினர்' விரும்புகிறார்கள் என்ற திருப்தி அவசியமாகும்."
        },
        # 14
        {
            "subtopic": "Language of the Supreme Court",
            "stem_en": "Under Article 348(1)(a), in what language shall all proceedings in the Supreme Court of India be conducted until Parliament by law otherwise provides?",
            "stem_ta": "சரத்து 348(1)(a)-ன் கீழ், நாடாளுமன்றம் சட்டத்தின் மூலம் வேறுவிதமாக வகை செய்யும் வரை, இந்திய உச்ச நீதிமன்றத்தின் அனைத்து நடவடிக்கைகளும் எந்த மொழியில் நடத்தப்பட வேண்டும்?",
            "options": [
                ("English", "ஆங்கிலம்"),
                ("Hindi in Devanagari script", "தேவநாகரி வரிவடிவ இந்தி"),
                ("Either English or Hindi at the discretion of the Chief Justice", "தலைமை நீதிபதியின் விருப்பப்படி ஆங்கிலம் அல்லது இந்தி"),
                ("Any Eighth Schedule language", "ஏதேனும் ஓர் எட்டாவது அட்டவணை மொழி")
            ],
            "correct_key": "A",
            "exp_en": "Article 348(1)(a) provides that until Parliament by law otherwise provides, all proceedings in the Supreme Court and in every High Court shall be in the English language.",
            "exp_ta": "சரத்து 348(1)(a)-ன் படி, நாடாளுமன்றம் சட்டத்தின் மூலம் வேறுவிதமாக வகை செய்யும் வரை, உச்ச நீதிமன்றம் மற்றும் ஒவ்வொரு உயர் நீதிமன்றத்தின் அனைத்து நடவடிக்கைகளும் ஆங்கில மொழியிலேயே இருக்க வேண்டும்.",
            "why_a_en": "Article 348(1)(a) explicitly mandates English for all Supreme Court proceedings.",
            "why_a_ta": "சரத்து 348(1)(a) உச்ச நீதிமன்றத்தின் அனைத்து நடவடிக்கைகளுக்கும் வெளிப்படையாக ஆங்கிலத்தைக் கட்டாயமாக்குகிறது.",
            "why_b_en": "Hindi is not authorized for the Supreme Court; only Parliament can authorize it by law, which has not been done.",
            "why_b_ta": "உச்ச நீதிமன்றத்திற்கு இந்தி அங்கீகரிக்கப்படவில்லை; நாடாளுமன்றம் மட்டுமே சட்டம் மூலம் அங்கீகரிக்க முடியும், அது இதுவரை செய்யப்படவில்லை.",
            "why_c_en": "The Chief Justice of India has no discretionary power to change the constitutional language of proceedings.",
            "why_c_ta": "நடவடிக்கைகளின் அரசியலமைப்பு மொழியை மாற்றுவதற்கு இந்தியத் தலைமை நீதிபதிக்கு விருப்புரிமை அதிகாரம் இல்லை.",
            "why_d_en": "Eighth Schedule languages cannot be used for Supreme Court proceedings without parliamentary enactment.",
            "why_d_ta": "நாடாளுமன்றச் சட்டமின்றி உச்ச நீதிமன்ற நடவடிக்கைகளுக்கு எட்டாவது அட்டவணை மொழிகளைப் பயன்படுத்த முடியாது.",
            "tip_en": "Supreme Court language = ENGLISH ONLY until Parliament passes a law otherwise.",
            "tip_ta": "நாடாளுமன்றம் வேறுவிதமாக சட்டம் இயற்றும் வரை உச்ச நீதிமன்றத்தின் மொழி = ஆங்கிலம் மட்டுமே.",
            "fact_en": "Even the Governor/President cannot authorize Hindi in the Supreme Court; that applies only to High Courts under 348(2).",
            "fact_ta": "குடியரசுத் தலைவர் அல்லது ஆளுநர் கூட உச்ச நீதிமன்றத்தில் இந்தியை அனுமதிக்க முடியாது; அது 348(2)-ன் கீழ் உயர் நீதிமன்றங்களுக்கு மட்டுமே பொருந்தும்."
        },
        # 15
        {
            "subtopic": "Authoritative Texts of Bills and Acts",
            "stem_en": "According to Article 348(1)(b), the authoritative texts of all Bills, Acts, Ordinances, Orders, Rules, and Regulations passed by Parliament or State Legislatures shall be in which language?",
            "stem_ta": "சரத்து 348(1)(b)-ன் படி, நாடாளுமன்றம் அல்லது மாநில சட்டமன்றங்களால் நிறைவேற்றப்படும் அனைத்து மசோதாக்கள், சட்டங்கள், அவசரச் சட்டங்கள், ஆணைகள் மற்றும் விதிகளின் அதிகாரப்பூர்வ மூல வாசகம் எந்த மொழியில் இருக்க வேண்டும்?",
            "options": [
                ("The English language", "ஆங்கில மொழி"),
                ("The Hindi language exclusively", "இந்தி மொழி மட்டுமே"),
                ("The official language of each State", "ஒவ்வொரு மாநிலத்தின் அதிகாரப்பூர்வ மொழி"),
                ("Both Hindi and Sanskrit", "இந்தி மற்றும் சமஸ்கிருதம் ஆகிய இரண்டும்")
            ],
            "correct_key": "A",
            "exp_en": "Article 348(1)(b) states that the authoritative texts of all Bills, Acts, Ordinances, Orders, Rules, Regulations, and Bye-laws at both Union and State levels shall be in the English language.",
            "exp_ta": "சரத்து 348(1)(b)-ன் படி, ஒன்றியம் மற்றும் மாநில அளவிலான அனைத்து மசோதாக்கள், சட்டங்கள், அவசரச் சட்டங்கள், ஆணைகள் மற்றும் விதிகளின் அதிகாரப்பூர்வ மூல வாசகம் ஆங்கில மொழியிலேயே இருக்க வேண்டும்.",
            "why_a_en": "Article 348(1)(b) makes English the authoritative reference text in case of conflict between translations.",
            "why_a_ta": "சரத்து 348(1)(b) மொழிபெயர்ப்புகளுக்கு இடையே முரண்பாடு ஏற்படும் பட்சத்தில் ஆங்கிலத்தை அதிகாரப்பூர்வ மூல ஆவணமாக ஆக்குகிறது.",
            "why_b_en": "Hindi is not the sole authoritative legal text prescribed by Article 348(1)(b).",
            "why_b_ta": "சரத்து 348(1)(b)-ல் இந்தி மட்டுமே அதிகாரப்பூர்வ சட்ட ஆவணமாகக் குறிப்பிடப்படவில்லை.",
            "why_c_en": "State official languages require an authoritative English translation published under Article 348(3).",
            "why_c_ta": "மாநில அதிகாரப்பூர்வ மொழிகளுக்கு சரத்து 348(3)-ன் கீழ் வெளியிடப்படும் அதிகாரப்பூர்வ ஆங்கில மொழிபெயர்ப்பு தேவைப்படுகிறது.",
            "why_d_en": "Sanskrit is not used for legislative enactment texts.",
            "why_d_ta": "சட்டமன்ற மசோதாக்களுக்கு சமஸ்கிருதம் பயன்படுத்தப்படுவதில்லை.",
            "tip_en": "If a State passes an Act in Tamil, its authoritative text in English must be published under Article 348(3).",
            "tip_ta": "ஒரு மாநிலம் தமிழில் ஒரு சட்டத்தை இயற்றினாலும், அதன் அதிகாரப்பூர்வ ஆங்கில வடிவம் சரத்து 348(3)-ன் கீழ் வெளியிடப்பட வேண்டும்.",
            "fact_en": "In case of conflict between English text and Hindi/vernacular text, the English text prevails in courts.",
            "fact_ta": "ஆங்கில வாசகத்திற்கும் இந்தி/வட்டார மொழி வாசகத்திற்கும் இடையே முரண்பாடு ஏற்பட்டால் நீதிமன்றங்களில் ஆங்கில வாசகமே மேலோங்கும்."
        },
        # 16
        {
            "subtopic": "High Court Language Authorization",
            "stem_en": "Under Article 348(2), who can authorize the use of Hindi or any other official language of a State in proceedings of the High Court of that State?",
            "stem_ta": "சரத்து 348(2)-ன் கீழ், ஒரு மாநில உயர் நீதிமன்ற நடவடிக்கைகளில் இந்தி அல்லது அம்மாநிலத்தின் பிற அதிகாரப்பூர்வ மொழியைப் பயன்படுத்த யார் அங்கீகரிக்க முடியும்?",
            "options": [
                ("The Governor of the State, with the previous consent of the President", "குடியரசுத் தலைவரின் முன் அனுமதியுடன் மாநில ஆளுநர்"),
                ("The Chief Justice of the High Court independently", "உயர் நீதிமன்றத் தலைமை நீதிபதி தன்னிச்சையாக"),
                ("The State Legislative Assembly by a two-thirds majority", "மூன்றில் இரண்டு பங்கு பெரும்பான்மையுடன் மாநில சட்டமன்றப் பேரவை"),
                ("The Union Law Minister directly", "ஒன்றிய சட்ட அமைச்சர் நேரடியாக")
            ],
            "correct_key": "A",
            "exp_en": "Article 348(2) provides that the Governor of a State may, with the previous consent of the President, authorize the use of Hindi or any other official language of the State in proceedings of the High Court.",
            "exp_ta": "சரத்து 348(2)-ன் படி, மாநில ஆளுநர் குடியரசுத் தலைவரின் முன் அனுமதியுடன், உயர் நீதிமன்ற நடவடிக்கைகளில் இந்தி அல்லது மாநிலத்தின் பிற அதிகாரப்பூர்வ மொழியைப் பயன்படுத்த அங்கீகரிக்கலாம்.",
            "why_a_en": "Article 348(2) explicitly requires Governor's authorization with President's previous consent.",
            "why_a_ta": "சரத்து 348(2) வெளிப்படையாகக் குடியரசுத் தலைவரின் முன் அனுமதியுடன் ஆளுநரின் அங்கீகாரத்தைக் கோருகிறது.",
            "why_b_en": "The Chief Justice of the High Court cannot unilaterally authorize language of proceedings.",
            "why_b_ta": "உயர் நீதிமன்றத் தலைமை நீதிபதி தன்னிச்சையாக நடவடிக்கைகளின் மொழியை அங்கீகரிக்க முடியாது.",
            "why_c_en": "The State Legislature cannot bypass the constitutional requirement of Presidential consent.",
            "why_c_ta": "மாநில சட்டமன்றம் குடியரசுத் தலைவரின் முன் அனுமதி என்ற அரசியலமைப்பு நிபந்தனையைத் தவிர்க்க முடியாது.",
            "why_d_en": "The Union Law Minister has no constitutional role under Article 348(2).",
            "why_d_ta": "சரத்து 348(2)-ன் கீழ் ஒன்றிய சட்ட அமைச்சருக்கு அரசியலமைப்பு ரீதியான பங்கு எதுவும் இல்லை.",
            "tip_en": "High Court Language: Governor + Previous Consent of President (Article 348(2)).",
            "tip_ta": "உயர் நீதிமன்ற மொழி: ஆளுநர் + குடியரசுத் தலைவரின் முன் அனுமதி (சரத்து 348(2)).",
            "fact_en": "Bihar, UP, MP, and Rajasthan have authorized Hindi in their High Courts under this provision.",
            "fact_ta": "பீகார், உ.பி, ம.பி மற்றும் ராஜஸ்தான் ஆகிய மாநிலங்கள் இந்த விதியின் கீழ் தங்கள் உயர் நீதிமன்றங்களில் இந்தியை அனுமதித்துள்ளன."
        },
        # 17
        {
            "subtopic": "Limitation on High Court Language Authorization",
            "stem_en": "Even if the Governor authorizes Hindi or a State official language in High Court proceedings under Article 348(2), what must still be in the English language?",
            "stem_ta": "சரத்து 348(2)-ன் கீழ் உயர் நீதிமன்ற நடவடிக்கைகளில் இந்தி அல்லது மாநில மொழியை ஆளுநர் அனுமதித்தாலும், பின்வருவனவற்றில் எது கட்டாயமாக ஆங்கில மொழியிலேயே இருக்க வேண்டும்?",
            "options": [
                ("Judgments, decrees, or orders passed by the High Court", "உயர் நீதிமன்றம் பிறப்பிக்கும் தீர்ப்புகள், ஆணைகள் அல்லது கட்டளைகள்"),
                ("Oral arguments of advocates", "வழக்கறிஞர்களின் வாய்மொழி வாதங்கள்"),
                ("Petitions filed by litigants", "மனுதாரர்களால் தாக்கல் செய்யப்படும் மனுக்கள்"),
                ("Affidavits submitted in court", "நீதிமன்றத்தில் சமர்ப்பிக்கப்படும் பிரமாணப் பத்திரங்கள்")
            ],
            "correct_key": "A",
            "exp_en": "The proviso to Article 348(2) states that nothing in that clause shall apply to any judgment, decree, or order passed or made by such High Court, which MUST be in English.",
            "exp_ta": "சரத்து 348(2)-ன் விதிவிலக்கின் படி, உயர் நீதிமன்றம் பிறப்பிக்கும் எந்தவொரு தீர்ப்பு, ஆணை அல்லது கட்டளைக்கு இது பொருந்தாது; அவை கட்டாயமாக ஆங்கிலத்திலேயே இருக்க வேண்டும்.",
            "why_a_en": "The proviso to Article 348(2) strictly prohibits non-English judgments and decrees unless an English translation accompanies them under statutory provision.",
            "why_a_ta": "சரத்து 348(2) விதிவிலக்கு ஆங்கிலம் அல்லாத தீர்ப்புகள் மற்றும் கட்டளைகளைத் திட்டவட்டமாகத் தடுக்கிறது.",
            "why_b_en": "Oral arguments can be in the authorized language.",
            "why_b_ta": "வாய்மொழி வாதங்கள் அங்கீகரிக்கப்பட்ட மொழியில் இருக்கலாம்.",
            "why_c_en": "Petitions can be submitted in the authorized language.",
            "why_c_ta": "மனுக்கள் அங்கீகரிக்கப்பட்ட மொழியில் சமர்ப்பிக்கப்படலாம்.",
            "why_d_en": "Affidavits can be submitted in the authorized language.",
            "why_d_ta": "பிரமாணப் பத்திரங்கள் அங்கீகரிக்கப்பட்ட மொழியில் சமர்ப்பிக்கப்படலாம்.",
            "tip_en": "Proceedings can be in regional language; Judgments/Decrees MUST be in English (Article 348(2) proviso).",
            "tip_ta": "நடவடிக்கைகள் வட்டார மொழியில் இருக்கலாம்; ஆனால் தீர்ப்புகள்/ஆணைகள் ஆங்கிலத்திலேயே இருக்க வேண்டும்.",
            "fact_en": "Section 7 of the Official Languages Act, 1963 permitted judgments in Hindi provided an English translation is published.",
            "fact_ta": "அதிகாரப்பூர்வ மொழிகள் சட்டம் 1963-ன் பிரிவு 7, ஆங்கில மொழிபெயர்ப்பு வழங்கப்படும் பட்சத்தில் இந்தியில் தீர்ப்புகளை அனுமதிக்கிறது."
        },
        # 18
        {
            "subtopic": "Special Procedure for Language Legislation",
            "stem_en": "Under Article 349, whose previous sanction is required for introducing any Bill or amendment in Parliament providing for the language to be used in the Supreme Court, High Courts, or official purposes during the 15-year transition period?",
            "stem_ta": "15 ஆண்டு இடைக்காலத்தில் உச்ச நீதிமன்றம், உயர் நீதிமன்றங்கள் அல்லது அதிகாரப்பூர்வ பணிகளுக்கான மொழியை ஒழுங்குபடுத்தும் மசோதாவை நாடாளுமன்றத்தில் அறிமுகப்படுத்த யாருடைய முன் அனுமதி தேவை என சரத்து 349 கூறுகிறது?",
            "options": [
                ("The President of India", "இந்தியக் குடியரசுத் தலைவர்"),
                ("The Chief Justice of India", "இந்தியத் தலைமை நீதிபதி"),
                ("The Speaker of Lok Sabha", "மக்களவைத் தலைவர்"),
                ("The Chairman of Rajya Sabha", "மாநிலங்களவைத் தலைவர்")
            ],
            "correct_key": "A",
            "exp_en": "Article 349 required the previous sanction of the President before introducing any language Bill during the 15-year period, and the President could give sanction only after considering the recommendations of the Commission and Committee under Article 344.",
            "exp_ta": "சரத்து 349-ன் கீழ் 15 ஆண்டு காலத்தில் எந்தவொரு மொழி மசோதாவையும் அறிமுகப்படுத்துவதற்கு முன் குடியரசுத் தலைவரின் முன் அனுமதி அவசியமாகும், மேலும் சரத்து 344 ஆணையம் மற்றும் குழுவின் பரிந்துரைகளை பரிசீலித்த பிறகே குடியரசுத் தலைவர் அனுமதி அளிக்க முடியும்.",
            "why_a_en": "Article 349 explicitly makes the President's previous sanction mandatory.",
            "why_a_ta": "சரத்து 349 வெளிப்படையாகக் குடியரசுத் தலைவரின் முன் அனுமதியைக் கட்டாயமாக்குகிறது.",
            "why_b_en": "The Chief Justice of India is not the sanctioning authority for legislative introductions.",
            "why_b_ta": "சட்ட மசோதா அறிமுகங்களுக்கு இந்தியத் தலைமை நீதிபதி அனுமதி அளிக்கும் அதிகாரம் கொண்டவர் அல்ல.",
            "why_c_en": "The Speaker decides on admissibility in Lok Sabha but does not give constitutional sanction.",
            "why_c_ta": "மக்களவைத் தலைவர் மக்களவையில் மசோதா ஏற்புத்தன்மையை தீர்மானிக்கிறார், அரசியலமைப்பு முன் அனுமதியை வழங்குவதில்லை.",
            "why_d_en": "The Chairman of Rajya Sabha does not possess this constitutional sanctioning power.",
            "why_d_ta": "மாநிலங்களவைத் தலைவருக்கு இந்த அரசியலமைப்பு முன் அனுமதி அதிகாரம் இல்லை.",
            "tip_en": "Article 349 applied during the 15-year period (1950-1965) to protect language consensus.",
            "tip_ta": "சரத்து 349 மொழி ஒருமித்த கருத்தைப் பாதுகாக்க 15 ஆண்டு காலத்தில் (1950-1965) பயன்படுத்தப்பட்டது.",
            "fact_en": "The Official Languages Bill, 1963 was introduced with the prior recommendation of President Dr. S. Radhakrishnan.",
            "fact_ta": "அதிகாரப்பூர்வ மொழிகள் மசோதா, 1963 குடியரசுத் தலைவர் டாக்டர் எஸ். ராதாகிருஷ்ணனின் முன் பரிந்துரையுடன் அறிமுகப்படுத்தப்பட்டது."
        },
        # 19
        {
            "subtopic": "Redress of Grievances Language",
            "stem_en": "According to Article 350, every person is entitled to submit a representation for the redress of any grievance to any officer or authority of the Union or a State in which language?",
            "stem_ta": "சரத்து 350-ன் படி, எந்தவொரு நபரும் தனது குறைகளைத் தீர்ப்பதற்காக ஒன்றியம் அல்லது மாநிலத்தின் எந்தவொரு அலுவலர் அல்லது அதிகாரியிடம் எந்த மொழியில் மனு அளிக்க உரிமை பெற்றுள்ளார்?",
            "options": [
                ("In any of the languages used in the Union or in the State", "ஒன்றியம் அல்லது மாநிலத்தில் பயன்பாட்டில் உள்ள எந்தவொரு மொழியிலும்"),
                ("In the official language of the Union only", "ஒன்றியத்தின் அதிகாரப்பூர்வ மொழியில் மட்டுமே"),
                ("In Hindi or English exclusively", "இந்தி அல்லது ஆங்கிலத்தில் மட்டுமே"),
                ("Only in the Eighth Schedule languages", "எட்டாவது அட்டவணை மொழிகளில் மட்டுமே")
            ],
            "correct_key": "A",
            "exp_en": "Article 350 provides that every person shall be entitled to submit a representation for the redress of any grievance to any officer or authority of the Union or a State in any of the languages used in the Union or in the State, as the case may be.",
            "exp_ta": "சரத்து 350-ன் படி, எந்தவொரு நபரும் தனது குறைகளைத் தீர்ப்பதற்கு ஒன்றியம் அல்லது மாநிலத்தில் பயன்பாட்டில் உள்ள எந்தவொரு மொழியிலும் மனு அளிக்க உரிமை உண்டு, அம்மனு அதிகாரப்பூர்வ மொழியில் இல்லை என்ற காரணத்திற்காக நிராகரிக்கப்படக் கூடாது.",
            "why_a_en": "Article 350 guarantees the democratic right of citizens to petition in any language used in the Union or State.",
            "why_a_ta": "சரத்து 350 குடிமக்கள் ஒன்றியம் அல்லது மாநிலத்தில் புழக்கத்தில் உள்ள எந்த மொழியிலும் மனு அளிக்கும் ஜனநாயக உரிமையை உறுதி செய்கிறது.",
            "why_b_en": "The citizen is not restricted to the Union official language under Article 350.",
            "why_b_ta": "சரத்து 350-ன் கீழ் குடிமக்கள் ஒன்றியத்தின் அதிகாரப்பூர்வ மொழிக்கு மட்டுமே கட்டுப்பட்டவர்கள் அல்ல.",
            "why_c_en": "A petition cannot be rejected solely because it is not in Hindi or English.",
            "why_c_ta": "இந்தி அல்லது ஆங்கிலத்தில் இல்லை என்பதற்காக மட்டுமே ஒரு மனுவை நிராகரிக்க முடியாது.",
            "why_d_en": "The protection extends to languages used in the State even if not listed in the Eighth Schedule.",
            "why_d_ta": "எட்டாவது அட்டவணையில் பட்டியலிடப்படாவிட்டாலும் மாநிலத்தில் பயன்பாட்டில் உள்ள மொழிகளுக்கும் இப் பாதுகாப்பு நீட்டிக்கப்படுகிறது.",
            "tip_en": "Article 350 is a citizen-centric grievance redressal right with zero language barriers.",
            "tip_ta": "சரத்து 350 என்பது எந்தவொரு மொழித் தடையும் இல்லாத குடிமக்களை மையமாகக் கொண்ட குறைதீர்க்கும் உரிமையாகும்.",
            "fact_en": "A representation under Article 350 cannot be rejected on the ground that it is in an unrecognized dialect.",
            "fact_ta": "சரத்து 350-ன் கீழான மனு அங்கீகரிக்கப்படாத வட்டார வழக்கில் உள்ளது என்ற அடிப்படையில் நிராகரிக்கப்பட முடியாது."
        },
        # 20
        {
            "subtopic": "Mother Tongue at Primary Stage",
            "stem_en": "Which constitutional amendment inserted Article 350A, providing facilities for instruction in mother tongue at the primary stage of education to children belonging to linguistic minority groups?",
            "stem_ta": "மொழிச் சிறுபான்மைப் பிரிவு குழந்தைகளுக்குத் தொடக்கக் கல்வி நிலையில் தாய்மொழியில் கற்பிப்பதற்கான வசதிகளை வழங்கும் சரத்து 350A-வை இணைத்த அரசியலமைப்புத் திருத்தம் எது?",
            "options": [
                ("7th Constitutional Amendment Act, 1956", "7-வது அரசியலமைப்புத் திருத்தச் சட்டம், 1956"),
                ("42nd Constitutional Amendment Act, 1976", "42-வது அரசியலமைப்புத் திருத்தச் சட்டம், 1976"),
                ("44th Constitutional Amendment Act, 1978", "44-வது அரசியலமைப்புத் திருத்தச் சட்டம், 1978"),
                ("1st Constitutional Amendment Act, 1951", "1-வது அரசியலமைப்புத் திருத்தச் சட்டம், 1951")
            ],
            "correct_key": "A",
            "exp_en": "Article 350A was inserted by the 7th Constitutional Amendment Act, 1956 on the recommendation of the States Reorganisation Commission (Fazl Ali Commission).",
            "exp_ta": "மாநில மறுசீரமைப்பு ஆணையத்தின் (பசல் அலி ஆணையம்) பரிந்துரையின் பேரில், 1956-ன் 7-வது அரசியலமைப்புத் திருத்தச் சட்டத்தின் மூலம் சரத்து 350A சேர்க்கப்பட்டது.",
            "why_a_en": "The 7th CAA, 1956 reorganized States on linguistic lines and inserted Article 350A and Article 350B as minority safeguards.",
            "why_a_ta": "7-வது திருத்தச் சட்டம், 1956 மொழிவாரி மாநிலங்களை அமைத்து, சிறுபான்மையினர் பாதுகாப்பிற்காக சரத்துகள் 350A மற்றும் 350B-ஐ இணைத்தது.",
            "why_b_en": "The 42nd CAA, 1976 added Fundamental Duties and amended the Preamble, not Article 350A.",
            "why_b_ta": "42-வது திருத்தச் சட்டம், 1976 அடிப்படைக் கடமைகளைச் சேர்த்தது, சரத்து 350A-வை அல்ல.",
            "why_c_en": "The 44th CAA, 1978 restored civil liberties after Emergency.",
            "why_c_ta": "44-வது திருத்தச் சட்டம், 1978 அவசரகால நிலைக்குப் பிந்தைய குடிமை உரிமைகளை மீட்டெடுத்தது.",
            "why_d_en": "The 1st CAA, 1951 created the Ninth Schedule and Article 31A/31B.",
            "why_d_ta": "1-வது திருத்தச் சட்டம், 1951 ஒன்பதாவது அட்டவணை மற்றும் சரத்து 31A/31B-ஐ உருவாக்கியது.",
            "tip_en": "7th CAA 1956 added twin safeguards: Article 350A (Primary Mother Tongue) + Article 350B (Special Officer).",
            "tip_ta": "7-வது சட்டத்திருத்தம் 1956 இரட்டைப் பாதுகாப்புகளைச் சேர்த்தது: சரத்து 350A (தொடக்க தாய்மொழி) + சரத்து 350B (சிறப்பு அலுவலர்).",
            "fact_en": "The President can issue directives to any State under Article 350A to secure provision of such facilities.",
            "fact_ta": "சரத்து 350A-ன் கீழ் இத்தகைய வசதிகளை வழங்குவதை உறுதி செய்ய குடியரசுத் தலைவர் எந்தவொரு மாநிலத்திற்கும் உத்தரவுகளைப் பிறப்பிக்கலாம்."
        },
        # 21
        {
            "subtopic": "Special Officer for Linguistic Minorities",
            "stem_en": "Under Article 350B of the Constitution of India, who appoints the Special Officer for Linguistic Minorities?",
            "stem_ta": "இந்திய அரசியலமைப்பின் சரத்து 350B-ன் கீழ், மொழிச் சிறுபான்மையினருக்கான சிறப்பு அலுவலரை நியமிப்பவர் யார்?",
            "options": [
                ("The President of India", "இந்தியக் குடியரசுத் தலைவர்"),
                ("The Prime Minister of India", "இந்தியப் பிரதமர்"),
                ("The Union Minister of Minority Affairs", "ஒன்றிய சிறுபான்மையினர் விவகார அமைச்சர்"),
                ("The Chief Justice of India", "இந்தியத் தலைமை நீதிபதி")
            ],
            "correct_key": "A",
            "exp_en": "Article 350B(1) provides that there shall be a Special Officer for linguistic minorities to be appointed by the President.",
            "exp_ta": "சரத்து 350B(1)-ன் படி, மொழிச் சிறுபான்மையினருக்கான ஒரு சிறப்பு அலுவலர் இருக்க வேண்டும், அவர் குடியரசுத் தலைவரால் நியமிக்கப்படுவார்.",
            "why_a_en": "Article 350B(1) explicitly states that the Special Officer is appointed by the President.",
            "why_a_ta": "சரத்து 350B(1) சிறப்பு அலுவலர் குடியரசுத் தலைவரால் நியமிக்கப்படுவார் என்று தெளிவாகக் கூறுகிறது.",
            "why_b_en": "The Prime Minister heads the executive but does not constitutionally appoint the Special Officer.",
            "why_b_ta": "பிரதமர் நிர்வாகத் தலைவர், ஆனால் அரசியலமைப்பு ரீதியாக சிறப்பு அலுவலரை நியமிப்பவர் அல்ல.",
            "why_c_en": "The Minister of Minority Affairs oversees the administrative ministry, but appointment is by the President.",
            "why_c_ta": "சிறுபான்மையினர் விவகார அமைச்சர் நிர்வாக அமைச்சகத்தைக் கண்காணிக்கிறார், ஆனால் நியமனம் குடியரசுத் தலைவரால் செய்யப்படுகிறது.",
            "why_d_en": "The Chief Justice of India has no role in appointing the Special Officer.",
            "why_d_ta": "சிறப்பு அலுவலரை நியமிப்பதில் இந்தியத் தலைமை நீதிபதிக்கு எந்தப் பங்கும் இல்லை.",
            "tip_en": "Designation: Commissioner for Linguistic Minorities (CLM). Headquarters: Prayagraj (Allahabad).",
            "tip_ta": "பதவிப் பெயர்: மொழிச் சிறுபான்மையினருக்கான ஆணையர் (CLM). தலைமையிடம்: பிரயாக்ராஜ் (அலகாபாத்).",
            "fact_en": "Article 350B was inserted by the 7th Constitutional Amendment Act, 1956.",
            "fact_ta": "சரத்து 350B 1956-ன் 7-வது அரசியலமைப்புத் திருத்தச் சட்டத்தின் மூலம் சேர்க்கப்பட்டது."
        },
        # 22
        {
            "subtopic": "Reporting by Special Officer for Linguistic Minorities",
            "stem_en": "To whom does the Special Officer for Linguistic Minorities submit reports on the safeguards provided for linguistic minorities under Article 350B(2)?",
            "stem_ta": "சரத்து 350B(2)-ன் கீழ் மொழிச் சிறுபான்மையினருக்காக வழங்கப்பட்டுள்ள பாதுகாப்புகள் குறித்த தனது அறிக்கைகளை மொழிச் சிறுபான்மையினருக்கான சிறப்பு அலுவலர் யாரிடம் சமர்ப்பிக்கிறார்?",
            "options": [
                ("The President of India", "இந்தியக் குடியரசுத் தலைவர்"),
                ("The Speaker of Lok Sabha directly", "மக்களவைத் தலைவரிடம் நேரடியாக"),
                ("The Union Home Minister", "ஒன்றிய உள்துறை அமைச்சர்"),
                ("The Supreme Court of India", "இந்திய உச்ச நீதிமன்றம்")
            ],
            "correct_key": "A",
            "exp_en": "Article 350B(2) mandates that the Special Officer shall report to the President, and the President shall cause all such reports to be laid before each House of Parliament and sent to the Governments of the States concerned.",
            "exp_ta": "சரத்து 350B(2)-ன் படி சிறப்பு அலுவலர் குடியரசுத் தலைவரிடம் அறிக்கை சமர்ப்பிக்க வேண்டும், குடியரசுத் தலைவர் அவ்வறிக்கைகளை நாடாளுமன்றத்தின் இரு அவைகளிலும் வைக்கச் செய்வார் மற்றும் சம்பந்தப்பட்ட மாநில அரசுகளுக்கும் அனுப்புவார்.",
            "why_a_en": "Article 350B(2) mandates reporting directly to the President, who then places it before Parliament and States.",
            "why_a_ta": "சரத்து 350B(2) நேரடியாகக் குடியரசுத் தலைவரிடம் அறிக்கை சமர்ப்பிப்பதைக் கட்டாயமாக்குகிறது.",
            "why_b_en": "The report is not submitted directly to the Speaker; it is laid by the President.",
            "why_b_ta": "அறிக்கை நேரடியாக மக்களவைத் தலைவரிடம் சமர்ப்பிக்கப்படுவதில்லை; அது குடியரசுத் தலைவரால் வைக்கப்படுகிறது.",
            "why_c_en": "The Home Minister does not receive the constitutional report directly.",
            "why_c_ta": "உள்துறை அமைச்சர் அரசியலமைப்பு அறிக்கையை நேரடியாகப் பெறுவதில்லை.",
            "why_d_en": "The Supreme Court is not an executive reporting authority under Part XVII.",
            "why_d_ta": "உச்ச நீதிமன்றம் பகுதி XVII-ன் கீழ் அறிக்கை பெறும் அதிகாரம் கொண்ட அமைப்பு அல்ல.",
            "tip_en": "Flow: Commissioner -> President -> Parliament & State Governments.",
            "tip_ta": "படிநிலை: ஆணையர் -> குடியரசுத் தலைவர் -> நாடாளுமன்றம் மற்றும் மாநில அரசுகள்.",
            "fact_en": "The Commissioner operates under the Ministry of Minority Affairs (earlier Ministry of Home Affairs / Social Justice).",
            "fact_ta": "ஆணையர் சிறுபான்மையினர் விவகார அமைச்சகத்தின் கீழ் செயல்படுகிறார் (முன்பு உள்துறை அமைச்சகம் / சமூக நீதி அமைச்சகம்)."
        },
        # 23
        {
            "subtopic": "Directive for Development of Hindi",
            "stem_en": "Which Article of the Constitution of India contains a directive that it shall be the duty of the Union to promote the spread of the Hindi language and to develop it?",
            "stem_ta": "இந்தி மொழியின் பரவலை மேம்படுத்துவதும், அதனை வளர்ப்பதும் ஒன்றியத்தின் கடமை என்ற வழிகாட்டுதலைக் கொண்டுள்ள இந்திய அரசியலமைப்பின் சரத்து எது?",
            "options": [
                ("Article 351", "சரத்து 351"),
                ("Article 343", "சரத்து 343"),
                ("Article 344", "சரத்து 344"),
                ("Article 350A", "சரத்து 350A")
            ],
            "correct_key": "A",
            "exp_en": "Article 351 states that it shall be the duty of the Union to promote the spread of the Hindi language, to develop it so that it may serve as a medium of expression for all elements of the composite culture of India.",
            "exp_ta": "சரத்து 351-ன் படி, இந்தியாவின் கூட்டுப் பண்பாட்டின் அனைத்துக் கூறுகளையும் வெளிப்படுத்தும் ஊடகமாகத் திகழும் வகையில் இந்தி மொழியின் பரவலை ஊக்குவிப்பதும் அதனை வளர்ப்பதும் ஒன்றியத்தின் கடமையாகும்.",
            "why_a_en": "Article 351 is the concluding article of Part XVII containing the directive for development of Hindi.",
            "why_a_ta": "சரத்து 351 பகுதி XVII-ன் இறுதிச் சரத்தாகும், இது இந்தி வளர்ச்சிக்கான வழிகாட்டுதலைக் கொண்டுள்ளது.",
            "why_b_en": "Article 343 defines the official language of the Union, not the development directive.",
            "why_b_ta": "சரத்து 343 ஒன்றியத்தின் அதிகாரப்பூர்வ மொழியை வரையறுக்கிறது, வளர்ச்சி வழிகாட்டுதலை அல்ல.",
            "why_c_en": "Article 344 deals with the Commission and Committee on Official Language.",
            "why_c_ta": "சரத்து 344 அதிகாரப்பூர்வ மொழிக்கான ஆணையம் மற்றும் குழுவைக் கையாள்கிறது.",
            "why_d_en": "Article 350A deals with primary education in mother tongue.",
            "why_d_ta": "சரத்து 350A தாய்மொழியில் தொடக்கக் கல்வியைக் கையாள்கிறது.",
            "tip_en": "Article 351: Vocabulary to be drawn primarily on Sanskrit and secondarily on other languages.",
            "tip_ta": "சரத்து 351: சொல்லகராதி முதன்மையாக சமஸ்கிருதத்திலிருந்தும், இரண்டாவதாக பிற மொழிகளிலிருந்தும் பெறப்பட வேண்டும்.",
            "fact_en": "Article 351 directives are non-justiciable like Directive Principles of State Policy.",
            "fact_ta": "சரத்து 351 வழிகாட்டுதல்கள் அரசு வழிகாட்டு நெறிமுறைகளைப் போல நீதிமன்றங்களால் கட்டாயப்படுத்த முடியாதவை."
        },
        # 24
        {
            "subtopic": "Source of Vocabulary under Article 351",
            "stem_en": "According to Article 351, from which language should Hindi primarily draw its vocabulary for its enrichment?",
            "stem_ta": "சரத்து 351-ன் படி, இந்தி மொழி தனது செறிவூட்டலுக்காக முதன்மையாக எந்த மொழியிலிருந்து சொற்களைப் பெற வேண்டும்?",
            "options": [
                ("Sanskrit", "சமஸ்கிருதம்"),
                ("Persian", "பாரசீகம்"),
                ("Arabic", "அரபு"),
                ("English", "ஆங்கிலம்")
            ],
            "correct_key": "A",
            "exp_en": "Article 351 specifies that Hindi should secure the enrichment of its vocabulary by drawing primarily on Sanskrit and secondarily on other languages specified in the Eighth Schedule.",
            "exp_ta": "சரத்து 351-ன் படி, இந்தி தனது சொல்லகராதியை முதன்மையாக சமஸ்கிருதத்திலிருந்தும், இரண்டாவதாக எட்டாவது அட்டவணையில் குறிப்பிடப்பட்டுள்ள பிற மொழிகளிலிருந்தும் பெற்று வளப்படுத்திக் கொள்ள வேண்டும்.",
            "why_a_en": "Article 351 explicitly names Sanskrit as the primary source of vocabulary.",
            "why_a_ta": "சரத்து 351 வெளிப்படையாக சமஸ்கிருதத்தை சொல்லகராதிக்கான முதன்மை ஆதாரமாகக் குறிப்பிடுகிறது.",
            "why_b_en": "Persian is not named as a primary source in Article 351.",
            "why_b_ta": "சரத்து 351-ல் பாரசீகம் முதன்மை ஆதாரமாகக் குறிப்பிடப்படவில்லை.",
            "why_c_en": "Arabic is not specified as a source language in Article 351.",
            "why_c_ta": "அரபு மொழி சரத்து 351-ல் மூல மொழியாகக் குறிப்பிடப்படவில்லை.",
            "why_d_en": "English is not the designated vocabulary source under Article 351.",
            "why_d_ta": "ஆங்கிலம் சரத்து 351-ன் கீழ் சொல்லகராதி ஆதாரமாக நியமிக்கப்படவில்லை.",
            "tip_en": "Article 351 Vocabulary Formula: Primarily = SANSKRIT; Secondarily = Other Eighth Schedule Languages.",
            "tip_ta": "சரத்து 351 சொற்களஞ்சிய சூத்திரம்: முதன்மையாக = சமஸ்கிருதம்; இரண்டாவதாக = பிற எட்டாவது அட்டவணை மொழிகள்.",
            "fact_en": "The secondarily drawn languages include Tamil, Telugu, Kannada, Bengali, and others in the 8th Schedule.",
            "fact_ta": "இரண்டாவதாகப் பெறப்படும் மொழிகளில் தமிழ், தெலுங்கு, கன்னடம், பெங்காலி மற்றும் எட்டாவது அட்டவணையின் பிற மொழிகள் அடங்கும்."
        },
        # 25
        {
            "subtopic": "Eighth Schedule Original Count",
            "stem_en": "How many languages were originally included in the Eighth Schedule of the Constitution of India in 1950?",
            "stem_ta": "1950-ல் இந்திய அரசியலமைப்பின் எட்டாவது அட்டவணையில் தொடக்கத்தில் எத்தனை மொழிகள் சேர்க்கப்பட்டிருந்தன?",
            "options": [
                ("14 languages", "14 மொழிகள்"),
                ("15 languages", "15 மொழிகள்"),
                ("18 languages", "18 மொழிகள்"),
                ("22 languages", "22 மொழிகள்")
            ],
            "correct_key": "A",
            "exp_en": "At the commencement of the Constitution in 1950, the Eighth Schedule contained 14 languages: Assamese, Bengali, Gujarati, Hindi, Kannada, Kashmiri, Malayalam, Marathi, Odia, Punjabi, Sanskrit, Tamil, Telugu, and Urdu.",
            "exp_ta": "1950-ல் அரசியலமைப்பு அமலுக்கு வந்தபோது, எட்டாவது அட்டவணையில் 14 மொழிகள் இருந்தன: அசாமி, பெங்காலி, குஜராத்தி, இந்தி, கன்னடம், காஷ்மீரி, மலையாளம், மராத்தி, ஒடியா, பஞ்சாபி, சமஸ்கிருதம், தமிழ், தெலுங்கு மற்றும் உருது.",
            "why_a_en": "Original Eighth Schedule = 14 languages in 1950.",
            "why_a_ta": "1950-ல் தொடக்க எட்டாவது அட்டவணை = 14 மொழிகள்.",
            "why_b_en": "15 languages was the count after Sindhi was added by 21st CAA in 1967.",
            "why_b_ta": "1967-ல் 21-வது திருத்தச் சட்டம் மூலம் சிந்தி சேர்க்கப்பட்ட பிறகு எண்ணிக்கை 15 ஆனது.",
            "why_c_en": "18 languages was the count after 71st CAA added Konkani, Manipuri, and Nepali in 1992.",
            "why_c_ta": "1992-ல் 71-வது திருத்தச் சட்டம் மூலம் கொங்கணி, மணிப்பூரி, நேபாளி சேர்க்கப்பட்ட பிறகு எண்ணிக்கை 18 ஆனது.",
            "why_d_en": "22 languages is the present count after 92nd CAA in 2003.",
            "why_d_ta": "2003-ல் 92-வது திருத்தச் சட்டம் மூலம் 4 மொழிகள் சேர்க்கப்பட்ட பிறகு தற்போதைய எண்ணிக்கை 22 ஆகும்.",
            "tip_en": "8th Schedule Progression: 14 (1950) -> +1 (1967) -> +3 (1992) -> +4 (2003) = 22 languages.",
            "tip_ta": "8-வது அட்டவணை வளர்ச்சி: 14 (1950) -> +1 (1967) -> +3 (1992) -> +4 (2003) = 22 மொழிகள்.",
            "fact_en": "Articles 344(1) and 351 refer directly to the Eighth Schedule.",
            "fact_ta": "சரத்துகள் 344(1) மற்றும் 351 ஆகியவை நேரடியாக எட்டாவது அட்டவணையைக் குறிப்பிடுகின்றன."
        },
        # 26
        {
            "subtopic": "21st Amendment Act, 1967",
            "stem_en": "Which language was added to the Eighth Schedule by the 21st Constitutional Amendment Act, 1967?",
            "stem_ta": "1967-ன் 21-வது அரசியலமைப்புத் திருத்தச் சட்டத்தின் மூலம் எட்டாவது அட்டவணையில் சேர்க்கப்பட்ட மொழி எது?",
            "options": [
                ("Sindhi", "சிந்தி"),
                ("Konkani", "கொங்கணி"),
                ("Manipuri", "மணிப்பூரி"),
                ("Nepali", "நேபாளி")
            ],
            "correct_key": "A",
            "exp_en": "Sindhi was added to the Eighth Schedule as the 15th language by the 21st Constitutional Amendment Act in 1967.",
            "exp_ta": "1967-ன் 21-வது அரசியலமைப்புத் திருத்தச் சட்டம் மூலம் சிந்தி மொழி 15-வது மொழியாக எட்டாவது அட்டவணையில் சேர்க்கப்பட்டது.",
            "why_a_en": "The 21st CAA, 1967 exclusively added Sindhi to the Eighth Schedule.",
            "why_a_ta": "21-வது சட்டத்திருத்தம், 1967 சிந்தி மொழியை மட்டுமே எட்டாவது அட்டவணையில் சேர்த்தது.",
            "why_b_en": "Konkani was added 25 years later by the 71st CAA in 1992.",
            "why_b_ta": "கொங்கணி 25 ஆண்டுகளுக்குப் பிறகு 1992-ல் 71-வது திருத்தச் சட்டம் மூலம் சேர்க்கப்பட்டது.",
            "why_c_en": "Manipuri was added by the 71st CAA in 1992.",
            "why_c_ta": "மணிப்பூரி 1992-ல் 71-வது திருத்தச் சட்டம் மூலம் சேர்க்கப்பட்டது.",
            "why_d_en": "Nepali was added by the 71st CAA in 1992.",
            "why_d_ta": "நேபாளி 1992-ல் 71-வது திருத்தச் சட்டம் மூலம் சேர்க்கப்பட்டது.",
            "tip_en": "21st CAA (1967) = Sindhi (15th language).",
            "tip_ta": "21-வது சட்டத்திருத்தம் (1967) = சிந்தி (15-வது மொழி).",
            "fact_en": "Sindhi is unique as an Eighth Schedule language without being the official language of any specific State.",
            "fact_ta": "சிந்தி மொழி எந்தவொரு குறிப்பிட்ட மாநிலத்தின் அதிகாரப்பூர்வ மொழியாகவும் இல்லாமல் எட்டாவது அட்டவணையில் உள்ள தனித்துவமான மொழியாகும்."
        },
        # 27
        {
            "subtopic": "71st Amendment Act, 1992",
            "stem_en": "Which three languages were added to the Eighth Schedule by the 71st Constitutional Amendment Act, 1992?",
            "stem_ta": "1992-ன் 71-வது அரசியலமைப்புத் திருத்தச் சட்டத்தின் மூலம் எட்டாவது அட்டவணையில் சேர்க்கப்பட்ட மூன்று மொழிகள் எவை?",
            "options": [
                ("Konkani, Manipuri, and Nepali", "கொங்கணி, மணிப்பூரி மற்றும் நேபாளி"),
                ("Bodo, Dogri, and Maithili", "போடோ, டோக்ரி மற்றும் மைதிலி"),
                ("Sindhi, Santhali, and Dogri", "சிந்தி, சந்தாலி மற்றும் டோக்ரி"),
                ("Manipuri, Bodo, and Santhali", "மணிப்பூரி, போடோ மற்றும் சந்தாலி")
            ],
            "correct_key": "A",
            "exp_en": "The 71st Constitutional Amendment Act, 1992 added Konkani, Manipuri, and Nepali to the Eighth Schedule, raising the total count to 18.",
            "exp_ta": "1992-ன் 71-வது அரசியலமைப்புத் திருத்தச் சட்டம் கொங்கணி, மணிப்பூரி மற்றும் நேபாளி ஆகிய மொழிகளை எட்டாவது அட்டவணையில் சேர்த்தது, இதன் மூலம் மொத்த எண்ணிக்கை 18 ஆக உயர்ந்தது.",
            "why_a_en": "Mnemonic 'KMN' (Konkani, Manipuri, Nepali) represents the 71st Amendment additions.",
            "why_a_ta": "'KMN' (கொங்கணி, மணிப்பூரி, நேபாளி) என்ற நினைவுக்குறிப்பு 71-வது திருத்தச் சேர்க்கைகளைக் குறிக்கிறது.",
            "why_b_en": "Bodo, Dogri, and Maithili were added later by the 92nd CAA, 2003.",
            "why_b_ta": "போடோ, டோக்ரி மற்றும் மைதிலி ஆகியவை பின்னர் 2003-ன் 92-வது திருத்தச் சட்டம் மூலம் சேர்க்கப்பட்டன.",
            "why_c_en": "Sindhi was added by 21st CAA (1967); Santhali and Dogri by 92nd CAA (2003).",
            "why_c_ta": "சிந்தி 21-வது திருத்தச் சட்டம் (1967) மூலமும், சந்தாலி மற்றும் டோக்ரி 92-வது திருத்தச் சட்டம் (2003) மூலமும் சேர்க்கப்பட்டன.",
            "why_d_en": "Bodo and Santhali belong to the 92nd Amendment, not the 71st.",
            "why_d_ta": "போடோ மற்றும் சந்தாலி 92-வது திருத்தச் சட்டத்தைச் சேர்ந்தவை, 71-வது திருத்தத்தைச் சேர்ந்தவை அல்ல.",
            "tip_en": "71st Amendment (1992) = K-M-N (Konkani, Manipuri, Nepali).",
            "tip_ta": "71-வது சட்டத்திருத்தம் (1992) = கொ-ம-நே (கொங்கணி, மணிப்பூரி, நேபாளி).",
            "fact_en": "Nepali is spoken widely in Sikkim and parts of West Bengal (Darjeeling).",
            "fact_ta": "நேபாளி சிக்கிம் மற்றும் மேற்கு வங்காளத்தின் சில பகுதிகளில் (டார்ஜிலிங்) பரவலாகப் பேசப்படுகிறது."
        },
        # 28
        {
            "subtopic": "92nd Amendment Act, 2003",
            "stem_en": "How many languages were added to the Eighth Schedule by the 92nd Constitutional Amendment Act, 2003?",
            "stem_ta": "2003-ன் 92-வது அரசியலமைப்புத் திருத்தச் சட்டத்தின் மூலம் எட்டாவது அட்டவணையில் எத்தனை மொழிகள் சேர்க்கப்பட்டன?",
            "options": [
                ("4 languages (Bodo, Dogri, Maithili, Santhali)", "4 மொழிகள் (போடோ, டோக்ரி, மைதிலி, சந்தாலி)"),
                ("3 languages (Konkani, Manipuri, Nepali)", "3 மொழிகள் (கொங்கணி, மணிப்பூரி, நேபாளி)"),
                ("1 language (Sindhi)", "1 மொழி (சிந்தி)"),
                ("2 languages (Odia, Bhojpuri)", "2 மொழிகள் (ஒடியா, போஜ்புரி)")
            ],
            "correct_key": "A",
            "exp_en": "The 92nd Constitutional Amendment Act, 2003 added four languages to the Eighth Schedule: Bodo, Dogri, Maithili, and Santhali (mnemonic: BDM-S), taking the total from 18 to 22.",
            "exp_ta": "2003-ன் 92-வது அரசியலமைப்புத் திருத்தச் சட்டம் போடோ, டோக்ரி, மைதிலி மற்றும் சந்தாலி (BDMS) ஆகிய நான்கு மொழிகளை எட்டாவது அட்டவணையில் சேர்த்தது, இதன் மூலம் எண்ணிக்கை 18-லிருந்து 22 ஆக உயர்ந்தது.",
            "why_a_en": "The 92nd CAA, 2003 added exactly 4 languages: Bodo, Dogri, Maithili, Santhali.",
            "why_a_ta": "92-வது சட்டத்திருத்தம், 2003 சரியாக 4 மொழிகளைச் சேர்த்தது: போடோ, டோக்ரி, மைதிலி, சந்தாலி.",
            "why_b_en": "3 languages were added by the 71st CAA in 1992.",
            "why_b_ta": "3 மொழிகள் 1992-ல் 71-வது திருத்தச் சட்டம் மூலம் சேர்க்கப்பட்டன.",
            "why_c_en": "1 language (Sindhi) was added by the 21st CAA in 1967.",
            "why_c_ta": "1 மொழி (சிந்தி) 1967-ல் 21-வது திருத்தச் சட்டம் மூலம் சேர்க்கப்பட்டது.",
            "why_d_en": "Bhojpuri is not in the Eighth Schedule; Odia was originally included as Oriya.",
            "why_d_ta": "போஜ்புரி எட்டாவது அட்டவணையில் இல்லை; ஒடியா தொடக்கத்திலேயே ஒரியாவாக சேர்க்கப்பட்டிருந்தது.",
            "tip_en": "Mnemonic: 21st (1) + 71st (3) = 92nd (4) languages added!",
            "tip_ta": "நினைவுக்குறிப்பு: 21 (1) + 71 (3) = 92-வது திருத்தம் (4 மொழிகள் சேர்க்கப்பட்டன)!",
            "fact_en": "The 92nd Amendment came into force on January 7, 2004.",
            "fact_ta": "92-வது திருத்தச் சட்டம் 2004 ஜனவரி 7 அன்று அமலுக்கு வந்தது."
        },
        # 29
        {
            "subtopic": "96th Amendment Act, 2011",
            "stem_en": "What change was effected in the Eighth Schedule by the 96th Constitutional Amendment Act, 2011?",
            "stem_ta": "2011-ன் 96-வது அரசியலமைப்புத் திருத்தச் சட்டத்தின் மூலம் எட்டாவது அட்டவணையில் செய்யப்பட்ட மாற்றம் என்ன?",
            "options": [
                ("The entry 'Oriya' was substituted with 'Odia'", "'ஒரியா' என்ற பெயர் 'ஒடியா' என மாற்றப்பட்டது"),
                ("A new language 'Bhojpuri' was added", "'போஜ்புரி' என்ற புதிய மொழி சேர்க்கப்பட்டது"),
                ("English was added to the Eighth Schedule", "ஆங்கிலம் எட்டாவது அட்டவணையில் சேர்க்கப்பட்டது"),
                ("Rajasthani was accorded scheduled status", "ராஜஸ்தானிக்கு அட்டவணை அந்தஸ்து வழங்கப்பட்டது")
            ],
            "correct_key": "A",
            "exp_en": "The 96th Constitutional Amendment Act, 2011 substituted the word 'Odia' for 'Oriya' in the Eighth Schedule, alongside the Orissa (Alteration of Name) Act, 2011.",
            "exp_ta": "2011-ன் 96-வது அரசியலமைப்புத் திருத்தச் சட்டம், ஒரிசா (பெயர் மாற்றம்) சட்டம் 2011-உடன் இணைந்து, எட்டாவது அட்டவணையில் 'ஒரியா' என்ற பெயரை 'ஒடியா' என மாற்றியது.",
            "why_a_en": "The 96th CAA solely changed the spelling and pronunciation of Oriya to Odia.",
            "why_a_ta": "96-வது திருத்தச் சட்டம் ஒரியா என்ற சொல்லுக்குப் பதிலாக ஒடியா என்பதை மட்டுமே மாற்றியமைத்தது.",
            "why_b_en": "Bhojpuri has not been added to the Eighth Schedule despite repeated demands.",
            "why_b_ta": "தொடர் கோரிக்கைகள் இருந்தபோதிலும் போஜ்புரி எட்டாவது அட்டவணையில் சேர்க்கப்படவில்லை.",
            "why_c_en": "English is not included in the Eighth Schedule of the Constitution.",
            "why_c_ta": "அரசியலமைப்பின் எட்டாவது அட்டவணையில் ஆங்கிலம் சேர்க்கப்படவில்லை.",
            "why_d_en": "Rajasthani remains pending demand, not yet added to the Eighth Schedule.",
            "why_d_ta": "ராஜஸ்தானி இன்னும் நிலுவையில் உள்ள கோரிக்கையாகவே உள்ளது, எட்டாவது அட்டவணையில் சேர்க்கப்படவில்லை.",
            "tip_en": "96th CAA 2011: Oriya -> Odia (No new language added; spelling substituted).",
            "tip_ta": "96-வது திருத்தம் 2011: ஒரியா -> ஒடியா (புதிய மொழி எதுவும் சேர்க்கப்படவில்லை; பெயர் மாற்றம் மட்டுமே).",
            "fact_en": "Simultaneously, the name of the State of Orissa was changed to Odisha.",
            "fact_ta": "அதே நேரத்தில், ஒரிசா மாநிலத்தின் பெயரும் ஒடிசா என மாற்றப்பட்டது."
        },
        # 30
        {
            "subtopic": "English Status in Eighth Schedule",
            "stem_en": "Is the English language included in the Eighth Schedule of the Constitution of India?",
            "stem_ta": "இந்திய அரசியலமைப்பின் எட்டாவது அட்டவணையில் ஆங்கில மொழி சேர்க்கப்பட்டுள்ளதா?",
            "options": [
                ("No, English is not included in the Eighth Schedule", "இல்லை, ஆங்கிலம் எட்டாவது அட்டவணையில் சேர்க்கப்படவில்லை"),
                ("Yes, English was included in 1950 originally", "ஆம், ஆங்கிலம் 1950-ல் தொடக்கத்திலேயே சேர்க்கப்பட்டது"),
                ("Yes, English was added by the 21st Amendment", "ஆம், ஆங்கிலம் 21-வது திருத்தத்தின் மூலம் சேர்க்கப்பட்டது"),
                ("Yes, English was added by the 92nd Amendment", "ஆம், ஆங்கிலம் 92-வது திருத்தத்தின் மூலம் சேர்க்கப்பட்டது")
            ],
            "correct_key": "A",
            "exp_en": "English is NOT one of the 22 languages listed in the Eighth Schedule of the Constitution of India, despite being the associate official language of the Union and the sole official language of some States.",
            "exp_ta": "ஒன்றியத்தின் கூடுதல் அதிகாரப்பூர்வ மொழியாகவும் சில மாநிலங்களின் ஒரே அதிகாரப்பூர்வ மொழியாகவும் இருந்தபோதிலும், இந்திய அரசியலமைப்பின் எட்டாவது அட்டவணையில் உள்ள 22 மொழிகளில் ஆங்கிலம் சேர்க்கப்படவில்லை.",
            "why_a_en": "English is completely absent from the Eighth Schedule.",
            "why_a_ta": "எட்டாவது அட்டவணையில் ஆங்கிலம் முழுமையாக இடம்பெறவில்லை.",
            "why_b_en": "1950 list had 14 Indian languages, not English.",
            "why_b_ta": "1950 பட்டியலில் 14 இந்திய மொழிகள் இருந்தன, ஆங்கிலம் இல்லை.",
            "why_c_en": "The 21st Amendment added Sindhi, not English.",
            "why_c_ta": "21-வது திருத்தம் சிந்தியைச் சேர்த்தது, ஆங்கிலத்தை அல்ல.",
            "why_d_en": "The 92nd Amendment added Bodo, Dogri, Maithili, and Santhali.",
            "why_d_ta": "92-வது திருத்தம் போடோ, டோக்ரி, மைதிலி மற்றும் சந்தாலியைச் சேர்த்தது.",
            "tip_en": "Classic TNPSC Trap: English is the official language of Nagaland, but NOT in the 8th Schedule!",
            "tip_ta": "முக்கிய டிஎன்பிஎஸ்சி பொறி: ஆங்கிலம் நாகாலாந்தின் அதிகாரப்பூர்வ மொழி, ஆனால் 8-வது அட்டவணையில் இல்லை!",
            "fact_en": "Sahitya Akademi gives awards in 24 languages: 22 Eighth Schedule languages + English and Rajasthani.",
            "fact_ta": "சாகித்ய அகாதமி 24 மொழிகளில் விருதுகளை வழங்குகிறது: 22 எட்டாவது அட்டவணை மொழிகள் + ஆங்கிலம் மற்றும் ராஜஸ்தானி."
        },
        # 31
        {
            "subtopic": "First Classical Language of India",
            "stem_en": "Which was the first language in India to be accorded the status of a 'Classical Language' by the Government of India in 2004?",
            "stem_ta": "2004-ல் இந்திய அரசால் 'செம்மொழி' (Classical Language) அந்தஸ்து வழங்கப்பட்ட இந்தியாவின் முதல் மொழி எது?",
            "options": [
                ("Tamil", "தமிழ்"),
                ("Sanskrit", "சமஸ்கிருதம்"),
                ("Telugu", "தெலுங்கு"),
                ("Kannada", "கன்னடம்")
            ],
            "correct_key": "A",
            "exp_en": "Tamil was the first language to be declared as a Classical Language of India in October 2004, under the government headed by Prime Minister Manmohan Singh.",
            "exp_ta": "பிரதமர் மன்மோகன் சிங் தலைமையிலான அரசால் 2004 அக்டோபரில் இந்தியாவின் முதல் செம்மொழியாகத் தமிழ் அறிவிக்கப்பட்டது.",
            "why_a_en": "Tamil received the historic first classical language notification in October 2004.",
            "why_a_ta": "தமிழ் அக்டோபர் 2004-ல் வரலாற்றுச் சிறப்புமிக்க முதல் செம்மொழி அறிவிப்பைப் பெற்றது.",
            "why_b_en": "Sanskrit was declared a Classical Language in 2005 (second).",
            "why_b_ta": "சமஸ்கிருதம் 2005-ல் (இரண்டாவதாக) செம்மொழியாக அறிவிக்கப்பட்டது.",
            "why_c_en": "Telugu was declared a Classical Language in 2008.",
            "why_c_ta": "தெலுங்கு 2008-ல் செம்மொழியாக அறிவிக்கப்பட்டது.",
            "why_d_en": "Kannada was declared a Classical Language in 2008.",
            "why_d_ta": "கன்னடம் 2008-ல் செம்மொழியாக அறிவிக்கப்பட்டது.",
            "tip_en": "First Classical Language = TAMIL (2004); Second = SANSKRIT (2005).",
            "tip_ta": "முதல் செம்மொழி = தமிழ் (2004); இரண்டாவது = சமஸ்கிருதம் (2005).",
            "fact_en": "The Central Institute of Classical Tamil (CICT) is headquartered in Chennai.",
            "fact_ta": "செம்மொழித் தமிழாய்வு மத்திய நிறுவனம் (CICT) சென்னையில் தலைமையிடத்தைக் கொண்டுள்ளது."
        },
        # 32
        {
            "subtopic": "Classical Language Declaration Year for Sanskrit",
            "stem_en": "In which year was Sanskrit declared as a Classical Language of India?",
            "stem_ta": "சமஸ்கிருதம் இந்தியாவின் செம்மொழியாக எந்த ஆண்டில் அறிவிக்கப்பட்டது?",
            "options": [
                ("2005", "2005"),
                ("2004", "2004"),
                ("2008", "2008"),
                ("2013", "2013")
            ],
            "correct_key": "A",
            "exp_en": "Sanskrit was declared a Classical Language in 2005, one year after Tamil was recognized in 2004.",
            "exp_ta": "2004-ல் தமிழுக்கு அங்கீகாரம் வழங்கப்பட்ட ஒரு வருடத்திற்குப் பிறகு, 2005-ல் சமஸ்கிருதம் செம்மொழியாக அறிவிக்கப்பட்டது.",
            "why_a_en": "Sanskrit classical status was notified in 2005.",
            "why_a_ta": "சமஸ்கிருதத்தின் செம்மொழி அந்தஸ்து 2005-ல் அறிவிக்கப்பட்டது.",
            "why_b_en": "2004 was the year Tamil was declared classical language.",
            "why_b_ta": "2004 தமிழ் செம்மொழியாக அறிவிக்கப்பட்ட ஆண்டாகும்.",
            "why_c_en": "2008 was the year Telugu and Kannada were declared classical languages.",
            "why_c_ta": "2008 தெலுங்கு மற்றும் கன்னடம் செம்மொழிகளாக அறிவிக்கப்பட்ட ஆண்டாகும்.",
            "why_d_en": "2013 was the year Malayalam was declared classical language.",
            "why_d_ta": "2013 மலையாளம் செம்மொழியாக அறிவிக்கப்பட்ட ஆண்டாகும்.",
            "tip_en": "Classical Languages chronology: Tamil (2004) -> Sanskrit (2005) -> Telugu & Kannada (2008).",
            "tip_ta": "செம்மொழிகள் காலவரிசை: தமிழ் (2004) -> சமஸ்கிருதம் (2005) -> தெலுங்கு & கன்னடம் (2008).",
            "fact_en": "Central Sanskrit University, New Delhi promotes classical Sanskrit studies.",
            "fact_ta": "புது தில்லியில் உள்ள மத்திய சமஸ்கிருதப் பல்கலைக்கழகம் செம்மொழி சமஸ்கிருத ஆய்வுகளை ஊக்குவிக்கிறது."
        },
        # 33
        {
            "subtopic": "Classical Language Status for Telugu and Kannada",
            "stem_en": "In which year were Kannada and Telugu accorded Classical Language status?",
            "stem_ta": "கன்னடம் மற்றும் தெலுங்கு ஆகிய மொழிகளுக்கு எந்த ஆண்டில் செம்மொழி அந்தஸ்து வழங்கப்பட்டது?",
            "options": [
                ("2008", "2008"),
                ("2004", "2004"),
                ("2005", "2005"),
                ("2014", "2014")
            ],
            "correct_key": "A",
            "exp_en": "Both Telugu and Kannada were granted Classical Language status concurrently in the year 2008.",
            "exp_ta": "தெலுங்கு மற்றும் கன்னடம் ஆகிய இரண்டு மொழிகளுக்கும் 2008 ஆம் ஆண்டில் ஒரே நேரத்தில் செம்மொழி அந்தஸ்து வழங்கப்பட்டது.",
            "why_a_en": "Telugu and Kannada were concurrently notified as classical languages in 2008.",
            "why_a_ta": "தெலுங்கு மற்றும் கன்னடம் இரண்டும் 2008-ல் ஒரே நேரத்தில் செம்மொழிகளாக அறிவிக்கப்பட்டன.",
            "why_b_en": "2004 was Tamil.",
            "why_b_ta": "2004 தமிழ் மொழிக்குரியது.",
            "why_c_en": "2005 was Sanskrit.",
            "why_c_ta": "2005 சமஸ்கிருதத்திற்குரியது.",
            "why_d_en": "2014 was Odia.",
            "why_d_ta": "2014 ஒடியா மொழிக்குரியது.",
            "tip_en": "2008 = Double K-T (Kannada & Telugu).",
            "tip_ta": "2008 = இரட்டை மொழிகள் (கன்னடம் & தெலுங்கு).",
            "fact_en": "The declaration followed expert committee verification of ancient inscriptions and literary texts.",
            "fact_ta": "பண்டைய கல்வெட்டுகள் மற்றும் இலக்கிய நூல்களை நிபுணர் குழு சரிபார்த்த பிறகு இந்த அறிவிப்பு வெளியானது."
        },
        # 34
        {
            "subtopic": "Classical Language Status for Malayalam and Odia",
            "stem_en": "In which years were Malayalam and Odia declared Classical Languages respectively?",
            "stem_ta": "மலையாளம் மற்றும் ஒடியா மொழிகள் முறையே எந்த ஆண்டுகளில் செம்மொழிகளாக அறிவிக்கப்பட்டன?",
            "options": [
                ("2013 and 2014", "2013 மற்றும் 2014"),
                ("2008 and 2010", "2008 மற்றும் 2010"),
                ("2004 and 2005", "2004 மற்றும் 2005"),
                ("2015 and 2016", "2015 மற்றும் 2016")
            ],
            "correct_key": "A",
            "exp_en": "Malayalam was declared a Classical Language in 2013, and Odia was declared in 2014 (the 6th classical language).",
            "exp_ta": "மலையாளம் 2013-லும், ஒடியா 2014-லும் (6-வது செம்மொழி) செம்மொழிகளாக அறிவிக்கப்பட்டன.",
            "why_a_en": "Malayalam = 2013; Odia = 2014.",
            "why_a_ta": "மலையாளம் = 2013; ஒடியா = 2014.",
            "why_b_en": "2008 was Telugu/Kannada; no language was declared in 2010.",
            "why_b_ta": "2008 தெலுங்கு/கன்னடம்; 2010-ல் எந்த மொழியும் அறிவிக்கப்படவில்லை.",
            "why_c_en": "2004 was Tamil; 2005 was Sanskrit.",
            "why_c_ta": "2004 தமிழ்; 2005 சமஸ்கிருதம்.",
            "why_d_en": "No classical declarations occurred in 2015 and 2016.",
            "why_d_ta": "2015 மற்றும் 2016-ல் செம்மொழி அறிவிப்புகள் எதுவும் நிகழவில்லை.",
            "tip_en": "Odia was the first Indo-Aryan language after Sanskrit to be declared classical (2014).",
            "tip_ta": "சமஸ்கிருதத்திற்குப் பிறகு செம்மொழியாக அறிவிக்கப்பட்ட முதல் இந்தோ-ஆரிய மொழி ஒடியா (2014).",
            "fact_en": "Until October 2024, there were 6 Classical Languages in India.",
            "fact_ta": "அக்டோபர் 2024 வரை இந்தியாவில் 6 செம்மொழிகள் மட்டுமே இருந்தன."
        },
        # 35
        {
            "subtopic": "2024 Classical Languages Expansion",
            "stem_en": "In October 2024, the Union Cabinet approved Classical Language status for which five languages simultaneously?",
            "stem_ta": "அக்டோபர் 2024-ல், ஒன்றிய அமைச்சரவை ஒரே நேரத்தில் எந்த ஐந்து மொழிகளுக்குச் செம்மொழி அந்தஸ்தை அங்கீகரித்தது?",
            "options": [
                ("Marathi, Pali, Prakrit, Assamese, and Bengali", "மராத்தி, பாலி, பிராகிருதம், அசாமி மற்றும் பெங்காலி"),
                ("Bhojpuri, Rajasthani, Maithili, Tulu, and Konkani", "போஜ்புரி, ராஜஸ்தானி, மைதிலி, துளு மற்றும் கொங்கணி"),
                ("Urdu, Sindhi, Kashmiri, Dogri, and Santhali", "உருது, சிந்தி, காஷ்மீரி, டோக்ரி மற்றும் சந்தாலி"),
                ("Hindi, English, Sanskrit, Persian, and Arabic", "இந்தி, ஆங்கிலம், சமஸ்கிருதம், பாரசீகம் மற்றும் அரபு")
            ],
            "correct_key": "A",
            "exp_en": "On October 3, 2024, the Union Cabinet chaired by PM Narendra Modi approved Classical Language status for five languages: Marathi, Pali, Prakrit, Assamese, and Bengali, expanding the total count to 11.",
            "exp_ta": "2024 அக்டோபர் 3 அன்று, பிரதமர் நரேந்திர மோடி தலைமையிலான ஒன்றிய அமைச்சரவை மராத்தி, பாலி, பிராகிருதம், அசாமி மற்றும் பெங்காலி ஆகிய ஐந்து மொழிகளுக்குச் செம்மொழி அந்தஸ்தை வழங்கியது, இதனால் மொத்த எண்ணிக்கை 11 ஆக உயர்ந்தது.",
            "why_a_en": "These exact 5 languages received the historic landmark cabinet approval in October 2024.",
            "why_a_ta": "இந்த 5 மொழிகள் அக்டோபர் 2024-ல் வரலாற்றுச் சிறப்புமிக்க அமைச்சரவை அங்கீகாரத்தைப் பெற்றன.",
            "why_b_en": "Bhojpuri, Rajasthani, and Tulu have not received classical language status.",
            "why_b_ta": "போஜ்புரி, ராஜஸ்தானி மற்றும் துளு ஆகிய மொழிகளுக்குச் செம்மொழி அந்தஸ்து கிடைக்கவில்லை.",
            "why_c_en": "Urdu, Sindhi, and Kashmiri have not been declared classical languages.",
            "why_c_ta": "உருது, சிந்தி மற்றும் காஷ்மீரி ஆகியவை செம்மொழிகளாக அறிவிக்கப்படவில்லை.",
            "why_d_en": "Hindi and English are official languages, not Classical Languages.",
            "why_d_ta": "இந்தி மற்றும் ஆங்கிலம் அதிகாரப்பூர்வ மொழிகள், செம்மொழிகள் அல்ல.",
            "tip_en": "Current Classical Languages = 11 (6 earlier + 5 in October 2024).",
            "tip_ta": "தற்போதைய செம்மொழிகள் = 11 (முந்தைய 6 + அக்டோபர் 2024-ல் 5).",
            "fact_en": "Pali and Prakrit are ancient languages not listed in the Eighth Schedule, yet granted Classical status.",
            "fact_ta": "பாலி மற்றும் பிராகிருதம் எட்டாவது அட்டவணையில் இல்லாத பண்டைய மொழிகள், இருப்பினும் செம்மொழி அந்தஸ்து பெற்றுள்ளன."
        },
        # 36
        {
            "subtopic": "Enactment of Official Languages Act",
            "stem_en": "In which year did the Parliament of India pass the Official Languages Act under Article 343(3)?",
            "stem_ta": "சரத்து 343(3)-ன் கீழ் இந்திய நாடாளுமன்றம் அதிகாரப்பூர்வ மொழிகள் சட்டத்தை எந்த ஆண்டில் இயற்றியது?",
            "options": [
                ("1963", "1963"),
                ("1955", "1955"),
                ("1950", "1950"),
                ("1967", "1967")
            ],
            "correct_key": "A",
            "exp_en": "The Official Languages Act was enacted by Parliament in 1963 to provide for the languages which may be used for the official purposes of the Union beyond January 26, 1965.",
            "exp_ta": "1965 ஜனவரி 26-க்குப் பிறகும் ஒன்றியத்தின் அதிகாரப்பூர்வ பணிகளுக்குப் பயன்படுத்தப்பட வேண்டிய மொழிகளை வழங்க 1963-ல் நாடாளுமன்றத்தால் அதிகாரப்பூர்வ மொழிகள் சட்டம் இயற்றப்பட்டது.",
            "why_a_en": "The original Official Languages Act was passed in 1963.",
            "why_a_ta": "அசல் அதிகாரப்பூர்வ மொழிகள் சட்டம் 1963-ல் நிறைவேற்றப்பட்டது.",
            "why_b_en": "1955 was the year the B.G. Kher Commission was appointed.",
            "why_b_ta": "1955 என்பது பி.ஜி. கெர் ஆணையம் அமைக்கப்பட்ட ஆண்டாகும்.",
            "why_c_en": "1950 was the year the Constitution commenced.",
            "why_c_ta": "1950 என்பது அரசியலமைப்பு அமலுக்கு வந்த ஆண்டாகும்.",
            "why_d_en": "1967 was the year the major Amendment Act was passed.",
            "why_d_ta": "1967 என்பது முக்கிய திருத்தச் சட்டம் நிறைவேற்றப்பட்ட ஆண்டாகும்.",
            "tip_en": "Official Languages Act, 1963 came into force Section 3 on January 26, 1965.",
            "tip_ta": "அதிகாரப்பூர்வ மொழிகள் சட்டம், 1963-ன் பிரிவு 3 ஜனவரி 26, 1965 அன்று அமலுக்கு வந்தது.",
            "fact_en": "Prime Minister Jawaharlal Nehru gave solemn assurances in Parliament that English would continue as an associate language.",
            "fact_ta": "பிரதமர் ஜவஹர்லால் நேரு நாடாளுமன்றத்தில் ஆங்கிலம் கூடுதல் மொழியாகத் தொடரும் என்று உறுதியளித்தார்."
        },
        # 37
        {
            "subtopic": "1967 Amendment Non-Hindi Veto",
            "stem_en": "What crucial safeguard was introduced by the Official Languages (Amendment) Act, 1967 regarding the discontinuance of English?",
            "stem_ta": "ஆங்கிலத்தை நிறுத்துவது தொடர்பாக அதிகாரப்பூர்வ மொழிகள் (திருத்தச்) சட்டம், 1967-ன் மூலம் அறிமுகப்படுத்தப்பட்ட முக்கியமான பாதுகாப்பு எது?",
            "options": [
                ("English cannot be discontinued without resolutions passed by legislatures of all non-Hindi States and both Houses of Parliament", "அனைத்து இந்தி பேசாத மாநிலங்களின் சட்டமன்றங்கள் மற்றும் நாடாளுமன்றத்தின் இரு அவைகளும் தீர்மானம் நிறைவேற்றாமல் ஆங்கிலத்தை நிறுத்த முடியாது"),
                ("The President can abolish English at any time by executive order", "குடியரசுத் தலைவர் நிர்வாக உத்தரவு மூலம் எந்த நேரத்திலும் ஆங்கிலத்தை ரத்து செய்யலாம்"),
                ("English was discontinued immediately with effect from 1967", "1967 முதல் உடனடியாக ஆங்கிலம் நிறுத்தப்பட்டது"),
                ("Only the Supreme Court can decide on the continuation of English", "உச்ச நீதிமன்றம் மட்டுமே ஆங்கிலம் தொடர்வது குறித்து தீர்மானிக்க முடியும்")
            ],
            "correct_key": "A",
            "exp_en": "Section 3(5) inserted by the 1967 Amendment provided that English shall not cease to be used until resolutions for discontinuance are passed by the Legislatures of all States which have not adopted Hindi as official language, and by each House of Parliament.",
            "exp_ta": "1967 திருத்தத்தின் மூலம் சேர்க்கப்பட்ட பிரிவு 3(5), இந்தியை அதிகாரப்பூர்வ மொழியாக ஏற்றுக்கொள்ளாத அனைத்து மாநிலங்களின் சட்டமன்றங்களும் மற்றும் நாடாளுமன்றத்தின் இரு அவைகளும் தீர்மானம் நிறைவேற்றும் வரை ஆங்கிலத்தின் பயன்பாட்டை நிறுத்த முடியாது என்ற சட்டப்பூர்வ தடையை விதித்தது.",
            "why_a_en": "This statutory lock gave an effective veto to each non-Hindi speaking State (including Tamil Nadu).",
            "why_a_ta": "இந்த சட்டப்பூர்வப் பூட்டு ஒவ்வொரு இந்தி பேசாத மாநிலத்திற்கும் (தமிழ்நாடு உட்பட) ஒரு வீட்டோ அதிகாரத்தை வழங்கியது.",
            "why_b_en": "The President cannot abolish English by executive decree.",
            "why_b_ta": "குடியரசுத் தலைவர் நிர்வாக ஆணை மூலம் ஆங்கிலத்தை ரத்து செய்ய முடியாது.",
            "why_c_en": "English was continued indefinitely, not discontinued.",
            "why_c_ta": "ஆங்கிலம் காலவரையின்றி தொடரப்பட்டது, நிறுத்தப்படவில்லை.",
            "why_d_en": "The decision is political and legislative, not judicial.",
            "why_d_ta": "இம்முடிவு அரசியல் மற்றும் சட்டமன்ற அதிகாரம் சார்ந்தது, நீதித்துறை சார்ந்தது அல்ல.",
            "tip_en": "Statutory Non-Hindi Veto: Even if ONE non-Hindi State objects, English MUST continue.",
            "tip_ta": "சட்டப்பூர்வ வீட்டோ: ஒரே ஒரு இந்தி பேசாத மாநிலம் எதிர்த்தாலும், ஆங்கிலம் தொடர வேண்டும்.",
            "fact_en": "This amendment fulfilled the historic 'Nehru Assurance' in statutory form under PM Indira Gandhi.",
            "fact_ta": "பிரதமர் இந்திரா காந்தியின் கீழ் வரலாற்றுச் சிறப்புமிக்க 'நேருவின் உறுதிமொழிக்கு' இந்தத் திருத்தம் சட்ட வடிவம் கொடுத்தது."
        },
        # 38
        {
            "subtopic": "Tamil Nadu Two-Language Formula",
            "stem_en": "In which year did the Tamil Nadu Legislative Assembly, led by Chief Minister C.N. Annadurai, pass the historic resolution adopting the Two-Language Formula (Tamil and English)?",
            "stem_ta": "முதலமைச்சர் சி.என். அண்ணாதுரை தலைமையில் தமிழ்நாடு சட்டமன்றப் பேரவை இருமொழிக் கொள்கையை (தமிழ் மற்றும் ஆங்கிலம்) ஏற்று வரலாற்றுச் சிறப்புமிக்க தீர்மானத்தை எந்த ஆண்டில் நிறைவேற்றியது?",
            "options": [
                ("1968", "1968"),
                ("1965", "1965"),
                ("1956", "1956"),
                ("1971", "1971")
            ],
            "correct_key": "A",
            "exp_en": "On January 23, 1968, the Tamil Nadu Legislative Assembly passed a historic resolution eliminating the Three-Language Formula and officially adopting the Two-Language Policy (Tamil and English).",
            "exp_ta": "1968 ஜனவரி 23 அன்று, தமிழ்நாடு சட்டமன்றப் பேரவை மும்மொழிக் கொள்கையை நிராகரித்து, இருமொழிக் கொள்கையை (தமிழ் மற்றும் ஆங்கிலம்) அதிகாரப்பூர்வமாக ஏற்று வரலாற்றுச் சிறப்புமிக்க தீர்மானத்தை நிறைவேற்றியது.",
            "why_a_en": "January 23, 1968 was the landmark special session resolution under C.N. Annadurai.",
            "why_a_ta": "1968 ஜனவரி 23 என்பது சி.என். அண்ணாதுரை தலைமையிலான சிறப்பு சட்டமன்றக் கூட்டத்தொடர் தீர்மான நாளாகும்.",
            "why_b_en": "1965 was the year of massive student anti-Hindi agitations in TN.",
            "why_b_ta": "1965 என்பது தமிழகத்தில் மாணவர்கள் நடத்திய தீவிர இந்தி எதிர்ப்புப் போராட்ட ஆண்டாகும்.",
            "why_c_en": "1956 was the year of the Tamil Nadu Official Language Act declaring Tamil as state official language.",
            "why_c_ta": "1956 என்பது தமிழை மாநில அதிகாரப்பூர்வ மொழியாக அறிவித்த தமிழ்நாடு அதிகாரப்பூர்வ மொழிச் சட்ட ஆண்டாகும்.",
            "why_d_en": "1971 was later during the tenure of M. Karunanidhi.",
            "why_d_ta": "1971 என்பது பின்னர் மு. கருணாநிதியின் ஆட்சிக்காலமாகும்.",
            "tip_en": "Tamil Nadu Formula: Tamil + English (Two-Language Policy since 1968).",
            "tip_ta": "தமிழ்நாட்டின் கொள்கை: தமிழ் + ஆங்கிலம் (1968 முதல் இருமொழிக் கொள்கை).",
            "fact_en": "The 1968 resolution also eliminated Hindi commands in the National Cadet Corps (NCC) in Tamil Nadu.",
            "fact_ta": "1968 தீர்மானம் தமிழ்நாட்டில் தேசிய மாணவர் படையில் (NCC) இந்தி கட்டளைகளையும் நீக்கியது."
        },
        # 39
        {
            "subtopic": "Tamil Nadu Official Language Act",
            "stem_en": "In which year was the Tamil Nadu Official Language Act enacted, declaring Tamil as the official language of the State?",
            "stem_ta": "தமிழை மாநிலத்தின் அதிகாரப்பூர்வ மொழியாக அறிவித்த தமிழ்நாடு அதிகாரப்பூர்வ மொழிச் சட்டம் எந்த ஆண்டில் இயற்றப்பட்டது?",
            "options": [
                ("1956", "1956"),
                ("1968", "1968"),
                ("1950", "1950"),
                ("1963", "1963")
            ],
            "correct_key": "A",
            "exp_en": "The Tamil Nadu Official Language Act was enacted in 1956 (Madras Act XXXIX of 1956) under Chief Minister K. Kamaraj, declaring Tamil as the official language of the State.",
            "exp_ta": "முதலமைச்சர் கே. காமராஜர் ஆட்சியின் கீழ் 1956-ல் தமிழ்நாடு அதிகாரப்பூர்வ மொழிச் சட்டம் இயற்றப்பட்டு, தமிழ் மாநிலத்தின் அதிகாரப்பூர்வ மொழியாக அறிவிக்கப்பட்டது.",
            "why_a_en": "1956 was the year the Madras Official Language Act was enacted under Kamaraj.",
            "why_a_ta": "1956 என்பது காமராஜர் ஆட்சியில் சென்னை மாகாண அதிகாரப்பூர்வ மொழிச் சட்டம் இயற்றப்பட்ட ஆண்டாகும்.",
            "why_b_en": "1968 was the Two-Language Resolution year.",
            "why_b_ta": "1968 என்பது இருமொழிக் கொள்கைத் தீர்மானம் நிறைவேற்றப்பட்ட ஆண்டாகும்.",
            "why_c_en": "1950 was the year the Constitution of India commenced.",
            "why_c_ta": "1950 என்பது இந்திய அரசியலமைப்பு அமலுக்கு வந்த ஆண்டாகும்.",
            "why_d_en": "1963 was the central Official Languages Act.",
            "why_d_ta": "1963 என்பது ஒன்றியத்தின் அதிகாரப்பூர்வ மொழிகள் சட்டமாகும்.",
            "tip_en": "TN Official Language Act = 1956 (Kamaraj); Two-Language Resolution = 1968 (Annadurai).",
            "tip_ta": "தமிழக அதிகாரப்பூர்வ மொழிச் சட்டம் = 1956 (காமராஜர்); இருமொழிக் கொள்கைத் தீர்மானம் = 1968 (அண்ணாதுரை).",
            "fact_en": "Tamil was introduced progressively in government offices and courts following this Act.",
            "fact_ta": "இச்சட்டத்தைத் தொடர்ந்து அரசு அலுவலகங்கள் மற்றும் நீதிமன்றங்களில் தமிழ் படிப்படியாக அறிமுகப்படுத்தப்பட்டது."
        },
        # 40
        {
            "subtopic": "Official Languages Rules, 1976 Classification",
            "stem_en": "Under the Official Languages Rules, 1976, into how many linguistic regions are the States and Union Territories of India classified for official communications?",
            "stem_ta": "அதிகாரப்பூர்வ மொழிகள் விதிகள், 1976-ன் கீழ், அதிகாரப்பூர்வ தகவல்தொடர்புகளுக்காக இந்தியாவின் மாநிலங்கள் மற்றும் ஒன்றியப் பகுதிகள் எத்தனை மொழி மண்டலங்களாகப் பிரிக்கப்பட்டுள்ளன?",
            "options": [
                ("Three regions (Region A, Region B, Region C)", "மூன்று மண்டலங்கள் (மண்டலம் A, மண்டலம் B, மண்டலம் C)"),
                ("Four regions (North, South, East, West)", "நான்கு மண்டலங்கள் (வடக்கு, தெற்கு, கிழக்கு, மேற்கு)"),
                ("Two regions (Hindi and Non-Hindi)", "இரண்டு மண்டலங்கள் (இந்தி மற்றும் இந்தி அல்லாதவை)"),
                ("Five regions (Zonal Council pattern)", "ஐந்து மண்டலங்கள் (மண்டலக் குழு முறை)"),
            ],
            "correct_key": "A",
            "exp_en": "The Official Languages Rules, 1976 classify States and UTs into three regions: Region A (predominantly Hindi states), Region B (partially Hindi states), and Region C (non-Hindi states including South India).",
            "exp_ta": "அதிகாரப்பூர்வ மொழிகள் விதிகள் 1976 மாநிலங்கள் மற்றும் யூனியன் பிரதேசங்களை மூன்று மண்டலங்களாகப் பிரிக்கிறது: மண்டலம் A (முழு இந்தி மாநிலங்கள்), மண்டலம் B (பகுதி இந்தி மாநிலங்கள்), மற்றும் மண்டலம் C (தென்னிந்தியா உள்ளிட்ட இந்தி பேசாத மாநிலங்கள்).",
            "why_a_en": "The 1976 Rules officially categorize India into Region A, Region B, and Region C.",
            "why_a_ta": "1976 விதிகள் அதிகாரப்பூர்வமாக இந்தியாவை மண்டலம் A, மண்டலம் B மற்றும் மண்டலம் C எனப் பிரிக்கின்றன.",
            "why_b_en": "Geographical four-direction classification is not used in language rules.",
            "why_b_ta": "புவியியல் நான்கு திசைப் பிரிப்பு மொழி விதிகளில் பயன்படுத்தப்படவில்லை.",
            "why_c_en": "It is a three-tier classification, not binary.",
            "why_c_ta": "இது மூன்று அடுக்கு வகைப்பாடு, இரண்டு அடுக்கு அல்ல.",
            "why_d_en": "Five regions relate to Zonal Councils under States Reorganisation Act, not language rules.",
            "why_d_ta": "ஐந்து மண்டலங்கள் என்பது மாநில மறுசீரமைப்புச் சட்டத்தின் கீழான மண்டலக் கவுன்சில்களுடன் தொடர்புடையது.",
            "tip_en": "Region A = Hindi heartland; Region B = Gujarat/Maharashtra/Punjab; Region C = South India & North-East.",
            "tip_ta": "மண்டலம் A = இந்தி பேசும் பகுதிகள்; மண்டலம் B = குஜராத்/மகாராஷ்டிரா/பஞ்சாப்; மண்டலம் C = தென்னிந்தியா & வடகிழக்கு.",
            "fact_en": "Communications to Region C are primarily in English.",
            "fact_ta": "மண்டலம் C-க்கான தகவல்தொடர்புகள் முதன்மையாக ஆங்கிலத்திலேயே இருக்கும்."
        },
        # 41
        {
            "subtopic": "Exemption of Tamil Nadu from 1976 Rules",
            "stem_en": "Which State is explicitly exempted from the application of the Official Languages (Use for Official Purpose of the Union) Rules, 1976?",
            "stem_ta": "அதிகாரப்பூர்வ மொழிகள் (ஒன்றியத்தின் அதிகாரப்பூர்வ பணிகளுக்கான பயன்பாடு) விதிகள், 1976-ன் வரம்பிலிருந்து வெளிப்படையாக விலக்கு அளிக்கப்பட்டுள்ள மாநிலம் எது?",
            "options": [
                ("Tamil Nadu", "தமிழ்நாடு"),
                ("Kerala", "கேரளா"),
                ("Karnataka", "கர்நாடகா"),
                ("West Bengal", "மேற்கு வங்காளம்")
            ],
            "correct_key": "A",
            "exp_en": "Rule 1(2) of the Official Languages Rules, 1976 explicitly provides that the Rules extend to the whole of India 'except the State of Tamil Nadu'.",
            "exp_ta": "அதிகாரப்பூர்வ மொழிகள் விதிகள் 1976-ன் விதி 1(2), 'தமிழ்நாடு மாநிலம் நீங்கலாக' இந்தியா முழுமைக்கும் இவ்விதிகள் பொருந்தும் என வெளிப்படையாகக் கூறுகிறது.",
            "why_a_en": "Tamil Nadu has a statutory exemption in Rule 1(2) due to its consistent Two-Language policy.",
            "why_a_ta": "தனது தொடர்ச்சியான இருமொழிக் கொள்கையின் காரணமாக தமிழ்நாடு விதி 1(2)-ல் சட்டப்பூர்வ விலக்கைப் பெற்றுள்ளது.",
            "why_b_en": "Kerala is in Region C and governed by the 1976 Rules.",
            "why_b_ta": "கேரளா மண்டலம் C-ல் உள்ளது மற்றும் 1976 விதிகளுக்கு உட்பட்டது.",
            "why_c_en": "Karnataka is governed by the 1976 Rules under Region C.",
            "why_c_ta": "கர்நாடகா மண்டலம் C-ன் கீழ் 1976 விதிகளுக்கு உட்பட்டது.",
            "why_d_en": "West Bengal is under Region C.",
            "why_d_ta": "மேற்கு வங்காளம் மண்டலம் C-ன் கீழ் வருகிறது.",
            "tip_en": "Rule 1(2) exception: Official Language Rules 1976 do NOT apply to Tamil Nadu.",
            "tip_ta": "விதி 1(2) விதிவிலக்கு: அதிகாரப்பூர்வ மொழிகள் விதிகள் 1976 தமிழ்நாட்டிற்குப் பொருந்தாது.",
            "fact_en": "Union communications to Tamil Nadu must always be accompanied by an English text.",
            "fact_ta": "தமிழ்நாட்டிற்கான ஒன்றியத்தின் தகவல்தொடர்புகள் எப்போதும் ஆங்கில உரையுடன் இணைந்தே இருக்க வேண்டும்."
        },
        # 42
        {
            "subtopic": "National Language Constitutional Reality",
            "stem_en": "Which language is declared as the 'National Language' (Rashtrabhasha) of India in the Constitution of India?",
            "stem_ta": "இந்திய அரசியலமைப்பில் இந்தியாவின் 'தேசிய மொழி' (ராஷ்டிரபாஷா) என்று எந்த மொழி அறிவிக்கப்பட்டுள்ளது?",
            "options": [
                ("No language is declared as the National Language", "எந்தவொரு மொழியும் தேசிய மொழியாக அறிவிக்கப்படவில்லை"),
                ("Hindi in Devanagari script", "தேவநாகரி வரிவடிவ இந்தி"),
                ("Sanskrit", "சமஸ்கிருதம்"),
                ("Both Hindi and English", "இந்தி மற்றும் ஆங்கிலம் ஆகிய இரண்டும்")
            ],
            "correct_key": "A",
            "exp_en": "The Constitution of India does NOT declare any language as the 'National Language'. Article 343 designates Hindi as the 'Official Language of the Union' for administrative purposes.",
            "exp_ta": "இந்திய அரசியலமைப்பு எந்தவொரு மொழியையும் 'தேசிய மொழி'யாக அறிவிக்கவில்லை. சரத்து 343 இந்தியை நிர்வாகப் பணிகளுக்கான 'ஒன்றியத்தின் அதிகாரப்பூர்வ மொழி'யாக மட்டுமே குறிப்பிடுகிறது.",
            "why_a_en": "India has no constitutional National Language; all 22 scheduled languages are equal national heritage languages.",
            "why_a_ta": "இந்தியாவிற்கு அரசியலமைப்பு ரீதியான தேசிய மொழி எதுவும் இல்லை; 22 அட்டவணை மொழிகளும் சமமான தேசிய பாரம்பரிய மொழிகளாகும்.",
            "why_b_en": "Hindi is an Official Language, NOT the National Language.",
            "why_b_ta": "இந்தி அதிகாரப்பூர்வ மொழி மட்டுமே, தேசிய மொழி அல்ல.",
            "why_c_en": "Sanskrit is a classical and scheduled language, not national language.",
            "why_c_ta": "சமஸ்கிருதம் செம்மொழி மற்றும் அட்டவணை மொழி, தேசிய மொழி அல்ல.",
            "why_d_en": "Neither English nor Hindi holds the title of 'National Language'.",
            "why_d_ta": "ஆங்கிலம் அல்லது இந்தி ஆகிய இரண்டுமே 'தேசிய மொழி' என்ற அந்தஸ்தைக் கொண்டிருக்கவில்லை.",
            "tip_en": "Constitutional Truth: Official Language != National Language. India has NO National Language.",
            "tip_ta": "அரசியலமைப்பு உண்மை: அதிகாரப்பூர்வ மொழி != தேசிய மொழி. இந்தியாவிற்குத் தேசிய மொழி எதுவும் இல்லை.",
            "fact_en": "The Gujarat High Court in 2010 (Suresh Kachhadia case) observed that Hindi is not the national language of India.",
            "fact_ta": "2010-ல் குஜராத் உயர் நீதிமன்றம் இந்தி இந்தியாவின் தேசிய மொழி அல்ல என்பதை உறுதிப்படுத்தியது."
        },
        # 43
        {
            "subtopic": "Ministry Governing CLM",
            "stem_en": "Under which Union Ministry does the Commissioner for Linguistic Minorities (appointed under Article 350B) function?",
            "stem_ta": "சரத்து 350B-ன் கீழ் நியமிக்கப்படும் மொழிச் சிறுபான்மையினருக்கான ஆணையர் எந்த ஒன்றிய அமைச்சகத்தின் கீழ் செயல்படுகிறார்?",
            "options": [
                ("Ministry of Minority Affairs", "சிறுபான்மையினர் விவகார அமைச்சகம்"),
                ("Ministry of Home Affairs", "உள்துறை அமைச்சகம்"),
                ("Ministry of Education", "கல்வி அமைச்சகம்"),
                ("Ministry of Law and Justice", "சட்டம் மற்றும் நீதி அமைச்சகம்")
            ],
            "correct_key": "A",
            "exp_en": "The Commissioner for Linguistic Minorities operates under the administrative control of the Ministry of Minority Affairs (created in 2006).",
            "exp_ta": "மொழிச் சிறுபான்மையினருக்கான ஆணையர் சிறுபான்மையினர் விவகார அமைச்சகத்தின் (2006-ல் உருவாக்கப்பட்டது) நிர்வாகக் கட்டுப்பாட்டின் கீழ் செயல்படுகிறார்.",
            "why_a_en": "Since 2006, the organization falls under the Ministry of Minority Affairs.",
            "why_a_ta": "2006 முதல் இவ்வமைப்பு சிறுபான்மையினர் விவகார அமைச்சகத்தின் கீழ் செயல்படுகிறது.",
            "why_b_en": "Earlier it was under Home Affairs and later Social Justice, but now Minority Affairs.",
            "why_b_ta": "முன்பு இது உள்துறை மற்றும் பின்னர் சமூக நீதி அமைச்சகத்தின் கீழ் இருந்தது, ஆனால் தற்போது சிறுபான்மையினர் விவகார அமைச்சகத்தில் உள்ளது.",
            "why_c_en": "Ministry of Education deals with school curricula and Three-Language Formula.",
            "why_c_ta": "கல்வி அமைச்சகம் பள்ளிப் பாடத்திட்டம் மற்றும் மும்மொழிக் கொள்கையைக் கையாள்கிறது.",
            "why_d_en": "Ministry of Law deals with legal drafting and court languages.",
            "why_d_ta": "சட்ட அமைச்சகம் சட்ட வரைவு மற்றும் நீதிமன்ற மொழிகளைக் கையாள்கிறது.",
            "tip_en": "Commissioner for Linguistic Minorities: HQ at Prayagraj; Ministry of Minority Affairs.",
            "tip_ta": "மொழிச் சிறுபான்மையினர் ஆணையர்: தலைமையிடம் பிரயாக்ராஜ்; சிறுபான்மையினர் விவகார அமைச்சகம்.",
            "fact_en": "Regional offices of the Commissioner are located at Belgaum, Chennai, and Kolkata.",
            "fact_ta": "ஆணையரின் மண்டல அலுவலகங்கள் பெல்காம், சென்னை மற்றும் கொல்கத்தாவில் அமைந்துள்ளன."
        },
        # 44
        {
            "subtopic": "Regional Offices of Linguistic Minorities Commissioner",
            "stem_en": "Which of the following cities hosts a Regional Office of the Commissioner for Linguistic Minorities?",
            "stem_ta": "பின்வரும் நகரங்களில் மொழிச் சிறுபான்மையினருக்கான ஆணையரின் மண்டல அலுவலகம் அமைந்துள்ள நகரம் எது?",
            "options": [
                ("Chennai", "சென்னை"),
                ("Mumbai", "மும்பை"),
                ("Bengaluru", "பெங்களூரு"),
                ("Hyderabad", "ஹைதராபாத்")
            ],
            "correct_key": "A",
            "exp_en": "The Commissioner for Linguistic Minorities has three Regional Offices: Belgaum (Karnataka), Chennai (Tamil Nadu), and Kolkata (West Bengal), with headquarters at Prayagraj.",
            "exp_ta": "மொழிச் சிறுபான்மையினருக்கான ஆணையருக்கு மூன்று மண்டல அலுவலகங்கள் உள்ளன: பெல்காம் (கர்நாடகா), சென்னை (தமிழ்நாடு) மற்றும் கொல்கத்தா (மேற்கு வங்காளம்), இதன் தலைமையகம் பிரயாக்ராஜில் உள்ளது.",
            "why_a_en": "Chennai is one of the three designated regional offices.",
            "why_a_ta": "சென்னை என்பது மூன்று குறிப்பிட்ட மண்டல அலுவலகங்களில் ஒன்றாகும்.",
            "why_b_en": "Mumbai does not have a regional office of the Commissioner.",
            "why_b_ta": "மும்பையில் ஆணையரின் மண்டல அலுவலகம் இல்லை.",
            "why_c_en": "Bengaluru is not a regional office; Belgaum was selected for Karnataka.",
            "why_c_ta": "பெங்களூருவில் மண்டல அலுவலகம் இல்லை; கர்நாடகாவிற்கு பெல்காம் தேர்ந்தெடுக்கப்பட்டது.",
            "why_d_en": "Hyderabad does not host a regional office.",
            "why_d_ta": "ஹைதராபாத்தில் மண்டல அலுவலகம் இல்லை.",
            "tip_en": "CLM Offices: HQ = Prayagraj (Allahabad); Regional = Chennai, Belgaum, Kolkata.",
            "tip_ta": "CLM அலுவலகங்கள்: தலைமையிடம் = பிரயாக்ராஜ்; மண்டலம் = சென்னை, பெல்காம், கொல்கத்தா.",
            "fact_en": "The Southern zone regional office in Chennai monitors linguistic minority safeguards across southern states.",
            "fact_ta": "சென்னையில் உள்ள தென்மண்டல அலுவலகம் தென்மாநிலங்களில் உள்ள மொழிச் சிறுபான்மையினரின் பாதுகாப்பைக் கண்காணிக்கிறது."
        },
        # 45
        {
            "subtopic": "Four Chapters of Part XVII",
            "stem_en": "How many chapters are there in Part XVII of the Constitution of India?",
            "stem_ta": "இந்திய அரசியலமைப்பின் பகுதி XVII-ல் எத்தனை அத்தியாயங்கள் உள்ளன?",
            "options": [
                ("Four chapters", "நான்கு அத்தியாயங்கள்"),
                ("Three chapters", "மூன்று அத்தியாயங்கள்"),
                ("Five chapters", "ஐந்து அத்தியாயங்கள்"),
                ("Two chapters", "இரண்டு அத்தியாயங்கள்")
            ],
            "correct_key": "A",
            "exp_en": "Part XVII is divided into four chapters: Chapter I (Language of the Union), Chapter II (Regional Languages), Chapter III (Language of the Judiciary & Texts of Bills), Chapter IV (Special Directives).",
            "exp_ta": "பகுதி XVII நான்கு அத்தியாயங்களாகப் பிரிக்கப்பட்டுள்ளது: அத்தியாயம் I (ஒன்றியத்தின் மொழி), அத்தியாயம் II (வட்டார மொழிகள்), அத்தியாயம் III (நீதித்துறை மற்றும் மசோதாக்களின் மொழி), அத்தியாயம் IV (சிறப்பு வழிகாட்டுதல்கள்).",
            "why_a_en": "Part XVII contains exactly Chapters I, II, III, and IV.",
            "why_a_ta": "பகுதி XVII சரியாக அத்தியாயங்கள் I, II, III மற்றும் IV ஆகியவற்றைக் கொண்டுள்ளது.",
            "why_b_en": "Three chapters does not include Chapter IV (Special Directives).",
            "why_b_ta": "மூன்று அத்தியாயங்கள் என்பது அத்தியாயம் IV-ஐ உள்ளடக்காது.",
            "why_c_en": "There is no Chapter V in Part XVII.",
            "why_c_ta": "பகுதி XVII-ல் அத்தியாயம் V இல்லை.",
            "why_d_en": "Two chapters is an incomplete division.",
            "why_d_ta": "இரண்டு அத்தியாயங்கள் என்பது முழுமையற்ற பகுப்பாகும்.",
            "tip_en": "Part XVII Chapters: Ch I (343-344), Ch II (345-347), Ch III (348-349), Ch IV (350-351).",
            "tip_ta": "பகுதி XVII அத்தியாயங்கள்: அத் I (343-344), அத் II (345-347), அத் III (348-349), அத் IV (350-351).",
            "fact_en": "Each chapter covers a distinct functional dimension of official language governance.",
            "fact_ta": "ஒவ்வொரு அத்தியாயமும் அதிகாரப்பூர்வ மொழி நிர்வாகத்தின் தனித்துவமான செயல்பாட்டுப் பரிமாணத்தை உள்ளடக்கியுள்ளது."
        },
        # 46
        {
            "subtopic": "Chapter III Scope",
            "stem_en": "Which Articles are contained in Chapter III of Part XVII of the Constitution of India?",
            "stem_ta": "இந்திய அரசியலமைப்பின் பகுதி XVII-ன் அத்தியாயம் III-ல் உள்ள சரத்துகள் எவை?",
            "options": [
                ("Articles 348 and 349", "சரத்துகள் 348 மற்றும் 349"),
                ("Articles 343 and 344", "சரத்துகள் 343 மற்றும் 344"),
                ("Articles 345, 346, and 347", "சரத்துகள் 345, 346 மற்றும் 347"),
                ("Articles 350, 350A, 350B, and 351", "சரத்துகள் 350, 350A, 350B மற்றும் 351")
            ],
            "correct_key": "A",
            "exp_en": "Chapter III (entitled 'Language of the Supreme Court, High Courts, etc.') consists of Articles 348 and 349.",
            "exp_ta": "அத்தியாயம் III ('உச்ச நீதிமன்றம், உயர் நீதிமன்றங்கள் போன்றவற்றின் மொழி') சரத்துகள் 348 மற்றும் 349 ஆகியவற்றைக் கொண்டுள்ளது.",
            "why_a_en": "Articles 348 and 349 form Chapter III governing judicial and legislative enactment languages.",
            "why_a_ta": "சரத்துகள் 348 மற்றும் 349 நீதித்துறை மற்றும் சட்டமியற்றும் மொழிகளை ஒழுங்குபடுத்தும் அத்தியாயம் III ஆகும்.",
            "why_b_en": "Articles 343 and 344 constitute Chapter I (Language of the Union).",
            "why_b_ta": "சரத்துகள் 343 மற்றும் 344 அத்தியாயம் I (ஒன்றியத்தின் மொழி) ஆகும்.",
            "why_c_en": "Articles 345, 346, and 347 constitute Chapter II (Regional Languages).",
            "why_c_ta": "சரத்துகள் 345, 346 மற்றும் 347 அத்தியாயம் II (வட்டார மொழிகள்) ஆகும்.",
            "why_d_en": "Articles 350 to 351 constitute Chapter IV (Special Directives).",
            "why_d_ta": "சரத்துகள் 350 முதல் 351 வரை அத்தியாயம் IV (சிறப்பு வழிகாட்டுதல்கள்) ஆகும்.",
            "tip_en": "Chapter III = Judiciary & Bills (348-349).",
            "tip_ta": "அத்தியாயம் III = நீதித்துறை & மசோதாக்கள் (348-349).",
            "fact_en": "Article 348 is often called the 'Judicial Language Code' of the Constitution.",
            "fact_ta": "சரத்து 348 பெரும்பாலும் அரசியலமைப்பின் 'நீதித்துறை மொழிக் குறியீடு' என்று அழைக்கப்படுகிறது."
        },
        # 47
        {
            "subtopic": "Section 3 of Official Languages Act 1963",
            "stem_en": "Under Section 3 of the Official Languages Act, 1963, for which two bodies must resolutions, general orders, rules, notifications, and contracts be in both Hindi and English?",
            "stem_ta": "அதிகாரப்பூர்வ மொழிகள் சட்டம் 1963-ன் பிரிவு 3-ன் கீழ், தீர்மானங்கள், பொது ஆணைகள், விதிகள், அறிவிப்புகள் மற்றும் ஒப்பந்தங்கள் இந்தி மற்றும் ஆங்கிலம் ஆகிய இரண்டிலும் கட்டாயமாக இருக்க வேண்டியது எங்கு?",
            "options": [
                ("Both Houses of Parliament and Central Government offices", "நாடாளுமன்றத்தின் இரு அவைகள் மற்றும் மத்திய அரசு அலுவலகங்கள்"),
                ("Only State Legislative Assemblies", "மாநில சட்டமன்றப் பேரவைகள் மட்டுமே"),
                ("Only Village Panchayats", "கிராம ஊராட்சிகள் மட்டுமே"),
                ("Only Municipal Corporations", "மாநகராட்சிகள் மட்டுமே")
            ],
            "correct_key": "A",
            "exp_en": "Section 3(3) of the Act mandates that both Hindi and English shall be used for resolutions, general orders, rules, notifications, administrative reports, press communiques, contracts, and tenders of Central Government and Parliament.",
            "exp_ta": "சட்டத்தின் பிரிவு 3(3), மத்திய அரசு மற்றும் நாடாளுமன்றத்தின் தீர்மானங்கள், பொது ஆணைகள், விதிகள், அறிவிப்புகள், நிர்வாக அறிக்கைகள், ஒப்பந்தங்கள் மற்றும் ஒப்பந்தப்புள்ளிகள் இந்தி மற்றும் ஆங்கிலம் ஆகிய இரண்டிலும் பயன்படுத்தப்பட வேண்டும் எனக் கட்டாயமாக்குகிறது.",
            "why_a_en": "Section 3(3) imposes the statutory obligation of bilingualism on Central Government and Parliament.",
            "why_a_ta": "பிரிவு 3(3) மத்திய அரசு மற்றும் நாடாளுமன்றத்தின் மீது இருமொழிப் பயன்பாட்டின் சட்டப்பூர்வக் கடமையை விதிக்கிறது.",
            "why_b_en": "State Legislatures are governed by state official language acts under Article 345.",
            "why_b_ta": "மாநில சட்டமன்றங்கள் சரத்து 345-ன் கீழான மாநில மொழிச் சட்டங்களால் ஆளப்படுகின்றன.",
            "why_c_en": "Village Panchayats are local bodies governed by State Panchayati Raj Acts.",
            "why_c_ta": "கிராம ஊராட்சிகள் மாநில ஊராட்சிச் சட்டங்களால் நிர்வகிக்கப்படுகின்றன.",
            "why_d_en": "Municipal Corporations are local bodies under State Municipal Acts.",
            "why_d_ta": "மாநகராட்சிகள் மாநில நகராட்சிச் சட்டங்களின் கீழான உள்ளாட்சி அமைப்புகளாகும்.",
            "tip_en": "Section 3(3) list: 14 categories of official documents MUST be bilingual (Hindi + English).",
            "tip_ta": "பிரிவு 3(3) பட்டியல்: 14 வகையான அதிகாரப்பூர்வ ஆவணங்கள் கட்டாயமாக இருமொழிகளிலும் (இந்தி + ஆங்கிலம்) இருக்க வேண்டும்.",
            "fact_en": "Violation of Section 3(3) bilingual mandate can be challenged before administrative tribunals.",
            "fact_ta": "பிரிவு 3(3) இருமொழி ஆணையை மீறுவது நிர்வாகத் தீர்ப்பாயங்களில் கேள்விக்குள்ளாக்கப்படலாம்."
        },
        # 48
        {
            "subtopic": "Classical Language Criteria - Antiquity",
            "stem_en": "According to the Government of India criteria, what is the recorded history or antiquity required for early texts of a language to qualify for Classical Language status?",
            "stem_ta": "இந்திய அரசின் அளவுகோல்களின்படி, ஒரு மொழி செம்மொழி அந்தஸ்தைப் பெறுவதற்கு அதன் ஆரம்பகால நூல்களின் பதிவு செய்யப்பட்ட வரலாறு அல்லது பழமை எவ்வளவு காலம் இருக்க வேண்டும்?",
            "options": [
                ("1500 to 2000 years", "1500 முதல் 2000 ஆண்டுகள்"),
                ("500 to 800 years", "500 முதல் 800 ஆண்டுகள்"),
                ("2500 to 3000 years", "2500 முதல் 3000 ஆண்டுகள்"),
                ("100 to 200 years", "100 முதல் 200 ஆண்டுகள்")
            ],
            "correct_key": "A",
            "exp_en": "The Ministry of Culture criteria stipulate high antiquity of early texts/recorded history over a period of 1500–2000 years for conferring Classical Language status.",
            "exp_ta": "செம்மொழி அந்தஸ்து வழங்குவதற்கு, ஒரு மொழியின் ஆரம்பகால நூல்கள்/பதிவுசெய்யப்பட்ட வரலாறு 1500-2000 ஆண்டுகள் பழமையானதாக இருக்க வேண்டும் என்று கலாச்சார அமைச்சகத்தின் அளவுகோல் நிபந்தனை விதிக்கிறது.",
            "why_a_en": "1500-2000 years is the official antiquity benchmark established in 2004/2005.",
            "why_a_ta": "1500-2000 ஆண்டுகள் என்பது 2004/2005-ல் நிறுவப்பட்ட அதிகாரப்பூர்வ பழமை அளவுகோலாகும்.",
            "why_b_en": "500-800 years is insufficient for classical language status.",
            "why_b_ta": "500-800 ஆண்டுகள் என்பது செம்மொழி அந்தஸ்திற்குப் போதுமானதல்ல.",
            "why_c_en": "2500-3000 years is not the mandatory minimum requirement.",
            "why_c_ta": "2500-3000 ஆண்டுகள் என்பது கட்டாய குறைந்தபட்ச நிபந்தனை அல்ல.",
            "why_d_en": "100-200 years relates to modern languages.",
            "why_d_ta": "100-200 ஆண்டுகள் நவீன மொழிகளுடன் தொடர்புடையது.",
            "tip_en": "Classical Criteria: Antiquity (1500-2000 yrs), Ancient literature/valuable heritage, Original literary tradition.",
            "tip_ta": "செம்மொழி அளவுகோல்கள்: பழமை (1500-2000 ஆண்டுகள்), பண்டைய இலக்கியம்/மதிப்புமிக்க பாரம்பரியம், அசல் இலக்கிய மரபு.",
            "fact_en": "Sangam literature easily satisfied the 2000-year antiquity criterion for Tamil.",
            "fact_ta": "சங்க இலக்கியங்கள் தமிழின் 2000 ஆண்டுகாலப் பழமை அளவுகோலை மிக எளிதாக நிறைவு செய்தன."
        },
        # 49
        {
            "subtopic": "Three-Language Formula Origin",
            "stem_en": "The Three-Language Formula was first formulated by which body in 1956?",
            "stem_ta": "மும்மொழிக் கொள்கை முதன்முதலில் 1956-ல் எந்த அமைப்பால் உருவாக்கப்பட்டது?",
            "options": [
                ("Central Advisory Board of Education (CABE)", "மத்தியக் கல்வி ஆலோசனைக் குழு (CABE)"),
                ("University Grants Commission (UGC)", "பல்கலைக்கழக மானியக் குழு (UGC)"),
                ("Planning Commission", "திட்டக் குழு"),
                ("Union Public Service Commission (UPSC)", "மத்திய அரசுப் பணியாளர் தேர்வாணையம் (UPSC)")
            ],
            "correct_key": "A",
            "exp_en": "The Three-Language Formula was devised by the Central Advisory Board of Education (CABE) in 1956 and later incorporated into the National Policy on Education, 1968.",
            "exp_ta": "மும்மொழிக் கொள்கை 1956-ல் மத்தியக் கல்வி ஆலோசனைக் குழுவால் (CABE) உருவாக்கப்பட்டு, பின்னர் 1968-ன் தேசியக் கல்விக் கொள்கையில் சேர்க்கப்பட்டது.",
            "why_a_en": "CABE formulated the Three-Language Formula in 1956.",
            "why_a_ta": "CABE 1956-ல் மும்மொழிக் கொள்கையை உருவாக்கியது.",
            "why_b_en": "UGC deals with higher education standards, not school language formula.",
            "why_b_ta": "UGC உயர் கல்வித் தரங்களைக் கையாள்கிறது, பள்ளி மொழிக் கொள்கையை அல்ல.",
            "why_c_en": "Planning Commission focused on five-year economic plans.",
            "why_c_ta": "திட்டக் குழு ஐந்தாண்டு பொருளாதாரத் திட்டங்களில் கவனம் செலுத்தியது.",
            "why_d_en": "UPSC conducts civil services and defense recruitment examinations.",
            "why_d_ta": "UPSC குடிமைப்பணிகள் மற்றும் பாதுகாப்பு ஆள்தேர்வுத் தேர்வுகளை நடத்துகிறது.",
            "tip_en": "Three-Language Formula: Devised by CABE (1956); Endorsed by CMs Conference (1961); Adopted in NPE (1968).",
            "tip_ta": "மும்மொழிக் கொள்கை: CABE (1956) உருவாக்கியது; முதலமைச்சர்கள் மாநாடு (1961) ஆதரித்தது; NPE (1968) ஏற்றுக்கொண்டது.",
            "fact_en": "Tamil Nadu rejected the Three-Language Formula in 1968 in favor of the Two-Language Formula.",
            "fact_ta": "தமிழ்நாடு 1968-ல் மும்மொழிக் கொள்கையை நிராகரித்து இருமொழிக் கொள்கையை ஏற்றுக்கொண்டது."
        },
        # 50
        {
            "subtopic": "Sanskrit in the Eighth Schedule",
            "stem_en": "Is Sanskrit an official language of the Union, a scheduled language in the Eighth Schedule, or both?",
            "stem_ta": "சமஸ்கிருதம் ஒன்றியத்தின் அதிகாரப்பூர்வ மொழியா, எட்டாவது அட்டவணையில் உள்ள அட்டவணை மொழியா அல்லது இரண்டுமா?",
            "options": [
                ("It is an Eighth Schedule language and a Classical Language, but NOT an official language of the Union", "இது எட்டாவது அட்டவணை மொழி மற்றும் செம்மொழி, ஆனால் ஒன்றியத்தின் அதிகாரப்பூர்வ மொழி அல்ல"),
                ("It is the sole official language of the Union", "இது ஒன்றியத்தின் ஒரே அதிகாரப்பூர்வ மொழி"),
                ("It is an official language of the Union alongside Hindi", "இது இந்தியுடன் இணைந்த ஒன்றியத்தின் அதிகாரப்பூர்வ மொழி"),
                ("It has no constitutional status under Part XVII", "பகுதி XVII-ன் கீழ் இதற்கு எந்த அரசியலமைப்பு அந்தஸ்தும் இல்லை")
            ],
            "correct_key": "A",
            "exp_en": "Sanskrit is an Eighth Schedule language and was declared a Classical Language in 2005. It is NOT an official language of the Union (which is Hindi in Devanagari script alongside English). However, Uttarakhand adopted Sanskrit as its second official language.",
            "exp_ta": "சமஸ்கிருதம் எட்டாவது அட்டவணை மொழியாகும் மற்றும் 2005-ல் செம்மொழியாக அறிவிக்கப்பட்டது. இது ஒன்றியத்தின் அதிகாரப்பூர்வ மொழி அல்ல (ஒன்றியத்தின் மொழி இந்தி மற்றும் ஆங்கிலம் மட்டுமே). இருப்பினும், உத்தராகண்ட் சமஸ்கிருதத்தைத் தனது இரண்டாவது அதிகாரப்பூர்வ மொழியாக ஏற்றுக்கொண்டது.",
            "why_a_en": "Sanskrit is in the Eighth Schedule and is Classical, but not the Union official language.",
            "why_a_ta": "சமஸ்கிருதம் எட்டாவது அட்டவணையில் உள்ளது மற்றும் செம்மொழி அந்தஸ்து பெற்றது, ஆனால் ஒன்றியத்தின் அதிகாரப்பூர்வ மொழி அல்ல.",
            "why_b_en": "Hindi in Devanagari is the official language of the Union under Article 343(1).",
            "why_b_ta": "சரத்து 343(1)-ன் கீழ் தேவநாகரி இந்தி ஒன்றியத்தின் அதிகாரப்பூர்வ மொழியாகும்.",
            "why_c_en": "Sanskrit is not designated as a Union official language alongside Hindi.",
            "why_c_ta": "சமஸ்கிருதம் இந்திக்கு இணையாக ஒன்றிய அதிகாரப்பூர்வ மொழியாக நியமிக்கப்படவில்லை.",
            "why_d_en": "Article 351 specifically mentions Sanskrit as the primary vocabulary source.",
            "why_d_ta": "சரத்து 351 சமஸ்கிருதத்தை முதன்மை சொல்லகராதி ஆதாரமாகக் குறிப்பிடுகிறது.",
            "tip_en": "Constitutional Status: Sanskrit is an 8th Schedule language, Classical language (2005), and Art 351 vocabulary source.",
            "tip_ta": "அரசியலமைப்பு அந்தஸ்து: சமஸ்கிருதம் 8-வது அட்டவணை மொழி, செம்மொழி (2005) மற்றும் சரத்து 351 சொல்லகராதி ஆதாரம்.",
            "fact_en": "Sanskrit is also the second official language of Uttarakhand and Himachal Pradesh.",
            "fact_ta": "சமஸ்கிருதம் உத்தராகண்ட் மற்றும் இமாச்சலப் பிரதேசத்தின் இரண்டாவது அதிகாரப்பூர்வ மொழியாகவும் உள்ளது."
        }
    ]

    questions = []
    for idx, item in enumerate(raw_data, start=1):
        qid = f"OL_E_{idx:03d}"
        opts = item["options"]
        correct_key = item["correct_key"]
        q = make_ol_q(
            qid=qid,
            diff="Easy",
            qtype="conceptual",
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
            tags=["polity", "official_language", "easy", item["subtopic"].lower().replace(" ", "_")]
        )
        questions.append(q)
    return questions

def build_easy_file():
    qs = get_easy_questions()
    print(f"Generated {len(qs)} raw Easy questions for Official Language.")
    balanced = randomize_and_balance_dataset(qs, seed=42)
    
    out_dir = os.path.join("data", "questions", "polity")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "official_language_easy.json")
    
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(balanced, f, ensure_ascii=False, indent=2)
    print(f"Saved balanced Easy MCQs to {out_path}")
    
    rep = ContentValidator.validate_file(out_path, expected_count=50, expected_prefix="OL_E_")
    print(f"Validation: {'PASS' if rep.is_valid else 'FAIL'} | Total: {rep.total_audited}")
    print(f"Keys: {rep.key_distribution}")
    if not rep.is_valid:
        for iss in rep.issues:
            print("  Issue:", iss.severity, iss.field_name, iss.message)
    return rep.is_valid

if __name__ == "__main__":
    build_easy_file()
