# -*- coding: utf-8 -*-
"""
Co-operative Societies - Part 2A: PYQ MCQs (50 Questions: CS_PYQ_001 to CS_PYQ_050)
TNPSC Nova AI Content Engine
"""
import os
import json
from collections import Counter
from tools.nova_content_engine.answer_randomizer import randomize_and_balance_dataset
from tools.nova_content_engine.validator import ContentValidator
from cooperative_societies_mcq_helper import make_coop_q


def get_pyq_raw_questions():
    return [
        # 1. TNPSC Group 1 2019
        {
            "subtopic": "97th Constitutional Amendment Act 2011",
            "stem_en": "[TNPSC Group 1 2019] Which Constitutional Amendment Act accorded constitutional status and protection to co-operative societies in India?",
            "stem_ta": "[TNPSC குரூப் 1 2019] இந்தியாவில் கூட்டுறவு சங்கங்களுக்கு அரசியலமைப்பு அந்தஸ்து மற்றும் பாதுகாப்பை வழங்கிய அரசியலமைப்பு திருத்தச் சட்டம் எது?",
            "options": [
                ("97th Constitutional Amendment Act, 2011", "97-வது அரசியலமைப்பு திருத்தச் சட்டம், 2011"),
                ("73rd Constitutional Amendment Act, 1992", "73-வது அரசியலமைப்பு திருத்தச் சட்டம், 1992"),
                ("74th Constitutional Amendment Act, 1992", "74-வது அரசியலமைப்பு திருத்தச் சட்டம், 1992"),
                ("91st Constitutional Amendment Act, 2003", "91-வது அரசியலமைப்பு திருத்தச் சட்டம், 2003")
            ],
            "correct_key": "A",
            "exp_en": "The 97th Constitutional Amendment Act, 2011 accorded constitutional status to cooperative societies by amending Article 19(1)(c), inserting Article 43B, and adding Part IX-B (Articles 243ZH to 243ZT).",
            "exp_ta": "2011-ஆம் ஆண்டின் 97-வது அரசியலமைப்பு திருத்தச் சட்டம் சரத்து 19(1)(c)-ஐத் திருத்தி, சரத்து 43B மற்றும் பகுதி IX-B-ஐச் சேர்த்து கூட்டுறவு சங்கங்களுக்கு அரசியலமைப்பு அந்தஸ்தை வழங்கியது.",
            "why_a_en": "Correct. 97th CAA 2011 added Part IX-B to the Constitution.",
            "why_a_ta": "சரி. 97வது திருத்தச் சட்டம் 2011 பகுதி IX-B-ஐச் சேர்த்தது.",
            "why_b_en": "Incorrect. 73rd CAA 1992 deals with Panchayati Raj (Part IX).",
            "why_b_ta": "தவறு. 73வது திருத்தம் பஞ்சாயத்து ராஜ் பற்றியது (பகுதி IX).",
            "why_c_en": "Incorrect. 74th CAA 1992 deals with Municipalities (Part IX-A).",
            "why_c_ta": "தவறு. 74வது திருத்தம் நகராட்சிகள் பற்றியது (பகுதி IX-A).",
            "why_d_en": "Incorrect. 91st CAA 2003 deals with limiting the size of the Council of Ministers to 15%.",
            "why_d_ta": "தவறு. 91வது திருத்தம் அமைச்சரவை அளவை 15% என வரம்பிட்டது.",
            "tip_en": "Remember the local democracy trio: 73rd = Panchayats; 74th = Municipalities; 97th = Cooperatives.",
            "tip_ta": "மறக்காதீர்கள்: 73வது = பஞ்சாயத்துகள்; 74வது = நகராட்சிகள்; 97வது = கூட்டுறவு சங்கங்கள்.",
            "fact_en": "The 97th CAA took effect on 15 February 2012.",
            "fact_ta": "97வது திருத்தச் சட்டம் 2012 பிப்ரவரி 15 முதல் நடைமுறைக்கு வந்தது."
        },

        # 2. TNPSC Group 2 2018
        {
            "subtopic": "Directive Principles - Article 43B",
            "stem_en": "[TNPSC Group 2 2018] Under which Article of the Indian Constitution is the State directed to promote voluntary formation, autonomous functioning, democratic control and professional management of co-operative societies?",
            "stem_ta": "[TNPSC குரூப் 2 2018] இந்திய அரசியலமைப்பின் எந்த உறுப்பின் கீழ் கூட்டுறவு சங்கங்களின் தன்னார்வ உருவாக்கம், தன்னாட்சி செயல்பாடு, ஜனநாயகக் கட்டுப்பாடு மற்றும் தொழில்முறை மேலாண்மையை ஊக்குவிக்க அரசுக்கு வழிகாட்டப்பட்டுள்ளது?",
            "options": [
                ("Article 43B", "உறுப்பு 43B"),
                ("Article 43A", "உறுப்பு 43A"),
                ("Article 43", "உறுப்பு 43"),
                ("Article 48A", "உறுப்பு 48A")
            ],
            "correct_key": "A",
            "exp_en": "Article 43B was inserted into Part IV (Directive Principles of State Policy) by the 97th Constitutional Amendment Act, 2011.",
            "exp_ta": "2011-ஆம் ஆண்டின் 97-வது அரசியலமைப்பு திருத்தச் சட்டத்தின் மூலம் பகுதி IV-ல் (அரசு வழிகாட்டு நெறிமுறைகள்) உறுப்பு 43B சேர்க்கப்பட்டது.",
            "why_a_en": "Correct. Article 43B directly directs the State to promote cooperative societies.",
            "why_a_ta": "சரி. உறுப்பு 43B கூட்டுறவு சங்கங்களை ஊக்குவிக்க அரசுக்கு வழிகாட்டுகிறது.",
            "why_b_en": "Incorrect. Article 43A deals with workers' participation in the management of industries (42nd CAA).",
            "why_b_ta": "தவறு. உறுப்பு 43A தொழில்துறை மேலாண்மையில் தொழிலாளர் பங்களிப்பைக் குறிக்கிறது (42வது திருத்தம்).",
            "why_c_en": "Incorrect. Article 43 deals with living wage and promotion of cottage industries.",
            "why_c_ta": "தவறு. உறுப்பு 43 வாழ்வாதார ஊதியம் மற்றும் குடிசைத் தொழில்களைக் குறிக்கிறது.",
            "why_d_en": "Incorrect. Article 48A deals with protection and improvement of environment and forests.",
            "why_d_ta": "தவறு. உறுப்பு 48A சுற்றுச்சூழல் மற்றும் வனப் பாதுகாப்பு பற்றியது.",
            "tip_en": "Article 43 = Cottage industries; Article 43A = Workers' participation; Article 43B = Co-operative societies.",
            "tip_ta": "உறுப்பு 43 = குடிசைத் தொழில்கள்; உறுப்பு 43A = தொழிலாளர் பங்களிப்பு; உறுப்பு 43B = கூட்டுறவு சங்கங்கள்.",
            "fact_en": "Article 43B was upheld as valid by the Supreme Court in 2021.",
            "fact_ta": "2021-ல் உச்சநீதிமன்றம் உறுப்பு 43B செல்லும் என்று உறுதிப்படுத்தியது."
        },

        # 3. TNPSC Assistant Director of Cooperative Societies 2022
        {
            "subtopic": "Fundamental Rights - Article 19(1)(c)",
            "stem_en": "[TNPSC AD of Cooperatives 2022] The words 'or co-operative societies' were added to which fundamental right under Article 19 of the Constitution?",
            "stem_ta": "[TNPSC கூட்டுறவு உதவி இயக்குநர் 2022] அரசியலமைப்பு உறுப்பு 19-ன் கீழ் எந்த அடிப்படை உரிமையில் 'அல்லது கூட்டுறவு சங்கங்கள்' என்ற சொற்கள் சேர்க்கப்பட்டன?",
            "options": [
                ("Article 19(1)(c)", "உறுப்பு 19(1)(c)"),
                ("Article 19(1)(a)", "உறுப்பு 19(1)(a)"),
                ("Article 19(1)(b)", "உறுப்பு 19(1)(b)"),
                ("Article 19(1)(d)", "உறுப்பு 19(1)(d)")
            ],
            "correct_key": "A",
            "exp_en": "Section 2 of the 97th Constitutional Amendment Act, 2011 amended Article 19(1)(c) to read: 'to form associations or unions or co-operative societies'.",
            "exp_ta": "97-வது திருத்தச் சட்டத்தின் பிரிவு 2, உறுப்பு 19(1)(c)-ல் 'சங்கங்கள் அல்லது தொழிற்சங்கங்கள் அல்லது கூட்டுறவு சங்கங்களை அமைக்கும் உரிமை' எனத் திருத்தியது.",
            "why_a_en": "Correct. Article 19(1)(c) guarantees freedom of association including cooperative societies.",
            "why_a_ta": "சரி. உறுப்பு 19(1)(c) கூட்டுறவு சங்கங்கள் அமைக்கும் உரிமையை அடிப்படை உரிமையாக்குகிறது.",
            "why_b_en": "Incorrect. Article 19(1)(a) protects freedom of speech and expression.",
            "why_b_ta": "தவறு. உறுப்பு 19(1)(a) பேச்சு மற்றும் கருத்துச் சுதந்திரத்தைக் குறிக்கிறது.",
            "why_c_en": "Incorrect. Article 19(1)(b) protects freedom of peaceful assembly without arms.",
            "why_c_ta": "தவறு. உறுப்பு 19(1)(b) ஆயுதமின்றி அமைதியாகக் கூடும் உரிமையைக் குறிக்கிறது.",
            "why_d_en": "Incorrect. Article 19(1)(d) protects freedom of movement throughout India.",
            "why_d_ta": "தவறு. உறுப்பு 19(1)(d) இந்தியா முழுவதும் சுதந்திரமாக நடமாடும் உரிமையைக் குறிக்கிறது.",
            "tip_en": "Article 19(1)(c) = Associations, Unions, Co-operative Societies.",
            "tip_ta": "உறுப்பு 19(1)(c) = சங்கங்கள், தொழிற்சங்கங்கள், கூட்டுறவு சங்கங்கள்.",
            "fact_en": "The right to form cooperative societies is subject to reasonable restrictions under Article 19(4).",
            "fact_ta": "கூட்டுறவு அமைக்கும் உரிமை உறுப்பு 19(4)-ன் கீழ் நியாயமான கட்டுப்பாடுகளுக்கு உட்பட்டது."
        },

        # 4. UPSC CSE Prelims 2021
        {
            "subtopic": "Seventh Schedule Distribution",
            "stem_en": "[UPSC CSE 2021] Under which List of the Seventh Schedule to the Constitution of India does the subject 'Co-operative Societies' operating within a State fall?",
            "stem_ta": "[UPSC CSE 2021] இந்திய அரசியலமைப்பின் ஏழாவது அட்டவணையின் எந்தப் பட்டியலின் கீழ் ஒரு மாநிலத்திற்குள் செயல்படும் 'கூட்டுறவு சங்கங்கள்' என்ற துறை வருகிறது?",
            "options": [
                ("List II (State List), Entry 32", "பட்டியல் II (மாநிலப் பட்டியல்), பதிவு 32"),
                ("List I (Union List), Entry 44", "பட்டியல் I (மத்திய பட்டியல்), பதிவு 44"),
                ("List III (Concurrent List), Entry 33", "பட்டியல் III (பொதுப் பட்டியல்), பதிவு 33"),
                ("List II (State List), Entry 5", "பட்டியல் II (மாநிலப் பட்டியல்), பதிவு 5")
            ],
            "correct_key": "A",
            "exp_en": "Under the Seventh Schedule, Entry 32 of List II (State List) exclusively covers 'co-operative societies'. Multi-state co-operatives fall under Entry 44 of List I (Union List).",
            "exp_ta": "ஏழாவது அட்டவணையின் கீழ், பட்டியல் II-ன் (மாநிலப் பட்டியல்) பதிவு 32 பிரத்யேகமாக 'கூட்டுறவு சங்கங்களை' உள்ளடக்கியுள்ளது. பல மாநில கூட்டுறவுகள் பட்டியல் I-ன் பதிவு 44-ன் கீழ் வருகின்றன.",
            "why_a_en": "Correct. Entry 32 of List II gives States exclusive legislative competence over cooperatives within their territory.",
            "why_a_ta": "சரி. பட்டியல் II பதிவு 32 மாநிலங்களுக்கு கூட்டுறவு சங்கங்கள் மீது முழு சட்டமியற்றும் அதிகாரத்தை வழங்குகிறது.",
            "why_b_en": "Incorrect. Entry 44 of List I covers corporations/cooperatives with objects not confined to one State.",
            "why_b_ta": "தவறு. பட்டியல் I பதிவு 44 ஒன்றுக்கு மேற்பட்ட மாநிலங்களில் செயல்படும் அமைப்புகளைக் குறிக்கிறது.",
            "why_c_en": "Incorrect. Entry 33 of List III deals with trade and commerce in essential foodstuffs/industrial products.",
            "why_c_ta": "தவறு. பட்டியல் III பதிவு 33 அத்தியாவசிய உணவு/தொழில் விளைபொருட்கள் வர்த்தகம் பற்றியது.",
            "why_d_en": "Incorrect. Entry 5 of List II covers local government (Panchayats and Municipalities).",
            "why_d_ta": "தவறு. பட்டியல் II பதிவு 5 உள்ளாட்சி அமைப்புகளைக் குறிக்கிறது.",
            "tip_en": "State Co-operatives = List II Entry 32; Multi-State Co-operatives = List I Entry 44.",
            "tip_ta": "மாநிலக் கூட்டுறவு = பட்டியல் II பதிவு 32; பல மாநிலக் கூட்டுறவு = பட்டியல் I பதிவு 44.",
            "fact_en": "Because Entry 32 of List II was affected without state ratification, Part IX-B was struck down for state cooperatives in 2021.",
            "fact_ta": "மாநிலப் பட்டியல் பதிவு 32 பாதிக்கப்பட்டதால் 2021-ல் பகுதி IX-B மாநிலக் கூட்டுறவுகளுக்கு செல்லாது என ரத்து செய்யப்பட்டது."
        },

        # 5. TNPSC Group 1 2021
        {
            "subtopic": "Composition of Board - Article 243ZJ",
            "stem_en": "[TNPSC Group 1 2021] According to Article 243ZJ of the Constitution, what is the maximum number of directors of a co-operative society?",
            "stem_ta": "[TNPSC குரூப் 1 2021] அரசியலமைப்பு உறுப்பு 243ZJ-ன் படி, ஒரு கூட்டுறவு சங்கத்தின் இயக்குநர்களின் அதிகபட்ச எண்ணிக்கை யாது?",
            "options": [
                ("21", "21"),
                ("15", "15"),
                ("25", "25"),
                ("11", "11")
            ],
            "correct_key": "A",
            "exp_en": "Article 243ZJ(1) provides that the board of a co-operative society shall consist of such number of directors not exceeding twenty-one.",
            "exp_ta": "உறுப்பு 243ZJ(1)-ன் படி, ஒரு கூட்டுறவு சங்கத்தின் நிர்வாக வாரியம் இருபத்தியொன்றுக்கு மிகாத எண்ணிக்கையிலான இயக்குநர்களைக் கொண்டிருக்க வேண்டும்.",
            "why_a_en": "Correct. The constitutional cap is 21 directors under Article 243ZJ(1).",
            "why_a_ta": "சரி. உறுப்பு 243ZJ(1)-ன் கீழ் அதிகபட்ச இயக்குநர்களின் எண்ணிக்கை 21 ஆகும்.",
            "why_b_en": "Incorrect. 15 is the ceiling for the Council of Ministers under Article 75(1A), not for cooperative boards.",
            "why_b_ta": "தவறு. 15 என்பது அமைச்சரவைக்கான வரம்பு, கூட்டுறவு வாரியத்திற்கான வரம்பு அல்ல.",
            "why_c_en": "Incorrect. 25 is not the ceiling.",
            "why_c_ta": "தவறு. 25 என்பது தவறான எண்.",
            "why_d_en": "Incorrect. 11 is not the constitutional ceiling.",
            "why_d_ta": "தவறு. 11 என்பது தவறான எண்.",
            "tip_en": "Article 243ZJ = Maximum 21 directors + up to 2 co-opted members.",
            "tip_ta": "உறுப்பு 243ZJ = அதிகபட்சம் 21 இயக்குநர்கள் + அதிகபட்சம் 2 இணை உறுப்பினர்கள்.",
            "fact_en": "Co-opted members are over and above the ceiling of 21 directors.",
            "fact_ta": "21 இயக்குநர்கள் என்ற உச்சவரம்பிற்கு அப்பாற்பட்டு 2 இணை உறுப்பினர்களை நியமிக்கலாம்."
        },

        # 6. TNPSC Group 4 2019
        {
            "subtopic": "Reservation of Seats - Article 243ZJ",
            "stem_en": "[TNPSC Group 4 2019] Under Article 243ZJ of the Indian Constitution, how many seats are reserved for women on the board of every co-operative society having individuals as members?",
            "stem_ta": "[TNPSC குரூப் 4 2019] இந்திய அரசியலமைப்பின் உறுப்பு 243ZJ-ன் கீழ், தனிநபர்களை உறுப்பினர்களாகக் கொண்ட ஒவ்வொரு கூட்டுறவு சங்கத்தின் வாரியத்திலும் பெண்களுக்கு எத்தனை இடங்கள் ஒதுக்கீடு செய்யப்பட்டுள்ளன?",
            "options": [
                ("Two seats", "இரண்டு இடங்கள்"),
                ("One seat", "ஒரு இடம்"),
                ("Three seats", "மூன்று இடங்கள்"),
                ("33% of total seats", "மொத்த இடங்களில் 33%"),
            ],
            "correct_key": "A",
            "exp_en": "Article 243ZJ(1) explicitly provides for the reservation of two seats for women and one seat for Scheduled Castes or Scheduled Tribes on the board of every cooperative society.",
            "exp_ta": "உறுப்பு 243ZJ(1)-ன் படி ஒவ்வொரு கூட்டுறவு சங்கத்தின் வாரியத்திலும் பெண்களுக்கு இரண்டு இடங்களும், பட்டியல் சாதியினர்/பழங்குடியினருக்கு ஒரு இடமும் கட்டாயம் ஒதுக்கப்பட வேண்டும்.",
            "why_a_en": "Correct. Two seats are specifically reserved for women under Article 243ZJ(1).",
            "why_a_ta": "சரி. உறுப்பு 243ZJ(1)-ன் கீழ் பெண்களுக்கு இரண்டு இடங்கள் ஒதுக்கப்பட்டுள்ளன.",
            "why_b_en": "Incorrect. One seat is reserved for SC/ST, while two seats are reserved for women.",
            "why_b_ta": "தவறு. SC/ST-க்கு ஒரு இடம், பெண்களுக்கு இரண்டு இடங்கள் ஒதுக்கப்பட்டுள்ளன.",
            "why_c_en": "Incorrect. Three seats is not the quota.",
            "why_c_ta": "தவறு. மூன்று இடங்கள் என்பது தவறானது.",
            "why_d_en": "Incorrect. Part IX-B reserves a fixed 2 seats for women, unlike Part IX/IX-A which specifies not less than one-third.",
            "why_d_ta": "தவறு. மூன்றில் ஒரு பங்கு என்பது பஞ்சாயத்து மற்றும் நகராட்சிகளுக்குரியது; கூட்டுறவில் நிலையாக 2 இடங்கள்.",
            "tip_en": "Contrast: Panchayats/Municipalities = Not less than 1/3rd for women; Cooperatives = Exactly 2 seats for women.",
            "tip_ta": "வேறுபாடு: பஞ்சாயத்து/நகராட்சி = மூன்றில் ஒரு பங்கு (1/3); கூட்டுறவு சங்கங்கள் = சரியாக 2 இடங்கள் பெண்களுக்கு.",
            "fact_en": "Reservation applies where such category of persons are members of the society.",
            "fact_ta": "இப்பிரிவினர் சங்கத்தில் உறுப்பினர்களாக இருக்கும் போது மட்டுமே இவ்விடஒதுக்கீடு பொருந்தும்."
        },

        # 7. TNPSC Group 2 2015
        {
            "subtopic": "Term of Office - Article 243ZJ",
            "stem_en": "[TNPSC Group 2 2015] What is the constitutionally prescribed term of office of elected members of the board of a co-operative society under Article 243ZJ(2)?",
            "stem_ta": "[TNPSC குரூப் 2 2015] உறுப்பு 243ZJ(2)-ன் கீழ் ஒரு கூட்டுறவு சங்க வாரியத்தின் தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்களின் அரசியலமைப்பு ரீதியான பதவிக்காலம் என்ன?",
            "options": [
                ("5 years from the date of election", "தேர்தல் தேதியிலிருந்து 5 ஆண்டுகள்"),
                ("3 years from the date of election", "தேர்தல் தேதியிலிருந்து 3 ஆண்டுகள்"),
                ("6 years from the date of election", "தேர்தல் தேதியிலிருந்து 6 ஆண்டுகள்"),
                ("4 years from the date of election", "தேர்தல் தேதியிலிருந்து 4 ஆண்டுகள்")
            ],
            "correct_key": "A",
            "exp_en": "Article 243ZJ(2) provides that the term of office of elected members of the board and its office bearers shall be five years from the date of election.",
            "exp_ta": "உறுப்பு 243ZJ(2)-ன் படி வாரியத்தின் தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்கள் மற்றும் அதன் நிர்வாகிகளின் பதவிக்காலம் தேர்தல் தேதியிலிருந்து 5 ஆண்டுகள் ஆகும்.",
            "why_a_en": "Correct. Exactly 5 years from the date of election.",
            "why_a_ta": "சரி. தேர்தல் தேதியிலிருந்து சரியாக 5 ஆண்டுகள்.",
            "why_b_en": "Incorrect. 3 years was common under some older state laws, but the constitutional norm is 5 years.",
            "why_b_ta": "தவறு. பழைய மாநில சட்டங்களில் 3 ஆண்டுகள் இருந்தது, ஆனால் அரசியலமைப்பு விதி 5 ஆண்டுகள் ஆகும்.",
            "why_c_en": "Incorrect. 6 years is the term of Rajya Sabha members, not cooperative boards.",
            "why_c_ta": "தவறு. 6 ஆண்டுகள் என்பது மாநிலங்களவை உறுப்பினர்களின் பதவிக்காலம்.",
            "why_d_en": "Incorrect. 4 years is incorrect.",
            "why_d_ta": "தவறு. 4 ஆண்டுகள் என்பது தவறானது.",
            "tip_en": "Term of elected board = 5 years (Article 243ZJ(2)).",
            "tip_ta": "தேர்ந்தெடுக்கப்பட்ட வாரியத்தின் பதவிக்காலம் = 5 ஆண்டுகள் (உறுப்பு 243ZJ(2)).",
            "fact_en": "The 5-year fixed term was introduced to eliminate prolonged nominated management by state governments.",
            "fact_ta": "மாநில அரசுகள் நியமன மேலாண்மையை நீட்டிப்பதைத் தடுக்கவே இந்த 5 ஆண்டு நிலையான பதவிக்காலம் கொண்டுவரப்பட்டது."
        },

        # 8. TNPSC VAO 2016
        {
            "subtopic": "Supersession of Board - Article 243ZL",
            "stem_en": "[TNPSC VAO 2016] Under Article 243ZL, what is the maximum period for which the board of a co-operative society (other than a banking society) can be superseded or kept under suspension?",
            "stem_ta": "[TNPSC VAO 2016] உறுப்பு 243ZL-ன் கீழ் ஒரு கூட்டுறவு சங்கத்தின் (வங்கி சங்கம் அல்லாத) நிர்வாக வாரியத்தை அதிகபட்சமாக எவ்வளவு காலம் கலைக்கவோ அல்லது இடைநீக்கத்தில் வைக்கவோ முடியும்?",
            "options": [
                ("Six months", "ஆறு மாதங்கள்"),
                ("One year", "ஒரு வருடம்"),
                ("Three months", "மூன்று மாதங்கள்"),
                ("Two years", "இரண்டு ஆண்டுகள்")
            ],
            "correct_key": "A",
            "exp_en": "Under Article 243ZL(1), no board shall be superseded or kept under suspension for a period exceeding six months (one year for banking cooperative societies).",
            "exp_ta": "உறுப்பு 243ZL(1)-ன் படி எந்தவொரு கூட்டுறவு சங்க வாரியமும் ஆறு மாதங்களுக்கு மேல் கலைக்கப்படவோ அல்லது இடைநீக்கத்தில் வைக்கப்படவோ கூடாது (கூட்டுறவு வங்கிகளுக்கு 1 வருடம்).",
            "why_a_en": "Correct. Six months is the constitutional limit for non-banking cooperative societies.",
            "why_a_ta": "சரி. வங்கி அல்லாத கூட்டுறவு சங்கங்களுக்கு 6 மாதங்கள் உச்சவரம்பு ஆகும்.",
            "why_b_en": "Incorrect. One year applies only to cooperative societies carrying on banking business.",
            "why_b_ta": "தவறு. ஒரு வருடம் என்பது வங்கித் தொழில் புரியும் கூட்டுறவு சங்கங்களுக்கு மட்டுமே பொருந்தும்.",
            "why_c_en": "Incorrect. Three months is not the limit.",
            "why_c_ta": "தவறு. மூன்று மாதங்கள் என்பது தவறானது.",
            "why_d_en": "Incorrect. Two years is far beyond the constitutional ceiling.",
            "why_d_ta": "தவறு. இரண்டு ஆண்டுகள் என்பது தவறானது.",
            "tip_en": "Supersession Cap: Non-banking = Max 6 months; Banking = Max 1 year.",
            "tip_ta": "வாரியக் கலைப்பு வரம்பு: வங்கி அல்லாதவை = அதிகபட்சம் 6 மாதங்கள்; வங்கிகள் = அதிகபட்சம் 1 வருடம்.",
            "fact_en": "Elections must be conducted within the 6-month period to constitute a new board.",
            "fact_ta": "புதிய வாரியத்தை அமைக்க இந்த 6 மாத காலத்திற்குள் தேர்தல் நடத்தப்பட வேண்டும்."
        },

        # 9. UPSC CSE Prelims 2022
        {
            "subtopic": "Supreme Court Judgment - 2021",
            "stem_en": "[UPSC CSE 2022] In which landmark case did the Supreme Court of India strike down Part IX-B of the Constitution in so far as it related to cooperative societies functioning within a single State?",
            "stem_ta": "[UPSC CSE 2022] எந்த வரலாற்றுச் சிறப்புமிக்க வழக்கில், ஒரு மாநிலத்திற்குள் செயல்படும் கூட்டுறவு சங்கங்கள் தொடர்பான அரசியலமைப்பின் பகுதி IX-B-ஐ உச்சநீதிமன்றம் ரத்து செய்தது?",
            "options": [
                ("Union of India v. Rajendra N. Shah (2021)", "இந்திய ஒன்றியம் எதிர் ராஜேந்திர என். ஷா (2021)"),
                ("Keshvananda Bharati v. State of Kerala (1973)", "கேசவானந்த பாரதி எதிர் கேரள அரசு (1973)"),
                ("S.R. Bommai v. Union of India (1994)", "எஸ்.ஆர். பொம்மை எதிர் இந்திய ஒன்றியம் (1994)"),
                ("Minerva Mills v. Union of India (1980)", "மினர்வா மில்ஸ் எதிர் இந்திய ஒன்றியம் (1980)")
            ],
            "correct_key": "A",
            "exp_en": "In Union of India v. Rajendra N. Shah (July 2021), a 3-judge bench of the Supreme Court headed by Justice R.F. Nariman struck down Part IX-B for state cooperatives due to lack of ratification under Article 368(2) proviso.",
            "exp_ta": "ஜூலை 2021-ல் இந்திய ஒன்றியம் எதிர் ராஜேந்திர என். ஷா வழக்கில், நீதிபதி ஆர்.எஃப். நாரிமன் தலைமையிலான உச்சநீதிமன்ற அமர்வு உறுப்பு 368(2) ஒப்புதல் பெறாததால் பகுதி IX-B-ஐ மாநிலக் கூட்டுறவுகளுக்கு ரத்து செய்தது.",
            "why_a_en": "Correct. Union of India v. Rajendra N. Shah (2021) is the landmark judgment on Part IX-B.",
            "why_a_ta": "சரி. இந்திய ஒன்றியம் எதிர் ராஜேந்திர என். ஷா (2021) பகுதி IX-B மீதான முக்கியத் தீர்ப்பாகும்.",
            "why_b_en": "Incorrect. Kesavananda Bharati (1973) established the Basic Structure doctrine.",
            "why_b_ta": "தவறு. கேசவானந்த பாரதி (1973) அடிப்படைக் கட்டமைப்புத் தத்துவத்தை உருவாக்கியது.",
            "why_c_en": "Incorrect. S.R. Bommai (1994) dealt with Article 356 and federalism.",
            "why_c_ta": "தவறு. எஸ்.ஆர். பொம்மை (1994) உறுப்பு 356 மற்றும் குடியரசுத் தலைவர் ஆட்சி பற்றியது.",
            "why_d_en": "Incorrect. Minerva Mills (1980) dealt with judicial review and balance between Parts III and IV.",
            "why_d_ta": "தவறு. மினர்வா மில்ஸ் (1980) நீதித்துறை மறுஆய்வு மற்றும் பகுதி III, IV சமநிலை பற்றியது.",
            "tip_en": "Remember the Co-operative case: Rajendra N. Shah (2021) — 97th Amendment & Part IX-B.",
            "tip_ta": "நினைவில் கொள்க: கூட்டுறவு வழக்கு = ராஜேந்திர என். ஷா (2021) — 97வது திருத்தம் & பகுதி IX-B.",
            "fact_en": "The judgment originated from a 2013 Gujarat High Court ruling holding Part IX-B ultra vires.",
            "fact_ta": "2013-ல் குஜராத் உயர்நீதிமன்றம் அளித்த தீர்ப்பை எதிர்த்து ஒன்றிய அரசு செய்த மேல்முறையீட்டிலேயே உச்சநீதிமன்றம் இத்தீர்ப்பை வழங்கியது."
        },

        # 10. TNPSC Group 1 2017
        {
            "subtopic": "Audit of Accounts - Article 243ZM",
            "stem_en": "[TNPSC Group 1 2017] Under Article 243ZM, within what period from the close of the financial year must the accounts of a co-operative society be audited?",
            "stem_ta": "[TNPSC குரூப் 1 2017] உறுப்பு 243ZM-ன் கீழ், நிதியாண்டு முடிவடைந்த எத்தனை மாதங்களுக்குள் ஒரு கூட்டுறவு சங்கத்தின் கணக்குகள் தணிக்கை செய்யப்பட வேண்டும்?",
            "options": [
                ("Within six months", "ஆறு மாதங்களுக்குள்"),
                ("Within three months", "மூன்று மாதங்களுக்குள்"),
                ("Within nine months", "ஒன்பது மாதங்களுக்குள்"),
                ("Within one year", "ஒரு வருடத்திற்குள்")
            ],
            "correct_key": "A",
            "exp_en": "Article 243ZM(1) mandates that the accounts of every co-operative society shall be audited within six months of the close of the financial year.",
            "exp_ta": "உறுப்பு 243ZM(1)-ன் படி ஒவ்வொரு கூட்டுறவு சங்கத்தின் கணக்குகளும் நிதியாண்டு முடிவடைந்த ஆறு மாதங்களுக்குள் தணிக்கை செய்யப்பட வேண்டும்.",
            "why_a_en": "Correct. Exactly within 6 months of close of financial year.",
            "why_a_ta": "சரி. நிதியாண்டு முடிவடைந்த 6 மாதங்களுக்குள்.",
            "why_b_en": "Incorrect. Three months is too short.",
            "why_b_ta": "தவறு. மூன்று மாதங்கள் என்பது தவறானது.",
            "why_c_en": "Incorrect. Nine months is not the constitutional period.",
            "why_c_ta": "தவறு. ஒன்பது மாதங்கள் என்பது தவறானது.",
            "why_d_en": "Incorrect. One year is incorrect.",
            "why_d_ta": "தவறு. ஒரு வருடம் என்பது தவறானது.",
            "tip_en": "Key Timelines under Part IX-B: Audit = 6 months; AGM = 6 months; Filing Returns = 6 months.",
            "tip_ta": "பகுதி IX-B முக்கியக் காலக்கெடு: தணிக்கை = 6 மாதங்கள்; பொதுக்குழு = 6 மாதங்கள்; அறிக்கை தாக்கல் = 6 மாதங்கள்.",
            "fact_en": "The auditors must be appointed from a panel approved by the State Government or an authorized body.",
            "fact_ta": "மாநில அரசால் அங்கீகரிக்கப்பட்ட தணிக்கையாளர் குழுவிலிருந்தே தணிக்கையாளர் நியமிக்கப்பட வேண்டும்."
        }
    ]


