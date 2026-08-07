from mic_mf_part1 import make_mf_q

questions = []

# MIC_MF_009
questions.append(make_mf_q(
    "MIC_MF_009", "Match the Following",
    "Match List I (Prominent Woman Member of Constituent Assembly) with List II (Key Distinction / Contribution) and select the correct answer using the codes given below:\n\nList I\nA. Begum Aizaz Rasul\nB. Dakshayani Velayudhan\nC. Hansa Mehta\nD. Rajkumari Amrit Kaur\n\nList II\n1. Presented the National Flag to the Assembly on behalf of the women of India\n2. Only Muslim woman member in the Constituent Assembly\n3. Served on Fundamental Rights Sub-Committee & became 1st Health Minister of India\n4. Only Dalit (Scheduled Caste) woman member in the Constituent Assembly",
    "பட்டியல் I-ஐ (அரசியலமைப்பு அவையின் முக்கிய பெண் உறுப்பினர்) பட்டியல் II உடன் (முக்கிய சிறப்பம்சம் / பங்களிப்பு) பொருத்தி கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான பதிலதைத் தேர்ந்தெடுக்கவும்:\n\nபட்டியல் I\nA. பேகம் ஐசாஸ் ரசூல்\nB. தாக்ஷாயணி வேலாயுதன்\nC. ஹன்சா மேத்தா\nD. ராஜ்குமாரி அம்ரித் கவுர்\n\nபட்டியல் II\n1. இந்தியப் பெண்களின் சார்பில் தேசியக் கொடியை அவைக்கு வழங்கினார்\n2. அரசியலமைப்பு நிர்ணய அவையில் இருந்த ஒரே முஸ்லிம் பெண் உறுப்பினர்\n3. அடிப்படை உரிமைகள் துணைக் குழுவில் பணியாற்றி இந்தியாவின் 1வது சுகாதார அமைச்சரானார்\n4. அரசியலமைப்பு நிர்ணய அவையில் இருந்த ஒரே தலித் (பட்டியலின) பெண் உறுப்பினர்",
    ["Begum Aizaz Rasul", "Dakshayani Velayudhan", "Hansa Mehta", "Rajkumari Amrit Kaur"],
    ["பேகம் ஐசாஸ் ரசூல்", "தாக்ஷாயணி வேலாயுதன்", "ஹன்சா மேத்தா", "ராஜ்குமாரி அம்ரித் கவுர்"],
    ["Presented the National Flag to the Assembly on behalf of the women of India", "Only Muslim woman member in the Constituent Assembly", "Served on Fundamental Rights Sub-Committee & became 1st Health Minister of India", "Only Dalit (Scheduled Caste) woman member in the Constituent Assembly"],
    ["இந்தியப் பெண்களின் சார்பில் தேசியக் கொடியை அவைக்கு வழங்கினார்", "அரசியலமைப்பு நிர்ணய அவையில் இருந்த ஒரே முஸ்லிம் பெண் உறுப்பினர்", "அடிப்படை உரிமைகள் துணைக் குழுவில் பணியாற்றி இந்தியாவின் 1வது சுகாதார அமைச்சரானார்", "அரசியலமைப்பு நிர்ணய அவையில் இருந்த ஒரே தலித் (பட்டியலின) பெண் உறுப்பினர்"],
    "A-2, B-4, C-1, D-3", "A-4, B-2, C-1, D-3", "A-2, B-1, C-4, D-3", "A-3, B-4, C-2, D-1",
    "A",
    "A-2: Begum Aizaz Rasul was the only Muslim woman member. B-4: Dakshayani Velayudhan was the only Dalit woman member. C-1: Hansa Mehta presented the National Flag on behalf of women. D-3: Rajkumari Amrit Kaur served on FR Sub-Committee & became 1st Health Minister.",
    "A-2: பேகம் ஐசாஸ் ரசூல் ஒரே முஸ்லிம் பெண் உறுப்பினர். B-4: தாக்ஷாயணி வேலாயுதன் ஒரே தலித் பெண் உறுப்பினர். C-1: ஹன்சா மேத்தா பெண்கள் சார்பில் தேசியக் கொடியை வழங்கினார். D-3: ராஜ்குமாரி அம்ரித் கவுர் 1வது சுகாதார அமைச்சர்.",
    "Correct. A-2, B-4, C-1, D-3 is the exact correct matching.", "சரி. A-2, B-4, C-1, D-3 சரியான பொருத்தம்.",
    "Incorrect. Begum Aizaz Rasul was the only Muslim woman member (2), not Dalit member (4).", "தவறு. பேகம் ஐசாஸ் ரசூல் ஒரே முஸ்லிம் பெண் உறுப்பினர் (2).",
    "Incorrect. Dakshayani Velayudhan was sole Dalit member (4), not flag presenter (1).", "தவறு. தாக்ஷாயணி வேலாயுதன் ஒரே தலித் பெண் உறுப்பினர் (4).",
    "Incorrect. Begum Aizaz Rasul was sole Muslim woman member (2), not Health Minister (3).", "தவறு. பேகம் ஐசாஸ் ரசூல் ஒரே முஸ்லிம் பெண் உறுப்பினர் (2).",
    "TNPSC Trap: Only Muslim woman member = Begum Aizaz Rasul. Only Dalit woman member = Dakshayani Velayudhan (representing Madras).",
    "TNPSC பொறி: ஒரே முஸ்லிம் பெண் உறுப்பினர் = பேகம் ஐசாஸ் ரசூல். ஒரே தலித் பெண் உறுப்பினர் = தாக்ஷாயணி வேலாயுதன் (மெட்ராஸ் பிரதிநிதி).",
    "There were a total of 15 women members in the Constituent Assembly.",
    "அரசியலமைப்பு நிர்ணய அவையில் மொத்தம் 15 பெண் உறுப்பினர்கள் இருந்தனர்.",
    "Analyze", 75, ["Polity", "Making of Indian Constitution", "Women's Representation", "Important Personalities"]
))

