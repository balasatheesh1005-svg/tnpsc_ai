# Constitutional Amendments - 50 Hard MCQs Builder Script (Unique Group 1 Questions)
# File: data/questions/polity/constitutional_amendments_hard.json
# Target Distribution: A: 13, B: 13, C: 12, D: 12 (Total 50)

import json
import os

def create_hard_questions():
    questions = []

    def add_q(q_id, q_en, q_ta,
              opt_a_en, opt_a_ta, opt_b_en, opt_b_ta, opt_c_en, opt_c_ta, opt_d_en, opt_d_ta,
              correct_ans, exp_en, exp_ta,
              why_a_en, why_a_ta, why_b_en, why_b_ta, why_c_en, why_c_ta, why_d_en, why_d_ta,
              tip_en, tip_ta, fact_en, fact_ta, bloom, pyq_sim, tags, notes_ref):
        questions.append({
            "id": q_id,
            "subject": "Polity",
            "topic": "Constitutional Amendments",
            "difficulty": "Hard",
            "question_type": "single_choice",
            "question": {"en": q_en, "ta": q_ta},
            "options": [
                {"id": "A", "en": opt_a_en, "ta": opt_a_ta},
                {"id": "B", "en": opt_b_en, "ta": opt_b_ta},
                {"id": "C", "en": opt_c_en, "ta": opt_c_ta},
                {"id": "D", "en": opt_d_en, "ta": opt_d_ta}
            ],
            "correct_answer": correct_ans,
            "explanation": {"en": exp_en, "ta": exp_ta},
            "why_not_others": {
                "A": {"en": why_a_en, "ta": why_a_ta},
                "B": {"en": why_b_en, "ta": why_b_ta},
                "C": {"en": why_c_en, "ta": why_c_ta},
                "D": {"en": why_d_en, "ta": why_d_ta}
            },
            "tnpsc_tip": {"en": tip_en, "ta": tip_ta},
            "revision_fact": {"en": fact_en, "ta": fact_ta},
            "source_reference": [
                "M. Laxmikanth — Indian Polity",
                f"TNPSC Nova AI Notes — Constitutional Amendments {notes_ref}"
            ],
            "bloom_level": bloom,
            "estimated_time_sec": 75,
            "pyq_similarity": pyq_sim,
            "tags": tags
        })

    # Q001 - Correct: A
    add_q(
        "CZ_AM_HD_001",
        "Which Supreme Court bench laid down that the Doctrine of Basic Structure applies to ALL constitutional amendments enacted after April 24, 1973, including those inserting laws into the 9th Schedule?",
        "1973 ஏப்ரல் 24 ஆம் தேதிக்குப் பிறகு இயற்றப்பட்ட 9வது அட்டவணையில் சட்டங்களைச் சேர்க்கும் திருத்தங்கள் உட்பட அனைத்து அரசியலமைப்புத் திருத்தங்களுக்கும் 'அடிப்படை அமைப்பு சோதனைக் கோட்பாடு' பொருந்தும் என்று தீர்ப்பளித்த உச்ச நீதிமன்ற அமர்வு எது?",
        "9-judge bench in I.R. Coelho v. State of Tamil Nadu (2007)", "ஐ.ஆர். கொஹெலோ எதிர் தமிழ்நாடு அரசு (2007) வழக்கில் 9 நீதிபதிகள் அமர்வு",
        "5-judge bench in Minerva Mills v. Union of India (1980)", "மினர்வா மில்ஸ் எதிர் இந்திய யூனியன் (1980) வழக்கில் 5 நீதிபதிகள் அமர்வு",
        "13-judge bench in Kesavananda Bharati v. State of Kerala (1973)", "கேசவாநந்த பாரதி எதிர் கேரள அரசு (1973) வழக்கில் 13 நீதிபதிகள் அமர்வு",
        "5-judge bench in Waman Rao v. Union of India (1981)", "வாமன் ராவ் எதிர் இந்திய யூனியன் (1981) வழக்கில் 5 நீதிபதிகள் அமர்வு",
        "A",
        "In I.R. Coelho v. State of Tamil Nadu (2007), a unanimous 9-judge Constitution Bench held that any law placed in the 9th Schedule after April 24, 1973 must pass the test of Basic Structure (Art 14, 19, 21 read with basic principles); blanket immunity under Art 31B is no longer valid.",
        "ஐ.ஆர். கொஹெலோ (2007) வழக்கில் 9 நீதிபதிகள் கொண்ட அரசியலமைப்பு அமர்வு, 1973 ஏப்ரல் 24 க்குப் பின் 9வது அட்டவணையில் சேர்க்கப்பட்ட எந்தவொரு சட்டமும் அடிப்படை அமைப்பு சோதனையில் வெற்றி பெற்றாக வேண்டும் எனத் தீர்ப்பளித்தது.",
        "Option A is correct because I.R. Coelho (9 judges, 2007) definitively established the basic structure test for 9th Schedule post-1973 laws.", "விருப்பம் A சரியானது, ஏனெனில் ஐ.ஆர். கொஹெலோ வழக்கு (9 நீதிபதிகள், 2007) இத்தீர்ப்பை வழங்கியது.",
        "Option B is incorrect; Minerva Mills (1980) dealt with Art 368(4)&(5) invalidation.", "விருப்பம் B தவறானது; மினர்வா மில்ஸ் வழக்கு சரத்து 368(4)&(5) ஐ ரத்து செய்தது.",
        "Option C is incorrect; Kesavananda Bharati (1973) established the doctrine, but I.R. Coelho extended its formal test to 9th Schedule specifically.", "விருப்பம் C தவறானது; கேசவாநந்த பாரதி வழக்கு கோட்பாட்டை உருவாக்கியது, ஆனால் 9வது அட்டவணைக்கான சோதனையை ஐ.ஆர். கொஹெலோ வழங்கியது.",
        "Option D is incorrect; Waman Rao (1981) first indicated the cutoff date, but I.R. Coelho (2007) delivered the authoritative 9-judge ruling.", "விருப்பம் D தவறானது; வாமன் ராவ் வழக்கு எல்லை நாளைக் குறிப்பிட்டது, ஆனால் 9 நீதிபதிகள் தீர்ப்பு கொஹெலோ வழக்கு.",
        "I.R. Coelho judgment affirmed that Parliament cannot validate an unconstitutional law violating basic structure merely by placing it in the 9th Schedule.",
        "அடிப்படை அமைப்பை மீறும் சட்டத்தை 9வது அட்டவணையில் சேர்ப்பதன் மூலம் மட்டுமே நாடாளுமன்றம் அதைச் செல்லுபடியாக்க முடியாது என்பதை ஐ.ஆர். கொஹெலோ தீர்ப்பு உறுதி செய்தது.",
        "April 24, 1973 is the date of the Kesavananda Bharati judgment.",
        "1973 ஏப்ரல் 24 என்பது கேசவாநந்த பாரதி தீர்ப்பு வழங்கப்பட்ட நாளாகும்.",
        "Analysis", "High", ["I.R. Coelho Case", "9th Schedule Basic Structure", "April 24 1973"], "Part 3"
    )

    # Q002 - Correct: B
    add_q(
        "CZ_AM_HD_002",
        "Consider the following federal provisions under the Proviso to Article 368(2):\nI. The Supreme Court and High Courts\nII. Distribution of legislative powers between Union and States\nIII. Any of the Lists in the Seventh Schedule\nIV. Representation of States in Parliament\nWhich of these provisions require Special Majority of Parliament PLUS Ratification by Half of the States?",
        "சரத்து 368(2) இன் கீழ் கூட்டாட்சி வரம்பில் உள்ள விதிகளை ஆராய்க:\nI. உச்ச நீதிமன்றம் மற்றும் உயர் நீதிமன்றங்கள்\nII. மத்திய மற்றும் மாநிலங்களுக்கிடையேயான சட்டமன்ற அதிகாரப் பகிர்வு\nIII. ஏழாவது அட்டவணையில் உள்ள ஏதேனும் ஒரு பட்டியல்\nIV. நாடாளுமன்றத்தில் மாநிலங்களின் பிரதிநிதித்துவம்\nஇவற்றில் எவற்றிற்கு நாடாளுமன்றத்தின் சிறப்பு பெரும்பான்மையுடன் பாதி மாநிலங்களின் ஒப்புதலும் தேவை?",
        "I and II only", "I மற்றும் II மட்டுமே",
        "I, II, III, and IV (All four)", "I, II, III, மற்றும் IV (நான்கும்)",
        "I, III, and IV only", "I, III, மற்றும் IV மட்டுமே",
        "II and IV only", "II மற்றும் IV மட்டுமே",
        "B",
        "All four listed items (Supreme Court & High Courts, Distribution of legislative powers, 7th Schedule Lists, Representation of States in Parliament) fall under the Proviso to Article 368(2) and require Special Majority PLUS State Ratification.",
        "மேலே பட்டியலிடப்பட்ட நான்கு அம்சங்களும் (உச்ச/உயர் நீதிமன்றங்கள், அதிகாரப் பகிர்வு, 7வது அட்டவணைப் பட்டியல்கள், நாடாளுமன்ற மாநிலப் பிரதிநிதித்துவம்) சரத்து 368(2) இன் வரம்பில் அமைந்துள்ளன. எனவே நான்கிற்கும் மாநில ஒப்புதல் கட்டாயம்.",
        "Option A is incorrect because items III and IV also require state ratification.", "விருப்பம் A தவறானது, ஏனெனில் III மற்றும் IV க்கும் மாநில ஒப்புதல் தேவை.",
        "Option B is correct because all four provisions affect the federal equilibrium and require ratification by at least half of the state legislatures under Art 368(2).", "விருப்பம் B சரியானது, ஏனெனில் நான்குமே கூட்டாட்சி அமைப்பைப் பாதிப்பதால் மாநில ஒப்புதல் தேவை.",
        "Option C is incorrect because item II also requires state ratification.", "விருப்பம் C தவறானது, ஏனெனில் II க்கும் மாநில ஒப்புதல் தேவை.",
        "Option D is incorrect because items I and III also require state ratification.", "விருப்பம் D தவறானது, ஏனெனில் I மற்றும் III க்கும் மாநில ஒப்புதல் தேவை.",
        "Proviso to Article 368(2) specifies 5 main federal categories: (1) Pres. Election, (2) Exec power limits, (3) SC/HCs, (4) 7th Schedule, (5) Rep of States in Parliament, & Art 368 itself.",
        "சரத்து 368(2) இன் வரம்புரை 5 முக்கிய கூட்டாட்சி வகைகளைக் குறிப்பிடுகிறது: குடியரசு தலைவர் தேர்தல், நிர்வாக வரம்பு, உச்ச/உயர் நீதிமன்றங்கள், 7வது அட்டவணை, நாடாளுமன்ற மாநிலப் பிரதிநிதித்துவம் மற்றும் சரத்து 368.",
        "If an amendment bill lacks state ratification in these categories, it is constitutionally void.",
        "இவ்வகைகளில் மாநில ஒப்புதல் பெறாத திருத்த மசோதா அரசியலமைப்புப்படி செல்லாது.",
        "Analysis", "High", ["Article 368 Proviso", "Federal Provisions", "State Ratification"], "Part 1"
    )

    # Q003 - Correct: C
    add_q(
        "CZ_AM_HD_003",
        "Which Constitutional Amendment Act introduced Article 31C for the first time, establishing that laws implementing Directive Principles under Article 39(b) and 39(c) cannot be declared void for violating Articles 14 and 19?",
        "சரத்து 39(b) மற்றும் 39(c) இல் உள்ள அரசு நெறிமுறைக் கோட்பாடுகளைச் செயல்படுத்தும் சட்டங்கள் சரத்துகள் 14 மற்றும் 19 ஐ மீறுவதாகக் கூறி செல்லாது என அறிவிக்க முடியாது என்று முதன்முறையாக சரத்து 31C ஐ அறிமுகப்படுத்திய அரசியலமைப்பு திருத்தச் சட்டம் எது?",
        "24th Constitutional Amendment Act, 1971", "24வது அரசியலமைப்பு திருத்தச் சட்டம், 1971",
        "42nd Constitutional Amendment Act, 1976", "42வது அரசியலமைப்பு திருத்தச் சட்டம், 1976",
        "25th Constitutional Amendment Act, 1971", "25வது அரசியலமைப்பு திருத்தச் சட்டம், 1971",
        "44th Constitutional Amendment Act, 1978", "44வது அரசியலமைப்பு திருத்தச் சட்டம், 1978",
        "C",
        "The 25th Constitutional Amendment Act, 1971 inserted Article 31C containing two clauses: (1) Immunity to laws giving effect to Art 39(b)&(c) from Arts 14, 19, & 31, and (2) Barring judicial review of such declarations.",
        "25வது அரசியலமைப்பு திருத்தச் சட்டம், 1971 சரத்து 31C ஐ இரு பிரிவுகளுடன் சேர்த்தது: (1) சரத்து 39(b)&(c) சட்டங்களுக்கு சரத்து 14, 19 இலிருந்து பாதுகாப்பு, (2) நீதிமன்ற மறுாய்வைத் தடுத்தல்.",
        "Option A is incorrect; 24th CA 1971 amended Article 368 and Article 13.", "விருப்பம் A தவறானது; 24வது திருத்தம் சரத்து 368 மற்றும் 13 ஐத் திருத்தியது.",
        "Option B is incorrect; 42nd CA expanded Art 31C to ALL DPSPs (which was later invalidated).", "விருப்பம் B தவறானது; 42வது திருத்தம் அனைத்து DPSP களுக்கும் 31C ஐ விரிவாக்கியது.",
        "Option C is correct because 25th CA 1971 inserted Article 31C for the first time.", "விருப்பம் C சரியானது, ஏனெனில் 25வது திருத்தம் 1971 முதன்முதலில் சரத்து 31C ஐச் சேர்த்தது.",
        "Option D is incorrect; 44th CA 1978 deleted Right to Property (Art 31).", "விருப்பம் D தவறானது; 44வது திருத்தம் சொத்துரிமையை நீக்கியது.",
        "Kesavananda Bharati (1973) upheld the 1st part of 25th CA (Art 31C immunity), but invalidated the 2nd part which barred judicial review.",
        "கேசவாநந்த பாரதி வழக்கு 25வது திருத்தத்தின் 1வது பகுதியை உறுதி செய்தது, ஆனால் நீதிமன்ற ஆய்வைத் தடுத்த 2வது பகுதியை ரத்து செய்தது.",
        "Article 39(b) deals with distribution of material resources; Article 39(c) deals with prevention of concentration of wealth.",
        "சரத்து 39(b) வளங்கள் பகிர்வு பற்றியது; சரத்து 39(c) செல்வக் குவிப்பைத் தடுத்தல் பற்றியது.",
        "Analysis", "High", ["25th Amendment", "Article 31C", "Kesavananda Partial Invalidation"], "Part 2"
    )

    # Q004 - Correct: D
    add_q(
        "CZ_AM_HD_004",
        "In Minerva Mills v. Union of India (1980), which two main provisions inserted by the 42nd Constitutional Amendment Act, 1976 were struck down by the Supreme Court as unconstitutional?",
        "மினர்வா மில்ஸ் எதிர் இந்திய யூனியன் (1980) வழக்கில் 42வது அரசியலமைப்பு திருத்தச் சட்டம் 1976 மூலம் சேர்க்கப்பட்ட எந்த இரு முக்கிய விதிகளை உச்ச நீதிமன்றம் அரசியலமைப்பிற்கு முரண் என ரத்து செய்தது?",
        "Article 51A and Article 39A", "சரத்து 51A மற்றும் சரத்து 39A",
        "Article 323A and Article 323B", "சரத்து 323A மற்றும் சரத்து 323B",
        "Article 239AA and Article 243", "சரத்து 239AA மற்றும் சரத்து 243",
        "Article 368(4) & (5) and extension of Article 31C", "சரத்து 368(4) & (5) மற்றும் சரத்து 31C இன் விரிவாக்கம்",
        "D",
        "In Minerva Mills (1980), SC struck down Clauses (4) and (5) of Article 368 (which claimed unlimited amending power and barred judicial review) and Section 4 extending Article 31C to ALL Directive Principles.",
        "மினர்வா மில்ஸ் வழக்கில் (1980) சரத்து 368(4)&(5) (வரம்பற்ற திருத்த அதிகாரம் & நீதிமன்ற ஆய்வுத் தடை) மற்றும் அனைத்து DPSP களுக்கும் சரத்து 31C ஐ விரிவாக்கிய பிரிவு 4 ஆகியவற்றை உச்ச நீதிமன்றம் ரத்து செய்தது.",
        "Option A is incorrect; Art 51A (Fundamental Duties) and Art 39A (Free Legal Aid) were NOT struck down.", "விருப்பம் A தவறானது; இச்சரத்துகள் ரத்து செய்யப்படவில்லை.",
        "Option B is incorrect; Art 323A and 323B were modified later in L. Chandra Kumar 1997, not Minerva Mills.", "விருப்பம் B தவறானது; இவை எல். சந்திர குமார் வழக்கில் திருத்தப்பட்டன.",
        "Option C is incorrect; Art 239AA was inserted by 69th CA 1991.", "விருப்பம் C தவறானது; சரத்து 239AA 69வது திருத்தத்தால் சேர்க்கப்பட்டது.",
        "Option D is correct because Minerva Mills (1980) invalidated Art 368(4)&(5) and the 42nd CA expansion of Art 31C.", "விருப்பம் D சரியானது, ஏனெனில் மினர்வா மில்ஸ் வழக்கு இவ்விரு விதிகளையும் ரத்து செய்தது.",
        "Justice Y.V. Chandrachud observed: 'The donee of a limited power cannot by the exercise of that power convert the limited power into an unlimited one'.", "தலைமை நீதிபதி ஒய்.வி. சந்திரசூட்: 'வரம்பிற்குட்பட்ட அதிகாரம் பெற்ற ஒருவர் அந்த அதிகாரத்தைப் பயன்படுத்தி அதை வரம்பற்ற அதிகாரமாக மாற்ற முடியாது' என்றார்.",
        "This judgment established that limited amending power itself is a basic structure.",
        "வரம்பிற்குட்பட்ட திருத்த அதிகாரமே ஒரு அடிப்படை அமைப்பு என்பதை இத்தீர்ப்பு நிறுவியது.",
        "Analysis", "High", ["Minerva Mills", "Article 368(4) and (5)", "Section 55 Invalidation"], "Part 3"
    )

    # Q005 - Correct: A
    add_q(
        "CZ_AM_HD_005",
        "Which Supreme Court judgment first established that a Constitutional Amendment Act under Article 368 CANNOT be challenged under Article 13(2) because 'law' in Article 13(2) includes only ordinary law, not constitutional amendment law?",
        "சரத்து 13(2) இல் உள்ள 'சட்டம்' என்பது சாதாரண சட்டத்தையே குறிக்கும், அரசியலமைப்பு திருத்தச் சட்டத்தைக் குறிக்காது என்பதால் சரத்து 368 இன் கீழான திருத்தத்தைச் சரத்து 13(2) மூலம் சவால் செய்ய முடியாது என முதன்முதலில் கூறிய உச்ச நீதிமன்றத் தீர்ப்பு எது?",
        "Shankari Prasad v. Union of India (1951)", "சங்கரி பிரசாத் எதிர் இந்திய யூனியன் (1951)",
        "Golaknath v. State of Punjab (1967)", "கோலக்நாத் எதிர் பஞ்சாப் அரசு (1967)",
        "Kesavananda Bharati v. State of Kerala (1973)", "கேசவாநந்த பாரதி எதிர் കേരള அரசு (1973)",
        "Minerva Mills v. Union of India (1980)", "மினர்வா மில்ஸ் எதிர் இந்திய யூனியன் (1980)",
        "A",
        "In Shankari Prasad (1951), the SC unanimously held that 'law' in Art 13(2) means ordinary legislative law, not constitutional amendment law under Art 368. Thus, Parliament could amend Fundamental Rights.",
        "சங்கரி பிரசாத் (1951) வழக்கில் உச்ச நீதிமன்றம் சரத்து 13(2) இல் உள்ள 'சட்டம்' என்பது சாதாரண சட்டத்தையே குறிக்கும் என்றும் 368 திருத்தத்தைக் குறிக்காது என்றும் தீர்ப்பளித்தது.",
        "Option A is correct because Shankari Prasad (1951) laid down the distinction between constituent law and ordinary law.", "விருப்பம் A சரியானது, ஏனெனில் சங்கரி பிரசாத் வழக்கு அரசியலமைப்பு உருவாக்க சட்டத்திற்கும் சாதாரண சட்டத்திற்கும் இடையிலான வேறுபாட்டை வகுத்தது.",
        "Option B is incorrect; Golaknath (1967) reversed Shankari Prasad and held 'law' INCLUDES constitutional amendments.", "விருப்பம் B தவறானது; கோலக்நாத் வழக்கு 'சட்டம்' என்பதில் திருத்தச் சட்டமும் அடங்கும் எனக் கூறி சங்கரி பிரசாத் தீர்ப்பை மாற்றியது.",
        "Option C is incorrect; Kesavananda (1973) overruled Golaknath and upheld 24th CA introducing Art 13(4) & 368(3).", "விருப்பம் C தவறானது; கேசவாநந்த பாரதி வழக்கு 24வது திருத்தத்தை உறுதி செய்து அடிப்படை அமைப்புக் கோட்பாட்டை உருவாக்கியது.",
        "Option D is incorrect; Minerva Mills (1980) dealt with basic structure application to Art 368(4)&(5).", "விருப்பம் D தவறானது; மினர்வா மில்ஸ் வழக்கு 368(4)&(5) ரத்து பற்றியது.",
        "Shankari Prasad judgment stood as settled law for 16 years until Golaknath reversed it in 1967.",
        "சங்கரி பிரசாத் தீர்ப்பு 16 ஆண்டுகள் நடைமுறையில் இருந்தது; பின்னர் 1967 இல் கோலக்நாத் வழக்கு அதை மாற்றியது.",
        "It drew a distinction between Constituent Power (Art 368) and Legislative Power (Art 245-248).",
        "இது அரசியலமைப்பு திருத்தும் அதிகாரம் மற்றும் சாதாரண சட்ட அதிகாரத்திற்கு இடையே தெளிவான வேறுபாட்டை ஏற்படுத்தியது.",
        "Analysis", "High", ["Shankari Prasad", "Article 13(2) vs Article 368"], "Part 3"
    )

    # Q006 - Correct: B
    add_q(
        "CZ_AM_HD_006",
        "Consider the following statements regarding the 44th Constitutional Amendment Act, 1978:\n1. It deleted the Right to Property from the list of Fundamental Rights.\n2. It substituted 'armed rebellion' for 'internal disturbance' in Article 352.\n3. It provided that Articles 20 and 21 cannot be suspended even during a National Emergency.\n4. It restored the term of Lok Sabha and Assemblies from 6 years to 5 years.\nWhich of the statements given above are CORRECT?",
        "44வது அரசியலமைப்பு திருத்தச் சட்டம் 1978 பற்றிய கூற்றுகளை ஆராய்க:\n1. இது சொத்துரிமையை அடிப்படை உரிமைகள் பட்டியலிலிருந்து நீக்கியது.\n2. இது சரத்து 352 இல் 'உள்நாட்டு அமைதியின்மை' என்பதற்குப் பதிலாக 'ஆயுதமேந்திய கிளர்ச்சி' என மாற்றியது.\n3. இது தேசிய அவசரநிலையின் போது கூட சரத்துகள் 20 மற்றும் 21 ஐ இடைநிறுத்தம் செய்ய முடியாது என மாற்றியது.\n4. இது மக்களவை மற்றும் சட்டமன்ற பதவிக் காலத்தை 6 ஆண்டிலிருந்து மீண்டும் 5 ஆண்டுகளாகக் குறைத்தது.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எவை சரியானவை?",
        "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
        "1, 2, 3, and 4 (All four)", "1, 2, 3, மற்றும் 4 (நான்கும்)",
        "1, 3, and 4 only", "1, 3, மற்றும் 4 மட்டுமே",
        "2, 3, and 4 only", "2, 3, மற்றும் 4 மட்டுமே",
        "B",
        "All four statements regarding the 44th CA 1978 are factually correct. It deleted Right to Property (Art 31), introduced 'armed rebellion' (Art 352), protected Arts 20 & 21 (Art 359), and restored 5-year Assembly term.",
        "44வது திருத்தச் சட்டம் 1978 தொடர்பான நான்கு கூற்றுகளும் முற்றிலும் சரியானவை. சொத்துரிமை நீக்கம், ஆயுதமேந்திய கிளர்ச்சி சொல் மாற்றம், சரத்து 20 & 21 பாதுகாப்பு, 5 ஆண்டு பதவிக் கால சீரமைப்பு ஆகிய அனைத்தையும் இது செய்தது.",
        "Option A is incorrect because statements 3 and 4 are also correct.", "விருப்பம் A தவறானது, ஏனெனில் கூற்றுகள் 3 மற்றும் 4 ம் சரியானவை.",
        "Option B is correct because all 4 statements accurately state key provisions of the 44th CA 1978.", "விருப்பம் B சரியானது, ஏனெனில் 4 கூற்றுகளும் 44வது திருத்தத்தின் முக்கிய விதிகளாகும்.",
        "Option C is incorrect because statement 2 is also correct.", "விருப்பம் C தவறானது, ஏனெனில் கூற்று 2 ம் சரியானது.",
        "Option D is incorrect because statement 1 is also correct.", "விருப்பம் D தவறானது, ஏனெனில் கூற்று 1 ம் சரியானது.",
        "44th CA 1978 was enacted by the Morarji Desai led Janata Party Government to undo the anti-democratic changes of the 42nd Amendment.",
        "44வது திருத்தச் சட்டம் 1978 ஜனதா கட்சி அரசாங்கத்தால் 42வது திருத்தத்தின் ஜனநாயக விரோத விதிகளை ரத்து செய்ய இயற்றப்பட்டது.",
        "It also introduced the provision that President can return Cabinet advice ONCE for reconsideration.",
        "அமைச்சரவை ஆலோசனையை குடியரசு தலைவர் ஒரு முறை மறுபரிசீலனைக்கு அனுப்பலாம் என்ற விதியையும் இது சேர்த்தது.",
        "Analysis", "High", ["44th Amendment Multi-statement", "Civil Liberty Restorations"], "Part 2"
    )

    # Q007 - Correct: C
    add_q(
        "CZ_AM_HD_007",
        "Which of the following constitutional provisions requires Special Majority of Parliament under Article 368 BUT DOES NOT require Ratification by State Legislatures?",
        "பின்வரும் எந்த அரசியலமைப்பு விதிக்கு சரத்து 368 இன் கீழ் நாடாளுமன்றத்தின் சிறப்பு பெரும்பான்மை தேவைப்படுகிறது, ஆனால் மாநில சட்டமன்றங்களின் ஒப்புதல் தேவை இல்லை?",
        "Election of the President and its manner (Arts 54 & 55)", "குடியரசுத் தலைவர் தேர்தல் மற்றும் அதன் முறை (சரத்துகள் 54 & 55)",
        "Extending the executive power of the Union (Art 73)", "மத்திய அரசின் நிர்வாக அதிகாரத்தை விரிவுபடுத்துதல் (சரத்து 73)",
        "Directive Principles of State Policy (Part IV)", "அரசு நெறிமுறைக் கோட்பாடுகள் (பகுதி IV)",
        "Representation of States in Parliament (4th Schedule)", "நாடாளுமன்றத்தில் மாநிலங்களின் பிரதிநிதித்துவம் (4வது அட்டவணை)",
        "C",
        "Directive Principles of State Policy (Part IV) and Fundamental Rights (Part III) require Special Majority under Article 368, but do NOT fall under the proviso requiring state ratification.",
        "அரசு நெறிமுறைக் கோட்பாடுகள் (பகுதி IV) மற்றும் அடிப்படை உரிமைகள் (பகுதி III) ஆகியவற்றைத் திருத்த சரத்து 368 இன் கீழ் சிறப்பு பெரும்பான்மை மட்டுமே தேவை; மாநில ஒப்புதல் தேவை இல்லை.",
        "Option A is incorrect because President election (Art 54 & 55) requires state ratification under Art 368(2) proviso.", "விருப்பம் A தவறானது; குடியரசு தலைவர் தேர்தலுக்கு மாநில ஒப்புதல் தேவை.",
        "Option B is incorrect because Union executive power extension (Art 73) requires state ratification.", "விருப்பம் B தவறானது; நிர்வாக அதிகாரம் விரிவாக்கத்திற்கு மாநில ஒப்புதல் தேவை.",
        "Option C is correct because DPSPs require special majority of Parliament only, not state ratification.", "விருப்பம் C சரியானது, ஏனெனில் DPSP திருத்தத்திற்கு நாடாளுமன்ற சிறப்பு பெரும்பான்மை மட்டுமே போதுமானது.",
        "Option D is incorrect because Representation of States in Parliament requires state ratification.", "விருப்பம் D தவறானது; மாநிலங்களின் பிரதிநிதித்துவத்திற்கு மாநில ஒப்புதல் தேவை.",
        "Provisions amended by Special Majority alone under Art 368: (1) Fundamental Rights, (2) Directive Principles of State Policy, (3) All other provisions not covered by simple majority or state ratification proviso.",
        "சிறப்பு பெரும்பான்மையால் மட்டுமே திருத்தப்படும் பகுதிகள்: (1) அடிப்படை உரிமைகள், (2) அரசு நெறிமுறைக் கோட்பாடுகள், (3) பிற வகைகள்.",
        "This distinction between federal and non-federal provisions is crucial for TNPSC Group 1 Polity.",
        "கூட்டாட்சி மற்றும் கூட்டாட்சி அல்லாத விதிகளுக்கிடையேயான இந்த வேறுபாடு டிஎன்பிஎஸ்சி குரூப் 1 தேர்வுக்கு மிக முக்கியமானது.",
        "Analysis", "High", ["Special Majority Only", "DPSP Amendment", "Article 368 Scope"], "Part 1"
    )

    # Q008 - Correct: D
    add_q(
        "CZ_AM_HD_008",
        "Which Constitutional Amendment Act inserted Article 243-ZD establishing District Planning Committees (DPC) and Article 243-ZE establishing Metropolitan Planning Committees (MPC)?",
        "மாவட்ட திட்டமிடல் குழுக்கள் (DPC - சரத்து 243ZD) மற்றும் பெருநகர திட்டமிடல் குழுக்கள் (MPC - சரத்து 243ZE) ஆகியவற்றை உருவாக்க வழிசெய்த அரசியலமைப்பு திருத்தச் சட்டம் எது?",
        "71st Amendment Act, 1992", "71வது திருத்தச் சட்டம், 1992",
        "73rd Amendment Act, 1992", "73வது திருத்தச் சட்டம், 1992",
        "77th Amendment Act, 1995", "77வது திருத்தச் சட்டம், 1995",
        "74th Amendment Act, 1992", "74வது திருத்தச் சட்டம், 1992",
        "D",
        "The 74th Constitutional Amendment Act, 1992 added Part IX-A containing Article 243ZD (District Planning Committee) and Article 243ZE (Metropolitan Planning Committee).",
        "74வது அரசியலமைப்பு திருத்தச் சட்டம், 1992 பகுதி IX-A ஐச் சேர்த்து அதில் சரத்து 243ZD (மாவட்ட திட்டமிடல் குழு) மற்றும் சரத்து 243ZE (பெருநகர திட்டமிடல் குழு) ஆகியவற்றை உருவாக்கியது.",
        "Option A is incorrect; 71st CA added languages to 8th Schedule.", "விருப்பம் A தவறானது; 71வது திருத்தம் மொழிகளைச் சேர்த்தது.",
        "Option B is incorrect; 73rd CA dealt with Rural Panchayats (Part IX).", "விருப்பம் B தவறானது; 73வது திருத்தம் கிராமப் பஞ்சாயத்துகள் பற்றியது.",
        "Option C is incorrect; 77th CA provided reservation in promotion for SC/STs.", "விருப்பம் C தவறானது; 77வது திருத்தம் எஸ்சி/எஸ்டி பதவி உயர்வு இடஒதுக்கீடு பற்றியது.",
        "Option D is correct because 74th CA 1992 introduced Articles 243ZD and 243ZE under Part IX-A.", "விருப்பம் D சரியானது, ஏனெனில் 74வது திருத்தம் 1992 சரத்துகள் 243ZD மற்றும் 243ZE ஐச் சேர்த்தது.",
        "District Planning Committee (DPC) consolidates plans prepared by Panchayats and Municipalities in the district (Art 243ZD).",
        "மாவட்ட திட்டமிடல் குழு (DPC) மாவட்டத்தில் உள்ள பஞ்சாயத்துகள் மற்றும் நகராட்சிகள் தயாரிக்கும் திட்டங்களை ஒருங்கிணைக்கிறது (சரத்து 243ZD).",
        "At least 4/5ths of DPC members must be elected from amongst elected members of District Panchayat and Municipalities.",
        "DPC உறுப்பினர்களில் குறைந்தபட்சம் 4/5 பங்கினர் மாவட்ட பஞ்சாயத்து மற்றும் நகராட்சிகளின் தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்களிலிருந்து தேர்ந்தெடுக்கப்பட வேண்டும்.",
        "Remembering", "High", ["74th Amendment", "District Planning Committee", "Article 243ZD"], "Part 2"
    )

    # Q009 - Correct: A
    add_q(
        "CZ_AM_HD_009",
        "Which Constitutional Amendment Act inserted Article 352(3) requiring Cabinet WRITTEN advice for declaring National Emergency, and where else does the word 'Cabinet' appear in the Constitution?",
        "தேசிய அவசரநிலை பிரகடனத்திற்கு அமைச்சரவையின் 'எழுத்துப்பூர்வ ஆலோசனை' கட்டாயம் என சரத்து 352(3) ஐச் சேர்த்த அரசியலமைப்பு திருத்தச் சட்டம் எது, மற்றும் 'அமைச்சரவை' என்ற சொல் அரசியலமைப்பில் வேறு எங்கு இடம்பெற்றுள்ளது?",
        "44th CA 1978; Nowhere else (It appears ONLY ONCE in Art 352(3))", "44வது திருத்தம் 1978; வேறு எங்கும் இல்லை (சரத்து 352(3) இல் ஒரே ஒரு முறை மட்டுமே)",
        "42nd CA 1976; Appears in Article 74 and Article 163", "42வது திருத்தம் 1976; சரத்து 74 மற்றும் 163 இல் இடம்பெற்றுள்ளது",
        "38th CA 1975; Appears in Article 75 and Article 164", "38வது திருத்தம் 1975; சரத்து 75 மற்றும் 164 இல் இடம்பெற்றுள்ளது",
        "59th CA 1988; Appears throughout Part V and Part VI", "59வது திருத்தம் 1988; பகுதி V மற்றும் VI முழுவதிலும் உள்ளது",
        "A",
        "The 44th Constitutional Amendment Act, 1978 inserted Article 352(3) requiring Cabinet WRITTEN advice. The word 'Cabinet' appears ONLY ONCE in the entire Constitution of India, in Article 352(3).",
        "44வது அரசியலமைப்பு திருத்தச் சட்டம், 1978 சரத்து 352(3) ஐச் சேர்த்து அமைச்சரவையின் எழுத்துப்பூர்வ ஆலோசனையைக் கட்டாயமாக்கியது. 'அமைச்சரவை' (Cabinet) என்ற சொல் அரசியலமைப்பில் சரத்து 352(3) இல் ஒரே ஒரு முறை மட்டுமே வருகிறது.",
        "Option A is correct because 44th CA 1978 introduced the word Cabinet in Art 352(3) and it appears nowhere else in the Constitution.", "விருப்பம் A சரியானது, ஏனெனில் 44வது திருத்தம் மட்டுமே இச்சொல்லை சேர்த்தது மற்றும் அது வேறு எங்கும் இல்லை.",
        "Option B is incorrect; Articles 74 & 163 use 'Council of Ministers', not 'Cabinet'.", "விருப்பம் B தவறானது; சரத்து 74 & 163 இல் 'அமைச்சர்கள் குழு' என்ற சொல்லே உள்ளது.",
        "Option C is incorrect; Articles 75 & 164 also use 'Council of Ministers'.", "விருப்பம் C தவறானது; சரத்து 75 & 164 லும் 'அமைச்சர்கள் குழு' என்ற சொல்லே உள்ளது.",
        "Option D is incorrect; Cabinet is not used throughout Parts V and VI.", "விருப்பம் D தவறானது; பகுதி V மற்றும் VI இல் கேபினெட் சொல் இல்லை.",
        "The word 'Cabinet' is defined in Article 352(3) as the Council consisting of Prime Minister and other Ministers of Cabinet rank under Article 75.",
        "சரத்து 352(3) இல் 'கேபினெட்' என்பது பிரதமர் மற்றும் கேபினெட் அந்தஸ்துள்ள பிற அமைச்சர்களைக் கொண்ட குழு என வரைவிலக்கணம் செய்யப்பட்டுள்ளது.",
        "This unique drafting fact is a classic TNPSC polity question.",
        "இந்த தனித்துவ வரைவு உண்மை டிஎன்பிஎஸ்சி தேர்வுகளில் அடிக்கடி கேட்கப்படும் ஒன்றாகும்.",
        "Analysis", "High", ["44th Amendment", "Cabinet Word Origin", "Article 352(3)"], "Part 2"
    )

    # Q010 - Correct: B
    add_q(
        "CZ_AM_HD_010",
        "Which Constitutional Amendment Act enacted the 93rd Amendment inserting Article 15(5) allowing OBC reservation in educational institutions, and which case upheld its validity?",
        "கல்வி நிறுவனங்களில் OBC பிரிவினருக்கு இடஒதுக்கீடு வழங்க சரத்து 15(5) ஐச் சேர்த்த 93வது திருத்தச் சட்டம் எது, மற்றும் இதன் செல்லுபடியாகும் தன்மையை உறுதி செய்த உச்ச நீதிமன்ற வழக்கு எது?",
        "Indra Sawhney v. Union of India (1992)", "இந்திரா சாவ்னி எதிர் இந்திய யூனியன் (1992)",
        "Ashok Kumar Thakur v. Union of India (2008)", "அசோக் குமார் தாக்குர் எதிர் இந்திய யூனியன் (2008)",
        "M. Nagaraj v. Union of India (2006)", "எம். நாகராஜ் எதிர் இந்திய யூனியன் (2006)",
        "Janhit Abhiyan v. Union of India (2022)", "ஜன்ஹித் அபியான் எதிர் இந்திய யூனியன் (2022)",
        "B",
        "The 93rd Constitutional Amendment Act, 2005 inserted Article 15(5). In Ashok Kumar Thakur v. Union of India (2008), a 5-judge Supreme Court bench upheld the validity of 93rd CA and 27% OBC quota in higher educational institutions.",
        "93வது அரசியலமைப்பு திருத்தச் சட்டம், 2005 சரத்து 15(5) ஐச் சேர்த்தது. அசோக் குமார் தாக்குர் எதிர் இந்திய யூனியன் (2008) வழக்கில் 5 நீதிபதிகள் அமர்வு 93வது திருத்தம் மற்றும் உயர்கல்வியில் 27% OBC இடஒதுக்கீட்டை உறுதி செய்தது.",
        "Option A is incorrect; Indra Sawhney (1992) dealt with 27% OBC job reservation under Mandal Commission.", "விருப்பம் A தவறானது; இந்திரா சாவ்னி வழக்கு 1992 வேலைவாய்ப்பு இடஒதுக்கீடு பற்றியது.",
        "Option B is correct because Ashok Kumar Thakur (2008) upheld 93rd CA Article 15(5) for Central Educational Institutions.", "விருப்பம் B சரியானது, ஏனெனில் அசோக் குமார் தாக்குர் வழக்கு (2008) 93வது திருத்தம் சரத்து 15(5) ஐ உறுதி செய்தது.",
        "Option C is incorrect; M. Nagaraj (2006) dealt with SC/ST reservations in promotions (77th, 81st, 82nd, 85th CAs).", "விருப்பம் C தவறானது; எம். நாகராஜ் வழக்கு 2006 பதவி உயர்வு இடஒதுக்கீடு பற்றியது.",
        "Option D is incorrect; Janhit Abhiyan (2022) upheld 103rd CA 2019 (EWS reservation).", "விருப்பம் D தவறானது; ஜன்ஹித் அபியான் வழக்கு 103வது திருத்தமான EWS இடஒதுக்கீட்டை உறுதி செய்தது.",
        "Ashok Kumar Thakur judgment mandated excluding the 'Creamy Layer' from OBC reservation benefits in educational institutions.",
        "அசோக் குமார் தாக்குர் தீர்ப்பு கல்வி நிறுவனங்களில் OBC இடஒதுக்கீடு பலன்களிலிருந்து 'கிரீமி லேயர்' (சடை அடுக்கு) பிரிவினரை விலக்கக் கட்டாயமாக்கியது.",
        "Article 15(5) excludes minority educational institutions under Article 30(1).",
        "சரத்து 15(5) சரத்து 30(1) இன் கீழான சிறுபான்மை கல்வி நிறுவனங்களுக்கு விலக்களிக்கிறது.",
        "Analysis", "High", ["93rd Amendment", "Ashok Kumar Thakur", "Article 15(5)"], "Part 3"
    )

    # Q011 - Correct: C
    add_q(
        "CZ_AM_HD_011",
        "In M. Nagaraj v. Union of India (2006), the Supreme Court upheld the constitutional validity of which set of Constitutional Amendments relating to SC/ST reservation in promotions?",
        "எம். நாகராஜ் எதிர் இந்திய யூனியன் (2006) வழக்கில் ஆதிதிராவிடர் மற்றும் பழங்குடியினருக்கான பதவி உயர்வு இடஒதுக்கீடு தொடர்பான எந்தெந்த அரசியலமைப்பு திருத்தங்களின் செல்லுபடியாகும் தன்மையை உச்ச நீதிமன்றம் உறுதி செய்தது?",
        "42nd, 44th, 52nd, and 61st CA", "42வது, 44வது, 52வது, மற்றும் 61வது திருத்தங்கள்",
        "65th, 69th, 73rd, and 74th CA", "65வது, 69வது, 73வது, மற்றும் 74வது திருத்தங்கள்",
        "77th, 81st, 82nd, and 85th CA", "77வது, 81வது, 82வது, மற்றும் 85வது திருத்தங்கள்",
        "86th, 89th, 91st, and 92nd CA", "86வது, 89வது, 91வது, மற்றும் 92வது திருத்தங்கள்",
        "C",
        "In M. Nagaraj (2006), a 5-judge Supreme Court bench upheld 77th CA 1995 (Art 16(4A)), 81st CA 2000 (Art 16(4B) backlog vacancies), 82nd CA 2000 (Art 335 qualifying marks relaxation), and 85th CA 2001 (consequential seniority).",
        "எம். நாகராஜ் (2006) வழக்கில் 5 நீதிபதிகள் அமர்வு 77வது, 81வது, 82வது மற்றும் 85வது திருத்தங்களின் அரசியலமைப்பு செல்லுபடியாகும் தன்மையை உறுதி செய்தது.",
        "Option A is incorrect; 42nd, 44th, 52nd, 61st CA relate to emergency, defection, voting age.", "விருப்பம் A தவறானது; இத்திருத்தங்கள் அவசரநிலை, கட்சித் தாவல், வாக்குரிமை பற்றியவை.",
        "Option B is incorrect; 65th, 69th, 73rd, 74th CA relate to NCSC, Delhi, Panchayats, Municipalities.", "விருப்பம் B தவறானது; இவை டெல்லி, உள்ளாட்சி அமைப்புகள் பற்றியவை.",
        "Option C is correct because M. Nagaraj (2006) upheld 77th, 81st, 82nd, and 85th CAs for SC/ST promotion reservations subject to 3 catch-up conditions.", "விருப்பம் C சரியானது, ஏனெனில் நாகராஜ் வழக்கு 77, 81, 82, 85 வது திருத்தங்களை உறுதி செய்தது.",
        "Option D is incorrect; 86th, 89th, 91st, 92nd CA relate to RTE, NCST, cabinet size, languages.", "விருப்பம் D தவறானது; இவை கல்வி உரிமை, NCST, மொழிகள் பற்றியவை.",
        "M. Nagaraj judgment laid down 3 mandatory conditions for SC/ST reservation in promotions: (1) Backwardness proof, (2) Inadequacy of representation, (3) Overall administrative efficiency (Art 335).",
        "நாகராஜ் தீர்ப்பு பதவி உயர்வு இடஒதுக்கீட்டிற்கு 3 நிபந்தனைகளை விதித்தது: பின்தங்கிய நிலை, போதிய பிரதிநிதித்துவமின்மை, மற்றும் நிர்வாகச் செயல்திறன்.",
        "Jarnail Singh v. Lachhmi Narain Gupta (2018) later modified the backwardness condition for SC/STs.",
        "பின்னர் ஜர்னைல் சிங் (2018) வழக்கு நாகராஜ் தீர்ப்பின் சில நிபந்தனைகளை மாற்றியமைத்தது.",
        "Analysis", "High", ["M. Nagaraj Case", "77th 81st 82nd 85th CA", "Promotion Reservation"], "Part 3"
    )

    # Q012 - Correct: D
    add_q(
        "CZ_AM_HD_012",
        "Which Constitutional Amendment Act inserted Article 31C and curtailed the Right to Property under Article 31, leading to the enactment of 26th Amendment (Privy Purses) and 29th Amendment (Kerala Land Reforms)?",
        "சரத்து 31C ஐச் சேர்த்து, சரத்து 31 இன் கீழான சொத்துரிமையைக் குறைத்து, அதன் தொடர்ச்சியாக 26வது திருத்தம் (மன்னர் மானியம் ரத்து) மற்றும் 29வது திருத்தம் (கேரள நிலச் சீர்திருத்தங்கள்) இயற்றப்படக் காரணமாக இருந்த அரசியலமைப்பு திருத்தச் சட்டம் எது?",
        "21st Amendment Act, 1967", "21வது திருத்தச் சட்டம், 1967",
        "24th Amendment Act, 1971", "24வது திருத்தச் சட்டம், 1971",
        "31st Amendment Act, 1973", "31வது திருத்தச் சட்டம், 1973",
        "25th Amendment Act, 1971", "25வது அரசியலமைப்பு திருத்தச் சட்டம், 1971",
        "D",
        "The 25th Constitutional Amendment Act, 1971 inserted Article 31C and substituted 'amount' for 'compensation' in Article 31(2), paving the way for radical land reforms and abolition of Privy Purses by 26th CA.",
        "25வது அரசியலமைப்பு திருத்தச் சட்டம், 1971 சரத்து 31C ஐச் சேர்த்து, சரத்து 31(2) இல் 'இழப்பீடு' என்பதற்குப் பதிலாக 'தொகை' என மாற்றி, நிலச் சீர்திருத்தங்களுக்கும் மன்னர் மானிய ரத்திற்கும் வழிவகுத்தது.",
        "Option A is incorrect; 21st CA added Sindhi language.", "விருப்பம் A தவறானது; 21வது திருத்தம் சிந்தி மொழியைச் சேர்த்தது.",
        "Option B is incorrect; 24th CA amended Article 368 procedural framework.", "விருப்பம் B தவறானது; 24வது திருத்தம் சரத்து 368 நடைமுறை பற்றியது.",
        "Option C is incorrect; 31st CA increased Lok Sabha seats to 545.", "விருப்பம் C தவறானது; 31வது திருத்தம் மக்களவை இடங்களை உயர்த்தியது.",
        "Option D is correct because 25th CA 1971 inserted Article 31C and modified property rights compensation scope.", "விருப்பம் D சரியானது, ஏனெனில் 25வது திருத்தம் 1971 சரத்து 31C ஐச் சேர்த்தது.",
        "24th, 25th, and 29th Constitutional Amendment Acts were together challenged in the landmark Kesavananda Bharati Case (1973).",
        "24வது, 25வது, மற்றும் 29வது அரசியலமைப்பு திருத்தச் சட்டங்கள் ஒன்றாக வரலாற்றுச் சிறப்புமிக்க கேசவாநந்த பாரதி வழக்கில் (1973) சவால் செய்யப்பட்டன.",
        "This led to the promulgation of the Basic Structure Doctrine.",
        "இதுவே அடிப்படை அமைப்புக் கோட்பாடு உருவாகக் காரணமாக அமைந்தது.",
        "Analysis", "High", ["25th Amendment", "Kesavananda Background", "Article 31C"], "Part 3"
    )

    # Q013 - Correct: A
    add_q(
        "CZ_AM_HD_013",
        "In Indira Nehru Gandhi v. Raj Narain (1975), which specific clause inserted by the 39th Constitutional Amendment Act, 1975 was struck down by the Supreme Court as violating Democracy and Judicial Review?",
        "இந்திரா நேரு காந்தி எதிர் ராஜ் நாராயண் (1975) வழக்கில் 39வது அரசியலமைப்பு திருத்தச் சட்டம் 1975 மூலம் சேர்க்கப்பட்ட எந்தப் குறிப்பிட்ட பிரிவு ஜனநாயகம் மற்றும் நீதிமன்ற மறுாய்வை மீறுவதாகக் கூறி உச்ச நீதிமன்றத்தால் ரத்து செய்யப்பட்டது?",
        "Clause (4) of Article 329A", "சரத்து 329A இன் பிரிவு (4)",
        "Clause (5) of Article 368", "சரத்து 368 இன் பிரிவு (5)",
        "Article 31C second part", "சரத்து 31C இன் இரண்டாவது பகுதி",
        "Article 359(1A)", "சரத்து 359(1A)",
        "A",
        "In Indira Gandhi (1975), Supreme Court struck down Clause (4) of Article 329A (inserted by 39th CA 1975) which placed the election disputes of Prime Minister and Speaker outside the purview of any court.",
        "இந்திரா காந்தி (1975) வழக்கில் பிரதமர் மற்றும் சபாநாயகர் தேர்தல் சர்ச்சைகளை நீதிமன்ற ஆய்விற்கு அப்பால் வைத்த 39வது திருத்தம் 1975 இன் சரத்து 329A உட்பிரிவு (4) ஐ உச்ச நீதிமன்றம் ரத்து செய்தது.",
        "Option A is correct because Article 329A(4) inserted by 39th CA 1975 was declared unconstitutional for violating democracy and judicial review.", "விருப்பம் A சரியானது, ஏனெனில் சரத்து 329A(4) இத்தீர்ப்பில் ரத்து செய்யப்பட்டது.",
        "Option B is incorrect; Art 368(5) was inserted by 42nd CA 1976 and struck down in Minerva Mills 1980.", "விருப்பம் B தவறானது; சரத்து 368(5) 42வது திருத்தத்தால் சேர்க்கப்பட்டு மினர்வா மில்ஸ் வழக்கில் ரத்து செய்யப்பட்டது.",
        "Option C is incorrect; Art 31C second part was struck down in Kesavananda Bharati 1973.", "விருப்பம் C தவறானது; 31C இரண்டாம் பகுதி கேசவாநந்த பாரதி வழக்கில் ரத்து செய்யப்பட்டது.",
        "Option D is incorrect; Art 359(1A) dealt with emergency fundamental rights suspension during 42nd/44th CA era.", "விருப்பம் D தவறானது; சரத்து 359(1A) அவசரநிலை பற்றியது.",
        "Indira Gandhi case was the FIRST instance where the Supreme Court applied the Basic Structure Doctrine to strike down a Constitutional Amendment Act.",
        "அரசியலமைப்புத் திருத்தச் சட்டத்தின் ஒரு பிரிவை ரத்து செய்ய உச்ச நீதிமன்றம் அடிப்படை அமைப்புக் கோட்பாட்டைப் பயன்படுத்திய முதல் வழக்கு இந்திரா காந்தி வழக்காகும்.",
        "Democracy, Free & Fair Elections, and Judicial Review were declared to be Basic Features of the Constitution.",
        "ஜனநாயகம், சுதந்திரமான நேர்மையான தேர்தல் மற்றும் நீதிமன்ற மறுாய்வு ஆகியவை அடிப்படை அம்சங்களாக அறிவிக்கப்பட்டன.",
        "Analysis", "High", ["Indira Gandhi Case", "39th Amendment Invalidation", "Article 329A(4)"], "Part 3"
    )

    # Q014 - Correct: B
    add_q(
        "CZ_AM_HD_014",
        "Consider the following statements regarding the 91st Constitutional Amendment Act, 2003:\n1. It limited the size of the Council of Ministers to 15% of the total strength of Lok Sabha / Assembly.\n2. It specified that the minimum number of Ministers in a State Assembly shall not be less than 12.\n3. It omitted the provision of 1/3rd split exception in the 10th Schedule (Anti-Defection Law).\n4. It added Co-operative Societies to the 8th Schedule of the Constitution.\nWhich of the statements given above are CORRECT?",
        "91வது அரசியலமைப்பு திருத்தச் சட்டம் 2003 பற்றிய கூற்றுகளை ஆராய்க:\n1. இது அமைச்சரவை அளவை மக்களவை / சட்டமன்ற மொத்த எண்ணிக்கையில் 15% எனக் கட்டுப்படுத்தியது.\n2. இது மாநில சட்டமன்றங்களில் குறைந்தபட்ச அமைச்சர்கள் எண்ணிக்கை 12 க்குக் குறையக்கூடாது என விதியமைத்தது.\n3. இது 10வது அட்டவணையில் (கட்சித் தாவல் சட்டம்) இருந்த 1/3 பிளவு விதிவிலக்கை நீக்கியது.\n4. இது கூட்டுறவு சங்கங்களை 8வது அட்டவணையில் சேர்த்தது.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எவை சரியானவை?",
        "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
        "1, 2, and 3 only", "1, 2, மற்றும் 3 மட்டுமே",
        "1, 3, and 4 only", "1, 3, மற்றும் 4 மட்டுமே",
        "2, 3, and 4 only", "2, 3, மற்றும் 4 மட்டுமே",
        "B",
        "Statements 1, 2, and 3 regarding 91st CA 2003 are correct. Statement 4 is INCORRECT because Co-operative Societies were introduced by the 97th CA 2011 (Part IX-B), not the 91st CA, and 8th Schedule is for languages.",
        "91வது திருத்தச் சட்டம் 2003 பற்றிய கூற்றுகள் 1, 2, 3 சரியானவை. கூற்று 4 தவறானது, ஏனெனில் கூட்டுறவு சங்கங்கள் 97வது திருத்தம் 2011 மூலம் பகுதி IX-B இல் சேர்க்கப்பட்டன; 8வது அட்டவணை மொழிகளுக்கானது.",
        "Option A is incorrect because statement 3 is also correct.", "விருப்பம் A தவறானது, ஏனெனில் கூற்று 3 ம் சரியானது.",
        "Option B is correct because 1, 2, and 3 accurately describe the 91st CA 2003 provisions.", "விருப்பம் B சரியானது, ஏனெனில் 1, 2, 3 ஆகிய மூன்றும் 91வது திருத்தத்தின் சரத்துகளாகும்.",
        "Option C is incorrect because statement 4 is false.", "விருப்பம் C தவறானது, ஏனெனில் கூற்று 4 தவறானது.",
        "Option D is incorrect because statement 4 is false.", "விருப்பம் D தவறானது, ஏனெனில் கூற்று 4 தவறானது.",
        "91st CA 2003 strengthened Anti-Defection Law: A defector disqualified under 10th Schedule is also disqualified from being appointed as a Minister or holding any remunerative political post under Art 75(1B) and Art 164(1B).",
        "91வது திருத்தம் 2003 கட்சித் தாவலில் தகுதிநீக்கம் செய்யப்பட்ட நபர் அமைச்சராகவோ அல்லது வருவாய் தரும் அரசியல் பதவிகளிலோ நியமிக்கப்படுவதைத் தடுத்தது.",
        "This completely eliminated wholesale defections engineered under the guise of 1/3rd splits.",
        "இது 1/3 பிளவு என்ற போர்வையில் நடத்தப்பட்ட கட்சித் தாவல்களை முற்றிலும் ஒழித்தது.",
        "Analysis", "High", ["91st Amendment Multi-statement", "Anti Defection Strengthening"], "Part 2"
    )

    # Q015 - Correct: C
    add_q(
        "CZ_AM_HD_015",
        "Which Constitutional Amendment Act substituted 'Odia' for 'Oriya' in the Eighth Schedule of the Constitution of India?",
        "இந்திய அரசியலமைப்பின் எட்டாவது அட்டவணையில் 'ஒரியா' (Oriya) என்ற சொல்லிற்குப் பதிலாக 'ஒடியா' (Odia) என மாற்றிய அரசியலமைப்பு திருத்தச் சட்டம் எது?",
        "92nd Constitutional Amendment Act, 2003", "92வது அரசியலமைப்பு திருத்தச் சட்டம், 2003",
        "94th Constitutional Amendment Act, 2006", "94வது அரசியலமைப்பு திருத்தச் சட்டம், 2006",
        "96th Constitutional Amendment Act, 2011", "96வது அரசியலமைப்பு திருத்தச் சட்டம், 2011",
        "97th Constitutional Amendment Act, 2011", "97வது அரசியலமைப்பு திருத்தச் சட்டம், 2011",
        "C",
        "The 96th Constitutional Amendment Act, 2011 substituted the word 'Odia' for 'Oriya' in entry 10 of the 8th Schedule of the Constitution.",
        "96வது அரசியலமைப்பு திருத்தச் சட்டம், 2011 எட்டாவது அட்டவணையின் 10வது வரிசையில் 'ஒரியா' என்பதற்குப் பதிலாக 'ஒடியா' என மாற்றியது.",
        "Option A is incorrect; 92nd CA 2003 added Bodo, Dogri, Maithili, Santhali.", "விருப்பம் A தவறானது; 92வது திருத்தம் 4 மொழிகளைச் சேர்த்தது.",
        "Option B is incorrect; 94th CA 2006 exempted Bihar from Tribal Minister requirement.", "விருப்பம் B தவறானது; 94வது திருத்தம் பீகார் பழங்குடியினர் நல அமைச்சர் விலக்கு பற்றியது.",
        "Option C is correct because 96th CA 2011 substituted 'Odia' for 'Oriya' in the 8th Schedule.", "விருப்பம் C சரியானது, ஏனெனில் 96வது திருத்தம் 2011 'ஒடியா' என மாற்றியது.",
        "Option D is incorrect; 97th CA 2011 added Part IX-B Co-operative Societies.", "விருப்பம் D தவறானது; 97வது திருத்தம் கூட்டுறவு சங்கங்கள் பற்றியது.",
        "Orissa state was renamed 'Odisha' by the Orissa (Alteration of Name) Act, 2011 passed alongside the 96th Amendment Act.",
        "ஒரிசா மாநிலத்தின் பெயரும் 96வது திருத்தச் சட்டத்துடன் இயற்றப்பட்ட சட்டத்தின் மூலம் 'ஒடிசா' என மாற்றப்பட்டது.",
        "This modification came into force on September 23, 2011.",
        "இந்த திருத்தம் 2011 செப்டம்பர் 23 முதல் அமலுக்கு வந்தது.",
        "Remembering", "High", ["96th Amendment", "Odia Language"], "Part 2"
    )

    # Q016 - Correct: D
    add_q(
        "CZ_AM_HD_016",
        "Regarding the 101st Constitutional Amendment Act, 2016 (GST), consider the following statements:\n1. It inserted Article 246A conferring concurrent tax power on Parliament and State Legislatures.\n2. It inserted Article 269A dealing with levy and collection of GST in inter-state trade.\n3. It inserted Article 279A empowering the President to constitute the GST Council.\n4. It required ratification by at least half of the State Legislatures before Presidential assent.\nWhich of the statements given above are CORRECT?",
        "101வது அரசியலமைப்பு திருத்தச் சட்டம் 2016 (GST) பற்றிய கூற்றுகளை ஆராய்க:\n1. இது நாடாளுமன்றத்திற்கும் மாநில சட்டமன்றங்களுக்கும் இணை வரி அதிகாரத்தை வழங்கும் சரத்து 246A ஐச் சேர்த்தது.\n2. இது மாநிலங்களுக்கிடையேயான வணிகத்தில் GST வசூல் பற்றிய சரத்து 269A ஐச் சேர்த்தது.\n3. இது GST கவுன்சிலை அமைக்க குடியரசுத் தலைவருக்கு அதிகாரமளிக்கும் சரத்து 279A ஐச் சேர்த்தது.\n4. குடியரசுத் தலைவர் ஒப்புதலுக்கு முன் இதற்கு குறைந்தது பாதி மாநில சட்டமன்றங்களின் ஒப்புதல் தேவைப்பட்டது.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எவை சரியானவை?",
        "1, 2, and 3 only", "1, 2, மற்றும் 3 மட்டுமே",
        "1 and 3 only", "1 மற்றும் 3 மட்டுமே",
        "2, 3, and 4 only", "2, 3, மற்றும் 4 மட்டுமே",
        "1, 2, 3, and 4 (All four)", "1, 2, 3, மற்றும் 4 (நான்கும்)",
        "D",
        "All four statements regarding the 101st CA 2016 are correct. GST affected 7th Schedule and state tax powers, so it required ratification by half of the State Legislatures (Assam was 1st state to ratify).",
        "101வது திருத்தச் சட்டம் 2016 பற்றிய நான்கு கூற்றுகளும் சரியானவை. GST 7வது அட்டவணை மற்றும் மாநில வரி அதிகாரத்தைப் பாதித்ததால் இதற்கு மாநிலங்களின் ஒப்புதல் தேவைப்பட்டது (அசாம் முதலில் ஒப்புதல் அளித்தது).",
        "Option A is incorrect because statement 4 is also correct.", "விருப்பம் A தவறானது, ஏனெனில் கூற்று 4 ம் சரியானது.",
        "Option B is incorrect because statements 2 and 4 are also correct.", "விருப்பம் B தவறானது, ஏனெனில் 2 மற்றும் 4 ம் சரியானவை.",
        "Option C is incorrect because statement 1 is also correct.", "விருப்பம் C தவறானது, ஏனெனில் கூற்று 1 ம் சரியானது.",
        "Option D is correct because all 4 statements accurately detail the 101st CA 2016 GST framework.", "விருப்பம் D சரியானது, ஏனெனில் 4 கூற்றுகளும் 101வது திருத்தத்தின் முக்கியமான சரத்துகளாகும்.",
        "Assam was the first State Legislative Assembly in India to ratify the 101st Constitutional Amendment Bill on August 12, 2016.",
        "2016 ஆகஸ்ட் 12 அன்று 101வது அரசியலமைப்பு திருத்த மசோதாவிற்கு ஒப்புதல் அளித்த முதல் மாநில சட்டமன்றம் அசாம் ஆகும்.",
        "GST Council voting structure: Union Government has 1/3rd weightage, all States together have 2/3rd weightage.",
        "ஜிஎஸ்டி கவுன்சில் வாக்கு கட்டமைப்பு: மத்திய அரசு 1/3 எடை, அனைத்து மாநிலங்களும் இணைந்து 2/3 எடை.",
        "Analysis", "High", ["101st Amendment Multi-statement", "GST Provisions", "State Ratification"], "Part 2"
    )

    # Q017 - Correct: A
    add_q(
        "CZ_AM_HD_017",
        "Which Constitutional Amendment Act substituted Article 338B and Article 342A granting constitutional status to the National Commission for Backward Classes (NCBC)?",
        "தேசிய பிற்படுத்தப்பட்டோர் ஆணையத்திற்கு (NCBC) அரசியலமைப்பு அந்தஸ்து வழங்க சரத்து 338B மற்றும் சரத்து 342A ஐச் சேர்த்த அரசியலமைப்பு திருத்தச் சட்டம் எது?",
        "102nd Constitutional Amendment Act, 2018", "102வது அரசியலமைப்பு திருத்தச் சட்டம், 2018",
        "100th Constitutional Amendment Act, 2015", "100வது அரசியலமைப்பு திருத்தச் சட்டம், 2015",
        "101st Constitutional Amendment Act, 2016", "101வது அரசியலமைப்பு திருத்தச் சட்டம், 2016",
        "103rd Constitutional Amendment Act, 2019", "103வது அரசியலமைப்பு திருத்தச் சட்டம், 2019",
        "A",
        "The 102nd Constitutional Amendment Act, 2018 inserted Article 338B (NCBC constitutional status) and Article 342A (SEBC notification process).",
        "102வது அரசியலமைப்பு திருத்தச் சட்டம், 2018 சரத்து 338B (NCBC அரசியலமைப்பு அந்தஸ்து) மற்றும் சரத்து 342A (SEBC அறிவிப்பு நடைமுறை) ஆகியவற்றைச் சேர்த்தது.",
        "Option A is correct because 102nd CA 2018 inserted Article 338B giving NCBC constitutional status.", "விருப்பம் A சரியானது, ஏனெனில் 102வது திருத்தம் 2018 சரத்து 338B ஐச் சேர்த்தது.",
        "Option B is incorrect; 100th CA implemented Land Boundary Agreement.", "விருப்பம் B தவறானது; 100வது திருத்தம் நில எல்லை ஒப்பந்தம் பற்றியது.",
        "Option C is incorrect; 101st CA enacted GST.", "விருப்பம் C தவறானது; 101வது திருத்தம் ஜிஎஸ்டி பற்றியது.",
        "Option D is incorrect; 103rd CA 2019 enacted 10% EWS reservation.", "விருப்பம் D தவறானது; 103வது திருத்தம் 10% EWS இடஒதுக்கீடு பற்றியது.",
        "NCBC was initially set up as a statutory body in 1993 under National Commission for Backward Classes Act, following Indra Sawhney judgment (1992).",
        "இந்திரா சாவ்னித் தீர்ப்பைத் (1992) தொடர்ந்து NCBC 1993 இல் சட்டப்பூர்வ அமைப்பாக அமைக்கப்பட்டது.",
        "102nd CA 2018 elevated it to a full constitutional body on par with NCSC and NCST.",
        "102வது திருத்தம் 2018 இதை NCSC மற்றும் NCST க்கு இணையான அரசியலமைப்பு அமைப்பாக உயர்த்தியது.",
        "Remembering", "High", ["102nd Amendment", "NCBC Article 338B", "Article 342A"], "Part 2"
    )

    # Q018 - Correct: B
    add_q(
        "CZ_AM_HD_018",
        "Which landmark Supreme Court judgment ruled by a 3:2 majority that the 103rd Constitutional Amendment Act, 2019 providing 10% EWS reservation does NOT violate the Basic Structure of the Constitution?",
        "10% EWS இடஒதுக்கீடு வழங்கும் 103வது அரசியலமைப்பு திருத்தச் சட்டம் 2019 அரசியலமைப்பின் அடிப்படை அமைப்பை மீறவில்லை என 3:2 பெரும்பான்மையில் தீர்ப்பளித்த வரலாற்றுச் சிறப்புமிக்க உச்ச நீதிமன்ற வழக்கு எது?",
        "Indra Sawhney v. Union of India (1992)", "இந்திரா சாவ்னி எதிர் இந்திய யூனியன் (1992)",
        "Janhit Abhiyan v. Union of India (2022)", "ஜன்ஹித் அபியான் எதிர் இந்திய யூனியன் (2022)",
        "M. Nagaraj v. Union of India (2006)", "எம். நாகராஜ் எதிர் இந்திய யூனியன் (2006)",
        "Ashok Kumar Thakur v. Union of India (2008)", "அசோக் குமார் தாக்குர் எதிர் இந்திய யூனியன் (2008)",
        "B",
        "In Janhit Abhiyan v. Union of India (2022), a 5-judge Supreme Court bench by 3:2 majority upheld the 103rd CA 2019, holding that reservation based purely on economic criteria does not violate basic structure.",
        "ஜன்ஹித் அபியான் எதிர் இந்திய யூனியன் (2022) வழக்கில் 5 நீதிபதிகள் அமர்வு 3:2 பெரும்பான்மையில் 103வது திருத்தத்தை உறுதி செய்து, பொருளாதார அடிப்படையிலான இடஒதுக்கீடு அடிப்படை அமைப்பை மீறாது எனத் தீர்ப்பளித்தது.",
        "Option A is incorrect; Indra Sawhney (1992) capped reservations at 50% for OBC/SC/ST.", "விருப்பம் A தவறானது; இந்திரா சாவ்னி வழக்கு இடஒதுக்கீட்டை 50% என வரம்பிட்டது.",
        "Option B is correct because Janhit Abhiyan (2022) upheld 103rd CA EWS reservation.", "விருப்பம் B சரியானது, ஏனெனில் ஜன்ஹித் அபியான் வழக்கு (2022) 103வது திருத்தத்தை உறுதி செய்தது.",
        "Option C is incorrect; M. Nagaraj (2006) dealt with SC/ST promotions.", "விருப்பம் C தவறானது; நாகராஜ் வழக்கு பதவி உயர்வு இடஒதுக்கீடு பற்றியது.",
        "Option D is incorrect; Ashok Kumar Thakur (2008) dealt with 93rd CA 2005 (OBC quota in colleges).", "விருப்பம் D தவறானது; அசோக் குமார் தாக்குர் வழக்கு 93வது திருத்தம் பற்றியது.",
        "Janhit Abhiyan verdict held that 50% ceiling rule laid down in Indra Sawhney is not inflexible for economic criteria reservations.",
        "இந்திரா சாவ்னி வழக்கில் கூறப்பட்ட 50% இடஒதுக்கீட்டு வரம்பு பொருளாதார இடஒதுக்கீட்டிற்கு மாறாத விதியாகப் பொருந்தாது என இவ்வழக்குக் கூறியது.",
        "Justices Dinesh Maheshwari, Bela M. Trivedi, and J.B. Pardiwala formed the majority; CJI U.U. Lalit and Justice S. Ravindra Bhat dissented.",
        "நீதிபதிகள் தினேஷ் மகேஸ்வரி, பெலா எம் திரிவேதி, ஜே.பி பார்திவாலா பெரும்பான்மை தீர்ப்பளித்தனர்; தலைமை நீதிபதி லலித் மற்றும் ரவீந்திர பட் மாறுபட்ட தீர்ப்பளித்தனர்.",
        "Analysis", "High", ["Janhit Abhiyan Case", "103rd Amendment EWS", "50 Percent Ceiling"], "Part 3"
    )

    # Q019 - Correct: C
    add_q(
        "CZ_AM_HD_019",
        "Which Constitutional Amendment Act substituted Article 334 to extend SC/ST reservation in Lok Sabha and Assemblies till 2030, while discontinuing the nomination of Anglo-Indians?",
        "மக்களவை மற்றும் சட்டமன்றங்களில் எஸ்சி/எஸ்டி இடஒதுக்கீட்டை 2030 வரை நீட்டித்து, ஆங்கிலோ-இந்தியர் நியமனத்தை ரத்து செய்து சரத்து 334 ஐத் திருத்திய அரசியலமைப்பு திருத்தச் சட்டம் எது?",
        "95th Constitutional Amendment Act, 2009", "95வது அரசியலமைப்பு திருத்தச் சட்டம், 2009",
        "103rd Constitutional Amendment Act, 2019", "103வது அரசியலமைப்பு திருத்தச் சட்டம், 2019",
        "104th Constitutional Amendment Act, 2020", "104வது அரசியலமைப்பு திருத்தச் சட்டம், 2020",
        "105th Constitutional Amendment Act, 2021", "105வது அரசியலமைப்பு திருத்தச் சட்டம், 2021",
        "C",
        "The 104th Constitutional Amendment Act, 2020 amended Article 334 extending SC/ST seats till January 25, 2030 and omitted the clause for Anglo-Indian nominated seats in Lok Sabha (Art 331) and Assemblies (Art 333).",
        "104வது அரசியலமைப்பு திருத்தச் சட்டம், 2020 சரத்து 334 ஐத் திருத்தி எஸ்சி/எஸ்டி இடங்களை 2030 வரை நீட்டித்தது; ஆங்கிலோ-இந்தியர் நியமன இடங்களை ரத்து செய்தது.",
        "Option A is incorrect; 95th CA (2009) extended reservation till 2020.", "விருப்பம் A தவறானது; 95வது திருத்தம் 2020 வரை நீட்டித்தது.",
        "Option B is incorrect; 103rd CA (2019) related to EWS 10% quota.", "விருப்பம் B தவறானது; 103வது திருத்தம் EWS இடஒதுக்கீடு பற்றியது.",
        "Option C is correct because 104th CA 2020 extended SC/ST reservation and ended Anglo-Indian nomination.", "விருப்பம் C சரியானது, ஏனெனில் 104வது திருத்தம் 2020 எஸ்சி/எஸ்டி நீட்டிப்பு மற்றும் ஆங்கிலோ-இந்திய நியமன ரத்தைச் செய்தது.",
        "Option D is incorrect; 105th CA (2021) restored state power over SEBC lists.", "விருப்பம் D தவறானது; 105வது திருத்தம் SEBC பட்டியல் அதிகாரம் பற்றியது.",
        "Article 331 empowered President to nominate up to 2 Anglo-Indians to Lok Sabha; Article 333 empowered Governor to nominate 1 Anglo-Indian to Assembly.",
        "சரத்து 331 குடியரசுத் தலைவர் மக்களவைக்கு 2 ஆங்கிலோ-இந்தியர்களை நியமிக்கவும், சரத்து 333 ஆளுநர் சட்டமன்றத்திற்கு 1 பேரை நியமிக்கவும் அதிகாரமளித்திருந்தன.",
        "104th CA effectively abolished this nominated representation from January 25, 2020.",
        "104வது திருத்தம் 2020 ஜனவரி 25 முதல் இந்த நியமன முறையை ரத்து செய்தது.",
        "Remembering", "High", ["104th Amendment", "Anglo Indian Abolition", "Article 334"], "Part 2"
    )

    # Q020 - Correct: D
    add_q(
        "CZ_AM_HD_020",
        "Which Constitutional Amendment Act substituted Article 342A to clarify that States and Union Territories have full power to prepare and maintain their own list of Socially and Educationally Backward Classes (SEBCs)?",
        "மாநிலங்கள் மற்றும் யூனியன் பிரதேசங்கள் தங்கள் சொந்த சமூக மற்றும் கல்வியில் பின்தங்கிய வகுப்பினரின் (SEBCs) பட்டியலை தயாரித்து பராமரிக்க முழு அதிகாரம் கொண்டுள்ளன என்பதைத் தெளிவுபடுத்த சரத்து 342A ஐத் திருத்திய அரசியலமைப்பு திருத்தச் சட்டம் எது?",
        "102nd Constitutional Amendment Act, 2018", "102வது அரசியலமைப்பு திருத்தச் சட்டம், 2018",
        "103rd Constitutional Amendment Act, 2019", "103வது அரசியலமைப்பு திருத்தச் சட்டம், 2019",
        "104th Constitutional Amendment Act, 2020", "104வது அரசியலமைப்பு திருத்தச் சட்டம், 2020",
        "105th Constitutional Amendment Act, 2021", "105வது அரசியலமைப்பு திருத்தச் சட்டம், 2021",
        "D",
        "The 105th Constitutional Amendment Act, 2021 amended Article 342A, Article 338B, and Article 366(26C) restoring the power of States to identify SEBCs independently of the Central List.",
        "105வது அரசியலமைப்பு திருத்தச் சட்டம், 2021 சரத்துகள் 342A, 338B, 366(26C) ஆகியவற்றைத் திருத்தி மத்திய பட்டியலிலிருந்து சுயாதீனமாக மாநிலங்கள் SEBC பட்டியலைத் தயாரிக்கும் அதிகாரத்தை மீட்டெடுத்தது.",
        "Option A is incorrect; 102nd CA 2018 created NCBC and original Art 342A.", "விருப்பம் A தவறானது; 102வது திருத்தம் NCBC ஐ உருவாக்கியது.",
        "Option B is incorrect; 103rd CA related to EWS 10% reservation.", "விருப்பம் B தவறானது; 103வது திருத்தம் EWS இடஒதுக்கீடு பற்றியது.",
        "Option C is incorrect; 104th CA related to SC/ST reservations.", "விருப்பம் C தவறானது; 104வது திருத்தம் எஸ்சி/எஸ்டி இடஒதுக்கீடு பற்றியது.",
        "Option D is correct because 105th CA 2021 explicitly restored State list powers over SEBCs.", "விருப்பம் D சரியானது, ஏனெனில் 105வது திருத்தம் 2021 மாநிலங்களின் SEBC அதிகாரத்தை மீட்டெடுத்தது.",
        "105th CA restored state autonomy in maintaining separate OBC lists for state jobs and state educational admissions.",
        "105வது திருத்தம் மாநிலப் பணிகள் மற்றும் உயர்கல்வி சேர்க்கைக்கு தனி OBC பட்டியலைப் பராமரிக்கும் மாநில தன்னாட்சியை மீட்டெடுத்தது.",
        "It was passed unanimously by both Houses of Parliament in August 2021.",
        "இது 2021 ஆகஸ்டில் நாடாளுமன்றத்தின் இரு அவைகளாலும் ஒருமனதாக நிறைவேற்றப்பட்டது.",
        "Remembering", "High", ["105th Amendment", "SEBC State Autonomy", "Article 342A"], "Part 2"
    )

    # Q021 - Correct: A
    add_q(
        "CZ_AM_HD_021",
        "Which Constitutional Amendment Act introduced Article 330A, Article 332A, and Article 239AA(2)(b) reserving 33% seats for women in Lok Sabha, State Legislative Assemblies, and Delhi Assembly?",
        "மக்களவை, மாநில சட்டமன்றங்கள் மற்றும் டெல்லி சட்டமன்றத்தில் பெண்களுக்கு 33% இடங்களை ஒதுக்க சரத்து 330A, சரத்து 332A மற்றும் சரத்து 239AA(2)(b) ஆகியவற்றை அறிமுகப்படுத்திய அரசியலமைப்பு திருத்தச் சட்டம் எது?",
        "106th Constitutional Amendment Act, 2023", "106வது அரசியலமைப்பு திருத்தச் சட்டம், 2023",
        "103rd Constitutional Amendment Act, 2019", "103வது அரசியலமைப்பு திருத்தச் சட்டம், 2019",
        "104th Constitutional Amendment Act, 2020", "104வது அரசியலமைப்பு திருத்தச் சட்டம், 2020",
        "105th Constitutional Amendment Act, 2021", "105வது அரசியலமைப்பு திருத்தச் சட்டம், 2021",
        "A",
        "The 106th Constitutional Amendment Act, 2023 (Nari Shakti Vandan Adhiniyam) inserted Articles 330A (Lok Sabha), 332A (State Assemblies), and amended 239AA (Delhi Assembly) reserving 1/3rd seats for women.",
        "106வது அரசியலமைப்பு திருத்தச் சட்டம், 2023 (நாரி சக்தி வந்தன் அதினியம்) மக்களவை (சரத்து 330A), மாநில சட்டமன்றங்கள் (சரத்து 332A), டெல்லி சட்டமன்றம் (சரத்து 239AA) ஆகியவற்றில் பெண்களுக்கு 1/3 பங்கு இடங்களை ஒதுக்கியது.",
        "Option A is correct because 106th CA 2023 inserted Articles 330A, 332A, and amended 239AA for women's reservation.", "விருப்பம் A சரியானது, ஏனெனில் 106வது திருத்தம் 2023 பெண்களுக்கான இடஒதுக்கீட்டை இயற்றியது.",
        "Option B is incorrect; 103rd CA 2019 introduced EWS reservation.", "விருப்பம் B தவறானது; 103வது திருத்தம் EWS இடஒதுக்கீடு பற்றியது.",
        "Option C is incorrect; 104th CA 2020 extended SC/ST seat reservation.", "விருப்பம் C தவறானது; 104வது திருத்தம் எஸ்சி/எஸ்டி இடஒதுக்கீடு பற்றியது.",
        "Option D is incorrect; 105th CA 2021 restored SEBC state list powers.", "விருப்பம் D தவறானது; 105வது திருத்தம் SEBC பட்டியல் அதிகாரம் பற்றியது.",
        "106th CA specifies that women's reservation shall continue for 15 years from commencement, unless extended by Parliament.",
        "106வது திருத்தம் பெண்களுக்கான இடஒதுக்கீடு அமலுக்கு வந்த நாளிலிருந்து 15 ஆண்டுகளுக்குத் தொடரும் எனக் கூறுகிறது.",
        "It was the first Bill passed in the newly constructed Parliament building of India in September 2023.",
        "இது 2023 செப்டம்பரில் புதிதாகக் கட்டப்பட்ட இந்திய நாடாளுமன்றக் கட்டிடத்தில் நிறைவேற்றப்பட்ட முதல் மசோதாவாகும்.",
        "Remembering", "High", ["106th Amendment", "Articles 330A 332A", "Nari Shakti Vandan"], "Part 2"
    )

    # Q022 - Correct: B
    add_q(
        "CZ_AM_HD_022",
        "In Waman Rao v. Union of India (1981), the Supreme Court clarified the applicability of the Basic Structure Doctrine to which specific schedule of the Constitution?",
        "வாமன் ராவ் எதிர் இந்திய யூனியன் (1981) வழக்கில் அரசியலமைப்பின் எந்தக் குறிப்பிட்ட அட்டவணைக்கு அடிப்படை அமைப்புக் கோட்பாட்டின் பயன்பாட்டை உச்ச நீதிமன்றம் தெளிவுபடுத்தியது?",
        "7th Schedule", "7வது அட்டவணை",
        "9th Schedule", "9வது அட்டவணை",
        "8th Schedule", "8வது அட்டவணை",
        "10th Schedule", "10வது அட்டவணை",
        "B",
        "In Waman Rao (1981), SC clarified that all amendments to the 9th Schedule enacted BEFORE April 24, 1973 are valid and protected, whereas amendments enacted AFTER April 24, 1973 are open to challenge on Basic Structure grounds.",
        "வாமன் ராவ் (1981) வழக்கில் 1973 ஏப்ரல் 24 க்கு முன் 9வது அட்டவணையில் செய்யப்பட்ட திருத்தங்கள் செல்லும் என்றும், 1973 ஏப்ரல் 24 க்குப் பின் செய்யப்பட்டவை அடிப்படை அமைப்பு அடிப்படையில் நீதிமன்ற ஆய்விற்கு உட்பட்டவை என்றும் கூறப்பட்டது.",
        "Option A is incorrect; 7th Schedule relates to legislative lists distribution.", "விருப்பம் A தவறானது; 7வது அட்டவணை அதிகாரப் பகிர்வு பற்றியது.",
        "Option B is correct because Waman Rao (1981) established the April 24, 1973 cutoff date for 9th Schedule judicial review immunity.", "விருப்பம் B சரியானது, ஏனெனில் வாமன் ராவ் வழக்கு 9வது அட்டவணைக்கான எல்லை நாளை நிர்ணயித்தது.",
        "Option C is incorrect; 8th Schedule relates to official languages.", "விருப்பம் C தவறானது; 8வது அட்டவணை ஆட்சிமொழிகள் பற்றியது.",
        "Option D is incorrect; 10th Schedule relates to Anti-Defection Law.", "விருப்பம் D தவறானது; 10வது அட்டவணை கட்சித் தாவல் தடைச் சட்டம்.",
        "Waman Rao verdict drew the line between pre-Kesavananda and post-Kesavananda 9th Schedule enactments.",
        "வாமன் ராவ் தீர்ப்பு கேசவாநந்த பாரதிக்கு முந்தைய மற்றும் பிந்தைய 9வது அட்டவணைச் சட்டங்களுக்கு இடையே எல்லைக் கோட்டை வரைந்தது.",
        "This principle was reaffirmed and consolidated by 9-judge bench in I.R. Coelho case (2007).",
        "இக்கோட்பாடு பின்னர் 2007 இல் 9 நீதிபதிகள் கொண்ட கொஹெலோ அமர்வால் மேலும் உறுதி செய்யப்பட்டது.",
        "Understanding", "High", ["Waman Rao Case", "9th Schedule Cutoff", "April 24 1973"], "Part 3"
    )

    # Q023 - Correct: C
    add_q(
        "CZ_AM_HD_023",
        "Which Constitutional Amendment Act inserted Article 312(1) allowing Parliament to create All India Judicial Service (AIJS) by law passed by Rajya Sabha with 2/3rd majority?",
        "மாநிலங்களவையில் 2/3 பங்கு பெரும்பான்மையுடன் சட்டம் இயற்றுவதன் மூலம் அகில இந்திய நீதிபதிகள் பணியை (AIJS) உருவாக்க நாடாளுமன்றத்திற்கு அதிகாரமளிக்கும் சரத்து 312(1) திருத்தத்தை எந்த அரசியலமைப்பு திருத்தச் சட்டம் செய்தது?",
        "24th Constitutional Amendment Act, 1971", "24வது அரசியலமைப்பு திருத்தச் சட்டம், 1971",
        "44th Constitutional Amendment Act, 1978", "44வது அரசியலமைப்பு திருத்தச் சட்டம், 1978",
        "42nd Constitutional Amendment Act, 1976", "42வது அரசியலமைப்பு திருத்தச் சட்டம், 1976",
        "73rd Constitutional Amendment Act, 1992", "73வது அரசியலமைப்பு திருத்தச் சட்டம், 1992",
        "C",
        "The 42nd Constitutional Amendment Act, 1976 amended Article 312 to include All India Judicial Service (AIJS) among the All-India Services that Parliament can create by law following a Rajya Sabha resolution.",
        "42வது அரசியலமைப்பு திருத்தச் சட்டம், 1976 சரத்து 312 ஐத் திருத்தி, மாநிலங்களவைத் தீர்மானத்தைத் தொடர்ந்து நாடாளுமன்றம் உருவாக்கக்கூடிய அகில இந்தியப் பணிகளில் அகில இந்திய நீதிபதிகள் பணியையும் (AIJS) சேர்த்தது.",
        "Option A is incorrect; 24th CA related to Article 368 amending power.", "விருப்பம் A தவறானது; 24வது திருத்தம் சரத்து 368 திருத்த அதிகாரம் பற்றியது.",
        "Option B is incorrect; 44th CA related to civil liberty restorations.", "விருப்பம் B தவறானது; 44வது திருத்தம் சிவில் உரிமைகள் சீரமைப்பு பற்றியது.",
        "Option C is correct because 42nd CA 1976 amended Article 312 to enable AIJS creation.", "விருப்பம் C சரியானது, ஏனெனில் 42வது திருத்தம் 1976 சரத்து 312 இல் AIJS ஐச் சேர்த்தது.",
        "Option D is incorrect; 73rd CA related to Panchayati Raj.", "விருப்பம் D தவறானது; 73வது திருத்தம் பஞ்சாயத்து ராஜ் பற்றியது.",
        "Article 312 specifies that AIJS shall not include any post inferior to that of a District Judge.",
        "சரத்து 312 அகில இந்திய நீதிபதிகள் பணியில் மாவட்ட நீதிபதி பதவிக்குக் கீழான எந்தப் பதவியும் இருக்கக்கூடாது எனக் கூறுகிறது.",
        "Creation of AIJS requires Rajya Sabha resolution supported by not less than 2/3rds of members present and voting under Article 312(1).",
        "AIJS உருவாக்க மாநிலங்களவையில் வருகை தந்து வாக்களிப்பவர்களில் 2/3 பங்கு உறுப்பினர்களின் ஆதரவுடன் தீர்மானம் நிறைவேற்றப்பட வேண்டும்.",
        "Remembering", "High", ["42nd Amendment", "Article 312", "All India Judicial Service"], "Part 2"
    )

    # Q024 - Correct: D
    add_q(
        "CZ_AM_HD_024",
        "Which Constitutional Amendment Act replaced the 1/3rd split exception in the 10th Schedule (Anti-Defection Law) with the requirement of a 2/3rd merger exception?",
        "10வது அட்டவணையில் (கட்சித் தாவல் சட்டம்) இருந்த 1/3 பிளவு விதிவிலக்கை நீக்கி, 2/3 இணைப்பு விதிவிலக்குத் தேவையை எந்த அரசியலமைப்பு திருத்தச் சட்டம் கட்டாயமாக்கியது?",
        "52nd Constitutional Amendment Act, 1985", "52வது அரசியலமைப்பு திருத்தச் சட்டம், 1985",
        "61st Constitutional Amendment Act, 1988", "61வது அரசியலமைப்பு திருத்தச் சட்டம், 1988",
        "84th Constitutional Amendment Act, 2001", "84வது அரசியலமைப்பு திருத்தச் சட்டம், 2001",
        "91st Constitutional Amendment Act, 2003", "91வது அரசியலமைப்பு திருத்தச் சட்டம், 2003",
        "D",
        "The 91st Constitutional Amendment Act, 2003 deleted Paragraph 3 of the 10th Schedule (which allowed disqualification immunity for 1/3rd splits), leaving ONLY Paragraph 4 (merger requiring 2/3rds approval of members).",
        "91வது அரசியலமைப்பு திருத்தச் சட்டம், 2003 10வது அட்டவணையின் 3வது பத்தியை (1/3 பிளவு விதிவிலக்கு) நீக்கி, 4வது பத்தியை (2/3 உறுப்பினர்கள் ஒப்புதலுடன் இணைப்பு) மட்டுமே சட்டப்பூர்வமாக்கியது.",
        "Option A is incorrect; 52nd CA 1985 originally created the 10th Schedule with the 1/3rd split provision.", "விருப்பம் A தவறானது; 52வது திருத்தம் 1985 இல் 1/3 பிளவு விதியைக் கொண்டு வந்தது.",
        "Option B is incorrect; 61st CA lowered voting age to 18.", "விருப்பம் B தவறானது; 61வது திருத்தம் வாக்குரிமை வயதைக் குறைத்தது.",
        "Option C is incorrect; 84th CA froze seat delimitation till 2026.", "விருப்பம் C தவறானது; 84வது திருத்தம் தொகுதி முடக்கம் பற்றியது.",
        "Option D is correct because 91st CA 2003 omitted the 1/3rd split exception in 10th Schedule.", "விருப்பம் D சரியானது, ஏனெனில் 91வது திருத்தம் 2003 1/3 பிளவு விதிவிலக்கை நீக்கியது.",
        "Under 10th Schedule Paragraph 4, a merger of a political party is recognized only if not less than 2/3rds of the members of the legislature party agree to such merger.",
        "10வது அட்டவணை 4வது பத்தியின் படி, சட்டமன்றக் கட்சி உறுப்பினர்களில் 2/3 பங்கிற்குக் குறையாதவர்கள் சம்மதித்தால் மட்டுமே கட்சி இணைப்பு அங்கீகரிக்கப்படும்.",
        "This plug was introduced to curb opportunistic political defections.",
        "அரசியல் கட்சித் தாவல்களைத் தடுக்க இந்தத் திருத்தம் கொண்டுவரப்பட்டது.",
        "Analysis", "High", ["91st Amendment", "Anti Defection Split Deletion", "2/3 Merger"], "Part 2"
    )

    # Q025 - Correct: A
    add_q(
        "CZ_AM_HD_025",
        "Which Constitutional Amendment Act raised the retirement age of High Court Judges from 60 years to 62 years and extended the jurisdiction of High Courts to Union Territories?",
        "உயர் நீதிமன்ற நீதிபதிகளின் பணி ஓய்வு வயதை 60 லிருந்து 62 ஆக உயர்த்தி, யூனியன் பிரதேசங்களுக்கும் உயர் நீதிமன்றங்களின் அதிகார வரம்பை விரிவுபடுத்திய அரசியலமைப்பு திருத்தச் சட்டம் எது?",
        "15th Constitutional Amendment Act, 1963", "15வது அரசியலமைப்பு திருத்தச் சட்டம், 1963",
        "7th Constitutional Amendment Act, 1956", "7வது அரசியலமைப்பு திருத்தச் சட்டம், 1956",
        "42nd Constitutional Amendment Act, 1976", "42வது அரசியலமைப்பு திருத்தச் சட்டம், 1976",
        "44th Constitutional Amendment Act, 1978", "44வது அரசியலமைப்பு திருத்தச் சட்டம், 1978",
        "A",
        "The 15th Constitutional Amendment Act, 1963 amended Article 217 raising retirement age of HC judges from 60 to 62 years, amended Article 226 enabling HCs to issue writs outside territorial jurisdiction if cause of action arises within, and enabled appointment of retired HC judges as acting judges.",
        "15வது அரசியலமைப்பு திருத்தச் சட்டம், 1963 சரத்து 217 ஐத் திருத்தி உயர் நீதிமன்ற நீதிபதிகளின் ஓய்வு வயதை 60 லிருந்து 62 ஆக உயர்த்தியது, மற்றும் சரத்து 226 இன் கீழ் ரிட் அதிகார வரம்பை விரிவுபடுத்தியது.",
        "Option A is correct because 15th CA 1963 raised HC judges retirement age to 62 years.", "விருப்பம் A சரியானது, ஏனெனில் 15வது திருத்தம் 1963 உயர் நீதிமன்ற நீதிபதிகளின் ஓய்வு வயதை 62 ஆக உயர்த்தியது.",
        "Option B is incorrect; 7th CA 1956 provided for common HCs for two or more states.", "விருப்பம் B தவறானது; 7வது திருத்தம் பொது உயர் நீதிமன்றங்களை அமைத்தது.",
        "Option C is incorrect; 42nd CA 1976 introduced administrative tribunals.", "விருப்பம் C தவறானது; 42வது திருத்தம் நிர்வாகத் தீர்ப்பாயங்களைக் கொண்டு வந்தது.",
        "Option D is incorrect; 44th CA 1978 restored writ jurisdiction powers.", "விருப்பம் D தவறானது; 44வது திருத்தம் ரிட் அதிகாரங்களை மீட்டெடுத்தது.",
        "Supreme Court judges retirement age is 65 years (fixed by original Constitution), whereas HC judges retirement age was raised from 60 to 62 by 15th CA 1963.",
        "உச்ச நீதிமன்ற நீதிபதிகளின் ஓய்வு வயது 65 ஆண்டுகள்; உயர் நீதிமன்ற நீதிபதிகளின் ஓய்வு வயது 15வது திருத்தத்தால் 60 லிருந்து 62 ஆக உயர்த்தப்பட்டது.",
        "104th Constitution Amendment Bill proposed raising HC judges age to 65, but was not enacted.",
        "உயர் நீதிமன்ற நீதிபதிகள் ஓய்வு வயதை 65 ஆக உயர்த்த கொண்டுவரப்பட்ட 104வது மசோதா நிறைவேற்றப்படவில்லை.",
        "Remembering", "High", ["15th Amendment", "High Court Judges Retirement Age 62"], "Part 2"
    )

    # Q026 - Correct: B
    add_q(
        "CZ_AM_HD_026",
        "Which Constitutional Amendment Act exempted the State of Bihar from the requirement of having a Minister in charge of Tribal Welfare under Article 164(1)?",
        "சரத்து 164(1) இன் கீழ் பழங்குடியினர் நலனுக்கென ஒரு தனி அமைச்சரைக் கட்டாயமாக நியமிப்பதிலிருந்து பீகார் மாநிலத்திற்கு விலக்களித்த அரசியலமைப்பு திருத்தச் சட்டம் எது?",
        "89th Constitutional Amendment Act, 2003", "89வது அரசியலமைப்பு திருத்தச் சட்டம், 2003",
        "94th Constitutional Amendment Act, 2006", "94வது அரசியலமைப்பு திருத்தச் சட்டம், 2006",
        "91st Constitutional Amendment Act, 2003", "91வது அரசியலமைப்பு திருத்தச் சட்டம், 2003",
        "83rd Constitutional Amendment Act, 2000", "83வது அரசியலமைப்பு திருத்தச் சட்டம், 2000",
        "B",
        "The 94th Constitutional Amendment Act, 2006 amended Article 164(1) proviso, freeing Bihar from the requirement of having a Tribal Welfare Minister (since Jharkhand was carved out of Bihar in 2000) and extending the requirement to Chhattisgarh, Jharkhand, Madhya Pradesh, and Odisha.",
        "94வது அரசியலமைப்பு திருத்தச் சட்டம், 2006 சரத்து 164(1) இன் வரம்புரையைத் திருத்தி, பீகாரை பழங்குடியினர் நல அமைச்சர் நியமனக் கட்டாயத்திலிருந்து விலக்கி, அதை சத்தீஸ்கர், ஜார்கண்ட், மத்திய பிரதேசம், ஒடிசா ஆகிய மாநிலங்களுக்கு விரிவாக்கியது.",
        "Option A is incorrect; 89th CA 2003 bifurcated NCSC and NCST.", "விருப்பம் A தவறானது; 89வது திருத்தம் எஸ்சி/எஸ்டி ஆணையங்களைப் பிரித்தது.",
        "Option B is correct because 94th CA 2006 exempted Bihar and included Chhattisgarh and Jharkhand under Art 164(1).", "விருப்பம் B சரியானது, ஏனெனில் 94வது திருத்தம் 2006 பீகாருக்கு விலக்களித்து சத்தீஸ்கர், ஜார்கண்டைச் சேர்த்தது.",
        "Option C is incorrect; 91st CA 2003 capped cabinet size at 15%.", "விருப்பம் C தவறானது; 91வது திருத்தம் 15% அமைச்சரவை வரம்பு பற்றியது.",
        "Option D is incorrect; 83rd CA 2000 exempted Arunachal Pradesh Panchayats from SC reservation.", "விருப்பம் D தவறானது; 83வது திருத்தம் அருணாச்சலப் பிரதேச SC விலக்கு பற்றியது.",
        "Original Article 164(1) mandated Tribal Welfare Ministers in Bihar, Madhya Pradesh, and Orissa.",
        "மூல சரத்து 164(1) பீகார், மத்திய பிரதேசம் மற்றும் ஒரிசாவில் பழங்குடியினர் நல அமைச்சரைக் கட்டாயமாக்கியிருந்தது.",
        "With Jharkhand created out of Bihar in 2000, 94th CA substituted Jharkhand and Chhattisgarh for Bihar.",
        "2000 இல் பீகாரிலிருந்து ஜார்கண்ட் பிரிக்கப்பட்டதால் 94வது திருத்தம் இம்மாற்றத்தைச் செய்தது.",
        "Remembering", "High", ["94th Amendment", "Article 164(1) Tribal Minister Exemption"], "Part 2"
    )

    # Q027 - Correct: C
    add_q(
        "CZ_AM_HD_027",
        "Which Constitutional Amendment Act added Article 16(4A) allowing state reservations in promotion for SCs and STs, overriding the 50% restriction imposed in Indra Sawhney case?",
        "இந்திரா சாவ்னி வழக்கில் விதிக்கப்பட்ட கட்டுப்பாட்டை மீறி, ஆதிதிராவிடர் மற்றும் பழங்குடியினருக்குப் பதவி உயர்வில் இடஒதுக்கீடு வழங்க அரசுக்கு அதிகாரமளிக்கும் சரத்து 16(4A) ஐச் சேர்த்த அரசியலமைப்பு திருத்தச் சட்டம் எது?",
        "73rd Constitutional Amendment Act, 1992", "73வது அரசியலமைப்பு திருத்தச் சட்டம், 1992",
        "74th Constitutional Amendment Act, 1992", "74வது அரசியலமைப்பு திருத்தச் சட்டம், 1992",
        "77th Constitutional Amendment Act, 1995", "77வது அரசியலமைப்பு திருத்தச் சட்டம், 1995",
        "81st Constitutional Amendment Act, 2000", "81வது அரசியலமைப்பு திருத்தச் சட்டம், 2000",
        "C",
        "The 77th Constitutional Amendment Act, 1995 inserted Article 16(4A) enabling the State to provide reservation in promotion to SCs and STs if they are not adequately represented in state services.",
        "77வது அரசியலமைப்பு திருத்தச் சட்டம், 1995 சரத்து 16(4A) ஐச் சேர்த்து, அரசுப் பணிகளில் போதிய பிரதிநிதித்துவம் பெறாத எஸ்சி மற்றும் எஸ்டி பிரிவினருக்குப் பதவி உயர்வில் இடஒதுக்கீடு வழங்க அரசுக்கு அதிகாரமளித்தது.",
        "Option A is incorrect; 73rd CA 1992 dealt with Panchayati Raj.", "விருப்பம் A தவறானது; 73வது திருத்தம் பஞ்சாயத்து ராஜ் பற்றியது.",
        "Option B is incorrect; 74th CA 1992 dealt with Municipalities.", "விருப்பம் B தவறானது; 74வது திருத்தம் நகராட்சிகள் பற்றியது.",
        "Option C is correct because 77th CA 1995 inserted Article 16(4A) into the Constitution.", "விருப்பம் C சரியானது, ஏனெனில் 77வது திருத்தம் 1995 சரத்து 16(4A) ஐச் சேர்த்தது.",
        "Option D is incorrect; 81st CA 2000 inserted Article 16(4B) for backlog vacancies.", "விருப்பம் D தவறானது; 81வது திருத்தம் சரத்து 16(4B) நிரப்பப்படாத இடங்கள் பற்றியது.",
        "Indra Sawhney (1992) held that reservation under Article 16(4) applies ONLY to initial appointment, not promotion; 77th CA nullified this restriction.",
        "இந்திரா சாவ்னி வழக்கு (1992) இடஒதுக்கீடு ஆரம்ப நியமனத்திற்கு மட்டுமே பொருந்தும் பதவி உயர்வுக்குப் பொருந்தாது என்றது; 77வது திருத்தம் இதை ரத்து செய்தது.",
        "77th CA was later upheld by 5-judge bench in M. Nagaraj case (2006).",
        "77வது திருத்தம் பின்னர் 2006 இல் எம். நாகராஜ் வழக்கில் உறுதி செய்யப்பட்டது.",
        "Remembering", "High", ["77th Amendment", "Article 16(4A)", "Promotion Reservation"], "Part 2"
    )

    # Q028 - Correct: D
    add_q(
        "CZ_AM_HD_028",
        "Which Constitutional Amendment Act inserted Article 16(4B) permitting the State to treat unfilled reserved backlog vacancies of a year as a separate class of vacancies, uninfluenced by the 50% ceiling limit?",
        "ஒரு ஆண்டின் நிரப்பப்படாத ஒதுக்கப்பட்ட காலியிடங்களை (Backlog vacancies) 50% உச்சவரம்பு வரம்பால் பாதிக்கப்படாமல் ஒரு தனித்துவமான வகுப்பாகக் கருதி நிரப்ப அனுமதிக்கும் சரத்து 16(4B) ஐச் சேர்த்த அரசியலமைப்பு திருத்தச் சட்டம் எது?",
        "77th Constitutional Amendment Act, 1995", "77வது அரசியலமைப்பு திருத்தச் சட்டம், 1995",
        "82nd Constitutional Amendment Act, 2000", "82வது அரசியலமைப்பு திருத்தச் சட்டம், 2000",
        "85th Constitutional Amendment Act, 2001", "85வது அரசியலமைப்பு திருத்தச் சட்டம், 2001",
        "81st Constitutional Amendment Act, 2000", "81வது அரசியலமைப்பு திருத்தச் சட்டம், 2000",
        "D",
        "The 81st Constitutional Amendment Act, 2000 inserted Article 16(4B) ending the 50% ceiling restriction on carry-forward backlog vacancies for SCs and STs.",
        "81வது அரசியலமைப்பு திருத்தச் சட்டம், 2000 சரத்து 16(4B) ஐச் சேர்த்து எஸ்சி மற்றும் எஸ்டி பிரிவினரின் நிரப்பப்படாத காலியிடங்கள் (Backlog) மீதான 50% இடஒதுக்கீட்டு உச்சவரம்பை நீக்கியது.",
        "Option A is incorrect; 77th CA 1995 inserted Article 16(4A) for promotion reservation.", "விருப்பம் A தவறானது; 77வது திருத்தம் சரத்து 16(4A) பதவி உயர்வு பற்றியது.",
        "Option B is incorrect; 82nd CA 2000 amended Article 335 for qualifying marks relaxation.", "விருப்பம் B தவறானது; 82வது திருத்தம் சரத்து 335 தகுதி மதிப்பெண் தளர்வு பற்றியது.",
        "Option C is incorrect; 85th CA 2001 provided consequential seniority.", "விருப்பம் C தவறானது; 85வது திருத்தம் தொடர்ச்சியான பணிமூப்பு பற்றியது.",
        "Option D is correct because 81st CA 2000 inserted Article 16(4B) for backlog vacancies.", "விருப்பம் D சரியானது, ஏனெனில் 81வது திருத்தம் 2000 சரத்து 16(4B) ஐச் சேர்த்தது.",
        "Article 16(4B) allows backlog vacancies to be filled up without considering them together with current year vacancies for calculating the 50% limit.",
        "சரத்து 16(4B) நிரப்பப்படாத காலியிடங்களை தற்போதைய ஆண்டின் காலியிடங்களுடன் சேர்த்து 50% வரம்பைக் கணக்கிடாமல் தனிப் பிரிவாக நிரப்ப அனுமதிக்கிறது.",
        "It was upheld by Supreme Court in M. Nagaraj v. Union of India (2006).",
        "இது எம். நாகராஜ் எதிர் இந்திய யூனியன் (2006) வழக்கில் உச்ச நீதிமன்றத்தால் உறுதி செய்யப்பட்டது.",
        "Remembering", "High", ["81st Amendment", "Article 16(4B)", "Backlog Vacancies 50 Percent Limit"], "Part 2"
    )

    # Q029 - Correct: A
    add_q(
        "CZ_AM_HD_029",
        "Which Constitutional Amendment Act amended Article 335 enabling relaxation in qualifying marks and lowering standards of evaluation for SCs and STs in public sector promotions?",
        "அரசுப் பணிப் பதவி உயர்வுகளில் ஆதிதிராவிடர் மற்றும் பழங்குடியினருக்குத் தகுதி மதிப்பெண்களில் தளர்வு மற்றும் மதிப்பீட்டுத் தரங்களைக் குறைக்க வழிவகுக்கும் சரத்து 335 ஐத் திருத்திய அரசியலமைப்பு திருத்தச் சட்டம் எது?",
        "82nd Constitutional Amendment Act, 2000", "82வது அரசியலமைப்பு திருத்தச் சட்டம், 2000",
        "81st Constitutional Amendment Act, 2000", "81வது அரசியலமைப்பு திருத்தச் சட்டம், 2000",
        "85th Constitutional Amendment Act, 2001", "85வது அரசியலமைப்பு திருத்தச் சட்டம், 2001",
        "77th Constitutional Amendment Act, 1995", "77வது அரசியலமைப்பு திருத்தச் சட்டம், 1995",
        "A",
        "The 82nd Constitutional Amendment Act, 2000 inserted a proviso to Article 335 restoring the power of the State to relax qualifying marks in examinations or lower evaluation standards for SC/ST promotion candidates.",
        "82வது அரசியலமைப்பு திருத்தச் சட்டம், 2000 சரத்து 335 இல் ஒரு வரம்புரையைச் சேர்த்து, எஸ்சி/எஸ்டி பதவி உயர்வு தேர்வுகளில் தகுதி மதிப்பெண் தளர்வு மற்றும் மதிப்பீட்டுத் தரத்தைக் குறைக்கும் அதிகாரத்தை மீட்டெடுத்தது.",
        "Option A is correct because 82nd CA 2000 amended Article 335.", "விருப்பம் A சரியானது, ஏனெனில் 82வது திருத்தம் 2000 சரத்து 335 ஐத் திருத்தியது.",
        "Option B is incorrect; 81st CA 2000 inserted Article 16(4B) for backlog vacancies.", "விருப்பம் B தவறானது; 81வது திருத்தம் சரத்து 16(4B) பற்றியது.",
        "Option C is incorrect; 85th CA 2001 inserted consequential seniority.", "விருப்பம் C தவறானது; 85வது திருத்தம் பணிமூப்பு பற்றியது.",
        "Option D is incorrect; 77th CA 1995 inserted Article 16(4A).", "விருப்பம் D தவறானது; 77வது திருத்தம் சரத்து 16(4A) பற்றியது.",
        "82nd CA nullified Supreme Court ruling in S. Vinod Kumar (1996) which had barred qualifying marks relaxation.",
        "82வது திருத்தம் மதிப்பெண் தளர்வைத் தடுத்த வினோத் குமார் (1996) வழக்குத் தீர்ப்பை ரத்து செய்தது.",
        "Article 335 balances reservation claims of SCs and STs with the maintenance of efficiency of administration.",
        "சரத்து 335 எஸ்சி/எஸ்டி இடஒதுக்கீட்டுக் கோரிக்கைகளை நிர்வாகச் செயல்திறனுடன் சமப்படுத்துகிறது.",
        "Remembering", "High", ["82nd Amendment", "Article 335", "Qualifying Marks Relaxation"], "Part 2"
    )

    # Q030 - Correct: B
    add_q(
        "CZ_AM_HD_030",
        "Which Constitutional Amendment Act amended Article 16(4A) to grant 'consequential seniority' to SC and ST government servants promoted on the basis of reservation?",
        "இடஒதுக்கீட்டின் அடிப்படையில் பதவி உயர்வு பெறும் எஸ்சி மற்றும் எஸ்டி அரசு ஊழியர்களுக்கு 'தொடர்ச்சியான பணிமூப்பு' (Consequential Seniority) வழங்க சரத்து 16(4A) ஐத் திருத்திய அரசியலமைப்பு திருத்தச் சட்டம் எது?",
        "77th Constitutional Amendment Act, 1995", "77வது அரசியலமைப்பு திருத்தச் சட்டம், 1995",
        "85th Constitutional Amendment Act, 2001", "85வது அரசியலமைப்பு திருத்தச் சட்டம், 2001",
        "81st Constitutional Amendment Act, 2000", "81வது அரசியலமைப்பு திருத்தச் சட்டம், 2000",
        "82nd Constitutional Amendment Act, 2000", "82வது அரசியலமைப்பு திருத்தச் சட்டம், 2000",
        "B",
        "The 85th Constitutional Amendment Act, 2001 amended Article 16(4A) with retrospective effect from June 17, 1995 to grant 'consequential seniority' to SC/ST candidates promoted by reservation.",
        "85வது அரசியலமைப்பு திருத்தச் சட்டம், 2001 சரத்து 16(4A) ஐ 1995 ஜூன் 17 முதல் முன் தேதியிட்டுத் திருத்தி எஸ்சி/எஸ்டி பணியாளர்களுக்குத் 'தொடர்ச்சியான பணிமூப்பு' (Consequential Seniority) வழங்கியது.",
        "Option A is incorrect; 77th CA 1995 introduced Article 16(4A) initially without consequential seniority clause.", "விருப்பம் A தவறானது; 77வது திருத்தம் ஆரம்பத்தில் இச்சொல்லைக் கொண்டிருக்கவில்லை.",
        "Option B is correct because 85th CA 2001 substituted the words 'in matters of promotion, with consequential seniority, to any class' in Article 16(4A).", "விருப்பம் B சரியானது, ஏனெனில் 85வது திருத்தம் 2001 'தொடர்ச்சியான பணிமூப்பு' என்ற சொல்லைச் சேர்த்தது.",
        "Option C is incorrect; 81st CA 2000 related to backlog vacancies.", "விருப்பம் C தவறானது; 81வது திருத்தம் காலியிடங்கள் பற்றியது.",
        "Option D is incorrect; 82nd CA 2000 related to Article 335 relaxation.", "விருப்பம் D தவறானது; 82வது திருத்தம் சரத்து 335 பற்றியது.",
        "85th CA nullified the 'Catch-up Rule' laid down by Supreme Court in Ajit Singh II (1999) and Sabharwal (1995) cases.",
        "85வது திருத்தம் அஜித் சிங் II (1999) வழக்கில் உச்ச நீதிமன்றம் வழங்கிய 'கேட்ச்-அப் விதியை' ரத்து செய்தது.",
        "85th CA was upheld by Supreme Court in M. Nagaraj case (2006).",
        "85வது திருத்தம் எம். நாகராஜ் (2006) வழக்கில் உச்ச நீதிமன்றத்தால் உறுதி செய்யப்பட்டது.",
        "Remembering", "High", ["85th Amendment", "Article 16(4A)", "Consequential Seniority"], "Part 2"
    )

    # Q031 - Correct: C
    add_q(
        "CZ_AM_HD_031",
        "Which Constitutional Amendment Act substituted Article 81 and Article 170 to freeze total seats in Lok Sabha and Assemblies till 2026 based on 1991 Census figures?",
        "1991 மக்கள் தொகை கணக்கெடுப்பின் அடிப்படையில் மக்களவை மற்றும் சட்டமன்றங்களின் மொத்த இடங்களை 2026 வரை முடக்க சரத்துகள் 81 மற்றும் 170 ஐத் திருத்திய அரசியலமைப்பு திருத்தச் சட்டம் எது?",
        "42nd Constitutional Amendment Act, 1976", "42வது அரசியலமைப்பு திருத்தச் சட்டம், 1976",
        "87th Constitutional Amendment Act, 2003", "87வது அரசியலமைப்பு திருத்தச் சட்டம், 2003",
        "84th Constitutional Amendment Act, 2001", "84வது அரசியலமைப்பு திருத்தச் சட்டம், 2001",
        "91st Constitutional Amendment Act, 2003", "91வது அரசியலமைப்பு திருத்தச் சட்டம், 2003",
        "C",
        "The 84th Constitutional Amendment Act, 2001 amended Articles 81, 82, 170, and 330 extending the freeze on constituency seat allocations till 2026 and specifying 1991 Census figures for internal delimitation.",
        "84வது அரசியலமைப்பு திருத்தச் சட்டம், 2001 சரத்துகள் 81, 82, 170, 330 ஐத் திருத்தி தொகுதி இடங்கள் ஒதுக்கீட்டை 2026 வரை நீட்டித்து 1991 கணக்கெடுப்பைக் குறிப்பிட்டது.",
        "Option A is incorrect; 42nd CA 1976 froze seats till 2000 based on 1971 Census.", "விருப்பம் A தவறானது; 42வது திருத்தம் 1971 கணக்கெடுப்பு படி 2000 வரை முடக்கியது.",
        "Option B is incorrect; 87th CA 2003 substituted 2001 Census for 1991 Census.", "விருப்பம் B தவறானது; 87வது திருத்தம் 2001 கணக்கெடுப்பை மாற்றியது.",
        "Option C is correct because 84th CA 2001 enacted the 2026 seat allocation freeze.", "விருப்பம் C சரியானது, ஏனெனில் 84வது திருத்தம் 2001 2026 தொகுதி முடக்கத்தை இயற்றியது.",
        "Option D is incorrect; 91st CA 2003 dealt with Council of Ministers 15% cap.", "விருப்பம் D தவறானது; 91வது திருத்தம் 15% அமைச்சரவை வரம்பு பற்றியது.",
        "The 84th CA was designed to ensure that state population control achievements do not lead to loss of parliamentary representation.",
        "மாநிலங்களின் மக்கள் தொகை கட்டுப்பாட்டு சாதனைகள் நாடாளுமன்றப் பிரதிநிதித்துவ இழப்பிற்கு வழிவகுக்கக்கூடாது என்பதற்காக 84வது திருத்தம் செய்யப்பட்டது.",
        "Post-2026 census delimitation will readjust state-wise seat allocations.",
        "2026 க்குப் பிறகான மக்கள் தொகை கணக்கெடுப்பு மாநில வாரியான இடங்களை மீண்டும் சீரமைக்கும்.",
        "Remembering", "High", ["84th Amendment", "Delimitation Freeze 2026", "Article 81 and 170"], "Part 2"
    )

    # Q032 - Correct: D
    add_q(
        "CZ_AM_HD_032",
        "Which Constitutional Amendment Act substituted '2001 Census' for '1991 Census' in Articles 81, 82, 170, and 330 for rationalising internal constituency boundaries without changing total seats allocated to states?",
        "மாநிலங்களுக்கு ஒதுக்கப்பட்ட மொத்த இடங்களை மாற்றாமல் உள்கட்டமைப்பு தொகுதி எல்லைகளை சீரமைக்க 1991 கணக்கெடுப்பிற்குப் பதிலாக '2001 மக்கள் தொகை கணக்கெடுப்பை' சரத்துகள் 81, 82, 170, 330 இல் சேர்த்த அரசியலமைப்பு திருத்தச் சட்டம் எது?",
        "84th Constitutional Amendment Act, 2001", "84வது அரசியலமைப்பு திருத்தச் சட்டம், 2001",
        "86th Constitutional Amendment Act, 2002", "86வது அரசியலமைப்பு திருத்தச் சட்டம், 2002",
        "91st Constitutional Amendment Act, 2003", "91வது அரசியலமைப்பு திருத்தச் சட்டம், 2003",
        "87th Constitutional Amendment Act, 2003", "87வது அரசியலமைப்பு திருத்தச் சட்டம், 2003",
        "D",
        "The 87th Constitutional Amendment Act, 2003 amended the 84th CA by substituting 2001 Census data for 1991 Census data for the purpose of internal delimitation of parliamentary and assembly constituencies.",
        "87வது அரசியலமைப்பு திருத்தச் சட்டம், 2003 84வது திருத்தத்தைத் திருத்தி, உள்கட்டமைப்பு தொகுதி மறுவரையறைக்கு 1991 கணக்கெடுப்பிற்குப் பதிலாக 2001 மக்கள் தொகை கணக்கெடுப்புத் தரவைச் சேர்த்தது.",
        "Option A is incorrect; 84th CA 2001 had originally specified 1991 Census.", "விருப்பம் A தவறானது; 84வது திருத்தம் ஆரம்பத்தில் 1991 கணக்கெடுப்பைக் குறிப்பிட்டிருந்தது.",
        "Option B is incorrect; 86th CA 2002 related to Right to Education.", "விருப்பம் B தவறானது; 86வது திருத்தம் கல்வி உரிமை பற்றியது.",
        "Option C is incorrect; 91st CA 2003 related to Council of Ministers size.", "விருப்பம் C தவறானது; 91வது திருத்தம் அமைச்சரவை அளவு பற்றியது.",
        "Option D is correct because 87th CA 2003 substituted 2001 Census figures for constituency delimitation.", "விருப்பம் D சரியானது, ஏனெனில் 87வது திருத்தம் 2003 2001 கணக்கெடுப்புத் தரவைச் சேர்த்தது.",
        "This enabled Delimitation Commission (under Justice Kuldip Singh) to redraw boundary lines of constituencies within each state.",
        "இது நீதிபதி குல்தீப் சிங் தலைமையிலான தொகுதி மறுவரையறை ஆணையத்திற்கு தொகுதி எல்லைகளை மாற்றி அமைக்க அதிகாரம் அளித்தது.",
        "The total number of seats in Lok Sabha for each State remained unchanged.",
        "ஒவ்வொரு மாநிலத்திற்கும் மக்களவையில் உள்ள மொத்த இடங்களின் எண்ணிக்கை மாற்றமின்றி அப்படியே இருந்தது.",
        "Remembering", "High", ["87th Amendment", "2001 Census Boundaries", "Delimitation Commission"], "Part 2"
    )

    # Q033 - Correct: A
    add_q(
        "CZ_AM_HD_033",
        "Which Constitutional Amendment Act substituted 'shall act in accordance with such advice' in Article 74(1), making it mandatory for the President to follow the advice of the Council of Ministers?",
        "சரத்து 74(1) இல் 'அத்தகைய ஆலோசனையின் படியே செயல்பட வேண்டும்' என மாற்றி, அமைச்சரவையின் ஆலோசனையைக் குடியரசுத் தலைவர் பின்பற்றுவதைக் கட்டாயமாக்கிய அரசியலமைப்பு திருத்தச் சட்டம் எது?",
        "42nd Constitutional Amendment Act, 1976", "42வது அரசியலமைப்பு திருத்தச் சட்டம், 1976",
        "44th Constitutional Amendment Act, 1978", "44வது அரசியலமைப்பு திருத்தச் சட்டம், 1978",
        "24th Constitutional Amendment Act, 1971", "24வது அரசியலமைப்பு திருத்தச் சட்டம், 1971",
        "25th Constitutional Amendment Act, 1971", "25வது அரசியலமைப்பு திருத்தச் சட்டம், 1971",
        "A",
        "The 42nd Constitutional Amendment Act, 1976 amended Article 74(1) establishing that the President shall act in accordance with advice tendered by the Council of Ministers.",
        "42வது அரசியலமைப்பு திருத்தச் சட்டம், 1976 சரத்து 74(1) ஐத் திருத்தி, அமைச்சரவை அளிக்கும் ஆலோசனையின் படியே குடியரசுத் தலைவர் செயல்பட வேண்டும் என மாற்றியது.",
        "Option A is correct because 42nd CA 1976 bound the President to Council of Ministers advice.", "விருப்பம் A சரியானது, ஏனெனில் 42வது திருத்தம் 1976 குடியரசு தலைவரை அமைச்சரவை ஆலோசனைக்குக் கட்டுப்படுத்தியது.",
        "Option B is incorrect; 44th CA 1978 added the proviso allowing President to request reconsideration ONCE.", "விருப்பம் B தவறானது; 44வது திருத்தம் ஆலோசனையை ஒரு முறை மறுபரிசீலனைக்கு அனுப்ப அனுமதித்தது.",
        "Option C is incorrect; 24th CA 1971 made assent mandatory for Art 368 bills.", "விருப்பம் C தவறானது; 24வது திருத்தம் சரத்து 368 ஒப்புதலைக் கட்டாயமாக்கியது.",
        "Option D is incorrect; 25th CA 1971 inserted Article 31C.", "விருப்பம் D தவறானது; 25வது திருத்தம் சரத்து 31C பற்றியது.",
        "44th CA 1978 modified this by adding a proviso: 'Provided that the President may require the Council of Ministers to reconsider such advice... but shall act in accordance with advice tendered after such reconsideration'.",
        "44வது திருத்தம் 1978 குடியரசு தலைவர் ஆலோசனையை ஒரு முறை மறுபரிசீலனைக்கு அனுப்பலாம் என்ற வரம்புரையைச் சேர்த்தது.",
        "This balanced constitutional oversight with cabinet supremacy.",
        "இது அமைச்சரவை மேலாதிக்கத்துடன் அரசியலமைப்பு மேற்பார்வையைச் சமப்படுத்தியது.",
        "Analysis", "High", ["42nd Amendment", "Article 74(1)", "Presidential Binding Advice"], "Part 2"
    )

    # Q034 - Correct: B
    add_q(
        "CZ_AM_HD_034",
        "Which Constitutional Amendment Act substituted '33%' reservation for women in Panchayats under Article 243D(3) and Municipalities under Article 243T(3)?",
        "சரத்து 243D(3) இன் கீழ் பஞ்சாயத்துகளிலும், சரத்து 243T(3) இன் கீழ் நகராட்சிகளிலும் பெண்களுக்கு 33% இடஒதுக்கீட்டை கட்டாயமாக்கிய அரசியலமைப்பு திருத்தச் சட்டங்கள் எவை?",
        "69th and 70th Amendment Acts, 1991-1992", "69வது மற்றும் 70வது திருத்தச் சட்டங்கள், 1991-1992",
        "73rd and 74th Amendment Acts, 1992", "73வது மற்றும் 74வது திருத்தச் சட்டங்கள், 1992",
        "86th and 91st Amendment Acts, 2002-2003", "86வது மற்றும் 91வது திருத்தச் சட்டங்கள், 2002-2003",
        "103rd and 104th Amendment Acts, 2019-2020", "103வது மற்றும் 104வது திருத்தச் சட்டங்கள், 2019-2020",
        "B",
        "The 73rd CA 1992 (Article 243D(3)) and 74th CA 1992 (Article 243T(3)) mandated that not less than 1/3rd (33%) of total seats in local bodies shall be reserved for women.",
        "73வது திருத்தம் 1992 (சரத்து 243D(3)) மற்றும் 74வது திருத்தம் 1992 (சரத்து 243T(3)) உள்ளாட்சி அமைப்புகளில் பெண்களுக்காகக் குறைந்தபட்சம் 1/3 பங்கு (33%) இடங்களை ஒதுக்க வேண்டும் எனக் கட்டாயமாக்கின.",
        "Option A is incorrect; 69th & 70th CAs relate to Delhi NCT and Presidential electoral college.", "விருப்பம் A தவறானது; 69 & 70 வது திருத்தங்கள் டெல்லி மற்றும் குடியரசு தலைவர் தேர்தல் பற்றியவை.",
        "Option B is correct because 73rd and 74th CAs 1992 enacted 33% women reservation in Panchayats and Municipalities.", "விருப்பம் B சரியானது, ஏனெனில் 73 மற்றும் 74 வது திருத்தங்கள் உள்ளாட்சிப் பெண் இடஒதுக்கீட்டை இயற்றின.",
        "Option C is incorrect; 86th & 91st CAs relate to RTE and cabinet size limit.", "விருப்பம் C தவறானது; 86 & 91 வது திருத்தங்கள் கல்வி உரிமை மற்றும் அமைச்சரவை அளவு பற்றியவை.",
        "Option D is incorrect; 103rd & 104th CAs relate to EWS and SC/ST reservation extension.", "விருப்பம் D தவறானது; 103 & 104 வது திருத்தங்கள் EWS மற்றும் எஸ்சி/எஸ்டி நீட்டிப்பு பற்றியவை.",
        "Several states (like Bihar, Tamil Nadu, MP, Kerala) have increased local body women's reservation to 50%.",
        "பீகார், தமிழ்நாடு, மத்திய பிரதேசம், கேரளா போன்ற பல மாநிலங்கள் உள்ளாட்சி அமைப்புகளில் பெண்களுக்கான இடஒதுக்கீட்டை 50% ஆக உயர்த்தியுள்ளன.",
        "This 1/3rd constitutional floor set by 73rd and 74th CAs provided the blueprint for the 106th CA 2023 for Parliament and Assemblies.",
        "73 மற்றும் 74 வது திருத்தங்கள் அமைத்த இந்த 33% அடித்தளமே 106வது திருத்தம் 2023 பாராளுமன்றப் பெண் இடஒதுக்கீட்டிற்கு மாதிரியாக அமைந்தது.",
        "Remembering", "High", ["73rd and 74th Amendments", "Women Local Body Reservation"], "Part 2"
    )

    # Q035 - Correct: C
    add_q(
        "CZ_AM_HD_035",
        "Which Constitutional Amendment Act substituted Article 368(4) claiming Parliament's amending power is subject to no limitation and Article 368(5) declaring no amendment shall be called in question in any court, which was later invalidated in Minerva Mills?",
        "நாடாளுமன்றத்தின் திருத்த அதிகாரம் எந்த வரம்பிற்கும் உட்பட்டது அல்ல என சரத்து 368(4) ஐயும், எந்தத் திருத்தத்தையும் எந்த நீதிமன்றத்திலும் கேள்வி கேட்க முடியாது என சரத்து 368(5) ஐயும் சேர்த்து, பின்னர் மினர்வா மில்ஸ் வழக்கில் ரத்து செய்யப்பட்ட அரசியலமைப்பு திருத்தச் சட்டம் எது?",
        "24th Constitutional Amendment Act, 1971", "24வது அரசியலமைப்பு திருத்தச் சட்டம், 1971",
        "25th Constitutional Amendment Act, 1971", "25வது அரசியலமைப்பு திருத்தச் சட்டம், 1971",
        "42nd Constitutional Amendment Act, 1976", "42வது அரசியலமைப்பு திருத்தச் சட்டம், 1976",
        "44th Constitutional Amendment Act, 1978", "44வது அரசியலமைப்பு திருத்தச் சட்டம், 1978",
        "C",
        "The 42nd Constitutional Amendment Act, 1976 inserted Clauses (4) and (5) to Article 368 in an attempt to completely oust judicial review of constitutional amendments. In Minerva Mills (1980), SC struck down both clauses as unconstitutional.",
        "42வது அரசியலமைப்பு திருத்தச் சட்டம், 1976 சரத்து 368 இல் உட்பிரிவுகள் (4) மற்றும் (5) ஐச் சேர்த்து நீதிமன்ற ஆய்வை முடக்க முயன்றது. மினர்வா மில்ஸ் (1980) வழக்கில் உச்ச நீதிமன்றம் இவ்விரு பிரிவுகளையும் ரத்து செய்தது.",
        "Option A is incorrect; 24th CA 1971 inserted Article 13(4) and Article 368(3).", "விருப்பம் A தவறானது; 24வது திருத்தம் சரத்து 13(4) மற்றும் 368(3) ஐச் சேர்த்தது.",
        "Option B is incorrect; 25th CA 1971 inserted Article 31C.", "விருப்பம் B தவறானது; 25வது திருத்தம் சரத்து 31C ஐச் சேர்த்தது.",
        "Option C is correct because 42nd CA 1976 inserted Article 368(4) and (5), which were struck down in Minerva Mills 1980.", "விருப்பம் C சரியானது, ஏனெனில் 42வது திருத்தம் 1976 சரத்து 368(4)&(5) ஐச் சேர்த்தது.",
        "Option D is incorrect; 44th CA 1978 did not insert Art 368(4)&(5).", "விருப்பம் D தவறானது; 44வது திருத்தம் இச்சரத்துகளைச் சேர்க்கவில்லை.",
        "Article 368(4) stated: 'No amendment of this Constitution... shall be called in question in any court on any ground'.",
        "சரத்து 368(4) எந்தவொரு நீதிமன்றத்திலும் அரசியலமைப்பு திருத்தத்தைக் கேள்வி கேட்கக் கூடாது எனக் கூறியது.",
        "Article 368(5) stated: 'For the removal of doubts, it is hereby declared that there shall be no limitation whatever on the constituent power of Parliament'.",
        "சரத்து 368(5) நாடாளுமன்றத்தின் திருத்தும் அதிகாரத்திற்கு எவ்வித வரம்பும் இல்லை என அறிவித்தது.",
        "Analysis", "High", ["42nd Amendment", "Article 368(4) and (5)", "Minerva Mills Invalidation"], "Part 3"
    )

    # Q036 - Correct: D
    add_q(
        "CZ_AM_HD_036",
        "Which Constitutional Amendment Act substituted '10 years' with '20 years' in Article 334, starting the 10-year periodic extension pattern for SC/ST reservations in Lok Sabha and State Legislative Assemblies?",
        "சரத்து 334 இல் '10 ஆண்டுகள்' என்பதற்குப் பதிலாக '20 ஆண்டுகள்' என மாற்றி, மக்களவை மற்றும் சட்டமன்றங்களில் எஸ்சி/எஸ்டி இடஒதுக்கீட்டுப் பத்து ஆண்டு காலமுறை நீட்டிப்பு வரிசையைத் தொடங்கி வைத்த அரசியலமைப்பு திருத்தச் சட்டம் எது?",
        "1st Constitutional Amendment Act, 1951", "1வது அரசியலமைப்பு திருத்தச் சட்டம், 1951",
        "7th Constitutional Amendment Act, 1956", "7வது அரசியலமைப்பு திருத்தச் சட்டம், 1956",
        "15th Constitutional Amendment Act, 1963", "15வது அரசியலமைப்பு திருத்தச் சட்டம், 1963",
        "8th Constitutional Amendment Act, 1959", "8வது அரசியலமைப்பு திருத்தச் சட்டம், 1959",
        "D",
        "The 8th Constitutional Amendment Act, 1959 was the FIRST amendment to extend SC/ST seat reservation under Article 334 from 10 years to 20 years (up to 1970).",
        "8வது அரசியலமைப்பு திருத்தச் சட்டம், 1959 சரத்து 334 இன் கீழ் எஸ்சி/எஸ்டி இடஒதுக்கீட்டை 10 லிருந்து 20 ஆண்டுகளாகக் (1970 வரை) நீட்டித்த முதல் திருத்தச் சட்டமாகும்.",
        "Option A is incorrect; 1st CA 1951 added 9th Schedule.", "விருப்பம் A தவறானது; 1வது திருத்தம் 9வது அட்டவணையைச் சேர்த்தது.",
        "Option B is incorrect; 7th CA 1956 reorganised states.", "விருப்பம் B தவறானது; 7வது திருத்தம் மாநிலங்கள் மறுசீரமைப்பு பற்றியது.",
        "Option C is incorrect; 15th CA 1963 raised HC judges retirement age.", "விருப்பம் C தவறானது; 15வது திருத்தம் உயர் நீதிமன்ற நீதிபதிகள் ஓய்வு வயது பற்றியது.",
        "Option D is correct because 8th CA 1959 started the 10-year extension cycle for Article 334.", "விருப்பம் D சரியானது, ஏனெனில் 8வது திருத்தம் 1959 சரத்து 334 நீட்டிப்பு வரிசையைத் தொடங்கியது.",
        "Article 334 extension history: 8th CA (1959) -> 23rd CA (1969) -> 45th CA (1980) -> 62nd CA (1989) -> 79th CA (1999) -> 95th CA (2009) -> 104th CA (2020).",
        "சரத்து 334 நீட்டிப்பு வரலாறு: 8வது (1959) -> 23வது (1969) -> 45வது (1980) -> 62வது (1989) -> 79வது (1999) -> 95வது (2009) -> 104வது (2020).",
        "This periodic extension pattern is a standard question in TNPSC Polity examinations.",
        "இந்தக் காலமுறை நீட்டிப்பு வரிசை டிஎன்பிஎஸ்சி தேர்வுகளில் கேட்கப்படும் ஒரு முக்கிய வினாவாகும்.",
        "Remembering", "High", ["8th Amendment", "Article 334 First Extension"], "Part 2"
    )

    # Q037 - Correct: A
    add_q(
        "CZ_AM_HD_037",
        "Which Constitutional Amendment Act created Article 239AA and Article 239AB establishing a 70-member Legislative Assembly for Delhi, and what was the maximum size of the Council of Ministers fixed by it under Article 239AA(4)?",
        "டெல்லிக்கு 70 உறுப்பினர்கள் கொண்ட சட்டமன்றத்தை நிறுவ சரத்துகள் 239AA மற்றும் 239AB ஐ உருவாக்கிய அரசியலமைப்பு திருத்தச் சட்டம் எது, மற்றும் சரத்து 239AA(4) இன் கீழ் அதன் அமைச்சரவை அளவு அதிகபட்சமாக எவ்வளவு நிர்ணயிக்கப்பட்டது?",
        "69th Amendment Act, 1991; 10% of Assembly strength (7 Ministers including CM)", "69வது திருத்தச் சட்டம், 1991; சட்டமன்ற எண்ணிக்கையில் 10% (முதல்வர் உட்பட 7 அமைச்சர்கள்)",
        "70th Amendment Act, 1992; 15% of Assembly strength (10 Ministers including CM)", "70வது திருத்தச் சட்டம், 1992; சட்டமன்ற எண்ணிக்கையில் 15% (முதல்வர் உட்பட 10 அமைச்சர்கள்)",
        "65th Amendment Act, 1990; 12 Ministers fixed floor limit", "65வது திருத்தச் சட்டம், 1990; 12 அமைச்சர்கள் வரம்பு",
        "91st Amendment Act, 2003; 15% of Assembly strength (11 Ministers including CM)", "91வது திருத்தச் சட்டம், 2003; சட்டமன்ற எண்ணிக்கையில் 15% (முதல்வர் உட்பட 11 அமைச்சர்கள்)",
        "A",
        "The 69th Constitutional Amendment Act, 1991 inserted Article 239AA(4) which specifically fixed Delhi's Council of Ministers at NOT MORE THAN 10% of the total number of members in the Assembly (7 ministers including CM).",
        "69வது அரசியலமைப்பு திருத்தச் சட்டம், 1991 சரத்து 239AA(4) ஐச் சேர்த்து டெல்லி அமைச்சரவையின் அளவை சட்டமன்ற எண்ணிக்கையில் 10% க்கு மிகாமல் (முதல்வர் உட்பட 7 அமைச்சர்கள்) என நிர்ணயித்தது.",
        "Option A is correct because 69th CA 1991 fixed Delhi's cabinet cap at 10% (unlike the general 15% cap for states under 91st CA).", "விருப்பம் A சரியானது, ஏனெனில் 69வது திருத்தம் 1991 டெல்லிக்கு 10% வரம்பை நிர்ணயித்தது.",
        "Option B is incorrect; 70th CA 1992 included Delhi MLAs in Presidential electoral college.", "விருப்பம் B தவறானது; 70வது திருத்தம் குடியரசு தலைவர் தேர்தல் மன்றம் பற்றியது.",
        "Option C is incorrect; 65th CA 1990 created NCSC & ST.", "விருப்பம் C தவறானது; 65வது திருத்தம் எஸ்சி/எஸ்டி ஆணையம் பற்றியது.",
        "Option D is incorrect; 91st CA 2003 applies 15% limit to other States, but Delhi remains governed by its special 10% limit under Art 239AA(4).", "விருப்பம் D தவறானது; 91வது திருத்தம் பிற மாநிலங்களுக்கு 15% வரம்பை அமைத்தது, டெல்லிக்கு 10% வரம்பே உள்ளது.",
        "TNPSC Group 1 Exception Trap: State Council of Ministers cap is 15% (under 91st CA 2003), BUT Delhi Council of Ministers cap is 10% (under 69th CA 1991).",
        "டிஎன்பிஎஸ்சி குரூப் 1 முக்கிய விதிவிலக்கு: பிற மாநிலங்களுக்கு அமைச்சரவை வரம்பு 15% (91வது திருத்தம்), ஆனால் டெல்லிக்கு அமைச்சரவை வரம்பு 10% (69வது திருத்தம்).",
        "Delhi Cabinet consists of the Chief Minister and 6 other Ministers.",
        "டெல்லி அமைச்சரவை முதலமைச்சர் மற்றும் 6 பிற அமைச்சர்களைக் கொண்டுள்ளது.",
        "Analysis", "High", ["69th Amendment", "Delhi Cabinet 10 Percent Exception", "Article 239AA"], "Part 2"
    )

    # Q038 - Correct: B
    add_q(
        "CZ_AM_HD_038",
        "Which Constitutional Amendment Act substituted '15%' as the ceiling limit for Council of Ministers in the Union and States, and what is the minimum number of Ministers prescribed for States under Article 164(1A)?",
        "மத்திய மற்றும் மாநிலங்களில் அமைச்சரவையின் அதிகபட்ச வரம்பை '15%' என நிர்ணயித்து, சரத்து 164(1A) இன் கீழ் மாநிலங்களுக்குக் குறைந்தபட்ச அமைச்சர்களின் எண்ணிக்கை எவ்வளவாக நிர்ணயித்த அரசியலமைப்பு திருத்தச் சட்டம் எது?",
        "84th CA 2001; Minimum 10 Ministers", "84வது திருத்தம் 2001; குறைந்தபட்சம் 10 அமைச்சர்கள்",
        "91st CA 2003; Minimum 12 Ministers", "91வது திருத்தச் சட்டம், 2003; குறைந்தபட்சம் 12 அமைச்சர்கள்",
        "86th CA 2002; Minimum 15 Ministers", "86வது திருத்தம் 2002; குறைந்தபட்சம் 15 அமைச்சர்கள்",
        "93rd CA 2005; Minimum 14 Ministers", "93வது திருத்தம் 2005; குறைந்தபட்சம் 14 அமைச்சர்கள்",
        "B",
        "The 91st Constitutional Amendment Act, 2003 inserted Article 164(1A) specifying that the total number of Ministers in a State shall not exceed 15% of Assembly strength, PROVIDED that the number of Ministers (including CM) shall NOT be less than 12.",
        "91வது அரசியலமைப்பு திருத்தச் சட்டம், 2003 சரத்து 164(1A) ஐச் சேர்த்து மாநில அமைச்சரவை அளவு 15% க்கு மிகக்கூடாது என்றும், அதே வேளையில் முதலமைச்சர் உட்பட குறைந்தபட்சம் 12 அமைச்சர்களுக்குக் குறையக்கூடாது என்றும் நிர்ணயித்தது.",
        "Option A is incorrect; 84th CA 2001 froze seat delimitation till 2026.", "விருப்பம் A தவறானது; 84வது திருத்தம் தொகுதி முடக்கம் பற்றியது.",
        "Option B is correct because 91st CA 2003 fixed 15% maximum ceiling and 12 ministers minimum floor for States under Article 164(1A).", "விருப்பம் B சரியானது, ஏனெனில் 91வது திருத்தம் 2003 15% அதிகபட்சம் மற்றும் 12 குறைந்தபட்சம் வரம்பை நிர்ணயித்தது.",
        "Option C is incorrect; 86th CA 2002 related to RTE.", "விருப்பம் C தவறானது; 86வது திருத்தம் கல்வி உரிமை பற்றியது.",
        "Option D is incorrect; 93rd CA 2005 related to OBC quota in colleges.", "விருப்பம் D தவறானது; 93வது திருத்தம் OBC இடஒதுக்கீடு பற்றியது.",
        "The 15% limit applies to Lok Sabha for the Union (Art 75(1A)), but there is NO minimum floor prescribed for the Union Cabinet under Article 75(1A).",
        "மத்திய அரசிற்கு மக்களவையில் 15% அதிகபட்ச வரம்பு உண்டு (சரத்து 75(1A)), ஆனால் குறைந்தபட்ச எண்ணிக்கை வரம்பு மத்திய அரசிற்கு நிர்ணயிக்கப்படவில்லை.",
        "Minimum 12 ministers rule applies ONLY to State Councils of Ministers under Article 164(1A).",
        "குறைந்தபட்சம் 12 அமைச்சர்கள் என்ற விதி மாநில அமைச்சரவைகளுக்கு மட்டுமே பொருந்தும்.",
        "Analysis", "High", ["91st Amendment", "Article 164(1A)", "Minimum 12 Ministers Floor"], "Part 2"
    )

    # Q039 - Correct: C
    add_q(
        "CZ_AM_HD_039",
        "Which Constitutional Amendment Act added Part IX-A (Municipalities) to the Constitution of India, and how many functional matters are contained in the 12th Schedule inserted by it?",
        "இந்திய அரசியலமைப்பில் பகுதி IX-A (நகராட்சிகள்) ஐச் சேர்த்த அரசியலமைப்பு திருத்தச் சட்டம் எது, மற்றும் அதனால் சேர்க்கப்பட்ட 12வது அட்டவணையில் எத்தனை செயல்பாட்டுப் பொருட்கள் உள்ளன?",
        "73rd CA 1992; 29 functional matters", "73வது திருத்தம் 1992; 29 செயல்பாட்டுப் பொருட்கள்",
        "71st CA 1992; 22 functional matters", "71வது திருத்தம் 1992; 22 செயல்பாட்டுப் பொருட்கள்",
        "74th CA 1992; 18 functional matters", "74வது அரசியலமைப்பு திருத்தச் சட்டம், 1992; 18 செயல்பாட்டுப் பொருட்கள்",
        "69th CA 1991; 12 functional matters", "69வது திருத்தம் 1991; 12 செயல்பாட்டுப் பொருட்கள்",
        "C",
        "The 74th Constitutional Amendment Act, 1992 inserted Part IX-A (Articles 243P to 243ZG) and the 12th Schedule containing 18 functional items for Municipalities.",
        "74வது அரசியலமைப்பு திருத்தச் சட்டம், 1992 பகுதி IX-A மற்றும் நகராட்சிகளுக்கான 18 செயல்பாட்டைக் கொண்ட 12வது அட்டவணையைச் சேர்த்தது.",
        "Option A is incorrect; 73rd CA 1992 added Part IX and 11th Schedule (29 functional matters for Panchayats).", "விருப்பம் A தவறானது; 73வது திருத்தம் பஞ்சாயத்துகளுக்கான 29 செயல்பாடுகளைக் கொண்டது.",
        "Option B is incorrect; 71st CA 1992 added languages to 8th Schedule.", "விருப்பம் B தவறானது; 71வது திருத்தம் மொழிகளைச் சேர்த்தது.",
        "Option C is correct because 74th CA 1992 introduced Part IX-A and 12th Schedule with 18 functional items.", "விருப்பம் C சரியானது, ஏனெனில் 74வது திருத்தம் 1992 பகுதி IX-A மற்றும் 18 செயல்பாடுகளைக் கொண்ட 12வது அட்டவணையைச் சேர்த்தது.",
        "Option D is incorrect; 69th CA 1991 related to Delhi NCT.", "விருப்பம் D தவறானது; 69வது திருத்தம் டெல்லி பற்றியது.",
        "TNPSC Comparison Fact: 11th Schedule (73rd CA Panchayats) = 29 items; 12th Schedule (74th CA Municipalities) = 18 items.",
        "டிஎன்பிஎஸ்சி ஒப்பீட்டு உண்மை: 11வது அட்டவணை (73வது திருத்தம் பஞ்சாயத்துகள்) = 29 பொருட்கள்; 12வது அட்டவணை (74வது திருத்தம் நகராட்சிகள்) = 18 பொருட்கள்.",
        "74th CA provides for 3 types of Municipalities: Nagar Panchayat, Municipal Council, and Municipal Corporation.",
        "74வது திருத்தம் 3 வகையான நகராட்சிகளை அளிக்கிறது: நகர பஞ்சாயத்து, நகராட்சி மன்றம், மாநகராட்சி.",
        "Remembering", "High", ["74th Amendment", "12th Schedule 18 Items", "Part IX-A"], "Part 2"
    )

    # Q040 - Correct: D
    add_q(
        "CZ_AM_HD_040",
        "Which Constitutional Amendment Act substituted 'Socialist, Secular, Integrity' into the Preamble, inserted Fundamental Duties, added Part XIV-A Tribunals, and extended Assembly terms to 6 years?",
        "முகப்புரையில் 'சமதர்ம, மதச்சார்பற்ற, ஒருமைப்பாடு' என்ற சொற்களைச் சேர்த்து, அடிப்படை கடமைகளை அறிமுகப்படுத்தி, பகுதி XIV-A தீர்ப்பாயங்களை உருவாக்கி, சட்டமன்ற பதவிக் காலத்தை 6 ஆண்டுகளாக உயர்த்திய அரசியலமைப்பு திருத்தச் சட்டம் எது?",
        "24th Constitutional Amendment Act, 1971", "24வது அரசியலமைப்பு திருத்தச் சட்டம், 1971",
        "25th Constitutional Amendment Act, 1971", "25வது அரசியலமைப்பு திருத்தச் சட்டம், 1971",
        "44th Constitutional Amendment Act, 1978", "44வது அரசியலமைப்பு திருத்தச் சட்டம், 1978",
        "42nd Constitutional Amendment Act, 1976", "42வது அரசியலமைப்பு திருத்தச் சட்டம், 1976",
        "D",
        "The 42nd Constitutional Amendment Act, 1976 enacted all these major additions simultaneously across Preamble, Fundamental Duties, Tribunals, and Directive Principles.",
        "42வது அரசியலமைப்பு திருத்தச் சட்டம், 1976 முகப்புரை, அடிப்படை கடமைகள், தீர்ப்பாயங்கள் மற்றும் அரசு நெறிமுறைக் கோட்பாடுகள் ஆகியவற்றில் இம்மாபெரும் சேர்க்கைகளை ஒரே நேரத்தில் இயற்றியது.",
        "Option A is incorrect; 24th CA 1971 amended Article 368 and 13.", "விருப்பம் A தவறானது; 24வது திருத்தம் சரத்து 368 மற்றும் 13 பற்றியது.",
        "Option B is incorrect; 25th CA 1971 inserted Article 31C.", "விருப்பம் B தவறானது; 25வது திருத்தம் சரத்து 31C பற்றியது.",
        "Option C is incorrect; 44th CA 1978 restored democratic checks.", "விருப்பம் C தவறானது; 44வது திருத்தம் அவசரநிலை சீரமைப்பு பற்றியது.",
        "Option D is correct because 42nd CA 1976 added Preamble words, Part IV-A, Part XIV-A, and Articles 39A, 43A, 48A.", "விருப்பம் D சரியானது, ஏனெனில் 42வது திருத்தம் 1976 இனைத்து முக்கிய அம்சங்களையும் சேர்த்தது.",
        "42nd CA 1976 is the most comprehensive amendment ever passed by Parliament of India, altering over 53 Articles of the Constitution.",
        "42வது திருத்தம் 1976 இந்திய நாடாளுமன்றத்தால் நிறைவேற்றப்பட்ட மிக விரிவான திருத்தமாகும்; இது அரசியலமைப்பின் 53 க்கும் மேற்பட்ட சரத்துகளைத் திருத்தியது.",
        "It was drafted under the chairmanship of Swaran Singh.",
        "இது ஸ்வரண் சிங் தலைமையின் கீழ் வரைவு செய்யப்பட்டது.",
        "Remembering", "High", ["42nd Amendment Comprehensive", "Mini Constitution Items"], "Part 2"
    )

    # Q041 - Correct: A
    add_q(
        "CZ_AM_HD_041",
        "Which Constitutional Amendment Act inserted Article 371D and Article 371E providing special provisions for the State of Andhra Pradesh, including the establishment of a Central University?",
        "ஆந்திரப் பிரதேச மாநிலத்திற்கு சிறப்பு விதிகளையும், மத்தியப் பல்கலைக்கழகம் அமைக்க வழிவகையையும் வழங்கும் சரத்துகள் 371D மற்றும் 371E ஆகியவற்றை அறிமுகப்படுத்திய அரசியலமைப்பு திருத்தச் சட்டம் எது?",
        "32nd Constitutional Amendment Act, 1973", "32வது அரசியலமைப்பு திருத்தச் சட்டம், 1973",
        "31st Constitutional Amendment Act, 1973", "31வது அரசியலமைப்பு திருத்தச் சட்டம், 1973",
        "35th Constitutional Amendment Act, 1974", "35வது அரசியலமைப்பு திருத்தச் சட்டம், 1974",
        "36th Constitutional Amendment Act, 1975", "36வது அரசியலமைப்பு திருத்தச் சட்டம், 1975",
        "A",
        "The 32nd Constitutional Amendment Act, 1973 inserted Articles 371D and 371E to satisfy the regional aspirations of Telangana and Andhra regions following the Six-Point Formula.",
        "32வது அரசியலமைப்பு திருத்தச் சட்டம், 1973 ஆறு அம்சத் திட்டத்தின் படி தெலுங்கானா மற்றும் ஆந்திரப் பகுதிகளின் பிராந்திய விருப்பங்களைப் பூர்த்தி செய்ய சரத்துகள் 371D மற்றும் 371E ஐச் சேர்த்தது.",
        "Option A is correct because 32nd CA 1973 created Articles 371D and 371E for Andhra Pradesh.", "விருப்பம் A சரியானது, ஏனெனில் 32வது திருத்தம் 1973 ஆந்திராவிற்காக சரத்துகள் 371D மற்றும் 371E ஐ உருவாக்கியது.",
        "Option B is incorrect; 31st CA 1973 increased Lok Sabha seats to 545.", "விருப்பம் B தவறானது; 31வது திருத்தம் மக்களவை இடங்களை 545 ஆக உயர்த்தியது.",
        "Option C is incorrect; 35th CA 1974 made Sikkim an Associate State.", "விருப்பம் C தவறானது; 35வது திருத்தம் சிக்கிம் இணை மாநிலம் பற்றியது.",
        "Option D is incorrect; 36th CA 1975 made Sikkim a full state.", "விருப்பம் D தவறானது; 36வது திருத்தம் சிக்கிம் முழு மாநிலம் பற்றியது.",
        "Article 371D deals with equitable opportunities and facilities for people of different parts of Andhra Pradesh in public employment and education.",
        "சரத்து 371D அரசு வேலைவாய்ப்பு மற்றும் கல்வியில் ஆந்திராவின் பல்வேறு பகுதிகளுக்குச் சமமான வாய்ப்புகளை அளிக்கிறது.",
        "Article 371E empowers Parliament to establish a Central University in Andhra Pradesh.",
        "சரத்து 371E ஆந்திராவில் மத்திய பல்கலைக்கழகத்தை நிறுவ நாடாளுமன்றத்திற்கு அதிகாரம் அளிக்கிறது.",
        "Remembering", "High", ["32nd Amendment", "Article 371D 371E", "Andhra Pradesh"], "Part 2"
    )

    # Q042 - Correct: B
    add_q(
        "CZ_AM_HD_042",
        "Which Constitutional Amendment Act exempted the State of Bihar from the requirement of having a Tribal Welfare Minister under Article 164(1) while extending it to Chhattisgarh and Jharkhand?",
        "சரத்து 164(1) இன் கீழ் பழங்குடியினர் நல அமைச்சரைக் கட்டாயமாக நியமிப்பதிலிருந்து பீகார் மாநிலத்திற்கு விலக்களித்து, சத்தீஸ்கர் மற்றும் ஜார்கண்டிற்கு அதை விரிவாக்கிய அரசியலமைப்பு திருத்தச் சட்டம் எது?",
        "89th Constitutional Amendment Act, 2003", "89வது அரசியலமைப்பு திருத்தச் சட்டம், 2003",
        "94th Constitutional Amendment Act, 2006", "94வது அரசியலமைப்பு திருத்தச் சட்டம், 2006",
        "91st Constitutional Amendment Act, 2003", "91வது அரசியலமைப்பு திருத்தச் சட்டம், 2003",
        "83rd Constitutional Amendment Act, 2000", "83வது அரசியலமைப்பு திருத்தச் சட்டம், 2000",
        "B",
        "The 94th Constitutional Amendment Act, 2006 amended Article 164(1) proviso, freeing Bihar from the requirement of having a Tribal Welfare Minister (since Jharkhand was carved out of Bihar in 2000) and extending the requirement to Chhattisgarh, Jharkhand, MP, and Odisha.",
        "94வது அரசியலமைப்பு திருத்தச் சட்டம், 2006 சரத்து 164(1) இன் வரம்புரையைத் திருத்தி, பீகாரை பழங்குடியினர் நல அமைச்சர் நியமனக் கட்டாயத்திலிருந்து விலக்கி, அதை சத்தீஸ்கர், ஜார்கண்ட், மத்திய பிரதேசம், ஒடிசா ஆகிய மாநிலங்களுக்கு விரிவாக்கியது.",
        "Option A is incorrect; 89th CA 2003 bifurcated NCSC and NCST.", "விருப்பம் A தவறானது; 89வது திருத்தம் எஸ்சி/எஸ்டி ஆணையங்களைப் பிரித்தது.",
        "Option B is correct because 94th CA 2006 exempted Bihar and included Chhattisgarh and Jharkhand under Art 164(1).", "விருப்பம் B சரியானது, ஏனெனில் 94வது திருத்தம் 2006 பீகாருக்கு விலக்களித்து சத்தீஸ்கர், ஜார்கண்டைச் சேர்த்தது.",
        "Option C is incorrect; 91st CA 2003 capped cabinet size at 15%.", "விருப்பம் C தவறானது; 91வது திருத்தம் 15% அமைச்சரவை வரம்பு பற்றியது.",
        "Option D is incorrect; 83rd CA 2000 exempted Arunachal Pradesh Panchayats from SC reservation.", "விருப்பம் D தவறானது; 83வது திருத்தம் அருணாச்சலப் பிரதேச SC விலக்கு பற்றியது.",
        "Original Article 164(1) mandated Tribal Welfare Ministers in Bihar, MP, and Odisha.",
        "மூல சரத்து 164(1) பீகார், மத்திய பிரதேசம் மற்றும் ஒரிசாவில் பழங்குடியினர் நல அமைச்சரைக் கட்டாயமாக்கியிருந்தது.",
        "With Jharkhand created out of Bihar in 2000, 94th CA substituted Jharkhand and Chhattisgarh for Bihar.",
        "2000 இல் பீகாரிலிருந்து ஜார்கண்ட் பிரிக்கப்பட்டதால் 94வது திருத்தம் இம்மாற்றத்தைச் செய்தது.",
        "Remembering", "High", ["94th Amendment", "Article 164(1) Tribal Minister Exemption"], "Part 2"
    )

    # Q043 - Correct: C
    add_q(
        "CZ_AM_HD_043",
        "In Kihoto Hollohan v. Zachillhu (1992), which Paragraph of the 10th Schedule (Anti-Defection Law inserted by 52nd CA 1985) was declared constitutionally invalid for lack of ratification by State Legislatures?",
        "கிஹோட்டோ ஹோலோஹன் (1992) வழக்கில் 10வது அட்டவணையின் (52வது திருத்தத்தால் சேர்க்கப்பட்ட கட்சித் தாவல் சட்டம்) எந்தப் பத்தி மாநில சட்டமன்றங்களின் ஒப்புதல் பெறாததால் அரசியலமைப்புப்படி செல்லாது என அறிவிக்கப்பட்டது?",
        "Paragraph 2 of 10th Schedule", "10வது அட்டவணையின் பத்தி 2",
        "Paragraph 5 of 10th Schedule", "10வது அட்டவணையின் பத்தி 5",
        "Paragraph 7 of 10th Schedule", "10வது அட்டவணையின் பத்தி 7",
        "Paragraph 4 of 10th Schedule", "10வது அட்டவணையின் பத்தி 4",
        "C",
        "In Kihoto Hollohan (1992), Supreme Court declared Paragraph 7 of the 10th Schedule unconstitutional because it barred judicial review and affected High Court powers without receiving state ratification under Article 368(2) proviso.",
        "கிஹோட்டோ ஹோலோஹன் (1992) வழக்கில் உச்ச நீதிமன்றம் 10வது அட்டவணையின் 7வது பத்தியை, அது உயர் நீதிமன்ற அதிகாரங்களைப் பாதிக்கும் நிலையிலும் மாநில ஒப்புதல் பெறாததால் செல்லாது என அறிவித்தது.",
        "Option A is incorrect; Paragraph 2 lays down disqualification grounds on defection.", "விருப்பம் A தவறானது; பத்தி 2 கட்சித் தாவல் தகுதிநீக்கக் காரணங்களைக் கூறுகிறது.",
        "Option B is incorrect; Paragraph 5 gives exemption to Presiding Officers.", "விருப்பம் B தவறானது; பத்தி 5 அவைத் தலைவர்களுக்கு விலக்களிக்கிறது.",
        "Option C is correct because Paragraph 7 of 10th Schedule was struck down in Kihoto Hollohan for violating Article 368(2) proviso requirement.", "விருப்பம் C சரியானது, ஏனெனில் 7வது பத்தி மாநில ஒப்புதல் பெறாததால் ரத்து செய்யப்பட்டது.",
        "Option D is incorrect; Paragraph 4 deals with mergers.", "விருப்பம் D தவறானது; பத்தி 4 கட்சி இணைப்பைக் கையாள்கிறது.",
        "The remaining paragraphs of the 10th Schedule were held severable and constitutional by the Supreme Court.",
        "10வது அட்டவணையின் எஞ்சிய பத்திகள் பிரிக்கக்கூடியவை என்றும் அரசியலமைப்புப்படி செல்லும் என்றும் தீர்ப்பளிக்கப்பட்டது.",
        "This judgment established that Presiding Officer's decision under 10th Schedule is subject to Judicial Review.",
        "10வது அட்டவணையின் கீழ் சபாநாயகர் எடுக்கும் முடிவு நீதிமன்ற ஆய்விற்கு உட்பட்டது என்பதை இத்தீர்ப்பு நிறுவியது.",
        "Analysis", "High", ["Kihoto Hollohan Case", "10th Schedule Paragraph 7", "Judicial Review Speaker"], "Part 3"
    )

    # Q044 - Correct: D
    add_q(
        "CZ_AM_HD_044",
        "Which Constitutional Amendment Act inserted Article 243H empowering Panchayats to levy, collect, and appropriate taxes, and Article 243X empowering Municipalities to do the same?",
        "பஞ்சாயத்துகள் (சரத்து 243H) மற்றும் நகராட்சிகள் (சரத்து 243X) வரிகள், கட்டணங்களை விதிக்கவும் வசூலிக்கவும் அதிகாரமளிக்கும் சரத்துகளை முறையே அறிமுகப்படுத்திய அரசியலமைப்பு திருத்தச் சட்டங்கள் எவை?",
        "69th and 70th Amendment Acts, 1991-1992", "69வது மற்றும் 70வது திருத்தச் சட்டங்கள், 1991-1992",
        "71st and 72nd Amendment Acts, 1992", "71வது மற்றும் 72வது திருத்தச் சட்டங்கள், 1992",
        "86th and 91st Amendment Acts, 2002-2003", "86வது மற்றும் 91வது திருத்தச் சட்டங்கள், 2002-2003",
        "73rd and 74th Amendment Acts, 1992", "73வது மற்றும் 74வது அரசியலமைப்பு திருத்தச் சட்டங்கள், 1992",
        "D",
        "The 73rd CA 1992 inserted Article 243H (Power to impose taxes by Panchayats) and 74th CA 1992 inserted Article 243X (Power to impose taxes by Municipalities).",
        "73வது திருத்தம் 1992 சரத்து 243H (பஞ்சாயத்துகள் வரி விதிக்கும் அதிகாரம்) மற்றும் 74வது திருத்தம் 1992 சரத்து 243X (நகராட்சிகள் வரி விதிக்கும் அதிகாரம்) ஆகியவற்றைச் சேர்த்தன.",
        "Option A is incorrect; 69th & 70th CAs relate to Delhi NCT and Presidential electoral college.", "விருப்பம் A தவறானது; 69 & 70 வது திருத்தங்கள் டெல்லி மற்றும் குடியரசு தலைவர் தேர்தல் பற்றியவை.",
        "Option B is incorrect; 71st CA added languages.", "விருப்பம் B தவறானது; 71வது திருத்தம் மொழிகளைச் சேர்த்தது.",
        "Option C is incorrect; 86th & 91st CAs relate to RTE and cabinet size.", "விருப்பம் C தவறானது; 86 & 91 வது திருத்தங்கள் கல்வி உரிமை பற்றியவை.",
        "Option D is correct because 73rd and 74th CAs 1992 provided financial taxation powers under Articles 243H and 243X.", "விருப்பம் D சரியானது, ஏனெனில் 73 மற்றும் 74 வது திருத்தங்கள் சரத்துகள் 243H மற்றும் 243X இன் கீழ் நிதி அதிகாரங்களை அளித்தன.",
        "Financial autonomy of local self-governments depends on effective implementation of Articles 243H and 243X by State Legislatures.",
        "உள்ளாட்சி அமைப்புகளின் நிதித் தன்னாட்சி இச்சரத்துகளை மாநில சட்டமன்றங்கள் முறையாக அமல்படுத்துவதைப் பொறுத்தது.",
        "State Finance Commissions recommend tax sharing under Articles 243I and 243Y.",
        "மாநில நிதி ஆணையங்கள் சரத்துகள் 243I மற்றும் 243Y இன் கீழ் வரிப் பகிர்வைப் பரிந்துரைக்கின்றன.",
        "Remembering", "High", ["73rd and 74th Amendments", "Articles 243H and 243X", "Local Body Taxation"], "Part 2"
    )

    # Q045 - Correct: A
    add_q(
        "CZ_AM_HD_045",
        "Which Constitutional Amendment Act amended the First Schedule to give effect to the transfer of Berubari Union No. 12 to Pakistan following the 1960 Supreme Court Advisory Opinion?",
        "1960 உச்ச நீதிமன்ற ஆலோசனைத் தீர்ப்பைத் தொடர்ந்து பெருபாரி யூனியன் எண் 12 ஐ பாகிஸ்தானிற்கு வழங்க முதலாம் அட்டவணையைத் திருத்திய அரசியலமைப்பு திருத்தச் சட்டம் எது?",
        "9th Constitutional Amendment Act, 1960", "9வது அரசியலமைப்பு திருத்தச் சட்டம், 1960",
        "1st Constitutional Amendment Act, 1951", "1வது அரசியலமைப்பு திருத்தச் சட்டம், 1951",
        "5th Constitutional Amendment Act, 1955", "5வது அரசியலமைப்பு திருத்தச் சட்டம், 1955",
        "100th Constitutional Amendment Act, 2015", "100வது அரசியலமைப்பு திருத்தச் சட்டம், 2015",
        "A",
        "Following the Supreme Court ruling in In re Berubari Union (1960) that ceding territory requires Article 368 amendment, Parliament passed the 9th Constitutional Amendment Act, 1960.",
        "பெருபாரி வழக்கில் (1960) இந்திய நிலப்பரப்பை அயல்நாட்டிற்கு வழங்குவதற்கு சரத்து 368 திருத்தம் கட்டாயம் தேவை என உச்ச நீதிமன்றம் கூறியதைத் தொடர்ந்து நாடாளுமன்றம் 9வது அரசியலமைப்பு திருத்தச் சட்டம் 1960 ஐ இயற்றியது.",
        "Option A is correct because 9th CA 1960 implemented the Berubari Union transfer to Pakistan under Indo-Pakistan Agreement 1958.", "விருப்பம் A சரியானது, ஏனெனில் 9வது திருத்தம் 1960 பெருபாரி யூனியன் நிலப்பரிமாற்றத்தைச் செயல்படுத்தியது.",
        "Option B is incorrect; 1st CA 1951 added 9th Schedule.", "விருப்பம் B தவறானது; 1வது திருத்தம் 9வது அட்டவணையைச் சேர்த்தது.",
        "Option C is incorrect; 5th CA 1955 related to state consultation time limit.", "விருப்பம் C தவறானது; 5வது திருத்தம் கருத்து கேட்பு காலக்கெடு பற்றியது.",
        "Option D is incorrect; 100th CA 2015 implemented Land Boundary Agreement with Bangladesh.", "விருப்ப点 D தவறானது; 100வது திருத்தம் வங்காளதேச எல்லை ஒப்பந்தம் பற்றியது.",
        "Supreme Court in Berubari Case (1960) held that power of Parliament to diminish state territory under Article 3 does NOT include power to cede Indian territory to a foreign country.",
        "சரத்து 3 இன் கீழ் மாநில எல்லையைக் குறைக்கும் நாடாளுமன்ற அதிகாரம் இந்திய நிலப்பரப்பை அயல்நாட்டிற்கு வழங்கும் அதிகாரத்தை உள்ளடக்காது என பெருபாரி வழக்கில் தீர்ப்பளிக்கப்பட்டது.",
        "Cession of territory can ONLY be done by amending the Constitution under Article 368.",
        "நிலப்பரப்பை அயல்நாட்டிற்கு வழங்குவது சரத்து 368 இன் கீழான அரசியலமைப்பு திருத்தம் மூலம் மட்டுமே சாத்தியமாகும்.",
        "Analysis", "High", ["9th Amendment", "Berubari Union Case", "Territory Cession"], "Part 2"
    )

    # Q046 - Correct: B
    add_q(
        "CZ_AM_HD_046",
        "Which Constitutional Amendment Act conferred full statehood on Arunachal Pradesh and inserted Article 371H conferring special responsibility on the Governor of Arunachal Pradesh with respect to law and order?",
        "அருணாச்சலப் பிரதேசத்திற்கு முழு மாநில அந்தஸ்து வழங்கி, சட்டம் ஒழுங்கு பராமரிப்பில் அருணாச்சலப் பிரதேச ஆளுநருக்கு சிறப்புப் பொறுப்பை அளிக்கும் சரத்து 371H ஐச் சேர்த்த அரசியலமைப்பு திருத்தச் சட்டம் எது?",
        "53rd Constitutional Amendment Act, 1986", "53வது அரசியலமைப்பு திருத்தச் சட்டம், 1986",
        "55th Constitutional Amendment Act, 1986", "55வது அரசியலமைப்பு திருத்தச் சட்டம், 1986",
        "56th Constitutional Amendment Act, 1987", "56வது அரசியலமைப்பு திருத்தச் சட்டம், 1987",
        "36th Constitutional Amendment Act, 1975", "36வது அரசியலமைப்பு திருத்தச் சட்டம், 1975",
        "B",
        "The 55th Constitutional Amendment Act, 1986 conferred statehood on Arunachal Pradesh (24th State) and inserted Article 371H conferring special responsibility on the Governor with respect to law and order.",
        "55வது அரசியலமைப்பு திருத்தச் சட்டம், 1986 அருணாச்சலப் பிரதேசத்திற்கு முழு மாநில அந்தஸ்து (24வது மாநிலம்) வழங்கி, ஆளுநருக்கு சட்டம் ஒழுங்கில் சிறப்புப் பொறுப்பளிக்கும் சரத்து 371H ஐச் சேர்த்தது.",
        "Option A is incorrect; 53rd CA 1986 conferred statehood on Mizoram (Article 371G).", "விருப்பம் A தவறானது; 53வது திருத்தம் மிசோரமிற்கு மாநில அந்தஸ்து வழங்கியது.",
        "Option B is correct because 55th CA 1986 created Article 371H for Arunachal Pradesh.", "விருப்பம் B சரியானது, ஏனெனில் 55வது திருத்தம் 1986 அருணாச்சலப் பிரதேசத்திற்காக சரத்து 371H ஐ உருவாக்கியது.",
        "Option C is incorrect; 56th CA 1987 conferred statehood on Goa (Article 371I).", "விருப்பம் C தவறானது; 56வது திருத்தம் கோவாவிற்கு மாநில அந்தஸ்து வழங்கியது.",
        "Option D is incorrect; 36th CA 1975 conferred statehood on Sikkim (Article 371F).", "விருப்பம் D தவறானது; 36வது திருத்தம் சிக்கிம் மாநில அந்தஸ்து பற்றியது.",
        "53rd CA 1986 = Mizoram (Art 371G, 23rd State); 55th CA 1986 = Arunachal Pradesh (Art 371H, 24th State); 56th CA 1987 = Goa (Art 371I, 25th State).",
        "53வது திருத்தம் = மிசோரம் (23வது மாநிலம்); 55வது திருத்தம் = அருணாச்சலப் பிரதேசம் (24வது மாநிலம்); 56வது திருத்தம் = கோவா (25வது மாநிலம்).",
        "This 1986-87 North-East statehood amendment triplet is frequently asked in TNPSC exams.",
        "1986-87 வடகிழக்கு மாநில உருவாக்கத் திருத்தங்கள் டிஎன்பிஎஸ்சி தேர்வுகளில் அடிக்கடி கேட்கப்படுபவை.",
        "Remembering", "High", ["55th Amendment", "Arunachal Pradesh Statehood", "Article 371H"], "Part 2"
    )

    # Q047 - Correct: C
    add_q(
        "CZ_AM_HD_047",
        "Which Constitutional Amendment Act created Article 243I and Article 243K providing for the State Finance Commission and State Election Commission for Panchayats?",
        "பஞ்சாயத்துகளுக்கான மாநில நிதி ஆணையம் (சரத்து 243I) மற்றும் மாநிலத் தேர்தல் ஆணையம் (சரத்து 243K) ஆகியவற்றை உருவாக்கிய அரசியலமைப்பு திருத்தச் சட்டம் எது?",
        "65th Amendment Act, 1990", "65வது திருத்தச் சட்டம், 1990",
        "70th Amendment Act, 1992", "70வது திருத்தச் சட்டம், 1992",
        "73rd Amendment Act, 1992", "73வது அரசியலமைப்பு திருத்தச் சட்டம், 1992",
        "74th Amendment Act, 1992", "74வது திருத்தச் சட்டம், 1992",
        "C",
        "The 73rd Constitutional Amendment Act, 1992 inserted Article 243I (State Finance Commission) and Article 243K (State Election Commission) to ensure financial devolution and free/fair local elections.",
        "73வது அரசியலமைப்பு திருத்தச் சட்டம், 1992 சரத்து 243I (மாநில நிதி ஆணையம்) மற்றும் சரத்து 243K (மாநிலத் தேர்தல் ஆணையம்) ஆகியவற்றைச் சேர்த்தது.",
        "Option A is incorrect; 65th CA related to NCSC & ST.", "விருப்பம் A தவறானது; 65வது திருத்தம் எஸ்சி/எஸ்டி ஆணையம் பற்றியது.",
        "Option B is incorrect; 70th CA related to Delhi & Puducherry Presidential voting.", "விருப்பம் B தவறானது; 70வது திருத்தம் குடியரசு தலைவர் தேர்தல் மன்றம் பற்றியது.",
        "Option C is correct because 73rd CA 1992 inserted Articles 243I and 243K into Part IX.", "விருப்பம் C சரியானது, ஏனெனில் 73வது திருத்தம் 1992 சரத்துகள் 243I மற்றும் 243K ஐச் சேர்த்தது.",
        "Option D is incorrect; 74th CA applied similar provisions for Municipalities under Art 243Y & 243ZA.", "விருப்பம் D தவறானது; 74வது திருத்தம் நகராட்சிகளுக்கான 243Y & 243ZA விதியைக் கொண்டது.",
        "State Election Commissioner is appointed by the Governor of the State under Article 243K(1).",
        "மாநிலத் தேர்தல் ஆணையர் மாநில ஆளுநரால் நியமிக்கப்படுகிறார் (சரத்து 243K(1)).",
        "State Election Commissioner can be removed from office only in like manner and on like grounds as a Judge of a High Court (Art 243K(2)).",
        "மாநிலத் தேர்தல் ஆணையரை உயர் நீதிமன்ற நீதிபதியை நீக்கும் அதே நடைமுறை மற்றும் காரணங்களின் அடிப்படையில் மட்டுமே நீக்க முடியும்.",
        "Remembering", "High", ["73rd Amendment", "State Election Commission", "Article 243K"], "Part 2"
    )

    # Q048 - Correct: D
    add_q(
        "CZ_AM_HD_048",
        "Which Constitutional Amendment Act substituted 'Armed Rebellion' for 'Internal Disturbance' in Article 352 and made written communication of the Cabinet decision mandatory for proclaiming National Emergency?",
        "சரத்து 352 இல் 'உள்நாட்டு அமைதியின்மை' என்பதற்குப் பதிலாக 'ஆயுதம் ஏந்திய கிளர்ச்சி' என்ற சொற்றொடரைச் சேர்த்து, தேசிய அவசரநிலையைப் பிரகடனப்படுத்த அமைச்சரவையின் எழுத்துப்பூர்வ முடிவைக் கட்டாயமாக்கிய அரசியலமைப்பு திருத்தச் சட்டம் எது?",
        "42nd Constitutional Amendment Act, 1976", "42வது அரசியலமைப்பு திருத்தச் சட்டம், 1976",
        "38th Constitutional Amendment Act, 1975", "38வது அரசியலமைப்பு திருத்தச் சட்டம், 1975",
        "52nd Constitutional Amendment Act, 1985", "52வது அரசியலமைப்பு திருத்தச் சட்டம், 1985",
        "44th Constitutional Amendment Act, 1978", "44வது அரசியலமைப்பு திருத்தச் சட்டம், 1978",
        "D",
        "The 44th Constitutional Amendment Act, 1978 introduced crucial safeguards in Article 352: (1) Substituted 'armed rebellion' for 'internal disturbance', (2) Required written advice of Union Cabinet, (3) Required special majority approval within 1 month.",
        "44வது அரசியலமைப்பு திருத்தச் சட்டம், 1978 சரத்து 352 இல் முக்கியப் பாதுகாப்புகளை அறிமுகப்படுத்தியது: (1) 'ஆயுதம் ஏந்திய கிளர்ச்சி' என மாற்றியது, (2) மத்திய அமைச்சரவையின் எழுத்துப்பூர்வ ஆலோசனையைக் கட்டாயமாக்கியது, (3) 1 மாதத்திற்குள் சிறப்புப் பெரும்பான்மை ஒப்புதலைக் கட்டாயமாக்கியது.",
        "Option A is incorrect; 42nd CA 1976 made Presidential satisfaction immune to judicial review.", "விருப்பம் A தவறானது; 42வது திருத்தம் 1976 குடியரசு தலைவர் திருப்தியை நீதிமன்ற ஆய்விலிருந்து விலக்கியது.",
        "Option B is incorrect; 38th CA 1975 made emergency declaration non-justiciable.", "விருப்பம் B தவறானது; 38வது திருத்தம் அவசரநிலை அறிவிப்பை நீதிமன்ற ஆய்வுக்கு அப்பாற்பட்டதாக்கியது.",
        "Option C is incorrect; 52nd CA 1985 enacted anti-defection law.", "விருப்பம் C தவறானது; 52வது திருத்தம் கட்சித் தாவல் தடைச் சட்டம் பற்றியது.",
        "Option D is correct because 44th CA 1978 substituted 'armed rebellion' and mandated written Cabinet advice under Article 352.", "விருப்பம் D சரியானது, ஏனெனில் 44வது திருத்தம் 1978 'ஆயுதம் ஏந்திய கிளர்ச்சி' மற்றும் எழுத்துப்பூர்வ அமைச்சரவை ஆலோசனையைச் சேர்த்தது.",
        "The term 'Cabinet' was inserted into the Indian Constitution for the very first time in Article 352 by the 44th Amendment Act, 1978.",
        "இந்திய அரசியலமைப்பில் 'அமைச்சரவை' (Cabinet) என்ற சொல் 44வது திருத்தச் சட்டம் 1978 மூலம் முதன்முறையாக சரத்து 352 இல் சேர்க்கப்பட்டது.",
        "Before 44th CA, Prime Minister Indira Gandhi had advised President Fakhruddin Ali Ahmed to declare emergency in 1975 without prior consultation with the Cabinet.",
        "44வது திருத்தத்திற்கு முன், 1975 இல் அமைச்சரவையுடன் கலந்தாலோசிக்காமல் பிரதமர் இந்திரா காந்தி குடியரசுத் தலைவருக்கு அவசரநிலை பிரகடனம் செய்ய ஆலோசனை வழங்கியிருந்தார்.",
        "Analysis", "High", ["44th Amendment", "Article 352 Armed Rebellion", "Cabinet Written Advice"], "Part 1"
    )

    # Q049 - Correct: A
    add_q(
        "CZ_AM_HD_049",
        "Which Constitutional Amendment Act inserted Article 21A, modified Article 45, and added Article 51A(k) establishing education as a fundamental right, DPSP directive, and fundamental duty?",
        "சரத்து 21A ஐச் சேர்த்து, சரத்து 45 ஐ திருத்தி, சரத்து 51A(k) ஐச் சேர்த்து கல்வியை அடிப்படை உரிமையாகவும், DPSP வழிகாட்டுதலாகவும், அடிப்படை கடமையாகவும் மாற்றிய அரசியலமைப்பு திருத்தச் சட்டம் எது?",
        "86th Constitutional Amendment Act, 2002", "86வது அரசியலமைப்பு திருத்தச் சட்டம், 2002",
        "84th Constitutional Amendment Act, 2001", "84வது அரசியலமைப்பு திருத்தச் சட்டம், 2001",
        "91st Constitutional Amendment Act, 2003", "91வது அரசியலமைப்பு திருத்தச் சட்டம், 2003",
        "93rd Constitutional Amendment Act, 2005", "93வது அரசியலமைப்பு திருத்தச் சட்டம், 2005",
        "A",
        "The 86th Constitutional Amendment Act, 2002 effected a triple constitutional change: (1) Art 21A in Part III, (2) Modified Art 45 in Part IV (early childhood care below 6 yrs), (3) Art 51A(k) in Part IV-A (duty of parent/guardian).",
        "86வது அரசியலமைப்பு திருத்தச் சட்டம், 2002 முப்பரிமாண மாற்றங்களைச் செய்தது: (1) பகுதி III இல் சரத்து 21A, (2) பகுதி IV இல் சரத்து 45 திருத்தம், (3) பகுதி IV-A இல் சரத்து 51A(k) கடமை சேர்க்கை.",
        "Option A is correct because 86th CA 2002 modified Part III, Part IV, and Part IV-A concurrently.", "விருப்பம் A சரியானது, ஏனெனில் 86வது திருத்தம் 2002 பகுதி III, IV, IV-A மூன்றிலும் மாற்றங்களை செய்தது.",
        "Option B is incorrect; 84th CA 2001 froze delimitation till 2026.", "விருப்பம் B தவறானது; 84வது திருத்தம் தொகுதி முடக்கம் பற்றியது.",
        "Option C is incorrect; 91st CA 2003 capped cabinet size at 15%.", "விருப்பம் C தவறானது; 91வது திருத்தம் 15% அமைச்சரவை வரம்பு பற்றியது.",
        "Option D is incorrect; 93rd CA 2005 inserted Article 15(5) for college reservation.", "விருப்பம் D தவறானது; 93வது திருத்தம் சரத்து 15(5) பற்றியது.",
        "Article 45 before 86th CA provided for free education up to 14 years within 10 years of Constitution; 86th CA redirected Art 45 to early childhood care (below 6 years).",
        "86வது திருத்தத்திற்கு முன் சரத்து 45 14 வயது வரை இலவசக் கல்வி எனக் கூறியது; 86வது திருத்தம் அதை 6 வயதிற்குட்பட்ட ஆரம்பப் பராமரிப்பாக மாற்றியது.",
        "Article 51A(k) mandates parent/guardian to provide education opportunities to child aged 6 to 14 years.",
        "சரத்து 51A(k) பெற்றோர்/பாதுகாவலர் 6 முதல் 14 வயதுக் குழந்தைக்குக் கல்வி வாய்ப்பளிக்கக் கடமைப்பட்டவர் என்கிறது.",
        "Analysis", "High", ["86th Amendment Triple Change", "Article 21A 45 51Ak"], "Part 2"
    )

    # Q050 - Correct: B
    add_q(
        "CZ_AM_HD_050",
        "Which Constitutional Amendment Act substituted 'shall give his assent' in Article 368(2), removing presidential discretion over Constitutional Amendment Bills?",
        "சரத்து 368(2) இல் 'ஒப்புதல் அளிக்க வேண்டும்' (shall give his assent) என மாற்றி, அரசியலமைப்பு திருத்த மசோதாக்கள் மீதான குடியரசுத் தலைவரின் விருப்ப அதிகாரத்தை நீக்கிய அரசியலமைப்பு திருத்தச் சட்டம் எது?",
        "1st Constitutional Amendment Act, 1951", "1வது அரசியலமைப்பு திருத்தச் சட்டம், 1951",
        "24th Constitutional Amendment Act, 1971", "24வது அரசியலமைப்பு திருத்தச் சட்டம், 1971",
        "7th Constitutional Amendment Act, 1956", "7வது அரசியலமைப்பு திருத்தச் சட்டம், 1956",
        "42nd Constitutional Amendment Act, 1976", "42வது அரசியலமைப்பு திருத்தச் சட்டம், 1976",
        "B",
        "The 24th Constitutional Amendment Act, 1971 amended Article 368(2) by substituting 'shall give his assent to the Bill' for 'he shall declare that he assents to the Bill or that he withholds assent therefrom'.",
        "24வது அரசியலமைப்பு திருத்தச் சட்டம், 1971 சரத்து 368(2) இல் 'மசோதாவிற்கு ஒப்புதல் அளிக்க வேண்டும்' என மாற்றி குடியரசுத் தலைவரின் நிராகரிப்பு அதிகாரத்தை நீக்கியது.",
        "Option A is incorrect; 1st CA added 9th Schedule.", "விருப்பம் A தவறானது; 1வது திருத்தம் 9வது அட்டவணையைச் சேர்த்தது.",
        "Option B is correct because 24th CA 1971 made Presidential assent mandatory under Article 368.", "விருப்பம் B சரியானது, ஏனெனில் 24வது திருத்தம் 1971 குடியரசு தலைவர் ஒப்புதலைக் கட்டாயமாக்கியது.",
        "Option C is incorrect; 7th CA reorganised states.", "விருப்பம் C தவறானது; 7வது திருத்தம் மாநிலங்கள் மறுசீரமைப்பு பற்றியது.",
        "Option D is incorrect; 42nd CA bound President to Cabinet advice under Article 74.", "விருப்பம் D தவறானது; 42வது திருத்தம் சரத்து 74 இன் கீழ் அமைச்சரவை ஆலோசனையைக் கட்டாயமாக்கியது.",
        "This amendment explicitly barred the President from using Suspensive Veto or Pocket Veto for Constitutional Amendment Bills.",
        "இந்தத் திருத்தம் அரசியலமைப்பு திருத்த மசோதாக்கள் மீது இடைநிறுத்த வீட்டோ அல்லது பாக்கெட் வீட்டோவைப் பயன்படுத்துவதைத் தடுத்தது.",
        "It ensured that once Parliament passes an amendment bill by required majority, Presidential assent is a mandatory formality.",
        "நாடாளுமன்றம் திருத்த மசோதாவை நிறைவேற்றியவுடன் குடியரசு தலைவர் ஒப்புதல் அளிப்பது கட்டாய நடைமுறையாகிறது.",
        "Analysis", "High", ["24th Amendment", "Article 368(2) Assent", "Presidential Discretion Removed"], "Part 1"
    )

    # Clean ID assignment
    for idx, q in enumerate(questions):
        q["id"] = f"CZ_AM_HD_{idx+1:03d}"

    return questions

if __name__ == "__main__":
    hd_qs = create_hard_questions()
    os.makedirs("data/questions/polity", exist_ok=True)
    out_path = "data/questions/polity/constitutional_amendments_hard.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(hd_qs, f, ensure_ascii=False, indent=2)
    
    from collections import Counter
    counts = Counter(q["correct_answer"] for q in hd_qs)
    print(f"Hard set complete. Total: {len(hd_qs)}")
    print(f"Answer balance: {dict(counts)}")
