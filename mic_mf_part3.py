from mic_mf_part1 import make_mf_q

questions = []

# MIC_MF_018
questions.append(make_mf_q(
    "MIC_MF_018", "Match the Following",
    "Match List I (Drafting Committee Member) with List II (State / Province Represented or Prior Position) and select the correct answer using the codes given below:\n\nList I\nA. Dr. B.R. Ambedkar\nB. Alladi Krishnaswamy Ayyar\nC. T.T. Krishnamachari\nD. N. Madhava Rau\n\nList II\n1. Representative from Madras Province (replaced D.P. Khaitan)\n2. Re-elected from Bombay Province (Poona seat) after Partition\n3. Former Dewan of Mysore State (replaced B.L. Mitter)\n4. Representative from Madras Province & former Advocate-General",
    "பட்டியல் I-ஐ (வரைவுக் குழு உறுப்பினர்) பட்டியல் II உடன் (பிரதிநிதித்துவப்படுத்திய மாநிலம் / முந்தைய பதவி) பொருத்தி கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான பதிலதைத் தேர்ந்தெடுக்கவும்:\n\nபட்டியல் I\nA. டாக்டர் பி.ஆர். அம்பேத்கர்\nB. அல்லாடி கிருஷ்ணசாமி அய்யர்\nC. டி.டி. கிருஷ்ணமாச்சாரி\nD. என். மாதவ ராவ்\n\nபட்டியல் II\n1. மெட்ராஸ் மாகாணப் பிரதிநிதி (டி.பி. கைத்தானுக்குப் பின் சேர்ந்தவர்)\n2. பிரிவினைக்குப் பின் பம்பாய் மாகாணத்திலிருந்து (பூனா) மீண்டும் தேர்ந்தெடுக்கப்பட்டவர்\n3. மைசூர் சமஸ்தானத்தின் முன்னாள் திவான் (பி.எல். மிட்டருக்குப் பின் சேர்ந்தவர்)\n4. மெட்ராஸ் மாகாணப் பிரதிநிதி & முன்னாள் தலைமை வழக்கறிஞர்",
    ["Dr. B.R. Ambedkar", "Alladi Krishnaswamy Ayyar", "T.T. Krishnamachari", "N. Madhava Rau"],
    ["டாக்டர் பி.ஆர். அம்பேத்கர்", "அல்லாடி கிருஷ்ணசாமி அய்யர்", "டி.டி. கிருஷ்ணமாச்சாரி", "என். மாதவ ராவ்"],
    ["Representative from Madras Province (replaced D.P. Khaitan)", "Re-elected from Bombay Province (Poona seat) after Partition", "Former Dewan of Mysore State (replaced B.L. Mitter)", "Representative from Madras Province & former Advocate-General"],
    ["மெட்ராஸ் மாகாணப் பிரதிநிதி (டி.பி. கைத்தானுக்குப் பின் சேர்ந்தவர்)", "பிரிவினைக்குப் பின் பம்பாய் மாகாணத்திலிருந்து (பூனா) மீண்டும் தேர்ந்தெடுக்கப்பட்டவர்", "மைசூர் சமஸ்தானத்தின் முன்னாள் திவான் (பி.எல். மிட்டருக்குப் பின் சேர்ந்தவர்)", "மெட்ராஸ் மாகாணப் பிரதிநிதி & முன்னாள் தலைமை வழக்கறிஞர்"],
    "A-2, B-4, C-1, D-3", "A-4, B-2, C-1, D-3", "A-2, B-1, C-4, D-3", "A-3, B-4, C-2, D-1",
    "A",
    "A-2: Dr. B.R. Ambedkar was re-elected from Bombay (Poona) after partition. B-4: Alladi Krishnaswamy Ayyar was Advocate-General & Madras member. C-1: T.T. Krishnamachari was Madras member replacing Khaitan. D-3: N. Madhava Rau was former Dewan of Mysore replacing Mitter.",
    "A-2: அம்பேத்கர் பம்பாயிலிருந்து மீண்டும் தேர்ந்தெடுக்கப்பட்டவர். B-4: அல்லாடி மெட்ராஸ் தலைமை வழக்கறிஞர். C-1: டி.டி. கிருஷ்ணமாச்சாரி கைத்தானுக்குப் பின் சேர்ந்தவர். D-3: மாதவ ராவ் மைசூர் முன்னாள் திவான்.",
    "Correct. A-2, B-4, C-1, D-3 is the exact correct matching.", "சரி. A-2, B-4, C-1, D-3 சரியான பொருத்தம்.",
    "Incorrect. Ambedkar was re-elected from Bombay (2), not Madras Advocate-General (4).", "தவறு. அம்பேத்கர் பம்பாயிலிருந்து தேர்ந்தெடுக்கப்பட்டவர் (2).",
    "Incorrect. Alladi was Madras Advocate-General (4), not replacing Khaitan (1).", "தவறு. அல்லாடி மெட்ராஸ் தலைமை வழக்கறிஞர் (4).",
    "Incorrect. Ambedkar was re-elected from Bombay (2), not Dewan of Mysore (3).", "தவறு. அம்பேத்கர் பம்பாயிலிருந்து தேர்ந்தெடுக்கப்பட்டவர் (2).",
    "TNPSC Trap: Ambedkar was initially elected from Jessore-Khulna (East Bengal); after Partition, M.R. Jayakar resigned his Bombay seat to allow Ambedkar's re-election.",
    "TNPSC பொறி: அம்பேத்கர் முதலில் கிழக்கு வங்காளத்திலிருந்து தேர்ந்தெடுக்கப்பட்டார்; பிரிவினைக்குப் பின் எம்.ஆர். ஜெயக்கர் விலகிய பூனா தொகுதியிலிருந்து பம்பாயில் தேர்ந்தெடுக்கப்பட்டார்.",
    "N. Madhava Rau was the former Dewan of Mysore who drafted municipal and constitutional reforms in Mysore.",
    "என். மாதவ ராவ் மைசூரின் முன்னாள் திவானாகப் பணியாற்றியவராவார்.",
    "Analyze", 75, ["Polity", "Making of Indian Constitution", "Drafting Committee", "Ambedkar", "Alladi Krishnaswamy Ayyar", "T. T. Krishnamachari"]
))