# MIC_MF_010
questions.append(make_mf_q(
    "MIC_MF_010", "Match the Following",
    "Match List I (Calligrapher / Artist) with List II (Specific Artistic Contribution to the Constitution) and select the correct answer using the codes given below:\n\nList I\nA. Prem Behari Narain Raizada\nB. Vasant Krishnan Vaidya\nC. Nandalal Bose\nD. Beohar Rammanohar Sinha\n\nList II\n1. Calligraphed the original Constitution in Hindi\n2. Illuminated and decorated the original Preamble page\n3. Calligraphed the original Constitution in English in flowing italic style\n4. Led the team of Shantiniketan artists who decorated and illuminated all manuscript pages",
    "பட்டியல் I-ஐ (கையெழுத்துக் கலைஞர் / ஓவியர்) பட்டியல் II உடன் (அரசியலமைப்புக்கான கலைப் பங்களிப்பு) பொருத்தி கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான பதிலதைத் தேர்ந்தெடுக்கவும்:\n\nபட்டியல் I\nA. பிரேம் பிஹாரி நரேன் ரைசாதா\nB. வசந்த் கிருஷ்ண வைத்யா\nC. நந்தலால் போஸ்\nD. பியோஹர் ராம்மனோஹர் சின்ஹா\n\nபட்டியல் II\n1. இந்தியில் அசல் அரசியலமைப்பை கையால் எழுதினார்\n2. அசல் முகப்புரைப் பக்கத்தை அலங்கரித்து ஒளிவூட்டினார்\n3. ஆங்கிலத்தில் அசல் அரசியலமைப்பை சாய்ந்த எழுத்து வடிவில் கையால் எழுதினார்\n4. கையெழுத்துப் பிரதியின் அனைத்து பக்கங்களையும் அலங்கரித்த சாந்திநிகேதன் கலைஞர்கள் குழுவிற்கு தலைமை தாங்கினார்",
    ["Prem Behari Narain Raizada", "Vasant Krishnan Vaidya", "Nandalal Bose", "Beohar Rammanohar Sinha"],
    ["பிரேம் பிஹாரி நரேன் ரைசாதா", "வசந்த் கிருஷ்ண வைத்யா", "நந்தலால் போஸ்", "பியோஹர் ராம்மனோஹர் சின்ஹா"],
    ["Calligraphed the original Constitution in Hindi", "Illuminated and decorated the original Preamble page", "Calligraphed the original Constitution in English in flowing italic style", "Led the team of Shantiniketan artists who decorated and illuminated all manuscript pages"],
    ["இந்தியில் அசல் அரசியலமைப்பை கையால் எழுதினார்", "அசல் முகப்புரைப் பக்கத்தை அலங்கரித்து ஒளிவூட்டினார்", "ஆங்கிலத்தில் அசல் அரசியலமைப்பை சாய்ந்த எழுத்து வடிவில் கையால் எழுதினார்", "கையெழுத்துப் பிரதியின் அனைத்து பக்கங்களையும் அலங்கரித்த சாந்திநிகேதன் கலைஞர்கள் குழுவிற்கு தலைமை தாங்கினார்"],
    "A-3, B-1, C-4, D-2", "A-1, B-3, C-2, D-4", "A-3, B-4, C-1, D-2", "A-2, B-1, C-4, D-3",
    "A",
    "A-3: Prem Behari Narain Raizada calligraphed the original English version. B-1: Vasant Krishnan Vaidya calligraphed the Hindi version. C-4: Nandalal Bose led the Shantiniketan team of artists. D-2: Beohar Rammanohar Sinha decorated the Preamble page.",
    "A-3: பிரேம் பிஹாரி நரேன் ரைசாதா ஆங்கிலப் பிரதியை எழுதினார். B-1: வசந்த் கிருஷ்ண வைத்யா இந்திப் பிரதியை எழுதினார். C-4: நந்தலால் போஸ் சாந்திநிகேதன் ஓவியர் குழுத் தலைவர். D-2: பியோஹர் ராம்மனோஹர் சின்ஹா முகப்புரையை வரைந்தார்.",
    "Correct. A-3, B-1, C-4, D-2 is the exact correct matching.", "சரி. A-3, B-1, C-4, D-2 சரியான பொருத்தம்.",
    "Incorrect. Raizada calligraphed English version (3), not Hindi version (1).", "தவறு. ரைசாதா ஆங்கிலப் பிரதியை எழுதினார் (3).",
    "Incorrect. Nandalal Bose led Shantiniketan team (4), not Hindi calligrapher (1).", "தவறு. நந்தலால் போஸ் ஓவியர் குழுத் தலைவர் (4).",
    "Incorrect. Raizada calligraphed English version (3), not Preamble decorator (2).", "தவறு. ரைசாதா ஆங்கிலப் பிரதியை எழுதினார் (3).",
    "TNPSC Trap: English Calligrapher = Prem Behari Narain Raizada. Hindi Calligrapher = Vasant Krishnan Vaidya. Preamble Page Artist = Beohar Rammanohar Sinha.",
    "TNPSC பொறி: ஆங்கிலக் கையெழுத்து = பிரேம் பிஹாரி நரேன் ரைசாதா. இந்திக் கையெழுத்து = வசந்த் கிருஷ்ண வைத்யா. முகப்புரை ஓவியர் = பியோஹர் ராம்மனோஹர் சின்ஹா.",
    "Prem Behari Narain Raizada wrote the entire Constitution in 6 months using 432 pen nibs.",
    "பிரேம் பிஹாரி நரேன் ரைசாதா 432 பேனா நிப்களைப் பயன்படுத்தி 6 மாதங்களில் முழு அரசியலமைப்பையும் எழுதினார்.",
    "Analyze", 75, ["Polity", "Making of Indian Constitution", "Handwritten Constitution", "Calligraphy", "Decoration of Constitution"]
))

