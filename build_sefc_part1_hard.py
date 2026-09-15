# -*- coding: utf-8 -*-
"""
State Election & Finance Commissions - Part 1: Hard MCQs (50 Questions)
TNPSC Nova AI Content Engine
"""
import os
import json
from collections import Counter
from tools.nova_content_engine.answer_randomizer import randomize_and_balance_dataset
from tools.nova_content_engine.validator import ContentValidator
from state_election_finance_commissions_mcq_helper import make_sefc_q


def get_hard_raw_questions():
    return [
        # 1. Kishan Singh Tomar Case - Constitutional Status
        {
            "subtopic": "State Election Commission - Constitutional Mandate & Provisions (Articles 243K & 243ZA)",
            "stem_en": "In Kishan Singh Tomar v. Municipal Corporation of Ahmedabad (2006), a Constitution Bench of the Supreme Court held that the State Election Commission:",
            "stem_ta": "கிஷன் சிங் தோமர் எதிர் அகமதாபாத் மாநகராட்சி (2006) வழக்கில், உச்ச நீதிமன்றத்தின் அரசியலமைப்பு அமர்வு மாநில தேர்தல் ஆணையம் பற்றி என்ன தீர்ப்பளித்தது?",
            "options": [
                ("Enjoys the same constitutional status and independence as the Election Commission of India under Article 324", "சரத்து 324-ன் கீழ் இந்திய தேர்தல் ஆணையத்திற்கு உள்ள அதே அரசியலமைப்பு அந்தஸ்தையும் சுதந்திரத்தையும் அனுபவிக்கிறது"),
                ("Is a subordinate statutory board subject to the direct administrative control of the State Panchayati Raj Department", "மாநில பஞ்சாயத்து ராஜ் துறையின் நேரடி நிர்வாகக் கட்டுப்பாட்டிற்கு உட்பட்ட ஒரு துணை சட்டப்பூர்வ வாரியம்"),
                ("Must obtain prior approval from the Governor before issuing any election notification", "எந்தவொரு தேர்தல் அறிவிப்பையும் வெளியிடுவதற்கு முன்பு ஆளுநரிடம் முன் அனுமதி பெற வேண்டும்"),
                ("Cannot issue directions to state police or administrative officers during local body elections", "உள்ளாட்சித் தேர்தல்களின் போது மாநில காவல்துறை அல்லது நிர்வாக அதிகாரிகளுக்கு உத்தரவுகளைப் பிறப்பிக்க முடியாது")
            ],
            "correct_key": "A",
            "exp_en": "In Kishan Singh Tomar (2006), the Supreme Court ruled that the powers of the State Election Commission under Articles 243K and 243ZA are on par with those of the Election Commission of India under Article 324, and the State Government must act in aid of the SEC.",
            "exp_ta": "கிஷன் சிங் தோமர் (2006) வழக்கில், சரத்துகள் 243K மற்றும் 243ZA-ன் கீழ் மாநில தேர்தல் ஆணையத்தின் அதிகாரங்கள் சரத்து 324-ன் கீழ் இந்திய தேர்தல் ஆணையத்தின் அதிகாரங்களுக்கு இணையானவை என்றும், மாநில அரசு SEC-க்கு உதவிகரமாகச் செயல்பட வேண்டும் என்றும் உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
            "why_a_en": "Correct. SC held SEC is on par with ECI regarding independence, superintendence, and control.",
            "why_a_ta": "சரி. சுதந்திரம், மேற்பார்வை மற்றும் கட்டுப்பாடு ஆகியவற்றில் SEC ஆனது ECI-க்கு சமமானது என்று உச்ச நீதிமன்றம் கூறியது.",
            "why_b_en": "Incorrect. SEC is an independent constitutional authority, not a subordinate board.",
            "why_b_ta": "தவறு. SEC ஒரு சுதந்திரமான அரசியலமைப்பு அதிகார அமைப்பாகும், துணை வாரியம் அல்ல.",
            "why_c_en": "Incorrect. Prior approval of the Governor is not required for issuing notifications.",
            "why_c_ta": "தவறு. அறிவிப்புகளை வெளியிட ஆளுநரின் முன் அனுமதி தேவையில்லை.",
            "why_d_en": "Incorrect. State officers are deemed to be on deputation to the SEC during elections.",
            "why_d_ta": "தவறு. தேர்தலின் போது மாநில அதிகாரிகள் SEC-ன் கீழ் அயல்பணியில் இருப்பதாகக் கருதப்படுகிறார்கள்.",
            "tip_en": "Kishan Singh Tomar (2006) = SEC parity with ECI under Art 324.",
            "tip_ta": "கிஷன் சிங் தோமர் (2006) = சரத்து 324-ன் கீழ் ECI உடன் SEC-ன் சமத்துவம்.",
            "fact_en": "The Kishan Singh Tomar bench emphasized that Article 243-E and 243-U mandate completing elections before tenure expiry.",
            "fact_ta": "கிஷன் சிங் தோமர் அமர்வு சரத்துகள் 243-E மற்றும் 243-U பதவிக்காலம் முடிவதற்குள் தேர்தலை நடத்த வேண்டும் என்று கட்டாயப்படுத்துவதை வலியுறுத்தியது."
        },

        # 2. Article 243-O and 243ZG Bar vs High Court Writ Jurisdiction
        {
            "subtopic": "State Election Commission - Constitutional Mandate & Provisions (Articles 243K & 243ZA)",
            "stem_en": "How does the bar on interference by courts in electoral matters under Articles 243-O(b) and 243ZG(b) interact with High Courts' writ jurisdiction under Article 226?",
            "stem_ta": "சரத்துகள் 243-O(b) மற்றும் 243ZG(b)-ன் கீழ் தேர்தல் விவகாரங்களில் நீதிமன்றங்கள் தலையிடுவதற்கான தடையானது, சரத்து 226-ன் கீழ் உயர் நீதிமன்றங்களின் நீதிப்பேராணை அதிகார வரம்புடன் எவ்வாறு தொடர்பு கொள்கிறது?",
            "options": [
                ("High Courts cannot stall the election process midway; challenges can only be raised after election via election petition, unless writ is in aid of election", "உயர் நீதிமன்றங்கள் தேர்தல் செயல்முறையை பாதியில் நிறுத்த முடியாது; தேர்தல் மனு மூலமே தேர்தல் முடிந்த பிறகு சவால் செய்ய முடியும், தேர்தல் நடைபெற உதவும் மனுக்கள் தவிர"),
                ("Article 226 completely overrides Article 243-O, allowing High Courts to stay polling at any stage unconditionally", "சரத்து 226 சரத்து 243-O வை முற்றிலும் முறியடித்து, உயர் நீதிமன்றங்கள் எந்த நிலையிலும் வாக்கெடுப்பை நிபந்தனையின்றி நிறுத்தி வைக்க அனுமதிக்கிறது"),
                ("Article 243-O completely extinguishes Article 226 powers, permanently barring all election petitions in judicial courts", "சரத்து 243-O சரத்து 226 அதிகாரங்களை முழுமையாக ஒழித்து, நீதிமன்றங்களில் அனைத்து தேர்தல் மனுக்களையும் நிரந்தரமாகத் தடை செய்கிறது"),
                ("Only the Supreme Court has jurisdiction under Article 32, while High Courts possess zero power over local elections", "உயர் நீதிமன்றங்களுக்கு உள்ளாட்சித் தேர்தல்கள் மீது பூஜ்ஜிய அதிகாரம் உள்ள நிலையில், உச்ச நீதிமன்றத்திற்கு மட்டுமே சரத்து 32-ன் கீழ் அதிகாரம் உண்டு")
            ],
            "correct_key": "A",
            "exp_en": "As settled in Mohinder Singh Gill (1977) and applied to local bodies in Kishan Singh Tomar (2006), once the election process begins, courts will not interfere or stall polling under Art 226. Aggrieved parties must file an election petition after results, except where writ petitions facilitate the election.",
            "exp_ta": "மொகிந்தர் சிங் கில் (1977) மற்றும் கிஷன் சிங் தோமர் (2006) வழக்குகளின்படி, தேர்தல் செயல்முறை தொடங்கியவுடன், சரத்து 226-ன் கீழ் நீதிமன்றங்கள் தலையிடவோ அல்லது தேர்தலை நிறுத்தவோ செய்யாது. தேர்தல் நடைபெற உதவும் மனுக்கள் தவிர, தேர்தல் முடிவுகளுக்குப் பின்னரே தேர்தல் மனு தாக்கல் செய்யப்பட வேண்டும்.",
            "why_a_en": "Correct. Stalling elections midway is prohibited; post-election petition is the constitutional remedy.",
            "why_a_ta": "சரி. நடுவழியில் தேர்தலை நிறுத்துவது தடைசெய்யப்பட்டுள்ளது; தேர்தலுக்குப் பிந்தைய தேர்தல் மனுவே அரசியலமைப்புத் தீர்வு.",
            "why_b_en": "Incorrect. Courts practice judicial self-restraint and cannot routinely stay ongoing elections.",
            "why_b_ta": "தவறு. நீதிமன்றங்கள் சுயக்கட்டுப்பாட்டைப் பயிற்சி செய்கின்றன, வழக்கமாக நடக்கும் தேர்தலைத் தடை செய்ய முடியாது.",
            "why_c_en": "Incorrect. Article 226 is part of basic structure and cannot be permanently extinguished.",
            "why_c_ta": "தவறு. சரத்து 226 அடிப்படை கட்டமைப்பின் ஒரு பகுதியாகும், அதை நிரந்தரமாக ஒழிக்க முடியாது.",
            "why_d_en": "Incorrect. High Courts hear election matters and election petitions designated by state law.",
            "why_d_ta": "தவறு. மாநில சட்டத்தால் நியமிக்கப்பட்ட தேர்தல் மனுக்களை உயர் நீதிமன்றங்கள் விசாரிக்கின்றன.",
            "tip_en": "Article 243-O(b) / 243ZG(b): Election can be questioned ONLY through an Election Petition presented to specified authority.",
            "tip_ta": "சரத்து 243-O(b) / 243ZG(b): குறிப்பிட்ட அதிகாரியிடம் தாக்கல் செய்யப்படும் தேர்தல் மனு மூலமாக மட்டுமே தேர்தலை எதிர்த்து கேள்வி கேட்க முடியும்.",
            "fact_en": "Delimitation of constituencies under 243-O(a) cannot be questioned in any court once finalized.",
            "fact_ta": "சரத்து 243-O(a)-ன் கீழ் தொகுதிகள் மறுவரையறை செய்யப்பட்டதை இறுதி செய்த பிறகு எந்த நீதிமன்றத்திலும் கேள்வி கேட்க முடியாது."
        },

        # 3. SEC Consultation on Disqualification
        {
            "subtopic": "State Election Commissioner - Appointment, Tenure, Removal & Autonomy",
            "stem_en": "Under Article 243V(2) of the Constitution, if any question arises as to whether a member of a Municipality has become subject to disqualification, to whom is the question referred?",
            "stem_ta": "அரசியலமைப்பின் சரத்து 243V(2)-ன் கீழ், ஒரு நகராட்சியின் உறுப்பினர் தகுதியிழப்பிற்கு ஆளாகிவிட்டாரா என்பது குறித்து ஏதேனும் கேள்வி எழுந்தால், அக்கேள்வி யாரிடம் பரிந்துரைக்கப்படுகிறது?",
            "options": [
                ("Such authority and in such manner as the Legislature of a State may, by law, provide", "மாநில சட்டமன்றம் சட்டத்தின் மூலம் வழங்கும் அத்தகைய அதிகாரம் மற்றும் அத்தகைய முறையில்"),
                ("Mandatorily to the Governor whose personal decision is final without right of appeal", "கட்டாயமாக ஆளுநரிடம், அவருடைய தனிப்பட்ட முடிவே மேல்முறையீட்டு உரிமையின்றி இறுதியானது"),
                ("Directly to the Chief Election Commissioner of India in New Delhi", "புது தில்லியில் உள்ள இந்திய தலைமை தேர்தல் ஆணையரிடம் நேரடியாக"),
                ("To the Mayor or Municipal Commissioner whose decision cannot be challenged", "மேயர் அல்லது நகராட்சி ஆணையரிடம், அவர்களுடைய முடிவை எதிர்க்க முடியாது")
            ],
            "correct_key": "A",
            "exp_en": "Under Article 243V(2) (for Municipalities) and Article 243F(2) (for Panchayats), questions of disqualification are referred to such authority as the State Legislature provides by law. In many states, this is designated as the State Election Commission or District Court.",
            "exp_ta": "சரத்து 243V(2) (நகராட்சிகள்) மற்றும் சரத்து 243F(2) (பஞ்சாயத்துகள்)-ன் கீழ், தகுதியிழப்பு பற்றிய கேள்விகள் மாநில சட்டமன்றம் சட்டத்தின் மூலம் வழங்கும் அதிகாரியிடம் பரிந்துரைக்கப்படும். பல மாநிலங்களில் இது மாநில தேர்தல் ஆணையம் அல்லது மாவட்ட நீதிமன்றமாக நிர்ணயிக்கப்பட்டுள்ளது.",
            "why_a_en": "Correct. The constitutional text explicitly delegates the determination mechanism to state law.",
            "why_a_ta": "சரி. அரசியலமைப்பு உரை தீர்மானிக்கும் வழிமுறையை மாநில சட்டத்திற்கு வெளிப்படையாக வழங்குகிறது.",
            "why_b_en": "Incorrect. Governor decides MLA/MLC disqualification under Art 192, not local body members under 243V/243F.",
            "why_b_ta": "தவறு. ஆளுநர் சரத்து 192-ன் கீழ் MLA/MLC தகுதியிழப்பைத் தீர்மானிக்கிறார், உள்ளாட்சி உறுப்பினர்களை அல்ல.",
            "why_c_en": "Incorrect. CEC of India has no role in local body member disqualifications.",
            "why_c_ta": "தவறு. உள்ளாட்சி உறுப்பினர் தகுதியிழப்பில் இந்திய CEC-க்கு எந்த பங்கும் இல்லை.",
            "why_d_en": "Incorrect. Mayors or Commissioners do not hold constitutional adjudicatory authority for member disqualification.",
            "why_d_ta": "தவறு. மேயர்கள் அல்லது ஆணையர்களுக்கு உறுப்பினர் தகுதியிழப்பு குறித்த தீர்ப்பு அதிகாரம் இல்லை.",
            "tip_en": "Contrast: Art 192 (MLAs - Governor on ECI opinion) vs Art 243F/243V (Local Bodies - Authority provided by State law).",
            "tip_ta": "வேறுபாடு: சரத்து 192 (MLAs - ECI கருத்தின்படி ஆளுநர்) vs சரத்து 243F/243V (உள்ளாட்சி - மாநில சட்டத்தால் குறிப்பிடப்பட்ட அதிகாரி).",
            "fact_en": "In Tamil Nadu, disputes regarding disqualification of panchayat members are referred to the District Judge under Sec 41 of TN Panchayats Act 1994.",
            "fact_ta": "தமிழ்நாட்டில், பஞ்சாயத்து உறுப்பினர்களின் தகுதியிழப்பு குறித்த சர்ச்சைகள் 1994 தமிழ்நாடு பஞ்சாயத்துகள் சட்டத்தின் பிரிவு 41-ன் கீழ் மாவட்ட நீதிபதியிடம் பரிந்துரைக்கப்படுகின்றன."
        },

        # 4. State Finance Commission Recommendations Action Taken
        {
            "subtopic": "State Finance Commission - Constitutional Mandate, Composition & Role (Articles 243I & 243Y)",
            "stem_en": "According to Article 243-I(4), what constitutional obligation rests on the Governor regarding the recommendations made by the State Finance Commission?",
            "stem_ta": "சரத்து 243-I(4)-ன் படி, மாநில நிதி ஆணையம் அளித்த பரிந்துரைகள் தொடர்பாக ஆளுநரின் அரசியலமைப்பு கடமை என்ன?",
            "options": [
                ("Cause every recommendation together with an explanatory memorandum as to action taken to be laid before the Legislature of the State", "ஒவ்வொரு பரிந்துரையையும் அதன் மீது எடுக்கப்பட்ட நடவடிக்கை குறித்த விளக்கக் குறிப்புடன் மாநில சட்டமன்றத்தின் முன் வைக்கச் செய்தல்"),
                ("Personally amend the state budget to implement 100% of the recommendations without legislative debate", "சட்டமன்ற விவாதமின்றி 100% பரிந்துரைகளை நடைமுறைப்படுத்த மாநில பட்ஜெட்டை தனிப்பட்ட முறையில் திருத்துதல்"),
                ("Forward the recommendations solely to the Union Finance Minister for central cabinet approval", "மத்திய அமைச்சரவை ஒப்புதலுக்காக பரிந்துரைகளை மத்திய நிதி அமைச்சருக்கு மட்டுமே அனுப்புதல்"),
                ("Publish the report in the Official Gazette but withhold it from the Legislative Assembly if revenue is deficient", "அறிக்கையை அதிகாரப்பூர்வ அரசிதழில் வெளியிட வேண்டும் ஆனால் வருவாய் பற்றாக்குறை இருந்தால் சட்டமன்றத்தில் இருந்து நிறுத்தி வைக்கலாம்")
            ],
            "correct_key": "A",
            "exp_en": "Article 243-I(4) mandates that the Governor shall cause every recommendation made by the State Finance Commission together with an explanatory memorandum as to the action taken thereon to be laid before the Legislature of the State.",
            "exp_ta": "சரத்து 243-I(4) மாநில நிதி ஆணையம் அளித்த ஒவ்வொரு பரிந்துரையையும் அதன் மீது எடுக்கப்பட்ட நடவடிக்கை குறித்த விளக்கக் குறிப்புடன் மாநில சட்டமன்றத்தின் முன் ஆளுநர் வைக்கச் செய்ய வேண்டும் என்று கட்டாயப்படுத்துகிறது.",
            "why_a_en": "Correct. Verbatim constitutional mandate of Article 243-I(4) and 243Y(2).",
            "why_a_ta": "சரி. சரத்து 243-I(4) மற்றும் 243Y(2)-ன் சரியான அரசியலமைப்பு கட்டளை.",
            "why_b_en": "Incorrect. Governor cannot unilaterally alter the budget; money bills require legislative passage.",
            "why_b_ta": "தவறு. ஆளுநர் ஒருதலைப்பட்சமாக பட்ஜெட்டை மாற்ற முடியாது; நிதி மசோதாக்கள் சட்டமன்ற ஒப்புதல் பெற வேண்டும்.",
            "why_c_en": "Incorrect. SFC reports are state legislative documents, not routed for Union Cabinet approval.",
            "why_c_ta": "தவறு. SFC அறிக்கைகள் மாநில சட்டமன்ற ஆவணங்கள், மத்திய அமைச்சரவை ஒப்புதலுக்கு அல்ல.",
            "why_d_en": "Incorrect. Tabling before the Legislature is a non-negotiable constitutional mandate.",
            "why_d_ta": "தவறு. சட்டமன்றத்தில் சமர்ப்பிப்பது பேச்சுவார்த்தைக்கு இடமில்லாத அரசியலமைப்பு கடமையாகும்.",
            "tip_en": "Article 281 is for Central Finance Commission (laid before Parliament); Article 243-I(4) is for SFC (laid before State Legislature).",
            "tip_ta": "சரத்து 281 மத்திய நிதி ஆணையத்திற்கான (நாடாளுமன்றம்); சரத்து 243-I(4) மாநில நிதி ஆணையத்திற்கான (மாநில சட்டமன்றம்).",
            "fact_en": "The Action Taken Report (ATR) must explicitly explain which SFC recommendations are accepted, modified, or rejected with reasons.",
            "fact_ta": "எடுக்கப்பட்ட நடவடிக்கை அறிக்கை (ATR) எந்த SFC பரிந்துரைகள் ஏற்றுக்கொள்ளப்பட்டன, மாற்றப்பட்டன அல்லது நிராகரிக்கப்பட்டன என்பதை காரணங்களுடன் விளக்க வேண்டும்."
        },

        # 5. Central Finance Commission Linkage (Article 280(3)(bb) & 280(3)(c))
        {
            "subtopic": "Financial Devolution, Intergovernmental Transfers & Local Governance",
            "stem_en": "Which constitutional amendments inserted sub-clauses (bb) and (c) into Article 280(3) to link the Central Finance Commission with State Finance Commissions?",
            "stem_ta": "மத்திய நிதி ஆணையத்தை மாநில நிதி ஆணையங்களுடன் இணைக்க சரத்து 280(3)-ல் உட்பிரிவுகள் (bb) மற்றும் (c)-ஐ சேர்த்த அரசியலமைப்பு திருத்தங்கள் எவை?",
            "options": [
                ("73rd and 74th Constitutional Amendment Acts, 1992", "73வது மற்றும் 74வது அரசியலமைப்பு திருத்தச் சட்டங்கள், 1992"),
                ("42nd and 44th Constitutional Amendment Acts, 1976 and 1978", "42வது மற்றும் 44வது அரசியலமைப்பு திருத்தச் சட்டங்கள், 1976 மற்றும் 1978"),
                ("86th and 91st Constitutional Amendment Acts, 2002 and 2003", "86வது மற்றும் 91வது அரசியலமைப்பு திருத்தச் சட்டங்கள், 2002 மற்றும் 2003"),
                ("101st and 103rd Constitutional Amendment Acts, 2016 and 2019", "101வது மற்றும் 103வது அரசியலமைப்பு திருத்தச் சட்டங்கள், 2016 மற்றும் 2019")
            ],
            "correct_key": "A",
            "exp_en": "The 73rd and 74th Amendment Acts inserted Article 280(3)(bb) and (c) requiring the Central Finance Commission to recommend measures needed to augment the Consolidated Fund of a State to supplement the resources of the Panchayats and Municipalities on the basis of the recommendations made by the SFC.",
            "exp_ta": "73வது மற்றும் 74வது திருத்தச் சட்டங்கள் சரத்து 280(3)(bb) மற்றும் (c)-ஐ சேர்த்தன. இது மாநில நிதி ஆணையத்தின் பரிந்துரைகளின் அடிப்படையில் பஞ்சாயத்துகள் மற்றும் நகராட்சிகளின் வளங்களை அதிகரிக்க மாநிலத்தின் தொகுப்பு நிதியை பெருக்குவதற்கு தேவையான நடவடிக்கைகளை மத்திய நிதி ஆணையம் பரிந்துரைக்க வேண்டும் என்று கூறுகிறது.",
            "why_a_en": "Correct. 73rd added 280(3)(bb) for Panchayats, 74th added 280(3)(c) for Municipalities.",
            "why_a_ta": "சரி. 73வது திருத்தம் பஞ்சாயத்துகளுக்கு 280(3)(bb)-யும், 74வது நகராட்சிகளுக்கு 280(3)(c)-யும் சேர்த்தது.",
            "why_b_en": "Incorrect. 42nd and 44th amendments predated the constitutionalization of local self-government.",
            "why_b_ta": "தவறு. 42வது மற்றும் 44வது திருத்தங்கள் உள்ளாட்சி அமைப்புகளின் அரசியலமைப்பு அங்கீகாரத்திற்கு முந்தையவை.",
            "why_c_en": "Incorrect. 86th is Right to Education; 91st limited Cabinet size.",
            "why_c_ta": "தவறு. 86வது கல்வி உரிமை; 91வது அமைச்சரவை அளவைக் கட்டுப்படுத்தியது.",
            "why_d_en": "Incorrect. 101st is GST; 103rd is EWS reservation.",
            "why_d_ta": "தவறு. 101வது GST; 103வது EWS இடஒதுக்கீடு.",
            "tip_en": "Art 280(3)(bb) = Panchayats; Art 280(3)(c) = Municipalities; both rely 'on the basis of recommendations of the SFC'.",
            "tip_ta": "சரத்து 280(3)(bb) = பஞ்சாயத்துகள்; சரத்து 280(3)(c) = நகராட்சிகள்; இரண்டும் 'SFC பரிந்துரைகளின் அடிப்படையில்' இயங்குகின்றன.",
            "fact_en": "If an SFC is not constituted on time, the Central Finance Commission can make its own independent assessment to grant funds.",
            "fact_ta": "SFC சரியான நேரத்தில் அமைக்கப்படாவிட்டால், நிதி வழங்க மத்திய நிதி ஆணையம் தனது சொந்த சுயாதீன மதிப்பீட்டைச் செய்யலாம்."
        },

        # 6. Bharathi Reddy Case (2016) - Disqualification & Election Petitions
        {
            "subtopic": "State Election Commission - Constitutional Mandate & Provisions (Articles 243K & 243ZA)",
            "stem_en": "In Bharathi Reddy v. State of Karnataka (2016), what principle did the Supreme Court lay down regarding High Court jurisdiction in local body election disputes?",
            "stem_ta": "பாரதி ரெட்டி எதிர் கர்நாடக அரசு (2016) வழக்கில், உள்ளாட்சித் தேர்தல் சர்ச்சைகளில் உயர் நீதிமன்ற அதிகார வரம்பு குறித்து உச்ச நீதிமன்றம் என்ன கொள்கையை வகுத்தது?",
            "options": [
                ("High Court can exercise Article 226 powers to issue a writ of quo warranto if an elected member lacks fundamental constitutional qualifications", "தேர்ந்தெடுக்கப்பட்ட உறுப்பினர் அடிப்படை அரசியலமைப்பு தகுதிகளைக் கொண்டிருக்கவில்லை என்றால் தகுதி வினவு நீதிப்பேராணை (quo warranto) பிறப்பிக்க உயர் நீதிமன்றம் சரத்து 226-ஐப் பயன்படுத்தலாம்"),
                ("Article 243-O places an absolute and impenetrable bar on quo warranto writs even if a candidate is not an Indian citizen", "ஒரு வேட்பாளர் இந்திய குடிமகனாக இல்லாவிட்டாலும் கூட சரத்து 243-O தகுதி வினவு நீதிப்பேராணைக்கு முழுமையான தடையை விதிக்கிறது"),
                ("Election tribunals have exclusive authority to amend the Constitution to disqualify sitting members", "பதவியில் உள்ள உறுப்பினர்களை தகுதி நீக்கம் செய்ய அரசியலமைப்பைத் திருத்த தேர்தல் தீர்ப்பாயங்களுக்கு மட்டுமே பிரத்யேக அதிகாரம் உண்டு"),
                ("State Election Commissions can overrule High Court writs through an executive resolution", "மாநில தேர்தல் ஆணையங்கள் ஒரு நிர்வாக தீர்மானத்தின் மூலம் உயர் நீதிமன்ற நீதிப்பேராணைகளை ரத்து செய்ய முடியும்")
            ],
            "correct_key": "A",
            "exp_en": "In Bharathi Reddy (2016), the Supreme Court clarified that despite the bar under Article 243-O, a writ of quo warranto under Article 226 lies if an elected representative is disqualified ab initio or lacks statutory eligibility, as an usurper of public office cannot seek shelter behind Article 243-O.",
            "exp_ta": "பாரதி ரெட்டி (2016) வழக்கில், சரத்து 243-O-ன் கீழ் தடை இருந்தபோதிலும், தேர்ந்தெடுக்கப்பட்ட பிரதிநிதி ஆரம்பத்திலிருந்தே தகுதியற்றவராக இருந்தாலோ அல்லது சட்டப்பூர்வ தகுதி இல்லாமலிருந்தாலோ சரத்து 226-ன் கீழ் தகுதி வினவு நீதிப்பேராணை தாக்கல் செய்யலாம் என்று உச்ச நீதிமன்றம் தெளிவுபடுத்தியது.",
            "why_a_en": "Correct. Quo warranto remains maintainable when a candidate lacks basic constitutional or statutory qualifications.",
            "why_a_ta": "சரி. ஒரு வேட்பாளர் அடிப்படை தகுதிகளைக் கொண்டிருக்காதபோது தகுதி வினவு நீதிப்பேராணை செல்லுபடியாகும்.",
            "why_b_en": "Incorrect. Article 243-O does not protect a complete usurper from quo warranto.",
            "why_b_ta": "தவறு. சரத்து 243-O ஒரு ஆக்கிரமிப்பாளரை தகுதி வினவு மனுவிலிருந்து பாதுகாக்காது.",
            "why_c_en": "Incorrect. Election tribunals cannot amend the Constitution.",
            "why_c_ta": "தவறு. தேர்தல் தீர்ப்பாயங்கள் அரசியலமைப்பைத் திருத்த முடியாது.",
            "why_d_en": "Incorrect. Executive or SEC resolutions cannot override High Court constitutional writs.",
            "why_d_ta": "தவறு. நிர்வாக அல்லது SEC தீர்மானங்கள் உயர் நீதிமன்ற நீதிப்பேராணைகளை ரத்து செய்ய முடியாது.",
            "tip_en": "Quo warranto questions: 'By what authority do you hold this public office?'",
            "tip_ta": "தகுதி வினவு நீதிப்பேராணை கேள்வி: 'எந்த அதிகாரத்தின் அடிப்படையில் நீங்கள் இந்தப் பொதுப் பதவியை வகிக்கிறீர்கள்?'",
            "fact_en": "The SC reconciled judicial review under Art 226 (basic structure) with Art 243-O/243ZG.",
            "fact_ta": "உச்ச நீதிமன்றம் சரத்து 226-ன் கீழ் நீதித்துறை மறுஆய்வை சரத்து 243-O/243ZG உடன் சமரசம் செய்தது."
        },

        # 7. TN SFC Terms of Reference & Horizontal vs Vertical Devolution
        {
            "subtopic": "Tamil Nadu State Election & Finance Commissions - Legal Framework, Rules & Precedents",
            "stem_en": "Under the recommendations of the Fifth and Sixth State Finance Commissions in Tamil Nadu, which ratio was traditionally recommended for the horizontal sharing of devolution funds between Rural Local Bodies and Urban Local Bodies?",
            "stem_ta": "தமிழ்நாட்டின் ஐந்தாவது மற்றும் ஆறாவது மாநில நிதி ஆணையங்களின் பரிந்துரைகளின் கீழ், ஊரக உள்ளாட்சி அமைப்புகளுக்கும் நகர்ப்புற உள்ளாட்சி அமைப்புகளுக்கும் இடையே நிதிப் பகிர்வுக்கான கிடைமட்ட விகிதம் பாரம்பரியமாக என்ன பரிந்துரைக்கப்பட்டது?",
            "options": [
                ("56 : 44 (56% to Rural Local Bodies and 44% to Urban Local Bodies)", "56 : 44 (ஊரக உள்ளாட்சி அமைப்புகளுக்கு 56% மற்றும் நகர்ப்புற உள்ளாட்சி அமைப்புகளுக்கு 44%)"),
                ("80 : 20 (80% to Rural Local Bodies and 20% to Urban Local Bodies)", "80 : 20 (ஊரக உள்ளாட்சி அமைப்புகளுக்கு 80% மற்றும் நகர்ப்புற உள்ளாட்சி அமைப்புகளுக்கு 20%)"),
                ("30 : 70 (30% to Rural Local Bodies and 70% to Urban Local Bodies)", "30 : 70 (ஊரக உள்ளாட்சி அமைப்புகளுக்கு 30% மற்றும் நகர்ப்புற உள்ளாட்சி அமைப்புகளுக்கு 70%)"),
                ("10 : 90 (10% to Rural Local Bodies and 90% to Urban Local Bodies)", "10 : 90 (ஊரக உள்ளாட்சி அமைப்புகளுக்கு 10% மற்றும் நகர்ப்புற உள்ளாட்சி அமைப்புகளுக்கு 90%)")
            ],
            "correct_key": "A",
            "exp_en": "In Tamil Nadu, the Fifth SFC (and continued largely in subsequent frameworks) established the horizontal devolution formula of 56% to Rural Local Bodies (RLBs) and 44% to Urban Local Bodies (ULBs) from the total net State's Own Tax Revenue (SOTR) pool.",
            "exp_ta": "தமிழ்நாட்டில், ஐந்தாவது SFC (மற்றும் அடுத்தடுத்த கட்டமைப்பு) மொத்த மாநில சொந்த வரி வருவாயில் (SOTR) இருந்து ஊரக உள்ளாட்சி அமைப்புகளுக்கு (RLBs) 56% மற்றும் நகர்ப்புற உள்ளாட்சி அமைப்புகளுக்கு (ULBs) 44% என்ற கிடைமட்ட பகிர்வு சூத்திரத்தை நிறுவியது.",
            "why_a_en": "Correct. 56:44 is the established horizontal ratio between RLBs and ULBs in Tamil Nadu.",
            "why_a_ta": "சரி. 56:44 என்பது தமிழ்நாட்டில் RLBs மற்றும் ULBs இடையே நிறுவப்பட்ட கிடைமட்ட விகிதமாகும்.",
            "why_b_en": "Incorrect. 80:20 is disproportionately skewed towards rural areas.",
            "why_b_ta": "தவறு. 80:20 என்பது கிராமப்புறங்களுக்கு அதிகப்படியான சமநிலையற்றதாகும்.",
            "why_c_en": "Incorrect. 30:70 reverses the population weightage of rural Tamil Nadu.",
            "why_c_ta": "தவறு. 30:70 கிராமப்புற தமிழ்நாட்டின் மக்கள் தொகை எடையை மாற்றியமைக்கிறது.",
            "why_d_en": "Incorrect. 10:90 is completely erroneous.",
            "why_d_ta": "தவறு. 10:90 முற்றிலும் தவறானது.",
            "tip_en": "Vertical devolution in TN is ~10% of SOTR, divided horizontally 56% (Rural) : 44% (Urban).",
            "tip_ta": "TN-ல் செங்குத்துப் பகிர்வு SOTR-ல் சுமார் 10%, கிடைமட்டமாக 56% (ஊரகம்) : 44% (நகர்ப்புறம்) என பிரிக்கப்படுகிறது.",
            "fact_en": "Within Rural Local Bodies, the 56% share is further divided among Village Panchayats, Panchayat Unions, and District Panchayats.",
            "fact_ta": "ஊரக உள்ளாட்சி அமைப்புகளுக்குள், 56% பங்கானது கிராம பஞ்சாயத்துகள், பஞ்சாயத்து ஒன்றியங்கள் மற்றும் மாவட்ட பஞ்சாயத்துகளிடையே மேலும் பிரிக்கப்படுகிறது."
        },

        # 8. Tamil Nadu Three-Tier Devolution Sharing (Rural Pool)
        {
            "subtopic": "Tamil Nadu State Election & Finance Commissions - Legal Framework, Rules & Precedents",
            "stem_en": "In Tamil Nadu's rural devolution pool under SFC guidelines, which tier of the Panchayati Raj system receives the largest share of devolution for basic civic infrastructure?",
            "stem_ta": "SFC வழிகாட்டுதல்களின் கீழ் தமிழ்நாட்டின் ஊரகப் பகிர்வுத் தொகுப்பில், அடிப்படை குடிமை உள்கட்டமைப்புக்காக பஞ்சாயத்து ராஜ் அமைப்பின் எந்த அடுக்கு அதிகப் பங்கைப் பெறுகிறது?",
            "options": [
                ("Village Panchayats (approx. 55% - 60% of the rural pool)", "கிராம பஞ்சாயத்துகள் (ஊரகப் பங்கில் சுமார் 55% - 60%)"),
                ("District Panchayats (approx. 90% of the rural pool)", "மாவட்ட பஞ்சாயத்துகள் (ஊரகப் பங்கில் சுமார் 90%)"),
                ("Panchayat Unions exclusively (100% of the rural pool)", "பஞ்சாயத்து ஒன்றியங்கள் மட்டுமே (ஊரகப் பங்கில் 100%)"),
                ("The Governor's Discretionary Local Fund", "ஆளுநரின் விருப்பப்படி உள்ளாட்சி நிதி")
            ],
            "correct_key": "A",
            "exp_en": "Village Panchayats form the foundation of local service delivery (drinking water, street lights, sanitation), so the SFCs in TN allocate the lion's share (typically 55% to 60%) of the rural pool directly to Village Panchayats, with Panchayat Unions getting around 30%-37% and District Panchayats 8%-10%.",
            "exp_ta": "கிராம பஞ்சாயத்துகள் அடிப்படை உள்ளாட்சி சேவை வழங்கலின் அடித்தளமாக விளங்குவதால் (குடிநீர், தெருவிளக்குகள், சுகாதாரம்), TN-ல் உள்ள SFC-கள் கிராம பஞ்சாயத்துகளுக்கு அதிகப் பங்கை (பொதுவாக 55% முதல் 60%) நேரடியாக ஒதுக்குகின்றன; பஞ்சாயத்து ஒன்றியங்களுக்கு சுமார் 30%-37% மற்றும் மாவட்ட பஞ்சாயத்துகளுக்கு 8%-10% கிடைக்கின்றன.",
            "why_a_en": "Correct. Village Panchayats handle core civic services and receive 55-60% of the rural share.",
            "why_a_ta": "சரி. கிராம பஞ்சாயத்துகள் முக்கிய குடிமைச் சேவைகளைக் கையாளுகின்றன மற்றும் ஊரகப் பங்கில் 55-60% பெறுகின்றன.",
            "why_b_en": "Incorrect. District Panchayats are primarily supervisory and receive only 8-10%.",
            "why_b_ta": "தவறு. மாவட்ட பஞ்சாயத்துகள் மேற்பார்வை அமைப்புகளாகும், மேலும் 8-10% மட்டுமே பெறுகின்றன.",
            "why_c_en": "Incorrect. Panchayat Unions do not receive 100%.",
            "why_c_ta": "தவறு. பஞ்சாயத்து ஒன்றியங்கள் 100% பெறுவதில்லை.",
            "why_d_en": "Incorrect. There is no Governor's discretionary local fund under SFC.",
            "why_d_ta": "தவறு. SFC-ன் கீழ் ஆளுநரின் விருப்பப்படி உள்ளாட்சி நிதி எதுவும் இல்லை.",
            "tip_en": "Rural Devolution split in TN: Village Panchayats (~60%) > Panchayat Unions (~32%) > District Panchayats (~8%).",
            "tip_ta": "TN ஊரகப் பகிர்வுப் பிரிவு: கிராம பஞ்சாயத்துகள் (~60%) > பஞ்சாயத்து ஒன்றியங்கள் (~32%) > மாவட்ட பஞ்சாயத்துகள் (~8%).",
            "fact_en": "District Panchayats receive the smallest devolution share because they have no direct executive taxation or utility maintenance powers.",
            "fact_ta": "மாவட்ட பஞ்சாயத்துகளுக்கு நேரடி நிர்வாக வரிவிதிப்பு அல்லது பயன்பாட்டு பராமரிப்பு அதிகாரங்கள் இல்லாததால் அவை மிகக் குறைந்த பகிர்வுப் பங்கைப் பெறுகின்றன."
        },

        # 9. Model Code of Conduct Enforceability in Local Bodies
        {
            "subtopic": "State Election Commissioner - Appointment, Tenure, Removal & Autonomy",
            "stem_en": "What is the legal basis and timing for the enforcement of the Model Code of Conduct (MCC) by the State Election Commission during local body elections?",
            "stem_ta": "உள்ளாட்சித் தேர்தல்களின் போது மாநில தேர்தல் ஆணையத்தால் தேர்தல் நடத்தை விதிகளை (MCC) அமல்படுத்துவதற்கான சட்ட அடிப்படை மற்றும் நேரம் என்ன?",
            "options": [
                ("It comes into operational force immediately upon the formal announcement of the election schedule and derives authority from constitutional powers of superintendence under Article 243K/243ZA", "தேர்தல் அட்டவணையின் முறையான அறிவிப்பு வெளியான உடனேயே இது செயல்பாட்டுக்கு வருகிறது மற்றும் சரத்து 243K/243ZA-ன் கீழ் உள்ள அரசியலமைப்பு மேற்பார்வை அதிகாரங்களிலிருந்து அதிகாரத்தைப் பெறுகிறது"),
                ("It comes into force only 24 hours prior to the commencement of actual ballot casting under the Indian Penal Code", "இந்திய தண்டனைச் சட்டத்தின் கீழ் உண்மையான வாக்குப்பதிவு தொடங்குவதற்கு 24 மணி நேரத்திற்கு முன்பு மட்டுமே இது நடைமுறைக்கு வருகிறது"),
                ("It requires prior statutory ratification by a joint session of the State Legislature for each election cycle", "ஒவ்வொரு தேர்தல் சுழற்சிக்கும் மாநில சட்டமன்றத்தின் கூட்டுக் கூட்டத்தால் முன் சட்டப்பூர்வ ஒப்புதல் தேவைப்படுகிறது"),
                ("It applies exclusively to opposition political parties while the ruling state cabinet is entirely exempt", "இது எதிர்க்கட்சிகளுக்கு மட்டுமே பொருந்தும், அதே நேரத்தில் ஆளும் மாநில அமைச்சரவைக்கு முற்றிலும் விலக்கு அளிக்கப்பட்டுள்ளது")
            ],
            "correct_key": "A",
            "exp_en": "The Model Code of Conduct (MCC) comes into force immediately upon the announcement of election dates by the SEC, drawing plenary power from Articles 243K and 243ZA (as affirmed in Election Commission of India v. Ashok Kumar and Kishan Singh Tomar cases). It binds all parties and candidates.",
            "exp_ta": "SEC தேர்தல் தேதிகளை அறிவித்த உடனேயே தேர்தல் நடத்தை விதிகள் (MCC) நடைமுறைக்கு வருகின்றன, இது சரத்துகள் 243K மற்றும் 243ZA-லிருந்து முழு அதிகாரத்தைப் பெறுகிறது (அசோக் குமார் மற்றும் கிஷன் சிங் தோமர் வழக்குகளில் உறுதிப்படுத்தப்பட்டது போல). இது அனைத்து கட்சிகளையும் வேட்பாளர்களையும் கட்டுப்படுத்துகிறது.",
            "why_a_en": "Correct. MCC activates on announcement date based on Art 243K/243ZA powers.",
            "why_a_ta": "சரி. சரத்து 243K/243ZA அதிகாரங்களின் அடிப்படையில் தேர்தல் அறிவிப்பு தேதியிலேயே MCC செயல்பாட்டுக்கு வருகிறது.",
            "why_b_en": "Incorrect. MCC does not wait until 24 hours before polling; 48 hours is silence period.",
            "why_b_ta": "தவறு. MCC வாக்குப்பதிவுக்கு 24 மணி நேரத்திற்கு முன் வரை காத்திருக்காது; 48 மணி நேரம் அமைதிக் காலம்.",
            "why_c_en": "Incorrect. No legislative ratification is needed for MCC implementation.",
            "why_c_ta": "தவறு. MCC அமலாக்கத்திற்கு சட்டமன்ற ஒப்புதல் தேவையில்லை.",
            "why_d_en": "Incorrect. MCC applies uniformly to ruling party and opposition alike.",
            "why_d_ta": "தவறு. MCC ஆளும் கட்சி மற்றும் எதிர்க்கட்சி ஆகிய இரு தரப்பிற்கும் ஒரே மாதிரியாகப் பொருந்தும்.",
            "tip_en": "MCC takes effect the moment SEC / ECI issues the press note announcing the election schedule.",
            "tip_ta": "SEC / ECI தேர்தல் அட்டவணையை அறிவிக்கும் செய்திக் குறிப்பை வெளியிட்ட தருணத்தில் MCC நடைமுறைக்கு வருகிறது.",
            "fact_en": "Ministers are barred from announcing new financial grants or schemes once the MCC is operational.",
            "fact_ta": "MCC செயல்பாட்டிற்கு வந்தவுடன் அமைச்சர்கள் புதிய நிதி மானியங்கள் அல்லது திட்டங்களை அறிவிக்கத் தடை விதிக்கப்பட்டுள்ளது."
        },

        # 10. Direct vs Indirect Elections in Tamil Nadu Local Governance
        {
            "subtopic": "Tamil Nadu State Election & Finance Commissions - Legal Framework, Rules & Precedents",
            "stem_en": "In the local governance architecture of Tamil Nadu, which of the following pairs of offices are filled via DIRECT election by registered voters?",
            "stem_ta": "தமிழ்நாட்டின் உள்ளாட்சி நிர்வாகக் கட்டமைப்பில், பதிவுசெய்யப்பட்ட வாக்காளர்களால் நேரடித் தேர்தல் மூலம் பின்வரும் எந்த ஜோடிப் பதவிகள் நிரப்பப்படுகின்றன?",
            "options": [
                ("Village Panchayat President and Village Panchayat Ward Member", "கிராம பஞ்சாயத்து தலைவர் மற்றும் கிராம பஞ்சாயத்து வார்டு உறுப்பினர்"),
                ("Panchayat Union Chairman and District Panchayat Chairman", "பஞ்சாயத்து ஒன்றியத் தலைவர் மற்றும் மாவட்ட பஞ்சாயத்து தலைவர்"),
                ("Municipal Corporation Mayor (under 2019/2022 amended rules) and Panchayat Union Chairman", "மாநகராட்சி மேயர் (2019/2022 திருத்தப்பட்ட விதிகளின் கீழ்) மற்றும் பஞ்சாயத்து ஒன்றியத் தலைவர்"),
                ("District Panchayat Chairman and Municipal Corporation Mayor", "மாவட்ட பஞ்சாயத்து தலைவர் மற்றும் மாநகராட்சி மேயர்")
            ],
            "correct_key": "A",
            "exp_en": "In Tamil Nadu, the Village Panchayat President and Village Panchayat Ward Members (as well as Ward Councillors of Panchayat Unions, District Panchayats, Municipalities, and Corporations) are directly elected. Panchayat Union Chairmen, District Panchayat Chairmen, and currently Mayors/Municipal Chairmen are elected indirectly by and from among the elected councillors.",
            "exp_ta": "தமிழ்நாட்டில், கிராம பஞ்சாயத்து தலைவர் மற்றும் கிராம பஞ்சாயத்து வார்டு உறுப்பினர்கள் (மற்றும் பஞ்சாயத்து ஒன்றியங்கள், மாவட்ட பஞ்சாயத்துகள், நகராட்சிகள் மற்றும் மாநகராட்சிகளின் வார்டு கவுன்சிலர்கள்) நேரடியாக தேர்ந்தெடுக்கப்படுகிறார்கள். பஞ்சாயத்து ஒன்றியத் தலைவர்கள், மாவட்ட பஞ்சாயத்து தலைவர்கள் மற்றும் தற்போது மேயர்கள்/நகராட்சித் தலைவர்கள் தேர்ந்தெடுக்கப்பட்ட கவுன்சிலர்களால் மறைமுகமாக தேர்ந்தெடுக்கப்படுகிறார்கள்.",
            "why_a_en": "Correct. Village Panchayat Presidents and Ward Members are directly elected by voters.",
            "why_a_ta": "சரி. கிராம பஞ்சாயத்து தலைவர்கள் மற்றும் வார்டு உறுப்பினர்கள் வாக்காளர்களால் நேரடியாக தேர்ந்தெடுக்கப்படுகிறார்கள்.",
            "why_b_en": "Incorrect. Panchayat Union and District Panchayat Chairmen are elected indirectly.",
            "why_b_ta": "தவறு. பஞ்சாயத்து ஒன்றிய மற்றும் மாவட்ட பஞ்சாயத்து தலைவர்கள் மறைமுகமாக தேர்ந்தெடுக்கப்படுகிறார்கள்.",
            "why_c_en": "Incorrect. Mayors and PU Chairmen are currently elected indirectly by councillors in TN.",
            "why_c_ta": "தவறு. மேயர்கள் மற்றும் PU தலைவர்கள் தற்போது TN-ல் கவுன்சிலர்களால் மறைமுகமாக தேர்ந்தெடுக்கப்படுகிறார்கள்.",
            "why_d_en": "Incorrect. Both District Panchayat Chairman and Mayor are indirect elections.",
            "why_d_ta": "தவறு. மாவட்ட பஞ்சாயத்து தலைவர் மற்றும் மேயர் ஆகிய இருவரும் மறைமுகத் தேர்தல்கள் மூலம் தேர்ந்தெடுக்கப்படுகின்றனர்.",
            "tip_en": "In TN: Direct = Village Panchayat President & all Ward Councillors. Indirect = PU Chairman, DP Chairman, Mayor, Municipal Chairman.",
            "tip_ta": "TN-ல்: நேரடி = கிராம பஞ்சாயத்து தலைவர் & அனைத்து வார்டு கவுன்சிலர்கள். மறைமுக = ஒன்றிய தலைவர், மாவட்ட தலைவர், மேயர், நகராட்சி தலைவர்.",
            "fact_en": "Non-party direct election is practiced for Village Panchayat President and Village Panchayat Ward Members in Tamil Nadu.",
            "fact_ta": "தமிழ்நாட்டில் கிராம பஞ்சாயத்து தலைவர் மற்றும் வார்டு உறுப்பினர்களுக்கு கட்சி சாரா நேரடித் தேர்தல் நடைமுறையில் உள்ளது."
        },

        # 11. Article 243-O Delimitation Immunity
        {
            "subtopic": "State Election Commission - Constitutional Mandate & Provisions (Articles 243K & 243ZA)",
            "stem_en": "Under Article 243-O(a) of the Constitution, what protection is afforded to the delimitation of constituencies and allotment of seats?",
            "stem_ta": "அரசியலமைப்பின் சரத்து 243-O(a)-ன் கீழ், தொகுதிகள் மறுவரையறை மற்றும் இடங்கள் ஒதுக்கீட்டிற்கு என்ன பாதுகாப்பு வழங்கப்படுகிறது?",
            "options": [
                ("The validity of any law relating to the delimitation of constituencies or allotment of seats shall not be called in question in any court", "தொகுதிகள் மறுவரையறை அல்லது இடங்கள் ஒதுக்கீடு தொடர்பான எந்தவொரு சட்டத்தின் செல்லுபடியாகும் தன்மையையும் எந்த நீதிமன்றத்திலும் கேள்வி கேட்க முடியாது"),
                ("Delimitation orders can be stayed by any District Munsif Court on an ex-parte injunction", "எந்தவொரு மாவட்ட முunsif நீதிமன்றமும் ஒருதலைப்பட்ச இடைக்காலத் தடையாணை மூலம் மறுவரையறை உத்தரவுகளை நிறுத்தி வைக்கலாம்"),
                ("Delimitation must be re-conducted every year before any casual vacancy can be filled", "எந்தவொரு தற்காலிக காலியிடத்தையும் நிரப்புவதற்கு முன் ஒவ்வொரு ஆண்டும் மறுவரையறை மீண்டும் நடத்தப்பட வேண்டும்"),
                ("The State Election Commissioner can unilaterally alter assembly constituencies under this clause", "மாநில தேர்தல் ஆணையர் இந்த விதியின் கீழ் சட்டமன்றத் தொகுதிகளை ஒருதலைப்பட்சமாக மாற்ற முடியும்")
            ],
            "correct_key": "A",
            "exp_en": "Article 243-O(a) explicitly provides: 'The validity of any law relating to the delimitation of constituencies or the allotment of seats to such constituencies, made or purporting to be made under article 243K, shall not be called in question in any court.'",
            "exp_ta": "சரத்து 243-O(a) வெளிப்படையாகக் கூறுகிறது: 'சரத்து 243K-ன் கீழ் உருவாக்கப்பட்ட அல்லது உருவாக்கப்பட்டதாகக் கூறப்படும் தொகுதிகள் மறுவரையறை அல்லது இடங்கள் ஒதுக்கீடு தொடர்பான எந்தவொரு சட்டத்தின் செல்லுபடியாகும் தன்மையையும் எந்த நீதிமன்றத்திலும் கேள்வி கேட்க முடியாது.'",
            "why_a_en": "Correct. Verbatim constitutional protection granted by Article 243-O(a).",
            "why_a_ta": "சரி. சரத்து 243-O(a)-ல் வழங்கப்பட்ட சரியான அரசியலமைப்புப் பாதுகாப்பு.",
            "why_b_en": "Incorrect. Civil courts have no jurisdiction to stall delimitation.",
            "why_b_ta": "தவறு. மறுவரையறையை நிறுத்த சிவில் நீதிமன்றங்களுக்கு அதிகாரம் இல்லை.",
            "why_c_en": "Incorrect. Delimitation is not conducted annually.",
            "why_c_ta": "தவறு. மறுவரையறை ஆண்டுதோறும் நடத்தப்படுவதில்லை.",
            "why_d_en": "Incorrect. Assembly constituencies are delimited by Central Delimitation Commission, not SEC.",
            "why_d_ta": "தவறு. சட்டமன்றத் தொகுதிகள் மத்திய மறுவரையறை ஆணையத்தால் மறுவரையறை செய்யப்படுகின்றன, SEC அல்ல.",
            "tip_en": "Article 243-O(a) mirrors Article 329(a) (bar on interference in parliamentary delimitation).",
            "tip_ta": "சரத்து 243-O(a) சரத்து 329(a)-ஐப் பிரதிபலிக்கிறது (நாடாளுமன்ற மறுவரையறையில் தலையிடுவதற்கான தடை).",
            "fact_en": "The Meghraj Kothari (1967) ruling on delimitation finality applies equally to local body delimitation under 243-O.",
            "fact_ta": "மறுவரையறை இறுதித்தன்மை குறித்த மேக்ராஜ் கோத்தாரி (1967) தீர்ப்பு சரத்து 243-O-ன் கீழ் உள்ளாட்சி மறுவரையறைக்கும் பொருந்தும்."
        },

        # 12. State Finance Commission - Qualifications of Members
        {
            "subtopic": "State Finance Commission - Constitutional Mandate, Composition & Role (Articles 243I & 243Y)",
            "stem_en": "Under Article 243-I(2), who is constitutionally empowered to determine the qualifications of members of the State Finance Commission and the manner of their selection?",
            "stem_ta": "சரத்து 243-I(2)-ன் கீழ், மாநில நிதி ஆணைய உறுப்பினர்களின் தகுதிகள் மற்றும் அவர்கள் தேர்ந்தெடுக்கப்படும் முறையைத் தீர்மானிக்க அரசியலமைப்பு ரீதியாக யாருக்கு அதிகாரம் அளிக்கப்பட்டுள்ளது?",
            "options": [
                ("The Legislature of a State, by law", "மாநில சட்டமன்றம், சட்டத்தின் மூலம்"),
                ("The Union Ministry of Finance by executive notification", "நிர்வாக அறிவிப்பின் மூலம் மத்திய நிதி அமைச்சகம்"),
                ("The Chief Justice of the respective High Court", "சம்பந்தப்பட்ட உயர் நீதிமன்ற தலைமை நீதிபதி"),
                ("The Comptroller and Auditor General of India", "இந்திய தலைமை கணக்குத் தணிக்கையாளர் (CAG)")
            ],
            "correct_key": "A",
            "exp_en": "Article 243-I(2) states: 'The Legislature of a State may, by law, determine the qualifications which shall be requisite for appointment as members of the Commission and the manner in which they shall be selected.'",
            "exp_ta": "சரத்து 243-I(2) கூறுகிறது: 'ஆணையத்தின் உறுப்பினர்களாக நியமிக்கப்படுவதற்குத் தேவையான தகுதிகளையும், அவர்கள் தேர்ந்தெடுக்கப்படும் முறையையும் மாநில சட்டமன்றம் சட்டத்தின் மூலம் தீர்மானிக்கலாம்.'",
            "why_a_en": "Correct. The State Legislature by law determines the qualifications and selection procedure.",
            "why_a_ta": "சரி. மாநில சட்டமன்றம் சட்டத்தின் மூலம் தகுதிகள் மற்றும் தேர்வு நடைமுறையைத் தீர்மானிக்கிறது.",
            "why_b_en": "Incorrect. The Union Finance Ministry does not decide State Finance Commission member qualifications.",
            "why_b_ta": "தவறு. மத்திய நிதி அமைச்சகம் மாநில நிதி ஆணைய உறுப்பினர் தகுதிகளைத் தீர்மானிப்பதில்லை.",
            "why_c_en": "Incorrect. High Court Chief Justice has no role in SFC appointments.",
            "why_c_ta": "தவறு. SFC நியமனங்களில் உயர் நீதிமன்ற தலைமை நீதிபதிக்கு எந்த பங்கும் இல்லை.",
            "why_d_en": "Incorrect. CAG does not determine SFC qualifications.",
            "why_d_ta": "தவறு. CAG SFC தகுதிகளைத் தீர்மானிப்பதில்லை.",
            "tip_en": "Art 280(2) empowers Parliament for Central FC; Art 243-I(2) empowers State Legislature for State FC.",
            "tip_ta": "சரத்து 280(2) மத்திய FC-க்கு நாடாளுமன்றத்திற்கு அதிகாரம் அளிக்கிறது; சரத்து 243-I(2) மாநில FC-க்கு மாநில சட்டமன்றத்திற்கு அதிகாரம் அளிக்கிறது.",
            "fact_en": "Section 240 of the Tamil Nadu Panchayats Act 1994 specifies that the SFC shall consist of a Chairman and not more than four other members.",
            "fact_ta": "1994 தமிழ்நாடு பஞ்சாயத்துகள் சட்டத்தின் பிரிவு 240, SFC ஒரு தலைவர் மற்றும் நான்கு உறுப்பினர்களுக்கு மிகாமல் இருக்க வேண்டும் என்று குறிப்பிடுகிறது."
        },

        # 13. Sec 239 of Tamil Nadu Panchayats Act 1994 - State Election Commissioner
        {
            "subtopic": "Tamil Nadu State Election & Finance Commissions - Legal Framework, Rules & Precedents",
            "stem_en": "Under Section 239 of the Tamil Nadu Panchayats Act, 1994, what is the maximum tenure and age limit prescribed for the Tamil Nadu State Election Commissioner?",
            "stem_ta": "1994 தமிழ்நாடு பஞ்சாயத்துகள் சட்டத்தின் பிரிவு 239-ன் கீழ், தமிழ்நாடு மாநில தேர்தல் ஆணையருக்கு நிர்ணயிக்கப்பட்டுள்ள அதிகபட்ச பதவிக்காலம் மற்றும் வயது வரம்பு என்ன?",
            "options": [
                ("A term of two years, with eligibility for reappointment up to a maximum age of 65 years", "இரண்டு ஆண்டுகள் பதவிக்காலம், அதிகபட்சமாக 65 வயது வரை மறுநியமனம் பெற தகுதி"),
                ("A single non-renewable term of six years or until attaining 70 years of age", "ஒற்றை புதுப்பிக்க முடியாத ஆறு ஆண்டுகள் பதவிக்காலம் அல்லது 70 வயதை அடையும் வரை"),
                ("A life-tenure subject only to removal by impeachment like a Supreme Court judge", "உச்ச நீதிமன்ற நீதிபதி போன்ற பதவி நீக்கம் மூலம் மட்டுமே நீக்கக்கூடிய ஆயுட்கால பதவி"),
                ("A term of ten years with unlimited eligibility for further state government postings", "மேலும் மாநில அரசுப் பணிகளுக்கு வரம்பற்ற தகுதியுடன் பத்து ஆண்டுகள் பதவிக்காலம்")
            ],
            "correct_key": "A",
            "exp_en": "Under Section 239 of the Tamil Nadu Panchayats Act 1994 and Tamil Nadu State Election Commissioner Conditions of Service Rules, the SEC holds office for a term of 2 years and is eligible for reappointment for two successive terms (subject to maximum age limit of 65 years).",
            "exp_ta": "1994 தமிழ்நாடு பஞ்சாயத்துகள் சட்டத்தின் பிரிவு 239 மற்றும் TN SEC பணி நிபந்தனைகள் விதிகளின் கீழ், SEC 2 ஆண்டுகள் பதவிக்காலம் வகிக்கிறார் மற்றும் அதிகபட்சமாக 65 வயது வரை அடுத்தடுத்த இரண்டு முறை மறுநியமனம் செய்ய தகுதியுடையவர்.",
            "why_a_en": "Correct. TN statutory rules establish a 2-year term with reappointment up to 65 years.",
            "why_a_ta": "சரி. TN சட்ட விதிகள் 65 வயது வரை மறுநியமனத்துடன் 2 ஆண்டு பதவிக்காலத்தை நிறுவுகின்றன.",
            "why_b_en": "Incorrect. 6 years / 70 years does not apply to TN SEC.",
            "why_b_ta": "தவறு. 6 ஆண்டுகள் / 70 வயது TN SEC-க்கு பொருந்தாது.",
            "why_c_en": "Incorrect. SEC does not have life tenure.",
            "why_c_ta": "தவறு. SEC-க்கு ஆயுட்கால பதவி கிடையாது.",
            "why_d_en": "Incorrect. Term is not 10 years; SEC is also barred from further government employment in the state.",
            "why_d_ta": "தவறு. பதவிக்காலம் 10 ஆண்டுகள் அல்ல; மேலும் அரசுப் பதவிகளிலிருந்தும் SEC தடை செய்யப்பட்டுள்ளார்.",
            "tip_en": "TN SEC: 2-year initial term, re-eligible up to age 65.",
            "tip_ta": "TN SEC: 2 ஆண்டு ஆரம்ப பதவிக்காலம், 65 வயது வரை மறுநியமனம் பெற தகுதி.",
            "fact_en": "On ceasing to hold office, the SEC is disqualified for further appointment under the Government of Tamil Nadu.",
            "fact_ta": "பதவியில் இருந்து விலகியவுடன், SEC தமிழ்நாடு அரசின் கீழ் மேலும் நியமனம் பெற தகுதியற்றவர் ஆகிறார்."
        },

        # 14. 15th Finance Commission Grants - Tied vs Untied Ratios
        {
            "subtopic": "Financial Devolution, Intergovernmental Transfers & Local Governance",
            "stem_en": "Under the 15th Central Finance Commission recommendations for local bodies, what condition was imposed regarding the allocation between Basic (Untied) and Tied Grants for rural local bodies?",
            "stem_ta": "உள்ளாட்சி அமைப்புகளுக்கான 15வது மத்திய நிதி ஆணையப் பரிந்துரைகளின் கீழ், ஊரக உள்ளாட்சி அமைப்புகளுக்கான அடிப்படை (கட்டுப்பாடற்ற) மற்றும் நிபந்தனைக்குட்பட்ட (Tied) மானியங்களுக்கு இடையே என்ன நிபந்தனை விதிக்கப்பட்டது?",
            "options": [
                ("Grants are split into 40% Untied and 60% Tied (specifically earmarked for sanitation, ODF, drinking water, and rainwater harvesting)", "மானியங்கள் 40% கட்டுப்பாடற்றவை மற்றும் 60% நிபந்தனைக்குட்பட்டவை என பிரிக்கப்பட்டுள்ளன (சுகாதாரம், ODF, குடிநீர் மற்றும் மழைநீர் சேகரிப்புக்காக பிரத்யேகமாக ஒதுக்கப்பட்டவை)"),
                ("100% of all grants are completely discretionary and untied with zero spending guidelines", "அனைத்து மானியங்களிலும் 100% முற்றிலும் விருப்பத்திற்குரியவை மற்றும் எந்த செலவு வழிகாட்டுதல்களும் இல்லாதவை"),
                ("Grants can only be spent on salaries of state civil servants deputed to the panchayat", "பஞ்சாயத்துக்கு அயல்பணியில் அனுப்பப்படும் மாநில அரசு ஊழியர்களின் ஊதியத்திற்கு மட்டுமே மானியங்களைச் செலவிட முடியும்"),
                ("Grants are disbursed only to Urban Municipal Corporations, completely excluding rural village panchayats", "ஊரக கிராம பஞ்சாயத்துகளை முற்றிலும் தவிர்த்து, நகர்ப்புற மாநகராட்சிகளுக்கு மட்டுமே மானியங்கள் வழங்கப்படுகின்றன")
            ],
            "correct_key": "A",
            "exp_en": "The 15th Finance Commission recommended that for rural local bodies, 40% of the grants be untied (basic grants for local needs) and 60% be tied grants specifically earmarked for drinking water supply, sanitation, maintenance of open-defecation-free (ODF) status, and rainwater harvesting.",
            "exp_ta": "15வது நிதி ஆணையம் ஊரக உள்ளாட்சி அமைப்புகளுக்கு 40% மானியங்கள் கட்டுப்பாடற்றதாகவும் (உள்ளூர் தேவைகளுக்கான அடிப்படை மானியங்கள்) மற்றும் 60% மானியங்கள் குடிநீர் விநியோகம், சுகாதாரம், திறந்தவெளி மலம் கழித்தல் இல்லாத (ODF) நிலையைப் பராமரித்தல் மற்றும் மழைநீர் சேகரிப்பு ஆகியவற்றிற்கு பிரத்யேகமாக ஒதுக்கப்பட்ட நிபந்தனைக்குட்பட்ட மானியங்களாகவும் பரிந்துரைத்தது.",
            "why_a_en": "Correct. 40% Untied and 60% Tied is the 15th FC ratio for rural local bodies.",
            "why_a_ta": "சரி. 40% கட்டுப்பாடற்றது மற்றும் 60% நிபந்தனைக்குட்பட்டது என்பது ஊரக அமைப்புகளுக்கான 15வது FC விகிதமாகும்.",
            "why_b_en": "Incorrect. Unconditional 100% untied grants were phased out from earlier commissions.",
            "why_b_ta": "தவறு. நிபந்தனையற்ற 100% மானியங்கள் முந்தைய ஆணையங்களிலிருந்து படிப்படியாக நிறுத்தப்பட்டன.",
            "why_c_en": "Incorrect. FC local body grants cannot be used for establishment salaries.",
            "why_c_ta": "தவறு. FC உள்ளாட்சி மானியங்களை நிர்வாக ஊதியங்களுக்குப் பயன்படுத்த முடியாது.",
            "why_d_en": "Incorrect. Rural local bodies receive a major portion of total local body grants.",
            "why_d_ta": "தவறு. மொத்த உள்ளாட்சி மானியங்களில் பெரும் பகுதியை ஊரக உள்ளாட்சி அமைப்புகள் பெறுகின்றன.",
            "tip_en": "15th FC: 40% Untied (flexible) + 60% Tied (WASH: Water, Sanitation, Hygiene).",
            "tip_ta": "15வது FC: 40% கட்டுப்பாடற்றவை (நெகிழ்வானவை) + 60% நிபந்தனைக்குட்பட்டவை (நீர், சுகாதாரம்).",
            "fact_en": "Release of tied grants is contingent on audited accounts and uploaded online accounting data on e-GramSwaraj.",
            "fact_ta": "e-GramSwaraj-ல் தணிக்கை செய்யப்பட்ட கணக்குகள் மற்றும் பதிவேற்றப்பட்ட கணக்குத் தரவுகளின் அடிப்படையிலேயே நிபந்தனை மானியங்கள் வெளியிடப்படுகின்றன."
        },

        # 15. Disqualification for Corrupt Practices & Election Petitions (Sec 258 TN Panchayats Act)
        {
            "subtopic": "Tamil Nadu State Election & Finance Commissions - Legal Framework, Rules & Precedents",
            "stem_en": "Under the Tamil Nadu Panchayats Act, 1994, within what time period must an election petition challenging an election be presented to the competent District Judge?",
            "stem_ta": "1994 தமிழ்நாடு பஞ்சாயத்துகள் சட்டத்தின் கீழ், ஒரு தேர்தலை எதிர்த்து தேர்தல் மனுவை தகுதிவாய்ந்த மாவட்ட நீதிபதியிடம் எத்தனை நாட்களுக்குள் சமர்ப்பிக்க வேண்டும்?",
            "options": [
                ("Within 45 days from the date of declaration of the results of the election", "தேர்தல் முடிவுகள் அறிவிக்கப்பட்ட தேதியிலிருந்து 45 நாட்களுக்குள்"),
                ("Within 365 days from the date of the first meeting of the local body", "உள்ளாட்சி அமைப்பின் முதல் கூட்டம் நடைபெற்ற தேதியிலிருந்து 365 நாட்களுக்குள்"),
                ("Within 7 days prior to the date of polling", "வாக்குப்பதிவு தேதிக்கு 7 நாட்களுக்கு முன்னதாக"),
                ("At any time during the entire five-year tenure without any limitation period", "எந்தவொரு கால வரம்பும் இன்றி ஐந்து ஆண்டு பதவிக்காலம் முழுவதும் எந்த நேரத்திலும்")
            ],
            "correct_key": "A",
            "exp_en": "Under Section 258 of the Tamil Nadu Panchayats Act 1994, an election petition calling in question any election must be presented within 45 days from the date of declaration of the results of the election to the Principal District Judge.",
            "exp_ta": "1994 தமிழ்நாடு பஞ்சாயத்துகள் சட்டத்தின் பிரிவு 258-ன் கீழ், எந்தவொரு தேர்தலையும் கேள்விக்குள்ளாக்கும் தேர்தல் மனு, தேர்தல் முடிவுகள் அறிவிக்கப்பட்ட தேதியிலிருந்து 45 நாட்களுக்குள் முதன்மை மாவட்ட நீதிபதியிடம் சமர்ப்பிக்கப்பட வேண்டும்.",
            "why_a_en": "Correct. 45 days is the statutory limitation period under Section 258.",
            "why_a_ta": "சரி. பிரிவு 258-ன் கீழ் 45 நாட்கள் என்பது சட்டப்பூர்வ கால வரம்பாகும்.",
            "why_b_en": "Incorrect. 365 days is excessively long and not prescribed.",
            "why_b_ta": "தவறு. 365 நாட்கள் என்பது சட்டத்தில் பரிந்துரைக்கப்படாத மிக நீண்ட காலமாகும்.",
            "why_c_en": "Incorrect. Pre-polling petitions are barred under Article 243-O.",
            "why_c_ta": "தவறு. வாக்குப்பதிவுக்கு முந்தைய மனுக்கள் சரத்து 243-O-ன் கீழ் தடைசெய்யப்பட்டுள்ளன.",
            "why_d_en": "Incorrect. Election petitions are strictly governed by statutory limitation periods.",
            "why_d_ta": "தவறு. தேர்தல் மனுக்கள் சட்டப்பூர்வ கால வரம்புகளால் கண்டிப்பாக நிர்வகிக்கப்படுகின்றன.",
            "tip_en": "Election Petition limitation: 45 days from declaration of results (matches RPA 1951 Sec 81 as well).",
            "tip_ta": "தேர்தல் மனு கால வரம்பு: முடிவுகள் அறிவிக்கப்பட்டதிலிருந்து 45 நாட்கள் (RPA 1951 பிரிவு 81-ஐயும் ஒத்துப்போகிறது).",
            "fact_en": "Failure to file within 45 days cannot be condoned under Section 5 of the Limitation Act for election petitions.",
            "fact_ta": "தேர்தல் மனுக்களுக்கு கால வரம்புச் சட்டத்தின் பிரிவு 5-ன் கீழ் 45 நாட்களுக்குள் தாக்கல் செய்யத் தவறியதை மன்னிக்க முடியாது."
        },

        # 16. K. Venkatachalam v. A. Swamickan (1999) - Ineligibility vs Bar
        {
            "subtopic": "State Election Commission - Constitutional Mandate & Provisions (Articles 243K & 243ZA)",
            "stem_en": "In K. Venkatachalam v. A. Swamickan (1999), what exception did the Supreme Court recognize to the constitutional bar on court interference in elections?",
            "stem_ta": "கே. வெங்கடாசலம் எதிர் ஏ. சுவாமிக்கண் (1999) வழக்கில், தேர்தலில் நீதிமன்ற தலையீட்டிற்கான அரசியலமைப்புத் தடைக்கு உச்ச நீதிமன்றம் என்ன விதிவிலக்கை அங்கீகரித்தது?",
            "options": [
                ("Article 226 can be invoked to declare an elected person disqualified if they impersonated another voter and lacked basic constitutional eligibility, where no election petition was filed in time", "தேர்தல் மனு சரியான நேரத்தில் தாக்கல் செய்யப்படாத போது, ஒரு நபர் ஆள்மாறாட்டம் செய்து அடிப்படை தகுதி கொண்டிருக்கவில்லை எனில், அவரை தகுதியற்றவர் என அறிவிக்க சரத்து 226-ஐப் பயன்படுத்தலாம்"),
                ("High Courts can nullify any election merely on oral complaints without sworn affidavits", "உயர் நீதிமன்றங்கள் எந்தவொரு தேர்தலையும் உறுதிமொழி ஆவணங்கள் இன்றி வெறும் வாய்மொழி புகாரின் பேரில் ரத்து செய்யலாம்"),
                ("The constitutional bar under Article 329(b) and 243-O is absolute and shields even convicted felons who forge identity documents", "சரத்து 329(b) மற்றும் 243-O-ன் கீழான தடை முழுமையானது மற்றும் போலி ஆவணங்களை உருவாக்கிய குற்றவாளிகளையும் பாதுகாக்கிறது"),
                ("Election petitions can only be heard by the Prime Minister's Office", "தேர்தல் மனுக்களை பிரதமரின் அலுவலகம் மட்டுமே விசாரிக்க முடியும்")
            ],
            "correct_key": "A",
            "exp_en": "In K. Venkatachalam (1999), the SC ruled that where a candidate fraudulently impersonated another on the electoral roll to contest, the High Court under Article 226 can declare him not qualified to sit in the Assembly/local body, as Article 226 is designed to prevent fraud on the Constitution.",
            "exp_ta": "கே. வெங்கடாசலம் (1999) வழக்கில், ஒரு வேட்பாளர் வாக்காளர் பட்டியலில் மற்றொரு நபரைப் போல ஆள்மாறாட்டம் செய்து போட்டியிட்டால், சரத்து 226-ன் கீழ் அவர் பதவியில் அமர தகுதியற்றவர் என்று உயர் நீதிமன்றம் அறிவிக்க முடியும் என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
            "why_a_en": "Correct. Constitutional fraud and blatant impersonation allows writ intervention under Art 226.",
            "why_a_ta": "சரி. அரசியலமைப்பு மோசடி மற்றும் ஆள்மாறாட்டம் சரத்து 226-ன் கீழ் நீதிப்பேராணை தலையீட்டை அனுமதிக்கிறது.",
            "why_b_en": "Incorrect. Strict judicial evidence and verification are mandatory.",
            "why_b_ta": "தவறு. கடுமையான நீதித்துறை ஆதாரங்கள் மற்றும் சரிபார்ப்பு கட்டாயமாகும்.",
            "why_c_en": "Incorrect. Fraud vitiates all solemn acts; constitutional bars do not shield fraudulent usurpers.",
            "why_c_ta": "தவறு. மோசடி அனைத்தையும் செல்லாததாக்கும்; அரசியலமைப்புத் தடைகள் ஆக்கிரமிப்பாளர்களைப் பாதுகாக்காது.",
            "why_d_en": "Incorrect. PMO has no judicial authority in election disputes.",
            "why_d_ta": "தவறு. தேர்தல் சர்ச்சைகளில் PMO-விற்கு நீதித்துறை அதிகாரம் இல்லை.",
            "tip_en": "Venkatachalam principle: Art 226 writ of quo warranto overcomes the bar if candidate committed fraud on the electoral roll.",
            "tip_ta": "வெங்கடாசலம் கொள்கை: வேட்பாளர் வாக்காளர் பட்டியலில் மோசடி செய்திருந்தால் சரத்து 226 தகுதி வினவு மனு தடையை முறியடிக்கும்.",
            "fact_en": "This landmark judgment from Tamil Nadu remains a foundational precedent cited in municipal and panchayat disqualification cases.",
            "fact_ta": "தமிழ்நாட்டைச் சேர்ந்த இந்த முக்கியத் தீர்ப்பு நகராட்சி மற்றும் பஞ்சாயத்து தகுதியிழப்பு வழக்குகளில் மேற்கோள் காட்டப்படும் ஒரு அடிப்படை முன்மாதிரியாக உள்ளது."
        },

        # 17. Multi-Member Wards in Local Bodies
        {
            "subtopic": "State Election Commission - Constitutional Mandate & Provisions (Articles 243K & 243ZA)",
            "stem_en": "What is meant by a 'multi-member ward system' in local body elections, and how does the State Election Commission administer voting in such wards?",
            "stem_ta": "உள்ளாட்சித் தேர்தல்களில் 'பன்முக உறுப்பினர் வார்டு முறை' என்றால் என்ன, அத்தகைய வார்டுகளில் மாநில தேர்தல் ஆணையம் வாக்குப்பதிவை எவ்வாறு நிர்வகிக்கிறது?",
            "options": [
                ("A single territorial ward elects two or more representatives, where each voter casts as many votes as there are seats to be filled", "ஒரு குறிப்பிட்ட பகுதி வார்டு இரண்டு அல்லது அதற்கு மேற்பட்ட பிரதிநிதிகளைத் தேர்ந்தெடுக்கிறது, அங்கு ஒவ்வொரு வாக்காளரும் நிரப்பப்பட வேண்டிய இடங்களின் எண்ணிக்கைக்கு ஏற்ப வாக்குகளை அளிக்கிறார்கள்"),
                ("Each voter is assigned two different political parties and must vote for both simultaneously", "ஒவ்வொரு வாக்காளருக்கும் இரண்டு வெவ்வேறு அரசியல் கட்சிகள் ஒதுக்கப்பட்டு இரண்டிற்கும் ஒரே நேரத்தில் வாக்களிக்க வேண்டும்"),
                ("Wards are rotated among five different taluks every alternate election month", "ஒவ்வொரு மாற்று தேர்தல் மாதத்திலும் ஐந்து வெவ்வேறு தாலுகாக்களுக்கு இடையே வார்டுகள் சுழற்றப்படுகின்றன"),
                ("Only joint family heads are permitted to cast votes on behalf of all ward residents", "வார்டு குடியிருப்பாளர்கள் அனைவரின் சார்பாகவும் கூட்டுக் குடும்பத் தலைவர்கள் மட்டுமே வாக்களிக்க அனுமதிக்கப்படுகிறார்கள்")
            ],
            "correct_key": "A",
            "exp_en": "In a multi-member ward system (historically used in various municipalities or local bodies), two or more councillors represent one ward (often one general and one reserved seat). Each elector has as many votes as seats, administered by SEC using multi-ballot or cumulative/distributive voting.",
            "exp_ta": "பன்முக உறுப்பினர் வார்டு முறையில், இரண்டு அல்லது அதற்கு மேற்பட்ட கவுன்சிலர்கள் ஒரு வார்டைப் பிரதிநிதித்துவப்படுத்துகிறார்கள் (பொதுவாக ஒன்று பொது மற்றும் ஒன்று ஒதுக்கப்பட்ட இடம்). ஒவ்வொரு வாக்காளருக்கும் இடங்களின் எண்ணிக்கைக்கு ஏற்ப வாக்குகள் இருக்கும், இது SEC-ஆல் நிர்வகிக்கப்படுகிறது.",
            "why_a_en": "Correct. Multi-member wards elect multiple members with each elector possessing multiple votes.",
            "why_a_ta": "சரி. பன்முக உறுப்பினர் வார்டுகள் பல உறுப்பினர்களைத் தேர்ந்தெடுக்கின்றன, இதில் ஒவ்வொரு வாக்காளருக்கும் பல வாக்குகள் இருக்கும்.",
            "why_b_en": "Incorrect. Voters vote for individual candidates, not forced dual party assignments.",
            "why_b_ta": "தவறு. வாக்காளர்கள் தனிப்பட்ட வேட்பாளர்களுக்கு வாக்களிக்கிறார்கள், இரட்டைக் கட்சி ஒதுக்கீட்டிற்கு அல்ல.",
            "why_c_en": "Incorrect. Ward rotation happens per census delimitation, not monthly taluk rotation.",
            "why_c_ta": "தவறு. வார்டு சுழற்சி மக்கள் தொகை கணக்கெடுப்பின்படி நடக்கிறது, மாதாந்திர தாலுகா சுழற்சி அல்ல.",
            "why_d_en": "Incorrect. Adult suffrage grants one vote per seat to every adult citizen.",
            "why_d_ta": "தவறு. வயதுவந்தோர் வாக்குரிமை ஒவ்வொரு வயதுவந்த குடிமகனுக்கும் வாக்களிக்கும் உரிமையை வழங்குகிறது.",
            "tip_en": "Single-member ward = 1 winner. Multi-member ward = 2 or more winners from the same territorial ward.",
            "tip_ta": "ஒற்றை உறுப்பினர் வார்டு = 1 வெற்றியாளர். பன்முக உறுப்பினர் வார்டு = ஒரே பகுதியிலிருந்து 2 அல்லது அதற்கு மேற்பட்ட வெற்றியாளர்கள்.",
            "fact_en": "Most municipal wards in Tamil Nadu currently operate on a single-member ward system.",
            "fact_ta": "தமிழ்நாட்டில் உள்ள பெரும்பாலான நகராட்சி வார்டுகள் தற்போது ஒற்றை உறுப்பினர் வார்டு முறையில் செயல்படுகின்றன."
        },

        # 18. SFC Net Proceeds Definition
        {
            "subtopic": "State Finance Commission - Constitutional Mandate, Composition & Role (Articles 243I & 243Y)",
            "stem_en": "Under Article 243-I(1)(a)(i), what forms the base from which the State Finance Commission recommends distribution between the State and the Panchayats?",
            "stem_ta": "சரத்து 243-I(1)(a)(i)-ன் கீழ், மாநிலத்திற்கும் பஞ்சாயத்துகளுக்கும் இடையிலான பகிர்வுக்கு மாநில நிதி ஆணையம் எந்த அடிப்படையிலிருந்து பரிந்துரைக்கிறது?",
            "options": [
                ("The net proceeds of the taxes, duties, tolls and fees leviable by the State", "மாநிலத்தால் விதிக்கக்கூடிய வரிகள், தீர்வைகள், சுங்கக் கட்டணங்கள் மற்றும் கட்டணங்களின் நிகர வருமானம்"),
                ("The total gross foreign direct investment received by the State industries department", "மாநில தொழில் துறையால் பெறப்பட்ட மொத்த அந்நிய நேரடி முதலீடு"),
                ("The net profits earned exclusively by public sector oil marketing companies", "பொதுத்துறை எண்ணெய் சந்தைப்படுத்தல் நிறுவனங்களால் மட்டுமே ஈட்டப்பட்ட நிகர லாபம்"),
                ("The total value of mineral assets confiscated by the police department", "காவல்துறையால் பறிமுதல் செய்யப்பட்ட கனிம சொத்துக்களின் மொத்த மதிப்பு")
            ],
            "correct_key": "A",
            "exp_en": "Article 243-I(1)(a)(i) stipulates the distribution between the State and the Panchayats of the net proceeds of the taxes, duties, tolls and fees leviable by the State, which may be divided between them or allocated to their respective levels.",
            "exp_ta": "சரத்து 243-I(1)(a)(i) மாநிலத்தால் விதிக்கக்கூடிய வரிகள், தீர்வைகள், சுங்கக் கட்டணங்கள் மற்றும் கட்டணங்களின் நிகர வருவாயை மாநிலத்திற்கும் பஞ்சாயத்துகளுக்கும் இடையே பகிர்ந்தளிப்பதை அல்லது அந்தந்த நிலைகளுக்கு ஒதுக்குவதை நிர்ணயிக்கிறது.",
            "why_a_en": "Correct. Verbatim constitutional phrasing of Article 243-I(1)(a)(i).",
            "why_a_ta": "சரி. சரத்து 243-I(1)(a)(i)-ன் சரியான அரசியலமைப்பு வாசகம்.",
            "why_b_en": "Incorrect. FDI is private capital investment, not state tax proceeds.",
            "why_b_ta": "தவறு. FDI என்பது தனியார் மூலதன முதலீடு, மாநில வரி வருவாய் அல்ல.",
            "why_c_en": "Incorrect. Central PSU profits do not form part of state tax divisible pool.",
            "why_c_ta": "தவறு. மத்திய பொதுத்துறை நிறுவனங்களின் லாபம் மாநில வரிப் பகிர்வுத் தொகுப்பில் சேராது.",
            "why_d_en": "Incorrect. Confiscated assets are not regular tax revenues.",
            "why_d_ta": "தவறு. பறிமுதல் செய்யப்பட்ட சொத்துக்கள் வழக்கமான வரி வருவாய்கள் அல்ல.",
            "tip_en": "Base for SFC devolution = Net proceeds of State's own taxes, duties, tolls, and fees.",
            "tip_ta": "SFC பகிர்வுக்கான அடிப்படை = மாநிலத்தின் சொந்த வரிகள், தீர்வைகள், சுங்கக் கட்டணங்கள் மற்றும் கட்டணங்களின் நிகர வருமானம்.",
            "fact_en": "Cost of collection is deducted from gross tax revenue to arrive at net proceeds.",
            "fact_ta": "நிகர வருவாயைக் கணக்கிட மொத்த வரி வருவாயிலிருந்து வசூல் செலவு கழிக்கப்படுகிறது."
        },

        # 19. Local Authorities Anti-Defection Act in Tamil Nadu (1999)
        {
            "subtopic": "Tamil Nadu State Election & Finance Commissions - Legal Framework, Rules & Precedents",
            "stem_en": "What does the Tamil Nadu Local Authorities (Prevention of Disqualification) Act / Local Authorities Anti-Defection provisions prescribe regarding elected members of local bodies?",
            "stem_ta": "தமிழ்நாடு உள்ளாட்சி அதிகார அமைப்புகள் (தகுதியிழப்புத் தடுப்புச் சட்டம்) / கட்சித் தாவல் தடை விதிகள் உள்ளாட்சி அமைப்புகளின் தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்கள் குறித்து என்ன பரிந்துரைக்கின்றன?",
            "options": [
                ("A councillor elected on a political party ticket who voluntarily gives up party membership or votes contrary to the party whip can be disqualified", "அரசியல் கட்சி சின்னத்தில் தேர்ந்தெடுக்கப்பட்ட கவுன்சிலர் தானாக முன்வந்து கட்சி உறுப்பினர் பதவியை கைவிட்டாலோ அல்லது கட்சி கொறடாவுக்கு எதிராக வாக்களித்தாலோ தகுதி நீக்கம் செய்யப்படலாம்"),
                ("Members of local bodies have absolute immunity and can switch parties daily without any legal consequences", "உள்ளாட்சி அமைப்புகளின் உறுப்பினர்களுக்கு முழுமையான பாதுகாப்பு உள்ளது மற்றும் எந்த சட்டப்பூர்வ விளைவுகளும் இன்றி தினமும் கட்சிகளை மாற்றலாம்"),
                ("All local body members must mandatorily resign and join the national ruling party within 30 days of election", "அனைத்து உள்ளாட்சி உறுப்பினர்களும் தேர்தல் முடிந்த 30 நாட்களுக்குள் கட்டாயமாக பதவி விலகி தேசிய ஆளும் கட்சியில் சேர வேண்டும்"),
                ("Anti-defection provisions in Tamil Nadu apply exclusively to independent candidates and not to recognized parties", "தமிழ்நாட்டில் கட்சித் தாவல் தடை விதிகள் சுயேச்சை வேட்பாளர்களுக்கு மட்டுமே பொருந்தும், அங்கீகரிக்கப்பட்ட கட்சிகளுக்குப் பொருந்தாது")
            ],
            "correct_key": "A",
            "exp_en": "Under state local body anti-defection frameworks (such as the TN Local Authorities Disqualification on Ground of Defection Act, 1999), a member elected on a political party symbol who voluntarily gives up membership or defies an official party directive/whip faces disqualification.",
            "exp_ta": "மாநில உள்ளாட்சி கட்சித் தாவல் தடை கட்டமைப்பின் கீழ் (1999 சட்டம்), ஒரு அரசியல் கட்சியின் சின்னத்தில் தேர்ந்தெடுக்கப்பட்டு, தானாக முன்வந்து உறுப்பினர் பதவியை கைவிடும் அல்லது அதிகாரப்பூர்வ கட்சி உத்தரவு/கொறடாவை மீறும் உறுப்பினர் தகுதியிழப்பை எதிர்கொள்கிறார்.",
            "why_a_en": "Correct. Voluntarily giving up membership or voting against party directions attracts defection disqualification.",
            "why_a_ta": "சரி. உறுப்பினர் பதவியை தானாக முன்வந்து கைவிடுவது அல்லது கட்சி உத்தரவுகளுக்கு எதிராக வாக்களிப்பது தகுதியிழப்பை ஏற்படுத்துகிறது.",
            "why_b_en": "Incorrect. Local councillors do not have unrestrained immunity to defect.",
            "why_b_ta": "தவறு. உள்ளாட்சி கவுன்சிலர்களுக்கு கட்சி மாற தடையற்ற உரிமை இல்லை.",
            "why_c_en": "Incorrect. Compulsory defection is completely unconstitutional.",
            "why_c_ta": "தவறு. கட்டாய கட்சித் தாவல் முற்றிலும் அரசியலமைப்பிற்கு முரணானது.",
            "why_d_en": "Incorrect. Defection laws apply specifically to candidates sponsored by political parties.",
            "why_d_ta": "தவறு. கட்சித் தாவல் சட்டங்கள் அரசியல் கட்சிகளால் நிறுத்தப்பட்ட வேட்பாளர்களுக்குப் பொருந்தும்.",
            "tip_en": "Similar to Tenth Schedule for MPs/MLAs, states have enacted statutory anti-defection laws for local bodies.",
            "tip_ta": "எம்.பி./எம்.எல்.ஏ.-க்களுக்கான பத்தாவது அட்டவணையைப் போலவே, மாநிலங்கள் உள்ளாட்சி அமைப்புகளுக்கு சட்டப்பூர்வ கட்சித் தாவல் தடைச் சட்டங்களை இயற்றியுள்ளன.",
            "fact_en": "Village Panchayat Ward Members in TN are elected on a non-party basis, so anti-defection rules do not apply to them.",
            "fact_ta": "TN-ல் கிராம பஞ்சாயத்து வார்டு உறுப்பினர்கள் கட்சி சாரா அடிப்படையில் தேர்ந்தெடுக்கப்படுவதால் அவர்களுக்கு கட்சித் தாவல் விதிகள் பொருந்தாது."
        },

        # 20. B.R. Kapur v. State of Tamil Nadu (2001) - Qualifications at Constitutional Levels
        {
            "subtopic": "State Election Commissioner - Appointment, Tenure, Removal & Autonomy",
            "stem_en": "In B.R. Kapur v. State of Tamil Nadu (2001), what crucial principle regarding eligibility for public office and disqualification was laid down by the Supreme Court?",
            "stem_ta": "பி.ஆர். கபூர் எதிர் தமிழ்நாடு அரசு (2001) வழக்கில், பொதுப் பதவிக்கான தகுதி மற்றும் தகுதியிழப்பு குறித்து உச்ச நீதிமன்றம் வகுத்த முக்கிய கொள்கை என்ன?",
            "options": [
                ("A person convicted of a criminal offence and disqualified under the Representation of the People Act cannot hold constitutional office even if appointed or elected", "மக்கள் பிரதிநிதித்துவச் சட்டத்தின் கீழ் குற்றவியல் குற்றத்திற்காக தண்டிக்கப்பட்டு தகுதி நீக்கம் செய்யப்பட்ட ஒருவர், நியமிக்கப்பட்டாலும் அல்லது தேர்ந்தெடுக்கப்பட்டாலும் அரசியலமைப்புப் பதவியை வகிக்க முடியாது"),
                ("Convicted individuals are granted absolute pardon upon being sworn into any public office", "எந்தவொரு பொதுப் பதவியிலும் பதவியேற்றவுடன் தண்டனை பெற்ற நபர்களுக்கு முழுமையான மன்னிப்பு வழங்கப்படுகிறது"),
                ("Only the Election Commission has the power to pardon criminal sentences of political candidates", "அரசியல் வேட்பாளர்களின் குற்றவியல் தண்டனைகளை மன்னிக்கும் அதிகாரம் தேர்தல் ஆணையத்திற்கு மட்டுமே உள்ளது"),
                ("Conviction under criminal law is irrelevant for holding the office of Chief Minister or local body leadership", "முதலமைச்சர் அல்லது உள்ளாட்சித் தலைமைப் பதவியை வகிப்பதற்கு குற்றவியல் சட்டத்தின் கீழான தண்டனை பொருத்தமற்றது")
            ],
            "correct_key": "A",
            "exp_en": "In B.R. Kapur (2001), the Supreme Court ruled that a person convicted of an offence carrying imprisonment over 2 years and disqualified under Section 8(3) of RPA 1951 cannot hold executive office, establishing that statutory disqualifications are strictly enforceable across all constitutional offices.",
            "exp_ta": "பி.ஆர். கபூர் (2001) வழக்கில், 2 ஆண்டுகளுக்கு மேல் சிறைத் தண்டனை விதிக்கப்பட்டு RPA 1951 பிரிவு 8(3)-ன் கீழ் தகுதி நீக்கம் செய்யப்பட்ட ஒருவர் நிர்வாகப் பதவியை வகிக்க முடியாது என்றும், சட்டப்பூர்வ தகுதியிழப்புகள் அனைத்து அரசியலமைப்புப் பதவிகளிலும் கண்டிப்பாக அமல்படுத்தப்பட வேண்டும் என்றும் உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
            "why_a_en": "Correct. Convicted and disqualified persons cannot hold public constitutional office.",
            "why_a_ta": "சரி. தண்டனை பெற்று தகுதி நீக்கம் செய்யப்பட்ட நபர்கள் பொது அரசியலமைப்புப் பதவியை வகிக்க முடியாது.",
            "why_b_en": "Incorrect. Swearing-in does not confer constitutional immunity from criminal conviction.",
            "why_b_ta": "தவறு. பதவியேற்பு குற்றவியல் தண்டனையிலிருந்து அரசியலமைப்புப் பாதுகாப்பை வழங்காது.",
            "why_c_en": "Incorrect. Pardoning power belongs only to the President (Art 72) and Governor (Art 161).",
            "why_c_ta": "தவறு. மன்னிக்கும் அதிகாரம் குடியரசுத் தலைவர் (சரத்து 72) மற்றும் ஆளுநருக்கு (சரத்து 161) மட்டுமே உள்ளது.",
            "why_d_en": "Incorrect. Criminal conviction is directly disqualifying for any elected or executive office.",
            "why_d_ta": "தவறு. குற்றவியல் தண்டனை தேர்ந்தெடுக்கப்பட்ட அல்லது நிர்வாகப் பதவிக்கு நேரடியாகத் தகுதியிழப்பை ஏற்படுத்துகிறது.",
            "tip_en": "Disqualification under election laws operates automatically upon conviction unless stayed by an appellate court.",
            "tip_ta": "மேல்முறையீட்டு நீதிமன்றத்தால் நிறுத்தி வைக்கப்படாவிட்டால் தேர்தல் சட்டங்களின் கீழான தகுதியிழப்பு தண்டனை பெற்றவுடன் தானாகவே செயல்படும்.",
            "fact_en": "This principle applies symmetrically to Panchayat Presidents and Municipal Chairpersons under Section 37/38 of the TN Panchayats Act 1994.",
            "fact_ta": "இந்தக் கொள்கை 1994 தமிழ்நாடு பஞ்சாயத்துகள் சட்டத்தின் பிரிவு 37/38-ன் கீழ் பஞ்சாயத்து தலைவர்கள் மற்றும் நகராட்சி தலைவர்களுக்கும் சமமாகப் பொருந்தும்."
        },

        # 21. SEC Powers during Law and Order Breakdown
        {
            "subtopic": "State Election Commission - Constitutional Mandate & Provisions (Articles 243K & 243ZA)",
            "stem_en": "In the event of booth capturing, massive violence, or serious irregularities during local body polling, what plenary powers can the State Election Commission exercise?",
            "stem_ta": "உள்ளாட்சித் தேர்தல் வாக்குப்பதிவின் போது வாக்குச்சாவடி கைப்பற்றப்படுதல், பெரும் வன்முறை அல்லது கடுமையான முறைகேடுகள் ஏற்பட்டால், மாநில தேர்தல் ஆணையம் எந்த முழுமையான அதிகாரங்களைப் பயன்படுத்தலாம்?",
            "options": [
                ("Order countermanding of polls, repoll in affected polling stations, or adjourn polling under its plenary constitutional authority", "தனது முழுமையான அரசியலமைப்பு அதிகாரத்தின் கீழ் தேர்தலை ரத்து செய்தல், பாதிக்கப்பட்ட வாக்குச்சாவடிகளில் மறுவாக்குப்பதிவு அல்லது வாக்கெடுப்பை ஒத்திவைத்தல் போன்றவற்றை உத்தரவிடலாம்"),
                ("Impose President's Rule across the entire state under Article 356 without consulting the Union Government", "மத்திய அரசைக் கலந்தாலோசிக்காமல் சரத்து 356-ன் கீழ் முழு மாநிலத்திலும் குடியரசுத் தலைவர் ஆட்சியை விதிக்கலாம்"),
                ("Disband the High Court and take over criminal trial of the rioters directly in the Commission's headquarters", "உயர் நீதிமன்றத்தைக் கலைத்து, கலவரக்காரர்களின் குற்றவியல் விசாரணையை ஆணையத்தின் தலைமையகத்தில் நேரடியாக எடுத்து நடத்தலாம்"),
                ("Direct the Indian Armed Forces to declare martial law under Article 34", "சரத்து 34-ன் கீழ் இராணுவச் சட்டத்தை பிரகடனப்படுத்த இந்திய ஆயுதப் படைகளுக்கு உத்தரவிடலாம்")
            ],
            "correct_key": "A",
            "exp_en": "Under Articles 243K/243ZA and corresponding statutory rules, the State Election Commission possesses plenary powers to adjourn polling, order fresh repolls in affected booths, or countermand elections in the face of widespread violence or booth capturing.",
            "exp_ta": "சரத்துகள் 243K/243ZA மற்றும் தொடர்புடைய சட்ட விதிகளின் கீழ், வன்முறை அல்லது வாக்குச்சாவடி கைப்பற்றல் நடக்கும் போது வாக்கெடுப்பை ஒத்திவைக்க, பாதிக்கப்பட்ட வாக்குச்சாவடிகளில் புதிய மறுவாக்குப்பதிவுக்கு உத்தரவிட அல்லது தேர்தலை ரத்து செய்ய மாநில தேர்தல் ஆணையத்திற்கு முழு அதிகாரம் உண்டு.",
            "why_a_en": "Correct. SEC can adjourn, order repolls, or countermand corrupted elections.",
            "why_a_ta": "சரி. SEC வாக்கெடுப்பை ஒத்திவைக்கலாம், மறுவாக்குப்பதிவுக்கு உத்தரவிடலாம் அல்லது சீர்குலைந்த தேர்தலை ரத்து செய்யலாம்.",
            "why_b_en": "Incorrect. Article 356 proclamation is strictly the President's constitutional prerogative.",
            "why_b_ta": "தவறு. சரத்து 356 பிரகடனம் என்பது முற்றிலும் குடியரசுத் தலைவரின் அரசியலமைப்பு சிறப்புரிமையாகும்.",
            "why_c_en": "Incorrect. SEC has no judicial powers to disband courts or try criminal cases.",
            "why_c_ta": "தவறு. நீதிமன்றங்களைக் கலைக்கவோ அல்லது குற்றவியல் வழக்குகளை விசாரிக்கவோ SEC-க்கு நீதித்துறை அதிகாரம் இல்லை.",
            "why_d_en": "Incorrect. SEC cannot declare martial law or deploy armed forces under Art 34.",
            "why_d_ta": "தவறு. SEC சரத்து 34-ன் கீழ் இராணுவச் சட்டத்தை அறிவிக்கவோ அல்லது ஆயுதப் படைகளை பயன்படுத்தவோ முடியாது.",
            "tip_en": "SEC plenary power under 243K = ECI plenary power under 324 (Ashok Kumar & Kishan Singh Tomar precedents).",
            "tip_ta": "243K-ன் கீழ் SEC முழு அதிகாரம் = 324-ன் கீழ் ECI முழு அதிகாரம் (அசோக் குமார் & கிஷன் சிங் தோமர் தீர்ப்புகள்).",
            "fact_en": "Staff on election duty are deemed to be on deputation to the SEC and subject to its disciplinary control.",
            "fact_ta": "தேர்தல் பணியில் உள்ள ஊழியர்கள் SEC-க்கு அயல்பணியில் இருப்பதாகக் கருதப்பட்டு அதன் ஒழுங்கு நடவடிக்கைக் கட்டுப்பாட்டிற்கு உட்பட்டவர்கள்."
        },

        # 22. Capital Grants vs Operational Deficit Grants by SFC
        {
            "subtopic": "Financial Devolution, Intergovernmental Transfers & Local Governance",
            "stem_en": "Why do State Finance Commissions distinguish between Capital Grants and Maintenance/Operational Grants when devolving funds to local bodies?",
            "stem_ta": "உள்ளாட்சி அமைப்புகளுக்கு நிதியைப் பகிர்ந்தளிக்கும் போது மாநில நிதி ஆணையங்கள் மூலதன மானியங்கள் மற்றும் பராமரிப்பு/செயல்பாட்டு மானியங்களுக்கு இடையே ஏன் வேறுபடுத்துகின்றன?",
            "options": [
                ("To ensure that funds earmarked for durable asset creation (water pipes, roads) are not diverted to recurring administrative consumption like electricity bills or salaries", "நீடித்த சொத்து உருவாக்கத்திற்காக ஒதுக்கப்பட்ட நிதி (குடிநீர்க் குழாய்கள், சாலைகள்) மின் கட்டணம் அல்லது ஊதியம் போன்ற தொடர் நிர்வாகச் செலவுகளுக்கு திருப்பி விடப்படுவதை தடுக்க"),
                ("Because local bodies are legally prohibited from owning any fixed physical infrastructure", "ஏனெனில் உள்ளாட்சி அமைப்புகள் எந்தவொரு நிலையான உள்கட்டமைப்பையும் சொந்தமாக வைத்திருக்க சட்டப்படி தடைசெய்யப்பட்டுள்ளன"),
                ("To ensure that only private multinational contractors can receive funds from the rural treasury", "தனியார் பன்னாட்டு ஒப்பந்ததாரர்கள் மட்டுமே கிராமப்புற கருவூலத்திலிருந்து நிதியைப் பெறுவதை உறுதி செய்ய"),
                ("Because the Constitution requires all capital assets in villages to be owned exclusively by the Governor", "ஏனெனில் கிராமங்களில் உள்ள அனைத்து மூலதனச் சொத்துக்களும் ஆளுநருக்கு மட்டுமே சொந்தமாக இருக்க வேண்டும் என்று அரசியலமைப்பு கோருகிறது")
            ],
            "correct_key": "A",
            "exp_en": "Distinguishing between Capital Grants and Maintenance/Operational Grants ensures financial discipline: capital grants build long-term public infrastructure (roads, drainage, water supply), whereas operational grants maintain them, preventing diversion of asset-creation funds into routine consumption.",
            "exp_ta": "மூலதன மானியங்கள் மற்றும் பராமரிப்பு மானியங்களுக்கு இடையிலான வேறுபாடு நிதி ஒழுக்கத்தை உறுதி செய்கிறது: மூலதன மானியங்கள் நீண்ட கால பொது உள்கட்டமைப்பை (சாலைகள், வடிகால், குடிநீர்) உருவாக்குகின்றன, அதே நேரத்தில் செயல்பாட்டு மானியங்கள் அவற்றை பராமரிக்கின்றன, சொத்து உருவாக்க நிதி வழக்கமான நுகர்வுக்கு மாற்றப்படுவதைத் தடுக்கின்றன.",
            "why_a_en": "Correct. Segregation prevents structural depletion of long-term civic infrastructure assets.",
            "why_a_ta": "சரி. இந்த பிரிப்பு நீண்ட கால குடிமை உள்கட்டமைப்பு சொத்துக்கள் குறைவதைத் தடுக்கிறது.",
            "why_b_en": "Incorrect. Local bodies legally own and maintain their civic infrastructure.",
            "why_b_ta": "தவறு. உள்ளாட்சி அமைப்புகள் தங்கள் குடிமை உள்கட்டமைப்பை சட்டப்பூர்வமாக சொந்தமாக வைத்து பராமரிக்கின்றன.",
            "why_c_en": "Incorrect. Local contracts are awarded per state transparency laws, not restricted to MNCs.",
            "why_c_ta": "தவறு. உள்ளூர் ஒப்பந்தங்கள் மாநில வெளிப்படைத்தன்மை சட்டங்களின்படி வழங்கப்படுகின்றன, MNC-களுக்கு மட்டும் அல்ல.",
            "why_d_en": "Incorrect. Panchayats and Municipalities hold institutional title to public property, not the Governor personally.",
            "why_d_ta": "தவறு. பஞ்சாயத்துகள் மற்றும் நகராட்சிகள் பொதுச் சொத்துக்களின் நிறுவன உரிமையைத் தக்கவைத்துக் கொள்கின்றன, ஆளுநர் அல்ல.",
            "tip_en": "Capital Grants = Asset creation. Maintenance Grants = Asset preservation and daily operational utility.",
            "tip_ta": "மூலதன மானியங்கள் = சொத்து உருவாக்கம். பராமரிப்பு மானியங்கள் = சொத்துப் பாதுகாப்பு மற்றும் தினசரி செயல்பாட்டு பயன்பாடு.",
            "fact_en": "The Sixth SFC in Tamil Nadu stressed setting aside dedicated Pooled Funds for water supply and street light tariff payments.",
            "fact_ta": "தமிழ்நாட்டின் ஆறாவது SFC குடிநீர் விநியோகம் மற்றும் தெருவிளக்கு கட்டணங்களை செலுத்துவதற்கு பிரத்யேக தொகுப்பு நிதியை ஒதுக்க வலியுறுத்தியது."
        },

        # 23. Special Reference No. 1 of 2002 - Timely Elections Principle
        {
            "subtopic": "State Election Commission - Constitutional Mandate & Provisions (Articles 243K & 243ZA)",
            "stem_en": "What constitutional doctrine regarding the completion of democratic elections before tenure expiration, established in Special Reference No. 1 of 2002, applies to local bodies under Article 243-E and 243-U?",
            "stem_ta": "2002-ன் சிறப்பு குறிப்பு எண் 1-ல் நிறுவப்பட்ட, பதவிக்காலம் முடிவதற்குள் ஜனநாயகத் தேர்தல்களை நடத்தி முடிக்க வேண்டும் என்ற எந்த அரசியலமைப்பு கோட்பாடு, சரத்துகள் 243-E மற்றும் 243-U-ன் கீழ் உள்ளாட்சி அமைப்புகளுக்குப் பொருந்தும்?",
            "options": [
                ("The five-year term is constitutionally rigid and immutable; holding elections prior to expiration is an absolute mandate that cannot be postponed on arbitrary administrative grounds", "ஐந்து ஆண்டு பதவிக்காலம் அரசியலமைப்பு ரீதியாக நிலையானது; பதவிக்காலம் முடிவதற்குள் தேர்தல்களை நடத்துவது தன்னிச்சையான நிர்வாகக் காரணங்களுக்காக ஒத்திவைக்க முடியாத ஒரு முழுமையான கட்டளையாகும்"),
                ("State Governments can unilaterally extend the tenure of elected councils indefinitely by issuing executive orders", "நிர்வாக உத்தரவுகளைப் பிறப்பிப்பதன் மூலம் தேர்ந்தெடுக்கப்பட்ட மன்றங்களின் பதவிக்காலத்தை மாநில அரசுகள் காலவரையின்றி நீட்டிக்க முடியும்"),
                ("Elections can only be conducted if all political parties unanimously submit written consent letters", "அனைத்து அரசியல் கட்சிகளும் ஒருமனதாக எழுத்துப்பூர்வ ஒப்புதல் கடிதங்களை சமர்ப்பித்தால் மட்டுமே தேர்தலை நடத்த முடியும்"),
                ("Article 243-E is merely directory and states can remain without elected local councils for decades", "சரத்து 243-E என்பது வெறும் வழிகாட்டுதல் மட்டுமே மற்றும் மாநிலங்கள் பல தசாப்தங்களாக தேர்ந்தெடுக்கப்பட்ட மன்றங்கள் இல்லாமல் இருக்கலாம்")
            ],
            "correct_key": "A",
            "exp_en": "In Special Reference No. 1 of 2002 and Kishan Singh Tomar (2006), the Supreme Court affirmed that the mandate to hold elections before the expiry of the 5-year term under Articles 243-E and 243-U is absolute and mandatory. Delay is permissible only in genuine calamities (war, super-cyclone, pandemic) and must be remedied immediately.",
            "exp_ta": "2002-ன் சிறப்பு குறிப்பு எண் 1 மற்றும் கிஷன் சிங் தோமர் (2006) வழக்குகளில், சரத்துகள் 243-E மற்றும் 243-U-ன் கீழ் 5 ஆண்டு பதவிக்காலம் முடிவதற்குள் தேர்தல்களை நடத்துவது கட்டாயமானது என்று உச்ச நீதிமன்றம் உறுதிப்படுத்தியது. உண்மையான இயற்கை பேரழிவுகளில் மட்டுமே தாமதம் அனுமதிக்கப்படும், அதுவும் உடனடியாக சரிசெய்யப்பட வேண்டும்.",
            "why_a_en": "Correct. 5-year constitutional term is mandatory; elections must precede expiration.",
            "why_a_ta": "சரி. 5 ஆண்டு அரசியலமைப்பு பதவிக்காலம் கட்டாயமானது; காலாவதியாகும் முன்பே தேர்தல்கள் நடத்தப்பட வேண்டும்.",
            "why_b_en": "Incorrect. Executive orders cannot override mandatory constitutional limits on tenure.",
            "why_b_ta": "தவறு. நிர்வாக உத்தரவுகள் பதவிக்காலம் குறித்த கட்டாய அரசியலமைப்பு வரம்புகளை மீற முடியாது.",
            "why_c_en": "Incorrect. Unanimous consent of political parties is never a prerequisite for elections.",
            "why_c_ta": "தவறு. தேர்தலுக்கு அரசியல் கட்சிகளின் ஒருமனதான ஒப்புதல் ஒருபோதும் நிபந்தனை அல்ல.",
            "why_d_en": "Incorrect. Article 243-E is mandatory, not directory.",
            "why_d_ta": "தவறு. சரத்து 243-E கட்டாயமானது, வெறும் வழிகாட்டுதல் அல்ல.",
            "tip_en": "Mandate of 243-E(3) & 243-U(3): Election MUST be completed before the expiry of its duration.",
            "tip_ta": "243-E(3) & 243-U(3)-ன் கட்டளை: பதவிக்காலம் முடிவதற்குள் தேர்தல் கட்டாயம் முடிக்கப்பட வேண்டும்.",
            "fact_en": "Appointment of Special Officers/Administrators after expiry is intended only as a brief stopgap, not an indefinite substitute.",
            "fact_ta": "பதவிக்காலம் முடிந்த பிறகு சிறப்பு அதிகாரிகள் நியமிக்கப்படுவது தற்காலிக ஏற்பாடே தவிர, காலவரையற்ற மாற்றாக இருக்க முடியாது."
        },

        # 24. SFC Formula Criteria - Horizontal Distribution Factors
        {
            "subtopic": "Financial Devolution, Intergovernmental Transfers & Local Governance",
            "stem_en": "Which of the following sets of criteria is typically given the highest combined weightage by State Finance Commissions in formula-based horizontal devolution among local bodies?",
            "stem_ta": "உள்ளாட்சி அமைப்புகளுக்கு இடையிலான சூத்திர அடிப்படையிலான கிடைமட்டப் பகிர்வில் மாநில நிதி ஆணையங்களால் பொதுவாக எந்த அளவுகோல்களுக்கு அதிக ஒருங்கிணைந்த முக்கியத்துவம் வழங்கப்படுகிறது?",
            "options": [
                ("Population and Geographical Area / Distance from highest per-capita income", "மக்கள் தொகை மற்றும் புவியியல் பரப்பளவு / அதிக தனிநபர் வருமானத்திலிருந்து உள்ள தூரம்"),
                ("Number of political rallies organized and party headquarters registered", "நடத்தப்பட்ட அரசியல் பேரணிகளின் எண்ணிக்கை மற்றும் பதிவு செய்யப்பட்ட கட்சித் தலைமையகங்கள்"),
                ("Total volume of gold jewelry pledged in private commercial pawn shops", "தனியார் வணிக அடகு கடைகளில் அடமானம் வைக்கப்பட்ட தங்க நகைகளின் மொத்த அளவு"),
                ("Number of luxury private cars registered in the district", "மாவட்டத்தில் பதிவு செய்யப்பட்ட சொகுசு தனியார் கார்களின் எண்ணிக்கை")
            ],
            "correct_key": "A",
            "exp_en": "Like Central Finance Commissions, State Finance Commissions rely primarily on Population (often 50%-60% weightage), Area (10%-15%), and equity/need criteria (such as SC/ST population, distance from state average income, or infrastructure deficiency) for fair horizontal distribution.",
            "exp_ta": "மத்திய நிதி ஆணையங்களைப் போலவே, மாநில நிதி ஆணையங்களும் நியாயமான கிடைமட்டப் பகிர்வுக்காக முக்கியமாக மக்கள் தொகை (பொதுவாக 50%-60%), பரப்பளவு (10%-15%) மற்றும் சமத்துவம்/தேவை அளவுகோல்களை (SC/ST மக்கள் தொகை, மாநில சராசரி வருமானத்திலிருந்து உள்ள தூரம் போன்றவை) நம்பியுள்ளன.",
            "why_a_en": "Correct. Population, Area, and Equity indicators dominate horizontal devolution formulas.",
            "why_a_ta": "சரி. மக்கள் தொகை, பரப்பளவு மற்றும் சமத்துவக் குறியீடுகள் கிடைமட்டப் பகிர்வு சூத்திரங்களில் ஆதிக்கம் செலுத்துகின்றன.",
            "why_b_en": "Incorrect. Political activities have no place in fiscal transfer formulas.",
            "why_b_ta": "தவறு. நிதிப் பகிர்வு சூத்திரங்களில் அரசியல் நடவடிக்கைகளுக்கு இடமில்லை.",
            "why_c_en": "Incorrect. Pawn shop pledges are not a recognized macroeconomic indicator.",
            "why_c_ta": "தவறு. அடகுக் கடை விவரங்கள் அங்கீகரிக்கப்பட்ட பேரியல் பொருளாதாரக் குறியீடு அல்ல.",
            "why_d_en": "Incorrect. Luxury car registrations do not determine local body devolution.",
            "why_d_ta": "தவறு. சொகுசு கார் பதிவுகள் உள்ளாட்சிப் பகிர்வைத் தீர்மானிப்பதில்லை.",
            "tip_en": "Horizontal devolution = Population (Need) + Area (Cost disability) + Per Capita Income Distance (Equity).",
            "tip_ta": "கிடைமட்டப் பகிர்வு = மக்கள் தொகை (தேவை) + பரப்பளவு (செலவு இயலாமை) + தனிநபர் வருமான தூரம் (சமத்துவம்).",
            "fact_en": "Tamil Nadu SFCs utilize the 2011 Census population data for calculating per capita devolution shares.",
            "fact_ta": "தமிழ்நாடு SFC-கள் தனிநபர் பகிர்வுப் பங்கைக் கணக்கிட 2011 மக்கள் தொகை கணக்கெடுப்புத் தரவைப் பயன்படுத்துகின்றன."
        },

        # 25. Delimitation Commission Act vs SEC Powers
        {
            "subtopic": "State Election Commission - Constitutional Mandate & Provisions (Articles 243K & 243ZA)",
            "stem_en": "What is the key institutional distinction between parliamentary/assembly constituency delimitation and local body ward delimitation?",
            "stem_ta": "நாடாளுமன்ற/சட்டமன்ற தொகுதி மறுவரையறைக்கும் உள்ளாட்சி வார்டு மறுவரையறைக்கும் இடையே உள்ள முக்கிய நிறுவன வேறுபாடு என்ன?",
            "options": [
                ("Parliamentary/assembly delimitation is conducted by an independent Delimitation Commission established by Parliament, whereas local body ward delimitation is administered under State statutory frameworks supervised by the SEC or State Delimitation Authority", "நாடாளுமன்ற/சட்டமன்ற மறுவரையறை நாடாளுமன்றத்தால் நிறுவப்பட்ட ஒரு சுயாதீன மறுவரையறை ஆணையத்தால் நடத்தப்படுகிறது, அதேசமயம் உள்ளாட்சி வார்டு மறுவரையறை SEC அல்லது மாநில மறுவரையறை ஆணையத்தால் மேற்பார்வையிடப்படும் மாநில சட்டக் கட்டமைப்பின் கீழ் நிர்வகிக்கப்படுகிறது"),
                ("Parliamentary delimitation is managed by the Village Panchayat President, while local wards are delimited by the United Nations", "நாடாளுமன்ற மறுவரையறை கிராம பஞ்சாயத்து தலைவரால் நிர்வகிக்கப்படுகிறது, உள்ளூர் வார்டுகள் ஐக்கிய நாடுகள் சபையால் மறுவரையறை செய்யப்படுகின்றன"),
                ("There is no delimitation for local body wards as ward boundaries have remained legally immutable since 1882", "உள்ளாட்சி வார்டுகளுக்கு எந்த மறுவரையறையும் இல்லை, ஏனெனில் வார்டு எல்லைகள் 1882 முதல் சட்டப்படி மாற்ற முடியாததாகவே உள்ளன"),
                ("Local body wards can only be delimited by an act of the Union Security Council", "உள்ளாட்சி வார்டுகளை மத்திய பாதுகாப்புக் குழுவின் சட்டத்தால் மட்டுமே மறுவரையறை செய்ய முடியும்")
            ],
            "correct_key": "A",
            "exp_en": "Parliamentary and Assembly constituencies are delimited by the Central Delimitation Commission under Article 82/170 and the Delimitation Act. In contrast, local body ward delimitation is enacted under State laws (such as the Tamil Nadu Delimitation Commission Act, 2017) and executed by the State Delimitation Commission in coordination with the SEC.",
            "exp_ta": "நாடாளுமன்ற மற்றும் சட்டமன்றத் தொகுதிகள் மத்திய மறுவரையறை ஆணையத்தால் சரத்து 82/170 மற்றும் மறுவரையறைச் சட்டத்தின் கீழ் மறுவரையறை செய்யப்படுகின்றன. இதற்கு மாறாக, உள்ளாட்சி வார்டு மறுவரையறை மாநில சட்டங்களின் கீழ் (தமிழ்நாடு மறுவரையறை ஆணையச் சட்டம் 2017 போன்றவை) இயற்றப்பட்டு, SEC உடன் ஒருங்கிணைந்து மாநில மறுவரையறை ஆணையத்தால் செயல்படுத்தப்படுகிறது.",
            "why_a_en": "Correct. Central Delimitation Commission handles MP/MLA seats; State authorities/SEC handle local wards.",
            "why_a_ta": "சரி. மத்திய மறுவரையறை ஆணையம் எம்.பி./எம்.எல்.ஏ. இடங்களைக் கையாள்கிறது; மாநில அதிகாரிகள்/SEC உள்ளூர் வார்டுகளைக் கையாளுகின்றனர்.",
            "why_b_en": "Incorrect. Panchayat presidents and the UN have no such authority.",
            "why_b_ta": "தவறு. பஞ்சாயத்து தலைவர்களுக்கோ அல்லது ஐ.நா.-விற்கோ அத்தகைய அதிகாரம் இல்லை.",
            "why_c_en": "Incorrect. Local wards are periodically reconstituted following decennial censuses.",
            "why_c_ta": "தவறு. பத்தாண்டு மக்கள் தொகை கணக்கெடுப்பைத் தொடர்ந்து உள்ளூர் வார்டுகள் அவ்வப்போது மறுசீரமைக்கப்படுகின்றன.",
            "why_d_en": "Incorrect. UN Security Council has no role in domestic administrative boundaries.",
            "why_d_ta": "தவறு. உள்நாட்டு நிர்வாக எல்லைகளில் ஐ.நா. பாதுகாப்புக் குழுவிற்கு எந்த பங்கும் இல்லை.",
            "tip_en": "TN Delimitation Commission Act 2017 established a dedicated State Delimitation Commission headed by the SEC as Chairman.",
            "tip_ta": "தமிழ்நாடு மறுவரையறை ஆணையச் சட்டம் 2017 SEC-ஐ தலைவராகக் கொண்ட ஒரு பிரத்யேக மாநில மறுவரையறை ஆணையத்தை நிறுவியது.",
            "fact_en": "In Tamil Nadu, the State Election Commissioner serves ex-officio as the Chairman of the Tamil Nadu Delimitation Commission.",
            "fact_ta": "தமிழ்நாட்டில், மாநில தேர்தல் ஆணையர் தமிழ்நாடு மறுவரையறை ஆணையத்தின் பதவி வழித் தலைவராக பணியாற்றுகிறார்."
        },

        # 26. SEC Expenditure Limit Enforcement
        {
            "subtopic": "State Election Commissioner - Appointment, Tenure, Removal & Autonomy",
            "stem_en": "What legal consequence follows if an elected candidate in a local body election fails to lodge their account of election expenses within the prescribed time under State Election Commission rules?",
            "stem_ta": "மாநில தேர்தல் ஆணைய விதிகளின் கீழ் குறிப்பிட்ட காலத்திற்குள் உள்ளாட்சித் தேர்தலில் தேர்ந்தெடுக்கப்பட்ட வேட்பாளர் தனது தேர்தல் செலவுக் கணக்கை தாக்கல் செய்யத் தவறினால் என்ன சட்டரீதியான விளைவு ஏற்படும்?",
            "options": [
                ("The SEC can issue notice and disqualify the candidate from contesting or voting for a specified statutory period (e.g., three years)", "SEC நோட்டீஸ் வழங்கி, குறிப்பிட்ட சட்டப்பூர்வ காலத்திற்கு (எ.கா. மூன்று ஆண்டுகள்) வேட்பாளர் போட்டியிடவோ வாக்களிக்கவோ தகுதி நீக்கம் செய்யலாம்"),
                ("The candidate is automatically sentenced to solitary confinement without trial", "வேட்பாளருக்கு விசாரணையின்றி தானாகவே தனிமைச் சிறைத் தண்டனை விதிக்கப்படும்"),
                ("The candidate's family members are permanently stripped of Indian citizenship", "வேட்பாளரின் குடும்ப உறுப்பினர்களின் இந்திய குடியுரிமை நிரந்தரமாக பறிக்கப்படும்"),
                ("The election expense limit failure is completely ignored as local body elections have zero financial accountability", "உள்ளாட்சித் தேர்தல்களுக்கு எந்த நிதிப் பொறுப்புணர்வும் இல்லாததால் தேர்தல் செலவு வரம்பு தோல்வி முற்றிலும் புறக்கணிக்கப்படுகிறது")
            ],
            "correct_key": "A",
            "exp_en": "State Election Commissions prescribe maximum expenditure ceilings for various local body posts. Failure to submit expenditure returns within the specified time (typically 30 days) without good cause results in a show-cause notice and subsequent disqualification from contesting for a period (e.g. 3 years).",
            "exp_ta": "பல்வேறு உள்ளாட்சிப் பதவிகளுக்கான அதிகபட்ச செலவு வரம்புகளை மாநில தேர்தல் ஆணையங்கள் பரிந்துரைக்கின்றன. குறிப்பிட்ட காலத்திற்குள் (பொதுவாக 30 நாட்கள்) சரியான காரணமின்றி செலவுக் கணக்குகளை சமர்ப்பிக்கத் தவறினால், விளக்கம் கேட்கும் நோட்டீஸ் மற்றும் அதைத் தொடர்ந்து ஒரு குறிப்பிட்ட காலத்திற்கு (எ.கா. 3 ஆண்டுகள்) போட்டியிடுவதிலிருந்து தகுதி நீக்கம் செய்ய வழிவகுக்கும்.",
            "why_a_en": "Correct. Failure to lodge expense accounts leads to statutory disqualification for up to 3 years.",
            "why_a_ta": "சரி. செலவுக் கணக்குகளை தாக்கல் செய்யத் தவறினால் 3 ஆண்டுகள் வரை சட்டப்பூர்வ தகுதியிழப்பு ஏற்படும்.",
            "why_b_en": "Incorrect. Solitary confinement without trial violates Article 21.",
            "why_b_ta": "தவறு. விசாரணையின்றி தனிமைச் சிறைத் தண்டனை விதிப்பது சரத்து 21-ஐ மீறுகிறது.",
            "why_c_en": "Incorrect. Citizenship cannot be stripped over municipal expense account defaults.",
            "why_c_ta": "தவறு. நகராட்சி செலவுக் கணக்கு குறைபாடுகளுக்காக குடியுரிமையைப் பறிக்க முடியாது.",
            "why_d_en": "Incorrect. Expense limits are statutorily audited and strictly monitored by SEC observers.",
            "why_d_ta": "தவறு. செலவு வரம்புகள் சட்டப்பூர்வமாக தணிக்கை செய்யப்பட்டு SEC பார்வையாளர்களால் கண்காணிக்கப்படுகின்றன.",
            "tip_en": "Failure to lodge election expenses within 30 days without justification = Disqualification by SEC.",
            "tip_ta": "காரணமின்றி 30 நாட்களுக்குள் தேர்தல் செலவுகளை தாக்கல் செய்யத் தவறினால் = SEC மூலம் தகுதியிழப்பு.",
            "fact_en": "Expenditure limits are progressively higher for Corporation Mayors and Councillors compared to Village Panchayat posts.",
            "fact_ta": "கிராம பஞ்சாயத்துப் பதவிகளுடன் ஒப்பிடும்போது மாநகராட்சி மேயர்கள் மற்றும் கவுன்சிலர்களுக்கு செலவு வரம்புகள் அதிகமாக உள்ளன."
        },

        # 27. Article 243-I(1) Five-Year Constitution Frequency
        {
            "subtopic": "State Finance Commission - Constitutional Mandate, Composition & Role (Articles 243I & 243Y)",
            "stem_en": "Under Article 243-I(1), how frequently must the Governor of a State constitute a State Finance Commission?",
            "stem_ta": "சரத்து 243-I(1)-ன் கீழ், ஒரு மாநிலத்தின் ஆளுநர் எவ்வளவு அடிக்கடி மாநில நிதி ஆணையத்தை அமைக்க வேண்டும்?",
            "options": [
                ("At the expiration of every fifth year, or at such earlier time as the Governor considers necessary", "ஒவ்வொரு ஐந்தாவது ஆண்டின் முடிவிலும், அல்லது ஆளுநர் அவசியம் என்று கருதும் முன்னரே உள்ள நேரத்திலும்"),
                ("Only once every twenty-five years following a comprehensive constitutional amendment", "ஒரு விரிவான அரசியலமைப்பு திருத்தத்தைத் தொடர்ந்து இருபத்தைந்து ஆண்டுகளுக்கு ஒரு முறை மட்டுமே"),
                ("Exclusively during periods when the State is placed under President's Rule", "மாநிலத்தில் குடியரசுத் தலைவர் ஆட்சி விதிக்கப்படும் காலங்களில் மட்டுமே"),
                ("Every six months concurrently with the biannual RBI monetary policy statement", "ஆர்பிஐயின் அரையாண்டு பணவியல் கொள்கை அறிக்கையுடன் இணைந்து ஒவ்வொரு ஆறு மாதங்களுக்கும்")
            ],
            "correct_key": "A",
            "exp_en": "Article 243-I(1) provides: 'The Governor of a State shall, as soon as may be within one year from the commencement of the Constitution (Seventy-third Amendment) Act, 1992, and thereafter at the expiration of every fifth year, constitute a Finance Commission...'",
            "exp_ta": "சரத்து 243-I(1) கூறுகிறது: '73வது திருத்தச் சட்டம் தொடங்கியதிலிருந்து ஒரு வருடத்திற்குள்ளும், அதன் பிறகு ஒவ்வொரு ஐந்தாவது ஆண்டின் முடிவிலும் ஆளுநர் ஒரு நிதி ஆணையத்தை அமைக்க வேண்டும்...'",
            "why_a_en": "Correct. At the expiration of every 5th year or earlier, exactly mirroring Article 280(1).",
            "why_a_ta": "சரி. ஒவ்வொரு 5வது ஆண்டின் முடிவிலும் அல்லது முன்னதாகவும், சரத்து 280(1)-ஐப் போலவே.",
            "why_b_en": "Incorrect. 25 years is grossly incorrect; the constitutional period is 5 years.",
            "why_b_ta": "தவறு. 25 ஆண்டுகள் என்பது தவறானது; அரசியலமைப்பு காலம் 5 ஆண்டுகள்.",
            "why_c_en": "Incorrect. SFC is a regular standing constitutional process during normal governance.",
            "why_c_ta": "தவறு. SFC என்பது வழக்கமான நிர்வாகத்தின் போது ஒரு நிலையான அரசியலமைப்பு செயல்முறையாகும்.",
            "why_d_en": "Incorrect. SFC is not constituted on a six-month cycle.",
            "why_d_ta": "தவறு. SFC ஆறு மாத சுழற்சியில் அமைக்கப்படுவதில்லை.",
            "tip_en": "SFC interval: 5 years (just like Central Finance Commission under Art 280).",
            "tip_ta": "SFC இடைவெளி: 5 ஆண்டுகள் (சரத்து 280-ன் கீழ் மத்திய நிதி ஆணையத்தைப் போலவே).",
            "fact_en": "The First SFC in Tamil Nadu was constituted in 1994, submitted in 1996, and devolved funds from 1997-98.",
            "fact_ta": "தமிழ்நாட்டில் முதல் SFC 1994-ல் அமைக்கப்பட்டு, 1996-ல் சமர்ப்பிக்கப்பட்டு, 1997-98 முதல் நிதியை பகிர்ந்தளித்தது."
        },

        # 28. Devolution of Own Tax Revenue vs Grants-in-Aid
        {
            "subtopic": "Financial Devolution, Intergovernmental Transfers & Local Governance",
            "stem_en": "In intergovernmental fiscal transfers, how does a percentage share in State's Own Tax Revenue (SOTR) differ fundamentally from discretionary Grants-in-Aid?",
            "stem_ta": "அரசுகளுக்கு இடையிலான நிதிப் பகிர்வில், மாநிலத்தின் சொந்த வரி வருவாயில் (SOTR) சதவீதப் பங்கு என்பது விருப்ப மானியங்களிலிருந்து (Grants-in-Aid) அடிப்படையில் எவ்வாறு வேறுபடுகிறது?",
            "options": [
                ("A percentage share in SOTR provides buoyant, formula-based, and predictable revenue that grows automatically with the state economy, whereas discretionary grants are ad-hoc and conditional", "SOTR-ல் ஒரு சதவீதப் பங்கு என்பது மாநிலப் பொருளாதாரத்துடன் தானாகவே வளரும், சூத்திர அடிப்படையிலான மற்றும் கணிக்கக்கூடிய வருவாயை வழங்குகிறது, அதேசமயம் விருப்ப மானியங்கள் தற்காலிகமானவை மற்றும் நிபந்தனைக்குட்பட்டவை"),
                ("Grants-in-Aid must be repaid by the local body with 18% compound interest within 30 days", "மானியங்களை உள்ளாட்சி அமைப்பு 30 நாட்களுக்குள் 18% கூட்டு வட்டியுடன் திருப்பிச் செலுத்த வேண்டும்"),
                ("SOTR devolution can only be received in the form of physical gold bullion", "SOTR பகிர்வை தங்கக் கட்டிகளின் வடிவில் மட்டுமே பெற முடியும்"),
                ("Discretionary grants are guaranteed by the Constitution while SOTR sharing is illegal under federal law", "விருப்ப மானியங்கள் அரசியலமைப்பால் உத்தரவாதம் அளிக்கப்படுகின்றன, அதே நேரத்தில் SOTR பகிர்வு கூட்டாட்சி சட்டத்தின் கீழ் சட்டவிரோதமானது")
            ],
            "correct_key": "A",
            "exp_en": "Tying local body devolution to a fixed percentage of SOTR creates revenue buoyancy: as the State's commercial tax, excise, and motor vehicle tax collections increase, local body revenues rise automatically. In contrast, ad-hoc discretionary grants depend on annual state budgetary whims.",
            "exp_ta": "SOTR-ன் நிலையான சதவீதத்துடன் உள்ளாட்சிப் பகிர்வை இணைப்பது வருவாய் விரிவாக்கத்தை உருவாக்குகிறது: மாநிலத்தின் வணிக வரி, கலால் மற்றும் மோட்டார் வாகன வரி வசூல் அதிகரிக்கும் போது, உள்ளாட்சி அமைப்புகளின் வருவாய் தானாகவே உயர்கிறது. இதற்கு மாறாக, தற்காலிக விருப்ப மானியங்கள் வருடாந்திர மாநில பட்ஜெட் விருப்பங்களைச் சார்ந்துள்ளன.",
            "why_a_en": "Correct. Tax share offers buoyant, predictable statutory revenue rather than uncertain grants.",
            "why_a_ta": "சரி. வரிப் பங்கு நிச்சயமற்ற மானியங்களை விட நிலையான, கணிக்கக்கூடிய சட்டப்பூர்வ வருவாயை வழங்குகிறது.",
            "why_b_en": "Incorrect. Grants are non-repayable transfers, not loans with compound interest.",
            "why_b_ta": "தவறு. மானியங்கள் திருப்பிச் செலுத்தத் தேவையில்லாத நிதிப் பகிர்வுகள், கூட்டு வட்டிக் கடன்கள் அல்ல.",
            "why_c_en": "Incorrect. Devolution transfers occur via treasury electronic funds transfer (e-Treasury).",
            "why_c_ta": "தவறு. பகிர்வு இடமாற்றங்கள் கருவூல மின்னணு நிதி பரிமாற்றம் மூலம் நடைபெறுகின்றன.",
            "why_d_en": "Incorrect. SOTR sharing is explicitly authorized under Article 243-I(1)(a).",
            "why_d_ta": "தவறு. SOTR பகிர்வு சரத்து 243-I(1)(a)-ன் கீழ் வெளிப்படையாக அங்கீகரிக்கப்பட்டுள்ளது.",
            "tip_en": "Buoyancy = When overall tax base expands, local bodies automatically benefit from higher nominal transfers.",
            "tip_ta": "விரிவாக்கம் = ஒட்டுமொத்த வரி அடிப்படை விரிவடையும் போது, உள்ளாட்சி அமைப்புகள் தானாகவே அதிக நிதிப் பரிமாற்றங்களைப் பெறுகின்றன.",
            "fact_en": "In Tamil Nadu, the SFCs moved from individual tax-sharing to a consolidated divisible pool of aggregate SOTR.",
            "fact_ta": "தமிழ்நாட்டில், SFC-கள் தனிப்பட்ட வரிப் பகிர்விலிருந்து ஒட்டுமொத்த SOTR-ன் ஒருங்கிணைந்த பகிர்வுத் தொகுப்பிற்கு மாறின."
        },

        # 29. Audit and Surcharge Proceedings under Local Fund Audit
        {
            "subtopic": "Tamil Nadu State Election & Finance Commissions - Legal Framework, Rules & Precedents",
            "stem_en": "What is the function of 'surcharge proceedings' initiated by the Local Fund Audit Department against a local body elected functionary in Tamil Nadu?",
            "stem_ta": "தமிழ்நாட்டில் உள்ளாட்சி அமைப்பின் தேர்ந்தெடுக்கப்பட்ட பிரதிநிதிக்கு எதிராக உள்ளூர் நிதித் தணிக்கைத் துறையால் தொடங்கப்படும் 'கூடுதல் கட்டண நடவடிக்கை' (surcharge proceedings)-ன் செயல்பாடு என்ன?",
            "options": [
                ("To recover financial loss, waste, or misappropriation of local body funds directly from the personal assets of the defaulting functionary", "தவறிழைத்த பிரதிநிதியின் தனிப்பட்ட சொத்துக்களிலிருந்து நேரடியாக உள்ளாட்சி நிதி இழப்பு, விரயம் அல்லது நிதி முறைகேடுகளை மீட்டெடுக்க"),
                ("To double the salary and allowances of the functionary as a performance reward", "செயல்திறன் வெகுமதியாக பிரதிநிதியின் ஊதியம் மற்றும் படிகளை இரட்டிப்பாக்க"),
                ("To promote the Village Panchayat President directly to the position of High Court Judge", "கிராம பஞ்சாயத்து தலைவரை நேரடியாக உயர் நீதிமன்ற நீதிபதி பதவிக்கு உயர்த்த"),
                ("To exempt the local body from all constitutional and statutory accounting audits forever", "உள்ளாட்சி அமைப்பை அனைத்து அரசியலமைப்பு மற்றும் சட்டப்பூர்வ தணிக்கைகளிலிருந்தும் என்றென்றும் விடுவிக்க")
            ],
            "correct_key": "A",
            "exp_en": "Under the Tamil Nadu Local Fund Audit Act and TN Panchayats Act 1994, surcharge is a quasi-judicial process where auditors disallow illegal expenditures and hold the responsible President/Chairman personally liable, ordering recovery of the squandered amount as arrears of land revenue.",
            "exp_ta": "தமிழ்நாடு உள்ளூர் நிதித் தணிக்கைச் சட்டம் மற்றும் 1994 பஞ்சாயத்துகள் சட்டத்தின் கீழ், தணிக்கையாளர்கள் சட்டவிரோத செலவினங்களை நிராகரித்து, சம்பந்தப்பட்ட தலைவர் மீது தனிப்பட்ட முறையில் பொறுப்பைச் சுமத்தி, வீணடிக்கப்பட்ட தொகையை நில வருவாய் நிலுவைத் தொகையாக மீட்டெடுக்க உத்தரவிடும் ஒரு நீதித்துறை போன்ற செயல்முறையே 'சர்சார்ஜ்' ஆகும்.",
            "why_a_en": "Correct. Surcharge recovers misappropriated public funds from the personal liability of functionaries.",
            "why_a_ta": "சரி. சர்சார்ஜ் என்பது பிரதிநிதிகளின் தனிப்பட்ட பொறுப்பிலிருந்து முறைகேடு செய்யப்பட்ட பொது நிதியை மீட்டெடுக்கிறது.",
            "why_b_en": "Incorrect. Surcharge is a punitive financial recovery, not a reward.",
            "why_b_ta": "தவறு. சர்சார்ஜ் என்பது தண்டனைக்குரிய நிதி மீட்பு, வெகுமதி அல்ல.",
            "why_c_en": "Incorrect. Surcharge has no connection to judicial promotions.",
            "why_c_ta": "தவறு. சர்சார்ஜுக்கு நீதித்துறை பதவி உயர்வுகளுடன் எந்த தொடர்பும் இல்லை.",
            "why_d_en": "Incorrect. Surcharge reinforces audit rigor rather than exempting it.",
            "why_d_ta": "தவறு. சர்சார்ஜ் தணிக்கைத் தீவிரத்தை வலுப்படுத்துகிறதே தவிர விலக்கு அளிக்காது.",
            "tip_en": "Surcharge = Recovery of wasted or illegal expenditure from the personal purse of the elected official.",
            "tip_ta": "சர்சார்ஜ் = தேர்ந்தெடுக்கப்பட்ட அதிகாரியின் தனிப்பட்ட பணத்திலிருந்து வீணான அல்லது சட்டவிரோத செலவை மீட்டெடுத்தல்.",
            "fact_en": "Section 205 of the TN Panchayats Act allows the District Collector/Inspector of Panchayats to remove a President for serious financial abuse.",
            "fact_ta": "TN பஞ்சாயத்துகள் சட்டத்தின் பிரிவு 205, கடுமையான நிதி முறைகேடுகளுக்காக தலைவரை பதவி நீக்கம் செய்ய மாவட்ட ஆட்சியர்/பஞ்சாயத்து ஆய்வாளருக்கு அதிகாரம் அளிக்கிறது."
        },

        # 30. Indirect Election Disputes Adjudication
        {
            "subtopic": "State Election Commission - Constitutional Mandate & Provisions (Articles 243K & 243ZA)",
            "stem_en": "How are disputes regarding the indirect election of Panchayat Union Chairmen or District Panchayat Chairmen adjudicated in Tamil Nadu?",
            "stem_ta": "தமிழ்நாட்டில் பஞ்சாயத்து ஒன்றியத் தலைவர்கள் அல்லது மாவட்ட பஞ்சாயத்து தலைவர்களின் மறைமுகத் தேர்தல் தொடர்பான சர்ச்சைகள் எவ்வாறு தீர்த்து வைக்கப்படுகின்றன?",
            "options": [
                ("By filing an election petition before the designated Principal District Court within the statutory limitation period", "சட்டப்பூர்வ கால வரம்பிற்குள் நியமிக்கப்பட்ட முதன்மை மாவட்ட நீதிமன்றத்தில் தேர்தல் மனு தாக்கல் செய்வதன் மூலம்"),
                ("By a secret voice vote conducted inside the State Cabinet chamber", "மாநில அமைச்சரவை அறையில் நடத்தப்படும் ரகசிய குரல் வாக்கெடுப்பு மூலம்"),
                ("Disputes are decided conclusively by the district chief of the ruling political party", "ஆளும் அரசியல் கட்சியின் மாவட்டத் தலைவரால் சர்ச்சைகள் இறுதியாகத் தீர்மானிக்கப்படுகின்றன"),
                ("By approaching the International Court of Justice in The Hague", "தி ஹேக்கில் உள்ள சர்வதேச நீதிமன்றத்தை அணுகுவதன் மூலம்")
            ],
            "correct_key": "A",
            "exp_en": "Under the Tamil Nadu Panchayats (Election) Rules and Section 258 of the TN Panchayats Act 1994, all disputes arising from both direct elections (members/presidents) and indirect elections (Chairmen/Vice-Chairmen) must be brought before the designated District Judge via an election petition.",
            "exp_ta": "தமிழ்நாடு பஞ்சாயத்துகள் (தேர்தல்) விதிகள் மற்றும் 1994 TN பஞ்சாயத்துகள் சட்டத்தின் பிரிவு 258-ன் கீழ், நேரடித் தேர்தல்கள் (உறுப்பினர்கள்/தலைவர்கள்) மற்றும் மறைமுகத் தேர்தல்கள் (ஒன்றியத் தலைவர்கள்/துணைத் தலைவர்கள்) இரண்டிலிருந்தும் எழும் அனைத்து சர்ச்சைகளும் தேர்தல் மனு மூலம் நியமிக்கப்பட்ட மாவட்ட நீதிபதியிடம் கொண்டு வரப்பட வேண்டும்.",
            "why_a_en": "Correct. District Courts serve as designated election tribunals under the state act.",
            "why_a_ta": "சரி. மாநில சட்டத்தின் கீழ் நியமிக்கப்பட்ட தேர்தல் தீர்ப்பாயங்களாக மாவட்ட நீதிமன்றங்கள் செயல்படுகின்றன.",
            "why_b_en": "Incorrect. Cabinets have no adjudicatory authority in election disputes.",
            "why_b_ta": "தவறு. தேர்தல் சர்ச்சைகளில் அமைச்சரவைகளுக்கு எந்த தீர்ப்பு அதிகாரமும் இல்லை.",
            "why_c_en": "Incorrect. Political parties possess no statutory dispute-resolution powers.",
            "why_c_ta": "தவறு. அரசியல் கட்சிகளுக்கு சட்டப்பூர்வ சர்ச்சை தீர்க்கும் அதிகாரங்கள் இல்லை.",
            "why_d_en": "Incorrect. ICJ only adjudicates disputes between sovereign nation-states.",
            "why_d_ta": "தவறு. சர்வதேச நீதிமன்றம் இறையாண்மை கொண்ட நாடுகளுக்கு இடையேயான சர்ச்சைகளை மட்டுமே விசாரிக்கிறது.",
            "tip_en": "All election challenges (direct or indirect) must proceed through an Election Petition in the designated District Court.",
            "tip_ta": "அனைத்து தேர்தல் சவால்களும் (நேரடி அல்லது மறைமுக) நியமிக்கப்பட்ட மாவட்ட நீதிமன்றத்தில் தேர்தல் மனு மூலமாக மட்டுமே தொடரப்பட வேண்டும்.",
            "fact_en": "Indirect elections are presided over by an officer specially authorized by the State Election Commission (Returning Officer).",
            "fact_ta": "மறைமுகத் தேர்தல்கள் மாநில தேர்தல் ஆணையத்தால் சிறப்பாக அங்கீகரிக்கப்பட்ட அதிகாரியால் (தேர்தல் நடத்தும் அதிகாரி) தலைமை தாங்கி நடத்தப்படுகின்றன."
        },

        # 31. State Election Commission Staffing Autonomy
        {
            "subtopic": "State Election Commissioner - Appointment, Tenure, Removal & Autonomy",
            "stem_en": "Under Article 243K(3) and Article 243ZA(2), what is the explicit obligation of the Governor of a State regarding the staffing of the State Election Commission?",
            "stem_ta": "சரத்து 243K(3) மற்றும் சரத்து 243ZA(2)-ன் கீழ், மாநில தேர்தல் ஆணையத்திற்கான பணியாளர்கள் தொடர்பாக மாநில ஆளுநரின் வெளிப்படையான கடமை என்ன?",
            "options": [
                ("When so requested by the SEC, make available to the Commission such staff as may be necessary for the discharge of its constitutional functions", "SEC கோரும் போது, அதன் அரசியலமைப்பு பணிகளைச் செய்வதற்குத் தேவையான பணியாளர்களை ஆணையத்திற்கு கிடைக்கச் செய்தல்"),
                ("Mandatorily appoint only retired military personnel without any state civil officers", "எந்தவொரு மாநில சிவில் அதிகாரிகளும் இன்றி ஓய்வுபெற்ற இராணுவ வீரர்களை மட்டுமே கட்டாயமாக நியமிக்க வேண்டும்"),
                ("Refuse staff allocation if the state budget has an unapproved fiscal deficit", "மாநில பட்ஜெட்டில் அங்கீகரிக்கப்படாத நிதிப் பற்றாக்குறை இருந்தால் பணியாளர்கள் ஒதுக்கீட்டை மறுக்கலாம்"),
                ("Direct the staff to report directly to the Chief Minister's office instead of the SEC", "பணியாளர்களை SEC-க்கு பதிலாக முதலமைச்சரின் அலுவலகத்திற்கு நேரடியாக அறிக்கை செய்ய உத்தரவிடலாம்")
            ],
            "correct_key": "A",
            "exp_en": "Articles 243K(3) and 243ZA(2) mandate: 'The Governor of a State shall, when so requested by the State Election Commissioner, make available to the State Election Commissioner such staff as may be necessary for the discharge of the functions conferred on the State Election Commission.'",
            "exp_ta": "சரத்துகள் 243K(3) மற்றும் 243ZA(2) கட்டாயப்படுத்துகின்றன: 'மாநில தேர்தல் ஆணையர் அவ்வாறு கோரும் போது, மாநில தேர்தல் ஆணையத்திற்கு வழங்கப்பட்டுள்ள பணிகளைச் செய்வதற்குத் தேவையான பணியாளர்களை மாநில தேர்தல் ஆணையருக்கு ஆளுநர் கிடைக்கச் செய்ய வேண்டும்.'",
            "why_a_en": "Correct. Verbatim constitutional mandate of Articles 243K(3) and 243ZA(2).",
            "why_a_ta": "சரி. சரத்துகள் 243K(3) மற்றும் 243ZA(2)-ன் சரியான அரசியலமைப்பு கட்டளை.",
            "why_b_en": "Incorrect. No military restriction exists; civil staff are requisitioned.",
            "why_b_ta": "தவறு. இராணுவ கட்டுப்பாடு எதுவும் இல்லை; சிவில் ஊழியர்கள் பெறப்படுகிறார்கள்.",
            "why_c_en": "Incorrect. Fiscal deficit cannot justify withholding election machinery.",
            "why_c_ta": "தவறு. நிதிப் பற்றாக்குறை தேர்தல் இயந்திரத்தை நிறுத்தி வைப்பதை நியாயப்படுத்த முடியாது.",
            "why_d_en": "Incorrect. Staff on election duty are under the sole disciplinary control of the SEC.",
            "why_d_ta": "தவறு. தேர்தல் பணியில் உள்ள ஊழியர்கள் SEC-ன் முழுமையான ஒழுங்கு நடவடிக்கைக் கட்டுப்பாட்டின் கீழ் உள்ளனர்.",
            "tip_en": "Governor MUST provide staff upon SEC's requisition (mirrors Art 324(6) for ECI).",
            "tip_ta": "SEC கோரிக்கையின் பேரில் ஆளுநர் கட்டாயம் பணியாளர்களை வழங்க வேண்டும் (ECI-க்கான சரத்து 324(6)-ஐப் பிரதிபலிக்கிறது).",
            "fact_en": "Failure of the State Government to provide adequate staff can be penalized by the Supreme Court under contempt powers.",
            "fact_ta": "போதிய பணியாளர்களை வழங்க மாநில அரசு தவறினால் நீதிமன்ற அவமதிப்பு அதிகாரத்தின் கீழ் உச்ச நீதிமன்றத்தால் தண்டிக்கப்படலாம்."
        },

        # 32. SFC Powers to Summon and Enforce Evidence
        {
            "subtopic": "State Finance Commission - Constitutional Mandate, Composition & Role (Articles 243I & 243Y)",
            "stem_en": "Under state legislation framed pursuant to Article 243-I(2), what procedural powers are vested in the State Finance Commission while conducting inquiries and assessing fiscal data?",
            "stem_ta": "சரத்து 243-I(2)-ன் படி உருவாக்கப்பட்ட மாநில சட்டத்தின் கீழ், விசாரணைகளை நடத்தும் போதும் நிதித் தரவை மதிப்பிடும் போதும் மாநில நிதி ஆணையத்திற்கு என்ன நடைமுறை அதிகாரங்கள் வழங்கப்பட்டுள்ளன?",
            "options": [
                ("Powers of a Civil Court under the Code of Civil Procedure, 1908 (summoning witnesses, requisitioning public records, requiring discovery of documents)", "சிவில் நடைமுறைச் சட்டம் 1908-ன் கீழ் ஒரு சிவில் நீதிமன்றத்தின் அதிகாரங்கள் (சாட்சிகளை அழைத்தல், பொது ஆவணங்களை கோருதல், ஆவணங்களை சமர்ப்பிக்கக் கோருதல்)"),
                ("Powers to pronounce capital punishment and imprison defaulters indefinitely", "மரண தண்டனை விதிக்க மற்றும் தவறிழைத்தவர்களை காலவரையின்றி சிறையில் அடைக்க அதிகாரங்கள்"),
                ("Powers to dismiss the State Cabinet and assume administrative executive control", "மாநில அமைச்சரவையை டிஸ்மிஸ் செய்து நிர்வாகக் கட்டுப்பாட்டை ஏற்கும் அதிகாரங்கள்"),
                ("Zero procedural powers; it operates purely as an informal debating club", "பூஜ்ஜிய நடைமுறை அதிகாரங்கள்; இது முற்றிலும் ஒரு முறைசாரா விவாத மன்றமாக மட்டுமே செயல்படுகிறது")
            ],
            "correct_key": "A",
            "exp_en": "State Finance Commission Acts (e.g., Section 241 of TN Panchayats Act 1994) endow the SFC with the powers of a Civil Court under the Code of Civil Procedure 1908, including summoning witnesses, examining on oath, discovery and production of documents, and requisitioning public records.",
            "exp_ta": "மாநில நிதி ஆணையச் சட்டங்கள் (எ.கா. 1994 TN பஞ்சாயத்துகள் சட்டத்தின் பிரிவு 241) SFC-க்கு சிவில் நடைமுறைச் சட்டம் 1908-ன் கீழ் ஒரு சிவில் நீதிமன்றத்தின் அதிகாரங்களை வழங்குகின்றன. இதில் சாட்சிகளை அழைப்பது, சத்தியப்பிரமாணத்தின் கீழ் விசாரிப்பது, ஆவணங்களைக் கோருவது மற்றும் பொது ஆவணங்களைப் பெறுவது ஆகியவை அடங்கும்.",
            "why_a_en": "Correct. SFC has civil court powers to ensure access to verified financial accounts.",
            "why_a_ta": "சரி. சரிபார்க்கப்பட்ட கணக்குகளை அணுகுவதை உறுதி செய்ய SFC-க்கு சிவில் நீதிமன்ற அதிகாரங்கள் உள்ளன.",
            "why_b_en": "Incorrect. SFC has no penal or criminal court powers.",
            "why_b_ta": "தவறு. SFC-க்கு குற்றவியல் நீதிமன்ற அதிகாரங்கள் இல்லை.",
            "why_c_en": "Incorrect. SFC cannot dismiss elected cabinets.",
            "why_c_ta": "தவறு. SFC தேர்ந்தெடுக்கப்பட்ட அமைச்சரவைகளை கலைக்க முடியாது.",
            "why_d_en": "Incorrect. SFC is a constitutional body with statutory civil court powers.",
            "why_d_ta": "தவறு. SFC என்பது சட்டப்பூர்வ சிவில் நீதிமன்ற அதிகாரங்களைக் கொண்ட ஒரு அரசியலமைப்பு அமைப்பாகும்.",
            "tip_en": "SFC powers = Civil Court powers under CPC 1908 (mirrors Central FC under Commission of Inquiry framework).",
            "tip_ta": "SFC அதிகாரங்கள் = CPC 1908-ன் கீழ் சிவில் நீதிமன்ற அதிகாரங்கள்.",
            "fact_en": "All proceedings before the Commission are deemed judicial proceedings within the meaning of Sections 193 and 228 of the IPC.",
            "fact_ta": "ஆணையத்தின் முன் நடைபெறும் அனைத்து நடவடிக்கைகளும் IPC-ன் 193 மற்றும் 228 பிரிவுகளின் கீழ் நீதித்துறை நடவடிக்கைகளாகக் கருதப்படுகின்றன."
        },

        # 33. State Finance Commission - Non-Binding Nature of Recommendations
        {
            "subtopic": "State Finance Commission - Constitutional Mandate, Composition & Role (Articles 243I & 243Y)",
            "stem_en": "What is the precise constitutional and legal status of the recommendations submitted by a State Finance Commission to the State Government?",
            "stem_ta": "மாநில நிதி ஆணையம் மாநில அரசிற்கு சமர்ப்பிக்கும் பரிந்துரைகளின் துல்லியமான அரசியலமைப்பு மற்றும் சட்டப்பூர்வ நிலை என்ன?",
            "options": [
                ("They are advisory in nature and not legally binding on the Government, though the Government is constitutionally bound to explain any deviation in the Action Taken Report", "அவை ஆலோசனைத் தன்மை கொண்டவை மற்றும் அரசாங்கத்தைக் கட்டுப்படுத்தாது, இருப்பினும் எடுக்கப்பட்ட நடவடிக்கை அறிக்கையில் ஏதேனும் மாறுபாடுகளை விளக்க அரசாங்கம் அரசியலமைப்பு ரீதியாகக் கடமைப்பட்டுள்ளது"),
                ("They constitute an automatic statutory decree that directly amends the Constitution without legislative passage", "அவை சட்டமன்ற ஒப்புதல் இன்றியே அரசியலமைப்பை நேரடியாகத் திருத்தும் ஒரு தானியங்கி சட்ட ஆணை ஆகும்"),
                ("They are subject to immediate veto by the District Collector without appeal", "அவை மேல்முறையீடின்றி மாவட்ட ஆட்சியரின் உடனடி வீட்டோ அதிகாரத்திற்கு உட்பட்டவை"),
                ("They are binding only on opposition MLAs while ruling party members are exempt", "அவை எதிர்க்கட்சி எம்.எல்.ஏ.-க்களை மட்டுமே கட்டுப்படுத்தும், ஆளும் கட்சி உறுப்பினர்களுக்கு விலக்கு அளிக்கப்படும்")
            ],
            "correct_key": "A",
            "exp_en": "Just like the Central Finance Commission under Article 280, the recommendations of the State Finance Commission are advisory and recommendatory. The State Government has executive discretion to accept, modify, or reject them, provided it tables an Explanatory Memorandum (ATR) detailing reasons before the Legislature.",
            "exp_ta": "சரத்து 280-ன் கீழ் உள்ள மத்திய நிதி ஆணையத்தைப் போலவே, மாநில நிதி ஆணையத்தின் பரிந்துரைகளும் ஆலோசனைத் தன்மை கொண்டவை. சட்டமன்றத்தின் முன் காரணங்களை விளக்கும் குறிப்பை (ATR) சமர்ப்பித்தால், அவற்றை ஏற்றுக்கொள்ளவோ, மாற்றவோ அல்லது நிராகரிக்கவோ மாநில அரசுக்கு நிர்வாக விருப்ப உரிமை உண்டு.",
            "why_a_en": "Correct. Advisory status with a mandatory explanatory memorandum under Art 243-I(4).",
            "why_a_ta": "சரி. சரத்து 243-I(4)-ன் கீழ் கட்டாய விளக்கக் குறிப்புடன் கூடிய ஆலோசனை நிலை.",
            "why_b_en": "Incorrect. SFC recommendations cannot alter the Constitution automatically.",
            "why_b_ta": "தவறு. SFC பரிந்துரைகள் அரசியலமைப்பை தானாகவே மாற்ற முடியாது.",
            "why_c_en": "Incorrect. District Collectors have no constitutional authority over SFC reports.",
            "why_c_ta": "தவறு. SFC அறிக்கைகள் மீது மாவட்ட ஆட்சியர்களுக்கு எந்த அரசியலமைப்பு அதிகாரமும் இல்லை.",
            "why_d_en": "Incorrect. Advisory status applies across all legislative members uniformly.",
            "why_d_ta": "தவறு. ஆலோசனை நிலை அனைத்து சட்டமன்ற உறுப்பினர்களுக்கும் ஒரே மாதிரியாகப் பொருந்தும்.",
            "tip_en": "Finance Commission recommendations = Advisory. Explanatory Memorandum (ATR) = Mandatory.",
            "tip_ta": "நிதி ஆணையப் பரிந்துரைகள் = ஆலோசனை. விளக்கக் குறிப்பு (ATR) = கட்டாயம்.",
            "fact_en": "Conventional democratic norms establish that governments accept majority of SFC devolution formulas unless extraordinary fiscal crises occur.",
            "fact_ta": "வழக்கமான ஜனநாயக நெறிமுறைகள், அசாதாரண நிதி நெருக்கடிகள் ஏற்படாவிட்டால் பெரும்பாலான SFC பகிர்வு சூத்திரங்களை அரசாங்கங்கள் ஏற்றுக்கொள்வதை நிறுவியுள்ளன."
        },

        # 34. Reservation of Offices in Local Bodies (Article 243D & 243T)
        {
            "subtopic": "State Election Commission - Constitutional Mandate & Provisions (Articles 243K & 243ZA)",
            "stem_en": "In K. Krishna Murthy v. Union of India (2010), what key principle was laid down by the Supreme Court regarding the reservation of seats and chairperson posts in local bodies under Articles 243D and 243T?",
            "stem_ta": "கே. கிருஷ்ண மூர்த்தி எதிர் இந்திய அரசு (2010) வழக்கில், சரத்துகள் 243D மற்றும் 243T-ன் கீழ் உள்ளாட்சி அமைப்புகளில் இடங்கள் மற்றும் தலைவர் பதவிகளுக்கான இடஒதுக்கீடு தொடர்பாக உச்ச நீதிமன்றம் வகுத்த முக்கிய கொள்கை என்ன?",
            "options": [
                ("Total reservation for SC, ST, and OBCs in local bodies cannot exceed an aggregate ceiling of 50%, and reservation for OBCs requires empirical inquiry into backwardness", "உள்ளாட்சி அமைப்புகளில் SC, ST மற்றும் OBC-களுக்கான மொத்த இடஒதுக்கீடு 50% உச்சவரம்பை தாண்டக்கூடாது, மேலும் OBC-களுக்கான இடஒதுக்கீட்டிற்கு பின்தங்கிய நிலை குறித்த அனுபவ ரீதியான விசாரணை தேவைப்படுகிறது"),
                ("Reservations in local bodies can be extended up to 100% at the sole discretion of the District Collector", "மாவட்ட ஆட்சியரின் விருப்பத்தின் பேரில் உள்ளாட்சி அமைப்புகளில் இடஒதுக்கீட்டை 100% வரை நீட்டிக்க முடியும்"),
                ("Women's reservation is limited only to nominated seats and prohibited in directly elected ward seats", "பெண்கள் இடஒதுக்கீடு நியமன இடங்களுக்கு மட்டுமே வரம்பிடப்பட்டுள்ளது மற்றும் நேரடியாக தேர்ந்தெடுக்கப்படும் வார்டு இடங்களில் தடைசெய்யப்பட்டுள்ளது"),
                ("Chairperson offices in Panchayats cannot be reserved for SC or ST candidates under any circumstances", "பஞ்சாயத்துகளில் தலைவர் பதவிகளை எந்த சூழ்நிலையிலும் SC அல்லது ST வேட்பாளர்களுக்கு ஒதுக்க முடியாது")
            ],
            "correct_key": "A",
            "exp_en": "In K. Krishna Murthy (2010), reaffirmed in Vikas Kishanrao Gawali (2021), a 5-judge bench held that political reservation in local bodies under Articles 243D and 243T cannot exceed the 50% ceiling laid down in Indra Sawhney, and providing OBC reservations requires a 'triple test' (dedicated commission, empirical data, ceiling).",
            "exp_ta": "கே. கிருஷ்ண மூர்த்தி (2010) வழக்கில், இந்திரா சாஹ்னி வழக்கில் நிர்ணயிக்கப்பட்ட 50% உச்சவரம்பை சரத்துகள் 243D மற்றும் 243T-ன் கீழான அரசியல் இடஒதுக்கீடு தாண்டக்கூடாது என்றும், OBC இடஒதுக்கீட்டிற்கு 'மூன்று கட்ட சோதனை' தேவை என்றும் 5 நீதிபதிகள் கொண்ட அமர்வு தீர்ப்பளித்தது.",
            "why_a_en": "Correct. 50% ceiling applies to vertical reservation in local self-government bodies.",
            "why_a_ta": "சரி. உள்ளாட்சி அமைப்புகளில் செங்குத்து இடஒதுக்கீட்டிற்கு 50% உச்சவரம்பு பொருந்தும்.",
            "why_b_en": "Incorrect. 100% reservation violates equality and is unconstitutional.",
            "why_b_ta": "தவறு. 100% இடஒதுக்கீடு சமத்துவத்தை மீறுகிறது மற்றும் அரசியலமைப்பிற்கு முரணானது.",
            "why_c_en": "Incorrect. Women's reservation applies to both ward seats and chairperson offices.",
            "why_c_ta": "தவறு. பெண்கள் இடஒதுக்கீடு வார்டு இடங்கள் மற்றும் தலைவர் பதவிகள் இரண்டிற்கும் பொருந்தும்.",
            "why_d_en": "Incorrect. Article 243D(4) explicitly requires reservation of chairperson offices for SCs and STs.",
            "why_d_ta": "தவறு. சரத்து 243D(4) தலைவர் பதவிகளை SC மற்றும் ST-களுக்கு ஒதுக்குவதை வெளிப்படையாகக் கட்டாயப்படுத்துகிறது.",
            "tip_en": "Triple test for local body OBC quotas: 1. Commission for empirical inquiry, 2. Specify proportion, 3. Aggregate <= 50%.",
            "tip_ta": "உள்ளாட்சி OBC இடஒதுக்கீட்டிற்கான மூன்று சோதனை: 1. பிரத்யேக ஆணையம், 2. விகிதத்தைக் குறிப்பிடுதல், 3. மொத்தம் <= 50%.",
            "fact_en": "Tamil Nadu provides 50% reservation for women across all local body ward seats and chairperson offices.",
            "fact_ta": "தமிழ்நாடு அனைத்து உள்ளாட்சி வார்டு இடங்கள் மற்றும் தலைவர் பதவிகளில் பெண்களுக்கு 50% இடஒதுக்கீடு வழங்குகிறது."
        },

        # 35. Article 243-O(b) Election Petition Forum in Tamil Nadu
        {
            "subtopic": "Tamil Nadu State Election & Finance Commissions - Legal Framework, Rules & Precedents",
            "stem_en": "Under the Tamil Nadu Panchayats Act 1994, which judicial officer is designated as the competent election tribunal to adjudicate election petitions challenging the election of a Village Panchayat President?",
            "stem_ta": "1994 தமிழ்நாடு பஞ்சாயத்துகள் சட்டத்தின் கீழ், கிராம பஞ்சாயத்து தலைவரின் தேர்தலை எதிர்த்து தொடரப்படும் தேர்தல் மனுக்களை விசாரிக்க எந்த நீதித்துறை அதிகாரி தகுதிவாய்ந்த தேர்தல் தீர்ப்பாயமாக நியமிக்கப்பட்டுள்ளார்?",
            "options": [
                ("The Principal District Judge / District Judge having territorial jurisdiction over the area", "சம்பந்தப்பட்ட பகுதியின் மீது அதிகார வரம்பு கொண்ட முதன்மை மாவட்ட நீதிபதி / மாவட்ட நீதிபதி"),
                ("The local Village Administrative Officer (VAO)", "உள்ளூர் கிராம நிர்வாக அலுவலர் (VAO)"),
                ("The Block Development Officer (BDO)", "வட்டார வளர்ச்சி அலுவலர் (BDO)"),
                ("The Sub-Inspector of Police of the local police station", "உள்ளூர் காவல் நிலையத்தின் காவல் சார்பு ஆய்வாளர்")
            ],
            "correct_key": "A",
            "exp_en": "Section 258 of the Tamil Nadu Panchayats Act 1994 designates the Principal District Judge (or a District Judge nominated by the Principal District Judge) as the election tribunal to try election petitions questioning any election held under the Act.",
            "exp_ta": "1994 தமிழ்நாடு பஞ்சாயத்துகள் சட்டத்தின் பிரிவு 258, இச்சட்டத்தின் கீழ் நடத்தப்படும் எந்தவொரு தேர்தலையும் கேள்விக்குள்ளாக்கும் தேர்தல் மனுக்களை விசாரிக்கும் தேர்தல் தீர்ப்பாயமாக முதன்மை மாவட்ட நீதிபதியை (அல்லது அவரால் பரிந்துரைக்கப்பட்ட மாவட்ட நீதிபதியை) நியமிக்கிறது.",
            "why_a_en": "Correct. Principal District Judge serves as the statutory election tribunal.",
            "why_a_ta": "சரி. முதன்மை மாவட்ட நீதிபதி சட்டப்பூர்வ தேர்தல் தீர்ப்பாயமாகச் செயல்படுகிறார்.",
            "why_b_en": "Incorrect. VAO is a revenue village administrative functionary with no judicial powers.",
            "why_b_ta": "தவறு. VAO என்பது நீதித்துறை அதிகாரங்கள் இல்லாத ஒரு கிராம நிர்வாகப் பணியாகும்.",
            "why_c_en": "Incorrect. BDO is an executive official and returning officer, not an adjudicatory tribunal.",
            "why_c_ta": "தவறு. BDO ஒரு நிர்வாக அதிகாரி மற்றும் தேர்தல் நடத்தும் அதிகாரி, தீர்ப்பாயம் அல்ல.",
            "why_d_en": "Incorrect. Police officers have no judicial adjudicatory role in election petitions.",
            "why_d_ta": "தவறு. தேர்தல் மனுக்களில் காவல்துறை அதிகாரிகளுக்கு எந்த நீதித்துறை பங்கும் இல்லை.",
            "tip_en": "TN Panchayats Act 1994 Sec 258 = Election Petitions decided by District Judge.",
            "tip_ta": "TN பஞ்சாயத்துகள் சட்டம் 1994 பிரிவு 258 = தேர்தல் மனுக்கள் மாவட்ட நீதிபதியால் தீர்மானிக்கப்படுகின்றன.",
            "fact_en": "An appeal against the decision of the District Judge lies to the High Court under Section 258(8).",
            "fact_ta": "மாவட்ட நீதிபதியின் முடிவுக்கு எதிரான மேல்முறையீடு பிரிவு 258(8)-ன் கீழ் உயர் நீதிமன்றத்தில் தாக்கல் செய்யப்படலாம்."
        },

        # 36. SFC Incentive Grants for Own Revenue Mobilization
        {
            "subtopic": "Financial Devolution, Intergovernmental Transfers & Local Governance",
            "stem_en": "Why do State Finance Commissions recommend dedicating an 'Incentive Fund' as part of the devolution envelope to local bodies?",
            "stem_ta": "உள்ளாட்சி அமைப்புகளுக்கு நிதியைப் பகிர்ந்தளிக்கும் போது மாநில நிதி ஆணையங்கள் ஒரு 'ஊக்க நிதியை' (Incentive Fund) ஒதுக்க ஏன் பரிந்துரைக்கின்றன?",
            "options": [
                ("To reward local bodies that achieve higher local tax collection efficiency, prompt property tax revisions, and own-revenue mobilization", "அதிக உள்ளூர் வரி வசூல் திறன், விரைவான சொத்து வரி திருத்தங்கள் மற்றும் சொந்த வருவாய் திரட்டலை அடையும் உள்ளாட்சி அமைப்புகளுக்கு வெகுமதி அளிக்க"),
                ("To subsidize corrupt contractors who abandon public toilet construction mid-way", "பொதுக் கழிப்பறை கட்டுமானத்தை பாதியில் கைவிடும் ஊழல் ஒப்பந்ததாரர்களுக்கு மானியம் வழங்க"),
                ("To penalize panchayats that maintain 100% clean drinking water connections", "100% சுத்தமான குடிநீர் இணைப்புகளைப் பராமரிக்கும் பஞ்சாயத்துகளைத் தண்டிக்க"),
                ("To purchase expensive overseas vacation tickets for local body ward members", "உள்ளாட்சி வார்டு உறுப்பினர்களுக்கு விலைமதிப்பற்ற வெளிநாட்டு சுற்றுலா டிக்கெட்டுகளை வாங்க")
            ],
            "correct_key": "A",
            "exp_en": "An Incentive Fund (recommended by successive Tamil Nadu SFCs and Central FCs) acts as a performance grant: local bodies that maximize their own tax revenues (e.g. house tax, profession tax, non-tax fees) receive matching grants from the fund, discouraging complacency and dependency on state transfers.",
            "exp_ta": "ஒரு ஊக்க நிதி (அடுத்தடுத்த தமிழ்நாடு SFC-கள் மற்றும் மத்திய FC-களால் பரிந்துரைக்கப்படுகிறது) ஒரு செயல்திறன் மானியமாக செயல்படுகிறது: தங்கள் சொந்த வரி வருவாயை (வீட்டு வரி, தொழில் வரி போன்றவை) அதிகரிக்கும் உள்ளாட்சி அமைப்புகள் இந்த நிதியிலிருந்து கூடுதல் மானியங்களைப் பெறுகின்றன, இது மாநில நிதியை மட்டுமே சார்ந்திருப்பதைத் தடுக்கிறது.",
            "why_a_en": "Correct. Performance-linked incentive funds foster local fiscal effort and tax buoyancy.",
            "why_a_ta": "சரி. செயல்திறன் அடிப்படையிலான ஊக்க நிதிகள் உள்ளூர் நிதி முயற்சி மற்றும் வரி வசூலை ஊக்குவிக்கின்றன.",
            "why_b_en": "Incorrect. Incentive funds reward efficiency, not corruption.",
            "why_b_ta": "தவறு. ஊக்க நிதிகள் திறனை வெகுமதி அளிக்கின்றன, ஊழலை அல்ல.",
            "why_c_en": "Incorrect. High service performance is rewarded, never penalized.",
            "why_c_ta": "தவறு. உயர் செயல்திறன் வெகுமதி அளிக்கப்படுகிறது, தண்டிக்கப்படுவதில்லை.",
            "why_d_en": "Incorrect. Funds cannot be diverted for private leisure travel.",
            "why_d_ta": "தவறு. நிதியை தனிப்பட்ட பயணங்களுக்கு திருப்பி விட முடியாது.",
            "tip_en": "Incentive grants motivate local bodies to mobilize their own source revenues (OSR).",
            "tip_ta": "ஊக்க மானியங்கள் உள்ளாட்சி அமைப்புகள் தங்கள் சொந்த மூல வருவாயை (OSR) திரட்ட தூண்டுகின்றன.",
            "fact_en": "In Tamil Nadu, a Capital Grant Fund (CGF) and Operational Reserve Fund (ORF) are operated alongside devolution to address infrastructure deficits.",
            "fact_ta": "தமிழ்நாட்டில், உள்கட்டமைப்பு பற்றாக்குறையை நிவர்த்தி செய்ய மூலதன மானிய நிதி (CGF) மற்றும் செயல்பாட்டு இருப்பு நிதி (ORF) ஆகியவை இயக்கப்படுகின்றன."
        },

        # 37. Symbol Allotment Rules in Local Elections
        {
            "subtopic": "Tamil Nadu State Election & Finance Commissions - Legal Framework, Rules & Precedents",
            "stem_en": "In Tamil Nadu, how does the State Election Commission regulate the allotment of election symbols to candidates contesting local body elections?",
            "stem_ta": "தமிழ்நாட்டில், உள்ளாட்சித் தேர்தலில் போட்டியிடும் வேட்பாளர்களுக்கு தேர்தல் சின்னங்களை ஒதுக்குவதை மாநில தேர்தல் ஆணையம் எவ்வாறு ஒழுங்குபடுத்துகிறது?",
            "options": [
                ("Recognized political parties are allotted their reserved symbols in party-based elections (Corporations, Municipalities, PU Councillors), while free symbols from an approved list are allotted to independent candidates and non-party panchayat elections", "கட்சி அடிப்படையிலான தேர்தல்களில் (மாநகராட்சிகள், நகராட்சிகள், ஒன்றிய கவுன்சிலர்கள்) அங்கீகரிக்கப்பட்ட கட்சிகளுக்கு அவற்றின் ஒதுக்கப்பட்ட சின்னங்கள் ஒதுக்கப்படுகின்றன; சுயேச்சை வேட்பாளர்கள் மற்றும் கட்சி சாரா பஞ்சாயத்து தேர்தல்களுக்கு அங்கீகரிக்கப்பட்ட பட்டியலிலிருந்து சுயேச்சை சின்னங்கள் ஒதுக்கப்படுகின்றன"),
                ("All candidates are legally required to draw their own hand-made sketches on ballot papers", "அனைத்து வேட்பாளர்களும் வாக்குச் சீட்டுகளில் தங்கள் சொந்த கையால் வரையப்பட்ட படங்களை வரைய சட்டப்படி கடமைப்பட்டுள்ளனர்"),
                ("Symbols are auctioned to the highest bidder by the District Collector", "சின்னங்கள் மாவட்ட ஆட்சியரால் அதிக ஏலம் எடுப்பவருக்கு ஏலம் விடப்படுகின்றன"),
                ("The SEC uses national flags of foreign countries as symbols for all local body contestants", "அனைத்து உள்ளாட்சிப் போட்டியாளர்களுக்கும் வெளிநாடுகளின் தேசியக் கொடிகளை SEC சின்னங்களாகப் பயன்படுத்துகிறது")
            ],
            "correct_key": "A",
            "exp_en": "Under the Tamil Nadu Panchayats / Municipalities (Allotment of Symbols) Rules, the SEC reserves symbols for recognized national and state parties for political posts (Corporation, Municipality, Town Panchayat councillors, PU & District Panchayat wards). For non-party posts (Village Panchayat President and Member) and independents, symbols are chosen from a published list of free symbols.",
            "exp_ta": "சின்னங்கள் ஒதுக்கீடு விதிகளின் கீழ், அரசியல் பதவிகளுக்கு (மாநகராட்சி, நகராட்சி, பேரூராட்சி, ஒன்றிய/மாவட்ட வார்டுகள்) அங்கீகரிக்கப்பட்ட தேசிய மற்றும் மாநிலக் கட்சிகளுக்கு சின்னங்களை SEC ஒதுக்குகிறது. கட்சி சாரா பதவிகள் (கிராம பஞ்சாயத்து தலைவர் மற்றும் உறுப்பினர்) மற்றும் சுயேச்சைகளுக்கு அங்கீகரிக்கப்பட்ட சுயேச்சை சின்னங்கள் பட்டியலிலிருந்து ஒதுக்கப்படுகின்றன.",
            "why_a_en": "Correct. Reserved symbols for recognized parties in party posts; free symbols for independents/village posts.",
            "why_a_ta": "சரி. கட்சிப் பதவிகளுக்கு அங்கீகரிக்கப்பட்ட கட்சிகளுக்கு ஒதுக்கப்பட்ட சின்னங்கள்; சுயேச்சை/கிராம பதவிகளுக்கு இலவச சின்னங்கள்.",
            "why_b_en": "Incorrect. Standardized symbols are officially printed on ballot papers and EVMs.",
            "why_b_ta": "தவறு. தரப்படுத்தப்பட்ட சின்னங்கள் அதிகாரப்பூர்வமாக வாக்குச் சீட்டுகள் மற்றும் EVM-களில் அச்சிடப்படுகின்றன.",
            "why_c_en": "Incorrect. Symbol auctioning is strictly illegal and a corrupt electoral practice.",
            "why_c_ta": "தவறு. சின்னங்களை ஏலம் விடுவது முற்றிலும் சட்டவிரோதமானது மற்றும் ஊழல் நடைமுறையாகும்.",
            "why_d_en": "Incorrect. Foreign flags or religious symbols are legally prohibited as election symbols.",
            "why_d_ta": "தவறு. வெளிநாட்டுக் கொடிகள் அல்லது மதச் சின்னங்கள் தேர்தல் சின்னங்களாகப் பயன்படுத்த தடை செய்யப்பட்டுள்ளன.",
            "tip_en": "Village Panchayat elections in TN are strictly NON-PARTY elections; party symbols CANNOT be used.",
            "tip_ta": "TN-ல் கிராம பஞ்சாயத்து தேர்தல்கள் முற்றிலும் கட்சி சாரா தேர்தல்கள்; கட்சி சின்னங்களைப் பயன்படுத்த முடியாது.",
            "fact_en": "Candidates contesting on party tickets must submit the official party authorization form ('Form A' and 'Form B') before the deadline.",
            "fact_ta": "கட்சி சின்னத்தில் போட்டியிடும் வேட்பாளர்கள் கடைசி தேதிக்குள் அதிகாரப்பூர்வ கட்சி அங்கீகார படிவத்தை ('படிவம் A' மற்றும் 'படிவம் B') சமர்ப்பிக்க வேண்டும்."
        },

        # 38. Article 243-E Six-Month Residual Tenure Exception
        {
            "subtopic": "State Election Commission - Constitutional Mandate & Provisions (Articles 243K & 243ZA)",
            "stem_en": "Under the proviso to Article 243-E(3) and Article 243-U(3), under what circumstance is a by-election NOT required when a casual vacancy occurs in a local body?",
            "stem_ta": "சரத்து 243-E(3) மற்றும் சரத்து 243-U(3)-ன் வரம்புரையின் கீழ், ஓர் உள்ளாட்சி அமைப்பில் தற்காலிக காலியிடம் ஏற்படும் போது எந்த சூழ்நிலையில் இடைத்தேர்தல் நடத்த தேவையில்லை?",
            "options": [
                ("Where the remainder of the period for which the dissolved local body or vacant seat would have continued is less than six months", "கலைக்கப்பட்ட உள்ளாட்சி அமைப்பு அல்லது காலியான இடம் நீடித்திருக்கக்கூடிய மீதமுள்ள காலம் ஆறு மாதங்களுக்கும் குறைவாக இருக்கும் போது"),
                ("If the vacant seat belonged to an independent candidate", "காலியான இடம் ஒரு சுயேச்சை வேட்பாளருக்கு சொந்தமானதாக இருந்தால்"),
                ("If the State Assembly passes an unanimous resolution opposing by-elections", "இடைத்தேர்தலை எதிர்த்து மாநில சட்டமன்றம் ஒருமனதாக தீர்மானம் நிறைவேற்றினால்"),
                ("Whenever the local temperature exceeds 40 degrees Celsius on polling day", "வாக்குப்பதிவு நாளில் உள்ளூர் வெப்பநிலை 40 டிகிரி செல்சியஸைத் தாண்டும் போதெல்லாம்")
            ],
            "correct_key": "A",
            "exp_en": "The proviso to Article 243-E(3) and 243-U(3) states that where the remainder of the period for which the dissolved Municipality or Panchayat would have continued is less than six months, it shall not be necessary to hold any election under this clause for constituting the Municipality/Panchayat for that period.",
            "exp_ta": "சரத்து 243-E(3) மற்றும் 243-U(3)-ன் வரம்புரை, கலைக்கப்பட்ட நகராட்சி அல்லது பஞ்சாயத்து நீடித்திருக்கக்கூடிய மீதமுள்ள காலம் ஆறு மாதங்களுக்கும் குறைவாக இருந்தால், அந்தக் காலத்திற்கு நகராட்சி/பஞ்சாயத்தை அமைப்பதற்கு தேர்தல் எதுவும் நடத்த தேவையில்லை என்று கூறுகிறது.",
            "why_a_en": "Correct. If less than 6 months remain, a by-election is dispensed with.",
            "why_a_ta": "சரி. 6 மாதங்களுக்கும் குறைவாக மீதமிருந்தால், இடைத்தேர்தல் நடத்த தேவையில்லை.",
            "why_b_en": "Incorrect. The rule applies regardless of whether the member was party-affiliated or independent.",
            "why_b_ta": "தவறு. உறுப்பினர் கட்சி சார்ந்தவரா அல்லது சுயேச்சையா என்பதைப் பொருட்படுத்தாமல் இந்த விதி பொருந்தும்.",
            "why_c_en": "Incorrect. Legislative resolutions cannot waive constitutional by-election mandates.",
            "why_c_ta": "தவறு. சட்டமன்ற தீர்மானங்கள் அரசியலமைப்பு இடைத்தேர்தல் கட்டளைகளை ரத்து செய்ய முடியாது.",
            "why_d_en": "Incorrect. Weather conditions do not dispense with constitutional election obligations.",
            "why_d_ta": "தவறு. வானிலை நிலைமைகள் அரசியலமைப்புத் தேர்தல் கடமைகளிலிருந்து விலக்கு அளிக்காது.",
            "tip_en": "Residual tenure < 6 months: NO by-election required. Same rule applies to Parliament & State Assemblies under RPA 1951 Sec 151A.",
            "tip_ta": "மீதமுள்ள பதவிக்காலம் < 6 மாதங்கள்: இடைத்தேர்தல் தேவையில்லை. நாடாளுமன்றம் மற்றும் சட்டமன்றங்களுக்கும் RPA 1951 பிரிவு 151A-ன் கீழ் இதே விதி பொருந்தும்.",
            "fact_en": "A local body reconstituted after premature dissolution continues only for the remainder of the original five-year period.",
            "fact_ta": "காலத்திற்கு முன்பே கலைக்கப்பட்டு மீண்டும் அமைக்கப்படும் உள்ளாட்சி அமைப்பு அசல் ஐந்து ஆண்டு காலத்தின் மீதமுள்ள காலத்திற்கு மட்டுமே நீடிக்கும்."
        },

        # 39. e-GramSwaraj and PRIA Soft - Local Body Fiscal Accountability
        {
            "subtopic": "Financial Devolution, Intergovernmental Transfers & Local Governance",
            "stem_en": "What role do national digital platforms like e-GramSwaraj and AuditOnline play in the disbursement of Finance Commission grants to local bodies?",
            "stem_ta": "உள்ளாட்சி அமைப்புகளுக்கு நிதி ஆணைய மானியங்களை வழங்குவதில் e-GramSwaraj மற்றும் AuditOnline போன்ற தேசிய டிஜிட்டல் தளங்கள் என்ன பங்கு வகிக்கின்றன?",
            "options": [
                ("They mandate transparent digital planning, voucher-level accounting, and online audit compliance as prerequisites before Central and State grants are released", "மத்திய மற்றும் மாநில மானியங்கள் வழங்கப்படுவதற்கு முன் வெளிப்படையான டிஜிட்டல் திட்டமிடல், கணக்கு பராமரிப்பு மற்றும் ஆன்லைன் தணிக்கை இணக்கத்தை முன்நிபந்தனைகளாக கட்டாயப்படுத்துகின்றன"),
                ("They automatically delete all municipal records every 30 days to save cloud server storage", "கிளவுட் சேமிப்பிடத்தை சேமிப்பதற்காக ஒவ்வொரு 30 நாட்களுக்கும் அனைத்து நகராட்சி பதிவுகளையும் தானாகவே நீக்குகின்றன"),
                ("They replace all elected Panchayat Ward Members with artificial intelligence robots", "அனைத்து தேர்ந்தெடுக்கப்பட்ட பஞ்சாயத்து வார்டு உறுப்பினர்களையும் செயற்கை நுண்ணறிவு ரோபோக்களால் மாற்றுகின்றன"),
                ("They permit local bodies to trade cryptocurrency tokens directly on foreign exchanges", "உள்ளாட்சி அமைப்புகள் வெளிநாட்டு பரிமாற்றங்களில் கிரிப்டோகரன்சியை நேரடியாக வர்த்தகம் செய்ய அனுமதிக்கின்றன")
            ],
            "correct_key": "A",
            "exp_en": "Under reforms mandated by the Ministry of Panchayati Raj and the 15th Finance Commission, local bodies must upload approved Panchayat Development Plans (GPDP) on e-GramSwaraj, maintain double-entry cash accounting on PRIA Soft, and undergo online audit on AuditOnline to become eligible for grant releases.",
            "exp_ta": "பஞ்சாயத்து ராஜ் அமைச்சகம் மற்றும் 15வது நிதி ஆணையத்தால் கட்டாயமாக்கப்பட்ட சீர்திருத்தங்களின் கீழ், உள்ளாட்சி அமைப்புகள் அங்கீகரிக்கப்பட்ட வளர்ச்சித் திட்டங்களை (GPDP) e-GramSwaraj-ல் பதிவேற்ற வேண்டும், PRIA Soft-ல் கணக்குகளை பராமரிக்க வேண்டும் மற்றும் மானியங்களை பெற AuditOnline-ல் ஆன்லைன் தணிக்கைக்கு உட்பட வேண்டும்.",
            "why_a_en": "Correct. Digital accounting and online auditing are mandatory conditions for fund release.",
            "why_a_ta": "சரி. டிஜிட்டல் கணக்கு பராமரிப்பு மற்றும் ஆன்லைன் தணிக்கை ஆகியவை நிதி வெளியீட்டிற்கான கட்டாய நிபந்தனைகளாகும்.",
            "why_b_en": "Incorrect. Digital records are preserved permanently as permanent public audit trails.",
            "why_b_ta": "தவறு. டிஜிட்டல் பதிவுகள் நிரந்தர பொதுத் தணிக்கை தடங்களாகப் பாதுகாக்கப்படுகின்றன.",
            "why_c_en": "Incorrect. Digital tools assist democratic representatives; they do not replace them.",
            "why_c_ta": "தவறு. டிஜிட்டல் கருவிகள் ஜனநாயக பிரதிநிதிகளுக்கு உதவுகின்றன, அவர்களை மாற்றுவதில்லை.",
            "why_d_en": "Incorrect. Speculative cryptocurrency trading with public funds is prohibited.",
            "why_d_ta": "தவறு. பொது நிதியைப் பயன்படுத்தி கிரிப்டோகரன்சி வர்த்தகம் செய்வது தடைசெய்யப்பட்டுள்ளது.",
            "tip_en": "15th FC tie-in: Untied and Tied grants require online upload of GPDP and audited accounts on AuditOnline.",
            "tip_ta": "15வது FC இணைப்பு: கட்டுப்பாடற்ற மற்றும் நிபந்தனை மானியங்கள் GPDP மற்றும் தணிக்கை செய்யப்பட்ட கணக்குகளை இணையத்தில் பதிவேற்ற வேண்டும்.",
            "fact_en": "Tamil Nadu has achieved near 100% onboarding of Village Panchayats onto the e-GramSwaraj portal.",
            "fact_ta": "தமிழ்நாடு கிராம பஞ்சாயத்துகளை e-GramSwaraj இணையதளத்தில் இணைப்பதில் கிட்டத்தட்ட 100% வெற்றியை எட்டியுள்ளது."
        },

        # 40. District Planning Committee Interlinkage (Article 243ZD)
        {
            "subtopic": "State Finance Commission - Constitutional Mandate, Composition & Role (Articles 243I & 243Y)",
            "stem_en": "How do the fiscal recommendations of the State Finance Commission support the functions of the District Planning Committee (DPC) constituted under Article 243ZD?",
            "stem_ta": "சரத்து 243ZD-ன் கீழ் அமைக்கப்பட்ட மாவட்ட திட்டக் குழுவின் (DPC) பணிகளுக்கு மாநில நிதி ஆணையத்தின் நிதிப் பரிந்துரைகள் எவ்வாறு ஆதரவளிக்கின்றன?",
            "options": [
                ("By providing predictable financial allocations enabling the DPC to consolidate rural and urban local plans into a coherent draft development plan for the entire district", "முழு மாவட்டத்திற்கும் ஊரக மற்றும் நகர்ப்புற திட்டங்களை ஒரு ஒருங்கிணைந்த வரைவு வளர்ச்சித் திட்டமாக ஒருங்கிணைக்க DPC-க்கு கணிக்கக்கூடிய நிதி ஒதுக்கீடுகளை வழங்குவதன் மூலம்"),
                ("By abolishing the District Planning Committee and transferring all its powers to the Union Planning Commission", "மாவட்ட திட்டக் குழுவை ஒழித்து அதன் அனைத்து அதிகாரங்களையும் மத்திய திட்டக் குழுவிற்கு மாற்றுவதன் மூலம்"),
                ("By directing that 100% of all district infrastructure funds must be spent exclusively on private golf resorts", "அனைத்து மாவட்ட உள்கட்டமைப்பு நிதியில் 100% தனியார் கோல்ஃப் ஓய்வு விடுதிகளுக்கு மட்டுமே செலவிடப்பட வேண்டும் என்று உத்தரவிடுவதன் மூலம்"),
                ("By preventing urban municipalities from coordinating with adjacent rural panchayats", "நகர்ப்புற நகராட்சிகள் அருகிலுள்ள கிராம பஞ்சாயத்துகளுடன் ஒருங்கிணைப்பதைத் தடுப்பதன் மூலம்")
            ],
            "correct_key": "A",
            "exp_en": "Article 243ZD mandates a District Planning Committee (DPC) in every district to consolidate the plans prepared by the Panchayats and Municipalities. SFC fund allocations provide the fiscal certainty and resource envelope necessary for the DPC to prepare a realistic draft development plan for the district.",
            "exp_ta": "சரத்து 243ZD பஞ்சாயத்துகள் மற்றும் நகராட்சிகளால் தயாரிக்கப்பட்ட திட்டங்களை ஒருங்கிணைக்க ஒவ்வொரு மாவட்டத்திலும் ஒரு மாவட்ட திட்டக் குழுவை (DPC) கட்டாயப்படுத்துகிறது. SFC நிதி ஒதுக்கீடுகள், மாவட்டத்திற்கான யதார்த்தமான வரைவு வளர்ச்சித் திட்டத்தைத் தயாரிக்க DPC-க்குத் தேவையான நிதி நிச்சயத்தன்மையை வழங்குகின்றன.",
            "why_a_en": "Correct. SFC allocations provide the financial foundation for DPC district development plans.",
            "why_a_ta": "சரி. SFC ஒதுக்கீடுகள் DPC மாவட்ட வளர்ச்சித் திட்டங்களுக்கான நிதி அடித்தளத்தை வழங்குகின்றன.",
            "why_b_en": "Incorrect. SFC cannot abolish constitutional bodies like DPC.",
            "why_b_ta": "தவறு. DPC போன்ற அரசியலமைப்பு அமைப்புகளை SFC ஒழிக்க முடியாது.",
            "why_c_en": "Incorrect. Public funds are dedicated to core civic amenities, not private golf resorts.",
            "why_c_ta": "தவறு. பொது நிதி அடிப்படை குடிமை வசதிகளுக்குப் பயன்படுத்தப்படுகிறது, தனியார் விடுதிகளுக்கு அல்ல.",
            "why_d_en": "Incorrect. Article 243ZD is specifically designed to harmonize rural-urban planning.",
            "why_d_ta": "தவறு. சரத்து 243ZD குறிப்பாக கிராமப்புற-நகர்ப்புற திட்டமிடலை ஒருங்கிணைக்க வடிவமைக்கப்பட்டுள்ளது.",
            "tip_en": "DPC under Article 243ZD consolidates plans from Panchayats (Art 243G) and Municipalities (Art 243W).",
            "tip_ta": "சரத்து 243ZD-ன் கீழ் DPC பஞ்சாயத்துகள் (சரத்து 243G) மற்றும் நகராட்சிகளின் (சரத்து 243W) திட்டங்களை ஒருங்கிணைக்கிறது.",
            "fact_en": "In Tamil Nadu, the District Collector functions as the Member-Secretary, and the District Panchayat Chairman functions as the Chairman of the DPC.",
            "fact_ta": "தமிழ்நாட்டில், மாவட்ட ஆட்சியர் உறுப்பினர்-செயலாளராகவும், மாவட்ட பஞ்சாயத்து தலைவர் DPC-ன் தலைவராகவும் செயல்படுகின்றனர்."
        },

        # 41. Electronic Voting Machines (EVMs) in Local Elections
        {
            "subtopic": "State Election Commission - Constitutional Mandate & Provisions (Articles 243K & 243ZA)",
            "stem_en": "Under which authority can the State Election Commission introduce and deploy Electronic Voting Machines (EVMs) for local body elections?",
            "stem_ta": "எந்த அதிகாரத்தின் கீழ் மாநில தேர்தல் ஆணையம் உள்ளாட்சித் தேர்தல்களுக்கு மின்னணு வாக்குப்பதிவு இயந்திரங்களை (EVM) அறிமுகப்படுத்தி பயன்படுத்த முடியும்?",
            "options": [
                ("Pursuant to statutory amendments in the State Municipal and Panchayat Acts read with plenary powers under Articles 243K and 243ZA", "சரத்துகள் 243K மற்றும் 243ZA-ன் கீழ் உள்ள முழுமையான அதிகாரங்களுடன் இணைந்த மாநில நகராட்சி மற்றும் பஞ்சாயத்து சட்டங்களின் சட்டப்பூர்வ திருத்தங்களின்படி"),
                ("Only with the unanimous written permission of the President of the United States", "அமெரிக்க அதிபரின் ஒருமனதான எழுத்துப்பூர்வ அனுமதியுடன் மட்டுமே"),
                ("Only if every individual voter passes a mandatory written computer engineering exam", "ஒவ்வொரு தனிப்பட்ட வாக்காளரும் கட்டாய கணினி பொறியியல் எழுத்துத் தேர்வில் தேர்ச்சி பெற்றால் மட்டுமே"),
                ("Deploying EVMs in local body elections is strictly unconstitutional and punishable under criminal law", "உள்ளாட்சித் தேர்தல்களில் EVM-களைப் பயன்படுத்துவது முற்றிலும் அரசியலமைப்பிற்கு முரணானது மற்றும் தண்டனைக்குரியது")
            ],
            "correct_key": "A",
            "exp_en": "State Legislatures enacted enabling amendments to state election laws (e.g. TN Panchayats and Municipalities Acts) authorizing the use of Electronic Voting Machines. Together with the plenary powers of superintendence under Art 243K/243ZA, the SEC regulates the procurement, testing, and deployment of multi-post EVMs.",
            "exp_ta": "மின்னணு வாக்குப்பதிவு இயந்திரங்களைப் பயன்படுத்துவதை அங்கீகரிக்கும் வகையில் மாநில சட்டமன்றங்கள் தேர்தல் சட்டங்களில் திருத்தங்களை இயற்றின. சரத்து 243K/243ZA-ன் கீழ் உள்ள முழுமையான அதிகாரங்களுடன் இணைந்து, SEC பல பதவி EVM-களை வாங்குதல், சோதித்தல் மற்றும் பயன்படுத்துவதை ஒழுங்குபடுத்துகிறது.",
            "why_a_en": "Correct. Enabling provisions in state acts and 243K/243ZA authorize EVM usage.",
            "why_a_ta": "சரி. மாநில சட்டங்கள் மற்றும் 243K/243ZA ஆகியவற்றில் உள்ள விதிகள் EVM பயன்பாட்டை அங்கீகரிக்கின்றன.",
            "why_b_en": "Incorrect. Foreign officials have no legal standing in Indian elections.",
            "why_b_ta": "தவறு. இந்திய தேர்தல்களில் வெளிநாட்டு அதிகாரிகளுக்கு எந்த சட்டப்பூர்வ அந்தஸ்தும் இல்லை.",
            "why_c_en": "Incorrect. Universal adult suffrage guarantees voting without literacy or technical tests.",
            "why_c_ta": "தவறு. வயதுவந்தோர் வாக்குரிமை எழுத்தறிவு அல்லது தொழில்நுட்ப சோதனைகள் இன்றி வாக்களிப்பதை உறுதி செய்கிறது.",
            "why_d_en": "Incorrect. EVM use has been repeatedly upheld as valid by the Supreme Court.",
            "why_d_ta": "தவறு. EVM பயன்பாடு உச்ச நீதிமன்றத்தால் மீண்டும் மீண்டும் செல்லுபடியாகும் என உறுதி செய்யப்பட்டுள்ளது.",
            "tip_en": "EVMs are widely used in urban local bodies (Corporations, Municipalities) across Tamil Nadu.",
            "tip_ta": "தமிழ்நாடு முழுவதும் உள்ள நகர்ப்புற உள்ளாட்சி அமைப்புகளில் (மாநகராட்சிகள், நகராட்சிகள்) EVM-கள் பரவலாகப் பயன்படுத்தப்படுகின்றன.",
            "fact_en": "For multi-post rural panchayat elections, paper ballots of different colors are still commonly deployed due to multiple simultaneous ballots (ward, president, union, district).",
            "fact_ta": "ஊரகப் பஞ்சாயத்துத் தேர்தல்களில் பல பதவிகள் இருப்பதால் (வார்டு, தலைவர், ஒன்றியம், மாவட்டம்), வெவ்வேறு வண்ணங்களைக் கொண்ட காகித வாக்குச் சீட்டுகள் பயன்படுத்தப்படுகின்றன."
        },

        # 42. Article 243-O Bar on Injunctions Against Returning Officers
        {
            "subtopic": "State Election Commission - Constitutional Mandate & Provisions (Articles 243K & 243ZA)",
            "stem_en": "What was the ruling in NP Ponnuswami v. Returning Officer (1952), which serves as the foundational precedent for local body elections under Article 243-O?",
            "stem_ta": "சரத்து 243-O-ன் கீழ் உள்ளாட்சித் தேர்தல்களுக்கு அடிப்படை முன்மாதிரியாக விளங்கும் என்.பி. பொன்னுசாமி எதிர் தேர்தல் நடத்தும் அதிகாரி (1952) வழக்கின் தீர்ப்பு என்ன?",
            "options": [
                ("The word 'election' encompasses the entire continuous process from notification to declaration of result, and courts cannot interrupt it midway by entertaining writ petitions against rejection of nomination papers", "'தேர்தல்' என்ற சொல் அறிவிப்பு முதல் முடிவுகள் அறிவிக்கப்படும் வரை உள்ள முழு தொடர்ச்சியான செயல்முறையையும் உள்ளடக்கியது, மேலும் வேட்புமனு நிராகரிப்புக்கு எதிரான மனுக்களை விசாரித்து நீதிமன்றங்கள் அதை நடுவழியில் குறுக்கிட முடியாது"),
                ("Returning officers can be personally arrested on the spot by any candidate who feels dissatisfied with the ballot paper color", "வாக்குச் சீட்டின் நிறத்தில் அதிருப்தி அடையும் எந்தவொரு வேட்பாளராலும் தேர்தல் நடத்தும் அதிகாரிகளை அந்த இடத்திலேயே கைது செய்ய முடியும்"),
                ("Elections must be cancelled if a candidate fails to score 100% of the total registered votes", "ஒரு வேட்பாளர் பதிவு செய்யப்பட்ட மொத்த வாக்குகளில் 100% பெறத் தவறினால் தேர்தலை ரத்து செய்ய வேண்டும்"),
                ("Only the Prime Minister can accept or reject nomination papers of local councillors", "உள்ளாட்சி கவுன்சிலர்களின் வேட்புமனுக்களை பிரதமரால் மட்டுமே ஏற்றுக்கொள்ளவோ அல்லது நிராகரிக்கவோ முடியும்")
            ],
            "correct_key": "A",
            "exp_en": "In N.P. Ponnuswami (1952), the SC established that 'election' in Article 329(b) [and identically in Article 243-O(b)] covers the entire gamut of polling from notification to declaration of results. No writ petition lies to stall or challenge nomination rejection midway; the sole remedy is an Election Petition after the results.",
            "exp_ta": "என்.பி. பொன்னுசாமி (1952) வழக்கில், சரத்து 329(b) [மற்றும் சரத்து 243-O(b)]-ல் உள்ள 'தேர்தல்' என்பது அறிவிப்பு முதல் முடிவு அறிவிப்பு வரை உள்ள முழு செயல்முறையையும் குறிக்கிறது என்று உச்ச நீதிமன்றம் நிறுவியது. நடுவழியில் வேட்புமனு நிராகரிப்பை எதிர்க்க நீதிப்பேராணை தாக்கல் செய்ய முடியாது; முடிவுகளுக்குப் பின் தேர்தல் மனுவே ஒரே தீர்வாகும்.",
            "why_a_en": "Correct. Landmark precedent establishing that 'election' is an indivisible, uninterrupted process.",
            "why_a_ta": "சரி. 'தேர்தல்' என்பது பிரிக்க முடியாத, தடையற்ற செயல்முறை என்பதை நிறுவிய வரலாற்றுச் சிறப்புமிக்க தீர்ப்பு.",
            "why_b_en": "Incorrect. Returning Officers are public servants acting with statutory immunity.",
            "why_b_ta": "தவறு. தேர்தல் நடத்தும் அதிகாரிகள் சட்டப்பூர்வ பாதுகாப்புடன் செயல்படும் அரசு ஊழியர்கள்.",
            "why_c_en": "Incorrect. First-Past-The-Post system requires only a plurality of votes.",
            "why_c_ta": "தவறு. முதலில் வந்தவருக்கு வெற்றி என்ற முறையில் அதிக வாக்குகள் பெற்றாலே போதுமானது.",
            "why_d_en": "Incorrect. Returning Officers statutory jurisdiction cannot be assumed by the Prime Minister.",
            "why_d_ta": "தவறு. தேர்தல் நடத்தும் அதிகாரியின் சட்டப்பூர்வ அதிகாரத்தை பிரதமரால் ஏற்க முடியாது.",
            "tip_en": "Ponnuswami principle (1952): Rejection of nomination paper CANNOT be challenged via writ under 226 midway; MUST wait for Election Petition.",
            "tip_ta": "பொன்னுசாமி கொள்கை (1952): வேட்புமனு நிராகரிப்பை நடுவழியில் 226-ன் கீழ் எதிர்க்க முடியாது; தேர்தல் மனு வரை காத்திருக்க வேண்டும்.",
            "fact_en": "N.P. Ponnuswami originated from Namakkal constituency in Tamil Nadu (then Madras State).",
            "fact_ta": "என்.பி. பொன்னுசாமி வழக்கு தமிழ்நாட்டின் நாமக்கல் தொகுதியிலிருந்து (அப்போதைய மெட்ராஸ் மாகாணம்) உருவானது."
        },

        # 43. Fiscal Equalization Grant Principle
        {
            "subtopic": "Financial Devolution, Intergovernmental Transfers & Local Governance",
            "stem_en": "What is the primary objective of a 'Fiscal Equalization Grant' recommended by a State Finance Commission?",
            "stem_ta": "மாநில நிதி ஆணையத்தால் பரிந்துரைக்கப்படும் 'நிதி சமன்பாட்டு மானியத்தின்' (Fiscal Equalization Grant) முதன்மை நோக்கம் என்ன?",
            "options": [
                ("To bridge the horizontal fiscal disparities among local bodies so that economically disadvantaged panchayats can provide standard public services at comparable tax rates", "பொருளாதார ரீதியாக பின்தங்கிய பஞ்சாயத்துகள் ஒப்பிடக்கூடிய வரி விகிதங்களில் நிலையான பொதுச் சேவைகளை வழங்கக்கூடிய வகையில் உள்ளாட்சி அமைப்புகளுக்கு இடையிலான நிதி ஏற்றத்தாழ்வுகளைக் குறைக்க"),
                ("To make all rich urban corporations surrender 100% of their revenues to the state sports department", "அனைத்து பணக்கார நகர்ப்புற மாநகராட்சிகளும் தங்கள் வருவாயில் 100% மாநில விளையாட்டுத் துறைக்கு ஒப்படைக்கச் செய்ய"),
                ("To ensure that all municipal councillors receive identical foreign luxury vehicles", "அனைத்து நகராட்சி கவுன்சிலர்களும் ஒரே மாதிரியான வெளிநாட்டு சொகுசு வாகனங்களைப் பெறுவதை உறுதி செய்ய"),
                ("To fund election campaigns of candidates contesting in parliamentary general elections", "நாடாளுமன்ற பொதுத் தேர்தல்களில் போட்டியிடும் வேட்பாளர்களின் தேர்தல் பிரச்சாரங்களுக்கு நிதி அளிக்க")
            ],
            "correct_key": "A",
            "exp_en": "Fiscal equalization grants aim to offset horizontal imbalances caused by disparities in local tax base capacity and differing expenditure needs (e.g. hilly terrain, sparse population), ensuring that citizens in backward or remote local bodies enjoy a constitutionally guaranteed minimum standard of public amenities.",
            "exp_ta": "நிதி சமன்பாட்டு மானியங்கள், உள்ளூர் வரி அடிப்படை திறன் மற்றும் மாறுபட்ட செலவுத் தேவைகளில் (எ.கா. மலைப்பாங்கான பகுதி, குறைந்த மக்கள் தொகை) ஏற்படும் ஏற்றத்தாழ்வுகளை ஈடுசெய்வதை நோக்கமாகக் கொண்டுள்ளன, இதன் மூலம் பின்தங்கிய பகுதிகளில் உள்ள குடிமக்களும் குறைந்தபட்ச தரமான பொது வசதிகளைப் பெறுவதை உறுதி செய்கின்றன.",
            "why_a_en": "Correct. Equalization ensures equitable basic services regardless of local fiscal wealth.",
            "why_a_ta": "சரி. சமன்பாட்டு மானியம் உள்ளூர் நிதி வசதியைப் பொருட்படுத்தாமல் சமமான அடிப்படைச் சேவைகளை உறுதி செய்கிறது.",
            "why_b_en": "Incorrect. Rich corporations retain their revenue base subject to formula sharing.",
            "why_b_ta": "தவறு. பணக்கார மாநகராட்சிகள் சூத்திரப் பகிர்வுக்கு உட்பட்டு தங்கள் வருவாய் அடிப்படையைத் தக்க வைத்துக் கொள்கின்றன.",
            "why_c_en": "Incorrect. Funds are not spent on private luxury vehicles.",
            "why_c_ta": "தவறு. ஆடம்பர வாகனங்களுக்கு நிதி செலவிடப்படுவதில்லை.",
            "why_d_en": "Incorrect. Public equalization funds cannot finance partisan election campaigns.",
            "why_d_ta": "தவறு. பொது சமன்பாட்டு நிதியைக் கொண்டு கட்சித் தேர்தல் பிரச்சாரங்களுக்கு நிதி அளிக்க முடியாது.",
            "tip_en": "Equalization = Equity principle in fiscal federalism (compensating for structural cost disadvantages).",
            "tip_ta": "சமன்பாடு = நிதி கூட்டாட்சியில் சமத்துவக் கொள்கை (கட்டமைப்புச் செலவு குறைபாடுகளை ஈடுசெய்தல்).",
            "fact_en": "Tamil Nadu uses a per-capita deficit grant to support village panchayats having meager house-tax revenues.",
            "fact_ta": "தமிழ்நாடு மிகக் குறைந்த வீட்டு வரி வருவாய் கொண்ட கிராம பஞ்சாயத்துகளை ஆதரிக்க தனிநபர் பற்றாக்குறை மானியத்தைப் பயன்படுத்துகிறது."
        },

        # 44. Section 205 Removal of Panchayat President in Tamil Nadu
        {
            "subtopic": "Tamil Nadu State Election & Finance Commissions - Legal Framework, Rules & Precedents",
            "stem_en": "Under Section 205 of the Tamil Nadu Panchayats Act 1994, what procedure is mandated before the Inspector of Panchayats (District Collector) can remove a Village Panchayat President for misconduct?",
            "stem_ta": "1994 தமிழ்நாடு பஞ்சாயத்துகள் சட்டத்தின் பிரிவு 205-ன் கீழ், தவறான நடத்தைக்காக கிராம பஞ்சாயத்து தலைவரை பஞ்சாயத்து ஆய்வாளர் (மாவட்ட ஆட்சியர்) பதவி நீக்கம் செய்வதற்கு முன் என்ன நடைமுறை கட்டாயமாக்கப்பட்டுள்ளது?",
            "options": [
                ("Issuing a show-cause notice, obtaining the views of the Village Panchayat in a specially convened meeting, and publishing an official gazette notification stating grounds", "விளக்கம் கேட்கும் நோட்டீஸ் வழங்குதல், சிறப்பாகக் கூட்டப்பட்ட கூட்டத்தில் கிராம பஞ்சாயத்தின் கருத்துக்களைப் பெறுதல் மற்றும் காரணங்களைக் கூறி அரசிதழில் அதிகாரப்பூர்வ அறிவிப்பை வெளியிடுதல்"),
                ("Immediate arbitrary termination via telephone call without recording any written reasons", "எந்தவொரு எழுத்துப்பூர்வ காரணங்களையும் பதிவு செய்யாமல் தொலைபேசி அழைப்பு மூலம் உடனடியாக தன்னிச்சையாக பதவி நீக்கம் செய்தல்"),
                ("Directly lodging the President in central prison without providing any opportunity to explain", "விளக்கமளிக்க எந்த வாய்ப்பும் வழங்காமல் தலைவரை நேரடியாக மத்திய சிறையில் அடைத்தல்"),
                ("Securing prior approval from the Governor and Union Home Minister", "ஆளுநர் மற்றும் மத்திய உள்துறை அமைச்சரிடம் முன் அனுமதி பெறுதல்")
            ],
            "correct_key": "A",
            "exp_en": "Section 205 of the TN Panchayats Act mandates a strict quasi-judicial procedure: the Collector issues a show-cause notice, places the explanation before the Village Panchayat at a special meeting presided over by the Tahsildar to record their views, and if satisfied of misconduct, issues a notification of removal in the District Gazette.",
            "exp_ta": "TN பஞ்சாயத்துகள் சட்டத்தின் பிரிவு 205 ஒரு கடுமையான நீதித்துறை போன்ற நடைமுறையை கட்டாயப்படுத்துகிறது: ஆட்சியர் விளக்கம் கேட்கும் நோட்டீஸ் வழங்குகிறார், வட்டாட்சியர் தலைமையில் நடைபெறும் சிறப்புக் கூட்டத்தில் கிராம பஞ்சாயத்தின் முன் விளக்கத்தை வைத்து அதன் கருத்துக்களைப் பதிவு செய்கிறார், மற்றும் தவறான நடத்தை நிரூபிக்கப்பட்டால் மாவட்ட அரசிதழில் பதவி நீக்க அறிவிப்பை வெளியிடுகிறார்.",
            "why_a_en": "Correct. Natural justice, recording views of panchayat, and gazette notification are mandatory under Sec 205.",
            "why_a_ta": "சரி. இயற்கை நீதி, பஞ்சாயத்தின் கருத்துக்களைப் பதிவு செய்தல் மற்றும் அரசிதழ் அறிவிப்பு ஆகியவை பிரிவு 205-ன் கீழ் கட்டாயமாகும்.",
            "why_b_en": "Incorrect. Unreasoned telephone termination violates Section 205 and Article 14.",
            "why_b_ta": "தவறு. காரணமற்ற தொலைபேசி நீக்கம் பிரிவு 205 மற்றும் சரத்து 14-ஐ மீறுகிறது.",
            "why_c_en": "Incorrect. S. 205 is an administrative removal process, not summary imprisonment.",
            "why_c_ta": "தவறு. பிரிவு 205 என்பது ஒரு நிர்வாக பதவி நீக்க செயல்முறை, சிறைத்தண்டனை அல்ல.",
            "why_d_en": "Incorrect. Governor or Union Home Minister approval is not required.",
            "why_d_ta": "தவறு. ஆளுநர் அல்லது மத்திய உள்துறை அமைச்சரின் ஒப்புதல் தேவையில்லை.",
            "tip_en": "Sec 205 removal requires: Notice -> Views of Panchayat (Tahsildar meeting) -> Gazette notification.",
            "tip_ta": "பிரிவு 205 பதவி நீக்கத்திற்கு தேவை: நோட்டீஸ் -> பஞ்சாயத்தின் கருத்துக்கள் (வட்டாட்சியர் கூட்டம்) -> அரசிதழ் அறிவிப்பு.",
            "fact_en": "An appeal against the Collector's removal order lies to the State Government under Section 205(12).",
            "fact_ta": "ஆட்சியரின் பதவி நீக்க உத்தரவுக்கு எதிரான மேல்முறையீடு பிரிவு 205(12)-ன் கீழ் மாநில அரசிடம் செய்யப்படலாம்."
        },

        # 45. Multi-Member Delimitation and Boundary Disputes
        {
            "subtopic": "State Election Commission - Constitutional Mandate & Provisions (Articles 243K & 243ZA)",
            "stem_en": "When a local body delimitation notification is challenged, on what grounds alone have Constitutional Courts historically entertained judicial scrutiny, despite Article 243-O(a)?",
            "stem_ta": "உள்ளாட்சி எல்லை மறுவரையறை அறிவிப்பு சவால் செய்யப்படும் போது, சரத்து 243-O(a) இருந்தபோதிலும், எந்த அடிப்படையில் மட்டுமே அரசியலமைப்பு நீதிமன்றங்கள் வரலாற்று ரீதியாக நீதித்துறை ஆய்வை அனுமதித்துள்ளன?",
            "options": [
                ("Gross violation of statutory mandatory rules, complete non-adherence to basic principles of natural justice, or blatant mala fide gerrymandering prior to election notification", "சட்டப்பூர்வ கட்டாய விதிகளை கடுமையாக மீறுதல், இயற்கை நீதியின் அடிப்படைக் கொள்கைகளை முழுமையாகப் பின்பற்றாமை அல்லது தேர்தல் அறிவிப்புக்கு முன் அப்பட்டமான உள்நோக்கத்துடன் கூடிய எல்லை மாற்றம்"),
                ("Dislike of the newly allotted ward numbers by individual candidates", "தனிப்பட்ட வேட்பாளர்கள் புதிதாக ஒதுக்கப்பட்ட வார்டு எண்களை விரும்பாததால்"),
                ("Because the candidate prefers a smaller geographical ward to walk fewer kilometers during campaign", "பிரச்சாரத்தின் போது குறைந்த தூரம் நடக்க வேட்பாளர் ஒரு சிறிய புவியியல் வார்டை விரும்புவதால்"),
                ("Because the delimitation committee did not provide complimentary meals to all ward electors", "மறுவரையறை குழு அனைத்து வார்டு வாக்காளர்களுக்கும் இலவச உணவு வழங்காததால்")
            ],
            "correct_key": "A",
            "exp_en": "While Article 243-O(a) bars questioning delimitation laws, courts (e.g. Dravida Munnetra Kazhagam v. State of TN, 2020) have held that pre-election judicial review is strictly confined to total non-compliance with statutory delimitation rules (e.g., failure to rotate reserved seats, total disregard of population quota) prior to formal issuance of election notification.",
            "exp_ta": "சரத்து 243-O(a) மறுவரையறை சட்டங்களை கேள்வி கேட்பதைத் தடை செய்தாலும், தேர்தல் அறிவிப்பு அதிகாரப்பூர்வமாக வெளியிடப்படுவதற்கு முன்பு சட்டப்பூர்வ மறுவரையறை விதிகளை முற்றிலும் பின்பற்றாத போது (எ.கா. சுழற்சி முறையைப் பின்பற்றாமை) மட்டுமே நீதித்துறை மறுஆய்வு செய்யப்படலாம் என்று நீதிமன்றங்கள் தீர்ப்பளித்துள்ளன.",
            "why_a_en": "Correct. Severe statutory violations or mala fides prior to notification allow limited judicial scrutiny.",
            "why_a_ta": "சரி. தேர்தல் அறிவிப்புக்கு முந்தைய கடுமையான சட்ட மீறல்கள் அல்லது தவறான எண்ணம் வரையறுக்கப்பட்ட நீதித்துறை ஆய்வை அனுமதிக்கிறது.",
            "why_b_en": "Incorrect. Subjective dislike of ward numbers is not a legal ground.",
            "why_b_ta": "தவறு. வார்டு எண்களை தனிப்பட்ட முறையில் விரும்பாமை ஒரு சட்டப்பூர்வ காரணம் அல்ல.",
            "why_c_en": "Incorrect. Campaign convenience cannot dictate constitutional boundary demarcations.",
            "why_c_ta": "தவறு. பிரச்சார வசதிக்காக அரசியலமைப்பு எல்லைகளை மாற்ற முடியாது.",
            "why_d_en": "Incorrect. Free meals have no connection to delimitation jurisprudence.",
            "why_d_ta": "தவறு. இலவச உணவுகளுக்கும் எல்லை மறுவரையறை நீதித்துறைக்கும் எந்த தொடர்பும் இல்லை.",
            "tip_en": "Once election notification is officially issued, the bar under 243-O becomes absolute and total.",
            "tip_ta": "தேர்தல் அறிவிப்பு அதிகாரப்பூர்வமாக வெளியிடப்பட்டவுடன், 243-O-ன் கீழான தடை முழுமையானதாக மாறுகிறது.",
            "fact_en": "In DMK v. State of TN (2019-20), the Supreme Court allowed rural local body elections to proceed while directing completion of delimitation in nine newly reconstituted districts.",
            "fact_ta": "திமுக எதிர் தமிழ்நாடு அரசு (2019-20) வழக்கில், ஒன்பது புதிய மாவட்டங்களில் மறுவரையறையை முடிக்க உத்தரவிட்ட உச்ச நீதிமன்றம், மற்ற மாவட்டங்களில் ஊரக உள்ளாட்சித் தேர்தல்களை நடத்த அனுமதித்தது."
        },

        # 46. Financial Autonomy vs State Control of Panchayats
        {
            "subtopic": "Financial Devolution, Intergovernmental Transfers & Local Governance",
            "stem_en": "Which structural reform has been consistently advocated by the Second Administrative Reforms Commission (2nd ARC) to enhance the genuine fiscal autonomy of local bodies?",
            "stem_ta": "உள்ளாட்சி அமைப்புகளின் உண்மையான நிதி சுயாட்சியை மேம்படுத்த இரண்டாவது நிர்வாக சீர்திருத்த ஆணையம் (2nd ARC) தொடர்ந்து பரிந்துரைத்த கட்டமைப்பு சீர்திருத்தம் எது?",
            "options": [
                ("Activity Mapping (clear demarcation of Funds, Functions, and Functionaries among the three tiers) to eliminate overlapping and unfunded mandates", "அடுக்குகளுக்கு இடையே மேலெழுதல் மற்றும் நிதியற்ற கட்டளைகளை அகற்ற 'செயல்பாட்டு வரைபடம்' (மூன்று அடுக்குகளிடையே நிதி, பணிகள் மற்றும் பணியாளர்களை தெளிவாக வரையறுத்தல்)"),
                ("Complete abolition of all local self-government institutions and return to British colonial collectorate rule", "அனைத்து உள்ளாட்சி அமைப்புகளையும் முற்றிலும் ஒழித்து, பிரிட்டிஷ் காலனித்துவ ஆட்சியர் ஆட்சிக்குத் திரும்புதல்"),
                ("Directing local bodies to generate 100% of their annual expenditure exclusively from lotteries", "உள்ளாட்சி அமைப்புகள் தங்கள் வருடாந்திர செலவினங்களில் 100% லாட்டரி மூலம் மட்டுமே ஈட்ட வேண்டும் என்று உத்தரவிடுதல்"),
                ("Banning local bodies from maintaining any bank accounts or written accounting registers", "உள்ளாட்சி அமைப்புகள் எந்தவொரு வங்கிக் கணக்குகளையும் அல்லது கணக்குப் பதிவேடுகளையும் பராமரிக்கத் தடை விதித்தல்")
            ],
            "correct_key": "A",
            "exp_en": "The 2nd Administrative Reforms Commission (6th Report, 'Local Governance') strongly emphasized 'Activity Mapping' based on the principle of subsidiarity, demarcating exactly which functions, functionaries, and funds belong to Village Panchayats, Panchayat Unions, and District Panchayats to prevent administrative encroachment.",
            "exp_ta": "இரண்டாவது நிர்வாக சீர்திருத்த ஆணையம் (6வது அறிக்கை, 'உள்ளாட்சி நிர்வாகம்') கிராம பஞ்சாயத்துகள், பஞ்சாயத்து ஒன்றியங்கள் மற்றும் மாவட்ட பஞ்சாயத்துகளுக்கு எந்தெந்த பணிகள், பணியாளர்கள் மற்றும் நிதி சொந்தமானது என்பதை தெளிவாக வரையறுக்கும் 'செயல்பாட்டு வரைபடத்தை' (Activity Mapping) கடுமையாக வலியுறுத்தியது.",
            "why_a_en": "Correct. Activity Mapping of Funds, Functions, and Functionaries is the cornerstone of 2nd ARC recommendations.",
            "why_a_ta": "சரி. நிதி, பணிகள் மற்றும் பணியாளர்களின் செயல்பாட்டு வரைபடம் 2வது ARC பரிந்துரைகளின் மூலக்கல்லாகும்.",
            "why_b_en": "Incorrect. ARC promotes deepening democratic decentralization, not abolishing local bodies.",
            "why_b_ta": "தவறு. ARC ஜனநாயக அதிகாரப் பரவலாக்கத்தை ஆழப்படுத்துவதை ஊக்குவிக்கிறதே தவிர உள்ளாட்சி அமைப்புகளை ஒழிப்பதை அல்ல.",
            "why_c_en": "Incorrect. Relying on lotteries is volatile and contrary to sustainable fiscal principles.",
            "why_c_ta": "தவறு. லாட்டரிகளை நம்பியிருப்பது நிலையற்றது மற்றும் நிலையான நிதிக் கொள்கைகளுக்கு எதிரானது.",
            "why_d_en": "Incorrect. Transparent accounting is mandatory under Art 243J.",
            "why_d_ta": "தவறு. சரத்து 243J-ன் கீழ் வெளிப்படையான கணக்கு பராமரிப்பு கட்டாயமாகும்.",
            "tip_en": "Subsidiarity principle: Whatever can be done best at a lower tier should not be assigned to a higher tier.",
            "tip_ta": "துணைநிலைக் கொள்கை: கீழ் அடுக்கில் சிறப்பாகச் செய்யக்கூடிய எதையும் மேல் அடுக்கிற்கு ஒதுக்கக் கூடாது.",
            "fact_en": "The 11th Schedule contains 29 functional items for Panchayats, while the 12th Schedule contains 18 items for Municipalities.",
            "fact_ta": "11வது அட்டவணையில் பஞ்சாயத்துகளுக்கு 29 செயல்பாட்டு உருப்படிகளும், 12வது அட்டவணையில் நகராட்சிகளுக்கு 18 உருப்படிகளும் உள்ளன."
        },

        # 47. State Election Commissioner Independence vs Disciplinary Actions
        {
            "subtopic": "State Election Commissioner - Appointment, Tenure, Removal & Autonomy",
            "stem_en": "Can a State Government initiate disciplinary proceedings or departmental inquiries against a serving State Election Commissioner under the state civil service rules?",
            "stem_ta": "மாநில சிவில் சர்வீஸ் விதிகளின் கீழ் பதவியில் உள்ள மாநில தேர்தல் ஆணையருக்கு எதிராக மாநில அரசு ஒழுங்கு நடவடிக்கைகளையோ அல்லது துறைசார் விசாரணைகளையோ தொடங்க முடியுமா?",
            "options": [
                ("No, because the SEC holds an independent constitutional office and can only be removed in like manner as a High Court Judge (impeachment by Parliament)", "இல்லை, ஏனெனில் SEC ஒரு சுதந்திரமான அரசியலமைப்பு பதவியை வகிக்கிறார் மற்றும் உயர் நீதிமன்ற நீதிபதியைப் போன்ற முறையில் (நாடாளுமன்ற பதவி நீக்கம்) மட்டுமே நீக்கப்பட முடியும்"),
                ("Yes, any District Collector can suspend the SEC without providing any justification", "ஆம், எந்தவொரு மாவட்ட ஆட்சியரும் எந்த நியாயமும் இன்றி SEC-ஐ சஸ்பெண்ட் செய்யலாம்"),
                ("Yes, the State Minister for Municipal Administration can unilaterally issue a suspension order", "ஆம், நகராட்சி நிர்வாகத்திற்கான மாநில அமைச்சர் ஒருதலைப்பட்சமாக சஸ்பெண்ட் உத்தரவை பிறப்பிக்கலாம்"),
                ("Yes, by treating the SEC as a temporary daily-wage contractual worker", "ஆம், SEC-ஐ ஒரு தற்காலிக தினக்கூலி ஒப்பந்தத் தொழிலாளியாகக் கருதுவதன் மூலம்")
            ],
            "correct_key": "A",
            "exp_en": "Under Article 243K(2), the SEC is constitutionally insulated from state executive control. A serving SEC cannot be subjected to disciplinary inquiries, suspensions, or punitive actions by the State Government; the only constitutional method of removal is an address by Parliament under Article 124(4) / 217.",
            "exp_ta": "சரத்து 243K(2)-ன் கீழ், SEC மாநில நிர்வாகக் கட்டுப்பாட்டிலிருந்து அரசியலமைப்பு ரீதியாகப் பாதுகாக்கப்படுகிறார். பதவியில் உள்ள ஒரு SEC-க்கு எதிராக மாநில அரசால் ஒழுங்கு விசாரணைகள், சஸ்பெண்ட் அல்லது தண்டனை நடவடிக்கைகள் மேற்கொள்ள முடியாது; நாடாளுமன்ற பதவி நீக்கத் தீர்மானம் மட்டுமே அவரை நீக்கும் ஒரே அரசியலமைப்பு முறையாகும்.",
            "why_a_en": "Correct. SEC enjoys High Court Judge removal protections and cannot be touched by state disciplinary rules.",
            "why_a_ta": "சரி. SEC உயர் நீதிமன்ற நீதிபதி நீக்கப் பாதுகாப்புகளை அனுபவிக்கிறார் மற்றும் மாநில ஒழுங்கு விதிகளால் அவரை தொட முடியாது.",
            "why_b_en": "Incorrect. District Collectors are subordinate officers and report to the SEC during elections.",
            "why_b_ta": "தவறு. மாவட்ட ஆட்சியர்கள் துணை அதிகாரிகள் மற்றும் தேர்தலின் போது SEC-க்கு கீழ் செயல்படுகின்றனர்.",
            "why_c_en": "Incorrect. Ministers have zero disciplinary authority over constitutional commissioners.",
            "why_c_ta": "தவறு. அரசியலமைப்பு ஆணையர்கள் மீது அமைச்சர்களுக்கு எந்த ஒழுங்கு நடவடிக்கையும் எடுக்கும் அதிகாரம் இல்லை.",
            "why_d_en": "Incorrect. SEC is an independent constitutional post, not a contractual laborer.",
            "why_d_ta": "தவறு. SEC ஒரு சுதந்திரமான அரசியலமைப்புப் பதவி, ஒப்பந்தத் தொழிலாளி அல்ல.",
            "tip_en": "Article 243K(2) Proviso 1: SEC shall not be removed from his office except in like manner and on like grounds as a Judge of a High Court.",
            "tip_ta": "சரத்து 243K(2) வரம்புரை 1: உயர் நீதிமன்ற நீதிபதியை நீக்கும் முறையிலும் அடிப்படைகளிலும் தவிர SEC-ஐ பதவியிலிருந்து நீக்க முடியாது.",
            "fact_en": "Conditions of service of the SEC cannot be varied to his disadvantage after appointment.",
            "fact_ta": "நியமனத்திற்குப் பிறகு SEC-ன் பணி நிபந்தனைகளை அவருக்கு பாதகமாக மாற்ற முடியாது."
        },

        # 48. Article 243-J and 243-Z Audit Requirements
        {
            "subtopic": "Tamil Nadu State Election & Finance Commissions - Legal Framework, Rules & Precedents",
            "stem_en": "Under Articles 243J and 243Z of the Constitution, what power is vested in the State Legislature regarding the financial accounts of local bodies?",
            "stem_ta": "அரசியலமைப்பின் சரத்துகள் 243J மற்றும் 243Z-ன் கீழ், உள்ளாட்சி அமைப்புகளின் நிதிக் கணக்குகள் தொடர்பாக மாநில சட்டமன்றத்திற்கு என்ன அதிகாரம் வழங்கப்பட்டுள்ளது?",
            "options": [
                ("To make provisions by law with respect to the maintenance of accounts and the auditing of such accounts of Panchayats and Municipalities", "பஞ்சாயத்துகள் மற்றும் நகராட்சிகளின் கணக்குகளைப் பராமரித்தல் மற்றும் அத்தகைய கணக்குகளைத் தணிக்கை செய்வது தொடர்பாக சட்டத்தின் மூலம் ஏற்பாடுகளைச் செய்தல்"),
                ("To mandate that local body accounts shall be audited exclusively by foreign commercial banks", "உள்ளாட்சி கணக்குகள் வெளிநாட்டு வணிக வங்கிகளால் மட்டுமே தணிக்கை செய்யப்பட வேண்டும் என்று கட்டாயப்படுத்துதல்"),
                ("To declare that all public fund transactions in local bodies are strictly confidential state secrets", "உள்ளாட்சி அமைப்புகளில் உள்ள அனைத்து பொது நிதி பரிவர்த்தனைகளும் மிகவும் ரகசியமான அரசு ரகசியங்கள் என்று அறிவிக்க"),
                ("To abolish all written records and conduct business purely by oral promises", "அனைத்து எழுத்துப்பூர்வ பதிவுகளையும் ஒழித்து முற்றிலும் வாய்மொழி வாக்குறுதிகள் மூலம் நிர்வாகத்தை நடத்த")
            ],
            "correct_key": "A",
            "exp_en": "Articles 243J (for Panchayats) and 243Z (for Municipalities) state that the Legislature of a State may, by law, make provisions with respect to the maintenance of accounts and the auditing of such accounts. Pursuant to this, states enacted Local Fund Audit Acts and Panchayats Audit Rules.",
            "exp_ta": "சரத்துகள் 243J (பஞ்சாயத்துகள்) மற்றும் 243Z (நகராட்சிகள்) கணக்குகளைப் பராமரித்தல் மற்றும் தணிக்கை செய்தல் தொடர்பாக மாநில சட்டமன்றம் சட்டத்தின் மூலம் ஏற்பாடுகளைச் செய்யலாம் என்று கூறுகின்றன. இதன்படி மாநிலங்கள் உள்ளூர் நிதித் தணிக்கைச் சட்டங்களை இயற்றின.",
            "why_a_en": "Correct. Verbatim constitutional mandate of Articles 243J and 243Z.",
            "why_a_ta": "சரி. சரத்துகள் 243J மற்றும் 243Z-ன் சரியான அரசியலமைப்பு கட்டளை.",
            "why_b_en": "Incorrect. Foreign banks have no role in local fund audit.",
            "why_b_ta": "தவறு. உள்ளூர் நிதித் தணிக்கையில் வெளிநாட்டு வங்கிகளுக்கு எந்த பங்கும் இல்லை.",
            "why_c_en": "Incorrect. Local accounts are open to public inspection and social audit.",
            "why_c_ta": "தவறு. உள்ளாட்சி கணக்குகள் பொது ஆய்வு மற்றும் சமூகத் தணிக்கைக்கு திறந்தவை.",
            "why_d_en": "Incorrect. Rigorous written double-entry accounting is constitutionally mandated.",
            "why_d_ta": "தவறு. கடுமையான இரட்டைப் பதிவு கணக்கு பராமரிப்பு அரசியலமைப்பு ரீதியாக கட்டாயமாக்கப்பட்டுள்ளது.",
            "tip_en": "Art 243J = Audit of accounts of Panchayats. Art 243Z = Audit of accounts of Municipalities.",
            "tip_ta": "சரத்து 243J = பஞ்சாயத்து கணக்குகளின் தணிக்கை. சரத்து 243Z = நகராட்சி கணக்குகளின் தணிக்கை.",
            "fact_en": "CAG provides Technical Guidance and Supervision (TG&S) to the Local Fund Audit Department in states.",
            "fact_ta": "CAG மாநிலங்களில் உள்ள உள்ளூர் நிதித் தணிக்கைத் துறைக்கு தொழில்நுட்ப வழிகாட்டுதல் மற்றும் மேற்பார்வையை (TG&S) வழங்குகிறது."
        },

        # 49. SEC Powers During Natural Disasters (Disaster Management Act)
        {
            "subtopic": "State Election Commission - Constitutional Mandate & Provisions (Articles 243K & 243ZA)",
            "stem_en": "During a severe natural disaster or pandemic, in what manner does the State Election Commission adjust the election schedule while respecting the constitutional five-year term requirement?",
            "stem_ta": "கடுமையான இயற்கை பேரழிவு அல்லது தொற்றுநோயின் போது, அரசியலமைப்பு ஐந்து ஆண்டு பதவிக்காலத் தேவையை மதிக்கும் அதே வேளையில் மாநில தேர்தல் ஆணையம் தேர்தல் அட்டவணையை எவ்வாறு மாற்றியமைக்கிறது?",
            "options": [
                ("It can temporarily defer polling for a brief justifiable period due to force majeure, but must conduct polls at the earliest possible normalcy as mandated by the Supreme Court", "கட்டாய இயற்கை இடர்பாடுகள் காரணமாக நியாயமான குறுகிய காலத்திற்கு வாக்கெடுப்பை தற்காலிகமாக ஒத்திவைக்கலாம், ஆனால் உச்ச நீதிமன்ற கட்டளைப்படி இயல்பு நிலை திரும்பியவுடன் விரைவில் தேர்தலை நடத்த வேண்டும்"),
                ("It can permanently declare the state as an absolute monarchy without any further elections", "மேலும் தேர்தல்கள் ஏதுமின்றி மாநிலத்தை ஒரு முழுமையான முடியாட்சியாக நிரந்தரமாக அறிவிக்கலாம்"),
                ("It dissolves the state assembly and hands power over to foreign election monitors", "இது மாநில சட்டமன்றத்தைக் கலைத்து அதிகாரத்தை வெளிநாட்டுத் தேர்தல் கண்காணிப்பாளர்களிடம் ஒப்படைக்கிறது"),
                ("It transfers the conduct of local body elections to the local police constables", "உள்ளாட்சித் தேர்தல்களை நடத்தும் பொறுப்பை உள்ளூர் காவலர்களிடம் ஒப்படைக்கிறது")
            ],
            "correct_key": "A",
            "exp_en": "While the 5-year tenure rule is mandatory, the Supreme Court in Kishan Singh Tomar (2006) recognized that unforeseen calamities (war, earthquake, floods, pandemics) act as 'force majeure' justifying a brief deferment. However, elections must be held at the earliest possible opportunity once normalcy returns.",
            "exp_ta": "5 ஆண்டு பதவிக்கால விதி கட்டாயமானது என்றாலும், கிஷன் சிங் தோமர் (2006) வழக்கில் உச்ச நீதிமன்றம் எதிர்பாராத பேரழிவுகள் (போர், நிலநடுக்கம், வெள்ளம், தொற்றுநோய்) குறுகிய கால ஒத்திவைப்பை நியாயப்படுத்தும் 'இயற்கை இடர்பாடுகளாக' செயல்படுகின்றன என்பதை அங்கீகரித்தது. இருப்பினும், இயல்பு நிலை திரும்பியவுடன் விரைவில் தேர்தல்கள் நடத்தப்பட வேண்டும்.",
            "why_a_en": "Correct. Brief emergency postponement is permitted, followed by prompt election resumption.",
            "why_a_ta": "சரி. குறுகிய அவசரகால ஒத்திவைப்பு அனுமதிக்கப்படுகிறது, அதைத் தொடர்ந்து உடனடியாக தேர்தல் மீண்டும் நடத்தப்பட வேண்டும்.",
            "why_b_en": "Incorrect. Democratic republic character is part of the basic structure.",
            "why_b_ta": "தவறு. ஜனநாயகக் குடியரசுத் தன்மை அடிப்படை கட்டமைப்பின் ஒரு பகுதியாகும்.",
            "why_c_en": "Incorrect. Foreign monitors have no jurisdiction in Indian sovereign elections.",
            "why_c_ta": "தவறு. இந்திய இறையாண்மைத் தேர்தல்களில் வெளிநாட்டு கண்காணிப்பாளர்களுக்கு எந்த அதிகாரமும் இல்லை.",
            "why_d_en": "Incorrect. SEC cannot abdicate its constitutional functions to the police force.",
            "why_d_ta": "தவறு. SEC தனது அரசியலமைப்பு பணிகளை காவல் துறையிடம் ஒப்படைக்க முடியாது.",
            "tip_en": "Force majeure deferment is narrow and must be remedied immediately upon cessation of the calamity.",
            "tip_ta": "இயற்கை இடர்பாடுகளுக்கான ஒத்திவைப்பு குறுகிய காலத்திற்கு மட்டுமே மற்றும் பேரழிவு முடிந்தவுடன் உடனடியாக சரிசெய்யப்பட வேண்டும்.",
            "fact_en": "During the COVID-19 pandemic in 2020-21, several local body polls were briefly rescheduled with SC approval.",
            "fact_ta": "2020-21 கோவிட் தொற்றுநோயின் போது, உச்ச நீதிமன்ற ஒப்புதலுடன் பல உள்ளாட்சித் தேர்தல்கள் சிறிது காலம் மாற்றி அமைக்கப்பட்டன."
        },

        # 50. SFC Synchronization with Central Finance Commission
        {
            "subtopic": "State Finance Commission - Constitutional Mandate, Composition & Role (Articles 243I & 243Y)",
            "stem_en": "Why have successive Central Finance Commissions (including the 13th, 14th, and 15th FCs) emphasized the synchronization of State Finance Commission award periods with the Central Finance Commission award period?",
            "stem_ta": "மத்திய நிதி ஆணையத்தின் விருது காலத்துடன் மாநில நிதி ஆணைய விருது காலங்களை ஒத்திசைக்க வேண்டும் என்று அடுத்தடுத்த மத்திய நிதி ஆணையங்கள் (13, 14 மற்றும் 15வது FC-கள் உட்பட) ஏன் வலியுறுத்தியுள்ளன?",
            "options": [
                ("To allow the Central Finance Commission to accurately assess the local body resource gaps based on current, updated SFC reports as contemplated under Article 280(3)(bb) and (c)", "சரத்து 280(3)(bb) மற்றும் (c)-ன் கீழ் கருதப்பட்டபடி தற்போதைய, புதுப்பிக்கப்பட்ட SFC அறிக்கைகளின் அடிப்படையில் உள்ளாட்சி அமைப்புகளின் நிதி இடைவெளிகளை மத்திய நிதி ஆணையம் துல்லியமாக மதிப்பிடுவதற்கு அனுமதிக்க"),
                ("To ensure that both commissions can hold joint press conferences in foreign countries", "இரு ஆணையங்களும் வெளிநாடுகளில் கூட்டாக செய்தியாளர் சந்திப்புகளை நடத்துவதை உறுதி செய்ய"),
                ("To combine the state budget with the central budget into a single unapproved treasury account", "மாநில பட்ஜெட்டையும் மத்திய பட்ஜெட்டையும் ஒரே அங்கீகரிக்கப்படாத கருவூலக் கணக்கில் இணைக்க"),
                ("To permanently bar states from collecting their own local sales and property taxes", "மாநிலங்கள் தங்கள் சொந்த உள்ளூர் விற்பனை மற்றும் சொத்து வரிகளை வசூலிப்பதை நிரந்தரமாகத் தடை செய்ய")
            ],
            "correct_key": "A",
            "exp_en": "Under Article 280(3)(bb) & (c), the Central Finance Commission is tasked with augmenting state consolidated funds 'on the basis of the recommendations made by the Finance Commission of the State'. When SFC reports are delayed or desynchronized, the Central FC is forced to rely on ad-hoc estimations rather than empirical state-level assessments.",
            "exp_ta": "சரத்து 280(3)(bb) & (c)-ன் கீழ், 'மாநில நிதி ஆணையத்தால் செய்யப்பட்ட பரிந்துரைகளின் அடிப்படையில்' மாநில தொகுப்பு நிதியை பெருக்குவது மத்திய நிதி ஆணையத்தின் பணியாகும். SFC அறிக்கைகள் தாமதமாகும் போது அல்லது ஒத்திசைவு இல்லாத போது, மத்திய FC மாநில அளவிலான மதிப்பீடுகளுக்குப் பதிலாக தற்காலிக மதிப்பீடுகளை நம்ப வேண்டிய கட்டாயத்திற்கு தள்ளப்படுகிறது.",
            "why_a_en": "Correct. Synchronization ensures empirical data from SFCs informs Central FC local body grant sizing.",
            "why_a_ta": "சரி. ஒத்திசைவு SFC-களின் தரவு மத்திய FC உள்ளாட்சி மானிய அளவை தீர்மானிக்க உதவுவதை உறுதி செய்கிறது.",
            "why_b_en": "Incorrect. Press conferences are incidental, not the constitutional rationale.",
            "why_b_ta": "தவறு. செய்தியாளர் சந்திப்புகள் தற்செயலானவை, அரசியலமைப்பு காரணம் அல்ல.",
            "why_c_en": "Incorrect. Central and State consolidated funds remain legally distinct under Articles 266.",
            "why_c_ta": "தவறு. மத்திய மற்றும் மாநில தொகுப்பு நிதிகள் சரத்து 266-ன் கீழ் சட்டப்பூர்வமாக தனித்தனியாகவே உள்ளன.",
            "why_d_en": "Incorrect. Property taxes remain the core sovereign prerogative of local self-government.",
            "why_d_ta": "தவறு. சொத்து வரி உள்ளாட்சி அமைப்புகளின் முக்கிய அதிகாரமாகவே தொடர்கிறது.",
            "tip_en": "Synchronization enables seamless vertical flow: Local SFC data -> Central FC award under Art 280(3)(bb)/(c) -> Local body grants.",
            "tip_ta": "ஒத்திசைவு தடையற்ற செங்குத்து ஓட்டத்தை செயல்படுத்துகிறது: உள்ளூர் SFC தரவு -> சரத்து 280(3)(bb)/(c)-ன் கீழ் மத்திய FC விருது -> உள்ளாட்சி மானியங்கள்.",
            "fact_en": "The 15th FC recommended that States must constitute SFCs timely and upload their reports before release of performance grants.",
            "fact_ta": "15வது FC, செயல்திறன் மானியங்களை வெளியிடுவதற்கு முன் மாநிலங்கள் SFC-களை சரியான நேரத்தில் அமைத்து அவற்றின் அறிக்கைகளை பதிவேற்ற வேண்டும் என்று பரிந்துரைத்தது."
        }
    ]


