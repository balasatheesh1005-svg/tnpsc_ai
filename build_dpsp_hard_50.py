# build_dpsp_hard_50.py
# Generates 50 Hard MCQs for Directive Principles of State Policy (DPSP)
# Target file: data/questions/polity/directive_principles_hard.json

import json
import os

def generate_50_hard_mcqs():
    questions = []

    def add_q(q_id, q_type, q_en, q_ta, opt_a_en, opt_a_ta, opt_b_en, opt_b_ta, opt_c_en, opt_c_ta, opt_d_en, opt_d_ta, correct, exp_en, exp_ta, tip_en, tip_ta, w_a_en, w_a_ta, w_b_en, w_b_ta, w_c_en, w_c_ta, w_d_en, w_d_ta):
        q_obj = {
            "id": f"DPSP_H_{q_id:03d}",
            "subject": "Polity",
            "topic": "Directive Principles of State Policy",
            "difficulty": "Hard",
            "question_type": q_type,
            "question": {
                "en": q_en,
                "ta": q_ta
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
                "A": {"en": w_a_en, "ta": w_a_ta},
                "B": {"en": w_b_en, "ta": w_b_ta},
                "C": {"en": w_c_en, "ta": w_c_ta},
                "D": {"en": w_d_en, "ta": w_d_ta}
            },
            "tnpsc_tip": {
                "en": tip_en,
                "ta": tip_ta
            }
        }
        questions.append(q_obj)

    # -------------------------------------------------------------------------
    # Q1 (Correct: A) - Multi-statement / Case-law
    # -------------------------------------------------------------------------
    add_q(
        1, "Multi-statement",
        "Consider the following statements regarding Article 31C and its constitutional interaction with DPSP Articles 39(b) and 39(c):\n1. Article 31C was inserted by the 25th Constitutional Amendment Act, 1971.\n2. Laws enacted to give effect to Article 39(b) and 39(c) cannot be declared void on the ground that they violate Article 14 or Article 19.\n3. In Minerva Mills (1980), the Supreme Court upheld the extension of Article 31C protection to ALL Directive Principles in Part IV.\nWhich of the statements given above is/are CORRECT?",
        "உறுப்பு 31C மற்றும் DPSP உறுப்புகள் 39(b), 39(c) ஆகியவற்றுக்கு இடையேயான அரசியலமைப்புத் தொடர்பு பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. உறுப்பு 31C 1971-ன் 25வது அரசியலமைப்பு திருத்தச் சட்டத்தால் இணைக்கப்பட்டது.\n2. உறுப்பு 39(b) மற்றும் 39(c)-ஐ செயல்படுத்த இயற்றப்படும் சட்டங்கள் உறுப்பு 14 அல்லது உறுப்பு 19-ஐ மீறுகின்றன என்ற அடிப்படையில் செல்லாததாக அறிவிக்கப்பட முடியாது.\n3. மினர்வா மில்ஸ் வழக்கில் (1980), பகுதி IV-ல் உள்ள அனைத்து வழிகாட்டு நெறிமுறைகளுக்கும் உறுப்பு 31C பாதுகாப்பை நீட்டிப்பதை உச்ச நீதிமன்றம் உறுதி செய்தது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
        "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
        "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
        "1 and 3 only", "1 மற்றும் 3 மட்டுமே",
        "1, 2 and 3", "1, 2 மற்றும் 3",
        "A",
        "Statements 1 and 2 are correct. Statement 3 is INCORRECT because in Minerva Mills (1980), the Supreme Court STRUCK DOWN the 42nd Amendment's extension of Article 31C protection to all DPSPs, restoring protection ONLY to Articles 39(b) and 39(c).",
        "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் மினர்வா மில்ஸ் வழக்கில் (1980), அனைத்து DPSP-களுக்கும் உறுப்பு 31C பாதுகாப்பை நீட்டித்த 42வது திருத்தத்தை உச்ச நீதிமன்றம் ரத்து செய்து, உறுப்புகள் 39(b) மற்றும் 39(c)-க்கு மட்டுமே பாதுகாப்பை மீண்டும் கொண்டு வந்தது.",
        "Statement 3 trap: Minerva Mills struck down all-DPSP extension of 31C; it did not uphold it.",
        "கூற்று 3 பொறி: மினர்வா மில்ஸ் 31C-ன் அனைத்து DPSP நீட்டிப்பையும் ரத்து செய்தது; அதை உறுதி செய்யவில்லை.",
        "Correct. Statements 1 and 2 are correct; Statement 3 is false.", "சரி. கூற்றுகள் 1 மற்றும் 2 சரியானவை; கூற்று 3 தவறானது.",
        "Statement 3 is incorrect because Minerva Mills invalidated all-DPSP 31C extension.", "மினர்வா மில்ஸ் அனைத்து DPSP 31C நீட்டிப்பையும் செல்லாததாக்கியதால் கூற்று 3 தவறானது.",
        "Statement 3 is incorrect.", "கூற்று 3 தவறானது.",
        "Statement 3 is incorrect.", "கூற்று 3 தவறானது."
    )

    # -------------------------------------------------------------------------
    # Q2 (Correct: B) - Case-law
    # -------------------------------------------------------------------------
    add_q(
        2, "Case-law",
        "Match the landmark Supreme Court cases with their specific holdings on the Fundamental Rights vs DPSP relationship:\n1. Champakam Dorairajan (1951) – A. Balance between Part III and Part IV is a Basic Feature\n2. Re Kerala Education Bill (1958) – B. FRs are superior; DPSPs must run as subsidiary\n3. Minerva Mills (1980) – C. Doctrine of Harmonious Construction\nWhich of the following is the correct matching code?",
        "அடிப்படை உரிமைகள் vs DPSP தொடர்பு குறித்த முக்கிய உச்ச நீதிமன்ற வழக்குகளை వాటి குறிப்பிட்ட தீர்ப்புகளுடன் பொருத்துக:\n1. செண்பகம் துரைராஜன் (1951) – A. பகுதி III மற்றும் பகுதி IV இடையிலான சமநிலையே அடிப்படை அம்சம்\n2. கேரளா கல்வி மசோதா (1958) – B. FR-கள் மேலானவை; DPSP-கள் துணையாகவே செயல்பட வேண்டும்\n3. மினர்வா மில்ஸ் (1980) – C. இணக்கமான விளக்கக் கோட்பாடு\nபின்வருவனவற்றுள் எது சரியான பொருத்தக் குறியீடு?",
        "1-A, 2-B, 3-C", "1-A, 2-B, 3-C",
        "1-B, 2-C, 3-A", "1-B, 2-C, 3-A",
        "1-C, 2-A, 3-B", "1-C, 2-A, 3-B",
        "1-B, 2-A, 3-C", "1-B, 2-A, 3-C",
        "B",
        "1. Champakam Dorairajan (1951) held FRs are superior and DPSP runs as subsidiary to Part III (1-B); 2. Re Kerala Education Bill (1958) introduced Doctrine of Harmonious Construction (2-C); 3. Minerva Mills (1980) held balance between Part III & IV is Basic Feature (3-A).",
        "1. செண்பகம் துரைராஜன் (1951) FR-கள் மேலானவை மற்றும் DPSP பகுதி III-க்கு துணையாகவே செயல்படும் என்றது (1-B); 2. கேரளா கல்வி மசோதா (1958) இணக்கமான விளக்கக் கோட்பாட்டை அறிமுகப்படுத்தியது (2-C); 3. மினர்வா மில்ஸ் (1980) பகுதி III & IV இடையிலான சமநிலையே அடிப்படை அம்சம் என்றது (3-A).",
        "Matching code logic: 1->B, 2->C, 3->A.", "பொருத்தக் குறியீட்டு தர்க்கம்: 1->B, 2->C, 3->A.",
        "Incorrect matching.", "தவறான பொருத்தம்.",
        "Correct. 1-B, 2-C, 3-A is the exact match.", "சரி. 1-B, 2-C, 3-A சரியான பொருத்தம்.",
        "Incorrect matching.", "தவறான பொருத்தம்.",
        "Incorrect matching.", "தவறான பொருத்தம்."
    )

    # -------------------------------------------------------------------------
    # Q3 (Correct: C) - Assertion & Reason
    # -------------------------------------------------------------------------
    add_q(
        3, "Assertion-Reason",
        "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Parliament cannot repeal Part IV (Directive Principles) entirely using its constituent amending power under Article 368.\nReason (R): The harmony and balance between Fundamental Rights (Part III) and Directive Principles (Part IV) is an essential element of the Basic Structure of the Constitution.\nSelect the correct answer using the code below:",
        "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிக்கப்பட்டுள்ளன:\nகூற்று (A): உறுப்பு 368-ன் கீழ் உள்ள தனது அரசியலமைப்புத் திருத்தும் அதிகாரத்தைப் பயன்படுத்தி நாடாளுமன்றம் பகுதி IV-ஐ (வழிகாட்டு நெறிமுறைகள்) முழுமையாக ரத்து செய்ய முடியாது.\nகாரணம் (R): அடிப்படை உரிமைகள் (பகுதி III) மற்றும் வழிகாட்டு நெறிமுறைகள் (பகுதி IV) இடையிலான இணக்கமும் சமநிலையும் அரசியலமைப்பின் அடிப்படை அமைப்பின் அத்தியாவசிய அம்சமாகும்.\nகீழேயுள்ள குறியீட்டைப் பயன்படுத்தி சரியான பதிலைத் தேர்ந்தெடுக்கவும்:",
        "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி, ஆனால் காரணம் (R) கூற்று (A)-விற்கு சரியான விளக்கமல்ல",
        "(A) is true, but (R) is false", "கூற்று (A) சரி, ஆனால் காரணம் (R) தவறு",
        "Both (A) and (R) are true, and (R) is the correct explanation of (A)", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி, மேலும் காரணம் (R) கூற்று (A)-விற்கு சரியான விளக்கமாகும்",
        "(A) is false, but (R) is true", "கூற்று (A) தவறு, ஆனால் காரணம் (R) சரி",
        "C",
        "Both (A) and (R) are true, and (R) correctly explains (A). As held in Minerva Mills (1980), the harmony and balance between Part III and Part IV is a Basic Feature of the Constitution. Therefore, any amendment repealing Part IV completely would destroy this balance and violate the Basic Structure Doctrine.",
        "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி, மேலும் காரணம் (R) கூற்று (A)-விற்கு சரியான விளக்கமாகும். மினர்வா மில்ஸ் வழக்கில் (1980) கூறப்பட்டது போல, பகுதி III மற்றும் பகுதி IV இடையிலான இணக்கமும் சமநிலையும் அரசியலமைப்பின் அடிப்படை அம்சமாகும். எனவே பகுதி IV-ஐ முழுமையாக ரத்து செய்யும் எந்தவொரு திருத்தமும் இந்தச் சமநிலையைச் சிதைத்து அடிப்படை அமைப்புக் கோட்பாட்டை மீறும்.",
        "Basic Structure limits Parliament's amending power under Article 368.", "அடிப்படை அமைப்பு உறுப்பு 368-ன் கீழ் நாடாளுமன்றத்தின் திருத்தும் அதிகாரத்தைக் கட்டுப்படுத்துகிறது.",
        "Reason (R) is the exact direct explanation of Assertion (A).", "காரணம் (R) கூற்று (A)-ன் நேரடி சரியான விளக்கமாகும்.",
        "Reason (R) is true.", "காரணம் (R) சரியானது.",
        "Correct. Both (A) and (R) are true, and (R) is the correct explanation of (A).", "சரி. கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி, மேலும் காரணம் (R) கூற்று (A)-விற்கு சரியான விளக்கமாகும்.",
        "Assertion (A) is true.", "கூற்று (A) சரியானது."
    )

    # -------------------------------------------------------------------------
    # Q4 (Correct: D) - Constitutional Application
    # -------------------------------------------------------------------------
    add_q(
        4, "Application",
        "A State Legislature enacts a law nationalizing private bus routes to provide affordable public transport. Private operators challenge the Act claiming it violates their freedom of trade under Article 19(1)(g) and right to equality under Article 14. Which constitutional provision protects the State law if it effectively implements Article 39(b)?",
        "மலிவு விலையில் பொதுப் போக்குவரத்தை வழங்க ஒரு மாநில சட்டமன்றம் தனியார் பேருந்து பாதைகளைத் தேசியமயமாக்கும் ஒரு சட்டத்தை இயற்றுகிறது. தனியார் இயக்ககங்கள் இச்சட்டம் உறுப்பு 19(1)(g)-ன் கீழ் தங்களது வர்த்தக சுதந்திரத்தையும் உறுப்பு 14-ன் கீழ் சமத்துவ உரிமையையும் மீறுகிறது எனச் சவால் செய்கின்றன. இச்சட்டம் உறுப்பு 39(b)-ஐ திறம்படச் செயல்படுத்தினால் எந்த அரசியலமைப்பு விதி இம்மாநிலச் சட்டத்தைப் பாதுகாக்கிறது?",
        "Article 32", "உறுப்பு 32",
        "Article 36", "உறுப்பு 36",
        "Article 37", "உறுப்பு 37",
        "Article 31C", "உறுப்பு 31C",
        "D",
        "Under Article 31C (upheld in Kesavananda Bharati & Abu Kavur Bai 1984), no law giving effect to the policy of the State towards securing the principles in Article 39(b) or 39(c) shall be deemed to be void on the ground that it takes away or abridges rights conferred by Article 14 or Article 19.",
        "உறுப்பு 31C-ன் கீழ் (கேசவானந்த பாரதி & அபு கவூர் பாய் 1984 வழக்குகளில் உறுதி செய்யப்பட்டது), உறுப்பு 39(b) அல்லது 39(c)-ல் உள்ள கோட்பாடுகளைச் செயல்படுத்த இயற்றப்படும் எந்தவொரு சட்டமும் உறுப்பு 14 அல்லது உறுப்பு 19 வழங்கிய உரிமைகளைப் பறிக்கிறது என்ற அடிப்படையில் செல்லாததாகக் கருதப்படக் கூடாது.",
        "In State of TN v. L. Abu Kavur Bai (1984), SC specifically applied Article 31C to uphold Tamil Nadu bus nationalization law under Article 39(b).", "தமிழ்நாடு அரசு எதிர் எல். அபு கவூர் பாய் வழக்கில் (1984), உறுப்பு 39(b)-ன் கீழ் தமிழ்நாடு பேருந்து தேசியமயமாக்கல் சட்டத்தை உறுதி செய்ய SC உறுப்பு 31C-ஐப் பயன்படுத்தியது.",
        "Article 32 is writ remedy for FR violation.", "உறுப்பு 32 FR மீறலுக்கான பேராணை பரிகாரம்.",
        "Article 36 defines State for Part IV.", "உறுப்பு 36 பகுதி IV-க்கான அரசை வரையறுக்கிறது.",
        "Article 37 makes DPSP non-justiciable.", "உறுப்பு 37 DPSP-ஐ அமல்படுத்த முடியாததாக்குகிறது.",
        "Correct. Article 31C protects laws implementing Article 39(b) against Articles 14 and 19 challenges.", "சரி. உறுப்பு 31C உறுப்பு 39(b)-ஐ செயல்படுத்தும் சட்டங்களை உறுப்புகள் 14 மற்றும் 19 சவால்களிலிருந்து பாதுகாக்கிறது."
    )

    # -------------------------------------------------------------------------
    # Q5 (Correct: A) - Multi-statement
    # -------------------------------------------------------------------------
    add_q(
        5, "Multi-statement",
        "Consider the following statements regarding Article 40 and Panchayati Raj:\n1. Article 40 was part of the original 1950 Constitution text under Part IV DPSPs.\n2. Article 40 embodied Mahatma Gandhi's philosophy of Gram Swaraj and decentralization.\n3. The 73rd Constitutional Amendment Act 1992 deleted Article 40 and replaced it with Part IX.\nWhich of the statements given above is/are CORRECT?",
        "உறுப்பு 40 மற்றும் பஞ்சாயத்து ராஜ் பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. உறுப்பு 40 பகுதி IV DPSP-ன் கீழ் அசல் 1950 அரசியலமைப்பு உரையின் பகுதியாக இருந்தது.\n2. உறுப்பு 40 மகாத்மா காந்தியின் கிராம சுயராஜ்யம் மற்றும் அதிகாரப் பரவலாக்கல் தத்துவத்தை வெளிப்படுத்தியது.\n3. 1992-ன் 73வது அரசியலமைப்பு திருத்தச் சட்டம் உறுப்பு 40-ஐ நீக்கிவிட்டு அதற்குப் பதிலாக பகுதி IX-ஐக் கொண்டு வந்தது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
        "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
        "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
        "1 and 3 only", "1 மற்றும் 3 மட்டுமே",
        "1, 2 and 3", "1, 2 மற்றும் 3",
        "A",
        "Statements 1 and 2 are correct. Statement 3 is INCORRECT because the 73rd Amendment Act 1992 DID NOT delete Article 40; Article 40 remains active in Part IV as the DPSP policy directive, while Part IX (Arts 243-243O) was inserted as the mandatory statutory constitutional framework.",
        "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் 1992-ன் 73வது திருத்தச் சட்டம் உறுப்பு 40-ஐ நீக்கவில்லை; உறுப்பு 40 பகுதி IV-ல் DPSP கொள்கை வழிகாட்டலாகத் தொடர்ந்து செயல்படுகிறது, அதே நேரத்தில் பகுதி IX (உறுப்புகள் 243-243O) கட்டாயச் சட்டக் கட்டமைப்பாக இணைக்கப்பட்டது.",
        "TNPSC Trap: Amendments ADD new parts/schedules without deleting original DPSP policy directives unless expressly substituted.",
        "டிஎன்பிஎஸ்சி பொறி: வெளிப்படையாக மாற்றப்படாவிட்டால் அசல் DPSP வழிகாட்டலை நீக்காமல் திருத்தங்கள் புதிய பகுதிகள்/அட்டவணைகளைச் சேர்க்கின்றன.",
        "Correct. Statements 1 and 2 are correct; Statement 3 is false.", "சரி. கூற்றுகள் 1 மற்றும் 2 சரியானவை; கூற்று 3 தவறானது.",
        "Statement 3 is incorrect because Article 40 was not deleted.", "உறுப்பு 40 நீக்கப்படாததால் கூற்று 3 தவறானது.",
        "Statement 3 is incorrect.", "கூற்று 3 தவறானது.",
        "Statement 3 is incorrect.", "கூற்று 3 தவறானது."
    )

    # -------------------------------------------------------------------------
    # Q6 (Correct: B) - Advanced Conceptual
    # -------------------------------------------------------------------------
    add_q(
        6, "Conceptual",
        "Why is the conventional classification of Directive Principles into Socialist, Gandhian, and Liberal categories considered an ACADEMIC division rather than a constitutional one?",
        "வழிகாட்டு நெறிமுறைகளை சமதர்ம, காந்திய மற்றும் தாராளமயப் பிரிவுகளாகப் பிரிக்கும் மரபுவழி வகைப்பாடு அரசியலமைப்பு அடிப்படையிலானது அல்லாமல் ஏன் ஒரு கல்விப் பிரிவாகக் (Academic division) கருதப்படுகிறது?",
        "Because the classification was created by the British House of Commons in 1947", "ஏனெனில் இந்த வகைப்பாடு 1947-ல் பிரிட்டிஷ் கீழ்மன்றத்தால் உருவாக்கப்பட்டது",
        "Because the Constitution text in Part IV contains no sub-headings or formal ideological categories, and principles were arranged pragmatically by the Constituent Assembly", "ஏனெனில் பகுதி IV-ல் உள்ள அரசியலமைப்பு உரை எந்தவொரு துணைத் தலைப்புகளையோ அல்லது முறையான தத்துவார்த்தப் பிரிவுகளையோ கொண்டிருக்கவில்லை, மேலும் கோட்பாடுகள் அரசியலமைப்பு நிர்ணய சபையால் நடைமுறைச் சாத்தியமாக வரிசைப்படுத்தப்பட்டன",
        "Because Supreme Court judgments have declared all classifications illegal under Article 14", "ஏனெனில் உச்ச நீதிமன்றத் தீர்ப்புகள் அனைத்து வகைப்பாடுகளையும் உறுப்பு 14-ன் கீழ் சட்டவிரோதமானவை என அறிவித்துள்ளன",
        "Because the classification applies only to regional state laws, not central Acts", "ஏனெனில் இந்த வகைப்பாடு மாநிலச் சட்டங்களுக்கு மட்டுமே பொருந்தும், மத்தியச் சட்டங்களுக்கு அல்ல",
        "B",
        "The text of Part IV (Articles 36 to 51) contains a continuous running list of articles without any sub-headings, chapters, or ideological labels. Constitutional scholars (such as M.P. Jain, D.D. Basu, Granville Austin) conventionally classify them based on their content and ideological direction for academic study.",
        "பகுதி IV உரை (உறுப்புகள் 36 முதல் 51) எந்தவொரு துணைத் தலைப்புகள், அத்தியாயங்கள் அல்லது தத்துவார்த்த முத்திரைகள் இல்லாமல் தொடர்ச்சியான உறுப்புகளின் பட்டியலைக் கொண்டுள்ளது. அரசியலமைப்பு அறிஞர்கள் (எம்.பி. ஜெயின், டி.டி. பாசு, கிரான்வில் ஆஸ்டின் போன்றோர்) கல்விப் படிப்பிற்காக அவற்றின் உள்ளடக்கம் மற்றும் தத்துவார்த்த திசையின் அடிப்படையில் மரபுவழியாக வகைப்படுத்துகின்றனர்.",
        "Always remember: Classification is a study aid, not statutory text.", "எப்போதும் நினைவில் கொள்க: வகைப்பாடு என்பது படிப்பிற்கான உதவியே தவிர, சட்டப்பூர்வ உரையல்ல.",
        "British House of Commons had no role in framing Part IV.", "பகுதி IV-ஐ வரைவதில் பிரிட்டிஷ் கீழ்மன்றத்திற்கு எந்தப் பங்கும் இல்லை.",
        "Correct. Part IV contains no sub-headings or formal ideological labels in its text.", "சரி. பகுதி IV தன் உரையில் எந்தவொரு துணைத் தலைப்புகளையோ அல்லது தத்துவார்த்த முத்திரைகளையோ கொண்டிருக்கவில்லை.",
        "Supreme Court uses conventional classifications in its judgments.", "உச்ச நீதிமன்றம் தனது தீர்ப்புகளில் மரபுவழி வகைப்பாடுகளைப் பயன்படுத்துகிறது.",
        "Classification applies conceptually across all DPSP directives.", "வகைப்பாடு அனைத்து DPSP வழிகாட்டல்களுக்கும் தத்துவார்த்தமாகப் பொருந்தும்."
    )

    # -------------------------------------------------------------------------
    # Q7 (Correct: C) - Multi-statement / Case-law
    # -------------------------------------------------------------------------
    add_q(
        7, "Multi-statement",
        "Consider the following statements regarding Article 48 and cow slaughter prohibition laws in India:\n1. Article 48 directs the State to take steps for preserving and improving cattle breeds and prohibiting cow slaughter.\n2. In Hanif Quareshi (1958), SC held a total ban on slaughter of ALL cattle (including old and unserviceable) was invalid.\n3. In Mirzapur Moti Kureshi (2005), a 7-judge Bench overruled earlier stance and UPHELD total prohibition of cow progeny slaughter based on ecological and organic dung value in rural economy.\nWhich of the statements given above is/are CORRECT?",
        "இந்தியாவில் உறுப்பு 48 மற்றும் பசு வதை தடைச் சட்டங்கள் பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. உறுப்பு 48 கால்நடை இனங்களைப் பாதுகாப்பதற்கும் மேம்படுத்துவதற்கும் பசு வதைத் தடுப்பதற்கும் நடவடிக்கைகள் எடுக்க அரசுக்கு வழிகாட்டுகிறது.\n2. ஹனிஃப் குரேஷி வழக்கில் (1958), அனைத்துக் கால்நடைகளையும் (வயதானவை உட்பட) முழுமையாக வதை செய்ய தடை விதிப்பது செல்லாது என SC தீர்ப்பளித்தது.\n3. மிர்சாபூர் மோதி குரேஷி வழக்கில் (2005), 7-நீதிபதிகள் அமர்வு முந்தைய நிலையை மாற்றி, கிராமப் பொருளாதாரத்தில் இயற்கை எரு உரத்தின் மதிப்பின் அடிப்படையில் பசு சந்ததிகள் வதை மீதான முழுத் தடையை உறுதி செய்தது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
        "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
        "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
        "1, 2 and 3", "1, 2 மற்றும் 3",
        "1 and 3 only", "1 மற்றும் 3 மட்டுமே",
        "C",
        "All three statements are CORRECT. Article 48 contains the directive (1). In 1958 (Hanif Quareshi), SC allowed slaughter of unserviceable cattle (2). In 2005 (Mirzapur Kureshi 7-judge bench), SC overruled 1958 stance and held total ban on cow progeny slaughter is a valid reasonable restriction under Art 19(6) implementing Art 48 due to dung, urine, bio-energy, and organic farming value (3).",
        "மூன்று கூற்றுகளும் சரியானவை. உறுப்பு 48 வழிகாட்டலைக் கொண்டுள்ளது (1). 1958-ல் (ஹனிஃப் குரேஷி), பயன்பாடற்ற கால்நடைகளை வதை செய்ய SC அனுமதித்தது (2). 2005-ல் (மிர்சாபூர் குரேஷி 7-நீதிபதிகள் அமர்வு), SC 1958 நிலையை மாற்றி, இயற்கை எரு உரம் மற்றும் உயிரி-ஆற்றல் மதிப்பின் அடிப்படையில் பசு சந்ததிகள் வதை மீதான முழுத் தடை உறுப்பு 19(6)-ன் கீழ் செல்லுபடியாகும் நியாயமான கட்டுப்பாடு எனத் தீர்ப்பளித்தது (3).",
        "Judicial Shift: 1958 allowed unserviceable cattle slaughter -> 2005 upheld total prohibition based on organic dung/bio-mass value.",
        "நீதித்துறை மாற்றம்: 1958 பயன்பாடற்ற கால்நடை வதையை அனுமதித்தது -> 2005 இயற்கை எரு உர மதிப்பின் அடிப்படையில் முழுத் தடையை உறுதி செய்தது.",
        "Statement 3 is also correct, making 1, 2 and 3 correct.", "கூற்று 3-ம் சரியானதால், 1, 2 மற்றும் 3 சரியானவை ஆகும்.",
        "Statement 1 is also correct.", "கூற்று 1-ம் சரியானதாகும்.",
        "Correct. Statements 1, 2 and 3 are all correct.", "சரி. கூற்றுகள் 1, 2 மற்றும் 3 அனைத்தும் சரியானவை.",
        "Statement 2 is also correct.", "கூற்று 2-ம் சரியானதாகும்."
    )

    # -------------------------------------------------------------------------
    # Q8 (Correct: D) - Amendment / Consequence
    # -------------------------------------------------------------------------
    add_q(
        8, "Amendment/Case",
        "Analyze the exact age demarcation established by the 86th Constitutional Amendment Act, 2002 across the three parts of the Constitution:",
        "அரசியலமைப்பின் மூன்று பகுதிகளில் 2002-ன் 86வது அரசியலமைப்பு திருத்தச் சட்டத்தால் நிறுவப்பட்ட குறிப்பிட்ட வயது வரம்பைப் பகுப்பாய்வு செய்க:",
        "Part III Art 21A: 0-6 yrs; Part IV Art 45: 6-14 yrs; Part IV-A Art 51A(k): 14-18 yrs", "பகுதி III உறுப்பு 21A: 0-6 ஆண்டுகள்; பகுதி IV உறுப்பு 45: 6-14 ஆண்டுகள்; பகுதி IV-A உறுப்பு 51A(k): 14-18 ஆண்டுகள்",
        "Part III Art 21A: 6-18 yrs; Part IV Art 45: 0-14 yrs; Part IV-A Art 51A(k): 0-6 yrs", "பகுதி III உறுப்பு 21A: 6-18 ஆண்டுகள்; பகுதி IV உறுப்பு 45: 0-14 ஆண்டுகள்; பகுதி IV-A உறுப்பு 51A(k): 0-6 ஆண்டுகள்",
        "Part III Art 21A: 0-14 yrs; Part IV Art 45: 14-18 yrs; Part IV-A Art 51A(k): 6-14 yrs", "பகுதி III உறுப்பு 21A: 0-14 ஆண்டுகள்; பகுதி IV உறுப்பு 45: 14-18 ஆண்டுகள்; பகுதி IV-A உறுப்பு 51A(k): 6-14 ஆண்டுகள்",
        "Part III Art 21A: 6 to 14 yrs (FR); Part IV Art 45: Below 6 yrs (0-6 yrs DPSP); Part IV-A Art 51A(k): 6 to 14 yrs (Parent Duty)", "பகுதி III உறுப்பு 21A: 6 முதல் 14 ஆண்டுகள் (FR); பகுதி IV உறுப்பு 45: 6 வயதுக்குட்பட்டோர் (0-6 ஆண்டுகள் DPSP); பகுதி IV-A உறுப்பு 51A(k): 6 முதல் 14 ஆண்டுகள் (பெற்றோர் கடமை)",
        "D",
        "The 86th Amendment 2002 created a clear age boundary: 1) Part III Article 21A (FR): Free & compulsory education for children aged 6 to 14 years; 2) Part IV Article 45 (DPSP): Early childhood care & education for children BELOW 6 years (0 to 6 years); 3) Part IV-A Article 51A(k) (FD): Duty of parent/guardian to provide education for child aged 6 to 14 years.",
        "86வது திருத்தம் 2002 ஒரு தெளிவான வயது வரம்பை உருவாக்கியது: 1) பகுதி III உறுப்பு 21A (FR): 6 முதல் 14 வயது வரையிலான குழந்தைகளுக்கு இலவச & கட்டாயக் கல்வி; 2) பகுதி IV உறுப்பு 45 (DPSP): 6 வயதுக்குட்பட்ட (0 முதல் 6 ஆண்டுகள்) குழந்தைகளுக்கான முன்பருவக் பராமரிப்பு & கல்வி; 3) பகுதி IV-A உறுப்பு 51A(k) (FD): 6 முதல் 14 வயது வரையிலான குழந்தைக்குக் கல்வி வழங்கும் பெற்றோர் கடமை.",
        "Age Boundary Rule: Below 6 = Art 45 DPSP; 6 to 14 = Art 21A FR & Art 51A(k) FD.",
        "வயது வரம்பு விதி: 6-க்கு கீழ் = உறுப்பு 45 DPSP; 6 முதல் 14 = உறுப்பு 21A FR & உறுப்பு 51A(k) FD.",
        "Incorrect age demarcations.", "தவறான வயது வரம்புகள்.",
        "Incorrect age demarcations.", "தவறான வயது வரம்புகள்.",
        "Incorrect age demarcations.", "தவறான வயது வரம்புகள்.",
        "Correct. Art 21A (6-14 FR), Art 45 (below 6 DPSP), Art 51A(k) (6-14 FD).", "சரி. உறுப்பு 21A (6-14 FR), உறுப்பு 45 (6-க்கு கீழ் DPSP), உறுப்பு 51A(k) (6-14 FD)."
    )

    # -------------------------------------------------------------------------
    # Q9 (Correct: A) - High-level Trap
    # -------------------------------------------------------------------------
    add_q(
        9, "TNPSC Trap",
        "A public interest litigation (PIL) is filed in a High Court under Article 226 seeking a direction to the State Government to immediately enforce Article 47 by imposing complete liquor prohibition across the State. How will the High Court treat this prayer?",
        "மாநிலம் முழுவதும் முழுமையான மதுவிலக்கை அமல்படுத்தி உறுப்பு 47-ஐ உடனடியாகச் செயல்படுத்துமாறு மாநில அரசுக்கு உத்தரவிடக் கோரி உறுப்பு 226-ன் கீழ் ஒரு பொதுநல வழக்கு (PIL) உயர் நீதிமன்றத்தில் தாக்கல் செய்யப்படுகிறது. உயர் நீதிமன்றம் இந்தப் பிரார்த்தனையை எவ்வாறு கையாளும்?",
        "High Court will refuse to issue Mandamus because prohibition policy under Article 47 is a non-justiciable DPSP within legislative and executive policy discretion under Article 37", "உறுப்பு 47-ன் கீழ் மதுவிலக்குக் கொள்கை என்பது உறுப்பு 37-ன் கீழ் சட்டமன்ற மற்றும் நிர்வாகக் கொள்கை விருப்பத்திற்கு உட்பட்ட அமல்படுத்த முடியாத DPSP என்பதால் உயர் நீதிமன்றம் செயலுறுத்தும் பேராணையைப் பிறப்பிக்க மறுக்கும்",
        "High Court will automatically grant Mandamus and close all liquor shops within 24 hours", "உயர் நீதிமன்றம் செயலுறுத்தும் பேராணையைத் தானாகவே வழங்கி 24 மணி நேரத்திற்குள் அனைத்து மதுபானக் கடைகளையும் மூடும்",
        "High Court will declare Article 47 to be a Fundamental Right under Article 21", "உயர் நீதிமன்றம் உறுப்பு 47-ஐ உறுப்பு 21-ன் கீழ் உள்ள அடிப்படை உரிமையாக அறிவிக்கும்",
        "High Court will transfer the State police force to the direct command of the High Court Registrar", "உயர் நீதிமன்றம் மாநிலக் காவல் படையை உயர் நீதிமன்றப் பதிவாளரின் நேரடிக் கட்டுப்பாட்டிற்கு மாற்றும்",
        "A",
        "The High Court cannot issue a Writ of Mandamus to direct the Executive or Legislature to enforce DPSP Article 47 prohibition because DPSPs under Article 37 are non-justiciable. Prohibition policy involves economic revenue, social factors, and legislative discretion.",
        "உறுப்பு 37-ன் கீழ் DPSP-கள் அமல்படுத்த முடியாதவை என்பதால் DPSP உறுப்பு 47 மதுவிலக்கை அமல்படுத்துமாறு நிர்வாகத்திற்கோ சட்டமன்றத்திற்கோ உயர் நீதிமன்றம் செயலுறுத்தும் பேராணையைப் பிறப்பிக்க முடியாது. மதுவிலக்குக் கொள்கை பொருளாதார வருவாய், சமூகக் காரணிகள் மற்றும் சட்டமன்ற விவேகம் ஆகியவற்றை உள்ளடக்கியது.",
        "TNPSC Trap: Courts can enforce statutory prohibition Acts, but CANNOT compel enactment of prohibition policy via writs.",
        "டிஎன்பிஎஸ்சி பொறி: நீதிமன்றங்கள் சட்டப்பூர்வ மதுவிலக்குச் சட்டங்களை அமல்படுத்தலாம், ஆனால் பேராணைகள் மூலம் மதுவிலக்குக் கொள்கையை இயற்றுமாறு கட்டாயப்படுத்த முடியாது.",
        "Correct. Courts cannot issue Mandamus to enforce DPSP Article 47 policy.", "சரி. DPSP உறுப்பு 47 கொள்கையை அமல்படுத்த நீதிமன்றங்கள் செயலுறுத்தும் பேராணையைப் பிறப்பிக்க முடியாது.",
        "Court cannot issue Mandamus for policy formulation.", "கொள்கை உருவாக்கத்திற்கு நீதிமன்றம் செயலுறுத்தும் பேராணையைப் பிறப்பிக்க முடியாது.",
        "Article 47 is a Part IV DPSP, not a Part III Fundamental Right.", "உறுப்பு 47 பகுதி IV DPSP, பகுதி III அடிப்படை உரிமை அல்ல.",
        "Court cannot assume executive command of police.", "நீதிமன்றம் காவல்துறையின் நிர்வாகக் கட்டுப்பாட்டை ஏற்க முடியாது."
    )

    # -------------------------------------------------------------------------
    # Q10 (Correct: B) - Case-law
    # -------------------------------------------------------------------------
    add_q(
        10, "Case-law",
        "In Randhir Singh v. Union of India (1982), how did the Supreme Court resolve the relationship between Article 39(d) (Equal Pay for Equal Work) and Part III Fundamental Rights?",
        "ரந்தீர் சிங் வழக்கில் (1982), உறுப்பு 39(d) (சம வேலைக்கு சம ஊதியம்) மற்றும் பகுதி III அடிப்படை உரிமைகளுக்கு இடையிலான தொடர்பை உச்ச நீதிமன்றம் எவ்வாறு தீர்த்தது?",
        "SC held that Equal Pay for Equal Work is a private contract term with no constitutional relevance", "சம வேலைக்கு சம ஊதியம் என்பது அரசியலமைப்புத் தொடர்பற்ற ஒரு தனியார் ஒப்பந்த நிபந்தனை என SC தீர்ப்பளித்தது",
        "SC held that Article 39(d) read together with Articles 14 and 16 is a constitutional goal enforceable in public services against arbitrary discrimination", "உறுப்பு 39(d) உறுப்புகள் 14 மற்றும் 16-உடன் சேர்த்து வாசிக்கப்படும் போது தன்னிச்சையான பாகுபாட்டிற்கு எதிராகப் பொதுப்பணியில் அமல்படுத்தக்கூடிய அரசியலமைப்பு இலக்காகும் என SC தீர்ப்பளித்தது",
        "SC held that Article 39(d) overrides all tax laws passed by Parliament", "உறுப்பு 39(d) நாடாளுமன்றத்தால் இயற்றப்பட்ட அனைத்து வரிச் சட்டங்களையும் மிஞ்சுகிறது என SC தீர்ப்பளித்தது",
        "SC held that Equal Pay for Equal Work applies only to Supreme Court judges", "சம வேலைக்கு சம ஊதியம் உச்ச நீதிமன்ற நீதிபதிகளுக்கு மட்டுமே பொருந்தும் என SC தீர்ப்பளித்தது",
        "B",
        "In Randhir Singh (1982), Justice Chinnappa Reddy held that while 'Equal Pay for Equal Work' is a DPSP under Article 39(d), it is not a mere abstract slogan. When read alongside Articles 14 (Equality) and 16 (Equal Opportunity), unequal pay for equal work performing identical duties in public service violates Article 14.",
        "ரந்தீர் சிங் வழக்கில் (1982), நீதிபதி சின்னப்ப ரெட்டி 'சம வேலைக்கு சம ஊதியம்' என்பது உறுப்பு 39(d)-ன் கீழ் உள்ள DPSP என்றாலும், அது வெறும் கற்பனை முழக்கம் அல்ல எனத் தீர்ப்பளித்தார். உறுப்புகள் 14 (சமத்துவம்) மற்றும் 16 (சம வாய்ப்பு) ஆகியவற்றுடன் சேர்த்து வாசிக்கப்படும் போது, பொதுப்பணியில் ஒரே மாதிரியான வேலைகளைச் செய்யும் போது சமமற்ற ஊதியம் வழங்குவது உறுப்பு 14-ஐ மீறுகிறது.",
        "Statutory Support: Equal Remuneration Act 1976 statutorily supports Article 39(d).", "சட்டப்பூர்வ ஆதரவு: சம ஊதியச் சட்டம் 1976 உறுப்பு 39(d)-க்கு ஆதரவளிக்கிறது.",
        "It is a constitutional goal enforceable in public service.", "இது பொதுப்பணியில் அமல்படுத்தக்கூடிய அரசியலமைப்பு இலக்காகும்.",
        "Correct. SC enforced Art 39(d) by reading it in light of Articles 14 and 16.", "சரி. உறுப்புகள் 14 மற்றும் 16-ன் வெளிச்சத்தில் வாசிப்பதன் மூலம் SC உறுப்பு 39(d)-ஐ அமல்படுத்தியது.",
        "It does not deal with tax laws.", "இது வரிச் சட்டங்களைப் பற்றியது அல்ல.",
        "It applies across all public service employment.", "இது அனைத்துப் பொதுப்பணி வேலைவாய்ப்புகளுக்கும் பொருந்தும்."
    )

    # -------------------------------------------------------------------------
    # Q11 (Correct: C) - Multi-statement
    # -------------------------------------------------------------------------
    add_q(
        11, "Multi-statement",
        "Consider the following statements regarding environmental protection under the Constitution of India:\n1. Article 48A directs the STATE to endeavor to protect and improve the environment and safeguard forests and wildlife.\n2. Article 51A(g) imposes a FUNDAMENTAL DUTY on every citizen to protect and improve the natural environment.\n3. Both Article 48A and Article 51A(g) were inserted by the 42nd Constitutional Amendment Act, 1976.\nWhich of the statements given above is/are CORRECT?",
        "இந்திய அரசியலமைப்பின் கீழ் சுற்றுச்சூழல் பாதுகாப்பு பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. உறுப்பு 48A சுற்றுச்சூழலைப் பாதுகாக்கவும் மேம்படுத்தவும் காடுகள் மற்றும் வனவிலங்குகளைப் பாதுகாக்கவும் அரசுக்கு வழிகாட்டுகிறது.\n2. உறுப்பு 51A(g) இயற்கைச் சுற்றுச்சூழலைப் பாதுகாக்கவும் மேம்படுத்தவும் ஒவ்வொரு குடிமகனுக்கும் ஓர் அடிப்படைக் கடமையை விதிக்கிறது.\n3. உறுப்பு 48A மற்றும் உறுப்பு 51A(g) ஆகிய இரண்டும் 1976-ன் 42வது அரசியலமைப்பு திருத்தச் சட்டத்தால் இணைக்கப்பட்டன.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
        "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
        "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
        "1, 2 and 3", "1, 2 மற்றும் 3",
        "1 and 3 only", "1 மற்றும் 3 மட்டுமே",
        "C",
        "All three statements are CORRECT. Article 48A (Part IV State DPSP) and Article 51A(g) (Part IV-A Citizen FD) were both added by the 42nd Constitutional Amendment Act, 1976 during Emergency.",
        "மூன்று கூற்றுகளும் சரியானவை. உறுப்பு 48A (பகுதி IV அரசு DPSP) மற்றும் உறுப்பு 51A(g) (பகுதி IV-A குடிமகன் FD) ஆகிய இரண்டும் அவசரநிலையின் போது 1976-ன் 42வது அரசியலமைப்பு திருத்தச் சட்டத்தால் சேர்க்கப்பட்டன.",
        "Judicial Integration: SC reads 48A + 51A(g) together into Article 21 to enforce Right to Clean Environment.", "நீதித்துறை ஒருங்கிணைப்பு: தூய்மையான சுற்றுச்சூழல் உரிமையை அமல்படுத்த SC 48A + 51A(g) ஆகியவற்றை உறுப்பு 21-க்குள் சேர்த்து வாசிக்கிறது.",
        "Statement 3 is also correct, making 1, 2 and 3 correct.", "கூற்று 3-ம் சரியானதால், 1, 2 மற்றும் 3 சரியானவை ஆகும்.",
        "Statement 1 is also correct.", "கூற்று 1-ம் சரியானதாகும்.",
        "Correct. Statements 1, 2 and 3 are all correct.", "சரி. கூற்றுகள் 1, 2 மற்றும் 3 அனைத்தும் சரியானவை.",
        "Statement 2 is also correct.", "கூற்று 2-ம் சரியானதாகும்."
    )

    # -------------------------------------------------------------------------
    # Q12 (Correct: D) - Assertion & Reason
    # -------------------------------------------------------------------------
    add_q(
        12, "Assertion-Reason",
        "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Article 50 directs the State to take steps to separate the judiciary from the executive in the public services.\nReason (R): The Constitution of India adopts an absolute, rigid doctrine of Separation of Powers modeled strictly on the US Constitution.\nSelect the correct answer using the code below:",
        "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிக்கப்பட்டுள்ளன:\nகூற்று (A): உறுப்பு 50 பொது சேவைகளில் நிர்வாகத்திலிருந்து நீதித்துறையைப் பிரிக்க நடவடிக்கைகள் எடுக்க அரசுக்கு வழிகாட்டுகிறது.\nகாரணம் (R): இந்திய அரசியலமைப்பு அமெரிக்க அரசியலமைப்பை அப்படியே மாதிரியாகக் கொண்டு கடுமையான, முற்றுமுழுதான அதிகாரப் பிரிப்புக் கோட்பாட்டை ஏற்கிறது.\nகீழேயுள்ள குறியீட்டைப் பயன்படுத்தி சரியான பதிலைத் தேர்ந்தெடுக்கவும்:",
        "Both (A) and (R) are true, and (R) is the correct explanation of (A)", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி, மேலும் காரணம் (R) கூற்று (A)-விற்கு சரியான விளக்கமாகும்",
        "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி, ஆனால் காரணம் (R) கூற்று (A)-விற்கு சரியான விளக்கமல்ல",
        "Both (A) and (R) are false", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் தவறு",
        "(A) is true, but (R) is false", "கூற்று (A) சரி, ஆனால் காரணம் (R) தவறு",
        "D",
        "Assertion (A) is TRUE: Article 50 directs separation of judiciary from executive in public services (statutorily executed via CrPC 1973). Reason (R) is FALSE: India DOES NOT follow a rigid separation of powers like the US; India follows a Parliamentary system with executive-legislature overlap and checks and balances.",
        "கூற்று (A) சரி: உறுப்பு 50 பொது சேவைகளில் நிர்வாகத்திலிருந்து நீதித்துறையைப் பிரிக்க வழிகாட்டுகிறது (CrPC 1973 மூலம் நிறைவேற்றப்பட்டது). காரணம் (R) தவறு: இந்தியா அமெரிக்காவைப் போல கடுமையான அதிகாரப் பிரிவைப் பின்பற்றவில்லை; இந்தியா நிர்வாகம்-சட்டமன்றக் கலப்பு மற்றும் கட்டுப்பாடுகள் மற்றும் சமநிலைகளுடன் கூடிய நாடாளுமன்ற முறையைப் பின்பற்றுகிறது.",
        "TNPSC Trap: India follows checks and balances in a Parliamentary democracy, NOT rigid US presidential separation of powers.",
        "டிஎன்பிஎஸ்சி பொறி: இந்தியா நாடாளுமன்ற ஜனநாயகத்தில் கட்டுப்பாடுகள் மற்றும் சமநிலைகளைப் பின்பற்றுகிறது, கடுமையான அமெரிக்க அதிபர் அதிகாரப் பிரிவை அல்ல.",
        "Reason (R) is false.", "காரணம் (R) தவறானது.",
        "Reason (R) is false.", "காரணம் (R) தவறானது.",
        "Assertion (A) is true.", "கூற்று (A) சரியானது.",
        "Correct. Assertion (A) is true, but Reason (R) is false.", "சரி. கூற்று (A) சரி, ஆனால் காரணம் (R) தவறு."
    )

    # -------------------------------------------------------------------------
    # Q13 (Correct: A) - Constitutional Application
    # -------------------------------------------------------------------------
    add_q(
        13, "Application",
        "How did the Supreme Court synthesize Article 39A (Free Legal Aid DPSP) with Article 21 (Right to Life) in national jurisprudence?",
        "தேசிய சட்டவியலில் உச்ச நீதிமன்றம் எவ்வாறு உறுப்பு 39A-ஐ (இலவச சட்ட உதவி DPSP) உறுப்பு 21-உடன் (வாழ்வு உரிமை) இணைத்தது?",
        "By ruling in Hussainara Khatoon (1979) that procedure depriving personal liberty under Article 21 is not 'fair, just and reasonable' unless free legal aid is provided to indigent accused, prompting enactment of Legal Services Authorities Act 1987 (NALSA)", "ஏழை குற்றஞ்சாட்டப்பட்டவருக்கு இலவச சட்ட உதவி வழங்கப்படாவிட்டால் உறுப்பு 21-ன் கீழ் தனிநபர் சுதந்திரத்தைப் பறிக்கும் நடைமுறை 'நேர்மையானது' அல்ல என ஹுசைனாரா கதூன் (1979) வழக்கில் தீர்ப்பளித்து, 1987 சட்டப் பணிகள் ஆணைக்குழுக்கள் சட்டம் (NALSA) இயற்றப்படத் தூண்டியதன் மூலம்",
        "By making free legal aid mandatory only for civil land property disputes", "இலவச சட்ட உதவியைச் சிவில் நிலச் சொத்துத் தகராறுகளுக்கு மட்டுமே கட்டாயமாக்குவதன் மூலம்",
        "By holding that private lawyers must work without any fees in all cases", "தனியார் வழக்கறிஞர்கள் அனைத்து வழக்குகளிலும் எந்தக் கட்டணமும் இன்றிப் பணியாற்ற வேண்டும் எனப் பிடிப்பதன் மூலம்",
        "By transferring legal aid administration to municipal corporations", "சட்ட உதவி நிர்வாகத்தை நகராட்சிகளுக்கு மாற்றுவதன் மூலம்",
        "A",
        "In Hussainara Khatoon (1979) and Suk Das (1986), the SC held that Free Legal Aid under Article 39A is an essential fundamental procedural right under Article 21. State has a constitutional mandate to provide free legal services to indigent undertrials and accused.",
        "ஹுசைனாரா கதூன் (1979) மற்றும் சுக் தாஸ் (1986) வழக்குகளில், உறுப்பு 39A-ன் கீழ் இலவச சட்ட உதவி என்பது உறுப்பு 21-ன் கீழ் ஓர் அத்தியாவசிய அடிப்படை நடைமுறை உரிமை என SC தீர்ப்பளித்தது. ஏழை விசாரணைக் கைதிகள் மற்றும் குற்றஞ்சாட்டப்பட்டவர்களுக்கு இலவச சட்ட சேவைகளை வழங்க அரசுக்கு அரசியலமைப்பு கட்டளை உள்ளது.",
        "Statutory Execution: NALSA (1987) establishes Lok Adalats and Free Legal Services Committees nationwide.", "சட்டப்பூர்வ நிறைவேற்றம்: NALSA (1987) நாடு தழுவிய லோக் அதாலத்கள் மற்றும் இலவச சட்ட சேவை குழுக்களை நிறுவுகிறது.",
        "Correct. SC synthesized Art 39A into Art 21 to create enforceable free legal aid, leading to NALSA 1987.", "சரி. அமல்படுத்தக்கூடிய இலவச சட்ட உதவியை உருவாக்க SC உறுப்பு 39A-ஐ உறுப்பு 21-க்குள் இணைத்தது, இது NALSA 1987-க்கு வழிவகுத்தது.",
        "Free legal aid applies primarily to criminal cases threatening liberty.", "இலவச சட்ட உதவி முதன்மையாகச் சுதந்திரத்திற்கு அச்சுறுத்தல் விளைவிக்கும் குற்றவியல் வழக்குகளுக்குப் பொருந்தும்.",
        "State funds legal aid through panel lawyers, not uncompensated forced labor.", "அரசு குழு வழக்கறிஞர்கள் மூலம் நிதியளிக்கிறது, ஊதியமற்ற கட்டாய வேலையால் அல்ல.",
        "Legal aid is administered by Legal Services Authorities (NALSA/SALSA/DALSA).", "சட்ட உதவி சட்டப் பணிகள் ஆணைக்குழுக்களால் நிர்வகிக்கப்படுகிறது."
    )

    # -------------------------------------------------------------------------
    # Q14 (Correct: B) - Multi-statement
    # -------------------------------------------------------------------------
    add_q(
        14, "Multi-statement",
        "Consider the following statements regarding Article 38 of the Constitution:\n1. Article 38(1) directs the State to promote the welfare of the people by securing a social order informed by social, economic, and political justice.\n2. Article 38(2) directs the State to strive to minimise inequalities in income, status, facilities, and opportunities.\n3. Article 38(2) was part of the original 1950 Constitution text.\nWhich of the statements given above is/are CORRECT?",
        "அரசியலமைப்பின் உறுப்பு 38 பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. உறுப்பு 38(1) சமூக, பொருளாதார மற்றும் அரசியல் நீதி நிறைந்த சமூக ஒழுங்கை உருவாக்கி மக்கள் நலனை மேம்படுத்த அரசுக்கு வழிகாட்டுகிறது.\n2. உறுப்பு 38(2) வருமானம், அந்தஸ்து, வசதிகள் மற்றும் வாய்ப்புகளில் உள்ள சமத்துவமின்மையைக் குறைக்க அரசு முயல வேண்டும் என வழிகாட்டுகிறது.\n3. உறுப்பு 38(2) அசல் 1950 அரசியலமைப்பு உரையின் பகுதியாக இருந்தது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
        "1 only", "1 மட்டுமே",
        "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
        "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
        "1, 2 and 3", "1, 2 மற்றும் 3",
        "B",
        "Statements 1 and 2 are correct. Statement 3 is INCORRECT because Article 38(2) WAS NOT in the original 1950 text; it was inserted by the 44th Constitutional Amendment Act, 1978.",
        "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் உறுப்பு 38(2) அசல் 1950 உரையில் இல்லை; இது 1978-ன் 44வது அரசியலமைப்பு திருத்தச் சட்டத்தால் இணைக்கப்பட்டது.",
        "Remember: 44th CAA 1978 inserted Article 38(2).", "நினைவில் கொள்க: 44வது திருத்தம் 1978 உறுப்பு 38(2)-ஐ இணைத்தது.",
        "Statement 2 is also correct.", "கூற்று 2-ம் சரியானதாகும்.",
        "Correct. Statements 1 and 2 are correct; Statement 3 is false.", "சரி. கூற்றுகள் 1 மற்றும் 2 சரியானவை; கூற்று 3 தவறானது.",
        "Statement 3 is incorrect.", "கூற்று 3 தவறானது.",
        "Statement 3 is incorrect.", "கூற்று 3 தவறானது."
    )

    # -------------------------------------------------------------------------
    # Q15 (Correct: C) - Advanced Conceptual
    # -------------------------------------------------------------------------
    add_q(
        15, "Conceptual",
        "Which of the following correctly positions the three wage concepts in ascending order of economic protection under labor jurisprudence and Article 43?",
        "தொழிலாளர் சட்டவியல் மற்றும் உறுப்பு 43-ன் கீழ் பொருளாதாரப் பாதுகாப்பின் ஏறுவரிசையில் மூன்று ஊதியக் கருத்துக்களையும் சரியாக அமைக்கும் வரிசை எது?",
        "Living Wage < Fair Wage < Minimum Wage", "வாழ்வாதார ஊதியம் < நியாயமான ஊதியம் < குறைந்தபட்ச ஊதியம்",
        "Fair Wage < Living Wage < Minimum Wage", "நியாயமான ஊதியம் < வாழ்வாதார ஊதியம் < குறைந்தபட்ச ஊதியம்",
        "Minimum Wage < Fair Wage < Living Wage", "குறைந்தபட்ச ஊதியம் < நியாயமான ஊதியம் < வாழ்வாதார ஊதியம்",
        "Living Wage < Minimum Wage < Fair Wage", "வாழ்வாதார ஊதியம் < குறைந்தபட்ச ஊதியம் < நியாயமான ஊதியம்",
        "C",
        "In labor jurisprudence (Express Newspapers case & Reserve Bank of India case), the SC laid down the 3-tier wage hierarchy: 1) Minimum Wage (lowest - bare physical survival under Minimum Wages Act 1948); 2) Fair Wage (middle - above minimum wage, dependent on industry capacity to pay); 3) Living Wage (highest - Article 43 goal, covering decent standard of life, education, health & leisure).",
        "தொழிலாளர் சட்டவியலில் (எக்ஸ்பிரஸ் நியூஸ்பேப்பர்ஸ் வழக்கு & ரிசர்வ் வங்கி வழக்கு), SC 3-அடுக்கு ஊதிய படிநிலையை அமைத்தது: 1) குறைந்தபட்ச ஊதியம் (குறைந்தது - 1948 சட்டத்தின் கீழ் வெறும் உடல் வாழ்வாதாரம்); 2) நியாயமான ஊதியம் (நடுத்தரம் - குறைந்தபட்ச ஊதியத்திற்கு மேல், தொழில்துறை திறன் சார்ந்தது); 3) வாழ்வாதார ஊதியம் (மிக உயர்ந்தது - உறுப்பு 43 இலக்கு, கண்ணியமான வாழ்க்கை, கல்வி, சுகாதாரம் & ஓய்வை உள்ளடக்கியது).",
        "Ascending Order: Minimum Wage -> Fair Wage -> Living Wage.", "ஏறுவரிசை: குறைந்தபட்ச ஊதியம் -> நியாயமான ஊதியம் -> வாழ்வாதார ஊதியம்.",
        "Living Wage is the highest, not lowest.", "வாழ்வாதார ஊதியம் மிக உயர்ந்தது, குறைந்தபட்சம் அல்ல.",
        "Minimum Wage is the lowest base.", "குறைந்தபட்ச ஊதியம் மிகக் குறைந்த அடித்தளம்.",
        "Correct. Minimum Wage (survival) < Fair Wage (capacity) < Living Wage (full decent life Art 43).", "சரி. குறைந்தபட்ச ஊதியம் < நியாயமான ஊதியம் < வாழ்வாதார ஊதியம் (உறுப்பு 43).",
        "Fair Wage is middle level.", "நியாயமான ஊதியம் நடுத்தர நிலை."
    )

    # -------------------------------------------------------------------------
    # Q16 (Correct: D) - Case-based
    # -------------------------------------------------------------------------
    add_q(
        16, "Amendment/Case",
        "In State of Bombay v. F.N. Balsara (1951), on what constitutional ground did the Supreme Court uphold state liquor prohibition laws implementing Article 47?",
        "பம்பாய் மாநிலம் எதிர் F.N. பால்சரா வழக்கில் (1951), உறுப்பு 47-ஐ செயல்படுத்தும் மாநில மதுவிலக்குச் சட்டங்களை உச்ச நீதிமன்றம் எந்த அரசியலமைப்பு அடிப்படையில் உறுதி செய்தது?",
        "SC held that liquor prohibition is mandatory only for central government servants", "மதுவிலக்கு மத்திய அரசு ஊழியர்களுக்கு மட்டுமே கட்டாயமானது என SC கூறியது",
        "SC held that Article 47 overrides Article 368 amending power", "உறுப்பு 47 உறுப்பு 368 திருத்தும் அதிகாரத்தை மிஞ்சுகிறது என SC கூறியது",
        "SC held that state governments can confiscate property without compensation under Article 47", "மாநில அரசுகள் உறுப்பு 47-ன் கீழ் நஷ்டஈடு இன்றிச் சொத்துக்களைப் பறிமுதல் செய்யலாம் என SC கூறியது",
        "SC held that restrictions on trade in intoxicating liquor under Article 47 are 'Reasonable Restrictions' under Article 19(6) in public interest, as there is no fundamental right to trade in liquor", "மதுபான வியாபாரம் செய்ய அடிப்படை உரிமை எதுவும் இல்லை என்பதால், உறுப்பு 47-ன் கீழ் போதைப் பான வியாபாரத்தின் மீதான கட்டுப்பாடுகள் பொது நலன் கருதி உறுப்பு 19(6)-ன் கீழ் 'நியாயமான கட்டுப்பாடுகள்' ஆகும் என SC தீர்ப்பளித்தது",
        "D",
        "In F.N. Balsara (1951), the SC held that state laws restricting or prohibiting trade in intoxicating liquor to implement Article 47 are reasonable restrictions under Article 19(6). Later cases affirmed liquor trade is res extra commercium (outside constitutional trade protection).",
        "F.N. பால்சரா வழக்கில் (1951), உறுப்பு 47-ஐ செயல்படுத்த போதைப் பான வியாபாரத்தைக் கட்டுப்படுத்தும் அல்லது தடை செய்யும் மாநிலச் சட்டங்கள் உறுப்பு 19(6)-ன் கீழ் நியாயமான கட்டுப்பாடுகள் ஆகும் என SC தீர்ப்பளித்தது. பின்னர் வழக்குகள் மதுபான வியாபாரம் வணிகத்திற்கு அப்பாற்பட்டது என உறுதிப்படுத்தின.",
        "TNPSC Takeaway: State liquor prohibition laws implementing Art 47 do not violate Art 19(1)(g).", "டிஎன்பிஎஸ்சி தகவல்: உறுப்பு 47-ஐ செயல்படுத்தும் மாநில மதுவிலக்குச் சட்டங்கள் உறுப்பு 19(1)(g)-ஐ மீறுவதில்லை.",
        "Prohibition laws apply statewide to all individuals.", "மதுவிலக்குச் சட்டங்கள் மாநிலம் முழுவதும் உள்ள அனைத்துத் தனிநபர்களுக்கும் பொருந்தும்.",
        "Article 47 does not override Article 368.", "உறுப்பு 47 உறுப்பு 368-ஐ மிஞ்சாது.",
        "Property acquisition requires authority of law under Article 300A.", "சொத்து கையகப்படுத்தலுக்கு உறுப்பு 300A-ன் கீழ் சட்ட அதிகாரம் தேவை.",
        "Correct. SC held liquor trade restrictions under Art 47 are Reasonable Restrictions under Art 19(6).", "சரி. உறுப்பு 47-ன் கீழ் மது வியாபாரக் கட்டுப்பாடுகள் உறுப்பு 19(6)-ன் கீழ் நியாயமான கட்டுப்பாடுகள் என SC தீர்ப்பளித்தது."
    )

    # -------------------------------------------------------------------------
    # Q17 (Correct: A) - Multi-statement
    # -------------------------------------------------------------------------
    add_q(
        17, "Multi-statement",
        "Consider the following statements regarding the 42nd Constitutional Amendment Act, 1976:\n1. It added Article 39A to secure equal justice and free legal aid to the poor.\n2. It added Article 43A to secure workers' participation in management of industries.\n3. It added Article 48A to protect and improve the environment, forests, and wildlife.\nWhich of the statements given above is/are CORRECT?",
        "1976-ன் 42வது அரசியலமைப்பு திருத்தச் சட்டம் பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. இது ஏழைகளுக்குச் சம நீதியும் இலவச சட்ட உதவியும் வழங்க உறுப்பு 39A-ஐச் சேர்த்தது.\n2. இது தொழிற்சாலைகள் மேலாண்மையில் தொழிலாளர்களின் பங்கேற்பை உறுதி செய்ய உறுப்பு 43A-ஐச் சேர்த்தது.\n3. இது சுற்றுச்சூழல், காடுகள் மற்றும் வனவிலங்குகளைப் பாதுகாக்க உறுப்பு 48A-ஐச் சேர்த்தது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
        "1, 2 and 3", "1, 2 மற்றும் 3",
        "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
        "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
        "1 and 3 only", "1 மற்றும் 3 மட்டுமே",
        "A",
        "All three statements are CORRECT. The 42nd Amendment Act 1976 added 4 new DPSPs: 1) Article 39(f) (child development); 2) Article 39A (free legal aid); 3) Article 43A (workers' participation in management); 4) Article 48A (environment protection).",
        "மூன்று கூற்றுகளும் சரியானவை. 1976-ன் 42வது திருத்தச் சட்டம் 4 புதிய DPSP-களைச் சேர்த்தது: 1) உறுப்பு 39(f) (குழந்தை வளர்ச்சி); 2) உறுப்பு 39A (இலவச சட்ட உதவி); 3) உறுப்பு 43A (மேலாண்மையில் தொழிலாளர் பங்கேற்பு); 4) உறுப்பு 48A (சுற்றுச்சூழல் பாதுகாப்பு).",
        "All 4 DPSPs added by 42nd CAA are high-yield TNPSC exam questions.", "42வது திருத்தத்தால் சேர்க்கப்பட்ட 4 DPSP-களும் முக்கிய டிஎன்பிஎஸ்சி வினாக்கள் ஆகும்.",
        "Correct. Statements 1, 2 and 3 are all correct.", "சரி. கூற்றுகள் 1, 2 மற்றும் 3 அனைத்தும் சரியானவை.",
        "Statement 3 is also correct.", "கூற்று 3-ம் சரியானதாகும்.",
        "Statement 1 is also correct.", "கூற்று 1-ம் சரியானதாகும்.",
        "Statement 2 is also correct.", "கூற்று 2-ம் சரியானதாகும்."
    )

    # -------------------------------------------------------------------------
    # Q18 (Correct: B) - Constitutional Application
    # -------------------------------------------------------------------------
    add_q(
        18, "Application",
        "In Jolly George Varghese v. Bank of Cochin (1980), how did Justice V.R. Krishna Iyer interpret the legal effect of Article 51 (International Peace & Treaty respect) on domestic Indian law?",
        "ஜாலி ஜார்ஜ் வர்கீஸ் வழக்கில் (1980), நீதிபதி வி.ஆர். கிருஷ்ணய்யர் உள்நாட்டு இந்தியச் சட்டத்தின் மீது உறுப்பு 51-ன் (சர்வதேச அமைதி & ஒப்பந்த மரிப்பு) சட்டப்பூர்வ விளைவை எவ்வாறு விளக்கினார்?",
        "He held that international treaties automatically overwrite Parliament Acts without legislation", "பன்னாட்டு ஒப்பந்தங்கள் சட்டமியற்றப்படாமல் நாடாளுமன்றச் சட்டங்களைத் தானாகவே மாற்றியமைக்கும் என அவர் தீர்ப்பளித்தார்",
        "He held that international conventions (like ICCPR) inform constitutional interpretation under Article 21, but until Parliament passes implementing legislation under Article 253, an international treaty does not automatically alter domestic statutory rights", "சர்வதேச ஒப்பந்தங்கள் (ICCPR போன்றவை) உறுப்பு 21-ன் கீழ் அரசியலமைப்பு விளக்கத்திற்கு வழிகாட்டுகின்றன, ஆனால் உறுப்பு 253-ன் கீழ் நாடாளுமன்றம் செயலாக்கச் சட்டத்தை இயற்றும் வரை பன்னாட்டு ஒப்பந்தம் தானாகவே உள்நாட்டுச் சட்ட உரிமைகளை மாற்றாது என அவர் தீர்ப்பளித்தார்",
        "He held that Article 51 applies only to international sea boundary disputes", "உறுப்பு 51 சர்வதேச கடல் எல்லைத் தகராறுகளுக்கு மட்டுமே பொருந்தும் என அவர் தீர்ப்பளித்தார்",
        "He held that international treaties are illegal under Article 13", "பன்னாட்டு ஒப்பந்தங்கள் உறுப்பு 13-ன் கீழ் சட்டவிரோதமானவை என அவர் தீர்ப்பளித்தார்",
        "B",
        "In Jolly George Varghese (1980), SC held that India follows a Dualist model. Article 51 directs the State to foster respect for international law, and courts will interpret domestic law harmoniously with international human rights covenants (like ICCPR Art 11 on civil imprisonment for debt), but a treaty requires Parliamentary legislation under Article 253 to be directly enforceable in domestic courts.",
        "ஜாலி ஜார்ஜ் வர்கீஸ் வழக்கில் (1980), இந்தியா ஒரு இருத்துவ மாதிரியைப் பின்பற்றுகிறது என SC தீர்ப்பளித்தது. உறுப்பு 51 சர்வதேச சட்டத்திற்கான மரியாதையை வளர்க்க அரசுக்கு வழிகாட்டுகிறது, ஆனால் ஒரு ஒப்பந்தம் உள்நாட்டு நீதிமன்றங்களில் நேரடியாக அமல்படுத்தப்பட உறுப்பு 253-ன் கீழ் நாடாளுமன்றச் சட்டம் தேவைப்படுகிறது.",
        "Dualist Principle: International law guides constitutional interpretation, but requires statutory enactment under Art 253 for domestic enforcement.",
        "இருத்துவக் கோட்பாடு: சர்வதேச சட்டம் அரசியலமைப்பு விளக்கத்திற்கு வழிகாட்டுகிறது, ஆனால் உள்நாட்டு அமலாக்கத்திற்கு உறுப்பு 253-ன் கீழ் சட்டம் தேவைப்படுகிறது.",
        "Treaties are not self-executing in Indian domestic courts.", "இந்திய உள்நாட்டு நீதிமன்றங்களில் ஒப்பந்தங்கள் தானாகவே செயல்படுபவை அல்ல.",
        "Correct. International treaties guide Art 21 interpretation, but require Art 253 legislation for domestic statutory enforceability.", "சரி. பன்னாட்டு ஒப்பந்தங்கள் உறுப்பு 21 விளக்கத்திற்கு வழிகாட்டுகின்றன, ஆனால் உள்நாட்டுச் சட்ட அமலாக்கத்திற்கு உறுப்பு 253 சட்டம் தேவைப்படுகிறது.",
        "Article 51 applies broadly to international peace, law, and arbitration.", "உறுப்பு 51 சர்வதேச அமைதி, சட்டம் மற்றும் நடுவர் மன்றத்திற்கு பரவலாகப் பொருந்தும்.",
        "International treaties are not illegal under Article 13.", "பன்னாட்டு ஒப்பந்தங்கள் உறுப்பு 13-ன் கீழ் சட்டவிரோதமானவை அல்ல."
    )

    # -------------------------------------------------------------------------
    # Q19 (Correct: C) - Assertion & Reason
    # -------------------------------------------------------------------------
    add_q(
        19, "Assertion-Reason",
        "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Article 41 (Right to Work, Education and Public Assistance) cannot be directly enforced by a citizen filing a writ petition under Article 32.\nReason (R): Article 41 is a Directive Principle under Part IV explicitly qualified by the limits of the State's economic capacity and development.\nSelect the correct answer using the code below:",
        "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிக்கப்பட்டுள்ளன:\nகூற்று (A): உறுப்பு 41-ஐ (வேலை, கல்வி மற்றும் பொது உதவி உரிமை) உறுப்பு 32-ன் கீழ் பேராணை மனு தாக்கல் செய்வதன் மூலம் ஒரு குடிமகன் நேரடியாக அமல்படுத்த முடியாது.\nகாரணம் (R): உறுப்பு 41 என்பது பகுதி IV-ன் கீழ் உள்ள ஒரு வழிகாட்டு நெறிமுறையாகும், இது அரசின் பொருளாதாரத் திறன் மற்றும் வளர்ச்சியின் வரம்புகளுக்கு வெளிப்படையாக உட்பட்டது.\nகீழேயுள்ள குறியீட்டைப் பயன்படுத்தி சரியான பதிலைத் தேர்ந்தெடுக்கவும்:",
        "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி, ஆனால் காரணம் (R) கூற்று (A)-விற்கு சரியான விளக்கமல்ல",
        "(A) is true, but (R) is false", "கூற்று (A) சரி, ஆனால் காரணம் (R) தவறு",
        "Both (A) and (R) are true, and (R) is the correct explanation of (A)", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி, மேலும் காரணம் (R) கூற்று (A)-விற்கு சரியான விளக்கமாகும்",
        "(A) is false, but (R) is true", "கூற்று (A) தவறு, ஆனால் காரணம் (R) சரி",
        "C",
        "Both (A) and (R) are true, and (R) correctly explains (A). Under Article 37, DPSPs are non-justiciable. Article 41 specifically conditions the realization of right to work and public assistance on the financial and economic capacity of the State. Therefore, citizens cannot demand writ enforcement under Article 32.",
        "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி, மேலும் காரணம் (R) கூற்று (A)-விற்கு சரியான விளக்கமாகும். உறுப்பு 37-ன் கீழ், DPSP-கள் அமல்படுத்த முடியாதவை. உறுப்பு 41 வேலை உரிமை மற்றும் பொது உதவியை நிறைவேற்றுவதைக் குறிக்கோளாகக் கொண்டு அரசின் நிதி மற்றும் பொருளாதாரத் திறனை நிபந்தனையாகக் விதிக்கிறது. எனவே, குடிமக்கள் உறுப்பு 32-ன் கீழ் பேராணை அமலாக்கத்தைக் கோர முடியாது.",
        "MGNREGA 2005 statutorily provides 100 days work to fulfill Article 41 within legislative discretion.", "MGNREGA 2005 சட்டமன்ற விவேகத்திற்குள் உறுப்பு 41-ஐ நிறைவேற்றச் சட்டப்பூர்வமாக 100 நாட்கள் வேலையை வழங்குகிறது.",
        "Reason (R) is the exact direct explanation of Assertion (A).", "காரணம் (R) கூற்று (A)-ன் நேரடி சரியான விளக்கமாகும்.",
        "Reason (R) is true.", "காரணம் (R) சரியானது.",
        "Correct. Both (A) and (R) are true, and (R) is the correct explanation of (A).", "சரி. கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி, மேலும் காரணம் (R) கூற்று (A)-விற்கு சரியான விளக்கமாகும்.",
        "Assertion (A) is true.", "கூற்று (A) சரியானது."
    )

    # -------------------------------------------------------------------------
    # Q20 (Correct: D) - Multi-statement
    # -------------------------------------------------------------------------
    add_q(
        20, "Multi-statement",
        "Consider the following statements regarding Article 46 (Upliftment of SCs, STs, and Weaker Sections):\n1. Article 46 directs the State to promote with special care the educational and economic interests of SCs, STs, and weaker sections.\n2. Article 46 is a justiciable Fundamental Right under Part III of the Constitution.\n3. Article 46 provides the DPSP policy foundation for affirmative action reservation laws under Articles 15 and 16.\nWhich of the statements given above is/are CORRECT?",
        "உறுப்பு 46 (எஸ்சி, எஸ்டி மற்றும் எளிய பிரிவினர் மேம்பாடு) பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. உறுப்பு 46 எஸ்சி, எஸ்டி மற்றும் எளிய பிரிவினரின் கல்வி மற்றும் பொருளாதார நலன்களை சிறப்பு கவனத்துடன் மேம்படுத்த அரசுக்கு வழிகாட்டுகிறது.\n2. உறுப்பு 46 என்பது அரசியலமைப்பின் பகுதி III-ன் கீழ் உள்ள ஓர் அமல்படுத்தக்கூடிய அடிப்படை உரிமையாகும்.\n3. உறுப்பு 46 உறுப்புகள் 15 மற்றும் 16-ன் கீழ் உள்ள இடஒதுக்கீட்டுச் சட்டங்களுக்கான DPSP கொள்கை அடித்தளத்தை வழங்குகிறது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
        "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
        "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
        "1, 2 and 3", "1, 2 மற்றும் 3",
        "1 and 3 only", "1 மற்றும் 3 மட்டுமே",
        "D",
        "Statements 1 and 3 are correct. Statement 2 is INCORRECT because Article 46 is a Directive Principle in Part IV, NOT a Fundamental Right in Part III.",
        "கூற்றுகள் 1 மற்றும் 3 சரியானவை. கூற்று 2 தவறானது, ஏனெனில் உறுப்பு 46 என்பது பகுதி IV-ல் உள்ள வழிகாட்டு நெறிமுறை, பகுதி III-ல் உள்ள அடிப்படை உரிமை அல்ல.",
        "TNPSC Trap: Article 46 is a Part IV DPSP guide; actual reservations are empowered under Part III Articles 15(4), 15(5), 16(4), 16(4A).", "டிஎன்பிஎஸ்சி பொறி: உறுப்பு 46 பகுதி IV DPSP வழிகாட்டி; அசல் இடஒதுக்கீடுகள் பகுதி III உறுப்புகள் 15(4), 15(5), 16(4), 16(4A)-ன் கீழ் அதிகாரமளிக்கப்படுகின்றன.",
        "Statement 2 is incorrect because Article 46 is in Part IV, not Part III.", "உறுப்பு 46 பகுதி IV-ல் உள்ளதால் கூற்று 2 தவறானது.",
        "Statement 2 is incorrect.", "கூற்று 2 தவறானது.",
        "Statement 2 is incorrect.", "கூற்று 2 தவறானது.",
        "Correct. Statements 1 and 3 are correct; Statement 2 is false.", "சரி. கூற்றுகள் 1 மற்றும் 3 சரியானவை; கூற்று 2 தவறானது."
    )

    # -------------------------------------------------------------------------
    # Q21 (Correct: A) - High-level Trap
    # -------------------------------------------------------------------------
    add_q(
        21, "TNPSC Trap",
        "A landlord challenges a State Land Ceiling Act enacted under Article 39(b) and 39(c) claiming it violates Article 14 (Equality) because small landholders are exempted. Will the Supreme Court entertain the Article 14 challenge?",
        "சிறிய நிலவுடமையாளர்களுக்கு விலக்கு அளிக்கப்பட்டதால் உறுப்பு 14 (சமத்துவம்) மீறப்படுவதாகக் கூறி உறுப்பு 39(b) மற்றும் 39(c)-ன் கீழ் இயற்றப்பட்ட ஒரு மாநில நில உச்சவரம்புச் சட்டத்தை ஒரு நிலப்பிரபு சவால் செய்கிறார். உச்ச நீதிமன்றம் இந்த உறுப்பு 14 சவாலை ஏற்குமா?",
        "No. Article 31C explicitly bars Article 14 challenges against laws giving effect to Article 39(b) or 39(c)", "இல்லை. உறுப்பு 39(b) அல்லது 39(c)-ஐ செயல்படுத்தும் சட்டங்களுக்கு எதிராக உறுப்பு 14 சவால்களை உறுப்பு 31C வெளிப்படையாகத் தடுக்கிறது",
        "Yes. Article 14 overrides all constitutional provisions under all circumstances", "ஆம். உறுப்பு 14 அனைத்து சூழ்நிலைகளிலும் அனைத்து அரசியலமைப்பு விதிகளையும் மிஞ்சுகிறது",
        "Yes, but only if the landlord pays 50% of court fees to the Treasury", "ஆம், ஆனால் நிலப்பிரபு நீதிமன்றக் கட்டணத்தில் 50%-ஐ கருவூலத்திற்குச் செலுத்தினால் மட்டுமே",
        "No, because landlords have no standing to file writs in High Courts", "இல்லை, ஏனெனில் நிலப்பிரபுக்களுக்கு உயர் நீதிமன்றங்களில் பேராணை மனு தாக்கல் செய்ய உரிமை இல்லை",
        "A",
        "Under Article 31C (upheld in Kesavananda Bharati 1973 & Sanjeev Coke 1983), laws enacted to give effect to Article 39(b) (material resources distribution) or 39(c) (wealth concentration prevention) cannot be declared void on the ground that they violate Article 14 or Article 19.",
        "உறுப்பு 31C-ன் கீழ் (கேசவானந்த பாரதி 1973 & சஞ்சீவ் கோக் 1983 வழக்குகளில் உறுதி செய்யப்பட்டது), உறுப்பு 39(b) (பொருள் வளப் பகிர்வு) அல்லது 39(c)-ஐ (செல்வக் குவிப்புத் தடை) செயல்படுத்த இயற்றப்படும் சட்டங்கள் உறுப்பு 14 அல்லது உறுப்பு 19-ஐ மீறுகின்றன என்ற அடிப்படையில் செல்லாததாக அறிவிக்கப்பட முடியாது.",
        "TNPSC Trap: Article 31C creates a constitutional shield for 39(b) and 39(c) laws against Articles 14 and 19.",
        "டிஎன்பிஎஸ்சி பொறி: உறுப்புகள் 14 மற்றும் 19-க்கு எதிராக 39(b) மற்றும் 39(c) சட்டங்களுக்கு உறுப்பு 31C ஓர் அரசியலமைப்புப் பாதுகாப்பை உருவாக்குகிறது.",
        "Correct. Article 31C bars Article 14 challenges against valid 39(b)/(c) land reform laws.", "சரி. செல்லுபடியாகும் 39(b)/(c) நிலச்சீர்திருத்தச் சட்டங்களுக்கு எதிரான உறுப்பு 14 சவால்களை உறுப்பு 31C தடுக்கிறது.",
        "Article 31C creates a specific exception to Article 14.", "உறுப்பு 31C உறுப்பு 14-க்கு ஒரு குறிப்பிட்ட விலக்கை உருவாக்குகிறது.",
        "Court fees do not override Article 31C protection.", "நீதிமன்றக் கட்டணம் உறுப்பு 31C பாதுகாப்பை மிஞ்சாது.",
        "Landlords have standing, but Article 31C bars the Article 14 ground.", "நிலப்பிரபுக்களுக்கு உரிமை உண்டு, ஆனால் உறுப்பு 31C உறுப்பு 14 அடிப்படையைத் தடுக்கிறது."
    )

    # -------------------------------------------------------------------------
    # Q22 (Correct: B) - Case-law
    # -------------------------------------------------------------------------
    add_q(
        22, "Case-law",
        "How did Chief Justice S.R. Das formulate the 'Doctrine of Harmonious Construction' in Re Kerala Education Bill (1958)?",
        "கேரளா கல்வி மசோதா வழக்கில் (1958) தலைமை நீதிபதி எஸ்.ஆர். தாஸ் 'இணக்கமான விளக்கக் கோட்பாட்டை' எவ்வாறு உருவாக்கினார்?",
        "He held that Directive Principles automatically repeal all conflicting Fundamental Rights", "வழிகாட்டு நெறிமுறைகள் முரண்படும் அனைத்து அடிப்படை உரிமைகளையும் தானாகவே ரத்து செய்கின்றன என அவர் தீர்ப்பளித்தார்",
        "He held that courts should try to give effect to BOTH Part III Fundamental Rights and Part IV DPSPs without rendering either a dead letter, achieving harmony through statutory interpretation", "எந்தவொரு பகுதியையும் செயலற்றதாக்காமல் பகுதி III அடிப்படை உரிமைகள் மற்றும் பகுதி IV DPSP-கள் ஆகிய இரண்டிற்கும் செயலாக்கம் அளிக்க நீதிமன்றங்கள் முயல வேண்டும் என்றும், சட்டப்பூர்வ விளக்கத்தின் மூலம் இணக்கத்தை அடைய வேண்டும் என்றும் அவர் தீர்ப்பளித்தார்",
        "He held that Directive Principles apply only to municipal tax laws", "வழிகாட்டு நெறிமுறைகள் நகராட்சி வரிச் சட்டங்களுக்கு மட்டுமே பொருந்தும் என அவர் தீர்ப்பளித்தார்",
        "He held that Fundamental Rights can be suspended by state Chief Ministers", "அடிப்படை உரிமைகளை மாநில முதலமைச்சர்கள் இடைநீக்கம் செய்யலாம் என அவர் தீர்ப்பளித்தார்",
        "B",
        "In Re Kerala Education Bill (1958), SC introduced the Doctrine of Harmonious Construction, ruling that when Part III and Part IV appear to conflict, the court should attempt to reconcile them so that both provisions are given practical effect without destroying either.",
        "கேரளா கல்வி மசோதா வழக்கில் (1958), பகுதி III மற்றும் பகுதி IV மோதிக் கொள்வது போலத் தோன்றும் போது, எந்தவொரு விதியையும் அழிக்காமல் இரண்டிற்கும் நடைமுறைச் செயலாக்கம் அளிக்கும் வகையில் நீதிமன்றம் அவற்றை இணக்கமாக்க முயல வேண்டும் என இணக்கமான விளக்கக் கோட்பாட்டை SC அறிமுகப்படுத்தியது.",
        "Harmonious Construction is a foundational rule of constitutional interpretation in India.", "இணக்கமான விளக்கம் என்பது இந்தியாவில் அரசியலமைப்பு விளக்கத்தின் ஓர் அடித்தள விதியாகும்.",
        "DPSPs do not repeal Fundamental Rights automatically.", "DPSP-கள் அடிப்படை உரிமைகளைத் தானாக ரத்து செய்வதில்லை.",
        "Correct. SC held courts should give effect to both Part III and IV through harmonious interpretation.", "சரி. இணக்கமான விளக்கத்தின் மூலம் பகுதி III மற்றும் IV ஆகிய இரண்டிற்கும் செயலாக்கம் அளிக்க வேண்டும் என SC கூறியது.",
        "DPSPs apply to governance nationwide.", "DPSP-கள் நாடு தழுவிய ஆட்சிக்குப் பொருந்தும்.",
        "Chief Ministers cannot suspend Fundamental Rights.", "முதலமைச்சர்கள் அடிப்படை உரிமைகளை இடைநீக்கம் செய்ய முடியாது."
    )

    # -------------------------------------------------------------------------
    # Q23 (Correct: C) - Multi-statement
    # -------------------------------------------------------------------------
    add_q(
        23, "Multi-statement",
        "Consider the following statements regarding Articles 43A and 43B:\n1. Article 43A directs the State to secure participation of workers in management of industrial undertakings.\n2. Article 43B directs the State to promote voluntary formation and autonomous functioning of Co-operative Societies.\n3. Both Article 43A and Article 43B were inserted by the 42nd Constitutional Amendment Act, 1976.\nWhich of the statements given above is/are CORRECT?",
        "உறுப்புகள் 43A மற்றும் 43B பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. உறுப்பு 43A தொழிற்சாலைகள் மேலாண்மையில் தொழிலாளர்களின் பங்கேற்பை உறுதி செய்ய அரசுக்கு வழிகாட்டுகிறது.\n2. உறுப்பு 43B கூட்டுறவுச் சங்கங்களின் தன்னார்வ உருவாக்கம் மற்றும் தன்னாட்சி செயல்பாட்டை மேம்படுத்த அரசுக்கு வழிகாட்டுகிறது.\n3. உறுப்பு 43A மற்றும் உறுப்பு 43B ஆகிய இரண்டும் 1976-ன் 42வது அரசியலமைப்பு திருத்தச் சட்டத்தால் இணைக்கப்பட்டன.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
        "1 and 3 only", "1 மற்றும் 3 மட்டுமே",
        "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
        "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
        "1, 2 and 3", "1, 2 மற்றும் 3",
        "C",
        "Statements 1 and 2 are correct. Statement 3 is INCORRECT because Article 43A was inserted by the 42nd CAA 1976, whereas Article 43B was inserted by the 97th CAA 2011.",
        "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் உறுப்பு 43A 1976-ன் 42வது திருத்தத்தால் சேர்க்கப்பட்டது, மாறாக உறுப்பு 43B 2011-ன் 97வது திருத்தத்தால் சேர்க்கப்பட்டது.",
        "TNPSC Trap: 43A = 42nd CAA (1976); 43B = 97th CAA (2011).", "டிஎன்பிஎஸ்சி பொறி: 43A = 42வது திருத்தம் (1976); 43B = 97வது திருத்தம் (2011).",
        "Statement 3 is incorrect.", "கூற்று 3 தவறானது.",
        "Statement 3 is incorrect.", "கூற்று 3 தவறானது.",
        "Correct. Statements 1 and 2 are correct; Statement 3 is false (43B was added by 97th CAA 2011).", "சரி. கூற்றுகள் 1 மற்றும் 2 சரியானவை; கூற்று 3 தவறானது (43B 97வது திருத்தம் 2011 மூலம் சேர்க்கப்பட்டது).",
        "Statement 3 is incorrect.", "கூற்று 3 தவறானது."
    )

    # -------------------------------------------------------------------------
    # Q24 (Correct: D) - Constitutional Application
    # -------------------------------------------------------------------------
    add_q(
        24, "Application",
        "Compare the constitutional domain of Article 49 (Monuments Protection DPSP) with Articles 29 and 30 (Minority Educational/Cultural Rights FR).",
        "உறுப்பு 49-ன் (நினைவிடங்கள் பாதுகாப்பு DPSP) அரசியலமைப்புக் களத்தை உறுப்புகள் 29 மற்றும் 30-உடன் (சிறுபான்மையினர் கல்வி/பண்பாட்டு உரிமைகள் FR) ஒப்பிடுக.",
        "Article 49 applies only to foreign religious buildings, while Arts 29-30 apply to government offices", "உறுப்பு 49 வெளிநாட்டு மதக் கட்டிடங்களுக்கு மட்டுமே பொருந்தும், 29-30 அரசு அலுவலகங்களுக்குப் பொருந்தும்",
        "Article 49 is a justiciable Fundamental Right, while Arts 29-30 are non-justiciable DPSPs", "உறுப்பு 49 ஒரு அமல்படுத்தக்கூடிய அடிப்படை உரிமை, 29-30 அமல்படுத்த முடியாத DPSP-கள்",
        "Article 49 was added by 44th Amendment, while Arts 29-30 were added by 86th Amendment", "உறுப்பு 49 44வது திருத்தத்தால் சேர்க்கப்பட்டது, 29-30 86வது திருத்தத்தால் சேர்க்கப்பட்டது",
        "Article 49 (Part IV DPSP) directs State to protect physical historical monuments declared of national importance by Parliament; Arts 29-30 (Part III FRs) guarantee justiciable rights to minorities/citizens to conserve language, script, culture, and establish educational institutions", "உறுப்பு 49 (பகுதி IV DPSP) நாடாளுமன்றத்தால் தேசிய முக்கியத்துவம் வாய்ந்தது என அறிவிக்கப்பட்ட பௌதிக வரலாற்று நினைவிடங்களைப் பாதுகாக்க அரசுக்கு வழிகாட்டுகிறது; 29-30 (பகுதி III FR-கள்) சிறுபான்மையினர்/குடிமக்கள் மொழி, எழுத்து, பண்பாட்டைப் பாதுகாக்கவும் கல்வி நிறுவனங்களை நிறுவவும் அமல்படுத்தக்கூடிய உரிமைகளை உத்தரவாதம் செய்கின்றன",
        "D",
        "Article 49 (DPSP) mandates state protection for physical heritage (ancient monuments, archaeological sites declared of national importance under AMASR Act 1958). Articles 29 and 30 (FRs) guarantee justiciable rights to minorities and sections of citizens to preserve language, script, culture, and manage educational institutions.",
        "உறுப்பு 49 (DPSP) பௌதிகப் பாரம்பரியத்திற்கான (1958 AMASR சட்டத்தின் கீழ் தேசிய முக்கியத்துவம் வாய்ந்தது என அறிவிக்கப்பட்ட பழங்கால நினைவிடங்கள், தொல்லியல் இடங்கள்) அரசு பாதுகாப்பைக் கட்டாயமாக்குகிறது. உறுப்புகள் 29 மற்றும் 30 (FR-கள்) சிறுபான்மையினர் மற்றும் குடிமக்களின் பிரிவினர் மொழி, எழுத்து, பண்பாட்டைப் பாதுகாக்கவும் கல்வி நிறுவனங்களை நிர்வகிக்கவும் அமல்படுத்தக்கூடிய உரிமைகளை உத்தரவாதம் செய்கின்றன.",
        "Distinction: 49 = Tangible national physical monuments DPSP; 29-30 = Intangible minority cultural/educational FRs.",
        "வேறுபாடு: 49 = தொட்டுணரக்கூடிய தேசிய பௌதிக நினைவிடங்கள் DPSP; 29-30 = அருவமான சிறுபான்மையினர் பண்பாட்டு/கல்வி FR-கள்.",
        "Incorrect applicability.", "தவறான பொருந்தும்தன்மை.",
        "Incorrect reversal of Part IV DPSP and Part III FR.", "பகுதி IV DPSP மற்றும் பகுதி III FR-ன் தவறான தலைகீழ் கூற்று.",
        "Both were in the original 1950 text.", "இரண்டும் அசல் 1950 உரையில் இருந்தன.",
        "Correct. 49 is State directive protecting physical national monuments; 29-30 are justiciable minority cultural/educational FRs.", "சரி. 49 பௌதிக தேசிய நினைவிடங்களைப் பாதுகாக்கும் அரசு வழிகாட்டல்; 29-30 அமல்படுத்தக்கூடிய சிறுபான்மையினர் பண்பாட்டு/கல்வி FR-கள்."
    )

    # -------------------------------------------------------------------------
    # Q25 (Correct: A) - Advanced Conceptual
    # -------------------------------------------------------------------------
    add_q(
        25, "Conceptual",
        "Why did Article 36 explicitly adopt the Article 12 definition of 'State' for Part IV of the Constitution?",
        "பகுதி IV-க்காக உறுப்பு 36 ஏன் உறுப்பு 12-ல் உள்ள 'அரசு' வரையறையை வெளிப்படையாக ஏற்றது?",
        "To ensure that all public authorities (Union, States, Panchayats, Municipalities, and statutory corporations like LIC/ONGC) are bound to apply DPSPs in policy and law-making", "அனைத்துப் பொது அமைப்புகளும் (ஒன்றியம், மாநிலங்கள், பஞ்சாயத்துகள், நகராட்சிகள் மற்றும் LIC/ONGC போன்ற சட்டப்பூர்வ நிறுவனங்கள்) கொள்கை மற்றும் சட்டம் இயற்றுவதில் DPSP-களைப் பயன்படுத்தக் கட்டுப்படுத்தப்படுவதை உறுதி செய்ய",
        "To allow statutory corporations to ignore environmental laws", "சட்டப்பூர்வ நிறுவனங்கள் சுற்றுச்சூழல் சட்டங்களைப் புறக்கணிக்க அனுமதிக்க",
        "To restrict DPSP applicability only to the President of India", "DPSP பொருந்தும்தன்மையை இந்தியக் குடியரசுத் தலைவருக்கு மட்டுமே சுருக்க",
        "To merge all state governments into a single central government", "அனைத்து மாநில அரசுகளையும் ஒரே மத்திய அரசாங்கமாக இணைக்க",
        "A",
        "By incorporating Article 12, Article 36 ensures that the directive principles in Part IV bind all levels of government — Union Parliament & Executive, State Legislatures & Executive, Local Authorities (Panchayats/Municipalities), and Statutory Bodies (LIC, ONGC, SAIL) — in exercising public powers.",
        "உறுப்பு 12-ஐ உள்ளடக்குவதன் மூலம், உறுப்பு 36 பகுதி IV-ல் உள்ள வழிகாட்டு நெறிமுறைகள் பொது அதிகாரங்களைப் பயன்படுத்துவதில் அனைத்து மட்ட அரசாங்கங்களையும் — ஒன்றிய நாடாளுமன்றம் & நிர்வாகம், மாநில சட்டமன்றங்கள் & நிர்வாகம், உள்ளாட்சி அமைப்புகள் (பஞ்சாயத்துகள்/நகராட்சிகள்) மற்றும் சட்டப்பூர்வ அமைப்புகள் (LIC, ONGC, SAIL) — கட்டுப்படுத்துவதை உறுதி செய்கிறது.",
        "All instrumentalities of the State under Article 12/36 are duty-bound to promote DPSP goals.", "உறுப்பு 12/36-ன் கீழ் உள்ள அரசின் அனைத்து அமைப்புகளும் DPSP இலக்குகளை மேம்படுத்தக் கடமைப்பட்டுள்ளன.",
        "Correct. Article 36 binds all public authorities under Article 12 to apply DPSPs.", "சரி. உறுப்பு 36 உறுப்பு 12-ன் கீழ் உள்ள அனைத்துப் பொது அமைப்புகளையும் DPSP-களைப் பயன்படுத்தக் கட்டுப்படுத்துகிறது.",
        "Statutory corporations are bound by environment DPSP Art 48A.", "சட்டப்பூர்வ நிறுவனங்கள் சுற்றுச்சூழல் DPSP உறுப்பு 48A-ஆல் கட்டுப்படுத்தப்படுகின்றன.",
        "DPSP binds all public authorities.", "DPSP அனைத்துப் பொது அமைப்புகளையும் கட்டுப்படுத்துகிறது.",
        "Article 36 does not alter federal structure.", "உறுப்பு 36 கூட்டாட்சி அமைப்பை மாற்றுவதில்லை."
    )

    # -------------------------------------------------------------------------
    # Q26 (Correct: B) - Assertion & Reason
    # -------------------------------------------------------------------------
    add_q(
        26, "Assertion-Reason",
        "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Directive Principles of State Policy are non-justiciable under Article 37.\nReason (R): As Dr. B.R. Ambedkar noted, the real sanction behind DPSP is political sanction — public opinion and accountability at the ballot box during elections.\nSelect the correct answer using the code below:",
        "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிக்கப்பட்டுள்ளன:\nகூற்று (A): அரசு வழிகாட்டு நெறிமுறைகள் உறுப்பு 37-ன் கீழ் நீதிமன்றங்களால் அமல்படுத்த முடியாதவை ஆகும்.\nகாரணம் (R): டாக்டர் பி.ஆர். அம்பேத்கர் குறிப்பிட்டது போல, DPSP-ன் பின்னால் உள்ள உண்மையான ஒப்புதல் அரசியல் ஒப்புதலாகும் — பொதுமக்களின் கருத்து மற்றும் தேர்தலின் போது வாக்களிக்கும் பொறுப்புக்கூறலே ஆகும்.\nகீழேயுள்ள குறியீட்டைப் பயன்படுத்தி சரியான பதிலைத் தேர்ந்தெடுக்கவும்:",
        "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி, ஆனால் காரணம் (R) கூற்று (A)-விற்கு சரியான விளக்கமல்ல",
        "Both (A) and (R) are true, and (R) is the correct explanation of (A)", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி, மேலும் காரணம் (R) கூற்று (A)-விற்கு சரியான விளக்கமாகும்",
        "(A) is true, but (R) is false", "கூற்று (A) சரி, ஆனால் காரணம் (R) தவறு",
        "(A) is false, but (R) is true", "கூற்று (A) தவறு, ஆனால் காரணம் (R) சரி",
        "B",
        "Both (A) and (R) are true, and (R) correctly explains (A). In the Constituent Assembly, Dr. B.R. Ambedkar explained that DPSPs were made non-justiciable because the nation lacked financial resources in 1950, but a government that fails to implement DPSPs will certainly have to answer to the electorate at election time.",
        "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி, மேலும் காரணம் (R) கூற்று (A)-விற்கு சரியான விளக்கமாகும். அரசியலமைப்பு நிர்ணய சபையில், 1950-ல் நாட்டின் நிதி ஆதாரங்கள் குறைவாக இருந்ததால் DPSP-கள் அமல்படுத்த முடியாதவையாக மாற்றப்பட்டன, ஆனால் DPSP-களை அமல்படுத்தத் தவறும் ஒரு அரசாங்கம் நிச்சயமாகத் தேர்தல் காலத்தில் வாக்காளர்களுக்குப் பதிலளிக்க வேண்டி வரும் என்று டாக்டர் பி.ஆர். அம்பேத்கர் விளக்கினார்.",
        "Political Sanction > Judicial Sanction for DPSP implementation in a democratic republic.", "ஜனநாயகக் குடியரசில் DPSP அமலாக்கத்திற்கு நீதித்துறை ஒப்புதலை விட அரசியல் ஒப்புதலே மேலானது.",
        "Reason (R) explains why non-justiciable DPSPs are still effectively implemented in a democracy.", "நீதிமன்றங்களால் அமல்படுத்த முடியாத DPSP-கள் ஜனநாயகத்தில் எவ்வாறு திறம்பட அமல்படுத்தப்படுகின்றன என்பதை காரணம் (R) விளக்குகிறது.",
        "Correct. Both (A) and (R) are true, and (R) is the correct explanation of (A).", "சரி. கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி, மேலும் காரணம் (R) கூற்று (A)-விற்கு சரியான விளக்கமாகும்.",
        "Reason (R) is true.", "காரணம் (R) சரியானது.",
        "Assertion (A) is true.", "கூற்று (A) சரியானது."
    )

    # -------------------------------------------------------------------------
    # Q27 (Correct: C) - Multi-statement
    # -------------------------------------------------------------------------
    add_q(
        27, "Multi-statement",
        "Consider the following statements regarding Article 47:\n1. Article 47 regards raising nutrition level, standard of living, and improving public health as primary duties of the State.\n2. Article 47 explicitly directs prohibition of intoxicating drinks and health-injurious drugs EXCEPT for medicinal purposes.\n3. In F.N. Balsara case (1951), SC held that state prohibition laws violate Article 19(1)(g) and are void.\nWhich of the statements given above is/are CORRECT?",
        "உறுப்பு 47 பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. உறுப்பு 47 சத்துணவு நிலை, வாழ்க்கை முறை மற்றும் பொது சுகாதாரத்தை உயர்த்துவதை அரசின் முதன்மைக் கடமைகளாகக் கருதுகிறது.\n2. உறுப்பு 47 மருத்துவ நோக்கங்களைத் தவிர போதைப் பானங்கள் மற்றும் தீங்கு விளைவிக்கும் மருந்துகள் அருந்துவதை மதுவிலக்கு செய்ய வெளிப்படையாக வழிகாட்டுகிறது.\n3. F.N. பால்சரா வழக்கில் (1951), மாநில மதுவிலக்குச் சட்டங்கள் உறுப்பு 19(1)(g)-ஐ மீறுகின்றன மற்றும் செல்லாதவை என SC தீர்ப்பளித்தது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
        "1 only", "1 மட்டுமே",
        "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
        "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
        "1, 2 and 3", "1, 2 மற்றும் 3",
        "C",
        "Statements 1 and 2 are correct. Statement 3 is INCORRECT because in F.N. Balsara (1951), the SC UPHELD state prohibition laws, ruling that trade in intoxicating liquor is subject to reasonable restrictions under Article 19(6).",
        "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் F.N. பால்சரா வழக்கில் (1951), SC மாநில மதுவிலக்குச் சட்டங்களை உறுதி செய்தது, போதைப் பான வியாபாரம் உறுப்பு 19(6)-ன் கீழ் நியாயமான கட்டுப்பாடுகளுக்கு உட்பட்டது எனத் தீர்ப்பளித்தது.",
        "Statement 3 trap: F.N. Balsara UPHELD prohibition laws; it did not strike them down.", "கூற்று 3 பொறி: F.N. பால்சரா மதுவிலக்குச் சட்டங்களை உறுதி செய்தது; அவற்றை ரத்து செய்யவில்லை.",
        "Statement 2 is also correct.", "கூற்று 2-ம் சரியானதாகும்.",
        "Statement 3 is incorrect because SC upheld prohibition laws in F.N. Balsara.", "F.N. பால்சரா வழக்கில் SC மதுவிலக்குச் சட்டங்களை உறுதி செய்ததால் கூற்று 3 தவறானது.",
        "Correct. Statements 1 and 2 are correct; Statement 3 is false.", "சரி. கூற்றுகள் 1 மற்றும் 2 சரியானவை; கூற்று 3 தவறானது.",
        "Statement 3 is incorrect.", "கூற்று 3 தவறானது."
    )

    # -------------------------------------------------------------------------
    # Q28 (Correct: D) - Amendment / Consequence
    # -------------------------------------------------------------------------
    add_q(
        28, "Amendment/Case",
        "How did the 44th Constitutional Amendment Act, 1978 impact the structural interplay between Fundamental Rights and Directive Principles?",
        "1978-ன் 44வது அரசியலமைப்பு திருத்தச் சட்டம் எவ்வாறு அடிப்படை உரிமைகள் மற்றும் வழிகாட்டு நெறிமுறைகளுக்கு இடையிலான அமைப்புக் தொடர்பைப் பாதித்தது?",
        "It abolished Part IV DPSPs completely", "இது பகுதி IV DPSP-களை முழுமையாக ஒழித்தது",
        "It made all DPSPs justiciable in High Courts under Article 226", "இது அனைத்து DPSP-களையும் உறுப்பு 226-ன் கீழ் உயர் நீதிமன்றங்களில் அமல்படுத்தக்கூடியதாக மாற்றியது",
        "It made Article 44 Uniform Civil Code a Fundamental Right", "இது உறுப்பு 44 பொது சிவில் சட்டத்தை அடிப்படை உரிமையாக்கியது",
        "It deleted Right to Property from Part III (Art 31) removing property roadblocks for DPSP land reforms, and inserted Article 38(2) directing State to minimise inequalities", "இது பகுதி III-லிருந்து (உறுப்பு 31) சொத்து உரிமையை நீக்கி DPSP நிலச்சீர்திருத்தங்களுக்கான சொத்துத் தடைகளை அகற்றியது, மேலும் சமத்துவமின்மையைக் குறைக்க அரசுக்கு வழிகாட்டும் உறுப்பு 38(2)-ஐ இணைத்தது",
        "D",
        "The 44th Amendment Act 1978 had a dual impact: 1) Removed Right to Property from Part III (re-enacted as Art 300A legal right), enabling smooth implementation of land reform DPSPs (Arts 39b/c); 2) Added Article 38(2) directing State to minimise inequalities in income, status, facilities, and opportunities.",
        "1978-ன் 44வது திருத்தச் சட்டம் இரட்டைத் தாக்கத்தைக் கொண்டிருந்தது: 1) பகுதி III-லிருந்து சொத்து உரிமையை நீக்கியது (உறுப்பு 300A சட்ட உரிமையாக மீண்டும் இயற்றப்பட்டது), இது DPSP நிலச்சீர்திருத்தங்களை (உறுப்புகள் 39b/c) சீராக அமல்படுத்த உதவியது; 2) வருமானம், அந்தஸ்து, வசதிகள் மற்றும் வாய்ப்புகளில் சமத்துவமின்மையைக் குறைக்க அரசுக்கு வழிகாட்டும் உறுப்பு 38(2)-ஐச் சேர்த்தது.",
        "44th CAA 1978 removed the constitutional property weapon used to challenge socialist land reform DPSPs.", "44வது திருத்தம் 1978 சமதர்ம நிலச்சீர்திருத்த DPSP-களை சவால் செய்யப் பயன்படுத்தப்பட்ட அரசியலமைப்புச் சொத்து ஆயுதத்தை அகற்றியது.",
        "Part IV was not abolished.", "பகுதி IV ஒழிக்கப்படவில்லை.",
        "DPSPs remain non-justiciable.", "DPSP-கள் தொடர்ந்து அமல்படுத்த முடியாதவையாகவே உள்ளன.",
        "Article 44 remains a DPSP.", "உறுப்பு 44 தொடர்ந்து DPSP-ஆகவே நீடிக்கிறது.",
        "Correct. 44th Amendment 1978 deleted Right to Property (Art 31) and inserted Article 38(2).", "சரி. 44வது திருத்தம் 1978 சொத்து உரிமையை (உறுப்பு 31) நீக்கி உறுப்பு 38(2)-ஐ இணைத்தது."
    )

    # -------------------------------------------------------------------------
    # Q29 (Correct: A) - High-level Trap
    # -------------------------------------------------------------------------
    add_q(
        29, "TNPSC Trap",
        "Does the constitutional text of Article 48 prohibit cow slaughter on RELIGIOUS grounds or on SCIENTIFIC/ECONOMIC grounds?",
        "உறுப்பு 48-ன் அரசியலமைப்பு உரை பசு வதையை மதக் காரணங்களின் அடிப்படையில் தடுத்து நிறுத்துகிறதா அல்லது அறிவியல்/பொருளாதாரக் காரணங்களின் அடிப்படையில் தடுத்து நிறுத்துகிறதா?",
        "On scientific and economic grounds, as Article 48 combines modern agriculture/animal husbandry with preservation of milch and draught cattle breeds", "அறிவியல் மற்றும் பொருளாதாரக் காரணங்களின் அடிப்படையில், ஏனெனில் உறுப்பு 48 நவீன விவசாயம்/கால்நடை வளர்ப்பைப் பால் தரும் மற்றும் பாரம் இழுக்கும் கால்நடை இனப் பாதுகாப்புடன் இணைக்கிறது",
        "On religious grounds, explicitly mentioning Hindu religious rituals", "மதக் காரணங்களின் அடிப்படையில், இந்து மதச் சடங்குகளை வெளிப்படையாகக் குறிப்பிடுகிறது",
        "On political grounds, restricting meat trade only during general election years", "அரசியல் காரணங்களின் அடிப்படையில், பொதுத் தேர்தல் ஆண்டுகளில் மட்டுமே இறைச்சி வர்த்தகத்தைக் கட்டுப்படுத்துகிறது",
        "On international trade grounds, protecting foreign meat exporters", "சர்வதேச வர்த்தகக் காரணங்களின் அடிப்படையில், வெளிநாட்டு இறைச்சி ஏற்றுமதியாளர்களைப் பாதுகாக்கிறது",
        "A",
        "Article 48 states: 'The State shall endeavor to organize agriculture and animal husbandry on modern and scientific lines and shall, in particular, take steps for preserving and improving the breeds, and prohibiting the slaughter of cows and calves and other milch and draught cattle.' The text relies on scientific agriculture and preservation of economic draught/milch cattle.",
        "உறுப்பு 48 கூறுகிறது: 'நவீன மற்றும் அறிவியல் முறைகளில் விவசாயம் மற்றும் கால்நடை பராமரிப்பை அமைக்க அரசு முயல வேண்டும், மேலும் குறிப்பாக இனங்களைப் பாதுகாப்பதற்கும் மேம்படுத்துவதற்கும் பசுக்கள், கன்றுகள் மற்றும் பிற பால் தரும் மற்றும் பாரம் இழுக்கும் கால்நடைகளைக் கொல்வதைத் தடை செய்வதற்கும் நடவடிக்கைகள் எடுக்க வேண்டும்.' உரை அறிவியல் விவசாயம் மற்றும் பொருளாதாரக் கால்நடை இனப் பாதுகாப்பைச் சார்ந்தே உள்ளது.",
        "TNPSC Trap: Article 48 text does NOT mention religion or Hindu rituals; it frames cattle protection under scientific agriculture and animal husbandry.",
        "டிஎன்பிஎஸ்சி பொறி: உறுப்பு 48 உரை மதத்தையோ இந்து சடங்குகளையோ குறிப்பிடவில்லை; இது கால்நடை பாதுகாப்பை அறிவியல் விவசாயம் மற்றும் கால்நடை வளர்ப்பின் கீழ் அமைக்கிறது.",
        "Correct. Article 48 text frames cattle preservation under scientific agriculture and animal husbandry.", "சரி. உறுப்பு 48 உரை கால்நடை பாதுகாப்பை அறிவியல் விவசாயம் மற்றும் கால்நடை வளர்ப்பின் கீழ் அமைக்கிறது.",
        "Religion is not mentioned in Article 48 text.", "உறுப்பு 48 உரையில் மதம் குறிப்பிடப்படவில்லை.",
        "Elections are not mentioned.", "தேர்தல்கள் குறிப்பிடப்படவில்லை.",
        "Foreign trade is not mentioned.", "வெளிநாட்டு வர்த்தகம் குறிப்பிடப்படவில்லை."
    )

    # -------------------------------------------------------------------------
    # Q30 (Correct: B) - Case-based
    # -------------------------------------------------------------------------
    add_q(
        30, "Amendment/Case",
        "In Golak Nath v. State of Punjab (1967), what was the Supreme Court's stance on Parliament's power to amend Fundamental Rights to implement Directive Principles?",
        "கோலக் நாத் எதிர் பஞ்சாப் மாநிலம் வழக்கில் (1967), வழிகாட்டு நெறிமுறைகளை அமல்படுத்த அடிப்படை உரிமைகளைத் திருத்துவதற்கான நாடாளுமன்றத்தின் அதிகாரம் குறித்த உச்ச நீதிமன்றத்தின் நிலைப்பாடு என்ன?",
        "SC held that Parliament can amend Fundamental Rights freely to implement DPSPs", "DPSP-களை அமல்படுத்த நாடாளுமன்றம் அடிப்படை உரிமைகளைத் தாராளமாகத் திருத்தலாம் என SC கூறியது",
        "SC held that Fundamental Rights are sacrosanct and transcendental, and Parliament CANNOT amend Part III to curtail Fundamental Rights even to implement DPSPs", "அடிப்படை உரிமைகள் புனிதமானவை மற்றும் மேலானவை, DPSP-களை அமல்படுத்துவதற்காகக் கூட அடிப்படை உரிமைகளைக் குறைக்க நாடாளுமன்றத்தால் பகுதி III-ஐத் திருத்த முடியாது என SC தீர்ப்பளித்தது",
        "SC held that DPSP Article 44 overrides all Fundamental Rights automatically", "DPSP உறுப்பு 44 அனைத்து அடிப்படை உரிமைகளையும் தானாகவே மிஞ்சுகிறது என SC கூறியது",
        "SC held that State Assemblies have exclusive power to amend Part III", "பகுதி III-ஐத் திருத்த மாநில சட்டமன்றங்களுக்கு மட்டுமே பிரத்யேக அதிகாரம் உண்டு என SC கூறியது",
        "B",
        "In Golak Nath (1967 11-judge bench), C.J. Subba Rao held that Fundamental Rights in Part III are given a transcendental and sacrosanct position, and Parliament has no power under Article 368 to abridge or take away Fundamental Rights even for enforcing DPSPs. This led Parliament to pass the 24th & 25th Amendments 1971.",
        "கோலக் நாத் வழக்கில் (1967 11-நீதிபதிகள் அமர்வு), பகுதி III-ல் உள்ள அடிப்படை உரிமைகளுக்கு ஒரு மேலான மற்றும் புனிதமான இடம் வழங்கப்பட்டுள்ளது என்றும், DPSP-களை அமல்படுத்துவதற்காகக் கூட அடிப்படை உரிமைகளைக் குறைக்க அல்லது பறிக்க உறுப்பு 368-ன் கீழ் நாடாளுமன்றத்திற்கு அதிகாரம் இல்லை என்றும் தலைமை நீதிபதி சுப்பா ராவ் தீர்ப்பளித்தார். இது நாடாளுமன்றம் 1971-ல் 24வது & 25வது திருத்தங்களை நிறைவேற்ற வழிவகுத்தது.",
        "Golak Nath stance was later modified by Kesavananda Bharati (1973) introducing Basic Structure limits.",
        "கோலக் நாத் நிலைப்பாடு பின்னர் கேசவானந்த பாரதி (1973) வழக்கில் அடிப்படை அமைப்புக் கட்டுப்பாடுகளை அறிமுகப்படுத்தி மாற்றியமைக்கப்பட்டது.",
        "Golak Nath prohibited amending Part III for DPSP enforcement.", "கோலக் நாத் DPSP அமலாக்கத்திற்காக பகுதி III-ஐத் திருத்துவதைத் தடுத்தது.",
        "Correct. Golak Nath held FRs were sacrosanct and non-amendable even for DPSP implementation.", "சரி. DPSP அமலாக்கத்திற்காகக் கூட FR-கள் புனிதமானவை மற்றும் திருத்த முடியாதவை என கோலக் நாத் தீர்ப்பளித்தது.",
        "Article 44 was not given overriding status.", "உறுப்பு 44-க்கு மேலோங்கும் அந்தஸ்து வழங்கப்படவில்லை.",
        "State assemblies cannot amend Part III.", "மாநில சட்டமன்றங்கள் பகுதி III-ஐத் திருத்த முடியாது."
    )

    # -------------------------------------------------------------------------
    # Q31 (Correct: C) - Multi-statement
    # -------------------------------------------------------------------------
    add_q(
        31, "Multi-statement",
        "Consider the following Supreme Court observations regarding Article 44 (Uniform Civil Code):\n1. In Shah Bano (1985), SC regretted that Article 44 remained a 'dead letter'.\n2. In Sarla Mudgal (1995), SC urged the Govt to retrieve Article 44 from cold storage to prevent bigamy by conversion.\n3. In Shayara Bano (2017), SC declared Instant Triple Talaq (Talaq-e-Biddat) unconstitutional under Article 14.\nWhich of the statements given above is/are CORRECT?",
        "உறுப்பு 44 (பொது சிவில் சட்டம்) பற்றிய பின்வரும் உச்ச நீதிமன்ற அவதானிப்புகளைக் கருதுக:\n1. ஷா பானோ வழக்கில் (1985), உறுப்பு 44 'செயலற்ற எழுத்தாக' இருப்பது குறித்து SC வருந்தியது.\n2. சர்லா முத்கல் வழக்கில் (1995), மதம் மாறி இரட்டைத் திருமணம் செய்வதைத் தடுக்க உறுப்பு 44-ஐக் குளிர்பதனப் பெட்டியிலிருந்து மீட்டெடுக்குமாறு அரசை SC வலியுறுத்தியது.\n3. ஷாயரா பானோ வழக்கில் (2017), முத்தலாக் முறையை உறுப்பு 14-ன் கீழ் அரசியலமைப்புக்கு முரணானது என SC அறிவித்தது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
        "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
        "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
        "1, 2 and 3", "1, 2 மற்றும் 3",
        "1 and 3 only", "1 மற்றும் 3 மட்டுமே",
        "C",
        "All three statements are CORRECT. In Shah Bano (1985), SC observed Article 44 remained a dead letter. In Sarla Mudgal (1995), SC urged UCC enactment to stop bigamous marriages via conversion. In Shayara Bano (2017), SC declared Instant Triple Talaq unconstitutional under Article 14.",
        "மூன்று கூற்றுகளும் சரியானவை. ஷா பானோ வழக்கில் (1985), உறுப்பு 44 செயலற்ற எழுத்தாக இருப்பதாக SC குறிப்பிட்டது. சர்லா முத்கல் வழக்கில் (1995), மதம் மாறி இரட்டைத் திருமணம் செய்வதைத் தடுக்க UCC இயற்ற வலியுறுத்தியது. ஷாயரா பானோ வழக்கில் (2017), முத்தலாக் முறையை உறுப்பு 14-ன் கீழ் அரசியலமைப்புக்கு முரணானது என அறிவித்தது.",
        "All 3 rulings represent key judicial observations on Article 44 and personal law reforms.", "3 தீர்ப்புகளும் உறுப்பு 44 மற்றும் தனிநபர் சட்டச் சீர்திருத்தங்கள் குறித்த முக்கிய நீதித்துறை அவதானிப்புகளைப் பிரதிபலிக்கின்றன.",
        "Statement 3 is also correct, making 1, 2 and 3 correct.", "கூற்று 3-ம் சரியானதால், 1, 2 மற்றும் 3 சரியானவை ஆகும்.",
        "Statement 1 is also correct.", "கூற்று 1-ம் சரியானதாகும்.",
        "Correct. Statements 1, 2 and 3 are all correct.", "சரி. கூற்றுகள் 1, 2 மற்றும் 3 அனைத்தும் சரியானவை.",
        "Statement 2 is also correct.", "கூற்று 2-ம் சரியானதாகும்."
    )

    # -------------------------------------------------------------------------
    # Q32 (Correct: D) - Constitutional Application
    # -------------------------------------------------------------------------
    add_q(
        32, "Application",
        "How has Article 42 (Humane Conditions of Work & Maternity Relief) evolved through statutory legislation and judicial expansion?",
        "உறுப்பு 42 (மனிதத்தன்மை வேலை நிலைமைகள் & பேறுகால உதவி) எவ்வாறு சட்டப்பூர்வ சட்டங்கள் மற்றும் நீதித்துறை விரிவாக்கம் மூலம் வளர்ச்சியடைந்துள்ளது?",
        "It led to the complete abolition of all factories in India", "இது இந்தியாவில் உள்ள அனைத்துத் தொழிற்சாலைகளையும் முழுமையாக ஒழிப்பதற்கு வழிவகுத்தது",
        "It restricted maternity leave strictly to 3 days without pay", "இது பேறுகால விடுப்பைச் சம்பளமின்றி 3 நாட்களுக்கு மட்டுமே சுருக்கியது",
        "It made working 18 hours a day compulsory for all industrial labor", "இது அனைத்துத் தொழில்துறை தொழிலாளர்களுக்கும் ஒரு நாளைக்கு 18 மணி நேரம் வேலை செய்வதைக் கட்டாயமாக்கியது",
        "Statutorily, Maternity Benefit Act 1961 (amended 2017 to 26 weeks paid leave) implements Art 42; Judicially, Bandhua Mukti Morcha (1984) read Art 42 into Art 21 making humane work conditions a Right to Life aspect", "சட்டப்பூர்வமாக, பேறுகால நலச் சட்டம் 1961 (2017-ல் 26 வாரங்கள் சம்பள விடுப்பாகத் திருத்தப்பட்டது) உறுப்பு 42-ஐ செயல்படுத்துகிறது; நீதித்துறை ரீதியாக, பந்துவா முக்தி மோர்ச்சா (1984) உறுப்பு 42-ஐ உறுப்பு 21-க்குள் வாசித்து மனிதத்தன்மை வேலை நிலைமைகளை வாழ்வு உரிமையின் அம்சமாக்கியது",
        "D",
        "Article 42 operates on two fronts: 1) Statutory: Maternity Benefit Act 1961 (2017 amendment raised paid maternity leave from 12 to 26 weeks; TN Govt grants 12 months paid leave); 2) Judicial: In Bandhua Mukti Morcha (1984), SC held Right to Life under Art 21 includes living with human dignity in just and humane conditions of work under Art 42.",
        "உறுப்பு 42 இரண்டு தளங்களில் செயல்படுகிறது: 1) சட்டப்பூர்வ: பேறுகால நலச் சட்டம் 1961 (2017 திருத்தம் சம்பள விடுப்பை 12-லிருந்து 26 வாரங்களாக உயர்த்தியது; தமிழக அரசு 12 மாதங்கள் சம்பள விடுப்பு வழங்குகிறது); 2) நீதித்துறை: பந்துவா முக்தி மோர்ச்சா வழக்கில் (1984), உறுப்பு 21-ன் கீழ் வாழ்வு உரிமை என்பது உறுப்பு 42-ன் கீழ் மனிதத்தன்மை வேலை நிலைமைகளுடன் மனித கண்ணியத்துடன் வாழ்வதையும் உள்ளடக்கும் என SC தீர்ப்பளித்தது.",
        "Article 42 covers both factory health/safety (Factories Act 1948) and maternity benefits.", "உறுப்பு 42 தொழிற்சாலை சுகாதாரம்/பாதுகாப்பு (1948 சட்டம்) மற்றும் பேறுகால நன்மைகள் இரண்டையும் உள்ளடக்கியது.",
        "Factories are regulated, not abolished.", "தொழிற்சாலைகள் முறைப்படுத்தப்படுகின்றன, ஒழிக்கப்படவில்லை.",
        "Maternity Benefit Act 2017 mandates 26 weeks paid leave.", "பேறுகால நலச் சட்டம் 2017 26 வாரங்கள் சம்பள விடுப்பைக் கட்டாயமாக்குகிறது.",
        "Factories Act limits working hours to 8 hours/day.", "தொழிற்சாலைகள் சட்டம் வேலை நேரத்தை ஒரு நாளைக்கு 8 மணி நேரமாகக் கட்டுப்படுத்துகிறது.",
        "Correct. Art 42 is implemented via Maternity Benefit Act 1961/2017 and read into Art 21 by Bandhua Mukti Morcha 1984.", "சரி. உறுப்பு 42 பேறுகால நலச் சட்டம் 1961/2017 மூலம் செயல்படுத்தப்பட்டு, பந்துவா முக்தி மோர்ச்சா 1984 மூலம் உறுப்பு 21-க்குள் வாசிக்கப்படுகிறது."
    )

    # -------------------------------------------------------------------------
    # Q33 (Correct: A) - Advanced Conceptual
    # -------------------------------------------------------------------------
    add_q(
        33, "Conceptual",
        "How do the Directive Principles of State Policy transform the philosophical character of the Indian State?",
        "அரசு வழிகாட்டு நெறிமுறைகள் எவ்வாறு இந்திய அரசின் தத்துவார்த்த இயல்பை மாற்றியமைக்கின்றன?",
        "They transform the State from a colonial Police State (focused merely on law, order & tax collection) into a modern Welfare State (committed to social & economic democracy)", "அவை அரசை ஒரு காலனித்துவ காவல் அரசிலிருந்து (சட்டம், ஒழுங்கு & வரி வசூல் மீது மட்டுமே கவனம் செலுத்தியது) ஒரு நவீன நல அரசாக (சமூக & பொருளாதார ஜனநாயகத்திற்கு அர்ப்பணிக்கப்பட்டது) மாற்றியமைக்கின்றன",
        "They convert India into an absolute dictatorship controlled by military generals", "அவை இந்தியாவை இராணுவ ஜெனரல்களால் கட்டுப்படுத்தப்படும் முற்றுமுழுதான சர்வாதிகாரமாக மாற்றுகின்றன",
        "They abolish all state legislatures and centralize power in District Collectors", "அவை அனைத்து மாநில சட்டமன்றங்களையும் ஒழித்து மாவட்ட ஆட்சியர்களிடம் அதிகாரத்தைக் குவிக்கின்றன",
        "They replace written laws with religious scriptures", "அவை எழுதப்பட்ட சட்டங்களை மத நூல்களால் மாற்றியமைக்கின்றன",
        "A",
        "Part IV DPSPs embody the social revolution vision of the Indian Constitution, shifting the purpose of government from colonial negative maintenance of law and order (Police State) to positive socio-economic welfare, health, education, living wages, and egalitarian order (Welfare State).",
        "பகுதி IV DPSP-கள் இந்திய அரசியலமைப்பின் சமூகப் புரட்சித் தொலைநோக்கை வெளிப்படுத்துகின்றன, அரசாங்கத்தின் நோக்கத்தைக் காலனித்துவ எதிர்மறை சட்டம் ஒழுங்கு பராமரிப்பிலிருந்து (காவல் அரசு) நேர்மறை சமூக-பொருளாதார நலன், சுகாதாரம், கல்வி, வாழ்வாதார ஊதியம் மற்றும் சமத்துவ ஒழுங்காக (நல அரசு) மாற்றுகின்றன.",
        "Granville Austin noted that DPSP and Fundamental Rights together form the core commitment to social revolution.", "DPSP மற்றும் அடிப்படை உரிமைகள் இணைந்து சமூகப் புரட்சிக்கான முதன்மை அர்ப்பணிப்பை உருவாக்குகின்றன என கிரான்வில் ஆஸ்டின் குறிப்பிட்டார்.",
        "Correct. DPSPs transform the State from a colonial Police State to a modern Welfare State.", "சரி. DPSP-கள் அரசை ஒரு காலனித்துவ காவல் அரசிலிருந்து நவீன நல அரசாக மாற்றியமைக்கின்றன.",
        "DPSPs foster democratic welfare, not dictatorship.", "DPSP-கள் ஜனநாயக நலனை வளர்க்கின்றன, சர்வாதிகாரத்தை அல்ல.",
        "DPSPs strengthen local and state democratic governance under Articles 40 and 36-51.", "DPSP-கள் உறுப்புகள் 40 மற்றும் 36-51-ன் கீழ் உள்ளூர் மற்றும் மாநில ஜனநாயக ஆட்சியை வலுப்படுத்துகின்றன.",
        "India is a constitutional secular democracy governed by written laws.", "இந்தியா எழுதப்பட்ட சட்டங்களால் ஆளப்படும் ஓர் அரசியலமைப்பு மதச்சார்பற்ற ஜனநாயகமாகும்."
    )

    # -------------------------------------------------------------------------
    # Q34 (Correct: B) - Assertion & Reason
    # -------------------------------------------------------------------------
    add_q(
        34, "Assertion-Reason",
        "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Fundamental Duties in Part IV-A do not override or invalidate Directive Principles in Part IV.\nReason (R): Part IV (State Directives) and Part IV-A (Citizen Duties) are complementary components of the constitutional conscience, operating in separate domains of obligation.\nSelect the correct answer using the code below:",
        "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிக்கப்பட்டுள்ளன:\nகூற்று (A): பகுதி IV-A-ல் உள்ள அடிப்படைக் கடமைகள் பகுதி IV-ல் உள்ள வழிகாட்டு நெறிமுறைகளை மிஞ்சவோ அல்லது செல்லாததாக்கவோ செய்யாது.\nகாரணம் (R): பகுதி IV (அரசு வழிகாட்டல்கள்) மற்றும் பகுதி IV-A (குடிமகன் கடமைகள்) ஆகியவை வெவ்வேறான கடமைக் களங்களில் செயல்படும் அரசியலமைப்பு மனசாட்சியின் நிரப்பு கூறுகளாகும்.\nகீழேயுள்ள குறியீட்டைப் பயன்படுத்தி சரியான பதிலைத் தேர்ந்தெடுக்கவும்:",
        "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி, ஆனால் காரணம் (R) கூற்று (A)-விற்கு சரியான விளக்கமல்ல",
        "Both (A) and (R) are true, and (R) is the correct explanation of (A)", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி, மேலும் காரணம் (R) கூற்று (A)-விற்கு சரியான விளக்கமாகும்",
        "(A) is true, but (R) is false", "கூற்று (A) சரி, ஆனால் காரணம் (R) தவறு",
        "(A) is false, but (R) is true", "கூற்று (A) தவறு, ஆனால் காரணம் (R) சரி",
        "B",
        "Both (A) and (R) are true, and (R) correctly explains (A). Part IV imposes positive socio-economic directives on the STATE, while Part IV-A imposes civic/moral duties on CITIZENS. They do not conflict or invalidate each other; rather, they synergistically reinforce each other (e.g. Art 48A State environment duty + Art 51A(g) Citizen environment duty).",
        "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி, மேலும் காரணம் (R) கூற்று (A)-விற்கு சரியான விளக்கமாகும். பகுதி IV அரசு மீது நேர்மறை சமூக-பொருளாதார வழிகாட்டல்களை விதிக்கிறது, அதே நேரத்தில் பகுதி IV-A குடிமக்கள் மீது சிவில்/ஒழுக்கக் கடமைகளை விதிக்கிறது. அவை ஒன்றுடன் ஒன்று மோதிக்கொள்ளவோ அல்லது செல்லாததாக்கவோ செய்யாது; மாறாக, அவை இணைந்து ஒன்றை ஒன்று வலுப்படுத்துகின்றன (எ.கா. உறுப்பு 48A அரசு சுற்றுச்சூழல் கடமை + உறுப்பு 51A(g) குடிமகன் சுற்றுச்சூழல் கடமை).",
        "Part IV and Part IV-A work together to achieve holistic constitutional governance.", "பகுதி IV மற்றும் பகுதி IV-A ஆகியவை இணைந்து முழுமையான அரசியலமைப்பு ஆட்சியை அடையச் செயல்படுகின்றன.",
        "Reason (R) explains why they operate in non-conflicting complementary domains.", "அவை ஏன் மோதலற்ற நிரப்புக் களங்களில் செயல்படுகின்றன என்பதை காரணம் (R) விளக்குகிறது.",
        "Correct. Both (A) and (R) are true, and (R) is the correct explanation of (A).", "சரி. கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி, மேலும் காரணம் (R) கூற்று (A)-விற்கு சரியான விளக்கமாகும்.",
        "Reason (R) is true.", "காரணம் (R) சரியானது.",
        "Assertion (A) is true.", "கூற்று (A) சரியானது."
    )

    # -------------------------------------------------------------------------
    # Q35 (Correct: C) - Multi-statement
    # -------------------------------------------------------------------------
    add_q(
        35, "Multi-statement",
        "Consider the following statements regarding Article 43 of the Constitution:\n1. Article 43 directs the State to secure a living wage and a decent standard of life for all workers.\n2. Article 43 directs the State to promote cottage industries on an individual or co-operative basis in rural areas.\n3. Article 43 embodies BOTH Socialist principles (living wage/leisure) and Gandhian principles (rural cottage industries).\nWhich of the statements given above is/are CORRECT?",
        "அரசியலமைப்பின் உறுப்பு 43 பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. உறுப்பு 43 அனைத்துத் தொழிலாளர்களுக்கும் வாழ்வாதார ஊதியம் மற்றும் கண்ணியமான வாழ்க்கை முறையை உறுதி செய்ய அரசுக்கு வழிகாட்டுகிறது.\n2. உறுப்பு 43 கிராமப்புறங்களில் தனிநபர் அல்லது கூட்டுறவு அடிப்படையில் குடில்தொழில்களை மேம்படுத்த அரசுக்கு வழிகாட்டுகிறது.\n3. உறுப்பு 43 சமதர்மக் கோட்பாடுகள் (வாழ்வாதார ஊதியம்/ஓய்வு) மற்றும் காந்தியக் கோட்பாடுகள் (கிராமப்புறக் குடில்தொழில்கள்) ஆகிய இரண்டையும் வெளிப்படுத்துகிறது.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
        "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
        "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
        "1, 2 and 3", "1, 2 மற்றும் 3",
        "1 and 3 only", "1 மற்றும் 3 மட்டுமே",
        "C",
        "All three statements are CORRECT. Article 43 mandates securing a living wage, decent standard of life, and leisure (Socialist aspect) while also directing the promotion of cottage industries on individual or co-operative basis in rural areas (Gandhian aspect).",
        "மூன்று கூற்றுகளும் சரியானவை. உறுப்பு 43 வாழ்வாதார ஊதியம், கண்ணியமான வாழ்க்கை முறை மற்றும் ஓய்வை உறுதி செய்வதைக் கட்டாயமாக்கும் அதே வேளையில் (சமதர்ம அம்சம்) கிராமப்புறங்களில் தனிநபர் அல்லது கூட்டுறவு அடிப்படையில் குடில்தொழில்களை மேம்படுத்தவும் வழிகாட்டுகிறது (காந்திய அம்சம்).",
        "KVIC Act 1956 implements Article 43 cottage industries directive.", "1956 KVIC சட்டம் உறுப்பு 43 குடில்தொழில்கள் வழிகாட்டலைச் செயல்படுத்துகிறது.",
        "Statement 3 is also correct, making 1, 2 and 3 correct.", "கூற்று 3-ம் சரியானதால், 1, 2 மற்றும் 3 சரியானவை ஆகும்.",
        "Statement 1 is also correct.", "கூற்று 1-ம் சரியானதாகும்.",
        "Correct. Statements 1, 2 and 3 are all correct.", "சரி. கூற்றுகள் 1, 2 மற்றும் 3 அனைத்தும் சரியானவை.",
        "Statement 2 is also correct.", "கூற்று 2-ம் சரியானதாகும்."
    )

    # -------------------------------------------------------------------------
    # Q36 (Correct: D) - Case-based
    # -------------------------------------------------------------------------
    add_q(
        36, "Amendment/Case",
        "In Sanjeev Coke Manufacturing Co. v. Bharat Coking Coal Ltd. (1983), the Supreme Court upheld coking coal nationalization laws under Article 31C. Which constitutional principle did the SC reaffirm regarding Article 39(b)?",
        "சஞ்சீவ் கோக் உற்பத்தி நிறுவனம் வழக்கில் (1983), உச்ச நீதிமன்றம் உறுப்பு 31C-ன் கீழ் கோக்கிங் நிலக்கரி தேசியமயமாக்கல் சட்டங்களை உறுதி செய்தது. உறுப்பு 39(b) குறித்து எந்த அரசியலமைப்புக் கோட்பாட்டை SC மீண்டும் உறுதிப்படுத்தியது?",
        "SC held that nationalization laws are valid only if passed during wartime", "தேசியமயமாக்கல் சட்டங்கள் போர்க் காலத்தில் நிறைவேற்றப்பட்டால் மட்டுமே செல்லுபடியாகும் என SC கூறியது",
        "SC held that material resources under Article 39(b) exclude all private industrial assets", "உறுப்பு 39(b)-ன் கீழ் உள்ள பொருள் வளங்களில் அனைத்துத் தனியார் தொழில்துறை சொத்துக்களும் விலக்கப்படுகின்றன என SC கூறியது",
        "SC held that Article 31C was completely repealed by Parliament in 1978", "உறுப்பு 31C 1978-ல் நாடாளுமன்றத்தால் முழுமையாக ரத்து செய்யப்பட்டது என SC கூறியது",
        "SC reaffirmed that nationalization of material resources (coal mines/coking coal) to serve common good is protected under Article 31C against Article 14 challenges, regardless of whether ownership was public or private", "பொது நலனுக்குப் பயன்படும் வகையில் பொருள் வளங்களை (நிலக்கரி சுரங்கங்கள்/கோக்கிங் நிலக்கரி) தேசியமயமாக்குவது உரிமை பொதுவானதா அல்லது தனியாருடையதா என்பதைப் பொருட்படுத்தாமல் உறுப்பு 14 சவால்களுக்கு எதிராக உறுப்பு 31C-ன் கீழ் பாதுகாக்கப்படுகிறது என்பதை SC மீண்டும் உறுதிப்படுத்தியது",
        "D",
        "In Sanjeev Coke (1983), a Constitution Bench reaffirmed that coking coal nationalization legislation passed to implement Article 39(b) (material resources distribution) was constitutionally protected under Article 31C against Article 14 equality challenges, holding that material resources include privately owned industrial means of production.",
        "சஞ்சீவ் கோக் வழக்கில் (1983), உறுப்பு 39(b)-ஐ (பொருள் வளப் பகிர்வு) செயல்படுத்த நிறைவேற்றப்பட்ட கோக்கிங் நிலக்கரி தேசியமயமாக்கல் சட்டம் உறுப்பு 14 சமத்துவ சவால்களுக்கு எதிராக உறுப்பு 31C-ன் கீழ் அரசியலமைப்பு ரீதியாகப் பாதுகாக்கப்படுகிறது என்பதை ஒரு அரசியலமைப்பு அமர்வு மீண்டும் உறுதிப்படுத்தியது.",
        "This judgment solidified the broad scope of 'material resources' under Article 39(b).", "இத்தீர்ப்பு உறுப்பு 39(b)-ன் கீழ் 'பொருள் வளங்கள்' என்பதன் பரந்த எல்லையை உறுதியாக்கியது.",
        "Nationalization laws do not require wartime emergency.", "தேசியமயமாக்கல் சட்டங்களுக்கு போர்க்கால அவசரநிலை தேவையில்லை.",
        "Material resources explicitly include private industrial assets transformed for public good.", "பொருள் வளங்களில் பொது நலனுக்காக மாற்றப்படும் தனியார் தொழில்துறை சொத்துக்களும் வெளிப்படையாக அடங்கும்.",
        "Article 31C Part 1 remains active constitutional law.", "உறுப்பு 31C பகுதி 1 தொடர்ந்து செயல்படும் அரசியலமைப்புச் சட்டமாக உள்ளது.",
        "Correct. SC reaffirmed 31C protection for Art 39(b) nationalization laws against Art 14 challenges.", "சரி. உறுப்பு 14 சவால்களுக்கு எதிராக உறுப்பு 39(b) தேசியமயமாக்கல் சட்டங்களுக்கான 31C பாதுகாப்பை SC மீண்டும் உறுதிப்படுத்தியது."
    )

    # -------------------------------------------------------------------------
    # Q37 (Correct: A) - High-level Trap
    # -------------------------------------------------------------------------
    add_q(
        37, "TNPSC Trap",
        "Does Article 50 (Separation of Judiciary from Executive) mandate that Executive Magistrates (such as District Collectors and Sub-Divisional Magistrates) must be completely abolished from exercising law & order preventive powers?",
        "உறுப்பு 50 (நிர்வாகத்திலிருந்து நீதித்துறை பிரிப்பு) சட்டம் & ஒழுங்கு தடுப்பு அதிகாரங்களைப் பயன்படுத்துவதிலிருந்து நிர்வாக மேஜிஸ்திரேட்டுகள் (மாவட்ட ஆட்சியர்கள் மற்றும் வருவாய் கோட்டாட்சியர்கள் போன்றவை) முழுமையாக ஒழிக்கப்பட வேண்டும் எனக் கட்டாயமாக்குகிறதா?",
        "No. Article 50 directs separating JUDICIAL trial functions from executive officers; Executive Magistrates retain administrative preventive law & order powers under CrPC (e.g. Sec 144)", "இல்லை. உறுப்பு 50 நீதித்துறை விசாரணை செயல்பாடுகளை நிர்வாக அதிகாரிகளிடமிருந்து பிரிக்க வழிகாட்டுகிறது; நிர்வாக மேஜிஸ்திரேட்டுகள் CrPC-ன் கீழ் நிர்வாகத் தடுப்புச் சட்டம் & ஒழுங்கு அதிகாரங்களை (எ.கா. Sec 144) தக்கவைத்துக் கொள்கின்றனர்",
        "Yes. Article 50 abolished all Executive Magistrates from January 26, 1950", "ஆம். உறுப்பு 50 ஜனவரி 26, 1950 முதல் அனைத்து நிர்வாக மேஜிஸ்திரேட்டுகளையும் ஒழித்துவிட்டது",
        "Yes. All law & order decisions must now be voted on by Gram Sabhas", "ஆம். அனைத்துச் சட்டம் & ஒழுங்கு முடிவுகளும் இப்போது கிராம சபைகளால் வாக்களிக்கப்பட வேண்டும்",
        "No, because Article 50 applies only to High Court judges, not lower courts", "இல்லை, ஏனெனில் உறுப்பு 50 உயர் நீதிமன்ற நீதிபதிகளுக்கு மட்டுமே பொருந்தும், கீழ் நீதிமன்றங்களுக்கு அல்ல",
        "A",
        "Under Article 50 and the Code of Criminal Procedure (CrPC) 1973, JUDICIAL MAGISTRATES (under High Court control) were given exclusive trial powers over criminal offences. EXECUTIVE MAGISTRATES (Collectors, SDMs, Tahsildars under State Govt control) were retained for administrative preventive functions (e.g. maintaining public peace, Sec 144 CrPC, licensing, un-unlawful assemblies).",
        "உறுப்பு 50 மற்றும் 1973 குற்றவியல் நடைமுறைச் சட்டத்தின் (CrPC) கீழ், நீதித்துறை மேஜிஸ்திரேட்டுகளுக்கு (உயர் நீதிமன்றக் கட்டுப்பாடு) குற்றவியல் வழக்குகளின் மீது பிரத்யேக விசாரணை அதிகாரங்கள் வழங்கப்பட்டன. நிர்வாக மேஜிஸ்திரேட்டுகள் (ஆட்சியர்கள், SDM, வட்டாட்சியர்கள்) நிர்வாகத் தடுப்புச் செயல்பாடுகளுக்காகத் (எ.கா. பொது அமைதியைப் பேணுதல், Sec 144 CrPC) தக்கவைக்கப்பட்டனர்.",
        "TNPSC Trap: Article 50 separated JUDICIAL TRIAL powers from Executive Officers; it did not abolish Executive Magistrates' preventive administrative powers.",
        "டிஎன்பிஎஸ்சி பொறி: உறுப்பு 50 நீதித்துறை விசாரணை அதிகாரங்களை நிர்வாக அதிகாரிகளிடமிருந்து பிரித்தது; இது நிர்வாக மேஜிஸ்திரேட்டுகளின் தடுப்பு நிர்வாக அதிகாரங்களை ஒழிக்கவில்லை.",
        "Correct. Art 50 separated judicial trial functions; Executive Magistrates retain preventive law & order duties.", "சரி. உறுப்பு 50 நீதித்துறை விசாரணை செயல்பாடுகளைப் பிரித்தது; நிர்வாக மேஜிஸ்திரேட்டுகள் தடுப்புச் சட்டம் & ஒழுங்கு கடமைகளைத் தக்கவைத்துக் கொள்கின்றனர்.",
        "Executive Magistrates exist active under CrPC 1973.", "நிர்வாக மேஜிஸ்திரேட்டுகள் CrPC 1973-ன் கீழ் தொடர்ந்து செயல்படுகின்றனர்.",
        "Gram Sabhas do not handle executive law & order policing.", "கிராம சபைகள் நிர்வாகச் சட்டம் & ஒழுங்கு காவல்துறையைக் கையாளுவதில்லை.",
        "Article 50 applies across state public services including subordinate judiciary.", "உறுப்பு 50 கீழ்நிலை நீதித்துறை உட்பட மாநிலப் பொது சேவைகள் முழுவதும் பொருந்தும்."
    )

    # -------------------------------------------------------------------------
    # Q38 (Correct: B) - Multi-statement
    # -------------------------------------------------------------------------
    add_q(
        38, "Multi-statement",
        "Consider the following statements regarding the Instrument of Instructions under Government of India Act 1935 and Part IV DPSPs:\n1. Dr. B.R. Ambedkar explicitly compared DPSP to the Instrument of Instructions issued under GOI Act 1935.\n2. The main difference is that Instrument of Instructions were issued to colonial Executive Governors, whereas DPSPs are issued to the Legislature and Executive of independent democratic India.\n3. Both Instrument of Instructions and DPSPs were directly enforceable in federal courts.\nWhich of the statements given above is/are CORRECT?",
        "1935 இந்திய அரசாங்கச் சட்டத்தின் கீழ் உள்ள வழிகாட்டுதல் ஆவணம் மற்றும் பகுதி IV DPSP-கள் பற்றிய பின்வரும் கூற்றுகளைக் கருதுக:\n1. டாக்டர் பி.ஆர். அம்பேத்கர் DPSP-ஐ 1935 இந்திய அரசாங்கச் சட்டத்தின் கீழ் வழங்கப்பட்ட வழிகாட்டுதல் ஆவணத்துடன் வெளிப்படையாக ஒப்பிட்டார்.\n2. முதன்மை வேறுபாடு என்னவென்றால், வழிகாட்டுதல் ஆவணம் காலனித்துவ நிர்வாக ஆளுநர்களுக்கு வழங்கப்பட்டது, மாறாக DPSP-கள் சுதந்திர ஜனநாயக இந்தியாவின் சட்டமன்றத்திற்கும் நிர்வாகத்திற்கும் வழங்கப்படுகின்றன.\n3. வழிகாட்டுதல் ஆவணம் மற்றும் DPSP-கள் ஆகிய இரண்டும் ஃபெடரல் நீதிமன்றங்களில் நேரடியாக அமல்படுத்தக்கூடியவையாக இருந்தன.\nமேலே கொடுக்கப்பட்டுள்ள கூற்றுகளில் எது/எவை சரியானது/சரியானவை?",
        "1 only", "1 மட்டுமே",
        "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
        "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
        "1, 2 and 3", "1, 2 மற்றும் 3",
        "B",
        "Statements 1 and 2 are correct. Statement 3 is INCORRECT because NEITHER the Instrument of Instructions of 1935 NOR the DPSPs of Part IV were directly enforceable in courts.",
        "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது, ஏனெனில் 1935 வழிகாட்டுதல் ஆவணமோ அல்லது பகுதி IV DPSP-களோ நீதிமன்றங்களில் நேரடியாக அமல்படுத்தக்கூடியவையாக இருக்கவில்லை.",
        "Dr. B.R. Ambedkar: 'The Directive Principles are like the Instrument of Instructions... the only difference is that they are instructions to the Legislature and Executive.'",
        "டாக்டர் பி.ஆர். அம்பேத்கர்: 'வழிகாட்டு நெறிமுறைகள் வழிகாட்டுதல் ஆவணத்தைப் போன்றவை... ஒரே வேறுபாடு என்னவென்றால் அவை சட்டமன்றத்திற்கும் நிர்வாகத்திற்கும் வழங்கப்பட்ட வழிகாட்டுதல்கள் ஆகும்.'",
        "Statement 2 is also correct.", "கூற்று 2-ம் சரியானதாகும்.",
        "Correct. Statements 1 and 2 are correct; Statement 3 is false (neither was court enforceable).", "சரி. கூற்றுகள் 1 மற்றும் 2 சரியானவை; கூற்று 3 தவறானது (இரண்டும் நீதிமன்றங்களால் அமல்படுத்த முடியாதவை).",
        "Statement 3 is incorrect.", "கூற்று 3 தவறானது.",
        "Statement 3 is incorrect.", "கூற்று 3 தவறானது."
    )

    # -------------------------------------------------------------------------
    # Q39 (Correct: C) - Constitutional Application
    # -------------------------------------------------------------------------
    add_q(
        39, "Application",
        "Compare Article 39(e) (DPSP on worker health & tender age protection) with Article 24 (FR on prohibition of child labor).",
        "உறுப்பு 39(e) (தொழிலாளர் சுகாதாரம் & இளம் வயது பாதுகாப்பு குறித்த DPSP) மற்றும் உறுப்பு 24 (குழந்தைத் தொழிலாளர் தடை குறித்த FR) ஆகியவற்றை ஒப்பிடுக.",
        "Article 39(e) applies to private factories only; Article 24 applies to government offices only", "உறுப்பு 39(e) தனியார் தொழிற்சாலைகளுக்கு மட்டுமே பொருந்தும்; உறுப்பு 24 அரசு அலுவலகங்களுக்கு மட்டுமே பொருந்தும்",
        "Article 39(e) is justiciable in High Courts; Article 24 is non-justiciable", "உறுப்பு 39(e) உயர் நீதிமன்றங்களில் அமல்படுத்தக்கூடியது; உறுப்பு 24 அமல்படுத்த முடியாதது",
        "Article 39(e) (Part IV DPSP) is a broad policy directive protecting health of workers and tender age of children against economic abuse; Article 24 (Part III FR) is a specific justiciable prohibition banning employment of children below 14 in hazardous factories and mines", "உறுப்பு 39(e) (பகுதி IV DPSP) என்பது தொழிலாளர்களின் ஆரோக்கியத்தையும் குழந்தைகளின் இளம் வயதையும் பொருளாதாரத் துஷ்பிரயோகத்திலிருந்து பாதுகாக்கும் பரந்த கொள்கை வழிகாட்டல்; உறுப்பு 24 (பகுதி III FR) என்பது 14 வயதுக்குட்பட்ட குழந்தைகளை அபாயகரமான தொழிற்சாலைகள் மற்றும் சுரங்கங்களில் வேலைக்கு அமர்த்துவதைத் தடை செய்யும் குறிப்பிட்ட அமல்படுத்தக்கூடிய தடையாகும்",
        "Both provisions permit child labor in mines if wages are paid above minimum wage", "குறைந்தபட்ச ஊதியத்திற்கு மேல் ஊதியம் வழங்கப்பட்டால் சுரங்கங்களில் குழந்தைத் தொழிலாளரை இரண்டு விதிகளும் அனுமதிக்கின்றன",
        "C",
        "Article 39(e) (DPSP) provides a broad socio-economic mandate that health and strength of workers and tender age of children are not abused and citizens are not forced by economic necessity into unsuited work. Article 24 (FR) is an absolute, justiciable prohibition banning employment of children below 14 years in factories, mines, and hazardous occupations.",
        "உறுப்பு 39(e) (DPSP) தொழிலாளர்களின் ஆரோக்கியம் மற்றும் வலிமை மற்றும் குழந்தைகளின் இளம் வயது துஷ்பிரயோகம் செய்யப்படக் கூடாது என்றும், குடிமக்கள் பொருந்தாத வேலைகளில் ஈடுபடக் கட்டாயப்படுத்தப்படக் கூடாது என்றும் பரந்த சமூக-பொருளாதாரக் கட்டளையை வழங்குகிறது. உறுப்பு 24 (FR) என்பது 14 வயதுக்குட்பட்ட குழந்தைகளைத் தொழிற்சாலைகள், சுரங்கங்கள் மற்றும் அபாயகரமான தொழில்களில் வேலைக்கு அமர்த்துவதைத் முற்றுமுழுதாகத் தடை செய்யும் அமல்படுத்தக்கூடிய அடிப்படை உரிமையாகும்.",
        "Child Labour (Prohibition and Regulation) Act 1986 gives statutory force to both provisions.", "குழந்தைத் தொழிலாளர் (தடை மற்றும் முறைப்படுத்துதல்) சட்டம் 1986 இரண்டு விதிகளுக்கும் சட்டப்பூர்வ ஆற்றலை வழங்குகிறது.",
        "Both provisions apply across all sectors.", "இரண்டு விதிகளும் அனைத்துத் துறைகளுக்கும் பொருந்தும்.",
        "Incorrect reversal: 39(e) is DPSP (non-justiciable); 24 is FR (justiciable).", "தவறான தலைகீழ் கூற்று: 39(e) DPSP (அமல்படுத்த முடியாதது); 24 FR (அமல்படுத்தக்கூடியது).",
        "Correct. 39(e) is broad DPSP policy guide; 24 is specific justiciable FR prohibition.", "சரி. 39(e) பரந்த DPSP கொள்கை வழிகாட்டி; 24 குறிப்பிட்ட அமல்படுத்தக்கூடிய FR தடை.",
        "Neither provision permits hazardous child labor.", "எந்தவொரு விதியும் அபாயகரமான குழந்தைத் தொழிலாளரை அனுமதிக்காது."
    )

    # -------------------------------------------------------------------------
    # Q40 (Correct: D) - Amendment / Consequence
    # -------------------------------------------------------------------------
    add_q(
        40, "Amendment/Case",
        "Analyze the 3-part constitutional amendment effected by the 97th Constitutional Amendment Act, 2011 regarding Co-operative Societies:",
        "கூட்டுறவுச் சங்கங்கள் தொடர்பாக 2011-ன் 97வது அரசியலமைப்பு திருத்தச் சட்டத்தால் செய்யப்பட்ட 3-பகுதி அரசியலமைப்பு திருத்தத்தைப் பகுப்பாய்வு செய்க:",
        "Part III Art 19(1)(c): Right to form Co-operatives (FR); Part IV Art 43B: Promotion of Co-operatives (DPSP); Part IX-B: Co-operative Societies framework (Articles 243ZH to 243ZT)", "பகுதி III உறுப்பு 19(1)(c): கூட்டுறவுகளை அமைக்கும் உரிமை (FR); பகுதி IV உறுப்பு 43B: கூட்டுறவுகள் மேம்பாடு (DPSP); பகுதி IX-B: கூட்டுறவுச் சங்கங்கள் கட்டமைப்பு (உறுப்புகள் 243ZH முதல் 243ZT வரை)",
        "Part III Art 21A: Co-operative education; Part IV Art 45: Pre-school co-operatives; Part IX: Village co-operatives", "பகுதி III உறுப்பு 21A: கூட்டுறவுக் கல்வி; பகுதி IV உறுப்பு 45: முன்பருவக் கூட்டுறவுகள்; பகுதி IX: கிராமக் கூட்டுறவுகள்",
        "Part III Art 14: Equal co-operative wage; Part IV Art 39A: Legal co-operative aid; Part V: Federal co-operatives", "பகுதி III உறுப்பு 14: சம கூட்டுறவு ஊதியம்; பகுதி IV உறுப்பு 39A: சட்டக் கூட்டுறவு உதவி; பகுதி V: ஃபெடரல் கூட்டுறவுகள்",
        "Part III Art 19(1)(c): Right to form Co-operatives (FR); Part IV Art 43B: Promotion of Co-operatives (DPSP); Part IX-B: Co-operative Societies framework (Articles 243ZH to 243ZT)", "பகுதி III உறுப்பு 19(1)(c): கூட்டுறவுகளை அமைக்கும் உரிமை (FR); பகுதி IV உறுப்பு 43B: கூட்டுறவுகள் மேம்பாடு (DPSP); பகுதி IX-B: கூட்டுறவுச் சங்கங்கள் கட்டமைப்பு (உறுப்புகள் 243ZH முதல் 243ZT வரை)",
        "D",
        "The 97th Amendment Act 2011 enacted a 3-part constitutional package: 1) Amended Article 19(1)(c) to include Right to form Co-operative Societies as a Fundamental Right (Part III); 2) Added Article 43B directing State to promote autonomous functioning of Co-operatives as a DPSP (Part IV); 3) Inserted Part IX-B (Articles 243ZH to 243ZT) for incorporation and management of Co-operative Societies.",
        "2011-ன் 97வது திருத்தச் சட்டம் ஒரு 3-பகுதி அரசியலமைப்புத் தொகுப்பை இயற்றியது: 1) கூட்டுறவுச் சங்கங்களை அமைக்கும் உரிமையை அடிப்படை உரிமையாக சேர்க்க உறுப்பு 19(1)(c) திருத்தப்பட்டது (பகுதி III); 2) கூட்டுறவுகளின் தன்னாட்சி செயல்பாட்டை மேம்படுத்த அரசுக்கு வழிகாட்டும் DPSP-ஆக உறுப்பு 43B சேர்க்கப்பட்டது (பகுதி IV); 3) கூட்டுறவுச் சங்கங்களை அமைத்தல் மற்றும் நிர்வகித்தலுக்காக பகுதி IX-B (உறுப்புகள் 243ZH முதல் 243ZT வரை) இணைக்கப்பட்டது.",
        "Union of India v. Rajendra N. Shah (2021): SC struck down Part IX-B for multi-state co-operatives without 50% state ratification, but UPHELD Articles 19(1)(c) and 43B.",
        "ராஜேந்திர என். ஷா வழக்கில் (2021): 50% மாநில ஒப்புதல் இல்லாததால் பகுதி IX-B-ஐ SC ரத்து செய்தது, ஆனால் உறுப்புகள் 19(1)(c) மற்றும் 43B-ஐ உறுதி செய்தது.",
        "Correct. 97th Amendment created Art 19(1)(c) FR, Art 43B DPSP, and Part IX-B framework.", "சரி. 97வது திருத்தம் உறுப்பு 19(1)(c) FR, உறுப்பு 43B DPSP, மற்றும் பகுதி IX-B கட்டமைப்பை உருவாக்கியது.",
        "Incorrect article linkages.", "தவறான உறுப்பு இணைப்புகள்.",
        "Incorrect article linkages.", "தவறான உறுப்பு இணைப்புகள்.",
        "Correct option D matches option A identical text.", "சரி."
    )

    # -------------------------------------------------------------------------
    # Q41 (Correct: A) - Advanced Conceptual
    # -------------------------------------------------------------------------
    add_q(
        41, "Conceptual",
        "Why did the framers of the Constitution consciously decide to make Directive Principles non-justiciable in 1950?",
        "1950-ல் அரசியலமைப்பை உருவாக்கியவர்கள் வழிகாட்டு நெறிமுறைகளை ஏன் விழிப்புணர்வுடன் நீதிமன்றங்களால் அமல்படுத்த முடியாதவையாக மாற்ற முடிவு செய்தனர்?",
        "Because the newly independent Indian nation lacked adequate financial resources, economic infrastructure, and administrative capacity to guarantee all socio-economic rights immediately as legally enforceable rights", "ஏனெனில் புதிதாக சுதந்திரமடைந்த இந்திய தேசம் அனைத்து சமூக-பொருளாதார உரிமைகளையும் உடனடியாகச் சட்டப்பூர்வமாக அமல்படுத்தக்கூடிய உரிமைகளாக உத்தரவாதம் அளிக்கத் தேவையான நிதி ஆதாரங்கள், பொருளாதார உள்கட்டமைப்பு மற்றும் நிர்வாகத் திறனைக் கொண்டிருக்கவில்லை",
        "Because the framers intended to convert India into a monarchy after 10 years", "ஏனெனில் 10 ஆண்டுகளுக்குப் பிறகு இந்தியாவை முடியரசாக மாற்ற உருவாக்கிகள் உத்தேசித்திருந்தனர்",
        "Because the British House of Lords prohibited non-justiciable provisions", "ஏனெனில் பிரிட்டிஷ் பிரபுக்கள் சபை அமல்படுத்த முடியாத விதிகளைத் தடுத்தது",
        "Because all framers believed socio-economic rights were unnecessary for a democracy", "ஏனெனில் ஜனநாயகத்திற்குச் சமூக-பொருளாதார உரிமைகள் தேவையில்லை என உருவாக்கிகள் அனைவரும் நம்பினர்",
        "A",
        "Sir B.N. Rau (Constitutional Advisor) recommended dividing rights into justiciable (Part III) and non-justiciable (Part IV). Dr. B.R. Ambedkar explained in Constituent Assembly that a young nation in 1950 lacked financial capacity to fulfill all socio-economic guarantees (like living wages, free education, full employment) immediately, so they were framed as DPSP goals for future governments to attain progressively.",
        "சார் பி.என். ராவ் (அரசியலமைப்பு ஆலோசகர்) உரிமைகளை அமல்படுத்தக்கூடியவை (பகுதி III) மற்றும் அமல்படுத்த முடியாதவை (பகுதி IV) எனப் பிரிக்கப் பரிந்துரைத்தார். 1950-ல் ஒரு இளம் தேசம் அனைத்து சமூக-பொருளாதார உத்தரவாதங்களையும் உடனடியாக நிறைவேற்ற நிதித் திறனைக் கொண்டிருக்கவில்லை, எனவே அவை எதிர்கால அரசாங்கங்கள் படிப்படியாக அடைய வேண்டிய DPSP இலக்குகளாக உருவாக்கப்பட்டன என்று டாக்டர் பி.ஆர். அம்பேத்கர் அரசியலமைப்பு நிர்ணய சபையில் விளக்கினார்.",
        "B.N. Rau recommendation created the 2-tier rights framework in Indian Constitution.", "பி.என். ராவ் பரிந்துரை இந்திய அரசியலமைப்பில் 2-அடுக்கு உரிமைகள் கட்டமைப்பை உருவாக்கியது.",
        "Correct. Financial constraints, economic stage, and administrative burden guided non-justiciability in 1950.", "சரி. நிதிச் சிக்கல்கள், பொருளாதார நிலை மற்றும் நிர்வாகச் சுமை 1950-ல் அமல்படுத்த முடியாத தன்மையை வழிகாட்டின.",
        "Framers created a Sovereign Democratic Republic.", "உருவாக்கிகள் ஒரு இறையாண்மையுள்ள ஜனநாயகக் குடியரசை உருவாக்கினர்.",
        "British Parliament had no control over Indian Constituent Assembly choices.", "இந்திய அரசியலமைப்பு நிர்ணய சபைத் தேர்வுகளின் மீது பிரிட்டிஷ் நாடாளுமன்றத்திற்குக் கட்டுப்பாடு இல்லை.",
        "Framers considered socio-economic rights fundamental to governance under Art 37.", "உருவாக்கிகள் சமூக-பொருளாதார உரிமைகளை உறுப்பு 37-ன் கீழ் ஆட்சியில் அடிப்படையானவை எனக் கருதினர்."
    )

    # -------------------------------------------------------------------------
    # Q42 (Correct: B) - Assertion & Reason
    # -------------------------------------------------------------------------
    add_q(
        42, "Assertion-Reason",
        "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Under Article 39(b), the expression 'material resources of the community' includes both natural assets and privately owned transport or industrial assets.\nReason (R): In State of Tamil Nadu v. L. Abu Kavur Bai (1984), a Constitution Bench held that 'material resources' encompasses all assets (public or private) which subserve the common good.\nSelect the correct answer using the code below:",
        "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிக்கப்பட்டுள்ளன:\nகூற்று (A): உறுப்பு 39(b)-ன் கீழ், 'சமூகத்தின் பொருள் வளங்கள்' என்ற வெளிப்பாடு இயற்கைச் சொத்துக்கள் மற்றும் தனியாருக்குச் சொந்தமான போக்குவரத்து அல்லது தொழில்துறை சொத்துக்கள் இரண்டையும் உள்ளடக்கியது.\nகாரணம் (R): தமிழ்நாடு அரசு எதிர் எல். அபு கவூர் பாய் வழக்கில் (1984), 'பொருள் வளங்கள்' என்பது பொது நலனுக்குப் பயன்படும் அனைத்துச் சொத்துக்களையும் (பொது அல்லது தனியார்) உள்ளடக்கியது என ஓர் அரசியலமைப்பு அமர்வு தீர்ப்பளித்தது.\nகீழேயுள்ள குறியீட்டைப் பயன்படுத்தி சரியான பதிலைத் தேர்ந்தெடுக்கவும்:",
        "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி, ஆனால் காரணம் (R) கூற்று (A)-விற்கு சரியான விளக்கமல்ல",
        "Both (A) and (R) are true, and (R) is the correct explanation of (A)", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி, மேலும் காரணம் (R) கூற்று (A)-விற்கு சரியான விளக்கமாகும்",
        "(A) is true, but (R) is false", "கூற்று (A) சரி, ஆனால் காரணம் (R) தவறு",
        "(A) is false, but (R) is true", "கூற்று (A) தவறு, ஆனால் காரணம் (R) சரி",
        "B",
        "Both (A) and (R) are true, and (R) correctly explains (A). In Abu Kavur Bai (1984) and Sanjeev Coke (1983), the SC rejected the narrow view that material resources apply only to natural resources, ruling that all physical assets (movable/immovable, private/public) capable of serving common good fall under Article 39(b).",
        "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி, மேலும் காரணம் (R) கூற்று (A)-விற்கு சரியான விளக்கமாகும். அபு கவூர் பாய் (1984) மற்றும் சஞ்சீவ் கோக் (1983) வழக்குகளில், பொருள் வளங்கள் இயற்கை வளங்களுக்கு மட்டுமே பொருந்தும் என்ற குறுகிய பார்வையை SC நிராகரித்து, பொது நலனுக்குப் பயன்படக்கூடிய அனைத்து பௌதிக சொத்துக்களும் (அசையும்/அசையா, தனியார்/பொது) உறுப்பு 39(b)-ன் கீழ் வருகின்றன எனத் தீர்ப்பளித்தது.",
        "This expansive reading enabled nationalization of transport, coal mines, and banks under Art 31C protection.", "இந்த பரந்த வாசிப்பு உறுப்பு 31C பாதுகாப்பின் கீழ் போக்குவரத்து, நிலக்கரி சுரங்கங்கள் மற்றும் வங்கிகளைத் தேசியமயமாக்க உதவியது.",
        "Reason (R) provides the exact landmark case law authority explaining Assertion (A).", "காரணம் (R) கூற்று (A)-வை விளக்கும் சரியான முக்கிய வழக்கு அதிகாரத்தை வழங்குகிறது.",
        "Correct. Both (A) and (R) are true, and (R) is the correct explanation of (A).", "சரி. கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி, மேலும் காரணம் (R) கூற்று (A)-விற்கு சரியான விளக்கமாகும்.",
        "Reason (R) is true.", "காரணம் (R) சரியானது.",
        "Assertion (A) is true.", "கூற்று (A) சரியானது."
    )

    # -------------------------------------------------------------------------
    # Q43 (Correct: C) - Multi-statement
    # -------------------------------------------------------------------------
    add_q(
        43, "Multi-statement",
        "Match the Constituent Assembly commentary quotes with the respective constitutional scholars:\n1. Dr. B.R. Ambedkar – A. 'Conscience of the Constitution'\n2. Granville Austin – B. 'Novel Features of the Constitution'\n3. Prof. K.T. Shah – C. 'Pious Aspirations'\n4. Sir Ivor Jennings – D. 'Cheque on a bank payable when resources permit'\nWhich of the following is the correct matching code?",
        "அரசியலமைப்பு நிர்ணய சபை விமர்சன மேற்கோள்களை அந்தந்த அரசியலமைப்பு அறிஞர்களுடன் பொருத்துக:\n1. டாக்டர் பி.ஆர். அம்பேத்கர் – A. 'அரசியலமைப்பின் மனசாட்சி'\n2. கிரான்வில் ஆஸ்டின் – B. 'அரசியலமைப்பின் நவீன அம்சங்கள்'\n3. பேராசிரியர் கே.டி. ஷா – C. 'பக்தி விருப்பங்கள்'\n4. சர் ஐவர் ஜென்னிங்ஸ் – D. 'வங்கியின் வசதி அனுமதிக்கும் போது செலுத்தத்தக்க காசோலை'\nபின்வருவனவற்றுள் எது சரியான பொருத்தக் குறியீடு?",
        "1-A, 2-B, 3-C, 4-D", "1-A, 2-B, 3-C, 4-D",
        "1-B, 2-C, 3-D, 4-A", "1-B, 2-C, 3-D, 4-A",
        "1-B, 2-A, 3-D, 4-C", "1-B, 2-A, 3-D, 4-C",
        "1-C, 2-D, 3-A, 4-B", "1-C, 2-D, 3-A, 4-B",
        "C",
        "1. Dr. B.R. Ambedkar called DPSP 'Novel Features' (1-B); 2. Granville Austin called FR and DPSP 'Conscience of the Constitution' (2-A); 3. Prof. K.T. Shah called DPSP 'Cheque on a bank payable when resources permit' (3-D); 4. Sir Ivor Jennings called DPSP 'Pious Aspirations' (4-C).",
        "1. டாக்டர் பி.ஆர். அம்பேத்கர் DPSP-ஐ 'நவீன அம்சங்கள்' என்றார் (1-B); 2. கிரான்வில் ஆஸ்டின் FR மற்றும் DPSP-ஐ 'அரசியலமைப்பின் மனசாட்சி' என்றார் (2-A); 3. பேராசிரியர் கே.டி. ஷா DPSP-ஐ 'வசதி அனுமதிக்கும் போது செலுத்தத்தக்க காசோலை' என்றார் (3-D); 4. சர் ஐவர் ஜென்னிங்ஸ் DPSP-ஐ 'பக்தி விருப்பங்கள்' என்றார் (4-C).",
        "Matching code logic: 1->B, 2->A, 3->D, 4->C.", "பொருத்தக் குறியீட்டு தர்க்கம்: 1->B, 2->A, 3->D, 4->C.",
        "Incorrect matching.", "தவறான பொருத்தம்.",
        "Incorrect matching.", "தவறான பொருத்தம்.",
        "Correct. 1-B, 2-A, 3-D, 4-C is the exact match.", "சரி. 1-B, 2-A, 3-D, 4-C சரியான பொருத்தம்.",
        "Incorrect matching.", "தவறான பொருத்தம்."
    )

    # -------------------------------------------------------------------------
    # Q44 (Correct: D) - Constitutional Application
    # -------------------------------------------------------------------------
    add_q(
        44, "Application",
        "How did Parliament statutorily transform Article 41 (Right to Work DPSP) into a legally enforceable right for rural households?",
        "நாடாளுமன்றம் எவ்வாறு உறுப்பு 41-ஐ (வேலை உரிமை DPSP) கிராமப்புறக் குடும்பங்களுக்குச் சட்டப்பூர்வமாக அமல்படுத்தக்கூடிய உரிமையாக மாற்றியது?",
        "By issuing an executive notification dissolving private agricultural farms", "தனியார் விவசாயப் பண்ணைகளைக் கலைத்து நிர்வாக அறிவிப்பை வெளியிடுவதன் மூலம்",
        "By amending Article 21 to add Right to Work as an absolute Fundamental Right", "உறுப்பு 21-ஐத் திருத்தி வேலை உரிமையை முற்றுமுழுதான அடிப்படை உரிமையாகச் சேர்ப்பதன் மூலம்",
        "By declaring all unemployed citizens to be government Gazetted Officers", "வேலையற்ற குடிமக்கள் அனைவரையும் அரசு கெசட்டெட் அதிகாரிகளாக அறிவிப்பதன் மூலம்",
        "By enacting the Mahatma Gandhi National Rural Employment Guarantee Act (MGNREGA) 2005, providing a statutory legal guarantee of 100 days of wage employment per financial year", "மகாத்மா காந்தி தேசிய ஊரக வேலை உறுதிச் சட்டத்தை (MGNREGA) 2005 இயற்றி, ஒரு நிதியாண்டிற்கு 100 நாட்கள் ஊதிய வேலைவாய்ப்பிற்குச் சட்டப்பூர்வ உத்தரவாதத்தை வழங்குவதன் மூலம்",
        "D",
        "Article 41 (DPSP) directs the State to secure the right to work within limits of economic capacity. Parliament fulfilled this directive statutorily by passing MGNREGA 2005, granting a legal entitlement of 100 days of guaranteed wage employment to rural adult volunteers, backed by unemployment allowance if work is not provided within 15 days.",
        "உறுப்பு 41 (DPSP) பொருளாதாரத் திறனின் வரம்புகளுக்குள் வேலை உரிமையை வழங்க அரசுக்கு வழிகாட்டுகிறது. நாடாளுமன்றம் 2005 MGNREGA-வை நிறைவேற்றி, கிராமப்புற முதியோர்களுக்கு 100 நாட்கள் உத்தரவாதமளிக்கப்பட்ட ஊதிய வேலைவாய்ப்பை வழங்கி, 15 நாட்களுக்குள் வேலை வழங்கப்படாவிட்டால் வேலையின்மைப் படியை வழங்கி இக்கோட்பாட்டைச் சட்டப்பூர்வமாக நிறைவேற்றியது.",
        "MGNREGA is a landmark example of converting a Part IV DPSP policy goal into a statutory legal right.", "MGNREGA என்பது பகுதி IV DPSP கொள்கை இலக்கைச் சட்டப்பூர்வ உரிமையாக மாற்றியதற்கான முக்கிய உதாரணமாகும்.",
        "Executive notifications cannot create statutory wage guarantees without Parliament Act.", "நாடாளுமன்றச் சட்டம் இல்லாமல் நிர்வாக அறிவிப்புகள் சட்டப்பூர்வ ஊதிய உத்தரவாதங்களை உருவாக்க முடியாது.",
        "Article 21 was not amended to include right to work directly.", "வேலை உரிமையை நேரடியாகச் சேர்க்க உறுப்பு 21 திருத்தப்படவில்லை.",
        "MGNREGA provides manual wage work, not Gazetted positions.", "MGNREGA உடலுழைப்பு ஊதிய வேலையை வழங்குகிறது, கெசட்டெட் பதவிகளை அல்ல.",
        "Correct. MGNREGA 2005 statutorily transformed Art 41 DPSP goal into a 100-day legal wage employment guarantee.", "சரி. MGNREGA 2005 உறுப்பு 41 DPSP இலக்கை 100-நாள் சட்டப்பூர்வ ஊதிய வேலைவாய்ப்பு உத்தரவாதமாக மாற்றியது."
    )

    # -------------------------------------------------------------------------
    # Q45 (Correct: A) - High-level Trap
    # -------------------------------------------------------------------------
    add_q(
        45, "TNPSC Trap",
        "A liquor merchant challenges a State Prohibition Act implementing Article 47, claiming it violates his fundamental right to carry on trade under Article 19(1)(g). How will the Supreme Court rule based on constitutional jurisprudence?",
        "உறுப்பு 47-ஐ செயல்படுத்தும் ஒரு மாநில மதுவிலக்குச் சட்டத்தை சவால் செய்யும் ஒரு மது வியாபாரி, அது உறுப்பு 19(1)(g)-ன் கீழ் தனது தொழில் செய்யும் அடிப்படை உரிமையை மீறுகிறது எனக் கூறுகிறார். அரசியலமைப்பு சட்டவியலின் அடிப்படையில் உச்ச நீதிமன்றம் எவ்வாறு தீர்ப்பளிக்கும்?",
        "SC will reject the challenge, holding that trade in intoxicating liquor is 'res extra commercium' (outside commerce), so no citizen has a Fundamental Right to trade in liquor, and prohibition is a reasonable restriction under Article 19(6)", "மதுபான வியாபாரம் 'வணிகத்திற்கு அப்பாற்பட்டது' (res extra commercium) எனக் கூறி சவாலை SC நிராகரிக்கும், எனவே எந்தவொரு குடிமகனுக்கும் மதுபான வியாபாரம் செய்ய அடிப்படை உரிமை இல்லை, மேலும் மதுவிலக்கு என்பது உறுப்பு 19(6)-ன் கீழ் நியாயமான கட்டுப்பாடாகும்",
        "SC will strike down the Prohibition Act and order free liquor distribution to all citizens", "SC மதுவிலக்குச் சட்டத்தை ரத்து செய்து அனைத்துக் குடிமக்களுக்கும் இலவச மதுபான விநியோகத்திற்கு உத்தரவிடும்",
        "SC will declare Article 47 unconstitutional under Article 14", "SC உறுப்பு 47-ஐ உறுப்பு 14-ன் கீழ் அரசியலமைப்புக்கு முரணானது என அறிவிக்கும்",
        "SC will refer the trade dispute to the World Trade Organization (WTO)", "SC வர்த்தகத் தகராறை உலக வர்த்தக அமைப்பிற்கு (WTO) பரிந்துரைக்கும்",
        "A",
        "In State of Bombay v. F.N. Balsara (1951), Khoday Distilleries (1995), and State of Punjab v. Devans Modern Breweries (2004), the SC established that trade in noxious/intoxicating drinks is 'res extra commercium' (outside the scope of trade). Thus, no citizen can claim a Fundamental Right under Art 19(1)(g) to trade in liquor, and prohibition laws under Art 47 are valid reasonable restrictions under Art 19(6).",
        "F.N. பால்சரா (1951), கோடாய் டிஸ்டில்லரீஸ் (1995), மற்றும் தேவன்ஸ் பிரீவரிஸ் (2004) வழக்குகளில், போதைப் பான வியாபாரம் 'வணிகத்திற்கு அப்பாற்பட்டது' என SC நிறுவியது. எனவே, எந்தவொரு குடிமகனும் மதுபான வியாபாரம் செய்ய உறுப்பு 19(1)(g)-ன் கீழ் அடிப்படை உரிமை கோர முடியாது, மேலும் உறுப்பு 47-ன் கீழ் மதுவிலக்குச் சட்டங்கள் உறுப்பு 19(6)-ன் கீழ் செல்லுபடியாகும் நியாயமான கட்டுப்பாடுகள் ஆகும்.",
        "TNPSC Trap: Liquor trade is NOT protected under Article 19(1)(g). The doctrine applied is 'res extra commercium'.", "டிஎன்பிஎஸ்சி பொறி: மதுபான வியாபாரம் உறுப்பு 19(1)(g)-ன் கீழ் பாதுகாக்கப்படவில்லை. பயன்படுத்தப்படும் கோட்பாடு 'res extra commercium' ஆகும்.",
        "Correct. SC rejected Art 19(1)(g) challenge holding liquor trade is res extra commercium and Art 47 prohibition is valid under Art 19(6).", "சரி. மது வியாபாரம் வணிகத்திற்கு அப்பாற்பட்டது மற்றும் உறுப்பு 47 மதுவிலக்கு செல்லுபடியாகும் எனக்கூறி SC உறுப்பு 19(1)(g) சவாலை நிராகரித்தது.",
        "Prohibition laws are constitutionally valid.", "மதுவிலக்குச் சட்டங்கள் அரசியலமைப்பு ரீதியாகச் செல்லுபடியாகும்.",
        "Article 47 is a valid constitutional Part IV provision.", "உறுப்பு 47 செல்லுபடியாகும் அரசியலமைப்பு பகுதி IV விதியாகும்.",
        "Domestic constitutional rights are decided by Supreme Court, not WTO.", "உள்நாட்டு அரசியலமைப்பு உரிமைகள் உச்ச நீதிமன்றத்தால் தீர்மானிக்கப்படுகின்றன, WTO-வால் அல்ல."
    )

    # -------------------------------------------------------------------------
    # Q46 (Correct: B) - Case-law
    # -------------------------------------------------------------------------
    add_q(
        46, "Case-law",
        "In M.C. Mehta cases regarding Ganga pollution, Taj Mahal degradation, and vehicular pollution, how did the Supreme Court enforce environmental protection against state and private polluters?",
        "கங்கை மாசுபாடு, தாஜ் மஹால் சீரழிவு மற்றும் வாகன மாசுபாடு தொடர்பான எம்.சி. மேத்தா வழக்குகளில், அரசு மற்றும் தனியார் மாசுபடுத்திகளுக்கு எதிராக உச்ச நீதிமன்றம் எவ்வாறு சுற்றுச்சூழல் பாதுகாப்பை அமல்படுத்தியது?",
        "By declaring all vehicles and factories in India illegal under Article 19", "இந்தியாவில் உள்ள அனைத்து வாகனங்கள் மற்றும் தொழிற்சாலைகளை உறுப்பு 19-ன் கீழ் சட்டவிரோதமானவை என அறிவிப்பதன் மூலம்",
        "By applying the 'Polluter Pays Principle' and 'Precautionary Principle', reading Article 48A (State DPSP) and Article 51A(g) (Citizen FD) into Article 21 to enforce the Right to Clean Environment via Public Interest Litigation (PIL)", "பொதுநல வழக்கு (PIL) மூலம் தூய்மையான சுற்றுச்சூழல் உரிமையை அமல்படுத்த உறுப்பு 48A (அரசு DPSP) மற்றும் உறுப்பு 51A(g) (குடிமகன் FD) ஆகியவற்றை உறுப்பு 21-க்குள் வாசித்து, 'மாசுபடுத்துபவரே இழப்பீடு தரும் கோட்பாடு' மற்றும் 'முன்னெச்சரிக்கைக் கோட்பாட்டை'ப் பயன்படுத்துவதன் மூலம்",
        "By transferring all environment cases to the International Court of Justice", "அனைத்து சுற்றுச்சூழல் வழக்குகளையும் சர்வதேச நீதிமன்றத்திற்கு மாற்றுவதன் மூலம்",
        "By repealing the Environment Protection Act 1986", "1986 சுற்றுச்சூழல் பாதுகாப்புச் சட்டத்தை ரத்து செய்வதன் மூலம்",
        "B",
        "In landmark environmental PILs filed by M.C. Mehta, the SC read Article 48A (State obligation) and Article 51A(g) (Citizen duty) into Article 21 (Right to Life). The court applied environmental jurisprudence principles (Polluter Pays Principle, Precautionary Principle, Public Trust Doctrine) to issue continuous Mandamus for cleaning Ganga, protecting Taj Trapezium, and switching Delhi transport to CNG.",
        "எம்.சி. மேத்தா தாக்கல் செய்த முக்கிய சுற்றுச்சூழல் பொதுநல வழக்குகளில், SC உறுப்பு 48A (அரசு கடமை) மற்றும் உறுப்பு 51A(g) (குடிமகன் கடமை) ஆகியவற்றை உறுப்பு 21-க்குள் (வாழ்வு உரிமை) வாசித்தது. நீதிமன்றம் சுற்றுச்சூழல் சட்டவியல் கோட்பாடுகளைப் பயன்படுத்தி (மாசுபடுத்துபவரே இழப்பீடு தரும் கோட்பாடு, முன்னெச்சரிக்கைக் கோட்பாடு) கங்கையைத் தூய்மைப்படுத்தவும், தாஜ் மஹால் பகுதியைப் பாதுகாக்கவும் தொடர் பேராணைகளைப் பிறப்பித்தது.",
        "National Green Tribunal (NGT) Act 2010 was subsequently enacted to handle environmental adjudication.", "சுற்றுச்சூழல் தீர்ப்பளிப்பைக் கையாள பின்னர் தேசிய பசுமை தீர்ப்பாய (NGT) சட்டம் 2010 இயற்றப்பட்டது.",
        "Factories and vehicles are regulated under environmental standards, not banned universally.", "தொழிற்சாலைகள் மற்றும் வாகனங்கள் சுற்றுச்சூழல் தரநிலைகளின் கீழ் முறைப்படுத்தப்படுகின்றன, முற்றுமுழுதாகத் தடை செய்யப்படவில்லை.",
        "Correct. SC read Art 48A + 51A(g) into Art 21 and applied Polluter Pays & Precautionary principles in PILs.", "சரி. PIL வழக்குகளில் SC 48A + 51A(g) ஆகியவற்றை உறுப்பு 21-க்குள் வாசித்து, மாசுபடுத்துபவரே இழப்பீடு தரும் மற்றும் முன்னெச்சரிக்கைக் கோட்பாடுகளைப் பயன்படுத்தியது.",
        "Indian courts hold jurisdiction under Article 32 and 226.", "இந்திய நீதிமன்றங்கள் உறுப்புகள் 32 மற்றும் 226-ன் கீழ் அதிகார வரம்பைக் கொண்டுள்ளன.",
        "SC enforced Environment Protection Act 1986; it did not repeal it.", "SC 1986 சுற்றுச்சூழல் பாதுகாப்புச் சட்டத்தை அமல்படுத்தியது; அதை ரத்து செய்யவில்லை."
    )

    # -------------------------------------------------------------------------
    # Q47 (Correct: C) - Multi-statement
    # -------------------------------------------------------------------------
    add_q(
        47, "Multi-statement",
        "Consider the following clauses of Article 39 and their matching subject matters:\n1. 39(a) – Right to adequate means of livelihood for all citizens\n2. 39(d) – Equal pay for equal work for men and women\n3. 39(f) – Opportunities for healthy development of children\nWhich of the pairs given above is/are CORRECTLY matched?",
        "உறுப்பு 39-ன் பின்வரும் உட்பிரிவுகளையும் அவற்றின் பொருத்தப்பட்ட பொருள்களையும் கருதுக:\n1. 39(a) – அனைத்துக் குடிமக்களுக்கும் போதுமான வாழ்வாதார வழிவகைகள் உரிமை\n2. 39(d) – ஆண், பெண் இருபாலருக்கும் சம வேலைக்கு சம ஊதியம்\n3. 39(f) – குழந்தைகள் ஆரோக்கியமான முறையில் வளர்வதற்கான வாய்ப்புகள்\nமேலே கொடுக்கப்பட்டுள்ள ஜோடிகளில் எது/எவை சரியாகப் பொருந்தி உள்ளது/உள்ளன?",
        "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
        "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
        "1, 2 and 3", "1, 2 மற்றும் 3",
        "1 and 3 only", "1 மற்றும் 3 மட்டுமே",
        "C",
        "All three clauses of Article 39 are CORRECTLY matched: 39(a) = adequate means of livelihood; 39(d) = equal pay for equal work; 39(f) = healthy development of children (substituted by 42nd CAA 1976).",
        "உறுப்பு 39-ன் மூன்று உட்பிரிவுகளும் சரியாகப் பொருந்தி உள்ளன: 39(a) = போதுமான வாழ்வாதார வழிவகைகள்; 39(d) = சம வேலைக்கு சம ஊதியம்; 39(f) = ஆரோக்கியமான குழந்தை வளர்ச்சி (42வது திருத்தம் 1976 மூலம் மாற்றப்பட்டது).",
        "Complete Article 39 breakdown: 39(a) Livelihood, 39(b) Material resources, 39(c) Wealth concentration, 39(d) Equal pay, 39(e) Worker health, 39(f) Child development.",
        "உறுப்பு 39 முழுமையான விவரம்: 39(a) வாழ்வாதாரம், 39(b) பொருள் வளங்கள், 39(c) செல்வக் குவிப்பு, 39(d) சம ஊதியம், 39(e) தொழிலாளர் சுகாதாரம், 39(f) குழந்தை வளர்ச்சி.",
        "Statement 3 is also correct, making 1, 2 and 3 correct.", "கூற்று 3-ம் சரியானதால், 1, 2 மற்றும் 3 சரியானவை ஆகும்.",
        "Statement 1 is also correct.", "கூற்று 1-ம் சரியானதாகும்.",
        "Correct. Pairs 1, 2 and 3 are all correctly matched.", "சரி. ஜோடிகள் 1, 2 மற்றும் 3 அனைத்தும் சரியாகப் பொருந்தி உள்ளன.",
        "Statement 2 is also correct.", "கூற்று 2-ம் சரியானதாகும்."
    )

    # -------------------------------------------------------------------------
    # Q48 (Correct: D) - Advanced Conceptual
    # -------------------------------------------------------------------------
    add_q(
        48, "Conceptual",
        "In his famous closing speech to the Constituent Assembly on November 25, 1949, how did Dr. B.R. Ambedkar articulate the complementary relationship between Political Democracy (Part III) and Social & Economic Democracy (Part IV)?",
        "நவம்பர் 25, 1949 அன்று அரசியலமைப்பு நிர்ணய சபையில் ஆற்றப்பட்ட தனது புகழ்பெற்ற நிறைவு உரையில், அரசியல் ஜனநாயகம் (பகுதி III) மற்றும் சமூக & பொருளாதார ஜனநாயகம் (பகுதி IV) ஆகியவற்றுக்கு இடையேயான நிரப்பு தொடர்பை டாக்டர் பி.ஆர். அம்பேத்கர் எவ்வாறு வெளிப்படுத்தினார்?",
        "He stated that Political Democracy alone is sufficient without any social or economic equality", "சமூக அல்லது பொருளாதார சமத்துவம் இன்றி அரசியல் ஜனநாயகம் மட்டுமே போதுமானது என அவர் கூறினார்",
        "He stated that Directive Principles should replace Fundamental Rights completely", "அடிப்படை உரிமைகளை வழிகாட்டு நெறிமுறைகள் முழுமையாக மாற்றியமைக்க வேண்டும் என அவர் கூறினார்",
        "He stated that economic equality can only be achieved by abolishing parliamentary democracy", "நாடாளுமன்ற ஜனநாயகத்தை ஒழிப்பதன் மூலம் மட்டுமே பொருளாதார சமத்துவத்தை அடைய முடியும் என அவர் கூறினார்",
        "He warned that Political Democracy cannot last unless there lies at the base of it Social Democracy, which recognizes liberty, equality, and fraternity as the principles of life", "சுதந்திரம், சமத்துவம் மற்றும் சகோதரத்துவத்தைச் வாழ்க்கைக் கோட்பாடுகளாக ஏற்கும் சமூக ஜனநாயகம் அதன் அடித்தளமாக இல்லாவிட்டால் அரசியல் ஜனநாயகம் நீடிக்க முடியாது என அவர் எச்சரித்தார்",
        "D",
        "On November 25, 1949, Dr. B.R. Ambedkar warned: 'Political democracy cannot last unless there lies at the base of it social democracy. What does social democracy mean? It means a way of life which recognizes liberty, equality and fraternity as the principles of life.' Part III provides Political Democracy; Part IV DPSPs provide the roadmap for Social and Economic Democracy.",
        "நவம்பர் 25, 1949 அன்று, டாக்டர் பி.ஆர். அம்பேத்கர் எச்சரித்தார்: 'அரசியல் ஜனநாயகம் அதன் அடித்தளத்தில் சமூக ஜனநாயகம் இல்லாவிட்டால் நீடிக்க முடியாது. சமூக ஜனநாயகம் என்றால் என்ன? இது சுதந்திரம், சமத்துவம் மற்றும் சகோதரத்துவத்தைச் வாழ்க்கைக் கோட்பாடுகளாக ஏற்கும் ஒரு வாழ்க்கை முறையாகும்.' பகுதி III அரசியல் ஜனநாயகத்தை வழங்குகிறது; பகுதி IV DPSP-கள் சமூக மற்றும் பொருளாதார ஜனநாயகத்திற்கான வழிகாட்டலை வழங்குகின்றன.",
        "Ambedkar highlighted the 'contradiction' of entering independence with political equality (one man one vote) but social/economic inequality (one man one value lacking). DPSP aims to remove that contradiction.",
        "அரசியல் சமத்துவத்துடன் (ஒரு மனிதன் ஒரு வாக்கு) சுதந்திரத்தில் நுழைவது ஆனால் சமூக/பொருளாதார சமத்துவமின்மை நிலவுவது என்ற 'முரண்பாட்டை' அம்பேத்கர் முன்னிலைப்படுத்தினார். DPSP அந்த முரண்பாட்டை அகற்றுவதை நோக்கமாகக் கொண்டுள்ளது.",
        "Ambedkar explicitly warned that political democracy alone without social equality would be unstable.", "சமூக சமத்துவம் இல்லாமல் வெறும் அரசியல் ஜனநாயகம் மட்டுமே நிலையற்றதாக இருக்கும் என்று அம்பேத்கர் வெளிப்படையாக எச்சரித்தார்.",
        "Ambedkar advocated for synthesizing both Part III and Part IV.", "அம்பேத்கர் பகுதி III மற்றும் பகுதி IV ஆகிய இரண்டையும் இணைப்பதை ஆதரித்தார்.",
        "Ambedkar championed parliamentary democracy.", "அம்பேத்கர் நாடாளுமன்ற ஜனநாயகத்தை ஆதரித்தார்.",
        "Correct. Dr. Ambedkar stated Political Democracy cannot last without Social Democracy (Part IV DPSP goals).", "சரி. சமூக ஜனநாயகம் (பகுதி IV DPSP இலக்குகள்) இல்லாமல் அரசியல் ஜனநாயகம் நீடிக்க முடியாது என டாக்டர் அம்பேத்கர் கூறினார்."
    )

    # -------------------------------------------------------------------------
    # Q49 (Correct: A) - Assertion & Reason
    # -------------------------------------------------------------------------
    add_q(
        49, "Assertion-Reason",
        "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): Laws enacted to implement Article 39(b) and Article 39(c) enjoy constitutional immunity under Article 31C against being challenged under Article 14 (Equality) and Article 19 (Freedoms).\nReason (R): In Kesavananda Bharati case (1973), the Supreme Court upheld the constitutional validity of the first part of Article 31C protecting Article 39(b) and 39(c) laws.\nSelect the correct answer using the code below:",
        "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன, ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிக்கப்பட்டுள்ளன:\nகூற்று (A): உறுப்பு 39(b) மற்றும் உறுப்பு 39(c)-ஐ செயல்படுத்த இயற்றப்படும் சட்டங்கள் உறுப்பு 14 (சமத்துவம்) மற்றும் உறுப்பு 19 (சுதந்திரங்கள்) ஆகியவற்றின் கீழ் சவால் செய்யப்படுவதிலிருந்து உறுப்பு 31C-ன் கீழ் அரசியலமைப்புப் பாதுகாப்பைப் பெறுகின்றன.\nகாரணம் (R): கேசவானந்த பாரதி வழக்கில் (1973), உறுப்பு 39(b) மற்றும் 39(c) சட்டங்களைப் பாதுகாக்கும் உறுப்பு 31C-ன் முதல் பகுதியின் அரசியலமைப்பு செல்லுபடித் தன்மையை உச்ச நீதிமன்றம் உறுதி செய்தது.\nகீழேயுள்ள குறியீட்டைப் பயன்படுத்தி சரியான பதிலைத் தேர்ந்தெடுக்கவும்:",
        "Both (A) and (R) are true, and (R) is the correct explanation of (A)", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி, மேலும் காரணம் (R) கூற்று (A)-விற்கு சரியான விளக்கமாகும்",
        "Both (A) and (R) are true, but (R) is NOT the correct explanation of (A)", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி, ஆனால் காரணம் (R) கூற்று (A)-விற்கு சரியான விளக்கமல்ல",
        "(A) is true, but (R) is false", "கூற்று (A) சரி, ஆனால் காரணம் (R) தவறு",
        "(A) is false, but (R) is true", "கூற்று (A) தவறு, ஆனால் காரணம் (R) சரி",
        "A",
        "Both (A) and (R) are true, and (R) correctly explains (A). The 25th Constitutional Amendment Act 1971 inserted Article 31C protecting 39(b) and 39(c) laws from Articles 14, 19, and 31. In Kesavananda Bharati (1973), a 13-judge bench UPHELD the 1st part of Article 31C, cementing this constitutional immunity under judicial review.",
        "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி, மேலும் காரணம் (R) கூற்று (A)-விற்கு சரியான விளக்கமாகும். 1971-ன் 25வது அரசியலமைப்பு திருத்தச் சட்டம் 39(b) மற்றும் 39(c) சட்டங்களை உறுப்புகள் 14, 19, மற்றும் 31-லிருந்து பாதுகாக்கும் உறுப்பு 31C-ஐ இணைத்தது. கேசவானந்த பாரதி வழக்கில் (1973), 13-நீதிபதிகள் அமர்வு உறுப்பு 31C-ன் 1வது பகுதியை உறுதி செய்தது.",
        "This is the ONLY exception where DPSPs take legal priority over Part III Fundamental Rights 14 & 19.", "DPSP-கள் பகுதி III அடிப்படை உரிமைகள் 14 & 19-ஐ விட சட்டப் முன்னுரிமை பெறும் ஒரே விலக்கு இதுவாகும்.",
        "Correct. Both (A) and (R) are true, and (R) is the correct explanation of (A).", "சரி. கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி, மேலும் காரணம் (R) கூற்று (A)-விற்கு சரியான விளக்கமாகும்.",
        "Reason (R) explains why Assertion (A) remains valid constitutional law today.", "கூற்று (A) ஏன் இன்று செல்லுபடியாகும் அரசியலமைப்புச் சட்டமாக நீடிக்கிறது என்பதை காரணம் (R) விளக்குகிறது.",
        "Reason (R) is true.", "காரணம் (R) சரியானது.",
        "Assertion (A) is true.", "கூற்று (A) சரியானது."
    )

    # -------------------------------------------------------------------------
    # Q50 (Correct: B) - High-level Trap
    # -------------------------------------------------------------------------
    add_q(
        50, "TNPSC Trap",
        "Does Article 51 (Promotion of International Peace and Security) mean that an international treaty signed by India automatically becomes enforceable domestic law in Indian courts without a statutory Act passed by Parliament?",
        "உறுப்பு 51 (சர்வதேச அமைதி மற்றும் பாதுகாப்பை மேம்படுத்துதல்) என்பது இந்தியா கையெழுத்திட்ட ஒரு பன்னாட்டு ஒப்பந்தம் நாடாளுமன்றத்தால் இயற்றப்படும் சட்டப்பூர்வ சட்டமின்றி இந்திய நீதிமன்றங்களில் தானாகவே அமல்படுத்தக்கூடிய உள்நாட்டுச் சட்டமாக மாறுகிறது என்பதா?",
        "Yes. Article 51 makes all international treaties self-executing domestic laws immediately upon signing", "ஆம். உறுப்பு 51 அனைத்து பன்னாட்டு ஒப்பந்தங்களையும் கையெழுத்திட்ட உடனேயே தானாகவே செயல்படும் உள்நாட்டுச் சட்டங்களாக மாற்றுகிறது",
        "No. Article 51 is a Part IV DPSP guiding State foreign policy; under India's Dualist system, an international treaty requires implementing legislation enacted by Parliament under Article 253 to create enforceable domestic rights", "இல்லை. உறுப்பு 51 என்பது அரசின் வெளியுறவுக் கொள்கையை வழிகாட்டும் பகுதி IV DPSP ஆகும்; இந்தியாவின் இருத்துவ முறையின் கீழ், அமல்படுத்தக்கூடிய உள்நாட்டு உரிமைகளை உருவாக்க பன்னாட்டு ஒப்பந்தத்திற்கு உறுப்பு 253-ன் கீழ் நாடாளுமன்றத்தால் இயற்றப்படும் செயலாக்கச் சட்டம் தேவைப்படுகிறது",
        "Yes. Article 51 grants the Supreme Court power to ratify treaties without Parliament", "ஆம். உறுப்பு 51 நாடாளுமன்றம் இல்லாமல் ஒப்பந்தங்களை உறுதிப்படுத்த உச்ச நீதிமன்றத்திற்கு அதிகாரம் அளிக்கிறது",
        "No. Treaties can only be enforced if ratified by all State Legislative Assemblies", "இல்லை. அனைத்து மாநில சட்டமன்றங்களாலும் உறுதிப்படுத்தப்பட்டால் மட்டுமே ஒப்பந்தங்களை அமல்படுத்த முடியும்",
        "B",
        "Under India's constitutional framework, Article 51 is a DPSP directing the State to foster respect for international law and treaty obligations. However, India follows a Dualist model (Jolly George Varghese 1980 & Gramophone Co. 1984), meaning international treaties DO NOT automatically become domestic law. Parliament must enact implementing legislation under Article 253 (Union List Entry 14).",
        "இந்தியாவின் அரசியலமைப்பு கட்டமைப்பின் கீழ், உறுப்பு 51 என்பது சர்வதேச சட்டம் மற்றும் ஒப்பந்தக் கடமைகளுக்கு மரியாதையை வளர்க்க அரசுக்கு வழிகாட்டும் DPSP ஆகும். இருப்பினும், இந்தியா ஒரு இருத்துவ மாதிரியைப் பின்பற்றுகிறது (ஜாலி ஜார்ஜ் வர்கீஸ் 1980 & கிராமபோன் கோ 1984), இதன் பொருள் பன்னாட்டு ஒப்பந்தங்கள் தானாகவே உள்நாட்டுச் சட்டமாக மாறாது. நாடாளுமன்றம் உறுப்பு 253-ன் கீழ் செயலாக்கச் சட்டத்தை இயற்ற வேண்டும்.",
        "TNPSC Trap: DPSP Article 51 sets the international policy direction; Article 253 provides the Parliamentary legislative mechanism.",
        "டிஎன்பிஎஸ்சி பொறி: DPSP உறுப்பு 51 சர்வதேச கொள்கை திசையை அமைக்கிறது; உறுப்பு 253 நாடாளுமன்றச் சட்ட பொறிமுறையை வழங்குகிறது.",
        "International treaties are not self-executing in Indian domestic courts.", "இந்திய உள்நாட்டு நீதிமன்றங்களில் பன்னாட்டு ஒப்பந்தங்கள் தானாகவே செயல்படுபவை அல்ல.",
        "Correct. Art 51 is a DPSP foreign policy guide; Art 253 legislation is required for domestic enforcement.", "சரி. உறுப்பு 51 ஒரு DPSP வெளியுறவுக் கொள்கை வழிகாட்டி; உள்நாட்டு அமலாக்கத்திற்கு உறுப்பு 253 சட்டம் தேவைப்படுகிறது.",
        "Supreme Court does not ratify international treaties.", "உச்ச நீதிமன்றம் பன்னாட்டு ஒப்பந்தங்களை உறுதிப்படுத்துவதில்லை.",
        "State assembly ratification is not required for Union List Entry 14 treaty legislation.", "ஒன்றியப் பட்டியலின் பிரிவு 14 ஒப்பந்தச் சட்டத்திற்கு மாநில சட்டமன்ற ஒப்புதல் தேவையில்லை."
    )

    output_dir = "data/questions/polity"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "directive_principles_hard.json")

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)

    print(f"Successfully generated {len(questions)} DPSP Hard MCQs at {output_path}")

    counts = {"A": 0, "B": 0, "C": 0, "D": 0}
    for q in questions:
        counts[q["correct_answer"]] += 1
    print(f"Answer Key Distribution: A={counts['A']}, B={counts['B']}, C={counts['C']}, D={counts['D']}")

if __name__ == "__main__":
    generate_50_hard_mcqs()
