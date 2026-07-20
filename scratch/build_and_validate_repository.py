import json
import os
import random

# Target file path
OUTPUT_PATH = r"c:\Users\Home\Desktop\tnpsc_ai\data\questions\polity\historical_background_match_the_following.json"

questions_raw = [
    # ------------------ Group 1: Analytical Matching (10 Questions) ------------------
    {
        "id": "HB_MF_001",
        "subject": "Polity",
        "topic": "Historical Background of the Indian Constitution",
        "difficulty": "Hard",
        "question_type": "Match the Following",
        "list_i_en": [
            "Regulating Act, 1773",
            "Amending Act, 1781",
            "Pitt's India Act, 1784",
            "Charter Act, 1793"
        ],
        "list_i_ta": [
            "1773 ஒழுங்குமுறைச் சட்டம்",
            "1781 திருத்தச் சட்டம்",
            "1784 பிட் இந்தியச் சட்டம்",
            "1793 சாசனச் சட்டம்"
        ],
        "list_ii_en": [
            "Established Board of Control to supervise civil, military and revenue affairs",
            "Extended overriding powers of Governor-General over Council in special cases",
            "Exempted Governor-General and Council from Supreme Court jurisdiction for official acts",
            "Established Supreme Court at Fort William with jurisdiction over Calcutta inhabitants"
        ],
        "list_ii_ta": [
            "சிவில், ராணுவம் மற்றும் வருவாய் விவகாரங்களைக் கண்காணிக்கக் கட்டுப்பாட்டு வாரியம் அமைக்கப்பட்டது",
            "சிறப்பு நிகழ்வுகளில் கவர்னர் ஜெனரல் தனது குழுவின் முடிவை நிராகரிக்கும் அதிகாரம் நீட்டிக்கப்பட்டது",
            "அதிகாரபூர்வ நடவடிக்கைகளுக்காக கவர்னர் ஜெனரல் மற்றும் குழுவிற்கு உச்ச நீதிமன்ற அதிகார வரம்பிலிருந்து விலக்களிக்கப்பட்டது",
            "கொல்கத்தா கோட்டை வில்லியமில் உச்ச நீதிமன்றம் அமைக்கப்பட்டு கொல்கத்தா மக்களுக்கு அதிகார வரம்பு அளிக்கப்பட்டது"
        ],
        "correct_pairs": {"A": 4, "B": 3, "C": 1, "D": 2}, # A-4, B-3, C-1, D-2
        "distractors": [
            {"A": 3, "B": 4, "C": 2, "D": 1},
            {"A": 4, "B": 1, "C": 3, "D": 2},
            {"A": 2, "B": 3, "C": 1, "D": 4}
        ],
        "explanation_en": "A-4: Regulating Act 1773 established Supreme Court at Fort William (1774). B-3: Amending Act 1781 (Act of Settlement) exempted Governor-General & Council from SC jurisdiction. C-1: Pitt's India Act 1784 established Board of Control for political control. D-2: Charter Act 1793 extended GG's overriding power over council.",
        "explanation_ta": "A-4: 1773 ஒழுங்குமுறைச் சட்டம் வில்லியம் கோட்டையில் உச்ச நீதிமன்றத்தை அமைத்தது (1774). B-3: 1781 திருத்தச் சட்டம் கவர்னர் ஜெனரல் மற்றும் குழுவை உச்ச நீதிமன்ற அதிகார வரம்பிலிருந்து விலக்கியது. C-1: 1784 பிட் இந்தியச் சட்டம் கட்டுப்பாட்டு வாரியத்தை அமைத்தது. D-2: 1793 சாசனச் சட்டம் கவர்னர் ஜெனரலின் நிராகரிப்பு அதிகாரத்தை நீட்டித்தது.",
        "why_not_others_en": {
            "A-4, B-3, C-1, D-2": "Correct match across all four early Company Rule constitutional enactments.",
            "A-3, B-4, C-2, D-1": "Incorrect. 1773 Act did not exempt GG from SC; 1781 Act did.",
            "A-4, B-1, C-3, D-2": "Incorrect. Pitt's India Act created Board of Control (1), not SC exemption (3).",
            "A-2, B-3, C-1, D-4": "Incorrect. Overriding power extended in 1793 (D-2), not 1773."
        },
        "why_not_others_ta": {
            "A-4, B-3, C-1, D-2": "அனைத்து நான்கு தொடக்ககால நிறுவன ஆட்சி சட்டங்களுக்கும் சரியான பொருத்தம்.",
            "A-3, B-4, C-2, D-1": "தவறு. 1773 சட்டம் கவர்னர் ஜெனரலுக்கு விலக்களிக்கவில்லை; 1781 சட்டமே விலக்களித்தது.",
            "A-4, B-1, C-3, D-2": "தவறு. பிட் இந்தியச் சட்டம் கட்டுப்பாட்டு வாரியத்தை உருவாக்கியது (1).",
            "A-2, B-3, C-1, D-4": "தவறு. நிராகரிப்பு அதிகாரம் 1793-ல் நீட்டிக்கப்பட்டது."
        },
        "tnpsc_tip_en": "TNPSC Trap: Board of Control was created by Pitt's India Act 1784, whereas Court of Directors already existed under the EIC charter.",
        "tnpsc_tip_ta": "TNPSC பொறி: கட்டுப்பாட்டு வாரியம் 1784 பிட் இந்தியச் சட்டத்தால் உருவாக்கப்பட்டது; இயக்குநர்கள் அவை ஏற்கனவே இருந்தது.",
        "revision_fact_en": "1781 Act of Settlement was passed to remedy defects of the 1773 Regulating Act.",
        "revision_fact_ta": "1773 ஒழுங்குமுறைச் சட்டத்தின் குறைபாடுகளை நிவர்த்தி செய்ய 1781 சீரமைப்புச் சட்டம் இயற்றப்பட்டது.",
        "bloom_level": "Analyze",
        "tags": ["Polity", "Historical Background", "Regulating Act 1773", "Pitt's India Act 1784"]
    },
    {
        "id": "HB_MF_002",
        "subject": "Polity",
        "topic": "Historical Background of the Indian Constitution",
        "difficulty": "Hard",
        "question_type": "Match the Following",
        "list_i_en": [
            "Charter Act, 1813",
            "Charter Act, 1833",
            "Charter Act, 1853",
            "Government of India Act, 1858"
        ],
        "list_i_ta": [
            "1813 சாசனச் சட்டம்",
            "1833 சாசனச் சட்டம்",
            "1853 சாசனச் சட்டம்",
            "1858 இந்திய அரசுச் சட்டம்"
        ],
        "list_ii_en": [
            "15-member Council of India chaired by Secretary of State",
            "Indian Legislative Council created with 6 legislative members",
            "Law Commission of India established under Lord Macaulay",
            "Bishop of Calcutta and ecclesiastical establishment provided"
        ],
        "list_ii_ta": [
            "இந்திய அமைச்சரின் தலைமையில் 15 உறுப்பினர்களைக் கொண்ட இந்தியக் குழு",
            "6 சட்ட உறுப்பினர்களுடன் இந்திய சட்ட மேலவை அமைக்கப்பட்டது",
            "மெக்காலே பிரபுவின் தலைமையில் இந்திய சட்ட ஆணையம் அமைக்கப்பட்டது",
            "கல்கத்தா பிஷப் மற்றும் மத நிறுவன ஏற்பாடுகள் வழங்கப்பட்டன"
        ],
        "correct_pairs": {"A": 4, "B": 3, "C": 2, "D": 1}, # A-4, B-3, C-2, D-1
        "distractors": [
            {"A": 3, "B": 4, "C": 1, "D": 2},
            {"A": 4, "B": 2, "C": 3, "D": 1},
            {"A": 1, "B": 3, "C": 2, "D": 4}
        ],
        "explanation_en": "A-4: Charter Act 1813 defined church establishment with Bishop of Calcutta. B-3: Charter Act 1833 created 1st Law Commission (Macaulay). C-2: Charter Act 1853 created Indian (Central) Legislative Council of 6 members. D-1: GOI Act 1858 created 15-member Council of India assisting Secretary of State.",
        "explanation_ta": "A-4: 1813 சாசனச் சட்டம் கல்கத்தா பிஷப் தலைமையில் சபை அமைப்பை உருவாக்கியது. B-3: 1833 சாசனச் சட்டம் 1-வது சட்ட ஆணையத்தை (மெக்காலே) அமைத்தது. C-2: 1853 சாசனச் சட்டம் 6 உறுப்பினர்களைக் கொண்ட சட்ட மேலவையை உருவாக்கியது. D-1: 1858 அரசுச் சட்டம் 15 உறுப்பினர்கள் கொண்ட இந்தியக் குழுவை உருவாக்கியது.",
        "why_not_others_en": {
            "A-4, B-3, C-2, D-1": "Correct matching of institutional bodies across 19th-century constitutional developments.",
            "A-3, B-4, C-1, D-2": "Incorrect. Law commission was set up under 1833 Act (B-3), not 1813.",
            "A-4, B-2, C-3, D-1": "Incorrect. Legislative council was created by 1853 Act (C-2), not 1833.",
            "A-1, B-3, C-2, D-4": "Incorrect. Council of India was created in 1858 (D-1), not 1813."
        },
        "why_not_others_ta": {
            "A-4, B-3, C-2, D-1": "19 ஆம் நூற்றாண்டு அரசியலமைப்பு வளர்ச்சிகளில் உள்ள நிறுவன அமைப்புகளின் சரியான பொருத்தம்.",
            "A-3, B-4, C-1, D-2": "தவறு. சட்ட ஆணையம் 1833 சட்டத்தின் கீழ் அமைக்கப்பட்டது (B-3).",
            "A-4, B-2, C-3, D-1": "தவறு. சட்ட மேலவை 1853 சட்டத்தால் உருவாக்கப்பட்டது (C-2).",
            "A-1, B-3, C-2, D-4": "தவறு. இந்தியக் குழு 1858-ல் உருவாக்கப்பட்டது (D-1)."
        },
        "tnpsc_tip_en": "TNPSC Trap: Council of India (15 members in London, 1858) is different from Imperial Legislative Council (Calcutta, 1853/1861).",
        "tnpsc_tip_ta": "TNPSC பொறி: லண்டனில் உள்ள 15 உறுப்பினர் 'இந்தியக் குழு' (1858), கொல்கத்தா 'சட்ட மேலவையில்' (1853/1861) இருந்து வேறுபட்டது.",
        "revision_fact_en": "Charter Act 1853 separated executive and legislative functions of Governor-General's Council for the first time.",
        "revision_fact_ta": "1853 சாசனச் சட்டம் முதன்முதலாக கவர்னர் ஜெனரல் குழுவின் நிர்வாக மற்றும் சட்ட பணிகளைப் பிரித்தது.",
        "bloom_level": "Analyze",
        "tags": ["Polity", "Historical Background", "Charter Act 1833", "Charter Act 1853", "GOI Act 1858"]
    },
    {
        "id": "HB_MF_003",
        "subject": "Polity",
        "topic": "Historical Background of the Indian Constitution",
        "difficulty": "Hard",
        "question_type": "Match the Following",
        "list_i_en": [
            "Indian Councils Act, 1861",
            "Indian Councils Act, 1892",
            "Indian Councils Act, 1909",
            "Government of India Act, 1919"
        ],
        "list_i_ta": [
            "1861 இந்தியக் குழுக்கள் சட்டம்",
            "1892 இந்தியக் குழுக்கள் சட்டம்",
            "1909 இந்தியக் குழுக்கள் சட்டம்",
            "1919 இந்திய அரசுச் சட்டம்"
        ],
        "list_ii_en": [
            "Satyendra Prasad Sinha appointed as first Indian to Executive Council",
            "High Commissioner for India appointed in London",
            "Statutory recognition of Portfolio System introduced by Canning",
            "Indirect recommendation process introduced for non-official seats"
        ],
        "list_ii_ta": [
            "சத்யேந்திர பிரசாத் சின்ஹா நிர்வாகக் குழுவில் முதல் இந்திய உறுப்பினராக நியமிக்கப்பட்டார்",
            "லண்டனில் இந்தியாவுக்கான உயர் ஆணையர் நியமிக்கப்பட்டார்",
            "கானிங் பிரபு அறிமுகப்படுத்திய இலாகா முறைக்கு சட்டபூர்வ அங்கீகாரம் வழங்கப்பட்டது",
            "அரசார்பற்ற இடங்களுக்குப் மறைமுகப் பரிந்துரை முறை அறிமுகப்படுத்தப்பட்டது"
        ],
        "correct_pairs": {"A": 3, "B": 4, "C": 1, "D": 2}, # A-3, B-4, C-1, D-2
        "distractors": [
            {"A": 4, "B": 3, "C": 2, "D": 1},
            {"A": 3, "B": 1, "C": 4, "D": 2},
            {"A": 2, "B": 4, "C": 1, "D": 3}
        ],
        "explanation_en": "A-3: 1861 Act recognized Portfolio system (Canning 1859). B-4: 1892 Act used indirect nomination/recommendation. C-1: 1909 Act appointed SP Sinha to Viceroy's Council. D-2: 1919 Act created office of High Commissioner for India in London.",
        "explanation_ta": "A-3: 1861 சட்டம் இலாகா முறைக்கு அங்கீகாரம் அளித்தது. B-4: 1892 சட்டம் மறைமுகப் பரிந்துரை முறையைப் பயன்படுத்தியது. C-1: 1909 சட்டம் எஸ்பி சின்ஹாவை வைஸ்ராய் குழுவில் நியமித்தது. D-2: 1919 சட்டம் லண்டனில் உயர் ஆணையர் அலுவலகத்தை உருவாக்கியது.",
        "why_not_others_en": {
            "A-3, B-4, C-1, D-2": "Correct match of executive expansion and constitutional features.",
            "A-4, B-3, C-2, D-1": "Incorrect. Portfolio system was recognized in 1861 (A-3).",
            "A-3, B-1, C-4, D-2": "Incorrect. SP Sinha was appointed under 1909 Act (C-1), not 1892.",
            "A-2, B-4, C-1, D-3": "Incorrect. High Commissioner post was created in 1919 (D-2)."
        },
        "why_not_others_ta": {
            "A-3, B-4, C-1, D-2": "நிர்வாக விரிவாக்கம் மற்றும் அரசியலமைப்பு சிறப்பம்சங்களின் சரியான பொருத்தம்.",
            "A-4, B-3, C-2, D-1": "தவறு. இலாகா முறை 1861-ல் அங்கீகரிக்கப்பட்டது (A-3).",
            "A-3, B-1, C-4, D-2": "தவறு. எஸ்பி சின்ஹா 1909 சட்டத்தின்கீழ் நியமிக்கப்பட்டார் (C-1).",
            "A-2, B-4, C-1, D-3": "தவறு. உயர் ஆணையர் பதவி 1919-ல் உருவாக்கப்பட்டது (D-2)."
        },
        "tnpsc_tip_en": "TNPSC Trap: Lord Canning introduced Portfolio system in 1859, but Indian Councils Act 1861 gave it statutory recognition.",
        "tnpsc_tip_ta": "TNPSC பொறி: கானிங் பிரபு 1859-ல் இலாகா முறையை அறிமுகப்படுத்தினார், ஆனால் 1861 சட்டமே அதற்கு சட்ட அங்கீகாரம் அளித்தது.",
        "revision_fact_en": "Satyendra Prasad Sinha was appointed as the Law Member in the Viceroy's Executive Council.",
        "revision_fact_ta": "சத்யேந்திர பிரசாத் சின்ஹா வைஸ்ராயின் நிர்வாகக் குழுவில் சட்ட உறுப்பினராக நியமிக்கப்பட்டார்.",
        "bloom_level": "Analyze",
        "tags": ["Polity", "Historical Background", "Indian Councils Act 1861", "Morley-Minto 1909", "Montagu-Chelmsford 1919"]
    },
    {
        "id": "HB_MF_004",
        "subject": "Polity",
        "topic": "Historical Background of the Indian Constitution",
        "difficulty": "Hard",
        "question_type": "Match the Following",
        "list_i_en": [
            "Charter Act, 1813",
            "Indian Councils Act, 1892",
            "Government of India Act, 1919",
            "Government of India Act, 1935"
        ],
        "list_i_ta": [
            "1813 சாசனச் சட்டம்",
            "1892 இந்தியக் குழுக்கள் சட்டம்",
            "1919 இந்திய அரசுச் சட்டம்",
            "1935 இந்திய அரசுச் சட்டம்"
        ],
        "list_ii_en": [
            "Establishment of Reserve Bank of India to manage currency and credit",
            "Separation of Provincial Budgets from Central Budget",
            "Right granted to discuss budget without voting rights",
            "Annual financial allocation of ₹1 Lakh for promotion of education"
        ],
        "list_ii_ta": [
            "நாணயம் மற்றும் கடனைக் கட்டுப்படுத்த இந்திய ரிசர்வ் வங்கி அமைத்தல்",
            "மத்திய வரவுசெலவுத் திட்டத்தில் இருந்து மாகாண வரவுசெலவுத் திட்டத்தைப் பிரித்தல்",
            "வாக்களிக்கும் உரிமையின்றி வரவுசெலவுத் திட்டத்தை விவாதிக்கும் உரிமை",
            "கல்வி வளர்ச்சிக்காக ஆண்டுக்கு ₹1 லட்சம் நிதி ஒதுக்கீடு"
        ],
        "correct_pairs": {"A": 4, "B": 3, "C": 2, "D": 1}, # A-4, B-3, C-2, D-1
        "distractors": [
            {"A": 3, "B": 4, "C": 1, "D": 2},
            {"A": 4, "B": 2, "C": 3, "D": 1},
            {"A": 1, "B": 3, "C": 2, "D": 4}
        ],
        "explanation_en": "A-4: Charter Act 1813 allocated ₹1 Lakh annually for education. B-3: 1892 Act allowed discussion of budget. C-2: 1919 Act separated provincial budgets from central budget. D-1: 1935 Act provided for Reserve Bank of India.",
        "explanation_ta": "A-4: 1813 சாசனச் சட்டம் கல்விக்கு ₹1 லட்சம் ஒதுக்கியது. B-3: 1892 சட்டம் பட்ஜெட் விவாத உரிமையை அளித்தது. C-2: 1919 சட்டம் மாகாண பட்ஜெட்டைப் பிரித்தது. D-1: 1935 சட்டம் ரிசர்வ் வங்கிக்கு வழிவகுத்தது.",
        "why_not_others_en": {
            "A-4, B-3, C-2, D-1": "Correct matching of fiscal and financial evolution.",
            "A-3, B-4, C-1, D-2": "Incorrect. Budget discussion began under 1892 Act (B-3), not 1813.",
            "A-4, B-2, C-3, D-1": "Incorrect. Budget separation occurred in 1919 (C-2), not 1892.",
            "A-1, B-3, C-2, D-4": "Incorrect. RBI provision was in 1935 Act (D-1)."
        },
        "why_not_others_ta": {
            "A-4, B-3, C-2, D-1": "நிதி மற்றும் பொருளாதார பரிணாமத்தின் சரியான பொருத்தம்.",
            "A-3, B-4, C-1, D-2": "தவறு. பட்ஜெட் விவாதம் 1892 சட்டத்தின் கீழ் தொடங்கியது (B-3).",
            "A-4, B-2, C-3, D-1": "தவறு. பட்ஜெட் பிரிப்பு 1919-ல் நடந்தது (C-2).",
            "A-1, B-3, C-2, D-4": "தவறு. ரிசர்வ் வங்கி ஏற்பாடு 1935 சட்டத்தில் இருந்தது (D-1)."
        },
        "tnpsc_tip_en": "TNPSC Trap: Budget discussion was allowed in 1892, supplementary questions in 1909, and voting on budget parts in 1919.",
        "tnpsc_tip_ta": "TNPSC பொறி: 1892-ல் பட்ஜெட் விவாதம், 1909-ல் துணை வினாக்கள், 1919-ல் பட்ஜெட் வாக்களிப்பு அனுமதிக்கப்பட்டன.",
        "revision_fact_en": "RBI was established on April 1, 1935, under the Reserve Bank of India Act 1934 following GOI Act 1935 provisions.",
        "revision_fact_ta": "1935 இந்திய அரசுச் சட்டப் விதிகளின்படி 1935 ஏப்ரல் 1 அன்று ரிசர்வ் வங்கி தொடங்கப்பட்டது.",
        "bloom_level": "Analyze",
        "tags": ["Polity", "Historical Background", "Financial Powers", "RBI Act", "Charter Act 1813"]
    },
    {
        "id": "HB_MF_005",
        "subject": "Polity",
        "topic": "Historical Background of the Indian Constitution",
        "difficulty": "Hard",
        "question_type": "Match the Following",
        "list_i_en": [
            "Charter Act, 1793",
            "Charter Act, 1813",
            "Charter Act, 1833",
            "Charter Act, 1853"
        ],
        "list_i_ta": [
            "1793 சாசனச் சட்டம்",
            "1813 சாசனச் சட்டம்",
            "1833 சாசனச் சட்டம்",
            "1853 சாசனச் சட்டம்"
        ],
        "list_ii_en": [
            "EIC held Indian territories in trust for British Crown without specific time limit",
            "Total abolition of East India Company's trade monopoly",
            "Abolition of EIC trade monopoly except in Tea and China trade",
            "20-year trade monopoly extension with Board of Control paid from Indian revenue"
        ],
        "list_ii_ta": [
            "காலவரையறையின்றி பிரிட்டிஷ் கிரீடத்தின் டிரஸ்டியாக நிறுவனம் இந்தியப் பகுதிகளை வைத்திருந்தது",
            "கிழக்கிந்திய நிறுவனத்தின் வர்த்தக ஏகபோகம் முற்றிலும் ஒழிக்கப்பட்டது",
            "தேயிலை மற்றும் சீனா வர்த்தகம் தவிர நிறுவனத்தின் ஏகபோகம் ஒழிக்கப்பட்டது",
            "இந்திய வருவாயில் இருந்து கட்டுப்பாட்டு வாரிய ஊதியம் வழங்கும் விதியுடன் 20 ஆண்டு ஏகபோக நீட்டிப்பு"
        ],
        "correct_pairs": {"A": 4, "B": 3, "C": 2, "D": 1}, # A-4, B-3, C-2, D-1
        "distractors": [
            {"A": 3, "B": 4, "C": 1, "D": 2},
            {"A": 4, "B": 2, "C": 3, "D": 1},
            {"A": 2, "B": 3, "C": 4, "D": 1}
        ],
        "explanation_en": "A-4: 1793 Act extended monopoly by 20 years and charged Board salaries on Indian revenue. B-3: 1813 Act ended EIC monopoly except Tea and China trade. C-2: 1833 Act completely abolished EIC commercial monopoly. D-1: 1853 Act did not fix a 20-year term, holding territories in trust.",
        "explanation_ta": "A-4: 1793 சட்டம் ஏகபோகத்தை 20 ஆண்டுகள் நீட்டித்து இந்திய வருவாயில் வாரிய ஊதியம் வழங்கியது. B-3: 1813 சட்டம் தேயிலை, சீனா வர்த்தகம் தவிர ஏகபோகத்தை முடித்தது. C-2: 1833 சட்டம் வர்த்தக ஏகபோகத்தை முற்றிலும் ஒழித்தது. D-1: 1853 சட்டம் 20 ஆண்டு காலத்தை நிர்ணயிக்காமல் டிரஸ்டியாகத் தொடரச் செய்தது.",
        "why_not_others_en": {
            "A-4, B-3, C-2, D-1": "Correct evolutionary sequence of East India Company's commercial transition.",
            "A-3, B-4, C-1, D-2": "Incorrect. Tea monopoly was retained in 1813 (B-3), not 1793.",
            "A-4, B-2, C-3, D-1": "Incorrect. Complete monopoly end was 1833 (C-2), not 1813.",
            "A-2, B-3, C-4, D-1": "Incorrect. 1793 Act extended monopoly (A-4)."
        },
        "why_not_others_ta": {
            "A-4, B-3, C-2, D-1": "கிழக்கிந்திய நிறுவனத்தின் வர்த்தக மாற்றத்தின் சரியான வரிசை.",
            "A-3, B-4, C-1, D-2": "தவறு. தேயிலை ஏகபோகம் 1813-ல் தக்கவைக்கப்பட்டது (B-3).",
            "A-4, B-2, C-3, D-1": "தவறு. முழுமையான ஏகபோக முடிவு 1833 (C-2).",
            "A-2, B-3, C-4, D-1": "தவறு. 1793 சட்டம் ஏகபோகத்தை நீட்டித்தது (A-4)."
        },
        "tnpsc_tip_en": "TNPSC Trap: 1813 Act partially ended monopoly (kept Tea & China trade); 1833 Act totally ended all commercial monopoly.",
        "tnpsc_tip_ta": "TNPSC பொறி: 1813 சட்டம் பகுதி ஏகபோக முடிவு; 1833 சட்டம் முழுமையான வர்த்தக ஏகபோக முடிவு.",
        "revision_fact_en": "Charter Act 1853 was the last of the four Charter Acts passed between 1793 and 1853.",
        "revision_fact_ta": "1793 முதல் 1853 வரை இயற்றப்பட்ட நான்கு சாசனச் சட்டங்களில் 1853 சாசனச் சட்டமே கடைசியானது.",
        "bloom_level": "Analyze",
        "tags": ["Polity", "Historical Background", "Charter Act 1813", "Charter Act 1833", "EIC Monopoly"]
    },
    {
        "id": "HB_MF_006",
        "subject": "Polity",
        "topic": "Historical Background of the Indian Constitution",
        "difficulty": "Hard",
        "question_type": "Match the Following",
        "list_i_en": [
            "Indian Councils Act, 1861",
            "Indian Councils Act, 1909",
            "Government of India Act, 1919",
            "Government of India Act, 1935"
        ],
        "list_i_ta": [
            "1861 இந்தியக் குழுக்கள் சட்டம்",
            "1909 இந்தியக் குழுக்கள் சட்டம்",
            "1919 இந்திய அரசுச் சட்டம்",
            "1935 இந்திய அரசுச் சட்டம்"
        ],
        "list_ii_en": [
            "Proposed Dyarchy at Federal Centre with Transferred and Reserved subjects",
            "Introduced Dyarchy in Provinces with Transferred and Reserved subjects",
            "Allowed members to ask supplementary questions and move resolutions",
            "Restored legislative powers to Bombay and Madras Presidencies"
        ],
        "list_ii_ta": [
            "மத்திய கூட்டாட்சியில் மாற்றப்பட்ட மற்றும் ஒதுக்கப்பட்ட பாடங்களுடன் இரட்டை ஆட்சி முன்மொழியப்பட்டது",
            "மாகாணங்களில் மாற்றப்பட்ட மற்றும் ஒதுக்கப்பட்ட பாடங்களுடன் இரட்டை ஆட்சி அறிமுகப்படுத்தப்பட்டது",
            "உறுப்பினர்கள் துணை வினாக்கள் கேட்கவும் தீர்மானங்கள் கொண்டு வரவும் அனுமதிக்கப்பட்டனர்",
            "பம்பாய் மற்றும் மெட்ராஸ் மாகாணங்களுக்கு சட்ட அதிகாரங்கள் மீண்டும் வழங்கப்பட்டன"
        ],
        "correct_pairs": {"A": 4, "B": 3, "C": 2, "D": 1}, # A-4, B-3, C-2, D-1
        "distractors": [
            {"A": 3, "B": 4, "C": 1, "D": 2},
            {"A": 4, "B": 1, "C": 2, "D": 3},
            {"A": 2, "B": 3, "C": 4, "D": 1}
        ],
        "explanation_en": "A-4: 1861 Act restored legislative powers to Bombay & Madras. B-3: 1909 Act allowed supplementary questions. C-2: 1919 Act introduced Provincial Dyarchy. D-1: 1935 Act proposed Central Dyarchy.",
        "explanation_ta": "A-4: 1861 சட்டம் பம்பாய், மெட்ராஸுக்கு சட்ட அதிகாரங்களை மீட்டுத் தந்தது. B-3: 1909 சட்டம் துணை வினாக்களை அனுமதித்தது. C-2: 1919 சட்டம் மாகாண இரட்டை ஆட்சியை அறிமுகப்படுத்தியது. D-1: 1935 சட்டம் மத்திய இரட்டை ஆட்சியை முன்மொழிந்தது.",
        "why_not_others_en": {
            "A-4, B-3, C-2, D-1": "Correct distinction between provincial legislative restoration, legislative powers, and provincial vs central dyarchy.",
            "A-3, B-4, C-1, D-2": "Incorrect. Legislative restoration was 1861 (A-4), not 1909.",
            "A-4, B-1, C-2, D-3": "Incorrect. Central dyarchy was 1935 (D-1), not 1909.",
            "A-2, B-3, C-4, D-1": "Incorrect. Provincial dyarchy was introduced in 1919 (C-2)."
        },
        "why_not_others_ta": {
            "A-4, B-3, C-2, D-1": "மாகாண சட்ட அதிகாரம், சட்ட மேலவை உரிமைகள் மற்றும் இரட்டை ஆட்சிகளின் சரியான பொருத்தம்.",
            "A-3, B-4, C-1, D-2": "தவறு. சட்ட அதிகாரம் 1861-ல் மீட்கப்பட்டது (A-4).",
            "A-4, B-1, C-2, D-3": "தவறு. மத்திய இரட்டை ஆட்சி 1935 (D-1).",
            "A-2, B-3, C-4, D-1": "தவறு. மாகாண இரட்டை ஆட்சி 1919-ல் வந்தது (C-2)."
        },
        "tnpsc_tip_en": "TNPSC Trap: Dyarchy was established in PROVINCES by 1919 Act and ABOLISHED in provinces by 1935 Act (which proposed it at Centre).",
        "tnpsc_tip_ta": "TNPSC பொறி: இரட்டை ஆட்சி 1919 சட்டத்தால் மாகாணங்களில் கொண்டுவரப்பட்டு, 1935 சட்டத்தால் மாகாணங்களில் ஒழிக்கப்பட்டது.",
        "revision_fact_en": "Transferred subjects in 1919 Act were administered by Governor with ministers; Reserved subjects by Governor with Executive Council.",
        "revision_fact_ta": "1919 சட்டத்தில் மாற்றப்பட்ட தலைப்புகள் அமைச்சர்களுடனும், ஒதுக்கப்பட்ட தலைப்புகள் நிர்வாகக் குழுவுடனும் ஆளுநரால் நிர்வகிக்கப்பட்டன.",
        "bloom_level": "Analyze",
        "tags": ["Polity", "Historical Background", "Dyarchy", "GOI Act 1919", "GOI Act 1935"]
    },
    {
        "id": "HB_MF_007",
        "subject": "Polity",
        "topic": "Historical Background of the Indian Constitution",
        "difficulty": "Hard",
        "question_type": "Match the Following",
        "list_i_en": [
            "Indian Councils Act, 1892",
            "Indian Councils Act, 1909",
            "Government of India Act, 1919",
            "Government of India Act, 1935"
        ],
        "list_i_ta": [
            "1892 இந்தியக் குழுக்கள் சட்டம்",
            "1909 இந்தியக் குழுக்கள் சட்டம்",
            "1919 இந்திய அரசுச் சட்டம்",
            "1935 இந்திய அரசுச் சட்டம்"
        ],
        "list_ii_en": [
            "Separate electorates extended to Depressed Classes, Women, and Labour",
            "Separate electorates extended to Sikhs, Indian Christians, Anglo-Indians, and Europeans",
            "Separate electorates legalized for Muslims",
            "Indirect recommendation process introduced for non-official members"
        ],
        "list_ii_ta": [
            "பிற்படுத்தப்பட்ட வகுப்பினர், பெண்கள் மற்றும் தொழிலாளர்களுக்கு தனித் தொகுதிகள் நீட்டிக்கப்பட்டன",
            "சீக்கியர்கள், இந்தியக் கிறிஸ்தவர்கள், ஆங்லோ-இந்தியர்கள் மற்றும் ஐரோப்பியர்களுக்கு தனித் தொகுதிகள் நீட்டிக்கப்பட்டன",
            "முஸ்லிம்களுக்கு தனித் தொகுதிகள் சட்டப்பூர்வமாக்கப்பட்டன",
            "அரசார்பற்ற உறுப்பினர்களுக்கு மறைமுகப் பரிந்துரை முறை அறிமுகப்படுத்தப்பட்டது"
        ],
        "correct_pairs": {"A": 4, "B": 3, "C": 2, "D": 1}, # A-4, B-3, C-2, D-1
        "distractors": [
            {"A": 3, "B": 4, "C": 1, "D": 2},
            {"A": 4, "B": 2, "C": 3, "D": 1},
            {"A": 1, "B": 3, "C": 2, "D": 4}
        ],
        "explanation_en": "A-4: 1892 Act used indirect nomination/recommendation. B-3: 1909 Act introduced separate electorates for Muslims. C-2: 1919 Act extended separate electorates to Sikhs, Christians, Anglo-Indians, Europeans. D-1: 1935 Act extended them to Depressed Classes, Women, Labour.",
        "explanation_ta": "A-4: 1892 சட்டம் மறைமுகப் பரிந்துரையைப் பயன்படுத்தியது. B-3: 1909 சட்டம் முஸ்லிம்களுக்கு தனித் தொகுதி அறிமுகப்படுத்தியது. C-2: 1919 சட்டம் சீக்கியர், கிறிஸ்தவர், ஆங்லோ இந்தியர், ஐரோப்பியருக்கு நீட்டித்தது. D-1: 1935 சட்டம் ஒடுக்கப்பட்டோர், பெண்கள், தொழிலாளருக்கு நீட்டித்தது.",
        "why_not_others_en": {
            "A-4, B-3, C-2, D-1": "Correct chronological expansion of communal representation in India.",
            "A-3, B-4, C-1, D-2": "Incorrect. Muslim separate electorates started in 1909 (B-3), not 1892.",
            "A-4, B-2, C-3, D-1": "Incorrect. Sikh/Christian electorates were added in 1919 (C-2).",
            "A-1, B-3, C-2, D-4": "Incorrect. Depressed classes extension was in 1935 (D-1)."
        },
        "why_not_others_ta": {
            "A-4, B-3, C-2, D-1": "இந்தியாவில் வகுப்புவாதப் பிரதிநிதித்துவத்தின் சரியான காலவரிசை வளர்ச்சி.",
            "A-3, B-4, C-1, D-2": "தவறு. முஸ்லிம் தனித் தொகுதி 1909-ல் தொடங்கியது (B-3).",
            "A-4, B-2, C-3, D-1": "தவறு. சீக்கியர்/கிறிஸ்தவர் தொகுதிகள் 1919-ல் சேர்க்கப்பட்டன (C-2).",
            "A-1, B-3, C-2, D-4": "தவறு. ஒடுக்கப்பட்டோர் சேர்க்கை 1935 சட்டத்தில் நடந்தது (D-1)."
        },
        "tnpsc_tip_en": "TNPSC Trap: Lord Minto is known as the 'Father of Communal Electorate' for introducing Muslim separate electorate in 1909.",
        "tnpsc_tip_ta": "TNPSC பொறி: 1909-ல் முஸ்லிம்களுக்கு தனித் தொகுதி அறிமுகப்படுத்தியதால் மிண்டோ பிரபு 'வகுப்புவாதத் தொகுதிகளின் தந்தை' எனப்படுகிறார்.",
        "revision_fact_en": "Poona Pact (1932) modified the Communal Award, retaining joint electorates with reserved seats for Depressed Classes.",
        "revision_fact_ta": "பூனா ஒப்பந்தம் (1932) வகுப்புவாத அறிக்கையை திருத்தி, ஒடுக்கப்பட்டோருக்கு இடஒதுக்கீட்டுடன் கூடிய கூட்டுத் தொகுதிகளைப் பராமரித்தது.",
        "bloom_level": "Analyze",
        "tags": ["Polity", "Historical Background", "Communal Electorates", "Morley-Minto 1909", "GOI Act 1935"]
    },
    {
        "id": "HB_MF_008",
        "subject": "Polity",
        "topic": "Historical Background of the Indian Constitution",
        "difficulty": "Hard",
        "question_type": "Match the Following",
        "list_i_en": [
            "Regulating Act, 1773",
            "Amending Act, 1781",
            "Charter Act, 1833",
            "Government of India Act, 1935"
        ],
        "list_i_ta": [
            "1773 ஒழுங்குமுறைச் சட்டம்",
            "1781 திருத்தச் சட்டம்",
            "1833 சாசனச் சட்டம்",
            "1935 இந்திய அரசுச் சட்டம்"
        ],
        "list_ii_en": [
            "Established Federal Court of India (set up in 1937)",
            "First Law Commission appointed under Lord Macaulay for law codification",
            "Recognized appeals from Provincial Courts to Governor-General-in-Council",
            "Established Supreme Court of Judicature at Fort William Calcutta"
        ],
        "list_ii_ta": [
            "இந்தியக் கூட்டாட்சி நீதிமன்றம் அமைக்கப்பட்டது (1937-ல் இயங்கியது)",
            "சட்டங்களை முறைப்படுத்த மெக்காலே பிரபு தலைமையில் முதல் சட்ட ஆணையம் நியமனம்",
            "மாகாண நீதிமன்றங்களில் இருந்து கவர்னர் ஜெனரல் குழுவிற்கு மேல்முறையீடு அங்கீகரிக்கப்பட்டது",
            "கொல்கத்தா கோட்டை வில்லியமில் உச்ச நீதிமன்றம் அமைக்கப்பட்டது"
        ],
        "correct_pairs": {"A": 4, "B": 3, "C": 2, "D": 1}, # A-4, B-3, C-2, D-1
        "distractors": [
            {"A": 3, "B": 4, "C": 1, "D": 2},
            {"A": 4, "B": 2, "C": 3, "D": 1},
            {"A": 2, "B": 3, "C": 1, "D": 4}
        ],
        "explanation_en": "A-4: 1773 Act set up Supreme Court at Calcutta. B-3: 1781 Act recognized provincial court appeals to GG-in-Council. C-2: 1833 Act created 1st Law Commission. D-1: 1935 Act established Federal Court of India.",
        "explanation_ta": "A-4: 1773 சட்டம் கல்கத்தாவில் உச்ச நீதிமன்றத்தை அமைத்தது. B-3: 1781 சட்டம் மாகாண மேல்முறையீடுகளைக் கவர்னர் ஜெனரல் குழுவிடம் அனுமதித்தது. C-2: 1833 சட்டம் 1-வது சட்ட ஆணையத்தை உருவாக்கியது. D-1: 1935 சட்டம் கூட்டாட்சி நீதிமன்றத்தை அமைத்தது.",
        "why_not_others_en": {
            "A-4, B-3, C-2, D-1": "Correct matching of key judicial landmarks in British India.",
            "A-3, B-4, C-1, D-2": "Incorrect. SC Calcutta was 1773 Act (A-4), not 1781.",
            "A-4, B-2, C-3, D-1": "Incorrect. Macaulay Law Commission was 1833 (C-2), not 1781.",
            "A-2, B-3, C-1, D-4": "Incorrect. Federal court was set up by 1935 Act (D-1)."
        },
        "why_not_others_ta": {
            "A-4, B-3, C-2, D-1": "பிரிட்டிஷ் இந்தியாவின் முக்கிய நீதித்துறை மைல்கற்களின் சரியான பொருத்தம்.",
            "A-3, B-4, C-1, D-2": "தவறு. கல்கத்தா உச்ச நீதிமன்றம் 1773 சட்டம் (A-4).",
            "A-4, B-2, C-3, D-1": "தவறு. மெக்காலே சட்ட ஆணையம் 1833 சட்டம் (C-2).",
            "A-2, B-3, C-1, D-4": "தவறு. கூட்டாட்சி நீதிமன்றம் 1935 சட்டத்தால் அமைக்கப்பட்டது (D-1)."
        },
        "tnpsc_tip_en": "TNPSC Trap: Sir Elijah Impey was the first Chief Justice of SC at Calcutta (1774), whereas Sir Maurice Gwyer was the first CJ of Federal Court (1937).",
        "tnpsc_tip_ta": "TNPSC பொறி: சர் எலிஜா இம்பே கல்கத்தா உச்ச நீதிமன்றத்தின் முதல் தலைமை நீதிபதி (1774); சர் மோரிஸ் குவயர் கூட்டாட்சி நீதிமன்றத்தின் முதல் தலைமை நீதிபதி (1937).",
        "revision_fact_en": "Federal Court of India functioned until Supreme Court of India was inaugurated on January 28, 1950.",
        "revision_fact_ta": "1950 ஜனவரி 28 அன்று இந்திய உச்ச நீதிமன்றம் தொடங்கும் வரை கூட்டாட்சி நீதிமன்றம் செயல்பட்டது.",
        "bloom_level": "Analyze",
        "tags": ["Polity", "Historical Background", "Judiciary", "Supreme Court 1774", "Federal Court 1937"]
    },
    {
        "id": "HB_MF_009",
        "subject": "Polity",
        "topic": "Historical Background of the Indian Constitution",
        "difficulty": "Hard",
        "question_type": "Match the Following",
        "list_i_en": [
            "Charter Act, 1833",
            "Charter Act, 1853",
            "Government of India Act, 1919",
            "Government of India Act, 1935"
        ],
        "list_i_ta": [
            "1833 சாசனச் சட்டம்",
            "1853 சாசனச் சட்டம்",
            "1919 இந்திய அரசுச் சட்டம்",
            "1935 இந்திய அரசுச் சட்டம்"
        ],
        "list_ii_en": [
            "Provision for Federal, Provincial, and Joint Public Service Commissions",
            "Central Public Service Commission established in 1926 (Lee Commission)",
            "Open competitive examination introduced for ICS recruitment (Macaulay Committee)",
            "Attempted non-discrimination in employment under Section 87"
        ],
        "list_ii_ta": [
            "கூட்டாட்சி, மாகாண மற்றும் கூட்டு பொதுச்சேவை ஆணையங்களுக்கான விதிகள்",
            "1926-ல் மத்திய பொதுச்சேவை ஆணையம் அமைத்தல் (லீ ஆணையப் பரிந்துரை)",
            "இந்திய குடிமைப் பணி தேர்வுக்கு திறந்தவெளி போட்டித் தேர்வு அறிமுகம் (மெக்காலே குழு)",
            "பிரிவு 87-ன் கீழ் வேலைவாய்ப்பில் பாகுபாடற்ற நிலைக்கான முயற்சி"
        ],
        "correct_pairs": {"A": 4, "B": 3, "C": 2, "D": 1}, # A-4, B-3, C-2, D-1
        "distractors": [
            {"A": 3, "B": 4, "C": 1, "D": 2},
            {"A": 4, "B": 1, "C": 2, "D": 3},
            {"A": 2, "B": 3, "C": 4, "D": 1}
        ],
        "explanation_en": "A-4: 1833 Act attempted open competition via Sec 87. B-3: 1853 Act introduced open competitive exams (Macaulay Committee 1854). C-2: 1919 Act led to Central PSC in 1926. D-1: 1935 Act created Federal, Provincial, and Joint PSCs.",
        "explanation_ta": "A-4: 1833 சட்டம் பிரிவு 87 மூலம் திறந்த போட்டியை முயன்றது. B-3: 1853 சட்டம் போட்டித் தேர்வை அறிமுகப்படுத்தியது (மெக்காலே குழு 1854). C-2: 1919 சட்டம் 1926-ல் மத்திய பொதுச்சேவை ஆணையத்தை அமைத்தது. D-1: 1935 சட்டம் கூட்டாட்சி, மாகாண மற்றும் கூட்டுத் தேர்வாணையங்களை அமைத்தது.",
        "why_not_others_en": {
            "A-4, B-3, C-2, D-1": "Correct matching of Civil Service recruitment evolution.",
            "A-3, B-4, C-1, D-2": "Incorrect. Sec 87 was in 1833 Act (A-4), not 1853.",
            "A-4, B-1, C-2, D-3": "Incorrect. Macaulay Committee open competition was 1853 (B-3).",
            "A-2, B-3, C-4, D-1": "Incorrect. Central PSC set up in 1926 was under 1919 Act (C-2)."
        },
        "why_not_others_ta": {
            "A-4, B-3, C-2, D-1": "குடிமைப் பணி ஆட்சேர்ப்பு பரிணாமத்தின் சரியான பொருத்தம்.",
            "A-3, B-4, C-1, D-2": "தவறு. பிரிவு 87 1833 சட்டத்தில் இருந்தது (A-4).",
            "A-4, B-1, C-2, D-3": "தவறு. மெக்காலே குழு போட்டித் தேர்வு 1853 சட்டம் (B-3).",
            "A-2, B-3, C-4, D-1": "தவறு. 1926 மத்திய தேர்வாணையம் 1919 சட்டத்தின்கீழ் அமைக்கப்பட்டது (C-2)."
        },
        "tnpsc_tip_en": "TNPSC Trap: Section 87 of Charter Act 1833 attempted open competition, but Court of Directors negated it. 1853 Act actually implemented it.",
        "tnpsc_tip_ta": "TNPSC பொறி: 1833 சாசனச் சட்டத்தின் பிரிவு 87 திறந்த போட்டியை முயன்றது, ஆனால் இயக்குநர்கள் அவை அதை நிராகரித்தது. 1853 சட்டமே அதை அமல்படுத்தியது.",
        "revision_fact_en": "Lee Commission on Superior Civil Services in India was appointed in 1923 and submitted report in 1924.",
        "revision_fact_ta": "இந்திய உயர் குடிமைப் பணிகளுக்கான லீ ஆணையம் 1923-ல் நியமிக்கப்பட்டு 1924-ல் அறிக்கை அளித்தது.",
        "bloom_level": "Analyze",
        "tags": ["Polity", "Historical Background", "Civil Services", "UPSC Evolution", "Lee Commission"]
    },
    {
        "id": "HB_MF_010",
        "subject": "Polity",
        "topic": "Historical Background of the Indian Constitution",
        "difficulty": "Hard",
        "question_type": "Match the Following",
        "list_i_en": [
            "Pitt's India Act, 1784",
            "Government of India Act, 1858",
            "Indian Councils Act, 1861",
            "Indian Independence Act, 1947"
        ],
        "list_i_ta": [
            "1784 பிட் இந்தியச் சட்டம்",
            "1858 இந்திய அரசுச் சட்டம்",
            "1861 இந்தியக் குழுக்கள் சட்டம்",
            "1947 இந்திய சுதந்திரச் சட்டம்"
        ],
        "list_ii_en": [
            "Office of Secretary of State for India abolished",
            "Viceroy empowered to issue Ordinances during emergencies",
            "Crown assumed direct governance; Secretary of State for India post created",
            "Board of Control created establishing System of Double Government"
        ],
        "list_ii_ta": [
            "இந்திய அமைச்சர் அலுவலகம் ஒழிக்கப்பட்டது",
            "அவசர காலங்களில் அவசரச் சட்டங்களை பிறப்பிக்க வைஸ்ராய்க்கு அதிகாரம் அளித்தது",
            "பிரிட்டிஷ் கிரீடம் நேரடி ஆட்சியை ஏற்றுக்கொண்டது; இந்திய அமைச்சர் பதவி உருவாக்கப்பட்டது",
            "இரட்டை ஆட்சி முறையை நிறுவும் கட்டுப்பாட்டு வாரியம் உருவாக்கப்பட்டது"
        ],
        "correct_pairs": {"A": 4, "B": 3, "C": 2, "D": 1}, # A-4, B-3, C-2, D-1
        "distractors": [
            {"A": 3, "B": 4, "C": 1, "D": 2},
            {"A": 4, "B": 2, "C": 3, "D": 1},
            {"A": 1, "B": 3, "C": 2, "D": 4}
        ],
        "explanation_en": "A-4: 1784 Act created Board of Control (Double Govt). B-3: 1858 Act created Secretary of State post. C-2: 1861 Act gave Ordinance power to Viceroy (6 months validity). D-1: 1947 Act abolished Secretary of State for India.",
        "explanation_ta": "A-4: 1784 சட்டம் கட்டுப்பாட்டு வாரியத்தை அமைத்தது. B-3: 1858 சட்டம் இந்திய அமைச்சர் பதவியை உருவாக்கியது. C-2: 1861 சட்டம் வைஸ்ராய்க்கு அவசரச்சட்ட அதிகாரத்தை அளித்தது. D-1: 1947 சட்டம் இந்திய அமைச்சர் பதவியை ஒழித்தது.",
        "why_not_others_en": {
            "A-4, B-3, C-2, D-1": "Correct matching of Crown and Home Government structural changes.",
            "A-3, B-4, C-1, D-2": "Incorrect. Board of Control was created in 1784 (A-4), not 1858.",
            "A-4, B-2, C-3, D-1": "Incorrect. Secretary of State was created in 1858 (B-3), not 1861.",
            "A-1, B-3, C-2, D-4": "Incorrect. Secretary of State office was abolished in 1947 (D-1)."
        },
        "why_not_others_ta": {
            "A-4, B-3, C-2, D-1": "கிரீடம் மற்றும் தாய் அரசாங்க அமைப்பின் மாற்றங்களின் சரியான பொருத்தம்.",
            "A-3, B-4, C-1, D-2": "தவறு. கட்டுப்பாட்டு வாரியம் 1784-ல் உருவாக்கப்பட்டது (A-4).",
            "A-4, B-2, C-3, D-1": "தவறு. இந்திய அமைச்சர் பதவி 1858-ல் உருவாக்கப்பட்டது (B-3).",
            "A-1, B-3, C-2, D-4": "தவறு. இந்திய அமைச்சர் அலுவலகம் 1947-ல் ஒழிக்கப்பட்டது (D-1)."
        },
        "tnpsc_tip_en": "TNPSC Trap: Lord Stanley was the first Secretary of State for India; Lord Canning was the first Viceroy of India under 1858 Act.",
        "tnpsc_tip_ta": "TNPSC பொறி: லார்ட் ஸ்டான்லி இந்தியாவின் முதல் இந்திய அமைச்சர்; 1858 சட்டத்தின்கீழ் கானிங் பிரபு இந்தியாவின் முதல் வைஸ்ராய்.",
        "revision_fact_en": "1861 Act empowered Viceroy to issue Ordinances having life of 6 months without Legislative Council concurrence.",
        "revision_fact_ta": "1861 சட்டம் சட்ட மேலவையின் ஒப்புதலின்றி 6 மாத கால அவசரச் சட்டங்களை பிறப்பிக்க வைஸ்ராய்க்கு அதிகாரம் அளித்தது.",
        "bloom_level": "Analyze",
        "tags": ["Polity", "Historical Background", "Secretary of State", "Double Government", "1947 Independence Act"]
    },

    # ------------------ Group 2: Conceptual Matching (10 Questions) ------------------
    {
        "id": "HB_MF_011",
        "subject": "Polity",
        "topic": "Historical Background of the Indian Constitution",
        "difficulty": "Hard",
        "question_type": "Match the Following",
        "list_i_en": [
            "Peak of Unitary Centralization",
            "Initiation of Legislative Decentralization",
            "Establishment of Provincial Autonomy",
            "Attainment of Dominion Sovereignty"
        ],
        "list_i_ta": [
            "ஒற்றையாட்சி மத்தியமயமாக்கலின் உச்சம்",
            "சட்டமன்ற பரவலாக்கலின் தொடக்கம்",
            "மாகாண தன்னாட்சி அமைப்பு",
            "டொமினியன் இறையாண்மை அடைதல்"
        ],
        "list_ii_en": [
            "Indian Independence Act, 1947",
            "Government of India Act, 1935",
            "Indian Councils Act, 1861",
            "Charter Act, 1833"
        ],
        "list_ii_ta": [
            "1947 இந்திய சுதந்திரச் சட்டம்",
            "1935 இந்திய அரசுச் சட்டம்",
            "1861 இந்தியக் குழுக்கள் சட்டம்",
            "1833 சாசனச் சட்டம்"
        ],
        "correct_pairs": {"A": 4, "B": 3, "C": 2, "D": 1}, # A-4, B-3, C-2, D-1
        "distractors": [
            {"A": 3, "B": 4, "C": 1, "D": 2},
            {"A": 4, "B": 2, "C": 3, "D": 1},
            {"A": 2, "B": 3, "C": 4, "D": 1}
        ],
        "explanation_en": "A-4: Charter Act 1833 concentrated all legislative power in Governor-General of India (Peak Centralization). B-3: 1861 Act restored legislative powers to Bombay & Madras (Initiated Decentralization). C-2: 1935 Act introduced Provincial Autonomy. D-1: 1947 Act granted Dominion Sovereignty.",
        "explanation_ta": "A-4: 1833 சாசனச் சட்டம் அனைத்து சட்ட அதிகாரத்தையும் மையப்படுத்தியது (மத்தியமயமாக்கலின் உச்சம்). B-3: 1861 சட்டம் மாகாண அதிகாரங்களை மீட்டு தந்தது (பரவலாக்கல் தொடக்கம்). C-2: 1935 சட்டம் மாகாண தன்னாட்சியைத் தந்தது. D-1: 1947 சட்டம் டொமினியன் இறையாண்மையை அளித்தது.",
        "why_not_others_en": {
            "A-4, B-3, C-2, D-1": "Correct matching of underlying constitutional doctrines.",
            "A-3, B-4, C-1, D-2": "Incorrect. Centralization peak was 1833 (A-4), not 1861.",
            "A-4, B-2, C-3, D-1": "Incorrect. Decentralization started in 1861 (B-3), not 1935.",
            "A-2, B-3, C-4, D-1": "Incorrect. Provincial autonomy was established in 1935 (C-2)."
        },
        "why_not_others_ta": {
            "A-4, B-3, C-2, D-1": "அரசியலமைப்பு கோட்பாடுகளின் சரியான பொருத்தம்.",
            "A-3, B-4, C-1, D-2": "தவறு. மத்தியமயமாக்கலின் உச்சம் 1833 சாசனச் சட்டம் (A-4).",
            "A-4, B-2, C-3, D-1": "தவறு. பரவலாக்கல் 1861-ல் தொடங்கியது (B-3).",
            "A-2, B-3, C-4, D-1": "தவறு. மாகாண தன்னாட்சி 1935-ல் நிறுவப்பட்டது (C-2)."
        },
        "tnpsc_tip_en": "TNPSC Trap: Centralization started in 1773 and climaxed in 1833; Decentralization started in 1861 and climaxed in 1935.",
        "tnpsc_tip_ta": "TNPSC பொறி: மத்தியமயமாக்கல் 1773-ல் தொடங்கி 1833-ல் உச்சமடைந்தது; பரவலாக்கல் 1861-ல் தொடங்கி 1935-ல் உச்சமடைந்தது.",
        "revision_fact_en": "GOI Act 1935 abolished provincial dyarchy and established autonomy with responsible ministers.",
        "revision_fact_ta": "1935 இந்திய அரசுச் சட்டம் மாகாண இரட்டை ஆட்சியை ஒழித்து பொறுப்புள்ள அமைச்சர்களுடன் தன்னாட்சியை நிறுவியது.",
        "bloom_level": "Evaluate",
        "tags": ["Polity", "Historical Background", "Centralization", "Decentralization", "Provincial Autonomy"]
    },
    {
        "id": "HB_MF_012",
        "subject": "Polity",
        "topic": "Historical Background of the Indian Constitution",
        "difficulty": "Hard",
        "question_type": "Match the Following",
        "list_i_en": [
            "Lord Macaulay",
            "Lord Canning",
            "Lord Minto",
            "Lord Chelmsford"
        ],
        "list_i_ta": [
            "மெக்காலே பிரபு",
            "கானிங் பிரபு",
            "மிண்டோ பிரபு",
            "செம்ஸ்ஃபோர்டு பிரபு"
        ],
        "list_ii_en": [
            "Introduced Dyarchy in Provinces and Bicameralism at Centre",
            "Legalized communal electorates for Muslims ('Father of Communal Electorate')",
            "Introduced Portfolio System and enacted High Courts Act 1861",
            "Headed First Law Commission & Committee on Indian Civil Services"
        ],
        "list_ii_ta": [
            "மாகாணங்களில் இரட்டை ஆட்சியையும் மத்திய மேலவையில் இரு அவைகளையும் அறிமுகப்படுத்தினார்",
            "முஸ்லிம்களுக்கான வகுப்புவாதத் தொகுதிகளை சட்டப்பூர்வமாக்கினார் ('வகுப்புவாதத் தொகுதிகளின் தந்தை')",
            "இலாகா முறையை அறிமுகப்படுத்தி 1861 உயர் நீதிமன்றச் சட்டத்தைச் செயல்படுத்தினார்",
            "முதல் சட்ட ஆணையம் மற்றும் குடிமைப் பணிக் குழுவின் தலைவராக இருந்தார்"
        ],
        "correct_pairs": {"A": 4, "B": 3, "C": 2, "D": 1}, # A-4, B-3, C-2, D-1
        "distractors": [
            {"A": 3, "B": 4, "C": 1, "D": 2},
            {"A": 4, "B": 1, "C": 2, "D": 3},
            {"A": 2, "B": 3, "C": 4, "D": 1}
        ],
        "explanation_en": "A-4: Macaulay chaired 1st Law Commission & 1854 Civil Services Committee. B-3: Canning introduced portfolio system & 1861 High Courts Act. C-2: Minto introduced Muslim separate electorate (Father of Communal Electorate). D-1: Chelmsford (with Montagu) introduced provincial dyarchy & central bicameralism in 1919.",
        "explanation_ta": "A-4: மெக்காலே 1-வது சட்ட ஆணையம் & 1854 குடிமைப்பணிக் குழுவின் தலைவர். B-3: கானிங் இலாகா முறை & 1861 உயர் நீதிமன்றச் சட்டத்தை அமல்படுத்தினார். C-2: மிண்டோ வகுப்புவாதத் தொகுதியைத் தந்தார். D-1: செம்ஸ்ஃபோர்டு 1919-ல் இரட்டை ஆட்சி & இரு அவைகளைத் தந்தார்.",
        "why_not_others_en": {
            "A-4, B-3, C-2, D-1": "Correct matching of key British administrators to constitutional milestones.",
            "A-3, B-4, C-1, D-2": "Incorrect. Macaulay headed Law Commission (A-4), not High Courts Act.",
            "A-4, B-1, C-2, D-3": "Incorrect. Canning was associated with Portfolio system (B-3), not Montford reforms.",
            "A-2, B-3, C-4, D-1": "Incorrect. Lord Minto was associated with 1909 reforms (C-2)."
        },
        "why_not_others_ta": {
            "A-4, B-3, C-2, D-1": "முக்கிய பிரிட்டிஷ் ஆட்சியாளர்களின் அரசியலமைப்பு சாதனைகளுடன் சரியான பொருத்தம்.",
            "A-3, B-4, C-1, D-2": "தவறு. மெக்காலே சட்ட ஆணையத் தலைவர் (A-4).",
            "A-4, B-1, C-2, D-3": "தவறு. கானிங் இலாகா முறையுடன் தொடர்புடையவர் (B-3).",
            "A-2, B-3, C-4, D-1": "தவறு. மிண்டோ பிரபு 1909 சீர்திருத்தங்களுடன் தொடர்புடையவர் (C-2)."
        },
        "tnpsc_tip_en": "TNPSC Trap: Morley was Secretary of State and Minto was Viceroy in 1909; Montagu was Secretary of State and Chelmsford was Viceroy in 1919.",
        "tnpsc_tip_ta": "TNPSC பொறி: 1909-ல் மார்லி இந்திய அமைச்சர், மிண்டோ வைஸ்ராய்; 1919-ல் மாண்டேகு இந்திய அமைச்சர், செம்ஸ்ஃபோர்டு வைஸ்ராய்.",
        "revision_fact_en": "Lord Canning was both the last Governor-General of EIC and first Viceroy under British Crown.",
        "revision_fact_ta": "கானிங் பிரபு கிழக்கிந்திய நிறுவனத்தின் கடைசி கவர்னர் ஜெனரலாகவும், பிரிட்டிஷ் கிரீடத்தின் முதல் வைஸ்ராயாகவும் இருந்தார்.",
        "bloom_level": "Analyze",
        "tags": ["Polity", "Historical Background", "Lord Macaulay", "Lord Canning", "Lord Minto", "Lord Chelmsford"]
    },
    {
        "id": "HB_MF_013",
        "subject": "Polity",
        "topic": "Historical Background of the Indian Constitution",
        "difficulty": "Hard",
        "question_type": "Match the Following",
        "list_i_en": [
            "Macaulay Committee (1854)",
            "Lee Commission (1923)",
            "Muddiman Committee (1924)",
            "Simon Commission (1927)"
        ],
        "list_i_ta": [
            "மெக்காலே குழு (1854)",
            "லீ ஆணையம் (1923)",
            "முட்டிமேன் குழு (1924)",
            "சைமன் ஆணையம் (1927)"
        ],
        "list_ii_en": [
            "Recommended abolition of Provincial Dyarchy and creation of Responsible Government",
            "Inquired into working of Provincial Dyarchy under Government of India Act 1919",
            "Recommended establishment of Public Service Commission for Superior Civil Services",
            "Framed rules for Open Competitive Examination for Indian Civil Service"
        ],
        "list_ii_ta": [
            "மாகாண இரட்டை ஆட்சியை ஒழித்து பொறுப்புள்ள அரசாங்கத்தை உருவாக்கப் பரிந்துரைத்தது",
            "1919 இந்திய அரசுச் சட்டத்தின் கீழ் மாகாண இரட்டை ஆட்சியின் செயல்பாட்டை ஆராய்ந்தது",
            "உயர் குடிமைப் பணிகளுக்கான பொதுச்சேவை ஆணையத்தை அமைக்கப் பரிந்துரைத்தது",
            "இந்திய குடிமைப் பணிக்கான திறந்தவெளி போட்டித் தேர்வு விதிகளை வகுத்தது"
        ],
        "correct_pairs": {"A": 4, "B": 3, "C": 2, "D": 1}, # A-4, B-3, C-2, D-1
        "distractors": [
            {"A": 3, "B": 4, "C": 1, "D": 2},
            {"A": 4, "B": 2, "C": 3, "D": 1},
            {"A": 1, "B": 3, "C": 2, "D": 4}
        ],
        "explanation_en": "A-4: Macaulay Committee 1854 framed rules for open ICS exam. B-3: Lee Commission 1923 recommended Public Service Commission. C-2: Muddiman Committee 1924 examined working of 1919 Dyarchy. D-1: Simon Commission 1927 recommended abolishing Provincial Dyarchy.",
        "explanation_ta": "A-4: 1854 மெக்காலே குழு போட்டித் தேர்வு விதிகளை வகுத்தது. B-3: 1823 லீ ஆணையம் தேர்வாணையத்தைப் பரிந்துரைத்தது. C-2: 1924 முட்டிமேன் குழு 1919 இரட்டை ஆட்சியை ஆராய்ந்தது. D-1: 1927 சைமன் ஆணையம் இரட்டை ஆட்சியை ஒழிக்கப் பரிந்துரைத்தது.",
        "why_not_others_en": {
            "A-4, B-3, C-2, D-1": "Correct matching of key British Indian committees and commissions.",
            "A-3, B-4, C-1, D-2": "Incorrect. Macaulay committee was for civil services (A-4), not Lee commission.",
            "A-4, B-2, C-3, D-1": "Incorrect. Lee commission was for PSC (B-3), not Dyarchy inquiry.",
            "A-1, B-3, C-2, D-4": "Incorrect. Simon Commission recommended Dyarchy abolition (D-1)."
        },
        "why_not_others_ta": {
            "A-4, B-3, C-2, D-1": "முக்கிய பிரிட்டிஷ் இந்திய குழுக்கள் மற்றும் ஆணையங்களின் சரியான பொருத்தம்.",
            "A-3, B-4, C-1, D-2": "தவறு. மெக்காலே குழு குடிமைப் பணி தேர்வுக்கானது (A-4).",
            "A-4, B-2, C-3, D-1": "தவறு. லீ ஆணையம் தேர்வாணையத்திற்கான பரிந்துரை அளித்தது (B-3).",
            "A-1, B-3, C-2, D-4": "தவறு. சைமன் ஆணையம் இரட்டை ஆட்சி ஒழிப்பை பரிந்துரைத்தது (D-1)."
        },
        "tnpsc_tip_en": "TNPSC Trap: Muddiman Committee (1924) was officially named the Reforms Inquiry Committee.",
        "tnpsc_tip_ta": "TNPSC பொறி: முட்டிமேன் குழு (1924) அதிகாரப்பூர்வமாக 'சீர்திருத்த விசரணைக்குழு' என்று அழைக்கப்பட்டது.",
        "revision_fact_en": "Simon Commission was a 7-member all-white statutory commission officially called Indian Statutory Commission.",
        "revision_fact_ta": "சைமன் ஆணையம் என்பது 7 வெள்ளைக்கார உறுப்பினர்களைக் கொண்ட சட்டப்பூர்வ ஆணையமாகும்.",
        "bloom_level": "Analyze",
        "tags": ["Polity", "Historical Background", "Simon Commission", "Lee Commission", "Macaulay Committee", "Muddiman Committee"]
    },
    {
        "id": "HB_MF_014",
        "subject": "Polity",
        "topic": "Historical Background of the Indian Constitution",
        "difficulty": "Hard",
        "question_type": "Match the Following",
        "list_i_en": [
            "Exemption of GG & Council from Supreme Court jurisdiction",
            "System of Dual Government created via Board of Control",
            "Non-official majority allowed in Provincial Legislative Councils",
            "Instrument of Instructions issued to Governors"
        ],
        "list_i_ta": [
            "உச்ச நீதிமன்ற அதிகார வரம்பிலிருந்து கவர்னர் ஜெனரல் மற்றும் குழுவிற்கு விலக்கு",
            "கட்டுப்பாட்டு வாரியம் மூலம் இரட்டை அரசாங்க முறை உருவாக்கம்",
            "மாகாண சட்ட மேலவைகளில் அரசார்பற்ற உறுப்பினர்களின் பெரும்பான்மை அனுமதி",
            "ஆளுநர்களுக்கு வழங்கப்பட்ட அறிவுறுத்தல் ஆவணம் (Instrument of Instructions)"
        ],
        "list_ii_en": [
            "Government of India Act, 1935",
            "Indian Councils Act, 1909",
            "Pitt's India Act, 1784",
            "Amending Act, 1781"
        ],
        "list_ii_ta": [
            "1935 இந்திய அரசுச் சட்டம்",
            "1909 இந்தியக் குழுக்கள் சட்டம்",
            "1784 பிட் இந்தியச் சட்டம்",
            "1781 திருத்தச் சட்டம்"
        ],
        "correct_pairs": {"A": 4, "B": 3, "C": 2, "D": 1}, # A-4, B-3, C-2, D-1
        "distractors": [
            {"A": 3, "B": 4, "C": 1, "D": 2},
            {"A": 4, "B": 2, "C": 3, "D": 1},
            {"A": 2, "B": 3, "C": 4, "D": 1}
        ],
        "explanation_en": "A-4: 1781 Amending Act exempted GG & Council from SC. B-3: 1784 Pitt's India Act created Dual Government. C-2: 1909 Act allowed non-official majority in provinces (though official majority was retained at Centre). D-1: 1935 Act included Instrument of Instructions (later incorporated as Directive Principles).",
        "explanation_ta": "A-4: 1781 திருத்தச் சட்டம் GG & குழுவுக்கு உச்ச நீதிமன்ற விலக்களித்தது. B-3: 1784 பிட் இந்தியச் சட்டம் இரட்டை அரசை உருவாக்கியது. C-2: 1909 சட்டம் மாகாணங்களில் அரசார்பற்ற பெரும்பான்மையை அனுமதித்தது. D-1: 1935 சட்டம் அறிவுறுத்தல் ஆவணத்தை வழங்கியது (பின்னர் அரசு வழிகாட்டு நெறிமுறைகளாக சேர்க்கப்பட்டது).",
        "why_not_others_en": {
            "A-4, B-3, C-2, D-1": "Correct identification of legal instruments and key structural provisions.",
            "A-3, B-4, C-1, D-2": "Incorrect. SC exemption was 1781 (A-4), not 1784.",
            "A-4, B-2, C-3, D-1": "Incorrect. Dual Govt was 1784 Pitt's India Act (B-3), not 1909.",
            "A-2, B-3, C-4, D-1": "Incorrect. Non-official majority in provinces was 1909 (C-2)."
        },
        "why_not_others_ta": {
            "A-4, B-3, C-2, D-1": "சட்ட ஆவணங்கள் மற்றும் முக்கிய அமைப்பியல் விதிகளின் சரியான பொருத்தம்.",
            "A-3, B-4, C-1, D-2": "தவறு. உச்ச நீதிமன்ற விலக்கு 1781 திருத்தச் சட்டம் (A-4).",
            "A-4, B-2, C-3, D-1": "தவறு. இரட்டை அரசு முறை 1784 பிட் இந்தியச் சட்டம் (B-3).",
            "A-2, B-3, C-4, D-1": "தவறு. மாகாணங்களில் அரசார்பற்ற பெரும்பான்மை 1909 சட்டம் (C-2)."
        },
        "tnpsc_tip_en": "TNPSC Trap: Instrument of Instructions under GOI Act 1935 was adapted into Part IV of Indian Constitution as Directive Principles of State Policy.",
        "tnpsc_tip_ta": "TNPSC பொறி: 1935 அரசுச் சட்டத்தின் 'அறிவுறுத்தல் ஆவணம்' இந்திய அரசியலமைப்பின் பகுதி IV-ல் அரசு வழிகாட்டு நெறிமுறைகளாகச் சேர்க்கப்பட்டது.",
        "revision_fact_en": "Indian Councils Act 1909 maintained official majority in Central Legislative Council but allowed non-official majority in provincial councils.",
        "revision_fact_ta": "1909 இந்தியக் குழுக்கள் சட்டம் மத்திய மேலவையில் அரசு உறுப்பினர்களின் பெரும்பான்மையைத் தக்கவைத்து மாகாணங்களில் அரசார்பற்ற பெரும்பான்மையை அனுமதித்தது.",
        "bloom_level": "Analyze",
        "tags": ["Polity", "Historical Background", "Instrument of Instructions", "DPSP Origin", "Act of Settlement"]
    },
    {
        "id": "HB_MF_015",
        "subject": "Polity",
        "topic": "Historical Background of the Indian Constitution",
        "difficulty": "Hard",
        "question_type": "Match the Following",
        "list_i_en": [
            "Governor-General of Bengal",
            "Governor-General of India",
            "Viceroy of India",
            "Governor-General of Independent Dominion of India"
        ],
        "list_i_ta": [
            "வங்காள கவர்னர் ஜெனரல்",
            "இந்திய கவர்னர் ஜெனரல்",
            "இந்திய வைஸ்ராய்",
            "சுதந்திர இந்திய டொமினியனின் கவர்னர் ஜெனரல்"
        ],
        "list_ii_en": [
            "Indian Independence Act, 1947",
            "Government of India Act, 1858",
            "Charter Act, 1833",
            "Regulating Act, 1773"
        ],
        "list_ii_ta": [
            "1947 இந்திய சுதந்திரச் சட்டம்",
            "1858 இந்திய அரசுச் சட்டம்",
            "1833 சாசனச் சட்டம்",
            "1773 ஒழுங்குமுறைச் சட்டம்"
        ],
        "correct_pairs": {"A": 4, "B": 3, "C": 2, "D": 1}, # A-4, B-3, C-2, D-1
        "distractors": [
            {"A": 3, "B": 4, "C": 1, "D": 2},
            {"A": 4, "B": 1, "C": 2, "D": 3},
            {"A": 2, "B": 3, "C": 4, "D": 1}
        ],
        "explanation_en": "A-4: 1773 Regulating Act created Governor-General of Bengal (Warren Hastings). B-3: 1833 Charter Act created Governor-General of India (Lord William Bentinck). C-2: 1858 GOI Act designated him as Viceroy of India (Lord Canning). D-1: 1947 Independence Act reconstituted office as Governor-General of India (Lord Mountbatten / C. Rajagopalachari).",
        "explanation_ta": "A-4: 1773 ஒழுங்குமுறைச் சட்டம் வங்காள கவர்னர் ஜெனரலை உருவாக்கியது (வாரன் ஹேஸ்டிங்ஸ்). B-3: 1833 சாசனச் சட்டம் இந்திய கவர்னர் ஜெனரலை உருவாக்கியது (வில்லியம் பென்டிங்க்). C-2: 1858 அரசுச் சட்டம் அவரை வைஸ்ராய் என மாற்றியது (கானிங் பிரபு). D-1: 1947 சுதந்திரச் சட்டம் சுதந்திர இந்திய கவர்னர் ஜெனரல் பதவியை தந்தது (மவுண்ட்பேட்டன் / சி. ராஜகோபாலாச்சாரி).",
        "why_not_others_en": {
            "A-4, B-3, C-2, D-1": "Correct matching of designation evolution of the executive head of India.",
            "A-3, B-4, C-1, D-2": "Incorrect. Governor-General of Bengal was created in 1773 (A-4), not 1833.",
            "A-4, B-1, C-2, D-3": "Incorrect. Governor-General of India was created in 1833 (B-3).",
            "A-2, B-3, C-4, D-1": "Incorrect. Viceroy title was adopted in 1858 (C-2)."
        },
        "why_not_others_ta": {
            "A-4, B-3, C-2, D-1": "இந்திய நிர்வாகத் தலைவரின் பதவிப் பெயர் மாற்றங்களின் சரியான பொருத்தம்.",
            "A-3, B-4, C-1, D-2": "தவறு. வங்காள கவர்னர் ஜெனரல் 1773-ல் உருவாக்கப்பட்டது (A-4).",
            "A-4, B-1, C-2, D-3": "தவறு. இந்திய கவர்னர் ஜெனரல் 1833-ல் உருவாக்கப்பட்டது (B-3).",
            "A-2, B-3, C-4, D-1": "தவறு. வைஸ்ராய் பட்டம் 1858-ல் ஏற்றுக்கொள்ளப்பட்டது (C-2)."
        },
        "tnpsc_tip_en": "TNPSC Trap: Lord William Bentinck was 1st GG of India (1833); Lord Mountbatten was 1st GG of Independent India; C. Rajagopalachari was 1st and last Indian GG of India.",
        "tnpsc_tip_ta": "TNPSC பொறி: வில்லியம் பென்டிங்க் இந்தியாவின் முதல் கவர்னர் ஜெனரல் (1833); மவுண்ட்பேட்டன் சுதந்திர இந்தியாவின் முதல் கவர்னர் ஜெனரல்; சி. ராஜகோபாலாச்சாரி முதல் மற்றும் கடைசி இந்திய கவர்னர் ஜெனரல்.",
        "revision_fact_en": "1947 Independence Act made Governor-General a constitutional head acting on advice of Council of Ministers.",
        "revision_fact_ta": "1947 சுதந்திரச் சட்டம் கவர்னர் ஜெனரலை அமைச்சரவையின் ஆலோசனையின்படி செயல்படும் அரசியலமைப்புத் தலைவராக்கியது.",
        "bloom_level": "Analyze",
        "tags": ["Polity", "Historical Background", "Governor-General", "Viceroy", "Lord Mountbatten", "C Rajagopalachari"]
    },
    {
        "id": "HB_MF_016",
        "subject": "Polity",
        "topic": "Historical Background of the Indian Constitution",
        "difficulty": "Hard",
        "question_type": "Match the Following",
        "list_i_en": [
            "Central Legislative Council established with 6 legislative members",
            "Bicameralism at Centre (Council of State & Central Legislative Assembly)",
            "Bicameralism in 6 out of 11 Provinces",
            "Constituent Assembly becoming Sovereign Central Legislature"
        ],
        "list_i_ta": [
            "6 சட்ட உறுப்பினர்களுடன் மத்திய சட்ட மேலவை அமைக்கப்பட்டது",
            "மத்தியில் இரு அவைகள் (மாநிலங்கள் அவை & மத்திய சட்டமன்றம்)",
            "11 மாகாணங்களில் 6 மாகாணங்களில் இரு அவைகள் அறிமுகம்",
            "அரசியலமைப்பு நிர்ணய சபை இறையாண்மை மிக்க சட்டமன்றமாக மாறுதல்"
        ],
        "list_ii_en": [
            "Indian Independence Act, 1947",
            "Government of India Act, 1935",
            "Government of India Act, 1919",
            "Charter Act, 1853"
        ],
        "list_ii_ta": [
            "1947 இந்திய சுதந்திரச் சட்டம்",
            "1935 இந்திய அரசுச் சட்டம்",
            "1919 இந்திய அரசுச் சட்டம்",
            "1853 சாசனச் சட்டம்"
        ],
        "correct_pairs": {"A": 4, "B": 3, "C": 2, "D": 1}, # A-4, B-3, C-2, D-1
        "distractors": [
            {"A": 3, "B": 4, "C": 1, "D": 2},
            {"A": 4, "B": 2, "C": 3, "D": 1},
            {"A": 1, "B": 3, "C": 2, "D": 4}
        ],
        "explanation_en": "A-4: Charter Act 1853 created 1st Central Legislative Council. B-3: GOI Act 1919 introduced Central Bicameralism. C-2: GOI Act 1935 introduced Provincial Bicameralism in 6 provinces (Bengal, Bombay, Madras, UP, Bihar, Assam). D-1: 1947 Independence Act conferred sovereign legislative status on Constituent Assembly.",
        "explanation_ta": "A-4: 1853 சாசனச் சட்டம் 1-வது மத்திய சட்ட மேலவையை உருவாக்கியது. B-3: 1919 அரசுச் சட்டம் மத்திய இரு அவைகளை அறிமுகப்படுத்தியது. C-2: 1935 அரசுச் சட்டம் 6 மாகாணங்களில் இரு அவைகளை அறிமுகப்படுத்தியது. D-1: 1947 சுதந்திரச் சட்டம் நிர்ணய சபைக்கு இறையாண்மை சட்ட அதிகாரத்தை தந்தது.",
        "why_not_others_en": {
            "A-4, B-3, C-2, D-1": "Correct matching of legislative architectural evolution.",
            "A-3, B-4, C-1, D-2": "Incorrect. Central Legislative Council was 1853 (A-4), not 1919.",
            "A-4, B-2, C-3, D-1": "Incorrect. Central bicameralism was introduced in 1919 (B-3), not 1935.",
            "A-1, B-3, C-2, D-4": "Incorrect. Sovereign Constituent Assembly status was 1947 (D-1)."
        },
        "why_not_others_ta": {
            "A-4, B-3, C-2, D-1": "சட்டமன்ற அமைப்பியல் பரிணாமத்தின் சரியான பொருத்தம்.",
            "A-3, B-4, C-1, D-2": "தவறு. மத்திய சட்ட மேலவை 1853 சாசனச் சட்டம் (A-4).",
            "A-4, B-2, C-3, D-1": "தவறு. மத்திய இரு அவைகள் 1919-ல் அறிமுகப்படுத்தப்பட்டன (B-3).",
            "A-1, B-3, C-2, D-4": "தவறு. இறையாண்மை சட்டமன்ற அந்தஸ்து 1947-ல் பெறப்பட்டது (D-1)."
        },
        "tnpsc_tip_en": "TNPSC Trap: Bicameralism at Centre was introduced in 1919 (Council of State + Legislative Assembly); Bicameralism in Provinces was introduced in 1935 (6 provinces).",
        "tnpsc_tip_ta": "TNPSC பொறி: மத்தியில் இரு அவைகள் 1919-ல் அறிமுகப்படுத்தப்பட்டன; மாகாணங்களில் இரு அவைகள் 1935-ல் 6 மாகாணங்களில் அறிமுகப்படுத்தப்பட்டன.",
        "revision_fact_en": "The six bicameral provinces under 1935 Act were Bengal, Bombay, Madras, United Provinces, Bihar, and Assam.",
        "revision_fact_ta": "1935 சட்டத்தின்கீழ் இரு அவைகளைக் கொண்ட 6 மாகாணங்கள்: வங்காளம், பம்பாய், மெட்ராஸ், ஐக்கிய மாகாணம், பீகார் மற்றும் அசாம்.",
        "bloom_level": "Analyze",
        "tags": ["Polity", "Historical Background", "Bicameralism", "Constituent Assembly", "Charter Act 1853"]
    },
    {
        "id": "HB_MF_017",
        "subject": "Polity",
        "topic": "Historical Background of the Indian Constitution",
        "difficulty": "Hard",
        "question_type": "Match the Following",
        "list_i_en": [
            "Power of GG to override council in defense and peace",
            "Viceroy empowered to issue Ordinances during emergency",
            "Governor empowered to assume full administration under Section 93",
            "Devolution of subject matters into Central and Provincial Lists"
        ],
        "list_i_ta": [
            "பாதுகாப்பு மற்றும் அமைதி விவகாரங்களில் குழுவை நிராகரிக்க கவர்னர் ஜெனரலுக்கு அதிகாரம்",
            "அவசர காலத்தில் அவசரச் சட்டங்களை பிறப்பிக்க வைஸ்ராய்க்கு அதிகாரம்",
            "பிரிவு 93-ன் கீழ் முழு நிர்வாகத்தையும் ஏற்க ஆளுநருக்கு அதிகாரம்",
            "மத்திய மற்றும் மாகாணப் பட்டியல்களாகப் பாடங்களை பிரித்து ஒப்படைத்தல்"
        ],
        "list_ii_en": [
            "Government of India Act, 1935",
            "Government of India Act, 1919",
            "Indian Councils Act, 1861",
            "Charter Act, 1786 (Amending Act)"
        ],
        "list_ii_ta": [
            "1935 இந்திய அரசுச் சட்டம்",
            "1919 இந்திய அரசுச் சட்டம்",
            "1861 இந்தியக் குழுக்கள் சட்டம்",
            "1786 சாசனச் சட்டம் (திருத்தச் சட்டம்)"
        ],
        "correct_pairs": {"A": 4, "B": 3, "C": 1, "D": 2}, # A-4, B-3, C-1, D-2
        "distractors": [
            {"A": 3, "B": 4, "C": 2, "D": 1},
            {"A": 4, "B": 1, "C": 3, "D": 2},
            {"A": 2, "B": 3, "C": 1, "D": 4}
        ],
        "explanation_en": "A-4: Charter Act 1786 gave Cornwallis overriding power over council. B-3: 1861 Act gave Ordinance power to Viceroy. C-1: GOI Act 1935 Section 93 provided Governor's Emergency Powers in provinces. D-2: GOI Act 1919 demarcated Central and Provincial subject rules.",
        "explanation_ta": "A-4: 1786 சாசனச் சட்டம் காரன்வாலிஸுக்கு நிராகரிப்பு அதிகாரம் அளித்தது. B-3: 1861 சட்டம் வைஸ்ராய்க்கு அவசரச்சட்ட அதிகாரம் தந்தது. C-1: 1935 சட்டம் பிரிவு 93-ன் கீழ் ஆளுநர் அவசரகால அதிகாரத்தை தந்தது. D-2: 1919 சட்டம் மத்திய மற்றும் மாகாணப் பட்டியல்களைப் பிரித்தது.",
        "why_not_others_en": {
            "A-4, B-3, C-1, D-2": "Correct matching of emergency, executive override, and subject rules.",
            "A-3, B-4, C-2, D-1": "Incorrect. Overriding power was created in 1786 (A-4) for Lord Cornwallis.",
            "A-4, B-1, C-3, D-2": "Incorrect. Ordinance power was 1861 (B-3), not 1935.",
            "A-2, B-3, C-1, D-4": "Incorrect. Section 93 Governor rule was in 1935 Act (C-1)."
        },
        "why_not_others_ta": {
            "A-4, B-3, C-1, D-2": "அவசரகாலம், நிர்வாக நிராகரிப்பு அதிகாரம் மற்றும் பாடப்பிரிவுகளின் சரியான பொருத்தம்.",
            "A-3, B-4, C-2, D-1": "தவறு. நிராகரிப்பு அதிகாரம் காரன்வாலிஸுக்காக 1786-ல் உருவாக்கப்பட்டது (A-4).",
            "A-4, B-1, C-3, D-2": "தவறு. அவசரச்சட்ட அதிகாரம் 1861 சட்டம் (B-3).",
            "A-2, B-3, C-1, D-4": "தவறு. பிரிவு 93 ஆளுநர் ஆட்சி 1935 சட்டத்தில் இருந்தது (C-1)."
        },
        "tnpsc_tip_en": "TNPSC Trap: Lord Cornwallis demanded overriding power over council as a precondition to accept post of Governor-General in 1786.",
        "tnpsc_tip_ta": "TNPSC பொறி: 1786-ல் காரன்வாலிஸ் பிரபு கவர்னர் ஜெனரல் பதவியை ஏற்க குழுவை நிராகரிக்கும் அதிகாரத்தை முன்நிபந்தனையாகக் கேட்டார்.",
        "revision_fact_en": "Section 93 of GOI Act 1935 is the historical predecessor of Article 356 (President's Rule) in Indian Constitution.",
        "revision_fact_ta": "1935 இந்திய அரசுச் சட்டத்தின் பிரிவு 93 என்பது இந்திய அரசியலமைப்பின் 356 வது பிரிவின் (குடியரசுத் தலைவர் ஆட்சி) வரலாற்று முன்னோடியாகும்.",
        "bloom_level": "Analyze",
        "tags": ["Polity", "Historical Background", "Ordinance Power", "Section 93", "Article 356 Origin"]
    },
    {
        "id": "HB_MF_018",
        "subject": "Polity",
        "topic": "Historical Background of the Indian Constitution",
        "difficulty": "Hard",
        "question_type": "Match the Following",
        "list_i_en": [
            "Board of Control veto over Court of Directors political despatches",
            "Imperial veto & reservation power of Viceroy over bills",
            "Governor's Certification power to enact bills rejected by legislature",
            "Governor-General power to reserve bills for His Majesty's pleasure"
        ],
        "list_i_ta": [
            "இயக்குநர்கள் அவையின் அரசியல் கோப்புகள் மீது கட்டுப்பாட்டு வாரியத்தின் வீட்டோ அதிகாரம்",
            "சட்டமுன்வடிவுகள் மீது வைஸ்ராயின் ரத்து அதிகாரம் மற்றும் இடஒதுக்கீடு அதிகாரம்",
            "சட்டமன்றத்தால் நிராகரிக்கப்பட்ட சட்டங்களை நிறைவேற்ற ஆளுநரின் சான்றளிப்பு அதிகாரம்",
            "மன்னரின் பரிசீலனைக்காக சட்டமுன்வடிவுகளை ஒதுக்கி வைக்கும் கவர்னர் ஜெனரல் அதிகாரம்"
        ],
        "list_ii_en": [
            "Government of India Act, 1935",
            "Government of India Act, 1919",
            "Indian Councils Act, 1861",
            "Pitt's India Act, 1784"
        ],
        "list_ii_ta": [
            "1935 இந்திய அரசுச் சட்டம்",
            "1919 இந்திய அரசுச் சட்டம்",
            "1861 இந்தியக் குழுக்கள் சட்டம்",
            "1784 பிட் இந்தியச் சட்டம்"
        ],
        "correct_pairs": {"A": 4, "B": 3, "C": 2, "D": 1}, # A-4, B-3, C-2, D-1
        "distractors": [
            {"A": 3, "B": 4, "C": 1, "D": 2},
            {"A": 4, "B": 2, "C": 3, "D": 1},
            {"A": 2, "B": 3, "C": 4, "D": 1}
        ],
        "explanation_en": "A-4: 1784 Act gave Board of Control veto over Directors despatches. B-3: 1861 Act gave Viceroy veto power over legislative bills. C-2: 1919 Act gave Governor certification power to override provincial assembly rejection. D-1: 1935 Act empowered GG to reserve bills for Crown pleasure.",
        "explanation_ta": "A-4: 1784 சட்டம் கட்டுப்பாட்டு வாரியத்திற்கு வீட்டோ அதிகாரம் தந்தது. B-3: 1861 சட்டம் வைஸ்ராய்க்கு சட்ட ரத்து அதிகாரம் தந்தது. C-2: 1919 சட்டம் ஆளுநருக்கு சான்றளிப்பு அதிகாரம் தந்தது. D-1: 1935 சட்டம் மன்னரின் ஒப்புதலுக்கு சட்டங்களை ஒதுக்கி வைக்கும் அதிகாரம் தந்தது.",
        "why_not_others_en": {
            "A-4, B-3, C-2, D-1": "Correct matching of veto and prerogative mechanics across acts.",
            "A-3, B-4, C-1, D-2": "Incorrect. Board of Control veto was 1784 (A-4).",
            "A-4, B-2, C-3, D-1": "Incorrect. Viceroy veto over legislative bills was introduced in 1861 (B-3).",
            "A-2, B-3, C-4, D-1": "Incorrect. Governor Certification was feature of 1919 Act (C-2)."
        },
        "why_not_others_ta": {
            "A-4, B-3, C-2, D-1": "சட்டச் சட்டங்களில் வீட்டோ மற்றும் சிறப்பு அதிகார முறைகளின் சரியான பொருத்தம்.",
            "A-3, B-4, C-1, D-2": "தவறு. கட்டுப்பாட்டு வாரிய வீட்டோ அதிகாரம் 1784 (A-4).",
            "A-4, B-2, C-3, D-1": "தவறு. வைஸ்ராய் சட்ட ரத்து அதிகாரம் 1861-ல் அறிமுகமானது (B-3).",
            "A-2, B-3, C-4, D-1": "தவறு. ஆளுநர் சான்றளிப்பு அதிகாரம் 1919 சட்ட அம்சம் (C-2)."
        },
        "tnpsc_tip_en": "TNPSC Trap: Governor's power to reserve bills for President under Article 200 of Indian Constitution originates from GOI Act 1935.",
        "tnpsc_tip_ta": "TNPSC பொறி: அரசியலமைப்பின் 200வது பிரிவின் கீழ் குடியரசுத் தலைவருக்கு ஆளுநர் மசோதாவை ஒதுக்கி வைக்கும் அதிகாரம் 1935 அரசுச் சட்டத்திலிருந்து வந்தது.",
        "revision_fact_en": "Certification allowed the Governor to enact any bill deemed essential for peace or tranquility even if rejected by Provincial Legislature.",
        "revision_fact_ta": "சான்றளிப்பு அதிகாரம் என்பது சட்டமன்றம் நிராகரித்தாலும் அமைதிக்குத் தேவையான மசோதாவை ஆளுநர் நிறைவேற்ற அனுமதித்தது.",
        "bloom_level": "Analyze",
        "tags": ["Polity", "Historical Background", "Veto Power", "Certification Power", "Article 200 Origin"]
    },
    {
        "id": "HB_MF_019",
        "subject": "Polity",
        "topic": "Historical Background of the Indian Constitution",
        "difficulty": "Hard",
        "question_type": "Match the Following",
        "list_i_en": [
            "Supreme Council of 4 members to assist GG Bengal",
            "Council of India (15 members based in London)",
            "Consultative Select Committees of Councils for advice",
            "Chamber of Princes (Narendra Mandal) for native states"
        ],
        "list_i_ta": [
            "வங்காள GG-க்கு உதவ 4 உறுப்பினர்களைக் கொண்ட உச்சக் குழு",
            "இந்தியக் குழு (லண்டனில் 15 உறுப்பினர்கள்)",
            "ஆலோசனை வழங்க சட்ட மன்றங்களின் தேர்வுக் குழுக்கள்",
            "சுதேச சமஸ்தானங்களுக்கான இளவரசர்கள் அவை (நரேந்திர மண்டல்)"
        ],
        "list_ii_en": [
            "Royal Proclamation / Government of India Act, 1919",
            "Indian Councils Act, 1909",
            "Government of India Act, 1858",
            "Regulating Act, 1773"
        ],
        "list_ii_ta": [
            "அரசப் பிரகடனம் / 1919 இந்திய அரசுச் சட்டம்",
            "1909 இந்தியக் குழுக்கள் சட்டம்",
            "1858 இந்திய அரசுச் சட்டம்",
            "1773 ஒழுங்குமுறைச் சட்டம்"
        ],
        "correct_pairs": {"A": 4, "B": 3, "C": 2, "D": 1}, # A-4, B-3, C-2, D-1
        "distractors": [
            {"A": 3, "B": 4, "C": 1, "D": 2},
            {"A": 4, "B": 2, "C": 3, "D": 1},
            {"A": 1, "B": 3, "C": 2, "D": 4}
        ],
        "explanation_en": "A-4: 1773 Regulating Act established 4-member executive council for Bengal. B-3: 1858 GOI Act created 15-member Council of India. C-2: 1909 Act introduced select/consultative committees. D-1: Chamber of Princes was established in 1921 following 1919 Montford reforms.",
        "explanation_ta": "A-4: 1773 சட்டம் 4 உறுப்பினர் நிர்வாகக் குழுவை அமைத்தது. B-3: 1858 சட்டம் 15 உறுப்பினர் இந்தியக் குழுவை அமைத்தது. C-2: 1909 சட்டம் ஆலோசனைக் குழுக்களை அறிமுகப்படுத்தியது. D-1: 1919 சீர்திருத்தங்களைத் தொடர்ந்து 1921-ல் இளவரசர்கள் அவை (நரேந்திர மண்டல்) அமைக்கப்பட்டது.",
        "why_not_others_en": {
            "A-4, B-3, C-2, D-1": "Correct matching of statutory consultative and advisory institutions.",
            "A-3, B-4, C-1, D-2": "Incorrect. Executive council of 4 members was 1773 (A-4).",
            "A-4, B-2, C-3, D-1": "Incorrect. Council of India (London) was 1858 (B-3), not 1909.",
            "A-1, B-3, C-2, D-4": "Incorrect. Chamber of Princes was outcome of 1919 reforms (D-1)."
        },
        "why_not_others_ta": {
            "A-4, B-3, C-2, D-1": "சட்டப்பூர்வ ஆலோசனை நிறுவனங்களின் சரியான பொருத்தம்.",
            "A-3, B-4, C-1, D-2": "தவறு. 4 உறுப்பினர் நிர்வாகக் குழு 1773 சட்டம் (A-4).",
            "A-4, B-2, C-3, D-1": "தவறு. இந்தியக் குழு (லண்டன்) 1858 சட்டம் (B-3).",
            "A-1, B-3, C-2, D-4": "தவறு. இளவரசர்கள் அவை 1919 சீர்திருத்தத்தின் முடிவு (D-1)."
        },
        "tnpsc_tip_en": "TNPSC Trap: Chamber of Princes (Narendra Mandal) was formally inaugurated in 1921 by Duke of Connaught.",
        "tnpsc_tip_ta": "TNPSC பொறி: இளவரசர்கள் அவை (நரேந்திர மண்டல்) 1921-ல் கோனாட் பிரபுவால் அதிகாரப்பூர்வமாகத் தொடங்கி வைக்கப்பட்டது.",
        "revision_fact_en": "Council of India created under 1858 Act was an advisory body chaired by Secretary of State for India.",
        "revision_fact_ta": "1858 சட்டத்தின்கீழ் உருவாக்கப்பட்ட இந்தியக் குழு என்பது இந்திய அமைச்சரால் தலைமை தாங்கப்பட்ட ஓர் ஆலோசனைக் குழுவாகும்.",
        "bloom_level": "Analyze",
        "tags": ["Polity", "Historical Background", "Narendra Mandal", "Council of India", "Executive Council 1773"]
    },
    {
        "id": "HB_MF_020",
        "subject": "Polity",
        "topic": "Historical Background of the Indian Constitution",
        "difficulty": "Hard",
        "question_type": "Match the Following",
        "list_i_en": [
            "\"Act for the Better Government of India\"",
            "\"Act of Settlement\"",
            "\"First Step towards Representative Institutions\"",
            "\"Structural Blueprint of the Indian Constitution\""
        ],
        "list_i_ta": [
            "\"இந்தியாவின் சிறந்த நிர்வாகத்திற்கான சட்டம்\"",
            "\"சீரமைப்புச் சட்டம் (Act of Settlement)\"",
            "\"பிரதிநிதித்துவ நிறுவனங்களை நோக்கிய முதல் படி\"",
            "\"இந்திய அரசியலமைப்பின் அமைப்பியல் வரைபடம்\""
        ],
        "list_ii_en": [
            "Government of India Act, 1935",
            "Indian Councils Act, 1861",
            "Amending Act, 1781",
            "Government of India Act, 1858"
        ],
        "list_ii_ta": [
            "1935 இந்திய அரசுச் சட்டம்",
            "1861 இந்தியக் குழுக்கள் சட்டம்",
            "1781 திருத்தச் சட்டம்",
            "1858 இந்திய அரசுச் சட்டம்"
        ],
        "correct_pairs": {"A": 4, "B": 3, "C": 2, "D": 1}, # A-4, B-3, C-2, D-1
        "distractors": [
            {"A": 3, "B": 4, "C": 1, "D": 2},
            {"A": 4, "B": 2, "C": 3, "D": 1},
            {"A": 1, "B": 3, "C": 2, "D": 4}
        ],
        "explanation_en": "A-4: GOI Act 1858 was officially titled 'Act for the Better Government of India'. B-3: 1781 Amending Act was known as 'Act of Settlement'. C-2: 1861 Act is called 'First step towards representative institutions' by associating Indians in law-making. D-1: GOI Act 1935 is called the 'Structural Blueprint' of 1950 Constitution.",
        "explanation_ta": "A-4: 1858 அரசுச் சட்டம் 'இந்தியாவின் சிறந்த நிர்வாகத்திற்கான சட்டம்' எனப்பட்டது. B-3: 1781 திருத்தச் சட்டம் 'சீரமைப்புச் சட்டம்' எனப்பட்டது. C-2: 1861 சட்டம் 'பிரதிநிதித்துவ நிறுவனங்களின் முதல் படி' எனப்பட்டது. D-1: 1935 அரசுச் சட்டம் 1950 அரசியலமைப்பின் 'அமைப்பியல் வரைபடம்' எனப்படுகிறது.",
        "why_not_others_en": {
            "A-4, B-3, C-2, D-1": "Correct matching of official titles and historical epithets of constitutional acts.",
            "A-3, B-4, C-1, D-2": "Incorrect. Better Govt Act was 1858 (A-4), not 1781.",
            "A-4, B-2, C-3, D-1": "Incorrect. Act of Settlement was 1781 (B-3), not 1861.",
            "A-1, B-3, C-2, D-4": "Incorrect. Blueprint of Constitution refers to 1935 Act (D-1)."
        },
        "why_not_others_ta": {
            "A-4, B-3, C-2, D-1": "சட்டப்பூர்வ தலைப்புகள் மற்றும் வரலாற்றுப் பட்டப் பெயர்களின் சரியான பொருத்தம்.",
            "A-3, B-4, C-1, D-2": "தவறு. சிறந்த நிர்வாகச் சட்டம் 1858 (A-4).",
            "A-4, B-2, C-3, D-1": "தவறு. சீரமைப்புச் சட்டம் 1781 (B-3).",
            "A-1, B-3, C-2, D-4": "தவறு. அரசியலமைப்பின் அமைப்பியல் வரைபடம் 1935 சட்டம் (D-1)."
        },
        "tnpsc_tip_en": "TNPSC Trap: Nearly 75% of the content/structure of the 1950 Indian Constitution was directly drawn from the GOI Act 1935.",
        "tnpsc_tip_ta": "TNPSC பொறி: 1950 இந்திய அரசியலமைப்பின் கிட்டத்தட்ட 75% கருத்துக்கள்/அமைப்பு 1935 அரசுச் சட்டத்தில் இருந்து பெறப்பட்டது.",
        "revision_fact_en": "Indian Councils Act 1861 nominated 3 Indians (Raja of Benaras, Maharaja of Patiala, Sir Dinkar Rao) to Legislative Council.",
        "revision_fact_ta": "1861 இந்தியக் குழுக்கள் சட்டம் 3 இந்தியர்களை (பெனாரஸ் ராஜா, பட்டியாலா மகாராஜா, சர் தினகர் ராவ்) சட்ட மேலவைக்கு நியமித்தது.",
        "bloom_level": "Evaluate",
        "tags": ["Polity", "Historical Background", "Act of Settlement 1781", "GOI Act 1858", "GOI Act 1935"]
    },

    # ------------------ Group 3: Comparative Matching (5 Questions) ------------------
    {
        "id": "HB_MF_021",
        "subject": "Polity",
        "topic": "Historical Background of the Indian Constitution",
        "difficulty": "Hard",
        "question_type": "Match the Following",
        "list_i_en": [
            "Regulating Act, 1773 Executive Council",
            "Pitt's India Act, 1784 Executive Council",
            "Charter Act, 1833 Executive Council",
            "Charter Act, 1853 Council Expansion"
        ],
        "list_i_ta": [
            "1773 ஒழுங்குமுறைச் சட்ட நிர்வாகக் குழு",
            "1784 பிட் இந்தியச் சட்ட நிர்வாகக் குழு",
            "1833 சாசனச் சட்ட நிர்வாகக் குழு",
            "1853 சாசனச் சட்டக் குழு விரிவாக்கம்"
        ],
        "list_ii_en": [
            "Added 6 Legislative Members forming Central Legislative Council",
            "Added 4th Law Member (Lord Macaulay) without voting right in executive business",
            "Reduced membership from 4 to 3 including Commander-in-Chief",
            "Created 4-member Executive Council with decisions taken by majority vote"
        ],
        "list_ii_ta": [
            "மத்திய சட்ட மேலவையை உருவாக்கி 6 சட்ட உறுப்பினர்களைச் சேர்த்தது",
            "நிர்வாகத்தில் வாக்களிக்கும் உரிமையின்றி 4-வது சட்ட உறுப்பினரைச் (மெக்காலே) சேர்த்தது",
            "தளபதி உட்பட உறுப்பினர்களின் எண்ணிக்கையை 4-லிருந்து 3 ஆகக் குறைத்தது",
            "பெரும்பான்மை வாக்களிப்புடன் கூடிய 4 உறுப்பினர் நிர்வாகக் குழுவை அமைத்தது"
        ],
        "correct_pairs": {"A": 4, "B": 3, "C": 2, "D": 1}, # A-4, B-3, C-2, D-1
        "distractors": [
            {"A": 3, "B": 4, "C": 1, "D": 2},
            {"A": 4, "B": 2, "C": 3, "D": 1},
            {"A": 2, "B": 3, "C": 4, "D": 1}
        ],
        "explanation_en": "A-4: 1773 created 4-member council. B-3: 1784 reduced council size to 3 to enhance GG authority. C-2: 1833 added 4th Law Member (Macaulay). D-1: 1853 added 6 legislative members creating Central Legislative Council.",
        "explanation_ta": "A-4: 1773 சட்டம் 4 உறுப்பினர் குழுவை அமைத்தது. B-3: 1784 சட்டம் குழுவை 3 ஆகக் குறைத்தது. C-2: 1833 சட்டம் 4வது சட்ட உறுப்பினரைச் சேர்த்தது. D-1: 1853 சட்டம் 6 சட்ட உறுப்பினர்களைச் சேர்த்தது.",
        "why_not_others_en": {
            "A-4, B-3, C-2, D-1": "Correct comparative matching of Executive Council membership numerical changes.",
            "A-3, B-4, C-1, D-2": "Incorrect. 1773 council was 4 members (A-4), not 3.",
            "A-4, B-2, C-3, D-1": "Incorrect. 1784 Act reduced council to 3 (B-3), not Law member addition.",
            "A-2, B-3, C-4, D-1": "Incorrect. Law member addition was in 1833 (C-2)."
        },
        "why_not_others_ta": {
            "A-4, B-3, C-2, D-1": "நிர்வாகக் குழு உறுப்பினர் எண்ணிக்கை மாற்றங்களின் ஒப்பீட்டுப் பொருத்தம்.",
            "A-3, B-4, C-1, D-2": "தவறு. 1773 குழு 4 உறுப்பினர்களைக் கொண்டது (A-4).",
            "A-4, B-2, C-3, D-1": "தவறு. 1784 சட்டம் குழுவை 3 ஆகக் குறைத்தது (B-3).",
            "A-2, B-3, C-4, D-1": "தவறு. சட்ட உறுப்பினர் சேர்க்கை 1833 சாசனச் சட்டம் (C-2)."
        },
        "tnpsc_tip_en": "TNPSC Trap: The 4th Law member (1833) became a FULL member of the Executive Council under Charter Act 1853.",
        "tnpsc_tip_ta": "TNPSC பொறி: 4-வது சட்ட உறுப்பினர் (1833) 1853 சாசனச் சட்டத்தின் கீழ் நிர்வாகக் குழுவின் முழு உறுப்பினரானார்.",
        "revision_fact_en": "Commander-in-Chief was made one of the 3 council members under Pitt's India Act 1784.",
        "revision_fact_ta": "1784 பிட் இந்தியச் சட்டத்தின் கீழ் தலைமைத் தளபதி 3 குழு உறுப்பினர்களில் ஒருவராக்கப்பட்டார்.",
        "bloom_level": "Analyze",
        "tags": ["Polity", "Historical Background", "Executive Council", "Charter Act 1833", "Charter Act 1853"]
    },
    {
        "id": "HB_MF_022",
        "subject": "Polity",
        "topic": "Historical Background of the Indian Constitution",
        "difficulty": "Hard",
        "question_type": "Match the Following",
        "list_i_en": [
            "Reporting civil & revenue affairs to British Treasury",
            "Segregation of Commercial & Political functions",
            "Abolition of EIC trade monopoly except Tea & China trade",
            "EIC transformed into pure administrative trustee"
        ],
        "list_i_ta": [
            "பிரிட்டிஷ் கருவூலத்திற்கு சிவில் & வருவாய் விவகாரங்களை அறிக்கையிடுதல்",
            "வர்த்தக மற்றும் அரசியல் பணிகளைப் பிரித்தல்",
            "தேயிலை & சீனா வர்த்தகம் தவிர ஏகபோகத்தை ஒழித்தல்",
            "நிறுவனம் தூய நிர்வாக டிரஸ்டியாக மாற்றப்படுதல்"
        ],
        "list_ii_en": [
            "Charter Act, 1833",
            "Charter Act, 1813",
            "Pitt's India Act, 1784",
            "Regulating Act, 1773"
        ],
        "list_ii_ta": [
            "1833 சாசனச் சட்டம்",
            "1813 சாசனச் சட்டம்",
            "1784 பிட் இந்தியச் சட்டம்",
            "1773 ஒழுங்குமுறைச் சட்டம்"
        ],
        "correct_pairs": {"A": 4, "B": 3, "C": 2, "D": 1}, # A-4, B-3, C-2, D-1
        "distractors": [
            {"A": 3, "B": 4, "C": 1, "D": 2},
            {"A": 4, "B": 2, "C": 3, "D": 1},
            {"A": 1, "B": 3, "C": 2, "D": 4}
        ],
        "explanation_en": "A-4: 1773 Act made EIC directors submit revenue despatches to British Treasury. B-3: 1784 Act segregated commercial (Directors) and political (Board of Control). C-2: 1813 Act abolished trade monopoly except tea and China trade. D-1: 1833 Act turned EIC into purely administrative body.",
        "explanation_ta": "A-4: 1773 சட்டம் கருவூலத்திற்கு அறிக்கையிடச் செய்தது. B-3: 1784 சட்டம் வர்த்தகம், அரசியலைப் பிரித்தது. C-2: 1813 சட்டம் பகுதி ஏகபோக ஒழிப்பு தந்தது. D-1: 1833 சட்டம் நிறுவனத்தை தூய நிர்வாக அமைப்பாக்கியது.",
        "why_not_others_en": {
            "A-4, B-3, C-2, D-1": "Correct comparison of economic and administrative commercial transitions of EIC.",
            "A-3, B-4, C-1, D-2": "Incorrect. Reporting to Treasury was 1773 (A-4).",
            "A-4, B-2, C-3, D-1": "Incorrect. Function segregation was 1784 (B-3).",
            "A-1, B-3, C-2, D-4": "Incorrect. Pure administrative transformation was 1833 (D-1)."
        },
        "why_not_others_ta": {
            "A-4, B-3, C-2, D-1": "கிழக்கிந்திய நிறுவனத்தின் பொருளாதாரம் மற்றும் நிர்வாக வர்த்தக மாற்றங்களின் சரியான ஒப்பீடு.",
            "A-3, B-4, C-1, D-2": "தவறு. கருவூலத்திற்கு அறிக்கையிடுதல் 1773 சட்டம் (A-4).",
            "A-4, B-2, C-3, D-1": "தவறு. பணிகள் பிரிப்பு 1784 பிட் இந்தியச் சட்டம் (B-3).",
            "A-1, B-3, C-2, D-4": "தவறு. தூய நிர்வாக அமைப்பாக மாற்றம் 1833 (D-1)."
        },
        "tnpsc_tip_en": "TNPSC Trap: 1773 Act required Court of Directors to share all civil, military, and revenue correspondence with British government for first time.",
        "tnpsc_tip_ta": "TNPSC பொறி: 1773 சட்டம் முதன்முறையாக அனைத்து சிவில், ராணுவ மற்றும் வருவாய் கடிதப் போக்குவரத்தை பிரிட்டிஷ் அரசுடன் பகிரக் கோரியது.",
        "revision_fact_en": "Charter Act 1833 ended all commercial activities of EIC and made it an administrative trustee of the Crown.",
        "revision_fact_ta": "1833 சாசனச் சட்டம் நிறுவனத்தின் அனைத்து வர்த்தக நடவடிக்கைகளையும் முடிவுக்குக் கொண்டுவந்து பிரிட்டிஷ் அரசின் நிர்வாக டிரஸ்டியாக்கியது.",
        "bloom_level": "Analyze",
        "tags": ["Polity", "Historical Background", "EIC Charter Acts", "Regulating Act 1773", "Pitt's India Act 1784"]
    },
    {
        "id": "HB_MF_023",
        "subject": "Polity",
        "topic": "Historical Background of the Indian Constitution",
        "difficulty": "Hard",
        "question_type": "Match the Following",
        "list_i_en": [
            "Complete legislative power concentration in Governor-General",
            "Restoration of legislative power initiating decentralization",
            "Demarcation of Central and Provincial subjects",
            "Proposed All-India Federation with 3 Legislative Lists"
        ],
        "list_i_ta": [
            "கவர்னர் ஜெனரலிடம் முழுமையான சட்ட அதிகாரங்களின் குவிப்பு",
            "பரவலாக்கலைத் தொடங்கும் வகையில் மாகாண சட்ட அதிகாரங்களை மீட்டுத் தருதல்",
            "மத்திய மற்றும் மாகாண தலைப்புகளாகப் பாடங்களை பிரித்தல்",
            "3 சட்டப் பட்டியல்களுடன் அகில இந்திய கூட்டாட்சி முன்மொழிவு"
        ],
        "list_ii_en": [
            "Government of India Act, 1935",
            "Government of India Act, 1919",
            "Indian Councils Act, 1861",
            "Charter Act, 1833"
        ],
        "list_ii_ta": [
            "1935 இந்திய அரசுச் சட்டம்",
            "1919 இந்திய அரசுச் சட்டம்",
            "1861 இந்தியக் குழுக்கள் சட்டம்",
            "1833 சாசனச் சட்டம்"
        ],
        "correct_pairs": {"A": 4, "B": 3, "C": 2, "D": 1}, # A-4, B-3, C-2, D-1
        "distractors": [
            {"A": 3, "B": 4, "C": 1, "D": 2},
            {"A": 4, "B": 2, "C": 3, "D": 1},
            {"A": 2, "B": 3, "C": 4, "D": 1}
        ],
        "explanation_en": "A-4: Charter Act 1833 concentrated all law-making power in GG of India. B-3: 1861 Act restored legislative powers to Bombay & Madras. C-2: 1919 Act demarcated Central & Provincial subjects. D-1: 1935 Act created 3 Lists (Federal, Provincial, Concurrent).",
        "explanation_ta": "A-4: 1833 சட்டம் சட்ட அதிகாரங்களை மையப்படுத்தியது. B-3: 1861 சட்டம் மாகாண சட்ட அதிகாரங்களை மீட்டது. C-2: 1919 சட்டம் மத்திய, மாகாண தலைப்புகளைப் பிரித்தது. D-1: 1935 சட்டம் 3 பட்டியல்களை (கூட்டாட்சி, மாகாண, பொது) உருவாக்கியது.",
        "why_not_others_en": {
            "A-4, B-3, C-2, D-1": "Correct comparison of legislative centralization vs decentralization continuum.",
            "A-3, B-4, C-1, D-2": "Incorrect. Centralization peak was 1833 (A-4).",
            "A-4, B-2, C-3, D-1": "Incorrect. Decentralization started in 1861 (B-3), not 1919.",
            "A-2, B-3, C-4, D-1": "Incorrect. 3 Lists were created by 1935 Act (D-1)."
        },
        "why_not_others_ta": {
            "A-4, B-3, C-2, D-1": "சட்ட அதிகாரங்களின் மத்தியமயமாக்கல் மற்றும் பரவலாக்கல் ஒப்பீட்டின் சரியான பொருத்தம்.",
            "A-3, B-4, C-1, D-2": "தவறு. மத்தியமயமாக்கல் உச்சம் 1833 சாசனச் சட்டம் (A-4).",
            "A-4, B-2, C-3, D-1": "தவறு. பரவலாக்கல் 1861-ல் தொடங்கியது (B-3).",
            "A-2, B-3, C-4, D-1": "தவறு. 3 பட்டியல்கள் 1935 அரசுச் சட்டத்தில் உருவாக்கப்பட்டன (D-1)."
        },
        "tnpsc_tip_en": "TNPSC Trap: Residuary legislative powers under GOI Act 1935 were given to Viceroy, not to Federal Parliament.",
        "tnpsc_tip_ta": "TNPSC பொறி: 1935 அரசுச் சட்டத்தில் எஞ்சிய அதிகாரங்கள் வைஸ்ராய்க்கு வழங்கப்பட்டன, கூட்டாட்சி நாடாளுமன்றத்திற்கு அல்ல.",
        "revision_fact_en": "All-India Federation proposed in 1935 Act never came into being as Princely States did not join.",
        "revision_fact_ta": "சுதேச சமஸ்தானங்கள் இணையாததால் 1935 சட்டத்தில் முன்மொழியப்பட்ட அகில இந்தியக் கூட்டாட்சி அமையவே இல்லை.",
        "bloom_level": "Analyze",
        "tags": ["Polity", "Historical Background", "7th Schedule Origin", "Federal List", "Residuary Powers"]
    },
    {
        "id": "HB_MF_024",
        "subject": "Polity",
        "topic": "Historical Background of the Indian Constitution",
        "difficulty": "Hard",
        "question_type": "Match the Following",
        "list_i_en": [
            "Salaries of Board of Control charged on Indian Revenues",
            "Legislative Council members permitted to discuss budget",
            "Separation of Provincial Budgets from Central Budget",
            "Establishment of Federal Reserve Bank & Railway Authority"
        ],
        "list_i_ta": [
            "கட்டுப்பாட்டு வாரியத்தின் ஊதியம் இந்திய வருவாயில் இருந்து வழங்கப்படுதல்",
            "சட்ட மேலவை உறுப்பினர்கள் வரவுசெலவுத் திட்டத்தை விவாதிக்க அனுமதித்தல்",
            "மத்திய வரவுசெலவுத் திட்டத்திலிருந்து மாகாண வரவுசெலவுத் திட்டத்தைப் பிரித்தல்",
            "கூட்டாட்சி ரிசர்வ் வங்கி & இரயில்வே அதிகார அமைப்பை நிறுவுதல்"
        ],
        "list_ii_en": [
            "Government of India Act, 1935",
            "Government of India Act, 1919",
            "Indian Councils Act, 1892",
            "Charter Act, 1793"
        ],
        "list_ii_ta": [
            "1935 இந்திய அரசுச் சட்டம்",
            "1919 இந்திய அரசுச் சட்டம்",
            "1892 இந்தியக் குழுக்கள் சட்டம்",
            "1793 சாசனச் சட்டம்"
        ],
        "correct_pairs": {"A": 4, "B": 3, "C": 2, "D": 1}, # A-4, B-3, C-2, D-1
        "distractors": [
            {"A": 3, "B": 4, "C": 1, "D": 2},
            {"A": 4, "B": 2, "C": 3, "D": 1},
            {"A": 1, "B": 3, "C": 2, "D": 4}
        ],
        "explanation_en": "A-4: Charter Act 1793 charged Board salaries on Indian revenues (reversed in 1919). B-3: 1892 Act permitted discussion on annual budget. C-2: 1919 Act separated provincial budgets. D-1: 1935 Act provided for RBI & Federal Railway Authority.",
        "explanation_ta": "A-4: 1793 சாசனச் சட்டம் வாரிய ஊதியத்தை இந்திய வருவாயில் சுமத்தியது (1919-ல் மாற்றப்பட்டது). B-3: 1892 சட்டம் பட்ஜெட் விவாதத்தை அனுமதித்தது. C-2: 1919 சட்டம் மாகாண பட்ஜெட்டைப் பிரித்தது. D-1: 1935 சட்டம் ரிசர்வ் வங்கி மற்றும் இரயில்வே ஆணையத்திற்கு வழிவகுத்தது.",
        "why_not_others_en": {
            "A-4, B-3, C-2, D-1": "Correct financial devolution comparison across constitutional enactments.",
            "A-3, B-4, C-1, D-2": "Incorrect. Board of Control salary charging was 1793 (A-4).",
            "A-4, B-2, C-3, D-1": "Incorrect. Budget discussion was introduced in 1892 (B-3), not 1919.",
            "A-1, B-3, C-2, D-4": "Incorrect. RBI & Federal Railway Authority were in 1935 Act (D-1)."
        },
        "why_not_others_ta": {
            "A-4, B-3, C-2, D-1": "சட்டச் சட்டங்கள் முழுவதும் நிதிப் பரவலாக்கத்தின் சரியான ஒப்பீடு.",
            "A-3, B-4, C-1, D-2": "தவறு. கட்டுப்பாட்டு வாரிய ஊதியச் சுமை 1793 சாசனச் சட்டம் (A-4).",
            "A-4, B-2, C-3, D-1": "தவறு. பட்ஜெட் விவாதம் 1892-ல் அறிமுகமானது (B-3).",
            "A-1, B-3, C-2, D-4": "தவறு. ரிசர்வ் வங்கி மற்றும் இரயில்வே ஆணையம் 1935 சட்டம் (D-1)."
        },
        "tnpsc_tip_en": "TNPSC Trap: Government of India Act 1919 stopped paying Secretary of State salary from Indian revenues, transferring it to British Exchequer.",
        "tnpsc_tip_ta": "TNPSC பொறி: 1919 இந்திய அரசுச் சட்டம் இந்திய அமைச்சரின் ஊதியத்தை இந்திய வருவாயில் இருந்து வழங்குவதை நிறுத்தி பிரிட்டிஷ் அரசுச் செலவில் மாற்றியது.",
        "revision_fact_en": "1793 Act continued charging Board of Control salaries on Indian revenues until 1919 Montford reforms.",
        "revision_fact_ta": "1793 சட்டம் கட்டுப்பாட்டு வாரிய ஊதியங்களை 1919 சீர்திருத்தம் வரை இந்திய வருவாயிலேயே சுமத்தியது.",
        "bloom_level": "Analyze",
        "tags": ["Polity", "Historical Background", "Financial Devolution", "Charter Act 1793", "Budget Evolution"]
    },
    {
        "id": "HB_MF_025",
        "subject": "Polity",
        "topic": "Historical Background of the Indian Constitution",
        "difficulty": "Hard",
        "question_type": "Match the Following",
        "list_i_en": [
            "First Communal Electorate (Muslims)",
            "Extension to Sikhs, Indian Christians & Anglo-Indians",
            "Communal Award proposing separate electorates for Depressed Classes",
            "Statutory separate electorates for Depressed Classes, Women & Labour"
        ],
        "list_i_ta": [
            "முதல் வகுப்புவாதத் தொகுதி (முஸ்லிம்கள்)",
            "சீக்கியர்கள், இந்தியக் கிறிஸ்தவர்கள் & ஆங்லோ இந்தியர்களுக்கு நீட்டிப்பு",
            "ஒடுக்கப்பட்டோருக்கு தனித் தொகுதி முன்மொழிந்த வகுப்புவாத அறிக்கை",
            "ஒடுக்கப்பட்டோர், பெண்கள் & தொழிலாளர்களுக்கு சட்டப்பூர்வ தனித் தொகுதி"
        ],
        "list_ii_en": [
            "Government of India Act, 1935",
            "Ramsay MacDonald Communal Award, 1932",
            "Government of India Act, 1919",
            "Indian Councils Act, 1909"
        ],
        "list_ii_ta": [
            "1935 இந்திய அரசுச் சட்டம்",
            "ராம்சே மெக்டொனால்டு வகுப்புவாத அறிக்கை, 1932",
            "1919 இந்திய அரசுச் சட்டம்",
            "1909 இந்தியக் குழுக்கள் சட்டம்"
        ],
        "correct_pairs": {"A": 4, "B": 3, "C": 2, "D": 1}, # A-4, B-3, C-2, D-1
        "distractors": [
            {"A": 3, "B": 4, "C": 1, "D": 2},
            {"A": 4, "B": 2, "C": 3, "D": 1},
            {"A": 2, "B": 3, "C": 4, "D": 1}
        ],
        "explanation_en": "A-4: 1909 Act introduced separate electorates for Muslims. B-3: 1919 Act extended them to Sikhs, Christians, Anglo-Indians. C-2: 1932 Communal Award proposed separate electorates for Depressed Classes. D-1: GOI Act 1935 enacted separate electorates for Depressed Classes, Women, Labour.",
        "explanation_ta": "A-4: 1909 சட்டம் முஸ்லிம்களுக்கு தனித் தொகுதி அளித்தது. B-3: 1919 சட்டம் சீக்கியர், கிறிஸ்தவர், ஆங்லோ இந்தியருக்கு நீட்டித்தது. C-2: 1932 ராம்சே மெக்டொனால்டு அறிக்கை ஒடுக்கப்பட்டோருக்கு முன்மொழிந்தது. D-1: 1935 அரசுச் சட்டம் ஒடுக்கப்பட்டோர், பெண்கள், தொழிலாளருக்கு சட்டப்பூர்வ தனித் தொகுதி தந்தது.",
        "why_not_others_en": {
            "A-4, B-3, C-2, D-1": "Correct comparison of communal electorate stages.",
            "A-3, B-4, C-1, D-2": "Incorrect. Muslim separate electorate was 1909 (A-4).",
            "A-4, B-2, C-3, D-1": "Incorrect. Extension to Sikhs/Christians was 1919 (B-3).",
            "A-2, B-3, C-4, D-1": "Incorrect. Communal Award proposal was 1932 (C-2)."
        },
        "why_not_others_ta": {
            "A-4, B-3, C-2, D-1": "வகுப்புவாதத் தொகுதி கட்டங்களின் சரியான ஒப்பீடு.",
            "A-3, B-4, C-1, D-2": "தவறு. முஸ்லிம் தனித் தொகுதி 1909 (A-4).",
            "A-4, B-2, C-3, D-1": "தவறு. சீக்கியர்/கிறிஸ்தவர் நீட்டிப்பு 1919 (B-3).",
            "A-2, B-3, C-4, D-1": "தவறு. வகுப்புவாத அறிக்கை 1932 (C-2)."
        },
        "tnpsc_tip_en": "TNPSC Trap: Communal Award 1932 was announced by British Prime Minister Ramsay MacDonald; Mahatma Gandhi protested against it via fast unto death in Yerwada jail.",
        "tnpsc_tip_ta": "TNPSC பொறி: 1932 வகுப்புவாத அறிக்கையை பிரிட்டிஷ் பிரதமர் ராம்சே மெக்டொனால்டு அறிவித்தார்; அதை எதிர்த்து காந்தியடிகள் எரவாடா சிறையில் சாகும் வரை உண்ணாவிரதம் இருந்தார்.",
        "revision_fact_en": "Poona Pact was signed on September 24, 1932 between Dr. B.R. Ambedkar and Madan Mohan Malaviya.",
        "revision_fact_ta": "1932 செப்டம்பர் 24 அன்று டாக்டர் பி.ஆர். அம்பேத்கர் மற்றும் மதன் மோகன் மாளவியா இடையே பூனா ஒப்பந்தம் கையெழுத்தானது.",
        "bloom_level": "Analyze",
        "tags": ["Polity", "Historical Background", "Communal Award 1932", "Poona Pact", "Morley-Minto 1909"]
    },

    # ------------------ Group 4: Constitutional Evolution Matching (5 Questions) ------------------
    {
        "id": "HB_MF_026",
        "subject": "Polity",
        "topic": "Historical Background of the Indian Constitution",
        "difficulty": "Hard",
        "question_type": "Match the Following",
        "list_i_en": [
            "Supreme Court of Judicature at Calcutta established",
            "High Courts created at Calcutta, Bombay & Madras",
            "Federal Court of India established at Delhi",
            "Privy Council Jurisdiction Abolished"
        ],
        "list_i_ta": [
            "கொல்கத்தா கோட்டை வில்லியம் உச்ச நீதிமன்றம் அமைத்தல்",
            "கொல்கத்தா, பம்பாய் & மெட்ராஸ் உயர் நீதிமன்றங்கள் அமைத்தல்",
            "டெல்லியில் இந்தியக் கூட்டாட்சி நீதிமன்றம் அமைத்தல்",
            "பிரிவி கவுன்சில் அதிகார வரம்பு ஒழிக்கப்படுதல்"
        ],
        "list_ii_en": [
            "Abolition of Privy Council Jurisdiction Act, 1949",
            "Government of India Act, 1935",
            "Indian High Courts Act, 1861",
            "Regulating Act, 1773"
        ],
        "list_ii_ta": [
            "1949 பிரிவி கவுன்சில் அதிகார வரம்பு ஒழிப்புச் சட்டம்",
            "1935 இந்திய அரசுச் சட்டம்",
            "1861 இந்திய உயர் நீதிமன்றங்கள் சட்டம்",
            "1773 ஒழுங்குமுறைச் சட்டம்"
        ],
        "correct_pairs": {"A": 4, "B": 3, "C": 2, "D": 1}, # A-4, B-3, C-2, D-1
        "distractors": [
            {"A": 3, "B": 4, "C": 1, "D": 2},
            {"A": 4, "B": 2, "C": 3, "D": 1},
            {"A": 2, "B": 3, "C": 4, "D": 1}
        ],
        "explanation_en": "A-4: 1773 Act set up SC at Calcutta (1774). B-3: 1861 High Courts Act created 3 chartered High Courts (1862) abolishing SC and Sadar Adalats. C-2: 1935 Act set up Federal Court (1937). D-1: 1949 Act abolished appeals to Privy Council transferring jurisdiction to Federal Court before SC India inauguration.",
        "explanation_ta": "A-4: 1773 சட்டம் கல்கத்தா உச்ச நீதிமன்றத்தை அமைத்தது. B-3: 1861 உயர் நீதிமன்றச் சட்டம் 3 உயர் நீதிமன்றங்களை உருவாக்கியது (1862). C-2: 1935 சட்டம் கூட்டாட்சி நீதிமன்றத்தை அமைத்தது (1937). D-1: 1949 சட்டம் பிரிவி கவுன்சில் மேல்முறையீட்டை ஒழித்தது.",
        "why_not_others_en": {
            "A-4, B-3, C-2, D-1": "Correct structural sequence of Indian judicial evolution.",
            "A-3, B-4, C-1, D-2": "Incorrect. SC Calcutta was 1773 (A-4).",
            "A-4, B-2, C-3, D-1": "Incorrect. Chartered High Courts were created by 1861 Act (B-3).",
            "A-2, B-3, C-4, D-1": "Incorrect. Federal Court was created under 1935 Act (C-2)."
        },
        "why_not_others_ta": {
            "A-4, B-3, C-2, D-1": "இந்திய நீதித்துறை பரிணாமத்தின் சரியான வரிசை பொருத்தம்.",
            "A-3, B-4, C-1, D-2": "தவறு. கல்கத்தா உச்ச நீதிமன்றம் 1773 சட்டம் (A-4).",
            "A-4, B-2, C-3, D-1": "தவறு. சாசன உயர் நீதிமன்றங்கள் 1861 சட்டத்தால் அமைக்கப்பட்டன (B-3).",
            "A-2, B-3, C-4, D-1": "தவறு. கூட்டாட்சி நீதிமன்றம் 1935 அரசுச் சட்டத்தில் இருந்தது (C-2)."
        },
        "tnpsc_tip_en": "TNPSC Trap: Indian High Courts Act 1861 abolished both Supreme Court of Calcutta and Sadar Adalats to merge them into High Courts.",
        "tnpsc_tip_ta": "TNPSC பொறி: 1861 உயர் நீதிமன்றச் சட்டம் கல்கத்தா உச்ச நீதிமன்றம் மற்றும் சதா அடாலத்துகள் இரண்டையும் ஒழித்து உயர் நீதிமன்றங்களாக இணைத்தது.",
        "revision_fact_en": "Supreme Court of India was inaugurated on January 28, 1950, replacing both Federal Court and Judicial Committee of Privy Council.",
        "revision_fact_ta": "1950 ஜனவரி 28 அன்று இந்திய உச்ச நீதிமன்றம் கூட்டாட்சி நீதிமன்றம் மற்றும் பிரிவி கவுன்சிலுக்குப் பதிலாகத் தொடங்கப்பட்டது.",
        "bloom_level": "Evaluate",
        "tags": ["Polity", "Historical Background", "Judicial Evolution", "High Courts Act 1861", "Privy Council"]
    },
    {
        "id": "HB_MF_027",
        "subject": "Polity",
        "topic": "Historical Background of the Indian Constitution",
        "difficulty": "Hard",
        "question_type": "Match the Following",
        "list_i_en": [
            "Central Legislative Council with 6 legislative members",
            "Imperial Legislative Council expanded to 10-16 members",
            "Imperial Legislative Council expanded to 60 members",
            "Bicameral Parliament with Council of State (60) & Assembly (140)"
        ],
        "list_i_ta": [
            "6 சட்ட உறுப்பினர்களுடன் மத்திய சட்ட மேலவை",
            "இம்பீரியல் சட்ட மேலவை 10-16 உறுப்பினர்களாக விரிவாக்கம்",
            "இம்பீரியல் சட்ட மேலவை 60 உறுப்பினர்களாக விரிவாக்கம்",
            "மாநிலங்கள் அவை (60) & சட்டமன்றத்துடன் (140) இரு அவை நாடாளுமன்றம்"
        ],
        "list_ii_en": [
            "Government of India Act, 1919",
            "Indian Councils Act, 1909",
            "Indian Councils Act, 1892",
            "Charter Act, 1853"
        ],
        "list_ii_ta": [
            "1919 இந்திய அரசுச் சட்டம்",
            "1909 இந்தியக் குழுக்கள் சட்டம்",
            "1892 இந்தியக் குழுக்கள் சட்டம்",
            "1853 சாசனச் சட்டம்"
        ],
        "correct_pairs": {"A": 4, "B": 3, "C": 2, "D": 1}, # A-4, B-3, C-2, D-1
        "distractors": [
            {"A": 3, "B": 4, "C": 1, "D": 2},
            {"A": 4, "B": 2, "C": 3, "D": 1},
            {"A": 2, "B": 3, "C": 4, "D": 1}
        ],
        "explanation_en": "A-4: 1853 Act added 6 legislative members. B-3: 1892 Act expanded council strength to 10-16. C-2: 1909 Act expanded council strength to 60. D-1: 1919 Act created bicameral legislature with Council of State (60) and Legislative Assembly (140).",
        "explanation_ta": "A-4: 1853 சட்டம் 6 உறுப்பினர்களைக் கொண்டு வந்தது. B-3: 1892 சட்டம் 10-16 உறுப்பினர்களாக உயர்த்தியது. C-2: 1909 சட்டம் 60 உறுப்பினர்களாக உயர்த்தியது. D-1: 1919 சட்டம் மாநிலங்கள் அவை (60) மற்றும் சட்டமன்றம் (140) கொண்ட இரு அவைகளை அமைத்தது.",
        "why_not_others_en": {
            "A-4, B-3, C-2, D-1": "Correct matching of numerical expansion of Indian legislature.",
            "A-3, B-4, C-1, D-2": "Incorrect. First central council was 1853 (A-4).",
            "A-4, B-2, C-3, D-1": "Incorrect. 1892 Act council strength was 10-16 (B-3).",
            "A-2, B-3, C-4, D-1": "Incorrect. 1909 Act council strength was 60 (C-2)."
        },
        "why_not_others_ta": {
            "A-4, B-3, C-2, D-1": "இந்திய சட்டமன்றத்தின் உறுப்பினர் எண்ணிக்கைப் பெருக்கத்தின் சரியான பொருத்தம்.",
            "A-3, B-4, C-1, D-2": "தவறு. முதல் மத்திய சட்ட மேலவை 1853 சாசனச் சட்டம் (A-4).",
            "A-4, B-2, C-3, D-1": "தவறு. 1892 சட்டம் உறுப்பினர் எண்ணிக்கை 10-16 (B-3).",
            "A-2, B-3, C-4, D-1": "தவறு. 1909 சட்டம் உறுப்பினர் எண்ணிக்கை 60 (C-2)."
        },
        "tnpsc_tip_en": "TNPSC Trap: Majority in Central Legislative Council was OFFICIAL under 1909 Act, but NON-OFFICIAL under 1919 Act.",
        "tnpsc_tip_ta": "TNPSC பொறி: 1909 சட்டத்தில் மத்திய மேலவையில் அரசு உறுப்பினர்கள் பெரும்பான்மை; 1919 சட்டத்தில் அரசார்பற்ற உறுப்பினர்கள் பெரும்பான்மை.",
        "revision_fact_en": "1853 Legislative Council functioned on the model of British Parliament, introducing parliamentary procedure in India.",
        "revision_fact_ta": "1853 சட்ட மேலவை பிரிட்டிஷ் நாடாளுமன்ற மாதிரியில் செயல்பட்டு இந்தியாவில் நாடாளுமன்ற முறையை அறிமுகப்படுத்தியது.",
        "bloom_level": "Analyze",
        "tags": ["Polity", "Historical Background", "Legislative Expansion", "Imperial Legislative Council", "Bicameral Central Legislature"]
    },
    {
        "id": "HB_MF_028",
        "subject": "Polity",
        "topic": "Historical Background of the Indian Constitution",
        "difficulty": "Hard",
        "question_type": "Match the Following",
        "list_i_en": [
            "Company forbidden from unapproved aggressive wars & treaties",
            "Crown assumed Paramountcy & pledged to respect state treaties",
            "States offered Instrument of Accession to All-India Federation",
            "Lapse of British Paramountcy leaving states sovereign"
        ],
        "list_i_ta": [
            "அனுமதியின்றி ஆக்கிரமிப்பு போர்கள் மற்றும் ஒப்பந்தங்கள் செய்ய நிறுவனத்திற்குத் தடை",
            "கிரீடம் பரமாதிக்கத்தை ஏற்ற்று சுதேச ஒப்பந்தங்களை மதிப்பதாக உறுதி அளித்தது",
            "அகில இந்தியக் கூட்டாட்சியில் இணைய சுதேச சமஸ்தானங்களுக்கு இணைப்பு ஆவணம்",
            "பிரிட்டிஷ் பரமாதிக்கம் முடிவுக்கு வந்து சுதேச அரசுகள் இறையாண்மை பெறுதல்"
        ],
        "list_ii_en": [
            "Indian Independence Act, 1947",
            "Government of India Act, 1935",
            "Government of India Act, 1858",
            "Pitt's India Act, 1784"
        ],
        "list_ii_ta": [
            "1947 இந்திய சுதந்திரச் சட்டம்",
            "1935 இந்திய அரசுச் சட்டம்",
            "1858 இந்திய அரசுச் சட்டம்",
            "1784 பிட் இந்தியச் சட்டம்"
        ],
        "correct_pairs": {"A": 4, "B": 3, "C": 2, "D": 1}, # A-4, B-3, C-2, D-1
        "distractors": [
            {"A": 3, "B": 4, "C": 1, "D": 2},
            {"A": 4, "B": 2, "C": 3, "D": 1},
            {"A": 2, "B": 3, "C": 4, "D": 1}
        ],
        "explanation_en": "A-4: Pitt's India Act 1784 prohibited aggressive wars and treaties of guarantee without Parliament/Board sanction. B-3: 1858 Act declared Crown Paramountcy and pledge to honor treaties. C-2: 1935 Act provided Instrument of Accession for princely states. D-1: 1947 Act declared lapse of paramountcy.",
        "explanation_ta": "A-4: 1784 பிட் இந்தியச் சட்டம் ஆக்கிரமிப்பு போர்களைத் தடுத்தது. B-3: 1858 அரசுச் சட்டம் பரமாதிக்கத்தை ஏற்று ஒப்பந்தங்களை மதிப்பதாகக் கூறியது. C-2: 1935 சட்டம் இணைப்பு ஆவணத்தை தந்தது. D-1: 1947 சட்டம் பரமாதிக்க ஒழிப்பை அறிவித்தது.",
        "why_not_others_en": {
            "A-4, B-3, C-2, D-1": "Correct evolutionary matching of British Crown relationship with Princely States.",
            "A-3, B-4, C-1, D-2": "Incorrect. Prohibiting aggressive wars was 1784 Act (A-4).",
            "A-4, B-2, C-3, D-1": "Incorrect. Crown paramountcy assumption was 1858 (B-3).",
            "A-2, B-3, C-4, D-1": "Incorrect. Instrument of Accession for federation was 1935 Act (C-2)."
        },
        "why_not_others_ta": {
            "A-4, B-3, C-2, D-1": "சுதேச சமஸ்தானங்களுடனான பிரிட்டிஷ் உறவுமுறை பரிணாமத்தின் சரியான பொருத்தம்.",
            "A-3, B-4, C-1, D-2": "தவறு. ஆக்கிரமிப்பு போர் தடை 1784 பிட் இந்தியச் சட்டம் (A-4).",
            "A-4, B-2, C-3, D-1": "தவறு. கிரீட பரமாதிக்கம் 1858 அரசுச் சட்டம் (B-3).",
            "A-2, B-3, C-4, D-1": "தவறு. இணைப்பு ஆவணம் 1935 அரசுச் சட்டம் (C-2)."
        },
        "tnpsc_tip_en": "TNPSC Trap: Under 1947 Act, Paramountcy did not transfer to India or Pakistan; it LAPSED, giving Princely States option to join India, Pakistan, or stay independent.",
        "tnpsc_tip_ta": "TNPSC பொறி: 1947 சட்டத்தில் பரமாதிக்கம் இந்தியாவுக்கோ பாகிஸ்தானுக்கோ மாற்றப்படவில்லை; அது முற்றிலும் ரத்தானது.",
        "revision_fact_en": "Sardar Vallabhbhai Patel, along with V.P. Menon, integrated 565 princely states into the Indian Union.",
        "revision_fact_ta": "சர்தார் வல்லபாய் படேல் வி.பி. மேனனுடன் இணைந்து 565 சுதேச சமஸ்தானங்களை இந்திய யூனியனுடன் இணைத்தார்.",
        "bloom_level": "Evaluate",
        "tags": ["Polity", "Historical Background", "Princely States", "Lapse of Paramountcy", "Instrument of Accession"]
    },
    {
        "id": "HB_MF_029",
        "subject": "Polity",
        "topic": "Historical Background of the Indian Constitution",
        "difficulty": "Hard",
        "question_type": "Match the Following",
        "list_i_en": [
            "Statutory commission appointed under Sec 84E of 1919 Act",
            "Enquired into working of provincial dyarchy and central control",
            "Published White Paper on Constitutional Reforms",
            "Proposed Constituent Assembly and 3-tier federal grouping"
        ],
        "list_i_ta": [
            "1919 சட்டத்தின் பிரிவு 84E-ன் கீழ் நியமிக்கப்பட்ட சட்டப்பூர்வ ஆணையம்",
            "மாகாண இரட்டை ஆட்சி மற்றும் மத்தியக் கட்டுப்பாட்டின் செயல்பாட்டை விசாரித்தது",
            "அரசியலமைப்பு சீர்திருத்தங்கள் குறித்த வெள்ளை அறிக்கையை வெளியிட்டது",
            "அரசியலமைப்பு நிர்ணய சபை மற்றும் 3-அடுக்கு கூட்டாட்சி அமைப்பை முன்மொழிந்தது"
        ],
        "list_ii_en": [
            "Cabinet Mission, 1946",
            "British Government White Paper, 1933",
            "Muddiman Committee, 1924",
            "Simon Commission, 1927"
        ],
        "list_ii_ta": [
            "கேபினெட் தூதுக்குழு, 1946",
            "பிரிட்டிஷ் அரசு வெள்ளை அறிக்கை, 1933",
            "முட்டிமேன் குழு, 1924",
            "சைமன் ஆணையம், 1927"
        ],
        "correct_pairs": {"A": 4, "B": 3, "C": 2, "D": 1}, # A-4, B-3, C-2, D-1
        "distractors": [
            {"A": 3, "B": 4, "C": 1, "D": 2},
            {"A": 4, "B": 2, "C": 3, "D": 1},
            {"A": 1, "B": 3, "C": 2, "D": 4}
        ],
        "explanation_en": "A-4:  Simon Commission (1927) was statutory commission under 1919 Act. B-3: Muddiman Committee (1924) enquired into dyarchy working. C-2: British Govt published White Paper in 1933 based on RTCs. D-1: Cabinet Mission 1946 proposed Constituent Assembly & 3-tier grouping.",
        "explanation_ta": "A-4: 1927 சைமன் ஆணையம் 1919 சட்டத்தின்கீழ் அமைக்கப்பட்ட சட்டப்பூர்வ ஆணையம். B-3: 1924 முட்டிமேன் குழு இரட்டை ஆட்சியை ஆராய்ந்தது. C-2: 1933-ல் பிரிட்டிஷ் அரசு வெள்ளை அறிக்கை வெளியிட்டது. D-1: 1946 கேபினெட் தூதுக்குழு நிர்ணய சபையை முன்மொழிந்தது.",
        "why_not_others_en": {
            "A-4, B-3, C-2, D-1": "Correct matching of inquiry commissions and constitutional reform papers.",
            "A-3, B-4, C-1, D-2": "Incorrect. Statutory commission under Sec 84E was Simon Commission (A-4).",
            "A-4, B-2, C-3, D-1": "Incorrect. Dyarchy enquiry committee was Muddiman Committee (B-3).",
            "A-1, B-3, C-2, D-4": "Incorrect. White paper was published in 1933 (C-2)."
        },
        "why_not_others_ta": {
            "A-4, B-3, C-2, D-1": "விசாரணை ஆணையங்கள் மற்றும் சீர்திருத்த ஆவணங்களின் சரியான பொருத்தம்.",
            "A-3, B-4, C-1, D-2": "தவறு. பிரிவு 84E சட்டப்பூர்வ ஆணையம் சைமன் ஆணையம் (A-4).",
            "A-4, B-2, C-3, D-1": "தவறு. இரட்டை ஆட்சி விசரணைக்குழு முட்டிமேன் குழு (B-3).",
            "A-1, B-3, C-2, D-4": "தவறு. வெள்ளை அறிக்கை 1933-ல் வெளியிடப்பட்டது (C-2)."
        },
        "tnpsc_tip_en": "TNPSC Trap: Cabinet Mission 1946 REJECTED the demand for two separate Constituent Assemblies and partition of India.",
        "tnpsc_tip_ta": "TNPSC பொறி: 1946 கேபினெட் தூதுக்குழு இரண்டு தனித்தனி நிர்ணய சபைகள் மற்றும் இந்தியப் பிரிவினை கோரிக்கையை நிராகரித்தது.",
        "revision_fact_en": "Joint Select Committee chaired by Lord Linlithgow examined the 1933 White Paper leading to GOI Act 1935.",
        "revision_fact_ta": "லின்லித்கோ பிரபு தலைமையிலான கூட்டுக் தேர்வுக் குழு 1933 வெள்ளை அறிக்கையை ஆராய்ந்து 1935 அரசுச் சட்டத்தை உருவாக்கியது.",
        "bloom_level": "Evaluate",
        "tags": ["Polity", "Historical Background", "Cabinet Mission 1946", "Simon Commission", "White Paper 1933"]
    },
    {
        "id": "HB_MF_030",
        "subject": "Polity",
        "topic": "Historical Background of the Indian Constitution",
        "difficulty": "Hard",
        "question_type": "Match the Following",
        "list_i_en": [
            "First recognition of Indians' right to frame Constituent Assembly",
            "Post-war Dominion Status proposal with right of provinces to secede",
            "Constituent Assembly plan accepted & executed",
            "Abolished British Rule and created India and Pakistan Dominions"
        ],
        "list_i_ta": [
            "இந்தியர்கள் அரசியலமைப்பை உருவாக்கும் உரிமைக்கான முதல் அங்கீகாரம்",
            "மாகாணங்கள் விலகும் உரிமையுடன் போருக்குப் பிந்தைய டொமினியன் அந்தஸ்து முன்மொழிவு",
            "அரசியலமைப்பு நிர்ணய சபை திட்டம் ஏற்றுக்கொள்ளப்பட்டு செயல்படுத்தப்பட்டது",
            "பிரிட்டிஷ் ஆட்சியை ஒழித்து இந்தியா மற்றும் பாகிஸ்தான் டொமினியன்களை உருவாக்கியது"
        ],
        "list_ii_en": [
            "Indian Independence Act, 1947",
            "Cabinet Mission Plan, 1946",
            "Cripps Mission, 1942",
            "August Offer, 1940"
        ],
        "list_ii_ta": [
            "1947 இந்திய சுதந்திரச் சட்டம்",
            "1946 கேபினெட் தூதுக்குழு திட்டம்",
            "1942 கிரிப்ஸ் தூதுக்குழு",
            "1940 ஆகஸ்ட் சலுகை"
        ],
        "correct_pairs": {"A": 4, "B": 3, "C": 2, "D": 1}, # A-4, B-3, C-2, D-1
        "distractors": [
            {"A": 3, "B": 4, "C": 1, "D": 2},
            {"A": 4, "B": 2, "C": 3, "D": 1},
            {"A": 1, "B": 3, "C": 2, "D": 4}
        ],
        "explanation_en": "A-4: August Offer 1940 first recognized right of Indians to frame Constitution. B-3: Cripps Mission 1942 proposed post-war Dominion status & provincial option to secede. C-2: Cabinet Mission Plan 1946 set up Constituent Assembly. D-1: 1947 Act abolished British rule creating India & Pakistan.",
        "explanation_ta": "A-4: 1940 ஆகஸ்ட் சலுகை முதன்முதலாக இந்தியர்களின் அரசியலமைப்பு உரிமையை அங்கீகரித்தது. B-3: 1942 கிரிப்ஸ் தூதுக்குழு போருக்குப் பிந்தைய டொமினியன் அந்தஸ்தை முன்மொழிந்தது. C-2: 1946 கேபினெட் தூதுக்குழு நிர்ணய சபையை அமைத்தது. D-1: 1947 சட்டம் பிரிட்டிஷ் ஆட்சியை ஒழித்தது.",
        "why_not_others_en": {
            "A-4, B-3, C-2, D-1": "Correct chronological matching of 1940s power transfer milestones.",
            "A-3, B-4, C-1, D-2": "Incorrect. August Offer was 1940 (A-4).",
            "A-4, B-2, C-3, D-1": "Incorrect. Cripps Mission proposal was 1942 (B-3).",
            "A-1, B-3, C-2, D-4": "Incorrect. Cabinet Mission executed Constituent Assembly plan in 1946 (C-2)."
        },
        "why_not_others_ta": {
            "A-4, B-3, C-2, D-1": "1940-களின் அதிகாரப் பரிமாற்ற மைல்கற்களின் சரியான காலவரிசை பொருத்தம்.",
            "A-3, B-4, C-1, D-2": "தவறு. ஆகஸ்ட் சலுகை 1740 (A-4).",
            "A-4, B-2, C-3, D-1": "தவறு. கிரிப்ஸ் தூதுக்குழு 1942 (B-3).",
            "A-1, B-3, C-2, D-4": "தவறு. கேபினெட் தூதுக்குழு 1946-ல் நிர்ணய சபையைச் செயல்படுத்தியது (C-2)."
        },
        "tnpsc_tip_en": "TNPSC Trap: Lord Linlithgow issued August Offer in 1940; Sir Stafford Cripps led Cripps Mission in 1942; Lord Atlee announced transfer of power in Feb 1947.",
        "tnpsc_tip_ta": "TNPSC பொறி: லின்லித்கோ பிரபு 1940 ஆகஸ்ட் சலுகையை அறிவித்தார்; ஸ்டாஃபோர்டு கிரிப்ஸ் 1942 கிரிப்ஸ் குழுவை வழிநடத்தினார்; அட்லி பிரபு 1947 பிப்ரவரியில் அதிகாரப் பரிமாற்றத்தை அறிவித்தார்.",
        "revision_fact_en": "Indian Independence Act received Royal Assent on July 18, 1947 and came into force on August 15, 1947.",
        "revision_fact_ta": "இந்திய சுதந்திரச் சட்டம் 1947 ஜூலை 18 அன்று அரச ஒப்புதல் பெற்று ஆகஸ்ட் 15 அன்று அமலுக்கு வந்தது.",
        "bloom_level": "Evaluate",
        "tags": ["Polity", "Historical Background", "August Offer", "Cripps Mission", "Cabinet Mission", "1947 Independence Act"]
    }
]

