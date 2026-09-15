# -*- coding: utf-8 -*-
"""
Co-operative Societies - Part 3: Grand Test Batch 1 (Questions 1 to 50: CS_GT_001 to CS_GT_050)
TNPSC Nova AI Content Engine
"""


def get_gt_batch1_raw():
    return [
        # GT 1
        {
            "subtopic": "Constitutional Amendment and Insertion",
            "stem_en": "Which constitutional amendment bill was introduced in the Lok Sabha in 2009 that eventually became the 97th Constitutional Amendment Act, 2011?",
            "stem_ta": "2009-ஆம் ஆண்டு மக்களவையில் அறிமுகப்படுத்தப்பட்டு பின்னர் 2011-ஆம் ஆண்டின் 97-வது அரசியலமைப்புத் திருத்தச் சட்டமாக மாறிய அரசியலமைப்புத் திருத்த மசோதா எது?",
            "options": [
                ("111th Constitutional Amendment Bill", "111-வது அரசியலமைப்பு திருத்த மசோதா"),
                ("108th Constitutional Amendment Bill", "108-வது அரசியலமைப்பு திருத்த மசோதா"),
                ("115th Constitutional Amendment Bill", "115-வது அரசியலமைப்பு திருத்த மசோதா"),
                ("117th Constitutional Amendment Bill", "117-வது அரசியலமைப்பு திருத்த மசோதா")
            ],
            "correct_key": "A",
            "exp_en": "The Constitution (One Hundred and Eleventh Amendment) Bill, 2009 was introduced in the Lok Sabha on 30 November 2009. It was enacted in December 2011 as the 97th Constitutional Amendment Act.",
            "exp_ta": "அரசியலமைப்பு (111-வது திருத்தம்) மசோதா 2009 நவம்பர் 30 அன்று மக்களவையில் அறிமுகப்படுத்தப்பட்டு, டிசம்பர் 2011-ல் 97-வது அரசியலமைப்புத் திருத்தச் சட்டமாக நிறைவேறியது.",
            "why_a_en": "Correct. 111th Amendment Bill became the 97th Amendment Act.",
            "why_a_ta": "சரி. 111வது திருத்த மசோதாவே 97வது திருத்தச் சட்டமாக மாறியது.",
            "why_b_en": "Incorrect. 108th Bill was the Women's Reservation Bill 2008.",
            "why_b_ta": "தவறு. 108வது மசோதா மகளிர் இடஒதுக்கீடு மசோதா.",
            "why_c_en": "Incorrect. 115th Bill dealt with GST introduction.",
            "why_c_ta": "தவறு. 115வது மசோதா ஜிஎஸ்டி பற்றியது.",
            "why_d_en": "Incorrect. 117th Bill dealt with reservation in promotions for SC/ST.",
            "why_d_ta": "தவறு. 117வது மசோதா பதவி உயர்வில் இடஒதுக்கீடு பற்றியது.",
            "tip_en": "Bill No. = 111th Amendment Bill (2009) → Act No. = 97th Constitutional Amendment Act (2011).",
            "tip_ta": "மசோதா எண் = 111 (2009) → சட்ட எண் = 97 (2011).",
            "fact_en": "The Bill was referred to the Standing Committee on Agriculture headed by Basudeb Acharia.",
            "fact_ta": "இம்மசோதா பாசுதேவ் ஆச்சார்யா தலைமையிலான வேளாண் நிலைக்குழுவின் ஆய்வுக்கு அனுப்பப்பட்டது."
        },

        # GT 2
        {
            "subtopic": "Scope of Part IX-B Post-2021",
            "stem_en": "Following the 2021 Supreme Court verdict in Union of India v. Rajendra N. Shah, which category of co-operative societies continues to be directly governed by Part IX-B of the Constitution?",
            "stem_ta": "2021 உச்சநீதிமன்றத்தின் இந்திய ஒன்றியம் எதிர் ராஜேந்திர என். ஷா தீர்ப்பிற்குப் பிறகு, எந்த வகைக் கூட்டுறவு சங்கங்கள் அரசியலமைப்பின் பகுதி IX-B-ஆல் தொடர்ந்து நேரடியாக நிர்வகிக்கப்படுகின்றன?",
            "options": [
                ("Multi-State Co-operative Societies and Co-operatives in Union Territories", "பல மாநில கூட்டுறவு சங்கங்கள் மற்றும் யூனியன் பிரதேசங்களில் உள்ள கூட்டுறவு சங்கங்கள்"),
                ("Primary Agricultural Credit Societies in all States", "அனைத்து மாநிலங்களிலும் உள்ள தொடக்க வேளாண்மைக் கடன் சங்கங்கள்"),
                ("District Central Co-operative Banks in non-scheduled areas", "பட்டியலிடப்படாத பகுதிகளில் உள்ள மாவட்ட மத்தியக் கூட்டுறவு வங்கிகள்"),
                ("State Apex Co-operative Federations", "மாநில தலைமை கூட்டுறவு கூட்டமைப்புகள்")
            ],
            "correct_key": "A",
            "exp_en": "The Supreme Court applied the Doctrine of Severability to uphold Part IX-B exclusively for Multi-State Co-operative Societies (List I Entry 44) and co-operatives in Union Territories (Article 246(4)).",
            "exp_ta": "பிரித்தெடுக்கும் கோட்பாட்டைப் பயன்படுத்தி, பல மாநில கூட்டுறவு சங்கங்கள் மற்றும் யூனியன் பிரதேசங்களில் உள்ள சங்கங்களுக்கு மட்டுமே பகுதி IX-B செல்லும் என உச்சநீதிமன்றம் தீர்ப்பளித்தது.",
            "why_a_en": "Correct. Multi-State Cooperatives and UT cooperatives remain under Part IX-B.",
            "why_a_ta": "சரி. பல மாநில கூட்டுறவு மற்றும் யூனியன் பிரதேச சங்கங்கள் மட்டுமே பகுதி IX-B-ன் கீழ் உள்ளன.",
            "why_b_en": "Incorrect. State cooperatives fall outside Part IX-B post-2021.",
            "why_b_ta": "தவறு. மாநிலக் கூட்டுறவுகள் பகுதி IX-B-லிருந்து நீக்கப்பட்டுவிட்டன.",
            "why_c_en": "Incorrect. DCCBs are state cooperatives under List II Entry 32.",
            "why_c_ta": "தவறு. DCCB வங்கிகள் மாநிலப் பட்டியல் பதிவு 32-ன் கீழ் வருகின்றன.",
            "why_d_en": "Incorrect. State apex federations are governed by State Acts.",
            "why_d_ta": "தவறு. மாநில தலைமை கூட்டமைப்புகள் மாநில சட்டங்களால் ஆளப்படுகின்றன.",
            "tip_en": "Severability Outcome: Part IX-B = Upheld for Multi-State + UTs; Struck down for State Cooperatives.",
            "tip_ta": "பிரித்தெடுக்கும் முடிவு: பகுதி IX-B = பல மாநிலம் & யூனியன் பிரதேசங்களுக்கு செல்லும்; மாநிலக் கூட்டுறவுகளுக்கு செல்லாது.",
            "fact_en": "The judgment was delivered on 20 July 2021 by a 2:1 majority.",
            "fact_ta": "இத்தீர்ப்பு 2021 ஜூலை 20 அன்று 2:1 பெரும்பான்மையில் வழங்கப்பட்டது."
        },

        # GT 3
        {
            "subtopic": "Article 19(1)(c) Scope",
            "stem_en": "Under Article 19(1)(c), the right to form cooperative societies is available to:",
            "stem_ta": "அரசியலமைப்பு உறுப்பு 19(1)(c)-ன் கீழ், கூட்டுறவு சங்கங்களை அமைக்கும் உரிமை யாருக்குக் கிடைக்கிறது?",
            "options": [
                ("Citizens of India only", "இந்தியக் குடிமக்களுக்கு மட்டுமே"),
                ("Both citizens and foreigners residing in India", "இந்தியாவில் வசிக்கும் குடிமக்கள் மற்றும் வெளிநாட்டினர் இருவருக்கும்"),
                ("Registered companies and corporations only", "பதிவு செய்யப்பட்ட நிறுவனங்கள் மற்றும் கழகங்களுக்கு மட்டுமே"),
                ("Non-resident Indians and Persons of Indian Origin only", "வெளிநாடு வாழ் இந்தியர்கள் மற்றும் இந்திய வம்சாவளியினருக்கு மட்டுமே")
            ],
            "correct_key": "A",
            "exp_en": "Fundamental rights under Article 19 (including the right to form associations, unions, or co-operative societies) are fundamental freedoms available exclusively to citizens of India.",
            "exp_ta": "உறுப்பு 19-ன் கீழ் உள்ள அடிப்படை உரிமைகள் (கூட்டுறவு அமைக்கும் உரிமை உட்பட) இந்தியக் குடிமக்களுக்கு மட்டுமே பிரத்யேகமாகக் கிடைக்கின்றன.",
            "why_a_en": "Correct. Article 19 rights are confined solely to Indian citizens.",
            "why_a_ta": "சரி. உறுப்பு 19 உரிமைகள் இந்திய குடிமக்களுக்கு மட்டுமே உரியது.",
            "why_b_en": "Incorrect. Article 19 does not extend to foreign nationals.",
            "why_b_ta": "தவறு. வெளிநாட்டினருக்கு உறுப்பு 19 பொருந்தாது.",
            "why_c_en": "Incorrect. Corporations are artificial legal entities and not citizens under Article 19.",
            "why_c_ta": "தவறு. நிறுவனங்கள் குடிமக்கள் அல்ல.",
            "why_d_en": "Incorrect. Confined to Indian citizens generally.",
            "why_d_ta": "தவறு. பொதுவாக இந்திய குடிமக்கள் அனைவருக்கும் உரியது.",
            "tip_en": "Rights exclusively for citizens: Articles 15, 16, 19, 29, and 30.",
            "tip_ta": "குடிமக்களுக்கு மட்டுமேயான அடிப்படை உரிமைகள்: உறுப்புகள் 15, 16, 19, 29 மற்றும் 30.",
            "fact_en": "The Supreme Court in State Trading Corporation v. CTO held that corporate entities cannot claim Article 19 citizenship.",
            "fact_ta": "வணிகக் கழகங்கள் உறுப்பு 19-ன் கீழ் குடியுரிமை கோர முடியாது என உச்சநீதிமன்றம் தீர்ப்பளித்துள்ளது."
        },

        # GT 4
        {
            "subtopic": "Board Ceilings and Reservations",
            "stem_en": "If a cooperative society has 21 elected directors, what is the maximum permissible total board strength including statutory co-opted expert members under Article 243ZJ?",
            "stem_ta": "ஒரு கூட்டுறவு சங்கம் 21 தேர்ந்தெடுக்கப்பட்ட இயக்குநர்களைக் கொண்டிருந்தால், உறுப்பு 243ZJ-ன் கீழ் சட்டப்பூர்வ இணை நிபுணர் உறுப்பினர்களையும் சேர்த்து அதிகபட்ச வாரிய பலம் எவ்வளவாக இருக்க முடியும்?",
            "options": [
                ("23 members", "23 உறுப்பினர்கள்"),
                ("21 members", "21 உறுப்பினர்கள்"),
                ("25 members", "25 உறுப்பினர்கள்"),
                ("22 members", "22 உறுப்பினர்கள்")
            ],
            "correct_key": "A",
            "exp_en": "Under Article 243ZJ(1), the maximum number of directors is 21. In addition, the second proviso permits co-opting up to 2 expert members. Thus, 21 + 2 = 23 members total.",
            "exp_ta": "உறுப்பு 243ZJ(1)-ன் படி அதிகபட்ச இயக்குநர்கள் 21 பேர். கூடுதலாக 2 நிபுணர்களை இணைத்துக் கொள்ளலாம். எனவே மொத்த உச்ச வரம்பு 21 + 2 = 23 உறுப்பினர்கள் ஆகும்.",
            "why_a_en": "Correct. 21 elected directors + up to 2 co-opted members = 23 total strength.",
            "why_a_ta": "சரி. 21 தேர்ந்தெடுக்கப்பட்ட இயக்குநர்கள் + 2 இணை உறுப்பினர்கள் = மொத்தம் 23 பேர்.",
            "why_b_en": "Incorrect. 21 is the ceiling excluding co-opted members.",
            "why_b_ta": "தவறு. 21 என்பது இணை உறுப்பினர்கள் இல்லாத வரம்பு.",
            "why_c_en": "Incorrect. 25 is beyond the constitutional limit.",
            "why_c_ta": "தவறு. 25 அரசமைப்பு வரம்பை மீறியது.",
            "why_d_en": "Incorrect. Co-opted limit is 2, not 1.",
            "why_d_ta": "தவறு. இணை உறுப்பினர்கள் வரம்பு 2 ஆகும்.",
            "tip_en": "Math for Board: 21 (Elected max) + 2 (Co-opted max) = 23 Total.",
            "tip_ta": "வாரியக் கணக்கு: 21 (தேர்ந்தெடுக்கப்பட்டவர்) + 2 (இணை உறுப்பினர்) = மொத்தம் 23.",
            "fact_en": "Co-opted members cannot vote in office-bearer elections.",
            "fact_ta": "இணை உறுப்பினர்கள் நிர்வாகி தேர்தலில் வாக்களிக்க முடியாது."
        },

        # GT 5
        {
            "subtopic": "Article 243ZH Definitions",
            "stem_en": "In Article 243ZH of the Constitution, how is 'board' defined?",
            "stem_ta": "அரசியலமைப்பு உறுப்பு 243ZH-ல் 'வாரியம்' (board) எவ்வாறு வரையறுக்கப்பட்டுள்ளது?",
            "options": [
                ("The governing body of a co-operative society to which the direction and control of the management of the affairs of a society is entrusted", "ஒரு கூட்டுறவு சங்கத்தின் விவகாரங்களை வழிநடத்தும் மற்றும் நிர்வகிக்கும் அதிகாரம் ஒப்படைக்கப்பட்ட அதன் நிர்வாக அமைப்பு"),
                ("A committee formed exclusively of government nominees", "அரசு நியமன உறுப்பினர்களை மட்டுமே கொண்ட ஒரு குழு"),
                ("The general body of all voting members assembled in a meeting", "கூட்டத்தில் கூடியுள்ள அனைத்து வாக்களிக்கும் உறுப்பினர்களின் பொதுக்குழு"),
                ("A tribunal appointed by the High Court to arbitrate society disputes", "சங்கத் தகராறுகளைத் தீர்க்க உயர்நீதிமன்றத்தால் நியமிக்கப்படும் ஒரு தீர்ப்பாயம்")
            ],
            "correct_key": "A",
            "exp_en": "Article 243ZH(a) defines 'board' as the governing body of a co-operative society, by whatever name called, to which the direction and control of the management of the affairs of a society is entrusted.",
            "exp_ta": "உறுப்பு 243ZH(a)-ன் படி, எந்தப் பெயரால் அழைக்கப்பட்டாலும், சங்கத்தின் விவகாரங்களை வழிநடத்தும் மற்றும் மேலாண்மை செய்யும் அதிகாரம் ஒப்படைக்கப்பட்ட நிர்வாகக் குழுவே 'வாரியம்' ஆகும்.",
            "why_a_en": "Correct. Verbatim definition from Article 243ZH(a).",
            "why_a_ta": "சரி. உறுப்பு 243ZH(a)-ன் துல்லியமான அரசமைப்பு வரையறை.",
            "why_b_en": "Incorrect. The board is primarily an elected body, not government nominees.",
            "why_b_ta": "தவறு. வாரியம் என்பது தேர்ந்தெடுக்கப்படும் அமைப்பு.",
            "why_c_en": "Incorrect. The general body is distinct from the board.",
            "why_c_ta": "தவறு. பொதுக்குழு என்பது வாரியத்திலிருந்து வேறுபட்டது.",
            "why_d_en": "Incorrect. Tribunals are separate judicial bodies.",
            "why_d_ta": "தவறு. தீர்ப்பாயங்கள் தனி நீதித்துறை அமைப்புகள்.",
            "tip_en": "Article 243ZH Definitions: Board = Governing body; Member = Admitted person; Office bearer = President/VP/Secretary.",
            "tip_ta": "உறுப்பு 243ZH வரையறைகள்: வாரியம் = நிர்வாகக் குழு; உறுப்பினர் = சேர்ந்த நபர்; நிர்வாகி = தலைவர்/துணைத் தலைவர்/செயலாளர்.",
            "fact_en": "The definition accommodates varied state nomenclature such as 'Managing Committee', 'Board of Directors', etc.",
            "fact_ta": "மேலாண்மைக் குழு, இயக்குநர் குழு போன்ற பல்வேறு மாநிலப் பெயர்களை உள்ளடக்கும் வகையில் இது வரையறுக்கப்பட்டுள்ளது."
        },

        # GT 6
        {
            "subtopic": "Multi-State Co-operative Societies 2023 Authority",
            "stem_en": "Under the Multi-State Co-operative Societies (Amendment) Act, 2023, the Co-operative Election Authority consists of a Chairperson, a Vice-Chairperson, and how many other members?",
            "stem_ta": "பல மாநில கூட்டுறவு சங்கங்கள் (திருத்தச்) சட்டம் 2023-ன் கீழ், கூட்டுறவு தேர்தல் ஆணையம் ஒரு தலைவர், ஒரு துணைத் தலைவர் மற்றும் எத்தனை உறுப்பினர்களைக் கொண்டுள்ளது?",
            "options": [
                ("Up to three members", "அதிகபட்சம் மூன்று உறுப்பினர்கள்"),
                ("Up to five members", "அதிகபட்சம் ஐந்து உறுப்பினர்கள்"),
                ("One member only", "ஒரு உறுப்பினர் மட்டுமே"),
                ("Up to seven members", "அதிகபட்சம் ஏழு உறுப்பினர்கள்")
            ],
            "correct_key": "A",
            "exp_en": "Under Section 45 of the amended MSCS Act, the Central Government establishes the Co-operative Election Authority comprising a Chairperson, a Vice-Chairperson, and not exceeding three members.",
            "exp_ta": "திருத்தப்பட்ட பல மாநில கூட்டுறவு சங்கங்கள் சட்டத்தின் பிரிவு 45-ன் படி, தேர்தல் ஆணையம் ஒரு தலைவர், ஒரு துணைத் தலைவர் மற்றும் மூன்றுக்கு மிகாத உறுப்பினர்களைக் கொண்டுள்ளது.",
            "why_a_en": "Correct. Chairperson + Vice-Chairperson + up to 3 members.",
            "why_a_ta": "சரி. தலைவர் + துணைத் தலைவர் + அதிகபட்சம் 3 உறுப்பினர்கள்.",
            "why_b_en": "Incorrect. Not five members.",
            "why_b_ta": "தவறு. ஐந்து உறுப்பினர்கள் அல்ல.",
            "why_c_en": "Incorrect. Not one member.",
            "why_c_ta": "தவறு. ஒரு உறுப்பினர் அல்ல.",
            "why_d_en": "Incorrect. Seven is incorrect.",
            "why_d_ta": "தவறு. ஏழு என்பது தவறானது.",
            "tip_en": "MSCS Election Authority: 1 Chairperson + 1 Vice-Chairperson + Max 3 Members = Max 5 individuals.",
            "tip_ta": "தேர்தல் ஆணைய கட்டமைப்பு: 1 தலைவர் + 1 துணைத் தலைவர் + அதிகபட்சம் 3 உறுப்பினர்கள் = மொத்தம் 5 பேர்.",
            "fact_en": "The Chairperson must have held the post of Additional Secretary to the Government of India or equivalent.",
            "fact_ta": "தலைவர் கூடுதல் செயலாளர் அல்லது அதற்கு இணையான பதவியை வகித்தவராக இருக்க வேண்டும்."
        },

        # GT 7
        {
            "subtopic": "Rehabilitation Fund Contribution",
            "stem_en": "What percentage of annual net profit must a profitable multi-state cooperative society contribute to the Co-operative Rehabilitation, Reconstruction and Development Fund under the 2023 MSCS Amendment?",
            "stem_ta": "2023 திருத்தச் சட்டத்தின் கீழ், லாபகரமாக இயங்கும் பல மாநில கூட்டுறவு சங்கம் தனது வருடாந்திர நிகர லாபத்தில் எத்தனை சதவீதத்தை கூட்டுறவு மறுவாழ்வு மற்றும் மேம்பாட்டு நிதிக்கு வழங்க வேண்டும்?",
            "options": [
                ("1% of net profits", "நிகர லாபத்தில் 1%"),
                ("5% of net profits", "நிகர லாபத்தில் 5%"),
                ("2% of net profits", "நிகர லாபத்தில் 2%"),
                ("10% of net profits", "நிகர லாபத்தில் 10%")
            ],
            "correct_key": "A",
            "exp_en": "Under the 2023 Amendment to the MSCS Act, multi-state cooperative societies that have generated net profits in the preceding three consecutive financial years must contribute 1% of net profits or ₹1 crore (whichever is less) to the Cooperative Rehabilitation Fund.",
            "exp_ta": "2023 திருத்தத்தின்படி, கடந்த 3 ஆண்டுகளாக லாபம் ஈட்டும் பல மாநில கூட்டுறவு சங்கங்கள் தங்களின் நிகர லாபத்தில் 1% அல்லது ₹1 கோடி (எது குறைவோ அதை) மறுவாழ்வு நிதிக்கு வழங்க வேண்டும்.",
            "why_a_en": "Correct. 1% of net profits is the statutory contribution rate.",
            "why_a_ta": "சரி. நிகர லாபத்தில் 1% சட்டப்பூர்வ பங்களிப்பு விகிதமாகும்.",
            "why_b_en": "Incorrect. 5% is not the statutory rate.",
            "why_b_ta": "தவறு. 5% தவறான விகிதம்.",
            "why_c_en": "Incorrect. 2% is the standard CSR rate under Section 135 of Companies Act, not the cooperative rehabilitation levy.",
            "why_c_ta": "தவறு. 2% என்பது நிறுவனங்களின் CSR விகிதம்.",
            "why_d_en": "Incorrect. 10% is incorrect.",
            "why_d_ta": "தவறு. 10% தவறானது.",
            "tip_en": "Don't confuse: Companies Act CSR = 2% of average net profits; MSCS Rehabilitation Fund = 1% of net profits.",
            "tip_ta": "குழப்ப வேண்டாம்: நிறுவனங்களின் CSR = 2%; கூட்டுறவு மறுவாழ்வு நிதி = 1%.",
            "fact_en": "This fund is used to revive sick multi-state cooperative societies.",
            "fact_ta": "நலிவடைந்த பல மாநில கூட்டுறவு சங்கங்களை மீண்டும் சீரமைக்க இந்நிதி பயன்படுத்தப்படுகிறது."
        },

        # GT 8
        {
            "subtopic": "Supreme Court Bench in 2021",
            "stem_en": "Which Supreme Court Justice delivered a partial dissent in Union of India v. Rajendra N. Shah (2021), holding that Part IX-B could not be severed and should be struck down in its entirety?",
            "stem_ta": "இந்திய ஒன்றியம் எதிர் ராஜேந்திர என். ஷா (2021) வழக்கில், பகுதி IX-B-ஐப் பிரிக்க முடியாது என்றும் அது முழுமையாக ரத்து செய்யப்பட வேண்டும் என்றும் மாறுபட்ட தீர்ப்பு வழங்கிய உச்சநீதிமன்ற நீதிபதி யார்?",
            "options": [
                ("Justice K.M. Joseph", "நீதிபதி கே.எம். ஜோசப்"),
                ("Justice R.F. Nariman", "நீதிபதி ஆர்.எஃப். நாரிமன்"),
                ("Justice B.R. Gavai", "நீதிபதி பி.ஆர். கவாய்"),
                ("Justice D.Y. Chandrachud", "நீதிபதி டி.ஒய். சந்திரசூட்")
            ],
            "correct_key": "A",
            "exp_en": "Justice K.M. Joseph wrote a dissenting opinion on the issue of severability, holding that Parliament enacted Part IX-B as a single composite code and it could not be severed, thus Part IX-B should be declared unconstitutional as a whole.",
            "exp_ta": "நீதிபதி கே.எம். ஜோசப் பகுதி IX-B பிரிக்க முடியாத ஒரு முழுமையான கட்டமைப்பு என்றும், எனவே அது முழுமையாக ரத்து செய்யப்பட வேண்டும் என்றும் மாறுபட்ட தீர்ப்பை எழுதினார்.",
            "why_a_en": "Correct. Justice K.M. Joseph delivered the dissenting opinion.",
            "why_a_ta": "சரி. நீதிபதி கே.எம். ஜோசப் மாறுபட்ட தீர்ப்பை வழங்கினார்.",
            "why_b_en": "Incorrect. Justice R.F. Nariman authored the majority opinion upholding severability.",
            "why_b_ta": "தவறு. நீதிபதி நாரிமன் பிரித்தெடுக்கும் கோட்பாட்டை ஆதரித்து பெரும்பான்மைத் தீர்ப்பு எழுதினார்.",
            "why_c_en": "Incorrect. Justice B.R. Gavai concurred with Justice Nariman in the majority.",
            "why_c_ta": "தவறு. நீதிபதி கவாய் நீதிபதி நாரிமனுடன் இணைந்து தீர்ப்பளித்தார்.",
            "why_d_en": "Incorrect. Justice Chandrachud was not on the bench.",
            "why_d_ta": "தவறு. நீதிபதி சந்திரசூட் இந்த அமர்வில் இல்லை.",
            "tip_en": "2021 Bench Split: Nariman + Gavai (Majority: Severable) vs K.M. Joseph (Dissent: Inseparable).",
            "tip_ta": "2021 அமர்வு தீர்ப்பு: நாரிமன் + கவாய் (பெரும்பான்மை: பிரிக்கலாம்) vs கே.எம். ஜோசப் (மாறுபட்ட கருத்து: பிரிக்க முடியாது).",
            "fact_en": "All three judges unanimously agreed that Part IX-B for State cooperatives violated Article 368(2) proviso.",
            "fact_ta": "மாநிலக் கூட்டுறவுகளுக்கு பகுதி IX-B உறுப்பு 368(2)-ஐ மீறுகிறது என்பதில் மூன்று நீதிபதிகளும் ஒருமனதாக உடன்பட்டனர்."
        },

        # GT 9
        {
            "subtopic": "First Provincial Act - Bombay 1925",
            "stem_en": "The Bombay Co-operative Societies Act of 1925 was historic primarily because:",
            "stem_ta": "1925-ஆம் ஆண்டின் பம்பாய் கூட்டுறவு சங்கங்கள் சட்டம் வரலாற்று முக்கியத்துவம் வாய்ந்ததாகக் கருதப்படுவதற்கு முதன்மைக் காரணம் என்ன?",
            "options": [
                ("It was the first provincial cooperative law passed in British India after co-operation became a provincial subject", "கூட்டுறவு மாகாணத் துறையான பிறகு பிரிட்டிஷ் இந்தியாவில் இயற்றப்பட்ட முதல் மாகாண கூட்டுறவுச் சட்டம் அதுவாகும்"),
                ("It abolished all rural money-lending across India", "அது இந்தியா முழுவதும் உள்ள அனைத்து கிராமப்புற கந்துவட்டி முறையையும் ஒழித்தது"),
                ("It nationalized all cooperative banks in western India", "அது மேற்கு இந்தியாவில் உள்ள அனைத்து கூட்டுறவு வங்கிகளையும் தேசியமயமாக்கியது"),
                ("It introduced constitutional status for local self-government", "அது உள்ளாட்சி அமைப்புகளுக்கு அரசியலமைப்பு அந்தஸ்தை அறிமுகப்படுத்தியது")
            ],
            "correct_key": "A",
            "exp_en": "Following the Government of India Act 1919 (Montagu-Chelmsford Reforms) which made cooperation a provincial transferred subject, Bombay became the first province to enact its own specialized Cooperative Societies Act in 1925.",
            "exp_ta": "1919 சட்டம் கூட்டுறவை மாகாண மாற்றப்பட்ட துறையாக்கியதைத் தொடர்ந்து, 1925-ல் பம்பாய் மாகாணம் தனது சொந்த சிறப்புச் சட்டத்தை இயற்றி முதல் மாகாணமாகத் திகழ்ந்தது.",
            "why_a_en": "Correct. Bombay Act 1925 was the pioneer provincial legislation.",
            "why_a_ta": "சரி. 1925 பம்பாய் சட்டமே முதல் மாகாண கூட்டுறவுச் சட்டமாகும்.",
            "why_b_en": "Incorrect. It did not abolish money-lending nationwide.",
            "why_b_ta": "தவறு. நாடு முழுவதும் கந்துவட்டியை ஒழிக்கவில்லை.",
            "why_c_en": "Incorrect. Nationalization occurred in commercial banking in 1969.",
            "why_c_ta": "தவறு. வங்கிகள் தேசியமயமாக்கல் 1969-ல் நடந்தது.",
            "why_d_en": "Incorrect. Constitutional status came with 73rd/74th amendments in 1992.",
            "why_d_ta": "தவறு. அரசியலமைப்பு அந்தஸ்து 1992-ல் வந்தது.",
            "tip_en": "1919 = Co-operation becomes provincial; 1925 = Bombay passes first provincial Act.",
            "tip_ta": "1919 = மாகாணத் துறையானது; 1925 = பம்பாய் முதல் மாகாண சட்டத்தை இயற்றியது.",
            "fact_en": "Madras Province followed in 1932, and Bengal in 1940.",
            "fact_ta": "இதைத் தொடர்ந்து மெட்ராஸ் 1932-லும், வங்காளம் 1940-லும் சொந்த சட்டங்களை இயற்றின."
        },

        # GT 10
        {
            "subtopic": "Madras Cooperative Land Mortgage Bank",
            "stem_en": "In which year was the Madras Co-operative Central Land Mortgage Bank established to finance primary land mortgage banks in the Madras Presidency?",
            "stem_ta": "மெட்ராஸ் மாகாணத்தில் தொடக்க நில அடமான வங்கிகளுக்கு நிதியளிக்க மெட்ராஸ் கூட்டுறவு மத்திய நில அடமான வங்கி எந்த ஆண்டு நிறுவப்பட்டது?",
            "options": [
                ("1929", "1929"),
                ("1904", "1904"),
                ("1947", "1947"),
                ("1965", "1965")
            ],
            "correct_key": "A",
            "exp_en": "The Madras Co-operative Central Land Mortgage Bank was established in 1929 to centralize the issue of debentures and coordinate long-term mortgage lending to farmers across the Presidency.",
            "exp_ta": "கடன் பத்திரங்களை வெளியிட்டு விவசாயிகளுக்கு நீண்ட கால வீட்டுக் கடன் வழங்க 1929-ல் மெட்ராஸ் கூட்டுறவு மத்திய நில அடமான வங்கி நிறுவப்பட்டது.",
            "why_a_en": "Correct. Established in 1929 based on Townsend recommendations.",
            "why_a_ta": "சரி. டவுன்சென்ட் குழு பரிந்துரைப்படி 1929-ல் நிறுவப்பட்டது.",
            "why_b_en": "Incorrect. 1904 was the Credit Societies Act.",
            "why_b_ta": "தவறு. 1904 முதல் கடன் சட்டம்.",
            "why_c_en": "Incorrect. 1947 is Independence.",
            "why_c_ta": "தவறு. 1947 சுதந்திர ஆண்டு.",
            "why_d_en": "Incorrect. 1965 is NDDB / Mirdha Committee.",
            "why_d_ta": "தவறு. 1965 தவறான ஆண்டு.",
            "tip_en": "Madras Land Mortgage Bank = 1929 (Apex for long-term agricultural investment credit).",
            "tip_ta": "மெட்ராஸ் நில அடமான வங்கி = 1929 (நீண்ட கால விவசாயக் கடனுக்கான உச்ச அமைப்பு).",
            "fact_en": "The bank floated debentures guaranteed by the Government of Madras.",
            "fact_ta": "மெட்ராஸ் அரசின் உத்தரவாதத்துடன் இவ்வங்கி கடன் பத்திரங்களை வெளியிட்டது."
        },

        # GT 11
        {
            "subtopic": "Cooperative Principles - ICA Manchester",
            "stem_en": "Which of the following is NOT one of the 7 cooperative principles formulated in the 1995 ICA Statement on Cooperative Identity?",
            "stem_ta": "1995-ஆம் ஆண்டின் ICA கூட்டுறவு அடையாள அறிக்கையில் வகுக்கப்பட்ட 7 கூட்டுறவுக் கோட்பாடுகளில் சேராதது எது?",
            "options": [
                ("Maximization of Capital Gain for Equity Holders", "பங்குதாரர்களுக்கு மூலதன ஆதாயத்தை அதிகப்படுத்துதல்"),
                ("Voluntary and Open Membership", "தன்னார்வ மற்றும் வெளிப்படையான உறுப்பினர் சேர்க்கை"),
                ("Democratic Member Control", "உறுப்பினர்களின் ஜனநாயகக் கட்டுப்பாடு"),
                ("Cooperation among Cooperatives", "கூட்டுறவுகளுக்கு இடையேயான கூட்டுறவு")
            ],
            "correct_key": "A",
            "exp_en": "Maximization of capital gains is a capitalist corporate objective, directly contrary to cooperative principles. The 7 ICA principles emphasize member democracy, service, education, cooperation among cooperatives, and community concern.",
            "exp_ta": "மூலதன ஆதாயத்தை அதிகப்படுத்துவது கார்ப்பரேட் நிறுவனங்களின் நோக்கம், கூட்டுறவுக் கோட்பாடு அல்ல. சேவை மற்றும் சமூக நலனே கூட்டுறவின் கோட்பாடுகள்.",
            "why_a_en": "Correct. Capital gain maximization is NOT a cooperative principle.",
            "why_a_ta": "சரி. மூலதன ஆதாயத்தை அதிகப்படுத்துவது கூட்டுறவுக் கோட்பாடு அல்ல.",
            "why_b_en": "Incorrect. Principle 1 is Voluntary and Open Membership.",
            "why_b_ta": "தவறு. கோட்பாடு 1 தன்னார்வ சேர்க்கை.",
            "why_c_en": "Incorrect. Principle 2 is Democratic Member Control.",
            "why_c_ta": "தவறு. கோட்பாடு 2 ஜனநாயகக் கட்டுப்பாடு.",
            "why_d_en": "Incorrect. Principle 6 is Cooperation among Cooperatives.",
            "why_d_ta": "தவறு. கோட்பாடு 6 கூட்டுறவுகளுக்கு இடையே கூட்டுறவு.",
            "tip_en": "Cooperative values: Self-help, self-responsibility, democracy, equality, equity, solidarity.",
            "tip_ta": "கூட்டுறவு விழுமியங்கள்: சுய உதவி, பொறுப்புடைமை, ஜனநாயகம், சமத்துவம், ஒற்றுமை.",
            "fact_en": "ICA principles were reviewed and adopted in Manchester at the ICA Centennial Congress in 1995.",
            "fact_ta": "1995-ல் மான்செஸ்டரில் நடைபெற்ற நூற்றாண்டு மாநாட்டில் இக்கோட்பாடுகள் ஏற்கப்பட்டன."
        },

        # GT 12
        {
            "subtopic": "Tamil Nadu Cooperative Election Commission Section",
            "stem_en": "Under which specific Section of the Tamil Nadu Co-operative Societies Act, 1983 was the Tamil Nadu State Co-operative Societies Election Commission constituted?",
            "stem_ta": "தமிழ்நாடு கூட்டுறவு சங்கங்கள் சட்டம் 1983-ன் எந்த குறிப்பிட்ட பிரிவின் கீழ் தமிழ்நாடு மாநிலக் கூட்டுறவு சங்கங்களின் தேர்தல் ஆணையம் அமைக்கப்பட்டது?",
            "options": [
                ("Section 33-A", "பிரிவு 33-A"),
                ("Section 81", "பிரிவு 81"),
                ("Section 88", "பிரிவு 88"),
                ("Section 90", "பிரிவு 90")
            ],
            "correct_key": "A",
            "exp_en": "Section 33-A was inserted into the Tamil Nadu Co-operative Societies Act, 1983 (by Tamil Nadu Act 4 of 2013) to establish the independent Tamil Nadu State Co-operative Societies Election Commission.",
            "exp_ta": "2013-ல் சேர்க்கப்பட்ட பிரிவு 33-A-ன் கீழ் தமிழ்நாடு மாநிலக் கூட்டுறவு சங்கங்களின் தேர்தல் ஆணையம் (TNSCSEC) அமைக்கப்பட்டது.",
            "why_a_en": "Correct. Section 33-A governs the Election Commission in TN.",
            "why_a_ta": "சரி. பிரிவு 33-A தமிழக கூட்டுறவு தேர்தல் ஆணையத்தை நிறுவுகிறது.",
            "why_b_en": "Incorrect. Section 81 governs statutory inquiries.",
            "why_b_ta": "தவறு. பிரிவு 81 விசாரணை பற்றியது.",
            "why_c_en": "Incorrect. Section 88 governs supersession.",
            "why_c_ta": "தவறு. பிரிவு 88 வாரியக் கலைப்பு பற்றியது.",
            "why_d_en": "Incorrect. Section 90 governs dispute arbitration.",
            "why_d_ta": "தவறு. பிரிவு 90 நடுவர் தீர்ப்பு பற்றியது.",
            "tip_en": "TN Election Section = 33-A (Inserted after 97th CAA 2011).",
            "tip_ta": "தமிழக தேர்தல் பிரிவு = 33-A (97வது திருத்தத்திற்குப் பின் சேர்க்கப்பட்டது).",
            "fact_en": "The Commissioner is appointed by the Governor on the recommendation of the State Government.",
            "fact_ta": "மாநில அரசின் பரிந்துரையின் பேரில் ஆளுநரால் தேர்தல் ஆணையர் நியமிக்கப்படுகிறார்."
        },

        # GT 13
        {
            "subtopic": "Vaidyanathan Committee Package",
            "stem_en": "What was the total financial outlay of the revival package recommended by the Prof. A. Vaidyanathan Committee (2004) for the Short-Term Rural Co-operative Credit Structure?",
            "stem_ta": "குறுகிய கால கிராமப்புற கூட்டுறவு கடன் கட்டமைப்புக்காக பேராசிரியர் ஏ. வைத்தியநாதன் குழு (2004) பரிந்துரைத்த மறுமலர்ச்சி நிதித் தொகுப்பின் மொத்த நிதி ஒதுக்கீடு என்ன?",
            "options": [
                ("Approximately ₹13,596 crore", "சுமார் ₹13,596 கோடி"),
                ("Approximately ₹5,000 crore", "சுமார் ₹5,000 கோடி"),
                ("Approximately ₹25,000 crore", "சுமார் ₹25,000 கோடி"),
                ("Approximately ₹50,000 crore", "சுமார் ₹50,000 கோடி")
            ],
            "correct_key": "A",
            "exp_en": "The Vaidyanathan Task Force recommended a ₹13,596 crore financial package funded by the Central Government, State Governments, and cooperative credit institutions in the ratio of 68:28:4.",
            "exp_ta": "வைத்தியநாதன் பணிக்குழு மத்திய அரசு, மாநில அரசு மற்றும் கூட்டுறவு அமைப்புகளின் 68:28:4 நிதிப் பங்களிப்புடன் ₹13,596 கோடி மறுமலர்ச்சி தொகுப்பைப் பரிந்துரைத்தது.",
            "why_a_en": "Correct. ₹13,596 crore was the recommended revival package.",
            "why_a_ta": "சரி. ₹13,596 கோடி பரிந்துரைக்கப்பட்ட மறுமலர்ச்சி நிதியாகும்.",
            "why_b_en": "Incorrect. Far lower than the recommended sum.",
            "why_b_ta": "தவறு. பரிந்துரைக்கப்பட்டதை விட மிகவும் குறைவு.",
            "why_c_en": "Incorrect. Incorrect estimate.",
            "why_c_ta": "தவறு. தவறான மதிப்பீடு.",
            "why_d_en": "Incorrect. Overstated amount.",
            "why_d_ta": "தவறு. மிகைப்படுத்தப்பட்ட தொகை.",
            "tip_en": "Vaidyanathan Package: ₹13,596 crore; Sharing ratio: Centre 68%, State 28%, Cooperatives 4%.",
            "tip_ta": "வைத்தியநாதன் நிதித் தொகுப்பு: ₹13,596 கோடி; பங்களிப்பு விகிதம்: மத்திய அரசு 68%, மாநில அரசு 28%, கூட்டுறவு 4%.",
            "fact_en": "The package was implemented through NABARD as the nodal agency.",
            "fact_ta": "நபார்டு வங்கி ஒருங்கிணைப்பு முகமையாக செயல்பட்டு இத்திட்டத்தை நிறைவேற்றியது."
        },

        # GT 14
        {
            "subtopic": "Model Bye-laws for PACS Activities",
            "stem_en": "Under the new Model Bye-laws for PACS unveiled by the Ministry of Cooperation, PACS are permitted to engage in approximately how many diverse business activities?",
            "stem_ta": "கூட்டுறவு அமைச்சகம் வெளியிட்ட PACS-க்கான புதிய மாதிரி துணை விதிகளின்படி, தொடக்க வேளாண் கடன் சங்கங்கள் சுமார் எத்தனை வகையான வணிக நடவடிக்கைகளில் ஈடுபட அனுமதிக்கப்பட்டுள்ளன?",
            "options": [
                ("More than 25 diverse business activities", "25-க்கும் மேற்பட்ட பல்வேறு வணிக நடவடிக்கைகள்"),
                ("Only 2 activities (credit and fertilizer)", "2 நடவடிக்கைகள் மட்டுமே (கடன் மற்றும் உரம்)"),
                ("Exactly 5 agricultural activities", "சரியாக 5 விவசாய நடவடிக்கைகள்"),
                ("Only banking activities permitted by RBI", "ரிசர்வ் வங்கி அனுமதித்த வங்கி நடவடிக்கைகள் மட்டுமே")
            ],
            "correct_key": "A",
            "exp_en": "The new Model Bye-laws enable PACS to diversify into over 25 economic activities including Common Service Centres (CSCs), fair price shops, dairy, fishery, custom hiring centres, LPG/petrol distribution, and cold storage.",
            "exp_ta": "புதிய மாதிரி துணை விதிகள் PACS சங்கங்களை பொது சேவை மையங்கள், நியாயவிலைக் கடைகள், பால்வளம், மீன்வளம், சேமிப்புக் கிடங்குகள் உட்பட 25-க்கும் மேற்பட்ட வணிகங்களை நடத்த அனுமதிக்கின்றன.",
            "why_a_en": "Correct. Over 25 diverse economic activities are permitted.",
            "why_a_ta": "சரி. 25-க்கும் மேற்பட்ட வணிக நடவடிக்கைகளுக்கு அனுமதி அளிக்கப்பட்டுள்ளது.",
            "why_b_en": "Incorrect. The old restriction to credit only has been removed.",
            "why_b_ta": "தவறு. கடன் மட்டும் வழங்கும் பழைய முறை நீக்கப்பட்டுவிட்டது.",
            "why_c_en": "Incorrect. Much broader than 5 activities.",
            "why_c_ta": "தவறு. 5-ஐ விட அதிகமான துறைகள்.",
            "why_d_en": "Incorrect. PACS are credit societies, not commercial banks.",
            "why_d_ta": "தவறு. PACS வணிக வங்கிகள் அல்ல.",
            "tip_en": "PACS Transformation: Single-purpose credit agency → Multi-Purpose Village Service Centre (>25 activities).",
            "tip_ta": "PACS மாற்றம்: கடன் சங்கம் மட்டும் அல்லாமல் 25-க்கும் மேற்பட்ட சேவைகளை வழங்கும் பல்நோக்கு கிராம மையம்.",
            "fact_en": "All States and UTs have adopted or agreed to adopt the Model Bye-laws.",
            "fact_ta": "அனைத்து மாநிலங்களும் இந்த மாதிரி துணை விதிகளை ஏற்றுக்கொண்டுள்ளன."
        },

        # GT 15
        {
            "subtopic": "National Cooperative Database Coverage",
            "stem_en": "The National Cooperative Database launched by the Ministry of Cooperation maps data for approximately how many cooperative societies in India?",
            "stem_ta": "கூட்டுறவு அமைச்சகத்தால் தொடங்கப்பட்ட தேசிய கூட்டுறவு தரவுத்தளம் இந்தியாவில் உள்ள சுமார் எத்தனை கூட்டுறவு சங்கங்களின் தரவுகளை வரைபடமாக்கியுள்ளது?",
            "options": [
                ("Over 8 lakh cooperative societies", "8 லட்சத்திற்கும் மேற்பட்ட கூட்டுறவு சங்கங்கள்"),
                ("About 1 lakh cooperative societies only", "சுமார் 1 லட்சம் கூட்டுறவு சங்கங்கள் மட்டுமே"),
                ("About 50,000 cooperative societies", "சுமார் 50,000 கூட்டுறவு சங்கங்கள்"),
                ("Over 25 lakh societies", "25 லட்சத்திற்கும் மேற்பட்ட சங்கங்கள்")
            ],
            "correct_key": "A",
            "exp_en": "The National Cooperative Database developed by the Ministry of Cooperation covers data of over 8 lakh cooperative societies across all tiers (Primary, District, State) spanning various sectors in India.",
            "exp_ta": "மத்திய கூட்டுறவு அமைச்சகம் உருவாக்கிய தேசிய கூட்டுறவு தரவுத்தளம் இந்தியாவில் உள்ள 8 லட்சத்திற்கும் மேற்பட்ட கூட்டுறவு சங்கங்களின் தரவுகளைக் கொண்டுள்ளது.",
            "why_a_en": "Correct. Over 8 lakh cooperative societies are indexed in the database.",
            "why_a_ta": "சரி. 8 லட்சத்திற்கும் மேற்பட்ட கூட்டுறவு சங்கங்கள் இதில் பதிவு செய்யப்பட்டுள்ளன.",
            "why_b_en": "Incorrect. 1 lakh is roughly the number of PACS only.",
            "why_b_ta": "தவறு. 1 லட்சம் என்பது தொடக்க வேளாண் கடன் சங்கங்களின் எண்ணிக்கை மட்டுமே.",
            "why_c_en": "Incorrect. Far too low.",
            "why_c_ta": "தவறு. மிகவும் குறைவான எண்ணிக்கை.",
            "why_d_en": "Incorrect. Total cooperatives in India is ~8.5 lakh, not 25 lakh.",
            "why_d_ta": "தவறு. இந்தியாவில் உள்ள மொத்த சங்கங்கள் சுமார் 8.5 லட்சம்.",
            "tip_en": "Cooperative Census: India has ~8.5 lakh cooperatives with ~30 crore members.",
            "tip_ta": "கூட்டுறவு புள்ளிவிவரம்: இந்தியாவில் சுமார் 8.5 லட்சம் சங்கங்களும் 30 கோடி உறுப்பினர்களும் உள்ளனர்.",
            "fact_en": "The database was launched in New Delhi in March 2024.",
            "fact_ta": "இத்தரவுத்தளம் 2024 மார்ச்சில் புது தில்லியில் தொடங்கி வைக்கப்பட்டது."
        },

        # GT 16
        {
            "subtopic": "Vaikunth Mehta Cooperative Leader",
            "stem_en": "In which Indian state did Vaikunth Lallubhai Mehta serve as Finance and Cooperation Minister between 1946 and 1952?",
            "stem_ta": "1946 முதல் 1952 வரை வைகுந்த் லல்லுபாய் மேத்தா எந்த இந்திய மாநிலத்தில் நிதி மற்றும் கூட்டுறவு அமைச்சராகப் பணியாற்றினார்?",
            "options": [
                ("Bombay State", "பம்பாய் மாநிலம்"),
                ("Madras State", "மெட்ராஸ் மாநிலம்"),
                ("Uttar Pradesh", "உத்தரப் பிரதேசம்"),
                ("West Bengal", "மேற்கு வங்காளம்")
            ],
            "correct_key": "A",
            "exp_en": "Vaikunth Lallubhai Mehta served as the Minister of Finance and Cooperation in Bombay State under Premier B.G. Kher from 1946 to 1952.",
            "exp_ta": "வைகுந்த் லல்லுபாய் மேத்தா 1946 முதல் 1952 வரை பி.ஜி. கெர் தலைமையிலான பம்பாய் மாநிலத்தில் நிதி மற்றும் கூட்டுறவு அமைச்சராகப் பணியாற்றினார்.",
            "why_a_en": "Correct. Bombay State was the venue of his ministerial career.",
            "why_a_ta": "சரி. பம்பாய் மாநிலத்தின் அமைச்சராகவே இவர் பணியாற்றினார்.",
            "why_b_en": "Incorrect. Not Madras State.",
            "why_b_ta": "தவறு. மெட்ராஸ் மாநிலம் அல்ல.",
            "why_c_en": "Incorrect. Not Uttar Pradesh.",
            "why_c_ta": "தவறு. உத்தரப் பிரதேசம் அல்ல.",
            "why_d_en": "Incorrect. Not West Bengal.",
            "why_d_ta": "தவறு. மேற்கு வங்காளம் அல்ல.",
            "tip_en": "Vaikunth Mehta: Bombay Finance Minister (1946-52) → KVIC Chairman (1957) → VAMNICOM named after him.",
            "tip_ta": "வைகுந்த் மேத்தா: பம்பாய் நிதி அமைச்சர் (1946-52) → KVIC தலைவர் (1957) → VAMNICOM புனே.",
            "fact_en": "Mehta was also the managing director of the Bombay Central Co-operative Bank for over 30 years.",
            "fact_ta": "மேத்தா பம்பாய் மத்திய கூட்டுறவு வங்கியின் நிர்வாக இயக்குநராக 30 ஆண்டுகளுக்கும் மேலாகப் பணியாற்றினார்."
        },

        # GT 17
        {
            "subtopic": "TRIFED Mandate",
            "stem_en": "The Tribal Cooperative Marketing Development Federation of India (TRIFED) was set up in 1987 under which administrative Ministry?",
            "stem_ta": "இந்திய பழங்குடியினர் கூட்டுறவு சந்தைப்படுத்தல் மேம்பாட்டு கூட்டமைப்பு (TRIFED) 1987-ல் எந்த மத்திய அமைச்சகத்தின் கீழ் தொடங்கப்பட்டது?",
            "options": [
                ("Ministry of Tribal Affairs", "பழங்குடியினர் விவகாரங்கள் அமைச்சகம்"),
                ("Ministry of Cooperation", "கூட்டுறவு அமைச்சகம்"),
                ("Ministry of Agriculture and Farmers Welfare", "வேளாண்மை மற்றும் விவசாயிகள் நல அமைச்சகம்"),
                ("Ministry of Commerce and Industry", "வர்த்தகம் மற்றும் தொழில் அமைச்சகம்")
            ],
            "correct_key": "A",
            "exp_en": "TRIFED was established in August 1987 under the Multi-State Co-operative Societies Act, 1984, and functions under the administrative control of the Ministry of Tribal Affairs to market minor forest produce.",
            "exp_ta": "டிரைஃபெட் (TRIFED) 1987 ஆகஸ்டில் தொடங்கப்பட்டு, பழங்குடியினரின் வன விளைபொருட்களைச் சந்தைப்படுத்த பழங்குடியினர் விவகாரங்கள் அமைச்சகத்தின் கீழ் செயல்படுகிறது.",
            "why_a_en": "Correct. Ministry of Tribal Affairs administers TRIFED.",
            "why_a_ta": "சரி. பழங்குடியினர் விவகார அமைச்சகம் TRIFED அமைப்பை நிர்வகிக்கிறது.",
            "why_b_en": "Incorrect. Ministry of Cooperation is not its administrative ministry.",
            "why_b_ta": "தவறு. கூட்டுறவு அமைச்சகம் இதன் நேரடி அமைச்சகம் அல்ல.",
            "why_c_en": "Incorrect. Not Agriculture Ministry.",
            "why_c_ta": "தவறு. வேளாண் அமைச்சகம் அல்ல.",
            "why_d_en": "Incorrect. Not Commerce Ministry.",
            "why_d_ta": "தவறு. வர்த்தக அமைச்சகம் அல்ல.",
            "tip_en": "TRIFED = Tribal Affairs Ministry; Brand = 'Tribes India'; Scheme = 'Van Dhan Vikas Kendra'.",
            "tip_ta": "டிரைஃபெட் = பழங்குடியினர் அமைச்சகம்; பிராண்ட் = 'ட்ரைப்ஸ் இந்தியா'; திட்டம் = 'வன் தன் விகாஸ் கேந்திரா'.",
            "fact_en": "TRIFED operates the 'Van Dhan Yojana' to ensure fair value for Non-Timber Forest Produce.",
            "fact_ta": "மரம் அல்லாத வன விளைபொருட்களுக்கு நியாயமான விலை கிடைக்க 'வன் தன் யோஜனா' திட்டத்தை டிரைஃபெட் நடத்துகிறது."
        },

        # GT 18
        {
            "subtopic": "Petrofils Cooperative Limited",
            "stem_en": "Which unique joint sector cooperative enterprise was established in Gujarat in 1974 to manufacture polyester filament yarn for handloom and powerloom weavers?",
            "stem_ta": "கைத்தறி மற்றும் விசைத்தறி நெசவாளர்களுக்காக பாலியஸ்டர் நூல் உற்பத்தி செய்ய 1974-ல் குஜராத்தில் தொடங்கப்பட்ட தனித்துவமான கூட்டுறவு நிறுவனம் எது?",
            "options": [
                ("Petrofils Cooperative Limited", "பெட்ரோஃபில்ஸ் கூட்டுறவு நிறுவனம் (Petrofils)"),
                ("KRIBHCO", "கிரிப்கோ (KRIBHCO)"),
                ("IFFCO", "இஃப்கோ (IFFCO)"),
                ("NAFED", "நாஃபெட் (NAFED)")
            ],
            "correct_key": "A",
            "exp_en": "Petrofils Cooperative Limited was established in 1974 as a joint venture between the Government of India and weaver cooperative societies in Vadodara, Gujarat, to supply synthetic yarn directly to weavers.",
            "exp_ta": "நெசவாளர்களுக்கு செயற்கை நூல் வழங்க 1974-ல் இந்திய அரசு மற்றும் நெசவாளர் கூட்டுறவு சங்கங்களின் கூட்டு முயற்சியாக குஜராத்தின் வடோராவில் பெட்ரோஃபில்ஸ் கூட்டுறவு தொடங்கப்பட்டது.",
            "why_a_en": "Correct. Petrofils produced polyester filament yarn.",
            "why_a_ta": "சரி. பெட்ரோஃபில்ஸ் பாலியஸ்டர் நூல் உற்பத்திக்காகத் தொடங்கப்பட்டது.",
            "why_b_en": "Incorrect. KRIBHCO produces chemical fertilizer.",
            "why_b_ta": "தவறு. கிரிப்கோ உர உற்பத்தியாளர்.",
            "why_c_en": "Incorrect. IFFCO is a fertilizer cooperative.",
            "why_c_ta": "தவறு. இஃப்கோ உரக் கூட்டுறவு.",
            "why_d_en": "Incorrect. NAFED markets agricultural produce.",
            "why_d_ta": "தவறு. NAFED விவசாய விளைபொருள் சந்தைப்படுத்துதல்.",
            "tip_en": "Petrofils = Cooperative synthetic yarn manufacturer (Vadodara, Gujarat).",
            "tip_ta": "பெட்ரோஃபில்ஸ் = கூட்டுறவு செயற்கை நூல் தயாரிப்பு நிறுவனம் (குஜராத்).",
            "fact_en": "It was one of the pioneer industrial petrochemical cooperatives in India.",
            "fact_ta": "இந்தியாவின் முன்னோடி பெட்ரோகெமிக்கல் கூட்டுறவு அமைப்புகளில் இது ஒன்றாகும்."
        },

        # GT 19
        {
            "subtopic": "Filing of Returns - Article 243ZP",
            "stem_en": "Under Article 243ZP of the Constitution, which of the following is NOT a mandatory item to be filed by a cooperative society in its annual returns?",
            "stem_ta": "அரசியலமைப்பு உறுப்பு 243ZP-ன் கீழ், ஒரு கூட்டுறவு சங்கம் தனது வருடாந்திர அறிக்கையில் சமர்ப்பிக்க வேண்டிய கட்டாய ஆவணங்களில் சேராதது எது?",
            "options": [
                ("Confidential income tax assessment orders of individual members", "தனிநபர் உறுப்பினர்களின் ரகசிய வருமான வரி மதிப்பீட்டு உத்தரவுகள்"),
                ("Annual report of its activities", "சங்கத்தின் செயல்பாடுகள் குறித்த வருடாந்திர அறிக்கை"),
                ("Audited statement of accounts", "தணிக்கை செய்யப்பட்ட கணக்கு அறிக்கை"),
                ("Plan for disposal of surplus as approved by general body", "பொதுக்குழுவால் அங்கீகரிக்கப்பட்ட உபரியை பகிர்ந்தளிக்கும் திட்டம்")
            ],
            "correct_key": "A",
            "exp_en": "Article 243ZP specifies filing of annual reports, audited accounts, plan for surplus disposal, list of amendments, declaration of elections, etc. Individual members' confidential tax orders are private and not part of statutory returns.",
            "exp_ta": "உறுப்பு 243ZP செயல்பாட்டு அறிக்கை, தணிக்கை அறிக்கை, உபரி பகிர்வு திட்டம், துணை விதி திருத்தங்கள் ஆகியவற்றை மட்டுமே கேட்கிறது. தனிநபர் உறுப்பினர்களின் ரகசிய வரி உத்தரவுகள் இதில் சேராது.",
            "why_a_en": "Correct. Individual tax orders are NOT part of Article 243ZP returns.",
            "why_a_ta": "சரி. தனிநபர் வரி உத்தரவுகள் உறுப்பு 243ZP அறிக்கையில் வராது.",
            "why_b_en": "Incorrect. Annual report is explicitly mandated under 243ZP(a).",
            "why_b_ta": "தவறு. வருடாந்திர அறிக்கை கட்டாயம் சமர்ப்பிக்கப்பட வேண்டும்.",
            "why_c_en": "Incorrect. Audited accounts are explicitly mandated under 243ZP(b).",
            "why_c_ta": "தவறு. தணிக்கை அறிக்கை கட்டாயமானது.",
            "why_d_en": "Incorrect. Surplus disposal plan is explicitly mandated under 243ZP(c).",
            "why_d_ta": "தவறு. உபரி பகிர்வு திட்டம் கட்டாயமானது.",
            "tip_en": "Article 243ZP Checklist: Activity Report + Audited Statement + Surplus Plan + Bye-law amendments + Election declaration.",
            "tip_ta": "உறுப்பு 243ZP பட்டியல்: செயல்பாட்டு அறிக்கை + தணிக்கை அறிக்கை + உபரி திட்டம் + திருத்தங்கள் + தேர்தல் அறிக்கை.",
            "fact_en": "Returns must be filed within 6 months of the close of every financial year.",
            "fact_ta": "ஒவ்வொரு நிதியாண்டும் முடிந்த 6 மாதங்களுக்குள் இவ்வறிக்கைகள் தாக்கல் செய்யப்பட வேண்டும்."
        },

        # GT 20
        {
            "subtopic": "First Land Mortgage Bank",
            "stem_en": "In which city or town was India's very first Primary Land Mortgage Bank established in 1920?",
            "stem_ta": "1920-ஆம் ஆண்டு இந்தியாவின் மிக முதல் தொடக்க நில அடமான வங்கி எந்த நகரில் தொடங்கப்பட்டது?",
            "options": [
                ("Jhang (Punjab)", "ஜாங் (பஞ்சாப்)"),
                ("Anand (Gujarat)", "ஆனந்த் (குஜராத்)"),
                ("Triplicane (Madras)", "திருவல்லிக்கேணி (மெட்ராஸ்)"),
                ("Pune (Maharashtra)", "புனே (மகாராஷ்டிரா)")
            ],
            "correct_key": "A",
            "exp_en": "The first cooperative land mortgage bank in India was organized at Jhang in the Punjab Province in 1920 to relieve agriculturists from debt bondage through long-term mortgage loans.",
            "exp_ta": "விவசாயிகளை கடன் சுமையிலிருந்து மீட்க 1920-ல் பஞ்சாப் மாகாணத்தின் ஜாங் நகரில் இந்தியாவின் முதல் நில அடமான வங்கி தொடங்கப்பட்டது.",
            "why_a_en": "Correct. Jhang, Punjab was the birthplace of land mortgage banking in India.",
            "why_a_ta": "சரி. பஞ்சாபின் ஜாங் நகரிலேயே முதல் நில அடமான வங்கி உருவானது.",
            "why_b_en": "Incorrect. Anand is famous for dairy cooperation (Amul).",
            "why_b_ta": "தவறு. ஆனந்த் பால்வளக் கூட்டுறவுக்குப் புகழ்பெற்றது.",
            "why_c_en": "Incorrect. Triplicane was the site of the first consumer cooperative (TUCS 1904).",
            "why_c_ta": "தவறு. திருவல்லிக்கேணி முதல் நுகர்வோர் கூட்டுறவு உருவான இடம்.",
            "why_d_en": "Incorrect. Pune is the seat of VAMNICOM.",
            "why_d_ta": "தவறு. புனே VAMNICOM உள்ள இடம்.",
            "tip_en": "Pioneering sites: Jhang (1920, Mortgage Bank); Triplicane (1904, Consumer Society); Anand (1946, Dairy); Pravaranagar (1950, Sugar).",
            "tip_ta": "முன்னோடி இடங்கள்: ஜாங் (1920, நில அடமானம்); திருவல்லிக்கேணி (1904, நுகர்வோர்); ஆனந்த் (1946, பால்); பிரவரநகர் (1950, சர்க்கரை).",
            "fact_en": "Jhang is now located in the Punjab province of present-day Pakistan.",
            "fact_ta": "ஜாங் நகரம் தற்போது பாகிஸ்தானில் உள்ள பஞ்சாப் மாகாணத்தில் அமைந்துள்ளது."
        },

        # GT 21
        {
            "subtopic": "Townsend Committee 1927",
            "stem_en": "The Committee on Co-operation in Madras (1927-28), which recommended the enactment of a separate provincial cooperative statute, was chaired by:",
            "stem_ta": "தனி மாகாண கூட்டுறவு சட்டம் இயற்றப் பரிந்துரைத்த மெட்ராஸ் கூட்டுறவு மீதான குழுவிற்கு (1927-28) தலைமை தாங்கியவர் யார்?",
            "options": [
                ("C.A.H. Townsend", "சி.ஏ.எச். டவுன்சென்ட்"),
                ("Sir Frederick Nicholson", "சர் பிரடெரிக் நிக்கல்சன்"),
                ("Edward Maclagan", "எட்வர்ட் மெக்லகன்"),
                ("A.D. Gorwala", "ஏ.டி. கோர்வாலா")
            ],
            "correct_key": "A",
            "exp_en": "The Townsend Committee (1927-28) reviewed the working of cooperatives in the Madras Presidency and recommended comprehensive legislation, leading to the Madras Co-operative Societies Act, 1932.",
            "exp_ta": "டவுன்சென்ட் குழு (1927-28) மெட்ராஸ் மாகாணக் கூட்டுறவுகளை ஆய்வு செய்து புதிய சட்டத்தைப் பரிந்துரைத்தது. இதுவே 1932 மெட்ராஸ் சட்டத்திற்கு வழிகோலியது.",
            "why_a_en": "Correct. Townsend headed the 1927 Madras committee.",
            "why_a_ta": "சரி. டவுன்சென்ட் 1927 மெட்ராஸ் குழுவிற்குத் தலைமை தாங்கினார்.",
            "why_b_en": "Incorrect. Nicholson reported in 1895.",
            "why_b_ta": "தவறு. நிக்கல்சன் 1895-ல் அறிக்கை அளித்தார்.",
            "why_c_en": "Incorrect. Maclagan headed the all-India committee in 1914.",
            "why_c_ta": "தவறு. மெக்லகன் 1914 அகில இந்தியக் குழுவிற்குத் தலைமை தாங்கினார்.",
            "why_d_en": "Incorrect. Gorwala headed the 1951-54 committee.",
            "why_d_ta": "தவறு. கோர்வாலா 1954 குழுவிற்குத் தலைமை தாங்கினார்.",
            "tip_en": "Townsend Committee (1927) → Madras Co-operative Societies Act, 1932.",
            "tip_ta": "டவுன்சென்ட் குழு (1927) → மெட்ராஸ் கூட்டுறவு சங்கங்கள் சட்டம் 1932.",
            "fact_en": "Townsend was a senior Indian Civil Service (ICS) officer.",
            "fact_ta": "டவுன்சென்ட் மூத்த ஐ.சி.எஸ் அதிகாரி ஆவார்."
        },

        # GT 22
        {
            "subtopic": "National Cooperative Exports Limited (NCEL)",
            "stem_en": "Under the Multi-State Co-operative Societies Act, 2002, the newly created National Cooperative Exports Limited (NCEL) has its registered office in which city?",
            "stem_ta": "பல மாநில கூட்டுறவு சங்கங்கள் சட்டம் 2002-ன் கீழ் புதிதாக உருவாக்கப்பட்ட தேசிய கூட்டுறவு ஏற்றுமதி நிறுவனத்தின் (NCEL) பதிவு அலுவலகம் எந்த நகரில் அமைந்துள்ளது?",
            "options": [
                ("New Delhi", "புது தில்லி"),
                ("Mumbai", "மும்பை"),
                ("Chennai", "சென்னை"),
                ("Ahmedabad", "அகமதாபாத்")
            ],
            "correct_key": "A",
            "exp_en": "National Cooperative Exports Limited (NCEL), established in 2023 under the MSCS Act 2002 with equity from AMUL, IFFCO, KRIBHCO, NAFED, and NCDC, is headquartered in New Delhi.",
            "exp_ta": "அமுல், இஃப்கோ, கிரிப்கோ, நாஃபெட் மற்றும் NCDC ஆகியவற்றின் கூட்டுப் பங்களிப்புடன் 2023-ல் அமைக்கப்பட்ட NCEL தலைமையகம் புது தில்லியில் உள்ளது.",
            "why_a_en": "Correct. NCEL is headquartered in New Delhi.",
            "why_a_ta": "சரி. NCEL தலைமையகம் புது தில்லியில் அமைந்துள்ளது.",
            "why_b_en": "Incorrect. Not Mumbai.",
            "why_b_ta": "தவறு. மும்பை அல்ல.",
            "why_c_en": "Incorrect. Not Chennai.",
            "why_c_ta": "தவறு. சென்னை அல்ல.",
            "why_d_en": "Incorrect. Not Ahmedabad.",
            "why_d_ta": "தவறு. அகமதாபாத் அல்ல.",
            "tip_en": "NCEL is the national export arm for all agricultural cooperatives across India.",
            "tip_ta": "இந்தியாவின் அனைத்து விவசாயக் கூட்டுறவுகளுக்குமான தேசிய ஏற்றுமதி நிறுவனம் NCEL ஆகும்.",
            "fact_en": "NCEL has been designated as the canalizing agency for government-to-government (G2G) export of non-basmati rice and sugar.",
            "fact_ta": "அரசுக்கு இடையேயான (G2G) அரிசி மற்றும் சர்க்கரை ஏற்றுமதிக்கான முகமையாக NCEL செயல்படுகிறது."
        },

        # GT 23
        {
            "subtopic": "Cooperative Banking Dual Control End",
            "stem_en": "Which cooperative bank fraud in 2019 led directly to the enactment of the Banking Regulation (Amendment) Act, 2020?",
            "stem_ta": "2019-ல் நடந்த எந்தக் கூட்டுறவு வங்கி நிதி மோசடி, 2020-ஆம் ஆண்டின் வங்கி ஒழுங்குமுறை (திருத்தச்) சட்டம் இயற்றப்பட நேரடிக் காரணமாக அமைந்தது?",
            "options": [
                ("Punjab and Maharashtra Co-operative (PMC) Bank", "பஞ்சாப் மற்றும் மகாராஷ்டிரா கூட்டுறவு (PMC) வங்கி"),
                ("Madhavpura Mercantile Co-operative Bank", "மாதவ்புரா மெர்கன்டைல் கூட்டுறவு வங்கி"),
                ("Bhadradri Co-operative Urban Bank", "பத்ராத்ரி கூட்டுறவு நகர்ப்புற வங்கி"),
                ("Cosmos Co-operative Bank", "காஸ்மோஸ் கூட்டுறவு வங்கி")
            ],
            "correct_key": "A",
            "exp_en": "The collapse of Punjab and Maharashtra Co-operative (PMC) Bank in September 2019 due to fraudulent concealment of loans to HDIL caused widespread panic and directly spurred Parliament to amend the BR Act in 2020.",
            "exp_ta": "செப்டம்பர் 2019-ல் பஞ்சாப் மற்றும் மகாராஷ்டிரா கூட்டுறவு (PMC) வங்கியில் நடந்த கடன் மோசடி நாடு முழுவதும் அதிர்ச்சியை ஏற்படுத்தி, 2020 வங்கித் திருத்தச் சட்டத்திற்கு வழிகோலியது.",
            "why_a_en": "Correct. PMC Bank scam was the direct trigger for the 2020 amendment.",
            "why_a_ta": "சரி. PMC வங்கி மோசடியே 2020 திருத்தத்திற்கு உடனடிக் காரணமாகும்.",
            "why_b_en": "Incorrect. Madhavpura scam occurred in 2001 (Ketan Parekh scam).",
            "why_b_ta": "தவறு. மாதவ்புரா மோசடி 2001-ல் நடந்தது.",
            "why_c_en": "Incorrect. Minor entity, not the cause of the central law.",
            "why_c_ta": "தவறு. சிறிய அமைப்பு.",
            "why_d_en": "Incorrect. Cosmos faced a cyber-attack in 2018, not loan fraud.",
            "why_d_ta": "தவறு. காஸ்மோஸ் வங்கி சைபர் தாக்குதலை எதிர்கொண்டது.",
            "tip_en": "Crisis to Reform: 2001 Madhavpura scam → Dual control reforms; 2019 PMC scam → 2020 BR Amendment Act.",
            "tip_ta": "மோசடியும் சீர்திருத்தமும்: 2001 மாதவ்புரா மோசடி → இரட்டை கட்டுப்பாடு ஆய்வு; 2019 PMC மோசடி → 2020 வங்கித் திருத்தச் சட்டம்.",
            "fact_en": "PMC Bank was subsequently amalgamated with Unity Small Finance Bank in 2022.",
            "fact_ta": "PMC வங்கி பின்னர் 2022-ல் யூனிட்டி ஸ்மால் பைனான்ஸ் வங்கியுடன் இணைக்கப்பட்டது."
        },

        # GT 24
        {
            "subtopic": "Model Co-operatives Act 1991 Principles",
            "stem_en": "What was the central philosophy of the Model Co-operatives Act drafted by the Choudhary Brahm Perkash Committee in 1991?",
            "stem_ta": "1991-ல் சவுத்ரி பிரம்ம பிரகாஷ் குழு வரைந்த மாதிரி கூட்டுறவு சங்கங்கள் சட்டத்தின் மையக் கோட்பாடு என்ன?",
            "options": [
                ("To make co-operatives autonomous, member-controlled, member-centric economic enterprises free from state control", "கூட்டுறவுகளை அரசாங்கக் கட்டுப்பாடற்ற, தன்னாட்சி பெற்ற, உறுப்பினர் மையப் பொருளாதார நிறுவனங்களாக மாற்றுதல்"),
                ("To nationalize all cooperative assets under central public sector undertakings", "அனைத்து கூட்டுறவு சொத்துக்களையும் மத்திய பொதுத்துறை நிறுவனங்களின் கீழ் தேசியமயமாக்குதல்"),
                ("To hand over cooperative management entirely to commercial banks", "கூட்டுறவு நிர்வாகத்தை வணிக வங்கிகளிடம் முழுமையாக ஒப்படைத்தல்"),
                ("To abolish voting rights for individual members", "தனிநபர் உறுப்பினர்களின் வாக்குரிமையை ரத்து செய்தல்")
            ],
            "correct_key": "A",
            "exp_en": "The Brahm Perkash Committee (1991) designed the Model Act to roll back intrusive government intervention (such as compulsory amalgamation, suo moto supersession, and government equity control) and restore democratic member autonomy.",
            "exp_ta": "பிரம்ம பிரகாஷ் குழு கூட்டுறவுகளில் அரசின் தேவையற்ற தலையீடுகளை நீக்கி, உறுப்பினர்கள் கட்டுப்பாட்டில் இயங்கும் தன்னாட்சி நிறுவனங்களாக அவற்றை மாற்ற மாதிரி சட்டத்தை வரைந்தது.",
            "why_a_en": "Correct. Member autonomy and freedom from bureaucratic hegemony was its core tenet.",
            "why_a_ta": "சரி. தன்னாட்சி மற்றும் அதிகாரவர்க்க தலையீடற்ற நிர்வாகமே இதன் முக்கிய நோக்கம்.",
            "why_b_en": "Incorrect. It advocated the exact opposite of state control.",
            "why_b_ta": "தவறு. அரசுடைமையாக்குவதற்கு இது எதிரானது.",
            "why_c_en": "Incorrect. Commercial bank takeover was never recommended.",
            "why_c_ta": "தவறு. வணிக வங்கிகளிடம் ஒப்படைக்கப் பரிந்துரைக்கவில்லை.",
            "why_d_en": "Incorrect. Member democracy was reinforced.",
            "why_d_ta": "தவறு. உறுப்பினர் ஜனநாயகம் மேலும் வலுப்படுத்தப்பட்டது.",
            "tip_en": "Brahm Perkash Committee (1991) = Self-reliance, minimal government control, genuine member democracy.",
            "tip_ta": "பிரம்ம பிரகாஷ் குழு (1991) = தற்சார்பு, குறைந்தபட்ச அரசுத் தலையீடு, உண்மையான உறுப்பினர் ஜனநாயகம்.",
            "fact_en": "States like Andhra Pradesh, Bihar, and Karnataka enacted parallel Self-Reliant Co-operative Societies Acts based on this Model Act.",
            "fact_ta": "ஆந்திரா, பீகார், கர்நாடகா உள்ளிட்ட மாநிலங்கள் இச்சட்டத்தின் அடிப்படையில் சுயசார்பு கூட்டுறவு சட்டங்களை இயற்றின."
        },

        # GT 25
        {
            "subtopic": "Common Service Centres in PACS",
            "stem_en": "By functioning as Common Service Centres (CSCs), Primary Agricultural Credit Societies are now empowered to provide:",
            "stem_ta": "பொது சேவை மையங்களாகச் (CSCs) செயல்படுவதன் மூலம், தொடக்க வேளாண் கடன் சங்கங்கள் இப்போது எவற்றை வழங்க அதிகாரம் பெற்றுள்ளன?",
            "options": [
                ("Over 300 government-to-citizen (G2C) and business-to-citizen (B2C) digital services at the village level", "கிராம அளவில் 300-க்கும் மேற்பட்ட அரசு மற்றும் வணிக டிஜிட்டல் சேவைகளை பொதுமக்களுக்கு வழங்குதல்"),
                ("Only crop loans and fertilizer distribution", "பயிர்க் கடன் மற்றும் உர விநியோகம் மட்டுமே"),
                ("Passport issuance directly to international travelers", "சர்வதேச பயணிகளுக்கு நேரடியாக பாஸ்போர்ட் வழங்குதல்"),
                ("Conducting state assembly elections in the village", "கிராமத்தில் சட்டமன்றத் தேர்தல்களை நடத்துதல்")
            ],
            "correct_key": "A",
            "exp_en": "Through CSC integration, PACS can deliver over 300 digital public services including Aadhaar seeding, utility bill payments, insurance, railway/flight ticketing, banking correspondent services, and land records access to rural citizens.",
            "exp_ta": "பொது சேவை மையங்கள் மூலம் ஆதார் இணைப்பு, மின் கட்டணம் செலுத்துதல், காப்பீடு, ரயில் பயணச்சீட்டு, பட்டா-சிட்டா உள்ளிட்ட 300-க்கும் மேற்பட்ட அரசு மற்றும் வணிக சேவைகளை PACS சங்கங்கள் கிராம மக்களுக்கு வழங்குகின்றன.",
            "why_a_en": "Correct. Over 300 digital citizen services are enabled through CSC-PACS integration.",
            "why_a_ta": "சரி. 300-க்கும் மேற்பட்ட டிஜிட்டல் மக்கள் சேவைகள் இதன் மூலம் வழங்கப்படுகின்றன.",
            "why_b_en": "Incorrect. CSCs go far beyond crop loans.",
            "why_b_ta": "தவறு. பயிர்க்கடனைத் தாண்டி பல சேவைகள் உள்ளன.",
            "why_c_en": "Incorrect. Passports are issued only by the Ministry of External Affairs.",
            "why_c_ta": "தவறு. வெளியுறவு அமைச்சகமே பாஸ்போர்ட் வழங்குகிறது.",
            "why_d_en": "Incorrect. Elections are conducted by Election Commissions.",
            "why_d_ta": "தவறு. தேர்தலை தேர்தல் ஆணையங்கள் நடத்துகின்றன.",
            "tip_en": "PACS as CSC: Eliminates rural-urban digital divide by turning village credit societies into Digital Service Hubs.",
            "tip_ta": "PACS பொது சேவை மையம்: கிராமப்புற கடன் சங்கங்களை டிஜிட்டல் சேவை மையங்களாக மாற்றி கிராம-நகர இடைவெளியைக் குறைக்கிறது.",
            "fact_en": "An MoU between Ministry of Cooperation, Ministry of Electronics & IT, NABARD, and CSC e-Governance Services was signed in February 2023.",
            "fact_ta": "பிப்ரவரி 2023-ல் இதற்கான புரிந்துணர்வு ஒப்பந்தம் மத்திய கூட்டுறவு மற்றும் IT அமைச்சகங்களால் கையெழுத்தானது."
        },

        # GT 26
        {
            "subtopic": "Reserve Bank Priority Sector Lending - Cooperatives",
            "stem_en": "Urban Co-operative Banks (UCBs) are required by the Reserve Bank of India to achieve what overall Priority Sector Lending (PSL) target by 31st March 2026?",
            "stem_ta": "2026 மார்ச் 31-க்குள் நகர்ப்புற கூட்டுறவு வங்கிகள் (UCBs) எத்தனை சதவீத முன்னுரிமைத் துறை கடன் (PSL) இலக்கை அடைய வேண்டும் என்று ரிசர்வ் வங்கி கட்டாயமாக்கியுள்ளது?",
            "options": [
                ("75% of Adjusted Net Bank Credit (ANBC)", "சரிசெய்யப்பட்ட நிகர வங்கிக் கடனில் 75%"),
                ("40% of Adjusted Net Bank Credit (ANBC)", "சரிசெய்யப்பட்ட நிகர வங்கிக் கடனில் 40%"),
                ("50% of Adjusted Net Bank Credit (ANBC)", "சரிசெய்யப்பட்ட நிகர வங்கிக் கடனில் 50%"),
                ("100% of Adjusted Net Bank Credit (ANBC)", "சரிசெய்யப்பட்ட நிகர வங்கிக் கடனில் 100%")
            ],
            "correct_key": "A",
            "exp_en": "The Reserve Bank of India mandated that Urban Co-operative Banks must increase their overall Priority Sector Lending (PSL) target to 75% of Adjusted Net Bank Credit (ANBC) or Credit Equivalent Amount of Off-Balance Sheet Exposure (CEOBE) in a phased manner by March 31, 2026.",
            "exp_ta": "ரிசர்வ் வங்கி நகர்ப்புற கூட்டுறவு வங்கிகள் தங்களின் முன்னுரிமைத் துறை கடனை (PSL) படிப்படியாக உயர்த்தி 2026 மார்ச் 31-க்குள் 75% அடைய வேண்டும் என உத்தரவிட்டுள்ளது.",
            "why_a_en": "Correct. 75% of ANBC is the revised PSL target for UCBs.",
            "why_a_ta": "சரி. நகர்ப்புற கூட்டுறவு வங்கிகளுக்கு 75% PSL இலக்கு நிர்ணயிக்கப்பட்டுள்ளது.",
            "why_b_en": "Incorrect. 40% is the PSL target for domestic scheduled commercial banks.",
            "why_b_ta": "தவறு. 40% என்பது வழக்கமான வணிக வங்கிகளுக்கான இலக்கு.",
            "why_c_en": "Incorrect. 50% was an intermediate milestone.",
            "why_c_ta": "தவறு. 50% இடைக்கால இலக்கு.",
            "why_d_en": "Incorrect. 100% is not required.",
            "why_d_ta": "தவறு. 100% இலக்கு அல்ல.",
            "tip_en": "PSL Targets: Commercial Banks = 40%; Regional Rural Banks (RRBs) & Small Finance Banks (SFBs) & UCBs = 75%.",
            "tip_ta": "PSL இலக்குகள்: வணிக வங்கிகள் = 40%; ஊரக வங்கிகள், SFB & UCB கூட்டுறவு வங்கிகள் = 75%.",
            "fact_en": "Sub-targets include advances to micro-enterprises and weaker sections.",
            "fact_ta": "இதில் குறுந்தொழில்கள் மற்றும் நலிவடைந்த பிரிவினருக்கான உட்பிரிவு இலக்குகளும் அடங்கும்."
        },

        # GT 27
        {
            "subtopic": "Offences under Article 243ZQ - Employer Default",
            "stem_en": "Under Article 243ZQ(1)(d), an employer commits an offence if the employer fails to pay to a cooperative society amounts deducted from employee wages within what period?",
            "stem_ta": "உறுப்பு 243ZQ(1)(d)-ன் கீழ், ஊழியர்களின் ஊதியத்திலிருந்து பிடித்தம் செய்த தொகையை எத்தனை நாட்களுக்குள் கூட்டுறவு சங்கத்தில் செலுத்தத் தவறினால் முதலாளி குற்றம் புரிகிறார்?",
            "options": [
                ("A period of fourteen days from the date on which such deduction is made", "அத்தகைய பிடித்தம் செய்யப்பட்ட தேதியிலிருந்து பதினான்கு நாட்களுக்குள்"),
                ("A period of thirty days from the close of the financial year", "நிதியாண்டு முடிந்த முப்பது நாட்களுக்குள்"),
                ("A period of six months from the deduction", "பிடித்தம் செய்த தேதியிலிருந்து ஆறு மாதங்களுக்குள்"),
                ("A period of sixty days from salary payment", "சம்பள வழங்கல் தேதியிலிருந்து அறுபது நாட்களுக்குள்")
            ],
            "correct_key": "A",
            "exp_en": "Article 243ZQ(1)(d) explicitly classifies as an offence: failure by an employer to pay to a co-operative society amounts deducted from employee wages under agreement within a period of fourteen days from the date of deduction.",
            "exp_ta": "உறுப்பு 243ZQ(1)(d)-ன் படி, ஊழியர் சம்பளத்தில் பிடித்தம் செய்த தொகையை 14 நாட்களுக்குள் கூட்டுறவு சங்கத்தில் செலுத்தத் தவறினால் முதலாளி தண்டனைக்குரிய குற்றம் புரிகிறார்.",
            "why_a_en": "Correct. Exactly 14 days from the date of deduction.",
            "why_a_ta": "சரி. பிடித்தம் செய்த தேதியிலிருந்து சரியாக 14 நாட்களுக்குள்.",
            "why_b_en": "Incorrect. 30 days is not the constitutional timeline.",
            "why_b_ta": "தவறு. 30 நாட்கள் என்பது தவறானது.",
            "why_c_en": "Incorrect. Six months is far too long.",
            "why_c_ta": "தவறு. 6 மாதங்கள் மிக நீண்ட காலம்.",
            "why_d_en": "Incorrect. 60 days is incorrect.",
            "why_d_ta": "தவறு. 60 நாட்கள் தவறானது.",
            "tip_en": "Key Penalty Timeline: Employer must remit cooperative salary deductions within 14 days (Art 243ZQ(1)(d)).",
            "tip_ta": "முக்கியக் காலக்கெடு: சம்பளப் பிடித்தத் தொகையை முதலாளி 14 நாட்களுக்குள் சங்கத்தில் செலுத்த வேண்டும்.",
            "fact_en": "This protects employee-credit cooperative societies from employer default and cash crunch.",
            "fact_ta": "இது ஊழியர் கடன் கூட்டுறவு சங்கங்களை முதலாளிகளின் பணப்பறிப்பிலிருந்து பாதுகாக்கிறது."
        },

        # GT 28
        {
            "subtopic": "Government Shareholding in Cooperatives",
            "stem_en": "What is the primary difference between a cooperative society where government holds share capital and one where there is no government aid, regarding supersession under Article 243ZL?",
            "stem_ta": "அரசு பங்கு மூலதனம் வைத்துள்ள கூட்டுறவு சங்கத்திற்கும், அரசு உதவி பெறாத சங்கத்திற்கும் இடையே உறுப்பு 243ZL-ன் கீழ் வாரியக் கலைப்பு குறித்த முதன்மை வேறுபாடு என்ன?",
            "options": [
                ("The board of a society with no government shares or loans cannot be superseded on grounds of persistent default, except in case of election deadlock", "தேர்தல் முடக்கம் போன்ற குறிப்பிட்ட விதிவிலக்குகள் தவிர்த்து, அரசு உதவி பெறாத சங்கங்களின் வாரியத்தைக் கலைக்க முடியாது"),
                ("Societies with no government shares cannot be audited by statutory auditors", "அரசுப் பங்குகள் இல்லாத சங்கங்களை தணிக்கையாளர்களால் தணிக்கை செய்ய முடியாது"),
                ("Societies with government shares have a 10-year term of office", "அரசுப் பங்குகள் உள்ள சங்கங்கள் 10 ஆண்டுகள் பதவிக்காலம் கொண்டிருக்கும்"),
                ("Societies with no government aid are exempt from the Constitution", "அரசு உதவி பெறாத சங்கங்களுக்கு அரசியலமைப்பு பொருந்தாது")
            ],
            "correct_key": "A",
            "exp_en": "The first proviso to Article 243ZL(1) explicitly protects cooperative societies with no government shareholding, loan, financial assistance, or guarantee from executive supersession, safeguarding their financial and managerial independence.",
            "exp_ta": "உறுப்பு 243ZL(1)-ன் முதல் வரம்புரை, அரசுப் பங்கு அல்லது கடன் உதவி இல்லாத தன்னாட்சி பெற்ற சங்கங்களை நிர்வாக ரீதியான வாரியக் கலைப்பிலிருந்து பாதுகாக்கிறது.",
            "why_a_en": "Correct. Proviso to 243ZL(1) grants immunity from supersession to self-reliant cooperatives.",
            "why_a_ta": "சரி. உறுப்பு 243ZL(1) வரம்புரை தற்சார்பு கூட்டுறவுகளுக்கு வாரியக் கலைப்பிலிருந்து பாதுகாப்பு அளிக்கிறது.",
            "why_b_en": "Incorrect. Audit is mandatory for all under Article 243ZM.",
            "why_b_ta": "தவறு. உறுப்பு 243ZM-ன் படி தணிக்கை அனைவருக்கும் கட்டாயம்.",
            "why_c_en": "Incorrect. Term is uniform 5 years under 243ZJ.",
            "why_c_ta": "தவறு. பதவிக்காலம் அனைவருக்கும் 5 ஆண்டுகள்.",
            "why_d_en": "Incorrect. Part IX-B applies uniformly.",
            "why_d_ta": "தவறு. அரசியலமைப்பு அனைவருக்கும் பொதுவானது.",
            "tip_en": "Self-reliance brings autonomy: No Govt Equity/Aid = Protected from State Supersession.",
            "tip_ta": "தற்சார்பே தன்னாட்சி: அரசு நிதி இல்லை என்றால் = வாரியக் கலைப்பிலிருந்து அரசமைப்புப் பாதுகாப்பு.",
            "fact_en": "This distinction implements the Brahm Perkash Committee recommendations on self-reliant cooperatives.",
            "fact_ta": "சுயசார்பு கூட்டுறவுகள் மீதான பிரம்ம பிரகாஷ் குழுவின் பரிந்துரையை இது பிரதிபலிக்கிறது."
        },

        # GT 29
        {
            "subtopic": "National Cooperative Organics Limited (NCOL)",
            "stem_en": "Under which commercial brand name does the National Cooperative Organics Limited (NCOL) market certified organic farm produce in India?",
            "stem_ta": "இந்தியாவில் சான்றளிக்கப்பட்ட இயற்கை விவசாய விளைபொருட்களை தேசிய கூட்டுறவு இயற்கை நிறுவனம் (NCOL) எந்த வணிக பிராண்ட் பெயரில் சந்தைப்படுத்துகிறது?",
            "options": [
                ("Bharat Organics", "பாரத் ஆர்கானிக்ஸ் (Bharat Organics)"),
                ("Amul Organic", "அமுல் ஆர்கானிக் (Amul Organic)"),
                ("Coop-Fresh", "கோ-ஆப் பிரஷ் (Coop-Fresh)"),
                ("Green India", "கிரீன் இந்தியா (Green India)")
            ],
            "correct_key": "A",
            "exp_en": "National Cooperative Organics Limited (NCOL), launched in 2023, markets certified organic agricultural products under the flagship national brand 'Bharat Organics'.",
            "exp_ta": "2023-ல் தொடங்கப்பட்ட தேசிய கூட்டுறவு இயற்கை நிறுவனம் (NCOL), சான்றளிக்கப்பட்ட இயற்கை விளைபொருட்களை 'பாரத் ஆர்கானிக்ஸ்' என்ற தேசிய பிராண்ட் பெயரில் சந்தைப்படுத்துகிறது.",
            "why_a_en": "Correct. 'Bharat Organics' is the official brand of NCOL.",
            "why_a_ta": "சரி. 'பாரத் ஆர்கானிக்ஸ்' என்பது NCOL-ன் அதிகாரப்பூர்வ பிராண்ட் ஆகும்.",
            "why_b_en": "Incorrect. Amul Organic is a separate product line of GCMMF.",
            "why_b_ta": "தவறு. அமுல் ஆர்கானிக் என்பது அமுலின் தனி தயாரிப்பு.",
            "why_c_en": "Incorrect. Not Coop-Fresh.",
            "why_c_ta": "தவறு. கோ-ஆப் பிரஷ் அல்ல.",
            "why_d_en": "Incorrect. Not Green India.",
            "why_d_ta": "தவறு. கிரீன் இந்தியா அல்ல.",
            "tip_en": "Brand Names: NCOL = Bharat Organics; Three National Multi-State Coops = NCEL, NCOL, BBSSL.",
            "tip_ta": "பிராண்ட்: NCOL = பாரத் ஆர்கானிக்ஸ்; 3 தேசிய அமைப்புகள் = NCEL, NCOL, BBSSL.",
            "fact_en": "NCOL tests and certifies soil and produce at affordable rates through network labs.",
            "fact_ta": "NCOL நியாயமான கட்டணத்தில் மண் மற்றும் விளைபொருட்களைப் பரிசோதித்து சான்றளிக்கிறது."
        },

        # GT 30
        {
            "subtopic": "Government of India Act 1935 - Cooperative Classification",
            "stem_en": "In the Government of India Act, 1935, co-operative societies were placed under:",
            "stem_ta": "1935-ஆம் ஆண்டின் இந்திய அரசுச் சட்டத்தில், கூட்டுறவு சங்கங்கள் எதன் கீழ் வைக்கப்பட்டன?",
            "options": [
                ("Provincial Legislative List (List II)", "மாகாண சட்டமன்றப் பட்டியல் (பட்டியல் II)"),
                ("Federal Legislative List (List I)", "கூட்டாட்சி சட்டமன்றப் பட்டியல் (பட்டியல் I)"),
                ("Concurrent Legislative List (List III)", "பொது சட்டமன்றப் பட்டியல் (பட்டியல் III)"),
                ("Residuary powers vested in Governor-General", "தலைமை ஆளுநரின் எஞ்சிய அதிகாரங்கள்")
            ],
            "correct_key": "A",
            "exp_en": "Under the Government of India Act, 1935, 'Co-operative societies' was placed in Item 33 of the Provincial Legislative List (List II), cementing its status as an exclusively provincial matter, which carried forward to List II Entry 32 of the 1950 Constitution.",
            "exp_ta": "1935 இந்திய அரசுச் சட்டத்தில், கூட்டுறவு சங்கங்கள் மாகாணப் பட்டியலின் (பட்டியல் II) பதிவு 33-ல் வைக்கப்பட்டன. இதுவே 1950 அரசியலமைப்பின் பட்டியல் II பதிவு 32-ல் தொடர்ந்தது.",
            "why_a_en": "Correct. Provincial Legislative List (List II) was the classification in 1935.",
            "why_a_ta": "சரி. 1935-ல் மாகாணப் பட்டியலிலேயே கூட்டுறவு வைக்கப்பட்டது.",
            "why_b_en": "Incorrect. Corporations with objects not confined to one province were in List I.",
            "why_b_ta": "தவறு. பல மாகாண அமைப்புகள் பட்டியல் I-ல் இருந்தன.",
            "why_c_en": "Incorrect. Concurrent List did not cover cooperative societies.",
            "why_c_ta": "தவறு. பொதுப் பட்டியலில் கூட்டுறவு இல்லை.",
            "why_d_en": "Incorrect. Residuary power was discretionary with the Governor-General, but cooperation was enumerated.",
            "why_d_ta": "தவறு. கூட்டுறவு வெளிப்படையாக மாகாணப் பட்டியலில் பட்டியலிடப்பட்டது.",
            "tip_en": "Continuity of Legislative Competence: 1919 (Transferred) → 1935 (Provincial List II) → 1950 (State List II Entry 32).",
            "tip_ta": "சட்ட அதிகாரத் தொடர்ச்சி: 1919 (மாற்றப்பட்ட துறை) → 1935 (மாகாணப் பட்டியல்) → 1950 (மாநிலப் பட்டியல் பதிவு 32).",
            "fact_en": "Provincial autonomy introduced under the 1935 Act deepened local cooperative administration.",
            "fact_ta": "1935 சட்டம் அறிமுகப்படுத்திய மாகாண தன்னாட்சி கூட்டுறவு நிர்வாகத்தை மேலும் பரவலாக்கியது."
        }
    ]