def get_pyq_questions_batch2():
    return [
        # 11. TNPSC Group 2 2012
        {
            "subtopic": "Historical Evolution - 1904 Act",
            "stem_en": "[TNPSC Group 2 2012] Who is acclaimed as the 'Father of Co-operative Movement in India' for his pioneering report recommending the introduction of agricultural credit societies on the Raiffeisen model?",
            "stem_ta": "[TNPSC குரூப் 2 2012] ரைஃபெய்சன் மாதிரியில் விவசாயக் கடன் சங்கங்களை அறிமுகப்படுத்தப் பரிந்துரைத்த தனது முன்னோடி அறிக்கைக்காக 'இந்திய கூட்டுறவு இயக்கத்தின் தந்தை' எனப் போற்றப்படுபவர் யார்?",
            "options": [
                ("Sir Frederick Nicholson", "சர் பிரடெரிக் நிக்கல்சன்"),
                ("Lord Curzon", "கர்சன் பிரபு"),
                ("Dr. Verghese Kurien", "டாக்டர் வர்கீஸ் குரியன்"),
                ("Vaikunth Mehta", "வைகுந்த் மேத்தா")
            ],
            "correct_key": "A",
            "exp_en": "Sir Frederick Nicholson was placed on special duty in 1892 by the Madras Government to study agricultural banks. His famous report in 1895 with the motto 'Find Raiffeisen' laid the foundation for the Co-operative Credit Societies Act, 1904.",
            "exp_ta": "1892-ல் மெட்ராஸ் அரசால் விவசாய வங்கிகளைப் பற்றி ஆய்வு செய்ய நியமிக்கப்பட்ட சர் பிரடெரிக் நிக்கல்சன், 1895-ல் 'ரைஃபெய்சனைக் கண்டறியுங்கள்' என்ற புகழ்பெற்ற அறிக்கையை அளித்தார். இதுவே 1904 சட்டத்திற்கு வழிகோலியது.",
            "why_a_en": "Correct. Sir Frederick Nicholson is acclaimed as the Father of Indian Co-operative Movement.",
            "why_a_ta": "சரி. சர் பிரடெரிக் நிக்கல்சன் இந்திய கூட்டுறவு இயக்கத்தின் தந்தையாகப் போற்றப்படுகிறார்.",
            "why_b_en": "Incorrect. Lord Curzon was the Viceroy who enacted the 1904 Act.",
            "why_b_ta": "தவறு. கர்சன் பிரபு 1904-ல் சட்டத்தை இயற்றிய வைஸ்ராய் ஆவார்.",
            "why_c_en": "Incorrect. Dr. Verghese Kurien is the Father of the White Revolution.",
            "why_c_ta": "தவறு. டாக்டர் வர்கீஸ் குரியன் வெண்மைப் புரட்சியின் தந்தை ஆவார்.",
            "why_d_en": "Incorrect. Vaikunth Mehta is known as the doyen of Indian cooperation.",
            "why_d_ta": "தவறு. வைகுந்த் மேத்தா நவீன இந்திய கூட்டுறவின் முன்னோடி ஆவார்.",
            "tip_en": "Nicholson = 'Find Raiffeisen' (1895) → 1904 Act.",
            "tip_ta": "நிக்கல்சன் = 'ரைஃபெய்சனைக் கண்டறியுங்கள்' (1895) → 1904 சட்டம்.",
            "fact_en": "Friedrich Wilhelm Raiffeisen was a German cooperative pioneer who developed rural credit unions.",
            "fact_ta": "ரைஃபெய்சன் என்பவர் ஜெர்மனியில் கிராமப்புற கூட்டுறவு கடன் சங்கங்களை உருவாக்கிய முன்னோடியாவார்."
        },

        # 12. TNPSC Group 4 2014
        {
            "subtopic": "Triplicane Urban Cooperative Society",
            "stem_en": "[TNPSC Group 4 2014] Which is the oldest consumer co-operative society in India, established in Chennai in the year 1904?",
            "stem_ta": "[TNPSC குரூப் 4 2014] 1904-ஆம் ஆண்டு சென்னையில் நிறுவப்பட்ட இந்தியாவின் மிகப் பழமையான நுகர்வோர் கூட்டுறவு சங்கம் எது?",
            "options": [
                ("Triplicane Urban Co-operative Society (TUCS)", "திருவல்லிக்கேணி நகர்ப்புறக் கூட்டுறவு சங்கம் (TUCS)"),
                ("Co-optex", "கோ-ஆப்லெக்ஸ்"),
                ("Aavin", "ஆவின்"),
                ("TANCEM", "டான்செம்")
            ],
            "correct_key": "A",
            "exp_en": "The Triplicane Urban Co-operative Society (TUCS) was registered on 9 April 1904 in Triplicane, Madras, making it the first and oldest consumer cooperative society in India.",
            "exp_ta": "திருவல்லிக்கேணி நகர்ப்புறக் கூட்டுறவு சங்கம் (TUCS) 1904 ஏப்ரல் 9 அன்று மெட்ராஸில் தொடங்கப்பட்டது. இதுவே இந்தியாவின் முதல் மற்றும் மிகப்பழமையான நுகர்வோர் கூட்டுறவு பண்டகசாலையாகும்.",
            "why_a_en": "Correct. TUCS is the pioneering consumer cooperative in India.",
            "why_a_ta": "சரி. TUCS இந்தியாவின் முதல் நுகர்வோர் கூட்டுறவு அமைப்பாகும்.",
            "why_b_en": "Incorrect. Co-optex was established in 1935 as a weavers' cooperative.",
            "why_b_ta": "தவறு. கோ-ஆப்லெக்ஸ் 1935-ல் நிறுவப்பட்ட நெசவாளர் கூட்டுறவு ஆகும்.",
            "why_c_en": "Incorrect. Aavin was established much later for dairy processing.",
            "why_c_ta": "தவறு. ஆவின் பால்வளத்திற்காகப் பின்னர் தொடங்கப்பட்டது.",
            "why_d_en": "Incorrect. TANCEM is a state-owned cement corporation, not a cooperative.",
            "why_d_ta": "தவறு. டான்செம் ஒரு அரசு சிமெண்ட் நிறுவனம், கூட்டுறவு அல்ல.",
            "tip_en": "TUCS = 1904 (Triplicane, Chennai) — Oldest consumer cooperative in India.",
            "tip_ta": "TUCS = 1904 (திருவல்லிக்கேணி, சென்னை) — இந்தியாவின் முதல் நுகர்வோர் கூட்டுறவு.",
            "fact_en": "TUCS today operates fair price shops, gas distribution, and consumer supermarkets in Chennai.",
            "fact_ta": "TUCS இன்றும் சென்னையில் நியாயவிலைக் கடைகள், எரிவாயு விநியோகம் மற்றும் பல்பொருள் அங்காடிகளை நடத்தி வருகிறது."
        },

        # 13. TNPSC Assistant Section Officer 2018
        {
            "subtopic": "Elections - Article 243ZK",
            "stem_en": "[TNPSC ASO 2018] Who conducts elections to the co-operative societies in Tamil Nadu?",
            "stem_ta": "[TNPSC ASO 2018] தமிழ்நாட்டில் கூட்டுறவு சங்கங்களுக்கான தேர்தலை நடத்தும் அமைப்பு எது?",
            "options": [
                ("Tamil Nadu State Co-operative Societies Election Commission", "தமிழ்நாடு மாநிலக் கூட்டுறவு சங்கங்களின் தேர்தல் ஆணையம்"),
                ("Tamil Nadu State Election Commission (TNSEC)", "தமிழ்நாடு மாநிலத் தேர்தல் ஆணையம்"),
                ("Election Commission of India (ECI)", "இந்தியத் தேர்தல் ஆணையம்"),
                ("Registrar of Co-operative Societies", "கூட்டுறவு சங்கங்களின் பதிவாளர்")
            ],
            "correct_key": "A",
            "exp_en": "Under Section 33-A of the Tamil Nadu Co-operative Societies Act, 1983 (enacted pursuant to Article 243ZK), elections to cooperative societies are conducted by the Tamil Nadu State Co-operative Societies Election Commission, NOT by the SEC.",
            "exp_ta": "உறுப்பு 243ZK மற்றும் தமிழ்நாடு கூட்டுறவு சங்கங்கள் சட்டம் 1983-ன் பிரிவு 33-A-ன் கீழ், கூட்டுறவு தேர்தல்களை நடத்த தமிழ்நாடு மாநிலக் கூட்டுறவு சங்கங்களின் தேர்தல் ஆணையம் என்ற தனி அமைப்பு அமைக்கப்பட்டுள்ளது.",
            "why_a_en": "Correct. TNSCSEC is the designated independent election authority in Tamil Nadu.",
            "why_a_ta": "சரி. TNSCSEC தமிழ்நாட்டில் இதற்காக உருவாக்கப்பட்ட தனி தேர்தல் ஆணையமாகும்.",
            "why_b_en": "Incorrect. TNSEC conducts local body elections (Panchayats and Municipalities), not cooperative elections.",
            "why_b_ta": "தவறு. TNSEC உள்ளாட்சித் தேர்தல்களை (பஞ்சாயத்து, நகராட்சி) மட்டுமே நடத்துகிறது.",
            "why_c_en": "Incorrect. ECI conducts Parliament and State Legislature elections.",
            "why_c_ta": "தவறு. ECI நாடாளுமன்றம் மற்றும் சட்டமன்றத் தேர்தல்களை நடத்துகிறது.",
            "why_d_en": "Incorrect. The Registrar does not conduct elections; an independent Commission conducts them.",
            "why_d_ta": "தவறு. பதிவாளர் தேர்தலை நடத்துவதில்லை; தனி ஆணையமே நடத்துகிறது.",
            "tip_en": "Do not confuse: TNSEC = Local bodies (Panchayats/Municipalities); TNSCSEC = Cooperative societies.",
            "tip_ta": "குழப்ப வேண்டாம்: TNSEC = உள்ளாட்சி அமைப்புகள்; TNSCSEC = கூட்டுறவு சங்கங்கள்.",
            "fact_en": "The Commissioner of the TNSCSEC has the status and salary equivalent to a High Court Judge or Principal Secretary.",
            "fact_ta": "கூட்டுறவு தேர்தல் ஆணையர் முதன்மைச் செயலாளர் அந்தஸ்திலான அதிகாரியாவார்."
        },

        # 14. TNPSC Group 1 2015
        {
            "subtopic": "Committees on Cooperatives - Gorwala",
            "stem_en": "[TNPSC Group 1 2015] 'Co-operation has failed, but Co-operation must succeed' was the famous observation made by which committee?",
            "stem_ta": "[TNPSC குரூப் 1 2015] 'கூட்டுறவு தோல்வியடைந்தது, ஆனால் கூட்டுறவு வெற்றி பெற்றே தீர வேண்டும்' என்ற வரலாற்றுப் புகழ்பெற்ற கருத்தைத் தெரிவித்த குழு எது?",
            "options": [
                ("All India Rural Credit Survey Committee (Gorwala Committee, 1954)", "அகில இந்திய கிராமப்புற கடன் ஆய்வுக் குழு (கோர்வாலா குழு, 1954)"),
                ("Ram Niwas Mirdha Committee (1965)", "ராம் நிவாஸ் மிர்தா குழு (1965)"),
                ("Brahm Perkash Committee (1991)", "பிரம்ம பிரகாஷ் குழு (1991)"),
                ("Vaidyanathan Committee (2004)", "வைத்தியநாதன் குழு (2004)")
            ],
            "correct_key": "A",
            "exp_en": "The All India Rural Credit Survey Committee (1954) headed by A.D. Gorwala observed that rural cooperation had covered very little credit, famously concluding: 'Cooperation has failed, but Cooperation must succeed.' It recommended the Integrated Scheme of Rural Credit with state partnership.",
            "exp_ta": "ஏ.டி. கோர்வாலா தலைமையிலான அகில இந்திய கிராமப்புற கடன் ஆய்வுக் குழு (1954), 'கூட்டுறவு தோல்வியடைந்தது, ஆனால் கூட்டுறவு வெற்றி பெற்றே தீர வேண்டும்' என்று கூறி, அரசுப் பங்களிப்புடன் கூடிய ஒருங்கிணைந்த கடன் திட்டத்தைப் பரிந்துரைத்தது.",
            "why_a_en": "Correct. Gorwala Committee made this iconic statement in 1954.",
            "why_a_ta": "சரி. 1954-ல் கோர்வாலா குழுவே இந்த வரலாற்றுப் புகழ்பெற்ற வாசகத்தைக் கூறியது.",
            "why_b_en": "Incorrect. Mirdha Committee (1965) focused on eliminating bogus societies.",
            "why_b_ta": "தவறு. மிர்தா குழு (1965) போலி சங்கங்களை ஒழிப்பதில் கவனம் செலுத்தியது.",
            "why_c_en": "Incorrect. Brahm Perkash Committee (1991) drafted the Model Cooperatives Act.",
            "why_c_ta": "தவறு. பிரம்ம பிரகாஷ் குழு (1991) மாதிரி கூட்டுறவு சட்டத்தை வரைந்தது.",
            "why_d_en": "Incorrect. Vaidyanathan Committee (2004) recommended revival package for STCCS.",
            "why_d_ta": "தவறு. வைத்தியநாதன் குழு (2004) குறுகிய கால கடன் மறுமலர்ச்சி நிதி தொகுப்பை வழங்கியது.",
            "tip_en": "Gorwala Committee (1954) = State partnership at all levels + SBI establishment + 'Cooperation must succeed'.",
            "tip_ta": "கோர்வாலா குழு (1954) = அனைத்து மட்டங்களிலும் அரசுப் பங்களிப்பு + SBI உருவாக்கம் + 'கூட்டுறவு வெற்றி பெற்றே தீர வேண்டும்'.",
            "fact_en": "The committee's report led directly to the nationalization of the Imperial Bank of India into the State Bank of India in 1955.",
            "fact_ta": "இக்குழுவின் அறிக்கையே 1955-ல் இம்பீரியல் வங்கியை தேசியமயமாக்கி ஸ்டேட் பாங்க் ஆப் இந்தியாவாக (SBI) மாற்றியது."
        },

        # 15. UPSC CSE Prelims 2018
        {
            "subtopic": "Multi-State Co-operative Societies Act",
            "stem_en": "[UPSC CSE 2018] Multi-State Co-operative Societies having objects not confined to one State are registered and administered by which authority?",
            "stem_ta": "[UPSC CSE 2018] ஒன்றுக்கு மேற்பட்ட மாநிலங்களில் செயல்படும் பல மாநில கூட்டுறவு சங்கங்களைப் பதிவு செய்து நிர்வகிக்கும் அதிகாரி யார்?",
            "options": [
                ("Central Registrar of Co-operative Societies (CRCS)", "மத்திய கூட்டுறவு சங்கங்களின் பதிவாளர் (CRCS)"),
                ("Registrar of Co-operative Societies of the home State", "தாய் மாநிலத்தின் கூட்டுறவு சங்கங்களின் பதிவாளர்"),
                ("Governor of the Reserve Bank of India", "இந்திய ரிசர்வ் வங்கியின் ஆளுநர்"),
                ("Secretary, Ministry of Corporate Affairs", "கார்ப்பரேட் விவகார அமைச்சகத்தின் செயலாளர்")
            ],
            "correct_key": "A",
            "exp_en": "Under the Multi-State Co-operative Societies Act, 2002, the Central Government appoints the Central Registrar of Co-operative Societies (CRCS) under the Ministry of Cooperation to register and regulate multi-state cooperatives.",
            "exp_ta": "பல மாநில கூட்டுறவு சங்கங்கள் சட்டம் 2002-ன் கீழ், கூட்டுறவு அமைச்சகத்தின் கீழ் செயல்படும் மத்திய கூட்டுறவு சங்கங்களின் பதிவாளர் (CRCS) பல மாநில கூட்டுறவு சங்கங்களைப் பதிவு செய்து நிர்வகிக்கிறார்.",
            "why_a_en": "Correct. CRCS is the statutory authority appointed under MSCS Act 2002.",
            "why_a_ta": "சரி. CRCS என்பது 2002 சட்டத்தின் கீழ் நியமிக்கப்படும் சட்டப்பூர்வ அதிகாரியாகும்.",
            "why_b_en": "Incorrect. State Registrars only regulate societies operating within a single State under List II Entry 32.",
            "why_b_ta": "தவறு. மாநில பதிவாளர்கள் ஒரு மாநிலத்திற்குள் மட்டுமே செயல்படும் சங்கங்களை நிர்வகிக்கின்றனர்.",
            "why_c_en": "Incorrect. RBI Governor regulates monetary policy and banks, not cooperative registration.",
            "why_c_ta": "தவறு. ரிசர்வ் வங்கி ஆளுநர் பணவியல் கொள்கையைக் கட்டுப்படுத்துகிறார்.",
            "why_d_en": "Incorrect. Corporate Affairs Ministry handles Companies, not Cooperatives.",
            "why_d_ta": "தவறு. கார்ப்பரேட் விவகார அமைச்சகம் நிறுவனங்களைக் கவனிக்கிறது.",
            "tip_en": "State Cooperatives = State RCS (List II); Multi-State Cooperatives = Central RCS / CRCS (List I).",
            "tip_ta": "மாநிலக் கூட்டுறவு = மாநில பதிவாளர் (பட்டியல் II); பல மாநிலக் கூட்டுறவு = மத்திய பதிவாளர் (பட்டியல் I).",
            "fact_en": "The CRCS office is headquartered in New Delhi under the Ministry of Cooperation.",
            "fact_ta": "CRCS அலுவலகம் புது தில்லியில் உள்ள மத்திய கூட்டுறவு அமைச்சகத்தின் கீழ் இயங்குகிறது."
        },

        # 16. TNPSC Group 2 2011
        {
            "subtopic": "Primary Agricultural Credit Societies",
            "stem_en": "[TNPSC Group 2 2011] In the three-tier short-term rural cooperative credit structure in India, which institution functions at the grass-root (village) level?",
            "stem_ta": "[TNPSC குரூப் 2 2011] இந்தியாவில் மூன்றடுக்கு குறுகிய கால கிராமப்புற கூட்டுறவு கடன் கட்டமைப்பில் அடிமட்ட (கிராம) அளவில் செயல்படும் அமைப்பு எது?",
            "options": [
                ("Primary Agricultural Credit Society (PACS)", "தொடக்க வேளாண்மைக் கூட்டுறவுக் கடன் சங்கம் (PACS)"),
                ("District Central Cooperative Bank (DCCB)", "மாவட்ட மத்தியக் கூட்டுறவு வங்கி (DCCB)"),
                ("State Cooperative Bank (StCB)", "மாநிலக் கூட்டுறவு வங்கி (StCB)"),
                ("Regional Rural Bank (RRB)", "பிராந்திய ஊரக வங்கி (RRB)")
            ],
            "correct_key": "A",
            "exp_en": "In the 3-tier short-term credit structure, PACS operates at the village level, DCCB at the district level, and State Cooperative Bank (StCB) at the apex state level.",
            "exp_ta": "மூன்றடுக்கு கடன் அமைப்பில், கிராம அளவில் தொடக்க வேளாண் கடன் சங்கங்களும் (PACS), மாவட்ட அளவில் DCCB-யும், மாநில அளவில் உச்ச அமைப்பாக StCB-யும் செயல்படுகின்றன.",
            "why_a_en": "Correct. PACS is the foundation of the rural cooperative credit pyramid.",
            "why_a_ta": "சரி. கிராமப்புற கூட்டுறவு கடன் பிரமிட்டின் அடித்தளமாக PACS உள்ளது.",
            "why_b_en": "Incorrect. DCCB functions at the district/intermediate tier.",
            "why_b_ta": "தவறு. DCCB மாவட்ட அளவில் செயல்படுகிறது.",
            "why_c_en": "Incorrect. StCB functions at the apex state tier.",
            "why_c_ta": "தவறு. StCB மாநில உச்ச அளவில் செயல்படுகிறது.",
            "why_d_en": "Incorrect. RRBs are scheduled commercial banks, not part of the cooperative credit hierarchy.",
            "why_d_ta": "தவறு. RRB என்பது வணிக வங்கியாகும், கூட்டுறவு அமைப்பின் அடுக்கு அல்ல.",
            "tip_en": "Cooperative Pyramid: PACS (Village) → DCCB (District) → StCB (State Apex).",
            "tip_ta": "கூட்டுறவு பிரமிடு: PACS (கிராமம்) → DCCB (மாவட்டம்) → StCB (மாநிலம்).",
            "fact_en": "There are approximately 1 lakh PACS in India with over 13 crore farmer members.",
            "fact_ta": "இந்தியாவில் சுமார் 1 லட்சம் தொடக்க வேளாண் கடன் சங்கங்களும் 13 கோடி விவசாய உறுப்பினர்களும் உள்ளனர்."
        },

        # 17. TNPSC Group 1 2014
        {
            "subtopic": "Urban Co-operative Banks and BR Act",
            "stem_en": "[TNPSC Group 1 2014] From which year was the Banking Regulation Act, 1949 made applicable to Co-operative Banks by the insertion of Section 56?",
            "stem_ta": "[TNPSC குரூப் 1 2014] எந்த ஆண்டிலிருந்து பிரிவு 56-ஐச் சேர்த்ததன் மூலம் வங்கி ஒழுங்குமுறைச் சட்டம் 1949 கூட்டுறவு வங்கிகளுக்குப் பொருந்தும்படி செய்யப்பட்டது?",
            "options": [
                ("1966", "1966"),
                ("1949", "1949"),
                ("1955", "1955"),
                ("1969", "1969")
            ],
            "correct_key": "A",
            "exp_en": "The Banking Laws (Application to Co-operative Societies) Act, 1965 inserted Part V (Section 56) into the Banking Regulation Act, 1949, making it applicable to cooperative banks with effect from 1st March 1966.",
            "exp_ta": "1965-ஆம் ஆண்டின் வங்கிச் சட்டங்கள் திருத்தத்தின் மூலம் பகுதி V (பிரிவு 56) சேர்க்கப்பட்டு, 1966 மார்ச் 1 முதல் வங்கி ஒழுங்குமுறைச் சட்டம் கூட்டுறவு வங்கிகளுக்கு நீட்டிக்கப்பட்டது.",
            "why_a_en": "Correct. 1 March 1966 is the effective date.",
            "why_a_ta": "சரி. 1966 மார்ச் 1 நடைமுறைக்கு வந்த தேதியாகும்.",
            "why_b_en": "Incorrect. 1949 was the year the original BR Act was passed for commercial banks only.",
            "why_b_ta": "தவறு. 1949-ல் வணிக வங்கிகளுக்கு மட்டுமே சட்டம் கொண்டுவரப்பட்டது.",
            "why_c_en": "Incorrect. 1955 was the year SBI was created.",
            "why_c_ta": "தவறு. 1955-ல் SBI உருவாக்கப்பட்டது.",
            "why_d_en": "Incorrect. 1969 was the year 14 major commercial banks were nationalized.",
            "why_d_ta": "தவறு. 1969-ல் 14 வணிக வங்கிகள் தேசியமயமாக்கப்பட்டன.",
            "tip_en": "Timeline: BR Act passed = 1949; Extended to Cooperative Banks (Sec 56) = 1966; BR Amendment strengthening RBI control = 2020.",
            "tip_ta": "காலக்கோடு: வங்கி ஒழுங்குமுறைச் சட்டம் = 1949; கூட்டுறவு வங்கிகளுக்கு நீட்டிப்பு = 1966; ரிசர்வ் வங்கி கட்டுப்பாடு அதிகரிப்பு = 2020.",
            "fact_en": "Section 56 modifies various provisions of the BR Act to adapt them to the cooperative corporate structure.",
            "fact_ta": "பிரிவு 56 கூட்டுறவு அமைப்பிற்கு ஏற்ப வங்கி ஒழுங்குமுறைச் சட்டத்தின் பல்வேறு விதிகளை மாற்றியமைக்கிறது."
        },

        # 18. TNPSC Assistant Director of Cooperatives 2017
        {
            "subtopic": "Model Co-operatives Act 1991",
            "stem_en": "[TNPSC AD of Cooperatives 2017] Which committee drafted the Model Co-operatives Act in 1991 to remove government intervention and restore cooperative democracy?",
            "stem_ta": "[TNPSC கூட்டுறவு உதவி இயக்குநர் 2017] அரசாங்கத் தலையீடுகளை நீக்கி கூட்டுறவு ஜனநாயகத்தை மீட்டெடுப்பதற்காக 1991-ல் மாதிரி கூட்டுறவு சங்கங்கள் சட்டத்தை வரைந்த குழு எது?",
            "options": [
                ("Choudhary Brahm Perkash Committee", "சவுத்ரி பிரம்ம பிரகாஷ் குழு"),
                ("Ram Niwas Mirdha Committee", "ராம் நிவாஸ் மிர்தா குழு"),
                ("A.D. Gorwala Committee", "ஏ.டி. கோர்வாலா குழு"),
                ("K. Santhanam Committee", "கே. சந்தானம் குழு")
            ],
            "correct_key": "A",
            "exp_en": "The Planning Commission appointed an Expert Committee headed by Choudhary Brahm Perkash which submitted its report and the Model Co-operatives Act in 1991, aiming to make cooperatives member-controlled rather than government-dominated.",
            "exp_ta": "திட்டக் குழுவால் நியமிக்கப்பட்ட சவுத்ரி பிரம்ம பிரகாஷ் நிபுணர் குழு 1991-ல் மாதிரி கூட்டுறவு சங்கங்கள் சட்டத்தை வரைந்து அறிக்கையளித்தது. இது கூட்டுறவுகளை அரசாங்கக் கட்டுப்பாட்டிலிருந்து விடுவிக்க வழிகோலியது.",
            "why_a_en": "Correct. Brahm Perkash Committee drafted the 1991 Model Act.",
            "why_a_ta": "சரி. பிரம்ம பிரகாஷ் குழுவே 1991 மாதிரி சட்டத்தை வரைந்தது.",
            "why_b_en": "Incorrect. Mirdha Committee (1965) addressed bogus societies.",
            "why_b_ta": "தவறு. மிர்தா குழு (1965) போலி சங்கங்களை ஆராய்ந்தது.",
            "why_c_en": "Incorrect. Gorwala Committee (1954) recommended state partnership.",
            "why_c_ta": "தவறு. கோர்வாலா குழு (1954) அரசுப் பங்களிப்பைப் பரிந்துரைத்தது.",
            "why_d_en": "Incorrect. Santhanam Committee (1962-64) dealt with prevention of corruption.",
            "why_d_ta": "தவறு. சந்தானம் குழு ஊழல் தடுப்பு பற்றியது.",
            "tip_en": "Brahm Perkash Committee (1991) = Model Co-operatives Act → Influenced MSCS Act 2002 and Mutually Aided Cooperative Societies Acts in AP, etc.",
            "tip_ta": "பிரம்ம பிரகாஷ் குழு (1991) = மாதிரி கூட்டுறவு சட்டம் → 2002 சட்டம் மற்றும் ஆந்திர சுய உதவி கூட்டுறவு சட்டங்களுக்கு வழிகோலியது.",
            "fact_en": "Choudhary Brahm Perkash was the first Chief Minister of Delhi and a prominent cooperative leader.",
            "fact_ta": "சவுத்ரி பிரம்ம பிரகாஷ் டெல்லியின் முதல் முதலமைச்சராகவும் சிறந்த கூட்டுறவுத் தலைவராகவும் திகழ்ந்தவர்."
        },

        # 19. TNPSC Group 2 2013
        {
            "subtopic": "Amul and Kaira District Union",
            "stem_en": "[TNPSC Group 2 2013] Under whose inspirational guidance was the Kaira District Co-operative Milk Producers' Union (Amul) founded in Anand, Gujarat in 1946?",
            "stem_ta": "[TNPSC குரூப் 2 2013] 1946-ல் குஜராத்தின் ஆனந்த் நகரில் யாருடைய உத்வேக வழிகாட்டுதலின் கீழ் கைரா மாவட்ட கூட்டுறவு பால் உற்பத்தியாளர்கள் ஒன்றியம் (அமுல்) நிறுவப்பட்டது?",
            "options": [
                ("Sardar Vallabhbhai Patel", "சர்தார் வல்லபாய் படேல்"),
                ("Mahatma Gandhi", "மகாத்மா காந்தி"),
                ("Jawaharlal Nehru", "ஜவஹர்லால் நேரு"),
                ("Morarji Desai", "மொரார்ஜி தேசாய்")
            ],
            "correct_key": "A",
            "exp_en": "Sardar Vallabhbhai Patel advised local dairy farmers exploited by Polson dairy to organize themselves into a cooperative milk union, leading to the birth of Amul in 1946 led by Tribhuvandas Patel.",
            "exp_ta": "போல்சன் நிறுவனத்தால் சுரண்டப்பட்ட விவசாயிகளை ஒன்றிணைந்து சொந்தக் கூட்டுறவு சங்கத்தை அமைக்குமாறு சர்தார் வல்லபாய் படேல் அறிவுறுத்தினார். இதன் மூலம் 1946-ல் திருபுவன்தாஸ் படேல் தலைமையில் அமுல் உருவானது.",
            "why_a_en": "Correct. Sardar Vallabhbhai Patel inspired the founding of Amul.",
            "why_a_ta": "சரி. சர்தார் வல்லபாய் படேலின் வழிகாட்டலிலேயே அமுல் தொடங்கியது.",
            "why_b_en": "Incorrect. Though Gandhi championed village self-sufficiency, Patel directly organized Anand farmers.",
            "why_b_ta": "தவறு. படேலே நேரடியாக ஆனந்த் விவசாயிகளை வழிநடத்தினார்.",
            "why_c_en": "Incorrect. Nehru later inaugurated the Amul plant but did not organize the 1946 union.",
            "why_c_ta": "தவறு. நேரு பின்னர் ஆலையைத் திறந்து வைத்தார், சங்கத்தை உருவாக்கவில்லை.",
            "why_d_en": "Incorrect. Morarji Desai was Patel's deputy who helped Tribhuvandas Patel.",
            "why_d_ta": "தவறு. மொரார்ஜி தேசாய் உடனிருந்த தலைவர், முக்கிய வழிகாட்டி படேல் ஆவார்.",
            "tip_en": "Amul Trinity: Sardar Patel (Inspiration) + Tribhuvandas Patel (Founder-President) + Dr. Verghese Kurien (Managerial/Technological Genius).",
            "tip_ta": "அமுல் மும்மூர்த்திகள்: சர்தார் படேல் (வழிகாட்டி) + திருபுவன்தாஸ் படேல் (நிறுவனர்-தலைவர்) + டாக்டர் வர்கீஸ் குரியன் (தொழில்நுட்ப சிற்பி).",
            "fact_en": "The name AMUL stands for Anand Milk Union Limited and is derived from Sanskrit 'Amulya' meaning priceless.",
            "fact_ta": "அமுல் (AMUL) என்பது ஆனந்த் பால் ஒன்றியத்தைக் குறிப்பதுடன் சமஸ்கிருதத்தின் 'அமுல்யா' (விலைமதிப்பற்றது) என்ற சொல்லிலிருந்தும் வந்தது."
        },

        # 20. UPSC CSE Prelims 2017
        {
            "subtopic": "NABARD and Cooperative Credit",
            "stem_en": "[UPSC CSE 2017] National Bank for Agriculture and Rural Development (NABARD) was established in 1982 on the recommendations of which committee?",
            "stem_ta": "[UPSC CSE 2017] விவசாயம் மற்றும் ஊரக வளர்ச்சிக்கான தேசிய வங்கி (NABARD) 1982-ல் எந்தக் குழுவின் பரிந்துரையின் பேரில் நிறுவப்பட்டது?",
            "options": [
                ("B. Sivaraman Committee (CRAFICARD)", "பி. சிவராமன் குழு (CRAFICARD)"),
                ("A.D. Gorwala Committee", "ஏ.டி. கோர்வாலா குழு"),
                ("M. Narasimham Committee", "எம். நரசிம்மம் குழு"),
                ("R.V. Gupta Committee", "ஆர்.வி. குப்தா குழு")
            ],
            "correct_key": "A",
            "exp_en": "The Committee to Review Arrangements For Institutional Credit for Agriculture and Rural Development (CRAFICARD) headed by B. Sivaraman recommended establishing NABARD, which was set up under Act 61 of 1981 on 12 July 1982.",
            "exp_ta": "பி. சிவராமன் தலைமையிலான கிராஃபிகார்ட் (CRAFICARD) குழுவின் பரிந்துரையின் பேரில், 1981-ஆம் ஆண்டு சட்டத்தின் கீழ் 1982 ஜூலை 12 அன்று நபார்டு வங்கி நிறுவப்பட்டது.",
            "why_a_en": "Correct. B. Sivaraman Committee recommended the establishment of NABARD.",
            "why_a_ta": "சரி. பி. சிவராமன் குழுவே நபார்டு வங்கியை அமைக்கப் பரிந்துரைத்தது.",
            "why_b_en": "Incorrect. Gorwala Committee (1954) led to SBI establishment.",
            "why_b_ta": "தவறு. கோர்வாலா குழு (1954) SBI உருவாக்கத்திற்கு வழிகோலியது.",
            "why_c_en": "Incorrect. Narasimham Committee (1991, 1998) dealt with banking sector reforms.",
            "why_c_ta": "தவறு. நரசிம்மம் குழு (1991) வங்கித்துறை சீர்திருத்தங்கள் பற்றியது.",
            "why_d_en": "Incorrect. R.V. Gupta Committee (1997) dealt with simplification of agricultural credit.",
            "why_d_ta": "தவறு. ஆர்.வி. குப்தா குழு (1997) விவசாயக் கடன் நடைமுறைகளை எளிமைப்படுத்துவது பற்றியது.",
            "tip_en": "NABARD established on 12 July 1982; Architect = B. Sivaraman Committee (CRAFICARD).",
            "tip_ta": "நபார்டு நிறுவப்பட்ட நாள்: 12 ஜூலை 1982; குழு = பி. சிவராமன் குழு.",
            "fact_en": "NABARD took over the agricultural credit functions of the Reserve Bank of India (ACD and RPCD).",
            "fact_ta": "ரிசர்வ் வங்கியின் விவசாய கடன் பணிகளை ஏற்று நபார்டு வங்கி செயல்படத் தொடங்கியது."
        }
    ]