# MIC_MF_019
questions.append(make_mf_q(
    "MIC_MF_019", "Match the Following",
    "Match List I (Article Enforced on Nov 26, 1949 under Art 394) with List II (Subject Matter) and select the correct answer using the codes given below:\n\nList I\nA. Articles 5, 6, 7, 8, 9\nB. Article 60\nC. Article 324\nD. Article 393\n\nList II\n1. Oath or affirmation by the President of India\n2. Short Title of the Constitution ('This Constitution may be called the Constitution of India')\n3. Citizenship provisions at the commencement of the Constitution\n4. Election Commission & superintendence of elections",
    "பட்டியல் I-ஐ (சரத்து 394 இன் படி நவம்பர் 26, 1949 இல் நடைமுறைக்கு வந்த சரத்துகள்) பட்டியல் II உடன் (பொருள்) பொருத்தி கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான பதிலதைத் தேர்ந்தெடுக்கவும்:\n\nபட்டியல் I\nA. சரத்துகள் 5, 6, 7, 8, 9\nB. சரத்து 60\nC. சரத்து 324\nD. சரத்து 393\n\nபட்டியல் II\n1. இந்தியக் குடியரசுத் தலைவரின் உறுதிமொழி அல்லது பிரமாணம்\n2. அரசியலமைப்பின் குறுகிய தலைப்பு ('இந்த அரசியலமைப்பு இந்திய அரசியலமைப்பு என்று அழைக்கப்படலாம்')\n3. அரசியலமைப்பு தொடங்கும் போது உள்ள குடியுரிமை விதிகள்\n4. தேர்தல் ஆணையம் & தேர்தல்களைக் மேற்பார்வையிடுதல்",
    ["Articles 5, 6, 7, 8, 9", "Article 60", "Article 324", "Article 393"],
    ["சரத்துகள் 5, 6, 7, 8, 9", "சரத்து 60", "சரத்து 324", "சரத்து 393"],
    ["Oath or affirmation by the President of India", "Short Title of the Constitution ('This Constitution may be called the Constitution of India')", "Citizenship provisions at the commencement of the Constitution", "Election Commission & superintendence of elections"],
    ["இந்தியக் குடியரசுத் தலைவரின் உறுதிமொழி அல்லது பிரமாணம்", "அரசியலமைப்பின் குறுகிய தலைப்பு ('இந்த அரசியலமைப்பு இந்திய அரசியலமைப்பு என்று அழைக்கப்படலாம்')", "அரசியலமைப்பு தொடங்கும் போது உள்ள குடியுரிமை விதிகள்", "தேர்தல் ஆணையம் & தேர்தல்களைக் மேற்பார்வையிடுதல்"],
    "A-3, B-1, C-4, D-2", "A-1, B-3, C-2, D-4", "A-3, B-4, C-1, D-2", "A-2, B-1, C-4, D-3",
    "A",
    "A-3: Articles 5-9 relate to Citizenship. B-1: Article 60 relates to Oath by President. C-4: Article 324 relates to Election Commission. D-2: Article 393 relates to Short Title.",
    "A-3: சரத்துகள் 5-9 குடியுரிமை. B-1: சரத்து 60 குடியரசுத் தலைவர் உறுதிமொழி. C-4: சரத்து 324 தேர்தல் ஆணையம். D-2: சரத்து 393 குறுகிய தலைப்பு.",
    "Correct. A-3, B-1, C-4, D-2 is the exact correct matching.", "சரி. A-3, B-1, C-4, D-2 சரியான பொருத்தம்.",
    "Incorrect. Articles 5-9 relate to Citizenship (3), not Oath by President (1).", "தவறு. சரத்துகள் 5-9 குடியுரிமை (3).",
    "Incorrect. Article 324 relates to Election Commission (4), not Oath (1).", "தவறு. சரத்து 324 தேர்தல் ஆணையம் (4).",
    "Incorrect. Articles 5-9 relate to Citizenship (3), not Short Title (2).", "தவறு. சரத்துகள் 5-9 குடியுரிமை (3).",
    "TNPSC Trap: Article 393 contains the official Short Title: 'Constitution of India'. Article 394 contained the enforcement date provisions.",
    "TNPSC பொறி: சரத்து 393 அதிகாரப்பூர்வ குறுகிய தலைப்பைக் கொண்டுள்ளது: 'இந்திய அரசியலமைப்பு'. சரத்து 394 நடைமுறைத் தேதியைக் கொண்டுள்ளது.",
    "Article 394 itself came into force on November 26, 1949.",
    "சரத்து 394 தானாகவே நவம்பர் 26, 1949 அன்று நடைமுறைக்கு வந்தது.",
    "Analyze", 75, ["Polity", "Making of Indian Constitution", "Enforcement of Constitution", "Constitutional Facts"]
))

