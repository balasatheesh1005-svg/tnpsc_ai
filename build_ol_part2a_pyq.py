# -*- coding: utf-8 -*-
"""
Official Language - Part 2A PYQ Practice MCQs Generator (50 MCQs: OL_PYQ_001 to OL_PYQ_050)
Strictly adheres to:
- 24 required fields schema
- TNPSC Past Year Questions & Standard Pattern Simulations
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

def get_pyq_questions():
    raw_data = [
        # 1
        {
            "subtopic": "Union Official Language Constitutional Basis",
            "stem_en": "[TNPSC Group 4 2014, Group 2 2016]\nUnder Article 343(1) of the Indian Constitution, what is declared as the official language of the Union?",
            "stem_ta": "[TNPSC குரூப் 4 2014, குரூப் 2 2016]\nஇந்திய அரசியலமைப்பின் சரத்து 343(1)-ன் கீழ் ஒன்றியத்தின் அதிகாரப்பூர்வ மொழியாக அறிவிக்கப்பட்டது எது?",
            "options": [
                ("Hindi in Devanagari script", "தேவநாகரி வரிவடிவத்திலான இந்தி"),
                ("Hindi in Roman script", "ரோமன் வரிவடிவத்திலான இந்தி"),
                ("Hindustani in Persian script", "பாரசீக வரிவடிவத்திலான இந்துஸ்தானி"),
                ("Sanskrit in Devanagari script", "தேவநாகரி வரிவடிவத்திலான சமஸ்கிருதம்")
            ],
            "correct_key": "A",
            "exp_en": "Article 343(1) states: 'The official language of the Union shall be Hindi in Devanagari script. The form of numerals to be used for the official purposes of the Union shall be the international form of Indian numerals.'",
            "exp_ta": "சரத்து 343(1) குறிப்பிடுகிறது: 'ஒன்றியத்தின் அதிகாரப்பூர்வ மொழி தேவநாகரி வரிவடிவத்திலான இந்தியாகும். ஒன்றியத்தின் பயன்பாட்டிற்கான எண்கள் இந்திய எண்களின் பன்னாட்டு வடிவமாக இருக்கும்.'",
            "why_a_en": "Article 343(1) specifies Hindi in Devanagari script as the official language.",
            "why_a_ta": "சரத்து 343(1) தேவநாகரி வரிவடிவத்திலான இந்தியை அதிகாரப்பூர்வ மொழியாகக் குறிப்பிடுகிறது.",
            "why_b_en": "The script prescribed is Devanagari, not Roman.",
            "why_b_ta": "பரிந்துரைக்கப்பட்ட வரிவடிவம் தேவநாகரி, ரோமன் அல்ல.",
            "why_c_en": "Hindustani was rejected during Constituent Assembly debates in favor of Hindi in Devanagari script.",
            "why_c_ta": "அரசியலமைப்பு நிர்ணய சபை விவாதங்களில் இந்துஸ்தானி நிராகரிக்கப்பட்டு தேவநாகரி இந்தியே ஏற்கப்பட்டது.",
            "why_d_en": "Sanskrit is an Eighth Schedule classical language, not the Union official language.",
            "why_d_ta": "சமஸ்கிருதம் எட்டாவது அட்டவணை செம்மொழி, ஒன்றியத்தின் அதிகாரப்பூர்வ மொழி அல்ல.",
            "tip_en": "PYQ Repeat: Article 343(1) contains two elements: Hindi in Devanagari script + International form of Indian numerals.",
            "tip_ta": "முந்தைய வினா குறிப்பு: சரத்து 343(1) இரண்டு கூறுகளைக் கொண்டது: தேவநாகரி இந்தி + பன்னாட்டு வடிவிலான இந்திய எண்கள்.",
            "fact_en": "Adopted on September 14, 1949 by the Constituent Assembly (celebrated as Hindi Diwas).",
            "fact_ta": "செப்டம்பர் 14, 1949 அன்று அரசியலமைப்பு நிர்ணய சபையால் ஏற்கப்பட்டது (இந்தி தினமாகக் கொண்டாடப்படுகிறது)."
        },
        # 2
        {
            "subtopic": "English 15-Year Transition Period",
            "stem_en": "[TNPSC Group 1 2015, Group 4 2018]\nFor how many years from the commencement of the Constitution was English authorized to continue for all official purposes of the Union under Article 343(2)?",
            "stem_ta": "[TNPSC குரூப் 1 2015, குரூப் 4 2018]\nசரத்து 343(2)-ன் கீழ் அரசியலமைப்பு அமலுக்கு வந்ததிலிருந்து எத்தனை ஆண்டுகளுக்கு ஒன்றியத்தின் அனைத்து அதிகாரப்பூர்வ பயன்பாடுகளுக்கும் ஆங்கிலம் தொடர அனுமதிக்கப்பட்டது?",
            "options": [
                ("15 years", "15 ஆண்டுகள்"),
                ("10 years", "10 ஆண்டுகள்"),
                ("20 years", "20 ஆண்டுகள்"),
                ("25 years", "25 ஆண்டுகள்")
            ],
            "correct_key": "A",
            "exp_en": "Article 343(2) provided that for a period of 15 years from the commencement of the Constitution (i.e., from 26 January 1950 to 25 January 1965), English language shall continue to be used for all official purposes of the Union.",
            "exp_ta": "சரத்து 343(2)-ன் படி அரசியலமைப்பு நடைமுறைக்கு வந்ததிலிருந்து 15 ஆண்டுகளுக்கு (26 ஜனவரி 1950 முதல் 25 ஜனவரி 1965 வரை) ஒன்றியத்தின் அனைத்து அதிகாரப்பூர்வ பயன்பாடுகளுக்கும் ஆங்கிலம் தொடர்ந்து பயன்பாட்டில் இருக்கும்.",
            "why_a_en": "Article 343(2) fixed 15 years as the transitional window.",
            "why_a_ta": "சரத்து 343(2) 15 ஆண்டுகளை இடைக்காலக் காலக்கெடுவாக நிர்ணயித்தது.",
            "why_b_en": "10 years applied to reservations under Article 334, not English under 343(2).",
            "why_b_ta": "10 ஆண்டுகள் சரத்து 334 இடஒதுக்கீட்டுக்குரியது, சரத்து 343(2) ஆங்கிலத்திற்குரியது அல்ல.",
            "why_c_en": "20 years was not the constitutional period specified.",
            "why_c_ta": "20 ஆண்டுகள் அரசியலமைப்பில் குறிப்பிடப்பட்ட காலம் அல்ல.",
            "why_d_en": "25 years is an incorrect distractor.",
            "why_d_ta": "25 ஆண்டுகள் தவறான விடை.",
            "tip_en": "15-year transition expired on 25 January 1965, prompting the Official Languages Act 1963.",
            "tip_ta": "15 ஆண்டு காலம் 25 ஜனவரி 1965 அன்று முடிவடைந்தது, இது அதிகாரப்பூர்வ மொழிகள் சட்டம் 1963-ஐ இயற்ற வழிவகுத்தது.",
            "fact_en": "Article 343(3) empowered Parliament to provide by law for the continued use of English beyond 15 years.",
            "fact_ta": "சரத்து 343(3) 15 ஆண்டுகளுக்குப் பிறகும் ஆங்கிலத்தைத் தொடர நாடாளுமன்றத்திற்கு சட்டமியற்றும் அதிகாரத்தை வழங்கியது."
        },
        # 3
        {
            "subtopic": "First Official Language Commission",
            "stem_en": "[TNPSC Group 2 2013, Group 1 2017]\nWho was appointed as the Chairman of the First Official Language Commission constituted by the President of India in 1955 under Article 344(1)?",
            "stem_ta": "[TNPSC குரூப் 2 2013, குரூப் 1 2017]\nசரத்து 344(1)-ன் கீழ் 1955-ல் இந்தியக் குடியரசுத் தலைவரால் அமைக்கப்பட்ட முதலாவது அதிகாரப்பூர்வ மொழி ஆணையத்தின் தலைவராக நியமிக்கப்பட்டவர் யார்?",
            "options": [
                ("B.G. Kher", "பி.ஜி. கேர்"),
                ("Govind Ballabh Pant", "கோவிந்த் வல்லப் பந்த்"),
                ("Suniti Kumar Chatterji", "சுனிதி குமார் சட்டர்ஜி"),
                ("P. Subbarayan", "பி. சுப்பராயன்")
            ],
            "correct_key": "A",
            "exp_en": "The First Official Language Commission was appointed by President Dr. Rajendra Prasad in June 1955 under the chairmanship of B.G. Kher (former Chief Minister of Bombay).",
            "exp_ta": "முதலாவது அதிகாரப்பூர்வ மொழி ஆணையம் ஜூன் 1955-ல் குடியரசுத் தலைவர் டாக்டர் ராஜேந்திர பிரசாத்தால் பி.ஜி. கேர் (பம்பாயின் முன்னாள் முதல்வர்) தலைமையில் அமைக்கப்பட்டது.",
            "why_a_en": "B.G. Kher headed the 1955 Commission and submitted its report in 1956.",
            "why_a_ta": "பி.ஜி. கேர் 1955 ஆணையத்திற்குத் தலைமை தாங்கி 1956-ல் அறிக்கை சமர்ப்பித்தார்.",
            "why_b_en": "G.B. Pant headed the 1957 Parliamentary Committee that examined the Kher Commission report.",
            "why_b_ta": "ஜி.பி. பந்த் கேர் ஆணைய அறிக்கையை ஆய்வு செய்த 1957 நாடாளுமன்றக் குழுவிற்குத் தலைமை தாங்கினார்.",
            "why_c_en": "Dr. Suniti Kumar Chatterji was a dissenting member of the Kher Commission, not chairman.",
            "why_c_ta": "டாக்டர் சுனிதி குமார் சட்டர்ஜி கேர் ஆணையத்தின் மாறுபட்ட கருத்துடைய உறுப்பினர், தலைவர் அல்ல.",
            "why_d_en": "Dr. P. Subbarayan (from Tamil Nadu) was a member who submitted a minute of dissent.",
            "why_d_ta": "டாக்டர் பி. சுப்பராயன் (தமிழ்நாடு) மாறுபட்ட குறிப்பை சமர்ப்பித்த உறுப்பினர் ஆவார்.",
            "tip_en": "Remember: Kher = 1955 Commission; Pant = 1957 Parliamentary Committee.",
            "tip_ta": "நினைவில் கொள்க: கேர் = 1955 ஆணையம்; பந்த் = 1957 நாடாளுமன்றக் குழு.",
            "fact_en": "Both Dr. P. Subbarayan and Dr. S.K. Chatterji submitted dissenting minutes against rapid Hindi imposition.",
            "fact_ta": "டாக்டர் பி. சுப்பராயன் மற்றும் டாக்டர் எஸ்.கே. சட்டர்ஜி ஆகிய இருவரும் அவசர இந்தி திணிப்புக்கு எதிராக மாறுபட்ட குறிப்புகளை சமர்ப்பித்தனர்."
        },
        # 4
        {
            "subtopic": "Parliamentary Committee on Official Language Structure",
            "stem_en": "[TNPSC Group 1 2019, Group 2 2018]\nWhat is the total membership of the Committee of Parliament on Official Language constituted under Article 344(4)?",
            "stem_ta": "[TNPSC குரூப் 1 2019, குரூப் 2 2018]\nசரத்து 344(4)-ன் கீழ் அமைக்கப்பட்ட அதிகாரப்பூர்வ மொழிக்கான நாடாளுமன்றக் குழுவின் மொத்த உறுப்பினர்களின் எண்ணிக்கை எவ்வளவு?",
            "options": [
                ("30 members (20 Lok Sabha + 10 Rajya Sabha)", "30 உறுப்பினர்கள் (20 மக்களவை + 10 மாநிலங்களவை)"),
                ("22 members (15 Lok Sabha + 7 Rajya Sabha)", "22 உறுப்பினர்கள் (15 மக்களவை + 7 மாநிலங்களவை)"),
                ("15 members (10 Lok Sabha + 5 Rajya Sabha)", "15 உறுப்பினர்கள் (10 மக்களவை + 5 மாநிலங்களவை)"),
                ("31 members (21 Lok Sabha + 10 Rajya Sabha)", "31 உறுப்பினர்கள் (21 மக்களவை + 10 மாநிலங்களவை)")
            ],
            "correct_key": "A",
            "exp_en": "Article 344(4) mandates that the Committee shall consist of 30 members, of whom 20 shall be members of the House of the People (Lok Sabha) and 10 shall be members of the Council of States (Rajya Sabha).",
            "exp_ta": "சரத்து 344(4) அக்குழுவில் 30 உறுப்பினர்கள் இருப்பார்கள் என்று விதிக்கிறது; இதில் 20 பேர் மக்களவையிலிருந்தும், 10 பேர் மாநிலங்களவையிலிருந்தும் தேர்ந்தெடுக்கப்படுவர்.",
            "why_a_en": "30 members (20 Lok Sabha and 10 Rajya Sabha) is the exact constitutional composition.",
            "why_a_ta": "30 உறுப்பினர்கள் (20 மக்களவை மற்றும் 10 மாநிலங்களவை) துல்லியமான அரசியலமைப்பு அமைப்பாகும்.",
            "why_b_en": "22 members (15+7) is the composition of the Public Accounts Committee and Committee on Public Undertakings.",
            "why_b_ta": "22 உறுப்பினர்கள் (15+7) என்பது பொதுக் கணக்குக் குழு மற்றும் பொதுத்துறை நிறுவனங்கள் குழுவின் அமைப்பாகும்.",
            "why_c_en": "15 members is not the size of this committee.",
            "why_c_ta": "15 உறுப்பினர்கள் என்பது இக்குழுவின் அளவு அல்ல.",
            "why_d_en": "31 members is typical of Departmentally Related Standing Committees.",
            "why_d_ta": "31 உறுப்பினர்கள் துறை சார்ந்த நிலைக்குழுக்களுக்கு உரியது.",
            "tip_en": "Composition ratio is 2:1 (20 from Lok Sabha, 10 from Rajya Sabha).",
            "tip_ta": "உறுப்பினர் விகிதம் 2:1 (மக்களவையில் இருந்து 20, மாநிலங்களவையில் இருந்து 10).",
            "fact_en": "Elected by proportional representation by means of the single transferable vote.",
            "fact_ta": "ஒற்றை மாற்று வாக்கு மூலம் விகிதாச்சார பிரதிநிதித்துவ முறையில் தேர்ந்தெடுக்கப்படுகின்றனர்."
        },
        # 5
        {
            "subtopic": "21st Constitutional Amendment Act 1967",
            "stem_en": "[TNPSC Group 4 2016, Group 2 2015]\nWhich language was added to the Eighth Schedule of the Constitution of India by the 21st Constitutional Amendment Act, 1967?",
            "stem_ta": "[TNPSC குரூப் 4 2016, குரூப் 2 2015]\n1967-ன் 21வது அரசியலமைப்பு திருத்தச் சட்டத்தின் மூலம் இந்திய அரசியலமைப்பின் எட்டாவது அட்டவணையில் சேர்க்கப்பட்ட மொழி எது?",
            "options": [
                ("Sindhi", "சிந்தி"),
                ("Konkani", "கொங்கணி"),
                ("Manipuri", "மணிப்பூரி"),
                ("Nepali", "நேபாளி")
            ],
            "correct_key": "A",
            "exp_en": "The 21st Constitutional Amendment Act, 1967 added Sindhi as the 15th language in the Eighth Schedule of the Constitution.",
            "exp_ta": "1967-ன் 21வது அரசியலமைப்பு திருத்தச் சட்டம் சிந்தியை எட்டாவது அட்டவணையின் 15வது மொழியாகச் சேர்த்தது.",
            "why_a_en": "Sindhi was added by the 21st Amendment in 1967.",
            "why_a_ta": "1967-ன் 21வது திருத்தம் மூலம் சிந்தி மொழி சேர்க்கப்பட்டது.",
            "why_b_en": "Konkani was added later by the 71st Amendment in 1992.",
            "why_b_ta": "கொங்கணி பின்னர் 1992-ன் 71வது திருத்தம் மூலம் சேர்க்கப்பட்டது.",
            "why_c_en": "Manipuri was added by the 71st Amendment in 1992.",
            "why_c_ta": "மணிப்பூரி 1992-ன் 71வது திருத்தம் மூலம் சேர்க்கப்பட்டது.",
            "why_d_en": "Nepali was added by the 71st Amendment in 1992.",
            "why_d_ta": "நேபாளி 1992-ன் 71வது திருத்தம் மூலம் சேர்க்கப்பட்டது.",
            "tip_en": "Remember the sequence: 21st (Sindhi) + 71st (KMN) = 92nd (BDMS). Note: 21 + 71 = 92!",
            "tip_ta": "நினைவு சூத்திரம்: 21வது (சிந்தி) + 71வது (KMN) = 92வது (BDMS). கவனியுங்கள்: 21 + 71 = 92!",
            "fact_en": "Sindhi was the first language added to the Eighth Schedule after the Constitution's commencement.",
            "fact_ta": "அரசியலமைப்பு அமலுக்கு வந்த பிறகு எட்டாவது அட்டவணையில் சேர்க்கப்பட்ட முதல் மொழி சிந்தி ஆகும்."
        },
        # 6
        {
            "subtopic": "71st Constitutional Amendment Act 1992",
            "stem_en": "[TNPSC Group 1 2014, Group 4 2019]\nWhich three languages were included in the Eighth Schedule by the 71st Constitutional Amendment Act, 1992?",
            "stem_ta": "[TNPSC குரூப் 1 2014, குரூப் 4 2019]\n1992-ன் 71வது அரசியலமைப்பு திருத்தச் சட்டத்தின் மூலம் எட்டாவது அட்டவணையில் சேர்க்கப்பட்ட மூன்று மொழிகள் எவை?",
            "options": [
                ("Konkani, Manipuri, and Nepali", "கொங்கணி, மணிப்பூரி மற்றும் நேபாளி"),
                ("Bodo, Dogri, and Maithili", "போடோ, டோக்ரி மற்றும் மைதிலி"),
                ("Sindhi, Santhali, and Nepali", "சிந்தி, சந்தாலி மற்றும் நேபாளி"),
                ("Manipuri, Bodo, and Santhali", "மணிப்பூரி, போடோ மற்றும் சந்தாலி")
            ],
            "correct_key": "A",
            "exp_en": "The 71st Constitutional Amendment Act, 1992 added Konkani, Manipuri, and Nepali to the Eighth Schedule, raising the total number of recognized languages to 18.",
            "exp_ta": "1992-ன் 71வது அரசியலமைப்பு திருத்தச் சட்டம் கொங்கணி, மணிப்பூரி மற்றும் நேபாளி ஆகிய மொழிகளை எட்டாவது அட்டவணையில் சேர்த்து மொத்த எண்ணிக்கையை 18 ஆக உயர்த்தியது.",
            "why_a_en": "Konkani, Manipuri, and Nepali (mnemonic: KMN) were added by 71st CAA 1992.",
            "why_a_ta": "கொங்கணி, மணிப்பூரி மற்றும் நேபாளி (நினைவுக்குறிப்பு: KMN) 71வது திருத்தத்தால் சேர்க்கப்பட்டன.",
            "why_b_en": "Bodo, Dogri, and Maithili were added by the 92nd Amendment in 2003.",
            "why_b_ta": "போடோ, டோக்ரி மற்றும் மைதிலி 2003-ன் 92வது திருத்தம் மூலம் சேர்க்கப்பட்டன.",
            "why_c_en": "Sindhi was added by 21st CAA and Santhali by 92nd CAA.",
            "why_c_ta": "சிந்தி 21வது திருத்தம் மற்றும் சந்தாலி 92வது திருத்தத்தால் சேர்க்கப்பட்டது.",
            "why_d_en": "Bodo and Santhali belong to the 92nd Amendment 2003.",
            "why_d_ta": "போடோ மற்றும் சந்தாலி 2003-ன் 92வது திருத்தத்தைச் சேர்ந்தவை.",
            "tip_en": "Mnemonic 'KMN' (Konkani, Manipuri, Nepali) or 'Kona-Ma-Ne' for 71st CAA 1992.",
            "tip_ta": "71வது திருத்தத்திற்கு 'KMN' (கொங்கணி, மணிப்பூரி, நேபாளி) என்ற நினைவுக்குறிப்பைப் பயன்படுத்தவும்.",
            "fact_en": "Nepali is the only foreign-origin trans-national language in the Eighth Schedule spoken predominantly in Sikkim and North Bengal.",
            "fact_ta": "சிக்கிம் மற்றும் வடக்கு வங்காளத்தில் பெருமளவில் பேசப்படும் நேபாளி எட்டாவது அட்டவணையில் உள்ள அயல்நாட்டு எல்லை தாண்டிய மொழியாகும்."
        },
        # 7
        {
            "subtopic": "92nd Constitutional Amendment Act 2003",
            "stem_en": "[TNPSC Group 2 2012, Group 1 2017]\nFour languages—Bodo, Dogri, Maithili, and Santhali—were added to the Eighth Schedule by which Constitutional Amendment Act?",
            "stem_ta": "[TNPSC குரூப் 2 2012, குரூப் 1 2017]\nபோடோ, டோக்ரி, மைதிலி மற்றும் சந்தாலி ஆகிய நான்கு மொழிகள் எந்த அரசியலமைப்பு திருத்தச் சட்டத்தின் மூலம் எட்டாவது அட்டவணையில் சேர்க்கப்பட்டன?",
            "options": [
                ("92nd Constitutional Amendment Act, 2003", "92வது அரசியலமைப்பு திருத்தச் சட்டம், 2003"),
                ("91st Constitutional Amendment Act, 2003", "91வது அரசியலமைப்பு திருத்தச் சட்டம், 2003"),
                ("93rd Constitutional Amendment Act, 2005", "93வது அரசியலமைப்பு திருத்தச் சட்டம், 2005"),
                ("96th Constitutional Amendment Act, 2011", "96வது அரசியலமைப்பு திருத்தச் சட்டம், 2011")
            ],
            "correct_key": "A",
            "exp_en": "The 92nd Constitutional Amendment Act, 2003 added Bodo, Dogri, Maithili, and Santhali (popularly remembered as BDMS) to the Eighth Schedule, raising the total number of languages to 22.",
            "exp_ta": "2003-ன் 92வது அரசியலமைப்பு திருத்தச் சட்டம் போடோ, டோக்ரி, மைதிலி மற்றும் சந்தாலி (BDMS என நினைவில் கொள்ளப்படும்) ஆகியவற்றை எட்டாவது அட்டவணையில் சேர்த்து மொத்த மொழிகளின் எண்ணிக்கையை 22 ஆக உயர்த்தியது.",
            "why_a_en": "92nd CAA 2003 added the four languages BDMS.",
            "why_a_ta": "92வது திருத்தம் 2003 நான்கு மொழிகளை (BDMS) சேர்த்தது.",
            "why_b_en": "91st CAA 2003 capped the size of the Council of Ministers to 15% and strengthened anti-defection.",
            "why_b_ta": "91வது திருத்தம் 2003 அமைச்சரவை அளவை 15% ஆகக் கட்டுப்படுத்தி கட்சித்தாவல் சட்டத்தை வலுப்படுத்தியது.",
            "why_c_en": "93rd CAA 2005 provided reservation for OBCs in private unaided educational institutions.",
            "why_c_ta": "93வது திருத்தம் 2005 தனியார் கல்வி நிறுவனங்களில் இதர பிற்படுத்தப்பட்டோருக்கு இடஒதுக்கீடு வழங்கியது.",
            "why_d_en": "96th CAA 2011 substituted 'Odia' for 'Oriya'.",
            "why_d_ta": "96வது திருத்தம் 2011 'ஒரியா' என்பதற்குப் பதிலாக 'ஒடியா' எனப் பெயர் மாற்றம் செய்தது.",
            "tip_en": "Mnemonic: 'BDMS' (Bodo, Dogri, Maithili, Santhali) = 92nd Amendment (came into effect Jan 2004).",
            "tip_ta": "நினைவுக்குறிப்பு: 'BDMS' (போடோ, டோக்ரி, மைதிலி, சந்தாலி) = 92வது திருத்தம் (ஜனவரி 2004 முதல் நடைமுறை).",
            "fact_en": "Santhali is the only tribal language from the Austroasiatic family included in the Eighth Schedule.",
            "fact_ta": "சந்தாலி எட்டாவது அட்டவணையில் சேர்க்கப்பட்டுள்ள ஆஸ்ட்ரோ-ஆசியாட்டிக் மொழிக்குடும்பத்தைச் சேர்ந்த ஒரே பழங்குடியின மொழியாகும்."
        },
        # 8
        {
            "subtopic": "Original Number of Eighth Schedule Languages",
            "stem_en": "[TNPSC Group 4 2012, Group 2 2018]\nHow many languages were originally recognized in the Eighth Schedule of the Indian Constitution at the time of its adoption in 1950?",
            "stem_ta": "[TNPSC குரூப் 4 2012, குரூப் 2 2018]\n1950-ல் இந்திய அரசியலமைப்பு ஏற்றுக்கொள்ளப்பட்டபோது எட்டாவது அட்டவணையில் தொடக்கத்தில் எத்தனை மொழிகள் அங்கீகரிக்கப்பட்டிருந்தன?",
            "options": [
                ("14 languages", "14 மொழிகள்"),
                ("12 languages", "12 மொழிகள்"),
                ("16 languages", "16 மொழிகள்"),
                ("18 languages", "18 மொழிகள்")
            ],
            "correct_key": "A",
            "exp_en": "Originally, the Eighth Schedule of the Constitution contained 14 languages: Assamese, Bengali, Gujarati, Hindi, Kannada, Kashmiri, Malayalam, Marathi, Oriya, Punjabi, Sanskrit, Tamil, Telugu, and Urdu.",
            "exp_ta": "தொடக்கத்தில் அரசியலமைப்பின் எட்டாவது அட்டவணையில் 14 மொழிகள் இருந்தன: அஸ்ஸாமி, பெங்காலி, குஜராத்தி, இந்தி, கன்னடம், காஷ்மீரி, மலையாளம், மராத்தி, ஒரியா, பஞ்சாபி, சமஸ்கிருதம், தமிழ், தெலுங்கு மற்றும் உருது.",
            "why_a_en": "14 languages were originally included in the Eighth Schedule in 1950.",
            "why_a_ta": "1950-ல் தொடக்கத்தில் 14 மொழிகள் எட்டாவது அட்டவணையில் இடம்பெற்றிருந்தன.",
            "why_b_en": "12 is incorrect.",
            "why_b_ta": "12 என்பது தவறானது.",
            "why_c_en": "16 is an incorrect intermediate number.",
            "why_c_ta": "16 தவறான இடைப்பட்ட எண்.",
            "why_d_en": "18 was the total after the 71st Amendment in 1992.",
            "why_d_ta": "18 என்பது 1992-ன் 71வது திருத்தத்திற்குப் பிந்தைய மொத்த எண்ணிக்கையாகும்.",
            "tip_en": "Track the growth: 14 (1950) -> +1 (1967) = 15 -> +3 (1992) = 18 -> +4 (2003) = 22.",
            "tip_ta": "வளர்ச்சியைக் கண்காணிக்கவும்: 14 (1950) -> +1 (1967) = 15 -> +3 (1992) = 18 -> +4 (2003) = 22.",
            "fact_en": "Neither English nor Rajasthani was included in the original 14 languages or subsequent additions.",
            "fact_ta": "ஆங்கிலமும் ராஜஸ்தானியும் தொடக்க 14 மொழிகளிலோ அல்லது அடுத்தடுத்த சேர்த்தல்களிலோ இடம்பெறவில்லை."
        },
        # 9
        {
            "subtopic": "Present Eighth Schedule Strength",
            "stem_en": "[TNPSC Group 4 2022, Group 2 2022]\nWhat is the present total number of languages recognized in the Eighth Schedule of the Constitution of India?",
            "stem_ta": "[TNPSC குரூப் 4 2022, குரூப் 2 2022]\nஇந்திய அரசியலமைப்பின் எட்டாவது அட்டவணையில் தற்போது அங்கீகரிக்கப்பட்டுள்ள மொழிகளின் மொத்த எண்ணிக்கை எவ்வளவு?",
            "options": [
                ("22 languages", "22 மொழிகள்"),
                ("24 languages", "24 மொழிகள்"),
                ("20 languages", "20 மொழிகள்"),
                ("18 languages", "18 மொழிகள்")
            ],
            "correct_key": "A",
            "exp_en": "At present, there are 22 languages recognized under the Eighth Schedule of the Indian Constitution, following the additions by the 21st, 71st, and 92nd Constitutional Amendment Acts.",
            "exp_ta": "21வது, 71வது மற்றும் 92வது அரசியலமைப்பு திருத்தச் சட்டங்களின் சேர்க்கைகளைத் தொடர்ந்து, தற்போது இந்திய அரசியலமைப்பின் எட்டாவது அட்டவணையின் கீழ் 22 மொழிகள் அங்கீகரிக்கப்பட்டுள்ளன.",
            "why_a_en": "22 languages is the current constitutional strength of the Eighth Schedule.",
            "why_a_ta": "22 மொழிகள் எட்டாவது அட்டவணையின் தற்போதைய அதிகாரப்பூர்வ எண்ணிக்கையாகும்.",
            "why_b_en": "24 languages is recognized by Sahitya Akademi (22 Schedule VIII + English + Rajasthani), NOT the Constitution.",
            "why_b_ta": "24 மொழிகள் சாகித்ய அகாடமியால் அங்கீகரிக்கப்பட்டவை (22 + ஆங்கிலம் + ராஜஸ்தானி), அரசியலமைப்பால் அல்ல.",
            "why_c_en": "20 is incorrect.",
            "why_c_ta": "20 என்பது தவறானது.",
            "why_d_en": "18 was the count prior to 2003.",
            "why_d_ta": "18 என்பது 2003-க்கு முந்தைய எண்ணிக்கையாகும்.",
            "tip_en": "Trap alert: Sahitya Akademi recognizes 24 languages; the Eighth Schedule of the Constitution recognizes 22 languages.",
            "tip_ta": "கவனிக்க: சாகித்ய அகாடமி 24 மொழிகளை அங்கீகரிக்கிறது; அரசியலமைப்பின் எட்டாவது அட்டவணை 22 மொழிகளை அங்கீகரிக்கிறது.",
            "fact_en": "Demands for inclusion of languages like Bhojpuri, Rajasthani, and Tulu are currently pending with the Government.",
            "fact_ta": "போஜ்புரி, ராஜஸ்தானி, துளு போன்ற மொழிகளைச் சேர்ப்பதற்கான கோரிக்கைகள் தற்போது அரசிடம் நிலுவையில் உள்ளன."
        },
        # 10
        {
            "subtopic": "First Classical Language of India",
            "stem_en": "[TNPSC Group 1 2011, Group 4 2013, Group 2 2014]\nWhich was the first language in India to be accorded the status of 'Classical Language' by the Government of India?",
            "stem_ta": "[TNPSC குரூப் 1 2011, குரூப் 4 2013, குரூப் 2 2014]\nஇந்திய அரசால் 'செம்மொழி' (Classical Language) தகுதி வழங்கப்பட்ட இந்தியாவின் முதல் மொழி எது?",
            "options": [
                ("Tamil (2004)", "தமிழ் (2004)"),
                ("Sanskrit (2005)", "சமஸ்கிருதம் (2005)"),
                ("Kannada (2008)", "கன்னடம் (2008)"),
                ("Telugu (2008)", "தெலுங்கு (2008)")
            ],
            "correct_key": "A",
            "exp_en": "Tamil was the first language in India to be declared a Classical Language by the Government of India on 12 October 2004.",
            "exp_ta": "12 அக்டோபர் 2004 அன்று இந்திய அரசால் இந்தியாவில் செம்மொழித் தகுதி பெற்ற முதல் மொழியாக தமிழ் அறிவிக்கப்பட்டது.",
            "why_a_en": "Tamil was the pioneer language to receive Classical status in 2004.",
            "why_a_ta": "2004-ல் செம்மொழித் தகுதி பெற்ற முன்னோடி மொழி தமிழ் ஆகும்.",
            "why_b_en": "Sanskrit was declared the second Classical Language in 2005.",
            "why_b_ta": "சமஸ்கிருதம் 2005-ல் இரண்டாவது செம்மொழியாக அறிவிக்கப்பட்டது.",
            "why_c_en": "Kannada was granted Classical status in 2008.",
            "why_c_ta": "கன்னடத்திற்கு 2008-ல் செம்மொழித் தகுதி வழங்கப்பட்டது.",
            "why_d_en": "Telugu was granted Classical status in 2008.",
            "why_d_ta": "தெலுங்கிற்கு 2008-ல் செம்மொழித் தகுதி வழங்கப்பட்டது.",
            "tip_en": "Key date: Tamil classical status was notified on 12 October 2004.",
            "tip_ta": "முக்கிய தேதி: தமிழின் செம்மொழித் தகுதி 12 அக்டோபர் 2004 அன்று அறிவிக்கப்பட்டது.",
            "fact_en": "The Central Institute of Classical Tamil (CICT) was established in Chennai following this declaration.",
            "fact_ta": "இந்த அறிவிப்பைத் தொடர்ந்து செம்மொழித் தமிழாய்வு மத்திய நிறுவனம் (CICT) சென்னையில் நிறுவப்பட்டது."
        },
        # 11
        {
            "subtopic": "Sanskrit Classical Language Status",
            "stem_en": "[TNPSC Group 2 2015]\nIn which year was Sanskrit conferred the status of a Classical Language by the Government of India?",
            "stem_ta": "[TNPSC குரூப் 2 2015]\nஇந்திய அரசால் சமஸ்கிருத மொழிக்கு செம்மொழித் தகுதி வழங்கப்பட்ட ஆண்டு எது?",
            "options": [
                ("2005", "2005"),
                ("2004", "2004"),
                ("2006", "2006"),
                ("2008", "2008")
            ],
            "correct_key": "A",
            "exp_en": "Sanskrit was declared a Classical Language by the Government of India in 2005, following Tamil in 2004.",
            "exp_ta": "2004-ல் தமிழைத் தொடர்ந்து, 2005-ல் இந்திய அரசால் சமஸ்கிருதம் செம்மொழியாக அறிவிக்கப்பட்டது.",
            "why_a_en": "2005 was the year Sanskrit became a Classical Language.",
            "why_a_ta": "2005-ல் சமஸ்கிருதம் செம்மொழியாக அறிவிக்கப்பட்டது.",
            "why_b_en": "2004 was Tamil's year of declaration.",
            "why_b_ta": "2004 தமிழின் அறிவிப்பு ஆண்டாகும்.",
            "why_c_en": "No language was declared classical in 2006.",
            "why_c_ta": "2006-ல் எந்த மொழிக்கும் செம்மொழித் தகுதி வழங்கப்படவில்லை.",
            "why_d_en": "2008 was the year Telugu and Kannada were granted classical status.",
            "why_d_ta": "2008-ல் தெலுங்கு மற்றும் கன்னடத்திற்கு செம்மொழித் தகுதி வழங்கப்பட்டது.",
            "tip_en": "Chronology: Tamil (2004) -> Sanskrit (2005) -> Telugu & Kannada (2008).",
            "tip_ta": "காலவரிசை: தமிழ் (2004) -> சமஸ்கிருதம் (2005) -> தெலுங்கு & கன்னடம் (2008).",
            "fact_en": "Central Sanskrit Universities Act 2020 converted three deemed universities into Central Sanskrit Universities.",
            "fact_ta": "மத்திய சமஸ்கிருதப் பல்கலைக்கழகங்கள் சட்டம் 2020 மூன்று நிகர்நிலைப் பல்கலைக்கழகங்களை மத்திய சமஸ்கிருதப் பல்கலைக்கழகங்களாக மாற்றியது."
        },
        # 12
        {
            "subtopic": "Telugu and Kannada Classical Status",
            "stem_en": "[TNPSC Group 1 2016]\nIn which year were Kannada and Telugu concurrently accorded Classical Language status?",
            "stem_ta": "[TNPSC குரூப் 1 2016]\nகன்னடம் மற்றும் தெலுங்கு ஆகிய இரண்டு மொழிகளுக்கும் ஒரே ஆண்டில் செம்மொழித் தகுதி வழங்கப்பட்ட ஆண்டு எது?",
            "options": [
                ("2008", "2008"),
                ("2006", "2006"),
                ("2010", "2010"),
                ("2013", "2013")
            ],
            "correct_key": "A",
            "exp_en": "Both Telugu and Kannada were officially declared Classical Languages by the Government of India in 2008.",
            "exp_ta": "தெலுங்கு மற்றும் கன்னடம் ஆகிய இரண்டும் 2008-ல் இந்திய அரசால் அதிகாரப்பூர்வமாக செம்மொழிகளாக அறிவிக்கப்பட்டன.",
            "why_a_en": "2008 saw both Telugu and Kannada receive Classical status.",
            "why_a_ta": "2008-ல் தெலுங்கு மற்றும் கன்னடம் இரண்டும் செம்மொழித் தகுதி பெற்றன.",
            "why_b_en": "2006 is incorrect.",
            "why_b_ta": "2006 என்பது தவறானது.",
            "why_c_en": "2010 is incorrect.",
            "why_c_ta": "2010 என்பது தவறானது.",
            "why_d_en": "2013 was the year Malayalam received Classical status.",
            "why_d_ta": "2013 மலையாளத்திற்கு செம்மொழித் தகுதி வழங்கப்பட்ட ஆண்டாகும்.",
            "tip_en": "Pair memory: Kannada and Telugu = 2008.",
            "tip_ta": "இணை நினைவூட்டல்: கன்னடம் மற்றும் தெலுங்கு = 2008.",
            "fact_en": "Criteria for classical status include high antiquity of early texts over 1500–2000 years and original literary tradition.",
            "fact_ta": "செம்மொழித் தகுதிக்கான அளவுகோல்களில் 1500–2000 ஆண்டுகள் பழமையான இலக்கியங்கள் மற்றும் தனித்தன்மை வாய்ந்த மரபு ஆகியவை அடங்கும்."
        },
        # 13
        {
            "subtopic": "Malayalam Classical Status",
            "stem_en": "[TNPSC Group 2 2017]\nIn which year was Malayalam declared a Classical Language by the Government of India?",
            "stem_ta": "[TNPSC குரூப் 2 2017]\nஇந்திய அரசால் மலையாள மொழி செம்மொழியாக அறிவிக்கப்பட்ட ஆண்டு எது?",
            "options": [
                ("2013", "2013"),
                ("2011", "2011"),
                ("2014", "2014"),
                ("2016", "2016")
            ],
            "correct_key": "A",
            "exp_en": "Malayalam was accorded the status of a Classical Language in May 2013, becoming the fifth language in India to achieve this honor.",
            "exp_ta": "மே 2013-ல் மலையாளத்திற்கு செம்மொழித் தகுதி வழங்கப்பட்டது; இது இந்த கௌரவத்தைப் பெற்ற இந்தியாவின் ஐந்தாவது மொழியாகும்.",
            "why_a_en": "2013 was the year Malayalam became a classical language.",
            "why_a_ta": "2013-ல் மலையாளம் செம்மொழியாக அறிவிக்கப்பட்டது.",
            "why_b_en": "2011 was when 96th CAA renamed Oriya to Odia.",
            "why_b_ta": "2011-ல் 96வது திருத்தம் ஒரியாவை ஒடியா என மாற்றியது.",
            "why_c_en": "2014 was when Odia was declared classical.",
            "why_c_ta": "2014-ல் ஒடியா செம்மொழியாக அறிவிக்கப்பட்டது.",
            "why_d_en": "2016 is incorrect.",
            "why_d_ta": "2016 என்பது தவறானது.",
            "tip_en": "Dravidian Classical Languages: Tamil (2004), Kannada (2008), Telugu (2008), Malayalam (2013).",
            "tip_ta": "திராவிட செம்மொழிகள்: தமிழ் (2004), கன்னடம் (2008), தெலுங்கு (2008), மலையாளம் (2013).",
            "fact_en": "Malayalam belongs to the South Dravidian language subfamily, diverging from Proto-Tamil-Malayalam around the 9th century CE.",
            "fact_ta": "மலையாளம் தென் திராவிட மொழிக் குடும்பத்தைச் சேர்ந்தது, கி.பி. 9 ஆம் நூற்றாண்டில் மூலத் தமிழ்-மலையாளத்திலிருந்து பிரிந்தது."
        },
        # 14
        {
            "subtopic": "Odia Sixth Classical Language",
            "stem_en": "[TNPSC Group 1 2019]\nWhich language became the sixth language of India to be declared a Classical Language in February 2014?",
            "stem_ta": "[TNPSC குரூப் 1 2019]\nபிப்ரவரி 2014-ல் செம்மொழியாக அறிவிக்கப்பட்ட இந்தியாவின் ஆறாவது மொழி எது?",
            "options": [
                ("Odia", "ஒடியா"),
                ("Bengali", "வங்காள மொழி"),
                ("Marathi", "மராத்தி"),
                ("Assamese", "அஸ்ஸாமி")
            ],
            "correct_key": "A",
            "exp_en": "Odia was notified as the sixth Classical Language on 20 February 2014. It was also the first language from the Indo-Aryan group other than Sanskrit to receive classical status.",
            "exp_ta": "20 பிப்ரவரி 2014 அன்று ஒடியா ஆறாவது செம்மொழியாக அறிவிக்கப்பட்டது. சமஸ்கிருதத்தைத் தவிர இந்தோ-ஆரிய மொழிக் குடும்பத்திலிருந்து செம்மொழித் தகுதி பெற்ற முதல் மொழியும் இதுவேயாகும்.",
            "why_a_en": "Odia was conferred classical status in 2014.",
            "why_a_ta": "2014-ல் ஒடியாவுக்கு செம்மொழித் தகுதி வழங்கப்பட்டது.",
            "why_b_en": "Bengali was granted classical status later in October 2024.",
            "why_b_ta": "வங்காள மொழிக்கு பின்னர் அக்டோபர் 2024-ல் தான் செம்மொழித் தகுதி வழங்கப்பட்டது.",
            "why_c_en": "Marathi was granted classical status in October 2024.",
            "why_c_ta": "மராத்திக்கு அக்டோபர் 2024-ல் செம்மொழித் தகுதி வழங்கப்பட்டது.",
            "why_d_en": "Assamese was granted classical status in October 2024.",
            "why_d_ta": "அஸ்ஸாமிக்கு அக்டோபர் 2024-ல் செம்மொழித் தகுதி வழங்கப்பட்டது.",
            "tip_en": "Odia was the 6th classical language (2014); in 2024, five more languages joined.",
            "tip_ta": "ஒடியா 6வது செம்மொழியாகும் (2014); 2024-ல் மேலும் ஐந்து மொழிகள் இணைந்தன.",
            "fact_en": "Odia's literary antiquity traces back to ancient inscriptions and Madala Panji temple chronicles.",
            "fact_ta": "ஒடியாவின் இலக்கியப் பழமை பண்டைய கல்வெட்டுகள் மற்றும் மடலா பாஞ்சி கோயில் வரலாற்றுப் பதிவுகளிலிருந்து தொடங்குகிறது."
        },
        # 15
        {
            "subtopic": "Non-Inclusion of English in Eighth Schedule",
            "stem_en": "[TNPSC Group 4 2016, Group 2 2017]\nWhich one of the following languages is NOT included in the Eighth Schedule of the Constitution of India, despite being an official language of several North-Eastern States?",
            "stem_ta": "[TNPSC குரூப் 4 2016, குரூப் 2 2017]\nபல வடகிழக்கு மாநிலங்களின் அதிகாரப்பூர்வ மொழியாக இருந்தபோதிலும், இந்திய அரசியலமைப்பின் எட்டாவது அட்டவணையில் சேர்க்கப்படாத மொழி எது?",
            "options": [
                ("English", "ஆங்கிலம்"),
                ("Sanskrit", "சமஸ்கிருதம்"),
                ("Urdu", "உருது"),
                ("Nepali", "நேபாளி")
            ],
            "correct_key": "A",
            "exp_en": "English is NOT included in the Eighth Schedule of the Constitution of India, despite being the sole official language of states like Nagaland and Meghalaya.",
            "exp_ta": "நாகாலாந்து மற்றும் மேகாலயா போன்ற மாநிலங்களின் ஒரே அதிகாரப்பூர்வ மொழியாக இருந்தபோதிலும், ஆங்கிலம் இந்திய அரசியலமைப்பின் எட்டாவது அட்டவணையில் சேர்க்கப்படவில்லை.",
            "why_a_en": "English is omitted from the Eighth Schedule.",
            "why_a_ta": "எட்டாவது அட்டவணையில் ஆங்கிலம் சேர்க்கப்படவில்லை.",
            "why_b_en": "Sanskrit is an original Eighth Schedule language.",
            "why_b_ta": "சமஸ்கிருதம் தொடக்கத்திலிருந்தே உள்ள எட்டாவது அட்டவணை மொழி.",
            "why_c_en": "Urdu is an original Eighth Schedule language.",
            "why_c_ta": "உருது தொடக்கத்திலிருந்தே உள்ள எட்டாவது அட்டவணை மொழி.",
            "why_d_en": "Nepali was added by 71st CAA in 1992.",
            "why_d_ta": "நேபாளி 1992-ல் 71வது திருத்தத்தால் சேர்க்கப்பட்டது.",
            "tip_en": "Classic TNPSC trap question: English is NOT an 8th Schedule language!",
            "tip_ta": "வழக்கமான TNPSC பொறியான வினா: ஆங்கிலம் 8வது அட்டவணை மொழி அல்ல!",
            "fact_en": "English is an associate official language of the Union under the Official Languages Act 1963.",
            "fact_ta": "அதிகாரப்பூர்வ மொழிகள் சட்டம் 1963-ன் கீழ் ஆங்கிலம் ஒன்றியத்தின் இணை அதிகாரப்பூர்வ மொழியாகும்."
        },
        # 16
        {
            "subtopic": "Official Languages Act 1963 Enactment",
            "stem_en": "[TNPSC Group 4 2014, Group 1 2015]\nIn which year was the Official Languages Act enacted by Parliament under the authority of Article 343(3)?",
            "stem_ta": "[TNPSC குரூப் 4 2014, குரூப் 1 2015]\nசரத்து 343(3)-ன் அதிகாரத்தின் கீழ் நாடாளுமன்றத்தால் அதிகாரப்பூர்வ மொழிகள் சட்டம் எந்த ஆண்டு இயற்றப்பட்டது?",
            "options": [
                ("1963", "1963"),
                ("1965", "1965"),
                ("1967", "1967"),
                ("1955", "1955")
            ],
            "correct_key": "A",
            "exp_en": "The Official Languages Act was enacted in 1963 to provide for the continued use of English for official purposes of the Union and for transaction of business in Parliament after the expiration of 15 years on 26 January 1965.",
            "exp_ta": "26 ஜனவரி 1965 அன்று 15 ஆண்டு காலம் முடிவடைந்த பிறகும் ஒன்றியத்தின் அதிகாரப்பூர்வ பணிகளுக்கும் நாடாளுமன்ற நடவடிக்கைகளுக்கும் ஆங்கிலத்தின் பயன்பாட்டைத் தொடர 1963-ல் அதிகாரப்பூர்வ மொழிகள் சட்டம் இயற்றப்பட்டது.",
            "why_a_en": "1963 is the year of enactment of the Official Languages Act.",
            "why_a_ta": "1963 அதிகாரப்பூர்வ மொழிகள் சட்டம் இயற்றப்பட்ட ஆண்டாகும்.",
            "why_b_en": "1965 is the year the 15-year constitutional limit expired.",
            "why_b_ta": "1965 என்பது 15 ஆண்டு அரசியலமைப்பு கெடு முடிந்த ஆண்டாகும்.",
            "why_c_en": "1967 was the year of the crucial amendment guaranteeing English.",
            "why_c_ta": "1967 ஆங்கிலத்தை உறுதி செய்த முக்கிய திருத்தச் சட்டம் இயற்றப்பட்ட ஆண்டாகும்.",
            "why_d_en": "1955 was when the Kher Commission was appointed.",
            "why_d_ta": "1955-ல் கேர் ஆணையம் அமைக்கப்பட்டது.",
            "tip_en": "Act passed: 1963; Amendment passed: 1967; Rules framed: 1976.",
            "tip_ta": "சட்டம் இயற்றப்பட்டது: 1963; திருத்தம்: 1967; விதிகள் உருவாக்கப்பட்டது: 1976.",
            "fact_en": "Section 3 of the 1963 Act used the phrase 'may... continue to be used', which led to major agitation in Tamil Nadu.",
            "fact_ta": "1963 சட்டத்தின் பிரிவு 3 'தொடர்ந்து பயன்படுத்தப்படலாம்' (may continue) என்ற சொற்றொடரைப் பயன்படுத்தியது, இது தமிழ்நாட்டில் பெரும் போராட்டத்திற்கு வழிவகுத்தது."
        },
        # 17
        {
            "subtopic": "Official Languages Amendment Act 1967 Non-Hindi Lock",
            "stem_en": "[TNPSC Group 1 2018]\nThe Official Languages (Amendment) Act, 1967 inserted which historic statutory guarantee regarding the continued use of English?",
            "stem_ta": "[TNPSC குரூப் 1 2018]\nஅதிகாரப்பூர்வ மொழிகள் (திருத்தச்) சட்டம் 1967 ஆங்கிலத்தின் தொடர்ச்சியான பயன்பாடு குறித்து எந்த வரலாற்றுச் சிறப்புமிக்க சட்டப்பூர்வ உத்தரவாதத்தைச் சேர்த்தது?",
            "options": [
                ("English cannot be discontinued without the consent of the legislatures of all non-Hindi States and both Houses of Parliament", "இந்தி பேசாத அனைத்து மாநிலங்களின் சட்டமன்றங்கள் மற்றும் நாடாளுமன்றத்தின் இரு அவைகளின் ஒப்புதல் இன்றி ஆங்கிலத்தை நிறுத்த முடியாது"),
                ("English was made the sole official language of India permanently", "ஆங்கிலம் இந்தியாவின் ஒரே நிரந்தர அதிகாரப்பூர்வ மொழியாக மாற்றப்பட்டது"),
                ("Hindi was declared the sole official language immediately", "இந்தி உடனடியாக ஒரே அதிகாரப்பூர்வ மொழியாக அறிவிக்கப்பட்டது"),
                ("States were prohibited from using English in their official administration", "மாநிலங்கள் தங்களது அதிகாரப்பூர்வ நிர்வாகத்தில் ஆங்கிலத்தைப் பயன்படுத்துவது தடை செய்யப்பட்டது")
            ],
            "correct_key": "A",
            "exp_en": "Section 3(5) inserted by the 1967 Amendment Act provides that English will not cease to be used until resolutions for its discontinuance are passed by the legislatures of all States that have not adopted Hindi as their official language, and by both Houses of Parliament.",
            "exp_ta": "1967 திருத்தச் சட்டத்தால் சேர்க்கப்பட்ட பிரிவு 3(5), இந்தியை அதிகாரப்பூர்வ மொழியாக ஏற்காத அனைத்து மாநிலங்களின் சட்டமன்றங்களும், நாடாளுமன்றத்தின் இரு அவைகளும் ஆங்கிலத்தை நிறுத்துவதற்கான தீர்மானங்களை நிறைவேற்றும் வரை ஆங்கிலத்தின் பயன்பாடு நிறுத்தப்படாது என்று விதிக்கிறது.",
            "why_a_en": "Section 3(5) established this non-Hindi state veto lock.",
            "why_a_ta": "பிரிவு 3(5) இந்தி பேசாத மாநிலங்களுக்கான இந்த தடுப்பு அதிகாரப் பூட்டை நிறுவியது.",
            "why_b_en": "English was retained as an associate official language, not the sole official language.",
            "why_b_ta": "ஆங்கிலம் இணை அதிகாரப்பூர்வ மொழியாகவே தொடர்ந்தது, ஒரே மொழியாக அல்ல.",
            "why_c_en": "Hindi was not made sole language; bilingualism was entrenched.",
            "why_c_ta": "இந்தி ஒரே மொழியாக்கப்படவில்லை; இருமொழி முறை நிலைநிறுத்தப்பட்டது.",
            "why_d_en": "States retain complete freedom under Article 345.",
            "why_d_ta": "மாநிலங்கள் சரத்து 345-ன் கீழ் முழு உரிமையைத் தக்கவைத்துள்ளன.",
            "tip_en": "Nehru's Assurance was given statutory backing by the 1967 Amendment under Prime Minister Indira Gandhi.",
            "tip_ta": "நேருவின் வாக்குறுதிக்கு பிரதமர் இந்திரா காந்தி காலத்தில் 1967 திருத்தத்தின் மூலம் சட்டப்பூர்வ அந்தஸ்து வழங்கப்பட்டது.",
            "fact_en": "This statutory lock ensures that a single non-Hindi State (such as Tamil Nadu) can veto the abolition of English.",
            "fact_ta": "இந்த சட்டப்பூர்வ விதிமுறை தமிழ்நாடு போன்ற ஒரு இந்தி பேசாத மாநிலம் கூட ஆங்கிலம் நீக்கப்படுவதைத் தடுக்கும் அதிகாரத்தை உறுதி செய்கிறது."
        },
        # 18
        {
            "subtopic": "Tamil Nadu Two-Language Policy 1968",
            "stem_en": "[TNPSC Group 1 2017, Group 2 2018]\nIn January 1968, the Tamil Nadu Legislative Assembly under Chief Minister C.N. Annadurai passed a landmark resolution establishing which language policy?",
            "stem_ta": "[TNPSC குரூப் 1 2017, குரூப் 2 2018]\nஜனவரி 1968-ல் முதலமைச்சர் சி.என். அண்ணாதுரை தலைமையில் தமிழ்நாடு சட்டமன்றம் எந்த மொழிக் கொள்கையை நிறுவி ஒரு வரலாற்றுச் சிறப்புமிக்க தீர்மானத்தை நிறைவேற்றியது?",
            "options": [
                ("Two-Language Policy (Tamil and English)", "இருமொழிக் கொள்கை (தமிழ் மற்றும் ஆங்கிலம்)"),
                ("Three-Language Formula (Tamil, English, Hindi)", "மும்மொழிக் கொள்கை (தமிழ், ஆங்கிலம், இந்தி)"),
                ("Single-Language Policy (Tamil only)", "ஒற்றை மொழிக் கொள்கை (தமிழ் மட்டுமே)"),
                ("Four-Language Policy including Sanskrit", "சமஸ்கிருதம் உள்ளிட்ட நான்கு மொழிக் கொள்கை")
            ],
            "correct_key": "A",
            "exp_en": "On 23 January 1968, the Tamil Nadu Legislative Assembly under Chief Minister C.N. Annadurai adopted the Two-Language Policy consisting of Tamil and English, rejecting the Three-Language Formula and eliminating Hindi from state school curricula.",
            "exp_ta": "23 ஜனவரி 1968 அன்று, முதலமைச்சர் சி.என். அண்ணாதுரை தலைமையில் தமிழ்நாடு சட்டமன்றம் மும்மொழிக் கொள்கையை நிராகரித்து, தமிழ் மற்றும் ஆங்கிலம் ஆகிய இருமொழிக் கொள்கையை ஏற்றுக்கொண்டு அரசுப் பள்ளிப் பாடத்திட்டங்களிலிருந்து இந்தியை நீக்கியது.",
            "why_a_en": "The 1968 resolution established the Two-Language Formula of Tamil and English.",
            "why_a_ta": "1968 தீர்மானம் தமிழ் மற்றும் ஆங்கிலம் கொண்ட இருமொழிக் கொள்கையை நிறுவியது.",
            "why_b_en": "The Three-Language Formula was explicitly rejected by the resolution.",
            "why_b_ta": "மும்மொழிக் கொள்கை இத்தீர்மானத்தால் வெளிப்படையாக நிராகரிக்கப்பட்டது.",
            "why_c_en": "Tamil Nadu retained English alongside Tamil, rejecting a monolingual policy.",
            "why_c_ta": "தமிழ்நாடு தமிழுடன் ஆங்கிலத்தையும் தக்கவைத்துக் கொண்டது, ஒற்றை மொழி முறையை அல்ல.",
            "why_d_en": "Four-language formula is fictional.",
            "why_d_ta": "நான்கு மொழிக் கொள்கை என்பது கற்பனையானது.",
            "tip_en": "Key date: 23 January 1968; Key leaders: Periyar E.V.R., C.N. Annadurai.",
            "tip_ta": "முக்கிய தேதி: 23 ஜனவரி 1968; முக்கிய தலைவர்கள்: தந்தை பெரியார், பேரறிஞர் அண்ணா.",
            "fact_en": "The resolution also suspended NCC training in the state because Hindi command words were insisted upon.",
            "fact_ta": "இந்தி கட்டளைச் சொற்கள் கட்டாயப்படுத்தப்பட்டதால் மாநிலத்தில் என்.சி.சி (NCC) பயிற்சியையும் இத்தீர்மானம் நிறுத்திவைத்தது."
        },
        # 19
        {
            "subtopic": "Article 350 Grievance Redressal Representation",
            "stem_en": "[TNPSC Group 1 2020]\nUnder Article 350 of the Constitution of India, every person is entitled to submit a representation for the redress of any grievance to any officer or authority of the Union or a State in:",
            "stem_ta": "[TNPSC குரூப் 1 2020]\nஇந்திய அரசியலமைப்பின் சரத்து 350-ன் படி, எந்தவொரு நபரும் தனது குறைதீர்ப்புக்கான விண்ணப்பத்தை ஒன்றியம் அல்லது மாநிலத்தின் எந்தவொரு அலுவலரிடமும் அல்லது அதிகார அமைப்பிடமும் எம்மொழியில் சமர்ப்பிக்க உரிமையுடையவர்?",
            "options": [
                ("Any of the languages used in the Union or in the State", "ஒன்றியத்தில் அல்லது மாநிலத்தில் பயன்படுத்தப்படும் மொழிகளில் ஏதேனும் ஒன்றில்"),
                ("Hindi in Devanagari script only", "தேவநாகரி வரிவடிவத்திலான இந்தியில் மட்டுமே"),
                ("English only", "ஆங்கிலத்தில் மட்டுமே"),
                ("Only in the recognized Eighth Schedule languages", "அங்கீகரிக்கப்பட்ட எட்டாவது அட்டவணை மொழிகளில் மட்டுமே")
            ],
            "correct_key": "A",
            "exp_en": "Article 350 states: 'Every person shall be entitled to submit a representation for the redress of any grievance to any officer or authority of the Union or a State in any of the languages used in the Union or in the State, as the case may be.'",
            "exp_ta": "சரத்து 350 குறிப்பிடுகிறது: 'ஒவ்வொரு நபரும் தனது குறைதீர்ப்புக்கான விண்ணப்பத்தை ஒன்றியம் அல்லது மாநிலத்தில் வழக்கிலுள்ள மொழிகளில் ஏதேனும் ஒன்றில் ஒன்றியம் அல்லது மாநிலத்தின் எந்தவொரு அலுவலரிடமும் சமர்ப்பிக்க உரிமையுடையவராவார்.'",
            "why_a_en": "Article 350 guarantees the right to petition in any language used in the Union or State.",
            "why_a_ta": "சரத்து 350 ஒன்றியம் அல்லது மாநிலத்தில் பயன்பாட்டிலுள்ள எந்த மொழியிலும் மனு அளிக்க உரிமை அளிக்கிறது.",
            "why_b_en": "Hindi is not mandatory for grievance representations.",
            "why_b_ta": "குறைதீர்ப்பு மனுக்களுக்கு இந்தி கட்டாயமல்ல.",
            "why_c_en": "English is not the sole permitted medium.",
            "why_c_ta": "ஆங்கிலம் மட்டுமே அனுமதிக்கப்பட்ட ஊடகம் அல்ல.",
            "why_d_en": "The language need not be an Eighth Schedule language; it can be any local language in use.",
            "why_d_ta": "மொழி எட்டாவது அட்டவணை மொழியாக இருக்க வேண்டிய அவசியமில்லை; பயன்பாட்டிலுள்ள எந்த உள்ளூர் மொழியாகவும் இருக்கலாம்.",
            "tip_en": "Democratic safeguard: No citizen's grievance representation can be rejected merely because of the language used.",
            "tip_ta": "ஜனநாயகப் பாதுகாப்பு: மொழி காரணமாக எந்தவொரு குடிமகனின் குறைதீர்ப்பு மனுவும் நிராகரிக்கப்பட முடியாது.",
            "fact_en": "Article 350 is part of Chapter IV of Part XVII (Special Directives).",
            "fact_ta": "சரத்து 350 பகுதி XVII-ன் அத்தியாயம் IV-ன் (சிறப்பு வழிகாட்டுதல்கள்) ஒரு பகுதியாகும்."
        },
        # 20
        {
            "subtopic": "Article 350A Mother Tongue at Primary Stage",
            "stem_en": "[TNPSC Group 2 2016, Group 1 2015]\nArticle 350A, inserted by the 7th Constitutional Amendment Act 1956, directs every State to provide adequate facilities for instruction in the mother tongue at which stage of education?",
            "stem_ta": "[TNPSC குரூப் 2 2016, குரூப் 1 2015]\n1956-ன் 7வது அரசியலமைப்பு திருத்தச் சட்டத்தால் சேர்க்கப்பட்ட சரத்து 350A, எந்தக் கல்வி நிலையில் தாய்மொழியில் கற்பிப்பதற்கான போதுமான வசதிகளைச் செய்து தர ஒவ்வொரு மாநிலத்திற்கும் வழிகாட்டுகிறது?",
            "options": [
                ("Primary stage of education to children belonging to linguistic minority groups", "மொழிச் சிறுபான்மையினக் குழுக்களைச் சேர்ந்த குழந்தைகளுக்கு தொடக்கக் கல்வி நிலையில்"),
                ("Secondary stage of education to all students", "அனைத்து மாணவர்களுக்கும் இடைநிலைக் கல்வி நிலையில்"),
                ("Higher secondary and collegiate education", "மேல்நிலைக் கல்வி மற்றும் கல்லூரி நிலையில்"),
                ("Postgraduate and professional courses", "முதுகலை மற்றும் தொழில்முறைப் படிப்புகளில்")
            ],
            "correct_key": "A",
            "exp_en": "Article 350A directs that it shall be the endeavour of every State and of every local authority to provide adequate facilities for instruction in the mother tongue at the primary stage of education to children belonging to linguistic minority groups.",
            "exp_ta": "சரத்து 350A மொழிச் சிறுபான்மைக் குழுக்களைச் சேர்ந்த குழந்தைகளுக்குத் தொடக்கக் கல்வி நிலையில் தாய்மொழி வழியில் கற்பிப்பதற்கான போதிய வசதிகளை ஏற்படுத்திக் கொடுப்பது ஒவ்வொரு மாநிலத்தின் மற்றும் உள்ளாட்சி அமைப்பின் கடமையாகும் என்று வழிகாட்டுகிறது.",
            "why_a_en": "Article 350A specifically targets the primary stage for linguistic minority children.",
            "why_a_ta": "சரத்து 350A குறிப்பாக மொழிச் சிறுபான்மையினக் குழந்தைகளுக்கு தொடக்கக் கல்வி நிலையை இலக்காகக் கொண்டுள்ளது.",
            "why_b_en": "It does not apply to secondary stage.",
            "why_b_ta": "இது இடைநிலைக் கல்வி நிலைக்குப் பொருந்தாது.",
            "why_c_en": "Higher education is beyond the scope of Article 350A.",
            "why_c_ta": "உயர்கல்வி சரத்து 350A-ன் வரம்பிற்கு அப்பாற்பட்டது.",
            "why_d_en": "Professional courses are not covered.",
            "why_d_ta": "தொழில்முறைப் படிப்புகள் இதில் அடங்காது.",
            "tip_en": "Inserted by the 7th Amendment 1956 on recommendations of the States Reorganisation Commission (Fazal Ali Commission).",
            "tip_ta": "மாநில மறுசீரமைப்பு ஆணையத்தின் (பசல் அலி ஆணையம்) பரிந்துரையின் பேரில் 1956-ன் 7வது திருத்தத்தால் சேர்க்கப்பட்டது.",
            "fact_en": "The President is empowered under Article 350A to issue directions to any State for securing these facilities.",
            "fact_ta": "இவ்வசதிகளை உறுதி செய்வதற்காக எந்தவொரு மாநிலத்திற்கும் வழிகாட்டுதல்களைப் பிறப்பிக்க குடியரசுத் தலைவருக்கு சரத்து 350A அதிகாரமளிக்கிறது."
        },
        # 21
        {
            "subtopic": "Article 350B Special Officer for Linguistic Minorities",
            "stem_en": "[TNPSC Group 1 2017, Group 2 2019]\nUnder Article 350B of the Constitution of India, who appoints the Special Officer for Linguistic Minorities?",
            "stem_ta": "[TNPSC குரூப் 1 2017, குரூப் 2 2019]\nஇந்திய அரசியலமைப்பின் சரத்து 350B-ன் கீழ் மொழிச் சிறுபான்மையினருக்கான சிறப்பு அலுவலரை நியமிப்பவர் யார்?",
            "options": [
                ("The President of India", "இந்தியக் குடியரசுத் தலைவர்"),
                ("The Prime Minister of India", "இந்தியப் பிரதமர்"),
                ("The Chief Justice of India", "இந்தியத் தலைமை நீதிபதி"),
                ("The Union Minister for Minority Affairs", "மத்திய சிறுபான்மையினர் நலத்துறை அமைச்சர்")
            ],
            "correct_key": "A",
            "exp_en": "Article 350B provides that there shall be a Special Officer for linguistic minorities to be appointed by the President. The officer investigates all matters relating to constitutional safeguards provided for linguistic minorities.",
            "exp_ta": "சரத்து 350B குடியரசுத் தலைவரால் நியமிக்கப்படும் மொழிச் சிறுபான்மையினருக்கான சிறப்பு அலுவலர் ஒருவர் இருப்பார் என்று கூறுகிறது. இவர் மொழிச் சிறுபான்மையினருக்கு வழங்கப்பட்டுள்ள அரசியலமைப்புப் பாதுகாப்புகள் தொடர்பான அனைத்து விவகாரங்களையும் ஆய்வு செய்வார்.",
            "why_a_en": "Article 350B explicitly vests appointment authority in the President.",
            "why_a_ta": "சரத்து 350B நியமன அதிகாரத்தை குடியரசுத் தலைவரிடம் வழங்குகிறது.",
            "why_b_en": "The Prime Minister does not make this constitutional appointment.",
            "why_b_ta": "பிரதமர் இந்த அரசியலமைப்பு நியமனத்தை மேற்கொள்வதில்லை.",
            "why_c_en": "The CJI has no appointing role here.",
            "why_c_ta": "இந்தியத் தலைமை நீதிபதிக்கு இதில் எவ்விதப் பங்கும் இல்லை.",
            "why_d_en": "The Minister heads the administrative ministry, but appointment is by the President.",
            "why_d_ta": "அமைச்சர் நிர்வாக அமைச்சகத்திற்குத் தலைமை தாங்குகிறார், ஆனால் நியமனம் குடியரசுத் தலைவரால் செய்யப்படுகிறது.",
            "tip_en": "Also inserted by 7th CAA 1956. The office was created in 1957 with headquarters at Prayagraj (Allahabad).",
            "tip_ta": "1956-ன் 7வது திருத்தத்தால் சேர்க்கப்பட்டது. இவ்வலுவலகம் 1957-ல் பிரயாக்ராஜில் (அலகாபாத்) தலைமையகத்துடன் உருவாக்கப்பட்டது.",
            "fact_en": "The Commissioner for Linguistic Minorities (CLM) functions under the Ministry of Minority Affairs.",
            "fact_ta": "மொழிச் சிறுபான்மையினர் ஆணையர் (CLM) சிறுபான்மையினர் நல அமைச்சகத்தின் கீழ் செயல்படுகிறார்."
        },
        # 22
        {
            "subtopic": "Article 351 Directive for Development of Hindi",
            "stem_en": "[TNPSC Group 4 2018, Group 2 2016]\nWhich Article of the Constitution lays down a directive for the Union to promote the spread and development of the Hindi language?",
            "stem_ta": "[TNPSC குரூப் 4 2018, குரூப் 2 2016]\nஇந்தி மொழியின் பரவலையும் வளர்ச்சியையும் ஊக்குவிக்க ஒன்றிய அரசுக்கு வழிகாட்டுதலை வழங்கும் அரசியலமைப்புச் சரத்து எது?",
            "options": [
                ("Article 351", "சரத்து 351"),
                ("Article 343", "சரத்து 343"),
                ("Article 345", "சரத்து 345"),
                ("Article 348", "சரத்து 348")
            ],
            "correct_key": "A",
            "exp_en": "Article 351 states that it shall be the duty of the Union to promote the spread of the Hindi language, to develop it so that it may serve as a medium of expression for all elements of the composite culture of India.",
            "exp_ta": "சரத்து 351 குறிப்பிடுகிறது: 'இந்தியாவின் கூட்டுப் பண்பாட்டின் அனைத்துக் கூறுகளையும் வெளிப்படுத்தும் ஊடகமாகத் திகழும் வகையில் இந்தி மொழியின் பரவலை ஊக்குவிப்பதும் அதன் வளர்ச்சியை மேம்படுத்துவதும் ஒன்றியத்தின் கடமையாகும்.'",
            "why_a_en": "Article 351 is the special directive for Hindi language development.",
            "why_a_ta": "சரத்து 351 இந்தி மொழி வளர்ச்சிக்கான சிறப்பு வழிகாட்டுதலாகும்.",
            "why_b_en": "Article 343 defines the official language of the Union.",
            "why_b_ta": "சரத்து 343 ஒன்றியத்தின் அதிகாரப்பூர்வ மொழியை வரையறுக்கிறது.",
            "why_c_en": "Article 345 governs official languages of States.",
            "why_c_ta": "சரத்து 345 மாநிலங்களின் அதிகாரப்பூர்வ மொழிகளைக் கையாள்கிறது.",
            "why_d_en": "Article 348 governs language of courts and legislative bills.",
            "why_d_ta": "சரத்து 348 நீதிமன்றங்கள் மற்றும் சட்டமன்ற மசோதாக்களின் மொழியைக் கையாள்கிறது.",
            "tip_en": "Article 351 specifies drawing vocabulary primarily from Sanskrit and secondarily from other Eighth Schedule languages.",
            "tip_ta": "சரத்து 351 சொல்வளத்தை முதன்மையாக சமஸ்கிருதத்திலிருந்தும், இரண்டாம் பட்சமாக பிற 8வது அட்டவணை மொழிகளிலிருந்தும் பெற வழிகாட்டுகிறது.",
            "fact_en": "Article 351 is not judicially enforceable as a fundamental right; it is a constitutional directive.",
            "fact_ta": "சரத்து 351 அடிப்படை உரிமையைப் போல நீதிமன்றத்தால் கட்டாயப்படுத்த முடியாது; இது ஒரு அரசியலமைப்பு வழிகாட்டுதலாகும்."
        },
        # 23
        {
            "subtopic": "Language of Supreme Court Article 348(1)",
            "stem_en": "[TNPSC Group 1 2016, Group 2 2017]\nUnder Article 348(1)(a) of the Constitution of India, in which language must all proceedings in the Supreme Court be conducted until Parliament by law otherwise provides?",
            "stem_ta": "[TNPSC குரூப் 1 2016, குரூப் 2 2017]\nஇந்திய அரசியலமைப்பின் சரத்து 348(1)(a)-ன் படி, நாடாளுமன்றம் சட்டத்தின் மூலம் வேறுவிதமாக ஏற்பாடு செய்யும் வரை, உச்ச நீதிமன்றத்தின் அனைத்து நடவடிக்கைகளும் எந்த மொழியில் நடத்தப்பட வேண்டும்?",
            "options": [
                ("English only", "ஆங்கிலத்தில் மட்டுமே"),
                ("Hindi in Devanagari script", "தேவநாகரி வரிவடிவத்திலான இந்தியில்"),
                ("Either Hindi or English at the discretion of the Chief Justice", "தலைமை நீதிபதியின் விருப்பப்படி இந்தி அல்லது ஆங்கிலத்தில்"),
                ("Any Eighth Schedule language chosen by the petitioner", "மனுதாரர் தேர்வு செய்யும் ஏதேனும் ஒரு எட்டாவது அட்டவணை மொழியில்")
            ],
            "correct_key": "A",
            "exp_en": "Article 348(1)(a) mandates that until Parliament by law otherwise provides, all proceedings in the Supreme Court and in every High Court shall be in the English language.",
            "exp_ta": "சரத்து 348(1)(a) நாடாளுமன்றம் சட்டத்தால் வேறு ஏற்பாடு செய்யும் வரை, உச்ச நீதிமன்றத்திலும் அனைத்து உயர் நீதிமன்றங்களிலும் நடைபெறும் அனைத்து நடவடிக்கைகளும் ஆங்கில மொழியிலேயே இருக்க வேண்டும் என்று கட்டாயமாக்குகிறது.",
            "why_a_en": "Article 348(1) strictly mandates English for Supreme Court proceedings.",
            "why_a_ta": "சரத்து 348(1) உச்ச நீதிமன்ற நடவடிக்கைகளுக்கு ஆங்கிலத்தை மட்டுமே கட்டாயமாக்குகிறது.",
            "why_b_en": "Hindi is not authorized for the Supreme Court under Article 348(1).",
            "why_b_ta": "சரத்து 348(1)-ன் கீழ் உச்ச நீதிமன்றத்திற்கு இந்தி அனுமதிக்கப்படவில்லை.",
            "why_c_en": "CJI cannot unilaterally substitute Hindi for English.",
            "why_c_ta": "தலைமை நீதிபதி தன்னிச்சையாக ஆங்கிலத்திற்குப் பதிலாக இந்தியை மாற்ற முடியாது.",
            "why_d_en": "Petitioner cannot compel proceedings in other scheduled languages.",
            "why_d_ta": "மனுதாரர் பிற அட்டவணை மொழிகளில் நடவடிக்கைகளை நடத்தக் கோர முடியாது.",
            "tip_en": "Supreme Court is English-only. Even for High Courts, Hindi/regional languages can be permitted only with Governor + President consent.",
            "tip_ta": "உச்ச நீதிமன்றம் ஆங்கிலம் மட்டுமே. உயர் நீதிமன்றங்களுக்கும் கூட, ஆளுநர் + குடியரசுத் தலைவர் ஒப்புதலுடன் மட்டுமே இந்தி/வட்டார மொழிகள் அனுமதிக்கப்படும்.",
            "fact_en": "The Full Court of the Supreme Court has repeatedly rejected proposals to introduce Hindi as an official language of the Supreme Court.",
            "fact_ta": "உச்ச நீதிமன்றத்தின் முழு அமர்வு உச்ச நீதிமன்றத்தின் அதிகாரப்பூர்வ மொழியாக இந்தியை அறிமுகப்படுத்தும் திட்டங்களை மீண்டும் மீண்டும் நிராகரித்துள்ளது."
        },
        # 24
        {
            "subtopic": "Language in High Courts Article 348(2)",
            "stem_en": "[TNPSC Group 1 2015, Group 2 2019]\nUnder Article 348(2), who is empowered to authorize the use of Hindi or any other official language of the State in proceedings of the High Court, and whose consent is mandatory?",
            "stem_ta": "[TNPSC குரூப் 1 2015, குரூப் 2 2019]\nசரத்து 348(2)-ன் கீழ் உயர் நீதிமன்ற நடவடிக்கைகளில் இந்தி அல்லது மாநிலத்தின் பிற அதிகாரப்பூர்வ மொழியைப் பயன்படுத்த அங்கீகரிக்க யாருக்கு அதிகாரமுள்ளது, மற்றும் யாருடைய முன் ஒப்புதல் கட்டாயமானது?",
            "options": [
                ("Governor of the State, with the previous consent of the President", "மாநில ஆளுநர், குடியரசுத் தலைவரின் முன் ஒப்புதலுடன்"),
                ("Chief Justice of the High Court, with the consent of the Governor", "உயர் நீதிமன்றத் தலைமை நீதிபதி, ஆளுநரின் ஒப்புதலுடன்"),
                ("State Legislature, with two-thirds majority", "மாநில சட்டமன்றம், மூன்றில் இரண்டு பங்கு பெரும்பான்மையுடன்"),
                ("President of India, on the recommendation of Parliament", "இந்தியக் குடியரசுத் தலைவர், நாடாளுமன்றப் பரிந்துரையின் பேரில்")
            ],
            "correct_key": "A",
            "exp_en": "Article 348(2) empowers the Governor of a State, with the previous consent of the President, to authorize the use of Hindi or any other official language of the State in proceedings of the High Court.",
            "exp_ta": "சரத்து 348(2) மாநில ஆளுநர், குடியரசுத் தலைவரின் முன் ஒப்புதலுடன், உயர் நீதிமன்ற நடவடிக்கைகளில் இந்தி அல்லது மாநிலத்தின் பிற அதிகாரப்பூர்வ மொழியைப் பயன்படுத்த அங்கீகாரம் அளிக்க அதிகாரமளிக்கிறது.",
            "why_a_en": "Governor acts with previous consent of the President under Article 348(2).",
            "why_a_ta": "சரத்து 348(2)-ன் கீழ் ஆளுநர் குடியரசுத் தலைவரின் முன் ஒப்புதலுடன் செயல்படுகிறார்.",
            "why_b_en": "The Chief Justice does not hold this statutory power.",
            "why_b_ta": "தலைமை நீதிபதிக்கு இந்த சட்டப்பூர்வ அதிகாரம் இல்லை.",
            "why_c_en": "State Legislature cannot pass this resolution directly.",
            "why_c_ta": "மாநில சட்டமன்றம் இந்தத் தீர்மானத்தை நேரடியாக நிறைவேற்ற முடியாது.",
            "why_d_en": "The Governor initiates the action, not the President directly.",
            "why_d_ta": "ஆளுநரே நடவடிக்கையைத் தொடங்குகிறார், குடியரசுத் தலைவர் நேரடியாக அல்ல.",
            "tip_en": "High Courts of UP, Bihar, Rajasthan, and MP use Hindi alongside English under this provision.",
            "tip_ta": "உத்தரப் பிரதேசம், பீகார், ராஜஸ்தான் மற்றும் மத்தியப் பிரதேச உயர் நீதிமன்றங்கள் இந்த விதியின் கீழ் ஆங்கிலத்துடன் இந்தியையும் பயன்படுத்துகின்றன.",
            "fact_en": "Tamil Nadu has repeatedly requested permission to use Tamil in the Madras High Court, which was declined by the Supreme Court.",
            "fact_ta": "சென்னை உயர் நீதிமன்றத்தில் தமிழைப் பயன்படுத்த தமிழ்நாடு விடுத்த தொடர் கோரிக்கைகளை உச்ச நீதிமன்றம் ஏற்க மறுத்துவிட்டது."
        },
        # 25
        {
            "subtopic": "English Translation of High Court Judgments",
            "stem_en": "[TNPSC Group 1 2018]\nEven if Hindi or a regional language is authorized for High Court proceedings, what does Section 7 of the Official Languages Act 1963 mandate for judgments, decrees, and orders?",
            "stem_ta": "[TNPSC குரூப் 1 2018]\nஉயர் நீதிமன்ற நடவடிக்கைகளுக்கு இந்தி அல்லது வட்டார மொழி அங்கீகரிக்கப்பட்டிருந்தாலும், தீர்ப்புகள், ஆணைகள் மற்றும் கட்டளைகளுக்கு அதிகாரப்பூர்வ மொழிகள் சட்டம் 1963-ன் பிரிவு 7 எதைக் கட்டாயமாக்குகிறது?",
            "options": [
                ("An authoritative English translation issued under the authority of the High Court must accompany them", "உயர் நீதிமன்றத்தின் அதிகாரத்தின் கீழ் வெளியிடப்பட்ட அதிகாரப்பூர்வ ஆங்கில மொழிபெயர்ப்பு இணைக்கப்பட வேண்டும்"),
                ("The judgment is invalid unless delivered exclusively in Sanskrit", "சமஸ்கிருதத்தில் மட்டுமே வழங்கப்படாவிட்டால் தீர்ப்பு செல்லாது"),
                ("No English translation is required if the Governor approves", "ஆளுநர் ஒப்புதல் அளித்தால் ஆங்கில மொழிபெயர்ப்பு தேவையில்லை"),
                ("The judgment must be re-argued in the Supreme Court before taking effect", "தீர்ப்பு அமலுக்கு வருவதற்கு முன்பு உச்ச நீதிமன்றத்தில் மீண்டும் வாதாடப்பட வேண்டும்")
            ],
            "correct_key": "A",
            "exp_en": "Under Section 7 of the Official Languages Act 1963, where judgments, decrees, or orders are passed in Hindi or a state language, they must be accompanied by an authoritative text of the same in the English language.",
            "exp_ta": "அதிகாரப்பூர்வ மொழிகள் சட்டம் 1963-ன் பிரிவு 7-ன் கீழ், தீர்ப்புகள், ஆணைகள் அல்லது கட்டளைகள் இந்தி அல்லது மாநில மொழியில் வழங்கப்பட்டால், அவற்றுடன் ஆங்கில மொழியிலான அதிகாரப்பூர்வ உரை இணைக்கப்பட வேண்டும்.",
            "why_a_en": "Section 7 mandates an accompanying authoritative English text.",
            "why_a_ta": "பிரிவு 7 உடன் அதிகாரப்பூர்வ ஆங்கில உரை இணைக்கப்பட வேண்டும் என்று கட்டாயமாக்குகிறது.",
            "why_b_en": "Sanskrit has no such requirement.",
            "why_b_ta": "சமஸ்கிருதத்திற்கு அத்தகைய விதி எதுவும் இல்லை.",
            "why_c_en": "Governor cannot waive this statutory English requirement.",
            "why_c_ta": "ஆளுநர் இந்த சட்டப்பூர்வ ஆங்கிலத் தேவையைத் தள்ளுபடி செய்ய முடியாது.",
            "why_d_en": "Re-arguing judgments is legally incorrect.",
            "why_d_ta": "மீண்டும் வாதாட வேண்டும் என்பது சட்டப்படி தவறானது.",
            "tip_en": "Judicial consistency across India is preserved by maintaining English as the unifying legal language.",
            "tip_ta": "ஆங்கிலத்தை ஒருங்கிணைக்கும் சட்ட மொழியாகப் பராமரிப்பதன் மூலம் இந்தியா முழுவதும் நீதித்துறை நிலைத்தன்மை பாதுகாக்கப்படுகிறது.",
            "fact_en": "Supreme Court judgements are reported and cited exclusively from the official English text.",
            "fact_ta": "உச்ச நீதிமன்றத் தீர்ப்புகள் அதிகாரப்பூர்வ ஆங்கில உரையிலிருந்து மட்டுமே மேற்கோள் காட்டப்பட்டு ஆவணப்படுத்தப்படுகின்றன."
        },
        # 26
        {
            "subtopic": "Official Languages Rules 1976 Framing",
            "stem_en": "[TNPSC Group 2 2018]\nIn which year were the Official Languages (Use for Official Purposes of the Union) Rules framed under Section 8 of the Official Languages Act, 1963?",
            "stem_ta": "[TNPSC குரூப் 2 2018]\nஅதிகாரப்பூர்வ மொழிகள் சட்டம் 1963-ன் பிரிவு 8-ன் கீழ் அதிகாரப்பூர்வ மொழிகள் (ஒன்றியத்தின் அதிகாரப்பூர்வ நோக்கங்களுக்கான பயன்பாடு) விதிகள் எந்த ஆண்டு உருவாக்கப்பட்டன?",
            "options": [
                ("1976", "1976"),
                ("1968", "1968"),
                ("1987", "1987"),
                ("1956", "1956")
            ],
            "correct_key": "A",
            "exp_en": "The Official Languages (Use for Official Purposes of the Union) Rules were framed in 1976 (amended in 1987 and 2007) by the Central Government.",
            "exp_ta": "அதிகாரப்பூர்வ மொழிகள் (ஒன்றியத்தின் அதிகாரப்பூர்வ நோக்கங்களுக்கான பயன்பாடு) விதிகள் 1976-ல் மத்திய அரசால் உருவாக்கப்பட்டன (1987 மற்றும் 2007-ல் திருத்தப்பட்டன).",
            "why_a_en": "1976 is the year the Rules were notified.",
            "why_a_ta": "1976 விதிகள் அறிவிக்கப்பட்ட ஆண்டாகும்.",
            "why_b_en": "1968 was the Official Language Resolution.",
            "why_b_ta": "1968 அதிகாரப்பூர்வ மொழித் தீர்மானத்தின் ஆண்டாகும்.",
            "why_c_en": "1987 was the year of amendment to the Rules.",
            "why_c_ta": "1987 விதிகளில் திருத்தம் செய்யப்பட்ட ஆண்டாகும்.",
            "why_d_en": "1956 was Kher report year.",
            "why_d_ta": "1956 கேர் அறிக்கை சமர்ப்பிக்கப்பட்ட ஆண்டாகும்.",
            "tip_en": "Rules divide India into Regions A, B, and C for communication in Hindi/English.",
            "tip_ta": "இவ்விதிகள் இந்தி/ஆங்கிலத் தொடர்புகளுக்காக இந்தியாவை பிராந்தியம் A, B மற்றும் C எனப் பிரிக்கின்றன.",
            "fact_en": "The Rules apply to all Union ministries, departments, corporations, and offices.",
            "fact_ta": "இவ்விதிகள் அனைத்து மத்திய அமைச்சகங்கள், துறைகள், கழகங்கள் மற்றும் அலுவலகங்களுக்கும் பொருந்தும்."
        },
        # 27
        {
            "subtopic": "Tamil Nadu Exemption from 1976 Rules",
            "stem_en": "[TNPSC Group 1 2019, Group 2 2021]\nUnder Rule 1(2) of the Official Languages Rules, 1976, which State of the Indian Union is explicitly exempted from the operation of these rules?",
            "stem_ta": "[TNPSC குரூப் 1 2019, குரூப் 2 2021]\nஅதிகாரப்பூர்வ மொழிகள் விதிகள் 1976-ன் விதி 1(2)-ன் கீழ், இந்திய ஒன்றியத்தின் எந்த மாநிலம் இவ்விதிகளின் செயல்பாட்டிலிருந்து வெளிப்படையாக விலக்களிக்கப்பட்டுள்ளது?",
            "options": [
                ("Tamil Nadu", "தமிழ்நாடு"),
                ("Kerala", "கேரளா"),
                ("Jammu and Kashmir", "ஜம்மு காஷ்மீர்"),
                ("Nagaland", "நாகாலாந்து")
            ],
            "correct_key": "A",
            "exp_en": "Rule 1(2) of the Official Languages Rules, 1976 states: 'They shall extend to the whole of India, except the State of Tamil Nadu.'",
            "exp_ta": "அதிகாரப்பூர்வ மொழிகள் விதிகள் 1976-ன் விதி 1(2) கூறுகிறது: 'இவ்விதிகள் தமிழ்நாடு மாநிலம் நீங்கலாக இந்தியா முழுவதும் பொருந்தும்.'",
            "why_a_en": "Tamil Nadu is expressly exempted under Rule 1(2).",
            "why_a_ta": "விதி 1(2)-ன் கீழ் தமிழ்நாட்டிற்கு வெளிப்படையாக விலக்களிக்கப்பட்டுள்ளது.",
            "why_b_en": "Kerala is classified in Region C and subject to the rules.",
            "why_b_ta": "கேரளா பிராந்தியம் C-ல் வகைப்படுத்தப்பட்டு விதிகளுக்கு உட்பட்டது.",
            "why_c_en": "Jammu & Kashmir is not exempted under Rule 1(2).",
            "why_c_ta": "விதி 1(2)-ன் கீழ் ஜம்மு காஷ்மீருக்கு விலக்களிக்கப்படவில்லை.",
            "why_d_en": "Nagaland is in Region C, not exempted under Rule 1(2).",
            "why_d_ta": "நாகாலாந்து பிராந்தியம் C-ல் உள்ளது, விதி 1(2)-ன் கீழ் விலக்களிக்கப்படவில்லை.",
            "tip_en": "High-yield TNPSC specialty: Tamil Nadu is the ONLY state exempted under Rule 1(2) of 1976 Rules.",
            "tip_ta": "முக்கிய TNPSC வினா: 1976 விதிகளின் விதி 1(2)-ன் கீழ் விலக்கு அளிக்கப்பட்ட ஒரே மாநிலம் தமிழ்நாடு மட்டுமே.",
            "fact_en": "Central Government offices located in Tamil Nadu communicate with Union Headquarters exclusively in English.",
            "fact_ta": "தமிழ்நாட்டில் அமைந்துள்ள மத்திய அரசு அலுவலகங்கள் ஒன்றியத் தலைமையகத்துடன் ஆங்கிலத்தில் மட்டுமே தொடர்பு கொள்கின்றன."
        },
        # 28
        {
            "subtopic": "Department of Official Language Ministry",
            "stem_en": "[TNPSC Group 2 2018]\nWhich Union Ministry has administrative charge of the Department of Official Language (Rajbhasha Vibhag)?",
            "stem_ta": "[TNPSC குரூப் 2 2018]\nஅதிகாரப்பூர்வ மொழித் துறையை (ராஜ்பாஷா விபாக்) நிர்வாகக் கட்டுப்பாட்டில் கொண்டுள்ள மத்திய அமைச்சகம் எது?",
            "options": [
                ("Ministry of Home Affairs", "உள்துறை அமைச்சகம்"),
                ("Ministry of Education", "கல்வி அமைச்சகம்"),
                ("Ministry of Culture", "பண்பாட்டு அமைச்சகம்"),
                ("Ministry of Law and Justice", "சட்டம் மற்றும் நீதித்துறை அமைச்சகம்")
            ],
            "correct_key": "A",
            "exp_en": "The Department of Official Language was set up in June 1975 as an independent Department of the Ministry of Home Affairs to oversee compliance with constitutional and statutory language provisions.",
            "exp_ta": "அரசியலமைப்பு மற்றும் சட்டப்பூர்வ மொழி விதிகளை நடைமுறைப்படுத்துவதைக் கண்காணிக்க ஜூன் 1975-ல் உள்துறை அமைச்சகத்தின் கீழ் ஒரு சுதந்திரமான துறையாக அதிகாரப்பூர்வ மொழித் துறை அமைக்கப்பட்டது.",
            "why_a_en": "Ministry of Home Affairs houses the Department of Official Language.",
            "why_a_ta": "உள்துறை அமைச்சகம் அதிகாரப்பூர்வ மொழித் துறையைக் கொண்டுள்ளது.",
            "why_b_en": "Ministry of Education oversees language promotion and Central Institute of Indian Languages (CIIL).",
            "why_b_ta": "கல்வி அமைச்சகம் மொழிக் கல்வி மற்றும் இந்திய மொழிகளின் மத்திய நிறுவனத்தை (CIIL) மேற்பார்வையிடுகிறது.",
            "why_c_en": "Ministry of Culture administers Classical Language grants.",
            "why_c_ta": "பண்பாட்டு அமைச்சகம் செம்மொழி மானியங்களை நிர்வகிக்கிறது.",
            "why_d_en": "Ministry of Law handles legislative drafting in Hindi.",
            "why_d_ta": "சட்ட அமைச்சகம் இந்தியில் சட்ட வரைவுப் பணிகளைக் கையாள்கிறது.",
            "tip_en": "Remember: Rajbhasha = Ministry of Home Affairs (headed by Union Home Minister).",
            "tip_ta": "நினைவில் கொள்க: ராஜ்பாஷா = உள்துறை அமைச்சகம் (மத்திய உள்துறை அமைச்சரின் தலைமையில்).",
            "fact_en": "The Department issues annual programmes fixing targets for Hindi correspondence in central offices.",
            "fact_ta": "மத்திய அலுவலகங்களில் இந்தி கடிதப் போக்குவரத்திற்கான இலக்குகளை நிர்ணயிக்கும் வருடாந்திர திட்டங்களை இத்துறை வெளியிடுகிறது."
        },
        # 29
        {
            "subtopic": "Kendriya Hindi Samiti Leadership",
            "stem_en": "[TNPSC Group 1 2016]\nWho serves as the ex-officio Chairman of the Kendriya Hindi Samiti (Central Hindi Committee), the supreme policy body for official language implementation?",
            "stem_ta": "[TNPSC குரூப் 1 2016]\nஅதிகாரப்பூர்வ மொழி அமலாக்கத்திற்கான உச்சபட்ச கொள்கை அமைப்பான கேந்திரிய இந்தி சமிதியின் (மத்திய இந்தி குழு) அலுவல் வழித் தலைவராக இருப்பவர் யார்?",
            "options": [
                ("Prime Minister of India", "இந்தியப் பிரதமர்"),
                ("President of India", "இந்தியக் குடியரசுத் தலைவர்"),
                ("Union Home Minister", "மத்திய உள்துறை அமைச்சர்"),
                ("Speaker of the Lok Sabha", "மக்களவைத் தலைவர்")
            ],
            "correct_key": "A",
            "exp_en": "The Kendriya Hindi Samiti was constituted in 1967 and is chaired by the Prime Minister of India. It is the apex body that coordinates official language policies across all Union ministries.",
            "exp_ta": "கேந்திரிய இந்தி சமிதி 1967-ல் அமைக்கப்பட்டது மற்றும் இந்தியப் பிரதமரின் தலைமையில் இயங்குகிறது. இது அனைத்து மத்திய அமைச்சகங்களிலும் அதிகாரப்பூர்வ மொழிக் கொள்கைகளை ஒருங்கிணைக்கும் உச்ச அமைப்பாகும்.",
            "why_a_en": "The Prime Minister is the ex-officio Chairman of the Kendriya Hindi Samiti.",
            "why_a_ta": "இந்தியப் பிரதமர் கேந்திரிய இந்தி சமிதியின் அலுவல் வழித் தலைவராவார்.",
            "why_b_en": "President receives reports under Article 344, but does not chair this committee.",
            "why_b_ta": "குடியரசுத் தலைவர் சரத்து 344-ன் கீழ் அறிக்கைகளைப் பெறுகிறார், ஆனால் இக்குழுவுக்குத் தலைமை தாங்குவதில்லை.",
            "why_c_en": "Union Home Minister is the Deputy Chairman of Kendriya Hindi Samiti.",
            "why_c_ta": "மத்திய உள்துறை அமைச்சர் கேந்திரிய இந்தி சமிதியின் துணைத் தலைவராவார்.",
            "why_d_en": "The Speaker has no role in the executive committee.",
            "why_d_ta": "மக்களவைத் தலைவருக்கு இந்த நிர்வாகக் குழுவில் எவ்விதப் பங்கும் இல்லை.",
            "tip_en": "Apex bodies: Kendriya Hindi Samiti = chaired by PM; Parliamentary Committee on Official Language = traditionally chaired by Home Minister.",
            "tip_ta": "முக்கிய தலைமை: கேந்திரிய இந்தி சமிதி = பிரதமர் தலைமை; அதிகாரப்பூர்வ மொழிக்கான நாடாளுமன்றக் குழு = வழக்கமாக உள்துறை அமைச்சர் தலைமை.",
            "fact_en": "Includes select Cabinet ministers, Chief Ministers, and language experts as members.",
            "fact_ta": "தேர்ந்தெடுக்கப்பட்ட மத்திய அமைச்சர்கள், முதலமைச்சர்கள் மற்றும் மொழி வல்லுநர்களை உறுப்பினர்களாகக் கொண்டுள்ளது."
        },
        # 30
        {
            "subtopic": "96th Constitutional Amendment Act 2011",
            "stem_en": "[TNPSC Group 4 2014, Group 2 2015]\nThe 96th Constitutional Amendment Act, 2011 substituted which language name in the Eighth Schedule?",
            "stem_ta": "[TNPSC குரூப் 4 2014, குரூப் 2 2015]\n2011-ன் 96வது அரசியலமைப்பு திருத்தச் சட்டம் எட்டாவது அட்டவணையில் எந்த மொழிப் பெயரை மாற்றியமைத்தது?",
            "options": [
                ("Substituted 'Odia' for 'Oriya'", "'ஒரியா' என்பதற்குப் பதிலாக 'ஒடியா' என மாற்றியது"),
                ("Substituted 'Bangla' for 'Bengali'", "'பெங்காலி' என்பதற்குப் பதிலாக 'பங்களா' என மாற்றியது"),
                ("Substituted 'Asamiya' for 'Assamese'", "'அஸ்ஸாமி' என்பதற்குப் பதிலாக 'அசாமியா' என மாற்றியது"),
                ("Substituted 'Kashmiri' for 'Kashur'", "'காஷூர்' என்பதற்குப் பதிலாக 'காஷ்மீரி' என மாற்றியது")
            ],
            "correct_key": "A",
            "exp_en": "The 96th Constitutional Amendment Act, 2011 amended the Eighth Schedule by substituting the entry 'Odia' for 'Oriya', reflecting the authentic pronunciation of the language.",
            "exp_ta": "2011-ன் 96வது அரசியலமைப்பு திருத்தச் சட்டம் எட்டாவது அட்டவணையில் 'ஒரியா' என்ற பதிவிற்குப் பதிலாக 'ஒடியா' என்று மாற்றி மொழியின் உண்மையான உச்சரிப்பைப் பிரதிபலித்தது.",
            "why_a_en": "96th CAA substituted 'Odia' for 'Oriya' in the Eighth Schedule.",
            "why_a_ta": "96வது திருத்தம் எட்டாவது அட்டவணையில் 'ஒரியா'வுக்குப் பதிலாக 'ஒடியா' என மாற்றியது.",
            "why_b_en": "Bangla has not been substituted in the Constitution.",
            "why_b_ta": "பங்களா அரசியலமைப்பில் மாற்றப்படவில்லை.",
            "why_c_en": "Asamiya is not the official Eighth Schedule entry.",
            "why_c_ta": "அசாமியா என்பது எட்டாவது அட்டவணைப் பதிவு அல்ல.",
            "why_d_en": "Kashmir entry remains Kashmiri.",
            "why_d_ta": "காஷ்மீர் பதிவு காஷ்மீரி என்றே நீடிக்கிறது.",
            "tip_en": "Simultaneously, the Orissa (Alteration of Name) Act, 2011 changed the state's name from 'Orissa' to 'Odisha'.",
            "tip_ta": "அதே நேரத்தில், ஒரிசா (பெயர் மாற்றம்) சட்டம் 2011 மாநிலத்தின் பெயரை 'ஒரிசா'விலிருந்து 'ஒடிசா' என மாற்றியது.",
            "fact_en": "State name change falls under Article 3; language name change in 8th Schedule required constitutional amendment under Article 368.",
            "fact_ta": "மாநிலப் பெயர் மாற்றம் சரத்து 3-ன் கீழ் வருகிறது; 8வது அட்டவணையில் மொழிப் பெயர் மாற்றம் சரத்து 368-ன் கீழ் அரசியலமைப்புத் திருத்தத்தைக் கோரியது."
        },
        # 31
        {
            "subtopic": "Kher Commission Report Submission",
            "stem_en": "[TNPSC Group 1 2017]\nIn which year did the B.G. Kher Official Language Commission submit its comprehensive report to the President of India?",
            "stem_ta": "[TNPSC குரூப் 1 2017]\nபி.ஜி. கேர் அதிகாரப்பூர்வ மொழி ஆணையம் தனது விரிவான அறிக்கையை இந்தியக் குடியரசுத் தலைவரிடம் சமர்ப்பித்த ஆண்டு எது?",
            "options": [
                ("1956", "1956"),
                ("1955", "1955"),
                ("1957", "1957"),
                ("1960", "1960")
            ],
            "correct_key": "A",
            "exp_en": "Appointed in June 1955, the B.G. Kher Commission submitted its final report to President Dr. Rajendra Prasad in 1956, and it was tabled in Parliament in 1957.",
            "exp_ta": "ஜூன் 1955-ல் நியமிக்கப்பட்ட பி.ஜி. கேர் ஆணையம் தனது இறுதி அறிக்கையை 1956-ல் குடியரசுத் தலைவர் டாக்டர் ராஜேந்திர பிரசாத்திடம் சமர்ப்பித்தது, அது 1957-ல் நாடாளுமன்றத்தில் வைக்கப்பட்டது.",
            "why_a_en": "1956 was the year of submission of the Kher report.",
            "why_a_ta": "1956 கேர் அறிக்கை சமர்ப்பிக்கப்பட்ட ஆண்டாகும்.",
            "why_b_en": "1955 was the year of appointment.",
            "why_b_ta": "1955 ஆணையம் அமைக்கப்பட்ட ஆண்டாகும்.",
            "why_c_en": "1957 was when the Parliamentary Committee under G.B. Pant was constituted.",
            "why_c_ta": "1957-ல் ஜி.பி. பந்த் தலைமையிலான நாடாளுமன்றக் குழு அமைக்கப்பட்டது.",
            "why_d_en": "1960 was when the President issued an order based on Pant committee findings.",
            "why_d_ta": "1960-ல் பந்த் குழு பரிந்துரைகளின் அடிப்படையில் குடியரசுத் தலைவர் உத்தரவு பிறப்பித்தார்.",
            "tip_en": "Timeline: Appointed 1955 -> Submitted 1956 -> Examined 1957–1958 -> Presidential Order 1960.",
            "tip_ta": "காலக்கோடு: நியமனம் 1955 -> சமர்ப்பிப்பு 1956 -> ஆய்வு 1957–1958 -> குடியரசுத் தலைவர் உத்தரவு 1960.",
            "fact_en": "The report recommended making Hindi the sole official language progressively, sparking strong protests in non-Hindi areas.",
            "fact_ta": "இந்தியைப் படிப்படியாக ஒரே அதிகாரப்பூர்வ மொழியாக்க இந்த அறிக்கை பரிந்துரைத்தது, இது இந்தி பேசாத பகுதிகளில் கடுமையான எதிர்ப்பைத் தூண்டியது."
        },
        # 32
        {
            "subtopic": "Parliamentary Committee Election Method",
            "stem_en": "[TNPSC Group 1 2021]\nUnder Article 344(4), what electoral system is used to elect members of the Parliamentary Committee on Official Language from both Houses of Parliament?",
            "stem_ta": "[TNPSC குரூப் 1 2021]\nசரத்து 344(4)-ன் கீழ் நாடாளுமன்றத்தின் இரு அவைகளிலிருந்தும் அதிகாரப்பூர்வ மொழிக்கான நாடாளுமன்றக் குழு உறுப்பினர்களைத் தேர்ந்தெடுக்கப் பயன்படுத்தப்படும் தேர்தல் முறை எது?",
            "options": [
                ("System of proportional representation by means of the single transferable vote", "ஒற்றை மாற்று வாக்கு மூலம் விகிதாச்சார பிரதிநிதித்துவ முறை"),
                ("First-past-the-post system by simple majority", "சாதாரண பெரும்பான்மை கொண்ட முன்னிலை வாக்கு முறை"),
                ("Direct nomination by the Prime Minister", "பிரதமரால் நேரடியாக நியமனம் செய்தல்"),
                ("Seniority-based automatic membership", "மூப்பு அடிப்படையிலான தானியங்கி உறுப்பினர் தகுதி")
            ],
            "correct_key": "A",
            "exp_en": "Article 344(4) explicitly specifies that the members of the Committee shall be elected respectively by the members of the Lok Sabha and the Rajya Sabha in accordance with the system of proportional representation by means of the single transferable vote.",
            "exp_ta": "சரத்து 344(4) மக்களவை மற்றும் மாநிலங்களவை உறுப்பினர்களால் ஒற்றை மாற்று வாக்கு மூலம் விகிதாச்சார பிரதிநிதித்துவ முறையின்படி இக்குழு உறுப்பினர்கள் தேர்ந்தெடுக்கப்பட வேண்டும் என்று வெளிப்படையாகக் குறிப்பிடுகிறது.",
            "why_a_en": "Article 344(4) mandates proportional representation by single transferable vote.",
            "why_a_ta": "சரத்து 344(4) ஒற்றை மாற்று வாக்கு மூலமான விகிதாச்சார பிரதிநிதித்துவ முறையைக் கட்டாயமாக்குகிறது.",
            "why_b_en": "FPTP is used for general elections, not parliamentary committees.",
            "why_b_ta": "பொதுத் தேர்தல்களுக்கு முன்னிலை முறை பயன்படுகிறது, நாடாளுமன்றக் குழுக்களுக்கு அல்ல.",
            "why_c_en": "Prime Minister does not nominate the members.",
            "why_c_ta": "பிரதமர் உறுப்பினர்களை நியமிப்பதில்லை.",
            "why_d_en": "Membership is elective, not seniority-based.",
            "why_d_ta": "உறுப்பினர் பதவி தேர்தலுக்குரியது, மூப்பு அடிப்படையிலானது அல்ல.",
            "tip_en": "Ensures minority parties and regional states have proportional voice on the committee.",
            "tip_ta": "சிறுபான்மை கட்சிகளும் மாநிலங்களும் குழுவில் விகிதாச்சாரக் குரலைக் கொண்டிருப்பதை இது உறுதி செய்கிறது.",
            "fact_en": "Similar election method is used for Public Accounts Committee and Committee on Estimates.",
            "fact_ta": "பொதுக் கணக்குக் குழு மற்றும் மதிப்பீட்டுக் குழுவிற்கும் இதே தேர்தல் முறை பயன்படுத்தப்படுகிறது."
        },
        # 33
        {
            "subtopic": "State Official Language Article 345 Scope",
            "stem_en": "[TNPSC Group 2 2016]\nUnder Article 345 of the Constitution of India, a State Legislature may adopt:",
            "stem_ta": "[TNPSC குரூப் 2 2016]\nஇந்திய அரசியலமைப்பின் சரத்து 345-ன் கீழ் ஒரு மாநில சட்டமன்றம் எதை அதிகாரப்பூர்வ மொழியாக ஏற்கலாம்?",
            "options": [
                ("Any one or more of the languages in use in the State or Hindi", "மாநிலத்தில் பயன்பாட்டிலுள்ள மொழிகளில் ஏதேனும் ஒன்று அல்லது அதற்கு மேற்பட்டவை அல்லது இந்தி"),
                ("Only languages listed in the Eighth Schedule", "எட்டாவது அட்டவணையில் பட்டியலிடப்பட்டுள்ள மொழிகளை மட்டுமே"),
                ("Exclusively Hindi as mandated by the Union", "ஒன்றியத்தால் கட்டாயப்படுத்தப்படும் இந்தியை மட்டுமே"),
                ("Only English until Parliament grants statehood", "நாடாளுமன்றம் அனுமதிக்கும் வரை ஆங்கிலத்தை மட்டுமே")
            ],
            "correct_key": "A",
            "exp_en": "Article 345 provides that the Legislature of a State may by law adopt any one or more of the languages in use in the State or Hindi as the language or languages to be used for all or any of the official purposes of that State.",
            "exp_ta": "சரத்து 345 ஒரு மாநில சட்டமன்றம் சட்டத்தின் மூலம் மாநிலத்தில் பயன்பாட்டில் உள்ள மொழிகளில் ஏதேனும் ஒன்றையோ அல்லது பலவற்றையோ அல்லது இந்தியையோ அம்மாநிலத்தின் அனைத்து அல்லது ஏதேனும் அதிகாரப்பூர்வ பணிகளுக்கான மொழியாக ஏற்றுக்கொள்ளலாம் என்று கூறுகிறது.",
            "why_a_en": "Article 345 allows any language in use in the State or Hindi.",
            "why_a_ta": "சரத்து 345 மாநிலத்தில் வழக்கிலுள்ள ஏதேனும் மொழி அல்லது இந்தியை ஏற்க அனுமதிக்கிறது.",
            "why_b_en": "The language need not be restricted to the Eighth Schedule.",
            "why_b_ta": "மொழி எட்டாவது அட்டவணையுடன் மட்டும் வரையறுக்கப்பட வேண்டியதில்லை.",
            "why_c_en": "The Union cannot impose Hindi upon State legislatures.",
            "why_c_ta": "ஒன்றியம் மாநில சட்டமன்றங்கள் மீது இந்தியைத் திணிக்க முடியாது.",
            "why_d_en": "States have complete constitutional autonomy under Article 345.",
            "why_d_ta": "சரத்து 345-ன் கீழ் மாநிலங்களுக்கு முழு அரசியலமைப்பு சுயாட்சி உள்ளது.",
            "tip_en": "Key freedom: States are NOT bound to choose Hindi or Eighth Schedule languages under Article 345.",
            "tip_ta": "முக்கிய சுதந்திரம்: சரத்து 345-ன் கீழ் மாநிலங்கள் இந்தியை அல்லது 8வது அட்டவணை மொழிகளை மட்டுமே தேர்வு செய்யக் கட்டுப்பட்டவை அல்ல.",
            "fact_en": "For instance, Meghalaya and Nagaland adopted English as their sole official language under Article 345.",
            "fact_ta": "எடுத்துக்காட்டாக, மேகாலயாவும் நாகாலாந்தும் சரத்து 345-ன் கீழ் ஆங்கிலத்தைத் தங்கள் ஒரே அதிகாரப்பூர்வ மொழியாக ஏற்றுக்கொண்டன."
        },
        # 34
        {
            "subtopic": "Default State Language Article 345 Proviso",
            "stem_en": "[TNPSC Group 4 2015]\nAccording to the proviso to Article 345, until the Legislature of the State otherwise provides by law, what language was to continue for all official purposes within the State?",
            "stem_ta": "[TNPSC குரூப் 4 2015]\nசரத்து 345-ன் வரம்புரையின்படி, மாநில சட்டமன்றம் சட்டத்தின் மூலம் வேறு ஏற்பாடு செய்யும் வரை, மாநிலத்திற்குள் அனைத்து அதிகாரப்பூர்வ பயன்பாடுகளுக்கும் எந்த மொழி தொடர்ந்து பயன்பாட்டில் இருக்க வேண்டும்?",
            "options": [
                ("English language", "ஆங்கில மொழி"),
                ("Hindi in Devanagari script", "தேவநாகரி வரிவடிவத்திலான இந்தி"),
                ("Sanskrit language", "சமஸ்கிருத மொழி"),
                ("Urdu language", "உருது மொழி")
            ],
            "correct_key": "A",
            "exp_en": "The proviso to Article 345 states that until the Legislature of the State otherwise provides by law, the English language shall continue to be used for those official purposes within the State for which it was being used immediately before the commencement of the Constitution.",
            "exp_ta": "சரத்து 345-ன் வரம்புரை, மாநில சட்டமன்றம் சட்டத்தால் வேறுவிதமாக ஏற்பாடு செய்யும் வரை, அரசியலமைப்பு தொடங்குவதற்கு முன்னர் அம்மாநிலத்தில் எந்தெந்த பயன்பாடுகளுக்கு ஆங்கிலம் பயன்படுத்தப்பட்டதோ அவற்றிற்கு ஆங்கிலமே தொடர்ந்து பயன்படுத்தப்படும் என்று கூறுகிறது.",
            "why_a_en": "English was the default continuing language under Article 345 proviso.",
            "why_a_ta": "சரத்து 345 வரம்புரையின் கீழ் ஆங்கிலமே தொடக்கநிலைத் தொடர்ச்சி மொழியாக இருந்தது.",
            "why_b_en": "Hindi was not the default language for States.",
            "why_b_ta": "இந்தி மாநிலங்களுக்கான இயல்புநிலை மொழி அல்ல.",
            "why_c_en": "Sanskrit was never a default administrative language.",
            "why_c_ta": "சமஸ்கிருதம் நிர்வாக இயல்புநிலை மொழியாக இருந்ததில்லை.",
            "why_d_en": "Urdu was not the default language.",
            "why_d_ta": "உருது இயல்புநிலை மொழி அல்ல.",
            "tip_en": "Ensured seamless transition and prevented administrative collapse in states after 1950.",
            "tip_ta": "1950-க்குப் பிறகு நிர்வாகத் தடங்கலின்றி மாநிலங்கள் தொடர்ந்து இயங்குவதை இது உறுதி செய்தது.",
            "fact_en": "Tamil Nadu passed the Tamil Nadu Official Language Act in 1956 adopting Tamil.",
            "fact_ta": "தமிழ்நாடு 1956-ல் தமிழ்நாடு அதிகாரப்பூர்வ மொழிச் சட்டத்தை இயற்றி தமிழை ஏற்றுக்கொண்டது."
        },
        # 35
        {
            "subtopic": "Inter-State Communication Article 346",
            "stem_en": "[TNPSC Group 1 2018]\nUnder Article 346, what is the authorized language for communication between one State and another State or between a State and the Union?",
            "stem_ta": "[TNPSC குரூப் 1 2018]\nசரத்து 346-ன் கீழ், ஒரு மாநிலத்திற்கும் மற்றொரு மாநிலத்திற்கும் இடையே அல்லது ஒரு மாநிலத்திற்கும் ஒன்றியத்திற்கும் இடையிலான தகவல்தொடர்புக்கு அங்கீகரிக்கப்பட்ட மொழி எது?",
            "options": [
                ("The language for the time being authorized for use in the Union for official purposes", "அப்போதைக்கு ஒன்றியத்தின் அதிகாரப்பூர்வ பயன்பாட்டிற்கு அங்கீகரிக்கப்பட்டுள்ள மொழி"),
                ("Exclusively Hindi in Devanagari script", "தேவநாகரி வரிவடிவத்திலான இந்தி மட்டுமே"),
                ("The regional language of the larger communicating State", "தொடர்பு கொள்ளும் பெரிய மாநிலத்தின் வட்டார மொழி"),
                ("Sanskrit language", "சமஸ்கிருத மொழி")
            ],
            "correct_key": "A",
            "exp_en": "Article 346 provides that the language for the time being authorized for use in the Union for official purposes shall be the official language for communication between one State and another State and between a State and the Union.",
            "exp_ta": "சரத்து 346 ஒன்றியத்தில் அப்போதைக்கு அதிகாரப்பூர்வ பயன்பாட்டிற்கு அங்கீகரிக்கப்பட்டுள்ள மொழியே மாநிலங்களுக்கு இடையிலான மற்றும் மாநிலத்திற்கும் ஒன்றியத்திற்கும் இடையிலான தொடர்பாடல் மொழியாக இருக்கும் என்று கூறுகிறது.",
            "why_a_en": "Article 346 specifies the authorized Union language (currently Hindi and English).",
            "why_a_ta": "சரத்து 346 ஒன்றியத்திற்கு அங்கீகரிக்கப்பட்ட மொழியையே (இந்தி மற்றும் ஆங்கிலம்) குறிப்பிடுகிறது.",
            "why_b_en": "Hindi is not the exclusive language; English is authorized under 1963 Act.",
            "why_b_ta": "இந்தி மட்டுமேயான மொழி அல்ல; 1963 சட்டத்தின் கீழ் ஆங்கிலமும் அங்கீகரிக்கப்பட்டுள்ளது.",
            "why_c_en": "State regional languages are not the inter-state link language.",
            "why_c_ta": "மாநில வட்டார மொழிகள் மாநிலங்களுக்கு இடையேயான இணைப்பு மொழியல்ல.",
            "why_d_en": "Sanskrit is not the inter-state communication language.",
            "why_d_ta": "சமஸ்கிருதம் மாநிலங்களுக்கு இடையேயான தொடர்பாடல் மொழி அல்ல.",
            "tip_en": "Official Languages Act 1963 Section 3(1)(c) mandates English translations for Hindi communications sent to non-Hindi states.",
            "tip_ta": "அதிகாரப்பூர்வ மொழிகள் சட்டம் 1963 பிரிவு 3(1)(c) இந்தி பேசாத மாநிலங்களுக்கு அனுப்பப்படும் இந்தி கடிதங்களுக்கு ஆங்கில மொழிபெயர்ப்பைக் கட்டாயமாக்குகிறது.",
            "fact_en": "Article 346 proviso allows two agreeing states to communicate in Hindi.",
            "fact_ta": "சரத்து 346 வரம்புரை இரு மாநிலங்கள் ஒப்புக்கொண்டால் தங்களுக்குள் இந்தியில் தொடர்பு கொள்ள அனுமதிக்கிறது."
        },
        # 36
        {
            "subtopic": "Article 346 Proviso Bilateral Hindi Agreement",
            "stem_en": "[TNPSC Group 2 2019]\nUnder the proviso to Article 346 of the Indian Constitution, if two or more States agree that Hindi should be the official language for communication between such States, that communication:",
            "stem_ta": "[TNPSC குரூப் 2 2019]\nஇந்திய அரசியலமைப்பின் சரத்து 346-ன் வரம்புரையின் கீழ், இரண்டு அல்லது அதற்கு மேற்பட்ட மாநிலங்கள் தங்களுக்கு இடையேயான தகவல்தொடர்புக்கு இந்தி அதிகாரப்பூர்வ மொழியாக இருக்க வேண்டும் என்று ஒப்புக்கொண்டால், அத்தொடர்பாடல்:",
            "options": [
                ("May be in the Hindi language", "இந்தி மொழியில் இருக்கலாம்"),
                ("Must still be accompanied by mandatory English text", "கட்டாயமாக ஆங்கில உரையுடன் மட்டுமே இருக்க வேண்டும்"),
                ("Requires prior permission of the Supreme Court", "உச்ச நீதிமன்றத்தின் முன் அனுமதி தேவைப்படும்"),
                ("Is null and void under federal balance principles", "கூட்டாட்சி சமநிலை விதிகளின் கீழ் செல்லாததாகும்")
            ],
            "correct_key": "A",
            "exp_en": "The proviso to Article 346 states: 'Provided that if two or more States agree that the Hindi language should be the official language for communication between such States, that language may be used for such communication.'",
            "exp_ta": "சரத்து 346-ன் வரம்புரை கூறுகிறது: 'இரண்டு அல்லது அதற்கு மேற்பட்ட மாநிலங்கள் தங்களுக்கு இடையிலான தகவல்தொடர்புக்கு இந்தி மொழியே அதிகாரப்பூர்வ மொழியாக இருக்க வேண்டும் என்று உடன்பட்டால், அத்தகைய தகவல்தொடர்புக்கு இந்தி மொழி பயன்படுத்தப்படலாம்.'",
            "why_a_en": "Article 346 proviso explicitly permits Hindi communication between agreeing States.",
            "why_a_ta": "சரத்து 346 வரம்புரை ஒப்புக்கொள்ளும் மாநிலங்கள் இந்தியில் தொடர்பு கொள்ள வெளிப்படையாக அனுமதிக்கிறது.",
            "why_b_en": "English is not mandatory between two Hindi-agreeing States.",
            "why_b_ta": "இந்தியை ஏற்கும் இரு மாநிலங்களுக்கு இடையே ஆங்கிலம் கட்டாயமில்லை.",
            "why_c_en": "Supreme Court permission is not needed.",
            "why_c_ta": "உச்ச நீதிமன்ற அனுமதி தேவையில்லை.",
            "why_d_en": "It is constitutionally valid and recognized.",
            "why_d_ta": "இது அரசியலமைப்பு ரீதியாக செல்லுபடியாகும் அங்கீகரிக்கப்பட்ட விதியாகும்.",
            "tip_en": "Hindi heartland states (e.g. UP, MP, Bihar, Rajasthan) communicate with each other in Hindi under this proviso.",
            "tip_ta": "இந்தி பேசும் மாநிலங்கள் (எ.கா. உ.பி, ம.பி, பீகார், ராஜஸ்தான்) இந்த வரம்புரையின் கீழ் தங்களுக்குள் இந்தியில் தொடர்பு கொள்கின்றன.",
            "fact_en": "Non-Hindi states cannot be forced to enter into such bilateral agreements.",
            "fact_ta": "இந்தி பேசாத மாநிலங்களை அத்தகைய இருதரப்பு ஒப்பந்தங்களில் ஈடுபட கட்டாயப்படுத்த முடியாது."
        },
        # 37
        {
            "subtopic": "Article 347 Presidential Power for Minority Languages",
            "stem_en": "[TNPSC Group 1 2020]\nUnder Article 347 of the Constitution of India, who has the power to direct that a language spoken by a substantial proportion of the population of a State shall also be officially recognized throughout that State or any part thereof?",
            "stem_ta": "[TNPSC குரூப் 1 2020]\nஇந்திய அரசியலமைப்பின் சரத்து 347-ன் கீழ், ஒரு மாநிலத்தின் மக்கட்தொகையில் குறிப்பிடத்தக்க பகுதியினரால் பேசப்படும் ஒரு மொழியை அம்மாநிலம் முழுவதிலும் அல்லது ஏதேனும் ஒரு பகுதியிலும் அதிகாரப்பூர்வமாக அங்கீகரிக்குமாறு உத்தரவிட யாருக்கு அதிகாரமுள்ளது?",
            "options": [
                ("The President of India", "இந்தியக் குடியரசுத் தலைவர்"),
                ("The Governor of the State", "மாநில ஆளுநர்"),
                ("The Chief Minister of the State", "மாநில முதலமைச்சர்"),
                ("The Speaker of the State Assembly", "மாநில சட்டமன்றத் தலைவர்")
            ],
            "correct_key": "A",
            "exp_en": "Article 347 provides that on a demand being made, the President may, if satisfied that a substantial proportion of the population of a State desire the use of any language spoken by them, direct that such language shall also be officially recognized throughout that State or any part thereof.",
            "exp_ta": "சரத்து 347 ஒரு மாநிலத்தின் மக்கட்தொகையில் கணிசமான பகுதியினர் தங்களால் பேசப்படும் மொழியைப் பயன்படுத்த விரும்புகின்றனர் என்று கோரிக்கை விடுக்கப்பட்டு குடியரசுத் தலைவர் திருப்தியுற்றால், அந்த மொழியையும் மாநிலம் முழுவதும் அல்லது ஏதேனும் ஒரு பகுதியில் அதிகாரப்பூர்வமாக அங்கீகரிக்குமாறு அவர் உத்தரவிடலாம் என்று கூறுகிறது.",
            "why_a_en": "Article 347 explicitly vests this power in the President of India.",
            "why_a_ta": "சரத்து 347 இந்த அதிகாரத்தை இந்தியக் குடியரசுத் தலைவரிடம் வழங்குகிறது.",
            "why_b_en": "The Governor does not issue directions under Article 347.",
            "why_b_ta": "ஆளுநர் சரத்து 347-ன் கீழ் உத்தரவுகளைப் பிறப்பிப்பதில்லை.",
            "why_c_en": "The Chief Minister has no such directive power.",
            "why_c_ta": "முதலமைச்சருக்கு அத்தகைய உத்தரவிடும் அதிகாரம் இல்லை.",
            "why_d_en": "The Speaker is limited to presiding over the House.",
            "why_d_ta": "சபாநாயகர் அவைக்குத் தலைமை தாங்குவதோடு மட்டுப்படுத்தப்பட்டவர்.",
            "tip_en": "Article 347 protects substantial linguistic minorities (e.g., Urdu in Bihar/UP, Bengali in parts of Assam).",
            "tip_ta": "சரத்து 347 கணிசமான மொழிச் சிறுபான்மையினரைப் பாதுகாக்கிறது (எ.கா. பீகார்/உ.பி-யில் உருது, அசாமின் சில பகுதிகளில் பெங்காலி).",
            "fact_en": "Requires satisfaction of the President based on a formal demand made by the speakers.",
            "fact_ta": "பேசுபவர்களால் விடுக்கப்படும் முறையான கோரிக்கையின் பேரில் குடியரசுத் தலைவரின் திருப்தி இதற்குத் தேவைப்படுகிறது."
        },
        # 38
        {
            "subtopic": "1957 Pant Committee Examination",
            "stem_en": "[TNPSC Group 1 2015]\nWhich Parliamentary Committee was constituted in September 1957 to examine the recommendations of the Official Language Commission (Kher Commission)?",
            "stem_ta": "[TNPSC குரூப் 1 2015]\nஅதிகாரப்பூர்வ மொழி ஆணையத்தின் (கேர் ஆணையம்) பரிந்துரைகளை ஆய்வு செய்வதற்காக செப்டம்பர் 1957-ல் அமைக்கப்பட்ட நாடாளுமன்றக் குழு எது?",
            "options": [
                ("Committee chaired by Govind Ballabh Pant", "கோவிந்த் வல்லப் பந்த் தலைமையிலான குழு"),
                ("Committee chaired by Lal Bahadur Shastri", "லால் பகதூர் சாஸ்திரி தலைமையிலான குழு"),
                ("Committee chaired by Morarji Desai", "மொரார்ஜி தேசாய் தலைமையிலான குழு"),
                ("Committee chaired by C. Rajagopalachari", "சி. ராஜகோபாலாச்சாரி தலைமையிலான குழு")
            ],
            "correct_key": "A",
            "exp_en": "In September 1957, a 30-member Parliamentary Committee on Official Language was constituted under the chairmanship of Union Home Minister Govind Ballabh Pant to examine the Kher Commission report.",
            "exp_ta": "செப்டம்பர் 1957-ல், கேர் ஆணைய அறிக்கையை ஆய்வு செய்வதற்காக மத்திய உள்துறை அமைச்சர் கோவிந்த் வல்லப் பந்த் தலைமையில் 30 உறுப்பினர்களைக் கொண்ட நாடாளுமன்றக் குழு அமைக்கப்பட்டது.",
            "why_a_en": "G.B. Pant chaired this first Article 344(4) parliamentary committee.",
            "why_a_ta": "ஜி.பி. பந்த் இந்த முதலாவது சரத்து 344(4) நாடாளுமன்றக் குழுவிற்குத் தலைமை தாங்கினார்.",
            "why_b_en": "Lal Bahadur Shastri succeeded Pant later as Home Minister.",
            "why_b_ta": "லால் பகதூர் சாஸ்திரி பின்னர் பந்திற்குப் பிறகு உள்துறை அமைச்சரானார்.",
            "why_c_en": "Morarji Desai was Finance Minister.",
            "why_c_ta": "மொரார்ஜி தேசாய் நிதியமைச்சராக இருந்தார்.",
            "why_d_en": "Rajaji opposed Hindi imposition and formed Swatantra Party in 1959.",
            "why_d_ta": "ராஜாஜி இந்தி திணிப்பை எதிர்த்து 1959-ல் சுதந்திராக் கட்சியைத் தொடங்கினார்.",
            "tip_en": "Pant Committee submitted its report in 1958, leading to the Presidential Order of 1960.",
            "tip_ta": "பந்த் குழு 1958-ல் அறிக்கை சமர்ப்பித்தது, இது 1960-ன் குடியரசுத் தலைவர் உத்தரவுக்கு வழிவகுத்தது.",
            "fact_en": "Pant Committee recommended that Hindi should be developed as the Union language, but English should not be discarded prematurely.",
            "fact_ta": "இந்தியை ஒன்றிய மொழியாக வளர்க்க வேண்டும், ஆனால் ஆங்கிலத்தை அவசரமாக கைவிடக் கூடாது என்று பந்த் குழு பரிந்துரைத்தது."
        },
        # 39
        {
            "subtopic": "October 2024 Classical Languages Decision",
            "stem_en": "[TNPSC Current Affairs & Polity 2024]\nIn October 2024, the Union Cabinet chaired by Prime Minister Narendra Modi conferred Classical Language status upon five languages. Which of the following is the correct set?",
            "stem_ta": "[TNPSC நடப்பு நிகழ்வுகள் & அரசியல் 2024]\nஅக்டோபர் 2024-ல் பிரதமர் நரேந்திர மோடி தலைமையிலான மத்திய அமைச்சரவை ஐந்து மொழிகளுக்கு செம்மொழித் தகுதியை வழங்கியது. பின்வருவனவற்றில் சரியான தொகுதி எது?",
            "options": [
                ("Assamese, Bengali, Marathi, Pali, and Prakrit", "அஸ்ஸாமி, வங்காள மொழி, மராத்தி, பாலி மற்றும் பிராகிருதம்"),
                ("Bhojpuri, Rajasthani, Maithili, Tulu, and Pali", "போஜ்புரி, ராஜஸ்தானி, மைதிலி, துளு மற்றும் பாலி"),
                ("Sindhi, Konkani, Manipuri, Nepali, and Prakrit", "சிந்தி, கொங்கணி, மணிப்பூரி, நேபாளி மற்றும் பிராகிருதம்"),
                ("Dogri, Bodo, Santhali, Marathi, and Assamese", "டோக்ரி, போடோ, சந்தாலி, மராத்தி மற்றும் அஸ்ஸாமி")
            ],
            "correct_key": "A",
            "exp_en": "On 3 October 2024, the Union Cabinet approved Classical status for 5 languages: Assamese, Bengali, Marathi, Pali, and Prakrit, expanding the total count of Classical Languages to 11.",
            "exp_ta": "3 அக்டோபர் 2024 அன்று மத்திய அமைச்சரவை 5 மொழிகளுக்கு செம்மொழித் தகுதியை அங்கீகரித்தது: அஸ்ஸாமி, வங்காள மொழி, மராத்தி, பாலி மற்றும் பிராகிருதம்; இதனால் செம்மொழிகளின் மொத்த எண்ணிக்கை 11 ஆக உயர்ந்தது.",
            "why_a_en": "These five languages were conferred classical status on 3 October 2024.",
            "why_a_ta": "இவ்வைந்து மொழிகளுக்கும் 3 அக்டோபர் 2024 அன்று செம்மொழித் தகுதி வழங்கப்பட்டது.",
            "why_b_en": "Bhojpuri, Rajasthani, and Tulu do not have classical status.",
            "why_b_ta": "போஜ்புரி, ராஜஸ்தானி மற்றும் துளுவிற்கு செம்மொழித் தகுதி இல்லை.",
            "why_c_en": "Sindhi, Konkani, Manipuri, Nepali are 8th Schedule languages, not classical.",
            "why_c_ta": "சிந்தி, கொங்கணி, மணிப்பூரி, நேபாளி 8வது அட்டவணை மொழிகள், செம்மொழிகள் அல்ல.",
            "why_d_en": "Dogri, Bodo, Santhali are not classical languages.",
            "why_d_ta": "டோக்ரி, போடோ, சந்தாலி செம்மொழிகள் அல்ல.",
            "tip_en": "Total Classical Languages now: 6 + 5 = 11 languages!",
            "tip_ta": "தற்போதைய மொத்த செம்மொழிகள்: 6 + 5 = 11 மொழிகள்!",
            "fact_en": "Pali and Prakrit are classical languages associated with ancient Buddhist and Jain canons respectively.",
            "fact_ta": "பாலி மற்றும் பிராகிருதம் ஆகியவை முறையே பண்டைய பௌத்த மற்றும் சமண சமய நூல்களுடன் தொடர்புடைய செம்மொழிகளாகும்."
        },
        # 40
        {
            "subtopic": "Classical Languages Outside Eighth Schedule",
            "stem_en": "[TNPSC Current Affairs & Polity 2024]\nAmong the 11 languages currently recognized as Classical Languages in India, which two languages are NOT included in the Eighth Schedule of the Constitution of India?",
            "stem_ta": "[TNPSC நடப்பு நிகழ்வுகள் & அரசியல் 2024]\nஇந்தியாவில் தற்போது செம்மொழிகளாக அங்கீகரிக்கப்பட்டுள்ள 11 மொழிகளில், இந்திய அரசியலமைப்பின் எட்டாவது அட்டவணையில் சேர்க்கப்படாத இரண்டு மொழிகள் எவை?",
            "options": [
                ("Pali and Prakrit", "பாலி மற்றும் பிராகிருதம்"),
                ("Marathi and Assamese", "மராத்தி மற்றும் அஸ்ஸாமி"),
                ("Bengali and Odia", "வங்காள மொழி மற்றும் ஒடியா"),
                ("Sanskrit and Malayalam", "சமஸ்கிருதம் மற்றும் மலையாளம்")
            ],
            "correct_key": "A",
            "exp_en": "Pali and Prakrit were declared Classical Languages in October 2024, but neither of them is included in the Eighth Schedule of the Indian Constitution, making them unique among classical languages.",
            "exp_ta": "அக்டோபர் 2024-ல் பாலி மற்றும் பிராகிருதம் செம்மொழிகளாக அறிவிக்கப்பட்டன, ஆனால் இவ்விரண்டும் இந்திய அரசியலமைப்பின் எட்டாவது அட்டவணையில் சேர்க்கப்படவில்லை; இது செம்மொழிகளில் இவற்றை தனித்துவமாக்குகிறது.",
            "why_a_en": "Pali and Prakrit are Classical Languages but absent from Eighth Schedule.",
            "why_a_ta": "பாலி மற்றும் பிராகிருதம் செம்மொழிகள் ஆனால் எட்டாவது அட்டவணையில் இல்லை.",
            "why_b_en": "Both Marathi and Assamese are in the Eighth Schedule.",
            "why_b_ta": "மராத்தி மற்றும் அஸ்ஸாமி இரண்டும் எட்டாவது அட்டவணையில் உள்ளன.",
            "why_c_en": "Bengali and Odia are in the Eighth Schedule.",
            "why_c_ta": "வங்காள மொழி மற்றும் ஒடியா எட்டாவது அட்டவணையில் உள்ளன.",
            "why_d_en": "Sanskrit and Malayalam are in the Eighth Schedule.",
            "why_d_ta": "சமஸ்கிருதம் மற்றும் மலையாளம் எட்டாவது அட்டவணையில் உள்ளன.",
            "tip_en": "Crucial distinction: Eighth Schedule = 22 languages; Classical Languages = 11 languages (9 overlap, Pali & Prakrit do not).",
            "tip_ta": "முக்கிய வேறுபாடு: 8வது அட்டவணை = 22 மொழிகள்; செம்மொழிகள் = 11 மொழிகள் (9 மொழிகள் பொதுவானவை, பாலி & பிராகிருதம் அட்டவணையில் இல்லை).",
            "fact_en": "Classical status is an executive classification by the Ministry of Culture, distinct from Eighth Schedule constitutional listing.",
            "fact_ta": "செம்மொழித் தகுதி என்பது பண்பாட்டு அமைச்சகத்தின் நிர்வாக வகைப்பாடு, எட்டாவது அட்டவணை அரசியலமைப்புப் பட்டியலிலிருந்து வேறுபட்டது."
        },
        # 41
        {
            "subtopic": "Language Prohibition in Representations Article 350",
            "stem_en": "[TNPSC Group 2 2017]\nWhich Article of the Constitution ensures that an aggrieved citizen cannot have their representation rejected by any authority merely on the ground that it is submitted in their local regional language?",
            "stem_ta": "[TNPSC குரூப் 2 2017]\nபாதிக்கப்பட்ட குடிமகன் தனது உள்ளூர் வட்டார மொழியில் மனு அளித்ததற்காக மட்டுமே எந்தவொரு அதிகாரியாலும் அவரது மனு நிராகரிக்கப்பட முடியாது என்பதை உறுதி செய்யும் அரசியலமைப்புச் சரத்து எது?",
            "options": [
                ("Article 350", "சரத்து 350"),
                ("Article 349", "சரத்து 349"),
                ("Article 351", "சரத்து 351"),
                ("Article 344", "சரத்து 344")
            ],
            "correct_key": "A",
            "exp_en": "Article 350 guarantees the right of any person to submit a grievance petition in any language used in the Union or the State, safeguarding citizens from bureaucratic language discrimination.",
            "exp_ta": "சரத்து 350 எந்தவொரு நபரும் ஒன்றியம் அல்லது மாநிலத்தில் பயன்பாட்டிலுள்ள எந்த மொழியிலும் குறைதீர்ப்பு மனுவை சமர்ப்பிக்கும் உரிமையை உறுதி செய்கிறது, இது நிர்வாக மொழிப் பாகுபாட்டிலிருந்து குடிமக்களைப் பாதுகாக்கிறது.",
            "why_a_en": "Article 350 guarantees grievance submissions in any language in use.",
            "why_a_ta": "சரத்து 350 பயன்பாட்டிலுள்ள எந்த மொழியிலும் குறைதீர்ப்பு மனு அளிக்க உத்தரவாதம் அளிக்கிறது.",
            "why_b_en": "Article 349 covers special procedure for language laws during first 15 years.",
            "why_b_ta": "சரத்து 349 முதல் 15 ஆண்டுகளில் மொழிச் சட்டங்களுக்கான சிறப்பு நடைமுறையைக் கையாள்கிறது.",
            "why_c_en": "Article 351 is Hindi development directive.",
            "why_c_ta": "சரத்து 351 இந்தி மொழி வளர்ச்சிக்கான வழிகாட்டுதல்.",
            "why_d_en": "Article 344 covers Commission and Committee on official language.",
            "why_d_ta": "சரத்து 344 அதிகாரப்பூர்வ மொழிக்கான ஆணையம் மற்றும் குழுவைக் கையாள்கிறது.",
            "tip_en": "A fundamental administrative safeguard for linguistic diversity across India.",
            "tip_ta": "இந்தியா முழுவதிலும் உள்ள மொழிப் பன்முகத்தன்மைக்கான அடிப்படை நிர்வாகப் பாதுகாப்பு.",
            "fact_en": "Officers are prohibited from insisting on Hindi or English for public grievance petitions under Article 350.",
            "fact_ta": "சரத்து 350-ன் கீழ் பொதுக் குறைதீர்ப்பு மனுக்களுக்கு இந்தி அல்லது ஆங்கிலத்தை வற்புறுத்த அலுவலர்களுக்குத் தடை விதிக்கப்பட்டுள்ளது."
        },
        # 42
        {
            "subtopic": "Section 3(3) Bilingual Documents Mandate",
            "stem_en": "[TNPSC Group 1 2019]\nUnder Section 3(3) of the Official Languages Act 1963, both Hindi and English MUST be used for which of the following official documents issued by the Central Government?",
            "stem_ta": "[TNPSC குரூப் 1 2019]\nஅதிகாரப்பூர்வ மொழிகள் சட்டம் 1963-ன் பிரிவு 3(3)-ன் கீழ், மத்திய அரசால் வெளியிடப்படும் பின்வரும் எந்த அதிகாரப்பூர்வ ஆவணங்களுக்கு இந்தி மற்றும் ஆங்கிலம் ஆகிய இரு மொழிகளும் கட்டாயமாகப் பயன்படுத்தப்பட வேண்டும்?",
            "options": [
                ("Resolutions, general orders, rules, notifications, administrative reports, press communiques, contracts, agreements, licenses, and tenders", "தீர்மானங்கள், பொது ஆணைகள், விதிகள், அறிவிக்கைகள், நிர்வாக அறிக்கைகள், செய்திக் குறிப்புகள், ஒப்பந்தங்கள், உடன்படிக்கைகள், உரிமங்கள் மற்றும் ஒப்பந்தப் புள்ளிகள்"),
                ("Only internal notes and confidential memos exchanged within the Home Ministry", "உள்துறை அமைச்சகத்திற்குள் பரிமாறப்படும் உள் குறிப்புகள் மற்றும் ரகசியக் குறிப்புகள் மட்டுமே"),
                ("Only speeches delivered by the President during Republic Day", "குடியரசு தினத்தின் போது குடியரசுத் தலைவர் நிகழ்த்தும் உரைகள் மட்டுமே"),
                ("Only passports and visas issued to foreign nationals", "வெளிநாட்டு குடிமக்களுக்கு வழங்கப்படும் கடவுச்சீட்டுகள் மற்றும் விசாக்கள் மட்டுமே")
            ],
            "correct_key": "A",
            "exp_en": "Section 3(3) of the Official Languages Act 1963 specifies 14 categories of documents (resolutions, general orders, rules, notifications, administrative reports, press communiques, contracts, agreements, licenses, permits, notices, and tender forms) that must be issued in both Hindi and English simultaneously.",
            "exp_ta": "அதிகாரப்பூர்வ மொழிகள் சட்டம் 1963-ன் பிரிவு 3(3) ஒரே நேரத்தில் இந்தி மற்றும் ஆங்கிலம் ஆகிய இரு மொழிகளிலும் வெளியிடப்பட வேண்டிய 14 வகை ஆவணங்களைக் (தீர்மானங்கள், பொது ஆணைகள், விதிகள், அறிவிப்புகள், நிர்வாக அறிக்கைகள், ஒப்பந்தங்கள், உரிமங்கள், டெண்டர் படிவங்கள் போன்றவை) குறிப்பிடுகிறது.",
            "why_a_en": "Section 3(3) specifically lists these public-facing and legal documents.",
            "why_a_ta": "பிரிவு 3(3) இந்த பொது மற்றும் சட்ட ஆவணங்களை வெளிப்படையாகப் பட்டியலிடுகிறது.",
            "why_b_en": "Internal notes do not fall under the strict statutory bilingual rule of 3(3).",
            "why_b_ta": "உள் குறிப்புகள் பிரிவு 3(3)-ன் கடுமையான இருமொழி விதிக்குள் வராது.",
            "why_c_en": "Presidential speeches are not governed by Section 3(3).",
            "why_c_ta": "குடியரசுத் தலைவர் உரைகள் பிரிவு 3(3)-ஆல் நிர்வகிக்கப்படுவதில்லை.",
            "why_d_en": "Passports and visas are issued under Passport Act, not Section 3(3).",
            "why_d_ta": "கடவுச்சீட்டுகள் பாஸ்போர்ட் சட்டத்தின் கீழ் வழங்கப்படுகின்றன, பிரிவு 3(3) கீழ் அல்ல.",
            "tip_en": "Any general order or tender issued in only one language violates Section 3(3) of the 1963 Act.",
            "tip_ta": "ஒரே ஒரு மொழியில் மட்டும் வெளியிடப்படும் பொது ஆணை அல்லது டெண்டர் 1963 சட்டத்தின் பிரிவு 3(3)-ஐ மீறுவதாகும்.",
            "fact_en": "The signing officer is held personally responsible for ensuring both bilingual versions are released concurrently.",
            "fact_ta": "இருமொழிப் பதிப்புகளும் ஒரே நேரத்தில் வெளியிடப்படுவதை உறுதி செய்வதற்கு கையொப்பமிடும் அதிகாரியே தனிப்பட்ட முறையில் பொறுப்பாவார்."
        },
        # 43
        {
            "subtopic": "1968 TN Assembly Resolution on Eighth Schedule",
            "stem_en": "[TNPSC Group 1 2018]\nIn addition to adopting the Two-Language Policy, what constitutional demand regarding the Eighth Schedule languages was incorporated in the Tamil Nadu Assembly Resolution of January 1968?",
            "stem_ta": "[TNPSC குரூப் 1 2018]\nஇருமொழிக் கொள்கையை ஏற்றுக் கொண்டதுடன், ஜனவரி 1968-ன் தமிழ்நாடு சட்டமன்றத் தீர்மானத்தில் எட்டாவது அட்டவணை மொழிகள் குறித்து சேர்க்கப்பட்ட அரசியலமைப்பு ரீதியான கோரிக்கை எது?",
            "options": [
                ("All languages in the Eighth Schedule should be declared as official languages of the Union", "எட்டாவது அட்டவணையில் உள்ள அனைத்து மொழிகளும் ஒன்றியத்தின் அதிகாரப்பூர்வ மொழிகளாக அறிவிக்கப்பட வேண்டும்"),
                ("Only Tamil should replace Hindi as the national link language", "இந்திக்கு மாற்றாக தமிழ் மட்டுமே தேசிய இணைப்பு மொழியாக வேண்டும்"),
                ("The Eighth Schedule should be abolished entirely from the Constitution", "அரசியலமைப்பிலிருந்து எட்டாவது அட்டவணை முற்றிலும் நீக்கப்பட வேண்டும்"),
                ("English should be completely removed from the Indian subcontinent", "இந்தியத் துணைக் கண்டத்திலிருந்து ஆங்கிலம் முற்றிலும் அகற்றப்பட வேண்டும்")
            ],
            "correct_key": "A",
            "exp_en": "The landmark 1968 Tamil Nadu Assembly resolution moved by Chief Minister C.N. Annadurai demanded that all national languages included in the Eighth Schedule of the Constitution should ultimately be made the official languages of the Union.",
            "exp_ta": "முதலமைச்சர் சி.என். அண்ணாதுரை கொண்டுவந்த வரலாற்றுச் சிறப்புமிக்க 1968 தமிழ்நாடு சட்டமன்றத் தீர்மானம், அரசியலமைப்பின் எட்டாவது அட்டவணையில் உள்ள அனைத்து தேசிய மொழிகளும் இறுதியில் ஒன்றியத்தின் அதிகாரப்பூர்வ மொழிகளாக ஆக்கப்பட வேண்டும் என்று கோரியது.",
            "why_a_en": "Equal status for all Eighth Schedule languages was the core demand.",
            "why_a_ta": "எட்டாவது அட்டவணையின் அனைத்து மொழிகளுக்கும் சம அந்தஸ்து என்பதே முதன்மைக் கோரிக்கையாகும்.",
            "why_b_en": "The resolution did not seek exclusive status for Tamil at the Union level.",
            "why_b_ta": "ஒன்றிய அளவில் தமிழ்க்கு மட்டுமேயான பிரத்யேக அந்தஸ்தை இத்தீர்மானம் கோரவில்லை.",
            "why_c_en": "The resolution did not seek abolition of the Eighth Schedule.",
            "why_c_ta": "எட்டாவது அட்டவணையை நீக்குமாறு இத்தீர்மானம் கோரவில்லை.",
            "why_d_en": "The resolution firmly championed English as the link language.",
            "why_d_ta": "இத்தீர்மானம் ஆங்கிலத்தை இணைப்பு மொழியாக உறுதியாக ஆதரித்தது.",
            "tip_en": "Annadurai's doctrine: 'All regional languages are national languages; until all are official, English must remain the common medium.'",
            "tip_ta": "அண்ணாவின் கோட்பாடு: 'எல்லா வட்டார மொழிகளும் தேசிய மொழிகளே; அனைத்தும் அதிகாரப்பூர்வமாகும் வரை ஆங்கிலமே பொது ஊடகமாக நீடிக்க வேண்டும்.'",
            "fact_en": "This position remains the foundational language policy of all major political parties in Tamil Nadu.",
            "fact_ta": "இந்த நிலைப்பாடே தமிழ்நாட்டின் அனைத்து முக்கிய அரசியல் கட்சிகளின் அடித்தளமான மொழிக் கொள்கையாக இன்றும் நீடிக்கிறது."
        },
        # 44
        {
            "subtopic": "Special Officer for Linguistic Minorities Reporting",
            "stem_en": "[TNPSC Group 2 2016]\nUnder Article 350B(2), to whom does the Special Officer for Linguistic Minorities submit his reports, and who causes them to be laid before each House of Parliament?",
            "stem_ta": "[TNPSC குரூப் 2 2016]\nசரத்து 350B(2)-ன் கீழ் மொழிச் சிறுபான்மையினருக்கான சிறப்பு அலுவலர் தனது அறிக்கைகளை யாரிடம் சமர்ப்பிக்கிறார், மற்றும் அவற்றை நாடாளுமன்றத்தின் ஒவ்வொரு அவையின் முன்னும் வைக்கச் செய்பவர் யார்?",
            "options": [
                ("Submits to the President of India, who causes them to be laid before Parliament", "இந்தியக் குடியரசுத் தலைவரிடம் சமர்ப்பிக்கிறார், அவர் அவற்றை நாடாளுமன்றத்தில் வைக்கச் செய்கிறார்"),
                ("Submits directly to the Speaker of Lok Sabha", "மக்களவைத் தலைவரிடம் நேரடியாக சமர்ப்பிக்கிறார்"),
                ("Submits to the Prime Minister", "பிரதமரிடம் சமர்ப்பிக்கிறார்"),
                ("Submits to the National Commission for Minorities", "தேசிய சிறுபான்மையினர் ஆணையத்திடம் சமர்ப்பிக்கிறார்")
            ],
            "correct_key": "A",
            "exp_en": "Article 350B(2) provides: 'It shall be the duty of the Special Officer to investigate all matters relating to safeguards provided for linguistic minorities and report to the President... and the President shall cause all such reports to be laid before each House of Parliament, and sent to the Governments of the States concerned.'",
            "exp_ta": "சரத்து 350B(2) மொழிச் சிறுபான்மையினருக்கு வழங்கப்பட்டுள்ள பாதுகாப்புகள் தொடர்பான அனைத்து விவகாரங்களையும் விசாரித்து குடியரசுத் தலைவரிடம் அறிக்கை சமர்ப்பிப்பது சிறப்பு அலுவலரின் கடமையாகும் என்றும், குடியரசுத் தலைவர் அவ்வறிக்கைகளை நாடாளுமன்றத்தின் இரு அவைகளின் முன்னும் வைக்கச் செய்து சம்பந்தப்பட்ட மாநில அரசுகளுக்கும் அனுப்புவார் என்றும் கூறுகிறது.",
            "why_a_en": "Article 350B(2) specifies submission to President and tabling in Parliament.",
            "why_a_ta": "சரத்து 350B(2) குடியரசுத் தலைவரிடம் சமர்ப்பிப்பதையும் நாடாளுமன்றத்தில் சமர்ப்பிக்கப்படுவதையும் குறிப்பிடுகிறது.",
            "why_b_en": "Reports are not submitted directly to the Speaker.",
            "why_b_ta": "அறிக்கைகள் சபாநாயகரிடம் நேரடியாக சமர்ப்பிக்கப்படுவதில்லை.",
            "why_c_en": "Prime Minister is not the recipient under Article 350B.",
            "why_c_ta": "சரத்து 350B-ன் கீழ் அறிக்கையைப் பெறுபவர் பிரதமர் அல்ல.",
            "why_d_en": "NCM is a statutory body under a separate 1992 Act.",
            "why_d_ta": "தேசிய சிறுபான்மையினர் ஆணையம் 1992 தனிச் சட்டத்தின் கீழான சட்டப்பூர்வ அமைப்பாகும்.",
            "tip_en": "Key detail: Reports are also sent to the Governors/Governments of the States concerned.",
            "tip_ta": "முக்கிய விவரம்: அறிக்கைகள் சம்பந்தப்பட்ட மாநிலங்களின் ஆளுநர்களுக்கும்/அரசுகளுக்கும் அனுப்பப்படுகின்றன.",
            "fact_en": "The Commissioner for Linguistic Minorities submits annual reports on linguistic minority schools, teachers, and textbooks.",
            "fact_ta": "மொழிச் சிறுபான்மையினர் ஆணையர் மொழிச் சிறுபான்மையினர் பள்ளிகள், ஆசிரியர்கள் மற்றும் பாடப்புத்தகங்கள் குறித்து வருடாந்திர அறிக்கைகளை சமர்ப்பிக்கிறார்."
        },
        # 45
        {
            "subtopic": "National Language Judicial Clarification",
            "stem_en": "[TNPSC Polity & Legal Precedents]\nIn which landmark 2010 case did the Gujarat High Court explicitly clarify that Hindi is NOT the 'National Language' of India, as the Constitution confers no such status?",
            "stem_ta": "[TNPSC அரசியல் & சட்ட முன்னுதாரணங்கள்]\nஅரசியலமைப்பு அத்தகைய எந்தத் தகுதியையும் வழங்காததால் இந்தி இந்தியாவின் 'தேசிய மொழி' அல்ல என்று குஜராத் உயர் நீதிமன்றம் எந்த முக்கிய 2010 வழக்கில் வெளிப்படையாகத் தெளிவுபடுத்தியது?",
            "options": [
                ("Suresh Kachhadia v. Union of India (2010)", "சுரேஷ் கச்சாடியா எதிர் இந்திய ஒன்றியம் (2010)"),
                ("Kesavananda Bharati v. State of Kerala (1973)", "கேசவானந்த பாரதி எதிர் கேரள மாநிலம் (1973)"),
                ("S.R. Bommai v. Union of India (1994)", "எஸ்.ஆர். பொம்மை எதிர் இந்திய ஒன்றியம் (1994)"),
                ("Minerva Mills v. Union of India (1980)", "மினர்வா மில்ஸ் எதிர் இந்திய ஒன்றியம் (1980)")
            ],
            "correct_key": "A",
            "exp_en": "In Suresh Kachhadia v. Union of India (2010), the Gujarat High Court observed: 'There is nothing on record to show that any provision has been made or order issued declaring Hindi as a national language of the country. Article 343 clearly provides that the official language of the Union shall be Hindi in Devanagari script.'",
            "exp_ta": "சுரேஷ் கச்சாடியா எதிர் இந்திய ஒன்றியம் (2010) வழக்கில் குஜராத் உயர் நீதிமன்றம் குறிப்பிட்டது: 'இந்தியை நாட்டின் தேசிய மொழியாக அறிவிக்கும் எந்தவொரு விதியோ அல்லது உத்தரவோ பிறப்பிக்கப்பட்டதாக எந்தப் பதிவும் இல்லை. சரத்து 343 ஒன்றியத்தின் அதிகாரப்பூர்வ மொழி தேவநாகரி வரிவடிவ இந்தி என்றே கூறுகிறது.'",
            "why_a_en": "Suresh Kachhadia (2010) is the ruling confirming India has no National Language.",
            "why_a_ta": "சுரேஷ் கச்சாடியா (2010) இந்தியாவிற்கு தேசிய மொழி இல்லை என்பதை உறுதிப்படுத்திய தீர்ப்பாகும்.",
            "why_b_en": "Kesavananda Bharati established Basic Structure doctrine.",
            "why_b_ta": "கேசவானந்த பாரதி அடிப்படை கட்டமைப்பு கோட்பாட்டை நிறுவியது.",
            "why_c_en": "S.R. Bommai dealt with Article 356 and secularism.",
            "why_c_ta": "எஸ்.ஆர். பொம்மை சரத்து 356 மற்றும் மதச்சார்பின்மையைக் கையாண்டது.",
            "why_d_en": "Minerva Mills reinforced judicial review and balance of Part III & IV.",
            "why_d_ta": "மினர்வா மில்ஸ் நீதித்துறை மறுஆய்வு மற்றும் பகுதி III & IV சமநிலையை வலுப்படுத்தியது.",
            "tip_en": "Constitution uses the term 'Official Language' (அதிகாரப்பூர்வ மொழி), NEVER 'National Language' (தேசிய மொழி).",
            "tip_ta": "அரசியலமைப்பு 'அதிகாரப்பூர்வ மொழி' என்ற சொல்லையே பயன்படுத்துகிறது, ஒருபோதும் 'தேசிய மொழி' என்று குறிப்பிடவில்லை.",
            "fact_en": "The PIL sought mandatory printing of maximum retail prices and manufacturing details in Hindi on consumer goods.",
            "fact_ta": "நுகர்வோர் பொருட்களின் அதிகபட்ச சில்லறை விலை மற்றும் தயாரிப்பு விவரங்களை இந்தியில் அச்சிடுவதைக் கட்டாயமாக்கக் கோரி இப்பொதுநல வழக்கு தொடரப்பட்டது."
        },
        # 46
        {
            "subtopic": "1976 Rules Regional Classification",
            "stem_en": "[TNPSC Group 1 2018]\nUnder the Official Languages Rules, 1976, into how many regions are Indian States and Union Territories classified for official communication purposes?",
            "stem_ta": "[TNPSC குரூப் 1 2018]\nஅதிகாரப்பூர்வ மொழிகள் விதிகள் 1976-ன் கீழ், அதிகாரப்பூர்வ தகவல்தொடர்பு நோக்கங்களுக்காக இந்திய மாநிலங்களும் யூனியன் பிரதேசங்களும் எத்தனை பிராந்தியங்களாக வகைப்படுத்தப்பட்டுள்ளன?",
            "options": [
                ("3 regions (Region A, Region B, and Region C)", "3 பிராந்தியங்கள் (பிராந்தியம் A, பிராந்தியம் B, மற்றும் பிராந்தியம் C)"),
                ("4 regions (North, South, East, and West)", "4 பிராந்தியங்கள் (வடக்கு, தெற்கு, கிழக்கு மற்றும் மேற்கு)"),
                ("2 regions (Hindi speaking and Non-Hindi speaking)", "2 பிராந்தியங்கள் (இந்தி பேசும் மற்றும் இந்தி பேசாத)"),
                ("5 regions (Zonal Council regions)", "5 பிராந்தியங்கள் (மண்டலக் குழு பிராந்தியங்கள்)")
            ],
            "correct_key": "A",
            "exp_en": "Rule 2 of the Official Languages Rules, 1976 classifies India into three distinct regions: Region A (Hindi states), Region B (states with substantial Hindi usage like Punjab, Gujarat, Maharashtra), and Region C (non-Hindi states including all southern and northeastern states).",
            "exp_ta": "அதிகாரப்பூர்வ மொழிகள் விதிகள் 1976-ன் விதி 2 இந்தியாவை மூன்று தனித்துவமான பிராந்தியங்களாக வகைப்படுத்துகிறது: பிராந்தியம் A (இந்தி மாநிலங்கள்), பிராந்தியம் B (பஞ்சாப், குஜராத், மகாராஷ்டிரா போன்ற கணிசமான இந்தி புழக்கம் உள்ளவை), மற்றும் பிராந்தியம் C (அனைத்து தென் மற்றும் வடகிழக்கு மாநிலங்கள் உட்பட இந்தி பேசாதவை).",
            "why_a_en": "The Rules establish a three-tier classification: Regions A, B, and C.",
            "why_a_ta": "இவ்விதிகள் மூன்று அடுக்கு வகைப்பாட்டை நிறுவுகின்றன: பிராந்தியங்கள் A, B மற்றும் C.",
            "why_b_en": "Geographical quadrants are not used in the 1976 Rules.",
            "why_b_ta": "1976 விதிகளில் புவியியல் திசைப் பிரிவுகள் பயன்படுத்தப்படவில்லை.",
            "why_c_en": "It is not a binary division; Region B provides an intermediate category.",
            "why_c_ta": "இது இரட்டைப் பிரிவு அல்ல; பிராந்தியம் B இடைப்பட்ட வகையை வழங்குகிறது.",
            "why_d_en": "Zonal councils are established under the States Reorganisation Act 1956.",
            "why_d_ta": "மண்டலக் குழுக்கள் மாநில மறுசீரமைப்புச் சட்டம் 1956-ன் கீழ் அமைக்கப்பட்டவை.",
            "tip_en": "Region A: Communications in Hindi; Region B: Hindi with English; Region C: Exclusively in English.",
            "tip_ta": "பிராந்தியம் A: இந்தியில் தொடர்பு; பிராந்தியம் B: இந்தி மற்றும் ஆங்கிலம்; பிராந்தியம் C: ஆங்கிலத்தில் மட்டுமே தொடர்பு.",
            "fact_en": "Tamil Nadu stands completely outside this classification pursuant to Rule 1(2).",
            "fact_ta": "விதி 1(2)-ன் படி தமிழ்நாடு இந்த வகைப்பாட்டிற்கு முற்றிலும் வெளியே நிற்கிறது."
        },
        # 47
        {
            "subtopic": "Region C Classification Composition",
            "stem_en": "[TNPSC Group 2 2017]\nUnder the Official Languages Rules, 1976, which of the following groups of States falls under 'Region C'?",
            "stem_ta": "[TNPSC குரூப் 2 2017]\nஅதிகாரப்பூர்வ மொழிகள் விதிகள் 1976-ன் கீழ், பின்வரும் எந்த மாநிலங்களின் தொகுதி 'பிராந்தியம் C' (Region C)-ன் கீழ் வருகிறது?",
            "options": [
                ("Kerala, Karnataka, Andhra Pradesh, and West Bengal", "கேரளா, கர்நாடகா, ஆந்திரப் பிரதேசம் மற்றும் மேற்கு வங்காளம்"),
                ("Uttar Pradesh, Madhya Pradesh, and Bihar", "உத்தரப் பிரதேசம், மத்தியப் பிரதேசம் மற்றும் பீகார்"),
                ("Punjab, Gujarat, and Maharashtra", "பஞ்சாப், குஜராத் மற்றும் மகாராஷ்டிரா"),
                ("Haryana, Rajasthan, and Himachal Pradesh", "ஹரியானா, ராஜஸ்தான் மற்றும் இமாச்சலப் பிரதேசம்")
            ],
            "correct_key": "A",
            "exp_en": "Region C comprises all States and Union Territories not included in Region A or Region B. Southern States like Kerala, Karnataka, Andhra Pradesh, Telangana, and eastern states like West Bengal and Odisha belong to Region C.",
            "exp_ta": "பிராந்தியம் C என்பது பிராந்தியம் A அல்லது B-ல் சேர்க்கப்படாத அனைத்து மாநிலங்களையும் யூனியன் பிரதேசங்களையும் உள்ளடக்கியது. தென்னிந்திய மாநிலங்களான கேரளா, கர்நாடகா, ஆந்திரா, தெலுங்கானா மற்றும் மேற்கு வங்காளம், ஒடிசா ஆகியவை பிராந்தியம் C-ல் வருகின்றன.",
            "why_a_en": "Southern and eastern non-Hindi states comprise Region C.",
            "why_a_ta": "தெற்கு மற்றும் கிழக்கு இந்தி பேசாத மாநிலங்கள் பிராந்தியம் C-ஐ உள்ளடக்கியுள்ளன.",
            "why_b_en": "UP, MP, Bihar belong to Region A (Hindi states).",
            "why_b_ta": "உ.பி, ம.பி, பீகார் ஆகியவை பிராந்தியம் A-வைச் சேர்ந்தவை.",
            "why_c_en": "Punjab, Gujarat, Maharashtra belong to Region B.",
            "why_c_ta": "பஞ்சாப், குஜராத், மகாராஷ்டிரா ஆகியவை பிராந்தியம் B-ஐச் சேர்ந்தவை.",
            "why_d_en": "Haryana, Rajasthan, Himachal Pradesh belong to Region A.",
            "why_d_ta": "ஹரியானா, ராஜஸ்தான், இமாச்சலப் பிரதேசம் ஆகியவை பிராந்தியம் A-வைச் சேர்ந்தவை.",
            "tip_en": "Communications sent from Central Government offices to Region C states must be in English.",
            "tip_ta": "மத்திய அரசு அலுவலகங்களிலிருந்து பிராந்தியம் C மாநிலங்களுக்கு அனுப்பப்படும் கடிதப் போக்குவரத்துகள் ஆங்கிலத்திலேயே இருக்க வேண்டும்.",
            "fact_en": "If any communication is sent to Region C in Hindi, an English translation must accompany it.",
            "fact_ta": "பிராந்தியம் C-க்கு இந்தியில் ஏதேனும் கடிதம் அனுப்பப்பட்டால், அதனுடன் ஆங்கில மொழிபெயர்ப்பு கட்டாயம் இணைக்கப்பட வேண்டும்."
        },
        # 48
        {
            "subtopic": "Article 344 Commission Constitution Interval",
            "stem_en": "[TNPSC Group 1 2019]\nAccording to Article 344(1) of the Constitution of India, at what time intervals was the President required to constitute a Commission on Official Language?",
            "stem_ta": "[TNPSC குரூப் 1 2019]\nஇந்திய அரசியலமைப்பின் சரத்து 344(1)-ன் படி, அதிகாரப்பூர்வ மொழிக்கான ஆணையத்தைக் குடியரசுத் தலைவர் எந்த கால இடைவெளியில் அமைக்க வேண்டும் என்று விதிக்கப்பட்டிருந்தது?",
            "options": [
                ("At the expiration of 5 years and 10 years from the commencement of the Constitution", "அரசியலமைப்பு அமலுக்கு வந்த 5 ஆண்டுகள் மற்றும் 10 ஆண்டுகள் முடிவில்"),
                ("Every 5 years indefinitely", "தொடர்ந்து ஒவ்வொரு 5 ஆண்டுகளுக்கும் ஒருமுறை"),
                ("Only once after 15 years", "15 ஆண்டுகளுக்குப் பிறகு ஒருமுறை மட்டுமே"),
                ("Every 10 years along with the decennial census", "பத்தாண்டு மக்கள் தொகைக் கணக்கெடுப்புடன் இணைந்து ஒவ்வொரு 10 ஆண்டுகளுக்கும்")
            ],
            "correct_key": "A",
            "exp_en": "Article 344(1) provided: 'The President shall, at the expiration of five years from the commencement of this Constitution and thereafter at the expiration of ten years from such commencement, by order constitute a Commission...'",
            "exp_ta": "சரத்து 344(1) குறிப்பிட்டது: 'குடியரசுத் தலைவர் இந்த அரசியலமைப்பு தொடங்கியதிலிருந்து ஐந்து ஆண்டுகள் முடிவிலும், அதன் பின்னர் அத்தகைய தொடக்கத்திலிருந்து பத்து ஆண்டுகள் முடிவிலும், ஆணையம் ஒன்றை உத்தரவின் மூலம் அமைக்க வேண்டும்...'",
            "why_a_en": "Article 344(1) explicitly provided for commissions at the 5-year and 10-year marks.",
            "why_a_ta": "சரத்து 344(1) 5 மற்றும் 10 ஆண்டுகள் முடிவில் ஆணையங்களை அமைக்க வெளிப்படையாக விதித்தது.",
            "why_b_en": "The Constitution did not mandate recurring 5-year commissions indefinitely.",
            "why_b_ta": "அரசியலமைப்பு தொடர்ச்சியான 5 ஆண்டு ஆணையங்களை காலவரையின்றி கட்டாயப்படுத்தவில்லை.",
            "why_c_en": "15 years was the transition period under Article 343(2), not Commission interval.",
            "why_c_ta": "15 ஆண்டுகள் சரத்து 343(2) இடைக்காலக் கெடுவாகும், ஆணைய இடைவெளி அல்ல.",
            "why_d_en": "It was not linked to the census.",
            "why_d_ta": "இது மக்கள் தொகைக் கணக்கெடுப்புடன் இணைக்கப்படவில்லை.",
            "tip_en": "First Commission was constituted in 1955 (Kher Commission); the 10-year commission was effectively replaced by the 1963 Parliamentary setup.",
            "tip_ta": "முதல் ஆணையம் 1955-ல் அமைக்கப்பட்டது (கேர் ஆணையம்); 10வது ஆண்டு ஆணையத்திற்குப் பதிலாக 1963 நாடாளுமன்ற நடைமுறை மாற்றீடாக வந்தது.",
            "fact_en": "The duty of the Commission was to recommend progressive use of Hindi and restrictions on English.",
            "fact_ta": "இந்தியின் பயன்பாட்டைப் படிப்படியாக அதிகரிப்பதற்கும் ஆங்கிலத்தின் மீதான கட்டுப்பாடுகளுக்கும் பரிந்துரைப்பதே ஆணையத்தின் பணியாகும்."
        },
        # 49
        {
            "subtopic": "Article 349 Special Procedure for Language Bills",
            "stem_en": "[TNPSC Group 1 2017]\nUnder Article 349, during the first 15 years from the commencement of the Constitution, what special requirement was mandatory before introducing any Bill in Parliament proposing language changes?",
            "stem_ta": "[TNPSC குரூப் 1 2017]\nசரத்து 349-ன் கீழ், அரசியலமைப்பு அமலுக்கு வந்த முதல் 15 ஆண்டுகளில், மொழி மாற்றங்களை முன்மொழியும் எந்தவொரு மசோதாவையும் நாடாளுமன்றத்தில் அறிமுகப்படுத்துவதற்கு முன் எந்த சிறப்புத் தேவை கட்டாயமானது?",
            "options": [
                ("Previous sanction of the President, who must first consider the recommendations of the Commission and the Committee under Article 344", "குடியரசுத் தலைவரின் முன் அனுமதி; அவர் முதலில் சரத்து 344-ன் கீழான ஆணையம் மற்றும் குழுவின் பரிந்துரைகளைக் கருத்தில் கொள்ள வேண்டும்"),
                ("Approval of two-thirds of all State Legislatures", "அனைத்து மாநில சட்டமன்றங்களில் மூன்றில் இரண்டு பங்கினரின் ஒப்புதல்"),
                ("Mandatory national referendum across all states", "அனைத்து மாநிலங்களிலும் கட்டாய தேசிய மக்கள் வாக்கெடுப்பு"),
                ("Unanimous consent of the Supreme Court collegium", "உச்ச நீதிமன்றக் கொலீஜியத்தின் ஒருமனதான ஒப்புதல்")
            ],
            "correct_key": "A",
            "exp_en": "Article 349 laid down that during the 15-year period, no Bill or amendment proposing to alter language provisions under Article 348(1) could be introduced in Parliament without the previous sanction of the President, who could not grant sanction without considering Kher Commission and Pant Committee reports.",
            "exp_ta": "சரத்து 349 முதல் 15 ஆண்டு காலத்தில், சரத்து 348(1)-ன் கீழ் உள்ள மொழி விதிகளை மாற்றியமைக்கும் எந்தவொரு மசோதாவையும் குடியரசுத் தலைவரின் முன் அனுமதியின்றி நாடாளுமன்றத்தில் அறிமுகப்படுத்த முடியாது என்றும், கேர் ஆணையம் மற்றும் பந்த் குழு அறிக்கைகளைக் கருத்தில் கொள்ளாமல் குடியரசுத் தலைவர் அனுமதி அளிக்க முடியாது என்றும் விதித்தது.",
            "why_a_en": "Article 349 mandated Presidential previous sanction conditioned on Article 344 reports.",
            "why_a_ta": "சரத்து 349 சரத்து 344 அறிக்கைகளின் அடிப்படையிலான குடியரசுத் தலைவரின் முன் அனுமதியைக் கட்டாயமாக்கியது.",
            "why_b_en": "State legislature ratification was not required under Article 349.",
            "why_b_ta": "சரத்து 349-ன் கீழ் மாநில சட்டமன்றங்களின் ஒப்புதல் தேவைப்படவில்லை.",
            "why_c_en": "No referendum is provided in the Indian Constitution.",
            "why_c_ta": "இந்திய அரசியலமைப்பில் மக்கள் வாக்கெடுப்பு முறை இல்லை.",
            "why_d_en": "Judiciary has no pre-legislative sanction power.",
            "why_d_ta": "சட்டமன்றத்திற்கு முந்தைய அனுமதி அதிகாரம் நீதித்துறைக்கு இல்லை.",
            "tip_en": "Article 349 acted as a procedural brake to prevent rash language legislation during the initial 15-year period.",
            "tip_ta": "சரத்து 349 தொடக்க 15 ஆண்டு காலத்தில் அவசர மொழிச் சட்டங்கள் இயற்றப்படுவதைத் தடுக்கும் ஒரு பாதுகாப்புத் தடையாகச் செயல்பட்டது.",
            "fact_en": "This Article became effectively redundant after the initial 15-year period expired on 25 January 1965.",
            "fact_ta": "25 ஜனவரி 1965-ல் தொடக்க 15 ஆண்டு காலம் முடிந்த பிறகு இச்சரத்து நடைமுறையில் காலாவதியானது."
        },
        # 50
        {
            "subtopic": "Classical Language Antiquity Criteria",
            "stem_en": "[TNPSC Group 1 2022]\nAccording to the revised criteria established by the Government of India for according Classical status to a language, what is the required antiquity of its early texts or recorded history?",
            "stem_ta": "[TNPSC குரூப் 1 2022]\nஒரு மொழிக்கு செம்மொழித் தகுதி வழங்குவதற்காக இந்திய அரசால் நிர்ணயிக்கப்பட்ட திருத்தப்பட்ட அளவுகோல்களின்படி, அதன் தொடக்ககால நூல்கள் அல்லது பதிவு செய்யப்பட்ட வரலாற்றின் தேவையான பழமை எவ்வளவு?",
            "options": [
                ("High antiquity of its early texts/recorded history over a period of 1500 to 2000 years", "1500 முதல் 2000 ஆண்டுகள் வரையிலான காலப்பகுதியைச் சேர்ந்த தொடக்ககால நூல்கள்/பதிவு செய்யப்பட்ட வரலாற்றின் உயர்ந்த தொன்மை"),
                ("At least 500 to 800 years of documented literature", "குறைந்தது 500 முதல் 800 ஆண்டுகள் வரையிலான ஆவணப்படுத்தப்பட்ட இலக்கியம்"),
                ("Origin tracing back to the Indus Valley Civilization", "சிந்து சமவெளி நாகரிகத்திற்கு முந்தைய தோற்றம்"),
                ("Antiquity of 5000 years with deciphered epigraphy", "படிக்கப்பட்ட கல்வெட்டுகளுடன் கூடிய 5000 ஆண்டு கால தொன்மை")
            ],
            "correct_key": "A",
            "exp_en": "The criteria for declaration as a Classical Language mandate: (1) High antiquity of its early texts/recorded history over a period of 1500–2000 years; (2) A body of ancient literature considered a valuable heritage; (3) An original literary tradition not borrowed from another speech community; and (4) The classical language and literature being distinct from modern.",
            "exp_ta": "செம்மொழியாக அறிவிப்பதற்கான அளவுகோல்கள்: (1) 1500–2000 ஆண்டுகள் பழமையான ஆரம்பகால நூல்கள்/பதிவு செய்யப்பட்ட வரலாற்றின் உயர்ந்த தொன்மை; (2) மதிப்புமிக்க பாரம்பரியமாகக் கருதப்படும் பண்டைய இலக்கியங்கள்; (3) பிற மொழிக் குழுவிடமிருந்து கடன் பெறாத தனித்தன்மை வாய்ந்த இலக்கிய மரபு; (4) செம்மொழி மற்றும் அதன் இலக்கியம் நவீன மொழியிலிருந்து வேறுபட்டிருத்தல்.",
            "why_a_en": "1500–2000 years of high antiquity is the explicit official criterion.",
            "why_a_ta": "1500–2000 ஆண்டுகள் உயர்ந்த தொன்மை என்பது அதிகாரப்பூர்வ அளவுகோலாகும்.",
            "why_b_en": "500–800 years is too recent for classical classification.",
            "why_b_ta": "500–800 ஆண்டுகள் செம்மொழி வகைப்பாட்டிற்கு போதுமானதல்ல.",
            "why_c_en": "Indus Valley script is undeciphered and not an official criterion.",
            "why_c_ta": "சிந்து சமவெளி வரிவடிவம் இன்னும் படிக்கப்படவில்லை மற்றும் அதிகாரப்பூர்வ அளவுகோல் அல்ல.",
            "why_d_en": "5000 years is not the threshold requirement.",
            "why_d_ta": "5000 ஆண்டுகள் என்பது வரம்புத் தேவை அல்ல.",
            "tip_en": "Remember the 4 criteria: (1) 1500-2000 yrs antiquity, (2) Ancient heritage literature, (3) Original literary tradition, (4) Distinction between classical and modern forms.",
            "tip_ta": "4 அளவுகோல்களை நினைவில் கொள்க: (1) 1500-2000 ஆண்டுகள் தொன்மை, (2) பாரம்பரிய இலக்கியம், (3) சுயாதீன மரபு, (4) செவ்வியல் மற்றும் நவீன வடிவங்களுக்கு இடையிலான வேறுபாடு.",
            "fact_en": "Revised criteria were finalized by the Linguistic Experts Committee under Sahitya Akademi in 2005.",
            "fact_ta": "திருத்தப்பட்ட அளவுகோல்கள் 2005-ல் சாகித்ய அகாடமியின் கீழ் உள்ள மொழி நிபுணர்கள் குழுவால் இறுதி செய்யப்பட்டன."
        }
    ]

    questions = []
    for idx, item in enumerate(raw_data, start=1):
        qid = f"OL_PYQ_{idx:03d}"
        opts = item["options"]
        correct_key = item["correct_key"]
        
        q = make_ol_q(
            qid=qid,
            diff="Easy" if idx <= 15 else ("Medium" if idx <= 35 else "Hard"),
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
            tags=["polity", "official_language", "pyq", item["subtopic"].lower().replace(" ", "_")]
        )
        questions.append(q)
    return questions

def build_pyq_file():
    qs = get_pyq_questions()
    print(f"Generated {len(qs)} raw PYQ questions for Official Language.")
    balanced = randomize_and_balance_dataset(qs, seed=49)
    
    out_dir = os.path.join("data", "questions", "polity")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "official_language_pyq.json")
    alias_path = os.path.join(out_dir, "official_language_pyq_practice.json")
    
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(balanced, f, ensure_ascii=False, indent=2)
    with open(alias_path, "w", encoding="utf-8") as f:
        json.dump(balanced, f, ensure_ascii=False, indent=2)
    print(f"Saved balanced PYQ MCQs to {out_path} and alias {alias_path}")
    
    rep = ContentValidator.validate_file(out_path, expected_count=50, expected_prefix="OL_PYQ_")
    print(f"Validation: {'PASS' if rep.is_valid else 'FAIL'} | Total: {rep.total_audited}")
    print(f"Keys: {rep.key_distribution}")
    if not rep.is_valid:
        for iss in rep.issues:
            print("  Issue:", iss.severity, iss.field_name, iss.message)
    return rep.is_valid

if __name__ == "__main__":
    build_pyq_file()