def get_gt_batch1_raw_part2():
    return [
        # GT 31
        {
            "subtopic": "NABARD Formation Date",
            "stem_en": "On which date was the National Bank for Agriculture and Rural Development (NABARD) officially dedicated to the service of the nation by Prime Minister Indira Gandhi?",
            "stem_ta": "விவசாயம் மற்றும் ஊரக வளர்ச்சிக்கான தேசிய வங்கி (NABARD) பிரதமர் இந்திரா காந்தியால் எந்த நாளில் அதிகாரப்பூர்வமாக நாட்டுக்கு அர்ப்பணிக்கப்பட்டது?",
            "options": [
                ("5th November 1982", "1982 நவம்பர் 5"),
                ("12th July 1982", "1982 ஜூலை 12"),
                ("15th August 1982", "1982 ஆகஸ்ட் 15"),
                ("2nd October 1982", "1982 அக்டோபர் 2")
            ],
            "correct_key": "A",
            "exp_en": "Although NABARD came into existence on 12 July 1982 under Act 61 of 1981, it was formally dedicated to the service of the nation by the then Prime Minister Indira Gandhi on 5 November 1982.",
            "exp_ta": "நபார்டு வங்கி 1982 ஜூலை 12 அன்று முறைப்படி தொடங்கப்பட்டாலும், அன்றைய பிரதமர் இந்திரா காந்தியால் 1982 நவம்பர் 5 அன்று அதிகாரப்பூர்வமாக நாட்டுக்கு அர்ப்பணிக்கப்பட்டது.",
            "why_a_en": "Correct. Dedicated to the nation on 5 November 1982.",
            "why_a_ta": "சரி. 1982 நவம்பர் 5 அன்று நாட்டுக்கு அர்ப்பணிக்கப்பட்டது.",
            "why_b_en": "Incorrect. 12 July 1982 was the legal date of establishment.",
            "why_b_ta": "தவறு. 1982 ஜூலை 12 சட்டப்பூர்வமாக அமைக்கப்பட்ட நாள்.",
            "why_c_en": "Incorrect. Not Independence Day.",
            "why_c_ta": "தவறு. சுதந்திர தினம் அல்ல.",
            "why_d_en": "Incorrect. Not Gandhi Jayanti.",
            "why_d_ta": "தவறு. காந்தி ஜெயந்தி அல்ல.",
            "tip_en": "NABARD Dual Dates: Established on 12 July 1982; Dedicated to nation on 5 Nov 1982.",
            "tip_ta": "நபார்டு இரு முக்கிய தேதிகள்: அமைக்கப்பட்ட நாள் 12 ஜூலை 1982; நாட்டுக்கு அர்ப்பணிக்கப்பட்ட நாள் 5 நவம்பர் 1982.",
            "fact_en": "NABARD started with an initial capital of ₹100 crore contributed equally by Government of India and RBI.",
            "fact_ta": "மத்திய அரசு மற்றும் ரிசர்வ் வங்கியின் சம பங்களிப்புடன் ₹100 கோடி மூலதனத்துடன் நபார்டு தொடங்கியது."
        },

        # GT 32
        {
            "subtopic": "Tamil Nadu Cooperative Societies Act 1983 Enforcement",
            "stem_en": "Although the Tamil Nadu Co-operative Societies Act was passed by the State Legislature in 1983, in which year did it finally come into force throughout Tamil Nadu after receiving Presidential assent?",
            "stem_ta": "தமிழ்நாடு கூட்டுறவு சங்கங்கள் சட்டம் 1983-ல் சட்டமன்றத்தில் நிறைவேற்றப்பட்டாலும், குடியரசுத் தலைவர் ஒப்புதல் பெற்று எந்த ஆண்டு தமிழ்நாடு முழுவதும் இறுதியாக நடைமுறைக்கு வந்தது?",
            "options": [
                ("1988", "1988"),
                ("1983", "1983"),
                ("1985", "1985"),
                ("1991", "1991")
            ],
            "correct_key": "A",
            "exp_en": "The Tamil Nadu Co-operative Societies Act, 1983 (Act 30 of 1983) received Presidential assent on 21 August 1987 and officially came into force on 13th April 1988.",
            "exp_ta": "தமிழ்நாடு கூட்டுறவு சங்கங்கள் சட்டம் 1983-ல் நிறைவேற்றப்பட்டு, 1987 ஆகஸ்ட் 21 அன்று குடியரசுத் தலைவர் ஒப்புதல் பெற்று, 1988 ஏப்ரல் 13 அன்று அதிகாரப்பூர்வமாக நடைமுறைக்கு வந்தது.",
            "why_a_en": "Correct. Enforced on 13 April 1988 throughout Tamil Nadu.",
            "why_a_ta": "சரி. 1988 ஏப்ரல் 13 அன்று நடைமுறைக்கு வந்தது.",
            "why_b_en": "Incorrect. 1983 was the year of legislative passage, not enforcement.",
            "why_b_ta": "தவறு. 1983 நிறைவேற்றப்பட்ட ஆண்டு.",
            "why_c_en": "Incorrect. 1985 is incorrect.",
            "why_c_ta": "தவறு. 1985 தவறான ஆண்டு.",
            "why_d_en": "Incorrect. 1991 is incorrect.",
            "why_d_ta": "தவறு. 1991 தவறான ஆண்டு.",
            "tip_en": "TN Act 1983: Enacted = 1983; Assent = 1987; Enforced = 13 April 1988.",
            "tip_ta": "தமிழக சட்டம் 1983: இயற்றப்பட்டது = 1983; ஒப்புதல் = 1987; அமல் = 13 ஏப்ரல் 1988.",
            "fact_en": "It replaced the Tamil Nadu Co-operative Societies Act, 1961 (Act 53 of 1961).",
            "fact_ta": "இது 1961-ஆம் ஆண்டின் தமிழ்நாடு கூட்டுறவு சங்கங்கள் சட்டத்திற்கு மாற்றாக வந்தது."
        },

        # GT 33
        {
            "subtopic": "Dispute Resolution Bar of Civil Courts",
            "stem_en": "Under Section 156 of the Tamil Nadu Co-operative Societies Act, 1983, the jurisdiction of which judicial authority is barred regarding disputes referable to the Registrar under Section 90?",
            "stem_ta": "தமிழ்நாடு கூட்டுறவு சங்கங்கள் சட்டம் 1983-ன் பிரிவு 156-ன் கீழ், பிரிவு 90-ன் படி பதிவாளரிடம் அனுப்பக்கூடிய தகராறுகள் தொடர்பாக எந்த நீதித்துறை அமைப்பின் அதிகார வரம்பிற்குத் தடை விதிக்கப்பட்டுள்ளது?",
            "options": [
                ("Civil Court", "உரிமையியல் நீதிமன்றம் (Civil Court)"),
                ("Co-operative Tribunal", "கூட்டுறவு தீர்ப்பாயம்"),
                ("High Court under Article 226", "உறுப்பு 226-ன் கீழ் உயர்நீதிமன்றம்"),
                ("Supreme Court under Article 32", "உறுப்பு 32-ன் கீழ் உச்சநீதிமன்றம்")
            ],
            "correct_key": "A",
            "exp_en": "Section 156 of the 1983 Act bars the jurisdiction of civil and revenue courts in respect of any dispute required to be referred to the Registrar under Section 90. However, constitutional writ jurisdiction under Articles 226/32 cannot be ousted by ordinary statute.",
            "exp_ta": "பிரிவு 156-ன் படி உரிமையியல் நீதிமன்றங்கள் கூட்டுறவுத் தகராறுகளை விசாரிக்கத் தடை உள்ளது. ஆனால் உயர்/உச்ச நீதிமன்றங்களின் அரசியலமைப்பு நீதிப்பேராணை அதிகாரத்தைத் தடுக்க முடியாது.",
            "why_a_en": "Correct. Section 156 expressly bars Civil Courts.",
            "why_a_ta": "சரி. பிரிவு 156 உரிமையியல் நீதிமன்றங்களின் அதிகார வரம்பைத் தடுக்கிறது.",
            "why_b_en": "Incorrect. The Co-operative Tribunal has statutory appellate jurisdiction under Section 152.",
            "why_b_ta": "தவறு. கூட்டுறவு தீர்ப்பாயத்திற்கு மேல்முறையீட்டு அதிகாரம் உண்டு.",
            "why_c_en": "Incorrect. State law cannot bar High Court's Article 226 powers.",
            "why_c_ta": "தவறு. உயர்நீதிமன்றத்தின் உறுப்பு 226 அதிகாரத்தை மாநில சட்டத்தால் தடுக்க முடியாது.",
            "why_d_en": "Incorrect. Article 32 powers cannot be ousted.",
            "why_d_ta": "தவறு. உச்சநீதிமன்ற அதிகாரத்தை சாதாரண சட்டம் தடுக்க முடியாது.",
            "tip_en": "Bar of Jurisdiction: State acts bar ordinary Civil Courts to ensure speedy arbitration by Registrar/Tribunal.",
            "tip_ta": "அதிகார வரம்புத் தடை: விரைவான தீர்விற்காக உரிமையியல் நீதிமன்றங்களுக்குத் தடை விதிக்கப்பட்டு பதிவாளர் மற்றும் தீர்ப்பாயத்திடம் அதிகாரம் வழங்கப்படுகிறது.",
            "fact_en": "Section 90 covers disputes between members, past members, societies, and employees touching the business of the society.",
            "fact_ta": "பிரிவு 90 சங்கத்தின் வணிகம் தொடர்பான அனைத்து உள் தகராறுகளையும் உள்ளடக்குகிறது."
        },

        # GT 34
        {
            "subtopic": "International Co-operative Alliance (ICA) Origins",
            "stem_en": "In which city was the International Co-operative Alliance (ICA), the apex global non-governmental body representing cooperatives worldwide, founded in 1895?",
            "stem_ta": "உலகளாவிய கூட்டுறவுகளைப் பிரதிநிதித்துவப்படுத்தும் உச்ச சர்வதேச அரசு சாரா அமைப்பான சர்வதேச கூட்டுறவு கூட்டணி (ICA) 1895-ல் எந்த நகரில் நிறுவப்பட்டது?",
            "options": [
                ("London (United Kingdom)", "லண்டன் (ஐக்கிய அரசு)"),
                ("Geneva (Switzerland)", "ஜெனிவா (சுவிட்சர்லாந்து)"),
                ("Manchester (United Kingdom)", "மான்செஸ்டர் (ஐக்கிய அரசு)"),
                ("Paris (France)", "பாரிஸ் (பிரான்ஸ்)")
            ],
            "correct_key": "A",
            "exp_en": "The International Co-operative Alliance was founded in London, England, on 19 August 1895 during the 1st Co-operative Congress.",
            "exp_ta": "சர்வதேச கூட்டுறவு கூட்டணி (ICA) 1895 ஆகஸ்ட் 19 அன்று லண்டனில் நடைபெற்ற முதல் கூட்டுறவு மாநாட்டில் நிறுவப்பட்டது.",
            "why_a_en": "Correct. Founded in London in 1895.",
            "why_a_ta": "சரி. 1895-ல் லண்டனில் நிறுவப்பட்டது.",
            "why_b_en": "Incorrect. Geneva is home to ILO, not the original founding city of ICA.",
            "why_b_ta": "தவறு. ஜெனிவா ILO உள்ள இடம்.",
            "why_c_en": "Incorrect. Manchester was the site of the 1995 Centennial Congress.",
            "why_c_ta": "தவறு. மான்செஸ்டர் 1995 நூற்றாண்டு மாநாடு நடந்த இடம்.",
            "why_d_en": "Incorrect. Not Paris.",
            "why_d_ta": "தவறு. பாரிஸ் அல்ல.",
            "tip_en": "ICA Milestones: Founded in London (1895); Centennial Congress at Manchester (1995); Current HQ = Brussels, Belgium.",
            "tip_ta": "ICA மைல்கற்கள்: லண்டனில் தொடக்கம் (1895); மான்செஸ்டர் மாநாடு (1995); தற்போதைய தலைமையகம் = பிரஸ்ஸல்ஸ், பெல்ஜியம்.",
            "fact_en": "The ICA is one of the largest non-governmental organizations in the world by the number of people represented (~1 billion individuals).",
            "fact_ta": "உறுப்பினர் எண்ணிக்கையின் அடிப்படையில் உலகின் மிகப்பெரிய அரசு சாரா அமைப்புகளில் ICA ஒன்றாகும் (~100 கோடி மக்கள்)."
        },

        # GT 35
        {
            "subtopic": "Tamil Nadu Cooperative Audit Department",
            "stem_en": "In Tamil Nadu, cooperative audit is conducted by an independent department known as the Department of Co-operative Audit, which functions under which administrative department of the State Government?",
            "stem_ta": "தமிழ்நாட்டில் கூட்டுறவு தணிக்கையானது கூட்டுறவு தணிக்கைத் துறை என்ற தனித் துறையால் நடத்தப்படுகிறது. இது மாநில அரசின் எந்த நிர்வாகத் துறையின் கீழ் செயல்படுகிறது?",
            "options": [
                ("Finance Department", "நிதித் துறை"),
                ("Co-operation, Food and Consumer Protection Department", "கூட்டுறவு, உணவு மற்றும் நுகர்வோர் பாதுகாப்புத் துறை"),
                ("Revenue Department", "வருவாய்த் துறை"),
                ("Law Department", "சட்டத் துறை")
            ],
            "correct_key": "A",
            "exp_en": "In Tamil Nadu, to ensure independence from administrative control, the Department of Co-operative Audit was separated from the Registrar and placed under the administrative control of the Finance Department in 1981.",
            "exp_ta": "நிர்வாகத் தலையீடின்றி தணிக்கை சுதந்திரமாக நடைபெற வேண்டும் என்பதற்காக, 1981-ல் கூட்டுறவு தணிக்கைத் துறை பதிவாளரிடமிருந்து பிரிக்கப்பட்டு நிதித் துறையின் கீழ் வைக்கப்பட்டது.",
            "why_a_en": "Correct. Co-operative Audit in TN functions under the Finance Department.",
            "why_a_ta": "சரி. தமிழகத்தில் கூட்டுறவு தணிக்கைத் துறை நிதித் துறையின் கீழ் இயங்குகிறது.",
            "why_b_en": "Incorrect. The Cooperation Department administers societies, but audit is placed under Finance to maintain independence.",
            "why_b_ta": "தவறு. கூட்டுறவுத் துறை சங்கங்களை நிர்வகிக்கிறது, தணிக்கை நிதித் துறையின் கீழ் உள்ளது.",
            "why_c_en": "Incorrect. Not Revenue Department.",
            "why_c_ta": "தவறு. வருவாய்த் துறை அல்ல.",
            "why_d_en": "Incorrect. Not Law Department.",
            "why_d_ta": "தவறு. சட்டத் துறை அல்ல.",
            "tip_en": "Structural check in TN: Cooperative Administration = Cooperation Department (RCS); Cooperative Audit = Finance Department (Director of Co-op Audit).",
            "tip_ta": "தமிழகக் கட்டமைப்பு: கூட்டுறவு நிர்வாகம் = கூட்டுறவுத் துறை (RCS); கூட்டுறவு தணிக்கை = நிதித் துறை (தணிக்கை இயக்குநர்).",
            "fact_en": "The Director of Co-operative Audit is the functional head of the department.",
            "fact_ta": "கூட்டுறவு தணிக்கைத் துறையின் தலைவராக கூட்டுறவு தணிக்கை இயக்குநர் செயல்படுகிறார்."
        },

        # GT 36
        {
            "subtopic": "Urban Co-operative Banks Tiering System",
            "stem_en": "Under the revised regulatory framework introduced by the RBI in 2022, Urban Co-operative Banks (UCBs) are categorized into how many tiers based on their deposit size?",
            "stem_ta": "2022-ல் ரிசர்வ் வங்கி அறிமுகப்படுத்திய திருத்தப்பட்ட ஒழுங்குமுறைக் கட்டமைப்பின் கீழ், நகர்ப்புற கூட்டுறவு வங்கிகள் (UCBs) அவற்றின் வைப்புத்தொகை அளவின் அடிப்படையில் எத்தனை அடுக்குகளாகப் பிரிக்கப்பட்டுள்ளன?",
            "options": [
                ("Four Tiers (Tier 1 to Tier 4)", "நான்கு அடுக்குகள் (அடுக்கு 1 முதல் அடுக்கு 4 வரை)"),
                ("Two Tiers (Tier 1 and Tier 2)", "இரண்டு அடுக்குகள் (அடுக்கு 1 மற்றும் அடுக்கு 2)"),
                ("Three Tiers (Tier 1, Tier 2, Tier 3)", "மூன்று அடுக்குகள் (அடுக்கு 1, 2 மற்றும் 3)"),
                ("Five Tiers (Tier 1 to Tier 5)", "ஐந்து அடுக்குகள் (அடுக்கு 1 முதல் அடுக்கு 5 வரை)")
            ],
            "correct_key": "A",
            "exp_en": "Following the N.S. Vishwanathan Committee recommendations, the RBI categorized UCBs into a four-tiered regulatory structure: Tier 1 (deposits up to ₹100 crore), Tier 2 (₹100 crore to ₹1,000 crore), Tier 3 (₹1,000 crore to ₹10,000 crore), and Tier 4 (deposits above ₹10,000 crore).",
            "exp_ta": "என்.எஸ். விஸ்வநாதன் குழுவின் பரிந்துரைப்படி ரிசர்வ் வங்கி UCB-களை 4 அடுக்குகளாகப் பிரித்துள்ளது: அடுக்கு 1 (₹100 கோடி வரை), அடுக்கு 2 (₹100 முதல் ₹1,000 கோடி), அடுக்கு 3 (₹1,000 முதல் ₹10,000 கோடி), அடுக்கு 4 (₹10,000 கோடிக்கு மேல்).",
            "why_a_en": "Correct. Four Tiers (Tier 1 to Tier 4) based on deposits.",
            "why_a_ta": "சரி. வைப்புத்தொகை அடிப்படையில் 4 அடுக்குகள்.",
            "why_b_en": "Incorrect. Two tiers was the older pre-2022 categorization.",
            "why_b_ta": "தவறு. இரண்டு அடுக்கு என்பது 2022-க்கு முந்தைய பழைய முறை.",
            "why_c_en": "Incorrect. Not three tiers.",
            "why_c_ta": "தவறு. மூன்று அடுக்கு அல்ல.",
            "why_d_en": "Incorrect. Not five tiers.",
            "why_d_ta": "தவறு. ஐந்து அடுக்கு அல்ல.",
            "tip_en": "UCB Tiering (2022): Tier 1 (<=100cr), Tier 2 (100-1000cr), Tier 3 (1000-10000cr), Tier 4 (>10000cr).",
            "tip_ta": "UCB அடுக்குகள் (2022): அடுக்கு 1 (<=100 கோடி), அடுக்கு 2 (100-1000 கோடி), அடுக்கு 3 (1000-10000 கோடி), அடுக்கு 4 (>10000 கோடி).",
            "fact_en": "Capital Adequacy (CRAR) minimum is 9% for Tier 1 and 12% for Tiers 2 to 4.",
            "fact_ta": "அடுக்கு 1-க்கு குறைந்தபட்ச மூலதனப் பாதுகாப்பு (CRAR) 9%, அடுக்கு 2 முதல் 4-க்கு 12% ஆகும்."
        },

        # GT 37
        {
            "subtopic": "National Cooperative Development Corporation Act Year",
            "stem_en": "Under which Act of Parliament was the National Cooperative Development Corporation (NCDC) constituted?",
            "stem_ta": "எந்த நாடாளுமன்றச் சட்டத்தின் கீழ் தேசிய கூட்டுறவு மேம்பாட்டுக் கழகம் (NCDC) அமைக்கப்பட்டது?",
            "options": [
                ("National Cooperative Development Corporation Act, 1962", "தேசிய கூட்டுறவு மேம்பாட்டுக் கழகச் சட்டம், 1962"),
                ("Multi-State Co-operative Societies Act, 2002", "பல மாநில கூட்டுறவு சங்கங்கள் சட்டம், 2002"),
                ("Co-operative Societies Act, 1912", "கூட்டுறவு சங்கங்கள் சட்டம், 1912"),
                ("Banking Regulation Act, 1949", "வங்கி ஒழுங்குமுறைச் சட்டம், 1949")
            ],
            "correct_key": "A",
            "exp_en": "NCDC is a statutory corporation established under the National Cooperative Development Corporation Act, 1962 (Act No. 26 of 1962), coming into force in March 1963.",
            "exp_ta": "NCDC என்பது 1962-ஆம் ஆண்டின் தேசிய கூட்டுறவு மேம்பாட்டுக் கழகச் சட்டத்தின் (சட்டம் 26/1962) கீழ் மார்ச் 1963-ல் அமைக்கப்பட்ட சட்டப்பூர்வ கழகமாகும்.",
            "why_a_en": "Correct. NCDC Act, 1962 is the governing statute.",
            "why_a_ta": "சரி. NCDC சட்டம் 1962 என்பதே இதன் சட்டப்பூர்வ ஆதாரமாகும்.",
            "why_b_en": "Incorrect. MSCS Act governs multi-state cooperatives, not NCDC.",
            "why_b_ta": "தவறு. MSCS சட்டம் பல மாநில சங்கங்களை நிர்வகிக்கிறது.",
            "why_c_en": "Incorrect. 1912 Act is a general colonial law.",
            "why_c_ta": "தவறு. 1912 சட்டம் பொதுவானது.",
            "why_d_en": "Incorrect. BR Act governs banks, not NCDC.",
            "why_d_ta": "தவறு. வங்கிச் சட்டம் வங்கிகளை மட்டுமே நிர்வகிக்கிறது.",
            "tip_en": "NCDC Act passed in 1962; Corporation set up in 1963.",
            "tip_ta": "NCDC சட்டம் 1962-ல் இயற்றப்பட்டு, 1963-ல் கழகம் அமைக்கப்பட்டது.",
            "fact_en": "NCDC has disbursed over ₹2 lakh crore in financial assistance to cooperatives since inception.",
            "fact_ta": "தொடங்கப்பட்டதிலிருந்து கூட்டுறவுகளுக்கு ₹2 லட்சம் கோடிக்கும் அதிகமான நிதி உதவிகளை NCDC வழங்கியுள்ளது."
        },

        # GT 38
        {
            "subtopic": "Raiffeisen Model Characteristics",
            "stem_en": "The Raiffeisen model of agricultural credit, which inspired Sir Frederick Nicholson's 1895 report, was characterized primarily by:",
            "stem_ta": "சர் பிரடெரிக் நிக்கல்சனின் 1895 அறிக்கைக்கு உத்வேகமளித்த ரைஃபெய்சன் விவசாய கடன் மாதிரியின் முதன்மைப் பண்பு என்ன?",
            "options": [
                ("Unlimited liability, small local area of operation, honorary management, and mutual supervision", "வரையறுக்கப்படாத பொறுப்பு, சிறிய உள்ளூர் செயல்பாட்டு எல்லை, ஊதியமற்ற மேலாண்மை மற்றும் பரஸ்பரக் கண்காணிப்பு"),
                ("Limited liability and capital-based dividend distribution", "வரையறுக்கப்பட்ட பொறுப்பு மற்றும் மூலதன அடிப்படையிலான ஈவுத்தொகை பங்கீடு"),
                ("Complete ownership and staffing by the central imperial bank", "மத்திய இம்பீரியல் வங்கியின் முழு உரிமை மற்றும் ஊழியர் மேலாண்மை"),
                ("Exclusion of small and marginal farmers", "சிறு மற்றும் குறு விவசாயிகளை விலக்கி வைத்தல்")
            ],
            "correct_key": "A",
            "exp_en": "Friedrich Wilhelm Raiffeisen's rural credit unions in 19th-century Germany operated on unlimited liability, restricted village-level operation, voluntary/honorary management, and mutual surveillance, ensuring high credit discipline.",
            "exp_ta": "19-ஆம் நூற்றாண்டு ஜெர்மனியில் ரைஃபெய்சன் உருவாக்கிய கிராம கடன் சங்கங்கள் வரையறுக்கப்படாத பொறுப்பு, கிராம எல்லை, ஊதியமற்ற சேவை மற்றும் பரஸ்பர கண்காணிப்பு ஆகியவற்றின் அடிப்படையில் இயங்கின.",
            "why_a_en": "Correct. Unlimited liability and mutual local trust were the pillars of Raiffeisen societies.",
            "why_a_ta": "சரி. வரையறுக்கப்படாத பொறுப்பும் பரஸ்பர நம்பிக்கையுமே ரைஃபெய்சன் சங்கங்களின் தூண்களாகும்.",
            "why_b_en": "Incorrect. Limited liability characterized urban Schulze-Delitzsch banks.",
            "why_b_ta": "தவறு. வரையறுக்கப்பட்ட பொறுப்பு ஷூல்ஸ்-டெலிட்ஸ் நகர்ப்புற வங்கிகளின் பண்பு.",
            "why_c_en": "Incorrect. Raiffeisen cooperatives were strictly community-owned.",
            "why_c_ta": "தவறு. அவை சமூகத்தால் சொந்தமாக நடத்தப்பட்டன.",
            "why_d_en": "Incorrect. Designed specifically to rescue indebted small farmers.",
            "why_d_ta": "தவறு. சிறு விவசாயிகளை மீட்கவே அவை தொடங்கப்பட்டன.",
            "tip_en": "German Cooperative Pioneers: Raiffeisen = Rural (Unlimited liability); Schulze-Delitzsch = Urban (Limited liability).",
            "tip_ta": "ஜெர்மன் முன்னோடிகள்: ரைஃபெய்சன் = கிராமப்புறம் (வரையறுக்கப்படாத பொறுப்பு); ஷூல்ஸ் = நகர்ப்புறம் (வரையறுக்கப்பட்ட பொறுப்பு).",
            "fact_en": "Nicholson famously concluded his report with the words: 'Find Raiffeisen'.",
            "fact_ta": "நிக்கல்சன் தனது அறிக்கையை 'ரைஃபெய்சனைக் கண்டறியுங்கள்' என்ற வரலாற்று வாசகத்துடன் முடித்தார்."
        },

        # GT 39
        {
            "subtopic": "Tamil Nadu PDS - Ration Shop Operations",
            "stem_en": "In Tamil Nadu, what percentage of all Fair Price Shops under the Public Distribution System (PDS) are run by cooperative societies?",
            "stem_ta": "தமிழ்நாட்டில், பொது விநியோகத் திட்டத்தின் (PDS) கீழ் உள்ள மொத்த நியாயவிலைக் கடைகளில் எத்தனை சதவீதம் கூட்டுறவு சங்கங்களால் நடத்தப்படுகின்றன?",
            "options": [
                ("Approximately 93% to 95%", "சுமார் 93% முதல் 95% வரை"),
                ("About 25% only", "சுமார் 25% மட்டுமே"),
                ("Exactly 50%", "சரியாக 50%"),
                ("Less than 10%", "10%-க்கும் குறைவாக")
            ],
            "correct_key": "A",
            "exp_en": "Out of approximately 35,000 Fair Price Shops in Tamil Nadu, over 93% (~32,500 shops) are run by cooperatives (PACS, Consumer Cooperatives, and Women Cooperatives), with the remainder run by TNCSC and women SHGs.",
            "exp_ta": "தமிழ்நாட்டில் உள்ள சுமார் 35,000 நியாயவிலைக் கடைகளில் 93%-க்கும் அதிகமானவை (~32,500 கடைகள்) கூட்டுறவு சங்கங்களால் நடத்தப்படுகின்றன; மீதமுள்ளவை TNCSC மற்றும் மகளிர் சுயஉதவிக் குழுக்களால் நடத்தப்படுகின்றன.",
            "why_a_en": "Correct. Over 93% of PDS shops in TN are operated by cooperatives.",
            "why_a_ta": "சரி. தமிழ்நாட்டில் 93%-க்கும் அதிகமான ரேஷன் கடைகள் கூட்டுறவு சங்கங்களால் நடத்தப்படுகின்றன.",
            "why_b_en": "Incorrect. Far too low.",
            "why_b_ta": "தவறு. மிகவும் குறைவான மதிப்பீடு.",
            "why_c_en": "Incorrect. Cooperatives dominate far beyond 50%.",
            "why_c_ta": "தவறு. கூட்டுறவு சங்கங்களின் பங்கு 50%-க்கும் அதிகம்.",
            "why_d_en": "Incorrect. Private traders do not run PDS in TN.",
            "why_d_ta": "தவறு. தமிழ்நாட்டில் தனியார் வியாபாரிகளுக்கு அனுமதி இல்லை.",
            "tip_en": "Tamil Nadu PDS Strength: Zero private dealers; run almost entirely by Cooperatives (PACS/Consumer stores).",
            "tip_ta": "தமிழக PDS பலம்: தனியார் இடைத்தரகர்கள் பூஜ்ஜியம்; முழுமையாக கூட்டுறவு சங்கங்களால் நடத்தப்படுகிறது.",
            "fact_en": "The Tamil Nadu Civil Supplies Corporation (TNCSC) operates roughly 4% of shops in specific locations.",
            "fact_ta": "தமிழ்நாடு நுகர்பொருள் வாணிபக் கழகம் (TNCSC) சுமார் 4% கடைகளை நடத்துகிறது."
        },

        # GT 40
        {
            "subtopic": "Article 243ZN General Body Quorum and Audit Report",
            "stem_en": "Under Article 243ZN and Article 243ZM, what must be placed before the general body of every cooperative society at its annual general meeting?",
            "stem_ta": "உறுப்பு 243ZN மற்றும் 243ZM-ன் கீழ், ஒவ்வொரு கூட்டுறவு சங்கத்தின் வருடாந்திர பொதுக்குழு கூட்டத்தின் முன் கட்டாயமாக வைக்கப்பட வேண்டியது எது?",
            "options": [
                ("The audited statement of accounts and the audit report", "தணிக்கை செய்யப்பட்ட கணக்கு அறிக்கை மற்றும் தணிக்கை அறிக்கை"),
                ("Confidential surveillance files on dissident members", "எதிர்ப்புத் தெரிவிக்கும் உறுப்பினர்கள் மீதான ரகசியக் கண்காணிப்பு கோப்புகள்"),
                ("Tax assessment files of the District Collector", "மாவட்ட ஆட்சியரின் வரி மதிப்பீட்டுக் கோப்புகள்"),
                ("Directives of the Governor under Article 356", "உறுப்பு 356-ன் கீழ் ஆளுநரின் உத்தரவுகள்")
            ],
            "correct_key": "A",
            "exp_en": "Article 243ZM(2) mandates that the audit report of the accounts of a registered co-operative society must be placed before the annual general body meeting convened under Article 243ZN.",
            "exp_ta": "உறுப்பு 243ZM(2)-ன் படி, உறுப்பு 243ZN-ன் கீழ் கூட்டப்படும் வருடாந்திரப் பொதுக்குழு கூட்டத்தின் முன் சங்கத்தின் தணிக்கை அறிக்கை வைக்கப்பட வேண்டும்.",
            "why_a_en": "Correct. Audited statement and audit report are mandatory AGM agenda items.",
            "why_a_ta": "சரி. தணிக்கை அறிக்கையை பொதுக்குழுவில் சமர்ப்பிப்பது கட்டாய அரசமைப்பு விதியாகும்.",
            "why_b_en": "Incorrect. Outlandish distractor.",
            "why_b_ta": "தவறு. பொருந்தாத ஒன்று.",
            "why_c_en": "Incorrect. Collector's files are unrelated.",
            "why_c_ta": "தவறு. ஆட்சியர் கோப்புகள் தொடர்பற்றவை.",
            "why_d_en": "Incorrect. Article 356 deals with President's rule.",
            "why_d_ta": "தவறு. உறுப்பு 356 குடியரசுத் தலைவர் ஆட்சி பற்றியது.",
            "tip_en": "AGM Mandate: Convened within 6 months; Audited accounts must be tabled and approved by members.",
            "tip_ta": "பொதுக்குழு கட்டாயம்: 6 மாதங்களுக்குள் கூட்டப்பட வேண்டும்; தணிக்கை அறிக்கை உறுப்பினர்கள் முன் வைக்கப்பட வேண்டும்.",
            "fact_en": "Failure to place the audit report before the AGM violates Article 243ZM and constitutes an offence under 243ZQ.",
            "fact_ta": "தணிக்கை அறிக்கையை வைக்கத் தவறுவது உறுப்பு 243ZQ-ன் கீழ் தண்டனைக்குரிய குற்றமாகும்."
        },

        # GT 41
        {
            "subtopic": "Reserve Bank of India Act - Cooperative Credit",
            "stem_en": "Under Section 17 of the Reserve Bank of India Act, 1934, RBI provides concessional refinance assistance for rural and agricultural credit through which channel?",
            "stem_ta": "இந்திய ரிசர்வ் வங்கி சட்டம் 1934-ன் பிரிவு 17-ன் கீழ், கிராமப்புற மற்றும் விவசாயக் கடனுக்கான சலுகை மறுநிதியுதவியை ரிசர்வ் வங்கி எந்த வழித்தடத்தின் மூலம் வழங்குகிறது?",
            "options": [
                ("NABARD and State Co-operative Banks", "நபார்டு மற்றும் மாநிலக் கூட்டுறவு வங்கிகள் வழியாக"),
                ("Direct cash lending to individual farmers at branch counters", "வங்கி கவுண்ட்டர்களில் தனிநபர் விவசாயிகளுக்கு நேரடி பணக் கடன்"),
                ("Private foreign merchant banks", "தனியார் வெளிநாட்டு வணிக வங்கிகள் வழியாக"),
                ("Stock brokers and commodity exchanges", "பங்குத் தரகர்கள் மற்றும் கமாடிட்டி சந்தைகள் வழியாக")
            ],
            "correct_key": "A",
            "exp_en": "Under Section 17 of the RBI Act, the Reserve Bank provides short-term refinance to NABARD and State Co-operative Banks for seasonal agricultural operations (crop loans) and marketing.",
            "exp_ta": "ரிசர்வ் வங்கி சட்டத்தின் பிரிவு 17-ன் கீழ் பருவகால விவசாயக் கடன்களுக்காக நபார்டு மற்றும் மாநிலக் கூட்டுறவு வங்கிகளுக்கு ரிசர்வ் வங்கி சலுகை மறுநிதியுதவி வழங்குகிறது.",
            "why_a_en": "Correct. NABARD and StCBs are the statutory refinance conduits.",
            "why_a_ta": "சரி. நபார்டு மற்றும் மாநில கூட்டுறவு வங்கிகளே சட்டப்பூர்வ மறுநிதி வழித்தடங்கள்.",
            "why_b_en": "Incorrect. RBI does not engage in retail lending to individuals.",
            "why_b_ta": "தவறு. ரிசர்வ் வங்கி பொதுமக்களுக்கு நேரடியாக கடன் வழங்குவதில்லை.",
            "why_c_en": "Incorrect. Foreign merchant banks do not finance agricultural credit.",
            "why_c_ta": "தவறு. வெளிநாட்டு வணிக வங்கிகள் இதில் ஈடுபடுவதில்லை.",
            "why_d_en": "Incorrect. Commodity exchanges do not provide credit.",
            "why_d_ta": "தவறு. பங்குச் சந்தைகள் கடன் வழங்குவதில்லை.",
            "tip_en": "Refinance flow: RBI → NABARD → State Cooperative Bank → DCCB → PACS → Farmer.",
            "tip_ta": "மறுநிதி ஓட்டம்: RBI → நபார்டு → மாநிலக் கூட்டுறவு வங்கி → DCCB → PACS → விவசாயி.",
            "fact_en": "Refinance rates for crop loans are subsidized under the Central Government's Interest Subvention Scheme.",
            "fact_ta": "பயிர்க்கடன்களுக்கான மறுநிதி விகிதங்கள் மத்திய அரசின் வட்டி மானியத் திட்டத்தின் கீழ் மானியப்படுத்தப்படுகின்றன."
        },

        # GT 42
        {
            "subtopic": "Producer Companies Board Composition",
            "stem_en": "Under the Companies Act, what is the minimum and maximum number of directors prescribed for a Producer Company?",
            "stem_ta": "நிறுவனங்கள் சட்டத்தின் கீழ், ஓர் உழவர் உற்பத்தியாளர் நிறுவனத்திற்கு (Producer Company) நிர்ணயிக்கப்பட்டுள்ள குறைந்தபட்ச மற்றும் அதிகபட்ச இயக்குநர்களின் எண்ணிக்கை என்ன?",
            "options": [
                ("Minimum 5 and maximum 15 directors", "குறைந்தபட்சம் 5 மற்றும் அதிகபட்சம் 15 இயக்குநர்கள்"),
                ("Minimum 2 and maximum 7 directors", "குறைந்தபட்சம் 2 மற்றும் அதிகபட்சம் 7 இயக்குநர்கள்"),
                ("Minimum 3 and maximum 21 directors", "குறைந்தபட்சம் 3 மற்றும் அதிகபட்சம் 21 இயக்குநர்கள்"),
                ("Minimum 7 and maximum 50 directors", "குறைந்தபட்சம் 7 மற்றும் அதிகபட்சம் 50 இயக்குநர்கள்")
            ],
            "correct_key": "A",
            "exp_en": "Under Section 378N of the Companies Act, 2013 (formerly Section 581O of Companies Act 1956), every Producer Company must have at least 5 directors and not more than 15 directors.",
            "exp_ta": "நிறுவனங்கள் சட்டம் 2013-ன் பிரிவு 378N-ன் படி, ஒவ்வொரு உற்பத்தியாளர் நிறுவனமும் குறைந்தபட்சம் 5 இயக்குநர்களையும், அதிகபட்சம் 15 இயக்குநர்களையும் கொண்டிருக்க வேண்டும்.",
            "why_a_en": "Correct. Minimum 5 and maximum 15 directors.",
            "why_a_ta": "சரி. குறைந்தபட்சம் 5 மற்றும் அதிகபட்சம் 15 இயக்குநர்கள்.",
            "why_b_en": "Incorrect. 2 is for private companies.",
            "why_b_ta": "தவறு. 2 என்பது சாதாரண தனியார் நிறுவனங்களுக்கு.",
            "why_c_en": "Incorrect. 21 is the ceiling for cooperative boards under Article 243ZJ, not Producer Companies.",
            "why_c_ta": "தவறு. 21 என்பது பகுதி IX-B கூட்டுறவு சங்கங்களுக்கான வரம்பு.",
            "why_d_en": "Incorrect. Far too high.",
            "why_d_ta": "தவறு. தவறான எண்ணிக்கை.",
            "tip_en": "Directors Ceilings: Cooperative Society (Art 243ZJ) = Max 21; Producer Company (Companies Act) = Min 5, Max 15.",
            "tip_ta": "இயக்குநர் உச்சவரம்பு: கூட்டுறவு சங்கம் = அதிகபட்சம் 21; உற்பத்தியாளர் நிறுவனம் = குறைந்தபட்சம் 5, அதிகபட்சம் 15.",
            "fact_en": "A Producer Company with more than 15 directors can be permitted only by a special resolution of its members.",
            "fact_ta": "15-க்கும் மேற்பட்ட இயக்குநர்களை நியமிக்க பொதுக்குழுவின் சிறப்புத் தீர்மானம் தேவை."
        },

        # GT 43
        {
            "subtopic": "National Cooperative Training Institute",
            "stem_en": "The premier national institute for research and training in cooperative management, VAMNICOM, is situated in:",
            "stem_ta": "கூட்டுறவு மேலாண்மையில் ஆராய்ச்சி மற்றும் பயிற்சிக்கான முதன்மை தேசிய நிறுவனமான VAMNICOM எந்த நகரில் அமைந்துள்ளது?",
            "options": [
                ("Pune (Maharashtra)", "புனே (மகாராஷ்டிரா)"),
                ("New Delhi", "புது தில்லி"),
                ("Nagpur (Maharashtra)", "நாக்பூர் (மகாராஷ்டிரா)"),
                ("Hyderabad (Telangana)", "ஹைதராபாத் (தெலுங்கானா)")
            ],
            "correct_key": "A",
            "exp_en": "Vaikunth Mehta National Institute of Cooperative Management (VAMNICOM) is located in Pune, Maharashtra, functioning under the National Council for Cooperative Training (NCCT).",
            "exp_ta": "வைகுந்த் மேத்தா தேசிய கூட்டுறவு மேலாண்மை நிறுவனம் (VAMNICOM) மகாராஷ்டிராவின் புனே நகரில் அமைந்துள்ளது.",
            "why_a_en": "Correct. Pune is the home of VAMNICOM.",
            "why_a_ta": "சரி. VAMNICOM புனேயில் அமைந்துள்ளது.",
            "why_b_en": "Incorrect. New Delhi houses NCUI and NCDC.",
            "why_b_ta": "தவறு. புது தில்லியில் NCUI மற்றும் NCDC உள்ளன.",
            "why_c_en": "Incorrect. Not Nagpur.",
            "why_c_ta": "தவறு. நாக்பூர் அல்ல.",
            "why_d_en": "Incorrect. Not Hyderabad.",
            "why_d_ta": "தவறு. ஹைதராபாத் அல்ல.",
            "tip_en": "VAMNICOM = Pune; NCCT = New Delhi; IRMA = Anand, Gujarat.",
            "tip_ta": "VAMNICOM = புனே; NCCT = புது தில்லி; IRMA = ஆனந்த், குஜராத்.",
            "fact_en": "VAMNICOM awards post-graduate diplomas in agri-business and cooperative management.",
            "fact_ta": "இன்நிறுவனம் வேளாண் வணிகம் மற்றும் கூட்டுறவு மேலாண்மையில் முதுகலை டிப்ளமோ பட்டங்களை வழங்குகிறது."
        },

        # GT 44
        {
            "subtopic": "Primary Weavers Societies in Tamil Nadu",
            "stem_en": "In Tamil Nadu, the apex organization Co-optex functions under the administrative control of which department?",
            "stem_ta": "தமிழ்நாட்டில் உச்ச அமைப்பான கோ-ஆப்லெக்ஸ் எந்த அரசுத் துறையின் நிர்வாகக் கட்டுப்பாட்டின் கீழ் செயல்படுகிறது?",
            "options": [
                ("Department of Handlooms, Handicrafts, Textiles and Khadi", "கைத்தறி, கைவினைப் பொருட்கள், ஜவுளி மற்றும் கதர்த்துறை"),
                ("Department of Agriculture and Farmers Welfare", "வேளாண்மை மற்றும் விவசாயிகள் நலத்துறை"),
                ("Department of Industries and Commerce", "தொழில் மற்றும் வர்த்தகத்துறை"),
                ("Department of Rural Development and Panchayat Raj", "ஊரக வளர்ச்சி மற்றும் ஊராட்சித் துறை")
            ],
            "correct_key": "A",
            "exp_en": "Co-optex and all primary handloom weavers' cooperative societies in Tamil Nadu function under the administrative control of the Department of Handlooms, Handicrafts, Textiles and Khadi.",
            "exp_ta": "கோ-ஆப்லெக்ஸ் மற்றும் அனைத்து தொடக்க நெசவாளர் கூட்டுறவு சங்கங்களும் தமிழக கைத்தறி, கைவினைப் பொருட்கள், ஜவுளி மற்றும் கதர்த்து றையின் நிர்வாகக் கட்டுப்பாட்டில் இயங்குகின்றன.",
            "why_a_en": "Correct. Handlooms and Textiles Department is the administrative authority.",
            "why_a_ta": "சரி. கைத்தறி மற்றும் ஜவுளித் துறையே இதன் நிர்வாகத் துறையாகும்.",
            "why_b_en": "Incorrect. Agriculture handles crops and PACS.",
            "why_b_ta": "தவறு. வேளாண் துறை பயிர்களைக் கவனிக்கிறது.",
            "why_c_en": "Incorrect. Industries handles major corporations, not handloom coops.",
            "why_c_ta": "தவறு. தொழில்துறை பெருநிறுவனங்களைக் கவனிக்கிறது.",
            "why_d_en": "Incorrect. Rural Development handles Panchayats.",
            "why_d_ta": "தவறு. ஊரக வளர்ச்சித் துறை பஞ்சாயத்துகளைக் கவனிக்கிறது.",
            "tip_en": "Sectoral Administrative Departments in TN: Agricultural Coops = Co-operation Dept; Weavers Coops = Handlooms Dept; Milk Coops = Animal Husbandry & Dairying Dept.",
            "tip_ta": "தமிழக நிர்வாகத் துறைகள்: விவசாயக் கூட்டுறவு = கூட்டுறவுத் துறை; நெசவாளர் கூட்டுறவு = கைத்தறித் துறை; பால் கூட்டுறவு = கால்நடை பராமரிப்பு & பால்வளத் துறை.",
            "fact_en": "The Commissioner of Handlooms and Textiles exercises the powers of the Registrar for weaver cooperatives.",
            "fact_ta": "கைத்தறி மற்றும் ஜவுளித்துறை ஆணையர் நெசவாளர் கூட்டுறவு சங்கங்களுக்கான பதிவாளர் அதிகாரத்தைப் பெற்றுள்ளார்."
        },

        # GT 45
        {
            "subtopic": "Multi-State Co-operative Societies (Amendment) Act 2023 Provisions",
            "stem_en": "Under the Multi-State Co-operative Societies (Amendment) Act, 2023, who appoints the Co-operative Ombudsman?",
            "stem_ta": "பல மாநில கூட்டுறவு சங்கங்கள் (திருத்தச்) சட்டம் 2023-ன் கீழ், கூட்டுறவு குறைதீர்ப்பாளரை (Co-operative Ombudsman) நியமிப்பது யார்?",
            "options": [
                ("The Central Government", "மத்திய அரசு"),
                ("The Reserve Bank of India", "இந்திய ரிசர்வ் வங்கி"),
                ("The Chief Justice of India", "இந்தியத் தலைமை நீதிபதி"),
                ("The President of the Multi-State Co-operative Society", "பல மாநில கூட்டுறவு சங்கத்தின் தலைவர்")
            ],
            "correct_key": "A",
            "exp_en": "Under Section 85A inserted by the 2023 Amendment Act, the Central Government appoints one or more Co-operative Ombudsmen with specified territorial jurisdiction to inquire into member complaints regarding deposits, elections, or rights.",
            "exp_ta": "2023 திருத்தச் சட்டத்தின் பிரிவு 85A-ன் கீழ், உறுப்பினர்களின் புகார்களை விசாரிக்க ஒன்று அல்லது அதற்கு மேற்பட்ட கூட்டுறவு குறைதீர்ப்பாளர்களை மத்திய அரசே நியமிக்கிறது.",
            "why_a_en": "Correct. The Central Government appoints the Co-operative Ombudsman.",
            "why_a_ta": "சரி. மத்திய அரசே குறைதீர்ப்பாளரை நியமிக்கிறது.",
            "why_b_en": "Incorrect. RBI appoints Banking Ombudsman, not Cooperative Ombudsman.",
            "why_b_ta": "தவறு. ரிசர்வ் வங்கி வங்கி குறைதீர்ப்பாளரை நியமிக்கிறது.",
            "why_c_en": "Incorrect. CJI does not appoint administrative ombudsmen.",
            "why_c_ta": "தவறு. தலைமை நீதிபதி நியமிப்பதில்லை.",
            "why_d_en": "Incorrect. Societies cannot appoint their own ombudsman.",
            "why_d_ta": "தவறு. சங்கங்களே தனக்கான குறைதீர்ப்பாளரை நியமிக்க முடியாது.",
            "tip_en": "Ombudsman Framework: Appointed by Central Government; Free dispute resolution for individual cooperative members.",
            "tip_ta": "குறைதீர்ப்பாளர் அமைப்பு: மத்திய அரசால் நியமிக்கப்படுகிறார்; கூட்டுறவு உறுப்பினர்களுக்கு கட்டணமில்லா குறைதீர்ப்பு.",
            "fact_en": "The Ombudsman must complete inquiry and make recommendations within three months.",
            "fact_ta": "குறைதீர்ப்பாளர் மூன்று மாதங்களுக்குள் விசாரணையை முடித்துப் பரிந்துரைகளை வழங்க வேண்டும்."
        },

        # GT 46
        {
            "subtopic": "Primary Agricultural Credit Societies Computerization ERP",
            "stem_en": "What is the primary objective of introducing a Common ERP software in Primary Agricultural Credit Societies across India?",
            "stem_ta": "இந்தியா முழுவதும் உள்ள தொடக்க வேளாண் கடன் சங்கங்களில் பொதுவான ஈஆர்பி (ERP) மென்பொருளை அறிமுகப்படுத்துவதன் முதன்மை நோக்கம் என்ன?",
            "options": [
                ("To bring transparency, eliminate accounting manipulation, speed up loan disbursals, and seamlessly integrate PACS with DCCBs and NABARD", "கணக்கு முறைகேடுகளை ஒழித்து, வெளிப்படைத்தன்மையைக் கொண்டுவந்து, கடன் வழங்கலை விரைவுபடுத்தி, PACS சங்கங்களை DCCB மற்றும் நபார்டுடன் தடையின்றி இணைத்தல்"),
                ("To completely replace all human employees with artificial intelligence robots", "அனைத்து ஊழியர்களையும் நீக்கிவிட்டு செயற்கை நுண்ணறிவு ரோபோக்களை நியமித்தல்"),
                ("To transfer ownership of all rural land to the Union Government", "அனைத்து கிராமப்புற நிலங்களின் உரிமையையும் மத்திய அரசுக்கு மாற்றுதல்"),
                ("To shut down cooperative banks and merge them with foreign private banks", "கூட்டுறவு வங்கிகளை மூடிவிட்டு வெளிநாட்டு தனியார் வங்கிகளுடன் இணைத்தல்")
            ],
            "correct_key": "A",
            "exp_en": "The Cloud-based National PACS ERP software aims to establish standard financial accounting, end-to-end transparency, audited balance sheets, credit scoring, and direct API integration with DCCBs and StCBs.",
            "exp_ta": "தேசிய PACS மென்பொருள் பொதுவான கணக்கியல் தரம், வெளிப்படைத்தன்மை, விரைவான கடன் வழங்கல் மற்றும் மாவட்ட/மாநில வங்கிகளுடன் நேரடி இணைப்பை உருவாக்குவதை நோக்கமாகக் கொண்டுள்ளது.",
            "why_a_en": "Correct. Transparency, financial integrity, and integration with the cooperative banking pyramid are the core goals.",
            "why_a_ta": "சரி. வெளிப்படைத்தன்மை மற்றும் முறையான கணக்கு ஒருங்கிணைப்பே இதன் முக்கிய நோக்கமாகும்.",
            "why_b_en": "Incorrect. Absurd distractor.",
            "why_b_ta": "தவறு. பொருந்தாத ஒன்று.",
            "why_c_en": "Incorrect. Land ownership is completely unaffected.",
            "why_c_ta": "தவறு. நில உரிமை மாற்றப்படுவதில்லை.",
            "why_d_en": "Incorrect. It strengthens cooperative banks, does not shut them down.",
            "why_d_ta": "தவறு. கூட்டுறவு வங்கிகளை வலுப்படுத்துவதே இதன் நோக்கம்.",
            "tip_en": "ERP Benefits: Transparent balance sheets, audit trail, fraud prevention, instant KCC crop loan disbursal.",
            "tip_ta": "ஈஆர்பி பயன்கள்: வெளிப்படையான இருப்புநிலை அறிக்கை, மோசடி தடுப்பு, உடனடி கேசிசி பயிர்க்கடன் வழங்கல்.",
            "fact_en": "The software supports multiple regional languages including Tamil.",
            "fact_ta": "இம்மென்பொருள் தமிழ் உள்ளிட்ட பல்வேறு மாநில மொழிகளை ஆதரிக்கிறது."
        },

        # GT 47
        {
            "subtopic": "Article 43B Classification",
            "stem_en": "Article 43B of the Constitution of India, which promotes voluntary formation and democratic functioning of cooperative societies, is classified under which philosophical stream of Directive Principles?",
            "stem_ta": "கூட்டுறவு சங்கங்களின் தன்னார்வ உருவாக்கம் மற்றும் ஜனநாயக செயல்பாட்டை ஊக்குவிக்கும் இந்திய அரசியலமைப்பின் உறுப்பு 43B, வழிகாட்டு நெறிமுறைகளின் எந்த தத்துவார்த்தப் பிரிவின் கீழ் வகைப்படுத்தப்படுகிறது?",
            "options": [
                ("Gandhian and Liberal-Intellectual Principles", "காந்திய மற்றும் தாராளவாத-அறிவுசார் நெறிமுறைகள்"),
                ("Socialist Principles only", "சமதர்ம நெறிமுறைகள் மட்டுமே"),
                ("International Law Principles only", "சர்வதேச சட்ட நெறிமுறைகள் மட்டுமே"),
                ("Western Capitalist Principles", "மேற்கத்திய முதலாளித்துவ நெறிமுறைகள்")
            ],
            "correct_key": "A",
            "exp_en": "Promotion of village self-reliance and cooperatives reflects Mahatma Gandhi's swaraj philosophy (Gandhian stream), while professional management and autonomous institutions reflect the Liberal-Intellectual stream.",
            "exp_ta": "கூட்டுறவு மூலம் கிராமப்புற தற்சார்பை உருவாக்குவது காந்தியக் கொள்கையாகும்; தொழில்முறை மேலாண்மை மற்றும் தன்னாட்சி அமைப்புகளை உருவாக்குவது தாராளவாத-அறிவுசார் கொள்கையாகும்.",
            "why_a_en": "Correct. Article 43B blends Gandhian grassroots ideals with modern liberal management principles.",
            "why_a_ta": "சரி. உறுப்பு 43B காந்திய தத்துவத்தையும் நவீன தாராளவாத மேலாண்மையையும் ஒருங்கிணைக்கிறது.",
            "why_b_en": "Incorrect. Not exclusively socialist.",
            "why_b_ta": "தவறு. சமதர்ம நெறிமுறை மட்டும் அல்ல.",
            "why_c_en": "Incorrect. International law is Article 51.",
            "why_c_ta": "தவறு. சர்வதேச சட்டம் உறுப்பு 51.",
            "why_d_en": "Incorrect. Cooperatives reject unbridled capitalism.",
            "why_d_ta": "தவறு. முதலாளித்துவத்திற்கு கூட்டுறவு எதிரானது.",
            "tip_en": "DPSP Classification: Gandhian (Arts 40, 43, 43B, 46, 47, 48); Socialist (Arts 38, 39, 39A, 41, 42, 43, 43A, 47); Liberal-Intellectual (Arts 44, 45, 48, 48A, 49, 50, 51).",
            "tip_ta": "நெறிமுறைகள் வகைப்பாடு: காந்தியக் கொள்கைகளில் உறுப்பு 43B முதன்மையானது.",
            "fact_en": "Article 43B is non-justiciable under Article 37 but fundamental in the governance of the country.",
            "fact_ta": "உறுப்பு 43B நீதிமன்றங்களால் நேரடியாகச் செயல்படுத்தப்பட முடியாது என்றாலும் நாட்டின் நிர்வாகத்தில் அடிப்படையானது."
        },

        # GT 48
        {
            "subtopic": "Tamil Nadu Universal PDS Distinctive Feature",
            "stem_en": "What fundamentally distinguishes the Public Distribution System in Tamil Nadu from the Targeted PDS (TPDS) model implemented in most other Indian states?",
            "stem_ta": "இந்தியாவின் பெரும்பாலான பிற மாநிலங்களில் செயல்படுத்தப்படும் இலக்கு அடிப்படையிலான பொது விநியோகத் திட்டத்திலிருந்து (TPDS) தமிழ்நாட்டின் பொது விநியோகத் திட்டத்தை அடிப்படையில் வேறுபடுத்துவது எது?",
            "options": [
                ("Universal coverage: all resident families are entitled to subsidized foodgrains without poverty-line exclusion", "அனைவருக்குமான முறை: வறுமைக் கோடு பாகுபாடின்றி அனைத்துக் குடும்பங்களுக்கும் மானிய விலை உணவு தானியங்கள் வழங்கப்படுதல்"),
                ("Foodgrains are sold only to families holding passport and government employment", "பாஸ்போர்ட் மற்றும் அரசு வேலை உள்ள குடும்பங்களுக்கு மட்டுமே உணவு தானியங்கள் விற்கப்படுதல்"),
                ("Only cash transfers are given without any physical grain distribution", "உணவு தானியங்களுக்குப் பதிலாக பணப் பரிமாற்றம் மட்டுமே செய்யப்படுதல்"),
                ("Ration shops are owned and staffed directly by foreign multinational companies", "நியாயவிலைக் கடைகள் வெளிநாட்டு பன்னாட்டு நிறுவனங்களால் நடத்தப்படுதல்")
            ],
            "correct_key": "A",
            "exp_en": "Unlike TPDS which restricts subsidized grain to Below Poverty Line (BPL) families, Tamil Nadu resolutely maintained a Universal PDS where rice is provided free or at nominal rates to all cardholders without means-testing exclusions.",
            "exp_ta": "மற்ற மாநிலங்கள் வறுமைக் கோட்டிற்கு கீழ் உள்ளவர்களுக்கு (BPL) மட்டுமே மானியம் வழங்கும் போது, தமிழ்நாட்டில் அனைவருக்கும் பொதுவான முறை மூலம் அனைத்துக் குடும்ப அட்டைதாரர்களுக்கும் இலவச அரிசி வழங்கப்படுகிறது.",
            "why_a_en": "Correct. Universal entitlement without exclusion errors is Tamil Nadu's hallmark.",
            "why_a_ta": "சரி. பாகுபாடற்ற அனைவருக்கும் பொதுவான உணவுப் பாதுகாப்பே தமிழ்நாட்டின் தனிச்சிறப்பாகும்.",
            "why_b_en": "Incorrect. Absurd exclusionary distractor.",
            "why_b_ta": "தவறு. பொருந்தாத ஒன்று.",
            "why_c_en": "Incorrect. Tamil Nadu strongly opted for physical grain delivery over direct cash transfers.",
            "why_c_ta": "தவறு. தமிழ்நாடு நேரடி தானிய விநியோகத்தையே உறுதி செய்துள்ளது.",
            "why_d_en": "Incorrect. Cooperatives run the shops.",
            "why_d_ta": "தவறு. கூட்டுறவு சங்கங்களே கடைகளை நடத்துகின்றன.",
            "tip_en": "Tamil Nadu PDS Model: Universal (Universal entitlement) + Cooperative-run + Free Rice Scheme.",
            "tip_ta": "தமிழக PDS மாதிரி: அனைவருக்கும் உணவு + கூட்டுறவு நிர்வாகம் + இலவச அரிசி திட்டம்.",
            "fact_en": "Universal PDS was protected under Section 3(3) of the National Food Security Act, 2013.",
            "fact_ta": "2013 தேசிய உணவுப் பாதுகாப்புச் சட்டத்திலும் தமிழகத்தின் இந்த உலகளாவிய முறை பாதுகாக்கப்பட்டது."
        },

        # GT 49
        {
            "subtopic": "All India Co-operative Institutes Association 1929",
            "stem_en": "The All India Co-operative Institutes Association, established in 1929 under the presidency of Sir Lallubhai Samaldas, is today known as:",
            "stem_ta": "1829-ல் சர் லல்லுபாய் சமல்தாஸ் தலைமையில் நிறுவப்பட்ட அகில இந்திய கூட்டுறவு நிறுவனங்களின் சங்கம் இன்று எவ்வாறு அழைக்கப்படுகிறது?",
            "options": [
                ("National Cooperative Union of India (NCUI)", "இந்திய தேசிய கூட்டுறவு ஒன்றியம் (NCUI)"),
                ("NAFED", "நாஃபெட் (NAFED)"),
                ("NDDB", "என்.டி.டி.பி (NDDB)"),
                ("IFFCO", "இஃப்கோ (IFFCO)")
            ],
            "correct_key": "A",
            "exp_en": "Founded on 1 October 1929, the All India Co-operative Institutes Association was amalgamated with the Indian Provincial Co-operative Banks Association and renamed as the National Cooperative Union of India (NCUI) in 1961.",
            "exp_ta": "1929 அக்டோபர் 1 அன்று தொடங்கப்பட்ட அகில இந்திய கூட்டுறவு நிறுவனங்களின் சங்கம், 1961-ல் இந்திய தேசிய கூட்டுறவு ஒன்றியம் (NCUI) எனப் பெயர் மாற்றப்பட்டது.",
            "why_a_en": "Correct. NCUI is the successor body to the 1929 Association.",
            "why_a_ta": "சரி. NCUI என்பது 1929 அமைப்பின் தற்போதைய வடிவமாகும்.",
            "why_b_en": "Incorrect. NAFED was set up in 1958 for marketing.",
            "why_b_ta": "தவறு. NAFED 1958-ல் சந்தைப்படுத்துதலுக்காகத் தொடங்கப்பட்டது.",
            "why_c_en": "Incorrect. NDDB was set up in 1965 for dairy.",
            "why_c_ta": "தவறு. NDDB 1965-ல் பால்வளத்திற்காகத் தொடங்கப்பட்டது.",
            "why_d_en": "Incorrect. IFFCO was registered in 1967.",
            "why_d_ta": "தவறு. இஃப்கோ 1967-ல் உருவானது.",
            "tip_en": "NCUI: Apex non-governmental promotional body; Celebrates All India Cooperative Week annually (14-20 November).",
            "tip_ta": "NCUI: உச்ச அரசு சாரா கூட்டுறவு அமைப்பு; ஆண்டுதோறும் நவம்பர் 14-20 வரை தேசிய கூட்டுறவு வாரத்தைக் கொண்டாடுகிறது.",
            "fact_en": "All India Cooperative Week starts on 14th November (Jawaharlal Nehru's birthday) every year.",
            "fact_ta": "ஒவ்வொரு ஆண்டும் நவம்பர் 14 (நேரு பிறந்த நாள்) அன்று அகில இந்திய கூட்டுறவு வாரம் தொடங்குகிறது."
        },

        # GT 50
        {
            "subtopic": "Panchayati Raj vs Cooperatives Elections Comparison",
            "stem_en": "Compare the election machinery: Elections to Panchayats and Municipalities are conducted by the State Election Commission (SEC) under Articles 243K and 243ZA, whereas elections to Co-operative Societies are conducted by:",
            "stem_ta": "தேர்தல் அமைப்பை ஒப்பிடுக: பஞ்சாயத்துகள் மற்றும் நகராட்சிகளுக்கான தேர்தல்கள் உறுப்புகள் 243K மற்றும் 243ZA-ன் கீழ் மாநிலத் தேர்தல் ஆணையத்தால் (SEC) நடத்தப்படுகின்றன, ஆனால் கூட்டுறவு சங்கங்களுக்கான தேர்தல்கள் யாரால் நடத்தப்படுகின்றன?",
            "options": [
                ("Such independent authority or body as provided by the Legislature of a State by law", "மாநில சட்டமன்றம் சட்டத்தால் உருவாக்கும் ஒரு தனி அதிகார அமைப்பு அல்லது ஆணையத்தால்"),
                ("The Election Commission of India in New Delhi exclusively", "புது தில்லியில் உள்ள இந்தியத் தேர்தல் ஆணையத்தால் மட்டுமே"),
                ("The Union Ministry of Home Affairs", "மத்திய உள்துறை அமைச்சகத்தால்"),
                ("The Supreme Court Registry", "உச்சநீதிமன்றப் பதிவாளரால்")
            ],
            "correct_key": "A",
            "exp_en": "Unlike Panchayats and Municipalities where elections are constitutionally entrusted to the State Election Commission (SEC), Article 243ZK leaves the superintendence and conduct of cooperative elections to an authority designated by State law (e.g., TNSCSEC in Tamil Nadu).",
            "exp_ta": "பஞ்சாயத்து மற்றும் நகராட்சித் தேர்தல்கள் மாநிலத் தேர்தல் ஆணையத்திடம் ஒப்படைக்கப்பட்டுள்ள நிலையில், உறுப்பு 243ZK கூட்டுறவுத் தேர்தலை மாநிலச் சட்டமன்றம் சட்டத்தால் உருவாக்கும் தனி தேர்தல் அமைப்பிடம் ஒப்படைத்துள்ளது.",
            "why_a_en": "Correct. State Legislature creates a specialized cooperative election authority.",
            "why_a_ta": "சரி. மாநில சட்டமன்றம் இதற்காக தனி தேர்தல் அமைப்பை உருவாக்குகிறது.",
            "why_b_en": "Incorrect. ECI conducts national and state parliamentary elections.",
            "why_b_ta": "தவறு. ECI நாடாளுமன்றத் தேர்தல்களை மட்டுமே நடத்துகிறது.",
            "why_c_en": "Incorrect. Home Ministry has no election role.",
            "why_c_ta": "தவறு. உள்துறை அமைச்சகத்திற்கு தேர்தல் பங்கு இல்லை.",
            "why_d_en": "Incorrect. Judicial registries do not conduct elections.",
            "why_d_ta": "தவறு. நீதிமன்றங்கள் தேர்தலை நடத்துவதில்லை.",
            "tip_en": "Electoral Framework: Art 243K = Panchayats (SEC); Art 243ZA = Municipalities (SEC); Art 243ZK = Cooperatives (State-created Authority).",
            "tip_ta": "தேர்தல் விதி ஒப்பீடு: உறுப்பு 243K = பஞ்சாயத்துகள் (SEC); உறுப்பு 243ZA = நகராட்சிகள் (SEC); உறுப்பு 243ZK = கூட்டுறவுகள் (மாநில தேர்தல் அமைப்பு).",
            "fact_en": "In Tamil Nadu, the TNSCSEC conducts elections for over 24,000 cooperative societies.",
            "fact_ta": "தமிழ்நாட்டில் TNSCSEC அமைப்பு 24,000-க்கும் மேற்பட்ட கூட்டுறவு சங்கங்களுக்கு தேர்தல் நடத்துகிறது."
        }
    ]


def get_gt_batch1():
    return get_gt_batch1_raw() + get_gt_batch1_raw_part2()
