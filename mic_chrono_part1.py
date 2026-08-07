def make_chrono_q(q_id, q_type, q_en, q_ta, events_en, events_ta,
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
    
    events_objs = [{"id": str(i+1), "en": events_en[i], "ta": events_ta[i]} for i in range(len(events_en))]

    return {
        "id": q_id,
        "subject": "Polity",
        "topic": "Making of Indian Constitution",
        "difficulty": "Hard",
        "question_type": "Chronology",
        "question": {"en": q_en, "ta": q_ta},
        "events": events_objs,
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

# MIC_CHRONO_001
questions.append(make_chrono_q(
    "MIC_CHRONO_001", "Chronology",
    "Arrange the following historical developments regarding the demand for a Constituent Assembly in correct chronological order:\n1. M.N. Roy puts forward the idea of a Constituent Assembly for India\n2. Indian National Congress officially demands a Constituent Assembly for the first time\n3. Jawaharlal Nehru declares that the Constitution of free India must be framed by a Constituent Assembly elected on adult franchise\n4. British Government accepts the demand for a Constituent Assembly in principle in the August Offer",
    "இந்தியாவிற்கான அரசியலமைப்பு நிர்ணய அவைக் கோரிக்கை பற்றிய பின்வரும் வரலாற்று முன்னேற்றங்களை சரியான காலவரிசையில் அமைக்கவும்:\n1. எம்.என். ராய் முதன்முதலில் இந்தியாவிற்கான அரசியலமைப்பு நிர்ணய அவைக் கருத்தை முன்வைத்தார்\n2. இந்திய தேசிய காங்கிரஸ் முதன்முறையாக அரசியலமைப்பு நிர்ணய அவையைக் கோரி அதிகாரப்பூர்வமாக கோரிக்கை விடுத்தது\n3. சுதந்திர இந்தியாவின் அரசியலமைப்பு வயதுவந்தோர் வாக்குரிமையால் தேர்ந்தெடுக்கப்பட்ட அவையால் உருவாக்கப்பட வேண்டும் என ஜவகர்லால் நேரு அறிவித்தார்\n4. பிரிட்டிஷ் அரசாங்கம் ஆகஸ்ட் சலுகையில் கொள்கையளவில் அவைக் கோரிக்கையை ஏற்றுக்கொண்டது",
    ["M.N. Roy puts forward the idea of a Constituent Assembly for India", "Indian National Congress officially demands a Constituent Assembly for the first time", "Jawaharlal Nehru declares that the Constitution of free India must be framed by a Constituent Assembly elected on adult franchise", "British Government accepts the demand for a Constituent Assembly in principle in the August Offer"],
    ["எம்.என். ராய் முதன்முதலில் இந்தியாவிற்கான அரசியலமைப்பு நிர்ணய அவைக் கருத்தை முன்வைத்தார்", "இந்திய தேசிய காங்கிரஸ் முதன்முறையாக அரசியலமைப்பு நிர்ணய அவையைக் கோரி அதிகாரப்பூர்வமாக கோரிக்கை விடுத்தது", "சுதந்திர இந்தியாவின் அரசியலமைப்பு வயதுவந்தோர் வாக்குரிமையால் தேர்ந்தெடுக்கப்பட்ட அவையால் உருவாக்கப்பட வேண்டும் என ஜவகர்லால் நேரு அறிவித்தார்", "பிரிட்டிஷ் அரசாங்கம் ஆகஸ்ட் சலுகையில் கொள்கையளவில் அவைக் கோரிக்கையை ஏற்றுக்கொண்டது"],
    "1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "3 -> 1 -> 2 -> 4",
    "A",
    "Correct Chronological Sequence: 1 (M.N. Roy idea, 1934) -> 2 (INC official demand, 1935) -> 3 (Nehru declaration on adult franchise, 1938) -> 4 (August Offer acceptance in principle, 1940).",
    "சரியான காலவரிசை: 1 (எம்.என். ராய் கருத்து, 1934) -> 2 (காங்கிரஸ் அதிகாரப்பூர்வ கோரிக்கை, 1935) -> 3 (நேருவின் அறிவிப்பு, 1938) -> 4 (ஆகஸ்ட் சலுகை ஏற்பு, 1940).",
    "Correct. 1 (1934) -> 2 (1935) -> 3 (1938) -> 4 (1940) follows exact chronological sequence.", "சரி. 1 (1934) -> 2 (1935) -> 3 (1938) -> 4 (1940) துல்லியமான காலவரிசையைப் பின்பற்றுகிறது.",
    "Incorrect. M.N. Roy proposed the idea in 1934 (1), before INC official demand in 1935 (2).", "தவறு. எம்.என். ராய் 1934 இல் முன்மொழிந்தார் (1).",
    "Incorrect. INC official demand was in 1935 (2), before Nehru's declaration in 1938 (3).", "தவறு. காங்கிரஸ் 1935 இல் கோரியது (2).",
    "Incorrect. M.N. Roy proposed the idea in 1934 (1), before Nehru's declaration in 1938 (3).", "தவறு. எம்.என். ராய் 1934 இல் முன்மொழிந்தார் (1).",
    "TNPSC Trap: M.N. Roy (1934) -> INC Official Demand (1935) -> Nehru Declaration (1938) -> August Offer (1940).",
    "TNPSC பொறி: எம்.என். ராய் (1934) -> காங்கிரஸ் கோரிக்கை (1935) -> நேரு அறிவிப்பு (1938) -> ஆகஸ்ட் சலுகை (1940).",
    "M.N. Roy was a pioneer of the communist movement in India and an advocate of radical democracy.",
    "எம்.என். ராய் இந்தியாவில் கம்யூனிச இயக்கத்தின் முன்னோடியும் தீவிர ஜனநாயகத்தின் ஆதரவாளரும் ஆவார்.",
    "Analyze", 75, ["Polity", "Making of Indian Constitution", "Demand for Constituent Assembly", "August Offer"]
))

# MIC_CHRONO_002
questions.append(make_chrono_q(
    "MIC_CHRONO_002", "Chronology",
    "Which one of the following is the correct chronological sequence of British proposals and missions sent to resolve India's constitutional deadlock?\n1. August Offer by Viceroy Linlithgow\n2. Cripps Mission led by Sir Stafford Cripps\n3. Arrival of Cabinet Mission in New Delhi\n4. Publication of Cabinet Mission's Constitutional Plan",
    "இந்தியாவின் அரசியலமைப்பு முட்டுக்கட்டையைத் தீர்க்க அனுப்பப்பட்ட பிரிட்டிஷ் திட்டங்கள் மற்றும் தூதுக்குழுக்களின் சரியான காலவரிசை எது?\n1. வைஸ்ராய் லின்லித்கோவின் ஆகஸ்ட் சலுகை\n2. சர் ஸ்டாஃபோர்ட் கிரிப்ஸ் தலைமையிலான கிரிப்ஸ் தூதுக்குழு\n3. புதுடெல்லியில் கேபினட் தூதுக்குழு வருகை\n4. கேபினட் தூதுக்குழுவின் அரசியலமைப்பு திட்டம் வெளியிடப்படுதல்",
    ["August Offer by Viceroy Linlithgow", "Cripps Mission led by Sir Stafford Cripps", "Arrival of Cabinet Mission in New Delhi", "Publication of Cabinet Mission's Constitutional Plan"],
    ["வைஸ்ராய் லின்லித்கோவின் ஆகஸ்ட் சலுகை", "சர் ஸ்டாஃபோர்ட் கிரிப்ஸ் தலைமையிலான கிரிப்ஸ் தூதுக்குழு", "புதுடெல்லியில் கேபினட் தூதுக்குழு வருகை", "கேபினட் தூதுக்குழுவின் அரசியலமைப்பு திட்டம் வெளியிடப்படுதல்"],
    "1 -> 2 -> 3 -> 4", "2 -> 1 -> 4 -> 3", "1 -> 3 -> 2 -> 4", "3 -> 1 -> 2 -> 4",
    "A",
    "Correct Chronological Sequence: 1 (August Offer, Aug 8, 1940) -> 2 (Cripps Mission, March 1942) -> 3 (Arrival of Cabinet Mission, March 24, 1946) -> 4 (Publication of Cabinet Mission Plan, May 16, 1946).",
    "சரியான காலவரிசை: 1 (ஆகஸ்ட் சலுகை, ஆகஸ்ட் 8, 1940) -> 2 (கிரிப்ஸ் திட்டம், மார்ச் 1942) -> 3 (கேபினட் தூதுக்குழு வருகை, மார்ச் 24, 1946) -> 4 (கேபினட் திட்டம் வெளியீடு, மே 16, 1946).",
    "Correct. 1 (1940) -> 2 (1942) -> 3 (March 1946) -> 4 (May 1946) is exact.", "சரி. 1 (1940) -> 2 (1942) -> 3 (மார்ச் 1946) -> 4 (மே 1946) துல்லியமானது.",
    "Incorrect. August Offer (1940) preceded Cripps Mission (1942).", "தவறு. ஆகஸ்ட் சலுகை (1940) கிரிப்ஸ் திட்டத்திற்கு முந்தியது.",
    "Incorrect. Cripps Mission (1942) arrived before Cabinet Mission (1946).", "தவறு. கிரிப்ஸ் திட்டம் (1942) கேபினட் தூதுக்குழுவிற்கு முந்தியது.",
    "Incorrect. Cabinet Mission arrived in March 1946 (3), after August Offer (1940).", "தவறு. கேபினட் தூதுக்குழு மார்ச் 1946 இல் வந்தது (3).",
    "TNPSC Trap: Cabinet Mission arrived in New Delhi on March 24, 1946, and announced its plan on May 16, 1946.",
    "TNPSC பொறி: கேபினட் தூதுக்குழு மார்ச் 24, 1946 இல் புதுடெல்லி வந்தது, மேலும் மே 16, 1946 இல் தனது திட்டத்தை அறிவித்தது.",
    "The Cripps Mission offered Dominion Status after WWII, which Gandhiji called 'a post-dated cheque on a crashing bank'.",
    "கிரிப்ஸ் திட்டம் போருக்குப் பின் டொமினியன் அந்தஸ்தை வழங்கியது, இதை காந்தியடிகள் 'நொடித்துப்போகும் வங்கியின் பின்நாளிட்ட காசோலை' என்றார்.",
    "Analyze", 75, ["Polity", "Making of Indian Constitution", "August Offer", "Cripps Mission", "Cabinet Mission Plan"]
))

# MIC_CHRONO_003
questions.append(make_chrono_q(
    "MIC_CHRONO_003", "Chronology",
    "Identify the correct chronological order of events in the initial formation of the Constituent Assembly in 1946:\n1. Elections held for British Indian seats in the Constituent Assembly\n2. Formation of the Interim Government of India headed by Jawaharlal Nehru\n3. First meeting of the Constituent Assembly attended by 211 members\n4. Dr. Rajendra Prasad elected as permanent President of the Assembly",
    "1946 இல் அரசியலமைப்பு நிர்ணய அவையின் ஆரம்ப உருவாக்கத்தில் நடந்த நிகழ்வுகளின் சரியான காலவரிசையை அடையாளம் காணவும்:\n1. அரசியலமைப்பு நிர்ணய அவையின் பிரிட்டிஷ் இந்திய இடங்களுக்கான தேர்தல்கள் நடத்தப்பட்டது\n2. ஜவகர்லால் நேரு தலைமையில் இந்தியாவின் இடைக்கால அரசு அமைக்கப்பட்டது\n3. 211 உறுப்பினர்கள் பங்கேற்ற அரசியலமைப்பு அவையின் முதல் கூட்டம்\n4. டாக்டர் ராஜேந்திர பிரசாத் அவையின் நிரந்தரத் தலைவராகத் தேர்ந்தெடுக்கப்பட்டார்",
    ["Elections held for British Indian seats in the Constituent Assembly", "Formation of the Interim Government of India headed by Jawaharlal Nehru", "First meeting of the Constituent Assembly attended by 211 members", "Dr. Rajendra Prasad elected as permanent President of the Assembly"],
    ["அரசியலமைப்பு நிர்ணய அவையின் பிரிட்டிஷ் இந்திய இடங்களுக்கான தேர்தல்கள் நடத்தப்பட்டது", "ஜவகர்லால் நேரு தலைமையில் இந்தியாவின் இடைக்கால அரசு அமைக்கப்பட்டது", "211 உறுப்பினர்கள் பங்கேற்ற அரசியலமைப்பு அவையின் முதல் கூட்டம்", "டாக்டர் ராஜேந்திர பிரசாத் அவையின் நிரந்தரத் தலைவராகத் தேர்ந்தெடுக்கப்பட்டார்"],
    "1 -> 2 -> 3 -> 4", "2 -> 1 -> 4 -> 3", "1 -> 3 -> 2 -> 4", "3 -> 1 -> 2 -> 4",
    "A",
    "Correct Chronological Sequence: 1 (Assembly Elections, July-Aug 1946) -> 2 (Interim Govt formed, Sept 2, 1946) -> 3 (First Meeting of CA, Dec 9, 1946) -> 4 (Dr. Rajendra Prasad elected President, Dec 11, 1946).",
    "சரியான காலவரிசை: 1 (அவைத் தேர்தல், ஜூலை-ஆகஸ்ட் 1946) -> 2 (இடைக்கால அரசு அமைப்பு, செப்டம்பர் 2, 1946) -> 3 (முதல் கூட்டம், டிசம்பர் 9, 1946) -> 4 (ராஜேந்திர பிரசாத் தலைவராகத் தேர்வு, டிசம்பர் 11, 1946).",
    "Correct. 1 (July-Aug 1946) -> 2 (Sept 2, 1946) -> 3 (Dec 9, 1946) -> 4 (Dec 11, 1946) is exact.", "சரி. 1 (ஜூலை-ஆகஸ்ட் 1946) -> 2 (செப் 2, 1946) -> 3 (டிச 9, 1946) -> 4 (டிச 11, 1946) துல்லியமானது.",
    "Incorrect. Assembly elections occurred in July-Aug 1946 (1), before Interim Govt in Sept 1946 (2).", "தவறு. அவைத் தேர்தல் ஜூலை-ஆகஸ்ட் 1946 இல் நடந்தது (1).",
    "Incorrect. Interim Govt was formed in Sept 1946 (2), before First Meeting in Dec 1946 (3).", "தவறு. இடைக்கால அரசு செப்டம்பர் 1946 இல் அமைந்தது (2).",
    "Incorrect. Assembly elections (1) preceded First meeting (3).", "தவறு. அவைத் தேர்தல் (1) முதல் கூட்டத்திற்கு முந்தியது (3).",
    "TNPSC Trap: Assembly Elections = July-August 1946. Interim Govt = Sept 2, 1946. First Assembly Meeting = Dec 9, 1946. Rajendra Prasad elected = Dec 11, 1946.",
    "TNPSC பொறி: அவைத் தேர்தல் = ஜூலை-ஆகஸ்ட் 1946. இடைக்கால அரசு = செப்டம்பர் 2, 1946. முதல் கூட்டம் = டிசம்பர் 9, 1946. ராஜேந்திர பிரசாத் தேர்வு = டிசம்பர் 11, 1946.",
    "Members of the Interim Government were members of the Viceroy's Executive Council, with Lord Wavell as President and Nehru as Vice-President.",
    "இடைக்கால அரசு உறுப்பினர்கள் வைஸ்ராய் செயற்குழு உறுப்பினர்களாக இருந்தனர்; வேவல் பிரபு தலைவராகவும் நேரு துணைத் தலைவராகவும் இருந்தனர்.",
    "Analyze", 75, ["Polity", "Making of Indian Constitution", "Constituent Assembly Election", "First Meeting", "Permanent President"]
))

# MIC_CHRONO_004
questions.append(make_chrono_q(
    "MIC_CHRONO_004", "Chronology",
    "Arrange the following events of the Constituent Assembly in correct chronological order:\n1. Introduction of the Objectives Resolution by Jawaharlal Nehru\n2. Unanimous adoption of the Objectives Resolution by the Assembly\n3. Representatives of six Princely States take their seats in the Assembly for the first time\n4. Setting up of the Ad hoc Committee on the National Flag",
    "அரசியலமைப்பு நிர்ணய அவையின் பின்வரும் நிகழ்வுகளை சரியான காலவரிசையில் அமைக்கவும்:\n1. ஜவகர்லால் நேருவால் குறிக்கோள்கள் தீர்மானம் அறிமுகப்படுத்தப்பட்டது\n2. அவையால் குறிக்கோள்கள் தீர்மானம் ஒருமனதாக ஏற்றுக்கொள்ளப்பட்டது\n3. ஆறு சுதேச சமஸ்தானங்களின் பிரதிநிதிகள் முதன்முதலில் அவையில் தங்களது இடங்களை எடுத்துக்கொண்டனர்\n4. தேசியக் கொடிக்கான தற்காலிகக் குழு அமைக்கப்பட்டது",
    ["Introduction of the Objectives Resolution by Jawaharlal Nehru", "Unanimous adoption of the Objectives Resolution by the Assembly", "Representatives of six Princely States take their seats in the Assembly for the first time", "Setting up of the Ad hoc Committee on the National Flag"],
    ["ஜவகர்லால் நேருவால் குறிக்கோள்கள் தீர்மானம் அறிமுகப்படுத்தப்பட்டது", "அவையால் குறிக்கோள்கள் தீர்மானம் ஒருமனதாக ஏற்றுக்கொள்ளப்பட்டது", "ஆறு சுதேச சமஸ்தானங்களின் பிரதிநிதிகள் முதன்முதலில் அவையில் தங்களது இடங்களை எடுத்துக்கொண்டனர்", "தேசியக் கொடிக்கான தற்காலிகக் குழு அமைக்கப்பட்டது"],
    "1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "3 -> 1 -> 2 -> 4",
    "A",
    "Correct Chronological Sequence: 1 (Objectives Resolution introduced, Dec 13, 1946) -> 2 (Objectives Resolution adopted, Jan 22, 1947) -> 3 (6 Princely States joined, April 28, 1947) -> 4 (Ad hoc Flag Committee setup, June 23, 1947).",
    "சரியான காலவரிசை: 1 (குறிக்கோள்கள் தீர்மானம் அறிமுகம், டிச 13, 1946) -> 2 (குறிக்கோள்கள் தீர்மானம் ஏற்பு, ஜன 22, 1947) -> 3 (6 சமஸ்தானங்கள் இணைவு, ஏப்ரல் 28, 1947) -> 4 (தேசியக் கொடிக் குழு அமைப்பு, ஜூன் 23, 1947).",
    "Correct. 1 (Dec 1946) -> 2 (Jan 1947) -> 3 (April 1947) -> 4 (June 1947) is exact.", "சரி. 1 (டிச 1946) -> 2 (ஜன 1947) -> 3 (ஏப்ரல் 1947) -> 4 (ஜூன் 1947) துல்லியமானது.",
    "Incorrect. Objectives Resolution was introduced (1) before it was adopted (2).", "தவறு. குறிக்கோள்கள் தீர்மானம் அறிமுகம் (1) ஏற்பிற்கு முந்தியது (2).",
    "Incorrect. Objectives Resolution was adopted (2) before 6 Princely States joined in April 1947 (3).", "தவறு. குறிக்கோள்கள் தீர்மானம் ஏற்பு (2) சமஸ்தானங்கள் இணைவிற்கு முந்தியது (3).",
    "Incorrect. Objectives Resolution was introduced (1) before 6 Princely States joined (3).", "தவறு. குறிக்கோள்கள் தீர்மானம் அறிமுகம் (1) சமஸ்தானங்கள் இணைவிற்கு முந்தியது (3).",
    "TNPSC Trap: Objectives Resolution introduced = Dec 13, 1946. Adopted = Jan 22, 1947. 6 Princely States joined = April 28, 1947. Ad hoc Flag Committee = June 23, 1947.",
    "TNPSC பொறி: குறிக்கோள்கள் தீர்மானம் அறிமுகம் = டிசம்பர் 13, 1946. ஏற்பு = ஜனவரி 22, 1947. 6 சமஸ்தானங்கள் இணைந்தது = ஏப்ரல் 28, 1947. தேசியக் கொடிக் குழு = ஜூன் 23, 1947.",
    "The 6 states that joined on April 28, 1947 were Baroda, Bikaner, Jaipur, Patiala, Rewa, and Udaipur.",
    "ஏப்ரல் 28, 1947 இல் சேர்ந்த 6 சமஸ்தானங்கள்: பரோடா, பிகானேர், ஜெய்ப்பூர், பட்டியாலா, ரேவா மற்றும் உதய்பூர்.",
    "Analyze", 75, ["Polity", "Making of Indian Constitution", "Objectives Resolution", "Princely State Representation", "National Flag adoption"]
))

# MIC_CHRONO_005
questions.append(make_chrono_q(
    "MIC_CHRONO_005", "Chronology",
    "Which one of the following represents the correct sequence of events surrounding Independence and Partition in 1947?\n1. Announcement of Mountbatten Plan (June 3 Plan)\n2. Royal Assent to the Indian Independence Act, 1947 by British Crown\n3. Adoption of the National Flag of India by Constituent Assembly\n4. Formal Transfer of Power and Independence of India",
    "1947 இல் சுதந்திரம் மற்றும் பிரிவினை தொடர்பான நிகழ்வுகளின் சரியான வரிசை எது?\n1. மவுண்ட்பேட்டன் திட்டம் அறிவிக்கப்படுதல் (ஜூன் 3 திட்டம்)\n2. பிரிட்டிஷ் அரசரால் 1947 இந்திய சுதந்திரச் சட்டத்திற்கு ஒப்புதல் அளிக்கப்படுதல்\n3. அரசியலமைப்பு அவையால் இந்திய தேசியக் கொடி ஏற்றுக்கொள்ளப்படுதல்\n4. அதிகாரப்பூர்வ அதிகார பரிமாற்றம் மற்றும் இந்திய சுதந்திரம்",
    ["Announcement of Mountbatten Plan (June 3 Plan)", "Royal Assent to the Indian Independence Act, 1947 by British Crown", "Adoption of the National Flag of India by Constituent Assembly", "Formal Transfer of Power and Independence of India"],
    ["மவுண்ட்பேட்டன் திட்டம் அறிவிக்கப்படுதல் (ஜூன் 3 திட்டம்)", "பிரிட்டிஷ் அரசரால் 1947 இந்திய சுதந்திரச் சட்டத்திற்கு ஒப்புதல் அளிக்கப்படுதல்", "அரசியலமைப்பு அவையால் இந்திய தேசியக் கொடி ஏற்றுக்கொள்ளப்படுதல்", "அதிகாரப்பூர்வ அதிகார பரிமாற்றம் மற்றும் இந்திய சுதந்திரம்"],
    "1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "3 -> 1 -> 2 -> 4",
    "A",
    "Correct Chronological Sequence: 1 (Mountbatten Plan, June 3, 1947) -> 2 (Royal Assent to Indian Independence Act, July 18, 1947) -> 3 (Adoption of National Flag, July 22, 1947) -> 4 (Independence of India, Aug 15, 1947).",
    "சரியான காலவரிசை: 1 (மவுண்ட்பேட்டன் திட்டம், ஜூன் 3, 1947) -> 2 (சுதந்திரச் சட்ட அரச ஒப்புதல், ஜூலை 18, 1947) -> 3 (தேசியக் கொடி ஏற்பு, ஜூலை 22, 1947) -> 4 (இந்திய சுதந்திரம், ஆகஸ்ட் 15, 1947).",
    "Correct. 1 (June 3) -> 2 (July 18) -> 3 (July 22) -> 4 (August 15) is exact.", "சரி. 1 (ஜூன் 3) -> 2 (ஜூலை 18) -> 3 (ஜூலை 22) -> 4 (ஆகஸ்ட் 15) துல்லியமானது.",
    "Incorrect. Mountbatten Plan (June 3) preceded Royal Assent to Independence Act (July 18).", "தவறு. மவுண்ட்பேட்டன் திட்டம் (ஜூன் 3) அரச ஒப்புதலுக்கு முந்தியது (ஜூலை 18).",
    "Incorrect. Royal Assent (July 18) occurred before National Flag adoption (July 22).", "தவறு. அரச ஒப்புதல் (ஜூலை 18) தேசியக் கொடி ஏற்பிற்கு முந்தியது (ஜூலை 22).",
    "Incorrect. Mountbatten Plan (June 3) preceded National Flag adoption (July 22).", "தவறு. மவுண்ட்பேட்டன் திட்டம் (ஜூன் 3) தேசியக் கொடி ஏற்பிற்கு முந்தியது (ஜூலை 22).",
    "TNPSC Trap: Indian Independence Act Royal Assent = July 18, 1947. National Flag Adoption = July 22, 1947 (Flag adopted 4 days after Royal Assent!).",
    "TNPSC பொறி: சுதந்திரச் சட்ட அரச ஒப்புதல் = ஜூலை 18, 1947. தேசியக் கொடி ஏற்பு = ஜூலை 22, 1947 (ஒப்புதல் அளித்த 4 நாட்களுக்குப் பின் கொடி ஏற்கப்பட்டது!).",
    "Lord Mountbatten was the last Viceroy of British India and 1st Governor-General of independent Dominion of India.",
    "மவுண்ட்பேட்டன் பிரபு பிரிட்டிஷ் இந்தியாவின் கடைசி வைஸ்ராய் மற்றும் சுதந்திர இந்திய டொமினியனின் 1வது கவர்னர்-ஜெனரல் ஆவார்.",
    "Analyze", 75, ["Polity", "Making of Indian Constitution", "Mountbatten Plan", "Partition Events", "National Flag adoption"]
))

# MIC_CHRONO_006
questions.append(make_chrono_q(
    "MIC_CHRONO_006", "Chronology",
    "Arrange the following stages of drafting the Indian Constitution in correct chronological order:\n1. Setting up of the Drafting Committee under the Chairmanship of Dr. B.R. Ambedkar\n2. Sir B.N. Rau prepares the initial draft of the Constitution containing 243 Articles\n3. Publication of the First Draft of the Constitution for public scrutiny and comments\n4. Publication of the Second (Revised) Draft of the Constitution by the Drafting Committee",
    "இந்திய அரசியலமைப்பை வரைவதன் பின்வரும் கட்டங்களை சரியான காலவரிசையில் அமைக்கவும்:\n1. டாக்டர் பி.ஆர். அம்பேத்கர் தலைமையில் வரைவுக் குழு அமைக்கப்படுதல்\n2. சர் பி.என். ராவ் 243 சரத்துகளைக் கொண்ட அரசியலமைப்பின் ஆரம்ப வரைவைத் தயாரித்தல்\n3. மக்கள் பரிசீலனை மற்றும் கருத்துகளுக்காக அரசியலமைப்பின் முதல் வரைவு வெளியிடப்படுதல்\n4. வரைவுக் குழுவால் அரசியலமைப்பின் இரண்டாவது (திருத்தப்பட்ட) வரைவு வெளியிடப்படுதல்",
    ["Setting up of the Drafting Committee under the Chairmanship of Dr. B.R. Ambedkar", "Sir B.N. Rau prepares the initial draft of the Constitution containing 243 Articles", "Publication of the First Draft of the Constitution for public scrutiny and comments", "Publication of the Second (Revised) Draft of the Constitution by the Drafting Committee"],
    ["டாக்டர் பி.ஆர். அம்பேத்கர் தலைமையில் வரைவுக் குழு அமைக்கப்படுதல்", "சர் பி.என். ராவ் 243 சரத்துகளைக் கொண்ட அரசியலமைப்பின் ஆரம்ப வரைவைத் தயாரித்தல்", "மக்கள் பரிசீலனை மற்றும் கருத்துகளுக்காக அரசியலமைப்பின் முதல் வரைவு வெளியிடப்படுதல்", "வரைவுக் குழுவால் அரசியலமைப்பின் இரண்டாவது (திருத்தப்பட்ட) வரைவு வெளியிடப்படுதல்"],
    "1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "3 -> 1 -> 2 -> 4",
    "A",
    "Correct Chronological Sequence: 1 (Drafting Committee setup, Aug 29, 1947) -> 2 (Sir B.N. Rau draft, Oct 1947) -> 3 (First Draft published, Feb 1948) -> 4 (Second Draft published, Oct 1948).",
    "சரியான காலவரிசை: 1 (வரைவுக் குழு அமைப்பு, ஆகஸ்ட் 29, 1947) -> 2 (பி.என். ராவ் வரைவு, அக்டோபர் 1947) -> 3 (முதல் வரைவு வெளியீடு, பிப்ரவரி 1948) -> 4 (இரண்டாவது வரைவு வெளியீடு, அக்டோபர் 1948).",
    "Correct. 1 (Aug 1947) -> 2 (Oct 1947) -> 3 (Feb 1948) -> 4 (Oct 1948) is exact.", "சரி. 1 (ஆகஸ்ட் 1947) -> 2 (அக்டோபர் 1947) -> 3 (பிப்ரவரி 1948) -> 4 (அக்டோபர் 1948) துல்லியமானது.",
    "Incorrect. Drafting Committee was set up in Aug 1947 (1), before B.N. Rau completed initial draft in Oct 1947 (2).", "தவறு. வரைவுக் குழு ஆகஸ்ட் 1947 இல் அமைக்கப்பட்டது (1).",
    "Incorrect. First Draft was published in Feb 1948 (3), before Second Draft in Oct 1948 (4).", "தவறு. முதல் வரைவு பிப்ரவரி 1948 இல் வெளியிடப்பட்டது (3).",
    "Incorrect. Drafting Committee setup (1) preceded First Draft publication (3).", "தவறு. வரைவுக் குழு அமைப்பு (1) முதல் வரைவு வெளியீட்டிற்கு முந்தியது (3).",
    "TNPSC Trap: Drafting Committee setup = Aug 29, 1947. B.N. Rau Draft = Oct 1947. 1st Draft published = Feb 1948 (8 months given). 2nd Draft published = Oct 1948.",
    "TNPSC பொறி: வரைவுக் குழு அமைப்பு = ஆகஸ்ட் 29, 1947. பி.என். ராவ் வரைவு = அக்டோபர் 1947. 1வது வரைவு வெளியீடு = பிப்ரவரி 1948 (8 மாதங்கள் அவகாசம்). 2வது வரைவு வெளியீடு = அக்டோபர் 1948.",
    "The public was given 8 months to discuss the first draft and propose amendments.",
    "முதல் வரைவை விவாதித்து திருத்தங்களை முன்மொழிய மக்களுக்கு 8 மாத காலம் வழங்கப்பட்டது.",
    "Analyze", 75, ["Polity", "Making of Indian Constitution", "Drafting Committee", "B. N. Rau", "Draft Constitution Publication"]
))

# MIC_CHRONO_007
questions.append(make_chrono_q(
    "MIC_CHRONO_007", "Chronology",
    "Identify the correct order of the debate and reading stages of the Draft Constitution in the Constituent Assembly:\n1. Dr. Ambedkar introduces Final Draft Constitution in Assembly (First Reading)\n2. Commencement of Second Reading (clause-by-clause consideration)\n3. Completion of Second Reading after discussing 2,473 amendments\n4. Commencement of Third Reading on the motion 'that the Constitution as settled by the Assembly be passed'",
    "அரசியலமைப்பு நிர்ணய அவையில் வரைவு அரசியலமைப்பின் விவாதம் மற்றும் வாசிப்பு கட்டங்களின் சரியான வரிசையை அடையாளம் காணவும்:\n1. அம்பேத்கர் இறுதி வரைவு அரசியலமைப்பை அவையில் அறிமுகப்படுத்துதல் (முதல் வாசிப்பு)\n2. 2வது வாசிப்பு தொடங்குதல் (சரத்து வாரியான பரிசீலனை)\n3. 2,473 திருத்தங்களை விவாதித்த பிறகு 2வது வாசிப்பு நிறைவடைதல்\n4. 'அவையால் தீர்மானிக்கப்பட்ட அரசியலமைப்பு நிறைவேற்றப்பட வேண்டும்' என்ற தீர்மானத்தின் மீதான 3வது வாசிப்பு தொடங்குதல்",
    ["Dr. Ambedkar introduces Final Draft Constitution in Assembly (First Reading)", "Commencement of Second Reading (clause-by-clause consideration)", "Completion of Second Reading after discussing 2,473 amendments", "Commencement of Third Reading on the motion 'that the Constitution as settled by the Assembly be passed'"],
    ["அம்பேத்கர் இறுதி வரைவு அரசியலமைப்பை அவையில் அறிமுகப்படுத்துதல் (முதல் வாசிப்பு)", "2வது வாசிப்பு தொடங்குதல் (சரத்து வாரியான பரிசீலனை)", "2,473 திருத்தங்களை விவாதித்த பிறகு 2வது வாசிப்பு நிறைவடைதல்", "‘அவையால் தீர்மானிக்கப்பட்ட அரசியலமைப்பு நிறைவேற்றப்பட வேண்டும்’ என்ற தீர்மானத்தின் மீதான 3வது வாசிப்பு தொடங்குதல்"],
    "1 -> 2 -> 3 -> 4", "2 -> 1 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "3 -> 1 -> 2 -> 4",
    "A",
    "Correct Chronological Sequence: 1 (First Reading introduced, Nov 4, 1948) -> 2 (Second Reading started, Nov 15, 1948) -> 3 (Second Reading completed, Oct 17, 1949) -> 4 (Third Reading started, Nov 14, 1949).",
    "சரியான காலவரிசை: 1 (முதல் வாசிப்பு அறிமுகம், நவ 4, 1948) -> 2 (2வது வாசிப்பு தொடக்கம், நவ 15, 1948) -> 3 (2வது வாசிப்பு முடிவு, அக்டோபர் 17, 1949) -> 4 (3வது வாசிப்பு தொடக்கம், நவ 14, 1949).",
    "Correct. 1 (Nov 4, 1948) -> 2 (Nov 15, 1948) -> 3 (Oct 17, 1949) -> 4 (Nov 14, 1949) is exact.", "சரி. 1 (நவ 4, 1948) -> 2 (நவ 15, 1948) -> 3 (அக்டோபர் 17, 1949) -> 4 (நவ 14, 1949) துல்லியமானது.",
    "Incorrect. First Reading (Nov 4) preceded Second Reading commencement (Nov 15).", "தவறு. முதல் வாசிப்பு (நவ 4) 2வது வாசிப்பு தொடக்கத்திற்கு முந்தியது (நவ 15).",
    "Incorrect. Second Reading started (Nov 15, 1948) before it completed (Oct 17, 1949).", "தவறு. 2வது வாசிப்பு தொடக்கம் (நவ 15, 1948) அதன் முடிவிற்கு முந்தியது.",
    "Incorrect. First Reading (Nov 4) preceded Second Reading completion (Oct 17, 1949).", "தவறு. முதல் வாசிப்பு (நவ 4) 2வது வாசிப்பு முடிவிற்கு முந்தியது.",
    "TNPSC Trap: First Reading = Nov 4-9, 1948. Second Reading = Nov 15, 1948 to Oct 17, 1949. Third Reading = Nov 14-26, 1949.",
    "TNPSC பொறி: முதல் வாசிப்பு = நவம்பர் 4-9, 1948. 2வது வாசிப்பு = நவம்பர் 15, 1948 முதல் அக்டோபர் 17, 1949 வரை. 3வது வாசிப்பு = நவம்பர் 14-26, 1949.",
    "Out of 7,635 amendments tabled during second reading, 2,473 were actually moved and discussed.",
    "2வது வாசிப்பின் போது தாக்கல் செய்யப்பட்ட 7,635 திருத்தங்களில் 2,473 உண்மையில் விவாதிக்கப்பட்டன.",
    "Analyze", 75, ["Polity", "Making of Indian Constitution", "Debate Stages", "Draft Constitution"]
))

# MIC_CHRONO_008
questions.append(make_chrono_q(
    "MIC_CHRONO_008", "Chronology",
    "Which of the following represents the correct sequence of events in the final enactment and implementation of the Constitution?\n1. Adoption and passing of the Constitution by Constituent Assembly\n2. Final session of Constituent Assembly and signing by 284 members\n3. Adoption of National Anthem ('Jana Gana Mana') and National Song ('Vande Mataram')\n4. Commencement / Full Enforcement of Constitution & 1st Republic Day",
    "அரசியலமைப்பின் இறுதி இயற்றல் மற்றும் செயலாக்கத்தில் நடந்த நிகழ்வுகளின் சரியான வரிசை எது?\n1. அரசியலமைப்பு அவையால் அரசியலமைப்பு ஏற்றுக்கொள்ளப்பட்டு நிறைவேற்றப்படுதல்\n2. அரசியலமைப்பு அவையின் இறுதி அமர்வு மற்றும் 284 உறுப்பினர்கள் கையெழுத்திடுதல்\n3. தேசிய கீதம் ('ஜன கண மன') மற்றும் தேசியப் பாடல் ('வந்தே மாதரம்') ஏற்றுக்கொள்ளப்படுதல்\n4. அரசியலமைப்பு தொடங்குதல் / முழுமையாக நடைமுறைக்கு வருதல் & 1வது குடியரசு தினம்",
    ["Adoption and passing of the Constitution by Constituent Assembly", "Final session of Constituent Assembly and signing by 284 members", "Adoption of National Anthem ('Jana Gana Mana') and National Song ('Vande Mataram')", "Commencement / Full Enforcement of Constitution & 1st Republic Day"],
    ["அரசியலமைப்பு அவையால் அரசியலமைப்பு ஏற்றுக்கொள்ளப்பட்டு நிறைவேற்றப்படுதல்", "அரசியலமைப்பு அவையின் இறுதி அமர்வு மற்றும் 284 உறுப்பினர்கள் கையெழுத்திடுதல்", "தேசிய கீதம் ('ஜன கண மன') மற்றும் தேசியப் பாடல் ('வந்தே மாதரம்') ஏற்றுக்கொள்ளப்படுதல்", "அரசியலமைப்பு தொடங்குதல் / முழுமையாக நடைமுறைக்கு வருதல் & 1வது குடியரசு தினம்"],
    "1 -> 2 -> 3 -> 4", "1 -> 3 -> 2 -> 4", "2 -> 1 -> 3 -> 4", "3 -> 1 -> 2 -> 4",
    "B",
    "Correct Chronological Sequence: 1 (Adoption of Constitution, Nov 26, 1949) -> 3 (Adoption of Anthem/Song, Jan 24, 1950 morning) -> 2 (Signing of Constitution by 284 members in final session, Jan 24, 1950) -> 4 (Commencement & Republic Day, Jan 26, 1950). Note: On Jan 24, 1950, adoption of Anthem/Song and election of President preceded signing of Constitution.",
    "சரியான காலவரிசை: 1 (அரசியலமைப்பு ஏற்பு, நவ 26, 1949) -> 3 (தேசிய கீதம்/பாடல் ஏற்பு, ஜன 24, 1950 காலை) -> 2 (284 உறுப்பினர்கள் கையெழுத்திடுதல், ஜன 24, 1950) -> 4 (நடைமுறைக்கு வருதல் & குடியரசு தினம், ஜன 26, 1950).",
    "Incorrect. Adoption of Anthem (Jan 24 morning) preceded final signing of copies.", "தவறு. தேசிய கீதம் ஏற்பு (ஜன 24 காலை) இறுதி கையெழுத்திற்கு முந்தியது.",
    "Correct. 1 (Nov 26, 1949) -> 3 (Jan 24, 1950) -> 2 (Jan 24, 1950) -> 4 (Jan 26, 1950) is logically ordered.", "சரி. 1 (நவ 26, 1949) -> 3 (ஜன 24, 1950) -> 2 (ஜன 24, 1950) -> 4 (ஜன 26, 1950) சரியான வரிசையாகும்.",
    "Incorrect. Adoption of Constitution (Nov 26, 1949) occurred before Jan 24, 1950.", "தவறு. அரசியலமைப்பு ஏற்பு (நவ 26, 1949) ஜனவரி 24, 1950-க்கு முந்தியது.",
    "Incorrect. Adoption of Constitution (Nov 26, 1949) occurred before Jan 24, 1950.", "தவறு. அரசியலமைப்பு ஏற்பு (நவ 26, 1949) ஜனவரி 24, 1950-க்கு முந்தியது.",
    "TNPSC Trap: Adoption Date = Nov 26, 1949. Anthem/Song Adoption & President Election & Signing = Jan 24, 1950. Commencement = Jan 26, 1950.",
    "TNPSC பொறி: ஏற்றுக்கொள்ளப்பட்ட நாள் = நவம்பர் 26, 1949. கீதம்/பாடல் ஏற்பு & தலைவர் தேர்வு & கையெழுத்து = ஜனவரி 24, 1950. நடைமுறைக்கு வந்த நாள் = ஜனவரி 26, 1950.",
    "Dr. Rajendra Prasad was the first to sign the Constitution on January 24, 1950.",
    "ஜனவரி 24, 1950 அன்று அரசியலமைப்பில் முதன்முதலில் கையெழுத்திட்டவர் டாக்டர் ராஜேந்திர பிரசாத் ஆவார்.",
    "Analyze", 75, ["Polity", "Making of Indian Constitution", "Constitution Adoption", "Constitution Signing", "Constitution Enforcement", "First Republic Day"]
))