# MIC_MF_011
questions.append(make_mf_q(
    "MIC_MF_011", "Match the Following",
    "Match List I (Minor Committee of Constituent Assembly) with List II (Chairman) and select the correct answer using the codes given below:\n\nList I\nA. Finance and Staff Committee\nB. House Committee\nC. Credentials Committee\nD. Order of Business Committee\n\nList II\n1. Dr. K.M. Munshi\n2. Alladi Krishnaswamy Ayyar\n3. B. Pattabhi Sitaramayya\n4. Dr. Rajendra Prasad",
    "பட்டியல் I-ஐ (அரசியலமைப்பு அவையின் சிறு குழுக்கள்) பட்டியல் II உடன் (தலைவர்) பொருத்தி கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான பதிலதைத் தேர்ந்தெடுக்கவும்:\n\nபட்டியல் I\nA. நிதி மற்றும் பணியாளர் குழு\nB. அவைக் குழு\nC. தகுதிகள் குழு\nD. வணிக வரிசைக் குழு\n\nபட்டியல் II\n1. டாக்டர் கே.எம். முன்ஷி\n2. அல்லாடி கிருஷ்ணசாமி அய்யர்\n3. பி. பட்டாபி சீதாராமையா\n4. டாக்டர் ராஜேந்திர பிரசாத்",
    ["Finance and Staff Committee", "House Committee", "Credentials Committee", "Order of Business Committee"],
    ["நிதி மற்றும் பணியாளர் குழு", "அவைக் குழு", "தகுதிகள் குழு", "வணிக வரிசைக் குழு"],
    ["Dr. K.M. Munshi", "Alladi Krishnaswamy Ayyar", "B. Pattabhi Sitaramayya", "Dr. Rajendra Prasad"],
    ["டாக்டர் கே.எம். முன்ஷி", "அல்லாடி கிருஷ்ணசாமி அய்யர்", "பி. பட்டாபி சீதாராமையா", "டாக்டர் ராஜேந்திர பிரசாத்"],
    "A-4, B-3, C-2, D-1", "A-3, B-4, C-1, D-2", "A-4, B-1, C-2, D-3", "A-2, B-3, C-4, D-1",
    "A",
    "A-4: Finance and Staff Committee was chaired by Dr. Rajendra Prasad. B-3: House Committee was chaired by B. Pattabhi Sitaramayya. C-2: Credentials Committee was chaired by Alladi Krishnaswamy Ayyar. D-1: Order of Business Committee was chaired by Dr. K.M. Munshi.",
    "A-4: நிதி மற்றும் பணியாளர் குழுத் தலைவர் டாக்டர் ராஜேந்திர பிரசாத். B-3: அவைக் குழுத் தலைவர் பி. பட்டாபி சீதாராமையா. C-2: தகுதிகள் குழுத் தலைவர் அல்லாடி கிருஷ்ணசாமி அய்யர். D-1: வணிக வரிசைக் குழுத் தலைவர் டாக்டர் கே.எம். முன்ஷி.",
    "Correct. A-4, B-3, C-2, D-1 is the exact correct matching.", "சரி. A-4, B-3, C-2, D-1 சரியான பொருத்தம்.",
    "Incorrect. Rajendra Prasad chaired Finance and Staff Committee (4), not Pattabhi Sitaramayya (3).", "தவறு. ராஜேந்திர பிரசாத் நிதி மற்றும் பணியாளர் குழுத் தலைவர் (4).",
    "Incorrect. Pattabhi Sitaramayya chaired House Committee (3), not Dr. K.M. Munshi (1).", "தவறு. பட்டாபி சீதாராமையா அவைக் குழுத் தலைவர் (3).",
    "Incorrect. Rajendra Prasad chaired Finance and Staff Committee (4), not Alladi (2).", "தவறு. ராஜேந்திர பிரசாத் நிதி மற்றும் பணியாளர் குழுத் தலைவர் (4).",
    "TNPSC Trap: Credentials Committee Chair = Alladi Krishnaswamy Ayyar. House Committee Chair = B. Pattabhi Sitaramayya.",
    "TNPSC பொறி: தகுதிகள் குழுத் தலைவர் = அல்லாடி கிருஷ்ணசாமி அய்யர். அவைக் குழுத் தலைவர் = பி. பட்டாபி சீதாராமையா.",
    "Dr. Rajendra Prasad chaired two minor committees: Finance and Staff Committee, and Ad hoc Committee on National Flag.",
    "டாக்டர் ராஜேந்திர பிரசாத் இரண்டு சிறு குழுக்களுக்குத் தலைமை தாங்கினார்: நிதி-பணியாளர் குழு மற்றும் தேசியக் கொடிக்கான தற்காலிகக் குழு.",
    "Analyze", 75, ["Polity", "Making of Indian Constitution", "Important Committees"]
))

