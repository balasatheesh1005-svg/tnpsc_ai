def make_mf_q(q_id, q_type, q_en, q_ta, list1_en, list1_ta, list2_en, list2_ta,
              opt_a, opt_b, opt_c, opt_d, correct_ans, exp_en, exp_ta,
              wno_a_en, wno_a_ta, wno_b_en, wno_b_ta, wno_c_en, wno_c_ta, wno_d_en, wno_d_ta,
              tip_en, tip_ta, rev_en, rev_ta, bloom, est_time, tags):
    opts = [
        {"id": "A", "en": opt_a, "ta": opt_a},
        {"id": "B", "en": opt_b, "ta": opt_b},
        {"id": "C", "en": opt_c, "ta": opt_c},
        {"id": "D", "en": opt_d, "ta": opt_d}
    ]
    opts_en = [opt_a, opt_b, opt_c, opt_d]
    opts_ta = [opt_a, opt_b, opt_c, opt_d]
    
    l1_objs = [{"id": chr(65+i), "en": list1_en[i], "ta": list1_ta[i]} for i in range(len(list1_en))]
    l2_objs = [{"id": str(i+1), "en": list2_en[i], "ta": list2_ta[i]} for i in range(len(list2_en))]

    return {
        "id": q_id,
        "subject": "Polity",
        "topic": "Making of Indian Constitution",
        "difficulty": "Hard",
        "question_type": "Match the Following",
        "question": {"en": q_en, "ta": q_ta},
        "list_1": l1_objs,
        "list_2": l2_objs,
        "options": opts,
        "correct_answer": correct_ans,
        "explanation": {"en": exp_en, "ta": exp_ta},
        "why_not_others": {
            "A": {"en": wno_a_en, "ta": wno_a_ta},
            "B": {"en": wno_b_en, "ta": wno_b_ta},
            "C": {"en": wno_c_en, "ta": wno_c_ta},
            "D": {"en": wno_d_en, "ta": wno_d_ta}
        },
        "tnpsc_tip": {"en": tip_en, "ta": tip_ta},
        "revision_fact": {"en": rev_en, "ta": rev_ta},
        "source_reference": ["M. Laxmikanth - Indian Polity", "NCERT Class 11 - Indian Constitution at Work", "Constituent Assembly Debates"],
        "bloom_level": bloom,
        "estimated_time_sec": est_time,
        "pyq_similarity": "High",
        "tags": tags,
        "question_en": q_en,
        "question_ta": q_ta,
        "options_en": opts_en,
        "options_ta": opts_ta,
        "answer": correct_ans.lower(),
        "explanation_en": exp_en,
        "explanation_ta": exp_ta
    }

questions = []

# MIC_MF_001
questions.append(make_mf_q(
    "MIC_MF_001", "Match the Following",
    "Match List I (Major Committee of Constituent Assembly) with List II (Chairman) and select the correct answer using the codes given below:\n\nList I\nA. Union Powers Committee\nB. Provincial Constitution Committee\nC. Steering Committee\nD. Drafting Committee\n\nList II\n1. Sardar Vallabhbhai Patel\n2. Dr. B.R. Ambedkar\n3. Jawaharlal Nehru\n4. Dr. Rajendra Prasad",
    "பட்டியல் I-ஐ (அரசியலமைப்பு நிர்ணய அவையின் முக்கியக் குழுக்கள்) பட்டியல் II உடன் (தலைவர்) பொருத்தி கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான பதிலதைத் தேர்ந்தெடுக்கவும்:\n\nபட்டியல் I\nA. மத்திய அதிகாரக் குழு\nB. மாகாண அரசியலமைப்புக்குழு\nC. வழிநடத்தல் குழு\nD. வரைவுக் குழு\n\nபட்டியல் II\n1. சர்தார் வல்லபாய் படேல்\n2. டாக்டர் பி.ஆர். அம்பேத்கர்\n3. ஜவகர்லால் நேரு\n4. டாக்டர் ராஜேந்திர பிரசாத்",
    ["Union Powers Committee", "Provincial Constitution Committee", "Steering Committee", "Drafting Committee"],
    ["மத்திய அதிகாரக் குழு", "மாகாண அரசியலமைப்புக்குழு", "வழிநடத்தல் குழு", "வரைவுக் குழு"],
    ["Sardar Vallabhbhai Patel", "Dr. B.R. Ambedkar", "Jawaharlal Nehru", "Dr. Rajendra Prasad"],
    ["சர்தார் வல்லபாய் படேல்", "டாக்டர் பி.ஆர். அம்பேத்கர்", "ஜவகர்லால் நேரு", "டாக்டர் ராஜேந்திர பிரசாத்"],
    "A-3, B-1, C-4, D-2", "A-1, B-3, C-2, D-4", "A-3, B-4, C-1, D-2", "A-2, B-1, C-4, D-3",
    "A",
    "A-3: Union Powers Committee was chaired by Jawaharlal Nehru. B-1: Provincial Constitution Committee was chaired by Sardar Vallabhbhai Patel. C-4: Steering Committee was chaired by Dr. Rajendra Prasad. D-2: Drafting Committee was chaired by Dr. B.R. Ambedkar.",
    "A-3: மத்திய அதிகாரக் குழுவின் தலைவர் ஜவகர்லால் நேரு. B-1: மாகாண அரசியலமைப்புக்குழுவின் தலைவர் சர்தார் வல்லபாய் படேல். C-4: வழிநடத்தல் குழுவின் தலைவர் டாக்டர் ராஜேந்திர பிரசாத். D-2: வரைவுக் குழுவின் தலைவர் டாக்டர் பி.ஆர். அம்பேத்கர்.",
    "Correct. A-3, B-1, C-4, D-2 is the exact correct matching.", "சரி. A-3, B-1, C-4, D-2 சரியான பொருத்தம்.",
    "Incorrect. Nehru chaired Union Powers Committee (A-3), not Provincial Constitution Committee.", "தவறு. நேரு மத்திய அதிகாரக் குழுவின் தலைவர் (A-3).",
    "Incorrect. Rajendra Prasad chaired Steering Committee (C-4), not Provincial Constitution Committee.", "தவறு. ராஜேந்திர பிரசாத் வழிநடத்தல் குழுவின் தலைவர் (C-4).",
    "Incorrect. Ambedkar chaired Drafting Committee (D-2), not Union Powers Committee.", "தவறு. அம்பேத்கர் வரைவுக் குழுவின் தலைவர் (D-2).",
    "TNPSC Trap: Steering Committee Chair = Dr. Rajendra Prasad (NOT Dr. Ambedkar). Union Powers Committee = Jawaharlal Nehru.",
    "TNPSC பொறி: வழிநடத்தல் குழுத் தலைவர் = டாக்டர் ராஜேந்திர பிரசாத் (அம்பேத்கர் அல்ல). மத்திய அதிகாரக் குழு = ஜவகர்லால் நேரு.",
    "Dr. Rajendra Prasad also chaired the Rules of Procedure Committee.",
    "டாக்டர் ராஜேந்திர பிரசாத் நடைமுறை விதிகள் குழுவிற்கும் தலைமை தாங்கினார்.",
    "Analyze", 75, ["Polity", "Making of Indian Constitution", "Important Committees", "Drafting Committee", "Steering Committee"]
))