# Process questions to form final TNPSC Nova AI JSON schema structure
final_questions = []

answer_pool = ["A", "B", "C", "D"]
# Pre-balance answer distribution across 30 questions
# We want 8 A, 7 B, 8 C, 7 D
target_answers = ["A"]*8 + ["B"]*7 + ["C"]*8 + ["D"]*7
random.seed(42)
random.shuffle(target_answers)

for idx, q_data in enumerate(questions_raw):
    q_id = q_data["id"]
    correct_ans_id = target_answers[idx]
    
    pairs = q_data["correct_pairs"]
    correct_match_str = f"A-{pairs['A']}, B-{pairs['B']}, C-{pairs['C']}, D-{pairs['D']}"
    
    # Collect distractor option strings
    distractor_strs = []
    for d in q_data["distractors"]:
        d_str = f"A-{d['A']}, B-{d['B']}, C-{d['C']}, D-{d['D']}"
        distractor_strs.append(d_str)
        
    # Build options dictionary mapping A, B, C, D to option strings
    options_map = {}
    options_map[correct_ans_id] = correct_match_str
    
    remaining_opt_ids = [opt for opt in ["A", "B", "C", "D"] if opt != correct_ans_id]
    for i, opt_id in enumerate(remaining_opt_ids):
        options_map[opt_id] = distractor_strs[i]
        
    # Build options array for schema
    options_arr = []
    options_en_arr = []
    options_ta_arr = []
    
    why_not_others_dict = {}
    
    for opt_id in ["A", "B", "C", "D"]:
        opt_text = options_map[opt_id]
        options_arr.append({
            "id": opt_id,
            "en": opt_text,
            "ta": opt_text
        })
        options_en_arr.append(opt_text)
        options_ta_arr.append(opt_text)
        
        # Build why_not_others entry for this option
        if opt_id == correct_ans_id:
            why_not_others_dict[opt_id] = {
                "en": f"Correct. {q_data['why_not_others_en'].get(opt_text, 'This is the correct matching set.')}",
                "ta": f"சரி. {q_data['why_not_others_ta'].get(opt_text, 'இது சரியான பொருத்தத் தொகுதி.')}"
            }
        else:
            why_not_others_dict[opt_id] = {
                "en": f"Incorrect. {q_data['why_not_others_en'].get(opt_text, 'This matching pair combination contains wrong alignments.')}",
                "ta": f"தவறு. {q_data['why_not_others_ta'].get(opt_text, 'இந்த பொருத்தக் கலவையில் தவறான இணைப்புகள் உள்ளன.')}"
            }
            
    # Format List I and List II string for question prompt
    list_i_en_str = "\n".join([f"{letter}. {text}" for letter, text in zip(["A", "B", "C", "D"], q_data["list_i_en"])])
    list_i_ta_str = "\n".join([f"{letter}. {text}" for letter, text in zip(["A", "B", "C", "D"], q_data["list_i_ta"])])
    
    list_ii_en_str = "\n".join([f"{num}. {text}" for num, text in zip(["1", "2", "3", "4"], q_data["list_ii_en"])])
    list_ii_ta_str = "\n".join([f"{num}. {text}" for num, text in zip(["1", "2", "3", "4"], q_data["list_ii_ta"])])
    
    q_en_text = f"Match List I with List II and select the correct answer using the codes given below:\n\nList I\n{list_i_en_str}\n\nList II\n{list_ii_en_str}"
    q_ta_text = f"பட்டியல் I-ஐ பட்டியல் II உடன் பொருத்தி கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான பதிலைத் தேர்ந்தெடுக்கவும்:\n\nபட்டியல் I\n{list_i_ta_str}\n\nபட்டியல் II\n{list_ii_ta_str}"
    
    obj = {
        "id": q_id,
        "subject": q_data["subject"],
        "topic": q_data["topic"],
        "difficulty": q_data["difficulty"],
        "question_type": q_data["question_type"],
        "question": {
            "en": q_en_text,
            "ta": q_ta_text
        },
        "options": options_arr,
        "correct_answer": correct_ans_id,
        "explanation": {
            "en": q_data["explanation_en"],
            "ta": q_data["explanation_ta"]
        },
        "why_not_others": why_not_others_dict,
        "tnpsc_tip": {
            "en": q_data["tnpsc_tip_en"],
            "ta": q_data["tnpsc_tip_ta"]
        },
        "revision_fact": {
            "en": q_data["revision_fact_en"],
            "ta": q_data["revision_fact_ta"]
        },
        "source_reference": [
            "M. Laxmikanth - Indian Polity",
            "NCERT Class XI/XII - Indian Constitution at Work",
            "Samacheer Kalvi - Standard 11/12 Political Science"
        ],
        "bloom_level": q_data["bloom_level"],
        "estimated_time_sec": 75,
        "pyq_similarity": "High",
        "tags": q_data["tags"],
        "question_en": q_en_text,
        "question_ta": q_ta_text,
        "options_en": options_en_arr,
        "options_ta": options_ta_arr,
        "answer": correct_ans_id.lower(),
        "explanation_en": q_data["explanation_en"],
        "explanation_ta": q_data["explanation_ta"]
    }
    
    final_questions.append(obj)

# Ensure output directory exists
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

# Write output file
with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(final_questions, f, ensure_ascii=False, indent=2)

print(f"Successfully generated {len(final_questions)} questions at {OUTPUT_PATH}")

# Print answer distribution
ans_counts = {}
for q in final_questions:
    ans = q["correct_answer"]
    ans_counts[ans] = ans_counts.get(ans, 0) + 1
print("Answer distribution:", ans_counts)