def get_pyq_questions_batch3():
    return [
        # 21. TNPSC Group 1 2020
        {
            "subtopic": "Tamil Nadu Co-operative Societies Act 1983",
            "stem_en": "[TNPSC Group 1 2020] Under which Section of the Tamil Nadu Co-operative Societies Act, 1983 is the settlement of disputes by arbitration provided?",
            "stem_ta": "[TNPSC குரூப் 1 2020] தமிழ்நாடு கூட்டுறவு சங்கங்கள் சட்டம் 1983-ன் எந்தப் பிரிவின் கீழ் நடுவர் தீர்ப்பாயம் (Arbitration) மூலம் தகராறுகளைத் தீர்ப்பதற்கான வழிவகை செய்யப்பட்டுள்ளது?",
            "options": [
                ("Section 90", "பிரிவு 90"),
                ("Section 81", "பிரிவு 81"),
                ("Section 87", "பிரிவு 87"),
                ("Section 88", "பிரிவு 88")
            ],
            "correct_key": "A",
            "exp_en": "Section 90 of the Tamil Nadu Co-operative Societies Act, 1983 provides for the reference of disputes touching the constitution, management or business of a registered society to the Registrar for arbitration.",
            "exp_ta": "தமிழ்நாடு கூட்டுறவு சங்கங்கள் சட்டம் 1983-ன் பிரிவு 90, சங்கத்தின் நிர்வாகம் அல்லது வணிகம் தொடர்பான தகராறுகளைப் பதிவாளரிடம் நடுவர் தீர்ப்புக்காக சமர்ப்பிக்க வழிவகை செய்கிறது.",
            "why_a_en": "Correct. Section 90 deals with arbitration of disputes.",
            "why_a_ta": "சரி. பிரிவு 90 தகராறுகளை நடுவர் தீர்ப்பு மூலம் தீர்ப்பது பற்றியது.",
            "why_b_en": "Incorrect. Section 81 deals with statutory Inquiry into the working of a society.",
            "why_b_ta": "தவறு. பிரிவு 81 சட்டப்பூர்வ விசாரணை (Inquiry) பற்றியது.",
            "why_c_en": "Incorrect. Section 87 deals with Surcharge proceedings for misappropriation or breach of trust.",
            "why_c_ta": "தவறு. பிரிவு 87 முறைகேடுகளுக்கான இழப்பீடு (Surcharge) பற்றியது.",
            "why_d_en": "Incorrect. Section 88 deals with supersession of the board.",
            "why_d_ta": "தவறு. பிரிவு 88 வாரியத்தைக் கலைப்பது பற்றியது.",
            "tip_en": "TN Act 1983 Key Sections: Sec 81 = Inquiry; Sec 87 = Surcharge; Sec 88 = Supersession; Sec 90 = Arbitration (Disputes).",
            "tip_ta": "தமிழக சட்டத்தின் முக்கிய பிரிவுகள்: பிரிவு 81 = விசாரணை; பிரிவு 87 = இழப்பீடு; பிரிவு 88 = வாரியக் கலைப்பு; பிரிவு 90 = தகராறுகள் தீர்த்தல்.",
            "fact_en": "Civil courts are barred from entertaining disputes that fall under Section 90.",
            "fact_ta": "பிரிவு 90-ன் கீழ் வரும் வழக்குகளை விசாரிக்க உரிமையியல் நீதிமன்றங்களுக்குத் தடை விதிக்கப்பட்டுள்ளது."
        },

        # 22. TNPSC Group 2 2017
        {
            "subtopic": "Tamil Nadu Co-operative Societies Act - Inquiry",
            "stem_en": "[TNPSC Group 2 2017] Under Section 81 of the Tamil Nadu Co-operative Societies Act, 1983, who is empowered to order a statutory inquiry into the affairs of a co-operative society?",
            "stem_ta": "[TNPSC குரூப் 2 2017] தமிழ்நாடு கூட்டுறவு சங்கங்கள் சட்டம் 1983-ன் பிரிவு 81-ன் கீழ், ஒரு கூட்டுறவு சங்கத்தின் செயல்பாடுகள் குறித்து சட்டப்பூர்வ விசாரணைக்கு உத்தரவிட யாருக்கு அதிகாரம் உள்ளது?",
            "options": [
                ("The Registrar of Co-operative Societies", "கூட்டுறவு சங்கங்களின் பதிவாளர்"),
                ("The District Collector", "மாவட்ட ஆட்சியர்"),
                ("The Chief Judicial Magistrate", "தலைமை நீதித்துறை நடுவர்"),
                ("The President of the Society", "சங்கத்தின் தலைவர்")
            ],
            "correct_key": "A",
            "exp_en": "Section 81 empowers the Registrar of Co-operative Societies, of his own motion or on the application of a majority of the board, not less than one-third of the members, or a financing bank, to hold or direct an inquiry into the constitution, working and financial condition of a registered society.",
            "exp_ta": "பிரிவு 81-ன் படி, கூட்டுறவு சங்கங்களின் பதிவாளர் தானாக முன்வந்தோ அல்லது வாரியத்தின் பெரும்பான்மையினர், மூன்றில் ஒரு பங்கு உறுப்பினர்கள் கோரிக்கையின் பேரிலோ விசாரணைக்கு உத்தரவிடலாம்.",
            "why_a_en": "Correct. The Registrar is the statutory authority under Section 81.",
            "why_a_ta": "சரி. பதிவாளரே பிரிவு 81-ன் கீழ் விசாரணைக்கு உத்தரவிடும் சட்டப்பூர்வ அதிகாரியாவார்.",
            "why_b_en": "Incorrect. The Collector does not order Section 81 inquiries.",
            "why_b_ta": "தவறு. மாவட்ட ஆட்சியருக்கு இதில் நேரடி அதிகாரமில்லை.",
            "why_c_en": "Incorrect. Judicial Magistrates have no role under Section 81.",
            "why_c_ta": "தவறு. நடுவர் நீதிமன்றங்களுக்கு இதில் அதிகாரமில்லை.",
            "why_d_en": "Incorrect. The President cannot order an inquiry against his own society.",
            "why_d_ta": "தவறு. தலைவர் தன் சொந்த சங்கத்தின் மீது விசாரணைக்கு உத்தரவிட முடியாது.",
            "tip_en": "Section 81 = Registrar orders statutory inquiry into society affairs.",
            "tip_ta": "பிரிவு 81 = பதிவாளர் சங்க விவகாரங்கள் மீது சட்டப்பூர்வ விசாரணைக்கு உத்தரவிடுகிறார்.",
            "fact_en": "The inquiry must be completed within 3 months, extendable up to 6 months for recorded reasons.",
            "fact_ta": "விசாரணை 3 மாதங்களுக்குள் முடிக்கப்பட வேண்டும், காரணங்கள் கூறி 6 மாதங்கள் வரை நீட்டிக்கலாம்."
        },

        # 23. TNPSC Assistant Director of Cooperatives 2018
        {
            "subtopic": "Tamil Nadu Co-operative Societies Act - Surcharge",
            "stem_en": "[TNPSC AD of Cooperatives 2018] Surcharge proceedings against persons responsible for misappropriation, fraudulent retention, or breach of trust in a cooperative society are initiated under which Section of the Tamil Nadu Co-operative Societies Act, 1983?",
            "stem_ta": "[TNPSC கூட்டுறவு உதவி இயக்குநர் 2018] கூட்டுறவு சங்கத்தில் நிதி முறைகேடு, மோசடி அல்லது நம்பிக்கை துரோகம் செய்தவர்களுக்கு எதிராக எந்தப் பிரிவின் கீழ் இழப்பீட்டு நடவடிக்கைகள் (Surcharge) தொடங்கப்படுகின்றன?",
            "options": [
                ("Section 87", "பிரிவு 87"),
                ("Section 81", "பிரிவு 81"),
                ("Section 88", "பிரிவு 88"),
                ("Section 90", "பிரிவு 90")
            ],
            "correct_key": "A",
            "exp_en": "Section 87 of the 1983 Act empowers the Registrar, following an audit (Sec 80), inquiry (Sec 81), inspection (Sec 82/83), or winding up, to assess damages and pass a surcharge order recovering money from any person who caused loss to the society.",
            "exp_ta": "பிரிவு 87-ன் படி, தணிக்கை அல்லது விசாரணைக்குப் பிறகு சங்கத்திற்கு நிதி இழப்பு ஏற்படுத்திய நபரிடமிருந்து தொகையை வசூலிக்க பதிவாளர் இழப்பீட்டு (Surcharge) உத்தரவைப் பிறப்பிக்கலாம்.",
            "why_a_en": "Correct. Section 87 provides for Surcharge orders.",
            "why_a_ta": "சரி. பிரிவு 87 இழப்பீட்டு நடவடிக்கைகள் பற்றியதாகும்.",
            "why_b_en": "Incorrect. Section 81 is the fact-finding Inquiry stage.",
            "why_b_ta": "தவறு. பிரிவு 81 விசாரணை நிலையாகும்.",
            "why_c_en": "Incorrect. Section 88 relates to supersession of the board.",
            "why_c_ta": "தவறு. பிரிவு 88 வாரியக் கலைப்பு பற்றியது.",
            "why_d_en": "Incorrect. Section 90 relates to civil disputes arbitration.",
            "why_d_ta": "தவறு. பிரிவு 90 சிவில் தகராறுகள் நடுவர் தீர்ப்பு பற்றியது.",
            "tip_en": "Sequence of accountability: Sec 80 (Audit) / Sec 81 (Inquiry) → Sec 87 (Surcharge Recovery).",
            "tip_ta": "நடவடிக்கை வரிசை: பிரிவு 80 (தணிக்கை) / பிரிவு 81 (விசாரணை) → பிரிவு 87 (இழப்பீடு வசூலித்தல்).",
            "fact_en": "An appeal against a Section 87 surcharge order lies before the Co-operative Tribunal under Section 152.",
            "fact_ta": "பிரிவு 87 இழப்பீட்டு உத்தரவிற்கு எதிராகப் பிரிவு 152-ன் கீழ் கூட்டுறவு தீர்ப்பாயத்தில் மேல்முறையீடு செய்யலாம்."
        },

        # 24. TNPSC Group 1 2011
        {
            "subtopic": "Pioneering Co-operative Leaders - Vaikunth Mehta",
            "stem_en": "[TNPSC Group 1 2011] Which eminent Indian cooperative thinker is hailed as the 'Doyen of the Indian Co-operative Movement' and served as the first Chairman of the Khadi and Village Industries Commission (KVIC)?",
            "stem_ta": "[TNPSC குரூப் 1 2011] 'இந்திய கூட்டுறவு இயக்கத்தின் முதன்மை வழிகாட்டி' எனப் போற்றப்படுபவரும், காதி மற்றும் கிராமத் தொழில்கள் ஆணையத்தின் (KVIC) முதல் தலைவராகப் பணியாற்றியவருமான சிறந்த சிந்தனையாளர் யார்?",
            "options": [
                ("Vaikunth Lallubhai Mehta", "வைகுந்த் லல்லுபாய் மேத்தா"),
                ("Dr. Verghese Kurien", "டாக்டர் வர்கீஸ் குரியன்"),
                ("Tribhuvandas Patel", "திருபுவன்தாஸ் படேல்"),
                ("C. Subramaniam", "சி. சுப்பிரமணியம்")
            ],
            "correct_key": "A",
            "exp_en": "Vaikunth Lallubhai Mehta (1891-1964) devoted his entire life to cooperative education, banking, and rural industries. He was the first Chairman of KVIC (1957) and Finance Minister of Bombay State. The premier institute VAMNICOM in Pune is named in his honour.",
            "exp_ta": "வைகுந்த் மேத்தா தனது வாழ்நாள் முழுவதையும் கூட்டுறவு கல்வி, வங்கி மற்றும் கிராமத் தொழில்களுக்கு அர்ப்பணித்தார். அவர் 1957-ல் KVIC-ன் முதல் தலைவராக இருந்தார். புனேயில் உள்ள VAMNICOM நிறுவனம் இவர் நினைவாக நிறுவப்பட்டது.",
            "why_a_en": "Correct. Vaikunth Mehta is known as the Doyen of Indian Cooperation.",
            "why_a_ta": "சரி. வைகுந்த் மேத்தா இந்திய கூட்டுறவின் முதன்மை வழிகாட்டியாகப் போற்றப்படுகிறார்.",
            "why_b_en": "Incorrect. Dr. Kurien led the dairy White Revolution.",
            "why_b_ta": "தவறு. டாக்டர் குரியன் வெண்மைப் புரட்சியை வழிநடத்தினார்.",
            "why_c_en": "Incorrect. Tribhuvandas Patel was the founding chairman of Amul.",
            "why_c_ta": "தவறு. திருபுவன்தாஸ் படேல் அமுலின் நிறுவனத் தலைவராவார்.",
            "why_d_en": "Incorrect. C. Subramaniam was the architect of India's Green Revolution.",
            "why_d_ta": "தவறு. சி. சுப்பிரமணியம் பசுமைப் புரட்சியின் சிற்பி ஆவார்.",
            "tip_en": "VAMNICOM = Vaikunth Mehta National Institute of Cooperative Management, Pune.",
            "tip_ta": "VAMNICOM = வைகுந்த் மேத்தா தேசிய கூட்டுறவு மேலாண்மை நிறுவனம், புனே.",
            "fact_en": "The Vaikunth Mehta Committee on Cooperative Credit (1960) recommended viability norms for primary societies.",
            "fact_ta": "1960-ல் வைகுந்த் மேத்தா குழு தொடக்க கூட்டுறவு கடன் சங்கங்களின் நிலைத்தன்மை விதிகளைப் பரிந்துரைத்தது."
        },

        # 25. UPSC CSE Prelims 2016
        {
            "subtopic": "National Cooperative Development Corporation (NCDC)",
            "stem_en": "[UPSC CSE 2016] With reference to the National Cooperative Development Corporation (NCDC), consider the following:\nIn which year was NCDC established as a statutory corporation by an Act of Parliament?",
            "stem_ta": "[UPSC CSE 2016] தேசிய கூட்டுறவு மேம்பாட்டுக் கழகம் (NCDC) நாடாளுமன்றச் சட்டத்தின் மூலம் எந்த ஆண்டு ஒரு சட்டப்பூர்வக் கழகமாக நிறுவப்பட்டது?",
            "options": [
                ("1963", "1963"),
                ("1952", "1952"),
                ("1975", "1975"),
                ("1982", "1982")
            ],
            "correct_key": "A",
            "exp_en": "NCDC was established in March 1963 under the National Cooperative Development Corporation Act, 1962.",
            "exp_ta": "1962-ஆம் ஆண்டின் NCDC சட்டத்தின் கீழ் 1963 மார்ச்சில் தேசிய கூட்டுறவு மேம்பாட்டுக் கழகம் நிறுவப்பட்டது.",
            "why_a_en": "Correct. NCDC was established in 1963.",
            "why_a_ta": "சரி. NCDC 1963-ல் நிறுவப்பட்டது.",
            "why_b_en": "Incorrect. 1952 was the year of the Community Development Programme.",
            "why_b_ta": "தவறு. 1952 சமூக மேம்பாட்டுத் திட்டம் தொடங்கப்பட்ட ஆண்டு.",
            "why_c_en": "Incorrect. 1975 was the year RRBs were established.",
            "why_c_ta": "தவறு. 1975 பிராந்திய ஊரக வங்கிகள் தொடங்கப்பட்ட ஆண்டு.",
            "why_d_en": "Incorrect. 1982 was the year NABARD was established.",
            "why_d_ta": "தவறு. 1982 நபார்டு வங்கி தொடங்கப்பட்ட ஆண்டு.",
            "tip_en": "Chronology: NCDC = 1963; NDDB = 1965; NABARD = 1982.",
            "tip_ta": "காலக்கோடு: NCDC = 1963; NDDB = 1965; நபார்டு = 1982.",
            "fact_en": "NCDC is now under the administrative control of the Ministry of Cooperation.",
            "fact_ta": "NCDC தற்போது மத்திய கூட்டுறவு அமைச்சகத்தின் நிர்வாகக் கட்டுப்பாட்டில் இயங்குகிறது."
        },

        # 26. TNPSC Group 4 2018
        {
            "subtopic": "Weavers Cooperatives - Co-optex",
            "stem_en": "[TNPSC Group 4 2018] In which year was the Tamil Nadu Handloom Weavers' Co-operative Society Limited, popularly known as 'Co-optex', established?",
            "stem_ta": "[TNPSC குரூப் 4 2018] 'கோ-ஆப்லெக்ஸ்' என்று பிரபலமாக அழைக்கப்படும் தமிழ்நாடு கைத்தறி நெசவாளர் கூட்டுறவு சங்கம் எந்த ஆண்டு நிறுவப்பட்டது?",
            "options": [
                ("1935", "1935"),
                ("1947", "1947"),
                ("1952", "1952"),
                ("1968", "1968")
            ],
            "correct_key": "A",
            "exp_en": "Co-optex was formed in 1935 as the Madras Handloom Weavers' Provincial Co-operative Society to organize scattered weavers and eliminate exploitation by middlemen.",
            "exp_ta": "நெசவாளர்களை ஒருங்கிணைத்து இடைத்தரகர்களின் சுரண்டலைத் தடுக்க 1935-ல் மெட்ராஸ் மாகாண கைத்தறி நெசவாளர் கூட்டுறவு சங்கமாக கோ-ஆப்லெக்ஸ் நிறுவப்பட்டது.",
            "why_a_en": "Correct. Co-optex was founded in 1935.",
            "why_a_ta": "சரி. கோ-ஆப்லெக்ஸ் 1935-ல் நிறுவப்பட்டது.",
            "why_b_en": "Incorrect. 1947 is the year of Indian Independence.",
            "why_b_ta": "தவறு. 1947 சுதந்திர ஆண்டு.",
            "why_c_en": "Incorrect. 1952 is incorrect.",
            "why_c_ta": "தவறு. 1952 தவறான ஆண்டு.",
            "why_d_en": "Incorrect. 1968 is incorrect.",
            "why_d_ta": "தவறு. 1968 தவறான ஆண்டு.",
            "tip_en": "Co-optex = 1935 (Apex handloom cooperative society of Tamil Nadu).",
            "tip_ta": "கோ-ஆப்லெக்ஸ் = 1935 (தமிழ்நாட்டின் முதன்மை கைத்தறி நெசவாளர் கூட்டுறவு சங்கம்).",
            "fact_en": "Co-optex holds several Geographical Indication (GI) tags including Kanchipuram silk and Bhavani jamakkalam.",
            "fact_ta": "காஞ்சிபுரம் பட்டு, பவானி ஜமக்காளம் உள்ளிட்ட பல புவிசார் குறியீடுகளைக் (GI) கோ-ஆப்லெக்ஸ் சந்தைப்படுத்துகிறது."
        },

        # 27. TNPSC Group 2 2014
        {
            "subtopic": "Aavin and Dairy Cooperatives",
            "stem_en": "[TNPSC Group 2 2014] What is the apex milk cooperative organization in Tamil Nadu established in 1972 on the Anand pattern?",
            "stem_ta": "[TNPSC குரூப் 2 2014] 1972-ல் ஆனந்த் மாதிரியில் தமிழ்நாட்டில் நிறுவப்பட்ட உச்ச பால்வளக் கூட்டுறவு அமைப்பு எது?",
            "options": [
                ("Tamil Nadu Co-operative Milk Producers' Federation (Aavin)", "தமிழ்நாடு கூட்டுறவு பால் உற்பத்தியாளர்கள் கூட்டமைப்பு (ஆவின்)"),
                ("Amul", "அமுல்"),
                ("Nandini", "நந்தினி"),
                ("Verka", "வெர்கா")
            ],
            "correct_key": "A",
            "exp_en": "The Tamil Nadu Co-operative Milk Producers' Federation Limited (TCMPF), popularly known as Aavin, was established in 1972 (taking over from the Dairy Development Department) as the apex dairy cooperative body.",
            "exp_ta": "ஆவின் என்று அழைக்கப்படும் தமிழ்நாடு கூட்டுறவு பால் உற்பத்தியாளர்கள் கூட்டமைப்பு 1972-ல் ஆனந்த் மாதிரியில் உச்ச அமைப்பாக உருவாக்கப்பட்டது.",
            "why_a_en": "Correct. Aavin is Tamil Nadu's apex dairy cooperative brand.",
            "why_a_ta": "சரி. ஆவின் தமிழ்நாட்டின் உச்ச பால்வளக் கூட்டுறவு அமைப்பாகும்.",
            "why_b_en": "Incorrect. Amul belongs to Gujarat (GCMMF).",
            "why_b_ta": "தவறு. அமுல் குஜராத்தின் கூட்டுறவு நிறுவனம்.",
            "why_c_en": "Incorrect. Nandini belongs to Karnataka (KMF).",
            "why_c_ta": "தவறு. நந்தினி கர்நாடகாவின் பால் கூட்டுறவு நிறுவனம்.",
            "why_d_en": "Incorrect. Verka belongs to Punjab (Milkfed).",
            "why_d_ta": "தவறு. வெர்கா பஞ்சாபின் பால் கூட்டுறவு நிறுவனம்.",
            "tip_en": "State Dairy Brands: Aavin (Tamil Nadu), Amul (Gujarat), Nandini (Karnataka), Milma (Kerala), Vijaya (Andhra Pradesh).",
            "tip_ta": "மாநில பால் பிராண்டுகள்: ஆவின் (தமிழ்நாடு), அமுல் (குஜராத்), நந்தினி (கர்நாடகா), மில்மா (கேரளா), விஜயா (ஆந்திரா).",
            "fact_en": "The 3-tier structure in TN: Village Milk Societies → District Milk Unions → TCMPF (Aavin Apex).",
            "fact_ta": "தமிழ்நாட்டின் மூன்றடுக்கு: கிராம சங்கம் → மாவட்ட ஒன்றியம் → மாநில ஆவின் கூட்டமைப்பு."
        },

        # 28. TNPSC Group 1 2013
        {
            "subtopic": "First Provincial Act - Bombay 1925",
            "stem_en": "[TNPSC Group 1 2013] Which was the first British Indian Province to pass its own independent Co-operative Societies Act in 1925 after co-operation was devolved to Provinces under the 1919 Reforms?",
            "stem_ta": "[TNPSC குரூப் 1 2013] 1919 சீர்திருத்தங்களின் கீழ் கூட்டுறவு மாகாணங்களுக்கு மாற்றப்பட்ட பிறகு, 1925-ல் தனது சொந்த சுயாதீன கூட்டுறவு சங்கங்கள் சட்டத்தை இயற்றிய முதல் பிரிட்டிஷ் இந்திய மாகாணம் எது?",
            "options": [
                ("Bombay Province", "பம்பாய் மாகாணம்"),
                ("Madras Province", "மெட்ராஸ் மாகாணம்"),
                ("Bengal Province", "வங்காள மாகாணம்"),
                ("Punjab Province", "பஞ்சாப் மாகாணம்")
            ],
            "correct_key": "A",
            "exp_en": "Following the Government of India Act 1919 making co-operation a provincial transferred subject, Bombay became the first province to enact its own Co-operative Societies Act in 1925 (Bombay Act VII of 1925).",
            "exp_ta": "1919 சட்டம் கூட்டுறவை மாகாண மாற்றப்பட்ட துறையாக்கியதைத் தொடர்ந்து, 1925-ல் பம்பாய் மாகாணம் தனது சொந்த கூட்டுறவு சட்டத்தை இயற்றிய முதல் மாகாணமானது.",
            "why_a_en": "Correct. Bombay Province passed the first Act in 1925.",
            "why_a_ta": "சரி. பம்பாய் மாகாணம் 1925-ல் முதல் சட்டத்தை இயற்றியது.",
            "why_b_en": "Incorrect. Madras Province enacted its Act in 1932.",
            "why_b_ta": "தவறு. மெட்ராஸ் மாகாணம் 1932-ல் இயற்றியது.",
            "why_c_en": "Incorrect. Bengal enacted its Act in 1940.",
            "why_c_ta": "தவறு. வங்காளம் 1940-ல் இயற்றியது.",
            "why_d_en": "Incorrect. Punjab did not enact the first Act.",
            "why_d_ta": "தவறு. பஞ்சாப் முதல் சட்டத்தை இயற்றவில்லை.",
            "tip_en": "Timeline of Provincial Acts: Bombay (1925) → Madras (1932) → Bengal (1940).",
            "tip_ta": "மாகாண சட்டங்கள் வரிசை: பம்பாய் (1925) → மெட்ராஸ் (1932) → வங்காளம் (1940).",
            "fact_en": "The 1925 Bombay Act introduced the principle of democratic control and one-man one-vote explicitly.",
            "fact_ta": "1925 பம்பாய் சட்டம் ஒருவருக்கு ஒரு வாக்கு என்ற ஜனநாயகக் கோட்பாட்டை வெளிப்படையாக அறிமுகப்படுத்தியது."
        },

        # 29. TNPSC Group 2 2016
        {
            "subtopic": "Madras Co-operative Societies Act 1932",
            "stem_en": "[TNPSC Group 2 2016] In which year did the Madras Legislature pass the Madras Co-operative Societies Act, replacing the Central Act of 1912 for the Madras Presidency?",
            "stem_ta": "[TNPSC குரூப் 2 2016] மெட்ராஸ் மாகாணத்திற்காக 1912-ஆம் ஆண்டின் மத்திய சட்டத்திற்குப் பதிலாக, மெட்ராஸ் சட்டமன்றம் மெட்ராஸ் கூட்டுறவு சங்கங்கள் சட்டத்தை எந்த ஆண்டு இயற்றியது?",
            "options": [
                ("1932", "1932"),
                ("1925", "1925"),
                ("1935", "1935"),
                ("1904", "1904")
            ],
            "correct_key": "A",
            "exp_en": "The Madras Co-operative Societies Act was passed in 1932 (Madras Act VI of 1932) based on the Townsend Committee recommendations.",
            "exp_ta": "டவுன்சென்ட் குழுவின் பரிந்துரைகளின் அடிப்படையில் 1932-ல் மெட்ராஸ் கூட்டுறவு சங்கங்கள் சட்டம் (Madras Act VI of 1932) இயற்றப்பட்டது.",
            "why_a_en": "Correct. Madras Act was passed in 1932.",
            "why_a_ta": "சரி. மெட்ராஸ் சட்டம் 1932-ல் இயற்றப்பட்டது.",
            "why_b_en": "Incorrect. 1925 was the Bombay Act.",
            "why_b_ta": "தவறு. 1925 பம்பாய் சட்டம்.",
            "why_c_en": "Incorrect. 1935 is Government of India Act.",
            "why_c_ta": "தவறு. 1935 இந்திய அரசுச் சட்டம்.",
            "why_d_en": "Incorrect. 1904 was the first Central Credit Act.",
            "why_d_ta": "தவறு. 1904 முதல் மத்திய கடன் சட்டம்.",
            "tip_en": "Madras Act = 1932 (Based on Townsend Committee report).",
            "tip_ta": "மெட்ராஸ் சட்டம் = 1932 (டவுன்சென்ட் குழுவின் அறிக்கை அடிப்படையில்).",
            "fact_en": "This was subsequently replaced by the 1961 Act and eventually by the Tamil Nadu Co-operative Societies Act, 1983.",
            "fact_ta": "பின்னர் இது 1961 சட்டத்தாலும், இறுதியாக தமிழ்நாடு கூட்டுறவு சங்கங்கள் சட்டம் 1983-ஆலும் மாற்றப்பட்டது."
        },

        # 30. UPSC CSE Prelims 2019
        {
            "subtopic": "Primary Agricultural Credit Societies Computerization",
            "stem_en": "[UPSC CSE 2019] Which apex agricultural financial institution serves as the national implementing agency for the project on computerization of Primary Agricultural Credit Societies (PACS)?",
            "stem_ta": "[UPSC CSE 2019] தொடக்க வேளாண்மைக் கூட்டுறவுக் கடன் சங்கங்கள் (PACS) கணினிமயமாக்கல் திட்டத்திற்கான தேசிய அமலாக்க முகமையாகச் செயல்படும் உச்ச விவசாய நிதி நிறுவனம் எது?",
            "options": [
                ("NABARD", "நபார்டு (NABARD)"),
                ("Reserve Bank of India (RBI)", "இந்திய ரிசர்வ் வங்கி (RBI)"),
                ("State Bank of India (SBI)", "பாரத ஸ்டேட் வங்கி (SBI)"),
                ("NCDC", "என்.சி.டி.சி (NCDC)")
            ],
            "correct_key": "A",
            "exp_en": "NABARD is the designated national implementing agency for the centrally sponsored PACS computerization project, linking PACS with DCCBs through cloud-based ERP software.",
            "exp_ta": "மத்திய நிதியுதவி பெறும் PACS கணினிமயமாக்கல் திட்டத்தின் தேசிய செயலாக்க முகமையாக நபார்டு (NABARD) வங்கி செயல்படுகிறது.",
            "why_a_en": "Correct. NABARD implements the PACS ERP project.",
            "why_a_ta": "சரி. நபார்டு வங்கி PACS மென்பொருள் திட்டத்தை செயல்படுத்துகிறது.",
            "why_b_en": "Incorrect. RBI is the central monetary authority.",
            "why_b_ta": "தவறு. ரிசர்வ் வங்கி மத்திய பணவியல் அதிகார அமைப்பு.",
            "why_c_en": "Incorrect. SBI is a commercial bank.",
            "why_c_ta": "தவறு. SBI ஒரு வணிக வங்கி.",
            "why_d_en": "Incorrect. NCDC finances cooperative marketing and processing infrastructure.",
            "why_d_ta": "தவறு. NCDC கூட்டுறவு கட்டமைப்புக்கு கடன் வழங்கும் அமைப்பு.",
            "tip_en": "PACS Computerization = Implemented by NABARD under Ministry of Cooperation.",
            "tip_ta": "PACS கணினிமயமாக்கல் = கூட்டுறவு அமைச்சகத்தின் கீழ் நபார்டு வங்கியால் செயல்படுத்தப்படுகிறது.",
            "fact_en": "The project covers approximately 63,000 functional PACS across all States and UTs.",
            "fact_ta": "இத்திட்டம் நாடு முழுவதும் சுமார் 63,000 தொடக்க வேளாண் கடன் சங்கங்களை உள்ளடக்கியுள்ளது."
        }
    ]


