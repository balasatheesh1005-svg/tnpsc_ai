# -*- coding: utf-8 -*-
"""
Builder for Part 1 of Constitutional Schedules (150 MCQs):
- 50 Easy MCQs (SCH_E_001 to SCH_E_050)
- 50 Medium MCQs (SCH_M_001 to SCH_M_050)
- 50 Hard MCQs (SCH_H_001 to SCH_H_050)
"""
import json
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.insert(0, os.path.dirname(__file__))

from sch_mcq_helper import make_sch_q, balance_question_keys

def get_easy_questions():
    qs = []
    
    # E01 - E10: Overview & Schedules 1 to 3
    qs.append(make_sch_q(
        "SCH_E_001", "Easy", "Conceptual", "Schedules Overview",
        "How many Schedules were there originally in the Constitution of India when it was adopted in 1949?",
        "1949-ல் ஏற்றுக்கொள்ளப்பட்ட இந்திய அரசியலமைப்பில் தொடக்கத்தில் எத்தனை அட்டவணைகள் இருந்தன?",
        "8 Schedules", "8 அட்டவணைகள்",
        "10 Schedules", "10 அட்டவணைகள்",
        "12 Schedules", "12 அட்டவணைகள்",
        "7 Schedules", "7 அட்டவணைகள்",
        "A",
        "The original Constitution of India adopted on November 26, 1949 contained 8 Schedules. Four more schedules (9th, 10th, 11th, and 12th) were added later by constitutional amendments, bringing the total to 12.",
        "1949 நவம்பர் 26 அன்று ஏற்றுக்கொள்ளப்பட்ட அசல் இந்திய அரசியலமைப்பில் 8 அட்டவணைகள் மட்டுமே இருந்தன. பின்னர் அரசியலமைப்புத் திருத்தங்கள் மூலம் நான்கு அட்டவணைகள் (9, 10, 11 மற்றும் 12) சேர்க்கப்பட்டு மொத்தம் 12 ஆக உயர்ந்தன.",
        "Correct. The original Constitution had exactly 8 Schedules.", "சரியானது. அசல் அரசியலமைப்பில் சரியாக 8 அட்டவணைகள் இருந்தன.",
        "Incorrect. 10 schedules was never the original count.", "தவறானது. தொடக்கத்தில் 10 அட்டவணைகள் இருக்கவில்லை.",
        "Incorrect. 12 is the current count, not the original count.", "தவறானது. 12 என்பது தற்போதைய எண்ணிக்கை, தொடக்க எண்ணிக்கை அல்ல.",
        "Incorrect. There were 8, not 7 schedules originally.", "தவறானது. தொடக்கத்தில் 7 அல்ல, 8 அட்டவணைகள் இருந்தன.",
        "Original: 8 Schedules. Current: 12 Schedules.",
        "தொடக்கத்தில்: 8 அட்டவணைகள். தற்போது: 12 அட்டவணைகள்.",
        "The 9th, 10th, 11th, and 12th Schedules were added by the 1st, 52nd, 73rd, and 74th Amendment Acts respectively.",
        "9, 10, 11 மற்றும் 12வது அட்டவணைகள் முறையே 1, 52, 73 மற்றும் 74வது திருத்தச் சட்டங்களால் சேர்க்கப்பட்டன."
    ))

    qs.append(make_sch_q(
        "SCH_E_002", "Easy", "Conceptual", "Schedules Overview",
        "How many Schedules are there in the Constitution of India at present?",
        "தற்போது இந்திய அரசியலமைப்பில் எத்தனை அட்டவணைகள் உள்ளன?",
        "12 Schedules", "12 அட்டவணைகள்",
        "8 Schedules", "8 அட்டவணைகள்",
        "10 Schedules", "10 அட்டவணைகள்",
        "14 Schedules", "14 அட்டவணைகள்",
        "A",
        "At present, the Constitution of India contains 12 Schedules.",
        "தற்போது இந்திய அரசியலமைப்பில் 12 அட்டவணைகள் உள்ளன.",
        "Correct. There are currently 12 Schedules.", "சரியானது. தற்போது 12 அட்டவணைகள் உள்ளன.",
        "Incorrect. 8 was the original count in 1950.", "தவறானது. 8 என்பது 1950-ல் இருந்த எண்ணிக்கை.",
        "Incorrect. 10 was the count before the 73rd and 74th amendments.", "தவறானது. 73 மற்றும் 74வது திருத்தங்களுக்கு முன்பு 10 அட்டவணைகள் இருந்தன.",
        "Incorrect. There are 12 schedules, not 14.", "தவறானது. 14 அல்ல, 12 அட்டவணைகளே உள்ளன.",
        "Current count is 12 Schedules.", "தற்போதைய அட்டவணைகளின் எண்ணிக்கை 12 ஆகும்.",
        "The 12th Schedule was added by the 74th Amendment Act in 1992.",
        "12வது அட்டவணை 1992-ல் 74வது திருத்தச் சட்டத்தின் மூலம் சேர்க்கப்பட்டது."
    ))

    qs.append(make_sch_q(
        "SCH_E_003", "Easy", "Conceptual", "First Schedule",
        "Which Schedule of the Indian Constitution specifies the names and territorial extent of States and Union Territories?",
        "இந்திய அரசியலமைப்பின் எந்த அட்டவணை மாநிலங்கள் மற்றும் யூனியன் பிரதேசங்களின் பெயர்கள் மற்றும் அவற்றின் எல்லைப் பகுதிகளைக் குறிப்பிடுகிறது?",
        "First Schedule", "முதல் அட்டவணை",
        "Second Schedule", "இரண்டாவது அட்டவணை",
        "Third Schedule", "மூன்றாவது அட்டவணை",
        "Fourth Schedule", "நான்காவது அட்டவணை",
        "A",
        "The First Schedule lists the names and territorial jurisdictions of the 28 States and 8 Union Territories of India.",
        "முதல் அட்டவணை இந்தியாவின் 28 மாநிலங்கள் மற்றும் 8 யூனியன் பிரதேசங்களின் பெயர்கள் மற்றும் அவற்றின் எல்லை அதிகார வரம்புகளைப் பட்டியலிடுகிறது.",
        "Correct. First Schedule lists States and Union Territories.", "சரியானது. முதல் அட்டவணை மாநிலங்கள் மற்றும் யூனியன் பிரதேசங்களைப் பட்டியலிடுகிறது.",
        "Incorrect. Second Schedule deals with salaries and allowances.", "தவறானது. இரண்டாவது அட்டவணை சம்பளங்கள் மற்றும் படிகளைக் கையாள்கிறது.",
        "Incorrect. Third Schedule deals with oaths and affirmations.", "தவறானது. மூன்றாவது அட்டவணை பிரமாணங்கள் மற்றும் உறுதியேற்புகளைக் கையாள்கிறது.",
        "Incorrect. Fourth Schedule deals with Rajya Sabha seat allocation.", "தவறானது. நான்காவது அட்டவணை மாநிலங்களவை இட ஒதுக்கீட்டைக் கையாள்கிறது.",
        "First Schedule = States & UTs (Articles 1 and 4).", "முதல் அட்டவணை = மாநிலங்கள் & யூனியன் பிரதேசங்கள் (உறுப்புகள் 1 மற்றும் 4).",
        "India currently comprises 28 States and 8 Union Territories listed in the First Schedule.",
        "இந்தியா தற்போது முதல் அட்டவணையில் பட்டியலிடப்பட்டுள்ள 28 மாநிலங்கள் மற்றும் 8 யூனியன் பிரதேசங்களைக் கொண்டுள்ளது."
    ))

    qs.append(make_sch_q(
        "SCH_E_004", "Easy", "Conceptual", "Second Schedule",
        "The Second Schedule of the Constitution of India deals with provisions relating to:",
        "இந்திய அரசியலமைப்பின் இரண்டாவது அட்டவணை எதனுடன் தொடர்புடைய விதிகளைக் கையாள்கிறது?",
        "Salaries, allowances, and pensions of constitutional authorities", "அரசியலமைப்பு அதிகார அமைப்புகளின் சம்பளம், படிகள் மற்றும் ஓய்வூதியங்கள்",
        "Forms of Oaths and Affirmations", "பதவிப் பிரமாணம் மற்றும் இரகசியக் காப்புப் பிரமாண படிவங்கள்",
        "Allocation of seats in the Rajya Sabha", "மாநிலங்களவை இடங்கள் ஒதுக்கீடு",
        "Administration of Scheduled Areas", "தாழ்த்தப்பட்ட மற்றும் பழங்குடியினர் பகுதிகளின் நிர்வாகம்",
        "A",
        "The Second Schedule contains provisions relating to the salaries, allowances, privileges, and pensions of specified constitutional authorities.",
        "இரண்டாவது அட்டவணை குறிப்பிட்ட அரசியலமைப்பு அதிகார அமைப்புகளின் சம்பளங்கள், படிகள், சலுகைகள் மற்றும் ஓய்வூதியங்கள் தொடர்பான விதிகளைக் கொண்டுள்ளது.",
        "Correct. Second Schedule deals with salaries and allowances.", "சரியானது. இரண்டாவது அட்டவணை சம்பளங்கள் மற்றும் படிகளைக் கையாள்கிறது.",
        "Incorrect. Oaths are covered in the Third Schedule.", "தவறானது. பிரமாணங்கள் மூன்றாவது அட்டவணையில் உள்ளன.",
        "Incorrect. Rajya Sabha seats are in the Fourth Schedule.", "தவறானது. மாநிலங்களவை இடங்கள் நான்காவது அட்டவணையில் உள்ளன.",
        "Incorrect. Scheduled Areas are in the Fifth and Sixth Schedules.", "தவறானது. பழங்குடியினர் பகுதிகள் ஐந்து மற்றும் ஆறாவது அட்டவணைகளில் உள்ளன.",
        "Schedule 2 = Salaries; Schedule 3 = Oaths.", "அட்டவணை 2 = சம்பளங்கள்; அட்டவணை 3 = பிரமாணங்கள்.",
        "Second Schedule covers 9 specified categories of constitutional offices.",
        "இரண்டாவது அட்டவணை 9 குறிப்பிட்ட அரசியலமைப்பு பதவிகளை உள்ளடக்கியது."
    ))

    qs.append(make_sch_q(
        "SCH_E_005", "Easy", "Conceptual", "Third Schedule",
        "Forms of Oaths or Affirmations for constitutional functionaries are contained in which Schedule?",
        "அரசியலமைப்புப் பதவிகளுக்கான பதவிப் பிரமாணம் அல்லது உறுதியேற்பு படிவங்கள் எந்த அட்டவணையில் உள்ளன?",
        "Third Schedule", "மூன்றாவது அட்டவணை",
        "Second Schedule", "இரண்டாவது அட்டவணை",
        "Fourth Schedule", "நான்காவது அட்டவணை",
        "Fifth Schedule", "ஐந்தாவது அட்டவணை",
        "A",
        "The Third Schedule contains forms of oaths or affirmations for Ministers, candidates for elections, Members of Parliament/Legislatures, Judges of SC/HC, and the CAG.",
        "மூன்றாவது அட்டவணை அமைச்சர்கள், தேர்தல் வேட்பாளர்கள், நாடாளுமன்ற/சட்டமன்ற உறுப்பினர்கள், உச்ச/உயர் நீதிமன்ற நீதிபதிகள் மற்றும் சி.ஏ.ஜி ஆகியோருக்கான பிரமாண படிவங்களைக் கொண்டுள்ளது.",
        "Correct. Third Schedule contains forms of oaths and affirmations.", "சரியானது. மூன்றாவது அட்டவணை பிரமாண படிவங்களைக் கொண்டுள்ளது.",
        "Incorrect. Second Schedule contains salaries.", "தவறானது. இரண்டாவது அட்டவணையில் சம்பளங்கள் உள்ளன.",
        "Incorrect. Fourth Schedule contains Rajya Sabha seats.", "தவறானது. நான்காவது அட்டவணையில் மாநிலங்களவை இடங்கள் உள்ளன.",
        "Incorrect. Fifth Schedule contains Scheduled Areas administration.", "தவறானது. ஐந்தாவது அட்டவணையில் பழங்குடியினர் பகுதி நிர்வாகம் உள்ளது.",
        "Schedule 3 = Oaths (Third Schedule).", "அட்டவணை 3 = பிரமாணங்கள் (மூன்றாவது அட்டவணை).",
        "The President, Vice-President, and Governor oaths are in Articles 60, 69, and 159 respectively, NOT in the Third Schedule.",
        "குடியரசுத் தலைவர், துணைத் தலைவர் மற்றும் ஆளுநர் பிரமாணங்கள் முறையே உறுப்புகள் 60, 69 மற்றும் 159-ல் உள்ளன, மூன்றாவது அட்டவணையில் இல்லை."
    ))

    qs.append(make_sch_q(
        "SCH_E_006", "Easy", "Conceptual", "Fourth Schedule",
        "Allocation of seats in the Council of States (Rajya Sabha) to States and Union Territories is specified in the:",
        "மாநிலங்கள் மற்றும் யூனியன் பிரதேசங்களுக்கு மாநிலங்களவை (Council of States) இடங்கள் ஒதுக்கீடு எதில் குறிப்பிடப்பட்டுள்ளது?",
        "Fourth Schedule", "நான்காவது அட்டவணை",
        "Third Schedule", "மூன்றாவது அட்டவணை",
        "Fifth Schedule", "ஐந்தாவது அட்டவணை",
        "Sixth Schedule", "ஆறாவது அட்டவணை",
        "A",
        "The Fourth Schedule specifies the allocation of seats in the Rajya Sabha to each State and Union Territory under Articles 4(1) and 80(2).",
        "நான்காவது அட்டவணை உறுப்புகள் 4(1) மற்றும் 80(2)-ன் கீழ் ஒவ்வொரு மாநிலம் மற்றும் யூனியன் பிரதேசத்திற்கான மாநிலங்களவை இட ஒதுக்கீட்டைக் குறிப்பிடுகிறது.",
        "Correct. Fourth Schedule governs Rajya Sabha seat allocation.", "சரியானது. நான்காவது அட்டவணை மாநிலங்களவை இட ஒதுக்கீட்டைக் குறிக்கிறது.",
        "Incorrect. Third Schedule is for oaths.", "தவறானது. மூன்றாவது அட்டவணை பிரமாணங்களுக்கானது.",
        "Incorrect. Fifth Schedule is for scheduled areas.", "தவறானது. ஐந்தாவது அட்டவணை பழங்குடி பகுதிகளுக்கானது.",
        "Incorrect. Sixth Schedule is for northeastern tribal areas.", "தவறானது. ஆறாவது அட்டவணை வடகிழக்கு பழங்குடி பகுதிகளுக்கானது.",
        "Fourth Schedule = Rajya Sabha seats allocation.", "நான்காவது அட்டவணை = மாநிலங்களவை இடங்கள் ஒதுக்கீடு.",
        "Uttar Pradesh has the highest number of Rajya Sabha seats (31), while Tamil Nadu has 18 seats.",
        "உத்தரப் பிரதேசம் அதிகபட்ச மாநிலங்களவை இடங்களைக் கொண்டுள்ளது (31), தமிழ்நாட்டிற்கு 18 இடங்கள் உள்ளன."
    ))

    qs.append(make_sch_q(
        "SCH_E_007", "Easy", "Conceptual", "Fifth Schedule",
        "The Fifth Schedule of the Constitution of India deals with the administration and control of:",
        "இந்திய அரசியலமைப்பின் ஐந்தாவது அட்டவணை எவற்றின் நிர்வாகம் மற்றும் கட்டுப்பாட்டைக் கையாள்கிறது?",
        "Scheduled Areas and Scheduled Tribes in states other than Assam, Meghalaya, Tripura, and Mizoram", "அசாம், மேகாலயா, திரிபுரா மற்றும் மிசோரம் தவிர பிற மாநிலங்களில் உள்ள தாழ்த்தப்பட்ட மற்றும் பழங்குடியினர் பகுதிகள்",
        "Tribal Areas in Assam, Meghalaya, Tripura, and Mizoram only", "அசாம், மேகாலயா, திரிபுரா மற்றும் மிசோரம் மாநிலங்களில் உள்ள பழங்குடியினர் பகுதிகள் மட்டுமே",
        "Municipalities and urban local governance", "நகராட்சிகள் மற்றும் நகர்ப்புற உள்ளாட்சி நிர்வாகம்",
        "Panchayati Raj institutions", "பஞ்சாயத்து ராஜ் அமைப்புகள்",
        "A",
        "The Fifth Schedule contains provisions regarding the administration and control of Scheduled Areas and Scheduled Tribes in any State other than the four northeastern states of Assam, Meghalaya, Tripura, and Mizoram.",
        "ஐந்தாவது அட்டவணை அசாம், மேகாலயா, திரிபுரா மற்றும் மிசோரம் ஆகிய நான்கு வடகிழக்கு மாநிலங்களைத் தவிர மற்ற மாநிலங்களில் உள்ள தாழ்த்தப்பட்ட மற்றும் பழங்குடியினர் பகுதிகளின் நிர்வாகத்தைக் கையாள்கிறது.",
        "Correct. Fifth Schedule applies to 10 states outside AMTM.", "சரியானது. ஐந்தாவது அட்டவணை AMTM அல்லாத 10 மாநிலங்களுக்குப் பொருந்தும்.",
        "Incorrect. AMTM is covered by the Sixth Schedule.", "தவறானது. AMTM ஆறாவது அட்டவணையில் உள்ளது.",
        "Incorrect. Municipalities are under Twelfth Schedule.", "தவறானது. நகராட்சிகள் 12வது அட்டவணையில் உள்ளன.",
        "Incorrect. Panchayats are under Eleventh Schedule.", "தவறானது. பஞ்சாயத்துகள் 11வது அட்டவணையில் உள்ளன.",
        "Fifth Schedule = Scheduled Areas (Article 244(1)).", "ஐந்தாவது அட்டவணை = திட்டமிடப்பட்ட பகுதிகள் (உறுப்பு 244(1)).",
        "A Tribes Advisory Council (TAC) of up to 20 members is established in Fifth Schedule states.",
        "ஐந்தாவது அட்டவணை மாநிலங்களில் 20 உறுப்பினர்கள் வரை கொண்ட பழங்குடியினர் ஆலோசனைக் குழு (TAC) அமைக்கப்படுகிறது."
    ))

    qs.append(make_sch_q(
        "SCH_E_008", "Easy", "Conceptual", "Sixth Schedule",
        "The Sixth Schedule of the Indian Constitution applies to the administration of tribal areas in which group of States?",
        "இந்திய அரசியலமைப்பின் ஆறாவது அட்டவணை எந்த மாநிலங்களின் பழங்குடியினர் பகுதிகளின் நிர்வாகத்திற்குப் பொருந்தும்?",
        "Assam, Meghalaya, Tripura, and Mizoram", "அசாம், மேகாலயா, திரிபுரா மற்றும் மிசோரம்",
        "Assam, Manipur, Nagaland, and Tripura", "அசாம், மணிப்பூர், நாகாலாந்து மற்றும் திரிபுரா",
        "Arunachal Pradesh, Nagaland, Manipur, and Mizoram", "அருணாச்சலப் பிரதேசம், நாகாலாந்து, மணிப்பூர் மற்றும் மிசோரம்",
        "Meghalaya, Manipur, Mizoram, and Nagaland", "மேகாலயா, மணிப்பூர், மிசோரம் மற்றும் நாகாலாந்து",
        "A",
        "The Sixth Schedule applies exclusively to the tribal areas in the four states of Assam, Meghalaya, Tripura, and Mizoram (AMTM) under Articles 244(2) and 275(1).",
        "ஆறாவது அட்டவணை உறுப்புகள் 244(2) மற்றும் 275(1)-ன் கீழ் அசாம், மேகாலயா, திரிபுரா மற்றும் மிசோரம் (AMTM) ஆகிய நான்கு மாநிலங்களில் உள்ள பழங்குடியினர் பகுதிகளுக்கு மட்டுமே பொருந்தும்.",
        "Correct. Sixth Schedule applies to AMTM states.", "சரியானது. ஆறாவது அட்டவணை AMTM மாநிலங்களுக்குப் பொருந்தும்.",
        "Incorrect. Manipur and Nagaland are NOT in the Sixth Schedule.", "தவறானது. மணிப்பூர் மற்றும் நாகாலாந்து 6வது அட்டவணையில் இல்லை.",
        "Incorrect. Arunachal Pradesh is not in Sixth Schedule.", "தவறானது. அருணாச்சலப் பிரதேசம் 6வது அட்டவணையில் இல்லை.",
        "Incorrect. Manipur is excluded from Sixth Schedule.", "தவறானது. மணிப்பூர் 6வது அட்டவணையில் சேர்க்கப்படவில்லை.",
        "Mnemonic for Sixth Schedule states: AMTM (Assam, Meghalaya, Tripura, Mizoram).",
        "ஆறாவது அட்டவணை மாநிலங்களுக்கான நினைவுக் குறியீடு: AMTM (அசாம், மேகாலயா, திரிபுரா, மிசோரம்).",
        "Sixth Schedule creates Autonomous District Councils (ADCs) with up to 30 members.",
        "ஆறாவது அட்டவணை 30 உறுப்பினர்கள் வரை கொண்ட தன்னாட்சி மாவட்டக் குழுக்களை (ADCs) உருவாக்குகிறது."
    ))

    qs.append(make_sch_q(
        "SCH_E_009", "Easy", "Conceptual", "Seventh Schedule",
        "The division of powers between the Union and the States into three lists (Union, State, Concurrent) is found in the:",
        "மத்திய மற்றும் மாநில அரசுகளுக்கு இடையிலான அதிகாரப் பகிர்வு மூன்று பட்டியல்களாக (மத்திய, மாநில, பொது) எந்த அட்டவணையில் உள்ளது?",
        "Seventh Schedule", "ஏழாவது அட்டவணை",
        "Eighth Schedule", "எட்டாவது அட்டவணை",
        "Sixth Schedule", "ஆறாவது அட்டவணை",
        "Ninth Schedule", "ஒன்பதாவது அட்டவணை",
        "A",
        "The Seventh Schedule under Article 246 divides legislative subjects into three lists: List I (Union List), List II (State List), and List III (Concurrent List).",
        "ஏழாவது அட்டவணை உறுப்பு 246-ன் கீழ் சட்டமன்ற அதிகாரங்களை மூன்று பட்டியல்களாகப் பிரிக்கிறது: பட்டியல் I (மத்தியப் பட்டியல்), பட்டியல் II (மாநிலப் பட்டியல்), மற்றும் பட்டியல் III (பொதுப் பட்டியல்).",
        "Correct. Seventh Schedule contains the 3 legislative lists.", "சரியானது. ஏழாவது அட்டவணையில் 3 அதிகாரப் பட்டியல்கள் உள்ளன.",
        "Incorrect. Eighth Schedule is for languages.", "தவறானது. எட்டாவது அட்டவணை மொழிகளுக்கானது.",
        "Incorrect. Sixth Schedule is for northeastern tribal areas.", "தவறானது. ஆறாவது அட்டவணை வடகிழக்கு பழங்குடி பகுதிகளுக்கானது.",
        "Incorrect. Ninth Schedule is for land reform validations.", "தவறானது. ஒன்பதாவது அட்டவணை நிலச் சீர்திருத்தப் பாதுகாப்பிற்கானது.",
        "Seventh Schedule = Division of Powers (3 Lists: Union, State, Concurrent).",
        "ஏழாவது அட்டவணை = அதிகாரப் பகிர்வு (3 பட்டியல்கள்: மத்திய, மாநில, பொது).",
        "Residuary powers under Article 248 vest in the Union Parliament.",
        "உறுப்பு 248-ன் கீழ் எஞ்சிய அதிகாரங்கள் மத்திய நாடாளுமன்றத்திற்கு மட்டுமே உள்ளன."
    ))

    qs.append(make_sch_q(
        "SCH_E_010", "Easy", "Conceptual", "Eighth Schedule",
        "How many official languages are currently recognized in the Eighth Schedule of the Indian Constitution?",
        "தற்போது இந்திய அரசியலமைப்பின் எட்டாவது அட்டவணையில் அங்கீகரிக்கப்பட்டுள்ள அதிகாரப்பூர்வ மொழிகள் எத்தனை?",
        "22 languages", "22 மொழிகள்",
        "14 languages", "14 மொழிகள்",
        "18 languages", "18 மொழிகள்",
        "25 languages", "25 மொழிகள்",
        "A",
        "Currently, there are 22 official languages recognized in the Eighth Schedule of the Constitution of India.",
        "தற்போது இந்திய அரசியலமைப்பின் எட்டாவது அட்டவணையில் 22 அதிகாரப்பூர்வ மொழிகள் அங்கீகரிக்கப்பட்டுள்ளன.",
        "Correct. There are currently 22 languages in the Eighth Schedule.", "சரியானது. தற்போது எட்டாவது அட்டவணையில் 22 மொழிகள் உள்ளன.",
        "Incorrect. 14 was the original number of languages in 1950.", "தவறானது. 14 என்பது 1950-ல் இருந்த தொடக்க எண்ணிக்கை.",
        "Incorrect. 18 was the number after the 71st amendment (1992).", "தவறானது. 18 என்பது 71வது திருத்தத்திற்கு (1992) பிந்தைய எண்ணிக்கை.",
        "Incorrect. There are 22 languages, not 25.", "தவறானது. 25 அல்ல, 22 மொழிகளே உள்ளன.",
        "Original: 14 languages. Current: 22 languages.",
        "தொடக்கத்தில்: 14 மொழிகள். தற்போது: 22 மொழிகள்.",
        "English is NOT recognized in the Eighth Schedule.",
        "ஆங்கிலம் எட்டாவது அட்டவணையில் இடம்பெறவில்லை."
    ))

    # E11 - E20: Schedules 9 to 12 & Basic Facts
    qs.append(make_sch_q(
        "SCH_E_011", "Easy", "Conceptual", "Ninth Schedule",
        "The Ninth Schedule was introduced into the Constitution of India by which Constitutional Amendment Act?",
        "இந்திய அரசியலமைப்பில் ஒன்பதாவது அட்டவணை எந்த அரசியலமைப்புத் திருத்தச் சட்டத்தின் மூலம் அறிமுகப்படுத்தப்பட்டது?",
        "1st Constitutional Amendment Act, 1951", "1வது அரசியலமைப்புத் திருத்தச் சட்டம், 1951",
        "42nd Constitutional Amendment Act, 1976", "42வது அரசியலமைப்புத் திருத்தச் சட்டம், 1976",
        "44th Constitutional Amendment Act, 1978", "44வது அரசியலமைப்புத் திருத்தச் சட்டம், 1978",
        "52nd Constitutional Amendment Act, 1985", "52வது அரசியலமைப்புத் திருத்தச் சட்டம், 1985",
        "A",
        "The Ninth Schedule along with Article 31B was added to the Constitution by the First Constitutional Amendment Act, 1951 to protect land reform laws from judicial review.",
        "நிலச் சீர்திருத்தச் சட்டங்களை நீதிமன்ற மறுஆய்விலிருந்து பாதுகாப்பதற்காக 1951-ல் 1வது அரசியலமைப்புத் திருத்தச் சட்டம் மூலம் உறுப்பு 31B உடன் ஒன்பதாவது அட்டவணை சேர்க்கப்பட்டது.",
        "Correct. 1st CAA 1951 added Ninth Schedule.", "சரியானது. 1வது திருத்தச் சட்டம் 1951 ஒன்பதாவது அட்டவணையைச் சேர்த்தது.",
        "Incorrect. 42nd CAA added fundamental duties, not 9th schedule.", "தவறானது. 42வது திருத்தம் அடிப்படைக் கடமைகளைச் சேர்த்தது.",
        "Incorrect. 44th CAA restored civil liberties post-emergency.", "தவறானது. 44வது திருத்தம் அவசரநிலைக்குப் பின் உரிமைகளை மீட்டது.",
        "Incorrect. 52nd CAA added Tenth Schedule.", "தவறானது. 52வது திருத்தம் 10வது அட்டவணையைச் சேர்த்தது.",
        "Ninth Schedule was added by the First Amendment in 1951 (Prime Minister: Jawaharlal Nehru).",
        "ஒன்பதாவது அட்டவணை 1951-ல் முதல் திருத்தத்தால் சேர்க்கப்பட்டது (பிரதமர்: ஜவஹர்லால் நேரு).",
        "The Tamil Nadu 69% Reservation Act of 1994 is placed in the Ninth Schedule.",
        "1994-ன் தமிழ்நாடு 69% இடஒதுக்கீட்டுச் சட்டம் ஒன்பதாவது அட்டவணையில் வைக்கப்பட்டுள்ளது."
    ))

    qs.append(make_sch_q(
        "SCH_E_012", "Easy", "Conceptual", "Tenth Schedule",
        "The Tenth Schedule of the Constitution of India is popularly known as the:",
        "இந்திய அரசியலமைப்பின் பத்தாவது அட்டவணை பொதுவாக எவ்வாறு அழைக்கப்படுகிறது?",
        "Anti-Defection Law", "கட்சித் தாவல் தடைச் சட்டம்",
        "Panchayati Raj Act", "பஞ்சாயத்து ராஜ் சட்டம்",
        "Right to Education Act", "கல்வி உரிமைச் சட்டம்",
        "Official Languages Act", "அலுவல் மொழிகள் சட்டம்",
        "A",
        "The Tenth Schedule contains provisions regarding the disqualification of members of Parliament and State Legislatures on grounds of defection, commonly called the Anti-Defection Law.",
        "பத்தாவது அட்டவணை கட்சித் தாவல் அடிப்படையில் நாடாளுமன்ற மற்றும் சட்டமன்ற உறுப்பினர்களைத் தகுதி நீக்கம் செய்வது தொடர்பான விதிகளைக் கொண்டுள்ளது; இது பொதுவாக கட்சித் தாவல் தடைச் சட்டம் என அழைக்கப்படுகிறது.",
        "Correct. Tenth Schedule is the Anti-Defection Law.", "சரியானது. பத்தாவது அட்டவணை கட்சித் தாவல் தடைச் சட்டம் ஆகும்.",
        "Incorrect. Panchayats are in the Eleventh Schedule.", "தவறானது. பஞ்சாயத்துகள் பதினோராவது அட்டவணையில் உள்ளன.",
        "Incorrect. Right to Education is under Article 21A.", "தவறானது. கல்வி உரிமை உறுப்பு 21A-ன் கீழ் உள்ளது.",
        "Incorrect. Official Languages are in the Eighth Schedule.", "தவறானது. அலுவல் மொழிகள் எட்டாவது அட்டவணையில் உள்ளன.",
        "Tenth Schedule = Anti-Defection Law (added by 52nd CAA 1985).",
        "பத்தாவது அட்டவணை = கட்சித் தாவல் தடைச் சட்டம் (52வது திருத்தம் 1985-ல் சேர்க்கப்பட்டது).",
        "Articles 102(2) and 191(2) govern disqualification under the Tenth Schedule.",
        "உறுப்புகள் 102(2) மற்றும் 191(2) பத்தாவது அட்டவணையின் கீழ் தகுதிநீக்கத்தைக் கட்டுப்படுத்துகின்றன."
    ))

    qs.append(make_sch_q(
        "SCH_E_013", "Easy", "Conceptual", "Tenth Schedule",
        "Which Constitutional Amendment Act added the Tenth Schedule (Anti-Defection Law) to the Constitution?",
        "எந்த அரசியலமைப்புத் திருத்தச் சட்டம் பத்தாவது அட்டவணையை (கட்சித் தாவல் தடைச் சட்டம்) அரசியலமைப்பில் சேர்த்தது?",
        "52nd Amendment Act, 1985", "52வது திருத்தச் சட்டம், 1985",
        "42nd Amendment Act, 1976", "42வது திருத்தச் சட்டம், 1976",
        "44th Amendment Act, 1978", "44வது திருத்தச் சட்டம், 1978",
        "61st Amendment Act, 1988", "61வது திருத்தச் சட்டம், 1988",
        "A",
        "The 52nd Constitutional Amendment Act, 1985 added the Tenth Schedule to the Constitution during the prime ministership of Rajiv Gandhi.",
        "ராஜீவ் காந்தி பிரதமராக இருந்தபோது 1985-ல் 52வது அரசியலமைப்புத் திருத்தச் சட்டம் மூலம் பத்தாவது அட்டவணை அரசியலமைப்பில் சேர்க்கப்பட்டது.",
        "Correct. 52nd CAA 1985 added the Tenth Schedule.", "சரியானது. 52வது திருத்தச் சட்டம் 1985 பத்தாவது அட்டவணையைச் சேர்த்தது.",
        "Incorrect. 42nd CAA was enacted in 1976.", "தவறானது. 42வது திருத்தம் 1976-ல் இயற்றப்பட்டது.",
        "Incorrect. 44th CAA was enacted in 1978.", "தவறானது. 44வது திருத்தம் 1978-ல் இயற்றப்பட்டது.",
        "Incorrect. 61st CAA reduced voting age to 18 in 1988.", "தவறானது. 61வது திருத்தம் 1988-ல் வாக்குரிமை வயதை 18 ஆகக் குறைத்தது.",
        "52nd CAA 1985 = Anti-Defection (Tenth Schedule).", "52வது திருத்தம் 1985 = கட்சித் தாவல் தடை (10வது அட்டவணை).",
        "The 91st Amendment Act 2003 omitted the 1/3rd split protection from the Tenth Schedule.",
        "91வது திருத்தச் சட்டம் 2003 பத்தாவது அட்டவணையில் இருந்த 1/3 பிரிவுப் பாதுகாப்பை நீக்கியது."
    ))

    qs.append(make_sch_q(
        "SCH_E_014", "Easy", "Conceptual", "Eleventh Schedule",
        "The Eleventh Schedule of the Constitution of India deals with:",
        "இந்திய அரசியலமைப்பின் பதினோராவது அட்டவணை எதைக் கையாள்கிறது?",
        "Powers, authority, and responsibilities of Panchayats (29 subjects)", "பஞ்சாயத்துகளின் அதிகாரங்கள் மற்றும் பொறுப்புகள் (29 துறைகள்)",
        "Powers, authority, and responsibilities of Municipalities (18 subjects)", "நகராட்சிகளின் அதிகாரங்கள் மற்றும் பொறுப்புகள் (18 துறைகள்)",
        "Anti-Defection provisions", "கட்சித் தாவல் தடை விதிகள்",
        "Official Languages", "அதிகாரப்பூர்வ மொழிகள்",
        "A",
        "The Eleventh Schedule, added by the 73rd Constitutional Amendment Act, 1992, lists 29 functional items placed under the jurisdiction of Panchayats under Article 243G.",
        "73வது அரசியலமைப்புத் திருத்தச் சட்டம் 1992 மூலம் சேர்க்கப்பட்ட பதினோராவது அட்டவணை, உறுப்பு 243G-ன் கீழ் பஞ்சாயத்துகளின் அதிகார வரம்பிற்குள் 29 செயல்பாட்டுத் துறைகளைப் பட்டியலிடுகிறது.",
        "Correct. Eleventh Schedule covers Panchayats (29 subjects).", "சரியானது. 11வது அட்டவணை பஞ்சாயத்துகளைக் (29 துறைகள்) கையாள்கிறது.",
        "Incorrect. Municipalities are under Twelfth Schedule.", "தவறானது. நகராட்சிகள் 12வது அட்டவணையில் உள்ளன.",
        "Incorrect. Anti-defection is under Tenth Schedule.", "தவறானது. கட்சித் தாவல் 10வது அட்டவணையில் உள்ளது.",
        "Incorrect. Official Languages are under Eighth Schedule.", "தவறானது. அலுவல் மொழிகள் 8வது அட்டவணையில் உள்ளன.",
        "Eleventh Schedule = Panchayats (29 subjects, Article 243G, 73rd CAA).",
        "11வது அட்டவணை = பஞ்சாயத்துகள் (29 துறைகள், உறுப்பு 243G, 73வது திருத்தம்).",
        "Mnemonic: 2 + 9 = 11 (29 subjects in 11th Schedule).",
        "நினைவுக் குறிப்பு: 2 + 9 = 11 (11வது அட்டவணையில் 29 துறைகள்)."
    ))

    qs.append(make_sch_q(
        "SCH_E_015", "Easy", "Conceptual", "Twelfth Schedule",
        "How many functional subjects are listed in the Twelfth Schedule of the Indian Constitution for Municipalities?",
        "இந்திய அரசியலமைப்பின் பன்னிரண்டாவது அட்டவணையில் நகராட்சிகளுக்காக எத்தனை செயல்பாட்டுத் துறைகள் பட்டியலிடப்பட்டுள்ளன?",
        "18 functional subjects", "18 செயல்பாட்டுத் துறைகள்",
        "29 functional subjects", "29 செயல்பாட்டுத் துறைகள்",
        "22 functional subjects", "22 செயல்பாட்டுத் துறைகள்",
        "12 functional subjects", "12 செயல்பாட்டுத் துறைகள்",
        "A",
        "The Twelfth Schedule, added by the 74th Amendment Act, 1992, specifies 18 functional matters for Municipalities under Article 243W.",
        "74வது திருத்தச் சட்டம் 1992 மூலம் சேர்க்கப்பட்ட பன்னிரண்டாவது அட்டவணை, உறுப்பு 243W-ன் கீழ் நகராட்சிகளுக்கான 18 செயல்பாட்டுத் துறைகளைக் குறிப்பிடுகிறது.",
        "Correct. Twelfth Schedule lists 18 subjects for Municipalities.", "சரியானது. 12வது அட்டவணை நகராட்சிகளுக்கான 18 துறைகளைப் பட்டியலிடுகிறது.",
        "Incorrect. 29 subjects are for Panchayats in Eleventh Schedule.", "தவறானது. 29 துறைகள் 11வது அட்டவணையில் பஞ்சாயத்துகளுக்கானவை.",
        "Incorrect. 22 is the number of languages in Eighth Schedule.", "தவறானது. 22 என்பது 8வது அட்டவணையில் உள்ள மொழிகளின் எண்ணிக்கை.",
        "Incorrect. 12 is the number of schedules in the Constitution.", "தவறானது. 12 என்பது அட்டவணைகளின் மொத்த எண்ணிக்கை.",
        "Panchayats = 29 subjects (11th Schedule); Municipalities = 18 subjects (12th Schedule).",
        "பஞ்சாயத்துகள் = 29 துறைகள் (11வது அட்டவணை); நகராட்சிகள் = 18 துறைகள் (12வது அட்டவணை).",
        "Article 243W governs the powers and authority of Municipalities listed in Twelfth Schedule.",
        "உறுப்பு 243W பன்னிரண்டாவது அட்டவணையில் உள்ள நகராட்சிகளின் அதிகாரங்களை நிர்வகிக்கிறது."
    ))

    # E16 - E30: Schedules 1-8 Specifics
    qs.append(make_sch_q(
        "SCH_E_016", "Easy", "Conceptual", "First Schedule",
        "Which article of the Indian Constitution states that laws altering the First Schedule are not deemed constitutional amendments under Article 368?",
        "இந்திய அரசியலமைப்பின் எந்த உறுப்பு முதல் அட்டவணையை மாற்றும் சட்டங்கள் உறுப்பு 368-ன் கீழ் அரசியலமைப்புத் திருத்தங்களாகக் கருதப்படாது எனக் கூறுகிறது?",
        "Article 4(2)", "உறுப்பு 4(2)",
        "Article 1(1)", "உறுப்பு 1(1)",
        "Article 2", "உறுப்பு 2",
        "Article 368(1)", "உறுப்பு 368(1)",
        "A",
        "Article 4(2) explicitly provides that no law under Article 2 or Article 3 altering the First or Fourth Schedules shall be deemed to be an amendment of the Constitution for the purposes of Article 368.",
        "உறுப்பு 4(2) முதல் அல்லது நான்காவது அட்டவணையை மாற்றும் உறுப்பு 2 அல்லது 3-ன் கீழான எந்தவொரு சட்டமும் உறுப்பு 368-ன் நோக்கங்களுக்காக அரசியலமைப்புத் திருத்தமாகக் கருதப்படாது எனத் தெளிவாகக் கூறுகிறது.",
        "Correct. Article 4(2) provides exemption from Article 368.", "சரியானது. உறுப்பு 4(2) உறுப்பு 368-லிருந்து விலக்கு அளிக்கிறது.",
        "Incorrect. Article 1(1) defines India as a Union of States.", "தவறானது. உறுப்பு 1(1) இந்தியாவை மாநிலங்களின் ஒன்றியம் என வரையறுக்கிறது.",
        "Incorrect. Article 2 empowers Parliament to admit new states.", "தவறானது. உறுப்பு 2 புதிய மாநிலங்களைச் சேர்க்க அதிகாரம் அளிக்கிறது.",
        "Incorrect. Article 368 governs formal constitutional amendments.", "தவறானது. உறுப்பு 368 வழக்கமான அரசியலமைப்புத் திருத்தங்களை நிர்வகிக்கிறது.",
        "Article 4 = Simple majority for First and Fourth Schedule amendments.",
        "உறுப்பு 4 = முதல் மற்றும் நான்காவது அட்டவணை திருத்தங்களுக்கு எளிய பெரும்பான்மை போதுமானது.",
        "State reorganisation acts are passed by a simple majority in Parliament.",
        "மாநில மறுசீரமைப்புச் சட்டங்கள் நாடாளுமன்றத்தில் எளிய பெரும்பான்மையால் நிறைவேற்றப்படுகின்றன."
    ))

    qs.append(make_sch_q(
        "SCH_E_017", "Easy", "Conceptual", "Second Schedule",
        "Whose salary and allowances are NOT governed by the Second Schedule of the Indian Constitution?",
        "இந்திய அரசியலமைப்பின் இரண்டாவது அட்டவணையால் யாருடைய சம்பளம் மற்றும் படிகள் நிர்வகிக்கப்படவில்லை?",
        "Prime Minister of India", "இந்தியப் பிரதமர்",
        "President of India", "இந்தியக் குடியரசுத் தலைவர்",
        "Chief Justice of India", "இந்தியத் தலைமை நீதிபதி",
        "Comptroller and Auditor General of India", "இந்தியக் கணக்குத் தணிக்கைத் தலைவர் (CAG)",
        "A",
        "The Prime Minister and other Union Ministers are NOT included in the Second Schedule. Their salaries are determined by Parliament under Article 75(6).",
        "இந்தியப் பிரதமர் மற்றும் பிற மத்திய அமைச்சர்கள் இரண்டாவது அட்டவணையில் சேர்க்கப்படவில்லை. அவர்களின் சம்பளங்கள் உறுப்பு 75(6)-ன் கீழ் நாடாளுமன்றத்தால் தீர்மானிக்கப்படுகின்றன.",
        "Correct. Prime Minister is NOT in the Second Schedule.", "சரியானது. பிரதமர் இரண்டாவது அட்டவணையில் இடம்பெறவில்லை.",
        "Incorrect. President is included in the Second Schedule.", "தவறானது. குடியரசுத் தலைவர் இரண்டாவது அட்டவணையில் உள்ளார்.",
        "Incorrect. Chief Justice is included in the Second Schedule.", "தவறானது. தலைமை நீதிபதி இரண்டாவது அட்டவணையில் உள்ளார்.",
        "Incorrect. CAG is included in the Second Schedule.", "தவறானது. சி.ஏ.ஜி இரண்டாவது அட்டவணையில் உள்ளார்.",
        "TRAP: PM, Union Ministers, and MPs are NOT in the Second Schedule.",
        "பொறி: பிரதமர், மத்திய அமைச்சர்கள் மற்றும் எம்பிக்கள் 2வது அட்டவணையில் இல்லை.",
        "The Second Schedule covers 9 specified categories of constitutional dignitaries.",
        "இரண்டாவது அட்டவணை 9 குறிப்பிட்ட வகை அரசியலமைப்புப் பிரமுகர்களை உள்ளடக்கியது."
    ))

    qs.append(make_sch_q(
        "SCH_E_018", "Easy", "Conceptual", "Third Schedule",
        "Under which Article of the Constitution does the President of India take his oath, which is NOT included in the Third Schedule?",
        "அரசியலமைப்பின் எந்த உறுப்பின் கீழ் இந்தியக் குடியரசுத் தலைவர் மூன்றாவது அட்டவணையில் இல்லாத தனது பதவிப் பிரமாணத்தை ஏற்கிறார்?",
        "Article 60", "உறுப்பு 60",
        "Article 52", "உறுப்பு 52",
        "Article 56", "உறுப்பு 56",
        "Article 72", "உறுப்பு 72",
        "A",
        "The oath of the President of India is specifically provided in Article 60 of the Constitution itself and is NOT part of the Third Schedule.",
        "இந்தியக் குடியரசுத் தலைவரின் பதவிப் பிரமாணம் அரசியலமைப்பின் உறுப்பு 60-ல் தனியாகக் குறிப்பிடப்பட்டுள்ளது, அது மூன்றாவது அட்டவணையின் ஒரு பகுதியாக இல்லை.",
        "Correct. President takes oath under Article 60.", "சரியானது. குடியரசுத் தலைவர் உறுப்பு 60-ன் கீழ் பிரமாணம் ஏற்கிறார்.",
        "Incorrect. Article 52 states there shall be a President of India.", "தவறானது. உறுப்பு 52 இந்தியக் குடியரசுத் தலைவர் பதவி பற்றிக் கூறுகிறது.",
        "Incorrect. Article 56 deals with term of office of President.", "தவறானது. உறுப்பு 56 குடியரசுத் தலைவரின் பதவிக்காலத்தைக் கையாள்கிறது.",
        "Incorrect. Article 72 deals with pardoning powers.", "தவறானது. உறுப்பு 72 மன்னிப்பளிக்கும் அதிகாரங்களைக் கையாள்கிறது.",
        "President (Art 60), Vice-President (Art 69), Governor (Art 159) oaths are NOT in Third Schedule.",
        "குடியரசுத் தலைவர் (உறுப்பு 60), துணைத் தலைவர் (உறுப்பு 69), ஆளுநர் (உறுப்பு 159) பிரமாணங்கள் 3வது அட்டவணையில் இல்லை.",
        "The Chief Justice of India administers the oath to the President under Article 60.",
        "உறுப்பு 60-ன் கீழ் இந்தியத் தலைமை நீதிபதி குடியரசுத் தலைவருக்குப் பதவிப் பிரமாணம் செய்து வைக்கிறார்."
    ))

    qs.append(make_sch_q(
        "SCH_E_019", "Easy", "Conceptual", "Third Schedule",
        "The Oath of Secrecy in the Third Schedule is prescribed ONLY for which of the following?",
        "மூன்றாவது அட்டவணையில் உள்ள இரகசியக் காப்புப் பிரமாணம் பின்வருவனவற்றில் யாருக்கு மட்டுமே பரிந்துரைக்கப்பட்டுள்ளது?",
        "Union and State Ministers", "மத்திய மற்றும் மாநில அமைச்சர்கள்",
        "Members of Parliament", "நாடாளுமன்ற உறுப்பினர்கள்",
        "Judges of the Supreme Court", "உச்ச நீதிமன்ற நீதிபதிகள்",
        "Comptroller and Auditor General", "இந்தியக் கணக்குத் தணிக்கைத் தலைவர்",
        "A",
        "The Oath of Secrecy in the Third Schedule is taken exclusively by Ministers (both Union and State). MPs, MLAs, Judges, and the CAG take only the oath of office, not an oath of secrecy.",
        "மூன்றாவது அட்டவணையில் உள்ள இரகசியக் காப்புப் பிரமாணம் அமைச்சர்களால் மட்டுமே (மத்திய மற்றும் மாநில) ஏற்கப்படுகிறது. எம்பிக்கள், நீதிபதிகள் மற்றும் சி.ஏ.ஜி ஆகியோர் பதவிப் பிரமாணம் மட்டுமே ஏற்கின்றனர்.",
        "Correct. Only Ministers take Oath of Secrecy.", "சரியானது. அமைச்சர்கள் மட்டுமே இரகசியக் காப்புப் பிரமாணம் ஏற்கின்றனர்.",
        "Incorrect. MPs take oath of office, not secrecy.", "தவறானது. எம்பிக்கள் பதவிப் பிரமாணம் மட்டுமே ஏற்கின்றனர்.",
        "Incorrect. SC Judges take judicial oath, not secrecy.", "தவறானது. உச்ச நீதிமன்ற நீதிபதிகள் நீதித்துறை பிரமாணம் ஏற்கின்றனர்.",
        "Incorrect. CAG takes oath of office, not secrecy.", "தவறானது. சி.ஏ.ஜி பதவிப் பிரமாணம் மட்டுமே ஏற்கிறார்.",
        "Oath of Secrecy = Ministers ONLY.", "இரகசியக் காப்புப் பிரமாணம் = அமைச்சர்களுக்கு மட்டுமே.",
        "Ordinary legislators are not bound by an oath of secrecy to ensure legislative transparency.",
        "சட்டமன்ற வெளிப்படைத்தன்மையை உறுதிப்படுத்த சாதாரண உறுப்பினர்களுக்கு இரகசியப் பிரமாணம் இல்லை."
    ))

    qs.append(make_sch_q(
        "SCH_E_020", "Easy", "Conceptual", "Fourth Schedule",
        "Which State has the highest number of allocated seats in the Rajya Sabha according to the Fourth Schedule?",
        "நான்காவது அட்டவணையின்படி மாநிலங்களவையில் அதிக எண்ணிக்கையிலான இடங்கள் ஒதுக்கப்பட்டுள்ள மாநிலம் எது?",
        "Uttar Pradesh", "உத்தரப் பிரதேசம்",
        "Maharashtra", "மகாராஷ்டிரா",
        "Tamil Nadu", "தமிழ்நாடு",
        "West Bengal", "மேற்கு வங்கம்",
        "A",
        "Uttar Pradesh has the highest allocation with 31 seats in the Rajya Sabha, reflecting its large population.",
        "உத்தரப் பிரதேசம் அதிக மக்கள் தொகையைக் கொண்டிருப்பதால், மாநிலங்களவையில் அதிகபட்சமாக 31 இடங்களைப் பெற்றுள்ளது.",
        "Correct. UP has 31 seats, the highest in Rajya Sabha.", "சரியானது. உத்தரப் பிரதேசம் 31 இடங்களுடன் முதலிடத்தில் உள்ளது.",
        "Incorrect. Maharashtra has 19 seats (second highest).", "தவறானது. மகாராஷ்டிரா 19 இடங்களைக் கொண்டுள்ளது (இரண்டாவது இடம்).",
        "Incorrect. Tamil Nadu has 18 seats.", "தவறானது. தமிழ்நாடு 18 இடங்களைக் கொண்டுள்ளது.",
        "Incorrect. West Bengal has 16 seats.", "தவறானது. மேற்கு வங்கம் 16 இடங்களைக் கொண்டுள்ளது.",
        "Top Rajya Sabha seat allocations: UP (31), Maharashtra (19), Tamil Nadu (18).",
        "முக்கிய மாநிலங்களவை இடங்கள்: UP (31), மகாராஷ்டிரா (19), தமிழ்நாடு (18).",
        "Tamil Nadu shares the third spot with Bihar (16) and West Bengal (16) closely following with 18 seats.",
        "தமிழ்நாடு 18 இடங்களுடன் முக்கியப் பிரதிநிதித்துவம் பெற்றுள்ளது."
    ))

    # E21 - E35: Additional Easy MCQs covering all schedules
    qs.append(make_sch_q(
        "SCH_E_021", "Easy", "Conceptual", "Fourth Schedule",
        "How many seats are allocated to Tamil Nadu in the Rajya Sabha under the Fourth Schedule?",
        "நான்காவது அட்டவணையின் கீழ் மாநிலங்களவையில் தமிழ்நாட்டிற்கு எத்தனை இடங்கள் ஒதுக்கப்பட்டுள்ளன?",
        "18 seats", "18 இடங்கள்",
        "39 seats", "39 இடங்கள்",
        "31 seats", "31 இடங்கள்",
        "16 seats", "16 இடங்கள்",
        "A",
        "Tamil Nadu is allocated 18 seats in the Rajya Sabha (Council of States) under the Fourth Schedule.",
        "நான்காவது அட்டவணையின் கீழ் மாநிலங்களவையில் தமிழ்நாட்டிற்கு 18 இடங்கள் ஒதுக்கப்பட்டுள்ளன.",
        "Correct. Tamil Nadu has 18 Rajya Sabha seats.", "சரியானது. தமிழ்நாட்டிற்கு 18 மாநிலங்களவை இடங்கள் உள்ளன.",
        "Incorrect. 39 is the number of Lok Sabha seats from Tamil Nadu.", "தவறானது. 39 என்பது தமிழ்நாட்டின் மக்களவை இடங்கள்.",
        "Incorrect. 31 is the number of seats for Uttar Pradesh.", "தவறானது. 31 என்பது உத்தரப் பிரதேசத்தின் இடங்கள்.",
        "Incorrect. 16 is the number of seats for West Bengal and Bihar.", "தவறானது. 16 என்பது மேற்கு வங்கம் மற்றும் பீகாரின் இடங்கள்.",
        "Tamil Nadu: 18 Rajya Sabha seats, 39 Lok Sabha seats.", "தமிழ்நாடு: 18 மாநிலங்களவை இடங்கள், 39 மக்களவை இடங்கள்.",
        "Rajya Sabha members from Tamil Nadu are elected by the elected members of the Tamil Nadu Legislative Assembly.",
        "தமிழ்நாட்டு மாநிலங்களவை உறுப்பினர்கள் தமிழ்நாடு சட்டமன்றத்தின் தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்களால் தேர்ந்தெடுக்கப்படுகின்றனர்."
    ))

    qs.append(make_sch_q(
        "SCH_E_022", "Easy", "Conceptual", "Fifth Schedule",
        "What is the maximum number of members in the Tribes Advisory Council (TAC) constituted under the Fifth Schedule?",
        "ஐந்தாவது அட்டவணையின் கீழ் அமைக்கப்படும் பழங்குடியினர் ஆலோசனைக் குழுவில் (TAC) அதிகபட்ச உறுப்பினர்களின் எண்ணிக்கை யாது?",
        "20 members", "20 உறுப்பினர்கள்",
        "15 members", "15 உறுப்பினர்கள்",
        "30 members", "30 உறுப்பினர்கள்",
        "25 members", "25 உறுப்பினர்கள்",
        "A",
        "The Fifth Schedule provides that a Tribes Advisory Council shall consist of not more than 20 members, of whom at least three-fourths shall be representatives of Scheduled Tribes in the Legislative Assembly.",
        "ஐந்தாவது அட்டவணை பழங்குடியினர் ஆலோசனைக் குழுவில் 20 உறுப்பினர்களுக்கு மிகாமல் இருக்க வேண்டும் என்றும், அவர்களில் குறைந்தது நான்கில் மூன்று பங்கு உறுப்பினர்கள் சட்டமன்ற பழங்குடிப் பிரதிநிதிகளாக இருக்க வேண்டும் என்றும் கூறுகிறது.",
        "Correct. Maximum 20 members in TAC.", "சரியானது. TAC-ல் அதிகபட்சம் 20 உறுப்பினர்கள்.",
        "Incorrect. 15 is not the statutory maximum.", "தவறானது. 15 என்பது சட்டப்பூர்வ அதிகபட்ச வரம்பு அல்ல.",
        "Incorrect. 30 is the maximum strength of an ADC in the Sixth Schedule.", "தவறானது. 30 என்பது ஆறாவது அட்டவணை ADC உறுப்பினர்களின் எண்ணிக்கை.",
        "Incorrect. 25 is incorrect.", "தவறானது. 25 என்பது தவறானது.",
        "Fifth Schedule TAC = Max 20 members (3/4th ST MLAs).",
        "ஐந்தாவது அட்டவணை TAC = அதிகபட்சம் 20 உறுப்பினர்கள் (3/4 பங்கு ST எம்.எல்.ஏக்கள்).",
        "Tribes Advisory Council advises on welfare and advancement of Scheduled Tribes in the State.",
        "பழங்குடியினர் ஆலோசனைக் குழு மாநிலத்தில் உள்ள பழங்குடியினரின் நல்வாழ்வு குறித்து ஆலோசனை வழங்குகிறது."
    ))

    qs.append(make_sch_q(
        "SCH_E_023", "Easy", "Conceptual", "Sixth Schedule",
        "How many members are there in an Autonomous District Council (ADC) under the Sixth Schedule?",
        "ஆறாவது அட்டவணையின் கீழ் ஒரு தன்னாட்சி மாவட்டக் குழுவில் (ADC) எத்தனை உறுப்பினர்கள் உள்ளனர்?",
        "30 members", "30 உறுப்பினர்கள்",
        "20 members", "20 உறுப்பினர்கள்",
        "25 members", "25 உறுப்பினர்கள்",
        "40 members", "40 உறுப்பினர்கள்",
        "A",
        "Each Autonomous District Council under the Sixth Schedule consists of not more than 30 members (26 elected on adult franchise and 4 nominated by the Governor).",
        "ஆறாவது அட்டவணையின் கீழ் ஒவ்வொரு தன்னாட்சி மாவட்டக் குழுவிலும் 30 உறுப்பினர்களுக்கு மிகாமல் உள்ளனர் (26 பேர் வயதுவந்தோர் வாக்குரிமை மூலம் தேர்ந்தெடுக்கப்படுபவர்கள், 4 பேர் ஆளுநரால் நியமிக்கப்படுபவர்கள்).",
        "Correct. ADCs have 30 members (26 elected, 4 nominated).", "சரியானது. ADC-ல் 30 உறுப்பினர்கள் (26 தேர்ந்தெடுக்கப்பட்டவர்கள், 4 நியமிக்கப்பட்டவர்கள்).",
        "Incorrect. 20 is the TAC strength in Fifth Schedule.", "தவறானது. 20 என்பது ஐந்தாவது அட்டவணை TAC உறுப்பினர்களின் எண்ணிக்கை.",
        "Incorrect. 25 is incorrect.", "தவறானது. 25 என்பது தவறானது.",
        "Incorrect. Bodoland Territorial Council has 46 members by special amendment, but general ADC strength is 30.", "தவறானது. போடோலாந்து சிறப்பு விதியால் 46 உறுப்பினர்களைக் கொண்டது, பொதுவான ADC வரம்பு 30.",
        "Sixth Schedule ADC = 30 members (26 elected + 4 nominated).",
        "ஆறாவது அட்டவணை ADC = 30 உறுப்பினர்கள் (26 தேர்ந்தெடுக்கப்பட்டோர் + 4 நியமிக்கப்படுவோர்).",
        "Elected members hold office for 5 years, while nominated members hold office at Governor's pleasure.",
        "தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்களின் பதவிக்காலம் 5 ஆண்டுகள், நியமிக்கப்பட்டவர்கள் ஆளுநரின் விருப்பம் வரை நீடிப்பர்."
    ))

    qs.append(make_sch_q(
        "SCH_E_024", "Easy", "Conceptual", "Seventh Schedule",
        "In which list of the Seventh Schedule is 'Police and Public Order' placed?",
        "ஏழாவது அட்டவணையின் எந்தப் பட்டியலில் 'காவல்துறை மற்றும் பொது ஒழுங்கு' வைக்கப்பட்டுள்ளது?",
        "State List (List II)", "மாநிலப் பட்டியல் (பட்டியல் II)",
        "Union List (List I)", "மத்தியப் பட்டியல் (பட்டியல் I)",
        "Concurrent List (List III)", "பொதுப் பட்டியல் (பட்டியல் III)",
        "Residuary Powers", "எஞ்சிய அதிகாரங்கள்",
        "A",
        "Public Order and Police are entries 1 and 2 in the State List (List II) of the Seventh Schedule.",
        "பொது ஒழுங்கு மற்றும் காவல்துறை ஆகியவை ஏழாவது அட்டவணையின் மாநிலப் பட்டியலில் (பட்டியல் II) முறையே 1 மற்றும் 2வது பதிவுகளாக உள்ளன.",
        "Correct. Police and Public Order are in the State List.", "சரியானது. காவல்துறை மற்றும் பொது ஒழுங்கு மாநிலப் பட்டியலில் உள்ளன.",
        "Incorrect. Union List covers defence, not state police.", "தவறானது. மத்தியப் பட்டியல் பாதுகாப்பைக் கையாள்கிறது, மாநில காவல்துறையை அல்ல.",
        "Incorrect. Criminal law is concurrent, but Police is State.", "தவறானது. குற்றவியல் சட்டம் பொதுவானது, ஆனால் காவல்துறை மாநிலப் பட்டியல்.",
        "Incorrect. Residuary powers do not apply to listed items.", "தவறானது. பட்டியலில் உள்ளவற்றிற்கு எஞ்சிய அதிகாரங்கள் பொருந்தாது.",
        "State List: Police, Public Order, Public Health, Agriculture.",
        "மாநிலப் பட்டியல்: காவல்துறை, பொது ஒழுங்கு, பொது சுகாதாரம், விவசாயம்.",
        "In Union Territories like Delhi, Police is exceptionally under the Union Government.",
        "டெல்லி போன்ற யூனியன் பிரதேசங்களில் காவல்துறை விதிவிலக்காக மத்திய அரசின் கீழ் உள்ளது."
    ))

    qs.append(make_sch_q(
        "SCH_E_025", "Easy", "Conceptual", "Seventh Schedule",
        "Which of the following subjects was transferred from the State List to the Concurrent List by the 42nd Amendment Act, 1976?",
        "1976-ல் 42வது திருத்தச் சட்டத்தின் மூலம் மாநிலப் பட்டியலிலிருந்து பொதுப் பட்டியலுக்கு மாற்றப்பட்ட துறை எது?",
        "Education", "கல்வி",
        "Public Health", "பொது சுகாதாரம்",
        "Police", "காவல்துறை",
        "Agriculture", "விவசாயம்",
        "A",
        "Education was transferred from the State List to the Concurrent List by the 42nd Constitutional Amendment Act, 1976, along with Forests, Weights & Measures, Protection of Wild Animals, and Administration of Justice.",
        "1976-ல் 42வது அரசியலமைப்புத் திருத்தச் சட்டம் மூலம் கல்வி, காடுகள், எடைகள் மற்றும் அளவுகள், வனவிலங்கு பாதுகாப்பு மற்றும் நீதி நிர்வாகம் ஆகிய 5 துறைகள் பொதுப் பட்டியலுக்கு மாற்றப்பட்டன.",
        "Correct. Education was shifted to Concurrent List by 42nd CAA.", "சரியானது. கல்வி 42வது திருத்தத்தால் பொதுப் பட்டியலுக்கு மாற்றப்பட்டது.",
        "Incorrect. Public Health remains in the State List.", "தவறானது. பொது சுகாதாரம் மாநிலப் பட்டியலிலேயே உள்ளது.",
        "Incorrect. Police remains in the State List.", "தவறானது. காவல்துறை மாநிலப் பட்டியலிலேயே உள்ளது.",
        "Incorrect. Agriculture remains in the State List.", "தவறானது. விவசாயம் மாநிலப் பட்டியலிலேயே உள்ளது.",
        "42nd CAA transferred 5 subjects: Education, Forests, Wild Animals, Weights/Measures, Administration of Justice.",
        "42வது திருத்தம் 5 துறைகளை மாற்றியது: கல்வி, காடுகள், வனவிலங்குகள், எடைகள்/அளவுகள், நீதி நிர்வாகம்.",
        "Transferred subjects allow both Parliament and State Legislatures to make laws under Article 246.",
        "மாற்றப்பட்ட துறைகளில் மத்திய மற்றும் மாநில அரசுகள் இரண்டும் சட்டம் இயற்ற முடியும்."
    ))

    qs.append(make_sch_q(
        "SCH_E_026", "Easy", "Conceptual", "Eighth Schedule",
        "Which was the first language to be declared as a 'Classical Language' in India?",
        "இந்தியாவில் 'செம்மொழி' (Classical Language) தகுதியைப் பெற்ற முதல் மொழி எது?",
        "Tamil (2004)", "தமிழ் (2004)",
        "Sanskrit (2005)", "சமஸ்கிருதம் (2005)",
        "Telugu (2008)", "தெலுங்கு (2008)",
        "Kannada (2008)", "கன்னடம் (2008)",
        "A",
        "Tamil was the first language in India to be accorded the status of a 'Classical Language' in the year 2004.",
        "2004 ஆம் ஆண்டில் இந்தியாவில் 'செம்மொழி' தகுதியைப் பெற்ற முதல் மொழி தமிழ் ஆகும்.",
        "Correct. Tamil was declared Classical Language in 2004.", "சரியானது. தமிழ் 2004-ல் செம்மொழியாக அறிவிக்கப்பட்டது.",
        "Incorrect. Sanskrit was declared in 2005.", "தவறானது. சமஸ்கிருதம் 2005-ல் அறிவிக்கப்பட்டது.",
        "Incorrect. Telugu was declared in 2008.", "தவறானது. தெலுங்கு 2008-ல் அறிவிக்கப்பட்டது.",
        "Incorrect. Kannada was declared in 2008.", "தவறானது. கன்னடம் 2008-ல் அறிவிக்கப்பட்டது.",
        "First Classical Language of India = Tamil (October 2004).",
        "இந்தியாவின் முதல் செம்மொழி = தமிழ் (அக்டோபர் 2004).",
        "Sanskrit was the second classical language declared in 2005.",
        "சமஸ்கிருதம் 2005-ல் அறிவிக்கப்பட்ட இரண்டாவது செம்மொழியாகும்."
    ))

    qs.append(make_sch_q(
        "SCH_E_027", "Easy", "Conceptual", "Eighth Schedule",
        "Which of the following languages is NOT included in the Eighth Schedule of the Indian Constitution?",
        "பின்வரும் மொழிகளில் எது இந்திய அரசியலமைப்பின் எட்டாவது அட்டவணையில் சேர்க்கப்படவில்லை?",
        "English", "ஆங்கிலம்",
        "Sanskrit", "சமஸ்கிருதம்",
        "Urdu", "உருது",
        "Sindhi", "சிந்தி",
        "A",
        "English is NOT recognized in the Eighth Schedule of the Indian Constitution, despite being an associate official language of the Union.",
        "மத்திய அரசின் இணை அலுவல் மொழியாக இருந்தபோதிலும், ஆங்கிலம் இந்திய அரசியலமைப்பின் எட்டாவது அட்டவணையில் சேர்க்கப்படவில்லை.",
        "Correct. English is NOT in the Eighth Schedule.", "சரியானது. ஆங்கிலம் எட்டாவது அட்டவணையில் இல்லை.",
        "Incorrect. Sanskrit is an original language in Eighth Schedule.", "தவறானது. சமஸ்கிருதம் எட்டாவது அட்டவணையில் உள்ள அசல் மொழி.",
        "Incorrect. Urdu is an original language in Eighth Schedule.", "தவறானது. உருது எட்டாவது அட்டவணையில் உள்ள அசல் மொழி.",
        "Incorrect. Sindhi was added by 21st Amendment in 1967.", "தவறானது. சிந்தி 1967-ல் 21வது திருத்தத்தால் சேர்க்கப்பட்டது.",
        "TRAP: English and Rajasthani are NOT in Eighth Schedule.",
        "பொறி: ஆங்கிலம் மற்றும் ராஜஸ்தானி 8வது அட்டவணையில் இல்லை.",
        "Hindi is the official language of the Union under Article 343.",
        "உறுப்பு 343-ன் கீழ் இந்தி மத்திய அரசின் அதிகாரப்பூர்வ மொழியாகும்."
    ))

    qs.append(make_sch_q(
        "SCH_E_028", "Easy", "Conceptual", "Ninth Schedule",
        "The Tamil Nadu 69% Reservation Act was placed in the Ninth Schedule by which Constitutional Amendment?",
        "தமிழ்நாட்டின் 69% இடஒதுக்கீட்டுச் சட்டம் எந்த அரசியலமைப்புத் திருத்தத்தின் மூலம் ஒன்பதாவது அட்டவணையில் வைக்கப்பட்டது?",
        "76th Amendment Act, 1994", "76வது திருத்தச் சட்டம், 1994",
        "73rd Amendment Act, 1992", "73வது திருத்தச் சட்டம், 1992",
        "74th Amendment Act, 1992", "74வது திருத்தச் சட்டம், 1992",
        "86th Amendment Act, 2002", "86வது திருத்தச் சட்டம், 2002",
        "A",
        "The Tamil Nadu Backward Classes, Scheduled Castes and Scheduled Tribes (Reservation of Seats in Educational Institutions and of Appointments or Posts in the Services under the State) Act, 1993 was placed in the Ninth Schedule by the 76th Constitutional Amendment Act, 1994.",
        "தமிழ்நாட்டின் 69% இடஒதுக்கீட்டுச் சட்டம் 1994-ல் 76வது அரசியலமைப்புத் திருத்தச் சட்டம் மூலம் ஒன்பதாவது அட்டவணையில் சேர்க்கப்பட்டது.",
        "Correct. 76th CAA 1994 protected TN 69% reservation.", "சரியானது. 76வது திருத்தச் சட்டம் 1994 தமிழக 69% இடஒதுக்கீட்டைப் பாதுகாத்தது.",
        "Incorrect. 73rd CAA is for Panchayats.", "தவறானது. 73வது திருத்தம் பஞ்சாயத்துகளுக்கானது.",
        "Incorrect. 74th CAA is for Municipalities.", "தவறானது. 74வது திருத்தம் நகராட்சிகளுக்கானது.",
        "Incorrect. 86th CAA added Right to Education.", "தவறானது. 86வது திருத்தம் கல்வி உரிமையைச் சேர்த்தது.",
        "76th CAA 1994 = TN 69% Reservation Act placed in 9th Schedule.",
        "76வது திருத்தம் 1994 = தமிழ்நாடு 69% இடஒதுக்கீடு 9வது அட்டவணையில் வைப்பு.",
        "The Act is Entry 257A in the Ninth Schedule.",
        "இச்சட்டம் ஒன்பதாவது அட்டவணையில் பதிவு 257A ஆக உள்ளது."
    ))

    qs.append(make_sch_q(
        "SCH_E_029", "Easy", "Conceptual", "Tenth Schedule",
        "Under the Tenth Schedule, who is the deciding authority on questions of disqualification of a Member of Lok Sabha?",
        "பத்தாவது அட்டவணையின் கீழ் மக்களவை உறுப்பினரின் தகுதிநீக்கம் தொடர்பான கேள்விகளில் முடிவெடுக்கும் அதிகாரம் யாரிடம் உள்ளது?",
        "Speaker of the Lok Sabha", "மக்களவைத் தலைவர் (சபாநாயகர்)",
        "President of India", "இந்தியக் குடியரசுத் தலைவர்",
        "Election Commission of India", "இந்தியத் தேர்தல் ஆணையம்",
        "Supreme Court of India", "இந்திய உச்ச நீதிமன்றம்",
        "A",
        "Under the Tenth Schedule, the question of disqualification on ground of defection is decided by the Speaker in the case of Lok Sabha and Chairman in the case of Rajya Sabha.",
        "பத்தாவது அட்டவணையின் கீழ், கட்சித் தாவல் தொடர்பான தகுதிநீக்கப் பிரச்சினையை மக்களவையில் சபாநாயகரும், மாநிலங்களவையில் தலைவரும் தீர்மானிக்கின்றனர்.",
        "Correct. Speaker decides defection cases in Lok Sabha.", "சரியானது. மக்களவையில் சபாநாயகர் கட்சித் தாவல் வழக்குகளைத் தீர்மானிக்கிறார்.",
        "Incorrect. President decides other disqualifications under Art 103 on EC advice.", "தவறானது. உறுப்பு 103-ன் கீழ் பிற தகுதிநீக்கங்களை தேர்தல் ஆணைய ஆலோசனையுடன் குடியரசுத் தலைவர் தீர்மானிக்கிறார்.",
        "Incorrect. EC only advises on general disqualifications, not defection.", "தவறானது. கட்சித் தாவலில் தேர்தல் ஆணையத்திற்கு நேரடி அதிகாரமில்லை.",
        "Incorrect. Supreme Court acts only on judicial review.", "தவறானது. உச்ச நீதிமன்றம் மறுஆய்வு மட்டுமே செய்ய முடியும்.",
        "Defection disqualification = Presiding Officer (Speaker/Chairman).",
        "கட்சித் தாவல் தகுதிநீக்கம் = அவைத் தலைவர் (சபாநாயகர் / தலைவர்).",
        "General disqualifications (Art 102(1)) are decided by the President under Article 103.",
        "பொதுவான தகுதிநீக்கங்கள் (உறுப்பு 102(1)) உறுப்பு 103-ன் கீழ் குடியரசுத் தலைவரால் தீர்மானிக்கப்படுகின்றன."
    ))

    qs.append(make_sch_q(
        "SCH_E_030", "Easy", "Conceptual", "Eleventh Schedule",
        "Which Constitutional Amendment Act added the Eleventh Schedule to the Constitution of India?",
        "இந்திய அரசியலமைப்பில் பதினோராவது அட்டவணையைச் சேர்த்த அரசியலமைப்புத் திருத்தச் சட்டம் எது?",
        "73rd Constitutional Amendment Act, 1992", "73வது அரசியலமைப்புத் திருத்தச் சட்டம், 1992",
        "74th Constitutional Amendment Act, 1992", "74வது அரசியலமைப்புத் திருத்தச் சட்டம், 1992",
        "52nd Constitutional Amendment Act, 1985", "52வது அரசியலமைப்புத் திருத்தச் சட்டம், 1985",
        "42nd Constitutional Amendment Act, 1976", "42வது அரசியலமைப்புத் திருத்தச் சட்டம், 1976",
        "A",
        "The 73rd Constitutional Amendment Act, 1992 added Part IX and the Eleventh Schedule containing 29 subjects for Panchayats.",
        "73வது அரசியலமைப்புத் திருத்தச் சட்டம் 1992, பகுதி IX மற்றும் பஞ்சாயத்துகளுக்கான 29 துறைகளைக் கொண்ட பதினோராவது அட்டவணையைச் சேர்த்தது.",
        "Correct. 73rd CAA 1992 added Eleventh Schedule.", "சரியானது. 73வது திருத்தச் சட்டம் 1992 பதினோராவது அட்டவணையைச் சேர்த்தது.",
        "Incorrect. 74th CAA added Twelfth Schedule.", "தவறானது. 74வது திருத்தம் 12வது அட்டவணையைச் சேர்த்தது.",
        "Incorrect. 52nd CAA added Tenth Schedule.", "தவறானது. 52வது திருத்தம் 10வது அட்டவணையைச் சேர்த்தது.",
        "Incorrect. 42nd CAA was enacted in 1976.", "தவறானது. 42வது திருத்தம் 1976-ல் இயற்றப்பட்டது.",
        "73rd CAA = Eleventh Schedule (Panchayati Raj, 29 items).",
        "73வது திருத்தம் = பதினோராவது அட்டவணை (பஞ்சாயத்து ராஜ், 29 துறைகள்).",
        "The amendment came into force on April 24, 1993, celebrated as National Panchayati Raj Day.",
        "இத்திருத்தம் 1993 ஏப்ரல் 24 அன்று நடைமுறைக்கு வந்தது; இந்நாள் தேசிய பஞ்சாயத்து ராஜ் தினமாகக் கொண்டாடப்படுகிறது."
    ))

    # E31 - E40: Schedule Numbers and Subject Quick Identification
    qs.append(make_sch_q(
        "SCH_E_031", "Easy", "Conceptual", "Twelfth Schedule",
        "Which Constitutional Amendment Act inserted the Twelfth Schedule into the Indian Constitution?",
        "இந்திய அரசியலமைப்பில் பன்னிரண்டாவது அட்டவணையைச் சேர்த்த அரசியலமைப்புத் திருத்தச் சட்டம் எது?",
        "74th Constitutional Amendment Act, 1992", "74வது அரசியலமைப்புத் திருத்தச் சட்டம், 1992",
        "73rd Constitutional Amendment Act, 1992", "73வது அரசியலமைப்புத் திருத்தச் சட்டம், 1992",
        "69th Constitutional Amendment Act, 1991", "69வது அரசியலமைப்புத் திருத்தச் சட்டம், 1991",
        "71st Constitutional Amendment Act, 1992", "71வது அரசியலமைப்புத் திருத்தச் சட்டம், 1992",
        "A",
        "The 74th Constitutional Amendment Act, 1992 added Part IXA and the Twelfth Schedule specifying 18 subjects for Municipalities.",
        "74வது அரசியலமைப்புத் திருத்தச் சட்டம் 1992, பகுதி IXA மற்றும் நகராட்சிகளுக்கான 18 துறைகளைக் கொண்ட பன்னிரண்டாவது அட்டவணையைச் சேர்த்தது.",
        "Correct. 74th CAA 1992 added Twelfth Schedule.", "சரியானது. 74வது திருத்தச் சட்டம் 1992 பன்னிரண்டாவது அட்டவணையைச் சேர்த்தது.",
        "Incorrect. 73rd CAA added Eleventh Schedule.", "தவறானது. 73வது திருத்தம் 11வது அட்டவணையைச் சேர்த்தது.",
        "Incorrect. 69th CAA made Delhi the NCT.", "தவறானது. 69வது திருத்தம் டெல்லியை தேசியத் தலைநகர் பகுதியாக்கியது.",
        "Incorrect. 71st CAA added 3 languages to Eighth Schedule.", "தவறானது. 71வது திருத்தம் எட்டாவது அட்டவணையில் 3 மொழிகளைச் சேர்த்தது.",
        "74th CAA = Twelfth Schedule (Municipalities, 18 items).",
        "74வது திருத்தம் = பன்னிரண்டாவது அட்டவணை (நகராட்சிகள், 18 துறைகள்).",
        "It came into effect on June 1, 1993.",
        "இது 1993 ஜூன் 1 அன்று நடைமுறைக்கு வந்தது."
    ))

    qs.append(make_sch_q(
        "SCH_E_032", "Easy", "Conceptual", "First Schedule",
        "How many States and Union Territories are specified in the First Schedule of the Constitution of India at present?",
        "தற்போது இந்திய அரசியலமைப்பின் முதல் அட்டவணையில் எத்தனை மாநிலங்கள் மற்றும் யூனியன் பிரதேசங்கள் குறிப்பிடப்பட்டுள்ளன?",
        "28 States and 8 Union Territories", "28 மாநிலங்கள் மற்றும் 8 யூனியன் பிரதேசங்கள்",
        "29 States and 7 Union Territories", "29 மாநிலங்கள் மற்றும் 7 யூனியன் பிரதேசங்கள்",
        "28 States and 9 Union Territories", "28 மாநிலங்கள் மற்றும் 9 யூனியன் பிரதேசங்கள்",
        "29 States and 8 Union Territories", "29 மாநிலங்கள் மற்றும் 8 யூனியன் பிரதேசங்கள்",
        "A",
        "Following the Jammu and Kashmir Reorganisation Act, 2019 and the merger of Dadra & Nagar Haveli and Daman & Diu in 2020, India has 28 States and 8 Union Territories in the First Schedule.",
        "2019-ன் ஜம்மு காஷ்மீர் மறுசீரமைப்புச் சட்டம் மற்றும் 2020-ன் தாத்ரா & நகர் ஹவேலி மற்றும் தாமன் & தியூ இணைப்புக்குப் பிறகு, முதல் அட்டவணையில் 28 மாநிலங்கள் மற்றும் 8 யூனியன் பிரதேசங்கள் உள்ளன.",
        "Correct. Currently 28 States and 8 UTs.", "சரியானது. தற்போது 28 மாநிலங்கள் மற்றும் 8 யூனியன் பிரதேசங்கள்.",
        "Incorrect. 29 states was prior to J&K reorganisation.", "தவறானது. ஜம்மு காஷ்மீர் மறுசீரமைப்பிற்கு முன் 29 மாநிலங்கள் இருந்தன.",
        "Incorrect. 9 UTs was prior to merger of DNH and DD.", "தவறானது. DNH மற்றும் DD இணைப்பிற்கு முன் 9 யூனியன் பிரதேசங்கள் இருந்தன.",
        "Incorrect. 29 states is outdated.", "தவறானது. 29 மாநிலங்கள் என்பது காலாவதியானது.",
        "Current First Schedule status: 28 States + 8 Union Territories.",
        "தற்போதைய முதல் அட்டவணை நிலை: 28 மாநிலங்கள் + 8 யூனியன் பிரதேசங்கள்.",
        "The merger of DNH and DD took effect on January 26, 2020.",
        "DNH மற்றும் DD இணைப்பு 2020 ஜனவரி 26 அன்று நடைமுறைக்கு வந்தது."
    ))

    qs.append(make_sch_q(
        "SCH_E_033", "Easy", "Conceptual", "Second Schedule",
        "The salary of the Comptroller and Auditor General (CAG) of India is charged under which Schedule?",
        "இந்தியக் கணக்குத் தணிக்கைத் தலைவரின் (CAG) சம்பளம் எந்த அட்டவணையின் கீழ் குறிப்பிடப்பட்டுள்ளது?",
        "Second Schedule, Part E", "இரண்டாவது அட்டவணை, பகுதி E",
        "Third Schedule", "மூன்றாவது அட்டவணை",
        "Fourth Schedule", "நான்காவது அட்டவணை",
        "First Schedule", "முதல் அட்டவணை",
        "A",
        "The salary and service conditions of the Comptroller and Auditor General of India are specified in Part E of the Second Schedule to the Constitution.",
        "இந்தியக் கணக்குத் தணிக்கைத் தலைவரின் சம்பளம் மற்றும் சேவை நிபந்தனைகள் அரசியலமைப்பின் இரண்டாவது அட்டவணையின் பகுதி E-ல் குறிப்பிடப்பட்டுள்ளன.",
        "Correct. Second Schedule Part E covers the CAG.", "சரியானது. இரண்டாவது அட்டவணை பகுதி E சி.ஏ.ஜி-யைக் குறிக்கிறது.",
        "Incorrect. Third Schedule provides oath, not salary.", "தவறானது. மூன்றாவது அட்டவணை பிரமாணத்தை வழங்குகிறது, சம்பளத்தை அல்ல.",
        "Incorrect. Fourth Schedule is for Rajya Sabha seats.", "தவறானது. நான்காவது அட்டவணை மாநிலங்களவை இடங்களுக்கானது.",
        "Incorrect. First Schedule is for territorial boundaries.", "தவறானது. முதல் அட்டவணை எல்லைப் பகுதிகளுக்கானது.",
        "CAG salary = Second Schedule; CAG oath = Third Schedule.",
        "சி.ஏ.ஜி சம்பளம் = இரண்டாவது அட்டவணை; சி.ஏ.ஜி பிரமாணம் = மூன்றாவது அட்டவணை.",
        "CAG salary is equal to that of a Supreme Court Judge.",
        "சி.ஏ.ஜி-யின் சம்பளம் உச்ச நீதிமன்ற நீதிபதியின் சம்பளத்திற்குச் சமமானது."
    ))

    qs.append(make_sch_q(
        "SCH_E_034", "Easy", "Conceptual", "Third Schedule",
        "Who among the following takes an oath according to the form set out in the Third Schedule?",
        "பின்வருவனவற்றில் யார் மூன்றாவது அட்டவணையில் குறிப்பிடப்பட்டுள்ள படிவத்தின்படி பதவிப் பிரமாணம் ஏற்கிறார்கள்?",
        "Judges of the Supreme Court of India", "இந்திய உச்ச நீதிமன்ற நீதிபதிகள்",
        "President of India", "இந்தியக் குடியரசுத் தலைவர்",
        "Vice-President of India", "இந்தியத் துணைத் தலைவர்",
        "Governor of a State", "ஒரு மாநிலத்தின் ஆளுநர்",
        "A",
        "Judges of the Supreme Court take their oath under the Third Schedule (Form IV), whereas the President (Art 60), Vice-President (Art 69), and Governor (Art 159) have their oaths directly in constitutional articles.",
        "உச்ச நீதிமன்ற நீதிபதிகள் மூன்றாவது அட்டவணையின் கீழ் பிரமாணம் ஏற்கின்றனர்; ஆனால் குடியரசுத் தலைவர் (உறுப்பு 60), துணைத் தலைவர் (உறுப்பு 69) மற்றும் ஆளுநர் (உறுப்பு 159) அரசியலமைப்பு உறுப்புகளில் நேரடியாகப் பிரமாணம் ஏற்கின்றனர்.",
        "Correct. SC Judges take oath under Third Schedule.", "சரியானது. உச்ச நீதிமன்ற நீதிபதிகள் மூன்றாவது அட்டவணையின் கீழ் பிரமாணம் ஏற்கின்றனர்.",
        "Incorrect. President oath is in Article 60.", "தவறானது. குடியரசுத் தலைவர் பிரமாணம் உறுப்பு 60-ல் உள்ளது.",
        "Incorrect. Vice-President oath is in Article 69.", "தவறானது. துணைத் தலைவர் பிரமாணம் உறுப்பு 69-ல் உள்ளது.",
        "Incorrect. Governor oath is in Article 159.", "தவறானது. ஆளுநர் பிரமாணம் உறுப்பு 159-ல் உள்ளது.",
        "Judges (SC/HC) take oath under Schedule 3; Heads of State (President/Governor) under specific Articles.",
        "நீதிபதிகள் 3வது அட்டவணையின் கீழ் பிரமாணம் ஏற்கின்றனர்; அரசுத் தலைவர்கள் குறிப்பிட்ட உறுப்புகளின் கீழ் ஏற்கின்றனர்.",
        "Third Schedule Form VIII covers High Court Judges.",
        "மூன்றாவது அட்டவணையின் படிவம் VIII உயர் நீதிமன்ற நீதிபதிகளை உள்ளடக்கியது."
    ))

    qs.append(make_sch_q(
        "SCH_E_035", "Easy", "Conceptual", "Fourth Schedule",
        "How many Union Territories currently have representation in the Rajya Sabha under the Fourth Schedule?",
        "நான்காவது அட்டவணையின் கீழ் தற்போது எத்தனை யூனியன் பிரதேசங்கள் மாநிலங்களவையில் பிரதிநிதித்துவம் பெற்றுள்ளன?",
        "3 Union Territories", "3 யூனியன் பிரதேசங்கள்",
        "2 Union Territories", "2 யூனியன் பிரதேசங்கள்",
        "4 Union Territories", "4 யூனியன் பிரதேசங்கள்",
        "All 8 Union Territories", "அனைத்து 8 யூனியன் பிரதேசங்கள்",
        "A",
        "Only 3 Union Territories (Delhi with 3 seats, Puducherry with 1 seat, and Jammu & Kashmir with 4 seats) currently have representation in the Rajya Sabha.",
        "தற்போது 3 யூனியன் பிரதேசங்கள் மட்டுமே (டெல்லி - 3 இடங்கள், புதுச்சேரி - 1 இடம், ஜம்மு & காஷ்மீர் - 4 இடங்கள்) மாநிலங்களவையில் பிரதிநிதித்துவம் பெற்றுள்ளன.",
        "Correct. Only 3 UTs (Delhi, Puducherry, J&K) have Rajya Sabha seats.", "சரியானது. 3 யூனியன் பிரதேசங்கள் மட்டுமே மாநிலங்களவை இடங்களைக் கொண்டுள்ளன.",
        "Incorrect. 2 was the count before J&K became a UT.", "தவறானது. ஜம்மு காஷ்மீர் UT ஆவதற்கு முன் 2 மட்டுமே இருந்தது.",
        "Incorrect. 4 is incorrect.", "தவறானது. 4 என்பது தவறானது.",
        "Incorrect. Other 5 UTs have no Rajya Sabha representation.", "தவறானது. மற்ற 5 UTகளுக்கு மாநிலங்களவை இடங்கள் இல்லை.",
        "UTs with Rajya Sabha representation: Delhi (3), Puducherry (1), J&K (4).",
        "மாநிலங்களவை பிரதிநிதித்துவம் உள்ள UTகள்: டெல்லி (3), புதுச்சேரி (1), J&K (4).",
        "Representation requires a Legislative Assembly to form the electoral college.",
        "மாநிலங்களவை உறுப்பினர்களைத் தேர்ந்தெடுக்க சட்டமன்றம் இருப்பது அவசியமாகும்."
    ))

    # E36 - E50: Schedules 5 to 12 Details
    qs.append(make_sch_q(
        "SCH_E_036", "Easy", "Conceptual", "Fifth Schedule",
        "Under the Fifth Schedule, who has the power to declare an area as a Scheduled Area?",
        "ஐந்தாவது அட்டவணையின் கீழ், ஒரு பகுதியை திட்டமிடப்பட்ட பகுதியாக (Scheduled Area) அறிவிக்கும் அதிகாரம் யாருக்கு உள்ளது?",
        "President of India", "இந்தியக் குடியரசுத் தலைவர்",
        "Governor of the State", "மாநில ஆளுநர்",
        "Parliament of India", "இந்திய நாடாளுமன்றம்",
        "Chief Minister of the State", "மாநில முதலமைச்சர்",
        "A",
        "The President of India is empowered under the Fifth Schedule to declare any area to be a Scheduled Area and can alter its boundaries in consultation with the Governor.",
        "ஐந்தாவது அட்டவணையின் கீழ் எந்தவொரு பகுதியையும் திட்டமிடப்பட்ட பகுதியாக அறிவிக்கவும், ஆளுநருடன் கலந்தாலோசித்து அதன் எல்லைகளை மாற்றவும் இந்தியக் குடியரசுத் தலைவருக்கு அதிகாரம் உள்ளது.",
        "Correct. President declares Scheduled Areas under Fifth Schedule.", "சரியானது. குடியரசுத் தலைவர் திட்டமிடப்பட்ட பகுதிகளை அறிவிக்கிறார்.",
        "Incorrect. Governor is only consulted by the President.", "தவறானது. ஆளுநரிடம் குடியரசுத் தலைவர் கலந்தாலோசிக்க மட்டுமே செய்கிறார்.",
        "Incorrect. Parliament does not issue the initial notification.", "தவறானது. தொடக்க அறிவிப்பை நாடாளுமன்றம் வெளியிடுவதில்லை.",
        "Incorrect. Chief Minister has no such constitutional power.", "தவறானது. முதலமைச்சருக்கு இத்தகைய அரசியலமைப்பு அதிகாரம் இல்லை.",
        "Declaration of Scheduled Area = President of India.",
        "திட்டமிடப்பட்ட பகுதியை அறிவிப்பவர் = இந்தியக் குடியரசுத் தலைவர்.",
        "The Governor submits an annual report to the President regarding the administration of Scheduled Areas.",
        "திட்டமிடப்பட்ட பகுதிகளின் நிர்வாகம் குறித்து ஆளுநர் ஆண்டுதோறும் குடியரசுத் தலைவருக்கு அறிக்கை சமர்ப்பிக்கிறார்."
    ))

    qs.append(make_sch_q(
        "SCH_E_037", "Easy", "Conceptual", "Sixth Schedule",
        "What is the tenure of elected members of an Autonomous District Council under the Sixth Schedule?",
        "ஆறாவது அட்டவணையின் கீழ் ஒரு தன்னாட்சி மாவட்டக் குழுவின் தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்களின் பதவிக்காலம் என்ன?",
        "5 years", "5 ஆண்டுகள்",
        "6 years", "6 ஆண்டுகள்",
        "4 years", "4 ஆண்டுகள்",
        "At the pleasure of the Governor", "ஆளுநரின் விருப்பம் வரை",
        "A",
        "The term of an Autonomous District Council is 5 years from the date of its first meeting for elected members, unless dissolved earlier.",
        "தன்னாட்சி மாவட்டக் குழுவின் தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்களின் பதவிக்காலம், முன்கூட்டியே கலைக்கப்படாவிட்டால், முதல் கூட்டத் தேதியிலிருந்து 5 ஆண்டுகள் ஆகும்.",
        "Correct. Term of elected ADC members is 5 years.", "சரியானது. தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்களின் பதவிக்காலம் 5 ஆண்டுகள்.",
        "Incorrect. 6 years applies to Rajya Sabha, not ADCs.", "தவறானது. 6 ஆண்டுகள் மாநிலங்களவைக்குரியது.",
        "Incorrect. 4 years is incorrect.", "தவறானது. 4 ஆண்டுகள் என்பது தவறானது.",
        "Incorrect. Nominated members hold office at Governor's pleasure, not elected members.", "தவறானது. நியமிக்கப்பட்ட உறுப்பினர்கள் மட்டுமே ஆளுநர் விருப்பம் வரை பதவி வகிப்பர்.",
        "Sixth Schedule ADC term = 5 years (elected members).",
        "ஆறாவது அட்டவணை ADC பதவிக்காலம் = 5 ஆண்டுகள் (தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்கள்).",
        "Governor can extend the term during an emergency by not more than one year at a time.",
        "அவசரநிலையின் போது ஆளுநர் ஒரே நேரத்தில் ஒரு ஆண்டுக்கு மிகாமல் பதவிக்காலத்தை நீட்டிக்க முடியும்."
    ))

    qs.append(make_sch_q(
        "SCH_E_038", "Easy", "Conceptual", "Seventh Schedule",
        "In which list of the Seventh Schedule is 'Banking and Insurance' placed?",
        "ஏழாவது அட்டவணையின் எந்தப் பட்டியலில் 'வங்கி மற்றும் காப்பீடு' வைக்கப்பட்டுள்ளது?",
        "Union List (List I)", "மத்தியப் பட்டியல் (பட்டியல் I)",
        "State List (List II)", "மாநிலப் பட்டியல் (பட்டியல் II)",
        "Concurrent List (List III)", "பொதுப் பட்டியல் (பட்டியல் III)",
        "Residuary Powers", "எஞ்சிய அதிகாரங்கள்",
        "A",
        "Banking (Entry 45) and Insurance (Entry 47) are subjects of national economic importance placed in the Union List (List I).",
        "வங்கி (பதிவு 45) மற்றும் காப்பீடு (பதிவு 47) ஆகியவை தேசிய முக்கியத்துவம் வாய்ந்த துறைகளாக மத்தியப் பட்டியலில் (பட்டியல் I) வைக்கப்பட்டுள்ளன.",
        "Correct. Banking and Insurance are in the Union List.", "சரியானது. வங்கி மற்றும் காப்பீடு மத்தியப் பட்டியலில் உள்ளன.",
        "Incorrect. They are not under State List.", "தவறானது. அவை மாநிலப் பட்டியலில் இல்லை.",
        "Incorrect. They are not concurrent subjects.", "தவறானது. அவை பொதுப் பட்டியலில் இல்லை.",
        "Incorrect. They are explicitly enumerated entries.", "தவறானது. அவை தெளிவாகக் குறிப்பிடப்பட்ட பதிவுகள்.",
        "Union List = Defence, Foreign Affairs, Railways, Banking, Insurance, Atomic Energy.",
        "மத்தியப் பட்டியல் = பாதுகாப்பு, வெளியுறவு, இரயில்வே, வங்கி, காப்பீடு, அணுசக்தி.",
        "Only Parliament has the exclusive power to make laws on Union List items.",
        "மத்தியப் பட்டியல் விவகாரங்களில் நாடாளுமன்றத்திற்கு மட்டுமே பிரத்யேக அதிகாரமுள்ளது."
    ))

    qs.append(make_sch_q(
        "SCH_E_039", "Easy", "Conceptual", "Seventh Schedule",
        "Under the Indian Constitution, with whom do the 'Residuary Powers' of legislation vest?",
        "இந்திய அரசியலமைப்பின் கீழ், சட்டமியற்றும் 'எஞ்சிய அதிகாரங்கள்' (Residuary Powers) யாரிடம் உள்ளன?",
        "Parliament of India exclusively (Article 248)", "இந்திய நாடாளுமன்றத்திற்கு மட்டுமே (உறுப்பு 248)",
        "State Legislatures exclusively", "மாநில சட்டமன்றங்களுக்கு மட்டுமே",
        "Both Parliament and State Legislatures concurrently", "நாடாளுமன்றம் மற்றும் மாநில சட்டமன்றங்கள் இரண்டிற்கும் பொதுவாக",
        "President of India", "இந்தியக் குடியரசுத் தலைவரிடம்",
        "A",
        "Under Article 248 and Entry 97 of the Union List, residuary powers (power to legislate on matters not mentioned in any of the three lists) vest exclusively in Parliament.",
        "உறுப்பு 248 மற்றும் மத்தியப் பட்டியலின் பதிவு 97-ன் கீழ், எஞ்சிய அதிகாரங்கள் (எந்தப் பட்டியலிலும் குறிப்பிடப்படாத துறைகளில் சட்டம் இயற்றும் அதிகாரம்) நாடாளுமன்றத்திற்கு மட்டுமே பிரத்யேகமாக வழங்கப்பட்டுள்ளன.",
        "Correct. Residuary powers vest exclusively in Parliament.", "சரியானது. எஞ்சிய அதிகாரங்கள் நாடாளுமன்றத்திற்கு மட்டுமே உள்ளன.",
        "Incorrect. State Legislatures have no residuary powers.", "தவறானது. மாநில சட்டமன்றங்களுக்கு எஞ்சிய அதிகாரங்கள் இல்லை.",
        "Incorrect. Residuary powers are not concurrent.", "தவறானது. எஞ்சிய அதிகாரங்கள் பொதுவானவை அல்ல.",
        "Incorrect. The executive does not hold legislative residuary power.", "தவறானது. நிர்வாகத்துறைக்கு சட்டமியற்றும் அதிகாரம் இல்லை.",
        "India vests residuary powers in the Centre (Canadian model), unlike USA which vests them in States.",
        "கனடா முறையைப் பின்பற்றி இந்தியா எஞ்சிய அதிகாரங்களை மத்திய அரசிடம் வைத்துள்ளது; அமெரிக்கா மாநிலங்களிடம் வைத்துள்ளது.",
        "Article 248 is reinforced by Entry 97 of the Union List.",
        "மத்தியப் பட்டியலின் 97வது பதிவு உறுப்பு 248-ஐ வலுப்படுத்துகிறது."
    ))

    qs.append(make_sch_q(
        "SCH_E_040", "Easy", "Conceptual", "Eighth Schedule",
        "Which Constitutional Amendment Act added the Sindhi language to the Eighth Schedule?",
        "சிந்தி மொழியை எட்டாவது அட்டவணையில் சேர்த்த அரசியலமைப்புத் திருத்தச் சட்டம் எது?",
        "21st Amendment Act, 1967", "21வது திருத்தச் சட்டம், 1967",
        "71st Amendment Act, 1992", "71வது திருத்தச் சட்டம், 1992",
        "92nd Amendment Act, 2003", "92வது திருத்தச் சட்டம், 2003",
        "96th Amendment Act, 2011", "96வது திருத்தச் சட்டம், 2011",
        "A",
        "Sindhi was added as the 15th language to the Eighth Schedule by the 21st Constitutional Amendment Act, 1967.",
        "1967-ல் 21வது அரசியலமைப்புத் திருத்தச் சட்டம் மூலம் சிந்தி மொழி எட்டாவது அட்டவணையில் 15வது மொழியாகச் சேர்க்கப்பட்டது.",
        "Correct. 21st CAA 1967 added Sindhi.", "சரியானது. 21வது திருத்தம் 1967 சிந்தியைச் சேர்த்தது.",
        "Incorrect. 71st CAA added Konkani, Manipuri, and Nepali in 1992.", "தவறானது. 71வது திருத்தம் 1992-ல் கொங்கணி, மணிப்பூரி, நேபாளியைச் சேர்த்தது.",
        "Incorrect. 92nd CAA added Bodo, Dogri, Maithili, and Santhali in 2003.", "தவறானது. 92வது திருத்தம் 2003-ல் போடோ, டோக்ரி, மைதிலி, சந்தாலியைச் சேர்த்தது.",
        "Incorrect. 96th CAA renamed Oriya to Odia in 2011.", "தவறானது. 96வது திருத்தம் 2011-ல் ஒரியாவை ஒடியா என மாற்றியது.",
        "21st CAA 1967 = Sindhi (15th language).", "21வது திருத்தம் 1967 = சிந்தி (15வது மொழி).",
        "Sindhi was the first language added to the Eighth Schedule after the Constitution was adopted.",
        "அரசியலமைப்பு ஏற்றுக்கொள்ளப்பட்ட பிறகு எட்டாவது அட்டவணையில் சேர்க்கப்பட்ட முதல் மொழி சிந்தி ஆகும்."
    ))

    qs.append(make_sch_q(
        "SCH_E_041", "Easy", "Conceptual", "Eighth Schedule",
        "Which group of three languages was added to the Eighth Schedule by the 71st Constitutional Amendment Act, 1992?",
        "1992-ல் 71வது அரசியலமைப்புத் திருத்தச் சட்டத்தின் மூலம் எட்டாவது அட்டவணையில் சேர்க்கப்பட்ட மூன்று மொழிகள் எவை?",
        "Konkani, Manipuri, and Nepali", "கொங்கணி, மணிப்பூரி மற்றும் நேபாளி",
        "Bodo, Dogri, and Maithili", "போடோ, டோக்ரி மற்றும் மைதிலி",
        "Sindhi, Sanskrit, and Kashmiri", "சிந்தி, சமஸ்கிருதம் மற்றும் காஷ்மீரி",
        "Maithili, Santhali, and Dogri", "மைதிலி, சந்தாலி மற்றும் டோக்ரி",
        "A",
        "The 71st Constitutional Amendment Act, 1992 added Konkani, Manipuri, and Nepali (mnemonic: KMN) to the Eighth Schedule.",
        "1992-ல் 71வது அரசியலமைப்புத் திருத்தச் சட்டம் கொங்கணி, மணிப்பூரி மற்றும் நேபாளி (KMN) ஆகிய மூன்று மொழிகளை எட்டாவது அட்டவணையில் சேர்த்தது.",
        "Correct. 71st CAA added Konkani, Manipuri, Nepali.", "சரியானது. 71வது திருத்தம் கொங்கணி, மணிப்பூரி, நேபாளியைச் சேர்த்தது.",
        "Incorrect. Bodo, Dogri, Maithili were added by 92nd CAA in 2003.", "தவறானது. போடோ, டோக்ரி, மைதிலி 2003-ல் 92வது திருத்தத்தால் சேர்க்கப்பட்டன.",
        "Incorrect. Sanskrit and Kashmiri were original languages.", "தவறானது. சமஸ்கிருதம் மற்றும் காஷ்மீரி அசல் மொழிகள்.",
        "Incorrect. Santhali was added by 92nd CAA.", "தவறானது. சந்தாலி 92வது திருத்தத்தால் சேர்க்கப்பட்டது.",
        "Mnemonic: 71st CAA = KMN (Konkani, Manipuri, Nepali).",
        "நினைவுக் குறிப்பு: 71வது திருத்தம் = KMN (கொங்கணி, மணிப்பூரி, நேபாளி).",
        "Nepali is the only foreign language of origin included in the Eighth Schedule.",
        "எட்டாவது அட்டவணையில் இடம்பெற்றுள்ள வெளிநாட்டுத் தோற்றம் கொண்ட ஒரே மொழி நேபாளி ஆகும்."
    ))

    qs.append(make_sch_q(
        "SCH_E_042", "Easy", "Conceptual", "Eighth Schedule",
        "Which four languages were added to the Eighth Schedule by the 92nd Constitutional Amendment Act, 2003?",
        "2003-ல் 92வது அரசியலமைப்புத் திருத்தச் சட்டத்தின் மூலம் எட்டாவது அட்டவணையில் சேர்க்கப்பட்ட நான்கு மொழிகள் எவை?",
        "Bodo, Dogri, Maithili, and Santhali", "போடோ, டோக்ரி, மைதிலி மற்றும் சந்தாலி",
        "Konkani, Manipuri, Nepali, and Sindhi", "கொங்கணி, மணிப்பூரி, நேபாளி மற்றும் சிந்தி",
        "Bodo, Assamese, Dogri, and Santhali", "போடோ, அசாமி, டோக்ரி மற்றும் சந்தாலி",
        "Bhojpuri, Maithili, Santhali, and Dogri", "போஜ்புரி, மைதிலி, சந்தாலி மற்றும் டோக்ரி",
        "A",
        "The 92nd Constitutional Amendment Act, 2003 added Bodo, Dogri, Maithili, and Santhali (mnemonic: BDMS), raising the total to 22 languages.",
        "2003-ல் 92வது அரசியலமைப்புத் திருத்தச் சட்டம் போடோ, டோக்ரி, மைதிலி மற்றும் சந்தாலி (BDMS) ஆகிய நான்கு மொழிகளைச் சேர்த்து, மொத்த மொழிகளின் எண்ணிக்கையை 22 ஆக உயர்த்தியது.",
        "Correct. 92nd CAA added Bodo, Dogri, Maithili, Santhali.", "சரியானது. 92வது திருத்தம் போடோ, டோக்ரி, மைதிலி, சந்தாலியைச் சேர்த்தது.",
        "Incorrect. Konkani, Manipuri, Nepali were added by 71st CAA.", "தவறானது. கொங்கணி, மணிப்பூரி, நேபாளி 71வது திருத்தத்தால் சேர்க்கப்பட்டன.",
        "Incorrect. Assamese was an original language.", "தவறானது. அசாமி அசல் மொழியாகும்.",
        "Incorrect. Bhojpuri is not in the Eighth Schedule.", "தவறானது. போஜ்புரி எட்டாவது அட்டவணையில் இல்லை.",
        "Mnemonic: 92nd CAA = BDMS (Bodo, Dogri, Maithili, Santhali).",
        "நினைவுக் குறிப்பு: 92வது திருத்தம் = BDMS (போடோ, டோக்ரி, மைதிலி, சந்தாலி).",
        "Santhali is an Austroasiatic language spoken predominantly by tribal populations in Jharkhand and West Bengal.",
        "சந்தாலி என்பது ஜார்க்கண்ட் மற்றும் மேற்கு வங்க பழங்குடி மக்களால் பேசப்படும் ஆஸ்ட்ரோ-ஆசிய மொழியாகும்."
    ))

    qs.append(make_sch_q(
        "SCH_E_043", "Easy", "Conceptual", "Ninth Schedule",
        "Which landmark judgment of the Supreme Court held that laws inserted in the Ninth Schedule after April 24, 1973 are subject to judicial review?",
        "1973 ஏப்ரல் 24-க்குப் பிறகு ஒன்பதாவது அட்டவணையில் சேர்க்கப்பட்ட சட்டங்கள் நீதிமன்ற மறுஆய்வுக்கு உட்பட்டவை என்று தீர்ப்பளித்த உச்ச நீதிமன்றத்தின் வரலாற்றுச் சிறப்புமிக்க வழக்கு எது?",
        "I.R. Coelho v. State of Tamil Nadu (2007)", "ஐ.ஆர். கோயல்ஹோ எதிர் தமிழ்நாடு அரசு (2007)",
        "Kesavananda Bharati v. State of Kerala (1973)", "கேசவாநந்த பாரதி எதிர் கேரள அரசு (1973)",
        "Minerva Mills v. Union of India (1980)", "மினர்வா மில்ஸ் எதிர் இந்திய ஒன்றியம் (1980)",
        "Maneka Gandhi v. Union of India (1978)", "மேனகா காந்தி எதிர் இந்திய ஒன்றியம் (1978)",
        "A",
        "In I.R. Coelho v. State of Tamil Nadu (2007), a unanimous 9-judge bench ruled that any law placed in the Ninth Schedule on or after April 24, 1973 is open to judicial challenge if it violates the Basic Structure or fundamental rights under Articles 14, 19, and 21.",
        "2007-ல் ஐ.ஆர். கோயல்ஹோ எதிர் தமிழ்நாடு அரசு வழக்கில், 9 நீதிபதிகள் கொண்ட அமர்வு, 1973 ஏப்ரல் 24-க்குப் பிறகு ஒன்பதாவது அட்டவணையில் சேர்க்கப்பட்ட எந்தவொரு சட்டமும் அடிப்படை அமைப்பு அல்லது உறுப்புகள் 14, 19, 21-ஐ மீறினால் நீதிமன்ற மறுஆய்வுக்கு உட்பட்டது என்று தீர்ப்பளித்தது.",
        "Correct. I.R. Coelho Case established review of post-1973 Ninth Schedule laws.", "சரியானது. ஐ.ஆர். கோயல்ஹோ வழக்கு 1973-க்குப் பிந்தைய 9வது அட்டவணைச் சட்டங்களின் மறுஆய்வை உறுதிப்படுத்தியது.",
        "Incorrect. Kesavananda Bharati propounded the Basic Structure doctrine.", "தவறானது. கேசவாநந்த பாரதி அடிப்படை அமைப்புக் கோட்பாட்டை உருவாக்கியது.",
        "Incorrect. Minerva Mills struck down clauses 4 and 5 of Art 368.", "தவறானது. மினர்வா மில்ஸ் உறுப்பு 368-ன் உட்பிரிவுகள் 4 மற்றும் 5-ஐ ரத்து செய்தது.",
        "Incorrect. Maneka Gandhi expanded Article 21.", "தவறானது. மேனகா காந்தி உறுப்பு 21-ஐ விரிவுபடுத்தியது.",
        "Cutoff date for Ninth Schedule immunity: April 24, 1973 (Kesavananda Bharati judgment date).",
        "ஒன்பதாவது அட்டவணைப் பாதுகாப்பிற்கான காலக்கெடு தேதி: ஏப்ரல் 24, 1973 (கேசவாநந்த பாரதி தீர்ப்பு நாள்).",
        "I.R. Coelho judgment was delivered by a 9-judge constitutional bench headed by CJI Y.K. Sabharwal.",
        "ஐ.ஆர். கோயல்ஹோ தீர்ப்பு தலைமை நீதிபதி ஒய்.கே. சபர்வால் தலைமையிலான 9 நீதிபதிகள் கொண்ட அரசியலமைப்பு அமர்வால் வழங்கப்பட்டது."
    ))

    qs.append(make_sch_q(
        "SCH_E_044", "Easy", "Conceptual", "Tenth Schedule",
        "What is the minimum proportion of members required for a valid political party merger under the Tenth Schedule as amended by the 91st Amendment Act, 2003?",
        "2003-ன் 91வது திருத்தச் சட்டத்தின்படி, பத்தாவது அட்டவணையின் கீழ் முறையான கட்சி இணைப்பிற்குத் தேவையான குறைந்தபட்ச உறுப்பினர் பங்கு என்ன?",
        "Two-thirds (2/3rd) of the members", "மூன்றில் இரண்டு பங்கு (2/3) உறுப்பினர்கள்",
        "One-third (1/3rd) of the members", "மூன்றில் ஒரு பங்கு (1/3) உறுப்பினர்கள்",
        "One-half (1/2) of the members", "பாதி (1/2) உறுப்பினர்கள்",
        "Three-fourths (3/4th) of the members", "நான்கில் மூன்று பங்கு (3/4) உறுப்பினர்கள்",
        "A",
        "The 91st Constitutional Amendment Act, 2003 eliminated the protection for a split by 1/3rd members and mandated that a merger is valid only if at least two-thirds (2/3rd) of the members of the legislative party agree.",
        "2003-ன் 91வது அரசியலமைப்புத் திருத்தச் சட்டம் 1/3 உறுப்பினர்களின் பிளவிற்கான பாதுகாப்பை நீக்கியது மற்றும் சட்டமன்றக் கட்சியின் குறைந்தது மூன்றில் இரண்டு பங்கு (2/3) உறுப்பினர்கள் ஒப்புக்கொண்டால் மட்டுமே இணைப்பு செல்லும் என கட்டாயமாக்கியது.",
        "Correct. 91st CAA mandated 2/3rd majority for merger.", "சரியானது. 91வது திருத்தம் இணைப்பிற்கு 2/3 பெரும்பான்மையைக் கட்டாயமாக்கியது.",
        "Incorrect. 1/3rd split provision was deleted by the 91st amendment.", "தவறானது. 1/3 பிளவு விதி 91வது திருத்தத்தால் நீக்கப்பட்டது.",
        "Incorrect. Simple half is not the threshold.", "தவறானது. பாதி என்பது வரம்பு அல்ல.",
        "Incorrect. 3/4th is incorrect.", "தவறானது. 3/4 என்பது தவறானது.",
        "Tenth Schedule merger threshold = at least 2/3rd members (91st CAA 2003).",
        "10வது அட்டவணை கட்சி இணைப்பு வரம்பு = குறைந்தது 2/3 உறுப்பினர்கள் (91வது திருத்தம் 2003).",
        "Prior to 2003, a split involving 1/3rd of the members was protected from disqualification.",
        "2003-க்கு முன்பு, 1/3 பங்கு உறுப்பினர்கள் கொண்ட பிளவு தகுதிநீக்கத்திலிருந்து பாதுகாக்கப்பட்டது."
    ))

    qs.append(make_sch_q(
        "SCH_E_045", "Easy", "Conceptual", "Eleventh Schedule",
        "Which of the following functional items is included in the Eleventh Schedule of the Indian Constitution?",
        "பின்வரும் செயல்பாட்டுத் துறைகளில் எது இந்திய அரசியலமைப்பின் பதினோராவது அட்டவணையில் சேர்க்கப்பட்டுள்ளது?",
        "Minor irrigation, water management, and watershed development", "சிறு பாசனம், நீர் மேலாண்மை மற்றும் நீர்ப்பிடிப்புப் பகுதி மேம்பாடு",
        "Urban planning including town planning", "நகர அமைப்பு உள்ளிட்ட நகர்ப்புறத் திட்டமிடல்",
        "Fire services", "தீயணைப்பு சேவைகள்",
        "Regulation of slaughterhouses and tanneries", "இறைச்சிக் கூடங்கள் மற்றும் தோல் பதனிடும் தொழிற்சாலைகளை ஒழுங்குபடுத்துதல்",
        "A",
        "Minor irrigation, water management, and watershed development is Entry 3 in the Eleventh Schedule for Panchayats. Urban planning, fire services, and slaughterhouses are in the Twelfth Schedule for Municipalities.",
        "சிறு பாசனம், நீர் மேலாண்மை மற்றும் நீர்ப்பிடிப்பு மேம்பாடு ஆகியவை பஞ்சாயத்துகளுக்கான 11வது அட்டவணையில் பதிவு 3 ஆக உள்ளன. நகரத் திட்டமிடல், தீயணைப்பு மற்றும் இறைச்சிக் கூடங்கள் நகராட்சிகளுக்கான 12வது அட்டவணையில் உள்ளன.",
        "Correct. Minor irrigation is in Eleventh Schedule (Panchayats).", "சரியானது. சிறு பாசனம் 11வது அட்டவணையில் (பஞ்சாயத்துகள்) உள்ளது.",
        "Incorrect. Urban planning is in Twelfth Schedule.", "தவறானது. நகர்ப்புறத் திட்டமிடல் 12வது அட்டவணையில் உள்ளது.",
        "Incorrect. Fire services is in Twelfth Schedule.", "தவறானது. தீயணைப்பு சேவைகள் 12வது அட்டவணையில் உள்ளன.",
        "Incorrect. Slaughterhouses regulation is in Twelfth Schedule.", "தவறானது. இறைச்சிக் கூடங்கள் ஒழுங்குமுறை 12வது அட்டவணையில் உள்ளது.",
        "Eleventh Schedule = Rural development & Panchayats; Twelfth Schedule = Urban services & Municipalities.",
        "11வது அட்டவணை = ஊரக வளர்ச்சி & பஞ்சாயத்துகள்; 12வது அட்டவணை = நகர்ப்புற சேவைகள் & நகராட்சிகள்.",
        "Entry 1 of Eleventh Schedule is Agriculture, including agricultural extension.",
        "பதினோராவது அட்டவணையின் முதல் பதிவு விவசாயம் மற்றும் விவசாய விரிவாக்கம் ஆகும்."
    ))

    qs.append(make_sch_q(
        "SCH_E_046", "Easy", "Conceptual", "Twelfth Schedule",
        "Which of the following subjects is an entry in the Twelfth Schedule of the Constitution for Municipalities?",
        "பின்வரும் துறைகளில் எது நகராட்சிகளுக்கான அரசியலமைப்பின் பன்னிரண்டாவது அட்டவணையில் ஒரு பதிவாக உள்ளது?",
        "Solid waste management, public health, and sanitation", "திடக்கழிவு மேலாண்மை, பொது சுகாதாரம் மற்றும் துப்புரவு",
        "Animal husbandry, dairying, and poultry", "கால்நடை பராமரிப்பு, பால் பண்ணை மற்றும் கோழி வளர்ப்பு",
        "Khadi, village, and cottage industries", "காதர், கிராம மற்றும் குடிசைத் தொழில்கள்",
        "Poverty alleviation programmes in rural areas", "கிராமப்புற வறுமை ஒழிப்புத் திட்டங்கள்",
        "A",
        "Public health, sanitation, conservancy, and solid waste management is Entry 6 in the Twelfth Schedule for Municipalities. Animal husbandry, khadi, and poverty alleviation are in the Eleventh Schedule for Panchayats.",
        "பொது சுகாதாரம், துப்புரவு மற்றும் திடக்கழிவு மேலாண்மை ஆகியவை நகராட்சிகளுக்கான பன்னிரண்டாவது அட்டவணையில் 6வது பதிவாக உள்ளன. கால்நடை பராமரிப்பு, காதி மற்றும் வறுமை ஒழிப்பு ஆகியவை பஞ்சாயத்துகளுக்கான 11வது அட்டவணையில் உள்ளன.",
        "Correct. Solid waste management is in Twelfth Schedule.", "சரியானது. திடக்கழிவு மேலாண்மை 12வது அட்டவணையில் உள்ளது.",
        "Incorrect. Animal husbandry is in Eleventh Schedule.", "தவறானது. கால்நடை பராமரிப்பு 11வது அட்டவணையில் உள்ளது.",
        "Incorrect. Khadi and cottage industries are in Eleventh Schedule.", "தவறானது. காதி மற்றும் குடிசைத் தொழில்கள் 11வது அட்டவணையில் உள்ளன.",
        "Incorrect. Rural poverty alleviation is in Eleventh Schedule.", "தவறானது. கிராமப்புற வறுமை ஒழிப்பு 11வது அட்டவணையில் உள்ளது.",
        "Twelfth Schedule = Urban infrastructure, public health, solid waste management.",
        "பன்னிரண்டாவது அட்டவணை = நகர்ப்புற உள்கட்டமைப்பு, பொது சுகாதாரம், திடக்கழிவு மேலாண்மை.",
        "The Twelfth Schedule contains exactly 18 functional items.",
        "பன்னிரண்டாவது அட்டவணை சரியாக 18 செயல்பாட்டுத் துறைகளைக் கொண்டுள்ளது."
    ))

    qs.append(make_sch_q(
        "SCH_E_047", "Easy", "Conceptual", "Schedules Overview",
        "Which Schedule was added to the Indian Constitution by the 73rd Amendment Act, 1992?",
        "1992-ன் 73வது திருத்தச் சட்டத்தால் இந்திய அரசியலமைப்பில் எந்த அட்டவணை சேர்க்கப்பட்டது?",
        "Eleventh Schedule", "பதினோராவது அட்டவணை",
        "Twelfth Schedule", "பன்னிரண்டாவது அட்டவணை",
        "Tenth Schedule", "பத்தாவது அட்டவணை",
        "Ninth Schedule", "ஒன்பதாவது அட்டவணை",
        "A",
        "The 73rd Constitutional Amendment Act, 1992 added the Eleventh Schedule detailing the powers of Panchayats.",
        "1992-ன் 73வது அரசியலமைப்புத் திருத்தச் சட்டம் பஞ்சாயத்துகளின் அதிகாரங்களை விவரிக்கும் பதினோராவது அட்டவணையைச் சேர்த்தது.",
        "Correct. 73rd CAA added the Eleventh Schedule.", "சரியானது. 73வது திருத்தம் 11வது அட்டவணையைச் சேர்த்தது.",
        "Incorrect. 74th CAA added the Twelfth Schedule.", "தவறானது. 74வது திருத்தம் 12வது அட்டவணையைச் சேர்த்தது.",
        "Incorrect. 52nd CAA added the Tenth Schedule.", "தவறானது. 52வது திருத்தம் 10வது அட்டவணையைச் சேர்த்தது.",
        "Incorrect. 1st CAA added the Ninth Schedule.", "தவறானது. 1வது திருத்தம் 9வது அட்டவணையைச் சேர்த்தது.",
        "73rd CAA = 11th Schedule (Panchayats); 74th CAA = 12th Schedule (Municipalities).",
        "73வது திருத்தம் = 11வது அட்டவணை (பஞ்சாயத்துகள்); 74வது திருத்தம் = 12வது அட்டவணை (நகராட்சிகள்).",
        "Both amendments were enacted in 1992 and enforced in 1993.",
        "இரண்டு திருத்தங்களும் 1992-ல் இயற்றப்பட்டு 1993-ல் நடைமுறைக்கு வந்தன."
    ))

    qs.append(make_sch_q(
        "SCH_E_048", "Easy", "Conceptual", "Eighth Schedule",
        "By which Constitutional Amendment Act was 'Oriya' renamed as 'Odia' in the Eighth Schedule?",
        "எந்த அரசியலமைப்புத் திருத்தச் சட்டத்தின் மூலம் எட்டாவது அட்டவணையில் 'ஒரியா' என்பது 'ஒடியா' எனப் பெயர் மாற்றம் செய்யப்பட்டது?",
        "96th Amendment Act, 2011", "96வது திருத்தச் சட்டம், 2011",
        "92nd Amendment Act, 2003", "92வது திருத்தச் சட்டம், 2003",
        "71st Amendment Act, 1992", "71வது திருத்தச் சட்டம், 1992",
        "21st Amendment Act, 1967", "21வது திருத்தச் சட்டம், 1967",
        "A",
        "The 96th Constitutional Amendment Act, 2011 substituted the word 'Odia' for 'Oriya' in the Eighth Schedule.",
        "2011-ன் 96வது அரசியலமைப்புத் திருத்தச் சட்டம் எட்டாவது அட்டவணையில் 'ஒரியா' என்ற சொல்லுக்குப் பதிலாக 'ஒடியா' என மாற்றியது.",
        "Correct. 96th CAA 2011 substituted Odia for Oriya.", "சரியானது. 96வது திருத்தம் 2011 ஒரியாவை ஒடியா என மாற்றியது.",
        "Incorrect. 92nd CAA added BDMS in 2003.", "தவறானது. 92வது திருத்தம் 2003-ல் BDMS மொழிகளைச் சேர்த்தது.",
        "Incorrect. 71st CAA added KMN in 1992.", "தவறானது. 71வது திருத்தம் 1992-ல் KMN மொழிகளைச் சேர்த்தது.",
        "Incorrect. 21st CAA added Sindhi in 1967.", "தவறானது. 21வது திருத்தம் 1967-ல் சிந்தியைச் சேர்த்தது.",
        "96th CAA 2011: Oriya → Odia in Eighth Schedule.",
        "96வது திருத்தம் 2011: எட்டாவது அட்டவணையில் ஒரியா → ஒடியா என மாற்றம்.",
        "Simultaneously, the Orissa (Alteration of Name) Act, 2011 renamed the State from Orissa to Odisha.",
        "அதே நேரத்தில், ஒரிசா (பெயர் மாற்றம்) சட்டம் 2011 மூலம் மாநிலத்தின் பெயர் ஒரிசாவிலிருந்து ஒடிசா என மாற்றப்பட்டது."
    ))

    qs.append(make_sch_q(
        "SCH_E_049", "Easy", "Conceptual", "Schedules Overview",
        "How many Schedules were added to the Constitution of India after its commencement in 1950?",
        "1950-ல் நடைமுறைக்கு வந்த பிறகு இந்திய அரசியலமைப்பில் எத்தனை அட்டவணைகள் புதிதாகச் சேர்க்கப்பட்டன?",
        "4 Schedules (9th, 10th, 11th, and 12th)", "4 அட்டவணைகள் (9, 10, 11 மற்றும் 12)",
        "2 Schedules (9th and 10th)", "2 அட்டவணைகள் (9 மற்றும் 10)",
        "3 Schedules (10th, 11th, and 12th)", "3 அட்டவணைகள் (10, 11 மற்றும் 12)",
        "6 Schedules", "6 அட்டவணைகள்",
        "A",
        "The Constitution originally had 8 Schedules in 1950. Exactly 4 Schedules (9th in 1951, 10th in 1985, 11th in 1992, and 12th in 1992) have been added, making a total of 12 Schedules.",
        "1950-ல் அரசியலமைப்பில் 8 அட்டவணைகள் இருந்தன. அதன் பிறகு சரியாக 4 அட்டவணைகள் (1951-ல் 9வது, 1985-ல் 10வது, 1992-ல் 11வது, 1992-ல் 12வது) சேர்க்கப்பட்டு மொத்தம் 12 அட்டவணைகள் உள்ளன.",
        "Correct. Exactly 4 schedules have been added since 1950.", "சரியானது. 1950-க்குப் பிறகு சரியாக 4 அட்டவணைகள் சேர்க்கப்பட்டுள்ளன.",
        "Incorrect. 11th and 12th were also added.", "தவறானது. 11 மற்றும் 12வது அட்டவணைகளும் சேர்க்கப்பட்டன.",
        "Incorrect. 9th schedule was also added.", "தவறானது. 9வது அட்டவணையும் சேர்க்கப்பட்டது.",
        "Incorrect. 6 is incorrect; 8 + 4 = 12.", "தவறானது. 8 + 4 = 12 அட்டவணைகளே உள்ளன.",
        "8 original + 4 added = 12 total Schedules.",
        "8 அசல் + 4 சேர்க்கப்பட்டவை = மொத்தம் 12 அட்டவணைகள்.",
        "Amendments that added schedules: 1st (9th), 52nd (10th), 73rd (11th), 74th (12th).",
        "அட்டவணைகளைச் சேர்த்த திருத்தங்கள்: 1வது (9வது), 52வது (10வது), 73வது (11வது), 74வது (12வது)."
    ))

    qs.append(make_sch_q(
        "SCH_E_050", "Easy", "Conceptual", "Schedules Overview",
        "Which of the following pairs of Schedule and Subject is INCORRECTLY matched?",
        "அட்டவணை மற்றும் துறை தொடர்பான பின்வரும் இணைகளில் எது தவறாகப் பொருத்தப்பட்டுள்ளது?",
        "Third Schedule – Salaries of Judges", "மூன்றாவது அட்டவணை – நீதிபதிகளின் சம்பளங்கள்",
        "First Schedule – Names of States and Union Territories", "முதல் அட்டவணை – மாநிலங்கள் மற்றும் யூனியன் பிரதேசங்களின் பெயர்கள்",
        "Fourth Schedule – Allocation of seats in Rajya Sabha", "நான்காவது அட்டவணை – மாநிலங்களவை இடங்கள் ஒதுக்கீடு",
        "Tenth Schedule – Provisions as to disqualification on ground of defection", "பத்தாவது அட்டவணை – கட்சித் தாவல் தொடர்பான தகுதிநீக்க விதிகள்",
        "A",
        "The Third Schedule deals with Forms of Oaths and Affirmations. Salaries of Judges and other constitutional authorities are governed by the Second Schedule.",
        "மூன்றாவது அட்டவணை பதவிப் பிரமாண படிவங்களைக் கையாள்கிறது. நீதிபதிகள் மற்றும் பிற அதிகாரிகளின் சம்பளங்கள் இரண்டாவது அட்டவணையில் உள்ளன.",
        "Correct. Third Schedule is for Oaths, NOT Salaries.", "சரியானது. மூன்றாவது அட்டவணை பிரமாணங்களுக்கானது, சம்பளங்களுக்கு அல்ல.",
        "Incorrect. First Schedule correctly lists States and UTs.", "தவறானது. முதல் அட்டவணை சரியாக மாநிலங்கள் & UTகளைக் குறிக்கிறது.",
        "Incorrect. Fourth Schedule correctly allocates Rajya Sabha seats.", "தவறானது. நான்காவது அட்டவணை சரியாக மாநிலங்களவை இடங்களை ஒதுக்குகிறது.",
        "Incorrect. Tenth Schedule correctly deals with Anti-Defection.", "தவறானது. பத்தாவது அட்டவணை சரியாக கட்சித் தாவலைக் கையாள்கிறது.",
        "Schedule 2 = Salaries; Schedule 3 = Oaths.", "அட்டவணை 2 = சம்பளங்கள்; அட்டவணை 3 = பிரமாணங்கள்.",
        "Always remember: Schedule 2 comes before Schedule 3 (Salaries come before Oaths).",
        "எப்போதும் நினைவில் கொள்க: சம்பளம் (2வது அட்டவணை) பிரமாணத்திற்கு (3வது அட்டவணை) முன்பே வருகிறது."
    ))

    return qs

