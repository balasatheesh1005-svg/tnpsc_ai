# -*- coding: utf-8 -*-
"""
Chronology MCQs for Constitutional Schedules (25 questions: SCH_C_001 to SCH_C_025)
Strictly adheres to the CRITICAL CHRONOLOGY RULE:
- Events in stem are presented in non-chronological order.
- Correct sequence is NEVER 1-2-3-4.
- 4 options are distinct, valid permutations of [1, 2, 3, 4].
- Explanations explicitly teach chronology with dates/years and arrow sequences (-> or →).
"""
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.insert(0, os.path.dirname(__file__))

from sch_mcq_helper import make_sch_q

def get_chronology_questions():
    qs = []

    # C01: Eighth Schedule Languages Addition
    qs.append(make_sch_q(
        "SCH_C_001", "Medium", "Chronology", "Eighth Schedule",
        "Arrange the following language inclusions/modifications in the Eighth Schedule in chronological order:\n"
        "1. Inclusion of Konkani, Manipuri, and Nepali\n"
        "2. Inclusion of Sindhi\n"
        "3. Renaming of 'Oriya' as 'Odia'\n"
        "4. Inclusion of Bodo, Dogri, Maithili, and Santhali",
        "எட்டாவது அட்டவணையில் பின்வரும் மொழிகள் சேர்க்கப்பட்ட/மாற்றப்பட்ட நிகழ்வுகளை காலவரிசைப்படி வரிசைப்படுத்துக:\n"
        "1. கொங்கணி, மணிப்பூரி மற்றும் நேபாளி மொழிகள் சேர்க்கப்பட்டது\n"
        "2. சிந்தி மொழி சேர்க்கப்பட்டது\n"
        "3. 'ஒரியா' என்பது 'ஒடியா' என பெயர் மாற்றம் செய்யப்பட்டது\n"
        "4. போடோ, டோக்ரி, மைதிலி மற்றும் சந்தாலி மொழிகள் சேர்க்கப்பட்டது",
        "2 - 1 - 4 - 3", "2 - 1 - 4 - 3",
        "1 - 2 - 4 - 3", "1 - 2 - 4 - 3",
        "2 - 4 - 1 - 3", "2 - 4 - 1 - 3",
        "3 - 2 - 1 - 4", "3 - 2 - 1 - 4",
        "A",
        "The chronological sequence of Eighth Schedule modifications is:\n"
        "- Sindhi: 21st CAA, 1967 (2)\n"
        "- Konkani, Manipuri, Nepali: 71st CAA, 1992 (1)\n"
        "- Bodo, Dogri, Maithili, Santhali: 92nd CAA, 2003 (4)\n"
        "- Oriya renamed to Odia: 96th CAA, 2011 (3)\n"
        "Chronological order: 2 (1967) -> 1 (1992) -> 4 (2003) -> 3 (2011).",
        "எட்டாவது அட்டவணை மாற்றங்களின் காலவரிசை:\n"
        "- சிந்தி: 21வது திருத்தம், 1967 (2)\n"
        "- கொங்கணி, மணிப்பூரி, நேபாளி: 71வது திருத்தம், 1992 (1)\n"
        "- போடோ, டோக்ரி, மைதிலி, சந்தாலி: 92வது திருத்தம், 2003 (4)\n"
        "- ஒரியா -> ஒடியா மாற்றம்: 96வது திருத்தம், 2011 (3)\n"
        "காலவரிசை: 2 (1967) -> 1 (1992) -> 4 (2003) -> 3 (2011).",
        "Correct. 1967 -> 1992 -> 2003 -> 2011.", "சரியானது. 1967 -> 1992 -> 2003 -> 2011.",
        "Incorrect sequence.", "தவறான வரிசை.",
        "Incorrect sequence.", "தவறான வரிசை.",
        "Incorrect sequence.", "தவறான வரிசை.",
        "Eighth Schedule Timeline: 1967 (Sindhi) -> 1992 (KMN) -> 2003 (BDMS) -> 2011 (Odia).",
        "8வது அட்டவணை காலவரிசை: 1967 (சிந்தி) -> 1992 (KMN) -> 2003 (BDMS) -> 2011 (ஒடியா)."
    ))

    # C02: Amendments Adding Schedules
    qs.append(make_sch_q(
        "SCH_C_002", "Hard", "Chronology", "Schedules Overview",
        "Arrange the following Constitutional Amendment Acts relating to Schedules in chronological order:\n"
        "1. 52nd Amendment Act (inserted Tenth Schedule)\n"
        "2. 1st Amendment Act (inserted Ninth Schedule)\n"
        "3. 73rd Amendment Act (inserted Eleventh Schedule)\n"
        "4. 35th Amendment Act (inserted original Tenth Schedule for Sikkim)",
        "அட்டவணைகள் தொடர்பான பின்வரும் அரசியலமைப்பு திருத்தச் சட்டங்களை காலவரிசைப்படி வரிசைப்படுத்துக:\n"
        "1. 52வது திருத்தச் சட்டம் (பத்தாவது அட்டவணையைச் சேர்த்தது)\n"
        "2. 1வது திருத்தச் சட்டம் (ஒன்பதாவது அட்டவணையைச் சேர்த்தது)\n"
        "3. 73வது திருத்தச் சட்டம் (பதினோராவது அட்டவணையைச் சேர்த்தது)\n"
        "4. 35வது திருத்தச் சட்டம் (சிக்கிமுக்காக அசல் பத்தாவது அட்டவணையைச் சேர்த்தது)",
        "2 - 4 - 1 - 3", "2 - 4 - 1 - 3",
        "2 - 1 - 4 - 3", "2 - 1 - 4 - 3",
        "4 - 2 - 1 - 3", "4 - 2 - 1 - 3",
        "1 - 2 - 4 - 3", "1 - 2 - 4 - 3",
        "A",
        "The chronological sequence of amendments is:\n"
        "- 1st Amendment Act: 1951 (2)\n"
        "- 35th Amendment Act: 1974 (4)\n"
        "- 52nd Amendment Act: 1985 (1)\n"
        "- 73rd Amendment Act: 1992 (3)\n"
        "Chronological order: 2 (1951) -> 4 (1974) -> 1 (1985) -> 3 (1992).",
        "திருத்தச் சட்டங்களின் காலவரிசை:\n"
        "- 1வது திருத்தச் சட்டம்: 1951 (2)\n"
        "- 35வது திருத்தச் சட்டம்: 1974 (4)\n"
        "- 52வது திருத்தச் சட்டம்: 1985 (1)\n"
        "- 73வது திருத்தச் சட்டம்: 1992 (3)\n"
        "காலவரிசை: 2 (1951) -> 4 (1974) -> 1 (1985) -> 3 (1992).",
        "Correct. 1951 -> 1974 -> 1985 -> 1992.", "சரியானது. 1951 -> 1974 -> 1985 -> 1992.",
        "Incorrect sequence.", "தவறான வரிசை.",
        "Incorrect sequence.", "தவறான வரிசை.",
        "Incorrect sequence.", "தவறான வரிசை.",
        "Amendments Timeline: 1st (1951) -> 35th (1974) -> 52nd (1985) -> 73rd (1992).",
        "திருத்தங்கள் காலவரிசை: 1வது (1951) -> 35வது (1974) -> 52வது (1985) -> 73வது (1992)."
    ))

    # C03: Landmark Supreme Court Judgments on Ninth Schedule
    qs.append(make_sch_q(
        "SCH_C_003", "Hard", "Chronology", "Ninth Schedule",
        "Arrange the following landmark Supreme Court judgments regarding the Ninth Schedule and fundamental rights in chronological order:\n"
        "1. I.R. Coelho v. State of Tamil Nadu\n"
        "2. Shankari Prasad v. Union of India\n"
        "3. Kesavananda Bharati v. State of Kerala\n"
        "4. Sajjan Singh v. State of Rajasthan",
        "ஒன்பதாவது அட்டவணை மற்றும் அடிப்படை உரிமைகள் தொடர்பான பின்வரும் உச்சநீதிமன்ற முக்கிய தீர்ப்புகளை காலவரிசைப்படி வரிசைப்படுத்துக:\n"
        "1. ஐ.ஆர். கோயல்ஹோ எதிர் தமிழ்நாடு அரசு\n"
        "2. சங்கரி பிரசாத் எதிர் இந்திய யூனியன்\n"
        "3. கேசவானந்த பாரதி எதிர் கேரள அரசு\n"
        "4. சஜ்ஜன் சிங் எதிர் ராஜஸ்தான் அரசு",
        "2 - 4 - 3 - 1", "2 - 4 - 3 - 1",
        "2 - 3 - 4 - 1", "2 - 3 - 4 - 1",
        "4 - 2 - 3 - 1", "4 - 2 - 3 - 1",
        "1 - 2 - 3 - 4", "1 - 2 - 3 - 4",
        "A",
        "The chronological sequence of landmark judicial decisions is:\n"
        "- Shankari Prasad v. Union of India: 1951 (2)\n"
        "- Sajjan Singh v. State of Rajasthan: 1965 (4)\n"
        "- Kesavananda Bharati v. State of Kerala: 1973 (3)\n"
        "- I.R. Coelho v. State of Tamil Nadu: 2007 (1)\n"
        "Chronological order: 2 (1951) -> 4 (1965) -> 3 (1973) -> 1 (2007).",
        "முக்கிய நீதித்துறை தீர்ப்புகளின் காலவரிசை:\n"
        "- சங்கரி பிரசாத் வழக்கு: 1951 (2)\n"
        "- சஜ்ஜன் சிங் வழக்கு: 1965 (4)\n"
        "- கேசவானந்த பாரதி வழக்கு: 1973 (3)\n"
        "- ஐ.ஆர். கோயல்ஹோ வழக்கு: 2007 (1)\n"
        "காலவரிசை: 2 (1951) -> 4 (1965) -> 3 (1973) -> 1 (2007).",
        "Correct. 1951 -> 1965 -> 1973 -> 2007.", "சரியானது. 1951 -> 1965 -> 1973 -> 2007.",
        "Incorrect sequence.", "தவறான வரிசை.",
        "Incorrect sequence.", "தவறான வரிசை.",
        "Incorrect sequence.", "தவறான வரிசை.",
        "Judicial Evolution: Shankari Prasad (1951) -> Sajjan Singh (1965) -> Kesavananda (1973) -> Coelho (2007).",
        "நீதித்துறை வளர்ச்சி: சங்கரி பிரசாத் (1951) -> சஜ்ஜன் சிங் (1965) -> கேசவானந்தா (1973) -> கோயல்ஹோ (2007)."
    ))

    # C04: Classical Languages Declaration
    qs.append(make_sch_q(
        "SCH_C_004", "Medium", "Chronology", "Eighth Schedule",
        "Arrange the following languages in the chronological order in which they were declared as 'Classical Languages' (செம்மொழி):\n"
        "1. Telugu and Kannada\n"
        "2. Tamil\n"
        "3. Odia\n"
        "4. Sanskrit",
        "பின்வரும் மொழிகள் 'செம்மொழி'யாக அறிவிக்கப்பட்ட காலவரிசைப்படி அவற்றை வரிசைப்படுத்துக:\n"
        "1. தெலுங்கு மற்றும் கன்னடம்\n"
        "2. தமிழ்\n"
        "3. ஒடியா\n"
        "4. சமஸ்கிருதம்",
        "2 - 4 - 1 - 3", "2 - 4 - 1 - 3",
        "2 - 1 - 4 - 3", "2 - 1 - 4 - 3",
        "4 - 2 - 1 - 3", "4 - 2 - 1 - 3",
        "1 - 2 - 4 - 3", "1 - 2 - 4 - 3",
        "A",
        "The chronological declaration of Classical Languages is:\n"
        "- Tamil: 2004 (2)\n"
        "- Sanskrit: 2005 (4)\n"
        "- Telugu and Kannada: 2008 (1)\n"
        "- Odia: 2014 (3)\n"
        "Chronological order: 2 (2004) -> 4 (2005) -> 1 (2008) -> 3 (2014).",
        "செம்மொழிகள் அறிவிக்கப்பட்ட காலவரிசை:\n"
        "- தமிழ்: 2004 (2)\n"
        "- சமஸ்கிருதம்: 2005 (4)\n"
        "- தெலுங்கு மற்றும் கன்னடம்: 2008 (1)\n"
        "- ஒடியா: 2014 (3)\n"
        "காலவரிசை: 2 (2004) -> 4 (2005) -> 1 (2008) -> 3 (2014).",
        "Correct. 2004 -> 2005 -> 2008 -> 2014.", "சரியானது. 2004 -> 2005 -> 2008 -> 2014.",
        "Incorrect sequence.", "தவறான வரிசை.",
        "Incorrect sequence.", "தவறான வரிசை.",
        "Incorrect sequence.", "தவறான வரிசை.",
        "Classical Languages: Tamil (2004) -> Sanskrit (2005) -> Telugu/Kannada (2008) -> Malayalam (2013) -> Odia (2014).",
        "செம்மொழிகள்: தமிழ் (2004) -> சமஸ்கிருதம் (2005) -> தெலுங்கு/கன்னடம் (2008) -> மலையாளம் (2013) -> ஒடியா (2014)."
    ))

    # C05: Tenth Schedule Landmark Cases
    qs.append(make_sch_q(
        "SCH_C_005", "Hard", "Chronology", "Tenth Schedule",
        "Arrange the following landmark Supreme Court judgments concerning the Tenth Schedule in chronological order:\n"
        "1. Keisham Meghachandra Singh v. Hon'ble Speaker, Manipur\n"
        "2. Kihoto Hollohan v. Zachillhu\n"
        "3. Nabam Rebia v. Deputy Speaker, Arunachal Pradesh\n"
        "4. Shrimanth Balasaheb Patil v. Speaker, Karnataka",
        "பத்தாவது அட்டவணை தொடர்பான பின்வரும் உச்சநீதிமன்ற வரலாற்று முக்கியத்துவம் வாய்ந்த தீர்ப்புகளை காலவரிசைப்படி வரிசைப்படுத்துக:\n"
        "1. கீஷம் மேகச்சந்திர சிங் எதிர் மணிப்பூர் சட்டமன்ற சபாநாயகர்\n"
        "2. கிகோட்டோ ஹோலோஹான் எதிர் சாச்சிலு\n"
        "3. நபம் ரெபியா எதிர் அருணாச்சலப் பிரதேச துணை சபாநாயகர்\n"
        "4. ஸ்ரீமந்த் பாலசாகேப் பாட்டீல் எதிர் கர்நாடக சபாநாயகர்",
        "2 - 3 - 4 - 1", "2 - 3 - 4 - 1",
        "2 - 4 - 3 - 1", "2 - 4 - 3 - 1",
        "3 - 2 - 4 - 1", "3 - 2 - 4 - 1",
        "1 - 2 - 3 - 4", "1 - 2 - 3 - 4",
        "A",
        "The chronological sequence of Tenth Schedule jurisprudence is:\n"
        "- Kihoto Hollohan v. Zachillhu: 1992 (2)\n"
        "- Nabam Rebia v. Deputy Speaker: 2016 (3)\n"
        "- Shrimanth Balasaheb Patil v. Speaker: 2019 (4)\n"
        "- Keisham Meghachandra Singh v. Speaker: 2020 (1)\n"
        "Chronological order: 2 (1992) -> 3 (2016) -> 4 (2019) -> 1 (2020).",
        "பத்தாவது அட்டவணை தீர்ப்புகளின் காலவரிசை:\n"
        "- கிகோட்டோ ஹோலோஹான் வழக்கு: 1992 (2)\n"
        "- நபம் ரெபியா வழக்கு: 2016 (3)\n"
        "- ஸ்ரீமந்த் பாலசாகேப் பாட்டீல் வழக்கு: 2019 (4)\n"
        "- கீஷம் மேகச்சந்திர சிங் வழக்கு: 2020 (1)\n"
        "காலவரிசை: 2 (1992) -> 3 (2016) -> 4 (2019) -> 1 (2020).",
        "Correct. 1992 -> 2016 -> 2019 -> 2020.", "சரியானது. 1992 -> 2016 -> 2019 -> 2020.",
        "Incorrect sequence.", "தவறான வரிசை.",
        "Incorrect sequence.", "தவறான வரிசை.",
        "Incorrect sequence.", "தவறான வரிசை.",
        "Anti-Defection Jurisprudence: 1992 (Kihoto) -> 2016 (Nabam Rebia) -> 2019 (Shrimanth) -> 2020 (Keisham).",
        "கட்சித் தாவல் தீர்ப்புகள்: 1992 (கிகோட்டோ) -> 2016 (நபம் ரெபியா) -> 2019 (ஸ்ரீமந்த்) -> 2020 (கீஷம்)."
    ))

    # C06: Formation of States altering First Schedule
    qs.append(make_sch_q(
        "SCH_C_006", "Medium", "Chronology", "First Schedule",
        "Arrange the formation of the following States (which amended the First Schedule) in chronological order:\n"
        "1. Haryana\n"
        "2. Andhra State\n"
        "3. Telangana\n"
        "4. Gujarat",
        "முதல் அட்டவணையைத் திருத்திய பின்வரும் மாநிலங்கள் உருவாக்கப்பட்ட நிகழ்வுகளை காலவரிசைப்படி வரிசைப்படுத்துக:\n"
        "1. ஹரியானா\n"
        "2. ஆந்திர மாநிலம்\n"
        "3. தெலங்கானா\n"
        "4. குஜராத்",
        "2 - 4 - 1 - 3", "2 - 4 - 1 - 3",
        "2 - 1 - 4 - 3", "2 - 1 - 4 - 3",
        "4 - 2 - 1 - 3", "4 - 2 - 1 - 3",
        "1 - 2 - 4 - 3", "1 - 2 - 4 - 3",
        "A",
        "The chronological order of state formation is:\n"
        "- Andhra State: 1953 (2)\n"
        "- Gujarat: 1960 (4)\n"
        "- Haryana: 1966 (1)\n"
        "- Telangana: 2014 (3)\n"
        "Chronological order: 2 (1953) -> 4 (1960) -> 1 (1966) -> 3 (2014).",
        "மாநிலங்கள் உருவாக்கப்பட்ட காலவரிசை:\n"
        "- ஆந்திர மாநிலம்: 1953 (2)\n"
        "- குஜராத்: 1960 (4)\n"
        "- ஹரியானா: 1966 (1)\n"
        "- தெலங்கானா: 2014 (3)\n"
        "காலவரிசை: 2 (1953) -> 4 (1960) -> 1 (1966) -> 3 (2014).",
        "Correct. 1953 -> 1960 -> 1966 -> 2014.", "சரியானது. 1953 -> 1960 -> 1966 -> 2014.",
        "Incorrect sequence.", "தவறான வரிசை.",
        "Incorrect sequence.", "தவறான வரிசை.",
        "Incorrect sequence.", "தவறான வரிசை.",
        "First Schedule State Timeline: Andhra (1953) -> Gujarat (1960) -> Haryana (1966) -> Telangana (2014).",
        "முதல் அட்டவணை மாநில காலவரிசை: ஆந்திரா (1953) -> குஜராத் (1960) -> ஹரியானா (1966) -> தெலங்கானா (2014)."
    ))

    # C07: Committees on Panchayati Raj and Tribal Areas
    qs.append(make_sch_q(
        "SCH_C_007", "Medium", "Chronology", "Eleventh Schedule",
        "Arrange the appointment/submission of the following major Committees relating to Local Self-Government and Tribal Schedules in chronological order:\n"
        "1. Dileep Singh Bhuria Committee\n"
        "2. Balwant Rai Mehta Committee\n"
        "3. L.M. Singhvi Committee\n"
        "4. Ashok Mehta Committee",
        "உள்ளாட்சி அமைப்புகள் மற்றும் பழங்குடி அட்டவணைகள் தொடர்பான பின்வரும் முக்கிய குழுக்கள் அமைக்கப்பட்ட நிகழ்வுகளை காலவரிசைப்படி வரிசைப்படுத்துக:\n"
        "1. திலீப் சிங் பூரியா குழு\n"
        "2. பல்வந்த் ராய் மேத்தா குழு\n"
        "3. எல்.எம். சிங்வி குழு\n"
        "4. அசோக் மேத்தா குழு",
        "2 - 4 - 3 - 1", "2 - 4 - 3 - 1",
        "2 - 3 - 4 - 1", "2 - 3 - 4 - 1",
        "4 - 2 - 3 - 1", "4 - 2 - 3 - 1",
        "1 - 2 - 4 - 3", "1 - 2 - 4 - 3",
        "A",
        "The chronological order of committees is:\n"
        "- Balwant Rai Mehta Committee: 1957 (2)\n"
        "- Ashok Mehta Committee: 1977 (4)\n"
        "- L.M. Singhvi Committee: 1986 (3)\n"
        "- Dileep Singh Bhuria Committee: 1995 (1)\n"
        "Chronological order: 2 (1957) -> 4 (1977) -> 3 (1986) -> 1 (1995).",
        "குழுக்களின் காலவரிசை:\n"
        "- பல்வந்த் ராய் மேத்தா குழு: 1957 (2)\n"
        "- அசோக் மேத்தா குழு: 1977 (4)\n"
        "- எல்.எம். சிங்வி குழு: 1986 (3)\n"
        "- திலீப் சிங் பூரியா குழு: 1995 (1)\n"
        "காலவரிசை: 2 (1957) -> 4 (1977) -> 3 (1986) -> 1 (1995).",
        "Correct. 1957 -> 1977 -> 1986 -> 1995.", "சரியானது. 1957 -> 1977 -> 1986 -> 1995.",
        "Incorrect sequence.", "தவறான வரிசை.",
        "Incorrect sequence.", "தவறான வரிசை.",
        "Incorrect sequence.", "தவறான வரிசை.",
        "Committees: Balwant Rai (1957) -> Ashok Mehta (1977) -> LM Singhvi (1986) -> Bhuria (1995).",
        "குழுக்கள்: பல்வந்த் ராய் (1957) -> அசோக் மேத்தா (1977) -> எல்.எம். சிங்வி (1986) -> பூரியா (1995)."
    ))

    # C08: Seventh Schedule Centre-State Milestones
    qs.append(make_sch_q(
        "SCH_C_008", "Hard", "Chronology", "Seventh Schedule",
        "Arrange the following Centre-State relations milestones relating to the Seventh Schedule in chronological order:\n"
        "1. Punchhi Commission submitted its report\n"
        "2. 42nd Amendment transferred 5 subjects to Concurrent List\n"
        "3. Sarkaria Commission submitted its report\n"
        "4. Rajamannar Committee submitted its report in Tamil Nadu",
        "ஏழாவது அட்டவணை தொடர்பான மத்திய-மாநில உறவுகளின் பின்வரும் முக்கிய நிகழ்வுகளை காலவரிசைப்படி வரிசைப்படுத்துக:\n"
        "1. பூஞ்சி ஆணையம் தனது அறிக்கையை சமர்ப்பித்தது\n"
        "2. 42வது திருத்தம் 5 துறைகளைப் பொதுப் பட்டியலுக்கு மாற்றியது\n"
        "3. சர்க்காரியா ஆணையம் தனது அறிக்கையை சமர்ப்பித்தது\n"
        "4. தமிழ்நாட்டில் ராஜமன்னார் குழு தனது அறிக்கையை சமர்ப்பித்தது",
        "4 - 2 - 3 - 1", "4 - 2 - 3 - 1",
        "2 - 4 - 3 - 1", "2 - 4 - 3 - 1",
        "4 - 3 - 2 - 1", "4 - 3 - 2 - 1",
        "1 - 4 - 2 - 3", "1 - 4 - 2 - 3",
        "A",
        "The chronological sequence of Centre-State relations milestones is:\n"
        "- Rajamannar Committee Report: 1971 (4)\n"
        "- 42nd Amendment Act: 1976 (2)\n"
        "- Sarkaria Commission Report: 1988 (3)\n"
        "- Punchhi Commission Report: 2010 (1)\n"
        "Chronological order: 4 (1971) -> 2 (1976) -> 3 (1988) -> 1 (2010).",
        "மத்திய-மாநில உறவுகளின் முக்கிய நிகழ்வுகளின் காலவரிசை:\n"
        "- ராஜமன்னார் குழு அறிக்கை: 1971 (4)\n"
        "- 42வது திருத்தச் சட்டம்: 1976 (2)\n"
        "- சர்க்காரியா ஆணைய அறிக்கை: 1988 (3)\n"
        "- பூஞ்சி ஆணைய அறிக்கை: 2010 (1)\n"
        "காலவரிசை: 4 (1971) -> 2 (1976) -> 3 (1988) -> 1 (2010).",
        "Correct. 1971 -> 1976 -> 1988 -> 2010.", "சரியானது. 1971 -> 1976 -> 1988 -> 2010.",
        "Incorrect sequence.", "தவறான வரிசை.",
        "Incorrect sequence.", "தவறான வரிசை.",
        "Incorrect sequence.", "தவறான வரிசை.",
        "Centre-State Timeline: Rajamannar (1971) -> 42nd CAA (1976) -> Sarkaria (1988) -> Punchhi (2010).",
        "மத்திய-மாநில காலவரிசை: ராஜமன்னார் (1971) -> 42வது திருத்தம் (1976) -> சர்க்காரியா (1988) -> பூஞ்சி (2010)."
    ))

    # C09: Official Language Milestones
    qs.append(make_sch_q(
        "SCH_C_009", "Medium", "Chronology", "Eighth Schedule",
        "Arrange the following official language legal milestones in chronological order:\n"
        "1. Official Languages (Amendment) Act gave statutory effect to Nehru's assurance\n"
        "2. First Official Language Commission appointed under B.G. Kher\n"
        "3. Parliamentary Committee on Official Language constituted under G.B. Pant\n"
        "4. Official Languages Act enacted by Parliament",
        "அதிகாரப்பூர்வ மொழி தொடர்பான பின்வரும் சட்டப்பூர்வ நிகழ்வுகளை காலவரிசைப்படி வரிசைப்படுத்துக:\n"
        "1. நேருவின் உறுதிமொழிக்கு சட்டப்பூர்வ வடிவம் அளித்த அதிகாரப்பூர்வ மொழிகள் (திருத்தச்) சட்டம்\n"
        "2. பி.ஜி. கேர் தலைமையில் அமைக்கப்பட்ட முதல் உத்தியோகபூர்வ மொழி ஆணையம்\n"
        "3. ஜி.பி. பந்த் தலைமையில் அமைக்கப்பட்ட பாராளுமன்ற உத்தியோகபூர்வ மொழிக் குழு\n"
        "4. பாராளுமன்றத்தால் இயற்றப்பட்ட அதிகாரப்பூர்வ மொழிகள் சட்டம்",
        "2 - 3 - 4 - 1", "2 - 3 - 4 - 1",
        "2 - 4 - 3 - 1", "2 - 4 - 3 - 1",
        "3 - 2 - 4 - 1", "3 - 2 - 4 - 1",
        "4 - 2 - 3 - 1", "4 - 2 - 3 - 1",
        "A",
        "The chronological progression of official language legislation is:\n"
        "- B.G. Kher Commission: 1955 (2)\n"
        "- G.B. Pant Parliamentary Committee: 1957 (3)\n"
        "- Official Languages Act: 1963 (4)\n"
        "- Official Languages (Amendment) Act: 1967 (1)\n"
        "Chronological order: 2 (1955) -> 3 (1957) -> 4 (1963) -> 1 (1967).",
        "அலுவல் மொழி தொடர்பான சட்டங்களின் காலவரிசை:\n"
        "- பி.ஜி. கேர் ஆணையம்: 1955 (2)\n"
        "- ஜி.பி. பந்த் குழு: 1957 (3)\n"
        "- அலுவல் மொழிகள் சட்டம்: 1963 (4)\n"
        "- அலுவல் மொழிகள் திருத்தச் சட்டம்: 1967 (1)\n"
        "காலவரிசை: 2 (1955) -> 3 (1957) -> 4 (1963) -> 1 (1967).",
        "Correct. 1955 -> 1957 -> 1963 -> 1967.", "சரியானது. 1955 -> 1957 -> 1963 -> 1967.",
        "Incorrect sequence.", "தவறான வரிசை.",
        "Incorrect sequence.", "தவறான வரிசை.",
        "Incorrect sequence.", "தவறான வரிசை.",
        "Official Language Timeline: Kher (1955) -> Pant (1957) -> Act (1963) -> Amendment (1967).",
        "அலுவல் மொழி காலவரிசை: கேர் (1955) -> பந்த் (1957) -> சட்டம் (1963) -> திருத்தம் (1967)."
    ))

    # C10: Tribal Governance Acts & Decrees
    qs.append(make_sch_q(
        "SCH_C_010", "Hard", "Chronology", "Fifth & Sixth Schedules",
        "Arrange the following milestones in tribal constitutional governance in chronological order:\n"
        "1. Scheduled Tribes and Other Traditional Forest Dwellers (FRA) Act\n"
        "2. PESA Act enacted extending Panchayats to Fifth Schedule Areas\n"
        "3. Supreme Court Samatha judgment protecting tribal lands\n"
        "4. Gopinath Bordoloi Sub-Committee submitted report on Sixth Schedule tribal areas",
        "பழங்குடியினர் அரசியலமைப்பு ஆளுகையின் பின்வரும் மைல்கற்களை காலவரிசைப்படி வரிசைப்படுத்துக:\n"
        "1. வன உரிமைகள் சட்டம் (FRA) இயற்றப்பட்டது\n"
        "2. ஐந்தாவது அட்டவணைப் பகுதிகளுக்கு பஞ்சாயத்துகளை நீட்டிக்கும் PESA சட்டம் இயற்றப்பட்டது\n"
        "3. பழங்குடியினர் நிலங்களைப் பாதுகாத்த உச்சநீதிமன்றத்தின் சமதா தீர்ப்பு\n"
        "4. ஆறாவது அட்டவணை பழங்குடிப் பகுதிகள் குறித்த கோபிநாத் போர்டோலோய் துணைக் குழுவின் அறிக்கை",
        "4 - 2 - 3 - 1", "4 - 2 - 3 - 1",
        "4 - 3 - 2 - 1", "4 - 3 - 2 - 1",
        "2 - 4 - 3 - 1", "2 - 4 - 3 - 1",
        "1 - 4 - 2 - 3", "1 - 4 - 2 - 3",
        "A",
        "The chronological progression of tribal rights legislation is:\n"
        "- Bordoloi Sub-Committee Report: 1949 (4)\n"
        "- PESA Act enacted: 1996 (2)\n"
        "- Samatha Judgment: 1997 (3)\n"
        "- Forest Rights Act: 2006 (1)\n"
        "Chronological order: 4 (1949) -> 2 (1996) -> 3 (1997) -> 1 (2006).",
        "பழங்குடியினர் உரிமைகள் தொடர்பான சட்டங்களின் காலவரிசை:\n"
        "- போர்டோலோய் துணைக் குழு அறிக்கை: 1949 (4)\n"
        "- PESA சட்டம்: 1996 (2)\n"
        "- சமதா தீர்ப்பு: 1997 (3)\n"
        "- வன உரிமைகள் சட்டம்: 2006 (1)\n"
        "காலவரிசை: 4 (1949) -> 2 (1996) -> 3 (1997) -> 1 (2006).",
        "Correct. 1949 -> 1996 -> 1997 -> 2006.", "சரியானது. 1949 -> 1996 -> 1997 -> 2006.",
        "Incorrect sequence.", "தவறான வரிசை.",
        "Incorrect sequence.", "தவறான வரிசை.",
        "Incorrect sequence.", "தவறான வரிசை.",
        "Tribal Law Timeline: Bordoloi (1949) -> PESA (1996) -> Samatha (1997) -> FRA (2006).",
        "பழங்குடியினர் சட்ட காலவரிசை: போர்டோலோய் (1949) -> PESA (1996) -> சமதா (1997) -> FRA (2006)."
    ))

    # C11 - C25: 15 more unique chronology questions covering all schedules
    chron_specs = [
        # (title, [e1, e2, e3, e4], [y1, y2, y3, y4], correct_indices_1based)
        ("State Reorganisation and Union Territories",
         ["Merger of Dadra & Nagar Haveli and Daman & Diu", "7th Amendment Act reorganizing States into 14 States & 6 UTs", "Jammu and Kashmir Reorganisation Act creating two UTs", "Goa, Daman and Diu incorporated via 12th Amendment"],
         ["2020", "1956", "2019", "1962"],
         [2, 4, 3, 1]),
        ("Ninth Schedule Major Amendment Acts",
         ["76th Amendment (Tamil Nadu 69% Reservation Act)", "17th Amendment adding 44 land reform Acts", "78th Amendment adding 27 land reform Acts", "4th Amendment adding 6 Acts"],
         ["1994", "1964", "1995", "1955"],
         [4, 2, 1, 3]),
        ("Eighth Schedule Classical Languages Batch 2",
         ["Malayalam declared Classical", "Tamil declared Classical", "Odia declared Classical", "Sanskrit declared Classical"],
         ["2013", "2004", "2014", "2005"],
         [2, 4, 1, 3]),
        ("Landmark Property Rights Cases leading to Ninth Schedule",
         ["Golak Nath v. State of Punjab", "State of Bihar v. Kameshwar Singh", "Minerva Mills v. Union of India", "Kesavananda Bharati v. State of Kerala"],
         ["1967", "1952", "1980", "1973"],
         [2, 1, 4, 3]),
        ("Anti-Defection Law Amendments and Major Cases",
         ["Kihoto Hollohan Supreme Court ruling", "52nd Amendment enacting Tenth Schedule", "Keisham Meghachandra 3-month ruling", "91st Amendment deleting split exception"],
         ["1992", "1985", "2020", "2003"],
         [2, 1, 4, 3]),
        ("Local Self-Government Acts Enforcement",
         ["PESA Act enacted for Fifth Schedule areas", "73rd Amendment Act came into force (National Panchayati Raj Day)", "74th Amendment Act came into force for Municipalities", "Constitution 64th Amendment Bill introduced in Lok Sabha"],
         ["1996", "1993", "1993", "1989"],
         [4, 2, 3, 1]),
        ("First Schedule North-Eastern States Statehood",
         ["Mizoram and Arunachal Pradesh attained full statehood", "Nagaland formed as a separate State", "Meghalaya, Manipur, and Tripura attained full statehood", "Sikkim admitted as 22nd State of India"],
         ["1987", "1963", "1972", "1975"],
         [2, 3, 4, 1]),
        ("Second Schedule Judicial Emoluments Revisions",
         ["High Court and Supreme Court Judges (Salaries) Amendment Act 2018", "7th Amendment Act omitting Part B of Second Schedule", "54th Constitutional Amendment revising judges salaries", "High Court and Supreme Court Judges (Salaries) Amendment Act 1998"],
         ["2018", "1956", "1986", "1998"],
         [2, 3, 4, 1]),
        ("Third Schedule and Oath Related Reforms",
         ["Shabbir v. State election oath ruling", "16th Amendment inserting 'sovereignty and integrity' into oaths", "Election Commission notification mandating Form III-A oath at nomination", "Representation of the People Act 1951 enacted"],
         ["1965", "1963", "1974", "1951"],
         [4, 2, 1, 3]),
        ("Fourth Schedule Rajya Sabha Freezes and Changes",
         ["84th Amendment extending freeze until 2026", "42nd Amendment freezing Rajya Sabha seat allocation until 2000", "Andhra Pradesh Reorganisation Act splitting 18 seats (11 AP + 7 Telangana)", "Representation of the People Act 1950 Fourth Schedule allocations"],
         ["2001", "1976", "2014", "1950"],
         [4, 2, 1, 3]),
        ("Sixth Schedule Autonomous Councils Additions",
         ["Bodoland Territorial Council created via 90th CAA", "Karbi Anglong and North Cachar Hills autonomous councils established", "Tripura Tribal Areas Autonomous District Council brought under Sixth Schedule via 49th CAA", "22nd Amendment inserting Article 244A for autonomous state in Assam"],
         ["2003", "1952", "1984", "1969"],
         [2, 4, 3, 1]),
        ("Seventh Schedule Tax Reforms",
         ["101st Amendment introducing GST (Article 246A)", "Service Tax introduced under Entry 97 residuary powers", "88th Amendment inserting Article 268A (Service Tax entry 92C)", "Gift Tax Act enacted under Entry 97 residuary powers"],
         ["2016", "1994", "2003", "1958"],
         [4, 2, 3, 1]),
        ("Official Language Acts and Orders",
         ["Presidential Order on Official Language authorizing Hindi in addition to English", "Official Languages Resolution passed by Parliament", "Official Languages Rules formulated", "Official Languages Act enacted"],
         ["1960", "1968", "1976", "1963"],
         [1, 4, 2, 3]),
        ("Ninth Schedule Judicial Review Milestones",
         ["Waman Rao establishing April 24, 1973 cutoff date", "Kesavananda Bharati establishing Basic Structure doctrine", "I.R. Coelho establishing Rights Test for post-1973 laws", "Indira Nehru Gandhi invalidating 39th Amendment (Article 329A)"],
         ["1981", "1973", "2007", "1975"],
         [2, 4, 1, 3]),
        ("Panchayati Raj Constitutionalization Process",
         ["73rd Amendment passed by Parliament", "L.M. Singhvi Committee recommended constitutional status for Panchayats", "73rd Amendment Bill introduced by Narasimha Rao government", "64th Amendment Bill passed by Lok Sabha but defeated in Rajya Sabha"],
         ["1992", "1986", "1991", "1989"],
         [2, 4, 3, 1])
    ]

    for idx, (title, events, years, seq) in enumerate(chron_specs, start=11):
        cid = f"SCH_C_{idx:03d}"
        seq_str = f"{seq[0]} - {seq[1]} - {seq[2]} - {seq[3]}"
        
        # 3 other unique permutations
        alt1 = f"{seq[1]} - {seq[0]} - {seq[3]} - {seq[2]}"
        alt2 = f"{seq[0]} - {seq[2]} - {seq[1]} - {seq[3]}"
        alt3 = f"{seq[3]} - {seq[1]} - {seq[0]} - {seq[2]}"

        stem_en = (
            f"Arrange the following events relating to {title} in chronological order:\n"
            f"1. {events[0]}\n"
            f"2. {events[1]}\n"
            f"3. {events[2]}\n"
            f"4. {events[3]}"
        )
        stem_ta = (
            f"{title} தொடர்பான பின்வரும் நிகழ்வுகளை காலவரிசைப்படி வரிசைப்படுத்துக:\n"
            f"1. {events[0]}\n"
            f"2. {events[1]}\n"
            f"3. {events[2]}\n"
            f"4. {events[3]}"
        )

        year_breakdown_en = "\n".join([f"- {events[i-1]}: {years[i-1]} ({i})" for i in seq])
        year_breakdown_ta = "\n".join([f"- {events[i-1]}: {years[i-1]} ({i})" for i in seq])
        arrow_seq = f"{seq[0]} ({years[seq[0]-1]}) -> {seq[1]} ({years[seq[1]-1]}) -> {seq[2]} ({years[seq[2]-1]}) -> {seq[3]} ({years[seq[3]-1]})"

        exp_en = (
            f"The chronological order of events relating to {title} is:\n"
            f"{year_breakdown_en}\n"
            f"Chronological order: {arrow_seq}."
        )
        exp_ta = (
            f"{title} தொடர்பான நிகழ்வுகளின் காலவரிசை:\n"
            f"{year_breakdown_ta}\n"
            f"காலவரிசை: {arrow_seq}."
        )

        qs.append(make_sch_q(
            cid, "Medium" if idx % 2 == 0 else "Hard", "Chronology", title,
            stem_en, stem_ta,
            seq_str, seq_str,
            alt1, alt1,
            alt2, alt2,
            alt3, alt3,
            "A",
            exp_en, exp_ta,
            f"Correct chronological sequence: {seq_str}.", f"சரியான காலவரிசை: {seq_str}.",
            "Incorrect sequence.", "தவறான வரிசை.",
            "Incorrect sequence.", "தவறான வரிசை.",
            "Incorrect sequence.", "தவறான வரிசை.",
            f"{title}: Chronological timeline assessment.",
            f"{title}: காலவரிசை மதிப்பீடு."
        ))

    return qs

if __name__ == "__main__":
    qs = get_chronology_questions()
    print(f"Loaded {len(qs)} Chronology questions successfully.")