def get_pyq_questions_batch4():
    return [
        # 31. TNPSC Group 1 2018
        {
            "subtopic": "Vaidyanathan Committee 2004",
            "stem_en": "[TNPSC Group 1 2018] Which committee was appointed by the Government of India in 2004 to recommend a revival package for the Short-Term Rural Cooperative Credit Structure (STCCS)?",
            "stem_ta": "[TNPSC குரூப் 1 2018] குறுகிய கால கிராமப்புற கூட்டுறவு கடன் கட்டமைப்புக்கு (STCCS) மறுமலர்ச்சி நிதித் தொகுப்பைப் பரிந்துரைக்க 2004-ல் இந்திய அரசால் அமைக்கப்பட்ட குழு எது?",
            "options": [
                ("Prof. A. Vaidyanathan Committee", "பேராசிரியர் ஏ. வைத்தியநாதன் குழு"),
                ("Y.V. Reddy Committee", "ஒய்.வி. ரெட்டி குழு"),
                ("B. Sivaraman Committee", "பி. சிவராமன் குழு"),
                ("C. Rangarajan Committee", "சி. ரங்கராஜன் குழு")
            ],
            "correct_key": "A",
            "exp_en": "The Task Force on Revival of Rural Cooperative Credit Institutions headed by Prof. A. Vaidyanathan was set up in 2004. It recommended an ₹13,596 crore financial revival package linked to legal and regulatory reforms.",
            "exp_ta": "2004-ல் அமைக்கப்பட்ட பேராசிரியர் ஏ. வைத்தியநாதன் தலைமையிலான பணிக்குழு கிராமப்புற கூட்டுறவு கடன் அமைப்புகளுக்கு ₹13,596 கோடி மறுமலர்ச்சி தொகுப்பை சட்ட சீர்திருத்தங்களுடன் பரிந்துரைத்தது.",
            "why_a_en": "Correct. Vaidyanathan Committee formulated the STCCS revival package.",
            "why_a_ta": "சரி. வைத்தியநாதன் குழுவே STCCS மறுமலர்ச்சி நிதி தொகுப்பை உருவாக்கியது.",
            "why_b_en": "Incorrect. Y.V. Reddy was former RBI Governor.",
            "why_b_ta": "தவறு. ஒய்.வி. ரெட்டி முன்னாள் ரிசர்வ் வங்கி ஆளுநர்.",
            "why_c_en": "Incorrect. B. Sivaraman headed CRAFICARD in 1979.",
            "why_c_ta": "தவறு. சிவராமன் 1979-ல் நபார்டு குழுவிற்குத் தலைமை தாங்கினார்.",
            "why_d_en": "Incorrect. C. Rangarajan headed committees on poverty and disinvestment.",
            "why_d_ta": "தவறு. ரங்கராஜன் வறுமை மற்றும் நிதி சீர்திருத்தக் குழுக்களுக்குத் தலைமை தாங்கினார்.",
            "tip_en": "Vaidyanathan Committee (2004) = Revival Package for Short-Term Rural Cooperative Credit Structure.",
            "tip_ta": "வைத்தியநாதன் குழு (2004) = குறுகிய கால கிராமப்புற கூட்டுறவு கடன் அமைப்பிற்கான மறுமலர்ச்சி திட்டம்.",
            "fact_en": "The package required States to sign an MoU with the Centre and NABARD.",
            "fact_ta": "இத்திட்டத்தின் பலனைப் பெற மாநிலங்கள் மத்திய அரசு மற்றும் நபார்டுடன் புரிந்துணர்வு ஒப்பந்தம் செய்ய வேண்டியிருந்தது."
        },

        # 32. TNPSC Group 2 2019
        {
            "subtopic": "Offences and Penalties - Article 243ZQ",
            "stem_en": "[TNPSC Group 2 2019] Under Article 243ZQ of the Constitution, which of the following is explicitly classified as an offence punishable under State law?",
            "stem_ta": "[TNPSC குரூப் 2 2019] அரசியலமைப்பு உறுப்பு 243ZQ-ன் கீழ் பின்வருவனவற்றில் எது மாநிலச் சட்டத்தின் கீழ் தண்டனைக்குரிய குற்றமாக வெளிப்படையாக வகைப்படுத்தப்பட்டுள்ளது?",
            "options": [
                ("Wilfully making a false return or furnishing false information", "வேண்டுமென்றே தவறான அறிக்கை தாக்கல் செய்தல் அல்லது தவறான தகவல் அளித்தல்"),
                ("Borrowing money from a cooperative society", "கூட்டுறவு சங்கத்திலிருந்து கடன் பெறுதல்"),
                ("Attending an Annual General Body Meeting", "ஆண்டுப் பொதுக்குழுக் கூட்டத்தில் கலந்துகொள்ளுதல்"),
                ("Opening a savings bank account in a cooperative bank", "கூட்டுறவு வங்கியில் சேமிப்புக் கணக்கு தொடங்குதல்")
            ],
            "correct_key": "A",
            "exp_en": "Article 243ZQ(1)(a) specifies that a cooperative society or officer wilfully making a false return or furnishing false information commits an offence.",
            "exp_ta": "உறுப்பு 243ZQ(1)(a)-ன் படி ஒரு கூட்டுறவு சங்கமோ அல்லது அதன் அதிகாரியோ வேண்டுமென்றே தவறான அறிக்கையை தாக்கல் செய்வது தண்டனைக்குரிய குற்றமாகும்.",
            "why_a_en": "Correct. Wilful false return is an explicit constitutional offence under Art 243ZQ.",
            "why_a_ta": "சரி. தவறான அறிக்கை அளிப்பது உறுப்பு 243ZQ-ன் கீழ் தண்டனைக்குரிய குற்றமாகும்.",
            "why_b_en": "Incorrect. Borrowing money is a normal legitimate activity.",
            "why_b_ta": "தவறு. கடன் பெறுவது சங்கத்தின் சாதாரண உரிமையாகும்.",
            "why_c_en": "Incorrect. Attending the AGM is a member's statutory right.",
            "why_c_ta": "தவறு. பொதுக்குழுவில் பங்கேற்பது உறுப்பினரின் உரிமையாகும்.",
            "why_d_en": "Incorrect. Opening an account is normal banking.",
            "why_d_ta": "தவறு. கணக்கு தொடங்குவது இயல்பான வங்கிப் பணியாகும்.",
            "tip_en": "Article 243ZQ = Offences: False return, disobeying summons, failing to remit salary deductions, corrupt election practices.",
            "tip_ta": "உறுப்பு 243ZQ = குற்றங்கள்: தவறான அறிக்கை, அழைப்பாணையை மீறுதல், சம்பளப் பிடித்தத்தை செலுத்தத் தவறுதல், தேர்தல் முறைகேடு.",
            "fact_en": "Penalties including fines and imprisonment are enacted under respective State Acts.",
            "fact_ta": "அபராதம் மற்றும் சிறைத்தண்டனைகள் அந்தந்த மாநில கூட்டுறவு சட்டங்களால் நிர்ணயிக்கப்படுகின்றன."
        },

        # 33. TNPSC Assistant Director of Cooperatives 2019
        {
            "subtopic": "Right to Information - Article 243ZO",
            "stem_en": "[TNPSC AD of Cooperatives 2019] Which Article of the Constitution provides for the right of every member of a co-operative society to access the books, information and accounts of the society?",
            "stem_ta": "[TNPSC கூட்டுறவு உதவி இயக்குநர் 2019] கூட்டுறவு சங்கத்தின் புத்தகங்கள், தகவல்கள் மற்றும் கணக்குகளைப் பார்வையிடும் உரிமையை ஒவ்வொரு உறுப்பினருக்கும் வழங்கும் அரசியலமைப்பு உறுப்பு எது?",
            "options": [
                ("Article 243ZO", "உறுப்பு 243ZO"),
                ("Article 243ZN", "உறுப்பு 243ZN"),
                ("Article 243ZP", "உறுப்பு 243ZP"),
                ("Article 243ZM", "உறுப்பு 243ZM")
            ],
            "correct_key": "A",
            "exp_en": "Article 243ZO is titled 'Right of a member to get information' and empowers the State Legislature to make provisions facilitating member access to books and accounts.",
            "exp_ta": "உறுப்பு 243ZO 'தகவல் பெறும் உறுப்பினரின் உரிமை' என்ற தலைப்பில் உறுப்பினர்கள் சங்கத்தின் புத்தகங்கள் மற்றும் கணக்குகளைப் பார்வையிட வழிவகை செய்கிறது.",
            "why_a_en": "Correct. Article 243ZO grants right to information for members.",
            "why_a_ta": "சரி. உறுப்பு 243ZO உறுப்பினர்களுக்கு தகவல் பெறும் உரிமையை வழங்குகிறது.",
            "why_b_en": "Incorrect. Article 243ZN deals with convening General Body meetings.",
            "why_b_ta": "தவறு. உறுப்பு 243ZN பொதுக்குழுவைக் கூட்டுவது பற்றியது.",
            "why_c_en": "Incorrect. Article 243ZP deals with filing of returns.",
            "why_c_ta": "தவறு. உறுப்பு 243ZP வருடாந்திர அறிக்கை தாக்கல் பற்றியது.",
            "why_d_en": "Incorrect. Article 243ZM deals with audit of accounts.",
            "why_d_ta": "தவறு. உறுப்பு 243ZM கணக்குத் தணிக்கை பற்றியது.",
            "tip_en": "Sequence mnemonic: ZM = Audit; ZN = Meeting; ZO = Observation (Information); ZP = Paperwork (Returns); ZQ = Questionable acts (Offences).",
            "tip_ta": "வரிசை நினைவுக்குறிப்பு: ZM = தணிக்கை; ZN = கூட்டம் (AGM); ZO = தகவல் பெறும் உரிமை; ZP = அறிக்கை தாக்கல்; ZQ = குற்றங்கள்.",
            "fact_en": "Member education is also mandated under Article 243ZO(2).",
            "fact_ta": "உறுப்பினர்களுக்கான கூட்டுறவு கல்வி மற்றும் பயிற்சியும் உறுப்பு 243ZO(2)-ன் கீழ் கட்டாயமாக்கப்பட்டுள்ளது."
        },

        # 34. TNPSC Group 1 2012
        {
            "subtopic": "National Policy on Cooperatives 2002",
            "stem_en": "[TNPSC Group 1 2012] In which year was the first National Policy on Co-operatives announced by the Government of India?",
            "stem_ta": "[TNPSC குரூப் 1 2012] இந்திய அரசால் கூட்டுறவுக்கான முதல் தேசியக் கொள்கை எந்த ஆண்டு அறிவிக்கப்பட்டது?",
            "options": [
                ("2002", "2002"),
                ("1991", "1991"),
                ("2011", "2011"),
                ("1985", "1985")
            ],
            "correct_key": "A",
            "exp_en": "The Government of India formulated and announced the first National Policy on Co-operatives in March 2002 to facilitate all-round development of cooperatives as self-reliant and democratic institutions.",
            "exp_ta": "கூட்டுறவு அமைப்புகளைத் தற்சார்பு மற்றும் ஜனநாயக நிறுவனங்களாக வளர்த்தெடுப்பதற்காக மார்ச் 2002-ல் முதல் தேசிய கூட்டுறவுக் கொள்கையை இந்திய அரசு வெளியிட்டது.",
            "why_a_en": "Correct. 2002 was the year of the first National Cooperative Policy.",
            "why_a_ta": "சரி. 2002 முதல் தேசிய கூட்டுறவுக் கொள்கை வெளியான ஆண்டாகும்.",
            "why_b_en": "Incorrect. 1991 was the year of the Brahm Perkash Committee report.",
            "why_b_ta": "தவறு. 1991 பிரம்ம பிரகாஷ் குழுவின் அறிக்கை வெளியான ஆண்டு.",
            "why_c_en": "Incorrect. 2011 was the year of the 97th Constitutional Amendment.",
            "why_c_ta": "தவறு. 2011 97வது அரசியலமைப்புத் திருத்தம் இயற்றப்பட்ட ஆண்டு.",
            "why_d_en": "Incorrect. 1985 is incorrect.",
            "why_d_ta": "தவறு. 1985 தவறான ஆண்டு.",
            "tip_en": "Policy Milestones: 1st National Policy = 2002; Suresh Prabhu Committee for New Policy = 2022.",
            "tip_ta": "கொள்கை மைல்கற்கள்: முதல் தேசியக் கொள்கை = 2002; புதிய கொள்கைக்கான சுரேஷ் பிரபு குழு = 2022.",
            "fact_en": "The 2002 policy served as the blueprint for reforming Multi-State Cooperative legislation.",
            "fact_ta": "2002 கொள்கையே பல மாநில கூட்டுறவு சட்ட சீர்திருத்தத்திற்கான வரைபடமாக விளங்கியது."
        },

        # 35. TNPSC Group 2 2018
        {
            "subtopic": "Cooperative Principles - Democratic Control",
            "stem_en": "[TNPSC Group 2 2018] Which principle fundamentally distinguishes a Co-operative Society from a Joint Stock Commercial Company?",
            "stem_ta": "[TNPSC குரூப் 2 2018] கூட்டுறவு சங்கத்தை ஒரு வணிக பங்கு நிறுவனத்திலிருந்து (Joint Stock Company) அடிப்படையில் வேறுபடுத்தும் முக்கியக் கோட்பாடு எது?",
            "options": [
                ("'One Member, One Vote' democratic principle", "'ஒரு உறுப்பினர், ஒரு வாக்கு' என்ற ஜனநாயகக் கோட்பாடு"),
                ("'One Share, One Vote' capital principle", "'ஒரு பங்கு, ஒரு வாக்கு' என்ற மூலதனக் கோட்பாடு"),
                ("Maximization of profit for shareholders", "பங்குதாரர்களுக்கு அதிகபட்ச லாபம் ஈட்டுதல்"),
                ("Limited liability of shareholders", "பங்குதாரர்களின் வரையறுக்கப்பட்ட பொறுப்பு")
            ],
            "correct_key": "A",
            "exp_en": "Cooperative societies operate on the democratic principle of 'One Member, One Vote' regardless of the number of shares held, whereas commercial companies operate on 'One Share, One Vote' where capital dominates.",
            "exp_ta": "கூட்டுறவு சங்கங்கள் எத்தனை பங்குகள் வைத்திருந்தாலும் 'ஒருவருக்கு ஒரு வாக்கு' என்ற ஜனநாயகக் கோட்பாட்டில் இயங்குகின்றன; வணிக நிறுவனங்களோ மூலதனத்தின் அடிப்படையில் 'ஒரு பங்கு, ஒரு வாக்கு' என இயங்குகின்றன.",
            "why_a_en": "Correct. Democratic control ('one member, one vote') is the hallmark of cooperatives.",
            "why_a_ta": "சரி. 'ஒரு உறுப்பினர், ஒரு வாக்கு' என்ற ஜனநாயகக் கட்டுப்பாடே கூட்டுறவின் முக்கிய அடையாளமாகும்.",
            "why_b_en": "Incorrect. 'One Share, One Vote' applies to capitalist companies.",
            "why_b_ta": "தவறு. 'ஒரு பங்கு, ஒரு வாக்கு' என்பது தனியார் நிறுவனங்களின் விதி.",
            "why_c_en": "Incorrect. Profit maximization is the motive of companies, not cooperatives.",
            "why_c_ta": "தவறு. லாப நோக்கம் நிறுவனங்களின் குறிக்கோள், கூட்டுறவின் குறிக்கோள் சேவை.",
            "why_d_en": "Incorrect. Limited liability can exist in both.",
            "why_d_ta": "தவறு. வரையறுக்கப்பட்ட பொறுப்பு இரண்டிலும் இருக்கலாம்.",
            "tip_en": "Core Difference: Company = Capital-controlled ('One Share, One Vote'); Cooperative = Human-controlled ('One Member, One Vote').",
            "tip_ta": "அடிப்படை வேறுபாடு: நிறுவனம் = மூலதனக் கட்டுப்பாடு (ஒரு பங்கு ஒரு வாக்கு); கூட்டுறவு = மனிதக் கட்டுப்பாடு (ஒரு உறுப்பினர் ஒரு வாக்கு).",
            "fact_en": "This principle originated with the Rochdale Society of Equitable Pioneers in England in 1844.",
            "fact_ta": "இக்கோட்பாடு 1844-ல் இங்கிலாந்தின் ரோச்டேல் முன்னோடிகளால் உருவாக்கப்பட்டது."
        },

        # 36. TNPSC Group 4 2015
        {
            "subtopic": "IFFCO and Fertilizer Cooperatives",
            "stem_en": "[TNPSC Group 4 2015] In which year was the Indian Farmers Fertiliser Cooperative Limited (IFFCO) registered?",
            "stem_ta": "[TNPSC குரூப் 4 2015] இந்திய விவசாயிகள் உரக் கூட்டுறவு நிறுவனம் (IFFCO) எந்த ஆண்டு பதிவு செய்யப்பட்டது?",
            "options": [
                ("1967", "1967"),
                ("1958", "1958"),
                ("1980", "1980"),
                ("1971", "1971")
            ],
            "correct_key": "A",
            "exp_en": "IFFCO was registered on 3 November 1967 as a multi-unit cooperative society with the primary objective of manufacturing and distributing quality chemical fertilizers to farmers.",
            "exp_ta": "விவசாயிகளுக்குத் தரமான உரங்களை உற்பத்தி செய்து வழங்குவதற்காக 1967 நவம்பர் 3 அன்று இஃப்கோ (IFFCO) பல மாநில கூட்டுறவு சங்கமாகப் பதிவு செய்யப்பட்டது.",
            "why_a_en": "Correct. IFFCO was founded in 1967.",
            "why_a_ta": "சரி. இஃப்கோ 1967-ல் நிறுவப்பட்டது.",
            "why_b_en": "Incorrect. 1958 was the year NAFED was founded.",
            "why_b_ta": "தவறு. 1958-ல் NAFED நிறுவப்பட்டது.",
            "why_c_en": "Incorrect. 1980 was the year KRIBHCO was founded.",
            "why_c_ta": "தவறு. 1980-ல் கிரிப்கோ (KRIBHCO) நிறுவப்பட்டது.",
            "why_d_en": "Incorrect. 1971 is incorrect.",
            "why_d_ta": "தவறு. 1971 தவறான ஆண்டு.",
            "tip_en": "Major Cooperative Federations: NAFED = 1958; IFFCO = 1967; KRIBHCO = 1980.",
            "tip_ta": "முக்கிய தேசிய கூட்டுறவுகள்: NAFED = 1958; IFFCO = 1967; KRIBHCO = 1980.",
            "fact_en": "IFFCO is today the largest fertilizer cooperative in the world with over 35,000 member cooperatives.",
            "fact_ta": "இஃப்கோ இன்று 35,000-க்கும் மேற்பட்ட கூட்டுறவு சங்கங்களை உறுப்பினர்களாகக் கொண்டு உலகின் மிகப்பெரிய உரக் கூட்டுறவாக உள்ளது."
        },

        # 37. TNPSC Group 1 2016
        {
            "subtopic": "Agricultural Marketing Cooperatives - NAFED",
            "stem_en": "[TNPSC Group 1 2016] On which historic national date was the National Agricultural Cooperative Marketing Federation of India (NAFED) established?",
            "stem_ta": "[TNPSC குரூப் 1 2016] இந்திய தேசிய வேளாண்மை கூட்டுறவு சந்தைப்படுத்தல் கூட்டமைப்பு (NAFED) எந்த வரலாற்றுச் சிறப்புமிக்க தேசிய நாளில் நிறுவப்பட்டது?",
            "options": [
                ("2nd October 1958 (Gandhi Jayanti)", "1958 அக்டோபர் 2 (காந்தி ஜெயந்தி)"),
                ("15th August 1947 (Independence Day)", "1947 ஆகஸ்ட் 15 (சுதந்திர தினம்)"),
                ("26th January 1950 (Republic Day)", "1950 ஜனவரி 26 (குடியரசு தினம்)"),
                ("14th November 1956 (Children's Day)", "1956 நவம்பர் 14 (குழந்தைகள் தினம்)")
            ],
            "correct_key": "A",
            "exp_en": "NAFED was set up on Gandhi Jayanti, 2nd October 1958 under the Multi-State Co-operative Societies Act to promote cooperative marketing of agricultural produce.",
            "exp_ta": "விவசாய விளைபொருட்களைச் சந்தைப்படுத்துவதை ஊக்குவிப்பதற்காக 1958 அக்டோபர் 2 காந்தி ஜெயந்தி அன்று NAFED நிறுவப்பட்டது.",
            "why_a_en": "Correct. NAFED was founded on 2 October 1958.",
            "why_a_ta": "சரி. NAFED 1958 அக்டோபர் 2-ல் நிறுவப்பட்டது.",
            "why_b_en": "Incorrect. 15 August 1947 is Independence Day.",
            "why_b_ta": "தவறு. 1947 ஆகஸ்ட் 15 சுதந்திர தினம்.",
            "why_c_en": "Incorrect. 26 January 1950 is Republic Day.",
            "why_c_ta": "தவறு. 1950 ஜனவரி 26 குடியரசு தினம்.",
            "why_d_en": "Incorrect. 14 November is Children's Day.",
            "why_d_ta": "தவறு. 14 நவம்பர் குழந்தைகள் தினம்.",
            "tip_en": "NAFED established on Gandhi Jayanti: 2 October 1958.",
            "tip_ta": "NAFED காந்தி ஜெயந்தி அன்று தொடங்கப்பட்டது: 2 அக்டோபர் 1958.",
            "fact_en": "NAFED acts as the primary agency for the Price Support Scheme (PSS) of the Central Government.",
            "fact_ta": "மத்திய அரசின் விலை ஆதரவுத் திட்டத்தின் (PSS) முதன்மை முகமையாக NAFED செயல்படுகிறது."
        },

        # 38. TNPSC Group 2 2015
        {
            "subtopic": "Montagu-Chelmsford Reforms 1919",
            "stem_en": "[TNPSC Group 2 2015] Under the dyarchical system introduced by the Government of India Act, 1919, in which category of subjects was 'Co-operation' placed?",
            "stem_ta": "[TNPSC குரூப் 2 2015] இந்திய அரசுச் சட்டம் 1919 அறிமுகப்படுத்திய இரட்டை ஆட்சி முறையில் 'கூட்டுறவு' எந்த வகைத் துறைகளில் வைக்கப்பட்டது?",
            "options": [
                ("Transferred Subject", "மாற்றப்பட்ட துறை"),
                ("Reserved Subject", "ஒதுக்கப்பட்ட துறை"),
                ("Federal Subject", "கூட்டாட்சித் துறை"),
                ("Concurrent Subject", "பொதுத்துறை")
            ],
            "correct_key": "A",
            "exp_en": "Under the 1919 Montagu-Chelmsford Reforms, provincial subjects were divided into 'Reserved' (kept with British Governor) and 'Transferred' (given to elected Indian Ministers). Co-operation was made a 'Transferred Subject'.",
            "exp_ta": "1919 மாண்டேகு-செம்ஸ்போர்டு சீர்திருத்தங்களில் மாகாணத் துறைகள் 'ஒதுக்கப்பட்டவை' மற்றும் 'மாற்றப்பட்டவை' எனப் பிரிக்கப்பட்டன. கூட்டுறவு தேர்ந்தெடுக்கப்பட்ட இந்திய அமைச்சர்களின் கீழ் உள்ள 'மாற்றப்பட்ட துறையாக' வைக்கப்பட்டது.",
            "why_a_en": "Correct. Co-operation was a Transferred Subject under Dyarchy.",
            "why_a_ta": "சரி. இரட்டை ஆட்சியில் கூட்டுறவு மாற்றப்பட்ட துறையாக இருந்தது.",
            "why_b_en": "Incorrect. Reserved subjects included law & order, finance, land revenue, police.",
            "why_b_ta": "தவறு. சட்டம்-ஒழுங்கு, நிதி போன்றவை ஒதுக்கப்பட்ட துறைகள்.",
            "why_c_en": "Incorrect. Federal subjects were at the central level.",
            "why_c_ta": "தவறு. கூட்டாட்சித் துறைகள் மத்திய அளவிலானவை.",
            "why_d_en": "Incorrect. Concurrent category was introduced in 1935.",
            "why_d_ta": "தவறு. பொதுப் பட்டியல் 1935-ல் அறிமுகமானது.",
            "tip_en": "1919 Dyarchy: Co-operation = Transferred Subject (Administered by Indian Ministers responsible to Provincial Legislature).",
            "tip_ta": "1919 இரட்டை ஆட்சி: கூட்டுறவு = மாற்றப்பட்ட துறை (மாகாண சட்டமன்றத்திற்குப் பொறுப்பான இந்திய அமைச்சர்களால் நிர்வகிக்கப்பட்டது).",
            "fact_en": "This devolution directly enabled provinces like Bombay and Madras to craft distinct cooperative laws.",
            "fact_ta": "இந்த அதிகார மாற்றமே பம்பாய், மெட்ராஸ் போன்ற மாகாணங்கள் சொந்த கூட்டுறவு சட்டங்களை இயற்ற வழிசெய்தது."
        },

        # 39. TNPSC Group 4 2016
        {
            "subtopic": "Primary Weavers Societies and Free Schemes",
            "stem_en": "[TNPSC Group 4 2016] Through which cooperative institutions does the Tamil Nadu Government primarily implement its Free Dhoti and Saree Scheme for Pongal?",
            "stem_ta": "[TNPSC குரூப் 4 2016] பொங்கல் பண்டிகைக்கான இலவச வேட்டி மற்றும் சேலை வழங்கும் திட்டத்தை தமிழ்நாடு அரசு பிரதானமாக எந்தக் கூட்டுறவு அமைப்புகள் மூலம் செயல்படுத்துகிறது?",
            "options": [
                ("Primary Handloom and Powerloom Weavers' Co-operative Societies", "தொடக்க கைத்தறி மற்றும் விசைத்தறி நெசவாளர் கூட்டுறவு சங்கங்கள்"),
                ("Primary Agricultural Credit Societies (PACS)", "தொடக்க வேளாண்மைக் கூட்டுறவுக் கடன் சங்கங்கள்"),
                ("Urban Co-operative Banks", "நகர்ப்புறக் கூட்டுறவு வங்கிகள்"),
                ("Co-operative Housing Societies", "கூட்டுறவு வீட்டுவசதிச் சங்கங்கள்")
            ],
            "correct_key": "A",
            "exp_en": "The Free Dhoti and Saree Scheme (introduced by former CM M.G. Ramachandran in 1983) is produced entirely through Primary Handloom and Powerloom Weavers Cooperative Societies in Tamil Nadu, providing continuous employment to thousands of weavers.",
            "exp_ta": "1983-ல் எம்.ஜி.ஆரால் தொடங்கப்பட்ட பொங்கல் இலவச வேட்டி-சேலை திட்டம் முழுமையாக தொடக்க கைத்தறி மற்றும் விசைத்தறி நெசவாளர் கூட்டுறவு சங்கங்கள் மூலமே உற்பத்தி செய்யப்பட்டு விநியோகிக்கப்படுகிறது.",
            "why_a_en": "Correct. Weavers' cooperatives execute the Free Dhoti and Saree scheme.",
            "why_a_ta": "சரி. நெசவாளர் கூட்டுறவு சங்கங்களே இலவச வேட்டி-சேலை திட்டத்தை நிறைவேற்றுகின்றன.",
            "why_b_en": "Incorrect. PACS handle agricultural credit and PDS distribution.",
            "why_b_ta": "தவறு. PACS விவசாயக் கடன் மற்றும் ரேஷன் கடைகளைக் கவனிக்கிறது.",
            "why_c_en": "Incorrect. UCBs handle banking operations.",
            "why_c_ta": "தவறு. UCBs வங்கிப் பணிகளைக் கவனிக்கிறது.",
            "why_d_en": "Incorrect. Housing societies handle shelter loans.",
            "why_d_ta": "தவறு. வீட்டுவசதி சங்கங்கள் வீட்டுக் கடன் வழங்குகின்றன.",
            "tip_en": "Tamil Nadu Welfare Schemes: Free Uniform Scheme + Free Dhoti and Saree Scheme = Implemented through Weavers' Cooperatives.",
            "tip_ta": "தமிழக நலத்திட்டங்கள்: இலவச சீருடை மற்றும் இலவச வேட்டி-சேலை திட்டம் = நெசவாளர் கூட்டுறவு மூலம் செயல்படுத்தப்படுகிறது.",
            "fact_en": "This scheme was launched in 1983 to provide year-round employment to handloom and powerloom weavers.",
            "fact_ta": "நெசவாளர்களுக்கு ஆண்டு முழுவதும் தொடர் வேலைவாய்ப்பு வழங்குவதற்காக 1983-ல் இத்திட்டம் தொடங்கப்பட்டது."
        },

        # 40. TNPSC Group 1 2022
        {
            "subtopic": "Ministry of Cooperation Creation",
            "stem_en": "[TNPSC Group 1 2022] On which date did the Government of India officially create the separate 'Ministry of Cooperation' to deepen the cooperative movement?",
            "stem_ta": "[TNPSC குரூப் 1 2022] கூட்டுறவு இயக்கத்தை வலுப்படுத்துவதற்காக இந்திய அரசால் அதிகாரப்பூர்வமாக தனி 'கூட்டுறவு அமைச்சகம்' எந்த நாளில் உருவாக்கப்பட்டது?",
            "options": [
                ("6th July 2021", "2021 ஜூலை 6"),
                ("15th August 2021", "2021 ஆகஸ்ட் 15"),
                ("26th January 2022", "2022 ஜனவரி 26"),
                ("15th February 2021", "2021 பிப்ரவரி 15")
            ],
            "correct_key": "A",
            "exp_en": "The Ministry of Cooperation was carved out of the Ministry of Agriculture and Farmers Welfare on 6 July 2021 by amending the Government of India (Allocation of Business) Rules, 1961.",
            "exp_ta": "மத்திய அரசின் வணிக ஒதுக்கீட்டு விதிகளைத் திருத்தி, 2021 ஜூலை 6 அன்று வேளாண் அமைச்சகத்திலிருந்து பிரிக்கப்பட்டு தனி கூட்டுறவு அமைச்சகம் உருவாக்கப்பட்டது.",
            "why_a_en": "Correct. 6 July 2021 is the official notification date.",
            "why_a_ta": "சரி. 2021 ஜூலை 6 அதிகாரப்பூர்வமாக உருவாக்கப்பட்ட நாளாகும்.",
            "why_b_en": "Incorrect. 15 August 2021 was Independence Day.",
            "why_b_ta": "தவறு. 15 ஆகஸ்ட் 2021 சுதந்திர தினம்.",
            "why_c_en": "Incorrect. 26 January 2022 was Republic Day.",
            "why_c_ta": "தவறு. 26 ஜனவரி 2022 குடியரசு தினம்.",
            "why_d_en": "Incorrect. 15 February 2021 is incorrect.",
            "why_d_ta": "தவறு. 15 பிப்ரவரி 2021 தவறான நாள்.",
            "tip_en": "Ministry of Cooperation: Created on 6 July 2021; First Minister = Amit Shah; Vision = 'Sahakar se Samriddhi'.",
            "tip_ta": "கூட்டுறவு அமைச்சகம்: உருவான நாள் 6 ஜூலை 2021; முதல் அமைச்சர் = அமித் ஷா; குறிக்கோள் = 'சககார் சே சம்ரித்தி'.",
            "fact_en": "The announcement was made just ahead of the Union Cabinet reshuffle in July 2021.",
            "fact_ta": "ஜூலை 2021 மத்திய அமைச்சரவை மாற்றியமைக்கப்படுவதற்கு சற்று முன்பு இந்த அறிவிப்பு வெளியானது."
        }
    ]