# MIC_MF_012
questions.append(make_mf_q(
    "MIC_MF_012", "Match the Following",
    "Match List I (Original Member / Key Position) with List II (Replacement Member / Official Symbol) and select the correct answer using the codes given below:\n\nList I\nA. B.L. Mitter (resigned due to ill-health)\nB. D.P. Khaitan (died in 1948)\nC. H.V.R. Iengar\nD. Official Emblem of Constituent Assembly\n\nList II\n1. Secretary to the Constituent Assembly\n2. Replaced by N. Madhava Rau\n3. Elephant\n4. Replaced by T.T. Krishnamachari",
    "பட்டியல் I-ஐ (அசல் உறுப்பினர் / முக்கியப் பதவி) பட்டியல் II உடன் (மாற்று உறுப்பினர் / அதிகாரப்பூர்வ சின்னம்) பொருத்தி கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான பதிலதைத் தேர்ந்தெடுக்கவும்:\n\nபட்டியல் I\nA. பி.எல். மிட்டர் (உடல்நலக்குறைவால் விலகினார்)\nB. டி.பி. கைத்தான் (1948 இல் காலமானார்)\nC. எச்.வி.ஆர். ஐயங்கார்\nD. அரசியலமைப்பு அவையின் அதிகாரப்பூர்வ சின்னம்\n\nபட்டியல் II\n1. அரசியலமைப்பு அவையின் செயலாளர்\n2. என். மாதவ ராவ் என்பவரால் மாற்றப்பட்டார்\n3. யானை\n4. டி.டி. கிருஷ்ணமாச்சாரி என்பவரால் மாற்றப்பட்டார்",
    ["B.L. Mitter (resigned due to ill-health)", "D.P. Khaitan (died in 1948)", "H.V.R. Iengar", "Official Emblem of Constituent Assembly"],
    ["பி.எல். மிட்டர் (உடல்நலக்குறைவால் விலகினார்)", "டி.பி. கைத்தான் (1948 இல் காலமானார்)", "எச்.வி.ஆர். ஐயங்கார்", "அரசியலமைப்பு அவையின் அதிகாரப்பூர்வ சின்னம்"],
    ["Secretary to the Constituent Assembly", "Replaced by N. Madhava Rau", "Elephant", "Replaced by T.T. Krishnamachari"],
    ["அரசியலமைப்பு அவையின் செயலாளர்", "என். மாதவ ராவ் என்பவரால் மாற்றப்பட்டார்", "யானை", "டி.டி. கிருஷ்ணமாச்சாரி என்பவரால் மாற்றப்பட்டார்"],
    "A-2, B-4, C-1, D-3", "A-4, B-2, C-1, D-3", "A-2, B-1, C-4, D-3", "A-3, B-4, C-2, D-1",
    "A",
    "A-2: B.L. Mitter was replaced by N. Madhava Rau. B-4: D.P. Khaitan died in 1948 and was replaced by T.T. Krishnamachari. C-1: H.V.R. Iengar was Secretary to CA. D-3: Official Emblem of CA was the Elephant.",
    "A-2: பி.எல். மிட்டருக்குப் பதிலாக என். மாதவ ராவ் சேர்ந்தார். B-4: டி.பி. கைத்தானுக்குப் பதிலாக டி.டி. கிருஷ்ணமாச்சாரி சேர்ந்தார். C-1: எச்.வி.ஆர். ஐயங்கார் அவைச் செயலாளர். D-3: அதிகாரப்பூர்வ சின்னம் யானை.",
    "Correct. A-2, B-4, C-1, D-3 is the exact correct matching.", "சரி. A-2, B-4, C-1, D-3 சரியான பொருத்தம்.",
    "Incorrect. B.L. Mitter was replaced by N. Madhava Rau (2), not T.T. Krishnamachari (4).", "தவறு. மிட்டருக்குப் பதிலாக மாதவ ராவ் (2).",
    "Incorrect. H.V.R. Iengar was Secretary (1), not replaced by T.T. Krishnamachari (4).", "தவறு. ஐயங்கார் அவைச் செயலாளர் (1).",
    "Incorrect. Emblem of CA was Elephant (3), not Secretary (1).", "தவறு. அவையின் சின்னம் யானை (3).",
    "TNPSC Trap: B.L. Mitter -> N. Madhava Rau. D.P. Khaitan -> T.T. Krishnamachari. Assembly Seal = Elephant.",
    "TNPSC பொறி: பி.எல். மிட்டர் -> என். மாதவ ராவ். டி.பி. கைத்தான் -> டி.டி. கிருஷ்ணமாச்சாரி. அவையின் முத்திரை = யானை.",
    "T.T. Krishnamachari was also a member of the drafting committee representing Madras.",
    "டி.டி. கிருஷ்ணமாச்சாரி மெட்ராஸைப் பிரதிநிதித்துவப்படுத்திய வரைவுக் குழு உறுப்பினருமாவார்.",
    "Analyze", 75, ["Polity", "Making of Indian Constitution", "Drafting Committee", "T. T. Krishnamachari", "Constitutional Facts"]
))