# MIC_MF_020
questions.append(make_mf_q(
    "MIC_MF_020", "Match the Following",
    "Match List I (Key Personality) with List II (Famous CAD Statement / Philosophical Position) and select the correct answer using the codes given below:\n\nList I\nA. Dr. B.R. Ambedkar\nB. Jawaharlal Nehru\nC. Sardar Vallabhbhai Patel\nD. Sir B.N. Rau\n\nList II\n1. Recommended replacing 'due process of law' with 'procedure established by law'\n2. Guided the integration of Princely States and chaired Advisory Committee\n3. Moved the Objectives Resolution declaring India as an Independent Sovereign Republic\n4. Warned that 'Bhakti in politics is a sure road to degradation and eventual dictatorship'",
    "பட்டியல் I-ஐ (முக்கிய ஆளுமை) பட்டியல் II உடன் (பிரபல CAD உரை / தத்துவ நிலைப்பாடு) பொருத்தி கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான பதிலதைத் தேர்ந்தெடுக்கவும்:\n\nபட்டியல் I\nA. டாக்டர் பி.ஆர். அம்பேத்கர்\nB. ஜவகர்லால் நேரு\nC. சர்தார் வல்லபாய் படேல்\nD. சர் பி.என். ராவ்\n\nபட்டியல் II\n1. 'சட்டத்தின் உரிய நடைமுறை' என்பதை 'சட்டத்தால் அமைக்கப்பட்ட நடைமுறை'யால் மாற்றப் பரிந்துரைத்தார்\n2. சுதேச சமஸ்தானங்களின் இணைப்பை வழிநடத்தி ஆலோசனைக் குழுவிற்கு தலைமை தாங்கினார்\n3. இந்தியாவை சுதந்திர இறையாண்மை கொண்ட குடியரசாக அறிவிக்கும் குறிக்கோள்கள் தீர்மானத்தை முன்மொழிந்தார்\n4. 'அரசியலில் பக்தி சீரழிவுக்கும் சர்வாதிகாரத்திற்கும் உறுதியான வழி' என்று எச்சரித்தார்",
    ["Dr. B.R. Ambedkar", "Jawaharlal Nehru", "Sardar Vallabhbhai Patel", "Sir B.N. Rau"],
    ["டாக்டர் பி.ஆர். அம்பேத்கர்", "ஜவகர்லால் நேரு", "சர்தார் வல்லபாய் படேல்", "சர் பி.என். ராவ்"],
    ["Recommended replacing 'due process of law' with 'procedure established by law'", "Guided the integration of Princely States and chaired Advisory Committee", "Moved the Objectives Resolution declaring India as an Independent Sovereign Republic", "Warned that 'Bhakti in politics is a sure road to degradation and eventual dictatorship'"],
    ["'சட்டத்தின் உரிய நடைமுறை' என்பதை 'சட்டத்தால் அமைக்கப்பட்ட நடைமுறை'யால் மாற்றப் பரிந்துரைத்தார்", "சுதேச சமஸ்தானங்களின் இணைப்பை வழிநடத்தி ஆலோசனைக் குழுவிற்கு தலைமை தாங்கினார்", "இந்தியாவை சுதந்திர இறையாண்மை கொண்ட குடியரசாக அறிவிக்கும் குறிக்கோள்கள் தீர்மானத்தை முன்மொழிந்தார்", "'அரசியலில் பக்தி சீரழிவுக்கும் சர்வாதிகாரத்திற்கும் உறுதியான வழி' என்று எச்சரித்தார்"],
    "A-4, B-3, C-2, D-1", "A-3, B-4, C-1, D-2", "A-4, B-1, C-2, D-3", "A-2, B-3, C-4, D-1",
    "A",
    "A-4: Dr. B.R. Ambedkar warned against Bhakti in politics. B-3: Jawaharlal Nehru moved the Objectives Resolution. C-2: Sardar Patel guided princely integration & chaired Advisory Committee. D-1: Sir B.N. Rau recommended replacing due process.",
    "A-4: அம்பேத்கர் அரசியலில் பக்தி பற்றி எச்சரித்தார். B-3: நேரு குறிக்கோள்கள் தீர்மானத்தை முன்மொழிந்தார். C-2: படேல் சமஸ்தானங்களை இணைத்து ஆலோசனைக் குழுத் தலைவரானார். D-1: பி.என். ராவ் சட்ட நடைமுறை மாற்றப் பரிந்துரை செய்தார்.",
    "Correct. A-4, B-3, C-2, D-1 is the exact correct matching.", "சரி. A-4, B-3, C-2, D-1 சரியான பொருத்தம்.",
    "Incorrect. Ambedkar warned against Bhakti in politics (4), not Objectives Resolution (3).", "தவறு. அம்பேத்கர் அரசியலில் பக்தி பற்றி எச்சரித்தார் (4).",
    "Incorrect. Nehru moved Objectives Resolution (3), not procedure established by law (1).", "தவறு. நேரு குறிக்கோள்கள் தீர்மானத்தை முன்மொழிந்தார் (3).",
    "Incorrect. Ambedkar warned against Bhakti in politics (4), not princely integration (2).", "தவறு. அம்பேத்கர் அரசியலில் பக்தி பற்றி எச்சரித்தார் (4).",
    "TNPSC Trap: Bhakti warning = Dr. B.R. Ambedkar. Objectives Resolution = Jawaharlal Nehru. Princely integration = Sardar Vallabhbhai Patel.",
    "TNPSC பொறி: பக்தி பற்றிய எச்சரிக்கை = டாக்டர் பி.ஆர். அம்பேத்கர். குறிக்கோள்கள் தீர்மானம் = ஜவகர்லால் நேரு. சமஸ்தானங்கள் இணைப்பு = சர்தார் படேல்.",
    "Ambedkar quoted John Stuart Mill in warning against hero-worship in politics.",
    "அரசியலில் நபர் வழிபாட்டிற்கு எதிராக எச்சரிக்கையில் அம்பேத்கர் ஜான் ஸ்டூவர்ட் மில்லை மேற்கோள் காட்டினார்.",
    "Analyze", 75, ["Polity", "Making of Indian Constitution", "Ambedkar", "Rajendra Prasad", "B. N. Rau", "Objectives Resolution"]
))

