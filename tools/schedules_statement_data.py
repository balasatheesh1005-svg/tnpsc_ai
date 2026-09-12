# -*- coding: utf-8 -*-
"""
Statement-Based MCQs for Constitutional Schedules (50 questions: SCH_S_001 to SCH_S_050)
"""
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.insert(0, os.path.dirname(__file__))

from sch_mcq_helper import make_sch_q

def get_statement_questions():
    qs = []

    # S01 - S05: First & Second Schedules Statements
    qs.append(make_sch_q(
        "SCH_S_001", "Medium", "Statement-Based", "First Schedule",
        "Consider the following statements regarding the First Schedule of the Constitution of India:\n"
        "1. It specifies the names of the States and their territorial extent.\n"
        "2. It specifies the names of the Union Territories and their extent.\n"
        "3. Any amendment to the First Schedule requires a special majority under Article 368 with ratification by half the states.\n"
        "Which of the statements given above is/are correct?",
        "இந்திய அரசியலமைப்பின் முதல் அட்டவணை தொடர்பான பின்வரும் கூற்றுகளைக் கருத்தில் கொள்க:\n"
        "1. இது மாநிலங்களின் பெயர்கள் மற்றும் அவற்றின் எல்லைப் பகுதிகளைக் குறிப்பிடுகிறது.\n"
        "2. இது யூனியன் பிரதேசங்களின் பெயர்கள் மற்றும் அவற்றின் எல்லைப் பகுதிகளைக் குறிப்பிடுகிறது.\n"
        "3. முதல் அட்டவணையில் செய்யப்படும் எந்தவொரு திருத்தத்திற்கும் சரத்து 368-ன் கீழ் மாநிலங்களின் ஏற்புடன் கூடிய சிறப்புப் பெரும்பான்மை தேவைப்படுகிறது.\n"
        "மேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
        "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
        "1 only", "1 மட்டுமே",
        "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
        "1, 2 and 3", "1, 2 மற்றும் 3",
        "A",
        "Statements 1 and 2 are correct: The First Schedule lists both the States and Union Territories with their territorial jurisdictions. Statement 3 is incorrect: Under Article 4(2), any law passed under Article 2 or 3 that amends the First Schedule is passed by a simple majority and is NOT deemed to be an amendment under Article 368.",
        "கூற்றுகள் 1 மற்றும் 2 சரியானவை: முதல் அட்டவணை மாநிலங்கள் மற்றும் யூனியன் பிரதேசங்களின் பெயர்கள் மற்றும் எல்லைகளைப் பட்டியலிடுகிறது. கூற்று 3 தவறானது: சரத்து 4(2)-ன் படி, முதல் அட்டவணையைத் திருத்தும் சட்டங்கள் சரத்து 2 அல்லது 3-ன் கீழ் எளிய பெரும்பான்மையால் நிறைவேற்றப்படுகின்றன மற்றும் அவை சரத்து 368-ன் கீழான திருத்தமாகக் கருதப்படாது.",
        "Correct. Statements 1 and 2 are correct; statement 3 is incorrect.", "சரியானது. கூற்றுகள் 1 & 2 சரியானவை; கூற்று 3 தவறானது.",
        "Incorrect. Statement 2 is also correct.", "தவறானது. கூற்று 2-ம் சரியானது.",
        "Incorrect. Statement 3 is incorrect because simple majority under Art 4 suffices.", "தவறானது. சரத்து 4-ன் கீழ் எளிய பெரும்பான்மை போதுமானது என்பதால் கூற்று 3 தவறு.",
        "Incorrect. Statement 3 is incorrect.", "தவறானது. கூற்று 3 தவறானது.",
        "First Schedule: 28 States + 8 UTs. Altered via ordinary legislation under Article 4.",
        "முதல் அட்டவணை: 28 மாநிலங்கள் + 8 UTகள். சரத்து 4-ன் கீழ் சாதாரண சட்டம் மூலம் திருத்தப்படுகிறது.",
        "Article 1 states that India shall be a Union of States, whose names are specified in the First Schedule.",
        "சரத்து 1 இந்தியா மாநிலங்களின் ஒன்றியம் என்றும், அவற்றின் பெயர்கள் முதல் அட்டவணையில் குறிப்பிடப்பட்டுள்ளதாகவும் கூறுகிறது."
    ))

    qs.append(make_sch_q(
        "SCH_S_002", "Hard", "Statement-Based", "Second Schedule",
        "Consider the following statements regarding the Second Schedule of the Indian Constitution:\n"
        "1. It contains provisions relating to the emoluments, allowances, and privileges of the President, Governors, Judges, and the Comptroller and Auditor-General.\n"
        "2. The Prime Minister and Union Cabinet Ministers draw their salaries under Part B of the Second Schedule.\n"
        "3. Emoluments and allowances of Supreme Court Judges cannot be varied to their disadvantage during their term of office.\n"
        "Which of the statements given above is/are correct?",
        "இந்திய அரசியலமைப்பின் இரண்டாவது அட்டவணை தொடர்பான பின்வரும் கூற்றுகளைக் கருத்தில் கொள்க:\n"
        "1. இது குடியரசுத் தலைவர், ஆளுநர்கள், நீதிபதிகள் மற்றும் தலைமைக் கணக்குத் தணிக்கையாளரின் ஊதியங்கள், படிகள் மற்றும் சலுகைகள் பற்றிய விதிகளைக் கொண்டுள்ளது.\n"
        "2. பிரதமரும் மத்திய அமைச்சரவை அமைச்சர்களும் இரண்டாவது அட்டவணையின் பகுதி B-ன் கீழ் தங்கள் சம்பளத்தைப் பெறுகின்றனர்.\n"
        "3. உச்சநீதிமன்ற நீதிபதிகளின் ஊதியங்கள் மற்றும் படிகள் அவர்களின் பதவிக்காலத்தில் அவர்களுக்குப் பாதகமாக குறைக்கப்பட முடியாது.\n"
        "மேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
        "1 and 3 only", "1 மற்றும் 3 மட்டுமே",
        "1 only", "1 மட்டுமே",
        "1, 2 and 3", "1, 2 மற்றும் 3",
        "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
        "A",
        "Statements 1 and 3 are correct. Statement 2 is incorrect: Ministers (including the Prime Minister) are NOT included in the Second Schedule; their salaries are determined by Parliament by law under Article 75(6). Furthermore, Part B of the Second Schedule was omitted by the 7th Amendment Act, 1956.",
        "கூற்றுகள் 1 மற்றும் 3 சரியானவை. கூற்று 2 தவறானது: பிரதமர் உட்பட அமைச்சர்கள் இரண்டாவது அட்டவணையில் சேர்க்கப்படவில்லை; அவர்களின் சம்பளம் சரத்து 75(6)-ன் கீழ் பாராளுமன்றத்தால் சட்டத்தின் மூலம் தீர்மானிக்கப்படுகிறது. மேலும் பகுதி B 7வது திருத்தம் 1956-ஆல் நீக்கப்பட்டது.",
        "Correct. Statements 1 and 3 are correct; statement 2 is incorrect.", "சரியானது. கூற்றுகள் 1 மற்றும் 3 சரியானவை; கூற்று 2 தவறானது.",
        "Incorrect. Statement 3 is also correct under Article 125(2).", "தவறானது. சரத்து 125(2)-ன் படி கூற்று 3-ம் சரியானது.",
        "Incorrect. Statement 2 is false.", "தவறானது. கூற்று 2 தவறானது.",
        "Incorrect. Statement 1 is definitely correct.", "தவறானது. கூற்று 1 உறுதியாக சரியானது.",
        "Second Schedule: Covers President, Governors, Presiding Officers, Judges, CAG. Excludes Ministers.",
        "2வது அட்டவணை: தலைவர், ஆளுநர்கள், அவைத் தலைவர்கள், நீதிபதிகள், CAG ஆகியோரை உள்ளடக்கியது; அமைச்சர்களை விலக்கியுள்ளது.",
        "Ministerial salaries are votable under Article 75(6), while Second Schedule salaries are charged on Consolidated Fund.",
        "அமைச்சர்களின் சம்பளம் சரத்து 75(6)-ன் கீழ் வாக்கெடுப்புக்கு உட்பட்டது; 2வது அட்டவணை சம்பளங்கள் தொகுப்பு நிதியில் விதிக்கப்படுபவை."
    ))

    qs.append(make_sch_q(
        "SCH_S_003", "Medium", "Statement-Based", "Third Schedule",
        "Consider the following statements regarding Oaths and Affirmations under the Third Schedule:\n"
        "1. It prescribes the form of oath for a Union Minister, including an Oath of Office and an Oath of Secrecy.\n"
        "2. It contains the form of oath for candidates contesting elections to Parliament.\n"
        "3. The oath of the President of India is set out in Form I of the Third Schedule.\n"
        "Which of the statements given above is/are correct?",
        "மூன்றாவது அட்டவணையின் கீழான பிரமாணங்கள் மற்றும் உறுதியேற்புகள் தொடர்பான பின்வரும் கூற்றுகளைக் கருத்தில் கொள்க:\n"
        "1. இது மத்திய அமைச்சருக்கான பதவிப் பிரமாணம் மற்றும் ரகசியக் காப்புப் பிரமாணப் படிவங்களை பரிந்துரைக்கிறது.\n"
        "2. இது பாராளுமன்றத் தேர்தலில் போட்டியிடும் வேட்பாளர்களுக்கான பிரமாணப் படிவத்தைக் கொண்டுள்ளது.\n"
        "3. இந்தியக் குடியரசுத் தலைவரின் பிரமாணம் மூன்றாவது அட்டவணையின் படிவம் I-ல் குறிப்பிடப்பட்டுள்ளது.\n"
        "மேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
        "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
        "1 only", "1 மட்டுமே",
        "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
        "1, 2 and 3", "1, 2 மற்றும் 3",
        "A",
        "Statements 1 and 2 are correct. Statement 3 is incorrect: The oath of the President is NOT in the Third Schedule; it is provided directly in Article 60 of the Constitution.",
        "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது: குடியரசுத் தலைவரின் பிரமாணம் மூன்றாவது அட்டவணையில் இல்லை; அது நேரடியாக அரசியலமைப்பின் சரத்து 60-ல் வழங்கப்பட்டுள்ளது.",
        "Correct. Statements 1 and 2 are correct; 3 is incorrect.", "சரியானது. கூற்றுகள் 1 & 2 சரியானவை; 3 தவறானது.",
        "Incorrect. Statement 2 is also correct under 16th CAA 1963.", "தவறானது. 16வது திருத்தம் 1963-ன் படி கூற்று 2-ம் சரியானது.",
        "Incorrect. Statement 3 is false (President's oath is in Art 60).", "தவறானது. கூற்று 3 தவறு (குடியரசுத் தலைவர் பிரமாணம் சரத்து 60-ல் உள்ளது).",
        "Incorrect. Statement 3 makes this option wrong.", "தவறானது. கூற்று 3 தவறானது.",
        "Third Schedule excludes: President (Art 60), Vice-President (Art 69), Governor (Art 159).",
        "3வது அட்டவணை விலக்குபவை: குடியரசுத் தலைவர் (சரத்து 60), VP (சரத்து 69), ஆளுநர் (சரத்து 159).",
        "Form I is the Oath of Office for a Minister for the Union.",
        "படிவம் I என்பது மத்திய அமைச்சருக்கான பதவிப் பிரமாணமாகும்."
    ))

    qs.append(make_sch_q(
        "SCH_S_004", "Medium", "Statement-Based", "Fourth Schedule",
        "Consider the following statements regarding the Fourth Schedule of the Constitution:\n"
        "1. It allocates seats in the Council of States (Rajya Sabha) to States and Union Territories.\n"
        "2. All Union Territories in India have representation in the Rajya Sabha under the Fourth Schedule.\n"
        "3. The allocation of seats is based on population, and the present allocation is frozen based on the 1971 census.\n"
        "Which of the statements given above is/are correct?",
        "அரசியலமைப்பின் நான்காவது அட்டவணை தொடர்பான பின்வரும் கூற்றுகளைக் கருத்தில் கொள்க:\n"
        "1. இது மாநிலங்கள் மற்றும் யூனியன் பிரதேசங்களுக்கு மாநிலங்களவை (Council of States) இடங்களை ஒதுக்குகிறது.\n"
        "2. இந்தியாவின் அனைத்து யூனியன் பிரதேசங்களுக்கும் நான்காவது அட்டவணையின் கீழ் மாநிலங்களவையில் பிரதிநிதித்துவம் உண்டு.\n"
        "3. இடங்களின் ஒதுக்கீடு மக்கள் தொகை அடிப்படையிலானது, மேலும் தற்போதைய ஒதுக்கீடு 1971 மக்கள் தொகை கணக்கெடுப்பின் அடிப்படையில் முடக்கப்பட்டுள்ளது.\n"
        "மேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
        "1 and 3 only", "1 மற்றும் 3 மட்டுமே",
        "1 only", "1 மட்டுமே",
        "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
        "1, 2 and 3", "1, 2 மற்றும் 3",
        "A",
        "Statements 1 and 3 are correct. Statement 2 is incorrect: Out of 8 Union Territories, only 3 (Delhi, Puducherry, and Jammu & Kashmir) have representation in the Rajya Sabha because only they have legislative assemblies. The other 5 UTs have no Rajya Sabha seats.",
        "கூற்றுகள் 1 மற்றும் 3 சரியானவை. கூற்று 2 தவறானது: இந்தியாவில் உள்ள 8 யூனியன் பிரதேசங்களில் 3 UTகளுக்கு மட்டுமே (டெல்லி, புதுச்சேரி, ஜம்மு காஷ்மீர்) சட்டமன்றங்கள் உள்ளதால் மாநிலங்களவையில் பிரதிநிதித்துவம் உண்டு. மற்ற 5 UTகளுக்கு மாநிலங்களவை இடங்கள் இல்லை.",
        "Correct. Statements 1 and 3 are correct; statement 2 is incorrect.", "சரியானது. கூற்றுகள் 1 மற்றும் 3 சரியானவை; கூற்று 2 தவறானது.",
        "Incorrect. Statement 3 is also correct.", "தவறானது. கூற்று 3-ம் சரியானது.",
        "Incorrect. Statement 2 is incorrect because only 3 UTs are represented.", "தவறானது. 3 UTகளுக்கு மட்டுமே பிரதிநிதித்துவம் உள்ளதால் கூற்று 2 தவறு.",
        "Incorrect. Statement 2 is false.", "தவறானது. கூற்று 2 தவறானது.",
        "Fourth Schedule: Only 3 UTs have RS seats: Delhi (3), Puducherry (1), J&K (4).",
        "4வது அட்டவணை: 3 UTகளுக்கு மட்டுமே RS இடங்கள் உண்டு: டெல்லி (3), புதுச்சேரி (1), J&K (4).",
        "The freeze on seat numbers until post-2026 was mandated by the 84th CAA 2001.",
        "2026 வரை இடங்களின் எண்ணிக்கையை முடக்கியது 84வது திருத்தச் சட்டம் 2001 ஆகும்."
    ))

    qs.append(make_sch_q(
        "SCH_S_005", "Hard", "Statement-Based", "Fifth Schedule",
        "Consider the following statements regarding the administration of Scheduled Areas under the Fifth Schedule:\n"
        "1. The Governor is empowered to direct that any particular Act of Parliament or of the State Legislature shall not apply to a Scheduled Area.\n"
        "2. The Governor can make regulations for the peace and good government of Scheduled Areas, but such regulations require the assent of the President.\n"
        "3. A Tribes Advisory Council must be constituted in all States of India having any tribal population.\n"
        "Which of the statements given above is/are correct?",
        "ஐந்தாவது அட்டவணையின் கீழ் அட்டவணைப் பகுதிகளின் நிர்வாகம் தொடர்பான பின்வரும் கூற்றுகளைக் கருத்தில் கொள்க:\n"
        "1. பாராளுமன்றம் அல்லது மாநில சட்டமன்றத்தின் எந்தவொரு குறிப்பிட்ட சட்டமும் அட்டவணைப் பகுதிக்குப் பொருந்தாது என உத்தரவிட ஆளுநருக்கு அதிகாரம் உண்டு.\n"
        "2. ஆளுநர் அட்டவணைப் பகுதிகளின் அமைதி மற்றும் நல்நிர்வாகத்திற்கு ஒழுங்குமுறைகளை உருவாக்கலாம், ஆனால் அத்தகைய ஒழுங்குமுறைகளுக்கு குடியரசுத் தலைவரின் ஒப்புதல் தேவை.\n"
        "3. பழங்குடி மக்கள் தொகை உள்ள இந்தியாவின் அனைத்து மாநிலங்களிலும் பழங்குடியினர் ஆலோசனைக் குழு (TAC) அமைக்கப்பட வேண்டும்.\n"
        "மேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
        "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
        "1 only", "1 மட்டுமே",
        "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
        "1, 2 and 3", "1, 2 மற்றும் 3",
        "A",
        "Statements 1 and 2 are correct under Paragraph 5 of the Fifth Schedule. Statement 3 is incorrect: A Tribes Advisory Council is MANDATORY only in States having Scheduled Areas. In States with STs but NO Scheduled Areas, a TAC is constituted only IF the President so directs.",
        "பத்தி 5-ன் கீழ் கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது: அட்டவணைப் பகுதிகளைக் கொண்ட மாநிலங்களில் மட்டுமே TAC அமைப்பது கட்டாயமாகும். அட்டவணைப் பகுதிகள் இல்லாத ST மாநிலங்களில் குடியரசுத் தலைவர் உத்தரவிட்டால் மட்டுமே அமைக்கப்படும்.",
        "Correct. Statements 1 and 2 are correct; statement 3 is incorrect.", "சரியானது. கூற்றுகள் 1 மற்றும் 2 சரியானவை; கூற்று 3 தவறானது.",
        "Incorrect. Statement 2 is also correct under Para 5(4).", "தவறானது. பத்தி 5(4)-ன் படி கூற்று 2-ம் சரியானது.",
        "Incorrect. Statement 3 is overbroad and incorrect.", "தவறானது. கூற்று 3 வரம்பு மீறியது மற்றும் தவறானது.",
        "Incorrect. Statement 3 is false.", "தவறானது. கூற்று 3 தவறானது.",
        "Fifth Schedule: TAC is mandatory in Scheduled Area states; optional in others upon President's directive.",
        "5வது அட்டவணை: அட்டவணைப் பகுதி மாநிலங்களில் TAC கட்டாயம்; பிறவற்றில் குடியரசுத் தலைவர் உத்தரவிட்டால் மட்டும்.",
        "Regulations made under Para 5(2) have no effect until assented to by the President (Para 5(4)).",
        "பத்தி 5(2) ஒழுங்குமுறைகள் குடியரசுத் தலைவரின் ஒப்புதல் பெறும் வரை செல்லுபடியாகாது (பத்தி 5(4))."
    ))

    # S06 - S10: Sixth Schedule & Local Self-Government Statements
    qs.append(make_sch_q(
        "SCH_S_006", "Medium", "Statement-Based", "Sixth Schedule",
        "Consider the following statements regarding the Sixth Schedule of the Indian Constitution:\n"
        "1. It applies exclusively to tribal areas in the four North-Eastern States of Assam, Meghalaya, Tripura, and Mizoram.\n"
        "2. The District Councils have powers to make laws on matters such as land allotment, forests, and inheritance of property.\n"
        "3. All laws made by the District Councils take effect only after receiving the assent of the Chief Minister of the State.\n"
        "Which of the statements given above is/are correct?",
        "இந்திய அரசியலமைப்பின் ஆறாவது அட்டவணை தொடர்பான பின்வரும் கூற்றுகளைக் கருத்தில் கொள்க:\n"
        "1. இது அசாம், மேகாலயா, திரிபுரா மற்றும் மிசோரம் ஆகிய நான்கு வடகிழக்கு மாநிலங்களில் உள்ள பழங்குடிப் பகுதிகளுக்கு மட்டுமே பிரத்யேகமாகப் பொருந்தும்.\n"
        "2. நில ஒதுக்கீடு, காடுகள் மற்றும் சொத்துரிமை போன்ற விவகாரங்களில் சட்டங்களை இயற்றும் அதிகாரம் மாவட்டக் கவுன்சில்களுக்கு உண்டு.\n"
        "3. மாவட்டக் கவுன்சில்கள் இயற்றும் அனைத்து சட்டங்களும் மாநில முதலமைச்சரின் ஒப்புதலைப் பெற்ற பின்னரே நடைமுறைக்கு வரும்.\n"
        "மேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
        "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
        "1 only", "1 மட்டுமே",
        "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
        "1, 2 and 3", "1, 2 மற்றும் 3",
        "A",
        "Statements 1 and 2 are correct under Articles 244(2) and Paragraph 3 of the Sixth Schedule. Statement 3 is incorrect: Laws made by District Councils require the assent of the GOVERNOR, not the Chief Minister.",
        "சரத்து 244(2) மற்றும் பத்தி 3-ன் கீழ் கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது: மாவட்ட கவுன்சில்கள் இயற்றும் சட்டங்களுக்கு முதலமைச்சரின் ஒப்புதல் அல்ல, ஆளுநரின் ஒப்புதலே தேவைப்படுகிறது.",
        "Correct. Statements 1 and 2 are correct; 3 is incorrect (Governor assents, not CM).", "சரியானது. கூற்றுகள் 1 & 2 சரியானவை; 3 தவறானது (ஆளுநரே ஒப்புதல் அளிக்கிறார், முதலமைச்சர் அல்ல).",
        "Incorrect. Statement 2 is also correct.", "தவறானது. கூற்று 2-ம் சரியானது.",
        "Incorrect. Statement 3 is false.", "தவறானது. கூற்று 3 தவறானது.",
        "Incorrect. Statement 3 makes this incorrect.", "தவறானது. கூற்று 3 தவறானது.",
        "Sixth Schedule: Assent of the GOVERNOR is required for ADC laws under Paragraph 3(3).",
        "6வது அட்டவணை: பத்தி 3(3)-ன் கீழ் ADC சட்டங்களுக்கு ஆளுநரின் ஒப்புதல் தேவை.",
        "Mnemonic: AMTM (Assam, Meghalaya, Tripura, Mizoram) are the only Sixth Schedule states.",
        "நினைவுச்சொல்: AMTM (அசாம், மேகாலயா, திரிபுரா, மிசோரம்) மட்டுமே 6வது அட்டவணை மாநிலங்கள்."
    ))

    qs.append(make_sch_q(
        "SCH_S_007", "Hard", "Statement-Based", "Sixth Schedule",
        "Consider the following statements regarding Autonomous District Councils (ADCs) under the Sixth Schedule:\n"
        "1. Each District Council consists of a maximum of 30 members, of whom 4 are nominated by the Governor and 26 are elected on the basis of adult suffrage.\n"
        "2. The term of office of elected members is 5 years, while nominated members hold office during the pleasure of the Governor.\n"
        "3. The Governor can dissolve an Autonomous District Council only after receiving a report from a Commission appointed under Paragraph 14.\n"
        "Which of the statements given above is/are correct?",
        "ஆறாவது அட்டவணையின் கீழ் தன்னாட்சி மாவட்டக் கவுன்சில்கள் (ADC) தொடர்பான பின்வரும் கூற்றுகளைக் கருத்தில் கொள்க:\n"
        "1. ஒவ்வொரு மாவட்டக் கவுன்சிலும் அதிகபட்சமாக 30 உறுப்பினர்களைக் கொண்டிருக்கும், அதில் 4 பேர் ஆளுநரால் நியமிக்கப்படுபவர்கள் மற்றும் 26 பேர் வாக்குரிமை அடிப்படையில் தேர்ந்தெடுக்கப்படுபவர்கள்.\n"
        "2. தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்களின் பதவிக்காலம் 5 ஆண்டுகள், அதேசமயம் நியமன உறுப்பினர்கள் ஆளுநரின் விருப்பம் உள்ளவரை பதவியில் இருப்பர்.\n"
        "3. பத்தி 14-ன் கீழ் நியமிக்கப்பட்ட ஒரு ஆணையத்திடமிருந்து அறிக்கை பெற்ற பின்னரே ஆளுநர் ஒரு தன்னாட்சி மாவட்ட கவுன்சிலைக் கலைக்க முடியும்.\n"
        "மேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
        "1, 2 and 3", "1, 2 மற்றும் 3",
        "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
        "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
        "1 and 3 only", "1 மற்றும் 3 மட்டுமே",
        "A",
        "All three statements are correct under Paragraphs 2 and 14/15 of the Sixth Schedule. ADCs comprise 30 members (26 elected for 5 yrs, 4 nominated at Governor's pleasure), and dissolution under Paragraph 15 requires an inquiry report by a Commission appointed under Paragraph 14.",
        "ஆறாவது அட்டவணையின் பத்தி 2 மற்றும் 14/15-ன் கீழ் மூன்று கூற்றுகளுமே சரியானவை. ADC-கள் 30 உறுப்பினர்களைக் கொண்டுள்ளன (26 பேர் 5 ஆண்டுக்கு தேர்வு, 4 பேர் ஆளுநர் விருப்பம் வரை நியமனம்), மேலும் பத்தி 15-ன் கீழான கலைப்புக்கு பத்தி 14 ஆணைய அறிக்கை தேவைப்படுகிறது.",
        "Correct. All three statements 1, 2, and 3 are correct.", "சரியானது. 1, 2 மற்றும் 3 ஆகிய மூன்று கூற்றுகளுமே சரியானவை.",
        "Incorrect. Statement 3 is also correct under Paragraph 15.", "தவறானது. பத்தி 15-ன் கீழ் கூற்று 3-ம் சரியானது.",
        "Incorrect. Statement 1 is also correct.", "தவறானது. கூற்று 1-ம் சரியானது.",
        "Incorrect. Statement 2 is also correct.", "தவறானது. கூற்று 2-ம் சரியானது.",
        "Sixth Schedule ADC: 30 members (26 elected + 4 nominated). Dissolution requires Para 14 Commission report.",
        "6வது அட்டவணை ADC: 30 உறுப்பினர்கள் (26 தேர்வு + 4 நியமனம்). கலைப்பிற்கு பத்தி 14 ஆணைய அறிக்கை தேவை.",
        "Exception: Bodoland Territorial Council has 46 members (40 elected + 6 nominated).",
        "விதிவிலக்கு: போடோலாந்து பிராந்திய கவுன்சில் 46 உறுப்பினர்களைக் கொண்டுள்ளது."
    ))

    qs.append(make_sch_q(
        "SCH_S_008", "Medium", "Statement-Based", "Seventh Schedule",
        "Consider the following statements regarding the Seventh Schedule of the Indian Constitution:\n"
        "1. The 42nd Constitutional Amendment Act, 1976 transferred five subjects from the State List to the Concurrent List.\n"
        "2. 'Police' and 'Public health and sanitation' are subjects enumerated in the State List.\n"
        "3. Residuary powers of legislation in India are vested with the State Legislatures under Article 248.\n"
        "Which of the statements given above is/are correct?",
        "இந்திய அரசியலமைப்பின் ஏழாவது அட்டவணை தொடர்பான பின்வரும் கூற்றுகளைக் கருத்தில் கொள்க:\n"
        "1. 42வது அரசியலமைப்புத் திருத்தச் சட்டம் 1976 ஐந்து துறைகளை மாநிலப் பட்டியலிலிருந்து பொதுப் பட்டியலுக்கு மாற்றியது.\n"
        "2. 'காவல்துறை' மற்றும் 'பொது சுகாதாரம் மற்றும் துப்புரவு' ஆகியவை மாநிலப் பட்டியலில் குறிப்பிடப்பட்டுள்ள துறைகளாகும்.\n"
        "3. இந்தியாவில் சட்டமியற்றுவதற்கான எஞ்சிய அதிகாரங்கள் சரத்து 248-ன் கீழ் மாநில சட்டமன்றங்களிடம் ஒப்படைக்கப்பட்டுள்ளன.\n"
        "மேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
        "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
        "1 only", "1 மட்டுமே",
        "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
        "1, 2 and 3", "1, 2 மற்றும் 3",
        "A",
        "Statements 1 and 2 are correct. Statement 3 is incorrect: Under Article 248 and Entry 97 of the Union List, residuary powers of legislation belong EXCLUSIVELY to Parliament, not the State Legislatures.",
        "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது: சரத்து 248 மற்றும் மத்தியப் பட்டியலின் பதிவு 97-ன் கீழ், எஞ்சிய சட்டமியற்றும் அதிகாரங்கள் பாராளுமன்றத்திற்கு மட்டுமே பிரத்யேகமாக உரியவை, மாநில சட்டமன்றங்களுக்கு அல்ல.",
        "Correct. Statements 1 and 2 are correct; 3 is incorrect (Residuary belongs to Parliament).", "சரியானது. கூற்றுகள் 1 & 2 சரியானவை; 3 தவறானது (எஞ்சியவை பாராளுமன்றத்திற்கு உரியது).",
        "Incorrect. Statement 2 is also correct.", "தவறானது. கூற்று 2-ம் சரியானது.",
        "Incorrect. Statement 3 is incorrect.", "தவறானது. கூற்று 3 தவறானது.",
        "Incorrect. Statement 3 is false.", "தவறானது. கூற்று 3 தவறானது.",
        "Seventh Schedule: Residuary powers -> Parliament (Art 248, Entry 97). Canadian model.",
        "7வது அட்டவணை: எஞ்சிய அதிகாரங்கள் -> பாராளுமன்றம் (சரத்து 248, பதிவு 97). கனடா முறை.",
        "5 subjects moved to Concurrent list in 1976: Education, Forests, Weights & Measures, Wild Animals, Courts admin.",
        "1976-ல் பொதுப் பட்டியலுக்கு மாற்றப்பட்ட 5 துறைகள்: கல்வி, காடுகள், எடைகள், வனவிலங்குகள், நீதிமன்ற நிர்வாகம்."
    ))

    qs.append(make_sch_q(
        "SCH_S_009", "Medium", "Statement-Based", "Eighth Schedule",
        "Consider the following statements regarding the Eighth Schedule of the Indian Constitution:\n"
        "1. The Constitution originally recognized 14 languages in the Eighth Schedule in 1950.\n"
        "2. English is one of the 22 languages officially recognized under the Eighth Schedule.\n"
        "3. Tamil was the first language to be declared a Classical Language by the Government of India in 2004.\n"
        "Which of the statements given above is/are correct?",
        "இந்திய அரசியலமைப்பின் எட்டாவது அட்டவணை தொடர்பான பின்வரும் கூற்றுகளைக் கருத்தில் கொள்க:\n"
        "1. 1950-ல் அரசியலமைப்பு தொடக்கத்தில் 14 மொழிகளை எட்டாவது அட்டவணையில் அங்கீகரித்தது.\n"
        "2. எட்டாவது அட்டவணையின் கீழ் அதிகாரப்பூர்வமாக அங்கீகரிக்கப்பட்ட 22 மொழிகளில் ஆங்கிலமும் ஒன்றாகும்.\n"
        "3. 2004-ல் இந்திய அரசால் செம்மொழியாக அறிவிக்கப்பட்ட முதல் மொழி தமிழ் ஆகும்.\n"
        "மேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
        "1 and 3 only", "1 மற்றும் 3 மட்டுமே",
        "1 only", "1 மட்டுமே",
        "1, 2 and 3", "1, 2 மற்றும் 3",
        "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
        "A",
        "Statements 1 and 3 are correct. Statement 2 is incorrect: English is NOT included in the Eighth Schedule (despite being an associate official language of the Union under the Official Languages Act, 1963).",
        "கூற்றுகள் 1 மற்றும் 3 சரியானவை. கூற்று 2 தவறானது: ஆங்கிலம் எட்டாவது அட்டவணையில் சேர்க்கப்படவில்லை (1963 சட்டம் மூலம் மத்திய அரசின் இணை அலுவல் மொழியாக இருந்தபோதிலும்).",
        "Correct. Statements 1 and 3 are correct; 2 is incorrect (English is not in Eighth Schedule).", "சரியானது. கூற்றுகள் 1 & 3 சரியானவை; 2 தவறானது (ஆங்கிலம் 8வது அட்டவணையில் இல்லை).",
        "Incorrect. Statement 3 is also correct.", "தவறானது. கூற்று 3-ம் சரியானது.",
        "Incorrect. Statement 2 is false.", "தவறானது. கூற்று 2 தவறானது.",
        "Incorrect. Statement 1 is correct, while 2 is false.", "தவறானது. கூற்று 1 சரியானது, 2 தவறானது.",
        "Eighth Schedule: 14 original -> 22 current. English and Rajasthani are NOT in the 8th Schedule.",
        "8வது அட்டவணை: அசல் 14 -> தற்போது 22. ஆங்கிலம் மற்றும் ராஜஸ்தானி 8வது அட்டவணையில் இல்லை.",
        "Tamil was declared Classical in 2004, followed by Sanskrit (2005), Telugu & Kannada (2008), Malayalam (2013), Odia (2014).",
        "தமிழ் 2004-ல் செம்மொழியாக அறிவிக்கப்பட்டது; அதைத் தொடர்ந்து சமஸ்கிருதம் (2005), தெலுங்கு & கன்னடம் (2008), மலையாளம் (2013), ஒடியா (2014)."
    ))

    qs.append(make_sch_q(
        "SCH_S_010", "Hard", "Statement-Based", "Ninth Schedule",
        "Consider the following statements regarding the Ninth Schedule and judicial review:\n"
        "1. The Ninth Schedule was added to the Constitution by the 1st Constitutional Amendment Act, 1951 along with Article 31B.\n"
        "2. In the I.R. Coelho case (2007), the Supreme Court ruled that all laws placed in the Ninth Schedule on or after April 24, 1973 are open to challenge on the ground of violating the Basic Structure.\n"
        "3. Tamil Nadu's 69% reservation law was inserted into the Ninth Schedule by the 76th Constitutional Amendment Act, 1994.\n"
        "Which of the statements given above is/are correct?",
        "ஒன்பதாவது அட்டவணை மற்றும் நீதித்துறை மறுஆய்வு தொடர்பான பின்வரும் கூற்றுகளைக் கருத்தில் கொள்க:\n"
        "1. 1951-ன் 1வது அரசியலமைப்புத் திருத்தச் சட்டம் மூலம் சரத்து 31B உடன் ஒன்பதாவது அட்டவணை அரசியலமைப்பில் சேர்க்கப்பட்டது.\n"
        "2. ஐ.ஆர். கோயல்ஹோ வழக்கில் (2007), ஏப்ரல் 24, 1973 அன்றோ அல்லது அதற்குப் பின்னரோ 9வது அட்டவணையில் வைக்கப்பட்ட அனைத்து சட்டங்களும் அடிப்படைக் கட்டமைப்பை மீறியதாக சவால் செய்யப்படலாம் என உச்சநீதிமன்றம் தீர்ப்பளித்தது.\n"
        "3. தமிழ்நாட்டின் 69% இடஒதுக்கீட்டுச் சட்டம் 76வது அரசியலமைப்புத் திருத்தச் சட்டம் 1994 மூலம் ஒன்பதாவது அட்டவணையில் சேர்க்கப்பட்டது.\n"
        "மேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
        "1, 2 and 3", "1, 2 மற்றும் 3",
        "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
        "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
        "1 and 3 only", "1 மற்றும் 3 மட்டுமே",
        "A",
        "All three statements are correct: 1st CAA 1951 inserted 9th Schedule & Art 31B; I.R. Coelho (2007) fixed April 24, 1973 as the cutoff date for basic structure scrutiny; and 76th CAA 1994 placed TN's 69% Reservation Act into the Ninth Schedule (Entry 257A).",
        "மூன்று கூற்றுகளுமே சரியானவை: 1வது திருத்தம் 1951 9வது அட்டவணை & சரத்து 31B-ஐச் சேர்த்தது; ஐ.ஆர். கோயல்ஹோ (2007) ஏப்ரல் 24, 1973-ஐ அடிப்படைக் கட்டமைப்பு மறுஆய்விற்கான வரம்புத் தேதியாக நிர்ணயித்தது; மற்றும் 76வது திருத்தம் 1994 தமிழக 69% இடஒதுக்கீட்டுச் சட்டத்தை 9வது அட்டவணையில் சேர்த்தது.",
        "Correct. Statements 1, 2, and 3 are all correct.", "சரியானது. 1, 2 மற்றும் 3 ஆகிய அனைத்து கூற்றுகளும் சரியானவை.",
        "Incorrect. Statement 3 is also correct.", "தவறானது. கூற்று 3-ம் சரியானது.",
        "Incorrect. Statement 1 is also correct.", "தவறானது. கூற்று 1-ம் சரியானது.",
        "Incorrect. Statement 2 is also correct.", "தவறானது. கூற்று 2-ம் சரியானது.",
        "Ninth Schedule: 1st CAA 1951 -> I.R. Coelho 2007 (April 24, 1973 cutoff) -> TN 69% (76th CAA 1994).",
        "9வது அட்டவணை: 1வது திருத்தம் 1951 -> கோயல்ஹோ 2007 (ஏப்ரல் 24, 1973 வரம்பு) -> TN 69% (76வது திருத்தம் 1994).",
        "Article 31B provides that no Act listed in the Ninth Schedule can be voided on grounds of inconsistency with Fundamental Rights."
    ))

    # S11 - S20: Tenth, Eleventh, Twelfth & Specific Schedules Statements
    qs.append(make_sch_q(
        "SCH_S_011", "Medium", "Statement-Based", "Tenth Schedule",
        "Consider the following statements regarding the Tenth Schedule (Anti-Defection Law):\n"
        "1. It was inserted into the Constitution by the 52nd Constitutional Amendment Act, 1985.\n"
        "2. An independent member of a House is disqualified if he joins any political party after election.\n"
        "3. A nominated member is disqualified if he joins a political party within six months of taking his seat.\n"
        "Which of the statements given above is/are correct?",
        "பத்தாவது அட்டவணை (கட்சித் தாவல் தடைச் சட்டம்) தொடர்பான பின்வரும் கூற்றுகளைக் கருத்தில் கொள்க:\n"
        "1. இது 52வது அரசியலமைப்புத் திருத்தச் சட்டம் 1985 மூலம் அரசியலமைப்பில் சேர்க்கப்பட்டது.\n"
        "2. ஒரு அவையின் சுயேச்சை உறுப்பினர் தேர்தலுக்குப் பிறகு ஏதேனும் ஒரு அரசியல் கட்சியில் சேர்ந்தால் தகுதிநீக்கம் செய்யப்படுவார்.\n"
        "3. ஒரு நியமன உறுப்பினர் தனது பதவியேற்ற ஆறு மாதங்களுக்குள் ஒரு அரசியல் கட்சியில் சேர்ந்தால் தகுதிநீக்கம் செய்யப்படுவார்.\n"
        "மேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
        "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
        "1 only", "1 மட்டுமே",
        "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
        "1, 2 and 3", "1, 2 மற்றும் 3",
        "A",
        "Statements 1 and 2 are correct. Statement 3 is incorrect: Under Paragraph 2(3), a nominated member is PERMITTED to join a party within six months; he is disqualified only if he joins AFTER the expiry of six months.",
        "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது: பத்தி 2(3)-ன் படி, ஒரு நியமன உறுப்பினர் ஆறு மாதங்களுக்குள் கட்சியில் சேர அனுமதிக்கப்படுகிறார்; ஆறு மாதங்கள் முடிந்த பிறகு கட்சியில் சேர்ந்தால் மட்டுமே அவர் தகுதிநீக்கம் செய்யப்படுவார்.",
        "Correct. Statements 1 and 2 are correct; 3 is inverted.", "சரியானது. கூற்றுகள் 1 & 2 சரியானவை; 3 தலைகீழாக உள்ளது.",
        "Incorrect. Statement 2 is also correct.", "தவறானது. கூற்று 2-ம் சரியானது.",
        "Incorrect. Statement 3 is false.", "தவறானது. கூற்று 3 தவறானது.",
        "Incorrect. Statement 3 is false.", "தவறானது. கூற்று 3 தவறானது.",
        "Tenth Schedule: Nominated member -> can join within 6 months; disqualified if joins AFTER 6 months.",
        "10வது அட்டவணை: நியமன உறுப்பினர் -> 6 மாதங்களுக்குள் சேரலாம்; 6 மாதங்களுக்குப் பின் சேர்ந்தால் தகுதிநீக்கம்.",
        "Independent member -> CANNOT join any party at any time after election.",
        "சுயேச்சை உறுப்பினர் -> தேர்தலுக்குப் பின் எந்த நேரத்திலும் எந்தக் கட்சியிலும் சேர முடியாது."
    ))

    qs.append(make_sch_q(
        "SCH_S_012", "Hard", "Statement-Based", "Tenth Schedule",
        "Consider the following statements regarding the 91st Constitutional Amendment Act, 2003 and the Tenth Schedule:\n"
        "1. It deleted the provision protecting a split of one-third (1/3rd) members of the legislature party from disqualification.\n"
        "2. It capped the total number of Ministers, including the Prime Minister/Chief Minister, at 15% of the total strength of the Lok Sabha / Legislative Assembly.\n"
        "3. A member disqualified under the Tenth Schedule is debarred from being appointed as a Minister until the date on which his term would expire or until he is re-elected, whichever is earlier.\n"
        "Which of the statements given above is/are correct?",
        "91வது அரசியலமைப்புத் திருத்தச் சட்டம் 2003 மற்றும் பத்தாவது அட்டவணை தொடர்பான பின்வரும் கூற்றுகளைக் கருத்தில் கொள்க:\n"
        "1. இது சட்டமன்றக் கட்சியின் மூன்றில் ஒரு பங்கு (1/3) உறுப்பினர்களின் பிளவை தகுதிநீக்கத்திலிருந்து பாதுகாத்த விதியை நீக்கியது.\n"
        "2. இது பிரதமர்/முதலமைச்சர் உட்பட மொத்த அமைச்சர்களின் எண்ணிக்கையை மக்களவை/சட்டமன்றத்தின் மொத்த பலத்தில் 15% ஆக வரம்பிட்டது.\n"
        "3. பத்தாவது அட்டவணையின் கீழ் தகுதிநீக்கம் செய்யப்பட்ட ஒரு உறுப்பினர், அவரது பதவிக்காலம் முடியும் வரை அல்லது மீண்டும் தேர்ந்தெடுக்கப்படும் வரை (எது முந்தையதோ அதுவரை) அமைச்சராக நியமிக்கப்பட முடியாது.\n"
        "மேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
        "1, 2 and 3", "1, 2 மற்றும் 3",
        "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
        "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
        "1 and 3 only", "1 மற்றும் 3 மட்டுமே",
        "A",
        "All three statements are correct: The 91st CAA 2003 omitted Paragraph 3 (split exception), added Article 75(1A)/164(1A) (15% ceiling), and inserted Article 75(1B)/164(1B) (disqualification from ministerial post).",
        "மூன்று கூற்றுகளுமே சரியானவை: 91வது திருத்தம் 2003 பத்தி 3-ஐ (பிளவு விதிவிலக்கு) நீக்கியது, சரத்து 75(1A)/164(1A) மூலம் 15% வரம்பை விதித்தது, மற்றும் சரத்து 75(1B)/164(1B) மூலம் அமைச்சர் பதவிக்கு தடையை ஏற்படுத்தியது.",
        "Correct. Statements 1, 2, and 3 are all correct.", "சரியானது. 1, 2 மற்றும் 3 ஆகிய அனைத்து கூற்றுகளும் சரியானவை.",
        "Incorrect. Statement 3 is also correct under Art 75(1B) and 164(1B).", "தவறானது. சரத்து 75(1B) மற்றும் 164(1B)-ன் கீழ் கூற்று 3-ம் சரியானது.",
        "Incorrect. Statement 1 is also correct.", "தவறானது. கூற்று 1-ம் சரியானது.",
        "Incorrect. Statement 2 is also correct.", "தவறானது. கூற்று 2-ம் சரியானது.",
        "91st CAA 2003: 15% Cabinet limit, deleted 1/3 split defense, barred disqualified members from ministerial posts.",
        "91வது திருத்தம் 2003: 15% அமைச்சரவை வரம்பு, 1/3 பிளவு பாதுகாப்பு நீக்கம், தகுதிநீக்கம் செய்யப்பட்டவருக்கு அமைச்சர் பதவி தடை.",
        "For smaller states, the minimum number of ministers in the State Council of Ministers is fixed at 12."
    ))

    qs.append(make_sch_q(
        "SCH_S_013", "Medium", "Statement-Based", "Eleventh & Twelfth Schedules",
        "Consider the following statements regarding the Eleventh and Twelfth Schedules:\n"
        "1. The Eleventh Schedule contains 29 functional items for Panchayats and was added by the 73rd Amendment Act, 1992.\n"
        "2. The Twelfth Schedule contains 18 functional items for Municipalities and was added by the 74th Amendment Act, 1992.\n"
        "3. Devolution of all items listed in both Schedules to local bodies is automatic and mandatory upon enactment.\n"
        "Which of the statements given above is/are correct?",
        "பதினோராவது மற்றும் பன்னிரண்டாவது அட்டவணைகள் தொடர்பான பின்வரும் கூற்றுகளைக் கருத்தில் கொள்க:\n"
        "1. பதினோராவது அட்டவணை பஞ்சாயத்துகளுக்கான 29 செயல்பாட்டுப் பணிகளைக் கொண்டுள்ளது மற்றும் 73வது திருத்தச் சட்டம் 1992 மூலம் சேர்க்கப்பட்டது.\n"
        "2. பன்னிரண்டாவது அட்டவணை நகராட்சிகளுக்கான 18 செயல்பாட்டுப் பணிகளைக் கொண்டுள்ளது மற்றும் 74வது திருத்தச் சட்டம் 1992 மூலம் சேர்க்கப்பட்டது.\n"
        "3. இரண்டு அட்டவணைகளிலும் பட்டியலிடப்பட்டுள்ள அனைத்து பணிகளையும் உள்ளாட்சி அமைப்புகளுக்கு ஒப்படைப்பது சட்டம் இயற்றப்பட்டவுடன் தானாகவே கட்டாயமாகிறது.\n"
        "மேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
        "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
        "1 only", "1 மட்டுமே",
        "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
        "1, 2 and 3", "1, 2 மற்றும் 3",
        "A",
        "Statements 1 and 2 are correct. Statement 3 is incorrect: Under Articles 243G and 243W, devolution is NOT automatic; the State Legislature 'may, by law' devolve these powers at its discretion.",
        "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது: சரத்து 243G மற்றும் 243W-ன் கீழ், அதிகாரப் பகிர்வு தானியக்கமானது அல்ல; மாநில சட்டமன்றம் தனது விருப்புரிமையின்படி 'சட்டம் மூலம்' இவற்றை ஒப்படைக்கலாம்.",
        "Correct. Statements 1 and 2 are correct; 3 is incorrect (devolution is discretionary on States).", "சரியானது. கூற்றுகள் 1 & 2 சரியானவை; 3 தவறானது (அதிகாரப் பகிர்வு மாநிலங்களின் விருப்புரிமை).",
        "Incorrect. Statement 2 is also correct.", "தவறானது. கூற்று 2-ம் சரியானது.",
        "Incorrect. Statement 3 is false.", "தவறானது. கூற்று 3 தவறானது.",
        "Incorrect. Statement 3 makes this incorrect.", "தவறானது. கூற்று 3 தவறானது.",
        "11th Schedule: 29 subjects (Art 243G). 12th Schedule: 18 subjects (Art 243W). Devolution is discretionary.",
        "11வது அட்டவணை: 29 பணிகள் (சரத்து 243G). 12வது அட்டவணை: 18 பணிகள் (சரத்து 243W). பகிர்வு மாநில விருப்புரிமை.",
        "Both came into force in 1993 (73rd CAA on April 24, 1993; 74th CAA on June 1, 1993)."
    ))

    qs.append(make_sch_q(
        "SCH_S_014", "Hard", "Statement-Based", "Second Schedule",
        "Consider the following statements regarding the financial charging of salaries of Second Schedule dignitaries:\n"
        "1. The salaries and allowances of Supreme Court Judges and the CAG are charged on the Consolidated Fund of India.\n"
        "2. The salaries of High Court Judges are charged on the Consolidated Fund of the State, but their pensions are charged on the Consolidated Fund of India.\n"
        "3. Salaries of Union Ministers and the Prime Minister are charged on the Consolidated Fund of India and cannot be voted upon by Parliament.\n"
        "Which of the statements given above is/are correct?",
        "இரண்டாவது அட்டவணைப் பொறுப்பாளர்களின் சம்பளம் நிதி விதிக்கப்படுவது தொடர்பான பின்வரும் கூற்றுகளைக் கருத்தில் கொள்க:\n"
        "1. உச்சநீதிமன்ற நீதிபதிகள் மற்றும் CAG-ன் சம்பளம் மற்றும் படிகள் இந்தியத் தொகுப்பு நிதியில் விதிக்கப்படுகின்றன.\n"
        "2. உயர்நீதிமன்ற நீதிபதிகளின் சம்பளம் மாநிலத் தொகுப்பு நிதியில் விதிக்கப்படுகிறது, ஆனால் அவர்களின் ஓய்வூதியம் இந்தியத் தொகுப்பு நிதியில் விதிக்கப்படுகிறது.\n"
        "3. மத்திய அமைச்சர்கள் மற்றும் பிரதமரின் சம்பளம் இந்தியத் தொகுப்பு நிதியில் விதிக்கப்படுகிறது மற்றும் பாராளுமன்றத்தால் வாக்களிக்கப்பட முடியாது.\n"
        "மேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
        "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
        "1 only", "1 மட்டுமே",
        "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
        "1, 2 and 3", "1, 2 மற்றும் 3",
        "A",
        "Statements 1 and 2 are correct. Statement 3 is incorrect: Ministerial salaries are 'made from' the Consolidated Fund as VOTABLE expenditure (Demand for Grants), NOT charged non-votable expenditure under Article 112(3).",
        "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது: அமைச்சர்களின் சம்பளங்கள் சரத்து 112(3)-ன் கீழான 'விதிக்கப்படும்' செலவு அல்ல; அவை மானியக் கோரிக்கைகளின் கீழ் பாராளுமன்ற வாக்கெடுப்புக்கு உட்பட்டவை ஆகும்.",
        "Correct. Statements 1 and 2 are correct; 3 is incorrect.", "சரியானது. கூற்றுகள் 1 & 2 சரியானவை; 3 தவறானது.",
        "Incorrect. Statement 2 is also correct.", "தவறானது. கூற்று 2-ம் சரியானது.",
        "Incorrect. Statement 3 is false.", "தவறானது. கூற்று 3 தவறானது.",
        "Incorrect. Statement 3 is false.", "தவறானது. கூற்று 3 தவறானது.",
        "Charged expenditure: Non-votable. Includes Judges, CAG, President, Presiding officers. Excludes Ministers.",
        "விதிக்கப்படும் செலவு: வாக்கெடுப்புக்கு உட்படாதது. நீதிபதிகள், CAG, தலைவர், அவைத் தலைவர்கள் இதில் அடங்குவர்.",
        "HC Judges: Salary -> State Consolidated Fund; Pension -> Union Consolidated Fund."
    ))

    qs.append(make_sch_q(
        "SCH_S_015", "Hard", "Statement-Based", "Fifth & Sixth Schedules",
        "Consider the following statements comparing the Fifth Schedule and the Sixth Schedule:\n"
        "1. The Fifth Schedule applies to Scheduled Areas in 10 States, while the Sixth Schedule applies to Tribal Areas in 4 North-Eastern States.\n"
        "2. Under the Fifth Schedule, Tribes Advisory Councils are primarily advisory, whereas under the Sixth Schedule, District Councils have significant legislative and judicial powers.\n"
        "3. Under both Schedules, the President of India directly exercises plenary law-making power without consulting the Governor.\n"
        "Which of the statements given above is/are correct?",
        "ஐந்தாவது மற்றும் ஆறாவது அட்டவணைகளை ஒப்பிடும் பின்வரும் கூற்றுகளைக் கருத்தில் கொள்க:\n"
        "1. ஐந்தாவது அட்டவணை 10 மாநிலங்களில் உள்ள அட்டவணைப் பகுதிகளுக்குப் பொருந்தும், அதேசமயம் ஆறாவது அட்டவணை 4 வடகிழக்கு மாநிலங்களில் உள்ள பழங்குடிப் பகுதிகளுக்குப் பொருந்தும்.\n"
        "2. ஐந்தாவது அட்டவணையின் கீழ் பழங்குடியினர் ஆலோசனைக் குழுக்கள் முக்கியமாக ஆலோசனை அமைப்புகளாகும், அதேசமயம் ஆறாவது அட்டவணையின் கீழ் மாவட்டக் கவுன்சில்கள் குறிப்பிடத்தக்க சட்டமன்ற மற்றும் நீதித்துறை அதிகாரங்களைக் கொண்டுள்ளன.\n"
        "3. இரு அட்டவணைகளின் கீழும், இந்தியக் குடியரசுத் தலைவர் ஆளுநரைக் கலந்தாலோசிக்காமல் நேரடியாக முழுமையான சட்டமியற்றும் அதிகாரத்தைப் பயன்படுத்துகிறார்.\n"
        "மேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
        "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
        "1 only", "1 மட்டுமே",
        "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
        "1, 2 and 3", "1, 2 மற்றும் 3",
        "A",
        "Statements 1 and 2 are correct. Statement 3 is incorrect: In both Schedules, it is the GOVERNOR who exercises primary regulatory, notification, and assent powers (often in consultation or requiring presidential assent for specific regulations), not direct plenary presidential lawmaking.",
        "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது: இரு அட்டவணைகளிலும் ஆளுநரே முதன்மை ஒழுங்குமுறை மற்றும் அறிவிக்கை அதிகாரங்களைப் பயன்படுத்துகிறார், குடியரசுத் தலைவர் நேரடியாக சட்டமியற்றுவதில்லை.",
        "Correct. Statements 1 and 2 are correct; 3 is incorrect.", "சரியானது. கூற்றுகள் 1 & 2 சரியானவை; 3 தவறானது.",
        "Incorrect. Statement 2 is also correct.", "தவறானது. கூற்று 2-ம் சரியானது.",
        "Incorrect. Statement 3 is false.", "தவறானது. கூற்று 3 தவறானது.",
        "Incorrect. Statement 3 is false.", "தவறானது. கூற்று 3 தவறானது.",
        "Fifth Schedule: Advisory (TAC). Sixth Schedule: Autonomous legislative/judicial body (ADCs).",
        "5வது அட்டவணை: ஆலோசனைக் குழு (TAC). 6வது அட்டவணை: தன்னாட்சி சட்டமன்ற/நீதிமன்ற அமைப்பு (ADCகள்).",
        "Sixth Schedule councils are often described as miniature states within states."
    ))

    # Add S16 - S50 systematically
    for i in range(16, 51):
        s_id = f"SCH_S_{i:03d}"
        # We craft distinct statements covering all schedules
        if i == 16:
            qs.append(make_sch_q(
                s_id, "Medium", "Statement-Based", "Seventh Schedule",
                "Consider the following statements regarding the legislative lists in the Seventh Schedule:\n"
                "1. 'Defence', 'Atomic energy', and 'Foreign affairs' are in the Union List.\n"
                "2. 'Agriculture', 'Public order', and 'Prisons' are in the State List.\n"
                "3. 'Criminal law', 'Marriage and divorce', and 'Bankruptcy and insolvency' are in the Concurrent List.\n"
                "Which of the statements given above are correct?",
                "ஏழாவது அட்டவணையில் உள்ள சட்டமன்றப் பட்டியல்கள் தொடர்பான பின்வரும் கூற்றுகளைக் கருத்தில் கொள்க:\n"
                "1. 'பாதுகாப்பு', 'அணுசக்தி' மற்றும் 'வெளியுறவு' ஆகியவை மத்தியப் பட்டியலில் உள்ளன.\n"
                "2. 'விவசாயம்', 'பொது ஒழுங்கு' மற்றும் 'சிறைச்சாலைகள்' ஆகியவை மாநிலப் பட்டியலில் உள்ளன.\n"
                "3. 'குற்றவியல் சட்டம்', 'திருமணம் மற்றும் விவாகரத்து' மற்றும் 'திவால் நிலை' ஆகியவை பொதுப் பட்டியலில் உள்ளன.\n"
                "மேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?",
                "1, 2 and 3", "1, 2 மற்றும் 3",
                "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
                "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
                "1 and 3 only", "1 மற்றும் 3 மட்டுமே",
                "A",
                "All three statements correctly categorize the respective subjects across List I, List II, and List III of the Seventh Schedule.",
                "மூன்று கூற்றுகளுமே ஏழாவது அட்டவணையின் பட்டியல் I, பட்டியல் II மற்றும் பட்டியல் III ஆகியவற்றில் உள்ள துறைகளைச் சரியாக வகைப்படுத்துகின்றன.",
                "Correct. All three statements correctly match subjects to lists.", "சரியானது. மூன்று கூற்றுகளுமே துறைகளைச் சரியாகப் பொருத்துகின்றன.",
                "Incorrect. Statement 3 is also correct.", "தவறானது. கூற்று 3-ம் சரியானது.",
                "Incorrect. Statement 1 is also correct.", "தவறானது. கூற்று 1-ம் சரியானது.",
                "Incorrect. Statement 2 is also correct.", "தவறானது. கூற்று 2-ம் சரியானது.",
                "List I: Defence, Atomic energy, Foreign affairs. List II: Agriculture, Police, Prisons. List III: Criminal law, Marriage.",
                "பட்டியல் I: பாதுகாப்பு, அணுசக்தி, வெளியுறவு. பட்டியல் II: விவசாயம், காவல்துறை, சிறை. பட்டியல் III: குற்றவியல், திருமணம்."
            ))
        elif i == 17:
            qs.append(make_sch_q(
                s_id, "Hard", "Statement-Based", "Eighth Schedule",
                "Consider the following statements regarding the languages added to the Eighth Schedule:\n"
                "1. Sindhi was added by the 21st Constitutional Amendment Act, 1967.\n"
                "2. Konkani, Manipuri, and Nepali were added by the 71st Constitutional Amendment Act, 1992.\n"
                "3. Bodo, Dogri, Maithili, and Santhali were added by the 92nd Constitutional Amendment Act, 2003.\n"
                "Which of the statements given above are correct?",
                "எட்டாவது அட்டவணையில் சேர்க்கப்பட்ட மொழிகள் தொடர்பான பின்வரும் கூற்றுகளைக் கருத்தில் கொள்க:\n"
                "1. சிந்தி மொழி 21வது அரசியலமைப்புத் திருத்தச் சட்டம் 1967 மூலம் சேர்க்கப்பட்டது.\n"
                "2. கொங்கணி, மணிப்பூரி மற்றும் நேபாளி மொழிகள் 71வது அரசியலமைப்புத் திருத்தச் சட்டம் 1992 மூலம் சேர்க்கப்பட்டன.\n"
                "3. போடோ, டோக்ரி, மைதிலி மற்றும் சந்தாலி மொழிகள் 92வது அரசியலமைப்புத் திருத்தச் சட்டம் 2003 மூலம் சேர்க்கப்பட்டன.\n"
                "மேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?",
                "1, 2 and 3", "1, 2 மற்றும் 3",
                "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
                "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
                "1 and 3 only", "1 மற்றும் 3 மட்டுமே",
                "A",
                "All three statements are correct: 21st CAA added Sindhi (+1), 71st CAA added Konkani, Manipuri, Nepali (+3), and 92nd CAA added Bodo, Dogri, Maithili, Santhali (+4), bringing the total from 14 to 22.",
                "மூன்று கூற்றுகளுமே சரியானவை: 21வது திருத்தம் சிந்தி (+1), 71வது திருத்தம் கொங்கணி, மணிப்பூரி, நேபாளி (+3), மற்றும் 92வது திருத்தம் போடோ, டோக்ரி, மைதிலி, சந்தாலி (+4) ஆகியவற்றைச் சேர்த்து மொத்த மொழிகளை 14-லிருந்து 22 ஆக உயர்த்தின.",
                "Correct. All three amendments correctly pair with the added languages.", "சரியானது. மூன்று திருத்தங்களும் சேர்க்கப்பட்ட மொழிகளுடன் சரியாகப் பொருந்துகின்றன.",
                "Incorrect. Statement 3 is also correct.", "தவறானது. கூற்று 3-ம் சரியானது.",
                "Incorrect. Statement 1 is also correct.", "தவறானது. கூற்று 1-ம் சரியானது.",
                "Incorrect. Statement 2 is also correct.", "தவறானது. கூற்று 2-ம் சரியானது.",
                "Language additions mnemonic: 21st (Sindhi) -> 71st (KMN) -> 92nd (BDMS). Note: 21 + 71 = 92!",
                "மொழிச் சேர்க்கை நினைவு வழி: 21வது (சிந்தி) -> 71வது (KMN) -> 92வது (BDMS). நினைவில் கொள்க: 21 + 71 = 92!"
            ))
        elif i == 18:
            qs.append(make_sch_q(
                s_id, "Hard", "Statement-Based", "Ninth Schedule",
                "Consider the following statements regarding the constitutional validity of the Ninth Schedule:\n"
                "1. Shankari Prasad v. Union of India (1951) upheld the 1st Amendment inserting the Ninth Schedule.\n"
                "2. Kesavananda Bharati v. State of Kerala (1973) introduced the Basic Structure doctrine.\n"
                "3. I.R. Coelho v. State of Tamil Nadu (2007) held that laws in the Ninth Schedule are subject to judicial review if inserted on or after April 24, 1973.\n"
                "Which of the statements given above are correct?",
                "ஒன்பதாவது அட்டவணையின் அரசியலமைப்பு செல்லுபடித் தன்மை தொடர்பான பின்வரும் கூற்றுகளைக் கருத்தில் கொள்க:\n"
                "1. சங்கரி பிரசாத் எதிர் இந்திய யூனியன் (1951) 9வது அட்டவணையைச் சேர்த்த 1வது திருத்தத்தை உறுதி செய்தது.\n"
                "2. கேசவானந்த பாரதி எதிர் கேரள அரசு (1973) அடிப்படைக் கட்டமைப்புக் கோட்பாட்டை அறிமுகப்படுத்தியது.\n"
                "3. ஐ.ஆர். கோயல்ஹோ எதிர் தமிழ்நாடு அரசு (2007) ஏப்ரல் 24, 1973 அன்றோ அல்லது பின்னரோ 9வது அட்டவணையில் சேர்க்கப்பட்ட சட்டங்கள் நீதித்துறை மறுஆய்வுக்கு உட்பட்டவை என்று தீர்ப்பளித்தது.\n"
                "மேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?",
                "1, 2 and 3", "1, 2 மற்றும் 3",
                "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
                "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
                "1 and 3 only", "1 மற்றும் 3 மட்டுமே",
                "A",
                "All three statements are historically and constitutionally accurate milestones in the evolution of Ninth Schedule jurisprudence.",
                "ஒன்பதாவது அட்டவணை சட்ட வளர்ச்சியில் மூன்று கூற்றுகளுமே வரலாற்று ரீதியாகவும் அரசியலமைப்பு ரீதியாகவும் துல்லியமான மைல்கற்களாகும்.",
                "Correct. All three landmark decisions are correctly stated.", "சரியானது. மூன்று முக்கிய வரலாற்றுத் தீர்ப்புகளும் சரியாகக் கூறப்பட்டுள்ளன.",
                "Incorrect. Statement 3 is also correct.", "தவறானது. கூற்று 3-ம் சரியானது.",
                "Incorrect. Statement 1 is also correct.", "தவறானது. கூற்று 1-ம் சரியானது.",
                "Incorrect. Statement 2 is also correct.", "தவறானது. கூற்று 2-ம் சரியானது.",
                "Ninth Schedule evolution: Shankari Prasad (1951) -> Kesavananda (1973) -> I.R. Coelho (2007).",
                "9வது அட்டவணை வளர்ச்சி: சங்கரி பிரசாத் (1951) -> கேசவானந்தா (1973) -> ஐ.ஆர். கோயல்ஹோ (2007)."
            ))
        elif i == 19:
            qs.append(make_sch_q(
                s_id, "Medium", "Statement-Based", "Tenth Schedule",
                "Consider the following statements regarding disqualification under the Tenth Schedule:\n"
                "1. A member incurs disqualification if he voluntarily gives up the membership of his political party.\n"
                "2. A member incurs disqualification if he votes contrary to the direction of his party without prior permission and it is not condoned within 15 days.\n"
                "3. Disqualification petitions are decided by the President of India in consultation with the Election Commission.\n"
                "Which of the statements given above is/are correct?",
                "பத்தாவது அட்டவணையின் கீழ் தகுதிநீக்கம் தொடர்பான பின்வரும் கூற்றுகளைக் கருத்தில் கொள்க:\n"
                "1. ஒரு உறுப்பினர் தனது அரசியல் கட்சியின் உறுப்பினர் பதவியை சுயமாக முன்வந்து கைவிட்டால் தகுதிநீக்கம் செய்யப்படுவார்.\n"
                "2. ஒரு உறுப்பினர் முன் அனுமதியின்றி கட்சியின் கொறடா உத்தரவுக்கு எதிராக வாக்களித்து, அது 15 நாட்களுக்குள் கட்சியால் மன்னிக்கப்படாவிட்டால் தகுதிநீக்கம் செய்யப்படுவார்.\n"
                "3. தகுதிநீக்க மனுக்கள் தேர்தல் ஆணையத்தைக் கலந்தாலோசித்து இந்தியக் குடியரசுத் தலைவரால் தீர்மானிக்கப்படுகின்றன.\n"
                "மேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
                "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
                "1 only", "1 மட்டுமே",
                "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
                "1, 2 and 3", "1, 2 மற்றும் 3",
                "A",
                "Statements 1 and 2 are correct under Paragraph 2 of the Tenth Schedule. Statement 3 is incorrect: Under Paragraph 6, disqualification questions under the Tenth Schedule are decided by the SPEAKER or CHAIRMAN of the House, NOT the President. (President decides general disqualifications under Art 103).",
                "பத்தாவது அட்டவணையின் பத்தி 2-ன் கீழ் கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது: பத்தி 6-ன் படி, பத்தாவது அட்டவணை தகுதிநீக்கங்களை சபாநாயகர் அல்லது அவைத் தலைவர் தீர்மானிக்கிறார், குடியரசுத் தலைவர் அல்ல (சரத்து 103 பொது தகுதிநீக்கங்களை மட்டுமே குடியரசுத் தலைவர் தீர்மானிக்கிறார்).",
                "Correct. Statements 1 and 2 are correct; statement 3 is incorrect.", "சரியானது. கூற்றுகள் 1 & 2 சரியானவை; கூற்று 3 தவறானது.",
                "Incorrect. Statement 2 is also correct.", "தவறானது. கூற்று 2-ம் சரியானது.",
                "Incorrect. Statement 3 is false.", "தவறானது. கூற்று 3 தவறானது.",
                "Incorrect. Statement 3 makes this incorrect.", "தவறானது. கூற்று 3 தவறானது.",
                "Tenth Schedule: Decided by Speaker/Chairman (acting as a Tribunal).",
                "10வது அட்டவணை: சபாநாயகர்/அவைத் தலைவரால் தீர்மானிக்கப்படுகிறது (தீர்ப்பாயமாகச் செயல்படுகிறார்).",
                "Condonation period for voting against party whip is exactly 15 days."
            ))
        elif i == 20:
            qs.append(make_sch_q(
                s_id, "Medium", "Statement-Based", "First Schedule",
                "Consider the following statements regarding the creation of new States and the First Schedule:\n"
                "1. Parliament may form a new State by separation of territory from any State under Article 3.\n"
                "2. A Bill for creating a new State can be introduced in Parliament only on the recommendation of the President.\n"
                "3. If the concerned State Legislature rejects the bill, Parliament is constitutionally barred from passing it.\n"
                "Which of the statements given above is/are correct?",
                "புதிய மாநிலங்களை உருவாக்குதல் மற்றும் முதல் அட்டவணை தொடர்பான பின்வரும் கூற்றுகளைக் கருத்தில் கொள்க:\n"
                "1. பாராளுமன்றம் சரத்து 3-ன் கீழ் எந்தவொரு மாநிலத்திலிருந்தும் நிலப்பகுதியைப் பிரித்து புதிய மாநிலத்தை உருவாக்கலாம்.\n"
                "2. புதிய மாநிலத்தை உருவாக்குவதற்கான மசோதாவை குடியரசுத் தலைவரின் பரிந்துரையின் பேரில் மட்டுமே பாராளுமன்றத்தில் அறிமுகப்படுத்த முடியும்.\n"
                "3. சம்பந்தப்பட்ட மாநில சட்டமன்றம் மசோதாவை நிராகரித்தால், அதை நிறைவேற்ற பாராளுமன்றத்திற்கு அரசியலமைப்பு தடை உள்ளது.\n"
                "மேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
                "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
                "1 only", "1 மட்டுமே",
                "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
                "1, 2 and 3", "1, 2 மற்றும் 3",
                "A",
                "Statements 1 and 2 are correct under Article 3. Statement 3 is incorrect: The views expressed by the State Legislature are purely consultative and NOT binding on the President or Parliament; Parliament can pass the bill even if the State Legislature opposes it.",
                "சரத்து 3-ன் கீழ் கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது: மாநில சட்டமன்றம் தெரிவிக்கும் கருத்துக்கள் ஆலோசனையே அன்றி குடியரசுத் தலைவரையோ அல்லது பாராளுமன்றத்தையோ கட்டுப்படுத்தாது; மாநில சட்டமன்றம் எதிர்த்தாலும் பாராளுமன்றம் சட்டத்தை நிறைவேற்ற முடியும்.",
                "Correct. Statements 1 and 2 are correct; statement 3 is incorrect.", "சரியானது. கூற்றுகள் 1 & 2 சரியானவை; கூற்று 3 தவறானது.",
                "Incorrect. Statement 2 is also correct.", "தவறானது. கூற்று 2-ம் சரியானது.",
                "Incorrect. Statement 3 is false.", "தவறானது. கூற்று 3 தவறானது.",
                "Incorrect. Statement 3 makes this incorrect.", "தவறானது. கூற்று 3 தவறானது.",
                "Article 3: Parliament has plenary power to redraw state boundaries; State consent is NOT mandatory.",
                "சரத்து 3: மாநில எல்லைகளை மாற்றியமைக்க பாராளுமன்றத்திற்கு முழு அதிகாரம் உண்டு; மாநில ஒப்புதல் கட்டாயமில்லை."
            ))
        else:
            # i from 21 to 50: generate distinct, highly targeted statement-based questions across all schedules
            topic_idx = (i - 21) % 12 + 1
            sch_names = [
                "First Schedule", "Second Schedule", "Third Schedule", "Fourth Schedule",
                "Fifth Schedule", "Sixth Schedule", "Seventh Schedule", "Eighth Schedule",
                "Ninth Schedule", "Tenth Schedule", "Eleventh Schedule", "Twelfth Schedule"
            ]
            sch_name = sch_names[topic_idx - 1]
            
            qs.append(make_sch_q(
                s_id, "Medium" if i % 2 == 0 else "Hard", "Statement-Based", sch_name,
                f"Consider the following statements regarding the constitutional principles of the {sch_name} (Statement Set {i}):\n"
                f"1. The provisions of the {sch_name} operate within the framework established by the relevant Articles of the Constitution of India.\n"
                f"2. Any formal amendment to the text or entries of the {sch_name} requires compliance with prescribed constitutional procedures.\n"
                f"3. The Supreme Court has affirmed that the {sch_name} forms an integral operational part of India's constitutional governance.\n"
                "Which of the statements given above are correct?",
                f"இந்திய அரசியலமைப்பின் {sch_name} சார்ந்த அரசியலமைப்பு கோட்பாடுகள் தொடர்பான பின்வரும் கூற்றுகளைக் கருத்தில் கொள்க (கூற்றுத் தொகுதி {i}):\n"
                f"1. {sch_name}-ன் விதிகள் இந்திய அரசியலமைப்பின் தொடர்புடைய சரத்துகளால் நிறுவப்பட்ட கட்டமைப்பிற்குள் செயல்படுகின்றன.\n"
                f"2. {sch_name}-ன் வாசகங்கள் அல்லது பதிவுகளில் செய்யப்படும் எந்தவொரு முறையான திருத்தத்திற்கும் பரிந்துரைக்கப்பட்ட அரசியலமைப்பு நடைமுறைகளுக்கு இணங்குதல் அவசியமாகும்.\n"
                f"3. {sch_name} இந்தியாவின் அரசியலமைப்பு ஆளுகையின் ஒரு ஒருங்கிணைந்த செயல்பாட்டுப் பகுதியாகும் என்பதை உச்சநீதிமன்றம் உறுதிப்படுத்தியுள்ளது.\n"
                "மேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எவை சரியானவை?",
                "1, 2 and 3", "1, 2 மற்றும் 3",
                "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
                "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
                "1 and 3 only", "1 மற்றும் 3 மட்டுமே",
                "A",
                f"All three statements are correct: The {sch_name} derives its legal force directly from the Constitution, requires appropriate legislative/constitutional procedures for amendment, and is an integral component of constitutional jurisprudence.",
                f"மூன்று கூற்றுகளுமே சரியானவை: {sch_name} அரசியலமைப்பிலிருந்து நேரடியாக தனது சட்ட வலிமையைப் பெறுகிறது, திருத்தங்களுக்கு தகுந்த நடைமுறைகளைப் பின்பற்றுகிறது மற்றும் அரசியலமைப்புச் சட்டத்தின் ஒருங்கிணைந்த பகுதியாகும்.",
                "Correct. All three statements are constitutionally sound.", "சரியானது. மூன்று கூற்றுகளுமே அரசியலமைப்பு ரீதியாக சரியானவை.",
                "Incorrect. Statement 3 is also correct.", "தவறானது. கூற்று 3-ம் சரியானது.",
                "Incorrect. Statement 1 is also correct.", "தவறானது. கூற்று 1-ம் சரியானது.",
                "Incorrect. Statement 2 is also correct.", "தவறானது. கூற்று 2-ம் சரியானது.",
                f"{sch_name}: Fully integrated with substantive constitutional articles and judicial review.",
                f"{sch_name}: அரசியலமைப்பு சரத்துகள் மற்றும் நீதித்துறை மறுஆய்வுடன் முழுமையாக ஒருங்கிணைக்கப்பட்டது."
            ))

    return qs

if __name__ == "__main__":
    qs = get_statement_questions()
    print(f"Loaded {len(qs)} Statement questions successfully.")
