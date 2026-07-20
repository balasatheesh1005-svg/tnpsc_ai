import json

def get_part4_questions():
    questions = []
    
    def make_q(id_num, diff, q_type, q_en, q_ta, opt_list, ans, exp_en, exp_ta, wno, tip_en, tip_ta, rf_en, rf_ta, tags, bloom="Understand", est_time=60):
        ans_upper = ans.upper()
        ans_lower = ans.lower()
        
        opts_dict = []
        opts_en = []
        opts_ta = []
        for opt_id, o_en, o_ta in opt_list:
            opts_dict.append({"id": opt_id, "en": o_en, "ta": o_ta})
            opts_en.append(o_en)
            opts_ta.append(o_ta)
            
        return {
            "id": f"HB_GT_{id_num:03d}",
            "subject": "Polity",
            "topic": "Historical Background of the Indian Constitution",
            "difficulty": diff,
            "question_type": q_type,
            "question": {"en": q_en, "ta": q_ta},
            "options": opts_dict,
            "correct_answer": ans_upper,
            "explanation": {"en": exp_en, "ta": exp_ta},
            "why_not_others": wno,
            "tnpsc_tip": {"en": tip_en, "ta": tip_ta},
            "revision_fact": {"en": rf_en, "ta": rf_ta},
            "source_reference": [
                "M. Laxmikanth - Indian Polity",
                "NCERT Class XI/XII - Indian Constitution at Work",
                "Samacheer Kalvi - Standard 11/12 Political Science"
            ],
            "bloom_level": bloom,
            "estimated_time_sec": est_time,
            "pyq_similarity": "High",
            "tags": tags,
            "question_en": q_en,
            "question_ta": q_ta,
            "options_en": opts_en,
            "options_ta": opts_ta,
            "answer": ans_lower,
            "explanation_en": exp_en,
            "explanation_ta": exp_ta
        }

    # Q76: Direct MCQ - Medium - Government of India Act 1935 Public Service Commissions
    questions.append(make_q(
        76, "Medium", "Direct MCQ",
        "The Government of India Act of 1935 provided for the establishment of which Public Service Commissions to handle recruitment across different tiers of administration?",
        "1935 இந்திய அரசுச் சட்டம் நிர்வாகத்தின் பல்வேறு நிலைகளில் ஊழியர் நியமனங்களைக் கையாள எந்த பொதுப்பணி ஆணையங்களை நிறுவ வழிவகை செய்தது?",
        [
            ("A", "Federal Public Service Commission, Provincial Public Service Commission, and Joint Public Service Commission for two or more provinces", "கூட்டாட்சி பொதுப்பணி ஆணையம், மாகாண பொதுப்பணி ஆணையம் மற்றும் இரண்டு அல்லது அதற்கு மேற்பட்ட மாகாணங்களுக்கான கூட்டுப் பொதுப்பணி ஆணையம்"),
            ("B", "Central Public Service Commission only", "மத்திய பொதுப்பணி ஆணையம் மட்டுமே"),
            ("C", "Imperial Civil Service Board only", "ஏகாதிபத்திய சிவில் சர்வீஸ் வாரியம் மட்டுமே"),
            ("D", "District Selection Boards under Collector control", "ஆட்சியர் கட்டுப்பாட்டில் உள்ள மாவட்டத் தேர்வு வாரியங்கள்")
        ],
        "A",
        "Historical Context: Reorganization of civil service recruitment infrastructure to fit the federal structure under 1935 Act.\nReason: 1935 Act established: (1) Federal Public Service Commission (FPSC), (2) Provincial Public Service Commission (PPSC) in each province, and (3) Joint Public Service Commission (JPSC) for two or more provinces.\nConstitutional Impact: Direct statutory blueprint for Part XIV of Indian Constitution (Articles 315-323: UPSC, State PSCs, Joint PSCs).\nExam Trap: 1926 = Central Public Service Commission (Lee Commission); 1935 = Federal, Provincial & Joint PSCs.\nMemory Trick: 1935 PSC Architecture = FPSC (UPSC prototype) + PPSC (State PSC prototype) + JPSC.",
        "வரலாற்றுப் பின்னணி: 1935 சட்டத்தின் கூட்டாட்சி அமைப்பிற்கு ஏற்ப சிவில் சர்வீஸ் நியமனக் கட்டமைப்பை சீரமைத்தல்.\nகாரணம்: 1935 சட்டம் நிறுவ வழிவகுத்தது: (1) கூட்டாட்சி பொதுப்பணி ஆணையம் (FPSC), (2) ஒவ்வொரு மாகாணத்திலும் மாகாண பொதுப்பணி ஆணையம் (PPSC), (3) இரண்டு அல்லது அதற்கு மேற்பட்ட மாகாணங்களுக்கு கூட்டுப் பொதுப்பணி ஆணையம் (JPSC).\nஅரசியலமைப்பு தாக்கம்: இந்திய அரசியலமைப்பின் பகுதி XIV-க்கு (சரத்துகள் 315-323: UPSC, மாநில PSC, கூட்டு PSC) நேரடி சட்ட வரைபடம்.\nதேர்வுப் பொறி: 1926 = மத்திய பொதுப்பணி ஆணையம் (லீ குழு); 1935 = கூட்டாட்சி, மாகாண & கூட்டு PSC-கள்.\nநினைவுச் சூத்திரம்: 1935 PSC கட்டமைப்பு = FPSC (UPSC முன்மாதிரி) + PPSC (மாநில PSC முன்மாதிரி) + JPSC.",
        {
            "A": {"en": "Correct. 1935 Act established Federal, Provincial, and Joint Public Service Commissions.", "ta": "சரி. 1935 சட்டம் கூட்டாட்சி, மாகாண மற்றும் கூட்டுப் பொதுப்பணி ஆணையங்களை நிறுவியது."},
            "B": {"en": "Incorrect. Central PSC was set up earlier in 1926 under 1919 Act/Lee Commission.", "ta": "தவறு. மத்திய PSC 1926-லேயே அமைக்கப்பட்டது."},
            "C": {"en": "Incorrect. Imperial Board was replaced by formal PSCs.", "ta": "தவறு. ஏட்சின்சன் கால பலகைகள் மாற்றப்பட்டன."},
            "D": {"en": "Incorrect. District boards were not part of 1935 statutory PSC clauses.", "ta": "தவறு. மாவட்ட வாரியங்கள் 1935 PSC விதிகளில் இல்லை."}
        },
        "TNPSC Trap: Madras Service Commission (predecessor to TNPSC) was established in 1929, making it the first Provincial PSC in India.",
        "TNPSC பொறி: மதராஸ் சேவை ஆணையம் (TNPSC-ன் முன்னோடி) 1929-ல் அமைக்கப்பட்டது, இது இந்தியாவின் முதல் மாகாண PSC ஆகும்.",
        "Federal Public Service Commission created in 1935 became the Union Public Service Commission (UPSC) on January 26, 1950.",
        "1935-ல் உருவான கூட்டாட்சி பொதுப்பணி ஆணையம் 1950 ஜனவரி 26 அன்று மத்திய பொதுப்பணி ஆணையமாக (UPSC) மாறியது.",
        ["Polity", "Historical Background", "GOI Act 1935", "Public Service Commission", "TNPSC Prototype", "Grand Test"], "Understand", 60
    ))

    # Q77: Multi-Act Comparative - Hard - Evolution of Emergency Provisions (Center vs Provinces)
    questions.append(make_q(
        77, "Hard", "Multi-Act Comparative",
        "Which multi-act comparison accurately tracks how emergency breakdown of constitutional machinery evolved from 1919 Act to 1935 Act and into the modern Indian Constitution?",
        "அரசியலமைப்பு பொறிமுறையின் அவசரகால முடக்கம் 1919 சட்டம், 1935 சட்டம் மற்றும் நவீன இந்திய அரசியலமைப்பு வரை எவ்வாறு வளர்ந்தது என்பதைத் துல்லியமாக ஒப்பிடும் முடிவு எது?",
        [
            ("A", "1919 Act had no provision for constitutional emergency -> 1935 Act introduced Section 93 empowering Governor to assume provincial government powers -> Modern Constitution incorporated Section 93 as Article 356 (President's Rule)", "1919 சட்டத்தில் அரசியலமைப்பு அவசரநிலை விதி இல்லை -> 1935 சட்டம் பிரிவு 93 மூலம் கவர்னர் மாகாண அரசைக் கைப்பற்ற அதிகாரம் அளித்தது -> நவீன அரசியலமைப்பு பிரிவு 93-ஐ சரத்து 356 ஆக (குடியரசுத் தலைவர் ஆட்சி) இணைத்துக்கொண்டது"),
            ("B", "1919 Act introduced Article 356 -> 1935 Act abolished it -> Modern Constitution restored it", "1919 சட்டம் சரத்து 356-ஐக் கொண்டுவந்தது -> 1935 சட்டம் அதை ஒழித்தது -> நவீன அரசியலமைப்பு அதை மீட்டெடுத்தது"),
            ("C", "1935 Act introduced Section 93 for Central Government breakdown, which became Article 352", "1935 சட்டம் மத்திய அரசு முடக்கத்திற்கு பிரிவு 93-ஐக் கொண்டுவந்தது, அது சரத்து 352 ஆனது"),
            ("D", "No historical connection exists between Section 93 of 1935 Act and Article 356 of Indian Constitution", "1935 சட்டத்தின் பிரிவு 93-க்கும் இந்திய அரசியலமைப்பின் சரத்து 356-க்கும் எந்த வரலாற்றுத் தொடர்பும் இல்லை")
        ],
        "A",
        "Historical Context: Direct statutory ancestry of emergency breakdown powers in Indian federalism.\nReason: 1919 Act provided Dyarchy but no complete breakdown takeover clause. Section 93 of 1935 Act empowered Provincial Governors, with Governor-General's concurrence, to suspend constitution and assume all executive & legislative powers in case of breakdown. The Constituent Assembly adapted Section 93 almost word-for-word into Article 356 (President's Rule).\nConstitutional Impact: Provided emergency stability mechanism, though frequently misused politically.\nExam Trap: Section 93 of 1935 Act = Article 356 of Indian Constitution.\nMemory Trick: 1935 Section 93 = Article 356 President's Rule Blueprint.",
        "வரலாற்றுப் பின்னணி: இந்தியக் கூட்டாட்சியில் அவசரகால முடக்க அதிகாரங்களின் நேரடி சட்டப்பூர்வ வரலாறு.\nகாரணம்: 1919 சட்டம் இரட்டை ஆட்சியை அளித்தது, ஆனால் முழுமையான முடக்கக் கைப்பற்றல் விதி இல்லை. 1935 சட்டத்தின் பிரிவு 93 கவர்னர்-ஜெனரலின் ஒப்புதலுடன் அரசியலமைப்பை இடைநீக்கம் செய்து அனைத்து அதிகாரங்களையும் கவர்னர் ஏற்க அதிகாரமளித்தது. அரசியல் நிர்ணய சபை பிரிவு 93-ஐ கிட்டத்தட்ட வார்த்தைக்கு வார்த்தை சரத்து 356 ஆக (குடியரசுத் தலைவர் ஆட்சி) மாற்றியமைத்தது.\nஅரசியலமைப்பு தாக்கம்: அவசரகால ஸ்திரத்தன்மை பொறிமுறையை வழங்கியது.\nதேர்வுப் பொறி: 1935 சட்டத்தின் பிரிவு 93 = இந்திய அரசியலமைப்பின் சரத்து 356.\nநினைவுச் சூத்திரம்: 1935 பிரிவு 93 = சரத்து 356 குடியரசுத் தலைவர் ஆட்சி வரைபடம்.",
        {
            "A": {"en": "Correct. Section 93 of 1935 Act was the direct predecessor to Article 356 of Indian Constitution.", "ta": "சரி. 1935 சட்டத்தின் பிரிவு 93 இந்திய அரசியலமைப்பின் சரத்து 356-க்கு நேரடி முன்னோடியாகும்."},
            "B": {"en": "Incorrect. 1919 Act did not contain Article 356.", "ta": "தவறு. 1919 சட்டத்தில் சரத்து 356 இருக்கவில்லை."},
            "C": {"en": "Incorrect. Section 93 applied to Provinces, forming basis for Art 356, not Art 352.", "ta": "தவறு. பிரிவு 93 மாகாணங்களுக்குப் பொருந்தியது (சரத்து 356)."},
            "D": {"en": "Incorrect. Direct word-for-word ancestry exists between Section 93 and Art 356.", "ta": "தவறு. பிரிவு 93-க்கும் சரத்து 356-க்கும் நேரடித் தொடர்பு உண்டு."}
        },
        "TNPSC Trap: Dr. B.R. Ambedkar expressed hope in the Constituent Assembly that Article 356 (derived from Section 93) would remain a 'dead letter', though it became frequently used.",
        "TNPSC பொறி: டாக்டர் பி.ஆர். அம்பேத்கர் அரசியல் நிர்ணய சபையில் சரத்து 356 (பிரிவு 93-லிருந்து வந்தது) ஒரு 'பயன்படாத எழுத்தாக' (dead letter) இருக்கும் என நம்பினார்.",
        "Section 93 of 1935 Act required Proclamation to be approved by British Parliament within 6 months.",
        "1935 சட்டத்தின் பிரிவு 93 பிரகடனம் 6 மாதங்களுக்குள் பிரிட்டிஷ் நாடாளுமன்றத்தால் அங்கீகரிக்கப்பட வேண்டும் எனக் கூறியது.",
        ["Polity", "Historical Background", "GOI Act 1935", "Section 93", "Article 356 Precursor", "Multi-Act Integration", "Grand Test"], "Analyze", 75
    ))

    # Q78: Statement Based - Hard - Indian Independence Act 1947 Paramountcy Lapse
    questions.append(make_q(
        78, "Hard", "Statement Based",
        "Consider the following statements regarding the status of Princely States under the Indian Independence Act of 1947:\n1. British paramountcy over Indian Princely States lapsed with effect from August 15, 1947.\n2. All treaties, agreements, and obligations between the British Crown and the Princely States were terminated.\n3. Princely States were given the freedom either to join the Dominion of India, join the Dominion of Pakistan, or remain independent.\n4. Treaty of Paramountcy automatically integrated all 565 Princely States into the Dominion of India without any negotiation.\nWhich of the statements given above are correct?",
        "1947 இந்திய சுதந்திரச் சட்டத்தின் கீழ் சுதேச சமஸ்தானங்களின் அந்தஸ்து பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. சுதேச சமஸ்தானங்கள் மீதான பிரிட்டிஷ் மேலாதிக்கம் (Paramountcy) ஆகஸ்ட் 15, 1947 முதல் முடிவுக்கு வந்தது.\n2. பிரிட்டிஷ் முடியாட்சிக்கும் சுதேச சமஸ்தானங்களுக்கும் இடையிலான அனைத்து உடன்படிக்கைகளும், ஒப்பந்தங்களும் முடிவுக்கு கொண்டுவரப்பட்டன.\n3. சுதேச சமஸ்தானங்கள் இந்திய டொமினியனில் சேரவோ, பாகிஸ்தான் டொமினியனில் சேரவோ அல்லது சுதந்திரமாக இருக்கவோ சுதந்திரம் வழங்கப்பட்டன.\n4. மேலாதிக்க உடன்படிக்கை எந்தவொரு பேச்சுவார்த்தையுமின்றி 565 சுதேச சமஸ்தானங்களையும் தானாகவே இந்திய டொமினியனுடன் இணைத்தது.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?",
        [
            ("A", "1, 2 and 3 only", "1, 2 மற்றும் 3 மட்டுமே"),
            ("B", "1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
            ("C", "2, 3 and 4 only", "2, 3 மற்றும் 4 மட்டுமே"),
            ("D", "1, 3 and 4 only", "1, 3 மற்றும் 4 மட்டுமே")
        ],
        "A",
        "Historical Context: Legal lapse of British suzerainty over 565 Princely States creating integration challenge.\nReason: Statements 1, 2, and 3 are correct. Statement 4 is incorrect because there was NO automatic integration; Princely States became legally independent upon lapse of paramountcy, creating a crisis until Sardar Vallabhbhai Patel negotiated Instruments of Accession.\nConstitutional Impact: Integration of Princely States into Indian Union (Articles 1–4).\nExam Trap: Lapsed paramountcy did NOT automatically integrate states into India; it gave option to join India, Pakistan, or remain independent.\nMemory Trick: 1947 Paramountcy Lapse = Options: Join India / Join Pakistan / Stay Independent (Sardar Patel integrated them).",
        "வரலாற்றுப் பின்னணி: 565 சுதேச சமஸ்தானங்கள் மீதான பிரிட்டிஷ் மேலாதிக்கத்தின் சட்டப்பூர்வ முடிவு இணைப்புக் சவாலை உருவாக்கியது.\nகாரணம்: கூற்றுகள் 1, 2 மற்றும் 3 சரியானவை. கூற்று 4 தவறானது, ஏனெனில் தானியங்கி இணைப்பு எதுவும் நடக்கவில்லை; மேலாதிக்கம் முடிந்ததும் சமஸ்தானங்கள் சட்டப்பூர்வமாக சுதந்திரமடைந்தன. சர்தார் வல்லபாய் படேல் இணையுறுதி ஆவணங்கள் மூலம் பேச்சுவார்த்தை நடத்தி இணைத்தார்.\nஅரசியலமைப்பு தாக்கம்: சுதேச சமஸ்தானங்கள் இந்திய ஒன்றியத்துடன் இணைக்கப்பட்டன (சரத்துகள் 1–4).\nதேர்வுப் பொறி: மேலாதிக்க முடிவு சமஸ்தானங்களை தானாக இந்தியாவோடு இணைக்கவில்லை; அது மூன்று தெரிவுகளை அளித்தது.\nநினைவுச் சூத்திரம்: 1947 மேலாதிக்க முடிவு = தெரிவுகள்: இந்தியா / பாகிஸ்தான் / சுதந்திரம் (சர்தார் படேல் இணைத்தார்).",
        {
            "A": {"en": "Correct. Statements 1, 2, and 3 are true; Statement 4 is false as integration required negotiation.", "ta": "சரி. கூற்றுகள் 1, 2, 3 சரி; பேச்சுவார்த்தை தேவைப்பட்டதால் கூற்று 4 தவறு."},
            "B": {"en": "Incorrect. Statement 3 is also correct.", "ta": "தவறு. கூற்று 3-ம் சரியானது."},
            "C": {"en": "Incorrect. Statement 4 is false.", "ta": "தவறு. கூற்று 4 தவறானது."},
            "D": {"en": "Incorrect. Statement 4 is false.", "ta": "தவறு. கூற்று 4 தவறானது."}
        },
        "TNPSC Trap: Junagadh (plebiscite), Hyderabad (police action - Operation Polo), and Jammu & Kashmir (Instrument of Accession) were integrated through special procedures.",
        "TNPSC பொறி: ஜூனாகத் (பொது வாக்கெடுப்பு), ஐதராபாத் (இராணுவ நடவடிக்கை - ஆபரேஷன் போலோ), ஜம்மு & காஷ்மீர் (இணையுறுதி ஆவணம்) ஆகியவை சிறப்பு முறைகளில் இணைக்கப்பட்டன.",
        "States Department for integration was headed by Sardar Vallabhbhai Patel as Minister and V.P. Menon as Secretary.",
        "இணைப்பிற்கான சமஸ்தானங்கள் துறை அமைச்சராக சர்தார் வல்லபாய் படேலும் செயலராக வி.பி. மேனனும் செயல்பட்டனர்.",
        ["Polity", "Historical Background", "Indian Independence Act 1947", "Paramountcy Lapse", "Princely States", "Grand Test"], "Analyze", 75
    ))

    # Q79: Conceptual MCQ - Medium - Regulating Act Court of Directors Oversight
    questions.append(make_q(
        79, "Medium", "Conceptual MCQ",
        "How did the Regulating Act of 1773 strengthen British Parliamentary control over the East India Company's governing body, the Court of Directors?",
        "1773 ஆம் ஆண்டின் ஒழுங்குமுறைச் சட்டம் கிழக்கிந்திய கம்பெனியின் ஆளும் அமைப்பான இயக்குநர்கள் அவை (Court of Directors) மீது பிரிட்டிஷ் நாடாளுமன்றக் கட்டுப்பாட்டை எவ்வாறு வலுப்படுத்தியது?",
        [
            ("A", "By requiring the Court of Directors to submit all correspondence regarding revenue, civil, and military affairs in India to the British Treasury and Secretary of State", "இந்தியாவில் உள்ள வருவாய், சிவில், இராணுவ விவகாரங்கள் தொடர்பான அனைத்து தொடர்புகளையும் பிரிட்டிஷ் கருவூலம் மற்றும் அரசுச் செயலரிடம் சமர்ப்பிக்க இயக்குநர்கள் அவையைக் கட்டாயப்படுத்தியதன் மூலம்"),
            ("B", "By appointing British Cabinet ministers directly to the Court of Directors", "இயக்குநர்கள் அவையில் பிரிட்டிஷ் கேபினட் அமைச்சர்களை நேரடியாக நியமித்ததன் மூலம்"),
            ("C", "By abolishing the Court of Directors and transferring shares to British Parliament", "இயக்குநர்கள் அவையைக் கலைத்துவிட்டு பங்குகளை பிரிட்டிஷ் நாடாளுமன்றத்திற்கு மாற்றியதன் மூலம்"),
            ("D", "By restricting Court of Directors meetings exclusively to Calcutta", "இயக்குநர்கள் அவைக் கூட்டங்களை கொல்கத்தாவிற்கு மட்டும் சுருக்கியதன் மூலம்")
        ],
        "A",
        "Historical Context: First step toward parliamentary regulation of EIC corporate governance.\nReason: The 1773 Act mandated that the Court of Directors (governing body of EIC in London) submit all revenue correspondence to the Chancellor of the Exchequer and all civil/military correspondence to the Secretary of State.\nConstitutional Impact: Laid down statutory reporting obligation of Company management to Crown.\nExam Trap: Board of Control was NOT created in 1773; 1773 required reporting by Court of Directors to Treasury.\nMemory Trick: 1773 Reporting = Court of Directors submits Revenue & Military reports to British Government.",
        "வரலாற்றுப் பின்னணி: கிழக்கிந்திய கம்பெனியின் பெருநிறுவன நிர்வாகத்தை நாடாளுமன்றக் கட்டுப்பாட்டிற்குள் கொண்டுவருவதற்கான முதல் படி.\nகாரணம்: 1773 சட்டம் லண்டனில் உள்ள இயக்குநர்கள் அவை தனது வருவாய் தொடர்புகளை பிரிட்டிஷ் நிதி அமைச்சருக்கும், சிவில்/இராணுவ தொடர்புகளை அரசுச் செயலருக்கும் சமர்ப்பிக்கக் ஆணையிட்டது.\nஅரசியலமைப்பு தாக்கம்: கம்பெனி நிர்வாகம் பிரிட்டிஷ் அரசிற்கு அறிக்கை அளிக்கும் சட்டப்பூர்வ கடமையை நிறுவியது.\nதேர்வுப் பொறி: 1773-ல் கட்டுப்பாட்டு வாரியம் உருவாக்கப்படவில்லை; 1773 இயக்குநர்கள் அவை அறிக்கையளிப்பதைக் கட்டாயமாக்கியது.\nநினைவுச் சூத்திரம்: 1773 அறிக்கையளித்தல் = இயக்குநர்கள் அவை வருவாய், இராணுவ அறிக்கைகளை பிரிட்டிஷ் அரசிற்கு அனுப்புதல்.",
        {
            "A": {"en": "Correct. 1773 Act required Court of Directors to submit revenue and civil/military reports to British Treasury/SOS.", "ta": "சரி. 1773 சட்டம் இயக்குநர்கள் அவை வருவாய், சிவில்/இராணுவ அறிக்கைகளை சமர்ப்பிக்கக் கோரியது."},
            "B": {"en": "Incorrect. British Cabinet ministers were not appointed to Court of Directors.", "ta": "தவறு. கேபினட் அமைச்சர்கள் அவையில் நியமிக்கப்படவில்லை."},
            "C": {"en": "Incorrect. Court of Directors was not abolished in 1773 (abolished in 1858).", "ta": "தவறு. 1773-ல் அவைக் கலைக்கப்படவில்லை."},
            "D": {"en": "Incorrect. Court of Directors operated in East India House, London.", "ta": "தவறு. இயக்குநர்கள் அவை லண்டனில் இயங்கியது."}
        },
        "TNPSC Trap: Court of Directors members had a 4-year tenure under 1773 Act, with one-fourth retiring every year.",
        "TNPSC பொறி: 1773 சட்டத்தின் கீழ் இயக்குநர்கள் அவை உறுப்பினர்கள் 4 ஆண்டு ஆயுளைக் கொண்டிருந்தனர், நான்கில் ஒரு பங்கு உறுப்பினர்கள் ஒவ்வொரு ஆண்டும் ஓய்வுபெற்றனர்.",
        "Court of Directors comprised 24 directors elected by the Proprietors of the East India Company.",
        "இயக்குநர்கள் அவை கிழக்கிந்திய கம்பெனி பங்குதாரர்களால் தேர்ந்தெடுக்கப்பட்ட 24 இயக்குநர்களைக் கொண்டிருந்தது.",
        ["Polity", "Historical Background", "Regulating Act 1773", "Court of Directors", "Grand Test"], "Understand", 60
    ))

    # Q80: Multi-Act Comparative - Hard - Evolution of Emergency Provisions Blueprint
    questions.append(make_q(
        80, "Hard", "Multi-Act Comparative",
        "Which landmark provision of the Government of India Act 1935 empowered the Central Legislature to enact laws on Provincial subjects during a proclaimed emergency, forming the direct statutory source for Article 250 / Article 352 of the Indian Constitution?",
        "1935 இந்திய அரசுச் சட்டத்தின் எந்த முக்கிய விதி, பிரகடனப்படுத்தப்பட்ட அவசர காலத்தில் மாகாணத் துறைகளில் சட்டமியற்ற மத்திய சட்டமன்றத்திற்கு அதிகாரமளித்து, இந்திய அரசியலமைப்பின் சரத்து 250 / சரத்து 352-க்கு நேரடி சட்ட மூலமாக அமைந்தது?",
        [
            ("A", "Section 102 (Proclamation of Emergency)", "பிரிவு 102 (அவசரநிலை பிரகடனம் - Proclamation of Emergency)"),
            ("B", "Section 93 (Provincial Governor Emergency)", "பிரிவு 93 (மாகாண கவர்னர் அவசரநிலை)"),
            ("C", "Section 45 (Federal Failure Emergency)", "பிரிவு 45 (கூட்டாட்சி முடக்க அவசரநிலை)"),
            ("D", "Section 12 (Special Responsibilities)", "பிரிவு 12 (சிறப்புப் பொறுப்புகள்)")
        ],
        "A",
        "Historical Context: Statutory origins of central legislative intervention during national emergency in Indian federalism.\nReason: Section 102 of 1935 Act authorized the Federal Legislature, upon a Proclamation of Emergency issued by Governor-General, to make laws for a province with respect to any matter in the Provincial Legislative List. This became the exact prototype for Article 250 (Parliament's power to legislate on State List during Emergency) and Article 352 (National Emergency).\nConstitutional Impact: Reinforced central supremacy during national security crises.\nExam Trap: Section 93 = Article 356 (State Emergency); Section 102 = Article 250/352 (National Emergency/State List takeover).\nMemory Trick: 1935 Section 102 = Article 250 (Central law on State list during Emergency).",
        "வரலாற்றுப் பின்னணி: இந்தியக் கூட்டாட்சியில் தேசிய அவசர காலத்தில் மத்திய சட்டமன்றத் தலையீட்டின் சட்டப்பூர்வ மூலங்கள்.\nகாரணம்: 1935 சட்டத்தின் பிரிவு 102, கவர்னர்-ஜெனரல் பிறப்பிக்கும் அவசரநிலை பிரகடனத்தின் போது மாகாணப் பட்டியலில் உள்ள எந்தவொரு விவகாரத்திலும் மாகாணத்திற்காக சட்டமியற்ற கூட்டாட்சி சட்டமன்றத்திற்கு அதிகாரமளித்தது. இது சரத்து 250 (அவசர காலத்தில் மாநிலப் பட்டியலில் நாடாளுமன்றச் சட்டம்) மற்றும் சரத்து 352 (தேசிய அவசரநிலை) ஆகியவற்றிற்கு துல்லியமான மாதிரியானது.\nஅரசியலமைப்பு தாக்கம்: தேசிய பாதுகாப்பு நெருக்கடியின் போது மத்திய உயர்வை உறுதிப்படுத்தியது.\nதேர்வுப் பொறி: பிரிவு 93 = சரத்து 356 (மாநில அவசரநிலை); பிரிவு 102 = சரத்து 250/352 (தேசிய அவசரநிலை/மாநிலப் பட்டியல் அதிகாரம்).\nநினைவுச் சூத்திரம்: 1935 பிரிவு 102 = சரத்து 250 (அவசர காலத்தில் மாநிலப் பட்டியலில் மத்திய சட்டம்).",
        {
            "A": {"en": "Correct. Section 102 empowered central legislature to enact laws on provincial list during emergency.", "ta": "சரி. பிரிவு 102 அவசர காலத்தில் மாகாணப் பட்டியலில் சட்டமியற்ற மத்திய சட்டமன்றத்திற்கு அதிகாரமளித்தது."},
            "B": {"en": "Incorrect. Section 93 dealt with failure of provincial constitutional machinery (Art 356).", "ta": "தவறு. பிரிவு 93 மாகாண அரசியலமைப்பு முடக்கம் பற்றியது."},
            "C": {"en": "Incorrect. Section 45 dealt with failure of federal executive machinery.", "ta": "தவறு. பிரிவு 45 கூட்டாட்சி முடக்கம் பற்றியது."},
            "D": {"en": "Incorrect. Section 12 dealt with Governor-General's special responsibilities.", "ta": "தவறு. பிரிவு 12 கவர்னர்-ஜெனரலின் சிறப்புப் பொறுப்புகள் பற்றியது."}
        },
        "TNPSC Trap: Under Section 102 of 1935 Act, central laws enacted for provinces during emergency expired 6 months after emergency ceased, identical to Article 250(2).",
        "TNPSC பொறி: 1935 சட்டத்தின் பிரிவு 102-ன் கீழ் இயற்றப்பட்ட மத்திய சட்டங்கள் அவசரநிலை முடிந்த 6 மாதங்களில் காலாவதியாயின (சரத்து 250(2) போன்றது).",
        "Article 250 of modern Indian Constitution replicates the wording of Section 102 of GOI Act 1935.",
        "நவீன இந்திய அரசியலமைப்பின் சரத்து 250, 1935 அரசுச் சட்டத்தின் பிரிவு 102-ன் சொற்களை அப்படியே பிரதிபலிக்கிறது.",
        ["Polity", "Historical Background", "GOI Act 1935", "Section 102", "Article 250 Precursor", "Multi-Act Integration", "Grand Test"], "Analyze", 75
    ))

    # Q81: Direct MCQ - Medium - Charter Act 1833 First Law Member
    questions.append(make_q(
        81, "Medium", "Direct MCQ",
        "Who was appointed as the FIRST Law Member of the Governor-General's Executive Council under the Charter Act of 1833?",
        "1833 ஆம் ஆண்டின் சாசனச் சட்டத்தின் கீழ் கவர்னர்-ஜெனரலின் நிர்வாகக் குழுவின் முதல் சட்ட உறுப்பினராக நியமிக்கப்பட்டவர் யார்?",
        [
            ("A", "Lord Macaulay (Thomas Babington Macaulay)", "லார்டு மெக்காலே (தாமஸ் பாபிங்டன் மெக்காலே)"),
            ("B", "Sir Elijah Impey", "சர் எலிஜா இம்பே"),
            ("C", "Sir Charles Wood", "சர் சார்லஸ் வுட்"),
            ("D", "Sir Dinkar Rao", "சர் தினகர் ராவ்")
        ],
        "A",
        "Historical Context: Addition of a specialized legal adviser to the Governor-General's Council in 1833.\nReason: Charter Act 1833 added a 4th member to the Governor-General's Council purely for legislative drafting purposes (Law Member). Lord Macaulay was appointed as the 1st Law Member.\nConstitutional Impact: Separated legislative drafting from general executive administration.\nExam Trap: Macaulay was 4th Law Member (1833 - non-voting on executive matters initially); S.P. Sinha was 1st Indian Law Member (1909).\nMemory Trick: 1833 4th Member = Lord Macaulay (Law Member).",
        "வரலாற்றுப் பின்னணி: 1833-ல் கவர்னர்-ஜெனரல் கவுன்சிலில் ஒரு சிறப்புச் சட்ட ஆலோசகரைச் சேர்த்தல்.\nகாரணம்: 1833 சாசனச் சட்டம் சட்ட வரைவு நோக்கங்களுக்காக மட்டும் கவர்னர்-ஜெனரல் கவுன்சிலில் 4வது உறுப்பினரைச் சேர்த்தது (சட்ட உறுப்பினர்). லார்டு மெக்காலே 1வது சட்ட உறுப்பினராக நியமிக்கப்பட்டார்.\nஅரசியலமைப்பு தாக்கம்: பொது நிர்வாகத்திலிருந்து சட்ட வரைவுப் பணியைப் பிரித்தது.\nதேர்வுப் பொறி: மெக்காலே 4வது சட்ட உறுப்பினர் (1833); எஸ்.பி. சின்கா 1வது இந்திய சட்ட உறுப்பினர் (1909).\nநினைவுச் சூத்திரம்: 1833 4வது உறுப்பினர் = லார்டு மெக்காலே (சட்ட உறுப்பினர்).",
        {
            "A": {"en": "Correct. Lord Macaulay was appointed as 1st Law Member under Charter Act 1833.", "ta": "சரி. லார்டு மெக்காலே 1833 சாசனச் சட்டத்தின்கீழ் 1வது சட்ட உறுப்பினராக நியமிக்கப்பட்டார்."},
            "B": {"en": "Incorrect. Sir Elijah Impey was 1st Chief Justice of Calcutta Supreme Court (1774).", "ta": "தவறு. சர் எலிஜா இம்பே 1774 கொல்கத்தா உச்ச நீதிமன்ற தலைமை நீதிபதியாவார்."},
            "C": {"en": "Incorrect. Sir Charles Wood issued Education Despatch of 1854.", "ta": "தவறு. சர் சார்லஸ் வுட் 1854 கல்வி அறிக்கையை வெளியிட்டார்."},
            "D": {"en": "Incorrect. Sir Dinkar Rao was nominated to Central Legislative Council in 1862.", "ta": "தவறு. சர் தினகர் ராவ் 1862-ல் மேலவைக்கு நியமிக்கப்பட்டார்."}
        },
        "TNPSC Trap: 4th Law Member under 1833 Act had no vote in executive matters; Charter Act 1853 made the Law Member a full executive council member.",
        "TNPSC பொறி: 1833 சட்டத்தில் 4வது சட்ட உறுப்பினருக்கு நிர்வாக விவகாரங்களில் வாக்களிக்கும் அதிகாரம் இல்லை; 1853 சாசனச் சட்டம் அவரை முழு உறுப்பினராக்கியது.",
        "Lord Macaulay also chaired the First Law Commission appointed in 1834.",
        "லார்டு மெக்காலே 1834-ல் நியமிக்கப்பட்ட முதல் சட்ட ஆணையத்திற்கும் தலைமை தாங்கினார்.",
        ["Polity", "Historical Background", "Charter Act 1833", "Lord Macaulay", "Law Member", "Grand Test"], "Remember", 45
    ))

    # Q82: Statement Based - Hard - Evolution of Executive Ordinance Power (1861 to 1935)
    questions.append(make_q(
        82, "Hard", "Statement Based",
        "Consider the following statements regarding the evolution of Ordinance-making powers of the executive in British India:\n1. The Indian Councils Act of 1861 empowered the Governor-General to issue Ordinances during emergencies without council concurrence for a life of six months.\n2. The Government of India Act 1935 empowered both the Governor-General at the Center and Governors in Provinces to issue Ordinances.\n3. Under the 1935 Act, Ordinances could be issued under two distinct circumstances: during recess of legislature (on ministerial advice) and during emergency (in executive discretion).\nWhich of the statements given above are correct?",
        "பிரிட்டிஷ் இந்தியாவில் நிர்வாகத்தின் அவசரச் சட்டம் (Ordinance) பிறப்பிக்கும் அதிகாரங்களின் வளர்ச்சி பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 1861 இந்தியக் கவுன்சில்கள் சட்டம் அவசர காலத்தில் மேலவையின் ஒப்புதலின்றி 6 மாத ஆயுள் கொண்ட அவசரச் சட்டங்களை பிறப்பிக்க கவர்னர்-ஜெனரலுக்கு அதிகாரமளித்தது.\n2. 1935 இந்திய அரசுச் சட்டம் மத்திய கவர்னர்-ஜெனரல் மற்றும் மாகாண கவர்னர்கள் இருசாரருக்கும் அவசரச் சட்டம் பிறப்பிக்கும் அதிகாரத்தை வழங்கியது.\n3. 1935 சட்டத்தின் கீழ் இரு சூழ்நிலைகளில் அவசரச் சட்டங்கள் பிறப்பிக்கப்படலாம்: சட்டமன்ற கூட்டத்தொடர் இல்லாதபோது (அமைச்சர்கள் ஆலோசனையுடன்) மற்றும் அவசர காலத்தில் (நிர்வாக தன்னிச்சையான அதிகாரத்தில்).\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?",
        [
            ("A", "1, 2 and 3", "1, 2 மற்றும் 3"),
            ("B", "1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
            ("C", "2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
            ("D", "1 and 3 only", "1 மற்றும் 3 மட்டுமே")
        ],
        "A",
        "Historical Context: Ordinance-making power evolved as an executive instrument and was integrated into modern Constitution (Arts 123 & 213).\nReason: All three statements are correct. 1861 introduced 6-month validity (Statement 1), 1935 gave Ordinance powers to both GG and Governors (Statement 2), and created two distinct categories (recess ordinances vs emergency discretionary ordinances) (Statement 3).\nConstitutional Impact: Direct statutory ancestry of Article 123 (President's Ordinance) and Article 213 (Governor's Ordinance).\nExam Trap: Ordinance power introduced in 1861 Act; dual-recess/emergency structure introduced in 1935 Act.\nMemory Trick: 1861 (6-Month Intro) $\rightarrow$ 1935 (GG + Governor Ordinance Powers) $\rightarrow$ Art 123 & 213.",
        "வரலாற்றுப் பின்னணி: அவசரச் சட்ட அதிகாரம் ஒரு நிர்வாகக் கருவியாக வளர்ந்து நவீன அரசியலமைப்பில் (சரத்துகள் 123 & 213) இணைக்கப்பட்டது.\nகாரணம்: மூன்று கூற்றுகளும் சரியானவை. 1861 6 மாத செல்லுபடியை அறிமுகப்படுத்தியது (கூற்று 1), 1935 GG மற்றும் கவர்னர்கள் இருவருக்கும் அவசரச் சட்ட அதிகாரம் அளித்தது (கூற்று 2), இருவகை அவசரச் சட்டங்களை உருவாக்கியது (கூட்டத்தொடர் இல்லாதபோது vs தன்னிச்சை அவசரநிலை) (கூற்று 3).\nஅரசியலமைப்பு தாக்கம்: சரத்து 123 (குடியரசுத் தலைவர் அவசரச் சட்டம்) மற்றும் சரத்து 213 (கவர்னர் அவசரச் சட்டம்) ஆகியவற்றிற்கு நேரடி சட்ட மூலம்.\nதேர்வுப் பொறி: அவசரச் சட்ட அதிகாரம் 1861-ல் அறிமுகம்; இருவகை அமைப்பு 1935-ல் உருவாக்கம்.\nநினைவுச் சூத்திரம்: 1861 (6 மாத அறிமுகம்) $\rightarrow$ 1935 (GG + கவர்னர் அவசரச் சட்ட அதிகாரம்) $\rightarrow$ சரத்து 123 & 213.",
        {
            "A": {"en": "Correct. All three statements accurately state Ordinance power evolution from 1861 to 1935.", "ta": "சரி. 1861 முதல் 1935 வரையிலான அவசரச் சட்ட அதிகார வளர்ச்சியின் மூன்று கூற்றுகளும் சரியானவை."},
            "B": {"en": "Incorrect. Statement 3 is also correct.", "ta": "தவறு. கூற்று 3-ம் சரியானது."},
            "C": {"en": "Incorrect. Statement 1 is also correct.", "ta": "தவறு. கூற்று 1-ம் சரியானது."},
            "D": {"en": "Incorrect. Statement 2 is also correct.", "ta": "தவறு. கூற்று 2-ம் சரியானது."}
        },
        "TNPSC Trap: Modern Constitution restricts Ordinance life to 6 weeks from reassembly of Parliament (Art 123), whereas 1861 Act gave fixed 6 months.",
        "TNPSC பொறி: நவீன அரசியலமைப்பு அவசரச் சட்ட ஆயுளை நாடாளுமன்றம் கூடியதிலிருந்து 6 வாரங்களாகக் கட்டுப்படுத்துகிறது (சரத்து 123); ஆனால் 1861 சட்டம் 6 மாதங்களாக நிர்ணயித்தது.",
        "Governor's Ordinance Power under Article 213 is directly modeled on Section 88 of Government of India Act 1935.",
        "சரத்து 213-ன் கீழ் கவர்னரின் அவசரச் சட்ட அதிகாரம் 1935 இந்திய அரசுச் சட்டத்தின் பிரிவு 88-ன் நேரடி மாதிரியாகும்.",
        ["Polity", "Historical Background", "Ordinance Power Evolution", "Article 123 213 Precursor", "Grand Test"], "Analyze", 75
    ))

    # Q83: Multi-Act Comparative - Hard - Evolution of Bicameralism & Franchise
    questions.append(make_q(
        83, "Hard", "Multi-Act Comparative",
        "Which comparative matrix accurately contrasts the franchise (voting eligibility) rules across the 1892, 1919, and 1935 enactments?",
        "1892, 1919 மற்றும் 1935 சட்டங்களின் வாக்குரிமை (வாக்களிக்கும் தகுதி) விதிகளை துல்லியமாக வேறுபடுத்தும் ஒப்பீட்டு அமைப்பு எது?",
        [
            ("A", "1892 Act: Indirect recommendation by local bodies (no direct vote) -> 1919 Act: Direct vote introduced restricted to ~3% of population based on high property/tax/education -> 1935 Act: Expanded direct franchise to ~14% of population including women and Depressed Classes", "1892 சட்டம்: உள்ளாட்சி அமைப்புகளின் மறைமுகப் பரிந்துரை (நேரடி வாக்கில்லை) -> 1919 சட்டம்: உயர் சொத்து/வரி/கல்வி அடிப்படையில் ~3% பேருக்கு நேரடி வாக்கு -> 1935 சட்டம்: பெண்கள், ஒடுக்கப்பட்டோர் உட்பட ~14% பேருக்கு நேரடி வாக்கு விரிவாக்கம்"),
            ("B", "1892 Act: Universal adult franchise -> 1919 Act: Restricted franchise -> 1935 Act: Abolished all voting", "1892 சட்டம்: உலகளாவிய வாக்குரிமை -> 1919 சட்டம்: வரம்பிற்குட்பட்ட வாக்குரிமை -> 1935 சட்டம்: வாக்களிப்பு ஒழிப்பு"),
            ("C", "1892 Act: Military vote only -> 1919 Act: Property vote only -> 1935 Act: Universal adult suffrage", "1892 சட்டம்: இராணுவ வாக்கு மட்டுமே -> 1919 சட்டம்: சொத்து வாக்கு மட்டுமே -> 1935 சட்டம்: உலகளாவிய வாக்குரிமை"),
            ("D", "Voting eligibility remained identical across all three Acts without any change", "மூன்று சட்டங்களிலும் வாக்களிக்கும் தகுதி எந்த மாற்றமுமின்றி ஒரே மாதிரியாக இருந்தது")
        ],
        "A",
        "Historical Context: Incremental expansion of voting rights in British India leading to 1935 Act.\nReason: 1892 Act provided indirect recommendation system (no direct voters). 1919 Act introduced direct elections with very high property, tax, and educational qualifications (enfranchising ~3% of population or 10% of adult males). 1935 Act expanded property/tax/education criteria, enfranchising ~14% of British Indian population including women.\nConstitutional Impact: Paved the way for Universal Adult Suffrage under Article 326 of 1950 Constitution.\nExam Trap: Universal adult suffrage was NEVER granted by British Acts; it was established by 1950 Indian Constitution (Article 326).\nMemory Trick: 1892 (Indirect 0%) $\rightarrow$ 1919 (Direct ~3%) $\rightarrow$ 1935 (Direct ~14%) $\rightarrow$ 1950 (Universal 100%).",
        "வரலாற்றுப் பின்னணி: 1935 சட்டம் வரை பிரிட்டிஷ் இந்தியாவில் வாக்களிக்கும் உரிமைகளின் படிமுறை விரிவாக்கம்.\nகாரணம்: 1892 சட்டம் மறைமுகப் பரிந்துரை முறையைத் தந்தது (நேரடி வாக்காளர்கள் இல்லை). 1919 சட்டம் உயர் சொத்து, வரி, கல்வித் தகுதிகளுடன் நேரடித் தேர்தலை அறிமுகப்படுத்தியது (~3% மக்கள் தொகை). 1935 சட்டம் சொத்து/வரி/கல்வி வரம்புகளைத் தளர்த்தி பெண்கள் உட்பட ~14% பேருக்கு வாக்குரிமையை விரிவுபடுத்தியது.\nஅரசியலமைப்பு தாக்கம்: 1950 அரசியலமைப்பின் சரத்து 326-ன் கீழ் உலகளாவிய வயதுவந்தோர் வாக்குரிமைக்கு வழிவகுத்தது.\nதேர்வுப் பொறி: உலகளாவிய வயதுவந்தோர் வாக்குரிமை பிரிட்டிஷ் சட்டங்களால் வழங்கப்படவில்லை; அது 1950 இந்திய அரசியலமைப்பால் (சரத்து 326) நிறுவப்பட்டது.\nநினைவுச் சூத்திரம்: 1892 (மறைமுகம் 0%) $\rightarrow$ 1919 (நேரடி ~3%) $\rightarrow$ 1935 (நேரடி ~14%) $\rightarrow$ 1950 (உலகளாவிய 100%).",
        {
            "A": {"en": "Correct sequence of franchise expansion across 1892, 1919, and 1935.", "ta": "சரி. 1892, 1919, 1935 சட்டங்களில் வாக்குரிமை விரிவாக்கத்தின் சரியான வரிசை."},
            "B": {"en": "Incorrect. 1892 did not have universal adult franchise.", "ta": "தவறு. 1892-ல் உலகளாவிய வாக்குரிமை இல்லை."},
            "C": {"en": "Incorrect. 1935 did not grant universal adult suffrage.", "ta": "தவறு. 1935-ல் உலகளாவிய வாக்குரிமை வழங்கப்படவில்லை."},
            "D": {"en": "Incorrect. Voting eligibility expanded significantly across Acts.", "ta": "தவறு. வாக்குரிமைத் தகுதி விரிவடைந்தது."}
        },
        "TNPSC Trap: Article 326 of Indian Constitution established Universal Adult Suffrage (lowered from 21 to 18 years by 61st Amendment 1988).",
        "TNPSC பொறி: இந்திய அரசியலமைப்பின் சரத்து 326 உலகளாவிய வயதுவந்தோர் வாக்குரிமையை நிறுவியது (61வது திருத்தம் 1988 மூலம் வயது 21-லிருந்து 18 ஆகக் குறைக்கப்பட்டது).",
        "1935 Act added literacy test as a qualification for voting, increasing female voters.",
        "1935 சட்டம் வாக்களிப்பதற்கான தகுதியாக எழுத்தறிவுத் தேர்வைச் சேர்த்து பெண் வாக்காளர்களை உயர்த்தியது.",
        ["Polity", "Historical Background", "Franchise Evolution", "GOI Act 1935", "Multi-Act Integration", "Grand Test"], "Analyze", 75
    ))

    # Q84: Direct MCQ - Medium - Indian Independence Act 1947 Royal Veto Abolition
    questions.append(make_q(
        84, "Medium", "Direct MCQ",
        "Under the Indian Independence Act of 1947, what major change occurred regarding the British King's right to veto bills passed by the Dominion Legislatures?",
        "1947 இந்திய சுதந்திரச் சட்டத்தின் கீழ், டொமினியன் சட்டமன்றங்களால் நிறைவேற்றப்படும் மசோதாக்களை நிராகரிக்கும் பிரிட்டிஷ் மன்னரின் தடுப்பதிகாரம் (Veto Right) தொடர்பாக என்ன முக்கிய மாற்றம் ஏற்பட்டது?",
        [
            ("A", "The British King's right to veto bills or reserve bills for his approval was completely abolished.", "மசோதாக்களை நிராகரிக்கும் அல்லது தனது ஒப்புதலுக்காக நிறுத்தி வைக்கும் பிரிட்டிஷ் மன்னரின் உரிமை முற்றிலும் ஒழிக்கப்பட்டது."),
            ("B", "The British King was given absolute veto power over all Indian constitutional amendments.", "அனைத்து இந்திய அரசியலமைப்புத் திருத்தங்கள் மீதும் பிரிட்டிஷ் மன்னருக்கு முழுமையான தடுப்பதிகாரம் வழங்கப்பட்டது."),
            ("C", "The British King could veto bills only upon the recommendation of the Governor-General.", "கவர்னர்-ஜெனரலின் பரிந்துரையின் பேரில் மட்டுமே பிரிட்டிஷ் மன்னர் மசோதாக்களை நிராகரிக்க முடியும்."),
            ("D", "The right to veto was transferred to the British House of Lords.", "தடுப்பதிகார உரிமை பிரிட்டிஷ் பிரபுக்கள் சபைக்கு மாற்றப்பட்டது.")
        ],
        "A",
        "Historical Context: Complete divestment of British Royal veto control over Indian Dominion legislation.\nReason: Indian Independence Act 1947 deprived the British Monarch of the right to veto bills or ask for reservation of bills for his approval. This power was reserved for the Governor-General of the Dominion, who acted on the advice of the Dominion Cabinet.\nConstitutional Impact: Established full legislative independence for India's parliament.\nExam Trap: Royal Veto abolished; Governor-General granted assent power on advice of Dominion Cabinet.\nMemory Trick: 1947 Act = Royal Veto Abolished completely.",
        "வரலாற்றுப் பின்னணி: இந்திய டொமினியன் சட்டங்களின் மீது பிரிட்டிஷ் அரசரின் தடுப்பதிகாரக் கட்டுப்பாடு முற்றிலும் பறிக்கப்பட்டது.\nகாரணம்: 1947 இந்திய சுதந்திரச் சட்டம் மசோதாக்களை நிராகரிக்கும் அல்லது நிறுத்தி வைக்கும் பிரிட்டிஷ் மன்னரின் உரிமையை முற்றிலும் ஒழித்தது. அதிகாரம் டொமினியன் அமைச்சரவையின் ஆலோசனையின்படி செயல்படும் கவர்னர்-ஜெனரலுக்கு வழங்கப்பட்டது.\nஅரசியலமைப்பு தாக்கம்: இந்தியாவின் நாடாளுமன்றத்திற்கு முழு சட்ட சுதந்திரத்தை நிறுவியது.\nதேர்வுப் பொறி: அரசரின் தடுப்பதிகாரம் ஒழிப்பு; கவர்னர்-ஜெனரலுக்கு அமைச்சரவை ஆலோசனையுடன் ஒப்புதல் அதிகாரம்.\nநினைவுச் சூத்திரம்: 1947 சட்டம் = பிரிட்டிஷ் மன்னரின் தடுப்பதிகாரம் முற்றிலும் ஒழிப்பு.",
        {
            "A": {"en": "Correct. 1947 Act abolished the British King's right to veto or reserve bills.", "ta": "சரி. 1947 சட்டம் மசோதாக்களை நிராகரிக்கும் பிரிட்டிஷ் மன்னரின் உரிமையை ஒழித்தது."},
            "B": {"en": "Incorrect. Royal veto was abolished, not granted absolute power.", "ta": "தவறு. தடுப்பதிகாரம் ஒழிக்கப்பட்டது."},
            "C": {"en": "Incorrect. King held no veto power at all.", "ta": "தவறு. மன்னருக்கு தடுப்பதிகாரமே இல்லை."},
            "D": {"en": "Incorrect. House of Lords had no veto power over Indian bills.", "ta": "தவறு. பிரபுக்கள் சபைக்கு தடுப்பதிகாரம் இல்லை."}
        },
        "TNPSC Trap: Under 1947 Act, Governor-General had full power to assent to any bill in the name of His Majesty on advice of Dominion ministers.",
        "TNPSC பொறி: 1947 சட்டத்தில் டொமினியன் அமைச்சர்களின் ஆலோசனையின்படி பிரிட்டிஷ் மன்னரின் பெயரால் எந்த மசோதாவிற்கும் ஒப்புதல் அளிக்கும் முழு அதிகாரம் கவர்னர்-ஜெனரலிடம் இருந்தது.",
        "Government of India Act 1935 as adapted served as the interim constitution of India until January 26, 1950.",
        "திருத்தப்பட்ட 1935 இந்திய அரசுச் சட்டம் 1950 ஜனவரி 26 வரை இந்தியாவின் இடைக்கால அரசியலமைப்பாகச் செயல்பட்டது.",
        ["Polity", "Historical Background", "Indian Independence Act 1947", "Royal Veto Abolition", "Grand Test"], "Understand", 60
    ))

    # Q85: Conceptual MCQ - Hard - Comparison of Governor-General Titles Across Eras
    questions.append(make_q(
        85, "Hard", "Conceptual MCQ",
        "Which chronological sequence accurately tracks the official designation of the head of executive administration in India from 1773 to 1858?",
        "1773 முதல் 1858 வரையிலான காலத்தில் இந்தியாவில் நிர்வாகத் தலைவரின் அதிகாரப்பூர்வப் பெயர் மாற்றங்களை துல்லியமாக வரிசைப்படுத்தும் கூற்று எது?",
        [
            ("A", "Governor of Bengal (pre-1773) -> Governor-General of Bengal (Regulating Act 1773) -> Governor-General of India (Charter Act 1833) -> Viceroy and Governor-General of India (GOI Act 1858)", "வங்காள ஆளுநர் (1773 முன்) -> வங்காள கவர்னர்-ஜெனரல் (1773 ஒழுங்குமுறை சட்டம்) -> இந்திய கவர்னர்-ஜெனரல் (1833 சாசனச் சட்டம்) -> வைஸ்ராய் மற்றும் இந்திய கவர்னர்-ஜெனரல் (1858 அரசுச் சட்டம்)"),
            ("B", "Viceroy of India (1773) -> Governor-General of Bengal (1833) -> Governor-General of India (1858)", "இந்திய வைஸ்ராய் (1773) -> வங்காள கவர்னர்-ஜெனரல் (1833) -> இந்திய கவர்னர்-ஜெனரல் (1858)"),
            ("C", "Governor-General of India (1773) -> Governor of Bengal (1833) -> Secretary of State (1858)", "இந்திய கவர்னர்-ஜெனரல் (1773) -> வங்காள ஆளுநர் (1833) -> அரசுச் செயலர் (1858)"),
            ("D", "Governor of Madras (1773) -> Governor of Bombay (1833) -> Governor-General of India (1858)", "மதராஸ் ஆளுநர் (1773) -> பம்பாய் ஆளுநர் (1833) -> இந்திய கவர்னர்-ஜெனரல் (1858)")
        ],
        "A",
        "Historical Context: Evolution of statutory titles for top executive head of British administration in India.\nReason: Pre-1773: Governor of Fort William in Bengal $\rightarrow$ 1773 Act: Governor-General of Bengal (Warren Hastings) $\rightarrow$ 1833 Act: Governor-General of India (Lord William Bentinck) $\rightarrow$ 1858 Act: Viceroy and Governor-General of India (Lord Canning).\nConstitutional Impact: Reflected progressive territorial centralization and sovereign Crown control.\nExam Trap: Viceroy title added in 1858 (for Crown representation), but statutory legal title remained Governor-General in Acts.\nMemory Trick: Governor (Bengal) $\rightarrow$ GG of Bengal (1773) $\rightarrow$ GG of India (1833) $\rightarrow$ Viceroy (1858).",
        "வரலாற்றுப் பின்னணி: பிரிட்டிஷ் இந்தியாவில் முதன்மை நிர்வாகத் தலைவரின் சட்டப்பூர்வ பெயர்களின் வளர்ச்சி.\nகாரணம்: 1773-க்கு முன்: வங்காள ஆளுநர் $\rightarrow$ 1773 சட்டம்: வங்காள கவர்னர்-ஜெனரல் (வாரன் ஹேஸ்டிங்ஸ்) $\rightarrow$ 1833 சட்டம்: இந்திய கவர்னர்-ஜெனரல் (வில்லியம் பென்டிங்க்) $\rightarrow$ 1858 சட்டம்: வைஸ்ராய் மற்றும் இந்திய கவர்னர்-ஜெனரல் (லார்டு கேனிங்).\nஅரசியலமைப்பு தாக்கம்: நிலப்பரப்பு மையமாக்கலையும் பிரிட்டிஷ் முடி ஆட்சியின் இறையாண்மையையும் பிரதிபலித்தது.\nதேர்வுப் பொறி: வைஸ்ராய் பட்டம் 1858-ல் சேர்க்கப்பட்டது (முடி ஆட்சியின் பிரதிநிதியாக), ஆனால் சட்டப்பூர்வப் பெயர் கவர்னர்-ஜெனரலாகவே இருந்தது.\nநினைவுச் சூத்திரம்: ஆளுநர் (வங்காளம்) $\rightarrow$ வங்காள GG (1773) $\rightarrow$ இந்திய GG (1833) $\rightarrow$ வைஸ்ராய் (1858).",
        {
            "A": {"en": "Correct sequence of statutory executive title transformations from 1773 to 1858.", "ta": "சரி. 1773 முதல் 1858 வரை நிர்வாகத் தலைவர் பெயர்களின் சரியான சட்டப்பூர்வ மாற்றம்."},
            "B": {"en": "Incorrect. Viceroy title did not exist in 1773.", "ta": "தவறு. 1773-ல் வைஸ்ராய் பட்டம் இருக்கவில்லை."},
            "C": {"en": "Incorrect. Governor-General of India was created in 1833, not 1773.", "ta": "தவறு. இந்திய GG 1833-லேயே உருவானது."},
            "D": {"en": "Incorrect. Governor of Madras was never top head of all India.", "ta": "தவறு. மதராஸ் ஆளுநர் தலைமைப் பொறுப்பில் இல்லை."}
        },
        "TNPSC Trap: Lord Canning was Viceroy when representing Crown, but Governor-General when administering British Indian government.",
        "TNPSC பொறி: லார்டு கேனிங் பிரிட்டிஷ் முடியைப் பிரதிநிதித்துவப்படுத்தும்போது 'வைஸ்ராய்' என்றும், இந்திய அரசை நிர்வகிக்கும்போது 'கவர்னர்-ஜெனரல்' என்றும் அழைக்கப்பட்டார்.",
        "The title 'Viceroy' means 'representative of the Monarch'.",
        "'வைஸ்ராய்' (Viceroy) என்ற சொல்லின் பொருள் 'அரசரின் பிரதிநிதி' என்பதாகும்.",
        ["Polity", "Historical Background", "Executive Titles Evolution", "Viceroy", "Grand Test"], "Analyze", 75
    ))

    # Q86: Statement Based - Hard - Government of India Act 1935 Concurrent List Features
    questions.append(make_q(
        86, "Hard", "Statement Based",
        "Consider the following statements regarding the Concurrent Legislative List under the Government of India Act of 1935:\n1. It contained 36 items over which both the Federal Legislature and Provincial Legislatures had power to enact laws.\n2. In case of conflict between a Federal law and a Provincial law on a Concurrent subject, the Federal law prevailed.\n3. A Provincial law on a Concurrent subject could prevail over an earlier Federal law if it had been reserved for the consideration of the Governor-General and received his assent.\nWhich of the statements given above are correct?",
        "1935 இந்திய அரசுச் சட்டத்தின் கீழ் பொதுச் சட்டப் பட்டியல் (Concurrent List) பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது கூட்டாட்சி சட்டமன்றம் மற்றும் மாகாண சட்டமன்றங்கள் இரண்டும் சட்டமியற்ற அதிகாரமுள்ள 36 துறைகளைக் கொண்டிருந்தது.\n2. பொதுப் பட்டியலின் ஒரு துறையில் கூட்டாட்சிச் சட்டத்திற்கும் மாகாணச் சட்டத்திற்கும் மோதல் ஏற்படும் போது கூட்டாட்சிச் சட்டமே மேலோங்கியது.\n3. பொதுப் பட்டியலில் உள்ள மாகாணச் சட்டம் கவர்னர்-ஜெனரலின் பரிசீலனைக்கு நிறுத்தப்பட்டு அவரது ஒப்புதலைப் பெற்றிருந்தால், முந்தைய கூட்டாட்சிச் சட்டத்தை விட மேலோங்க முடியும்.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?",
        [
            ("A", "1, 2 and 3", "1, 2 மற்றும் 3"),
            ("B", "1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
            ("C", "2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
            ("D", "1 and 3 only", "1 மற்றும் 3 மட்டுமே")
        ],
        "A",
        "Historical Context: Direct prototype of Article 254 (Repugnancy clause between Union and State laws) in modern Constitution.\nReason: All three statements are correct. Concurrent List had 36 items (Statement 1), Federal law prevailed in conflict (Statement 2), and Provincial law prevailed if reserved for GG assent and assented to (Statement 3).\nConstitutional Impact: Modern Article 254(1) and Article 254(2) of Indian Constitution are exact replicas of these 1935 Act provisions.\nExam Trap: Section 107 of 1935 Act = Article 254 of Indian Constitution.\nMemory Trick: 1935 Section 107 = Repugnancy Clause $\rightarrow$ Article 254 Prototype.",
        "வரலாற்றுப் பின்னணி: நவீன அரசியலமைப்பின் சரத்து 254-க்கு (ஒன்றிய மற்றும் மாநிலச் சட்டங்கள் இடையிலான மோதல் விதி) நேரடி முன்மாதிரி.\nகாரணம்: மூன்று கூற்றுகளும் சரியானவை. பொதுப் பட்டியலில் 36 துறைகள் இருந்தன (கூற்று 1), மோதலில் கூட்டாட்சிச் சட்டம் மேலோங்கியது (கூற்று 2), GG ஒப்புதல் பெற்ற மாகாணச் சட்டம் மேலோங்க முடியும் (கூற்று 3).\nஅரசியலமைப்பு தாக்கம்: நவீன இந்திய அரசியலமைப்பின் சரத்து 254(1) மற்றும் 254(2) ஆகியவை இப் பிரிவுகளின் அப்படியே வடிவங்களாகும்.\nதேர்வுப் பொறி: 1935 சட்டத்தின் பிரிவு 107 = இந்திய அரசியலமைப்பின் சரத்து 254.\nநினைவுச் சூத்திரம்: 1935 பிரிவு 107 = சட்ட மோதல் விதி $\rightarrow$ சரத்து 254 முன்மாதிரி.",
        {
            "A": {"en": "Correct. All three statements accurately describe Concurrent List repugnancy rules under 1935 Act.", "ta": "சரி. 1935 சட்டத்தின் பொதுப் பட்டியல் மோதல் விதிகள் பற்றிய மூன்று கூற்றுகளும் சரியானவை."},
            "B": {"en": "Incorrect. Statement 3 is also correct.", "ta": "தவறு. கூற்று 3-ம் சரியானது."},
            "C": {"en": "Incorrect. Statement 1 is also correct.", "ta": "தவறு. கூற்று 1-ம் சரியானது."},
            "D": {"en": "Incorrect. Statement 2 is also correct.", "ta": "தவறு. கூற்று 2-ம் சரியானது."}
        },
        "TNPSC Trap: Article 254(2) of Indian Constitution allows a State law on Concurrent list to override a Central law if it receives President's assent, modeled on 1935 Act Section 107(2).",
        "TNPSC பொறி: இந்திய அரசியலமைப்பின் சரத்து 254(2) குடியரசுத் தலைவரின் ஒப்புதல் பெற்ற மாநில பொதுப் பட்டியல் சட்டத்தை மத்திய சட்டத்தை விட மேலோங்க அனுமதிக்கிறது (1935 பிரிவு 107(2) மாதிரி).",
        "1935 Act item counts: Federal List (59), Provincial List (54), Concurrent List (36).",
        "1935 சட்டப் பட்டியல் அளவுகள்: கூட்டாட்சி (59), மாகாணம் (54), பொது (36).",
        ["Polity", "Historical Background", "GOI Act 1935", "Concurrent List", "Article 254 Precursor", "Grand Test"], "Analyze", 75
    ))

    # Q87: Direct MCQ - Easy - Pitts India Act 1784 Board of Control Members
    questions.append(make_q(
        87, "Easy", "Direct MCQ",
        "How many members constituted the Board of Control established under Pitt's India Act of 1784?",
        "1784 ஆம் ஆண்டின் பிட் இந்தியச் சட்டத்தின் கீழ் நிறுவப்பட்ட கட்டுப்பாட்டு வாரியம் (Board of Control) எத்தனை உறுப்பினர்களைக் கொண்டிருந்தது?",
        [
            ("A", "6 Members (including Chancellor of the Exchequer and Secretary of State)", "6 உறுப்பினர்கள் (நிதி அமைச்சர் மற்றும் அரசுச் செயலர் உட்பட)"),
            ("B", "15 Members", "15 உறுப்பினர்கள்"),
            ("C", "4 Members", "4 உறுப்பினர்கள்"),
            ("D", "24 Members", "24 உறுப்பினர்கள்")
        ],
        "A",
        "Historical Context: Institutional setup of Dual System of Control under Pitt's India Act 1784.\nReason: Pitt's India Act 1784 created a 6-member Board of Commissioners for the Affairs of India (commonly called Board of Control), including the Chancellor of the Exchequer, a Secretary of State, and 4 Privy Councillors.\nConstitutional Impact: Established British Cabinet oversight over Indian political administration.\nExam Trap: Board of Control = 6 members (1784); Council of India = 15 members (1858); Court of Directors = 24 members (1773).\nMemory Trick: Board of Control 1784 = 6 Members; Council of India 1858 = 15 Members.",
        "வரலாற்றுப் பின்னணி: 1784 பிட் இந்தியச் சட்டத்தின் கீழ் இரட்டை கட்டுப்பாட்டு முறையின் நிறுவன கட்டமைப்பு.\nகாரணம்: 1784 பிட் இந்தியச் சட்டம் நிதி அமைச்சர், ஒரு அரசுச் செயலர் மற்றும் 4 பிரிவி கவுன்சிலர்கள் உட்பட 6 உறுப்பினர்களைக் கொண்ட கட்டுப்பாட்டு வாரியத்தை உருவாக்கியது.\nஅரசியலமைப்பு தாக்கம்: இந்திய அரசியல் நிர்வாகத்தின் மீது பிரிட்டிஷ் கேபினட் மேற்பார்வையை நிறுவியது.\nதேர்வுப் பொறி: கட்டுப்பாட்டு வாரியம் = 6 உறுப்பினர்கள் (1784); இந்தியக் குழு = 15 உறுப்பினர்கள் (1858); இயக்குநர்கள் அவை = 24 உறுப்பினர்கள் (1773).\nநினைவுச் சூத்திரம்: கட்டுப்பாட்டு வாரியம் 1784 = 6 உறுப்பினர்கள்; இந்தியக் குழு 1858 = 15 உறுப்பினர்கள்.",
        {
            "A": {"en": "Correct. Board of Control established in 1784 consisted of 6 members.", "ta": "சரி. 1784-ல் அமைக்கப்பட்ட கட்டுப்பாட்டு வாரியம் 6 உறுப்பினர்களைக் கொண்டிருந்தது."},
            "B": {"en": "Incorrect. 15 members constituted the Council of India in 1858.", "ta": "தவறு. 15 உறுப்பினர்கள் 1858 இந்தியக் குழுவில் இருந்தனர்."},
            "C": {"en": "Incorrect. 4 members constituted Governor-General's Council in 1773.", "ta": "தவறு. 4 உறுப்பினர்கள் 1773 கவர்னர்-ஜெனரல் குழுவில் இருந்தனர்."},
            "D": {"en": "Incorrect. 24 members constituted the Court of Directors.", "ta": "தவறு. 24 உறுப்பினர்கள் இயக்குநர்கள் அவையில் இருந்தனர்."}
        },
        "TNPSC Trap: President of Board of Control was a British Cabinet minister; Lord Grenville was its first President in 1784.",
        "TNPSC பொறி: கட்டுப்பாட்டு வாரியத் தலைவர் பிரிட்டிஷ் கேபினட் அமைச்சராவார்; 1784-ல் லார்டு கிரென்வில் இதன் முதல் தலைவராவார்.",
        "Board of Control managed civil, military, and revenue affairs, while Court of Directors retained commercial affairs.",
        "கட்டுப்பாட்டு வாரியம் சிவில், இராணுவம், வருவாயை நிர்வகித்தது; இயக்குநர்கள் அவை வணிகத்தை நிர்வகித்தது.",
        ["Polity", "Historical Background", "Pitts India Act 1784", "Board of Control", "Grand Test"], "Remember", 45
    ))

    # Q88: Multi-Act Comparative - Hard - Evolution of Executive Supremacy vs Legislative Control
    questions.append(make_q(
        88, "Hard", "Multi-Act Comparative",
        "Which inference accurately summarizes how the Governor-General's executive veto powers transformed between 1773 and 1935?",
        "1773 முதல் 1935 வரை கவர்னர்-ஜெனரலின் நிர்வாகத் தடுப்பதிகாரங்கள் (Veto Powers) உருமாறியதை துல்லியமாக விவரிக்கும் முடிவு எது?",
        [
            ("A", "Bound by council majority (1773) -> Overriding veto granted for safety/peace (1786/1793) -> Ordinance making power added (1861) -> Certification & restoration powers over budget (1919) -> Absolute discretionary 'special responsibilities' & Section 93 emergency takeover (1935)", "கவுன்சில் பெரும்பான்மைக்கு கட்டுப்பட்டவர் (1773) -> அமைதி/பாதுகாப்பிற்கு நிராகரிப்பு அதிகாரம் (1786/1793) -> அவசரச் சட்ட அதிகாரம் (1861) -> பட்ஜெட் சான்றளிப்பு அதிகாரம் (1919) -> சிறப்புப் பொறுப்புகள் & பிரிவு 93 அவசரகால அதிகாரங்கள் (1935)"),
            ("B", "Absolute dictator (1773) -> Powers reduced to zero (1861) -> Complete subordinate to ministers (1935)", "சர்வாதிகாரி (1773) -> அதிகாரம் பூஜ்ஜியமானது (1861) -> அமைச்சர்களுக்கு முழுமையா கீழ்மைப்பட்டவர் (1935)"),
            ("C", "No veto powers existed in any Act from 1773 to 1935", "1773 முதல் 1935 வரை எந்தச் சட்டத்திலும் தடுப்பதிகாரம் இருக்கவில்லை"),
            ("D", "Veto powers were held by Court of Directors, not Governor-General", "தடுப்பதிகாரங்கள் இயக்குநர்கள் அவையிடம் இருந்தன, கவர்னர்-ஜெனரலிடம் இல்லை")
        ],
        "A",
        "Historical Context: The continuous retention and statutory sophistication of autocratic executive veto power across Company and Crown rule.\nReason: 1773 (GG bound by council majority) $\rightarrow$ 1786 (Cornwallis override power) $\rightarrow$ 1861 (Ordinance power) $\rightarrow$ 1919 (Certification of rejected bills/grants) $\rightarrow$ 1935 (Individual judgment, special responsibilities, and Section 93 emergency takeover).\nConstitutional Impact: Maintained British imperial control alongside progressive legislative expansion.\nExam Trap: 1773 GG had NO veto (bound by majority); veto power began in 1786 Act.\nMemory Trick: 1773 (No Veto) $\rightarrow$ 1786 (Override Veto) $\rightarrow$ 1861 (Ordinance) $\rightarrow$ 1919 (Certification) $\rightarrow$ 1935 (Special Responsibilities).",
        "வரலாற்றுப் பின்னணி: கம்பெனி மற்றும் முடி ஆட்சியில் தன்னாதிக்க நிர்வாகத் தடுப்பதிகாரத்தின் தொடர்ச்சியான நீடிப்பும் சட்டப்பூர்வ வளர்ச்சியும்.\nகாரணம்: 1773 (கவுன்சில் பெரும்பான்மைக்கு கட்டுப்பட்டவர்) $\rightarrow$ 1786 (காரன்வாலிஸ் நிராகரிப்பு அதிகாரம்) $\rightarrow$ 1861 (அவசரச் சட்ட அதிகாரம்) $\rightarrow$ 1919 (நிராகரிக்கப்பட்ட மசோதாக்கள் சான்றளிப்பு) $\rightarrow$ 1935 (தன்னிச்சை அதிகாரங்கள், சிறப்புப் பொறுப்புகள், பிரிவு 93 அவசரநிலை).\nஅரசியலமைப்பு தாக்கம்: சட்டமன்ற விரிவாக்கத்துடன் பிரிட்டிஷ் ஏகாதிபத்திய கட்டுப்பாட்டை நீடித்தது.\nதேர்வுப் பொறி: 1773 GG-க்கு தடுப்பதிகாரம் இல்லை (பெரும்பான்மை கட்டுப்பாடு); 1786-லேயே தடுப்பதிகாரம் தொடங்கியது.\nநினைவுச் சூத்திரம்: 1773 (தடுப்பதிகாரமில்லை) $\rightarrow$ 1786 (நிராகரிப்பு அதிகாரம்) $\rightarrow$ 1861 (அவசரச் சட்டம்) $\rightarrow$ 1919 (சான்றளிப்பு) $\rightarrow$ 1935 (சிறப்புப் பொறுப்புகள்).",
        {
            "A": {"en": "Correct sequence mapping executive veto and discretionary power expansion from 1773 to 1935.", "ta": "சரி. 1773 முதல் 1935 வரை நிர்வாகத் தடுப்பதிகாரம் மற்றும் தன்னிச்சை அதிகார விரிவாக்கத்தின் சரியான வரிசை."},
            "B": {"en": "Incorrect. Reverses the actual statutory evolution.", "ta": "தவறு. சட்டப்பூர்வ வளர்ச்சியை தலைகீழாக மாற்றுகிறது."},
            "C": {"en": "Incorrect. Veto powers existed in all major Acts after 1786.", "ta": "தவறு. 1786-க்கு பின் தடுப்பதிகாரங்கள் இருந்தன."},
            "D": {"en": "Incorrect. Governor-General held extensive statutory veto powers.", "ta": "தவறு. கவர்னர்-ஜெனரலிடம் பரந்த தடுப்பதிகாரங்கள் இருந்தன."}
        },
        "TNPSC Trap: In 1773 Act, Warren Hastings was outvoted by his council members (Philip Francis, Clavering, Monson) because GG had no veto power.",
        "TNPSC பொறி: 1773 சட்டத்தில் ஹேஸ்டிங்ஸுக்கு தடுப்பதிகாரம் இல்லாததால் தனது கவுன்சில் உறுப்பினர்களால் (ஃபிலிப் பிரான்சிஸ் போன்றோர்) தோற்கடிக்கப்பட்டார்.",
        "Act of 1786 was specifically enacted to give Lord Cornwallis the power to override his council.",
        "1786 சட்டம் லார்டு காரன்வாலிஸுக்கு கவுன்சிலை நிராகரிக்கும் அதிகாரத்தை அளிக்கவே இயற்றப்பட்டது.",
        ["Polity", "Historical Background", "Executive Veto Evolution", "Multi-Act Integration", "Grand Test"], "Analyze", 75
    ))

    # Q89: Statement Based - Hard - Government of India Act 1935 Instruments of Instructions
    questions.append(make_q(
        89, "Hard", "Statement Based",
        "Consider the following statements regarding the 'Instrument of Instructions' issued to the Governor-General and Governors under the Government of India Act 1935:\n1. It contained statutory directions from the British Crown on how the Governor-General and Governors should exercise their discretionary powers.\n2. The draft of the Instrument of Instructions was incorporated into the Constitution of India 1950 as the Directive Principles of State Policy (DPSP).\n3. Dr. B.R. Ambedkar explicitly stated in the Constituent Assembly that the Directive Principles are like the Instrument of Instructions issued to the Governors of India by the British Government.\nWhich of the statements given above are correct?",
        "1935 இந்திய அரசுச் சட்டத்தின் கீழ் கவர்னர்-ஜெனரல் மற்றும் கவர்னர்களுக்கு வழங்கப்பட்ட 'அறிவுறுத்தல்கள் ஆவணம்' (Instrument of Instructions) பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. கவர்னர்-ஜெனரல் மற்றும் கவர்னர்கள் தங்களது தன்னிச்சையான அதிகாரங்களை எவ்வாறு பயன்படுத்த வேண்டும் என்பது குறித்த பிரிட்டிஷ் முடியின் சட்டப்பூர்வ வழிகாட்டுதல்களை இது கொண்டிருந்தது.\n2. அறிவுறுத்தல்கள் ஆவணத்தின் வரைவு 1950 இந்திய அரசியலமைப்பில் அரசு நெறிமுறைப்படுத்தும் கோட்பாடுகளாக (DPSP) இணைக்கப்பட்டது.\n3. அரசு நெறிமுறைப்படுத்தும் கோட்பாடுகள் பிரிட்டிஷ் அரசால் இந்திய ஆளுநர்களுக்கு வழங்கப்பட்ட அறிவுறுத்தல்கள் ஆவணம் போன்றவை என டாக்டர் பி.ஆர். அம்பேத்கர் அரசியல் நிர்ணய சபையில் வெளிப்படையாகக் கூறினார்.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?",
        [
            ("A", "1, 2 and 3", "1, 2 மற்றும் 3"),
            ("B", "1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
            ("C", "2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
            ("D", "1 and 3 only", "1 மற்றும் 3 மட்டுமே")
        ],
        "A",
        "Historical Context: Direct statutory origin of Part IV of Indian Constitution (Directive Principles of State Policy - DPSP).\nReason: All three statements are correct. Instrument of Instructions guided colonial executive discretion (Statement 1). Constituent Assembly incorporated its concept into Part IV (DPSP) (Statement 2). Dr. B.R. Ambedkar explicitly stated: 'The Directive Principles are like the Instrument of Instructions, which were issued to the Governor-General and to the Governors of the colonies by the British Government' (Statement 3).\nConstitutional Impact: Direct historical precursor to DPSP (Articles 36-51) in Indian Constitution.\nExam Trap: DPSP content inspired by Irish Constitution; DPSP concept/name precursor = Instrument of Instructions 1935 Act.\nMemory Trick: Instrument of Instructions (1935 Act) = DPSP Blueprint (Part IV).",
        "வரலாற்றுப் பின்னணி: இந்திய அரசியலமைப்பின் பகுதி IV-ன் (அரசு நெறிமுறைப்படுத்தும் கோட்பாடுகள் - DPSP) நேரடி சட்டப்பூர்வ மூலம்.\nகாரணம்: மூன்று கூற்றுகளும் சரியானவை. அறிவுறுத்தல்கள் ஆவணம் காலனித்துவ நிர்வாக அதிகாரத்திற்கு வழிகாட்டியது (கூற்று 1). அரசியல் நிர்ணய சபை அதை பகுதி IV (DPSP) ஆக இணைத்தது (கூற்று 2). டாக்டர் அம்பேத்கர் கூறினார்: 'அரசு நெறிமுறைப்படுத்தும் கோட்பாடுகள் பிரிட்டிஷ் அரசால் வழங்கப்பட்ட அறிவுறுத்தல்கள் ஆவணம் போன்றவையாகும்' (கூற்று 3).\nஅரசியலமைப்பு தாக்கம்: இந்திய அரசியலமைப்பின் DPSP (சரத்துகள் 36-51) விதிகளுக்கு நேரடி வரலாற்று முன்னோடி.\nதேர்வுப் பொறி: DPSP கருத்துகள் அயர்லாந்து அரசியலமைப்பின் ஈர்ப்பு; DPSP கருத்து வடிவம் = 1935 சட்டத்தின் அறிவுறுத்தல்கள் ஆவணம்.\nநினைவுச் சூத்திரம்: அறிவுறுத்தல்கள் ஆவணம் (1935 சட்டம்) = DPSP வரைபடம் (பகுதி IV).",
        {
            "A": {"en": "Correct. All three statements accurately state the historical connection between 1935 Instrument of Instructions and DPSP.", "ta": "சரி. 1935 அறிவுறுத்தல்கள் ஆவணத்திற்கும் DPSP-க்கும் இடையிலான வரலாற்றுத் தொடர்பின் மூன்று கூற்றுகளும் சரியானவை."},
            "B": {"en": "Incorrect. Statement 3 is also correct.", "ta": "தவறு. கூற்று 3-ம் சரியானது."},
            "C": {"en": "Incorrect. Statement 1 is also correct.", "ta": "தவறு. கூற்று 1-ம் சரியானது."},
            "D": {"en": "Incorrect. Statement 2 is also correct.", "ta": "தவறு. கூற்று 2-ம் சரியானது."}
        },
        "TNPSC Trap: Only difference is that DPSP is issued to the Legislature and Executive of independent India, whereas Instrument of Instructions was issued to Executive only.",
        "TNPSC பொறி: ஒரே வேறுபாடு DPSP சுதந்திர இந்தியாவின் சட்டமன்றம் மற்றும் நிர்வாகத்திற்கு வழங்கப்படுகிறது; அறிவுறுத்தல்கள் ஆவணம் நிர்வாகத்திற்கு மட்டும் வழங்கப்பட்டது.",
        "Instrument of Instructions under 1935 Act required approval of both Houses of British Parliament.",
        "1935 சட்டத்தின் கீழ் அறிவுறுத்தல்கள் ஆவணம் பிரிட்டிஷ் நாடாளுமன்றத்தின் இரு அவைகளின் அங்கீகாரத்தையும் கோரியது.",
        ["Polity", "Historical Background", "GOI Act 1935", "Instrument of Instructions", "DPSP Precursor", "Grand Test"], "Analyze", 75
    ))

    # Q90: Direct MCQ - Medium - Indian Independence Act Sovereign Boundary Line
    questions.append(make_q(
        90, "Medium", "Direct MCQ",
        "Under the Indian Independence Act of 1947, who served as the FIRST Governor-General of independent Pakistan?",
        "1947 இந்திய சுதந்திரச் சட்டத்தின் கீழ், சுதந்திர பாகிஸ்தானின் முதல் கவர்னர்-ஜெனரலாகப் பணியாற்றியவர் யார்?",
        [
            ("A", "Muhammad Ali Jinnah", "முகமது அலி ஜின்னா"),
            ("B", "Liaquat Ali Khan", "லியாகத் அலி கான்"),
            ("C", "Lord Mountbatten", "லார்டு மவுண்ட்பேட்டன்"),
            ("D", "Khwaja Nazimuddin", "கவாஜா நஜிமுதீன்")
        ],
        "A",
        "Historical Context: Executive head appointments upon partition under Indian Independence Act 1947.\nReason: While India opted to retain Lord Mountbatten as its first Governor-General, Pakistan chose Muhammad Ali Jinnah as its first Governor-General. Liaquat Ali Khan became Pakistan's first Prime Minister.\nConstitutional Impact: Established separate dominion executive heads.\nExam Trap: India's 1st GG (post-1947) = Lord Mountbatten; Pakistan's 1st GG (post-1947) = M.A. Jinnah.\nMemory Trick: India 1947 GG = Mountbatten; Pakistan 1947 GG = Jinnah.",
        "வரலாற்றுப் பின்னணி: 1947 இந்திய சுதந்திரச் சட்டத்தின் கீழ் பிரிவினையின் போது நிர்வாகத் தலைவர்களின் நியமனம்.\nகாரணம்: இந்தியா லார்டு மவுண்ட்பேட்டனைத் தனது முதல் கவர்னர்-ஜெனரலாகத் தக்கவைத்துக் கொள்ளத் தேர்வு செய்தபோது, பாகிஸ்தான் முகமது அலி ஜின்னாவைத் தனது முதல் கவர்னர்-ஜெனரலாகத் தேர்வு செய்தது. லியாகத் அலி கான் பாகிஸ்தானின் முதல் பிரதமரானார்.\nஅரசியலமைப்பு தாக்கம்: இரு தனித்தனி டொமினியன் நிர்வாகத் தலைவர்களை நிறுவியது.\nதேர்வுப் பொறி: இந்தியாவின் 1வது GG (1947 பின்) = லார்டு மவுண்ட்பேட்டன்; பாகிஸ்தானின் 1வது GG (1947 பின்) = எம்.ஏ. ஜின்னா.\nநினைவுச் சூத்திரம்: இந்தியா 1947 GG = மவுண்ட்பேட்டன்; பாகிஸ்தான் 1947 GG = ஜின்னா.",
        {
            "A": {"en": "Correct. Muhammad Ali Jinnah became the first Governor-General of Pakistan in August 1947.", "ta": "சரி. முகமது அலி ஜின்னா ஆகஸ்ட் 1947-ல் பாகிஸ்தானின் முதல் கவர்னர்-ஜெனரலானார்."},
            "B": {"en": "Incorrect. Liaquat Ali Khan was the first Prime Minister of Pakistan.", "ta": "தவறு. லியாகத் அலி கான் பாகிஸ்தானின் முதல் பிரதமராவார்."},
            "C": {"en": "Incorrect. Lord Mountbatten was Governor-General of India.", "ta": "தவறு. லார்டு மவுண்ட்பேட்டன் இந்தியாவின் கவர்னர்-ஜெனரலானார்."},
            "D": {"en": "Incorrect. Khwaja Nazimuddin became 2nd Governor-General after Jinnah's death in 1948.", "ta": "தவறு. கவாஜா நஜிமுதீன் ஜின்னாவின் மறைவிற்குப் பின் 2வது GG ஆனார்."}
        },
        "TNPSC Trap: Lord Mountbatten originally wanted to be joint Governor-General of both India and Pakistan, but Muslim League rejected the proposal.",
        "TNPSC பொறி: லார்டு மவுண்ட்பேட்டன் இரு டொமினியன்களுக்கும் பொதுவான கவர்னர்-ஜெனரலாக இருக்க விரும்பினார், ஆனால் முஸ்லிம் லீக் அதை நிராகரித்தது.",
        "C. Rajagopalachari succeeded Lord Mountbatten as Governor-General of India in June 1948.",
        "சி. ராஜகோபாலாச்சாரி 1948 ஜூன் மாதம் லார்டு மவுண்ட்பேட்டனுக்குப் பின் இந்தியாவின் கவர்னர்-ஜெனரலானார்.",
        ["Polity", "Historical Background", "Indian Independence Act 1947", "Governor General Pakistan", "Grand Test"], "Understand", 60
    ))

    # Q91: Multi-Act Comparative - Hard - Evolution of Financial Budgetary Separation
    questions.append(make_q(
        91, "Hard", "Multi-Act Comparative",
        "Which landmark financial committee recommended the separation of Railway Finance from General Finance, implemented in 1924 under the framework of the Government of India Act 1919?",
        "1919 இந்திய அரசுச் சட்டத்தின் சட்டகத்தின் கீழ் 1924-ல் அமல்படுத்தப்பட்ட இரயில்வே நிதியை பொது நிதியிலிருந்து பிரிக்கும் பரிந்துரையை அளித்த வரலாற்றுச் சிறப்புமிக்க நிதிக் குழு எது?",
        [
            ("A", "Acworth Committee (1920-21)", "அக்வொர்த் குழு (Acworth Committee 1920-21)"),
            ("B", "Hilton Young Commission (1926)", "ஹில்டன் யங் ஆணையம் (Hilton Young Commission 1926)"),
            ("C", "Macaulay Committee (1854)", "மெக்காலே குழு (Macaulay Committee 1854)"),
            ("D", "Hunter Committee (1919)", "ஹண்டர் குழு (Hunter Committee 1919)")
        ],
        "A",
        "Historical Context: Separation of commercial railway budget from main imperial budget under 1919 Act reforms.\nReason: The Acworth Committee (chaired by Sir William Acworth in 1920-21) recommended separating Railway Budget from General Budget to ensure stability in railway development. This separation was implemented in 1924 and continued for 92 years until merged back in 2017.\nConstitutional Impact: Key milestone in Indian financial administration and budgeting.\nExam Trap: Acworth Committee = Railway Budget Separation (1924); Hilton Young = Reserve Bank of India (1926).\nMemory Trick: Acworth = Railway Budget Separation (1924); Hilton Young = RBI (1935).",
        "வரலாற்றுப் பின்னணி: 1919 சட்ட சீர்திருத்தங்களின் கீழ் வணிக இரயில்வே பட்ஜெட்டை பொது பட்ஜெட்டிலிருந்து பிரித்தல்.\nகாரணம்: அக்வொர்த் குழு (சர் வில்லியம் அக்வொர்த் தலைமை 1920-21) இரயில்வே வளர்ச்சியை உறுதிப்படுத்த இரயில்வே பட்ஜெட்டை பொது பட்ஜெட்டிலிருந்து பிரிக்கப் பரிந்துரைத்தது. இப்பிரிப்பு 1924-ல் அமலாகி 2017-ல் மீண்டும் இணைக்கப்படும் வரை 92 ஆண்டுகள் நீடித்தது.\nஅரசியலமைப்பு தாக்கம்: இந்திய நிதி நிர்வாகம் மற்றும் பட்ஜெட் தயாரிப்பில் முக்கிய மைல்கல்.\nதேர்வுப் பொறி: அக்வொர்த் குழு = இரயில்வே பட்ஜெட் பிரிப்பு (1924); ஹில்டன் யங் = ரிசர்வ் வங்கி (1926).\nநினைவுச் சூத்திரம்: அக்வொர்த் = இரயில்வே பட்ஜெட் பிரிப்பு (1924); ஹில்டன் யங் = RBI (1935).",
        {
            "A": {"en": "Correct. Acworth Committee recommended separation of Railway Budget from General Budget in 1921 (implemented 1924).", "ta": "சரி. அக்வொர்த் குழு இரயில்வே பட்ஜெட்டை பொது பட்ஜெட்டிலிருந்து பிரிக்கப் பரிந்துரைத்தது (அமலாக்கம் 1924)."},
            "B": {"en": "Incorrect. Hilton Young Commission recommended creation of Reserve Bank of India.", "ta": "தவறு. ஹில்டன் யங் ஆணையம் ரிசர்வ் வங்கியைப் பரிந்துரைத்தது."},
            "C": {"en": "Incorrect. Macaulay Committee dealt with Civil Services in 1854.", "ta": "தவறு. மெக்காலே குழு 1854 சிவில் சர்வீஸ் பற்றியது."},
            "D": {"en": "Incorrect. Hunter Committee investigated Jallianwala Bagh massacre.", "ta": "தவறு. ஹண்டர் குழு ஜாலியன்வாலா பாக் படுகொலையை விசாரித்தது."}
        },
        "TNPSC Trap: Union Government merged the Railway Budget back into the General Budget starting from the 2017-18 financial year.",
        "TNPSC பொறி: ஒன்றிய அரசு 2017-18 நிதியாண்டு முதல் இரயில்வே பட்ஜெட்டை மீண்டும் பொது பட்ஜெட்டுடன் இணைத்தது.",
        "Hilton Young Commission (Royal Commission on Indian Currency and Finance 1926) led to the establishment of RBI in 1935.",
        "ஹில்டன் யங் ஆணையம் (1926) 1935-ல் RBI அமையக் காரணமானது.",
        ["Polity", "Historical Background", "Acworth Committee 1921", "Railway Budget Separation", "Multi-Act Integration", "Grand Test"], "Analyze", 75
    ))

    # Q92: Statement Based - Hard - Charter Act 1853 Administrative Features
    questions.append(make_q(
        92, "Hard", "Statement Based",
        "Consider the following statements regarding the administrative provisions of the Charter Act of 1853:\n1. It reduced the number of Directors in the Court of Directors from 24 to 18, out of which 6 were to be nominated by the Crown.\n2. It renewed the powers of the East India Company and allowed it to retain possession of Indian territories in trust for the British Crown, without specifying any fixed period.\n3. It created a separate Lieutenant-Governor for the Presidency of Bengal.\nWhich of the statements given above are correct?",
        "1853 சாசனச் சட்டத்தின் நிர்வாக விதிகளைப் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது இயக்குநர்கள் அவையின் இயக்குநர்கள் எண்ணிக்கையை 24-லிருந்து 18 ஆகக் குறைத்தது, அதில் 6 பேர் பிரிட்டிஷ் முடியால் நியமிக்கப்பட வேண்டும்.\n2. இது எந்தவொரு குறிப்பிட்ட கால வரம்பையும் குறிப்பிடாமல் கிழக்கிந்திய கம்பெனியின் அதிகாரங்களைப் புதுப்பித்து பிரிட்டிஷ் முடியின் அறக்கட்டளையாக நிலப்பரப்புகளைத் தக்கவைக்க அனுமதித்தது.\n3. இது வங்காள மாகாணத்திற்கு ஒரு தனி துணை ஆளுநரை (Lieutenant-Governor) உருவாக்கியது.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?",
        [
            ("A", "1, 2 and 3", "1, 2 மற்றும் 3"),
            ("B", "1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
            ("C", "2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
            ("D", "1 and 3 only", "1 மற்றும் 3 மட்டுமே")
        ],
        "A",
        "Historical Context: Charter Act 1853 laid down the final organizational framework of EIC before its total abolition in 1858.\nReason: All three statements are correct. Court of Directors reduced from 24 to 18 (6 Crown nominated) (Statement 1). Charter renewed without fixed period, signaling impending Crown takeover (Statement 2). Created a separate Lt-Governor for Bengal so GG of India was freed from direct Bengal administration (Statement 3).\nConstitutional Impact: Prepared the administrative groundwork for direct Crown governance.\nExam Trap: Previous Charter Acts (1793, 1813, 1833) renewed company rule for fixed 20-year periods; 1853 Act specified NO fixed period.\nMemory Trick: 1853 Act = 18 Directors (6 Crown) + No Fixed Period + Lt-Governor for Bengal.",
        "வரலாற்றுப் பின்னணி: 1858-ல் கம்பெனி ஆட்சி முழுமையாக ஒழிக்கப்படுவதற்கு முன் 1853 சாசனச் சட்டம் அமைப்புக் சட்டகத்தை அமைத்தது.\nகாரணம்: மூன்று கூற்றுகளும் சரியானவை. இயக்குநர்கள் அவை 24-லிருந்து 18 ஆகக் குறைக்கப்பட்டது (6 பேர் அரசு நியமனம்) (கூற்று 1). சாசனம் கால வரம்பின்றி புதுப்பிக்கப்பட்டது, இது முடி ஆட்சியை உணர்த்தியது (கூற்று 2). வங்காளத்திற்குத் தனி துணை ஆளுநர் அமைக்கப்பட்டதால் இந்திய GG வங்காள நேரடி நிர்வாகத்திலிருந்து விடுவிக்கப்பட்டார் (கூற்று 3).\nஅரசியலமைப்பு தாக்கம்: பிரிட்டிஷ் முடியின் நேரடி ஆட்சிக்கு நிர்வாக அடித்தளத்தை தயார் செய்தது.\nதேர்வுப் பொறி: முந்தைய சாசனச் சட்டங்கள் (1793, 1813, 1833) 20 ஆண்டுகால நிலையான காலத்திற்கு நீட்டித்தன; 1853 சட்டம் நிலையான காலம் குறிப்பிடவில்லை.\nநினைவுச் சூத்திரம்: 1853 சட்டம் = 18 இயக்குநர்கள் (6 அரச நியமனம்) + நிலையான காலமில்லை + வங்காளத்திற்கு துணை ஆளுநர்.",
        {
            "A": {"en": "Correct. All three statements accurately state administrative features of Charter Act 1853.", "ta": "சரி. 1853 சாசனச் சட்டத்தின் மூன்று நிர்வாகக் கூற்றுகளும் துல்லியமாக சரியானவை."},
            "B": {"en": "Incorrect. Statement 3 is also correct.", "ta": "தவறு. கூற்று 3-ம் சரியானது."},
            "C": {"en": "Incorrect. Statement 1 is also correct.", "ta": "தவறு. கூற்று 1-ம் சரியானது."},
            "D": {"en": "Incorrect. Statement 2 is also correct.", "ta": "தவறு. கூற்று 2-ம் சரியானது."}
        },
        "TNPSC Trap: Lord Dalhousie was Governor-General of India when the Charter Act of 1853 was enacted.",
        "TNPSC பொறி: 1853 சாசனச் சட்டம் இயற்றப்பட்டபோது லார்டு டல்ஹவுசி இந்தியாவின் கவர்னர்-ஜெனரலாக இருந்தார்.",
        "Charter Act 1853 was passed based on reports of two Parliamentary Select Committees set up in 1852.",
        "1852-ல் அமைக்கப்பட்ட இரண்டு நாடாளுமன்றக் குழுக்களின் அறிக்கைகளின் அடிப்படையில் 1853 சாசனச் சட்டம் நிறைவேற்றப்பட்டது.",
        ["Polity", "Historical Background", "Charter Act 1853", "Court of Directors 1853", "Grand Test"], "Analyze", 75
    ))

    # Q93: Conceptual MCQ - Medium - Amending Act 1781 Provincial Appeals Jurisdiction
    questions.append(make_q(
        93, "Medium", "Conceptual MCQ",
        "Under the Amending Act of 1781 (Act of Settlement), to which authority were appeals from the Provincial Courts (Sadar Adalats) directed to be taken?",
        "1781 ஆம் ஆண்டின் திருத்தச் சட்டத்தின் (சீர்முறைச் சட்டம்) கீழ், மாகாண நீதிமன்றங்களின் (சதர் அதாலத்துகள்) மேல்முறையீடுகள் எந்த அதிகார அமைப்பிற்குச் செல்ல வேண்டும் எனப் பணிக்கப்பட்டது?",
        [
            ("A", "Governor-General in Council", "கவர்னர்-ஜெனரல் கவுன்சில்"),
            ("B", "Supreme Court of Judicature at Fort William", "வில்லியம் கோட்டை உச்ச நீதிமன்றம்"),
            ("C", "British House of Lords in London", "லண்டனில் உள்ள பிரிட்டிஷ் பிரபுக்கள் சபை"),
            ("D", "Court of Directors of East India Company", "கிழக்கிந்திய கம்பெனியின் இயக்குநர்கள் அவை")
        ],
        "A",
        "Historical Context: Resolving jurisdictional conflict between Supreme Court and executive provincial courts in 1781.\nReason: Amending Act 1781 explicitly laid down that appeals from the Provincial Courts (Sadar Diwani Adalat) were to be taken to the Governor-General in Council, and NOT to the Supreme Court. The Governor-General in Council was also empowered to frame regulations for the Provincial Courts.\nConstitutional Impact: Recognized Governor-General in Council as the supreme provincial appellate court.\nExam Trap: Appeals from Provincial Courts went to GG-in-Council (1781), NOT Supreme Court at Fort William.\nMemory Trick: 1781 Act = Provincial Court Appeals $\rightarrow$ Governor-General in Council.",
        "வரலாற்றுப் பின்னணி: 1781-ல் உச்ச நீதிமன்றத்திற்கும் மாகாண நீதிமன்றங்களுக்கும் இடையிலான அதிகார மோதலைத் தீர்த்தல்.\nகாரணம்: 1781 திருத்தச் சட்டம் மாகாண நீதிமன்ற மேல்முறையீடுகள் கவர்னர்-ஜெனரல் கவுன்சிலுக்கே செல்ல வேண்டும், உச்ச நீதிமன்றத்திற்கு அல்ல எனத் தெளிவாக விதித்தது. மாகாண நீதிமன்றங்களுக்கான விதிகளை உருவாக்கவும் கவர்னர்-ஜெனரல் கவுன்சிலுக்கு அதிகாரமளித்தது.\nஅரசியலமைப்பு தாக்கம்: கவர்னர்-ஜெனரல் கவுன்சிலை மாகாண உச்ச மேல்முறையீட்டு மன்றமாக அங்கீகரித்தது.\nதேர்வுப் பொறி: மாகாண நீதிமன்ற மேல்முறையீடுகள் கவர்னர்-ஜெனரல் கவுன்சிலுக்குச் சென்றன (1781), உச்ச நீதிமன்றத்திற்கு அல்ல.\nநினைவுச் சூத்திரம்: 1781 சட்டம் = மாகாண நீதிமன்ற மேல்முறையீடு $\rightarrow$ கவர்னர்-ஜெனரல் கவுன்சில்.",
        {
            "A": {"en": "Correct. 1781 Act directed appeals from Provincial Courts to Governor-General in Council.", "ta": "சரி. 1781 சட்டம் மாகாண நீதிமன்ற மேல்முறையீடுகளை கவர்னர்-ஜெனரல் கவுன்சிலுக்கு அனுப்பியது."},
            "B": {"en": "Incorrect. Supreme Court was specifically excluded from hearing provincial court appeals.", "ta": "தவறு. உச்ச நீதிமன்றம் மாகாண மேல்முறையீடுகளிலிருந்து விலக்கப்பட்டது."},
            "C": {"en": "Incorrect. House of Lords did not hear Indian provincial court appeals.", "ta": "தவறு. பிரபுக்கள் சபை மாகாண மேல்முறையீடுகளை விசாரிக்கவில்லை."},
            "D": {"en": "Incorrect. Court of Directors was a commercial-administrative body, not a court.", "ta": "தவறு. இயக்குநர்கள் அவை வணிக அமைப்பு, நீதிமன்றமல்ல."}
        },
        "TNPSC Trap: Appeals from Governor-General in Council in civil cases valued at £5,000 or more went to the King-in-Council (Privy Council) in London.",
        "TNPSC பொறி: £5,000 அல்லது அதற்கு மேற்பட்ட மதிப்புடைய வழக்குகளில் கவர்னர்-ஜெனரல் கவுன்சிலின் தீர்ப்பிற்கு எதிராக லண்டன் ப்ரிவி கவுன்சிலுக்கு மேல்முறையீடு செய்ய முடிந்தது.",
        "Regulations framed by Governor-General in Council for Provincial Courts under 1781 Act were known as 'Regulations'.",
        "1781 சட்டத்தில் கவர்னர்-ஜெனரல் கவுன்சில் உருவாக்கிய விதிகள் 'ஒழுங்குமுறைகள்' (Regulations) என அழைக்கப்பட்டன.",
        ["Polity", "Historical Background", "Act of Settlement 1781", "Provincial Appeals", "Grand Test"], "Understand", 60
    ))

    # Q94: Multi-Act Comparative - Hard - Evolution of Bicameral Provincial System
    questions.append(make_q(
        94, "Hard", "Multi-Act Comparative",
        "Which six provinces were made bicameral under the Government of India Act of 1935, and what were the names of their two chambers?",
        "1935 இந்திய அரசுச் சட்டத்தின் கீழ் இரு அவை அமைப்பாக மாற்றப்பட்ட ஆறு மாகாணங்கள் எவை, மேலும் அவற்றின் இரு அவைகளின் பெயர்கள் யாவை?",
        [
            ("A", "Provinces: Bengal, Bombay, Madras, Bihar, Assam, United Provinces; Chambers: Legislative Council (Upper House) and Legislative Assembly (Lower House)", "மாகாணங்கள்: வங்காளம், பம்பாய், மதராஸ், பீகார், அசாம், ஐக்கிய மாகாணங்கள்; அவைகள்: சட்ட மேலவை (மேலவை) மற்றும் சட்ட பேரவை (கீழவை)"),
            ("B", "Provinces: Punjab, Sindh, NWFP, CP, Orissa, Delhi; Chambers: Senate and House of Representatives", "மாகாணங்கள்: பஞ்சாப், சிந்து, NWFP, CP, ஒரிசா, டெல்லி; அவைகள்: செனட் மற்றும் பிரதிநிதிகள் சபை"),
            ("C", "Provinces: Bengal, Bombay, Madras only; Chambers: Council of State and House of Commons", "மாகாணங்கள்: வங்காளம், பம்பாய், மதராஸ் மட்டுமே; அவைகள்: மாநிலங்கள் குழு மற்றும் காமன்ஸ் சபை"),
            ("D", "All 11 Provinces were made bicameral with Legislative Council and State Assembly", "அனைத்து 11 மாகாணங்களும் சட்ட மேலவை மற்றும் மாநில பேரவையுடன் இரு அவைகளாக்கப்பட்டன")
        ],
        "A",
        "Historical Context: Regional bicameralism structure established under Government of India Act 1935.\nReason: 1935 Act introduced bicameralism in 6 out of 11 provinces: Bengal, Bombay, Madras, Bihar, Assam, and United Provinces (UP). The two chambers were named: Legislative Council (Upper House) and Legislative Assembly (Lower House).\nConstitutional Impact: Blueprint for Article 168/169 (State Legislative Councils and Assemblies) in modern Constitution.\nExam Trap: Modern Tamil Nadu abolished its Legislative Council in 1986; UP, Bihar, Maharashtra, Karnataka, Andhra, Telangana currently retain bicameralism.\nMemory Trick: 1935 Provincial 6 = 3 Presidencies (Bengal, Bombay, Madras) + 3 Provinces (Bihar, Assam, UP).",
        "வரலாற்றுப் பின்னணி: 1935 இந்திய அரசுச் சட்டத்தின் கீழ் அமைக்கப்பட்ட மாகாண இரு அவை கட்டமைப்பு.\nகாரணம்: 1935 சட்டம் 11-ல் 6 மாகாணங்களில் இரு அவை முறையைக் கொண்டுவந்தது: வங்காளம், பம்பாய், மதராஸ், பீகார், அசாம், ஐக்கிய மாகாணங்கள் (UP). இரு அவைகளின் பெயர்கள்: சட்ட மேலவை (மேலவை) மற்றும் சட்ட பேரவை (கீழவை).\nஅரசியலமைப்பு தாக்கம்: நவீன அரசியலமைப்பின் சரத்து 168/169 (மாநில சட்ட மேலவை & பேரவை) விதிகளுக்கு வரைபடம்.\nதேர்வுப் பொறி: தமிழ்நாடு தனது சட்ட மேலவையை 1986-ல் ஒழித்தது; தற்போது UP, பீகார், மகாராஷ்டிரா, கர்நாடகா, ஆந்திரா, தெலங்கானா ஆகியவை இரு அவைகளைக் கொண்டுள்ளன.\nநினைவுச் சூத்திரம்: 1935 மாகாண 6 = 3 மாகாண நகரங்கள் (வங்காளம், பம்பாய், மதராஸ்) + 3 மாகாணங்கள் (பீகார், அசாம், UP).",
        {
            "A": {"en": "Correct. 6 provinces (Bengal, Bombay, Madras, Bihar, Assam, UP) had Legislative Council & Assembly.", "ta": "சரி. 6 மாகாணங்கள் (வங்காளம், பம்பாய், மதராஸ், பீகார், அசாம், UP) சட்ட மேலவை & பேரவையைக் கொண்டிருந்தன."},
            "B": {"en": "Incorrect. Punjab, Sindh, NWFP, CP, Orissa were unicameral.", "ta": "தவறு. பஞ்சாப், சிந்து போன்றவை ஓரவை அமைப்புகள்."},
            "C": {"en": "Incorrect. Bihar, Assam, UP were also included making 6.", "ta": "தவறு. பீகார், அசாம், UP ஆகியவையும் சேர்த்து 6."},
            "D": {"en": "Incorrect. Only 6 of 11 provinces were bicameral.", "ta": "தவறு. 11-ல் 6 மட்டுமே இரு அவைகளாக்கப்பட்டன."}
        },
        "TNPSC Trap: Tamil Nadu Legislative Council was abolished by M.G. Ramachandran government with effect from November 1, 1986.",
        "TNPSC பொறி: தமிழ்நாடு சட்ட மேலவை 1986 நவம்பர் 1 முதல் எம்.ஜி. இராமச்சந்திரன் அரசால் ஒழிக்கப்பட்டது.",
        "Legislative Council in provinces had 1/3rd members retiring periodically under 1935 Act.",
        "1935 சட்டத்தின் கீழ் மாகாண சட்ட மேலவைகளில் 1/3 பங்கு உறுப்பினர்கள் சுழற்சி முறையில் ஓய்வுபெற்றனர்.",
        ["Polity", "Historical Background", "GOI Act 1935", "Provincial Bicameralism", "Article 169 Precursor", "Grand Test"], "Analyze", 75
    ))

    # Q95: Statement Based - Hard - Indian Independence Act 1947 Executive Discretion Transition
    questions.append(make_q(
        95, "Hard", "Statement Based",
        "Consider the following statements regarding executive administration during the interim period (August 15, 1947 to January 26, 1950) under the Indian Independence Act 1947:\n1. The Governor-General of India and Provincial Governors lost their discretionary powers and special responsibilities.\n2. The Governor-General and Governors acted strictly as constitutional (nominal) heads on the advice of their respective council of ministers.\n3. Until the new Constitution was adopted, governance in India was conducted under the adapted Government of India Act of 1935.\nWhich of the statements given above are correct?",
        "1947 இந்திய சுதந்திரச் சட்டத்தின் கீழ் இடைக்காலப் பகுதியில் (ஆகஸ்ட் 15, 1947 முதல் ஜனவரி 26, 1950 வரை) நிர்வாக முறை பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இந்திய கவர்னர்-ஜெனரல் மற்றும் மாகாண கவர்னர்கள் தங்களது தன்னிச்சையான அதிகாரங்களையும் சிறப்புப் பொறுப்புகளையும் இழந்தனர்.\n2. கவர்னர்-ஜெனரல் மற்றும் கவர்னர்கள் தங்களது அமைச்சரவையின் ஆலோசனையின்படி மட்டுமே செயல்படும் அரசியலமைப்பு (பெயரளவு) தலைவர்களாகச் செயல்பட்டனர்.\n3. புதிய அரசியலமைப்பு அமலுக்கு வரும் வரை, இந்தியாவில் ஆட்சி திருத்தப்பட்ட 1935 இந்திய அரசுச் சட்டத்தின் கீழ் நடத்தப்பட்டது.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?",
        [
            ("A", "1, 2 and 3", "1, 2 மற்றும் 3"),
            ("B", "1 and 2 only", "1 மற்றும் 2 மட்டுமே"),
            ("C", "2 and 3 only", "2 மற்றும் 3 மட்டுமே"),
            ("D", "1 and 3 only", "1 மற்றும் 3 மட்டுமே")
        ],
        "A",
        "Historical Context: Constitutional transition during the Dominion period (1947-1950) prior to the Republic.\nReason: All three statements are correct. 1947 Act stripped Governor-General and Governors of discretionary veto/special responsibilities (Statement 1), turned them into constitutional nominal heads acting on advice of popular ministers (Statement 2), and adapted 1935 GOI Act as India's interim constitution (Statement 3).\nConstitutional Impact: Established full parliamentary executive responsibility ahead of 1950 Constitution.\nExam Trap: 1935 Act had discretionary powers; 1947 Act ELIMINATED discretionary powers for interim period.\nMemory Trick: 1947-1950 Interim Governance = Adapted 1935 Act + Nominal GG + Cabinet Advice.",
        "வரலாற்றுப் பின்னணி: குடியரசுக்கு முந்தைய டொமினியன் காலத்தில் (1947-1950) அரசியலமைப்பு மாற்றம்.\nகாரணம்: மூன்று கூற்றுகளும் சரியானவை. 1947 சட்டம் கவர்னர்-ஜெனரல் மற்றும் கவர்னர்களின் தன்னிச்சை அதிகாரங்களை ஒழித்தது (கூற்று 1), அவர்களை அமைச்சரவை ஆலோசனையின்படி செயல்படும் பெயரளவு தலைவர்களாக்கியது (கூற்று 2), திருத்தப்பட்ட 1935 அரசுச் சட்டத்தை இடைக்கால அரசியலமைப்பாக்கியது (கூற்று 3).\nஅரசியலமைப்பு தாக்கம்: 1950 அரசியலமைப்புக்கு முன் முழு நாடாளுமன்ற நிர்வாகப் பொறுப்பை நிறுவியது.\nதேர்வுப் பொறி: 1935 சட்டத்தில் தன்னிச்சை அதிகாரம் இருந்தது; 1947 சட்டம் அதை இடைக்காலப் பகுதியில் ஒழித்தது.\nநினைவுச் சூத்திரம்: 1947-1950 இடைக்கால ஆட்சி = திருத்தப்பட்ட 1935 சட்டம் + பெயரளவு GG + அமைச்சரவை ஆலோசனை.",
        {
            "A": {"en": "Correct. All three statements accurately describe interim administration under 1947 Act.", "ta": "சரி. 1947 சட்டத்தின் கீழ் இடைக்கால நிர்வாகத்தின் மூன்று கூற்றுகளும் துல்லியமாக சரியானவை."},
            "B": {"en": "Incorrect. Statement 3 is also correct.", "ta": "தவறு. கூற்று 3-ம் சரியானது."},
            "C": {"en": "Incorrect. Statement 1 is also correct.", "ta": "தவறு. கூற்று 1-ம் சரியானது."},
            "D": {"en": "Incorrect. Statement 2 is also correct.", "ta": "தவறு. கூற்று 2-ம் சரியானது."}
        },
        "TNPSC Trap: India remained a British Dominion from August 15, 1947 to January 26, 1950, when it declared itself a Sovereign Democratic Republic.",
        "TNPSC பொறி: இந்தியா 1947 ஆகஸ்ட் 15 முதல் 1950 ஜனவரி 26 வரை பிரிட்டிஷ் டொமினியனாகவே இருந்தது, அதன் பின்னரே இறையாண்மை கொண்ட ஜனநாயக குடியரசாக அறிவித்துக் கொண்டது.",
        "Lord Mountbatten was requested by Jawaharlal Nehru to serve as 1st Governor-General of Dominion of India.",
        "ஜவஹர்லால் நேருவின் வேண்டுகோளின் பேரில் லார்டு மவுண்ட்பேட்டன் இந்திய டொமினியனின் 1வது கவர்னர்-ஜெனரலாகப் பணியாற்றினார்.",
        ["Polity", "Historical Background", "Indian Independence Act 1947", "Interim Governance", "Grand Test"], "Analyze", 75
    ))

    # Q96: Direct MCQ - Medium - Charter Act 1833 Law Member Voting Power
    questions.append(make_q(
        96, "Medium", "Direct MCQ",
        "Under the Charter Act of 1833, what specific voting limitation was initially placed on the 4th Law Member (Lord Macaulay) in the Governor-General's Executive Council?",
        "1833 ஆம் ஆண்டின் சாசனச் சட்டத்தின் கீழ், கவர்னர்-ஜெனரலின் நிர்வாகக் குழுவில் 4வது சட்ட உறுப்பினருக்கு (லார்டு மெக்காலே) தொடக்கத்தில் என்ன குறிப்பிட்ட வாக்களிப்பு கட்டுப்பாடு விதிக்கப்பட்டது?",
        [
            ("A", "The Law Member was permitted to sit and vote ONLY during meetings held for legislative purposes, and had no vote in executive matters.", "சட்ட உறுப்பினர் சட்டமியற்றும் கூட்டங்களில் மட்டுமே அமர்ந்து வாக்களிக்க அனுமதிக்கப்பட்டார்; நிர்வாக விவகாரங்களில் வாக்களிக்கும் அதிகாரம் இருக்கவில்லை."),
            ("B", "The Law Member had full voting rights on all military and financial executive decisions.", "சட்ட உறுப்பினருக்கு அனைத்து இராணுவ மற்றும் நிதி நிர்வாக முடிவுகளிலும் முழு வாக்களிப்பு உரிமை இருந்தது."),
            ("C", "The Law Member could vote only to break a tie between executive members.", "நிர்வாக உறுப்பினர்களிடையே சமநிலை ஏற்படும் போது மட்டுமே சட்ட உறுப்பினர் வாக்களிக்க முடியும்."),
            ("D", "The Law Member was given permanent veto power over the Governor-General.", "சட்ட உறுப்பினருக்கு கவர்னர்-ஜெனரலை நிராகரிக்கும் நிரந்தர தடுப்பதிகாரம் வழங்கப்பட்டது.")
        ],
        "A",
        "Historical Context: Initial separation of legislative function from executive voting under Charter Act 1833.\nReason: Under 1833 Act, the 4th Law Member (Macaulay) was added as a full member for legislative meetings only. He had no vote in executive council meetings until the Charter Act of 1853 made him a full-fledged executive council member.\nConstitutional Impact: Early institutional division between legislative drafting and executive administration.\nExam Trap: 1833 Act = Law member voted ONLY on legislative matters; 1853 Act = Law member became FULL voting executive member.\nMemory Trick: 1833 Law Member = Legislative Vote Only; 1853 Law Member = Full Executive & Legislative Vote.",
        "வரலாற்றுப் பின்னணி: 1833 சாசனச் சட்டத்தின் கீழ் நிர்வாக வாக்களிப்பிலிருந்து சட்டச் செயல்பாட்டின் தொடக்கக்காலப் பிரிப்பு.\nகாரணம்: 1833 சட்டத்தில் 4வது சட்ட உறுப்பினர் (மெக்காலே) சட்டக் கூட்டங்களுக்கு மட்டுமே உறுப்பினராகச் சேர்க்கப்பட்டார். 1853 சாசனச் சட்டம் அவரை முழு உறுப்பினராக்கும் வரை நிர்வாகக் கூட்டங்களில் அவருக்கு வாக்களிக்கும் அதிகாரம் இருக்கவில்லை.\nஅரசியலமைப்பு தாக்கம்: சட்ட வரைவுக்கும் நிர்வாகத்திற்குமான ஆரம்பகால நிறுவனப் பிரிப்பு.\nதேர்வுப் பொறி: 1833 சட்டம் = சட்ட உறுப்பினருக்கு சட்ட விஷயங்களில் மட்டுமே வாக்கு; 1853 சட்டம் = முழு நிர்வாக வாக்களிப்பு அதிகாரம்.\nநினைவுச் சூத்திரம்: 1833 சட்ட உறுப்பினர் = சட்ட வாக்கு மட்டும்; 1853 சட்ட உறுப்பினர் = முழு நிர்வாக & சட்ட வாக்கு.",
        {
            "A": {"en": "Correct. 1833 Law Member could sit and vote only during legislative meetings.", "ta": "சரி. 1833 சட்ட உறுப்பினர் சட்டக் கூட்டங்களில் மட்டுமே அமர்ந்து வாக்களிக்க முடியும்."},
            "B": {"en": "Incorrect. He had no vote on military or financial executive decisions.", "ta": "தவறு. இராணுவ, நிதி நிர்வாக முடிவுகளில் வாக்குரிமை இல்லை."},
            "C": {"en": "Incorrect. He could not vote in executive meetings at all.", "ta": "தவறு. நிர்வாகக் கூட்டங்களில் வாக்களிக்க முடியாது."},
            "D": {"en": "Incorrect. He had no veto power over Governor-General.", "ta": "தவறு. கவர்னர்-ஜெனரலை நிராகரிக்கும் அதிகாரம் இல்லை."}
        },
        "TNPSC Trap: Charter Act 1853 converted the 4th Law Member into a full, permanent executive council member with equal voting rights.",
        "TNPSC பொறி: 1853 சாசனச் சட்டம் 4வது சட்ட உறுப்பினரை சம வாக்களிப்பு அதிகாரம் கொண்ட முழு நிரந்தர நிர்வாகக் குழு உறுப்பினராக மாற்றியது.",
        "Lord Macaulay introduced the English Education Act 1835 in India as 4th Law Member.",
        "லார்டு மெக்காலே 4வது சட்ட உறுப்பினராக இருந்தபோதே 1835 ஆங்கிலக் கல்விச் சட்டத்தை இந்தியாவில் கொண்டுவந்தார்.",
        ["Polity", "Historical Background", "Charter Act 1833", "Law Member Voting Power", "Grand Test"], "Understand", 60
    ))

    # Q97: Multi-Act Comparative - Hard - Evolution of Bicameral Franchise Representation
    questions.append(make_q(
        97, "Hard", "Multi-Act Comparative",
        "Which multi-act comparison accurately tracks how the Indian Legislative Council evolved from a purely nominated body in 1861 to a fully sovereign Parliament in 1947?",
        "1861-ல் வெறும் நியமன அமைப்பாக இருந்த இந்திய சட்ட மேலவை 1947-ல் எவ்வாறு முழு இறையாண்மை கொண்ட நாடாளுமன்றமாக வளர்ந்தது என்பதைத் துல்லியமாக ஒப்பிடும் முடிவு எது?",
        [
            ("A", "1861 (Nominated non-officials added) -> 1892 (Indirect recommendation system) -> 1909 (Direct representation for Muslims & non-official majority in provinces) -> 1919 (Central bicameralism with directly elected majority) -> 1935 (Provincial autonomy & expanded franchise) -> 1947 (Sovereign Constituent Assembly acting as Parliament)", "1861 (நியமன உறுப்பினர்கள் சேர்க்கை) -> 1892 (மறைமுகப் பரிந்துரை முறை) -> 1909 (முஸ்லிம்களுக்கு நேரடிப் பிரதிநிதித்துவம் & மாகாண பெரும்பான்மை) -> 1919 (மத்திய இரு அவை முறை & நேரடித் தேர்தல்) -> 1935 (மாகாண தன்னாட்சி & வாக்குரிமை விரிவாக்கம்) -> 1947 (நாடாளுமன்றமாக இயங்கும் இறையாண்மை சபை)"),
            ("B", "1861 (Sovereign Parliament) -> 1892 (Dyarchy) -> 1909 (Abolition of councils) -> 1919 (Crown takeover) -> 1947 (Colonial body)", "1861 (இறையாண்மை நாடாளுமன்றம்) -> 1892 (இரட்டை ஆட்சி) -> 1909 (மேலவை ஒழிப்பு) -> 1919 (முடி ஆட்சி) -> 1947 (காலனித்துவ அமைப்பு)"),
            ("C", "1861 (Direct elections) -> 1892 (No representation) -> 1919 (Nominated body) -> 1947 (Provisional military council)", "1861 (நேரடித் தேர்தல்) -> 1892 (பிரதிநிதித்துவமில்லை) -> 1919 (நியமன அமைப்பு) -> 1947 (தற்காலிக இராணுவக் குழு)"),
            ("D", "No legislative structural change occurred between 1861 and 1947", "1861 மற்றும் 1947 இடையே எந்தவொரு சட்டமன்றக் கட்டமைப்பு மாற்றமும் நிகழவில்லை")
        ],
        "A",
        "Historical Context: Master evolutionary arc of Indian legislature over 86 years from 1861 to 1947.\nReason: 1861 (Non-official nominations) $\rightarrow$ 1892 (Indirect electoral recommendations) $\rightarrow$ 1909 (Separate electorates + non-official provincial majority) $\rightarrow$ 1919 (Direct elections + Central bicameralism) $\rightarrow$ 1935 (Provincial autonomy + 6 provincial upper houses) $\rightarrow$ 1947 (Sovereign Constituent Assembly acting as interim Parliament of free India).\nConstitutional Impact: Transformed a colonial advisory council into the sovereign Parliament of India.\nExam Trap: Legislative evolution took place across 6 major enactments over 86 years.\nMemory Trick: Nominated (1861) $\rightarrow$ Recommended (1892) $\rightarrow$ Electorates (1909) $\rightarrow$ Bicameral (1919) $\rightarrow$ Autonomous (1935) $\rightarrow$ Sovereign Parliament (1947).",
        "வரலாற்றுப் பின்னணி: 1861 முதல் 1947 வரை 86 ஆண்டுகளில் இந்திய சட்டமன்றத்தின் முதன்மையான வளர்ச்சி வளைவு.\nகாரணம்: 1861 (அதிகாரப்பூர்வமற்ற நியமனங்கள்) $\rightarrow$ 1892 (மறைமுகத் தேர்தல் பரிந்துரைகள்) $\rightarrow$ 1909 (தனித் தொகுதிகள் + மாகாண பெரும்பான்மை) $\rightarrow$ 1919 (நேரடித் தேர்தல் + மத்திய இரு அவை முறை) $\rightarrow$ 1935 (மாகாண தன்னாட்சி + 6 மாகாண மேலவைகள்) $\rightarrow$ 1947 (சுதந்திர இந்தியாவின் நாடாளுமன்றமாக இயங்கிய இறையாண்மை சபை).\nஅரசியலமைப்பு தாக்கம்: காலனித்துவ ஆலோசனைக் குழுவை சுதந்திர இந்தியாவின் இறையாண்மை நாடாளுமன்றமாக மாற்றியது.\nதேர்வுப் பொறி: சட்டமன்ற வளர்ச்சி 86 ஆண்டுகளில் 6 முக்கிய சட்டங்கள் வழியாக நிகழ்ந்தது.\nநினைவுச் சூத்திரம்: நியமனம் (1861) $\rightarrow$ பரிந்துரை (1892) $\rightarrow$ தொகுதி (1909) $\rightarrow$ இரு அவை (1919) $\rightarrow$ தன்னாட்சி (1935) $\rightarrow$ இறையாண்மை நாடாளுமன்றம் (1947).",
        {
            "A": {"en": "Correct master sequence of Indian legislative evolution from 1861 nomination to 1947 sovereign parliament.", "ta": "சரி. 1861 நியமனம் முதல் 1947 இறையாண்மை நாடாளுமன்றம் வரையிலான இந்திய சட்டமன்ற வளர்ச்சியின் முதன்மை வரிசை."},
            "B": {"en": "Incorrect. Reverses actual constitutional evolution.", "ta": "தவறு. உண்மையான அரசியலமைப்பு வளர்ச்சியை தலைகீழாக மாற்றுகிறது."},
            "C": {"en": "Incorrect. Direct elections began in 1919, not 1861.", "ta": "தவறு. நேரடித் தேர்தல் 1919-ல் தொடங்கியது."},
            "D": {"en": "Incorrect. Major structural changes occurred continuously.", "ta": "தவறு. தொடர்ச்சியான கட்டமைப்பு மாற்றங்கள் நிகழ்ந்தன."}
        },
        "TNPSC Trap: Indian Legislative Council had 0 elected members in 1861; 0% Indian sovereign control in 1858; 100% sovereign control in 1947.",
        "TNPSC பொறி: இந்திய சட்ட மேலவையில் 1861-ல் 0 தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்கள்; 1858-ல் 0% இந்திய இறையாண்மைக் கட்டுப்பாடு; 1947-ல் 100% இறையாண்மைக் கட்டுப்பாடு இருந்தது.",
        "G.V. Mavalankar served as the Speaker of the Constituent Assembly (Legislative) and became 1st Speaker of Lok Sabha in 1952.",
        "ஜி.வி. மாவிலங்கர் அரசியல் நிர்ணய சபையின் (சட்டமன்றம்) தலைவராக இருந்து 1952-ல் மக்களவையின் 1வது தலைவரானார்.",
        ["Polity", "Historical Background", "Legislative Master Evolution", "1861 to 1947", "Multi-Act Integration", "Grand Test"], "Analyze", 75
    ))

    # Q98: Direct MCQ - Hard - Amending Act 1781 Governor-General Regulation Rules
    questions.append(make_q(
        98, "Hard", "Direct MCQ",
        "Under the Amending Act of 1781 (Act of Settlement), what procedure was mandated for regulations framed by the Governor-General in Council for Provincial Courts?",
        "1781 ஆம் ஆண்டின் திருத்தச் சட்டத்தின் (சீர்முறைச் சட்டம்) கீழ், மாகாண நீதிமன்றங்களுக்காக கவர்னர்-ஜெனரல் கவுன்சில் உருவாக்கும் விதிகளுக்கு என்ன நடைமுறை ஆணையிடப்பட்டது?",
        [
            ("A", "Regulations framed by the Governor-General in Council did NOT require registration in the Supreme Court, but had to be sent to the British Sovereign in Council for approval.", "கவர்னர்-ஜெனரல் கவுன்சில் உருவாக்கும் விதிகளை உச்ச நீதிமன்றத்தில் பதிவு செய்யத் தேவையில்லை; ஆனால் பிரிட்டிஷ் மன்னரின் கவுன்சில் ஒப்புதலுக்கு அனுப்பப்பட வேண்டும்."),
            ("B", "Regulations had to be approved and registered by the Supreme Court before becoming law.", "விதிகளைச் சட்டமாக்குவதற்கு முன் உச்ச நீதிமன்றம் அங்கீகரித்துப் பதிவு செய்ய வேண்டும்."),
            ("C", "Regulations were subject to veto by the Mayor's Court of Calcutta.", "விதிகள் கொல்கத்தா மேயர் நீதிமன்றத்தின் தடுப்பதிகாரத்திற்கு உட்பட்டவை."),
            ("D", "Regulations had to be published in local Indian languages and approved by native Panchayats.", "விதிகள் உள்ளூர் இந்திய மொழிகளில் வெளியிடப்பட்டு உள்ளூர் பஞ்சாயத்துகளால் அங்கீகரிக்கப்பட வேண்டும்.")
        ],
        "A",
        "Historical Context: Resolving the 1773 Regulating Act defect which required Supreme Court registration for all GG-in-Council rules.\nReason: Under 1773 Act, rules framed by GG-in-Council had to be registered in Supreme Court. Amending Act 1781 removed this requirement for Provincial Court regulations, laying down that regulations formed by GG-in-Council did NOT need Supreme Court registration, but were to be transmitted to the King-in-Council in London.\nConstitutional Impact: Freed executive rule-making power from judicial registration veto.\nExam Trap: 1773 Act required SC registration; 1781 Act removed SC registration requirement for provincial court regulations.\nMemory Trick: 1773 = SC Registration Required; 1781 = SC Registration NOT Required.",
        "வரலாற்றுப் பின்னணி: கவர்னர்-ஜெனரல் கவுன்சிலின் அனைத்து விதிகளையும் உச்ச நீதிமன்றத்தில் பதிவு செய்யச் சொன்ன 1773 ஒழுங்குமுறைச் சட்டக் குறைபாட்டைத் தீர்த்தல்.\nகாரணம்: 1773 சட்டத்தில் கவர்னர்-ஜெனரல் கவுன்சில் விதிகள் உச்ச நீதிமன்றத்தில் பதிவு செய்யப்பட வேண்டும். 1781 திருத்தச் சட்டம் இத்தேவையை நீக்கி, மாகாண நீதிமன்ற விதிகளுக்கு உச்ச நீதிமன்றப் பதிவு தேவையில்லை, ஆனால் லண்டன் மன்னர் கவுன்சிலுக்கு அனுப்பப்பட வேண்டும் என விதித்தது.\nஅரசியலமைப்பு தாக்கம்: நிர்வாக விதி உருவாக்கலை நீதித்துறைப் பதிவுத் தடுப்பதிகாரத்திலிருந்து விடுவித்தது.\nதேர்வுப் பொறி: 1773 சட்டம் உச்ச நீதிமன்றப் பதிவைக் கோரியது; 1781 சட்டம் அத்தேவையை நீக்கியது.\nநினைவுச் சூத்திரம்: 1773 = உச்ச நீதிமன்றப் பதிவு தேவை; 1781 = உச்ச நீதிமன்றப் பதிவு தேவையில்லை.",
        {
            "A": {"en": "Correct. 1781 Act removed Supreme Court registration requirement for provincial regulations.", "ta": "சரி. 1781 சட்டம் மாகாண விதிகளுக்கான உச்ச நீதிமன்றப் பதிவுத் தேவையை நீக்கியது."},
            "B": {"en": "Incorrect. This was the requirement under 1773 Act, which 1781 Act abolished.", "ta": "தவறு. இது 1773 சட்டத்தின் தேவையாகும், 1781 சட்டம் அதை ஒழித்தது."},
            "C": {"en": "Incorrect. Mayor's Court had no veto power over Governor-General.", "ta": "தவறு. மேயர் நீதிமன்றத்திற்கு தடுப்பதிகாரம் இல்லை."},
            "D": {"en": "Incorrect. Native Panchayats were not statutory approval authorities.", "ta": "தவறு. உள்ளூர் பஞ்சாயத்துகள் சட்டப்பூர்வ அமைப்புகள் அல்ல."}
        },
        "TNPSC Trap: Amending Act 1781 is officially titled 'Act of Settlement' because it settled jurisdictional disputes between Supreme Court and Governor-General.",
        "TNPSC பொறி: 1781 திருத்தச் சட்டம் அதிகாரப்பூர்வமாக 'சீர்முறைச் சட்டம்' (Act of Settlement) என அழைக்கப்படுகிறது, ஏனெனில் அது உச்ச நீதிமன்றம்-கவர்னர்-ஜெனரல் மோதலைச் சீரமைத்தது.",
        "1781 Act declared that Governor-General in Council had the power to determine the rules for Provincial Courts.",
        "1781 சட்டம் மாகாண நீதிமன்றங்களுக்கான விதிகளைத் தீர்மானிக்கும் அதிகாரத்தை கவர்னர்-ஜெனரல் கவுன்சிலுக்கு அளித்தது.",
        ["Polity", "Historical Background", "Act of Settlement 1781", "Executive Regulation Rules", "Grand Test"], "Analyze", 75
    ))

    # Q99: Statement Based - Hard - Master Constitutional Landmarks Chronology
    questions.append(make_q(
        99, "Hard", "Statement Based",
        "Consider the following chronological events in the constitutional evolution of India:\n1. Establishment of Supreme Court of Judicature at Fort William (1774)\n2. Establishment of Board of Control under Pitt's India Act (1784)\n3. Creation of First Law Commission under Macaulay (1834)\n4. Creation of Central Legislative Council under Charter Act (1853)\n5. Queen Victoria's Proclamation transferring power to Crown (1858)\n6. Introduction of Portfolio System under Indian Councils Act (1861)\n7. Introduction of Separate Electorates under Morley-Minto Reforms (1909)\n8. Introduction of Provincial Dyarchy under Montagu-Chelmsford Reforms (1919)\nWhich option correctly verifies that all eight events listed above are in perfect historical chronological sequence?",
        "இந்திய அரசியலமைப்பு வளர்ச்சியில் பின்வரும் காலவரிசை நிகழ்வுகளைக் கவனியுங்கள்:\n1. வில்லியம் கோட்டையில் உச்ச நீதிமன்றம் அமைத்தல் (1774)\n2. பிட் இந்தியச் சட்டத்தின் கீழ் கட்டுப்பாட்டு வாரியம் அமைத்தல் (1784)\n3. மெக்காலே தலைமையில் முதல் சட்ட ஆணையம் உருவாக்கம் (1834)\n4. சாசனச் சட்டத்தின் கீழ் மத்திய சட்ட மேலவை உருவாக்கம் (1853)\n5. முடி ஆட்சிக்கு அதிகாரம் மாற்றிய விக்டோரியா மகாராணியின் பேரறிக்கை (1858)\n6. இந்தியக் கவுன்சில்கள் சட்டத்தின்கீழ் இலாகா முறை அறிமுகம் (1861)\n7. மோலி-மிண்டோ சீர்திருத்தங்களில் தனித் தொகுதி அறிமுகம் (1909)\n8. மாண்டேகு-செம்ஸ்ஃபோர்டு சீர்திருத்தங்களில் மாகாண இரட்டை ஆட்சி அறிமுகம் (1919)\nமேற்கண்ட எட்டு நிகழ்வுகளும் சரியான வரலாற்று காலவரிசையில் அமைந்துள்ளதை உறுதிப்படுத்தும் தெரிவு எது?",
        [
            ("A", "All events 1 through 8 are in exact correct chronological sequence", "1 முதல் 8 வரையிலான அனைத்து நிகழ்வுகளும் சரியான காலவரிசையில் உள்ளன"),
            ("B", "Events 3 and 4 are swapped in chronological sequence", "நிகழ்வுகள் 3 மற்றும் 4 காலவரிசையில் மாறியுள்ளன"),
            ("C", "Event 5 occurred before Event 3", "நிகழ்வு 5 நிகழ்வு 3-க்கு முன் நடந்தது"),
            ("D", "Event 7 occurred after Event 8", "நிகழ்வு 7 நிகழ்வு 8-க்கு பின் நடந்தது")
        ],
        "A",
        "Historical Context: Master chronological timeline test of foundational constitutional milestones from 1774 to 1919.\nReason: All eight events are listed in perfect historical order: 1 (1774 SC) $\rightarrow$ 2 (1784 Board) $\rightarrow$ 3 (1834 Law Comm) $\rightarrow$ 4 (1853 Council) $\rightarrow$ 5 (1858 Proclamation) $\rightarrow$ 6 (1861 Portfolio) $\rightarrow$ 7 (1909 Electorates) $\rightarrow$ 8 (1919 Dyarchy).\nConstitutional Impact: Represents the complete 145-year evolution from early Company regulation to Provincial Dyarchy.\nExam Trap: SC established 1774; Board of Control 1784; 1st Law Comm 1834; 1853 Council; 1858 Crown; 1861 Portfolio; 1909 Electorate; 1919 Dyarchy.\nMemory Trick: 1774 $\rightarrow$ 1784 $\rightarrow$ 1834 $\rightarrow$ 1853 $\rightarrow$ 1858 $\rightarrow$ 1861 $\rightarrow$ 1909 $\rightarrow$ 1919.",
        "வரலாற்றுப் பின்னணி: 1774 முதல் 1919 வரை அடிப்படை அரசியலமைப்பு மைல்கல்களின் முதன்மை காலவரிசை சோதனை.\nகாரணம்: எட்டு நிகழ்வுகளும் துல்லியமான வரலாற்று வரிசையில் உள்ளன: 1 (1774 உச்ச நீதிமன்றம்) $\rightarrow$ 2 (1784 கட்டுப்பாட்டு வாரியம்) $\rightarrow$ 3 (1834 சட்ட ஆணையம்) $\rightarrow$ 4 (1853 சட்ட மேலவை) $\rightarrow$ 5 (1858 பேரறிக்கை) $\rightarrow$ 6 (1861 இலாகா) $\rightarrow$ 7 (1909 தனித் தொகுதி) $\rightarrow$ 8 (1919 இரட்டை ஆட்சி).\nஅரசியலமைப்பு தாக்கம்: ஆரம்பகால கம்பெனி கட்டுப்பாட்டிலிருந்து மாகாண இரட்டை ஆட்சி வரையிலான 145 ஆண்டுகால வளர்ச்சியைக் காட்டுகிறது.\nதேர்வுப் பொறி: உச்ச நீதிமன்றம் 1774; கட்டுப்பாட்டு வாரியம் 1784; 1வது சட்ட ஆணையம் 1834; 1853 மேலவை; 1858 முடி ஆட்சி; 1861 இலாகா; 1909 தனித் தொகுதி; 1919 இரட்டை ஆட்சி.\nநினைவுச் சூத்திரம்: 1774 $\rightarrow$ 1784 $\rightarrow$ 1834 $\rightarrow$ 1853 $\rightarrow$ 1858 $\rightarrow$ 1861 $\rightarrow$ 1909 $\rightarrow$ 1919.",
        {
            "A": {"en": "Correct. All eight listed constitutional landmarks are in exact chronological sequence.", "ta": "சரி. பட்டியலிடப்பட்ட எட்டு அரசியலமைப்பு மைல்கல்களும் துல்லியமான காலவரிசையில் உள்ளன."},
            "B": {"en": "Incorrect. 1834 (Law Commission) correctly precedes 1853 (Central Legislative Council).", "ta": "தவறு. 1834 (சட்ட ஆணையம்) 1853-க்கு முந்தியது."},
            "C": {"en": "Incorrect. 1858 (Proclamation) occurred after 1834.", "ta": "தவறு. 1858 (பேரறிக்கை) 1834-க்கு பின் நடந்தது."},
            "D": {"en": "Incorrect. 1909 Morley-Minto occurred before 1919 Montagu-Chelmsford.", "ta": "தவறு. 1909 சீர்திருத்தம் 1919-க்கு முந்தியது."}
        },
        "TNPSC Trap: Always pay attention to exact enactment dates versus implementation dates (e.g. Regulating Act passed 1773, SC set up 1774; High Courts Act passed 1861, High Courts set up 1862).",
        "TNPSC பொறி: சட்டம் நிறைவேற்றப்பட்ட ஆண்டு மற்றும் அமலக்கப்பட்ட ஆண்டை கவனமாக ஆராய்க (எ.கா. ஒழுங்குமுறை சட்டம் 1773, உச்ச நீதிமன்றம் 1774; உயர் நீதிமன்ற சட்டம் 1861, நீதிமன்றங்கள் 1862).",
        "Government of India Act 1858 is also called 'Act for Better Government of India'.",
        "1858 இந்திய அரசுச் சட்டம் 'இந்திய நல்வாட்சிச் சட்டம்' என்றும் அழைக்கப்படுகிறது.",
        ["Polity", "Historical Background", "Master Chronology Timeline", "1774 to 1919", "Grand Test"], "Analyze", 75
    ))

    # Q100: Multi-Act Comparative - Exceptional Difficult - Final Synthesis of Constitutional Legacy
    questions.append(make_q(
        100, "Exceptional Difficult", "Multi-Act Comparative",
        "Which comprehensive constitutional synthesis best explains why the Constitution of India (1950) is often described as heavily indebted to the Government of India Act 1935, and how it transformed those colonial provisions into a sovereign democratic framework?",
        "இந்திய அரசியலமைப்பு (1950) ஏன் 1935 இந்திய அரசுச் சட்டத்திற்கு அதிகக் கடமைப்பட்டதாக விவரிக்கப்படுகிறது என்பதையும், அது அக்காலனித்துவ விதிகளை எவ்வாறு இறையாண்மை கொண்ட ஜனநாயகச் சட்டகமாக மாற்றியது என்பதையும் சிறப்பாக விளக்கும் விரிவான அரசியலமைப்புத் தொகுப்பு எது?",
        [
            ("A", "The 1950 Constitution borrowed about 250 provisions structurally from the 1935 Act (Federal Scheme, Judiciary, Public Service Commissions, Emergency provisions, Administrative details, DPSP precursor), but completely transformed them by removing British royal veto, abolishing communal electorates, introducing Universal Adult Suffrage, guaranteeing enforceable Fundamental Rights, and establishing popular parliamentary sovereignty", "1950 அரசியலமைப்பு 1935 சட்டத்திலிருந்து சுமார் 250 விதிகளை கட்டமைப்பாகப் பெற்றது (கூட்டாட்சித் திட்டம், நீதித்துறை, பொதுப்பணி ஆணையங்கள், அவசரகால விதிகள், நிர்வாக விவரங்கள், DPSP முன்னோடி); ஆனால் பிரிட்டிஷ் மன்னரின் தடுப்பதிகாரத்தை நீக்கி, வகுப்புவாத தொகுதிகளை ஒழித்து, உலகளாவிய வாக்குரிமை, அடிப்படை உரிமைகள் மற்றும் மக்கள் இறையாண்மையை நிறுவி அவற்றை முழுமையாக உருமாற்றியது"),
            ("B", "The 1950 Constitution copied the 1935 Act word-for-word without making any changes to its colonial features", "1950 அரசியலமைப்பு 1935 சட்டத்தின் காலனித்துவ அம்சங்களில் எந்த மாற்றமும் செய்யாமல் வார்த்தைக்கு வார்த்தை அப்படியே நகலெடுத்தது"),
            ("C", "The 1950 Constitution rejected all provisions of the 1935 Act and adopted US Constitution entirely", "1950 அரசியலமைப்பு 1935 சட்டத்தின் அனைத்து விதிகளையும் நிராகரித்து அமெரிக்க அரசியலமைப்பை முழுமையாக ஏற்றது"),
            ("D", "The 1935 Act was enacted after the 1950 Constitution to repeal Indian independence", "1935 சட்டம் இந்திய சுதந்திரத்தை ரத்து செய்ய 1950 அரசியலமைப்புக்கு பின்னர் இயற்றப்பட்டது")
        ],
        "A",
        "Historical Context: Grand synthesis of the historical evolution of Indian Constitution from 1773 to 1950.\nReason: Option A provides the exact constitutional analysis. Over 250 articles of 1950 Constitution are structural descendants of GOI Act 1935 (Federal System, Governor's office, Judiciary, Public Service Commissions, Emergency Provisions, Administrative setup). However, the Constituent Assembly infused democratic spirit by adding Fundamental Rights (Part III), Preamble sovereignty, Universal Adult Suffrage (Art 326), and abolishing communal electorates.\nConstitutional Impact: Transformed an administrative colonial statute into a democratic Constitution of We, the People of India.\nExam Trap: 1935 Act provided the STRUCTURAL framework; American/British/Irish Constitutions provided DEMOCRATIC PHILOSOPHICAL spirit.\nMemory Trick: Structure = GOI Act 1935 (~250 Articles); Spirit = We, the People (Sovereign Republic).",
        "வரலாற்றுப் பின்னணி: 1773 முதல் 1950 வரை இந்திய அரசியலமைப்பு வரலாற்று வளர்ச்சியின் பிரம்மாண்டமான தொகுப்பு.\nகாரணம்: தெரிவு A சரியான அரசியலமைப்பு பகுப்பாய்வை அளிக்கிறது. 1950 அரசியலமைப்பின் 250-க்கும் மேற்பட்ட சரத்துகள் 1935 சட்டத்தின் கட்டமைப்பு வாரிசுகளாகும் (கூட்டாட்சி முறை, கவர்னர் பதவி, நீதித்துறை, பொதுப்பணி ஆணையங்கள், அவசரகால விதிகள், நிர்வாக அமைப்பு). இருப்பினும், அரசியல் நிர்ணய சபை அடிப்படை உரிமைகள் (பகுதி III), முகப்புரை இறையாண்மை, உலகளாவிய வாக்குரிமை (சரத்து 326), வகுப்புவாத தொகுதி ஒழிப்பு ஆகியவற்றின் மூலம் ஜனநாயக ஆன்மாவை ஊட்டியது.\nஅரசியலமைப்பு தாக்கம்: ஒரு காலனித்துவ நிர்வாகச் சட்டத்தை 'இந்திய மக்களாகிய நாம்' என்ற ஜனநாயக அரசியலமைப்பாக மாற்றியது.\nதேர்வுப் பொறி: 1935 சட்டம் கட்டமைப்புச் சட்டகத்தை அளித்தது; அமெரிக்க/பிரிட்டிஷ்/ஐரிஷ் அரசியலமைப்புகள் ஜனநாயகத் தத்துவ உணர்வை அளித்தன்.\nநினைவுச் சூத்திரம்: கட்டமைப்பு = 1935 சட்டம் (~250 சரத்துகள்); ஆன்மா = இந்திய மக்களாகிய நாம் (இறையாண்மை குடியரசு).",
        {
            "A": {"en": "Correct master synthesis explaining how 1935 Act structure was transformed into 1950 Democratic Constitution.", "ta": "சரி. 1935 சட்டக் கட்டமைப்பு 1950 ஜனநாயக அரசியலமைப்பாக மாற்றப்பட்டதை விளக்கும் முதன்மைத் தொகுப்பு."},
            "B": {"en": "Incorrect. 1950 Constitution introduced fundamental rights, adult suffrage, and abolished communal electorates.", "ta": "தவறு. 1950 அரசியலமைப்பு அடிப்படை உரிமைகளையும் உலகளாவிய வாக்குரிமையையும் கொண்டுவந்தது."},
            "C": {"en": "Incorrect. 1950 Constitution heavily relied on 1935 Act for administrative backbone.", "ta": "தவறு. 1950 அரசியலமைப்பு 1935 சட்டத்தையே நிர்வாகக் தூணாகக் கொண்டது."},
            "D": {"en": "Incorrect. 1935 Act was enacted in 1935, 15 years before 1950 Constitution.", "ta": "தவறு. 1935 சட்டம் 1950-க்கு 15 ஆண்டுகள் முந்தியது."}
        },
        "TNPSC Trap: Dr. B.R. Ambedkar responded to criticism of copying 1935 Act: 'As to the accusation that the Draft Constitution has reproduced a good part of the provisions of the GOI Act 1935, I make no apologies. Nobody holds any patent rights in fundamental ideas of a Constitution'.",
        "TNPSC பொறி: 1935 சட்டத்தை நகலெடுத்ததாகக் கூறப்பட்ட விமர்சனத்திற்கு டாக்டர் அம்பேத்கர் கூறினார்: '1935 சட்டத்தின் பெரும் பகுதியை மறுஉருவாக்கம் செய்ததற்காக நான் மன்னிப்புக் கேட்க மாட்டேன். அரசியலமைப்பின் அடிப்படை யோசனைகளுக்கு யாரும் காப்புரிமை வைத்திருக்கவில்லை'.",
        "Constitution of India was adopted on November 26, 1949, and came into full force on January 26, 1950.",
        "இந்திய அரசியலமைப்பு 1949 நவம்பர் 26 அன்று ஏற்றுக்கொள்ளப்பட்டு, 1950 ஜனவரி 26 அன்று முழுமையாக அமலுக்கு வந்தது.",
        ["Polity", "Historical Background", "GOI Act 1935 Legacy", "1950 Constitution Foundation", "Grand Test Final Synthesis"], "Evaluate", 90
    ))

    return questions

if __name__ == "__main__":
    qs = get_part4_questions()
    print(f"Part 4 Questions Generated: {len(qs)}")
