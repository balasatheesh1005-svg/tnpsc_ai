import json
import os

questions = [
    # Question 1: Model 1 - Acts Chronological Order - Analytical
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
            {
                "id": "A",
                "en": "2 -> 1 -> 4 -> 3",
                "ta": "2 -> 1 -> 4 -> 3"
            },
            {
                "id": "B",
                "en": "1 -> 2 -> 3 -> 4",
                "ta": "1 -> 2 -> 3 -> 4"
            },
            {
                "id": "C",
                "en": "2 -> 4 -> 1 -> 3",
                "ta": "2 -> 4 -> 1 -> 3"
            },
            {
                "id": "D",
                "en": "4 -> 2 -> 1 -> 3",
                "ta": "4 -> 2 -> 1 -> 3"
            }
        ],
        "correct_answer": "A",
        "explanation": {
            "en": "Correct Chronological Sequence:\n1. Establishment of Supreme Court at Fort William: 1774 (under Regulating Act, 1773).\n2. Exemption of GG-in-Council from SC jurisdiction: 1781 (Amending Act of 1781 / Act of Settlement).\n3. Establishment of Board of Control: 1784 (Pitt's India Act, 1784).\n4. Extension of GG's overriding powers over Council: 1793 (Charter Act, 1793).\n\nConstitutional Significance: This sequence marks the initial Parliamentary attempt to regulate EIC governance, clarify executive-judicial boundaries, establish dual control (Directors & Board), and solidify central executive command.",
            "ta": "சரியான காலவரிசை:\n1. வில்லியம் கோட்டையில் உச்ச நீதிமன்றம் அமைத்தல்: 1774 (1773 ஒழுங்குமுறைச் சட்டத்தின் கீழ்).\n2. கவர்னர்-ஜெனரலுக்கு உச்ச நீதிமன்ற அதிகார வரம்பிலிருந்து விலக்களித்தல்: 1781 (1781 திருத்தச் சட்டம் / சீரமைப்புச் சட்டம்).\n3. கட்டுப்பாட்டு வாரியம் அமைத்தல்: 1784 (1784 பிட் இந்தியச் சட்டம்).\n4. கவர்னர்-ஜெனரலின் நிராகரிப்பு அதிகாரத்தை நீட்டித்தல்: 1793 (1793 சாசனச் சட்டம்).\n\nஅரசியலமைப்பு முக்கியத்துவம்: இக்காலவரிசை கிழக்கிந்திய கம்பெனியின் நிர்வாகத்தை ஒழுங்குபடுத்தவும், நிர்வாக-நீதிமன்ற எல்லைகளைத் தெளிவுபடுத்தவும், இரட்டைப் பகுப்பாய்வு அமைப்பை ஏற்படுத்தவும் நாடாளுமன்றம் மேற்கொண்ட தொடக்ககால முயற்சிகளைக் காட்டுகிறது."
        },
        "why_not_others": {
            "A": {
                "en": "Correct. 2 (1774) -> 1 (1781) -> 4 (1784) -> 3 (1793) perfectly follows historical enactment dates.",
                "ta": "சரி. 2 (1774) -> 1 (1781) -> 4 (1784) -> 3 (1793) வரலாற்று சட்ட இயற்றல் ஆண்டுகளைத் துல்லியமாகப் பின்பற்றுகிறது."
            },
            "B": {
                "en": "Incorrect. Exemption from SC jurisdiction (1781) occurred AFTER Supreme Court was established (1774).",
                "ta": "தவறு. உச்ச நீதிமன்ற விலக்களிப்பு (1781) உச்ச நீதிமன்றம் அமைக்கப்பட்ட பின்னரே (1774) ஏற்பட்டது."
            },
            "C": {
                "en": "Incorrect. Board of Control was established in 1784, after the Amending Act of 1781.",
                "ta": "தவறு. கட்டுப்பாட்டு வாரியம் 1784-ல் அமைக்கப்பட்டது, இது 1781 திருத்தச் சட்டத்திற்குப் பின்னராகும்."
            },
            "D": {
                "en": "Incorrect. Board of Control (1784) was not established before the Supreme Court (1774).",
                "ta": "தவறு. கட்டுப்பாட்டு வாரியம் (1784) உச்ச நீதிமன்றத்திற்கு (1774) முன் அமைக்கப்படவில்லை."
            }
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
        "tags": [
            "Polity",
            "Historical Background",
            "Chronology",
            "Company Rule",
            "Regulating Act 1773"
        ],
        "question_en": "Arrange the following key legislative provisions during Company Rule in correct chronological order:\n1. Exemption of Governor-General and Council from Supreme Court jurisdiction for official acts\n2. Establishment of Supreme Court of Judicature at Fort William, Calcutta\n3. Extension of Governor-General's overriding powers over his council to future Governors-General\n4. Establishment of the Board of Control to supervise civil, military, and revenue affairs",
        "question_ta": "கம்பெனி ஆட்சியின் போது மேற்கொள்ளப்பட்ட பின்வரும் முக்கிய சட்டப்பூர்வ விதிகளை சரியான காலவரிசையில் அமைக்கவும்:\n1. அதிகாரபூர்வ நடவடிக்கைகளுக்காக உச்ச நீதிமன்ற அதிகார வரம்பிலிருந்து கவர்னர்-ஜெனரல் மற்றும் கவுன்சிலுக்கு விலக்களித்தல்\n2. கொல்கத்தா வில்லியம் கோட்டையில் உச்ச நீதிமன்றம் அமைத்தல்\n3. கவர்னர்-ஜெனரலின் நிராகரிப்பு அதிகாரத்தை எதிர்கால கவர்னர்-ஜெனரல்களுக்கு நீட்டித்தல்\n4. சிவில், ராணுவ மற்றும் வருவாய் விவகாரங்களைக் கண்காணிக்கக் கட்டுப்பாட்டு வாரியத்தை அமைத்தல்",
        "options_en": [
            "2 -> 1 -> 4 -> 3",
            "1 -> 2 -> 3 -> 4",
            "2 -> 4 -> 1 -> 3",
            "4 -> 2 -> 1 -> 3"
        ],
        "options_ta": [
            "2 -> 1 -> 4 -> 3",
            "1 -> 2 -> 3 -> 4",
            "2 -> 4 -> 1 -> 3",
            "4 -> 2 -> 1 -> 3"
        ],
        "answer": "a",
        "explanation_en": "Correct Chronological Sequence:\n1. Supreme Court established at Fort William: 1774\n2. Amending Act exemptions: 1781\n3. Board of Control established: 1784\n4. Charter Act overriding powers extension: 1793.",
        "explanation_ta": "சரியான காலவரிசை:\n1. வில்லியம் கோட்டை உச்ச நீதிமன்றம்: 1774\n2. திருத்தச் சட்ட விலக்களிப்பு: 1781\n3. கட்டுப்பாட்டு வாரியம் உருவாக்கம்: 1784\n4. சாசனச் சட்ட நிராகரிப்பு அதிகார நீட்டிப்பு: 1793."
    },

    # Question 2: Model 1 - Acts Chronological Order - Analytical
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
            {
                "id": "A",
                "en": "1 -> 2 -> 4 -> 3",
                "ta": "1 -> 2 -> 4 -> 3"
            },
            {
                "id": "B",
                "en": "2 -> 1 -> 4 -> 3",
                "ta": "2 -> 1 -> 4 -> 3"
            },
            {
                "id": "C",
                "en": "2 -> 4 -> 1 -> 3",
                "ta": "2 -> 4 -> 1 -> 3"
            },
            {
                "id": "D",
                "en": "4 -> 2 -> 1 -> 3",
                "ta": "4 -> 2 -> 1 -> 3"
            }
        ],
        "correct_answer": "B",
        "explanation": {
            "en": "Correct Chronological Sequence:\n1. Partial abolition of trade monopoly (retaining tea & China): Charter Act of 1813.\n2. Total abolition of EIC trade monopoly: Charter Act of 1833.\n3. Extension of charter without fixed time period: Charter Act of 1853.\n4. Complete transfer of power to Crown: Government of India Act 1858.\n\nConstitutional Significance: This progression illustrates how the British Parliament systematically stripped EIC of commercial monopoly, transformed it into a political administrative entity, kept its tenure indefinite in 1853, and finally abolished Company Rule in 1858.",
            "ta": "சரியான காலவரிசை:\n1. பகுதியளவு வர்த்தக முற்றுரிமை ஒழிப்பு (தேயிலை & சீனா தவிர): 1813 சாசனச் சட்டம்.\n2. கம்பெனி வர்த்தக முற்றுரிமை முழுமையாக ஒழிப்பு: 1833 சாசனச் சட்டம்.\n3. குறிப்பிட்ட காலவரையறையின்றி சாசனம் நீட்டிப்பு: 1853 சாசனச் சட்டம்.\n4. பிரிட்டிஷ் முடிக்கு அதிகாரம் முழுமையாக மாற்றம்: 1858 இந்திய அரசுச் சட்டம்.\n\nஅரசியலமைப்பு முக்கியத்துவம்: இக்காலவரிசை பிரிட்டிஷ் நாடாளுமன்றம் கம்பெனியின் வணிக முற்றுரிமையை எவ்வாறு படிப்படியாக நீக்கி, அதை நிர்வாக அமைப்பாக மாற்றி, 1858-ல் முடிக்கு அதிகாரத்தை மாற்றியது என்பதை விளக்குகிறது."
        },
        "why_not_others": {
            "A": {
                "en": "Incorrect. Total abolition of monopoly (1833) happened AFTER partial abolition (1813).",
                "ta": "தவறு. முழுமையான வர்த்தக முற்றுரிமை ஒழிப்பு (1833) பகுதியளவு ஒழிப்புக்கு (1813) பிறகே நடந்தது."
            },
            "B": {
                "en": "Correct. Sequence 2 (1813) -> 1 (1833) -> 4 (1853) -> 3 (1858) accurately tracks Charter Act evolution.",
                "ta": "சரி. 2 (1813) -> 1 (1833) -> 4 (1853) -> 3 (1858) வரிசை சாசனச் சட்டங்களின் வளர்ச்சியைத் துல்லியமாகக் காட்டுகிறது."
            },
            "C": {
                "en": "Incorrect. Indefinite charter extension (1853) came AFTER 1833 Act.",
                "ta": "தவறு. காலவரையறையற்ற சாசன நீட்டிப்பு (1853) 1833 சட்டத்திற்குப் பின்னரே வந்தது."
            },
            "D": {
                "en": "Incorrect. Charter Act of 1853 (4) was the last of the four Charter Acts.",
                "ta": "தவறு. 1853 சாசனச் சட்டம் (4) நான்கு சாசனச் சட்டங்களில் இறுதியானதாகும்."
            }
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
        "tags": [
            "Polity",
            "Historical Background",
            "Chronology",
            "Charter Acts",
            "Commercial Monopoly"
        ],
        "question_en": "Arrange the following Charter Acts and Parliamentary Acts in correct chronological sequence based on the gradual reduction of East India Company's privileges:\n1. Total abolition of EIC commercial monopoly (including tea and trade with China)\n2. Partial abolition of EIC trade monopoly in India, retaining monopoly in tea and trade with China\n3. Complete transfer of Indian administration from EIC to the British Crown\n4. Extension of EIC charter without specifying any fixed time period for the first time",
        "question_ta": "கிழக்கிந்திய கம்பெனியின் சலுகைகள் படிப்படியாகக் குறைக்கப்பட்டதன் அடிப்படையில் பின்வரும் சாசனச் சட்டங்கள் மற்றும் நாடாளுமன்றச் சட்டங்களை சரியான காலவரிசையில் அமைக்கவும்:\n1. தேயிலை மற்றும் சீனாவுடனான வர்த்தகம் உட்பட கம்பெனியின் வர்த்தக முற்றுரிமை முழுமையாக ஒழிக்கப்படல்\n2. தேயிலை மற்றும் சீனா வர்த்தகம் தவிர்த்து இந்தியாவில் கம்பெனியின் வர்த்தக முற்றுரிமை பகுதியளவாக ஒழிக்கப்படல்\n3. இந்திய நிர்வாகம் கிழக்கிந்திய கம்பெனியிடமிருந்து பிரிட்டிஷ் முடிக்கு முழுமையாக மாற்றப்படல்\n4. எந்தவொரு குறிப்பிட்ட காலவரையறையுமின்றி கம்பெனியின் சாசனம் முதன்முறையாக நீட்டிக்கப்படல்",
        "options_en": [
            "1 -> 2 -> 4 -> 3",
            "2 -> 1 -> 4 -> 3",
            "2 -> 4 -> 1 -> 3",
            "4 -> 2 -> 1 -> 3"
        ],
        "options_ta": [
            "1 -> 2 -> 4 -> 3",
            "2 -> 1 -> 4 -> 3",
            "2 -> 4 -> 1 -> 3",
            "4 -> 2 -> 1 -> 3"
        ],
        "answer": "b",
        "explanation_en": "Sequence: 2 (1813 Act) -> 1 (1833 Act) -> 4 (1853 Act) -> 3 (1858 Act).",
        "explanation_ta": "வரிசை: 2 (1813 சட்டம்) -> 1 (1833 சட்டம்) -> 4 (1853 சட்டம்) -> 3 (1858 சட்டம்)."
    }
]

print(f"Initial test questions count: {len(questions)}")