# MIC_MF_002
questions.append(make_mf_q(
    "MIC_MF_002", "Match the Following",
    "Match List I (Historical Date) with List II (Constitutional Milestone) and select the correct answer using the codes given below:\n\nList I\nA. December 9, 1946\nB. December 13, 1946\nC. January 22, 1947\nD. July 22, 1947\n\nList II\n1. Adoption of Objectives Resolution\n2. Adoption of the National Flag\n3. First meeting of Constituent Assembly\n4. Introduction of Objectives Resolution",
    "பட்டியல் I-ஐ (வரலாற்றுத் தேதி) பட்டியல் II உடன் (அரசியலமைப்பு மைல்கல்) பொருத்தி கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான பதிலதைத் தேர்ந்தெடுக்கவும்:\n\nபட்டியல் I\nA. டிசம்பர் 9, 1946\nB. டிசம்பர் 13, 1946\nC. ஜனவரி 22, 1947\nD. ஜூலை 22, 1947\n\nபட்டியல் II\n1. குறிக்கோள்கள் தீர்மானம் ஏற்றுக்கொள்ளப்பட்டது\n2. தேசியக் கொடி ஏற்றுக்கொள்ளப்பட்டது\n3. அரசியலமைப்பு நிர்ணய அவையின் முதல் கூட்டம்\n4. குறிக்கோள்கள் தீர்மானம் அறிமுகப்படுத்தப்பட்டது",
    ["December 9, 1946", "December 13, 1946", "January 22, 1947", "July 22, 1947"],
    ["டிசம்பர் 9, 1946", "டிசம்பர் 13, 1946", "ஜனவரி 22, 1947", "ஜூலை 22, 1947"],
    ["Adoption of Objectives Resolution", "Adoption of the National Flag", "First meeting of Constituent Assembly", "Introduction of Objectives Resolution"],
    ["குறிக்கோள்கள் தீர்மானம் ஏற்றுக்கொள்ளப்பட்டது", "தேசியக் கொடி ஏற்றுக்கொள்ளப்பட்டது", "அரசியலமைப்பு நிர்ணய அவையின் முதல் கூட்டம்", "குறிக்கோள்கள் தீர்மானம் அறிமுகப்படுத்தப்பட்டது"],
    "A-3, B-4, C-1, D-2", "A-1, B-3, C-4, D-2", "A-3, B-1, C-4, D-2", "A-4, B-3, C-2, D-1",
    "A",
    "A-3: Dec 9, 1946 was the First meeting of the Constituent Assembly. B-4: Dec 13, 1946 was Nehru introducing Objectives Resolution. C-1: Jan 22, 1947 was the unanimous adoption of Objectives Resolution. D-2: July 22, 1947 was the adoption of the National Flag.",
    "A-3: டிசம்பர் 9, 1946 முதல் கூட்டம். B-4: டிசம்பர் 13, 1946 குறிக்கோள்கள் தீர்மானம் அறிமுகம். C-1: ஜனவரி 22, 1947 குறிக்கோள்கள் தீர்மானம் ஏற்றுக்கொள்ளப்பட்டது. D-2: ஜூலை 22, 1947 தேசியக் கொடி ஏற்றுக்கொள்ளப்பட்டது.",
    "Correct. A-3, B-4, C-1, D-2 is the exact correct matching.", "சரி. A-3, B-4, C-1, D-2 சரியான பொருத்தம்.",
    "Incorrect. Dec 9 was first meeting (3), not adoption of Objectives Resolution (1).", "தவறு. டிசம்பர் 9 முதல் கூட்டம் (3).",
    "Incorrect. Dec 13 was introduction of Objectives Resolution (4), not adoption (1).", "தவறு. டிசம்பர் 13 தீர்மான அறிமுகம் (4).",
    "Incorrect. Dec 9 was first meeting (3), not introduction of Objectives Resolution (4).", "தவறு. டிசம்பர் 9 முதல் கூட்டம் (3).",
    "TNPSC Trap: Objectives Resolution introduced on Dec 13, 1946; Adopted on Jan 22, 1947 (NOT same day).",
    "TNPSC பொறி: குறிக்கோள்கள் தீர்மானம் அறிமுகம் டிசம்பர் 13, 1946; ஏற்கப்பட்டது ஜனவரி 22, 1947 (ஒரே நாளில் அல்ல).",
    "National Flag was adopted on July 22, 1947, just weeks before Independence.",
    "தேசியக் கொடி சுதந்திரத்திற்கு சில வாரங்களுக்கு முன்பு ஜூலை 22, 1947 அன்று ஏற்றுக்கொள்ளப்பட்டது.",
    "Analyze", 75, ["Polity", "Making of Indian Constitution", "Constitutional Milestones", "Important Dates", "National Flag"]
))