def get_pyq_questions_batch5():
    return [
        # 41. TNPSC Group 2 2018
        {
            "subtopic": "National Cooperative Union of India (NCUI)",
            "stem_en": "[TNPSC Group 2 2018] In which year was the National Cooperative Union of India (NCUI), the apex non-official promotional organization of the Indian cooperative movement, originally established as the All India Co-operative Institutes Association?",
            "stem_ta": "[TNPSC குரூப் 2 2018] இந்திய கூட்டுறவு இயக்கத்தின் அரசு சாரா உச்ச அமைப்பான இந்திய தேசிய கூட்டுறவு ஒன்றியம் (NCUI), அகில இந்திய கூட்டுறவு நிறுவனங்களின் சங்கமாக முதலில் எந்த ஆண்டு நிறுவப்பட்டது?",
            "options": [
                ("1929", "1929"),
                ("1947", "1947"),
                ("1904", "1904"),
                ("1954", "1954")
            ],
            "correct_key": "A",
            "exp_en": "NCUI was originally established on 1 October 1929 as the All India Co-operative Institutes Association and was re-designated as the National Cooperative Union of India in 1961.",
            "exp_ta": "NCUI முதலில் 1929 அக்டோபர் 1 அன்று அகில இந்திய கூட்டுறவு நிறுவனங்களின் சங்கமாக நிறுவப்பட்டு, பின்னர் 1961-ல் இந்திய தேசிய கூட்டுறவு ஒன்றியம் எனப் பெயர் மாற்றப்பட்டது.",
            "why_a_en": "Correct. NCUI traces its roots to 1929.",
            "why_a_ta": "சரி. NCUI 1929-ல் தன் பயணத்தைத் தொடங்கியது.",
            "why_b_en": "Incorrect. 1947 was Independence.",
            "why_b_ta": "தவறு. 1947 சுதந்திர ஆண்டு.",
            "why_c_en": "Incorrect. 1904 was the first Credit Societies Act.",
            "why_c_ta": "தவறு. 1904 முதல் கடன் சங்கங்கள் சட்டம்.",
            "why_d_en": "Incorrect. 1954 was the Gorwala Committee report.",
            "why_d_ta": "தவறு. 1954 கோர்வாலா குழு அறிக்கை.",
            "tip_en": "NCUI: Established in 1929; Headquarters = New Delhi; Represents all sectors of Indian cooperatives.",
            "tip_ta": "NCUI: 1929-ல் நிறுவப்பட்டது; தலைமையகம் = புது தில்லி; அனைத்து கூட்டுறவு துறைகளையும் பிரதிநிதித்துவப்படுத்துகிறது.",
            "fact_en": "NCUI publishes the prestigious cooperative journal 'The Cooperator'.",
            "fact_ta": "NCUI 'தி கோஆப்பரேட்டர்' என்ற புகழ்பெற்ற இதழை வெளியிட்டு வருகிறது."
        },

        # 42. TNPSC Group 1 2014
        {
            "subtopic": "Deposit Insurance for Cooperative Banks",
            "stem_en": "[TNPSC Group 1 2014] What is the current maximum deposit insurance cover provided by the Deposit Insurance and Credit Guarantee Corporation (DICGC) per depositor in an insured cooperative bank?",
            "stem_ta": "[TNPSC குரூப் 1 2014] காப்பீடு செய்யப்பட்ட ஒரு கூட்டுறவு வங்கியில் ஒரு வைப்புத்தொகையாளருக்கு வைப்புத்தொகை காப்பீடு மற்றும் கடன் உத்தரவாதக் கழகத்தால் (DICGC) வழங்கப்படும் தற்போதைய அதிகபட்ச காப்பீட்டு வரம்பு என்ன?",
            "options": [
                ("₹5 lakh", "₹5 லட்சம்"),
                ("₹1 lakh", "₹1 லட்சம்"),
                ("₹10 lakh", "₹10 லட்சம்"),
                ("₹2 lakh", "₹2 லட்சம்")
            ],
            "correct_key": "A",
            "exp_en": "The deposit insurance limit was enhanced from ₹1 lakh to ₹5 lakh per depositor per insured bank with effect from 4 February 2020 by the Central Government.",
            "exp_ta": "மத்திய அரசால் 2020 பிப்ரவரி 4 முதல் வைப்புத்தொகை காப்பீட்டு உச்சவரம்பு ₹1 லட்சத்திலிருந்து ₹5 லட்சமாக உயர்த்தப்பட்டது.",
            "why_a_en": "Correct. ₹5 lakh is the current limit under DICGC Act.",
            "why_a_ta": "சரி. தற்போதைய DICGC வரம்பு ₹5 லட்சம் ஆகும்.",
            "why_b_en": "Incorrect. ₹1 lakh was the older limit from 1993 to 2020.",
            "why_b_ta": "தவறு. ₹1 லட்சம் என்பது 1993 முதல் 2020 வரை இருந்த பழைய வரம்பு.",
            "why_c_en": "Incorrect. ₹10 lakh is not the limit.",
            "why_c_ta": "தவறு. ₹10 லட்சம் என்பது தவறானது.",
            "why_d_en": "Incorrect. ₹2 lakh is not the limit.",
            "why_d_ta": "தவறு. ₹2 லட்சம் என்பது தவறானது.",
            "tip_en": "DICGC Cover: Increased from ₹1 lakh to ₹5 lakh on 4 Feb 2020. Covers eligible Urban and District/State Cooperative Banks.",
            "tip_ta": "DICGC காப்பீடு: 4 பிப் 2020 முதல் ₹5 லட்சமாக உயர்த்தப்பட்டது. இது தகுதியுடைய கூட்டுறவு வங்கிகளுக்குப் பொருந்தும்.",
            "fact_en": "PACS are not banks and hence are NOT covered by DICGC insurance.",
            "fact_ta": "PACS வங்கிகள் அல்ல என்பதால் அவற்றுக்கு DICGC காப்பீடு கிடைக்காது."
        },

        # 43. TNPSC Assistant Director of Cooperatives 2021
        {
            "subtopic": "Multi-State Co-operative Societies Amendment 2023",
            "stem_en": "[TNPSC AD of Cooperatives 2021] Under the Multi-State Co-operative Societies (Amendment) Act, 2023, which authority is established to conduct and superintend elections to multi-state co-operative societies?",
            "stem_ta": "[TNPSC கூட்டுறவு உதவி இயக்குநர் 2021] பல மாநில கூட்டுறவு சங்கங்கள் (திருத்தச்) சட்டம் 2023-ன் கீழ், பல மாநில கூட்டுறவு சங்கங்களின் தேர்தல்களை நடத்தவும் கண்காணிக்கவும் எந்த அதிகார அமைப்பு உருவாக்கப்பட்டுள்ளது?",
            "options": [
                ("Co-operative Election Authority", "கூட்டுறவு தேர்தல் ஆணையம் (Co-operative Election Authority)"),
                ("Election Commission of India", "இந்தியத் தேர்தல் ஆணையம்"),
                ("State Election Commission", "மாநிலத் தேர்தல் ஆணையம்"),
                ("Central Registrar of Co-operative Societies", "மத்திய கூட்டுறவு சங்கங்களின் பதிவாளர்")
            ],
            "correct_key": "A",
            "exp_en": "Section 45 of the Multi-State Co-operative Societies (Amendment) Act, 2023 inserted provisions establishing the 'Co-operative Election Authority' consisting of a Chairperson, Vice-Chairperson, and up to three members appointed by the Central Government.",
            "exp_ta": "2023 திருத்தச் சட்டத்தின் பிரிவு 45, மத்திய அரசால் நியமிக்கப்படும் தலைவர் மற்றும் உறுப்பினர்களைக் கொண்ட 'கூட்டுறவு தேர்தல் ஆணையத்தை' (Co-operative Election Authority) உருவாக்கியுள்ளது.",
            "why_a_en": "Correct. Co-operative Election Authority is the statutory body created under the 2023 Amendment.",
            "why_a_ta": "சரி. 2023 திருத்தச் சட்டம் கூட்டுறவு தேர்தல் ஆணையத்தை உருவாக்கியுள்ளது.",
            "why_b_en": "Incorrect. ECI conducts Lok Sabha and Assembly elections.",
            "why_b_ta": "தவறு. ECI நாடாளுமன்ற மற்றும் சட்டமன்றத் தேர்தல்களை நடத்துகிறது.",
            "why_c_en": "Incorrect. State Election Commission conducts local body elections.",
            "why_c_ta": "தவறு. மாநிலத் தேர்தல் ஆணையம் உள்ளாட்சித் தேர்தல்களை நடத்துகிறது.",
            "why_d_en": "Incorrect. The CRCS exercises regulatory and administrative powers, while the Authority conducts elections.",
            "why_d_ta": "தவறு. CRCS பதிவாளர் ஆவார், தேர்தலை இந்த ஆணையம் நடத்துகிறது.",
            "tip_en": "2023 MSCS Reforms: Co-operative Election Authority + Co-operative Ombudsman + 1% Net Profit contribution to Rehabilitation Fund.",
            "tip_ta": "2023 பல மாநில கூட்டுறவு சீர்திருத்தங்கள்: கூட்டுறவு தேர்தல் ஆணையம் + குறைதீர்ப்பாளர் + மறுவாழ்வு நிதிக்கு 1% லாபப் பங்களிப்பு.",
            "fact_en": "This reform eliminates the earlier practice where incumbent boards appointed their own returning officers.",
            "fact_ta": "பதவியில் உள்ள வாரியமே தனக்கு வேண்டிய தேர்தல் அதிகாரியை நியமிக்கும் பழைய முறையை இது ஒழித்துள்ளது."
        },

        # 44. TNPSC Group 1 2019
        {
            "subtopic": "Panchayats vs Municipalities vs Cooperatives Amendments",
            "stem_en": "[TNPSC Group 1 2019] Match the local and grassroots democratic bodies with their constitutional parts inserted by amendments:\nPanchayats, Municipalities, and Co-operative Societies correspond respectively to which Parts of the Constitution?",
            "stem_ta": "[TNPSC குரூப் 1 2019] பஞ்சாயத்துகள், நகராட்சிகள் மற்றும் கூட்டுறவு சங்கங்கள் முறையே இந்திய அரசியலமைப்பின் எந்தப் பகுதிகளில் சேர்க்கப்பட்டுள்ளன?",
            "options": [
                ("Part IX, Part IX-A, and Part IX-B", "பகுதி IX, பகுதி IX-A, மற்றும் பகுதி IX-B"),
                ("Part IX, Part X, and Part XI", "பகுதி IX, பகுதி X, மற்றும் பகுதி XI"),
                ("Part VIII, Part IX, and Part IX-A", "பகுதி VIII, பகுதி IX, மற்றும் பகுதி IX-A"),
                ("Part IX-A, Part IX-B, and Part IX-C", "பகுதி IX-A, பகுதி IX-B, மற்றும் பகுதி IX-C")
            ],
            "correct_key": "A",
            "exp_en": "Part IX (Panchayats, Arts 243-243O) by 73rd CAA 1992; Part IX-A (Municipalities, Arts 243P-243ZG) by 74th CAA 1992; Part IX-B (Co-operative Societies, Arts 243ZH-243ZT) by 97th CAA 2011.",
            "exp_ta": "பகுதி IX (பஞ்சாயத்துகள்) 73வது திருத்தம்; பகுதி IX-A (நகராட்சிகள்) 74வது திருத்தம்; பகுதி IX-B (கூட்டுறவு சங்கங்கள்) 97வது திருத்தம்.",
            "why_a_en": "Correct. Part IX = Panchayats, Part IX-A = Municipalities, Part IX-B = Cooperatives.",
            "why_a_ta": "சரி. பகுதி IX = பஞ்சாயத்துகள், பகுதி IX-A = நகராட்சிகள், பகுதி IX-B = கூட்டுறவு சங்கங்கள்.",
            "why_b_en": "Incorrect. Part X covers Scheduled Areas; Part XI covers Centre-State Relations.",
            "why_b_ta": "தவறு. பகுதி X பழங்குடியினர் பகுதிகள்; பகுதி XI மத்திய-மாநில உறவுகள்.",
            "why_c_en": "Incorrect. Part VIII covers Union Territories.",
            "why_c_ta": "தவறு. பகுதி VIII யூனியன் பிரதேசங்கள்.",
            "why_d_en": "Incorrect. There is no Part IX-C in the Constitution.",
            "why_d_ta": "தவறு. அரசமைப்பில் பகுதி IX-C என்று எதுவும் இல்லை.",
            "tip_en": "Grassroots Democracy Trilogy: Part IX (Rural) → Part IX-A (Urban) → Part IX-B (Economic/Cooperative).",
            "tip_ta": "அடிமட்ட ஜனநாயக மும்மூர்த்திகள்: பகுதி IX (கிராமம்) → பகுதி IX-A (நகரம்) → பகுதி IX-B (பொருளாதாரம்/கூட்டுறவு).",
            "fact_en": "All three parts were inserted to strengthen decentralized democratic participation.",
            "fact_ta": "அதிகாரப் பரவலாக்கல் மற்றும் ஜனநாயகப் பங்கேற்பை வலுப்படுத்தவே இம்மூன்று பகுதிகளும் சேர்க்கப்பட்டன."
        },

        # 45. TNPSC Group 2 2012
        {
            "subtopic": "Producer Companies under Companies Act",
            "stem_en": "[TNPSC Group 2 2012] On the recommendations of which committee were provisions for 'Producer Companies' incorporated into the Companies Act?",
            "stem_ta": "[TNPSC குரூப் 2 2012] எந்தக் குழுவின் பரிந்துரைகளின் பேரில் 'உழவர் உற்பத்தியாளர் நிறுவனங்கள்' (Producer Companies) தொடர்பான விதிகள் நிறுவனங்கள் சட்டத்தில் சேர்க்கப்பட்டன?",
            "options": [
                ("Dr. Y.K. Alagh Committee", "டாக்டர் ஓய்.கே. அலாக் குழு"),
                ("Dr. M.S. Swaminathan Committee", "டாக்டர் எம்.எஸ். சுவாமிநாதன் குழு"),
                ("Dr. C. Rangarajan Committee", "டாக்டர் சி. ரங்கராஜன் குழு"),
                ("Dr. B.S. Minhas Committee", "டாக்டர் பி.எஸ். மின்ஹாஸ் குழு")
            ],
            "correct_key": "A",
            "exp_en": "The Government of India constituted a High Powered Committee under Dr. Y.K. Alagh in 1999 to draft legislation enabling the incorporation of cooperatives as producer companies, leading to Part IX-A of the Companies Act, 1956 in 2002.",
            "exp_ta": "1999-ல் அமைக்கப்பட்ட டாக்டர் ஓய்.கே. அலாக் தலைமையிலான உயர்மட்டக் குழு உற்பத்தியாளர் நிறுவனங்களுக்கான சட்ட வரைவை உருவாக்கியது. இது 2002-ல் நிறுவனங்கள் சட்டத்தில் சேர்க்கப்பட்டது.",
            "why_a_en": "Correct. Y.K. Alagh Committee formulated the Producer Companies framework.",
            "why_a_ta": "சரி. ஓய்.கே. அலாக் குழுவே உற்பத்தியாளர் நிறுவனங்களுக்கான சட்டக் கட்டமைப்பை உருவாக்கியது.",
            "why_b_en": "Incorrect. Swaminathan Committee headed the National Commission on Farmers (2004-06).",
            "why_b_ta": "தவறு. சுவாமிநாதன் குழு தேசிய விவசாயிகள் ஆணையத்திற்குத் தலைமை தாங்கியது.",
            "why_c_en": "Incorrect. Rangarajan Committee dealt with financial inclusion and poverty.",
            "why_c_ta": "தவறு. ரங்கராஜன் குழு நிதி உள்ளடக்கத்திற்குத் தலைமை தாங்கியது.",
            "why_d_en": "Incorrect. Minhas Committee dealt with agricultural labor.",
            "why_d_ta": "தவறு. மின்ஹாஸ் குழு விவசாயத் தொழிலாளர்கள் பற்றியது.",
            "tip_en": "Producer Companies = Y.K. Alagh Committee (2000) → Companies Act Amendment 2002.",
            "tip_ta": "உற்பத்தியாளர் நிறுவனங்கள் = ஓய்.கே. அலாக் குழு (2000) → நிறுவனங்கள் சட்டம் திருத்தம் 2002.",
            "fact_en": "Producer Companies operate on cooperative principles ('one member, one vote') while registered under Company Law.",
            "fact_ta": "நிறுவனங்கள் சட்டத்தின் கீழ் பதிவு செய்யப்பட்டாலும் உற்பத்தியாளர் நிறுவனங்கள் 'ஒருவருக்கு ஒரு வாக்கு' என்ற கூட்டுறவுக் கொள்கையிலேயே இயங்குகின்றன."
        },

        # 46. TNPSC Group 4 2012
        {
            "subtopic": "Anand Pattern Three-Tier Structure",
            "stem_en": "[TNPSC Group 4 2012] In the famous 'Anand Pattern' cooperative dairy model, what constitutes the intermediate tier between the village dairy society and the state milk federation?",
            "stem_ta": "[TNPSC குரூப் 4 2012] புகழ்பெற்ற 'ஆனந்த் மாதிரி' கூட்டுறவு பால்வள அமைப்பில், கிராமப் பால் சங்கம் மற்றும் மாநிலப் பால் கூட்டமைப்புக்கு இடையே உள்ள இடைநிலை அடுக்கு எது?",
            "options": [
                ("District Co-operative Milk Producers' Union", "மாவட்டக் கூட்டுறவு பால் உற்பத்தியாளர்கள் ஒன்றியம்"),
                ("Taluk Dairy Cooperative", "வட்டார பால் கூட்டுறவு சங்கம்"),
                ("Regional Milk Board", "மண்டல பால் வாரியம்"),
                ("Block Dairy Union", "வட்டார பால் ஒன்றியம்")
            ],
            "correct_key": "A",
            "exp_en": "The Anand Pattern is a three-tier model: Tier 1 = Village Dairy Cooperative Society; Tier 2 = District Cooperative Milk Producers' Union (operates processing plant); Tier 3 = State Cooperative Milk Marketing Federation.",
            "exp_ta": "ஆனந்த் மாதிரி என்பது மூன்றடுக்கு அமைப்பு: அடுக்கு 1 = கிராமப் பால் சங்கம்; அடுக்கு 2 = மாவட்ட பால் உற்பத்தியாளர்கள் ஒன்றியம் (பதப்படுத்தும் ஆலை); அடுக்கு 3 = மாநில பால் சந்தைப்படுத்தல் கூட்டமைப்பு.",
            "why_a_en": "Correct. District Union is the intermediate processing tier.",
            "why_a_ta": "சரி. மாவட்ட பால் உற்பத்தியாளர்கள் ஒன்றியமே இடைநிலை அடுக்காகும்.",
            "why_b_en": "Incorrect. Taluk tier does not exist in the Anand model.",
            "why_b_ta": "தவறு. ஆனந்த் மாதிரியில் தாலுகா அடுக்கு கிடையாது.",
            "why_c_en": "Incorrect. Regional boards are not part of this structure.",
            "why_c_ta": "தவறு. மண்டல வாரியங்கள் இதில் இல்லை.",
            "why_d_en": "Incorrect. Block tier is not part of Anand pattern.",
            "why_d_ta": "தவறு. வட்டார அடுக்கு இதில் இல்லை.",
            "tip_en": "Anand Model Flow: Village Society (Collection) → District Union (Processing) → State Federation (Marketing).",
            "tip_ta": "ஆனந்த் மாதிரி ஓட்டம்: கிராம சங்கம் (கொள்முதல்) → மாவட்ட ஒன்றியம் (பதப்படுத்துதல்) → மாநில கூட்டமைப்பு (விற்பனை).",
            "fact_en": "This three-tier structure eliminated middlemen and directly empowered rural women dairy farmers.",
            "fact_ta": "இந்த மூன்றடுக்கு அமைப்பு இடைத்தரகர்களை ஒழித்து கிராமப்புற பெண் பால் உற்பத்தியாளர்களை நேரடியாக வலுப்படுத்தியது."
        },

        # 47. TNPSC Group 1 2021
        {
            "subtopic": "Union of India v. Rajendra N. Shah - Bench",
            "stem_en": "[TNPSC Group 1 2021] Who was the presiding judge of the three-judge Supreme Court bench that delivered the landmark judgment in Union of India v. Rajendra N. Shah on 20th July 2021?",
            "stem_ta": "[TNPSC குரூப் 1 2021] 2021 ஜூலை 20 அன்று இந்திய ஒன்றியம் எதிர் ராஜேந்திர என். ஷா வழக்கில் வரலாற்றுச் சிறப்புமிக்க தீர்ப்பை வழங்கிய உச்சநீதிமன்றத்தின் மூன்று நீதிபதிகள் கொண்ட அமர்வின் தலைமை நீதிபதி யார்?",
            "options": [
                ("Justice R.F. Nariman", "நீதிபதி ஆர்.எஃப். நாரிமன்"),
                ("Justice N.V. Ramana", "நீதிபதி என்.வி. ரமணா"),
                ("Justice D.Y. Chandrachud", "நீதிபதி டி.ஒய். சந்திரசூட்"),
                ("Justice Ranjan Gogoi", "நீதிபதி ரஞ்சன் கோகோய்")
            ],
            "correct_key": "A",
            "exp_en": "The 3-judge bench comprised Justice R.F. Nariman, Justice B.R. Gavai, and Justice K.M. Joseph. Justice Nariman authored the majority judgment declaring Part IX-B unconstitutional for state cooperatives while upholding it for multi-state cooperatives.",
            "exp_ta": "நீதிபதிகள் ஆர்.எஃப். நாரிமன், பி.ஆர். கவாய் மற்றும் கே.எம். ஜோசப் அடங்கிய 3 நீதிபதிகள் கொண்ட அமர்வில், நீதிபதி நாரிமன் பெரும்பான்மைத் தீர்ப்பை எழுதினார்.",
            "why_a_en": "Correct. Justice R.F. Nariman headed the bench and authored the majority judgment.",
            "why_a_ta": "சரி. நீதிபதி ஆர்.எஃப். நாரிமன் அமர்வுக்குத் தலைமை தாங்கி பெரும்பான்மைத் தீர்ப்பை எழுதினார்.",
            "why_b_en": "Incorrect. Justice N.V. Ramana was the Chief Justice of India at that time, but not on this bench.",
            "why_b_ta": "தவறு. நீதிபதி என்.வி. ரமணா அப்போது தலைமை நீதிபதியாக இருந்தார், ஆனால் இந்த அமர்வில் இல்லை.",
            "why_c_en": "Incorrect. Justice D.Y. Chandrachud was not on this bench.",
            "why_c_ta": "தவறு. நீதிபதி டி.ஒய். சந்திரசூட் இந்த அமர்வில் இல்லை.",
            "why_d_en": "Incorrect. Justice Ranjan Gogoi had retired in 2019.",
            "why_d_ta": "தவறு. நீதிபதி ரஞ்சன் கோகோய் 2019-ல் ஓய்வு பெற்றார்.",
            "tip_en": "Rajendra N. Shah Bench: Justice R.F. Nariman (Presiding & Author) + Justice B.R. Gavai (Concurring) + Justice K.M. Joseph (Dissenting on severability).",
            "tip_ta": "ராஜேந்திர ஷா அமர்வு: நீதிபதி நாரிமன் (தலைமை & தீர்ப்பு) + நீதிபதி கவாய் (ஆதரவு) + நீதிபதி ஜோசப் (மாறுபட்ட தீர்ப்பு).",
            "fact_en": "This was one of the last landmark constitutional judgments authored by Justice R.F. Nariman before his retirement in August 2021.",
            "fact_ta": "நீதிபதி ஆர்.எஃப். நாரிமன் ஆகஸ்ட் 2021-ல் ஓய்வு பெறுவதற்கு முன் வழங்கிய கடைசி முக்கிய அரசியலமைப்புத் தீர்ப்புகளில் இது ஒன்றாகும்."
        },

        # 48. TNPSC Group 2 2013
        {
            "subtopic": "Continuance of Existing Laws - Article 243ZT",
            "stem_en": "[TNPSC Group 2 2013] Under Article 243ZT of the Constitution, what was the maximum transitional period granted to States to amend their cooperative laws to bring them into conformity with Part IX-B?",
            "stem_ta": "[TNPSC குரூப் 2 2013] அரசியலமைப்பு உறுப்பு 243ZT-ன் கீழ், பகுதி IX-B-க்கு இணங்க தங்களின் கூட்டுறவு சட்டங்களைத் திருத்துவதற்கு மாநிலங்களுக்கு வழங்கப்பட்ட அதிகபட்ச இடைக்கால அவகாசம் என்ன?",
            "options": [
                ("One year", "ஒரு வருடம்"),
                ("Two years", "இரண்டு ஆண்டுகள்"),
                ("Six months", "ஆறு மாதங்கள்"),
                ("Three years", "மூன்று ஆண்டுகள்")
            ],
            "correct_key": "A",
            "exp_en": "Article 243ZT provided that inconsistent provisions of existing state laws would continue until amended or repealed, but not beyond one year from the commencement of the 97th Constitutional Amendment Act, 2011.",
            "exp_ta": "உறுப்பு 243ZT-ன் படி, முரண்பட்ட மாநிலச் சட்டங்கள் திருத்தப்படும் வரை அல்லது 97வது திருத்தம் அமலுக்கு வந்த தேதியிலிருந்து அதிகபட்சம் ஒரு வருடம் வரை மட்டுமே தொடர அனுமதிக்கப்பட்டன.",
            "why_a_en": "Correct. One year was the constitutional sunset period under Article 243ZT.",
            "why_a_ta": "சரி. உறுப்பு 243ZT-ன் கீழ் வழங்கப்பட்ட அவகாசம் சரியாக 1 வருடம்.",
            "why_b_en": "Incorrect. Two years was not provided.",
            "why_b_ta": "தவறு. இரண்டு ஆண்டுகள் வழங்கப்படவில்லை.",
            "why_c_en": "Incorrect. Six months is too short.",
            "why_c_ta": "தவறு. ஆறு மாதங்கள் என்பது தவறானது.",
            "why_d_en": "Incorrect. Three years is incorrect.",
            "why_d_ta": "தவறு. மூன்று ஆண்டுகள் என்பது தவறானது.",
            "tip_en": "Sunset Clauses in Local Government: Art 243N (Panchayats) = 1 year; Art 243ZF (Municipalities) = 1 year; Art 243ZT (Cooperatives) = 1 year.",
            "tip_ta": "இடைக்கால காலக்கெடு: உறுப்பு 243N (பஞ்சாயத்து) = 1 ஆண்டு; உறுப்பு 243ZF (நகராட்சி) = 1 ஆண்டு; உறுப்பு 243ZT (கூட்டுறவு) = 1 ஆண்டு.",
            "fact_en": "Tamil Nadu amended its Co-operative Societies Act in 2013 just before the expiry of the one-year period.",
            "fact_ta": "தமிழ்நாடு ஓராண்டு கால அவகாசம் முடிவடைவதற்கு சற்று முன்பு 2013-ல் தனது கூட்டுறவு சட்டத்தைத் திருத்தியது."
        },

        # 49. TNPSC Group 4 2011
        {
            "subtopic": "First Co-operative Credit Societies Act 1904",
            "stem_en": "[TNPSC Group 4 2011] Which Viceroy was in office when the historic Co-operative Credit Societies Act, 1904 was enacted in British India?",
            "stem_ta": "[TNPSC குரூப் 4 2011] பிரிட்டிஷ் இந்தியாவில் வரலாற்றுச் சிறப்புமிக்க கூட்டுறவு கடன் சங்கங்கள் சட்டம் 1904 இயற்றப்பட்டபோது பதவியில் இருந்த வைஸ்ராய் யார்?",
            "options": [
                ("Lord Curzon", "கர்சன் பிரபு"),
                ("Lord Ripon", "ரிப்பன் பிரபு"),
                ("Lord Minto", "மிண்டோ பிரபு"),
                ("Lord Chelmsford", "செம்ஸ்போர்டு பிரபு")
            ],
            "correct_key": "A",
            "exp_en": "The Co-operative Credit Societies Act (Act X of 1904) was passed by the Imperial Legislative Council on 25 March 1904 during the viceroyalty of Lord Curzon (1899-1905).",
            "exp_ta": "1904 மார்ச் 25 அன்று கர்சன் பிரபுவின் (1899-1905) ஆட்சிக் காலத்தில் கூட்டுறவு கடன் சங்கங்கள் சட்டம் (Act X of 1904) நிறைவேற்றப்பட்டது.",
            "why_a_en": "Correct. Lord Curzon was the Viceroy in 1904.",
            "why_a_ta": "சரி. 1904-ல் வைஸ்ராயாக இருந்தவர் கர்சன் பிரபு ஆவார்.",
            "why_b_en": "Incorrect. Lord Ripon (1880-84) was the Father of Local Self-Government in India.",
            "why_b_ta": "தவறு. ரிப்பன் பிரபு (1880-84) உள்ளாட்சி அமைப்புகளின் தந்தை ஆவார்.",
            "why_c_en": "Incorrect. Lord Minto was Viceroy from 1905 to 1910 (Morley-Minto Reforms).",
            "why_c_ta": "தவறு. மிண்டோ பிரபு 1905 முதல் 1910 வரை பதவியில் இருந்தார்.",
            "why_d_en": "Incorrect. Lord Chelmsford was Viceroy from 1916 to 1921 (Montagu-Chelmsford Reforms).",
            "why_d_ta": "தவறு. செம்ஸ்போர்டு பிரபு 1916 முதல் 1921 வரை பதவியில் இருந்தார்.",
            "tip_en": "Lord Curzon's Key Reforms: Co-operative Credit Societies Act (1904), Ancient Monuments Preservation Act (1904), Universities Act (1904).",
            "tip_ta": "கர்சன் பிரபுவின் சீர்திருத்தங்கள்: கூட்டுறவு சட்டம் (1904), தொல்பொருள் பாதுகாப்பு சட்டம் (1904), பல்கலைக்கழகங்கள் சட்டம் (1904).",
            "fact_en": "The 1904 Act classified societies into 'Rural' and 'Urban' societies.",
            "fact_ta": "1904 சட்டம் சங்கங்களை 'கிராமப்புற' மற்றும் 'நகர்ப்புற' சங்கங்கள் என இரு வகையாகப் பிரித்தது."
        },

        # 50. TNPSC Group 1 2022
        {
            "subtopic": "Motto of Cooperation",
            "stem_en": "[TNPSC Group 1 2022] What is the internationally accepted philosophical motto of the Co-operative Movement?",
            "stem_ta": "[TNPSC குரூப் 1 2022] கூட்டுறவு இயக்கத்தின் சர்வதேச அளவில் ஏற்றுக்கொள்ளப்பட்ட தத்துவார்த்த பொன்மொழி எது?",
            "options": [
                ("'Each for all and all for each'", "'ஒருவர் அனைவருக்கும், அனைவரும் ஒருவருக்கு'"),
                ("'Survival of the fittest'", "'வல்லவன் வாழ்வான்'"),
                ("'Profit above all'", "'அனைத்திற்கும் மேல் லாபம்'"),
                ("'Work is worship'", "'உழைப்பே உயர்வு'"),
            ],
            "correct_key": "A",
            "exp_en": "The universal motto of the cooperative movement is 'Each for all and all for each' (Self-help through mutual aid), reflecting the spirit of solidarity, shared prosperity, and collective economic democracy.",
            "exp_ta": "கூட்டுறவு இயக்கத்தின் சர்வதேச பொன்மொழி 'ஒருவர் அனைவருக்கும், அனைவரும் ஒருவருக்கு' (பரஸ்பர உதவி மூலம் சுய உதவி) என்பதாகும். இது ஒற்றுமை மற்றும் கூட்டுப் பொருளாதார ஜனநாயகத்தைப் பிரதிபலிக்கிறது.",
            "why_a_en": "Correct. 'Each for all and all for each' is the foundational cooperative motto.",
            "why_a_ta": "சரி. 'ஒருவர் அனைவருக்கும், அனைவரும் ஒருவருக்கு' என்பதே கூட்டுறவின் அடிப்படை தத்துவமாகும்.",
            "why_b_en": "Incorrect. 'Survival of the fittest' is Spencer's social Darwinism concept.",
            "why_b_ta": "தவறு. 'வல்லவன் வாழ்வான்' என்பது சமூக டார்வினிசக் கோட்பாடு.",
            "why_c_en": "Incorrect. Profit above all is the corporate capitalist slogan.",
            "why_c_ta": "தவறு. லாபமே பிரதானம் என்பது கார்ப்பரேட் நிறுவனங்களின் நோக்கம்.",
            "why_d_en": "Incorrect. 'Work is worship' is a general proverb, not the cooperative motto.",
            "why_d_ta": "தவறு. 'உழைப்பே உயர்வு' என்பது பொதுவான பழமொழி.",
            "tip_en": "Cooperative Motto = 'Each for all and all for each' + 'Self-help through mutual help'.",
            "tip_ta": "கூட்டுறவு பொன்மொழி = 'ஒருவர் அனைவருக்கும், அனைவரும் ஒருவருக்கு' + 'பரஸ்பர உதவி மூலம் சுய உதவி'.",
            "fact_en": "The International Co-operative Alliance (ICA) rainbow flag symbolizes the unity and diversity of cooperatives worldwide.",
            "fact_ta": "சர்வதேச கூட்டுறவு கூட்டணியின் (ICA) வானவில் கொடி உலகளாவிய கூட்டுறவுகளின் ஒற்றுமை மற்றும் பன்முகத்தன்மையைக் குறிக்கிறது."
        }
    ]


