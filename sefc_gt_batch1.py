# -*- coding: utf-8 -*-
"""
State Election & Finance Commissions - Grand Test Batch 1 (Questions 1-50)
TNPSC Nova AI Content Engine
"""

def get_gt_batch1():
    return [
        # 1. Article 243K(1) Vesting Clause
        {
            "subtopic": "sec_constitutional_provisions",
            "stem_en": "In whom is the superintendence, direction, and control of the preparation of electoral rolls for, and the conduct of, all elections to the Panchayats constitutionally vested under Article 243K(1)?",
            "stem_ta": "சரத்து 243K(1)-ன் கீழ், ஊராட்சிகளுக்கான அனைத்துத் தேர்தல்களையும் நடத்துவதற்கும், வாக்காளர் பட்டியல்களைத் தயாரிப்பதற்கும் மேற்பார்வை, வழிகாட்டுதல் மற்றும் கட்டுப்படுத்தும் அதிகாரம் யாரிடம் அரசியலமைப்பு ரீதியாக வழங்கப்பட்டுள்ளது?",
            "options": [
                ("State Election Commission consisting of a State Election Commissioner", "மாநில தேர்தல் ஆணையரைக் கொண்ட மாநில தேர்தல் ஆணையம்"),
                ("Election Commission of India through the Chief Electoral Officer", "தலைமைத் தேர்தல் அதிகாரி வாயிலாக இந்தியத் தேர்தல் ஆணையம்"),
                ("State Panchayati Raj and Rural Development Department", "மாநில ஊராட்சி மற்றும் ஊரக வளர்ச்சித் துறை"),
                ("District Collector acting as District Election Officer", "மாவட்ட தேர்தல் அதிகாரியாக செயல்படும் மாவட்ட ஆட்சித்தலைவர்")
            ],
            "correct_key": "A",
            "exp_en": "Article 243K(1) explicitly states that the superintendence, direction, and control of the preparation of electoral rolls for, and the conduct of, all elections to the Panchayats shall be vested in a State Election Commission consisting of a State Election Commissioner to be appointed by the Governor.",
            "exp_ta": "சரத்து 243K(1)-ன் படி, ஊராட்சிகளுக்கான அனைத்துத் தேர்தல்களையும் நடத்துவதற்கும், வாக்காளர் பட்டியல்களைத் தயாரிப்பதற்கும் மேற்பார்வை, வழிகாட்டுதல் மற்றும் கட்டுப்படுத்தும் அதிகாரம், ஆளுநரால் நியமிக்கப்படும் மாநிலத் தேர்தல் ஆணையரைக் கொண்ட மாநிலத் தேர்தல் ஆணையத்திடம் ஒப்படைக்கப்பட்டுள்ளது.",
            "why_a_en": "Correct. Article 243K(1) vests all electoral authority for Panchayats in the State Election Commission.",
            "why_a_ta": "சரி. சரத்து 243K(1) ஊராட்சிகளுக்கான அனைத்துத் தேர்தல் அதிகாரத்தையும் மாநிலத் தேர்தல் ஆணையத்திடம் ஒப்படைக்கிறது.",
            "why_b_en": "Incorrect. Election Commission of India (Article 324) conducts Parliament and State Legislative elections, not local body elections.",
            "why_b_ta": "தவறு. இந்தியத் தேர்தல் ஆணையம் (சரத்து 324) பாராளுமன்றம் மற்றும் சட்டமன்றத் தேர்தல்களை நடத்துகிறது, உள்ளாட்சித் தேர்தல்களை அல்ல.",
            "why_c_en": "Incorrect. The Rural Development Department is an executive department, not the constitutional electoral authority.",
            "why_c_ta": "தவறு. ஊரக வளர்ச்சித் துறை என்பது ஒரு நிர்வாகத் துறையாகும், அரசியலமைப்பு தேர்தல் அதிகாரம் அல்ல.",
            "why_d_en": "Incorrect. District Collectors function under the superintendence of the State Election Commission during local polls.",
            "why_d_ta": "தவறு. உள்ளாட்சித் தேர்தலின் போது மாவட்ட ஆட்சித்தலைவர்கள் மாநிலத் தேர்தல் ஆணையத்தின் மேற்பார்வையின் கீழ் செயல்படுகின்றனர்.",
            "tip_en": "Remember: SEC handles Panchayats (243K) and Municipalities (243ZA).",
            "tip_ta": "நினைவில் கொள்க: மாநிலத் தேர்தல் ஆணையம் ஊராட்சிகளையும் (243K) நகராட்சிகளையும் (243ZA) கையாள்கிறது.",
            "fact_en": "Article 243K was inserted by the 73rd Constitutional Amendment Act, 1992.",
            "fact_ta": "சரத்து 243K 1992-ஆம் ஆண்டின் 73-வது அரசியலமைப்புத் திருத்தச் சட்டத்தால் சேர்க்கப்பட்டது."
        },

        # 2. Removal grounds of SEC
        {
            "subtopic": "sec_constitutional_provisions",
            "stem_en": "Under the proviso to Article 243K(2), on what grounds and through which procedure can the State Election Commissioner be removed from office?",
            "stem_ta": "சரத்து 243K(2)-ன் நிபந்தனைக் கூற்றின் கீழ், எந்தக் காரணங்களின் அடிப்படையிலும் எந்த நடைமுறையின் மூலமும் மாநிலத் தேர்தல் ஆணையரை பதவியிலிருந்து நீக்க முடியும்?",
            "options": [
                ("In like manner and on the like grounds as a Judge of a High Court", "உயர்நீதிமன்ற நீதிபதியை நீக்குவது போன்ற முறையிலும் அதே காரணங்களுக்காகவும்"),
                ("By the Governor at pleasure without assigning any reasons", "எந்த காரணமும் கூறாமல் ஆளுநரின் விருப்பப்படி"),
                ("By a simple majority resolution passed by the State Legislative Assembly", "மாநில சட்டமன்றப் பேரவையில் நிறைவேற்றப்படும் சாதாரண பெரும்பான்மை தீர்மானத்தின் மூலம்"),
                ("By the President of India on the advice of the Union Council of Ministers", "மத்திய அமைச்சரவையின் ஆலோசனையின் பேரில் இந்திய குடியரசுத் தலைவரால்")
            ],
            "correct_key": "A",
            "exp_en": "The proviso to Article 243K(2) mandates that the State Election Commissioner shall not be removed from office except in like manner and on the like grounds as a Judge of a High Court (i.e. proved misbehaviour or incapacity, backed by an address passed by each House of Parliament by a special majority).",
            "exp_ta": "சரத்து 243K(2)-ன் படி, உயர்நீதிமன்ற நீதிபதியை எந்த நடைமுறையிலும் காரணங்களுக்காகவும் நீக்க முடியுமோ (நிரூபிக்கப்பட்ட தவறான நடத்தை அல்லது திறமையின்மை, பாராளுமன்றத்தின் இரு அவைகளிலும் சிறப்புப் பெரும்பான்மை), அதே வழியில்தான் மாநிலத் தேர்தல் ஆணையரையும் நீக்க முடியும்.",
            "why_a_en": "Correct. The constitutional security of tenure matches that of a High Court Judge.",
            "why_a_ta": "சரி. அரசியலமைப்புப் பதவிப் பாதுகாப்பு உயர்நீதிமன்ற நீதிபதியுடன் ஒத்துள்ளது.",
            "why_b_en": "Incorrect. The Commissioner does NOT hold office during the pleasure of the Governor.",
            "why_b_ta": "தவறு. தேர்தல் ஆணையர் ஆளுநரின் விருப்பத்தின் பேரில் பதவியில் நீடிப்பதில்லை.",
            "why_c_en": "Incorrect. The State Legislature alone cannot remove the Commissioner by a simple resolution.",
            "why_c_ta": "தவறு. மாநில சட்டமன்றம் ஒரு சாதாரண தீர்மானத்தின் மூலம் ஆணையரை நீக்க முடியாது.",
            "why_d_en": "Incorrect. Removal requires parliamentary impeachment proceedings as applied to High Court judges under Article 217/124.",
            "why_d_ta": "தவறு. நீக்குதலுக்கு சரத்து 217/124-ன் கீழ் உயர்நீதிமன்ற நீதிபதிகளுக்குப் பொருந்தும் பாராளுமன்றக் கண்டன நடைமுறை தேவைப்படுகிறது.",
            "tip_en": "SEC tenure protection: Same as High Court Judge (same manner and grounds).",
            "tip_ta": "SEC பதவிப் பாதுகாப்பு: உயர்நீதிமன்ற நீதிபதிக்கு இணையானது (அதே முறை மற்றும் காரணங்கள்).",
            "fact_en": "Article 243K(2) ensures complete institutional insulation from state executive interference.",
            "fact_ta": "சரத்து 243K(2) மாநில நிர்வாகத்தின் தலையீட்டிலிருந்து முழுமையான நிறுவனப் பாதுகாப்பை உறுதி செய்கிறது."
        },

        # 3. Non-variation of service conditions to disadvantage
        {
            "subtopic": "sec_constitutional_provisions",
            "stem_en": "Which constitutional safeguard is provided to the State Election Commissioner regarding service conditions under Article 243K(2)?",
            "stem_ta": "சரத்து 243K(2)-ன் கீழ் மாநிலத் தேர்தல் ஆணையரின் பணிக் கால நிபந்தனைகள் தொடர்பாக வழங்கப்பட்டுள்ள அரசியலமைப்புப் பாதுகாப்பு எது?",
            "options": [
                ("Conditions of service shall not be varied to their disadvantage after appointment", "நியமனத்திற்குப் பிறகு அவரது பணிக்கால நிபந்தனைகள் அவருக்குப் பாதகமாக மாற்றப்படக்கூடாது"),
                ("Salary and allowances are determined annually by the Governor", "ஊதியம் மற்றும் படிகள் ஆளுநரால் ஆண்டுதோறும் நிர்ணயிக்கப்படும்"),
                ("Conditions of service can be altered at any time by an executive order of the Chief Minister", "முதலமைச்சரின் நிர்வாக உத்தரவின் மூலம் பணிக்கால நிபந்தனைகள் எந்த நேரத்திலும் மாற்றப்படலாம்"),
                ("The Commissioner is barred from any pensionary benefits after retirement", "ஓய்வுக்குப் பிறகு ஆணையருக்கு எந்தவொரு ஓய்வூதியப் பலன்களும் பெறத் தடை விதிக்கப்பட்டுள்ளது")
            ],
            "correct_key": "A",
            "exp_en": "Article 243K(2) second proviso clearly specifies: 'Provided further that the conditions of service of the State Election Commissioner shall not be varied to his disadvantage after his appointment.'",
            "exp_ta": "சரத்து 243K(2)-ன் இரண்டாவது நிபந்தனை, மாநிலத் தேர்தல் ஆணையரின் நியமனத்திற்குப் பிறகு அவரது பணிக்கால நிபந்தனைகள் அவருக்குப் பாதகமான வகையில் மாற்றப்படக் கூடாது என்பதைத் தெளிவாகக் குறிப்பிடுகிறது.",
            "why_a_en": "Correct. Article 243K(2) prevents adverse modification of service conditions after appointment.",
            "why_a_ta": "சரி. சரத்து 243K(2) நியமனத்திற்குப் பிறகு பணிக்கால நிபந்தனைகளை பாதகமாக மாற்றுவதைத் தடுக்கிறது.",
            "why_b_en": "Incorrect. Service conditions are governed by state law and cannot be unilaterally lowered annually.",
            "why_b_ta": "தவறு. பணிக்கால நிபந்தனைகள் மாநிலச் சட்டத்தால் நிர்வகிக்கப்படுகின்றன, ஆண்டுதோறும் குறைக்கப்பட முடியாது.",
            "why_c_en": "Incorrect. Executive orders cannot dilute constitutional guarantees.",
            "why_c_ta": "தவறு. நிர்வாக உத்தரவுகள் அரசியலமைப்பு உத்தரவாதங்களை நீர்த்துப்போகச் செய்ய முடியாது.",
            "why_d_en": "Incorrect. Commissioners are entitled to pension and post-retirement benefits as prescribed by law.",
            "why_d_ta": "தவறு. ஆணையர்கள் சட்டப்படி பரிந்துரைக்கப்பட்ட ஓய்வூதியம் மற்றும் ஓய்வூதிய பலன்களைப் பெற உரிமையுடையவர்கள்.",
            "tip_en": "Like Supreme Court and High Court Judges, SEC service conditions cannot be worsened after appointment.",
            "tip_ta": "உச்சநீதிமன்ற, உயர்நீதிமன்ற நீதிபதிகளைப் போலவே, SEC பணிக்கால நிபந்தனைகளை நியமனத்திற்குப் பிறகு குறைக்க முடியாது.",
            "fact_en": "This safeguard prevents the ruling party from using salary cuts to influence municipal and panchayat elections.",
            "fact_ta": "இந்த பாதுகாப்பு ஆளும் கட்சி உள்ளாட்சித் தேர்தல்களை பாதிக்கும் வகையில் ஊதியக் குறைப்புகளைப் பயன்படுத்துவதைத் தடுக்கிறது."
        },

        # 4. Article 243ZA and Municipalities
        {
            "subtopic": "sec_constitutional_provisions",
            "stem_en": "Which article of the Constitution of India mutatis mutandis extends the powers of the State Election Commission to elections of Municipalities?",
            "stem_ta": "இந்திய அரசியலமைப்பின் எந்த சரத்து மாநில தேர்தல் ஆணையத்தின் அதிகாரங்களை நகராட்சிகளின் தேர்தல்களுக்கும் அப்படியே விரிவுபடுத்துகிறது?",
            "options": [
                ("Article 243ZA", "சரத்து 243ZA"),
                ("Article 243ZG", "சரத்து 243ZG"),
                ("Article 243W", "சரத்து 243W"),
                ("Article 243S", "சரத்து 243S")
            ],
            "correct_key": "A",
            "exp_en": "Article 243ZA(1) provides that the superintendence, direction, and control of the preparation of electoral rolls for, and the conduct of, all elections to the Municipalities shall be vested in the State Election Commission referred to in Article 243K.",
            "exp_ta": "சரத்து 243ZA(1)-ன் படி, நகராட்சிகளுக்கான அனைத்துத் தேர்தல்களையும் நடத்துவதற்கும், வாக்காளர் பட்டியல்களைத் தயாரிப்பதற்கும் மேற்பார்வை, வழிகாட்டுதல் மற்றும் கட்டுப்படுத்தும் அதிகாரம் சரத்து 243K-ல் குறிப்பிடப்பட்டுள்ள மாநிலத் தேர்தல் ஆணையத்திடம் ஒப்படைக்கப்படும்.",
            "why_a_en": "Correct. Article 243ZA covers Municipal elections under the 74th Amendment.",
            "why_a_ta": "சரி. சரத்து 243ZA 74-வது திருத்தத்தின் கீழ் நகராட்சித் தேர்தல்களை உள்ளடக்கியுள்ளது.",
            "why_b_en": "Incorrect. Article 243ZG bars court interference in municipal electoral matters.",
            "why_b_ta": "தவறு. சரத்து 243ZG நகராட்சி தேர்தல் விவகாரங்களில் நீதிமன்ற தலையீட்டைத் தடை செய்கிறது.",
            "why_c_en": "Incorrect. Article 243W outlines the powers, authority, and responsibilities of Municipalities.",
            "why_c_ta": "தவறு. சரத்து 243W நகராட்சிகளின் அதிகாரங்கள் மற்றும் பொறுப்புகளைக் கூறுகிறது.",
            "why_d_en": "Incorrect. Article 243S deals with the constitution and composition of Wards Committees.",
            "why_d_ta": "தவறு. சரத்து 243S வார்டு குழுக்களின் அமைப்பு மற்றும் கலவையைக் கையாள்கிறது.",
            "tip_en": "Panchayat elections = 243K; Municipality elections = 243ZA.",
            "tip_ta": "ஊராட்சித் தேர்தல்கள் = 243K; நகராட்சித் தேர்தல்கள் = 243ZA.",
            "fact_en": "Both Articles 243K and 243ZA refer to the same single constitutional body in every state.",
            "fact_ta": "சரத்து 243K மற்றும் 243ZA ஆகிய இரண்டும் ஒவ்வொரு மாநிலத்திலும் உள்ள ஒரே அரசியலமைப்பு அமைப்பையே குறிக்கின்றன."
        },

        # 5. Staff requisition from Governor
        {
            "subtopic": "sec_constitutional_provisions",
            "stem_en": "When requested by the State Election Commission, who is constitutionally obligated under Article 243K(3) to make available staff for discharge of election duties?",
            "stem_ta": "மாநில தேர்தல் ஆணையம் கோரும் போது, தேர்தல் பணிகளை ஆற்றுவதற்கு தேவையான பணியாளர்களை வழங்க அரசியலமைப்பின் சரத்து 243K(3)-ன் கீழ் கடமைப்பட்டுள்ளவர் யார்?",
            "options": [
                ("The Governor of the State", "மாநில ஆளுநர்"),
                ("The Chief Election Commissioner of India", "இந்திய தலைமைத் தேர்தல் ஆணையர்"),
                ("The Chief Justice of the High Court", "உயர்நீதிமன்ற தலைமை நீதிபதி"),
                ("The Union Minister of Panchayati Raj", "மத்திய ஊராட்சித் துறை அமைச்சர்")
            ],
            "correct_key": "A",
            "exp_en": "Article 243K(3) mandates that the Governor of the State shall, when so requested by the State Election Commission, make available to the State Election Commission such staff as may be necessary for the discharge of the functions conferred on the Commission.",
            "exp_ta": "சரத்து 243K(3)-ன் படி, மாநிலத் தேர்தல் ஆணையம் அவ்வாறு கோரும் போது, ஆணைக்குழுவிற்கு ஒப்படைக்கப்பட்ட பணிகளை ஆற்றுவதற்குத் தேவையான பணியாளர்களை மாநில ஆளுநர் வழங்க வேண்டும்.",
            "why_a_en": "Correct. Article 243K(3) specifies the Governor of the State.",
            "why_a_ta": "சரி. சரத்து 243K(3) மாநில ஆளுநரைக் குறிப்பிடுகிறது.",
            "why_b_en": "Incorrect. ECI staff assistance is requested by CEC under Article 324(6) to the President/Governor, not for SEC.",
            "why_b_ta": "தவறு. இந்திய தேர்தல் ஆணையம் குடியரசுத் தலைவர்/ஆளுநரிடம் கேட்கிறது, SEC அல்ல.",
            "why_c_en": "Incorrect. Judiciary does not provide staff for conducting local elections.",
            "why_c_ta": "தவறு. உள்ளாட்சித் தேர்தல்களை நடத்துவதற்கு நீதித்துறை பணியாளர்களை வழங்குவதில்லை.",
            "why_d_en": "Incorrect. Union Ministry does not deploy state field staff for local elections.",
            "why_d_ta": "தவறு. மத்திய அமைச்சகம் உள்ளாட்சித் தேர்தல்களுக்கு மாநிலப் பணியாளர்களை நியமிப்பதில்லை.",
            "tip_en": "Article 243K(3) for Panchayats and 243ZA(2) for Municipalities place this obligation on the Governor.",
            "tip_ta": "சரத்து 243K(3) (ஊராட்சிகள்) மற்றும் 243ZA(2) (நகராட்சிகள்) இந்த கடமையை ஆளுநர் மீது சுமத்துகின்றன.",
            "fact_en": "Staff on election duty are deemed to be on deputation to the State Election Commission.",
            "fact_ta": "தேர்தல் பணியில் உள்ள ஊழியர்கள் மாநிலத் தேர்தல் ஆணையத்தின் அயற்பணியில் இருப்பதாகக் கருதப்படுகிறார்கள்."
        },

        # 6. Delimitation bar under 243-O(a) & 243ZG(a)
        {
            "subtopic": "sec_constitutional_provisions",
            "stem_en": "What is the constitutional effect of Article 243-O(a) and Article 243ZG(a) regarding the delimitation of constituencies for local bodies?",
            "stem_ta": "உள்ளாட்சி அமைப்புகளுக்கான தொகுதிகள் மறுசீரமைப்பு தொடர்பாக சரத்து 243-O(a) மற்றும் சரத்து 243ZG(a)-ன் அரசியலமைப்பு விளைவு என்ன?",
            "options": [
                ("The validity of any law relating to delimitation or allotment of seats cannot be called in question in any court", "தொகுதி மறுசீரமைப்பு அல்லது இட ஒதுக்கீடு தொடர்பான எந்தவொரு சட்டத்தின் செல்லுபடியாகும் தன்மையையும் எந்த நீதிமன்றத்திலும் கேள்வி கேட்க முடியாது"),
                ("Delimitation orders must be ratified by the Supreme Court before implementation", "மறுசீரமைப்பு உத்தரவுகள் அமல்படுத்தப்படுவதற்கு முன்பு உச்ச நீதிமன்றத்தால் அங்கீகரிக்கப்பட வேண்டும்"),
                ("Delimitation disputes are subject to direct appeal before the High Court within 30 days", "தொகுதி மறுசீரமைப்பு தகராறுகள் 30 நாட்களுக்குள் உயர் நீதிமன்றத்தில் நேரடி மேல்முறையீட்டிற்கு உட்பட்டவை"),
                ("Only the State Finance Commission can approve constituency boundary changes", "மாநில நிதி ஆணையத்தால் மட்டுமே தொகுதி எல்லை மாற்றங்களை அங்கீகரிக்க முடியும்")
            ],
            "correct_key": "A",
            "exp_en": "Articles 243-O(a) and 243ZG(a) create an express constitutional bar providing that the validity of any law relating to the delimitation of constituencies or the allotment of seats to such constituencies shall not be called in question in any court.",
            "exp_ta": "சரத்து 243-O(a) மற்றும் 243ZG(a) ஆகியவை தொகுதி மறுசீரமைப்பு அல்லது தொகுதிகளுக்கு இடங்கள் ஒதுக்கீடு செய்வது தொடர்பான எந்தவொரு சட்டத்தின் செல்லுபடியாகும் தன்மையையும் எந்தவொரு நீதிமன்றத்திலும் கேள்வி கேட்க முடியாது என்று வெளிப்படையான தடையை விதிக்கின்றன.",
            "why_a_en": "Correct. Both articles bar judicial questioning of delimitation laws to prevent election stalling.",
            "why_a_ta": "சரி. தேர்தல்கள் முடங்குவதைத் தடுக்க இரு சரத்துகளும் தொகுதி மறுசீரமைப்புச் சட்டங்களை நீதிமன்றத்தில் கேள்வி கேட்பதைத் தடை செய்கின்றன.",
            "why_b_en": "Incorrect. No ratification by the Supreme Court is required.",
            "why_b_ta": "தவறு. உச்ச நீதிமன்றத்தின் ஒப்புதல் தேவையில்லை.",
            "why_c_en": "Incorrect. The bar explicitly prevents calling delimitation in question.",
            "why_c_ta": "தவறு. மறுசீரமைப்பைக் கேள்வி கேட்பதை இந்த சரத்துகள் வெளிப்படையாகத் தடுக்கின்றன.",
            "why_d_en": "Incorrect. State Finance Commission has no role in delimitation.",
            "why_d_ta": "தவறு. மறுசீரமைப்பில் மாநில நிதி ஆணையத்திற்கு எந்தப் பங்கும் இல்லை.",
            "tip_en": "243-O applies to Panchayats, 243ZG applies to Municipalities.",
            "tip_ta": "243-O ஊராட்சிகளுக்கும், 243ZG நகராட்சிகளுக்கும் பொருந்தும்.",
            "fact_en": "This mirrors Article 329(a) which applies to Parliament and State Legislative delimitation.",
            "fact_ta": "இது பாராளுமன்றம் மற்றும் சட்டமன்ற தொகுதி மறுசீரமைப்புக்கு பொருந்தும் சரத்து 329(a)-ஐ ஒத்துள்ளது."
        },

        # 7. Bar on questioning elections except by election petition
        {
            "subtopic": "sec_constitutional_provisions",
            "stem_en": "According to Article 243-O(b) and Article 243ZG(b), how can an election to any Panchayat or Municipality be challenged?",
            "stem_ta": "சரத்து 243-O(b) மற்றும் சரத்து 243ZG(b)-ன் படி, எந்தவொரு ஊராட்சி அல்லது நகராட்சிக்கான தேர்தலை எவ்வாறு எதிர்க்க முடியும்?",
            "options": [
                ("Only by an election petition presented to such authority and in such manner as provided by State Legislature", "மாநில சட்டமன்றத்தால் வழங்கப்பட்ட அதிகாரியிடம் மற்றும் முறைப்படி தாக்கல் செய்யப்படும் தேர்தல் மனுவின் மூலம் மட்டுமே"),
                ("By filing an interlocutory writ petition in the Supreme Court before counting starts", "வாக்கு எண்ணிக்கை தொடங்குவதற்கு முன் உச்ச நீதிமன்றத்தில் இடைக்கால ரிட் மனு தாக்கல் செய்வதன் மூலம்"),
                ("By approaching the District Revenue Officer within 7 days of nomination", "வேட்புமனு தாக்கல் செய்த 7 நாட்களுக்குள் மாவட்ட வருவாய் அதிகாரியை அணுகுவதன் மூலம்"),
                ("By appealing directly to the Governor seeking annulment of the gazette notification", "அரசிதழ் அறிவிப்பை ரத்து செய்யக் கோரி நேரடியாக ஆளுநரிடம் முறையிடுவதன் மூலம்")
            ],
            "correct_key": "A",
            "exp_en": "Articles 243-O(b) and 243ZG(b) state that no election to any Panchayat or Municipality shall be called in question except by an election petition presented to such authority and in such manner as is provided for by or under any law made by the Legislature of a State.",
            "exp_ta": "சரத்து 243-O(b) மற்றும் 243ZG(b) ஆகியவற்றின்படி, மாநில சட்டமன்றத்தால் இயற்றப்பட்ட சட்டத்தின்படி தேர்தல் மனு தாக்கல் செய்வதன் மூலமேயன்றி, எந்தவொரு ஊராட்சி அல்லது நகராட்சித் தேர்தலையும் நீதிமன்றத்தில் கேள்வி கேட்க முடியாது.",
            "why_a_en": "Correct. An election petition under state law is the sole constitutional remedy.",
            "why_a_ta": "சரி. மாநிலச் சட்டத்தின் கீழ் தாக்கல் செய்யப்படும் தேர்தல் மனு மட்டுமே ஒரே அரசியலமைப்புத் தீர்வாகும்.",
            "why_b_en": "Incorrect. Writ petitions cannot interrupt the election process once initiated.",
            "why_b_ta": "தவறு. தேர்தல் செயல்முறை தொடங்கிய பின்னர் ரிட் மனுக்கள் அதைத் தடுக்க முடியாது.",
            "why_c_en": "Incorrect. DRO is not the sole constitutional election tribunal.",
            "why_c_ta": "தவறு. மாவட்ட வருவாய் அதிகாரி மட்டுமே தேர்தல் தீர்ப்பாயம் அல்ல.",
            "why_d_en": "Incorrect. The Governor has no jurisdiction to cancel elections via appeals.",
            "why_d_ta": "தவறு. மேல்முறையீடுகள் மூலம் தேர்தல்களை ரத்து செய்ய ஆளுநருக்கு அதிகார வரம்பு இல்லை.",
            "tip_en": "Once election notification is issued, courts do not interfere; challenges occur post-election via Election Petition.",
            "tip_ta": "தேர்தல் அறிவிப்பு வெளியான பிறகு நீதிமன்றங்கள் தலையிடாது; தேர்தல் மனு மூலம் தேர்தல் முடிந்த பிறகே சவால் செய்ய முடியும்.",
            "fact_en": "This principle ensures that local democratic transitions are completed within the mandated 5-year cycle.",
            "fact_ta": "இந்தக் கோட்பாடு உள்ளாட்சி ஜனநாயக மாற்றங்கள் 5 ஆண்டு காலத்திற்குள் முடிவடைவதை உறுதி செய்கிறது."
        },

        # 8. Kishan Singh Tomar Case 2006
        {
            "subtopic": "sec_powers_functions_elections",
            "stem_en": "In which landmark verdict did the Supreme Court hold that the powers of the State Election Commission are on par with those of the Election Commission of India under Article 324?",
            "stem_ta": "மாநிலத் தேர்தல் ஆணையத்தின் அதிகாரங்கள் சரத்து 324-ன் கீழ் உள்ள இந்தியத் தேர்தல் ஆணையத்தின் அதிகாரங்களுக்கு இணையானவை என்று உச்ச நீதிமன்றம் எந்த வரலாற்றுச் சிறப்புமிக்க தீர்ப்பில் கூறியது?",
            "options": [
                ("Kishan Singh Tomar v. Municipal Corporation of the City of Ahmedabad (2006)", "கிஷன் சிங் தோமர் எதிர் அகமதாபாத் மாநகராட்சி (2006)"),
                ("Mohinder Singh Gill v. Chief Election Commissioner (1978)", "மொஹிந்தர் சிங் கில் எதிர் தலைமை தேர்தல் ஆணையர் (1978)"),
                ("Indira Nehru Gandhi v. Raj Narain (1975)", "இந்திரா நேரு காந்தி எதிர் ராஜ் நாராயண் (1975)"),
                ("S.R. Bommai v. Union of India (1994)", "எஸ்.ஆர். பொம்மை எதிர் இந்திய யூனியன் (1994)")
            ],
            "correct_key": "A",
            "exp_en": "In Kishan Singh Tomar v. Municipal Corporation of the City of Ahmedabad (2006), a Constitution Bench of the Supreme Court held that the powers and status of the State Election Commission under Articles 243K and 243ZA are identical to those of the Election Commission of India under Article 324, and State Governments are bound to obey its directives.",
            "exp_ta": "கிஷன் சிங் தோமர் எதிர் அகமதாபாத் மாநகராட்சி (2006) வழக்கில், உச்ச நீதிமன்ற அரசியலமைப்பு அமர்வு, சரத்துகள் 243K மற்றும் 243ZA-ன் கீழ் மாநிலத் தேர்தல் ஆணையத்தின் அதிகாரங்களும் அந்தஸ்தும் சரத்து 324-ன் கீழ் உள்ள இந்தியத் தேர்தல் ஆணையத்திற்கு சமமானவை என்றும், மாநில அரசுகள் அதன் உத்தரவுகளுக்குக் கட்டுப்பட வேண்டும் என்றும் தீர்ப்பளித்தது.",
            "why_a_en": "Correct. Kishan Singh Tomar (2006) established constitutional parity between SEC and ECI.",
            "why_a_ta": "சரி. கிஷன் சிங் தோமர் (2006) தீர்ப்பு SEC மற்றும் ECI இடையே அரசியலமைப்புச் சமநிலையை நிறுவியது.",
            "why_b_en": "Incorrect. Mohinder Singh Gill (1978) dealt with ECI's plenary powers under Article 324.",
            "why_b_ta": "தவறு. மொஹிந்தர் சிங் கில் (1978) சரத்து 324-ன் கீழ் ECI-ன் முழுமையான அதிகாரங்களைக் கையாண்டது.",
            "why_c_en": "Incorrect. Indira Gandhi v. Raj Narain dealt with free and fair elections as a basic feature.",
            "why_c_ta": "தவறு. இந்திரா காந்தி எதிர் ராஜ் நாராயண் சுதந்திரமான தேர்தலை அடிப்படை அம்சமாகக் கையாண்டது.",
            "why_d_en": "Incorrect. S.R. Bommai dealt with Article 356 and federalism.",
            "why_d_ta": "தவறு. எஸ்.ஆர். பொம்மை சரத்து 356 மற்றும் கூட்டாட்சித் தத்துவத்தைக் கையாண்டது.",
            "tip_en": "Kishan Singh Tomar = SEC has same powers for local bodies as ECI has for Parliament/Assemblies.",
            "tip_ta": "கிஷன் சிங் தோமர் = பாராளுமன்றத்திற்கு ECI போன்றே, உள்ளாட்சிக்கு SEC-க்கும் சம அதிகாரம் உண்டு.",
            "fact_en": "The court ruled that State Governments cannot use administrative pretexts to delay five-yearly local body elections.",
            "fact_ta": "ஐந்தாண்டு உள்ளாட்சித் தேர்தல்களை தாமதப்படுத்த மாநில அரசுகள் நிர்வாகக் காரணங்களைக் கூற முடியாது என்று நீதிமன்றம் தீர்ப்பளித்தது."
        },

        # 9. 5-year duration mandate
        {
            "subtopic": "sec_powers_functions_elections",
            "stem_en": "Under Articles 243E and 243U, when must an election to constitute a Panchayat or Municipality be completed?",
            "stem_ta": "சரத்துகள் 243E மற்றும் 243U-ன் கீழ், ஒரு ஊராட்சி அல்லது நகராட்சியை அமைப்பதற்கான தேர்தல் எப்போது முடிக்கப்பட வேண்டும்?",
            "options": [
                ("Before the expiry of its duration of five years, or before six months from date of dissolution", "அதன் ஐந்தாண்டு காலம் முடிவடைவதற்கு முன்னதாக, அல்லது கலைக்கப்பட்ட தேதியிலிருந்து ஆறு மாதங்களுக்குள்"),
                ("Within one year after the completion of the five-year term", "ஐந்தாண்டு காலம் முடிந்த பிறகு ஒரு வருடத்திற்குள்"),
                ("Whenever the State Cabinet passes an executive resolution approving elections", "மாநில அமைச்சரவை தேர்தலுக்கு ஒப்புதல் அளித்து நிர்வாகத் தீர்மானம் நிறைவேற்றும் போதெல்லாம்"),
                ("Only after the Census figures of the preceding decade are published", "முந்தைய பத்தாண்டுகளின் மக்கள் தொகை கணக்கெடுப்பு புள்ளிவிவரங்கள் வெளியிடப்பட்ட பின்னரே"),
            ],
            "correct_key": "A",
            "exp_en": "Articles 243E(3) and 243U(3) mandate that an election to constitute a Panchayat or Municipality must be completed before the expiry of its 5-year duration, or in case of dissolution, before the expiration of a period of six months from the date of its dissolution.",
            "exp_ta": "சரத்துகள் 243E(3) மற்றும் 243U(3) ஆகியவற்றின்படி, ஒரு ஊராட்சி அல்லது நகராட்சியை உருவாக்குவதற்கான தேர்தல் அதன் 5 ஆண்டுகள் முடிவடைவதற்கு முன்னரோ, அல்லது கலைக்கப்பட்டால் கலைக்கப்பட்ட தேதியிலிருந்து ஆறு மாத காலத்திற்குள்ளோ முடிக்கப்பட வேண்டும்.",
            "why_a_en": "Correct. Constitution strictly mandates completion before term expiry or within 6 months of dissolution.",
            "why_a_ta": "சரி. பதவிக்காலம் முடிவதற்கு முன்போ அல்லது கலைக்கப்பட்ட 6 மாதங்களுக்குள்ளோ தேர்தல் முடிக்கப்பட வேண்டும் என்பது அரசியலமைப்பு கட்டாயமாகும்.",
            "why_b_en": "Incorrect. One-year gap is unconstitutional.",
            "why_b_ta": "தவறு. ஒரு வருட இடைவெளி அரசியலமைப்புக்கு முரணானது.",
            "why_c_en": "Incorrect. Cabinet resolutions cannot supersede the constitutional 5-year mandate.",
            "why_c_ta": "தவறு. அமைச்சரவைத் தீர்மானங்கள் அரசியலமைப்பின் 5 ஆண்டு ஆணையை மீற முடியாது.",
            "why_d_en": "Incorrect. Census delay cannot be used as an excuse to avoid constitutional timelines.",
            "why_d_ta": "தவறு. மக்கள் தொகை கணக்கெடுப்பு தாமதத்தை தேர்தல் தாமதத்திற்கு சாக்காகப் பயன்படுத்த முடியாது.",
            "tip_en": "Rule of 6 months: If remainder period is less than 6 months, election is held for a fresh 5-year term.",
            "tip_ta": "6 மாத விதி: மீதமுள்ள காலம் 6 மாதங்களுக்கும் குறைவாக இருந்தால், புதிய 5 ஆண்டு காலத்திற்கு தேர்தல் நடத்தப்படும்.",
            "fact_en": "Prior to 1992, state governments routinely superseded local bodies for decades without elections.",
            "fact_ta": "1992-க்கு முன், மாநில அரசுகள் உள்ளாட்சி அமைப்புகளை கலைத்துவிட்டு பல தசாப்தங்களாக தேர்தல் நடத்தாமல் இருந்தன."
        },

        # 10. Status of SEC
        {
            "subtopic": "sec_constitutional_provisions",
            "stem_en": "What judicial status and rank is accorded to the State Election Commissioner to safeguard independent functioning?",
            "stem_ta": "சுயேச்சையான செயல்பாட்டைப் பாதுகாக்க மாநிலத் தேர்தல் ஆணையருக்கு எந்த நீதித்துறை அந்தஸ்தும் பதவியும் வழங்கப்பட்டுள்ளது?",
            "options": [
                ("Rank and status equivalent to a Judge of a High Court", "உயர்நீதிமன்ற நீதிபதிக்கு இணையான தகுதியும் அந்தஸ்தும்"),
                ("Status equivalent to a District and Sessions Judge", "மாவட்ட மற்றும் அமர்வு நீதிபதிக்கு இணையான அந்தஸ்து"),
                ("Status equivalent to a Cabinet Minister of the State Government", "மாநில அரசின் கேபினட் அமைச்சருக்கு இணையான அந்தஸ்து"),
                ("Status of a Chief Secretary without judicial immunity", "நீதித்துறை விலக்களிக்கப்படாத தலைமைச் செயலாளரின் அந்தஸ்து")
            ],
            "correct_key": "A",
            "exp_en": "The State Election Commissioner is granted status, removal conditions, and tenure protections equivalent to a sitting Judge of a High Court under Article 243K(2).",
            "exp_ta": "சரத்து 243K(2)-ன் கீழ் மாநிலத் தேர்தல் ஆணையருக்கு உயர்நீதிமன்றத்தின் பதவியில் உள்ள நீதிபதிக்கு இணையான அந்தஸ்து, நீக்கும் முறை மற்றும் பதவிப் பாதுகாப்பு வழங்கப்பட்டுள்ளது.",
            "why_a_en": "Correct. Proviso to 243K(2) equates SEC removal and status with a High Court Judge.",
            "why_a_ta": "சரி. 243K(2)-ன் நிபந்தனை SEC நீக்கம் மற்றும் அந்தஸ்தை உயர்நீதிமன்ற நீதிபதியுடன் சமப்படுத்துகிறது.",
            "why_b_en": "Incorrect. SEC status is higher than a District Judge.",
            "why_b_ta": "தவறு. SEC அந்தஸ்து மாவட்ட நீதிபதியை விட உயர்ந்தது.",
            "why_c_en": "Incorrect. Equating with a Cabinet Minister would compromise non-partisan neutrality.",
            "why_c_ta": "தவறு. அமைச்சருக்கு சமமாக வைப்பது நடுநிலைமையை பாதிக்கும்.",
            "why_d_en": "Incorrect. SEC has judicial protection regarding removal, unlike civil servants.",
            "why_d_ta": "தவறு. அரசு ஊழியர்களைப் போலன்றி, SEC-க்கு நீதித்துறை நீக்கப் பாதுகாப்பு உள்ளது.",
            "tip_en": "Removal of SEC = High Court Judge removal procedure (Parliamentary address).",
            "tip_ta": "SEC நீக்கம் = உயர்நீதிமன்ற நீதிபதி நீக்க நடைமுறை (பாராளுமன்ற தீர்மானம்).",
            "fact_en": "This ensures the Commissioner cannot be pressured by the state bureaucracy or ruling political executive.",
            "fact_ta": "இது ஆணையர் மாநில அதிகார வர்க்கத்தாலோ அல்லது ஆளும் கட்சியினராலோ அச்சுறுத்தப்படுவதைத் தடுக்கிறது."
        },

        # 11. Tamil Nadu SEC establishment
        {
            "subtopic": "sec_powers_functions_elections",
            "stem_en": "In which year was the Tamil Nadu State Election Commission established as a statutory and constitutional body following the 73rd and 74th Amendments?",
            "stem_ta": "73 மற்றும் 74-வது திருத்தங்களைத் தொடர்ந்து தமிழ்நாட்டில் மாநிலத் தேர்தல் ஆணையம் எந்த ஆண்டில் நிறுவப்பட்டது?",
            "options": [
                ("1994", "1994"),
                ("1992", "1992"),
                ("1996", "1996"),
                ("2001", "2001")
            ],
            "correct_key": "A",
            "exp_en": "The Tamil Nadu State Election Commission was constituted in 1994 under the Tamil Nadu Panchayats Act, 1994, to conduct elections to rural and urban local bodies across the state.",
            "exp_ta": "மாநிலம் முழுவதும் உள்ள ஊரக மற்றும் நகர்ப்புற உள்ளாட்சி அமைப்புகளுக்கு தேர்தல்களை நடத்துவதற்காக, தமிழ்நாடு ஊராட்சிகள் சட்டம் 1994-ன் கீழ், 1994-ஆம் ஆண்டில் தமிழ்நாடு மாநிலத் தேர்தல் ஆணையம் அமைக்கப்பட்டது.",
            "why_a_en": "Correct. Established in 1994 after the passage of the TN Panchayats Act 1994.",
            "why_a_ta": "சரி. 1994-ல் தமிழ்நாடு ஊராட்சிகள் சட்டம் இயற்றப்பட்ட பின்னர் அமைக்கப்பட்டது.",
            "why_b_en": "Incorrect. 1992 was the year of parliamentary enactment of 73rd and 74th CAAs.",
            "why_b_ta": "தவறு. 1992 என்பது பாராளுமன்றத்தில் 73 மற்றும் 74-வது சட்டங்கள் இயற்றப்பட்ட ஆண்டு.",
            "why_c_en": "Incorrect. The first general local body elections in TN were held in October 1996, but SEC was established in 1994.",
            "why_c_ta": "தவறு. முதல் பொது உள்ளாட்சித் தேர்தல் அக்டோபர் 1996-ல் நடைபெற்றது, ஆனால் ஆணையம் 1994-ல் அமைக்கப்பட்டது.",
            "why_d_en": "Incorrect. 2001 was the year of the second ordinary local body elections.",
            "why_d_ta": "தவறு. 2001 என்பது இரண்டாவது சாதாரண உள்ளாட்சித் தேர்தல் நடைபெற்ற ஆண்டு.",
            "tip_en": "TN Panchayats Act was enacted in April 1994; TN SEC was set up in the same year.",
            "tip_ta": "தமிழ்நாடு ஊராட்சிகள் சட்டம் ஏப்ரல் 1994-ல் இயற்றப்பட்டது; அதே ஆண்டில் TN SEC அமைக்கப்பட்டது.",
            "fact_en": "The first ordinary elections to rural and urban local bodies in Tamil Nadu were conducted in October 1996.",
            "fact_ta": "தமிழ்நாட்டில் ஊரக மற்றும் நகர்ப்புற உள்ளாட்சி அமைப்புகளுக்கான முதல் சாதாரணத் தேர்தல்கள் அக்டோபர் 1996-ல் நடத்தப்பட்டன."
        },

        # 12. Location of TN SEC Headquarters
        {
            "subtopic": "sec_powers_functions_elections",
            "stem_en": "Where is the headquarters of the Tamil Nadu State Election Commission situated?",
            "stem_ta": "தமிழ்நாடு மாநிலத் தேர்தல் ஆணையத்தின் தலைமை அலுவலகம் எங்கு அமைந்துள்ளது?",
            "options": [
                ("Chennai (Koyambedu)", "சென்னை (கோயம்பேடு)"),
                ("Madurai (Tallakulam)", "மதுரை (தல்லாகுளம்)"),
                ("Coimbatore (Gandhipuram)", "கோயம்புத்தூர் (காந்திபுரம்)"),
                ("Tiruchirappalli (Thillai Nagar)", "திருச்சிராப்பள்ளி (தில்லை நகர்)")
            ],
            "correct_key": "A",
            "exp_en": "The Tamil Nadu State Election Commission is headquartered at Koyambedu, Chennai.",
            "exp_ta": "தமிழ்நாடு மாநிலத் தேர்தல் ஆணையத்தின் தலைமை அலுவலகம் சென்னை கோயம்பேட்டில் அமைந்துள்ளது.",
            "why_a_en": "Correct. TN SEC operates from its own office complex in Koyambedu, Chennai.",
            "why_a_ta": "சரி. TN SEC சென்னை கோயம்பேட்டில் உள்ள தனது சொந்த அலுவலக வளாகத்தில் செயல்படுகிறது.",
            "why_b_en": "Incorrect. Madurai hosts the High Court Bench, not the SEC headquarters.",
            "why_b_ta": "தவறு. மதுரையில் உயர்நீதிமன்ற கிளை உள்ளது, தேர்தல் ஆணையத் தலைமையகம் அல்ல.",
            "why_c_en": "Incorrect. Coimbatore does not house the state election headquarters.",
            "why_c_ta": "தவறு. கோயம்புத்தூரில் மாநிலத் தேர்தல் தலைமையகம் இல்லை.",
            "why_d_en": "Incorrect. Tiruchirappalli is not the headquarters location.",
            "why_d_ta": "தவறு. திருச்சிராப்பள்ளி தலைமையக இடம் அல்ல.",
            "tip_en": "TN SEC building is located on Inner Ring Road, Jai Nagar, Koyambedu, Chennai.",
            "tip_ta": "TN SEC கட்டிடம் சென்னை கோயம்பேடு உள்வட்டச் சாலையில் அமைந்துள்ளது.",
            "fact_en": "The Commission is headed by a retired senior IAS officer designated as State Election Commissioner.",
            "fact_ta": "இவ்வாணையம் ஓய்வுபெற்ற மூத்த IAS அதிகாரியான மாநிலத் தேர்தல் ஆணையரால் தலைமை தாங்கப்படுகிறது."
        },

        # 13. Single-member structure
        {
            "subtopic": "sec_constitutional_provisions",
            "stem_en": "Unlike the multi-member Election Commission of India, what is the default structural composition of the State Election Commission under Article 243K(1)?",
            "stem_ta": "பல உறுப்பினர்களைக் கொண்ட இந்தியத் தேர்தல் ஆணையத்தைப் போலன்றி, சரத்து 243K(1)-ன் கீழ் மாநிலத் தேர்தல் ஆணையத்தின் இயல்புநிலையான கட்டமைப்பு அமைப்பு என்ன?",
            "options": [
                ("A single-member body consisting of a State Election Commissioner", "ஒரு மாநில தேர்தல் ஆணையரைக் கொண்ட ஒரு நபர் அமைப்பு"),
                ("A mandatory three-member panel comprising a Chief Commissioner and two Commissioners", "ஒரு தலைமை ஆணையர் மற்றும் இரண்டு ஆணையர்களைக் கொண்ட கட்டாய மூன்று நபர் குழு"),
                ("A five-member commission chaired by the Chief Secretary", "தலைமைச் செயலாளர் தலைமையில் இயங்கும் ஐந்து பேர் கொண்ட ஆணையம்"),
                ("A collegium consisting of High Court retired judges", "உயர்நீதிமன்ற ஓய்வுபெற்ற நீதிபதிகளைக் கொண்ட கொலீஜியம்")
            ],
            "correct_key": "A",
            "exp_en": "Article 243K(1) provides for a State Election Commission 'consisting of a State Election Commissioner to be appointed by the Governor'. In almost all states, including Tamil Nadu, it functions as a single-member body.",
            "exp_ta": "சரத்து 243K(1) 'ஆளுநரால் நியமிக்கப்படும் மாநிலத் தேர்தல் ஆணையரைக் கொண்ட' மாநிலத் தேர்தல் ஆணையத்தை வழங்குகிறது. தமிழ்நாடு உட்பட பெரும்பாலான மாநிலங்களில், இது ஒரு நபர் அமைப்பாகச் செயல்படுகிறது.",
            "why_a_en": "Correct. The constitutional text provides for a State Election Commissioner (single-member).",
            "why_a_ta": "சரி. அரசியலமைப்பு உரை ஒரு மாநிலத் தேர்தல் ஆணையரை மட்டுமே குறிப்பிடுகிறது.",
            "why_b_en": "Incorrect. Multi-member structure is an ECI feature under Article 324, not mandated for SEC.",
            "why_b_ta": "தவறு. பல நபர் கட்டமைப்பு சரத்து 324-ன் கீழ் ECI-க்கு உரியது, SEC-க்கு கட்டாயமில்லை.",
            "why_c_en": "Incorrect. Chief Secretary cannot chair the constitutional election commission.",
            "why_c_ta": "தவறு. அரசியலமைப்பு தேர்தல் ஆணையத்திற்கு தலைமைச் செயலாளர் தலைமை தாங்க முடியாது.",
            "why_d_en": "Incorrect. No retired judge collegium is prescribed by the Constitution.",
            "why_d_ta": "தவறு. அரசியலமைப்பில் அத்தகைய கொலீஜியம் எதுவும் கூறப்படவில்லை.",
            "tip_en": "ECI = Chief Election Commissioner + 2 Election Commissioners (since 1993); SEC = Single State Election Commissioner in most states.",
            "tip_ta": "ECI = தலைமைத் தேர்தல் ஆணையர் + 2 தேர்தல் ஆணையர்கள்; SEC = பெரும்பாலான மாநிலங்களில் ஒற்றை ஆணையர்.",
            "fact_en": "The Commissioner is assisted by a Secretary and administrative officers drawn from the state civil service.",
            "fact_ta": "ஆணையருக்கு ஒரு செயலாளர் மற்றும் மாநில நிர்வாகப் பணியிலிருந்து பெறப்பட்ட அதிகாரிகள் உதவுகிறார்கள்."
        },

        # 14. Regulatory powers and Model Code
        {
            "subtopic": "sec_powers_functions_elections",
            "stem_en": "Which authority issues notifications fixing the dates, phases, and enforcement of the Model Code of Conduct for local body elections in a State?",
            "stem_ta": "ஒரு மாநிலத்தில் உள்ளாட்சித் தேர்தல்களுக்கான தேதிகள், கட்டங்கள் மற்றும் மாதிரி நடத்தை நெறிமுறைகளை அமல்படுத்துவதற்கான அறிவிப்புகளை வெளியிடும் அதிகாரம் எது?",
            "options": [
                ("State Election Commission", "மாநில தேர்தல் ஆணையம்"),
                ("State Legislative Assembly Secretariat", "மாநில சட்டப் பேரவைச் செயலகம்"),
                ("State Rural Development and Municipal Administration Ministry", "மாநில ஊரக வளர்ச்சி மற்றும் நகராட்சி நிர்வாக அமைச்சகம்"),
                ("Directorate of Local Fund Audit", "உள்ளாட்சி நிதித் தணிக்கை இயக்ககம்")
            ],
            "correct_key": "A",
            "exp_en": "The State Election Commission issues election notifications fixing the poll schedule, counting dates, and enforces the Model Code of Conduct across rural and urban local bodies.",
            "exp_ta": "மாநிலத் தேர்தல் ஆணையமே வாக்குப்பதிவு அட்டவணை, வாக்கு எண்ணிக்கை தேதிகள் ஆகியவற்றை நிர்ணயித்து தேர்தல் அறிவிப்புகளை வெளியிடுகிறது மற்றும் மாதிரி நடத்தை நெறிமுறைகளை நடைமுறைப்படுத்துகிறது.",
            "why_a_en": "Correct. SEC holds exclusive constitutional authority over election schedules and code enforcement.",
            "why_a_ta": "சரி. தேர்தல் அட்டவணை மற்றும் நடத்தை நெறிமுறைகள் மீது SEC பிரத்யேக அதிகாரம் கொண்டுள்ளது.",
            "why_b_en": "Incorrect. Legislative Secretariat has no role in conducting local polls.",
            "why_b_ta": "தவறு. உள்ளாட்சித் தேர்தல்களை நடத்துவதில் சட்டமன்றச் செயலகத்திற்கு எந்தப் பங்கும் இல்லை.",
            "why_c_en": "Incorrect. State Ministries must comply with SEC guidelines once elections are notified.",
            "why_c_ta": "தவறு. தேர்தல் அறிவிக்கப்பட்டவுடன் மாநில அமைச்சகங்கள் SEC வழிகாட்டுதல்களுக்குக் கட்டுப்பட வேண்டும்.",
            "why_d_en": "Incorrect. Local Fund Audit is an accounting audit body, not an election regulator.",
            "why_d_ta": "தவறு. உள்ளாட்சி நிதி தணிக்கை என்பது ஒரு தணிக்கை அமைப்பு, தேர்தல் கட்டுப்பாட்டாளர் அல்ல.",
            "tip_en": "State Government cannot dictate poll dates once SEC initiates the notification process.",
            "tip_ta": "SEC தேர்தல் அறிவிப்பைத் தொடங்கிய பிறகு தேர்தல் தேதிகளை மாநில அரசு கட்டளையிட முடியாது.",
            "fact_en": "Violation of the Model Code of Conduct can lead to disciplinary action and lodging of FIRs under SEC directives.",
            "fact_ta": "மாதிரி நடத்தை நெறிமுறைகளை மீறினால் SEC உத்தரவுகளின் கீழ் ஒழுங்கு நடவடிக்கை மற்றும் எஃப்.ஐ.ஆர் பதிவு செய்யப்படலாம்."
        },

        # 15. Disqualification disputes under 243F / 243V
        {
            "subtopic": "sec_constitutional_provisions",
            "stem_en": "Under Articles 243F(2) and 243V(2), if any question arises as to whether a member of a Panchayat or Municipality has become subject to disqualification, to whom must the question be referred?",
            "stem_ta": "சரத்துகள் 243F(2) மற்றும் 243V(2)-ன் கீழ், ஒரு ஊராட்சி அல்லது நகராட்சியின் உறுப்பினர் தகுதி இழப்பிற்கு ஆளாகிவிட்டாரா என்ற கேள்வி எழுந்தால், அந்த விவகாரம் யாரிடம் பரிந்துரைக்கப்பட வேண்டும்?",
            "options": [
                ("To such authority and in such manner as the Legislature of a State may by law provide", "மாநில சட்டமன்றம் சட்டத்தின் மூலம் ஏற்படுத்திய அதிகாரி மற்றும் நடைமுறையின்படி"),
                ("Directly to the President of India", "நேரடியாக இந்திய குடியரசுத் தலைவரிடம்"),
                ("Exclusively to the Lokayukta of the State", "மாநில லோக்ஆயுக்தாவிடம் மட்டுமே"),
                ("To a three-member committee of the ruling party MLAs", "ஆளும் கட்சி சட்டமன்ற உறுப்பினர்களின் மூன்று நபர் குழுவிடம்")
            ],
            "correct_key": "A",
            "exp_en": "Articles 243F(2) (for Panchayats) and 243V(2) (for Municipalities) state that if any question arises regarding disqualification of a member, it shall be referred for the decision of such authority and in such manner as the Legislature of a State may by law provide.",
            "exp_ta": "சரத்துகள் 243F(2) மற்றும் 243V(2) ஆகியவற்றின்படி, ஓர் உறுப்பினர் தகுதி இழப்புக்கு ஆளாகிவிட்டாரா என்ற கேள்வி எழுந்தால், மாநில சட்டமன்றம் சட்டத்தின் மூலம் வழங்கும் அதிகாரி மற்றும் நடைமுறையின்படி தீர்வுக்காக அனுப்பப்பட வேண்டும்.",
            "why_a_en": "Correct. State Legislature decides the forum (e.g. District Judge or SEC or designated appellate authority).",
            "why_a_ta": "சரி. மாநில சட்டமன்றமே அதற்கான அதிகாரியை (எ.கா. மாவட்ட நீதிபதி அல்லது SEC) முடிவு செய்கிறது.",
            "why_b_en": "Incorrect. President decides MP disqualifications under Article 103, not local bodies.",
            "why_b_ta": "தவறு. குடியரசுத் தலைவர் எம்.பி.க்கள் தகுதி இழப்பை சரத்து 103-ன் கீழ் முடிவு செய்கிறார், உள்ளாட்சி அல்ல.",
            "why_c_en": "Incorrect. Lokayukta deals with corruption inquiries, not constitutional election disqualifications.",
            "why_c_ta": "தவறு. லோக்ஆயுக்தா ஊழல் விசாரணைகளைக் கையாள்கிறது, தகுதி இழப்பை அல்ல.",
            "why_d_en": "Incorrect. Political party committees have no constitutional standing.",
            "why_d_ta": "தவறு. அரசியல் கட்சிக் குழுக்களுக்கு அரசியலமைப்பு அந்தஸ்து இல்லை.",
            "tip_en": "Contrast: For MPs -> President (Art 103); for MLAs -> Governor (Art 192); for PRIs/ULBs -> Authority provided by State Law (Art 243F/243V).",
            "tip_ta": "ஒப்பிடுக: எம்.பி -> குடியரசுத் தலைவர் (103); எம்.எல்.ஏ -> ஆளுநர் (192); உள்ளாட்சி -> மாநிலச் சட்டம் கூறும் அதிகாரி (243F/243V).",
            "fact_en": "A minimum age of 21 years qualifies a person to be chosen as a member of a local body (unlike 25 for MLA).",
            "fact_ta": "உள்ளாட்சி உறுப்பினராகத் தேர்ந்தெடுக்கப்பட குறைந்தபட்ச வயது 21 ஆண்டுகள் ஆகும் (எம்.எல்.ஏ.-வுக்கு 25 ஆண்டுகள்)."
        },

        # 16. ECI vs SEC Jurisdiction distinction
        {
            "subtopic": "sec_powers_functions_elections",
            "stem_en": "Which of the following bodies is NOT subject to elections conducted by the State Election Commission?",
            "stem_ta": "பின்வருவனவற்றில் எந்த அமைப்பிற்கான தேர்தல் மாநில தேர்தல் ஆணையத்தால் நடத்தப்படுவதில்லை?",
            "options": [
                ("State Legislative Assembly and State Legislative Council", "மாநில சட்டப் பேரவை மற்றும் மாநில சட்ட மேலவை"),
                ("Gram Panchayats and Panchayat Unions", "கிராம ஊராட்சிகள் மற்றும் ஊராட்சி ஒன்றியங்கள்"),
                ("District Panchayats (Zilla Parishads)", "மாவட்ட ஊராட்சிகள் (ஜில்லா பரிஷத்துகள்)"),
                ("Municipal Corporations, Municipalities, and Town Panchayats", "மாநகராட்சிகள், நகராட்சிகள் மற்றும் பேரூராட்சிகள்")
            ],
            "correct_key": "A",
            "exp_en": "The State Legislative Assembly and Council elections are conducted by the Election Commission of India under Article 324. The State Election Commission conducts elections strictly to rural local bodies (PRIs) and urban local bodies (ULBs) under Articles 243K and 243ZA.",
            "exp_ta": "மாநில சட்டப் பேரவை மற்றும் சட்ட மேலவைத் தேர்தல்கள் சரத்து 324-ன் கீழ் இந்தியத் தேர்தல் ஆணையத்தால் நடத்தப்படுகின்றன. மாநிலத் தேர்தல் ஆணையம் சரத்துகள் 243K மற்றும் 243ZA-ன் கீழ் ஊரக மற்றும் நகர்ப்புற உள்ளாட்சி அமைப்புகளுக்கு மட்டுமே தேர்தல்களை நடத்துகிறது.",
            "why_a_en": "Correct. State Legislature elections belong entirely to the jurisdiction of the Election Commission of India.",
            "why_a_ta": "சரி. மாநில சட்டமன்றத் தேர்தல்கள் முழுமையாக இந்திய தேர்தல் ஆணையத்தின் அதிகார வரம்பிற்கு உட்பட்டவை.",
            "why_b_en": "Incorrect. Village Panchayats and Panchayat Unions are under SEC.",
            "why_b_ta": "தவறு. கிராம ஊராட்சிகள் மற்றும் ஊராட்சி ஒன்றியங்கள் SEC-ன் கீழ் உள்ளன.",
            "why_c_en": "Incorrect. District Panchayats are under SEC.",
            "why_c_ta": "தவறு. மாவட்ட ஊராட்சிகள் SEC-ன் கீழ் உள்ளன.",
            "why_d_en": "Incorrect. Urban bodies (Corporations, Municipalities, Town Panchayats) are under SEC.",
            "why_d_ta": "தவறு. நகர்ப்புற உள்ளாட்சி அமைப்புகள் SEC-ன் கீழ் வருகின்றன.",
            "tip_en": "ECI = President, Vice President, Parliament, Vidhan Sabha, Vidhan Parishad. SEC = Panchayats and Municipalities.",
            "tip_ta": "ECI = குடியரசுத் தலைவர், துணைத் தலைவர், பாராளுமன்றம், சட்டமன்றம், மேலவை. SEC = ஊராட்சிகள் மற்றும் நகராட்சிகள்.",
            "fact_en": "ECI and SEC are distinct, independent constitutional bodies with no hierarchical subordinate relationship.",
            "fact_ta": "ECI மற்றும் SEC ஆகியவை தமக்குள் எந்தவொரு படிநிலை கீழ்நிலையும் இல்லாத தனித்தனி அரசியலமைப்பு அமைப்புகளாகும்."
        },

        # 17. Electoral rolls integration
        {
            "subtopic": "sec_powers_functions_elections",
            "stem_en": "How are the electoral rolls for local body elections prepared by the State Election Commission in practice?",
            "stem_ta": "நடைமுறையில் உள்ளாட்சித் தேர்தல்களுக்கான வாக்காளர் பட்டியல்களை மாநிலத் தேர்தல் ஆணையம் எவ்வாறு தயார் செய்கிறது?",
            "options": [
                ("By adopting the relevant parts of the ECI Assembly electoral rolls and ward-wise splitting them", "இந்திய தேர்தல் ஆணையத்தின் சட்டமன்ற வாக்காளர் பட்டியலின் தொடர்புடைய பகுதிகளை ஏற்று வார்டு வாரியாக பிரிப்பதன் மூலம்"),
                ("By conducting an independent house-to-house census every six months without using assembly rolls", "சட்டமன்ற பட்டியலைப் பயன்படுத்தாமல் ஒவ்வொரு ஆறு மாதங்களுக்கும் தனி கணக்கெடுப்பு நடத்துவதன் மூலம்"),
                ("By relying entirely on the ration card database managed by the Food Department", "உணவுத் துறையால் நிர்வகிக்கப்படும் ரேஷன் கார்டு தரவுத்தளத்தை மட்டுமே நம்பியிருப்பதன் மூலம்"),
                ("By delegating the entire roll preparation to local commercial contractors", "வாக்காளர் பட்டியல் தயாரிப்பை முழுமையாக உள்ளூர் தனியார் ஒப்பந்ததாரர்களிடம் ஒப்படைப்பதன் மூலம்")
            ],
            "correct_key": "A",
            "exp_en": "Under state panchayat and municipal laws, the State Election Commission is empowered to adopt the electoral rolls prepared by the Election Commission of India for the State Legislative Assembly constituencies as the base, segregating voters ward-by-ward and street-by-street.",
            "exp_ta": "மாநில உள்ளாட்சிச் சட்டங்களின்படி, சட்டப் பேரவைத் தொகுதிகளுக்காக இந்தியத் தேர்தல் ஆணையம் தயாரித்த வாக்காளர் பட்டியலை அடிப்படையாக ஏற்று, வார்டு வாரியாகவும் தெரு வாரியாகவும் வாக்காளர்களைப் பிரித்து உள்ளாட்சி வாக்காளர் பட்டியலைத் தயாரிக்க SEC-க்கு அதிகாரம் உள்ளது.",
            "why_a_en": "Correct. Assembly rolls prepared by ECI are adopted and adapted ward-wise by SEC.",
            "why_a_ta": "சரி. ECI தயாரித்த சட்டமன்றப் பட்டியல் ஏற்கப்பட்டு, SEC-யால் வார்டு வாரியாகப் பிரிக்கப்படுகிறது.",
            "why_b_en": "Incorrect. Completely independent door-to-door census is not feasible or standard practice.",
            "why_b_ta": "தவறு. முற்றிலும் சுயேச்சையான தனி கணக்கெடுப்பு சாத்தியமற்றது மற்றும் நடைமுறையில் இல்லை.",
            "why_c_en": "Incorrect. Ration card databases do not define constitutional franchise.",
            "why_c_ta": "தவறு. குடும்ப அட்டை தரவுத்தளம் வாக்களிக்கும் உரிமையை நிர்ணயிப்பதில்லை.",
            "why_d_en": "Incorrect. Constitutional duty cannot be delegated to private contractors.",
            "why_d_ta": "தவறு. அரசியலமைப்பு கடமையை தனியார் ஒப்பந்ததாரர்களிடம் ஒப்படைக்க முடியாது.",
            "tip_en": "SEC has plenary power to prepare its own rolls, but adopts ECI rolls to save cost and avoid duplication.",
            "tip_ta": "SEC-க்கு சொந்தப் பட்டியல் தயாரிக்க அதிகாரம் இருந்தாலும், செலவைத் தவிர்க்க ECI பட்டியலை ஏற்றுக்கொள்கிறது.",
            "fact_en": "Anyone enrolled in the Assembly electoral roll for the corresponding area is entitled to vote in local body polls.",
            "fact_ta": "சம்பந்தப்பட்ட பகுதிக்கான சட்டமன்ற வாக்காளர் பட்டியலில் இடம்பெற்றுள்ள எவரும் உள்ளாட்சித் தேர்தலில் வாக்களிக்க தகுதியுடையவர்."
        },

        # 18. Plenary power to order re-poll
        {
            "subtopic": "sec_powers_functions_elections",
            "stem_en": "In the event of booth capturing, natural calamity, or large-scale violence during local polls, under which authority does the State Election Commission order a fresh poll or re-poll?",
            "stem_ta": "உள்ளாட்சித் தேர்தலின் போது வாக்குச்சாவடி கைப்பற்றுதல், இயற்கை பேரிடர் அல்லது பெருமளவிலான வன்முறை ஏற்பட்டால், எந்த அதிகாரத்தின் கீழ் மாநிலத் தேர்தல் ஆணையம் மறுவாக்குப்பதிவுக்கு உத்தரவிடுகிறது?",
            "options": [
                ("Plenary powers of superintendence, direction, and control under Articles 243K and 243ZA", "சரத்துகள் 243K மற்றும் 243ZA-ன் கீழ் உள்ள முழுமையான மேற்பார்வை மற்றும் வழிகாட்டுதல் அதிகாரங்கள்"),
                ("Only upon receiving written sanction from the Union Home Ministry", "மத்திய உள்துறை அமைச்சகத்திடம் எழுத்துப்பூர்வ அனுமதி பெற்ற பின்னரே"),
                ("Only after obtaining prior concurrence of the High Court Registrar", "உயர்நீதிமன்றப் பதிவாளரின் முன் அனுமதியைப் பெற்ற பிறகு மட்டுமே"),
                ("Through an ordinance promulgated by the Governor on Cabinet advice", "அமைச்சரவையின் ஆலோசனையின் பேரில் ஆளுநர் பிறப்பிக்கும் அவசரச் சட்டத்தின் மூலம்")
            ],
            "correct_key": "A",
            "exp_en": "The plenary powers of superintendence, direction, and control vested in the State Election Commission under Articles 243K and 243ZA empower it to adjourn polls, declare votes void, and order re-polls to uphold free and fair elections.",
            "exp_ta": "சரத்துகள் 243K மற்றும் 243ZA-ன் கீழ் மாநிலத் தேர்தல் ஆணையத்திடம் ஒப்படைக்கப்பட்டுள்ள முழுமையான அதிகாரங்கள், வாக்குப்பதிவை ஒத்திவைக்கவும், வாக்குகளை செல்லாது என அறிவிக்கவும், மறுவாக்குப்பதிவுக்கு உத்தரவிடவும் அதற்கு அதிகாரம் அளிக்கின்றன.",
            "why_a_en": "Correct. Constitutional vesting of superintendence and control gives plenary authority for re-poll.",
            "why_a_ta": "சரி. மேற்பார்வை மற்றும் கட்டுப்பாட்டுக்கான அரசியலமைப்பு அதிகாரம் மறுவாக்குப்பதிவுக்கான முழுமையான அதிகாரத்தை அளிக்கிறது.",
            "why_b_en": "Incorrect. SEC does not report to the Union Home Ministry.",
            "why_b_ta": "தவறு. SEC மத்திய உள்துறை அமைச்சகத்தின் கீழ் செயல்படுவதில்லை.",
            "why_c_en": "Incorrect. Judicial concurrence is not required for administrative election orders.",
            "why_c_ta": "தவறு. நிர்வாக தேர்தல் உத்தரவுகளுக்கு நீதிமன்ற ஒப்புதல் தேவையில்லை.",
            "why_d_en": "Incorrect. Ordinances are not required to counter election day irregularities.",
            "why_d_ta": "தவறு. தேர்தல் முறைகேடுகளை சமாளிக்க அவசரச் சட்டங்கள் தேவையில்லை.",
            "tip_en": "Kishan Singh Tomar (2006) affirmed that SEC has inherent plenary powers identical to ECI under Mohinder Singh Gill.",
            "tip_ta": "கிஷன் சிங் தோமர் (2006) தீர்ப்பு SEC-க்கு ECI போன்றே உள்ளார்ந்த முழு அதிகாரங்கள் உண்டு என்பதை உறுதி செய்தது.",
            "fact_en": "The SEC can also change Returning Officers or observers if their neutrality is compromised.",
            "fact_ta": "தேர்தல் நடத்தும் அதிகாரிகளின் நடுநிலைமை பாதிக்கப்பட்டால் அவர்களை மாற்றவும் SEC-க்கு அதிகாரம் உண்டு."
        },

        # 19. Multi-post EVMs
        {
            "subtopic": "sec_powers_functions_elections",
            "stem_en": "What technological innovation has been deployed by State Election Commissions (such as in Tamil Nadu) to conduct simultaneous voting for multiple tiers of Panchayats?",
            "stem_ta": "ஊராட்சிகளின் பல்வேறு அடுக்குகளுக்கு ஒரே நேரத்தில் வாக்குப்பதிவு நடத்துவதற்காக மாநில தேர்தல் ஆணையங்களால் (தமிழ்நாடு போன்றவை) பயன்படுத்தப்பட்ட தொழில்நுட்ப கண்டுபிடிப்பு எது?",
            "options": [
                ("Multi-post Electronic Voting Machines (EVMs)", "பல பதவிகளுக்கான மின்னணு வாக்குப்பதிவு இயந்திரங்கள் (Multi-post EVMs)"),
                ("Blockchain-based mobile remote voting systems", "பிளாக்செயின் அடிப்படையிலான மொபைல் தொலைதூர வாக்குப்பதிவு முறைகள்"),
                ("Optical Mark Recognition (OMR) optical scanners", "OMR ஆப்டிகல் ஸ்கேனர்கள்"),
                ("Facial recognition internet voting kiosks", "முக அங்கீகார இணைய வாக்குப்பதிவு மையங்கள்")
            ],
            "correct_key": "A",
            "exp_en": "State Election Commissions developed and deployed Multi-post EVMs capable of recording separate votes for Gram Panchayat Ward Member, Gram Panchayat President, Panchayat Union Ward Member, and District Panchayat Ward Member simultaneously.",
            "exp_ta": "கிராம ஊராட்சி வார்டு உறுப்பினர், ஊராட்சி தலைவர், ஒன்றிய வார்டு உறுப்பினர் மற்றும் மாவட்ட ஊராட்சி வார்டு உறுப்பினர் ஆகிய பதவிகளுக்கு ஒரே நேரத்தில் தனித்தனியாக வாக்குகளைப் பதிவு செய்யக்கூடிய 'பல பதவிகளுக்கான மின்னணு வாக்குப்பதிவு இயந்திரங்களை' மாநில தேர்தல் ஆணையங்கள் பயன்படுத்தின.",
            "why_a_en": "Correct. Multi-post EVMs allow a rural voter to cast 4 different votes on a single setup.",
            "why_a_ta": "சரி. Multi-post EVM-கள் ஒரு கிராம வாக்காளர் ஒரே அமைப்பில் 4 வெவ்வேறு வாக்குகளைப் பதிவு செய்ய அனுமதிக்கின்றன.",
            "why_b_en": "Incorrect. Mobile blockchain voting is not adopted for local elections in India.",
            "why_b_ta": "தவறு. மொபைல் பிளாக்செயின் வாக்குப்பதிவு இந்தியாவில் உள்ளாட்சித் தேர்தல்களுக்கு நடைமுறையில் இல்லை.",
            "why_c_en": "Incorrect. OMR scanners are not used as ballot casting machines in TN polls.",
            "why_c_ta": "தவறு. OMR ஸ்கேனர்கள் வாக்குப்பதிவு இயந்திரங்களாகப் பயன்படுத்தப்படுவதில்லை.",
            "why_d_en": "Incorrect. Facial recognition internet kiosks are not authorized.",
            "why_d_ta": "தவறு. இணைய வழி வாக்குப்பதிவு மையங்களுக்கு அனுமதி இல்லை.",
            "tip_en": "In urban local bodies (ULBs), single-post EVMs are generally used because voters cast only one vote for their ward councillor.",
            "tip_ta": "நகர்ப்புறங்களில் வாக்காளர் ஒரு வார்டு உறுப்பினருக்கு மட்டுமே வாக்களிப்பதால் ஒற்றைப் பதவி EVM பயன்படுத்தப்படுகிறது.",
            "fact_en": "Multi-post EVMs were developed in collaboration with Electronics Corporation of India Limited (ECIL) and BEL.",
            "fact_ta": "ECIL மற்றும் BEL நிறுவனங்களின் ஒத்துழைப்புடன் இந்த பல-பதவி EVM-கள் உருவாக்கப்பட்டன."
        },

        # 20. Direct vs Indirect elections
        {
            "subtopic": "sec_powers_functions_elections",
            "stem_en": "In local governance, which of the following positions in Tamil Nadu is filled through INDIRECT election by elected ward members under SEC supervision?",
            "stem_ta": "தமிழ்நாட்டில் உள்ளாட்சி நிர்வாகத்தில், மாநிலத் தேர்தல் ஆணையத்தின் மேற்பார்வையின் கீழ் தேர்ந்தெடுக்கப்பட்ட வார்டு உறுப்பினர்களால் மறைமுகத் தேர்தல் மூலம் நிரப்பப்படும் பதவி எது?",
            "options": [
                ("Chairman of Panchayat Union Council and District Panchayat", "ஊராட்சி ஒன்றியக் குழு மற்றும் மாவட்ட ஊராட்சிக் குழுத் தலைவர்"),
                ("Village Panchayat Ward Member", "கிராம ஊராட்சி வார்டு உறுப்பினர்"),
                ("Village Panchayat President", "கிராம ஊராட்சி மன்றத் தலைவர்"),
                ("Municipal Corporation Ward Councillor", "மாநகராட்சி வார்டு கவுன்சிலர்")
            ],
            "correct_key": "A",
            "exp_en": "Under the Tamil Nadu Panchayats Act, the Chairman and Vice-Chairman of Panchayat Union Councils and District Panchayats are indirectly elected by and from among the elected ward members. Village Panchayat Presidents and Ward Members are directly elected by voters.",
            "exp_ta": "தமிழ்நாடு ஊராட்சிகள் சட்டத்தின் கீழ், ஊராட்சி ஒன்றியக் குழு மற்றும் மாவட்ட ஊராட்சிக் குழுக்களின் தலைவர்கள் தேர்ந்தெடுக்கப்பட்ட வார்டு உறுப்பினர்களிலிருந்து மறைமுகத் தேர்தல் மூலம் தேர்ந்தெடுக்கப்படுகிறார்கள்.",
            "why_a_en": "Correct. Intermediate and district panchayat chairpersons are elected indirectly across India (Article 243C(5)).",
            "why_a_ta": "சரி. ஒன்றிய மற்றும் மாவட்ட ஊராட்சித் தலைவர்கள் மறைமுகத் தேர்தல் மூலம் தேர்ந்தெடுக்கப்படுகிறார்கள் (சரத்து 243C(5)).",
            "why_b_en": "Incorrect. Ward members are directly elected by universal adult franchise.",
            "why_b_ta": "தவறு. வார்டு உறுப்பினர்கள் நேரடித் தேர்தல் மூலம் தேர்ந்தெடுக்கப்படுகிறார்கள்.",
            "why_c_en": "Incorrect. Village Panchayat Presidents in Tamil Nadu are directly elected by village voters.",
            "why_c_ta": "தவறு. தமிழ்நாட்டில் கிராம ஊராட்சித் தலைவர் கிராம வாக்காளர்களால் நேரடியாகத் தேர்ந்தெடுக்கப்படுகிறார்.",
            "why_d_en": "Incorrect. Ward councillors are directly elected by city voters.",
            "why_d_ta": "தவறு. வார்டு கவுன்சிலர்கள் நகர வாக்காளர்களால் நேரடியாகத் தேர்ந்தெடுக்கப்படுகிறார்கள்.",
            "tip_en": "Article 243C(5): Chairperson of Panchayat at intermediate or district level SHALL be elected indirectly; at village level, as state law provides.",
            "tip_ta": "சரத்து 243C(5): இடைநிலை மற்றும் மாவட்ட ஊராட்சித் தலைவர்கள் மறைமுகமாக மட்டுமே தேர்ந்தெடுக்கப்பட வேண்டும்.",
            "fact_en": "Mayors of Municipal Corporations in Tamil Nadu have alternated between direct and indirect elections depending on legislative amendments.",
            "fact_ta": "தமிழ்நாட்டில் மாநகராட்சி மேயர்கள் சட்டமன்றத் திருத்தங்களைப் பொறுத்து நேரடி மற்றும் மறைமுகத் தேர்தல்களுக்கு இடையே மாற்றப்பட்டுள்ளனர்."
        },

        # 21. Reservation of offices rotation
        {
            "subtopic": "sec_powers_functions_elections",
            "stem_en": "Under Articles 243D and 243T, on what basis must the reservation of seats and offices of Chairpersons for SCs, STs, and Women be implemented across successive elections?",
            "stem_ta": "சரத்துகள் 243D மற்றும் 243T-ன் கீழ், அடுத்தடுத்த தேர்தல்களில் பட்டியல் சாதிகள், பழங்குடியினர் மற்றும் பெண்களுக்கான இடங்கள் மற்றும் தலைவர் பதவிகளுக்கான இடஒதுக்கீடு எந்த அடிப்படையில் செயல்படுத்தப்பட வேண்டும்?",
            "options": [
                ("By rotation to different constituencies and wards", "வெவ்வேறு தொகுதிகள் மற்றும் வார்டுகளுக்கு சுழற்சி முறை அடிப்படையில்"),
                ("Permanently fixed in the same wards for a 50-year period", "50 ஆண்டு காலத்திற்கு ஒரே வார்டுகளில் நிரந்தரமாக நிர்ணயிக்கப்பட்டு"),
                ("Decided by a lottery draw held on the day of polling", "வாக்குப்பதிவு நாளன்று நடத்தப்படும் குலுக்கல் முறை மூலம்"),
                ("Restricted only to urban municipal wards with no rural rotation", "ஊரக சுழற்சி இல்லாமல் நகர்ப்புற நகராட்சி வார்டுகளுக்கு மட்டுமே மட்டுப்படுத்தப்பட்டு")
            ],
            "correct_key": "A",
            "exp_en": "Articles 243D and 243T mandate that seats reserved for Scheduled Castes, Scheduled Tribes, and Women (including chairpersons' offices) may be allotted by rotation to different constituencies in a Panchayat or Municipality.",
            "exp_ta": "சரத்துகள் 243D மற்றும் 243T ஆகியவை பட்டியல் சாதியினர், பழங்குடியினர் மற்றும் பெண்களுக்காக ஒதுக்கப்பட்ட இடங்கள் (தலைவர் பதவிகள் உட்பட) ஒரு ஊராட்சி அல்லது நகராட்சியில் உள்ள வெவ்வேறு தொகுதிகளுக்கு சுழற்சி முறையில் ஒதுக்கப்படலாம் என்று கூறுகின்றன.",
            "why_a_en": "Correct. Principle of rotation is explicitly enshrined in Articles 243D(1) and 243T(1).",
            "why_a_ta": "சரி. சுழற்சி முறை சரத்துகள் 243D(1) மற்றும் 243T(1)-ல் வெளிப்படையாகக் கூறப்பட்டுள்ளது.",
            "why_b_en": "Incorrect. Permanent freezing defeats equal geographic opportunity.",
            "why_b_ta": "தவறு. நிரந்தரமாக முடக்குவது சமமான வாய்ப்பைத் தடுக்கும்.",
            "why_c_en": "Incorrect. Quotas are gazetted months ahead of poll notifications, not on polling day.",
            "why_c_ta": "தவறு. இடஒதுக்கீடு தேர்தலுக்கு முன்பே அரசிதழில் வெளியிடப்படுகிறது.",
            "why_d_en": "Incorrect. Rotation applies equally to both Panchayats (243D) and Municipalities (243T).",
            "why_d_ta": "தவறு. சுழற்சி முறை ஊராட்சிகளுக்கும் நகராட்சிகளுக்கும் சமமாகப் பொருந்தும்.",
            "tip_en": "Tamil Nadu provides 50% reservation for women in local bodies (increased from the constitutional minimum of 33.3%).",
            "tip_ta": "தமிழ்நாடு உள்ளாட்சி அமைப்புகளில் பெண்களுக்கு 50% இடஒதுக்கீடு வழங்குகிறது (அரசியலமைப்பு குறைந்தபட்சம் 33.3%).",
            "fact_en": "Tamil Nadu amended its Panchayat and Municipal Acts in 2016 to increase women's reservation to 50%.",
            "fact_ta": "பெண்களுக்கான இடஒதுக்கீட்டை 50% ஆக உயர்த்த தமிழ்நாடு 2016-ல் தனது ஊராட்சி மற்றும் நகராட்சி சட்டங்களைத் திருத்தியது."
        },

        # 22. None of the Above (NOTA) in SEC polls
        {
            "subtopic": "sec_powers_functions_elections",
            "stem_en": "Following the Supreme Court's directives in the PUCL case, how did State Election Commissions incorporate voter rejection on ballot papers and EVMs?",
            "stem_ta": "PUCL வழக்கில் உச்ச நீதிமன்றத்தின் உத்தரவுகளைத் தொடர்ந்து, வாக்குச் சீட்டுகள் மற்றும் EVM-களில் வாக்காளர்களின் நிராகரிப்பு உரிமையை மாநிலத் தேர்தல் ஆணையங்கள் எவ்வாறு இணைத்தன?",
            "options": [
                ("By introducing the 'None of the Above' (NOTA) option as the last choice", "'மேற்கண்ட எவருமில்லை' (NOTA) விருப்பத்தை கடைசித் தேர்வாக அறிமுகப்படுத்துவதன் மூலம்"),
                ("By providing a secret negative marking box beside every candidate", "ஒவ்வொரு வேட்பாளரின் பக்கத்திலும் ரகசிய எதிர்மறை மதிப்பெண் பெட்டியை வழங்குவதன் மூலம்"),
                ("By requiring voters to surrender their voter ID cards if unsatisfied", "திருப்தியடையாத வாக்காளர்கள் தங்கள் வாக்காளர் அடையாள அட்டையை ஒப்படைக்கக் கோருவதன் மூலம்"),
                ("By conducting mandatory manual paper recall ballots", "கட்டாய காகித திரும்ப அழைக்கும் வாக்குகளை நடத்துவதன் மூலம்")
            ],
            "correct_key": "A",
            "exp_en": "Following the People's Union for Civil Liberties (PUCL) v. Union of India (2013) judgment, State Election Commissions incorporated NOTA ('None of the Above' / 'நோட்டா') as an option on EVMs and ballot papers for local body elections.",
            "exp_ta": "PUCL எதிர் இந்திய யூனியன் (2013) தீர்ப்பைத் தொடர்ந்து, உள்ளாட்சித் தேர்தல்களுக்கான வாக்குப்பதிவு இயந்திரங்கள் மற்றும் வாக்குச் சீட்டுகளில் NOTA ('நோட்டா') விருப்பத்தை மாநில தேர்தல் ஆணையங்கள் இணைத்தன.",
            "why_a_en": "Correct. NOTA enables electors to exercise their right not to vote for any candidate while maintaining secrecy.",
            "why_a_ta": "சரி. நோட்டா ரகசியத்தன்மையைப் பேணி எந்த வேட்பாளருக்கும் வாக்களிக்காத உரிமையை வழங்குகிறது.",
            "why_b_en": "Incorrect. Negative marking does not exist in Indian elections.",
            "why_b_ta": "தவறு. இந்தியத் தேர்தல்களில் எதிர்மறை வாக்குகள் இல்லை.",
            "why_c_en": "Incorrect. Surrendering voter IDs is completely illegal.",
            "why_c_ta": "தவறு. அடையாள அட்டையை ஒப்படைப்பது சட்டவிரோதமானது.",
            "why_d_en": "Incorrect. Manual recall ballots are not part of Indian local elections.",
            "why_d_ta": "தவறு. திரும்ப அழைக்கும் வாக்குகள் நடைமுறையில் இல்லை.",
            "tip_en": "NOTA votes do not lead to election cancellation under standard rules unless specific state amendments apply.",
            "tip_ta": "குறிப்பிட்ட மாநில விதிகள் திருத்தப்படாவிட்டால், நோட்டா வாக்குகள் அதிகபட்சமாக இருந்தாலும் தேர்தல் ரத்து செய்யப்படுவதில்லை.",
            "fact_en": "Maharashtra and Haryana SECs subsequently framed rules treating NOTA as a 'fictional candidate' requiring re-poll if NOTA secures majority.",
            "fact_ta": "மகாராஷ்டிரா மற்றும் ஹரியானா SEC-கள் நோட்டா பெரும்பான்மை பெற்றால் மறுதேர்தல் நடத்தும் விதிகளை வகுத்தன."
        },

        # 23. Disqualification for non-submission of election expenses
        {
            "subtopic": "sec_powers_functions_elections",
            "stem_en": "If a contesting candidate in local body elections fails to lodge an account of election expenses within the prescribed period without good reason, what power does the State Election Commission possess?",
            "stem_ta": "உள்ளாட்சித் தேர்தலில் போட்டியிடும் ஒரு வேட்பாளர் உரிய காரணமின்றி குறிப்பிட்ட காலத்திற்குள் தேர்தல் செலவுக் கணக்கை தாக்கல் செய்யத் தவறினால், மாநில தேர்தல் ஆணையத்திற்கு என்ன அதிகாரம் உள்ளது?",
            "options": [
                ("Power to declare the candidate disqualified for a specified period (e.g. 3 years)", "குறிப்பிட்ட காலத்திற்கு (எ.கா. 3 ஆண்டுகள்) அத்தேர்தல் வேட்பாளரை தகுதியற்றவர் என அறிவிக்கும் அதிகாரம்"),
                ("Power to confiscate the entire ancestral property of the candidate", "வேட்பாளரின் முழு பூர்வீகச் சொத்தையும் பறிமுதல் செய்யும் அதிகாரம்"),
                ("Power to cancel the civic voting rights of the candidate's entire family", "வேட்பாளரின் முழு குடும்பத்தின் வாக்குரிமையை ரத்து செய்யும் அதிகாரம்"),
                ("Power to order immediate preventive detention without trial", "விசாரணையின்றி உடனடி தடுப்புக் காவலுக்கு உத்தரவிடும் அதிகாரம்")
            ],
            "correct_key": "A",
            "exp_en": "Under state local body election rules, the State Election Commission has statutory powers to disqualify a candidate who fails to lodge election expense accounts within the stipulated time without justifiable reason, typically for a period of three years.",
            "exp_ta": "மாநில உள்ளாட்சித் தேர்தல் விதிகளின்படி, நியாயமான காரணமின்றி நிர்ணயிக்கப்பட்ட காலத்திற்குள் தேர்தல் செலவுக் கணக்குகளைத் தாக்கல் செய்யத் தவறும் ஒரு வேட்பாளரை பொதுவாக 3 ஆண்டுகள் வரை தகுதி நீக்கம் செய்ய மாநில தேர்தல் ஆணையத்திற்கு அதிகாரம் உள்ளது.",
            "why_a_en": "Correct. Disqualification for a fixed term (usually 3 years) is the standard statutory sanction.",
            "why_a_ta": "சரி. ஒரு குறிப்பிட்ட காலத்திற்கு (பொதுவாக 3 ஆண்டுகள்) தகுதி நீக்கம் செய்வதே நிலையான சட்டப்பூர்வ தண்டனையாகும்.",
            "why_b_en": "Incorrect. Property confiscation is not permissible for election expense defaults.",
            "why_b_ta": "தவறு. செலவுக் கணக்கு தாக்கல் செய்யாததற்காக சொத்து பறிமுதல் செய்ய முடியாது.",
            "why_c_en": "Incorrect. Family voting rights cannot be revoked.",
            "why_c_ta": "தவறு. குடும்பத்தின் வாக்குரிமையை ரத்து செய்ய முடியாது.",
            "why_d_en": "Incorrect. Preventive detention is unconstitutional in this context.",
            "why_d_ta": "தவறு. இச்சூழலில் தடுப்புக் காவல் அரசியலமைப்புக்கு முரணானது.",
            "tip_en": "Laxmikanth Notes: Failure to lodge election expenses within time leads to disqualification under SEC orders.",
            "tip_ta": "லட்சுமிகாந்த் குறிப்புகள்: தேர்தல் செலவுக் கணக்கை உரிய நேரத்தில் தாக்கல் செய்யத் தவறினால் SEC உத்தரவின் பேரில் தகுதி நீக்கம் செய்யப்படும்.",
            "fact_en": "TN SEC mandates filing of election expenses within 30 days of the declaration of local election results.",
            "fact_ta": "உள்ளாட்சித் தேர்தல் முடிவுகள் அறிவிக்கப்பட்ட 30 நாட்களுக்குள் தேர்தல் செலவுக் கணக்கை தாக்கல் செய்ய வேண்டும் என TN SEC கட்டாயமாக்குகிறது."
        },

        # 24. Symbol Allotment and Unrecognized Parties
        {
            "subtopic": "sec_powers_functions_elections",
            "stem_en": "How are election symbols allocated to political parties and independent candidates in local body elections?",
            "stem_ta": "உள்ளாட்சித் தேர்தல்களில் அரசியல் கட்சிகளுக்கும் சுயேச்சை வேட்பாளர்களுக்கும் தேர்தல் சின்னங்கள் எவ்வாறு ஒதுக்கப்படுகின்றன?",
            "options": [
                ("Under the Local Bodies Election Symbols (Reservation and Allotment) Order issued by the SEC", "மாநில தேர்தல் ஆணையத்தால் வெளியிடப்படும் உள்ளாட்சித் தேர்தல் சின்னங்கள் (ஒதுக்கீடு) உத்தரவின் கீழ்"),
                ("Directly by the Registrar of the Supreme Court", "நேரடியாக உச்ச நீதிமன்றப் பதிவாளரால்"),
                ("By drawing lots conducted by the District Police Superintendent", "மாவட்ட காவல் கண்காணிப்பாளரால் நடத்தப்படும் குலுக்கல் மூலம்"),
                ("Exclusively on the recommendations of the State Planning Commission", "மாநில திட்டக் குழுவின் பரிந்துரைகளின் பேரில் மட்டுமே")
            ],
            "correct_key": "A",
            "exp_en": "The State Election Commission promulgates statutory orders (e.g. Tamil Nadu Local Bodies Election Symbols Order) reserving symbols for recognized national and state parties and providing a pool of free symbols for unrecognized parties and independents.",
            "exp_ta": "அங்கீகரிக்கப்பட்ட தேசிய மற்றும் மாநிலக் கட்சிகளுக்கான சின்னங்களை ஒதுக்கவும், சுயேச்சைகளுக்கு சுயாதீன சின்னங்களை வழங்கவும் மாநில தேர்தல் ஆணையம் உள்ளாட்சித் தேர்தல் சின்னங்கள் உத்தரவை வெளியிடுகிறது.",
            "why_a_en": "Correct. SEC issues the Election Symbols Order governing local polls.",
            "why_a_ta": "சரி. உள்ளாட்சித் தேர்தல்களை நிர்வகிக்கும் தேர்தல் சின்னங்கள் உத்தரவை SEC வெளியிடுகிறது.",
            "why_b_en": "Incorrect. Supreme Court does not allot election symbols.",
            "why_b_ta": "தவறு. உச்ச நீதிமன்றம் தேர்தல் சின்னங்களை ஒதுக்குவதில்லை.",
            "why_c_en": "Incorrect. Police officials have no symbol allocation authority.",
            "why_c_ta": "தவறு. சின்னங்கள் ஒதுக்கீட்டில் காவல்துறையினருக்கு அதிகாரம் இல்லை.",
            "why_d_en": "Incorrect. Planning Commission does not deal with election symbols.",
            "why_d_ta": "தவறு. திட்டக்குழு தேர்தல் சின்னங்களைக் கையாள்வதில்லை.",
            "tip_en": "In Tamil Nadu, elections to Village Panchayat Ward Members and Presidents are conducted on a NON-PARTY basis (no party symbols allowed).",
            "tip_ta": "தமிழ்நாட்டில், கிராம ஊராட்சி வார்டு உறுப்பினர் மற்றும் தலைவர் தேர்தல்கள் கட்சி சார்பற்ற அடிப்படையில் நடத்தப்படுகின்றன (கட்சி சின்னங்களுக்கு அனுமதியில்லை).",
            "fact_en": "Only Panchayat Union Ward, District Panchayat Ward, and Urban local body elections are held on party lines in Tamil Nadu.",
            "fact_ta": "ஒன்றிய வார்டு, மாவட்ட வார்டு மற்றும் நகர்ப்புற உள்ளாட்சித் தேர்தல்கள் மட்டுமே தமிழ்நாட்டில் கட்சி அடிப்படையில் நடத்தப்படுகின்றன."
        },

        # 25. Non-party elections in Village Panchayats
        {
            "subtopic": "sec_powers_functions_elections",
            "stem_en": "In Tamil Nadu, which tier of rural local governance conducts elections on a strictly non-party basis where party flags and symbols are banned?",
            "stem_ta": "தமிழ்நாட்டில் ஊரக உள்ளாட்சி அமைப்புகளில் எந்த அடுக்கிற்கான தேர்தல்கள் கட்சிச் சின்னங்கள் மற்றும் கொடிகள் தடை செய்யப்பட்டு முற்றிலும் கட்சி சார்பற்ற முறையில் நடத்தப்படுகின்றன?",
            "options": [
                ("Village Panchayat President and Village Panchayat Ward Members", "கிராம ஊராட்சி மன்றத் தலைவர் மற்றும் கிராம ஊராட்சி வார்டு உறுப்பினர்கள்"),
                ("Panchayat Union Ward Councillors", "ஊராட்சி ஒன்றிய வார்டு கவுன்சிலர்கள்"),
                ("District Panchayat Ward Councillors", "மாவட்ட ஊராட்சி வார்டு கவுன்சிலர்கள்"),
                ("Municipal Corporation Ward Councillors", "மாநகராட்சி வார்டு கவுன்சிலர்கள்")
            ],
            "correct_key": "A",
            "exp_en": "Under the Tamil Nadu Panchayats Act, 1994, elections to the offices of Village Panchayat President and Village Panchayat Ward Members are conducted on a non-party basis. Candidates are allotted free symbols and cannot use political party symbols or flags.",
            "exp_ta": "தமிழ்நாடு ஊராட்சிகள் சட்டம் 1994-ன் படி, கிராம ஊராட்சி தலைவர் மற்றும் கிராம ஊராட்சி வார்டு உறுப்பினர் பதவிகளுக்கான தேர்தல்கள் கட்சி சார்பற்ற முறையில் நடத்தப்படுகின்றன. வேட்பாளர்களுக்கு சுயேச்சை சின்னங்கள் மட்டுமே ஒதுக்கப்படுகின்றன.",
            "why_a_en": "Correct. Village Panchayat grassroots elections are non-party in Tamil Nadu.",
            "why_a_ta": "சரி. தமிழ்நாட்டில் கிராம ஊராட்சி தேர்தல்கள் கட்சி சார்பற்றவை.",
            "why_b_en": "Incorrect. Panchayat Union elections are contested on political party symbols.",
            "why_b_ta": "தவறு. ஊராட்சி ஒன்றியத் தேர்தல்கள் கட்சிச் சின்னங்களில் போட்டியிடப்படுகின்றன.",
            "why_c_en": "Incorrect. District Panchayat elections are contested on political party symbols.",
            "why_c_ta": "தவறு. மாவட்ட ஊராட்சி தேர்தல்கள் அரசியல் கட்சி சின்னங்களில் நடைபெறுகின்றன.",
            "why_d_en": "Incorrect. Municipal Corporation elections are fought along political party lines.",
            "why_d_ta": "தவறு. மாநகராட்சித் தேர்தல்கள் அரசியல் கட்சிகளின் சின்னங்களில் போட்டியிடப்படுகின்றன.",
            "tip_en": "Grassroots peace: Non-party elections at village level aim to prevent partisan rivalries from paralyzing basic civic amenities.",
            "tip_ta": "அடிமட்ட அமைதி: கட்சிப் பூசல்கள் அடிப்படை குடிமைப் பணிகளை முடக்குவதைத் தவிர்க்க கிராம அளவில் கட்சி சார்பற்ற தேர்தல் நடத்தப்படுகிறது.",
            "fact_en": "Political parties cannot officially field candidates or issue party whips for Village Panchayat elections.",
            "fact_ta": "கிராம ஊராட்சித் தேர்தல்களில் அரசியல் கட்சிகள் அதிகாரப்பூர்வமாக வேட்பாளர்களை நிறுத்தவோ அல்லது கொறடா உத்தரவு பிறப்பிக்கவோ முடியாது."
        },

        # 26. Criminal Antecedents Disclosure
        {
            "subtopic": "sec_powers_functions_elections",
            "stem_en": "To enforce transparency, what must contesting candidates in local body elections submit along with their nomination papers under SEC regulations?",
            "stem_ta": "வெளிப்படைத்தன்மையை உறுதி செய்வதற்காக, SEC விதிமுறைகளின்படி உள்ளாட்சித் தேர்தலில் போட்டியிடும் வேட்பாளர்கள் தங்கள் வேட்புமனுவுடன் எதனை சமர்ப்பிக்க வேண்டும்?",
            "options": [
                ("A sworn affidavit disclosing criminal antecedents, assets, liabilities, and educational qualifications", "குற்றப் பின்னணி, சொத்துக்கள், கடன்கள் மற்றும் கல்வித் தகுதிகளை வெளிப்படுத்தும் உறுதிமொழிப் பத்திரம்"),
                ("A solvency certificate from a commercial bank for at least Rs. 1 crore", "வணிக வங்கியிலிருந்து குறைந்தபட்சம் ரூ. 1 கோடிக்கான சொத்து மதிப்புச் சான்றிதழ்"),
                ("A recommendation letter signed by the sitting Member of Parliament", "பதவியில் உள்ள நாடாளுமன்ற உறுப்பினரால் கையொப்பமிடப்பட்ட பரிந்துரைக் கடிதம்"),
                ("A guarantee bond issued by the District Treasury Office", "மாவட்ட கருவூல அலுவலகத்தால் வழங்கப்பட்ட உத்தரவாதப் பத்திரம்")
            ],
            "correct_key": "A",
            "exp_en": "Following the Supreme Court rulings in Union of India v. ADR (2002) and PUCL (2003), State Election Commissions made it mandatory for all local election candidates to submit a sworn affidavit disclosing pending criminal charges, convictions, assets, liabilities, and educational qualifications.",
            "exp_ta": "ADR (2002) மற்றும் PUCL (2003) வழக்குகளில் உச்ச நீதிமன்றத் தீர்ப்புகளைத் தொடர்ந்து, உள்ளாட்சி வேட்பாளர்கள் அனைவரும் நிலுவையில் உள்ள குற்ற வழக்குகள், தண்டனைகள், சொத்துகள், கடன்கள் மற்றும் கல்வித் தகுதிகளை வெளிப்படுத்தும் உறுதிமொழிப் பத்திரத்தை சமர்ப்பிப்பதை மாநில தேர்தல் ஆணையங்கள் கட்டாயமாக்கின.",
            "why_a_en": "Correct. Affidavits disclosing criminal cases, assets, and education are constitutionally mandated.",
            "why_a_ta": "சரி. குற்ற வழக்குகள், சொத்துக்கள் மற்றும் கல்வியை வெளிப்படுத்தும் உறுதிமொழிப் பத்திரம் கட்டாயமாகும்.",
            "why_b_en": "Incorrect. No large commercial solvency certificate is required to contest.",
            "why_b_ta": "தவறு. போட்டியிட பெரிய அளவிலான வங்கி சொத்துச் சான்றிதழ் தேவையில்லை.",
            "why_c_en": "Incorrect. MP recommendations are not required.",
            "why_c_ta": "தவறு. எம்.பி.-யின் பரிந்துரை தேவையில்லை.",
            "why_d_en": "Incorrect. Treasury guarantee bonds are not required.",
            "why_d_ta": "தவறு. கருவூல உத்தரவாத பத்திரங்கள் தேவையில்லை.",
            "tip_en": "Failure to disclose or filing false affidavits can result in rejection of nominations or election voidance.",
            "tip_ta": "தகவல்களை மறைப்பது அல்லது தவறான உறுதிமொழிப் பத்திரம் தாக்கல் செய்வது வேட்புமனு நிராகரிப்புக்கு வழிவகுக்கும்.",
            "fact_en": "These affidavits are displayed on notice boards and published on the SEC portal for public scrutiny.",
            "fact_ta": "இந்த உறுதிமொழிப் பத்திரங்கள் பொதுமக்கள் பார்வைக்காக தகவல் பலகைகளிலும் SEC இணையதளத்திலும் வெளியிடப்படுகின்றன."
        },

        # 27. Appointment of Observers
        {
            "subtopic": "sec_powers_functions_elections",
            "stem_en": "Whom does the State Election Commission typically appoint as General Observers and Expenditure Observers to monitor field-level local body election conduct?",
            "stem_ta": "கள அளவில் உள்ளாட்சித் தேர்தல் நடத்தப்படுவதைக் கண்காணிக்க பொதுப் பார்வையாளர்களாகவும் தேர்தல் செலவுப் பார்வையாளர்களாகவும் மாநில தேர்தல் ஆணையம் பொதுவாக யாரை நியமிக்கிறது?",
            "options": [
                ("Senior Indian Administrative Service (IAS) and State Civil Service officers", "மூத்த இந்திய ஆட்சிப் பணி (IAS) மற்றும் மாநில அரசு சிவில் சர்வீஸ் அதிகாரிகள்"),
                ("Sitting ward members from neighbouring municipalities", "அண்டை நகராட்சிகளைச் சேர்ந்த பதவியில் உள்ள வார்டு உறுப்பினர்கள்"),
                ("Office bearers of the ruling political party", "ஆளும் அரசியல் கட்சியின் நிர்வாகிகள்"),
                ("Members of the State Legislative Assembly Committee on Petitions", "மாநில சட்டமன்ற மனுக்கள் குழுவின் உறுப்பினர்கள்")
            ],
            "correct_key": "A",
            "exp_en": "The State Election Commission appoints senior civil servants, including IAS officers and senior revenue officers, as General and Expenditure Observers to oversee polling booths, verify expenditure, and ensure free and fair elections.",
            "exp_ta": "வாக்குச்சாவடிகளைக் கண்காணிக்கவும், செலவுகளைச் சரிபார்க்கவும், சுதந்திரமான தேர்தலை உறுதி செய்யவும் மூத்த ஐ.ஏ.எஸ் அதிகாரிகள் மற்றும் மூத்த அதிகாரிகளை பொது மற்றும் செலவினப் பார்வையாளர்களாக மாநில தேர்தல் ஆணையம் நியமிக்கிறது.",
            "why_a_en": "Correct. Independent senior civil servants are deployed as observers.",
            "why_a_ta": "சரி. சுயேச்சையான மூத்த அரசு அதிகாரிகள் பார்வையாளர்களாக நியமிக்கப்படுகிறார்கள்.",
            "why_b_en": "Incorrect. Political ward members cannot act as neutral observers.",
            "why_b_ta": "தவறு. வார்டு உறுப்பினர்கள் நடுநிலைப் பார்வையாளர்களாக செயல்பட முடியாது.",
            "why_c_en": "Incorrect. Party office bearers would violate electoral neutrality.",
            "why_c_ta": "தவறு. ஆளும் கட்சியினர் பார்வையாளர்களாக செயல்பட முடியாது.",
            "why_d_en": "Incorrect. Legislative committees do not monitor polling stations.",
            "why_d_ta": "தவறு. சட்டமன்றக் குழுக்கள் வாக்குச்சாவடிகளைக் கண்காணிப்பதில்லை.",
            "tip_en": "Observers act as the eyes and ears of the State Election Commission during election campaigns.",
            "tip_ta": "தேர்தல் பிரச்சாரங்களின் போது பார்வையாளர்கள் மாநில தேர்தல் ஆணையத்தின் கண்களாகவும் காதுகளாகவும் செயல்படுகிறார்கள்.",
            "fact_en": "Observers report directly to the State Election Commissioner, bypassing the local district administration.",
            "fact_ta": "பார்வையாளர்கள் மாவட்ட நிர்வாகத்தைத் தவிர்த்து, நேரடியாக மாநில தேர்தல் ஆணையரிடம் அறிக்கை சமர்ப்பிக்கின்றனர்."
        },

        # 28. Electoral rolls revision cycle
        {
            "subtopic": "sec_powers_functions_elections",
            "stem_en": "What is the qualifying date for inclusion in the electoral roll for local body elections as aligned with Election Commission of India norms?",
            "stem_ta": "இந்திய தேர்தல் ஆணையத்தின் விதிகளுக்கு இணங்க, உள்ளாட்சித் தேர்தல்களுக்கான வாக்காளர் பட்டியலில் பெயர் சேர்ப்பதற்கான தகுதி நாள் எது?",
            "options": [
                ("1st of January (and subsequent quarterly qualifying dates: 1st April, 1st July, 1st October)", "ஜனவரி 1-ஆம் தேதி (மற்றும் காலாண்டு தகுதி தேதிகள்: ஏப்ரல் 1, ஜூலை 1, அக்டோபர் 1)"),
                ("Only 31st of December of an election year", "தேர்தல் ஆண்டின் டிசம்பர் 31 மட்டுமே"),
                ("The date on which the candidate files their nomination paper", "வேட்பாளர் தனது வேட்புமனுவை தாக்கல் செய்யும் தேதி"),
                ("15th of August of every alternate year", "ஒவ்வொரு மாற்று ஆண்டின் ஆகஸ்ட் 15-ஆம் தேதி")
            ],
            "correct_key": "A",
            "exp_en": "Following the 2022 amendments to election law, there are four qualifying dates in a calendar year (January 1, April 1, July 1, and October 1) for registration as an elector, with January 1 serving as the primary baseline date for annual revisions.",
            "exp_ta": "தேர்தல் சட்டத் திருத்தங்களைத் தொடர்ந்து, வாக்காளராகப் பதிவு செய்ய ஒரு காலண்டர் ஆண்டில் நான்கு தகுதி தேதிகள் (ஜனவரி 1, ஏப்ரல் 1, ஜூலை 1 மற்றும் அக்டோபர் 1) உள்ளன; இதில் ஜனவரி 1 முதன்மை தகுதித் தேதியாகும்.",
            "why_a_en": "Correct. January 1st is the standard qualifying date along with quarterly additions.",
            "why_a_ta": "சரி. ஜனவரி 1 நிலையான தகுதி தேதியாகும், மேலும் காலாண்டு தேதிகளும் உள்ளன.",
            "why_b_en": "Incorrect. December 31 is not the qualifying cutoff date.",
            "why_b_ta": "தவறு. டிசம்பர் 31 தகுதி நாளாகப் பயன்படுவதில்லை.",
            "why_c_en": "Incorrect. Qualifying date relates to age qualification (18 years), not nomination date.",
            "why_c_ta": "தவறு. தகுதி தேதி என்பது வயது தகுதியைக் குறிக்கும் (18 வயது), வேட்புமனு தேதியை அல்ல.",
            "why_d_en": "Incorrect. August 15 is Independence Day, not an electoral cutoff date.",
            "why_d_ta": "தவறு. ஆகஸ்ட் 15 சுதந்திர தினம், வாக்காளர் தகுதி நாள் அல்ல.",
            "tip_en": "A citizen must be at least 18 years of age on the qualifying date to be registered as a voter.",
            "tip_ta": "வாக்காளராகப் பதிவு செய்ய தகுதி நாளன்று ஒரு குடிமகனுக்கு குறைந்தபட்சம் 18 வயது பூர்த்தியாகியிருக்க வேண்டும்.",
            "fact_en": "Prior to 2022, January 1 was the sole qualifying date in each calendar year.",
            "fact_ta": "2022-க்கு முன்பு, ஒவ்வொரு காலண்டர் ஆண்டிலும் ஜனவரி 1 மட்டுமே ஒரே தகுதி நாளாக இருந்தது."
        },

        # 29. Casual vacancies in local bodies
        {
            "subtopic": "sec_powers_functions_elections",
            "stem_en": "When a casual vacancy occurs in the office of a Panchayat or Municipality ward member due to death or resignation, within what timeframe must the bye-election be held under statutory rules?",
            "stem_ta": "இறப்பு அல்லது ராஜினாமா காரணமாக ஒரு ஊராட்சி அல்லது நகராட்சி வார்டு உறுப்பினர் பதவியில் எதிர்பாராத காலியிடம் ஏற்பட்டால், சட்ட விதிகளின்படி இடைத்தேர்தல் எத்தனை மாதங்களுக்குள் நடத்தப்பட வேண்டும்?",
            "options": [
                ("Within six months from the date of occurrence of the vacancy", "காலியிடம் ஏற்பட்ட தேதியிலிருந்து ஆறு மாதங்களுக்குள்"),
                ("Within two years from the vacancy date", "காலியான தேதியிலிருந்து இரண்டு ஆண்டுகளுக்குள்"),
                ("At the end of the full five-year term along with general elections", "பொதுத் தேர்தலுடன் சேர்த்து முழு ஐந்தாண்டு காலத்தின் முடிவில்"),
                ("Whenever the District Collector issues an administrative clearance", "மாவட்ட ஆட்சித்தலைவர் நிர்வாக அனுமதி வழங்கும் போதெல்லாம்")
            ],
            "correct_key": "A",
            "exp_en": "Under the Tamil Nadu Panchayats Act and local body laws, a bye-election to fill a casual vacancy must be conducted within six months from the date of occurrence of the vacancy, provided the remainder of the term is not less than six months.",
            "exp_ta": "தமிழ்நாடு ஊராட்சிகள் சட்டம் மற்றும் உள்ளாட்சி விதிகளின்படி, பதவிக்காலம் முடிவடைய 6 மாதங்களுக்கு மேல் இருக்கும் பட்சத்தில், காலியிடம் ஏற்பட்ட தேதியிலிருந்து ஆறு மாதங்களுக்குள் இடைத்தேர்தல் நடத்தப்பட வேண்டும்.",
            "why_a_en": "Correct. Six months is the universal statutory deadline for filling casual vacancies.",
            "why_a_ta": "சரி. காலியிடங்களை நிரப்புவதற்கான உலகளாவிய காலக்கெடு ஆறு மாதங்கள் ஆகும்.",
            "why_b_en": "Incorrect. Two years is an unconstitutional delay.",
            "why_b_ta": "தவறு. இரண்டு ஆண்டுகள் என்பது அனுமதிக்க முடியாத தாமதமாகும்.",
            "why_c_en": "Incorrect. Vacancies cannot be kept unfilled until general polls if more than 6 months remain.",
            "why_c_ta": "தவறு. 6 மாதங்களுக்கு மேல் பதவிக்காலம் இருக்கும் போது நிரப்பாமல் வைத்திருக்க முடியாது.",
            "why_d_en": "Incorrect. Collector cannot arbitrarily postpone bye-elections.",
            "why_d_ta": "தவறு. மாவட்ட ஆட்சியர் தன்னிச்சையாக இடைத்தேர்தலை ஒத்திவைக்க முடியாது.",
            "tip_en": "Proviso exception: If the remainder of the term is less than six months, no bye-election is held.",
            "tip_ta": "விதிவிலக்கு: எஞ்சியிருக்கும் பதவிக்காலம் ஆறு மாதங்களுக்கும் குறைவாக இருந்தால் இடைத்தேர்தல் நடத்தப்படுவதில்லை.",
            "fact_en": "A member elected to fill a casual vacancy holds office only for the remainder of the term.",
            "fact_ta": "இடைத்தேர்தலில் தேர்ந்தெடுக்கப்படும் உறுப்பினர் எஞ்சியிருக்கும் காலத்திற்கு மட்டுமே பதவியில் இருப்பார்."
        },

        # 30. Requisitioning of Premises and Vehicles
        {
            "subtopic": "sec_powers_functions_elections",
            "stem_en": "Under state local body election laws, which public authority is empowered to requisition schools, public buildings, and vehicles for polling stations and transport?",
            "stem_ta": "மாநில உள்ளாட்சித் தேர்தல் சட்டங்களின்படி, வாக்குச்சாவடிகள் மற்றும் போக்குவரத்திற்காக பள்ளிகள், பொதுக் கட்டடங்கள் மற்றும் வாகனங்களைக் கையகப்படுத்த எந்த அதிகாரம் படைத்தவருக்கு அதிகாரம் உள்ளது?",
            "options": [
                ("District Election Officer / District Collector under powers delegated by SEC", "மாநில தேர்தல் ஆணையத்தால் அதிகாரமளிக்கப்பட்ட மாவட்ட தேர்தல் அதிகாரி / மாவட்ட ஆட்சித்தலைவர்"),
                ("President of the local Parent-Teacher Association", "உள்ளூர் பெற்றோர் ஆசிரியர் கழகத்தின் தலைவர்"),
                ("Regional Transport Officer acting independently", "சுயேச்சையாக செயல்படும் வட்டாரப் போக்குவரத்து அலுவலர்"),
                ("Executive Engineer of Public Works Department", "பொதுப்பணித்துறை செயற்பொறியாளர்")
            ],
            "correct_key": "A",
            "exp_en": "Under the Tamil Nadu Panchayats Act and Municipal laws, the District Election Officer (District Collector), acting under the superintendence of the State Election Commission, is empowered to requisition premises, educational institutions, and transport vehicles for conduct of polls.",
            "exp_ta": "மாநிலத் தேர்தல் ஆணையத்தின் மேற்பார்வையின் கீழ் செயல்படும் மாவட்ட தேர்தல் அதிகாரி (மாவட்ட ஆட்சித்தலைவர்), தேர்தல் நடத்துவதற்காக பள்ளிகள், கட்டடங்கள் மற்றும் வாகனங்களைக் கையகப்படுத்த அதிகாரம் பெற்றுள்ளார்.",
            "why_a_en": "Correct. District Collector / DEO exercises statutory requisitioning powers under SEC oversight.",
            "why_a_ta": "சரி. SEC மேற்பார்வையில் மாவட்ட தேர்தல் அதிகாரி/ஆட்சியர் இத்தகைய அதிகாரங்களைப் பயன்படுத்துகிறார்.",
            "why_b_en": "Incorrect. PTA presidents have no statutory administrative authority.",
            "why_b_ta": "தவறு. பெற்றோர் ஆசிரியர் கழகத் தலைவருக்கு சட்டப்பூர்வ அதிகாரம் இல்லை.",
            "why_c_en": "Incorrect. RTO assists the Collector, but cannot independently requisition buildings.",
            "why_c_ta": "தவறு. RTO மாவட்ட ஆட்சியருக்கு உதவுகிறார், தானாக கையகப்படுத்த முடியாது.",
            "why_d_en": "Incorrect. PWD engineers provide infrastructure maintenance, not requisition orders.",
            "why_d_ta": "தவறு. பொதுப்பணித்துறை பொறியாளர்கள் கட்டடப் பராமரிப்பை மட்டுமே செய்கின்றனர்.",
            "tip_en": "Reasonable compensation must be paid for requisitioned private vehicles and premises.",
            "tip_ta": "கையகப்படுத்தப்படும் தனியார் வாகனங்கள் மற்றும் வளாகங்களுக்கு நியாயமான இழப்பீடு வழங்கப்பட வேண்டும்.",
            "fact_en": "Places of religious worship cannot be requisitioned as polling stations.",
            "fact_ta": "மத வழிபாட்டுத் தலங்களை வாக்குச்சாவடிகளாக கையகப்படுத்த முடியாது."
        },

        # 31. State Finance Commission - Constitutional Article 243-I
        {
            "subtopic": "sfc_constitutional_provisions_composition",
            "stem_en": "Under Article 243-I(1), who is constitutionally mandated to constitute a State Finance Commission at the expiration of every fifth year?",
            "stem_ta": "சரத்து 243-I(1)-ன் கீழ், ஒவ்வொரு ஐந்தாவது ஆண்டின் முடிவிலும் மாநில நிதி ஆணையத்தை அமைக்க அரசியலமைப்பு ரீதியாக கடமைப்பட்டுள்ளவர் யார்?",
            "options": [
                ("The Governor of the State", "மாநில ஆளுநர்"),
                ("The Chief Minister of the State", "மாநில முதலமைச்சர்"),
                ("The Speaker of the Legislative Assembly", "சட்டமன்றப் பேரவைத் தலைவர்"),
                ("The Comptroller and Auditor General of India", "இந்தியக் தலைமைத் தணிக்கையாளர் (CAG)")
            ],
            "correct_key": "A",
            "exp_en": "Article 243-I(1) mandates that the Governor of a State shall, as soon as may be within one year from the commencement of the Constitution (73rd Amendment) Act, 1992, and thereafter at the expiration of every fifth year, constitute a Finance Commission to review the financial position of the Panchayats.",
            "exp_ta": "சரத்து 243-I(1)-ன் படி, ஊராட்சிகளின் நிதி நிலையை மறுஆய்வு செய்வதற்காக, 73-வது திருத்தச் சட்டம் அமலுக்கு வந்த ஒரு வருடத்திற்குள்ளும், அதன் பிறகு ஒவ்வொரு ஐந்தாவது ஆண்டின் முடிவிலும் மாநில ஆளுநர் நிதி ஆணையத்தை அமைக்க வேண்டும்.",
            "why_a_en": "Correct. Article 243-I(1) expressly places this duty upon the Governor of the State.",
            "why_a_ta": "சரி. சரத்து 243-I(1) இந்த கடமையை மாநில ஆளுநர் மீது வெளிப்படையாக விதிக்கிறது.",
            "why_b_en": "Incorrect. Chief Minister heads the Council of Ministers which advises the Governor, but the constitutional power vests in the Governor.",
            "why_b_ta": "தவறு. முதலமைச்சர் ஆலோசனை வழங்குகிறார், ஆனால் அதிகாரம் ஆளுநரிடம் உள்ளது.",
            "why_c_en": "Incorrect. The Speaker does not constitute finance commissions.",
            "why_c_ta": "தவறு. சபாநாயகர் நிதி ஆணையத்தை அமைப்பதில்லை.",
            "why_d_en": "Incorrect. CAG audits accounts, does not constitute state finance commissions.",
            "why_d_ta": "தவறு. சி.ஏ.ஜி தணிக்கை செய்கிறது, ஆணையங்களை அமைப்பதில்லை.",
            "tip_en": "Panchayat finance = Article 243-I; Municipality finance = Article 243Y (both constituted by the Governor).",
            "tip_ta": "ஊராட்சி நிதி = சரத்து 243-I; நகராட்சி நிதி = சரத்து 243Y (இரண்டும் ஆளுநரால் அமைக்கப்படுகின்றன).",
            "fact_en": "Article 243-I mirrors Article 280 under which the President constitutes the Central Finance Commission every 5 years.",
            "fact_ta": "சரத்து 243-I, குடியரசுத் தலைவர் மத்திய நிதி ஆணையத்தை 5 ஆண்டுகளுக்கு ஒருமுறை அமைக்கும் சரத்து 280-ஐ ஒத்துள்ளது."
        },

        # 32. Article 243Y and Municipalities
        {
            "subtopic": "sfc_constitutional_provisions_composition",
            "stem_en": "Which article of the Indian Constitution provides that the State Finance Commission constituted under Article 243-I shall also review the financial position of Municipalities?",
            "stem_ta": "சரத்து 243-I-ன் கீழ் அமைக்கப்பட்ட மாநில நிதி ஆணையம் நகராட்சிகளின் நிதி நிலையையும் மறுஆய்வு செய்ய வேண்டும் என்று கூறும் இந்திய அரசியலமைப்பின் சரத்து எது?",
            "options": [
                ("Article 243Y", "சரத்து 243Y"),
                ("Article 243X", "சரத்து 243X"),
                ("Article 243W", "சரத்து 243W"),
                ("Article 243Z", "சரத்து 243Z")
            ],
            "correct_key": "A",
            "exp_en": "Article 243Y(1) states that the Finance Commission constituted under Article 243-I shall also review the financial position of the Municipalities and make recommendations to the Governor.",
            "exp_ta": "சரத்து 243Y(1)-ன் படி, சரத்து 243-I-ன் கீழ் அமைக்கப்பட்ட நிதி ஆணையமானது நகராட்சிகளின் நிதி நிலையையும் மறுஆய்வு செய்து ஆளுநருக்குப் பரிந்துரைகளை வழங்க வேண்டும்.",
            "why_a_en": "Correct. Article 243Y extends SFC purview to Municipalities.",
            "why_a_ta": "சரி. சரத்து 243Y நகராட்சிகளுக்கும் மாநில நிதி ஆணையத்தின் அதிகார வரம்பை விரிவுபடுத்துகிறது.",
            "why_b_en": "Incorrect. Article 243X deals with power of Municipalities to impose taxes and funds.",
            "why_b_ta": "தவறு. சரத்து 243X நகராட்சிகள் வரி விதிக்கும் அதிகாரம் பற்றியது.",
            "why_c_en": "Incorrect. Article 243W deals with powers, authority, and responsibilities of Municipalities.",
            "why_c_ta": "தவறு. சரத்து 243W நகராட்சிகளின் பணிகள் மற்றும் பொறுப்புகள் பற்றியது.",
            "why_d_en": "Incorrect. Article 243Z deals with audit of accounts of Municipalities.",
            "why_d_ta": "தவறு. சரத்து 243Z நகராட்சிகளின் கணக்குகள் தணிக்கை பற்றியது.",
            "tip_en": "Panchayat SFC = 243-I; Municipality SFC = 243Y. There is only ONE State Finance Commission covering both.",
            "tip_ta": "ஊராட்சி SFC = 243-I; நகராட்சி SFC = 243Y. இரண்டையும் உள்ளடக்கிய ஒரே மாநில நிதி ஆணையமே செயல்படுகிறது.",
            "fact_en": "Both rural and urban local bodies submit their financial memoranda to the same State Finance Commission.",
            "fact_ta": "ஊரக மற்றும் நகர்ப்புற உள்ளாட்சி அமைப்புகள் இரண்டும் ஒரே மாநில நிதி ஆணையத்திடமே தங்கள் நிதி நிலை மனுக்களை அளிக்கின்றன."
        },

        # 33. Composition and Qualifications determined by State Legislature
        {
            "subtopic": "sfc_constitutional_provisions_composition",
            "stem_en": "Under Article 243-I(2), which organ is empowered to determine the composition of the State Finance Commission, qualifications of members, and manner of selection?",
            "stem_ta": "சரத்து 243-I(2)-ன் கீழ், மாநில நிதி ஆணையத்தின் கட்டமைப்பு, உறுப்பினர்களின் தகுதிகள் மற்றும் அவர்கள் தேர்ந்தெடுக்கப்படும் முறையை நிர்ணயிக்க அதிகாரம் பெற்றுள்ள அமைப்பு எது?",
            "options": [
                ("The Legislature of the State by law", "சட்டத்தின் மூலம் மாநில சட்டமன்றம்"),
                ("The Union Parliament by a constitutional amendment", "அரசியலமைப்பு திருத்தத்தின் மூலம் மத்திய பாராளுமன்றம்"),
                ("The Union Ministry of Finance by a gazette notification", "அரசிதழ் அறிவிப்பின் மூலம் மத்திய நிதி அமைச்சகம்"),
                ("The Central Finance Commission by general guidelines", "பொது வழிகாட்டுதல்கள் மூலம் மத்திய நிதி ஆணையம்")
            ],
            "correct_key": "A",
            "exp_en": "Article 243-I(2) provides: 'The Legislature of a State may, by law, provide for the composition of the Commission, the qualifications which shall be requisite for appointment as members thereof and the manner in which they shall be selected.'",
            "exp_ta": "சரத்து 243-I(2) கூறுகிறது: 'மாநில சட்டமன்றம் சட்டத்தின் மூலம், ஆணைக்குழுவின் கலவை, அதன் உறுப்பினர்களாக நியமிக்கப்படுவதற்குத் தேவையான தகுதிகள் மற்றும் அவர்கள் தேர்ந்தெடுக்கப்படும் முறை ஆகியவற்றை வழங்கலாம்.'",
            "why_a_en": "Correct. State Legislature has the exclusive constitutional power under Article 243-I(2).",
            "why_a_ta": "சரி. சரத்து 243-I(2)-ன் கீழ் மாநில சட்டமன்றத்திற்கு பிரத்யேக அதிகாரம் உள்ளது.",
            "why_b_en": "Incorrect. Parliament does not frame state-specific SFC member qualifications.",
            "why_b_ta": "தவறு. பாராளுமன்றம் மாநில SFC உறுப்பினர்களின் தகுதிகளை நிர்ணயிப்பதில்லை.",
            "why_c_en": "Incorrect. Union Ministry of Finance has no direct administrative control over SFC setup.",
            "why_c_ta": "தவறு. மத்திய நிதி அமைச்சகத்திற்கு நேரடி நிர்வாகக் கட்டுப்பாடு இல்லை.",
            "why_d_en": "Incorrect. Central Finance Commission receives recommendations, but does not prescribe state laws.",
            "why_d_ta": "தவறு. மத்திய நிதி ஆணையம் மாநிலச் சட்டங்களை இயற்றுவதில்லை.",
            "tip_en": "Compare Article 280(2): Parliament determines Central FC qualifications; Article 243-I(2): State Legislature determines State FC qualifications.",
            "tip_ta": "ஒப்பிடுக: மத்திய நிதி ஆணைய தகுதியை பாராளுமன்றம் (280(2)) தீர்மானிக்கிறது; மாநில நிதி ஆணைய தகுதியை மாநில சட்டமன்றம் (243-I(2)) தீர்மானிக்கிறது.",
            "fact_en": "Typically, an SFC comprises a Chairman and 2 to 4 members drawn from public administration, finance, and economics.",
            "fact_ta": "பொதுவாக, SFC ஒரு தலைவர் மற்றும் பொது நிர்வாகம், நிதி மற்றும் பொருளாதாரத் துறையைச் சேர்ந்த 2 முதல் 4 உறுப்பினர்களைக் கொண்டுள்ளது."
        },

        # 34. Tabling of SFC recommendations
        {
            "subtopic": "sfc_constitutional_provisions_composition",
            "stem_en": "What must the Governor do with the recommendations made by the State Finance Commission under Article 243-I(4) and Article 243Y(2)?",
            "stem_ta": "சரத்து 243-I(4) மற்றும் சரத்து 243Y(2)-ன் கீழ் மாநில நிதி ஆணையம் அளிக்கும் பரிந்துரைகளை ஆளுநர் என்ன செய்ய வேண்டும்?",
            "options": [
                ("Cause every recommendation together with an explanatory memorandum of action taken to be laid before the State Legislature", "ஒவ்வொரு பரிந்துரையையும் அதன் மீது எடுக்கப்பட்ட நடவடிக்கை குறித்த விளக்கக் குறிப்புடன் மாநில சட்டமன்றத்தின் முன் வைக்க வேண்டும்"),
                ("Forward it secretly to the Reserve Bank of India without publishing", "வெளியிடாமல் ரகசியமாக இந்திய ரிசர்வ் வங்கிக்கு அனுப்ப வேண்டும்"),
                ("Implement the financial transfers directly through executive decrees without legislative debate", "சட்டமன்ற விவாதமின்றி நிர்வாக உத்தரவுகள் மூலம் நிதிப் பகிர்வை நேரடியாகச் செயல்படுத்த வேண்டும்"),
                ("Submit the report to the Union Cabinet for prior approval before state presentation", "மாநிலத்தில் சமர்ப்பிப்பதற்கு முன் மத்திய அமைச்சரவையின் ஒப்புதலுக்காக அனுப்ப வேண்டும்")
            ],
            "correct_key": "A",
            "exp_en": "Article 243-I(4) mandates that the Governor shall cause every recommendation made by the Commission together with an explanatory memorandum as to the action taken thereon to be laid before the Legislature of the State.",
            "exp_ta": "சரத்து 243-I(4)-ன் படி, ஆணைக்குழு அளித்த ஒவ்வொரு பரிந்துரையையும், அதன் மீது எடுக்கப்பட்ட நடவடிக்கை குறித்த விளக்கக் குறிப்புடன் (Action Taken Memorandum) மாநில சட்டமன்றத்தின் முன் ஆளுநர் வைக்கச் செய்ய வேண்டும்.",
            "why_a_en": "Correct. Tabling the report with the Action Taken Memorandum (ATM) before the State Legislature is constitutionally mandatory.",
            "why_a_ta": "சரி. நடவடிக்கை எடுக்கப்பட்ட விளக்கக் குறிப்புடன் சட்டமன்றத்தில் அறிக்கையை வைப்பது கட்டாயமாகும்.",
            "why_b_en": "Incorrect. SFC reports are public legislative documents, not secret RBI reports.",
            "why_b_ta": "தவறு. SFC அறிக்கைகள் சட்டமன்றத்தின் பொது ஆவணங்கள், ரகசிய ஆவணங்கள் அல்ல.",
            "why_c_en": "Incorrect. Democratic accountability requires tabling and legislative scrutiny.",
            "why_c_ta": "தவறு. ஜனநாயகப் பொறுப்புடைமைக்கு சட்டமன்றப் பரிசீலனை அவசியமாகும்.",
            "why_d_en": "Incorrect. No Union Cabinet clearance is required for State Finance Commission reports.",
            "why_d_ta": "தவறு. மத்திய அமைச்சரவையின் முன் அனுமதி தேவையில்லை.",
            "tip_en": "Action Taken Memorandum (ATM) explains which recommendations are accepted, rejected, or modified.",
            "tip_ta": "நடவடிக்கைக் குறிப்பு (ATM) எந்தெந்தப் பரிந்துரைகள் ஏற்கப்பட்டன, நிராகரிக்கப்பட்டன அல்லது மாற்றப்பட்டன என்பதை விளக்குகிறது.",
            "fact_en": "This mirrors Article 281 under which the President causes Central FC reports to be laid before Parliament.",
            "fact_ta": "இது குடியரசுத் தலைவர் மத்திய நிதி ஆணைய அறிக்கையை பாராளுமன்றத்தில் வைக்கும் சரத்து 281-ஐ ஒத்துள்ளது."
        },

        # 35. Core functions under 243-I(1)(a) - Distribution of net proceeds
        {
            "subtopic": "sfc_functions_devolution_recommendations",
            "stem_en": "Under Article 243-I(1)(a)(i), what primary financial distribution is recommended by the State Finance Commission?",
            "stem_ta": "சரத்து 243-I(1)(a)(i)-ன் கீழ், மாநில நிதி ஆணையத்தால் பரிந்துரைக்கப்படும் முதன்மையான நிதிப் பகிர்வு எது?",
            "options": [
                ("Distribution between the State and the Panchayats of the net proceeds of taxes, duties, tolls, and fees leviable by the State", "மாநிலத்தால் விதிக்கப்படக்கூடிய வரிகள், சுங்கங்கள் மற்றும் கட்டணங்களின் நிகர வருவாயை மாநிலத்திற்கும் ஊராட்சிகளுக்கும் இடையே பகிர்ந்தளித்தல்"),
                ("Sharing of central corporate income tax between Union and Panchayats", "மத்திய கார்ப்பரேட் வருமான வரியை மத்திய அரசுக்கும் ஊராட்சிகளுக்கும் இடையே பகிர்ந்தளித்தல்"),
                ("Allocation of customs duties among coastal district panchayats", "கடலோர மாவட்ட ஊராட்சிகளுக்கு இடையே சுங்க வரியை ஒதுக்கீடு செய்தல்"),
                ("Apportionment of foreign loans received by the Union Government", "மத்திய அரசு பெறும் வெளிநாட்டுக் கடன்களைப் பங்கிடுதல்")
            ],
            "correct_key": "A",
            "exp_en": "Article 243-I(1)(a)(i) requires the SFC to recommend the distribution between the State and the Panchayats of the net proceeds of the taxes, duties, tolls, and fees leviable by the State which may be divided between them and the allocation between the Panchayats at all levels of their respective shares.",
            "exp_ta": "சரத்து 243-I(1)(a)(i)-ன் படி, மாநிலத்தால் விதிக்கப்படும் வரிகள், சுங்கங்கள் மற்றும் கட்டணங்களின் நிகர வருவாயை மாநிலத்திற்கும் ஊராட்சிகளுக்கும் இடையே பகிர்ந்தளிப்பதற்கும், அனைத்து நிலை ஊராட்சிகளுக்கும் இடையே அதனைப் பங்கீடு செய்வதற்கும் SFC பரிந்துரைக்க வேண்டும்.",
            "why_a_en": "Correct. Vertical and horizontal devolution of state tax proceeds is the core SFC mandate.",
            "why_a_ta": "சரி. மாநில வரி வருவாயை செங்குத்தாகவும் கிடைமட்டமாகவும் பகிர்ந்தளிப்பதே SFC-ன் முதன்மைப் பணியாகும்.",
            "why_b_en": "Incorrect. Central taxes are devolved by Central FC under Article 270/280, not SFC.",
            "why_b_ta": "தவறு. மத்திய வரிகள் மத்திய நிதி ஆணையத்தால் (280) பகிரப்படுகின்றன, SFC அல்ல.",
            "why_c_en": "Incorrect. Customs duty belongs exclusively to the Union List.",
            "why_c_ta": "தவறு. சுங்க வரி மத்திய பட்டியலுக்கு மட்டுமே உரியது.",
            "why_d_en": "Incorrect. External loans are outside state legislative purview.",
            "why_d_ta": "தவறு. வெளிநாட்டுக் கடன்கள் மாநில வரம்பிற்கு அப்பாற்பட்டவை.",
            "tip_en": "Two dimensions of sharing: Vertical (State vs Local Bodies) and Horizontal (among Panchayats/Municipalities at all tiers).",
            "tip_ta": "பகிர்வின் இரண்டு பரிமாணங்கள்: செங்குத்துப் பகிர்வு (மாநிலம் vs உள்ளாட்சி) மற்றும் கிடைமட்டப் பகிர்வு (பல்வேறு உள்ளாட்சி அடுக்குகளுக்குள்).",
            "fact_en": "In Tamil Nadu, the divisible pool is formed out of the State's Own Tax Revenue (SOTR).",
            "fact_ta": "தமிழ்நாட்டில், மாநிலத்தின் சொந்த வரி வருவாயிலிருந்து (SOTR) பகிர்வு நிதி உருவாக்கப்படுகிறது."
        },

        # 36. Assignment of taxes under 243-I(1)(a)(ii)
        {
            "subtopic": "sfc_functions_devolution_recommendations",
            "stem_en": "Under Article 243-I(1)(a)(ii), what recommendation does the State Finance Commission make regarding local taxation powers?",
            "stem_ta": "சரத்து 243-I(1)(a)(ii)-ன் கீழ், உள்ளாட்சி அமைப்புகளின் வரி விதிப்பு அதிகாரங்கள் தொடர்பாக மாநில நிதி ஆணையம் என்ன பரிந்துரையை செய்கிறது?",
            "options": [
                ("Determination of the taxes, duties, tolls, and fees which may be assigned to, or appropriated by, the Panchayats", "ஊராட்சிகளுக்கு ஒதுக்கப்படக்கூடிய அல்லது அவற்றால் பயன்படுத்தப்படக்கூடிய வரிகள், சுங்கங்கள் மற்றும் கட்டணங்களை நிர்ணயித்தல்"),
                ("Abolition of all property taxes across all rural panchayats", "அனைத்து கிராம ஊராட்சிகளிலும் உள்ள அனைத்து சொத்து வரிகளையும் ரத்து செய்தல்"),
                ("Conversion of local professional tax into a central excise duty", "உள்ளூர் தொழில் வரியை மத்திய கலால் வரியாக மாற்றுதல்"),
                ("Transfer of all municipal taxation powers to private collection agencies", "அனைத்து நகராட்சி வரி அதிகாரங்களையும் தனியார் வசூல் முகமைகளுக்கு மாற்றுதல்")
            ],
            "correct_key": "A",
            "exp_en": "Article 243-I(1)(a)(ii) provides that the Commission shall recommend the determination of the taxes, duties, tolls, and fees which may be assigned to, or appropriated by, the Panchayats.",
            "exp_ta": "சரத்து 243-I(1)(a)(ii)-ன் படி, ஊராட்சிகளுக்கு ஒதுக்கப்படக்கூடிய அல்லது அவற்றால் வசூலித்து பயன்படுத்தப்படக்கூடிய வரிகள், சுங்கங்கள் மற்றும் கட்டணங்களை நிர்ணயிப்பது குறித்து ஆணையம் பரிந்துரைக்க வேண்டும்.",
            "why_a_en": "Correct. Determining assigned and appropriated taxes is explicitly covered under 243-I(1)(a)(ii).",
            "why_a_ta": "சரி. ஒதுக்கப்படும் மற்றும் பயன்படுத்தப்படும் வரிகளை நிர்ணயிப்பது 243-I(1)(a)(ii)-ன் கீழ் வருகிறது.",
            "why_b_en": "Incorrect. House tax/property tax is the mainstay of local revenue, not abolished.",
            "why_b_ta": "தவறு. சொத்து வரி உள்ளாட்சியின் முக்கிய வருவாய், அது ரத்து செய்யப்படுவதில்லை.",
            "why_c_en": "Incorrect. Profession tax is a state/local tax under Article 276, not central excise.",
            "why_c_ta": "தவறு. தொழில் வரி என்பது சரத்து 276-ன் கீழ் உள்ள மாநில/உள்ளாட்சி வரி.",
            "why_d_en": "Incorrect. Sovereign taxation powers cannot be abdicated to private entities.",
            "why_d_ta": "தவறு. இறையாண்மை வரி அதிகாரங்களை தனியாருக்கு தாரைவார்க்க முடியாது.",
            "tip_en": "Assigned taxes in TN include Surcharge on Stamp Duty and Local Cess/Local Cess Surcharge.",
            "tip_ta": "தமிழ்நாட்டில் ஒதுக்கப்படும் வரிகளில் முத்திரைத்தாள் கூடுதல் கட்டணம் மற்றும் உள்ளூர் செஸ் ஆகியவை அடங்கும்.",
            "fact_en": "Appropriated taxes are those collected by the local body itself and retained for its own expenditures.",
            "fact_ta": "பயன்படுத்தப்படும் வரிகள் என்பது உள்ளாட்சி அமைப்பாலேயே வசூலிக்கப்பட்டு அதன் சொந்த செலவுகளுக்குப் பயன்படுத்தப்படுபவை."
        },

        # 37. Grants-in-aid under 243-I(1)(a)(iii)
        {
            "subtopic": "sfc_functions_devolution_recommendations",
            "stem_en": "From which public fund are grants-in-aid recommended by the State Finance Commission to be paid to Panchayats and Municipalities?",
            "stem_ta": "மாநில நிதி ஆணையத்தின் பரிந்துரையின் பேரில் ஊராட்சிகளுக்கும் நகராட்சிகளுக்கும் எந்தப் பொது நிதியிலிருந்து மானியங்கள் (Grants-in-aid) வழங்கப்படுகின்றன?",
            "options": [
                ("The Consolidated Fund of the State", "மாநிலத்தின் தொகுப்பு நிதி (Consolidated Fund of the State)"),
                ("The Contingency Fund of India", "இந்திய அவசரக்கால நிதி"),
                ("The Prime Minister's National Relief Fund", "பிரதமரின் தேசிய நிவாரண நிதி"),
                ("The Public Account of the Union Government", "மத்திய அரசின் பொதுக் கணக்கு நிதி")
            ],
            "correct_key": "A",
            "exp_en": "Under Article 243-I(1)(a)(iii), the State Finance Commission recommends the grants-in-aid to the Panchayats from the Consolidated Fund of the State. Article 243Y applies the same for Municipalities.",
            "exp_ta": "சரத்து 243-I(1)(a)(iii)-ன் கீழ், மாநிலத்தின் தொகுப்பு நிதியிலிருந்து ஊராட்சிகளுக்கு வழங்கப்படும் மானியங்கள் குறித்து மாநில நிதி ஆணையம் பரிந்துரைக்கிறது. சரத்து 243Y நகராட்சிகளுக்கும் இதையே உறுதி செய்கிறது.",
            "why_a_en": "Correct. Grants-in-aid to local bodies are paid out of the Consolidated Fund of the State.",
            "why_a_ta": "சரி. உள்ளாட்சிகளுக்கான மானியங்கள் மாநிலத் தொகுப்பு நிதியிலிருந்தே வழங்கப்படுகின்றன.",
            "why_b_en": "Incorrect. Contingency Fund of India is for unforeseen central emergencies under Article 267(1).",
            "why_b_ta": "தவறு. இந்திய அவசரக்கால நிதி மத்திய அரசின் எதிர்பாராத அவசரச் செலவுகளுக்கானது.",
            "why_c_en": "Incorrect. PMNRF is a charitable trust fund, not a statutory devolution mechanism.",
            "why_c_ta": "தவறு. PMNRF என்பது ஒரு அறக்கட்டளை நிதி, சட்டப்பூர்வ நிதிப் பகிர்வு அல்ல.",
            "why_d_en": "Incorrect. State local grants do not flow from the Union Public Account.",
            "why_d_ta": "தவறு. மாநில உள்ளாட்சி மானியங்கள் மத்திய பொதுக் கணக்கிலிருந்து வழங்கப்படுவதில்லை.",
            "tip_en": "Grants bridge the fiscal gap between local revenue collection capacity and essential service delivery costs.",
            "tip_ta": "உள்ளாட்சியின் வருவாய் வசூல் திறனுக்கும் அத்தியாவசிய சேவைச் செலவுகளுக்கும் இடையிலான இடைவெளியை மானியங்கள் நிரப்புகின்றன.",
            "fact_en": "Grants can be untied (general purpose) or tied (specific sectors like water supply and sanitation).",
            "fact_ta": "மானியங்கள் நிபந்தனையற்றவையாகவோ அல்லது குறிப்பிட்ட துறைகளுக்கான (குடிநீர், சுகாதாரம்) நிபந்தனைக்குட்பட்டவையாகவோ இருக்கலாம்."
        },

        # 38. Article 280(3)(bb) & 280(3)(c) Linkage
        {
            "subtopic": "inter_relations_local_bodies_cag_audit",
            "stem_en": "How are the recommendations of the State Finance Commission linked to the Central Finance Commission under Article 280(3)(bb) and Article 280(3)(c)?",
            "stem_ta": "சரத்து 280(3)(bb) மற்றும் 280(3)(c)-ன் கீழ் மாநில நிதி ஆணையத்தின் பரிந்துரைகள் மத்திய நிதி ஆணையத்துடன் எவ்வாறு இணைக்கப்பட்டுள்ளன?",
            "options": [
                ("Central FC recommends measures to augment the Consolidated Fund of a State to supplement local resources on the basis of SFC recommendations", "மாநில நிதி ஆணையத்தின் பரிந்துரைகளின் அடிப்படையில் உள்ளாட்சி வளங்களுக்கு துணைபுரிய மாநிலத் தொகுப்பு நிதியை அதிகரிப்பதற்கான நடவடிக்கைகளை மத்திய நிதி ஆணையம் பரிந்துரைக்கிறது"),
                ("State FC reports are directly vetted and approved by the Comptroller and Auditor General", "மாநில நிதி ஆணைய அறிக்கைகள் நேரடியாக சி.ஏ.ஜி-யால் தணிக்கை செய்யப்பட்டு அங்கீகரிக்கப்படுகின்றன"),
                ("Central FC completely replaces all State Finance Commissions across the country", "மத்திய நிதி ஆணையம் நாடு முழுவதும் உள்ள அனைத்து மாநில நிதி ஆணையங்களையும் முழுமையாக மாற்றியமைக்கிறது"),
                ("State local bodies are directly financed through the Union Budget without state mediation", "மாநில உள்ளாட்சி அமைப்புகள் மாநில அரசின் தலையீடின்றி நேரடியாக மத்திய பட்ஜெட் மூலம் நிதியளிக்கப்படுகின்றன")
            ],
            "correct_key": "A",
            "exp_en": "Articles 280(3)(bb) and 280(3)(c), inserted by the 73rd and 74th Amendments, mandate that the Central Finance Commission shall recommend measures needed to augment the Consolidated Fund of a State to supplement the resources of the Panchayats and Municipalities in the State 'on the basis of the recommendations made by the Finance Commission of the State'.",
            "exp_ta": "73 மற்றும் 74-வது திருத்தங்களால் சேர்க்கப்பட்ட சரத்துகள் 280(3)(bb) மற்றும் 280(3)(c) ஆகியவற்றின்படி, 'மாநில நிதி ஆணையம் செய்த பரிந்துரைகளின் அடிப்படையில்', ஊராட்சிகள் மற்றும் நகராட்சிகளின் வளங்களை பெருக்குவதற்காக மாநிலத்தின் தொகுப்பு நிதியை அதிகரிப்பதற்கான நடவடிக்கைகளை மத்திய நிதி ஆணையம் பரிந்துரைக்க வேண்டும்.",
            "why_a_en": "Correct. This forms the organic constitutional link between State FCs and the Central FC.",
            "why_a_ta": "சரி. இது மாநில நிதி ஆணையங்களுக்கும் மத்திய நிதி ஆணையத்திற்கும் இடையே உள்ள அரசியலமைப்பு இணைப்பாகும்.",
            "why_b_en": "Incorrect. CAG audits accounts, but does not approve policy reports of SFCs.",
            "why_b_ta": "தவறு. சி.ஏ.ஜி கணக்குகளைத் தணிக்கை செய்கிறது, SFC கொள்கை அறிக்கைகளை அங்கீகரிப்பதில்லை.",
            "why_c_en": "Incorrect. Both SFC and CFC coexist as distinct constitutional bodies.",
            "why_c_ta": "தவறு. SFC மற்றும் CFC இரண்டும் தனித்தனி அரசியலமைப்பு அமைப்புகளாக நீடிக்கின்றன.",
            "why_d_en": "Incorrect. Central grants flow through the Consolidated Fund of the State.",
            "why_d_ta": "தவறு. மத்திய மானியங்கள் மாநிலத் தொகுப்பு நிதியின் மூலமாகவே வழங்கப்படுகின்றன.",
            "tip_en": "Article 280(3)(bb) = Panchayats; Article 280(3)(c) = Municipalities.",
            "tip_ta": "சரத்து 280(3)(bb) = ஊராட்சிகள்; சரத்து 280(3)(c) = நகராட்சிகள்.",
            "fact_en": "The 11th Finance Commission was the first Central Finance Commission mandated to make recommendations under these sub-clauses.",
            "fact_ta": "இந்த துணை விதிகளின் கீழ் பரிந்துரைகளை வழங்க பணிக்கப்பட்ட முதல் மத்திய நிதி ஆணையம் 11-வது நிதி ஆணையமாகும்."
        },

        # 39. First State Finance Commission in Tamil Nadu
        {
            "subtopic": "sfc_functions_devolution_recommendations",
            "stem_en": "When was the First State Finance Commission (1st SFC) constituted in Tamil Nadu, and which award period did its recommendations cover?",
            "stem_ta": "தமிழ்நாட்டில் முதல் மாநில நிதி ஆணையம் (1st SFC) எப்போது அமைக்கப்பட்டது, அதன் பரிந்துரைகள் எந்தக் காலக்கட்டத்தை உள்ளடக்கியிருந்தன?",
            "options": [
                ("Constituted in April 1994; covered the award period 1997–2002", "ஏப்ரல் 1994-ல் அமைக்கப்பட்டது; 1997–2002 காலக்கட்டத்தை உள்ளடக்கியது"),
                ("Constituted in January 1990; covered the award period 1992–1997", "ஜனவரி 1990-ல் அமைக்கப்பட்டது; 1992–1997 காலக்கட்டத்தை உள்ளடக்கியது"),
                ("Constituted in October 2000; covered the award period 2002–2007", "அக்டோபர் 2000-ல் அமைக்கப்பட்டது; 2002–2007 காலக்கட்டத்தை உள்ளடக்கியது"),
                ("Constituted in August 2010; covered the award period 2012–2017", "ஆகஸ்ட் 2010-ல் அமைக்கப்பட்டது; 2012–2017 காலக்கட்டத்தை உள்ளடக்கியது")
            ],
            "correct_key": "A",
            "exp_en": "The First State Finance Commission of Tamil Nadu was constituted on April 23, 1994, under the chairmanship of Dr. P.S. Vaidyanathan. Its report was submitted in 1996 and recommendations covered the five-year award period 1997–2002.",
            "exp_ta": "தமிழ்நாட்டின் முதல் மாநில நிதி ஆணையம் டாக்டர் பி.எஸ். வைத்தியநாதன் தலைமையில் 1994 ஏப்ரல் 23 அன்று அமைக்கப்பட்டது. இதன் அறிக்கை 1996-ல் சமர்ப்பிக்கப்பட்டு, 1997–2002 வரையிலான ஐந்து ஆண்டு காலக்கட்டத்தை உள்ளடக்கியது.",
            "why_a_en": "Correct. Constituted in 1994 following the 73rd CAA mandate, operating for 1997-2002.",
            "why_a_ta": "சரி. 73-வது திருத்தத்திற்குப் பிறகு 1994-ல் அமைக்கப்பட்டு, 1997-2002 காலத்திற்குச் செயல்பட்டது.",
            "why_b_en": "Incorrect. 73rd CAA was not in force in 1990.",
            "why_b_ta": "தவறு. 1990-ல் 73-வது திருத்தம் நடைமுறைக்கு வரவில்லை.",
            "why_c_en": "Incorrect. 2000-2002 was the timeframe of the Second SFC.",
            "why_c_ta": "தவறு. 2000-2002 என்பது இரண்டாவது SFC-ன் காலமாகும்.",
            "why_d_en": "Incorrect. 2010 was the period of the Fourth SFC.",
            "why_d_ta": "தவறு. 2010 என்பது நான்காவது SFC-ன் காலமாகும்.",
            "tip_en": "Tamil Nadu was among the pioneer states to promptly constitute all successive SFCs (1st to 6th SFCs).",
            "tip_ta": "தமிழ்நாடு அனைத்து தொடர்ச்சியான SFC-களையும் (1 முதல் 6-வது வரை) உடனுக்குடன் அமைத்த முன்னணி மாநிலங்களில் ஒன்றாகும்.",
            "fact_en": "The 1st SFC recommended devolving 8% of the State's net tax revenue to rural and urban local bodies.",
            "fact_ta": "1-வது SFC மாநிலத்தின் நிகர வரி வருவாயில் 8%-ஐ உள்ளாட்சி அமைப்புகளுக்கு வழங்கப் பரிந்துரைத்தது."
        },

        # 40. Tamil Nadu Divisible Pool Percentage Progression
        {
            "subtopic": "sfc_functions_devolution_recommendations",
            "stem_en": "How did the vertical devolution percentage of State's Own Tax Revenue (SOTR) recommended for local bodies evolve from the 1st SFC to the 5th/6th SFC in Tamil Nadu?",
            "stem_ta": "தமிழ்நாட்டில் 1-வது SFC முதல் 5/6-வது SFC வரை உள்ளாட்சி அமைப்புகளுக்குப் பரிந்துரைக்கப்பட்ட மாநிலத்தின் சொந்த வரி வருவாய் (SOTR) பகிர்வு சதவீதம் எவ்வாறு உயர்ந்தது?",
            "options": [
                ("Increased progressively from 8% (1st SFC) to 10% (5th/6th SFC)", "8% (1-வது SFC)-லிருந்து படிப்படியாக 10% (5/6-வது SFC) ஆக அதிகரித்தது"),
                ("Decreased from 25% to 5% due to fiscal consolidation", "நிதி ஒருங்கிணைப்பு காரணமாக 25%-லிருந்து 5% ஆகக் குறைந்தது"),
                ("Remained strictly frozen at 2% across all commission reports", "அனைத்து ஆணைக்குழு அறிக்கைகளிலும் 2% என்ற அளவில் மாற்றமின்றி முடக்கப்பட்டது"),
                ("Fluctuated unpredictably between 1% and 50% every alternate year", "ஒவ்வொரு மாற்று ஆண்டிலும் 1% முதல் 50% வரை கணிக்க முடியாத அளவில் ஏற்ற இறக்கம் கண்டது")
            ],
            "correct_key": "A",
            "exp_en": "In Tamil Nadu, vertical devolution from SOTR progressed steadily: 1st SFC recommended 8%, 2nd SFC recommended 8% (phased to 9%), 3rd SFC recommended 9%, 4th SFC recommended 10%, and 5th/6th SFCs maintained 10% devolution to local bodies.",
            "exp_ta": "தமிழ்நாட்டில் SOTR-லிருந்து செங்குத்துப் பகிர்வு சீராக உயர்ந்தது: 1-வது SFC 8%, 2-வது SFC 8% (9% ஆக உயர்ந்தது), 3-வது SFC 9%, 4-வது SFC 10% எனப் பரிந்துரைத்தது; 5 மற்றும் 6-வது SFC-கள் 10% பகிர்வை பராமரித்தன.",
            "why_a_en": "Correct. Devolution expanded from 8% to 10% of SOTR over successive commissions.",
            "why_a_ta": "சரி. அடுத்தடுத்த ஆணையங்கள் மூலம் பகிர்வு SOTR-ன் 8%-லிருந்து 10% ஆக உயர்ந்தது.",
            "why_b_en": "Incorrect. Devolution was increased, not decreased to 5%.",
            "why_b_ta": "தவறு. பகிர்வு அதிகரிக்கப்பட்டதே தவிர 5% ஆகக் குறைக்கப்படவில்லை.",
            "why_c_en": "Incorrect. 2% is too trivial; TN devolves around 10%.",
            "why_c_ta": "தவறு. 2% என்பது மிகவும் குறைவு; தமிழ்நாடு சுமார் 10% வழங்குகிறது.",
            "why_d_en": "Incorrect. Allocations are stable 5-year percentages, not wildly fluctuating.",
            "why_d_ta": "தவறு. ஒதுக்கீடுகள் நிலையான 5 ஆண்டு சதவீதங்கள், நிலையற்றவை அல்ல.",
            "tip_en": "Tamil Nadu has one of the highest vertical devolution rates (10% of SOTR) among Indian states.",
            "tip_ta": "இந்திய மாநிலங்களில் மிக உயர்ந்த செங்குத்துப் பகிர்வு விகிதத்தைக் (SOTR-ல் 10%) கொண்டுள்ள மாநிலங்களில் தமிழ்நாடும் ஒன்று.",
            "fact_en": "The 10% pool is divided between rural local bodies (Panchayats) and urban local bodies (Municipalities/Corporations).",
            "fact_ta": "இந்த 10% பகிர்வு நிதி ஊரக உள்ளாட்சி அமைப்புகள் மற்றும் நகர்ப்புற உள்ளாட்சி அமைப்புகளுக்கு இடையே பிரிக்கப்படுகிறது."
        },

        # 41. Rural-Urban Ratio in Tamil Nadu SFC Devolution
        {
            "subtopic": "sfc_functions_devolution_recommendations",
            "stem_en": "In Tamil Nadu, into what broad ratio is the 10% devolution pool typically split between Rural Local Bodies (RLBs) and Urban Local Bodies (ULBs) following SFC recommendations?",
            "stem_ta": "தமிழ்நாட்டில், SFC பரிந்துரைகளின்படி 10% பகிர்வு நிதியானது ஊரக உள்ளாட்சி அமைப்புகள் (RLBs) மற்றும் நகர்ப்புற உள்ளாட்சி அமைப்புகளுக்கு (ULBs) இடையே பொதுவாக எந்த விகிதத்தில் பிரிக்கப்படுகிறது?",
            "options": [
                ("Roughly 56:44 or 58:42 in favour of Rural Local Bodies based on census population", "மக்கள் தொகையின் அடிப்படையில் ஊரக உள்ளாட்சிகளுக்கு ஆதரவாக தோராயமாக 56:44 அல்லது 58:42 என்ற விகிதத்தில்"),
                ("95:5 in favour of Rural Local Bodies", "ஊரக உள்ளாட்சிகளுக்கு ஆதரவாக 95:5 என்ற விகிதத்தில்"),
                ("10:90 in favour of Urban Municipal Corporations", "நகர்ப்புற மாநகராட்சிகளுக்கு ஆதரவாக 10:90 என்ற விகிதத்தில்"),
                ("100% to Urban bodies with 0% allocation to Panchayats", "நகர்ப்புற அமைப்புகளுக்கு 100% மற்றும் ஊராட்சிகளுக்கு 0% என்ற அளவில்")
            ],
            "correct_key": "A",
            "exp_en": "Successive Tamil Nadu State Finance Commissions have divided the devolution pool between rural and urban local bodies in the approximate ratio of 58:42 (or 56:44 under the 5th/6th SFC) reflecting the state's rural-urban population distribution.",
            "exp_ta": "தமிழ்நாட்டின் தொடர்ச்சியான மாநில நிதி ஆணையங்கள், மாநிலத்தின் ஊரக-நகர்ப்புற மக்கள் தொகை பரவலைப் பிரதிபலிக்கும் வகையில், பகிர்வு நிதியை ஊரக மற்றும் நகர்ப்புற அமைப்புகளுக்கு இடையே தோராயமாக 58:42 (அல்லது 5-வது/6-வது SFC-ன் கீழ் 56:44) என்ற விகிதத்தில் பிரித்துள்ளன.",
            "why_a_en": "Correct. Approximately 56-58% to rural and 42-44% to urban local bodies.",
            "why_a_ta": "சரி. ஊரகத்திற்கு சுமார் 56-58% மற்றும் நகர்ப்புறத்திற்கு 42-44% பகிர்ந்தளிக்கப்படுகிறது.",
            "why_b_en": "Incorrect. Tamil Nadu is highly urbanized (~48.4% urban), so 95:5 is impossible.",
            "why_b_ta": "தவறு. தமிழ்நாடு 48.4% நகர்மயமானது என்பதால் 95:5 சாத்தியமில்லை.",
            "why_c_en": "Incorrect. Panchayats receive the majority share of the pool.",
            "why_c_ta": "தவறு. ஊராட்சிகளே நிதியில் பெரும்பான்மைப் பங்கை பெறுகின்றன.",
            "why_d_en": "Incorrect. Both rural and urban bodies are constitutionally protected.",
            "why_d_ta": "தவறு. இரண்டு அமைப்புகளும் அரசியலமைப்பு ரீதியாக பாதுகாக்கப்படுகின்றன.",
            "tip_en": "Tamil Nadu is one of the most urbanized large states in India according to Census 2011 (48.45% urban).",
            "tip_ta": "2011 மக்கள் தொகை கணக்கெடுப்பின்படி தமிழ்நாடு இந்தியாவின் மிகவும் நகர்மயமான பெரிய மாநிலங்களில் ஒன்றாகும் (48.45% நகர்ப்புறம்).",
            "fact_en": "Within rural local bodies, the funds are further distributed among Village Panchayats, Panchayat Unions, and District Panchayats.",
            "fact_ta": "ஊரக அமைப்புகளுக்குள், கிராம ஊராட்சிகள், ஊராட்சி ஒன்றியங்கள் மற்றும் மாவட்ட ஊராட்சிகளுக்கு இடையே நிதி மேலும் பிரிக்கப்படுகிறது."
        },

        # 42. Horizontal sharing criteria
        {
            "subtopic": "sfc_functions_devolution_recommendations",
            "stem_en": "Which of the following criteria is commonly given the highest weightage by State Finance Commissions when allocating funds among individual local bodies (horizontal devolution)?",
            "stem_ta": "தனிப்பட்ட உள்ளாட்சி அமைப்புகளுக்கு இடையே நிதியை ஒதுக்கும் போது (Horizontal Devolution) மாநில நிதி ஆணையங்களால் பொதுவாக அதிக முக்கியத்துவம் அளிக்கப்படும் காரணி எது?",
            "options": [
                ("Total Population of the local body according to the latest Census", "சமீபத்திய மக்கள் தொகை கணக்கெடுப்பின்படியான உள்ளாட்சி அமைப்பின் மொத்த மக்கள் தொகை"),
                ("Number of political party offices located within the ward", "வார்டுக்குள் அமைந்துள்ள அரசியல் கட்சி அலுவலகங்களின் எண்ணிக்கை"),
                ("Total length of national highways passing through the district", "மாவட்டம் வழியாக செல்லும் தேசிய நெடுஞ்சாலைகளின் மொத்த நீளம்"),
                ("Total commercial bank deposits held by private corporations", "தனியார் நிறுவனங்கள் வைத்துள்ள மொத்த வணிக வங்கி வைப்புத்தொகை")
            ],
            "correct_key": "A",
            "exp_en": "Population carries the highest weightage (typically 50% to 65%) in the horizontal devolution formula adopted by SFCs, ensuring that funds match the sheer volume of citizens requiring basic civic services (water supply, sanitation, lighting).",
            "exp_ta": "SFC-களால் பின்பற்றப்படும் கிடைமட்ட பகிர்வு சூத்திரத்தில் மக்கள் தொகை மிக அதிக முக்கியத்துவத்தைக் (பொதுவாக 50% முதல் 65% வரை) கொண்டுள்ளது; இது அடிப்படை சேவைகள் தேவைப்படும் மக்களின் எண்ணிக்கைக்கு ஏற்ப நிதி செல்வதை உறுதி செய்கிறது.",
            "why_a_en": "Correct. Population is the foundational demographic criterion with maximum weightage.",
            "why_a_ta": "சரி. மக்கள் தொகையே அதிக எடையைக் கொண்ட முதன்மையான காரணியாகும்.",
            "why_b_en": "Incorrect. Party offices are irrelevant to fiscal formulas.",
            "why_b_ta": "தவறு. கட்சி அலுவலகங்கள் நிதி சூத்திரங்களுக்கு பொருத்தமற்றவை.",
            "why_c_en": "Incorrect. National highways are funded by the central NHAI, not local body grants.",
            "why_c_ta": "தவறு. தேசிய நெடுஞ்சாலைகள் மத்திய NHAI-ஆல் நிதியளிக்கப்படுகின்றன.",
            "why_d_en": "Incorrect. Bank deposits do not determine local body grant allocation.",
            "why_d_ta": "தவறு. வங்கி வைப்புத்தொகை உள்ளாட்சி மானியத்தை தீர்மானிப்பதில்லை.",
            "tip_en": "Other criteria include Area, Per Capita Income Distance, Index of Deprivation, and SC/ST population.",
            "tip_ta": "பிற காரணிகளில் பரப்பளவு, தனிநபர் வருமான இடைவெளி, பின்தங்கிய நிலை குறியீடு மற்றும் SC/ST மக்கள் தொகை ஆகியவை அடங்கும்.",
            "fact_en": "In Tamil Nadu, horizontal sharing also utilizes an Index of Deprivation (infrastructure deficit) to assist poorer panchayats.",
            "fact_ta": "தமிழ்நாட்டில், ஏழை ஊராட்சிகளுக்கு உதவ உள்கட்டமைப்பு பற்றாக்குறை குறியீடும் பயன்படுத்தப்படுகிறது."
        },

        # 43. Sixth State Finance Commission of Tamil Nadu
        {
            "subtopic": "sfc_functions_devolution_recommendations",
            "stem_en": "Under whose chairmanship was the Sixth State Finance Commission (6th SFC) of Tamil Nadu constituted in March 2020?",
            "stem_ta": "மார்ச் 2020-ல் தமிழ்நாட்டின் ஆறாவது மாநில நிதி ஆணையம் (6th SFC) யாருடைய தலைமையில் அமைக்கப்பட்டது?",
            "options": [
                ("Thiru Mohan Pyare, IAS (Retd.)", "திரு மோகன் பியாரே, இ.ஆ.ப. (ஓய்வு)"),
                ("Dr. C. Rangarajan", "டாக்டர் சி. ரங்கராஜன்"),
                ("Thiru K. Venkataramanan", "திரு கே. வெங்கடரமணன்"),
                ("Dr. S. Narayan", "டாக்டர் எஸ். நாராயண்")
            ],
            "correct_key": "A",
            "exp_en": "The 6th State Finance Commission of Tamil Nadu was constituted in March 2020 under the chairmanship of Thiru Mohan Pyare, IAS (Retd.), to review the financial position of local bodies and recommend devolution for the 2022–2027 period.",
            "exp_ta": "தமிழ்நாட்டின் 6-வது மாநில நிதி ஆணையம் 2022–2027 காலத்திற்கான நிதி நிலையை ஆய்வு செய்து பகிர்வை பரிந்துரைக்க, மார்ச் 2020-ல் திரு மோகன் பியாரே, இ.ஆ.ப. (ஓய்வு) அவர்களின் தலைமையில் அமைக்கப்பட்டது.",
            "why_a_en": "Correct. Thiru Mohan Pyare headed the 6th SFC of Tamil Nadu.",
            "why_a_ta": "சரி. திரு மோகன் பியாரே தமிழ்நாட்டின் 6-வது SFC-க்கு தலைமை தாங்கினார்.",
            "why_b_en": "Incorrect. Dr. C. Rangarajan headed the 12th Central Finance Commission and state economic advisory panels.",
            "why_b_ta": "தவறு. டாக்டர் சி. ரங்கராஜன் 12-வது மத்திய நிதி ஆணையத்திற்கு தலைமை தாங்கினார்.",
            "why_c_en": "Incorrect. Thiru K. Venkataramanan headed an earlier commission.",
            "why_c_ta": "தவறு. திரு கே. வெங்கடரமணன் முந்தைய ஆணையத்திற்கு தலைமை தாங்கினார்.",
            "why_d_en": "Incorrect. Dr. S. Narayan was associated with earlier economic and finance bodies.",
            "why_d_ta": "தவறு. டாக்டர் எஸ். நாராயண் முந்தைய நிதி அமைப்புகளில் பணியாற்றியவர்.",
            "tip_en": "6th SFC covered the award period 2022-2027, aligned with the 15th Central Finance Commission cycle.",
            "tip_ta": "6-வது SFC 2022-2027 காலக்கட்டத்தை உள்ளடக்கியது, இது 15-வது மத்திய நிதி ஆணைய சுழற்சியுடன் இணைந்தது.",
            "fact_en": "The 6th SFC report laid special emphasis on own-source revenue mobilization and digitizing local property tax records.",
            "fact_ta": "6-வது SFC அறிக்கை சொந்த வருவாய் திரட்டல் மற்றும் சொத்து வரி பதிவுகளை டிஜிட்டல் மயமாக்குவதில் சிறப்பு கவனம் செலுத்தியது."
        },

        # 44. Local Fund Audit Department role
        {
            "subtopic": "inter_relations_local_bodies_cag_audit",
            "stem_en": "Which specialized state department is responsible for the statutory audit of accounts of rural and urban local bodies in Tamil Nadu under state legislation?",
            "stem_ta": "மாநில சட்டத்தின் கீழ் தமிழ்நாட்டில் ஊரக மற்றும் நகர்ப்புற உள்ளாட்சி அமைப்புகளின் கணக்குகளை சட்டப்பூர்வமாக தணிக்கை செய்யும் பொறுப்புள்ள சிறப்பு மாநிலத் துறை எது?",
            "options": [
                ("Directorate of Local Fund Audit (DLFA)", "உள்ளாட்சி நிதி தணிக்கை இயக்ககம் (DLFA)"),
                ("Central Vigilance Commission", "மத்திய விழிப்புணர்வு ஆணையம் (CVC)"),
                ("Enforcement Directorate", "அமலாக்க இயக்ககம் (ED)"),
                ("Serious Fraud Investigation Office", "தீவிர மோசடி விசாரணை அலுவலகம் (SFIO)")
            ],
            "correct_key": "A",
            "exp_en": "The Directorate of Local Fund Audit (DLFA) in Tamil Nadu is the statutory auditing authority empowered to audit the accounts of Village Panchayats, Panchayat Unions, District Panchayats, Municipalities, and Municipal Corporations.",
            "exp_ta": "தமிழ்நாட்டில் உள்ளாட்சி நிதி தணிக்கை இயக்ககம் (DLFA) என்பது கிராம ஊராட்சிகள், ஊராட்சி ஒன்றியங்கள், மாவட்ட ஊராட்சிகள், நகராட்சிகள் மற்றும் மாநகராட்சிகளின் கணக்குகளைத் தணிக்கை செய்ய அதிகாரம் பெற்ற சட்டப்பூர்வ தணிக்கை அதிகார அமைப்பாகும்.",
            "why_a_en": "Correct. Directorate of Local Fund Audit conducts statutory audits of local bodies.",
            "why_a_ta": "சரி. உள்ளாட்சி நிதி தணிக்கை இயக்ககம் உள்ளாட்சி அமைப்புகளின் சட்டப்பூர்வ தணிக்கையை நடத்துகிறது.",
            "why_b_en": "Incorrect. CVC is an apex central anti-corruption body.",
            "why_b_ta": "தவறு. CVC என்பது மத்திய ஊழல் தடுப்பு அமைப்பு.",
            "why_c_en": "Incorrect. ED investigates money laundering, not municipal accounts.",
            "why_c_ta": "தவறு. அமலாக்க இயக்ககம் பணமோசடி வழக்குகளை விசாரிக்கிறது.",
            "why_d_en": "Incorrect. SFIO investigates corporate corporate frauds under the Companies Act.",
            "why_d_ta": "தவறு. SFIO கார்ப்பரேட் நிறுவன மோசடிகளை விசாரிக்கிறது.",
            "tip_en": "DLFA also issues surcharge notices against local body functionaries for recovery of misappropriated funds.",
            "tip_ta": "முறைகேடாகப் பயன்படுத்தப்பட்ட நிதியை மீட்டெடுக்க உள்ளாட்சி நிர்வாகிகள் மீது கூடுதல் கட்டண (Surcharge) நோட்டீஸ்களையும் DLFA வெளியிடுகிறது.",
            "fact_en": "The Director of Local Fund Audit acts as the statutory auditor under the Tamil Nadu Local Fund Audit Act, 2014.",
            "fact_ta": "தமிழ்நாடு உள்ளாட்சி நிதி தணிக்கைச் சட்டம் 2014-ன் கீழ் உள்ளாட்சி நிதி தணிக்கை இயக்குநர் சட்டப்பூர்வ தணிக்கையாளராக செயல்படுகிறார்."
        },

        # 45. Technical Guidance and Support (TGS) by CAG
        {
            "subtopic": "inter_relations_local_bodies_cag_audit",
            "stem_en": "Under the recommendations of the Eleventh and successive Central Finance Commissions, what institutional role is entrusted to the Comptroller and Auditor General (CAG) regarding local body finances?",
            "stem_ta": "பதினோராவது மற்றும் அடுத்தடுத்த மத்திய நிதி ஆணையங்களின் பரிந்துரைகளின்படி, உள்ளாட்சி நிதிகள் தொடர்பாக இந்தியத் தலைமைத் தணிக்கையாளரிடம் (CAG) ஒப்படைக்கப்பட்டுள்ள நிறுவனப் பங்கு என்ன?",
            "options": [
                ("Technical Guidance and Support (TGS) to the State Local Fund Audit and test checking of accounts", "மாநில உள்ளாட்சி நிதி தணிக்கைக்கு தொழில்நுட்ப வழிகாட்டுதல் மற்றும் ஆதரவு (TGS) மற்றும் கணக்குகளை மாதிரி சரிபார்த்தல்"),
                ("Direct daily day-to-day administration of village panchayat bank accounts", "கிராம ஊராட்சி வங்கி கணக்குகளை நேரடியாக தினசரி நிர்வகித்தல்"),
                ("Power to directly dismiss elected mayors without state legislative proceedings", "மாநில சட்டமன்ற நடைமுறைகளின்றி தேர்ந்தெடுக்கப்பட்ட மேயர்களை நேரடியாக பதவி நீக்கம் செய்யும் அதிகாரம்"),
                ("Exclusive monopoly over printing all local body currency notes", "அனைத்து உள்ளாட்சி பணத்தாள்களையும் அச்சிடுவதற்கான பிரத்யேக ஏகபோக உரிமை")
            ],
            "correct_key": "A",
            "exp_en": "Under the Technical Guidance and Support (TGS) framework recommended by Central Finance Commissions, the CAG provides audit methodology, standards, and training to the State Local Fund Audit and conducts test checks of local body accounts, placing annual audit reports before the State Legislature.",
            "exp_ta": "மத்திய நிதி ஆணையங்களால் பரிந்துரைக்கப்பட்ட தொழில்நுட்ப வழிகாட்டுதல் மற்றும் ஆதரவு (TGS) கட்டமைப்பின் கீழ், CAG தணிக்கை முறைகள், தரநிலைகள் மற்றும் பயிற்சிகளை மாநில உள்ளாட்சி நிதி தணிக்கைத் துறைக்கு வழங்குகிறது மற்றும் மாதிரி தணிக்கைகளை மேற்கொண்டு சட்டமன்றத்தில் அறிக்கைகளை சமர்ப்பிக்கிறது.",
            "why_a_en": "Correct. CAG exercises TGS over local body audit and conducts sample test checks.",
            "why_a_ta": "சரி. சி.ஏ.ஜி உள்ளாட்சி தணிக்கை மீது TGS-ஐ செலுத்தி மாதிரி தணிக்கைகளை மேற்கொள்கிறது.",
            "why_b_en": "Incorrect. CAG does not operate or manage local bank accounts.",
            "why_b_ta": "தவறு. சி.ஏ.ஜி உள்ளாட்சி வங்கி கணக்குகளை நிர்வகிப்பதில்லை.",
            "why_c_en": "Incorrect. CAG has no removal powers over elected representatives.",
            "why_c_ta": "தவறு. தேர்ந்தெடுக்கப்பட்ட பிரதிநிதிகளை நீக்கும் அதிகாரம் சி.ஏ.ஜி-க்கு இல்லை.",
            "why_d_en": "Incorrect. Currency printing belongs strictly to RBI, not local bodies.",
            "why_d_ta": "தவறு. ரூபாய் நோட்டுகளை அச்சிடுவது ரிசர்வ் வங்கிக்கு மட்டுமே உரியது.",
            "tip_en": "TGS ensures uniform accounting standards (Panchayat Accounting System and National Municipal Accounting Manual).",
            "tip_ta": "TGS சீரான கணக்கியல் தரநிலைகளை (தேசிய நகராட்சி கணக்கியல் கையேடு) உறுதி செய்கிறது.",
            "fact_en": "CAG's Audit Reports on Local Bodies are examined by the Public Accounts Committee (PAC) or Committee on Local Bodies of the State Legislature.",
            "fact_ta": "உள்ளாட்சி அமைப்புகள் மீதான சி.ஏ.ஜி-யின் தணிக்கை அறிக்கைகள் மாநில சட்டமன்றத்தின் பொதுக் கணக்குக் குழுவால் (PAC) ஆய்வு செய்யப்படுகின்றன."
        },

        # 46. District Planning Committee under 243ZD
        {
            "subtopic": "inter_relations_local_bodies_cag_audit",
            "stem_en": "Which constitutional committee is mandated under Article 243ZD to consolidate the draft development plans prepared by Panchayats and Municipalities at the district level?",
            "stem_ta": "சரத்து 243ZD-ன் கீழ் மாவட்ட அளவில் ஊராட்சிகள் மற்றும் நகராட்சிகளால் தயாரிக்கப்படும் வரைவு வளர்ச்சித் திட்டங்களை ஒருங்கிணைக்க கட்டாயப்படுத்தப்பட்டுள்ள அரசியலமைப்பு குழு எது?",
            "options": [
                ("District Planning Committee (DPC)", "மாவட்ட திட்டமிடும் குழு (DPC)"),
                ("District Consumer Redressal Forum", "மாவட்ட நுகர்வோர் குறைதீர் மன்றம்"),
                ("District Vigilance and Monitoring Committee", "மாவட்ட கண்காணிப்புக் குழு"),
                ("District Delimitation Commission", "மாவட்ட எல்லை மறுசீரமைப்பு ஆணையம்")
            ],
            "correct_key": "A",
            "exp_en": "Article 243ZD mandates the constitution of a District Planning Committee (DPC) in every district to consolidate the plans prepared by the Panchayats and the Municipalities in the district and to prepare a draft development plan for the district as a whole.",
            "exp_ta": "சரத்து 243ZD-ன் படி, மாவட்டத்தில் உள்ள ஊராட்சிகள் மற்றும் நகராட்சிகளால் தயாரிக்கப்பட்ட திட்டங்களை ஒருங்கிணைத்து, மாவட்டம் முழுமைக்குமான வரைவு வளர்ச்சித் திட்டத்தை தயாரிப்பதற்காக ஒவ்வொரு மாவட்டத்திலும் மாவட்ட திட்டமிடும் குழு (DPC) அமைக்கப்பட வேண்டும்.",
            "why_a_en": "Correct. Article 243ZD specifically creates the District Planning Committee.",
            "why_a_ta": "சரி. சரத்து 243ZD குறிப்பாக மாவட்ட திட்டக் குழுவை உருவாக்குகிறது.",
            "why_b_en": "Incorrect. Consumer forum deals with consumer disputes under Consumer Protection Act.",
            "why_b_ta": "தவறு. நுகர்வோர் மன்றம் நுகர்வோர் வழக்குகளைக் கையாள்கிறது.",
            "why_c_en": "Incorrect. Vigilance committee monitors central schemes, not spatial planning consolidation.",
            "why_c_ta": "தவறு. கண்காணிப்புக் குழு திட்டங்களை கண்காணிக்கிறது, வளர்ச்சி திட்டத்தை உருவாக்குவதில்லை.",
            "why_d_en": "Incorrect. Delimitation is an electoral exercise, not economic planning.",
            "why_d_ta": "தவறு. தொகுதி மறுசீரமைப்பு என்பது தேர்தல் செயல்முறை, திட்டமிடல் அல்ல.",
            "tip_en": "At least four-fifths (4/5ths) of DPC members must be elected from and by the elected members of the District Panchayat and Municipalities.",
            "tip_ta": "DPC உறுப்பினர்களில் குறைந்தபட்சம் ஐந்தில் நான்கு பங்கு (4/5) பேர் மாவட்ட ஊராட்சி மற்றும் நகராட்சி உறுப்பினர்களால் தேர்ந்தெடுக்கப்பட வேண்டும்.",
            "fact_en": "In Tamil Nadu, the District Panchayat Chairperson is designated as the Chairperson of the DPC, with the District Collector as Member-Secretary.",
            "fact_ta": "தமிழ்நாட்டில் மாவட்ட ஊராட்சித் தலைவர் DPC-யின் தலைவராகவும், மாவட்ட ஆட்சித்தலைவர் உறுப்பினர்-செயலாளராகவும் உள்ளனர்."
        },

        # 47. Metropolitan Planning Committee under 243ZE
        {
            "subtopic": "inter_relations_local_bodies_cag_audit",
            "stem_en": "Under Article 243ZE, what is the population threshold for an urban agglomeration to mandate the constitution of a Metropolitan Planning Committee (MPC)?",
            "stem_ta": "சரத்து 243ZE-ன் கீழ் பெருநகர திட்டமிடும் குழுவை (MPC) அமைப்பதற்கு ஒரு பெருநகரப் பகுதிக்குத் தேவையான குறைந்தபட்ச மக்கள் தொகை வரம்பு என்ன?",
            "options": [
                ("A population of 10 lakhs (1 million) or more", "10 லட்சம் (1 மில்லியன்) அல்லது அதற்கு மேற்பட்ட மக்கள் தொகை"),
                ("A population of 1 lakh or more", "1 லட்சம் அல்லது அதற்கு மேற்பட்ட மக்கள் தொகை"),
                ("A population of 50 lakhs or more exclusively", "50 லட்சம் அல்லது அதற்கு மேற்பட்ட மக்கள் தொகை மட்டுமே"),
                ("A population of 1 crore or more", "1 கோடி அல்லது அதற்கு மேற்பட்ட மக்கள் தொகை")
            ],
            "correct_key": "A",
            "exp_en": "Under Article 243P(c) read with Article 243ZE, a 'Metropolitan area' means an area having a population of ten lakhs (1,000,000) or more, comprised in one or more districts and consisting of two or more Municipalities or Panchayats, mandating a Metropolitan Planning Committee.",
            "exp_ta": "சரத்து 243P(c) மற்றும் 243ZE ஆகியவற்றின்படி, 'பெருநகரப் பகுதி' என்பது ஒன்று அல்லது அதற்கு மேற்பட்ட மாவட்டங்களில் பரவி, இரண்டு அல்லது அதற்கு மேற்பட்ட நகராட்சிகள் அல்லது ஊராட்சிகளைக் கொண்ட 10 லட்சம் அல்லது அதற்கு மேற்பட்ட மக்கள் தொகையைக் கொண்ட பகுதியாகும்.",
            "why_a_en": "Correct. 10 lakhs (1 million) is the constitutional population threshold for a Metropolitan area.",
            "why_a_ta": "சரி. 10 லட்சம் மக்கள் தொகையே பெருநகரப் பகுதிக்கான அரசியலமைப்பு வரம்பாகும்.",
            "why_b_en": "Incorrect. 1 lakh is too small for a metropolitan classification.",
            "why_b_ta": "தவறு. 1 லட்சம் என்பது பெருநகர வரையறைக்கு மிகக் குறைவு.",
            "why_c_en": "Incorrect. 50 lakhs is not the minimum threshold.",
            "why_c_ta": "தவறு. 50 லட்சம் என்பது குறைந்தபட்ச வரம்பு அல்ல.",
            "why_d_en": "Incorrect. 1 crore is for megacities, not the constitutional floor.",
            "why_d_ta": "தவறு. 1 கோடி என்பது மெகா நகரங்களுக்கானது, அரசியலமைப்பு குறைந்தபட்சம் அல்ல.",
            "tip_en": "Not less than two-thirds (2/3rds) of MPC members are elected by elected members of Municipalities and chairpersons of Panchayats in the area.",
            "tip_ta": "MPC உறுப்பினர்களில் மூன்றில் இரண்டு பங்கிற்கு குறையாதவர்கள் (2/3) அப்பகுதி நகராட்சி மற்றும் ஊராட்சித் தலைவர்களால் தேர்ந்தெடுக்கப்படுகின்றனர்.",
            "fact_en": "Chennai Metropolitan Development Authority (CMDA) functions within the Chennai Metropolitan Area covering over 8 million people.",
            "fact_ta": "சென்னை பெருநகர வளர்ச்சிக் குழுமம் (CMDA) 80 லட்சத்திற்கும் அதிகமான மக்களைக் கொண்ட சென்னை பெருநகரப் பகுதியில் செயல்படுகிறது."
        },

        # 48. Surcharge Proceedings by Audit
        {
            "subtopic": "inter_relations_local_bodies_cag_audit",
            "stem_en": "Under the Tamil Nadu Local Fund Audit Act, what legal mechanism is employed by the audit authority to recover losses caused by illegal payments or gross negligence from elected representatives or officials?",
            "stem_ta": "தமிழ்நாடு உள்ளாட்சி நிதி தணிக்கைச் சட்டத்தின் கீழ், தேர்ந்தெடுக்கப்பட்ட பிரதிநிதிகள் அல்லது அதிகாரிகளால் சட்டவிரோதக் கொடுப்பனவுகள் அல்லது கடுமையான அலட்சியத்தால் ஏற்படும் இழப்புகளை மீட்டெடுக்க தணிக்கை அதிகாரியால் பயன்படுத்தப்படும் சட்ட வழிமுறை எது?",
            "options": [
                ("Issuing Surcharge Notices and Surcharge Certificates", "கூடுதல் கட்டண அறிவிப்புகள் மற்றும் சான்றிதழ்களை (Surcharge Notices) வழங்குதல்"),
                ("Directly filing treason charges in a military court", "இராணுவ நீதிமன்றத்தில் நேரடியாக தேசத்துரோகக் குற்றச்சாட்டுகளைப் பதிவு செய்தல்"),
                ("Revoking Indian citizenship of the erring functionary", "தவறிழைத்த அதிகாரியின் இந்தியக் குடியுரிமையை ரத்து செய்தல்"),
                ("Imposing physical hard labour without judicial sanction", "நீதிமன்ற அனுமதியின்றி கடுமையான உடல் உழைப்புத் தண்டனையை விதித்தல்")
            ],
            "correct_key": "A",
            "exp_en": "Under the Local Fund Audit Act, the auditor has statutory powers to surcharge any person responsible for making or authorizing illegal payments, gross negligence, or misappropriation, issuing a Surcharge Certificate to recover the quantified amount as arrears of land revenue.",
            "exp_ta": "உள்ளாட்சி நிதி தணிக்கைச் சட்டத்தின் கீழ், சட்டவிரோத பணம் செலுத்துதல் அல்லது மோசடிக்கு காரணமான நபர் மீது கூடுதல் கட்டணம் (Surcharge) விதிக்கவும், இழப்புத் தொகையை நில வருவாய் நிலுவையைப் போல மீட்டெடுக்க கூடுதல் கட்டணச் சான்றிதழ் வழங்கவும் தணிக்கையாளருக்கு அதிகாரம் உண்டு.",
            "why_a_en": "Correct. Surcharge notice and certificate is the established statutory mechanism for fiscal recovery.",
            "why_a_ta": "சரி. கூடுதல் கட்டண அறிவிப்பு மற்றும் சான்றிதழே நிதி இழப்பை மீட்பதற்கான சட்டப்பூர்வ வழியாகும்.",
            "why_b_en": "Incorrect. Military courts have no jurisdiction over civil local bodies.",
            "why_b_ta": "தவறு. சிவில் உள்ளாட்சி அமைப்புகள் மீது இராணுவ நீதிமன்றங்களுக்கு அதிகார வரம்பு இல்லை.",
            "why_c_en": "Incorrect. Citizenship cannot be revoked for audit irregularities.",
            "why_c_ta": "தவறு. தணிக்கை முரண்பாடுகளுக்காக குடியுரிமையை ரத்து செய்ய முடியாது.",
            "why_d_en": "Incorrect. Physical labour cannot be administratively imposed.",
            "why_d_ta": "தவறு. உடல் உழைப்புத் தண்டனையை நிர்வாக ரீதியாக விதிக்க முடியாது.",
            "tip_en": "An aggrieved person can appeal against a surcharge order to the Principal District Court within a stipulated time limit.",
            "tip_ta": "பாதிக்கப்பட்ட நபர் குறிப்பிட்ட காலத்திற்குள் கூடுதல் கட்டண உத்தரவுக்கு எதிராக முதன்மை மாவட்ட நீதிமன்றத்தில் மேல்முறையீடு செய்யலாம்.",
            "fact_en": "Surcharge proceedings ensure that local functionaries are personally liable for financial losses caused to the civic body.",
            "fact_ta": "கூடுதல் கட்டண நடவடிக்கைகள் உள்ளாட்சி அமைப்பிற்கு ஏற்படும் நிதி இழப்புகளுக்கு உள்ளூர் நிர்வாகிகள் தனிப்பட்ட முறையில் பொறுப்பாவதை உறுதி செய்கின்றன."
        },

        # 49. Social Audit in Panchayati Raj
        {
            "subtopic": "inter_relations_local_bodies_cag_audit",
            "stem_en": "Under Section 17 of the MGNREGA and state Panchayati Raj rules, which grassroots forum is constitutionally and statutorily empowered to conduct Social Audits of all village works?",
            "stem_ta": "MGNREGA சட்டத்தின் பிரிவு 17 மற்றும் மாநில ஊராட்சி விதிகளின் கீழ், அனைத்து கிராமப் பணிகளின் சமூகத் தணிக்கையை (Social Audit) நடத்த அரசியலமைப்பு மற்றும் சட்டப்பூர்வ அதிகாரம் பெற்றுள்ள அடிமட்ட அமைப்பு எது?",
            "options": [
                ("Gram Sabha consisting of all registered voters of the village", "கிராமத்தின் அனைத்து பதிவு செய்யப்பட்ட வாக்காளர்களையும் கொண்ட கிராம சபை"),
                ("Standing Committee of the State Legislative Assembly", "மாநில சட்டப் பேரவையின் நிலைக்குழு"),
                ("District Chamber of Commerce and Industries", "மாவட்ட வர்த்தக மற்றும் தொழில் சபை"),
                ("Board of Directors of the Lead Commercial Bank", "முன்னணி வணிக வங்கியின் இயக்குநர் குழு")
            ],
            "correct_key": "A",
            "exp_en": "Under Article 243A of the Constitution and Section 17 of the MGNREGA Act, the Gram Sabha (comprising all persons registered in the electoral rolls for the village) is empowered to conduct social audits of all development projects executed in the village.",
            "exp_ta": "அரசியலமைப்பின் சரத்து 243A மற்றும் MGNREGA சட்டத்தின் பிரிவு 17 ஆகியவற்றின் கீழ், கிராம வாக்காளர் பட்டியலில் பதிவு செய்துள்ள அனைவரையும் உள்ளடக்கிய 'கிராம சபை' கிராமத்தில் செயல்படுத்தப்படும் அனைத்து வளர்ச்சிப் பணிகளின் சமூகத் தணிக்கையை மேற்கொள்ள அதிகாரம் பெற்றுள்ளது.",
            "why_a_en": "Correct. Gram Sabha conducts social audits of local development projects.",
            "why_a_ta": "சரி. கிராம சபை உள்ளூர் வளர்ச்சித் திட்டங்களின் சமூகத் தணிக்கையை நடத்துகிறது.",
            "why_b_en": "Incorrect. Legislative committees do not assemble at the village level for social audit.",
            "why_b_ta": "தவறு. சட்டமன்றக் குழுக்கள் கிராம அளவில் கூடி சமூகத் தணிக்கை செய்வதில்லை.",
            "why_c_en": "Incorrect. Private trade chambers have no audit mandate over rural public works.",
            "why_c_ta": "தவறு. தனியார் வர்த்தக சபைகளுக்கு கிராமப் பணிகளைத் தணிக்கை செய்யும் அதிகாரம் இல்லை.",
            "why_d_en": "Incorrect. Commercial bank boards do not review village civic works.",
            "why_d_ta": "தவறு. வணிக வங்கிகள் கிராமப் பணிகளை ஆய்வு செய்வதில்லை.",
            "tip_en": "In Tamil Nadu, mandatory Gram Sabha meetings are convened on specified days (Jan 26, May 1, Aug 15, Oct 2, Mar 22 - World Water Day, Nov 1 - Local Governance Day).",
            "tip_ta": "தமிழ்நாட்டில் குறிப்பிட்ட நாட்களில் (ஜனவரி 26, மே 1, ஆகஸ்ட் 15, அக்டோபர் 2, மார்ச் 22, நவம்பர் 1) கட்டாய கிராம சபைக் கூட்டங்கள் கூட்டப்படுகின்றன.",
            "fact_en": "Social audit reports must be read out publicly, enabling beneficiaries to verify muster rolls and material bills directly.",
            "fact_ta": "சமூகத் தணிக்கை அறிக்கைகள் வெளிப்படையாகப் படிக்கப்பட வேண்டும், இதன் மூலம் பயனாளிகள் வருகைப் பதிவேடு மற்றும் செலவுகளை நேரடியாகச் சரிபார்க்கலாம்."
        },

        # 50. SFC Delay and 15th Finance Commission Conditionality
        {
            "subtopic": "inter_relations_local_bodies_cag_audit",
            "stem_en": "What stringent conditionality did the Fifteenth Central Finance Commission impose on states regarding State Finance Commissions for releasing rural and urban local body grants?",
            "stem_ta": "பதினைந்தாவது மத்திய நிதி ஆணையம் ஊரக மற்றும் நகர்ப்புற உள்ளாட்சி மானியங்களை விடுவிப்பதற்காக மாநில நிதி ஆணையங்கள் தொடர்பாக மாநிலங்களுக்கு விதித்த கடுமையான நிபந்தனை எது?",
            "options": [
                ("States must constitute SFCs, table their Action Taken Reports in the legislature, and implement recommendations", "மாநிலங்கள் SFC-களை அமைத்து, அவற்றின் மீது எடுக்கப்பட்ட நடவடிக்கை அறிக்கைகளை சட்டமன்றத்தில் தாக்கல் செய்து, பரிந்துரைகளை அமல்படுத்த வேண்டும்"),
                ("States must abolish the office of State Election Commissioner to receive central grants", "மத்திய மானியங்களைப் பெற மாநிலங்கள் மாநில தேர்தல் ஆணையர் பதவியை ரத்து செய்ய வேண்டும்"),
                ("States must surrender 50% of their legislative power over municipal taxation to the Union", "மாநிலங்கள் நகராட்சி வரிவிதிப்பு மீதான தங்கள் சட்டமன்ற அதிகாரத்தில் 50%-ஐ மத்திய அரசிடம் ஒப்படைக்க வேண்டும்"),
                ("States must stop holding local body elections permanently", "மாநிலங்கள் உள்ளாட்சித் தேர்தல்களை நிரந்தரமாக நடத்துவதை நிறுத்த வேண்டும்")
            ],
            "correct_key": "A",
            "exp_en": "The 15th Central Finance Commission stipulated that no local body grants shall be released to states after March 2024 unless the state has constituted the State Finance Commission, caused its recommendations along with the Action Taken Memorandum to be laid before the State Legislature, and acted on its recommendations.",
            "exp_ta": "15-வது மத்திய நிதி ஆணையம், ஒரு மாநிலம் மாநில நிதி ஆணையத்தை அமைத்து, அதன் பரிந்துரைகளை நடவடிக்கை எடுக்கப்பட்ட விளக்கக் குறிப்புடன் சட்டமன்றத்தில் சமர்ப்பித்து, அவற்றைச் செயல்படுத்தாவிட்டால் மார்ச் 2024-க்குப் பிறகு உள்ளாட்சி மானியங்கள் எதுவும் விடுவிக்கப்படாது என்று நிபந்தனை விதித்தது.",
            "why_a_en": "Correct. Constituting SFCs and tabling ATRs was made an uncompromising pre-condition for release of central grants.",
            "why_a_ta": "சரி. SFC-ஐ அமைத்து ATR-ஐ சட்டமன்றத்தில் சமர்ப்பிப்பது மத்திய மானியங்களை விடுவிப்பதற்கான கட்டாய முன்நிபந்தனையாக்கப்பட்டது.",
            "why_b_en": "Incorrect. Abolishing SEC is absurd and unconstitutional.",
            "why_b_ta": "தவறு. SEC-ஐ ரத்து செய்வது அரசியலமைப்புக்கு முற்றிலும் முரணானது.",
            "why_c_en": "Incorrect. Fiscal federalism is preserved; no surrender of state legislative list is demanded.",
            "why_c_ta": "தவறு. மாநில அதிகாரங்களை ஒப்படைக்க கோரப்படவில்லை.",
            "why_d_en": "Incorrect. Elections must be regularly conducted; freezing them causes forfeiture of grants.",
            "why_d_ta": "தவறு. தேர்தல்கள் முறையாக நடத்தப்பட வேண்டும்; முடக்குவது மானிய இழப்பை ஏற்படுத்தும்.",
            "tip_en": "This conditionality forced several delinquent states to immediately constitute long-delayed State Finance Commissions.",
            "tip_ta": "இந்த நிபந்தனை பல மாநிலங்களை நீண்டகாலமாக தாமதித்த மாநில நிதி ஆணையங்களை உடனடியாக அமைக்க கட்டாயப்படுத்தியது.",
            "fact_en": "The 15th FC tied 60% of rural local body grants to drinking water supply, rainwater harvesting, and open-defecation-free sanitation.",
            "fact_ta": "15-வது நிதி ஆணையம் ஊரக உள்ளாட்சி மானியங்களில் 60%-ஐ குடிநீர் வழங்கல், மழைநீர் சேகரிப்பு மற்றும் தூய்மைப் பணிகளுடன் இணைத்தது."
        }
    ]