# MIC_MF_003
questions.append(make_mf_q(
    "MIC_MF_003", "Match the Following",
    "Match List I (Key Personality) with List II (Constitutional Role / Contribution) and select the correct answer using the codes given below:\n\nList I\nA. Dr. Sachchidananda Sinha\nB. H.C. Mookherjee\nC. Sir B.N. Rau\nD. S.N. Mukerjee\n\nList II\n1. Chief Draftsman of the Constitution\n2. Constitutional Adviser to the Assembly\n3. Vice-President of Constituent Assembly & Chair of Minorities Sub-Committee\n4. Temporary President of the Constituent Assembly",
    "பட்டியல் I-ஐ (முக்கிய ஆளுமை) பட்டியல் II உடன் (அரசியலமைப்புப் பங்கு / பங்களிப்பு) பொருத்தி கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான பதிலதைத் தேர்ந்தெடுக்கவும்:\n\nபட்டியல் I\nA. டாக்டர் சச்சிதானந்த சின்ஹா\nB. எச்.சி. முகர்ஜி\nC. சர் பி.என். ராவ்\nD. எஸ்.என். முகர்ஜி\n\nபட்டியல் II\n1. அரசியலமைப்பின் தலைமை வரைவாளர்\n2. அவையின் அரசியலமைப்பு ஆலோசகர்\n3. அரசியலமைப்பு அவையின் துணைத் தலைவர் & சிறுபான்மையினர் துணைக் குழுத் தலைவர்\n4. அரசியலமைப்பு அவையின் தற்காலிகத் தலைவர்",
    ["Dr. Sachchidananda Sinha", "H.C. Mookherjee", "Sir B.N. Rau", "S.N. Mukerjee"],
    ["டாக்டர் சச்சிதானந்த சின்ஹா", "எச்.சி. முகர்ஜி", "சர் பி.என். ராவ்", "எஸ்.என். முகர்ஜி"],
    ["Chief Draftsman of the Constitution", "Constitutional Adviser to the Assembly", "Vice-President of Constituent Assembly & Chair of Minorities Sub-Committee", "Temporary President of the Constituent Assembly"],
    ["அரசியலமைப்பின் தலைமை வரைவாளர்", "அவையின் அரசியலமைப்பு ஆலோசகர்", "அரசியலமைப்பு அவையின் துணைத் தலைவர் & சிறுபான்மையினர் துணைக் குழுத் தலைவர்", "அரசியலமைப்பு அவையின் தற்காலிகத் தலைவர்"],
    "A-4, B-3, C-2, D-1", "A-2, B-4, C-1, D-3", "A-4, B-1, C-2, D-3", "A-3, B-2, C-4, D-1",
    "A",
    "A-4: Dr. Sachchidananda Sinha was Temporary President (Dec 9, 1946). B-3: H.C. Mookherjee was Vice-President & Minorities Sub-Committee Chair. C-2: Sir B.N. Rau was Constitutional Adviser. D-1: S.N. Mukerjee was Chief Draftsman.",
    "A-4: டாக்டர் சச்சிதானந்த சின்ஹா தற்காலிகத் தலைவர். B-3: எச்.சி. முகர்ஜி துணைத் தலைவர் & சிறுபான்மையினர் துணைக் குழுத் தலைவர். C-2: சர் பி.என். ராவ் அரசியலமைப்பு ஆலோசகர். D-1: எஸ்.என். முகர்ஜி தலைமை வரைவாளர்.",
    "Correct. A-4, B-3, C-2, D-1 is the exact correct matching.", "சரி. A-4, B-3, C-2, D-1 சரியான பொருத்தம்.",
    "Incorrect. Sinha was Temporary President (A-4), not Constitutional Adviser (2).", "தவறு. சின்ஹா தற்காலிகத் தலைவர் (A-4).",
    "Incorrect. H.C. Mookherjee was Vice-President (B-3), not Chief Draftsman (1).", "தவறு. முகர்ஜி துணைத் தலைவர் (B-3).",
    "Incorrect. Sinha was Temporary President (A-4), not Vice-President (3).", "தவறு. சின்ஹா தற்காலிகத் தலைவர் (A-4).",
    "TNPSC Trap: Constitutional Adviser = Sir B.N. Rau (NOT member). Chief Draftsman = S.N. Mukerjee. Temporary President = Sachchidananda Sinha.",
    "TNPSC பொறி: அரசியலமைப்பு ஆலோசகர் = சர் பி.என். ராவ் (உறுப்பினர் அல்ல). தலைமை வரைவாளர் = எஸ்.என். முகர்ஜி. தற்காலிகத் தலைவர் = சச்சிதானந்த சின்ஹா.",
    "Dr. Sachchidananda Sinha was chosen following the French tradition of electing the oldest member.",
    "மூத்த உறுப்பினரைத் தேர்ந்தெடுக்கும் ஃபிரெஞ்சுக் வழக்கத்தின்படி டாக்டர் சச்சிதானந்த சின்ஹா தேர்ந்தெடுக்கப்பட்டார்.",
    "Analyze", 75, ["Polity", "Making of Indian Constitution", "Sachchidananda Sinha", "H. C. Mukherjee", "B. N. Rau", "Important Personalities"]
))