# MIC_MF_013
questions.append(make_mf_q(
    "MIC_MF_013", "Match the Following",
    "Match List I (Historical Date) with List II (Enactment / Specific Provision Enforced) and select the correct answer using the codes given below:\n\nList I\nA. May 1949\nB. July 22, 1947\nC. November 26, 1949\nD. January 26, 1930\n\nList II\n1. Official adoption of the National Flag of India\n2. Celebration of Poorna Swaraj Day following Lahore INC Session\n3. Ratification of India's membership of the Commonwealth\n4. Enforcement of Citizenship (Articles 5-9) and Elections (Article 324)",
    "பட்டியல் I-ஐ (வரலாற்றுத் தேதி) பட்டியல் II உடன் (இயற்றல் / நடைமுறைப்படுத்தப்பட்ட குறிப்பிட்ட விதி) பொருத்தி கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான பதிலதைத் தேர்ந்தெடுக்கவும்:\n\nபட்டியல் I\nA. மே 1949\nB. ஜூலை 22, 1947\nC. நவம்பர் 26, 1949\nD. ஜனவரி 26, 1930\n\nபட்டியல் II\n1. இந்திய தேசியக் கொடி அதிகாரப்பூர்வமாக ஏற்றுக்கொள்ளப்பட்டது\n2. லாகூர் காங்கிரஸ் மாநாட்டைத் தொடர்ந்து பூரண சுயராஜ்ய தினம் கொண்டாடப்பட்டது\n3. காமன்வெல்த்தில் இந்தியாவின் உறுப்பினருரிமை உறுதிப்படுத்தப்பட்டது\n4. குடியுரிமை (சரத்துகள் 5-9) மற்றும் தேர்தல்கள் (சரத்து 324) நடைமுறைக்கு வந்தன",
    ["May 1949", "July 22, 1947", "November 26, 1949", "January 26, 1930"],
    ["மே 1949", "ஜூலை 22, 1947", "நவம்பர் 26, 1949", "ஜனவரி 26, 1930"],
    ["Official adoption of the National Flag of India", "Celebration of Poorna Swaraj Day following Lahore INC Session", "Ratification of India's membership of the Commonwealth", "Enforcement of Citizenship (Articles 5-9) and Elections (Article 324)"],
    ["இந்திய தேசியக் கொடி அதிகாரப்பூர்வமாக ஏற்றுக்கொள்ளப்பட்டது", "லாகூர் காங்கிரஸ் மாநாட்டைத் தொடர்ந்து பூரண சுயராஜ்ய தினம் கொண்டாடப்பட்டது", "காமன்வெல்த்தில் இந்தியாவின் உறுப்பினருரிமை உறுதிப்படுத்தப்பட்டது", "குடியுரிமை (சரத்துகள் 5-9) மற்றும் தேர்தல்கள் (சரத்து 324) நடைமுறைக்கு வந்தன"],
    "A-3, B-1, C-4, D-2", "A-1, B-3, C-2, D-4", "A-3, B-4, C-1, D-2", "A-2, B-1, C-4, D-3",
    "A",
    "A-3: May 1949 was ratification of India's membership of Commonwealth. B-1: July 22, 1947 was adoption of National Flag. C-4: Nov 26, 1949 was enforcement of Citizenship & Elections. D-2: Jan 26, 1930 was Poorna Swaraj Day.",
    "A-3: மே 1949 காமன்வெல்த் உறுப்பினர் பதிவு. B-1: ஜூலை 22, 1947 தேசியக் கொடி ஏற்பு. C-4: நவம்பர் 26, 1949 குடியுரிமை & தேர்தல் விதிகள் அமுல். D-2: ஜனவரி 26, 1930 பூரண சுயராஜ்ய தினம்.",
    "Correct. A-3, B-1, C-4, D-2 is the exact correct matching.", "சரி. A-3, B-1, C-4, D-2 சரியான பொருத்தம்.",
    "Incorrect. May 1949 was Commonwealth ratification (3), not Flag adoption (1).", "தவறு. மே 1949 காமன்வெல்த் உறுப்பினர் உறுதிப்பாடு (3).",
    "Incorrect. Nov 26, 1949 was enforcement of Citizenship/Elections (4), not Flag adoption (1).", "தவறு. நவம்பர் 26 குடியுரிமை/தேர்தல் நடைமுறை (4).",
    "Incorrect. May 1949 was Commonwealth ratification (3), not Poorna Swaraj (2).", "தவறு. மே 1949 காமன்வெல்த் உறுப்பினர் உறுதிப்பாடு (3).",
    "TNPSC Trap: India ratified Commonwealth membership in May 1949 while maintaining full republican sovereignty.",
    "TNPSC பொறி: இந்தியா முழு குடியரசு இறையாண்மையைப் பேணியபடியே மே 1949 இல் காமன்வெல்த் உறுப்பினருரிமையை உறுதிப்படுத்தியது.",
    "Poorna Swaraj resolution was passed under Jawaharlal Nehru's presidency at Lahore in Dec 1929.",
    "பூரண சுயராஜ்ய தீர்மானம் 1929 டிசம்பரில் லாகூரில் ஜவகர்லால் நேரு தலைமையில் நிறைவேற்றப்பட்டது.",
    "Analyze", 75, ["Polity", "Making of Indian Constitution", "Constitutional Milestones", "National Flag adoption", "Enforcement of Constitution"]
))

# MIC_MF_014
questions.append(make_mf_q(
    "MIC_MF_014", "Match the Following",
    "Match List I (National Symbol / Emblem) with List II (Specification / Composer) and select the correct answer using the codes given below:\n\nList I\nA. National Flag of India\nB. National Anthem ('Jana Gana Mana')\nC. National Song ('Vande Mataram')\nD. Seal of Constituent Assembly\n\nList II\n1. Composed in Sanskrit by Bankim Chandra Chatterjee\n2. Elephant\n3. Composed in Bengali by Rabindranath Tagore\n4. Tricolour with 24-spoke Ashoka Chakra in 3:2 ratio",
    "பட்டியல் I-ஐ (தேசிய சின்னங்கள்) பட்டியல் II உடன் (குறிப்பீடு / இயற்றியவர்) பொருத்தி கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான பதிலதைத் தேர்ந்தெடுக்கவும்:\n\nபட்டியல் I\nA. இந்திய தேசியக் கொடி\nB. தேசிய கீதம் ('ஜன கண மன')\nC. தேசியப் பாடல் ('வந்தே மாதரம்')\nD. அரசியலமைப்பு அவையின் முத்திரை\n\nபட்டியல் II\n1. பங்கிம் சந்திர சட்டர்ஜியால் சமஸ்கிருதத்தில் இயற்றப்பட்டது\n2. யானை\n3. ரவீந்திரநாத் தாகூரால் வங்காள மொழியில் இயற்றப்பட்டது\n4. 3:2 விகிதத்தில் 24 ஆரங்கள் கொண்ட அசோக சக்கரத்துடன் மூவர்ணக் கொடி",
    ["National Flag of India", "National Anthem ('Jana Gana Mana')", "National Song ('Vande Mataram')", "Seal of Constituent Assembly"],
    ["இந்திய தேசியக் கொடி", "தேசிய கீதம் ('ஜன கண மன')", "தேசியப் பாடல் ('வந்தே மாதரம்')", "அரசியலமைப்பு அவையின் முத்திரை"],
    ["Composed in Sanskrit by Bankim Chandra Chatterjee", "Elephant", "Composed in Bengali by Rabindranath Tagore", "Tricolour with 24-spoke Ashoka Chakra in 3:2 ratio"],
    ["பங்கிம் சந்திர சட்டர்ஜியால் சமஸ்கிருதத்தில் இயற்றப்பட்டது", "யானை", "ரவீந்திரநாத் தாகூரால் வங்காள மொழியில் இயற்றப்பட்டது", "3:2 விகிதத்தில் 24 ஆரங்கள் கொண்ட அசோக சக்கரத்துடன் மூவர்ணக் கொடி"],
    "A-4, B-3, C-1, D-2", "A-3, B-4, C-2, D-1", "A-4, B-1, C-3, D-2", "A-2, B-3, C-1, D-4",
    "A",
    "A-4: National Flag is tricolour with 24-spoke Chakra in 3:2 ratio. B-3: National Anthem was composed by Rabindranath Tagore. C-1: National Song was composed by Bankim Chandra Chatterjee. D-2: Assembly Seal was Elephant.",
    "A-4: தேசியக் கொடி 3:2 விகிதம், 24 ஆரங்கள். B-3: தேசிய கீதம் தாகூரால் இயற்றப்பட்டது. C-1: தேசியப் பாடல் பங்கிம் சந்திர சட்டர்ஜியால் இயற்றப்பட்டது. D-2: அவையின் முத்திரை யானை.",
    "Correct. A-4, B-3, C-1, D-2 is the exact correct matching.", "சரி. A-4, B-3, C-1, D-2 சரியான பொருத்தம்.",
    "Incorrect. National Flag is 3:2 tricolour (4), not composed by Tagore (3).", "தவறு. தேசியக் கொடி 3:2 மூவர்ணக் கொடி (4).",
    "Incorrect. National Anthem was composed by Tagore (3), not Bankim Chandra (1).", "தவறு. தேசிய கீதம் தாகூரால் இயற்றப்பட்டது (3).",
    "Incorrect. National Flag is 3:2 tricolour (4), not Elephant (2).", "தவறு. தேசியக் கொடி 3:2 மூவர்ணக் கொடி (4).",
    "TNPSC Trap: National Anthem & National Song were BOTH adopted on Jan 24, 1950. National Song 'Vande Mataram' has equal status with National Anthem.",
    "TNPSC பொறி: தேசிய கீதம் & தேசியப் பாடல் இரண்டும் ஜனவரி 24, 1950 அன்று ஏற்கப்பட்டன. தேசியப் பாடல் தேசிய கீதத்திற்கு இணையான தகுதியைக் கொண்டது.",
    "'Vande Mataram' was originally published in Bankim Chandra Chatterjee's novel 'Anandamath' in 1882.",
    "'வந்தே மாதரம்' முதன்முதலில் 1882 இல் பங்கிம் சந்திர சட்டர்ஜியின் 'ஆனந்தமடம்' நாவலில் வெளியானது.",
    "Analyze", 75, ["Polity", "Making of Indian Constitution", "National Flag adoption", "National Anthem adoption", "National Song"]
))

