# -*- coding: utf-8 -*-
"""
Co-operative Societies - Part 1: Hard MCQs (50 Questions: CS_H_001 to CS_H_050)
TNPSC Nova AI Content Engine
"""
import os
import json
from collections import Counter
from tools.nova_content_engine.answer_randomizer import randomize_and_balance_dataset
from tools.nova_content_engine.validator import ContentValidator
from cooperative_societies_mcq_helper import make_coop_q


def get_hard_raw_questions():
    return [
        # 1. Thalappalam Case (RTI and Cooperatives)
        {
            "subtopic": "Judicial Pronouncements - Fundamental Rights & RTI",
            "stem_en": "In the landmark judgment Thalappalam Service Cooperative Bank Ltd. v. State of Kerala (2013), what did the Supreme Court rule regarding the applicability of the Right to Information (RTI) Act, 2005 to co-operative societies?",
            "stem_ta": "தலப்பாலம் சர்வீஸ் கூட்டுறவு வங்கி எதிர் கேரள அரசு (2013) என்ற முக்கிய வழக்கில், தகவல் அறியும் உரிமைச் சட்டம் (RTI) 2005 கூட்டுறவு சங்கங்களுக்குப் பொருந்துவது குறித்து உச்ச நீதிமன்றம் என்ன தீர்ப்பளித்தது?",
            "options": [
                ("Cooperative societies are NOT 'public authorities' under Section 2(h) of the RTI Act unless substantially financed or controlled by Government, but information accessible to the Registrar under state law can be accessed by citizens under RTI", "அரசால் கணிசமாக நிதியளிக்கப்படாவிட்டால் அல்லது கட்டுப்படுத்தப்படாவிட்டால் கூட்டுறவு சங்கங்கள் RTI சட்டத்தின் பிரிவு 2(h)-ன் கீழ் 'பொது அதிகார அமைப்புகள்' அல்ல; ஆனால் மாநிலச் சட்டத்தின் கீழ் பதிவாளரால் பெறக்கூடிய தகவல்களை குடிமக்கள் RTI மூலம் பெறலாம்"),
                ("All cooperative societies are automatically public authorities under the RTI Act regardless of funding", "நிதி உதவியைப் பொருட்படுத்தாமல் அனைத்து கூட்டுறவு சங்கங்களும் RTI சட்டத்தின் கீழ் தானாகவே பொது அதிகார அமைப்புகளாகும்"),
                ("Citizens have zero right to obtain any information about cooperatives under any circumstances", "எந்தச் சூழ்நிலையிலும் கூட்டுறவுகள் பற்றிய எந்தத் தகவலையும் பெற குடிமக்களுக்கு எந்த உரிமையும் இல்லை"),
                ("The RTI Act applies only to multi-state cooperatives and never to state cooperatives", "RTI சட்டம் பல்மாநில கூட்டுறவுகளுக்கு மட்டுமே பொருந்தும், மாநில கூட்டுறவுகளுக்கு ஒருபோதும் பொருந்தாது")
            ],
            "correct_key": "A",
            "exp_en": "In Thalappalam (2013), the Supreme Court held that cooperative societies not owned, controlled, or substantially financed by government do not fall within the definition of 'public authority' under Section 2(h) of RTI Act. However, citizens can seek information regarding such societies through the Registrar under Section 2(f) of the RTI Act to the extent the Registrar can access it under state cooperative laws.",
            "exp_ta": "தலப்பாலம் (2013) வழக்கில், அரசால் சொந்தமாக வைத்திருக்கப்படாத, கட்டுப்படுத்தப்படாத அல்லது கணிசமாக நிதியளிக்கப்படாத கூட்டுறவு சங்கங்கள் RTI சட்டத்தின் பிரிவு 2(h)-ன் கீழ் 'பொது அதிகார அமைப்பு' என்ற வரையறைக்குள் வராது என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது. இருப்பினும், மாநில கூட்டுறவுச் சட்டங்களின் கீழ் பதிவாளர் பெறக்கூடிய தகவல்களை குடிமக்கள் RTI சட்டத்தின் பிரிவு 2(f)-ன் கீழ் பதிவாளர் மூலமாகப் பெற முடியும்.",
            "why_a_en": "Correct. Precise synthesis of the Thalappalam ruling on Section 2(h) vs Section 2(f).",
            "why_a_ta": "சரி. பிரிவு 2(h) மற்றும் பிரிவு 2(f) தொடர்பான தலப்பாலம் தீர்ப்பின் துல்லியமான விளக்கம்.",
            "why_b_en": "Incorrect. Pure member-funded cooperatives are not public authorities under Section 2(h).",
            "why_b_ta": "தவறு. உறுப்பினர்களால் மட்டுமே நடத்தப்படும் சங்கங்கள் பிரிவு 2(h)-ன் கீழ் பொது அதிகார அமைப்புகள் அல்ல.",
            "why_c_en": "Incorrect. Citizens can obtain information through the regulatory Registrar.",
            "why_c_ta": "தவறு. பதிவாளர் வழியாக குடிமக்கள் தகவல்களைப் பெற முடியும்.",
            "why_d_en": "Incorrect. Substantially financed state cooperatives also fall under RTI Section 2(h).",
            "why_d_ta": "தவறு. அரசு நிதி உதவி பெறும் கூட்டுறவுகளுக்கும் RTI பொருந்தும்.",
            "tip_en": "RTI route: Citizen -> Applies to Cooperative Registrar (Public Authority) -> Registrar collects and provides info under Section 2(f).",
            "tip_ta": "RTI வழிமுறை: குடிமகன் -> கூட்டுறவுப் பதிவாளருக்கு விண்ணப்பிக்கிறார் -> பதிவாளர் பிரிவு 2(f)-ன் கீழ் தகவலைப் பெற்றுத் தருகிறார்.",
            "fact_en": "Substantial financing can be direct or indirect grants/subsidies from the Consolidated Fund.",
            "fact_ta": "ஒருங்கிணைந்த நிதியிலிருந்து வழங்கப்படும் நேரடி அல்லது மறைமுக மானியங்கள் கணிசமான நிதி உதவியாகக் கருதப்படும்."
        },

        # 2. Damyanti Naranga Case (1971)
        {
            "subtopic": "Fundamental Rights - Article 19(1)(c)",
            "stem_en": "In the constitutional bench decision Damyanti Naranga v. Union of India (1971), what fundamental doctrine regarding the scope of Article 19(1)(c) was established by the Supreme Court?",
            "stem_ta": "தமயந்தி நரங்கா எதிர் இந்திய அரசு (1971) அரசியலமைப்பு அமர்வு வழக்கில், சரத்து 19(1)(c)-ன் வரம்பு குறித்து உச்ச நீதிமன்றத்தால் நிறுவப்பட்ட அடிப்படை கோட்பாடு என்ன?",
            "options": [
                ("The right to form an association includes the right to continue it with members of their own choice; forced statutory alteration of membership violates Article 19(1)(c)", "சங்கம் அமைக்கும் உரிமையானது தாங்கள் விரும்பிய உறுப்பினர்களுடன் அதைத் தொடரும் உரிமையையும் உள்ளடக்கியது; சட்டத்தின் மூலம் உறுப்பினர்களைக் கட்டாயமாகத் திணிப்பது சரத்து 19(1)(c)-ஐ மீறுவதாகும்"),
                ("The Government has absolute power to replace all members of any private society at any time", "எந்தவொரு தனியார் சங்கத்தின் அனைத்து உறுப்பினர்களையும் எந்த நேரத்திலும் மாற்ற அரசுக்கு முழு அதிகாரம் உள்ளது"),
                ("Article 19(1)(c) applies only to political parties and not to voluntary associations", "சரத்து 19(1)(c) அரசியல் கட்சிகளுக்கு மட்டுமே பொருந்தும், தன்னார்வச் சங்கங்களுக்கு அல்ல"),
                ("Members have no right to associate unless authorized by the local police", "உள்ளூர் காவல்துறையினரால் அங்கீகரிக்கப்படாவிட்டால் உறுப்பினர்களுக்கு சங்கம் அமைக்கும் உரிமை இல்லை")
            ],
            "correct_key": "A",
            "exp_en": "In Damyanti Naranga (1971), the Supreme Court ruled that the right to form an association under Article 19(1)(c) is not merely the right to initiate an association, but includes the right to continue the association with the composition agreed upon by its members. Enforced expansion of membership by legislative statute without members' consent violates Article 19(1)(c).",
            "exp_ta": "தமயந்தி நரங்கா (1971) வழக்கில், சரத்து 19(1)(c)-ன் கீழ் சங்கம் அமைக்கும் உரிமை என்பது சங்கத்தைத் தொடங்குவது மட்டுமல்லாமல், உறுப்பினர்கள் ஒப்புக்கொண்ட அமைப்போடு அதைத் தொடர்வதையும் உள்ளடக்கியது என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது. உறுப்பினர்களின் சம்மதமின்றி சட்டத்தின் மூலம் புதிய உறுப்பினர்களைத் திணிப்பது சரத்து 19(1)(c)-ஐ மீறுவதாகும்.",
            "why_a_en": "Correct. Foundational precedent protecting voluntary autonomy of associations.",
            "why_a_ta": "சரி. சங்கங்களின் தன்னார்வ தன்னாட்சியைப் பாதுகாக்கும் அடிப்படையான தீர்ப்பு.",
            "why_b_en": "Incorrect. Executive cannot arbitrarily alter membership without violating 19(1)(c).",
            "why_b_ta": "தவறு. தன்னிச்சையாக உறுப்பினர்களை மாற்ற அரசுக்கு அதிகாரம் இல்லை.",
            "why_c_en": "Incorrect. 19(1)(c) explicitly covers associations, unions, and cooperatives.",
            "why_c_ta": "தவறு. சரத்து 19(1)(c) சங்கங்கள், தொழிற்சங்கங்கள் மற்றும் கூட்டுறவுகளை உள்ளடக்கியது.",
            "why_d_en": "Incorrect. Police authorization is not a constitutional prerequisite for forming an association.",
            "why_d_ta": "தவறு. காவல் அனுமதி அரசியலமைப்புத் தேவை அல்ல.",
            "tip_en": "Damyanti Naranga forms the constitutional bedrock cited in all modern cooperative autonomy litigations.",
            "tip_ta": "தமயந்தி நரங்கா வழக்கு அனைத்து நவீன கூட்டுறவு தன்னாட்சி வழக்குகளிலும் மேற்கோள் காட்டப்படும் அரசியலமைப்பு அடித்தளமாகும்.",
            "fact_en": "The case arose out of the Hindi Sahitya Sammelan Act enacted by Parliament.",
            "fact_ta": "இந்த வழக்கு நாடாளுமன்றத்தால் இயற்றப்பட்ட இந்தி சாகித்ய சம்மேளனச் சட்டத்திலிருந்து உருவானது."
        },

        # 3. Zoroastrian Co-operative Housing Society Case (2005)
        {
            "subtopic": "Fundamental Rights vs Cooperative Autonomy",
            "stem_en": "In Zoroastrian Co-operative Housing Society Ltd. v. District Registrar (2005), what did the Supreme Court hold regarding restrictive membership by-laws in a cooperative housing society?",
            "stem_ta": "ஜொராஸ்ட்ரியன் கூட்டுறவு வீட்டுவசதி சங்கம் எதிர் மாவட்டப் பதிவாளர் (2005) வழக்கில், கூட்டுறவு வீட்டுவசதி சங்கத்தின் குறிப்பிட்ட சமூக உறுப்பினர்களுக்கான துணைவிதி குறித்து உச்ச நீதிமன்றம் என்ன தீர்ப்பளித்தது?",
            "options": [
                ("A cooperative society can validly restrict membership to a specific community in its by-laws under freedom of contract and association, and the Registrar cannot force it to admit outsiders contrary to by-laws", "ஒப்பந்தம் மற்றும் சங்கம் அமைக்கும் சுதந்திரத்தின் கீழ் ஒரு கூட்டுறவு சங்கம் தனது துணைவிதிகளில் குறிப்பிட்ட சமூகத்திற்கு மட்டுமே உறுப்பினர் சேர்க்கையை கட்டுப்படுத்த முடியும்; துணைவிதிகளுக்கு மாறாக வெளியாட்களை சேர்க்க பதிவாளர் கட்டாயப்படுத்த முடியாது"),
                ("All cooperative societies must mandatorily open membership to all citizens without any qualification", "அனைத்து கூட்டுறவு சங்கங்களும் எந்தத் தகுதியும் இன்றி அனைத்து குடிமக்களுக்கும் உறுப்பினர் சேர்க்கையை கட்டாயமாகத் திறக்க வேண்டும்"),
                ("Housing cooperatives are unconstitutional per se", "வீட்டுவசதி கூட்டுறவுகள் அரசியலமைப்பிற்கு முரணானவை"),
                ("Only the State Government can own residential plots in India", "இந்தியாவில் குடியிருப்பு மனைகளை மாநில அரசு மட்டுமே சொந்தமாக வைத்திருக்க முடியும்")
            ],
            "correct_key": "A",
            "exp_en": "In Zoroastrian Co-operative Housing Society (2005), the Supreme Court held that members entering into a cooperative contract are entitled to associate with persons of their choice. A by-law restricting membership to Parsis was valid and did not violate public policy, Article 14, or Article 15 (which applies to State discrimination, not private cooperative covenants).",
            "exp_ta": "ஜொராஸ்ட்ரியன் கூட்டுறவு வீட்டுவசதி சங்க (2005) வழக்கில், கூட்டுறவு ஒப்பந்தத்தில் நுழையும் உறுப்பினர்கள் தாங்கள் விரும்பும் நபர்களுடன் இணைய உரிமை உண்டு என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது. பார்சி சமூகத்தினருக்கு மட்டுமே உறுப்பினர் சேர்க்கையைக் கட்டுப்படுத்தும் துணைவிதி செல்லுபடியாகும்; இது சரத்து 14 அல்லது 15-ஐ மீறவில்லை (சரத்து 15 அரசு பாகுபாட்டிற்கு மட்டுமே பொருந்தும்).",
            "why_a_en": "Correct. Upholding freedom of contract and voluntary association in cooperative housing by-laws.",
            "why_a_ta": "சரி. கூட்டுறவு துணைவிதிகளில் ஒப்பந்த சுதந்திரம் மற்றும் தன்னார்வ சங்கம் அமைக்கும் உரிமையை உறுதி செய்தது.",
            "why_b_en": "Incorrect. Open membership is a principle, but reasonable contractual restrictions in housing societies were upheld.",
            "why_b_ta": "தவறு. வீட்டுவசதி சங்கங்களில் நியாயமான ஒப்பந்தக் கட்டுப்பாடுகள் செல்லும் என தீர்ப்பளிக்கப்பட்டது.",
            "why_c_en": "Incorrect. Housing cooperatives are fully recognized statutory entities.",
            "why_c_ta": "தவறு. வீட்டுவசதி கூட்டுறவுகள் சட்டப்பூர்வ அமைப்புகளாகும்.",
            "why_d_en": "Incorrect. Private property ownership is protected under Article 300A.",
            "why_d_ta": "தவறு. சொத்துரிமை சரத்து 300A-ன் கீழ் பாதுகாக்கப்படுகிறது.",
            "tip_en": "Article 15(1) prohibits discrimination by the 'State'; private voluntary cooperative associations enjoy contractual autonomy.",
            "tip_ta": "சரத்து 15(1) 'அரசு' பாகுபாடு காட்டுவதைத் தடை செய்கிறது; தனியார் தன்னார்வக் கூட்டுறவுகள் ஒப்பந்த தன்னாட்சியைக் கொண்டுள்ளன.",
            "fact_en": "The case affirmed that cooperative law respects the self-determined qualifications agreed upon in by-laws.",
            "fact_ta": "துணைவிதிகளில் ஒப்புக்கொள்ளப்பட்ட தகுதிகளை கூட்டுறவுச் சட்டம் மதிக்கிறது என்பதை இந்த வழக்கு உறுதிப்படுத்தியது."
        },

        # 4. SARFAESI Act Applicability - Pandurang Ganpati Chaugule (2020)
        {
            "subtopic": "Banking Cooperatives & SARFAESI Act",
            "stem_en": "In the landmark 5-Judge Constitution Bench ruling Pandurang Ganpati Chaugule v. Vishwasrao Patil Murgud Sahakari Bank Ltd. (2020), what major constitutional determination was made regarding cooperative banks?",
            "stem_ta": "பாண்டுரங் கணபதி சவுகுலே எதிர் விஸ்வாசராவ் பாட்டீல் முர்குட் சககாரி வங்கி (2020) என்ற 5 நீதிபதிகள் கொண்ட அரசியலமைப்பு அமர்வு வரலாற்றுத் தீர்ப்பில், கூட்டுறவு வங்கிகள் தொடர்பாக எடுக்கப்பட்ட முக்கிய அரசியலமைப்பு முடிவு என்ன?",
            "options": [
                ("Cooperative banks are 'banks' under the SARFAESI Act, 2002, and Parliament has legislative competence under Union List Entry 45 to regulate debt recovery of cooperative banks", "கூட்டுறவு வங்கிகள் SARFAESI சட்டம் 2002-ன் கீழ் 'வங்கிகள்' ஆகும், மேலும் மத்தியப் பட்டியல் பதிவு 45-ன் கீழ் கூட்டுறவு வங்கிகளின் கடன் வசூலை ஒழுங்குபடுத்த நாடாளுமன்றத்திற்கு முழு சட்டமன்ற அதிகாரம் உண்டு"),
                ("Cooperative banks are strictly forbidden from recovering loans from borrowers", "கூட்டுறவு வங்கிகள் கடன் வாங்கியவர்களிடமிருந்து கடனை வசூலிக்க கண்டிப்பாகத் தடை விதிக்கப்பட்டுள்ளது"),
                ("SARFAESI Act applies only to foreign multinational banks in India", "SARFAESI சட்டம் இந்தியாவில் உள்ள வெளிநாட்டு பன்னாட்டு வங்கிகளுக்கு மட்டுமே பொருந்தும்"),
                ("Cooperative banks can only function under village panchayat resolutions", "கூட்டுறவு வங்கிகள் கிராம ஊராட்சித் தீர்மானங்களின் கீழ் மட்டுமே செயல்பட முடியும்")
            ],
            "correct_key": "A",
            "exp_en": "In Pandurang Ganpati Chaugule (2020), a 5-Judge Constitution Bench overruled previous ambiguities and held that cooperative banks registered under state legislation fall within the meaning of 'banking companies' under Entry 45 of List I. Consequently, the SARFAESI Act applies to cooperative banks, enabling speedy recovery of non-performing assets (NPAs) without civil court intervention.",
            "exp_ta": "பாண்டுரங் கணபதி சவுகுலே (2020) வழக்கில், 5 நீதிபதிகள் கொண்ட அரசியலமைப்பு அமர்வு, மாநிலச் சட்டங்களின் கீழ் பதிவு செய்யப்பட்ட கூட்டுறவு வங்கிகள் பட்டியல் I-ன் பதிவு 45-ன் கீழ் 'வங்கி நிறுவனங்கள்' என்ற வரம்பிற்குள் வருகின்றன என்று தீர்ப்பளித்தது. இதனால், SARFAESI சட்டம் கூட்டுறவு வங்கிகளுக்கும் பொருந்தும், இதன் மூலம் வாராக் கடன்களை சிவில் நீதிமன்றத் தலையீடின்றி விரைவாக வசூலிக்க முடியும்.",
            "why_a_en": "Correct. SARFAESI Act applies to cooperative banks under Union List Entry 45 (Banking).",
            "why_a_ta": "சரி. மத்தியப் பட்டியல் பதிவு 45 (வங்கித் தொழில்)-ன் கீழ் SARFAESI சட்டம் கூட்டுறவு வங்கிகளுக்கும் பொருந்தும்.",
            "why_b_en": "Incorrect. The ruling specifically empowered cooperative banks to recover NPAs faster.",
            "why_b_ta": "தவறு. கூட்டுறவு வங்கிகள் கடன்களை விரைவாக வசூலிக்கவே இத்தீர்ப்பு அதிகாரம் அளித்தது.",
            "why_c_en": "Incorrect. SARFAESI Act applies to Indian public, private, and cooperative banks.",
            "why_c_ta": "தவறு. SARFAESI சட்டம் பொது, தனியார் மற்றும் கூட்டுறவு வங்கிகளுக்குப் பொருந்தும்.",
            "why_d_en": "Incorrect. Banking is governed by RBI and Central Banking Regulation Act.",
            "why_d_ta": "தவறு. வங்கித் தொழில் ரிசர்வ் வங்கி மற்றும் மத்திய சட்டத்தால் ஆளப்படுகிறது.",
            "tip_en": "Doctrine of Pith and Substance: The 'pith and substance' of SARFAESI is 'Banking' (List I Entry 45), not 'Cooperative Societies' (List II Entry 32).",
            "tip_ta": "அடிநாதக் கோட்பாடு: SARFAESI சட்டத்தின் 'அடிநாதம்' என்பது 'வங்கித் தொழில்' (பட்டியல் I பதிவு 45) ஆகும், 'கூட்டுறவு சங்கம்' (பட்டியல் II பதிவு 32) அல்ல.",
            "fact_en": "This verdict resolved nearly two decades of conflicting judgments on cooperative debt recovery.",
            "fact_ta": "கூட்டுறவுக் கடன் வசூல் தொடர்பாக இரண்டு தசாப்தங்களாக நிலவி வந்த முரண்பாடான தீர்ப்புகளுக்கு இத்தீர்ப்பு முற்றுப்புள்ளி வைத்தது."
        },

        # 5. Greater Bombay Co-op Bank Case (2007)
        {
            "subtopic": "Banking Cooperatives & Federal Competence",
            "stem_en": "What was the core holding in Greater Bombay Co-operative Bank Ltd. v. United Yarn Tex Pvt. Ltd. (2007) that previously distinguished cooperative banks from commercial banks?",
            "stem_ta": "கிரேட்டர் பாம்பே கூட்டுறவு வங்கி எதிர் யுனைடெட் நூல் டெக்ஸ் (2007) வழக்கில் கூட்டுறவு வங்கிகளை வணிக வங்கிகளிலிருந்து வேறுபடுத்திய முந்தைய முக்கியத் தீர்ப்பு என்ன?",
            "options": [
                ("Cooperative banks constituted under State Acts were not covered under the Recovery of Debts Due to Banks Act, 1993 (DRT Act) unless expressly included by Parliament", "நாடாளுமன்றத்தால் வெளிப்படையாகச் சேர்க்கப்படும் வரை, மாநிலச் சட்டங்களின் கீழ் அமைக்கப்பட்ட கூட்டுறவு வங்கிகள் வங்கிகளுக்கு வர வேண்டிய கடன் வசூல் சட்டம் 1993-ன் (DRT சட்டம்) கீழ் வராது"),
                ("Cooperative banks cannot accept money deposits from Indian citizens", "கூட்டுறவு வங்கிகள் இந்திய குடிமக்களிடமிருந்து பண வைப்புகளை ஏற்க முடியாது"),
                ("Cooperative banks are exempt from all taxes", "கூட்டுறவு வங்கிகளுக்கு அனைத்து வரிகளிலிருந்தும் விலக்கு உண்டு"),
                ("The Reserve Bank of India has zero authority over cooperative banks", "கூட்டுறவு வங்கிகள் மீது ரிசர்வ் வங்கிக்கு எவ்வித அதிகாரமும் இல்லை")
            ],
            "correct_key": "A",
            "exp_en": "In Greater Bombay (2007), the Supreme Court held that cooperative banks registered under State Cooperative laws were not 'banking companies' for the purpose of the 1993 DRT Act. This led Parliament in 2013 to specifically amend the SARFAESI Act to include multi-state and state cooperative banks.",
            "exp_ta": "கிரேட்டர் பாம்பே (2007) வழக்கில், மாநிலக் கூட்டுறவுச் சட்டங்களின் கீழ் பதிவு செய்யப்பட்ட கூட்டுறவு வங்கிகள் 1993 DRT சட்டத்தின் நோக்கங்களுக்கான 'வங்கி நிறுவனங்கள்' அல்ல என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது. இதனைத் தொடர்ந்தே 2013-ல் நாடாளுமன்றம் SARFAESI சட்டத்தைத் திருத்தி கூட்டுறவு வங்கிகளை வெளிப்படையாக இணைத்தது.",
            "why_a_en": "Correct. Greater Bombay held that DRT Act 1993 did not automatically cover state cooperative banks.",
            "why_a_ta": "சரி. 1993 DRT சட்டம் தானாகவே மாநில கூட்டுறவு வங்கிகளுக்குப் பொருந்தாது என கிரேட்டர் பாம்பே வழக்கு கூறியது.",
            "why_b_en": "Incorrect. Cooperative banks have always accepted public deposits.",
            "why_b_ta": "தவறு. கூட்டுறவு வங்கிகள் பொது வைப்புகளை ஏற்று வருகின்றன.",
            "why_c_en": "Incorrect. Cooperative banks pay income tax under Section 80P restrictions.",
            "why_c_ta": "தவறு. கூட்டுறவு வங்கிகள் வருமான வரி செலுத்துகின்றன.",
            "why_d_en": "Incorrect. Banking Regulation Act 1949 applies to cooperative banks under Part V.",
            "why_d_ta": "தவறு. வங்கி ஒழுங்குமுறைச் சட்டம் பகுதி V-ன் கீழ் கூட்டுறவு வங்கிகளுக்குப் பொருந்துகிறது.",
            "tip_en": "Greater Bombay (2007) was later harmonized and distinguished by the 5-Judge Constitution Bench in Pandurang Chaugule (2020).",
            "tip_ta": "கிரேட்டர் பாம்பே (2007) தீர்ப்பு பின்னர் பாண்டுரங் சவுகுலே (2020) அரசியலமைப்பு அமர்வால் தெளிவுபடுத்தப்பட்டது.",
            "fact_en": "Cooperative banks operate under Section 56 of the Banking Regulation Act, 1949.",
            "fact_ta": "கூட்டுறவு வங்கிகள் வங்கி ஒழுங்குமுறைச் சட்டம் 1949-ன் பிரிவு 56-ன் கீழ் செயல்படுகின்றன."
        },

        # 6. Priority Sector Lending (PSL) Targets for UCBs
        {
            "subtopic": "Banking Cooperatives & RBI Regulation",
            "stem_en": "Under the revised Reserve Bank of India regulatory framework, what is the mandated Priority Sector Lending (PSL) target that Urban Co-operative Banks (UCBs) must achieve by March 31, 2026?",
            "stem_ta": "இந்திய ரிசர்வ் வங்கியின் திருத்தப்பட்ட ஒழுங்குமுறை கட்டமைப்பின் கீழ், நகர்ப்புறக் கூட்டுறவு வங்கிகள் (UCBs) 2026 மார்ச் 31-க்குள் அடைய வேண்டிய கட்டாய முன்னுரிமைத் துறை கடன் (PSL) இலக்கு என்ன?",
            "options": [
                ("75% of Adjusted Net Bank Credit (ANBC)", "சரிசெய்யப்பட்ட நிகர வங்கிக் கடனில் (ANBC) 75%"),
                ("40% of ANBC", "ANBC-ல் 40%"),
                ("25% of ANBC", "ANBC-ல் 25%"),
                ("100% of ANBC", "ANBC-ல் 100%")
            ],
            "correct_key": "A",
            "exp_en": "The Reserve Bank of India mandated that Urban Cooperative Banks (UCBs) must progressively increase their Priority Sector Lending (PSL) target from 40% to 75% of Adjusted Net Bank Credit (ANBC) or Credit Equivalent Amount of Off-Balance Sheet Exposure (CEOBE) by March 31, 2026.",
            "exp_ta": "இந்திய ரிசர்வ் வங்கி, நகர்ப்புறக் கூட்டுறவு வங்கிகள் (UCBs) தங்களின் முன்னுரிமைத் துறை கடன் (PSL) இலக்கை சரிசெய்யப்பட்ட நிகர வங்கிக் கடனில் (ANBC) 40%-லிருந்து 75%-ஆக 2026 மார்ச் 31-க்குள் படிப்படியாக உயர்த்த வேண்டும் என்று கட்டாயமாக்கியுள்ளது.",
            "why_a_en": "Correct. 75% of ANBC is the mandated PSL target for UCBs by March 2026.",
            "why_a_ta": "சரி. 2026 மார்ச் மாதத்திற்குள் UCB-களுக்கான PSL இலக்கு ANBC-ல் 75% ஆகும்.",
            "why_b_en": "Incorrect. 40% is the target for domestic scheduled commercial banks.",
            "why_b_ta": "தவறு. 40% என்பது வணிக வங்கிகளுக்கான இலக்கு.",
            "why_c_en": "Incorrect. 25% is too low.",
            "why_c_ta": "தவறு. 25% மிகக் குறைவு.",
            "why_d_en": "Incorrect. 100% is not mandated.",
            "why_d_ta": "தவறு. 100% கட்டாயமில்லை.",
            "tip_en": "Commercial Banks PSL target = 40%; UCBs PSL target = 75% (emphasizing MSME and small borrower support).",
            "tip_ta": "வணிக வங்கிகள் PSL = 40%; நகர்ப்புற கூட்டுறவு வங்கிகள் PSL = 75% (சிறு குறு தொழில்கள் ஆதரவு).",
            "fact_en": "Sub-targets include 12% for weaker sections and 40% for micro, small, and medium enterprises.",
            "fact_ta": "இதில் நலிவடைந்த பிரிவினருக்கு 12% மற்றும் குறு, சிறு தொழில்களுக்கு 40% என்ற துணை இலக்குகளும் அடங்கும்."
        },

        # 7. Four-Tier Regulatory Framework for UCBs (NS Vishwanathan Committee)
        {
            "subtopic": "Banking Cooperatives & RBI Regulation",
            "stem_en": "Based on the recommendations of the N.S. Vishwanathan Committee (2021), into how many tiers did the RBI categorize Urban Co-operative Banks based on deposit size for differentiated regulation?",
            "stem_ta": "என்.எஸ். விஸ்வநாதன் குழுவின் (2021) பரிந்துரைகளின் அடிப்படையில், மாறுபட்ட ஒழுங்குமுறைக்காக வைப்புத்தொகை அளவின் அடிப்படையில் நகர்ப்புறக் கூட்டுறவு வங்கிகளை ரிசர்வ் வங்கி எத்தனை அடுக்குகளாக வகைப்படுத்தியது?",
            "options": [
                ("4 Tiers (Tier 1: <=100 cr, Tier 2: 100-1000 cr, Tier 3: 1000-10000 cr, Tier 4: >10000 cr)", "4 அடுக்குகள் (அடுக்கு 1: <=100 கோடி, அடுக்கு 2: 100-1000 கோடி, அடுக்கு 3: 1000-10000 கோடி, அடுக்கு 4: >10000 கோடி)"),
                ("2 Tiers", "2 அடுக்குகள்"),
                ("3 Tiers", "3 அடுக்குகள்"),
                ("5 Tiers", "5 அடுக்குகள்")
            ],
            "correct_key": "A",
            "exp_en": "In 2022, following the N.S. Vishwanathan Committee recommendations, RBI adopted a 4-Tier regulatory framework for UCBs based on deposits: Tier 1 (deposits up to Rs. 100 cr), Tier 2 (Rs. 100 cr to Rs. 1,000 cr), Tier 3 (Rs. 1,000 cr to Rs. 10,000 cr), and Tier 4 (deposits above Rs. 10,000 cr).",
            "exp_ta": "2022-ல் என்.எஸ். விஸ்வநாதன் குழு பரிந்துரையை ஏற்று, ரிசர்வ் வங்கி UCB-களை வைப்புத்தொகை அடிப்படையில் 4 அடுக்குகளாக வகைப்படுத்தியது: அடுக்கு 1 (ரூ. 100 கோடி வரை), அடுக்கு 2 (ரூ. 100 முதல் 1,000 கோடி வரை), அடுக்கு 3 (ரூ. 1,000 முதல் 10,000 கோடி வரை), மற்றும் அடுக்கு 4 (ரூ. 10,000 கோடிக்கு மேல்).",
            "why_a_en": "Correct. Exactly 4 Tiers based on deposit size.",
            "why_a_ta": "சரி. வைப்புத்தொகை அடிப்படையில் சரியாக 4 அடுக்குகள்.",
            "why_b_en": "Incorrect. Older framework had 2 tiers; revised has 4.",
            "why_b_ta": "தவறு. பழைய முறையில் 2 அடுக்குகள் இருந்தன; திருத்தப்பட்ட முறையில் 4.",
            "why_c_en": "Incorrect. 3 tiers is incorrect.",
            "why_c_ta": "தவறு. 3 அடுக்குகள் தவறானது.",
            "why_d_en": "Incorrect. 5 tiers is incorrect.",
            "why_d_ta": "தவறு. 5 அடுக்குகள் தவறானது.",
            "tip_en": "Tier 1 UCBs enjoy simpler regulatory capital requirements (9% CRAR), while Tier 2 to 4 UCBs must maintain 12% CRAR.",
            "tip_ta": "அடுக்கு 1 வங்கிகளுக்கு மூலதன நிறைவு விகிதம் (CRAR) 9%, ஆனால் அடுக்கு 2 முதல் 4 வரை உள்ள வங்கிகளுக்கு 12% ஆகும்.",
            "fact_en": "The largest UCBs in India (such as Saraswat Bank and Cosmos Bank) fall in Tier 4.",
            "fact_ta": "இந்தியாவின் மிகப்பெரிய கூட்டுறவு வங்கிகள் (சரஸ்வத் வங்கி, காஸ்மோஸ் வங்கி போன்றவை) அடுக்கு 4-ல் வருகின்றன."
        },

        # 8. Statutory Reserve Fund Percentage
        {
            "subtopic": "Financial Architecture of Cooperatives",
            "stem_en": "Under state cooperative societies legislation (including Section 72 of the Tamil Nadu Co-operative Societies Act, 1983), what minimum percentage of the net profit must be compulsorily transferred to the Reserve Fund before declaring dividends?",
            "stem_ta": "மாநிலக் கூட்டுறவுச் சட்டங்களின் கீழ் (தமிழ்நாடு கூட்டுறவு சங்கங்கள் சட்டம் 1983-ன் பிரிவு 72 உட்பட), ஈவுத்தொகை அறிவிப்பதற்கு முன் நிகர லாபத்தில் குறைந்தபட்சம் எத்தனை சதவீதம் கட்டாயமாக சேம நிதிக்கு (Reserve Fund) மாற்றப்பட வேண்டும்?",
            "options": [
                ("Not less than 25% of net profits", "நிகர லாபத்தில் 25%-க்கு குறையாமல்"),
                ("Not less than 10% of net profits", "நிகர லாபத்தில் 10%-க்கு குறையாமல்"),
                ("Not less than 50% of net profits", "நிகர லாபத்தில் 50%-க்கு குறையாமல்"),
                ("Not less than 5% of net profits", "நிகர லாபத்தில் 5%-க்கு குறையாமல்")
            ],
            "correct_key": "A",
            "exp_en": "Section 72(1)(a) of the TN Act 1983 and standard cooperative statutes stipulate that every co-operative society which earns a net profit shall transfer not less than 25% of such net profit to the statutory Reserve Fund to ensure capital adequacy and solvency.",
            "exp_ta": "1983 TN சட்டத்தின் பிரிவு 72(1)(a) மற்றும் நிலையான கூட்டுறவுச் சட்டங்கள், நிகர லாபம் ஈட்டும் ஒவ்வொரு கூட்டுறவு சங்கமும் நிதி நிலைத்தன்மையை உறுதி செய்வதற்காக தனது நிகர லாபத்தில் குறைந்தபட்சம் 25%-ஐ சட்டப்பூர்வ சேம நிதிக்கு மாற்ற வேண்டும் என்று விதிக்கின்றன.",
            "why_a_en": "Correct. Mandatory 25% transfer to the statutory Reserve Fund.",
            "why_a_ta": "சரி. சட்டப்பூர்வ சேம நிதிக்கு கட்டாயமாக 25% மாற்றப்பட வேண்டும்.",
            "why_b_en": "Incorrect. 10% is below the statutory threshold.",
            "why_b_ta": "தவறு. 10% சட்டப்பூர்வ வரம்பை விடக் குறைவு.",
            "why_c_en": "Incorrect. 50% is not the minimum statutory requirement.",
            "why_c_ta": "தவறு. 50% குறைந்தபட்ச தேவை அல்ல.",
            "why_d_en": "Incorrect. 5% is incorrect.",
            "why_d_ta": "தவறு. 5% தவறானது.",
            "tip_en": "Cooperative Reserve Fund is indivisible and cannot be distributed among members even upon dissolution.",
            "tip_ta": "கூட்டுறவு சேம நிதி பிரிக்க முடியாதது மற்றும் சங்கம் கலைக்கப்பட்டாலும் உறுப்பினர்களுக்குப் பகிர்ந்தளிக்க முடியாது.",
            "fact_en": "The Reserve Fund belongs to the society in perpetuity, protecting against unforeseen future losses.",
            "fact_ta": "சேம நிதி சங்கத்திற்கு நிரந்தரமாகச் சொந்தமானது, எதிர்பாராத எதிர்கால இழப்புகளிலிருந்து பாதுகாக்கிறது."
        },

        # 9. Special Officer Appointment in Tamil Nadu (Section 89A)
        {
            "subtopic": "Tamil Nadu Cooperative Governance",
            "stem_en": "Under Section 89A of the Tamil Nadu Co-operative Societies Act, 1983, when elections cannot be held or the board cannot be reconstituted, who can be appointed by the Government to manage the affairs of a cooperative society?",
            "stem_ta": "தமிழ்நாடு கூட்டுறவு சங்கங்கள் சட்டம் 1983-ன் பிரிவு 89A-ன் கீழ், தேர்தல்களை நடத்த முடியாத போது அல்லது வாரியத்தை மீண்டும் அமைக்க முடியாத போது, கூட்டுறவு சங்கத்தின் விவகாரங்களை நிர்வகிக்க அரசால் யார் நியமிக்கப்படலாம்?",
            "options": [
                ("A Special Officer", "ஒரு தனி அலுவலர் (Special Officer)"),
                ("The Chief Justice of Madras High Court", "மெட்ராஸ் உயர் நீதிமன்றத் தலைமை நீதிபதி"),
                ("The Leader of Opposition", "எதிர்க்கட்சித் தலைவர்"),
                ("A private corporate receiver", "தனியார் கார்ப்பரேட் ரிசீவர்")
            ],
            "correct_key": "A",
            "exp_en": "Section 89A was inserted into the TN Act 1983 to empower the Government to appoint a 'Special Officer' (usually a departmental officer from cooperative service) to manage the affairs of a society where elections could not be held or the board ceased to exist.",
            "exp_ta": "1983 TN சட்டத்தில் சேர்க்கப்பட்ட பிரிவு 89A, தேர்தல்களை நடத்த முடியாத போது அல்லது வாரியம் காலாவதியான போது சங்கத்தின் விவகாரங்களை நிர்வகிக்க 'தனி அலுவலரை' (Special Officer - பொதுவாக கூட்டுறவுத் துறை அதிகாரி) நியமிக்க அரசுக்கு அதிகாரம் அளிக்கிறது.",
            "why_a_en": "Correct. Special Officer manages the society under Section 89A.",
            "why_a_ta": "சரி. பிரிவு 89A-ன் கீழ் தனி அலுவலர் சங்கத்தை நிர்வகிக்கிறார்.",
            "why_b_en": "Incorrect. High Court judges do not manage cooperative societies.",
            "why_b_ta": "தவறு. உயர் நீதிமன்ற நீதிபதிகள் கூட்டுறவுகளை நிர்வகிப்பதில்லை.",
            "why_c_en": "Incorrect. Leader of Opposition has no administrative executive appointment power.",
            "why_c_ta": "தவறு. எதிர்க்கட்சித் தலைவருக்கு நிர்வாக நியமன அதிகாரம் இல்லை.",
            "why_d_en": "Incorrect. Special Officers are public servants from cooperative audit/administration.",
            "why_d_ta": "தவறு. தனி அலுவலர்கள் அரசுப் பணியாளர்கள்.",
            "tip_en": "Though widely used historically, prolonged appointment of Special Officers undermines grassroots cooperative democracy.",
            "tip_ta": "வரலாற்று ரீதியாகப் பயன்படுத்தப்பட்டாலும், நீண்ட காலம் தனி அலுவலர்களை நியமிப்பது கூட்டுறவு ஜனநாயகத்தைப் பலவீனப்படுத்துகிறது.",
            "fact_en": "Special Officer possesses all the powers of the elected Board of Directors under the Act.",
            "fact_ta": "சட்டத்தின் கீழ் தேர்ந்தெடுக்கப்பட்ட இயக்குநர் வாரியத்தின் அனைத்து அதிகாரங்களையும் தனி அலுவலர் கொண்டுள்ளார்."
        },

        # 10. Multi-State Cooperative Societies Act Section 84 (Arbitration)
        {
            "subtopic": "Dispute Resolution - Multi-State",
            "stem_en": "Under Section 84 of the Multi-State Co-operative Societies Act, 2002, how are disputes touching the constitution, management, or business of a multi-state cooperative society resolved?",
            "stem_ta": "2002-ஆம் ஆண்டின் பல்மாநில கூட்டுறவு சங்கங்கள் சட்டத்தின் பிரிவு 84-ன் கீழ், ஒரு பல்மாநில கூட்டுறவு சங்கத்தின் அமைப்பு, மேலாண்மை அல்லது வணிகம் தொடர்பான சர்ச்சைகள் எவ்வாறு தீர்க்கப்படுகின்றன?",
            "options": [
                ("By reference to arbitration under the Arbitration and Conciliation Act, 1996 to the Central Registrar or an arbitrator appointed by him", "1996-ஆம் ஆண்டின் நடுவர் மற்றும் சமரசச் சட்டத்தின் கீழ் மத்தியப் பதிவாளரிடமோ அல்லது அவரால் நியமிக்கப்பட்ட நடுவரிடமோ நடுவர் தீர்ப்பிற்கு அனுப்பி வைப்பதன் மூலம்"),
                ("By trial before a military court martial", "ராணுவ நீதிமன்றத்தில் விசாரணை நடத்துவதன் மூலம்"),
                ("By a mandatory referendum among all Indian voters", "அனைத்து இந்திய வாக்காளர்களிடையே கட்டாய வாக்கெடுப்பு நடத்துவதன் மூலம்"),
                ("Exclusively by the International Court of Justice (ICJ) at The Hague", "ஹேக்கில் உள்ள சர்வதேச நீதிமன்றத்தால் (ICJ) மட்டுமே")
            ],
            "correct_key": "A",
            "exp_en": "Section 84 of the MSCS Act, 2002 provides that notwithstanding anything contained in any other law, any dispute touching the constitution, management, or business of a multi-state co-operative society shall be referred to arbitration under the Arbitration and Conciliation Act, 1996.",
            "exp_ta": "2002 MSCS சட்டத்தின் பிரிவு 84, வேறு எந்தச் சட்டத்தில் என்ன கூறப்பட்டிருந்தாலும், ஒரு பல்மாநில கூட்டுறவு சங்கத்தின் அமைப்பு, மேலாண்மை அல்லது வணிகம் தொடர்பான எந்தவொரு சர்ச்சையும் 1996-ஆம் ஆண்டின் நடுவர் மற்றும் சமரசச் சட்டத்தின் கீழ் நடுவர் தீர்ப்பிற்கு அனுப்பப்பட வேண்டும் என்று கூறுகிறது.",
            "why_a_en": "Correct. Statutory arbitration under the Arbitration and Conciliation Act, 1996.",
            "why_a_ta": "சரி. 1996-ஆம் ஆண்டின் நடுவர் மற்றும் சமரசச் சட்டத்தின் கீழ் சட்டப்பூர்வ நடுவர் தீர்ப்பு.",
            "why_b_en": "Incorrect. Military court martial has no jurisdiction over cooperatives.",
            "why_b_ta": "தவறு. ராணுவ நீதிமன்றத்திற்கு கூட்டுறவுகளில் அதிகார வரம்பு இல்லை.",
            "why_c_en": "Incorrect. National referendum is not a dispute mechanism.",
            "why_c_ta": "தவறு. தேசிய வாக்கெடுப்பு சர்ச்சை தீர்வு முறை அல்ல.",
            "why_d_en": "Incorrect. ICJ handles disputes between sovereign nation-states.",
            "why_d_ta": "தவறு. ICJ இறையாண்மை கொண்ட நாடுகளுக்கு இடையேயான வழக்குகளைக் கையாள்கிறது.",
            "tip_en": "Civil court jurisdiction is expressly ousted by Section 84(5) of the MSCS Act.",
            "tip_ta": "MSCS சட்டத்தின் பிரிவு 84(5) மூலம் சிவில் நீதிமன்றங்களின் அதிகார வரம்பு வெளிப்படையாக நீக்கப்பட்டுள்ளது.",
            "fact_en": "The arbitrator's award is enforceable as a decree of a civil court.",
            "fact_ta": "நடுவரின் தீர்ப்பு ஒரு சிவில் நீதிமன்றத்தின் ஆணையைப் போலவே செயல்படுத்தத்தக்கதாகும்."
        },

        # 11. Cooperative Societies Winding Up and Liquidation
        {
            "subtopic": "Winding Up and Liquidation",
            "stem_en": "When an order for winding up (liquidation) of a cooperative society is passed under cooperative law, what official is appointed to take custody of all property, assets, and actionable claims?",
            "stem_ta": "கூட்டுறவுச் சட்டத்தின் கீழ் ஒரு கூட்டுறவு சங்கத்தைக் கலைப்பதற்கான (லிக்விடேஷன்) உத்தரவு பிறப்பிக்கப்படும் போது, அனைத்து சொத்துக்கள் மற்றும் நிதி கோரிக்கைகளை தன்வசம் எடுத்துக்கொள்ள நியமிக்கப்படும் அதிகாரி யார்?",
            "options": [
                ("A Liquidator", "ஒரு கலைப்பாளர் (Liquidator)"),
                ("The Official Liquidator of the High Court under Companies Act", "நிறுவனங்கள் சட்டத்தின் கீழ் உயர் நீதிமன்றத்தின் அதிகாரப்பூர்வ கலைப்பாளர்"),
                ("The Comptroller and Auditor General directly", "தலைமை கணக்குத் தணிக்கையாளர் நேரடியாக"),
                ("The local Village Administrative Officer (VAO)", "உள்ளூர் கிராம நிர்வாக அலுவலர் (VAO)")
            ],
            "correct_key": "A",
            "exp_en": "When the Registrar orders winding up under state cooperative law (e.g. Section 137 of TN Act 1983) or MSCS Act, a Liquidator is appointed under Section 138 to realize assets, settle creditor liabilities, discharge loans, and distribute any remaining surplus according to statutory priority.",
            "exp_ta": "மாநிலக் கூட்டுறவுச் சட்டம் (எ.கா. 1983 TN சட்டத்தின் பிரிவு 137) அல்லது MSCS சட்டத்தின் கீழ் பதிவாளர் கலைத்தல் உத்தரவை பிறப்பிக்கும் போது, சொத்துக்களை விற்று, கடன்களைத் தீர்த்து, உபரியைப் பகிர்ந்தளிக்க பிரிவு 138-ன் கீழ் ஒரு 'கலைப்பாளர்' (Liquidator) நியமிக்கப்படுகிறார்.",
            "why_a_en": "Correct. A statutory Liquidator is appointed by the Registrar.",
            "why_a_ta": "சரி. பதிவாளரால் சட்டப்பூர்வ கலைப்பாளர் நியமிக்கப்படுகிறார்.",
            "why_b_en": "Incorrect. Company Official Liquidator handles corporate insolvencies, not cooperatives.",
            "why_b_ta": "தவறு. நிறுவன அதிகாரப்பூர்வ கலைப்பாளர் கார்ப்பரேட் நிறுவனங்களைக் கையாள்கிறார்.",
            "why_c_en": "Incorrect. CAG does not act as cooperative liquidator.",
            "why_c_ta": "தவறு. CAG கூட்டுறவு கலைப்பாளராகச் செயல்படுவதில்லை.",
            "why_d_en": "Incorrect. VAO is a grassroots revenue officer.",
            "why_d_ta": "தவறு. VAO வருவாய்த்துறை அதிகாரி.",
            "tip_en": "Priority of asset distribution in liquidation: Costs of liquidation -> Government dues -> Wages of employees -> Secured creditors -> Unsecured creditors -> Share capital.",
            "tip_ta": "சொத்து பகிர்வு முன்னுரிமை: கலைத்தல் செலவுகள் -> அரசு நிலுவைகள் -> பணியாளர் ஊதியம் -> பாதுகாக்கப்பட்ட கடன்கள் -> பங்கு மூலதனம்.",
            "fact_en": "Once liquidation is completed, the registration of the society is formally cancelled.",
            "fact_ta": "கலைத்தல் நடவடிக்கைகள் முடிந்ததும், சங்கத்தின் பதிவு அதிகாரப்பூர்வமாக ரத்து செய்யப்படுகிறது."
        },

        # 12. Primary Handloom Weavers Apex Organization (Co-optex) Structure
        {
            "subtopic": "Tamil Nadu Cooperative Ecosystem",
            "stem_en": "What is the organizational tier structure of handloom weaving cooperatives in Tamil Nadu?",
            "stem_ta": "தமிழ்நாட்டில் கைத்தறி நெசவு கூட்டுறவுகளின் நிறுவன அடுக்கு அமைப்பு என்ன?",
            "options": [
                ("Two-tier structure: Primary Handloom Weavers Cooperative Societies at grassroots and Co-optex at State Apex level", "இரண்டு அடுக்கு அமைப்பு: அடிமட்டத்தில் தொடக்க கைத்தறி நெசவாளர் கூட்டுறவு சங்கங்கள் மற்றும் மாநில அளவில் கோ-ஆப்டெக்ஸ் தலைமை அமைப்பு"),
                ("Four-tier structure including international sales offices in every country", "ஒவ்வொரு நாட்டிலும் சர்வதேச விற்பனை அலுவலகங்கள் உட்பட நான்கு அடுக்கு அமைப்பு"),
                ("Single unitary society with direct individual membership across Tamil Nadu", "தமிழ்நாடு முழுவதும் நேரடி தனிநபர் உறுப்பினர்களைக் கொண்ட ஒற்றை அமைப்பு"),
                ("Operated under municipal corporations without cooperative registration", "கூட்டுறவுப் பதிவின்றி மாநகராட்சிகளின் கீழ் செயல்படும் அமைப்பு")
            ],
            "correct_key": "A",
            "exp_en": "Handloom cooperatives in Tamil Nadu follow a 2-tier federal structure: Primary Handloom Weavers Cooperative Societies (PWCS) at the base village/town level where individual weavers are members, federated into the Tamil Nadu Handloom Weavers' Co-operative Society Limited (Co-optex) as the apex marketing organization.",
            "exp_ta": "தமிழ்நாட்டில் கைத்தறி கூட்டுறவுகள் 2 அடுக்கு கூட்டாட்சி அமைப்பைப் பின்பற்றுகின்றன: தனிநபர் நெசவாளர்கள் உறுப்பினர்களாக உள்ள கிராம/நகர அளவிலான தொடக்க கைத்தறி நெசவாளர் கூட்டுறவு சங்கங்கள் (PWCS) மற்றும் உச்ச சந்தைப்படுத்தல் அமைப்பான கோ-ஆப்டெக்ஸ் (Co-optex).",
            "why_a_en": "Correct. 2-tier structure: Primary societies -> Co-optex Apex.",
            "why_a_ta": "சரி. 2 அடுக்கு அமைப்பு: தொடக்கச் சங்கங்கள் -> கோ-ஆப்டெக்ஸ் தலைமை அமைப்பு.",
            "why_b_en": "Incorrect. There is no four-tier international structure.",
            "why_b_ta": "தவறு. 4 அடுக்கு அமைப்பு இல்லை.",
            "why_c_en": "Incorrect. It is federal, not a single unitary society.",
            "why_c_ta": "தவறு. இது கூட்டாட்சி அமைப்பாகும், ஒற்றை அமைப்பு அல்ல.",
            "why_d_en": "Incorrect. They are registered cooperatives under the TN Cooperative Societies Act.",
            "why_d_ta": "தவறு. அவை TN கூட்டுறவு சங்கங்கள் சட்டத்தின் கீழ் பதிவு செய்யப்பட்டவை.",
            "tip_en": "Co-optex operates over 150 retail showrooms across India.",
            "tip_ta": "கோ-ஆப்டெக்ஸ் இந்தியா முழுவதும் 150-க்கும் மேற்பட்ட விற்பனை நிலையங்களை இயக்குகிறது.",
            "fact_en": "Co-optex markets GI-tagged handlooms like Kanchipuram Silk, Arani Silk, Madurai Sungudi, and Bhavani Jamakkalam.",
            "fact_ta": "காஞ்சிபுரம் பட்டு, ஆரணி பட்டு, மதுரை சுங்குடி மற்றும் பவானி ஜமக்காளம் போன்ற புவிசார் குறியீடு பெற்ற துணிகளை கோ-ஆப்டெக்ஸ் விற்பனை செய்கிறது."
        },

        # 13. State Co-operative Union Functions
        {
            "subtopic": "Tamil Nadu Cooperative Ecosystem",
            "stem_en": "What is the specialized statutory role of the Tamil Nadu Co-operative Union (TNCU) in the state cooperative institutional framework?",
            "stem_ta": "மாநிலக் கூட்டுறவு நிறுவனக் கட்டமைப்பில் தமிழ்நாடு கூட்டுறவு ஒன்றியத்தின் (TNCU) சிறப்புச் சட்டப்பூர்வப் பணி என்ன?",
            "options": [
                ("Propagating cooperative principles, conducting member education, administering Cooperative Training Institutes (CTIs), and publishing cooperative journals", "கூட்டுறவுக் கொள்கைகளைப் பரப்புதல், உறுப்பினர் கல்வி நடத்துதல், கூட்டுறவுப் பயிற்சி நிலையங்களை (CTIs) நிர்வகித்தல், மற்றும் கூட்டுறவு இதழ்களை வெளியிடுதல்"),
                ("Issuing sovereign commercial loans to foreign governments", "வெளிநாட்டு அரசுகளுக்கு வர்த்தகக் கடன்களை வழங்குவது"),
                ("Controlling Indian naval fleet deployments", "இந்திய கடற்படைப் பிரிவுகளைக் கட்டுப்படுத்துவது"),
                ("Regulating nuclear power plant safety standards", "அணுமின் நிலைய பாதுகாப்புத் தரங்களை ஒழுங்குபடுத்துவது")
            ],
            "correct_key": "A",
            "exp_en": "The Tamil Nadu Co-operative Union (TNCU), registered in 1914 as the Madras Provincial Co-operative Union, functions as the non-credit apex promotional organization for cooperative education, running Institutes of Cooperative Management (ICMs) and publishing the monthly magazine 'Kooturavu'.",
            "exp_ta": "1914-ல் மெட்ராஸ் மாகாண கூட்டுறவு ஒன்றியமாகப் பதிவு செய்யப்பட்ட தமிழ்நாடு கூட்டுறவு ஒன்றியம் (TNCU), கூட்டுறவுக் கல்விக்கான கடன் சாரா உச்ச ஊக்குவிப்பு அமைப்பாகச் செயல்படுகிறது; இது கூட்டுறவு மேலாண்மை நிலையங்களை (ICMs) நடத்துகிறது மற்றும் 'கூட்டுறவு' என்ற மாத இதழை வெளியிடுகிறது.",
            "why_a_en": "Correct. TNCU is the apex educational and promotional union in Tamil Nadu.",
            "why_a_ta": "சரி. TNCU தமிழ்நாட்டின் தலைமைக் கல்வி மற்றும் ஊக்குவிப்பு ஒன்றியமாகும்.",
            "why_b_en": "Incorrect. Foreign loans are sovereign central powers.",
            "why_b_ta": "தவறு. வெளிநாட்டுக் கடன் மத்திய அரசின் பணி.",
            "why_c_en": "Incorrect. Navy is under Ministry of Defence.",
            "why_c_ta": "தவறு. கடற்படை பாதுகாப்பு அமைச்சகத்தின் கீழ் உள்ளது.",
            "why_d_en": "Incorrect. AERB regulates nuclear safety.",
            "why_d_ta": "தவறு. AERB அணுசக்தி பாதுகாப்பைக் கண்காணிக்கிறது.",
            "tip_en": "TNCU administers the Cooperative Education Fund under Section 72 of the TN Act 1983.",
            "tip_ta": "TNCU 1983 TN சட்டத்தின் பிரிவு 72-ன் கீழ் கூட்டுறவுக் கல்வி நிதியை நிர்வகிக்கிறது.",
            "fact_en": "TNCU conducts diploma courses in cooperative management across district training institutes.",
            "fact_ta": "TNCU மாவட்டப் பயிற்சி நிலையங்கள் மூலம் கூட்டுறவு மேலாண்மையில் டிப்ளமோ படிப்புகளை நடத்துகிறது."
        },

        # 14. Cooperative Audit Department Independence
        {
            "subtopic": "Tamil Nadu Cooperative Governance",
            "stem_en": "In Tamil Nadu, why was the Department of Co-operative Audit separated from the administrative Department of Co-operative Societies in 1981?",
            "stem_ta": "தமிழ்நாட்டில், 1981-ல் கூட்டுறவுத் தணிக்கைத் துறையானது கூட்டுறவுச் சங்கங்களின் நிர்வாகத் துறையிலிருந்து ஏன் தனியாகப் பிரிக்கப்பட்டது?",
            "options": [
                ("To ensure independent, objective, and unbiased audit of cooperative accounts free from administrative conflict of interest", "நிர்வாக நலன் முரண்பாடுகள் இன்றி கூட்டுறவுக் கணக்குகளின் சுதந்திரமான, பாரபட்சமற்ற மற்றும் புறநிலையான தணிக்கையை உறுதி செய்ய"),
                ("To abolish all cooperative societies in the state", "மாநிலத்தில் உள்ள அனைத்து கூட்டுறவு சங்கங்களையும் ஒழிப்பதற்காக"),
                ("To privatize all rural cooperative banks into private companies", "அனைத்து கிராமப்புற கூட்டுறவு வங்கிகளையும் தனியார் நிறுவனங்களாக மாற்றுவதற்கு"),
                ("To transfer all cooperative assets to the central government", "அனைத்து கூட்டுறவு சொத்துக்களையும் மத்திய அரசுக்கு மாற்றுவதற்கு")
            ],
            "correct_key": "A",
            "exp_en": "On the recommendations of various committees and to avoid conflict of interest where the administering department audits its own actions, the Government of Tamil Nadu separated the Department of Co-operative Audit under an independent Director of Co-operative Audit in 1981.",
            "exp_ta": "நிர்வாகம் செய்யும் துறையே தனது சொந்த நடவடிக்கைகளைத் தணிக்கை செய்யும் நலன் முரண்பாட்டைத் தவிர்ப்பதற்காகவும், பல்வேறு குழுக்களின் பரிந்துரைகளின் அடிப்படையிலும், 1981-ல் தமிழ்நாடு அரசு ஒரு சுதந்திரமான கூட்டுறவுத் தணிக்கை இயக்குநரின் கீழ் கூட்டுறவுத் தணிக்கைத் துறையைப் பிரித்தது.",
            "why_a_en": "Correct. Ensuring independent, conflict-free cooperative auditing.",
            "why_a_ta": "சரி. சுதந்திரமான, முரண்பாடற்ற கூட்டுறவுத் தணிக்கையை உறுதி செய்வதற்காக.",
            "why_b_en": "Incorrect. Separation strengthens cooperatives, not abolishes them.",
            "why_b_ta": "தவறு. கூட்டுறவை ஒழிப்பது நோக்கம் அல்ல.",
            "why_c_en": "Incorrect. Privatization was never the goal.",
            "why_c_ta": "தவறு. தனியார்மயமாக்கல் நோக்கம் அல்ல.",
            "why_d_en": "Incorrect. Cooperatives remain under state jurisdiction.",
            "why_d_ta": "தவறு. கூட்டுறவுகள் மாநில அதிகார வரம்பிலேயே உள்ளன.",
            "tip_en": "Article 243ZM(1) subsequently constitutionalized this principle of independent empanelment of auditors.",
            "tip_ta": "சரத்து 243ZM(1) பின்னர் சுதந்திரமான தணிக்கையாளர்கள் பட்டியலிடப்பட வேண்டும் என்ற இக்கொள்கையை அரசியலமைப்பு ரீதியாக உறுதிப்படுத்தியது.",
            "fact_en": "Tamil Nadu was a pioneer in establishing an independent Cooperative Audit Directorate.",
            "fact_ta": "சுதந்திரமான கூட்டுறவு தணிக்கை இயக்ககத்தை நிறுவியதில் தமிழ்நாடு ஒரு முன்னோடியாகும்."
        },

        # 15. Urban Cooperative Banks Multi-State Registration Threshold
        {
            "subtopic": "Multi-State Co-operative Banking",
            "stem_en": "When an Urban Co-operative Bank (UCB) operating in Tamil Nadu desires to open branches in neighboring Kerala and Karnataka, under which legislation must it register?",
            "stem_ta": "தமிழ்நாட்டில் செயல்படும் ஒரு நகர்ப்புறக் கூட்டுறவு வங்கி (UCB) அண்டை மாநிலங்களான கேரளா மற்றும் கர்நாடகாவில் கிளைகளைத் திறக்க விரும்பினால், அது எந்தச் சட்டத்தின் கீழ் பதிவு செய்யப்பட வேண்டும்?",
            "options": [
                ("Multi-State Co-operative Societies Act, 2002 under the Central Registrar", "மத்தியப் பதிவாளரின் கீழ் 2002-ஆம் ஆண்டின் பல்மாநில கூட்டுறவு சங்கங்கள் சட்டம்"),
                ("Tamil Nadu Co-operative Societies Act, 1983 exclusively", "தமிழ்நாடு கூட்டுறவு சங்கங்கள் சட்டம் 1983 மட்டுமே"),
                ("Companies Act, 2013 as a public limited company", "பொது வரையறுக்கப்பட்ட நிறுவனமாக நிறுவனங்கள் சட்டம் 2013"),
                ("Foreign Exchange Management Act, 1999", "அந்நியச் செலாவணி மேலாண்மைச் சட்டம் 1999")
            ],
            "correct_key": "A",
            "exp_en": "When a cooperative bank expands its area of operation and membership beyond a single State into two or more States, it ceases to be governed by the single-state act and must register under the Multi-State Co-operative Societies Act, 2002 under Entry 44 of Union List, falling under the jurisdiction of the Central Registrar of Co-operative Societies.",
            "exp_ta": "ஒரு கூட்டுறவு வங்கி தனது செயல்பாட்டுப் பகுதி மற்றும் உறுப்பினர் சேர்க்கையை ஒற்றை மாநிலத்தைத் தாண்டி இரண்டு அல்லது அதற்கு மேற்பட்ட மாநிலங்களுக்கு விரிவுபடுத்தும் போது, அது மாநிலச் சட்டத்தின் கீழ் செயல்பட முடியாது; அது மத்தியப் பட்டியல் பதிவு 44-ன் கீழ் உள்ள 2002 பல்மாநில கூட்டுறவு சங்கங்கள் சட்டத்தின் கீழ் மத்தியப் பதிவாளரிடம் பதிவு செய்யப்பட வேண்டும்.",
            "why_a_en": "Correct. Expansion to multiple states requires MSCS Act registration.",
            "why_a_ta": "சரி. பல மாநிலங்களுக்கு விரிவடையும் போது MSCS சட்டத்தின் கீழ் பதிவு செய்ய வேண்டும்.",
            "why_b_en": "Incorrect. State Acts have extra-territorial limitations and cannot operate in other states.",
            "why_b_ta": "தவறு. மாநிலச் சட்டங்கள் பிற மாநிலங்களில் செல்லாது.",
            "why_c_en": "Incorrect. Cooperative identity is retained under MSCS Act, not Companies Act.",
            "why_c_ta": "தவறு. கூட்டுறவு அந்தஸ்து MSCS சட்டத்தின் கீழ் தக்கவைக்கப்படுகிறது.",
            "why_d_en": "Incorrect. FEMA governs cross-border foreign exchange, not interstate branching.",
            "why_d_ta": "தவறு. ஃபெமா வெளிநாட்டு செலாவணியைக் கையாள்கிறது.",
            "tip_en": "In addition to MSCS Act registration, branch expansion requires prior licensing approval from RBI under Section 23 of Banking Regulation Act.",
            "tip_ta": "MSCS பதிவுக்கு கூடுதலாக, வங்கி ஒழுங்குமுறைச் சட்டத்தின் பிரிவு 23-ன் கீழ் ரிசர்வ் வங்கியின் முன் அனுமதியும் தேவை.",
            "fact_en": "Saraswat Bank, Cosmos Bank, and SVC Bank are premier multi-state cooperative banks in India.",
            "fact_ta": "சரஸ்வத் வங்கி மற்றும் காஸ்மோஸ் வங்கி ஆகியவை இந்தியாவின் முதன்மை பல்மாநில கூட்டுறவு வங்கிகளாகும்."
        },

        # 16. Cooperative Identity Statement (1995 Manchester)
        {
            "subtopic": "Core Principles of Cooperation",
            "stem_en": "The universally accepted Statement on the Co-operative Identity was adopted by the International Co-operative Alliance (ICA) at which historic Congress?",
            "stem_ta": "உலகளவில் ஏற்றுக்கொள்ளப்பட்ட கூட்டுறவு அடையாள அறிக்கை எந்த வரலாற்று மாநாட்டில் சர்வதேச கூட்டுறவு கூட்டணியால் (ICA) ஏற்றுக்கொள்ளப்பட்டது?",
            "options": [
                ("1995 Manchester Centennial Congress", "1995 மான்செஸ்டர் நூற்றாண்டு மாநாடு"),
                ("1844 Rochdale Conference", "1844 ரோச்டேல் மாநாடு"),
                ("1966 Vienna Congress", "1966 வியன்னா மாநாடு"),
                ("1947 Geneva Conference", "1947 ஜெனிவா மாநாடு")
            ],
            "correct_key": "A",
            "exp_en": "The Statement on the Co-operative Identity was adopted at the Centennial Congress of the International Co-operative Alliance held in Manchester, United Kingdom in September 1995, containing the official definition of a cooperative, cooperative values, and the 7 revised principles.",
            "exp_ta": "கூட்டுறவு அடையாள அறிக்கை 1995 செப்டம்பரில் இங்கிலாந்தின் மான்செஸ்டரில் நடைபெற்ற சர்வதேச கூட்டுறவு கூட்டணியின் நூற்றாண்டு மாநாட்டில் ஏற்றுக்கொள்ளப்பட்டது; இது கூட்டுறவின் அதிகாரப்பூர்வ வரையறை, கூட்டுறவு மதிப்புகள் மற்றும் 7 திருத்தப்பட்ட கொள்கைகளைக் கொண்டுள்ளது.",
            "why_a_en": "Correct. 1995 Manchester Centennial Congress adopted the current 7 principles.",
            "why_a_ta": "சரி. 1995 மான்செஸ்டர் நூற்றாண்டு மாநாடே தற்போதைய 7 கொள்கைகளை ஏற்றுக்கொண்டது.",
            "why_b_en": "Incorrect. 1844 was the founding of Rochdale Pioneers.",
            "why_b_ta": "தவறு. 1844 ரோச்டேல் முன்னோடிகள் சங்கம் தொடங்கப்பட்ட ஆண்டு.",
            "why_c_en": "Incorrect. 1966 Congress was held in Vienna (adopted 6 principles).",
            "why_c_ta": "தவறு. 1966 மாநாடு வியன்னாவில் நடைபெற்றது (6 கொள்கைகள்).",
            "why_d_en": "Incorrect. 1947 Geneva was GATT conference.",
            "why_d_ta": "தவறு. 1947 ஜெனிவா GATT மாநாடு.",
            "tip_en": "Values of Cooperation: Self-help, self-responsibility, democracy, equality, equity, and solidarity.",
            "tip_ta": "கூட்டுறவு மதிப்புகள்: சுயஉதவி, சுயபொறுப்பு, ஜனநாயகம், சமத்துவம், நேர்மை மற்றும் ஒற்றுமை.",
            "fact_en": "Ethical values include honesty, openness, social responsibility, and caring for others.",
            "fact_ta": "நேர்மை, வெளிப்படைத்தன்மை, சமூகப் பொறுப்பு மற்றும் பிறர் மீதான அக்கறை ஆகியவை இதன் நெறிமுறை மதிப்புகளாகும்."
        },

        # 17. National Cooperative Database
        {
            "subtopic": "Digital Transformation & Initiatives",
            "stem_en": "What is the primary purpose of the 'National Cooperative Database' developed by the Ministry of Cooperation in 2023?",
            "stem_ta": "2023-ல் கூட்டுறவு அமைச்சகத்தால் உருவாக்கப்பட்ட 'தேசியக் கூட்டுறவு தரவுத்தளத்தின்' (National Cooperative Database) முதன்மை நோக்கம் என்ன?",
            "options": [
                ("Mapping and capturing comprehensive sector-wise and district-wise data of over 8 lakh cooperatives across India for evidence-based policy making", "சான்றுகள் அடிப்படையிலான கொள்கை உருவாக்கத்திற்காக இந்தியா முழுவதும் உள்ள 8 லட்சத்திற்கும் மேற்பட்ட கூட்டுறவுகளின் துறை வாரியான மற்றும் மாவட்ட வாரியான விரிவான தரவுகளை வரைபடமாக்குதல்"),
                ("Privatizing all urban cooperative banks", "அனைத்து நகர்ப்புற கூட்டுறவு வங்கிகளையும் தனியார்மயமாக்குவது"),
                ("Replacing state registrars with artificial intelligence chatbots exclusively", "மாநிலப் பதிவாளர்களுக்குப் பதிலாக செயற்கை நுண்ணறிவு சாட்போட்களை மட்டுமே மாற்றுவது"),
                ("Merging all cooperatives into a single multinational bank", "அனைத்து கூட்டுறவுகளையும் ஒரே பன்னாட்டு வங்கியாக இணைப்பது")
            ],
            "correct_key": "A",
            "exp_en": "The Ministry of Cooperation developed the National Cooperative Database to map over 8 lakh cooperatives across primary, secondary, and tertiary tiers nationwide, identifying 'cooperative-dry' panchayats and enabling targeted expansion under the 'Sahakar Se Samriddhi' roadmap.",
            "exp_ta": "மத்திய கூட்டுறவு அமைச்சகம் நாடு முழுவதும் தொடக்க, இடைநிலை மற்றும் உச்ச அடுக்குகளில் உள்ள 8 லட்சத்திற்கும் மேற்பட்ட கூட்டுறவுகளை வரைபடமாக்கவும், கூட்டுறவே இல்லாத கிராம ஊராட்சிகளைக் கண்டறிந்து திட்டமிட்டு விரிவுபடுத்தவும் தேசிய கூட்டுறவு தரவுத்தளத்தை உருவாக்கியது.",
            "why_a_en": "Correct. National Cooperative Database captures census-level data of 8+ lakh cooperatives.",
            "why_a_ta": "சரி. தேசிய கூட்டுறவு தரவுத்தளம் 8 லட்சத்திற்கும் அதிகமான கூட்டுறவுகளின் விரிவான தரவுகளைக் கொண்டுள்ளது.",
            "why_b_en": "Incorrect. It is a data and planning tool, not a privatization scheme.",
            "why_b_ta": "தவறு. இது திட்டமிடல் கருவி, தனியார்மயமாக்கல் அல்ல.",
            "why_c_en": "Incorrect. AI chatbots do not replace statutory registrars.",
            "why_c_ta": "தவறு. AI பதிவாளர்களுக்கு மாற்றாகாது.",
            "why_d_en": "Incorrect. Decentralized federal diversity is maintained.",
            "why_d_ta": "தவறு. பரவலாக்கப்பட்ட கூட்டாட்சித் தன்மை தக்கவைக்கப்படுகிறது.",
            "tip_en": "Data covers PACS, dairy cooperatives, fisheries cooperatives, sugar mills, housing societies, and weavers cooperatives.",
            "tip_ta": "இத்தரவுகள் PACS, பால், மீன்வளம், சர்க்கரை ஆலைகள், வீட்டுவசதி மற்றும் நெசவாளர் கூட்டுறவுகளை உள்ளடக்கியது.",
            "fact_en": "The database revealed that over 2 lakh panchayats still lacked a PACS or dairy cooperative.",
            "fact_ta": "2 லட்சத்திற்கும் அதிகமான கிராம ஊராட்சிகளில் இன்னும் PACS அல்லது பால் கூட்டுறவு இல்லை என்பதை இந்த தரவுத்தளம் வெளிப்படுத்தியது."
        },

        # 18. PACS in Every Panchayat Scheme
        {
            "subtopic": "Government Initiatives - Vision 2027",
            "stem_en": "What is the national target set by the Government of India under the plan approved in February 2023 to expand primary cooperatives across uncovered areas?",
            "stem_ta": "மூடப்படாத பகுதிகளில் தொடக்கக் கூட்டுறவுகளை விரிவுபடுத்துவதற்காக 2023 பிப்ரவரியில் இந்திய அரசால் அங்கீகரிக்கப்பட்ட திட்டத்தின் கீழ் நிர்ணயிக்கப்பட்ட தேசிய இலக்கு என்ன?",
            "options": [
                ("Setting up 2 lakh new viable PACS, dairy, and fisheries cooperatives covering every uncovered Panchayat/village in 5 years", "5 ஆண்டுகளில் கூட்டுறவு இல்லாத ஒவ்வொரு பஞ்சாயத்து/கிராமத்தையும் உள்ளடக்கி 2 லட்சம் புதிய PACS, பால் மற்றும் மீன்வளக் கூட்டுறவுகளை அமைப்பது"),
                ("Setting up 10,000 corporate branches", "10,000 கார்ப்பரேட் கிளைகளை அமைப்பது"),
                ("Reducing the number of cooperatives by 50%", "கூட்டுறவுகளின் எண்ணிக்கையை 50% குறைப்பது"),
                ("Abolishing primary cooperatives in hill areas", "மலைப் பகுதிகளில் உள்ள தொடக்கக் கூட்டுறவுகளை ஒழிப்பது")
            ],
            "correct_key": "A",
            "exp_en": "On 15th February 2023, the Union Cabinet approved a plan to establish 2 lakh new multipurpose PACS, dairy, and fisheries cooperatives in uncovered Panchayats and villages over a period of 5 years, leveraging existing schemes of Ministry of Fisheries, Animal Husbandry and Dairying.",
            "exp_ta": "2023 பிப்ரவரி 15 அன்று, மத்திய அமைச்சரவை 5 ஆண்டுகளில் கூட்டுறவு இல்லாத கிராம ஊராட்சிகளில் 2 லட்சம் புதிய பல்நோக்கு PACS, பால் மற்றும் மீன்வளக் கூட்டுறவுகளை நிறுவும் திட்டத்திற்கு ஒப்புதல் அளித்தது.",
            "why_a_en": "Correct. 2 lakh new multipurpose primary cooperatives target by 2027-28.",
            "why_a_ta": "சரி. 2027-28-க்குள் 2 லட்சம் புதிய பல்நோக்கு தொடக்கக் கூட்டுறவுகளை அமைப்பதே இலக்காகும்.",
            "why_b_en": "Incorrect. Corporate branches are not the policy focus.",
            "why_b_ta": "தவறு. கார்ப்பரேட் கிளைகள் கொள்கை இலக்கு அல்ல.",
            "why_c_en": "Incorrect. Expansion, not contraction, is the policy.",
            "why_c_ta": "தவறு. விரிவாக்கமே கொள்கை, குறைப்பது அல்ல.",
            "why_d_en": "Incorrect. Hill areas receive special priority.",
            "why_d_ta": "தவறு. மலைப் பகுதிகளுக்கு சிறப்பு முன்னுரிமை அளிக்கப்படுகிறது.",
            "tip_en": "Ensures 'Every Village a Cooperative' (Panchayat level economic empowerment).",
            "tip_ta": "'ஒவ்வொரு கிராமத்திற்கும் ஒரு கூட்டுறவு' என்ற ஊரகப் பொருளாதார மேம்பாட்டை உறுதி செய்கிறது.",
            "fact_en": "Convergence with NABARD, NDDB, and NFDB is utilized for grassroots implementation.",
            "fact_ta": "அடிமட்ட அமலாக்கத்திற்கு நபார்டு, NDDB மற்றும் NFDB ஆகியவற்றின் ஒருங்கிணைப்பு பயன்படுத்தப்படுகிறது."
        },

        # 19. Difference between State and Multi-State Cooperative
        {
            "subtopic": "Comparative Legal Matrix",
            "stem_en": "Which of the following correctly describes the key jurisdictional difference between a State Co-operative Society and a Multi-State Co-operative Society?",
            "stem_ta": "பின்வருவனவற்றில் எது ஒரு மாநிலக் கூட்டுறவு சங்கத்திற்கும் ஒரு பல்மாநிலக் கூட்டுறவு சங்கத்திற்கும் இடையிலான முக்கிய அதிகார வரம்பு வேறுபாட்டைச் சரியாக விவரிக்கிறது?",
            "options": [
                ("State cooperatives fall under State List Entry 32 and are governed by the State Registrar, while Multi-State cooperatives fall under Union List Entry 44 and are governed by the Central Registrar", "மாநிலக் கூட்டுறவுகள் மாநிலப் பட்டியல் பதிவு 32-ன் கீழ் வந்து மாநிலப் பதிவாளரால் நிர்வகிக்கப்படுகின்றன; பல்மாநிலக் கூட்டுறவுகள் மத்தியப் பட்டியல் பதிவு 44-ன் கீழ் வந்து மத்தியப் பதிவாளரால் நிர்வகிக்கப்படுகின்றன"),
                ("State cooperatives are financed exclusively in gold, while Multi-State cooperatives use paper money", "மாநிலக் கூட்டுறவுகள் தங்கத்தில் மட்டுமே நிதியளிக்கப்படுகின்றன, பல்மாநிலக் கூட்டுறவுகள் காகிதப் பணத்தைப் பயன்படுத்துகின்றன"),
                ("Multi-State cooperatives have no board of directors", "பல்மாநிலக் கூட்டுறவுகளுக்கு இயக்குநர் வாரியமே கிடையாது"),
                ("State cooperatives cannot accept deposits from members", "மாநிலக் கூட்டுறவுகள் உறுப்பினர்களிடமிருந்து வைப்புகளை ஏற்க முடியாது")
            ],
            "correct_key": "A",
            "exp_en": "A single-state cooperative's objects are confined to one state, placing it squarely under Entry 32 of List II governed by the State Legislature and State Registrar. A multi-state cooperative's objects extend beyond one state, placing it under Entry 44 of List I governed by Parliament under the MSCS Act and Central Registrar.",
            "exp_ta": "ஒரு மாநிலக் கூட்டுறவின் நோக்கங்கள் ஒரு மாநிலத்திற்குள் மட்டுமே வரையறுக்கப்பட்டு, பட்டியல் II-ன் பதிவு 32-ன் கீழ் மாநிலச் சட்டமன்றம் மற்றும் மாநிலப் பதிவாளரால் நிர்வகிக்கப்படுகிறது. பல்மாநிலக் கூட்டுறவின் நோக்கங்கள் ஒன்றுக்கு மேற்பட்ட மாநிலங்களுக்கு விரிவடைந்து, பட்டியல் I-ன் பதிவு 44-ன் கீழ் நாடாளுமன்றத்தின் MSCS சட்டம் மற்றும் மத்தியப் பதிவாளரால் நிர்வகிக்கப்படுகிறது.",
            "why_a_en": "Correct. Fundamental constitutional and administrative jurisdictional distinction.",
            "why_a_ta": "சரி. அடிப்படையான அரசியலமைப்பு மற்றும் நிர்வாக அதிகார வரம்பு வேறுபாடு.",
            "why_b_en": "Incorrect. Currency modes are identical across India.",
            "why_b_ta": "தவறு. பணப் புழக்கம் நாடு முழுவதும் ஒன்றே.",
            "why_c_en": "Incorrect. Both have democratically elected boards of directors.",
            "why_c_ta": "தவறு. இரண்டிலுமே தேர்ந்தெடுக்கப்பட்ட இயக்குநர் வாரியங்கள் உண்டு.",
            "why_d_en": "Incorrect. Both accept deposits from members.",
            "why_d_ta": "தவறு. இரண்டும் உறுப்பினர்களிடமிருந்து வைப்புகளை ஏற்கின்றன.",
            "tip_en": "This constitutional dichotomy was the precise dividing line in the 2021 Rajendra Shah judgment.",
            "tip_ta": "இந்த அரசியலமைப்பு வேறுபாடே 2021 ராஜேந்திர ஷா தீர்ப்பின் முக்கியப் பிரிவுக் கோடாகும்.",
            "fact_en": "Part IX-B continues to apply to Multi-State Cooperatives, but state acts apply to State Cooperatives.",
            "fact_ta": "பகுதி IX-B பல்மாநிலக் கூட்டுறவுகளுக்குத் தொடர்கிறது, ஆனால் மாநிலக் கூட்டுறவுகளுக்கு மாநிலச் சட்டங்களே ஆளுகின்றன."
        },

        # 20. PACS Computerization Funding Pattern
        {
            "subtopic": "Government Initiatives - Funding",
            "stem_en": "What is the funding pattern between the Central Government and State Governments for the ongoing national PACS computerization project?",
            "stem_ta": "தற்போது நடைபெற்று வரும் தேசிய PACS கணினிமயமாக்கல் திட்டத்திற்கான மத்திய அரசு மற்றும் மாநில அரசுகளுக்கு இடையேயான நிதிப் பகிர்வு முறை என்ன?",
            "options": [
                ("60:40 for general states; 90:10 for North Eastern and Himalayan states; 100% Central for Union Territories", "பொது மாநிலங்களுக்கு 60:40; வடகிழக்கு மற்றும் இமயமலை மாநிலங்களுக்கு 90:10; யூனியன் பிரதேசங்களுக்கு 100% மத்திய அரசு"),
                ("50:50 uniformly for all states and UTs", "அனைத்து மாநிலங்களுக்கும் ஒரே சீராக 50:50"),
                ("100% funded by farmers directly", "100% விவசாயிகளால் நேரடியாக நிதியளிக்கப்படுகிறது"),
                ("10% Central and 90% State Governments", "10% மத்திய அரசு மற்றும் 90% மாநில அரசு")
            ],
            "correct_key": "A",
            "exp_en": "The financial cost of the Centrally Sponsored Scheme for PACS computerization is shared on a 60:40 basis between the Centre and general States, 90:10 for North-Eastern and Himalayan States/UTs with legislature, and 100% Central funding for UTs without legislature.",
            "exp_ta": "PACS கணினிமயமாக்கலுக்கான மத்திய நிதியுதவித் திட்டத்தின் நிதிச் செலவு, மத்திய அரசு மற்றும் பொது மாநிலங்களுக்கு இடையே 60:40 என்ற அடிப்படையிலும், வடகிழக்கு மற்றும் இமயமலை மாநிலங்களுக்கு 90:10 என்ற அடிப்படையிலும், சட்டமன்றம் இல்லாத யூனியன் பிரதேசங்களுக்கு 100% மத்திய நிதியிலும் பகிரப்படுகிறது.",
            "why_a_en": "Correct. Standard Centrally Sponsored Scheme (CSS) sharing pattern: 60:40 and 90:10.",
            "why_a_ta": "சரி. நிலையான மத்திய நிதியுதவித் திட்ட நிதிப் பகிர்வு முறை: 60:40 மற்றும் 90:10.",
            "why_b_en": "Incorrect. 50:50 is not the sharing formula.",
            "why_b_ta": "தவறு. 50:50 பகிர்வு முறை அல்ல.",
            "why_c_en": "Incorrect. Farmers pay nothing for software infrastructure.",
            "why_c_ta": "தவறு. உள்கட்டமைப்புக்கு விவசாயிகள் பணம் செலுத்துவதில்லை.",
            "why_d_en": "Incorrect. Centre bears the majority 60% share.",
            "why_d_ta": "தவறு. மத்திய அரசே பெரும்பான்மை 60% பங்கை ஏற்கிறது.",
            "tip_en": "NABARD is the National Level Implementing Agency (NLIA) for the project.",
            "tip_ta": "இத்திட்டத்திற்கான தேசிய அளவிலான அமலாக்க முகமையாக நபார்டு (NABARD) செயல்படுகிறது.",
            "fact_en": "Hardware procured includes computers, biometric readers, web cameras, printers, and UPS backups for each PACS.",
            "fact_ta": "ஒவ்வொரு PACS-க்கும் கணினிகள், பயோமெட்ரிக் கருவிகள், வெப்கேமராக்கள் மற்றும் யுபிஎஸ் உபகரணங்கள் வழங்கப்படுகின்றன."
        },

        # 21. Urban Cooperative Banks Tier 1 Criteria
        {
            "subtopic": "Banking Cooperatives & RBI Regulation",
            "stem_en": "Under the RBI revised categorization, what is the defining deposit ceiling for a Tier 1 Urban Co-operative Bank?",
            "stem_ta": "ரிசர்வ் வங்கியின் திருத்தப்பட்ட வகைப்பாட்டின் கீழ், அடுக்கு 1 (Tier 1) நகர்ப்புறக் கூட்டுறவு வங்கியின் வைப்புத்தொகை உச்சவரம்பு என்ன?",
            "options": [
                ("Deposits up to Rs. 100 crore", "ரூ. 100 கோடி வரையிலான வைப்புத்தொகை"),
                ("Deposits up to Rs. 10 crore", "ரூ. 10 கோடி வரையிலான வைப்புத்தொகை"),
                ("Deposits up to Rs. 500 crore", "ரூ. 500 கோடி வரையிலான வைப்புத்தொகை"),
                ("Deposits up to Rs. 1,000 crore", "ரூ. 1,000 கோடி வரையிலான வைப்புத்தொகை")
            ],
            "correct_key": "A",
            "exp_en": "Under the RBI 4-tier regulatory framework for UCBs, Tier 1 comprises all unit UCBs and salary earners' UCBs irrespective of deposit size, and all other UCBs having deposits up to Rs. 100 crore.",
            "exp_ta": "ரிசர்வ் வங்கியின் 4 அடுக்கு ஒழுங்குமுறை கட்டமைப்பின் கீழ், அடுக்கு 1 என்பது வைப்புத்தொகை அளவைப் பொருட்படுத்தாமல் அனைத்து ஒற்றைக் கிளை UCB-கள் மற்றும் சம்பளதாரர் UCB-கள், மற்றும் ரூ. 100 கோடி வரை வைப்புத்தொகை கொண்ட பிற அனைத்து UCB-களையும் உள்ளடக்கியது.",
            "why_a_en": "Correct. Tier 1 threshold is deposits up to Rs. 100 crore.",
            "why_a_ta": "சரி. அடுக்கு 1 வரம்பு ரூ. 100 கோடி வரையிலான வைப்புத்தொகையாகும்.",
            "why_b_en": "Incorrect. Rs. 10 crore was an obsolete earlier benchmark.",
            "why_b_ta": "தவறு. ரூ. 10 கோடி முந்தைய பழைய வரம்பு.",
            "why_c_en": "Incorrect. Rs. 500 crore is in Tier 2 (Rs. 100-1000 cr).",
            "why_c_ta": "தவறு. ரூ. 500 கோடி அடுக்கு 2-ல் வருகிறது.",
            "why_d_en": "Incorrect. Rs. 1,000 crore is the boundary between Tier 2 and Tier 3.",
            "why_d_ta": "தவறு. ரூ. 1,000 கோடி என்பது அடுக்கு 2 மற்றும் 3-ன் எல்லை.",
            "tip_en": "Tier 1 UCBs enjoy exemptions from full Basel requirements to reduce compliance burden on small local banks.",
            "tip_ta": "சிறிய உள்ளூர் வங்கிகளின் சுமையைக் குறைக்க அடுக்கு 1 வங்கிகளுக்கு கடுமையான பேசல் விதிகளிலிருந்து விலக்கு அளிக்கப்பட்டுள்ளது.",
            "fact_en": "Tier 1 UCBs must maintain minimum Capital to Risk-Weighted Assets Ratio (CRAR) of 9%.",
            "fact_ta": "அடுக்கு 1 UCB-கள் குறைந்தபட்சம் 9% மூலதன நிறைவு விகிதத்தைப் (CRAR) பராமரிக்க வேண்டும்."
        },

        # 22. Multi-State Cooperative Societies Amendment Act 2023 - Board Composition
        {
            "subtopic": "Recent Legislative Reforms (2023)",
            "stem_en": "Under the Multi-State Co-operative Societies (Amendment) Act, 2023, what new mandatory board representation was introduced to align with democratic inclusivity?",
            "stem_ta": "2023-ஆம் ஆண்டின் பல்மாநில கூட்டுறவு சங்கங்கள் (திருத்தச்) சட்டத்தின் கீழ், ஜனநாயக உள்ளடக்கத்திற்கு ஏற்ப வாரியத்தில் என்ன புதிய கட்டாயப் பிரதிநிதித்துவம் அறிமுகப்படுத்தப்பட்டது?",
            "options": [
                ("Mandatory reservation of 1 SC/ST seat and 2 Women seats on the board of multi-state cooperatives", "பல்மாநில கூட்டுறவுகளின் வாரியத்தில் 1 SC/ST இடம் மற்றும் 2 பெண்கள் இடங்கள் கட்டாய இடஒதுக்கீடு"),
                ("Mandatory reservation of 10 seats for foreign nationals", "வெளிநாட்டு குடிமக்களுக்கு 10 இடங்கள் கட்டாய ஒதுக்கீடு"),
                ("Exclusion of all women from the board of directors", "இயக்குநர் வாரியத்திலிருந்து அனைத்துப் பெண்களையும் விலக்குதல்"),
                ("Reservation of 50% seats for commercial bank representatives", "வணிக வங்கிப் பிரதிநிதிகளுக்கு 50% இடங்கள் ஒதுக்கீடு")
            ],
            "correct_key": "A",
            "exp_en": "The MSCS (Amendment) Act, 2023 amended Section 41 to mandate reservation of 1 seat for Scheduled Castes or Scheduled Tribes and 2 seats for Women on the board of every multi-state co-operative society consisting of individuals as members.",
            "exp_ta": "2023 MSCS திருத்தச் சட்டம் பிரிவு 41-ஐத் திருத்தி, தனிநபர்களை உறுப்பினர்களாகக் கொண்ட ஒவ்வொரு பல்மாநிலக் கூட்டுறவு சங்க வாரியத்திலும் பட்டியல் சாதியினர் அல்லது பழங்குடியினருக்கு 1 இடம் மற்றும் பெண்களுக்கு 2 இடங்களை ஒதுக்குவதைக் கட்டாயமாக்கியது.",
            "why_a_en": "Correct. 1 SC/ST seat and 2 Women seats are now statutory under MSCS Act 2023.",
            "why_a_ta": "சரி. 1 SC/ST இடம் மற்றும் 2 பெண்கள் இடங்கள் இப்போது 2023 MSCS சட்டத்தின் கீழ் கட்டாயமாகும்.",
            "why_b_en": "Incorrect. Foreign nationals cannot be members or directors of Indian cooperatives.",
            "why_b_ta": "தவறு. வெளிநாட்டினர் இந்தியக் கூட்டுறவுகளில் இயக்குநராக முடியாது.",
            "why_c_en": "Incorrect. Women representation is promoted, not excluded.",
            "why_c_ta": "தவறு. பெண்கள் பிரதிநிதித்துவம் கட்டாயமாக்கப்பட்டுள்ளது.",
            "why_d_en": "Incorrect. Commercial banks do not take over cooperative boards.",
            "why_d_ta": "தவறு. வணிக வங்கிகளுக்கு 50% இடங்கள் இல்லை.",
            "tip_en": "This directly transplants the constitutional mandate of Article 243ZJ into the central MSCS statute.",
            "tip_ta": "இது சரத்து 243ZJ-ன் அரசியலமைப்பு விதியை மத்திய MSCS சட்டத்தில் நேரடியாக இணைக்கிறது.",
            "fact_en": "The total number of directors on an MSCS board remains capped at 21.",
            "fact_ta": "MSCS வாரியத்தின் மொத்த இயக்குநர்களின் எண்ணிக்கை 21-க்கு மிகாமல் இருக்க வேண்டும்."
        },

        # 23. Cooperative Rehabilitation and Development Fund (2023)
        {
            "subtopic": "Recent Legislative Reforms (2023)",
            "stem_en": "Under the Multi-State Co-operative Societies (Amendment) Act, 2023, what fund was created for the revival of sick multi-state co-operative societies?",
            "stem_ta": "2023-ஆம் ஆண்டின் பல்மாநில கூட்டுறவு சங்கங்கள் (திருத்தச்) சட்டத்தின் கீழ், நலிவடைந்த பல்மாநிலக் கூட்டுறவு சங்கங்களை மீட்டெடுப்பதற்காக உருவாக்கப்பட்ட நிதி எது?",
            "options": [
                ("Co-operative Rehabilitation and Reconstruction Fund", "கூட்டுறவு மறுவாழ்வு மற்றும் புனரமைப்பு நிதி"),
                ("Insolvency and Bankruptcy Liquidation Fund", "திவால் மற்றும் நொடிப்பு கலைத்தல் நிதி"),
                ("National Disaster Response Fund", "தேசிய பேரிடர் மறுமொழி நிதி"),
                ("Universal Service Obligation Fund", "உலகளாவிய சேவை கடமை நிதி")
            ],
            "correct_key": "A",
            "exp_en": "The MSCS (Amendment) Act, 2023 established the 'Co-operative Rehabilitation and Reconstruction Fund' financed by annual contributions from profitable multi-state cooperatives (1% of net profits or Rs. 1 crore, whichever is less) to rehabilitate sick multi-state cooperatives.",
            "exp_ta": "2023 MSCS திருத்தச் சட்டம், நலிவடைந்த பல்மாநிலக் கூட்டுறவுகளை மீட்டெடுப்பதற்காக லாபம் ஈட்டும் பல்மாநிலக் கூட்டுறவுகளின் வருடாந்திர பங்களிப்புடன் (நிகர லாபத்தில் 1% அல்லது ரூ. 1 கோடி) 'கூட்டுறவு மறுவாழ்வு மற்றும் புனரமைப்பு நிதியை' நிறுவியது.",
            "why_a_en": "Correct. Co-operative Rehabilitation and Reconstruction Fund was created under the 2023 Act.",
            "why_a_ta": "சரி. கூட்டுறவு மறுவாழ்வு மற்றும் புனரமைப்பு நிதி 2023 சட்டத்தின் கீழ் உருவாக்கப்பட்டது.",
            "why_b_en": "Incorrect. IBC handles corporate insolvency, not cooperative rehabilitation fund.",
            "why_b_ta": "தவறு. IBC கார்ப்பரேட் திவால் நிலையைக் கையாள்கிறது.",
            "why_c_en": "Incorrect. NDRF handles natural disaster relief.",
            "why_c_ta": "தவறு. NDRF இயற்கை பேரிடர் நிவாரண நிதி.",
            "why_d_en": "Incorrect. USOF is for rural telecommunications under DoT.",
            "why_d_ta": "தவறு. USOF தொலைத்தொடர்புத் துறைக்கானது.",
            "tip_en": "Sick multi-state cooperatives are defined as societies having accumulated losses equal to or exceeding their net worth.",
            "tip_ta": "தங்கள் நிகர மதிப்பை விடக் கூடுதல் நஷ்டம் அடைந்த சங்கங்கள் நலிவடைந்த சங்கங்களாகக் கருதப்படுகின்றன.",
            "fact_en": "The Fund operates on the principle of mutual assistance among cooperatives.",
            "fact_ta": "இந்த நிதி கூட்டுறவுகளுக்கு இடையேயான பரஸ்பர உதவி என்ற கொள்கையின் அடிப்படையில் செயல்படுகிறது."
        },

        # 24. Audit Board Panel Approval Authority
        {
            "subtopic": "Audit of Accounts - Article 243ZM",
            "stem_en": "Under Article 243ZM, who approves the panel of auditors or auditing firms from which a cooperative society's general body must appoint its auditor?",
            "stem_ta": "சரத்து 243ZM-ன் கீழ், ஒரு கூட்டுறவு சங்கத்தின் பொதுக்குழு தனது தணிக்கையாளரைத் தேர்ந்தெடுக்க வேண்டிய தணிக்கையாளர் அல்லது தணிக்கை நிறுவனங்களின் பட்டியலை அங்கீகரிப்பது யார்?",
            "options": [
                ("The State Government or an authority authorized by the State Government", "மாநில அரசு அல்லது மாநில அரசால் அங்கீகரிக்கப்பட்ட ஓர் அதிகாரம்"),
                ("The outgoing Board of Directors unilaterally", "பதவி முடியும் இயக்குநர் வாரியம் தன்னிச்சையாக"),
                ("The Institute of Chartered Accountants of India (ICAI) directly without state consultation", "மாநில அரசை ஆலோசிக்காமல் இந்திய பட்டயக் கணக்காளர்கள் நிறுவனம் (ICAI) நேரடியாக"),
                ("The Chief Justice of the High Court", "உயர் நீதிமன்றத் தலைமை நீதிபதி")
            ],
            "correct_key": "A",
            "exp_en": "Article 243ZM(1) explicitly specifies: '...from a panel approved by a State Government or an authority authorised by the State Government in this behalf.' This guarantees that only vetted, qualified auditors audit public cooperative funds.",
            "exp_ta": "சரத்து 243ZM(1) தெளிவாகக் குறிப்பிடுகிறது: '...மாநில அரசால் அல்லது இது தொடர்பாக மாநில அரசால் அங்கீகரிக்கப்பட்ட அதிகாரியால் அங்கீகரிக்கப்பட்ட பட்டியலில் இருந்து.' இது தகுதியான தணிக்கையாளர்கள் மட்டுமே பொதுக் கூட்டுறவு நிதியைத் தணிக்கை செய்வதை உறுதி செய்கிறது.",
            "why_a_en": "Correct. Panel is approved by the State Government or designated state authority.",
            "why_a_ta": "சரி. தணிக்கையாளர் பட்டியல் மாநில அரசால் அல்லது அங்கீகரிக்கப்பட்ட அதிகாரியால் அங்கீகரிக்கப்படுகிறது.",
            "why_b_en": "Incorrect. Outgoing board cannot handpick an unapproved auditor (prevents collusion).",
            "why_b_ta": "தவறு. வாரியம் தன்னிச்சையாக அங்கீகரிக்கப்படாத தணிக்கையாளரைத் தேர்ந்தெடுக்க முடியாது.",
            "why_c_en": "Incorrect. ICAI certifies CAs, but the state panel is curated by the State Government.",
            "why_c_ta": "தவறு. ICAI பட்டயக் கணக்காளர் தகுதி அளிக்கிறது, ஆனால் பட்டியல் மாநில அரசால் உருவாக்கப்படுகிறது.",
            "why_d_en": "Incorrect. Judiciary does not empanel cooperative auditors.",
            "why_d_ta": "தவறு. நீதித்துறை தணிக்கையாளர் பட்டியலை உருவாக்குவதில்லை.",
            "tip_en": "In Tamil Nadu, the Director of Cooperative Audit maintains and publishes this approved panel.",
            "tip_ta": "தமிழ்நாட்டில், கூட்டுறவுத் தணிக்கை இயக்குநர் இந்த அங்கீகரிக்கப்பட்ட பட்டியலைப் பராமரித்து வெளியிடுகிறார்.",
            "fact_en": "The General Body appoints the auditor at the Annual General Meeting from this approved panel.",
            "fact_ta": "இப்பட்டியலிலிருந்து பொதுக்குழுவே வருடாந்திரக் கூட்டத்தில் தணிக்கையாளரை நியமிக்கிறது."
        },

        # 25. Supreme Court Ruling on Severability - R.F. Nariman's Ratio
        {
            "subtopic": "Judicial Pronouncements - Landmark Ruling",
            "stem_en": "In the majority opinion of Union of India v. Rajendra N. Shah (2021) authored by Justice R.F. Nariman, why was Part IX-B held severable and preserved for Multi-State Cooperatives?",
            "stem_ta": "நீதிபதி ஆர்.எஃப். நாரிமன் எழுதிய மத்திய அரசு v. ராஜேந்திர என். ஷா (2021) பெரும்பான்மை தீர்ப்பில், பகுதி IX-B பிரிக்கப்படக்கூடியது என்றும், பல்மாநிலக் கூட்டுறவுகளுக்கு அது செல்லுபடியாகும் என்றும் ஏன் தீர்ப்பளிக்கப்பட்டது?",
            "options": [
                ("Because Parliament had full legislative competence over Multi-State Cooperatives under Union List Entry 44, and Part IX-B can operate independently for them without impacting State List Entry 32", "ஏனெனில் மத்தியப் பட்டியல் பதிவு 44-ன் கீழ் பல்மாநிலக் கூட்டுறவுகள் மீது நாடாளுமன்றத்திற்கு முழு சட்டமன்ற அதிகாரம் இருந்தது, மேலும் மாநிலப் பட்டியல் பதிவு 32-ஐப் பாதிக்காமல் பகுதி IX-B அவற்றிற்குத் தனித்து இயங்க முடியும் என்பதால்"),
                ("Because all 28 States unanimously requested Parliament to pass the law", "ஏனெனில் அனைத்து 28 மாநிலங்களும் ஒருமனதாக நாடாளுமன்றத்தை இச்சட்டத்தை இயற்றக் கேட்டுக்கொண்டதால்"),
                ("Because cooperatives are declared international entities under the United Nations", "ஏனெனில் கூட்டுறவுகள் ஐக்கிய நாடுகள் சபையின் கீழ் சர்வதேச அமைப்புகளாக அறிவிக்கப்பட்டுள்ளதால்"),
                ("Because the President issued an emergency ordinance overriding state legislatures", "ஏனெனில் மாநில சட்டமன்றங்களை மீறி குடியரசுத் தலைவர் அவசரச் சட்டம் பிறப்பித்ததால்")
            ],
            "correct_key": "A",
            "exp_en": "Justice R.F. Nariman held that Parliament was competent under Article 246(1) read with Entry 44 List I to legislate for Multi-State Cooperatives, and under Article 246(4) for Union Territories. Only the provisions affecting State cooperatives (List II Entry 32) required Article 368(2) ratification. Severing the invalid state provisions left a coherent, viable constitutional framework for multi-state cooperatives.",
            "exp_ta": "மத்தியப் பட்டியல் பதிவு 44-ன் கீழ் பல்மாநிலக் கூட்டுறவுகளுக்கும், சரத்து 246(4)-ன் கீழ் யூனியன் பிரதேசங்களுக்கும் சட்டம் இயற்ற நாடாளுமன்றத்திற்கு முழு அதிகாரம் உண்டு என்று நீதிபதி நாரிமன் கூறினார். மாநில கூட்டுறவுகளைப் (பட்டியல் II பதிவு 32) பாதிக்கும் விதிகளுக்கு மட்டுமே சரத்து 368(2) மாநில ஒப்புதல் தேவைப்பட்டது. செல்லாத மாநில விதிகளை நீக்கிய பிறகும், பல்மாநில கூட்டுறவுகளுக்கான அரசியலமைப்பு கட்டமைப்பு முழுமையாகத் தனித்து இயங்கக்கூடியதாக இருந்தது.",
            "why_a_en": "Correct. Parliament's legislative competence under Entry 44 List I justified severability.",
            "why_a_ta": "சரி. பட்டியல் I பதிவு 44-ன் கீழ் நாடாளுமன்றத்தின் சட்டமன்ற அதிகாரமே பிரித்தெடுப்புக் கோட்பாட்டை நியாயப்படுத்தியது.",
            "why_b_en": "Incorrect. States were not consulted; lack of ratification was the core violation.",
            "why_b_ta": "தவறு. மாநிலங்கள் ஒப்புதல் அளிக்கவில்லை; அதுவே முக்கிய மீறல்.",
            "why_c_en": "Incorrect. Cooperatives are domestic juristic entities under municipal law.",
            "why_c_ta": "தவறு. கூட்டுறவுகள் உள்நாட்டு சட்டத்திற்குட்பட்ட அமைப்புகள்.",
            "why_d_en": "Incorrect. No emergency ordinance was involved.",
            "why_d_ta": "தவறு. எந்த அவசரச் சட்டமும் இதில் சம்பந்தப்படவில்லை.",
            "tip_en": "The test of severability: After striking out the invalid portion, does what remains survive as an independent, workable legislative scheme? SC answered YES for MSCS.",
            "tip_ta": "பிரித்தெடுப்பு சோதனை: செல்லாத பகுதியை நீக்கிய பிறகும், எஞ்சிய பகுதி முழுமையாகத் தனித்து இயங்க முடியுமா? உச்ச நீதிமன்றம் ஆம் என பதிலளித்தது.",
            "fact_en": "This verdict reinforced federalism as part of the Basic Structure of the Indian Constitution.",
            "fact_ta": "இத்தீர்ப்பு இந்திய அரசியலமைப்பின் அடிப்படைக் கட்டமைப்பின் ஒரு பகுதியாக கூட்டாட்சியை மீண்டும் உறுதிப்படுத்தியது."
        },

        # 26. Multi-Unit Cooperative Societies Act, 1942
        {
            "subtopic": "Historical Legislation",
            "stem_en": "Before the enactment of the Multi-State Co-operative Societies Act in 1984, which colonial legislation governed cooperative societies whose objects were not confined to a single province in British India?",
            "stem_ta": "1984-ல் பல்மாநில கூட்டுறவு சங்கங்கள் சட்டம் இயற்றப்படுவதற்கு முன்பு, பிரிட்டிஷ் இந்தியாவில் ஒற்றை மாகாணத்திற்குள் வரையறுக்கப்படாத நோக்கங்களைக் கொண்ட கூட்டுறவு சங்கங்களை எந்தக் காலனித்துவ சட்டம் நிர்வகித்தது?",
            "options": [
                ("Multi-Unit Cooperative Societies Act, 1942", "பல-அலகு கூட்டுறவு சங்கங்கள் சட்டம், 1942"),
                ("Imperial Cooperative Banking Act, 1935", "இம்பீரியல் கூட்டுறவு வங்கிச் சட்டம், 1935"),
                ("Inter-Provincial Trading Act, 1919", "மாகாணங்களுக்கு இடையேயான வர்த்தகச் சட்டம், 1919"),
                ("Government of India Act, 1858", "இந்திய அரசுச் சட்டம், 1858")
            ],
            "correct_key": "A",
            "exp_en": "During World War II, the Central Legislature enacted the Multi-Unit Cooperative Societies Act, 1942 to regulate cooperative societies having objects extending to more than one province, which served as the precursor to the MSCS Acts of 1984 and 2002.",
            "exp_ta": "இரண்டாம் உலகப் போரின் போது, ஒன்றுக்கு மேற்பட்ட மாகாணங்களுக்கு விரிவடையும் நோக்கங்களைக் கொண்ட கூட்டுறவு சங்கங்களை ஒழுங்குபடுத்துவதற்காக மத்திய சட்டமன்றம் 1942-ஆம் ஆண்டின் பல-அலகு கூட்டுறவு சங்கங்கள் சட்டத்தை இயற்றியது; இதுவே 1984 மற்றும் 2002 MSCS சட்டங்களின் முன்னோடியாகும்.",
            "why_a_en": "Correct. 1942 Act was the colonial multi-unit cooperative legislation.",
            "why_a_ta": "சரி. 1942 சட்டம் காலனித்துவ கால பல-அலகு கூட்டுறவுச் சட்டமாகும்.",
            "why_b_en": "Incorrect. No such Act existed.",
            "why_b_ta": "தவறு. அப்படி ஒரு சட்டம் இல்லை.",
            "why_c_en": "Incorrect. 1919 was the general Government of India Act.",
            "why_c_ta": "தவறு. 1919 என்பது இந்திய அரசுச் சட்டம்.",
            "why_d_en": "Incorrect. 1858 transferred power to the British Crown.",
            "why_d_ta": "தவறு. 1858 சட்டம் ஆட்சியை பிரிட்டன் அரசியிடம் மாற்றியது.",
            "tip_en": "Timeline: Multi-Unit Act 1942 -> Multi-State Act 1984 -> Multi-State Act 2002 -> MSCS Amendment Act 2023.",
            "tip_ta": "காலவரிசை: 1942 பல-அலகு சட்டம் -> 1984 பல்மாநில சட்டம் -> 2002 பல்மாநில சட்டம் -> 2023 திருத்தச் சட்டம்.",
            "fact_en": "The 1942 Act delegated powers to the Registrar of the province where the society's head office was situated.",
            "fact_ta": "1942 சட்டம் சங்கத்தின் தலைமை அலுவலகம் அமைந்துள்ள மாகாணப் பதிவாளருக்கு அதிகாரங்களை வழங்கியது."
        },

        # 27. Primary Agricultural Credit Societies Member Composition
        {
            "subtopic": "Grassroots Cooperative Structure",
            "stem_en": "In a Primary Agricultural Cooperative Credit Society (PACS), who constitutes the 'General Body' which exercises ultimate democratic authority under cooperative principles?",
            "stem_ta": "ஒரு தொடக்க வேளாண்மைக் கூட்டுறவுக் கடன் சங்கத்தில் (PACS), கூட்டுறவுக் கொள்கைகளின் கீழ் இறுதி ஜனநாயக அதிகாரத்தைப் பயன்படுத்தும் 'பொதுக்குழு' (General Body) யாரைக் கொண்டு அமைகிறது?",
            "options": [
                ("All the individual primary members admitted in accordance with by-laws and having voting rights", "துணைவிதிகளின்படி சேர்க்கப்பட்டு வாக்குரிமை கொண்ட அனைத்து தனிநபர் தொடக்க உறுப்பினர்கள்"),
                ("Only the elected 21 members of the Board of Directors", "இயக்குநர் வாரியத்தின் தேர்ந்தெடுக்கப்பட்ட 21 உறுப்பினர்கள் மட்டுமே"),
                ("The District Collector and Block Development Officer (BDO)", "மாவட்ட ஆட்சியர் மற்றும் வட்டார வளர்ச்சி அலுவலர் (BDO)"),
                ("The local members of Legislative Assembly and Parliament", "உள்ளூர் சட்டமன்ற மற்றும் நாடாளுமன்ற உறுப்பினர்கள்")
            ],
            "correct_key": "A",
            "exp_en": "In any cooperative society, the General Body consists of all regular voting members. The General Body is the supreme authority of the society, to which the Board of Directors is accountable. The Board is an executive committee elected by and from the General Body.",
            "exp_ta": "எந்தவொரு கூட்டுறவு சங்கத்திலும், பொதுக்குழு என்பது அனைத்து வழக்கமான வாக்களிக்கும் உறுப்பினர்களையும் உள்ளடக்கியது. பொதுக்குழுவே சங்கத்தின் உச்சபட்ச அதிகார அமைப்பாகும்; இதற்கு இயக்குநர் வாரியம் பொறுப்புக் கூற கடமைப்பட்டுள்ளது. வாரியம் என்பது பொதுக்குழுவால் தேர்ந்தெடுக்கப்பட்ட நிர்வாகக் குழுவாகும்.",
            "why_a_en": "Correct. All voting primary members constitute the supreme General Body.",
            "why_a_ta": "சரி. வாக்களிக்கும் அனைத்து தொடக்க உறுப்பினர்களும் உச்ச பொதுக்குழுவை உருவாக்குகிறார்கள்.",
            "why_b_en": "Incorrect. 21 members form the Board, which is subordinate to the General Body.",
            "why_b_ta": "தவறு. 21 உறுப்பினர்கள் வாரியத்தை உருவாக்குகிறார்கள், இது பொதுக்குழுவுக்கு உட்பட்டது.",
            "why_c_en": "Incorrect. Bureaucrats are not members of the general body.",
            "why_c_ta": "தவறு. அதிகாரிகள் பொதுக்குழு உறுப்பினர்கள் அல்ல.",
            "why_d_en": "Incorrect. MLAs/MPs are political representatives, not the cooperative general body.",
            "why_d_ta": "தவறு. சட்டமன்ற உறுப்பினர்கள் சங்கத்தின் பொதுக்குழு அல்ல.",
            "tip_en": "Cooperative Governance hierarchy: General Body (Supreme) -> Board of Directors (Executive) -> Secretary/Managing Director (Administration).",
            "tip_ta": "கூட்டுறவு ஆளுகை படிநிலை: பொதுக்குழு (உச்ச அதிகாரம்) -> இயக்குநர் வாரியம் (நிர்வாகம்) -> செயலாளர்/மேலாண்மை இயக்குநர் (செயல்பாடுகள்).",
            "fact_en": "Major decisions like amendment of by-laws, election of directors, and disposal of net profit require General Body approval.",
            "fact_ta": "துணைவிதிகள் திருத்தம், இயக்குநர்கள் தேர்தல் மற்றும் நிகர லாபப் பகிர்வு போன்ற முக்கிய முடிவுகளுக்கு பொதுக்குழு ஒப்புதல் அவசியம்."
        },

        # 28. Cooperative Sugar Mills in Tamil Nadu
        {
            "subtopic": "Tamil Nadu Cooperative Ecosystem",
            "stem_en": "In Tamil Nadu, what apex cooperative organization coordinates and provides technical, administrative, and financial guidance to all cooperative and public sector sugar mills in the state?",
            "stem_ta": "தமிழ்நாட்டில், மாநிலத்தில் உள்ள அனைத்து கூட்டுறவு மற்றும் பொதுத்துறை சர்க்கரை ஆலைகளையும் ஒருங்கிணைத்து தொழில்நுட்ப, நிர்வாக மற்றும் நிதி வழிகாட்டுதலை வழங்கும் தலைமைக் கூட்டுறவு அமைப்பு எது?",
            "options": [
                ("Tamil Nadu Co-operative Sugar Federation Limited (TNCSF)", "தமிழ்நாடு கூட்டுறவு சர்க்கரை இணையம் (TNCSF)"),
                ("Tamil Nadu Tea Plantation Corporation (TANTEA)", "தமிழ்நாடு தேயிலைத் தோட்டக் கழகம் (TANTEA)"),
                ("Tamil Nadu Civil Supplies Corporation (TNCSC)", "தமிழ்நாடு நுகர்பொருள் வாணிபக் கழகம் (TNCSC)"),
                ("Tamil Nadu Industrial Development Corporation (TIDCO)", "தமிழ்நாடு தொழில் வளர்ச்சி நிறுவனம் (TIDCO)")
            ],
            "correct_key": "A",
            "exp_en": "The Tamil Nadu Co-operative Sugar Federation Limited (TNCSF), established in 1962 in Chennai, acts as the apex federal organization of all cooperative sugar mills in Tamil Nadu, coordinating cane development, byproduct utilization, ethanol production, and marketing of sugar.",
            "exp_ta": "1962-ல் சென்னையில் நிறுவப்பட்ட தமிழ்நாடு கூட்டுறவு சர்க்கரை இணையம் (TNCSF), தமிழ்நாட்டில் உள்ள அனைத்து கூட்டுறவு சர்க்கரை ஆலைகளின் உச்ச அமைப்பாகச் செயல்பட்டு, கரும்பு மேம்பாடு, துணைப் பொருட்கள் பயன்பாடு, எத்தனால் உற்பத்தி மற்றும் சர்க்கரை விற்பனையை ஒருங்கிணைக்கிறது.",
            "why_a_en": "Correct. TNCSF coordinates cooperative sugar mills in Tamil Nadu.",
            "why_a_ta": "சரி. TNCSF தமிழ்நாட்டின் கூட்டுறவு சர்க்கரை ஆலைகளை ஒருங்கிணைக்கிறது.",
            "why_b_en": "Incorrect. TANTEA produces tea in Nilgiris and Valparai.",
            "why_b_ta": "தவறு. TANTEA தேயிலை உற்பத்தியில் ஈடுபடுகிறது.",
            "why_c_en": "Incorrect. TNCSC handles food grain procurement and civil supplies.",
            "why_c_ta": "தவறு. TNCSC உணவு தானியக் கொள்முதலைக் கையாள்கிறது.",
            "why_d_en": "Incorrect. TIDCO promotes large-scale industrial projects.",
            "why_d_ta": "தவறு. TIDCO பெரிய தொழில்துறைத் திட்டங்களை ஊக்குவிக்கிறது.",
            "tip_en": "Prominent cooperative sugar mills in TN include Amaravathi, Kallakurichi, Chengalpattu, and Subramaniya Siva cooperative sugar mills.",
            "tip_ta": "அமராவதி, கள்ளக்குறிச்சி, செங்கல்பட்டு மற்றும் சுப்பிரமணிய சிவா ஆகியவை TN-ன் முக்கிய கூட்டுறவு சர்க்கரை ஆலைகளாகும்.",
            "fact_en": "TNCSF also promotes cogeneration power plants and distillery ethanol units attached to cooperative sugar mills.",
            "fact_ta": "TNCSF சர்க்கரை ஆலைகளுடன் இணைக்கப்பட்ட இணை மின் உற்பத்தி மற்றும் எத்தனால் பிரிவுகளையும் ஊக்குவிக்கிறது."
        },

        # 29. Fisheries Cooperatives Apex Body in Tamil Nadu
        {
            "subtopic": "Tamil Nadu Cooperative Ecosystem",
            "stem_en": "What is the apex cooperative body promoting marine and inland fisheries welfare and marketing fish products in Tamil Nadu?",
            "stem_ta": "தமிழ்நாட்டில் கடல் மற்றும் உள்நாட்டு மீனவர் நலனை மேம்படுத்தவும், மீன் பொருட்களை சந்தைப்படுத்தவும் செயல்படும் தலைமைக் கூட்டுறவு அமைப்பு எது?",
            "options": [
                ("Tamil Nadu State Apex Fisheries Co-operative Federation Limited (TAFCOFED)", "தமிழ்நாடு மாநில தலைமைக் கூட்டுறவு மீன்வளக் கூட்டமைப்பு நிறுவனம் (TAFCOFED)"),
                ("Marine Products Export Development Authority (MPEDA)", "கடல் பொருட்கள் ஏற்றுமதி மேம்பாட்டு ஆணையம் (MPEDA)"),
                ("Fisheries Survey of India (FSI)", "இந்திய மீன்வளக் கணக்கெடுப்பு நிறுவனம் (FSI)"),
                ("Central Marine Fisheries Research Institute (CMFRI)", "மத்திய கடல் மீன்வள ஆராய்ச்சி நிறுவனம் (CMFRI)")
            ],
            "correct_key": "A",
            "exp_en": "TAFCOFED (Tamil Nadu State Apex Fisheries Co-operative Federation Limited), established in 1991, is the apex cooperative federation coordinating over 1,400 marine and inland fishermen and fisherwomen cooperative societies across Tamil Nadu.",
            "exp_ta": "1991-ல் நிறுவப்பட்ட TAFCOFED (தமிழ்நாடு மாநில தலைமைக் கூட்டுறவு மீன்வளக் கூட்டமைப்பு), தமிழ்நாடு முழுவதிலும் உள்ள 1,400-க்கும் மேற்பட்ட கடல் மற்றும் உள்நாட்டு மீனவ மற்றும் மீனவர் மகளிர் கூட்டுறவு சங்கங்களை ஒருங்கிணைக்கும் உச்ச கூட்டுறவு அமைப்பாகும்.",
            "why_a_en": "Correct. TAFCOFED is the apex fisheries cooperative in Tamil Nadu.",
            "why_a_ta": "சரி. TAFCOFED தமிழ்நாட்டின் தலைமைக் கூட்டுறவு மீன்வளக் கூட்டமைப்பாகும்.",
            "why_b_en": "Incorrect. MPEDA is a statutory export agency under Ministry of Commerce.",
            "why_b_ta": "தவறு. MPEDA மத்திய வர்த்தக அமைச்சகத்தின் ஏற்றுமதி ஆணையம்.",
            "why_c_en": "Incorrect. FSI is a scientific survey institute under Department of Fisheries.",
            "why_c_ta": "தவறு. FSI அறிவியல் கணக்கெடுப்பு நிறுவனம்.",
            "why_d_en": "Incorrect. CMFRI is an ICAR fisheries research institute.",
            "why_d_ta": "தவறு. CMFRI ஐசிஏஆர் ஆராய்ச்சி நிறுவனம்.",
            "tip_en": "TAFCOFED provides subsidized diesel, fishing gear, life-saving jackets, and modern hygienic retail fish stalls in Tamil Nadu.",
            "tip_ta": "TAFCOFED மானிய விலையில் டீசல், மீன்பிடி உபகரணங்கள் மற்றும் நவீன மீன் விற்பனை நிலையங்களை வழங்குகிறது.",
            "fact_en": "Fishermen cooperative societies in TN disburse interest-free loans and lean period relief allowances.",
            "fact_ta": "TN மீனவர் கூட்டுறவு சங்கங்கள் வட்டி இல்லா கடன்கள் மற்றும் மீன்பிடி தடைக்கால நிவாரண உதவிகளை வழங்குகின்றன."
        },

        # 30. Single-State vs Multi-State Election Authority
        {
            "subtopic": "Electoral Framework - Comparative Matrix",
            "stem_en": "Following the 2021 Supreme Court judgment in Rajendra N. Shah, which election authorities conduct elections for State Co-operatives vs Multi-State Co-operatives, respectively?",
            "stem_ta": "2021 ராஜேந்திர ஷா உச்ச நீதிமன்றத் தீர்ப்பைத் தொடர்ந்து, முறையே மாநிலக் கூட்டுறவுகள் மற்றும் பல்மாநிலக் கூட்டுறவுகளுக்கான தேர்தல்களை நடத்தும் தேர்தல் அதிகார அமைப்புகள் எவை?",
            "options": [
                ("State Cooperative Election Authorities established under State Laws for State Cooperatives; Central Co-operative Election Authority under MSCS Act for Multi-State Cooperatives", "மாநிலக் கூட்டுறவுகளுக்கு மாநிலச் சட்டங்களின் கீழ் அமைக்கப்பட்ட மாநிலக் கூட்டுறவுத் தேர்தல் ஆணையங்கள்; பல்மாநிலக் கூட்டுறவுகளுக்கு MSCS சட்டத்தின் கீழ் மத்தியக் கூட்டுறவுத் தேர்தல் ஆணையம்"),
                ("Election Commission of India conducts both under Article 324", "சரத்து 324-ன் கீழ் இந்தியத் தேர்தல் ஆணையமே இரண்டையும் நடத்துகிறது"),
                ("State Election Commission (SEC) under Article 243K conducts both", "சரத்து 243K-ன் கீழ் மாநிலத் தேர்தல் ஆணையமே (SEC) இரண்டையும் நடத்துகிறது"),
                ("District Collectors conduct all cooperative elections directly without any statutory authority", "எந்த சட்டப்பூர்வ ஆணையமும் இன்றி மாவட்ட ஆட்சியர்களே நேரடியாக அனைத்துத் தேர்தல்களையும் நடத்துகிறார்கள்")
            ],
            "correct_key": "A",
            "exp_en": "Because Part IX-B was struck down for State cooperatives, election to State cooperatives is governed entirely by State Acts through State Cooperative Election Authorities (e.g. TN State Cooperative Societies Election Commission). For Multi-State cooperatives, elections are conducted by the newly created Co-operative Election Authority under Section 45 of MSCS Act, 2023.",
            "exp_ta": "மாநிலக் கூட்டுறவுகளுக்கான பகுதி IX-B ரத்து செய்யப்பட்டதால், மாநிலக் கூட்டுறவுகளுக்கான தேர்தல்கள் மாநிலச் சட்டங்களின் கீழ் உள்ள மாநிலக் கூட்டுறவுத் தேர்தல் ஆணையங்களால் (எ.கா. TN தேர்தல் ஆணையம்) நடத்தப்படுகின்றன. பல்மாநிலக் கூட்டுறவுகளுக்கு, 2023 MSCS சட்டத்தின் பிரிவு 45-ன் கீழ் அமைக்கப்பட்ட மத்தியக் கூட்டுறவுத் தேர்தல் ஆணையத்தால் தேர்தல்கள் நடத்தப்படுகின்றன.",
            "why_a_en": "Correct. State Election Commission for State Cooperatives; Central Cooperative Election Authority for MSCS.",
            "why_a_ta": "சரி. மாநிலக் கூட்டுறவுகளுக்கு மாநில ஆணையம்; பல்மாநிலங்களுக்கு மத்தியக் கூட்டுறவுத் தேர்தல் ஆணையம்.",
            "why_b_en": "Incorrect. ECI has zero role in cooperative elections.",
            "why_b_ta": "தவறு. கூட்டுறவுத் தேர்தல்களில் இந்தியத் தேர்தல் ஆணையத்திற்குப் பங்கில்லை.",
            "why_c_en": "Incorrect. SEC conducts Panchayat and Municipality elections, not cooperative polls.",
            "why_c_ta": "தவறு. SEC பஞ்சாயத்து மற்றும் நகராட்சி தேர்தல்களை மட்டுமே நடத்துகிறது.",
            "why_d_en": "Incorrect. Elections are conducted by designated statutory election commissions, not unguided Collectors.",
            "why_d_ta": "தவறு. சட்டப்பூர்வ தேர்தல் ஆணையங்களே நடத்துகின்றன.",
            "tip_en": "Do not confuse: SEC (Article 243K) = Panchayats/Municipalities; State Cooperative Election Commission = Cooperative societies.",
            "tip_ta": "குழப்பிக் கொள்ள வேண்டாம்: SEC (243K) = உள்ளாட்சி அமைப்புகள்; கூட்டுறவுத் தேர்தல் ஆணையம் = கூட்டுறவு சங்கங்கள்.",
            "fact_en": "The Multi-State Co-operative Election Authority is headquartered in New Delhi.",
            "fact_ta": "பல்மாநில கூட்டுறவுத் தேர்தல் ஆணையம் புது தில்லியைத் தலைமையிடமாகக் கொண்டுள்ளது."
        },

        # 31. Cooperative Development in Five-Year Plans
        {
            "subtopic": "Five-Year Plans and Cooperative Policy",
            "stem_en": "In which Five-Year Plan did the Government of India first formally declare that 'Cooperation' should be the principal instrument of democratic economic planning and social policy?",
            "stem_ta": "எந்த ஐந்தாண்டுத் திட்டத்தில் இந்திய அரசு முதன்முதலில் 'கூட்டுறவு' என்பது ஜனநாயகப் பொருளாதாரத் திட்டமிடல் மற்றும் சமூகக் கொள்கையின் முதன்மைக் கருவியாக இருக்க வேண்டும் என்று அதிகாரப்பூர்வமாக அறிவித்தது?",
            "options": [
                ("First Five-Year Plan (1951-1956)", "முதலாவது ஐந்தாண்டுத் திட்டம் (1951-1956)"),
                ("Fifth Five-Year Plan (1974-1979)", "ஐந்தாவது ஐந்தாண்டுத் திட்டம் (1974-1979)"),
                ("Eighth Five-Year Plan (1992-1997)", "எட்டாவது ஐந்தாண்டுத் திட்டம் (1992-1997)"),
                ("Tenth Five-Year Plan (2002-2007)", "பத்தாவது ஐந்தாண்டுத் திட்டம் (2002-2007)")
            ],
            "correct_key": "A",
            "exp_en": "The First Five-Year Plan (1951-56) formulated under Prime Minister Jawaharlal Nehru dedicated an entire chapter to cooperatives, declaring: 'The cooperative form of organisation can be made a potent instrument for carrying out socioeconomic development in rural areas.'",
            "exp_ta": "பிரதமர் ஜவஹர்லால் நேருவின் கீழ் உருவாக்கப்பட்ட முதலாவது ஐந்தாண்டுத் திட்டம் (1951-56) கூட்டுறவுக்காக ஒரு முழு அத்தியாயத்தை ஒதுக்கியது; 'கிராமப்புறங்களில் சமூகப் பொருளாதார வளர்ச்சியை மேற்கொள்வதற்கான ஆற்றல்மிக்க கருவியாக கூட்டுறவு அமைப்பை உருவாக்க முடியும்' என்று அறிவித்தது.",
            "why_a_en": "Correct. First FYP laid the policy cornerstone of planned state support for cooperatives.",
            "why_a_ta": "சரி. முதலாவது ஐந்தாண்டுத் திட்டமே கூட்டுறவுக்கான திட்டமிட்ட அரசு ஆதரவின் அடித்தளத்தை அமைத்தது.",
            "why_b_en": "Incorrect. Fifth FYP focused on poverty eradication (Garibi Hatao).",
            "why_b_ta": "தவறு. ஐந்தாவது திட்டம் வறுமை ஒழிப்பில் கவனம் செலுத்தியது.",
            "why_c_en": "Incorrect. Eighth FYP dealt with post-1991 economic liberalization.",
            "why_c_ta": "தவறு. எட்டாவது திட்டம் 1991 தாராளமயமாக்கலைக் கையாண்டது.",
            "why_d_en": "Incorrect. Tenth FYP focused on 8% GDP growth.",
            "why_d_ta": "தவறு. பத்தாவது திட்டம் 8% பொருளாதார வளர்ச்சியில் கவனம் செலுத்தியது.",
            "tip_en": "The Second FYP (1956-61) accepted the Gorwala Committee recommendations and introduced state share capital participation.",
            "tip_ta": "இரண்டாவது ஐந்தாண்டுத் திட்டம் கோர்வாலா குழு பரிந்துரைகளை ஏற்று அரசு பங்கு மூலதனப் பங்களிப்பை அறிமுகப்படுத்தியது.",
            "fact_en": "Cooperative farming was also piloted during the Second and Third FYPs but had limited success.",
            "fact_ta": "இரண்டாவது மற்றும் மூன்றாவது திட்டங்களில் கூட்டுறவுப் பண்ணை முறையும் பரிசோதிக்கப்பட்டது."
        },

        # 32. National Policy on Cooperatives (2002)
        {
            "subtopic": "National Policy Evolution",
            "stem_en": "The National Policy on Cooperatives formulated by the Central Government in 2002 emphasized which core strategic shift?",
            "stem_ta": "2002-ல் மத்திய அரசால் உருவாக்கப்பட்ட தேசியக் கூட்டுறவுக் கொள்கை எந்த முக்கிய மூலோபாய மாற்றத்தை வலியுறுத்தியது?",
            "options": [
                ("Facilitating autonomous, self-reliant, member-controlled cooperatives by reducing direct government interference and financial dependency", "நேரடி அரசுத் தலையீடு மற்றும் நிதிச் சார்பைக் குறைத்து, தன்னாட்சி, சுயசார்பு மற்றும் உறுப்பினர் கட்டுப்பாட்டிலான கூட்டுறவுகளை உருவாக்குவது"),
                ("Nationalizing all cooperative societies into public sector corporations", "அனைத்து கூட்டுறவு சங்கங்களையும் பொதுத்துறை நிறுவனங்களாக தேசியமயமாக்குவது"),
                ("Transferring cooperative regulation from state governments to foreign multinational auditors", "கூட்டுறவு ஒழுங்குமுறையை வெளிநாட்டு பன்னாட்டுத் தணிக்கையாளர்களிடம் மாற்றுவது"),
                ("Banning all agricultural credit cooperatives in India", "இந்தியாவில் அனைத்து வேளாண் கடன் கூட்டுறவுகளையும் தடை செய்வது")
            ],
            "correct_key": "A",
            "exp_en": "The National Policy on Cooperatives announced in March 2002 aimed at facilitating all-round cooperative development, recognizing cooperatives as autonomous, member-owned institutions, and encouraging withdrawal of state equity and bureaucratic dominance.",
            "exp_ta": "2002 மார்ச் மாதத்தில் அறிவிக்கப்பட்ட தேசியக் கூட்டுறவுக் கொள்கையானது, கூட்டுறவுகளைத் தன்னாட்சி பெற்ற உறுப்பினர் அமைப்புகளாக அங்கீகரித்து, அரசின் பங்கு மூலதனத்தையும் அதிகாரத்துவ ஆதிக்கத்தையும் படிப்படியாகக் குறைப்பதை நோக்கமாகக் கொண்டிருந்தது.",
            "why_a_en": "Correct. 2002 Policy championed cooperative autonomy and professional self-reliance.",
            "why_a_ta": "சரி. 2002 கொள்கை கூட்டுறவு தன்னாட்சி மற்றும் தொழில்முறை சுயசார்பை ஆதரித்தது.",
            "why_b_en": "Incorrect. Nationalization was completely contrary to the policy vision.",
            "why_b_ta": "தவறு. தேசியமயமாக்கல் கொள்கைக்கு எதிரானது.",
            "why_c_en": "Incorrect. Foreign regulation was never contemplated.",
            "why_c_ta": "தவறு. வெளிநாட்டு ஒழுங்குமுறை கருதப்படவில்லை.",
            "why_d_en": "Incorrect. The policy sought to strengthen agricultural cooperatives.",
            "why_d_ta": "தவறு. வேளாண் கூட்டுறவுகளை வலுப்படுத்துவதே நோக்கம்.",
            "tip_en": "A new National Cooperation Policy is currently under formulation by a committee chaired by former Union Minister Suresh Prabhu.",
            "tip_ta": "முன்னாள் மத்திய அமைச்சர் சுரேஷ் பிரபு தலைமையிலான குழுவால் புதிய தேசியக் கூட்டுறவுக் கொள்கை தற்போது உருவாக்கப்பட்டு வருகிறது.",
            "fact_en": "The 2002 policy served as a conceptual stepping stone toward the 97th Constitutional Amendment in 2011.",
            "fact_ta": "2002 கொள்கையே 2011-ல் 97வது அரசியலமைப்புத் திருத்தத்திற்கான கருத்தியல் படிக்கல்லாக அமைந்தது."
        },

        # 33. National Cooperation Policy Committee (Suresh Prabhu Committee)
        {
            "subtopic": "Recent Committees & Visions",
            "stem_en": "In September 2022, the Ministry of Cooperation constituted a 47-member National Level Committee to draft the New National Cooperation Policy Document under the chairmanship of whom?",
            "stem_ta": "2022 செப்டம்பரில், புதிய தேசியக் கூட்டுறவுக் கொள்கை ஆவணத்தை வரைவதற்காக கூட்டுறவு அமைச்சகத்தால் யாருடைய தலைமையில் 47 உறுப்பினர்களைக் கொண்ட தேசிய அளவிலான குழு அமைக்கப்பட்டது?",
            "options": [
                ("Shri Suresh Prabhu", "திரு. சுரேஷ் பிரபு"),
                ("Shri N.K. Singh", "திரு. என்.கே. சிங்"),
                ("Dr. Rajiv Kumar", "டாக்டர் ராஜீவ் குமார்"),
                ("Shri Amitabh Kant", "திரு. அமிதாப் காந்த்")
            ],
            "correct_key": "A",
            "exp_en": "In September 2022, Union Minister of Cooperation Amit Shah constituted a 47-member committee chaired by former Union Minister Suresh Prabhu to draft the new National Cooperation Policy Document to promote a vibrant cooperative-based economic development model.",
            "exp_ta": "2022 செப்டம்பரில், துடிப்பான கூட்டுறவு அடிப்படையிலான பொருளாதார மேம்பாட்டு மாதிரியை உருவாக்க புதிய தேசியக் கூட்டுறவுக் கொள்கை ஆவணத்தை வரைவதற்காக முன்னாள் மத்திய அமைச்சர் சுரேஷ் பிரபு தலைமையில் 47 பேர் கொண்ட குழுவை மத்திய அரசு அமைத்தது.",
            "why_a_en": "Correct. Suresh Prabhu headed the National Cooperation Policy Committee.",
            "why_a_ta": "சரி. சுரேஷ் பிரபு தேசியக் கூட்டுறவுக் கொள்கைக் குழுவிற்குத் தலைமை தாங்கினார்.",
            "why_b_en": "Incorrect. N.K. Singh chaired the 15th Finance Commission.",
            "why_b_ta": "தவறு. என்.கே. சிங் 15வது நிதி ஆணையத்தின் தலைவராக இருந்தார்.",
            "why_c_en": "Incorrect. Rajiv Kumar was Vice-Chairman of NITI Aayog.",
            "why_c_ta": "தவறு. ராஜீவ் குமார் நிதி ஆயோக் துணைத் தலைவராக இருந்தார்.",
            "why_d_en": "Incorrect. Amitabh Kant was G20 Sherpa and CEO of NITI Aayog.",
            "why_d_ta": "தவறு. அமிதாப் காந்த் ஜி20 ஷெர்பா.",
            "tip_en": "Vision of the new policy: 'Sahakar Se Samriddhi' - making cooperatives competitive in the globalized digital economy.",
            "tip_ta": "புதிய கொள்கையின் பார்வை: 'கூட்டுறவு மூலம் செழிப்பு' - உலகமயமாக்கப்பட்ட டிஜிட்டல் பொருளாதாரத்தில் கூட்டுறவுகளைப் போட்டியிட வைப்பது.",
            "fact_en": "The committee includes representatives from all sectors of cooperatives, state governments, and research bodies.",
            "fact_ta": "இக்குழுவில் அனைத்துக் கூட்டுறவுத் துறைகள், மாநில அரசுகள் மற்றும் ஆராய்ச்சி அமைப்புகளின் பிரதிநிதிகள் இடம்பெற்றுள்ளனர்."
        },

        # 34. Cooperative Sugar Sector Ethanol Blending
        {
            "subtopic": "Sectoral Innovations - Sugar Cooperatives",
            "stem_en": "How are cooperative sugar mills actively contributing to India's National Policy on Biofuels target of achieving 20% ethanol blending in petrol (E20) by 2025-26?",
            "stem_ta": "2025-26-க்குள் பெட்ரோலில் 20% எத்தனால் கலக்கும் (E20) இந்தியாவின் தேசிய உயிரி எரிபொருள் கொள்கை இலக்கிற்கு கூட்டுறவு சர்க்கரை ஆலைகள் எவ்வாறு தீவிரமாகப் பங்களிக்கின்றன?",
            "options": [
                ("By setting up attached molasses-based and sugarcane juice distilleries to produce fuel-grade anhydrous ethanol", "எரிபொருள் தர எத்தனாலை உற்பத்தி செய்ய கரும்புச்சாறு மற்றும் பாகு (மொலாசஸ்) அடிப்படையிலான வடிசாலைகளை அமைப்பதன் மூலம்"),
                ("By refining imported petroleum diesel in village mills", "கிராம ஆலைகளில் இறக்குமதி செய்யப்பட்ட டீசலைச் சுத்திகரிப்பதன் மூலம்"),
                ("By exporting 100% of raw sugarcane to foreign nations without processing", "எந்த பதப்படுத்துதலும் இன்றி 100% கரும்பை வெளிநாடுகளுக்கு ஏற்றுமதி செய்வதன் மூலம்"),
                ("By closing down all sugar factories during harvesting season", "அறுவடை காலத்தில் அனைத்து சர்க்கரை ஆலைகளையும் மூடுவதன் மூலம்")
            ],
            "correct_key": "A",
            "exp_en": "Cooperative sugar mills in Maharashtra, Uttar Pradesh, Karnataka, and Tamil Nadu have diversified into ethanol production by installing modern distilleries utilizing B-heavy molasses, sugarcane juice, and syrup, directly supplying oil marketing companies (OMCs) to achieve the E20 blending target.",
            "exp_ta": "மகாராஷ்டிரா, உத்தரப் பிரதேசம், கர்நாடகா மற்றும் தமிழ்நாடு ஆகிய மாநிலங்களில் உள்ள கூட்டுறவு சர்க்கரை ஆலைகள், கரும்புச்சாறு மற்றும் மொலாசஸைப் பயன்படுத்தி நவீன வடிசாலைகளை அமைத்து எத்தனால் உற்பத்தியில் ஈடுபட்டு, எண்ணெய் நிறுவனங்களுக்கு நேரடியாக விநியோகிப்பதன் மூலம் E20 இலக்கை அடைய உதவுகின்றன.",
            "why_a_en": "Correct. Modern cooperative distilleries produce ethanol for petrol blending.",
            "why_a_ta": "சரி. நவீன கூட்டுறவு வடிசாலைகள் பெட்ரோலில் கலக்க எத்தனாலை உற்பத்தி செய்கின்றன.",
            "why_b_en": "Incorrect. Crude diesel is not refined by sugar mills.",
            "why_b_ta": "தவறு. டீசல் சுத்திகரிப்பு சர்க்கரை ஆலைகளின் பணி அல்ல.",
            "why_c_en": "Incorrect. Sugarcane is perishable and processed domestically.",
            "why_c_ta": "தவறு. கரும்பு உள்நாட்டிலேயே பதப்படுத்தப்படுகிறது.",
            "why_d_en": "Incorrect. Sugar mills operate at peak during harvesting season.",
            "why_d_ta": "தவறு. அறுவடை காலத்திலேயே ஆலைகள் முழுவீச்சில் இயங்குகின்றன.",
            "tip_en": "Ethanol production provides sugar cooperatives with steady cash flow, ensuring timely Fair and Remunerative Price (FRP) payments to farmers.",
            "tip_ta": "எத்தனால் உற்பத்தி சர்க்கரை கூட்டுறவுகளுக்கு நிலையான பணப்புழக்கத்தை வழங்கி, விவசாயிகளுக்கு நியாயமான மற்றும் ஆதாய விலையை (FRP) உரிய நேரத்தில் வழங்க உதவுகிறது.",
            "fact_en": "Interest subvention schemes by the Central Government have subsidized loans for cooperative ethanol distilleries.",
            "fact_ta": "மத்திய அரசின் வட்டி மானியத் திட்டங்கள் கூட்டுறவு எத்தனால் வடிசாலைகளுக்கான கடன்களுக்கு மானியம் வழங்கியுள்ளன."
        },

        # 35. Primary Co-operative Banks and DICGC Deposit Insurance
        {
            "subtopic": "Banking Cooperatives & Depositor Protection",
            "stem_en": "Under the Deposit Insurance and Credit Guarantee Corporation (DICGC) Act, 1961, what is the maximum insurance coverage provided to a depositor in an insured cooperative bank?",
            "stem_ta": "வைப்புத்தொகை காப்பீடு மற்றும் கடன் உத்தரவாதக் கழக (DICGC) சட்டம் 1961-ன் கீழ், காப்பீடு செய்யப்பட்ட ஒரு கூட்டுறவு வங்கியில் ஒரு வைப்பீட்டாளருக்கு வழங்கப்படும் அதிகபட்ச காப்பீட்டுத் தொகை என்ன?",
            "options": [
                ("Up to Rs. 5,00,000 (Rupees Five Lakh) per depositor across all accounts in the same bank", "ஒரே வங்கியில் உள்ள அனைத்துக் கணக்குகளிலும் ஒரு வைப்பீட்டாளருக்கு அதிகபட்சம் ரூ. 5,00,000 (ரூபாய் ஐந்து லட்சம்) வரை"),
                ("Up to Rs. 1,00,000 only", "ரூ. 1,00,000 வரை மட்டுமே"),
                ("Up to Rs. 50,000 only", "ரூ. 50,000 வரை மட்டுமே"),
                ("Unlimited insurance coverage for any amount", "எந்தத் தொகைக்கும் வரம்பற்ற காப்பீட்டுப் பாதுகாப்பு")
            ],
            "correct_key": "A",
            "exp_en": "In February 2020, the Government of India increased the deposit insurance limit from Rs. 1 lakh to Rs. 5 lakh per depositor per bank (both principal and interest), covering all commercial, urban cooperative, and rural cooperative banks insured with DICGC.",
            "exp_ta": "2020 பிப்ரவரியில், இந்திய அரசு ஒரு வங்கியில் ஒரு வைப்பீட்டாளருக்கான வைப்புத்தொகை காப்பீட்டு வரம்பை ரூ. 1 லட்சத்திலிருந்து ரூ. 5 லட்சமாக உயர்த்தியது (அசல் மற்றும் வட்டி இரண்டும் சேர்த்து); இது DICGC-ல் காப்பீடு செய்யப்பட்ட அனைத்து வணிக மற்றும் கூட்டுறவு வங்கிகளுக்கும் பொருந்தும்.",
            "why_a_en": "Correct. Rs. 5,00,000 is the statutory DICGC deposit insurance limit.",
            "why_a_ta": "சரி. ரூ. 5,00,000 என்பது சட்டப்பூர்வ DICGC வைப்புக் காப்பீட்டு வரம்பாகும்.",
            "why_b_en": "Incorrect. Rs. 1 lakh was the older limit prior to February 2020.",
            "why_b_ta": "தவறு. ரூ. 1 லட்சம் என்பது 2020-க்கு முந்தைய பழைய வரம்பு.",
            "why_c_en": "Incorrect. Rs. 50,000 is an obsolete limit from the 1990s.",
            "why_c_ta": "தவறு. ரூ. 50,000 என்பது 1990-களின் பழைய வரம்பு.",
            "why_d_en": "Incorrect. Deposit insurance is capped at Rs. 5 lakh.",
            "why_d_ta": "தவறு. காப்பீடு ரூ. 5 லட்சத்திற்குள் வரம்பிடப்பட்டுள்ளது.",
            "tip_en": "The DICGC (Amendment) Act, 2021 mandates payment of insured deposit within 90 days of moratorium/restrictions placed by RBI on a troubled cooperative bank.",
            "tip_ta": "2021 திருத்தச் சட்டம், ஒரு கூட்டுறவு வங்கி மீது ரிசர்வ் வங்கி தடை விதித்த 90 நாட்களுக்குள் காப்பீட்டுத் தொகையை வைப்பீட்டாளருக்கு வழங்க கட்டாயமாக்குகிறது.",
            "fact_en": "Over 98% of depositors across cooperative banks in India are fully covered within this Rs. 5 lakh limit.",
            "fact_ta": "இந்தியாவில் உள்ள கூட்டுறவு வங்கி வைப்பீட்டாளர்களில் 98%-க்கும் அதிகமானோர் இந்த ரூ. 5 லட்சம் வரம்பிற்குள் முழுமையாகப் பாதுகாக்கப்படுகின்றனர்."
        },

        # 36. Primary Cooperative Agriculture and Rural Development Banks Refinancing
        {
            "subtopic": "Long-Term Rural Credit Structure",
            "stem_en": "How does the long-term cooperative credit structure in India (comprising SCARDBs and PCARDBs) raise capital for their long-term lending operations?",
            "stem_ta": "இந்தியாவில் நீண்ட காலக் கூட்டுறவுக் கடன் அமைப்பு (SCARDBs மற்றும் PCARDBs) தங்களின் நீண்ட கால கடன் நடவடிக்கைகளுக்கான மூலதனத்தை எவ்வாறு திரட்டுகிறது?",
            "options": [
                ("By floating long-term debentures subscribed by NABARD, Central/State Governments, and commercial banks", "நபார்டு, மத்திய/மாநில அரசுகள் மற்றும் வணிக வங்கிகளால் வாங்கப்படும் நீண்ட காலக் கடன் பத்திரங்களை (டிபஞ்சர்கள்) வெளியிடுவதன் மூலம்"),
                ("By issuing high-risk equity shares on the New York Stock Exchange", "நியூயார்க் பங்குச் சந்தையில் அதிக ஆபத்துள்ள பங்குகளை வெளியிடுவதன் மூலம்"),
                ("By printing government sovereign currency directly", "அரசின் இறையாண்மை நாணயத்தை நேரடியாக அச்சிடுவதன் மூலம்"),
                ("By taking short-term overnight call money loans from foreign hedge funds", "வெளிநாட்டு ஹெட்ஜ் நிதிகளிடமிருந்து குறுகிய கால ஒரே நாள் கடன்களைப் பெறுவதன் மூலம்")
            ],
            "correct_key": "A",
            "exp_en": "Unlike commercial banks that rely on short-term deposits, State Co-operative Agriculture and Rural Development Banks (SCARDBs) raise long-term resources primarily by floating debentures guaranteed by State Governments and subscribed by NABARD, commercial banks, and LIC.",
            "exp_ta": "குறுகிய கால வைப்புகளை நம்பியிருக்கும் வணிக வங்கிகளைப் போலன்றி, மாநில கூட்டுறவு வேளாண்மை மற்றும் ஊரக வளர்ச்சி வங்கிகள் (SCARDBs) மாநில அரசுகளின் உத்தரவாதத்துடன் நபார்டு, வணிக வங்கிகள் மற்றும் எல்.ஐ.சி ஆகியவற்றால் வாங்கப்படும் நீண்ட காலக் கடன் பத்திரங்களை (Debentures) வெளியிட்டு நிதியைத் திரட்டுகின்றன.",
            "why_a_en": "Correct. Floating state-guaranteed debentures refinanced by NABARD.",
            "why_a_ta": "சரி. நபார்டு மறுநிதியளிக்கும் அரசு உத்தரவாதக் கடன் பத்திரங்களை வெளியிடுதல்.",
            "why_b_en": "Incorrect. Cooperatives do not trade equity shares on foreign stock exchanges.",
            "why_b_ta": "தவறு. கூட்டுறவுகள் வெளிநாட்டு பங்குச் சந்தைகளில் பங்குகளை வெளியிடுவதில்லை.",
            "why_c_en": "Incorrect. Only RBI has currency-issuing authority.",
            "why_c_ta": "தவறு. ரிசர்வ் வங்கி மட்டுமே நாணயத்தை வெளியிடுகிறது.",
            "why_d_en": "Incorrect. Long-term assets cannot be financed by speculative overnight call money.",
            "why_d_ta": "தவறு. நீண்ட கால சொத்துக்களை குறுகிய காலக் கடன்கள் மூலம் நிதியளிக்க முடியாது.",
            "tip_en": "Asset-Liability Matching: Long-term farm investments (15 years) require matched long-term debenture financing to avoid liquidity crisis.",
            "tip_ta": "சொத்து-பொறுப்பு பொருத்தம்: 15 ஆண்டுகால விவசாயக் கடன்களுக்கு சமமான நீண்ட காலக் கடன் பத்திர நிதி அவசியமாகும்.",
            "fact_en": "NABARD provides up to 90-95% refinance support for rural development debentures.",
            "fact_ta": "நபார்டு ஊரக வளர்ச்சிக் கடன் பத்திரங்களுக்கு 90-95% வரை மறுநிதியளிப்பு ஆதரவை வழங்குகிறது."
        },

        # 37. Cooperatives and Direct Selling on GeM Portal
        {
            "subtopic": "Modern Reforms & Market Access",
            "stem_en": "In June 2022, the Union Cabinet approved which landmark policy enabling cooperative societies to participate directly as buyers and sellers in public procurement?",
            "stem_ta": "2022 ஜூன் மாதம், பொதுக் கொள்முதலில் கூட்டுறவு சங்கங்கள் நேரடியாக வாங்குபவர்களாகவும் விற்பனையாளர்களாகவும் பங்கேற்க உதவும் எந்த மைல்கல் கொள்கைக்கு மத்திய அமைச்சரவை ஒப்புதல் அளித்தது?",
            "options": [
                ("Allowing Co-operative Societies to onboard on the Government e-Marketplace (GeM) portal", "கூட்டுறவு சங்கங்களை அரசு இ-மார்க்கெட்பிளேஸ் (GeM) போர்ட்டலில் இணைய அனுமதிப்பது"),
                ("Banning all private vendors from participating in government procurement", "அரசு கொள்முதலில் அனைத்து தனியார் விற்பனையாளர்களும் பங்கேற்க தடை விதிப்பது"),
                ("Mandating that all government offices buy exclusively from multinational foreign firms", "அனைத்து அரசு அலுவலகங்களும் வெளிநாட்டு நிறுவனங்களிடமிருந்து மட்டுமே வாங்க வேண்டும் என்று கட்டாயப்படுத்துவது"),
                ("Abolishing electronic tendering in all public departments", "அனைத்து அரசுத் துறைகளிலும் மின்னணு டெண்டர் முறையை ஒழிப்பது")
            ],
            "correct_key": "A",
            "exp_en": "In June 2022, the Union Cabinet permitted cooperatives to register as buyers on the Government e-Marketplace (GeM) platform. This allows over 8.5 lakh cooperatives to procure goods and services transparently at competitive rates and sell their produce directly to government departments.",
            "exp_ta": "2022 ஜூன் மாதம், மத்திய அமைச்சரவை கூட்டுறவு சங்கங்களை அரசு இ-மார்க்கெட்பிளேஸ் (GeM) தளத்தில் வாங்குபவர்களாகவும் விற்பனையாளர்களாகவும் பதிவு செய்ய அனுமதித்தது; இது 8.5 லட்சத்திற்கும் மேற்பட்ட கூட்டுறவுகள் வெளிப்படைத்தன்மையுடன் குறைந்த விலையில் பொருட்களை வாங்கவும் அரசுக்கு விற்கவும் உதவுகிறது.",
            "why_a_en": "Correct. Cooperative onboarding onto the GeM portal was approved in June 2022.",
            "why_a_ta": "சரி. GeM போர்ட்டலில் கூட்டுறவுகளை இணைப்பது ஜூன் 2022-ல் அங்கீகரிக்கப்பட்டது.",
            "why_b_en": "Incorrect. Private vendors continue to participate on GeM.",
            "why_b_ta": "தவறு. தனியார் விற்பனையாளர்களும் GeM-ல் பங்கேற்கின்றனர்.",
            "why_c_en": "Incorrect. Policy promotes domestic procurement under Atmanirbhar Bharat.",
            "why_c_ta": "தவறு. உள்நாட்டுக் கொள்முதலை ஊக்குவிப்பதே கொள்கை.",
            "why_d_en": "Incorrect. GeM is completely electronic and paperless.",
            "why_d_ta": "தவறு. GeM முழுமையாக மின்னணு மயமானது.",
            "tip_en": "GeM onboarding eliminated middlemen, enabling primary cooperatives to procure fertilizers, computers, and agricultural machinery at bulk government rates.",
            "tip_ta": "GeM இணைப்பு இடைத்தரகர்களை நீக்கி, கூட்டுறவுகள் குறைந்த அரசு விலையில் பொருட்களைப் பெற உதவியது.",
            "fact_en": "Major cooperatives like Amul, IFFCO, and KRIBHCO are active sellers and buyers on GeM.",
            "fact_ta": "அமுல், இஃப்கோ போன்ற முன்னணி கூட்டுறவுகள் GeM-ல் தீவிரமாகச் செயல்படுகின்றன."
        },

        # 38. Primary Agricultural Credit Societies as Common Service Centres (CSCs)
        {
            "subtopic": "Service Diversification of PACS",
            "stem_en": "Under the MoU signed between the Ministry of Cooperation and the Ministry of Electronics & IT (MeitY) in February 2023, what new function can PACS perform at the village level?",
            "stem_ta": "2023 பிப்ரவரியில் கூட்டுறவு அமைச்சகத்திற்கும் மின்னணு மற்றும் தகவல் தொழில்நுட்ப அமைச்சகத்திற்கும் (MeitY) இடையே கையெழுத்தான ஒப்பந்தத்தின் கீழ், PACS-கள் கிராம அளவில் என்ன புதிய பணியைச் செய்ய முடியும்?",
            "options": [
                ("Functioning as Common Service Centres (CSCs) delivering over 300 e-services like Aadhaar, PAN card, banking, and citizen certificates", "ஆதார், பான் கார்டு, வங்கிச் சேவைகள் மற்றும் சான்றிதழ்கள் போன்ற 300-க்கும் மேற்பட்ட இ-சேவைகளை வழங்கும் பொது சேவை மையங்களாகச் (CSCs) செயல்படுவது"),
                ("Issuing commercial driving licenses directly without RTO approval", "RTO அனுமதியின்றி வணிக ஓட்டுநர் உரிமங்களை நேரடியாக வழங்குவது"),
                ("Conducting criminal trials for murder cases", "கொலை வழக்குகளுக்கான குற்றவியல் விசாரணைகளை நடத்துவது"),
                ("Operating international border customs clearance checkpoints", "சர்வதேச எல்லை சுங்க அனுமதி சோதனைச் சாவடிகளை இயக்குவது")
            ],
            "correct_key": "A",
            "exp_en": "In February 2023, a historic MoU enabled functional PACS to deliver all services provided by Common Service Centres (CSCs), transforming village PACS into digital service delivery points for over 300 government and commercial services, creating new non-credit revenue streams for cooperatives.",
            "exp_ta": "2023 பிப்ரவரியில் கையெழுத்தான வரலாற்று ஒப்பந்தம், PACS-களை பொது சேவை மையங்களாக (CSCs) மாற்றி, ஆதார், பான், பாஸ்போர்ட் விண்ணப்பம், மற்றும் அரசு சான்றிதழ்கள் உள்ளிட்ட 300-க்கும் மேற்பட்ட டிஜிட்டல் சேவைகளை கிராமங்களில் வழங்க அனுமதித்தது; இது கூட்டுறவுகளுக்கு புதிய கடன் சாரா வருவாயை உருவாக்குகிறது.",
            "why_a_en": "Correct. PACS functioning as Common Service Centres (CSCs).",
            "why_a_ta": "சரி. PACS-கள் பொது சேவை மையங்களாக (CSCs) செயல்படுகின்றன.",
            "why_b_en": "Incorrect. Driving licenses are issued by Motor Vehicles Department.",
            "why_b_ta": "தவறு. ஓட்டுநர் உரிமம் போக்குவரத்துத் துறையால் வழங்கப்படுகிறது.",
            "why_c_en": "Incorrect. Criminal trials are conducted by Sessions Courts.",
            "why_c_ta": "தவறு. குற்றவியல் விசாரணை அமர்வு நீதிமன்றங்களால் நடத்தப்படுகிறது.",
            "why_d_en": "Incorrect. Customs checkpoints are manned by Central CBIC.",
            "why_d_ta": "தவறு. சுங்கச் சாவடிகள் மத்திய சுங்கத் துறையால் நிர்வகிக்கப்படுகின்றன.",
            "tip_en": "Over 50,000 PACS have already registered as CSCs across India.",
            "tip_ta": "இந்தியா முழுவதும் 50,000-க்கும் மேற்பட்ட PACS-கள் ஏற்கனவே CSC-களாகப் பதிவு செய்துள்ளன.",
            "fact_en": "Village farmers no longer need to travel to taluk towns for simple government certificates.",
            "fact_ta": "கிராமத்து விவசாயிகள் எளிய அரசு சான்றிதழ்களுக்காக தாலுகா நகரங்களுக்குச் செல்ல வேண்டியதில்லை."
        },

        # 39. Co-operative Movement Centenary Year
        {
            "subtopic": "Historical Milestones",
            "stem_en": "In which year did the cooperative movement in India complete 100 years of official statutory existence, commemorated as the Centenary Year?",
            "stem_ta": "இந்தியாவில் கூட்டுறவு இயக்கம் எந்த ஆண்டில் அதிகாரப்பூர்வ சட்டப்பூர்வ இருப்பின் 100 ஆண்டுகளை நிறைவு செய்து நூற்றாண்டு விழாவாகக் கொண்டாடப்பட்டது?",
            "options": [
                ("2004", "2004"),
                ("1995", "1995"),
                ("2012", "2012"),
                ("1982", "1982")
            ],
            "correct_key": "A",
            "exp_en": "The Indian cooperative movement commenced with the passage of the Cooperative Credit Societies Act in March 1904. Hence, the year 2004 marked the centenary of the cooperative movement in India, commemorated nationwide with national conferences and reform initiatives.",
            "exp_ta": "இந்தியக் கூட்டுறவு இயக்கம் 1904 மார்ச்சில் கூட்டுறவு கடன் சங்கங்கள் சட்டம் இயற்றப்பட்டதன் மூலம் தொடங்கியது. எனவே, 2004-ஆம் ஆண்டு இந்தியாவில் கூட்டுறவு இயக்கத்தின் நூற்றாண்டு விழாவாக நாடு முழுவதும் கொண்டாடப்பட்டது.",
            "why_a_en": "Correct. 1904 to 2004 marks the centenary.",
            "why_a_ta": "சரி. 1904 முதல் 2004 வரை நூற்றாண்டு நிறைவைக் குறிக்கிறது.",
            "why_b_en": "Incorrect. 1995 was the centenary of International Co-operative Alliance (ICA).",
            "why_b_ta": "தவறு. 1995 என்பது சர்வதேச கூட்டுறவு கூட்டணியின் (ICA) நூற்றாண்டு ஆண்டு.",
            "why_c_en": "Incorrect. 2012 was UN International Year of Cooperatives.",
            "why_c_ta": "தவறு. 2012 ஐ.நா சர்வதேச கூட்டுறவு ஆண்டு.",
            "why_d_en": "Incorrect. 1982 was the founding year of NABARD.",
            "why_d_ta": "தவறு. 1982 நபார்டு நிறுவப்பட்ட ஆண்டு.",
            "tip_en": "The centenary led the Government of India to appoint the Vaidyanathan Task Force in 2004 to revitalize the rural cooperative credit structure.",
            "tip_ta": "நூற்றாண்டு ஆண்டை ஒட்டியே ஊரகக் கூட்டுறவு கடன் கட்டமைப்பைப் புத்துயிரூட்ட 2004-ல் மத்திய அரசு வைத்தியநாதன் பணிக்குழுவை அமைத்தது.",
            "fact_en": "Special postage stamps and commemorative coins were released in 2004 to honor Indian cooperatives.",
            "fact_ta": "இந்தியக் கூட்டுறவுகளைக் கௌரவிக்க 2004-ல் சிறப்பு அஞ்சல் தலைகள் மற்றும் நினைவு நாணயங்கள் வெளியிடப்பட்டன."
        },

        # 40. Cooperative Federalism vs Cooperative Societies
        {
            "subtopic": "Conceptual Clarification",
            "stem_en": "In Indian constitutional jurisprudence, what is the clear distinction between the concept of 'Cooperative Federalism' and 'Co-operative Societies'?",
            "stem_ta": "இந்திய அரசியலமைப்பு சட்டக் கோட்பாட்டில், 'கூட்டுறவுக் கூட்டாட்சி' (Cooperative Federalism) மற்றும் 'கூட்டுறவு சங்கங்கள்' (Co-operative Societies) ஆகிய கருத்துக்களுக்கு இடையிலான தெளிவான வேறுபாடு என்ன?",
            "options": [
                ("'Cooperative Federalism' refers to the collaborative intergovernmental relationship between Union and States, whereas 'Co-operative Societies' are voluntary economic associations of citizens", "'கூட்டுறவுக் கூட்டாட்சி' என்பது மத்திய மற்றும் மாநில அரசுகளுக்கு இடையேயான கூட்டுறவு உறவைக் குறிக்கிறது, ஆனால் 'கூட்டுறவு சங்கங்கள்' என்பது குடிமக்களின் தன்னார்வப் பொருளாதார அமைப்புகளாகும்"),
                ("Both are identical statutory terms under the Companies Act", "இரண்டுமே நிறுவனங்கள் சட்டத்தின் கீழ் ஒரே மாதிரியான சட்டப்பூர்வ விதிமுறைகள்"),
                ("'Cooperative Federalism' applies exclusively to cooperative sugar mills", "'கூட்டுறவுக் கூட்டாட்சி' என்பது கூட்டுறவு சர்க்கரை ஆலைகளுக்கு மட்டுமே பொருந்தும்"),
                ("'Co-operative Societies' are sovereign states with foreign embassies", "'கூட்டுறவு சங்கங்கள்' என்பது வெளிநாட்டுத் தூதரகங்களைக் கொண்ட இறையாண்மை கொண்ட மாநிலங்கள் ஆகும்")
            ],
            "correct_key": "A",
            "exp_en": "'Cooperative Federalism' is a constitutional governance philosophy (reflected in GST Council, NITI Aayog, Inter-State Council) where Centre and States work in harmonious coordination. In contrast, 'Co-operative Societies' are democratic, member-owned grassroots socioeconomic associations governed by Part IX-B and state cooperative acts.",
            "exp_ta": "'கூட்டுறவுக் கூட்டாட்சி' என்பது மத்திய மற்றும் மாநில அரசுகள் இணைந்து இணக்கமாகச் செயல்படும் ஓர் அரசியலமைப்பு ஆளுகைத் தத்துவமாகும் (ஜிஎஸ்டி கவுன்சில், நிதி ஆயோக் போன்றவை). மாறாக, 'கூட்டுறவு சங்கங்கள்' என்பது பகுதி IX-B மற்றும் மாநிலச் சட்டங்களால் நிர்வகிக்கப்படும் உறுப்பினர்களுக்குச் சொந்தமான சமூகப் பொருளாதார அமைப்புகளாகும்.",
            "why_a_en": "Correct. Intergovernmental collaboration vs grassroots economic member associations.",
            "why_a_ta": "சரி. அரசுகளுக்கிடையேயான ஒத்துழைப்பு vs அடிமட்ட பொருளாதார உறுப்பினர் சங்கங்கள்.",
            "why_b_en": "Incorrect. Neither is defined under the Companies Act.",
            "why_b_ta": "தவறு. நிறுவனங்கள் சட்டத்தின் கீழ் இவை வரையறுக்கப்படவில்லை.",
            "why_c_en": "Incorrect. Cooperative federalism is a macro constitutional concept.",
            "why_c_ta": "தவறு. கூட்டாட்சி என்பது ஒரு பரந்த அரசியலமைப்பு கோட்பாடு.",
            "why_d_en": "Incorrect. Cooperatives are domestic juristic associations.",
            "why_d_ta": "தவறு. கூட்டுறவுகள் உள்நாட்டு சட்ட அமைப்புகள்.",
            "tip_en": "TNPSC Trap: Do not confuse questions on Cooperative Federalism (Inter-State Council Art 263) with Co-operative Societies (Part IX-B).",
            "tip_ta": "TNPSC பொறி: கூட்டுறவுக் கூட்டாட்சி (சரத்து 263) வினாக்களையும், கூட்டுறவு சங்கங்கள் (பகுதி IX-B) வினாக்களையும் குழப்பிக் கொள்ளாதீர்கள்.",
            "fact_en": "The Supreme Court in Rajendra Shah ironically invoked 'Cooperative Federalism' to protect States' exclusive legislative domain over 'Co-operative Societies'.",
            "fact_ta": "உச்ச நீதிமன்றம் ராஜேந்திர ஷா தீர்ப்பில் மாநிலங்களின் கூட்டுறவு அதிகாரத்தைப் பாதுகாக்க 'கூட்டுறவுக் கூட்டாட்சி' கோட்பாட்டை மேற்கோள் காட்டியது."
        },

        # 41. Power of State Government to Give Directions
        {
            "subtopic": "State Regulation vs Autonomy",
            "stem_en": "Under state cooperative legislation (such as Section 170 of the Tamil Nadu Co-operative Societies Act, 1983), on what specific grounds can the State Government issue binding policy directions to cooperative societies?",
            "stem_ta": "மாநிலக் கூட்டுறவுச் சட்டங்களின் கீழ் (தமிழ்நாடு கூட்டுறவு சங்கங்கள் சட்டம் 1983-ன் பிரிவு 170 உட்பட), எந்தக் குறிப்பிட்ட காரணங்களுக்காக மாநில அரசு கூட்டுறவு சங்கங்களுக்குக் கட்டுப்படுத்தும் கொள்கை உத்தரவுகளைப் பிறப்பிக்க முடியும்?",
            "options": [
                ("In the public interest or to secure the proper implementation of cooperative production and agricultural development programmes", "பொது நலன் கருதி அல்லது கூட்டுறவு உற்பத்தி மற்றும் வேளாண் மேம்பாட்டுத் திட்டங்களை முறையாகச் செயல்படுத்துவதை உறுதி செய்வதற்காக"),
                ("To force societies to donate all funds to private political parties", "தனியார் அரசியல் கட்சிகளுக்கு அனைத்து நிதியையும் நன்கொடையாக வழங்க கட்டாயப்படுத்த"),
                ("To prohibit members from speaking in their native language", "உறுப்பினர்கள் தங்கள் தாய்மொழியில் பேசுவதைத் தடை செய்ய"),
                ("To dissolve societies without any statutory record", "சட்டப்பூர்வ பதிவுகள் ஏதுமின்றி சங்கங்களை கலைத்துவிட")
            ],
            "correct_key": "A",
            "exp_en": "Section 170 of the TN Act 1983 empowers the State Government to issue directions to any cooperative society or class of societies in the public interest, for the prevention of affairs being conducted detrimentally, or to secure proper implementation of agricultural development programmes, which the societies are bound to comply with.",
            "exp_ta": "1983 TN சட்டத்தின் பிரிவு 170, பொது நலன் கருதி, சங்கத்தின் விவகாரங்கள் பாதிப்பு ஏற்படுத்தும் வகையில் நடத்தப்படுவதைத் தடுக்க அல்லது வேளாண் வளர்ச்சித் திட்டங்களை முறையாகச் செயல்படுத்துவதை உறுதி செய்ய எந்தவொரு கூட்டுறவு சங்கத்திற்கும் அரசு கட்டாயக் கொள்கை வழிகாட்டுதல்களை வழங்க அதிகாரம் அளிக்கிறது.",
            "why_a_en": "Correct. Public interest and proper scheme implementation are the statutory grounds.",
            "why_a_ta": "சரி. பொது நலன் மற்றும் திட்டங்களைச் செயல்படுத்துவதே சட்டப்பூர்வ காரணங்களாகும்.",
            "why_b_en": "Incorrect. Cooperatives cannot donate to political parties.",
            "why_b_ta": "தவறு. அரசியல் கட்சிகளுக்கு நிதி அளிக்க முடியாது.",
            "why_c_en": "Incorrect. Language prohibition is unconstitutional.",
            "why_c_ta": "தவறு. மொழித் தடை அரசியலமைப்பிற்கு முரணானது.",
            "why_d_en": "Incorrect. Dissolution must strictly follow Section 137 procedures.",
            "why_d_ta": "தவறு. கலைத்தல் பிரிவு 137 நடைமுறைகளைப் பின்பற்ற வேண்டும்.",
            "tip_en": "Directions under Section 170 must be general policy directions, not interfering in day-to-day loan sanctioning to individual borrowers.",
            "tip_ta": "பிரிவு 170-ன் கீழ் பிறப்பிக்கப்படும் உத்தரவுகள் பொதுவான கொள்கை உத்தரவுகளாக இருக்க வேண்டும், அன்றாட நிர்வாகத்தில் தலையிடக் கூடாது.",
            "fact_en": "Government crop loan waiver orders in Tamil Nadu are issued under this statutory power.",
            "fact_ta": "தமிழ்நாட்டில் விவசாயக் கடன் தள்ளுபடி உத்தரவுகள் இந்த சட்டப்பூர்வ அதிகாரத்தின் கீழேயே பிறப்பிக்கப்படுகின்றன."
        },

        # 42. Crop Loan Interest Waiver Schemes in Tamil Nadu
        {
            "subtopic": "Tamil Nadu Cooperative Welfare Schemes",
            "stem_en": "In Tamil Nadu, cooperative crop loans disbursed through Primary Agricultural Cooperative Credit Societies (PACS) carry what effective interest rate for farmers who repay their loans promptly within the due date?",
            "stem_ta": "தமிழ்நாட்டில், தொடக்க வேளாண்மைக் கூட்டுறவுக் கடன் சங்கங்கள் (PACS) மூலம் வழங்கப்படும் பயிர்க்கடன்களை உரிய தவணைத் தேதிக்குள் முறையாகத் திருப்பிச் செலுத்தும் விவசாயிகளுக்கு நடைமுறை வட்டி விகிதம் என்ன?",
            "options": [
                ("0% (Interest-Free Crop Loans due to 100% state interest subvention)", "0% (100% மாநில அரசு வட்டி மானியம் காரணமாக வட்டியில்லா பயிர்க்கடன்)"),
                ("7% annual interest", "ஆண்டுக்கு 7% வட்டி"),
                ("12% annual interest", "ஆண்டுக்கு 12% வட்டி"),
                ("18% compound interest", "18% கூட்டு வட்டி")
            ],
            "correct_key": "A",
            "exp_en": "In Tamil Nadu, farmers who repay their cooperative crop loans promptly within the due date (usually 10-12 months) receive 100% interest subvention from the State Government, effectively making the crop loan completely interest-free (0% interest).",
            "exp_ta": "தமிழ்நாட்டில், தொடக்க வேளாண் கூட்டுறவு கடன் சங்கங்களில் பெற்ற பயிர்க்கடனை உரிய காலத்திற்குள் முறையாகத் திருப்பிச் செலுத்தும் விவசாயிகளுக்கு மாநில அரசு 100% வட்டி மானியம் வழங்குகிறது; இதனால் விவசாயிகளுக்கு பயிர்க்கடன் முற்றிலும் வட்டியில்லாமல் (0% வட்டி) கிடைக்கிறது.",
            "why_a_en": "Correct. Prompt repayment entitles farmers to 0% interest-free crop loans in Tamil Nadu.",
            "why_a_ta": "சரி. உரிய நேரத்தில் திருப்பிச் செலுத்தினால் 0% வட்டியில்லா பயிர்க்கடன் வழங்கப்படுகிறது.",
            "why_b_en": "Incorrect. 7% is the base rate subsidized by the government.",
            "why_b_ta": "தவறு. 7% என்பது அரசு மானியம் வழங்கும் அடிப்படை வட்டி.",
            "why_c_en": "Incorrect. 12% applies to overdue defaulters.",
            "why_c_ta": "தவறு. 12% தவணை தவறியவர்களுக்குப் பொருந்தும்.",
            "why_d_en": "Incorrect. Compound interest is prohibited on agricultural crop loans.",
            "why_d_ta": "தவறு. பயிர்க்கடன்களுக்கு கூட்டு வட்டி விதிக்கப்படுவதில்லை.",
            "tip_en": "Over Rs. 14,000 crore of interest-free crop loans are disbursed annually through PACS in Tamil Nadu.",
            "tip_ta": "தமிழ்நாட்டில் ஆண்டுதோறும் ரூ. 14,000 கோடிக்கும் அதிகமான வட்டியில்லா பயிர்க்கடன்கள் PACS மூலம் வழங்கப்படுகின்றன.",
            "fact_en": "The scheme protects small and marginal farmers from local usurious private moneylenders.",
            "fact_ta": "இத்திட்டம் சிறு மற்றும் குறு விவசாயிகளை கந்துவட்டிக்காரர்களிடமிருந்து பாதுகாக்கிறது."
        },

        # 43. Multi-State Cooperative Societies Rules - Audit Norms
        {
            "subtopic": "Multi-State Co-operative Governance",
            "stem_en": "Under the Multi-State Co-operative Societies Act, 2002, who among the following CANNOT be appointed as an auditor of a multi-state cooperative society?",
            "stem_ta": "2002-ஆம் ஆண்டின் பல்மாநில கூட்டுறவு சங்கங்கள் சட்டத்தின் கீழ், பின்வருவனவற்றில் யார் ஒரு பல்மாநில கூட்டுறவு சங்கத்தின் தணிக்கையாளராக நியமிக்கப்பட முடியாது?",
            "options": [
                ("An officer or employee of the multi-state co-operative society or a person who is a partner of an officer of the society", "பல்மாநில கூட்டுறவு சங்கத்தின் ஓர் அதிகாரி அல்லது பணியாளர், அல்லது சங்க அதிகாரியின் வணிகக் கூட்டாளியாக உள்ள ஒரு நபர்"),
                ("An independent Chartered Accountant holding a valid certificate of practice", "செல்லுபடியாகும் தொழில் சான்றிதழ் கொண்ட ஒரு சுதந்திரமான பட்டயக் கணக்காளர்"),
                ("A reputed auditing firm comprising Chartered Accountants", "பட்டயக் கணக்காளர்களைக் கொண்ட ஒரு புகழ்பெற்ற தணிக்கை நிறுவனம்"),
                ("An auditor on the panel approved by the Central Registrar", "மத்தியப் பதிவாளரால் அங்கீகரிக்கப்பட்ட பட்டியலில் உள்ள தணிக்கையாளர்")
            ],
            "correct_key": "A",
            "exp_en": "Section 70 of the MSCS Act explicitly disqualifies officers, employees, persons indebted to the society for over Rs. 1,000, or partners/employees of officers from being appointed as auditors to maintain uncompromising professional audit independence.",
            "exp_ta": "MSCS சட்டத்தின் பிரிவு 70, தணிக்கை தன்னாட்சியைப் பேணுவதற்காக சங்கத்தின் அதிகாரிகள், ஊழியர்கள், சங்கத்திற்கு ரூ. 1,000-க்கு மேல் கடன்பட்டவர்கள் அல்லது அதிகாரிகளின் கூட்டாளிகள் தணிக்கையாளராக நியமிக்கப்படுவதை வெளிப்படையாகத் தகுதி நீக்கம் செய்கிறது.",
            "why_a_en": "Correct. Officers or employees cannot audit their own institution due to conflict of interest.",
            "why_a_ta": "சரி. அதிகாரிகள் அல்லது ஊழியர்கள் நலன் முரண்பாடு காரணமாக தணிக்கை செய்ய முடியாது.",
            "why_b_en": "Incorrect. Independent CAs are the primary qualified auditors.",
            "why_b_ta": "தவறு. சுதந்திரமான பட்டயக் கணக்காளர்களே தகுதியான தணிக்கையாளர்கள்.",
            "why_c_en": "Incorrect. CA firms are routinely appointed.",
            "why_c_ta": "தவறு. தணிக்கை நிறுவனங்கள் நியமிக்கப்படலாம்.",
            "why_d_en": "Incorrect. Central Registrar panel auditors are fully eligible.",
            "why_d_ta": "தவறு. மத்தியப் பதிவாளர் பட்டியலில் உள்ளவர்கள் தகுதியுடையவர்கள்.",
            "tip_en": "Disqualifications mirror Section 141 of the Companies Act, 2013 regarding auditor independence.",
            "tip_ta": "இந்த தகுதியிழப்புகள் நிறுவனங்கள் சட்டம் 2013-ன் பிரிவு 141-ன் தணிக்கையாளர் தன்னாட்சி விதிகளைப் போன்றது.",
            "fact_en": "The auditor must report whether the balance sheet gives a true and fair view of the society's financial state.",
            "fact_ta": "இருப்புநிலைக் குறிப்பு சங்கத்தின் நிதிநிலையின் உண்மையான மற்றும் நியாயமான பார்வையைத் தருகிறதா என்பதை தணிக்கையாளர் தெரிவிக்க வேண்டும்."
        },

        # 44. Central Registrar Powers of Supersession
        {
            "subtopic": "Multi-State Co-operative Governance",
            "stem_en": "Under Section 123 of the Multi-State Co-operative Societies Act, 2002, in which of the following circumstances can the Central Government supersede the board of a multi-state cooperative society?",
            "stem_ta": "2002-ஆம் ஆண்டின் பல்மாநில கூட்டுறவு சங்கங்கள் சட்டத்தின் பிரிவு 123-ன் கீழ், பின்வரும் எந்தச் சூழ்நிலையில் மத்திய அரசு ஒரு பல்மாநில கூட்டுறவு சங்கத்தின் வாரியத்தை இடைநீக்கம் செய்ய முடியும்?",
            "options": [
                ("Where the Central Government has contributed not less than 51% of paid-up share capital or guaranteed repayment of principal and interest, and the board has persistently made default", "மத்திய அரசு செலுத்தப்பட்ட பங்கு மூலதனத்தில் 51%-க்கு குறையாமல் பங்களித்திருக்கும் போது அல்லது அசல் மற்றும் வட்டி திருப்பிச் செலுத்துவதற்கு உத்தரவாதம் அளித்திருக்கும் போது, மற்றும் வாரியம் தொடர்ந்து தவறிழைத்தால்"),
                ("Whenever the Central Government desires to appoint a party politician as chairman", "அரசியல்வாதியை தலைவராக நியமிக்க மத்திய அரசு விரும்பும் போதெல்லாம்"),
                ("Where the society operates with 100% private member funds and makes substantial profit", "சங்கம் 100% தனியார் உறுப்பினர் நிதியுடன் செயல்பட்டு அதிக லாபம் ஈட்டும் போது"),
                ("Where the society expands into two new states without borrowing government money", "அரசு கடன் வாங்காமல் இரண்டு புதிய மாநிலங்களில் சங்கம் விரிவடையும் போது")
            ],
            "correct_key": "A",
            "exp_en": "Section 123 of the MSCS Act permits supersession by the Central Government only where the government has contributed at least 51% of the paid-up share capital or guaranteed the loans, and there is persistent default, negligence, or an impasse in the board.",
            "exp_ta": "MSCS சட்டத்தின் பிரிவு 123, மத்திய அரசு குறைந்தபட்சம் 51% பங்கு மூலதனத்தை வழங்கியிருந்தால் அல்லது கடன்களுக்கு உத்தரவாதம் அளித்திருந்தால் மட்டுமே, மற்றும் தொடர் தவறிழைப்பு அல்லது முட்டுக்கட்டை ஏற்பட்டால் மட்டுமே வாரியத்தை இடைநீக்கம் செய்ய அனுமதிக்கிறது.",
            "why_a_en": "Correct. At least 51% government equity/guarantee is a statutory prerequisite for central supersession.",
            "why_a_ta": "சரி. குறைந்தபட்சம் 51% அரசுப் பங்கு அல்லது உத்தரவாதம் இடைநீக்கத்திற்கு அவசியமான சட்டப்பூர்வ நிபந்தனையாகும்.",
            "why_b_en": "Incorrect. Political appointments are an abuse of power and struck down by courts.",
            "why_b_ta": "தவறு. அரசியல் நியமனங்கள் நீதிமன்றங்களால் ரத்து செய்யப்படுகின்றன.",
            "why_c_en": "Incorrect. Autonomous societies without government equity cannot be superseded.",
            "why_c_ta": "தவறு. அரசு பங்கு இல்லாத தன்னாட்சி சங்கங்களை இடைநீக்கம் செய்ய முடியாது.",
            "why_d_en": "Incorrect. Interstate expansion is legal under the Act.",
            "why_d_ta": "தவறு. மாநிலங்களுக்கு இடையே விரிவடைவது சட்டப்படியானது.",
            "tip_en": "Notice period: The board must be given a show cause notice of at least 15 days before supersession.",
            "tip_ta": "இடைநீக்கத்திற்கு முன் வாரியத்திற்கு குறைந்தபட்சம் 15 நாட்கள் விளக்கம் கேட்கும் நோட்டீஸ் வழங்கப்பட வேண்டும்.",
            "fact_en": "Administrator is appointed for a period not exceeding 6 months under the 2023 amendment.",
            "fact_ta": "2023 திருத்தத்தின் கீழ் அதிகபட்சம் 6 மாத காலத்திற்கு மட்டுமே நிர்வாகி நியமிக்கப்படுகிறார்."
        },

        # 45. Producer Cooperatives vs Producer Companies
        {
            "subtopic": "Comparative Institutional Forms",
            "stem_en": "Introduced by the Companies (Amendment) Act, 2002 on the recommendation of the Y.K. Alagh Committee, what is a 'Producer Company'?",
            "stem_ta": "ஒய்.கே. அலக் குழுவின் பரிந்துரையின் பேரில் 2002-ஆம் ஆண்டின் நிறுவனங்கள் (திருத்தச்) சட்டத்தால் அறிமுகப்படுத்தப்பட்ட 'உற்பத்தியாளர் நிறுவனம்' (Producer Company) என்பது என்ன?",
            "options": [
                ("A hybrid corporate entity combining the cooperative ethos of mutual assistance with the professional flexibility and capital discipline of a private limited company", "பரஸ்பர உதவியின் கூட்டுறவுக் கொள்கையையும், ஒரு தனியார் நிறுவனத்தின் தொழில்முறை நெகிழ்வுத்தன்மை மற்றும் மூலதன ஒழுக்கத்தையும் இணைக்கும் ஒரு கலப்பின கார்ப்பரேட் அமைப்பு"),
                ("A state government department run by civil servants", "அரசு ஊழியர்களால் நடத்தப்படும் ஒரு மாநில அரசுத் துறை"),
                ("A charitable trust exempt from all commercial accounting", "வணிகக் கணக்குப்பதிவிலிருந்து விலக்கு அளிக்கப்பட்ட ஒரு தொண்டு அறக்கட்டளை"),
                ("An unincorporated association of agricultural laborers without legal personality", "சட்டப்பூர்வ ஆளுமை இல்லாத விவசாயத் தொழிலாளர்களின் பதிவு செய்யப்படாத சங்கம்")
            ],
            "correct_key": "A",
            "exp_en": "Farmer Producer Companies (FPCs), formulated under Part IX-A of the Companies Act 1956 (now Chapter XXI-A of Companies Act 2013) on Dr. Y.K. Alagh Committee recommendations, blend cooperative democratic principles ('One member, one vote', limited dividend) with the freedom from bureaucratic Registrar interference enjoyed by private companies.",
            "exp_ta": "டாக்டர் ஒய்.கே. அலக் குழுவின் பரிந்துரைகளின் அடிப்படையில் நிறுவனங்கள் சட்டத்தின் கீழ் உருவாக்கப்பட்ட உழவர் உற்பத்தியாளர் நிறுவனங்கள் (FPCs), கூட்டுறவு ஜனநாயகக் கொள்கைகளை ('ஒரு உறுப்பினர், ஒரு வாக்கு') தனியார் நிறுவனங்களின் அதிகாரத்துவ தலையீடற்ற சுதந்திரத்துடன் இணைக்கின்றன.",
            "why_a_en": "Correct. Hybrid combining cooperative democratic principles with corporate flexibility.",
            "why_a_ta": "சரி. கூட்டுறவு ஜனநாயகக் கொள்கைகளையும் கார்ப்பரேட் நெகிழ்வுத்தன்மையையும் இணைக்கும் கலப்பின அமைப்பு.",
            "why_b_en": "Incorrect. FPCs are owned by primary farmers, not civil servants.",
            "why_b_ta": "தவறு. FPC-கள் விவசாயிகளுக்குச் சொந்தமானவை.",
            "why_c_en": "Incorrect. FPCs are commercial business entities under Companies Act.",
            "why_c_ta": "தவறு. FPC-கள் நிறுவனச் சட்டத்தின் கீழ் உள்ள வணிக நிறுவனங்கள்.",
            "why_d_en": "Incorrect. FPCs are incorporated bodies corporate registered with ROC.",
            "why_d_ta": "தவறு. FPC-கள் நிறுவனப் பதிவாளரிடம் (ROC) பதிவு செய்யப்பட்ட அமைப்புகள்.",
            "tip_en": "FPC = Regulated by Registrar of Companies (ROC) under Ministry of Corporate Affairs, NOT by state Cooperative Registrar.",
            "tip_ta": "FPC = கார்ப்பரேட் விவகார அமைச்சகத்தின் நிறுவனப் பதிவாளரால் (ROC) ஒழுங்குபடுத்தப்படுகிறது, கூட்டுறவுப் பதிவாளரால் அல்ல.",
            "fact_en": "Over 10,000 FPOs/FPCs are being formed across India under a dedicated Central Scheme.",
            "fact_ta": "மத்திய அரசின் சிறப்புத் திட்டத்தின் கீழ் இந்தியா முழுவதும் 10,000-க்கும் மேற்பட்ட FPO/FPC-கள் உருவாக்கப்பட்டு வருகின்றன."
        },

        # 46. District Central Cooperative Banks (DCCBs) in Tamil Nadu
        {
            "subtopic": "Tamil Nadu Cooperative Credit",
            "stem_en": "How many District Central Co-operative Banks (DCCBs) currently function in Tamil Nadu forming the intermediate tier of the rural credit structure?",
            "stem_ta": "தமிழ்நாட்டில் ஊரகக் கடன் கட்டமைப்பின் இடைநிலை அடுக்காக தற்போது எத்தனை மாவட்ட மத்தியக் கூட்டுறவு வங்கிகள் (DCCBs) செயல்படுகின்றன?",
            "options": [
                ("23 DCCBs", "23 மாவட்ட மத்தியக் கூட்டுறவு வங்கிகள்"),
                ("38 DCCBs (one in every revenue district)", "38 மாவட்ட மத்தியக் கூட்டுறவு வங்கிகள் (ஒவ்வொரு மாவட்டத்திலும் ஒன்று)"),
                ("5 DCCBs", "5 மாவட்ட மத்தியக் கூட்டுறவு வங்கிகள்"),
                ("50 DCCBs", "50 மாவட்ட மத்தியக் கூட்டுறவு வங்கிகள்")
            ],
            "correct_key": "A",
            "exp_en": "In Tamil Nadu, there are 23 District Central Co-operative Banks (DCCBs) operating across the state (several DCCBs have jurisdiction over more than one revenue district, such as the Kancheepuram DCCB covering Kancheepuram, Chengalpattu, and Tiruvallur).",
            "exp_ta": "தமிழ்நாட்டில் 23 மாவட்ட மத்தியக் கூட்டுறவு வங்கிகள் (DCCBs) செயல்படுகின்றன (காஞ்சிபுரம், செங்கல்பட்டு மற்றும் திருவள்ளூரை உள்ளடக்கிய காஞ்சிபுரம் DCCB போன்ற சில DCCB-கள் ஒன்றுக்கு மேற்பட்ட வருவாய் மாவட்டங்களை உள்ளடக்கிய அதிகார வரம்பைக் கொண்டுள்ளன).",
            "why_a_en": "Correct. Exactly 23 DCCBs operate in Tamil Nadu.",
            "why_a_ta": "சரி. தமிழ்நாட்டில் சரியாக 23 மாவட்ட மத்திய கூட்டுறவு வங்கிகள் செயல்படுகின்றன.",
            "why_b_en": "Incorrect. There are 38 revenue districts, but DCCBs were not reorganized for each new district, remaining at 23.",
            "why_b_ta": "தவறு. 38 வருவாய் மாவட்டங்கள் இருந்தாலும், DCCB-களின் எண்ணிக்கை 23 ஆகவே உள்ளது.",
            "why_c_en": "Incorrect. 5 is far too few.",
            "why_c_ta": "தவறு. 5 மிகக் குறைவு.",
            "why_d_en": "Incorrect. 50 exceeds the number of districts.",
            "why_d_ta": "தவறு. 50 மாவட்டங்களின் எண்ணிக்கையை விட அதிகம்.",
            "tip_en": "DCCBs mobilize urban deposits and channel refinance to village PACS for agricultural lending.",
            "tip_ta": "DCCB-கள் வைப்புகளைத் திரட்டி, கிராமத்து PACS-களுக்கு விவசாயக் கடன்களுக்காக மறுநிதியளிப்பை வழங்குகின்றன.",
            "fact_en": "All 23 DCCBs in Tamil Nadu are licensed by the Reserve Bank of India.",
            "fact_ta": "தமிழ்நாட்டில் உள்ள அனைத்து 23 DCCB-களும் இந்திய ரிசர்வ் வங்கியால் உரிமம் பெற்றவை."
        },

        # 47. Surcharge Limitation Period in Tamil Nadu
        {
            "subtopic": "Tamil Nadu Cooperative Governance",
            "stem_en": "Under Section 87 of the Tamil Nadu Co-operative Societies Act, 1983, what is the maximum period of limitation from the date of the alleged act or omission within which surcharge proceedings must be commenced?",
            "stem_ta": "தமிழ்நாடு கூட்டுறவு சங்கங்கள் சட்டம் 1983-ன் பிரிவு 87-ன் கீழ், குற்றம் சாட்டப்பட்ட செயல் அல்லது குறைபாடு நிகழ்ந்த தேதியிலிருந்து எத்தனை ஆண்டுகளுக்குள் சர்சார்ஜ் நடவடிக்கைகள் தொடங்கப்பட வேண்டும் என்ற கால வரம்பு விதிக்கப்பட்டுள்ளது?",
            "options": [
                ("Within 7 years", "7 ஆண்டுகளுக்குள்"),
                ("Within 1 year", "1 ஆண்டிற்குள்"),
                ("Within 30 days", "30 நாட்களுக்குள்"),
                ("No limitation period applies", "எந்தக் கால வரம்பும் பொருந்தாது")
            ],
            "correct_key": "A",
            "exp_en": "The second proviso to Section 87(1) of the TN Co-operative Societies Act, 1983 provides that no surcharge proceeding shall be commenced after the expiry of 7 years from the date of any act or omission giving rise to such proceeding.",
            "exp_ta": "1983 தமிழ்நாடு கூட்டுறவு சங்கங்கள் சட்டத்தின் பிரிவு 87(1) இரண்டாவது வரம்பு, சர்சார்ஜ் நடவடிக்கைக்கான செயல் அல்லது குறைபாடு நிகழ்ந்த தேதியிலிருந்து 7 ஆண்டுகள் முடிந்த பிறகு எந்த நடவடிக்கையும் தொடங்கப்படக் கூடாது என்று கூறுகிறது.",
            "why_a_en": "Correct. 7 years is the statutory limitation period under Section 87.",
            "why_a_ta": "சரி. பிரிவு 87-ன் கீழ் சட்டப்பூர்வ கால வரம்பு 7 ஆண்டுகள் ஆகும்.",
            "why_b_en": "Incorrect. 1 year is too short for uncovering complex financial frauds.",
            "why_b_ta": "தவறு. நிதி முறைகேடுகளைக் கண்டறிய 1 ஆண்டு போதாது.",
            "why_c_en": "Incorrect. 30 days applies to procedural notices.",
            "why_c_ta": "தவறு. 30 நாட்கள் நோட்டீஸிற்குப் பொருந்தும்.",
            "why_d_en": "Incorrect. An indefinite limitation period would lead to endless harassment of retired officers.",
            "why_d_ta": "தவறு. கால வரம்பு இல்லாமல் இருக்க முடியாது.",
            "tip_en": "Madras High Court has repeatedly quashed surcharge notices issued after the 7-year statutory limitation.",
            "tip_ta": "7 ஆண்டு கால வரம்பிற்குப் பிறகு பிறப்பிக்கப்பட்ட சர்சார்ஜ் உத்தரவுகளை மெட்ராஸ் உயர் நீதிமன்றம் பலமுறை ரத்து செய்துள்ளது.",
            "fact_en": "Once initiated, the surcharge inquiry itself should be completed within 6 months.",
            "fact_ta": "தொடங்கப்பட்டவுடன், சர்சார்ஜ் விசாரணை 6 மாதங்களுக்குள் முடிக்கப்பட வேண்டும்."
        },

        # 48. Tribal Cooperative Apex - Marketing of Minor Forest Produce
        {
            "subtopic": "Tribal Cooperatives",
            "stem_en": "Which constitutional and legal provision empowers tribal gatherers of Minor Forest Produce (MFP) in Fifth Schedule areas to enjoy ownership rights over non-timber forest produce, coordinated through cooperatives?",
            "stem_ta": "ஐந்தாவது அட்டவணைப் பகுதிகளில் உள்ள சிறு வன உற்பத்திப் பொருட்கள் (MFP) சேகரிக்கும் பழங்குடியினருக்கு, மரமல்லாத வனப் பொருட்கள் மீதான உரிமை அதிகாரத்தை கூட்டுறவுகள் மூலம் ஒருங்கிணைக்க அதிகாரம் அளிக்கும் அரசியலமைப்பு மற்றும் சட்டப்பூர்வ விதி எது?",
            "options": [
                ("Panchayats (Extension to the Scheduled Areas) Act, 1996 (PESA) and Forest Rights Act, 2006 (FRA)", "பஞ்சாயத்துகள் (பட்டியலிடப்பட்ட பகுதிகளுக்கான நீட்டிப்பு) சட்டம் 1996 (PESA) மற்றும் வன உரிமைகள் சட்டம் 2006 (FRA)"),
                ("Indian Forest Act, 1927 exclusively", "1927-ஆம் ஆண்டின் இந்திய வனச் சட்டம் மட்டுமே"),
                ("Wildlife Protection Act, 1972", "வனவிலங்கு பாதுகாப்புச் சட்டம் 1972"),
                ("Armed Forces Special Powers Act, 1958", "ஆயுதப்படை சிறப்பு அதிகாரங்கள் சட்டம் 1958")
            ],
            "correct_key": "A",
            "exp_en": "Section 4(m)(ii) of PESA Act, 1996 and Section 3(1)(c) of the Forest Rights Act (FRA), 2006 vest the ownership of Minor Forest Produce (MFP) in the Gram Sabha and tribal forest dwellers. TRIFED and Large-Sized Adivasi Multi-Purpose Societies (LAMPS) organize marketing to ensure fair prices.",
            "exp_ta": "1996 PESA சட்டத்தின் பிரிவு 4(m)(ii) மற்றும் 2006 வன உரிமைகள் சட்டத்தின் பிரிவு 3(1)(c) ஆகியவை சிறு வன உற்பத்திப் பொருட்களின் (MFP) உரிமையை கிராம சபை மற்றும் பழங்குடியின மக்களுக்கு வழங்குகின்றன. TRIFED மற்றும் LAMPS கூட்டுறவுகள் நியாயமான விலையை உறுதி செய்ய சந்தைப்படுத்தலை ஒருங்கிணைக்கின்றன.",
            "why_a_en": "Correct. PESA 1996 and FRA 2006 legally recognize tribal community ownership of MFP.",
            "why_a_ta": "சரி. PESA 1996 மற்றும் FRA 2006 பழங்குடியினரின் வனப் பொருட்கள் உரிமையை சட்டப்பூர்வமாக அங்கீகரிக்கின்றன.",
            "why_b_en": "Incorrect. The colonial 1927 Act established state monopoly over forests.",
            "why_b_ta": "தவறு. 1927 காலனித்துவ சட்டம் காடுகள் மீது அரசின் ஆதிக்கத்தை நிறுவியது.",
            "why_c_en": "Incorrect. Wildlife Act created national parks and wildlife sanctuaries.",
            "why_c_ta": "தவறு. வனவிலங்கு பாதுகாப்புச் சட்டம் சரணாலயங்களை உருவாக்கியது.",
            "why_d_en": "Incorrect. AFSPA is a security and counter-insurgency law.",
            "why_d_ta": "தவறு. AFSPA ஒரு பாதுகாப்புச் சட்டம்.",
            "tip_en": "LAMPS (Large-Sized Adivasi Multi-Purpose Societies) operate at the block/village level in tribal belts.",
            "tip_ta": "LAMPS கூட்டுறவுகள் பழங்குடியினர் பகுதிகளில் வட்டார அளவில் செயல்படுகின்றன.",
            "fact_en": "Minor Forest Produce includes honey, tamarind, lac, gum, tendu patta, and herbal medicinal plants.",
            "fact_ta": "சிறு வனப் பொருட்களில் தேன், புளி, அரக்கு, பிசின், தெண்டு இலைகள் மற்றும் மூலிகைகள் அடங்கும்."
        },

        # 49. LAMPS in Tamil Nadu
        {
            "subtopic": "Tamil Nadu Tribal Cooperatives",
            "stem_en": "In the hilly tribal tracts of Tamil Nadu (such as Kolli Hills, Jawadhu Hills, Kalrayan Hills, and Anamalai), which cooperative institutions provide credit and market non-timber forest produce for tribal members?",
            "stem_ta": "தமிழ்நாட்டின் மலைவாழ் பழங்குடியினர் பகுதிகளில் (கொல்லி மலை, ஜவ்வாது மலை, கல்வராயன் மலை மற்றும் ஆனைமலை போன்றவை), பழங்குடி உறுப்பினர்களுக்குக் கடன் வழங்கி வனப் பொருட்களை சந்தைப்படுத்தும் கூட்டுறவு நிறுவனங்கள் எவை?",
            "options": [
                ("Large-Sized Adivasi Multi-Purpose Cooperative Societies (LAMPS)", "பெரிய அளவிலான ஆதிவாசி பல்நோக்குக் கூட்டுறவு சங்கங்கள் (LAMPS)"),
                ("Urban Co-operative Credit Banks exclusively", "நகர்ப்புறக் கூட்டுறவுக் கடன் வங்கிகள் மட்டுமே"),
                ("Chambers of Commerce and Industry", "வணிக மற்றும் தொழில்துறை கூட்டமைப்புகள்"),
                ("State Industrial Promotion Corporation of Tamil Nadu (SIPCOT)", "சிப்காட் (SIPCOT) நிறுவனம்")
            ],
            "correct_key": "A",
            "exp_en": "Large-Sized Adivasi Multi-Purpose Cooperative Societies (LAMPS) function specifically in the Integrated Tribal Development Programme (ITDP) areas of Tamil Nadu to provide interest-free crop loans, distribute consumer articles, and procure minor forest produce from tribal members at fair prices.",
            "exp_ta": "தமிழ்நாட்டின் ஒருங்கிணைந்த பழங்குடியினர் மேம்பாட்டுத் திட்டப் பகுதிகளில் (ITDP) பெரிய அளவிலான ஆதிவாசி பல்நோக்குக் கூட்டுறவு சங்கங்கள் (LAMPS) செயல்பட்டு, வட்டியில்லா பயிர்க்கடன்கள் வழங்கவும், நுகர்பொருட்களை விநியோகிக்கவும், பழங்குடியினரிடமிருந்து வனப் பொருட்களை நியாயமான விலையில் கொள்முதல் செய்யவும் உதவுகின்றன.",
            "why_a_en": "Correct. LAMPS are the specialized grassroots tribal cooperatives in Tamil Nadu.",
            "why_a_ta": "சரி. LAMPS என்பது தமிழ்நாட்டின் பிரத்யேக பழங்குடியினர் கூட்டுறவு சங்கங்களாகும்.",
            "why_b_en": "Incorrect. Urban banks operate in municipal and city centers.",
            "why_b_ta": "தவறு. நகர்ப்புற வங்கிகள் நகரங்களில் செயல்படுகின்றன.",
            "why_c_en": "Incorrect. Chambers of Commerce represent private corporate businesses.",
            "why_c_ta": "தவறு. வணிகக் கூட்டமைப்புகள் கார்ப்பரேட் வர்த்தக அமைப்புகள்.",
            "why_d_en": "Incorrect. SIPCOT sets up industrial parks.",
            "why_d_ta": "தவறு. சிப்காட் தொழிற்பேட்டைகளை அமைக்கிறது.",
            "tip_en": "Tribal honey and organic pepper procured through LAMPS in Kolli and Jawadhu Hills are marketed across Tamil Nadu.",
            "tip_ta": "கொல்லி மற்றும் ஜவ்வாது மலையில் LAMPS மூலம் கொள்முதல் செய்யப்படும் தேன் மற்றும் மிளகு தமிழ்நாடு முழுவதும் விற்கப்படுகின்றன.",
            "fact_en": "There are over 40 functional LAMPS societies in the tribal pockets of Tamil Nadu.",
            "fact_ta": "தமிழ்நாட்டின் பழங்குடியினர் பகுதிகளில் 40-க்கும் மேற்பட்ட LAMPS சங்கங்கள் செயல்படுகின்றன."
        },

        # 50. Seven Cooperative Principles Evolution (Tokyo vs Manchester)
        {
            "subtopic": "Core Principles of Cooperation",
            "stem_en": "When the International Co-operative Alliance (ICA) revised the cooperative principles at the Manchester Congress in 1995, which new 7th principle was added that was absent in the earlier 1966 Vienna/Tokyo formulation?",
            "stem_ta": "1995-ல் மான்செஸ்டர் மாநாட்டில் சர்வதேச கூட்டுறவு கூட்டணி (ICA) கூட்டுறவுக் கொள்கைகளைத் திருத்திய போது, முந்தைய 1966 கொள்கைகளில் இல்லாத எந்தப் புதிய 7-வது கொள்கை சேர்க்கப்பட்டது?",
            "options": [
                ("Concern for Community (sustainable community development)", "சமூகத்தின் மீதான அக்கறை (நிலையான சமூக வளர்ச்சி)"),
                ("Religious Discrimination", "மதப் பாகுபாடு"),
                ("Unlimited Profit Maximization", "வரம்பற்ற லாபத்தை அதிகரித்தல்"),
                ("Compulsory State Ownership", "கட்டாய அரசு உரிமை")
            ],
            "correct_key": "A",
            "exp_en": "The 1966 formulation had 6 principles. The 1995 Manchester Centennial Congress introduced the 7th Principle: 'Concern for Community', obligating cooperatives to work for the sustainable economic, social, and environmental development of their local communities.",
            "exp_ta": "1966-ல் 6 கொள்கைகள் மட்டுமே இருந்தன. 1995 மான்செஸ்டர் நூற்றாண்டு மாநாடு 7-வது கொள்கையாக 'சமூகத்தின் மீதான அக்கறை' என்பதை அறிமுகப்படுத்தியது; இது தங்கள் உள்ளூர் சமூகங்களின் நிலையான பொருளாதார, சமூக மற்றும் சுற்றுச்சூழல் வளர்ச்சிக்காக உழைக்க கூட்டுறவுகளைக் கடமைப்படுத்துகிறது.",
            "why_a_en": "Correct. 'Concern for Community' was the brand-new 7th principle added in 1995.",
            "why_a_ta": "சரி. 'சமூகத்தின் மீதான அக்கறை' என்பது 1995-ல் புதிதாகச் சேர்க்கப்பட்ட 7-வது கொள்கையாகும்.",
            "why_b_en": "Incorrect. Discrimination is strictly forbidden in cooperatives.",
            "why_b_ta": "தவறு. பாகுபாடு கூட்டுறவில் கண்டிப்பாகத் தடை செய்யப்பட்டுள்ளது.",
            "why_c_en": "Incorrect. Cooperatives prioritize service and member welfare, not unbridled profit maximization.",
            "why_c_ta": "தவறு. லாபத்தை அதிகரிப்பது கூட்டுறவின் நோக்கமல்ல.",
            "why_d_en": "Incorrect. Principle 4 is 'Autonomy and Independence' from state control.",
            "why_d_ta": "தவறு. கொள்கை 4 தன்னாட்சி மற்றும் சுதந்திரமாகும்.",
            "tip_en": "The 7 Modern ICA Principles: 1. Voluntary & Open Membership, 2. Democratic Member Control, 3. Member Economic Participation, 4. Autonomy & Independence, 5. Education, Training & Information, 6. Cooperation among Cooperatives, 7. Concern for Community.",
            "tip_ta": "7 நவீன ICA கொள்கைகள்: 1. தன்னார்வ சேர்க்கை, 2. ஜனநாயகக் கட்டுப்பாடு, 3. பொருளாதாரப் பங்களிப்பு, 4. தன்னாட்சி, 5. கல்வி & பயிற்சி, 6. கூட்டுறவுகளுக்குள் கூட்டுறவு, 7. சமூக அக்கறை.",
            "fact_en": "This 7th principle directly aligns cooperative enterprises with the UN Sustainable Development Goals (SDGs).",
            "fact_ta": "இந்த 7-வது கொள்கை கூட்டுறவு நிறுவனங்களை ஐ.நாவின் நிலையான வளர்ச்சி இலக்குகளுடன் (SDGs) நேரடியாக இணைக்கிறது."
        }
    ]


def build_hard_file():
    raw_qs = get_hard_raw_questions()
    print(f"Loaded {len(raw_qs)} raw Hard questions.")
    assert len(raw_qs) == 50, f"Expected 50 questions, got {len(raw_qs)}"

    questions = []
    for idx, item in enumerate(raw_qs, start=1):
        qid = f"CS_H_{idx:03d}"
        opts = item["options"]
        correct_key = item["correct_key"]

        q = make_coop_q(
            qid=qid,
            diff="Hard",
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
            tags=["polity", "cooperative_societies", "hard", item["subtopic"].lower().replace(" ", "_")]
        )
        questions.append(q)

    # Randomize and balance answer keys: 12-13 per option, max run <= 2
    balanced = randomize_and_balance_dataset(questions, seed=202)
    key_dist = Counter(q["correct_answer"] for q in balanced)
    print(f"Balanced Key Distribution: {dict(key_dist)}")

    out_dir = os.path.join("data", "questions", "polity")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "cooperative_societies_hard.json")

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(balanced, f, ensure_ascii=False, indent=2)
    print(f"Saved balanced Hard MCQs to {out_path}")

    # Validation
    rep = ContentValidator.validate_file(out_path, expected_count=50, expected_prefix="CS_H_")
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