# MIC_MF_004
questions.append(make_mf_q(
    "MIC_MF_004", "Match the Following",
    "Match List I (Committee) with List II (Primary Function / Mandate) and select the correct answer using the codes given below:\n\nList I\nA. States Committee\nB. Advisory Committee\nC. Rules of Procedure Committee\nD. Drafting Committee\n\nList II\n1. Framing rules to conduct business in the Assembly\n2. Negotiating with Princely States regarding representation\n3. Preparing the legal text of the Draft Constitution\n4. Recommending on Fundamental Rights, Minorities, and Tribal Areas",
    "பட்டியல் I-ஐ (குழு) பட்டியல் II உடன் (முதன்மையான செயல்பாடு) பொருத்தி கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான பதிலதைத் தேர்ந்தெடுக்கவும்:\n\nபட்டியல் I\nA. மாநிலங்கள் குழு\nB. ஆலோசனைக் குழு\nC. நடைமுறை விதிகள் குழு\nD. வரைவுக் குழு\n\nபட்டியல் II\n1. அவையில் நடவடிக்கைகளை நடத்த விதிகளை உருவாக்குதல்\n2. பிரதிநிதித்துவம் தொடர்பாக சுதேச சமஸ்தானங்களுடன் பேச்சுவார்த்தை நடத்துதல்\n3. வரைவு அரசியலமைப்பின் சட்டப் உரையைத் தயாரித்தல்\n4. அடிப்படை உரிமைகள், சிறுபான்மையினர் மற்றும் பழங்குடியினர் பகுதிகள் குறித்து பரிந்துரைத்தல்",
    ["States Committee", "Advisory Committee", "Rules of Procedure Committee", "Drafting Committee"],
    ["மாநிலங்கள் குழு", "ஆலோசனைக் குழு", "நடைமுறை விதிகள் குழு", "வரைவுக் குழு"],
    ["Framing rules to conduct business in the Assembly", "Negotiating with Princely States regarding representation", "Preparing the legal text of the Draft Constitution", "Recommending on Fundamental Rights, Minorities, and Tribal Areas"],
    ["அவையில் நடவடிக்கைகளை நடத்த விதிகளை உருவாக்குதல்", "பிரதிநிதித்துவம் தொடர்பாக சுதேச சமஸ்தானங்களுடன் பேச்சுவார்த்தை நடத்துதல்", "வரைவு அரசியலமைப்பின் சட்டப் உரையைத் தயாரித்தல்", "அடிப்படை உரிமைகள், சிறுபான்மையினர் மற்றும் பழங்குடியினர் பகுதிகள் குறித்து பரிந்துரைத்தல்"],
    "A-2, B-4, C-1, D-3", "A-1, B-2, C-4, D-3", "A-2, B-1, C-4, D-3", "A-4, B-3, C-1, D-2",
    "A",
    "A-2: States Committee negotiated with Princely States. B-4: Advisory Committee recommended on FR, Minorities, Tribal areas. C-1: Rules of Procedure Committee framed procedural rules. D-3: Drafting Committee prepared legal text of draft constitution.",
    "A-2: மாநிலங்கள் குழு சமஸ்தானங்களுடன் பேச்சுவார்த்தை நடத்தியது. B-4: ஆலோசனைக் குழு அடிப்படை உரிமைகள், சிறுபான்மையினருக்குப் பரிந்துரைத்தது. C-1: நடைமுறை விதிகள் குழு விதிகளை வகுத்தது. D-3: வரைவுக் குழு வரைவு அரசியலமைப்பை தயாரித்தது.",
    "Correct. A-2, B-4, C-1, D-3 is the exact correct matching.", "சரி. A-2, B-4, C-1, D-3 சரியான பொருத்தம்.",
    "Incorrect. States Committee negotiated with princely states (2), not framed rules (1).", "தவறு. மாநிலங்கள் குழு பேச்சுவார்த்தை நடத்தியது (2).",
    "Incorrect. Advisory Committee recommended on FR (4), not framed rules (1).", "தவறு. ஆலோசனைக் குழு உரிமைகளுக்குப் பரிந்துரைத்தது (4).",
    "Incorrect. States Committee negotiated with princely states (2), not FR recommendation (4).", "தவறு. மாநிலங்கள் குழு பேச்சுவார்த்தை நடத்தியது (2).",
    "TNPSC Trap: States Committee (Committee for Negotiating with States) was chaired by Jawaharlal Nehru.",
    "TNPSC பொறி: மாநிலங்கள் குழு (மாநில பேச்சுவார்த்தைக் குழு) ஜவகர்லால் நேரு தலைமையிலானது.",
    "Advisory Committee headed by Sardar Patel was the largest committee of the Constituent Assembly.",
    "சர்தார் படேல் தலைமையிலான ஆலோசனைக் குழுவே அவையின் மிகப்பெரிய குழுவாகும்.",
    "Analyze", 75, ["Polity", "Making of Indian Constitution", "States Committee", "Advisory Committee", "Rules Committee", "Drafting Committee"]
))