def build_pyq_file():
    raw_list = (
        get_pyq_raw_questions() +
        get_pyq_questions_batch2() +
        get_pyq_questions_batch3() +
        get_pyq_questions_batch4() +
        get_pyq_questions_batch5()
    )
    print(f"Loaded {len(raw_list)} raw PYQ questions.")
    assert len(raw_list) == 50, f"Expected 50 questions, got {len(raw_list)}"

    questions = []
    for idx, item in enumerate(raw_list, start=1):
        qid = f"CS_PYQ_{idx:03d}"
        opts = item["options"]
        correct_key = item["correct_key"]

        q = make_coop_q(
            qid=qid,
            diff="Medium" if idx % 2 == 0 else "Easy",
            qtype="PYQ",
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
            tags=["polity", "cooperative_societies", "pyq", item["subtopic"].lower().replace(" ", "_")]
        )
        questions.append(q)

    # Randomize and balance answer keys: 12-13 per option, max run <= 2
    balanced = randomize_and_balance_dataset(questions, seed=202)
    key_dist = Counter(q["correct_answer"] for q in balanced)
    print(f"Balanced Key Distribution: {dict(key_dist)}")

    out_dir = os.path.join("data", "questions", "polity")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "cooperative_societies_pyq.json")

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(balanced, f, ensure_ascii=False, indent=2)
    print(f"Saved balanced PYQ MCQs to {out_path}")

    # Validation
    rep = ContentValidator.validate_file(out_path, expected_count=50, expected_prefix="CS_PYQ_")
    print(f"Validation: {'PASS' if rep.is_valid else 'FAIL'} | Total: {rep.total_audited}")
    print(f"Keys: {rep.key_distribution}")
    if not rep.is_valid:
        for iss in rep.issues:
            print("  Issue:", iss.severity, iss.field_name, iss.message)
    return rep.is_valid


if __name__ == "__main__":
    success = build_pyq_file()
    if not success:
        exit(1)
