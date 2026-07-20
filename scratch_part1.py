import json
import os

repo = [
    # Q1: Analytical - Model 1 - Acts Chronology
    {
        "id": "HB_CHRONO_001",
        "subject": "Polity",
        "topic": "Historical Background of the Indian Constitution",
        "difficulty": "Hard",
        "question_type": "Chronology",
        "question": {
            "en": "Arrange the following key legislative provisions during Company Rule in correct chronological order:\n1. Exemption of Governor-General and Council from Supreme Court jurisdiction for official acts\n2. Establishment of Supreme Court of Judicature at Fort William, Calcutta\n3. Extension of Governor-General's overriding powers over his council to future Governors-General\n4. Establishment of the Board of Control to supervise civil, military, and revenue affairs",
            "ta": "கம்பெனி ஆட்சியின் போது மேற்கொள்ளப்பட்ட பின்வரும் முக்கிய சட்டப்பூர்வ விதிகளை சரியான காலவரிசையில் அமைக்கவும்:\n1. அதிகாரபூர்வ நடவடிக்கைகளுக்காக உச்ச நீதிமன்ற அதிகார வரம்பிலிருந்து கவர்னர்-ஜெனரல் மற்றும் கவுன்சிலுக்கு விலக்களித்தல்\n2. கொல்கத்தா வில்லியம் கோட்டையில் உச்ச நீதிமன்றம் அமைத்தல்\n3. கவர்னர்-ஜெனரலின் நிராகரிப்பு அதிகாரத்தை எதிர்கால கவர்னர்-ஜெனரல்களுக்கு நீட்டித்தல்\n4. சிவில், ராணுவ மற்றும் வருவாய் விவகாரங்களைக் கண்காணிக்கக் கட்டுப்பாட்டு வாரியத்தை அமைத்தல்"
        },
        "options": [
            {"id": "A", "en": "2 -> 1 -> 4 -> 3", "ta": "2 -> 1 -> 4 -> 3"},
            {"id": "B", "en": "1 -> 2 -> 3 -> 4", "ta": "1 -> 2 -> 3 -> 4"},
            {"id": "C", "en": "2 -> 4 -> 1 -> 3", "ta": "2 -> 4 -> 1 -> 3"},
            {"id": "D", "en": "4 -> 2 -> 1 -> 3", "ta": "4 -> 2 -> 1 -> 3"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Correct Chronological Sequence:\n1. Establishment of Supreme Court at Fort William: 1774 (under Regulating Act, 1773).\n2. Exemption of GG-in-Council from SC jurisdiction: 1781 (Amending Act of 1781 / Act of Settlement).\n3. Establishment of Board of Control: 1784 (Pitt's India Act, 1784).\n4. Extension of GG's overriding powers over Council: 1793 (Charter Act, 1793).\n\nConstitutional Significance: This sequence marks the initial Parliamentary attempt to regulate EIC governance, clarify executive-judicial boundaries, establish dual control (Directors & Board), and solidify central executive command.",
            "ta": "சரியான காலவரிசை:\n1. வில்லியம் கோட்டையில் உச்ச நீதிமன்றம் அமைத்தல்: 1774 (1773 ஒழுங்குமுறைச் சட்டத்தின் கீழ்).\n2. கவர்னர்-ஜெனரலுக்கு உச்ச நீதிமன்ற அதிகார வரம்பிலிருந்து விலக்களித்தல்: 1781 (1781 திருத்தச் சட்டம் / சீரமைப்புச் சட்டம்).\n3. கட்டுப்பாட்டு வாரியம் அமைத்தல்: 1784 (1784 பிட் இந்தியச் சட்டம்).\n4. கவர்னர்-ஜெனரலின் நிராகரிப்பு அதிகாரத்தை நீட்டித்தல்: 1793 (1793 சாசனச் சட்டம்).\n\nஅரசியலமைப்பு முக்கியத்துவம்: இக்காலவரிசை கிழக்கிந்திய கம்பெனியின் நிர்வாகத்தை ஒழுங்குபடுத்தவும், நிர்வாக-நீதிமன்ற எல்லைகளைத் தெளிவுபடுத்தவும், இரட்டைப் பகுப்பாய்வு அமைப்பை ஏற்படுத்தவும் நாடாளுமன்றம் மேற்கொண்ட தொடக்ககால முயற்சிகளைக் காட்டுகிறது."
        },
        "why_not_others": {
            "A": {"en": "Correct. 2 (1774) -> 1 (1781) -> 4 (1784) -> 3 (1793) perfectly follows historical enactment dates.", "ta": "சரி. 2 (1774) -> 1 (1781) -> 4 (1784) -> 3 (1793) வரலாற்று சட்ட இயற்றல் ஆண்டுகளைத் துல்லியமாகப் பின்பற்றுகிறது."},
            "B": {"en": "Incorrect. Exemption from SC jurisdiction (1781) occurred AFTER Supreme Court was established (1774).", "ta": "தவறு. உச்ச நீதிமன்ற விலக்களிப்பு (1781) உச்ச நீதிமன்றம் அமைக்கப்பட்ட பின்னரே (1774) ஏற்பட்டது."},
            "C": {"en": "Incorrect. Board of Control was established in 1784, after the Amending Act of 1781.", "ta": "தவறு. கட்டுப்பாட்டு வாரியம் 1784-ல் அமைக்கப்பட்டது, இது 1781 திருத்தச் சட்டத்திற்குப் பின்னராகும்."},
            "D": {"en": "Incorrect. Board of Control (1784) was not established before the Supreme Court (1774).", "ta": "தவறு. கட்டுப்பாட்டு வாரியம் (1784) உச்ச நீதிமன்றத்திற்கு (1774) முன் அமைக்கப்படவில்லை."}
        },
        "tnpsc_tip": {
            "en": "TNPSC Trap: Candidates confuse Supreme Court creation under 1773 Act (established 1774) with the Amending Act 1781 which resolved the jurisdiction clashes.",
            "ta": "TNPSC பொறி: 1773 சட்டத்தின் கீழ் அமைக்கப்பட்ட உச்ச நீதிமன்றத்தையும் (1774), அதன் அதிகார வரம்பு மோதல்களைத் தீர்த்த 1781 திருத்தச் சட்டத்தையும் குழப்பிக் கொள்ளக் கூடாது."
        },
        "revision_fact": {
            "en": "The Amending Act of 1781 is also officially known as the 'Act of Settlement'.",
            "ta": "1781 ஆம் ஆண்டின் திருத்தச் சட்டம் அதிகாரப்பூர்வமாக 'சீரமைப்புச் சட்டம்' (Act of Settlement) என்று அழைக்கப்படுகிறது."
        },
        "source_reference": [
            "M. Laxmikanth - Indian Polity",
            "NCERT Class XI/XII - Indian Constitution at Work",
            "Samacheer Kalvi - Standard 11/12 Political Science"
        ],
        "bloom_level": "Analyze",
        "estimated_time_sec": 75,
        "pyq_similarity": "High",
        "tags": ["Polity", "Historical Background", "Chronology", "Company Rule", "Regulating Act 1773"],
        "question_en": "Arrange the following key legislative provisions during Company Rule in correct chronological order:\n1. Exemption of Governor-General and Council from Supreme Court jurisdiction for official acts\n2. Establishment of Supreme Court of Judicature at Fort William, Calcutta\n3. Extension of Governor-General's overriding powers over his council to future Governors-General\n4. Establishment of the Board of Control to supervise civil, military, and revenue affairs",
        "question_ta": "கம்பெனி ஆட்சியின் போது மேற்கொள்ளப்பட்ட பின்வரும் முக்கிய சட்டப்பூர்வ விதிகளை சரியான காலவரிசையில் அமைக்கவும்:\n1. அதிகாரபூர்வ நடவடிக்கைகளுக்காக உச்ச நீதிமன்ற அதிகார வரம்பிலிருந்து கவர்னர்-ஜெனரல் மற்றும் கவுன்சிலுக்கு விலக்களித்தல்\n2. கொல்கத்தா வில்லியம் கோட்டையில் உச்ச நீதிமன்றம் அமைத்தல்\n3. கவர்னர்-ஜெனரலின் நிராகரிப்பு அதிகாரத்தை எதிர்கால கவர்னர்-ஜெனரல்களுக்கு நீட்டித்தல்\n4. சிவில், ராணுவ மற்றும் வருவாய் விவகாரங்களைக் கண்காணிக்கக் கட்டுப்பாட்டு வாரியத்தை அமைத்தல்",
        "options_en": ["2 -> 1 -> 4 -> 3", "1 -> 2 -> 3 -> 4", "2 -> 4 -> 1 -> 3", "4 -> 2 -> 1 -> 3"],
        "options_ta": ["2 -> 1 -> 4 -> 3", "1 -> 2 -> 3 -> 4", "2 -> 4 -> 1 -> 3", "4 -> 2 -> 1 -> 3"],
        "answer": "a",
        "explanation_en": "Sequence: 2 (1774 Supreme Court) -> 1 (1781 Exemption) -> 4 (1784 Board of Control) -> 3 (1793 Charter Act).",
        "explanation_ta": "வரிசை: 2 (1774 உச்ச நீதிமன்றம்) -> 1 (1781 விலக்களிப்பு) -> 4 (1784 கட்டுப்பாட்டு வாரியம்) -> 3 (1793 சாசனச் சட்டம்)."
    },

    # Q2: Analytical - Model 1 - Acts Chronology
    {
        "id": "HB_CHRONO_002",
        "subject": "Polity",
        "topic": "Historical Background of the Indian Constitution",
        "difficulty": "Hard",
        "question_type": "Chronology",
        "question": {
            "en": "Arrange the following Charter Acts and Parliamentary Acts in correct chronological sequence based on the gradual reduction of East India Company's privileges:\n1. Total abolition of EIC commercial monopoly (including tea and trade with China)\n2. Partial abolition of EIC trade monopoly in India, retaining monopoly in tea and trade with China\n3. Complete transfer of Indian administration from EIC to the British Crown\n4. Extension of EIC charter without specifying any fixed time period for the first time",
            "ta": "கிழக்கிந்திய கம்பெனியின் சலுகைகள் படிப்படியாகக் குறைக்கப்பட்டதன் அடிப்படையில் பின்வரும் சாசனச் சட்டங்கள் மற்றும் நாடாளுமன்றச் சட்டங்களை சரியான காலவரிசையில் அமைக்கவும்:\n1. தேயிலை மற்றும் சீனாவுடனான வர்த்தகம் உட்பட கம்பெனியின் வர்த்தக முற்றுரிமை முழுமையாக ஒழிக்கப்படல்\n2. தேயிலை மற்றும் சீனா வர்த்தகம் தவிர்த்து இந்தியாவில் கம்பெனியின் வர்த்தக முற்றுரிமை பகுதியளவாக ஒழிக்கப்படல்\n3. இந்திய நிர்வாகம் கிழக்கிந்திய கம்பெனியிடமிருந்து பிரிட்டிஷ் முடிக்கு முழுமையாக மாற்றப்படல்\n4. எந்தவொரு குறிப்பிட்ட காலவரையறையுமின்றி கம்பெனியின் சாசனம் முதன்முறையாக நீட்டிக்கப்படல்"
        },
        "options": [
            {"id": "A", "en": "1 -> 2 -> 4 -> 3", "ta": "1 -> 2 -> 4 -> 3"},
            {"id": "B", "en": "2 -> 1 -> 4 -> 3", "ta": "2 -> 1 -> 4 -> 3"},
            {"id": "C", "en": "2 -> 4 -> 1 -> 3", "ta": "2 -> 4 -> 1 -> 3"},
            {"id": "D", "en": "4 -> 2 -> 1 -> 3", "ta": "4 -> 2 -> 1 -> 3"}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "Correct Chronological Sequence:\n1. Partial abolition of trade monopoly (retaining tea & China): Charter Act of 1813.\n2. Total abolition of EIC trade monopoly: Charter Act of 1833.\n3. Extension of charter without fixed time period: Charter Act of 1853.\n4. Complete transfer of power to Crown: Government of India Act 1858.\n\nConstitutional Significance: This progression illustrates how the British Parliament systematically stripped EIC of commercial monopoly, transformed it into a political administrative entity, kept its tenure indefinite in 1853, and finally abolished Company Rule in 1858.",
            "ta": "சரியான காலவரிசை:\n1. பகுதியளவு வர்த்தக முற்றுரிமை ஒழிப்பு (தேயிலை & சீனா தவிர): 1813 சாசனச் சட்டம்.\n2. கம்பெனி வர்த்தக முற்றுரிமை முழுமையாக ஒழிப்பு: 1833 சாசனச் சட்டம்.\n3. குறிப்பிட்ட காலவரையறையின்றி சாசனம் நீட்டிப்பு: 1853 சாசனச் சட்டம்.\n4. பிரிட்டிஷ் முடிக்கு அதிகாரம் முழுமையாக மாற்றம்: 1858 இந்திய அரசுச் சட்டம்.\n\nஅரசியலமைப்பு முக்கியத்துவம்: இக்காலவரிசை பிரிட்டிஷ் நாடாளுமன்றம் கம்பெனியின் வணிக முற்றுரிமையை எவ்வாறு படிப்படியாக நீக்கி, அதை நிர்வாக அமைப்பாக மாற்றி, 1858-ல் முடிக்கு அதிகாரத்தை மாற்றியது என்பதை விளக்குகிறது."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Total abolition of monopoly (1833) happened AFTER partial abolition (1813).", "ta": "தவறு. முழுமையான வர்த்தக முற்றுரிமை ஒழிப்பு (1833) பகுதியளவு ஒழிப்புக்கு (1813) பிறகே நடந்தது."},
            "B": {"en": "Correct. Sequence 2 (1813) -> 1 (1833) -> 4 (1853) -> 3 (1858) accurately tracks Charter Act evolution.", "ta": "சரி. 2 (1813) -> 1 (1833) -> 4 (1853) -> 3 (1858) வரிசை சாசனச் சட்டங்களின் வளர்ச்சியைத் துல்லியமாகக் காட்டுகிறது."},
            "C": {"en": "Incorrect. Indefinite charter extension (1853) came AFTER 1833 Act.", "ta": "தவறு. காலவரையறையற்ற சாசன நீட்டிப்பு (1853) 1833 சட்டத்திற்குப் பின்னரே வந்தது."},
            "D": {"en": "Incorrect. Charter Act of 1853 (4) was the last of the four Charter Acts.", "ta": "தவறு. 1853 சாசனச் சட்டம் (4) நான்கு சாசனச் சட்டங்களில் இறுதியானதாகும்."}
        },
        "tnpsc_tip": {
            "en": "TNPSC Trap: Remember that earlier Charter Acts (1793, 1813, 1833) renewed the charter for 20 years, whereas Charter Act of 1853 did NOT specify a 20-year period, signalling imminent Crown takeover.",
            "ta": "TNPSC பொறி: முந்தைய சாசனச் சட்டங்கள் (1793, 1813, 1833) 20 ஆண்டுகள் நீடித்தன; ஆனால் 1853 சாசனச் சட்டம் 20 ஆண்டுக் கெடுவை விதிக்கவில்லை."
        },
        "revision_fact": {
            "en": "The Charter Act of 1833 designated the Governor-General of Bengal as the 'Governor-General of India'.",
            "ta": "1833 சாசனச் சட்டம் வங்காளத்தின் கவர்னர்-ஜெனரலை 'இந்தியாவின் கவர்னர்-ஜெனரல்' என மாற்றியமைத்தது."
        },
        "source_reference": [
            "M. Laxmikanth - Indian Polity",
            "NCERT Class XI/XII - Indian Constitution at Work",
            "Samacheer Kalvi - Standard 11/12 Political Science"
        ],
        "bloom_level": "Analyze",
        "estimated_time_sec": 75,
        "pyq_similarity": "High",
        "tags": ["Polity", "Historical Background", "Chronology", "Charter Acts", "Commercial Monopoly"],
        "question_en": "Arrange the following Charter Acts and Parliamentary Acts in correct chronological sequence based on the gradual reduction of East India Company's privileges:\n1. Total abolition of EIC commercial monopoly (including tea and trade with China)\n2. Partial abolition of EIC trade monopoly in India, retaining monopoly in tea and trade with China\n3. Complete transfer of Indian administration from EIC to the British Crown\n4. Extension of EIC charter without specifying any fixed time period for the first time",
        "question_ta": "கிழக்கிந்திய கம்பெனியின் சலுகைகள் படிப்படியாகக் குறைக்கப்பட்டதன் அடிப்படையில் பின்வரும் சாசனச் சட்டங்கள் மற்றும் நாடாளுமன்றச் சட்டங்களை சரியான காலவரிசையில் அமைக்கவும்:\n1. தேயிலை மற்றும் சீனாவுடனான வர்த்தகம் உட்பட கம்பெனியின் வர்த்தக முற்றுரிமை முழுமையாக ஒழிக்கப்படல்\n2. தேயிலை மற்றும் சீனா வர்த்தகம் தவிர்த்து இந்தியாவில் கம்பெனியின் வர்த்தக முற்றுரிமை பகுதியளவாக ஒழிக்கப்படல்\n3. இந்திய நிர்வாகம் கிழக்கிந்திய கம்பெனியிடமிருந்து பிரிட்டிஷ் முடிக்கு முழுமையாக மாற்றப்படல்\n4. எந்தவொரு குறிப்பிட்ட காலவரையறையுமின்றி கம்பெனியின் சாசனம் முதன்முறையாக நீட்டிக்கப்படல்",
        "options_en": ["1 -> 2 -> 4 -> 3", "2 -> 1 -> 4 -> 3", "2 -> 4 -> 1 -> 3", "4 -> 2 -> 1 -> 3"],
        "options_ta": ["1 -> 2 -> 4 -> 3", "2 -> 1 -> 4 -> 3", "2 -> 4 -> 1 -> 3", "4 -> 2 -> 1 -> 3"],
        "answer": "b",
        "explanation_en": "Sequence: 2 (1813 Act) -> 1 (1833 Act) -> 4 (1853 Act) -> 3 (1858 Act).",
        "explanation_ta": "வரிசை: 2 (1813 சட்டம்) -> 1 (1833 சட்டம்) -> 4 (1853 சட்டம்) -> 3 (1858 சட்டம்)."
    },

    # Q3: Analytical - Model 1 - Acts Chronology
    {
        "id": "HB_CHRONO_003",
        "subject": "Polity",
        "topic": "Historical Background of the Indian Constitution",
        "difficulty": "Hard",
        "question_type": "Chronology",
        "question": {
            "en": "Arrange the following Crown Rule legislative reforms in correct chronological order:\n1. Introduction of Dyarchy in the executive government of Provinces\n2. Granting statutory recognition to Viceroy's Portfolio System and restoration of legislative powers to Presidencies\n3. Introduction of separate electorates for Muslims\n4. First use of the element of election (indirect) for non-official seats in legislative councils",
            "ta": "பிரிட்டிஷ் முடி ஆட்சியின் கீழ் கொண்டுவரப்பட்ட பின்வரும் சட்டப்பூர்வ சீர்திருத்தங்களை சரியான காலவரிசையில் அமைக்கவும்:\n1. மாகாணங்களின் நிர்வாக அரசில் இரட்டை ஆட்சி முறையை அறிமுகப்படுத்துதல்\n2. வைஸ்ராயின் இலாகா முறைக்கு சட்டப்பூர்வ அங்கீகாரம் அளித்தல் மற்றும் மாகாணங்களுக்கு சட்டமியற்றும் அதிகாரத்தை மீட்டளித்தல்\n3. முஸ்லிம்களுக்கு தனித் தொகுதிகளை அறிமுகப்படுத்துதல்\n4. சட்ட மேலவைகளில் அதிகாரப்பூர்வமற்ற இடங்களுக்கு முதன்முறையாக (மறைமுக) தேர்தல் முறையைப் பயன்படுத்துதல்"
        },
        "options": [
            {"id": "A", "en": "2 -> 3 -> 4 -> 1", "ta": "2 -> 3 -> 4 -> 1"},
            {"id": "B", "en": "4 -> 2 -> 3 -> 1", "ta": "4 -> 2 -> 3 -> 1"},
            {"id": "C", "en": "2 -> 4 -> 3 -> 1", "ta": "2 -> 4 -> 3 -> 1"},
            {"id": "D", "en": "2 -> 4 -> 1 -> 3", "ta": "2 -> 4 -> 1 -> 3"}
        ],
        "correct_answer": "C",
        "explanation": {
            "en": "Correct Chronological Sequence:\n1. Statutory recognition of Portfolio System & restoration of legislative powers to Presidencies: 1861 (Indian Councils Act 1861).\n2. Indirect election element for non-official members: 1892 (Indian Councils Act 1892).\n3. Separate electorate for Muslims: 1909 (Indian Councils Act 1909 / Morley-Minto Reforms).\n4. Dyarchy in Provinces: 1919 (Government of India Act 1919 / Montagu-Chelmsford Reforms).\n\nConstitutional Significance: This sequence tracks the expansion of representative democracy, from initial inclusion of non-officials to representative elections, communal divisions, and constitutional executive division in provinces.",
            "ta": "சரியான காலவரிசை:\n1. இலாகா முறைக்கு அங்கீகாரம் & மாகாண அதிகார மீட்பு: 1861 (இந்தியக் கவுன்சில்கள் சட்டம் 1861).\n2. மறைமுகத் தேர்தல் முறை அறிமுகம்: 1892 (இந்தியக் கவுன்சில்கள் சட்டம் 1892).\n3. முஸ்லிம்களுக்கு தனித் தொகுதி: 1909 (இந்தியக் கவுன்சில்கள் சட்டம் 1909 / மார்லி-மிண்டோ சீர்திருத்தங்கள்).\n4. மாகாண இரட்டை ஆட்சி: 1919 (இந்திய அரசுச் சட்டம் 1919 / மாண்டேகு-செம்ஸ்ஃபோர்டு சீர்திருத்தங்கள்).\n\nஅரசியலமைப்பு முக்கியத்துவம்: இக்காலவரிசை பிரதிநிதித்துவ ஜனநாயகத்தின் வளர்ச்சியைத் தொடக்க நிலை முதல் மாகாண இரட்டை ஆட்சி வரை காட்டுகிறது."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Indirect election (1892) preceded separate electorates (1909).", "ta": "தவறு. மறைமுகத் தேர்தல் (1892) தனித் தொகுதிக்கு (1909) முந்தியது."},
            "B": {"en": "Incorrect. Indian Councils Act 1861 (2) came before the 1892 Act (4).", "ta": "தவறு. 1861 இந்தியக் கவுன்சில்கள் சட்டம் (2) 1892 சட்டத்திற்கு (4) முந்தியது."},
            "C": {"en": "Correct. 2 (1861) -> 4 (1892) -> 3 (1909) -> 1 (1919) accurately depicts legislative expansion.", "ta": "சரி. 2 (1861) -> 4 (1892) -> 3 (1909) -> 1 (1919) சரியான சட்ட வளர்ச்சியை விவரிக்கிறது."},
            "D": {"en": "Incorrect. Separate electorate was 1909 (3), whereas Provincial Dyarchy was 1919 (1).", "ta": "தவறு. தனித் தொகுதி 1909 (3), ஆனால் மாகாண இரட்டை ஆட்சி 1919 (1)." }
        },
        "tnpsc_tip": {
            "en": "TNPSC Trap: Note that the word 'election' was NOT explicitly used in the Act of 1892, though the process was effectively an indirect nomination based on recommendations.",
            "ta": "TNPSC பொறி: 1892 சட்டத்தில் 'தேர்தல்' என்ற வார்த்தை வெளிப்படையாகப் பயன்படுத்தப்படவில்லை; ஆனால் பரிந்துரைகளின் அடிப்படையில் மறைமுகமாக நடைபெற்றது."
        },
        "revision_fact": {
            "en": "Lord Minto came to be known as the 'Father of Communal Electorate' for introducing separate electorates for Muslims in 1909.",
            "ta": "1909-ல் முஸ்லிம்களுக்கு தனித் தொகுதியை அறிமுகப்படுத்தியதால் பிரபு மிண்டோ 'வகுப்புவாதத் தொகுதிகளின் தந்தை' என அழைக்கப்படுகிறார்."
        },
        "source_reference": [
            "M. Laxmikanth - Indian Polity",
            "NCERT Class XI/XII - Indian Constitution at Work",
            "Samacheer Kalvi - Standard 11/12 Political Science"
        ],
        "bloom_level": "Analyze",
        "estimated_time_sec": 75,
        "pyq_similarity": "High",
        "tags": ["Polity", "Historical Background", "Chronology", "Crown Rule", "Indian Councils Acts"],
        "question_en": "Arrange the following Crown Rule legislative reforms in correct chronological order:\n1. Introduction of Dyarchy in the executive government of Provinces\n2. Granting statutory recognition to Viceroy's Portfolio System and restoration of legislative powers to Presidencies\n3. Introduction of separate electorates for Muslims\n4. First use of the element of election (indirect) for non-official seats in legislative councils",
        "question_ta": "பிரிட்டிஷ் முடி ஆட்சியின் கீழ் கொண்டுவரப்பட்ட பின்வரும் சட்டப்பூர்வ சீர்திருத்தங்களை சரியான காலவரிசையில் அமைக்கவும்:\n1. மாகாணங்களின் நிர்வாக அரசில் இரட்டை ஆட்சி முறையை அறிமுகப்படுத்துதல்\n2. வைஸ்ராயின் இலாகா முறைக்கு சட்டப்பூர்வ அங்கீகாரம் அளித்தல் மற்றும் மாகாணங்களுக்கு சட்டமியற்றும் அதிகாரத்தை மீட்டளித்தல்\n3. முஸ்லிம்களுக்கு தனித் தொகுதிகளை அறிமுகப்படுத்துதல்\n4. சட்ட மேலவைகளில் அதிகாரப்பூர்வமற்ற இடங்களுக்கு முதன்முறையாக (மறைமுக) தேர்தல் முறையைப் பயன்படுத்துதல்",
        "options_en": ["2 -> 3 -> 4 -> 1", "4 -> 2 -> 3 -> 1", "2 -> 4 -> 3 -> 1", "2 -> 4 -> 1 -> 3"],
        "options_ta": ["2 -> 3 -> 4 -> 1", "4 -> 2 -> 3 -> 1", "2 -> 4 -> 3 -> 1", "2 -> 4 -> 1 -> 3"],
        "answer": "c",
        "explanation_en": "Sequence: 2 (1861 Act) -> 4 (1892 Act) -> 3 (1909 Act) -> 1 (1919 Act).",
        "explanation_ta": "வரிசை: 2 (1861 சட்டம்) -> 4 (1892 சட்டம்) -> 3 (1909 சட்டம்) -> 1 (1919 சட்டம்)."
    },

    # Q4: Analytical - Model 2 - Constitutional Provisions Evolution
    {
        "id": "HB_CHRONO_004",
        "subject": "Polity",
        "topic": "Historical Background of the Indian Constitution",
        "difficulty": "Hard",
        "question_type": "Chronology",
        "question": {
            "en": "Arrange the following administrative and executive milestones in chronological order of their evolution:\n1. Creation of the Office of Secretary of State for India replacing Board of Control and Court of Directors\n2. Addition of a Fourth Member (Law Member) to the Governor-General's Executive Council\n3. Introduction of open competition system for selection of Indian Civil Servants\n4. Formal dual control division into Court of Directors (commercial) and Board of Control (political)",
            "ta": "பின்வரும் நிர்வாக மற்றும் தலைமை அதிகார மைல்கற்களை அவற்றின் வளர்ச்சிக்கு ஏற்ப சரியான காலவரிசையில் அமைக்கவும்:\n1. கட்டுப்பாட்டு வாரியம் மற்றும் இயக்குநர்கள் அவைக்குப் பதிலாக இந்திய அரசுச் செயலர் அலுவலகத்தை உருவாக்குதல்\n2. கவர்னர்-ஜெனரலின் நிர்வாகக் குழுவில் நான்காவது உறுப்பினராக (சட்ட உறுப்பினர்) ஒருவரைச் சேர்த்தல்\n3. இந்திய சிவில் சர்வீஸ் தேர்வுக்கு திறந்தவெளி போட்டித் தேர்வு முறையை அறிமுகப்படுத்துதல்\n4. இயக்குநர்கள் அவை (வணிகம்) மற்றும் கட்டுப்பாட்டு வாரியம் (அரசியல்) என அதிகாரத்தை முறைப்படி இரட்டையாகப் பிரித்தல்"
        },
        "options": [
            {"id": "A", "en": "4 -> 3 -> 2 -> 1", "ta": "4 -> 3 -> 2 -> 1"},
            {"id": "B", "en": "2 -> 4 -> 3 -> 1", "ta": "2 -> 4 -> 3 -> 1"},
            {"id": "C", "en": "4 -> 2 -> 1 -> 3", "ta": "4 -> 2 -> 1 -> 3"},
            {"id": "D", "en": "4 -> 2 -> 3 -> 1", "ta": "4 -> 2 -> 3 -> 1"}
        ],
        "correct_answer": "D",
        "explanation": {
            "en": "Correct Chronological Sequence:\n1. Dual Control (Court of Directors & Board of Control): 1784 (Pitt's India Act 1784).\n2. Law Member added to Executive Council: 1833 (Charter Act 1833 - Lord Macaulay was first Law Member).\n3. Open Competition for Civil Services: 1853 (Charter Act 1853 / Macaulay Committee 1854).\n4. Secretary of State for India created: 1858 (Government of India Act 1858).\n\nConstitutional Significance: This structural evolution displays the gradual professionalization of Indian governance from dual commercial-political supervision to specialized legal council, open civil meritocracy, and direct cabinet-level British control.",
            "ta": "சரியான காலவரிசை:\n1. இரட்டைக் கட்டுப்பாடு (இயக்குநர்கள் அவை & கட்டுப்பாட்டு வாரியம்): 1784 (1784 பிட் இந்தியச் சட்டம்).\n2. சட்ட உறுப்பினர் சேர்க்கை: 1833 (1833 சாசனச் சட்டம் - முதல் சட்ட உறுப்பினர் லார்டு மெக்காலே).\n3. திறந்தவெளி போட்டித் தேர்வு முறை: 1853 (1853 சாசனச் சட்டம் / 1854 மெக்காலே குழு).\n4. இந்திய அரசுச் செயலர் உருவாக்கப்படுதல்: 1858 (1858 இந்திய அரசுச் சட்டம்).\n\nஅரசியலமைப்பு முக்கியத்துவம்: இந்நிறுவன வளர்ச்சி இந்தியாவின் நிர்வாகத் திறனை உயர்த்தி, லண்டனில் அமைச்சரவை அளவிலான கண்காணிப்பை ஏற்படுத்தியதைக் காட்டுகிறது."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Open competition (1853) was introduced after Law Member addition (1833).", "ta": "தவறு. போட்டித் தேர்வு (1853) சட்ட உறுப்பினர் சேர்க்கைக்கு (1833) பின்னரே அறிமுகமானது."},
            "B": {"en": "Incorrect. Dual Control division (1784) came before Charter Act 1833.", "ta": "தவறு. இரட்டைக் கட்டுப்பாடு (1784) 1833 சாசனச் சட்டத்திற்கு முந்தியது."},
            "C": {"en": "Incorrect. Open competition (1853) preceded creation of Secretary of State (1858).", "ta": "தவறு. போட்டித் தேர்வு (1853) அரசுச் செயலர் உருவாக்கத்திற்கு (1858) முந்தியது."},
            "D": {"en": "Correct. 4 (1784) -> 2 (1833) -> 3 (1853) -> 1 (1858) follows exact executive structural changes.", "ta": "சரி. 4 (1784) -> 2 (1833) -> 3 (1853) -> 1 (1858) சரியான நிர்வாக மாற்றங்களை வரிசைப்படுத்துகிறது."}
        },
        "tnpsc_tip": {
            "en": "TNPSC Trap: Lord Macaulay was appointed as the Fourth Member (Law Member) under 1833 Act, but he served only in a advisory/legislative capacity without full executive voting status until later.",
            "ta": "TNPSC பொறி: லார்டு மெக்காலே 1833 சட்டத்தில் நான்காவது சட்ட உறுப்பினராக சேர்க்கப்பட்டார், ஆனால் தொடக்கத்தில் அவருக்கு வாக்களிக்கும் உரிமை வழங்கப்படவில்லை."
        },
        "revision_fact": {
            "en": "The Secretary of State for India was a member of the British Cabinet and was assisted by a 15-member advisory council called the 'Council of India'.",
            "ta": "இந்திய அரசுச் செயலர் பிரிட்டிஷ் அமைச்சரவையின் உறுப்பினராவார்; அவருக்கு உதவ 15 உறுப்பினர்களைக் கொண்ட 'இந்தியக் குழு' அமைந்தது."
        },
        "source_reference": [
            "M. Laxmikanth - Indian Polity",
            "NCERT Class XI/XII - Indian Constitution at Work",
            "Samacheer Kalvi - Standard 11/12 Political Science"
        ],
        "bloom_level": "Analyze",
        "estimated_time_sec": 75,
        "pyq_similarity": "High",
        "tags": ["Polity", "Historical Background", "Chronology", "Administrative Evolution", "Civil Services"],
        "question_en": "Arrange the following administrative and executive milestones in chronological order of their evolution:\n1. Creation of the Office of Secretary of State for India replacing Board of Control and Court of Directors\n2. Addition of a Fourth Member (Law Member) to the Governor-General's Executive Council\n3. Introduction of open competition system for selection of Indian Civil Servants\n4. Formal dual control division into Court of Directors (commercial) and Board of Control (political)",
        "question_ta": "பின்வரும் நிர்வாக மற்றும் தலைமை அதிகார மைல்கற்களை அவற்றின் வளர்ச்சிக்கு ஏற்ப சரியான காலவரிசையில் அமைக்கவும்:\n1. கட்டுப்பாட்டு வாரியம் மற்றும் இயக்குநர்கள் அவைக்குப் பதிலாக இந்திய அரசுச் செயலர் அலுவலகத்தை உருவாக்குதல்\n2. கவர்னர்-ஜெனரலின் நிர்வாகக் குழுவில் நான்காவது உறுப்பினராக (சட்ட உறுப்பினர்) ஒருவரைச் சேர்த்தல்\n3. இந்திய சிவில் சர்வீஸ் தேர்வுக்கு திறந்தவெளி போட்டித் தேர்வு முறையை அறிமுகப்படுத்துதல்\n4. இயக்குநர்கள் அவை (வணிகம்) மற்றும் கட்டுப்பாட்டு வாரியம் (அரசியல்) என அதிகாரத்தை முறைப்படி இரட்டையாகப் பிரித்தல்",
        "options_en": ["4 -> 3 -> 2 -> 1", "2 -> 4 -> 3 -> 1", "4 -> 2 -> 1 -> 3", "4 -> 2 -> 3 -> 1"],
        "options_ta": ["4 -> 3 -> 2 -> 1", "2 -> 4 -> 3 -> 1", "4 -> 2 -> 1 -> 3", "4 -> 2 -> 3 -> 1"],
        "answer": "d",
        "explanation_en": "Sequence: 4 (1784 Pitt's India Act) -> 2 (1833 Charter Act) -> 3 (1853 Charter Act) -> 1 (1858 GOI Act).",
        "explanation_ta": "வரிசை: 4 (1784 பிட் இந்தியச் சட்டம்) -> 2 (1833 சாசனச் சட்டம்) -> 3 (1853 சாசனச் சட்டம்) -> 1 (1858 இந்திய அரசுச் சட்டம்)."
    },

    # Q5: Analytical - Model 2 - Constitutional Provisions Evolution
    {
        "id": "HB_CHRONO_005",
        "subject": "Polity",
        "topic": "Historical Background of the Indian Constitution",
        "difficulty": "Hard",
        "question_type": "Chronology",
        "question": {
            "en": "Arrange the following legislative council financial and structural privileges in order of their constitutional grant:\n1. Grant of Provincial Autonomy and establishment of a tri-partite legislative distribution (Federal, Provincial, Concurrent lists)\n2. Right of legislative members to discuss the budget without power to vote or move resolutions\n3. Establishment of a bicameral legislature at the Centre with Council of State and Legislative Assembly\n4. Right of legislative members to ask supplementary questions and move resolutions on the budget",
            "ta": "சட்ட மேலவைகளின் நிதி மற்றும் கட்டமைப்பு சலுகைகள் வழங்கப்பட்டதன் அடிப்படையில் அவற்றை சரியான காலவரிசையில் அமைக்கவும்:\n1. மாகாண தன்னாட்சி வழங்குதல் மற்றும் மூன்று அடுக்கு சட்டப் பட்டியல்கள் (கூட்டாட்சி, மாகாண, பொதுப் பட்டியல்கள்) உருவாக்குதல்\n2. வாக்களிக்கும் அல்லது தீர்மானம் கொண்டுவரும் அதிகாரமின்றி வரவு செலவுத் திட்டத்தை (பட்ஜெட்) விவாதிக்க உறுப்பினர்களுக்கு உரிமை அளித்தல்\n3. மத்திய சட்டமன்றத்தில் மாநிலங்கள் அவை மற்றும் சட்டப் பேரவை கொண்ட இரு அவை முறையை உருவாக்குதல்\n4. பட்ஜெட் மீது துணைக் கேள்விகள் கேட்கவும் தீர்மானங்கள் கொண்டுவரவும் உறுப்பினர்களுக்கு உரிமை அளித்தல்"
        },
        "options": [
            {"id": "A", "en": "2 -> 4 -> 3 -> 1", "ta": "2 -> 4 -> 3 -> 1"},
            {"id": "B", "en": "4 -> 2 -> 3 -> 1", "ta": "4 -> 2 -> 3 -> 1"},
            {"id": "C", "en": "2 -> 3 -> 4 -> 1", "ta": "2 -> 3 -> 4 -> 1"},
            {"id": "D", "en": "2 -> 4 -> 1 -> 3", "ta": "2 -> 4 -> 1 -> 3"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Correct Chronological Sequence:\n1. Budget discussion without voting: 1892 (Indian Councils Act 1892).\n2. Supplementary questions & budget resolutions: 1909 (Indian Councils Act 1909).\n3. Central Bicameralism: 1919 (Government of India Act 1919).\n4. Provincial Autonomy & 3 Legislative Lists: 1935 (Government of India Act 1935).\n\nConstitutional Significance: Demonstrates how Indian representatives gradually gained financial scrutiny powers, legislative bicameral representation, and eventual provincial legislative autonomy.",
            "ta": "சரியான காலவரிசை:\n1. வாக்களிப்பின்றி பட்ஜெட் விவாதம்: 1892 (இந்தியக் கவுன்சில்கள் சட்டம் 1892).\n2. துணைக் கேள்விகள் & பட்ஜெட் தீர்மானங்கள்: 1909 (இந்தியக் கவுன்சில்கள் சட்டம் 1909).\n3. மத்திய இரு அவை முறை: 1919 (இந்திய அரசுச் சட்டம் 1919).\n4. மாகாண தன்னாட்சி & 3 பட்டியல்கள்: 1935 (இந்திய அரசுச் சட்டம் 1935).\n\nஅரசியலமைப்பு முக்கியத்துவம்: இந்திய பிரதிநிதிகள் எவ்வாறு நிதி தணிக்கை அதிகாரங்கள், இரு அவை அமைப்பு மற்றும் மாகாண தன்னாட்சியைப் பெற்றனர் என்பதை இது விளக்குகிறது."
        },
        "why_not_others": {
            "A": {"en": "Correct. 2 (1892) -> 4 (1909) -> 3 (1919) -> 1 (1935) accurately follows parliamentary rights evolution.", "ta": "சரி. 2 (1892) -> 4 (1909) -> 3 (1919) -> 1 (1935) நாடாளுமன்ற உரிமைகளின் வளர்ச்சியைத் துல்லியமாகப் பின்பற்றுகிறது."},
            "B": {"en": "Incorrect. Discussion of budget (1892) preceded supplementary questions (1909).", "ta": "தவறு. பட்ஜெட் விவாதம் (1892) துணைக் கேள்விகளுக்கு (1909) முந்தியது."},
            "C": {"en": "Incorrect. Bicameralism at center (1919) came AFTER supplementary questions (1909).", "ta": "தவறு. மத்திய இரு அவை முறை (1919) துணைக் கேள்விகளுக்குப் (1909) பின்னரே வந்தது."},
            "D": {"en": "Incorrect. Provincial Autonomy (1935) was enacted AFTER 1919 Act.", "ta": "தவறு. மாகாண தன்னாட்சி (1935) 1919 சட்டத்திற்குப் பின்னரே இயற்றப்பட்டது."}
        },
        "tnpsc_tip": {
            "en": "TNPSC Trap: Supplementary questions were allowed under Morley-Minto Reforms (1909), whereas initial budget discussion was allowed under Indian Councils Act 1892.",
            "ta": "TNPSC பொறி: துணைக் கேள்விகள் மார்லி-மிண்டோ சீர்திருத்தங்கள் (1909) கீழ் அனுமதிக்கப்பட்டன; ஆனால் ஆரம்ப பட்ஜெட் விவாதம் 1892 சட்டத்தின் கீழ் அனுமதிக்கப்பட்டது."
        },
        "revision_fact": {
            "en": "The GOI Act of 1919 separated provincial budgets from the central budget for the very first time.",
            "ta": "1919 ஆம் ஆண்டின் இந்திய அரசுச் சட்டம் முதன்முறையாக மாகாண வரவு செலவுத் திட்டத்தை மத்திய வரவு செலவுத் திட்டத்திலிருந்து பிரித்தது."
        },
        "source_reference": [
            "M. Laxmikanth - Indian Polity",
            "NCERT Class XI/XII - Indian Constitution at Work",
            "Samacheer Kalvi - Standard 11/12 Political Science"
        ],
        "bloom_level": "Analyze",
        "estimated_time_sec": 75,
        "pyq_similarity": "High",
        "tags": ["Polity", "Historical Background", "Chronology", "Budget Rights", "Legislative Powers"],
        "question_en": "Arrange the following legislative council financial and structural privileges in order of their constitutional grant:\n1. Grant of Provincial Autonomy and establishment of a tri-partite legislative distribution (Federal, Provincial, Concurrent lists)\n2. Right of legislative members to discuss the budget without power to vote or move resolutions\n3. Establishment of a bicameral legislature at the Centre with Council of State and Legislative Assembly\n4. Right of legislative members to ask supplementary questions and move resolutions on the budget",
        "question_ta": "சட்ட மேலவைகளின் நிதி மற்றும் கட்டமைப்பு சலுகைகள் வழங்கப்பட்டதன் அடிப்படையில் அவற்றை சரியான காலவரிசையில் அமைக்கவும்:\n1. மாகாண தன்னாட்சி வழங்குதல் மற்றும் மூன்று அடுக்கு சட்டப் பட்டியல்கள் (கூட்டாட்சி, மாகாண, பொதுப் பட்டியல்கள்) உருவாக்குதல்\n2. வாக்களிக்கும் அல்லது தீர்மானம் கொண்டுவரும் அதிகாரமின்றி வரவு செலவுத் திட்டத்தை (பட்ஜெட்) விவாதிக்க உறுப்பினர்களுக்கு உரிமை அளித்தல்\n3. மத்திய சட்டமன்றத்தில் மாநிலங்கள் அவை மற்றும் சட்டப் பேரவை கொண்ட இரு அவை முறையை உருவாக்குதல்\n4. பட்ஜெட் மீது துணைக் கேள்விகள் கேட்கவும் தீர்மானங்கள் கொண்டுவரவும் உறுப்பினர்களுக்கு உரிமை அளித்தல்",
        "options_en": ["2 -> 4 -> 3 -> 1", "4 -> 2 -> 3 -> 1", "2 -> 3 -> 4 -> 1", "2 -> 4 -> 1 -> 3"],
        "options_ta": ["2 -> 4 -> 3 -> 1", "4 -> 2 -> 3 -> 1", "2 -> 3 -> 4 -> 1", "2 -> 4 -> 1 -> 3"],
        "answer": "a",
        "explanation_en": "Sequence: 2 (1892 Act) -> 4 (1909 Act) -> 3 (1919 Act) -> 1 (1935 Act).",
        "explanation_ta": "வரிசை: 2 (1892 சட்டம்) -> 4 (1909 சட்டம்) -> 3 (1919 சட்டம்) -> 1 (1935 சட்டம்)."
    },

    # Q6: Analytical - Model 2 - Constitutional Provisions Evolution
    {
        "id": "HB_CHRONO_006",
        "subject": "Polity",
        "topic": "Historical Background of the Indian Constitution",
        "difficulty": "Hard",
        "question_type": "Chronology",
        "question": {
            "en": "Arrange the establishment of the following judicial bodies in British India and Independent India in correct chronological order:\n1. Inauguration of the Supreme Court of India under the Constitution of India\n2. Establishment of the Federal Court of India at Delhi\n3. Establishment of High Courts at Calcutta, Bombay, and Madras\n4. Establishment of the Supreme Court of Judicature at Fort William, Calcutta",
            "ta": "பிரிட்டிஷ் இந்தியா மற்றும் சுதந்திர இந்தியாவில் பின்வரும் நீதித்துறை அமைப்புகள் நிறுவப்பட்டதை சரியான காலவரிசையில் அமைக்கவும்:\n1. இந்திய அரசியலமைப்பின் கீழ் இந்திய உச்ச நீதிமன்றத்தை முறைப்படி தொடங்குதல்\n2. டெல்லியில் இந்தியாவின் கூட்டாட்சி நீதிமன்றத்தை (Federal Court) அமைத்தல்\n3. கொல்கத்தா, பம்பாய் மற்றும் மதராஸில் உயர் நீதிமன்றங்களை அமைத்தல்\n4. கொல்கத்தா வில்லியம் கோட்டையில் உச்ச நீதிமன்றத்தை அமைத்தல்"
        },
        "options": [
            {"id": "A", "en": "4 -> 2 -> 3 -> 1", "ta": "4 -> 2 -> 3 -> 1"},
            {"id": "B", "en": "4 -> 3 -> 2 -> 1", "ta": "4 -> 3 -> 2 -> 1"},
            {"id": "C", "en": "3 -> 4 -> 2 -> 1", "ta": "3 -> 4 -> 2 -> 1"},
            {"id": "D", "en": "4 -> 3 -> 1 -> 2", "ta": "4 -> 3 -> 1 -> 2"}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "Correct Chronological Sequence:\n1. Supreme Court at Fort William: Established 1774 (under 1773 Act).\n2. High Courts at Calcutta, Bombay, Madras: Established 1862 (under Indian High Courts Act 1861).\n3. Federal Court of India: Established 1937 (under GOI Act 1935).\n4. Supreme Court of India: Inaugurated January 28, 1950 (replacing Federal Court & Privy Council jurisdiction).\n\nConstitutional Significance: Documents the evolution from isolated presidency courts to provincial high courts, a federal appellate court, and finally the unified single integrated judiciary of independent India.",
            "ta": "சரியான காலவரிசை:\n1. வில்லியம் கோட்டை உச்ச நீதிமன்றம்: 1774 (1773 சட்டத்தின் கீழ்).\n2. கொல்கத்தா, பம்பாய், மதராஸ் உயர் நீதிமன்றங்கள்: 1862 (1861 உயர் நீதிமன்றங்கள் சட்டத்தின் கீழ்).\n3. கூட்டாட்சி நீதிமன்றம்: 1937 (1935 இந்திய அரசுச் சட்டத்தின் கீழ்).\n4. இந்திய உச்ச நீதிமன்றம்: ஜனவரி 28, 1950 (கூட்டாட்சி நீதிமன்றம் மற்றும் லண்டன் ப்ரிவி கவுன்சிலுக்குப் பதிலாக).\n\nஅரசியலமைப்பு முக்கியத்துவம்: தனித்தனி மாகாண நீதிமன்றங்களிலிருந்து ஒருங்கிணைந்த இந்திய நீதித்துறை அமைப்பாக மாறியதன் வரலாற்றுப் பாதையை இது காட்டுகிறது."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. High Courts (1862) were established before the Federal Court (1937).", "ta": "தவறு. உயர் நீதிமன்றங்கள் (1862) கூட்டாட்சி நீதிமன்றத்திற்கு (1937) முன்பே அமைக்கப்பட்டன."},
            "B": {"en": "Correct. 4 (1774) -> 3 (1862) -> 2 (1937) -> 1 (1950) accurately mirrors judicial history.", "ta": "சரி. 4 (1774) -> 3 (1862) -> 2 (1937) -> 1 (1950) நீதித்துறை வரலாற்றைத் துல்லியமாகப் பிரதிபலிக்கிறது."},
            "C": {"en": "Incorrect. Fort William Supreme Court (1774) was created long before High Courts (1862).", "ta": "தவறு. வில்லியம் கோட்டை உச்ச நீதிமன்றம் (1774) உயர் நீதிமன்றங்களுக்கு (1862) பல ஆண்டுகளுக்கு முன்பே அமைந்தது."},
            "D": {"en": "Incorrect. Supreme Court of India (1950) was inaugurated after Federal Court (1937).", "ta": "தவறு. இந்திய உச்ச நீதிமன்றம் (1950) கூட்டாட்சி நீதிமன்றத்திற்குப் (1937) பின்னரே தொடங்கப்பட்டது."}
        },
        "tnpsc_tip": {
            "en": "TNPSC Trap: High Courts of Calcutta, Bombay, and Madras were established in 1862 pursuant to the Indian High Courts Act passed in 1861.",
            "ta": "TNPSC பொறி: கொல்கத்தா, பம்பாய் மற்றும் மதராஸ் உயர் நீதிமன்றங்கள் 1861-ல் இயற்றப்பட்ட சட்டத்தின் கீழ் 1862-ல் நிறுவப்பட்டன."
        },
        "revision_fact": {
            "en": "The Supreme Court of India succeeded both the Federal Court of India (1937-1950) and the Judicial Committee of the Privy Council.",
            "ta": "இந்திய உச்ச நீதிமன்றம் இந்தியாவின் கூட்டாட்சி நீதிமன்றம் மற்றும் பிரிட்டிஷ் ப்ரிவி கவுன்சில் ஆகிய இரண்டின் அதிகார வரம்பையும் பெற்றுத் தொடங்கப்பட்டது."
        },
        "source_reference": [
            "M. Laxmikanth - Indian Polity",
            "NCERT Class XI/XII - Indian Constitution at Work",
            "Samacheer Kalvi - Standard 11/12 Political Science"
        ],
        "bloom_level": "Analyze",
        "estimated_time_sec": 75,
        "pyq_similarity": "High",
        "tags": ["Polity", "Historical Background", "Chronology", "Judiciary Evolution", "Federal Court"],
        "question_en": "Arrange the establishment of the following judicial bodies in British India and Independent India in correct chronological order:\n1. Inauguration of the Supreme Court of India under the Constitution of India\n2. Establishment of the Federal Court of India at Delhi\n3. Establishment of High Courts at Calcutta, Bombay, and Madras\n4. Establishment of the Supreme Court of Judicature at Fort William, Calcutta",
        "question_ta": "பிரிட்டிஷ் இந்தியா மற்றும் சுதந்திர இந்தியாவில் பின்வரும் நீதித்துறை அமைப்புகள் நிறுவப்பட்டதை சரியான காலவரிசையில் அமைக்கவும்:\n1. இந்திய அரசியலமைப்பின் கீழ் இந்திய உச்ச நீதிமன்றத்தை முறைப்படி தொடங்குதல்\n2. டெல்லியில் இந்தியாவின் கூட்டாட்சி நீதிமன்றத்தை (Federal Court) அமைத்தல்\n3. கொல்கத்தா, பம்பாய் மற்றும் மதராஸில் உயர் நீதிமன்றங்களை அமைத்தல்\n4. கொல்கத்தா வில்லியம் கோட்டையில் உச்ச நீதிமன்றத்தை அமைத்தல்",
        "options_en": ["4 -> 2 -> 3 -> 1", "4 -> 3 -> 2 -> 1", "3 -> 4 -> 2 -> 1", "4 -> 3 -> 1 -> 2"],
        "options_ta": ["4 -> 2 -> 3 -> 1", "4 -> 3 -> 2 -> 1", "3 -> 4 -> 2 -> 1", "4 -> 3 -> 1 -> 2"],
        "answer": "b",
        "explanation_en": "Sequence: 4 (1774 Supreme Court) -> 3 (1862 High Courts) -> 2 (1937 Federal Court) -> 1 (1950 Supreme Court of India).",
        "explanation_ta": "வரிசை: 4 (1774 உச்ச நீதிமன்றம்) -> 3 (1862 உயர் நீதிமன்றங்கள்) -> 2 (1937 கூட்டாட்சி நீதிமன்றம்) -> 1 (1950 இந்திய உச்ச நீதிமன்றம்)."
    },

    # Q7: Analytical - Model 3 - Administrative Reforms Progression
    {
        "id": "HB_CHRONO_007",
        "subject": "Polity",
        "topic": "Historical Background of the Indian Constitution",
        "difficulty": "Hard",
        "question_type": "Chronology",
        "question": {
            "en": "Arrange the following Civil Services Commissions and Reform Committees in British India in correct chronological sequence:\n1. Royal Commission on Superior Civil Services in India (Lee Commission)\n2. Committee on the Indian Civil Service (Macaulay Committee)\n3. Royal Commission on Public Services in India (Islington Commission)\n4. Public Service Commission under Sir Charles Aitchison (Aitchison Commission)",
            "ta": "பிரிட்டிஷ் இந்தியாவில் சிவில் சர்வீசஸ் கமிஷன்கள் மற்றும் சீர்திருத்தக் குழுக்கள் அமைக்கப்பட்டதை சரியான காலவரிசையில் அமைக்கவும்:\n1. இந்தியாவில் மேலதிக சிவில் சர்வீசஸ்க்கான அரச ஆணையம் (லீ ஆணையம்)\n2. இந்திய சிவில் சர்வீஸ் குழு (மெக்காலே குழு)\n3. இந்தியாவில் பொதுச் சேவைகளுக்கான அரச ஆணையம் (இஸ்லிங்டன் ஆணையம்)\n4. சர் சார்லஸ் அட்சிகன் தலைமையிலான பொதுச் சேவை ஆணையம் (அட்சிகன் ஆணையம்)"
        },
        "options": [
            {"id": "A", "en": "2 -> 1 -> 4 -> 3", "ta": "2 -> 1 -> 4 -> 3"},
            {"id": "B", "en": "4 -> 2 -> 3 -> 1", "ta": "4 -> 2 -> 3 -> 1"},
            {"id": "C", "en": "2 -> 4 -> 3 -> 1", "ta": "2 -> 4 -> 3 -> 1"},
            {"id": "D", "en": "2 -> 4 -> 1 -> 3", "ta": "2 -> 4 -> 1 -> 3"}
        ],
        "correct_answer": "C",
        "explanation": {
            "en": "Correct Chronological Sequence:\n1. Macaulay Committee: Appointed 1854 (pursuant to Charter Act 1853).\n2. Aitchison Commission: Appointed 1886 (classified services into Imperial, Provincial, Subordinate).\n3. Islington Commission: Appointed 1912 (submitted report 1915, recommended 25% entries in India).\n4. Lee Commission: Appointed 1923 (recommended establishment of Federal Public Service Commission).\n\nConstitutional Significance: Traces the reform trajectory of Indian bureaucratic recruitment from British monopoly to merit-based competition, service categorization, Indianization, and independent PSC establishment.",
            "ta": "சரியான காலவரிசை:\n1. மெக்காலே குழு: 1854-ல் நியமிக்கப்பட்டது (1853 சாசனச் சட்டத்தின் கீழ்).\n2. அட்சிகன் ஆணையம்: 1886-ல் நியமிக்கப்பட்டது (இம்பீரியல், மாகாண, கீழ்நிலை சேவைகள் எனப் பிரித்தது).\n3. இஸ்லிங்டன் ஆணையம்: 1912-ல் நியமிக்கப்பட்டது (இந்தியாவில் 25% நியமனங்களை பரிந்துரைத்தது).\n4. லீ ஆணையம்: 1923-ல் நியமிக்கப்பட்டது (பொதுச் சேவை ஆணையம் அமைக்கப் பரிந்துரைத்தது).\n\nஅரசியலமைப்பு முக்கியத்துவம்: இந்திய சிவில் சர்வீஸ் தேர்வில் திறந்தவெளி போட்டி, இந்தியமயமாக்கல் மற்றும் தன்னாட்சி பெற்ற தேர்வாணையம் அமைத்தலின் வளர்ச்சியை இது காட்டுகிறது."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Lee Commission (1923) was appointed long after Aitchison Commission (1886).", "ta": "தவறு. லீ ஆணையம் (1923) அட்சிகன் ஆணையத்திற்குப் (1886) பின்னரே நியமிக்கப்பட்டது."},
            "B": {"en": "Incorrect. Macaulay Committee (1854) was the earliest among civil service committees.", "ta": "தவறு. சிவில் சர்வீஸ் குழுக்களில் மெக்காலே குழுவே (1854) மிகவும் பழமையானது."},
            "C": {"en": "Correct. 2 (1854) -> 4 (1886) -> 3 (1912) -> 1 (1923) accurately follows Civil Service Commission history.", "ta": "சரி. 2 (1854) -> 4 (1886) -> 3 (1912) -> 1 (1923) சிவில் சர்வீஸ் ஆணையங்களின் வரலாற்றைத் துல்லியமாகப் பின்பற்றுகிறது."},
            "D": {"en": "Incorrect. Islington Commission (1912) preceded Lee Commission (1923).", "ta": "தவறு. இஸ்லிங்டன் ஆணையம் (1912) லீ ஆணையத்திற்கு (1923) முந்தியது."}
        },
        "tnpsc_tip": {
            "en": "TNPSC Trap: Aitchison Commission (1886) dropped the terms 'covenanted' and 'uncovenanted' and divided civil services into Imperial, Provincial, and Subordinate Civil Services.",
            "ta": "TNPSC பொறி: அட்சிகன் ஆணையம் (1886) 'ஒப்பந்தம் செய்யப்பட்ட' மற்றும் 'ஒப்பந்தம் செய்யப்படாத' என்ற வார்த்தைகளை நீக்கி இம்பீரியல், மாகாண மற்றும் கீழ்நிலை சேவைகள் எனப் பிரித்தது."
        },
        "revision_fact": {
            "en": "Based on the recommendations of the Lee Commission (1923), the Central Public Service Commission was set up in 1926.",
            "ta": "லீ ஆணையத்தின் (1923) பரிந்துரைகளின் அடிப்படையில், 1926 ஆம் ஆண்டில் மத்திய பொதுச் சேவை ஆணையம் அமைக்கப்பட்டது."
        },
        "source_reference": [
            "M. Laxmikanth - Indian Polity",
            "NCERT Class XI/XII - Indian Constitution at Work",
            "Samacheer Kalvi - Standard 11/12 Political Science"
        ],
        "bloom_level": "Analyze",
        "estimated_time_sec": 75,
        "pyq_similarity": "High",
        "tags": ["Polity", "Historical Background", "Chronology", "Civil Services Commissions", "Lee Commission"],
        "question_en": "Arrange the following Civil Services Commissions and Reform Committees in British India in correct chronological sequence:\n1. Royal Commission on Superior Civil Services in India (Lee Commission)\n2. Committee on the Indian Civil Service (Macaulay Committee)\n3. Royal Commission on Public Services in India (Islington Commission)\n4. Public Service Commission under Sir Charles Aitchison (Aitchison Commission)",
        "question_ta": "பிரிட்டிஷ் இந்தியாவில் சிவில் சர்வீசஸ் கமிஷன்கள் மற்றும் சீர்திருத்தக் குழுக்கள் அமைக்கப்பட்டதை சரியான காலவரிசையில் அமைக்கவும்:\n1. இந்தியாவில் மேலதிக சிவில் சர்வீசஸ்க்கான அரச ஆணையம் (லீ ஆணையம்)\n2. இந்திய சிவில் சர்வீஸ் குழு (மெக்காலே குழு)\n3. இந்தியாவில் பொதுச் சேவைகளுக்கான அரச ஆணையம் (இஸ்லிங்டன் ஆணையம்)\n4. சர் சார்லஸ் அட்சிகன் தலைமையிலான பொதுச் சேவை ஆணையம் (அட்சிகன் ஆணையம்)",
        "options_en": ["2 -> 1 -> 4 -> 3", "4 -> 2 -> 3 -> 1", "2 -> 4 -> 3 -> 1", "2 -> 4 -> 1 -> 3"],
        "options_ta": ["2 -> 1 -> 4 -> 3", "4 -> 2 -> 3 -> 1", "2 -> 4 -> 3 -> 1", "2 -> 4 -> 1 -> 3"],
        "answer": "c",
        "explanation_en": "Sequence: 2 (1854 Macaulay) -> 4 (1886 Aitchison) -> 3 (1912 Islington) -> 1 (1923 Lee).",
        "explanation_ta": "வரிசை: 2 (1854 மெக்காலே) -> 4 (1886 அட்சிகன்) -> 3 (1912 இஸ்லிங்டன்) -> 1 (1923 லீ)."
    },

    # Q8: Analytical - Model 3 - Administrative Reforms Progression
    {
        "id": "HB_CHRONO_008",
        "subject": "Polity",
        "topic": "Historical Background of the Indian Constitution",
        "difficulty": "Hard",
        "question_type": "Chronology",
        "question": {
            "en": "Arrange the following administrative decentralization and local self-government milestones in chronological order:\n1. Transfer of Local Self-Government to the administrative control of elected Indian Ministers (Transferred Subject)\n2. Lord Ripon's Resolution on Local Self-Government (Magna Carta of Local Self-Government)\n3. Appointment of the Royal Commission on Decentralization (Hobhouse Commission)\n4. Lord Mayo's Resolution on Financial Decentralization granting fixed grants to provinces",
            "ta": "பின்வரும் நிர்வாகப் பரவலாக்கம் மற்றும் உள்ளாட்சி சுயஅரசு மைல்கற்களை காலவரிசையில் அமைக்கவும்:\n1. உள்ளாட்சி சுயஅரசை தேர்ந்தெடுக்கப்பட்ட இந்திய அமைச்சர்களின் நிர்வாகக் கட்டுப்பாட்டிற்கு மாற்றுதல் (மாற்றப்பட்ட துறை)\n2. லார்டு ரிப்பனின் உள்ளாட்சி சுயஅரசு தீர்மானம் (உள்ளாட்சி சுயஅரசின் மகாசாசனம்)\n3. பரவலாக்கத்திற்கான அரச ஆணையம் அமைத்தல் (ஹாப்ஹவுஸ் ஆணையம்)\n4. மாகாணங்களுக்கு நிலையான மானியங்களை வழங்கி நிதிப் பரவலாக்கம் செய்த லார்டு மேயோவின் தீர்மானம்"
        },
        "options": [
            {"id": "A", "en": "4 -> 3 -> 2 -> 1", "ta": "4 -> 3 -> 2 -> 1"},
            {"id": "B", "en": "2 -> 4 -> 3 -> 1", "ta": "2 -> 4 -> 3 -> 1"},
            {"id": "C", "en": "4 -> 2 -> 1 -> 3", "ta": "4 -> 2 -> 1 -> 3"},
            {"id": "D", "en": "4 -> 2 -> 3 -> 1", "ta": "4 -> 2 -> 3 -> 1"}
        ],
        "correct_answer": "D",
        "explanation": {
            "en": "Correct Chronological Sequence:\n1. Lord Mayo's Financial Decentralization Resolution: 1870.\n2. Lord Ripon's Local Self-Government Resolution: 1882.\n3. Royal Commission on Decentralization (Hobhouse): Appointed 1907 (submitted report 1909).\n4. Transfer of Local Self-Govt to Indian Ministers: 1919 (under Dyarchy of GOI Act 1919).\n\nConstitutional Significance: Marks the step-by-step devolution of administrative authority from imperial financial delegation to grassroots municipal self-governance and responsible ministerial control.",
            "ta": "சரியான காலவரிசை:\n1. லார்டு மேயோவின் நிதிப் பரவலாக்கத் தீர்மானம்: 1870.\n2. லார்டு ரிப்பனின் உள்ளாட்சி சுயஅரசுத் தீர்மானம்: 1882.\n3. பரவலாக்கத்திற்கான அரச ஆணையம் (ஹாப்ஹவுஸ்): 1907-ல் நியமிக்கப்பட்டது.\n4. உள்ளாட்சி அமைப்புகளை இந்திய அமைச்சர்களிடம் ஒப்படைத்தல்: 1919 (1919 இந்திய அரசுச் சட்டத்தின் கீழ்).\n\nஅரசியலமைப்பு முக்கியத்துவம்: பேரரசு நிதியொதுக்கீட்டிலிருந்து அடிமட்ட உள்ளாட்சி நிர்வாகம் மற்றும் இந்திய அமைச்சர்களின் பொறுப்புக்கு அதிகாரம் மாற்றப்பட்டதன் வரலாற்றை இது காட்டுகிறது."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Ripon's Resolution (1882) came before Hobhouse Commission (1907).", "ta": "தவறு. ரிப்பனின் தீர்மானம் (1882) ஹாப்ஹவுஸ் ஆணையத்திற்கு (1907) முந்தியது."},
            "B": {"en": "Incorrect. Mayo's Resolution (1870) came before Ripon's Resolution (1882).", "ta": "தவறு. மேயோவின் தீர்மானம் (1870) ரிப்பனின் தீர்மானத்திற்கு (1882) முந்தியது."},
            "C": {"en": "Incorrect. Hobhouse Commission (1907) was appointed before GOI Act 1919.", "ta": "தவறு. ஹாப்ஹவுஸ் ஆணையம் (1907) 1919 சட்டத்திற்கு முன்பே நியமிக்கப்பட்டது."},
            "D": {"en": "Correct. 4 (1870) -> 2 (1882) -> 3 (1907) -> 1 (1919) accurately traces local governance history.", "ta": "சரி. 4 (1870) -> 2 (1882) -> 3 (1907) -> 1 (1919) உள்ளாட்சி வரலாற்றைத் துல்லியமாகப் பின்பற்றுகிறது."}
        },
        "tnpsc_tip": {
            "en": "TNPSC Trap: Lord Ripon is known as the 'Father of Local Self-Government in India', whereas Lord Mayo introduced the concept of financial decentralization.",
            "ta": "TNPSC பொறி: லார்டு ரிப்பன் 'இந்திய உள்ளாட்சி அமைப்புகளின் தந்தை' என அழைக்கப்படுகிறார்; ஆனால் லார்டு மேயோ நிதிப் பரவலாக்கக் கருத்தை அறிமுகப்படுத்தினார்."
        },
        "revision_fact": {
            "en": "Under GOI Act 1919, Local Self-Government was made a 'Transferred Subject' administered by the Governor with the advice of elected Indian Ministers.",
            "ta": "1919 இந்திய அரசுச் சட்டத்தின் கீழ், உள்ளாட்சி சுயஅரசு தேர்ந்தெடுக்கப்பட்ட இந்திய அமைச்சர்களின் ஆலோசனையுடன் கவர்னரால் நிர்வகிக்கப்படும் 'மாற்றப்பட்ட துறையாக' ஆக்கப்பட்டது."
        },
        "source_reference": [
            "M. Laxmikanth - Indian Polity",
            "NCERT Class XI/XII - Indian Constitution at Work",
            "Samacheer Kalvi - Standard 11/12 Political Science"
        ],
        "bloom_level": "Analyze",
        "estimated_time_sec": 75,
        "pyq_similarity": "High",
        "tags": ["Polity", "Historical Background", "Chronology", "Local Self Government", "Decentralization"],
        "question_en": "Arrange the following administrative decentralization and local self-government milestones in chronological order:\n1. Transfer of Local Self-Government to the administrative control of elected Indian Ministers (Transferred Subject)\n2. Lord Ripon's Resolution on Local Self-Government (Magna Carta of Local Self-Government)\n3. Appointment of the Royal Commission on Decentralization (Hobhouse Commission)\n4. Lord Mayo's Resolution on Financial Decentralization granting fixed grants to provinces",
        "question_ta": "பின்வரும் நிர்வாகப் பரவலாக்கம் மற்றும் உள்ளாட்சி சுயஅரசு மைல்கற்களை காலவரிசையில் அமைக்கவும்:\n1. உள்ளாட்சி சுயஅரசை தேர்ந்தெடுக்கப்பட்ட இந்திய அமைச்சர்களின் நிர்வாகக் கட்டுப்பாட்டிற்கு மாற்றுதல் (மாற்றப்பட்ட துறை)\n2. லார்டு ரிப்பனின் உள்ளாட்சி சுயஅரசு தீர்மானம் (உள்ளாட்சி சுயஅரசின் மகாசாசனம்)\n3. பரவலாக்கத்திற்கான அரச ஆணையம் அமைத்தல் (ஹாப்ஹவுஸ் ஆணையம்)\n4. மாகாணங்களுக்கு நிலையான மானியங்களை வழங்கி நிதிப் பரவலாக்கம் செய்த லார்டு மேயோவின் தீர்மானம்",
        "options_en": ["4 -> 3 -> 2 -> 1", "2 -> 4 -> 3 -> 1", "4 -> 2 -> 1 -> 3", "4 -> 2 -> 3 -> 1"],
        "options_ta": ["4 -> 3 -> 2 -> 1", "2 -> 4 -> 3 -> 1", "4 -> 2 -> 1 -> 3", "4 -> 2 -> 3 -> 1"],
        "answer": "d",
        "explanation_en": "Sequence: 4 (1870 Mayo Resolution) -> 2 (1882 Ripon Resolution) -> 3 (1907 Hobhouse Commission) -> 1 (1919 Dyarchy Transfer).",
        "explanation_ta": "வரிசை: 4 (1870 மேயோ தீர்மானம்) -> 2 (1882 ரிப்பன் தீர்மானம்) -> 3 (1907 ஹாப்ஹவுஸ் ஆணையம்) -> 1 (1919 இரட்டை ஆட்சி மாற்றம்)."
    },

    # Q9: Analytical - Model 3 - Administrative Reforms Progression
    {
        "id": "HB_CHRONO_009",
        "subject": "Polity",
        "topic": "Historical Background of the Indian Constitution",
        "difficulty": "Hard",
        "question_type": "Chronology",
        "question": {
            "en": "Arrange the following phases of legislative centralization and decentralization in India in correct chronological sequence:\n1. Total centralized legislative authority vested in Governor-General of India, depriving Bombay and Madras of legislative powers\n2. Reversal of centralization policy by restoring legislative powers to Bombay and Madras Presidencies\n3. Initial subordination of Bombay and Madras Presidencies to Governor-General of Bengal in matters of war and peace\n4. Complete grant of Provincial Autonomy with full executive responsibility to provincial ministers",
            "ta": "இந்தியாவில் சட்டமியற்றும் அதிகார மையமாக்கல் மற்றும் அதிகாரப் பரவலாக்கத்தின் பின்வரும் கட்டங்களை சரியான காலவரிசையில் அமைக்கவும்:\n1. பம்பாய் மற்றும் மதராஸின் சட்ட அதிகாரங்களைப் பறித்து, இந்தியாவின் கவர்னர்-ஜெனரலிடம் சட்ட அதிகாரத்தை முழுமையாக மையப்படுத்துதல்\n2. பம்பாய் மற்றும் மதராஸ் மாகாணங்களுக்கு சட்ட அதிகாரங்களை மீட்டளித்து அதிகார மையமாக்கலைத் திரும்பப் பெறுதல்\n3. போர் மற்றும் அமைதி விவகாரங்களில் பம்பாய் மற்றும் மதராஸ் மாகாணங்களை வங்காள கவர்னர்-ஜெனரலுக்குத் தொடக்கத்தில் கீழ்ப்படுத்துதல்\n4. மாகாண அமைச்சர்களுக்கு முழு நிர்வாகப் பொறுப்புடன் கூடிய முழுமையான மாகாண தன்னாட்சி வழங்குதல்"
        },
        "options": [
            {"id": "A", "en": "3 -> 1 -> 2 -> 4", "ta": "3 -> 1 -> 2 -> 4"},
            {"id": "B", "en": "1 -> 3 -> 2 -> 4", "ta": "1 -> 3 -> 2 -> 4"},
            {"id": "C", "en": "3 -> 2 -> 1 -> 4", "ta": "3 -> 2 -> 1 -> 4"},
            {"id": "D", "en": "3 -> 1 -> 4 -> 2", "ta": "3 -> 1 -> 4 -> 2"}
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Correct Chronological Sequence:\n1. Initial subordination of Presidencies: 1773 (Regulating Act 1773).\n2. Total centralization of legislative power: 1833 (Charter Act 1833).\n3. Commencement of legislative decentralization: 1861 (Indian Councils Act 1861).\n4. Complete Provincial Autonomy: 1935 (Government of India Act 1935).\n\nConstitutional Significance: Illustrates the complete U-turn in British constitutional policy—from centralization under EIC (1773-1833) to systematic legislative decentralization under Crown Rule, culminating in 1935 Provincial Autonomy.",
            "ta": "சரியான காலவரிசை:\n1. மாகாணங்களை கீழ்நிலையாக்கல்: 1773 (1773 ஒழுங்குமுறைச் சட்டம்).\n2. சட்ட அதிகார முழுமையாக்க மையமாக்கல்: 1833 (1833 சாசனச் சட்டம்).\n3. சட்ட அதிகாரப் பரவலாக்கத் தொடக்கம்: 1861 (1861 இந்தியக் கவுன்சில்கள் சட்டம்).\n4. முழுமையான மாகாண தன்னாட்சி: 1935 (1935 இந்திய அரசுச் சட்டம்).\n\nஅரசியலமைப்பு முக்கியத்துவம்: பிரிட்டிஷ் ஆட்சியின் சட்டக் கொள்கை மையமாக்கலிலிருந்து (1773-1833) அதிகாரப் பரவலாக்கத்திற்கு (1861-1935) எவ்வாறு மாறியது என்பதை இக்காலவரிசை காட்டுகிறது."
        },
        "why_not_others": {
            "A": {"en": "Correct. 3 (1773) -> 1 (1833) -> 2 (1861) -> 4 (1935) accurately tracks the pendulum shift between centralization and decentralization.", "ta": "சரி. 3 (1773) -> 1 (1833) -> 2 (1861) -> 4 (1935) மையமாக்கல் மற்றும் பரவலாக்க நிலைகளைத் துல்லியமாகக் காட்டுகிறது."},
            "B": {"en": "Incorrect. Subordination of presidencies (1773) occurred before total legislative centralization (1833).", "ta": "தவறு. மாகாணங்கள் கீழ்ப்படுத்தப்படுதல் (1773) முழு சட்ட மையமாக்கலுக்கு (1833) முந்தியது."},
            "C": {"en": "Incorrect. Legislative powers were restored in 1861 (2), long after Charter Act 1833 (1).", "ta": "தவறு. சட்ட அதிகாரங்கள் 1861-ல் மீட்டளிக்கப்பட்டன (2), இது 1833 சாசனச் சட்டத்திற்குப் (1) பின்னராகும்."},
            "D": {"en": "Incorrect. Restoration of legislative powers (1861) preceded 1935 Provincial Autonomy.", "ta": "தவறு. சட்ட அதிகார மீட்பு (1861) 1935 மாகாண தன்னாட்சிக்கு முந்தியது."}
        },
        "tnpsc_tip": {
            "en": "TNPSC Trap: Charter Act of 1833 was the 'climax of legislative centralization', whereas Indian Councils Act of 1861 was the 'turning point toward decentralization'.",
            "ta": "TNPSC பொறி: 1833 சாசனச் சட்டம் 'சட்ட அதிகார மையமாக்கலின் உச்சம்'; 1861 இந்தியக் கவுன்சில்கள் சட்டம் 'அதிகாரப் பரவலாக்கத்தின் திருப்புமுனை'."
        },
        "revision_fact": {
            "en": "The process of legislative devolution initiated in 1861 culminated in complete provincial autonomy under the Government of India Act of 1935.",
            "ta": "1861-ல் தொடங்கப்பட்ட சட்ட அதிகாரப் பரவலாக்க நடவடிக்கை 1935 இந்திய அரசுச் சட்டத்தின் கீழ் முழு மாகாண தன்னாட்சியாக நிறைவடைந்தது."
        },
        "source_reference": [
            "M. Laxmikanth - Indian Polity",
            "NCERT Class XI/XII - Indian Constitution at Work",
            "Samacheer Kalvi - Standard 11/12 Political Science"
        ],
        "bloom_level": "Analyze",
        "estimated_time_sec": 75,
        "pyq_similarity": "High",
        "tags": ["Polity", "Historical Background", "Chronology", "Centralization", "Provincial Autonomy"],
        "question_en": "Arrange the following phases of legislative centralization and decentralization in India in correct chronological sequence:\n1. Total centralized legislative authority vested in Governor-General of India, depriving Bombay and Madras of legislative powers\n2. Reversal of centralization policy by restoring legislative powers to Bombay and Madras Presidencies\n3. Initial subordination of Bombay and Madras Presidencies to Governor-General of Bengal in matters of war and peace\n4. Complete grant of Provincial Autonomy with full executive responsibility to provincial ministers",
        "question_ta": "இந்தியாவில் சட்டமியற்றும் அதிகார மையமாக்கல் மற்றும் அதிகாரப் பரவலாக்கத்தின் பின்வரும் கட்டங்களை சரியான காலவரிசையில் அமைக்கவும்:\n1. பம்பாய் மற்றும் மதராஸின் சட்ட அதிகாரங்களைப் பறித்து, இந்தியாவின் கவர்னர்-ஜெனரலிடம் சட்ட அதிகாரத்தை முழுமையாக மையப்படுத்துதல்\n2. பம்பாய் மற்றும் மதராஸ் மாகாணங்களுக்கு சட்ட அதிகாரங்களை மீட்டளித்து அதிகார மையமாக்கலைத் திரும்பப் பெறுதல்\n3. போர் மற்றும் அமைதி விவகாரங்களில் பம்பாய் மற்றும் மதராஸ் மாகாணங்களை வங்காள கவர்னர்-ஜெனரலுக்குத் தொடக்கத்தில் கீழ்ப்படுத்துதல்\n4. மாகாண அமைச்சர்களுக்கு முழு நிர்வாகப் பொறுப்புடன் கூடிய முழுமையான மாகாண தன்னாட்சி வழங்குதல்",
        "options_en": ["3 -> 1 -> 2 -> 4", "1 -> 3 -> 2 -> 4", "3 -> 2 -> 1 -> 4", "3 -> 1 -> 4 -> 2"],
        "options_ta": ["3 -> 1 -> 2 -> 4", "1 -> 3 -> 2 -> 4", "3 -> 2 -> 1 -> 4", "3 -> 1 -> 4 -> 2"],
        "answer": "a",
        "explanation_en": "Sequence: 3 (1773 Act) -> 1 (1833 Act) -> 2 (1861 Act) -> 4 (1935 Act).",
        "explanation_ta": "வரிசை: 3 (1773 சட்டம்) -> 1 (1833 சட்டம்) -> 2 (1861 சட்டம்) -> 4 (1935 சட்டம்)."
    },

    # Q10: Analytical - Model 4 - Committees -> Recommendations -> Acts
    {
        "id": "HB_CHRONO_010",
        "subject": "Polity",
        "topic": "Historical Background of the Indian Constitution",
        "difficulty": "Hard",
        "question_type": "Chronology",
        "question": {
            "en": "Arrange the following major political events and committee recommendations leading to the Government of India Act 1935 in correct chronological order:\n1. Publication of the Nehru Report proposing a Dominion Status Constitution for India\n2. Submission of the Simon Commission Report recommending abolition of Dyarchy\n3. Publication of the British Government's 'White Paper on Constitutional Reforms'\n4. Convening of the First Round Table Conference in London",
            "ta": "1935 இந்திய அரசுச் சட்டத்திற்கு வழிகோலிய பின்வரும் முக்கிய அரசியல் நிகழ்வுகள் மற்றும் குழு பரிந்துரைகளை சரியான காலவரிசையில் அமைக்கவும்:\n1. இந்தியாவுக்கு டொமினியன் அந்தஸ்து அரசியலமைப்பை முன்மொழிந்த நேரு அறிக்கை வெளியிடப்படல்\n2. இரட்டை ஆட்சியை நீக்கப் பரிந்துரைத்து சைமன் குழு அறிக்கை சமர்ப்பிக்கப்படல்\n3. பிரிட்டிஷ் அரசாங்கத்தின் 'அரசியலமைப்பு சீர்திருத்தங்கள் பற்றிய வெள்ளை அறிக்கை' வெளியிடப்படல்\n4. லண்டனில் முதலாவது வட்டமேஜை மாநாடு கூட்டப்படல்"
        },
        "options": [
            {"id": "A", "en": "1 -> 4 -> 2 -> 3", "ta": "1 -> 4 -> 2 -> 3"},
            {"id": "B", "en": "1 -> 2 -> 4 -> 3", "ta": "1 -> 2 -> 4 -> 3"},
            {"id": "C", "en": "2 -> 1 -> 4 -> 3", "ta": "2 -> 1 -> 4 -> 3"},
            {"id": "D", "en": "1 -> 2 -> 3 -> 4", "ta": "1 -> 2 -> 3 -> 4"}
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "Correct Chronological Sequence:\n1. Nehru Report published: August 1928.\n2. Simon Commission Report submitted: May 1930.\n3. First Round Table Conference convened: November 1930.\n4. White Paper on Constitutional Reforms published: March 1933.\n\nConstitutional Significance: This sequence tracks the intense negotiating process between Indian leadership, imperial commissions, and round table dialogues that directly formed the blueprint for the 1935 Act.",
            "ta": "சரியான காலவரிசை:\n1. நேரு அறிக்கை வெளியீடு: ஆகஸ்ட் 1928.\n2. சைமன் குழு அறிக்கை சமர்ப்பிப்பு: மே 1930.\n3. முதலாவது வட்டமேஜை மாநாடு: நவம்பர் 1930.\n4. அரசியலமைப்பு சீர்திருத்த வெள்ளை அறிக்கை: மார்ச் 1933.\n\nஅரசியலமைப்பு முக்கியத்துவம்: இந்தியத் தலைவர்கள் மற்றும் பிரிட்டிஷ் அரசு இடையிலான பேச்சுவார்த்தைகள் 1935 இந்திய அரசுச் சட்டத்தின் வரைபடத்தை உருவாக்கியதை இது காட்டுகிறது."
        },
        "why_not_others": {
            "A": {"en": "Incorrect. Simon Commission Report (May 1930) was submitted BEFORE First Round Table Conference (Nov 1930).", "ta": "தவறு. சைமன் குழு அறிக்கை (மே 1930) முதலாவது வட்டமேஜை மாநாட்டிற்கு (நவம்பர் 1930) முன்பே சமர்ப்பிக்கப்பட்டது."},
            "B": {"en": "Correct. 1 (Aug 1928) -> 2 (May 1930) -> 4 (Nov 1930) -> 3 (March 1933) matches the exact historical calendar.", "ta": "சரி. 1 (ஆகஸ்ட் 1928) -> 2 (மே 1930) -> 4 (நவம்பர் 1930) -> 3 (மார்ச் 1933) வரலாற்று காலவரிசையைப் துல்லியமாகப் பின்பற்றுகிறது."},
            "C": {"en": "Incorrect. Nehru Report (1928) was drafted before Simon Commission submitted its report (1930).", "ta": "தவறு. நேரு அறிக்கை (1928) சைமன் குழு அறிக்கை சமர்ப்பிக்கப்படுவதற்கு (1930) முன்பே தயாரிக்கப்பட்டது."},
            "D": {"en": "Incorrect. White Paper (1933) was published AFTER the Round Table Conferences concluded.", "ta": "தவறு. வெள்ளை அறிக்கை (1933) வட்டமேஜை மாநாடுகள் முடிந்த பிறகே வெளியிடப்பட்டது."}
        },
        "tnpsc_tip": {
            "en": "TNPSC Trap: Nehru Report was drafted in 1928 as an all-parties counter-challenge to Lord Birkenhead's assertion that Indians could not draft a unified constitution.",
            "ta": "TNPSC பொறி: இந்தியர்களால் ஒருமனதான அரசியலமைப்பை உருவாக்க முடியாது என்ற லார்டு பர்க்கன்ஹெட்டின் சவாலுக்குப் பதிலாக 1928-ல் நேரு அறிக்கை தயாரிக்கப்பட்டது."
        },
        "revision_fact": {
            "en": "The White Paper on Constitutional Reforms published in 1933 was scrutinized by a Joint Select Committee of the British Parliament, which prepared the bill for GOI Act 1935.",
            "ta": "1933-ல் வெளியிடப்பட்ட வெள்ளை அறிக்கை பிரிட்டிஷ் நாடாளுமன்றக் கூட்டுத் தேர்வுக் குழுவால் பரிசீலிக்கப்பட்டு 1935 இந்திய அரசுச் சட்ட மசோதாவாக மாறியது."
        },
        "source_reference": [
            "M. Laxmikanth - Indian Polity",
            "NCERT Class XI/XII - Indian Constitution at Work",
            "Samacheer Kalvi - Standard 11/12 Political Science"
        ],
        "bloom_level": "Analyze",
        "estimated_time_sec": 75,
        "pyq_similarity": "High",
        "tags": ["Polity", "Historical Background", "Chronology", "Nehru Report", "Simon Commission"],
        "question_en": "Arrange the following major political events and committee recommendations leading to the Government of India Act 1935 in correct chronological order:\n1. Publication of the Nehru Report proposing a Dominion Status Constitution for India\n2. Submission of the Simon Commission Report recommending abolition of Dyarchy\n3. Publication of the British Government's 'White Paper on Constitutional Reforms'\n4. Convening of the First Round Table Conference in London",
        "question_ta": "1935 இந்திய அரசுச் சட்டத்திற்கு வழிகோலிய பின்வரும் முக்கிய அரசியல் நிகழ்வுகள் மற்றும் குழு பரிந்துரைகளை சரியான காலவரிசையில் அமைக்கவும்:\n1. இந்தியாவுக்கு டொமினியன் அந்தஸ்து அரசியலமைப்பை முன்மொழிந்த நேரு அறிக்கை வெளியிடப்படல்\n2. இரட்டை ஆட்சியை நீக்கப் பரிந்துரைத்து சைமன் குழு அறிக்கை சமர்ப்பிக்கப்படல்\n3. பிரிட்டிஷ் அரசாங்கத்தின் 'அரசியலமைப்பு சீர்திருத்தங்கள் பற்றிய வெள்ளை அறிக்கை' வெளியிடப்படல்\n4. லண்டனில் முதலாவது வட்டமேஜை மாநாடு கூட்டப்படல்",
        "options_en": ["1 -> 4 -> 2 -> 3", "1 -> 2 -> 4 -> 3", "2 -> 1 -> 4 -> 3", "1 -> 2 -> 3 -> 4"],
        "options_ta": ["1 -> 4 -> 2 -> 3", "1 -> 2 -> 4 -> 3", "2 -> 1 -> 4 -> 3", "1 -> 2 -> 3 -> 4"],
        "answer": "b",
        "explanation_en": "Sequence: 1 (Nehru Report Aug 1928) -> 2 (Simon Report May 1930) -> 4 (1st RTC Nov 1930) -> 3 (White Paper Mar 1933).",
        "explanation_ta": "வரிசை: 1 (நேரு அறிக்கை ஆக 1928) -> 2 (சைமன் அறிக்கை மே 1930) -> 4 (1வது RTC நவ 1930) -> 3 (வெள்ளை அறிக்கை மார்ச் 1933)."
    }
]

print(f"Loaded {len(repo)} initial questions.")
