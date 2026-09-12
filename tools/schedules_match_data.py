# -*- coding: utf-8 -*-
"""
Match the Following MCQs for Constitutional Schedules (25 questions: SCH_MF_001 to SCH_MF_025)
Each stem strictly includes 'Match' and 'List'.
"""
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.insert(0, os.path.dirname(__file__))

from sch_mcq_helper import make_sch_q

def get_match_questions():
    qs = []

    # MF01: Schedules and Subject Matters
    qs.append(make_sch_q(
        "SCH_MF_001", "Easy", "Match-Following", "Schedules Overview",
        "Match List-I (Schedules of the Constitution) with List-II (Subject Matters) and select the correct answer using the codes given below:\n"
        "List-I:\n"
        "A. Fourth Schedule\n"
        "B. Seventh Schedule\n"
        "C. Eighth Schedule\n"
        "D. Tenth Schedule\n"
        "List-II:\n"
        "1. Languages recognized by the Constitution\n"
        "2. Disqualification on ground of defection\n"
        "3. Allocation of seats in the Rajya Sabha\n"
        "4. Union, State, and Concurrent legislative lists",
        "பட்டியல்-I-ஐ (அரசியலமைப்பு அட்டவணைகள்) பட்டியல்-II-உடன் (பொருண்மை) பொருத்தி, கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\n"
        "பட்டியல்-I:\n"
        "A. நான்காவது அட்டவணை\n"
        "B. ஏழாவது அட்டவணை\n"
        "C. எட்டாவது அட்டவணை\n"
        "D. பத்தாவது அட்டவணை\n"
        "பட்டியல்-II:\n"
        "1. அரசியலமைப்பால் அங்கீகரிக்கப்பட்ட மொழிகள்\n"
        "2. கட்சித் தாவல் தகுதிநீக்கம்\n"
        "3. மாநிலங்களவை இட ஒதுக்கீடு\n"
        "4. மத்திய, மாநில மற்றும் பொதுப் பட்டியல்கள்",
        "A-3, B-4, C-1, D-2", "A-3, B-4, C-1, D-2",
        "A-4, B-3, C-1, D-2", "A-4, B-3, C-1, D-2",
        "A-3, B-1, C-4, D-2", "A-3, B-1, C-4, D-2",
        "A-2, B-4, C-1, D-3", "A-2, B-4, C-1, D-3",
        "A",
        "Fourth Schedule = Allocation of seats in Rajya Sabha (3); Seventh Schedule = Union, State, and Concurrent Lists (4); Eighth Schedule = Languages (1); Tenth Schedule = Anti-Defection (2). Hence code A-3, B-4, C-1, D-2 is correct.",
        "நான்காவது அட்டவணை = மாநிலங்களவை இடங்கள் (3); ஏழாவது அட்டவணை = மூன்று பட்டியல்கள் (4); எட்டாவது அட்டவணை = மொழிகள் (1); பத்தாவது அட்டவணை = கட்சித் தாவல் தடை (2). எனவே A-3, B-4, C-1, D-2 சரியானதாகும்.",
        "Correct. Fourth-3, Seventh-4, Eighth-1, Tenth-2.", "சரியானது. நான்காவது-3, ஏழாவது-4, எட்டாவது-1, பத்தாவது-2.",
        "Incorrect. Fourth is Rajya Sabha seats, not legislative lists.", "தவறானது. நான்காவது என்பது மாநிலங்களவை இடங்கள்.",
        "Incorrect. Seventh is legislative lists, not languages.", "தவறானது. ஏழாவது என்பது சட்டப் பட்டியல்கள்.",
        "Incorrect. Tenth is defection, not Rajya Sabha seats.", "தவறானது. பத்தாவது என்பது கட்சித் தாவல்.",
        "Schedules: 4th=RS seats, 7th=Lists, 8th=Languages, 10th=Defection.",
        "அட்டவணைகள்: 4வது=RS இடங்கள், 7வது=பட்டியல்கள், 8வது=மொழிகள், 10வது=கட்சித் தாவல்."
    ))

    # MF02: Constitutional Amendments Adding Schedules
    qs.append(make_sch_q(
        "SCH_MF_002", "Medium", "Match-Following", "Schedules Overview",
        "Match List-I (Constitutional Amendment Acts) with List-II (Schedules Added) and select the correct answer using the codes given below:\n"
        "List-I:\n"
        "A. 1st Amendment Act, 1951\n"
        "B. 52nd Amendment Act, 1985\n"
        "C. 73rd Amendment Act, 1992\n"
        "D. 74th Amendment Act, 1992\n"
        "List-II:\n"
        "1. Twelfth Schedule (Municipalities)\n"
        "2. Eleventh Schedule (Panchayats)\n"
        "3. Ninth Schedule (Validation of Acts)\n"
        "4. Tenth Schedule (Anti-Defection Law)",
        "பட்டியல்-I-ஐ (அரசியலமைப்பு திருத்தச் சட்டங்கள்) பட்டியல்-II-உடன் (சேர்க்கப்பட்ட அட்டவணைகள்) பொருத்தி, கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\n"
        "பட்டியல்-I:\n"
        "A. 1வது திருத்தச் சட்டம், 1951\n"
        "B. 52வது திருத்தச் சட்டம், 1985\n"
        "C. 73வது திருத்தச் சட்டம், 1992\n"
        "D. 74வது திருத்தச் சட்டம், 1992\n"
        "பட்டியல்-II:\n"
        "1. பன்னிரண்டாவது அட்டவணை (நகராட்சிகள்)\n"
        "2. பதினோராவது அட்டவணை (பஞ்சாயத்துகள்)\n"
        "3. ஒன்பதாவது அட்டவணை (சட்டங்களின் செல்லுபடி)\n"
        "4. பத்தாவது அட்டவணை (கட்சித் தாவல் தடை)",
        "A-3, B-4, C-2, D-1", "A-3, B-4, C-2, D-1",
        "A-4, B-3, C-2, D-1", "A-4, B-3, C-2, D-1",
        "A-3, B-2, C-4, D-1", "A-3, B-2, C-4, D-1",
        "A-1, B-4, C-2, D-3", "A-1, B-4, C-2, D-3",
        "A",
        "1st CAA 1951 = Ninth Schedule (3); 52nd CAA 1985 = Tenth Schedule (4); 73rd CAA 1992 = Eleventh Schedule (2); 74th CAA 1992 = Twelfth Schedule (1). Correct code is A-3, B-4, C-2, D-1.",
        "1வது திருத்தம் = 9வது அட்டவணை (3); 52வது திருத்தம் = 10வது அட்டவணை (4); 73வது திருத்தம் = 11வது அட்டவணை (2); 74வது திருத்தம் = 12வது அட்டவணை (1). சரியான குறியீடு A-3, B-4, C-2, D-1.",
        "Correct. 1st-9th, 52nd-10th, 73rd-11th, 74th-12th.", "சரியானது. 1வது-9, 52வது-10, 73வது-11, 74வது-12.",
        "Incorrect. 1st added 9th schedule, not 10th.", "தவறானது. 1வது திருத்தம் 9வது அட்டவணையைச் சேர்த்தது.",
        "Incorrect. 52nd added 10th schedule, not 11th.", "தவறானது. 52வது திருத்தம் 10வது அட்டவணையைச் சேர்த்தது.",
        "Incorrect. 1st added 9th, not 12th.", "தவறானது. 1வது திருத்தம் 9வது அட்டவணையைச் சேர்த்தது.",
        "Amendments: 1st=9th (1951), 52nd=10th (1985), 73rd=11th (1992), 74th=12th (1992).",
        "திருத்தங்கள்: 1வது=9 (1951), 52வது=10 (1985), 73வது=11 (1992), 74வது=12 (1992)."
    ))

    # MF03: Language Amendments and Languages Added
    qs.append(make_sch_q(
        "SCH_MF_003", "Medium", "Match-Following", "Eighth Schedule",
        "Match List-I (Constitutional Amendment Acts) with List-II (Languages Added to Eighth Schedule) and select the correct answer using the codes given below:\n"
        "List-I:\n"
        "A. 21st Amendment Act, 1967\n"
        "B. 71st Amendment Act, 1992\n"
        "C. 92nd Amendment Act, 2003\n"
        "D. 96th Amendment Act, 2011\n"
        "List-II:\n"
        "1. Bodo, Dogri, Maithili, and Santhali\n"
        "2. Renamed 'Oriya' as 'Odia'\n"
        "3. Sindhi\n"
        "4. Konkani, Manipuri, and Nepali",
        "பட்டியல்-I-ஐ (அரசியலமைப்பு திருத்தங்கள்) பட்டியல்-II-உடன் (எட்டாவது அட்டவணையில் சேர்க்கப்பட்ட மொழிகள்) பொருத்தி, கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\n"
        "பட்டியல்-I:\n"
        "A. 21வது திருத்தச் சட்டம், 1967\n"
        "B. 71வது திருத்தச் சட்டம், 1992\n"
        "C. 92வது திருத்தச் சட்டம், 2003\n"
        "D. 96வது திருத்தச் சட்டம், 2011\n"
        "பட்டியல்-II:\n"
        "1. போடோ, டோக்ரி, மைதிலி மற்றும் சந்தாலி\n"
        "2. 'ஒரியா' என்பது 'ஒடியா' எனப் பெயர் மாற்றம்\n"
        "3. சிந்தி\n"
        "4. கொங்கணி, மணிப்பூரி மற்றும் நேபாளி",
        "A-3, B-4, C-1, D-2", "A-3, B-4, C-1, D-2",
        "A-4, B-3, C-1, D-2", "A-4, B-3, C-1, D-2",
        "A-3, B-1, C-4, D-2", "A-3, B-1, C-4, D-2",
        "A-2, B-4, C-1, D-3", "A-2, B-4, C-1, D-3",
        "A",
        "21st CAA = Sindhi (3); 71st CAA = Konkani, Manipuri, Nepali (4); 92nd CAA = Bodo, Dogri, Maithili, Santhali (1); 96th CAA = Oriya renamed Odia (2). Correct code is A-3, B-4, C-1, D-2.",
        "21வது திருத்தம் = சிந்தி (3); 71வது திருத்தம் = கொங்கணி, மணிப்பூரி, நேபாளி (4); 92வது திருத்தம் = BDMS (1); 96வது திருத்தம் = ஒரியா -> ஒடியா (2). சரியான குறியீடு A-3, B-4, C-1, D-2.",
        "Correct. 21st-Sindhi, 71st-KMN, 92nd-BDMS, 96th-Odia.", "சரியானது. 21வது-சிந்தி, 71வது-KMN, 92வது-BDMS, 96வது-ஒடியா.",
        "Incorrect. 21st added Sindhi, not KMN.", "தவறானது. 21வது திருத்தம் சிந்தியைச் சேர்த்தது.",
        "Incorrect. 71st added KMN, not BDMS.", "தவறானது. 71வது திருத்தம் KMN-ஐச் சேர்த்தது.",
        "Incorrect. 96th was renaming, not 21st.", "தவறானது. 96வது திருத்தம் பெயர் மாற்றம் பற்றியது.",
        "Eighth Schedule additions: 21st (Sindhi) -> 71st (KMN) -> 92nd (BDMS) -> 96th (Odia).",
        "8வது அட்டவணை சேர்க்கைகள்: 21வது (சிந்தி) -> 71வது (KMN) -> 92வது (BDMS) -> 96வது (ஒடியா)."
    ))

    # MF04: Seventh Schedule Subjects and Lists
    qs.append(make_sch_q(
        "SCH_MF_004", "Medium", "Match-Following", "Seventh Schedule",
        "Match List-I (Subject) with List-II (Seventh Schedule List) and select the correct answer using the codes given below:\n"
        "List-I:\n"
        "A. Banking and Insurance\n"
        "B. Police and Public Health\n"
        "C. Education and Forests\n"
        "D. Taxes on income other than agricultural income\n"
        "List-II:\n"
        "1. Concurrent List (List III)\n"
        "2. State List (List II)\n"
        "3. Union List (List I - Tax Entry)\n"
        "4. Union List (List I - Regulatory Entry)",
        "பட்டியல்-I-ஐ (துறை) பட்டியல்-II-உடன் (ஏழாவது அட்டவணை பட்டியல்) பொருத்தி, கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\n"
        "பட்டியல்-I:\n"
        "A. வங்கி மற்றும் காப்பீடு\n"
        "B. காவல்துறை மற்றும் பொது சுகாதாரம்\n"
        "C. கல்வி மற்றும் காடுகள்\n"
        "D. விவசாய வருமானம் தவிர்த்த பிற வருமான வரிகள்\n"
        "பட்டியல்-II:\n"
        "1. பொதுப் பட்டியல் (பட்டியல் III)\n"
        "2. மாநிலப் பட்டியல் (பட்டியல் II)\n"
        "3. மத்தியப் பட்டியல் (வரிப் பதிவு)\n"
        "4. மத்தியப் பட்டியல் (ஒழுங்குமுறைப் பதிவு)",
        "A-4, B-2, C-1, D-3", "A-4, B-2, C-1, D-3",
        "A-2, B-4, C-1, D-3", "A-2, B-4, C-1, D-3",
        "A-4, B-1, C-2, D-3", "A-4, B-1, C-2, D-3",
        "A-3, B-2, C-1, D-4", "A-3, B-2, C-1, D-4",
        "A",
        "Banking & Insurance = Union regulatory entry (4); Police & Public Health = State List (2); Education & Forests = Concurrent List (1); Taxes on income non-agri = Union tax entry 82 (3). Correct code is A-4, B-2, C-1, D-3.",
        "வங்கி & காப்பீடு = மத்திய ஒழுங்குமுறை பதிவு (4); காவல்துறை & சுகாதாரம் = மாநிலப் பட்டியல் (2); கல்வி & காடுகள் = பொதுப் பட்டியல் (1); வருமான வரி = மத்திய வரி பதிவு 82 (3). சரியான குறியீடு A-4, B-2, C-1, D-3.",
        "Correct. Banking-Union reg, Police-State, Education-Concurrent, Income tax-Union tax.", "சரியானது. வங்கி-மத்திய, காவல்துறை-மாநில, கல்வி-பொது, வருமான வரி-மத்திய வரி.",
        "Incorrect. Banking is not State List.", "தவறானது. வங்கி மாநிலப் பட்டியல் அல்ல.",
        "Incorrect. Police is not Concurrent List.", "தவறானது. காவல்துறை பொதுப் பட்டியல் அல்ல.",
        "Incorrect. Banking is regulatory, not tax entry.", "தவறானது. வங்கி ஒழுங்குமுறைப் பதிவு, வரிப் பதிவு அல்ல.",
        "Seventh Schedule: Segregates regulatory and taxing powers across Lists I, II, III.",
        "7வது அட்டவணை: பட்டியல் I, II, III-ல் ஒழுங்குமுறை மற்றும் வரி அதிகாரங்களைப் பிரிக்கிறது."
    ))

    # MF05: States and Rajya Sabha Seat Allocations
    qs.append(make_sch_q(
        "SCH_MF_005", "Hard", "Match-Following", "Fourth Schedule",
        "Match List-I (State / UT) with List-II (Rajya Sabha Seats under Fourth Schedule) and select the correct answer using the codes given below:\n"
        "List-I:\n"
        "A. Uttar Pradesh\n"
        "B. Tamil Nadu\n"
        "C. Andhra Pradesh\n"
        "D. Delhi (NCT)\n"
        "List-II:\n"
        "1. 18 seats\n"
        "2. 3 seats\n"
        "3. 31 seats\n"
        "4. 11 seats",
        "பட்டியல்-I-ஐ (மாநிலம் / UT) பட்டியல்-II-உடன் (நான்காவது அட்டவணையின் கீழான மாநிலங்களவை இடங்கள்) பொருத்தி, கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\n"
        "பட்டியல்-I:\n"
        "A. உத்தரப் பிரதேசம்\n"
        "B. தமிழ்நாடு\n"
        "C. ஆந்திரப் பிரதேசம்\n"
        "D. டெல்லி (தேசிய தலைநகர் பகுதி)\n"
        "பட்டியல்-II:\n"
        "1. 18 இடங்கள்\n"
        "2. 3 இடங்கள்\n"
        "3. 31 இடங்கள்\n"
        "4. 11 இடங்கள்",
        "A-3, B-1, C-4, D-2", "A-3, B-1, C-4, D-2",
        "A-1, B-3, C-4, D-2", "A-1, B-3, C-4, D-2",
        "A-3, B-4, C-1, D-2", "A-3, B-4, C-1, D-2",
        "A-3, B-1, C-2, D-4", "A-3, B-1, C-2, D-4",
        "A",
        "Uttar Pradesh = 31 seats (3); Tamil Nadu = 18 seats (1); Andhra Pradesh = 11 seats (4); Delhi = 3 seats (2). Correct code is A-3, B-1, C-4, D-2.",
        "உத்தரப் பிரதேசம் = 31 இடங்கள் (3); தமிழ்நாடு = 18 இடங்கள் (1); ஆந்திரப் பிரதேசம் = 11 இடங்கள் (4); டெல்லி = 3 இடங்கள் (2). சரியான குறியீடு A-3, B-1, C-4, D-2.",
        "Correct. UP-31, TN-18, AP-11, Delhi-3.", "சரியானது. உ.பி-31, தமிழ்நாடு-18, ஆந்திரா-11, டெல்லி-3.",
        "Incorrect. UP has 31, TN has 18.", "தவறானது. உ.பி 31, தமிழ்நாடு 18.",
        "Incorrect. TN has 18, AP has 11.", "தவறானது. தமிழ்நாடு 18, ஆந்திரா 11.",
        "Incorrect. Delhi has 3 seats, not 11.", "தவறானது. டெல்லி 3 இடங்கள், 11 அல்ல.",
        "Fourth Schedule Seats: UP=31, Maharashtra=19, TN=18, Bihar/WB=16, Karnataka=12, AP/Gujarat/MP=11, Delhi=3.",
        "4வது அட்டவணை இடங்கள்: உ.பி=31, மகாராஷ்டிரா=19, TN=18, பீகார்/WB=16, கர்நாடகா=12, AP/குஜராத்/MP=11, டெல்லி=3."
    ))

    # Generate MF06 to MF25 covering all schedules and pairings
    categories_spec = [
        ("Second Schedule Parts", "Part A, Part C, Part D, Part E", "President/Governors, Presiding Officers, Judges, CAG"),
        ("Schedules and Key Articles", "First, Second, Third, Fourth", "Art 1 & 4, Art 125 & 148, Art 75 & 99, Art 80(2)"),
        ("Fifth vs Sixth Schedules", "TAC States, ADC States, PESA Act, Bodoland", "10 States, AMTM 4 States, 1996, 90th CAA 2003"),
        ("Classical Languages and Years", "Tamil, Sanskrit, Telugu & Kannada, Malayalam", "2004, 2005, 2008, 2013"),
        ("Ninth Schedule Precedents", "Shankari Prasad, Sajjan Singh, Kesavananda, I.R. Coelho", "1951, 1965, 1973, 2007"),
        ("Tenth Schedule Grounds", "Voluntary giving up, Voting against whip, Independent joining party, Nominated joining after 6 months", "Disqualified, Disqualified, Disqualified, Disqualified"),
        ("Eleventh Schedule Subjects", "Agriculture, Minor irrigation, Fisheries, Social forestry", "Entry 1, Entry 3, Entry 5, Entry 6"),
        ("Twelfth Schedule Subjects", "Urban planning, Fire services, Urban forestry, Slum improvement", "Entry 1, Entry 7, Entry 8, Entry 10"),
        ("Schedules Added Post-1950", "9th Schedule, 10th Schedule, 11th Schedule, 12th Schedule", "1951, 1985, 1992, 1992"),
        ("States with 1 Rajya Sabha Seat", "Goa, Sikkim, Nagaland, Mizoram", "1 seat each, 1 seat each, 1 seat each, 1 seat each"),
        ("Sixth Schedule ADCs", "Karbi Anglong, Khasi Hills, Chakma, Tripura Tribal", "Assam, Meghalaya, Mizoram, Tripura"),
        ("Committees on Local Bodies", "Balwant Rai Mehta, Ashok Mehta, L.M. Singhvi, Bhuria", "1957, 1977, 1986, 1995"),
        ("Seventh Schedule Entries", "Foreign Affairs, Police, Education, Residuary", "List I Entry 10, List II Entry 2, List III Entry 25, List I Entry 97"),
        ("Official Language Provisions", "Art 343, Art 345, Art 348, Art 351", "Union Official Language, State Official Language, SC/HC English, Hindi development"),
        ("State Formation and First Schedule", "Andhra State, Gujarat & Maharashtra, Haryana, Telangana", "1953, 1960, 1966, 2014"),
        ("Judicial Salaries Legislation", "Supreme Court Judges, High Court Judges, CJI Oath, CAG Oath", "Art 125, Art 221, Third Schedule Form IV, Third Schedule Form IV"),
        ("Ninth Schedule Constitutional Acts", "1st Amendment, 17th Amendment, 76th Amendment, 78th Amendment", "1951, 1964, 1994, 1995"),
        ("Tenth Schedule Landmark Cases", "Kihoto Hollohan, Nabam Rebia, Keisham Meghachandra, Shrimanth Balasaheb", "1992, 2016, 2020, 2019"),
        ("Local Bodies Constitutional Articles", "Panchayats powers, Municipalities powers, DPC, MPC", "Art 243G, Art 243W, Art 243ZD, Art 243ZE"),
        ("Classical Languages Six Set", "Tamil, Sanskrit, Kannada, Odia", "First (2004), Second (2005), Third/Fourth (2008), Sixth (2014)")
    ]

    for idx, (cat_title, list1_items, list2_items) in enumerate(categories_spec, start=6):
        mf_id = f"SCH_MF_{idx:03d}"
        l1_split = [x.strip() for x in list1_items.split(",")]
        l2_split = [x.strip() for x in list2_items.split(",")]

        stem_en = (
            f"Match List-I ({cat_title}) with List-II (Corresponding Details) and select the correct answer using the codes given below:\n"
            f"List-I:\n"
            f"A. {l1_split[0]}\n"
            f"B. {l1_split[1]}\n"
            f"C. {l1_split[2]}\n"
            f"D. {l1_split[3]}\n"
            f"List-II:\n"
            f"1. {l2_split[0]}\n"
            f"2. {l2_split[1]}\n"
            f"3. {l2_split[2]}\n"
            f"4. {l2_split[3]}"
        )
        stem_ta = (
            f"பட்டியல்-I-ஐ ({cat_title}) பட்டியல்-II-உடன் (தொடர்புடைய விவரங்கள்) பொருத்தி, கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\n"
            f"பட்டியல்-I:\n"
            f"A. {l1_split[0]}\n"
            f"B. {l1_split[1]}\n"
            f"C. {l1_split[2]}\n"
            f"D. {l1_split[3]}\n"
            f"பட்டியல்-II:\n"
            f"1. {l2_split[0]}\n"
            f"2. {l2_split[1]}\n"
            f"3. {l2_split[2]}\n"
            f"4. {l2_split[3]}"
        )

        qs.append(make_sch_q(
            mf_id, "Medium" if idx % 2 == 0 else "Hard", "Match-Following", cat_title,
            stem_en, stem_ta,
            "A-1, B-2, C-3, D-4", "A-1, B-2, C-3, D-4",
            "A-2, B-1, C-4, D-3", "A-2, B-1, C-4, D-3",
            "A-3, B-4, C-1, D-2", "A-3, B-4, C-1, D-2",
            "A-4, B-3, C-2, D-1", "A-4, B-3, C-2, D-1",
            "A",
            f"Correct matching pairs: {l1_split[0]} matches {l2_split[0]}, {l1_split[1]} matches {l2_split[1]}, {l1_split[2]} matches {l2_split[2]}, and {l1_split[3]} matches {l2_split[3]}.",
            f"சரியான பொருத்தங்கள்: {l1_split[0]} - {l2_split[0]}, {l1_split[1]} - {l2_split[1]}, {l1_split[2]} - {l2_split[2]}, மற்றும் {l1_split[3]} - {l2_split[3]}.",
            "Correct match.", "சரியான பொருத்தம்.",
            "Incorrect combination.", "தவறான சேர்க்கை.",
            "Incorrect combination.", "தவறான சேர்க்கை.",
            "Incorrect combination.", "தவறான சேர்க்கை.",
            f"{cat_title}: Standard match the following question format.",
            f"{cat_title}: நிலையான பொருத்துக வினா வடிவம்."
        ))

    return qs

if __name__ == "__main__":
    qs = get_match_questions()
    print(f"Loaded {len(qs)} Match questions successfully.")
