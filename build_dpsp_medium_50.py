# build_dpsp_medium_50.py
# Generates 50 Medium MCQs for Directive Principles of State Policy (DPSP)
# Target file: data/questions/polity/directive_principles_medium.json

import json
import os

def generate_50_medium_mcqs():
    questions = []

    def add_q(q_id, q_type, q_en, q_ta, opt_a_en, opt_a_ta, opt_b_en, opt_b_ta, opt_c_en, opt_c_ta, opt_d_en, opt_d_ta, correct, exp_en, exp_ta, tip_en, tip_ta, w_a_en, w_a_ta, w_b_en, w_b_ta, w_c_en, w_c_ta, w_d_en, w_d_ta):
        q_obj = {
            "id": f"DPSP_M_{q_id:03d}",
            "subject": "Polity",
            "topic": "Directive Principles of State Policy",
            "difficulty": "Medium",
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
    # Q1 (Correct: A) - Conceptual Distinction
    # -------------------------------------------------------------------------
    add_q(
        1, "Conceptual",
        "Which of the following best reflects the legal distinction between Article 37 (Part IV) and Article 32 (Part III) of the Constitution?",
        "அரசியலமைப்பின் உறுப்பு 37 (பகுதி IV) மற்றும் உறுப்பு 32 (பகுதி III) இடையேயான சட்டப்பூர்வ வேறுபாட்டைப் பின்வருவனவற்றுள் எது மிகச்சரியாகப் பிரதிபலிக்கிறது?",
        "Article 37 declares DPSPs non-enforceable by courts, whereas Article 32 provides a justiciable Fundamental Right to move the Supreme Court for writ remedies", "உறுப்பு 37 DPSP-கள் நீதிமன்றங்களால் அமல்படுத்த முடியாதவை என்கிறது, மாறாக உறுப்பு 32 பேராணை பரிகாரங்களுக்காக உச்ச நீதிமன்றத்தை அணுகும் அமல்படுத்தக்கூடிய அடிப்படை உரிமையை வழங்குகிறது",
        "Article 37 empowers High Courts to enforce DPSPs, whereas Article 32 applies exclusively to Parliament", "உறுப்பு 37 உயர் நீதிமன்றங்களுக்கு DPSP-களை அமல்படுத்த அதிகாரமளிக்கிறது, மாறாக உறுப்பு 32 நாடாளுமன்றத்திற்கு மட்டுமே பொருந்தும்",
        "Article 37 applies only during a National Emergency, whereas Article 32 applies only during peacetime", "உறுப்பு 37 தேசிய அவசரநிலையின் போது மட்டுமே பொருந்தும், மாறாக உறுப்பு 32 அமைதி காலத்தில் மட்டுமே பொருந்தும்",
        "Article 37 creates criminal penalties for State inaction, whereas Article 32 grants civil damages", "உறுப்பு 37 அரசின் செயலின்மைக்குக் குற்றவியல் தண்டனைகளை உருவாக்குகிறது, மாறாக உறுப்பு 32 சிவில் நஷ்டஈடுகளை வழங்குகிறது",
        "A",
        "Article 37 explicitly makes DPSPs non-justiciable in any court, while Article 32 is itself a justiciable Fundamental Right guaranteeing constitutional remedies (writs) for Part III violations.",
        "உறுப்பு 37 DPSP-களை எந்தவொரு நீதிமன்றத்தாலும் அமல்படுத்த முடியாது எனக் கூறுகிறது, மாறாக உறுப்பு 32 பகுதி III மீறல்களுக்கு அரசியலமைப்பு பரிகாரங்களை (பேராணைகள்) உத்தரவாதம் செய்யும் அமல்படுத்தக்கூடிய அடிப்படை உரிமையாகும்.",
        "Remember: Article 37 explicitly bars courts from issuing writs for DPSP enforcement.",
        "நினைவில் கொள்க: DPSP அமலாக்கத்திற்காக நீதிமன்றங்கள் பேராணைகளைப் பிறப்பிப்பதை உறுப்பு 37 வெளிப்படையாகத் தடுக்கிறது.",
        "Correct. Article 37 declares DPSPs non-justiciable, while Article 32 is a justiciable writ remedy.", "சரி. உறுப்பு 37 DPSP-களை அமல்படுத்த முடியாதது என்கிறது, உறுப்பு 32 அமல்படுத்தக்கூடிய பேராணை பரிகாரமாகும்.",
        "Neither High Court nor Supreme Court can enforce Article 37 DPSPs directly via writs.", "உயர் நீதிமன்றமோ உச்ச நீதிமன்றமோ உறுப்பு 37 DPSP-களை நேரடியாகப் பேராணைகள் மூலம் அமல்படுத்த முடியாது.",
        "Article 37 applies at all times as a governance principle, not restricted to emergency.", "உறுப்பு 37 அவசரநிலைக்கு மட்டும் சுருங்காமல் அனைத்துக் காலங்களிலும் ஆட்சிக் கோட்பாடாகப் பொருந்தும்.",
        "Article 37 creates no criminal penalties or civil damages.", "உறுப்பு 37 குற்றவியல் தண்டனைகளையோ சிவில் நஷ்டஈடுகளையோ உருவாக்கவில்லை."
    )

    # -------------------------------------------------------------------------
    # Q2 (Correct: B) - Provision-based
    # -------------------------------------------------------------------------
    add_q(
        2, "Article-based",
        "Consider Articles 39(b) and 39(c). What specific economic objectives do these two clauses mandate?",
        "உறுப்புகள் 39(b) மற்றும் 39(c)-ஐக் கருதுக. இந்த இரண்டு உட்பிரிவுகளும் எந்த குறிப்பிட்ட பொருளாதார நோக்கங்களை ஆணையிடுகின்றன?",
        "39(b) mandates equal pay for equal work; 39(c) mandates free legal aid to workers", "39(b) சம வேலைக்கு சம ஊதியத்தைக் கட்டாயமாக்குகிறது; 39(c) தொழிலாளர்களுக்கு இலவச சட்ட உதவியைக் கட்டாயமாக்குகிறது",
        "39(b) mandates distribution of material resources for common good; 39(c) mandates prevention of concentration of wealth", "39(b) பொது நலனுக்காகச் சமூகத்தின் பொருள் வளங்களைப் பகிர்ந்தளிப்பதைக் கட்டாயமாக்குகிறது; 39(c) செல்வக் குவிப்பைத் தடுப்பதைக் கட்டாயமாக்குகிறது",
        "39(b) mandates statutory minimum wages; 39(c) mandates cottage industry subsidies", "39(b) சட்டப்பூர்வ குறைந்தபட்ச ஊதியத்தைக் கட்டாயமாக்குகிறது; 39(c) குடில்தொழில் மானியங்களைக் கட்டாயமாக்குகிறது",
        "39(b) mandates maternity relief; 39(c) mandates early childhood education below 6 years", "39(b) பேறுகால உதவியைக் கட்டாயமாக்குகிறது; 39(c) 6 வயதுக்குட்பட்ட முன்பருவக் கல்வியைக் கட்டாயமாக்குகிறது",
        "B",
        "Article 39(b) directs that ownership and control of material resources of the community are distributed to subserve the common good; Article 39(c) directs that the economic system does not result in the concentration of wealth and means of production.",
        "உறுப்பு 39(b) பொது நலனுக்குப் பயன்படும் வகையில் சமூகத்தின் பொருள் வளங்களின் உரிமையும் கட்டுப்பாடும் பகிர்ந்தளிக்கப்பட வேண்டும் என்கிறது; உறுப்பு 39(c) பொருளாதார அமைப்பு செல்வம் மற்றும் உற்பத்தி சாதனங்கள் குவிவதற்கு வழிவகுக்கக் கூடாது என்கிறது.",
        "Articles 39(b) and 39(c) are the ONLY two DPSPs protected under Article 31C against Articles 14 and 19.",
        "உறுப்புகள் 39(b) மற்றும் 39(c) ஆகியவை மட்டுமே உறுப்புகள் 14 மற்றும் 19-க்கு எதிராக உறுப்பு 31C-ன் கீழ் பாதுகாக்கப்பட்ட இரண்டு DPSP-கள் ஆகும்.",
        "Equal pay is 39(d); free legal aid is 39A.", "சம ஊதியம் 39(d); இலவச சட்ட உதவி 39A.",
        "Correct. 39(b) covers material resources distribution; 39(c) covers wealth concentration prevention.", "சரி. 39(b) பொருள் வளப் பகிர்வையும்; 39(c) செல்வக் குவிப்புத் தடையையும் உள்ளடக்கியது.",
        "Minimum wage is under Article 43.", "குறைந்தபட்ச ஊதியம் உறுப்பு 43-ன் கீழ் உள்ளது.",
        "Maternity relief is Article 42; early childhood education is Article 45.", "பேறுகால உதவி உறுப்பு 42; முன்பருவக் கல்வி உறுப்பு 45."
    )

    # -------------------------------------------------------------------------
    # Q3 (Correct: C) - Application / Inference
    # -------------------------------------------------------------------------
    add_q(
        3, "Application",
        "How does the Supreme Court harmonise Article 44 (Uniform Civil Code DPSP) with Articles 25 to 28 (Freedom of Religion FR)?",
        "உச்ச நீதிமன்றம் உறுப்பு 44-ஐ (பொது சிவில் சட்டம் DPSP) உறுப்புகள் 25 முதல் 28 வரையிலானவற்றுடன் (மத சுதந்திரம் FR) எவ்வாறு இணக்கமாக்குகிறது?",
        "SC ruled that personal laws are immune from any judicial scrutiny or equality standards", "தனிநபர் சட்டங்கள் எந்தவொரு நீதித்துறை ஆய்விலிருந்தோ சமத்துவத் தரங்கிலிருந்தோ விலக்கு பெற்றவை என SC தீர்ப்பளித்தது",
        "SC ruled that Article 44 automatically invalidates all religious freedoms under Article 25", "உறுப்பு 44 உறுப்பு 25-ன் கீழ் உள்ள அனைத்து மத சுதந்திரங்களையும் தானாகவே செல்லாததாக்குகிறது என SC தீர்ப்பளித்தது",
        "SC held that personal laws governing secular civil matters must yield to gender equality (Art 14) and human dignity without destroying religious freedom", "மத சுதந்திரத்தை அழிக்காமல், மதச்சார்பற்ற சிவில் விவகாரங்களை ஆளும் தனிநபர் சட்டங்கள் பாலின சமத்துவம் (உறுப்பு 14) மற்றும் மனித கண்ணியத்திற்குக் கட்டுப்பட வேண்டும் என SC கூறியது",
        "SC ruled that Uniform Civil Code can only be enacted by religious authorities, not Parliament", "பொது சிவில் சட்டத்தை நாடாளுமன்றம் அல்லாமல் மத அமைப்புகள் மட்டுமே இயற்ற முடியும் என SC தீர்ப்பளித்தது",
        "C",
        "In cases like Sarla Mudgal (1995) and Shayara Bano (2017), the SC held that religious freedom under Article 25 covers essential religious practices, but secular civil practices (marriage, divorce, inheritance) must conform to Article 14 gender equality and human dignity.",
        "சர்லா முத்கல் (1995) மற்றும் ஷாயரா பானோ (2017) வழக்குகளில், உறுப்பு 25-ன் கீழ் உள்ள மத சுதந்திரம் அத்தியாவசிய மத நடைமுறைகளை உள்ளடக்கியது, ஆனால் மதச்சார்பற்ற சிவில் நடைமுறைகள் உறுப்பு 14 பாலின சமத்துவத்திற்கும் மனித கண்ணியத்திற்கும் கட்டுப்பட வேண்டும் என SC தீர்ப்பளித்தது.",
        "Harmonious construction ensures secular civil uniformity without violating core freedom of conscience.",
        "இணக்கமான விளக்கம் அடிப்படை மனசாட்சி சுதந்திரத்தை மீறாமல் மதச்சார்பற்ற சிவில் சீரான தன்மையை உறுதி செய்கிறது.",
        "Personal laws are subject to constitutional equality and human rights.", "தனிநபர் சட்டங்கள் அரசியலமைப்பு சமத்துவம் மற்றும் மனித உரிமைகளுக்கு உட்பட்டவை.",
        "Article 44 does not invalidate Article 25; both coexist harmoniously.", "உறுப்பு 44 உறுப்பு 25-ஐ செல்லாததாக்கவில்லை; இரண்டும் இணக்கமாக இணைந்து வாழ்கின்றன.",
        "Correct. SC held secular civil personal laws are subject to Art 14 gender equality and dignity.", "சரி. மதச்சார்பற்ற சிவில் தனிநபர் சட்டங்கள் உறுப்பு 14 பாலின சமத்துவத்திற்கும் கண்ணியத்திற்கும் உட்பட்டவை என SC கூறியது.",
        "Parliament has power under Entry 5 of Concurrent List to enact personal/civil laws.", "பொதுப் பட்டியலின் பிரிவு 5-ன் கீழ் தனிநபர்/சிவில் சட்டங்களை இயற்ற நாடாளுமன்றத்திற்கு அதிகாரம் உண்டு."
    )

    # -------------------------------------------------------------------------
    # Q4 (Correct: D) - Amendment / Case
    # -------------------------------------------------------------------------
    add_q(
        4, "Amendment/Case",
        "Which set of four Directive Principles was inserted into Part IV by the landmark 42nd Constitutional Amendment Act, 1976?",
        "1976-ன் வரலாற்றுச் சிறப்புமிக்க 42வது அரசியலமைப்பு திருத்தச் சட்டத்தால் பகுதி IV-ல் சேர்க்கப்பட்ட நான்கு வழிகாட்டு நெறிமுறைகளின் தொகுதி எது?",
        "Articles 38(2), 40, 44, and 45", "உறுப்புகள் 38(2), 40, 44, மற்றும் 45",
        "Articles 39(b), 39(c), 41, and 43", "உறுப்புகள் 39(b), 39(c), 41, மற்றும் 43",
        "Articles 43B, 46, 47, and 48", "உறுப்புகள் 43B, 46, 47, மற்றும் 48",
        "Articles 39(f), 39A, 43A, and 48A", "உறுப்புகள் 39(f), 39A, 43A, மற்றும் 48A",
        "D",
        "The 42nd Constitutional Amendment Act, 1976 added 4 new DPSPs: Article 39(f) (healthy child development), Article 39A (free legal aid), Article 43A (workers' participation in management), and Article 48A (environment and wildlife protection).",
        "1976-ன் 42வது அரசியலமைப்பு திருத்தச் சட்டம் 4 புதிய DPSP-களைச் சேர்த்தது: உறுப்பு 39(f) (குழந்தை வளர்ச்சி), உறுப்பு 39A (இலவச சட்ட உதவி), உறுப்பு 43A (மேலாண்மையில் தொழிலாளர் பங்கேற்பு), மற்றும் உறுப்பு 48A (சுற்றுச்சூழல் பாதுகாப்பு).",
        "Memory Trick for 42nd CAA DPSPs: Children (39f), Legal Aid (39A), Worker Mgmt (43A), Environment (48A).",
        "நினைவுக் குறிப்பு: குழந்தைகள் (39f), சட்ட உதவி (39A), தொழிலாளர் மேலாண்மை (43A), சுற்றுச்சூழல் (48A).",
        "Article 38(2) was added by 44th CAA 1978; 40, 44, 45 were in original 1950 text.", "உறுப்பு 38(2) 44வது திருத்தத்தால் சேர்க்கப்பட்டது; 40, 44, 45 அசல் 1950 உரையில் இருந்தன.",
        "Articles 39(b), 39(c), 41, 43 were part of original 1950 text.", "உறுப்புகள் 39(b), 39(c), 41, 43 அசல் 1950 உரையின் பகுதியாகும்.",
        "Article 43B was added by 97th CAA 2011; 46, 47, 48 were in original 1950 text.", "உறுப்பு 43B 97வது திருத்தம் 2011 மூலம் சேர்க்கப்பட்டது; 46, 47, 48 அசல் உரையில் இருந்தன.",
        "Correct. 42nd Amendment 1976 added Articles 39(f), 39A, 43A, and 48A.", "சரி. 42வது திருத்தம் 1976 உறுப்புகள் 39(f), 39A, 43A, மற்றும் 48A-ஐச் சேர்த்தது."
    )

    # -------------------------------------------------------------------------
    # Q5 (Correct: A) - Case-based
    # -------------------------------------------------------------------------
    add_q(
        5, "Amendment/Case",
        "In Minerva Mills v. Union of India (1980), why did the Supreme Court invalidate Section 4 of the 42nd Amendment Act 1976?",
        "மினர்வா மில்ஸ் எதிர் இந்திய யூனியன் வழக்கில் (1980), 42வது திருத்தச் சட்டம் 1976-ன் பிரிவு 4-ஐ உச்ச நீதிமன்றம் ஏன் செல்லாததாக அறிவித்தது?",
        "Because Section 4 attempted to give ALL Directive Principles precedence over Fundamental Rights (Arts 14 & 19), destroying the Basic Structure harmony", "ஏனெனில் பிரிவு 4 அனைத்து வழிகாட்டு நெறிமுறைகளுக்கும் அடிப்படை உரிமைகளை (உறுப்புகள் 14 & 19) விட முதன்மை அளிக்க முயன்று, அடிப்படை அமைப்பின் இணக்கத்தைச் சிதைத்தது",
        "Because Section 4 abolished the office of the Prime Minister during Emergency", "ஏனெனில் பிரிவு 4 அவசரநிலையின் போது பிரதமர் பதவியை ஒழித்தது",
        "Because Section 4 made Directive Principles justiciable in High Courts", "ஏனெனில் பிரிவு 4 வழிகாட்டு நெறிமுறைகளை உயர் நீதிமன்றங்களில் அமல்படுத்தக்கூடியதாக மாற்றியது",
        "Because Section 4 removed Article 39(b) and 39(c) from Part IV text", "ஏனெனில் பிரிவு 4 பகுதி IV உரையிலிருந்து உறுப்புகள் 39(b) மற்றும் 39(c)-ஐ நீக்கியது",
        "A",
        "Section 4 of 42nd CAA 1976 tried to extend Article 31C protection to ALL DPSPs over Articles 14 and 19. In Minerva Mills (1980), SC held that giving absolute primacy to Part IV over Part III destroys the HARMONY AND BALANCE which is a Basic Feature of the Constitution.",
        "1976-ன் 42வது திருத்தத்தின் பிரிவு 4 உறுப்புகள் 14 மற்றும் 19-ஐ விட அனைத்து DPSP-களுக்கும் உறுப்பு 31C பாதுகாப்பை நீட்டிக்க முயன்றது. மினர்வா மில்ஸ் வழக்கில் (1980), பகுதி III-ஐ விட பகுதி IV-க்கு முழு முதன்மை அளிப்பது அரசியலமைப்பின் அடிப்படை அம்சமான இணக்கத்தையும் சமநிலையையும் சிதைக்கும் என SC தீர்ப்பளித்தது.",
        "Post-Minerva Mills: Priority over Arts 14 and 19 remains restricted ONLY to Articles 39(b) and 39(c).",
        "மினர்வா மில்ஸுக்குப் பின்: உறுப்புகள் 14 மற்றும் 19-ஐ விட முன்னுரிமை உறுப்புகள் 39(b) மற்றும் 39(c)-க்கு மட்டுமே சுருக்கப்பட்டுள்ளது.",
        "Correct. Section 4 gave absolute primacy to all DPSPs over FRs, disturbing Basic Structure harmony.", "சரி. பிரிவு 4 FR-களை விட அனைத்து DPSP-களுக்கும் முழு முதன்மை அளித்து, அடிப்படை அமைப்பின் இணக்கத்தைக் குலைத்தது.",
        "Section 4 did not deal with Prime Minister's office.", "பிரிவு 4 பிரதமர் அலுவலகத்தைப் பற்றியது அல்ல.",
        "Section 4 did not make DPSPs justiciable.", "பிரிவு 4 DPSP-களை அமல்படுத்தக்கூடியதாக மாற்றவில்லை.",
        "Section 4 did not remove 39(b) or 39(c).", "பிரிவு 4 39(b) அல்லது 39(c)-ஐ நீக்கவில்லை."
    )

    # -------------------------------------------------------------------------
    # Q6 (Correct: B) - Simple Comparison
    # -------------------------------------------------------------------------
    add_q(
        6, "Comparison",
        "Which statement correctly compares Article 40 (DPSP) with Part IX (Articles 243–243O) inserted by the 73rd Amendment Act 1992?",
        "உறுப்பு 40-ஐ (DPSP) 73வது திருத்தச் சட்டம் 1992-ல் இணைக்கப்பட்ட பகுதி IX உடன் (உறுப்புகள் 243–243O) சரியாக ஒப்பிடும் கூற்று எது?",
        "Article 40 is a justiciable law, whereas Part IX is a non-justiciable vision statement", "உறுப்பு 40 ஒரு அமல்படுத்தக்கூடிய சட்டம், மாறாக பகுதி IX ஒரு அமல்படுத்த முடியாத தொலைநோக்கு அறிக்கை",
        "Article 40 is a non-justiciable DPSP directive, whereas Part IX provides a mandatory justiciable constitutional framework for 3-tier Panchayati Raj", "உறுப்பு 40 ஒரு அமல்படுத்த முடியாத DPSP வழிகாட்டுதல், மாறாக பகுதி IX 3-அடுக்கு பஞ்சாயத்து ராஜிற்கான கட்டாய அமல்படுத்தக்கூடிய அரசியலமைப்பு சட்டக் கட்டமைப்பை வழங்குகிறது",
        "Article 40 applies only to urban municipalities, whereas Part IX applies only to tribal areas", "உறுப்பு 40 நகர்ப்புற நகராட்சிகளுக்கு மட்டுமே பொருந்தும், மாறாக பகுதி IX பழங்குடியினப் பகுதிகளுக்கு மட்டுமே பொருந்தும்",
        "Article 40 was deleted from the Constitution after the 73rd Amendment was enacted", "73வது திருத்தம் இயற்றப்பட்ட பிறகு உறுப்பு 40 அரசியலமைப்பிலிருந்து நீக்கப்பட்டது",
        "B",
        "Article 40 is a non-justiciable DPSP policy goal directing State to organize village panchayats. The 73rd Amendment Act 1992 created Part IX and 11th Schedule, making a 3-tier Panchayati Raj structure mandatory and constitutionally enforceable.",
        "உறுப்பு 40 என்பது கிராம ஊராட்சிகளை அமைக்க அரசுக்கு ஆணையிடும் ஒரு அமல்படுத்த முடியாத DPSP கொள்கை இலக்காகும். 73வது திருத்தச் சட்டம் 1992 பகுதி IX மற்றும் 11வது அட்டவணையை உருவாக்கி, 3-அடுக்கு பஞ்சாயத்து ராஜ் அமைப்பைக் கட்டாயமாகவும் அரசியலமைப்பு ரீதியாக அமல்படுத்தக்கூடியதாகவும் மாற்றியது.",
        "Article 40 represents the policy seed; Part IX represents the statutory constitutional tree.",
        "உறுப்பு 40 கொள்கை விதையைக் குறிக்கிறது; பகுதி IX சட்டப்பூர்வ அரசியலமைப்பு மரத்தைக் குறிக்கிறது.",
        "Incorrect reversal: Article 40 is non-justiciable; Part IX is justiciable constitutional law.", "சட்ட அந்தஸ்தின் தவறான தலைகீழ் கூற்று.",
        "Correct. Article 40 is a DPSP directive; Part IX is mandatory 3-tier constitutional framework.", "சரி. உறுப்பு 40 DPSP வழிகாட்டுதல்; பகுதி IX கட்டாய 3-அடுக்கு அரசியலமைப்பு சட்டக் கட்டமைப்பு.",
        "Article 40 deals with village panchayats (rural); municipalities are Part IX-A (Art 243P-243ZG).", "உறுப்பு 40 கிராம ஊராட்சிகள் பற்றியது; நகராட்சிகள் பகுதி IX-A ஆகும்.",
        "Article 40 remains active in Part IV text.", "உறுப்பு 40 பகுதி IV உரையில் தொடர்ந்து செயல்படுகிறது."
    )

    # -------------------------------------------------------------------------
    # Q7 (Correct: C) - Conceptual Distinction
    # -------------------------------------------------------------------------
    add_q(
        7, "Conceptual",
        "In economic jurisprudence and labor welfare under Article 43, how is 'Living Wage' distinguished from 'Minimum Wage' and 'Fair Wage'?",
        "பொருளாதாரச் சட்டவியல் மற்றும் உறுப்பு 43-ன் கீழ் உள்ள தொழிலாளர் நலனில், 'வாழ்வாதார ஊதியம்' (Living Wage) என்பது 'குறைந்தபட்ச ஊதியம்' மற்றும் 'நியாயமான ஊதியத்திலிருந்து' எவ்வாறு வேறுபடுத்தப்படுகிறது?",
        "Living Wage covers bare food for worker physical survival only", "வாழ்வாதார ஊதியம் தொழிலாளியின் வெறும் உடல் வாழ்வாதாரத்திற்கான உணவை மட்டுமே உள்ளடக்கியது",
        "Living Wage is lower than Minimum Wage and excludes medical care", "வாழ்வாதார ஊதியம் குறைந்தபட்ச ஊதியத்தை விடக் குறைவானது மற்றும் மருத்துவப் பராமரிப்பை விலக்குகிறது",
        "Living Wage is the highest standard covering food, clothing, shelter PLUS education, health insurance, social security, and reasonable leisure", "வாழ்வாதார ஊதியம் என்பது உணவு, உடை, இருப்பிடத்துடன் கல்வி, சுகாதாரக் காப்பீடு, சமூகப் பாதுகாப்பு மற்றும் நியாயமான ஓய்வை உள்ளடக்கிய மிக உயர்ந்த தரமாகும்",
        "Living Wage is paid only to government IAS officers", "வாழ்வாதார ஊதியம் அரசு IAS அதிகாரிகளுக்கு மட்டுமே வழங்கப்படுகிறது",
        "C",
        "Under Article 43, 'Living Wage' is the ideal constitutional wage level which provides not merely bare subsistence, but a decent standard of life, education for children, health protection, social security, and full enjoyment of leisure.",
        "உறுப்பு 43-ன் கீழ், 'வாழ்வாதார ஊதியம்' என்பது வெறும் உடல் வாழ்வாதாரத்தை மட்டுமல்லாமல், கண்ணியமான வாழ்க்கை முறை, குழந்தைகளின் கல்வி, சுகாதாரப் பாதுகாப்பு, சமூகப் பாதுகாப்பு மற்றும் முழு ஓய்வை வழங்கும் லட்சிய அரசியலமைப்பு ஊதிய நிலையாகும்.",
        "Hierarchy: Minimum Wage (bare survival) < Fair Wage (industry capacity) < Living Wage (full security & decent life).",
        "படிநிலை: குறைந்தபட்ச ஊதியம் < நியாயமான ஊதியம் < வாழ்வாதார ஊதியம்.",
        "Bare physical survival food/clothing/shelter is Minimum Wage.", "வெறும் உடல் வாழ்வாதார உணவு/உடை/இருப்பிடம் குறைந்தபட்ச ஊதியமாகும்.",
        "Living Wage is the highest level, not lower than Minimum Wage.", "வாழ்வாதார ஊதியம் மிக உயர்ந்த நிலை, குறைந்தபட்ச ஊதியத்தை விடக் குறைவானது அல்ல.",
        "Correct. Living Wage is the highest wage standard covering decent life, education, health & leisure.", "சரி. வாழ்வாதார ஊதியம் என்பது கண்ணியமான வாழ்க்கை, கல்வி, சுகாதாரம் & ஓய்வை உள்ளடக்கிய மிக உயர்ந்த ஊதியத் தரமாகும்.",
        "Article 43 applies to all workers (agricultural, industrial or otherwise).", "உறுப்பு 43 அனைத்துத் தொழிலாளர்களுக்கும் (விவசாய, தொழில்துறை அல்லது பிற) பொருந்தும்."
    )

    # -------------------------------------------------------------------------
    # Q8 (Correct: D) - Amendment / Case
    # -------------------------------------------------------------------------
    add_q(
        8, "Amendment/Case",
        "What structural change was effected in the Indian Constitution by the 86th Constitutional Amendment Act, 2002 regarding education?",
        "கல்வி தொடர்பாக 2002-ன் 86வது அரசியலமைப்பு திருத்தச் சட்டத்தால் இந்திய அரசியலமைப்பில் என்ன அமைப்புக் மாற்றம் செய்யப்பட்டது?",
        "It deleted Article 45 completely without adding any new article", "இது எந்தவொரு புதிய உறுப்பையும் சேர்க்காமல் உறுப்பு 45-ஐ முழுமையாக நீக்கியது",
        "It made higher university education a Fundamental Right under Article 19", "இது உறுப்பு 19-ன் கீழ் உயர் பல்கலைக்கழகக் கல்வியை அடிப்படை உரிமையாக்கியது",
        "It converted Article 45 into a penal provision punishing illiterate parents", "இது உறுப்பு 45-ஐ எழுத்தறிவில்லாத பெற்றோரைத் தண்டிக்கும் குற்றவியல் விதியாக மாற்றியது",
        "It created Article 21A (FR for 6-14 yrs), substituted Article 45 (DPSP for below 6 yrs), and added Article 51A(k) (FD)", "இது உறுப்பு 21A-ஐ (6-14 வயது FR) உருவாக்கி, உறுப்பு 45-ஐ (6 வயதுக்குட்பட்ட DPSP) மாற்றியமைத்து, உறுப்பு 51A(k)-ஐச் (FD) சேர்த்தது",
        "D",
        "The 86th Amendment Act 2002 enacted a comprehensive 3-way educational package: 1) Created Art 21A (FR for 6-14 yrs); 2) Substituted Art 45 (DPSP for early childhood care below 6 yrs); 3) Inserted Art 51A(k) (FD for parents).",
        "2002-ன் 86வது திருத்தச் சட்டம் ஒரு விரிவான 3-வழி கல்வித் தொகுப்பை இயற்றியது: 1) உறுப்பு 21A உருவாக்கப்பட்டது (6-14 வயது FR); 2) உறுப்பு 45 மாற்றப்பட்டது (6 வயதுக்குட்பட்ட DPSP); 3) உறுப்பு 51A(k) சேர்க்கப்பட்டது (பெற்றோர் FD).",
        "Right of Children to Free and Compulsory Education (RTE) Act 2009 was enacted to implement Article 21A.",
        "உறுப்பு 21A-ஐ செயல்படுத்த 2009-ல் குழந்தைகளுக்கான இலவச மற்றும் கட்டாயக் கல்வி உரிமைச் (RTE) சட்டம் இயற்றப்பட்டது.",
        "Article 45 was substituted, not deleted.", "உறுப்பு 45 மாற்றியமைக்கப்பட்டது, நீக்கப்படவில்லை.",
        "Article 21A covers elementary education (6-14 yrs), not higher university education.", "உறுப்பு 21A தொடக்கக் கல்வியை (6-14 ஆண்டுகள்) உள்ளடக்கியது, உயர் பல்கலைக்கழகக் கல்வியை அல்ல.",
        "Article 51A(k) is a Fundamental Duty, not a penal provision.", "உறுப்பு 51A(k) ஒரு அடிப்படைக் கடமை, குற்றவியல் விதி அல்ல.",
        "Correct. 86th Amendment created Art 21A (FR), substituted Art 45 (DPSP), and added Art 51A(k) (FD).", "சரி. 86வது திருத்தம் உறுப்பு 21A (FR), உறுப்பு 45 (DPSP) மற்றும் உறுப்பு 51A(k) (FD) ஆகியவற்றை உருவாக்கியது."
    )

    # -------------------------------------------------------------------------
    # Q9 (Correct: A) - Simple Comparison
    # -------------------------------------------------------------------------
    add_q(
        9, "Comparison",
        "Which statement correctly highlights the constitutional relationship between Article 48A (Part IV DPSP) and Article 51A(g) (Part IV-A FD)?",
        "உறுப்பு 48A (பகுதி IV DPSP) மற்றும் உறுப்பு 51A(g) (பகுதி IV-A FD) இடையேயான அரசியலமைப்புத் தொடர்பை மிகச்சரியாக முன்னிலைப்படுத்தும் கூற்று எது?",
        "Article 48A is a State directive and Article 51A(g) is a Citizen duty; together read with Article 21, SC enforces the Right to Clean Environment", "உறுப்பு 48A அரசு வழிகாட்டுதல் மற்றும் உறுப்பு 51A(g) குடிமகன் கடமை; உறுப்பு 21-உடன் இணைந்து வாசிக்கப்படும் போது SC தூய்மையான சுற்றுச்சூழல் உரிமையை அமல்படுத்துகிறது",
        "Article 48A applies only to private factories, while Article 51A(g) applies only to public servants", "உறுப்பு 48A தனியார் தொழிற்சாலைகளுக்கு மட்டுமே பொருந்தும், 51A(g) அரசு ஊழியர்களுக்கு மட்டுமே பொருந்தும்",
        "Article 48A was enacted in 1950, while Article 51A(g) was enacted by the 86th Amendment in 2002", "உறுப்பு 48A 1950-ல் இயற்றப்பட்டது, 51A(g) 2002-ன் 86வது திருத்தத்தால் இயற்றப்பட்டது",
        "Article 48A overrides all environmental laws passed by Parliament", "உறுப்பு 48A நாடாளுமன்றத்தால் இயற்றப்பட்ட அனைத்து சுற்றுச்சூழல் சட்டங்களையும் மிஞ்சுகிறது",
        "A",
        "In landmark environmental rulings (M.C. Mehta cases), the SC held that Article 48A (State obligation) and Article 51A(g) (Citizen duty) read together with Article 21 elevate the 'Right to Clean Environment' to a justiciable Fundamental Right.",
        "முக்கிய சுற்றுச்சூழல் தீர்ப்புகளில் (எம்.சி. மேத்தா வழக்குகள்), உறுப்பு 48A (அரசு கடமை) மற்றும் உறுப்பு 51A(g) (குடிமகன் கடமை) ஆகியவை உறுப்பு 21-உடன் இணைந்து வாசிக்கப்படும் போது 'தூய்மையான சுற்றுச்சூழல் உரிமை' ஒரு அமல்படுத்தக்கூடிய அடிப்படை உரிமையாக உயர்த்தப்படுகிறது என SC தீர்ப்பளித்தது.",
        "Both Article 48A and Article 51A(g) were inserted by the 42nd Constitutional Amendment Act, 1976.",
        "48A மற்றும் 51A(g) ஆகிய இரண்டும் 1976-ன் 42வது அரசியலமைப்பு திருத்தச் சட்டத்தால் இணைக்கப்பட்டன.",
        "Correct. 48A (State) and 51A(g) (Citizen) read with Art 21 form the Right to Clean Environment.", "சரி. 48A (அரசு) மற்றும் 51A(g) (குடிமகன்) உறுப்பு 21-உடன் இணைந்து தூய்மையான சுற்றுச்சூழல் உரிமையை உருவாக்குகின்றன.",
        "48A applies to the State; 51A(g) applies to all citizens.", "48A அரசுக்குப் பொருந்தும்; 51A(g) அனைத்துக் குடிமக்களுக்கும் பொருந்தும்.",
        "Both were added by the 42nd Amendment in 1976, not 1950 or 2002.", "இரண்டும் 1976-ன் 42வது திருத்தத்தால் சேர்க்கப்பட்டவை, 1950 அல்லது 2002-ல் அல்ல.",
        "48A guides state law-making; it does not override statutory environment Acts.", "48A அரசுச் சட்ட உருவாக்கத்திற்கு வழிகாட்டுகிறது; இது சட்டப்பூர்வ சுற்றுச்சூழல் சட்டங்களை மிஞ்சாது."
    )

    # -------------------------------------------------------------------------
    # Q10 (Correct: B) - Conceptual Distinction
    # -------------------------------------------------------------------------
    add_q(
        10, "Conceptual",
        "Article 50 directs the State to separate the judiciary from the executive in the public services. Why does India NOT follow a rigid, absolute doctrine of Separation of Powers?",
        "உறுப்பு 50 பொது சேவைகளில் நிர்வாகத்திலிருந்து நீதித்துறையைப் பிரிக்க அரசுக்கு வழிகாட்டுகிறது. இந்தியா ஏன் கடுமையான, முற்றுமுழுதான அதிகாரப் பிரிப்புக் கோட்பாட்டைப் பின்பற்றவில்லை?",
        "Because India is a unitary monarchy ruled by an absolute sovereign", "ஏனெனில் இந்தியா முற்றுமுழுதான மன்னரால் ஆளப்படும் ஒற்றையாட்சி முடியரசாகும்",
        "Because India follows a Parliamentary system of government where the Executive is drawn from and responsible to the Legislature, operating with checks and balances", "ஏனெனில் இந்தியா நாடாளுமன்ற அரசாங்க முறையைப் பின்பற்றுகிறது, இதில் நிர்வாகம் சட்டமன்றத்திலிருந்து பெறப்பட்டு பொறுப்பாக உள்ளது, கட்டுப்பாடுகள் மற்றும் சமநிலைகளுடன் செயல்படுகிறது",
        "Because Supreme Court judges are appointed directly by popular elections", "ஏனெனில் உச்ச நீதிமன்ற நீதிபதிகள் மக்களால் நேரடியாகத் தேர்ந்தெடுக்கப்படுகிறார்கள்",
        "Because State Assemblies can veto rulings of the Supreme Court of India", "ஏனெனில் மாநில சட்டமன்றங்கள் இந்திய உச்ச நீதிமன்றத்தின் தீர்ப்புகளை வீட்டோ செய்ய முடியும்",
        "B",
        "Unlike the US Presidential system which follows rigid separation of powers, India follows a Parliamentary democracy where the Executive (Prime Minister & Cabinet) is an integral part of the Legislature, bound by collective responsibility and checks and balances.",
        "கடுமையான அதிகாரப் பிரிப்பைப் பின்பற்றும் அமெரிக்க அதிபர் முறையைப் போலன்றி, இந்தியா ஒரு நாடாளுமன்ற ஜனநாயகத்தைப் பின்பற்றுகிறது, இதில் நிர்வாகம் (பிரதமர் & அமைச்சரவை) சட்டமன்றத்தின் ஒருங்கமைந்த பகுதியாகும், இது கூட்டுப் பொறுப்பு மற்றும் கட்டுப்பாடுகள் மற்றும் சமநிலைகளால் கட்டுப்படுத்தப்படுகிறது.",
        "Article 50 specifically targets judicial independence in public services (separating judicial magistrates from executive collectors).",
        "உறுப்பு 50 பொது சேவைகளில் நீதித்துறை சுயசார்பைக் குறிப்பாக நோக்கமாகக் கொண்டுள்ளது (நீதித்துறை மேஜிஸ்திரேட்டுகளை நிர்வாக ஆட்சியர்களிடமிருந்து பிரித்தல்).",
        "India is a Sovereign Democratic Republic, not a monarchy.", "இந்தியா ஒரு இறையாண்மையுள்ள ஜனநாயகக் குடியரசு, முடியரசு அல்ல.",
        "Correct. India follows Parliamentary Democracy with executive-legislature overlap and checks and balances.", "சரி. இந்தியா நிர்வாகம்-சட்டமன்றக் கலப்பு மற்றும் கட்டுப்பாடுகள் மற்றும் சமநிலைகளுடன் கூடிய நாடாளுமன்ற ஜனநாயகத்தைப் பின்பற்றுகிறது.",
        "Judges are appointed by President via collegium system, not popular election.", "நீதிபதிகள் கொலீஜியம் முறை மூலம் குடியரசுத் தலைவரால் நியமிக்கப்படுகிறார்கள், மக்கள் தேர்தலால் அல்ல.",
        "State Assemblies cannot veto Supreme Court judgments.", "மாநில சட்டமன்றங்கள் உச்ச நீதிமன்றத் தீர்ப்புகளை வீட்டோ செய்ய முடியாது."
    )

    # -------------------------------------------------------------------------
    # Q11 (Correct: C) - Article-based
    # -------------------------------------------------------------------------
    add_q(
        11, "Article-based",
        "Consider Article 38(1) and Article 38(2). Which of the following statements correctly distinguishes their scope?",
        "உறுப்பு 38(1) மற்றும் உறுப்பு 38(2)-ஐக் கருதுக. பின்வரும் கூற்றுகளில் எது அவற்றின் எல்லையைச் சரியாக வேறுபடுத்துகிறது?",
        "38(1) deals with military defence; 38(2) deals with foreign trade", "38(1) இராணுவப் பாதுகாப்பு பற்றியது; 38(2) வெளிநாட்டு வர்த்தகம் பற்றியது",
        "38(1) was added by 42nd Amendment; 38(2) was in original 1950 text", "38(1) 42வது திருத்தத்தால் சேர்க்கப்பட்டது; 38(2) அசல் 1950 உரையில் இருந்தது",
        "38(1) directs securing a social order for promotion of welfare (social, economic, political justice); 38(2) (added by 44th CAA 1978) specifically directs minimising inequalities in income, status, facilities, and opportunities", "38(1) மக்கள் நலனுக்கான சமூக ஒழுங்கை உருவாக்குவதை வழிகாட்டுகிறது; 38(2) (44வது திருத்தம் 1978 மூலம் சேர்க்கப்பட்டது) வருமானம், அந்தஸ்து, வசதிகள், வாய்ப்புகளில் சமத்துவமின்மையைக் குறைப்பதை வெளிப்படையாக வழிகாட்டுகிறது",
        "38(1) applies only to High Courts; 38(2) applies only to District Courts", "38(1) உயர் நீதிமன்றங்களுக்கு மட்டுமே பொருந்தும்; 38(2) மாவட்ட நீதிமன்றங்களுக்கு மட்டுமே பொருந்தும்",
        "C",
        "Article 38(1) (original text) commands the State to strive to promote welfare by securing a social order in which social, economic and political justice informs all institutions. Article 38(2) (added by 44th CAA 1978) directs minimising inequalities in income, status, facilities, and opportunities.",
        "உறுப்பு 38(1) (அசல் உரை) சமூக, பொருளாதார மற்றும் அரசியல் நீதி நிறைந்த சமூக ஒழுங்கை உருவாக்கி மக்கள் நலனை மேம்படுத்த முயலுமாறு அரசுக்கு ஆணையிடுகிறது. உறுப்பு 38(2) (44வது திருத்தம் 1978 மூலம் சேர்க்கப்பட்டது) வருமானம், அந்தஸ்து, வசதிகள், வாய்ப்புகளில் சமத்துவமின்மையைக் குறைக்க வழிகாட்டுகிறது.",
        "Article 38 is the primary overarching Welfare State directive in Part IV.", "உறுப்பு 38 என்பது பகுதி IV-ல் உள்ள முதன்மையான ஒட்டுமொத்த நல அரசு வழிகாட்டுதலாகும்.",
        "Neither clause deals with military defence or foreign trade.", "எந்தவொரு உட்பிரிவும் இராணுவப் பாதுகாப்பு அல்லது வெளிநாட்டு வர்த்தகம் பற்றியது அல்ல.",
        "Incorrect reversal: 38(1) was original; 38(2) was added by 44th Amendment in 1978.", "தவறான தலைகீழ் கூற்று: 38(1) அசலானது; 38(2) 1978-ன் 44வது திருத்தத்தால் சேர்க்கப்பட்டது.",
        "Correct. 38(1) is original social order welfare; 38(2) is 44th Amendment minimising inequalities directive.", "சரி. 38(1) அசல் சமூக ஒழுங்கு நலன்; 38(2) சமத்துவமின்மையைக் குறைக்கும் 44வது திருத்த வழிகாட்டுதல்.",
        "Article 38 applies to the State governance, not court jurisdiction.", "உறுப்பு 38 அரசின் ஆட்சிக்கே பொருந்தும், நீதிமன்ற அதிகார வரம்பிற்கு அல்ல."
    )

    # -------------------------------------------------------------------------
    # Q12 (Correct: D) - Case-based
    # -------------------------------------------------------------------------
    add_q(
        12, "Amendment/Case",
        "In Kesavananda Bharati case (1973), what was the Supreme Court's ruling on the validity of Article 31C inserted by the 25th Constitutional Amendment Act 1971?",
        "கேசவானந்த பாரதி வழக்கில் (1973), 25வது அரசியலமைப்பு திருத்தச் சட்டம் 1971-ன் மூலம் இணைக்கப்பட்ட உறுப்பு 31C-ன் செல்லுபடித் தன்மை குறித்து உச்ச நீதிமன்றத்தின் தீர்ப்பு என்ன?",
        "SC declared the entire Article 31C unconstitutional and void", "SC முழு உறுப்பு 31C-யையும் அரசியலமைப்புக்கு முரணானது மற்றும் செல்லாதது என அறிவித்தது",
        "SC held that DPSP Article 44 takes precedence over Article 31C", "DPSP உறுப்பு 44 உறுப்பு 31C-ஐ விட மேலோங்குகிறது என SC கூறியது",
        "SC held that Article 31C applies only to foreign multinational corporations", "உறுப்பு 31C வெளிநாட்டு பன்னாட்டு நிறுவனங்களுக்கு மட்டுமே பொருந்தும் என SC கூறியது",
        "SC UPHELD the first part of Article 31C (giving priority to Art 39(b) & (c) over Arts 14 & 19), but struck down the second part excluding judicial review", "SC உறுப்பு 31C-ன் முதல் பகுதியை (உறுப்புகள் 14 & 19-ஐ விட 39(b) & (c)-க்கு முன்னுரிமை) உறுதி செய்தது, ஆனால் நீதித்துறை ஆய்வை விலக்கும் இரண்டாம் பகுதியை ரத்து செய்தது",
        "D",
        "In Kesavananda Bharati (1973), a 13-judge bench upheld the 1st part of Art 31C (laws implementing Art 39(b)/(c) cannot be declared void under Arts 14 or 19), but invalidated the 2nd part which stated 'no law containing such declaration shall be called in question in any court' because Judicial Review is a Basic Feature.",
        "கேசவானந்த பாரதி வழக்கில் (1973), 13-நீதிபதிகள் அமர்வு உறுப்பு 31C-ன் 1வது பகுதியை உறுதி செய்தது, ஆனால் 'எந்தவொரு நீதிமன்றத்திலும் இத்தகைய சட்டத்தைச் சவால் செய்ய முடியாது' என்ற 2வது பகுதியை ரத்து செய்தது, ஏனெனில் நீதித்துறை ஆய்வு ஒரு அடிப்படை அம்சமாகும்.",
        "This ruling firmly established that DPSP 39(b) and 39(c) can take priority over FRs 14 and 19 under judicial oversight.",
        "இத்தீர்ப்பு நீதித்துறை மேற்பார்வையின் கீழ் DPSP 39(b) மற்றும் 39(c) FR 14 மற்றும் 19-ஐ விட முன்னுரிமை பெறலாம் என்பதை உறுதியாக நிறுவியது.",
        "SC did not declare the entire Article 31C void; 1st part was upheld.", "SC முழு உறுப்பு 31C-யையும் செல்லாததாக அறிவிக்கவில்லை; 1வது பகுதி உறுதி செய்யப்பட்டது.",
        "Article 44 was not the subject of Article 31C.", "உறுப்பு 44 உறுப்பு 31C-ன் பொருளாக இருக்கவில்லை.",
        "Article 31C applies to socio-economic reform laws implementing 39(b)/(c).", "உறுப்பு 31C 39(b)/(c)-ஐ செயல்படுத்தும் சமூக-பொருளாதார சீர்திருத்தச் சட்டங்களுக்குப் பொருந்தும்.",
        "Correct. SC upheld 1st part of 31C (protecting 39b/c laws) and struck down 2nd part (barring judicial review).", "சரி. SC 31C-ன் 1வது பகுதியை உறுதி செய்தது மற்றும் 2வது பகுதியை ரத்து செய்தது."
    )

    # -------------------------------------------------------------------------
    # Q13 (Correct: A) - Application / Inference
    # -------------------------------------------------------------------------
    add_q(
        13, "Application",
        "Article 47 mandates both a POSITIVE duty and a NEGATIVE prohibition. Which pair correctly identifies these two aspects?",
        "உறுப்பு 47 ஒரு நேர்மறைக் கடமையையும் ஒரு எதிர்மறை மதுவிலக்கையும் ஒரே சேர ஆணையிடுகிறது. எந்தக் ஜோடி இந்த இரண்டு அம்சங்களையும் சரியாக அடையாளம் காட்டுகிறது?",
        "Positive: Raising nutrition, standard of living & public health; Negative: Prohibition of intoxicating drinks and health-injurious drugs", "நேர்மறை: சத்துணவு, வாழ்க்கை முறை & பொது சுகாதாரத்தை உயர்த்துதல்; எதிர்மறை: போதைப் பானங்கள் மற்றும் தீங்கு விளைவிக்கும் மருந்துகள் அருந்துவதை மதுவிலக்கு செய்தல்",
        "Positive: Building mega highways; Negative: Ban on foreign trade", "நேர்மறை: மெகா நெடுஞ்சாலைகளை அமைத்தல்; எதிர்மறை: வெளிநாட்டு வர்த்தகத் தடை",
        "Positive: Mandatory military conscription; Negative: Ban on newspapers", "நேர்மறை: கட்டாய இராணுவப் பயிற்சி; எதிர்மறை: செய்தித் தாள்கள் தடை",
        "Positive: Free housing for all; Negative: Prohibition of English language", "நேர்மறை: அனைவருக்கும் இலவச வீடு; எதிர்மறை: ஆங்கில மொழித் தடை",
        "A",
        "Article 47 has two distinct components: 1) Positive Duty (Socialist): State shall regard raising level of nutrition, standard of living, and improvement of public health as primary duties; 2) Negative Prohibition (Gandhian): State shall endeavor to bring about prohibition of intoxicating drinks and health-injurious drugs except for medicinal use.",
        "உறுப்பு 47 இரண்டு வெவ்வேறான அம்சங்களைக் கொண்டுள்ளது: 1) நேர்மறைக் கடமை (சமதர்மம்): சத்துணவு நிலை, வாழ்க்கை முறை மற்றும் பொது சுகாதாரத்தை உயர்த்துவது முதன்மைக் கடமை; 2) எதிர்மறை மதுவிலக்கு (காந்தியம்): மருத்துவ பயன்பாடு தவிர போதைப் பானங்கள் மற்றும் தீங்கு விளைவிக்கும் மருந்துகள் அருந்துவதை மதுவிலக்கு செய்ய முயலுதல்.",
        "Poshan Abhiyaan & Mid-Day Meals fulfill the positive duty; State Dry/Prohibition laws fulfill the negative prohibition.",
        "போஷன் அபியான் & காலை உணவுத் திட்டம் நேர்மறைக் கடமையை நிறைவேற்றுகின்றன; மாநில மதுவிலக்குச் சட்டங்கள் எதிர்மறை மதுவிலக்கை நிறைவேற்றுகின்றன.",
        "Correct. Positive is raising nutrition/health; Negative is prohibition of intoxicating drinks/drugs.", "சரி. நேர்மறை என்பது சத்துணவு/சுகாதாரத்தை உயர்த்துவது; எதிர்மறை என்பது போதைப் பானங்கள்/மருந்துகள் மதுவிலக்கு.",
        "Highways and foreign trade are not Article 47 directives.", "நெடுஞ்சாலைகள் மற்றும் வெளிநாட்டு வர்த்தகம் உறுப்பு 47 வழிகாட்டல்கள் அல்ல.",
        "Military conscription and press ban are not Article 47 directives.", "இராணுவப் பயிற்சி மற்றும் செய்தித் தாள் தடை உறுப்பு 47 வழிகாட்டல்கள் அல்ல.",
        "Housing and language policy are covered under other constitutional provisions.", "வீட்டுவசதி மற்றும் மொழிக் கொள்கை பிற அரசியலமைப்பு விதிகளின் கீழ் வருகின்றன."
    )

    # -------------------------------------------------------------------------
    # Q14 (Correct: B) - Simple Comparison
    # -------------------------------------------------------------------------
    add_q(
        14, "Comparison",
        "How does Article 46 (DPSP) relate conceptually to Article 15(4) and Article 16(4) (Fundamental Rights)?",
        "உறுப்பு 46 (DPSP) எவ்வாறு உறுப்பு 15(4) மற்றும் உறுப்பு 16(4) (அடிப்படை உரிமைகள்) ஆகியவற்றுடன் தத்துவார்த்த ரீதியாகத் தொடர்புடைதாக உள்ளது?",
        "Article 46 prohibits reservation in jobs, whereas Arts 15(4) and 16(4) mandate 100% reservation", "உறுப்பு 46 வேலைகளில் இடஒதுக்கீட்டைத் தடுக்கிறது, மாறாக 15(4) மற்றும் 16(4) 100% இடஒதுக்கீட்டைக் கட்டாயமாக்குகின்றன",
        "Article 46 serves as the overarching DPSP policy anchor directing special care for educational/economic interests of SCs/STs, while Arts 15(4) and 16(4) are justiciable FR exceptions empowering reservation laws", "உறுப்பு 46 எஸ்சி/எஸ்டிகளின் கல்வி/பொருளாதார நலன்களுக்கான சிறப்பு கவனத்திற்கு வழிகாட்டும் ஒட்டுமொத்த DPSP கொள்கை நங்கூரமாகச் செயல்படுகிறது, மாறாக 15(4) மற்றும் 16(4) இடஒதுக்கீட்டுச் சட்டங்களுக்கு அதிகாரமளிக்கும் அமல்படுத்தக்கூடிய FR விலக்குகள் ஆகும்",
        "Article 46 applies only to private companies, while Arts 15(4) and 16(4) apply only to foreign embassies", "உறுப்பு 46 தனியார் நிறுவனங்களுக்கு மட்டுமே பொருந்தும், மாறாக 15(4) மற்றும் 16(4) வெளிநாட்டுத் தூதரகங்களுக்கு மட்டுமே பொருந்தும்",
        "Article 46 was deleted by the 1st Amendment Act 1951", "உறுப்பு 46 1வது திருத்தச் சட்டம் 1951 மூலம் நீக்கப்பட்டது",
        "B",
        "Article 46 (DPSP) mandates that the State shall promote with special care the educational and economic interests of SCs, STs, and weaker sections. This DPSP policy goal provides the constitutional justification for statutory reservation provisions enacted under Articles 15(4) (educational reservation) and 16(4) (employment reservation).",
        "உறுப்பு 46 (DPSP) எஸ்சி, எஸ்டி மற்றும் எளிய பிரிவினரின் கல்வி மற்றும் பொருளாதார நலன்களை சிறப்பு கவனத்துடன் மேம்படுத்த அரசுக்கு ஆணையிடுகிறது. இந்த DPSP கொள்கை இலக்கு உறுப்புகள் 15(4) (கல்வி இடஒதுக்கீடு) மற்றும் 16(4) (வேலைவாய்ப்பு இடஒதுக்கீடு) ஆகியவற்றுக்கு அரசியலமைப்பு நியாயப்படுத்துதலை வழங்குகிறது.",
        "In Champakam Dorairajan (1951), reservation G.O. under Art 46 was held invalid under Art 29(2), prompting 1st CAA 1951 inserting Art 15(4).",
        "செண்பகம் துரைராஜன் வழக்கில் (1951) உறுப்பு 46-ன் கீழ் உள்ள இடஒதுக்கீடு G.O. செல்லாததாக அறிவிக்கப்பட்டது, இது 1வது திருத்தம் 1951 உறுப்பு 15(4)-ஐ இணைக்கத் தூண்டியது.",
        "Article 46 supports affirmative action, not prohibits it.", "உறுப்பு 46 இடஒதுக்கீட்டை ஆதரிக்கிறதே தவிர, தடுக்கவில்லை.",
        "Correct. 46 is the DPSP policy anchor; 15(4)/16(4) are the justiciable FR reservation empowering clauses.", "சரி. 46 DPSP கொள்கை நங்கூரம்; 15(4)/16(4) அமல்படுத்தக்கூடிய FR இடஒதுக்கீட்டு அதிகாரப் பிரிவுகள்.",
        "Neither provision applies to foreign embassies.", "எந்தவொரு விதியும் வெளிநாட்டுத் தூதரகங்களுக்குப் பொருந்தாது.",
        "Article 46 was not deleted; it remains active in Part IV.", "உறுப்பு 46 நீக்கப்படவில்லை; இது பகுதி IV-ல் தொடர்ந்து செயல்படுகிறது."
    )

    # -------------------------------------------------------------------------
    # Q15 (Correct: C) - Simple Comparison
    # -------------------------------------------------------------------------
    add_q(
        15, "Comparison",
        "Compare the constitutional enforceability of Article 41 (Right to Education DPSP) and Article 21A (Right to Education FR).",
        "உறுப்பு 41 (கல்வி உரிமை DPSP) மற்றும் உறுப்பு 21A (கல்வி உரிமை FR) ஆகியவற்றின் அரசியலமைப்பு அமலாக்கத் தன்மையை ஒப்பிடுக.",
        "Both Article 41 and Article 21A are fully justiciable in Supreme Court under Article 32", "உறுப்பு 41 மற்றும் உறுப்பு 21A ஆகிய இரண்டும் உறுப்பு 32-ன் கீழ் உச்ச நீதிமன்றத்தில் முழுமையாக அமல்படுத்தக்கூடியவை",
        "Article 41 is a Fundamental Right, while Article 21A is a DPSP", "உறுப்பு 41 ஒரு அடிப்படை உரிமை, மாறாக உறுப்பு 21A ஒரு DPSP",
        "Article 41 is a non-justiciable DPSP directive dependent on State economic capacity covering all ages, whereas Article 21A is a justiciable FR guaranteeing free & compulsory education strictly for children aged 6 to 14 years", "உறுப்பு 41 என்பது அனைத்து வயதினருக்கும் பொருந்தும் அரசின் பொருளாதாரத் திறனைச் சார்ந்த அமல்படுத்த முடியாத DPSP வழிகாட்டுதல், மாறாக உறுப்பு 21A என்பது 6 முதல் 14 வயது வரையிலான குழந்தைகளுக்கு மட்டுமே இலவச & கட்டாயக் கல்வியை உத்தரவாதம் செய்யும் அமல்படுத்தக்கூடிய FR ஆகும்",
        "Neither Article 41 nor Article 21A relates to education", "உறுப்பு 41 அல்லது உறுப்பு 21A எதுவும் கல்வி பற்றியது அல்ல",
        "C",
        "Article 41 (DPSP) directs the State to secure right to education within limits of economic capacity across all age groups, but is non-justiciable. Article 21A (FR inserted by 86th CAA 2002) is a justiciable Fundamental Right guaranteeing free and compulsory education for children aged 6 to 14 years.",
        "உறுப்பு 41 (DPSP) அனைத்து வயதுக் குழுக்களுக்கும் பொருளாதாரத் திறனின் வரம்புகளுக்குள் கல்வி உரிமையை வழங்க வழிகாட்டுகிறது, ஆனால் அமல்படுத்த முடியாதது. உறுப்பு 21A (86வது திருத்தம் 2002 மூலம் இணைக்கப்பட்ட FR) 6 முதல் 14 வயது வரையிலான குழந்தைகளுக்கு இலவச மற்றும் கட்டாயக் கல்வியை உத்தரவாதம் செய்யும் அமல்படுத்தக்கூடிய அடிப்படை உரிமையாகும்.",
        "RTE Act 2009 gives statutory enforcement to Article 21A.", "RTE சட்டம் 2009 உறுப்பு 21A-க்கு சட்டப்பூர்வ அமலாக்கத்தை வழங்குகிறது.",
        "Article 41 is non-justiciable; only Article 21A is justiciable under Article 32.", "உறுப்பு 41 அமல்படுத்த முடியாதது; உறுப்பு 21A மட்டுமே உறுப்பு 32-ன் கீழ் அமல்படுத்தக்கூடியது.",
        "Incorrect reversal: 41 is DPSP; 21A is FR.", "தவறான தலைகீழ் கூற்று: 41 DPSP; 21A FR.",
        "Correct. 41 is non-justiciable DPSP (all ages, economic limit); 21A is justiciable FR (6-14 yrs).", "சரி. 41 அமல்படுத்த முடியாத DPSP (அனைத்து வயதும், பொருளாதார வரம்பு); 21A அமல்படுத்தக்கூடிய FR (6-14 ஆண்டுகள்).",
        "Both articles explicitly deal with education.", "இரண்டு உறுப்புகளும் வெளிப்படையாகக் கல்வி பற்றியவை."
    )

    # -------------------------------------------------------------------------
    # Q16 (Correct: D) - Provision-based
    # -------------------------------------------------------------------------
    add_q(
        16, "Article-based",
        "Distinguish the primary domain of Article 42 from that of Article 43.",
        "உறுப்பு 42-ன் முதன்மைக் களத்தை உறுப்பு 43-ன் களத்திலிருந்து வேறுடுத்துக.",
        "Article 42 deals with international law; Article 43 deals with army weapons", "உறுப்பு 42 சர்வதேச சட்டம் பற்றியது; உறுப்பு 43 இராணுவ ஆயுதங்கள் பற்றியது",
        "Article 42 deals with cow slaughter ban; Article 43 deals with Uniform Civil Code", "உறுப்பு 42 பசு வதை தடை பற்றியது; உறுப்பு 43 பொது சிவில் சட்டம் பற்றியது",
        "Article 42 deals with Panchayats; Article 43 deals with National Monuments", "உறுப்பு 42 பஞ்சாயத்துகள் பற்றியது; உறுப்பு 43 தேசிய நினைவிடங்கள் பற்றியது",
        "Article 42 focuses on workplace environment (just & humane conditions) and maternity relief; Article 43 focuses on remuneration (living wage), decent standard of life, leisure, and rural cottage industries", "உறுப்பு 42 பணியிடச் சூழல் (நியாயமான & மனிதத்தன்மை நிலைமைகள்) மற்றும் பேறுகால உதவி மீது கவனம் செலுத்துகிறது; உறுப்பு 43 ஊதியம் (வாழ்வாதார ஊதியம்), கண்ணியமான வாழ்க்கை முறை, ஓய்வு மற்றும் கிராமப்புறக் குடில்தொழில்கள் மீது கவனம் செலுத்துகிறது",
        "D",
        "Article 42 regulates workplace working environment (safety, sanitation, working hours) and maternity relief. Article 43 regulates remuneration levels (living wage), quality of life, leisure, and rural cottage industries.",
        "உறுப்பு 42 பணியிட வேலைச் சூழல் (பாதுகாப்பு, சுகாதாரம், வேலை நேரம்) மற்றும் பேறுகால உதவியைக் கட்டுப்படுத்துகிறது. உறுப்பு 43 ஊதிய நிலைகள் (வாழ்வாதார ஊதியம்), வாழ்க்கை தரம், ஓய்வு மற்றும் கிராமப்புறக் குடில்தொழில்களைக் கட்டுப்படுத்துகிறது.",
        "Maternity Benefit Act 1961 relates to Art 42; Minimum Wages Act 1948 and KVIC relate to Art 43.",
        "பேறுகால நலச் சட்டம் 1961 உறுப்பு 42-க்கு உரியது; குறைந்தபட்ச ஊதியச் சட்டம் 1948 மற்றும் KVIC உறுப்பு 43-க்கு உரியவை.",
        "Neither deals with international law or army weapons.", "எதுவும் சர்வதேச சட்டம் அல்லது இராணுவ ஆயுதங்கள் பற்றியது அல்ல.",
        "Cow slaughter ban is Art 48; UCC is Art 44.", "பசு வதை தடை உறுப்பு 48; UCC உறுப்பு 44.",
        "Panchayats is Art 40; Monuments is Art 49.", "பஞ்சாயத்துகள் உறுப்பு 40; நினைவிடங்கள் உறுப்பு 49.",
        "Correct. Article 42 covers workplace environment & maternity relief; Article 43 covers living wage, leisure & cottage industries.", "சரி. உறுப்பு 42 பணியிடச் சூழல் & பேறுகால உதவியையும்; உறுப்பு 43 வாழ்வாதார ஊதியம், ஓய்வு & குடில்தொழில்களையும் உள்ளடக்கியது."
    )

    # -------------------------------------------------------------------------
    # Q17 (Correct: A) - Amendment / Provision
    # -------------------------------------------------------------------------
    add_q(
        17, "Article-based",
        "Compare the constitutional origin and specific scope of Article 43A and Article 43B.",
        "உறுப்பு 43A மற்றும் உறுப்பு 43B ஆகியவற்றின் அரசியலமைப்புத் தோற்றம் மற்றும் குறிப்பிட்ட எல்லையை ஒப்பிடுக.",
        "Article 43A (42nd CAA 1976) deals with workers' participation in management of industrial undertakings; Article 43B (97th CAA 2011) deals with voluntary formation and autonomous functioning of Co-operative Societies", "உறுப்பு 43A (42வது திருத்தம் 1976) தொழிற்சாலைகள் மேலாண்மையில் தொழிலாளர்களின் பங்கேற்பைப் பற்றியது; உறுப்பு 43B (97வது திருத்தம் 2011) கூட்டுறவுச் சங்கங்களின் தன்னார்வ உருவாக்கம் மற்றும் தன்னாட்சி செயல்பாட்டைப் பற்றியது",
        "Article 43A deals with Panchayats; Article 43B deals with Municipalities", "உறுப்பு 43A பஞ்சாயத்துகள் பற்றியது; உறுப்பு 43B நகராட்சிகள் பற்றியது",
        "Article 43A was inserted in 1950; Article 43B was inserted by the 44th Amendment in 1978", "உறுப்பு 43A 1950-ல் இணைக்கப்பட்டது; உறுப்பு 43B 1978-ன் 44வது திருத்தத்தால் இணைக்கப்பட்டது",
        "Article 43A applies to civil servants; Article 43B applies to Supreme Court judges", "உறுப்பு 43A அரசு ஊழியர்களுக்குப் பொருந்தும்; உறுப்பு 43B உச்ச நீதிமன்ற நீதிபதிகளுக்குப் பொருந்தும்",
        "A",
        "Article 43A was added by the 42nd Constitutional Amendment Act 1976 directing steps to secure participation of workers in management of industries. Article 43B was added by the 97th Constitutional Amendment Act 2011 directing promotion of voluntary formation and autonomous functioning of co-operative societies.",
        "உறுப்பு 43A 1976-ன் 42வது அரசியலமைப்பு திருத்தச் சட்டத்தால் தொழிலாளர்கள் தொழிற்துறை மேலாண்மையில் பங்கேற்பதை உறுதி செய்யச் சேர்க்கப்பட்டது. உறுப்பு 43B 2011-ன் 97வது அரசியலமைப்பு திருத்தச் சட்டத்தால் கூட்டுறவுச் சங்கங்களின் தன்னார்வ உருவாக்கத்தை மேம்படுத்தச் சேர்க்கப்பட்டது.",
        "Both 43A and 43B are post-1950 amendment additions to Part IV.", "43A மற்றும் 43B ஆகிய இரண்டும் 1950-க்குப் பின் திருத்தங்கள் மூலம் பகுதி IV-ல் சேர்க்கப்பட்டவை ஆகும்.",
        "Correct. 43A (42nd CAA 1976) is Worker Participation in Management; 43B (97th CAA 2011) is Co-operative Societies.", "சரி. 43A (42வது திருத்தம் 1976) மேலாண்மையில் தொழிலாளர் பங்கேற்பு; 43B (97வது திருத்தம் 2011) கூட்டுறவுச் சங்கங்கள்.",
        "Panchayats is Art 40/Part IX; Municipalities is Part IX-A.", "பஞ்சாயத்துகள் உறுப்பு 40/பகுதி IX; நகராட்சிகள் பகுதி IX-A.",
        "Neither was in original 1950 text; 43B was added in 2011, not 1978.", "எதுவும் அசல் 1950 உரையில் இல்லை; 43B 2011-ல் சேர்க்கப்பட்டது, 1978-ல் அல்ல.",
        "Neither is restricted to civil servants or judges.", "எதுவும் அரசு ஊழியர்கள் அல்லது நீதிபதிகளுக்கு சுருங்கவில்லை."
    )

    # -------------------------------------------------------------------------
    # Q18 (Correct: B) - Application / Inference
    # -------------------------------------------------------------------------
    add_q(
        18, "Application",
        "How does Article 51 (Foreign Policy DPSP) operate alongside Article 253 of the Constitution?",
        "உறுப்பு 51 (வெளியுறவுக் கொள்கை DPSP) எவ்வாறு அரசியலமைப்பின் உறுப்பு 253 உடன் இணைந்து செயல்படுகிறது?",
        "Article 51 allows state Chief Ministers to sign international treaties independently of Article 253", "உறுப்பு 51 மாநில முதலமைச்சர்கள் உறுப்பு 253-க்கு சுயாதீனமாக பன்னாட்டு ஒப்பந்தங்களில் கையெழுத்திட அனுமதிக்கிறது",
        "Article 51 provides the policy directive to foster respect for international law and treaties, whereas Article 253 grants exclusive power to Parliament to enact legislation implementing international treaties into domestic law", "உறுப்பு 51 சர்வதேச சட்டம் மற்றும் ஒப்பந்தங்களுக்கு மரியாதையை வளர்க்கும் கொள்கை வழிகாட்டலை வழங்குகிறது, மாறாக உறுப்பு 253 பன்னாட்டு ஒப்பந்தங்களை உள்நாட்டுச் சட்டமாக அமல்படுத்தச் சட்டங்களை இயற்ற நாடாளுமன்றத்திற்கு மட்டுமே பிரத்யேக அதிகாரத்தை வழங்குகிறது",
        "Article 51 makes all international treaties automatically enforceable without any law under Article 253", "உறுப்பு 51 உறுப்பு 253-ன் கீழ் எந்தச் சட்டமும் இல்லாமல் அனைத்து பன்னாட்டு ஒப்பந்தங்களையும் தானாகவே அமல்படுத்தக்கூடியதாக மாற்றுகிறது",
        "Article 253 overrides Article 51 and bans India from joining the United Nations", "உறுப்பு 253 உறுப்பு 51-ஐ மிஞ்சி, இந்தியா ஐக்கிய நாடுகள் சபையில் சேர்வதைத் தடுக்கிறது",
        "B",
        "Article 51 (Part IV DPSP) guides State policy towards international peace, honourable relations, and respect for international law. Article 253 (Part XI) empowers Parliament exclusively to make any law for the whole or any part of India for implementing any treaty, agreement, or convention.",
        "உறுப்பு 51 (பகுதி IV DPSP) சர்வதேச அமைதி, கெளரவமான உறவுகள் மற்றும் சர்வதேச சட்டத்திற்கான மரியாதையை நோக்கிய அரசின் கொள்கையை வழிகாட்டுகிறது. உறுப்பு 253 (பகுதி XI) எந்தவொரு ஒப்பந்தத்தையும் அமல்படுத்துவதற்காக இந்தியா முழுமைக்கும் அல்லது எந்தப் பகுதிக்கும் சட்டம் இயற்ற நாடாளுமன்றத்திற்கு மட்டுமே பிரத்யேக அதிகாரமளிக்கிறது.",
        "India follows a Dualist model: Treaties require Parliamentary legislation under Article 253 to bind domestic courts.",
        "இந்தியா ஒரு இருத்துவ மாதிரியைப் பின்பற்றுகிறது: ஒப்பந்தங்கள் உள்நாட்டு நீதிமன்றங்களைக் கட்டுப்படுத்த உறுப்பு 253-ன் கீழ் நாடாளுமன்றச் சட்டம் தேவைப்படுகிறது.",
        "State Chief Ministers have no treaty-making powers under Union List Entry 14.", "ஒன்றியப் பட்டியலின் பிரிவு 14-ன் கீழ் மாநில முதலமைச்சர்களுக்கு ஒப்பந்தம் செய்யும் அதிகாரம் இல்லை.",
        "Correct. 51 is the policy directive; 253 is Parliament's legislative power to implement treaties.", "சரி. 51 என்பது கொள்கை வழிகாட்டல்; 253 என்பது ஒப்பந்தங்களை அமல்படுத்துவதற்கான நாடாளுமன்றத்தின் சட்ட அதிகாரம்.",
        "Treaties are not self-executing in domestic courts without Article 253 legislation.", "உறுப்பு 253 சட்டம் இல்லாமல் ஒப்பந்தங்கள் உள்நாட்டு நீதிமன்றங்களில் தானாகவே செயல்படுபவை அல்ல.",
        "Article 253 enables international treaty execution; it does not ban UN membership.", "உறுப்பு 253 சர்வதேச ஒப்பந்த அமலாக்கத்தை சாத்தியமாக்குகிறது; இது ஐ.நா உறுப்பினர் உரிமையைத் தடுக்கவில்லை."
    )

    # -------------------------------------------------------------------------
    # Q19 (Correct: C) - Simple Comparison
    # -------------------------------------------------------------------------
    add_q(
        19, "Comparison",
        "Distinguish between Article 49 (Monuments Protection) and Article 48A (Environment Protection) in Part IV.",
        "பகுதி IV-ல் உள்ள உறுப்பு 49 (நினைவிடங்கள் பாதுகாப்பு) மற்றும் உறுப்பு 48A (சுற்றுச்சூழல் பாதுகாப்பு) ஆகியவற்றை வேறுபடுத்துக.",
        "Article 49 was added by 42nd Amendment; Article 48A was in original 1950 text", "உறுப்பு 49 42வது திருத்தத்தால் சேர்க்கப்பட்டது; உறுப்பு 48A அசல் 1950 உரையில் இருந்தது",
        "Article 49 deals with agriculture; Article 48A deals with Panchayats", "உறுப்பு 49 விவசாயம் பற்றியது; உறுப்பு 48A பஞ்சாயத்துகள் பற்றியது",
        "Article 49 directs protection of man-made monuments, places and historical objects declared of national importance by Parliament; Article 48A (added by 42nd CAA 1976) directs protection of natural environment, forests and wildlife", "உறுப்பு 49 நாடாளுமன்றத்தால் தேசிய முக்கியத்துவம் வாய்ந்தது என அறிவிக்கப்பட்ட மனிதனால் உருவாக்கப்பட்ட நினைவிடங்கள், இடங்கள் மற்றும் வரலாற்றுப் பொருட்களைப் பாதுகாக்க வழிகாட்டுகிறது; உறுப்பு 48A (42வது திருத்தம் 1976 மூலம் சேர்க்கப்பட்டது) இயற்கைச் சூழல், காடுகள் மற்றும் வனவிலங்குகளைப் பாதுகாக்க வழிகாட்டுகிறது",
        "Article 49 is justiciable; Article 48A is non-justiciable", "உறுப்பு 49 அமல்படுத்தக்கூடியது; உறுப்பு 48A அமல்படுத்த முடியாதது",
        "C",
        "Article 49 focuses on man-made cultural/historical heritage (monuments, places, artistic objects declared by Parliament). Article 48A (inserted by 42nd CAA 1976) focuses on natural environmental heritage (environment, forests, wildlife).",
        "உறுப்பு 49 மனிதனால் உருவாக்கப்பட்ட பண்பாட்டு/வரலாற்றுப் பாரம்பரியத்தில் (நாடாளுமன்றத்தால் அறிவிக்கப்பட்ட நினைவிடங்கள், இடங்கள், கலைப் பொருட்கள்) கவனம் செலுத்துகிறது. உறுப்பு 48A (42வது திருத்தம் 1976 மூலம் இணைக்கப்பட்டது) இயற்கை சுற்றுச்சூழல் பாரம்பரியத்தில் (சுற்றுச்சூழல், காடுகள், வனவிலங்குகள்) கவனம் செலுத்துகிறது.",
        "AMASR Act 1958 implements Article 49; Wildlife Protection Act 1972 & Forest Conservation Act 1980 implement Article 48A.",
        "1958 AMASR சட்டம் உறுப்பு 49-ஐ செயல்படுத்துகிறது; 1972 வனவிலங்கு பாதுகாப்புச் சட்டம் & 1980 வனப் பாதுகாப்புச் சட்டம் உறுப்பு 48A-ஐ செயல்படுத்துகின்றன.",
        "Incorrect reversal: Art 49 was in original 1950 text; Art 48A was added by 42nd Amendment in 1976.", "தவறான தலைகீழ் கூற்று: உறுப்பு 49 அசல் 1950 உரையில் இருந்தது; உறுப்பு 48A 1976-ன் 42வது திருத்தத்தால் சேர்க்கப்பட்டது.",
        "Article 49 deals with monuments; Article 48A deals with environment.", "உறுப்பு 49 நினைவிடங்கள் பற்றியது; உறுப்பு 48A சுற்றுச்சூழல் பற்றியது.",
        "Correct. 49 is man-made national monuments protection; 48A is natural environment/wildlife protection.", "சரி. 49 மனிதனால் உருவாக்கப்பட்ட தேசிய நினைவிடங்கள் பாதுகாப்பு; 48A இயற்கை சுற்றுச்சூழல்/வனவிலங்கு பாதுகாப்பு.",
        "Both Articles 49 and 48A are non-justiciable DPSPs in Part IV.", "உறுப்புகள் 49 மற்றும் 48A ஆகிய இரண்டும் பகுதி IV-ல் உள்ள அமல்படுத்த முடியாத DPSP-கள் ஆகும்."
    )

    # -------------------------------------------------------------------------
    # Q20 (Correct: D) - Conceptual Distinction
    # -------------------------------------------------------------------------
    add_q(
        20, "Conceptual",
        "Which of the following Articles under Part IV contains a directive that combines BOTH Socialist principles (raising level of nutrition and public health) AND Gandhian principles (prohibition of intoxicating drinks)?",
        "பகுதி IV-ன் கீழ் உள்ள பின்வரும் உறுப்புகளில் எது சமதர்மக் கோட்பாடுகள் (சத்துணவு நிலை மற்றும் பொது சுகாதாரத்தை உயர்த்துதல்) மற்றும் காந்தியக் கோட்பாடுகள் (போதைப் பானங்கள் மதுவிலக்கு) ஆகிய இரண்டையும் ஒன்றாகக் கொண்டுள்ளது?",
        "Article 40", "உறுப்பு 40",
        "Article 44", "உறுப்பு 44",
        "Article 45", "உறுப்பு 45",
        "Article 47", "உறுப்பு 47",
        "D",
        "Article 47 has a dual character: 1) Raising level of nutrition and standard of living and improving public health (Socialist Principle); 2) Endeavoring prohibition of intoxicating drinks and health-injurious drugs (Gandhian Principle).",
        "உறுப்பு 47 இரட்டை இயல்பைக் கொண்டுள்ளது: 1) சத்துணவு நிலை, வாழ்க்கை முறை மற்றும் பொது சுகாதாரத்தை உயர்த்துதல் (சமதர்மக் கோட்பாடு); 2) போதைப் பானங்கள் மற்றும் தீங்கு விளைவிக்கும் மருந்துகள் அருந்துவதை மதுவிலக்கு செய்ய முயலுதல் (காந்தியக் கோட்பாடு).",
        "Similarly, Article 43 contains Socialist (living wage/leisure) and Gandhian (rural cottage industry) principles.",
        "அதேபோல உறுப்பு 43 சமதர்ம (வாழ்வாதார ஊதியம்/ஓய்வு) மற்றும் காந்திய (கிராமப்புறக் குடில்தொழில்) கோட்பாடுகளைக் கொண்டுள்ளது.",
        "Article 40 is purely Gandhian (Village Panchayats).", "உறுப்பு 40 முற்றிலும் காந்தியம் (கிராம ஊராட்சிகள்).",
        "Article 44 is Liberal-Intellectual (Uniform Civil Code).", "உறுப்பு 44 தாராளமய-அறிவுசார் (பொது சிவில் சட்டம்).",
        "Article 45 is Liberal-Intellectual (Early childhood education).", "உறுப்பு 45 தாராளமய-அறிவுசார் (முன்பருவக் கல்வி).",
        "Correct. Article 47 combines Socialist (nutrition/health) and Gandhian (prohibition) directives.", "சரி. உறுப்பு 47 சமதர்ம (சத்துணவு/சுகாதாரம்) மற்றும் காந்திய (மதுவிலக்கு) வழிகாட்டல்களை ஒருங்கிணைக்கிறது."
    )

    # -------------------------------------------------------------------------
    # Q21 (Correct: A) - Case-based
    # -------------------------------------------------------------------------
    add_q(
        21, "Amendment/Case",
        "Trace the historical sequence of Supreme Court decisions regarding the hierarchy between Fundamental Rights and Directive Principles:",
        "அடிப்படை உரிமைகள் மற்றும் வழிகாட்டு நெறிமுறைகளுக்கு இடையிலான படிநிலை பற்றிய உச்ச நீதிமன்றத் தீர்ப்புகளின் வரலாற்றுச் வரிசையைக் கண்டறிக:",
        "Champakam Dorairajan (1951) -> Re Kerala Education Bill (1958) -> Kesavananda Bharati (1973) -> Minerva Mills (1980)", "செண்பகம் துரைராஜன் (1951) -> கேரளா கல்வி மசோதா (1958) -> கேசவானந்த பாரதி (1973) -> மினர்வா மில்ஸ் (1980)",
        "Minerva Mills (1980) -> Kesavananda Bharati (1973) -> Champakam Dorairajan (1951) -> Re Kerala Education Bill (1958)", "மினர்வா மில்ஸ் (1980) -> கேசவானந்த பாரதி (1973) -> செண்பகம் துரைராஜன் (1951) -> கேரளா கல்வி மசோதா (1958)",
        "Kesavananda Bharati (1973) -> Champakam Dorairajan (1951) -> Minerva Mills (1980) -> Re Kerala Education Bill (1958)", "கேசவானந்த பாரதி (1973) -> செண்பகம் துரைராஜன் (1951) -> மினர்வா மில்ஸ் (1980) -> கேரளா கல்வி மசோதா (1958)",
        "Re Kerala Education Bill (1958) -> Minerva Mills (1980) -> Champakam Dorairajan (1951) -> Kesavananda Bharati (1973)", "கேரளா கல்வி மசோதா (1958) -> மினர்வா மில்ஸ் (1980) -> செண்பகம் துரைராஜன் (1951) -> கேசவானந்த பாரதி (1973)",
        "A",
        "The chronological evolution of FR vs DPSP hierarchy: 1) Champakam Dorairajan (1951 - FR superior); 2) Re Kerala Education Bill (1958 - Harmonious Construction); 3) Kesavananda Bharati (1973 - Art 31C part 1 valid); 4) Minerva Mills (1980 - Harmony & Balance is Basic Feature).",
        "FR vs DPSP படிநிலையின் காலவரிசை வளர்ச்சி: 1) செண்பகம் துரைராஜன் (1951 - FR மேலானது); 2) கேரளா கல்வி மசோதா (1958 - இணக்கமான விளக்கம்); 3) கேசவானந்த பாரதி (1973 - உறுப்பு 31C பகுதி 1 செல்லுபடியாகும்); 4) மினர்வா மில்ஸ் (1980 - இணக்கம் & சமநிலையே அடிப்படை அம்சம்).",
        "Chronology mnemonic: Champakam (51) -> Kerala Ed (58) -> Kesavananda (73) -> Minerva (80).",
        "காலவரிசை நினைவுக் குறிப்பு: செண்பகம் (51) -> கேரளா கல்வி (58) -> கேசவானந்த (73) -> மினர்வா (80).",
        "Correct. Sequential timeline is 1951 -> 1958 -> 1973 -> 1980.", "சரி. காலவரிசை காலக்கோடு 1951 -> 1958 -> 1973 -> 1980.",
        "Minerva Mills was 1980, not first.", "மினர்வா மில்ஸ் 1980, முதன்மையானது அல்ல.",
        "Kesavananda was 1973, after Champakam 1951.", "கேசவானந்த 1973, செண்பகம் 1951-க்கு பின்பு.",
        "Re Kerala Education Bill was 1958, after Champakam 1951.", "கேரளா கல்வி மசோதா 1958, செண்பகம் 1951-க்கு பின்பு."
    )

    # -------------------------------------------------------------------------
    # Q22 (Correct: B) - Application / Inference
    # -------------------------------------------------------------------------
    add_q(
        22, "Application",
        "In Randhir Singh v. Union of India (1982), how did the Supreme Court enforce Article 39(d) 'Equal Pay for Equal Work' despite DPSP being non-justiciable?",
        "ரந்தீர் சிங் வழக்கில் (1982), DPSP அமல்படுத்த முடியாததாக இருந்தபோதிலும், உச்ச நீதிமன்றம் உறுப்பு 39(d) 'சம வேலைக்கு சம ஊதியத்தை' எவ்வாறு அமல்படுத்தியது?",
        "By declaring Article 39(d) to be a Fundamental Duty under Article 51A", "உறுப்பு 39(d)-ஐ உறுப்பு 51A-ன் கீழ் உள்ள அடிப்படைக் கடமையாக அறிவிப்பதன் மூலம்",
        "By reading Article 39(d) together with Article 14 (Equality before Law) and Article 16 (Equality of Opportunity in Public Employment), making it an enforceable constitutional goal in public service", "உறுப்பு 39(d)-ஐ உறுப்பு 14 (சட்டத்தின் முன் சமத்துவம்) மற்றும் உறுப்பு 16 (பொதுப்பணியில் சம வாய்ப்பு) ஆகியவற்றுடன் சேர்த்து வாசித்து, பொதுப்பணியில் அமல்படுத்தக்கூடிய அரசியலமைப்பு இலக்காக மாற்றுவதன் மூலம்",
        "By creating a new constitutional amendment in court", "நீதிமன்றத்தில் ஒரு புதிய அரசியலமைப்பு திருத்தத்தை உருவாக்குவதன் மூலம்",
        "By abolishing all private sector employment contracts nationwide", "நாடு தழுவிய அனைத்துத் தனியார் துறை வேலைவாய்ப்பு ஒப்பந்தங்களையும் ஒழிப்பதன் மூலம்",
        "B",
        "The SC held that 'Equal Pay for Equal Work' is not an abstract doctrine but a constitutional goal. When read alongside Article 14 (Equality) and Article 16 (Equal Opportunity), non-arbitrary pay scales must be applied to employees performing identical work duties in public service.",
        "சம வேலைக்கு சம ஊதியம் என்பது வெறும் கற்பனைக் கோட்பாடு அல்ல, ஒரு அரசியலமைப்பு இலக்காகும் என SC தீர்ப்பளித்தது. உறுப்பு 14 (சமத்துவம்) மற்றும் உறுப்பு 16 (சம வாய்ப்பு) ஆகியவற்றுடன் சேர்த்து வாசிக்கப்படும் போது, பொதுப்பணியில் ஒரே மாதிரியான வேலைகளைச் செய்யும் ஊழியர்களுக்குத் தன்னிச்சையற்ற ஊதிய விகிதங்கள் பயன்படுத்தப்பட வேண்டும்.",
        "Equal Remuneration Act 1976 statutorily supports Article 39(d).", "சம ஊதியச் சட்டம் 1976 உறுப்பு 39(d)-க்கு சட்டப்பூர்வ ஆதரவை வழங்குகிறது.",
        "Article 39(d) is a Part IV DPSP, not a Part IV-A Fundamental Duty.", "உறுப்பு 39(d) பகுதி IV DPSP, பகுதி IV-A அடிப்படைக் கடமை அல்ல.",
        "Correct. SC read Article 39(d) in light of Articles 14 and 16 to enforce equal pay in public service.", "சரி. பொதுப்பணியில் சம ஊதியத்தை அமல்படுத்த SC உறுப்பு 39(d)-ஐ உறுப்புகள் 14 மற்றும் 16-ன் வெளிச்சத்தில் வாசித்தது.",
        "Judiciary cannot enact constitutional amendments.", "நீதித்துறை அரசியலமைப்பு திருத்தங்களை இயற்ற முடியாது.",
        "Randhir Singh applied to public service pay anomalies.", "ரந்தீர் சிங் வழக்கு பொதுப்பணி ஊதிய முரண்பாடுகளுக்குப் பொருந்தியது."
    )

    # -------------------------------------------------------------------------
    # Q23 (Correct: C) - Case-based
    # -------------------------------------------------------------------------
    add_q(
        23, "Amendment/Case",
        "In State of Gujarat v. Mirzapur Moti Kureshi Kassab Jamat (2005), a 7-judge Constitution Bench overruled earlier precedents and UPHELD total prohibition of cow progeny slaughter under Article 48 based on which economic reasoning?",
        "குஜராத் அரசு எதிர் மிர்சாபூர் மோதி குரேஷி வழக்கில் (2005), 7-நீதிபதிகள் அரசியலமைப்பு அமர்வு முந்தைய முன்னுதாரணங்களை மாற்றி, எந்த பொருளாதாரக் காரணத்தின் அடிப்படையில் உறுப்பு 48-ன் கீழ் பசு சந்ததிகள் வதை மீதான முழுத் தடையை உறுதி செய்தது?",
        "Because old cattle consume no food or water in rural areas", "ஏனெனில் கிராமப்புறங்களில் வயதான கால்நடைகள் உணவோ தண்ணீரோ உட்கொள்வதில்லை என்பதால்",
        "Because old cattle are exported to foreign countries for massive tax revenues", "ஏனெனில் வயதான கால்நடைகள் பெரும் வரி வருவாய்க்காக வெளிநாடுகளுக்கு ஏற்றுமதி செய்யப்படுகின்றன என்பதால்",
        "Because even old/unserviceable cattle continue to contribute to agriculture, bio-gas energy, and organic dung manure essential for rural economy", "ஏனெனில் வயதான/பயன்பாடற்ற கால்நடைகள் கூட கிராமப்புறப் பொருளாதாரத்திற்கு அத்தியாவசியமான விவசாயம், பயோ-கேஸ் ஆற்றல் மற்றும் இயற்கை எரு உரத்திற்குத் தொடர்ந்து பங்காற்றுகின்றன என்பதால்",
        "Because slaughterhouses were declared illegal under Article 21", "ஏனெனில் உறுப்பு 21-ன் கீழ் இறைச்சிக் கூடங்கள் சட்டவிரோதமானவையாக அறிவிக்கப்பட்டன என்பதால்",
        "C",
        "In Mirzapur Kureshi (2005), SC held that cattle progeny, even when old or unserviceable for draught, continue to yield dung and urine vital for organic farming, bio-mass energy, and soil fertility, making a total ban on cow progeny slaughter a valid reasonable restriction under Article 19(6) implementing Article 48.",
        "மிர்சாபூர் குரேஷி வழக்கில் (2005), பசு சந்ததிகள், பாரம் இழுக்க முடியாத வயதான காலத்திலும் கூட, இயற்கை விவசாயம், பயோ-மாஸ் ஆற்றல் மற்றும் மண் வளத்திற்கு அத்தியாவசியமான சாணம் மற்றும் சிறுநீரை வழங்குகின்றன, எனவே உறுப்பு 48-ஐ செயல்படுத்தும் பசு சந்ததிகள் வதை மீதான முழுத் தடை உறுப்பு 19(6)-ன் கீழ் நியாயமான கட்டுப்பாடாகும் என SC தீர்ப்பளித்தது.",
        "This judgment reversed the earlier Hanif Quareshi (1958) ruling which allowed slaughter of unserviceable cattle.",
        "இத்தீர்ப்பு பயன்பாடற்ற கால்நடைகளை வதை செய்ய அனுமதித்த முந்தைய ஹனிஃப் குரேஷி (1958) தீர்ப்பை மாற்றியமைத்தது.",
        "Old cattle do require fodder and water.", "வயதான கால்நடைகளுக்கும் தீவனமும் தண்ணீரும் தேவைப்படும்.",
        "Total slaughter ban prevents export for slaughter.", "முழு வதை தடை வதைக்காக ஏற்றுமதி செய்வதைத் தடுக்கிறது.",
        "Correct. SC highlighted ecological and organic manure value of old cattle progeny in rural economy.", "சரி. கிராமப் பொருளாதாரத்தில் வயதான பசு சந்ததிகளின் சுற்றுச்சூழல் மற்றும் இயற்கை உர மதிப்பினை SC முன்னிலைப்படுத்தியது.",
        "Slaughterhouses operating legally are not per se illegal under Art 21.", "சட்டப்பூர்வமாக இயங்கும் இறைச்சிக் கூடங்கள் உறுப்பு 21-ன் கீழ் சட்டவிரோதமானவை அல்ல."
    )

    # -------------------------------------------------------------------------
    # Q24 (Correct: D) - Simple Comparison
    # -------------------------------------------------------------------------
    add_q(
        24, "Comparison",
        "Compare Part IV (Directive Principles) with Part IV-A (Fundamental Duties) regarding their constitutional obligation.",
        "அவற்றின் அரசியலமைப்பு கடமை குறித்து பகுதி IV (வழிகாட்டு நெறிமுறைகள்) மற்றும் பகுதி IV-A (அடிப்படைக் கடமைகள்) ஆகியவற்றை ஒப்பிடுக.",
        "Part IV imposes duties on citizens, while Part IV-A imposes duties on the President of India", "பகுதி IV குடிமக்களுக்குக் கடமைகளை விதிக்கிறது, மாறாக பகுதி IV-A இந்தியக் குடியரசுத் தலைவருக்குக் கடமைகளை விதிக்கிறது",
        "Part IV is justiciable in High Courts, while Part IV-A is justiciable in District Courts", "பகுதி IV உயர் நீதிமன்றங்களில் அமல்படுத்தக்கூடியது, மாறாக பகுதி IV-A மாவட்ட நீதிமன்றங்களில் அமல்படுத்தக்கூடியது",
        "Part IV was enacted in 1976, while Part IV-A was enacted in 1950", "பகுதி IV 1976-ல் இயற்றப்பட்டது, மாறாக பகுதி IV-A 1950-ல் இயற்றப்பட்டது",
        "Part IV specifies positive governance directives addressed to the STATE, whereas Part IV-A specifies civic/moral duties addressed to EVERY CITIZEN of India", "பகுதி IV அரசுக்கு வழங்கப்பட்ட நேர்மறை ஆட்சி வழிகாட்டல்களைக் குறிப்பிடுகிறது, மாறாக பகுதி IV-A இந்தியாவின் ஒவ்வொரு குடிமகனுக்கும் வழங்கப்பட்ட சிவில்/ஒழுக்கக் கடமைகளைக் குறிப்பிடுகிறது",
        "D",
        "Part IV (DPSPs, Arts 36-51) contains positive socio-economic directives addressed to the STATE (Government/Legislatures). Part IV-A (Fundamental Duties, Art 51A inserted by 42nd CAA 1976) contains civic and moral duties addressed to EVERY CITIZEN.",
        "பகுதி IV (DPSP-கள், உறுப்புகள் 36-51) அரசுக்கு (அரசாங்கம்/சட்டமன்றங்கள்) வழங்கப்பட்ட நேர்மறை சமூக-பொருளாதார வழிகாட்டல்களைக் கொண்டுள்ளது. பகுதி IV-A (அடிப்படைக் கடமைகள், 42வது திருத்தம் 1976 மூலம் இணைக்கப்பட்ட உறுப்பு 51A) ஒவ்வொரு குடிமகனுக்கும் வழங்கப்பட்ட சிவில் மற்றும் ஒழுக்கக் கடமைகளைக் கொண்டுள்ளது.",
        "Both Part IV and Part IV-A are non-justiciable in courts unless enforced by specific statutory legislation.",
        "குறிப்பிட்ட சட்டப்பூர்வ சட்டங்களால் அமல்படுத்தப்படாவிட்டால் பகுதி IV மற்றும் பகுதி IV-A ஆகிய இரண்டும் நீதிமன்றங்களால் அமல்படுத்த முடியாதவை ஆகும்.",
        "Incorrect reversal: Part IV is for State; Part IV-A is for Citizens.", "தவறான தலைகீழ் கூற்று: பகுதி IV அரசுக்கானது; பகுதி IV-A குடிமக்களுக்கானது.",
        "Neither is directly justiciable in any court without statutory backing.", "சட்டப்பூர்வ ஆதரவு இல்லாமல் இரண்டும் எந்தவொரு நீதிமன்றத்திலும் நேரடியாக அமல்படுத்த முடியாதவை.",
        "Part IV was 1950 original text; Part IV-A was added by 42nd Amendment in 1976.", "பகுதி IV 1950 அசல் உரை; பகுதி IV-A 1976-ன் 42வது திருத்தத்தால் சேர்க்கப்பட்டது.",
        "Correct. Part IV is State Governance Directives; Part IV-A is Citizen Civic/Moral Duties.", "சரி. பகுதி IV அரசு ஆட்சி வழிகாட்டல்கள்; பகுதி IV-A குடிமகன் சிவில்/ஒழுக்கக் கடமைகள்."
    )

    # -------------------------------------------------------------------------
    # Q25 (Correct: A) - Conceptual Distinction
    # -------------------------------------------------------------------------
    add_q(
        25, "Conceptual",
        "Why does Article 36 incorporate the wide definition of 'State' from Article 12 for the purpose of Part IV?",
        "பகுதி IV-ன் நோக்கத்திற்காக உறுப்பு 36 ஏன் உறுப்பு 12-லிருந்து 'அரசு' என்ற பரந்த வரையறையை ஏற்கிறது?",
        "To ensure that all organs of government (Union, State, Local bodies, and statutory authorities) are bound to apply DPSP in law-making and policy", "அரசாங்கத்தின் அனைத்து அமைப்புகளும் (ஒன்றியம், மாநிலம், உள்ளாட்சி அமைப்புகள் மற்றும் சட்டப்பூர்வ அமைப்புகள்) சட்டம் இயற்றுவதிலும் கொள்கையிலும் DPSP-ஐப் பயன்படுத்தக் கட்டுப்படுத்தப்படுவதை உறுதி செய்ய",
        "To allow private corporations to claim immunity from state taxes", "தனியார் நிறுவனங்கள் மாநில வரிகளிலிருந்து விலக்குக் கோர அனுமதிக்க",
        "To restrict DPSP enforcement only to the Prime Minister's Office", "DPSP அமலாக்கத்தைப் பிரதமர் அலுவலகத்திற்கு மட்டுமே சுருக்க",
        "To make state assembly laws superior to constitutional provisions", "மாநில சட்டமன்றச் சட்டங்களை அரசியலமைப்பு விதிகளுக்கு மேலானதாக மாற்ற",
        "A",
        "By adopting Article 12 definition, Article 36 ensures that 'State' includes the Executive and Parliament of India, Executive and Legislatures of States, Panchayats, Municipalities, District Boards, and statutory authorities (LIC, ONGC, SAIL, etc.), making all public power authorities responsible for furthering DPSP goals.",
        "உறுப்பு 12 வரையறையை ஏற்பதன் மூலம், உறுப்பு 36 'அரசு' என்பதில் இந்திய நிர்வாகம் மற்றும் நாடாளுமன்றம், மாநில நிர்வாகம் மற்றும் சட்டமன்றங்கள், பஞ்சாயத்துகள், நகராட்சிகள், மாவட்ட வாரியங்கள் மற்றும் சட்டப்பூர்வ அமைப்புகள் (LIC, ONGC, SAIL போன்றவை) அடங்கும் என்பதை உறுதி செய்து, அனைத்து பொது அதிகார அமைப்புகளையும் DPSP இலக்குகளை முன்னெடுப்பதற்குப் பொறுப்பாக்குகிறது.",
        "Public authorities executing public functions are bound by Part IV guidelines.", "பொதுச் செயல்பாடுகளை நிறைவேற்றும் பொது அமைப்புகள் பகுதி IV வழிகாட்டுதல்களால் கட்டுப்படுத்தப்படுகின்றன.",
        "Correct. Article 36 binds all levels of government and statutory authorities to apply DPSPs.", "சரி. உறுப்பு 36 அனைத்து மட்ட அரசாங்கங்களையும் சட்டப்பூர்வ அமைப்புகளையும் DPSP-களைப் பயன்படுத்தக் கட்டுப்படுத்துகிறது.",
        "Private corporations are not 'State' unless performing public agency functions.", "பொது முகமைச் செயல்பாடுகளைச் செய்யாவிட்டால் தனியார் நிறுவனங்கள் 'அரசு' அல்ல.",
        "DPSP binds all public authorities, not just PMO.", "DPSP பிரதமர் அலுவலகத்தை மட்டும் அல்லாமல் அனைத்துப் பொது அமைப்புகளையும் கட்டுப்படுத்துகிறது.",
        "State assembly laws cannot violate constitutional limits.", "மாநில சட்டமன்றச் சட்டங்கள் அரசியலமைப்பு வரம்புகளை மீற முடியாது."
    )

    # -------------------------------------------------------------------------
    # Q26 (Correct: B) - Application / Inference
    # -------------------------------------------------------------------------
    add_q(
        26, "Application",
        "How did the Supreme Court link Article 39A (Free Legal Aid DPSP) with Article 21 (Right to Life) in Hussainara Khatoon v. Home Secretary, State of Bihar (1979)?",
        "ஹுசைனாரா கதூன் வழக்கில் (1979), உச்ச நீதிமன்றம் எவ்வாறு உறுப்பு 39A-ஐ (இலவச சட்ட உதவி DPSP) உறுப்பு 21-உடன் (வாழ்வு உரிமை) இணைத்தது?",
        "SC held that free legal aid can only be granted to foreign citizens", "இலவச சட்ட உதவி வெளிநாட்டு குடிமக்களுக்கு மட்டுமே வழங்கப்பட முடியும் என SC கூறியது",
        "SC held that 'Right to Free Legal Services' to poor undertrial prisoners is an essential ingredient of a 'reasonable, fair and just' procedure under Article 21, read in light of Article 39A", "உறுப்பு 39A-ன் வெளிச்சத்தில் வாசிக்கப்படும் போது, ஏழை விசாரணைக் கைதிகளுக்கு 'இலவச சட்ட சேவை உரிமை' என்பது உறுப்பு 21-ன் கீழ் 'நியாயமான, நேர்மையான' நடைமுறையின் அத்தியாவசிய அம்சம் என SC தீர்ப்பளித்தது",
        "SC declared that legal aid must be paid by private charitable trusts", "சட்ட உதவி தனியார் அறக்கட்டளைகளால் செலுத்தப்பட வேண்டும் என SC அறிவித்தது",
        "SC struck down Article 39A as an illegal burden on state treasury", "மாநில கருவூலத்திற்கு சட்டவிரோத சுமை எனக் கூறி உறுப்பு 39A-ஐ SC ரத்து செய்தது",
        "B",
        "In Hussainara Khatoon (1979) regarding thousands of poor undertrials languishing in Bihar jails, Justice P.N. Bhagwati held that procedure under Article 21 cannot be 'fair, just and reasonable' unless free legal services are provided to an accused who is unable to engage a lawyer due to poverty, drawing strength from Article 39A.",
        "பீகார் சிறைகளில் வாடும் ஆயிரக்கணக்கான ஏழை விசாரணைக் கைதிகள் தொடர்பான ஹுசைனாரா கதூன் வழக்கில் (1979), வறுமையின் காரணமாக வழக்கறிஞரை அமர்த்த முடியாத குற்றஞ்சாட்டப்பட்டவருக்கு இலவச சட்ட சேவைகள் வழங்கப்படாவிட்டால் உறுப்பு 21-ன் கீழ் நடைமுறை 'நேர்மையானதாக' இருக்க முடியாது என நீதிபதி பி.என். பகவதி தீர்ப்பளித்தார்.",
        "This ruling prompted Parliament to enact the Legal Services Authorities Act, 1987 (NALSA).",
        "இத்தீர்ப்பு நாடாளுமன்றம் 1987-ல் சட்டப் பணிகள் ஆணைக்குழுக்கள் சட்டத்தை (NALSA) இயற்றத் தூண்டியது.",
        "Free legal aid applies to all indigent accused citizens in India.", "இலவச சட்ட உதவி இந்தியாவில் உள்ள அனைத்து ஏழைக் குற்றஞ்சாட்டப்பட்ட குடிமக்களுக்கும் பொருந்தும்.",
        "Correct. SC read Article 39A into Article 21 to make Free Legal Aid an enforceable fundamental procedural right.", "சரி. இலவச சட்ட உதவியை அமல்படுத்தக்கூடிய அடிப்படை நடைமுறை உரிமையாக மாற்ற SC உறுப்பு 39A-ஐ உறுப்பு 21-க்குள் வாசித்தது.",
        "State has constitutional duty under Art 39A/21 to fund legal aid.", "சட்ட உதவிக்கு நிதியளிக்க அரசுக்கு உறுப்பு 39A/21-ன் கீழ் அரசியலமைப்பு கடமை உண்டு.",
        "SC upheld Article 39A; it did not strike it down.", "SC உறுப்பு 39A-ஐ உறுதி செய்தது; அதை ரத்து செய்யவில்லை."
    )

    # -------------------------------------------------------------------------
    # Q27 (Correct: C) - Conceptual Distinction
    # -------------------------------------------------------------------------
    add_q(
        27, "Conceptual",
        "What is the fundamental conceptual difference between a 'Police State' and a 'Welfare State' in constitutional philosophy?",
        "அரசியலமைப்புத் தத்துவத்தில் 'காவல் அரசு' (Police State) மற்றும் 'நல அரசு' (Welfare State) ஆகியவற்றுக்கு இடையேயான அடிப்படைத் தத்துவார்த்த வேறுபாடு என்ன?",
        "A Police State promotes social equality, while a Welfare State enforces military law", "காவல் அரசு சமூக சமத்துவத்தை மேம்படுத்துகிறது, மாறாக நல அரசு இராணுவச் சட்டத்தை அமல்படுத்துகிறது",
        "A Police State is governed by a written constitution, while a Welfare State has no laws", "காவல் அரசு எழுதப்பட்ட அரசியலமைப்பால் ஆளப்படுகிறது, மாறாக நல அரசுக்கு சட்டங்கள் இல்லை",
        "A Police State restricts its functions primarily to maintaining law, order, and defence (negative governance), whereas a Welfare State actively promotes socio-economic well-being, health, education, and livelihood for all (positive governance via DPSP)", "ஒரு காவல் அரசு தனது செயல்பாடுகளை முதன்மையாக சட்டம் ஒழுங்கு மற்றும் பாதுகாப்பைப் பேணுவதற்கு மட்டுமே சுருக்கிக் கொள்கிறது (எதிர்மறை ஆட்சி), மாறாக ஒரு நல அரசு அனைவருக்கும் சமூக-பொருளாதார நல்வாழ்வு, சுகாதாரம், கல்வி மற்றும் வாழ்வாதாரத்தை தீவிரமாக மேம்படுத்துகிறது (DPSP மூலமான நேர்மறை ஆட்சி)",
        "There is no difference between a Police State and a Welfare State", "காவல் அரசுக்கும் நல அரசுக்கும் இடையே எந்த வேறுபாடும் இல்லை",
        "C",
        "Colonial rule in India operated primarily as a Police State (focusing on tax collection and law enforcement). Part IV Directive Principles transformed India into a Welfare State where the State assumes positive responsibility for public health, nutrition, education, living wages, and social security.",
        "இந்தியாவில் காலனித்துவ ஆட்சி முதன்மையாக ஒரு காவல் அரசாகச் செயல்பட்டது (வரி வசூல் மற்றும் சட்டம் ஒழுங்கு மீது கவனம்). பகுதி IV வழிகாட்டு நெறிமுறைகள் இந்தியாவை ஒரு நல அரசாக மாற்றின, இதில் அரசு பொது சுகாதாரம், சத்துணவு, கல்வி, வாழ்வாதார ஊதியம் மற்றும் சமூகப் பாதுகாப்பிற்கு நேர்மறைப் பொறுப்பை ஏற்கிறது.",
        "Preamble and Part IV together outline the Welfare State framework.", "முகப்புரை மற்றும் பகுதி IV ஆகியவை இணைந்து நல அரசு கட்டமைப்பை விவரிக்கின்றன.",
        "Police State restricts functions; Welfare State actively promotes socio-economic welfare.", "காவல் அரசு செயல்பாடுகளைச் சுருக்குகிறது; நல அரசு சமூக-பொருளாதார நலனைத் தீவிரமாக மேம்படுத்துகிறது.",
        "Welfare State operates under the Rule of Law and written constitution.", "நல அரசு சட்டத்தின் ஆட்சி மற்றும் எழுதப்பட்ட அரசியலமைப்பின் கீழ் செயல்படுகிறது.",
        "Correct. Police State focuses on law & order; Welfare State actively promotes socio-economic well-being.", "சரி. காவல் அரசு சட்டம் ஒழுங்கில் கவனம் செலுத்துகிறது; நல அரசு சமூக-பொருளாதார நல்வாழ்வைத் தீவிரமாக மேம்படுத்துகிறது.",
        "Both models are distinct concepts in political theory.", "இரண்டு மாதிரிகளும் அரசியல் கோட்பாட்டில் வெவ்வேறான கருத்துக்கள் ஆகும்."
    )

    # -------------------------------------------------------------------------
    # Q28 (Correct: D) - Simple Comparison
    # -------------------------------------------------------------------------
    add_q(
        28, "Comparison",
        "Compare the functional scope of the 11th Schedule (Part IX / Art 40 Panchayats) with the 12th Schedule (Part IX-A Municipalities).",
        "11வது அட்டவணையின் (பகுதி IX / உறுப்பு 40 பஞ்சாயத்துகள்) செயல்பாட்டு எல்லையை 12வது அட்டவணையுடன் (பகுதி IX-A நகராட்சிகள்) ஒப்பிடுக.",
        "11th Schedule has 18 subjects for urban areas; 12th Schedule has 29 subjects for rural areas", "11வது அட்டவணை நகர்ப்புறங்களுக்கு 18 தலைப்புகளைக் கொண்டுள்ளது; 12வது அட்டவணை கிராமப்புறங்களுக்கு 29 தலைப்புகளைக் கொண்டுள்ளது",
        "11th Schedule applies only to Union Territories; 12th Schedule applies only to States", "11வது அட்டவணை யூனியன் பிரதேசங்களுக்கு மட்டுமே பொருந்தும்; 12வது அட்டவணை மாநிலங்களுக்கு மட்டுமே பொருந்தும்",
        "11th Schedule was added by 42nd Amendment; 12th Schedule was added by 44th Amendment", "11வது அட்டவணை 42வது திருத்தத்தால் சேர்க்கப்பட்டது; 12வது அட்டவணை 44வது திருத்தத்தால் சேர்க்கப்பட்டது",
        "11th Schedule (73rd CAA 1992) lists 29 functional subjects for rural Panchayats; 12th Schedule (74th CAA 1992) lists 18 functional subjects for urban Municipalities", "11வது அட்டவணை (73வது திருத்தம் 1992) கிராமப்புற பஞ்சாயத்துகளுக்கு 29 செயல்பாட்டுத் தலைப்புகளைப் பட்டியலிடுகிறது; 12வது அட்டவணை (74வது திருத்தம் 1992) நகர்ப்புற நகராட்சிகளுக்கு 18 செயல்பாட்டுத் தலைப்புகளைப் பட்டியலிடுகிறது",
        "D",
        "The 73rd Amendment Act 1992 inserted Part IX and the 11th Schedule containing 29 functional matters for rural local self-government (Panchayati Raj fulfilling Art 40). The 74th Amendment Act 1992 inserted Part IX-A and the 12th Schedule containing 18 functional matters for urban local self-government (Municipalities).",
        "1992-ன் 73வது திருத்தச் சட்டம் பகுதி IX மற்றும் 11வது அட்டவணையை இணைத்து கிராமப்புற உள்ளாட்சி சுயஆட்சிக்கு 29 செயல்பாட்டுத் தலைப்புகளை வழங்கியது (உறுப்பு 40-ஐ நிறைவேற்றும் பஞ்சாயத்து ராஜ்). 1992-ன் 74வது திருத்தச் சட்டம் பகுதி IX-A மற்றும் 12வது அட்டவணையை இணைத்து நகர்ப்புற உள்ளாட்சி சுயஆட்சிக்கு 18 செயல்பாட்டுத் தலைப்புகளை வழங்கியது (நகராட்சிகள்).",
        "Numbers to remember: 11th Schedule = 29 subjects (Panchayats); 12th Schedule = 18 subjects (Municipalities).",
        "நினைவில் கொள்ள வேண்டிய எண்கள்: 11வது அட்டவணை = 29 தலைப்புகள் (பஞ்சாயத்துகள்); 12வது அட்டவணை = 18 தலைப்புகள் (நகராட்சிகள்).",
        "Incorrect numbers: 11th has 29 subjects (rural); 12th has 18 subjects (urban).", "தவறான எண்கள்: 11வது 29 தலைப்புகளைக் கொண்டுள்ளது; 12வது 18 தலைப்புகளைக் கொண்டுள்ளது.",
        "Both schedules apply across States and UTs.", "இரண்டு அட்டவணைகளும் மாநிலங்கள் மற்றும் UT-கள் முழுவதும் பொருந்தும்.",
        "11th and 12th Schedules were added by 73rd and 74th Amendments in 1992.", "11வது மற்றும் 12வது அட்டவணைகள் 1992-ல் 73வது மற்றும் 74வது திருத்தங்களால் சேர்க்கப்பட்டன.",
        "Correct. 11th Schedule has 29 rural Panchayat subjects; 12th Schedule has 18 urban Municipality subjects.", "சரி. 11வது அட்டவணை 29 கிராமப் பஞ்சாயத்துத் தலைப்புகளைக் கொண்டுள்ளது; 12வது அட்டவணை 18 நகர்ப்புற நகராட்சித் தலைப்புகளைக் கொண்டுள்ளது."
    )

    # -------------------------------------------------------------------------
    # Q29 (Correct: A) - TNPSC Trap
    # -------------------------------------------------------------------------
    add_q(
        29, "TNPSC Trap",
        "If a citizen files a writ petition under Article 32 demanding that the Supreme Court issue a Writ of Mandamus directing Parliament to immediately pass a law enforcing Article 44 (Uniform Civil Code), how will the Supreme Court rule?",
        "உறுப்பு 44-ஐ (பொது சிவில் சட்டம்) உடனடியாக அமல்படுத்த நாடாளுமன்றத்திற்கு உத்தரவிட்டு செயலுறுத்தும் பேராணை (Mandamus) பிறப்பிக்குமாறு கோரி ஒரு குடிமகன் உறுப்பு 32-ன் கீழ் பேராணை மனு தாக்கல் செய்தால், உச்ச நீதிமன்றம் எவ்வாறு தீர்ப்பளிக்கும்?",
        "SC will dismiss the petition because Article 37 prohibits courts from issuing writs to compel Parliament to enact DPSP laws", "உறுப்பு 37 DPSP சட்டங்களை இயற்றுமாறு நாடாளுமன்றத்தைக் கட்டாயப்படுத்தி பேராணைகளைப் பிறப்பிப்பதைத் தடுப்பதால் SC மனுவைத் தள்ளுபடி செய்யும்",
        "SC will issue Mandamus and suspend Parliament until the law is passed", "SC செயலுறுத்தும் பேராணையைப் பிறப்பித்து சட்டம் இயற்றப்படும் வரை நாடாளுமன்றத்தை இடைநீக்கம் செய்யும்",
        "SC will automatically enact the Uniform Civil Code itself as a judicial decree", "SC பொது சிவில் சட்டத்தை நீதித்துறை ஆணையாகத் தானே தானாக இயற்றிவிடும்",
        "SC will refer the matter to the United Nations Security Council", "SC இந்த விஷயத்தை ஐக்கிய நாடுகள் பாதுகாப்புச் சபைக்குப் பரிந்துரைக்கும்",
        "A",
        "The Supreme Court (Maharishi Avadhesh v. Union of India 1994 & Pannalal Bansilal 1996) firmly held that court cannot issue a Writ of Mandamus to Parliament or State Legislatures directing them to enact legislation to implement DPSP under Part IV (such as Article 44 UCC), because law-making is within legislative wisdom and DPSPs are non-justiciable under Article 37.",
        "உறுப்பு 44 UCC போன்ற பகுதி IV DPSP-ஐ அமல்படுத்த சட்டம் இயற்றுமாறு நாடாளுமன்றத்திற்கு அல்லது மாநில சட்டமன்றங்களுக்கு செயலுறுத்தும் பேராணை பிறப்பிக்க முடியாது என உச்ச நீதிமன்றம் தீர்ப்பளித்தது, ஏனெனில் சட்டம் இயற்றுவது சட்டமன்ற விவேகத்திற்கு உட்பட்டது மற்றும் DPSP-கள் உறுப்பு 37-ன் கீழ் அமல்படுத்த முடியாதவை ஆகும்.",
        "TNPSC Trap: Courts can encourage or urge UCC enactment (Sarla Mudgal), but CANNOT issue a binding Mandamus to Parliament.",
        "டிஎன்பிஎஸ்சி பொறி: நீதிமன்றங்கள் UCC இயற்றுவதை ஊக்குவிக்கலாம், ஆனால் நாடாளுமன்றத்திற்கு கட்டாயப் பேராணையைப் பிறப்பிக்க முடியாது.",
        "Correct. Article 37 bars judicial writs compelling Parliament to enact DPSPs.", "சரி. DPSP-களை இயற்றுமாறு நாடாளுமன்றத்தைக் கட்டாயப்படுத்தும் நீதித்துறை பேராணைகளை உறுப்பு 37 தடுக்கிறது.",
        "Court cannot suspend Parliament.", "நீதிமன்றம் நாடாளுமன்றத்தை இடைநீக்கம் செய்ய முடியாது.",
        "Judiciary cannot enact legislation.", "நீதித்துறை சட்டங்களை இயற்ற முடியாது.",
        "Domestic DPSP implementation is an internal constitutional matter, not a UN matter.", "உள்நாட்டு DPSP அமலாக்கம் என்பது உள்நாட்டு அரசியலமைப்பு விவகாரம், ஐ.நா விவகாரம் அல்ல."
    )

    # -------------------------------------------------------------------------
    # Q30 (Correct: B) - Simple Comparison
    # -------------------------------------------------------------------------
    add_q(
        30, "Comparison",
        "Compare Article 39(e) (DPSP) with Article 24 (Fundamental Right) regarding child welfare.",
        "குழந்தை நலன் குறித்து உறுப்பு 39(e) (DPSP) மற்றும் உறுப்பு 24 (அடிப்படை உரிமை) ஆகியவற்றை ஒப்பிடுக.",
        "Article 39(e) applies to adults only; Article 24 applies to animals", "உறுப்பு 39(e) பெரியவர்களுக்கு மட்டுமே பொருந்தும்; உறுப்பு 24 விலங்குகளுக்குப் பொருந்தும்",
        "Article 39(e) is a non-justiciable DPSP directing protection of tender age of children against economic abuse; Article 24 is a justiciable FR strictly prohibiting employment of children below 14 years in hazardous factories/mines", "உறுப்பு 39(e) என்பது பொருளாதாரத் துஷ்பிரயோகத்திலிருந்து குழந்தைகளின் இளம் வயதைப் பாதுகாக்கும் அமல்படுத்த முடியாத DPSP; உறுப்பு 24 என்பது அபாயகரமான தொழிற்சாலைகள்/சுரங்கங்களில் 14 வயதுக்குட்பட்ட குழந்தைகளை வேலைக்கு அமர்த்துவதை முற்றுமுழுதாகத் தடுத்து நிறுத்தும் அமல்படுத்தக்கூடிய FR ஆகும்",
        "Article 39(e) was added by 86th Amendment; Article 24 was added by 97th Amendment", "உறுப்பு 39(e) 86வது திருத்தத்தால் சேர்க்கப்பட்டது; உறுப்பு 24 97வது திருத்தத்தால் சேர்க்கப்பட்டது",
        "Article 39(e) permits child labor in hazardous mines if paid minimum wage", "குறைந்தபட்ச ஊதியம் வழங்கப்பட்டால் அபாயகரமான சுரங்கங்களில் குழந்தைகள் வேலை செய்ய உறுப்பு 39(e) அனுமதிக்கிறது",
        "B",
        "Article 39(e) (Part IV DPSP) directs that health and strength of workers and tender age of children are not abused and citizens are not forced by economic necessity to enter avocations unsuited to their age. Article 24 (Part III FR) is a justiciable Fundamental Right absolutely banning employment of children below 14 in factories, mines, or hazardous occupations.",
        "உறுப்பு 39(e) (பகுதி IV DPSP) தொழிலாளர்களின் ஆரோக்கியம் மற்றும் வலிமை மற்றும் குழந்தைகளின் இளம் வயது துஷ்பிரயோகம் செய்யப்படக் கூடாது என வழிகாட்டுகிறது. உறுப்பு 24 (பகுதி III FR) 14 வயதுக்குட்பட்ட குழந்தைகளைத் தொழிற்சாலைகள், சுரங்கங்கள் அல்லது அபாயகரமான தொழில்களில் வேலைக்கு அமர்த்துவதை முற்றுமுழுதாகத் தடை செய்யும் அமல்படுத்தக்கூடிய அடிப்படை உரிமையாகும்.",
        "Child Labour (Prohibition and Regulation) Act 1986 implements both Article 24 and Article 39(e).", "குழந்தைத் தொழிலாளர் (தடை மற்றும் முறைப்படுத்துதல்) சட்டம் 1986 உறுப்பு 24 மற்றும் உறுப்பு 39(e) ஆகிய இரண்டையும் செயல்படுத்துகிறது.",
        "Article 39(e) explicitly mentions tender age of children.", "உறுப்பு 39(e) வெளிப்படையாகக் குழந்தைகளின் இளம் வயதைக் குறிப்பிடுகிறது.",
        "Correct. 39(e) is DPSP protecting tender age from abuse; 24 is FR prohibiting child labor below 14 in hazardous work.", "சரி. 39(e) இளம் வயதைத் துஷ்பிரயோகத்திலிருந்து பாதுகாக்கும் DPSP; 24 என்பது 14 வயதுக்குட்பட்ட குழந்தைத் தொழிலாளரைத் தடுக்கும் FR.",
        "Both provisions were in the original 1950 Constitution text.", "இரண்டு விதிகளும் அசல் 1950 அரசியலமைப்பு உரையில் இருந்தன.",
        "Neither Article permits hazardous child labor.", "எந்தவொரு உறுப்பும் அபாயகரமான குழந்தைத் தொழிலாளரை அனுமதிக்காது."
    )

    # -------------------------------------------------------------------------
    # Q31 (Correct: C) - Amendment / Case
    # -------------------------------------------------------------------------
    add_q(
        31, "Amendment/Case",
        "Apart from adding Article 38(2) to DPSP, what major constitutional change did the 44th Constitutional Amendment Act 1978 effect regarding Fundamental Rights?",
        "DPSP-ல் உறுப்பு 38(2)-ஐச் சேர்த்ததைத் தவிர, 1978-ன் 44வது அரசியலமைப்பு திருத்தச் சட்டம் அடிப்படை உரிமைகள் குறித்து என்ன முக்கிய அரசியலமைப்பு மாற்றத்தைச் செய்தது?",
        "It made Right to Education a Fundamental Right under Article 21A", "இது உறுப்பு 21A-ன் கீழ் கல்வி உரிமையை அடிப்படை உரிமையாக்கியது",
        "It added Fundamental Duties under Article 51A", "இது உறுப்பு 51A-ன் கீழ் அடிப்படைக் கடமைகளைச் சேர்த்தது",
        "It deleted the Right to Property (Article 31) from Fundamental Rights and made it a legal right under Article 300A", "இது அடிப்படை உரிமைகளிலிருந்து சொத்து உரிமையை (உறுப்பு 31) நீக்கி, உறுப்பு 300A-ன் கீழ் அதை ஒரு சட்ட உரிமையாக மாற்றியது",
        "It introduced 10% EWS reservation under Article 15(6)", "இது உறுப்பு 15(6)-ன் கீழ் 10% EWS இடஒதுக்கீட்டை அறிமுகப்படுத்தியது",
        "C",
        "The 44th Constitutional Amendment Act, 1978 (Morarji Desai Janata Govt) deleted Right to Property from Part III (Articles 19(1)(f) and 31) and re-enacted it as a statutory legal right under Article 300A in Part XII, while simultaneously inserting Article 38(2) into DPSP.",
        "1978-ன் 44வது அரசியலமைப்பு திருத்தச் சட்டம் (மொரார்ஜி தேசாய் ஜனதா அரசு) பகுதி III-லிருந்து சொத்து உரிமையை நீக்கி, பகுதி XII-ல் உறுப்பு 300A-ன் கீழ் அதை ஒரு சட்டப் பூர்வ உரிமையாக மாற்றியது, அதே நேரத்தில் DPSP-ல் உறுப்பு 38(2)-ஐ இணைத்தது.",
        "This removed property protection roadblocks for socio-economic land reform laws implementing Articles 39(b) and 39(c).", "இது உறுப்புகள் 39(b) மற்றும் 39(c)-ஐ செயல்படுத்தும் சமூக-பொருளாதார நிலச்சீர்திருத்தச் சட்டங்களுக்கான சொத்து பாதுகாப்புத் தடைகளை அகற்றியது.",
        "Right to Education under Art 21A was added by 86th Amendment 2002.", "உறுப்பு 21A-ன் கீழ் கல்வி உரிமை 86வது திருத்தம் 2002 மூலம் சேர்க்கப்பட்டது.",
        "Fundamental Duties were added by 42nd Amendment 1976.", "அடிப்படைக் கடமைகள் 42வது திருத்தம் 1976 மூலம் சேர்க்கப்பட்டன.",
        "Correct. 44th Amendment 1978 removed Right to Property (Art 31) from Part III to Art 300A and inserted Art 38(2).", "சரி. 44வது திருத்தம் 1978 பகுதி III-லிருந்து சொத்து உரிமையை நீக்கி உறுப்பு 300A-க்கு மாற்றியது மற்றும் உறுப்பு 38(2)-ஐ இணைத்தது.",
        "EWS reservation was introduced by 103rd Amendment 2019.", "EWS இடஒதுக்கீடு 103வது திருத்தம் 2019 மூலம் அறிமுகப்படுத்தப்பட்டது."
    )

    # -------------------------------------------------------------------------
    # Q32 (Correct: D) - Application / Inference
    # -------------------------------------------------------------------------
    add_q(
        32, "Application",
        "How has the judicial expansion of Article 21 (Right to Life) affected the practical enforceability of non-justiciable DPSPs?",
        "உறுப்பு 21-ன் (வாழ்வு உரிமை) நீதித்துறை விரிவாக்கம் எவ்வாறு அமல்படுத்த முடியாத DPSP-களின் நடைமுறை அமலாக்கத்தைப் பாதித்துள்ளது?",
        "It made all DPSPs completely void and unenforceable", "இது அனைத்து DPSP-களையும் முற்றிலும் செல்லாததாகவும் அமல்படுத்த முடியாததாகவும் மாற்றியது",
        "It restricted Supreme Court powers to hearing tax appeals only", "இது உச்ச நீதிமன்ற அதிகாரங்களை வரி மேல்முறையீடுகளை விசாரிப்பதற்கு மட்டுமே சுருக்கியது",
        "It prevented Parliament from passing any welfare legislation", "இது நாடாளுமன்றம் எந்தவொரு நலச் சட்டத்தையும் இயற்றுவதைத் தடுத்தது",
        "It creatively incorporated key DPSPs (like Art 39A Free Legal Aid, Art 42 Humane Work, Art 47 Public Health, Art 48A Environment) INTO Article 21, making them enforceable as aspects of Right to Life", "இது முக்கிய DPSP-களை (உறுப்பு 39A இலவச சட்ட உதவி, உறுப்பு 42 மனிதத்தன்மை வேலை, உறுப்பு 47 பொது சுகாதாரம், உறுப்பு 48A சுற்றுச்சூழல் போன்றவை) உறுப்பு 21-க்குள் ஆக்கப்பூர்வமாக உள்ளடக்கி, வாழ்வு உரிமையின் அம்சங்களாக அவற்றை அமல்படுத்தக்கூடியதாக மாற்றியது",
        "D",
        "Through judicial activism (post-Maneka Gandhi 1978), the Supreme Court expanded the horizon of Article 21 ('Right to live with human dignity') by reading various DPSPs (39A, 42, 47, 48A, 45) into Article 21, effectively making aspects of socio-economic justice enforceable via writ petitions.",
        "நீதித்துறை விழிப்புணர்வு மூலம் (மேனகா காந்தி 1978க்குப் பின்), உச்ச நீதிமன்றம் பல்வேறு DPSP-களை (39A, 42, 47, 48A, 45) உறுப்பு 21-க்குள் வாசிப்பதன் மூலம் உறுப்பு 21-ன் எல்லையை ('மனித கண்ணியத்துடன் வாழும் உரிமை') விரிவுபடுத்தியது.",
        "This synthesis bridges the gap between Part III civil liberties and Part IV socio-economic goals.",
        "இந்தச் சேர்க்கை பகுதி III சிவில் சுதந்திரங்களுக்கும் பகுதி IV சமூக-பொருளாதார இலக்குகளுக்கும் இடையிலான இடைவெளியைக் குறைக்கிறது.",
        "Judicial expansion enhanced DPSP enforceability, not voided it.", "நீதித்துறை விரிவாக்கம் DPSP அமலாக்கத்தை மேம்படுத்தியதே தவிர, செல்லாததாக்கவில்லை.",
        "Article 21 expansion broadened Supreme Court jurisdiction via PILs.", "உறுப்பு 21 விரிவாக்கம் பொதுநல வழக்குகள் (PIL) மூலம் உச்ச நீதிமன்ற அதிகார வரம்பை விரிவுபடுத்தியது.",
        "It encouraged Parliament to pass welfare Acts.", "இது நாடாளுமன்றம் நலச் சட்டங்களை இயற்ற ஊக்குவித்தது.",
        "Correct. SC creatively read key DPSPs into Article 21 to make them enforceable procedural and substantive rights.", "சரி. DPSP-களை அமல்படுத்தக்கூடிய உரிமைகளாக மாற்ற SC முக்கிய DPSP-களை உறுப்பு 21-க்குள் ஆக்கப்பூர்வமாக வாசித்தது."
    )

    # -------------------------------------------------------------------------
    # Q33 (Correct: A) - Case-based
    # -------------------------------------------------------------------------
    add_q(
        33, "Amendment/Case",
        "In State of Tamil Nadu v. L. Abu Kavur Bai (1984), how did the Supreme Court view state nationalization of transport services under Article 39(b)?",
        "தமிழ்நாடு அரசு எதிர் எல். அபு கவூர் பாய் வழக்கில் (1984), உறுப்பு 39(b)-ன் கீழ் போக்குவரத்து சேவைகளை மாநில அரசு தேசியமயமாக்கியதை உச்ச நீதிமன்றம் எவ்வாறு நோக்கியது?",
        "SC UPHELD state transport nationalization, holding that material resources under Art 39(b) include both natural and man-made, public and private assets for common good", "உறுப்பு 39(b)-ன் கீழ் பொருள் வளங்களில் இயற்கை மற்றும் மனிதனால் உருவாக்கப்பட்ட, பொது மற்றும் தனியார் சொத்துக்கள் இரண்டும் அடங்கும் எனப் பிடித்து, மாநில போக்குவரத்து தேசியமயமாக்கலை SC உறுதி செய்தது",
        "SC STRUCK DOWN transport nationalization as a violation of Article 19(1)(g)", "உறுப்பு 19(1)(g)-ஐ மீறுவதாகக் கூறி போக்குவரத்து தேசியமயமாக்கலை SC ரத்து செய்தது",
        "SC held that Article 39(b) applies only to agricultural land, not buses", "உறுப்பு 39(b) விவசாய நிலத்திற்கு மட்டுமே பொருந்தும், பேருந்துகளுக்கு அல்ல என SC கூறியது",
        "SC referred the transport policy to the Privy Council in London", "SC போக்குவரத்து கொள்கையை லண்டனில் உள்ள பிரிவி கவுன்சிலுக்குப் பரிந்துரைத்தது",
        "A",
        "In State of TN v. L. Abu Kavur Bai (1984), a Constitution Bench held that 'material resources of the community' under Article 39(b) is a wide expression encompassing all resources (natural, physical, movable, immovable, public or private) which subserve common good, upholding Tamil Nadu Motor Vehicles Nationalisation Act under Article 31C protection.",
        "தமிழ்நாடு அரசு எதிர் எல். அபு கவூர் பாய் வழக்கில் (1984), உறுப்பு 39(b)-ன் கீழ் 'சமூகத்தின் பொருள் வளங்கள்' என்பது பொது நலனுக்குப் பயன்படும் அனைத்து வளங்களையும் (இயற்கை, பௌதிக, அசையும், அசையா, பொது அல்லது தனியார்) உள்ளடக்கிய ஒரு பரந்த வெளிப்பாடு என அரசியலமைப்பு அமர்வு தீர்ப்பளித்தது.",
        "This affirmed that nationalization of private transport services for public welfare is protected under Article 31C.",
        "பொது நலனுக்காகத் தனியார் போக்குவரத்து சேவைகளைத் தேசியமயமாக்குவது உறுப்பு 31C-ன் கீழ் பாதுகாக்கப்படுகிறது என்பதை இது உறுதிப்படுத்தியது.",
        "Correct. SC upheld nationalization under Art 39(b) protected by Art 31C.", "சரி. உறுப்பு 31C-ஆல் பாதுகாக்கப்பட்ட உறுப்பு 39(b)-ன் கீழ் தேசியமயமாக்கலை SC உறுதி செய்தது.",
        "Nationalization law was protected under Art 31C against Art 19(1)(g).", "தேசியமயமாக்கல் சட்டம் உறுப்பு 19(1)(g)-க்கு எதிராக உறுப்பு 31C-ன் கீழ் பாதுகாக்கப்பட்டது.",
        "Material resources includes both natural assets and transport/industrial assets.", "பொருள் வளங்களில் இயற்கை சொத்துக்கள் மற்றும் போக்குவரத்து/தொழில்துறை சொத்துக்கள் இரண்டும் அடங்கும்.",
        "Privy Council appeals were abolished by Abolition of Privy Council Jurisdiction Act 1949.", "பிரிவி கவுன்சில் மேல்முறையீடுகள் 1949 சட்டத்தால் ஒழிக்கப்பட்டன."
    )

    # -------------------------------------------------------------------------
    # Q34 (Correct: B) - Provision-based
    # -------------------------------------------------------------------------
    add_q(
        34, "Article-based",
        "Which clause of Article 39 specifically directs the State to secure that 'workers are not forced by economic necessity to enter avocations unsuited to their age or strength'?",
        "'தொழிலாளர்கள் வறுமையின் காரணமாகத் தங்களது வயது அல்லது வலிமைக்குப் பொருந்தாத வேலைகளில் ஈடுபடக் கட்டாயப்படுத்தப்படக் கூடாது' என்பதை உறுதி செய்ய அரசுக்கு ஆணையிடும் உறுப்பு 39-ன் குறிப்பிட்ட உட்பிரிவு எது?",
        "Article 39(c)", "உறுப்பு 39(c)",
        "Article 39(e)", "உறுப்பு 39(e)",
        "Article 39(f)", "உறுப்பு 39(f)",
        "Article 39A", "உறுப்பு 39A",
        "B",
        "Article 39(e) directs that the health and strength of workers, men and women, and the tender age of children are not abused and that citizens are not forced by economic necessity to enter avocations unsuited to their age or strength.",
        "உறுப்பு 39(e) ஆண், பெண் தொழிலாளர்களின் ஆரோக்கியம் மற்றும் வலிமை மற்றும் குழந்தைகளின் இளம் வயது துஷ்பிரயோகம் செய்யப்படக் கூடாது என்றும், குடிமக்கள் தங்களது வயது அல்லது வலிமைக்குப் பொருந்தாத வேலைகளில் ஈடுபடக் கட்டாயப்படுத்தப்படக் கூடாது என்றும் வழிகாட்டுகிறது.",
        "Article 39(e) focuses on occupational health and protection against unsuited forced labor.", "உறுப்பு 39(e) தொழிலும்சார் சுகாதாரம் மற்றும் பொருந்தாத கட்டாய வேலையிலிருந்து பாதுகாப்பது மீது கவனம் செலுத்துகிறது.",
        "Article 39(c) deals with wealth concentration prevention.", "உறுப்பு 39(c) செல்வக் குவிப்புத் தடை பற்றியது.",
        "Correct. Article 39(e) protects workers from unsuited forced avocations.", "சரி. உறுப்பு 39(e) தொழிலாளர்களைப் பொருந்தாத கட்டாய வேலைகளிலிருந்து பாதுகாக்கிறது.",
        "Article 39(f) deals with healthy child development opportunities.", "உறுப்பு 39(f) ஆரோக்கியமான குழந்தை வளர்ச்சி வாய்ப்புகள் பற்றியது.",
        "Article 39A deals with free legal aid.", "உறுப்பு 39A இலவச சட்ட உதவி பற்றியது."
    )

    # -------------------------------------------------------------------------
    # Q35 (Correct: C) - Application / Inference
    # -------------------------------------------------------------------------
    add_q(
        35, "Application",
        "How did Parliament statutorily implement Article 50 (Separation of Judiciary from Executive) through the Code of Criminal Procedure (CrPC) 1973?",
        "1973 குற்றவியல் நடைமுறைச் சட்டம் (CrPC) மூலம் நாடாளுமன்றம் எவ்வாறு உறுப்பு 50-ஐ (நிர்வாகத்திலிருந்து நீதித்துறை பிரிப்பு) சட்டப்பூர்வமாகச் செயல்படுத்தியது?",
        "By placing District Collectors under the direct administrative control of the High Court", "மாவட்ட ஆட்சியர்களை உயர் நீதிமன்றத்தின் நேரடி நிர்வாகக் கட்டுப்பாட்டின் கீழ் வைப்பதன் மூலம்",
        "By abolishing Executive Magistrates completely across all states", "அனைத்து மாநிலங்களிலும் நிர்வாக மேஜிஸ்திரேட்டுகளை முழுமையாக ஒழிப்பதன் மூலம்",
        "By creating two distinct categories of Magistrates: Judicial Magistrates (trying criminal cases under High Court supervision) and Executive Magistrates (maintaining law & order under State Govt supervision)", "இரண்டு வெவ்வேறான மேஜிஸ்திரேட் பிரிவுகளை உருவாக்குவதன் மூலம்: நீதித்துறை மேஜிஸ்திரேட்டுகள் (உயர் நீதிமன்ற மேற்பார்வையில் குற்றவியல் வழக்குகளை விசாரிப்பவர்கள்) மற்றும் நிர்வாக மேஜிஸ்திரேட்டுகள் (மாநில அரசு மேற்பார்வையில் சட்டம் ஒழுங்கைப் பராமரிப்பவர்கள்)",
        "By merging criminal courts with municipal revenue offices", "குற்றவியல் நீதிமன்றங்களை நகராட்சி வருவாய் அலுவலகங்களுடன் இணைப்பதன் மூலம்",
        "C",
        "Before CrPC 1973, District Collectors/Magistrates exercised both executive law-enforcement powers and judicial trial powers. CrPC 1973 separated trial functions by placing Judicial Magistrates exclusively under High Court control (Articles 233-237), leaving Executive Magistrates with preventive law & order duties.",
        "CrPC 1973-க்கு முன், மாவட்ட ஆட்சியர்கள் நிர்வாகச் சட்டம்-அமலாக்க அதிகாரங்கள் மற்றும் நீதித்துறை விசாரணை அதிகாரங்கள் இரண்டையும் பயன்படுத்தினர். CrPC 1973 நீதித்துறை மேஜிஸ்திரேட்டுகளை உயர் நீதிமன்றக் கட்டுப்பாட்டின் கீழ் வைத்து விசாரணை செயல்பாடுகளைப் பிரித்தது.",
        "This statutorily fulfilled the directive under Article 50 effective April 1, 1974.", "இது ஏப்ரல் 1, 1974 முதல் உறுப்பு 50-ன் கீழ் உள்ள வழிகாட்டுதலை சட்டப்பூர்வமாக நிறைவேற்றியது.",
        "Collectors remain under State Govt executive branch, not High Court.", "ஆட்சியர்கள் மாநில அரசு நிர்வாகக் கிளையின் கீழ் உள்ளனர், உயர் நீதிமன்றத்தின் கீழ் அல்ல.",
        "Executive Magistrates were retained for preventive sections (e.g. Sec 144 CrPC).", "தடுப்புப் பிரிவுகளுக்காக (எ.கா. Sec 144 CrPC) நிர்வாக மேஜிஸ்திரேட்டுகள் தக்கவைக்கப்பட்டனர்.",
        "Correct. CrPC 1973 created Judicial Magistrates (HC control) distinct from Executive Magistrates (State Govt control).", "சரி. CrPC 1973 நிர்வாக மேஜிஸ்திரேட்டுகளிடமிருந்து வேறுபட்ட நீதித்துறை மேஜிஸ்திரேட்டுகளை (HC கட்டுப்பாடு) உருவாக்கியது.",
        "Courts were separated from revenue offices, not merged.", "நீதிமன்றங்கள் வருவாய் அலுவலகங்களிலிருந்து பிரிக்கப்பட்டன, இணைக்கப்படவில்லை."
    )

    # -------------------------------------------------------------------------
    # Q36 (Correct: D) - Direct Factual
    # -------------------------------------------------------------------------
    add_q(
        36, "Direct",
        "Which Supreme Court judgment first introduced the 'Doctrine of Harmonious Construction' to resolve conflicts between Fundamental Rights and Directive Principles?",
        "அடிப்படை உரிமைகள் மற்றும் வழிகாட்டு நெறிமுறைகளுக்கு இடையிலான மோதல்களைத் தீர்க்க 'இணக்கமான விளக்கக் கோட்பாட்டை' முதன்முதலில் அறிமுகப்படுத்திய உச்ச நீதிமன்றத் தீர்ப்பு எது?",
        "Champakam Dorairajan v. State of Madras (1951)", "செண்பகம் துரைராஜன் எதிர் மதராஸ் மாநிலம் (1951)",
        "Golak Nath v. State of Punjab (1967)", "கோலக் நாத் எதிர் பஞ்சாப் மாநிலம் (1967)",
        "Minerva Mills v. Union of India (1980)", "மினர்வா மில்ஸ் எதிர் இந்திய யூனியன் (1980)",
        "Re Kerala Education Bill Case (1958)", "கேரளா கல்வி மசோதா வழக்கு (1958)",
        "D",
        "In Re Kerala Education Bill (1958), Chief Justice S.R. Das enunciated the Doctrine of Harmonious Construction, holding that courts should aim to give effect to BOTH Part III and Part IV without rendering either a dead letter.",
        "கேரளா கல்வி மசோதா வழக்கில் (1958), தலைமை நீதிபதி எஸ்.ஆர். தாஸ் இணக்கமான விளக்கக் கோட்பாட்டை வெளியிட்டார், நீதிமன்றங்கள் பகுதி III மற்றும் பகுதி IV ஆகிய இரண்டையும் செயலற்றதாக்காமல் செயலாக்கம் அளிக்க முயல வேண்டும் என்றார்.",
        "This softened the rigid subordination stance taken earlier in Champakam Dorairajan (1951).", "இது முந்தைய செண்பகம் துரைராஜன் (1951) வழக்கில் எடுக்கப்பட்ட கடுமையான கீழ்நிலைப் பார்வையைத் தளர்த்தியது.",
        "Champakam Dorairajan (1951) held FRs were strictly superior to DPSP.", "செண்பகம் துரைராஜன் (1951) FR-கள் DPSP-ஐ விட மேலானவை என்றது.",
        "Golak Nath (1967) held FRs non-amendable.", "கோலக் நாத் (1967) FR-களைத் திருத்த முடியாது என்றது.",
        "Minerva Mills (1980) held balance between Part III and IV is Basic Feature.", "மினர்வா மில்ஸ் (1980) பகுதி III மற்றும் IV இடையிலான சமநிலையே அடிப்படை அம்சம் என்றது.",
        "Correct. Re Kerala Education Bill (1958) introduced Doctrine of Harmonious Construction.", "சரி. கேரளா கல்வி மசோதா வழக்கு (1958) இணக்கமான விளக்கக் கோட்பாட்டை அறிமுகப்படுத்தியது."
    )

    # -------------------------------------------------------------------------
    # Q37 (Correct: A) - Conceptual Distinction
    # -------------------------------------------------------------------------
    add_q(
        37, "Conceptual",
        "Why is Article 37 described as the 'hinge' or 'key' to understanding the constitutional status of Directive Principles?",
        "வழிகாட்டு நெறிமுறைகளின் அரசியலமைப்பு அந்தஸ்தைப் புரிந்துகொள்வதற்கு உறுப்பு 37 ஏன் 'திருகு' அல்லது 'சாவி' என்று விவரிக்கப்படுகிறது?",
        "Because Article 37 contains both the negative limitation (non-justiciable) and the positive imperative (fundamental in governance)", "ஏனெனில் உறுப்பு 37 எதிர்மறை வரம்பு (அமல்படுத்த முடியாதது) மற்றும் நேர்மறை கட்டாயம் (ஆட்சியில் அடிப்படையானது) ஆகிய இரண்டையும் கொண்டுள்ளது",
        "Because Article 37 allows the President to suspend Part IV during National Emergency", "ஏனெனில் உறுப்பு 37 தேசிய அவசரநிலையின் போது பகுதி IV-ஐ இடைநீக்கம் செய்யக் குடியரசுத் தலைவருக்கு அனுமதிக்கிறது",
        "Because Article 37 grants Supreme Court power to appoint State Governors", "ஏனெனில் உறுப்பு 37 மாநில ஆளுநர்களை நியமிக்க உச்ச நீதிமன்றத்திற்கு அதிகாரம் அளிக்கிறது",
        "Because Article 37 repeals all pre-constitutional laws inconsistent with Part IV", "ஏனெனில் உறுப்பு 37 பகுதி IV-க்கு முரணான அனைத்து முன்-அரசியலமைப்புச் சட்டங்களையும் ரத்து செய்கிறது",
        "A",
        "Article 37 contains a dual declaration: 1) Negative Clause: 'shall not be enforceable by any court' (preventing judicial writs); 2) Positive Clause: 'principles laid down are fundamental in the governance of the country and it shall be the duty of the State to apply these principles in making laws'.",
        "உறுப்பு 37 இரட்டை அறிவிப்பைக் கொண்டுள்ளது: 1) எதிர்மறைப் பிரிவு: 'நீதிமன்றங்களால் அமல்படுத்தப்படாது' (நீதித்துறை பேராணைகளைத் தடுத்தல்); 2) நேர்மறைப் பிரிவு: 'வழங்கப்பட்டுள்ள கோட்பாடுகள் நாட்டின் ஆட்சியில் அடிப்படையானவை மற்றும் சட்டம் இயற்றுவதில் இக்கோட்பாடுகளைப் பயன்படுத்துவது அரசின் கடமையாகும்'.",
        "This dual structure creates a moral and political obligation on Parliament while respecting judicial non-interference.",
        "இந்த இரட்டை அமைப்பு நீதித்துறை தலையீடின்மையை மதிக்கும் அதே வேளையில் நாடாளுமன்றத்தின் மீது ஒழுக்க மற்றும் அரசியல் கடமையை உருவாக்குகிறது.",
        "Correct. Article 37 balances non-justiciability with fundamental duty in governance.", "சரி. உறுப்பு 37 அமல்படுத்த முடியாத தன்மையை ஆட்சியில் உள்ள அடிப்படைக் கடமையுடன் சமநிலைப்படுத்துகிறது.",
        "Part IV is never suspended during Emergency.", "அவசரநிலையின் போது பகுதி IV ஒருபோதும் இடைநீக்கம் செய்யப்படுவதில்லை.",
        "Article 37 does not deal with appointment of Governors.", "உறுப்பு 37 ஆளுநர்களின் நியமனம் பற்றியது அல்ல.",
        "Article 13 repeals laws inconsistent with Part III, not Article 37 for Part IV.", "உறுப்பு 13 பகுதி III-க்கு முரணான சட்டங்களை ரத்து செய்கிறது, பகுதி IV-க்காக உறுப்பு 37 அல்ல."
    )

    # -------------------------------------------------------------------------
    # Q38 (Correct: B) - Simple Comparison
    # -------------------------------------------------------------------------
    add_q(
        38, "Comparison",
        "Compare Article 39(f) (as substituted by 42nd Amendment 1976) with Article 45 (as substituted by 86th Amendment 2002).",
        "உறுப்பு 39(f)-ஐ (42வது திருத்தம் 1976 மூலம் மாற்றியமைக்கப்பட்டது) உறுப்பு 45-உடன் (86வது திருத்தம் 2002 மூலம் மாற்றியமைக்கப்பட்டது) ஒப்பிடுக.",
        "Article 39(f) covers higher education; Article 45 covers cow protection", "உறுப்பு 39(f) உயர்கல்வியை உள்ளடக்கியது; உறுப்பு 45 பசு பாதுகாப்பை உள்ளடக்கியது",
        "Article 39(f) directs securing opportunities for healthy development and protection of children/youth against exploitation; Article 45 directs securing early childhood care and education for children below six years", "உறுப்பு 39(f) ஆரோக்கியமான வளர்ச்சி மற்றும் குழந்தைகள்/இளைஞர்களைத் துஷ்பிரயோகத்திலிருந்து பாதுகாப்பதற்கான வாய்ப்புகளை உறுதி செய்ய வழிகாட்டுகிறது; உறுப்பு 45 ஆறு வயதுக்குட்பட்ட குழந்தைகளுக்கான முன்பருவக் பராமரிப்பு மற்றும் கல்வியை உறுதி செய்ய வழிகாட்டுகிறது",
        "Article 39(f) applies to adults; Article 45 applies to senior citizens", "உறுப்பு 39(f) பெரியவர்களுக்குப் பொருந்தும்; உறுப்பு 45 முதியோர்களுக்குப் பொருந்தும்",
        "Article 39(f) is justiciable; Article 45 is a Fundamental Duty", "உறுப்பு 39(f) அமல்படுத்தக்கூடியது; உறுப்பு 45 ஒரு அடிப்படைக் கடமை",
        "B",
        "Article 39(f) (42nd CAA 1976) provides a broad welfare directive protecting children and youth from exploitation and securing healthy development in freedom and dignity. Article 45 (86th CAA 2002) provides a specific educational directive focusing on early childhood care and education (ECCE) for infants/children aged 0 to 6 years.",
        "உறுப்பு 39(f) (42வது திருத்தம் 1976) குழந்தைகள் மற்றும் இளைஞர்களைத் துஷ்பிரயோகத்திலிருந்து பாதுகாக்கும் பரந்த நல வழிகாட்டுதலை வழங்குகிறது. உறுப்பு 45 (86வது திருத்தம் 2002) 0 முதல் 6 வயது வரையிலான குழந்தைகளுக்கான முன்பருவக் பராமரிப்பு மற்றும் கல்வியில் (ECCE) கவனம் செலுத்தும் குறிப்பிட்ட கல்வி வழிகாட்டுதலை வழங்குகிறது.",
        "Both 39(f) and 45 are child-centric DPSPs added/modified by constitutional amendments.", "39(f) மற்றும் 45 ஆகிய இரண்டும் அரசியலமைப்பு திருத்தங்களால் சேர்க்கப்பட்ட/மாற்றப்பட்ட குழந்தைகளை மையமாகக் கொண்ட DPSP-கள் ஆகும்.",
        "Neither deals with higher education or cow protection.", "எதுவும் உயர்கல்வி அல்லது பசு பாதுகாப்பு பற்றியது அல்ல.",
        "Correct. 39(f) is broad child development/anti-exploitation DPSP; 45 is specific ECCE (<6 yrs) DPSP.", "சரி. 39(f) பரந்த குழந்தை வளர்ச்சி/துஷ்பிரயோக எதிர்ப்பு DPSP; 45 குறிப்பிட்ட முன்பருவக் கல்வி (<6 ஆண்டுகள்) DPSP.",
        "Both target children and youth.", "இரண்டும் குழந்தைகள் மற்றும் இளைஞர்களை இலக்காகக் கொண்டவை.",
        "Both are non-justiciable DPSPs in Part IV.", "இரண்டும் பகுதி IV-ல் உள்ள அமல்படுத்த முடியாத DPSP-கள் ஆகும்."
    )

    # -------------------------------------------------------------------------
    # Q39 (Correct: C) - Direct Factual
    # -------------------------------------------------------------------------
    add_q(
        39, "Direct",
        "Which prominent member of the Constituent Assembly famously compared the Directive Principles of State Policy to 'a cheque on a bank, payable only when the resources of the bank permit'?",
        "அரசியலமைப்பு நிர்ணய சபையின் எந்தப் புகழ்பெற்ற உறுப்பினர் அரசு வழிகாட்டு நெறிமுறைகளை 'வங்கியின் வசதி அனுமதிக்கும் போது மட்டுமே செலுத்தத்தக்க வங்கியின் காசோலைக்கு' (a cheque on a bank, payable only when resources permit) ஒப்பிட்டார்?",
        "Dr. B.R. Ambedkar", "டாக்டர் பி.ஆர். அம்பேத்கர்",
        "Granville Austin", "கிரான்வில் ஆஸ்டின்",
        "Prof. K.T. Shah", "பேராசிரியர் கே.டி. ஷா",
        "Sir Alladi Krishnaswami Ayyar", "சர் அல்லாடி கிருஷ்ணசுவாமி அய்யர்",
        "C",
        "Prof. K.T. Shah, a prominent member of the Constituent Assembly, criticized the non-justiciable nature of DPSP by comparing them to 'a cheque on a bank, payable only when the resources of the bank permit'.",
        "அரசியலமைப்பு நிர்ணய சபையின் புகழ்பெற்ற உறுப்பினரான பேராசிரியர் கே.டி. ஷா, DPSP-ன் அமல்படுத்த முடியாத இயல்பை விமர்சித்து, அவற்றை 'வங்கியின் வசதி அனுமதிக்கும் போது மட்டுமே செலுத்தத்தக்க வங்கியின் காசோலைக்கு' ஒப்பிட்டார்.",
        "This quote is a classic TNPSC exam factual question on Constituent Assembly debates.", "இந்த மேற்கோள் அரசியலமைப்பு நிர்ணய சபை விவாதங்கள் பற்றிய ஒரு செவ்வியல் டிஎன்பிஎஸ்சி தேர்வு வினாவாகும்.",
        "Dr. B.R. Ambedkar called DPSP 'Novel Features'.", "டாக்டர் பி.ஆர். அம்பேத்கர் DPSP-ஐ 'நவீன அம்சங்கள்' என்றார்.",
        "Granville Austin called DPSP 'Conscience of the Constitution'.", "கிரான்வில் ஆஸ்டின் DPSP-ஐ 'அரசியலமைப்பின் மனசாட்சி' என்றார்.",
        "Correct. Prof. K.T. Shah made the bank cheque analogy for DPSP.", "சரி. பேராசிரியர் கே.டி. ஷா DPSP-க்கு வங்கி காசோலை உவமையைக் கூறினார்.",
        "Sir Alladi Krishnaswami Ayyar praised DPSP governance mandate.", "சர் அல்லாடி கிருஷ்ணசுவாமி அய்யர் DPSP ஆட்சி கட்டளையைப் பாராட்டினார்."
    )

    # -------------------------------------------------------------------------
    # Q40 (Correct: D) - Case-based
    # -------------------------------------------------------------------------
    add_q(
        40, "Amendment/Case",
        "In Sanjeev Coke Manufacturing Co. v. Bharat Coking Coal Ltd. (1983), the Supreme Court reiterated the constitutional validity of nationalization laws enacted under which DPSP clauses?",
        "சஞ்சீவ் கோக் உற்பத்தி நிறுவனம் வழக்கில் (1983), எந்த DPSP உட்பிரிவுகளின் கீழ் இயற்றப்பட்ட தேசியமயமாக்கல் சட்டங்களின் அரசியலமைப்பு செல்லுபடித் தன்மையை உச்ச நீதிமன்றம் மீண்டும் உறுதிப்படுத்தியது?",
        "Articles 40 and 44", "உறுப்புகள் 40 மற்றும் 44",
        "Articles 41 and 42", "உறுப்புகள் 41 மற்றும் 42",
        "Articles 48 and 48A", "உறுப்புகள் 48 மற்றும் 48A",
        "Articles 39(b) and 39(c)", "உறுப்புகள் 39(b) மற்றும் 39(c)",
        "D",
        "In Sanjeev Coke (1983), the SC reaffirmed that statutory nationalization of coal mines and coking coal infrastructure aimed at serving common good and preventing wealth concentration was protected under Article 31C implementing Articles 39(b) and 39(c).",
        "சஞ்சீவ் கோக் வழக்கில் (1983), பொது நலனுக்குப் பயன்படுவதையும் செல்வக் குவிப்பதைத் தடுப்பதையும் நோக்கமாகக் கொண்ட நிலக்கரி சுரங்கங்கள் மற்றும் கோக்கிங் நிலக்கரி உள்கட்டமைப்பின் சட்டப்பூர்வ தேசியமயமாக்கல் உறுப்புகள் 39(b) மற்றும் 39(c)-ஐ செயல்படுத்தும் உறுப்பு 31C-ன் கீழ் பாதுகாக்கப்படுகிறது என்பதை SC மீண்டும் உறுதிப்படுத்தியது.",
        "Article 31C protects laws implementing 39(b) and 39(c) from Article 14 and 19 challenges.", "உறுப்பு 31C உறுப்புகள் 14 மற்றும் 19 சவால்களிலிருந்து 39(b) மற்றும் 39(c)-ஐ செயல்படுத்தும் சட்டங்களைப் பாதுகாக்கிறது.",
        "Articles 40 and 44 are not protected under Article 31C.", "உறுப்புகள் 40 மற்றும் 44 உறுப்பு 31C-ன் கீழ் பாதுகாக்கப்பட்டவை அல்ல.",
        "Articles 41 and 42 are not protected under Article 31C.", "உறுப்புகள் 41 மற்றும் 42 உறுப்பு 31C-ன் கீழ் பாதுகாக்கப்பட்டவை அல்ல.",
        "Articles 48 and 48A are not protected under Article 31C.", "உறுப்புகள் 48 மற்றும் 48A உறுப்பு 31C-ன் கீழ் பாதுகாக்கப்பட்டவை அல்ல.",
        "Correct. Sanjeev Coke (1983) upheld coking coal nationalization laws under Articles 39(b) and 39(c).", "சரி. சஞ்சீவ் கோக் (1983) உறுப்புகள் 39(b) மற்றும் 39(c)-ன் கீழ் நிலக்கரி தேசியமயமாக்கல் சட்டங்களை உறுதி செய்தது."
    )

    # -------------------------------------------------------------------------
    # Q41 (Correct: A) - Simple Comparison
    # -------------------------------------------------------------------------
    add_q(
        41, "Comparison",
        "Compare the constitutional status of Co-operative Societies under Article 19(1)(c) (Part III FR) and Article 43B (Part IV DPSP), both inserted by the 97th Amendment Act 2011.",
        "2011-ன் 97வது திருத்தச் சட்டத்தால் இணைக்கப்பட்ட உறுப்பு 19(1)(c) (பகுதி III FR) மற்றும் உறுப்பு 43B (பகுதி IV DPSP) ஆகியவற்றின் கீழ் கூட்டுறவுச் சங்கங்களின் அரசியலமைப்பு அந்தஸ்தை ஒப்பிடுக.",
        "Article 19(1)(c) grants citizens a justiciable Fundamental Right to form co-operative societies, whereas Article 43B is a non-justiciable DPSP directing the State to promote their voluntary formation and autonomous functioning", "உறுப்பு 19(1)(c) குடிமக்களுக்குக் கூட்டுறவுச் சங்கங்களை அமைக்கும் அமல்படுத்தக்கூடிய அடிப்படை உரிமையை வழங்குகிறது, மாறாக உறுப்பு 43B என்பது அவற்றின் தன்னார்வ உருவாக்கம் மற்றும் தன்னாட்சி செயல்பாட்டை மேம்படுத்த அரசுக்கு வழிகாட்டும் அமல்படுத்த முடியாத DPSP ஆகும்",
        "Article 19(1)(c) applies to foreign firms, while Article 43B applies to state armed forces", "உறுப்பு 19(1)(c) வெளிநாட்டு நிறுவனங்களுக்குப் பொருந்தும், 43B மாநில ஆயுதப் படைகளுக்குப் பொருந்தும்",
        "Article 19(1)(c) is a DPSP, while Article 43B is a Fundamental Right", "உறுப்பு 19(1)(c) ஒரு DPSP, 43B ஒரு அடிப்படை உரிமை",
        "Both provisions were deleted by the Supreme Court in 2021", "இரண்டு விதிகளும் 2021-ல் உச்ச நீதிமன்றத்தால் நீக்கப்பட்டன",
        "A",
        "The 97th Amendment Act 2011 amended Article 19(1)(c) to include 'co-operative societies' as a justiciable Fundamental Right to form associations, while simultaneously inserting Article 43B into Part IV as a DPSP guiding State policy to promote autonomous functioning of co-operatives.",
        "2011-ன் 97வது திருத்தச் சட்டம் 'கூட்டுறவுச் சங்கங்களை' அமைக்கும் அமல்படுத்தக்கூடிய அடிப்படை உரிமையாக உறுப்பு 19(1)(c)-ஐத் திருத்தியது, அதே நேரத்தில் கூட்டுறவுகளின் தன்னாட்சி செயல்பாட்டை மேம்படுத்த அரசுக் கொள்கையை வழிகாட்டும் DPSP-ஆக பகுதி IV-ல் உறுப்பு 43B-ஐ இணைத்தது.",
        "Part IX-B added by 97th Amendment regarding state co-operative rules was partially struck down in 2021 for lack of state ratification, but Arts 19(1)(c) and 43B remain active.",
        "மாநில ஒப்புதல் இல்லாததால் பகுதி IX-B 2021-ல் பகுதியளவாக ரத்து செய்யப்பட்டது, ஆனால் உறுப்புகள் 19(1)(c) மற்றும் 43B தொடர்ந்து செயல்படுகின்றன.",
        "Correct. 19(1)(c) is citizen FR to form co-operatives; 43B is State DPSP to promote co-operatives.", "சரி. 19(1)(c) கூட்டுறவுகளை அமைக்கும் குடிமகன் FR; 43B கூட்டுறவுகளை மேம்படுத்தும் அரசு DPSP.",
        "Neither provision applies to foreign firms or armed forces.", "எந்தவொரு விதியும் வெளிநாட்டு நிறுவனங்கள் அல்லது ஆயுதப் படைகளுக்குப் பொருந்தாது.",
        "Incorrect reversal of Part III FR and Part IV DPSP.", "பகுதி III FR மற்றும் பகுதி IV DPSP-ன் தவறான தலைகீழ் கூற்று.",
        "Articles 19(1)(c) and 43B remain active constitutional text.", "உறுப்புகள் 19(1)(c) மற்றும் 43B தொடர்ந்து அரசியலமைப்பு உரையாகச் செயல்படுகின்றன."
    )

    # -------------------------------------------------------------------------
    # Q42 (Correct: B) - Application / Inference
    # -------------------------------------------------------------------------
    add_q(
        42, "Application",
        "Which of the following major national social welfare programs statutorily implements the Directive Principle contained in Article 41 (Right to Work)?",
        "பின்வரும் எந்த முதன்மையான தேசிய சமூக நலத் திட்டம் உறுப்பு 41-ல் (வேலை உரிமை) உள்ள வழிகாட்டு நெறிமுறையைச் சட்டப்பூர்வமாகச் செயல்படுத்துகிறது?",
        "PM POSHAN Scheme", "பிஎம் போஷன் திட்டம்",
        "Mahatma Gandhi National Rural Employment Guarantee Act (MGNREGA), 2005", "மகாத்மா காந்தி தேசிய ஊரக வேலை உறுதிச் சட்டம் (MGNREGA), 2005",
        "Ayushman Bharat Pradhan Mantri Jan Arogya Yojana", "ஆயுஷ்மான் பாரத் பிரதான் மந்திரி ஜன் ஆரோக்கிய யோஜனா",
        "Deendayal Antyodaya Yojana - National Urban Livelihoods Mission", "தீன்தயாள அந்த்யோதயா யோஜனா - தேசிய நகர்ப்புற வாழ்வாதார இயக்கம்",
        "B",
        "MGNREGA 2005 statutorily implements Article 41 (Right to Work) by providing a legal guarantee of 100 days of wage employment in a financial year to every rural household whose adult members volunteer to do unskilled manual work.",
        "MGNREGA 2005 உடலுழைப்பு செய்ய முன்வரும் ஒவ்வொரு கிராமப்புறக் குடும்பத்திற்கும் ஒரு நிதியாண்டில் 100 நாட்கள் ஊதிய வேலைவாய்ப்பிற்குச் சட்டப்பூர்வ உத்தரவாதம் அளிப்பதன் மூலம் உறுப்பு 41-ஐ (வேலை உரிமை) சட்டப்பூர்வமாகச் செயல்படுத்துகிறது.",
        "MGNREGA transformed Article 41 DPSP goal into a statutory legal right.", "MGNREGA உறுப்பு 41 DPSP இலக்கை ஒரு சட்டப்பூர்வ உரிமையாக மாற்றியது.",
        "PM POSHAN implements Article 47 (Nutrition).", "பிஎம் போஷன் உறுப்பு 47-ஐ (சத்துணவு) செயல்படுத்துகிறது.",
        "Correct. MGNREGA 2005 statutorily implements Article 41 Right to Work.", "சரி. MGNREGA 2005 உறுப்பு 41 வேலை உரிமையைச் சட்டப்பூர்வமாகச் செயல்படுத்துகிறது.",
        "Ayushman Bharat implements Article 47 (Public Health).", "ஆயுஷ்மான் பாரத் உறுப்பு 47-ஐ (பொது சுகாதாரம்) செயல்படுத்துகிறது.",
        "National Urban Livelihoods Mission focuses on urban skill development.", "தேசிய நகர்ப்புற வாழ்வாதார இயக்கம் நகர்ப்புறத் திறன் மேம்பாட்டில் கவனம் செலுத்துகிறது."
    )

    # -------------------------------------------------------------------------
    # Q43 (Correct: C) - Direct Factual
    # -------------------------------------------------------------------------
    add_q(
        43, "Direct",
        "Which state in India is historically the ONLY state to have a legacy Uniform Civil Code (UCC) operating since the colonial era preserved under Article 44 principles?",
        "இந்தியாவில் வரலாற்று ரீதியாக உறுப்பு 44 கோட்பாடுகளின் கீழ் பாதுகாக்கப்பட்ட காலனித்துவ காலத்திலிருந்து செயல்படும் பாரம்பரிய பொது சிவில் சட்டத்தைக் (UCC) கொண்ட ஒரே மாநிலம் எது?",
        "Kerala", "கேரளா",
        "Gujarat", "குஜராத்",
        "Goa", "கோவா",
        "Punjab", "பஞ்சாப்",
        "C",
        "Goa is the only state in India that has a functioning Uniform Civil Code — the Goa Civil Code 1867 (Portuguese Civil Code) — which was retained post-liberation in 1961 governing marriage, divorce, and inheritance for all religious communities.",
        "கோவா இந்தியாவில் செயல்படும் பொது சிவில் சட்டத்தைக் கொண்ட ஒரே மாநிலமாகும் — 1867 கோவா சிவில் சட்டம் (போர்ச்சுகீசிய சிவில் சட்டம்) — இது 1961 விடுதலைக்குப் பின் தக்கவைக்கப்பட்டு அனைத்து மதச் சமூகங்களுக்கும் திருமணம், விவாகரத்து மற்றும் வாரிசுரிமையைக் கட்டுப்படுத்துகிறது.",
        "Uttarakhand became the first state in independent India to pass a new UCC Bill in 2024.", "சுதந்திர இந்தியாவில் 2024-ல் புதிய UCC மசோதாவை நிறைவேற்றிய முதல் மாநிலம் உத்தரகாண்ட் ஆகும்.",
        "Kerala does not have a Uniform Civil Code.", "கேரளாவில் பொது சிவில் சட்டம் இல்லை.",
        "Gujarat does not have a legacy UCC.", "குஜராத்தில் பாரம்பரிய UCC இல்லை.",
        "Correct. Goa is the only Indian state with a legacy Uniform Civil Code.", "சரி. கோவா பாரம்பரிய பொது சிவில் சட்டத்தைக் கொண்ட ஒரே இந்திய மாநிலமாகும்.",
        "Punjab follows standard personal laws.", "பஞ்சாப் வழக்கமான தனிநபர் சட்டங்களைப் பின்பற்றுகிறது."
    )

    # -------------------------------------------------------------------------
    # Q44 (Correct: D) - Application / Inference
    # -------------------------------------------------------------------------
    add_q(
        44, "Application",
        "Synthesize the 3-way constitutional integration of environmental protection in the Indian Constitution across Part III, Part IV, and Part IV-A.",
        "இந்திய அரசியலமைப்பில் பகுதி III, பகுதி IV மற்றும் பகுதி IV-A ஆகியவற்றில் சுற்றுச்சூழல் பாதுகாப்பின் 3-வழி அரசியலமைப்பு ஒருங்கிணைப்பைத் தொகுத்துக் கூறுக.",
        "Part III prohibits environment laws; Part IV bans forests; Part IV-A applies only to foreign citizens", "பகுதி III சுற்றுச்சூழல் சட்டங்களைத் தடுக்கிறது; பகுதி IV காடுகளைத் தடை செய்கிறது; பகுதி IV-A வெளிநாட்டு குடிமக்களுக்கு மட்டுமே பொருந்தும்",
        "Environmental protection is mentioned only in Part III under Article 19", "சுற்றுச்சூழல் பாதுகாப்பு பகுதி III-ல் உறுப்பு 19-ன் கீழ் மட்டுமே குறிப்பிடப்பட்டுள்ளது",
        "Environmental protection is mentioned only in Part IV-A under Article 51A(a)", "சுற்றுச்சூழல் பாதுகாப்பு பகுதி IV-A-ல் உறுப்பு 51A(a)-ன் கீழ் மட்டுமே குறிப்பிடப்பட்டுள்ளது",
        "Part IV Article 48A imposes State Duty; Part IV-A Article 51A(g) imposes Citizen Duty; Part III Article 21 read together enforces the justiciable Right to Clean Environment", "பகுதி IV உறுப்பு 48A அரசு கடமையை விதிக்கிறது; பகுதி IV-A உறுப்பு 51A(g) குடிமகன் கடமையை விதிக்கிறது; பகுதி III உறுப்பு 21 இணைந்து வாசிக்கப்படும் போது அமல்படுத்தக்கூடிய தூய்மையான சுற்றுச்சூழல் உரிமையை அமல்படுத்துகிறது",
        "D",
        "India's environmental constitutional framework is a 3-way integration: 1) Part IV Art 48A (State Directive to protect environment & wildlife); 2) Part IV-A Art 51A(g) (Fundamental Duty of citizens to protect natural environment); 3) Part III Art 21 (Judicial interpretation enforcing Right to Clean Air/Water as Right to Life).",
        "இந்தியாவின் சுற்றுச்சூழல் அரசியலமைப்பு கட்டமைப்பு ஒரு 3-வழி ஒருங்கிணைப்பாகும்: 1) பகுதி IV உறுப்பு 48A (சுற்றுச்சூழலை எதிர்நோக்கும் அரசு வழிகாட்டுதல்); 2) பகுதி IV-A உறுப்பு 51A(g) (இயற்கைச் சூழலைப் பாதுகாக்கும் குடிமகனின் அடிப்படைக் கடமை); 3) பகுதி III உறுப்பு 21 (தூய்மையான காற்று/நீர் உரிமையை வாழ்வு உரிமையாக அமல்படுத்தும் நீதித்துறை விளக்கம்).",
        "This 3-way synthesis was forged by Justice V.R. Krishna Iyer and Justice P.N. Bhagwati in environmental PILs.", "இந்த 3-வழி தொகுப்பு சுற்றுச்சூழல் பொதுநல வழக்குகளில் நீதிபதி வி.ஆர். கிருஷ்ணய்யர் மற்றும் நீதிபதி பி.என். பகவதி ஆகியோரால் உருவாக்கப்பட்டது.",
        "Environment laws are encouraged, not prohibited.", "சுற்றுச்சூழல் சட்டங்கள் ஊக்குவிக்கப்படுகின்றன, தடுக்கப்படவில்லை.",
        "Environment protection is in Art 48A (Part IV) and Art 51A(g) (Part IV-A), not Art 19.", "சுற்றுச்சூழல் பாதுகாப்பு உறுப்புகள் 48A மற்றும் 51A(g)-ல் உள்ளது, உறுப்பு 19-ல் அல்ல.",
        "Article 51A(a) deals with National Flag and Anthem, not environment.", "உறுப்பு 51A(a) தேசியக் கொடி மற்றும் கீதம் பற்றியது, சுற்றுச்சூழல் பற்றியது அல்ல.",
        "Correct. 48A (State DPSP) + 51A(g) (Citizen FD) + Art 21 (FR) form the 3-way environmental integration.", "சரி. 48A (அரசு DPSP) + 51A(g) (குடிமகன் FD) + உறுப்பு 21 (FR) ஆகியவை 3-வழி சுற்றுச்சூழல் ஒருங்கிணைப்பை உருவாக்குகின்றன."
    )

    # -------------------------------------------------------------------------
    # Q45 (Correct: A) - Conceptual Distinction
    # -------------------------------------------------------------------------
    add_q(
        45, "Conceptual",
        "What does the phrase 'fundamental in the governance of the country' under Article 37 signify for the Executive and Legislature?",
        "உறுப்பு 37-ன் கீழ் உள்ள 'நாட்டின் ஆட்சியில் அடிப்படையானவை' என்ற சொற்றொடர் நிர்வாகம் மற்றும் சட்டமன்றத்திற்கு என்ன குறிக்கிறது?",
        "It signifies that while courts cannot enforce DPSPs via writs, the Executive and Legislature are constitutionally duty-bound to apply DPSPs as policy benchmarks in formulating budgets and enacting laws", "நீதிமன்றங்கள் DPSP-களைப் பேராணைகள் மூலம் அமல்படுத்த முடியாது என்றாலும், பட்ஜெட்டுகளை உருவாக்குவதிலும் சட்டங்களை இயற்றுவதிலும் DPSP-களைக் கொள்கை அளவுகோல்களாகப் பயன்படுத்த நிர்வாகமும் சட்டமன்றமும் அரசியலமைப்பு ரீதியாகக் கடமைப்பட்டுள்ளன என்பதை இது குறிக்கிறது",
        "It signifies that all DPSP laws automatically bypass Governor and Presidential assent", "அனைத்து DPSP சட்டங்களும் ஆளுநர் மற்றும் குடியரசுத் தலைவர் ஒப்புதலைத் தானாகவே தவிர்க்கும் என்பதை இது குறிக்கிறது",
        "It signifies that state ministers can be impeached by District Courts for ignoring DPSP", "DPSP-ஐப் புறக்கணிப்பதற்காக மாநில அமைச்சர்களை மாவட்ட நீதிமன்றங்கள் பதவி நீக்கம் செய்யலாம் என்பதை இது குறிக்கிறது",
        "It signifies that DPSPs apply only to Panchayats and not to Parliament", "DPSP-கள் நாடாளுமன்றத்திற்கு அல்லாமல் பஞ்சாயத்துகளுக்கு மட்டுமே பொருந்தும் என்பதை இது குறிக்கிறது",
        "A",
        "Article 37 explicitly states 'it shall be the duty of the State to apply these principles in making laws'. 'Fundamental in governance' means DPSPs serve as the guiding light, moral compass, and socio-economic test for all government policies and legislative Acts.",
        "உறுப்பு 37 'சட்டம் இயற்றுவதில் இக்கோட்பாடுகளைப் பயன்படுத்துவது அரசின் கடமையாகும்' என வெளிப்படையாகக் கூறுகிறது. 'ஆட்சியில் அடிப்படையானவை' என்றால் DPSP-கள் அனைத்து அரசு கொள்கைகளுக்கும் சட்டமன்ற சட்டங்களுக்கும் வழிகாட்டும் ஒளியாகவும், ஒழுக்க திசைகாட்டியாகவும், சமூக-பொருளாதார சோதனையாகவும் செயல்படுகின்றன என்று பொருளாகும்.",
        "Dr. B.R. Ambedkar stressed that no government can ignore DPSPs without answering to voters at election time.", "தேர்தல் காலத்தில் வாக்காளர்களுக்குப் பதிலளிக்காமல் எந்தவொரு அரசாங்கமும் DPSP-களைப் புறக்கணிக்க முடியாது என்று டாக்டர் பி.ஆர். அம்பேத்கர் வலியுறுத்தினார்.",
        "Correct. Fundamental in governance means moral and policy duty on Executive and Legislature in law-making.", "சரி. ஆட்சியில் அடிப்படையானவை என்பது சட்டம் இயற்றுவதில் நிர்வாகம் மற்றும் சட்டமன்றத்தின் மீதுள்ள ஒழுக்க மற்றும் கொள்கைக் கடமையாகும்.",
        "Governor/President assent under Arts 200/201 is still required.", "உறுப்புகள் 200/201-ன் கீழ் ஆளுநர்/குடியரசுத் தலைவர் ஒப்புதல் இன்னமும் தேவைப்படுகிறது.",
        "Courts cannot impeach ministers; impeachment is a legislative/constitutional process.", "நீதிமன்றங்கள் அமைச்சர்களைப் பதவி நீக்கம் செய்ய முடியாது.",
        "DPSPs bind all levels of government including Parliament.", "DPSP நாடாளுமன்றம் உட்பட அனைத்து மட்ட அரசாங்கங்களையும் கட்டுப்படுத்துகிறது."
    )

    # -------------------------------------------------------------------------
    # Q46 (Correct: B) - Application / Inference
    # -------------------------------------------------------------------------
    add_q(
        46, "Application",
        "How does Article 39(c) (prevention of concentration of wealth) balance against Article 19(1)(g) (freedom to practice any profession/trade)?",
        "உறுப்பு 39(c) (செல்வக் குவிப்புத் தடை) எவ்வாறு உறுப்பு 19(1)(g) உடன் (தொழில்/வியாபாரம் செய்யும் சுதந்திரம்) சமநிலைப்படுகிறது?",
        "Article 19(1)(g) completely abolishes Article 39(c)", "உறுப்பு 19(1)(g) உறுப்பு 39(c)-ஐ முழுமையாக ஒழிக்கிறது",
        "Under Article 31C, laws enacted to prevent concentration of wealth under Article 39(c) are protected against challenge under Article 19(1)(g), allowing reasonable regulation of monopolies for public interest", "உறுப்பு 31C-ன் கீழ், உறுப்பு 39(c)-ன் கீழ் செல்வக் குவிப்பைத் தடுக்க இயற்றப்படும் சட்டங்கள் உறுப்பு 19(1)(g)-ன் கீழ் சவால் செய்யப்படுவதிலிருந்து பாதுகாக்கப்படுகின்றன, இது பொது நலனுக்காக ஏகபோகங்களை நியாயமாக முறைப்படுத்த அனுமதிக்கிறது",
        "Article 39(c) allows the State to confiscate all private bank accounts without any law", "உறுப்பு 39(c) எந்தவொரு சட்டமும் இல்லாமல் அனைத்துத் தனியார் வங்கி கணக்குகளையும் பறிமுதல் செய்ய அரசுக்கு அனுமதிக்கிறது",
        "Article 19(1)(g) applies only to foreign citizens operating in India", "உறுப்பு 19(1)(g) இந்தியாவில் செயல்படும் வெளிநாட்டு குடிமக்களுக்கு மட்டுமே பொருந்தும்",
        "B",
        "Article 31C expressly protects laws giving effect to Article 39(c) (preventing concentration of wealth) from being declared void under Article 19. This empowers Parliament to pass anti-monopoly laws (like MRTP Act / Competition Act) and nationalization laws for common welfare.",
        "உறுப்பு 39(c)-ஐ (செல்வக் குவிப்பைத் தடுத்தல்) செயல்படுத்தும் சட்டங்களை உறுப்பு 19-ன் கீழ் செல்லாததாக அறிவிக்கப்படுவதிலிருந்து உறுப்பு 31C வெளிப்படையாகப் பாதுகாக்கிறது. இது ஏகபோக எதிர்ப்புச் சட்டங்களையும் பொது நலனுக்கான தேசியமயமாக்கல் சட்டங்களையும் இயற்ற நாடாளுமன்றத்திற்கு அதிகாரமளிக்கிறது.",
        "Monopolies and Restrictive Trade Practices (MRTP) Act 1969 was enacted under Article 39(c) principles.", "ஏகபோகங்கள் மற்றும் வர்த்தகத் தடை நடைமுறைகள் (MRTP) சட்டம் 1969 உறுப்பு 39(c) கோட்பாடுகளின் கீழ் இயற்றப்பட்டது.",
        "Article 19(1)(g) does not abolish Article 39(c); Article 31C gives precedence to Article 39(c).", "உறுப்பு 19(1)(g) உறுப்பு 39(c)-ஐ ஒழிக்கவில்லை; உறுப்பு 31C உறுப்பு 39(c)-க்கு முன்னுரிமை அளிக்கிறது.",
        "Correct. Art 31C protects Art 39(c) laws preventing wealth concentration against Art 19 challenges.", "சரி. உறுப்பு 31C செல்வக் குவிப்பைத் தடுக்கும் 39(c) சட்டங்களை உறுப்பு 19 சவால்களிலிருந்து பாதுகாக்கிறது.",
        "Confiscation requires authority of law under Article 300A.", "பறிமுதல் செய்வதற்கு உறுப்பு 300A-ன் கீழ் சட்ட அதிகாரம் தேவை.",
        "Article 19(1)(g) applies to Indian citizens.", "உறுப்பு 19(1)(g) இந்தியக் குடிமக்களுக்குப் பொருந்தும்."
    )

    # -------------------------------------------------------------------------
    # Q47 (Correct: C) - Basic Structure
    # -------------------------------------------------------------------------
    add_q(
        47, "Conceptual",
        "Why can Parliament NOT repeal Part IV (Directive Principles) entirely using its constituent amending power under Article 368?",
        "உறுப்பு 368-ன் கீழ் உள்ள தனது அரசியலமைப்புத் திருத்தும் அதிகாரத்தைப் பயன்படுத்தி நாடாளுமன்றம் ஏன் பகுதி IV-ஐ (வழிகாட்டு நெறிமுறைகள்) முழுமையாக ரத்து செய்ய முடியாது?",
        "Because Part IV was written by the British Parliament and cannot be changed", "ஏனெனில் பகுதி IV பிரிட்டிஷ் நாடாளுமன்றத்தால் எழுதப்பட்டது, அதை மாற்ற முடியாது",
        "Because Article 368 strictly forbids adding any new articles to the Constitution", "ஏனெனில் உறுப்பு 368 அரசியலமைப்பில் புதிய உறுப்புகளைச் சேர்ப்பதைக் கண்டிப்பாகத் தடுக்கிறது",
        "Because Part IV forms an essential element of the Welfare State framework and the balance between Part III and Part IV is a Basic Feature of the Constitution (Minerva Mills 1980)", "ஏனெனில் பகுதி IV நல அரசு கட்டமைப்பின் அத்தியாவசிய அம்சத்தை உருவாக்குகிறது மற்றும் பகுதி III மற்றும் பகுதி IV இடையிலான சமநிலையே அரசியலமைப்பின் அடிப்படை அம்சமாகும் (மினர்வா மில்ஸ் 1980)",
        "Because Part IV applies only to Union Territories and not to Parliament", "ஏனெனில் பகுதி IV நாடாளுமன்றத்திற்கு அல்லாமல் யூனியன் பிரதேசங்களுக்கு மட்டுமே பொருந்தும்",
        "C",
        "In Kesavananda Bharati (1973) and Minerva Mills (1980), the SC established that Parliament's amending power under Article 368 is limited by the Basic Structure Doctrine. Since the Welfare State goal and the harmony between Fundamental Rights and DPSPs constitute Basic Features, repealing Part IV would destroy the constitutional identity.",
        "கேசவானந்த பாரதி (1973) மற்றும் மினர்வா மில்ஸ் (1980) வழக்குகளில், உறுப்பு 368-ன் கீழ் நாடாளுமன்றத்தின் திருத்தும் அதிகாரம் அடிப்படை அமைப்புக் கோட்பாட்டால் வரம்பிற்குட்படுத்தப்பட்டுள்ளது என SC நிறுவியது. நல அரசு இலக்கும் FR மற்றும் DPSP இடையிலான இணக்கமும் அடிப்படை அம்சங்களாக இருப்பதால், பகுதி IV-ஐ ரத்து செய்வது அரசியலமைப்பு அடையாளத்தைச் சிதைத்துவிடும்.",
        "Basic Structure Doctrine protects core constitutional identity from being destroyed by amendments.", "அடிப்படை அமைப்புக் கோட்பாடு முதன்மை அரசியலமைப்பு அடையாளத்தைத் திருத்தங்களால் சிதைக்கப்படுவதிலிருந்து பாதுகாக்கிறது.",
        "Part IV was framed by India's Constituent Assembly, not British Parliament.", "பகுதி IV இந்தியாவின் அரசியலமைப்பு நிர்ணய சபையால் வரைவு செய்யப்பட்டது.",
        "Article 368 permits constitutional amendments that do not violate Basic Structure.", "உறுப்பு 368 அடிப்படை அமைப்பை மீறாத அரசியலமைப்பு திருத்தங்களை அனுமதிக்கிறது.",
        "Correct. Repealing Part IV destroys Welfare State architecture and Part III-IV balance which is Basic Feature.", "சரி. பகுதி IV-ஐ ரத்து செய்வது நல அரசு கட்டமைப்பையும் அடிப்படை அம்சமான பகுதி III-IV சமநிலையையும் சிதைக்கும்.",
        "Part IV binds all levels of Indian governance.", "பகுதி IV இந்திய ஆட்சியின் அனைத்து மட்டங்களையும் கட்டுப்படுத்துகிறது."
    )

    # -------------------------------------------------------------------------
    # Q48 (Correct: D) - Simple Comparison
    # -------------------------------------------------------------------------
    add_q(
        48, "Comparison",
        "Compare Article 49 (Monuments Protection DPSP) with Article 51A(f) (Composite Culture FD).",
        "உறுப்பு 49-ஐ (நினைவிடங்கள் பாதுகாப்பு DPSP) உறுப்பு 51A(f)-உடன் (கூட்டுப் பண்பாடு FD) ஒப்பிடுக.",
        "Article 49 applies to citizens; Article 51A(f) applies to the State", "உறுப்பு 49 குடிமக்களுக்குப் பொருந்தும்; உறுப்பு 51A(f) அரசுக்குப் பொருந்தும்",
        "Article 49 deals with agriculture; Article 51A(f) deals with international arbitration", "உறுப்பு 49 விவசாயம் பற்றியது; உறுப்பு 51A(f) சர்வதேச நடுவர் மன்றம் பற்றியது",
        "Article 49 was added by 86th Amendment; Article 51A(f) was in original 1950 text", "உறுப்பு 49 86வது திருத்தத்தால் சேர்க்கப்பட்டது; உறுப்பு 51A(f) அசல் 1950 உரையில் இருந்தது",
        "Article 49 (Part IV DPSP) directs the STATE to protect physical monuments and historic places of national importance; Article 51A(f) (Part IV-A FD) imposes a duty on CITIZENS to value and preserve the rich heritage of composite culture", "உறுப்பு 49 (பகுதி IV DPSP) தேசிய முக்கியத்துவம் வாய்ந்த பௌதிக நினைவிடங்கள் மற்றும் வரலாற்று இடங்களைப் பாதுகாக்க அரசுக்கு வழிகாட்டுகிறது; உறுப்பு 51A(f) (பகுதி IV-A FD) கூட்டுப் பண்பாட்டின் வளமான பாரம்பரியத்தை மதித்து பேணிப் பாதுகாக்கக் குடிமக்களுக்குக் கடமையை விதிக்கிறது",
        "D",
        "Article 49 is a State DPSP directing legislative/executive action to protect physical monuments, historical buildings, and artistic objects declared by Parliament. Article 51A(f) is a Citizen Fundamental Duty commanding individual citizens to value and preserve India's rich heritage of composite culture (சமஸ்கிருதி / பண்பாடு).",
        "உறுப்பு 49 என்பது நாடாளுமன்றத்தால் அறிவிக்கப்பட்ட பௌதிக நினைவிடங்கள், வரலாற்றுச் சின்னங்கள் மற்றும் கலைப் பொருட்களைப் பாதுகாக்கச் சட்டமன்ற/நிர்வாக நடவடிக்கைக்கு வழிகாட்டும் அரசு DPSP ஆகும். உறுப்பு 51A(f) என்பது இந்தியாவின் கூட்டுப் பண்பாட்டின் வளமான பாரம்பரியத்தை மதித்து பேணிப் பாதுகாக்கத் தனிப்பட்ட குடிமக்களுக்கு ஆணையிடும் அடிப்படைக் கடமையாகும்.",
        "Article 49 focuses on tangible physical monuments; Article 51A(f) focuses on intangible composite culture.", "உறுப்பு 49 பௌதிக நினைவிடங்கள் மீது கவனம் செலுத்துகிறது; உறுப்பு 51A(f) அருவமான கூட்டுப் பண்பாடு மீது கவனம் செலுத்துகிறது.",
        "Incorrect reversal: 49 is State DPSP; 51A(f) is Citizen FD.", "தவறான தலைகீழ் கூற்று: 49 அரசு DPSP; 51A(f) குடிமகன் FD.",
        "Monuments protection is 49; arbitration is 51(d).", "நினைவிடங்கள் பாதுகாப்பு 49; நடுவர் மன்றம் 51(d).",
        "49 was in 1950 original text; 51A(f) was added by 42nd Amendment in 1976.", "49 1950 அசல் உரையில் இருந்தது; 51A(f) 1976-ன் 42வது திருத்தத்தால் சேர்க்கப்பட்டது.",
        "Correct. 49 is State directive protecting physical national monuments; 51A(f) is citizen duty preserving composite culture.", "சரி. 49 பௌதிக தேசிய நினைவிடங்களைப் பாதுகாக்கும் அரசு வழிகாட்டல்; 51A(f) கூட்டுப் பண்பாட்டைப் பாதுகாக்கும் குடிமகன் கடமை."
    )

    # -------------------------------------------------------------------------
    # Q49 (Correct: A) - Application / Inference
    # -------------------------------------------------------------------------
    add_q(
        49, "Application",
        "Which clause of Article 51 explicitly directs the State to 'encourage settlement of international disputes by arbitration'?",
        "சர்வதேச தகராறுகளை நடுவர் மன்றம் (Arbitration) மூலம் அமைதியான முறையில் தீர்ப்பதை ஊக்குவிக்க அரசுக்கு வெளிப்படையாக ஆணையிடும் உறுப்பு 51-ன் உட்பிரிவு எது?",
        "Article 51(d)", "உறுப்பு 51(d)",
        "Article 51(a)", "உறுப்பு 51(a)",
        "Article 51(b)", "உறுப்பு 51(b)",
        "Article 51(c)", "உறுப்பு 51(c)",
        "A",
        "Article 51 contains four sub-clauses: 51(a) promote international peace & security; 51(b) maintain just & honourable national relations; 51(c) foster respect for international law & treaty obligations; 51(d) encourage settlement of international disputes by arbitration.",
        "உறுப்பு 51 நான்கு உட்பிரிவுகளைக் கொண்டுள்ளது: 51(a) சர்வதேச அமைதி & பாதுகாப்பை மேம்படுத்துதல்; 51(b) நியாயமான & கெளரவமான தேசிய உறவுகளைப் பேணுதல்; 51(c) சர்வதேச சட்டம் & ஒப்பந்தங்களுக்கு மரியாதையை வளர்த்தல்; 51(d) சர்வதேச தகராறுகளை நடுவர் மன்றம் மூலம் தீர்ப்பதை ஊக்குவித்தல்.",
        "Arbitration Act 1996 and International Commercial Arbitration frameworks align with Article 51(d).", "நடுவர் மன்றச் சட்டம் 1996 மற்றும் சர்வதேச வர்த்தக நடுவர் மன்றக் கட்டமைப்பு உறுப்பு 51(d)-உடன் இணைகின்றன.",
        "Correct. Article 51(d) explicitly mandates arbitration for international dispute settlement.", "சரி. உறுப்பு 51(d) சர்வதேச தகராறு தீர்விற்காக நடுவர் மன்றத்தை வெளிப்படையாகக் கட்டாயமாக்குகிறது.",
        "Article 51(a) deals with international peace and security.", "உறுப்பு 51(a) சர்வதேச அமைதி மற்றும் பாதுகாப்பு பற்றியது.",
        "Article 51(b) deals with just and honourable relations.", "உறுப்பு 51(b) நியாயமான மற்றும் கெளரவமான உறவுகள் பற்றியது.",
        "Article 51(c) deals with respect for international law and treaty obligations.", "உறுப்பு 51(c) சர்வதேச சட்டம் மற்றும் ஒப்பந்தக் கடமைகள் பற்றியது."
    )

    # -------------------------------------------------------------------------
    # Q50 (Correct: B) - TNPSC Trap
    # -------------------------------------------------------------------------
    add_q(
        50, "TNPSC Trap",
        "Consider the statement: 'Since Directive Principles are non-justiciable under Article 37, any law passed by Parliament to implement a Directive Principle that violates a Fundamental Right is invalid, EXCEPT laws implementing Article 39(b) and 39(c).' Is this statement CORRECT?",
        "'உறுப்பு 37-ன் கீழ் வழிகாட்டு நெறிமுறைகள் அமல்படுத்த முடியாதவை என்பதால், உறுப்பு 39(b) மற்றும் 39(c)-ஐ செயல்படுத்தும் சட்டங்களைத் தவிர, அடிப்படை உரிமையை மீறும் வகையில் DPSP-ஐச் செயல்படுத்த நாடாளுமன்றத்தால் இயற்றப்படும் எந்தவொரு சட்டமும் செல்லாததாகும்.' இந்தக் கூற்று சரியா?",
        "No. All Directive Principles override Fundamental Rights post-42nd Amendment", "இல்லை. 42வது திருத்தத்திற்குப் பின் அனைத்து வழிகாட்டு நெறிமுறைகளும் அடிப்படை உரிமைகளை மிஞ்சுகின்றன",
        "Yes. Following Minerva Mills (1980), general Fundamental Rights have primacy over DPSPs, and ONLY laws implementing Article 39(b) and Article 39(c) are protected under Article 31C from Articles 14 and 19", "ஆம். மினர்வா மில்ஸுக்குப் பின் (1980), பொதுவான அடிப்படை உரிமைகளுக்கே DPSP-களை விட முதன்மை உண்டு, மற்றும் உறுப்பு 39(b) மற்றும் உறுப்பு 39(c)-ஐ செயல்படுத்தும் சட்டங்கள் மட்டுமே உறுப்பு 31C-ன் கீழ் உறுப்புகள் 14 மற்றும் 19-லிருந்து பாதுகாக்கப்படுகின்றன",
        "No. Directive Principles can never conflict with Fundamental Rights in any situation", "இல்லை. வழிகாட்டு நெறிமுறைகள் எந்தவொரு சூழ்நிலையிலும் அடிப்படை உரிமைகளுடன் மோத முடியாது",
        "Yes, but only if the law is approved by the United Nations General Assembly", "ஆம், ஆனால் சட்டம் ஐக்கிய நாடுகள் பொதுச் சபையால் அங்கீகரிக்கப்பட்டால் மட்டுமே",
        "B",
        "In Minerva Mills (1980), SC invalidated the 42nd Amendment's attempt to extend 31C protection to ALL DPSPs. Thus, the present legal position is: FRs generally prevail over DPSPs, EXCEPT that laws giving effect to Article 39(b) and Article 39(c) take precedence over Article 14 (Equality) and Article 19 (Freedoms).",
        "மினர்வா மில்ஸ் வழக்கில் (1980), அனைத்து DPSP-களுக்கும் 31C பாதுகாப்பை நீட்டிக்க முயன்ற 42வது திருத்தத்தின் முயற்சியை SC ரத்து செய்தது. எனவே தற்போதைய சட்ட நிலை என்னவெனில்: DPSP-களை விட பொதுவான FR-களுக்கே முதன்மை உண்டு, ஆனால் உறுப்பு 39(b) மற்றும் உறுப்பு 39(c)-ஐ செயல்படுத்தும் சட்டங்கள் மட்டுமே உறுப்பு 14 (சமத்துவம்) மற்றும் உறுப்பு 19 (சுதந்திரங்கள்) ஆகியவற்றை விட முதன்மை பெறுகின்றன.",
        "TNPSC Trap: Remember that ONLY 39(b) and 39(c) enjoy Article 31C protection against Articles 14 and 19. All other DPSPs must conform to Part III Rights.",
        "டிஎன்பிஎஸ்சி பொறி: உறுப்புகள் 14 மற்றும் 19-க்கு எதிராக 39(b) மற்றும் 39(c) மட்டுமே உறுப்பு 31C பாதுகாப்பைப் பெறுகின்றன என்பதை நினைவில் கொள்க. மற்ற அனைத்து DPSP-களும் பகுதி III உரிமைகளுக்குக் கட்டுப்பட வேண்டும்.",
        "42nd Amendment extension of 31C to all DPSPs was struck down in Minerva Mills 1980.", "அனைத்து DPSP-களுக்கும் 31C-ஐ நீட்டித்த 42வது திருத்தம் மினர்வா மில்ஸ் 1980-ல் ரத்து செய்யப்பட்டது.",
        "Correct. General FRs prevail over DPSPs, EXCEPT laws implementing Art 39(b)/(c) protected under Art 31C.", "சரி. உறுப்பு 31C-ன் கீழ் பாதுகாக்கப்பட்ட 39(b)/(c) சட்டங்களைத் தவிர, பொதுவான FR-களே DPSP-களை விட மேலோங்குகின்றன.",
        "Conflicts have occurred and led to landmark constitutional amendments/cases.", "மோதல்கள் ஏற்பட்டு முக்கிய அரசியலமைப்பு திருத்தங்கள்/வழக்குகளுக்கு வழிவகுத்துள்ளன.",
        "UN Assembly approval is irrelevant to Indian domestic constitutional validity.", "ஐ.நா சபை அங்கீகாரம் இந்திய உள்நாட்டு அரசியலமைப்பு செல்லுபடித்ன்மைக்குத் தொடர்பற்றது."
    )

    output_dir = "data/questions/polity"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "directive_principles_medium.json")

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)

    print(f"Successfully generated {len(questions)} DPSP Medium MCQs at {output_path}")

    counts = {"A": 0, "B": 0, "C": 0, "D": 0}
    for q in questions:
        counts[q["correct_answer"]] += 1
    print(f"Answer Key Distribution: A={counts['A']}, B={counts['B']}, C={counts['C']}, D={counts['D']}")

if __name__ == "__main__":
    generate_50_medium_mcqs()