# MIC_MF_015
questions.append(make_mf_q(
    "MIC_MF_015", "Match the Following",
    "Match List I (Constituent Assembly Statistical Parameter) with List II (Exact Value / Number) and select the correct answer using the codes given below:\n\nList I\nA. Total time taken to frame the Constitution\nB. Total number of sessions held\nC. Total draft amendments proposed\nD. Total expenditure incurred\n\nList II\n1. 7,635 amendments (2,473 actually discussed)\n2. 2 Years, 11 Months, and 18 Days\n3. ₹64 Lakh Rupees\n4. 11 Sessions (covering 165 days of sittings)",
    "பட்டியல் I-ஐ (அரசியலமைப்பு அவையின் புள்ளிவிவர அளவுரு) பட்டியல் II உடன் (துல்லியமான மதிப்பு / எண்) பொருத்தி கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான பதிலதைத் தேர்ந்தெடுக்கவும்:\n\nபட்டியல் I\nA. அரசியலமைப்பை உருவாக்க எடுத்துக்கொண்ட மொத்த காலம்\nB. நடத்தப்பட்ட மொத்த அமர்வுகளின் எண்ணிக்கை\nC. முன்மொழியப்பட்ட மொத்த வரைவு திருத்தங்கள்\nD. ஏற்பட்ட மொத்த செலவு\n\nபட்டியல் II\n1. 7,635 திருத்தங்கள் (2,473 உண்மையில் விவாதிக்கப்பட்டவை)\n2. 2 ஆண்டுகள், 11 மாதங்கள் மற்றும் 18 நாட்கள்\n3. ₹64 லட்சம் ரூபாய்\n4. 11 அமர்வுகள் (165 நாட்கள் அமர்வுகளை உள்ளடக்கியது)",
    ["Total time taken to frame the Constitution", "Total number of sessions held", "Total draft amendments proposed", "Total expenditure incurred"],
    ["அரசியலமைப்பை உருவாக்க எடுத்துக்கொண்ட மொத்த காலம்", "நடத்தப்பட்ட மொத்த அமர்வுகளின் எண்ணிக்கை", "முன்மொழியப்பட்ட மொத்த வரைவு திருத்தங்கள்", "ஏற்பட்ட மொத்த செலவு"],
    ["7,635 amendments (2,473 actually discussed)", "2 Years, 11 Months, and 18 Days", "₹64 Lakh Rupees", "11 Sessions (covering 165 days of sittings)"],
    ["7,635 திருத்தங்கள் (2,473 உண்மையில் விவாதிக்கப்பட்டவை)", "2 ஆண்டுகள், 11 மாதங்கள் மற்றும் 18 நாட்கள்", "₹64 லட்சம் ரூபாய்", "11 அமர்வுகள் (165 நாட்கள் அமர்வுகளை உள்ளடக்கியது)"],
    "A-2, B-4, C-1, D-3", "A-4, B-2, C-1, D-3", "A-2, B-1, C-4, D-3", "A-3, B-4, C-2, D-1",
    "A",
    "A-2: Total time taken was 2 yrs 11 mos 18 days. B-4: Total sessions held was 11 (165 sitting days). C-1: Total amendments proposed was 7,635. D-3: Total expenditure was ₹64 lakh.",
    "A-2: மொத்த காலம் 2 ஆண்டுகள் 11 மாதங்கள் 18 நாட்கள். B-4: மொத்த அமர்வுகள் 11 (165 நாட்கள்). C-1: முன்மொழியப்பட்ட திருத்தங்கள் 7,635. D-3: மொத்த செலவு ₹64 லட்சம்.",
    "Correct. A-2, B-4, C-1, D-3 is the exact correct matching.", "சரி. A-2, B-4, C-1, D-3 சரியான பொருத்தம்.",
    "Incorrect. Total time taken was 2 yrs 11 mos 18 days (2), not 11 sessions (4).", "தவறு. மொத்த காலம் 2 ஆண்டுகள் 11 மாதங்கள் 18 நாட்கள் (2).",
    "Incorrect. Total sessions held was 11 (4), not amendments proposed (1).", "தவறு. மொத்த அமர்வுகள் 11 (4).",
    "Incorrect. Total time taken was 2 yrs 11 mos 18 days (2), not expenditure (3).", "தவறு. மொத்த காலம் 2 ஆண்டுகள் 11 மாதங்கள் 18 நாட்கள் (2).",
    "TNPSC Trap: Total time = 2 yrs 11 mos 18 days. Total sessions = 11. Total expenditure = ₹64 lakh.",
    "TNPSC பொறி: மொத்த காலம் = 2 ஆண்டுகள் 11 மாதங்கள் 18 நாட்கள். மொத்த அமர்வுகள் = 11. மொத்த செலவு = ₹64 லட்சம்.",
    "The Assembly scrutinized constitutions of about 60 countries.",
    "அரசியலமைப்பு அவை சுமார் 60 நாடுகளின் அரசியலமைப்புகளை ஆராய்ந்தது.",
    "Analyze", 75, ["Polity", "Making of Indian Constitution", "Interesting Constitutional Facts"]
))