def main():
    import sys
    sys.path.insert(0, os.path.dirname(__file__))
    from schedules_medium_data import get_medium_questions
    from schedules_hard_data import get_hard_questions

    easy_qs = get_easy_questions()
    med_qs = get_medium_questions()
    hard_qs = get_hard_questions()

    print(f"Loaded: Easy={len(easy_qs)}, Medium={len(med_qs)}, Hard={len(hard_qs)}")
    assert len(easy_qs) == 50, f"Expected 50 Easy, got {len(easy_qs)}"
    assert len(med_qs) == 50, f"Expected 50 Medium, got {len(med_qs)}"
    assert len(hard_qs) == 50, f"Expected 50 Hard, got {len(hard_qs)}"

    # Balance and shuffle keys (anti-block distribution rule)
    easy_balanced = balance_question_keys(easy_qs, seed=101)
    med_balanced = balance_question_keys(med_qs, seed=202)
    hard_balanced = balance_question_keys(hard_qs, seed=303)

    out_dir = os.path.join(os.path.dirname(__file__), "..", "data", "questions", "polity")
    os.makedirs(out_dir, exist_ok=True)

    files = [
        ("constitutional_schedules_easy.json", easy_balanced),
        ("constitutional_schedules_medium.json", med_balanced),
        ("constitutional_schedules_hard.json", hard_balanced)
    ]

    for fname, data in files:
        fpath = os.path.join(out_dir, fname)
        with open(fpath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Saved {len(data)} questions to {fpath}")

if __name__ == "__main__":
    main()
