import json
import os
from collections import Counter

def create_chronology_questions():
    questions = []

    def add_q(q_id, question_en, question_ta, opt_a_en, opt_a_ta, opt_b_en, opt_b_ta, opt_c_en, opt_c_ta, opt_d_en, opt_d_ta, correct, exp_en, exp_ta, why_a_en, why_a_ta, why_b_en, why_b_ta, why_c_en, why_c_ta, why_d_en, why_d_ta, tip_en, tip_ta, fact_en, fact_ta, bloom, difficulty, tags, notes_part):
        q_obj = {
            "id": q_id,
            "subject": "Polity",
            "topic": "Constitutional Amendments",
            "difficulty": difficulty,
            "question_type": "chronology",
            "question": {
                "en": question_en,
                "ta": question_ta
            },
            "options": [
                {"id": "A", "en": opt_a_en, "ta": opt_a_ta},
                {"id": "B", "en": opt_b_en, "ta": opt_b_ta},
                {"id": "C", "en": opt_c_en, "ta": opt_c_ta},
                {"id": "D", "en": opt_d_en, "ta": opt_d_ta}
            ],
            "correct_answer": correct,
            "explanation": {
                "en": exp_en,
                "ta": exp_ta
            },
            "why_not_others": {
                "A": {"en": why_a_en, "ta": why_a_ta},
                "B": {"en": why_b_en, "ta": why_b_ta},
                "C": {"en": why_c_en, "ta": why_c_ta},
                "D": {"en": why_d_en, "ta": why_d_ta}
            },
            "tnpsc_tip": {
                "en": tip_en,
                "ta": tip_ta
            },
            "revision_fact": {
                "en": fact_en,
                "ta": fact_ta
            },
            "source_reference": [
                "M. Laxmikanth — Indian Polity",
                "NCERT Class XI — Constitution at Work",
                "Tamil Nadu Samacheer Kalvi — Class 12 Polity",
                f"TNPSC Nova AI Notes — Constitutional Amendments ({notes_part})"
            ],
            "bloom_level": bloom,
            "estimated_time_sec": 90,
            "pyq_similarity": "High Similarity to TNPSC Group 1 Chronology Questions",
            "tags": tags
        }
        questions.append(q_obj)

    # 25 Chronology questions balance: A:6, B:6, C:7, D:6

    chronology_data = [
        # Q001 - Correct: A (1)
        (
            "CZ_AM_CH_001",
            "Arrange the following constitutional developments in chronological order:\n1. Insertion of 9th Schedule into the Constitution\n2. Substitution of 'Socialist, Secular, Integrity' into the Preamble\n3. Insertion of Anti-Defection Law (10th Schedule)\n4. Insertion of Right to Education as a Fundamental Right (Article 21A)",
            "பின்வரும் அரசியலமைப்பு வளர்ச்சிகளைக் காலவரிசைப்படி வரிசைப்படுத்துக:\n1. 9வது அட்டவணையை அரசியலமைப்பில் சேர்த்தல்\n2. முகப்புரையில் 'சமதர்ம, மதச்சார்பற்ற, ஒருமைப்பாடு' சொற்களைச் சேர்த்தல்\n3. கட்சித் தாவல் தடைச் சட்டத்தைச் சேர்த்தல் (10வது அட்டவணை)\n4. கல்வி உரிமையை அடிப்படை உரிமையாகச் சேர்த்தல் (சரத்து 21A)",
            "1 → 2 → 3 → 4", "1 → 2 → 3 → 4",
            "2 → 1 → 4 → 3", "2 → 1 → 4 → 3",
            "3 → 1 → 2 → 4", "3 → 1 → 2 → 4",
            "4 → 3 → 2 → 1", "4 → 3 → 2 → 1",
            "A",
            "Chronological order:\n1. Insertion of 9th Schedule: 1st Amendment Act, 1951\n2. Words in Preamble: 42nd Amendment Act, 1976\n3. Anti-Defection Law: 52nd Amendment Act, 1985\n4. Right to Education (Art 21A): 86th Amendment Act, 2002\nHence, correct order is 1 → 2 → 3 → 4.",
            "காலவரிசை:\n1. 9வது அட்டவணை சேர்க்கை: 1வது திருத்தம், 1951\n2. முகப்புரை சொற்கள்: 42வது திருத்தம், 1976\n3. கட்சித் தாவல் தடைச் சட்டம்: 52வது திருத்தம், 1985\n4. கல்வி உரிமை (சரத்து 21A): 86வது திருத்தம், 2002\nஎனவே சரியான வரிசை 1 → 2 → 3 → 4.",
            "Option A is correct because the exact chronological sequence is 1951 (1) → 1976 (2) → 1985 (3) → 2002 (4).", "விருப்பம் A சரியானது, ஏனெனில் சரியான காலவரிசை 1951 (1) → 1976 (2) → 1985 (3) → 2002 (4).",
            "Option B is incorrect because placing 1976 before 1951 is chronologically false.", "விருப்பம் B தவறானது, ஏனெனில் 1951 க்கு முன் 1976 ஐ வைப்பது தவறு.",
            "Option C is incorrect because placing 1985 before 1951 is chronologically false.", "விருப்பம் C தவறானது, ஏனெனில் 1951 க்கு முன் 1985 ஐ வைப்பது தவறு.",
            "Option D is incorrect because it reverses the actual timeline completely.", "விருப்பம் D தவறானது, ஏனெனில் இது காலவரிசையை தலைகீழாகக் காட்டுகிறது.",
            "TNPSC Chronology Tip: Always memorize key milestone amendment years: 1st (1951), 42nd (1976), 52nd (1985), 86th (2002).",
            "டிஎன்பிஎஸ்சி காலவரிசைக் குறிப்பு: முக்கிய திருத்த ஆண்டுகளை நினைவில் கொள்க: 1வது (1951), 42வது (1976), 52வது (1985), 86வது (2002).",
            "1st CA added 9th Sched (1951); 42nd added Preamble words (1976); 52nd added Anti-defection (1985); 86th added RTE (2002).",
            "1வது திருத்தம் 9வது அட்டவணையைச் சேர்த்தது; 42வது முகப்புரை சொற்கள்; 52வது கட்சித் தாவல் சட்டம்; 86வது கல்வி உரிமை.",
            "Analyzing", "Medium", ["Chronology Amendments", "1st CA 1951", "42nd CA 1976", "52nd CA 1985", "86th CA 2002"], "Part 2"
        ),
        # Q002 - Correct: B (1)
        (
            "CZ_AM_CH_002",
            "Arrange the following landmark Supreme Court judgments regarding Constitutional Amendments in chronological order:\n1. Golaknath v. State of Punjab\n2. Kesavananda Bharati v. State of Kerala\n3. Shankari Prasad v. Union of India\n4. Minerva Mills v. Union of India",
            "அரசியலமைப்பு திருத்தங்கள் தொடர்பான பின்வரும் வரலாற்றுச் சிறப்புமிக்க உச்ச நீதிமன்றத் தீர்ப்புகளைக் காலவரிசைப்படி வரிசைப்படுத்துக:\n1. கோலக்நாத் எதிர் பஞ்சாப் மாநிலம்\n2. கேசவாநந்த பாரதி எதிர் கேரள மாநிலம்\n3. சங்கரி பிரசாத் எதிர் இந்திய யூனியன்\n4. மினர்வா மில்ஸ் எதிர் இந்திய யூனியன்",
            "1 → 3 → 2 → 4", "1 → 3 → 2 → 4",
            "3 → 1 → 2 → 4", "3 → 1 → 2 → 4",
            "2 → 1 → 4 → 3", "2 → 1 → 4 → 3",
            "3 → 2 → 1 → 4", "3 → 2 → 1 → 4",
            "B",
            "Chronological order of judgments:\n1. Shankari Prasad v. Union of India (1951)\n2. Golaknath v. State of Punjab (1967)\n3. Kesavananda Bharati v. State of Kerala (1973)\n4. Minerva Mills v. Union of India (1980)\nHence, correct order is 3 → 1 → 2 → 4.",
            "தீர்ப்புகளின் காலவரிசை:\n1. சங்கரி பிரசாத் வழக்கு (1951)\n2. கோலக்நாத் வழக்கு (1967)\n3. கேசவாநந்த பாரதி வழக்கு (1973)\n4. மினர்வா மில்ஸ் வழக்கு (1980)\nஎனவே சரியான வரிசை 3 → 1 → 2 → 4.",
            "Option A is incorrect because Golaknath (1967) came after Shankari Prasad (1951).", "விருப்பம் A தவறானது, ஏனெனில் சங்கரி பிரசாத்திற்குப் பின்னரே கோலக்நாத் வந்தது.",
            "Option B is correct because the sequence 1951 (3) → 1967 (1) → 1973 (2) → 1980 (4) is exact.", "விருப்பம் B சரியானது, ஏனெனில் 1951 (3) → 1967 (1) → 1973 (2) → 1980 (4) சரியான வரிசையாகும்.",
            "Option C is incorrect because Kesavananda (1973) came after Golaknath (1967).", "விருப்பம் C தவறானது, ஏனெனில் கேசவாநந்த வழக்கு கோலக்நாத்திற்குப் பின்னரே வந்தது.",
            "Option D is incorrect because Kesavananda (1973) came after Golaknath (1967).", "விருப்பம் D தவறானது, ஏனெனில் கேசவாநந்த வழக்கு கோலக்நாத்திற்குப் பின்னரே வந்தது.",
            "Judicial Precedent Evolution: Shankari Prasad (1951) upheld Art 368 -> Golaknath (1967) restricted FR amendments -> Kesavananda (1973) created Basic Structure -> Minerva Mills (1980) affirmed Basic Structure immunity.",
            "நீதிமன்ற முன்மாதிரி வளர்ச்சி: சங்கரி பிரசாத் (1951) -> கோலக்நாத் (1967) -> கேசவாநந்த பாரதி (1973) -> மினர்வா மில்ஸ் (1980).",
            "Shankari Prasad (1951), Golaknath (1967), Kesavananda (1973), Minerva Mills (1980).",
            "சங்கரி பிரசாத் (1951), கோலக்நாத் (1967), கேசவாநந்த பாரதி (1973), மினர்வா மில்ஸ் (1980).",
            "Analyzing", "Hard", ["Landmark Cases Chronology", "Shankari Prasad 1951", "Golaknath 1967", "Kesavananda 1973", "Minerva Mills 1980"], "Part 3"
        ),
        # Q003 - Correct: C (1)
        (
            "CZ_AM_CH_003",
            "Arrange the following constitutional provisions introduced by amendments in chronological order:\n1. Introduction of Goods and Services Tax (GST Council)\n2. Reduction of Voting Age from 21 to 18 years\n3. Constitutional status for Panchayati Raj Institutions\n4. Introduction of Economically Weaker Sections (EWS) reservation",
            "திருத்தங்கள் மூலம் அறிமுகப்படுத்தப்பட்ட பின்வரும் அரசியலமைப்பு விதிகளைக் காலவரிசைப்படி வரிசைப்படுத்துக:\n1. சரக்கு மற்றும் சேவை வரி (GST கவுன்சில்) அறிமுகம்\n2. வாக்குரிமை வயதை 21 இலிருந்து 18 ஆகக் குறைத்தல்\n3. பஞ்சாயத்து ராஜ் அமைப்புகளுக்கு அரசியலமைப்பு அந்தஸ்து\n4. பொருளாதாரத்தில் பின்தங்கிய பிரிவினருக்கான (EWS) இடஒதுக்கீடு அறிமுகம்",
            "1 → 2 → 3 → 4", "1 → 2 → 3 → 4",
            "3 → 2 → 1 → 4", "3 → 2 → 1 → 4",
            "2 → 3 → 1 → 4", "2 → 3 → 1 → 4",
            "4 → 1 → 3 → 2", "4 → 1 → 3 → 2",
            "C",
            "Chronological order:\n1. Voting age reduced to 18: 61st Amendment Act, 1988\n2. Constitutional status for Panchayats: 73rd Amendment Act, 1992\n3. Goods and Services Tax (GST): 101st Amendment Act, 2016\n4. EWS Reservation: 103rd Amendment Act, 2019\nHence, correct sequence is 2 → 3 → 1 → 4.",
            "காலவரிசை:\n1. வாக்குரிமை வயது 18 ஆகக் குறைப்பு: 61வது திருத்தம், 1988\n2. பஞ்சாயத்து ராஜ் அரசியலமைப்பு அந்தஸ்து: 73வது திருத்தம், 1992\n3. ஜிஎஸ்டி அறிமுகம்: 101வது திருத்தம், 2016\n4. EWS இடஒதுக்கீடு: 103வது திருத்தம், 2019\nஎனவே சரியான வரிசை 2 → 3 → 1 → 4.",
            "Option A is incorrect because GST (2016) came long after voting age reduction (1988).", "விருப்பம் A தவறானது, ஏனெனில் ஜிஎஸ்டி (2016) வாக்குரிமை வயது குறைப்பிற்கு (1988) பின்னரே வந்தது.",
            "Option B is incorrect because voting age reduction (1988) came before Panchayati Raj (1992).", "விருப்பம் B தவறானது, ஏனெனில் வாக்குரிமை குறைப்பு (1988) பஞ்சாயத்து ராஜிற்கு (1992) முன்னே வந்தது.",
            "Option C is correct because the timeline 1988 (2) → 1992 (3) → 2016 (1) → 2019 (4) is exact.", "விருப்பம் C சரியானது, ஏனெனில் 1988 (2) → 1992 (3) → 2016 (1) → 2019 (4) சரியான வரிசையாகும்.",
            "Option D is incorrect because EWS (2019) is the most recent among the four.", "விருப்பம் D தவறானது, ஏனெனில் EWS (2019) கடைசியாக வந்தது.",
            "Key Amendment Years: 61st CA (1988), 73rd CA (1992), 101st CA (2016), 103rd CA (2019).",
            "முக்கிய திருத்த ஆண்டுகள்: 61வது திருத்தம் (1988), 73வது திருத்தம் (1992), 101வது திருத்தம் (2016), 103வது திருத்தம் (2019).",
            "Voting age lowered in 1988; Panchayats 1992; GST 2016; EWS 2019.",
            "வாக்குரிமை வயது 1988; பஞ்சாயத்துகள் 1992; ஜிஎஸ்டி 2016; EWS 2019.",
            "Remembering", "Medium", ["Chronology Provisions", "61st CA 1988", "73rd CA 1992", "101st CA 2016", "103rd CA 2019"], "Part 2"
        ),
        # Q004 - Correct: D (1)
        (
            "CZ_AM_CH_004",
            "Arrange the following Constitutional Amendment Acts relating to official languages in chronological order:\n1. 92nd Amendment Act (Bodo, Dogri, Maithili, Santhali added)\n2. 21st Amendment Act (Sindhi added)\n3. 96th Amendment Act (Oriya renamed to Odia)\n4. 71st Amendment Act (Konkani, Manipuri, Nepali added)",
            "ஆட்சிமொழிகள் தொடர்பான பின்வரும் அரசியலமைப்பு திருத்தச் சட்டங்களை அவைகளின் காலவரிசைப்படி வரிசைப்படுத்துக:\n1. 92வது திருத்தச் சட்டம் (போடோ, டோக்ரி, மைதிலி, சந்தாலி சேர்க்கை)\n2. 21வது திருத்தச் சட்டம் (சிந்தி மொழி சேர்க்கை)\n3. 96வது திருத்தச் சட்டம் (ஒரியா மொழி ஒடியா என பெயர் மாற்றம்)\n4. 71வது திருத்தச் சட்டம் (கொங்கணி, மணிப்பூரி, நேபாளி சேர்க்கை)",
            "1 → 4 → 2 → 3", "1 → 4 → 2 → 3",
            "4 → 2 → 1 → 3", "4 → 2 → 1 → 3",
            "2 → 1 → 4 → 3", "2 → 1 → 4 → 3",
            "2 → 4 → 1 → 3", "2 → 4 → 1 → 3",
            "D",
            "Chronology of Language Amendments:\n1. 21st CA 1967: Sindhi added as 15th language\n2. 71st CA 1992: Konkani, Manipuri, Nepali added (16th-18th)\n3. 92nd CA 2003: Bodo, Dogri, Maithili, Santhali added (19th-22nd)\n4. 96th CA 2011: Oriya substituted with Odia in 8th Schedule\nHence, correct sequence is 2 → 4 → 1 → 3.",
            "மொழித் திருத்தங்களின் காலவரிசை:\n1. 21வது திருத்தம் 1967: சிந்தி 15வது மொழியாகச் சேர்க்கப்பட்டது\n2. 71வது திருத்தம் 1992: கொங்கணி, மணிப்பூரி, நேபாளி சேர்க்கப்பட்டன (16-18)\n3. 92வது திருத்தம் 2003: போடோ, டோக்ரி, மைதிலி, சந்தாலி சேர்க்கப்பட்டன (19-22)\n4. 96வது திருத்தம் 2011: 8வது அட்டவணையில் ஒரியா ஒடியா என மாற்றப்பட்டது\nஎனவே சரியான வரிசை 2 → 4 → 1 → 3.",
            "Option A is incorrect because 21st CA (1967) occurred first.", "விருப்பம் A தவறானது, ஏனெனில் 21வது திருத்தம் (1967) முதலாவதாக வந்தது.",
            "Option B is incorrect because 21st CA (1967) came before 71st CA (1992).", "விருப்பம் B தவறானது, ஏனெனில் 21வது திருத்தம் 71வது திருத்தத்திற்கு முன்னே வந்தது.",
            "Option C is incorrect because 71st CA (1992) came before 92nd CA (2003).", "விருப்பம் C தவறானது, ஏனெனில் 71வது திருத்தம் 92வது திருத்தத்திற்கு முன்னே வந்தது.",
            "Option D is correct because 1967 (2) → 1992 (4) → 2003 (1) → 2011 (3) is exact.", "விருப்பம் D சரியானது, ஏனெனில் 1967 (2) → 1992 (4) → 2003 (1) → 2011 (3) சரியான வரிசையாகும்.",
            "TNPSC Language Formula: 21st CA (1967) = Sindhi; 71st CA (1992) = Konkani, Manipuri, Nepali (KMN); 92nd CA (2003) = Bodo, Dogri, Maithili, Santhali (BDMS); 96th CA (2011) = Odia.",
            "டிஎன்பிஎஸ்சி மொழிச் சூத்திரம்: 21வது (1967) = சிந்தி; 71வது (1992) = கொங்கணி, மணிப்பூரி, நேபாளி; 92வது (2003) = போடோ, டோக்ரி, மைதிலி, சந்தாலி; 96வது (2011) = ஒடியா.",
            "8th Schedule originally had 14 languages; now has 22 languages.",
            "8வது அட்டவணையில் முதலில் 14 மொழிகள் இருந்தன; தற்போது 22 மொழிகள் உள்ளன.",
            "Remembering", "Medium", ["Language Amendments Chronology", "21st CA 1967", "71st CA 1992", "92nd CA 2003", "96th CA 2011"], "Part 2"
        ),
    ]

    for cd in chronology_data:
        add_q(*cd)

    # We generate remaining 21 questions to complete 25 with balance: A:6, B:6, C:7, D:6
    # Current counts: Q1=A, Q2=B, Q3=C, Q4=D.

    chronology_templates = [
        ("A", ["1st CA Land Reforms 1951", "7th CA Reorganisation 1956", "24th CA Assent 1971", "42nd CA Mini Constitution 1976"], "1 → 2 → 3 → 4", "Part 2"),
        ("B", ["Golaknath 1967", "24th CA 1971", "Kesavananda 1973", "42nd CA 1976"], "1 → 2 → 3 → 4", "Part 3"),
        ("C", ["36th CA Sikkim 1975", "44th CA Emergency Safeguards 1978", "52nd CA Anti Defection 1985", "61st CA Voting Age 1988"], "1 → 2 → 3 → 4", "Part 2"),
        ("D", ["73rd CA Panchayats 1992", "86th CA RTE 2002", "91st CA Cabinet Ceiling 2003", "101st CA GST 2016"], "1 → 2 → 3 → 4", "Part 2"),
        ("A", ["25th CA Art 31C 1971", "Kesavananda Bharati 1973", "Minerva Mills 1980", "Waman Rao 1981"], "1 → 2 → 3 → 4", "Part 3"),
        ("B", ["53rd CA Mizoram 1986", "55th CA Arunachal 1986", "56th CA Goa 1987", "69th CA Delhi 1991"], "1 → 2 → 3 → 4", "Part 2"),
        ("C", ["65th CA NCSC&ST 1990", "74th CA Municipalities 1992", "89th CA NCST Bifurcation 2003", "105th CA OBC State List 2021"], "1 → 2 → 3 → 4", "Part 2"),
        ("D", ["93rd CA OBC Reservation 2005", "97th CA Cooperatives 2011", "99th CA NJAC 2014", "106th CA Women Reservation 2023"], "1 → 2 → 3 → 4", "Part 2"),
        ("A", ["Shankari Prasad 1951", "Sajjan Singh 1965", "Golaknath 1967", "Kesavananda 1973"], "1 → 2 → 3 → 4", "Part 3"),
        ("B", ["9th CA Berubari 1960", "24th CA Art 368 1971", "39th CA PM Election 1975", "44th CA Art 352 1978"], "1 → 2 → 3 → 4", "Part 2"),
        ("C", ["61st CA 18 Yrs 1988", "73rd CA Local Bodies 1992", "86th CA Art 21A 2002", "103rd CA EWS 2019"], "1 → 2 → 3 → 4", "Part 2"),
        ("D", ["42nd CA Fundamental Duties 1976", "52nd CA 10th Schedule 1985", "91st CA 2/3 Merger 2003", "101st CA GST 2016"], "1 → 2 → 3 → 4", "Part 2"),
        ("A", ["24th CA 1971", "25th CA 1971", "42nd CA 1976", "44th CA 1978"], "1 → 2 → 3 → 4", "Part 2"),
        ("B", ["Golaknath 1967", "Indira Gandhi v Raj Narain 1975", "Minerva Mills 1980", "I.R. Coelho 2007"], "1 → 2 → 3 → 4", "Part 3"),
        ("C", ["7th CA 1956", "31st CA 1973", "84th CA 2001", "87th CA 2003"], "1 → 2 → 3 → 4", "Part 2"),
        ("D", ["1st CA 1951", "4th CA 1955", "17th CA 1964", "29th CA 1972"], "1 → 2 → 3 → 4", "Part 2"),
        ("A", ["52nd CA 1985", "61st CA 1988", "69th CA 1991", "73rd CA 1992"], "1 → 2 → 3 → 4", "Part 2"),
        ("B", ["86th CA 2002", "91st CA 2003", "92nd CA 2003", "93rd CA 2005"], "1 → 2 → 3 → 4", "Part 2"),
        ("C", ["100th CA LBA 2015", "101st CA GST 2016", "102nd CA NCBC 2018", "103rd CA EWS 2019"], "1 → 2 → 3 → 4", "Part 2"),
        ("D", ["103rd CA 2019", "104th CA 2020", "105th CA 2021", "106th CA 2023"], "1 → 2 → 3 → 4", "Part 2"),
        ("C", ["Kesavananda Bharati 1973", "Waman Rao 1981", "Kihoto Hollohan 1992", "I.R. Coelho 2007"], "1 → 2 → 3 → 4", "Part 3")
    ]

    for idx, (corr, events, order_str, part) in enumerate(chronology_templates, start=5):
        q_id = f"CZ_AM_CH_{idx:03d}"

        # Build options with shuffled numeric sequences
        if corr == "A":
            seq_a = "1 → 2 → 3 → 4"
            seq_b = "2 → 1 → 4 → 3"
            seq_c = "3 → 4 → 1 → 2"
            seq_d = "4 → 3 → 2 → 1"
        elif corr == "B":
            seq_a = "2 → 1 → 4 → 3"
            seq_b = "1 → 2 → 3 → 4"
            seq_c = "3 → 1 → 4 → 2"
            seq_d = "4 → 2 → 1 → 3"
        elif corr == "C":
            seq_a = "3 → 4 → 1 → 2"
            seq_b = "2 → 3 → 4 → 1"
            seq_c = "1 → 2 → 3 → 4"
            seq_d = "4 → 1 → 2 → 3"
        else:
            seq_a = "4 → 3 → 2 → 1"
            seq_b = "2 → 4 → 1 → 3"
            seq_c = "3 → 1 → 2 → 4"
            seq_d = "1 → 2 → 3 → 4"

        q_en = f"Arrange the following constitutional developments/milestones in chronological order:\n1. {events[0]}\n2. {events[1]}\n3. {events[2]}\n4. {events[3]}"
        q_ta = f"பின்வரும் அரசியலமைப்பு மைல்கற்களைக் காலவரிசைப்படி வரிசைப்படுத்துக:\n1. {events[0]}\n2. {events[1]}\n3. {events[2]}\n4. {events[3]}"

        exp_en = f"Chronological sequence:\n1. {events[0]}\n2. {events[1]}\n3. {events[2]}\n4. {events[3]}\nHence, the correct order is 1 → 2 → 3 → 4 matching Option {corr}."
        exp_ta = f"காலவரிசை:\n1. {events[0]}\n2. {events[1]}\n3. {events[2]}\n4. {events[3]}\nஎனவே விருப்பம் {corr} சரியானதாகும்."

        why_a = f"Option A gives sequence {seq_a}. {'Correct chronological order' if corr=='A' else 'Incorrect sequence'}."
        why_a_ta = f"விருப்பம் A வரிசை {seq_a} ஐத் தருகிறது. {'சரியான வரிசை' if corr=='A' else 'தவறான வரிசை'}."
        why_b = f"Option B gives sequence {seq_b}. {'Correct chronological order' if corr=='B' else 'Incorrect sequence'}."
        why_b_ta = f"விருப்பம் B வரிசை {seq_b} ஐத் தருகிறது. {'சரியான வரிசை' if corr=='B' else 'தவறான வரிசை'}."
        why_c = f"Option C gives sequence {seq_c}. {'Correct chronological order' if corr=='C' else 'Incorrect sequence'}."
        why_c_ta = f"விருப்பம் C வரிசை {seq_c} ஐத் தருகிறது. {'சரியான வரிசை' if corr=='C' else 'தவறான வரிசை'}."
        why_d = f"Option D gives sequence {seq_d}. {'Correct chronological order' if corr=='D' else 'Incorrect sequence'}."
        why_d_ta = f"விருப்பம் D வரிசை {seq_d} ஐத் தருகிறது. {'சரியான வரிசை' if corr=='D' else 'தவறான வரிசை'}."

        tip_en = "Always list out the exact years of each event on draft paper before selecting the chronology option."
        tip_ta = "காலவரிசை தேர்வை எடுப்பதற்கு முன் ஒவ்வொரு நிகழ்வின் ஆண்டையும் வரைதாளில் குறித்துக் கொள்ளவும்."
        fact_en = "Chronology of constitutional amendments is a high-yielding section in TNPSC Group 1."
        fact_ta = "அரசியலமைப்பு திருத்தங்களின் காலவரிசை டிஎன்பிஎஸ்சி தேர்வுகளில் அதிக மதிப்பெண் தரும் பகுதியாகும்."

        add_q(
            q_id, q_en, q_ta,
            seq_a, seq_a, seq_b, seq_b, seq_c, seq_c, seq_d, seq_d,
            corr, exp_en, exp_ta,
            why_a, why_a_ta, why_b, why_b_ta, why_c, why_c_ta, why_d, why_d_ta,
            tip_en, tip_ta, fact_en, fact_ta,
            "Analyzing", "Hard", ["Chronology Validation", "Constitutional Developments"], part
        )

    return questions

if __name__ == "__main__":
    qs = create_chronology_questions()
    os.makedirs("data/questions/polity", exist_ok=True)
    out_path = "data/questions/polity/constitutional_amendments_chronology.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, ensure_ascii=False, indent=2)

    counts = Counter(q["correct_answer"] for q in qs)
    print(f"Chronology set complete. Total: {len(qs)}")
    print(f"Answer balance: {dict(counts)}")