# MIC_MF_021
questions.append(make_mf_q(
    "MIC_MF_021", "Match the Following",
    "Match List I (Assembly Dual Function / Aspect) with List II (Presiding Officer / Detail) and select the correct answer using the codes given below:\n\nList I\nA. Assembly meeting as Constituent Body\nB. Assembly meeting as Legislative Body\nC. Commencement of Dual Functions\nD. Duration of Provisional Parliament\n\nList II\n1. November 17, 1947 (when Speaker was elected)\n2. Chaired by Dr. Rajendra Prasad\n3. Functioned until first general elections in May 1952\n4. Chaired by G.V. Mavlankar",
    "பட்டியல் I-ஐ (அவையின் இரட்டைச் செயல்பாடு / அம்சம்) பட்டியல் II உடன் (தலைமை தாங்கிய அதிகாரி / விவரம்) பொருத்தி கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான பதிலதைத் தேர்ந்தெடுக்கவும்:\n\nபட்டியல் I\nA. அவை அரசியலமைப்பு அமைப்பாகக் கூடிய போது\nB. அவை சட்டமன்றமாகக் கூடிய போது\nC. இரட்டைச் செயல்பாடுகள் தொடங்கிய நாள்\nD. தற்காலிக நாடாளுமன்றத்தின் காலம்\n\nபட்டியல் II\n1. நவம்பர் 17, 1947 (சபாநாயகர் தேர்ந்தெடுக்கப்பட்ட போது)\n2. டாக்டர் ராஜேந்திர பிரசாத் தலைமை தாங்கினார்\n3. மே 1952 இல் முதல் பொதுத் தேர்தல் வரை செயல்பட்டது\n4. ஜி.வி. மாவ்லங்கார் தலைமை தாங்கினார்",
    ["Assembly meeting as Constituent Body", "Assembly meeting as Legislative Body", "Commencement of Dual Functions", "Duration of Provisional Parliament"],
    ["அவை அரசியலமைப்பு அமைப்பாகக் கூடிய போது", "அவை சட்டமன்றமாகக் கூடிய போது", "இரட்டைச் செயல்பாடுகள் தொடங்கிய நாள்", "தற்காலிக நாடாளுமன்றத்தின் காலம்"],
    ["November 17, 1947 (when Speaker was elected)", "Chaired by Dr. Rajendra Prasad", "Functioned until first general elections in May 1952", "Chaired by G.V. Mavlankar"],
    ["நவம்பர் 17, 1947 (சபாநாயகர் தேர்ந்தெடுக்கப்பட்ட போது)", "டாக்டர் ராஜேந்திர பிரசாத் தலைமை தாங்கினார்", "மே 1952 இல் முதல் பொதுத் தேர்தல் வரை செயல்பட்டது", "ஜி.வி. மாவ்லங்கார் தலைமை தாங்கினார்"],
    "A-2, B-4, C-1, D-3", "A-4, B-2, C-1, D-3", "A-2, B-1, C-4, D-3", "A-3, B-4, C-2, D-1",
    "A",
    "A-2: Assembly as Constituent Body was chaired by Dr. Rajendra Prasad. B-4: Assembly as Legislative Body was chaired by G.V. Mavlankar. C-1: Dual functions commenced on Nov 17, 1947. D-3: Provisional Parliament operated till May 1952.",
    "A-2: அரசியலமைப்பு அவையாகக் கூடிய போது தலைவர் ராஜேந்திர பிரசாத். B-4: சட்டமன்றமாகக் கூடிய போது தலைவர் ஜி.வி. மாவ்லங்கார். C-1: இரட்டைச் செயல்பாடுகள் நவம்பர் 17, 1947 இல் தொடங்கின. D-3: தற்காலிக நாடாளுமன்றம் மே 1952 வரை செயல்பட்டது.",
    "Correct. A-2, B-4, C-1, D-3 is the exact correct matching.", "சரி. A-2, B-4, C-1, D-3 சரியான பொருத்தம்.",
    "Incorrect. Constituent Body was chaired by Rajendra Prasad (2), not Mavlankar (4).", "தவறு. அரசியலமைப்பு அவையின் தலைவர் ராஜேந்திர பிரசாத் (2).",
    "Incorrect. Legislative Body was chaired by Mavlankar (4), not Nov 17 date (1).", "தவறு. சட்டமன்றத்தின் தலைவர் மாவ்லங்கார் (4).",
    "Incorrect. Constituent Body was chaired by Rajendra Prasad (2), not Provisional Parliament duration (3).", "தவறு. அரசியலமைப்பு அவையின் தலைவர் ராஜேந்திர பிரசாத் (2).",
    "TNPSC Trap: Assembly met as Constituent Body under Rajendra Prasad, and Legislative Body under G.V. Mavlankar on SEPARATE DAYS.",
    "TNPSC பொறி: அவை அரசியலமைப்பு அவையாக ராஜேந்திர பிரசாத் தலைமையிலும், சட்டமன்றமாக ஜி.வி. மாவ்லங்கார் தலைமையிலும் வெவ்வேறு நாட்களில் கூடியது.",
    "G.V. Mavlankar was fondly called 'Dadasaheb' and became 1st Speaker of Lok Sabha.",
    "ஜி.வி. மாவ்லங்கார் 'தாதாசாகேப்' என்று அன்புடன் அழைக்கப்பட்டார் மற்றும் மக்களவையின் 1வது சபாநாயகரானார்.",
    "Analyze", 75, ["Polity", "Making of Indian Constitution", "Constituent Assembly as Legislature", "Rajendra Prasad"]
))