# MIC_MF_005
questions.append(make_mf_q(
    "MIC_MF_005", "Match the Following",
    "Match List I (Drafting Committee Member) with List II (Background / Specific Contribution) and select the correct answer using the codes given below:\n\nList I\nA. Alladi Krishnaswamy Ayyar\nB. Dr. K.M. Munshi\nC. N. Gopalaswamy Ayyangar\nD. Syed Mohammad Saadulla\n\nList II\n1. Sole original Congress member in Drafting Committee & Order of Business Chair\n2. Former Premier of Assam & Muslim League representative\n3. Former Advocate-General of Madras State\n4. Former Prime Minister of Jammu & Kashmir & drafter of Article 370",
    "பட்டியல் I-ஐ (வரைவுக் குழு உறுப்பினர்) பட்டியல் II உடன் (பின்னணி / குறிப்பிட்ட பங்களிப்பு) பொருத்தி கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான பதிலதைத் தேர்ந்தெடுக்கவும்:\n\nபட்டியல் I\nA. அல்லாடி கிருஷ்ணசாமி அய்யர்\nB. டாக்டர் கே.எம். முன்ஷி\nC. என். கோபாலசாமி அய்யங்கார்\nD. சையத் முகமது சாதுல்லா\n\nபட்டியல் II\n1. வரைவுக் குழுவில் இருந்த ஒரே அசல் காங்கிரஸ் உறுப்பினர் & வணிக வரிசைக் குழுத் தலைவர்\n2. அசாமின் முன்னாள் பிரதமர் & முஸ்லீம் லீக் பிரதிநிதி\n3. மெட்ராஸ் மாகாணத்தின் முன்னாள் தலைமை வழக்கறிஞர்\n4. ஜம்மு காஷ்மீரின் முன்னாள் பிரதமர் & சரத்து 370 வரைவாளர்",
    ["Alladi Krishnaswamy Ayyar", "Dr. K.M. Munshi", "N. Gopalaswamy Ayyangar", "Syed Mohammad Saadulla"],
    ["அல்லாடி கிருஷ்ணசாமி அய்யர்", "டாக்டர் கே.எம். முன்ஷி", "என். கோபாலசாமி அய்யங்கார்", "சையத் முகமது சாதுல்லா"],
    ["Sole original Congress member in Drafting Committee & Order of Business Chair", "Former Premier of Assam & Muslim League representative", "Former Advocate-General of Madras State", "Former Prime Minister of Jammu & Kashmir & drafter of Article 370"],
    ["வரைவுக் குழுவில் இருந்த ஒரே அசல் காங்கிரஸ் உறுப்பினர் & வணிக வரிசைக் குழுத் தலைவர்", "அசாமின் முன்னாள் பிரதமர் & முஸ்லீம் லீக் பிரதிநிதி", "மெட்ராஸ் மாகாணத்தின் முன்னாள் தலைமை வழக்கறிஞர்", "ஜம்மு காஷ்மீரின் முன்னாள் பிரதமர் & சரத்து 370 வரைவாளர்"],
    "A-3, B-1, C-4, D-2", "A-1, B-3, C-2, D-4", "A-3, B-4, C-1, D-2", "A-4, B-1, C-3, D-2",
    "A",
    "A-3: Alladi Krishnaswamy Ayyar was Advocate-General of Madras. B-1: Dr. K.M. Munshi was sole original Congress member in Drafting Committee. C-4: N. Gopalaswamy Ayyangar was PM of J&K and drafted Art 370. D-2: Syed Mohammad Saadulla was Premier of Assam.",
    "A-3: அல்லாடி கிருஷ்ணசாமி மெட்ராஸ் தலைமை வழக்கறிஞர். B-1: கே.எம். முன்ஷி வரைவுக் குழுவில் இருந்த ஒரே அசல் காங்கிரஸ் உறுப்பினர். C-4: கோபாலசாமி அய்யங்கார் ஜம்மு காஷ்மீர் பிரதமர் & சரத்து 370 வரைவாளர். D-2: சாதுல்லா அசாம் பிரதமர்.",
    "Correct. A-3, B-1, C-4, D-2 is the exact correct matching.", "சரி. A-3, B-1, C-4, D-2 சரியான பொருத்தம்.",
    "Incorrect. Alladi Krishnaswamy Ayyar was Advocate-General of Madras (3), not Congress member (1).", "தவறு. அல்லாடி மெட்ராஸ் தலைமை வழக்கறிஞர் (3).",
    "Incorrect. Gopalaswamy Ayyangar drafted Art 370 (4), not Congress member (1).", "தவறு. கோபாலசாமி அய்யங்கார் சரத்து 370 வரைவாளர் (4).",
    "Incorrect. Alladi was Advocate-General of Madras (3), not PM of J&K (4).", "தவறு. அல்லாடி மெட்ராஸ் தலைமை வழக்கறிஞர் (3).",
    "TNPSC Trap: N. Gopalaswamy Ayyangar drafted Article 370. Dr. K.M. Munshi was the ONLY original Congress party candidate elected to the Drafting Committee.",
    "TNPSC பொறி: என். கோபாலசாமி அய்யங்கார் சரத்து 370 ஐ வரைந்தார். கே.எம். முன்ஷி மட்டுமே வரைவுக் குழுவில் தேர்ந்தெடுக்கப்பட்ட ஒரே அசல் காங்கிரஸ் வேட்பாளர்.",
    "Dr. Ambedkar was not a Congress member initially; he was elected from Scheduled Castes Federation.",
    "அம்பேத்கர் ஆரம்பத்தில் காங்கிரஸ் உறுப்பினர் அல்ல; அவர் பட்டியல் சாதியினர் கூட்டமைப்பில் இருந்து தேர்ந்தெடுக்கப்பட்டார்.",
    "Analyze", 75, ["Polity", "Making of Indian Constitution", "Drafting Committee", "Alladi Krishnaswamy Ayyar", "K. M. Munshi", "Gopalaswami Ayyangar"]
))