def build_hard_file():
    raw_qs = get_hard_raw_questions()
    print(f"Generated {len(raw_qs)} raw Hard questions for State Election & Finance Commissions.")

    questions = []
    for i, item in enumerate(raw_qs, start=1):
        opts = item["options"]
        correct_key = item["correct_key"]

        q = make_sefc_q(
            qid=f"SEFC_H_{i:03d}",
            diff="hard",
            qtype="factual",
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
            tags=["polity", "state_election_finance_commissions", "hard", item["subtopic"].lower().replace(" ", "_")]
        )
        questions.append(q)

    # Randomize and balance answer keys: 12-13 per option
    balanced = randomize_and_balance_dataset(questions, seed=42)
    key_dist = Counter(q["correct_answer"] for q in balanced)
    print(f"Balanced Hard Key Distribution: {dict(key_dist)}")

    out_dir = os.path.join("data", "questions", "polity")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "state_election_finance_commissions_hard.json")

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(balanced, f, ensure_ascii=False, indent=2)
    print(f"Saved balanced Hard MCQs to {out_path}")

    # Validation
    rep = ContentValidator.validate_file(out_path, expected_count=50, expected_prefix="SEFC_H_")
    print(f"Validation: {'PASS' if rep.is_valid else 'FAIL'} | Total: {rep.total_audited}")
    print(f"Keys: {rep.key_distribution}")
    if not rep.is_valid:
        for iss in rep.issues:
            print("  Issue:", iss.severity, iss.field_name, iss.message)
    return rep.is_valid


if __name__ == "__main__":
    success = build_hard_file()
    if not success:
        exit(1)