# MIC_MF_022
questions.append(make_mf_q(
    "MIC_MF_022", "Match the Following",
    "Match List I (Draft Constitution Milestone Date) with List II (Specific Event / Reading Stage) and select the correct answer using the codes given below:\n\nList I\nA. February 1948\nB. November 4, 1948\nC. October 17, 1949\nD. November 26, 1949\n\nList II\n1. First Reading commenced in Assembly with Ambedkar moving the draft\n2. Third Reading completed and motion on Draft Constitution passed\n3. Publication of the First Draft of the Constitution for public scrutiny\n4. Completion of Second Reading (clause-by-clause consideration)",
    "பட்டியல் I-ஐ (வரைவு அரசியலமைப்பு மைல்கல் தேதி) பட்டியல் II உடன் (குறிப்பிட்ட நிகழ்வு / வாசிப்பு நிலை) பொருத்தி கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான பதிலதைத் தேர்ந்தெடுக்கவும்:\n\nபட்டியல் I\nA. பிப்ரவரி 1948\nB. நவம்பர் 4, 1948\nC. அக்டோபர் 17, 1949\nD. நவம்பர் 26, 1949\n\nபட்டியல் II\n1. அம்பேத்கர் வரைவை அறிமுகப்படுத்தியவுடன் அவையில் முதல் வாசிப்பு தொடங்கியது\n2. 3வது வாசிப்பு முடிவடைந்து வரைவு அரசியலமைப்பு மீதான தீர்மானம் நிறைவேற்றப்பட்டது\n3. மக்கள் பரிசீலனைக்காக அரசியலமைப்பின் முதல் வரைவு வெளியிடப்பட்டது\n4. 2வது வாசிப்பு (சரத்து வாரியான பரிசீலனை) நிறைவடைந்தது",
    ["February 1948", "November 4, 1948", "October 17, 1949", "November 26, 1949"],
    ["பிப்ரவரி 1948", "நவம்பர் 4, 1948", "அக்டோபர் 17, 1949", "நவம்பர் 26, 1949"],
    ["First Reading commenced in Assembly with Ambedkar moving the draft", "Third Reading completed and motion on Draft Constitution passed", "Publication of the First Draft of the Constitution for public scrutiny", "Completion of Second Reading (clause-by-clause consideration)"],
    ["அம்பேத்கர் வரைவை அறிமுகப்படுத்தியவுடன் அவையில் முதல் வாசிப்பு தொடங்கியது", "3வது வாசிப்பு முடிவடைந்து வரைவு அரசியலமைப்பு மீதான தீர்மானம் நிறைவேற்றப்பட்டது", "மக்கள் பரிசீலனைக்காக அரசியலமைப்பின் முதல் வரைவு வெளியிடப்பட்டது", "2வது வாசிப்பு (சரத்து வாரியான பரிசீலனை) நிறைவடைந்தது"],
    "A-3, B-1, C-4, D-2", "A-1, B-3, C-2, D-4", "A-3, B-4, C-1, D-2", "A-2, B-1, C-4, D-3",
    "A",
    "A-3: Feb 1948 was publication of First Draft. B-1: Nov 4, 1948 was introduction & First Reading. C-4: Oct 17, 1949 was completion of Second Reading. D-2: Nov 26, 1949 was completion of Third Reading & passing.",
    "A-3: பிப்ரவரி 1948 முதல் வரைவு வெளியீடு. B-1: நவம்பர் 4, 1948 முதல் வாசிப்பு தொடக்கம். C-4: அக்டோபர் 17, 1949 2வது வாசிப்பு முடிவு. D-2: நவம்பர் 26, 1949 3வது வாசிப்பு முடிந்து தீர்மானம் நிறைவேறியது.",
    "Correct. A-3, B-1, C-4, D-2 is the exact correct matching.", "சரி. A-3, B-1, C-4, D-2 சரியான பொருத்தம்.",
    "Incorrect. Feb 1948 was First Draft publication (3), not First Reading (1).", "தவறு. பிப்ரவரி 1948 முதல் வரைவு வெளியீடு (3).",
    "Incorrect. Oct 17, 1949 was Second Reading completion (4), not First Reading (1).", "தவறு. அக்டோபர் 17, 1949 2வது வாசிப்பு முடிவு (4).",
    "Incorrect. Feb 1948 was First Draft publication (3), not Third Reading (2).", "தவறு. பிப்ரவரி 1948 முதல் வரைவு வெளியீடு (3).",
    "TNPSC Trap: First Draft = Feb 1948. First Reading = Nov 4-9, 1948. Second Reading ended = Oct 17, 1949. Passed = Nov 26, 1949.",
    "TNPSC பொறி: முதல் வரைவு = பிப்ரவரி 1948. முதல் வாசிப்பு = நவம்பர் 4-9, 1948. 2வது வாசிப்பு முடிவு = அக்டோபர் 17, 1949. நிறைவேற்றப்பட்டது = நவம்பர் 26, 1949.",
    "The Second Reading was the longest stage, clause-by-clause, where 7,635 amendments were proposed.",
    "இரண்டாவது வாசிப்பே மிக நீண்ட கட்டமாகும், இதில் 7,635 திருத்தங்கள் முன்மொழியப்பட்டன.",
    "Analyze", 75, ["Polity", "Making of Indian Constitution", "Draft Constitution", "Adoption of Constitution"]
))