# MIC_MF_016
questions.append(make_mf_q(
    "MIC_MF_016", "Match the Following",
    "Match List I (Critic / Scholar) with List II (Quotation / Critical Term) and select the correct answer using the codes given below:\n\nList I\nA. Dr. B.R. Ambedkar\nB. Granville Austin\nC. Naziruddin Ahmad\nD. Winston Churchill\n\nList II\n1. Described Assembly as 'a one-party body in an essentially one-party country'\n2. Remarked Assembly represented 'only one major community in India'\n3. Coined the phrase 'Grammar of Anarchy' for unconstitutional agitations\n4. Mockingly called the Drafting Committee a 'Drifting Committee'",
    "பட்டியல் I-ஐ (விமர்சகர் / அறிஞர்) பட்டியல் II உடன் (மேற்கோள் / விமர்சனச் சொல்) பொருத்தி கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான பதிலதைத் தேர்ந்தெடுக்கவும்:\n\nபட்டியல் I\nA. டாக்டர் பி.ஆர். அம்பேத்கர்\nB. கிரான்வில் ஆஸ்டின்\nC. நசிருதீன் அகமது\nD. வின்ஸ்டன் சர்ச்சில்\n\nபட்டியல் II\n1. அவையை 'ஒரு கட்சி நாட்டில் ஒரு கட்சி அமைப்பு' என விவரித்தார்\n2. அவை 'இந்தியாவின் ஒரே ஒரு முக்கிய சமூகத்தை மட்டுமே பிரதிநிதித்துவப்படுத்தியது' என்றார்\n3. அரசியலமைப்புக்கு புறம்பான போராட்டங்களுக்கு 'அராஜகத்தின் இலக்கணம்' என்றார்\n4. வரைவுக் குழுவைக் கேலியாக 'மிதவைக் குழு' (Drifting Committee) என்று அழைத்தார்",
    ["Dr. B.R. Ambedkar", "Granville Austin", "Naziruddin Ahmad", "Winston Churchill"],
    ["டாக்டர் பி.ஆர். அம்பேத்கர்", "கிரான்வில் ஆஸ்டின்", "நசிருதீன் அகமது", "வின்ஸ்டன் சர்ச்சில்"],
    ["Described Assembly as 'a one-party body in an essentially one-party country'", "Remarked Assembly represented 'only one major community in India'", "Coined the phrase 'Grammar of Anarchy' for unconstitutional agitations", "Mockingly called the Drafting Committee a 'Drifting Committee'"],
    ["அவையை 'ஒரு கட்சி நாட்டில் ஒரு கட்சி அமைப்பு' என விவரித்தார்", "அவை 'இந்தியாவின் ஒரே ஒரு முக்கிய சமூகத்தை மட்டுமே பிரதிநிதித்துவப்படுத்தியது' என்றார்", "அரசியலமைப்புக்கு புறம்பான போராட்டங்களுக்கு 'அராஜகத்தின் இலக்கணம்' என்றார்", "வரைவுக் குழுவைக் கேலியாக 'மிதவைக் குழு' (Drifting Committee) என்று அழைத்தார்"],
    "A-3, B-1, C-4, D-2", "A-1, B-3, C-2, D-4", "A-3, B-4, C-1, D-2", "A-4, B-1, C-3, D-2",
    "A",
    "A-3: Ambedkar coined 'Grammar of Anarchy'. B-1: Granville Austin described Assembly as one-party body in one-party country. C-4: Naziruddin Ahmad called Drafting Committee 'Drifting Committee'. D-2: Winston Churchill said Assembly represented only one major community.",
    "A-3: அம்பேத்கர் 'அராஜகத்தின் இலக்கணம்' என்றார். B-1: கிரான்வில் ஆஸ்டின் 'ஒரு கட்சி நாட்டில் ஒரு கட்சி அமைப்பு' என்றார். C-4: நசிருதீன் அகமது 'மிதவைக் குழு' என்றார். D-2: சர்ச்சில் 'ஒரே முக்கிய சமூகம்' என்றார்.",
    "Correct. A-3, B-1, C-4, D-2 is the exact correct matching.", "சரி. A-3, B-1, C-4, D-2 சரியான பொருத்தம்.",
    "Incorrect. Ambedkar coined 'Grammar of Anarchy' (3), not one-party body (1).", "தவறு. அம்பேத்கர் 'அராஜகத்தின் இலக்கணம்' என்றார் (3).",
    "Incorrect. Naziruddin Ahmad called it 'Drifting Committee' (4), not one-party body (1).", "தவறு. நசிருதீன் அகமது 'மிதவைக் குழு' என்றார் (4).",
    "Incorrect. Ambedkar coined 'Grammar of Anarchy' (3), not Drifting Committee (4).", "தவறு. அம்பேத்கர் 'அராஜகத்தின் இலக்கணம்' என்றார் (3).",
    "TNPSC Trap: Naziruddin Ahmad = 'Drifting Committee'. Winston Churchill = 'One major community in India'. Lord Viscount Simon = 'A body of Hindus'.",
    "TNPSC பொறி: நசிருதீன் அகமது = 'மிதவைக் குழு'. வின்ஸ்டன் சர்ச்சில் = 'ஒரே ஒரு முக்கிய சமூகம்'. லார்ட் சைமன் = 'இந்துக்களின் அமைப்பு'.",
    "Granville Austin praised the Constituent Assembly for making decisions by consensus and accommodation.",
    "கிரான்வில் ஆஸ்டின் அரசியலமைப்பு அவை ஒருமித்த கருத்து மற்றும் இடமளித்தல் மூலம் முடிவுகளை எடுத்ததைப் பாராட்டினார்.",
    "Analyze", 75, ["Polity", "Making of Indian Constitution", "Criticism of Constituent Assembly", "Granville Austin's Views", "Ambedkar's Final Speech"]
))

