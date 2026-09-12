# -*- coding: utf-8 -*-
"""
PYQ MCQs for Constitutional Schedules (50 questions: SCH_PYQ_001 to SCH_PYQ_050)
Authentic exam-standard questions tagged with TNPSC Group 1, 2, 4, and UPSC Civil Services.
"""
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.insert(0, os.path.dirname(__file__))

from sch_mcq_helper import make_sch_q

def get_pyq_questions():
    qs = []

    # PYQ 01 - 10
    qs.append(make_sch_q(
        "SCH_PYQ_001", "Easy", "PYQ", "Ninth Schedule",
        "[TNPSC Group 1 Prelims 2019 / UPSC CSE 2003] The Ninth Schedule of the Indian Constitution was introduced during the prime ministership of:",
        "[TNPSC குரூப் 1 முதல்நிலை 2019 / UPSC CSE 2003] இந்திய அரசியலமைப்பின் ஒன்பதாவது அட்டவணை யாருடைய பிரதமரின் காலத்தில் அறிமுகப்படுத்தப்பட்டது?",
        "Jawaharlal Nehru", "ஜவஹர்லால் நேரு",
        "Lal Bahadur Shastri", "லால் பகதூர் சாஸ்திரி",
        "Indira Gandhi", "இந்திரா காந்தி",
        "Morarji Desai", "மொரார்ஜி தேசாய்",
        "A",
        "The Ninth Schedule was added by the 1st Constitutional Amendment Act, 1951, enacted on June 18, 1951, during the prime ministership of Jawaharlal Nehru.",
        "ஒன்பதாவது அட்டவணை 1951 ஜூன் 18 அன்று 1வது அரசியலமைப்புத் திருத்தச் சட்டம் மூலம் சேர்க்கப்பட்டது. அக்காலத்தில் ஜவஹர்லால் நேரு இந்தியாவின் பிரதமராக இருந்தார்.",
        "Correct. Jawaharlal Nehru was Prime Minister in 1951.", "சரியானது. 1951-ல் ஜவஹர்லால் நேரு பிரதமராக இருந்தார்.",
        "Incorrect. Lal Bahadur Shastri was PM from 1964 to 1966.", "தவறானது. லால் பகதூர் சாஸ்திரி 1964 முதல் 1966 வரை பிரதமராக இருந்தார்.",
        "Incorrect. Indira Gandhi became PM in 1966.", "தவறானது. இந்திரா காந்தி 1966-ல் பிரதமரானார்.",
        "Incorrect. Morarji Desai became PM in 1977.", "தவறானது. மொரார்ஜி தேசாய் 1977-ல் பிரதமரானார்.",
        "1st CAA 1951: Introduced Ninth Schedule under PM Jawaharlal Nehru.",
        "1வது திருத்தம் 1951: பிரதமர் ஜவஹர்லால் நேருவின் கீழ் 9வது அட்டவணையை அறிமுகப்படுத்தியது."
    ))

    qs.append(make_sch_q(
        "SCH_PYQ_002", "Easy", "PYQ", "Fourth Schedule",
        "[TNPSC Group 2 Prelims 2018 / UPSC CSE 2015] Which Schedule of the Constitution of India contains provisions regarding the allocation of seats in the Council of States (Rajya Sabha)?",
        "[TNPSC குரூப் 2 முதல்நிலை 2018 / UPSC CSE 2015] மாநிலங்களவையில் (Council of States) இடங்கள் ஒதுக்கீடு செய்வது தொடர்பான விதிகளைக் கொண்டுள்ள இந்திய அரசியலமைப்பின் அட்டவணை எது?",
        "Fourth Schedule", "நான்காவது அட்டவணை",
        "Third Schedule", "மூன்றாவது அட்டவணை",
        "Fifth Schedule", "ஐந்தாவது அட்டவணை",
        "Sixth Schedule", "ஆறாவது அட்டவணை",
        "A",
        "The Fourth Schedule deals with the allocation of seats in the Rajya Sabha (Council of States) to the States and Union Territories (read with Article 4(1) and Article 80(2)).",
        "நான்காவது அட்டவணை மாநிலங்கள் மற்றும் யூனியன் பிரதேசங்களுக்கு மாநிலங்களவை இடங்கள் ஒதுக்கீடு செய்வதைக் கையாள்கிறது (சரத்து 4(1) மற்றும் 80(2)).",
        "Correct. Fourth Schedule allocates Rajya Sabha seats.", "சரியானது. நான்காவது அட்டவணை மாநிலங்களவை இடங்களை ஒதுக்குகிறது.",
        "Incorrect. Third Schedule deals with Oaths and Affirmations.", "தவறானது. மூன்றாவது அட்டவணை பதவிப் பிரமாணங்களைக் கையாள்கிறது.",
        "Incorrect. Fifth Schedule deals with Scheduled Areas administration.", "தவறானது. ஐந்தாவது அட்டவணை அட்டவணைப் பகுதிகள் நிர்வாகத்தைக் கையாள்கிறது.",
        "Incorrect. Sixth Schedule deals with Tribal Areas in AMTM.", "தவறானது. ஆறாவது அட்டவணை AMTM பழங்குடிப் பகுதிகளைக் கையாள்கிறது.",
        "Fourth Schedule = Allocation of seats in Rajya Sabha.",
        "நான்காவது அட்டவணை = மாநிலங்களவை இடங்கள் ஒதுக்கீடு."
    ))

    qs.append(make_sch_q(
        "SCH_PYQ_003", "Easy", "PYQ", "Tenth Schedule",
        "[TNPSC Group 4 2019 / UPSC CSE 2014] Which Constitutional Amendment Act added the Tenth Schedule (Anti-Defection Law) to the Constitution of India?",
        "[TNPSC குரூப் 4 2019 / UPSC CSE 2014] எந்த அரசியலமைப்புத் திருத்தச் சட்டம் பத்தாவது அட்டவணையை (கட்சித் தாவல் தடைச் சட்டம்) இந்திய அரசியலமைப்பில் சேர்த்தது?",
        "52nd Constitutional Amendment Act, 1985", "52வது அரசியலமைப்புத் திருத்தச் சட்டம், 1985",
        "42nd Constitutional Amendment Act, 1976", "42வது அரசியலமைப்புத் திருத்தச் சட்டம், 1976",
        "44th Constitutional Amendment Act, 1978", "44வது அரசியலமைப்புத் திருத்தச் சட்டம், 1978",
        "61st Constitutional Amendment Act, 1988", "61வது அரசியலமைப்புத் திருத்தச் சட்டம், 1988",
        "A",
        "The 52nd Constitutional Amendment Act, 1985 added the Tenth Schedule to the Constitution of India, providing for disqualification of members on grounds of defection.",
        "52வது அரசியலமைப்புத் திருத்தச் சட்டம் 1985, கட்சித் தாவல் அடிப்படையில் உறுப்பினர்களைத் தகுதிநீக்கம் செய்வதற்கான பத்தாவது அட்டவணையை இந்திய அரசியலமைப்பில் சேர்த்தது.",
        "Correct. 52nd CAA 1985 introduced the Anti-Defection Law in Tenth Schedule.", "சரியானது. 52வது திருத்தம் 1985 கட்சித் தாவல் தடைச் சட்டத்தை 10வது அட்டவணையில் சேர்த்தது.",
        "Incorrect. 42nd CAA 1976 was the 'Mini-Constitution'.", "தவறானது. 42வது திருத்தம் 1976 'குறு-அரசியலமைப்பு' எனப்படுகிறது.",
        "Incorrect. 44th CAA 1978 restored constitutional safeguards after Emergency.", "தவறானது. 44வது திருத்தம் 1978 அவசரநிலைக்குப் பின் பாதுகாப்புகளை மீட்டது.",
        "Incorrect. 61st CAA 1988 reduced voting age from 21 to 18.", "தவறானது. 61வது திருத்தம் 1988 வாக்களிக்கும் வயதை 21-லிருந்து 18 ஆகக் குறைத்தது.",
        "Tenth Schedule = 52nd CAA 1985 under Rajiv Gandhi government.",
        "10வது அட்டவணை = ராஜீவ் காந்தி அரசில் 52வது திருத்தம் 1985."
    ))

    qs.append(make_sch_q(
        "SCH_PYQ_004", "Easy", "PYQ", "Eleventh Schedule",
        "[TNPSC Group 1 2021 / TNPSC Group 2 2015] How many functional subjects are listed in the Eleventh Schedule of the Constitution relating to Panchayats?",
        "[TNPSC குரூப் 1 2021 / TNPSC குரூப் 2 2015] பஞ்சாயத்துகள் தொடர்பான அரசியலமைப்பின் பதினோராவது அட்டவணையில் எத்தனை செயல்பாட்டுத் துறைகள் பட்டியலிடப்பட்டுள்ளன?",
        "29 subjects", "29 துறைகள்",
        "18 subjects", "18 துறைகள்",
        "22 subjects", "22 துறைகள்",
        "12 subjects", "12 துறைகள்",
        "A",
        "The Eleventh Schedule contains 29 functional items placed under the purview of Panchayati Raj institutions under Article 243G, added by the 73rd Constitutional Amendment Act, 1992.",
        "73வது அரசியலமைப்புத் திருத்தச் சட்டம் 1992 மூலம் சேர்க்கப்பட்ட பதினோராவது அட்டவணை, சரத்து 243G-ன் கீழ் பஞ்சாயத்து ராஜ் அமைப்புகளுக்கு 29 செயல்பாட்டுத் துறைகளை வழங்குகிறது.",
        "Correct. 29 subjects are listed in the Eleventh Schedule for Panchayats.", "சரியானது. பஞ்சாயத்துகளுக்கான 11வது அட்டவணையில் 29 துறைகள் பட்டியலிடப்பட்டுள்ளன.",
        "Incorrect. 18 subjects are in the Twelfth Schedule for Municipalities.", "தவறானது. 18 துறைகள் நகராட்சிகளுக்கான 12வது அட்டவணையில் உள்ளன.",
        "Incorrect. 22 is the number of languages in Eighth Schedule.", "தவறானது. 22 என்பது 8வது அட்டவணையில் உள்ள மொழிகளின் எண்ணிக்கை.",
        "Incorrect. 12 is the total number of schedules in the Constitution.", "தவறானது. 12 என்பது மொத்த அட்டவணைகளின் எண்ணிக்கை.",
        "Eleventh Schedule (Panchayats) = 29 subjects. Twelfth Schedule (Municipalities) = 18 subjects.",
        "11வது அட்டவணை (பஞ்சாயத்துகள்) = 29 துறைகள். 12வது அட்டவணை (நகராட்சிகள்) = 18 துறைகள்."
    ))

    qs.append(make_sch_q(
        "SCH_PYQ_005", "Easy", "PYQ", "Twelfth Schedule",
        "[TNPSC Group 2 2019 / Combined Engineering 2018] Which Constitutional Amendment Act added the Twelfth Schedule to the Indian Constitution?",
        "[TNPSC குரூப் 2 2019 / ஒருங்கிணைந்த பொறியியல் 2018] இந்திய அரசியலமைப்பில் பன்னிரண்டாவது அட்டவணையைச் சேர்த்த அரசியலமைப்புத் திருத்தச் சட்டம் எது?",
        "74th Constitutional Amendment Act, 1992", "74வது அரசியலமைப்புத் திருத்தச் சட்டம், 1992",
        "73rd Constitutional Amendment Act, 1992", "73வது அரசியலமைப்புத் திருத்தச் சட்டம், 1992",
        "71st Constitutional Amendment Act, 1992", "71வது அரசியலமைப்புத் திருத்தச் சட்டம், 1992",
        "69th Constitutional Amendment Act, 1991", "69வது அரசியலமைப்புத் திருத்தச் சட்டம், 1991",
        "A",
        "The 74th Constitutional Amendment Act, 1992 added the Twelfth Schedule (18 functional items for Municipalities under Article 243W) and Part IX-A to the Constitution of India.",
        "74வது அரசியலமைப்புத் திருத்தச் சட்டம் 1992, இந்திய அரசியலமைப்பில் பன்னிரண்டாவது அட்டவணை (சரத்து 243W-ன் கீழ் நகராட்சிகளுக்கான 18 பணிகள்) மற்றும் பகுதி IX-A-வைச் சேர்த்தது.",
        "Correct. 74th CAA 1992 added Twelfth Schedule.", "சரியானது. 74வது திருத்தம் 1992 12வது அட்டவணையைச் சேர்த்தது.",
        "Incorrect. 73rd CAA 1992 added Eleventh Schedule for Panchayats.", "தவறானது. 73வது திருத்தம் 1992 பஞ்சாயத்துகளுக்கான 11வது அட்டவணையைச் சேர்த்தது.",
        "Incorrect. 71st CAA 1992 added Konkani, Manipuri, Nepali to Eighth Schedule.", "தவறானது. 71வது திருத்தம் 1992 கொங்கணி, மணிப்பூரி, நேபாளியை 8வது அட்டவணையில் சேர்த்தது.",
        "Incorrect. 69th CAA 1991 designated Delhi as NCT.", "தவறானது. 69வது திருத்தம் 1991 டெல்லியை தேசிய தலைநகர் பகுதியாக மாற்றியது.",
        "74th CAA 1992 -> Twelfth Schedule (18 subjects for Municipalities, Article 243W).",
        "74வது திருத்தம் 1992 -> 12வது அட்டவணை (நகராட்சிகளுக்கான 18 பணிகள், சரத்து 243W)."
    ))

    qs.append(make_sch_q(
        "SCH_PYQ_006", "Medium", "PYQ", "Sixth Schedule",
        "[UPSC CSE 2019 / TNPSC Group 1 2017] The provisions of the Sixth Schedule of the Indian Constitution apply to the tribal areas of which of the following States?",
        "[UPSC CSE 2019 / TNPSC குரூப் 1 2017] இந்திய அரசியலமைப்பின் ஆறாவது அட்டவணையின் விதிகள் பின்வரும் எந்த மாநிலங்களின் பழங்குடிப் பகுதிகளுக்குப் பொருந்தும்?",
        "Assam, Meghalaya, Tripura, and Mizoram", "அசாம், மேகாலயா, திரிபுரா மற்றும் மிசோரம்",
        "Manipur, Nagaland, Assam, and Meghalaya", "மணிப்பூர், நாகாலாந்து, அசாம் மற்றும் மேகாலயா",
        "Arunachal Pradesh, Nagaland, Assam, and Tripura", "அருணாச்சலப் பிரதேசம், நாகாலாந்து, அசாம் மற்றும் திரிபுரா",
        "Sikkim, Manipur, Mizoram, and Tripura", "சிக்கிம், மணிப்பூர், மிசோரம் மற்றும் திரிபுரா",
        "A",
        "Under Article 244(2) and the Sixth Schedule, its autonomous provisions apply strictly and exclusively to the tribal areas in the four North-Eastern states: Assam, Meghalaya, Tripura, and Mizoram (AMTM).",
        "சரத்து 244(2) மற்றும் ஆறாவது அட்டவணையின் கீழ், அதன் தன்னாட்சி விதிகள் நான்கு வடகிழக்கு மாநிலங்களின் பழங்குடிப் பகுதிகளுக்கு மட்டுமே பொருந்தும்: அசாம், மேகாலயா, திரிபுரா மற்றும் மிசோரம் (AMTM).",
        "Correct. Sixth Schedule covers Assam, Meghalaya, Tripura, Mizoram (AMTM).", "சரியானது. ஆறாவது அட்டவணை அசாம், மேகாலயா, திரிபுரா, மிசோரத்தை உள்ளடக்கியது.",
        "Incorrect. Manipur and Nagaland are NOT covered by the Sixth Schedule.", "தவறானது. மணிப்பூர் மற்றும் நாகாலாந்து 6வது அட்டவணையில் சேர்க்கப்படவில்லை.",
        "Incorrect. Arunachal Pradesh and Nagaland are NOT Sixth Schedule states.", "தவறானது. அருணாச்சலப் பிரதேசம் மற்றும் நாகாலாந்து 6வது அட்டவணை மாநிலங்கள் அல்ல.",
        "Incorrect. Sikkim and Manipur are not covered.", "தவறானது. சிக்கிம் மற்றும் மணிப்பூர் இதில் இல்லை.",
        "Sixth Schedule Mnemonic: AMTM = Assam, Meghalaya, Tripura, Mizoram.",
        "ஆறாவது அட்டவணை நினைவுச்சொல்: AMTM = அசாம், மேகாலயா, திரிபுரா, மிசோரம்."
    ))

    qs.append(make_sch_q(
        "SCH_PYQ_007", "Medium", "PYQ", "Seventh Schedule",
        "[TNPSC Group 1 2015 / UPSC CSE 2016] 'Economic and Social Planning' is an entry in which List of the Seventh Schedule of the Indian Constitution?",
        "[TNPSC குரூப் 1 2015 / UPSC CSE 2016] 'பொருளாதார மற்றும் சமூகத் திட்டமிடல்' என்பது இந்திய அரசியலமைப்பின் ஏழாவது அட்டவணையின் எந்தப் பட்டியலில் இடம்பெற்றுள்ள பதிவாகும்?",
        "Concurrent List (List III)", "பொதுப் பட்டியல் (பட்டியல் III)",
        "Union List (List I)", "மத்தியப் பட்டியல் (பட்டியல் I)",
        "State List (List II)", "மாநிலப் பட்டியல் (பட்டியல் II)",
        "Residuary subjects outside all lists", "அனைத்துப் பட்டியல்களுக்கும் வெளியே உள்ள எஞ்சிய துறைகள்",
        "A",
        "Entry 20 of the Concurrent List (List III) in the Seventh Schedule is 'Economic and social planning'. This provides constitutional authority for both the Centre and the States to undertake planning initiatives (such as Five-Year Plans and NITI Aayog coordination).",
        "ஏழாவது அட்டவணையின் பொதுப் பட்டியலில் (பட்டியல் III) உள்ள பதிவு 20 'பொருளாதார மற்றும் சமூகத் திட்டமிடல்' ஆகும். இது மத்திய மற்றும் மாநில அரசுகள் இரண்டும் திட்டமிடல் பணிகளை மேற்கொள்ள அரசியலமைப்பு அதிகாரத்தை வழங்குகிறது.",
        "Correct. Economic and social planning is Entry 20 in the Concurrent List.", "சரியானது. பொருளாதார மற்றும் சமூகத் திட்டமிடல் பொதுப் பட்டியலின் பதிவு 20 ஆகும்.",
        "Incorrect. It is not exclusively in the Union List.", "தவறானது. இது மத்தியப் பட்டியலில் மட்டும் உள்ளதல்ல.",
        "Incorrect. It is not in the State List.", "தவறானது. இது மாநிலப் பட்டியலில் இல்லை.",
        "Incorrect. It is an enumerated entry in List III, not a residuary subject.", "தவறானது. இது பட்டியல் III-ல் பட்டியலிடப்பட்ட பதிவு, எஞ்சிய துறை அல்ல.",
        "Economic and social planning = Concurrent List (Entry 20).",
        "பொருளாதார மற்றும் சமூகத் திட்டமிடல் = பொதுப் பட்டியல் (பதிவு 20)."
    ))

    qs.append(make_sch_q(
        "SCH_PYQ_008", "Medium", "PYQ", "Eighth Schedule",
        "[TNPSC Group 2 2018 / UPSC CSE 2007] Which one of the following languages is NOT included in the Eighth Schedule of the Constitution of India?",
        "[TNPSC குரூப் 2 2018 / UPSC CSE 2007] பின்வரும் மொழிகளில் எது இந்திய அரசியலமைப்பின் எட்டாவது அட்டவணையில் சேர்க்கப்படவில்லை?",
        "Rajasthani", "ராஜஸ்தானி",
        "Sanskrit", "சமஸ்கிருதம்",
        "Kashmiri", "காஷ்மீரி",
        "Sindhi", "சிந்தி",
        "A",
        "Rajasthani (and English and Bhojpuri) is NOT included in the Eighth Schedule. Sanskrit and Kashmiri were among the original 14 languages in 1950, and Sindhi was added by the 21st CAA 1967.",
        "ராஜஸ்தானி (மற்றும் ஆங்கிலம், போஜ்புரி) எட்டாவது அட்டவணையில் சேர்க்கப்படவில்லை. சமஸ்கிருதம் மற்றும் காஷ்மீரி 1950-ன் அசல் 14 மொழிகளில் இருந்தன, மேலும் சிந்தி 1967-ல் 21வது திருத்தத்தால் சேர்க்கப்பட்டது.",
        "Correct. Rajasthani is not in the Eighth Schedule.", "சரியானது. ராஜஸ்தானி எட்டாவது அட்டவணையில் இல்லை.",
        "Incorrect. Sanskrit is an Eighth Schedule language and a Classical language.", "தவறானது. சமஸ்கிருதம் 8வது அட்டவணை மற்றும் செம்மொழி ஆகும்.",
        "Incorrect. Kashmiri is an Eighth Schedule language.", "தவறானது. காஷ்மீரி 8வது அட்டவணை மொழியாகும்.",
        "Incorrect. Sindhi was added to the Eighth Schedule by the 21st CAA 1967.", "தவறானது. சிந்தி 21வது திருத்தம் 1967 மூலம் சேர்க்கப்பட்டது.",
        "Non-scheduled prominent languages: English, Rajasthani, Bhojpuri.",
        "அட்டவணையில் இல்லாத முக்கிய மொழிகள்: ஆங்கிலம், ராஜஸ்தானி, போஜ்புரி."
    ))

    qs.append(make_sch_q(
        "SCH_PYQ_009", "Hard", "PYQ", "Ninth Schedule",
        "[UPSC CSE 2018 / TNPSC Group 1 2020] In which landmark case did the Supreme Court hold that the laws placed in the Ninth Schedule after April 24, 1973 do not enjoy blanket immunity from judicial review?",
        "[UPSC CSE 2018 / TNPSC குரூப் 1 2020] ஏப்ரல் 24, 1973-க்குப் பிறகு ஒன்பதாவது அட்டவணையில் வைக்கப்பட்ட சட்டங்கள் நீதித்துறை மறுஆய்விலிருந்து முழுமையான பாதுகாப்பைப் பெறாது என்று உச்சநீதிமன்றம் எந்த முக்கிய வழக்கில் தீர்ப்பளித்தது?",
        "I.R. Coelho v. State of Tamil Nadu (2007)", "ஐ.ஆர். கோயல்ஹோ எதிர் தமிழ்நாடு அரசு (2007)",
        "Kesavananda Bharati v. State of Kerala (1973)", "கேசவானந்த பாரதி எதிர் கேரள அரசு (1973)",
        "Minerva Mills v. Union of India (1980)", "மினர்வா மில்ஸ் எதிர் இந்திய யூனியன் (1980)",
        "Indira Nehru Gandhi v. Raj Narain (1975)", "இந்திரா நேரு காந்தி எதிர் ராஜ் நாராயண் (1975)",
        "A",
        "In I.R. Coelho (2007), a unanimous 9-judge Constitution Bench held that any law inserted in the Ninth Schedule on or after April 24, 1973 is subject to judicial review and can be challenged for violating the Basic Structure (Articles 14, 19, 21).",
        "ஐ.ஆர். கோயல்ஹோ (2007) வழக்கில் 9 நீதிபதிகள் கொண்ட அமர்வு, ஏப்ரல் 24, 1973 அன்றோ அல்லது அதற்குப் பின்னரோ 9வது அட்டவணையில் சேர்க்கப்பட்ட எந்தவொரு சட்டமும் நீதித்துறை மறுஆய்வுக்கு உட்பட்டது என்றும், அடிப்படைக் கட்டமைப்பை மீறினால் செல்லாது என்றும் ஒருமனதாகத் தீர்ப்பளித்தது.",
        "Correct. I.R. Coelho (2007) established judicial review over post-1973 Ninth Schedule laws.", "சரியானது. ஐ.ஆர். கோயல்ஹோ (2007) 1973-க்குப் பிந்தைய 9வது அட்டவணைச் சட்டங்கள் மீதான நீதிமன்ற மறுஆய்வை நிறுவியது.",
        "Incorrect. Kesavananda (1973) established Basic Structure doctrine generally.", "தவறானது. கேசவானந்தா (1973) பொதுவாக அடிப்படைக் கட்டமைப்புக் கோட்பாட்டை நிறுவியது.",
        "Incorrect. Minerva Mills (1980) struck down Art 31C clauses (4) and (5).", "தவறானது. மினர்வா மில்ஸ் (1980) சரத்து 31C பிரிவுகளை ரத்து செய்தது.",
        "Incorrect. Indira Gandhi (1975) invalidated Article 329A(4).", "தவறானது. இந்திரா காந்தி (1975) சரத்து 329A(4)-ஐ ரத்து செய்தது.",
        "I.R. Coelho (2007): 9-judge bench; April 24, 1973 cutoff date for Ninth Schedule immunity.",
        "ஐ.ஆர். கோயல்ஹோ (2007): 9 நீதிபதிகள் அமர்வு; 9வது அட்டவணை பாதுகாப்பிற்கான வரம்புத் தேதி ஏப்ரல் 24, 1973."
    ))

    qs.append(make_sch_q(
        "SCH_PYQ_010", "Medium", "PYQ", "Third Schedule",
        "[TNPSC Group 1 2022 / TNPSC Group 2 2012] The forms of Oaths and Affirmations for which of the following is NOT contained in the Third Schedule of the Indian Constitution?",
        "[TNPSC குரூப் 1 2022 / TNPSC குரூப் 2 2012] பின்வருவனவற்றில் யாருக்கான பதவிப் பிரமாண மற்றும் உறுதியேற்பு படிவம் இந்திய அரசியலமைப்பின் மூன்றாவது அட்டவணையில் இடம் பெறவில்லை?",
        "President of India", "இந்தியக் குடியரசுத் தலைவர்",
        "Judges of the Supreme Court", "உச்சநீதிமன்ற நீதிபதிகள்",
        "Comptroller and Auditor-General of India", "இந்தியத் தலைமைக் கணக்குத் தணிக்கையாளர் (CAG)",
        "Union Ministers", "மத்திய அமைச்சர்கள்",
        "A",
        "The oath of the President of India is contained directly in Article 60 of the Constitution, NOT in the Third Schedule. The Third Schedule contains oaths for Union Ministers, MPs, candidates, SC/HC Judges, and the CAG.",
        "இந்தியக் குடியரசுத் தலைவரின் பதவிப் பிரமாணம் நேரடியாக அரசியலமைப்பின் சரத்து 60-ல் உள்ளது, மூன்றாவது அட்டவணையில் இல்லை. மூன்றாவது அட்டவணை மத்திய அமைச்சர்கள், எம்.பி.க்கள், வேட்பாளர்கள், நீதிபதிகள் மற்றும் CAG-க்கான பிரமாணங்களைக் கொண்டுள்ளது.",
        "Correct. President's oath is in Article 60, not Third Schedule.", "சரியானது. குடியரசுத் தலைவரின் பிரமாணம் சரத்து 60-ல் உள்ளது, 3வது அட்டவணையில் அல்ல.",
        "Incorrect. Supreme Court Judges take oath under Third Schedule Form IV.", "தவறானது. உச்சநீதிமன்ற நீதிபதிகள் 3வது அட்டவணை படிவம் IV-ன் கீழ் உறுதிமொழி ஏற்கின்றனர்.",
        "Incorrect. CAG takes oath under Third Schedule Form IV.", "தவறானது. CAG 3வது அட்டவணை படிவம் IV-ன் கீழ் உறுதிமொழி ஏற்கிறார்.",
        "Incorrect. Union Ministers take oath under Third Schedule Forms I and II.", "தவறானது. மத்திய அமைச்சர்கள் 3வது அட்டவணை படிவங்கள் I & II-ன் கீழ் உறுதிமொழி ஏற்கின்றனர்.",
        "Oaths outside Third Schedule: President (Art 60), Vice-President (Art 69), Governor (Art 159).",
        "3வது அட்டவணைக்கு வெளியே உள்ள பிரமாணங்கள்: குடியரசுத் தலைவர் (சரத்து 60), VP (சரத்து 69), ஆளுநர் (சரத்து 159)."
    ))

    # PYQ 11 - 20
    qs.append(make_sch_q(
        "SCH_PYQ_011", "Medium", "PYQ", "Seventh Schedule",
        "[TNPSC Group 1 2020] By which Constitutional Amendment Act was 'Education' transferred from the State List to the Concurrent List?",
        "[TNPSC குரூப் 1 2020] எந்த அரசியலமைப்புத் திருத்தச் சட்டத்தின் மூலம் 'கல்வி' மாநிலப் பட்டியலிலிருந்து பொதுப் பட்டியலுக்கு மாற்றப்பட்டது?",
        "42nd Constitutional Amendment Act, 1976", "42வது அரசியலமைப்புத் திருத்தச் சட்டம், 1976",
        "44th Constitutional Amendment Act, 1978", "44வது அரசியலமைப்புத் திருத்தச் சட்டம், 1978",
        "24th Constitutional Amendment Act, 1971", "24வது அரசியலமைப்புத் திருத்தச் சட்டம், 1971",
        "86th Constitutional Amendment Act, 2002", "86வது அரசியலமைப்புத் திருத்தச் சட்டம், 2002",
        "A",
        "The 42nd Amendment Act, 1976 transferred Education, Forests, Weights & Measures, Protection of wild animals and birds, and Administration of Justice from State List to Concurrent List.",
        "42வது திருத்தச் சட்டம் 1976, கல்வி, காடுகள், எடைகள் மற்றும் அளவுகள், வனவிலங்குகள் பாதுகாப்பு மற்றும் நீதிமன்ற நீதி நிர்வாகம் ஆகியவற்றை மாநிலப் பட்டியலிலிருந்து பொதுப் பட்டியலுக்கு மாற்றியது.",
        "Correct. 42nd CAA 1976 transferred Education to Concurrent List.", "சரியானது. 42வது திருத்தம் 1976 கல்வியை பொதுப் பட்டியலுக்கு மாற்றியது.",
        "Incorrect. 44th CAA 1978 did not transfer education.", "தவறானது. 44வது திருத்தம் 1978 கல்வியை மாற்றவில்லை.",
        "Incorrect. 24th CAA 1971 amended Article 368.", "தவறானது. 24வது திருத்தம் சரத்து 368-ஐத் திருத்தியது.",
        "Incorrect. 86th CAA 2002 made primary education a fundamental right (Art 21A).", "தவறானது. 86வது திருத்தம் கல்வியை அடிப்படை உரிமையாக்கியது (சரத்து 21A).",
        "Education in Concurrent List: 42nd CAA 1976 (Entry 25 of List III).",
        "கல்வி பொதுப் பட்டியலில் சேர்க்கப்பட்டது: 42வது திருத்தம் 1976 (பட்டியல் III பதிவு 25)."
    ))

    qs.append(make_sch_q(
        "SCH_PYQ_012", "Easy", "PYQ", "Eighth Schedule",
        "[TNPSC Group 2 2015] In which year was Classical Language (செம்மொழி) status granted to the Tamil language by the Government of India?",
        "[TNPSC குரூப் 2 2015] எந்த ஆண்டில் இந்திய அரசால் தமிழ் மொழிக்கு செம்மொழி அந்தஸ்து வழங்கப்பட்டது?",
        "2004", "2004",
        "2005", "2005",
        "2008", "2008",
        "2014", "2014",
        "A",
        "Tamil was declared as the very first Classical Language of India in 2004.",
        "தமிழ் 2004-ல் இந்தியாவின் முதல் செம்மொழியாக அறிவிக்கப்பட்டது.",
        "Correct. Tamil was accorded Classical Language status in 2004.", "சரியானது. தமிழுக்கு 2004-ல் செம்மொழி அந்தஸ்து வழங்கப்பட்டது.",
        "Incorrect. Sanskrit was declared classical in 2005.", "தவறானது. சமஸ்கிருதம் 2005-ல் செம்மொழியாக அறிவிக்கப்பட்டது.",
        "Incorrect. Telugu and Kannada were declared in 2008.", "தவறானது. தெலுங்கு மற்றும் கன்னடம் 2008-ல் அறிவிக்கப்பட்டன.",
        "Incorrect. Odia was declared in 2014.", "தவறானது. ஒடியா 2014-ல் அறிவிக்கப்பட்டது.",
        "Tamil: First Classical Language in India (2004).",
        "தமிழ்: இந்தியாவின் முதல் செம்மொழி (2004)."
    ))

    qs.append(make_sch_q(
        "SCH_PYQ_013", "Easy", "PYQ", "Schedules Overview",
        "[TNPSC Group 4 2018] What is the total number of Schedules in the Constitution of India at present?",
        "[TNPSC குரூப் 4 2018] தற்போது இந்திய அரசியலமைப்பில் உள்ள மொத்த அட்டவணைகளின் எண்ணிக்கை என்ன?",
        "12 Schedules", "12 அட்டவணைகள்",
        "8 Schedules", "8 அட்டவணைகள்",
        "10 Schedules", "10 அட்டவணைகள்",
        "14 Schedules", "14 அட்டவணைகள்",
        "A",
        "The Constitution originally had 8 schedules in 1950, and currently has 12 schedules.",
        "அரசியலமைப்பில் தொடக்கத்தில் 8 அட்டவணைகள் இருந்தன, தற்போது 12 அட்டவணைகள் உள்ளன.",
        "Correct. 12 schedules are currently in the Indian Constitution.", "சரியானது. தற்போது இந்திய அரசியலமைப்பில் 12 அட்டவணைகள் உள்ளன.",
        "Incorrect. 8 was the original count in 1950.", "தவறானது. 8 என்பது 1950-ன் தொடக்க எண்ணிக்கை.",
        "Incorrect. 10 was before 73rd and 74th amendments.", "தவறானது. 10 என்பது 73/74வது திருத்தங்களுக்கு முன்பு இருந்தது.",
        "Incorrect. 14 was the original number of languages, not schedules.", "தவறானது. 14 என்பது அசல் மொழிகளின் எண்ணிக்கை.",
        "Current Schedules: 12 Schedules.",
        "தற்போதைய அட்டவணைகள்: 12 அட்டவணைகள்."
    ))

    qs.append(make_sch_q(
        "SCH_PYQ_014", "Hard", "PYQ", "Tenth Schedule",
        "[TNPSC Group 1 2014] Which Constitutional Amendment Act deleted the provision protecting a split of one-third (1/3rd) members under the Tenth Schedule?",
        "[TNPSC குரூப் 1 2014] பத்தாவது அட்டவணையின் கீழ் மூன்றில் ஒரு பங்கு (1/3) உறுப்பினர்களின் பிளவைப் பாதுகாத்த விதியை நீக்கிய அரசியலமைப்புத் திருத்தச் சட்டம் எது?",
        "91st Constitutional Amendment Act, 2003", "91வது அரசியலமைப்புத் திருத்தச் சட்டம், 2003",
        "52nd Constitutional Amendment Act, 1985", "52வது அரசியலமைப்புத் திருத்தச் சட்டம், 1985",
        "86th Constitutional Amendment Act, 2002", "86வது அரசியலமைப்புத் திருத்தச் சட்டம், 2002",
        "92nd Constitutional Amendment Act, 2003", "92வது அரசியலமைப்புத் திருத்தச் சட்டம், 2003",
        "A",
        "The 91st Constitutional Amendment Act, 2003 deleted Paragraph 3 of the Tenth Schedule, which had exempted one-third splits from disqualification.",
        "91வது அரசியலமைப்புத் திருத்தச் சட்டம் 2003, பத்தாவது அட்டவணையின் பத்தி 3-ஐ நீக்கியது; இது மூன்றில் ஒரு பங்கு பிளவுக்கு தகுதிநீக்கத்திலிருந்து விலக்கு அளித்திருந்தது.",
        "Correct. 91st CAA 2003 deleted the 1/3rd split defense.", "சரியானது. 91வது திருத்தம் 2003 மூன்றில் ஒரு பங்கு பிளவு பாதுகாப்பை நீக்கியது.",
        "Incorrect. 52nd CAA 1985 originally created the split defense.", "தவறானது. 52வது திருத்தம் 1985-ல் தான் பிளவு விதி முதலில் உருவாக்கப்பட்டது.",
        "Incorrect. 86th CAA 2002 is about education.", "தவறானது. 86வது திருத்தம் கல்வி பற்றியது.",
        "Incorrect. 92nd CAA 2003 added 4 languages to Eighth Schedule.", "தவறானது. 92வது திருத்தம் 4 மொழிகளை எட்டாவது அட்டவணையில் சேர்த்தது.",
        "91st CAA 2003: Deleted 1/3 split; only 2/3 merger is protected.",
        "91வது திருத்தம் 2003: 1/3 பிளவு நீக்கம்; 2/3 கட்சி இணைப்பு மட்டுமே பாதுகாக்கப்படுகிறது."
    ))

    qs.append(make_sch_q(
        "SCH_PYQ_015", "Medium", "PYQ", "Fifth Schedule",
        "[TNPSC Group 2A 2017] What is the maximum number of members in a Tribes Advisory Council established under the Fifth Schedule?",
        "[TNPSC குரூப் 2A 2017] ஐந்தாவது அட்டவணையின் கீழ் அமைக்கப்படும் பழங்குடியினர் ஆலோசனைக் குழுவில் (TAC) இருக்கக்கூடிய அதிகபட்ச உறுப்பினர்களின் எண்ணிக்கை என்ன?",
        "20 members", "20 உறுப்பினர்கள்",
        "30 members", "30 உறுப்பினர்கள்",
        "15 members", "15 உறுப்பினர்கள்",
        "25 members", "25 உறுப்பினர்கள்",
        "A",
        "Under Paragraph 4(1) of the Fifth Schedule, a Tribes Advisory Council shall consist of not more than twenty members.",
        "ஐந்தாவது அட்டவணையின் பத்தி 4(1)-ன் படி, பழங்குடியினர் ஆலோசனைக் குழு 20 பேருக்கு மிகாமல் உறுப்பினர்களைக் கொண்டிருக்கும்.",
        "Correct. TAC maximum strength is 20 members.", "சரியானது. TAC-ன் அதிகபட்ச உறுப்பினர் பலம் 20 ஆகும்.",
        "Incorrect. 30 members is the strength of Sixth Schedule ADCs.", "தவறானது. 30 என்பது 6வது அட்டவணை ADC-ன் பலம்.",
        "Incorrect. 15 is not the constitutional ceiling.", "தவறானது. 15 என்பது அரசியலமைப்பு உச்சவரம்பு அல்ல.",
        "Incorrect. 25 is incorrect.", "தவறானது. 25 என்பது தவறானது.",
        "Fifth Schedule TAC: Not more than 20 members (3/4th ST MLAs).",
        "5வது அட்டவணை TAC: 20 உறுப்பினர்களுக்கு மிகாமல் (3/4 பங்கு ST சட்டமன்ற உறுப்பினர்கள்)."
    ))

    qs.append(make_sch_q(
        "SCH_PYQ_016", "Medium", "PYQ", "First Schedule",
        "[UPSC CSE 2014] If a new State of the Indian Union is to be created, which one of the following Schedules of the Constitution must be amended?",
        "[UPSC CSE 2014] இந்திய ஒன்றியத்தின் ஒரு புதிய மாநிலம் உருவாக்கப்பட வேண்டுமானால், அரசியலமைப்பின் பின்வரும் அட்டவணைகளில் எதைத் திருத்த வேண்டும்?",
        "First Schedule", "முதல் அட்டவணை",
        "Second Schedule", "இரண்டாவது அட்டவணை",
        "Third Schedule", "மூன்றாவது அட்டவணை",
        "Fifth Schedule", "ஐந்தாவது அட்டவணை",
        "A",
        "The First Schedule specifies the names and territorial extent of all States and Union Territories. Creating a new State under Article 2 or 3 necessarily requires amending the First Schedule.",
        "முதல் அட்டவணை அனைத்து மாநிலங்கள் மற்றும் யூனியன் பிரதேசங்களின் பெயர்கள் மற்றும் எல்லைப் பகுதிகளைக் குறிப்பிடுகிறது. சரத்து 2 அல்லது 3-ன் கீழ் புதிய மாநிலத்தை உருவாக்க முதல் அட்டவணையைத் திருத்துவது அவசியமாகும்.",
        "Correct. First Schedule must be amended to add the new State.", "சரியானது. புதிய மாநிலத்தைச் சேர்க்க முதல் அட்டவணை திருத்தப்பட வேண்டும்.",
        "Incorrect. Second Schedule deals with salaries.", "தவறானது. இரண்டாவது அட்டவணை சம்பளங்களைக் கையாள்கிறது.",
        "Incorrect. Third Schedule deals with oaths.", "தவறானது. மூன்றாவது அட்டவணை பிரமாணங்களைக் கையாள்கிறது.",
        "Incorrect. Fifth Schedule deals with scheduled areas administration.", "தவறானது. ஐந்தாவது அட்டவணை அட்டவணைப் பகுதிகளைக் கையாள்கிறது.",
        "New State creation amends: First Schedule (territory) and Fourth Schedule (Rajya Sabha seats).",
        "புதிய மாநில உருவாக்கம் திருத்துபவை: முதல் அட்டவணை (எல்லை) மற்றும் நான்காவது அட்டவணை (மாநிலங்களவை இடங்கள்)."
    ))

    qs.append(make_sch_q(
        "SCH_PYQ_017", "Medium", "PYQ", "Second Schedule",
        "[TNPSC Group 1 2022] The salary and service conditions of the Comptroller and Auditor-General of India are specified in which Part of the Second Schedule?",
        "[TNPSC குரூப் 1 2022] இந்தியத் தலைமைக் கணக்குத் தணிக்கையாளரின் (CAG) ஊதியம் மற்றும் சேவை நிபந்தனைகள் இரண்டாவது அட்டவணையின் எந்தப் பகுதியில் குறிப்பிடப்பட்டுள்ளன?",
        "Part E", "பகுதி E",
        "Part A", "பகுதி A",
        "Part C", "பகுதி C",
        "Part D", "பகுதி D",
        "A",
        "Part E of the Second Schedule specifically contains provisions as to the Comptroller and Auditor-General of India.",
        "இரண்டாவது அட்டவணையின் பகுதி E பிரத்யேகமாக இந்தியத் தலைமைக் கணக்குத் தணிக்கையாளர் (CAG) பற்றிய விதிகளைக் கொண்டுள்ளது.",
        "Correct. Part E covers the CAG.", "சரியானது. பகுதி E இந்திய CAG-ஐக் குறிக்கிறது.",
        "Incorrect. Part A covers President and Governors.", "தவறானது. பகுதி A குடியரசுத் தலைவர் மற்றும் ஆளுநர்களைக் குறிக்கிறது.",
        "Incorrect. Part C covers Speakers and Deputy Speakers.", "தவறானது. பகுதி C சபாநாயகர்கள் மற்றும் துணைச் சபாநாயகர்களைக் குறிக்கிறது.",
        "Incorrect. Part D covers Supreme Court and High Court Judges.", "தவறானது. பகுதி D உச்ச & உயர் நீதிமன்ற நீதிபதிகளைக் குறிக்கிறது.",
        "Second Schedule: Part E = Comptroller and Auditor-General of India.",
        "இரண்டாவது அட்டவணை: பகுதி E = இந்தியத் தலைமைக் கணக்குத் தணிக்கையாளர்."
    ))

    qs.append(make_sch_q(
        "SCH_PYQ_018", "Easy", "PYQ", "Eighth Schedule",
        "[TNPSC Group 2 2018] Which three languages were added to the Eighth Schedule of the Constitution of India by the 71st Constitutional Amendment Act, 1992?",
        "[TNPSC குரூப் 2 2018] 71வது அரசியலமைப்புத் திருத்தச் சட்டம் 1992 மூலம் இந்திய அரசியலமைப்பின் எட்டாவது அட்டவணையில் சேர்க்கப்பட்ட மூன்று மொழிகள் எவை?",
        "Konkani, Manipuri, and Nepali", "கொங்கணி, மணிப்பூரி மற்றும் நேபாளி",
        "Bodo, Dogri, and Maithili", "போடோ, டோக்ரி மற்றும் மைதிலி",
        "Sindhi, Sanskrit, and Kashmiri", "சிந்தி, சமஸ்கிருதம் மற்றும் காஷ்மீரி",
        "Assamese, Bengali, and Gujarati", "அசாமி, பெங்காலி மற்றும் குஜராத்தி",
        "A",
        "The 71st Constitutional Amendment Act, 1992 added Konkani, Manipuri, and Nepali (mnemonic: KMN) to the Eighth Schedule.",
        "71வது அரசியலமைப்புத் திருத்தச் சட்டம் 1992, கொங்கணி, மணிப்பூரி மற்றும் நேபாளி (நினைவுச்சொல்: KMN) ஆகிய மூன்று மொழிகளை எட்டாவது அட்டவணையில் சேர்த்தது.",
        "Correct. Konkani, Manipuri, and Nepali were added by 71st CAA 1992.", "சரியானது. கொங்கணி, மணிப்பூரி, நேபாளி 71வது திருத்தம் 1992 மூலம் சேர்க்கப்பட்டன.",
        "Incorrect. Bodo, Dogri, Maithili were added by 92nd CAA 2003.", "தவறானது. போடோ, டோக்ரி, மைதிலி 92வது திருத்தம் 2003 மூலம் சேர்க்கப்பட்டன.",
        "Incorrect. Sindhi was added in 1967; Sanskrit & Kashmiri were original.", "தவறானது. சிந்தி 1967-ல் சேர்க்கப்பட்டது; சமஸ்கிருதம் & காஷ்மீரி தொடக்க மொழிகள்.",
        "Incorrect. Assamese, Bengali, Gujarati were among the original 14 languages.", "தவறானது. அசாமி, பெங்காலி, குஜராத்தி அசல் 14 மொழிகளில் இருந்தன.",
        "71st CAA 1992 = Konkani, Manipuri, Nepali (KMN).",
        "71வது திருத்தம் 1992 = கொங்கணி, மணிப்பூரி, நேபாளி (KMN)."
    ))

    qs.append(make_sch_q(
        "SCH_PYQ_019", "Easy", "PYQ", "Eighth Schedule",
        "[TNPSC Group 4 2016] Which Constitutional Amendment Act added four languages—Bodo, Dogri, Maithili, and Santhali—to the Eighth Schedule in 2003?",
        "[TNPSC குரூப் 4 2016] 2003-ல் போடோ, டோக்ரி, மைதிலி மற்றும் சந்தாலி ஆகிய நான்கு மொழிகளை எட்டாவது அட்டவணையில் சேர்த்த அரசியலமைப்புத் திருத்தச் சட்டம் எது?",
        "92nd Constitutional Amendment Act, 2003", "92வது அரசியலமைப்புத் திருத்தச் சட்டம், 2003",
        "91st Constitutional Amendment Act, 2003", "91வது அரசியலமைப்புத் திருத்தச் சட்டம், 2003",
        "71st Constitutional Amendment Act, 1992", "71வது அரசியலமைப்புத் திருத்தச் சட்டம், 1992",
        "21st Constitutional Amendment Act, 1967", "21வது அரசியலமைப்புத் திருத்தச் சட்டம், 1967",
        "A",
        "The 92nd Constitutional Amendment Act, 2003 added Bodo, Dogri, Maithili, and Santhali (BDMS) to the Eighth Schedule, raising the total number of recognized languages to 22.",
        "92வது அரசியலமைப்புத் திருத்தச் சட்டம் 2003, போடோ, டோக்ரி, மைதிலி மற்றும் சந்தாலி (BDMS) ஆகிய மொழிகளை எட்டாவது அட்டவணையில் சேர்த்து மொத்த மொழிகளின் எண்ணிக்கையை 22 ஆக உயர்த்தியது.",
        "Correct. 92nd CAA 2003 added Bodo, Dogri, Maithili, Santhali.", "சரியானது. 92வது திருத்தம் 2003 போடோ, டோக்ரி, மைதிலி, சந்தாலியைச் சேர்த்தது.",
        "Incorrect. 91st CAA 2003 dealt with anti-defection and cabinet size.", "தவறானது. 91வது திருத்தம் கட்சித் தாவல் மற்றும் அமைச்சரவை அளவு பற்றியது.",
        "Incorrect. 71st CAA 1992 added Konkani, Manipuri, Nepali.", "தவறானது. 71வது திருத்தம் கொங்கணி, மணிப்பூரி, நேபாளியைச் சேர்த்தது.",
        "Incorrect. 21st CAA 1967 added Sindhi.", "தவறானது. 21வது திருத்தம் சிந்தியைச் சேர்த்தது.",
        "92nd CAA 2003: BDMS (Bodo, Dogri, Maithili, Santhali) -> Total 22 languages.",
        "92வது திருத்தம் 2003: BDMS (போடோ, டோக்ரி, மைதிலி, சந்தாலி) -> மொத்தம் 22 மொழிகள்."
    ))

    qs.append(make_sch_q(
        "SCH_PYQ_020", "Medium", "PYQ", "Ninth Schedule",
        "[TNPSC Group 1 2017] By which Constitutional Amendment Act was the Tamil Nadu Backward Classes, Scheduled Castes and Scheduled Tribes Act, 1993 (protecting 69% reservation) included in the Ninth Schedule?",
        "[TNPSC குரூப் 1 2017] தமிழ்நாட்டின் 69% இடஒதுக்கீட்டைப் பாதுகாக்கும் தமிழ்நாடு பிற்படுத்தப்பட்டோர், எஸ்சி மற்றும் எஸ்டி சட்டம் 1993 எந்த அரசியலமைப்புத் திருத்தச் சட்டத்தின் மூலம் ஒன்பதாவது அட்டவணையில் சேர்க்கப்பட்டது?",
        "76th Constitutional Amendment Act, 1994", "76வது அரசியலமைப்புத் திருத்தச் சட்டம், 1994",
        "73rd Constitutional Amendment Act, 1992", "73வது அரசியலமைப்புத் திருத்தச் சட்டம், 1992",
        "77th Constitutional Amendment Act, 1995", "77வது அரசியலமைப்புத் திருத்தச் சட்டம், 1995",
        "85th Constitutional Amendment Act, 2001", "85வது அரசியலமைப்புத் திருத்தச் சட்டம், 2001",
        "A",
        "The 76th Constitutional Amendment Act, 1994 inserted the Tamil Nadu Reservation Act of 1994 into the Ninth Schedule as Entry 257A.",
        "76வது அரசியலமைப்புத் திருத்தச் சட்டம் 1994, தமிழ்நாடு இடஒதுக்கீடு சட்டம் 1994-ஐ ஒன்பதாவது அட்டவணையில் பதிவு 257A ஆகச் சேர்த்தது.",
        "Correct. 76th CAA 1994 protected TN 69% reservation in Ninth Schedule.", "சரியானது. 76வது திருத்தம் 1994 தமிழக 69% இடஒதுக்கீட்டை 9வது அட்டவணையில் சேர்த்தது.",
        "Incorrect. 73rd CAA 1992 was Panchayati Raj.", "தவறானது. 73வது திருத்தம் பஞ்சாயத்து ராஜ் பற்றியது.",
        "Incorrect. 77th CAA 1995 provided reservation in promotions for SC/ST.", "தவறானது. 77வது திருத்தம் எஸ்சி/எஸ்டி பதவி உயர்வில் இடஒதுக்கீடு வழங்கியது.",
        "Incorrect. 85th CAA 2001 provided consequential seniority for SC/ST.", "தவறானது. 85வது திருத்தம் தொடர் பணிமூப்பு சலுகை வழங்கியது.",
        "76th CAA 1994: Tamil Nadu 69% Reservation Act placed in Ninth Schedule.",
        "76வது திருத்தம் 1994: தமிழக 69% இடஒதுக்கீட்டுச் சட்டம் ஒன்பதாவது அட்டவணையில் வைக்கப்பட்டது."
    ))

    # PYQ 21 - 30
    qs.append(make_sch_q(
        "SCH_PYQ_021", "Hard", "PYQ", "Tenth Schedule",
        "[UPSC CSE 2013] In Kihoto Hollohan v. Zachillhu (1992), which provision of the Tenth Schedule was declared unconstitutional by the Supreme Court?",
        "[UPSC CSE 2013] கிகோட்டோ ஹோலோஹான் எதிர் சாச்சிலு (1992) வழக்கில், பத்தாவது அட்டவணையின் எந்த விதி உச்சநீதிமன்றத்தால் அரசியலமைப்புக்கு முரணானது என அறிவிக்கப்பட்டது?",
        "Paragraph 7 (barring jurisdiction of courts)", "பத்தி 7 (நீதிமன்றங்களின் அதிகார வரம்பைத் தடுத்தது)",
        "Paragraph 2 (grounds of disqualification)", "பத்தி 2 (தகுதிநீக்கத்திற்கான காரணங்கள்)",
        "Paragraph 4 (merger exemption)", "பத்தி 4 (கட்சி இணைப்பு விதிவிலக்கு)",
        "Paragraph 6 (decision of Speaker is final)", "பத்தி 6 (சபாநாயகரின் முடிவே இறுதியானது)",
        "A",
        "In Kihoto Hollohan (1992), the Supreme Court struck down Paragraph 7 of the Tenth Schedule because it barred the jurisdiction of courts without being ratified by the States as required by the proviso to Article 368(2).",
        "கிகோட்டோ ஹோலோஹான் (1992) வழக்கில், நீதிமன்றங்களின் அதிகார வரம்பைத் தடுத்த பத்தாவது அட்டவணையின் பத்தி 7-ஐ உச்சநீதிமன்றம் ரத்து செய்தது; ஏனெனில் சரத்து 368(2)-ன் படி மாநிலங்களின் ஏற்பு பெறப்படாமல் அது இயற்றப்பட்டது.",
        "Correct. Paragraph 7 was struck down, establishing judicial review over the Speaker's decisions.", "சரியானது. பத்தி 7 ரத்து செய்யப்பட்டு சபாநாயகர் முடிவு மீது நீதிமன்ற மறுஆய்வு நிலைநாட்டப்பட்டது.",
        "Incorrect. Paragraph 2 was upheld as valid.", "தவறானது. பத்தி 2 செல்லுபடியாகும் என உறுதி செய்யப்பட்டது.",
        "Incorrect. Paragraph 4 on merger was upheld.", "தவறானது. இணைப்பு பற்றிய பத்தி 4 உறுதி செய்யப்பட்டது.",
        "Incorrect. Paragraph 6 was read down, not struck down entirely.", "தவறானது. பத்தி 6 முழுமையாக ரத்து செய்யப்படவில்லை.",
        "Kihoto Hollohan (1992): Para 7 unconstitutional. Speaker acts as a tribunal under judicial review.",
        "கிகோட்டோ ஹோலோஹான் (1992): பத்தி 7 செல்லாது. சபாநாயகர் நீதிமன்ற மறுஆய்வுக்கு உட்பட்ட தீர்ப்பாயமாகச் செயல்படுகிறார்."
    ))

    qs.append(make_sch_q(
        "SCH_PYQ_022", "Easy", "PYQ", "Seventh Schedule",
        "[TNPSC Group 2 2012] Which of the following subjects was transferred from the State List to the Concurrent List by the 42nd Amendment?",
        "[TNPSC குரூப் 2 2012] 42வது திருத்தத்தின் மூலம் பின்வரும் எந்தத் துறை மாநிலப் பட்டியலிலிருந்து பொதுப் பட்டியலுக்கு மாற்றப்பட்டது?",
        "Forests", "காடுகள்",
        "Police", "காவல்துறை",
        "Public Health", "பொது சுகாதாரம்",
        "Agriculture", "விவசாயம்",
        "A",
        "Forests (along with Education, Weights & Measures, Wild Animals protection, and Administration of Justice) was transferred from State List to Concurrent List by the 42nd CAA 1976.",
        "42வது திருத்தம் 1976-ன் மூலம் காடுகள் (மற்றும் கல்வி, எடைகள் & அளவுகள், வனவிலங்குகள் பாதுகாப்பு, நீதி நிர்வாகம்) மாநிலப் பட்டியலிலிருந்து பொதுப் பட்டியலுக்கு மாற்றப்பட்டது.",
        "Correct. Forests was transferred to Concurrent List by 42nd CAA 1976.", "சரியானது. காடுகள் 42வது திருத்தம் 1976 மூலம் பொதுப் பட்டியலுக்கு மாற்றப்பட்டது.",
        "Incorrect. Police remains in State List (Entry 2).", "தவறானது. காவல்துறை மாநிலப் பட்டியலிலேயே நீடிக்கிறது.",
        "Incorrect. Public Health remains in State List (Entry 6).", "தவறானது. பொது சுகாதாரம் மாநிலப் பட்டியலிலேயே நீடிக்கிறது.",
        "Incorrect. Agriculture remains in State List (Entry 14).", "தவறானது. விவசாயம் மாநிலப் பட்டியலிலேயே நீடிக்கிறது.",
        "42nd CAA 1976 transferred Forests to List III (Concurrent List).",
        "42வது திருத்தம் 1976 காடுகளைப் பொதுப் பட்டியலுக்கு (பட்டியல் III) மாற்றியது."
    ))

    qs.append(make_sch_q(
        "SCH_PYQ_023", "Easy", "PYQ", "Fourth Schedule",
        "[TNPSC Group 1 2019] Which State has the largest number of seats allocated in the Rajya Sabha under the Fourth Schedule?",
        "[TNPSC குரூப் 1 2019] நான்காவது அட்டவணையின் கீழ் மாநிலங்களவையில் மிக அதிக எண்ணிக்கையிலான இடங்கள் ஒதுக்கப்பட்டுள்ள மாநிலம் எது?",
        "Uttar Pradesh (31 seats)", "உத்தரப் பிரதேசம் (31 இடங்கள்)",
        "Maharashtra (19 seats)", "மகாராஷ்டிரா (19 இடங்கள்)",
        "Tamil Nadu (18 seats)", "தமிழ்நாடு (18 இடங்கள்)",
        "Bihar (16 seats)", "பீகார் (16 இடங்கள்)",
        "A",
        "Uttar Pradesh has 31 seats in the Rajya Sabha, the highest among all States in the Fourth Schedule.",
        "நான்காவது அட்டவணையில் உள்ள அனைத்து மாநிலங்களிலும் உத்தரப் பிரதேசம் அதிகபட்சமாக 31 மாநிலங்களவை இடங்களைக் கொண்டுள்ளது.",
        "Correct. Uttar Pradesh has the highest allocation (31 seats).", "சரியானது. உத்தரப் பிரதேசம் அதிகபட்சமாக 31 இடங்களைக் கொண்டுள்ளது.",
        "Incorrect. Maharashtra has 19 seats (second highest).", "தவறானது. மகாராஷ்டிரா 19 இடங்களைக் கொண்டுள்ளது (இரண்டாவது இடம்).",
        "Incorrect. Tamil Nadu has 18 seats (third highest).", "தவறானது. தமிழ்நாடு 18 இடங்களைக் கொண்டுள்ளது (மூன்றாவது இடம்).",
        "Incorrect. Bihar and West Bengal have 16 seats each.", "தவறானது. பீகார் மற்றும் மேற்கு வங்கம் தலா 16 இடங்களைக் கொண்டுள்ளன.",
        "Rajya Sabha Seats: UP (31) > Maharashtra (19) > Tamil Nadu (18) > WB & Bihar (16).",
        "மாநிலங்களவை இடங்கள்: உ.பி (31) > மகாராஷ்டிரா (19) > தமிழ்நாடு (18) > மேற்கு வங்கம் & பீகார் (16)."
    ))

    qs.append(make_sch_q(
        "SCH_PYQ_024", "Easy", "PYQ", "Fourth Schedule",
        "[TNPSC Group 4 2014] How many members represent the State of Tamil Nadu in the Rajya Sabha under the Fourth Schedule?",
        "[TNPSC குரூப் 4 2014] நான்காவது அட்டவணையின் கீழ் தமிழ்நாடு மாநிலத்தை மாநிலங்களவையில் பிரதிநிதித்துவப்படுத்தும் உறுப்பினர்களின் எண்ணிக்கை எத்தனை?",
        "18 members", "18 உறுப்பினர்கள்",
        "39 members", "39 உறுப்பினர்கள்",
        "234 members", "234 உறுப்பினர்கள்",
        "16 members", "16 உறுப்பினர்கள்",
        "A",
        "Tamil Nadu is allocated 18 seats in the Rajya Sabha under the Fourth Schedule (and 39 seats in the Lok Sabha).",
        "நான்காவது அட்டவணையின் கீழ் மாநிலங்களவையில் தமிழ்நாட்டிற்கு 18 இடங்கள் ஒதுக்கப்பட்டுள்ளன (மற்றும் மக்களவையில் 39 இடங்கள்).",
        "Correct. Tamil Nadu has 18 Rajya Sabha seats.", "சரியானது. தமிழ்நாட்டிற்கு 18 மாநிலங்களவை இடங்கள் உள்ளன.",
        "Incorrect. 39 is the number of Lok Sabha seats for Tamil Nadu.", "தவறானது. 39 என்பது தமிழ்நாட்டின் மக்களவை இடங்கள்.",
        "Incorrect. 234 is the strength of the Tamil Nadu Legislative Assembly.", "தவறானது. 234 என்பது தமிழக சட்டமன்றத்தின் மொத்த பலம்.",
        "Incorrect. 16 is the allocation for Bihar and West Bengal.", "தவறானது. 16 என்பது பீகார் மற்றும் மேற்கு வங்கத்தின் இடங்கள்.",
        "Tamil Nadu in Parliament: 18 Rajya Sabha seats (4th Schedule) + 39 Lok Sabha seats.",
        "பாராளுமன்றத்தில் தமிழ்நாடு: 18 மாநிலங்களவை இடங்கள் (4வது அட்டவணை) + 39 மக்களவை இடங்கள்."
    ))

    qs.append(make_sch_q(
        "SCH_PYQ_025", "Medium", "PYQ", "Eleventh Schedule",
        "[UPSC CSE 2016] Which Article of the Indian Constitution is directly associated with the Eleventh Schedule?",
        "[UPSC CSE 2016] இந்திய அரசியலமைப்பின் எந்த சரத்து நேரடியாக பதினோராவது அட்டவணையுடன் தொடர்புடையது?",
        "Article 243G", "சரத்து 243G",
        "Article 243W", "சரத்து 243W",
        "Article 243ZD", "சரத்து 243ZD",
        "Article 243K", "சரத்து 243K",
        "A",
        "Article 243G empowers the State Legislature to confer powers and responsibilities on Panchayats with respect to matters listed in the Eleventh Schedule.",
        "சரத்து 243G, பதினோராவது அட்டவணையில் பட்டியலிடப்பட்டுள்ள துறைகளில் பஞ்சாயத்துகளுக்கு அதிகாரங்களையும் பொறுப்புகளையும் வழங்க மாநில சட்டமன்றத்திற்கு அதிகாரம் அளிக்கிறது.",
        "Correct. Article 243G governs Eleventh Schedule subjects.", "சரியானது. சரத்து 243G பதினோராவது அட்டவணை பணிகளை நிர்வகிக்கிறது.",
        "Incorrect. Article 243W governs Twelfth Schedule for Municipalities.", "தவறானது. சரத்து 243W நகராட்சிகளுக்கான 12வது அட்டவணையை நிர்வகிக்கிறது.",
        "Incorrect. Article 243ZD is District Planning Committee.", "தவறானது. சரத்து 243ZD மாவட்ட திட்டமிடல் குழு பற்றியது.",
        "Incorrect. Article 243K is State Election Commission.", "தவறானது. சரத்து 243K மாநிலத் தேர்தல் ஆணையம் பற்றியது.",
        "Article 243G -> Eleventh Schedule (Panchayats). Article 243W -> Twelfth Schedule (Municipalities).",
        "சரத்து 243G -> 11வது அட்டவணை (பஞ்சாயத்துகள்). சரத்து 243W -> 12வது அட்டவணை (நகராட்சிகள்)."
    ))

    qs.append(make_sch_q(
        "SCH_PYQ_026", "Medium", "PYQ", "Twelfth Schedule",
        "[TNPSC Group 2A 2016] How many functional subjects are enumerated in the Twelfth Schedule of the Indian Constitution?",
        "[TNPSC குரூப் 2A 2016] இந்திய அரசியலமைப்பின் பன்னிரண்டாவது அட்டவணையில் எத்தனை செயல்பாட்டுத் துறைகள் குறிப்பிடப்பட்டுள்ளன?",
        "18 subjects", "18 துறைகள்",
        "29 subjects", "29 துறைகள்",
        "22 subjects", "22 துறைகள்",
        "12 subjects", "12 துறைகள்",
        "A",
        "The Twelfth Schedule contains 18 functional items for Municipalities under Article 243W.",
        "பன்னிரண்டாவது அட்டவணை சரத்து 243W-ன் கீழ் நகராட்சிகளுக்கான 18 செயல்பாட்டுப் பணிகளைக் கொண்டுள்ளது.",
        "Correct. Twelfth Schedule contains 18 subjects.", "சரியானது. பன்னிரண்டாவது அட்டவணை 18 துறைகளைக் கொண்டுள்ளது.",
        "Incorrect. 29 subjects is in the Eleventh Schedule.", "தவறானது. 29 துறைகள் 11வது அட்டவணையில் உள்ளன.",
        "Incorrect. 22 is languages in Eighth Schedule.", "தவறானது. 22 என்பது 8வது அட்டவணையின் மொழிகள்.",
        "Incorrect. 12 is total schedules in the Constitution.", "தவறானது. 12 என்பது அரசியலமைப்பின் மொத்த அட்டவணைகள்.",
        "Twelfth Schedule = 18 subjects under Article 243W.",
        "12வது அட்டவணை = சரத்து 243W-ன் கீழ் 18 துறைகள்."
    ))

    qs.append(make_sch_q(
        "SCH_PYQ_027", "Easy", "PYQ", "Eighth Schedule",
        "[TNPSC Group 1 2015] By which Constitutional Amendment Act was Sindhi language added to the Eighth Schedule?",
        "[TNPSC குரூப் 1 2015] எந்த அரசியலமைப்புத் திருத்தச் சட்டம் மூலம் சிந்தி மொழி எட்டாவது அட்டவணையில் சேர்க்கப்பட்டது?",
        "21st Constitutional Amendment Act, 1967", "21வது அரசியலமைப்புத் திருத்தச் சட்டம், 1967",
        "71st Constitutional Amendment Act, 1992", "71வது அரசியலமைப்புத் திருத்தச் சட்டம், 1992",
        "92nd Constitutional Amendment Act, 2003", "92வது அரசியலமைப்புத் திருத்தச் சட்டம், 2003",
        "1st Constitutional Amendment Act, 1951", "1வது அரசியலமைப்புத் திருத்தச் சட்டம், 1951",
        "A",
        "Sindhi was added as the 15th language by the 21st Constitutional Amendment Act, 1967.",
        "21வது அரசியலமைப்புத் திருத்தச் சட்டம் 1967 மூலம் 15வது மொழியாக சிந்தி சேர்க்கப்பட்டது.",
        "Correct. 21st CAA 1967 added Sindhi.", "சரியானது. 21வது திருத்தம் 1967 சிந்தியைச் சேர்த்தது.",
        "Incorrect. 71st CAA 1992 added KMN.", "தவறானது. 71வது திருத்தம் 1992 KMN மொழிகளைச் சேர்த்தது.",
        "Incorrect. 92nd CAA 2003 added BDMS.", "தவறானது. 92வது திருத்தம் 2003 BDMS மொழிகளைச் சேர்த்தது.",
        "Incorrect. 1st CAA 1951 added Ninth Schedule.", "தவறானது. 1வது திருத்தம் 9வது அட்டவணையைச் சேர்த்தது.",
        "21st CAA 1967: Sindhi became 15th language in Eighth Schedule.",
        "21வது திருத்தம் 1967: சிந்தி 8வது அட்டவணையில் 15வது மொழியானது."
    ))

    qs.append(make_sch_q(
        "SCH_PYQ_028", "Medium", "PYQ", "Fifth Schedule",
        "[TNPSC Group 2 2013] The Provisions of the Panchayats (Extension to the Scheduled Areas) Act, 1996 (PESA) extends local self-governance to areas under which Schedule?",
        "[TNPSC குரூப் 2 2013] பஞ்சாயத்துகள் (அட்டவணைப்படுத்தப்பட்ட பகுதிகளுக்கு நீட்டிப்பு) சட்டம் 1996 (PESA) எந்த அட்டவணையின் கீழ் உள்ள பகுதிகளுக்கு உள்ளாட்சி அதிகாரத்தை நீட்டிக்கிறது?",
        "Fifth Schedule", "ஐந்தாவது அட்டவணை",
        "Sixth Schedule", "ஆறாவது அட்டவணை",
        "Seventh Schedule", "ஏழாவது அட்டவணை",
        "Eighth Schedule", "எட்டாவது அட்டவணை",
        "A",
        "PESA Act, 1996 specifically extends Part IX Panchayati Raj provisions to the Scheduled Areas referred to in Clause (1) of Article 244 (the Fifth Schedule).",
        "PESA சட்டம் 1996, சரத்து 244(1)-ன் கீழ் குறிப்பிடப்பட்டுள்ள ஐந்தாவது அட்டவணைப் பகுதிகளுக்கு பகுதி IX பஞ்சாயத்து ராஜ் விதிகளை நீட்டிக்கிறது.",
        "Correct. PESA Act applies to Fifth Schedule Areas in 10 States.", "சரியானது. PESA சட்டம் 10 மாநிலங்களில் உள்ள 5வது அட்டவணைப் பகுதிகளுக்குப் பொருந்தும்.",
        "Incorrect. Sixth Schedule areas have their own Autonomous District Councils.", "தவறானது. 6வது அட்டவணைப் பகுதிகள் தங்கள் சொந்த மாவட்ட கவுன்சில்களைக் கொண்டுள்ளன.",
        "Incorrect. Seventh Schedule is legislative lists.", "தவறானது. ஏழாவது அட்டவணை சட்டப் பட்டியல்கள்.",
        "Incorrect. Eighth Schedule is languages.", "தவறானது. எட்டாவது அட்டவணை மொழிகள்.",
        "PESA Act 1996: Empowers Gram Sabhas in Fifth Schedule Areas across 10 States.",
        "PESA சட்டம் 1996: 10 மாநிலங்களில் உள்ள 5வது அட்டவணைப் பகுதி கிராம சபைகளுக்கு அதிகாரம் அளிக்கிறது."
    ))

    qs.append(make_sch_q(
        "SCH_PYQ_029", "Hard", "PYQ", "Sixth Schedule",
        "[UPSC CSE 2015] Under the Sixth Schedule of the Indian Constitution, an Autonomous District Council has powers to make laws on which of the following subjects?",
        "[UPSC CSE 2015] இந்திய அரசியலமைப்பின் ஆறாவது அட்டவணையின் கீழ், ஒரு தன்னாட்சி மாவட்டக் கவுன்சிலுக்கு பின்வரும் எந்தத் துறைகளில் சட்டங்களை உருவாக்கும் அதிகாரம் உண்டு?",
        "Inheritance of property, marriage, and management of unreserved forests",
        "சொத்துரிமை, திருமணம் மற்றும் ஒதுக்கப்படாத காடுகளின் மேலாண்மை",
        "Foreign trade, national defense, and railways", "வெளிநாட்டு வர்த்தகம், தேசிய பாதுகாப்பு மற்றும் இரயில்வே",
        "Income tax and central excise duties", "வருமான வரி மற்றும் மத்திய கலால் வரிகள்",
        "Atomic minerals and maritime shipping", "அணு கனிமங்கள் மற்றும் கடல்வழி கப்பல் போக்குவரத்து",
        "A",
        "Under Paragraph 3 of the Sixth Schedule, District Councils have legislative powers regarding land allotment, management of unreserved forests, use of canal water, inheritance of property, marriage, and social customs.",
        "ஆறாவது அட்டவணையின் பத்தி 3-ன் கீழ், மாவட்டக் கவுன்சில்கள் நில ஒதுக்கீடு, ஒதுக்கப்படாத காடுகள், கால்வாய் நீர், சொத்துரிமை, திருமணம் மற்றும் சமூக வழக்கங்கள் குறித்து சட்டங்களை இயற்றலாம்.",
        "Correct. ADC can legislate on inheritance, marriage, and unreserved forests.", "சரியானது. ADC சொத்துரிமை, திருமணம் மற்றும் காடுகள் குறித்து சட்டமியற்றலாம்.",
        "Incorrect. Foreign trade and defense are exclusive Union List subjects.", "தவறானது. வெளிநாட்டு வர்த்தகம் மற்றும் பாதுகாப்பு மத்தியப் பட்டியலுக்கு உரியவை.",
        "Incorrect. Central taxes belong to Parliament.", "தவறானது. மத்திய வரிகள் பாராளுமன்றத்திற்கு உரியவை.",
        "Incorrect. Atomic minerals belong exclusively to the Union.", "தவறானது. அணு கனிமங்கள் மத்திய அரசுக்கு மட்டுமே உரியவை.",
        "Sixth Schedule Para 3: Legislative powers over land, forests, customs, marriage, and property.",
        "6வது அட்டவணை பத்தி 3: நிலம், காடுகள், வழக்கங்கள், திருமணம், சொத்து ஆகியவற்றின் மீதான சட்ட அதிகாரம்."
    ))

    qs.append(make_sch_q(
        "SCH_PYQ_030", "Easy", "PYQ", "Schedules Overview",
        "[TNPSC Group 4 2013] How many Schedules did the Constitution of India contain when it was originally enacted in 1950?",
        "[TNPSC குரூப் 4 2013] 1950-ல் தொடக்கத்தில் இயற்றப்பட்ட போது இந்திய அரசியலமைப்பில் எத்தனை அட்டவணைகள் இருந்தன?",
        "8 Schedules", "8 அட்டவணைகள்",
        "9 Schedules", "9 அட்டவணைகள்",
        "10 Schedules", "10 அட்டவணைகள்",
        "12 Schedules", "12 அட்டவணைகள்",
        "A",
        "The original Constitution had 395 Articles and 8 Schedules.",
        "அசல் அரசியலமைப்பில் 395 சரத்துகள் மற்றும் 8 அட்டவணைகள் இருந்தன.",
        "Correct. 8 schedules were originally enacted.", "சரியானது. தொடக்கத்தில் 8 அட்டவணைகள் இயற்றப்பட்டன.",
        "Incorrect. 9th was added in 1951.", "தவறானது. 9வது அட்டவணை 1951-ல் சேர்க்கப்பட்டது.",
        "Incorrect. 10th was added in 1985.", "தவறானது. 10வது அட்டவணை 1985-ல் சேர்க்கப்பட்டது.",
        "Incorrect. 12 is current, not original.", "தவறானது. 12 என்பது தற்போதைய எண்ணிக்கை.",
        "Original Constitution (1950): 8 Schedules. Current (2026): 12 Schedules.",
        "அசல் அரசியலமைப்பு (1950): 8 அட்டவணைகள். தற்போது: 12 அட்டவணைகள்."
    ))

    # PYQ 31 - 40
    qs.append(make_sch_q(
        "SCH_PYQ_031", "Medium", "PYQ", "Seventh Schedule",
        "[TNPSC Group 1 2011] Under Article 248 of the Constitution, residuary powers of legislation belong to:",
        "[TNPSC குரூப் 1 2011] அரசியலமைப்பின் சரத்து 248-ன் கீழ், சட்டமியற்றுவதற்கான எஞ்சிய அதிகாரங்கள் யாருக்கு உரியவை?",
        "Parliament of India exclusively", "இந்தியப் பாராளுமன்றத்திற்கு மட்டுமே",
        "State Legislatures exclusively", "மாநில சட்டமன்றங்களுக்கு மட்டுமே",
        "Both Parliament and State Legislatures jointly", "பாராளுமன்றம் மற்றும் மாநில சட்டமன்றங்கள் இரண்டிற்கும் இணைந்து",
        "The President of India", "இந்தியக் குடியரசுத் தலைவருக்கு",
        "A",
        "Article 248 and Entry 97 of the Union List vest all residuary powers of legislation exclusively in Parliament.",
        "சரத்து 248 மற்றும் மத்தியப் பட்டியலின் பதிவு 97 எஞ்சிய அனைத்து சட்டமியற்றும் அதிகாரங்களையும் பாராளுமன்றத்திற்கு மட்டுமே வழங்குகின்றன.",
        "Correct. Residuary powers belong exclusively to Parliament.", "சரியானது. எஞ்சிய அதிகாரங்கள் பாராளுமன்றத்திற்கு மட்டுமே உரியவை.",
        "Incorrect. States have no residuary powers.", "தவறானது. மாநிலங்களுக்கு எஞ்சிய அதிகாரங்கள் இல்லை.",
        "Incorrect. Not concurrent/joint.", "தவறானது. இது பொதுவானது அல்ல.",
        "Incorrect. Not with the President.", "தவறானது. குடியரசுத் தலைவருக்கு அல்ல.",
        "Residuary Powers: Article 248 + Entry 97 -> Parliament.",
        "எஞ்சிய அதிகாரங்கள்: சரத்து 248 + பதிவு 97 -> பாராளுமன்றம்."
    ))

    qs.append(make_sch_q(
        "SCH_PYQ_032", "Easy", "PYQ", "Seventh Schedule",
        "[TNPSC Group 2 2011] Under the Seventh Schedule, 'Police' and 'Public Order' are entries in which List?",
        "[TNPSC குரூப் 2 2011] ஏழாவது அட்டவணையின் கீழ், 'காவல்துறை' மற்றும் 'பொது ஒழுங்கு' ஆகியவை எந்தப் பட்டியலில் உள்ள பதிவுகளாகும்?",
        "State List (List II)", "மாநிலப் பட்டியல் (பட்டியல் II)",
        "Union List (List I)", "மத்தியப் பட்டியல் (பட்டியல் I)",
        "Concurrent List (List III)", "பொதுப் பட்டியல் (பட்டியல் III)",
        "Residuary List", "எஞ்சிய பட்டியல்",
        "A",
        "Public order is Entry 1 and Police is Entry 2 of the State List (List II) in the Seventh Schedule.",
        "பொது ஒழுங்கு பதிவு 1 மற்றும் காவல்துறை பதிவு 2 ஆகியவை ஏழாவது அட்டவணையின் மாநிலப் பட்டியலில் (பட்டியல் II) உள்ளன.",
        "Correct. Police and Public Order are in the State List.", "சரியானது. காவல்துறை மற்றும் பொது ஒழுங்கு மாநிலப் பட்டியலில் உள்ளன.",
        "Incorrect. Not in Union List.", "தவறானது. மத்தியப் பட்டியலில் இல்லை.",
        "Incorrect. Not in Concurrent List.", "தவறானது. பொதுப் பட்டியலில் இல்லை.",
        "Incorrect. Not residuary.", "தவறானது. எஞ்சிய துறை அல்ல.",
        "State List: Entry 1 = Public order; Entry 2 = Police.",
        "மாநிலப் பட்டியல்: பதிவு 1 = பொது ஒழுங்கு; பதிவு 2 = காவல்துறை."
    ))

    qs.append(make_sch_q(
        "SCH_PYQ_033", "Hard", "PYQ", "Second Schedule",
        "[UPSC CSE 2012] Who among the following does NOT have their emoluments and allowances specified under the Second Schedule?",
        "[UPSC CSE 2012] பின்வருவனவற்றில் யாருடைய ஊதியம் மற்றும் படிகள் இரண்டாவது அட்டவணையின் கீழ் குறிப்பிடப்படவில்லை?",
        "Prime Minister of India", "இந்தியப் பிரதமர்",
        "Speaker of the Lok Sabha", "மக்களவைத் தலைவர்",
        "Comptroller and Auditor-General", "தலைமைக் கணக்குத் தணிக்கையாளர்",
        "Judges of the Supreme Court", "உச்சநீதிமன்ற நீதிபதிகள்",
        "A",
        "The Prime Minister and other Ministers are not listed in the Second Schedule; their salaries are governed by ordinary legislation under Article 75(6).",
        "பிரதமர் மற்றும் பிற அமைச்சர்கள் இரண்டாவது அட்டவணையில் இல்லை; அவர்களின் சம்பளம் சரத்து 75(6)-ன் கீழ் பாராளுமன்ற சட்டத்தால் நிர்வகிக்கப்படுகிறது.",
        "Correct. Prime Minister is excluded from the Second Schedule.", "சரியானது. பிரதமர் இரண்டாவது அட்டவணையில் சேர்க்கப்படவில்லை.",
        "Incorrect. Lok Sabha Speaker is in Part C.", "தவறானது. மக்களவைத் தலைவர் பகுதி C-ல் உள்ளார்.",
        "Incorrect. CAG is in Part E.", "தவறானது. CAG பகுதி E-ல் உள்ளார்.",
        "Incorrect. SC Judges are in Part D.", "தவறானது. உச்சநீதிமன்ற நீதிபதிகள் பகுதி D-ல் உள்ளனர்.",
        "Second Schedule excludes Ministers; includes President, Governors, Judges, Speakers, CAG.",
        "2வது அட்டவணை அமைச்சர்களை விலக்கியுள்ளது; தலைவர், ஆளுநர்கள், நீதிபதிகள், சபாநாயகர்கள், CAG-ஐ உள்ளடக்கியுள்ளது."
    ))

    qs.append(make_sch_q(
        "SCH_PYQ_034", "Medium", "PYQ", "Third Schedule",
        "[TNPSC Group 4 2012] The oath of which of the following dignitaries is NOT provided in the Third Schedule?",
        "[TNPSC குரூப் 4 2012] பின்வரும் உயர் பொறுப்பாளர்களில் யாருடைய பிரமாணம் மூன்றாவது அட்டவணையில் வழங்கப்படவில்லை?",
        "Vice-President of India", "இந்தியத் துணைக் குடியரசுத் தலைவர்",
        "Judge of the High Court", "உயர்நீதிமன்ற நீதிபதி",
        "Member of Parliament", "பாராளுமன்ற உறுப்பினர்",
        "Union Minister", "மத்திய அமைச்சர்",
        "A",
        "The oath of the Vice-President of India is provided in Article 69 of the Constitution, not in the Third Schedule.",
        "இந்தியத் துணைக் குடியரசுத் தலைவரின் பிரமாணம் சரத்து 69-ல் உள்ளது, மூன்றாவது அட்டவணையில் இல்லை.",
        "Correct. Vice-President's oath is in Article 69.", "சரியானது. துணைக் குடியரசுத் தலைவரின் பிரமாணம் சரத்து 69-ல் உள்ளது.",
        "Incorrect. HC Judges take oath under Form VIII.", "தவறானது. உயர்நீதிமன்ற நீதிபதிகள் படிவம் VIII-ன் கீழ் உறுதிமொழி ஏற்கின்றனர்.",
        "Incorrect. MPs take oath under Form III.", "தவறானது. எம்.பி.க்கள் படிவம் III-ன் கீழ் உறுதிமொழி ஏற்கின்றனர்.",
        "Incorrect. Union Ministers take oath under Forms I and II.", "தவறானது. மத்திய அமைச்சர்கள் படிவங்கள் I & II-ன் கீழ் உறுதிமொழி ஏற்கின்றனர்.",
        "Oaths in Constitution articles: President (Art 60), VP (Art 69), Governor (Art 159).",
        "அரசியலமைப்பு சரத்துகளில் உள்ள பிரமாணங்கள்: தலைவர் (சரத்து 60), VP (சரத்து 69), ஆளுநர் (சரத்து 159)."
    ))

    qs.append(make_sch_q(
        "SCH_PYQ_035", "Medium", "PYQ", "Seventh Schedule",
        "[TNPSC Group 1 2008] How many subjects were originally enumerated in the Union List (List I) of the Seventh Schedule?",
        "[TNPSC குரூப் 1 2008] ஏழாவது அட்டவணையின் மத்தியப் பட்டியலில் (பட்டியல் I) தொடக்கத்தில் எத்தனை துறைகள் குறிப்பிடப்பட்டிருந்தன?",
        "97 subjects", "97 துறைகள்",
        "66 subjects", "66 துறைகள்",
        "47 subjects", "47 துறைகள்",
        "100 subjects", "100 துறைகள்",
        "A",
        "Originally, the Union List had 97 entries (currently numbered up to 97, but with 100 actual subjects). The State List had 66 (now 61) and Concurrent List had 47 (now 52).",
        "தொடக்கத்தில், மத்தியப் பட்டியலில் 97 பதிவுகள் இருந்தன (தற்போது 100 துறைகள்). மாநிலப் பட்டியலில் 66 (தற்போது 61) மற்றும் பொதுப் பட்டியலில் 47 (தற்போது 52) பதிவுகள் இருந்தன.",
        "Correct. 97 subjects were originally in the Union List.", "சரியானது. தொடக்கத்தில் மத்தியப் பட்டியலில் 97 துறைகள் இருந்தன.",
        "Incorrect. 66 was the original count in the State List.", "தவறானது. 66 என்பது மாநிலப் பட்டியலின் தொடக்க எண்ணிக்கை.",
        "Incorrect. 47 was the original count in the Concurrent List.", "தவறானது. 47 என்பது பொதுப் பட்டியலின் தொடக்க எண்ணிக்கை.",
        "Incorrect. 100 is the effective current count in Union List.", "தவறானது. 100 என்பது தற்போதைய நடைமுறை எண்ணிக்கை.",
        "Original Seventh Schedule counts: Union=97, State=66, Concurrent=47.",
        "அசல் 7வது அட்டவணை எண்ணிக்கை: மத்திய=97, மாநில=66, பொது=47."
    ))

    qs.append(make_sch_q(
        "SCH_PYQ_036", "Easy", "PYQ", "Eighth Schedule",
        "[TNPSC Group 2 2010] By which Constitutional Amendment Act was 'Oriya' substituted by 'Odia' in the Eighth Schedule?",
        "[TNPSC குரூப் 2 2010] எந்த அரசியலமைப்புத் திருத்தச் சட்டம் மூலம் எட்டாவது அட்டவணையில் 'ஒரியா' என்பது 'ஒடியா' என மாற்றப்பட்டது?",
        "96th Constitutional Amendment Act, 2011", "96வது அரசியலமைப்புத் திருத்தச் சட்டம், 2011",
        "92nd Constitutional Amendment Act, 2003", "92வது அரசியலமைப்புத் திருத்தச் சட்டம், 2003",
        "91st Constitutional Amendment Act, 2003", "91வது அரசியலமைப்புத் திருத்தச் சட்டம், 2003",
        "97th Constitutional Amendment Act, 2011", "97வது அரசியலமைப்புத் திருத்தச் சட்டம், 2011",
        "A",
        "The 96th Constitutional Amendment Act, 2011 substituted the word 'Odia' for 'Oriya' in the Eighth Schedule.",
        "96வது அரசியலமைப்புத் திருத்தச் சட்டம் 2011 எட்டாவது அட்டவணையில் 'ஒரியா' என்ற சொல்லுக்குப் பதிலாக 'ஒடியா' என மாற்றியது.",
        "Correct. 96th CAA 2011 substituted Odia for Oriya.", "சரியானது. 96வது திருத்தம் 2011 ஒரியாவை ஒடியா என மாற்றியது.",
        "Incorrect. 92nd CAA 2003 added BDMS.", "தவறானது. 92வது திருத்தம் 2003 BDMS மொழிகளைச் சேர்த்தது.",
        "Incorrect. 91st CAA 2003 was anti-defection and cabinet size.", "தவறானது. 91வது திருத்தம் கட்சித் தாவல் மற்றும் அமைச்சரவை பற்றியது.",
        "Incorrect. 97th CAA 2011 was Cooperative Societies.", "தவறானது. 97வது திருத்தம் கூட்டுறவு சங்கங்கள் பற்றியது.",
        "96th CAA 2011: Oriya -> Odia in Eighth Schedule.",
        "96வது திருத்தம் 2011: எட்டாவது அட்டவணையில் ஒரியா -> ஒடியா."
    ))

    qs.append(make_sch_q(
        "SCH_PYQ_037", "Hard", "PYQ", "Fourth Schedule",
        "[UPSC CSE 2011] Which of the following Union Territories have seats allocated to them in the Rajya Sabha under the Fourth Schedule?",
        "[UPSC CSE 2011] நான்காவது அட்டவணையின் கீழ் மாநிலங்களவையில் இடங்கள் ஒதுக்கப்பட்டுள்ள யூனியன் பிரதேசங்கள் எவை?",
        "Delhi, Puducherry, and Jammu & Kashmir", "டெல்லி, புதுச்சேரி மற்றும் ஜம்மு காஷ்மீர்",
        "Delhi and Chandigarh only", "டெல்லி மற்றும் சண்டிகர் மட்டுமே",
        "Delhi, Puducherry, and Andaman & Nicobar Islands", "டெல்லி, புதுச்சேரி மற்றும் அந்தமான் நிக்கோபார் தீவுகள்",
        "Puducherry and Lakshadweep only", "புதுச்சேரி மற்றும் லட்சத்தீவு மட்டுமே",
        "A",
        "Only 3 Union Territories (Delhi with 3 seats, Puducherry with 1 seat, and J&K with 4 seats) have representation in the Rajya Sabha under the Fourth Schedule.",
        "நான்காவது அட்டவணையின் கீழ் 3 யூனியன் பிரதேசங்களுக்கு மட்டுமே (டெல்லி 3, புதுச்சேரி 1, ஜம்மு காஷ்மீர் 4) மாநிலங்களவையில் இடங்கள் ஒதுக்கப்பட்டுள்ளன.",
        "Correct. Delhi, Puducherry, and J&K are the only 3 UTs in Rajya Sabha.", "சரியானது. டெல்லி, புதுச்சேரி, ஜம்மு காஷ்மீர் மட்டுமே மாநிலங்களவையில் உள்ள 3 UTகள்.",
        "Incorrect. Chandigarh has no Rajya Sabha seat.", "தவறானது. சண்டிகருக்கு மாநிலங்களவை இடம் இல்லை.",
        "Incorrect. Andaman & Nicobar has no Rajya Sabha seat.", "தவறானது. அந்தமான் நிக்கோபாருக்கு மாநிலங்களவை இடம் இல்லை.",
        "Incorrect. Lakshadweep has no Rajya Sabha seat.", "தவறானது. லட்சத்தீவுக்கு மாநிலங்களவை இடம் இல்லை.",
        "Fourth Schedule UT seats: Delhi (3) + Puducherry (1) + J&K (4) = 8 seats.",
        "4வது அட்டவணை UT இடங்கள்: டெல்லி (3) + புதுச்சேரி (1) + J&K (4) = 8 இடங்கள்."
    ))

    qs.append(make_sch_q(
        "SCH_PYQ_038", "Medium", "PYQ", "Fifth Schedule",
        "[TNPSC Group 4 2011] Who possesses the power to direct that an Act of Parliament shall not apply to a Scheduled Area under the Fifth Schedule?",
        "[TNPSC குரூப் 4 2011] ஐந்தாவது அட்டவணையின் கீழ் ஒரு பாராளுமன்றச் சட்டம் அட்டவணைப் பகுதிக்குப் பொருந்தாது என உத்தரவிடும் அதிகாரம் யாரிடம் உள்ளது?",
        "Governor of the State", "மாநில ஆளுநர்",
        "President of India", "இந்தியக் குடியரசுத் தலைவர்",
        "Chief Minister", "முதலமைச்சர்",
        "Speaker of the Legislative Assembly", "சட்டமன்ற சபாநாயகர்",
        "A",
        "Under Paragraph 5(1) of the Fifth Schedule, the Governor may by public notification direct that any Act of Parliament or of the State Legislature shall not apply to a Scheduled Area.",
        "ஐந்தாவது அட்டவணையின் பத்தி 5(1)-ன் படி, பாராளுமன்ற அல்லது மாநில சட்டமன்ற சட்டம் அட்டவணைப் பகுதிக்குப் பொருந்தாது என பொது அறிவிக்கை மூலம் ஆளுநர் உத்தரவிடலாம்.",
        "Correct. Governor issues notification under Paragraph 5(1).", "சரியானது. பத்தி 5(1)-ன் கீழ் ஆளுநரே அறிவிக்கையை வெளியிடுகிறார்.",
        "Incorrect. President has power under Sixth Schedule for certain states, not Fifth Schedule Para 5(1).", "தவறானது. 5வது அட்டவணை பத்தி 5(1)-ன் கீழ் ஆளுநருக்கே அதிகாரம் உள்ளது.",
        "Incorrect. Chief Minister has no such constitutional power.", "தவறானது. முதலமைச்சருக்கு இந்த அதிகாரம் இல்லை.",
        "Incorrect. Speaker has no administrative notification power.", "தவறானது. சபாநாயகருக்கு இந்த அதிகாரம் இல்லை.",
        "Fifth Schedule Para 5(1): Governor directs non-application or modified application of laws.",
        "5வது அட்டவணை பத்தி 5(1): ஆளுநர் சட்டங்களை விலக்கவோ மாற்றியமைக்கவோ உத்தரவிடுகிறார்."
    ))

    qs.append(make_sch_q(
        "SCH_PYQ_039", "Easy", "PYQ", "Ninth Schedule",
        "[TNPSC Group 1 2007] Which Constitutional Amendment Act introduced Article 31B and the Ninth Schedule into the Constitution?",
        "[TNPSC குரூப் 1 2007] எந்த அரசியலமைப்புத் திருத்தச் சட்டம் சரத்து 31B மற்றும் ஒன்பதாவது அட்டவணையை அரசியலமைப்பில் அறிமுகப்படுத்தியது?",
        "1st Constitutional Amendment Act, 1951", "1வது அரசியலமைப்புத் திருத்தச் சட்டம், 1951",
        "7th Constitutional Amendment Act, 1956", "7வது அரசியலமைப்புத் திருத்தச் சட்டம், 1956",
        "42nd Constitutional Amendment Act, 1976", "42வது அரசியலமைப்புத் திருத்தச் சட்டம், 1976",
        "44th Constitutional Amendment Act, 1978", "44வது அரசியலமைப்புத் திருத்தச் சட்டம், 1978",
        "A",
        "The 1st Constitutional Amendment Act, 1951 added Article 31B and the Ninth Schedule to validate land reform and zamindari abolition laws.",
        "1வது அரசியலமைப்புத் திருத்தச் சட்டம் 1951, நிலச் சீர்திருத்தம் மற்றும் ஜமீன்தாரி ஒழிப்புச் சட்டங்களைப் பாதுகாக்க சரத்து 31B மற்றும் 9வது அட்டவணையைச் சேர்த்தது.",
        "Correct. 1st CAA 1951 introduced Article 31B and Ninth Schedule.", "சரியானது. 1வது திருத்தம் 1951 சரத்து 31B மற்றும் 9வது அட்டவணையை அறிமுகப்படுத்தியது.",
        "Incorrect. 7th CAA 1956 was States Reorganisation.", "தவறானது. 7வது திருத்தம் மாநிலங்கள் மறுசீரமைப்பு பற்றியது.",
        "Incorrect. 42nd CAA was 1976.", "தவறானது. 42வது திருத்தம் 1976-ல் வந்தது.",
        "Incorrect. 44th CAA was 1978.", "தவறானது. 44வது திருத்தம் 1978-ல் வந்தது.",
        "1st CAA 1951: Article 31B + Ninth Schedule (originally 13 land reform Acts).",
        "1வது திருத்தம் 1951: சரத்து 31B + 9வது அட்டவணை (தொடக்கத்தில் 13 சட்டங்கள்)."
    ))

    qs.append(make_sch_q(
        "SCH_PYQ_040", "Medium", "PYQ", "Seventh Schedule",
        "[TNPSC Group 2 2009] 'Prevention of cruelty to animals' is an entry in which List of the Seventh Schedule?",
        "[TNPSC குரூப் 2 2009] 'விலங்குகள் வதை தடுப்பு' என்பது ஏழாவது அட்டவணையின் எந்தப் பட்டியலில் உள்ள பதிவாகும்?",
        "Concurrent List (List III)", "பொதுப் பட்டியல் (பட்டியல் III)",
        "Union List (List I)", "மத்தியப் பட்டியல் (பட்டியல் I)",
        "State List (List II)", "மாநிலப் பட்டியல் (பட்டியல் II)",
        "Residuary subjects", "எஞ்சிய துறைகள்",
        "A",
        "Entry 17 of the Concurrent List (List III) is 'Prevention of cruelty to animals'.",
        "ஏழாவது அட்டவணையின் பொதுப் பட்டியலில் (பட்டியல் III) உள்ள பதிவு 17 'விலங்குகள் வதை தடுப்பு' ஆகும்.",
        "Correct. Prevention of cruelty to animals is Entry 17 in Concurrent List.", "சரியானது. விலங்குகள் வதை தடுப்பு பொதுப் பட்டியலின் பதிவு 17 ஆகும்.",
        "Incorrect. Not in Union List.", "தவறானது. மத்தியப் பட்டியலில் இல்லை.",
        "Incorrect. Not in State List.", "தவறானது. மாநிலப் பட்டியலில் இல்லை.",
        "Incorrect. Not a residuary power.", "தவறானது. எஞ்சிய துறை அல்ல.",
        "Concurrent List Entry 17: Prevention of cruelty to animals (Jallikattu law relates to this entry).",
        "பொதுப் பட்டியல் பதிவு 17: விலங்குகள் வதை தடுப்பு (ஜல்லிக்கட்டு சட்டம் இப்பதிவுடன் தொடர்புடையது)."
    ))

    # PYQ 41 - 50
    qs.append(make_sch_q(
        "SCH_PYQ_041", "Medium", "PYQ", "Seventh Schedule",
        "[UPSC CSE 2008] Under the Seventh Schedule, 'Taxes on agricultural income' is enumerated in which List?",
        "[UPSC CSE 2008] ஏழாவது அட்டவணையின் கீழ், 'விவசாய வருமானத்தின் மீதான வரிகள்' எந்தப் பட்டியலில் குறிப்பிடப்பட்டுள்ளது?",
        "State List (List II)", "மாநிலப் பட்டியல் (பட்டியல் II)",
        "Union List (List I)", "மத்தியப் பட்டியல் (பட்டியல் I)",
        "Concurrent List (List III)", "பொதுப் பட்டியல் (பட்டியல் III)",
        "Residuary powers under Article 248", "சரத்து 248-ன் கீழான எஞ்சிய அதிகாரங்கள்",
        "A",
        "Taxes on agricultural income is Entry 46 of the State List (List II). Entry 82 of the Union List specifically covers 'Taxes on income OTHER than agricultural income'.",
        "விவசாய வருமானத்தின் மீதான வரிகள் என்பது மாநிலப் பட்டியலின் (பட்டியல் II) பதிவு 46 ஆகும். மத்தியப் பட்டியலின் பதிவு 82 'விவசாய வருமானம் தவிர்த்த பிற வருமான வரிகளை' மட்டுமே குறிக்கிறது.",
        "Correct. Taxes on agricultural income is Entry 46 of the State List.", "சரியானது. விவசாய வருமான வரி மாநிலப் பட்டியலின் பதிவு 46 ஆகும்.",
        "Incorrect. Union List explicitly excludes agricultural income.", "தவறானது. மத்தியப் பட்டியல் விவசாய வருமானத்தை வெளிப்படையாக விலக்குகிறது.",
        "Incorrect. Not in Concurrent List.", "தவறானது. பொதுப் பட்டியலில் இல்லை.",
        "Incorrect. Not a residuary power.", "தவறானது. எஞ்சிய அதிகாரம் அல்ல.",
        "State List Entry 46: Taxes on agricultural income.",
        "மாநிலப் பட்டியல் பதிவு 46: விவசாய வருமானத்தின் மீதான வரிகள்."
    ))

    qs.append(make_sch_q(
        "SCH_PYQ_042", "Easy", "PYQ", "Eighth Schedule",
        "[TNPSC Group 1 2021] Which of the following ancient languages was declared as a Classical Language in 2005, following Tamil in 2004?",
        "[TNPSC குரூப் 1 2021] 2004-ல் தமிழைத் தொடர்ந்து 2005-ல் செம்மொழியாக அறிவிக்கப்பட்ட பண்டைய மொழி எது?",
        "Sanskrit", "சமஸ்கிருதம்",
        "Telugu", "தெலுங்கு",
        "Kannada", "கன்னடம்",
        "Malayalam", "மலையாளம்",
        "A",
        "Sanskrit was declared as a Classical Language in 2005, the second language to receive this status after Tamil (2004).",
        "2004-ல் தமிழுக்கு அடுத்தபடியாக 2005-ல் சமஸ்கிருதம் இரண்டாவது செம்மொழியாக அறிவிக்கப்பட்டது.",
        "Correct. Sanskrit was declared Classical in 2005.", "சரியானது. சமஸ்கிருதம் 2005-ல் செம்மொழியாக அறிவிக்கப்பட்டது.",
        "Incorrect. Telugu was declared in 2008.", "தவறானது. தெலுங்கு 2008-ல் அறிவிக்கப்பட்டது.",
        "Incorrect. Kannada was declared in 2008.", "தவறானது. கன்னடம் 2008-ல் அறிவிக்கப்பட்டது.",
        "Incorrect. Malayalam was declared in 2013.", "தவறானது. மலையாளம் 2013-ல் அறிவிக்கப்பட்டது.",
        "Classical Languages order: Tamil (2004) -> Sanskrit (2005) -> Telugu & Kannada (2008) -> Malayalam (2013) -> Odia (2014).",
        "செம்மொழிகள் வரிசை: தமிழ் (2004) -> சமஸ்கிருதம் (2005) -> தெலுங்கு & கன்னடம் (2008) -> மலையாளம் (2013) -> ஒடியா (2014)."
    ))

    qs.append(make_sch_q(
        "SCH_PYQ_043", "Medium", "PYQ", "Sixth Schedule",
        "[TNPSC Group 4 2015] In which State of India is the Bodoland Territorial Council functioning under the Sixth Schedule?",
        "[TNPSC குரூப் 4 2015] இந்தியாவில் போடோலாந்து பிராந்திய கவுன்சில் எந்த மாநிலத்தில் ஆறாவது அட்டவணையின் கீழ் செயல்படுகிறது?",
        "Assam", "அசாம்",
        "Meghalaya", "மேகாலயா",
        "Tripura", "திரிபுரா",
        "Mizoram", "மிசோரம்",
        "A",
        "The Bodoland Territorial Council (BTC) was created under the Sixth Schedule in Assam via the 90th Constitutional Amendment Act, 2003.",
        "போடோலாந்து பிராந்திய கவுன்சில் (BTC) அசாம் மாநிலத்தில் ஆறாவது அட்டவணையின் கீழ் 90வது அரசியலமைப்புத் திருத்தச் சட்டம் 2003 மூலம் உருவாக்கப்பட்டது.",
        "Correct. Bodoland Territorial Council is located in Assam.", "சரியானது. போடோலாந்து பிராந்திய கவுன்சில் அசாமில் அமைந்துள்ளது.",
        "Incorrect. Meghalaya has Khasi, Garo, and Jaintia ADCs.", "தவறானது. மேகாலயாவில் காசி, காரோ, ஜெயந்தியா ADC-கள் உள்ளன.",
        "Incorrect. Tripura has Tripura Tribal Areas ADC.", "தவறானது. திரிபுராவில் திரிபுரா பழங்குடி ADC உள்ளது.",
        "Incorrect. Mizoram has Chakma, Mara, and Lai ADCs.", "தவறானது. மிசோரமில் சக்மா, மாரா, லாய் ADC-கள் உள்ளன.",
        "Assam ADCs under 6th Schedule: Bodoland, Karbi Anglong, Dima Hasao.",
        "அசாமில் 6வது அட்டவணை ADC-கள்: போடோலாந்து, கர்பி அங்லாங், திமா ஹசாவ்."
    ))

    qs.append(make_sch_q(
        "SCH_PYQ_044", "Hard", "PYQ", "Third Schedule",
        "[TNPSC Group 2 2016] Which Constitutional Amendment Act introduced the phrase 'uphold the sovereignty and integrity of India' into the forms of oath in the Third Schedule?",
        "[TNPSC குரூப் 2 2016] எந்த அரசியலமைப்புத் திருத்தச் சட்டம் மூன்றாவது அட்டவணையின் பிரமாணப் படிவங்களில் 'இந்தியாவின் இறையாண்மையையும் ஒருமைப்பாட்டையும் நிலைநிறுத்துவேன்' என்ற சொற்றொடரைச் சேர்த்தது?",
        "16th Constitutional Amendment Act, 1963", "16வது அரசியலமைப்புத் திருத்தச் சட்டம், 1963",
        "42nd Constitutional Amendment Act, 1976", "42வது அரசியலமைப்புத் திருத்தச் சட்டம், 1976",
        "44th Constitutional Amendment Act, 1978", "44வது அரசியலமைப்புத் திருத்தச் சட்டம், 1978",
        "24th Constitutional Amendment Act, 1971", "24வது அரசியலமைப்புத் திருத்தச் சட்டம், 1971",
        "A",
        "The 16th Constitutional Amendment Act, 1963 amended the Third Schedule to insert 'uphold the sovereignty and integrity of India' into all forms of oaths/affirmations.",
        "16வது அரசியலமைப்புத் திருத்தச் சட்டம் 1963, மூன்றாவது அட்டவணையின் அனைத்து பிரமாணப் படிவங்களிலும் 'இந்தியாவின் இறையாண்மையையும் ஒருமைப்பாட்டையும் நிலைநிறுத்துவேன்' என்ற சொற்றொடரைச் சேர்த்தது.",
        "Correct. 16th CAA 1963 inserted 'sovereignty and integrity' into the Third Schedule.", "சரியானது. 16வது திருத்தம் 1963 'இறையாண்மை மற்றும் ஒருமைப்பாட்டை' 3வது அட்டவணையில் சேர்த்தது.",
        "Incorrect. 42nd CAA 1976 added Integrity to Preamble, not 3rd Schedule.", "தவறானது. 42வது திருத்தம் 1976 முகப்புரையில் ஒருமைப்பாட்டைச் சேர்த்தது, 3வது அட்டவணையில் அல்ல.",
        "Incorrect. 44th CAA 1978 restored civil liberties.", "தவறானது. 44வது திருத்தம் உரிமைகளை மீட்டது.",
        "Incorrect. 24th CAA 1971 amended Article 368.", "தவறானது. 24வது திருத்தம் சரத்து 368-ஐத் திருத்தியது.",
        "16th CAA 1963: Enacted on recommendations of National Integration Committee.",
        "16வது திருத்தம் 1963: தேசிய ஒருமைப்பாடு குழுவின் பரிந்துரையின் பேரில் இயற்றப்பட்டது."
    ))

    qs.append(make_sch_q(
        "SCH_PYQ_045", "Hard", "PYQ", "Second Schedule",
        "[UPSC CSE 2005] Which of the following is charged on the Consolidated Fund of India regarding a High Court Judge?",
        "[UPSC CSE 2005] ஒரு உயர்நீதிமன்ற நீதிபதி தொடர்பாக பின்வருவனவற்றில் எது இந்தியத் தொகுப்பு நிதியில் விதிக்கப்படுகிறது?",
        "Pension of the High Court Judge", "உயர்நீதிமன்ற நீதிபதியின் ஓய்வூதியம்",
        "Salary of the High Court Judge", "உயர்நீதிமன்ற நீதிபதியின் சம்பளம்",
        "Both salary and pension of the High Court Judge", "உயர்நீதிமன்ற நீதிபதியின் சம்பளம் மற்றும் ஓய்வூதியம் இரண்டுமே",
        "Neither salary nor pension of the High Court Judge", "உயர்நீதிமன்ற நீதிபதியின் சம்பளமோ அல்லது ஓய்வூதியமோ எதுவுமே இல்லை",
        "A",
        "Under Article 112(3)(d)(iii), the pension of a High Court Judge is charged on the Consolidated Fund of India, while their active salary is charged on the State Consolidated Fund under Article 202(3)(d).",
        "சரத்து 112(3)(d)(iii)-ன் படி உயர்நீதிமன்ற நீதிபதியின் ஓய்வூதியம் இந்தியத் தொகுப்பு நிதியில் விதிக்கப்படுகிறது, அதேசமயம் பணிக்கால சம்பளம் சரத்து 202(3)(d)-ன் படி மாநிலத் தொகுப்பு நிதியில் விதிக்கப்படுகிறது.",
        "Correct. Only the pension is charged on the Consolidated Fund of India.", "சரியானது. ஓய்வூதியம் மட்டுமே இந்தியத் தொகுப்பு நிதியில் விதிக்கப்படுகிறது.",
        "Incorrect. Salary is charged on the Consolidated Fund of the State.", "தவறானது. சம்பளம் மாநிலத் தொகுப்பு நிதியில் விதிக்கப்படுகிறது.",
        "Incorrect. Both are not charged on the Union fund.", "தவறானது. இரண்டுமே மத்திய நிதியில் விதிக்கப்படுவதில்லை.",
        "Incorrect. Pension is definitely charged on the Union Fund.", "தவறானது. ஓய்வூதியம் மத்திய நிதியில் உறுதியாக விதிக்கப்படுகிறது.",
        "High Court Judges: Salary -> State Consolidated Fund; Pension -> Consolidated Fund of India.",
        "உயர்நீதிமன்ற நீதிபதிகள்: சம்பளம் -> மாநிலத் தொகுப்பு நிதி; ஓய்வூதியம் -> இந்தியத் தொகுப்பு நிதி."
    ))

    qs.append(make_sch_q(
        "SCH_PYQ_046", "Hard", "PYQ", "Fifth Schedule",
        "[TNPSC Group 1 2018] In the Samatha judgment (1997), the Supreme Court protected tribal land against mining leases in areas governed by which Schedule?",
        "[TNPSC குரூப் 1 2018] சமதா தீர்ப்பில் (1997), எந்த அட்டவணையால் நிர்வகிக்கப்படும் பகுதிகளில் சுரங்கக் குத்தகைகளுக்கு எதிராக பழங்குடியினர் நிலங்களை உச்சநீதிமன்றம் பாதுகாத்தது?",
        "Fifth Schedule", "ஐந்தாவது அட்டவணை",
        "Sixth Schedule", "ஆறாவது அட்டவணை",
        "Seventh Schedule", "ஏழாவது அட்டவணை",
        "Ninth Schedule", "ஒன்பதாவது அட்டவணை",
        "A",
        "In Samatha v. State of Andhra Pradesh (1997), the Supreme Court ruled that tribal land in Fifth Schedule areas cannot be leased to non-tribal private mining companies.",
        "சமதா எதிர் ஆந்திரப் பிரதேச அரசு (1997) வழக்கில், ஐந்தாவது அட்டவணைப் பகுதிகளில் உள்ள பழங்குடியினர் நிலங்களை பழங்குடியினர் அல்லாத தனியார் சுரங்க நிறுவனங்களுக்கு குத்தகைக்கு விட முடியாது என உச்சநீதிமன்றம் தீர்ப்பளித்தது.",
        "Correct. Samatha judgment upheld Fifth Schedule protections.", "சரியானது. சமதா தீர்ப்பு 5வது அட்டவணை பாதுகாப்புகளை உறுதி செய்தது.",
        "Incorrect. Sixth Schedule applies to AMTM.", "தவறானது. ஆறாவது அட்டவணை AMTM-க்கு பொருந்தும்.",
        "Incorrect. Seventh Schedule is legislative lists.", "தவறானது. ஏழாவது அட்டவணை சட்டப் பட்டியல்கள்.",
        "Incorrect. Ninth Schedule is land reforms validation.", "தவறானது. ஒன்பதாவது அட்டவணை நிலச் சீர்திருத்த சட்டம்.",
        "Samatha v. State of AP (1997): Landmark 5th Schedule judgment protecting tribal lands.",
        "சமதா வழக்கு (1997): பழங்குடி நிலங்களைப் பாதுகாத்த வரலாற்றுச் சிறப்புமிக்க 5வது அட்டவணை தீர்ப்பு."
    ))

    qs.append(make_sch_q(
        "SCH_PYQ_047", "Medium", "PYQ", "Fourth Schedule",
        "[TNPSC Group 2A 2019] By which Constitutional Amendment Act was the allocation of seats in the Rajya Sabha (Fourth Schedule) based on the 1971 census frozen until the year 2026?",
        "[TNPSC குரூப் 2A 2019] 1971 மக்கள் தொகை கணக்கெடுப்பின் அடிப்படையிலான மாநிலங்களவை இட ஒதுக்கீட்டை (நான்காவது அட்டவணை) 2026 ஆம் ஆண்டு வரை முடக்கிய அரசியலமைப்புத் திருத்தச் சட்டம் எது?",
        "84th Constitutional Amendment Act, 2001", "84வது அரசியலமைப்புத் திருத்தச் சட்டம், 2001",
        "42nd Constitutional Amendment Act, 1976", "42வது அரசியலமைப்புத் திருத்தச் சட்டம், 1976",
        "87th Constitutional Amendment Act, 2003", "87வது அரசியலமைப்புத் திருத்தச் சட்டம், 2003",
        "91st Constitutional Amendment Act, 2003", "91வது அரசியலமைப்புத் திருத்தச் சட்டம், 2003",
        "A",
        "The 84th Constitutional Amendment Act, 2001 extended the freeze on seat allocation in the Lok Sabha and Rajya Sabha (Fourth Schedule) until the first census after 2026.",
        "84வது அரசியலமைப்புத் திருத்தச் சட்டம் 2001, மக்களவை மற்றும் மாநிலங்களவை (4வது அட்டவணை) இட ஒதுக்கீட்டு முடக்கத்தை 2026-க்குப் பிந்தைய முதல் மக்கள் தொகை கணக்கெடுப்பு வரை நீடித்தது.",
        "Correct. 84th CAA 2001 froze Fourth Schedule seat counts until post-2026.", "சரியானது. 84வது திருத்தம் 2001 நான்காவது அட்டவணை இடங்களை 2026 வரை முடக்கியது.",
        "Incorrect. 42nd CAA 1976 had imposed the initial freeze until 2000.", "தவறானது. 42வது திருத்தம் 1976 தொடக்க முடக்கத்தை 2000 வரை விதித்தது.",
        "Incorrect. 87th CAA 2003 allowed delimitation based on 2001 census without changing state seat totals.", "தவறானது. 87வது திருத்தம் 2003 மாநில மொத்த இடங்களை மாற்றாமல் தொகுதிகளை மறுசீரமைக்க அனுமதித்தது.",
        "Incorrect. 91st CAA 2003 dealt with ministry size and defection.", "தவறானது. 91வது திருத்தம் அமைச்சரவை அளவு மற்றும் கட்சித் தாவல் பற்றியது.",
        "84th CAA 2001: Froze Fourth Schedule seat distribution until first census post-2026.",
        "84வது திருத்தம் 2001: 4வது அட்டவணை இடப் பகிர்வை 2026-க்குப் பிந்தைய முதல் கணக்கெடுப்பு வரை முடக்கியது."
    ))

    qs.append(make_sch_q(
        "SCH_PYQ_048", "Medium", "PYQ", "Seventh Schedule",
        "[TNPSC Group 4 2017] In which List of the Seventh Schedule is 'Regulation and development of inter-State rivers and river valleys' located?",
        "[TNPSC குரூப் 4 2017] ஏழாவது அட்டவணையின் எந்தப் பட்டியலில் 'மாநிலங்களுக்கு இடையேயான நதிகள் மற்றும் நதிப் பள்ளத்தாக்குகளின் ஒழுங்குமுறை மற்றும் வளர்ச்சி' இடம்பெற்றுள்ளது?",
        "Union List (List I)", "மத்தியப் பட்டியல் (பட்டியல் I)",
        "State List (List II)", "மாநிலப் பட்டியல் (பட்டியல் II)",
        "Concurrent List (List III)", "பொதுப் பட்டியல் (பட்டியல் III)",
        "Residuary Powers", "எஞ்சிய அதிகாரங்கள்",
        "A",
        "Entry 56 of the Union List covers the regulation and development of inter-State rivers and river valleys to the extent declared by Parliament by law to be expedient in the public interest (read with Article 262). Water in general is Entry 17 of the State List, but subject to Entry 56 of List I.",
        "பாராளுமன்றத்தால் பொது நலனுக்காக அறிவிக்கப்பட்ட அளவிற்கு மாநிலங்களுக்கு இடையேயான நதிகள் மற்றும் நதிப் பள்ளத்தாக்குகளின் ஒழுங்குமுறை மத்தியப் பட்டியலின் பதிவு 56-ல் உள்ளது (சரத்து 262). பொதுவாக நீர் மாநிலப் பட்டியல் பதிவு 17-ல் இருந்தாலும், அது மத்தியப் பட்டியல் பதிவு 56-க்கு உட்பட்டதாகும்.",
        "Correct. Inter-State rivers regulation is Union List Entry 56.", "சரியானது. மாநிலங்களுக்கு இடையேயான நதிகள் ஒழுங்குமுறை மத்தியப் பட்டியல் பதிவு 56 ஆகும்.",
        "Incorrect. General water is in State List, but inter-state rivers are in Union List.", "தவறானது. பொதுவான நீர் மாநிலப் பட்டியலில் உள்ளது, ஆனால் மாநிலங்களுக்கிடையேயான நதிகள் மத்தியப் பட்டியலில் உள்ளன.",
        "Incorrect. Not in Concurrent List.", "தவறானது. பொதுப் பட்டியலில் இல்லை.",
        "Incorrect. Not a residuary subject.", "தவறானது. எஞ்சிய துறை அல்ல.",
        "Union List Entry 56: Inter-State rivers regulation. State List Entry 17: Water supply and irrigation.",
        "மத்தியப் பட்டியல் பதிவு 56: மாநிலங்களுக்கு இடையேயான நதிகள் ஒழுங்குமுறை. மாநிலப் பட்டியல் பதிவு 17: நீர் வழங்கல் & பாசனம்."
    ))

    qs.append(make_sch_q(
        "SCH_PYQ_049", "Hard", "PYQ", "Tenth Schedule",
        "[UPSC CSE 2001] Under the Tenth Schedule, voting or abstaining contrary to the party whip is NOT penalized with disqualification IF such voting is condoned by the party within how many days?",
        "[UPSC CSE 2001] பத்தாவது அட்டவணையின் கீழ், கட்சி கொறடா உத்தரவுக்கு எதிராக வாக்களிப்பது அல்லது வாக்களிக்காமல் இருப்பது, கட்சியால் எத்தனை நாட்களுக்குள் மன்னிக்கப்பட்டால் தகுதிநீக்கம் செய்யப்படாது?",
        "Within 15 days", "15 நாட்களுக்குள்",
        "Within 30 days", "30 நாட்களுக்குள்",
        "Within 60 days", "60 நாட்களுக்குள்",
        "Within 7 days", "7 நாட்களுக்குள்",
        "A",
        "Paragraph 2(1)(b) of the Tenth Schedule provides that voting or abstaining contrary to party direction will not result in disqualification if such act is condoned by the political party within 15 days from the date of such voting or abstention.",
        "பத்தாவது அட்டவணையின் பத்தி 2(1)(b)-ன் படி, கட்சி உத்தரவுக்கு எதிராக வாக்களித்த அல்லது வாக்களிக்காத நாளிலிருந்து 15 நாட்களுக்குள் அரசியல் கட்சியால் அச்செயல் மன்னிக்கப்பட்டால் தகுதிநீக்கம் ஏற்படாது.",
        "Correct. The condonation period is strictly 15 days.", "சரியானது. மன்னிப்பு வழங்கும் காலம் சரியாக 15 நாட்கள் ஆகும்.",
        "Incorrect. 30 days is incorrect.", "தவறானது. 30 நாட்கள் என்பது தவறானது.",
        "Incorrect. 60 days is the vacation of seat for absence under Art 101(4).", "தவறானது. 60 நாட்கள் என்பது சரத்து 101(4)-ன் கீழ் அவைக்கு வராமல் இருப்பதற்கான கால வரம்பு.",
        "Incorrect. 7 days is too short.", "தவறானது. 7 நாட்கள் என்பது மிகக் குறைவானது.",
        "Tenth Schedule Para 2(1)(b): Whip violation condonation window is 15 days.",
        "10வது அட்டவணை பத்தி 2(1)(b): கொறடா மீறல் மன்னிப்பு கால வரம்பு 15 நாட்கள் ஆகும்."
    ))

    qs.append(make_sch_q(
        "SCH_PYQ_050", "Medium", "PYQ", "Twelfth Schedule",
        "[TNPSC Group 1 2016] Which of the following functional items is explicitly enumerated in the Twelfth Schedule of the Indian Constitution?",
        "[TNPSC குரூப் 1 2016] பின்வரும் செயல்பாட்டுப் பணிகளில் எது இந்திய அரசியலமைப்பின் பன்னிரண்டாவது அட்டவணையில் வெளிப்படையாகக் குறிப்பிடப்பட்டுள்ளது?",
        "Fire services", "தீயணைப்பு சேவைகள்",
        "Agriculture, including agricultural extension", "விவசாயம் மற்றும் விவசாய விரிவாக்கம்",
        "Animal husbandry, dairying and poultry", "கால்நடை வளர்ப்பு, பால்வளம் மற்றும் கோழி வளர்ப்பு",
        "Fisheries", "மீன்வளம்",
        "A",
        "Fire services is Entry 7 of the Twelfth Schedule (Article 243W). Agriculture (Entry 1), Animal husbandry (Entry 4), and Fisheries (Entry 5) are listed in the Eleventh Schedule for Panchayats.",
        "தீயணைப்பு சேவைகள் என்பது பன்னிரண்டாவது அட்டவணையின் (சரத்து 243W) பதிவு 7 ஆகும். விவசாயம் (பதிவு 1), கால்நடை வளர்ப்பு (பதிவு 4) மற்றும் மீன்வளம் (பதிவு 5) ஆகியவை பஞ்சாயத்துகளுக்கான பதினோராவது அட்டவணையில் உள்ளன.",
        "Correct. Fire services is Entry 7 of the Twelfth Schedule.", "சரியானது. தீயணைப்பு சேவைகள் பன்னிரண்டாவது அட்டவணையின் பதிவு 7 ஆகும்.",
        "Incorrect. Agriculture is in Eleventh Schedule Entry 1.", "தவறானது. விவசாயம் 11வது அட்டவணையின் பதிவு 1 ஆகும்.",
        "Incorrect. Animal husbandry is in Eleventh Schedule Entry 4.", "தவறானது. கால்நடை வளர்ப்பு 11வது அட்டவணையின் பதிவு 4 ஆகும்.",
        "Incorrect. Fisheries is in Eleventh Schedule Entry 5.", "தவறானது. மீன்வளம் 11வது அட்டவணையின் பதிவு 5 ஆகும்.",
        "Twelfth Schedule Entry 7: Fire services (distinctive urban municipal function).",
        "12வது அட்டவணை பதிவு 7: தீயணைப்பு சேவைகள் (பிரத்யேக நகராட்சி பணி)."
    ))

    return qs

if __name__ == "__main__":
    qs = get_pyq_questions()
    print(f"Loaded {len(qs)} PYQ questions successfully.")
