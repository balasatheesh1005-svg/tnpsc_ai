# -*- coding: utf-8 -*-
"""
Co-operative Societies - Part 2B: Chronology MCQs (25 Questions: CS_C_001 to CS_C_025)
TNPSC Nova AI Content Engine
Enforces strict ChronologyValidator rules:
- 4 numbered events (1, 2, 3, 4) in stem in non-chronological order
- Correct sequence != 1-2-3-4
- Options are unique permutations of [1, 2, 3, 4]
- Explanations explicitly teach chronology with dates/years and '→' sequences
"""
import os
import json
from collections import Counter
from tools.nova_content_engine.answer_randomizer import randomize_and_balance_dataset
from tools.nova_content_engine.chronology_validator import ChronologyValidator
from tools.nova_content_engine.validator import ContentValidator
from cooperative_societies_mcq_helper import make_coop_q


def get_chronology_raw_questions():
    return [
        # CS_C_001: Early Legislative Evolution
        {
            "subtopic": "Early Legislative History",
            "stem_en": "Arrange the following historic events in the early cooperative movement of British India in chronological order:\n1. Co-operative Societies Act (Act II of 1912)\n2. Sir Frederick Nicholson's report advising 'Find Raiffeisen'\n3. Bombay Co-operative Societies Act passed by provincial legislature\n4. Enactment of the first Co-operative Credit Societies Act",
            "stem_ta": "பிரிட்டிஷ் இந்தியாவின் ஆரம்பகால கூட்டுறவு இயக்கத்தின் பின்வரும் வரலாற்று நிகழ்வுகளை காலவரிசைப்படி ஒழுங்குபடுத்துக:\n1. கூட்டுறவு சங்கங்கள் சட்டம் (Act II of 1912)\n2. 'ரைஃபெய்சனைக் கண்டறியுங்கள்' எனப் பரிந்துரைத்த சர் பிரடெரிக் நிக்கல்சனின் அறிக்கை\n3. பம்பாய் மாகாண சட்டமன்றத்தால் இயற்றப்பட்ட பம்பாய் கூட்டுறவு சங்கங்கள் சட்டம்\n4. முதல் கூட்டுறவு கடன் சங்கங்கள் சட்டம் இயற்றப்படுதல்",
            "options": [
                ("2 - 4 - 1 - 3", "2 - 4 - 1 - 3"),
                ("4 - 2 - 1 - 3", "4 - 2 - 1 - 3"),
                ("2 - 1 - 4 - 3", "2 - 1 - 4 - 3"),
                ("3 - 1 - 4 - 2", "3 - 1 - 4 - 2")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order of events is 2 → 4 → 1 → 3:\n- 2. Sir Frederick Nicholson's report (1895)\n- 4. First Co-operative Credit Societies Act (1904)\n- 1. Co-operative Societies Act allowing non-credit societies (1912)\n- 3. Bombay Co-operative Societies Act (1925).\nHence, the correct sequence is 2 - 4 - 1 - 3.",
            "exp_ta": "நிகழ்வுகளின் சரியான காலவரிசை 2 → 4 → 1 → 3:\n- 2. சர் பிரடெரிக் நிக்கல்சன் அறிக்கை (1895)\n- 4. முதல் கூட்டுறவு கடன் சங்கங்கள் சட்டம் (1904)\n- 1. கடன் அல்லாத சங்கங்களை அனுமதித்த கூட்டுறவு சங்கங்கள் சட்டம் (1912)\n- 3. பம்பாய் கூட்டுறவு சங்கங்கள் சட்டம் (1925).\nஎனவே, சரியான வரிசை 2 - 4 - 1 - 3 ஆகும்.",
            "why_a_en": "Correct sequence: 1895 (Nicholson) → 1904 (Credit Act) → 1912 (Act II) → 1925 (Bombay Act).",
            "why_a_ta": "சரியான காலவரிசை: 1895 (நிக்கல்சன்) → 1904 (கடன் சட்டம்) → 1912 (சட்டம் II) → 1925 (பம்பாய் சட்டம்).",
            "why_b_en": "Incorrect. Nicholson's report (1895) preceded the 1904 Act.",
            "why_b_ta": "தவறு. 1904 சட்டத்திற்கு முன்பே 1895-ல் நிக்கல்சன் அறிக்கை வெளியானது.",
            "why_c_en": "Incorrect. 1904 Act preceded the 1912 Act.",
            "why_c_ta": "தவறு. 1912 சட்டத்திற்கு முன்பே 1904 சட்டம் வந்தது.",
            "why_d_en": "Incorrect. Bombay Act (1925) was the last of these events.",
            "why_d_ta": "தவறு. பம்பாய் சட்டம் (1925) இறுதியானது.",
            "tip_en": "Chronology tip: 1895 (Nicholson) → 1904 (Act) → 1912 (Act) → 1925 (Bombay Act).",
            "tip_ta": "காலவரிசை குறிப்பு: 1895 (நிக்கல்சன்) → 1904 → 1912 → 1925 (பம்பாய்).",
            "fact_en": "Nicholson studied rural agricultural banks across Germany and Italy before submitting his report in 1895.",
            "fact_ta": "நிக்கல்சன் 1895-ல் அறிக்கை சமர்ப்பிக்கும் முன் ஜெர்மனி மற்றும் இத்தாலியின் கூட்டுறவு வங்கிகளை நேரில் ஆய்வு செய்தார்."
        },

        # CS_C_002: National Committees on Cooperatives
        {
            "subtopic": "Committees Chronology",
            "stem_en": "Arrange the following national committees on cooperative societies in chronological order of their constitution / report:\n1. Choudhary Brahm Perkash Committee on Model Co-operatives Act\n2. All India Rural Credit Survey Committee (Gorwala Committee)\n3. Prof. A. Vaidyanathan Task Force on Rural Cooperative Credit\n4. Ram Niwas Mirdha Committee on Cooperatives",
            "stem_ta": "கூட்டுறவு சங்கங்கள் மீதான பின்வரும் தேசியக் குழுக்களை அவை அமைக்கப்பட்ட / அறிக்கை அளித்த காலவரிசைப்படி ஒழுங்குபடுத்துக:\n1. மாதிரி கூட்டுறவு சட்டம் குறித்த சவுத்ரி பிரம்ம பிரகாஷ் குழு\n2. அகில இந்திய கிராமப்புற கடன் ஆய்வுக் குழு (கோர்வாலா குழு)\n3. கிராமப்புற கூட்டுறவு கடன் மீதான பேராசிரியர் ஏ. வைத்தியநாதன் பணிக்குழு\n4. கூட்டுறவு மீதான ராம் நிவாஸ் மிர்தா குழு",
            "options": [
                ("2 - 4 - 1 - 3", "2 - 4 - 1 - 3"),
                ("4 - 2 - 1 - 3", "4 - 2 - 1 - 3"),
                ("2 - 1 - 4 - 3", "2 - 1 - 4 - 3"),
                ("1 - 2 - 4 - 3", "1 - 2 - 4 - 3")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order of the committees is 2 → 4 → 1 → 3:\n- 2. All India Rural Credit Survey Committee / Gorwala (1954)\n- 4. Ram Niwas Mirdha Committee (1965)\n- 1. Choudhary Brahm Perkash Committee (1991)\n- 3. Prof. A. Vaidyanathan Task Force (2004).\nHence, the correct sequence is 2 - 4 - 1 - 3.",
            "exp_ta": "இக்குழுக்களின் சரியான காலவரிசை 2 → 4 → 1 → 3:\n- 2. அகில இந்திய கிராமப்புற கடன் ஆய்வுக் குழு / கோர்வாலா (1954)\n- 4. ராம் நிவாஸ் மிர்தா குழு (1965)\n- 1. சவுத்ரி பிரம்ம பிரகாஷ் குழு (1991)\n- 3. பேராசிரியர் ஏ. வைத்தியநாதன் பணிக்குழு (2004).\nஎனவே, சரியான வரிசை 2 - 4 - 1 - 3 ஆகும்.",
            "why_a_en": "Correct sequence: 1954 (Gorwala) → 1965 (Mirdha) → 1991 (Brahm Perkash) → 2004 (Vaidyanathan).",
            "why_a_ta": "சரியான காலவரிசை: 1954 (கோர்வாலா) → 1965 (மிர்தா) → 1991 (பிரம்ம பிரகாஷ்) → 2004 (வைத்தியநாதன்).",
            "why_b_en": "Incorrect. Gorwala Committee (1954) preceded Mirdha Committee (1965).",
            "why_b_ta": "தவறு. 1965 மிர்தா குழுவிற்கு முன்பே 1954 கோர்வாலா குழு அமைந்தது.",
            "why_c_en": "Incorrect. Mirdha Committee (1965) preceded Brahm Perkash (1991).",
            "why_c_ta": "தவறு. பிரம்ம பிரகாஷ் குழுவிற்கு முன் மிர்தா குழு அறிக்கை அளித்தது.",
            "why_d_en": "Incorrect. Brahm Perkash was in 1991, not before Gorwala (1954).",
            "why_d_ta": "தவறு. பிரம்ம பிரகாஷ் 1991-ல் அமைந்தது.",
            "tip_en": "Committee sequence: Gorwala (1954) → Mirdha (1965) → Brahm Perkash (1991) → Vaidyanathan (2004).",
            "tip_ta": "குழுக்களின் வரிசை: கோர்வாலா (1954) → மிர்தா (1965) → பிரம்ம பிரகாஷ் (1991) → வைத்தியநாதன் (2004).",
            "fact_en": "All four committees fundamentally shaped post-independence cooperative policy in India.",
            "fact_ta": "இந்நான்கு குழுக்களுமே சுதந்திரத்திற்குப் பிந்தைய இந்தியக் கூட்டுறவுக் கொள்கைகளை வடிவமைத்தன."
        },

        # CS_C_003: Dairy Movement & Operation Flood
        {
            "subtopic": "Dairy Movement Milestones",
            "stem_en": "Arrange the following milestones in the Indian dairy cooperative movement in chronological order:\n1. Founding of Kaira District Co-operative Milk Producers' Union (Amul)\n2. Establishment of the National Dairy Development Board (NDDB)\n3. Creation of the Union Ministry of Cooperation\n4. Launch of Operation Flood Phase-I under Dr. Verghese Kurien",
            "stem_ta": "இந்திய பால்வளக் கூட்டுறவு இயக்கத்தின் பின்வரும் மைல்கற்களை காலவரிசைப்படி ஒழுங்குபடுத்துக:\n1. கைரா மாவட்ட கூட்டுறவு பால் உற்பத்தியாளர்கள் ஒன்றியம் (அமுல்) நிறுவப்படுதல்\n2. தேசிய பால்வள மேம்பாட்டு வாரியம் (NDDB) நிறுவப்படுதல்\n3. மத்திய கூட்டுறவு அமைச்சகம் உருவாக்கப்படுதல்\n4. டாக்டர் வர்கீஸ் குரியன் தலைமையில் ஆபரேஷன் பிளட் கட்டம்-I தொடங்கப்படுதல்",
            "options": [
                ("1 - 2 - 4 - 3", "1 - 2 - 4 - 3"),
                ("2 - 1 - 4 - 3", "2 - 1 - 4 - 3"),
                ("1 - 4 - 2 - 3", "1 - 4 - 2 - 3"),
                ("4 - 1 - 2 - 3", "4 - 1 - 2 - 3")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is 1 → 2 → 4 → 3:\n- 1. Founding of Kaira Union / Amul (1946)\n- 2. Establishment of NDDB at Anand (1965)\n- 4. Launch of Operation Flood Phase-I (1970)\n- 3. Creation of Ministry of Cooperation (2021).\nHence, the correct sequence is 1 - 2 - 4 - 3.",
            "exp_ta": "சரியான காலவரிசை 1 → 2 → 4 → 3:\n- 1. கைரா ஒன்றியம் / அமுல் தொடக்கம் (1946)\n- 2. ஆனந்த் நகரில் NDDB நிறுவப்படுதல் (1965)\n- 4. ஆபரேஷன் பிளட் கட்டம்-I தொடக்கம் (1970)\n- 3. தனி கூட்டுறவு அமைச்சகம் உருவாக்கம் (2021).\nஎனவே, சரியான வரிசை 1 - 2 - 4 - 3 ஆகும்.",
            "why_a_en": "Correct sequence: 1946 (Amul) → 1965 (NDDB) → 1970 (Operation Flood) → 2021 (Ministry).",
            "why_a_ta": "சரியான காலவரிசை: 1946 (அமுல்) → 1965 (NDDB) → 1970 (வெண்மைப் புரட்சி) → 2021 (அமைச்சகம்).",
            "why_b_en": "Incorrect. Amul was founded in 1946, well before NDDB was created in 1965.",
            "why_b_ta": "தவறு. 1965 NDDB உருவாக்கத்திற்கு முன்பே 1946-ல் அமுல் தொடங்கியது.",
            "why_c_en": "Incorrect. NDDB (1965) was created before Operation Flood (1970).",
            "why_c_ta": "தவறு. ஆபரேஷன் பிளட்டிற்கு முன்பே NDDB தொடங்கப்பட்டது.",
            "why_d_en": "Incorrect. Operation Flood was in 1970, not before Amul (1946).",
            "why_d_ta": "தவறு. 1946 அமுலுக்குப் பிறகே ஆபரேஷன் பிளட் வந்தது.",
            "tip_en": "Dairy timeline: 1946 (Amul) → 1965 (NDDB) → 1970 (Operation Flood) → 2021 (Ministry).",
            "tip_ta": "பால்வள காலக்கோடு: 1946 (அமுல்) → 1965 (NDDB) → 1970 (ஆபரேஷன் பிளட்) → 2021 (அமைச்சகம்).",
            "fact_en": "Prime Minister Lal Bahadur Shastri visited Anand in 1964 and directed the creation of NDDB to replicate the Anand pattern across India.",
            "fact_ta": "1964-ல் ஆனந்த் சென்ற பிரதமர் லால் பகதூர் சாஸ்திரி நாடு முழுவதும் ஆனந்த் மாதிரியைப் பரப்ப NDDB-ஐ உருவாக்க உத்தரவிட்டார்."
        },

        # CS_C_004: Constitutional Amendments Sequence
        {
            "subtopic": "Constitutional Amendments",
            "stem_en": "Arrange the following Constitutional Amendment Acts in chronological order of their enactment:\n1. 97th Constitutional Amendment Act (Part IX-B Co-operative Societies)\n2. 73rd Constitutional Amendment Act (Part IX Panchayats)\n3. 42nd Constitutional Amendment Act (Inserted Article 43A)\n4. 44th Constitutional Amendment Act (Right to Property removed as Fundamental Right)",
            "stem_ta": "பின்வரும் அரசியலமைப்பு திருத்தச் சட்டங்களை அவை இயற்றப்பட்ட காலவரிசைப்படி ஒழுங்குபடுத்துக:\n1. 97-வது அரசியலமைப்பு திருத்தச் சட்டம் (பகுதி IX-B கூட்டுறவு சங்கங்கள்)\n2. 73-வது அரசியலமைப்பு திருத்தச் சட்டம் (பகுதி IX பஞ்சாயத்துகள்)\n3. 42-வது அரசியலமைப்பு திருத்தச் சட்டம் (உறுப்பு 43A சேர்க்கப்பட்டது)\n4. 44-வது அரசியலமைப்பு திருத்தச் சட்டம் (சொத்துரிமை அடிப்படை உரிமையிலிருந்து நீக்கப்பட்டது)",
            "options": [
                ("3 - 4 - 2 - 1", "3 - 4 - 2 - 1"),
                ("4 - 3 - 2 - 1", "4 - 3 - 2 - 1"),
                ("3 - 2 - 4 - 1", "3 - 2 - 4 - 1"),
                ("2 - 3 - 4 - 1", "2 - 3 - 4 - 1")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order of the Amendments is 3 → 4 → 2 → 1:\n- 3. 42nd Constitutional Amendment Act (1976)\n- 4. 44th Constitutional Amendment Act (1978)\n- 2. 73rd Constitutional Amendment Act (1992)\n- 1. 97th Constitutional Amendment Act (2011).\nHence, the correct sequence is 3 - 4 - 2 - 1.",
            "exp_ta": "அரசியலமைப்பு திருத்தங்களின் சரியான காலவரிசை 3 → 4 → 2 → 1:\n- 3. 42-வது திருத்தச் சட்டம் (1976)\n- 4. 44-வது திருத்தச் சட்டம் (1978)\n- 2. 73-வது திருத்தச் சட்டம் (1992)\n- 1. 97-வது திருத்தச் சட்டம் (2011).\nஎனவே, சரியான வரிசை 3 - 4 - 2 - 1 ஆகும்.",
            "why_a_en": "Correct sequence: 1976 (42nd) → 1978 (44th) → 1992 (73rd) → 2011 (97th).",
            "why_a_ta": "சரியான காலவரிசை: 1976 (42வது) → 1978 (44வது) → 1992 (73வது) → 2011 (97வது).",
            "why_b_en": "Incorrect. 42nd CAA (1976) preceded 44th CAA (1978).",
            "why_b_ta": "தவறு. 44வது திருத்தத்திற்கு (1978) முன்பே 42வது திருத்தம் (1976) வந்தது.",
            "why_c_en": "Incorrect. 44th CAA (1978) preceded 73rd CAA (1992).",
            "why_c_ta": "தவறு. 73வது திருத்தத்திற்கு முன்பே 44வது திருத்தம் வந்தது.",
            "why_d_en": "Incorrect. 73rd CAA was in 1992, not before 1976.",
            "why_d_ta": "தவறு. 73வது திருத்தம் 1992-ல் வந்தது.",
            "tip_en": "Constitutional Amendment sequence: 42nd (1976) → 44th (1978) → 73rd/74th (1992) → 97th (2011).",
            "tip_ta": "திருத்தங்களின் வரிசை: 42வது (1976) → 44வது (1978) → 73வது (1992) → 97வது (2011).",
            "fact_en": "Articles 43A (workers participation) and 43B (cooperatives) were inserted 35 years apart (1976 vs 2011).",
            "fact_ta": "உறுப்புகள் 43A (1976) மற்றும் 43B (2011) ஆகியவை 35 ஆண்டுகள் இடைவெளியில் சேர்க்கப்பட்டன."
        },

        # CS_C_005: Agricultural Financing Institutions
        {
            "subtopic": "Financial Institutions Chronology",
            "stem_en": "Arrange the following agricultural and cooperative financial institutions in chronological order of their establishment:\n1. State Bank of India (SBI)\n2. National Bank for Agriculture and Rural Development (NABARD)\n3. Reserve Bank of India (RBI)\n4. Multi-State Co-operative Societies Act enacted by Parliament",
            "stem_ta": "பின்வரும் விவசாய மற்றும் கூட்டுறவு நிதி நிறுவனங்களை அவை நிறுவப்பட்ட காலவரிசைப்படி ஒழுங்குபடுத்துக:\n1. பாரத ஸ்டேட் வங்கி (SBI)\n2. விவசாயம் மற்றும் ஊரக வளர்ச்சிக்கான தேசிய வங்கி (NABARD)\n3. இந்திய ரிசர்வ் வங்கி (RBI)\n4. நாடாளுமன்றத்தால் பல மாநில கூட்டுறவு சங்கங்கள் சட்டம் இயற்றப்படுதல்",
            "options": [
                ("3 - 1 - 2 - 4", "3 - 1 - 2 - 4"),
                ("1 - 3 - 2 - 4", "1 - 3 - 2 - 4"),
                ("3 - 2 - 1 - 4", "3 - 2 - 1 - 4"),
                ("2 - 3 - 1 - 4", "2 - 3 - 1 - 4")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is 3 → 1 → 2 → 4:\n- 3. Reserve Bank of India established (1935)\n- 1. State Bank of India formed from Imperial Bank (1955)\n- 2. NABARD established on Sivaraman Committee recommendation (1982)\n- 4. Multi-State Co-operative Societies Act enacted (2002).\nHence, the correct sequence is 3 - 1 - 2 - 4.",
            "exp_ta": "சரியான காலவரிசை 3 → 1 → 2 → 4:\n- 3. இந்திய ரிசர்வ் வங்கி நிறுவப்படுதல் (1935)\n- 1. பாரத ஸ்டேட் வங்கி (SBI) உருவாக்கப்படுதல் (1955)\n- 2. நபார்டு (NABARD) வங்கி நிறுவப்படுதல் (1982)\n- 4. பல மாநில கூட்டுறவு சங்கங்கள் சட்டம் இயற்றப்படுதல் (2002).\nஎனவே, சரியான வரிசை 3 - 1 - 2 - 4 ஆகும்.",
            "why_a_en": "Correct sequence: 1935 (RBI) → 1955 (SBI) → 1982 (NABARD) → 2002 (MSCS Act).",
            "why_a_ta": "சரியான காலவரிசை: 1935 (RBI) → 1955 (SBI) → 1982 (NABARD) → 2002 (MSCS சட்டம்).",
            "why_b_en": "Incorrect. RBI (1935) was established before SBI (1955).",
            "why_b_ta": "தவறு. 1955 SBI-க்கு முன்பே 1935-ல் ரிசர்வ் வங்கி உருவானது.",
            "why_c_en": "Incorrect. SBI (1955) preceded NABARD (1982).",
            "why_c_ta": "தவறு. நபார்டு வங்கிக்கு முன்பே SBI உருவானது.",
            "why_d_en": "Incorrect. NABARD was in 1982, not the first.",
            "why_d_ta": "தவறு. நபார்டு 1982-ல் உருவானது.",
            "tip_en": "Banking Institutional Timeline: RBI (1935) → SBI (1955) → NABARD (1982) → MSCS Act (2002).",
            "tip_ta": "வங்கி காலக்கோடு: RBI (1935) → SBI (1955) → நபார்டு (1982) → MSCS சட்டம் (2002).",
            "fact_en": "NABARD took over the Agricultural Credit Department (ACD) from RBI on 12 July 1982.",
            "fact_ta": "நபார்டு 1982 ஜூலை 12 அன்று ரிசர்வ் வங்கியின் விவசாயக் கடன் துறையை ஏற்றுக்கொண்டது."
        }
    ]


def get_chronology_questions_batch2():
    return [
        # CS_C_006: Tamil Nadu Cooperative Milestones
        {
            "subtopic": "Tamil Nadu Cooperative History",
            "stem_en": "Arrange the following historic milestones in Tamil Nadu's cooperative history in chronological order:\n1. Tamil Nadu Co-operative Societies Act (Act 30 of 1983) passed\n2. Founding of Triplicane Urban Co-operative Society (TUCS)\n3. Establishment of Co-optex (Madras Handloom Weavers' Society)\n4. Enactment of Madras Co-operative Societies Act (Act VI of 1932)",
            "stem_ta": "தமிழ்நாட்டின் கூட்டுறவு வரலாற்றின் பின்வரும் மைல்கற்களை காலவரிசைப்படி ஒழுங்குபடுத்துக:\n1. தமிழ்நாடு கூட்டுறவு சங்கங்கள் சட்டம் (Act 30 of 1983) இயற்றப்படுதல்\n2. திருவல்லிக்கேணி நகர்ப்புற கூட்டுறவு சங்கம் (TUCS) தொடங்கப்படுதல்\n3. கோ-ஆப்லெக்ஸ் (மெட்ராஸ் கைத்தறி நெசவாளர் சங்கம்) நிறுவப்படுதல்\n4. மெட்ராஸ் கூட்டுறவு சங்கங்கள் சட்டம் (Act VI of 1932) இயற்றப்படுதல்",
            "options": [
                ("2 - 4 - 3 - 1", "2 - 4 - 3 - 1"),
                ("2 - 3 - 4 - 1", "2 - 3 - 4 - 1"),
                ("4 - 2 - 3 - 1", "4 - 2 - 3 - 1"),
                ("2 - 4 - 1 - 3", "2 - 4 - 1 - 3")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is 2 → 4 → 3 → 1:\n- 2. TUCS founded in Chennai (1904)\n- 4. Madras Co-operative Societies Act (1932)\n- 3. Establishment of Co-optex (1935)\n- 1. Tamil Nadu Co-operative Societies Act enacted (1983).\nHence, the correct sequence is 2 - 4 - 3 - 1.",
            "exp_ta": "சரியான காலவரிசை 2 → 4 → 3 → 1:\n- 2. சென்னையில் TUCS நுகர்வோர் சங்கம் தொடக்கம் (1904)\n- 4. மெட்ராஸ் கூட்டுறவு சங்கங்கள் சட்டம் (1932)\n- 3. கோ-ஆப்லெக்ஸ் அமைப்பு நிறுவப்படுதல் (1935)\n- 1. தமிழ்நாடு கூட்டுறவு சங்கங்கள் சட்டம் இயற்றப்படுதல் (1983).\nஎனவே, சரியான வரிசை 2 - 4 - 3 - 1 ஆகும்.",
            "why_a_en": "Correct sequence: 1904 (TUCS) → 1932 (Madras Act) → 1935 (Co-optex) → 1983 (TN Act).",
            "why_a_ta": "சரியான காலவரிசை: 1904 (TUCS) → 1932 (மெட்ராஸ் சட்டம்) → 1935 (கோ-ஆப்லெக்ஸ்) → 1983 (தமிழக சட்டம்).",
            "why_b_en": "Incorrect. Madras Act (1932) was passed before Co-optex (1935).",
            "why_b_ta": "தவறு. கோ-ஆப்லெக்ஸ் அமைப்பிற்கு முன்பே 1932-ல் மெட்ராஸ் சட்டம் இயற்றப்பட்டது.",
            "why_c_en": "Incorrect. TUCS (1904) is the oldest event.",
            "why_c_ta": "தவறு. TUCS (1904) எல்லாவற்றிற்கும் முந்தையது.",
            "why_d_en": "Incorrect. TN Act was enacted in 1983, after Co-optex (1935).",
            "why_d_ta": "தவறு. தமிழக சட்டம் 1983-ல் இயற்றப்பட்டது.",
            "tip_en": "Tamil Nadu Cooperative History: 1904 (TUCS) → 1932 (Madras Act) → 1935 (Co-optex) → 1983 (Current Act).",
            "tip_ta": "தமிழகக் கூட்டுறவு காலக்கோடு: 1904 (TUCS) → 1932 (மெட்ராஸ் சட்டம்) → 1935 (கோ-ஆப்லெக்ஸ்) → 1983 (தற்போதைய சட்டம்).",
            "fact_en": "The 1983 Act came into force across Tamil Nadu on 13 April 1988.",
            "fact_ta": "1983-ஆம் ஆண்டு சட்டம் தமிழ்நாடு முழுவதும் 1988 ஏப்ரல் 13 அன்று நடைமுறைக்கு வந்தது."
        },

        # CS_C_007: National Cooperative Federations
        {
            "subtopic": "National Federations Chronology",
            "stem_en": "Arrange the following apex national cooperative federations in chronological order of their establishment:\n1. Indian Farmers Fertiliser Cooperative Limited (IFFCO)\n2. National Agricultural Cooperative Marketing Federation of India (NAFED)\n3. National Cooperative Development Corporation (NCDC)\n4. Krishak Bharati Cooperative Limited (KRIBHCO)",
            "stem_ta": "பின்வரும் தேசிய உச்ச கூட்டுறவு கூட்டமைப்புகளை அவை நிறுவப்பட்ட காலவரிசைப்படி ஒழுங்குபடுத்துக:\n1. இந்திய விவசாயிகள் உரக் கூட்டுறவு நிறுவனம் (IFFCO)\n2. இந்திய தேசிய வேளாண்மை கூட்டுறவு சந்தைப்படுத்தல் கூட்டமைப்பு (NAFED)\n3. தேசிய கூட்டுறவு மேம்பாட்டுக் கழகம் (NCDC)\n4. கிரிஷக் பாரதி கூட்டுறவு நிறுவனம் (KRIBHCO)",
            "options": [
                ("2 - 3 - 1 - 4", "2 - 3 - 1 - 4"),
                ("3 - 2 - 1 - 4", "3 - 2 - 1 - 4"),
                ("2 - 1 - 3 - 4", "2 - 1 - 3 - 4"),
                ("1 - 2 - 3 - 4", "1 - 2 - 3 - 4")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is 2 → 3 → 1 → 4:\n- 2. NAFED established (2 October 1958)\n- 3. NCDC set up under statute (March 1963)\n- 1. IFFCO registered (3 November 1967)\n- 4. KRIBHCO established (17 April 1980).\nHence, the correct sequence is 2 - 3 - 1 - 4.",
            "exp_ta": "சரியான காலவரிசை 2 → 3 → 1 → 4:\n- 2. NAFED நிறுவப்படுதல் (2 அக்டோபர் 1958)\n- 3. NCDC சட்டப்பூர்வமாக உருவாக்கப்படுதல் (மார்ச் 1963)\n- 1. IFFCO பதிவு செய்யப்படுதல் (3 நவம்பர் 1967)\n- 4. KRIBHCO நிறுவப்படுதல் (17 ஏப்ரல் 1980).\nஎனவே, சரியான வரிசை 2 - 3 - 1 - 4 ஆகும்.",
            "why_a_en": "Correct sequence: 1958 (NAFED) → 1963 (NCDC) → 1967 (IFFCO) → 1980 (KRIBHCO).",
            "why_a_ta": "சரியான காலவரிசை: 1958 (NAFED) → 1963 (NCDC) → 1967 (IFFCO) → 1980 (KRIBHCO).",
            "why_b_en": "Incorrect. NAFED (1958) was established before NCDC (1963).",
            "why_b_ta": "தவறு. NCDC-க்கு முன்பே NAFED 1958-ல் உருவானது.",
            "why_c_en": "Incorrect. NCDC (1963) preceded IFFCO (1967).",
            "why_c_ta": "தவறு. இஃப்கோவிற்கு முன்பே NCDC உருவானது.",
            "why_d_en": "Incorrect. IFFCO was in 1967, not first.",
            "why_d_ta": "தவறு. இஃப்கோ 1967-ல் உருவானது.",
            "tip_en": "National Federations Timeline: NAFED (1958) → NCDC (1963) → IFFCO (1967) → KRIBHCO (1980).",
            "tip_ta": "தேசிய கூட்டமைப்புகள் காலக்கோடு: NAFED (1958) → NCDC (1963) → IFFCO (1967) → KRIBHCO (1980).",
            "fact_en": "Both IFFCO and KRIBHCO were promoted with government equity which was later fully retired by the cooperatives.",
            "fact_ta": "இஃப்கோ மற்றும் கிரிப்கோ இரண்டும் பின்னர் அரசுப் பங்குகளை முழுமையாகத் திருப்பிச் செலுத்தி முழு தன்னாட்சி பெற்றன."
        },

        # CS_C_008: Constitutional Landmarks on Federalism
        {
            "subtopic": "Federal Jurisprudence Chronology",
            "stem_en": "Arrange the following landmark Supreme Court judgments touching federalism and basic structure in chronological order:\n1. Union of India v. Rajendra N. Shah (Part IX-B unconstitutional for State cooperatives)\n2. Kesavananda Bharati v. State of Kerala (Basic Structure Doctrine established)\n3. Minerva Mills v. Union of India (Directive Principles cannot destroy Fundamental Rights)\n4. S.R. Bommai v. Union of India (Federalism held an integral part of Basic Structure)",
            "stem_ta": "கூட்டாட்சி மற்றும் அடிப்படைக் கட்டமைப்பு தொடர்பான பின்வரும் உச்சநீதிமன்றத்தின் வரலாற்றுத் தீர்ப்புகளை காலவரிசைப்படி ஒழுங்குபடுத்துக:\n1. இந்திய ஒன்றியம் எதிர் ராஜேந்திர என். ஷா (மாநிலக் கூட்டுறவுகளுக்கு பகுதி IX-B செல்லாது)\n2. கேசவானந்த பாரதி எதிர் கேரள அரசு (அடிப்படை கட்டமைப்பு தத்துவம் உருவாக்கப்பட்டது)\n3. மினர்வா மில்ஸ் எதிர் இந்திய ஒன்றியம் (வழிகாட்டு நெறிமுறைகள் அடிப்படை உரிமைகளை அழிக்க முடியாது)\n4. எஸ்.ஆர். பொம்மை எதிர் இந்திய ஒன்றியம் (கூட்டாட்சி என்பது அடிப்படைக் கட்டமைப்பின் பிரிக்க முடியாத பகுதி)",
            "options": [
                ("2 - 3 - 4 - 1", "2 - 3 - 4 - 1"),
                ("3 - 2 - 4 - 1", "3 - 2 - 4 - 1"),
                ("2 - 4 - 3 - 1", "2 - 4 - 3 - 1"),
                ("4 - 2 - 3 - 1", "4 - 2 - 3 - 1")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order of the judgments is 2 → 3 → 4 → 1:\n- 2. Kesavananda Bharati (1973)\n- 3. Minerva Mills (1980)\n- 4. S.R. Bommai (1994)\n- 1. Union of India v. Rajendra N. Shah (2021).\nHence, the correct sequence is 2 - 3 - 4 - 1.",
            "exp_ta": "வழக்குகளின் சரியான காலவரிசை 2 → 3 → 4 → 1:\n- 2. கேசவானந்த பாரதி (1973)\n- 3. மினர்வா மில்ஸ் (1980)\n- 4. எஸ்.ஆர். பொம்மை (1994)\n- 1. இந்திய ஒன்றியம் எதிர் ராஜேந்திர என். ஷா (2021).\nஎனவே, சரியான வரிசை 2 - 3 - 4 - 1 ஆகும்.",
            "why_a_en": "Correct sequence: 1973 (Kesavananda) → 1980 (Minerva) → 1994 (Bommai) → 2021 (Rajendra Shah).",
            "why_a_ta": "சரியான காலவரிசை: 1973 (கேசவானந்தா) → 1980 (மினர்வா) → 1994 (பொம்மை) → 2021 (ராஜேந்திர ஷா).",
            "why_b_en": "Incorrect. Kesavananda (1973) preceded Minerva Mills (1980).",
            "why_b_ta": "தவறு. 1980 மினர்வா மில்ஸிற்கு முன்பே 1973 கேசவானந்த பாரதி வந்தது.",
            "why_c_en": "Incorrect. Minerva Mills (1980) preceded Bommai (1994).",
            "why_c_ta": "தவறு. பொம்மை வழக்கிற்கு முன்பே மினர்வா மில்ஸ் வந்தது.",
            "why_d_en": "Incorrect. Bommai was decided in 1994, not first.",
            "why_d_ta": "தவறு. பொம்மை வழக்கு 1994-ல் தீர்ப்பளிக்கப்பட்டது.",
            "tip_en": "Landmark Benchmarks: 1973 (Kesavananda) → 1980 (Minerva) → 1994 (Bommai) → 2021 (Cooperative case).",
            "tip_ta": "முக்கிய வழக்குகள்: 1973 (கேசவானந்தா) → 1980 (மினர்வா) → 1994 (பொம்மை) → 2021 (கூட்டுறவு வழக்கு).",
            "fact_en": "The Rajendra N. Shah bench cited both Kesavananda and Bommai in its analysis of Article 368(2).",
            "fact_ta": "ராஜேந்திர ஷா அமர்வு உறுப்பு 368(2) ஆய்வில் கேசவானந்தா மற்றும் பொம்மை வழக்குகளை மேற்கோள் காட்டியது."
        },

        # CS_C_009: 97th Amendment Journey
        {
            "subtopic": "97th CAA Milestones",
            "stem_en": "Arrange the following events in the life cycle of the 97th Constitutional Amendment in chronological order:\n1. Supreme Court judgment in Union of India v. Rajendra N. Shah\n2. Passing of the 97th Constitutional Amendment Act by Parliament\n3. Notification of the 97th Amendment coming into force (15 February)\n4. Gujarat High Court judgment striking down Part IX-B",
            "stem_ta": "97-வது அரசியலமைப்புத் திருத்தத்தின் வாழ்க்கைச் சுழற்சியில் பின்வரும் நிகழ்வுகளை காலவரிசைப்படி ஒழுங்குபடுத்துக:\n1. இந்திய ஒன்றியம் எதிர் ராஜேந்திர என். ஷா வழக்கில் உச்சநீதிமன்றத் தீர்ப்பு\n2. நாடாளுமன்றத்தால் 97-வது அரசியலமைப்புத் திருத்தச் சட்டம் நிறைவேற்றப்படுதல்\n3. 97-வது திருத்தம் நடைமுறைக்கு வந்த அதிகாரப்பூர்வ நாள் (பிப்ரவரி 15)\n4. பகுதி IX-B-ஐ ரத்து செய்த குஜராத் உயர் நீதிமன்றத் தீர்ப்பு",
            "options": [
                ("2 - 3 - 4 - 1", "2 - 3 - 4 - 1"),
                ("3 - 2 - 4 - 1", "3 - 2 - 4 - 1"),
                ("2 - 4 - 3 - 1", "2 - 4 - 3 - 1"),
                ("4 - 2 - 3 - 1", "4 - 2 - 3 - 1")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is 2 → 3 → 4 → 1:\n- 2. Passed by Parliament (December 2011)\n- 3. Came into force (15 February 2012)\n- 4. Gujarat High Court struck down Part IX-B (22 April 2013)\n- 1. Supreme Court final verdict in Rajendra N. Shah (20 July 2021).\nHence, the correct sequence is 2 - 3 - 4 - 1.",
            "exp_ta": "சரியான காலவரிசை 2 → 3 → 4 → 1:\n- 2. நாடாளுமன்றத்தில் நிறைவேற்றப்பட்டது (டிசம்பர் 2011)\n- 3. அமலுக்கு வந்தது (15 பிப்ரவரி 2012)\n- 4. குஜராத் உயர் நீதிமன்றம் ரத்து செய்தது (22 ஏப்ரல் 2013)\n- 1. உச்சநீதிமன்றத்தின் இறுதித் தீர்ப்பு (20 ஜூலை 2021).\nஎனவே, சரியான வரிசை 2 - 3 - 4 - 1 ஆகும்.",
            "why_a_en": "Correct sequence: Dec 2011 (Parliament) → Feb 2012 (Enforced) → Apr 2013 (Gujarat HC) → Jul 2021 (Supreme Court).",
            "why_a_ta": "சரியான காலவரிசை: டிசம்பர் 2011 → பிப்ரவரி 2012 → ஏப்ரல் 2013 → ஜூலை 2021.",
            "why_b_en": "Incorrect. Enforcement in Feb 2012 happened after parliamentary passage in Dec 2011.",
            "why_b_ta": "தவறு. நாடாளுமன்றம் நிறைவேற்றிய பின்னரே சட்டம் அமலானது.",
            "why_c_en": "Incorrect. Gujarat HC struck it down after it came into force.",
            "why_c_ta": "தவறு. அமலுக்கு வந்த பின்னரே குஜராத் உயர்நீதிமன்ற தீர்ப்பு வந்தது.",
            "why_d_en": "Incorrect. High Court judgment came in 2013, not first.",
            "why_d_ta": "தவறு. உயர் நீதிமன்றத் தீர்ப்பு 2013-ல் வந்தது.",
            "tip_en": "97th CAA Lifeline: Enacted (2011) → Enforced (2012) → Struck down by HC (2013) → Severed by SC (2021).",
            "tip_ta": "97வது திருத்தம் காலக்கோடு: நிறைவேற்றம் (2011) → அமல் (2012) → உயர்நீதிமன்ற தீர்ப்பு (2013) → உச்சநீதிமன்ற இறுதித் தீர்ப்பு (2021).",
            "fact_en": "The appeal remained pending before the Supreme Court for eight years (2013 to 2021).",
            "fact_ta": "குஜராத் உயர்நீதிமன்றத் தீர்ப்பிற்கு எதிரான மேல்முறையீடு உச்சநீதிமன்றத்தில் 8 ஆண்டுகள் நிலுவையில் இருந்தது."
        },

        # CS_C_010: Multi-State Cooperatives Legislative Evolution
        {
            "subtopic": "Multi-State Legislation Chronology",
            "stem_en": "Arrange the following parliamentary statutes governing Multi-State Co-operative Societies in chronological order:\n1. Multi-State Co-operative Societies Act, 1984\n2. Multi-State Co-operative Societies (Amendment) Act, 2023\n3. Multi-State Co-operative Societies Act, 2002\n4. Multi-Unit Co-operative Societies Act, 1942",
            "stem_ta": "பல மாநில கூட்டுறவு சங்கங்களை நிர்வகிக்கும் பின்வரும் நாடாளுமன்றச் சட்டங்களை காலவரிசைப்படி ஒழுங்குபடுத்துக:\n1. பல மாநில கூட்டுறவு சங்கங்கள் சட்டம், 1984\n2. பல மாநில கூட்டுறவு சங்கங்கள் (திருத்தச்) சட்டம், 2023\n3. பல மாநில கூட்டுறவு சங்கங்கள் சட்டம், 2002\n4. பல பகுதி கூட்டுறவு சங்கங்கள் சட்டம், 1942 (Multi-Unit Act)",
            "options": [
                ("4 - 1 - 3 - 2", "4 - 1 - 3 - 2"),
                ("1 - 4 - 3 - 2", "1 - 4 - 3 - 2"),
                ("4 - 3 - 1 - 2", "4 - 3 - 1 - 2"),
                ("3 - 4 - 1 - 2", "3 - 4 - 1 - 2")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order of Multi-State legislation is 4 → 1 → 3 → 2:\n- 4. Multi-Unit Co-operative Societies Act (1942)\n- 1. Multi-State Co-operative Societies Act (1984)\n- 3. Multi-State Co-operative Societies Act (2002)\n- 2. Multi-State Co-operative Societies (Amendment) Act (2023).\nHence, the correct sequence is 4 - 1 - 3 - 2.",
            "exp_ta": "பல மாநில சட்டங்களின் சரியான காலவரிசை 4 → 1 → 3 → 2:\n- 4. பல பகுதி கூட்டுறவு சங்கங்கள் சட்டம் (1942)\n- 1. பல மாநில கூட்டுறவு சங்கங்கள் சட்டம் (1984)\n- 3. பல மாநில கூட்டுறவு சங்கங்கள் சட்டம் (2002)\n- 2. பல மாநில கூட்டுறவு சங்கங்கள் (திருத்தச்) சட்டம் (2023).\nஎனவே, சரியான வரிசை 4 - 1 - 3 - 2 ஆகும்.",
            "why_a_en": "Correct sequence: 1942 (Multi-Unit) → 1984 (First MSCS Act) → 2002 (Modern MSCS Act) → 2023 (Election Authority & Ombudsman Amendment).",
            "why_a_ta": "சரியான காலவரிசை: 1942 (மல்டி-யூனிட்) → 1984 (முதல் MSCS) → 2002 (நவீன MSCS) → 2023 (தேர்தல் ஆணையம் திருத்தம்).",
            "why_b_en": "Incorrect. 1942 Multi-Unit Act preceded the 1984 Act.",
            "why_b_ta": "தவறு. 1942 சட்டம் 1984 சட்டத்திற்கு முன்பே இயற்றப்பட்டது.",
            "why_c_en": "Incorrect. 1984 Act preceded 2002 Act.",
            "why_c_ta": "தவறு. 2002 சட்டத்திற்கு முன்பே 1984 சட்டம் இயற்றப்பட்டது.",
            "why_d_en": "Incorrect. 2002 was not the first.",
            "why_d_ta": "தவறு. 2002 முதலாவது அல்ல.",
            "tip_en": "Multi-State Acts sequence: 1942 (Colonial) → 1984 (Post-independence) → 2002 (Liberalized) → 2023 (Reforms).",
            "tip_ta": "பல மாநில சட்டங்கள்: 1942 → 1984 → 2002 → 2023.",
            "fact_en": "The 2002 Act was based on the Choudhary Brahm Perkash Model Act.",
            "fact_ta": "2002 சட்டம் சவுத்ரி பிரம்ம பிரகாஷ் மாதிரி சட்டத்தின் அடிப்படையில் உருவாக்கப்பட்டது."
        }
    ]


def get_chronology_questions_batch3():
    return [
        # CS_C_011: Modern Committees Leading to 97th CAA
        {
            "subtopic": "Reform Trajectory Chronology",
            "stem_en": "Arrange the following milestones leading up to constitutional status for cooperatives in chronological order:\n1. Shivaji Rao Patil High-Powered Committee on Cooperatives submits report\n2. Choudhary Brahm Perkash Committee drafts Model Co-operatives Act\n3. Lok Sabha and Rajya Sabha pass the 97th Constitutional Amendment Bill\n4. Introduction of the 111th Constitutional Amendment Bill in Lok Sabha",
            "stem_ta": "கூட்டுறவுகளுக்கு அரசியலமைப்பு அந்தஸ்து வழங்கப்பட்ட வரலாற்றுப் பாதையின் மைல்கற்களை காலவரிசைப்படி ஒழுங்குபடுத்துக:\n1. சிவாஜிராவ் பாட்டீல் உயர்மட்டக் குழு அறிக்கை சமர்ப்பித்தல்\n2. சவுத்ரி பிரம்ம பிரகாஷ் குழு மாதிரி கூட்டுறவு சட்டத்தை வரைதல்\n3. மக்களவை மற்றும் மாநிலங்களவையில் 97-வது திருத்த மசோதா நிறைவேற்றப்படுதல்\n4. 111-வது அரசியலமைப்பு திருத்த மசோதா மக்களவையில் அறிமுகப்படுத்தப்படுதல்",
            "options": [
                ("2 - 1 - 4 - 3", "2 - 1 - 4 - 3"),
                ("1 - 2 - 4 - 3", "1 - 2 - 4 - 3"),
                ("2 - 4 - 1 - 3", "2 - 4 - 1 - 3"),
                ("4 - 2 - 1 - 3", "4 - 2 - 1 - 3")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is 2 → 1 → 4 → 3:\n- 2. Brahm Perkash Committee (1991)\n- 1. Shivaji Rao Patil Committee report (May 2009)\n- 4. Introduction of 111th Amendment Bill (November 2009)\n- 3. Passed by Parliament as 97th CAA (December 2011).\nHence, the correct sequence is 2 - 1 - 4 - 3.",
            "exp_ta": "சரியான காலவரிசை 2 → 1 → 4 → 3:\n- 2. பிரம்ம பிரகாஷ் மாதிரி சட்டம் (1991)\n- 1. சிவாஜிராவ் பாட்டீல் குழு அறிக்கை (மே 2009)\n- 4. 111-வது திருத்த மசோதா அறிமுகம் (நவம்பர் 2009)\n- 3. நாடாளுமன்றத்தில் 97-வது திருத்தமாக நிறைவேற்றம் (டிசம்பர் 2011).\nஎனவே, சரியான வரிசை 2 - 1 - 4 - 3 ஆகும்.",
            "why_a_en": "Correct sequence: 1991 (Brahm Perkash) → May 2009 (Patil Report) → Nov 2009 (111th Bill) → Dec 2011 (97th CAA).",
            "why_a_ta": "சரியான காலவரிசை: 1991 → மே 2009 → நவம்பர் 2009 → டிசம்பர் 2011.",
            "why_b_en": "Incorrect. Brahm Perkash (1991) preceded Shivaji Rao Patil (2009).",
            "why_b_ta": "தவறு. 2009 பாட்டீல் குழுவிற்கு முன்பே 1991 பிரம்ம பிரகாஷ் குழு அமைந்தது.",
            "why_c_en": "Incorrect. Patil report directly prompted the introduction of the 111th Bill.",
            "why_c_ta": "தவறு. பாட்டீல் குழு அறிக்கையைத் தொடர்ந்தே 111வது மசோதா அறிமுகமானது.",
            "why_d_en": "Incorrect. The Bill was introduced in 2009, not first.",
            "why_d_ta": "தவறு. மசோதா 2009-ல் அறிமுகமானது.",
            "tip_en": "Path to 97th CAA: Model Act (1991) → Patil Committee (2009) → 111th Bill (2009) → 97th CAA (2011).",
            "tip_ta": "97வது திருத்தத்தின் பாதை: மாதிரி சட்டம் (1991) → பாட்டீல் குழு (2009) → 111வது மசோதா (2009) → 97வது திருத்தம் (2011).",
            "fact_en": "The 111th Amendment Bill was scrutinized by the Parliamentary Standing Committee before enactment.",
            "fact_ta": "111-வது திருத்த மசோதா நாடாளுமன்ற நிலைக்குழுவின் ஆய்விற்குப் பின்னரே நிறைவேற்றப்பட்டது."
        },

        # CS_C_012: Industrial and Agro-Processing Cooperatives
        {
            "subtopic": "Industrial Cooperatives History",
            "stem_en": "Arrange the following historic events in industrial and agro-processing cooperation in chronological order:\n1. Formation of National Federation of Cooperative Sugar Factories (NFCSF)\n2. Pravara Cooperative Sugar Factory established in Pravaranagar, Maharashtra\n3. Petrofils Cooperative Limited established to manufacture polyester yarn\n4. First Land Mortgage Bank established at Jhang in Punjab",
            "stem_ta": "தொழில்துறை மற்றும் விவசாயப் பதப்படுத்துதல் கூட்டுறவின் பின்வரும் வரலாற்று நிகழ்வுகளை காலவரிசைப்படி ஒழுங்குபடுத்துக:\n1. கூட்டுறவு சர்க்கரை ஆலைகளின் தேசிய கூட்டமைப்பு (NFCSF) உருவாக்கப்படுதல்\n2. மகாராஷ்டிராவின் பிரவரநகரில் பிரவரா கூட்டுறவு சர்க்கரை ஆலை நிறுவப்படுதல்\n3. பாலியஸ்டர் நூல் உற்பத்திக்காக பெட்ரோஃபில்ஸ் கூட்டுறவு நிறுவனம் நிறுவப்படுதல்\n4. பஞ்சாபின் ஜாங் நகரில் இந்தியாவின் முதல் நில அடமான வங்கி தொடங்கப்படுதல்",
            "options": [
                ("4 - 2 - 1 - 3", "4 - 2 - 1 - 3"),
                ("2 - 4 - 1 - 3", "2 - 4 - 1 - 3"),
                ("4 - 1 - 2 - 3", "4 - 1 - 2 - 3"),
                ("2 - 1 - 4 - 3", "2 - 1 - 4 - 3")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is 4 → 2 → 1 → 3:\n- 4. First Land Mortgage Bank at Jhang (1920)\n- 2. Pravara Cooperative Sugar Factory by Vikhe Patil (1950)\n- 1. National Federation of Cooperative Sugar Factories (1960)\n- 3. Petrofils Cooperative Limited set up (1974).\nHence, the correct sequence is 4 - 2 - 1 - 3.",
            "exp_ta": "சரியான காலவரிசை 4 → 2 → 1 → 3:\n- 4. ஜாங் நகரில் முதல் நில அடமான வங்கி (1920)\n- 2. விகே பாட்டீலின் பிரவரா கூட்டுறவு சர்க்கரை ஆலை (1950)\n- 1. கூட்டுறவு சர்க்கரை ஆலைகளின் தேசிய கூட்டமைப்பு (1960)\n- 3. பெட்ரோஃபில்ஸ் கூட்டுறவு நிறுவனம் (1974).\nஎனவே, சரியான வரிசை 4 - 2 - 1 - 3 ஆகும்.",
            "why_a_en": "Correct sequence: 1920 (Jhang) → 1950 (Pravara Sugar) → 1960 (NFCSF) → 1974 (Petrofils).",
            "why_a_ta": "சரியான காலவரிசை: 1920 (ஜாங்) → 1950 (பிரவரா) → 1960 (NFCSF) → 1974 (பெட்ரோஃபில்ஸ்).",
            "why_b_en": "Incorrect. Jhang Bank (1920) preceded Pravara Sugar (1950).",
            "why_b_ta": "தவறு. 1950 பிரவராவிற்கு முன்பே 1920-ல் ஜாங் வங்கி உருவானது.",
            "why_c_en": "Incorrect. Pravara (1950) was established before the apex federation NFCSF (1960).",
            "why_c_ta": "தவறு. உச்ச கூட்டமைப்பு 1960-ல் உருவானது, ஆலை 1950-ல் தொடங்கியது.",
            "why_d_en": "Incorrect. Petrofils was in 1974, not first.",
            "why_d_ta": "தவறு. பெட்ரோஃபில்ஸ் 1974-ல் உருவானது.",
            "tip_en": "Agro-Industrial Timeline: Jhang Bank (1920) → Pravara Sugar (1950) → NFCSF (1960) → Petrofils (1974).",
            "tip_ta": "தொழில் கூட்டுறவு காலக்கோடு: ஜாங் (1920) → பிரவரா சர்க்கரை (1950) → NFCSF (1960) → பெட்ரோஃபில்ஸ் (1974).",
            "fact_en": "Sugar cooperatives once produced over 60% of India's total white crystal sugar.",
            "fact_ta": "கூட்டுறவு சர்க்கரை ஆலைகள் ஒரு காலத்தில் இந்தியாவின் மொத்த சர்க்கரை உற்பத்தியில் 60%-க்கும் மேல் உற்பத்தி செய்தன."
        },

        # CS_C_013: Banking Regulation of Co-operatives
        {
            "subtopic": "Banking Regulation Milestones",
            "stem_en": "Arrange the following milestones in the banking regulation of cooperative banks in chronological order:\n1. Extension of Banking Regulation Act to Cooperative Banks (Section 56)\n2. Enactment of the original Banking Regulation Act (for commercial banks)\n3. Enhancement of DICGC insurance cover to ₹5 lakh per depositor\n4. Passing of Banking Regulation (Amendment) Act expanding RBI powers over UCBs",
            "stem_ta": "கூட்டுறவு வங்கிகள் மீதான வங்கி ஒழுங்குமுறை வரலாற்று நிகழ்வுகளை காலவரிசைப்படி ஒழுங்குபடுத்துக:\n1. வங்கி ஒழுங்குமுறைச் சட்டம் கூட்டுறவு வங்கிகளுக்கு நீட்டிக்கப்படுதல் (பிரிவு 56)\n2. மூல வங்கி ஒழுங்குமுறைச் சட்டம் இயற்றப்படுதல் (வணிக வங்கிகளுக்கு)\n3. DICGC காப்பீட்டு வரம்பு ஒருவருக்கு ₹5 லட்சமாக உயர்த்தப்படுதல்\n4. UCBs மீது ரிசர்வ் வங்கியின் அதிகாரத்தை விரிவுபடுத்திய வங்கி ஒழுங்குமுறை (திருத்தச்) சட்டம்",
            "options": [
                ("2 - 1 - 3 - 4", "2 - 1 - 3 - 4"),
                ("1 - 2 - 3 - 4", "1 - 2 - 3 - 4"),
                ("2 - 1 - 4 - 3", "2 - 1 - 4 - 3"),
                ("2 - 3 - 1 - 4", "2 - 3 - 1 - 4")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is 2 → 1 → 3 → 4:\n- 2. Banking Regulation Act enacted (1949)\n- 1. Extension to Cooperative Banks under Section 56 (1 March 1966)\n- 3. DICGC cover raised to ₹5 lakh (4 February 2020)\n- 4. Banking Regulation (Amendment) Act passed by Parliament (September 2020).\nHence, the correct sequence is 2 - 1 - 3 - 4.",
            "exp_ta": "சரியான காலவரிசை 2 → 1 → 3 → 4:\n- 2. வங்கி ஒழுங்குமுறைச் சட்டம் இயற்றப்படுதல் (1949)\n- 1. பிரிவு 56 மூலம் கூட்டுறவு வங்கிகளுக்கு நீட்டிப்பு (1 மார்ச் 1966)\n- 3. DICGC காப்பீடு ₹5 லட்சமாக உயர்வு (4 பிப்ரவரி 2020)\n- 4. ரிசர்வ் வங்கி அதிகாரத்தை விரிவுபடுத்திய திருத்தச் சட்டம் (செப்டம்பர் 2020).\nஎனவே, சரியான வரிசை 2 - 1 - 3 - 4 ஆகும்.",
            "why_a_en": "Correct sequence: 1949 (BR Act) → 1966 (Sec 56) → Feb 2020 (DICGC ₹5L) → Sep 2020 (BR Amendment).",
            "why_a_ta": "சரியான காலவரிசை: 1949 → 1966 → பிப்ரவரி 2020 → செப்டம்பர் 2020.",
            "why_b_en": "Incorrect. Original BR Act (1949) preceded Section 56 extension (1966).",
            "why_b_ta": "தவறு. 1966 நீட்டிப்பிற்கு முன்பே 1949-ல் மூலச் சட்டம் இயற்றப்பட்டது.",
            "why_c_en": "Incorrect. DICGC limit increase (Feb 2020) occurred before the BR Amendment Act (Sep 2020).",
            "why_c_ta": "தவறு. பிப்ரவரி 2020-ல் காப்பீடு உயர்த்தப்பட்டது, செப்டம்பரில் சட்டத் திருத்தம் வந்தது.",
            "why_d_en": "Incorrect. Section 56 was inserted in 1966, not after 2020.",
            "why_d_ta": "தவறு. பிரிவு 56 என்பது 1966-ல் சேர்க்கப்பட்டது.",
            "tip_en": "Cooperative Banking Regulation: 1949 (BR Act) → 1966 (Sec 56) → Feb 2020 (DICGC) → Sep 2020 (BR Amendment).",
            "tip_ta": "வங்கி ஒழுங்குமுறை காலக்கோடு: 1949 → 1966 → பிப் 2020 → செப் 2020.",
            "fact_en": "Section 56 covers over 50 specific adaptations of banking law for cooperative banks.",
            "fact_ta": "கூட்டுறவு வங்கிகளுக்காக வங்கிச் சட்டத்தில் 50-க்கும் மேற்பட்ட குறிப்பிட்ட மாற்றங்களை பிரிவு 56 செய்கிறது."
        },

        # CS_C_014: Evolution of Agricultural Credit Committees
        {
            "subtopic": "Agricultural Credit Evolution",
            "stem_en": "Arrange the following historic committees reviewing rural and agricultural credit in chronological order:\n1. All India Rural Credit Survey Committee (Gorwala Committee)\n2. CRAFICARD (B. Sivaraman Committee recommending NABARD)\n3. Townsend Committee on Co-operation in Madras\n4. Maclagan Committee on Co-operation in British India",
            "stem_ta": "கிராமப்புற மற்றும் விவசாயக் கடனை ஆய்வு செய்த பின்வரும் வரலாற்றுக் குழுக்களை காலவரிசைப்படி ஒழுங்குபடுத்துக:\n1. அகில இந்திய கிராமப்புற கடன் ஆய்வுக் குழு (கோர்வாலா குழு)\n2. கிராஃபிகார்ட் (CRAFICARD - நபார்டு வங்கியைப் பரிந்துரைத்த சிவராமன் குழு)\n3. மெட்ராஸ் கூட்டுறவு மீதான டவுன்சென்ட் குழு\n4. பிரிட்டிஷ் இந்தியாவில் கூட்டுறவு மீதான மெக்லகன் குழு (Maclagan Committee)",
            "options": [
                ("4 - 3 - 1 - 2", "4 - 3 - 1 - 2"),
                ("3 - 4 - 1 - 2", "3 - 4 - 1 - 2"),
                ("4 - 1 - 3 - 2", "4 - 1 - 3 - 2"),
                ("1 - 4 - 3 - 2", "1 - 4 - 3 - 2")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is 4 → 3 → 1 → 2:\n- 4. Maclagan Committee (1914-15)\n- 3. Townsend Committee in Madras (1927-28)\n- 1. All India Rural Credit Survey Committee / Gorwala (1951-54)\n- 2. CRAFICARD / Sivaraman Committee (1979-81).\nHence, the correct sequence is 4 - 3 - 1 - 2.",
            "exp_ta": "சரியான காலவரிசை 4 → 3 → 1 → 2:\n- 4. மெக்லகன் குழு (1914-15)\n- 3. மெட்ராஸ் டவுன்சென்ட் குழு (1927-28)\n- 1. அகில இந்திய கிராமப்புற கடன் ஆய்வுக் குழு / கோர்வாலா (1951-54)\n- 2. கிராஃபிகார்ட் / சிவராமன் குழு (1979-81).\nஎனவே, சரியான வரிசை 4 - 3 - 1 - 2 ஆகும்.",
            "why_a_en": "Correct sequence: 1914 (Maclagan) → 1927 (Townsend) → 1954 (Gorwala) → 1979 (CRAFICARD).",
            "why_a_ta": "சரியான காலவரிசை: 1914 (மெக்லகன்) → 1927 (டவுன்சென்ட்) → 1954 (கோர்வாலா) → 1979 (கிராஃபிகார்ட்).",
            "why_b_en": "Incorrect. Maclagan (1914) preceded Townsend (1927).",
            "why_b_ta": "தவறு. 1927 டவுன்சென்ட் குழுவிற்கு முன்பே 1914 மெக்லகன் குழு வந்தது.",
            "why_c_en": "Incorrect. Townsend (1927) preceded Gorwala (1954).",
            "why_c_ta": "தவறு. 1954 கோர்வாலா குழுவிற்கு முன் டவுன்சென்ட் குழு அறிக்கை அளித்தது.",
            "why_d_en": "Incorrect. Gorwala was in 1954, not the first.",
            "why_d_ta": "தவறு. கோர்வாலா 1954-ல் அறிக்கை அளித்தது.",
            "tip_en": "Historic Credit Committees: Maclagan (1914) → Townsend (1927) → Gorwala (1954) → Sivaraman (1979).",
            "tip_ta": "வரலாற்று கடன் குழுக்கள்: மெக்லகன் (1914) → டவுன்சென்ட் (1927) → கோர்வாலா (1954) → சிவராமன் (1979).",
            "fact_en": "The Maclagan Committee laid down the structural architecture for 3-tier cooperative credit in India.",
            "fact_ta": "மெக்லகன் குழுவே இந்தியாவில் மூன்றடுக்கு கூட்டுறவு கடன் அமைப்பிற்கான அடித்தளத்தை வகுத்தது."
        },

        # CS_C_015: Producer Companies & Corporate Framework
        {
            "subtopic": "Producer Companies Evolution",
            "stem_en": "Arrange the following milestones in the evolution of Producer Companies and FPOs in chronological order:\n1. Companies Act, 2013 enacted (retaining Producer Companies provisions)\n2. Dr. Y.K. Alagh Committee on Producer Companies submits report\n3. Central Sector Scheme for Formation and Promotion of 10,000 FPOs launched\n4. Companies Act, 1956 amended to insert Part IX-A (Producer Companies)",
            "stem_ta": "உழவர் உற்பத்தியாளர் நிறுவனங்கள் (FPO) பரிணாம வளர்ச்சியின் பின்வரும் மைல்கற்களை காலவரிசைப்படி ஒழுங்குபடுத்துக:\n1. நிறுவனங்கள் சட்டம் 2013 இயற்றப்படுதல் (உற்பத்தியாளர் நிறுவன விதிகள் தக்கவைக்கப்பட்டன)\n2. உற்பத்தியாளர் நிறுவனங்கள் மீதான டாக்டர் ஓய்.கே. அலாக் குழு அறிக்கை சமர்ப்பித்தல்\n3. 10,000 உழவர் உற்பத்தியாளர் நிறுவனங்களை (FPO) உருவாக்குவதற்கான மத்தியத் திட்டம் தொடங்கப்படுதல்\n4. நிறுவனங்கள் சட்டம் 1956-ல் பகுதி IX-A சேர்க்கப்பட்டு திருத்தப்படுதல்",
            "options": [
                ("2 - 4 - 1 - 3", "2 - 4 - 1 - 3"),
                ("4 - 2 - 1 - 3", "4 - 2 - 1 - 3"),
                ("2 - 1 - 4 - 3", "2 - 1 - 4 - 3"),
                ("1 - 2 - 4 - 3", "1 - 2 - 4 - 3")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is 2 → 4 → 1 → 3:\n- 2. Y.K. Alagh Committee report (2000)\n- 4. Companies Act 1956 amended to add Part IX-A (2002)\n- 1. Companies Act 2013 enacted (2013)\n- 3. Central Sector Scheme for 10,000 FPOs launched (2020).\nHence, the correct sequence is 2 - 4 - 1 - 3.",
            "exp_ta": "சரியான காலவரிசை 2 → 4 → 1 → 3:\n- 2. ஓய்.கே. அலாக் குழு அறிக்கை (2000)\n- 4. 1956 நிறுவனங்கள் சட்டத்தில் பகுதி IX-A சேர்க்கப்படுதல் (2002)\n- 1. நிறுவனங்கள் சட்டம் 2013 இயற்றப்படுதல் (2013)\n- 3. 10,000 FPO அமைக்கும் மத்தியத் திட்டம் தொடக்கம் (2020).\nஎனவே, சரியான வரிசை 2 - 4 - 1 - 3 ஆகும்.",
            "why_a_en": "Correct sequence: 2000 (Alagh) → 2002 (Part IX-A) → 2013 (Companies Act 2013) → 2020 (10,000 FPOs).",
            "why_a_ta": "சரியான காலவரிசை: 2000 (அலாக்) → 2002 (பகுதி IX-A) → 2013 (நிறுவனங்கள் சட்டம்) → 2020 (10,000 FPO திட்டம்).",
            "why_b_en": "Incorrect. Alagh Committee (2000) preceded the amendment (2002).",
            "why_b_ta": "தவறு. 2002 திருத்தத்திற்கு முன்பே 2000-ல் அலாக் குழு அறிக்கை அளித்தது.",
            "why_c_en": "Incorrect. 2002 amendment preceded the 2013 Act.",
            "why_c_ta": "தவறு. 2013 சட்டத்திற்கு முன்பே 2002 திருத்தம் வந்தது.",
            "why_d_en": "Incorrect. 2013 was not first.",
            "why_d_ta": "தவறு. 2013 முதலாவது அல்ல.",
            "tip_en": "FPO Timeline: Alagh Committee (2000) → Part IX-A (2002) → Companies Act (2013) → 10,000 FPOs (2020).",
            "tip_ta": "FPO காலக்கோடு: அலாக் குழு (2000) → பகுதி IX-A (2002) → நிறுவன சட்டம் (2013) → 10,000 FPO (2020).",
            "fact_en": "Implementing agencies for the 10,000 FPO scheme include SFAC, NABARD, and NCDC.",
            "fact_ta": "10,000 FPO திட்டத்தை SFAC, நபார்டு மற்றும் NCDC ஆகியவை செயல்படுத்துகின்றன."
        }
    ]


def get_chronology_questions_batch4():
    return [
        # CS_C_016: Tamil Nadu Dairy Milestones
        {
            "subtopic": "Tamil Nadu Dairy History",
            "stem_en": "Arrange the following milestones in Tamil Nadu's dairy cooperative history in chronological order:\n1. Establishment of the Tamil Nadu Dairy Development Corporation (TNDDC)\n2. Formation of Dairy Development Department in Madras State\n3. TCMPF (Aavin) taking over all commercial dairy processing and marketing\n4. Launch of Operation Flood in Tamil Nadu",
            "stem_ta": "தமிழ்நாட்டின் பால்வளக் கூட்டுறவு வரலாற்றின் பின்வரும் மைல்கற்களை காலவரிசைப்படி ஒழுங்குபடுத்துக:\n1. தமிழ்நாடு பால்வள மேம்பாட்டுக் கழகம் (TNDDC) நிறுவப்படுதல்\n2. மெட்ராஸ் மாநிலத்தில் பால்வள மேம்பாட்டுத் துறை உருவாக்கப்படுதல்\n3. ஆவின் (TCMPF) அனைத்து வணிக ரீதியான பால் பதப்படுத்துதல் மற்றும் விற்பனையை ஏற்று நடத்துதல்\n4. தமிழ்நாட்டில் ஆபரேஷன் பிளட் திட்டம் தொடங்கப்படுதல்",
            "options": [
                ("2 - 4 - 1 - 3", "2 - 4 - 1 - 3"),
                ("2 - 1 - 4 - 3", "2 - 1 - 4 - 3"),
                ("4 - 2 - 1 - 3", "4 - 2 - 1 - 3"),
                ("2 - 4 - 3 - 1", "2 - 4 - 3 - 1")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is 2 → 4 → 1 → 3:\n- 2. Dairy Development Department formed (1958)\n- 4. Operation Flood launched in TN (1971)\n- 1. Tamil Nadu Dairy Development Corporation set up (1972)\n- 3. TCMPF (Aavin) taking over apex operations (1981).\nHence, the correct sequence is 2 - 4 - 1 - 3.",
            "exp_ta": "சரியான காலவரிசை 2 → 4 → 1 → 3:\n- 2. பால்வள மேம்பாட்டுத் துறை உருவாக்கம் (1958)\n- 4. தமிழ்நாட்டில் ஆபரேஷன் பிளட் தொடக்கம் (1971)\n- 1. தமிழ்நாடு பால்வள மேம்பாட்டுக் கழகம் தொடக்கம் (1972)\n- 3. ஆவின் (TCMPF) உச்ச வணிகப் பணிகளை ஏற்றல் (1981).\nஎனவே, சரியான வரிசை 2 - 4 - 1 - 3 ஆகும்.",
            "why_a_en": "Correct sequence: 1958 (Department) → 1971 (Operation Flood) → 1972 (TNDDC) → 1981 (TCMPF/Aavin).",
            "why_a_ta": "சரியான காலவரிசை: 1958 → 1971 → 1972 → 1981.",
            "why_b_en": "Incorrect. Operation Flood (1971) prompted the creation of TNDDC (1972).",
            "why_b_ta": "தவறு. ஆபரேஷன் பிளட்டைத் தொடர்ந்தே 1972-ல் கழகம் அமைக்கப்பட்டது.",
            "why_c_en": "Incorrect. Department was formed in 1958, before Operation Flood.",
            "why_c_ta": "தவறு. 1958-ல் துறை உருவானது.",
            "why_d_en": "Incorrect. 1981 was the last event.",
            "why_d_ta": "தவறு. 1981 இறுதியானது.",
            "tip_en": "TN Dairy Timeline: 1958 (Dept) → 1971 (Op Flood) → 1972 (Corporation) → 1981 (Aavin Apex Federation).",
            "tip_ta": "தமிழக பால் காலக்கோடு: 1958 → 1971 → 1972 → 1981 (ஆவின்).",
            "fact_en": "Madhavaram milk colony was the first organized modern milk project in Chennai.",
            "fact_ta": "சென்னையில் மாதவரம் பால் பண்ணை காலனி முதல் நவீன பால் திட்டமாக உருவாக்கப்பட்டது."
        },

        # CS_C_017: International Cooperative Identity Milestones
        {
            "subtopic": "International Cooperative Movement",
            "stem_en": "Arrange the following historic milestones of the global cooperative movement in chronological order:\n1. ICA Statement on the Co-operative Identity adopted at Manchester\n2. Rochdale Society of Equitable Pioneers founded in Lancashire, England\n3. International Co-operative Alliance (ICA) established in London\n4. United Nations International Year of Cooperatives celebrated",
            "stem_ta": "உலகளாவிய கூட்டுறவு இயக்கத்தின் பின்வரும் வரலாற்று மைல்கற்களை காலவரிசைப்படி ஒழுங்குபடுத்துக:\n1. மான்செஸ்டரில் ஏற்றுக்கொள்ளப்பட்ட ICA கூட்டுறவு அடையாள அறிக்கை\n2. இங்கிலாந்தின் லங்காஷயரில் ரோச்டேல் முன்னோடிகள் சங்கம் நிறுவப்படுதல்\n3. லண்டனில் சர்வதேச கூட்டுறவு கூட்டணி (ICA) நிறுவப்படுதல்\n4. ஐக்கிய நாடுகள் சர்வதேசக் கூட்டுறவு ஆண்டு கொண்டாடப்படுதல்",
            "options": [
                ("2 - 3 - 1 - 4", "2 - 3 - 1 - 4"),
                ("3 - 2 - 1 - 4", "3 - 2 - 1 - 4"),
                ("2 - 1 - 3 - 4", "2 - 1 - 3 - 4"),
                ("2 - 3 - 4 - 1", "2 - 3 - 4 - 1")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is 2 → 3 → 1 → 4:\n- 2. Rochdale Pioneers (1844)\n- 3. International Co-operative Alliance formed in London (1895)\n- 1. ICA Manchester Statement on Co-operative Identity (1995)\n- 4. UN International Year of Cooperatives (2012).\nHence, the correct sequence is 2 - 3 - 1 - 4.",
            "exp_ta": "சரியான காலவரிசை 2 → 3 → 1 → 4:\n- 2. ரோச்டேல் முன்னோடிகள் சங்கம் (1844)\n- 3. லண்டனில் சர்வதேச கூட்டுறவு கூட்டணி (ICA) உருவாக்கம் (1895)\n- 1. மான்செஸ்டர் ICA கூட்டுறவு அடையாள அறிக்கை (1995)\n- 4. ஐ.நா சர்வதேசக் கூட்டுறவு ஆண்டு (2012).\nஎனவே, சரியான வரிசை 2 - 3 - 1 - 4 ஆகும்.",
            "why_a_en": "Correct sequence: 1844 (Rochdale) → 1895 (ICA) → 1995 (Manchester Statement) → 2012 (UN Year).",
            "why_a_ta": "சரியான காலவரிசை: 1844 (ரோச்டேல்) → 1895 (ICA) → 1995 (மான்செஸ்டர்) → 2012 (ஐ.நா ஆண்டு).",
            "why_b_en": "Incorrect. Rochdale (1844) was the pioneer well before ICA (1895).",
            "why_b_ta": "தவறு. ICA-க்கு முன்பே 1844-ல் ரோச்டேல் முன்னோடிகள் தொடங்கினர்.",
            "why_c_en": "Incorrect. ICA (1895) preceded Manchester Statement (1995).",
            "why_c_ta": "தவறு. 1995 மான்செஸ்டர் அறிக்கைக்கு முன்பே 1895-ல் ICA உருவானது.",
            "why_d_en": "Incorrect. 1995 was before 2012.",
            "why_d_ta": "தவறு. 1995 அறிக்கை 2012-க்கு முந்தையது.",
            "tip_en": "Global Cooperative Timeline: 1844 (Rochdale) → 1895 (ICA) → 1995 (Centenary Principles) → 2012 (UN Year).",
            "tip_ta": "உலகளாவிய காலக்கோடு: 1844 (ரோச்டேல்) → 1895 (ICA) → 1995 (கோட்பாடுகள்) → 2012 (ஐ.நா ஆண்டு).",
            "fact_en": "The Rochdale Principles of 1844 are celebrated as the root of modern cooperative democracy.",
            "fact_ta": "1844 ரோச்டேல் கோட்பாடுகளே நவீன கூட்டுறவு ஜனநாயகத்தின் வேராகக் கொண்டாடப்படுகின்றன."
        },

        # CS_C_018: Constitutional Provisions Insertion
        {
            "subtopic": "Constitutional Articles Insertion",
            "stem_en": "Arrange the following constitutional provisions in chronological order of their insertion into the Constitution of India:\n1. Part IX-A (Municipalities, Articles 243P to 243ZG)\n2. Part IX (Panchayats, Articles 243 to 243O)\n3. Article 43 (Promotion of cottage industries in rural areas)\n4. Part IX-B (Co-operative Societies, Articles 243ZH to 243ZT)",
            "stem_ta": "பின்வரும் அரசியலமைப்பு விதிகளை இந்திய அரசியலமைப்பில் சேர்க்கப்பட்ட காலவரிசைப்படி ஒழுங்குபடுத்துக:\n1. பகுதி IX-A (நகராட்சிகள், உறுப்புகள் 243P முதல் 243ZG வரை)\n2. பகுதி IX (பஞ்சாயத்துகள், உறுப்புகள் 243 முதல் 243O வரை)\n3. உறுப்பு 43 (கிராமப்புறங்களில் குடிசைத் தொழில்களை ஊக்குவித்தல்)\n4. பகுதி IX-B (கூட்டுறவு சங்கங்கள், உறுப்புகள் 243ZH முதல் 243ZT வரை)",
            "options": [
                ("3 - 2 - 1 - 4", "3 - 2 - 1 - 4"),
                ("2 - 1 - 3 - 4", "2 - 1 - 3 - 4"),
                ("3 - 1 - 2 - 4", "3 - 1 - 2 - 4"),
                ("3 - 2 - 4 - 1", "3 - 2 - 4 - 1")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order of insertion is 3 → 2 → 1 → 4:\n- 3. Article 43 in Part IV (original Constitution, 1950)\n- 2. Part IX inserted by 73rd CAA (enacted 1992, enforced 24 April 1993)\n- 1. Part IX-A inserted by 74th CAA (enacted 1992, enforced 1 June 1993)\n- 4. Part IX-B inserted by 97th CAA (enacted 2011, enforced 15 Feb 2012).\nHence, the correct sequence is 3 - 2 - 1 - 4.",
            "exp_ta": "சரியான காலவரிசை 3 → 2 → 1 → 4:\n- 3. உறுப்பு 43 (1950 மூல அரசியலமைப்பு)\n- 2. பகுதி IX பஞ்சாயத்துகள் (73வது திருத்தம், அமல் ஏப்ரல் 1993)\n- 1. பகுதி IX-A நகராட்சிகள் (74வது திருத்தம், அமல் ஜூன் 1993)\n- 4. பகுதி IX-B கூட்டுறவு சங்கங்கள் (97வது திருத்தம், அமல் பிப்ரவரி 2012).\nஎனவே, சரியான வரிசை 3 - 2 - 1 - 4 ஆகும்.",
            "why_a_en": "Correct sequence: 1950 (Art 43) → Apr 1993 (Part IX) → Jun 1993 (Part IX-A) → Feb 2012 (Part IX-B).",
            "why_a_ta": "சரியான காலவரிசை: 1950 (உறுப்பு 43) → ஏப் 1993 (பகுதி IX) → ஜூன் 1993 (பகுதி IX-A) → பிப் 2012 (பகுதி IX-B).",
            "why_b_en": "Incorrect. Article 43 was in the original 1950 Constitution.",
            "why_b_ta": "தவறு. உறுப்பு 43 மூல அரசியலமைப்பிலேயே (1950) இருந்தது.",
            "why_c_en": "Incorrect. 73rd CAA (Panchayats) came into effect before 74th CAA (Municipalities).",
            "why_c_ta": "தவறு. நகராட்சிகளுக்கு முன்பே பஞ்சாயத்துகள் சட்டம் அமலுக்கு வந்தது.",
            "why_d_en": "Incorrect. Part IX-B was in 2011/2012, after Municipalities.",
            "why_d_ta": "தவறு. பகுதி IX-B 2011-ல் வந்தது.",
            "tip_en": "Local Democracy Progression: 1950 (DPSP) → 1992 (Panchayats) → 1992 (Municipalities) → 2011 (Cooperatives).",
            "tip_ta": "உள்ளாட்சி ஜனநாயகம்: 1950 (நெறிமுறைகள்) → 1992 (பஞ்சாயத்து) → 1992 (நகராட்சி) → 2011 (கூட்டுறவு).",
            "fact_en": "Article 43 specifically promoted cottage industries on an individual or co-operative basis.",
            "fact_ta": "உறுப்பு 43 தனிநபர் அல்லது கூட்டுறவு அடிப்படையில் குடிசைத் தொழில்களை ஊக்குவிக்க வலியுறுத்துகிறது."
        },

        # CS_C_019: Recent Initiatives of Ministry of Cooperation
        {
            "subtopic": "Ministry of Cooperation Initiatives",
            "stem_en": "Arrange the following recent flagship initiatives of the Ministry of Cooperation in chronological order:\n1. Dedicated Committee under Suresh Prabhu to draft new National Cooperation Policy\n2. Formal creation of the independent Ministry of Cooperation\n3. Launch of the National Cooperative Database by Union Minister of Cooperation\n4. Union Cabinet approval for establishment of 3 new national multi-state cooperatives",
            "stem_ta": "கூட்டுறவு அமைச்சகத்தின் பின்வரும் சமீபத்திய முக்கிய முயற்சிகளை காலவரிசைப்படி ஒழுங்குபடுத்துக:\n1. புதிய தேசிய கூட்டுறவுக் கொள்கையை வரைவதற்காக சுரேஷ் பிரபு தலைமையில் பிரத்யேகக் குழு அமைக்கப்படுதல்\n2. தனி கூட்டுறவு அமைச்சகம் அதிகாரப்பூர்வமாக உருவாக்கப்படுதல்\n3. மத்திய கூட்டுறவு அமைச்சரால் தேசிய கூட்டுறவு தரவுத்தளம் தொடங்கி வைக்கப்படுதல்\n4. மூன்று புதிய தேசிய பல மாநில கூட்டுறவு சங்கங்களை அமைக்க மத்திய அமைச்சரவை ஒப்புதல் அளித்தல்",
            "options": [
                ("2 - 1 - 4 - 3", "2 - 1 - 4 - 3"),
                ("1 - 2 - 4 - 3", "1 - 2 - 4 - 3"),
                ("2 - 4 - 1 - 3", "2 - 4 - 1 - 3"),
                ("4 - 2 - 1 - 3", "4 - 2 - 1 - 3")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is 2 → 1 → 4 → 3:\n- 2. Creation of Ministry of Cooperation (July 2021)\n- 1. Suresh Prabhu Committee constituted (September 2022)\n- 4. Cabinet approval for 3 new multi-state cooperatives (January 2023)\n- 3. National Cooperative Database launched (March 2024).\nHence, the correct sequence is 2 - 1 - 4 - 3.",
            "exp_ta": "சரியான காலவரிசை 2 → 1 → 4 → 3:\n- 2. கூட்டுறவு அமைச்சகம் உருவாக்கம் (ஜூலை 2021)\n- 1. சுரேஷ் பிரபு குழு அமைப்பு (செப்டம்பர் 2022)\n- 4. மூன்று புதிய கூட்டுறவுகளுக்கு அமைச்சரவை ஒப்புதல் (ஜனவரி 2023)\n- 3. தேசிய கூட்டுறவு தரவுத்தளம் தொடக்கம் (மார்ச் 2024).\nஎனவே, சரியான வரிசை 2 - 1 - 4 - 3 ஆகும்.",
            "why_a_en": "Correct sequence: Jul 2021 (Ministry) → Sep 2022 (Prabhu Committee) → Jan 2023 (3 New Coops) → Mar 2024 (Database).",
            "why_a_ta": "சரியான காலவரிசை: ஜூலை 2021 → செப் 2022 → ஜனவரி 2023 → மார்ச் 2024.",
            "why_b_en": "Incorrect. Ministry was created in 2021 before the Prabhu Committee in 2022.",
            "why_b_ta": "தவறு. 2021-ல் அமைச்சகம் உருவான பின்னரே 2022-ல் பிரபு குழு அமைக்கப்பட்டது.",
            "why_c_en": "Incorrect. Prabhu Committee (2022) preceded the 2023 Cabinet decision.",
            "why_c_ta": "தவறு. 2022 பிரபு குழுவிற்குப் பிறகே 2023 அமைச்சரவை முடிவு வந்தது.",
            "why_d_en": "Incorrect. 2023 Cabinet decision was not first.",
            "why_d_ta": "தவறு. 2023 அமைச்சரவை முடிவு முதலாவது அல்ல.",
            "tip_en": "Modern Cooperation Timeline: 2021 (Ministry) → 2022 (Policy Committee) → 2023 (3 New Apex Societies) → 2024 (National Database).",
            "tip_ta": "நவீன கூட்டுறவு காலக்கோடு: 2021 (அமைச்சகம்) → 2022 (கொள்கைக் குழு) → 2023 (3 புதிய சங்கங்கள்) → 2024 (தரவுத்தளம்).",
            "fact_en": "The 3 new apex societies cover exports (NCEL), organics (NCOL), and seeds (BBSSL).",
            "fact_ta": "3 புதிய உச்ச அமைப்புகள் ஏற்றுமதி (NCEL), இயற்கை வேளாண்மை (NCOL), மற்றும் விதைகளை (BBSSL) உள்ளடக்கியவை."
        },

        # CS_C_020: Handloom Welfare Landmarks in Tamil Nadu
        {
            "subtopic": "Handloom Milestones in Tamil Nadu",
            "stem_en": "Arrange the following handloom welfare milestones in Tamil Nadu in chronological order:\n1. National Handloom Day celebrated first time on 7th August\n2. Establishment of Co-optex as Madras Handloom Weavers' Provincial Society\n3. Enactment of Handlooms (Reservation of Articles for Production) Act by Parliament\n4. Introduction of Free Dhoti and Saree Scheme for Pongal in Tamil Nadu",
            "stem_ta": "தமிழ்நாட்டில் கைத்தறி நலன் சார்ந்த பின்வரும் வரலாற்று மைல்கற்களை காலவரிசைப்படி ஒழுங்குபடுத்துக:\n1. ஆகஸ்ட் 7 அன்று முதல் முறையாக தேசிய கைத்தறி தினம் கொண்டாடப்படுதல்\n2. கோ-ஆப்லெக்ஸ் அமைப்பு மெட்ராஸ் மாகாண கைத்தறி சங்கமாக நிறுவப்படுதல்\n3. நாடாளுமன்றத்தால் கைத்தறி (உற்பத்திக்கான பொருட்கள் இடஒதுக்கீடு) சட்டம் இயற்றப்படுதல்\n4. தமிழ்நாட்டில் பொங்கல் பண்டிகைக்கான இலவச வேட்டி மற்றும் சேலை திட்டம் அறிமுகப்படுத்தப்படுதல்",
            "options": [
                ("2 - 4 - 3 - 1", "2 - 4 - 3 - 1"),
                ("2 - 3 - 4 - 1", "2 - 3 - 4 - 1"),
                ("4 - 2 - 3 - 1", "4 - 2 - 3 - 1"),
                ("2 - 4 - 1 - 3", "2 - 4 - 1 - 3")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is 2 → 4 → 3 → 1:\n- 2. Co-optex established (1935)\n- 4. Free Dhoti and Saree Scheme introduced by MGR (1983)\n- 3. Handlooms Reservation Act passed by Parliament (1985)\n- 1. First National Handloom Day inaugurated in Chennai by PM (7 August 2015).\nHence, the correct sequence is 2 - 4 - 3 - 1.",
            "exp_ta": "சரியான காலவரிசை 2 → 4 → 3 → 1:\n- 2. கோ-ஆப்லெக்ஸ் அமைப்பு நிறுவப்படுதல் (1935)\n- 4. எம்.ஜி.ஆரால் இலவச வேட்டி-சேலை திட்டம் தொடங்கப்படுதல் (1983)\n- 3. மத்திய அரசின் கைத்தறி இடஒதுக்கீடு சட்டம் (1985)\n- 1. சென்னையில் முதல் தேசிய கைத்தறி தினம் தொடங்கப்படுதல் (7 ஆகஸ்ட் 2015).\nஎனவே, சரியான வரிசை 2 - 4 - 3 - 1 ஆகும்.",
            "why_a_en": "Correct sequence: 1935 (Co-optex) → 1983 (Free Dhoti/Saree) → 1985 (Reservation Act) → 2015 (National Handloom Day).",
            "why_a_ta": "சரியான காலவரிசை: 1935 (கோ-ஆப்லெக்ஸ்) → 1983 (இலவச வேட்டி) → 1985 (இடஒதுக்கீடு சட்டம்) → 2015 (கைத்தறி தினம்).",
            "why_b_en": "Incorrect. Free Dhoti scheme (1983) preceded the 1985 Act.",
            "why_b_ta": "தவறு. 1985 சட்டத்திற்கு முன்பே 1983-ல் இலவச வேட்டி-சேலை திட்டம் வந்தது.",
            "why_c_en": "Incorrect. Co-optex (1935) was the earliest event.",
            "why_c_ta": "தவறு. கோ-ஆப்லெக்ஸ் (1935) எல்லாவற்றிற்கும் முந்தையது.",
            "why_d_en": "Incorrect. Handloom Day was inaugurated in 2015, after the 1985 Act.",
            "why_d_ta": "தவறு. கைத்தறி தினம் 2015-ல் தொடங்கியது.",
            "tip_en": "Handloom History: 1935 (Co-optex) → 1983 (Free Scheme) → 1985 (Reservation Act) → 2015 (Handloom Day on Swadeshi Day).",
            "tip_ta": "கைத்தறி வரலாறு: 1935 (கோ-ஆப்லெக்ஸ்) → 1983 (இலவச திட்டம்) → 1985 (சட்டம்) → 2015 (தேசிய கைத்தறி தினம்).",
            "fact_en": "7th August was chosen for National Handloom Day to commemorate the launch of the Swadeshi Movement on 7 August 1905.",
            "fact_ta": "1905 ஆகஸ்ட் 7 அன்று தொடங்கப்பட்ட சுதேசி இயக்கத்தின் நினைவாக தேசிய கைத்தறி தினம் இந்நாளில் கொண்டாடப்படுகிறது."
        }
    ]


def get_chronology_questions_batch5():
    return [
        # CS_C_021: Land Development Banking Evolution
        {
            "subtopic": "Long-Term Credit History",
            "stem_en": "Arrange the following historic events in the evolution of long-term cooperative credit (Land Development Banks) in chronological order:\n1. Establishment of the Central Land Mortgage Bank in Madras\n2. First Land Mortgage Bank in India established at Jhang in Punjab\n3. Townsend Committee in Madras reviewing land mortgage banks\n4. Renaming of Land Development Banks as State Cooperative Agriculture and Rural Development Banks (SCARDBs)",
            "stem_ta": "நீண்ட கால கூட்டுறவு கடன் (நிலவள வங்கிகள்) வரலாற்றின் பின்வரும் நிகழ்வுகளை காலவரிசைப்படி ஒழுங்குபடுத்துக:\n1. மெட்ராஸில் மத்திய நில அடமான வங்கி நிறுவப்படுதல்\n2. பஞ்சாபின் ஜாங் நகரில் இந்தியாவின் முதல் நில அடமான வங்கி தொடங்கப்படுதல்\n3. மெட்ராஸில் நில அடமான வங்கிகளை ஆய்வு செய்த டவுன்சென்ட் குழு\n4. நில மேம்பாட்டு வங்கிகள் 'மாநிலக் கூட்டுறவு விவசாய மற்றும் ஊரக வளர்ச்சி வங்கிகள்' (SCARDB) எனப் பெயர் மாற்றப்படுதல்",
            "options": [
                ("2 - 3 - 1 - 4", "2 - 3 - 1 - 4"),
                ("3 - 2 - 1 - 4", "3 - 2 - 1 - 4"),
                ("2 - 1 - 3 - 4", "2 - 1 - 3 - 4"),
                ("1 - 2 - 3 - 4", "1 - 2 - 3 - 4")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is 2 → 3 → 1 → 4:\n- 2. Jhang Land Mortgage Bank, Punjab (1920)\n- 3. Townsend Committee report in Madras (1927)\n- 1. Madras Central Land Mortgage Bank established (1929)\n- 4. Renamed as SCARDBs / ARDBs across States (1980s).\nHence, the correct sequence is 2 - 3 - 1 - 4.",
            "exp_ta": "சரியான காலவரிசை 2 → 3 → 1 → 4:\n- 2. பஞ்சாபின் ஜாங் நகரில் முதல் நில அடமான வங்கி (1920)\n- 3. மெட்ராஸ் டவுன்சென்ட் குழு அறிக்கை (1927)\n- 1. மெட்ராஸ் மத்திய நில அடமான வங்கி நிறுவப்படுதல் (1929)\n- 4. SCARDB எனப் பெயர் மாற்றப்படுதல் (1980-கள்).\nஎனவே, சரியான வரிசை 2 - 3 - 1 - 4 ஆகும்.",
            "why_a_en": "Correct sequence: 1920 (Jhang) → 1927 (Townsend) → 1929 (Madras Bank) → 1980s (SCARDB renaming).",
            "why_a_ta": "சரியான காலவரிசை: 1920 (ஜாங்) → 1927 (டவுன்சென்ட்) → 1929 (மெட்ராஸ் வங்கி) → 1980-கள் (SCARDB).",
            "why_b_en": "Incorrect. Jhang Bank (1920) was the first in India.",
            "why_b_ta": "தவறு. 1920 ஜாங் வங்கியே இந்தியாவில் முதலாவது.",
            "why_c_en": "Incorrect. Townsend committee (1927) paved the way for Madras bank in 1929.",
            "why_c_ta": "தவறு. டவுன்சென்ட் குழுவின் பரிந்துரைப்படியே 1929-ல் மெட்ராஸ் வங்கி உருவானது.",
            "why_d_en": "Incorrect. Madras was not the first; Jhang in Punjab was first.",
            "why_d_ta": "தவறு. மெட்ராஸ் முதலாவது அல்ல, பஞ்சாபின் ஜாங் முதலாவது.",
            "tip_en": "Long-term credit timeline: 1920 (Jhang) → 1927 (Townsend) → 1929 (Madras) → 1980s (SCARDB).",
            "tip_ta": "நீண்ட கால கடன் காலக்கோடு: 1920 (ஜாங்) → 1927 (டவுன்சென்ட்) → 1929 (மெட்ராஸ்) → 1980-கள் (SCARDB).",
            "fact_en": "Madras was the first province to pass a dedicated Land Mortgage Banks Act in 1934.",
            "fact_ta": "1934-ல் நில அடமான வங்கிகளுக்கான பிரத்யேகச் சட்டத்தை இயற்றிய முதல் மாகாணம் மெட்ராஸ் ஆகும்."
        },

        # CS_C_022: Governance Reform Committees Sequence
        {
            "subtopic": "Governance Reform Committees",
            "stem_en": "Arrange the following committees recommending governance and structural reforms in cooperatives in chronological order:\n1. K.N. Ardhanareeswaran Committee on Cooperative Law for Democratic Management\n2. Choudhary Brahm Perkash Committee on Model Co-operatives Act\n3. Ram Niwas Mirdha Committee on Cooperatives\n4. Prof. A. Vaidyanathan Committee on Rural Cooperative Revival",
            "stem_ta": "கூட்டுறவுகளில் நிர்வாகம் மற்றும் கட்டமைப்புச் சீர்திருத்தங்களைப் பரிந்துரைத்த பின்வரும் குழுக்களை காலவரிசைப்படி ஒழுங்குபடுத்துக:\n1. ஜனநாயக நிர்வாகத்திற்கான கூட்டுறவு சட்டம் குறித்த கே.என். அர்த்தநாரீஸ்வரன் குழு\n2. மாதிரி கூட்டுறவு சட்டம் குறித்த சவுத்ரி பிரம்ம பிரகாஷ் குழு\n3. கூட்டுறவு மீதான ராம் நிவாஸ் மிர்தா குழு\n4. கிராமப்புற கூட்டுறவு மறுமலர்ச்சி மீதான பேராசிரியர் ஏ. வைத்தியநாதன் குழு",
            "options": [
                ("3 - 1 - 2 - 4", "3 - 1 - 2 - 4"),
                ("1 - 3 - 2 - 4", "1 - 3 - 2 - 4"),
                ("3 - 2 - 1 - 4", "3 - 2 - 1 - 4"),
                ("3 - 1 - 4 - 2", "3 - 1 - 4 - 2")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is 3 → 1 → 2 → 4:\n- 3. Mirdha Committee (1965)\n- 1. Ardhanareeswaran Committee (1987)\n- 2. Brahm Perkash Committee (1991)\n- 4. Vaidyanathan Committee (2004).\nHence, the correct sequence is 3 - 1 - 2 - 4.",
            "exp_ta": "சரியான காலவரிசை 3 → 1 → 2 → 4:\n- 3. மிர்தா குழு (1965)\n- 1. அர்த்தநாரீஸ்வரன் குழு (1987)\n- 2. பிரம்ம பிரகாஷ் குழு (1991)\n- 4. வைத்தியநாதன் குழு (2004).\nஎனவே, சரியான வரிசை 3 - 1 - 2 - 4 ஆகும்.",
            "why_a_en": "Correct sequence: 1965 (Mirdha) → 1987 (Ardhanareeswaran) → 1991 (Brahm Perkash) → 2004 (Vaidyanathan).",
            "why_a_ta": "சரியான காலவரிசை: 1965 (மிர்தா) → 1987 (அர்த்தநாரீஸ்வரன்) → 1991 (பிரம்ம பிரகாஷ்) → 2004 (வைத்தியநாதன்).",
            "why_b_en": "Incorrect. Mirdha Committee (1965) preceded Ardhanareeswaran (1987).",
            "why_b_ta": "தவறு. 1987 அர்த்தநாரீஸ்வரன் குழுவிற்கு முன்பே 1965 மிர்தா குழு அமைந்தது.",
            "why_c_en": "Incorrect. Ardhanareeswaran (1987) preceded Brahm Perkash (1991).",
            "why_c_ta": "தவறு. பிரம்ம பிரகாஷ் குழுவிற்கு முன் அர்த்தநாரீஸ்வரன் குழு அறிக்கை அளித்தது.",
            "why_d_en": "Incorrect. Vaidyanathan was in 2004, after Brahm Perkash (1991).",
            "why_d_ta": "தவறு. வைத்தியநாதன் குழு 2004-ல் அமைந்தது.",
            "tip_en": "Reforms Sequence: Mirdha (1965) → Ardhanareeswaran (1987) → Brahm Perkash (1991) → Vaidyanathan (2004).",
            "tip_ta": "சீர்திருத்த வரிசை: மிர்தா (1965) → அர்த்தநாரீஸ்வரன் (1987) → பிரம்ம பிரகாஷ் (1991) → வைத்தியநாதன் (2004).",
            "fact_en": "Ardhanareeswaran Committee was the first to recommend removing the Registrar's power to supersede elected boards arbitrarily.",
            "fact_ta": "தேர்ந்தெடுக்கப்பட்ட வாரியங்களை தன்னிச்சையாகக் கலைக்கும் பதிவாளரின் அதிகாரத்தை நீக்க அர்த்தநாரீஸ்வரன் குழுவே முதலில் பரிந்துரைத்தது."
        },

        # CS_C_023: Housing Cooperatives Institutional Evolution
        {
            "subtopic": "Housing Cooperatives Milestones",
            "stem_en": "Arrange the following institutional milestones in cooperative housing in India in chronological order:\n1. National Cooperative Housing Federation of India (NCHF) established\n2. First Cooperative Housing Society established in Bangalore\n3. Tamil Nadu Co-operative Housing Federation (TNCHF) formed\n4. National Housing Bank (NHB) established as apex housing finance regulator",
            "stem_ta": "இந்தியாவில் கூட்டுறவு வீட்டுவசதி அமைப்புகளின் பின்வரும் மைல்கற்களை காலவரிசைப்படி ஒழுங்குபடுத்துக:\n1. இந்திய தேசிய கூட்டுறவு வீட்டுவசதி கூட்டமைப்பு (NCHF) நிறுவப்படுதல்\n2. இந்தியாவின் முதல் கூட்டுறவு வீட்டுவசதி சங்கம் பெங்களூரில் தொடங்கப்படுதல்\n3. தமிழ்நாடு கூட்டுறவு வீட்டுவசதி கூட்டமைப்பு (TNCHF) உருவாக்கப்படுதல்\n4. தேசிய வீட்டுவசதி வங்கி (NHB) உச்ச வீட்டுவசதி நிதி ஒழுங்குமுறை அமைப்பாக நிறுவப்படுதல்",
            "options": [
                ("2 - 3 - 1 - 4", "2 - 3 - 1 - 4"),
                ("3 - 2 - 1 - 4", "3 - 2 - 1 - 4"),
                ("2 - 1 - 3 - 4", "2 - 1 - 3 - 4"),
                ("1 - 2 - 3 - 4", "1 - 2 - 3 - 4")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is 2 → 3 → 1 → 4:\n- 2. First cooperative housing society in Bangalore (1909)\n- 3. Tamil Nadu Co-operative Housing Federation set up (1959)\n- 1. National Cooperative Housing Federation of India set up (1969)\n- 4. National Housing Bank established (1988).\nHence, the correct sequence is 2 - 3 - 1 - 4.",
            "exp_ta": "சரியான காலவரிசை 2 → 3 → 1 → 4:\n- 2. பெங்களூரில் முதல் கூட்டுறவு வீட்டுவசதி சங்கம் (1909)\n- 3. தமிழ்நாடு கூட்டுறவு வீட்டுவசதி கூட்டமைப்பு தொடக்கம் (1959)\n- 1. இந்திய தேசிய கூட்டுறவு வீட்டுவசதி கூட்டமைப்பு (NCHF) உருவாக்கம் (1969)\n- 4. தேசிய வீட்டுவசதி வங்கி (NHB) நிறுவப்படுதல் (1988).\nஎனவே, சரியான வரிசை 2 - 3 - 1 - 4 ஆகும்.",
            "why_a_en": "Correct sequence: 1909 (Bangalore Society) → 1959 (TNCHF) → 1969 (NCHF) → 1988 (NHB).",
            "why_a_ta": "சரியான காலவரிசை: 1909 (பெங்களூர்) → 1959 (TNCHF) → 1969 (NCHF) → 1988 (NHB).",
            "why_b_en": "Incorrect. Bangalore society (1909) was the earliest.",
            "why_b_ta": "தவறு. 1909 பெங்களூர் சங்கம் முதலாவது.",
            "why_c_en": "Incorrect. TNCHF (1959) preceded NCHF (1969).",
            "why_c_ta": "தவறு. NCHF-க்கு முன்பே 1959-ல் தமிழக கூட்டமைப்பு உருவானது.",
            "why_d_en": "Incorrect. NCHF was in 1969, not first.",
            "why_d_ta": "தவறு. NCHF 1969-ல் உருவானது.",
            "tip_en": "Housing Timeline: 1909 (Bangalore) → 1959 (TNCHF) → 1969 (NCHF) → 1988 (NHB).",
            "tip_ta": "வீட்டுவசதி காலக்கோடு: 1909 (பெங்களூர்) → 1959 (TNCHF) → 1969 (NCHF) → 1988 (NHB).",
            "fact_en": "Cooperative housing societies have constructed over 25 lakh housing units across India.",
            "fact_ta": "கூட்டுறவு வீட்டுவசதி சங்கங்கள் நாடு முழுவதும் 25 லட்சத்திற்கும் மேற்பட்ட வீடுகளைக் கட்டியுள்ளன."
        },

        # CS_C_024: Recent Regulatory and Judicial Milestones
        {
            "subtopic": "2020-2023 Regulatory Milestones",
            "stem_en": "Arrange the following landmark regulatory and judicial events affecting cooperative societies in chronological order:\n1. Multi-State Co-operative Societies (Amendment) Act passed by Parliament\n2. Creation of the dedicated Union Ministry of Cooperation\n3. Banking Regulation (Amendment) Act passed bringing UCBs under direct RBI oversight\n4. Supreme Court judgment in Union of India v. Rajendra N. Shah (20 July)",
            "stem_ta": "கூட்டுறவு சங்கங்கள் தொடர்பான பின்வரும் சமீபத்திய ஒழுங்குமுறை மற்றும் நீதித்துறை நிகழ்வுகளை காலவரிசைப்படி ஒழுங்குபடுத்துக:\n1. நாடாளுமன்றத்தால் பல மாநில கூட்டுறவு சங்கங்கள் (திருத்தச்) சட்டம் நிறைவேற்றப்படுதல்\n2. தனி மத்திய கூட்டுறவு அமைச்சகம் உருவாக்கப்படுதல் (6 ஜூலை)\n3. UCBs-ஐ ரிசர்வ் வங்கியின் நேரடி கண்காணிப்பில் கொண்டுவந்த வங்கி ஒழுங்குமுறை (திருத்தச்) சட்டம்\n4. இந்திய ஒன்றியம் எதிர் ராஜேந்திர என். ஷா வழக்கில் உச்சநீதிமன்றத் தீர்ப்பு (20 ஜூலை)",
            "options": [
                ("3 - 2 - 4 - 1", "3 - 2 - 4 - 1"),
                ("2 - 3 - 4 - 1", "2 - 3 - 4 - 1"),
                ("3 - 4 - 2 - 1", "3 - 4 - 2 - 1"),
                ("4 - 3 - 2 - 1", "4 - 3 - 2 - 1")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is 3 → 2 → 4 → 1:\n- 3. Banking Regulation (Amendment) Act passed (September 2020)\n- 2. Creation of Ministry of Cooperation (6 July 2021)\n- 4. Supreme Court verdict in Rajendra N. Shah (20 July 2021)\n- 1. Multi-State Co-operative Societies (Amendment) Act passed (August 2023).\nHence, the correct sequence is 3 - 2 - 4 - 1.",
            "exp_ta": "சரியான காலவரிசை 3 → 2 → 4 → 1:\n- 3. வங்கி ஒழுங்குமுறை (திருத்தச்) சட்டம் (செப்டம்பர் 2020)\n- 2. கூட்டுறவு அமைச்சகம் உருவாக்கம் (6 ஜூலை 2021)\n- 4. ராஜேந்திர ஷா வழக்கில் உச்சநீதிமன்றத் தீர்ப்பு (20 ஜூலை 2021)\n- 1. பல மாநில கூட்டுறவு திருத்தச் சட்டம் (ஆகஸ்ட் 2023).\nஎனவே, சரியான வரிசை 3 - 2 - 4 - 1 ஆகும்.",
            "why_a_en": "Correct sequence: Sep 2020 (BR Amendment) → 6 Jul 2021 (Ministry) → 20 Jul 2021 (SC Judgment) → Aug 2023 (MSCS Amendment).",
            "why_a_ta": "சரியான காலவரிசை: செப் 2020 → 6 ஜூலை 2021 → 20 ஜூலை 2021 → ஆகஸ்ட் 2023.",
            "why_b_en": "Incorrect. BR Amendment was passed in 2020, before the Ministry was created in July 2021.",
            "why_b_ta": "தவறு. 2020-லேயே வங்கித் திருத்தம் வந்தது, அமைச்சகம் 2021-ல் உருவானது.",
            "why_c_en": "Incorrect. Ministry creation (6 July 2021) happened 14 days before the Supreme Court judgment (20 July 2021).",
            "why_c_ta": "தவறு. ஜூலை 6-ல் அமைச்சகம் உருவானது, ஜூலை 20-ல் உச்சநீதிமன்றத் தீர்ப்பு வந்தது.",
            "why_d_en": "Incorrect. Supreme Court verdict was in 2021, not first.",
            "why_d_ta": "தவறு. உச்சநீதிமன்றத் தீர்ப்பு 2021-ல் வந்தது.",
            "tip_en": "Crucial Dates: 6 July 2021 = Ministry created; 20 July 2021 = Supreme Court Rajendra Shah verdict.",
            "tip_ta": "முக்கிய தேதிகள்: 6 ஜூலை 2021 = அமைச்சகம் உருவாக்கம்; 20 ஜூலை 2021 = உச்சநீதிமன்றத் தீர்ப்பு.",
            "fact_en": "The Ministry of Cooperation was created just two weeks before the Supreme Court severed Part IX-B.",
            "fact_ta": "உச்சநீதிமன்றம் பகுதி IX-B-ஐப் பிரித்து தீர்ப்பளிப்பதற்கு இரண்டு வாரங்களுக்கு முன்பே கூட்டுறவு அமைச்சகம் உருவாக்கப்பட்டது."
        },

        # CS_C_025: Grand National Initiatives Trajectory
        {
            "subtopic": "2021-2024 Transformation Trajectory",
            "stem_en": "Arrange the following transformative initiatives in chronological order:\n1. Commercial rollout of 'Bharat Organics' brand by National Cooperative Organics Limited (NCOL)\n2. Centrally Sponsored Project for PACS Computerization approved by Cabinet\n3. Official Creation of Ministry of Cooperation\n4. Inauguration of the National Cooperative Database covering 8+ lakh societies",
            "stem_ta": "கூட்டுறவுத் துறையின் பின்வரும் மாற்றத்தக்க தேசிய முயற்சிகளை காலவரிசைப்படி ஒழுங்குபடுத்துக:\n1. NCOL அமைப்பால் 'பாரத் ஆர்கானிக்ஸ்' பிராண்ட் அதிகாரப்பூர்வமாக சந்தையில் அறிமுகப்படுத்தப்படுதல்\n2. PACS கணினிமயமாக்கலுக்கான மத்திய நிதியுதவித் திட்டத்திற்கு அமைச்சரவை ஒப்புதல் அளித்தல்\n3. அதிகாரப்பூர்வமாக தனி கூட்டுறவு அமைச்சகம் உருவாக்கப்படுதல்\n4. 8 லட்சத்திற்கும் மேற்பட்ட சங்கங்களை உள்ளடக்கிய தேசிய கூட்டுறவு தரவுத்தளம் தொடங்கி வைக்கப்படுதல்",
            "options": [
                ("3 - 2 - 1 - 4", "3 - 2 - 1 - 4"),
                ("2 - 3 - 1 - 4", "2 - 3 - 1 - 4"),
                ("3 - 1 - 2 - 4", "3 - 1 - 2 - 4"),
                ("1 - 3 - 2 - 4", "1 - 3 - 2 - 4")
            ],
            "correct_key": "A",
            "exp_en": "The correct chronological order is 3 → 2 → 1 → 4:\n- 3. Creation of Ministry of Cooperation (July 2021)\n- 2. Cabinet approved PACS Computerization Project (June 2022)\n- 1. Bharat Organics brand launched under NCOL (November 2023)\n- 4. National Cooperative Database dedicated to nation (March 2024).\nHence, the correct sequence is 3 - 2 - 1 - 4.",
            "exp_ta": "சரியான காலவரிசை 3 → 2 → 1 → 4:\n- 3. தனி கூட்டுறவு அமைச்சகம் உருவாக்கம் (ஜூலை 2021)\n- 2. PACS கணினிமயமாக்கல் திட்டத்திற்கு அமைச்சரவை ஒப்புதல் (ஜூன் 2022)\n- 1. பாரத் ஆர்கானிக்ஸ் பிராண்ட் அறிமுகம் (நவம்பர் 2023)\n- 4. தேசிய கூட்டுறவு தரவுத்தளம் நாட்டுக்கு அர்ப்பணிப்பு (மார்ச் 2024).\nஎனவே, சரியான வரிசை 3 - 2 - 1 - 4 ஆகும்.",
            "why_a_en": "Correct sequence: Jul 2021 (Ministry) → Jun 2022 (PACS ERP) → Nov 2023 (Bharat Organics) → Mar 2024 (Database).",
            "why_a_ta": "சரியான காலவரிசை: ஜூலை 2021 → ஜூன் 2022 → நவம்பர் 2023 → மார்ச் 2024.",
            "why_b_en": "Incorrect. Ministry creation (2021) preceded the PACS project approval (2022).",
            "why_b_ta": "தவறு. 2021 அமைச்சக உருவாக்கத்திற்குப் பிறகே 2022-ல் PACS திட்டம் வந்தது.",
            "why_c_en": "Incorrect. PACS project (2022) preceded Bharat Organics (2023).",
            "why_c_ta": "தவறு. 2022 PACS திட்டத்திற்குப் பிறகே 2023 பாரத் ஆர்கானிக்ஸ் வந்தது.",
            "why_d_en": "Incorrect. Bharat Organics was in 2023, not first.",
            "why_d_ta": "தவறு. பாரத் ஆர்கானிக்ஸ் 2023-ல் வந்தது.",
            "tip_en": "2021-2024 Trajectory: Ministry (2021) → PACS ERP (2022) → Bharat Organics (2023) → National Database (2024).",
            "tip_ta": "மாற்ற காலக்கோடு: அமைச்சகம் (2021) → PACS கணினி (2022) → பாரத் ஆர்கானிக்ஸ் (2023) → தரவுத்தளம் (2024).",
            "fact_en": "The national cooperative transformation aims to establish 2 lakh new multipurpose primary societies across uncovered gram panchayats.",
            "fact_ta": "கூட்டுறவு இல்லாத கிராம ஊராட்சிகளில் 2 லட்சம் புதிய பலநோக்கு தொடக்கச் சங்கங்களை அமைப்பதே இந்த மாற்றத்தின் உச்ச இலக்காகும்."
        }
    ]


def build_chronology_file():
    raw_list = (
        get_chronology_raw_questions() +
        get_chronology_questions_batch2() +
        get_chronology_questions_batch3() +
        get_chronology_questions_batch4() +
        get_chronology_questions_batch5()
    )
    print(f"Loaded {len(raw_list)} raw Chronology questions.")
    assert len(raw_list) == 25, f"Expected 25 questions, got {len(raw_list)}"

    questions = []
    for idx, item in enumerate(raw_list, start=1):
        qid = f"CS_C_{idx:03d}"
        opts = item["options"]
        correct_key = item["correct_key"]

        q = make_coop_q(
            qid=qid,
            diff="Hard",
            qtype="chronology",
            subtopic=item["subtopic"],
            en_stem=item["stem_en"],
            ta_stem=item["stem_ta"],
            en_a=opts[0][0],
            ta_a=opts[0][1],
            en_b=opts[1][0],
            ta_b=opts[1][1],
            en_c=opts[2][0],
            ta_c=opts[2][1],
            en_d=opts[3][0],
            ta_d=opts[3][1],
            correct_key=correct_key,
            exp_en=item["exp_en"],
            exp_ta=item["exp_ta"],
            why_a_en=item["why_a_en"],
            why_a_ta=item["why_a_ta"],
            why_b_en=item["why_b_en"],
            why_b_ta=item["why_b_ta"],
            why_c_en=item["why_c_en"],
            why_c_ta=item["why_c_ta"],
            why_d_en=item["why_d_en"],
            why_d_ta=item["why_d_ta"],
            tip_en=item["tip_en"],
            tip_ta=item["tip_ta"],
            fact_en=item["fact_en"],
            fact_ta=item["fact_ta"],
            tags=["polity", "cooperative_societies", "chronology", item["subtopic"].lower().replace(" ", "_")]
        )
        questions.append(q)

    # Randomize and balance answer keys: 6-7 per option, max run <= 2
    balanced = randomize_and_balance_dataset(questions, seed=505)
    key_dist = Counter(q["correct_answer"] for q in balanced)
    print(f"Balanced Key Distribution: {dict(key_dist)}")

    out_dir = os.path.join("data", "questions", "polity")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "cooperative_societies_chronology.json")

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(balanced, f, ensure_ascii=False, indent=2)
    print(f"Saved balanced Chronology MCQs to {out_path}")

    # Chronology Validator Check
    c_rep = ChronologyValidator.validate_file(out_path)
    print("--- Chronology Validator Audit ---")
    print(c_rep.format_final_report())
    if not c_rep.is_valid:
        print("Chronology validation failed!")
        for iss in c_rep.issues:
            print("  -", iss)
        return False

    # Suite Validator Check
    rep = ContentValidator.validate_file(out_path, expected_count=25, expected_prefix="CS_C_")
    print(f"Content Validation: {'PASS' if rep.is_valid else 'FAIL'} | Total: {rep.total_audited}")
    print(f"Keys: {rep.key_distribution}")
    if not rep.is_valid:
        for iss in rep.issues:
            print("  Issue:", iss.severity, iss.field_name, iss.message)
        return False

    return True


if __name__ == "__main__":
    success = build_chronology_file()
    if not success:
        exit(1)