# MIC_MF_017
questions.append(make_mf_q(
    "MIC_MF_017", "Match the Following",
    "Match List I (Assembly Membership Category) with List II (Seat Breakdown Post-Partition) and select the correct answer using the codes given below:\n\nList I\nA. Pre-Partition Total Strength\nB. Post-Partition Total Strength\nC. Post-Partition Indian Provinces Strength\nD. Post-Partition Princely States Strength\n\nList II\n1. 229 Seats (Reduced from 292)\n2. 70 Seats (Reduced from 93)\n3. 299 Seats\n4. 389 Seats",
    "பட்டியல் I-ஐ (அவை உறுப்பினர் பிரிவு) பட்டியல் II உடன் (பிரிவினைக்குப் பிந்தைய இடங்கள் விவரம்) பொருத்தி கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான பதிலதைத் தேர்ந்தெடுக்கவும்:\n\nபட்டியல் I\nA. பிரிவினைக்கு முந்தைய மொத்த எண்ணிக்கை\nB. பிரிவினைக்குப் பிந்தைய மொத்த எண்ணிக்கை\nC. பிரிவினைக்குப் பிந்தைய இந்திய மாகாணங்கள் எண்ணிக்கை\nD. பிரிவினைக்குப் பிந்தைய சுதேச சமஸ்தானங்கள் எண்ணிக்கை\n\nபட்டியல் II\n1. 229 இடங்கள் (292 இலிருந்து குறைந்தது)\n2. 70 இடங்கள் (93 இலிருந்து குறைந்தது)\n3. 299 இடங்கள்\n4. 389 இடங்கள்",
    ["Pre-Partition Total Strength", "Post-Partition Total Strength", "Post-Partition Indian Provinces Strength", "Post-Partition Princely States Strength"],
    ["பிரிவினைக்கு முந்தைய மொத்த எண்ணிக்கை", "பிரிவினைக்குப் பிந்தைய மொத்த எண்ணிக்கை", "பிரிவினைக்குப் பிந்தைய இந்திய மாகாணங்கள் எண்ணிக்கை", "பிரிவினைக்குப் பிந்தைய சுதேச சமஸ்தானங்கள் எண்ணிக்கை"],
    ["229 Seats (Reduced from 292)", "70 Seats (Reduced from 93)", "299 Seats", "389 Seats"],
    ["229 இடங்கள் (292 இலிருந்து குறைந்தது)", "70 இடங்கள் (93 இலிருந்து குறைந்தது)", "299 இடங்கள்", "389 இடங்கள்"],
    "A-4, B-3, C-1, D-2", "A-3, B-4, C-2, D-1", "A-4, B-1, C-3, D-2", "A-2, B-3, C-1, D-4",
    "A",
    "A-4: Pre-partition total strength was 389. B-3: Post-partition total strength was 299. C-1: Post-partition Indian provinces strength was 229. D-2: Post-partition Princely States strength was 70.",
    "A-4: பிரிவினைக்கு முன் மொத்த எண்ணிக்கை 389. B-3: பிரிவினைக்குப் பின் மொத்த எண்ணிக்கை 299. C-1: மாகாணங்கள் 229. D-2: சமஸ்தானங்கள் 70.",
    "Correct. A-4, B-3, C-1, D-2 is the exact correct matching.", "சரி. A-4, B-3, C-1, D-2 சரியான பொருத்தம்.",
    "Incorrect. Pre-partition total was 389 (4), not 299 (3).", "தவறு. பிரிவினைக்கு முன் 389 (4).",
    "Incorrect. Post-partition total was 299 (3), not 229 (1).", "தவறு. பிரிவினைக்குப் பின் 299 (3).",
    "Incorrect. Pre-partition total was 389 (4), not 70 (2).", "தவறு. பிரிவினைக்கு முன் 389 (4).",
    "TNPSC Trap: Memorize post-partition reduction: Total 389 -> 299; Provinces 292 -> 229; Princely States 93 -> 70.",
    "TNPSC பொறி: பிரிவினைக்குப் பிந்தைய குறைப்பை மனனம் செய்க: மொத்தம் 389 -> 299; மாகாணங்கள் 292 -> 229; சமஸ்தானங்கள் 93 -> 70.",
    "The reduction occurred because Muslim League members from Pakistan areas (West Punjab, East Bengal, NWFP, Sindh, Baluchistan, Sylhet) withdrew.",
    "பாகிஸ்தான் பகுதிகளிலிருந்த முஸ்லிம் லீக் உறுப்பினர்கள் விலகியதால் இந்நீக்கம் ஏற்பட்டது.",
    "Analyze", 75, ["Polity", "Making of Indian Constitution", "Partition impact", "Reduction from 389 to 299 members"]
))