# MIC_MF_006
questions.append(make_mf_q(
    "MIC_MF_006", "Match the Following",
    "Match List I (Date) with List II (Constitutional Milestone / Event) and select the correct answer using the codes given below:\n\nList I\nA. August 29, 1947\nB. November 26, 1949\nC. January 24, 1950\nD. January 26, 1950\n\nList II\n1. Final session of Constituent Assembly & adoption of National Anthem/Song\n2. Setting up of the Drafting Committee under Dr. Ambedkar\n3. Commencement / Enforcement of the Constitution of India\n4. Passing and adoption of the Constitution by Constituent Assembly",
    "பட்டியல் I-ஐ (தேதி) பட்டியல் II உடன் (அரசியலமைப்பு மைல்கல் / நிகழ்வு) பொருத்தி கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான பதிலதைத் தேர்ந்தெடுக்கவும்:\n\nபட்டியல் I\nA. ஆகஸ்ட் 29, 1947\nB. நவம்பர் 26, 1949\nC. ஜனவரி 24, 1950\nD. ஜனவரி 26, 1950\n\nபட்டியல் II\n1. அரசியலமைப்பு அவையின் இறுதி அமர்வு & தேசிய கீதம்/பாடல் ஏற்றுக் கொள்ளப்பட்டது\n2. அம்பேத்கர் தலைமையில் வரைவுக் குழு அமைக்கப்பட்டது\n3. இந்திய அரசியலமைப்பு நடைமுறைக்கு வந்தது / தொடங்கியது\n4. அரசியலமைப்பு அவையால் அரசியலமைப்பு நிறைவேற்றப்பட்டு ஏற்றுக்கொள்ளப்பட்டது",
    ["August 29, 1947", "November 26, 1949", "January 24, 1950", "January 26, 1950"],
    ["ஆகஸ்ட் 29, 1947", "நவம்பர் 26, 1949", "ஜனவரி 24, 1950", "ஜனவரி 26, 1950"],
    ["Final session of Constituent Assembly & adoption of National Anthem/Song", "Setting up of the Drafting Committee under Dr. Ambedkar", "Commencement / Enforcement of the Constitution of India", "Passing and adoption of the Constitution by Constituent Assembly"],
    ["அரசியலமைப்பு அவையின் இறுதி அமர்வு & தேசிய கீதம்/பாடல் ஏற்றுக் கொள்ளப்பட்டது", "அம்பேத்கர் தலைமையில் வரைவுக் குழு அமைக்கப்பட்டது", "இந்திய அரசியலமைப்பு நடைமுறைக்கு வந்தது / தொடங்கியது", "அரசியலமைப்பு அவையால் அரசியலமைப்பு நிறைவேற்றப்பட்டு ஏற்றுக்கொள்ளப்பட்டது"],
    "A-2, B-4, C-1, D-3", "A-1, B-3, C-4, D-2", "A-2, B-1, C-4, D-3", "A-4, B-2, C-1, D-3",
    "A",
    "A-2: Aug 29, 1947 was setting up of Drafting Committee. B-4: Nov 26, 1949 was passing and adoption of Constitution. C-1: Jan 24, 1950 was final session, signing, and adoption of Anthem/Song. D-3: Jan 26, 1950 was Commencement/Enforcement.",
    "A-2: ஆகஸ்ட் 29, 1947 வரைவுக் குழு அமைப்பு. B-4: நவம்பர் 26, 1949 அரசியலமைப்பு ஏற்பு. C-1: ஜனவரி 24, 1950 இறுதி அமர்வு & தேசிய கீதம்/பாடல் ஏற்பு. D-3: ஜனவரி 26, 1950 நடைமுறைக்கு வந்தது.",
    "Correct. A-2, B-4, C-1, D-3 is the exact correct matching.", "சரி. A-2, B-4, C-1, D-3 சரியான பொருத்தம்.",
    "Incorrect. Aug 29 was setting up Drafting Committee (2), not final session (1).", "தவறு. ஆகஸ்ட் 29 வரைவுக் குழு அமைப்பு (2).",
    "Incorrect. Nov 26 was adoption of Constitution (4), not final session (1).", "தவறு. நவம்பர் 26 அரசியலமைப்பு ஏற்பு (4).",
    "Incorrect. Aug 29 was setting up Drafting Committee (2), not adoption of Constitution (4).", "தவறு. ஆகஸ்ட் 29 வரைவுக் குழு அமைப்பு (2).",
    "TNPSC Trap: Date of Adoption = Nov 26, 1949. Date of Commencement = Jan 26, 1950. Final Session = Jan 24, 1950.",
    "TNPSC பொறி: ஏற்றுக்கொள்ளப்பட்ட நாள் = நவம்பர் 26, 1949. நடைமுறைக்கு வந்த நாள் = ஜனவரி 26, 1950. இறுதி அமர்வு = ஜனவரி 24, 1950.",
    "Drafting Committee was set up exactly two weeks after India attained independence.",
    "இந்தியா சுதந்திரமடைந்த சரியாக இரண்டு வாரங்களுக்குப் பிறகு வரைவுக் குழு அமைக்கப்பட்டது.",
    "Analyze", 75, ["Polity", "Making of Indian Constitution", "Constitutional Milestones", "Important Dates", "Drafting Committee"]
))

