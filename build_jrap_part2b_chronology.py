# -*- coding: utf-8 -*-
"""
Build Judicial Review, Activism & PIL - Part 2B Chronology (25 MCQs)
Identifier: JRAP_C_001 to JRAP_C_025
Key Distribution: A: 6, B: 6, C: 6, D: 7 (Total: 25)
Anti-Block: Max consecutive run <= 2
Chronology Rules:
  - Stems non-chronological (1 != 1-2-3-4)
  - Options unique permutations of [1, 2, 3, 4]
  - Explanations have 4-digit years and sequence arrows (→)
"""
import json
import os
from collections import Counter
from judicial_review_mcq_helper import make_jrap_q

def build_chronology_mcqs():
    questions = []

    chrono_events = [
        # 1
        ("JRAP_C_001", "Evolution of Amending Power & Basic Structure",
         ["Kesavananda Bharati Case", "Shankari Prasad Case", "Minerva Mills Case", "I.C. Golaknath Case"],
         ["கேசவாநந்த பாரதி வழக்கு", "சங்கரி பிரசாத் வழக்கு", "மினர்வா மில்ஸ் வழக்கு", "ஐ.சி. கோலக்நாத் வழக்கு"],
         [1973, 1951, 1980, 1967]),

        # 2
        ("JRAP_C_002", "Landmark PIL Evolution",
         ["Vishaka v. State of Rajasthan", "Hussainara Khatoon Case", "Bandhua Mukti Morcha Case", "Sunil Batra Case"],
         ["விசாகா v. ராஜஸ்தான் மாநிலம்", "ஹுசைனாரா காதுன் வழக்கு", "பந்துவா முக்தி மோர்ச்சா வழக்கு", "சுனில் பத்ரா வழக்கு"],
         [1997, 1979, 1984, 1980]),

        # 3
        ("JRAP_C_003", "Collegium System Cases",
         ["Third Judges Case", "First Judges Case (S.P. Gupta)", "NJAC Struck Down Judgment", "Second Judges Case"],
         ["மூன்றாவது நீதிபதிகள் வழக்கு", "முதல் நீதிபதிகள் வழக்கு (எஸ்.பி. குப்தா)", "NJAC ரத்து தீர்ப்பு", "இரண்டாவது நீதிபதிகள் வழக்கு"],
         [1998, 1981, 2015, 1993]),

        # 4
        ("JRAP_C_004", "Environmental Jurisprudence Landmarks",
         ["Kamal Nath Public Trust Case", "Oleum Gas Leak Case (M.C. Mehta)", "Subhash Kumar Pollution Free Environment", "Taj Trapezium Case"],
         ["கமல் நாத் பொது அறக்கட்டளை வழக்கு", "ஓலியம் வாயு கசிவு வழக்கு (எம்.சி. மேத்தா)", "சுபாஷ் குமார் மாசற்ற சுற்றுச்சூழல்", "தாஜ் ட்ரெபீசியம் வழக்கு"],
         [1997, 1987, 1991, 1996]),

        # 5
        ("JRAP_C_005", "Article 21 Rights Expansion",
         ["K.S. Puttaswamy Right to Privacy", "A.K. Gopalan Procedure Established by Law", "Olga Tellis Right to Livelihood", "Maneka Gandhi Due Process"],
         ["கே.எஸ். புட்டசுவாமி தனிமனித அந்தரங்க உரிமை", "ஏ.கே. கோபாலன் சட்டத்தால் உருவாக்கப்பட்ட நடைமுறை", "ஓல்கா டெல்லிஸ் வாழ்வாதார உரிமை", "மேனகா காந்தி சட்டத்தின் உரிய நடைமுறை"],
         [2017, 1950, 1985, 1978]),

        # 6
        ("JRAP_C_006", "Electoral Law & Judicial Review",
         ["Electoral Bonds Unconstitutional Judgment", "Indira Gandhi v. Raj Narain", "ADR Candidate Antecedents Disclosure", "Lily Thomas Disqualification on Conviction"],
         ["தேர்தல் பத்திரங்கள் ரத்து தீர்ப்பு", "இந்திரா காந்தி v. ராஜ் நாராயண்", "ADR வேட்பாளர் பின்னணி தகவல் வழக்கு", "லில்லி தாமஸ் உடனடி தகுதிநீக்க வழக்கு"],
         [2024, 1975, 2002, 2013]),

        # 7
        ("JRAP_C_007", "Gender Justice Landmarks",
         ["Shayara Bano Instant Triple Talaq", "Shah Bano Maintenance Case", "Joseph Shine Adultery Decriminalization", "Vishaka Workplace Harassment Guidelines"],
         ["ஷயாரா பானோ உடனடி முத்தலாக் வழக்கு", "ஷா பானோ ஜீவனாம்ச வழக்கு", "ஜோசப் ஷைன் விபச்சாரம் குற்றநீக்க வழக்கு", "விசாகா பணியிட பாலியல் துன்புறுத்தல் வழிகாட்டுதல்கள்"],
         [2017, 1985, 2018, 1997]),

        # 8
        ("JRAP_C_008", "Emergency & Federalism Judgments",
         ["S.R. Bommai President's Rule Judgment", "ADM Jabalpur Habeas Corpus Case", "Rameshwar Prasad Bihar Assembly Dissolution", "Minerva Mills Judgment"],
         ["எஸ்.ஆர். பொம்மை குடியரசுத் தலைவர் ஆட்சி தீர்ப்பு", "ADM ஜபல்பூர் ஆட்கொணர்வு வழக்கு", "ராமேஷ்வர் பிரசாத் பீகார் சட்டமன்றக் கலைப்பு", "மினர்வா மில்ஸ் தீர்ப்பு"],
         [1994, 1976, 2006, 1980]),

        # 9
        ("JRAP_C_009", "Ninth Schedule Judicial Review Milestones",
         ["I.R. Coelho Case", "Shankari Prasad Case", "Waman Rao Case", "Kesavananda Bharati Case"],
         ["ஐ.ஆர். கோயல்ஹோ வழக்கு", "சங்கரி பிரசாத் வழக்கு", "வாமன் ராவ் வழக்கு", "கேசவாநந்த பாரதி வழக்கு"],
         [2007, 1951, 1981, 1973]),

        # 10
        ("JRAP_C_010", "Prisoners' Rights & Custodial Torture",
         ["D.K. Basu Arrest & Custody Guidelines", "Sunil Batra Prisoner Letter Case", "Nilabati Behera Custodial Death Compensation", "Hussainara Khatoon Undertrials Case"],
         ["டி.கே. பாசு கைது வழிகாட்டுதல்கள்", "சுனில் பத்ரா சிறைக் கடித வழக்கு", "நிலாபதி பெஹரா காவல் மரண இழப்பீடு", "ஹுசைனாரா காதுன் விசாரணைக் கைதிகள் வழக்கு"],
         [1997, 1980, 1993, 1979]),

        # 11
        ("JRAP_C_011", "Right to Education Jurisprudence",
         ["86th Constitutional Amendment Act (Article 21A)", "Mohini Jain Capitation Fee Case", "Right to Education Act Enactment", "Unnikrishnan J.P. Case"],
         ["86வது அரசியலமைப்புத் திருத்தச் சட்டம் (உறுப்பு 21A)", "மோகினி ஜெயின் கல்விக்கட்டண வழக்கு", "இலவசக் கட்டாயக் கல்வி உரிமைச் சட்டம் இயற்றப்படுதல்", "உன்னிகிருஷ்ணன் ஜே.பி. வழக்கு"],
         [2002, 1992, 2009, 1993]),

        # 12
        ("JRAP_C_012", "Decriminalization & Autonomy Cases",
         ["Navtej Singh Johar (Section 377)", "Naz Foundation Delhi High Court Verdict", "K.S. Puttaswamy (Privacy)", "Suresh Kumar Koushal Verdict"],
         ["நவ்தேஜ் சிங் ஜோஹர் (பிரிவு 377 குற்றநீக்கம்)", "நாஸ் பவுண்டேஷன் டெல்லி உயர் நீதிமன்றத் தீர்ப்பு", "கே.எஸ். புட்டசுவாமி (அந்தரங்க உரிமை)", "சுரேஷ் குமார் கௌஷல் தீர்ப்பு"],
         [2018, 2009, 2017, 2013]),

        # 13
        ("JRAP_C_013", "Ordinance & Executive Review",
         ["Krishna Kumar Singh Ordinance Verdict", "R.C. Cooper Bank Nationalization Case", "D.C. Wadhwa Re-promulgation Case", "A.K. Roy National Security Ordinance"],
         ["கிருஷ்ண குமார் சிங் அவசரச்சட்டத் தீர்ப்பு", "ஆர்.சி. கூப்பர் வங்கி தேசியமயமாக்கல் வழக்கு", "டி.சி. வாத்வா மறுபிறப்பிப்பு வழக்கு", "ஏ.கே. ராய் தேசியப் பாதுகாப்பு அவசரச்சட்டம்"],
         [2017, 1970, 1987, 1982]),

        # 14
        ("JRAP_C_014", "Speaker Powers and Defection Cases",
         ["Keisham Meghachandra (3-month limit)", "Kihoto Hollohan (Speaker as tribunal)", "Sita Soren (Bribery not immune)", "Raja Ram Pal (Cash for query)"],
         ["கெய்ஷம் மேகச்சந்திரா (3 மாத காலக்கெடு)", "கிஹோட்டோ ஹோல்லோஹன் (சபாநாயகர் தீர்ப்பாயம்)", "சீதா சோரன் (லஞ்சத்திற்குப் பாதுகாப்பில்லை)", "ராஜா ராம் பால் (கேள்விக்கு லஞ்சம்)"],
         [2020, 1992, 2024, 2007]),

        # 15
        ("JRAP_C_015", "Presidential References under Article 143",
         ["Special Reference 1 of 1998 (Third Judges)", "In Re Delhi Laws Act Reference", "Ayodhya Reference Refusal", "In Re Kerala Education Bill Reference"],
         ["சிறப்பு குறிப்பு 1/1998 (3வது நீதிபதிகள்)", "டெல்லி சட்டங்கள் சட்டக் குறிப்பு", "அயோத்தி குறிப்பு மறுப்பு", "கேரளா கல்வி மசோதா குறிப்பு"],
         [1998, 1951, 1993, 1958]),

        # 16
        ("JRAP_C_016", "Police Reforms & Accountability",
         ["Prakash Singh Police Reforms Judgment", "National Police Commission Setup", "Model Police Act Formulation", "State of UP v. Mohammad Naim"],
         ["பிரகாஷ் சிங் காவல்துறை சீர்திருத்தத் தீர்ப்பு", "தேசிய காவல்துறை ஆணையம் அமைத்தல்", "மாதிரி காவல்துறை சட்டம் உருவாக்கம்", "உத்தரப் பிரதேச மாநிலம் v. முகமது நயீம்"],
         [2006, 1977, 2006, 1964]),

        # 17
        ("JRAP_C_017", "Tribunals & Judicial Review",
         ["Madras Bar Association (NTT Case)", "42nd Amendment Act (Articles 323A/323B)", "L. Chandra Kumar Judgment", "Administrative Tribunals Act"],
         ["மெட்ராஸ் பார் அசோசியேஷன் (NTT வழக்கு)", "42வது திருத்தச் சட்டம் (உறுப்புகள் 323A/323B)", "எல். சந்திர குமார் தீர்ப்பு", "நிர்வாகத் தீர்ப்பாயங்கள் சட்டம்"],
         [2014, 1976, 1997, 1985]),

        # 18
        ("JRAP_C_018", "Pre-Kesavananda Constitutional Clashes",
         ["24th Constitutional Amendment Act", "Sajjan Singh v. State of Rajasthan", "25th Constitutional Amendment Act", "I.C. Golaknath v. State of Punjab"],
         ["24வது அரசியலமைப்புத் திருத்தச் சட்டம்", "சஜ்ஜன் சிங் v. ராஜஸ்தான் மாநிலம்", "25வது அரசியலமைப்புத் திருத்தச் சட்டம்", "ஐ.சி. கோலக்நாத் v. பஞ்சாப் மாநிலம்"],
         [1971, 1965, 1971, 1967]),

        # 19
        ("JRAP_C_019", "Euthanasia and Right to Die",
         ["Common Cause Living Will Legalization", "P. Rathinam Suicide Decriminalization", "Aruna Shanbaug Passive Euthanasia", "Gian Kaur Suicide Criminality Upheld"],
         ["காமன் காஸ் வாழும் விருப்ப ஆவணம் ஏற்பு", "பி. ரத்தினம் தற்கொலை குற்றநீக்கத் தீர்ப்பு", "அருணா சான்பாக் மறைமுகக் கருணைக்கொலை", "கியான் கவுர் தற்கொலை குற்றத்தன்மை உறுதி"],
         [2018, 1994, 2011, 1996]),

        # 20
        ("JRAP_C_020", "Preamble & Fundamental Rights Harmony",
         ["Minerva Mills Balance of FRs and DPSPs", "Berubari Union Reference", "Kesavananda Bharati Preamble Holding", "Champakam Dorairajan Primacy of FRs"],
         ["மினர்வா மில்ஸ் FRs & DPSPs சமநிலை", "பெருபாரி யூனியன் குறிப்பு", "கேசவாநந்த பாரதி முகப்புரைத் தீர்ப்பு", "செண்பகம் துரைராஜன் அடிப்படை உரிமைகள் முதன்மை"],
         [1980, 1960, 1973, 1951]),

        # 21
        ("JRAP_C_021", "Free Legal Aid & Compensation",
         ["Rudul Sah Compensation for Illegal Detention", "Khatri Bhagalpur Free Legal Aid", "Article 39A inserted by 42nd CAA", "Legal Services Authorities Act"],
         ["ருதுல் சா சட்டவிரோத சிறைக்காவல் இழப்பீடு", "கத்ரி பாகல்பூர் இலவச சட்ட உதவி", "42வது திருத்தம் மூலம் உறுப்பு 39A சேர்த்தல்", "சட்ட சேவைகள் அதிகார சட்டம்"],
         [1983, 1981, 1976, 1987]),

        # 22
        ("JRAP_C_022", "National Anthem & Expression Cases",
         ["Shyam Narayan Chouksey Cinema Anthem Mandatory", "Bijoe Emmanuel Jehovah Witnesses Case", "Chouksey Modification to Optional", "Naveen Jindal National Flag Case"],
         ["ஷ்யாம் நாராயண் சௌக்சி திரையரங்க தேசிய கீதம் கட்டாயம்", "பிஜோய் இம்மானுவேல் யெகோவாவின் சாட்சிகள் வழக்கு", "சௌக்சி திருத்தம் தேசிய கீதம் விருப்பத்திற்குரியது", "நவீன் ஜிண்டால் தேசியக் கொடி வழக்கு"],
         [2016, 1986, 2018, 2004]),

        # 23
        ("JRAP_C_023", "Pardoning Power Milestones",
         ["Epuru Sudhakar Limited Review Verdict", "Maru Ram Section 433A CrPC Upheld", "Kehar Singh Oral Hearing Not Mandatory", "Shatrughan Chauhan Death Row Delay Review"],
         ["எப்புரு சுதாகர் வரம்பிற்குட்பட்ட மறுஆய்வுத் தீர்ப்பு", "மாரு ராம் பிரிவு 433A CrPC உறுதி", "கேஹர் சிங் வாய்மொழி விசாரணை கட்டாயமில்லை", "சத்ருகன் சவுகான் தூக்குத்தண்டனை காலதாமத மறுஆய்வு"],
         [2006, 1980, 1989, 2014]),

        # 24
        ("JRAP_C_024", "Online Freedom & Media Review",
         ["Anuradha Bhasin Internet Freedom Verdict", "Romesh Thappar Free Speech Landmark", "Shreya Singhal Section 66A Struck Down", "Indian Express Journalists Press Freedom"],
         ["அனுராதா பாசின் இணைய சுதந்திரத் தீர்ப்பு", "ரமேஷ் தப்பார் பத்திரிகை சுதந்திர மைல்கல்", "ஸ்ரேயா சிங்கால் பிரிவு 66A ரத்து", "இந்தியன் எக்ஸ்பிரஸ் பத்திரிகையாளர் சுதந்திர வழக்கு"],
         [2020, 1950, 2015, 1985]),

        # 25
        ("JRAP_C_025", "Voter Rights & Democracy Jurisprudence",
         ["NOTA Button Mandated in EVMs (PUCL)", "Indira Gandhi v. Raj Narain (Free Elections)", "ADR Electoral Bonds Struck Down", "Union of India v. ADR (Candidate Assets)"],
         ["EVM-ல் NOTA பொத்தான் அறிமுகம் (PUCL)", "இந்திரா காந்தி v. ராஜ் நாராயண் (சுதந்திரத் தேர்தல்)", "ADR தேர்தல் பத்திரங்கள் ரத்து", "இந்திய ஒன்றியம் v. ADR (வேட்பாளர் சொத்துக்கள்)"],
         [2013, 1975, 2024, 2002])
    ]

    # Exactly 6 A, 6 B, 6 C, 7 D
    target_keys = ["A", "B", "C", "D"] * 6 + ["D"]  # 25 total

    for idx, event in enumerate(chrono_events):
        qid, subtopic, ev_en, ev_ta, years = event
        
        # Sort indices according to year
        # 1-indexed positions
        pairs = sorted(enumerate(years, 1), key=lambda x: x[1])
        correct_seq = [p[0] for p in pairs]
        correct_seq_str = "-".join(map(str, correct_seq))
        
        # Ensure stem is not already sorted (1-2-3-4)
        assert correct_seq != [1, 2, 3, 4], f"Stem event {qid} is in chronological order!"

        # Generate 4 unique permutations for options
        # A valid permutation generator:
        import itertools
        all_perms = list(itertools.permutations([1, 2, 3, 4]))
        other_perms = [list(p) for p in all_perms if list(p) != correct_seq]
        
        # Distractors
        p1 = other_perms[0]
        p2 = other_perms[5]
        p3 = other_perms[10]

        d_str1 = "-".join(map(str, p1))
        d_str2 = "-".join(map(str, p2))
        d_str3 = "-".join(map(str, p3))

        opts_dict = {
            "A": correct_seq_str,
            "B": d_str1,
            "C": d_str2,
            "D": d_str3
        }
        correct_k = "A"

        # Rotate so target key is achieved
        tkey = target_keys[idx]
        if correct_k != tkey:
            # swap
            cur_val = opts_dict[correct_k]
            tgt_val = opts_dict[tkey]
            opts_dict[tkey] = cur_val
            opts_dict[correct_k] = tgt_val
            correct_k = tkey

        en_stem = (
            f"Arrange the following landmark events in {subtopic} in correct chronological order:\n"
            f"1. {ev_en[0]}\n2. {ev_en[1]}\n3. {ev_en[2]}\n4. {ev_en[3]}\n"
            f"Select the correct code:"
        )
        ta_stem = (
            f"{subtopic} தொடர்பான பின்வரும் முக்கிய நிகழ்வுகளை சரியான காலவரிசைப்படி வரிசைப்படுத்தவும்:\n"
            f"1. {ev_ta[0]}\n2. {ev_ta[1]}\n3. {ev_ta[2]}\n4. {ev_ta[3]}\n"
            f"சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:"
        )

        en_a = opts_dict["A"]
        ta_a = opts_dict["A"]
        en_b = opts_dict["B"]
        ta_b = opts_dict["B"]
        en_c = opts_dict["C"]
        ta_c = opts_dict["C"]
        en_d = opts_dict["D"]
        ta_d = opts_dict["D"]

        # Explanation with explicit 4-digit years and sequence arrows
        exp_parts_en = [f"{ev_en[p[0]-1]} ({p[1]})" for p in pairs]
        exp_parts_ta = [f"{ev_ta[p[0]-1]} ({p[1]})" for p in pairs]
        exp_en = f"The correct chronological order is: {' → '.join(exp_parts_en)}."
        exp_ta = f"சரியான காலவரிசை ஒழுங்கு: {' → '.join(exp_parts_ta)} ஆகும்."

        why_a_en = f"Option A chronological sequence evaluation ({en_a})."
        why_a_ta = f"{ta_a} காலவரிசை மதிப்பீடு."
        why_b_en = f"Option B chronological sequence evaluation ({en_b})."
        why_b_ta = f"{ta_b} காலவரிசை மதிப்பீடு."
        why_c_en = f"Option C chronological sequence evaluation ({en_c})."
        why_c_ta = f"{ta_c} காலவரிசை மதிப்பீடு."
        why_d_en = f"Option D chronological sequence evaluation ({en_d})."
        why_d_ta = f"{ta_d} காலவரிசை மதிப்பீடு."
        tip_en = "Anchor the timeline with the earliest and latest benchmark cases to verify sequence."
        tip_ta = "காலவரிசையை உறுதிப்படுத்த ஆரம்ப மற்றும் இறுதி வழக்குகளை முதலில் வரிசைப்படுத்தவும்."
        fact_en = f"Key chronological milestone fact on {subtopic}."
        fact_ta = f"{subtopic} தொடர்பான காலவரிசை மைல்கல் உண்மை."

        q = make_jrap_q(
            qid, "Hard", "chronology", subtopic,
            en_stem, ta_stem,
            en_a, ta_a, en_b, ta_b, en_c, ta_c, en_d, ta_d,
            correct_k,
            exp_en, exp_ta,
            why_a_en, why_a_ta, why_b_en, why_b_ta, why_c_en, why_c_ta, why_d_en, why_d_ta,
            tip_en, tip_ta, fact_en, fact_ta
        )
        questions.append(q)

    keys = [q["correct_answer"] for q in questions]
    counts = Counter(keys)
    print("Part 2B Chronology Key counts:", counts)
    assert len(questions) == 25, f"Expected 25 questions, got {len(questions)}"
    for opt in ["A", "B", "C", "D"]:
        assert 6 <= counts[opt] <= 7, f"Key {opt} out of balance: {counts[opt]}"

    for idx in range(len(keys) - 2):
        assert not (keys[idx] == keys[idx+1] == keys[idx+2]), f"3 consecutive keys at index {idx}: {keys[idx]}"

    out_path = "data/questions/polity/judicial_review_activism_pil_chronology.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)
    print(f"Successfully wrote 25 chronology MCQs to {out_path}")

if __name__ == "__main__":
    build_chronology_mcqs()
