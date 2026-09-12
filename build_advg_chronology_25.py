# -*- coding: utf-8 -*-
"""
Builder for Advocate General of a State - Chronology Level (25 MCQs: ADVG_C_001 to ADVG_C_025).
Strictly complies with ChronologyValidator and ContentValidator.
All 6 Gates satisfied:
1. 4 events per stem.
2. Presentation order != Chronological order (never 1, 2, 3, 4).
3. Sequence arrows ('->') and 4-digit years in explanations.
4. Balanced keys: 7 A, 6 B, 6 C, 6 D.
5. 4 unique valid permutations.
"""
import json
import os
from advg_mcq_helper import make_advg_q
from tools.nova_content_engine.validator import ContentValidator
from tools.nova_content_engine.chronology_validator import ChronologyValidator

def get_chronology_questions():
    qs = []

    def add_chrono(qid, subtopic, title_en, title_ta,
                   e1_en, e1_ta, y1,
                   e2_en, e2_ta, y2,
                   e3_en, e3_ta, y3,
                   e4_en, e4_ta, y4,
                   correct_key,
                   opt_a, opt_b, opt_c, opt_d,
                   exp_en, exp_ta,
                   tip_en, tip_ta, fact_en, fact_ta):
        
        en_stem = f"Arrange the following {title_en} in correct chronological order:\n1. {e1_en}\n2. {e2_en}\n3. {e3_en}\n4. {e4_en}\nSelect the correct answer using the codes given below:"
        ta_stem = f"பின்வரும் {title_ta} சரியான காலவரிசையில் ஒழுங்குபடுத்துக:\n1. {e1_ta}\n2. {e2_ta}\n3. {e3_ta}\n4. {e4_ta}\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:"

        why_a_en = f"Option A indicates order: {opt_a}."
        why_a_ta = f"விருப்பம் A குறிக்கும் வரிசை: {opt_a}."
        why_b_en = f"Option B indicates order: {opt_b}."
        why_b_ta = f"விருப்பம் B குறிக்கும் வரிசை: {opt_b}."
        why_c_en = f"Option C indicates order: {opt_c}."
        why_c_ta = f"விருப்பம் C குறிக்கும் வரிசை: {opt_c}."
        why_d_en = f"Option D indicates order: {opt_d}."
        why_d_ta = f"விருப்பம் D குறிக்கும் வரிசை: {opt_d}."

        qs.append(make_advg_q(
            qid=qid, diff="Hard", qtype="Chronology", subtopic=subtopic,
            en_stem=en_stem, ta_stem=ta_stem,
            en_a=opt_a, ta_a=opt_a, en_b=opt_b, ta_b=opt_b,
            en_c=opt_c, ta_c=opt_c, en_d=opt_d, ta_d=opt_d,
            correct_key=correct_key, exp_en=exp_en, exp_ta=exp_ta,
            why_a_en=why_a_en, why_a_ta=why_a_ta, why_b_en=why_b_en, why_b_ta=why_b_ta,
            why_c_en=why_c_en, why_c_ta=why_c_ta, why_d_en=why_d_en, why_d_ta=why_d_ta,
            tip_en=tip_en, tip_ta=tip_ta, fact_en=fact_en, fact_ta=fact_ta
        ))

    # --- 7 Questions with Key 'A' ---
    # Q1 (A) Correct seq: 2 - 4 - 1 - 3 (1861 -> 1935 -> 1950 -> 1961)
    # 1: Constitution 1950, 2: High Courts Act 1861, 3: Advocates Act 1961, 4: GoI Act 1935
    add_chrono(
        "ADVG_C_001", "Constitutional Evolution",
        "statutory enactments relating to the evolution of law officers and High Courts in India",
        "இந்தியாவில் சட்ட அதிகாரிகள் மற்றும் உயர் நீதிமன்றங்களின் பரிணாமம் தொடர்பான சட்டங்கள்",
        "Enactment of the Constitution of India (Article 165)", "இந்திய அரசியலமைப்பு சட்டம் இயற்றப்படுதல் (உறுப்பு 165)", 1950,
        "Passage of the Indian High Courts Act", "இந்திய உயர் நீதிமன்றங்கள் சட்டம் நிறைவேற்றப்படுதல்", 1861,
        "Enactment of the Advocates Act (Section 23 pre-audience)", "வழக்கறிஞர்கள் சட்டம் இயற்றப்படுதல் (பிரிவு 23 முன்னுரிமை)", 1961,
        "Government of India Act providing for Provincial Advocate-General (Section 55)", "மாகாண தலைமை வழக்கறிஞரை வழங்கிய இந்திய அரசுச் சட்டம் (பிரிவு 55)", 1935,
        "A",
        "2 - 4 - 1 - 3", "4 - 2 - 1 - 3", "2 - 1 - 4 - 3", "1 - 4 - 2 - 3",
        "The correct chronological sequence is: Indian High Courts Act (1861) -> Government of India Act (1935) -> Constitution of India (1950) -> Advocates Act (1961). Correct order: 2 -> 4 -> 1 -> 3.",
        "சரியான காலவரிசை: இந்திய உயர் நீதிமன்றங்கள் சட்டம் (1861) -> இந்திய அரசுச் சட்டம் (1935) -> இந்திய அரசியலமைப்பு சட்டம் (1950) -> வழக்கறிஞர்கள் சட்டம் (1961). சரியான வரிசை: 2 -> 4 -> 1 -> 3.",
        "Remember key years: High Courts Act (1861), GoI Act (1935), Constitution (1950), Advocates Act (1961).",
        "முக்கிய ஆண்டுகளை நினைவில் கொள்க: உயர் நீதிமன்றங்கள் சட்டம் (1861), 1935 சட்டம், அரசியலமைப்பு (1950), வழக்கறிஞர்கள் சட்டம் (1961).",
        "Section 55 of GoI Act 1935 was the direct predecessor of Article 165.",
        "1935-ஆம் ஆண்டு இந்திய அரசுச் சட்டத்தின் பிரிவு 55 உறுப்பு 165-ன் நேரடி முன்னோடியாகும்."
    )

    # Q2 (A) Correct seq: 3 - 1 - 4 - 2 (1952 -> 1962 -> 1994 -> 2004)
    # 1: Atlas Cycle 1962, 2: M.T. Khan 2004, 3: G.D. Karkare 1952, 4: UP Law Officers 1994
    add_chrono(
        "ADVG_C_002", "Landmark Judgments",
        "landmark judicial decisions concerning the Advocate General and government law officers",
        "தலைமை வழக்கறிஞர் மற்றும் அரசு சட்ட அதிகாரிகள் தொடர்பான முக்கிய நீதிமன்றத் தீர்ப்புகள்",
        "Atlas Cycle Industries v. Their Workmen (SC affirmation of AG age criteria)", "அட்லஸ் சைக்கிள் இண்டஸ்ட்ரீஸ் வழக்கு (AG வயது வரம்பு குறித்த உச்ச நீதிமன்ற உறுதிப்படுத்தல்)", 1962,
        "M.T. Khan v. Government of Andhra Pradesh (Singular Advocate General office)", "எம்.டி. கான் எதிர் ஆந்திரப் பிரதேச அரசு (ஒற்றை தலைமை வழக்கறிஞர் பதவி)", 2004,
        "G.D. Karkare v. T.L. Shevde (Nagpur HC ruling on retirement age)", "ஜி.டி. கார்கரே எதிர் டி.எல். ஷேவ்டே (ஓய்வு வயது குறித்த நாக்பூர் உயர் நீதிமன்றத் தீர்ப்பு)", 1952,
        "State of U.P. v. U.P. State Law Officers Association (Fiduciary public office)", "உத்தரப் பிரதேச அரசு எதிர் உ.பி. மாநில சட்ட அதிகாரிகள் சங்கம் (பொது அலுவலகம்)", 1994,
        "A",
        "3 - 1 - 4 - 2", "1 - 3 - 4 - 2", "3 - 4 - 1 - 2", "4 - 3 - 1 - 2",
        "The correct chronological sequence is: G.D. Karkare v. T.L. Shevde (1952) -> Atlas Cycle Industries (1962) -> State of U.P. v. U.P. State Law Officers Association (1994) -> M.T. Khan v. Govt of A.P. (2004). Correct order: 3 -> 1 -> 4 -> 2.",
        "சரியான காலவரிசை: ஜி.டி. கார்கரே வழக்கு (1952) -> அட்லஸ் சைக்கிள் இண்டஸ்ட்ரீஸ் (1962) -> உ.பி. மாநில சட்ட அதிகாரிகள் சங்கம் வழக்கு (1994) -> எம்.டி. கான் வழக்கு (2004). சரியான வரிசை: 3 -> 1 -> 4 -> 2.",
        "Chronological chain: Karkare (1952) -> Atlas (1962) -> UP Law Officers (1994) -> M.T. Khan (2004).",
        "காலவரிசை சங்கிலி: கார்கரே (1952) -> அட்லஸ் (1962) -> உ.பி. சட்ட அதிகாரிகள் (1994) -> எம்.டி. கான் (2004).",
        "M.T. Khan (2004) settled that Additional AG is an executive post, not Article 165.",
        "கூடுதல் AG என்பது நிர்வாகப் பதவி, உறுப்பு 165 அல்ல என்பதை எம்.டி. கான் (2004) உறுதி செய்தது."
    )

    # Q3 (A) Correct seq: 2 - 1 - 4 - 3 (1908 -> 1950 -> 1961 -> 1971)
    # 1: Constitution 1950, 2: CPC 1908, 3: Contempt Act 1971, 4: Advocates Act 1961
    add_chrono(
        "ADVG_C_003", "Statutory Framework",
        "key legal enactments defining the statutory powers and privileges of the Advocate General",
        "தலைமை வழக்கறிஞரின் சட்டப்பூர்வ அதிகாரங்கள் மற்றும் சிறப்புரிமைகளை வரையறுக்கும் சட்டங்கள்",
        "Adoption of the Constitution of India (Articles 165, 177, 194)", "இந்திய அரசியலமைப்பு ஏற்றுக்கொள்ளப்படுதல் (உறுப்புகள் 165, 177, 194)", 1950,
        "Code of Civil Procedure enacted (Sections 91 and 92 public suits)", "சிவில் நடைமுறைச் சட்டம் இயற்றப்படுதல் (பிரிவுகள் 91 மற்றும் 92 பொது வழக்குகள்)", 1908,
        "Contempt of Courts Act enacted (Section 15 consent power)", "நீதிமன்ற அவமதிப்புச் சட்டம் இயற்றப்படுதல் (பிரிவு 15 இசைவு அதிகாரம்)", 1971,
        "Advocates Act enacted (Section 3 Bar Council, Section 23 Pre-audience)", "வழக்கறிஞர்கள் சட்டம் இயற்றப்படுதல் (பிரிவு 3 பார் கவுன்சில், பிரிவு 23 முன்னுரிமை)", 1961,
        "A",
        "2 - 1 - 4 - 3", "1 - 2 - 4 - 3", "2 - 4 - 1 - 3", "4 - 2 - 1 - 3",
        "The correct chronological sequence is: Code of Civil Procedure (1908) -> Constitution of India (1950) -> Advocates Act (1961) -> Contempt of Courts Act (1971). Correct order: 2 -> 1 -> 4 -> 3.",
        "சரியான காலவரிசை: சிவில் நடைமுறைச் சட்டம் (1908) -> இந்திய அரசியலமைப்பு (1950) -> வழக்கறிஞர்கள் சட்டம் (1961) -> நீதிமன்ற அவமதிப்புச் சட்டம் (1971). சரியான வரிசை: 2 -> 1 -> 4 -> 3.",
        "Four statutory pillars: CPC (1908) -> Constitution (1950) -> Advocates Act (1961) -> Contempt Act (1971).",
        "நான்கு சட்டத் தூண்கள்: CPC (1908) -> அரசியலமைப்பு (1950) -> வழக்கறிஞர்கள் சட்டம் (1961) -> அவமதிப்புச் சட்டம் (1971).",
        "These four statutes constitute the complete statutory toolkit of the Advocate General.",
        "இந்த நான்கு சட்டங்களும் தலைமை வழக்கறிஞரின் முழுமையான சட்டப்பூர்வ அதிகாரங்களை உருவாக்குகின்றன."
    )

    # Q4 (A) Correct seq: 4 - 1 - 3 - 2 (1971 -> 1988 -> 2005 -> 2014)
    # 1: P.N. Duda 1988, 2: Swamy v. Shourie 2014, 3: Bal Thackrey 2005, 4: Daphtary 1971
    add_chrono(
        "ADVG_C_004", "Contempt Jurisprudence",
        "landmark decisions shaping the law on criminal contempt and law officer consent",
        "குற்றவியல் அவமதிப்பு மற்றும் சட்ட அதிகாரி இசைவு தொடர்பான முக்கிய நீதிமன்றத் தீர்ப்புகள்",
        "P.N. Duda v. P. Shiv Shanker (Quasi-judicial role under Section 15)", "பி.என். துதா எதிர் பி. சிவ் சங்கர் (பிரிவு 15-ன் கீழான நீதித்துறை போன்ற பணி)", 1988,
        "Subramanian Swamy v. Arun Shourie (Truth as defense in contempt)", "சுப்பிரமணியன் சுவாமி எதிர் அருண் ஷோரி (அவமதிப்பில் உண்மை ஒரு பாதுகாப்பாகுதல்)", 2014,
        "Bal Thackrey v. Harish Pimpale (Mandatory nature of Section 15 consent)", "பால் தாக்கரே எதிர் ஹரிஷ் பிம்பாலே (பிரிவு 15 இசைவின் கட்டாயத் தன்மை)", 2005,
        "C.K. Daphtary v. O.P. Gupta (Contempt law officers standing affirmed)", "சி.கே. தப்தாரி எதிர் ஓ.பி. குப்தா (அவமதிப்பு சட்ட அதிகாரிகள் தகுதி உறுதி)", 1971,
        "A",
        "4 - 1 - 3 - 2", "1 - 4 - 3 - 2", "4 - 3 - 1 - 2", "3 - 4 - 1 - 2",
        "The correct chronological sequence is: C.K. Daphtary v. O.P. Gupta (1971) -> P.N. Duda v. P. Shiv Shanker (1988) -> Bal Thackrey v. Harish Pimpale (2005) -> Subramanian Swamy v. Arun Shourie (2014). Correct order: 4 -> 1 -> 3 -> 2.",
        "சரியான காலவரிசை: சி.கே. தப்தாரி வழக்கு (1971) -> பி.என். துதா வழக்கு (1988) -> பால் தாக்கரே வழக்கு (2005) -> சுப்பிரமணியன் சுவாமி வழக்கு (2014). சரியான வரிசை: 4 -> 1 -> 3 -> 2.",
        "Sequence of Contempt Cases: Daphtary (1971) -> Duda (1988) -> Thackrey (2005) -> Swamy (2014).",
        "அவமதிப்பு வழக்குகள் வரிசை: தப்தாரி (1971) -> துதா (1988) -> தாக்கரே (2005) -> சுவாமி (2014).",
        "In 2006, Section 13 of the Contempt Act was amended to recognize truth as a valid defense.",
        "2006-ல் அவமதிப்புச் சட்டத்தின் பிரிவு 13 உண்மையை ஒரு செல்லுபடியாகும் பாதுகாப்பாக அங்கீகரிக்க திருத்தப்பட்டது."
    )

    # Q5 (A) Correct seq: 2 - 3 - 1 - 4 (1945 -> 1951 -> 1966 -> 1976)
    # 1: Mohan Kumaramangalam 1966, 2: K. Rajah Iyer 1945, 3: V.K. Thiruvenkatachari 1951, 4: K. Parasaran 1976
    add_chrono(
        "ADVG_C_005", "Madras Advocate Generals Group 1",
        "tenures of distinguished Advocate Generals of Madras / Tamil Nadu",
        "சென்னை / தமிழ்நாட்டின் புகழ்பெற்ற தலைமை வழக்கறிஞர்களின் பதவிக்காலங்கள்",
        "Appointment of Mohan Kumaramangalam as Advocate General", "மோகன் குமாரமங்கலம் தலைமை வழக்கறிஞராக நியமிக்கப்படுதல்", 1966,
        "Appointment of K. Rajah Iyer as Advocate General of Madras", "கே. ராஜா ஐயர் சென்னை தலைமை வழக்கறிஞராக நியமிக்கப்படுதல்", 1945,
        "Appointment of V.K. Thiruvenkatachari as Advocate General of Madras", "வி.கே. திருவேங்கடாச்சாரி சென்னை தலைமை வழக்கறிஞராக நியமிக்கப்படுதல்", 1951,
        "Appointment of K. Parasaran as Advocate General of Tamil Nadu", "கே. பராசரன் தமிழ்நாடு தலைமை வழக்கறிஞராக நியமிக்கப்படுதல்", 1976,
        "A",
        "2 - 3 - 1 - 4", "3 - 2 - 1 - 4", "2 - 1 - 3 - 4", "1 - 2 - 3 - 4",
        "The correct chronological sequence is: K. Rajah Iyer (1945) -> V.K. Thiruvenkatachari (1951) -> Mohan Kumaramangalam (1966) -> K. Parasaran (1976). Correct order: 2 -> 3 -> 1 -> 4.",
        "சரியான காலவரிசை: கே. ராஜா ஐயர் (1945) -> வி.கே. திருவேங்கடாச்சாரி (1951) -> மோகன் குமாரமங்கலம் (1966) -> கே. பராசரன் (1976). சரியான வரிசை: 2 -> 3 -> 1 -> 4.",
        "TN AG Succession 1: Rajah Iyer (1945) -> Thiruvenkatachari (1951) -> Kumaramangalam (1966) -> Parasaran (1976).",
        "தமிழ்நாடு AG வரிசை 1: ராஜா ஐயர் (1945) -> திருவேங்கடாச்சாரி (1951) -> குமாரமங்கலம் (1966) -> பராசரன் (1976).",
        "V.K. Thiruvenkatachari served for an illustrious 13 years (1951 to 1964).",
        "வி.கே. திருவேங்கடாச்சாரி 13 ஆண்டுகள் (1951 முதல் 1964 வரை) மிக நீண்ட காலம் பணியாற்றினார்."
    )

    # Q6 (A) Correct seq: 3 - 1 - 4 - 2 (1977 -> 1994 -> 2006 -> 2022)
    # 1: S.R. Bommai 1994, 2: Mohit Minerals 2022, 3: State of Rajasthan 1977, 4: Rameshwar Prasad 2006
    add_chrono(
        "ADVG_C_006", "Federalism Landmark Suits",
        "landmark Supreme Court judgments on federalism and state constitutional powers",
        "கூட்டாட்சி மற்றும் மாநில அரசியலமைப்பு அதிகாரங்கள் தொடர்பான முக்கிய உச்ச நீதிமன்றத் தீர்ப்புகள்",
        "S.R. Bommai v. Union of India (Floor test as sole forum; secularism basic structure)", "எஸ்.ஆர். பொம்மை எதிர் இந்திய ஒன்றியம் (நம்பிக்கை வாக்கெடுப்பு; மதச்சார்பின்மை அடிப்படைக் கட்டமைப்பு)", 1994,
        "Union of India v. Mohit Minerals (Simultaneous GST power under Article 246A)", "மோஹித் மினரல்ஸ் வழக்கு (உறுப்பு 246A-ன் கீழான சமகால ஜிஎஸ்டி அதிகாரம்)", 2022,
        "State of Rajasthan v. Union of India (Article 131 suit on Assembly dissolution)", "ராஜஸ்தான் அரசு எதிர் இந்திய ஒன்றியம் (சட்டமன்றக் கலைப்பு மீதான உறுப்பு 131 வழக்கு)", 1977,
        "Rameshwar Prasad v. Union of India (Judicial review of Governor report under Article 356)", "ராமேஷ்வர் பிரசாத் எதிர் இந்திய ஒன்றியம் (உறுப்பு 356 ஆளுநர் அறிக்கை மீதான மறுஆய்வு)", 2006,
        "A",
        "3 - 1 - 4 - 2", "1 - 3 - 4 - 2", "3 - 4 - 1 - 2", "4 - 3 - 1 - 2",
        "The correct chronological sequence is: State of Rajasthan v. Union of India (1977) -> S.R. Bommai v. Union of India (1994) -> Rameshwar Prasad v. Union of India (2006) -> Union of India v. Mohit Minerals (2022). Correct order: 3 -> 1 -> 4 -> 2.",
        "சரியான காலவரிசை: ராஜஸ்தான் அரசு வழக்கு (1977) -> எஸ்.ஆர். பொம்மை வழக்கு (1994) -> ராமேஷ்வர் பிரசாத் வழக்கு (2006) -> மோஹித் மினரல்ஸ் வழக்கு (2022). சரியான வரிசை: 3 -> 1 -> 4 -> 2.",
        "Federalism Jurisprudence: Rajasthan (1977) -> Bommai (1994) -> Rameshwar Prasad (2006) -> Mohit Minerals (2022).",
        "கூட்டாட்சித் தீர்ப்புகள்: ராஜஸ்தான் (1977) -> பொம்மை (1994) -> ராமேஷ்வர் பிரசாத் (2006) -> மோஹித் மினரல்ஸ் (2022).",
        "These cases define the federal boundaries within which State Advocate Generals operate.",
        "இவ்வழக்குகள் மாநில தலைமை வழக்கறிஞர்கள் செயல்படும் கூட்டாட்சி வரம்புகளை வரையறுக்கின்றன."
    )

    # Q7 (A) Correct seq: 4 - 2 - 1 - 3 (1965 -> 1983 -> 1993 -> 1997)
    # 1: Nilabati Behera 1993, 2: Rudul Sah 1983, 3: D.K. Basu 1997, 4: Kasturi Lal 1965
    add_chrono(
        "ADVG_C_007", "Public Law Tort Evolution",
        "milestones in the evolution of state liability and human rights compensation in India",
        "இந்தியாவில் அரசு பொறுப்பு மற்றும் மனித உரிமைகள் இழப்பீட்டு பரிணாம வளர்ச்சியின் மைல்கற்கள்",
        "Nilabati Behera v. State of Orissa (Strict public law liability under Article 21)", "நீலபதி பெஹரா எதிர் ஒரிசா அரசு (உறுப்பு 21-ன் கீழான கடுமையான பொதுச் சட்டப் பொறுப்பு)", 1993,
        "Rudul Sah v. State of Bihar (First monetary compensation awarded under Article 32)", "ருதுல் சா எதிர் பீகார் அரசு (உறுப்பு 32-ன் கீழ் முதல் பண இழப்பீடு வழங்கப்படுதல்)", 1983,
        "D.K. Basu v. State of West Bengal (Mandatory arrest and custody guidelines)", "டி.கே. பாசு எதிர் மேற்கு வங்க அரசு (கட்டாய கைது மற்றும் காவல் வழிகாட்டுதல்கள்)", 1997,
        "Kasturi Lal v. State of U.P. (Sovereign immunity defense in gold seizure negligence)", "கஸ்தூரி லால் எதிர் உ.பி. அரசு (தங்கப் பறிமுதல் வழக்கில் இறையாண்மை விலக்களிப்பு)", 1965,
        "A",
        "4 - 2 - 1 - 3", "2 - 4 - 1 - 3", "4 - 1 - 2 - 3", "1 - 4 - 2 - 3",
        "The correct chronological sequence is: Kasturi Lal (1965) -> Rudul Sah (1983) -> Nilabati Behera (1993) -> D.K. Basu (1997). Correct order: 4 -> 2 -> 1 -> 3.",
        "சரியான காலவரிசை: கஸ்தூரி லால் (1965) -> ருதுல் சா (1983) -> நீலபதி பெஹரா (1993) -> டி.கே. பாசு (1997). சரியான வரிசை: 4 -> 2 -> 1 -> 3.",
        "State Liability progression: Kasturi Lal (1965) -> Rudul Sah (1983) -> Nilabati Behera (1993) -> D.K. Basu (1997).",
        "அரசு பொறுப்பு முன்னேற்றம்: கஸ்தூரி லால் (1965) -> ருதுல் சா (1983) -> நீலபதி பெஹரா (1993) -> டி.கே. பாசு (1997).",
        "Nilabati Behera dismantled the sovereign immunity defense for Article 21 violations.",
        "நீலபதி பெஹரா வழக்கு உறுப்பு 21 மீறல்களுக்கான இறையாண்மை விலக்களிப்பு வாதத்தை தகர்த்தெறிந்தது."
    )

    # --- 6 Questions with Key 'B' ---
    # Q8 (B) Correct seq: 2 - 4 - 1 - 3 (1981 -> 1982 -> 1987 -> 2017)
    # 1: D.C. Wadhwa 1987, 2: R.K. Garg 1981, 3: Krishna Kumar Singh 2017, 4: A.K. Roy 1982
    add_chrono(
        "ADVG_C_008", "Article 213 Ordinance Cases",
        "landmark constitutional decisions on the scope and limits of the ordinance-making power",
        "அவசரச் சட்டம் பிறப்பிக்கும் அதிகாரத்தின் வரம்புகள் குறித்த முக்கிய அரசியலமைப்புத் தீர்ப்புகள்",
        "D.C. Wadhwa v. State of Bihar (Re-promulgation of ordinances held fraud on Constitution)", "டி.சி. வாத்வா எதிர் பீகார் அரசு (அவசரச் சட்ட மறுபிறப்பீடு அரசியலமைப்பு மோசடி)", 1987,
        "R.K. Garg v. Union of India (Special Bearer Bonds ordinance upheld)", "ஆர்.கே. கார்க் எதிர் இந்திய ஒன்றியம் (சிறப்பு பத்திரம் அவசரச் சட்டம் உறுதி)", 1981,
        "Krishna Kumar Singh v. State of Bihar (7-judge bench affirms mandatory legislative tabling)", "கிருஷ்ண குமார் சிங் வழக்கு (7 நீதிபதிகள் அமர்வு கட்டாய சட்டமன்ற சமர்ப்பிப்பை உறுதி செய்தல்)", 2017,
        "A.K. Roy v. Union of India (National Security Ordinance judicial review affirmed)", "ஏ.கே. ராய் எதிர் இந்திய ஒன்றியம் (தேசிய பாதுகாப்பு அவசரச் சட்ட நீதித்துறை மறுஆய்வு)", 1982,
        "B",
        "1 - 2 - 4 - 3", "2 - 4 - 1 - 3", "2 - 1 - 4 - 3", "4 - 2 - 1 - 3",
        "The correct chronological sequence is: R.K. Garg (1981) -> A.K. Roy (1982) -> D.C. Wadhwa (1987) -> Krishna Kumar Singh (2017). Correct order: 2 -> 4 -> 1 -> 3.",
        "சரியான காலவரிசை: ஆர்.கே. கார்க் (1981) -> ஏ.கே. ராய் (1982) -> டி.சி. வாத்வா (1987) -> கிருஷ்ண குமார் சிங் (2017). சரியான வரிசை: 2 -> 4 -> 1 -> 3.",
        "Ordinance Jurisprudence: Garg (1981) -> Roy (1982) -> Wadhwa (1987) -> Krishna Kumar (2017).",
        "அவசரச் சட்டத் தீர்ப்புகள்: கார்க் (1981) -> ராய் (1982) -> வாத்வா (1987) -> கிருஷ்ண குமார் (2017).",
        "D.C. Wadhwa and Krishna Kumar Singh are paramount authorities for Advocate Generals vetting ordinances.",
        "அவசரச் சட்டங்களை ஆய்வு செய்யும் தலைமை வழக்கறிஞர்களுக்கு வாத்வா மற்றும் கிருஷ்ண குமார் சிங் மிக முக்கியமான வழிகாட்டிகளாகும்."
    )

    # Q9 (B) Correct seq: 3 - 1 - 4 - 2 (1935 -> 1950 -> 1956 -> 2007)
    # 1: Constitution Art 262 1950, 2: Cauvery Award 2007, 3: GoI Act Sec 130 1935, 4: Inter-State Water Act 1956
    add_chrono(
        "ADVG_C_009", "Inter-State River Water Legal History",
        "milestones in the constitutional and statutory framework of inter-state river water dispute resolution",
        "மாநிலங்களுக்கு இடையேயான நதிநீர் தாவா தீர்வுக்கான அரசியலமைப்பு மற்றும் சட்டப்பூர்வ கட்டமைப்பின் மைல்கற்கள்",
        "Adoption of Article 262 in the Constitution of India", "இந்திய அரசியலமைப்பில் உறுப்பு 262 ஏற்றுக்கொள்ளப்படுதல்", 1950,
        "Final Award of the Cauvery Water Disputes Tribunal delivered", "காவிரி நதிநீர் தாவா தீர்ப்பாயத்தின் இறுதித் தீர்ப்பு வழங்கப்படுதல்", 2007,
        "Government of India Act enacting Sections 130 to 134 on provincial water rights", "மாகாண நீர் உரிமைகள் குறித்து இந்திய அரசுச் சட்டம் பிரிவுகள் 130 முதல் 134 வரை இயற்றுதல்", 1935,
        "Enactment of the Inter-State River Water Disputes Act by Parliament", "நாடாளுமன்றத்தால் மாநிலங்களுக்கு இடையேயான நதிநீர் தாவாக்கள் சட்டம் இயற்றப்படுதல்", 1956,
        "B",
        "3 - 4 - 1 - 2", "3 - 1 - 4 - 2", "1 - 3 - 4 - 2", "4 - 3 - 1 - 2",
        "The correct chronological sequence is: Government of India Act (1935) -> Constitution of India Article 262 (1950) -> Inter-State River Water Disputes Act (1956) -> Cauvery Tribunal Final Award (2007). Correct order: 3 -> 1 -> 4 -> 2.",
        "சரியான காலவரிசை: இந்திய அரசுச் சட்டம் (1935) -> இந்திய அரசியலமைப்பு உறுப்பு 262 (1950) -> நதிநீர் தாவாக்கள் சட்டம் (1956) -> காவிரி தீர்ப்பாய இறுதித் தீர்ப்பு (2007). சரியான வரிசை: 3 -> 1 -> 4 -> 2.",
        "River Water Milestones: GoI Act (1935) -> Art 262 (1950) -> ISRWD Act (1956) -> Cauvery Award (2007).",
        "நதிநீர் மைல்கற்கள்: 1935 சட்டம் -> உறுப்பு 262 (1950) -> 1956 சட்டம் -> காவிரி தீர்ப்பு (2007).",
        "The Cauvery Tribunal award was subsequently modified by the Supreme Court in 2018.",
        "காவிரி தீர்ப்பாயத் தீர்ப்பு பின்னர் 2018-ல் உச்ச நீதிமன்றத்தால் மாற்றியமைக்கப்பட்டது."
    )

    # Q10 (B) Correct seq: 4 - 1 - 2 - 3 (1898 -> 1969 -> 1973 -> 2023)
    # 1: Law Commission 41st Report 1969, 2: CrPC 1973, 3: BNSS 2023, 4: Code of Criminal Procedure 1898
    add_chrono(
        "ADVG_C_010", "Criminal Procedure Framework Evolution",
        "legislative landmarks in the evolution of criminal procedure and prosecution administration in India",
        "இந்தியாவில் குற்றவியல் நடைமுறை மற்றும் அரசுத் தரப்பு நிர்வாக பரிணாம வளர்ச்சியின் மைல்கற்கள்",
        "Law Commission of India 41st Report recommending separate Directorate of Prosecution", "தனி அரசுத் தரப்பு இயக்ககத்தை பரிந்துரைத்த இந்திய சட்ட ஆணையத்தின் 41-வது அறிக்கை", 1969,
        "Enactment of the Code of Criminal Procedure, 1973 (Act No. 2 of 1974)", "குற்றவியல் நடைமுறைச் சட்டம் 1973 இயற்றப்படுதல்", 1973,
        "Enactment of the Bharatiya Nagarik Suraksha Sanhita (BNSS) replacing the 1973 Code", "1973 சட்டத்திற்குப் பதிலாக பாரதிய நகரிக் சுரக்ஷா சன்ஹிதா (BNSS) இயற்றப்படுதல்", 2023,
        "Enactment of the Code of Criminal Procedure under British rule (Act V of 1898)", "பிரிட்டிஷ் ஆட்சியில் குற்றவியல் நடைமுறைச் சட்டம் இயற்றப்படுதல் (1898 சட்டம்)", 1898,
        "B",
        "1 - 4 - 2 - 3", "4 - 1 - 2 - 3", "4 - 2 - 1 - 3", "2 - 4 - 1 - 3",
        "The correct chronological sequence is: CrPC (1898) -> Law Commission 41st Report (1969) -> CrPC (1973) -> Bharatiya Nagarik Suraksha Sanhita (2023). Correct order: 4 -> 1 -> 2 -> 3.",
        "சரியான காலவரிசை: CrPC (1898) -> சட்ட ஆணைய 41-வது அறிக்கை (1969) -> CrPC (1973) -> பாரதிய நகரிக் சுரக்ஷா சன்ஹிதா (2023). சரியான வரிசை: 4 -> 1 -> 2 -> 3.",
        "Criminal Code Milestones: CrPC 1898 -> Law Commission 1969 -> CrPC 1973 -> BNSS 2023.",
        "குற்றவியல் சட்ட மைல்கற்கள்: CrPC 1898 -> சட்ட ஆணையம் 1969 -> CrPC 1973 -> BNSS 2023.",
        "BNSS 2023 modernizes criminal procedure while preserving the core institutional role of the Public Prosecutor.",
        "BNSS 2023 குற்றவியல் நடைமுறையை நவீனமயமாக்கும் அதே வேளையில் அரசு வழக்கறிஞரின் முக்கியப் பங்கைத் தக்க வைத்துக் கொண்டுள்ளது."
    )

    # Q11 (B) Correct seq: 2 - 4 - 1 - 3 (1957 -> 1980 -> 1987 -> 2000)
    # 1: Sheonandan Paswan 1987, 2: Ram Naresh Pandey 1957, 3: Abdul Karim (Veerappan) 2000, 4: Subhash Chander 1980
    add_chrono(
        "ADVG_C_011", "Section 321 Withdrawal Precedents",
        "authoritative Supreme Court decisions on withdrawal from prosecution under Section 321 CrPC",
        "CrPC பிரிவு 321-ன் கீழ் வழக்குகளை திரும்பப் பெறுவது தொடர்பான முக்கிய உச்ச நீதிமன்றத் தீர்ப்புகள்",
        "Sheonandan Paswan v. State of Bihar (Constitution Bench on Prosecutor's independent mind)", "ஷிவநந்தன் பாஸ்வான் எதிர் பீகார் அரசு (சுதந்திர சிந்தனை குறித்த அரசியலமைப்பு அமர்வு தீர்ப்பு)", 1987,
        "State of Bihar v. Ram Naresh Pandey (First major SC ruling on withdrawal from prosecution)", "பீகார் அரசு எதிர் ராம் நரேஷ் பாண்டே (வழக்கு திரும்பப் பெறுதல் மீதான முதல் முக்கிய தீர்ப்பு)", 1957,
        "Abdul Karim v. State of Karnataka (Veerappan hostage case quashing withdrawal)", "அப்துல் கரீம் எதிர் கர்நாடக அரசு (வீரப்பன் பிணைக்கைதி வழக்கில் திரும்பப் பெறுதல் ரத்து)", 2000,
        "Subhash Chander v. State (Chandigarh Administration) (Reiterating judicial discretion)", "சுபாஷ் சந்தர் எதிர் சண்டிகர் நிர்வாகம் (நீதித்துறை விருப்புரிமையை மீண்டும் உறுதி செய்தல்)", 1980,
        "B",
        "2 - 1 - 4 - 3", "2 - 4 - 1 - 3", "4 - 2 - 1 - 3", "1 - 2 - 4 - 3",
        "The correct chronological sequence is: Ram Naresh Pandey (1957) -> Subhash Chander (1980) -> Sheonandan Paswan (1987) -> Abdul Karim (2000). Correct order: 2 -> 4 -> 1 -> 3.",
        "சரியான காலவரிசை: ராம் நரேஷ் பாண்டே (1957) -> சுபாஷ் சந்தர் (1980) -> ஷிவநந்தன் பாஸ்வான் (1987) -> அப்துல் கரீம் (2000). சரியான வரிசை: 2 -> 4 -> 1 -> 3.",
        "Section 321 chain: Ram Naresh Pandey (1957) -> Subhash Chander (1980) -> Sheonandan Paswan (1987) -> Abdul Karim (2000).",
        "பிரிவு 321 சங்கிலி: ராம் நரேஷ் பாண்டே (1957) -> சுபாஷ் சந்தர் (1980) -> ஷிவநந்தன் பாஸ்வான் (1987) -> அப்துல் கரீம் (2000).",
        "The court's consent under Section 321 is an active judicial function, not a rubber stamp.",
        "பிரிவு 321-ன் கீழான நீதிமன்ற ஒப்புதல் ஒரு தீவிர நீதித்துறை செயல்பாடு, வெறும் ஒப்புதல் முத்திரை அல்ல."
    )

    # Q12 (B) Correct seq: 1 - 4 - 2 - 3 (1956 -> 1976 -> 1978 -> 2016)
    # 1: 7th Amendment 1956, 2: 44th Amendment 1978, 3: 101st Amendment 2016, 4: 42nd Amendment 1976
    add_chrono(
        "ADVG_C_012", "Constitutional Amendments Federalism",
        "vital Constitutional Amendment Acts fundamentally affecting State executive and legislative powers",
        "மாநில நிர்வாக மற்றும் சட்டமன்ற அதிகாரங்களை பாதித்த முக்கிய அரசியலமைப்பு திருத்தச் சட்டங்கள்",
        "7th Constitutional Amendment Act (Reorganization of States and High Courts)", "7-வது அரசியலமைப்பு திருத்தச் சட்டம் (மாநிலங்கள் மற்றும் உயர் நீதிமன்றங்கள் மறுசீரமைப்பு)", 1956,
        "44th Constitutional Amendment Act (Safeguards against Article 356 misuse; Art 134A inserted)", "44-வது அரசியலமைப்பு திருத்தச் சட்டம் (உறுப்பு 356 துஷ்பிரயோகத் தடுப்பு; உறுப்பு 134A சேர்க்கை)", 1978,
        "101st Constitutional Amendment Act (Introduction of Goods and Services Tax / Article 246A)", "101-வது அரசியலமைப்பு திருத்தச் சட்டம் (சரக்கு மற்றும் சேவை வரி / உறுப்பு 246A அறிமுகம்)", 2016,
        "42nd Constitutional Amendment Act (Education and forests transferred to Concurrent List)", "42-வது அரசியலமைப்பு திருத்தச் சட்டம் (கல்வி மற்றும் காடுகள் பொதுப் பட்டியலுக்கு மாற்றம்)", 1976,
        "B",
        "1 - 2 - 4 - 3", "1 - 4 - 2 - 3", "4 - 1 - 2 - 3", "1 - 4 - 3 - 2",
        "The correct chronological sequence is: 7th Amendment (1956) -> 42nd Amendment (1976) -> 44th Amendment (1978) -> 101st Amendment (2016). Correct order: 1 -> 4 -> 2 -> 3.",
        "சரியான காலவரிசை: 7-வது திருத்தம் (1956) -> 42-வது திருத்தம் (1976) -> 44-வது திருத்தம் (1978) -> 101-வது திருத்தம் (2016). சரியான வரிசை: 1 -> 4 -> 2 -> 3.",
        "Major Amendments: 7th (1956) -> 42nd (1976) -> 44th (1978) -> 101st (2016).",
        "முக்கிய திருத்தங்கள்: 7-வது (1956) -> 42-வது (1976) -> 44-வது (1978) -> 101-வது (2016).",
        "The 101st Amendment radically transformed Indian fiscal federalism by introducing Article 246A.",
        "101-வது திருத்தம் உறுப்பு 246A-வை அறிமுகப்படுத்தியதன் மூலம் இந்திய நிதி கூட்டாட்சியை முற்றிலும் மாற்றியமைத்தது."
    )

    # Q13 (B) Correct seq: 3 - 1 - 4 - 2 (1958 -> 1964 -> 1998 -> 2024)
    # 1: Keshav Singh 1964, 2: Sita Soren 2024, 3: Searchlight 1958, 4: P.V. Narasimha Rao 1998
    add_chrono(
        "ADVG_C_013", "Legislative Privileges Jurisprudence",
        "milestones in the constitutional jurisprudence of legislative privileges under Article 105 and Article 194",
        "உறுப்பு 105 மற்றும் 194-ன் கீழான சட்டமன்ற சிறப்புரிமைகள் தொடர்பான அரசியலமைப்புத் தீர்ப்புகளின் மைல்கற்கள்",
        "Special Reference No. 1 of 1964 (Keshav Singh case on judicial review of legislative warrants)", "1964-ஆம் ஆண்டின் சிறப்பு குறிப்பு எண் 1 (கேசவ் சிங் வழக்கு - சட்டமன்ற வாரண்டுகள் மீதான மறுஆய்வு)", 1964,
        "Sita Soren v. Union of India (7-judge bench overruling bribery immunity for legislators)", "சீதா சோரன் எதிர் இந்திய ஒன்றியம் (சட்டமன்ற உறுப்பினர்களின் லஞ்ச விலக்களிப்பை ரத்து செய்த 7 நீதிபதிகள் அமர்வு தீர்ப்பு)", 2024,
        "M.S.M. Sharma v. Sri Krishna Sinha (Searchlight case on fundamental rights and privileges)", "எம்.எஸ்.எம். சர்மா எதிர் ஸ்ரீ கிருஷ்ண சின்ஹா (சர்ச்லைட் வழக்கு - அடிப்படை உரிமைகள் மற்றும் சிறப்புரிமைகள்)", 1958,
        "P.V. Narasimha Rao v. State (CBI) (Majority ruling granting immunity for votes cast for bribe)", "பி.வி. நரசிம்ம ராவ் வழக்கு (லஞ்சம் பெற்று வாக்களித்ததற்கு விலக்களிப்பு அளித்த பெரும்பான்மைத் தீர்ப்பு)", 1998,
        "B",
        "3 - 4 - 1 - 2", "3 - 1 - 4 - 2", "1 - 3 - 4 - 2", "4 - 3 - 1 - 2",
        "The correct chronological sequence is: Searchlight case (1958) -> Keshav Singh case (1964) -> P.V. Narasimha Rao (1998) -> Sita Soren (2024). Correct order: 3 -> 1 -> 4 -> 2.",
        "சரியான காலவரிசை: சர்ச்லைட் வழக்கு (1958) -> கேசவ் சிங் வழக்கு (1964) -> பி.வி. நரசிம்ம ராவ் (1998) -> சீதா சோரன் (2024). சரியான வரிசை: 3 -> 1 -> 4 -> 2.",
        "Privilege Precedents: Searchlight (1958) -> Keshav Singh (1964) -> Narasimha Rao (1998) -> Sita Soren (2024).",
        "சிறப்புரிமை தீர்ப்புகள்: சர்ச்லைட் (1958) -> கேசவ் சிங் (1964) -> நரசிம்ம ராவ் (1998) -> சீதா சோரன் (2024).",
        "In 2024, a unanimous 7-judge bench in Sita Soren held that bribery destroys the foundation of representative democracy.",
        "2024-ல், சீதா சோரன் வழக்கில் 7 நீதிபதிகள் கொண்ட அமர்வு லஞ்சம் பெறுவது பிரதிநிதித்துவ ஜனநாயகத்தின் அடித்தளத்தையே அழிக்கிறது என்று தீர்ப்பளித்தது."
    )

    # --- 6 Questions with Key 'C' ---
    # Q14 (C) Correct seq: 2 - 1 - 4 - 3 (1993 -> 2003 -> 2005 -> 2013)
    # 1: CVC Act 2003, 2: Human Rights Act 1993, 3: Lokpal Act 2013, 4: RTI Act 2005
    add_chrono(
        "ADVG_C_014", "Statutory Oversight Authorities",
        "statutory enactments establishing key state oversight, transparency, and human rights bodies",
        "முக்கிய மாநில மேற்பார்வை, வெளிப்படைத்தன்மை மற்றும் மனித உரிமைகள் அமைப்புகளை நிறுவிய சட்டங்கள்",
        "Central Vigilance Commission Act enacted", "மத்திய ஊழல் கண்காணிப்பு ஆணையச் சட்டம் இயற்றப்படுதல்", 2003,
        "Protection of Human Rights Act enacted (State Human Rights Commissions established)", "மனித உரிமைகள் பாதுகாப்புச் சட்டம் இயற்றப்படுதல் (மாநில மனித உரிமைகள் ஆணையங்கள்)", 1993,
        "Lokpal and Lokayuktas Act enacted by Parliament", "நாடாளுமன்றத்தால் லோக்பால் மற்றும் லோக்ஆயுக்தா சட்டம் இயற்றப்படுதல்", 2013,
        "Right to Information Act enacted (State Information Commissions created)", "தகவல் அறியும் உரிமைச் சட்டம் இயற்றப்படுதல் (மாநில தகவல் ஆணையங்கள் உருவாக்கம்)", 2005,
        "C",
        "1 - 2 - 4 - 3", "2 - 4 - 1 - 3", "2 - 1 - 4 - 3", "4 - 2 - 1 - 3",
        "The correct chronological sequence is: Protection of Human Rights Act (1993) -> CVC Act (2003) -> Right to Information Act (2005) -> Lokpal and Lokayuktas Act (2013). Correct order: 2 -> 1 -> 4 -> 3.",
        "சரியான காலவரிசை: மனித உரிமைகள் பாதுகாப்புச் சட்டம் (1993) -> CVC சட்டம் (2003) -> தகவல் அறியும் உரிமைச் சட்டம் (2005) -> லோக்பால் மற்றும் லோக்ஆயுக்தா சட்டம் (2013). சரியான வரிசை: 2 -> 1 -> 4 -> 3.",
        "Statutory Oversight Timeline: Human Rights (1993) -> CVC (2003) -> RTI (2005) -> Lokpal (2013).",
        "கண்காணிப்பு அமைப்புகள் காலவரிசை: மனித உரிமைகள் (1993) -> CVC (2003) -> RTI (2005) -> லோக்பால் (2013).",
        "The Advocate General represents the State in constitutional litigation involving these commissions.",
        "இவ்வாணையங்கள் தொடர்பான அரசியலமைப்பு வழக்குகளில் தலைமை வழக்கறிஞர் மாநிலத்தைப் பிரதிநிதித்துவப்படுத்துகிறார்."
    )

    # Q15 (C) Correct seq: 4 - 1 - 3 - 2 (1961 -> 1974 -> 1994 -> 2010)
    # 1: Samsher Singh 1974, 2: B.P. Singhal 2010, 3: UP Law Officers 1994, 4: Babu Ram Upadhya 1961
    add_chrono(
        "ADVG_C_015", "Pleasure Doctrine Precedents",
        "Supreme Court judgments elaborating the scope, limits, and executive nature of the doctrine of pleasure",
        "விருப்பக் கோட்பாட்டின் வரம்புகள் மற்றும் நிர்வாகத் தன்மையை விளக்கும் உச்ச நீதிமன்றத் தீர்ப்புகள்",
        "Samsher Singh v. State of Punjab (Governor acts on Cabinet advice in all executive functions)", "ஷம்ஷேர் சிங் எதிர் பஞ்சாப் அரசு (நிர்வாகப் பணிகளில் ஆளுநர் அமைச்சரவை ஆலோசனைப்படி செயல்படுதல்)", 1974,
        "B.P. Singhal v. Union of India (Pleasure doctrine cannot be exercised arbitrarily or whimsically)", "பி.பி. சிங்கால் எதிர் இந்திய ஒன்றியம் (விருப்பக் கோட்பாட்டை தன்னிச்சையாகப் பயன்படுத்த முடியாது)", 2010,
        "State of U.P. v. U.P. State Law Officers Association (En masse dismissal of law officers reviewable)", "உ.பி. மாநில சட்ட அதிகாரிகள் சங்கம் வழக்கு (சட்ட அதிகாரிகள் ஒட்டுமொத்த நீக்கம் மறுஆய்வுக்குரியது)", 1994,
        "State of U.P. v. Babu Ram Upadhya (Classical analysis of pleasure doctrine under Indian Constitution)", "பாபு ராம் உபாத்யா வழக்கு (இந்திய அரசியலமைப்பின் கீழான விருப்பக் கோட்பாட்டின் செவ்வியல் ஆய்வு)", 1961,
        "C",
        "1 - 4 - 3 - 2", "4 - 3 - 1 - 2", "4 - 1 - 3 - 2", "3 - 4 - 1 - 2",
        "The correct chronological sequence is: Babu Ram Upadhya (1961) -> Samsher Singh (1974) -> UP Law Officers (1994) -> B.P. Singhal (2010). Correct order: 4 -> 1 -> 3 -> 2.",
        "சரியான காலவரிசை: பாபு ராம் உபாத்யா (1961) -> ஷம்ஷேர் சிங் (1974) -> உ.பி. சட்ட அதிகாரிகள் (1994) -> பி.பி. சிங்கால் (2010). சரியான வரிசை: 4 -> 1 -> 3 -> 2.",
        "Pleasure Doctrine Evolution: Upadhya (1961) -> Samsher (1974) -> UP Law Officers (1994) -> Singhal (2010).",
        "விருப்பக் கோட்பாடு பரிணாமம்: உபாத்யா (1961) -> ஷம்ஷேர் (1974) -> உ.பி. சட்ட அதிகாரிகள் (1994) -> சிங்கால் (2010).",
        "B.P. Singhal settled that pleasure is not an unbridled monarchical prerogative.",
        "விருப்பக் கோட்பாடு என்பது வரம்பற்ற மன்னராட்சி தனியுரிமை அல்ல என்பதை பி.பி. சிங்கால் வழக்கு நிறுவியது."
    )

    # Q16 (C) Correct seq: 1 - 4 - 2 - 3 (1800 -> 1861 -> 1915 -> 1961)
    # 1: Charter of 1800, 2: GoI Act 1915, 3: Advocates Act 1961, 4: High Courts Act 1861
    add_chrono(
        "ADVG_C_016", "Madras High Court History",
        "historical milestones in the judicial and legal institutional history of Madras / Tamil Nadu",
        "சென்னை / தமிழ்நாட்டின் நீதித்துறை மற்றும் சட்ட நிறுவன வரலாற்றின் வரலாற்று மைல்கற்கள்",
        "Letters Patent / Charter establishing the Supreme Court of Judicature at Madras", "சென்னையில் நீதித்துறை உச்ச நீதிமன்றத்தை நிறுவிய சாசனம்", 1800,
        "Government of India Act consolidating Indian high courts and provincial law officers", "இந்திய உயர் நீதிமன்றங்கள் மற்றும் மாகாண சட்ட அதிகாரிகளை ஒருங்கிணைத்த இந்திய அரசுச் சட்டம்", 1915,
        "Advocates Act unifying the Indian Bar and creating State Bar Councils", "இந்திய வழக்கறிஞர் சங்கத்தை ஒருங்கிணைத்து மாநில பார் கவுன்சில்களை உருவாக்கிய வழக்கறிஞர்கள் சட்டம்", 1961,
        "Indian High Courts Act establishing the High Court of Judicature at Madras", "சென்னை உயர் நீதிமன்றத்தை நிறுவிய இந்திய உயர் நீதிமன்றங்கள் சட்டம்", 1861,
        "C",
        "4 - 1 - 2 - 3", "1 - 2 - 4 - 3", "1 - 4 - 2 - 3", "4 - 2 - 1 - 3",
        "The correct chronological sequence is: Charter establishing Supreme Court of Madras (1800) -> Indian High Courts Act (1861) -> Government of India Act (1915) -> Advocates Act (1961). Correct order: 1 -> 4 -> 2 -> 3.",
        "சரியான காலவரிசை: சென்னை உச்ச நீதிமன்ற சாசனம் (1800) -> இந்திய உயர் நீதிமன்றங்கள் சட்டம் (1861) -> இந்திய அரசுச் சட்டம் (1915) -> வழக்கறிஞர்கள் சட்டம் (1961). சரியான வரிசை: 1 -> 4 -> 2 -> 3.",
        "Madras Legal History: Supreme Court of Madras (1800) -> High Court (1861) -> GoI Act (1915) -> Advocates Act (1961).",
        "சென்னை சட்ட வரலாறு: சென்னை உச்ச நீதிமன்றம் (1800) -> உயர் நீதிமன்றம் (1861) -> 1915 சட்டம் -> வழக்கறிஞர்கள் சட்டம் (1961).",
        "The Madras High Court was formally inaugurated on August 15, 1862.",
        "சென்னை உயர் நீதிமன்றம் ஆகஸ்ட் 15, 1862 அன்று முறைப்படி தொடங்கி வைக்கப்பட்டது."
    )

    # Q17 (C) Correct seq: 2 - 4 - 1 - 3 (1981 -> 1993 -> 1998 -> 2015)
    # 1: Third Judges Case 1998, 2: First Judges Case 1981, 3: NJAC Judgment 2015, 4: Second Judges Case 1993
    add_chrono(
        "ADVG_C_017", "Judges Cases Collegium Evolution",
        "the famous 'Judges Cases' shaping the appointment of High Court and Supreme Court judges in India",
        "இந்தியாவில் உயர் மற்றும் உச்ச நீதிமன்ற நீதிபதிகள் நியமனத்தை வடிவமைத்த புகழ்பெற்ற 'நீதிபதிகள் வழக்குகள்'",
        "In re: Special Reference 1 of 1998 (Third Judges Case establishing 4+1 collegium consultation)", "1998-ன் சிறப்பு குறிப்பு 1 (மூன்றாவது நீதிபதிகள் வழக்கு - 4+1 கொலீஜியம் முறை உருவாக்கம்)", 1998,
        "S.P. Gupta v. Union of India (First Judges Case upholding executive primacy)", "எஸ்.பி. குப்தா எதிர் இந்திய ஒன்றியம் (முதல் நீதிபதிகள் வழக்கு - நிர்வாக மேலாதிக்கத்தை உறுதி செய்தது)", 1981,
        "Supreme Court Advocates-on-Record Association v. UOI (Fourth Judges Case striking down NJAC)", "நான்காவது நீதிபதிகள் வழக்கு (NJAC சட்டத்தை ரத்து செய்த உச்ச நீதிமன்றத் தீர்ப்பு)", 2015,
        "Supreme Court Advocates-on-Record Association v. UOI (Second Judges Case creating Collegium)", "இரண்டாவது நீதிபதிகள் வழக்கு (கொலீஜியம் அமைப்பை உருவாக்கிய வரலாற்றுத் தீர்ப்பு)", 1993,
        "C",
        "2 - 1 - 4 - 3", "1 - 2 - 4 - 3", "2 - 4 - 1 - 3", "4 - 2 - 1 - 3",
        "The correct chronological sequence is: First Judges Case (1981) -> Second Judges Case (1993) -> Third Judges Case (1998) -> Fourth Judges Case / NJAC (2015). Correct order: 2 -> 4 -> 1 -> 3.",
        "சரியான காலவரிசை: முதல் நீதிபதிகள் வழக்கு (1981) -> இரண்டாவது நீதிபதிகள் வழக்கு (1993) -> மூன்றாவது நீதிபதிகள் வழக்கு (1998) -> நான்காவது நீதிபதிகள் வழக்கு / NJAC (2015). சரியான வரிசை: 2 -> 4 -> 1 -> 3.",
        "Judges Cases Progression: First (1981) -> Second (1993) -> Third (1998) -> Fourth/NJAC (2015).",
        "நீதிபதிகள் வழக்குகள் வரிசை: முதல் (1981) -> இரண்டாவது (1993) -> மூன்றாவது (1998) -> நான்காவது/NJAC (2015).",
        "High Court judges qualifications under Article 217(2) form the benchmark for Advocate General eligibility.",
        "உறுப்பு 217(2)-ன் கீழான உயர் நீதிமன்ற நீதிபதி தகுதிகளே தலைமை வழக்கறிஞர் தகுதிக்கான அளவுகோலாகும்."
    )

    # Q18 (C) Correct seq: 3 - 1 - 4 - 2 (1992 -> 1994 -> 2020 -> 2023)
    # 1: Ravi Naik 1994, 2: Subhash Desai 2023, 3: Kihoto Hollohan 1992, 4: Keisham Meghachandra 2020
    add_chrono(
        "ADVG_C_018", "Tenth Schedule Anti-Defection Rulings",
        "landmark decisions regarding the Tenth Schedule, Speaker's jurisdiction, and judicial review",
        "பத்தாவது அட்டவணை, சபாநாயகரின் அதிகார வரம்பு மற்றும் நீதித்துறை மறுஆய்வு தொடர்பான முக்கியத் தீர்ப்புகள்",
        "Ravi S. Naik v. Union of India (Voluntary giving up of membership broadly construed)", "ரவி எஸ். நாயக் எதிர் இந்திய ஒன்றியம் (உறுப்பினர் பதவியை தானாக முன்வந்து கைவிடுதல் விளக்கம்)", 1994,
        "Subhash Desai v. Principal Secretary, Maharashtra (Floor test and Speaker reference rules)", "சுபாஷ் தேசாய் வழக்கு (நம்பிக்கை வாக்கெடுப்பு மற்றும் சபாநாயகர் விதிகள்)", 2023,
        "Kihoto Hollohan v. Zachillhu (Constitution Bench upholding Tenth Schedule and tribunal status)", "கிகோட்டோ ஹோலோஹான் வழக்கு (பத்தாவது அட்டவணை மற்றும் தீர்ப்பாய நிலையை உறுதி செய்தல்)", 1992,
        "Keisham Meghachandra Singh v. Speaker, Manipur (Three-month timeline for deciding defection)", "கீஷம் மேகசந்திர சிங் வழக்கு (கட்சித் தாவலை தீர்மானிக்க 3 மாத காலக்கெடு)", 2020,
        "C",
        "3 - 4 - 1 - 2", "1 - 3 - 4 - 2", "3 - 1 - 4 - 2", "4 - 3 - 1 - 2",
        "The correct chronological sequence is: Kihoto Hollohan (1992) -> Ravi S. Naik (1994) -> Keisham Meghachandra (2020) -> Subhash Desai (2023). Correct order: 3 -> 1 -> 4 -> 2.",
        "சரியான காலவரிசை: கிகோட்டோ ஹோலோஹான் (1992) -> ரவி எஸ். நாயக் (1994) -> கீஷம் மேகசந்திர சிங் (2020) -> சுபாஷ் தேசாய் (2023). சரியான வரிசை: 3 -> 1 -> 4 -> 2.",
        "Anti-Defection Progression: Kihoto (1992) -> Ravi Naik (1994) -> Meghachandra (2020) -> Subhash Desai (2023).",
        "கட்சித் தாவல் தீர்ப்புகள்: கிகோட்டோ (1992) -> ரவி நாயக் (1994) -> மேகசந்திரா (2020) -> சுபாஷ் தேசாய் (2023).",
        "The Advocate General represents the State Government in defection disputes affecting majority testing.",
        "பெரும்பான்மை சோதனையைப் பாதிக்கும் கட்சித் தாவல் வழக்குகளில் தலைமை வழக்கறிஞர் மாநில அரசைப் பிரதிநிதித்துவப்படுத்துகிறார்."
    )

    # Q19 (C) Correct seq: 4 - 1 - 2 - 3 (1974 -> 1978 -> 1979 -> 2017)
    # 1: Maneka Gandhi 1978, 2: Ramana Dayaram Shetty 1979, 3: Shayara Bano 2017, 4: E.P. Royappa 1974
    add_chrono(
        "ADVG_C_019", "Article 14 Non-Arbitrariness Evolution",
        "landmark decisions expanding the scope of equality and non-arbitrariness under Article 14",
        "உறுப்பு 14-ன் கீழ் சமத்துவம் மற்றும் தன்னிச்சையின்மையின் வரம்பை விரிவுபடுத்திய முக்கியத் தீர்ப்புகள்",
        "Maneka Gandhi v. Union of India (Golden Triangle of Articles 14, 19, and 21 established)", "மேனகா காந்தி எதிர் இந்திய ஒன்றியம் (உறுப்புகள் 14, 19 மற்றும் 21-ன் பொன் முக்கோணம் நிறுவப்படுதல்)", 1978,
        "Ramana Dayaram Shetty v. International Airport Authority (State contracts bound by Article 14)", "ரமணா தயாரம் ஷெட்டி வழக்கு (அரசு ஒப்பந்தங்கள் உறுப்பு 14-க்கு கட்டுப்பட்டவை)", 1979,
        "Shayara Bano v. Union of India (Manifest arbitrariness recognized as ground to strike down law)", "ஷயாரா பானோ எதிர் இந்திய ஒன்றியம் (வெளிப்படையான தன்னிச்சைத் தன்மை சட்டம் ரத்துக்கான காரணமாகுதல்)", 2017,
        "E.P. Royappa v. State of Tamil Nadu (New doctrine of equality as antithesis of arbitrariness)", "இ.பி. ராயப்பா எதிர் தமிழ்நாடு அரசு (தன்னிச்சைத் தன்மைக்கு எதிரான சமத்துவப் புதிய கோட்பாடு)", 1974,
        "C",
        "1 - 4 - 2 - 3", "4 - 2 - 1 - 3", "4 - 1 - 2 - 3", "2 - 4 - 1 - 3",
        "The correct chronological sequence is: E.P. Royappa (1974) -> Maneka Gandhi (1978) -> Ramana Dayaram Shetty (1979) -> Shayara Bano (2017). Correct order: 4 -> 1 -> 2 -> 3.",
        "சரியான காலவரிசை: இ.பி. ராயப்பா (1974) -> மேனகா காந்தி (1978) -> ரமணா தயாரம் ஷெட்டி (1979) -> ஷயாரா பானோ (2017). சரியான வரிசை: 4 -> 1 -> 2 -> 3.",
        "Article 14 Evolution: Royappa (1974) -> Maneka (1978) -> Ramana (1979) -> Shayara Bano (2017).",
        "உறுப்பு 14 பரிணாமம்: ராயப்பா (1974) -> மேனகா (1978) -> ரமணா (1979) -> ஷயாரா பானோ (2017).",
        "Non-arbitrariness under Article 14 governs both statutory enactments and executive appointments of law officers.",
        "உறுப்பு 14-ன் கீழான தன்னிச்சையின்மை சட்டங்களையும், சட்ட அதிகாரிகளின் நிர்வாக நியமனங்களையும் நிர்வகிக்கிறது."
    )

    # --- 6 Questions with Key 'D' ---
    # Q20 (D) Correct seq: 2 - 4 - 1 - 3 (1962 -> 1983 -> 2023 -> 2024)
    # 1: State of Punjab v. Governor 2023, 2: Purushothaman Nambudiri 1962, 3: State of TN v. Governor 2024, 4: Hoechst Pharmaceuticals 1983
    add_chrono(
        "ADVG_C_020", "Article 200 Governor Assent Timeline",
        "landmark decisions regarding the Governor's options and duties when bills are presented for assent under Article 200",
        "உறுப்பு 200-ன் கீழ் மசோதாக்களுக்கு ஒப்புதல் அளிப்பது தொடர்பான ஆளுநரின் அதிகாரங்கள் குறித்த முக்கியத் தீர்ப்புகள்",
        "State of Punjab v. Principal Secretary to Governor (Governor cannot sit on bills indefinitely)", "பஞ்சாப் அரசு எதிர் ஆளுநரின் முதன்மைச் செயலாளர் (ஆளுநர் காலவரையின்றி மசோதாக்களை நிறுத்தி வைக்க முடியாது)", 2023,
        "Purushothaman Nambudiri v. State of Kerala (Pending bill does not lapse on dissolution of Assembly)", "புருஷோத்தமன் நம்பூதிரி எதிர் கேரள அரசு (பேரவை கலைக்கப்பட்டாலும் நிலுவை மசோதா காலாவதியாகாது)", 1962,
        "State of Tamil Nadu v. Governor of Tamil Nadu (Binding nature of re-passed bills under Art 200)", "தமிழ்நாடு அரசு எதிர் தமிழக ஆளுநர் (மீண்டும் நிறைவேற்றப்பட்ட மசோதாக்களுக்கு ஒப்புதல் கட்டாயம்)", 2024,
        "Hoechst Pharmaceuticals Ltd. v. State of Bihar (Presidential assent under Article 254(2) analyzed)", "ஹோய்ச்ட் பார்மாசூட்டிகல்ஸ் வழக்கு (உறுப்பு 254(2) குடியரசுத் தலைவர் ஒப்புதல் ஆய்வு)", 1983,
        "D",
        "1 - 2 - 4 - 3", "2 - 1 - 4 - 3", "4 - 2 - 1 - 3", "2 - 4 - 1 - 3",
        "The correct chronological sequence is: Purushothaman Nambudiri (1962) -> Hoechst Pharmaceuticals (1983) -> State of Punjab (2023) -> State of Tamil Nadu (2024). Correct order: 2 -> 4 -> 1 -> 3.",
        "சரியான காலவரிசை: புருஷோத்தமன் நம்பூதிரி (1962) -> ஹோய்ச்ட் பார்மாசூட்டிகல்ஸ் (1983) -> பஞ்சாப் அரசு வழக்கு (2023) -> தமிழ்நாடு அரசு வழக்கு (2024). சரியான வரிசை: 2 -> 4 -> 1 -> 3.",
        "Article 200 Lineage: Purushothaman (1962) -> Hoechst (1983) -> Punjab (2023) -> Tamil Nadu (2024).",
        "உறுப்பு 200 காலவரிசை: புருஷோத்தமன் (1962) -> ஹோய்ச்ட் (1983) -> பஞ்சாப் (2023) -> தமிழ்நாடு (2024).",
        "Recent judgments clarify that Governors must act within constitutional timelines and comity.",
        "சமீபத்திய தீர்ப்புகள் ஆளுநர்கள் அரசியலமைப்பு காலக்கெடுவிற்குள் செயல்பட வேண்டும் என்பதை தெளிவுபடுத்துகின்றன."
    )

    # Q21 (D) Correct seq: 3 - 1 - 4 - 2 (1974 -> 1981 -> 1986 -> 2010)
    # 1: Air Act 1981, 2: NGT Act 2010, 3: Water Act 1974, 4: Environment Act 1986
    add_chrono(
        "ADVG_C_021", "Environmental Legislation Milestones",
        "statutory enactments constituting the core environmental regulatory architecture in India",
        "இந்தியாவில் சுற்றுச்சூழல் ஒழுங்குமுறை கட்டமைப்பை உருவாக்கிய முக்கிய சட்டங்கள்",
        "Air (Prevention and Control of Pollution) Act enacted under Article 253", "உறுப்பு 253-ன் கீழ் காற்று (மாசு தடுப்பு மற்றும் கட்டுப்பாடு) சட்டம் இயற்றப்படுதல்", 1981,
        "National Green Tribunal Act enacted providing specialized environmental adjudication", "தேசிய பசுமைத் தீர்ப்பாயச் சட்டம் இயற்றப்படுதல் (சிறப்பு சுற்றுச்சூழல் நீதிமன்றம்)", 2010,
        "Water (Prevention and Control of Pollution) Act enacted under Article 252", "உறுப்பு 252-ன் கீழ் நீர் (மாசு தடுப்பு மற்றும் கட்டுப்பாடு) சட்டம் இயற்றப்படுதல்", 1974,
        "Environment (Protection) Act enacted following the Bhopal gas leak disaster", "போபால் விஷ வாயுப் பேரழிவைத் தொடர்ந்து சுற்றுச்சூழல் (பாதுகாப்பு) சட்டம் இயற்றப்படுதல்", 1986,
        "D",
        "1 - 3 - 4 - 2", "3 - 4 - 1 - 2", "4 - 3 - 1 - 2", "3 - 1 - 4 - 2",
        "The correct chronological sequence is: Water Act (1974) -> Air Act (1981) -> Environment Protection Act (1986) -> National Green Tribunal Act (2010). Correct order: 3 -> 1 -> 4 -> 2.",
        "சரியான காலவரிசை: நீர் சட்டம் (1974) -> காற்று சட்டம் (1981) -> சுற்றுச்சூழல் பாதுகாப்புச் சட்டம் (1986) -> தேசிய பசுமைத் தீர்ப்பாயச் சட்டம் (2010). சரியான வரிசை: 3 -> 1 -> 4 -> 2.",
        "Environmental Statutes: Water (1974) -> Air (1981) -> EPA (1986) -> NGT (2010).",
        "சுற்றுச்சூழல் சட்டங்கள்: நீர் (1974) -> காற்று (1981) -> EPA (1986) -> NGT (2010).",
        "The Advocate General represents the State Government in all major environmental litigation before NGT Benches.",
        "NGT அமர்வுகளின் முன் அனைத்து முக்கிய சுற்றுச்சூழல் வழக்குகளிலும் தலைமை வழக்கறிஞரே மாநிலத்தைப் பிரதிநிதித்துவப்படுத்துகிறார்."
    )

    # Q22 (D) Correct seq: 4 - 1 - 2 - 3 (1861 -> 1962 -> 1965 -> 1999)
    # 1: Vidyawati 1962, 2: Kasturi Lal 1965, 3: Common Cause 1999, 4: P&O Steam Navigation 1861
    add_chrono(
        "ADVG_C_022", "Article 300 Sovereign Immunity Cases",
        "historic decisions defining the limits of state liability and sovereign immunity under Article 300",
        "உறுப்பு 300-ன் கீழ் அரசு பொறுப்பு மற்றும் இறையாண்மை விலக்களிப்பின் வரம்புகளை வரையறுத்த வரலாற்றுத் தீர்ப்புகள்",
        "State of Rajasthan v. Vidyawati (State held vicariously liable for government driver's negligence)", "ராஜஸ்தான் அரசு எதிர் வித்யாவதி (அரசு ஓட்டுநரின் கவனக்குறைவுக்கு அரசு பொறுப்புடைமை)", 1962,
        "Kasturi Lal v. State of U.P. (Sovereign immunity upheld in gold theft by police)", "கஸ்தூரி லால் எதிர் உ.பி. அரசு (காவல்துறையினரின் தங்கம் திருட்டில் இறையாண்மை விலக்களிப்பு உறுதி)", 1965,
        "Common Cause v. Union of India (Petrol pump allotment; misfeasance in public office damages)", "காமன் காஸ் எதிர் இந்திய ஒன்றியம் (பெட்ரோல் பங்க் ஒதுக்கீடு; பொது அலுவலக முறைகேடு இழப்பீடு)", 1999,
        "Peninsular and Oriental Steam Navigation Co. v. Secretary of State (Distinction between sovereign and non-sovereign acts)", "பி&ஓ ஸ்டீம் நேவிகேஷன் வழக்கு (இறையாண்மை மற்றும் இறையாண்மை சாரா செயல்களுக்கு இடையேயான வேறுபாடு)", 1861,
        "D",
        "1 - 4 - 2 - 3", "4 - 2 - 1 - 3", "2 - 4 - 1 - 3", "4 - 1 - 2 - 3",
        "The correct chronological sequence is: P&O Steam Navigation (1861) -> Vidyawati (1962) -> Kasturi Lal (1965) -> Common Cause (1999). Correct order: 4 -> 1 -> 2 -> 3.",
        "சரியான காலவரிசை: பி&ஓ ஸ்டீம் நேவிகேஷன் (1861) -> வித்யாவதி (1962) -> கஸ்தூரி லால் (1965) -> காமன் காஸ் (1999). சரியான வரிசை: 4 -> 1 -> 2 -> 3.",
        "Sovereign Immunity Evolution: P&O (1861) -> Vidyawati (1962) -> Kasturi Lal (1965) -> Common Cause (1999).",
        "இறையாண்மை விலக்களிப்பு பரிணாமம்: பி&ஓ (1861) -> வித்யாவதி (1962) -> கஸ்தூரி லால் (1965) -> காமன் காஸ் (1999).",
        "Article 300 continues pre-constitutional liability tracing back to 1858.",
        "உறுப்பு 300 என்பது 1858-ஆம் ஆண்டிலிருந்து தொடரும் சுதந்திரத்திற்கு முந்தைய பொறுப்பை நீட்டிக்கிறது."
    )

    # Q23 (D) Correct seq: 1 - 4 - 2 - 3 (1950 -> 1951 -> 1972 -> 2002)
    # 1: RPA 1950, 2: Delimitation Act 1972, 3: Delimitation Act 2002, 4: RPA 1951
    add_chrono(
        "ADVG_C_023", "Electoral Law Evolution",
        "legislative enactments governing the democratic electoral architecture in India",
        "இந்தியாவில் ஜனநாயகத் தேர்தல் கட்டமைப்பை நிர்வகிக்கும் சட்டமன்ற சட்டங்கள்",
        "Representation of the People Act, 1950 (Voter registration and seat allocation enacted)", "மக்கள் பிரதிநிதித்துவச் சட்டம், 1950 (வாக்காளர் பதிவு மற்றும் இட ஒதுக்கீடு இயற்றப்படுதல்)", 1950,
        "Delimitation Act, 1972 enacted following the 1971 Census", "1971 மக்கள் தொகைக் கணக்கெடுப்பைத் தொடர்ந்து தொகுதி மறுவரையறைச் சட்டம் 1972 இயற்றப்படுதல்", 1972,
        "Delimitation Act, 2002 enacted setting up the Delimitation Commission headed by Justice Kuldip Singh", "நீதிபதி குல்தீப் சிங் தலைமையிலான தொகுதி மறுவரையறை ஆணையத்தை அமைத்த 2002 சட்டம்", 2002,
        "Representation of the People Act, 1951 (Conduct of elections and election petitions enacted)", "மக்கள் பிரதிநிதித்துவச் சட்டம், 1951 (தேர்தல் நடத்தை மற்றும் தேர்தல் மனுக்கள் இயற்றப்படுதல்)", 1951,
        "D",
        "1 - 2 - 4 - 3", "4 - 1 - 2 - 3", "1 - 4 - 3 - 2", "1 - 4 - 2 - 3",
        "The correct chronological sequence is: RPA 1950 -> RPA 1951 -> Delimitation Act 1972 -> Delimitation Act 2002. Correct order: 1 -> 4 -> 2 -> 3.",
        "சரியான காலவரிசை: மக்கள் பிரதிநிதித்துவச் சட்டம் 1950 -> மக்கள் பிரதிநிதித்துவச் சட்டம் 1951 -> தொகுதி மறுவரையறைச் சட்டம் 1972 -> தொகுதி மறுவரையறைச் சட்டம் 2002. சரியான வரிசை: 1 -> 4 -> 2 -> 3.",
        "Electoral Statutes: RPA 1950 -> RPA 1951 -> Delimitation 1972 -> Delimitation 2002.",
        "தேர்தல் சட்டங்கள்: RPA 1950 -> RPA 1951 -> மறுவரையறை 1972 -> மறுவரையறை 2002.",
        "The Advocate General represents the State Government when statutory electoral rules are challenged in court.",
        "சட்டப்பூர்வ தேர்தல் விதிகள் நீதிமன்றத்தில் சவால் செய்யப்படும் போது தலைமை வழக்கறிஞர் மாநில அரசைப் பிரதிநிதித்துவப்படுத்துகிறார்."
    )

    # Q24 (D) Correct seq: 3 - 1 - 4 - 2 (1966 -> 1976 -> 1980 -> 1996)
    # 1: K. Parasaran 1976, 2: K.V. Venkatapathy 1996, 3: Mohan Kumaramangalam 1966, 4: R. Krishnamoorthy 1980
    add_chrono(
        "ADVG_C_024", "Madras Advocate Generals Group 2",
        "tenure appointments of prominent Advocate Generals of Tamil Nadu across four decades",
        "நான்கு தசாப்தங்களில் தமிழ்நாட்டின் முக்கிய தலைமை வழக்கறிஞர்களின் பதவிக்கால நியமனங்கள்",
        "Appointment of K. Parasaran as Advocate General of Tamil Nadu", "கே. பராசரன் தமிழ்நாடு தலைமை வழக்கறிஞராக நியமிக்கப்படுதல்", 1976,
        "Appointment of K.V. Venkatapathy as Advocate General of Tamil Nadu", "கே.வி. வெங்கடபதி தமிழ்நாடு தலைமை வழக்கறிஞராக நியமிக்கப்படுதல்", 1996,
        "Appointment of Mohan Kumaramangalam as Advocate General of Madras", "மோகன் குமாரமங்கலம் சென்னை தலைமை வழக்கறிஞராக நியமிக்கப்படுதல்", 1966,
        "Appointment of R. Krishnamoorthy as Advocate General of Tamil Nadu", "ஆர். கிருஷ்ணமூர்த்தி தமிழ்நாடு தலைமை வழக்கறிஞராக நியமிக்கப்படுதல்", 1980,
        "D",
        "1 - 3 - 4 - 2", "3 - 4 - 1 - 2", "4 - 3 - 1 - 2", "3 - 1 - 4 - 2",
        "The correct chronological sequence is: Mohan Kumaramangalam (1966) -> K. Parasaran (1976) -> R. Krishnamoorthy (1980) -> K.V. Venkatapathy (1996). Correct order: 3 -> 1 -> 4 -> 2.",
        "சரியான காலவரிசை: மோகன் குமாரமங்கலம் (1966) -> கே. பராசரன் (1976) -> ஆர். கிருஷ்ணமூர்த்தி (1980) -> கே.வி. வெங்கடபதி (1996). சரியான வரிசை: 3 -> 1 -> 4 -> 2.",
        "TN AG Succession 2: Kumaramangalam (1966) -> Parasaran (1976) -> Krishnamoorthy (1980) -> Venkatapathy (1996).",
        "தமிழ்நாடு AG வரிசை 2: குமாரமங்கலம் (1966) -> பராசரன் (1976) -> கிருஷ்ணமூர்த்தி (1980) -> வெங்கடபதி (1996).",
        "K. Parasaran later served as the Attorney General of India (1983 to 1989).",
        "கே. பராசரன் பின்னர் இந்திய தலைமை வழக்கறிஞராகவும் (1983 முதல் 1989 வரை) பணியாற்றினார்."
    )

    # Q25 (D) Correct seq: 2 - 1 - 4 - 3 (1935 -> 1950 -> 1961 -> 2004)
    # 1: Constitution 1950, 2: GoI Act 1935, 3: M.T. Khan 2004, 4: Advocates Act 1961
    add_chrono(
        "ADVG_C_025", "Milestones in the Office of Advocate General",
        "defining constitutional and legal milestones in the creation, evolution, and interpretation of the office of Advocate General",
        "தலைமை வழக்கறிஞர் அலுவலகத்தின் உருவாக்கம், பரிணாமம் மற்றும் விளக்கத்தின் முக்கிய மைல்கற்கள்",
        "Adoption of Article 165 in the Constitution establishing the Advocate General for each State", "ஒவ்வொரு மாநிலத்திற்கும் தலைமை வழக்கறிஞரை நிறுவும் அரசியலமைப்பின் உறுப்பு 165 ஏற்றுக்கொள்ளப்படுதல்", 1950,
        "Government of India Act enacting Section 55 establishing the office of Provincial Advocate-General", "மாகாண தலைமை வழக்கறிஞர் பதவியை நிறுவிய இந்திய அரசுச் சட்டத்தின் பிரிவு 55 இயற்றப்படுதல்", 1935,
        "Supreme Court judgment in M.T. Khan v. Govt of A.P. affirming the singular constitutional office", "ஒற்றை அரசியலமைப்பு பதவியை உறுதி செய்த எம்.டி. கான் வழக்கின் உச்ச நீதிமன்றத் தீர்ப்பு", 2004,
        "Advocates Act enacting Section 23 conferring statutory pre-audience on the Advocate General", "தலைமை வழக்கறிஞருக்கு சட்டப்பூர்வ முன்னுரிமையை வழங்கிய வழக்கறிஞர்கள் சட்டத்தின் பிரிவு 23 இயற்றப்படுதல்", 1961,
        "D",
        "1 - 2 - 4 - 3", "2 - 4 - 1 - 3", "4 - 2 - 1 - 3", "2 - 1 - 4 - 3",
        "The correct chronological sequence is: Government of India Act Section 55 (1935) -> Constitution of India Article 165 (1950) -> Advocates Act Section 23 (1961) -> M.T. Khan Judgment (2004). Correct order: 2 -> 1 -> 4 -> 3.",
        "சரியான காலவரிசை: இந்திய அரசுச் சட்டம் பிரிவு 55 (1935) -> இந்திய அரசியலமைப்பு உறுப்பு 165 (1950) -> வழக்கறிஞர்கள் சட்டம் பிரிவு 23 (1961) -> எம்.டி. கான் தீர்ப்பு (2004). சரியான வரிசை: 2 -> 1 -> 4 -> 3.",
        "Master Milestone Sequence: GoI Act (1935) -> Constitution (1950) -> Advocates Act (1961) -> M.T. Khan (2004).",
        "முதன்மை மைல்கற்கள் வரிசை: 1935 சட்டம் -> அரசியலமைப்பு (1950) -> வழக்கறிஞர்கள் சட்டம் (1961) -> எம்.டி. கான் (2004).",
        "These four milestones mark the complete historical arc of the Advocate General's constitutional office.",
        "இந்த நான்கு மைல்கற்களும் தலைமை வழக்கறிஞரின் அரசியலமைப்பு அலுவலகத்தின் முழுமையான வரலாற்றுப் பாதையைக் குறிக்கின்றன."
    )

    return qs

def main():
    questions = get_chronology_questions()
    print(f"Total Chronology questions generated: {len(questions)}")
    
    out_dir = "data/questions/polity"
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "advocate_general_chronology.json")
    
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)
    print(f"Saved to {out_file}")
    
    # 1. Validate with ChronologyValidator
    print("\n--- RUNNING CHRONOLOGY VALIDATOR ---")
    chrono_rep = ChronologyValidator.validate_file(out_file)
    print(f"Chronology Validator Result: {'PASS' if chrono_rep.is_valid else 'FAIL'}")
    if not chrono_rep.is_valid:
        for iss in chrono_rep.issues:
            print("Chronology Issue:", iss)
            
    # 2. Validate with ContentValidator
    print("\n--- RUNNING CONTENT VALIDATOR ---")
    validator = ContentValidator()
    report = validator.validate_file(out_file, expected_count=25, expected_prefix="ADVG_C_")
    print(f"Content Validator Result: {'PASS' if report.is_valid else 'FAIL'} | Audited: {report.total_audited}")
    print(f"Key Distribution: {report.key_distribution}")
    if not report.is_valid:
        for iss in report.issues:
            print("Issue:", iss.severity, iss.field, iss.message)

if __name__ == "__main__":
    main()