# MIC_MF_007
questions.append(make_mf_q(
    "MIC_MF_007", "Match the Following",
    "Match List I (Sub-Committee of Advisory Committee) with List II (Chairman) and select the correct answer using the codes given below:\n\nList I\nA. Fundamental Rights Sub-Committee\nB. Minorities Sub-Committee\nC. North-East Frontier Tribal Areas Sub-Committee\nD. Excluded and Partially Excluded Areas (Other than Assam) Sub-Committee\n\nList II\n1. H.C. Mookherjee\n2. A.V. Thakkar\n3. J.B. Kripalani\n4. Gopinath Bordoloi",
    "பட்டியல் I-ஐ (ஆலோசனைக் குழுவின் துணைக் குழு) பட்டியல் II உடன் (தலைவர்) பொருத்தி கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான பதிலதைத் தேர்ந்தெடுக்கவும்:\n\nபட்டியல் I\nA. அடிப்படை உரிமைகள் துணைக் குழு\nB. சிறுபான்மையினர் துணைக் குழு\nC. வடகிழக்கு எல்லைப் பழங்குடியினர் பகுதி துணைக் குழு\nD. விலக்கப்பட்ட மற்றும் பகுதி விலக்கப்பட்ட பகுதிகள் (அசாம் தவிர) துணைக் குழு\n\nபட்டியல் II\n1. எச்.சி. முகர்ஜி\n2. ஏ.வி. தாக்கர்\n3. ஜெ.பி. கிருபளானி\n4. கோபிநாத் பர்தோலோய்",
    ["Fundamental Rights Sub-Committee", "Minorities Sub-Committee", "North-East Frontier Tribal Areas Sub-Committee", "Excluded and Partially Excluded Areas (Other than Assam) Sub-Committee"],
    ["அடிப்படை உரிமைகள் துணைக் குழு", "சிறுபான்மையினர் துணைக் குழு", "வடகிழக்கு எல்லைப் பழங்குடியினர் பகுதி துணைக் குழு", "விலக்கப்பட்ட மற்றும் பகுதி விலக்கப்பட்ட பகுதிகள் (அசாம் தவிர) துணைக் குழு"],
    ["H.C. Mookherjee", "A.V. Thakkar", "J.B. Kripalani", "Gopinath Bordoloi"],
    ["எச்.சி. முகர்ஜி", "ஏ.வி. தாக்கர்", "ஜெ.பி. கிருபளானி", "கோபிநாத் பர்தோலோய்"],
    "A-3, B-1, C-4, D-2", "A-1, B-3, C-2, D-4", "A-3, B-4, C-1, D-2", "A-2, B-1, C-4, D-3",
    "A",
    "A-3: Fundamental Rights Sub-Committee was chaired by J.B. Kripalani. B-1: Minorities Sub-Committee was chaired by H.C. Mookherjee. C-4: North-East Frontier Tribal Sub-Committee was chaired by Gopinath Bordoloi. D-2: Excluded Areas Sub-Committee was chaired by A.V. Thakkar.",
    "A-3: அடிப்படை உரிமைகள் துணைக் குழுத் தலைவர் ஜெ.பி. கிருபளானி. B-1: சிறுபான்மையினர் துணைக் குழுத் தலைவர் எச்.சி. முகர்ஜி. C-4: வடகிழக்கு பழங்குடியினர் துணைக் குழுத் தலைவர் கோபிநாத் பர்தோலோய். D-2: பிற விலக்கப்பட்ட பகுதிகள் குழுத் தலைவர் ஏ.வி. தாக்கர்.",
    "Correct. A-3, B-1, C-4, D-2 is the exact correct matching.", "சரி. A-3, B-1, C-4, D-2 சரியான பொருத்தம்.",
    "Incorrect. Kripalani chaired Fundamental Rights Sub-Committee (3), not Minorities (1).", "தவறு. கிருபளானி அடிப்படை உரிமைகள் துணைக் குழுத் தலைவர் (3).",
    "Incorrect. Bordoloi chaired North-East Tribal Sub-Committee (4), not Minorities (1).", "தவறு. பர்தோலோய் வடகிழக்கு பழங்குடியினர் துணைக் குழுத் தலைவர் (4).",
    "Incorrect. Thakkar chaired Excluded Areas Sub-Committee (2), not Fundamental Rights (3).", "தவறு. தாக்கர் பிற விலக்கப்பட்ட பகுதிகள் குழுத் தலைவர் (2).",
    "TNPSC Trap: Fundamental Rights Sub-Committee Chair = J.B. Kripalani. Main Advisory Committee Chair = Sardar Vallabhbhai Patel.",
    "TNPSC பொறி: அடிப்படை உரிமைகள் துணைக் குழுத் தலைவர் = ஜெ.பி. கிருபளானி. முதன்மை ஆலோசனைக் குழுத் தலைவர் = சர்தார் வல்லபாய் படேல்.",
    "A.V. Thakkar (Thakkar Bapa) was a pioneering social worker who worked extensively for tribal welfare.",
    "ஏ.வி. தாக்கர் (தாக்கர் பாப்பா) பழங்குடியினர் நலனுக்காகப் பணியாற்றிய ஒரு முன்னோடி சமூகப் பணியாளர் ஆவார்.",
    "Analyze", 75, ["Polity", "Making of Indian Constitution", "Advisory Committee", "Important Committees"]
))

