from mic_pyq_part1 import make_pyq_q

questions = []

# MIC_PYQ_041 (Chronology)
questions.append(make_pyq_q(
    "MIC_PYQ_041", "Chronology",
    "Arrange the following historical developments regarding the demand for a Constituent Assembly in correct chronological order:\n1. M.N. Roy puts forward the idea of a Constituent Assembly for India\n2. Indian National Congress officially demands a Constituent Assembly for the first time\n3. Jawaharlal Nehru declares that the Constitution of free India must be framed by a Constituent Assembly elected on adult franchise\n4. British Government accepts the demand for a Constituent Assembly in principle in the August Offer",
    "இந்தியாவிற்கான அரசியலமைப்பு நிர்ணய அவைக் கோரிக்கை பற்றிய பின்வரும் வரலாற்று முன்னேற்றங்களை சரியான காலவரிசையில் அமைக்கவும்:\n1. எம்.என். ராய் முதன்முதலில் இந்தியாவிற்கான அரசியலமைப்பு நிர்ணய அவைக் கருத்தை முன்வைத்தார்\n2. இந்திய தேசிய காங்கிரஸ் முதன்முறையாக அரசியலமைப்பு நிர்ணய அவையைக் கோரி அதிகாரப்பூர்வமாக கோரிக்கை விடுத்தது\n3. சுதந்திர இந்தியாவின் அரசியலமைப்பு வயதுவந்தோர் வாக்குரிமையால் தேர்ந்தெடுக்கப்பட்ட அவையால் உருவாக்கப்பட வேண்டும் என ஜவகர்லால் நேரு அறிவித்தார்\n4. பிரிட்டிஷ் அரசாங்கம் ஆகஸ்ட் சலுகையில் கொள்கையளவில் அவைக் கோரிக்கையை ஏற்றுக்கொண்டது",
    ["1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "3 -> 1 -> 2 -> 4"],
    ["1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "3 -> 1 -> 2 -> 4"],
    "A",
    "Correct Chronological Sequence: 1 (M.N. Roy, 1934) -> 2 (INC official demand, 1935) -> 3 (Nehru declaration, 1938) -> 4 (August Offer, 1940).",
    "சரியான காலவரிசை: 1 (எம்.என். ராய், 1934) -> 2 (காங்கிரஸ் கோரிக்கை, 1935) -> 3 (நேரு அறிவிப்பு, 1938) -> 4 (ஆகஸ்ட் சலுகை, 1940).",
    "Correct. 1 (1934) -> 2 (1935) -> 3 (1938) -> 4 (1940) is exact.", "சரி. 1 (1934) -> 2 (1935) -> 3 (1938) -> 4 (1940) துல்லியமானது.",
    "Incorrect. M.N. Roy proposed the idea in 1934 (1) before INC demand in 1935 (2).", "தவறு. எம்.என். ராய் 1934 இல் முன்மொழிந்தார் (1).",
    "Incorrect. INC demand was in 1935 (2) before Nehru's declaration in 1938 (3).", "தவறு. காங்கிரஸ் 1935 இல் கோரியது (2).",
    "Incorrect. M.N. Roy proposed the idea in 1934 (1).", "தவறு. எம்.என். ராய் 1934 இல் முன்மொழிந்தார் (1).",
    "TNPSC Trap: M.N. Roy (1934) -> INC Demand (1935) -> Nehru Demand (1938) -> August Offer (1940).",
    "TNPSC பொறி: எம்.என். ராய் (1934) -> காங்கிரஸ் கோரிக்கை (1935) -> நேரு கோரிக்கை (1938) -> ஆகஸ்ட் சலுகை (1940).",
    "August Offer was announced by Viceroy Lord Linlithgow on August 8, 1940.",
    "ஆகஸ்ட் சலுகை வைஸ்ராய் லின்லித்கோ பிரபுவால் ஆகஸ்ட் 8, 1940 இல் அறிவிக்கப்பட்டது.",
    "Medium", "Analyze", 60, ["Polity", "Making of Indian Constitution", "Demand for Constituent Assembly", "August Offer"],
    events=[{"id": "1", "en": "M.N. Roy idea (1934)", "ta": "எம்.என். ராய் கருத்து (1934)"}, {"id": "2", "en": "INC official demand (1935)", "ta": "காங்கிரஸ் கோரிக்கை (1935)"}, {"id": "3", "en": "Nehru declaration (1938)", "ta": "நேரு அறிவிப்பு (1938)"}, {"id": "4", "en": "August Offer (1940)", "ta": "ஆகஸ்ட் சலுகை (1940)"}]
))

# MIC_PYQ_042 (Chronology)
questions.append(make_pyq_q(
    "MIC_PYQ_042", "Chronology",
    "Which one of the following is the correct chronological sequence of British missions and proposals sent to India?\n1. August Offer by Viceroy Linlithgow\n2. Cripps Mission headed by Sir Stafford Cripps\n3. Arrival of Cabinet Mission in New Delhi\n4. Announcement of Cabinet Mission Plan",
    "இந்தியாவிற்கு அனுப்பப்பட்ட பிரிட்டிஷ் தூதுக்குழுக்கள் மற்றும் திட்டங்களின் சரியான காலவரிசை எது?\n1. வைஸ்ராய் லின்லித்கோவின் ஆகஸ்ட் சலுகை\n2. சர் ஸ்டாஃபோர்ட் கிரிப்ஸ் தலைமையிலான கிரிப்ஸ் தூதுக்குழு\n3. புதுடெல்லியில் கேபினட் தூதுக்குழு வருகை\n4. கேபினட் தூதுக்குழு திட்டம் அறிவிக்கப்படுதல்",
    ["1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "3 -> 1 -> 2 -> 4"],
    ["1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "3 -> 1 -> 2 -> 4"],
    "A",
    "Correct Chronological Sequence: 1 (August Offer, Aug 1940) -> 2 (Cripps Mission, March 1942) -> 3 (Cabinet Mission Arrival, March 24, 1946) -> 4 (Cabinet Mission Plan, May 16, 1946).",
    "சரியான காலவரிசை: 1 (ஆகஸ்ட் சலுகை, ஆகஸ்ட் 1940) -> 2 (கிரிப்ஸ் திட்டம், மார்ச் 1942) -> 3 (கேபினட் வருகை, மார்ச் 24, 1946) -> 4 (கேபினட் திட்டம், மே 16, 1946).",
    "Correct. 1 (1940) -> 2 (1942) -> 3 (March 1946) -> 4 (May 1946) is exact.", "சரி. 1 (1940) -> 2 (1942) -> 3 (மார்ச் 1946) -> 4 (மே 1946) துல்லியமானது.",
    "Incorrect. August Offer (1940) preceded Cripps Mission (1942).", "தவறு. ஆகஸ்ட் சலுகை (1940) கிரிப்ஸ் திட்டத்திற்கு முந்தியது (1942).",
    "Incorrect. Cripps Mission (1942) preceded Cabinet Mission (1946).", "தவறு. கிரிப்ஸ் திட்டம் (1942) கேபினட் தூதுக்குழுவிற்கு முந்தியது.",
    "Incorrect. Cabinet Mission arrived in March 1946 (3).", "தவறு. கேபினட் தூதுக்குழு மார்ச் 1946 இல் வந்தது (3).",
    "TNPSC Trap: Cabinet Mission arrived in Delhi on March 24, 1946, and published its plan on May 16, 1946.",
    "TNPSC பொறி: கேபினட் தூதுக்குழு மார்ச் 24, 1946 இல் டெல்லி வந்தது, மே 16, 1946 இல் திட்டத்தை வெளியிட்டது.",
    "Gandhiji called Cripps Mission proposals 'a post-dated cheque on a crashing bank'.",
    "காந்தியடிகள் கிரிப்ஸ் திட்டத்தை 'நொடித்துப்போகும் வங்கியின் பின்நாளிட்ட காசோலை' என்றார்.",
    "Medium", "Analyze", 60, ["Polity", "Making of Indian Constitution", "August Offer", "Cripps Mission", "Cabinet Mission Plan"],
    events=[{"id": "1", "en": "August Offer (1940)", "ta": "ஆகஸ்ட் சலுகை (1940)"}, {"id": "2", "en": "Cripps Mission (1942)", "ta": "கிரிப்ஸ் திட்டம் (1942)"}, {"id": "3", "en": "Cabinet Mission arrival (March 1946)", "ta": "கேபினட் தூதுக்குழு வருகை (மார்ச் 1946)"}, {"id": "4", "en": "Cabinet Mission plan (May 1946)", "ta": "கேபினட் தூதுக்குழு திட்டம் (மே 1946)"}]
))

# MIC_PYQ_043 (Chronology)
questions.append(make_pyq_q(
    "MIC_PYQ_043", "Chronology",
    "Identify the correct chronological order of Constituent Assembly events in 1946:\n1. Completion of Assembly elections for British Indian seats\n2. Formation of the Interim Government headed by Jawaharlal Nehru\n3. First meeting of the Constituent Assembly attended by 211 members\n4. Dr. Rajendra Prasad elected as permanent President of the Assembly",
    "1946 இல் அரசியலமைப்பு அவையின் நிகழ்வுகளின் சரியான காலவரிசையை அடையாளம் காணவும்:\n1. பிரிட்டிஷ் இந்திய இடங்களுக்கான அவைத் தேர்தல்கள் நிறைவடைதல்\n2. ஜவகர்லால் நேரு தலைமையில் இடைக்கால அரசு அமைக்கப்படுதல்\n3. 211 உறுப்பினர்கள் பங்கேற்ற அரசியலமைப்பு அவையின் முதல் கூட்டம்\n4. டாக்டர் ராஜேந்திர பிரசாத் அவையின் நிரந்தரத் தலைவராகத் தேர்ந்தெடுக்கப்படுதல்",
    ["1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "3 -> 1 -> 2 -> 4"],
    ["1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "3 -> 1 -> 2 -> 4"],
    "A",
    "Correct Chronological Sequence: 1 (Assembly Elections, July-Aug 1946) -> 2 (Interim Govt, Sept 2, 1946) -> 3 (First Meeting, Dec 9, 1946) -> 4 (Dr. Rajendra Prasad elected, Dec 11, 1946).",
    "சரியான காலவரிசை: 1 (தேர்தல், ஜூலை-ஆகஸ்ட் 1946) -> 2 (இடைக்கால அரசு, செப் 2, 1946) -> 3 (முதல் கூட்டம், டிச 9, 1946) -> 4 (ராஜேந்திர பிரசாத் தேர்வு, டிச 11, 1946).",
    "Correct. 1 (July-Aug 1946) -> 2 (Sept 2, 1946) -> 3 (Dec 9, 1946) -> 4 (Dec 11, 1946) is exact.", "சரி. 1 (ஜூலை-ஆகஸ்ட் 1946) -> 2 (செப் 2, 1946) -> 3 (டிச 9, 1946) -> 4 (டிச 11, 1946) துல்லியமானது.",
    "Incorrect. Elections (July-Aug) occurred before Interim Govt (Sept 2).", "தவறு. அவைத் தேர்தல் (ஜூலை-ஆகஸ்ட்) இடைக்கால அரசிற்கு முந்தியது (செப் 2).",
    "Incorrect. Interim Govt (Sept 2) was formed before First Meeting (Dec 9).", "தவறு. இடைக்கால அரசு (செப் 2) முதல் கூட்டத்திற்கு முந்தியது (டிச 9).",
    "Incorrect. Elections (1) occurred before First Meeting (3).", "தவறு. அவைத் தேர்தல் (1) முதல் கூட்டத்திற்கு முந்தியது (3).",
    "TNPSC Trap: Assembly Elections = July-Aug 1946. Interim Govt = Sept 2, 1946. First Meeting = Dec 9, 1946. Rajendra Prasad elected = Dec 11, 1946.",
    "TNPSC பொறி: அவைத் தேர்தல் = ஜூலை-ஆகஸ்ட் 1946. இடைக்கால அரசு = செப்டம்பர் 2, 1946. முதல் கூட்டம் = டிசம்பர் 9, 1946. ராஜேந்திர பிரசாத் தேர்வு = டிசம்பர் 11, 1946.",
    "Dr. Sachchidananda Sinha served as Temporary President for 2 days (Dec 9-10, 1946).",
    "டாக்டர் சச்சிதானந்த சின்ஹா 2 நாட்கள் (டிசம்பர் 9-10, 1946) தற்காலிகத் தலைவராகப் பணியாற்றினார்.",
    "Medium", "Analyze", 60, ["Polity", "Making of Indian Constitution", "Constituent Assembly Election", "First Meeting", "Permanent President"],
    events=[{"id": "1", "en": "Assembly elections (July-Aug 1946)", "ta": "அவைத் தேர்தல் (ஜூலை-ஆகஸ்ட் 1946)"}, {"id": "2", "en": "Interim Govt (Sept 2, 1946)", "ta": "இடைக்கால அரசு (செப் 2, 1946)"}, {"id": "3", "en": "First Meeting (Dec 9, 1946)", "ta": "முதல் கூட்டம் (டிச 9, 1946)"}, {"id": "4", "en": "Rajendra Prasad elected (Dec 11, 1946)", "ta": "ராஜேந்திர பிரசாத் தேர்வு (டிச 11, 1946)"}]
))

# MIC_PYQ_044 (Chronology)
questions.append(make_pyq_q(
    "MIC_PYQ_044", "Chronology",
    "Arrange the following constitutional milestones in correct chronological order:\n1. Adoption of the National Flag of India by Constituent Assembly\n2. Appointment of the Drafting Committee under Dr. B.R. Ambedkar\n3. Ratification of India's membership of the Commonwealth by Constituent Assembly\n4. Adoption and enactment of the Constitution by Constituent Assembly",
    "பின்வரும் அரசியலமைப்பு மைல்கற்களை சரியான காலவரிசையில் அமைக்கவும்:\n1. அரசியலமைப்பு அவையால் இந்திய தேசியக் கொடி ஏற்றுக்கொள்ளப்படுதல்\n2. அம்பேத்கர் தலைமையில் வரைவுக் குழு நியமிக்கப்படுதல்\n3. காமன்வெல்த்தில் இந்தியாவின் உறுப்பினருரிமையை அரசியலமைப்பு அவை உறுதிப்படுத்துதல்\n4. அரசியலமைப்பு அவையால் அரசியலமைப்பு ஏற்றுக்கொள்ளப்பட்டு இயற்றப்படுதல்",
    ["1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "3 -> 1 -> 2 -> 4"],
    ["1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "3 -> 1 -> 2 -> 4"],
    "A",
    "Correct Chronological Sequence: 1 (National Flag, July 22, 1947) -> 2 (Drafting Committee, Aug 29, 1947) -> 3 (Commonwealth Ratification, May 1949) -> 4 (Constitution Adoption, Nov 26, 1949).",
    "சரியான காலவரிசை: 1 (தேசியக் கொடி, ஜூலை 22, 1947) -> 2 (வரைவுக் குழு, ஆகஸ்ட் 29, 1947) -> 3 (காமன்வெல்த் உறுதிப்பாடு, மே 1949) -> 4 (அரசியலமைப்பு ஏற்பு, நவ 26, 1949).",
    "Correct. 1 (July 1947) -> 2 (Aug 1947) -> 3 (May 1949) -> 4 (Nov 26, 1949) is exact.", "சரி. 1 (ஜூலை 1947) -> 2 (ஆகஸ்ட் 1947) -> 3 (மே 1949) -> 4 (நவ 26, 1949) துல்லியமானது.",
    "Incorrect. National Flag (July 1947) preceded Drafting Committee setup (Aug 1947).", "தவறு. தேசியக் கொடி (ஜூலை 1947) வரைவுக் குழு அமைப்பிற்கு முந்தியது (ஆகஸ்ட் 1947).",
    "Incorrect. Drafting Committee setup (Aug 1947) preceded Commonwealth ratification (May 1949).", "தவறு. வரைவுக் குழு அமைப்பு (ஆகஸ்ட் 1947) காமன்வெல்த் உறுதிப்பாட்டிற்கு முந்தியது.",
    "Incorrect. National Flag (July 1947) was the earliest.", "தவறு. தேசியக் கொடி (ஜூலை 1947) மிக முந்தையது.",
    "TNPSC Trap: Flag Adoption (July 22, 1947) -> Drafting Committee (Aug 29, 1947) -> Commonwealth (May 1949) -> Adoption (Nov 26, 1949).",
    "TNPSC பொறி: கொடி ஏற்பு (ஜூலை 22, 1947) -> வரைவுக் குழு (ஆகஸ்ட் 29, 1947) -> காமன்வெல்த் (மே 1949) -> ஏற்பு (நவ 26, 1949).",
    "India's membership of Commonwealth was ratified in May 1949.",
    "இந்தியாவின் காமன்வெல்த் உறுப்பினருரிமை மே 1949 இல் உறுதிப்படுத்தப்பட்டது.",
    "Medium", "Analyze", 60, ["Polity", "Making of Indian Constitution", "National Flag adoption", "Drafting Committee", "Constitutional Milestones"],
    events=[{"id": "1", "en": "National Flag adoption (July 22, 1947)", "ta": "தேசியக் கொடி ஏற்பு (ஜூலை 22, 1947)"}, {"id": "2", "en": "Drafting Committee (Aug 29, 1947)", "ta": "வரைவுக் குழு (ஆகஸ்ட் 29, 1947)"}, {"id": "3", "en": "Commonwealth ratification (May 1949)", "ta": "காமன்வெல்த் உறுதிப்பாடு (மே 1949)"}, {"id": "4", "en": "Constitution adoption (Nov 26, 1949)", "ta": "அரசியலமைப்பு ஏற்பு (நவ 26, 1949)"}]
))

# MIC_PYQ_045 (Chronology)
questions.append(make_pyq_q(
    "MIC_PYQ_045", "Chronology",
    "Which of the following represents the correct chronological sequence of events leading to the final enforcement of the Constitution?\n1. Adoption and passing of the Constitution by Constituent Assembly\n2. Adoption of National Anthem and National Song by Constituent Assembly\n3. Election of Dr. Rajendra Prasad as first President of India by Constituent Assembly\n4. Commencement of the Constitution and celebration of 1st Republic Day",
    "அரசியலமைப்பின் இறுதிச் செயலாக்கத்திற்கு வழிவகுத்த நிகழ்வுகளின் சரியான காலவரிசை எது?\n1. அரசியலமைப்பு அவையால் அரசியலமைப்பு ஏற்றுக்கொள்ளப்பட்டு நிறைவேற்றப்படுதல்\n2. அரசியலமைப்பு அவையால் தேசிய கீதம் மற்றும் தேசியப் பாடல் ஏற்றுக்கொள்ளப்படுதல்\n3. அரசியலமைப்பு அவையால் டாக்டர் ராஜேந்திர பிரசாத் முதல் குடியரசுத் தலைவராகத் தேர்ந்தெடுக்கப்படுதல்\n4. அரசியலமைப்பு நடைமுறைக்கு வருதல் மற்றும் 1வது குடியரசு தினக் கொண்டாட்டம்",
    ["1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "3 -> 1 -> 2 -> 4"],
    ["1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "3 -> 1 -> 2 -> 4"],
    "A",
    "Correct Chronological Sequence: 1 (Adoption of Constitution, Nov 26, 1949) -> 2 (Adoption of Anthem/Song, Jan 24, 1950 morning) -> 3 (Election of 1st President, Jan 24, 1950 afternoon) -> 4 (Commencement & Republic Day, Jan 26, 1950).",
    "சரியான காலவரிசை: 1 (அரசியலமைப்பு ஏற்பு, நவ 26, 1949) -> 2 (தேசிய கீதம்/பாடல் ஏற்பு, ஜன 24, 1950 காலை) -> 3 (முதல் குடியரசுத் தலைவர் தேர்வு, ஜன 24, 1950) -> 4 (நடைமுறை & குடியரசு தினம், ஜன 26, 1950).",
    "Correct. 1 (Nov 26, 1949) -> 2 (Jan 24, 1950) -> 3 (Jan 24, 1950) -> 4 (Jan 26, 1950) is exact.", "சரி. 1 (நவ 26, 1949) -> 2 (ஜன 24, 1950) -> 3 (ஜன 24, 1950) -> 4 (ஜன 26, 1950) துல்லியமானது.",
    "Incorrect. Adoption of Constitution (Nov 26, 1949) preceded Jan 24, 1950.", "தவறு. அரசியலமைப்பு ஏற்பு (நவ 26, 1949) ஜனவரி 24, 1950-க்கு முந்தியது.",
    "Incorrect. Adoption of Anthem preceded election of President on Jan 24 morning.", "தவறு. தேசிய கீதம் ஏற்பு தலைவர் தேர்வுக்கு முந்தியது.",
    "Incorrect. Adoption of Constitution (Nov 26, 1949) was the earliest.", "தவறு. அரசியலமைப்பு ஏற்பு (நவ 26, 1949) மிக முந்தையது.",
    "TNPSC Trap: Adoption = Nov 26, 1949. Anthem/Song Adoption & President Election = Jan 24, 1950. Commencement = Jan 26, 1950.",
    "TNPSC பொறி: ஏற்பு = நவம்பர் 26, 1949. கீதம்/பாடல் ஏற்பு & தலைவர் தேர்வு = ஜனவரி 24, 1950. நடைமுறை = ஜனவரி 26, 1950.",
    "On January 24, 1950, 284 members signed 3 copies (2 handwritten in English & Hindi, 1 printed in English).",
    "ஜனவரி 24, 1950 அன்று 284 உறுப்பினர்கள் 3 பிரதிகளில் கையெழுத்திட்டனர்.",
    "Medium", "Analyze", 60, ["Polity", "Making of Indian Constitution", "Constitution Adoption", "National Anthem adoption", "Enforcement of Constitution", "First Republic Day"],
    events=[{"id": "1", "en": "Constitution adoption (Nov 26, 1949)", "ta": "அரசியலமைப்பு ஏற்பு (நவ 26, 1949)"}, {"id": "2", "en": "Anthem/Song adoption (Jan 24, 1950)", "ta": "கீதம்/பாடல் ஏற்பு (ஜன 24, 1950)"}, {"id": "3", "en": "1st President election (Jan 24, 1950)", "ta": "1வது குடியரசுத் தலைவர் தேர்வு (ஜன 24, 1950)"}, {"id": "4", "en": "Commencement & Republic Day (Jan 26, 1950)", "ta": "நடைமுறை & குடியரசு தினம் (ஜன 26, 1950)"}]
))

# MIC_PYQ_046 (Reasoning / Analytical)
questions.append(make_pyq_q(
    "MIC_PYQ_046", "Reasoning / Analytical",
    "Why did Jawaharlal Nehru and the Indian National Congress insist in 1938 that the Constitution of free India must be framed by a Constituent Assembly elected on adult franchise without outside interference?",
    "சுதந்திர இந்தியாவின் அரசியலமைப்பு வெளிச்சக்திகளின் தலையீடின்றி வயதுவந்தோர் வாக்குரிமையால் தேர்ந்தெடுக்கப்பட்ட அவையால் மட்டுமே உருவாக்கப்பட வேண்டும் என 1938 இல் நேருவும் காங்கிரஸும் ஏன் வலியுறுத்தினர்?",
    ["To assert national popular sovereignty and ensure political legitimacy against British imperial imposition", "To prevent Muslim League from participating in constitution-framing", "To establish a purely unitary system of government under British supervision", "To avoid conducting elections in Princely States"],
    ["பிரிட்டிஷ் ஏகாதிபத்திய திணிப்பிற்கு எதிராக தேசிய மக்கள் இறையாண்மையை அழுத்தமாக வெளிப்படுத்தவும் அரசியல் சட்டபூர்வமான தன்மையை உறுதிப்படுத்தவும்", "அரசியலமைப்பு உருவாக்கத்தில் முஸ்லீம் லீக் பங்கேற்பதைத் தடுக்க", "பிரிட்டிஷ் மேற்பார்வையில் முற்றிலும் ஒற்றையாட்சி அமைப்பை நிறுவ", "சுதேச சமஸ்தானங்களில் தேர்தல்களை நடத்துவதைத் தவிர்க்க"],
    "A",
    "The demand for a Constituent Assembly elected on adult franchise was the ultimate assertion of popular sovereignty—that political authority belongs to the people of India, not British Parliament.",
    "வயதுவந்தோர் வாக்குரிமையால் தேர்ந்தெடுக்கப்பட்ட அவைக் கோரிக்கை என்பது மக்கள் இறையாண்மையின் அழுத்தமான வெளிப்பாடாகும்—அரசியல் அதிகாரம் பிரிட்டிஷ் நாடாளுமன்றத்திற்கு அல்ல, இந்திய மக்களுக்கே உரியது.",
    "Correct. Popular sovereignty and political legitimacy were the core reasons.", "சரி. மக்கள் இறையாண்மை மற்றும் அரசியல் சட்டபூர்வமான தன்மையே முதன்மைக் காரணங்கள்.",
    "Incorrect. It was aimed against British imperial control, not League exclusion.", "தவறு. இது பிரிட்டிஷ் கட்டுப்பாட்டிற்கு எதிரானது.",
    "Incorrect. It demanded complete independence from British supervision.", "தவறு. இது பிரிட்டிஷ் மேற்பார்வையிலிருந்து முழு சுதந்திரத்தைக் கோரியது.",
    "Incorrect. It sought full democratic representation across India.", "தவறு. இது இந்தியா முழுவதும் முழு ஜனநாயகப் பிரதிநிதித்துவத்தைக் கோரியது.",
    "TNPSC Trap: Nehru's 1938 declaration established the fundamental principle of Popular Sovereignty.",
    "TNPSC பொறி: நேருவின் 1938 அறிவிப்பு மக்கள் இறையாண்மை என்ற அடிப்படைத் தத்துவத்தை நிறுவியது.",
    "Popular sovereignty is enshrined in the Preamble ('We, the People of India').",
    "மக்கள் இறையாண்மை முகப்புரையில் ('இந்திய மக்களாகிய நாம்') பொறிக்கப்பட்டுள்ளது.",
    "Hard", "Analyze", 75, ["Polity", "Making of Indian Constitution", "Demand for Constituent Assembly", "Jawaharlal Nehru"]
))

# MIC_PYQ_047 (Reasoning / Analytical)
questions.append(make_pyq_q(
    "MIC_PYQ_047", "Reasoning / Analytical",
    "Why was Dr. B.R. Ambedkar chosen to head the Drafting Committee of the Constituent Assembly despite his prior sharp political opposition to the ruling Congress party?",
    "ஆளும் காங்கிரஸ் கட்சிக்கு எதிராக அரசியலில் ஈடுபட்டிருந்தபோதிலும், டாக்டர் பி.ஆர். அம்பேத்கர் வரைவுக் குழுவின் தலைவராக ஏன் தேர்ந்தெடுக்கப்பட்டார்?",
    ["Congress leaders recognized Ambedkar's unmatched legal jurisprudence and dedication to social democracy above party differences", "British Government mandated Ambedkar's appointment under Cabinet Mission Plan", "Ambedkar was the only member with a formal law degree in the Assembly", "Muslim League insisted on Ambedkar's chairmanship as a condition for partition"],
    ["காங்கிரஸ் தலைவர்கள் கட்சி வேறுபாடுகளுக்கு மேலாக அம்பேத்கரின் இணையற்ற சட்டப் புலமையையும் சமூக ஜனநாயக அர்ப்பணிப்பையும் அங்கீகரித்தனர்", "கேபினட் திட்டத்தின் கீழ் பிரிட்டிஷ் அரசாங்கம் அம்பேத்கரின் நியமனத்தைக் கட்டாயப்படுத்தியது", "அவையில் முறையான சட்டப் பட்டம் பெற்ற ஒரே உறுப்பினர் அம்பேத்கர் மட்டுமே என்பதால்", "பிரிவினைக்கான நிபந்தனையாக முஸ்லீம் லீக் அம்பேத்கரின் தலைமையை வலியுறுத்தியதால்"],
    "A",
    "Mahatma Gandhi, Nehru, and Patel recognized that drafting free India's Constitution required Ambedkar's extraordinary legal jurisprudence and commitment to social equality, transcending partisan politics.",
    "சுதந்திர இந்தியாவின் அரசியலமைப்பை வரைவதற்கு அம்பேத்கரின் இணையற்ற சட்டப் புலமையும் சமூகச் சமத்துவ அர்ப்பணிப்பும் தேவை என்பதை காந்தியடிகள், நேரு மற்றும் படேல் அங்கீகரித்தனர்.",
    "Correct. Meritocracy, legal genius, and social vision transcended party differences.", "சரி. தகுதி, சட்டப் புலமை மற்றும் சமூகப் பார்வை கட்சி வேறுபாடுகளுக்கு மேல் இருந்தது.",
    "Incorrect. Cabinet Mission had no role in appointing Drafting Committee.", "தவறு. கேபினட் தூதுக்குழு வரைவுக் குழு நியமனத்தில் எவ்விதப் பங்கும் வகிக்கவில்லை.",
    "Incorrect. Many members (Alladi, Munshi, Rau) had formal law degrees.", "தவறு. அல்லாடி, முன்ஷி, ராவ் போன்ற பல உறுப்பினர்கள் சட்டப் பட்டம் பெற்றிருந்தனர்.",
    "Incorrect. Muslim League had boycotted the Assembly.", "தவறு. முஸ்லீம் லீக் அவையைப் புறக்கணித்திருந்தது.",
    "TNPSC Trap: Mahatma Gandhi explicitly suggested including non-Congress legal experts like Ambedkar in the Cabinet and Drafting Committee.",
    "TNPSC பொறி: அமைச்சரவையிலும் வரைவுக் குழுவிலும் அம்பேத்கர் போன்ற காங்கிரஸ் அல்லாத சட்ட நிபுணர்களைச் சேர்க்க மகாத்மா காந்தி பரிந்துரைத்தார்.",
    "Ambedkar was also appointed as India's first Law Minister in the post-independence Cabinet.",
    "சுதந்திரக்குப் பிந்தைய அமைச்சரவையில் அம்பேத்கர் இந்தியாவின் முதல் சட்ட அமைச்சராக நியமிக்கப்பட்டார்.",
    "Hard", "Analyze", 75, ["Polity", "Making of Indian Constitution", "Ambedkar", "Drafting Committee"]
))

# MIC_PYQ_048 (Reasoning / Analytical)
questions.append(make_pyq_q(
    "MIC_PYQ_048", "Reasoning / Analytical",
    "Why did Dr. B.R. Ambedkar warn in his final Assembly address that 'Bhakti or hero-worship in politics is a sure road to degradation and to eventual dictatorship'?",
    "அரசியலில் பக்தி அல்லது நபர் வழிபாடு சீரழிவுக்கும் இறுதியில் சர்வாதிகாரத்திற்கும் உறுதியான வழியாகும் என்று டாக்டர் பி.ஆர். அம்பேத்கர் தனது இறுதி உரையில் ஏன் எச்சரித்தார்?",
    ["Unquestioning blind devotion leads citizens to surrender their liberties and subvert democratic institutions", "Hero-worship causes economic inflation and currency devaluation", "Bhakti prevents religious harmony among different communities", "Hero-worship was illegal under the Indian Independence Act 1947"],
    ["கேள்வி கேட்காத குருட்டுப் பக்தி குடிமக்கள் தங்கள் சுதந்திரங்களைச் சரணடையச் செய்து ஜனநாயக அமைப்புகளைச் சீரழிக்க வழிவகுக்கும் என்பதால்", "நபர் வழிபாடு பொருளாதார பணவீக்கத்தையும் நாணய மதிப்பிழப்பையும் ஏற்படுத்துகிறது என்பதால்", "பக்தி பல்வேறு சமூகங்களுக்கிடையே மத நல்லிணக்கத்தைத் தடுக்கிறது என்பதால்", "1947 இந்திய சுதந்திரச் சட்டத்தின் கீழ் நபர் வழிபாடு சட்டவிரோதமானது என்பதால்"],
    "A",
    "Quoting John Stuart Mill, Ambedkar warned that hero-worship in politics leads citizens to surrender their rights at the feet of a leader, destroying constitutional democracy and birthing dictatorship.",
    "ஜான் ஸ்டூவர்ட் மில்லை மேற்கோள் காட்டி, அரசியலில் நபர் வழிபாடு குடிமக்களைத் தலைவரின் காலடியில் தங்கள் உரிமைகளைச் சமர்ப்பிக்கச் செய்து சர்வாதிகாரத்திற்கு வழிவகுக்கும் என அம்பேத்கர் எச்சரித்தார்.",
    "Correct. Blind devotion subverts democracy and spawns dictatorship.", "சரி. குருட்டுப் பக்தி ஜனநாயகத்தைச் சீரழித்து சர்வாதிகாரத்தை உருவாக்கும்.",
    "Incorrect. It was a warning about political democracy, not inflation.", "தவறு. இது அரசியல் ஜனநாயகம் பற்றிய எச்சரிக்கை.",
    "Incorrect. Bhakti in religion is harmless, but fatal in politics.", "தவறு. மதத்தில் பக்தி தீங்கற்றது, ஆனால் அரசியலில் ஆபத்தானது என்றார்.",
    "Incorrect. It was a philosophical warning, not a legal ban.", "தவறு. இது ஒரு தத்துவ எச்சரிக்கை.",
    "TNPSC Trap: Ambedkar said Bhakti may be a road to salvation in religion, BUT in politics, Bhakti is a sure road to degradation and dictatorship.",
    "TNPSC பொறி: மதத்தில் பக்தி முக்திக்கு வழியாக இருக்கலாம், ஆனால் அரசியலில் அது சீரழிவுக்கும் சர்வாதிகாரத்திற்கும் உறுதியான வழி என்றார் அம்பேத்கர்.",
    "Ambedkar delivered this warning on November 25, 1949.",
    "அம்பேத்கர் இந்த எச்சரிக்கையை நவம்பர் 25, 1949 அன்று வழங்கினார்.",
    "Hard", "Analyze", 75, ["Polity", "Making of Indian Constitution", "Ambedkar's Final Speech", "Bhakti in politics"]
))

# MIC_PYQ_049 (Reasoning / Analytical)
questions.append(make_pyq_q(
    "MIC_PYQ_049", "Reasoning / Analytical",
    "Why did Dr. B.R. Ambedkar term civil disobedience, non-cooperation, and satyagraha as the 'Grammar of Anarchy' after the Constitution was enacted?",
    "அரசியலமைப்பு இயற்றப்பட்ட பிறகு சட்டமறுப்பு, ஒத்துழையாமை மற்றும் சத்தியாகிரகம் ஆகியவற்றை 'அராஜகத்தின் இலக்கணம்' என்று டாக்டர் பி.ஆர். அம்பேத்கர் ஏன் வர்ணித்தார்?",
    ["When constitutional methods for achieving economic and social objectives are open, unconstitutional extra-parliamentary agitations subvert the rule of law", "Satyagraha was a foreign concept borrowed from European revolutions", "Civil disobedience was prohibited under Article 368 of the Constitution", "Non-cooperation was effective only against foreign British rule"],
    ["சமூக-பொருளாதார இலக்குகளை அடைய அரசியலமைப்பு முறைகள் திறந்துள்ள போது, அரசியலமைப்புக்கு புறம்பான போராட்டங்கள் சட்டத்தின் ஆட்சியைச் சீரழிக்கின்றன என்பதால்", "சத்தியாகிரகம் என்பது ஐரோப்பிய புரட்சிகளிலிருந்து பெறப்பட்ட அயல்நாட்டுக் கருத்து என்பதால்", "அரசியலமைப்பின் சரத்து 368 இன் கீழ் சட்டமறுப்பு தடை செய்யப்பட்டிருந்தது என்பதால்", "ஒத்துழையாமை பிரிட்டிஷ் ஆட்சிக்கு எதிராக மட்டுமே பயனுள்ளதாக இருந்தது என்பதால்"],
    "A",
    "Ambedkar argued that during British rule, unconstitutional agitations were justified because democratic constitutional remedies were absent. Once a democratic Constitution is enacted, unconstitutional methods undermine law and order.",
    "பிரிட்டிஷ் ஆட்சியில் ஜனநாயகத் தீர்வுகள் இல்லாததால் போராட்டங்கள் நியாயமானவை. ஆனால் ஜனநாயக அரசியலமைப்பு அமைந்த பின் அரசியலமைப்புக்கு புறம்பான போராட்டங்கள் சட்டத்தின் ஆட்சியை அழிக்கும் என்றார்.",
    "Correct. Availability of constitutional remedies makes extra-constitutional agitation unconstitutional.", "சரி. அரசியலமைப்புத் தீர்வுகள் உள்ள போது பிற போராட்டங்கள் அராஜகமாகும்.",
    "Incorrect. Satyagraha was indigenous, developed by Gandhiji.", "தவறு. சத்தியாகிரகம் காந்தியடிகளால் உருவாக்கப்பட்டது.",
    "Incorrect. Article 368 deals with constitutional amendments.", "தவறு. சரத்து 368 திருத்தங்களைப் பற்றியது.",
    "Incorrect. The core reason is the availability of constitutional remedies for redressal.", "தவறு. அரசியலமைப்புத் தீர்வுகள் இருப்பதே முதன்மைக் காரணம்.",
    "TNPSC Trap: Ambedkar said: 'Where constitutional methods are open, there can be no justification for unconstitutional methods.'",
    "TNPSC பொறி: 'அரசியலமைப்பு முறைகள் திறந்திருக்கும் போது, அரசியலமைப்புக்கு புறம்பான முறைகளுக்கு நியாயமே இருக்க முடியாது' என்றார் அம்பேத்கர்.",
    "This concept was articulated in Ambedkar's Nov 25, 1949 speech.",
    "இந்தக் கருத்து அம்பேத்கரின் நவம்பர் 25, 1949 உரையில் தெளிவுபடுத்தப்பட்டது.",
    "Hard", "Analyze", 75, ["Polity", "Making of Indian Constitution", "Grammar of Anarchy", "Ambedkar's Final Speech"]
))

# MIC_PYQ_050 (Reasoning / Analytical)
questions.append(make_pyq_q(
    "MIC_PYQ_050", "Reasoning / Analytical",
    "Why did Dr. B.R. Ambedkar stress that political democracy cannot last unless there lies at the base of it social democracy?",
    "சமூக ஜனநாயகத்தின் அடித்தளத்தின் மீது கட்டப்படாவிட்டால் அரசியல் ஜனநாயகம் நிலைக்க முடியாது என்று டாக்டர் பி.ஆர். அம்பேத்கர் ஏன் அழுத்தமாகக் கூறினார்?",
    ["Granting political equality ('one man, one vote') while preserving deep social/economic inequality ('one man, one value' denied) creates a contradiction that will blow up democracy", "Social democracy is required by the Cabinet Mission Plan 1946", "Political democracy applies only to Central Government while social democracy applies to States", "Without social democracy, foreign countries will not grant loans to India"],
    ["அரசியல் சமத்துவத்தை ('ஒரு மனிதனுக்கு ஒரு வாக்கு') வழங்கும் அதே வேளையில் ஆழமான சமூக/பொருளாதார சமத்துவமின்மையை ('ஒரு மனிதனுக்கு ஒரு மதிப்பு' மறுப்பு) பேணுவது ஜனநாயகத்தைத் தகர்க்கும் முரண்பாட்டை உருவாக்கும் என்பதால்", "1946 கேபினட் தூதுக்குழு திட்டத்தால் சமூக ஜனநாயகம் கோரப்பட்டதால்", "அரசியல் ஜனநாயகம் மத்திய அரசுக்கும் சமூக ஜனநாயகம் மாநிலங்களுக்கும் மட்டுமே பொருந்தும் என்பதால்", "சமூக ஜனநாயகம் இல்லையென்றால் வெளிநாடுகள் இந்தியாவிற்கு கடன் வழங்காது என்பதால்"],
    "A",
    "Ambedkar highlighted the danger of entering a life of contradictions on Jan 26, 1950: equality in politics (one man, one vote) but inequality in social and economic structure (denying one man, one value). He urged establishing social democracy recognizing Liberty, Equality, and Fraternity as a trinity.",
    "ஜனவரி 26, 1950 இல் இந்தியா முரண்பாட்டில் நுழைகிறது: அரசியலில் சமத்துவம் (ஒரு வாக்கு) ஆனால் சமூகத்தில் சமத்துவமின்மை (மதிப்பற்ற நிலை). சமூக ஜனநாயகம் இல்லாவிட்டால் இந்த முரண்பாடு ஜனநாயகத்தைத் தகர்க்கும் என்றார்.",
    "Correct. Contradiction between political equality and social inequality threatens democracy.", "சரி. அரசியல் சமத்துவத்திற்கும் சமூக சமத்துவமின்மைக்கும் இடையிலான முரண்பாடு ஜனநாயகத்திற்கு ஆபத்தானது.",
    "Incorrect. Cabinet Mission Plan did not mandate social democracy.", "தவறு. கேபினட் திட்டம் சமூக ஜனநாயகத்தைக் கோரவில்லை.",
    "Incorrect. Both apply to the entire nation at all levels.", "தவறு. இரண்டும் அனைத்து நிலைகளுக்கும் பொருந்தும்.",
    "Incorrect. Foreign loans have no relevance to Ambedkar's philosophical warning.", "தவறு. வெளிநாட்டுக் கடன்களுக்கும் இதற்கும் தொடர்பில்லை.",
    "TNPSC Trap: Social Democracy = Way of life recognizing Liberty, Equality, and Fraternity as an INSEPARABLE TRINITY.",
    "TNPSC பொறி: சமூக ஜனநாயகம் = சுதந்திரம், சமத்துவம், சகோதரத்துவத்தை பிரிக்க முடியாத திரித்துவமாகக் கொள்ளும் வாழ்க்கை முறை.",
    "Divorcing Liberty from Equality, or Equality from Liberty, defeats the primary purpose of democracy.",
    "சுதந்திரத்தையும் சமத்துவத்தையும் பிரிப்பது ஜனநாயகத்தின் முதன்மை நோக்கத்தைச் சீரழிக்கும்.",
    "Hard", "Analyze", 75, ["Polity", "Making of Indian Constitution", "Social Democracy", "Ambedkar's Final Speech"]
))