# MIC_MF_023
questions.append(make_mf_q(
    "MIC_MF_023", "Match the Following",
    "Match List I (Special / Ad hoc Committee) with List II (Chairman) and select the correct answer using the codes given below:\n\nList I\nA. Ad hoc Committee on National Flag\nB. Order of Business Committee\nC. Special Committee to Examine Draft Constitution\nD. Committee on Functions of Constituent Assembly\n\nList II\n1. G.V. Mavlankar\n2. Sir Alladi Krishnaswamy Ayyar\n3. Dr. K.M. Munshi\n4. Dr. Rajendra Prasad",
    "பட்டியல் I-ஐ (சிறப்பு / தற்காலிகக் குழு) பட்டியல் II உடன் (தலைவர்) பொருத்தி கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான பதிலதைத் தேர்ந்தெடுக்கவும்:\n\nபட்டியல் I\nA. தேசியக் கொடிக்கான தற்காலிகக் குழு\nB. வணிக வரிசைக் குழு\nC. வரைவு அரசியலமைப்பை ஆராயும் சிறப்புக் குழு\nD. அரசியலமைப்பு அவையின் செயல்பாடுகள் குழு\n\nபட்டியல் II\n1. ஜி.வி. மாவ்லங்கார்\n2. சர் அல்லாடி கிருஷ்ணசாமி அய்யர்\n3. டாக்டர் கே.எம். முன்ஷி\n4. டாக்டர் ராஜேந்திர பிரசாத்",
    ["Ad hoc Committee on National Flag", "Order of Business Committee", "Special Committee to Examine Draft Constitution", "Committee on Functions of Constituent Assembly"],
    ["தேசியக் கொடிக்கான தற்காலிகக் குழு", "வணிக வரிசைக் குழு", "வரைவு அரசியலமைப்பை ஆராயும் சிறப்புக் குழு", "அரசியலமைப்பு அவையின் செயல்பாடுகள் குழு"],
    ["G.V. Mavlankar", "Sir Alladi Krishnaswamy Ayyar", "Dr. K.M. Munshi", "Dr. Rajendra Prasad"],
    ["ஜி.வி. மாவ்லங்கார்", "சர் அல்லாடி கிருஷ்ணசாமி அய்யர்", "டாக்டர் கே.எம். முன்ஷி", "டாக்டர் ராஜேந்திர பிரசாத்"],
    "A-4, B-3, C-2, D-1", "A-3, B-4, C-1, D-2", "A-4, B-1, C-2, D-3", "A-2, B-3, C-4, D-1",
    "A",
    "A-4: Ad hoc Flag Committee was chaired by Dr. Rajendra Prasad. B-3: Order of Business Committee was chaired by Dr. K.M. Munshi. C-2: Special Committee to Examine Draft Constitution was chaired by Sir Alladi Krishnaswamy Ayyar. D-1: Committee on Functions of Assembly was chaired by G.V. Mavlankar.",
    "A-4: தேசியக் கொடிக் குழுத் தலைவர் டாக்டர் ராஜேந்திர பிரசாத். B-3: வணிக வரிசைக் குழுத் தலைவர் கே.எம். முன்ஷி. C-2: வரைவு அரசியலமைப்பு ஆராயும் குழுத் தலைவர் அல்லாடி கிருஷ்ணசாமி அய்யர். D-1: அவையின் செயல்பாடுகள் குழுத் தலைவர் ஜி.வி. மாவ்லங்கார்.",
    "Correct. A-4, B-3, C-2, D-1 is the exact correct matching.", "சரி. A-4, B-3, C-2, D-1 சரியான பொருத்தம்.",
    "Incorrect. Ad hoc Flag Committee was chaired by Rajendra Prasad (4), not Munshi (3).", "தவறு. தேசியக் கொடிக் குழுத் தலைவர் ராஜேந்திர பிரசாத் (4).",
    "Incorrect. Order of Business Committee was chaired by Munshi (3), not Mavlankar (1).", "தவறு. வணிக வரிசைக் குழுத் தலைவர் முன்ஷி (3).",
    "Incorrect. Ad hoc Flag Committee was chaired by Rajendra Prasad (4), not Alladi (2).", "தவறு. தேசியக் கொடிக் குழுத் தலைவர் ராஜேந்திர பிரசாத் (4).",
    "TNPSC Trap: Committee on Functions of the Constituent Assembly = G.V. Mavlankar. Ad hoc Flag Committee = Dr. Rajendra Prasad.",
    "TNPSC பொறி: அவையின் செயல்பாடுகள் குழுத் தலைவர் = ஜி.வி. மாவ்லங்கார். தேசியக் கொடிக்கான தற்காலிகக் குழுத் தலைவர் = டாக்டர் ராஜேந்திர பிரசாத்.",
    "The Ad hoc Flag Committee was set up on June 23, 1947 and adopted the flag design on July 22, 1947.",
    "தேசியக் கொடிக்கான தற்காலிகக் குழு ஜூன் 23, 1947 இல் அமைக்கப்பட்டு ஜூலை 22, 1947 இல் கொடியை ஏற்றது.",
    "Analyze", 75, ["Polity", "Making of Indian Constitution", "Important Committees", "National Flag adoption"]
))