# MIC_MF_008
questions.append(make_mf_q(
    "MIC_MF_008", "Match the Following",
    "Match List I (Cabinet Mission Plan Allocation Category) with List II (Exact Number of Seats / Ratio) and select the correct answer using the codes given below:\n\nList I\nA. Total Assembly Strength\nB. British Indian Governor's Provinces\nC. Chief Commissioners' Provinces\nD. Population Representation Ratio\n\nList II\n1. 4 Seats (Delhi, Ajmer-Merwara, Coorg, Baluchistan)\n2. 1 Seat for every 1 Million (10 Lakh) population\n3. 292 Seats\n4. 389 Seats",
    "பட்டியல் I-ஐ (கேபினட் தூதுக்குழு ஒதுக்கீட்டுப் பிரிவு) பட்டியல் II உடன் (துல்லியமான இடங்களின் எண்ணிக்கை / விகிதம்) பொருத்தி கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான பதிலதைத் தேர்ந்தெடுக்கவும்:\n\nபட்டியல் I\nA. அவையின் மொத்த உறுப்பினர்கள் எண்ணிக்கை\nB. பிரிட்டிஷ் இந்திய கவர்னர் மாகாணங்கள்\nC. தலைமை ஆணையர் மாகாணங்கள்\nD. மக்கள் தொகை பிரதிநிதித்துவ விகிதம்\n\nபட்டியல் II\n1. 4 இடங்கள் (டெல்லி, அஜ்மீர்-மேர்வாரா, கூர்க், பலுசிஸ்தான்)\n2. 10 லட்சம் (1 மில்லியன்) மக்கள் தொகைக்கு 1 இடம்\n3. 292 இடங்கள்\n4. 389 இடங்கள்",
    ["Total Assembly Strength", "British Indian Governor's Provinces", "Chief Commissioners' Provinces", "Population Representation Ratio"],
    ["அவையின் மொத்த உறுப்பினர்கள் எண்ணிக்கை", "பிரிட்டிஷ் இந்திய கவர்னர் மாகாணங்கள்", "தலைமை ஆணையர் மாகாணங்கள்", "மக்கள் தொகை பிரதிநிதித்துவ விகிதம்"],
    ["4 Seats (Delhi, Ajmer-Merwara, Coorg, Baluchistan)", "1 Seat for every 1 Million (10 Lakh) population", "292 Seats", "389 Seats"],
    ["4 இடங்கள் (டெல்லி, அஜ்மீர்-மேர்வாரா, கூர்க், பலுசிஸ்தான்)", "10 லட்சம் (1 மில்லியன்) மக்கள் தொகைக்கு 1 இடம்", "292 இடங்கள்", "389 இடங்கள்"],
    "A-4, B-3, C-1, D-2", "A-3, B-4, C-2, D-1", "A-4, B-1, C-3, D-2", "A-2, B-3, C-1, D-4",
    "A",
    "A-4: Total Assembly strength was 389. B-3: Governor's provinces were allocated 292 seats. C-1: Chief Commissioners' provinces got 4 seats. D-2: Population ratio was 1 seat per 1 million population.",
    "A-4: அவையின் மொத்த எண்ணிக்கை 389. B-3: கவர்னர் மாகாணங்கள் 292 இடங்கள். C-1: தலைமை ஆணையர் மாகாணங்கள் 4 இடங்கள். D-2: மக்கள் தொகை விகிதம் 10 லட்சத்திற்கு 1 இடம்.",
    "Correct. A-4, B-3, C-1, D-2 is the exact correct matching.", "சரி. A-4, B-3, C-1, D-2 சரியான பொருத்தம்.",
    "Incorrect. Total Assembly strength was 389 (4), not 292 (3).", "தவறு. அவையின் மொத்த எண்ணிக்கை 389 (4).",
    "Incorrect. Chief Commissioners got 4 seats (1), not 292 (3).", "தவறு. தலைமை ஆணையர் மாகாணங்கள் 4 இடங்கள் (1).",
    "Incorrect. Total Assembly strength was 389 (4), not ratio (2).", "தவறு. அவையின் மொத்த எண்ணிக்கை 389 (4).",
    "TNPSC Trap: Total British India seats = 296 (292 Governor's Provinces + 4 Chief Commissioners' Provinces). Princely States = 93.",
    "TNPSC பொறி: பிரிட்டிஷ் இந்தியாவின் மொத்த இடங்கள் = 296 (292 கவர்னர் மாகாணங்கள் + 4 தலைமை ஆணையர் மாகாணங்கள்). சமஸ்தானங்கள் = 93.",
    "The 4 Chief Commissioners' Provinces were Delhi, Ajmer-Merwara, Coorg, and British Baluchistan.",
    "4 தலைமை ஆணையர் மாகாணங்கள்: டெல்லி, அஜ்மீர்-மேர்வாரா, கூர்க் மற்றும் பிரிட்டிஷ் பலுசிஸ்தான்.",
    "Analyze", 75, ["Polity", "Making of Indian Constitution", "Cabinet Mission Plan", "Composition"]
))
