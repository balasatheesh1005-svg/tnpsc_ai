# build_dpsp_match_25.py
# Generates 25 Match the Following MCQs for Directive Principles of State Policy (DPSP)
# Target files: data/questions/polity/directive_principles_match.json & directive_principles_match_the_following.json

import json
import os

def generate_25_match_mcqs():
    questions = []

    def add_q(q_id, q_en, q_ta, l1_a_en, l1_a_ta, l1_b_en, l1_b_ta, l1_c_en, l1_c_ta, l1_d_en, l1_d_ta, l2_1_en, l2_1_ta, l2_2_en, l2_2_ta, l2_3_en, l2_3_ta, l2_4_en, l2_4_ta, opt_a, opt_b, opt_c, opt_d, correct, exp_en, exp_ta, tip_en, tip_ta, w_a_en, w_a_ta, w_b_en, w_b_ta, w_c_en, w_c_ta, w_d_en, w_d_ta):
        q_obj = {
            "id": f"DPSP_MTH_{q_id:03d}",
            "subject": "Polity",
            "topic": "Directive Principles of State Policy",
            "difficulty": "Medium",
            "question_type": "Match the Following",
            "question": {
                "en": q_en,
                "ta": q_ta
            },
            "list_1": [
                {"id": "A", "en": l1_a_en, "ta": l1_a_ta},
                {"id": "B", "en": l1_b_en, "ta": l1_b_ta},
                {"id": "C", "en": l1_c_en, "ta": l1_c_ta},
                {"id": "D", "en": l1_d_en, "ta": l1_d_ta}
            ],
            "list_2": [
                {"id": "1", "en": l2_1_en, "ta": l2_1_ta},
                {"id": "2", "en": l2_2_en, "ta": l2_2_ta},
                {"id": "3", "en": l2_3_en, "ta": l2_3_ta},
                {"id": "4", "en": l2_4_en, "ta": l2_4_ta}
            ],
            "options": [
                {"id": "A", "en": opt_a, "ta": opt_a},
                {"id": "B", "en": opt_b, "ta": opt_b},
                {"id": "C", "en": opt_c, "ta": opt_c},
                {"id": "D", "en": opt_d, "ta": opt_d}
            ],
            "correct_answer": correct,
            "explanation": {
                "en": exp_en,
                "ta": exp_ta
            },
            "why_not_others": {
                "A": {"en": w_a_en, "ta": w_a_ta},
                "B": {"en": w_b_en, "ta": w_b_ta},
                "C": {"en": w_c_en, "ta": w_c_ta},
                "D": {"en": w_d_en, "ta": w_d_ta}
            },
            "tnpsc_tip": {
                "en": tip_en,
                "ta": tip_ta
            },
            # Backward compatibility fields
            "question_en": q_en,
            "question_ta": q_ta,
            "options_en": [opt_a, opt_b, opt_c, opt_d],
            "options_ta": [opt_a, opt_b, opt_c, opt_d],
            "answer": correct.lower(),
            "explanation_en": exp_en,
            "explanation_ta": exp_ta
        }
        questions.append(q_obj)

    # -------------------------------------------------------------------------
    # Q1 (Correct: A) - Article ↔ Provision
    # -------------------------------------------------------------------------
    add_q(
        1,
        "Match List I (Articles of Part IV) with List II (Constitutional Provisions) and select the correct code:",
        "பட்டியல் I-ஐ (பகுதி IV உறுப்புகள்) பட்டியல் II உடன் (அரசியலமைப்பு விதிகள்) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "Article 36", "உறுப்பு 36", "Article 37", "உறுப்பு 37", "Article 38", "உறுப்பு 38", "Article 39A", "உறுப்பு 39A",
        "Definition of State for Part IV", "பகுதி IV-க்கான அரசு வரையறை",
        "Non-justiciable nature of DPSP", "DPSP-ன் அமல்படுத்த முடியாத இயல்பு",
        "Welfare social order informed by justice", "நீதி நிறைந்த நலன்சார் சமூக ஒழுங்கு",
        "Equal justice and free legal aid", "சம நீதியும் இலவச சட்ட உதவியும்",
        "A-1, B-2, C-3, D-4", "A-2, B-1, C-4, D-3", "A-1, B-3, C-2, D-4", "A-4, B-2, C-3, D-1",
        "A",
        "A-1: Art 36 defines State. B-2: Art 37 establishes non-justiciability. C-3: Art 38 directs welfare social order. D-4: Art 39A guarantees equal justice & free legal aid.",
        "A-1: உறுப்பு 36 அரசை வரையறுக்கிறது. B-2: உறுப்பு 37 அமல்படுத்த முடியாத தன்மையை நிறுவுகிறது. C-3: உறுப்பு 38 நலன்சார் சமூக ஒழுங்கை வழிகாட்டுகிறது. D-4: உறுப்பு 39A சம நீதி & இலவச சட்ட உதவியை உத்தரவாதம் செய்கிறது.",
        "Art 36 adopts Art 12 State definition; Art 37 makes DPSP non-justiciable.",
        "உறுப்பு 36 உறுப்பு 12 அரசு வரையறையை ஏற்கிறது; உறுப்பு 37 DPSP-ஐ அமல்படுத்த முடியாததாக்குகிறது.",
        "Correct. A-1, B-2, C-3, D-4 is the exact match.", "சரி. A-1, B-2, C-3, D-4 சரியான பொருத்தம்.",
        "Incorrect. Article 36 matches 1, not 2.", "தவறு. உறுப்பு 36 பொருத்தம் 1 ஆகும்.",
        "Incorrect. Article 38 matches 3, not 2.", "தவறு. உறுப்பு 38 பொருத்தம் 3 ஆகும்.",
        "Incorrect. Article 39A matches 4, not 1.", "தவறு. உறுப்பு 39A பொருத்தம் 4 ஆகும்."
    )

    # -------------------------------------------------------------------------
    # Q2 (Correct: B) - Article ↔ Provision
    # -------------------------------------------------------------------------
    add_q(
        2,
        "Match List I (Articles 40 to 43) with List II (Constitutional Directives) and select the correct code:",
        "பட்டியல் I-ஐ (உறுப்புகள் 40 முதல் 43 வரை) பட்டியல் II உடன் (அரசியலமைப்பு வழிகாட்டல்கள்) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "Article 40", "உறுப்பு 40", "Article 41", "உறுப்பு 41", "Article 42", "உறுப்பு 42", "Article 43", "உறுப்பு 43",
        "Right to work, education and public assistance", "வேலை, கல்வி மற்றும் பொது உதவி உரிமை",
        "Organization of Village Panchayats", "கிராம பஞ்சாயத்துகள் அமைத்தல்",
        "Living wage and cottage industries", "வாழ்வாதார ஊதியம் மற்றும் குடில்தொழில்கள்",
        "Humane conditions of work and maternity relief", "மனிதத்தன்மை வேலை நிலைமைகள் மற்றும் பேறுகால உதவி",
        "A-1, B-2, C-3, D-4", "A-2, B-1, C-4, D-3", "A-2, B-3, C-4, D-1", "A-4, B-1, C-2, D-3",
        "B",
        "A-2: Art 40 = Village Panchayats. B-1: Art 41 = Right to work & education. C-4: Art 42 = Humane work conditions & maternity relief. D-3: Art 43 = Living wage & cottage industries.",
        "A-2: உறுப்பு 40 = கிராம பஞ்சாயத்துகள். B-1: உறுப்பு 41 = வேலை & கல்வி உரிமை. C-4: உறுப்பு 42 = மனிதத்தன்மை வேலை நிலைமைகள் & பேறுகால உதவி. D-3: உறுப்பு 43 = வாழ்வாதார ஊதியம் & குடில்தொழில்கள்.",
        "Memorize Articles 40-43 in order: 40 Panchayats, 41 Work, 42 Maternity, 43 Living wage.",
        "உறுப்புகள் 40-43 வரிசையாக மனப்பாடம் செய்க: 40 பஞ்சாயத்துகள், 41 வேலை, 42 பேறுகாலம், 43 வாழ்வாதார ஊதியம்.",
        "Incorrect. Article 40 matches 2, not 1.", "தவறு. உறுப்பு 40 பொருத்தம் 2 ஆகும்.",
        "Correct. A-2, B-1, C-4, D-3 is the exact match.", "சரி. A-2, B-1, C-4, D-3 சரியான பொருத்தம்.",
        "Incorrect. Article 41 matches 1, not 3.", "தவறு. உறுப்பு 41 பொருத்தம் 1 ஆகும்.",
        "Incorrect. Article 40 matches 2, not 4.", "தவறு. உறுப்பு 40 பொருத்தம் 2 ஆகும்."
    )

    # -------------------------------------------------------------------------
    # Q3 (Correct: C) - Article ↔ Provision
    # -------------------------------------------------------------------------
    add_q(
        3,
        "Match List I (Articles 43A to 45) with List II (Constitutional Directives) and select the correct code:",
        "பட்டியல் I-ஐ (உறுப்புகள் 43A முதல் 45 வரை) பட்டியல் II உடன் (அரசியலமைப்பு வழிகாட்டல்கள்) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "Article 43A", "உறுப்பு 43A", "Article 43B", "உறுப்பு 43B", "Article 44", "உறுப்பு 44", "Article 45", "உறுப்பு 45",
        "Uniform Civil Code for citizens", "குடிமக்களுக்கான பொது சிவில் சட்டம்",
        "Early childhood care for children below 6 years", "6 வயதுக்குட்பட்ட குழந்தைகளுக்கான முன்பருவக் பராமரிப்பு",
        "Participation of workers in management of industries", "தொழிற்சாலைகள் மேலாண்மையில் தொழிலாளர்கள் பங்கேற்பு",
        "Promotion of Co-operative Societies", "கூட்டுறவுச் சங்கங்கள் மேம்பாடு",
        "A-1, B-2, C-3, D-4", "A-3, B-1, C-4, D-2", "A-3, B-4, C-1, D-2", "A-4, B-3, C-2, D-1",
        "C",
        "A-3: Art 43A = Workers' participation in management. B-4: Art 43B = Co-operative societies. C-1: Art 44 = Uniform Civil Code. D-2: Art 45 = Early childhood care (below 6 yrs).",
        "A-3: உறுப்பு 43A = மேலாண்மையில் தொழிலாளர் பங்கேற்பு. B-4: உறுப்பு 43B = கூட்டுறவுச் சங்கங்கள். C-1: உறுப்பு 44 = பொது சிவில் சட்டம். D-2: உறுப்பு 45 = முன்பருவக் பராமரிப்பு (6 வயதுக்கு கீழ்).",
        "Key Amendments: 43A added by 42nd CAA (1976); 43B added by 97th CAA (2011).", "முக்கிய திருத்தங்கள்: 43A 42வது திருத்தம் (1976); 43B 97வது திருத்தம் (2011).",
        "Incorrect. Article 43A matches 3, not 1.", "தவறு. உறுப்பு 43A பொருத்தம் 3 ஆகும்.",
        "Incorrect. Article 43B matches 4, not 1.", "தவறு. உறுப்பு 43B பொருத்தம் 4 ஆகும்.",
        "Correct. A-3, B-4, C-1, D-2 is the exact match.", "சரி. A-3, B-4, C-1, D-2 சரியான பொருத்தம்.",
        "Incorrect. Article 44 matches 1, not 2.", "தவறு. உறுப்பு 44 பொருத்தம் 1 ஆகும்."
    )

    # -------------------------------------------------------------------------
    # Q4 (Correct: D) - Article ↔ Provision
    # -------------------------------------------------------------------------
    add_q(
        4,
        "Match List I (Articles 46 to 48A) with List II (Constitutional Directives) and select the correct code:",
        "பட்டியல் I-ஐ (உறுப்புகள் 46 முதல் 48A வரை) பட்டியல் II உடன் (அரசியலமைப்பு வழிகாட்டல்கள்) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "Article 46", "உறுப்பு 46", "Article 47", "உறுப்பு 47", "Article 48", "உறுப்பு 48", "Article 48A", "உறுப்பு 48A",
        "Protection of environment, forests and wildlife", "சுற்றுச்சூழல், காடுகள் மற்றும் வனவிலங்குகள் பாதுகாப்பு",
        "Raising nutrition level, public health & prohibition", "சத்துணவு நிலை, பொது சுகாதாரம் & மதுவிலக்கு",
        "Scientific agriculture & cow slaughter prohibition", "அறிவியல் விவசாயம் & பசு வதைத் தடை",
        "Educational & economic promotion of SCs, STs", "எஸ்சி, எஸ்டி பிரிவினரின் கல்வி & பொருளாதார மேம்பாடு",
        "A-1, B-2, C-3, D-4", "A-4, B-3, C-2, D-1", "A-2, B-1, C-4, D-3", "A-4, B-2, C-3, D-1",
        "D",
        "A-4: Art 46 = SC/ST upliftment. B-2: Art 47 = Nutrition, health & liquor prohibition. C-3: Art 48 = Agriculture & cow slaughter prohibition. D-1: Art 48A = Environment protection.",
        "A-4: உறுப்பு 46 = எஸ்சி/எஸ்டி மேம்பாடு. B-2: உறுப்பு 47 = சத்துணவு, சுகாதாரம் & மதுவிலக்கு. C-3: உறுப்பு 48 = விவசாயம் & பசு வதைத் தடை. D-1: உறுப்பு 48A = சுற்றுச்சூழல் பாதுகாப்பு.",
        "Distinguish: Art 48 = Agriculture & cattle; Art 48A = Environment & wildlife.", "வேறுபடுத்துக: உறுப்பு 48 = விவசாயம் & கால்நடை; உறுப்பு 48A = சுற்றுச்சூழல் & வனவிலங்கு.",
        "Incorrect. Article 46 matches 4, not 1.", "தவறு. உறுப்பு 46 பொருத்தம் 4 ஆகும்.",
        "Incorrect. Article 47 matches 2, not 3.", "தவறு. உறுப்பு 47 பொருத்தம் 2 ஆகும்.",
        "Incorrect. Article 48 matches 3, not 4.", "தவறு. உறுப்பு 48 பொருத்தம் 3 ஆகும்.",
        "Correct. A-4, B-2, C-3, D-1 is the exact match.", "சரி. A-4, B-2, C-3, D-1 சரியான பொருத்தம்."
    )

    # -------------------------------------------------------------------------
    # Q5 (Correct: A) - Article ↔ Provision
    # -------------------------------------------------------------------------
    add_q(
        5,
        "Match List I (Articles 49 to 39(d)) with List II (Constitutional Directives) and select the correct code:",
        "பட்டியல் I-ஐ (உறுப்புகள் 49 முதல் 39(d) வரை) பட்டியல் II உடன் (அரசியலமைப்பு வழிகாட்டல்கள்) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "Article 49", "உறுப்பு 49", "Article 50", "உறுப்பு 50", "Article 51", "உறுப்பு 51", "Article 39(d)", "உறுப்பு 39(d)",
        "Protection of monuments of national importance", "தேசிய முக்கியத்துவம் வாய்ந்த நினைவிடங்கள் பாதுகாப்பு",
        "Separation of judiciary from executive", "நிர்வாகத்திலிருந்து நீதித்துறை பிரிப்பு",
        "Promotion of international peace & security", "சர்வதேச அமைதி & பாதுகாப்பு மேம்பாடு",
        "Equal pay for equal work for men and women", "ஆண், பெண் இருபாலருக்கும் சம வேலைக்கு சம ஊதியம்",
        "A-1, B-2, C-3, D-4", "A-2, B-1, C-4, D-3", "A-1, B-3, C-2, D-4", "A-4, B-2, C-3, D-1",
        "A",
        "A-1: Art 49 = Monuments protection. B-2: Art 50 = Separation of judiciary. C-3: Art 51 = International peace. D-4: Art 39(d) = Equal pay for equal work.",
        "A-1: உறுப்பு 49 = நினைவிடங்கள் பாதுகாப்பு. B-2: உறுப்பு 50 = நீதித்துறை பிரிப்பு. C-3: உறுப்பு 51 = சர்வதேச அமைதி. D-4: உறுப்பு 39(d) = சம வேலைக்கு சம ஊதியம்.",
        "Article 51 is the final DPSP in Part IV.", "உறுப்பு 51 பகுதி IV-ல் உள்ள கடைசி DPSP ஆகும்.",
        "Correct. A-1, B-2, C-3, D-4 is the exact match.", "சரி. A-1, B-2, C-3, D-4 சரியான பொருத்தம்.",
        "Incorrect. Article 49 matches 1, not 2.", "தவறு. உறுப்பு 49 பொருத்தம் 1 ஆகும்.",
        "Incorrect. Article 50 matches 2, not 3.", "தவறு. உறுப்பு 50 பொருத்தம் 2 ஆகும்.",
        "Incorrect. Article 39(d) matches 4, not 1.", "தவறு. உறுப்பு 39(d) பொருத்தம் 4 ஆகும்."
    )

    # -------------------------------------------------------------------------
    # Q6 (Correct: B) - Amendment ↔ Constitutional Change
    # -------------------------------------------------------------------------
    add_q(
        6,
        "Match List I (Constitutional Amendment Acts) with List II (DPSP Changes) and select the correct code:",
        "பட்டியல் I-ஐ (அரசியலமைப்பு திருத்தச் சட்டங்கள்) பட்டியல் II உடன் (DPSP மாற்றங்கள்) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "42nd Amendment Act 1976", "42வது திருத்தச் சட்டம் 1976", "44th Amendment Act 1978", "44வது திருத்தச் சட்டம் 1978", "73rd Amendment Act 1992", "73வது திருத்தச் சட்டம் 1992", "86th Amendment Act 2002", "86வது திருத்தச் சட்டம் 2002",
        "Inserted Article 38(2) on minimising inequalities", "சமத்துவமின்மையைக் குறைக்க உறுப்பு 38(2)-ஐ இணைத்தது",
        "Added 4 new DPSPs: Arts 39(f), 39A, 43A, 48A", "4 புதிய DPSP-களைச் சேர்த்தது: உறுப்புகள் 39(f), 39A, 43A, 48A",
        "Modified Article 45 to early childhood care below 6 yrs", "உறுப்பு 45-ஐ 6 வயதுக்குட்பட்ட முன்பருவப் பராமரிப்பாக மாற்றியது",
        "Added Part IX to constitutionalize Article 40 Panchayats", "உறுப்பு 40 பஞ்சாயத்துகளை அரசியலமைப்புமையாக்க பகுதி IX-ஐச் சேர்த்தது",
        "A-1, B-2, C-3, D-4", "A-2, B-1, C-4, D-3", "A-2, B-3, C-4, D-1", "A-4, B-1, C-2, D-3",
        "B",
        "A-2: 42nd CAA added 4 DPSPs (39f, 39A, 43A, 48A). B-1: 44th CAA added Art 38(2). C-4: 73rd CAA added Part IX (Art 40). D-3: 86th CAA modified Art 45.",
        "A-2: 42வது திருத்தம் 4 DPSP-களைச் சேர்த்தது (39f, 39A, 43A, 48A). B-1: 44வது திருத்தம் உறுப்பு 38(2)-ஐச் சேர்த்தது. C-4: 73வது திருத்தம் பகுதி IX-ஐச் சேர்த்தது (உறுப்பு 40). D-3: 86வது திருத்தம் உறுப்பு 45-ஐ மாற்றியது.",
        "High-yield Amendment map: 42nd = 4 DPSPs; 44th = Art 38(2); 73rd = Part IX; 86th = Art 45.", "முக்கிய திருத்த வரைபடம்: 42வது = 4 DPSP-கள்; 44வது = உறுப்பு 38(2); 73வது = பகுதி IX; 86வது = உறுப்பு 45.",
        "Incorrect. 42nd CAA matches 2, not 1.", "தவறு. 42வது திருத்தம் பொருத்தம் 2 ஆகும்.",
        "Correct. A-2, B-1, C-4, D-3 is the exact match.", "சரி. A-2, B-1, C-4, D-3 சரியான பொருத்தம்.",
        "Incorrect. 44th CAA matches 1, not 3.", "தவறு. 44வது திருத்தம் பொருத்தம் 1 ஆகும்.",
        "Incorrect. 42nd CAA matches 2, not 4.", "தவறு. 42வது திருத்தம் பொருத்தம் 2 ஆகும்."
    )

    # -------------------------------------------------------------------------
    # Q7 (Correct: C) - Case ↔ Principle
    # -------------------------------------------------------------------------
    add_q(
        7,
        "Match List I (Landmark SC Cases) with List II (Constitutional Principles Established) and select the correct code:",
        "பட்டியல் I-ஐ (முக்கிய SC வழக்குகள்) பட்டியல் II உடன் (நிறுவப்பட்ட அரசியலமைப்புக் கோட்பாடுகள்) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "Champakam Dorairajan (1951)", "செண்பகம் துரைராஜன் (1951)", "Re Kerala Education Bill (1958)", "கேரளா கல்வி மசோதா (1958)", "Kesavananda Bharati (1973)", "கேசவானந்த பாரதி (1973)", "Minerva Mills (1980)", "மினர்வா மில்ஸ் (1980)",
        "Upheld 1st part of Art 31C protecting Arts 39(b) & (c)", "39(b) & (c)-ஐப் பாதுகாக்கும் உறுப்பு 31C-ன் 1வது பகுதியை உறுதி செய்தது",
        "Balance between Part III and Part IV is a Basic Feature", "பகுதி III மற்றும் பகுதி IV இடையிலான சமநிலையே அடிப்படை அம்சம்",
        "FRs are superior and DPSPs run as subsidiary to Part III", "FR-கள் மேலானவை மற்றும் DPSP-கள் பகுதி III-க்கு துணையாகச் செயல்படும்",
        "Formulated the Doctrine of Harmonious Construction", "இணக்கமான விளக்கக் கோட்பாட்டை உருவாக்கியது",
        "A-1, B-2, C-3, D-4", "A-3, B-1, C-4, D-2", "A-3, B-4, C-1, D-2", "A-4, B-3, C-2, D-1",
        "C",
        "A-3: Champakam Dorairajan (FR superior, DPSP subsidiary). B-4: Re Kerala Education Bill (Harmonious Construction). C-1: Kesavananda Bharati (31C 1st part upheld). D-2: Minerva Mills (Part III/IV balance is Basic Feature).",
        "A-3: செண்பகம் துரைராஜன் (FR மேலானது, DPSP துணை). B-4: கேரளா கல்வி மசோதா (இணக்கமான விளக்கம்). C-1: கேசவானந்த பாரதி (31C 1வது பகுதி உறுதி). D-2: மினர்வா மில்ஸ் (பகுதி III/IV சமநிலை அடிப்படை அம்சம்).",
        "FR vs DPSP evolution: Champakam (1951) -> Kerala Ed (1958) -> Kesavananda (1973) -> Minerva Mills (1980).", "FR vs DPSP வளர்ச்சி: செண்பகம் (1951) -> கேரளா கல்வி (1958) -> கேசவானந்த (1973) -> மினர்வா மில்ஸ் (1980).",
        "Incorrect. Champakam matches 3, not 1.", "தவறு. செண்பகம் பொருத்தம் 3 ஆகும்.",
        "Incorrect. Kerala Ed matches 4, not 1.", "தவறு. கேரளா கல்வி பொருத்தம் 4 ஆகும்.",
        "Correct. A-3, B-4, C-1, D-2 is the exact match.", "சரி. A-3, B-4, C-1, D-2 சரியான பொருத்தம்.",
        "Incorrect. Minerva Mills matches 2, not 1.", "தவறு. மினர்வா மில்ஸ் பொருத்தம் 2 ஆகும்."
    )

    # -------------------------------------------------------------------------
    # Q8 (Correct: D) - DPSP ↔ Conventional Classification
    # -------------------------------------------------------------------------
    add_q(
        8,
        "Match List I (DPSP Directives) with List II (Conventional Ideological Classifications) and select the correct code:",
        "பட்டியல் I-ஐ (DPSP வழிகாட்டல்கள்) பட்டியல் II உடன் (மரபுவழி தத்துவார்த்த வகைப்பாடுகள்) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "Article 39(b) & 39(c)", "உறுப்பு 39(b) & 39(c)", "Article 40 & 47 (liquor)", "உறுப்பு 40 & 47 (மதுவிலக்கு)", "Article 44 & 50", "உறுப்பு 44 & 50", "Article 43B", "உறுப்பு 43B",
        "Liberal-Intellectual Directive", "தாராளமய-அறிவுசார் வழிகாட்டல்",
        "Gandhian & Socialist Directive (97th CAA)", "காந்திய & சமதர்ம வழிகாட்டல் (97வது திருத்தம்)",
        "Socialist Directive", "சமதர்ம வழிகாட்டல்",
        "Gandhian Directive", "காந்திய வழிகாட்டல்",
        "A-1, B-2, C-3, D-4", "A-2, B-1, C-4, D-3", "A-3, B-1, C-4, D-2", "A-3, B-4, C-1, D-2",
        "D",
        "A-3: Art 39(b)/(c) = Socialist. B-4: Art 40 & 47 (liquor) = Gandhian. C-1: Art 44 & 50 = Liberal-Intellectual. D-2: Art 43B = Gandhian & Socialist (added by 97th CAA 2011).",
        "A-3: உறுப்பு 39(b)/(c) = சமதர்மம். B-4: உறுப்பு 40 & 47 (மதுவிலக்கு) = காந்தியம். C-1: உறுப்பு 44 & 50 = தாராளமய-அறிவுசார். D-2: உறுப்பு 43B = காந்திய & சமதர்மம் (97வது திருத்தம் 2011).",
        "Classification is academic; constitutional text in Part IV has no sub-headings.", "வகைப்பாடு கல்விசார்பானது; பகுதி IV உரையில் துணைத் தலைப்புகள் இல்லை.",
        "Incorrect. Article 39(b)/(c) matches 3, not 1.", "தவறு. உறுப்பு 39(b)/(c) பொருத்தம் 3 ஆகும்.",
        "Incorrect. Article 40 matches 4, not 1.", "தவறு. உறுப்பு 40 பொருத்தம் 4 ஆகும்.",
        "Incorrect. Article 44 matches 1, not 4.", "தவறு. உறுப்பு 44 பொருத்தம் 1 ஆகும்.",
        "Correct. A-3, B-4, C-1, D-2 is the exact match.", "சரி. A-3, B-4, C-1, D-2 சரியான பொருத்தம்."
    )

    # -------------------------------------------------------------------------
    # Q9 (Correct: A) - Article ↔ Specific Objective
    # -------------------------------------------------------------------------
    add_q(
        9,
        "Match List I (Article 38 & 39 Clauses) with List II (Specific Constitutional Objectives) and select the correct code:",
        "பட்டியல் I-ஐ (உறுப்பு 38 & 39 உட்பிரிவுகள்) பட்டியல் II உடன் (குறிப்பிட்ட அரசியலமைப்பு நோக்கங்கள்) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "Article 38(1)", "உறுப்பு 38(1)", "Article 39(b)", "உறுப்பு 39(b)", "Article 39(c)", "உறுப்பு 39(c)", "Article 39(e)", "உறுப்பு 39(e)",
        "Social order informed by social, economic & political justice", "சமூக, பொருளாதார & அரசியல் நீதி நிறைந்த சமூக ஒழுங்கு",
        "Distribution of material resources to subserve common good", "பொது நலனுக்குப் பயன்படும் வகையில் பொருள் வளப் பகிர்வு",
        "Prevention of concentration of wealth & means of production", "செல்வம் & உற்பத்தி சாதனங்கள் குவிப்பதைத் தடுத்தல்",
        "Protection of worker health and child tender age", "தொழிலாளர் சுகாதாரம் மற்றும் குழந்தை இளம் வயது பாதுகாப்பு",
        "A-1, B-2, C-3, D-4", "A-2, B-1, C-4, D-3", "A-1, B-3, C-2, D-4", "A-4, B-2, C-3, D-1",
        "A",
        "A-1: Art 38(1) = Social order justice. B-2: Art 39(b) = Material resources distribution. C-3: Art 39(c) = Wealth concentration prevention. D-4: Art 39(e) = Worker health & child tender age protection.",
        "A-1: உறுப்பு 38(1) = சமூக ஒழுங்கு நீதி. B-2: உறுப்பு 39(b) = பொருள் வளப் பகிர்வு. C-3: உறுப்பு 39(c) = செல்வக் குவிப்புத் தடை. D-4: உறுப்பு 39(e) = தொழிலாளர் சுகாதாரம் & குழந்தை இளம் வயது பாதுகாப்பு.",
        "Articles 39(b) and 39(c) are protected under Article 31C.", "உறுப்புகள் 39(b) மற்றும் 39(c) உறுப்பு 31C-ன் கீழ் பாதுகாக்கப்படுகின்றன.",
        "Correct. A-1, B-2, C-3, D-4 is the exact match.", "சரி. A-1, B-2, C-3, D-4 சரியான பொருத்தம்.",
        "Incorrect. Article 38(1) matches 1, not 2.", "தவறு. உறுப்பு 38(1) பொருத்தம் 1 ஆகும்.",
        "Incorrect. Article 39(c) matches 3, not 2.", "தவறு. உறுப்பு 39(c) பொருத்தம் 3 ஆகும்.",
        "Incorrect. Article 39(e) matches 4, not 1.", "தவறு. உறுப்பு 39(e) பொருத்தம் 4 ஆகும்."
    )

    # -------------------------------------------------------------------------
    # Q10 (Correct: B) - Article ↔ Key Keyword
    # -------------------------------------------------------------------------
    add_q(
        10,
        "Match List I (42nd CAA Added DPSPs) with List II (Key Keywords) and select the correct code:",
        "பட்டியல் I-ஐ (42வது திருத்தத்தால் சேர்க்கப்பட்ட DPSP-கள்) பட்டியல் II உடன் (முக்கிய வார்த்தைகள்) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "Article 39A", "உறுப்பு 39A", "Article 43A", "உறுப்பு 43A", "Article 48A", "உறுப்பு 48A", "Article 39(f)", "உறுப்பு 39(f)",
        "Workers' participation in management", "மேலாண்மையில் தொழிலாளர்கள் பங்கேற்பு",
        "Free legal aid to the poor", "ஏழைகளுக்கு இலவச சட்ட உதவி",
        "Opportunities for healthy development of children", "குழந்தைகள் ஆரோக்கியமாக வளர்வதற்கான வாய்ப்புகள்",
        "Safeguard forests and wildlife", "காடுகள் மற்றும் வனவிலங்குகளைப் பாதுகாத்தல்",
        "A-1, B-2, C-3, D-4", "A-2, B-1, C-4, D-3", "A-2, B-3, C-4, D-1", "A-4, B-1, C-2, D-3",
        "B",
        "A-2: Art 39A = Free legal aid. B-1: Art 43A = Workers' participation in management. C-4: Art 48A = Safeguard forests & wildlife. D-3: Art 39(f) = Healthy child development opportunities.",
        "A-2: உறுப்பு 39A = இலவச சட்ட உதவி. B-1: உறுப்பு 43A = மேலாண்மையில் தொழிலாளர் பங்கேற்பு. C-4: உறுப்பு 48A = காடுகள் & வனவிலங்குகள் பாதுகாப்பு. D-3: உறுப்பு 39(f) = ஆரோக்கியமான குழந்தை வளர்ச்சி வாய்ப்புகள்.",
        "All 4 DPSPs were inserted by the 42nd Constitutional Amendment Act, 1976.", "4 DPSP-களும் 1976-ன் 42வது அரசியலமைப்பு திருத்தச் சட்டத்தால் சேர்க்கப்பட்டன.",
        "Incorrect. Article 39A matches 2, not 1.", "தவறு. உறுப்பு 39A பொருத்தம் 2 ஆகும்.",
        "Correct. A-2, B-1, C-4, D-3 is the exact match.", "சரி. A-2, B-1, C-4, D-3 சரியான பொருத்தம்.",
        "Incorrect. Article 43A matches 1, not 3.", "தவறு. உறுப்பு 43A பொருத்தம் 1 ஆகும்.",
        "Incorrect. Article 39A matches 2, not 4.", "தவறு. உறுப்பு 39A பொருத்தம் 2 ஆகும்."
    )

    # -------------------------------------------------------------------------
    # Q11 (Correct: C) - DPSP Article ↔ Related Fundamental Right
    # -------------------------------------------------------------------------
    add_q(
        11,
        "Match List I (DPSP Directives) with List II (Interrelated Fundamental Rights) and select the correct code:",
        "பட்டியல் I-ஐ (DPSP வழிகாட்டல்கள்) பட்டியல் II உடன் (தொடர்புடைய அடிப்படை உரிமைகள்) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "Article 45 (DPSP)", "உறுப்பு 45 (DPSP)", "Article 41 (DPSP)", "உறுப்பு 41 (DPSP)", "Article 39(d) (DPSP)", "உறுப்பு 39(d) (DPSP)", "Article 47 (DPSP)", "உறுப்பு 47 (DPSP)",
        "Article 14 & 16 (Equal Pay in Public Service)", "உறுப்பு 14 & 16 (பொதுப்பணியில் சம ஊதியம்)",
        "Article 21 (Right to Life & Public Health)", "உறுப்பு 21 (வாழ்வு உரிமை & பொது சுகாதாரம்)",
        "Article 21A (Free Education 6-14 yrs)", "உறுப்பு 21A (இலவசக் கல்வி 6-14 ஆண்டுகள்)",
        "Article 21 (Right to Work aspect via MGNREGA)", "உறுப்பு 21 (MGNREGA வழியே வேலை உரிமை அம்சம்)",
        "A-1, B-2, C-3, D-4", "A-3, B-1, C-4, D-2", "A-3, B-4, C-1, D-2", "A-4, B-3, C-2, D-1",
        "C",
        "A-3: Art 45 (DPSP) relates to Art 21A (FR). B-4: Art 41 (DPSP) relates to Art 21 (Right to Work/Livelihood). C-1: Art 39(d) (DPSP) relates to Arts 14 & 16 (Equal Pay). D-2: Art 47 (DPSP) relates to Art 21 (Public Health/Dignity).",
        "A-3: உறுப்பு 45 (DPSP) உறுப்பு 21A (FR)-உடன் தொடர்புடையது. B-4: உறுப்பு 41 (DPSP) உறுப்பு 21 (வேலை/வாழ்வாதார உரிமை)-உடன் தொடர்புடையது. C-1: உறுப்பு 39(d) (DPSP) உறுப்புகள் 14 & 16 (சம ஊதியம்)-உடன் தொடர்புடையது. D-2: உறுப்பு 47 (DPSP) உறுப்பு 21 (பொது சுகாதாரம்/கண்ணியம்)-உடன் தொடர்புடையது.",
        "SC expands Article 21 by incorporating DPSP policy goals.", "DPSP கொள்கை இலக்குகளை உள்ளடக்குவதன் மூலம் SC உறுப்பு 21-ஐ விரிவாக்குகிறது.",
        "Incorrect. Article 45 matches 3, not 1.", "தவறு. உறுப்பு 45 பொருத்தம் 3 ஆகும்.",
        "Incorrect. Article 41 matches 4, not 1.", "தவறு. உறுப்பு 41 பொருத்தம் 4 ஆகும்.",
        "Correct. A-3, B-4, C-1, D-2 is the exact match.", "சரி. A-3, B-4, C-1, D-2 சரியான பொருத்தம்.",
        "Incorrect. Article 47 matches 2, not 1.", "தவறு. உறுப்பு 47 பொருத்தம் 2 ஆகும்."
    )

    # -------------------------------------------------------------------------
    # Q12 (Correct: D) - DPSP Article ↔ Related Fundamental Duty
    # -------------------------------------------------------------------------
    add_q(
        12,
        "Match List I (State DPSPs in Part IV) with List II (Corresponding Citizen Fundamental Duties in Part IV-A) and select the correct code:",
        "பட்டியல் I-ஐ (பகுதி IV-ல் உள்ள அரசு DPSP-கள்) பட்டியல் II உடன் (பகுதி IV-A-ல் உள்ள இணையான குடிமகன் அடிப்படைக் கடமைகள்) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "Article 48A (DPSP)", "உறுப்பு 48A (DPSP)", "Article 45 (DPSP)", "உறுப்பு 45 (DPSP)", "Article 51 (DPSP)", "உறுப்பு 51 (DPSP)", "Article 49 (DPSP)", "உறுப்பு 49 (DPSP)",
        "Article 51A(f) (Value rich heritage of composite culture)", "உறுப்பு 51A(f) (கூட்டுப் பண்பாட்டின் வளமான பாரம்பரியத்தைப் போற்றுதல்)",
        "Article 51A(c) (Uphold sovereignty, unity & integrity)", "உறுப்பு 51A(c) (இறையாண்மை, ஒருமைப்பாடு & ஒற்றுமையைப் பேணுதல்)",
        "Article 51A(k) (Parent duty to educate child 6-14 yrs)", "உறுப்பு 51A(k) (6-14 வயது குழந்தைக்குக் கல்வி வழங்கும் பெற்றோர் கடமை)",
        "Article 51A(g) (Citizen duty to protect environment)", "உறுப்பு 51A(g) (சுற்றுச்சூழலைப் பாதுகாக்கும் குடிமகன் கடமை)",
        "A-1, B-2, C-3, D-4", "A-4, B-1, C-2, D-3", "A-2, B-3, C-4, D-1", "A-4, B-3, C-2, D-1",
        "D",
        "A-4: Art 48A (State Environment DPSP) pairs with Art 51A(g) (Citizen Environment Duty). B-3: Art 45 (State Early Child DPSP) pairs with Art 51A(k) (Parent Education Duty). C-2: Art 51 (State Foreign Peace DPSP) pairs with Art 51A(c) (Sovereignty/Unity Duty). D-1: Art 49 (State Monuments DPSP) pairs with Art 51A(f) (Rich Heritage Duty).",
        "A-4: உறுப்பு 48A (அரசு சுற்றுச்சூழல் DPSP) உறுப்பு 51A(g) (குடிமகன் சுற்றுச்சூழல் கடமை)-உடன் ஜோடியாகிறது. B-3: உறுப்பு 45 (அரசு குழந்தைகள் DPSP) உறுப்பு 51A(k) (பெற்றோர் கல்விக் கடமை)-உடன் ஜோடியாகிறது. C-2: உறுப்பு 51 (அரசு சர்வதேச அமைதி DPSP) உறுப்பு 51A(c) (இறையாண்மை கடமை)-உடன் ஜோடியாகிறது. D-1: உறுப்பு 49 (அரசு நினைவிடங்கள் DPSP) உறுப்பு 51A(f) (பாரம்பரிய கடமை)-உடன் ஜோடியாகிறது.",
        "Part IV State directives and Part IV-A Citizen duties form complementary pairs.", "பகுதி IV அரசு வழிகாட்டல்களும் பகுதி IV-A குடிமகன் கடமைகளும் நிரப்பு ஜோடிகளாக அமைகின்றன.",
        "Incorrect. Article 48A matches 4, not 1.", "தவறு. உறுப்பு 48A பொருத்தம் 4 ஆகும்.",
        "Incorrect. Article 45 matches 3, not 1.", "தவறு. உறுப்பு 45 பொருத்தம் 3 ஆகும்.",
        "Incorrect. Article 51 matches 2, not 4.", "தவறு. உறுப்பு 51 பொருத்தம் 2 ஆகும்.",
        "Correct. A-4, B-3, C-2, D-1 is the exact match.", "சரி. A-4, B-3, C-2, D-1 சரியான பொருத்தம்."
    )

    # -------------------------------------------------------------------------
    # Q13 (Correct: A) - Case ↔ Specific Holding
    # -------------------------------------------------------------------------
    add_q(
        13,
        "Match List I (Case Law) with List II (DPSP Integration Holding) and select the correct code:",
        "பட்டியல் I-ஐ (வழக்குச் சட்டம்) பட்டியல் II உடன் (DPSP இணைப்புத் தீர்ப்பு) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "State of TN v. Abu Kavur Bai (1984)", "தமிழ்நாடு அரசு எதிர் அபு கவூர் பாய் (1984)", "Randhir Singh (1982)", "ரந்தீர் சிங் (1982)", "Sanjeev Coke (1983)", "சஞ்சீவ் கோக் (1983)", "Hussainara Khatoon (1979)", "ஹுசைனாரா கதூன் (1979)",
        "Bus nationalization protected under Art 31C & 39(b)", "பேருந்து தேசியமயமாக்கல் உறுப்பு 31C & 39(b)-ன் கீழ் பாதுகாப்பு",
        "Equal Pay for Equal Work (Art 39d) read into Arts 14 & 16", "சம ஊதியம் (உறுப்பு 39d) உறுப்புகள் 14 & 16-க்குள் வாசிப்பு",
        "Coking coal nationalization protected under Art 31C & 39(b)", "கோக்கிங் நிலக்கரி தேசியமயமாக்கல் 31C & 39(b)-ன் கீழ் பாதுகாப்பு",
        "Free Legal Aid (Art 39A) read into Right to Life (Art 21)", "இலவச சட்ட உதவி (உறுப்பு 39A) வாழ்வு உரிமைக்குள் (உறுப்பு 21) வாசிப்பு",
        "A-1, B-2, C-3, D-4", "A-2, B-1, C-4, D-3", "A-1, B-3, C-2, D-4", "A-4, B-2, C-3, D-1",
        "A",
        "A-1: Abu Kavur Bai 1984 (TN Bus nationalization Art 31C/39b). B-2: Randhir Singh 1982 (Equal Pay Art 39d into Arts 14/16). C-3: Sanjeev Coke 1983 (Coking Coal Art 31C/39b). D-4: Hussainara Khatoon 1979 (Free Legal Aid Art 39A into Art 21).",
        "A-1: அபு கவூர் பாய் 1984 (TN பேருந்து தேசியமயமாக்கல் உறுப்பு 31C/39b). B-2: ரந்தீர் சிங் 1982 (சம ஊதியம் உறுப்பு 39d உறுப்புகள் 14/16-க்குள்). C-3: சஞ்சீவ் கோக் 1983 (கோக்கிங் நிலக்கரி உறுப்பு 31C/39b). D-4: ஹுசைனாரா கதூன் 1979 (இலவச சட்ட உதவி உறுப்பு 39A உறுப்பு 21-க்குள்).",
        "All four cases represent landmark Supreme Court DPSP enforcement judgments.", "நான்கு வழக்குகளும் முக்கிய உச்ச நீதிமன்ற DPSP அமலாக்கத் தீர்ப்புகளாகும்.",
        "Correct. A-1, B-2, C-3, D-4 is the exact match.", "சரி. A-1, B-2, C-3, D-4 சரியான பொருத்தம்.",
        "Incorrect. Abu Kavur Bai matches 1, not 2.", "தவறு. அபு கவூர் பாய் பொருத்தம் 1 ஆகும்.",
        "Incorrect. Randhir Singh matches 2, not 3.", "தவறு. ரந்தீர் சிங் பொருத்தம் 2 ஆகும்.",
        "Incorrect. Hussainara Khatoon matches 4, not 1.", "தவறு. ஹுசைனாரா கதூன் பொருத்தம் 4 ஆகும்."
    )

    # -------------------------------------------------------------------------
    # Q14 (Correct: B) - Constitutional Phrase ↔ Article
    # -------------------------------------------------------------------------
    add_q(
        14,
        "Match List I (Constitutional Phrases in Part IV) with List II (Respective Articles) and select the correct code:",
        "பட்டியல் I-ஐ (பகுதி IV-ல் உள்ள அரசியலமைப்புத் தொடர்கள்) பட்டியல் II உடன் (உரிய உறுப்புகள்) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "'Fundamental in the governance of the country'", "'நாட்டின் ஆட்சியில் அடிப்படையானவை'", "'Minimise inequalities in income, status, facilities'", "'வருமானம், அந்தஸ்தில் சமத்துவமின்மையைக் குறைத்தல்'", "'Participation of workers in management'", "'மேலாண்மையில் தொழிலாளர்கள் பங்கேற்பு'", "'Separate the judiciary from the executive'", "'நிர்வாகத்திலிருந்து நீதித்துறையைப் பிரித்தல்'",
        "Article 38(2)", "உறுப்பு 38(2)",
        "Article 37", "உறுப்பு 37",
        "Article 50", "உறுப்பு 50",
        "Article 43A", "உறுப்பு 43A",
        "A-1, B-2, C-3, D-4", "A-2, B-1, C-4, D-3", "A-2, B-3, C-4, D-1", "A-4, B-1, C-2, D-3",
        "B",
        "A-2: 'Fundamental in governance' = Art 37. B-1: 'Minimise inequalities' = Art 38(2). C-4: 'Workers participation' = Art 43A. D-3: 'Separate judiciary' = Art 50.",
        "A-2: 'ஆட்சியில் அடிப்படையானவை' = உறுப்பு 37. B-1: 'சமத்துவமின்மையைக் குறைத்தல்' = உறுப்பு 38(2). C-4: 'தொழிலாளர்கள் பங்கேற்பு' = உறுப்பு 43A. D-3: 'நீதித்துறையைப் பிரித்தல்' = உறுப்பு 50.",
        "Exact text phrasing is tested frequently in TNPSC Group 1.", "துல்லியமான உரைத் தொடர்கள் டிஎன்பிஎஸ்சி குரூப் 1-ல் அடிக்கடி சோதிக்கப்படுகின்றன.",
        "Incorrect. Phrase A matches 2, not 1.", "தவறு. தொடர் A பொருத்தம் 2 ஆகும்.",
        "Correct. A-2, B-1, C-4, D-3 is the exact match.", "சரி. A-2, B-1, C-4, D-3 சரியான பொருத்தம்.",
        "Incorrect. Phrase B matches 1, not 3.", "தவறு. தொடர் B பொருத்தம் 1 ஆகும்.",
        "Incorrect. Phrase A matches 2, not 4.", "தவறு. தொடர் A பொருத்தம் 2 ஆகும்."
    )

    # -------------------------------------------------------------------------
    # Q15 (Correct: C) - Constitutional Provision ↔ Enacting Act/System
    # -------------------------------------------------------------------------
    add_q(
        15,
        "Match List I (DPSP Articles) with List II (Statutory Legislation / System Enacted) and select the correct code:",
        "பட்டியல் I-ஐ (DPSP உறுப்புகள்) பட்டியல் II உடன் (இயற்றப்பட்ட சட்டங்கள் / அமைப்புகள்) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "Article 40", "உறுப்பு 40", "Article 41", "உறுப்பு 41", "Article 42", "உறுப்பு 42", "Article 49", "உறுப்பு 49",
        "Maternity Benefit Act 1961 / 2017", "பேறுகால நலச் சட்டம் 1961 / 2017",
        "AMASR Act 1958 & ASI", "AMASR சட்டம் 1958 & ASI",
        "73rd Amendment Act 1992 & Part IX", "73வது திருத்தச் சட்டம் 1992 & பகுதி IX",
        "MGNREGA 2005", "MGNREGA 2005",
        "A-1, B-2, C-3, D-4", "A-3, B-1, C-4, D-2", "A-3, B-4, C-1, D-2", "A-4, B-3, C-2, D-1",
        "C",
        "A-3: Art 40 implemented by 73rd CAA 1992 (Part IX). B-4: Art 41 implemented by MGNREGA 2005. C-1: Art 42 implemented by Maternity Benefit Act 1961/2017. D-2: Art 49 implemented by AMASR Act 1958.",
        "A-3: உறுப்பு 40 73வது திருத்தம் 1992 (பகுதி IX) மூலம் செயல்படுத்தப்பட்டது. B-4: உறுப்பு 41 MGNREGA 2005 மூலம் செயல்படுத்தப்பட்டது. C-1: உறுப்பு 42 பேறுகால நலச் சட்டம் 1961/2017 மூலம் செயல்படுத்தப்பட்டது. D-2: உறுப்பு 49 AMASR சட்டம் 1958 மூலம் செயல்படுத்தப்பட்டது.",
        "Connecting DPSP Articles to actual Acts of Parliament is essential for Group 1 Mains & Prelims.", "DPSP உறுப்புகளை நாடாளுமன்ற அசல் சட்டங்களுடன் இணைப்பது குரூப் 1 நிலைகளுக்கு அத்தியாவசியமானது.",
        "Incorrect. Article 40 matches 3, not 1.", "தவறு. உறுப்பு 40 பொருத்தம் 3 ஆகும்.",
        "Incorrect. Article 41 matches 4, not 1.", "தவறு. உறுப்பு 41 பொருத்தம் 4 ஆகும்.",
        "Correct. A-3, B-4, C-1, D-2 is the exact match.", "சரி. A-3, B-4, C-1, D-2 சரியான பொருத்தம்.",
        "Incorrect. Article 49 matches 2, not 1.", "தவறு. உறுப்பு 49 பொருத்தம் 2 ஆகும்."
    )

    # -------------------------------------------------------------------------
    # Q16 (Correct: D) - DPSP ↔ Target Beneficiary Group
    # -------------------------------------------------------------------------
    add_q(
        16,
        "Match List I (DPSP Directives) with List II (Target Beneficiary Groups) and select the correct code:",
        "பட்டியல் I-ஐ (DPSP வழிகாட்டல்கள்) பட்டியல் II உடன் (இலக்கு பயனாளிகள் குழுக்கள்) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "Article 39(f)", "உறுப்பு 39(f)", "Article 43A", "உறுப்பு 43A", "Article 46", "உறுப்பு 46", "Article 47", "உறுப்பு 47",
        "General public needing public health & nutrition", "பொது சுகாதாரம் & சத்துணவு தேவைப்படும் பொதுமக்கள்",
        "Children needing healthy development opportunities", "ஆரோக்கியமான வளர்ச்சி வாய்ப்புகள் தேவைப்படும் குழந்தைகள்",
        "Industrial workers in management", "மேலாண்மையில் உள்ள தொழில்துறை தொழிலாளர்கள்",
        "Scheduled Castes, Scheduled Tribes & weaker sections", "பட்டியல் சாதியினர், பட்டியல் பழங்குடியினர் & எளிய பிரிவினர்",
        "A-1, B-2, C-3, D-4", "A-4, B-3, C-2, D-1", "A-2, B-1, C-4, D-3", "A-2, B-3, C-4, D-1",
        "D",
        "A-2: Art 39(f) = Children. B-3: Art 43A = Industrial workers. C-4: Art 46 = SCs, STs & weaker sections. D-1: Art 47 = General public (health/nutrition).",
        "A-2: உறுப்பு 39(f) = குழந்தைகள். B-3: உறுப்பு 43A = தொழிலாளர்கள். C-4: உறுப்பு 46 = எஸ்சி, எஸ்டி & எளிய பிரிவினர். D-1: உறுப்பு 47 = பொதுமக்கள் (சுகாதாரம்/சத்துணவு).",
        "Each DPSP directive targets specific vulnerable or general social segments.", "ஒவ்வொரு DPSP வழிகாட்டலும் குறிப்பிட்ட எளிய அல்லது பொதுவான சமூகப் பிரிவுகளை இலக்காகக் கொண்டுள்ளது.",
        "Incorrect. Article 39(f) matches 2, not 1.", "தவறு. உறுப்பு 39(f) பொருத்தம் 2 ஆகும்.",
        "Incorrect. Article 43A matches 3, not 2.", "தவறு. உறுப்பு 43A பொருத்தம் 3 ஆகும்.",
        "Incorrect. Article 47 matches 1, not 3.", "தவறு. உறுப்பு 47 பொருத்தம் 1 ஆகும்.",
        "Correct. A-2, B-3, C-4, D-1 is the exact match.", "சரி. A-2, B-3, C-4, D-1 சரியான பொருத்தம்."
    )

    # -------------------------------------------------------------------------
    # Q17 (Correct: A) - Article ↔ Key Exemption/Condition
    # -------------------------------------------------------------------------
    add_q(
        17,
        "Match List I (Articles/Provisions) with List II (Key Constitutional Qualification/Exemption) and select the correct code:",
        "பட்டியல் I-ஐ (உறுப்புகள்/விதிகள்) பட்டியல் II உடன் (முக்கிய அரசியலமைப்புத் தகுதி/விலக்கு) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "Article 37", "உறுப்பு 37", "Article 41", "உறுப்பு 41", "Article 47", "உறுப்பு 47", "Article 31C", "உறுப்பு 31C",
        "Non-justiciable in any court", "எந்தவொரு நீதிமன்றத்திலும் அமல்படுத்த முடியாதது",
        "Subject to limits of economic capacity", "பொருளாதாரத் திறனின் வரம்புகளுக்கு உட்பட்டது",
        "Prohibition EXCEPT for medicinal purposes", "மருத்துவ நோக்கங்களைத் தவிர பிறவற்றிற்கு மதுவிலக்கு",
        "Protection against Articles 14 and 19", "உறுப்புகள் 14 மற்றும் 19-க்கு எதிரான பாதுகாப்பு",
        "A-1, B-2, C-3, D-4", "A-2, B-1, C-4, D-3", "A-1, B-3, C-2, D-4", "A-4, B-2, C-3, D-1",
        "A",
        "A-1: Art 37 = Non-justiciable in court. B-2: Art 41 = Economic capacity limit. C-3: Art 47 = Prohibition except medicinal. D-4: Art 31C = Protection against Arts 14 & 19.",
        "A-1: உறுப்பு 37 = நீதிமன்றங்களில் அமல்படுத்த முடியாதது. B-2: உறுப்பு 41 = பொருளாதாரத் திறன் வரம்பு. C-3: உறுப்பு 47 = மருத்துவ நோக்கங்களைத் தவிர மதுவிலக்கு. D-4: உறுப்பு 31C = உறுப்புகள் 14 & 19-க்கு எதிரான பாதுகாப்பு.",
        "Constitutional qualifications restrict or clarify DPSP application scope.", "அரசியலமைப்புத் தகுதிகள் DPSP பயன்பாட்டு எல்லையைக் கட்டுப்படுத்துகின்றன அல்லது தெளிவுபடுத்துகின்றன.",
        "Correct. A-1, B-2, C-3, D-4 is the exact match.", "சரி. A-1, B-2, C-3, D-4 சரியான பொருத்தம்.",
        "Incorrect. Article 37 matches 1, not 2.", "தவறு. உறுப்பு 37 பொருத்தம் 1 ஆகும்.",
        "Incorrect. Article 41 matches 2, not 3.", "தவறு. உறுப்பு 41 பொருத்தம் 2 ஆகும்.",
        "Incorrect. Article 31C matches 4, not 1.", "தவறு. உறுப்பு 31C பொருத்தம் 4 ஆகும்."
    )

    # -------------------------------------------------------------------------
    # Q18 (Correct: B) - Case ↔ Landmark Area
    # -------------------------------------------------------------------------
    add_q(
        18,
        "Match List I (Landmark Cases) with List II (Specific DPSP Topic Area) and select the correct code:",
        "பட்டியல் I-ஐ (முக்கிய வழக்குகள்) பட்டியல் II உடன் (குறிப்பிட்ட DPSP தலைப்புப் பகுதி) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "F.N. Balsara (1951)", "F.N. பால்சரா (1951)", "Mirzapur Moti Kureshi (2005)", "மிர்சாபூர் மோதி குரேஷி (2005)", "M.C. Mehta cases", "எம்.சி. மேத்தா வழக்குகள்", "Bandhua Mukti Morcha (1984)", "பந்துவா முக்தி மோர்ச்சா (1984)",
        "Total ban on cow progeny slaughter under Art 48", "உறுப்பு 48-ன் கீழ் பசு சந்ததிகள் வதை மீதான முழுத் தடை",
        "State liquor prohibition upheld under Art 47 & 19(6)", "உறுப்புகள் 47 & 19(6)-ன் கீழ் மாநில மதுவிலக்கு உறுதி",
        "Humane work conditions Art 42 read into Art 21", "மனிதத்தன்மை வேலை நிலைமைகள் உறுப்பு 42 உறுப்பு 21-க்குள் வாசிப்பு",
        "Environment directives Art 48A & 51A(g) read into Art 21", "சுற்றுச்சூழல் உறுப்புகள் 48A & 51A(g) உறுப்பு 21-க்குள் வாசிப்பு",
        "A-1, B-2, C-3, D-4", "A-2, B-1, C-4, D-3", "A-2, B-3, C-4, D-1", "A-4, B-1, C-2, D-3",
        "B",
        "A-2: F.N. Balsara 1951 = Liquor prohibition Art 47. B-1: Mirzapur Kureshi 2005 = Cow slaughter Art 48. C-4: M.C. Mehta = Environment Art 48A/51A(g). D-3: Bandhua Mukti Morcha = Work conditions Art 42.",
        "A-2: F.N. பால்சரா 1951 = மதுவிலக்கு உறுப்பு 47. B-1: மிர்சாபூர் குரேஷி 2005 = பசு வதை உறுப்பு 48. C-4: எம்.சி. மேத்தா = சுற்றுச்சூழல் உறுப்பு 48A/51A(g). D-3: பந்துவா முக்தி மோர்ச்சா = வேலை நிலைமைகள் உறுப்பு 42.",
        "Landmark case laws synthesize DPSP directives into Art 21 Right to Life.", "முக்கிய வழக்குச் சட்டங்கள் DPSP வழிகாட்டல்களை உறுப்பு 21 வாழ்வு உரிமைக்குள் இணைக்கின்றன.",
        "Incorrect. F.N. Balsara matches 2, not 1.", "தவறு. F.N. பால்சரா பொருத்தம் 2 ஆகும்.",
        "Correct. A-2, B-1, C-4, D-3 is the exact match.", "சரி. A-2, B-1, C-4, D-3 சரியான பொருத்தம்.",
        "Incorrect. Mirzapur Kureshi matches 1, not 3.", "தவறு. மிர்சாபூர் குரேஷி பொருத்தம் 1 ஆகும்.",
        "Incorrect. F.N. Balsara matches 2, not 4.", "தவறு. F.N. பால்சரா பொருத்தம் 2 ஆகும்."
    )

    # -------------------------------------------------------------------------
    # Q19 (Correct: C) - Article ↔ Classification Group
    # -------------------------------------------------------------------------
    add_q(
        19,
        "Match List I (Article Pairings) with List II (Ideological Group Classification) and select the correct code:",
        "பட்டியல் I-ஐ (உறுப்பு ஜோடிகள்) பட்டியல் II உடன் (தத்துவார்த்த குழு வகைப்பாடு) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "Articles 38 & 39", "உறுப்புகள் 38 & 39", "Articles 40 & 47 (liquor)", "உறுப்புகள் 40 & 47 (மதுவிலக்கு)", "Articles 44 & 48A", "உறுப்புகள் 44 & 48A", "Articles 43A & 43B", "உறுப்புகள் 43A & 43B",
        "Liberal-Intellectual Directives", "தாராளமய-அறிவுசார் வழிகாட்டல்கள்",
        "Amended Directives (42nd & 97th CAAs)", "திருத்தப்பட்ட வழிகாட்டல்கள் (42வது & 97வது திருத்தங்கள்)",
        "Socialist Directives", "சமதர்ம வழிகாட்டல்கள்",
        "Gandhian Directives", "காந்திய வழிகாட்டல்கள்",
        "A-1, B-2, C-3, D-4", "A-3, B-1, C-4, D-2", "A-3, B-4, C-1, D-2", "A-4, B-3, C-2, D-1",
        "C",
        "A-3: Arts 38 & 39 = Socialist. B-4: Arts 40 & 47 = Gandhian. C-1: Arts 44 & 48A = Liberal-Intellectual. D-2: Arts 43A & 43B = Amended Directives (42nd CAA 1976 & 97th CAA 2011).",
        "A-3: உறுப்புகள் 38 & 39 = சமதர்மம். B-4: உறுப்புகள் 40 & 47 = காந்தியம். C-1: உறுப்புகள் 44 & 48A = தாராளமய-அறிவுசார். D-2: உறுப்புகள் 43A & 43B = திருத்தப்பட்ட வழிகாட்டல்கள் (42வது திருத்தம் 1976 & 97வது திருத்தம் 2011).",
        "Understand the ideological roots of each DPSP grouping.", "ஒவ்வொரு DPSP குழுவின் தத்துவார்த்த வேர்களைப் புரிந்து கொள்ளுங்கள்.",
        "Incorrect. Articles 38 & 39 match 3, not 1.", "தவறு. உறுப்புகள் 38 & 39 பொருத்தம் 3 ஆகும்.",
        "Incorrect. Articles 40 & 47 match 4, not 1.", "தவறு. உறுப்புகள் 40 & 47 பொருத்தம் 4 ஆகும்.",
        "Correct. A-3, B-4, C-1, D-2 is the exact match.", "சரி. A-3, B-4, C-1, D-2 சரியான பொருத்தம்.",
        "Incorrect. Articles 44 & 48A match 1, not 2.", "தவறு. உறுப்புகள் 44 & 48A பொருத்தம் 1 ஆகும்."
    )

    # -------------------------------------------------------------------------
    # Q20 (Correct: D) - Article ↔ Key Protection
    # -------------------------------------------------------------------------
    add_q(
        20,
        "Match List I (DPSP Provisions) with List II (Constitutional Protection / Goal) and select the correct code:",
        "பட்டியல் I-ஐ (DPSP விதிகள்) பட்டியல் II உடன் (அரசியலமைப்புப் பாதுகாப்பு / இலக்கு) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "Article 39(b) & (c)", "உறுப்பு 39(b) & (c)", "Article 39A", "உறுப்பு 39A", "Article 48A", "உறுப்பு 48A", "Article 51", "உறுப்பு 51",
        "International arbitration & peace", "சர்வதேச நடுவர் மன்றம் & அமைதி",
        "Free legal aid to indigent accused", "ஏழை குற்றஞ்சாட்டப்பட்டவருக்கு இலவச சட்ட உதவி",
        "Safeguard environment and forests", "சுற்றுச்சூழல் மற்றும் காடுகளைப் பாதுகாத்தல்",
        "Immunity from Arts 14 & 19 via Art 31C", "உறுப்பு 31C வழியே உறுப்புகள் 14 & 19-லிருந்து பாதுகாப்பு",
        "A-1, B-2, C-3, D-4", "A-2, B-1, C-4, D-3", "A-4, B-1, C-2, D-3", "A-4, B-2, C-3, D-1",
        "D",
        "A-4: Art 39(b)/(c) = Immunity via Art 31C. B-2: Art 39A = Free legal aid. C-3: Art 48A = Safeguard environment. D-1: Art 51 = International arbitration & peace.",
        "A-4: உறுப்பு 39(b)/(c) = உறுப்பு 31C வழியே பாதுகாப்பு. B-2: உறுப்பு 39A = இலவச சட்ட உதவி. C-3: உறுப்பு 48A = சுற்றுச்சூழல் பாதுகாப்பு. D-1: உறுப்பு 51 = சர்வதேச நடுவர் மன்றம் & அமைதி.",
        "Art 31C protection applies ONLY to Arts 39(b) and 39(c).", "உறுப்பு 31C பாதுகாப்பு உறுப்புகள் 39(b) மற்றும் 39(c)-க்கு மட்டுமே பொருந்தும்.",
        "Incorrect. Article 39(b)/(c) matches 4, not 1.", "தவறு. உறுப்பு 39(b)/(c) பொருத்தம் 4 ஆகும்.",
        "Incorrect. Article 39A matches 2, not 1.", "தவறு. உறுப்பு 39A பொருத்தம் 2 ஆகும்.",
        "Incorrect. Article 48A matches 3, not 2.", "தவறு. உறுப்பு 48A பொருத்தம் 3 ஆகும்.",
        "Correct. A-4, B-2, C-3, D-1 is the exact match.", "சரி. A-4, B-2, C-3, D-1 சரியான பொருத்தம்."
    )

    # -------------------------------------------------------------------------
    # Q21 (Correct: A) - Constituent Assembly Quote ↔ Author
    # -------------------------------------------------------------------------
    add_q(
        21,
        "Match List I (Constituent Assembly Quotes on DPSP) with List II (Authors/Scholars) and select the correct code:",
        "பட்டியல் I-ஐ (DPSP குறித்த அரசியலமைப்பு நிர்ணய சபை மேற்கோள்கள்) பட்டியல் II உடன் (ஆசிரியர்கள்/அறிஞர்கள்) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "'Novel Features of the Constitution'", "'அரசியலமைப்பின் நவீன அம்சங்கள்'", "'Conscience of the Constitution'", "'அரசியலமைப்பின் மனசாட்சி'", "'Cheque on a bank payable when resources permit'", "'வங்கியின் வசதி அனுமதிக்கும் போது செலுத்தத்தக்க காசோலை'", "'Pious Aspirations'", "'பக்தி விருப்பங்கள்'",
        "Dr. B.R. Ambedkar", "டாக்டர் பி.ஆர். அம்பேத்கர்",
        "Granville Austin", "கிரான்வில் ஆஸ்டின்",
        "Prof. K.T. Shah", "பேராசிரியர் கே.டி. ஷா",
        "Sir Ivor Jennings", "சர் ஐவர் ஜென்னிங்ஸ்",
        "A-1, B-2, C-3, D-4", "A-2, B-1, C-4, D-3", "A-1, B-3, C-2, D-4", "A-4, B-2, C-3, D-1",
        "A",
        "A-1: Dr. Ambedkar = 'Novel Features'. B-2: Granville Austin = 'Conscience of Constitution'. C-3: Prof. K.T. Shah = 'Cheque on a bank'. D-4: Sir Ivor Jennings = 'Pious Aspirations'.",
        "A-1: டாக்டர் அம்பேத்கர் = 'நவீன அம்சங்கள்'. B-2: கிரான்வில் ஆஸ்டின் = 'அரசியலமைப்பின் மனசாட்சி'. C-3: பேராசிரியர் கே.டி. ஷா = 'வங்கியின் காசோலை'. D-4: சர் ஐவர் ஜென்னிங்ஸ் = 'பக்தி விருப்பங்கள்'.",
        "All four quotes are standard high-priority TNPSC question items.", "நான்கு மேற்கோள்களும் தரப்படுத்தப்பட்ட உயர் முன்னுரிமை டிஎன்பிஎஸ்சி வினாக்கள் ஆகும்.",
        "Correct. A-1, B-2, C-3, D-4 is the exact match.", "சரி. A-1, B-2, C-3, D-4 சரியான பொருத்தம்.",
        "Incorrect. Quote A matches 1, not 2.", "தவறு. மேற்கோள் A பொருத்தம் 1 ஆகும்.",
        "Incorrect. Quote B matches 2, not 3.", "தவறு. மேற்கோள் B பொருத்தம் 2 ஆகும்.",
        "Incorrect. Quote D matches 4, not 1.", "தவறு. மேற்கோள் D பொருத்தம் 4 ஆகும்."
    )

    # -------------------------------------------------------------------------
    # Q22 (Correct: B) - Article ↔ Age Scope
    # -------------------------------------------------------------------------
    add_q(
        22,
        "Match List I (Articles on Education/Child Welfare) with List II (Age Demarcation Scope) and select the correct code:",
        "பட்டியல் I-ஐ (கல்வி/குழந்தை நலன் பற்றிய உறுப்புகள்) பட்டியல் II உடன் (வயது வரம்பு எல்லை) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "Article 45 (present DPSP)", "உறுப்பு 45 (தற்போதைய DPSP)", "Article 21A (Part III FR)", "உறுப்பு 21A (பகுதி III FR)", "Article 24 (Part III FR)", "உறுப்பு 24 (பகுதி III FR)", "Article 51A(k) (Part IV-A FD)", "உறுப்பு 51A(k) (பகுதி IV-A FD)",
        "Free and compulsory education 6 to 14 years", "6 முதல் 14 ஆண்டுகள் இலவச மற்றும் கட்டாயக் கல்வி",
        "Early childhood care & education below 6 years", "6 வயதுக்குட்பட்ட முன்பருவக் பராமரிப்பு & கல்வி",
        "Parent/guardian duty for education 6 to 14 years", "6 முதல் 14 ஆண்டுகள் பெற்றோர் கல்விக் கடமை",
        "Prohibition of employment below 14 years in factories", "தொழிற்சாலைகளில் 14 வயதுக்குட்பட்ட வேலைவாய்ப்புத் தடை",
        "A-1, B-2, C-3, D-4", "A-2, B-1, C-4, D-3", "A-2, B-3, C-4, D-1", "A-4, B-1, C-2, D-3",
        "B",
        "A-2: Art 45 (DPSP) = Below 6 yrs early childhood care. B-1: Art 21A (FR) = 6 to 14 yrs free education. C-4: Art 24 (FR) = Below 14 yrs child labor prohibition. D-3: Art 51A(k) (FD) = 6 to 14 yrs parent duty.",
        "A-2: உறுப்பு 45 (DPSP) = 6 வயதுக்கு கீழ் முன்பருவக் பராமரிப்பு. B-1: உறுப்பு 21A (FR) = 6 முதல் 14 ஆண்டுகள் இலவசக் கல்வி. C-4: உறுப்பு 24 (FR) = 14 வயதுக்கு கீழ் குழந்தைத் தொழிலாளர் தடை. D-3: உறுப்பு 51A(k) (FD) = 6 முதல் 14 ஆண்டுகள் பெற்றோர் கடமை.",
        "Age Demarcation Rule: Below 6 = Art 45; 6 to 14 = Art 21A & 51A(k); Below 14 = Art 24.", "வயது வரம்பு விதி: 6-க்கு கீழ் = உறுப்பு 45; 6 முதல் 14 = உறுப்பு 21A & 51A(k); 14-க்கு கீழ் = உறுப்பு 24.",
        "Incorrect. Article 45 matches 2, not 1.", "தவறு. உறுப்பு 45 பொருத்தம் 2 ஆகும்.",
        "Correct. A-2, B-1, C-4, D-3 is the exact match.", "சரி. A-2, B-1, C-4, D-3 சரியான பொருத்தம்.",
        "Incorrect. Article 21A matches 1, not 3.", "தவறு. உறுப்பு 21A பொருத்தம் 1 ஆகும்.",
        "Incorrect. Article 45 matches 2, not 4.", "தவறு. உறுப்பு 45 பொருத்தம் 2 ஆகும்."
    )

    # -------------------------------------------------------------------------
    # Q23 (Correct: C) - Article ↔ Scope of Directive
    # -------------------------------------------------------------------------
    add_q(
        23,
        "Match List I (Socialist Directives) with List II (Scope of Mandate) and select the correct code:",
        "பட்டியல் I-ஐ (சமதர்ம வழிகாட்டல்கள்) பட்டியல் II உடன் (கட்டளையின் எல்லை) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "Article 39(a)", "உறுப்பு 39(a)", "Article 39(e)", "உறுப்பு 39(e)", "Article 43", "உறுப்பு 43", "Article 43A", "உறுப்பு 43A",
        "Decent standard of life & leisure, cottage industries", "கண்ணியமான வாழ்க்கை முறை & ஓய்வு, குடில்தொழில்கள்",
        "Participation of workers in industrial management", "தொழில்துறை மேலாண்மையில் தொழிலாளர்கள் பங்கேற்பு",
        "Right to adequate means of livelihood for all", "அனைவருக்கும் போதுமான வாழ்வாதார வழிவகைகள் உரிமை",
        "Health and strength of workers and tender age of children", "தொழிலாளர் சுகாதாரம் மற்றும் குழந்தை இளம் வயது",
        "A-1, B-2, C-3, D-4", "A-3, B-1, C-4, D-2", "A-3, B-4, C-1, D-2", "A-4, B-3, C-2, D-1",
        "C",
        "A-3: Art 39(a) = Livelihood means. B-4: Art 39(e) = Health & strength of workers. C-1: Art 43 = Decent standard of life & cottage industries. D-2: Art 43A = Workers' participation in management.",
        "A-3: உறுப்பு 39(a) = வாழ்வாதார வழிவகைகள். B-4: உறுப்பு 39(e) = தொழிலாளர் சுகாதாரம் & பலம். C-1: உறுப்பு 43 = கண்ணியமான வாழ்க்கை முறை & குடில்தொழில்கள். D-2: உறுப்பு 43A = மேலாண்மையில் தொழிலாளர்கள் பங்கேற்பு.",
        "All four articles form the core labor welfare suite in Part IV.", "நான்கு உறுப்புகளும் பகுதி IV-ல் உள்ள முதன்மைத் தொழிலாளர் நலத் தொகுப்பை உருவாக்குகின்றன.",
        "Incorrect. Article 39(a) matches 3, not 1.", "தவறு. உறுப்பு 39(a) பொருத்தம் 3 ஆகும்.",
        "Incorrect. Article 39(e) matches 4, not 1.", "தவறு. உறுப்பு 39(e) பொருத்தம் 4 ஆகும்.",
        "Correct. A-3, B-4, C-1, D-2 is the exact match.", "சரி. A-3, B-4, C-1, D-2 சரியான பொருத்தம்.",
        "Incorrect. Article 43A matches 2, not 1.", "தவறு. உறுப்பு 43A பொருத்தம் 2 ஆகும்."
    )

    # -------------------------------------------------------------------------
    # Q24 (Correct: D) - Constitutional Development ↔ Year
    # -------------------------------------------------------------------------
    add_q(
        24,
        "Match List I (Constitutional Amendments on DPSP) with List II (Enactment Years) and select the correct code:",
        "பட்டியல் I-ஐ (DPSP மீதான அரசியலமைப்பு திருத்தங்கள்) பட்டியல் II உடன் (இயற்றப்பட்ட ஆண்டுகள்) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "Insertion of Article 31C (25th CAA)", "உறுப்பு 31C இணைப்பு (25வது திருத்தம்)", "Insertion of Article 38(2) (44th CAA)", "உறுப்பு 38(2) இணைப்பு (44வது திருத்தம்)", "Modification of Article 45 (86th CAA)", "உறுப்பு 45 திருத்தம் (86வது திருத்தம்)", "Insertion of Article 43B (97th CAA)", "உறுப்பு 43B இணைப்பு (97வது திருத்தம்)",
        "2011", "2011",
        "1978", "1978",
        "2002", "2002",
        "1971", "1971",
        "A-1, B-2, C-3, D-4", "A-2, B-1, C-4, D-3", "A-4, B-1, C-2, D-3", "A-4, B-2, C-3, D-1",
        "D",
        "A-4: Art 31C (25th CAA) = 1971. B-2: Art 38(2) (44th CAA) = 1978. C-3: Art 45 (86th CAA) = 2002. D-1: Art 43B (97th CAA) = 2011.",
        "A-4: உறுப்பு 31C (25வது திருத்தம்) = 1971. B-2: உறுப்பு 38(2) (44வது திருத்தம்) = 1978. C-3: உறுப்பு 45 (86வது திருத்தம்) = 2002. D-1: உறுப்பு 43B (97வது திருத்தம்) = 2011.",
        "DPSP Amendment Years: 25th CAA (1971), 42nd CAA (1976), 44th CAA (1978), 86th CAA (2002), 97th CAA (2011).", "DPSP திருத்த ஆண்டுகள்: 25வது (1971), 42வது (1976), 44வது (1978), 86வது (2002), 97வது (2011).",
        "Incorrect. 25th CAA matches 4, not 1.", "தவறு. 25வது திருத்தம் பொருத்தம் 4 ஆகும்.",
        "Incorrect. 44th CAA matches 2, not 1.", "தவறு. 44வது திருத்தம் பொருத்தம் 2 ஆகும்.",
        "Incorrect. 86th CAA matches 3, not 2.", "தவறு. 86வது திருத்தம் பொருத்தம் 3 ஆகும்.",
        "Correct. A-4, B-2, C-3, D-1 is the exact match.", "சரி. A-4, B-2, C-3, D-1 சரியான பொருத்தம்."
    )

    # -------------------------------------------------------------------------
    # Q25 (Correct: D) - Article ↔ Fundamental Duty Counterpart
    # -------------------------------------------------------------------------
    add_q(
        25,
        "Match List I (State Directives in Part IV) with List II (Corresponding Fundamental Duties in Part IV-A) and select the correct code:",
        "பட்டியல் I-ஐ (பகுதி IV-ல் உள்ள அரசு வழிகாட்டல்கள்) பட்டியல் II உடன் (பகுதி IV-A-ல் உள்ள இணையான அடிப்படைக் கடமைகள்) பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
        "Article 48A (Environment DPSP)", "உறுப்பு 48A (சுற்றுச்சூழல் DPSP)", "Article 49 (Monuments DPSP)", "உறுப்பு 49 (நினைவிடங்கள் DPSP)", "Article 51 (International Peace DPSP)", "உறுப்பு 51 (சர்வதேச அமைதி DPSP)", "Article 45 (Childcare DPSP)", "உறுப்பு 45 (குழந்தைகள் DPSP)",
        "Article 51A(k) (Parent duty for education)", "உறுப்பு 51A(k) (பெற்றோர் கல்விக் கடமை)",
        "Article 51A(g) (Citizen duty for environment)", "உறுப்பு 51A(g) (குடிமகன் சுற்றுச்சூழல் கடமை)",
        "Article 51A(f) (Value rich heritage of culture)", "உறுப்பு 51A(f) (பண்பாட்டின் வளமான பாரம்பரியத்தைப் போற்றுதல்)",
        "Article 51A(c) (Uphold sovereignty, unity & integrity)", "உறுப்பு 51A(c) (இறையாண்மை, ஒற்றுமையைப் பேணுதல்)",
        "A-1, B-2, C-3, D-4", "A-2, B-1, C-4, D-3", "A-3, B-4, C-1, D-2", "A-2, B-3, C-4, D-1",
        "D",
        "A-2: Art 48A (Environment DPSP) = Art 51A(g) (Environment FD). B-3: Art 49 (Monuments DPSP) = Art 51A(f) (Heritage FD). C-4: Art 51 (International Peace DPSP) = Art 51A(c) (Sovereignty/Unity FD). D-1: Art 45 (Childcare DPSP) = Art 51A(k) (Parent Education FD).",
        "A-2: உறுப்பு 48A (சுற்றுச்சூழல் DPSP) = உறுப்பு 51A(g) (சுற்றுச்சூழல் FD). B-3: உறுப்பு 49 (நினைவிடங்கள் DPSP) = உறுப்பு 51A(f) (பாரம்பரிய FD). C-4: உறுப்பு 51 (சர்வதேச அமைதி DPSP) = உறுப்பு 51A(c) (இறையாண்மை FD). D-1: உறுப்பு 45 (குழந்தைகள் DPSP) = உறுப்பு 51A(k) (பெற்றோர் கல்விக் கடமை FD).",
        "Part IV (State Directives) and Part IV-A (Citizen Duties) harmoniously reinforce constitutional goals.", "பகுதி IV (அரசு வழிகாட்டல்கள்) மற்றும் பகுதி IV-A (குடிமகன் கடமைகள்) இணக்கமாக அரசியலமைப்பு இலக்குகளை வலுப்படுத்துகின்றன.",
        "Incorrect. Article 48A matches 2, not 1.", "தவறு. உறுப்பு 48A பொருத்தம் 2 ஆகும்.",
        "Incorrect. Article 49 matches 3, not 1.", "தவறு. உறுப்பு 49 பொருத்தம் 3 ஆகும்.",
        "Incorrect. Article 51 matches 4, not 1.", "தவறு. உறுப்பு 51 பொருத்தம் 4 ஆகும்.",
        "Correct. A-2, B-3, C-4, D-1 is the exact match.", "சரி. A-2, B-3, C-4, D-1 சரியான பொருத்தம்."
    )

    output_dir = "data/questions/polity"
    os.makedirs(output_dir, exist_ok=True)
    
    # Save to both file names so question_loader finds it under both names
    output_path1 = os.path.join(output_dir, "directive_principles_match.json")
    output_path2 = os.path.join(output_dir, "directive_principles_match_the_following.json")

    with open(output_path1, "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)

    with open(output_path2, "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)

    print(f"Successfully generated {len(questions)} DPSP Match MCQs at {output_path1} and {output_path2}")

    counts = {"A": 0, "B": 0, "C": 0, "D": 0}
    for q in questions:
        counts[q["correct_answer"]] += 1
    print(f"Answer Key Distribution: A={counts['A']}, B={counts['B']}, C={counts['C']}, D={counts['D']}")

if __name__ == "__main__":
    generate_25_match_mcqs()