# MIC_MF_024
questions.append(make_mf_q(
    "MIC_MF_024", "Match the Following",
    "Match List I (Philosophical Term / Concept) with List II (Definition / Originator) and select the correct answer using the codes given below:\n\nList I\nA. Social Democracy\nB. Constitutional Morality\nC. Grammar of Anarchy\nD. Top-Dressing Description\n\nList II\n1. Term for civil disobedience & satyagraha when constitutional remedies are open\n2. Way of life recognizing Liberty, Equality, and Fraternity as an inseparable trinity\n3. Ambedkar's remark that Indian democracy is only a surface coat on undemocratic soil\n4. Reverence for constitutional forms borrowed from historian George Grote",
    "பட்டியல் I-ஐ (தத்துவச் சொல் / கோட்பாடு) பட்டியல் II உடன் (வரையறை / உருவாக்கியவர்) பொருத்தி கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான பதிலதைத் தேர்ந்தெடுக்கவும்:\n\nபட்டியல் I\nA. சமூக ஜனநாயகம்\nB. அரசியலமைப்பு அறநெறி\nC. அராஜகத்தின் இலக்கணம்\nD. மேல்-பூச்சு வர்ணனை\n\nபட்டியல் II\n1. அரசியலமைப்பு தீர்வுகள் உள்ள போது சட்டமறுப்பு & சத்தியாகிரகத்திற்கான சொல்\n2. சுதந்திரம், சமத்துவம், சகோதரத்துவத்தை பிரிக்க முடியாத திரித்துவமாகக் கொள்ளும் வாழ்க்கை முறை\n3. ஜனநாயகமற்ற மண்ணில் இந்திய ஜனநாயகம் ஒரு மேல்-பூச்சு மட்டுமே என்ற அம்பேத்கரின் வர்ணனை\n4. வரலாற்று ஆசிரியர் ஜார்ஜ் குரோட்டிடமிருந்து பெறப்பட்ட அரசியலமைப்பு வடிவங்கள் மீதான மரியாதை",
    ["Social Democracy", "Constitutional Morality", "Grammar of Anarchy", "Top-Dressing Description"],
    ["சமூக ஜனநாயகம்", "அரசியலமைப்பு அறநெறி", "அராஜகத்தின் இலக்கணம்", "மேல்-பூச்சு வர்ணனை"],
    ["Term for civil disobedience & satyagraha when constitutional remedies are open", "Way of life recognizing Liberty, Equality, and Fraternity as an inseparable trinity", "Ambedkar's remark that Indian democracy is only a surface coat on undemocratic soil", "Reverence for constitutional forms borrowed from historian George Grote"],
    ["அரசியலமைப்பு தீர்வுகள் உள்ள போது சட்டமறுப்பு & சத்தியாகிரகத்திற்கான சொல்", "சுதந்திரம், சமத்துவம், சகோதரத்துவத்தை பிரிக்க முடியாத திரித்துவமாகக் கொள்ளும் வாழ்க்கை முறை", "ஜனநாயகமற்ற மண்ணில் இந்திய ஜனநாயகம் ஒரு மேல்-பூச்சு மட்டுமே என்ற அம்பேத்கரின் வர்ணனை", "வரலாற்று ஆசிரியர் ஜார்ஜ் குரோட்டிடமிருந்து பெறப்பட்ட அரசியலமைப்பு வடிவங்கள் மீதான மரியாதை"],
    "A-2, B-4, C-1, D-3", "A-4, B-2, C-1, D-3", "A-2, B-1, C-4, D-3", "A-3, B-4, C-2, D-1",
    "A",
    "A-2: Social Democracy is a way of life recognizing Liberty, Equality, Fraternity as a trinity. B-4: Constitutional Morality is reverence for constitutional forms (George Grote). C-1: Grammar of Anarchy refers to unconstitutional agitations. D-3: Top-dressing describes democracy on undemocratic Indian soil.",
    "A-2: சமூக ஜனநாயகம் என்பது திரித்துவக் கோட்பாடு. B-4: அரசியலமைப்பு அறநெறி ஜார்ஜ் குரோட்டின் கோட்பாடு. C-1: அராஜகத்தின் இலக்கணம் என்பது சட்டமறுப்பு/சத்தியாகிரகம். D-3: மேல்-பூச்சு என்பது ஜனநாயகமற்ற மண்ணின் மீதான பூச்சு.",
    "Correct. A-2, B-4, C-1, D-3 is the exact correct matching.", "சரி. A-2, B-4, C-1, D-3 சரியான பொருத்தம்.",
    "Incorrect. Social Democracy is the trinity of Liberty-Equality-Fraternity (2), not George Grote concept (4).", "தவறு. சமூக ஜனநாயகம் என்பது திரித்துவக் கோட்பாடு (2).",
    "Incorrect. Grammar of Anarchy refers to unconstitutional agitations (1), not George Grote concept (4).", "தவறு. அராஜகத்தின் இலக்கணம் என்பது சட்டமறுப்பு (1).",
    "Incorrect. Social Democracy is the trinity (2), not top-dressing description (3).", "தவறு. சமூக ஜனநாயகம் என்பது திரித்துவக் கோட்பாடு (2).",
    "TNPSC Trap: All four concepts—Social Democracy, Constitutional Morality, Grammar of Anarchy, and Top-Dressing—were introduced by Dr. B.R. Ambedkar in his speeches.",
    "TNPSC பொறி: இந்த நான்கு கோட்பாடுகளையும் (சமூக ஜனநாயகம், அரசியலமைப்பு அறநெறி, அராஜகத்தின் இலக்கணம், மேல்-பூச்சு) டாக்டர் பி.ஆர். அம்பேத்கர் தனது உரைகளில் அறிமுகப்படுத்தினார்.",
    "Ambedkar insisted that without social democracy, political democracy cannot survive.",
    "சமூக ஜனநாயகம் இல்லாமல் அரசியல் ஜனநாயகம் நீடிக்க முடியாது என்று அம்பேத்கர் வலியுறுத்தினார்.",
    "Analyze", 75, ["Polity", "Making of Indian Constitution", "Ambedkar's Final Speech", "Constitutional Morality", "Grammar of Anarchy", "Social Democracy"]
))

