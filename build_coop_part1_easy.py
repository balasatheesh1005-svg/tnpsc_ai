# -*- coding: utf-8 -*-
"""
Co-operative Societies - Part 1: Easy MCQs (50 Questions: CS_E_001 to CS_E_050)
TNPSC Nova AI Content Engine
"""
import os
import json
from collections import Counter
from tools.nova_content_engine.answer_randomizer import randomize_and_balance_dataset
from tools.nova_content_engine.validator import ContentValidator
from cooperative_societies_mcq_helper import make_coop_q


def get_easy_raw_questions():
    return [
        # 1. Constitutional Part
        {
            "subtopic": "Constitutional Provisions - Part IX-B",
            "stem_en": "Which Part was added to the Constitution of India by the 97th Constitutional Amendment Act, 2011 to provide constitutional status to Co-operative Societies?",
            "stem_ta": "கூட்டுறவு சங்கங்களுக்கு அரசியலமைப்பு அந்தஸ்து வழங்குவதற்காக 2011-ஆம் ஆண்டின் 97-வது அரசியலமைப்புத் திருத்தச் சட்டத்தின் மூலம் இந்திய அரசியலமைப்பில் சேர்க்கப்பட்ட பகுதி எது?",
            "options": [
                ("Part IX-B", "பகுதி IX-B"),
                ("Part IX-A", "பகுதி IX-A"),
                ("Part IX", "பகுதி IX"),
                ("Part XIV-A", "பகுதி XIV-A")
            ],
            "correct_key": "A",
            "exp_en": "The 97th Constitutional Amendment Act, 2011 added Part IX-B entitled 'The Co-operative Societies' comprising Articles 243ZH to 243ZT.",
            "exp_ta": "2011-ஆம் ஆண்டின் 97-வது அரசியலமைப்புத் திருத்தச் சட்டம் 'கூட்டுறவு சங்கங்கள்' என்ற தலைப்பில் சரத்துகள் 243ZH முதல் 243ZT வரை கொண்ட பகுதி IX-B-ஐச் சேர்த்தது.",
            "why_a_en": "Correct. Part IX-B specifically deals with Co-operative Societies.",
            "why_a_ta": "சரி. பகுதி IX-B குறிப்பாகக் கூட்டுறவு சங்கங்களைக் கையாள்கிறது.",
            "why_b_en": "Incorrect. Part IX-A covers Municipalities (Articles 243P-243ZG).",
            "why_b_ta": "தவறு. பகுதி IX-A நகராட்சிகளை உள்ளடக்கியது (சரத்துகள் 243P-243ZG).",
            "why_c_en": "Incorrect. Part IX covers Panchayats (Articles 243-243O).",
            "why_c_ta": "தவறு. பகுதி IX பஞ்சாயத்துகளை உள்ளடக்கியது (சரத்துகள் 243-243O).",
            "why_d_en": "Incorrect. Part XIV-A deals with Tribunals (Articles 323A-323B).",
            "why_d_ta": "தவறு. பகுதி XIV-A தீர்ப்பாயங்களைக் கையாள்கிறது (சரத்துகள் 323A-323B).",
            "tip_en": "Remember: Part IX = Panchayats, Part IX-A = Municipalities, Part IX-B = Co-operative Societies.",
            "tip_ta": "நினைவில் கொள்க: பகுதி IX = பஞ்சாயத்துகள், பகுதி IX-A = நகராட்சிகள், பகுதி IX-B = கூட்டுறவு சங்கங்கள்.",
            "fact_en": "The 97th Constitutional Amendment came into effect on 15th February 2012.",
            "fact_ta": "97வது அரசியலமைப்புத் திருத்தச் சட்டம் 2012 பிப்ரவரி 15 அன்று நடைமுறைக்கு வந்தது."
        },

        # 2. Fundamental Right - Article 19(1)(c)
        {
            "subtopic": "Fundamental Rights - Article 19(1)(c)",
            "stem_en": "Under which Fundamental Right was the right to form 'co-operative societies' explicitly included by the 97th Constitutional Amendment Act, 2011?",
            "stem_ta": "2011-ஆம் ஆண்டின் 97-வது அரசியலமைப்புத் திருத்தச் சட்டத்தின் மூலம் 'கூட்டுறவு சங்கங்களை' அமைக்கும் உரிமை எந்த அடிப்படை உரிமையின் கீழ் வெளிப்படையாகச் சேர்க்கப்பட்டது?",
            "options": [
                ("Article 19(1)(c)", "சரத்து 19(1)(c)"),
                ("Article 19(1)(a)", "சரத்து 19(1)(a)"),
                ("Article 19(1)(b)", "சரத்து 19(1)(b)"),
                ("Article 21", "சரத்து 21")
            ],
            "correct_key": "A",
            "exp_en": "The 97th Amendment amended Article 19(1)(c) to guarantee all citizens the fundamental right to form associations or unions or 'co-operative societies'.",
            "exp_ta": "97வது திருத்தம் சரத்து 19(1)(c)-ஐத் திருத்தி, அனைத்துக் குடிமக்களுக்கும் சங்கங்கள் அல்லது தொழிற்சங்கங்கள் அல்லது 'கூட்டுறவு சங்கங்களை' அமைக்கும் அடிப்படை உரிமையை உத்தரவாதப்படுத்தியது.",
            "why_a_en": "Correct. Article 19(1)(c) guarantees freedom of association, including co-operative societies.",
            "why_a_ta": "சரி. சரத்து 19(1)(c) கூட்டுறவு சங்கங்கள் உட்பட சங்கம் அமைக்கும் சுதந்திரத்தை உறுதி செய்கிறது.",
            "why_b_en": "Incorrect. Article 19(1)(a) guarantees freedom of speech and expression.",
            "why_b_ta": "தவறு. சரத்து 19(1)(a) பேச்சு மற்றும் கருத்துச் சுதந்திரத்தை உறுதி செய்கிறது.",
            "why_c_en": "Incorrect. Article 19(1)(b) guarantees freedom to assemble peacefully without arms.",
            "why_c_ta": "தவறு. சரத்து 19(1)(b) ஆயுதங்களின்றி அமைதியாகக் கூடும் உரிமையை உறுதி செய்கிறது.",
            "why_d_en": "Incorrect. Article 21 protects life and personal liberty.",
            "why_d_ta": "தவறு. சரத்து 21 வாழ்வு மற்றும் தனிநபர் சுதந்திரத்தைப் பாதுகாக்கிறது.",
            "tip_en": "The right to form cooperatives is a Fundamental Right, but the right to recognition or affiliation is not.",
            "tip_ta": "கூட்டுறவு அமைக்கும் உரிமை அடிப்படை உரிமையாகும், ஆனால் அங்கீகாரம் பெறும் உரிமை அடிப்படை உரிமை அல்ல.",
            "fact_en": "The Supreme Court in the 2021 Rajendra Shah case upheld Article 19(1)(c) as fully valid.",
            "fact_ta": "2021 ராஜேந்திர ஷா வழக்கில் உச்ச நீதிமன்றம் சரத்து 19(1)(c)-ஐ முழுமையாகச் செல்லுபடியாகும் என உறுதி செய்தது."
        },

        # 3. DPSP - Article 43B
        {
            "subtopic": "Directive Principles - Article 43B",
            "stem_en": "Which Article was inserted into Part IV (Directive Principles of State Policy) of the Indian Constitution to promote Co-operative Societies?",
            "stem_ta": "கூட்டுறவு சங்கங்களை ஊக்குவிப்பதற்காக இந்திய அரசியலமைப்பின் பகுதி IV-ல் (அரசு வழிகாட்டு நெறிமுறைகள்) சேர்க்கப்பட்ட சரத்து எது?",
            "options": [
                ("Article 43B", "சரத்து 43B"),
                ("Article 43A", "சரத்து 43A"),
                ("Article 44", "சரத்து 44"),
                ("Article 48A", "சரத்து 48A")
            ],
            "correct_key": "A",
            "exp_en": "Article 43B was inserted into Part IV by the 97th Amendment, directing the State to endeavor to promote voluntary formation, autonomous functioning, democratic control and professional management of co-operative societies.",
            "exp_ta": "97வது திருத்தத்தால் பகுதி IV-ல் சரத்து 43B சேர்க்கப்பட்டது; இது கூட்டுறவு சங்கங்களின் தன்னார்வ உருவாக்கம், தன்னாட்சி செயல்பாடு, ஜனநாயகக் கட்டுப்பாடு மற்றும் தொழில்முறை நிர்வாகத்தை ஊக்குவிக்க அரசு முயல வேண்டும் என்று கூறுகிறது.",
            "why_a_en": "Correct. Article 43B promotes co-operative societies under DPSP.",
            "why_a_ta": "சரி. சரத்து 43B DPSP-ன் கீழ் கூட்டுறவு சங்கங்களை ஊக்குவிக்கிறது.",
            "why_b_en": "Incorrect. Article 43A deals with workers' participation in management of industries (42nd CAA 1976).",
            "why_b_ta": "தவறு. சரத்து 43A தொழிற்சாலைகள் நிர்வாகத்தில் தொழிலாளர்களின் பங்கேற்பைக் கையாள்கிறது (42வது திருத்தம் 1976).",
            "why_c_en": "Incorrect. Article 44 deals with the Uniform Civil Code.",
            "why_c_ta": "தவறு. சரத்து 44 பொது சிவில் சட்டத்தைக் கையாள்கிறது.",
            "why_d_en": "Incorrect. Article 48A deals with protection and improvement of environment and forests.",
            "why_d_ta": "தவறு. சரத்து 48A சுற்றுச்சூழல் மற்றும் காடுகள் பாதுகாப்பைக் கையாள்கிறது.",
            "tip_en": "Remember: 43A = Workers' participation; 43B = Co-operative societies.",
            "tip_ta": "நினைவில் கொள்க: 43A = தொழிலாளர் பங்கேற்பு; 43B = கூட்டுறவு சங்கங்கள்.",
            "fact_en": "Article 43B belongs to the category of Gandhian and Socialistic principles in DPSP.",
            "fact_ta": "சரத்து 43B DPSP-ல் காந்திய மற்றும் சமதர்மக் கொள்கைகளின் கீழ் வகைப்படுத்தப்படுகிறது."
        },

        # 4. Maximum Board Members
        {
            "subtopic": "Board Composition & Term - Article 243ZJ",
            "stem_en": "What is the maximum number of directors permitted on the board of a co-operative society under Article 243ZJ(1) of the Indian Constitution?",
            "stem_ta": "இந்திய அரசியலமைப்பின் சரத்து 243ZJ(1)-ன் கீழ் ஒரு கூட்டுறவு சங்கத்தின் இயக்குநர் வாரியத்தில் அனுமதிக்கப்படும் அதிகபட்ச இயக்குநர்களின் எண்ணிக்கை யாது?",
            "options": [
                ("21", "21"),
                ("15", "15"),
                ("25", "25"),
                ("31", "31")
            ],
            "correct_key": "A",
            "exp_en": "Article 243ZJ(1) explicitly provides that the number of directors of a co-operative society shall not exceed 21.",
            "exp_ta": "சரத்து 243ZJ(1) ஒரு கூட்டுறவு சங்கத்தின் இயக்குநர்களின் எண்ணிக்கை 21-க்கு மிகாமல் இருக்க வேண்டும் என்று வெளிப்படையாக விதிக்கிறது.",
            "why_a_en": "Correct. The constitutional ceiling on the number of directors is 21.",
            "why_a_ta": "சரி. இயக்குநர்களின் எண்ணிக்கையின் மீதான அரசியலமைப்பு உச்சவரம்பு 21 ஆகும்.",
            "why_b_en": "Incorrect. 15 is the limit for Council of Ministers (15% of assembly size), not cooperatives.",
            "why_b_ta": "தவறு. 15 என்பது அமைச்சரவைக்கான வரம்பு (15%), கூட்டுறவுக்கு அல்ல.",
            "why_c_en": "Incorrect. 25 is not the statutory maximum.",
            "why_c_ta": "தவறு. 25 சட்டப்பூர்வ அதிகபட்ச வரம்பு அல்ல.",
            "why_d_en": "Incorrect. 31 is the maximum number of Supreme Court judges originally before 2019.",
            "why_d_ta": "தவறு. 31 என்பது 2019-க்கு முந்தைய உச்ச நீதிமன்ற நீதிபதிகளின் எண்ணிக்கை.",
            "tip_en": "21 directors maximum on the board; co-opted directors (max 2) are in addition to the 21.",
            "tip_ta": "வாரியத்தில் அதிகபட்சம் 21 இயக்குநர்கள்; இணைத்துக் கொள்ளப்படும் இயக்குநர்கள் (அதிகபட்சம் 2) இந்த 21-க்கு கூடுதலானவர்கள்.",
            "fact_en": "Co-opted members are excluded from the maximum ceiling of 21 directors.",
            "fact_ta": "இணைத்துக் கொள்ளப்பட்ட உறுப்பினர்கள் 21 இயக்குநர்கள் என்ற உச்சவரம்பிலிருந்து விலக்களிக்கப்படுகிறார்கள்."
        },

        # 5. Term of Board
        {
            "subtopic": "Board Composition & Term - Article 243ZJ",
            "stem_en": "What is the constitutional term of office of elected members of the board of a co-operative society under Article 243ZJ(2)?",
            "stem_ta": "சரத்து 243ZJ(2)-ன் கீழ் ஒரு கூட்டுறவு சங்க வாரியத்தின் தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்களின் அரசியலமைப்புப் பதவிக்காலம் என்ன?",
            "options": [
                ("5 years from the date of election", "தேர்தல் தேதியிலிருந்து 5 ஆண்டுகள்"),
                ("3 years from the date of election", "தேர்தல் தேதியிலிருந்து 3 ஆண்டுகள்"),
                ("4 years from the date of election", "தேர்தல் தேதியிலிருந்து 4 ஆண்டுகள்"),
                ("6 years from the date of election", "தேர்தல் தேதியிலிருந்து 6 ஆண்டுகள்")
            ],
            "correct_key": "A",
            "exp_en": "Article 243ZJ(2) provides that the term of office of elected members of the board and its office bearers shall be 5 years from the date of election.",
            "exp_ta": "சரத்து 243ZJ(2) தேர்ந்தெடுக்கப்பட்ட வாரிய உறுப்பினர்கள் மற்றும் அதன் நிர்வாகிகளின் பதவிக்காலம் தேர்தல் தேதியிலிருந்து 5 ஆண்டுகள் என்று வழங்குகிறது.",
            "why_a_en": "Correct. The constitutional tenure is 5 years from election.",
            "why_a_ta": "சரி. அரசியலமைப்புப் பதவிக்காலம் தேர்தலிலிருந்து 5 ஆண்டுகள்.",
            "why_b_en": "Incorrect. 3 years was a term in certain historical state acts, but Constitution sets 5 years.",
            "why_b_ta": "தவறு. 3 ஆண்டுகள் சில வரலாற்று மாநிலச் சட்டங்களில் இருந்தது, ஆனால் அரசியலமைப்பு 5 ஆண்டுகளை நிர்ணயிக்கிறது.",
            "why_c_en": "Incorrect. 4 years is not the constitutional term.",
            "why_c_ta": "தவறு. 4 ஆண்டுகள் அரசியலமைப்புப் பதவிக்காலம் அல்ல.",
            "why_d_en": "Incorrect. 6 years is the term of Rajya Sabha members.",
            "why_d_ta": "தவறு. 6 ஆண்டுகள் ராஜ்யசபா உறுப்பினர்களின் பதவிக்காலம்.",
            "tip_en": "Cooperative board term matches Panchayat and Municipality terms (5 years).",
            "tip_ta": "கூட்டுறவு வாரியப் பதவிக்காலம் பஞ்சாயத்து மற்றும் நகராட்சி பதவிக்காலத்துடன் ஒத்துப்போகிறது (5 ஆண்டுகள்).",
            "fact_en": "Elections must be completed before the expiry of the 5-year term under Article 243ZK.",
            "fact_ta": "சரத்து 243ZK-ன் படி 5 ஆண்டு காலம் முடிவதற்குள் தேர்தல்கள் நடத்தி முடிக்கப்பட வேண்டும்."
        },

        # 6. SC/ST and Women Reservation
        {
            "subtopic": "Board Composition & Term - Article 243ZJ",
            "stem_en": "Under Article 243ZJ(1), what is the mandatory reservation provided on the board of every co-operative society having members from such categories?",
            "stem_ta": "சரத்து 243ZJ(1)-ன் கீழ், அத்தகைய பிரிவு உறுப்பினர்களைக் கொண்ட ஒவ்வொரு கூட்டுறவு சங்கத்தின் வாரியத்திலும் வழங்கப்படும் கட்டாய இடஒதுக்கீடு என்ன?",
            "options": [
                ("1 seat for SC/ST and 2 seats for Women", "SC/ST-க்கு 1 இடம் மற்றும் பெண்களுக்கு 2 இடங்கள்"),
                ("2 seats for SC/ST and 1 seat for Women", "SC/ST-க்கு 2 இடங்கள் மற்றும் பெண்களுக்கு 1 இடம்"),
                ("1 seat for SC/ST and 1 seat for Women", "SC/ST-க்கு 1 இடம் மற்றும் பெண்களுக்கு 1 இடம்"),
                ("2 seats for SC/ST and 2 seats for Women", "SC/ST-க்கு 2 இடங்கள் மற்றும் பெண்களுக்கு 2 இடங்கள்")
            ],
            "correct_key": "A",
            "exp_en": "Article 243ZJ(1) mandates reservation of 1 seat for Scheduled Castes or Scheduled Tribes and 2 seats for Women on the board of every co-operative society consisting of individuals as members.",
            "exp_ta": "சரத்து 243ZJ(1) தனிநபர்களை உறுப்பினர்களாகக் கொண்ட ஒவ்வொரு கூட்டுறவு சங்க வாரியத்திலும் பட்டியல் சாதியினர் அல்லது பழங்குடியினருக்கு 1 இடமும், பெண்களுக்கு 2 இடங்களும் ஒதுக்கீடு செய்வதைக் கட்டாயமாக்குகிறது.",
            "why_a_en": "Correct. Exactly 1 SC/ST seat and 2 Women seats are reserved.",
            "why_a_ta": "சரி. சரியாக 1 SC/ST இடம் மற்றும் 2 பெண்கள் இடங்கள் ஒதுக்கப்பட்டுள்ளன.",
            "why_b_en": "Incorrect. Reverses the ratio.",
            "why_b_ta": "தவறு. விகிதத்தை மாற்றிக் காட்டுகிறது.",
            "why_c_en": "Incorrect. Women have 2 seats, not 1.",
            "why_c_ta": "தவறு. பெண்களுக்கு 2 இடங்கள் உண்டு, 1 அல்ல.",
            "why_d_en": "Incorrect. SC/ST has 1 seat, not 2.",
            "why_d_ta": "தவறு. SC/ST-க்கு 1 இடம் மட்டுமே, 2 அல்ல.",
            "tip_en": "Memory Code: Cooperative Board = 1 SC/ST + 2 Women (Total 3 reserved seats).",
            "tip_ta": "நினைவுக் குறியீடு: கூட்டுறவு வாரியம் = 1 SC/ST + 2 பெண்கள் (மொத்தம் 3 இடஒதுக்கீட்டு இடங்கள்).",
            "fact_en": "These seats are reserved within the overall ceiling of 21 directors.",
            "fact_ta": "இந்த இடங்கள் 21 இயக்குநர்கள் என்ற ஒட்டுமொத்த உச்சவரம்பிற்குள்ளேயே ஒதுக்கப்படுகின்றன."
        },

        # 7. Co-opted Members Voting Rights
        {
            "subtopic": "Board Composition & Term - Article 243ZJ",
            "stem_en": "How many co-opted persons having specialized banking or finance experience can be accommodated on the board, and do they have voting rights in office-bearer elections?",
            "stem_ta": "வங்கி அல்லது நிதி அனுபவம் கொண்ட எத்தனை நபர்களை வாரியத்தில் இணைத்துக் கொள்ளலாம், மேலும் அவர்களுக்கு நிர்வாகி தேர்தல்களில் வாக்களிக்கும் உரிமை உண்டா?",
            "options": [
                ("Maximum 2 co-opted members; they CANNOT vote in office-bearer elections", "அதிகபட்சம் 2 இணை உறுப்பினர்கள்; அவர்களுக்கு நிர்வாகி தேர்தல்களில் வாக்களிக்கும் உரிமை இல்லை"),
                ("Maximum 2 co-opted members; they CAN vote in all elections", "அதிகபட்சம் 2 இணை உறுப்பினர்கள்; அவர்கள் அனைத்து தேர்தல்களிலும் வாக்களிக்கலாம்"),
                ("Maximum 3 co-opted members; they CANNOT vote in any matter", "அதிகபட்சம் 3 இணை உறுப்பினர்கள்; அவர்கள் எந்த விஷயத்திலும் வாக்களிக்க முடியாது"),
                ("Maximum 5 co-opted members; they have full voting rights", "அதிகபட்சம் 5 இணை உறுப்பினர்கள்; அவர்களுக்கு முழு வாக்குரிமை உண்டு")
            ],
            "correct_key": "A",
            "exp_en": "Under Article 243ZJ(1) second proviso, the State Legislature may provide for co-option of up to 2 persons having experience in banking, management or finance, provided that they shall NOT have the right to vote in any election of office bearers or be eligible to be elected as office bearers.",
            "exp_ta": "சரத்து 243ZJ(1) இரண்டாவது வரம்பின் படி, வங்கி, மேலாண்மை அல்லது நிதி அனுபவம் கொண்ட 2 நபர்கள் வரை இணைத்துக் கொள்ள மாநில சட்டமன்றம் வழிவகை செய்யலாம்; ஆனால் அவர்கள் நிர்வாகி தேர்தல்களில் வாக்களிக்கவோ அல்லது நிர்வாகிகளாகத் தேர்ந்தெடுக்கப்படவோ உரிமை கிடையாது.",
            "why_a_en": "Correct. Maximum 2 co-opted members, and they cannot vote in office-bearer elections.",
            "why_a_ta": "சரி. அதிகபட்சம் 2 இணை உறுப்பினர்கள், மற்றும் அவர்களுக்கு நிர்வாகி தேர்தல்களில் வாக்களிக்கும் உரிமை இல்லை.",
            "why_b_en": "Incorrect. They are barred from voting in office-bearer elections.",
            "why_b_ta": "தவறு. அவர்கள் நிர்வாகி தேர்தல்களில் வாக்களிக்கத் தடை விதிக்கப்பட்டுள்ளனர்.",
            "why_c_en": "Incorrect. The limit is 2, not 3.",
            "why_c_ta": "தவறு. வரம்பு 2 ஆகும், 3 அல்ல.",
            "why_d_en": "Incorrect. Maximum is 2.",
            "why_d_ta": "தவறு. அதிகபட்சம் 2 மட்டுமே.",
            "tip_en": "Co-opted members can participate in general board meetings but cannot vote for President/Vice-President.",
            "tip_ta": "இணை உறுப்பினர்கள் பொது வாரியக் கூட்டங்களில் பங்கேற்கலாம் ஆனால் தலைவர்/துணைத்தலைவர் தேர்தலில் வாக்களிக்க முடியாது.",
            "fact_en": "Co-opted members are also not counted for the purpose of quorum.",
            "fact_ta": "கோரம் (குறைந்தபட்ச வருகை) கணக்கிடுவதற்கு இணை உறுப்பினர்கள் கணக்கில் கொள்ளப்படுவதில்லை."
        },

        # 8. Maximum Period of Supersession
        {
            "subtopic": "Supersession and Suspension of Board - Article 243ZL",
            "stem_en": "Under Article 243ZL(1), what is the maximum period for which the board of a normal (non-banking) co-operative society can be kept superseded or suspended?",
            "stem_ta": "சரத்து 243ZL(1)-ன் கீழ், ஒரு சாதாரண (வங்கி அல்லாத) கூட்டுறவு சங்கத்தின் வாரியத்தை அதிகபட்சமாக எவ்வளவு காலம் இடைநீக்கம் செய்து வைத்திருக்க முடியும்?",
            "options": [
                ("6 months", "6 மாதங்கள்"),
                ("1 year", "1 ஆண்டு"),
                ("2 years", "2 ஆண்டுகள்"),
                ("3 months", "3 மாதங்கள்")
            ],
            "correct_key": "A",
            "exp_en": "Article 243ZL(1) provides that no board shall be superseded or kept under suspension for a period exceeding 6 months. For co-operative societies conducting banking business, this period can extend up to 1 year.",
            "exp_ta": "சரத்து 243ZL(1) எந்தவொரு வாரியமும் 6 மாதங்களுக்கு மிகாமல் மட்டுமே இடைநீக்கம் செய்யப்படலாம் என்று கூறுகிறது. வங்கித் தொழில் செய்யும் கூட்டுறவு சங்கங்களுக்கு இது 1 ஆண்டு வரை நீட்டிக்கப்படலாம்.",
            "why_a_en": "Correct. Normal co-operative boards can only be superseded for up to 6 months.",
            "why_a_ta": "சரி. சாதாரண கூட்டுறவு வாரியங்கள் அதிகபட்சம் 6 மாதங்கள் மட்டுமே இடைநீக்கம் செய்யப்படலாம்.",
            "why_b_en": "Incorrect. 1 year applies ONLY to cooperative societies doing banking business.",
            "why_b_ta": "தவறு. 1 ஆண்டு என்பது வங்கி வணிகம் செய்யும் கூட்டுறவு சங்கங்களுக்கு மட்டுமே பொருந்தும்.",
            "why_c_en": "Incorrect. 2 years was permitted under older arbitrary state laws, but 97th CAA capped it at 6 months.",
            "why_c_ta": "தவறு. பழைய மாநிலச் சட்டங்களில் 2 ஆண்டுகள் அனுமதிக்கப்பட்டது, ஆனால் 97வது திருத்தம் 6 மாதங்களாகக் கட்டுப்படுத்தியது.",
            "why_d_en": "Incorrect. 3 months is too short.",
            "why_d_ta": "தவறு. 3 மாதங்கள் மிகக் குறைவு.",
            "tip_en": "Supersession limit: Normal = 6 months; Banking = 1 year.",
            "tip_ta": "இடைநீக்க வரம்பு: சாதாரண சங்கங்கள் = 6 மாதங்கள்; வங்கி சங்கங்கள் = 1 ஆண்டு.",
            "fact_en": "Elections must be held within 6 months to reconstitute the board.",
            "fact_ta": "வாரியத்தை மீண்டும் அமைக்க 6 மாதங்களுக்குள் தேர்தல்கள் நடத்தப்பட வேண்டும்."
        },

        # 9. Exemption from Supersession
        {
            "subtopic": "Supersession and Suspension of Board - Article 243ZL",
            "stem_en": "Under Article 243ZL, in which of the following cases CANNOT a co-operative society's board be superseded or suspended by the Government?",
            "stem_ta": "சரத்து 243ZL-ன் கீழ், பின்வரும் எந்தச் சூழ்நிலையில் ஒரு கூட்டுறவு சங்க வாரியத்தை அரசால் இடைநீக்கம் செய்ய முடியாது?",
            "options": [
                ("Where there is no government shareholding, loan, financial assistance, or guarantee", "அரசின் பங்குகள், கடன், நிதி உதவி அல்லது உத்தரவாதம் இல்லாத சங்கங்களில்"),
                ("Where there is 10% government shareholding", "10% அரசுப் பங்குகள் உள்ள சங்கங்களில்"),
                ("Where a loan has been guaranteed by the State Government", "மாநில அரசால் கடனுக்கு உத்தரவாதம் அளிக்கப்பட்ட சங்கங்களில்"),
                ("Where financial assistance was provided by the Central Government", "மத்திய அரசால் நிதி உதவி வழங்கப்பட்ட சங்கங்களில்")
            ],
            "correct_key": "A",
            "exp_en": "Article 243ZL first proviso explicitly states that the board of any co-operative society shall not be superseded or kept under suspension where there is no Government shareholding or loan or financial assistance or any guarantee by the Government.",
            "exp_ta": "சரத்து 243ZL முதல் வரம்பு, எந்தவொரு கூட்டுறவு சங்கத்திலும் அரசின் பங்குகள், கடன், நிதி உதவி அல்லது அரசின் உத்தரவாதம் இல்லாத நிலையில் அதன் வாரியத்தை இடைநீக்கம் செய்ய முடியாது என்று வெளிப்படையாகக் கூறுகிறது.",
            "why_a_en": "Correct. Complete financial autonomy protects the board from executive supersession.",
            "why_a_ta": "சரி. முழுமையான நிதி தன்னாட்சியானது வாரியத்தை நிர்வாக இடைநீக்கத்திலிருந்து பாதுகாக்கிறது.",
            "why_b_en": "Incorrect. If there is government shareholding, supersession is legally possible on specified grounds.",
            "why_b_ta": "தவறு. அரசுப் பங்குகள் இருந்தால் குறிப்பிட்ட காரணங்களுக்காக இடைநீக்கம் செய்ய முடியும்.",
            "why_c_en": "Incorrect. Government guarantee allows supersession in case of default/mismanagement.",
            "why_c_ta": "தவறு. அரசின் உத்தரவாதம் இருந்தால் தவறான நிர்வாகத்தின் போது இடைநீக்கம் செய்ய அனுமதிக்கப்படுகிறது.",
            "why_d_en": "Incorrect. Government financial assistance brings the society within supersession powers.",
            "why_d_ta": "தவறு. அரசு நிதி உதவி பெற்ற சங்கங்கள் இடைநீக்க அதிகார வரம்பிற்குள் வருகின்றன.",
            "tip_en": "No government money = No government power to supersede board.",
            "tip_ta": "அரசு நிதி இல்லை = வாரியத்தை இடைநீக்கம் செய்ய அரசுக்கு அதிகாரம் இல்லை.",
            "fact_en": "This protection promotes genuine member-controlled autonomous cooperative development.",
            "fact_ta": "இந்த பாதுகாப்பு உண்மையான உறுப்பினர் கட்டுப்பாட்டு தன்னாட்சி கூட்டுறவு வளர்ச்சியை ஊக்குவிக்கிறது."
        },

        # 10. Audit Timeframe
        {
            "subtopic": "Audit of Accounts - Article 243ZM",
            "stem_en": "Within what period from the close of the financial year must the accounts of every co-operative society be audited under Article 243ZM(2)?",
            "stem_ta": "சரத்து 243ZM(2)-ன் கீழ் ஒவ்வொரு கூட்டுறவு சங்கத்தின் கணக்குகளும் நிதியாண்டு முடிந்ததிலிருந்து எத்தனை காலத்திற்குள் தணிக்கை செய்யப்பட வேண்டும்?",
            "options": [
                ("Within 6 months", "6 மாதங்களுக்குள்"),
                ("Within 3 months", "3 மாதங்களுக்குள்"),
                ("Within 9 months", "9 மாதங்களுக்குள்"),
                ("Within 1 year", "1 ஆண்டிற்குள்")
            ],
            "correct_key": "A",
            "exp_en": "Article 243ZM(2) mandates that the accounts of every co-operative society shall be audited within 6 months of the close of the financial year to which such accounts relate.",
            "exp_ta": "சரத்து 243ZM(2) ஒவ்வொரு கூட்டுறவு சங்கத்தின் கணக்குகளும் சம்பந்தப்பட்ட நிதியாண்டு முடிந்த 6 மாதங்களுக்குள் தணிக்கை செய்யப்பட வேண்டும் என்று கட்டாயமாக்குகிறது.",
            "why_a_en": "Correct. Audit must be completed within 6 months of financial year close.",
            "why_a_ta": "சரி. நிதியாண்டு முடிவடைந்த 6 மாதங்களுக்குள் தணிக்கை முடிக்கப்பட வேண்டும்.",
            "why_b_en": "Incorrect. 3 months is insufficient time for comprehensive cooperative audit.",
            "why_b_ta": "தவறு. விரிவான கூட்டுறவு தணிக்கைக்கு 3 மாதங்கள் போதுமான நேரமல்ல.",
            "why_c_en": "Incorrect. 9 months is not the constitutional timeframe.",
            "why_c_ta": "தவறு. 9 மாதங்கள் அரசியலமைப்பு காலக்கெடு அல்ல.",
            "why_d_en": "Incorrect. 1 year is the limit for placing audit report in legislature, not conducting audit.",
            "why_d_ta": "தவறு. 1 ஆண்டு என்பது தணிக்கை அறிக்கையைச் சமர்ப்பிப்பதற்கான காலக்கெடுவாகும்.",
            "tip_en": "Audit period (243ZM) and AGM period (243ZN) are both 6 months from close of financial year.",
            "tip_ta": "தணிக்கை காலம் (243ZM) மற்றும் AGM காலம் (243ZN) இரண்டுமே நிதியாண்டு முடிந்த 6 மாதங்கள் ஆகும்.",
            "fact_en": "Audit must be conducted by an auditor or auditing firm approved by the State Government.",
            "fact_ta": "மாநில அரசால் அங்கீகரிக்கப்பட்ட தணிக்கையாளர் அல்லது தணிக்கை நிறுவனத்தால் மட்டுமே தணிக்கை செய்யப்பட வேண்டும்."
        },

        # 11. Annual General Meeting (AGM)
        {
            "subtopic": "Convening of General Body Meetings - Article 243ZN",
            "stem_en": "Under Article 243ZN, within what timeframe must the Annual General Body Meeting (AGM) of every co-operative society be convened?",
            "stem_ta": "சரத்து 243ZN-ன் கீழ் ஒவ்வொரு கூட்டுறவு சங்கத்தின் வருடாந்திர பொதுக்குழு கூட்டம் (AGM) எந்த காலக்கெடுவுக்குள் கூட்டப்பட வேண்டும்?",
            "options": [
                ("Within 6 months of the close of the financial year", "நிதியாண்டு முடிந்த 6 மாத காலத்திற்குள்"),
                ("Within 3 months of the close of the financial year", "நிதியாண்டு முடிந்த 3 மாத காலத்திற்குள்"),
                ("Within 12 months of the close of the financial year", "நிதியாண்டு முடிந்த 12 மாத காலத்திற்குள்"),
                ("Within 45 days of the close of the financial year", "நிதியாண்டு முடிந்த 45 நாட்களுக்குள்")
            ],
            "correct_key": "A",
            "exp_en": "Article 243ZN provides that every co-operative society shall convene an annual general meeting of its members within a period of 6 months of close of the financial year.",
            "exp_ta": "சரத்து 243ZN ஒவ்வொரு கூட்டுறவு சங்கமும் நிதியாண்டு முடிவடைந்த 6 மாத காலத்திற்குள் அதன் உறுப்பினர்களின் வருடாந்திர பொதுக்குழு கூட்டத்தைக் கூட்ட வேண்டும் என்று கூறுகிறது.",
            "why_a_en": "Correct. AGM must be convened within 6 months of financial year close.",
            "why_a_ta": "சரி. நிதியாண்டு முடிந்த 6 மாதங்களுக்குள் AGM கூட்டப்பட வேண்டும்.",
            "why_b_en": "Incorrect. 3 months is not the constitutional limit.",
            "why_b_ta": "தவறு. 3 மாதங்கள் அரசியலமைப்பு வரம்பு அல்ல.",
            "why_c_en": "Incorrect. 12 months would defeat the purpose of timely democratic accountability.",
            "why_c_ta": "தவறு. 12 மாதங்கள் ஜனநாயகக் கணக்குப்பொறுப்பை தாமதப்படுத்தும்.",
            "why_d_en": "Incorrect. 45 days is too short.",
            "why_d_ta": "தவறு. 45 நாட்கள் மிகக் குறுகிய காலம்.",
            "tip_en": "Remember the '6-Month Rule' across Part IX-B: Supersession max 6 months, Audit within 6 months, AGM within 6 months, Returns filing within 6 months.",
            "tip_ta": "பகுதி IX-B-ல் '6 மாத விதியை' நினைவில் கொள்க: இடைநீக்கம் அதிகபட்சம் 6 மாதங்கள், தணிக்கை 6 மாதங்களுக்குள், AGM 6 மாதங்களுக்குள், கணக்கு விவரம் தாக்கல் 6 மாதங்களுக்குள்.",
            "fact_en": "Failure to hold AGM within the stipulated time is an offence under Article 243ZQ.",
            "fact_ta": "குறிப்பிட்ட காலத்திற்குள் AGM நடத்தத் தவறுவது சரத்து 243ZQ-ன் கீழ் குற்றமாகும்."
        },

        # 12. Filing of Returns
        {
            "subtopic": "Filing of Returns - Article 243ZP",
            "stem_en": "Within what period from the close of each financial year must every co-operative society file its annual returns with the Registrar under Article 243ZP?",
            "stem_ta": "சரத்து 243ZP-ன் கீழ் ஒவ்வொரு கூட்டுறவு சங்கமும் ஒவ்வொரு நிதியாண்டும் முடிந்த எத்தனை காலத்திற்குள் தனது வருடாந்திர கணக்கு விவரங்களை (ரிட்டர்ன்கள்) பதிவாளரிடம் தாக்கல் செய்ய வேண்டும்?",
            "options": [
                ("Within 6 months", "6 மாதங்களுக்குள்"),
                ("Within 1 month", "1 மாதத்திற்குள்"),
                ("Within 3 months", "3 மாதங்களுக்குள்"),
                ("Within 9 months", "9 மாதங்களுக்குள்")
            ],
            "correct_key": "A",
            "exp_en": "Article 243ZP specifies that every co-operative society shall file returns, within 6 months of the close of every financial year, to the authority designated by the State Government.",
            "exp_ta": "சரத்து 243ZP ஒவ்வொரு கூட்டுறவு சங்கமும் ஒவ்வொரு நிதியாண்டும் முடிந்த 6 மாதங்களுக்குள் மாநில அரசால் நியமிக்கப்பட்ட அதிகாரியிடம் வருடாந்திர விவரங்களைத் தாக்கல் செய்ய வேண்டும் என்று குறிப்பிடுகிறது.",
            "why_a_en": "Correct. Returns must be filed within 6 months.",
            "why_a_ta": "சரி. 6 மாதங்களுக்குள் விவரங்கள் தாக்கல் செய்யப்பட வேண்டும்.",
            "why_b_en": "Incorrect. 1 month is too short.",
            "why_b_ta": "தவறு. 1 மாதம் மிகக் குறைவு.",
            "why_c_en": "Incorrect. 3 months is not the constitutional requirement.",
            "why_c_ta": "தவறு. 3 மாதங்கள் அரசியலமைப்புத் தேவை அல்ல.",
            "why_d_en": "Incorrect. 9 months is not the timeframe.",
            "why_d_ta": "தவறு. 9 மாதங்கள் காலக்கெடு அல்ல.",
            "tip_en": "Returns include: annual report of activities, audited accounts statement, plan for surplus disposal, list of amendment to by-laws, and declaration regarding election.",
            "tip_ta": "தாக்கல் செய்ய வேண்டியவை: ஆண்டறிக்கை, தணிக்கை செய்யப்பட்ட கணக்குகள், உபரி பகிர்வுத் திட்டம், துணைவிதிகள் திருத்தப் பட்டியல் மற்றும் தேர்தல் அறிவிப்பு.",
            "fact_en": "Failure to file returns is punishable under Article 243ZQ.",
            "fact_ta": "விவரங்களை தாக்கல் செய்யத் தவறுவது சரத்து 243ZQ-ன் கீழ் தண்டனைக்குரியது."
        },

        # 13. Application to Union Territories
        {
            "subtopic": "Application to Union Territories - Article 243ZS",
            "stem_en": "Under Article 243ZS, who has the constitutional authority to direct that Part IX-B shall apply to a Union Territory subject to specified modifications?",
            "stem_ta": "சரத்து 243ZS-ன் கீழ், பகுதி IX-B ஆனது குறிப்பிட்ட மாற்றங்களுக்கு உட்பட்டு ஒரு யூனியன் பிரதேசத்திற்குப் பொருந்தும் என்று உத்தரவிடும் அரசியலமைப்பு அதிகாரம் யாருக்கு உள்ளது?",
            "options": [
                ("The President of India", "இந்தியக் குடியரசுத் தலைவர்"),
                ("The Lieutenant Governor", "துணைநிலை ஆளுநர்"),
                ("The Union Minister of Cooperation", "மத்திய கூட்டுறவு அமைச்சர்"),
                ("The Chief Minister of the Union Territory", "யூனியன் பிரதேச முதலமைச்சர்")
            ],
            "correct_key": "A",
            "exp_en": "Article 243ZS provides that the provisions of Part IX-B shall apply to Union Territories, and the President may, by public notification, direct that they apply subject to such exceptions and modifications as specified.",
            "exp_ta": "சரத்து 243ZS பகுதி IX-B-ன் விதிகள் யூனியன் பிரதேசங்களுக்குப் பொருந்தும் என்றும், குடியரசுத் தலைவர் பொது அறிவிக்கையின் மூலம் குறிப்பிட்ட விலக்குகள் மற்றும் மாற்றங்களுடன் அவை பொருந்தும் என்று உத்தரவிடலாம் என்றும் கூறுகிறது.",
            "why_a_en": "Correct. The President issues notifications for applying Part IX-B to Union Territories.",
            "why_a_ta": "சரி. யூனியன் பிரதேசங்களுக்கு பகுதி IX-B-ஐப் பயன்படுத்துவதற்கான அறிவிக்கைகளைக் குடியரசுத் தலைவர் வெளியிடுகிறார்.",
            "why_b_en": "Incorrect. LG is an administrator who acts on President's behalf, but the constitutional power lies with the President.",
            "why_b_ta": "தவறு. துணைநிலை ஆளுநர் குடியரசுத் தலைவரின் சார்பாகச் செயல்படும் நிர்வாகி ஆவார்.",
            "why_c_en": "Incorrect. Executive minister has no direct constitutional notification power.",
            "why_c_ta": "தவறு. அமைச்சருக்கு நேரடி அரசியலமைப்பு அறிவிக்கை அதிகாரம் இல்லை.",
            "why_d_en": "Incorrect. CM does not issue presidential notifications under 243ZS.",
            "why_d_ta": "தவறு. முதலமைச்சர் குடியரசுத் தலைவர் அறிவிக்கைகளை வெளியிடுவதில்லை.",
            "tip_en": "Parallel provisions: Article 243L (Panchayats to UTs by President), Article 243ZB (Municipalities to UTs by President), Article 243ZS (Cooperatives to UTs by President).",
            "tip_ta": "ஒரே மாதிரியான விதிகள்: 243L (பஞ்சாயத்துகள்), 243ZB (நகராட்சிகள்), 243ZS (கூட்டுறவுகள்) - அனைத்திலும் குடியரசுத் தலைவரே அறிவிக்கிறார்.",
            "fact_en": "The Supreme Court in the 2021 judgment upheld Part IX-B for all Union Territories.",
            "fact_ta": "2021 தீர்ப்பில் உச்ச நீதிமன்றம் அனைத்து யூனியன் பிரதேசங்களுக்கும் பகுதி IX-B செல்லும் என உறுதி செய்தது."
        },

        # 14. First Cooperative Legislation in India
        {
            "subtopic": "Historical Evolution - Colonial Era",
            "stem_en": "Which was the first formal cooperative legislation enacted in India, and under whose viceroyalty was it passed?",
            "stem_ta": "இந்தியாவில் இயற்றப்பட்ட முதல் முறையான கூட்டுறவுச் சட்டம் எது, மற்றும் யாருடைய அரசப்பிரதிநிதித்துவத்தின் (வைஸ்ராய்) கீழ் அது நிறைவேற்றப்பட்டது?",
            "options": [
                ("Cooperative Credit Societies Act, 1904 under Lord Curzon", "கர்சன் பிரபுவின் கீழ் 1904-ஆம் ஆண்டின் கூட்டுறவு கடன் சங்கங்கள் சட்டம்"),
                ("Cooperative Societies Act, 1912 under Lord Hardinge", "ஹார்டிங் பிரபுவின் கீழ் 1912-ஆம் ஆண்டின் கூட்டுறவு சங்கங்கள் சட்டம்"),
                ("Government of India Act, 1919 under Lord Chelmsford", "செம்ஸ்போர்டு பிரபுவின் கீழ் 1919-ஆம் ஆண்டின் இந்திய அரசுச் சட்டம்"),
                ("Multi-Unit Cooperative Societies Act, 1942 under Lord Linlithgow", "லின்லித்கோ பிரபுவின் கீழ் 1942-ஆம் ஆண்டின் பல-அலகு கூட்டுறவு சங்கங்கள் சட்டம்")
            ],
            "correct_key": "A",
            "exp_en": "The first cooperative legislation in India was the Cooperative Credit Societies Act, 1904, enacted during the viceroyalty of Lord Curzon based on the recommendations of the Sir Edward Law Committee.",
            "exp_ta": "இந்தியாவின் முதல் கூட்டுறவுச் சட்டம் சர் எட்வர்ட் லா குழுவின் பரிந்துரைகளின் அடிப்படையில் கர்சன் பிரபுவின் ஆட்சிக் காலத்தில் இயற்றப்பட்ட 1904-ஆம் ஆண்டின் கூட்டுறவு கடன் சங்கங்கள் சட்டம் ஆகும்.",
            "why_a_en": "Correct. 1904 Act under Lord Curzon was the pioneer cooperative law.",
            "why_a_ta": "சரி. கர்சன் பிரபுவின் கீழ் இயற்றப்பட்ட 1904 சட்டம் முதல் கூட்டுறவுச் சட்டமாகும்.",
            "why_b_en": "Incorrect. 1912 Act was the second legislation, expanding to non-credit societies.",
            "why_b_ta": "தவறு. 1912 சட்டம் இரண்டாவது சட்டம், இது கடன் சாரா சங்கங்களுக்கும் விரிவுபடுத்தப்பட்டது.",
            "why_c_en": "Incorrect. 1919 Act transferred cooperation to provinces.",
            "why_c_ta": "தவறு. 1919 சட்டம் கூட்டுறவை மாகாணங்களுக்கு மாற்றியது.",
            "why_d_en": "Incorrect. 1942 Act covered multi-unit societies across provincial borders.",
            "why_d_ta": "தவறு. 1942 சட்டம் மாகாண எல்லைகளைத் தாண்டிய சங்கங்களை உள்ளடக்கியது.",
            "tip_en": "Sir Frederick Nicholson was sent to Europe in 1892 by the Madras Government; his famous report concluded: 'Find Raiffeisen'.",
            "tip_ta": "1892-ல் மெட்ராஸ் அரசால் ஐரோப்பாவிற்கு அனுப்பப்பட்ட சர் பிரடெரிக் நிக்கல்சன் தனது புகழ்பெற்ற அறிக்கையில் 'ரைஃபெய்சனைக் கண்டறியுங்கள்' (Find Raiffeisen) எனக் குறிப்பிட்டார்.",
            "fact_en": "The 1904 Act applied only to agricultural and urban credit societies, not non-credit societies.",
            "fact_ta": "1904 சட்டம் வேளாண் மற்றும் நகர்ப்புற கடன் சங்கங்களுக்கு மட்டுமே பொருந்தியது, கடன் சாரா சங்கங்களுக்கு அல்ல."
        },

        # 15. Cooperative Societies Act, 1912
        {
            "subtopic": "Historical Evolution - Colonial Era",
            "stem_en": "What was the major breakthrough introduced by the Cooperative Societies Act, 1912 compared to the 1904 Act?",
            "stem_ta": "1904-ஆம் ஆண்டு சட்டத்துடன் ஒப்பிடும்போது 1912-ஆம் ஆண்டின் கூட்டுறவு சங்கங்கள் சட்டத்தால் அறிமுகப்படுத்தப்பட்ட முக்கிய முன்னேற்றம் என்ன?",
            "options": [
                ("It allowed the registration of non-credit societies, central banks, and federations", "இது கடன் சாரா சங்கங்கள், மத்திய வங்கிகள் மற்றும் கூட்டமைப்புகளைப் பதிவு செய்ய அனுமதித்தது"),
                ("It abolished state supervision over cooperatives", "இது கூட்டுறவுகள் மீதான அரசின் மேற்பார்வையை ஒழித்தது"),
                ("It made cooperation a Central subject", "இது கூட்டுறவை ஒரு மத்தியப் பாடமாக மாற்றியது"),
                ("It restricted membership only to landowners", "இது நில உரிமையாளர்களுக்கு மட்டுமே உறுப்பினர் சேர்க்கையைக் கட்டுப்படுத்தியது")
            ],
            "correct_key": "A",
            "exp_en": "The Cooperative Societies Act, 1912 rectified the shortcomings of the 1904 Act by allowing registration of non-credit societies (marketing, consumer, housing) and facilitating higher-tier secondary bodies like central cooperative banks and federations.",
            "exp_ta": "1912-ஆம் ஆண்டின் கூட்டுறவு சங்கங்கள் சட்டம் கடன் சாரா சங்கங்களை (விற்பனை, நுகர்வோர், வீட்டுவசதி) பதிவு செய்ய அனுமதிப்பதன் மூலமும், மத்திய கூட்டுறவு வங்கிகள் மற்றும் கூட்டமைப்புகள் போன்ற உயர் அடுக்கு அமைப்புகளை உருவாக்குவதன் மூலமும் 1904 சட்டத்தின் குறைபாடுகளைச் சரிசெய்தது.",
            "why_a_en": "Correct. 1912 Act introduced non-credit societies and cooperative federations.",
            "why_a_ta": "சரி. 1912 சட்டம் கடன் சாரா சங்கங்கள் மற்றும் கூட்டுறவுக் கூட்டமைப்புகளை அறிமுகப்படுத்தியது.",
            "why_b_en": "Incorrect. State control through the Registrar was retained and strengthened.",
            "why_b_ta": "தவறு. பதிவாளர் மூலமான அரசின் கட்டுப்பாடு தக்கவைக்கப்பட்டு பலப்படுத்தப்பட்டது.",
            "why_c_en": "Incorrect. It remained under general regulation, not converted to exclusive central subject.",
            "why_c_ta": "தவறு. இது பிரத்யேக மத்தியப் பாடமாக மாற்றப்படவில்லை.",
            "why_d_en": "Incorrect. Membership was not restricted to landowners.",
            "why_d_ta": "தவறு. உறுப்பினர் சேர்க்கை நில உரிமையாளர்களுக்கு மட்டும் கட்டுப்படுத்தப்படவில்லை.",
            "tip_en": "1904 Act = Credit only; 1912 Act = Credit + Non-credit + Central Banks / Federations.",
            "tip_ta": "1904 சட்டம் = கடன் சங்கங்கள் மட்டுமே; 1912 சட்டம் = கடன் + கடன் சாரா சங்கங்கள் + மத்திய வங்கிகள்/கூட்டமைப்புகள்.",
            "fact_en": "The 1912 Act classified societies into limited liability and unlimited liability societies.",
            "fact_ta": "1912 சட்டம் சங்கங்களை வரையறுக்கப்பட்ட பொறுப்பு மற்றும் வரையறுக்கப்படாத பொறுப்பு சங்கங்கள் என வகைப்படுத்தியது."
        },

        # 16. Devolution of Cooperation to Provinces (1919)
        {
            "subtopic": "Historical Evolution - Constitutional Devolution",
            "stem_en": "Under which landmark constitutional reform was 'Cooperation' made a 'Transferred' subject administered by Indian ministers in the Provinces?",
            "stem_ta": "எந்த முக்கிய அரசியலமைப்புச் சீர்திருத்தத்தின் கீழ் 'கூட்டுறவு' என்பது மாகாணங்களில் இந்திய அமைச்சர்களால் நிர்வகிக்கப்படும் ஒரு 'மாற்றப்பட்ட' (Transferred) பாடமாக மாற்றப்பட்டது?",
            "options": [
                ("Government of India Act, 1919 (Montagu-Chelmsford Reforms)", "1919-ஆம் ஆண்டின் இந்திய அரசுச் சட்டம் (மாண்டேகு-செம்ஸ்போர்டு சீர்திருத்தங்கள்)"),
                ("Morley-Minto Reforms, 1909", "1909-ஆம் ஆண்டின் மார்லி-மிண்டோ சீர்திருத்தங்கள்"),
                ("Government of India Act, 1935", "1935-ஆம் ஆண்டின் இந்திய அரசுச் சட்டம்"),
                ("Indian Independence Act, 1947", "1947-ஆம் ஆண்டின் இந்திய சுதந்திரச் சட்டம்")
            ],
            "correct_key": "A",
            "exp_en": "Under the Government of India Act, 1919, dyarchy was introduced in the Provinces and 'Cooperation' was placed in the Transferred List under the charge of an elected Indian Minister.",
            "exp_ta": "1919-ஆம் ஆண்டின் இந்திய அரசுச் சட்டத்தின் கீழ், மாகாணங்களில் இரட்டை ஆட்சி அறிமுகப்படுத்தப்பட்டது மற்றும் 'கூட்டுறவு' தேர்ந்தெடுக்கப்பட்ட இந்திய அமைச்சரின் பொறுப்பில் 'மாற்றப்பட்ட பாடங்கள்' பட்டியலில் வைக்கப்பட்டது.",
            "why_a_en": "Correct. Montagu-Chelmsford Reforms (1919) transferred cooperation to provincial ministers.",
            "why_a_ta": "சரி. மாண்டேகு-செம்ஸ்போர்டு சீர்திருத்தங்கள் (1919) கூட்டுறவை மாகாண அமைச்சர்களுக்கு மாற்றியது.",
            "why_b_en": "Incorrect. Morley-Minto reforms did not introduce dyarchy or transferred subjects.",
            "why_b_ta": "தவறு. மார்லி-மிண்டோ சீர்திருத்தங்கள் இரட்டை ஆட்சியை அறிமுகப்படுத்தவில்லை.",
            "why_c_en": "Incorrect. 1935 Act introduced Provincial Autonomy, but transfer first happened in 1919.",
            "why_c_ta": "தவறு. 1935 சட்டம் மாகாண தன்னாட்சியை அறிமுகப்படுத்தியது, ஆனால் மாற்றம் முதலில் 1919-ல் நிகழ்ந்தது.",
            "why_d_en": "Incorrect. 1947 Act partitioned and granted independence to India.",
            "why_d_ta": "தவறு. 1947 சட்டம் இந்தியாவிற்கு சுதந்திரம் வழங்கியது.",
            "tip_en": "Following the 1919 Act, Bombay became the first province to pass its own Cooperative Societies Act in 1925.",
            "tip_ta": "1919 சட்டத்தைத் தொடர்ந்து, 1925-ல் பம்பாய் தனது சொந்த கூட்டுறவு சங்கங்கள் சட்டத்தை இயற்றிய முதல் மாகாணமானது.",
            "fact_en": "Madras Province enacted the Madras Co-operative Societies Act in 1932.",
            "fact_ta": "மெட்ராஸ் மாகாணம் 1932-ல் மெட்ராஸ் கூட்டுறவு சங்கங்கள் சட்டத்தை இயற்றியது."
        },

        # 17. Seventh Schedule List II Entry 32
        {
            "subtopic": "Federal Distribution of Powers",
            "stem_en": "Under which Entry of the State List (List II) in the Seventh Schedule of the Indian Constitution does 'Co-operative Societies' fall?",
            "stem_ta": "இந்திய அரசியலமைப்பின் ஏழாவது அட்டவணையில் உள்ள மாநிலப் பட்டியலில் (பட்டியல் II) எந்தப் பதிவின் கீழ் 'கூட்டுறவு சங்கங்கள்' வருகின்றன?",
            "options": [
                ("Entry 32 of List II", "பட்டியல் II-ன் பதிவு 32"),
                ("Entry 44 of List I", "பட்டியல் I-ன் பதிவு 44"),
                ("Entry 43 of List I", "பட்டியல் I-ன் பதிவு 43"),
                ("Entry 33 of List III", "பட்டியல் III-ன் பதிவு 33")
            ],
            "correct_key": "A",
            "exp_en": "Seventh Schedule List II Entry 32 covers: 'Incorporation, regulation and winding up of corporations, other than those specified in List I, and universities; unincorporated trading, literary, scientific, religious and other societies and associations; co-operative societies.'",
            "exp_ta": "ஏழாவது அட்டவணை பட்டியல் II பதிவு 32: பட்டியல் I-ல் குறிப்பிடப்பட்டுள்ளவை தவிர பிற கூட்டு நிறுவனங்கள், பல்கலைக்கழகங்கள், வர்த்தக, இலக்கிய, அறிவியல், மத மற்றும் பிற சங்கங்கள்; கூட்டுறவு சங்கங்களின் அமைப்பாக்கம், ஒழுங்குமுறை மற்றும் கலைத்தல் ஆகியவற்றைக் குறிக்கிறது.",
            "why_a_en": "Correct. Entry 32 of List II gives States exclusive power over cooperative societies.",
            "why_a_ta": "சரி. பட்டியல் II-ன் பதிவு 32 கூட்டுறவு சங்கங்கள் மீது மாநிலங்களுக்கு முழுமையான அதிகாரத்தை அளிக்கிறது.",
            "why_b_en": "Incorrect. Entry 44 of List I covers Multi-State corporations/cooperatives.",
            "why_b_ta": "தவறு. பட்டியல் I-ன் பதிவு 44 பல்மாநில கூட்டுறவுகளை உள்ளடக்கியது.",
            "why_c_en": "Incorrect. Entry 43 of List I covers trading corporations (Union List).",
            "why_c_ta": "தவறு. பட்டியல் I-ன் பதிவு 43 வர்த்தகக் கூட்டு நிறுவனங்களைக் கையாள்கிறது.",
            "why_d_en": "Incorrect. Entry 33 of List III covers trade and commerce in products of scheduled industries.",
            "why_d_ta": "தவறு. பட்டியல் III-ன் பதிவு 33 பொதுப்பட்டியலில் உள்ள வர்த்தகம் பற்றியது.",
            "tip_en": "Single-State Cooperatives = List II Entry 32 (State List); Multi-State Cooperatives = List I Entry 44 (Union List).",
            "tip_ta": "ஒற்றை மாநில கூட்டுறவுகள் = பட்டியல் II பதிவு 32; பல்மாநில கூட்டுறவுகள் = பட்டியல் I பதிவு 44.",
            "fact_en": "This entry was the focal point of the Supreme Court judgment striking down Part IX-B for State cooperatives in 2021.",
            "fact_ta": "2021-ல் மாநில கூட்டுறவுகளுக்கான பகுதி IX-B-ஐ ரத்து செய்த உச்ச நீதிமன்றத் தீர்ப்பின் மையப்புள்ளி இந்தப் பதிவே ஆகும்."
        },

        # 18. Multi-State Cooperative Societies Legislative Entry
        {
            "subtopic": "Federal Distribution of Powers",
            "stem_en": "Under which Entry of the Union List (List I) does the Parliament of India have the exclusive power to legislate for Multi-State Co-operative Societies?",
            "stem_ta": "பல்மாநில கூட்டுறவு சங்கங்களுக்குச் சட்டம் இயற்றுவதற்கு இந்திய நாடாளுமன்றத்திற்கு எந்த மத்தியப் பட்டியல் (பட்டியல் I) பதிவின் கீழ் பிரத்யேக அதிகாரம் உள்ளது?",
            "options": [
                ("Entry 44 of List I", "பட்டியல் I-ன் பதிவு 44"),
                ("Entry 32 of List II", "பட்டியல் II-ன் பதிவு 32"),
                ("Entry 43 of List I", "பட்டியல் I-ன் பதிவு 43"),
                ("Entry 45 of List I", "பட்டியல் I-ன் பதிவு 45")
            ],
            "correct_key": "A",
            "exp_en": "Entry 44 of List I in the Seventh Schedule deals with 'Incorporation, regulation and winding up of corporations, whether trading or not, with objects not confined to one State, but not including universities'.",
            "exp_ta": "ஏழாவது அட்டவணையில் உள்ள பட்டியல் I-ன் பதிவு 44, 'ஒரு மாநிலத்திற்குள் மட்டும் வரையறுக்கப்படாத நோக்கங்களைக் கொண்ட, வர்த்தக அல்லது வர்த்தகமற்ற கூட்டு நிறுவனங்கள் (பல்கலைக்கழகங்கள் நீங்கலாக) ஆகியவற்றின் அமைப்பாக்கம், ஒழுங்குமுறை மற்றும் கலைத்தல்' ஆகியவற்றைக் கையாள்கிறது.",
            "why_a_en": "Correct. Entry 44 covers corporations and cooperatives with objects extending beyond one State.",
            "why_a_ta": "சரி. பதிவு 44 ஒரு மாநிலத்திற்கு மேல் செயல்படும் கூட்டுறவுகள் மற்றும் நிறுவனங்களைக் கையாள்கிறது.",
            "why_b_en": "Incorrect. Entry 32 of List II covers state-level cooperatives.",
            "why_b_ta": "தவறு. பட்டியல் II-ன் பதிவு 32 மாநில அளவிலான கூட்டுறவுகளை உள்ளடக்கியது.",
            "why_c_en": "Incorrect. Entry 43 covers trading corporations within Union territory or overall.",
            "why_c_ta": "தவறு. பதிவு 43 பொது வர்த்தக நிறுவனங்களைக் குறிக்கிறது.",
            "why_d_en": "Incorrect. Entry 45 of List I covers Banking.",
            "why_d_ta": "தவறு. பட்டியல் I-ன் பதிவு 45 வங்கித் தொழிலைக் கையாள்கிறது.",
            "tip_en": "Multi-State Cooperatives Act, 2002 was enacted by Parliament using Entry 44.",
            "tip_ta": "2002-ஆம் ஆண்டின் பல்மாநில கூட்டுறவு சங்கங்கள் சட்டம் பதிவு 44-ஐப் பயன்படுத்தி நாடாளுமன்றத்தால் இயற்றப்பட்டது.",
            "fact_en": "The Supreme Court in 2021 held that Part IX-B remains operative for Multi-State cooperatives under Entry 44.",
            "fact_ta": "பதிவு 44-ன் கீழ் பல்மாநில கூட்டுறவுகளுக்கு பகுதி IX-B தொடர்ந்து செயல்படும் என்று 2021-ல் உச்ச நீதிமன்றம் தீர்ப்பளித்தது."
        },

        # 19. Creation of Ministry of Cooperation
        {
            "subtopic": "Institutional Framework - Union Ministry",
            "stem_en": "In which year was a separate Union Ministry of Cooperation created by the Government of India to realize the vision of 'Sahakar Se Samriddhi'?",
            "stem_ta": "'கூட்டுறவு மூலம் செழிப்பு' (Sahakar Se Samriddhi) என்ற தொலைநோக்குப் பார்வையை நனவாக்குவதற்காக இந்திய அரசால் எந்த ஆண்டு தனியாக மத்திய கூட்டுறவு அமைச்சகம் உருவாக்கப்பட்டது?",
            "options": [
                ("July 2021", "ஜூலை 2021"),
                ("January 2019", "ஜனவரி 2019"),
                ("August 2014", "ஆகஸ்ட் 2014"),
                ("December 2022", "டிசம்பர் 2022")
            ],
            "correct_key": "A",
            "exp_en": "On 6th July 2021, the Government of India created a separate Ministry of Cooperation, carved out from the Department of Agriculture, Cooperation and Farmers Welfare, to strengthen the cooperative movement.",
            "exp_ta": "கூட்டுறவு இயக்கத்தை வலுப்படுத்துவதற்காக, வேளாண்மை, கூட்டுறவு மற்றும் விவசாயிகள் நலத் துறையிலிருந்து பிரித்து 2021 ஜூலை 6 அன்று இந்திய அரசால் தனி கூட்டுறவு அமைச்சகம் உருவாக்கப்பட்டது.",
            "why_a_en": "Correct. Ministry of Cooperation was established in July 2021.",
            "why_a_ta": "சரி. கூட்டுறவு அமைச்சகம் ஜூலை 2021-ல் நிறுவப்பட்டது.",
            "why_b_en": "Incorrect. In 2019, Department of Fisheries was created.",
            "why_b_ta": "தவறு. 2019-ல் மீன்வளத்துறை உருவாக்கப்பட்டது.",
            "why_c_en": "Incorrect. In 2014, Ministry of Skill Development was created.",
            "why_c_ta": "தவறு. 2014-ல் திறன் மேம்பாட்டு அமைச்சகம் உருவாக்கப்பட்டது.",
            "why_d_en": "Incorrect. 2022 is incorrect.",
            "why_d_ta": "தவறு. 2022 தவறானது.",
            "tip_en": "Motto of the Ministry of Cooperation: 'Sahakar Se Samriddhi' (Prosperity through Cooperation).",
            "tip_ta": "கூட்டுறவு அமைச்சகத்தின் குறிக்கோள்: 'சககார் சே சம்ரிதி' (கூட்டுறவு மூலம் செழிப்பு).",
            "fact_en": "Shri Amit Shah was appointed as India's first Union Minister of Cooperation.",
            "fact_ta": "திரு. அமித் ஷா இந்தியாவின் முதல் மத்திய கூட்டுறவு அமைச்சராக நியமிக்கப்பட்டார்."
        },

        # 20. First Consumer Cooperative in India (TUCS)
        {
            "subtopic": "Tamil Nadu Cooperative History",
            "stem_en": "Which historic cooperative society, established in Madras in 1904, is recognized as the first consumer co-operative society in India?",
            "stem_ta": "1904-ல் சென்னையில் நிறுவப்பட்ட எந்த வரலாற்றுச் சிறப்புமிக்க கூட்டுறவு சங்கம் இந்தியாவின் முதல் நுகர்வோர் கூட்டுறவு சங்கமாக அங்கீகரிக்கப்பட்டுள்ளது?",
            "options": [
                ("Triplicane Urban Co-operative Society (TUCS)", "திருவல்லிக்கேணி நகரக் கூட்டுறவு சங்கம் (TUCS)"),
                ("Madras Central Co-operative Bank", "மெட்ராஸ் மத்திய கூட்டுறவு வங்கி"),
                ("Co-optex", "கோ-ஆப்டெக்ஸ்"),
                ("Tirur Agricultural Credit Society", "திருவூர் விவசாயக் கடன் சங்கம்")
            ],
            "correct_key": "A",
            "exp_en": "The Triplicane Urban Co-operative Society (TUCS), established on 9th April 1904 in Triplicane, Madras, is the oldest and first consumer cooperative society in India.",
            "exp_ta": "1904 ஏப்ரல் 9 அன்று மெட்ராஸ் திருவல்லிக்கேணியில் நிறுவப்பட்ட திருவல்லிக்கேணி நகரக் கூட்டுறவு சங்கம் (TUCS) இந்தியாவின் மிகப் பழமையான மற்றும் முதல் நுகர்வோர் கூட்டுறவு சங்கமாகும்.",
            "why_a_en": "Correct. TUCS is the first consumer cooperative in India.",
            "why_a_ta": "சரி. TUCS இந்தியாவின் முதல் நுகர்வோர் கூட்டுறவு சங்கமாகும்.",
            "why_b_en": "Incorrect. Madras Central Cooperative Bank was founded later in 1906.",
            "why_b_ta": "தவறு. மெட்ராஸ் மத்திய கூட்டுறவு வங்கி பின்னர் 1906-ல் நிறுவப்பட்டது.",
            "why_c_en": "Incorrect. Co-optex (Handloom apex) was formed in 1935.",
            "why_c_ta": "தவறு. கோ-ஆப்டெக்ஸ் (கைத்தறி சங்கம்) 1935-ல் உருவாக்கப்பட்டது.",
            "why_d_en": "Incorrect. Tirur was the first primary agricultural credit cooperative in Madras (1904).",
            "why_d_ta": "தவறு. திருவூர் என்பது முதல் தொடக்க வேளாண் கடன் கூட்டுறவு சங்கமாகும் (1904).",
            "tip_en": "TUCS pioneered consumer cooperatives and public distribution through cooperatives in Tamil Nadu.",
            "tip_ta": "TUCS தமிழ்நாட்டில் நுகர்வோர் கூட்டுறவு மற்றும் நியாயவிலைக் கடை விநியோகத்தில் முன்னோடியாகத் திகழ்ந்தது.",
            "fact_en": "TUCS was registered under the Cooperative Credit Societies Act, 1904.",
            "fact_ta": "TUCS 1904-ஆம் ஆண்டின் கூட்டுறவு கடன் சங்கங்கள் சட்டத்தின் கீழ் பதிவு செய்யப்பட்டது."
        },

        # 21. First Agricultural Credit Society in Tamil Nadu
        {
            "subtopic": "Tamil Nadu Cooperative History",
            "stem_en": "In which village of Tiruvallur district was the first agricultural cooperative credit society in the Madras Presidency registered in 1904?",
            "stem_ta": "1904-ஆம் ஆண்டில் மெட்ராஸ் மாகாணத்தின் முதல் விவசாயக் கூட்டுறவுக் கடன் சங்கம் திருவள்ளூர் மாவட்டத்தின் எந்த கிராமத்தில் பதிவு செய்யப்பட்டது?",
            "options": [
                ("Tirur", "திருவூர்"),
                ("Ponneri", "பொன்னேரி"),
                ("Uthiramerur", "உத்திரமேரூர்"),
                ("Avadi", "ஆவடி")
            ],
            "correct_key": "A",
            "exp_en": "The first Primary Agricultural Cooperative Credit Society (PACS) in Tamil Nadu (Madras Presidency) was registered at Tirur village in Tiruvallur district in 1904.",
            "exp_ta": "தமிழ்நாட்டில் (மெட்ராஸ் மாகாணம்) முதல் தொடக்க வேளாண்மைக் கூட்டுறவுக் கடன் சங்கம் (PACS) 1904-ல் திருவள்ளூர் மாவட்டத்திலுள்ள திருவூர் கிராமத்தில் பதிவு செய்யப்பட்டது.",
            "why_a_en": "Correct. Tirur was the pioneer village agricultural cooperative in Madras Presidency.",
            "why_a_ta": "சரி. திருவூர் மெட்ராஸ் மாகாணத்தின் முன்னோடி கிராமக் கூட்டுறவு சங்கமாகும்.",
            "why_b_en": "Incorrect. Ponneri is a taluk in Tiruvallur, not the village of first registration.",
            "why_b_ta": "தவறு. பொன்னேரி திருவள்ளூரின் ஒரு தாலுகா, முதல் சங்கத்தின் கிராமம் அல்ல.",
            "why_c_en": "Incorrect. Uthiramerur is famous for ancient local governance inscriptions (Chola era).",
            "why_c_ta": "தவறு. உத்திரமேரூர் சோழர் கால உள்ளாட்சித் தேர்தல் கல்வெட்டுகளுக்குப் புகழ்பெற்றது.",
            "why_d_en": "Incorrect. Avadi is an industrial township.",
            "why_d_ta": "தவறு. ஆவடி ஒரு தொழிற்பேட்டை நகரம்.",
            "tip_en": "Tirur = First Rural Credit Society (1904); TUCS Triplicane = First Urban Consumer Society (1904).",
            "tip_ta": "திருவூர் = முதல் கிராமக் கடன் சங்கம் (1904); TUCS = முதல் நகர்ப்புற நுகர்வோர் சங்கம் (1904).",
            "fact_en": "Tamil Nadu has a rich cooperative heritage spanning over 120 years.",
            "fact_ta": "தமிழ்நாடு 120 ஆண்டுகளுக்கும் மேலான வளமான கூட்டுறவு பாரம்பரியத்தைக் கொண்டுள்ளது."
        },

        # 22. Definition of Co-operative Society (243ZH)
        {
            "subtopic": "Definitions - Article 243ZH",
            "stem_en": "Under Article 243ZH(a), how is a 'co-operative society' defined in Part IX-B of the Indian Constitution?",
            "stem_ta": "சரத்து 243ZH(a)-ன் கீழ், இந்திய அரசியலமைப்பின் பகுதி IX-B-ல் 'கூட்டுறவு சங்கம்' எவ்வாறு வரையறுக்கப்படுகிறது?",
            "options": [
                ("A society registered or deemed to be registered under any law relating to co-operative societies for the time being in force in any State", "ஏதேனும் ஒரு மாநிலத்தில் நடைமுறையில் உள்ள கூட்டுறவு சங்கங்கள் தொடர்பான சட்டத்தின் கீழ் பதிவு செய்யப்பட்ட அல்லது பதிவு செய்யப்பட்டதாகக் கருதப்படும் ஒரு சங்கம்"),
                ("A society financed exclusively by the Central Government", "மத்திய அரசால் மட்டுமே முழுமையாக நிதி அளிக்கப்படும் ஒரு சங்கம்"),
                ("A company incorporated under the Companies Act with limited profit motives", "குறைந்த லாப நோக்கத்துடன் நிறுவனங்கள் சட்டத்தின் கீழ் பதிவு செய்யப்பட்ட ஒரு நிறுவனம்"),
                ("A trade union registered under the Trade Unions Act, 1926", "தொழிற்சங்கங்கள் சட்டம் 1926-ன் கீழ் பதிவு செய்யப்பட்ட ஒரு தொழிற்சங்கம்")
            ],
            "correct_key": "A",
            "exp_en": "Article 243ZH(a) defines 'co-operative society' as a society registered or deemed to be registered under any law relating to co-operative societies for the time being in force in any State.",
            "exp_ta": "சரத்து 243ZH(a) 'கூட்டுறவு சங்கம்' என்பதை எந்தவொரு மாநிலத்திலும் நடைமுறையில் உள்ள கூட்டுறவு சங்கங்கள் தொடர்பான சட்டத்தின் கீழ் பதிவு செய்யப்பட்ட அல்லது பதிவு செய்யப்பட்டதாகக் கருதப்படும் ஒரு சங்கம் என வரையறுக்கிறது.",
            "why_a_en": "Correct. Verbatim constitutional definition under Article 243ZH(a).",
            "why_a_ta": "சரி. சரத்து 243ZH(a)-ன் படியான அரசியலமைப்பு வரையறை.",
            "why_b_en": "Incorrect. Central financing is not part of the definition.",
            "why_b_ta": "தவறு. மத்திய நிதி உதவி வரையறையின் பகுதி அல்ல.",
            "why_c_en": "Incorrect. Companies are governed by Companies Act, not Cooperative laws.",
            "why_c_ta": "தவறு. நிறுவனங்கள் நிறுவனச் சட்டத்தால் ஆளப்படுகின்றன.",
            "why_d_en": "Incorrect. Trade unions are distinct entities under Trade Unions Act.",
            "why_d_ta": "தவறு. தொழிற்சங்கங்கள் தொழிற்சங்கச் சட்டத்தின் கீழ் உள்ள தனி அமைப்புகள்.",
            "tip_en": "Article 243ZH is the definition clause for the entire Part IX-B.",
            "tip_ta": "சரத்து 243ZH என்பது பகுதி IX-B முழுவதற்குமான வரையறைப் பிரிவாகும்.",
            "fact_en": "Multi-state cooperative society is separately defined in Article 243ZH(c).",
            "fact_ta": "பல்மாநில கூட்டுறவு சங்கம் சரத்து 243ZH(c)-ல் தனியாக வரையறுக்கப்பட்டுள்ளது."
        },

        # 23. Definition of Board (243ZH)
        {
            "subtopic": "Definitions - Article 243ZH",
            "stem_en": "Under Article 243ZH(b), what does 'board' mean in relation to a co-operative society?",
            "stem_ta": "சரத்து 243ZH(b)-ன் கீழ், ஒரு கூட்டுறவு சங்கத்தைப் பொறுத்தவரை 'வாரியம்' (board) என்பது எதனைக் குறிக்கிறது?",
            "options": [
                ("The board of directors or the governing body of a co-operative society to which the direction and control of the management of the affairs of a society is entrusted", "சங்கத்தின் விவகாரங்களின் மேலாண்மையை இயக்குதல் மற்றும் கட்டுப்படுத்துதல் ஒப்படைக்கப்பட்டுள்ள இயக்குநர் வாரியம் அல்லது ஆளும் குழு"),
                ("The general body of all voting members", "அனைத்து வாக்களிக்கும் உறுப்பினர்களின் பொதுக்குழு"),
                ("The panel of external statutory auditors", "வெளிப்புற சட்டப்பூர்வ தணிக்கையாளர் குழு"),
                ("The Registrar and his subordinate inspectors", "பதிவாளர் மற்றும் அவரது கீழ்நிலை ஆய்வாளர்கள்")
            ],
            "correct_key": "A",
            "exp_en": "Article 243ZH(b) defines 'board' as the board of directors or the governing body of a co-operative society, by whatever name called, to which the direction and control of the management of the affairs of a society is entrusted.",
            "exp_ta": "சரத்து 243ZH(b) 'வாரியம்' என்பதை, எந்தப் பெயரால் அழைக்கப்பட்டாலும், ஒரு கூட்டுறவு சங்கத்தின் விவகாரங்களின் மேலாண்மையை இயக்குதல் மற்றும் கட்டுப்படுத்துதல் ஒப்படைக்கப்பட்டுள்ள இயக்குநர் வாரியம் அல்லது நிர்வாகக் குழு என வரையறுக்கிறது.",
            "why_a_en": "Correct. Verbatim definition under Article 243ZH(b).",
            "why_a_ta": "சரி. சரத்து 243ZH(b)-ன் படியான அரசியலமைப்பு வரையறை.",
            "why_b_en": "Incorrect. General body comprises all members; board is the elected executive body.",
            "why_b_ta": "தவறு. பொதுக்குழுவில் அனைத்து உறுப்பினர்களும் அடங்குவர்; வாரியம் தேர்ந்தெடுக்கப்பட்ட நிர்வாக அமைப்பு.",
            "why_c_en": "Incorrect. Auditors do not manage the society.",
            "why_c_ta": "தவறு. தணிக்கையாளர்கள் சங்கத்தை நிர்வகிப்பதில்லை.",
            "why_d_en": "Incorrect. Registrar represents the regulatory authority.",
            "why_d_ta": "தவறு. பதிவாளர் ஒழுங்குமுறை அதிகார அமைப்பைப் பிரதிநிதித்துவப்படுத்துகிறார்.",
            "tip_en": "Board = Governing executive body entrusted with management.",
            "tip_ta": "வாரியம் = மேலாண்மை ஒப்படைக்கப்பட்ட ஆளும் நிர்வாக அமைப்பு.",
            "fact_en": "The maximum size of the board is fixed at 21 directors under Article 243ZJ.",
            "fact_ta": "சரத்து 243ZJ-ன் கீழ் வாரியத்தின் அதிகபட்ச அளவு 21 இயக்குநர்களாக நிர்ணயிக்கப்பட்டுள்ளது."
        },

        # 24. Rochdale Principles
        {
            "subtopic": "Core Principles of Cooperation",
            "stem_en": "In which country was the famous Rochdale Society of Equitable Pioneers established in 1844, giving birth to the modern cooperative principles?",
            "stem_ta": "நவீன கூட்டுறவுக் கொள்கைகளுக்கு வித்திட்ட புகழ்பெற்ற ரோச்டேல் சமத்துவ முன்னோடிகள் சங்கம் (Rochdale Society of Equitable Pioneers) 1844-ல் எந்த நாட்டில் நிறுவப்பட்டது?",
            "options": [
                ("England (United Kingdom)", "இங்கிலாந்து (பிரிட்டன்)"),
                ("Germany", "ஜெர்மனி"),
                ("France", "பிரான்ஸ்"),
                ("United States of America", "அமெரிக்க ஐக்கிய நாடுகள்")
            ],
            "correct_key": "A",
            "exp_en": "The Rochdale Society of Equitable Pioneers was founded in 1844 in Rochdale, Lancashire, England by 28 weavers, establishing the foundational principles of modern cooperative enterprise (democratic control, open membership, limited interest on capital).",
            "exp_ta": "1844-ல் இங்கிலாந்தின் லங்காஷயரில் உள்ள ரோச்டேல் நகரில் 28 நெசவாளர்களால் ரோச்டேல் சமத்துவ முன்னோடிகள் சங்கம் நிறுவப்பட்டது; இதுவே நவீன கூட்டுறவுக் கொள்கைகளான ஜனநாயகக் கட்டுப்பாடு, திறந்த உறுப்பினர் சேர்க்கை போன்றவற்றை வகுத்தது.",
            "why_a_en": "Correct. Rochdale Pioneers were in England (1844).",
            "why_a_ta": "சரி. ரோச்டேல் முன்னோடிகள் இங்கிலாந்தைச் சேர்ந்தவர்கள் (1844).",
            "why_b_en": "Incorrect. Germany was the pioneer of credit cooperatives (Raiffeisen and Schulze-Delitzsch).",
            "why_b_ta": "தவறு. ஜெர்மனி கடன் கூட்டுறவுகளுக்கு முன்னோடியாகும் (ரைஃபெய்சன்).",
            "why_c_en": "Incorrect. France had early worker production cooperatives.",
            "why_c_ta": "தவறு. பிரான்ஸ் ஆரம்பகால தொழிலாளர் உற்பத்தி கூட்டுறவுகளைக் கொண்டிருந்தது.",
            "why_d_en": "Incorrect. USA was not the home of the Rochdale Pioneers.",
            "why_d_ta": "தவறு. அமெரிக்கா ரோச்டேல் முன்னோடிகளின் தாய்நாடு அல்ல.",
            "tip_en": "Rochdale = Consumer Cooperatives (England, 1844); Raiffeisen = Rural Credit Cooperatives (Germany, 1862).",
            "tip_ta": "ரோச்டேல் = நுகர்வோர் கூட்டுறவு (இங்கிலாந்து, 1844); ரைஃபெய்சன் = கிராமப்புற கடன் கூட்டுறவு (ஜெர்மனி, 1862).",
            "fact_en": "The International Co-operative Alliance (ICA) was formed in London in 1895.",
            "fact_ta": "சர்வதேச கூட்டுறவு கூட்டணி (ICA) 1895-ல் லண்டனில் உருவாக்கப்பட்டது."
        },

        # 25. Friedrich Wilhelm Raiffeisen
        {
            "subtopic": "Core Principles of Cooperation",
            "stem_en": "Friedrich Wilhelm Raiffeisen, who pioneered the rural cooperative credit movement studied by Sir Frederick Nicholson for India, belonged to which country?",
            "stem_ta": "இந்தியாவிற்காக சர் பிரடெரிக் நிக்கல்சனால் ஆய்வு செய்யப்பட்ட கிராமப்புற கூட்டுறவுக் கடன் இயக்கத்திற்கு முன்னோடியாகத் திகழ்ந்த பிரடெரிக் வில்ஹெல்ம் ரைஃபெய்சன் எந்த நாட்டைச் சேர்ந்தவர்?",
            "options": [
                ("Germany", "ஜெர்மனி"),
                ("England", "இங்கிலாந்து"),
                ("Denmark", "டென்மார்க்"),
                ("Switzerland", "சுவிட்சர்லாந்து")
            ],
            "correct_key": "A",
            "exp_en": "Friedrich Wilhelm Raiffeisen pioneered rural cooperative credit societies in Germany in the 1860s based on unlimited liability, small area of operation, and mutual self-help among poor farmers.",
            "exp_ta": "பிரடெரிக் வில்ஹெல்ம் ரைஃபெய்சன் 1860-களில் ஜெர்மனியில் ஏழை விவசாயிகளிடையே வரம்பற்ற பொறுப்பு, சிறிய செயல்பாட்டுப் பகுதி மற்றும் பரஸ்பர சுயஉதவி ஆகியவற்றின் அடிப்படையில் கிராமப்புறக் கடன் கூட்டுறவுகளைத் தொடங்கினார்.",
            "why_a_en": "Correct. Raiffeisen was German.",
            "why_a_ta": "சரி. ரைஃபெய்சன் ஜெர்மனியைச் சேர்ந்தவர்.",
            "why_b_en": "Incorrect. Robert Owen and Rochdale pioneers were British.",
            "why_b_ta": "தவறு. ராபர்ட் ஓவன் மற்றும் ரோச்டேல் முன்னோடிகள் பிரிட்டிஷ்காரர்கள்.",
            "why_c_en": "Incorrect. Denmark is famous for dairy cooperatives, not Raiffeisen credit model.",
            "why_c_ta": "தவறு. டென்மார்க் பால் கூட்டுறவுகளுக்குப் புகழ்பெற்றது.",
            "why_d_en": "Incorrect. Switzerland is home to ICA headquarters today, but Raiffeisen was German.",
            "why_d_ta": "தவறு. சுவிட்சர்லாந்து அல்ல.",
            "tip_en": "Sir Frederick Nicholson's two-word advice to Madras Presidency in 1897: 'Find Raiffeisen'.",
            "tip_ta": "1897-ல் மெட்ராஸ் மாகாணத்திற்கு சர் பிரடெரிக் நிக்கல்சன் வழங்கிய இரண்டு வார்த்தை அறிவுரை: 'ரைஃபெய்சனைக் கண்டறியுங்கள்' (Find Raiffeisen).",
            "fact_en": "Nicholson is revered as the 'Father of Cooperative Movement in India'.",
            "fact_ta": "நிக்கல்சன் 'இந்திய கூட்டுறவு இயக்கத்தின் தந்தை' எனப் போற்றப்படுகிறார்."
        },

        # 26. Father of Cooperative Movement in India
        {
            "subtopic": "Historical Evolution - Pioneers",
            "stem_en": "Who among the following British administrators is widely regarded as the 'Father of the Co-operative Movement in India'?",
            "stem_ta": "பின்வரும் பிரிட்டிஷ் அதிகாரிகளில் 'இந்திய கூட்டுறவு இயக்கத்தின் தந்தை' என்று பரவலாகக் கருதப்படுபவர் யார்?",
            "options": [
                ("Sir Frederick Nicholson", "சர் பிரடெரிக் நிக்கல்சன்"),
                ("Lord Curzon", "கர்சன் பிரபு"),
                ("Sir Edward Law", "சர் எட்வர்ட் லா"),
                ("Lord Ripon", "ரிப்பன் பிரபு")
            ],
            "correct_key": "A",
            "exp_en": "Sir Frederick Nicholson, ICS, who served in Madras Presidency and authored landmark reports in 1895 and 1897 advocating cooperative credit on the Raiffeisen model, is hailed as the Father of the Cooperative Movement in India.",
            "exp_ta": "மெட்ராஸ் மாகாணத்தில் பணியாற்றி, 1895 மற்றும் 1897-ல் ரைஃபெய்சன் மாதிரியில் கூட்டுறவுக் கடனைப் பரிந்துரைத்து அறிக்கைகளை அளித்த ஐ.சி.எஸ் அதிகாரி சர் பிரடெரிக் நிக்கல்சன் 'இந்திய கூட்டுறவு இயக்கத்தின் தந்தை' என அழைக்கப்படுகிறார்.",
            "why_a_en": "Correct. Sir Frederick Nicholson conceived and pioneered the Indian cooperative movement.",
            "why_a_ta": "சரி. சர் பிரடெரிக் நிக்கல்சன் இந்திய கூட்டுறவு இயக்கத்தை வடிவமைத்து வழிநடத்தினார்.",
            "why_b_en": "Incorrect. Lord Curzon was the Viceroy who passed the 1904 Act.",
            "why_b_ta": "தவறு. கர்சன் பிரபு 1904 சட்டத்தை நிறைவேற்றிய வைஸ்ராய்.",
            "why_c_en": "Incorrect. Sir Edward Law chaired the 1901 committee on cooperative legislation.",
            "why_c_ta": "தவறு. சர் எட்வர்ட் லா 1901 கூட்டுறவு சட்டக் குழுவின் தலைவர்.",
            "why_d_en": "Incorrect. Lord Ripon is the 'Father of Local Self-Government in India'.",
            "why_d_ta": "தவறு. ரிப்பன் பிரபு 'இந்திய உள்ளாட்சி அமைப்புகளின் தந்தை'.",
            "tip_en": "Ripon = Local Self-Government; Nicholson = Cooperative Movement.",
            "tip_ta": "ரிப்பன் = உள்ளாட்சி அமைப்புகள்; நிக்கல்சன் = கூட்டுறவு இயக்கம்.",
            "fact_en": "Nicholson served as the Collector of Tirunelveli and member of the Board of Revenue in Madras.",
            "fact_ta": "நிக்கல்சன் திருநெல்வேலி மாவட்ட ஆட்சியராகவும், மெட்ராஸ் வருவாய்த்துறை வாரிய உறுப்பினராகவும் பணியாற்றினார்."
        },

        # 27. Primary Agricultural Credit Societies (PACS) Tier
        {
            "subtopic": "Structure of Cooperative Credit",
            "stem_en": "In the three-tier short-term rural cooperative credit structure in India, which body operates at the grassroots (village) level?",
            "stem_ta": "இந்தியாவில் குறுகிய கால ஊரகக் கூட்டுறவுக் கடன் கட்டமைப்பின் மூன்று அடுக்குகளில், அடிமட்ட (கிராம) அளவில் செயல்படும் அமைப்பு எது?",
            "options": [
                ("Primary Agricultural Credit Societies (PACS)", "தொடக்க வேளாண்மைக் கூட்டுறவுக் கடன் சங்கங்கள் (PACS)"),
                ("District Central Co-operative Banks (DCCBs)", "மாவட்ட மத்தியக் கூட்டுறவு வங்கிகள் (DCCBs)"),
                ("State Co-operative Apex Bank (StCB)", "மாநிலத் தலைமைக் கூட்டுறவு வங்கி (StCB)"),
                ("Regional Rural Banks (RRBs)", "பிராந்திய ஊரக வங்கிகள் (RRBs)")
            ],
            "correct_key": "A",
            "exp_en": "The short-term rural cooperative credit structure is a 3-tier pyramid: PACS at the village level, DCCBs at the district level, and the State Cooperative Bank (Apex Bank) at the state level.",
            "exp_ta": "குறுகிய கால ஊரகக் கூட்டுறவுக் கடன் அமைப்பு 3 அடுக்கு பிரமிடு ஆகும்: கிராம அளவில் PACS, மாவட்ட அளவில் DCCBs, மற்றும் மாநில அளவில் மாநில தலைமைக் கூட்டுறவு வங்கி (StCB).",
            "why_a_en": "Correct. PACS operates at the village grassroots tier.",
            "why_a_ta": "சரி. PACS கிராம அளவில் செயல்படும் அடிமட்ட அமைப்பாகும்.",
            "why_b_en": "Incorrect. DCCB operates at the intermediate district level.",
            "why_b_ta": "தவறு. DCCB இடைநிலை மாவட்ட அளவில் செயல்படுகிறது.",
            "why_c_en": "Incorrect. StCB operates at the apex state level.",
            "why_c_ta": "தவறு. StCB மாநில அளவிலான உச்ச அமைப்பாகும்.",
            "why_d_en": "Incorrect. RRBs are separate scheduled commercial banks formed under RRB Act 1976.",
            "why_d_ta": "தவறு. RRBs என்பது 1976 சட்டத்தின் கீழ் உருவாக்கப்பட்ட தனி வர்த்தக வங்கிகள்.",
            "tip_en": "Grassroots = PACS -> Intermediate = DCCB -> Apex = State Cooperative Bank.",
            "tip_ta": "அடிமட்டம் = PACS -> இடைநிலை = DCCB -> தலைமை = மாநில கூட்டுறவு வங்கி.",
            "fact_en": "There are approximately 1 lakh PACS across India serving over 13 crore farmers.",
            "fact_ta": "இந்தியா முழுவதும் சுமார் 1 லட்சம் PACS-கள் 13 கோடிக்கும் அதிகமான விவசாயிகளுக்குச் சேவை செய்கின்றன."
        },

        # 28. Banking Regulation Act Amendment (2020)
        {
            "subtopic": "Regulatory Framework - RBI Supervision",
            "stem_en": "The Banking Regulation (Amendment) Act, 2020 brought Urban Co-operative Banks (UCBs) and Multi-State Co-operative Banks under the direct supervisory control of which authority?",
            "stem_ta": "2020-ஆம் ஆண்டின் வங்கி ஒழுங்குமுறை (திருத்தச்) சட்டம் நகர்ப்புறக் கூட்டுறவு வங்கிகள் (UCBs) மற்றும் பல்மாநிலக் கூட்டுறவு வங்கிகளை எந்த அதிகார அமைப்பின் நேரடி மேற்பார்வைக் கட்டுப்பாட்டின் கீழ் கொண்டு வந்தது?",
            "options": [
                ("Reserve Bank of India (RBI)", "இந்திய ரிசர்வ் வங்கி (RBI)"),
                ("State Registrar of Co-operative Societies", "மாநிலக் கூட்டுறவு சங்கங்களின் பதிவாளர்"),
                ("NABARD exclusively", "நபார்டு (NABARD) மட்டுமே"),
                ("Ministry of Corporate Affairs", "கார்ப்பரேட் விவகாரங்கள் அமைச்சகம்")
            ],
            "correct_key": "A",
            "exp_en": "Following the PMC Bank crisis, the Banking Regulation (Amendment) Act, 2020 empowered the Reserve Bank of India (RBI) to regulate and supervise cooperative banks in terms of management, capital, audit, and resolution.",
            "exp_ta": "PMC வங்கி நெருக்கடியைத் தொடர்ந்து, 2020 வங்கி ஒழுங்குமுறை (திருத்தச்) சட்டம் கூட்டுறவு வங்கிகளை மேலாண்மை, மூலதனம், தணிக்கை மற்றும் தீர்வு ஆகியவற்றில் கட்டுப்படுத்த இந்திய ரிசர்வ் வங்கிக்கு (RBI) அதிகாரம் அளித்தது.",
            "why_a_en": "Correct. RBI now exercises full banking regulation over cooperative banks.",
            "why_a_ta": "சரி. கூட்டுறவு வங்கிகள் மீது RBI இப்போது முழு வங்கி ஒழுங்குமுறை அதிகாரத்தைச் செலுத்துகிறது.",
            "why_b_en": "Incorrect. State Registrars retain administrative control, but banking supervision shifted to RBI.",
            "why_b_ta": "தவறு. மாநிலப் பதிவாளர்கள் நிர்வாகக் கட்டுப்பாட்டைக் கொண்டுள்ளனர், ஆனால் வங்கி மேற்பார்வை RBI-க்கு மாற்றப்பட்டது.",
            "why_c_en": "Incorrect. NABARD inspects rural cooperatives, but RBI is the apex regulator.",
            "why_c_ta": "தவறு. நபார்டு ஊரகக் கூட்டுறவுகளை ஆய்வு செய்கிறது, ஆனால் RBI முதன்மை ஒழுங்குமுறை அமைப்பாகும்.",
            "why_d_en": "Incorrect. MCA regulates commercial companies.",
            "why_d_ta": "தவறு. MCA வணிக நிறுவனங்களை ஒழுங்குபடுத்துகிறது.",
            "tip_en": "Dual control of cooperative banks: Banking functions = RBI; Administrative & incorporation = Registrar.",
            "tip_ta": "இரட்டைக் கட்டுப்பாடு: வங்கிப் பணிகள் = RBI; நிர்வாகம் மற்றும் அமைப்பாக்கம் = பதிவாளர்.",
            "fact_en": "PACS and primary agricultural credit societies remain outside the full Banking Regulation Act.",
            "fact_ta": "PACS மற்றும் தொடக்க வேளாண் கடன் சங்கங்கள் முழு வங்கி ஒழுங்குமுறைச் சட்டத்தின் வரம்பிற்கு வெளியே உள்ளன."
        },

        # 29. NABARD Establishment
        {
            "subtopic": "Institutional Architecture - Refinancing",
            "stem_en": "On the recommendation of which committee was the National Bank for Agriculture and Rural Development (NABARD) established in 1982 to apex rural cooperative credit?",
            "stem_ta": "ஊரகக் கூட்டுறவுக் கடனுக்கான தலைமை அமைப்பாக 1982-ல் விவசாயம் மற்றும் ஊரக வளர்ச்சிக்கான தேசிய வங்கி (NABARD) எந்தக் குழுவின் பரிந்துரையின் பேரில் நிறுவப்பட்டது?",
            "options": [
                ("B. Sivaraman Committee (CRAFICARD)", "பி. சிவராமன் குழு (CRAFICARD)"),
                ("All India Rural Credit Survey Committee (A.D. Gorwala)", "அகில இந்திய ஊரகக் கடன் ஆய்வுக் குழு (A.D. கோர்வாலா)"),
                ("M. Narasimham Committee", "எம். நரசிம்மம் குழு"),
                ("Kelkar Committee", "கேல்கர் குழு")
            ],
            "correct_key": "A",
            "exp_en": "NABARD was established on 12th July 1982 under the NABARD Act, 1981, based on the recommendations of the Committee to Review Arrangements for Institutional Credit for Agriculture and Rural Development (CRAFICARD) headed by B. Sivaraman.",
            "exp_ta": "பி. சிவராமன் தலைமையிலான விவசாயம் மற்றும் ஊரக வளர்ச்சிக்கான நிறுவனக் கடன் ஏற்பாடுகளை மறுஆய்வு செய்யும் குழுவின் (CRAFICARD) பரிந்துரைகளின் அடிப்படையில் 1982 ஜூலை 12 அன்று நபார்டு (NABARD) சட்டம் 1981-ன் கீழ் நிறுவப்பட்டது.",
            "why_a_en": "Correct. B. Sivaraman Committee recommended NABARD.",
            "why_a_ta": "சரி. பி. சிவராமன் குழு நபார்டைப் பரிந்துரைத்தது.",
            "why_b_en": "Incorrect. Gorwala Committee (1954) recommended creation of SBI and Warehousing Corporation.",
            "why_b_ta": "தவறு. கோர்வாலா குழு (1954) SBI மற்றும் கிடங்கு கழகத்தை உருவாக்கப் பரிந்துரைத்தது.",
            "why_c_en": "Incorrect. Narasimham Committee dealt with financial system reforms (1991, 1998).",
            "why_c_ta": "தவறு. நரசிம்மம் குழு நிதித்துறை சீர்திருத்தங்களைக் கையாண்டது.",
            "why_d_en": "Incorrect. Kelkar Committee dealt with tax reforms and PPP model.",
            "why_d_ta": "தவறு. கேல்கர் குழு வரிக் கொள்கை மற்றும் PPP மாதிரியைக் கையாண்டது.",
            "tip_en": "NABARD replaced the Agricultural Credit Department (ACD) and Rural Planning and Credit Cell (RPCC) of RBI.",
            "tip_ta": "நபார்டு ரிசர்வ் வங்கியின் வேளாண் கடன் துறை (ACD) மற்றும் ஊரகத் திட்டமிடல் மற்றும் கடன் பிரிவை (RPCC) மாற்றியமைத்தது.",
            "fact_en": "NABARD refinances State Cooperative Banks and District Central Cooperative Banks.",
            "fact_ta": "மாநிலக் கூட்டுறவு வங்கிகள் மற்றும் மாவட்ட மத்தியக் கூட்டுறவு வங்கிகளுக்கு நபார்டு மறுநிதியளிப்பு செய்கிறது."
        },

        # 30. Aavin Full Name
        {
            "subtopic": "Tamil Nadu Cooperative Ecosystem",
            "stem_en": "What is the official apex cooperative organization behind the well-known 'Aavin' brand in Tamil Nadu?",
            "stem_ta": "தமிழ்நாட்டில் நன்கு அறியப்பட்ட 'ஆவின்' (Aavin) பிராண்டின் பின்னணியில் உள்ள அதிகாரப்பூர்வ தலைமைக் கூட்டுறவு அமைப்பு எது?",
            "options": [
                ("Tamil Nadu Co-operative Milk Producers' Federation Limited (TCMPF)", "தமிழ்நாடு கூட்டுறவு பால் உற்பத்தியாளர்கள் கூட்டமைப்பு நிறுவனம் (TCMPF)"),
                ("Tamil Nadu Dairy Development Corporation", "தமிழ்நாடு பால் மேம்பாட்டுக் கழகம்"),
                ("Madras Milk Union", "மெட்ராஸ் பால் சங்கம்"),
                ("Tamil Nadu Agricultural Marketing Board", "தமிழ்நாடு வேளாண்மை விற்பனை வாரியம்")
            ],
            "correct_key": "A",
            "exp_en": "Aavin is the commercial trademark of the Tamil Nadu Co-operative Milk Producers' Federation Limited (TCMPF), a 3-tier apex dairy cooperative established in 1981 to procure, process, and market milk.",
            "exp_ta": "ஆவின் என்பது 1981-ல் பால் கொள்முதல், பதப்படுத்துதல் மற்றும் விற்பனை செய்வதற்காக நிறுவப்பட்ட 3 அடுக்கு தலைமைக் கூட்டுறவு அமைப்பான தமிழ்நாடு கூட்டுறவு பால் உற்பத்தியாளர்கள் கூட்டமைப்பு நிறுவனத்தின் (TCMPF) வணிக வர்த்தக முத்திரையாகும்.",
            "why_a_en": "Correct. TCMPF is the apex body of dairy cooperatives in Tamil Nadu.",
            "why_a_ta": "சரி. TCMPF தமிழ்நாட்டின் பால் கூட்டுறவுகளின் உச்ச அமைப்பாகும்.",
            "why_b_en": "Incorrect. Dairy Development Corporation was the predecessor government company, converted to cooperative in 1981.",
            "why_b_ta": "தவறு. பால் மேம்பாட்டுக் கழகம் முந்தைய அரசு நிறுவனம், 1981-ல் கூட்டுறவாக மாற்றப்பட்டது.",
            "why_c_en": "Incorrect. Madras Milk Union was an older pre-independence union.",
            "why_c_ta": "தவறு. மெட்ராஸ் பால் சங்கம் சுதந்திரத்திற்கு முந்தைய பழைய சங்கம்.",
            "why_d_en": "Incorrect. Agricultural Marketing Board is an independent statutory board.",
            "why_d_ta": "தவறு. வேளாண் விற்பனை வாரியம் ஒரு தனி சட்டப்பூர்வ வாரியம்.",
            "tip_en": "Dairy structure in TN: Village Dairy Cooperative -> District Cooperative Milk Producers' Union -> State Federation (Aavin/TCMPF).",
            "tip_ta": "TN பால் கட்டமைப்பு: கிராமக் கூட்டுறவு சங்கம் -> மாவட்ட பால் உற்பத்தியாளர்கள் சங்கம் -> மாநிலக் கூட்டமைப்பு (ஆவின்).",
            "fact_en": "Aavin was modeled on the Anand (Amul) cooperative model under Operation Flood.",
            "fact_ta": "ஆவின் ஆபரேஷன் ஃபிளட் திட்டத்தின் கீழ் ஆனந்த் (அமுல்) கூட்டுறவு மாதிரியை அடிப்படையாகக் கொண்டு உருவாக்கப்பட்டது."
        },

        # 31. Co-optex Establishment
        {
            "subtopic": "Tamil Nadu Cooperative Ecosystem",
            "stem_en": "In which year was the Tamil Nadu Handloom Weavers' Co-operative Society Limited, popularly known as 'Co-optex', established?",
            "stem_ta": "'கோ-ஆப்டெக்ஸ்' (Co-optex) என்று பிரபலமாக அழைக்கப்படும் தமிழ்நாடு கைத்தறி நெசவாளர் கூட்டுறவு சங்கம் எந்த ஆண்டு நிறுவப்பட்டது?",
            "options": [
                ("1935", "1935"),
                ("1952", "1952"),
                ("1983", "1983"),
                ("1904", "1904")
            ],
            "correct_key": "A",
            "exp_en": "The Tamil Nadu Handloom Weavers' Co-operative Society Limited (Co-optex) was established in 1935 to organize the handloom weavers of the state and market their handwoven fabrics.",
            "exp_ta": "தமிழ்நாடு கைத்தறி நெசவாளர் கூட்டுறவு சங்கம் (கோ-ஆப்டெக்ஸ்) மாநிலத்தின் கைத்தறி நெசவாளர்களை ஒன்றிணைத்து அவர்களின் தயாரிப்புகளை சந்தைப்படுத்துவதற்காக 1935-ல் நிறுவப்பட்டது.",
            "why_a_en": "Correct. Co-optex was formed in 1935.",
            "why_a_ta": "சரி. கோ-ஆப்டெக்ஸ் 1935-ல் உருவாக்கப்பட்டது.",
            "why_b_en": "Incorrect. 1952 was the year of the first general election.",
            "why_b_ta": "தவறு. 1952 முதல் பொதுத் தேர்தல் ஆண்டு.",
            "why_c_en": "Incorrect. 1983 was the year of Tamil Nadu Co-operative Societies Act.",
            "why_c_ta": "தவறு. 1983 தமிழ்நாடு கூட்டுறவு சங்கங்கள் சட்டத்தின் ஆண்டு.",
            "why_d_en": "Incorrect. 1904 was the year of first cooperative act.",
            "why_d_ta": "தவறு. 1904 முதல் கூட்டுறவுச் சட்டத்தின் ஆண்டு.",
            "tip_en": "Co-optex is the largest apex handloom weavers' cooperative society in India.",
            "tip_ta": "கோ-ஆப்டெக்ஸ் இந்தியாவின் மிகப்பெரிய உச்ச கைத்தறி நெசவாளர் கூட்டுறவு சங்கமாகும்.",
            "fact_en": "It coordinates thousands of primary handloom weavers' societies across Tamil Nadu.",
            "fact_ta": "இது தமிழ்நாடு முழுவதும் உள்ள ஆயிரக்கணக்கான தொடக்க கைத்தறி நெசவாளர் சங்கங்களை ஒருங்கிணைக்கிறது."
        },

        # 32. Multi-State Co-operative Societies Act Year
        {
            "subtopic": "Statutory Framework - Central Legislation",
            "stem_en": "Which Act currently governs Multi-State Co-operative Societies having objects extending to more than one State in India?",
            "stem_ta": "இந்தியாவில் ஒன்றுக்கு மேற்பட்ட மாநிலங்களுக்கு விரிவடையும் நோக்கங்களைக் கொண்ட பல்மாநில கூட்டுறவு சங்கங்களை தற்போது நிர்வகிக்கும் சட்டம் எது?",
            "options": [
                ("Multi-State Co-operative Societies Act, 2002", "பல்மாநில கூட்டுறவு சங்கங்கள் சட்டம், 2002"),
                ("Multi-State Co-operative Societies Act, 1984", "பல்மாநில கூட்டுறவு சங்கங்கள் சட்டம், 1984"),
                ("Multi-Unit Cooperative Societies Act, 1942", "பல-அலகு கூட்டுறவு சங்கங்கள் சட்டம், 1942"),
                ("Companies Act, 2013", "நிறுவனங்கள் சட்டம், 2013")
            ],
            "correct_key": "A",
            "exp_en": "The Multi-State Co-operative Societies Act, 2002 (enacted under Entry 44 of List I) currently regulates multi-state cooperatives, replacing the earlier 1984 legislation.",
            "exp_ta": "2002-ஆம் ஆண்டின் பல்மாநில கூட்டுறவு சங்கங்கள் சட்டம் (பட்டியல் I-ன் பதிவு 44-ன் கீழ் இயற்றப்பட்டது) முந்தைய 1984 சட்டத்தை மாற்றி தற்போது பல்மாநில கூட்டுறவுகளை ஒழுங்குபடுத்துகிறது.",
            "why_a_en": "Correct. The 2002 Act is the governing central legislation.",
            "why_a_ta": "சரி. 2002 சட்டம் தற்போது நடைமுறையில் உள்ள மத்திய சட்டமாகும்.",
            "why_b_en": "Incorrect. The 1984 Act was repealed and replaced by the 2002 Act.",
            "why_b_ta": "தவறு. 1984 சட்டம் ரத்து செய்யப்பட்டு 2002 சட்டத்தால் மாற்றப்பட்டது.",
            "why_c_en": "Incorrect. 1942 Act was the colonial precursor.",
            "why_c_ta": "தவறு. 1942 சட்டம் காலனித்துவ கால முந்தைய சட்டம்.",
            "why_d_en": "Incorrect. Companies Act does not apply to cooperatives.",
            "why_d_ta": "தவறு. நிறுவனங்கள் சட்டம் கூட்டுறவுகளுக்குப் பொருந்தாது.",
            "tip_en": "Major amendments to the MSCS Act were passed in 2023 to bring transparency and introduce an Election Authority.",
            "tip_ta": "வெளிப்படைத்தன்மையைக் கொண்டுவரவும் தேர்தல் ஆணையத்தை அறிமுகப்படுத்தவும் 2023-ல் MSCS சட்டத்தில் முக்கிய திருத்தங்கள் செய்யப்பட்டன.",
            "fact_en": "The Central Registrar of Cooperative Societies registers and regulates all MSCS.",
            "fact_ta": "மத்திய கூட்டுறவு சங்கங்களின் பதிவாளர் அனைத்து MSCS-களையும் பதிவு செய்து ஒழுங்குபடுத்துகிறார்."
        },

        # 33. Central Registrar Appointment
        {
            "subtopic": "Statutory Framework - Multi-State",
            "stem_en": "Under Section 4 of the Multi-State Co-operative Societies Act, 2002, who appoints the Central Registrar of Co-operative Societies?",
            "stem_ta": "2002-ஆம் ஆண்டின் பல்மாநில கூட்டுறவு சங்கங்கள் சட்டத்தின் பிரிவு 4-ன் கீழ் மத்திய கூட்டுறவு சங்கங்களின் பதிவாளரை நியமிப்பவர் யார்?",
            "options": [
                ("The Central Government", "மத்திய அரசு"),
                ("The Governor of the Reserve Bank of India", "இந்திய ரிசர்வ் வங்கி ஆளுநர்"),
                ("The President of India by warrant", "குடியரசுத் தலைவர் தனது கையொப்பமிட்ட ஆணை மூலம்"),
                ("A collegium headed by the Prime Minister", "பிரதமர் தலைமையிலான தேர்வுக்குழு")
            ],
            "correct_key": "A",
            "exp_en": "Section 4(1) of the MSCS Act, 2002 provides that the Central Government may appoint a person to be the Central Registrar of Co-operative Societies and may appoint other officers to assist him.",
            "exp_ta": "2002 MSCS சட்டத்தின் பிரிவு 4(1) மத்திய அரசு ஒரு நபரை மத்திய கூட்டுறவு சங்கங்களின் பதிவாளராக நியமிக்கலாம் மற்றும் அவருக்கு உதவ பிற அதிகாரிகளை நியமிக்கலாம் என்று கூறுகிறது.",
            "why_a_en": "Correct. The Central Government appoints the Central Registrar.",
            "why_a_ta": "சரி. மத்திய அரசு மத்தியப் பதிவாளரை நியமிக்கிறது.",
            "why_b_en": "Incorrect. RBI Governor regulates banks, does not appoint cooperative registrar.",
            "why_b_ta": "தவறு. RBI ஆளுநர் வங்கிகளை ஒழுங்குபடுத்துகிறார், கூட்டுறவுப் பதிவாளரை நியமிப்பதில்லை.",
            "why_c_en": "Incorrect. The President does not appoint under constitutional warrant.",
            "why_c_ta": "தவறு. குடியரசுத் தலைவர் சிறப்பு ஆணை மூலம் நியமிப்பதில்லை.",
            "why_d_en": "Incorrect. No collegium is specified in Section 4.",
            "why_d_ta": "தவறு. பிரிவு 4-ல் எவ்வித தேர்வுக்குழுவும் குறிப்பிடப்படவில்லை.",
            "tip_en": "Central Registrar = Appointed by Central Government; State Registrar = Appointed by State Government.",
            "tip_ta": "மத்தியப் பதிவாளர் = மத்திய அரசால் நியமிக்கப்படுபவர்; மாநிலப் பதிவாளர் = மாநில அரசால் நியமிக்கப்படுபவர்.",
            "fact_en": "The Central Registrar functions under the Ministry of Cooperation in New Delhi.",
            "fact_ta": "மத்தியப் பதிவாளர் புது தில்லியில் உள்ள மத்திய கூட்டுறவு அமைச்சகத்தின் கீழ் செயல்படுகிறார்."
        },

        # 34. Right to Information of Members (243ZO)
        {
            "subtopic": "Democratic Rights of Members - Article 243ZO",
            "stem_en": "Which Article in Part IX-B guarantees members of a co-operative society the right to access the books, information, and accounts of the society?",
            "stem_ta": "பகுதி IX-B-ல் உள்ள எந்தச் சரத்து ஒரு கூட்டுறவு சங்கத்தின் உறுப்பினர்களுக்கு சங்கத்தின் புத்தகங்கள், தகவல்கள் மற்றும் கணக்குகளைப் பார்க்கும் உரிமையை உத்தரவாதப்படுத்துகிறது?",
            "options": [
                ("Article 243ZO", "சரத்து 243ZO"),
                ("Article 243ZH", "சரத்து 243ZH"),
                ("Article 243ZK", "சரத்து 243ZK"),
                ("Article 243ZR", "சரத்து 243ZR")
            ],
            "correct_key": "A",
            "exp_en": "Article 243ZO directs the State Legislature to make provisions to ensure the right of a member to get information and have access to the books, information and accounts of the co-operative society.",
            "exp_ta": "சரத்து 243ZO ஒரு கூட்டுறவு சங்கத்தின் புத்தகங்கள், தகவல்கள் மற்றும் கணக்குகளைப் பெறுவதற்கும் பார்ப்பதற்கும் உறுப்பினரின் உரிமையை உறுதி செய்ய மாநில சட்டமன்றம் விதிகளை உருவாக்க வேண்டும் என்று வழிகாட்டுகிறது.",
            "why_a_en": "Correct. Article 243ZO provides for right of members to get information.",
            "why_a_ta": "சரி. சரத்து 243ZO உறுப்பினர்களின் தகவல் பெறும் உரிமையை வழங்குகிறது.",
            "why_b_en": "Incorrect. Article 243ZH is the definition clause.",
            "why_b_ta": "தவறு. சரத்து 243ZH வரையறைப் பிரிவாகும்.",
            "why_c_en": "Incorrect. Article 243ZK governs election of board members.",
            "why_c_ta": "தவறு. சரத்து 243ZK வாரிய உறுப்பினர்களின் தேர்தலை நிர்வகிக்கிறது.",
            "why_d_en": "Incorrect. Article 243ZR applies Part IX-B to multi-state cooperatives.",
            "why_d_ta": "தவறு. சரத்து 243ZR பகுதி IX-B-ஐப் பல்மாநில கூட்டுறவுகளுக்குப் பயன்படுத்துகிறது.",
            "tip_en": "Article 243ZO promotes internal transparency and prevents corruption by the board.",
            "tip_ta": "சரத்து 243ZO சங்கத்தின் உள் வெளிப்படைத்தன்மையை ஊக்குவிக்கிறது மற்றும் வாரிய ஊழலைத் தடுக்கிறது.",
            "fact_en": "Members are also entitled to cooperative education and training under Article 243ZO.",
            "fact_ta": "உறுப்பினர்கள் சரத்து 243ZO-ன் கீழ் கூட்டுறவுக் கல்வி மற்றும் பயிற்சி பெறவும் தகுதியுடையவர்கள்."
        },

        # 35. Offenses and Penalties (243ZQ)
        {
            "subtopic": "Offenses and Penalties - Article 243ZQ",
            "stem_en": "Under Article 243ZQ, which of the following acts is specifically enumerated as a constitutional offense by a co-operative society or its officials?",
            "stem_ta": "சரத்து 243ZQ-ன் கீழ், பின்வருவனவற்றில் எது ஒரு கூட்டுறவு சங்கம் அல்லது அதன் அதிகாரிகளால் செய்யப்படும் அரசியலமைப்பு ரீதியான குற்றமாகக் குறிப்பிடப்பட்டுள்ளது?",
            "options": [
                ("Willfully making a false return or furnishing false information", "வேண்டுமென்றே தவறான கணக்கு விவரங்களைத் தாக்கல் செய்தல் அல்லது தவறான தகவல்களை அளித்தல்"),
                ("Opening a new branch office with board approval", "வாரிய ஒப்புதலுடன் புதிய கிளை அலுவலகத்தைத் திறப்பது"),
                ("Convening the Annual General Meeting within 6 months", "6 மாதங்களுக்குள் வருடாந்திர பொதுக்குழு கூட்டத்தைக் கூட்டுவது"),
                ("Admitting new members meeting eligibility criteria", "தகுதி வாய்ந்த புதிய உறுப்பினர்களைச் சேர்ப்பது"),
            ],
            "correct_key": "A",
            "exp_en": "Article 243ZQ provides that the State Legislature shall make provisions for offences and penalties, specifically penalizing willfully making false returns, failing to furnish information, or disobeying lawful summons.",
            "exp_ta": "சரத்து 243ZQ வேண்டுமென்றே தவறான விவரங்களைத் தாக்கல் செய்வது, தகவல்களை அளிக்கத் தவறுவது அல்லது சட்டப்பூர்வ அழைப்பாணைகளை அவமதிப்பது போன்றவற்றை குற்றங்களாகவும் தண்டனைக்குரியதாகவும் மாநில சட்டமன்றம் நிர்ணயிக்க வேண்டும் என்று கூறுகிறது.",
            "why_a_en": "Correct. Willful false reporting is explicitly an offense under 243ZQ.",
            "why_a_ta": "சரி. வேண்டுமென்றே தவறான தகவல்களை அளிப்பது 243ZQ-ன் கீழ் வெளிப்படையான குற்றமாகும்.",
            "why_b_en": "Incorrect. Opening branches legally is a regular managerial activity.",
            "why_b_ta": "தவறு. கிளைகளைத் திறப்பது வழக்கமான நிர்வாக நடவடிக்கை.",
            "why_c_en": "Incorrect. Convening AGM on time is a mandatory constitutional duty.",
            "why_c_ta": "தவறு. உரிய நேரத்தில் AGM கூட்டுவது கட்டாய அரசியலமைப்புக் கடமையாகும்.",
            "why_d_en": "Incorrect. Open membership is a core cooperative principle.",
            "why_d_ta": "தவறு. உறுப்பினர்களைச் சேர்ப்பது அடிப்படைக் கொள்கை.",
            "tip_en": "Article 243ZQ provides the constitutional teeth to enforce audit, returns, and elections.",
            "tip_ta": "சரத்து 243ZQ தணிக்கை, கணக்குத் தாக்கல் மற்றும் தேர்தல்களை அமல்படுத்துவதற்கான அதிகாரத்தை அளிக்கிறது.",
            "fact_en": "State legislatures determine the fine and imprisonment terms for these offenses.",
            "fact_ta": "இந்தக் குற்றங்களுக்கான அபராதம் மற்றும் சிறைத் தண்டனை விதிமுறைகளை மாநிலச் சட்டமன்றங்கள் தீர்மானிக்கின்றன."
        },

        # 36. Continuance of Existing Laws (243ZT)
        {
            "subtopic": "Transitional Provisions - Article 243ZT",
            "stem_en": "Under Article 243ZT, what transition period was granted to States to amend their inconsistent state co-operative laws to align with Part IX-B?",
            "stem_ta": "சரத்து 243ZT-ன் கீழ், பகுதி IX-B-க்கு ஏற்ப தங்கள் முரண்பட்ட மாநிலக் கூட்டுறவுச் சட்டங்களைத் திருத்துவதற்கு மாநிலங்களுக்கு வழங்கப்பட்ட மாறுதல் கால அவகாசம் என்ன?",
            "options": [
                ("1 year from the commencement of the 97th Amendment", "97வது திருத்தம் நடைமுறைக்கு வந்ததிலிருந்து 1 ஆண்டு"),
                ("6 months from commencement", "நடைமுறைக்கு வந்ததிலிருந்து 6 மாதங்கள்"),
                ("2 years from commencement", "நடைமுறைக்கு வந்ததிலிருந்து 2 ஆண்டுகள்"),
                ("3 years from commencement", "நடைமுறைக்கு வந்ததிலிருந்து 3 ஆண்டுகள்")
            ],
            "correct_key": "A",
            "exp_en": "Article 243ZT mandated that any provision of law relating to co-operative societies in force in any State inconsistent with Part IX-B shall continue until amended by a competent Legislature or until the expiration of one year from commencement.",
            "exp_ta": "சரத்து 243ZT, பகுதி IX-B-க்கு முரணாக உள்ள எந்தவொரு மாநிலக் கூட்டுறவுச் சட்ட விதிகளும் தகுதிவாய்ந்த சட்டமன்றத்தால் திருத்தப்படும் வரை அல்லது நடைமுறைக்கு வந்த ஒரு ஆண்டு முடியும் வரை மட்டுமே தொடரும் என்று விதித்தது.",
            "why_a_en": "Correct. Exactly 1 year was granted for alignment.",
            "why_a_ta": "சரி. சட்டங்களைத் திருத்த சரியாக 1 ஆண்டு அவகாசம் வழங்கப்பட்டது.",
            "why_b_en": "Incorrect. 6 months was not the transitional period.",
            "why_b_ta": "தவறு. 6 மாதங்கள் மாறுதல் காலமல்ல.",
            "why_c_en": "Incorrect. 2 years was not granted.",
            "why_c_ta": "தவறு. 2 ஆண்டுகள் வழங்கப்படவில்லை.",
            "why_d_en": "Incorrect. 3 years is incorrect.",
            "why_d_ta": "தவறு. 3 ஆண்டுகள் தவறானது.",
            "tip_en": "Identical 1-year sunset clauses exist in Article 243N (Panchayats) and Article 243ZF (Municipalities).",
            "tip_ta": "சரத்து 243N (பஞ்சாயத்துகள்) மற்றும் சரத்து 243ZF (நகராட்சிகள்) ஆகியவற்றிலும் இதேபோன்ற 1 ஆண்டு அவகாச விதி உள்ளது.",
            "fact_en": "The 1-year window expired on 14th February 2013.",
            "fact_ta": "இந்த 1 ஆண்டு காலக்கெடு 2013 பிப்ரவரி 14 அன்று முடிவடைந்தது."
        },

        # 37. Amul Cooperative Model
        {
            "subtopic": "National Cooperative Landmarks",
            "stem_en": "The Kaira District Co-operative Milk Producers' Union Limited, which pioneered the 'Amul' white revolution, was established in which State?",
            "stem_ta": "'அமுல்' (Amul) வெண்மைப் புரட்சிக்கு முன்னோடியாகத் திகழ்ந்த கைரா மாவட்டக் கூட்டுறவு பால் உற்பத்தியாளர்கள் சங்கம் எந்த மாநிலத்தில் நிறுவப்பட்டது?",
            "options": [
                ("Gujarat", "குஜராத்"),
                ("Maharashtra", "மகாராஷ்டிரா"),
                ("Punjab", "பஞ்சாப்"),
                ("Tamil Nadu", "தமிழ்நாடு")
            ],
            "correct_key": "A",
            "exp_en": "Amul was founded in 1946 in Anand (Kaira district), Gujarat, under the inspiration of Sardar Vallabhbhai Patel and leadership of Tribhuvandas Patel and Dr. Verghese Kurien.",
            "exp_ta": "சர்தார் வல்லபாய் படேலின் வழிகாட்டுதலில் திரிபுவன்தாஸ் படேல் மற்றும் டாக்டர் வர்கீஸ் குரியன் ஆகியோரின் தலைமையில் 1946-ல் குஜராத்தின் ஆனந்த் (கைரா மாவட்டம்) பகுதியில் அமுல் தொடங்கப்பட்டது.",
            "why_a_en": "Correct. Amul was founded in Anand, Gujarat.",
            "why_a_ta": "சரி. அமுல் குஜராத்தின் ஆனந்தில் தொடங்கப்பட்டது.",
            "why_b_en": "Incorrect. Maharashtra is famous for cooperative sugar factories.",
            "why_b_ta": "தவறு. மகாராஷ்டிரா கூட்டுறவு சர்க்கரை ஆலைகளுக்குப் புகழ்பெற்றது.",
            "why_c_en": "Incorrect. Punjab is famous for green revolution grain production.",
            "why_c_ta": "தவறு. பஞ்சாப் பசுமைப் புரட்சிக்கு புகழ்பெற்றது.",
            "why_d_en": "Incorrect. Tamil Nadu developed the Aavin model.",
            "why_d_ta": "தவறு. தமிழ்நாடு ஆவின் மாதிரியை உருவாக்கியது.",
            "tip_en": "Dr. Verghese Kurien is known as the 'Father of the White Revolution in India'.",
            "tip_ta": "டாக்டர் வர்கீஸ் குரியன் 'இந்தியாவின் வெண்மைப் புரட்சியின் தந்தை' என அழைக்கப்படுகிறார்.",
            "fact_en": "The National Dairy Development Board (NDDB) was established in 1965 to replicate the Anand model nationwide.",
            "fact_ta": "ஆனந்த் மாதிரியை நாடு முழுவதும் செயல்படுத்த 1965-ல் தேசிய பால் மேம்பாட்டு வாரியம் (NDDB) நிறுவப்பட்டது."
        },

        # 38. IFFCO Organization Type
        {
            "subtopic": "National Cooperative Landmarks",
            "stem_en": "The Indian Farmers Fertiliser Cooperative Limited (IFFCO) is legally organized under which cooperative framework?",
            "stem_ta": "இந்திய விவசாயிகள் உரக் கூட்டுறவு நிறுவனம் (IFFCO) சட்டப்பூர்வமாக எந்தக் கூட்டுறவுக் கட்டமைப்பின் கீழ் செயல்படுகிறது?",
            "options": [
                ("Multi-State Co-operative Society", "பல்மாநிலக் கூட்டுறவு சங்கம்"),
                ("State Public Sector Undertaking", "மாநில அரசுப் பொதுத்துறை நிறுவனம்"),
                ("Statutory Corporation of Parliament", "நாடாளுமன்றத்தின் சட்டப்பூர்வக் கழகம்"),
                ("Non-Governmental Organization (NGO)", "அரசு சாரா அமைப்பு (NGO)")
            ],
            "correct_key": "A",
            "exp_en": "IFFCO, founded in 1967, is registered as a Multi-State Co-operative Society under the Multi-State Co-operative Societies Act, owned by over 35,000 member cooperative societies across India.",
            "exp_ta": "1967-ல் தொடங்கப்பட்ட IFFCO, இந்தியா முழுவதிலும் உள்ள 35,000-க்கும் மேற்பட்ட உறுப்பினர் கூட்டுறவு சங்கங்களுக்குச் சொந்தமான பல்மாநில கூட்டுறவு சங்கங்கள் சட்டத்தின் கீழ் பதிவு செய்யப்பட்ட ஒரு பல்மாநிலக் கூட்டுறவு சங்கமாகும்.",
            "why_a_en": "Correct. IFFCO is the world's largest fertilizer cooperative under MSCS Act.",
            "why_a_ta": "சரி. IFFCO என்பது MSCS சட்டத்தின் கீழ் உள்ள உலகின் மிகப்பெரிய உரக் கூட்டுறவு அமைப்பாகும்.",
            "why_b_en": "Incorrect. It is not a state PSU.",
            "why_b_ta": "தவறு. இது மாநில பொதுத்துறை நிறுவனம் அல்ல.",
            "why_c_en": "Incorrect. It is a cooperative society, not a statutory corporation like LIC.",
            "why_c_ta": "தவறு. இது LIC போன்ற சட்டப்பூர்வக் கழகம் அல்ல.",
            "why_d_en": "Incorrect. It is a commercial cooperative enterprise, not an NGO.",
            "why_d_ta": "தவறு. இது ஒரு வணிகக் கூட்டுறவு நிறுவனம்.",
            "tip_en": "IFFCO and KRIBHCO (Krishak Bharati Cooperative) are India's premier multi-state fertilizer cooperatives.",
            "tip_ta": "IFFCO மற்றும் KRIBHCO ஆகியவை இந்தியாவின் முதன்மையான பல்மாநில உரக் கூட்டுறவு அமைப்புகளாகும்.",
            "fact_en": "IFFCO pioneered Nano Urea in India.",
            "fact_ta": "IFFCO இந்தியாவில் நானோ யூரியாவை முதன்முதலில் அறிமுகப்படுத்தியது."
        },

        # 39. Election Authority for Cooperatives
        {
            "subtopic": "Elections of Board Members - Article 243ZK",
            "stem_en": "Under Article 243ZK, who is responsible for conducting elections to the board of a co-operative society?",
            "stem_ta": "சரத்து 243ZK-ன் கீழ், ஒரு கூட்டுறவு சங்கத்தின் இயக்குநர் வாரியத்திற்கான தேர்தல்களை நடத்தும் பொறுப்பு யாரிடம் ஒப்படைக்கப்பட்டுள்ளது?",
            "options": [
                ("Such body as may be provided by the Legislature of a State by law", "மாநிலச் சட்டமன்றம் சட்டத்தின் மூலம் வழங்கும் அமைப்பிடம்"),
                ("The Election Commission of India (ECI)", "இந்தியத் தேர்தல் ஆணையத்திடம் (ECI)"),
                ("The District Collector exclusively", "மாவட்ட ஆட்சியரிடம் மட்டுமே"),
                ("The President of the outgoing board", "பதவி முடியும் வாரியத்தின் தலைவரிடம்")
            ],
            "correct_key": "A",
            "exp_en": "Article 243ZK provides that the superintendence, direction and control of the preparation of electoral rolls for, and the conduct of, all elections to a co-operative society shall vest in such an independent body as provided by State Legislature by law.",
            "exp_ta": "சரத்து 243ZK ஒரு கூட்டுறவு சங்கத்திற்கான வாக்காளர் பட்டியல் தயாரித்தல் மற்றும் அனைத்து தேர்தல்களையும் நடத்துவதற்கான மேற்பார்வை, வழிகாட்டுதல் மற்றும் கட்டுப்பாடு ஆகியவை மாநிலச் சட்டமன்றத்தால் சட்டத்தின் மூலம் ஏற்படுத்தப்படும் ஒரு சுதந்திரமான அமைப்பிடம் ஒப்படைக்கப்படும் என்று கூறுகிறது.",
            "why_a_en": "Correct. State Legislatures create independent cooperative election authorities.",
            "why_a_ta": "சரி. மாநில சட்டமன்றங்கள் இதற்காகத் தனி தேர்தல் அமைப்புகளை உருவாக்குகின்றன.",
            "why_b_en": "Incorrect. ECI conducts Parliament and State Assembly elections under Article 324.",
            "why_b_ta": "தவறு. ECI நாடாளுமன்ற மற்றும் சட்டமன்றத் தேர்தல்களை நடத்துகிறது.",
            "why_c_en": "Incorrect. District Collector may act as district election officer, but the overarching authority is designated by state law.",
            "why_c_ta": "தவறு. மாவட்ட ஆட்சியர் தேர்தல் அதிகாரியாகச் செயல்படலாம், ஆனால் உச்ச அதிகாரம் மாநிலச் சட்டத்தால் நிர்ணயிக்கப்படுகிறது.",
            "why_d_en": "Incorrect. Outgoing board cannot conduct its own election due to conflict of interest.",
            "why_d_ta": "தவறு. பதவி முடியும் வாரியமே தேர்தலை நடத்த முடியாது.",
            "tip_en": "In Tamil Nadu, the Tamil Nadu State Cooperative Societies Election Commission conducts cooperative polls.",
            "tip_ta": "தமிழ்நாட்டில், தமிழ்நாடு மாநில கூட்டுறவு சங்கங்கள் தேர்தல் ஆணையம் இத்தேர்தல்களை நடத்துகிறது.",
            "fact_en": "Elections must be completed prior to the expiry of the 5-year board term.",
            "fact_ta": "5 ஆண்டு பதவிக்காலம் முடிவதற்கு முன்பே தேர்தல்கள் நடத்தி முடிக்கப்பட வேண்டும்."
        },

        # 40. Tamil Nadu State Cooperative Societies Election Commission
        {
            "subtopic": "Tamil Nadu Cooperative Governance",
            "stem_en": "In which year was the dedicated Tamil Nadu State Cooperative Societies Election Commission established under the TN Cooperative Societies Act?",
            "stem_ta": "தமிழ்நாடு கூட்டுறவு சங்கங்கள் சட்டத்தின் கீழ் பிரத்யேக தமிழ்நாடு மாநில கூட்டுறவு சங்கங்கள் தேர்தல் ஆணையம் எந்த ஆண்டு அமைக்கப்பட்டது?",
            "options": [
                ("2013", "2013"),
                ("2004", "2004"),
                ("1983", "1983"),
                ("1996", "1996")
            ],
            "correct_key": "A",
            "exp_en": "Following the 97th Constitutional Amendment, Tamil Nadu amended the TN Co-operative Societies Act 1983 and constituted the Tamil Nadu State Cooperative Societies Election Commission in 2013 under a retired IAS officer.",
            "exp_ta": "97வது அரசியலமைப்புத் திருத்தத்தைத் தொடர்ந்து, தமிழ்நாடு அரசு 1983-ஆம் ஆண்டின் சட்டத்தைத் திருத்தி, ஓய்வுபெற்ற ஐ.ஏ.எஸ் அதிகாரி தலைமையில் 2013-ல் தமிழ்நாடு மாநில கூட்டுறவு சங்கங்கள் தேர்தல் ஆணையத்தை அமைத்தது.",
            "why_a_en": "Correct. The Commission was set up in 2013.",
            "why_a_ta": "சரி. இந்த ஆணையம் 2013-ல் அமைக்கப்பட்டது.",
            "why_b_en": "Incorrect. 2004 was the centenary year of cooperation in India.",
            "why_b_ta": "தவறு. 2004 என்பது கூட்டுறவு இயக்கத்தின் நூற்றாண்டு விழா ஆண்டு.",
            "why_c_en": "Incorrect. 1983 was the year the parent Act was passed.",
            "why_c_ta": "தவறு. 1983 தாய் சட்டம் இயற்றப்பட்ட ஆண்டு.",
            "why_d_en": "Incorrect. 1996 was when local body polls were conducted after 73rd/74th amendments.",
            "why_d_ta": "தவறு. 1996 உள்ளாட்சித் தேர்தல் நடைபெற்ற ஆண்டு.",
            "tip_en": "The Election Commissioner for Cooperatives in TN is appointed by the State Government for a fixed term.",
            "tip_ta": "TN கூட்டுறவு தேர்தல் ஆணையர் மாநில அரசால் குறிப்பிட்ட பதவிக்காலத்திற்கு நியமிக்கப்படுகிறார்.",
            "fact_en": "It functions independently of the State Election Commission which handles Panchayat and Municipal polls.",
            "fact_ta": "இது பஞ்சாயத்து மற்றும் நகராட்சி தேர்தல்களை நடத்தும் மாநில தேர்தல் ஆணையத்திலிருந்து தனித்து இயங்குகிறது."
        },

        # 41. Vaidyanathan Committee
        {
            "subtopic": "Committees and Commissions",
            "stem_en": "The Task Force on Revival of Rural Cooperative Credit Structure (2004-05), which recommended financial recapitalization of PACS, was chaired by whom?",
            "stem_ta": "தொடக்க வேளாண் கூட்டுறவுக் கடன் சங்கங்களுக்கு (PACS) நிதி மறுமூலதனத்தை பரிந்துரைத்த ஊரகக் கூட்டுறவுக் கடன் கட்டமைப்பை புத்துயிரூட்டுவதற்கான பணிக்குழு (2004-05) யாருடைய தலைமையில் அமைக்கப்பட்டது?",
            "options": [
                ("Prof. A. Vaidyanathan", "பேராசிரியர் ஏ. வைத்தியநாதன்"),
                ("Dr. C. Rangarajan", "டாக்டர் சி. ரங்கராஜன்"),
                ("Dr. Y.V. Reddy", "டாக்டர் ஒய்.வி. ரெட்டி"),
                ("B. Sivaraman", "பி. சிவராமன்")
            ],
            "correct_key": "A",
            "exp_en": "The Vaidyanathan Committee (Task Force on Revival of Short-Term Rural Cooperative Credit Institutions, 2004) recommended a comprehensive financial revival package of over Rs. 13,000 crore conditional on legal and institutional reforms.",
            "exp_ta": "வைத்தியநாதன் குழு (குறுகிய கால ஊரகக் கூட்டுறவுக் கடன் நிறுவனங்களைப் புத்துயிரூட்டுவதற்கான பணிக்குழு, 2004) சட்ட மற்றும் நிறுவன சீர்திருத்தங்களை நிபந்தனையாகக் கொண்டு ரூ. 13,000 கோடிக்கும் அதிகமான நிதிப் புத்துயிரூட்டல் தொகுப்பை பரிந்துரைத்தது.",
            "why_a_en": "Correct. Prof. A. Vaidyanathan headed the landmark revival task force.",
            "why_a_ta": "சரி. பேராசிரியர் ஏ. வைத்தியநாதன் இக்குழுவிற்குத் தலைமை தாங்கினார்.",
            "why_b_en": "Incorrect. Rangarajan Committee dealt with financial inclusion and poverty estimation.",
            "why_b_ta": "தவறு. ரங்கராஜன் குழு நிதி உள்ளடக்கம் மற்றும் வறுமைக் கோட்டைக் கையாண்டது.",
            "why_c_en": "Incorrect. Y.V. Reddy was RBI Governor.",
            "why_c_ta": "தவறு. ஒய்.வி. ரெட்டி ரிசர்வ் வங்கி ஆளுநராக இருந்தார்.",
            "why_d_en": "Incorrect. Sivaraman Committee recommended NABARD in 1979-81.",
            "why_d_ta": "தவறு. சிவராமன் குழு 1981-ல் நபார்டை பரிந்துரைத்தது.",
            "tip_en": "Vaidyanathan Committee Package: Financial assistance tied to removing government nominees from cooperative boards.",
            "tip_ta": "வைத்தியநாதன் குழு தொகுப்பு: கூட்டுறவு வாரியங்களிலிருந்து அரசு பரிந்துரைத்தவர்களை நீக்குவதோடு இணைக்கப்பட்ட நிதி உதவி.",
            "fact_en": "The package required states to sign a tripartite Memorandum of Understanding (MoU) with Central Government and NABARD.",
            "fact_ta": "இத்திட்டம் மாநிலங்கள் மத்திய அரசு மற்றும் நபார்டுடன் முத்தரப்பு புரிந்துணர்வு ஒப்பந்தத்தில் கையெழுத்திடக் கோரியது."
        },

        # 42. Gorwala Committee (1954)
        {
            "subtopic": "Committees and Commissions",
            "stem_en": "Which landmark report of 1954 gave the famous slogan: 'Cooperation has failed, but Cooperation must succeed'?",
            "stem_ta": "'கூட்டுறவு தோற்றுவிட்டது, ஆனால் கூட்டுறவு வென்றே தீர வேண்டும்' என்ற புகழ்பெற்ற முழக்கத்தை வழங்கிய 1954-ஆம் ஆண்டின் மைல்கல் அறிக்கை எது?",
            "options": [
                ("All India Rural Credit Survey Committee (A.D. Gorwala)", "அகில இந்திய ஊரகக் கடன் ஆய்வுக் குழு (A.D. கோர்வாலா)"),
                ("Maclagan Committee on Cooperation", "கூட்டுறவு மீதான மெக்லகன் குழு"),
                ("Nicholson Report", "நிக்கல்சன் அறிக்கை"),
                ("Royal Commission on Agriculture", "விவசாயத்திற்கான அரச ஆணையம்")
            ],
            "correct_key": "A",
            "exp_en": "The All India Rural Credit Survey Committee (1954), appointed by the RBI under the chairmanship of A.D. Gorwala, analyzed the rural economy and famously remarked: 'Cooperation has failed, but Cooperation must succeed.'",
            "exp_ta": "A.D. கோர்வாலா தலைமையில் ரிசர்வ் வங்கியால் அமைக்கப்பட்ட அகில இந்திய ஊரகக் கடன் ஆய்வுக் குழு (1954) கிராமப்புறப் பொருளாதாரத்தை ஆய்வு செய்து, 'கூட்டுறவு தோற்றுவிட்டது, ஆனால் கூட்டுறவு வென்றே தீர வேண்டும்' என்று குறிப்பிட்டது.",
            "why_a_en": "Correct. Gorwala Committee coined this historic verdict.",
            "why_a_ta": "சரி. கோர்வாலா குழு இந்த வரலாற்றுத் தீர்ப்பை வழங்கியது.",
            "why_b_en": "Incorrect. Maclagan Committee (1915) examined cooperative finance in British India.",
            "why_b_ta": "தவறு. மெக்லகன் குழு 1915-ல் பிரிட்டிஷ் இந்தியாவின் கூட்டுறவு நிதியை ஆய்வு செய்தது.",
            "why_c_en": "Incorrect. Nicholson's slogan was 'Find Raiffeisen' (1897).",
            "why_c_ta": "தவறு. நிக்கல்சனின் முழக்கம் 'ரைஃபெய்சனைக் கண்டறியுங்கள்' (1897).",
            "why_d_en": "Incorrect. Royal Commission (1928) stated 'if cooperation fails, there will fail the best hope of rural India'.",
            "why_d_ta": "தவறு. ராயல் கமிஷன் 1928-ல் 'கூட்டுறவு தோற்றால், கிராமப்புற இந்தியாவின் சிறந்த நம்பிக்கை தோற்கும்' என்றது.",
            "tip_en": "Gorwala Committee led to the nationalization of the Imperial Bank into the State Bank of India (SBI) in 1955 to support rural credit.",
            "tip_ta": "கோர்வாலா குழுவின் பரிந்துரைப்படியே கிராமப்புறக் கடனை ஆதரிக்க 1955-ல் இம்பீரியல் வங்கி பாரத ஸ்டேட் வங்கியாக (SBI) தேசியமயமாக்கப்பட்டது.",
            "fact_en": "It also recommended state partnership in the share capital of cooperative institutions.",
            "fact_ta": "கூட்டுறவு நிறுவனங்களின் பங்கு மூலதனத்தில் அரசின் பங்களிப்பையும் இக்குழு பரிந்துரைத்தது."
        },

        # 43. International Cooperative Day
        {
            "subtopic": "General Awareness & Principles",
            "stem_en": "On which day is the International Day of Cooperatives celebrated globally every year under United Nations auspices?",
            "stem_ta": "ஐக்கிய நாடுகள் சபையின் கீழ் ஆண்டுதோறும் சர்வதேச கூட்டுறவு தினம் உலகளவில் எந்த நாளில் கொண்டாடப்படுகிறது?",
            "options": [
                ("First Saturday of July", "ஜூலை மாதத்தின் முதல் சனிக்கிழமை"),
                ("First Monday of October", "அக்டோபர் மாதத்தின் முதல் திங்கட்கிழமை"),
                ("May 1st", "மே 1"),
                ("November 14th", "நவம்பர் 14")
            ],
            "correct_key": "A",
            "exp_en": "The International Day of Cooperatives is celebrated annually on the first Saturday of July, officially recognized by the United Nations General Assembly since 1995.",
            "exp_ta": "சர்வதேச கூட்டுறவு தினம் ஆண்டுதோறும் ஜூலை மாதத்தின் முதல் சனிக்கிழமை கொண்டாடப்படுகிறது; இது 1995 முதல் ஐக்கிய நாடுகள் பொதுச் சபையால் அதிகாரப்பூர்வமாக அங்கீகரிக்கப்பட்டது.",
            "why_a_en": "Correct. First Saturday of July is UN International Day of Cooperatives.",
            "why_a_ta": "சரி. ஜூலை முதல் சனிக்கிழமை ஐ.நா சர்வதேச கூட்டுறவு தினமாகும்.",
            "why_b_en": "Incorrect. First Monday of October is World Habitat Day.",
            "why_b_ta": "தவறு. அக்டோபர் முதல் திங்கள் உலக வாழ்விட நாள்.",
            "why_c_en": "Incorrect. May 1st is International Workers' Day.",
            "why_c_ta": "தவறு. மே 1 தொழிலாளர் தினம்.",
            "why_d_en": "Incorrect. In India, National Cooperative Week begins on November 14th.",
            "why_d_ta": "தவறு. இந்தியாவில் நவம்பர் 14 அன்று தேசிய கூட்டுறவு வாரம் தொடங்குகிறது.",
            "tip_en": "Global Day = First Saturday of July; Indian National Cooperative Week = 14 to 20 November.",
            "tip_ta": "உலக தினம் = ஜூலை முதல் சனிக்கிழமை; இந்திய தேசிய கூட்டுறவு வாரம் = நவம்பர் 14 முதல் 20 வரை.",
            "fact_en": "Year 2012 was declared by the UN as the 'International Year of Cooperatives'.",
            "fact_ta": "2012 ஆம் ஆண்டை ஐ.நா 'சர்வதேச கூட்டுறவு ஆண்டாக' அறிவித்தது."
        },

        # 44. Indian National Cooperative Week
        {
            "subtopic": "General Awareness & Principles",
            "stem_en": "During which dates is National Co-operative Week celebrated annually throughout India?",
            "stem_ta": "இந்தியா முழுவதும் ஆண்டுதோறும் தேசியக் கூட்டுறவு வாரம் எந்த நாட்களில் கொண்டாடப்படுகிறது?",
            "options": [
                ("November 14 to November 20", "நவம்பர் 14 முதல் நவம்பர் 20 வரை"),
                ("October 2 to October 8", "அக்டோபர் 2 முதல் அக்டோபர் 8 வரை"),
                ("January 26 to February 1", "ஜனவரி 26 முதல் பிப்ரவரி 1 வரை"),
                ("August 15 to August 21", "ஆகஸ்ட் 15 முதல் ஆகஸ்ட் 21 வரை")
            ],
            "correct_key": "A",
            "exp_en": "National Co-operative Week is celebrated every year from 14th November (commencing on the birthday of Jawaharlal Nehru) to 20th November across India.",
            "exp_ta": "தேசிய கூட்டுறவு வாரம் ஆண்டுதோறும் நவம்பர் 14 (ஜவஹர்லால் நேருவின் பிறந்த நாளில் தொடக்கம்) முதல் நவம்பர் 20 வரை இந்தியா முழுவதும் கொண்டாடப்படுகிறது.",
            "why_a_en": "Correct. November 14 to 20 is National Cooperative Week.",
            "why_a_ta": "சரி. நவம்பர் 14 முதல் 20 வரை தேசிய கூட்டுறவு வாரமாகும்.",
            "why_b_en": "Incorrect. October 2 to 8 is Wildlife Week.",
            "why_b_ta": "தவறு. அக்டோபர் 2 முதல் 8 வரை வனவிலங்கு வாரம்.",
            "why_c_en": "Incorrect. Dates are unrelated to cooperatives.",
            "why_c_ta": "தவறு. கூட்டுறவோடு தொடர்பற்ற தேதிகள்.",
            "why_d_en": "Incorrect. August 15 is Independence Day.",
            "why_d_ta": "தவறு. ஆகஸ்ட் 15 சுதந்திர தினம்.",
            "tip_en": "Nehru strongly advocated cooperatives: 'Convulse India with cooperation'.",
            "tip_ta": "நேரு கூட்டுறவை தீவிரமாக ஆதரித்தார்: 'கூட்டுறவு மூலம் இந்தியாவை எழுச்சியுறச் செய்யுங்கள்'.",
            "fact_en": "Cooperative Week is coordinated by the National Cooperative Union of India (NCUI).",
            "fact_ta": "கூட்டுறவு வாரத்தை இந்திய தேசிய கூட்டுறவு ஒன்றியம் (NCUI) ஒருங்கிணைக்கிறது."
        },

        # 45. Apex Body for Cooperative Education in India
        {
            "subtopic": "National Institutional Architecture",
            "stem_en": "Which organization serves as the apex body of the cooperative movement in India, representing all sectors of cooperatives and promoting cooperative education?",
            "stem_ta": "இந்தியாவில் கூட்டுறவு இயக்கத்தின் உச்ச அமைப்பாகச் செயல்பட்டு, அனைத்துக் கூட்டுறவுத் துறைகளையும் பிரதிநிதித்துவப்படுத்தி, கூட்டுறவுக் கல்வியை ஊக்குவிக்கும் அமைப்பு எது?",
            "options": [
                ("National Cooperative Union of India (NCUI)", "இந்திய தேசியக் கூட்டுறவு ஒன்றியம் (NCUI)"),
                ("National Cooperative Development Corporation (NCDC)", "தேசிய கூட்டுறவு வளர்ச்சிக் கழகம் (NCDC)"),
                ("NABARD", "நபார்டு (NABARD)"),
                ("TRIFED", "டிரைஃபெட் (TRIFED)")
            ],
            "correct_key": "A",
            "exp_en": "The National Cooperative Union of India (NCUI), established in 1929 (originally as All India Co-operative Institutes' Association), is the apex organization representing the entire Indian Cooperative Movement and leading cooperative education and training.",
            "exp_ta": "1929-ல் நிறுவப்பட்ட இந்திய தேசியக் கூட்டுறவு ஒன்றியம் (NCUI), முழு இந்தியக் கூட்டுறவு இயக்கத்தையும் பிரதிநிதித்துவப்படுத்தி கூட்டுறவுக் கல்வி மற்றும் பயிற்சியை வழிநடத்தும் உச்ச அமைப்பாகும்.",
            "why_a_en": "Correct. NCUI is the apex promotional and educational body.",
            "why_a_ta": "சரி. NCUI என்பது முதன்மை ஊக்குவிப்பு மற்றும் கல்வி உச்ச அமைப்பாகும்.",
            "why_b_en": "Incorrect. NCDC is a statutory financing corporation under the Ministry of Cooperation.",
            "why_b_ta": "தவறு. NCDC என்பது கூட்டுறவு அமைச்சகத்தின் கீழ் உள்ள சட்டப்பூர்வ நிதி உதவி நிறுவனம்.",
            "why_c_en": "Incorrect. NABARD is a development financial institution for agriculture and rural credit.",
            "why_c_ta": "தவறு. நபார்டு விவசாயம் மற்றும் ஊரகக் கடனுக்கான நிதி நிறுவனம்.",
            "why_d_en": "Incorrect. TRIFED promotes marketing of tribal produce.",
            "why_d_ta": "தவறு. டிரைஃபெட் பழங்குடியினரின் வன உற்பத்திப் பொருட்களை சந்தைப்படுத்துகிறது.",
            "tip_en": "NCUI runs the National Council for Cooperative Training (NCCT) and VAMNICOM Pune.",
            "tip_ta": "NCUI பூனேவில் உள்ள VAMNICOM மற்றும் தேசிய கூட்டுறவு பயிற்சிக் குழுவை (NCCT) நடத்துகிறது.",
            "fact_en": "NCUI is headquartered at Siri Fort in New Delhi.",
            "fact_ta": "NCUI-ன் தலைமை அலுவலகம் புது தில்லியில் உள்ள சிரி கோட்டையில் அமைந்துள்ளது."
        },

        # 46. National Cooperative Development Corporation (NCDC)
        {
            "subtopic": "National Institutional Architecture",
            "stem_en": "In which year was the National Cooperative Development Corporation (NCDC) set up as a statutory corporation by an Act of Parliament to finance cooperative programs?",
            "stem_ta": "கூட்டுறவுத் திட்டங்களுக்கு நிதியளிப்பதற்காக நாடாளுமன்றச் சட்டத்தின் மூலம் தேசிய கூட்டுறவு வளர்ச்சிக் கழகம் (NCDC) எந்த ஆண்டு சட்டப்பூர்வக் கழகமாக அமைக்கப்பட்டது?",
            "options": [
                ("1963", "1963"),
                ("1952", "1952"),
                ("1975", "1975"),
                ("1982", "1982")
            ],
            "correct_key": "A",
            "exp_en": "The National Cooperative Development Corporation (NCDC) was established in March 1963 under the National Cooperative Development Corporation Act, 1962, as a statutory corporation for planning and promoting programs for agricultural products and other notified commodities.",
            "exp_ta": "1962-ஆம் ஆண்டின் NCDC சட்டத்தின் கீழ் 1963 மார்ச் மாதத்தில் தேசிய கூட்டுறவு வளர்ச்சிக் கழகம் (NCDC) வேளாண் பொருட்கள் மற்றும் அறிவிக்கப்பட்ட பொருட்களுக்கான திட்டங்களைத் திட்டமிட்டு ஊக்குவிக்கும் சட்டப்பூர்வக் கழகமாக நிறுவப்பட்டது.",
            "why_a_en": "Correct. NCDC was established in 1963 under the 1962 Act.",
            "why_a_ta": "சரி. NCDC 1962 சட்டத்தின் கீழ் 1963-ல் நிறுவப்பட்டது.",
            "why_b_en": "Incorrect. 1952 is unrelated to NCDC.",
            "why_b_ta": "தவறு. 1952 NCDC உடன் தொடர்பற்றது.",
            "why_c_en": "Incorrect. 1975 was the year Regional Rural Banks were introduced.",
            "why_c_ta": "தவறு. 1975 பிராந்திய ஊரக வங்கிகள் அறிமுகப்படுத்தப்பட்ட ஆண்டு.",
            "why_d_en": "Incorrect. 1982 was the year NABARD was established.",
            "why_d_ta": "தவறு. 1982 நபார்டு அமைக்கப்பட்ட ஆண்டு.",
            "tip_en": "NCDC is known as the 'post office of cooperative credit' and now functions directly under the Ministry of Cooperation.",
            "tip_ta": "NCDC இப்போது நேரடியாக மத்திய கூட்டுறவு அமைச்சகத்தின் கீழ் செயல்படுகிறது.",
            "fact_en": "NCDC finances schemes like Sahakar Mitra and Yuva Sahakar.",
            "fact_ta": "NCDC சககார் மித்ரா மற்றும் யுவ சககார் போன்ற திட்டங்களுக்கு நிதியளிக்கிறது."
        },

        # 47. One Member, One Vote Principle
        {
            "subtopic": "Core Principles of Cooperation",
            "stem_en": "What fundamental democratic principle distinguishes a co-operative society from a joint stock commercial company?",
            "stem_ta": "ஒரு கூட்டுறவு சங்கத்தை ஒரு கூட்டுப் பங்கு வணிக நிறுவனத்திலிருந்து வேறுபடுத்தும் அடிப்படை ஜனநாயகக் கொள்கை எது?",
            "options": [
                ("'One Member, One Vote' irrespective of the number of shares held", "வைத்திருக்கும் பங்குகளின் எண்ணிக்கையைப் பொருட்படுத்தாமல் 'ஒரு உறுப்பினர், ஒரு வாக்கு'"),
                ("'One Share, One Vote' based on capital contributed", "வழங்கப்பட்ட மூலதனத்தின் அடிப்படையில் 'ஒரு பங்கு, ஒரு வாக்கு'"),
                ("Voting rights proportional to annual dividend earned", "ஈட்டப்பட்ட வருடாந்திர ஈவுத்தொகைக்கு ஏற்ப வாக்குரிமை"),
                ("Only founding promoters have voting rights", "நிறுவனர்களுக்கு மட்டுமே வாக்குரிமை உண்டு")
            ],
            "correct_key": "A",
            "exp_en": "In a co-operative society, democratic control is exercised on the basis of 'One Member, One Vote', ensuring that capital does not dominate member equality, unlike joint stock companies where voting power is proportional to shareholding ('One Share, One Vote').",
            "exp_ta": "ஒரு கூட்டுறவு சங்கத்தில், ஜனநாயகக் கட்டுப்பாடு 'ஒரு உறுப்பினர், ஒரு வாக்கு' என்ற அடிப்படையில் செயல்படுத்தப்படுகிறது; இது வணிக நிறுவனங்களைப் போலன்றி மூலதனம் உறுப்பினர்களின் சமத்துவத்தை ஆதிக்கம் செலுத்தாமல் இருப்பதை உறுதி செய்கிறது.",
            "why_a_en": "Correct. 'One Member, One Vote' is the cornerstone of cooperative democracy.",
            "why_a_ta": "சரி. 'ஒரு உறுப்பினர், ஒரு வாக்கு' என்பது கூட்டுறவு ஜனநாயகத்தின் அடித்தளமாகும்.",
            "why_b_en": "Incorrect. 'One Share, One Vote' applies to commercial companies.",
            "why_b_ta": "தவறு. 'ஒரு பங்கு, ஒரு வாக்கு' வணிக நிறுவனங்களுக்குப் பொருந்தும்.",
            "why_c_en": "Incorrect. Voting has no relation to dividends.",
            "why_c_ta": "தவறு. வாக்குரிமை ஈவுத்தொகையோடு தொடர்புடையது அல்ல.",
            "why_d_en": "Incorrect. Promoters have no superior voting rights.",
            "why_d_ta": "தவறு. நிறுவனர்களுக்கு எந்தவித மேலான வாக்குரிமையும் இல்லை.",
            "tip_en": "Cooperative = Association of persons (Human dignity); Joint Stock Company = Association of capital (Money power).",
            "tip_ta": "கூட்டுறவு = மனிதர்களின் கூட்டமைப்பு (மனிதாபிமானம்); நிறுவனம் = மூலதனத்தின் கூட்டமைப்பு (பணபலம்).",
            "fact_en": "No member can dominate a cooperative through disproportionate share accumulation.",
            "fact_ta": "அதிகப்படியான பங்குகளைக் குவிப்பதன் மூலம் எந்த ஒரு உறுப்பினரும் கூட்டுறவை ஆதிக்கம் செலுத்த முடியாது."
        },

        # 48. Maximum Shareholding Limit
        {
            "subtopic": "Core Principles of Cooperation",
            "stem_en": "To prevent concentration of control in a few hands, state cooperative laws typically restrict an individual member's shareholding to what maximum limit of total share capital?",
            "stem_ta": "சில நபர்களின் கைகளில் கட்டுப்பாடு குவிவதைத் தடுக்க, மாநிலக் கூட்டுறவுச் சட்டங்கள் பொதுவாக ஒரு தனிநபர் உறுப்பினரின் பங்கு மூலதனத்தை மொத்தப் பங்கு மூலதனத்தில் அதிகபட்சமாக எத்தனை சதவீதமாகக் கட்டுப்படுத்துகின்றன?",
            "options": [
                ("Not exceeding 20% (one-fifth) of total share capital", "மொத்த பங்கு மூலதனத்தில் 20%-க்கு (ஐந்தில் ஒரு பங்கு) மிகாமல்"),
                ("Up to 51% of total share capital", "மொத்த பங்கு மூலதனத்தில் 51% வரை"),
                ("Up to 75% of total share capital", "மொத்த பங்கு மூலதனத்தில் 75% வரை"),
                ("No limit on shareholding", "பங்கு மூலதனத்திற்கு எவ்வித வரம்பும் இல்லை")
            ],
            "correct_key": "A",
            "exp_en": "Section 5 of the Cooperative Societies Act 1912 and state laws (including TN Act 1983) stipulate that no individual member shall hold more than one-fifth (20%) of the total share capital of the society, preventing hostile takeovers or capitalist domination.",
            "exp_ta": "1912 கூட்டுறவுச் சட்டத்தின் பிரிவு 5 மற்றும் மாநிலச் சட்டங்கள் (TN சட்டம் 1983 உட்பட) எந்தவொரு தனிநபர் உறுப்பினரும் சங்கத்தின் மொத்த பங்கு மூலதனத்தில் ஐந்தில் ஒரு பங்குக்கு (20%) மேல் வைத்திருக்கக் கூடாது என்று நிர்ணயிக்கின்றன.",
            "why_a_en": "Correct. Individual shareholding is capped at 20% (one-fifth).",
            "why_a_ta": "சரி. தனிநபர் பங்கு மூலதனம் 20%-க்கு மேல் இருக்கக் கூடாது.",
            "why_b_en": "Incorrect. 51% would give absolute ownership control, contrary to cooperative ethos.",
            "why_b_ta": "தவறு. 51% முழு கட்டுப்பாட்டை அளித்துவிடும், இது கூட்டுறவுக் கொள்கைக்கு எதிரானது.",
            "why_c_en": "Incorrect. 75% applies to special resolutions in company law.",
            "why_c_ta": "தவறு. 75% நிறுவனச் சட்டத்தின் சிறப்புத் தீர்மானங்களுக்குப் பொருந்தும்.",
            "why_d_en": "Incorrect. Uncapped shareholding is strictly prohibited in cooperatives.",
            "why_d_ta": "தவறு. வரம்பற்ற பங்கு மூலதனம் கூட்டுறவுகளில் கண்டிப்பாகத் தடை செய்யப்பட்டுள்ளது.",
            "tip_en": "Even if a member holds the maximum 20% shares, they still have only ONE vote.",
            "tip_ta": "ஒரு உறுப்பினர் அதிகபட்சமாக 20% பங்குகளை வைத்திருந்தாலும், அவருக்கு ஒரு வாக்கு மட்டுமே உண்டு.",
            "fact_en": "Government and institutional bodies may hold higher shares under statutory partnership schemes.",
            "fact_ta": "சட்டப்பூர்வ பங்குதாரர் திட்டங்களின் கீழ் அரசும் நிறுவன அமைப்புகளும் அதிக பங்குகளை வைத்திருக்கலாம்."
        },

        # 49. Cooperative Principles and ICA
        {
            "subtopic": "Core Principles of Cooperation",
            "stem_en": "How many Statement of Cooperative Identity principles are currently recognized globally by the International Co-operative Alliance (ICA)?",
            "stem_ta": "சர்வதேச கூட்டுறவு கூட்டணியால் (ICA) தற்போது உலகளவில் எத்தனை கூட்டுறவு அடையாளக் கொள்கைகள் அங்கீகரிக்கப்பட்டுள்ளன?",
            "options": [
                ("7 Principles", "7 கொள்கைகள்"),
                ("5 Principles", "5 கொள்கைகள்"),
                ("10 Principles", "10 கொள்கைகள்"),
                ("12 Principles", "12 கொள்கைகள்")
            ],
            "correct_key": "A",
            "exp_en": "The International Co-operative Alliance (ICA) adopted 7 cooperative principles in Manchester in 1995: 1. Voluntary & Open Membership, 2. Democratic Member Control, 3. Member Economic Participation, 4. Autonomy & Independence, 5. Education, Training & Information, 6. Cooperation among Cooperatives, 7. Concern for Community.",
            "exp_ta": "1995-ல் மான்செஸ்டரில் சர்வதேச கூட்டுறவு கூட்டணி (ICA) 7 கூட்டுறவுக் கொள்கைகளை ஏற்றுக்கொண்டது: 1. தன்னார்வ மற்றும் திறந்த உறுப்பினர் சேர்க்கை, 2. ஜனநாயக உறுப்பினர் கட்டுப்பாடு, 3. உறுப்பினர் பொருளாதாரப் பங்களிப்பு, 4. தன்னாட்சி மற்றும் சுதந்திரம், 5. கல்வி, பயிற்சி மற்றும் தகவல், 6. கூட்டுறவுகளுக்கு இடையே கூட்டுறவு, 7. சமூகத்தின் மீதான அக்கறை.",
            "why_a_en": "Correct. Exactly 7 ICA principles govern modern cooperatives.",
            "why_a_ta": "சரி. சரியாக 7 ICA கொள்கைகள் நவீன கூட்டுறவுகளை நிர்வகிக்கின்றன.",
            "why_b_en": "Incorrect. 5 is incorrect.",
            "why_b_ta": "தவறு. 5 தவறானது.",
            "why_c_en": "Incorrect. 10 is incorrect.",
            "why_c_ta": "தவறு. 10 தவறானது.",
            "why_d_en": "Incorrect. 12 is incorrect.",
            "why_d_ta": "தவறு. 12 தவறானது.",
            "tip_en": "Remember the 7th principle: 'Concern for Community' (sustainable development).",
            "tip_ta": "7-வது கொள்கையை நினைவில் கொள்க: 'சமூகத்தின் மீதான அக்கறை' (நிலையான வளர்ச்சி).",
            "fact_en": "These principles were incorporated into Article 243ZI by the 97th Constitutional Amendment.",
            "fact_ta": "இந்தக் கொள்கைகள் 97வது அரசியலமைப்புத் திருத்தத்தின் மூலம் சரத்து 243ZI-ல் இணைக்கப்பட்டன."
        },

        # 50. Supreme Court Bench in Rajendra N. Shah (2021)
        {
            "subtopic": "Judicial Pronouncements - Landmark Ruling",
            "stem_en": "In the landmark verdict of Union of India v. Rajendra N. Shah (July 2021), what was the size of the Supreme Court Bench that delivered the judgment?",
            "stem_ta": "மத்திய அரசு v. ராஜேந்திர என். ஷா (ஜூலை 2021) வரலாற்றுச் சிறப்புமிக்க தீர்ப்பில், தீர்ப்பை வழங்கிய உச்ச நீதிமன்ற அமர்வின் நீதிபதிகளின் எண்ணிக்கை யாது?",
            "options": [
                ("3-Judge Bench", "3 நீதிபதிகள் கொண்ட அமர்வு"),
                ("5-Judge Constitution Bench", "5 நீதிபதிகள் கொண்ட அரசியலமைப்பு அமர்வு"),
                ("2-Judge Division Bench", "2 நீதிபதிகள் கொண்ட அமர்வு"),
                ("7-Judge Bench", "7 நீதிபதிகள் கொண்ட அமர்வு")
            ],
            "correct_key": "A",
            "exp_en": "Union of India v. Rajendra N. Shah (decided on 20 July 2021) was adjudicated by a 3-Judge Bench comprising Justice R.F. Nariman, Justice K.M. Joseph, and Justice B.R. Gavai (with a 2:1 majority ruling on severability).",
            "exp_ta": "மத்திய அரசு v. ராஜேந்திர என். ஷா (2021 ஜூலை 20 அன்று தீர்ப்பளிக்கப்பட்டது) நீதிபதி ஆர்.எஃப். நாரிமன், நீதிபதி கே.எம். ஜோசப் மற்றும் நீதிபதி பி.ஆர். கவாய் ஆகியோர் அடங்கிய 3 நீதிபதிகள் கொண்ட அமர்வால் விசாரிக்கப்பட்டது (பிரித்தெடுப்புக் கோட்பாட்டில் 2:1 பெரும்பான்மை தீர்ப்பு).",
            "why_a_en": "Correct. It was delivered by a 3-Judge Bench headed by Justice R.F. Nariman.",
            "why_a_ta": "சரி. நீதிபதி ஆர்.எஃப். நாரிமன் தலைமையிலான 3 நீதிபதிகள் கொண்ட அமர்வால் வழங்கப்பட்டது.",
            "why_b_en": "Incorrect. It was a 3-Judge Bench, not a 5-Judge Constitution Bench.",
            "why_b_ta": "தவறு. இது 3 நீதிபதிகள் கொண்ட அமர்வு, 5 நீதிபதிகள் கொண்ட அரசியலமைப்பு அமர்வு அல்ல.",
            "why_c_en": "Incorrect. It had three judges, not two.",
            "why_c_ta": "தவறு. இதில் மூன்று நீதிபதிகள் இருந்தனர், இரண்டு அல்ல.",
            "why_d_en": "Incorrect. 7-Judge bench is incorrect.",
            "why_d_ta": "தவறு. 7 நீதிபதிகள் அமர்வு அல்ல.",
            "tip_en": "Justice R.F. Nariman and Justice B.R. Gavai formed the majority; Justice K.M. Joseph dissented on severability holding the entire Part IX-B unconstitutional.",
            "tip_ta": "நீதிபதிகள் நாரிமன் மற்றும் கவாய் பெரும்பான்மை தீர்ப்பளித்தனர்; நீதிபதி கே.எம். ஜோசப் பகுதி IX-B முழுவதுமே செல்லாது என மாறுபட்ட தீர்ப்பை அளித்தார்.",
            "fact_en": "The judgment originated from a 2013 Gujarat High Court verdict striking down the 97th Amendment.",
            "fact_ta": "இத்தீர்ப்பு 97வது திருத்தத்தை ரத்து செய்த 2013 குஜராத் உயர் நீதிமன்றத் தீர்ப்பின் மேல்முறையீடாகும்."
        }
    ]


def build_easy_file():
    raw_qs = get_easy_raw_questions()
    print(f"Loaded {len(raw_qs)} raw Easy questions.")
    assert len(raw_qs) == 50, f"Expected 50 questions, got {len(raw_qs)}"

    questions = []
    for idx, item in enumerate(raw_qs, start=1):
        qid = f"CS_E_{idx:03d}"
        opts = item["options"]
        correct_key = item["correct_key"]

        q = make_coop_q(
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
            tags=["polity", "cooperative_societies", "easy", item["subtopic"].lower().replace(" ", "_")]
        )
        questions.append(q)

    # Randomize and balance answer keys: 12-13 per option, max run <= 2
    balanced = randomize_and_balance_dataset(questions, seed=42)
    key_dist = Counter(q["correct_answer"] for q in balanced)
    print(f"Balanced Key Distribution: {dict(key_dist)}")

    out_dir = os.path.join("data", "questions", "polity")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "cooperative_societies_easy.json")

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(balanced, f, ensure_ascii=False, indent=2)
    print(f"Saved balanced Easy MCQs to {out_path}")

    # Validation
    rep = ContentValidator.validate_file(out_path, expected_count=50, expected_prefix="CS_E_")
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