# MIC_MF_025
questions.append(make_mf_q(
    "MIC_MF_025", "Match the Following",
    "Match List I (Pre-existing Statute / Constitutional Element) with List II (Status under Article 395 / CAD Enactment Sequence) and select the correct answer using the codes given below:\n\nList I\nA. Government of India Act, 1935\nB. Indian Independence Act, 1947\nC. Abolition of Privy Council Jurisdiction Act, 1949\nD. Preamble to the Constitution\n\nList II\n1. Repealed explicitly by Article 395 alongside GoI Act 1935\n2. Enacted LAST by the Assembly after the entire Constitution was voted upon\n3. Repealed explicitly by Article 395 of the Constitution\n4. EXCEPTED from repeal under Article 395 and preserved in force",
    "பட்டியல் I-ஐ (முந்தைய சட்டம் / அரசியலமைப்பு அம்சம்) பட்டியல் II உடன் (சரத்து 395 இன் கீழ் நிலை / CAD இயற்றல் வரிசை) பொருத்தி கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான பதிலதைத் தேர்ந்தெடுக்கவும்:\n\nபட்டியல் I\nA. 1935 இந்திய அரசுச் சட்டம்\nB. 1947 இந்திய சுதந்திரச் சட்டம்\nC. 1949 பிரிவி கவுன்சில் அதிகார வரம்பு ஒழிப்புச் சட்டம்\nD. அரசியலமைப்பின் முகப்புரை\n\nபட்டியல் II\n1. 1935 இந்திய அரசுச் சட்டத்துடன் சரத்து 395 ஆல் வெளிப்படையாக ரத்து செய்யப்பட்டது\n2. முழு அரசியலமைப்பும் வாக்களிக்கப்பட்ட பிறகு அவையால் கடைசியாக இயற்றப்பட்டது\n3. அரசியலமைப்பின் சரத்து 395 ஆல் வெளிப்படையாக ரத்து செய்யப்பட்டது\n4. சரத்து 395 இன் கீழ் ரத்து செய்வதிலிருந்து விலக்களிக்கப்பட்டு அமலில் பாதுகாக்கப்பட்டது",
    ["Government of India Act, 1935", "Indian Independence Act, 1947", "Abolition of Privy Council Jurisdiction Act, 1949", "Preamble to the Constitution"],
    ["1935 இந்திய அரசுச் சட்டம்", "1947 இந்திய சுதந்திரச் சட்டம்", "1949 பிரிவி கவுன்சில் அதிகார வரம்பு ஒழிப்புச் சட்டம்", "அரசியலமைப்பின் முகப்புரை"],
    ["Repealed explicitly by Article 395 alongside GoI Act 1935", "Enacted LAST by the Assembly after the entire Constitution was voted upon", "Repealed explicitly by Article 395 of the Constitution", "EXCEPTED from repeal under Article 395 and preserved in force"],
    ["1935 இந்திய அரசுச் சட்டத்துடன் சரத்து 395 ஆல் வெளிப்படையாக ரத்து செய்யப்பட்டது", "முழு அரசியலமைப்பும் வாக்களிக்கப்பட்ட பிறகு அவையால் கடைசியாக இயற்றப்பட்டது", "அரசியலமைப்பின் சரத்து 395 ஆல் வெளிப்படையாக ரத்து செய்யப்பட்டது", "சரத்து 395 இன் கீழ் ரத்து செய்வதிலிருந்து விலக்களிக்கப்பட்டு அமலில் பாதுகாக்கப்பட்டது"],
    "A-3, B-1, C-4, D-2", "A-1, B-3, C-2, D-4", "A-3, B-4, C-1, D-2", "A-2, B-1, C-4, D-3",
    "A",
    "A-3: GoI Act 1935 was explicitly repealed by Article 395. B-1: Indian Independence Act 1947 was explicitly repealed by Article 395. C-4: Abolition of Privy Council Jurisdiction Act 1949 was EXCEPTED from repeal. D-2: Preamble was enacted LAST.",
    "A-3: 1935 சட்டம் சரத்து 395 ஆல் ரத்து செய்யப்பட்டது. B-1: 1947 சுதந்திரச் சட்டம் சரத்து 395 ஆல் ரத்து செய்யப்பட்டது. C-4: 1949 பிரிவி கவுன்சில் சட்டம் ரத்திலிருந்து விலக்களிக்கப்பட்டது. D-2: முகப்புரை கடைசியாக இயற்றப்பட்டது.",
    "Correct. A-3, B-1, C-4, D-2 is the exact correct matching.", "சரி. A-3, B-1, C-4, D-2 சரியான பொருத்தம்.",
    "Incorrect. GoI Act 1935 was repealed (3), not enacted last (2).", "தவறு. 1935 சட்டம் சரத்து 395 ஆல் ரத்து செய்யப்பட்டது (3).",
    "Incorrect. Abolition of Privy Council Act was EXCEPTED from repeal (4), not repealed (1).", "தவறு. பிரிவி கவுன்சில் சட்டம் ரத்திலிருந்து விலக்கப்பட்டது (4).",
    "Incorrect. GoI Act 1935 was repealed (3), not enacted last (2).", "தவறு. 1935 சட்டம் சரத்து 395 ஆல் ரத்து செய்யப்பட்டது (3).",
    "TNPSC Trap: Article 395 repealed GoI Act 1935 & Indian Independence Act 1947, BUT explicitly preserved the Abolition of Privy Council Jurisdiction Act 1949.",
    "TNPSC பொறி: சரத்து 395 1935 இந்திய அரசுச் சட்டம் & 1947 சுதந்திரச் சட்டத்தை ரத்து செய்தது, ஆனால் 1949 பிரிவி கவுன்சில் ஒழிப்புச் சட்டத்தை வெளிப்படையாகப் பாதுகாத்தது.",
    "The Preamble was enacted last to ensure harmony with the finalized provisions of the Constitution.",
    "இறுதி செய்யப்பட்ட அரசியலமைப்பு விதிகளுடன் இணக்கத்தைப் பேணவே முகப்புரை கடைசியாக இயற்றப்பட்டது.",
    "Analyze", 75, ["Polity", "Making of Indian Constitution", "Enforcement of Constitution", "Adoption of Constitution", "Constitutional Facts"]
))
