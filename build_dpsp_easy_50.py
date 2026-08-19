# build_dpsp_easy_50.py
# Generates 50 Easy MCQs for Directive Principles of State Policy (DPSP)
# Target file: data/questions/polity/directive_principles_easy.json

import json
import os

def generate_50_easy_mcqs():
    questions = []

    # Helper function to append question with validation
    def add_q(q_id, q_type, q_en, q_ta, opt_a_en, opt_a_ta, opt_b_en, opt_b_ta, opt_c_en, opt_c_ta, opt_d_en, opt_d_ta, correct, exp_en, exp_ta, tip_en, tip_ta, w_a_en, w_a_ta, w_b_en, w_b_ta, w_c_en, w_c_ta, w_d_en, w_d_ta):
        q_obj = {
            "id": f"DPSP_E_{q_id:03d}",
            "subject": "Polity",
            "topic": "Directive Principles of State Policy",
            "difficulty": "Easy",
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
    # Q1 (Correct: A) - Direct Factual
    # -------------------------------------------------------------------------
    add_q(
        1, "Direct",
        "Which Part of the Constitution of India contains the Directive Principles of State Policy (DPSP)?",
        "இந்திய அரசியலமைப்பின் எந்தப் பகுதியில் அரசு வழிகாட்டு நெறிமுறைகள் (DPSP) இடம்பெற்றுள்ளன?",
        "Part IV (Articles 36 to 51)", "பகுதி IV (உறுப்புகள் 36 முதல் 51)",
        "Part III (Articles 12 to 35)", "பகுதி III (உறுப்புகள் 12 முதல் 35)",
        "Part IV-A (Article 51A)", "பகுதி IV-A (உறுப்பு 51A)",
        "Part V (Articles 52 to 151)", "பகுதி V (உறுப்புகள் 52 முதல் 151)",
        "A",
        "Part IV of the Constitution, comprising Articles 36 to 51, contains the Directive Principles of State Policy.",
        "உறுப்புகள் 36 முதல் 51 வரையிலான அரசியலமைப்பின் பகுதி IV அரசு வழிகாட்டு நெறிமுறைகளைக் கொண்டுள்ளது.",
        "DPSP was borrowed from the Irish Constitution of 1937.",
        "DPSP 1937-ன் அயர்லாந்து அரசியலமைப்பிலிருந்து பெறப்பட்டது.",
        "Correct. Part IV contains DPSP.", "சரி. பகுதி IV DPSP-ஐக் கொண்டுள்ளது.",
        "Part III deals with Fundamental Rights.", "பகுதி III அடிப்படை உரிமைகள் பற்றியது.",
        "Part IV-A deals with Fundamental Duties.", "பகுதி IV-A அடிப்படைக் கடமைகள் பற்றியது.",
        "Part V deals with The Union Government.", "பகுதி V ஒன்றிய அரசாங்கம் பற்றியது."
    )

    # -------------------------------------------------------------------------
    # Q2 (Correct: B) - Direct Factual
    # -------------------------------------------------------------------------
    add_q(
        2, "Direct",
        "From which country's constitution were the Directive Principles of State Policy borrowed by the framers of the Indian Constitution?",
        "இந்திய அரசியலமைப்பை உருவாக்கியவர்கள் அரசு வழிகாட்டு நெறிமுறைகளை எந்த நாட்டின் அரசியலமைப்பிலிருந்து பெற்றனர்?",
        "United States of America", "அமெரிக்க ஐக்கிய நாடுகள்",
        "Irish Republic (Ireland)", "அயர்லாந்து குடியரசு",
        "United Kingdom (Britain)", "ஐக்கிய இராச்சியம் (பிரிட்டன்)",
        "Soviet Union (USSR)", "சோவியத் ஒன்றியம் (USSR)",
        "B",
        "The Directive Principles of State Policy in Part IV were borrowed from the Irish Constitution of 1937 (which had copied them from the Spanish Constitution).",
        "பகுதி IV-ல் உள்ள அரசு வழிகாட்டு நெறிமுறைகள் 1937-ன் அயர்லாந்து அரசியலமைப்பிலிருந்து பெறப்பட்டவை.",
        "Ireland borrowed its Directive Principles from Spain.",
        "அயர்லாந்து தனது வழிகாட்டு நெறிமுறைகளை ஸ்பெயினிலிருந்து பெற்றது.",
        "Fundamental Rights were borrowed from the US Bill of Rights.", "அடிப்படை உரிமைகள் அமெரிக்க உரிமைகள் மசோதாவிலிருந்து பெறப்பட்டவை.",
        "Correct. DPSP was borrowed from Ireland.", "சரி. DPSP அயர்லாந்திலிருந்து பெறப்பட்டது.",
        "Parliamentary system was borrowed from Britain.", "நாடாளுமன்ற முறை பிரிட்டனிலிருந்து பெறப்பட்டது.",
        "Fundamental Duties were inspired by USSR.", "அடிப்படைக் கடமைகள் USSR-ஆல் ஈர்க்கப்பட்டவை."
    )

    # -------------------------------------------------------------------------
    # Q3 (Correct: C) - Basic Conceptual
    # -------------------------------------------------------------------------
    add_q(
        3, "Conceptual",
        "What is the primary objective of incorporating the Directive Principles of State Policy in the Constitution of India?",
        "இந்திய அரசியலமைப்பில் அரசு வழிகாட்டு நெறிமுறைகளைச் சேர்த்ததன் முதன்மை நோக்கம் என்ன?",
        "To establish a Police State with strong central authority", "கடுமையான மத்திய அதிகாரத்துடன் கூடிய காவல் அரசை நிறுவுதல்",
        "To guarantee religious supremacy to the majority community", "பெரும்பான்மை சமூகத்திற்கு மத மேலாதிக்கத்தை உத்தரவாதம் செய்தல்",
        "To establish a Welfare State and economic democracy", "ஒரு நல அரசு மற்றும் பொருளாதார ஜனநாயகத்தை நிறுவுதல்",
        "To enforce strict judicial punishment for civic defaults", "சிவில் தவறுகளுக்குக் கடுமையான நீதித்துறை தண்டனையை அமல்படுத்துதல்",
        "C",
        "The primary goal of DPSP is to establish a 'Welfare State' and achieve social and economic democracy in India.",
        "DPSP-ன் முதன்மை இலக்கு ஒரு 'நல அரசை' நிறுவுவதும் சமூக மற்றும் பொருளாதார ஜனநாயகத்தை அடைவதும் ஆகும்.",
        "Fundamental Rights establish Political Democracy; DPSP establishes Social & Economic Democracy.",
        "அடிப்படை உரிமைகள் அரசியல் ஜனநாயகத்தை நிறுவுகின்றன; DPSP சமூக & பொருளாதார ஜனநாயகத்தை நிறுவுகிறது.",
        "DPSP aims for a Welfare State, not a Police State.", "DPSP நல அரசை நோக்கமாகக் கொண்டது, காவல் அரசை அல்ல.",
        "Indian Constitution establishes a secular state, not religious supremacy.", "இந்திய அரசியலமைப்பு மதச்சார்பற்ற அரசை நிறுவுகிறது.",
        "Correct. DPSP aims for a Welfare State and socio-economic democracy.", "சரி. DPSP நல அரசு மற்றும் சமூக-பொருளாதார ஜனநாயகத்தை நோக்கமாகக் கொண்டது.",
        "DPSP directives are non-justiciable and non-punitive.", "DPSP வழிகாட்டுதல்கள் அமல்படுத்த முடியாதவை மற்றும் தண்டனையற்றவை."
    )

    # -------------------------------------------------------------------------
    # Q4 (Correct: D) - Direct Factual
    # -------------------------------------------------------------------------
    add_q(
        4, "Direct",
        "Who described the Directive Principles of State Policy as 'Novel Features' of the Constitution of India?",
        "அரசு வழிகாட்டு நெறிமுறைகளை இந்திய அரசியலமைப்பின் 'நவீன அம்சங்கள்' (Novel Features) என்று விவரித்தவர் யார்?",
        "Jawaharlal Nehru", "ஜவஹர்லால் நேரு",
        "Dr. Rajendra Prasad", "டாக்டர் இராஜேந்திர பிரசாத்",
        "Granville Austin", "கிரான்வில் ஆஸ்டின்",
        "Dr. B.R. Ambedkar", "டாக்டர் பி.ஆர். அம்பேத்கர்",
        "D",
        "Dr. B.R. Ambedkar described the Directive Principles of State Policy as 'novel features' of the Indian Constitution.",
        "டாக்டர் பி.ஆர். அம்பேத்கர் அரசு வழிகாட்டு நெறிமுறைகளை இந்திய அரசியலமைப்பின் 'நவீன அம்சங்கள்' என்று விவரித்தார்.",
        "Granville Austin called Fundamental Rights and DPSP the 'Conscience of the Constitution'.",
        "கிரான்வில் ஆஸ்டின் அடிப்படை உரிமைகள் மற்றும் DPSP-ஐ 'அரசியலமைப்பின் மனசாட்சி' என்று அழைத்தார்.",
        "Nehru framed the Objectives Resolution.", "நேரு குறிக்கோள்கள் தீர்மானத்தை வரைந்தார்.",
        "Dr. Rajendra Prasad was President of Constituent Assembly.", "டாக்டர் இராஜேந்திர பிரசாத் அரசியலமைப்பு நிர்ணய சபையின் தலைவராக இருந்தார்.",
        "Granville Austin called them 'Conscience of the Constitution'.", "கிரான்வில் ஆஸ்டின் இவற்றை 'அரசியலமைப்பின் மனசாட்சி' என்றார்.",
        "Correct. Dr. B.R. Ambedkar called DPSP 'Novel Features'.", "சரி. டாக்டர் பி.ஆர். அம்பேத்கர் DPSP-ஐ 'நவீன அம்சங்கள்' என்றார்."
    )

    # -------------------------------------------------------------------------
    # Q5 (Correct: A) - Article-based
    # -------------------------------------------------------------------------
    add_q(
        5, "Article-based",
        "Which Article of the Constitution states that Directive Principles are non-justiciable in courts but fundamental in governance?",
        "வழிகாட்டு நெறிமுறைகள் நீதிமன்றங்களால் அமல்படுத்த முடியாதவை, ஆனால் ஆட்சியில் அடிப்படையானவை எனக் கூறும் அரசியலமைப்பு உறுப்பு எது?",
        "Article 37", "உறுப்பு 37",
        "Article 36", "உறுப்பு 36",
        "Article 38", "உறுப்பு 38",
        "Article 39", "உறுப்பு 39",
        "A",
        "Article 37 explicitly states that DPSPs shall not be enforceable by any court, but the principles laid down are fundamental in the governance of the country.",
        "உறுப்பு 37 DPSP-கள் நீதிமன்றங்களால் அமல்படுத்தப்படாது, ஆனால் நாட்டின் ஆட்சியில் அவை அடிப்படையானவை என வெளிப்படையாகக் கூறுகிறது.",
        "Non-justiciable means a citizen cannot file a writ petition in court claiming non-implementation of DPSP.",
        "அமல்படுத்த முடியாதது என்றால் DPSP செயல்படவில்லை எனச் சொல்லி நீதிமன்றத்தில் பேராணை மனு தாக்கல் செய்ய முடியாது.",
        "Correct. Article 37 declares DPSP non-justiciable but fundamental in governance.", "சரி. உறுப்பு 37 DPSP நீதிமன்றங்களால் அமல்படுத்த முடியாதது, ஆனால் ஆட்சியில் அடிப்படையானது என்கிறது.",
        "Article 36 defines the 'State' for Part IV.", "உறுப்பு 36 பகுதி IV-க்கான 'அரசை' வரையறுக்கிறது.",
        "Article 38 directs State to secure a social order for welfare of people.", "உறுப்பு 38 மக்கள் நலனுக்கான சமூக ஒழுங்கை உருவாக்க அரசுக்கு ஆணையிடுகிறது.",
        "Article 39 outlines specific policy principles.", "உறுப்பு 39 குறிப்பிட்ட கொள்கைக் கோட்பாடுகளை விவரிக்கிறது."
    )

    # -------------------------------------------------------------------------
    # Q6 (Correct: B) - Simple Comparison
    # -------------------------------------------------------------------------
    add_q(
        6, "Comparison",
        "How does Article 36 of Part IV define the term 'State'?",
        "பகுதி IV-ல் உள்ள உறுப்பு 36 'அரசு' என்ற சொல்லை எவ்வாறு வரையறுக்கிறது?",
        "It provides a completely new definition unrelated to Part III", "பகுதி III உடன் தொடர்பில்லாத முற்றிலும் புதிய வரையறையை வழங்குகிறது",
        "It adopts the exact same meaning of 'State' as defined in Article 12 of Part III", "பகுதி III உறுப்பு 12-ல் வரையறுக்கப்பட்டுள்ள அதே பொருளைப் பெறுகிறது",
        "It restricts the term 'State' only to the Parliament of India", "இது 'அரசு' என்ற சொல்லை இந்திய நாடாளுமன்றத்திற்கு மட்டுமே சுருக்குகிறது",
        "It excludes state legislative assemblies from the definition", "இது மாநில சட்டமன்றங்களை வரையறையிலிருந்து விலக்குகிறது",
        "B",
        "Article 36 states that unless the context otherwise requires, 'the State' has the same meaning as in Part III (Article 12).",
        "உறுப்பு 36 சூழல் வேறுவிதமாகக் கோரினாலன்றி, 'அரசு' என்பது பகுதி III-ல் (உறுப்பு 12) உள்ள அதே பொருளைக் கொண்டது எனக் கூறுகிறது.",
        "Both Part III (Art 12) and Part IV (Art 36) share the same 4-tier definition of State.",
        "பகுதி III (உறுப்பு 12) மற்றும் பகுதி IV (உறுப்பு 36) ஆகிய இரண்டும் அரசின் ஒரே 4-அடுக்கு வரையறையைப் பகிர்ந்து கொள்கின்றன.",
        "Article 36 does not provide a new separate definition.", "உறுப்பு 36 புதிய தனி வரையறையை வழங்கவில்லை.",
        "Correct. Article 36 adopts the definition of State given in Article 12.", "சரி. உறுப்பு 36, உறுப்பு 12-ல் கொடுக்கப்பட்ட அரசு வரையறையை ஏற்கிறது.",
        "State includes Parliament, State Legislatures, Local and Other Authorities.", "அரசு என்பதில் நாடாளுமன்றம், மாநில சட்டமன்றங்கள், உள்ளாட்சி மற்றும் இதர அமைப்புகள் அடங்கும்.",
        "State Assemblies are explicitly included under Article 12/36.", "மாநில சட்டமன்றங்கள் உறுப்பு 12/36-ன் கீழ் வெளிப்படையாகச் சேர்க்கப்பட்டுள்ளன."
    )

    # -------------------------------------------------------------------------
    # Q7 (Correct: C) - Article-based
    # -------------------------------------------------------------------------
    add_q(
        7, "Article-based",
        "Clause (2) of Article 38, directing the State to minimise inequalities in income, status, facilities, and opportunities, was added by which Constitutional Amendment Act?",
        "வருமானம், அந்தஸ்து, வசதிகள் மற்றும் வாய்ப்புகளில் உள்ள சமத்துவமின்மையைக் குறைக்க அரசுக்கு ஆணையிடும் உறுப்பு 38(2), எந்த அரசியலமைப்பு திருத்தச் சட்டத்தால் சேர்க்கப்பட்டது?",
        "42nd Constitutional Amendment Act, 1976", "42வது அரசியலமைப்பு திருத்தச் சட்டம், 1976",
        "44th Constitutional Amendment Act, 1978", "44வது அரசியலமைப்பு திருத்தச் சட்டம், 1978",
        "44th Constitutional Amendment Act, 1978", "44வது அரசியலமைப்பு திருத்தச் சட்டம், 1978",
        "86th Constitutional Amendment Act, 2002", "86வது அரசியலமைப்பு திருத்தச் சட்டம், 2002",
        "C",
        "Article 38(2) was inserted by the 44th Constitutional Amendment Act, 1978, directing the State to minimise inequalities in income, status, facilities, and opportunities.",
        "44வது அரசியலமைப்பு திருத்தச் சட்டம், 1978 மூலம் உறுப்பு 38(2) இணைக்கப்பட்டது.",
        "Remember: 42nd Amendment added 39A, 39(f), 43A, 48A; 44th Amendment added 38(2).",
        "நினைவில் கொள்க: 42வது திருத்தம் 39A, 39(f), 43A, 48A-ஐச் சேர்த்தது; 44வது திருத்தம் 38(2)-ஐச் சேர்த்தது.",
        "42nd Amendment added 39A, 39(f), 43A, and 48A.", "42வது திருத்தம் 39A, 39(f), 43A மற்றும் 48A-ஐச் சேர்த்தது.",
        "Incorrect amendment year.", "தவறான திருத்த ஆண்டு.",
        "Correct. 44th Constitutional Amendment Act, 1978 inserted Article 38(2).", "சரி. 44வது அரசியலமைப்பு திருத்தச் சட்டம், 1978 உறுப்பு 38(2)-ஐ இணைத்தது.",
        "86th Amendment 2002 substituted Article 45 and inserted Article 21A.", "86வது திருத்தம் 2002 உறுப்பு 45-ஐ மாற்றியமைத்து உறுப்பு 21A-ஐ இணைத்தது."
    )

    # -------------------------------------------------------------------------
    # Q8 (Correct: D) - Direct Factual
    # -------------------------------------------------------------------------
    add_q(
        8, "Direct",
        "Which clause of Article 39 directs the State to secure 'Equal pay for equal work for both men and women'?",
        "ஆண், பெண் இருபாலருக்கும் 'சம வேலைக்கு சம ஊதியம்' வழங்குவதை உறுதி செய்ய அரசுக்கு ஆணையிடும் உறுப்பு 39-ன் உட்பிரிவு எது?",
        "Article 39(a)", "உறுப்பு 39(a)",
        "Article 39(b)", "உறுப்பு 39(b)",
        "Article 39(c)", "உறுப்பு 39(c)",
        "Article 39(d)", "உறுப்பு 39(d)",
        "D",
        "Article 39(d) directs the State to secure that there is equal pay for equal work for both men and women (statutorily enacted via Equal Remuneration Act 1976).",
        "உறுப்பு 39(d) ஆண், பெண் இருபாலருக்கும் சம வேலைக்கு சம ஊதியம் வழங்குவதை உறுதி செய்ய அரசுக்கு ஆணையிடுகிறது.",
        "Randhir Singh v. Union of India (1982) held Equal Pay for Equal Work is a constitutional goal under Art 39(d).",
        "ரந்தீர் சிங் வழக்கில் (1982) சம வேலைக்கு சம ஊதியம் என்பது உறுப்பு 39(d)-ன் கீழ் அரசியலமைப்பு இலக்கு எனத் தீர்ப்பளிக்கப்பட்டது.",
        "Article 39(a) covers adequate means of livelihood.", "உறுப்பு 39(a) போதுமான வாழ்வாதார வழிகளைக் குறிக்கிறது.",
        "Article 39(b) covers material resources distribution.", "உறுப்பு 39(b) பொருள் வளப் பகிர்வைக் குறிக்கிறது.",
        "Article 39(c) covers prevention of wealth concentration.", "உறுப்பு 39(c) செல்வக் குவிப்புத் தடையைக் குறிக்கிறது.",
        "Correct. Article 39(d) mandates Equal Pay for Equal Work.", "சரி. உறுப்பு 39(d) சம வேலைக்கு சம ஊதியத்தைக் கட்டாயமாக்குகிறது."
    )

    # -------------------------------------------------------------------------
    # Q9 (Correct: A) - Amendment / Case
    # -------------------------------------------------------------------------
    add_q(
        9, "Amendment/Case",
        "Article 39A (Equal Justice and Free Legal Aid) was added to Part IV by which Constitutional Amendment Act?",
        "உறுப்பு 39A (சம நீதியும் இலவச சட்ட உதவியும்) எந்த அரசியலமைப்பு திருத்தச் சட்டத்தின் மூலம் பகுதி IV-ல் சேர்க்கப்பட்டது?",
        "42nd Constitutional Amendment Act, 1976", "42வது அரசியலமைப்பு திருத்தச் சட்டம், 1976",
        "44th Constitutional Amendment Act, 1978", "44வது அரசியலமைப்பு திருத்தச் சட்டம், 1978",
        "73rd Constitutional Amendment Act, 1992", "73வது அரசியலமைப்பு திருத்தச் சட்டம், 1992",
        "86th Constitutional Amendment Act, 2002", "86வது அரசியலமைப்பு திருத்தச் சட்டம், 2002",
        "A",
        "Article 39A was added by the 42nd Constitutional Amendment Act, 1976 to provide equal justice and free legal aid to the poor.",
        "ஏழைகளுக்குச் சம நீதியும் இலவச சட்ட உதவியும் வழங்க 1976-ன் 42வது அரசியலமைப்பு திருத்தச் சட்டத்தால் உறுப்பு 39A சேர்க்கப்பட்டது.",
        "Parliament enacted Legal Services Authorities Act 1987 (NALSA) to fulfill Article 39A.",
        "உறுப்பு 39A-ஐ நிறைவேற்ற நாடாளுமன்றம் 1987-ல் சட்டப் பணிகள் ஆணைக்குழுக்கள் சட்டத்தை (NALSA) இயற்றியது.",
        "Correct. 42nd Amendment Act 1976 inserted Article 39A.", "சரி. 42வது திருத்தச் சட்டம் 1976 உறுப்பு 39A-ஐ இணைத்தது.",
        "44th Amendment added Article 38(2).", "44வது திருத்தம் உறுப்பு 38(2)-ஐச் சேர்த்தது.",
        "73rd Amendment gave constitutional status to Panchayats.", "73வது திருத்தம் பஞ்சாயத்துகளுக்கு அரசியலமைப்பு அந்தஸ்து வழங்கியது.",
        "86th Amendment substituted Article 45 and inserted Article 21A.", "86வது திருத்தம் உறுப்பு 45-ஐ மாற்றியமைத்து உறுப்பு 21A-ஐ இணைத்தது."
    )

    # -------------------------------------------------------------------------
    # Q10 (Correct: B) - Article-based
    # -------------------------------------------------------------------------
    add_q(
        10, "Article-based",
        "Which Article of the Constitution directs the State to organize Village Panchayats and endow them with powers of self-government?",
        "கிராம ஊராட்சிகளை அமைத்து அவற்றிற்கு சுயஆட்சி அதிகாரங்களை வழங்க அரசுக்கு ஆணையிடும் அரசியலமைப்பு உறுப்பு எது?",
        "Article 39", "உறுப்பு 39",
        "Article 40", "உறுப்பு 40",
        "Article 41", "உறுப்பு 41",
        "Article 42", "உறுப்பு 42",
        "B",
        "Article 40 directs the State to organize village panchayats and endow them with such powers and authority as may be necessary to function as units of self-government.",
        "உறுப்பு 40 கிராம ஊராட்சிகளை அமைத்து அவை சுயஆட்சி அலகுகளாகச் செயல்படத் தேவையான அதிகாரங்களை வழங்க அரசுக்கு ஆணையிடுகிறது.",
        "Article 40 embodies Mahatma Gandhi's dream of Gram Swaraj.",
        "உறுப்பு 40 மகாத்மா காந்தியின் கிராம சுயராஜ்யக் கனவை வெளிப்படுத்துகிறது.",
        "Article 39 deals with economic policy principles.", "உறுப்பு 39 பொருளாதாரக் கொள்கைக் கோட்பாடுகள் பற்றியது.",
        "Correct. Article 40 deals with Village Panchayats.", "சரி. உறுப்பு 40 கிராம ஊராட்சிகள் பற்றியது.",
        "Article 41 deals with Right to work, education, and public assistance.", "உறுப்பு 41 வேலை, கல்வி, பொது உதவி உரிமை பற்றியது.",
        "Article 42 deals with humane work conditions and maternity relief.", "உறுப்பு 42 மனிதத்தன்மை வேலை நிலைமைகள் மற்றும் பேறுகால உதவி பற்றியது."
    )

    # -------------------------------------------------------------------------
    # Q11 (Correct: C) - Basic Conceptual
    # -------------------------------------------------------------------------
    add_q(
        11, "Conceptual",
        "Under Article 41, the Right to Work, Education, and Public Assistance is qualified by which express constitutional condition?",
        "உறுப்பு 41-ன் கீழ் வேலை, கல்வி மற்றும் பொது உதவி பெறும் உரிமை எந்த வெளிப்படையான அரசியலமைப்பு நிபந்தனையால் கட்டுப்படுத்தப்படுகிறது?",
        "Absolute mandatory enforcement within 5 years of independence", "சுதந்திரம் அடைந்த 5 ஆண்டுகளுக்குள் முற்றுமுழுதான கட்டாய அமலாக்கம்",
        "Subject to approval by the Supreme Court of India", "இந்திய உச்ச நீதிமன்றத்தின் ஒப்புதலுக்கு உட்பட்டது",
        "Within the limits of the State's economic capacity and development", "அரசின் பொருளாதாரத் திறன் மற்றும் வளர்ச்சியின் வரம்புகளுக்கு உட்பட்டது",
        "Applicable only to citizens living in rural Union Territories", "யூனியன் பிரதேச கிராமப்புறங்களில் வாழும் குடிமக்களுக்கு மட்டுமே பொருந்தும்",
        "C",
        "Article 41 explicitly states that the State shall make effective provision for right to work, education and public assistance 'within the limits of its economic capacity and development'.",
        "உறுப்பு 41 'தனது பொருளாதாரத் திறன் மற்றும் வளர்ச்சியின் வரம்புகளுக்குள்' வேலை, கல்வி மற்றும் பொது உதவி உரிமையை வழங்க அரசு நடவடிக்கை எடுக்க வேண்டும் எனக் வெளிப்படையாகக் கூறுகிறது.",
        "Unlike Article 21A (FR), Article 41 (DPSP) is dependent on state financial resources.",
        "உறுப்பு 21A (FR) போலன்றி, உறுப்பு 41 (DPSP) அரசின் நிதி ஆதாரங்களைச் சார்ந்ததாகும்.",
        "There was no 5-year limit under Article 41.", "உறுப்பு 41-ன் கீழ் 5 ஆண்டு வரம்பு எதுவும் இல்லை.",
        "Supreme Court approval is not required for policy planning.", "கொள்கைத் திட்டமிடலுக்கு உச்ச நீதிமன்ற ஒப்புதல் தேவையில்லை.",
        "Correct. Article 41 is subject to State economic capacity.", "சரி. உறுப்பு 41 அரசின் பொருளாதாரத் திறனுக்கு உட்பட்டது.",
        "Article 41 applies nationwide to all citizens in undeserved want.", "உறுப்பு 41 தகுதியற்ற வறுமையில் உள்ள நாடு முழுவதிலும் உள்ள அனைத்துக் குடிமக்களுக்கும் பொருந்தும்."
    )

    # -------------------------------------------------------------------------
    # Q12 (Correct: D) - Direct Factual
    # -------------------------------------------------------------------------
    add_q(
        12, "Direct",
        "Maternity relief for women workers is explicitly mentioned in which Article of Part IV?",
        "பெண் தொழிலாளர்களுக்கான பேறுகால உதவி பகுதி IV-ன் எந்த உறுப்பில் வெளிப்படையாகக் குறிப்பிடப்பட்டுள்ளது?",
        "Article 39", "உறுப்பு 39",
        "Article 40", "உறுப்பு 40",
        "Article 41", "உறுப்பு 41",
        "Article 42", "உறுப்பு 42",
        "D",
        "Article 42 states that the State shall make provision for securing just and humane conditions of work and for maternity relief.",
        "உறுப்பு 42 நியாயமான மற்றும் மனிதத்தன்மையுள்ள வேலை நிலைமைகளையும் பேறுகால உதவியையும் உறுதிசெய்ய விதிகளை உருவாக்க அரசுக்கு ஆணையிடுகிறது.",
        "Maternity Benefit Act 1961 was enacted to implement Article 42.",
        "உறுப்பு 42-ஐ செயல்படுத்த பேறுகால நலச் சட்டம் 1961 இயற்றப்பட்டது.",
        "Article 39 covers livelihood, wealth distribution, and equal pay.", "உறுப்பு 39 வாழ்வாதாரம், செல்வப் பகிர்வு, சம ஊதியத்தை உள்ளடக்கியது.",
        "Article 40 covers Village Panchayats.", "உறுப்பு 40 கிராம ஊராட்சிகளை உள்ளடக்கியது.",
        "Article 41 covers Right to work and public assistance.", "உறுப்பு 41 வேலை உரிமை மற்றும் பொது உதவியை உள்ளடக்கியது.",
        "Correct. Article 42 mandates maternity relief and humane work conditions.", "சரி. உறுப்பு 42 பேறுகால உதவி மற்றும் மனிதத்தன்மை வேலை நிலைமைகளைக் கட்டாயமாக்குகிறது."
    )

    # -------------------------------------------------------------------------
    # Q13 (Correct: A) - Simple Comparison
    # -------------------------------------------------------------------------
    add_q(
        13, "Comparison",
        "Which wage level mentioned in Article 43 is higher than Minimum Wage and covers food, clothing, shelter, education, health, and social security?",
        "குறைந்தபட்ச ஊதியத்தை விட அதிகமாகி, உணவு, உடை, இருப்பிடம், கல்வி, சுகாதாரம் மற்றும் சமூகப் பாதுகாப்பை உள்ளடக்கிய உறுப்பு 43-ல் குறிப்பிடப்பட்டுள்ள ஊதிய நிலை எது?",
        "Living Wage", "வாழ்வாதார ஊதியம் (Living Wage)",
        "Minimum Wage", "குறைந்தபட்ச ஊதியம் (Minimum Wage)",
        "Fair Wage", "நியாயமான ஊதியம் (Fair Wage)",
        "Basic Wage", "அடிப்படை ஊதியம் (Basic Wage)",
        "A",
        "Article 43 specifically directs securing a 'Living Wage' (வாழ்வாதார ஊதியம்), which provides a decent standard of life, social/cultural opportunities, and full leisure.",
        "உறுப்பு 43 குறிப்பிட்ட 'வாழ்வாதார ஊதியத்தைப்' பெற வழிகாட்டுகிறது, இது கண்ணியமான வாழ்க்கை முறை, சமூக/பண்பாட்டு வாய்ப்புகள் மற்றும் முழு ஓய்வை வழங்குகிறது.",
        "Wage hierarchy: Minimum Wage (survival) < Fair Wage (industry capacity) < Living Wage (full security & decent life).",
        "ஊதிய படிநிலை: குறைந்தபட்ச ஊதியம் < நியாயமான ஊதியம் < வாழ்வாதார ஊதியம்.",
        "Correct. Article 43 aims for a Living Wage.", "சரி. உறுப்பு 43 வாழ்வாதார ஊதியத்தை நோக்கமாகக் கொண்டுள்ளது.",
        "Minimum Wage covers bare physical survival under Minimum Wages Act 1948.", "குறைந்தபட்ச ஊதியம் 1948 சட்டத்தின் கீழ் வெறும் உடல் வாழ்வாதாரத்தை மட்டுமே உள்ளடக்கியது.",
        "Fair Wage lies between Minimum Wage and Living Wage.", "நியாயமான ஊதியம் குறைந்தபட்ச மற்றும் வாழ்வாதார ஊதியத்திற்கு இடையில் உள்ளது.",
        "Basic wage is an accounting component, not a constitutional wage standard.", "அடிப்படை ஊதியம் என்பது கணக்கியல் அம்சம், அரசியலமைப்பு ஊதியத் தரம் அல்ல."
    )

    # -------------------------------------------------------------------------
    # Q14 (Correct: B) - Amendment / Case
    # -------------------------------------------------------------------------
    add_q(
        14, "Amendment/Case",
        "Article 43A, directing the State to take steps to secure workers' participation in management of industries, was added by which amendment?",
        "தொழிற்சாலைகள் மேலாண்மையில் தொழிலாளர்களின் பங்கேற்பை உறுதி செய்ய அரசு நடவடிக்கை எடுக்க வேண்டும் என்ற உறுப்பு 43A எந்தத் திருத்தத்தால் சேர்க்கப்பட்டது?",
        "24th Constitutional Amendment Act, 1971", "24வது அரசியலமைப்பு திருத்தச் சட்டம், 1971",
        "42nd Constitutional Amendment Act, 1976", "42வது அரசியலமைப்பு திருத்தச் சட்டம், 1976",
        "44th Constitutional Amendment Act, 1978", "44வது அரசியலமைப்பு திருத்தச் சட்டம், 1978",
        "97th Constitutional Amendment Act, 2011", "97வது அரசியலமைப்பு திருத்தச் சட்டம், 2011",
        "B",
        "Article 43A was inserted by the 42nd Constitutional Amendment Act, 1976 during Emergency to promote workers' participation in industrial management.",
        "1976-ன் 42வது அரசியலமைப்பு திருத்தச் சட்டத்தால் தொழிற்சாலைகள் மேலாண்மையில் தொழிலாளர்களின் பங்கேற்பை ஊக்குவிக்க உறுப்பு 43A சேர்க்கப்பட்டது.",
        "97th Amendment Act 2011 added Article 43B for Co-operative Societies.", "2011-ன் 97வது திருத்தச் சட்டம் கூட்டுறவுச் சங்கங்களுக்காக உறுப்பு 43B-ஐச் சேர்த்தது.",
        "24th Amendment 1971 amended Article 13 and 368.", "24வது திருத்தம் 1971 உறுப்புகள் 13 மற்றும் 368-ஐத் திருத்தியது.",
        "Correct. 42nd Constitutional Amendment Act 1976 inserted Article 43A.", "சரி. 42வது அரசியலமைப்பு திருத்தச் சட்டம் 1976 உறுப்பு 43A-ஐ இணைத்தது.",
        "44th Amendment 1978 inserted Article 38(2).", "44வது திருத்தம் 1978 உறுப்பு 38(2)-ஐ இணைத்தது.",
        "97th Amendment 2011 inserted Article 43B for Co-operatives.", "97வது திருத்தம் 2011 கூட்டுறவுகளுக்காக உறுப்பு 43B-ஐ இணைத்தது."
    )

    # -------------------------------------------------------------------------
    # Q15 (Correct: C) - Article-based
    # -------------------------------------------------------------------------
    add_q(
        15, "Article-based",
        "Which Article of the Constitution directs the State to endeavor to secure a Uniform Civil Code (UCC) for all citizens throughout India?",
        "இந்தியா முழுவதிலும் உள்ள குடிமக்களுக்கு ஒரு பொது சிவில் சட்டத்தைப் (UCC) பெற அரசு முயல வேண்டும் எனக் கூறும் அரசியலமைப்பு உறுப்பு எது?",
        "Article 42", "உறுப்பு 42",
        "Article 43", "உறுப்பு 43",
        "Article 44", "உறுப்பு 44",
        "Article 45", "உறுப்பு 45",
        "C",
        "Article 44 states that the State shall endeavor to secure for the citizens a Uniform Civil Code throughout the territory of India.",
        "உறுப்பு 44 இந்தியா முழுவதிலும் உள்ள குடிமக்களுக்கு ஒரு பொது சிவில் சட்டத்தைப் பெற அரசு முயல வேண்டும் எனக் கூறுகிறது.",
        "Goa is the only state in India with a legacy Uniform Civil Code (Goa Civil Code 1867).",
        "கோவா பாரம்பரிய பொது சிவில் சட்டத்தைக் கொண்ட இந்தியாவின் ஒரே மாநிலமாகும்.",
        "Article 42 deals with humane work conditions and maternity relief.", "உறுப்பு 42 மனிதத்தன்மை வேலை நிலைமைகள் மற்றும் பேறுகால உதவி பற்றியது.",
        "Article 43 deals with living wage and cottage industries.", "உறுப்பு 43 வாழ்வாதார ஊதியம் மற்றும் குடில்தொழில்கள் பற்றியது.",
        "Correct. Article 44 deals with Uniform Civil Code.", "சரி. உறுப்பு 44 பொது சிவில் சட்டம் பற்றியது.",
        "Article 45 deals with early childhood care and education.", "உறுப்பு 45 முன்பருவக் குழந்தைப் பராமரிப்பு மற்றும் கல்வி பற்றியது."
    )

    # -------------------------------------------------------------------------
    # Q16 (Correct: D) - Simple Comparison
    # -------------------------------------------------------------------------
    add_q(
        16, "Comparison",
        "Following the 86th Constitutional Amendment Act 2002, what is the age group covered under the present Article 45?",
        "2002-ன் 86வது அரசியலமைப்பு திருத்தச் சட்டத்தைத் தொடர்ந்து, தற்போதைய உறுப்பு 45-ன் கீழ் உள்ளடக்கப்பட்டுள்ள வயதுக் குழு எது?",
        "Children up to 14 years of age", "14 வயது வரையிலான குழந்தைகள்",
        "Children between 6 and 14 years of age", "6 முதல் 14 வயது வரையிலான குழந்தைகள்",
        "Youth between 15 and 18 years of age", "15 முதல் 18 வயது வரையிலான இளைஞர்கள்",
        "Children below the age of six years (0 to 6 years)", "ஆறு வயதுக்குட்பட்ட குழந்தைகள் (0 முதல் 6 ஆண்டுகள்)",
        "D",
        "The 86th Amendment Act 2002 substituted Article 45 to cover early childhood care and education for children below six years (0-6 years), shifting age 6-14 education to Article 21A (FR).",
        "86வது திருத்தச் சட்டம் 2002 உறுப்பு 45-ஐ மாற்றியமைத்து 6 வயதுக்குட்பட்ட (0-6 ஆண்டுகள்) முன்பருவப் பராமரிப்பை உள்ளடக்கியது, 6-14 வயதுக் கல்வியை உறுப்பு 21A (FR)-க்கு மாற்றியது.",
        "Original Article 45 covered 0-14 years; Present Article 45 covers ONLY 0-6 years.",
        "அசல் உறுப்பு 45 0-14 ஆண்டுகளை உள்ளடக்கியது; தற்போதைய உறுப்பு 45 0-6 ஆண்டுகளை மட்டுமே உள்ளடக்குகிறது.",
        "Original Article 45 covered up to 14 years prior to 2002.", "அசல் உறுப்பு 45 2002-க்கு முன் 14 ஆண்டுகள் வரை உள்ளடக்கியது.",
        "Age 6 to 14 years is covered under Article 21A as a Fundamental Right.", "6 முதல் 14 வயது வரை உறுப்பு 21A-ன் கீழ் அடிப்படை உரிமையாக உள்ளது.",
        "15 to 18 years is not the scope of Article 45.", "15 முதல் 18 ஆண்டுகள் உறுப்பு 45-ன் எல்லை அல்ல.",
        "Correct. Present Article 45 covers children below six years of age.", "சரி. தற்போதைய உறுப்பு 45 ஆறு வயதுக்குட்பட்ட குழந்தைகளை உள்ளடக்குகிறது."
    )

    # -------------------------------------------------------------------------
    # Q17 (Correct: A) - Article-based
    # -------------------------------------------------------------------------
    add_q(
        17, "Article-based",
        "Which Article of Part IV directs the State to promote with special care the educational and economic interests of Scheduled Castes, Scheduled Tribes, and other weaker sections?",
        "பட்டியலினத்தவர், பழங்குடியினர் மற்றும் இதர எளிய பிரிவினரின் கல்வி மற்றும் பொருளாதார நலன்களை சிறப்பு கவனத்துடன் மேம்படுத்த அரசுக்கு ஆணையிடும் பகுதி IV-ன் உறுப்பு எது?",
        "Article 46", "உறுப்பு 46",
        "Article 47", "உறுப்பு 47",
        "Article 48", "உறுப்பு 48",
        "Article 49", "உறுப்பு 49",
        "A",
        "Article 46 directs the State to promote with special care the educational and economic interests of the weaker sections of the people, and in particular, of SCs and STs, and protect them from social injustice.",
        "உறுப்பு 46 எஸ்சி, எஸ்டி மற்றும் எளிய பிரிவினரின் கல்வி மற்றும் பொருளாதார நலன்களை சிறப்பு கவனத்துடன் மேம்படுத்தவும் சமூக அநீதியிலிருந்து பாதுகாக்கவும் அரசுக்கு ஆணையிடுகிறது.",
        "Article 46 provides the DPSP policy foundation for affirmative action reservations under Articles 15(4) and 16(4).",
        "உறுப்பு 46 உறுப்புகள் 15(4) மற்றும் 16(4)-ன் கீழ் இடஒதுக்கீடுகளுக்கான DPSP கொள்கை அடித்தளத்தை வழங்குகிறது.",
        "Correct. Article 46 deals with educational and economic interests of SCs/STs.", "சரி. உறுப்பு 46 எஸ்சி/எஸ்டிகளின் கல்வி மற்றும் பொருளாதார நலன்கள் பற்றியது.",
        "Article 47 deals with nutrition, public health, and prohibition.", "உறுப்பு 47 சத்துணவு, பொது சுகாதாரம் மற்றும் மதுவிலக்கு பற்றியது.",
        "Article 48 deals with scientific agriculture and cow slaughter ban.", "உறுப்பு 48 அறிவியல் விவசாயம் மற்றும் பசு வதை தடை பற்றியது.",
        "Article 49 deals with protection of national monuments.", "உறுப்பு 49 தேசிய நினைவிடங்கள் பாதுகாப்பு பற்றியது."
    )

    # -------------------------------------------------------------------------
    # Q18 (Correct: B) - TNPSC Trap
    # -------------------------------------------------------------------------
    add_q(
        18, "TNPSC Trap",
        "Under Article 47, the State's directive to bring about prohibition of intoxicating drinks and health-injurious drugs contains which specific constitutional exception?",
        "உறுப்பு 47-ன் கீழ், போதைப் பானங்கள் மற்றும் ஆரோக்கியத்திற்குத் தீங்கு விளைவிக்கும் மருந்துகள் அருந்துவதை மதுவிலக்கு செய்யும் அரசின் வழிகாட்டுதல் எந்த குறிப்பிட்ட அரசியலமைப்பு விதிவிலக்கைக் கொண்டுள்ளது?",
        "Exception for consumption during religious festivals", "மத பண்டிகைகளின் போது அருந்துவதற்கான விதிவிலக்கு",
        "Except for medicinal purposes", "மருத்துவ நோக்கங்களைத் தவிர",
        "Except for tourists holding foreign passports", "வெளிநாட்டு பாஸ்போர்ட் வைத்துள்ள சுற்றுலாப் பயணிகளைத் தவிர",
        "Except for traditional community celebrations", "பாரம்பரிய சமூகக் கொண்டாட்டங்களைத் தவிர",
        "B",
        "Article 47 explicitly states that the State shall endeavor to bring about prohibition of intoxicating drinks and drugs injurious to health 'except for medicinal purposes'.",
        "உறுப்பு 47 'மருத்துவ நோக்கங்களைத் தவிர' ஆரோக்கியத்திற்குத் தீங்கு விளைவிக்கும் போதைப் பானங்கள் மற்றும் மருந்துகள் அருந்துவதை மதுவிலக்கு செய்ய அரசு முயல வேண்டும் எனக் கூறுகிறது.",
        "TNPSC Trap: Medicinal use is the ONLY constitutional exception written in Article 47 text.",
        "டிஎன்பிஎஸ்சி பொறி: மருத்துவப் பயன்பாடே உறுப்பு 47 உரையில் எழுதப்பட்ட ஒரே அரசியலமைப்பு விதிவிலக்காகும்.",
        "Religious festivals are not an exception under Article 47 text.", "மத பண்டிகைகள் உறுப்பு 47 உரையின் கீழ் விதிவிலக்கு அல்ல.",
        "Correct. 'Except for medicinal purposes' is the express constitutional exception in Article 47.", "சரி. 'மருத்துவ நோக்கங்களைத் தவிர' என்பதே உறுப்பு 47-ல் உள்ள வெளிப்படையான விதிவிலக்காகும்.",
        "Foreign tourists are not mentioned in Article 47 text.", "வெளிநாட்டு சுற்றுலாப் பயணிகள் உறுப்பு 47 உரையில் குறிப்பிடப்படவில்லை.",
        "Community celebrations are not an exception.", "சமூகக் கொண்டாட்டங்கள் விதிவிலக்கு அல்ல."
    )

    # -------------------------------------------------------------------------
    # Q19 (Correct: C) - Direct Factual
    # -------------------------------------------------------------------------
    add_q(
        19, "Direct",
        "Which Article of the Constitution directs the State to organize agriculture and animal husbandry on modern lines and prohibit the slaughter of cows and calves?",
        "விவசாயம் மற்றும் கால்நடை பராமரிப்பை நவீன முறைகளில் அமைக்கவும் பசுக்கள் மற்றும் கன்றுகள் வதைத் தடுக்கவும் அரசுக்கு ஆணையிடும் அரசியலமைப்பு உறுப்பு எது?",
        "Article 46", "உறுப்பு 46",
        "Article 47", "உறுப்பு 47",
        "Article 48", "உறுப்பு 48",
        "Article 49", "உறுப்பு 49",
        "C",
        "Article 48 directs the State to endeavor to organize agriculture and animal husbandry on modern and scientific lines and preserve breeds and prohibit cow/calf slaughter.",
        "உறுப்பு 48 நவீன அறிவியல் முறைகளில் விவசாயம் மற்றும் கால்நடை பராமரிப்பை அமைக்கவும் பசு/கன்று வதைத் தடுக்கவும் அரசுக்கு ஆணையிடுகிறது.",
        "State of Gujarat v. Mirzapur Moti Kureshi (2005) upheld total ban on cow progeny slaughter under Article 48.",
        "மிர்சாபூர் மோதி குரேஷி வழக்கில் (2005) உறுப்பு 48-ன் கீழ் பசு சந்ததிகள் வதை மீதான முழுத் தடை உறுதி செய்யப்பட்டது.",
        "Article 46 covers SC/ST educational and economic interests.", "உறுப்பு 46 எஸ்சி/எஸ்டி கல்வி மற்றும் பொருளாதார நலன்களை உள்ளடக்கியது.",
        "Article 47 covers nutrition and liquor prohibition.", "உறுப்பு 47 சத்துணவு மற்றும் மதுவிலக்கை உள்ளடக்கியது.",
        "Correct. Article 48 mandates scientific agriculture and cow slaughter ban.", "சரி. உறுப்பு 48 அறிவியல் விவசாயம் மற்றும் பசு வதை தடையைக் கட்டாயமாக்குகிறது.",
        "Article 49 covers national monuments protection.", "உறுப்பு 49 தேசிய நினைவிடங்கள் பாதுகாப்பை உள்ளடக்கியது."
    )

    # -------------------------------------------------------------------------
    # Q20 (Correct: D) - Simple Comparison
    # -------------------------------------------------------------------------
    add_q(
        20, "Comparison",
        "What is the key structural distinction between Article 48A (Part IV) and Article 51A(g) (Part IV-A)?",
        "உறுப்பு 48A (பகுதி IV) மற்றும் உறுப்பு 51A(g) (பகுதி IV-A) இடையேயான முதன்மை அமைப்புக் கோட்பாடு வேறுபாடு என்ன?",
        "Article 48A applies to citizens, while 51A(g) applies to foreigners", "உறுப்பு 48A குடிமக்களுக்குப் பொருந்தும், 51A(g) வெளிநாட்டினருக்குப் பொருந்தும்",
        "Article 48A is a Fundamental Right, while 51A(g) is a DPSP", "உறுப்பு 48A ஒரு அடிப்படை உரிமை, 51A(g) ஒரு DPSP",
        "Article 48A deals with agriculture, while 51A(g) deals with Panchayats", "உறுப்பு 48A விவசாயம் பற்றியது, 51A(g) பஞ்சாயத்துகள் பற்றியது",
        "Article 48A imposes a Directive on the STATE, while 51A(g) imposes a Duty on CITIZENS", "உறுப்பு 48A அரசுக்கு வழிகாட்டுதலை விதிக்கிறது, 51A(g) குடிமக்களுக்குக் கடமையை விதிக்கிறது",
        "D",
        "Article 48A (DPSP) directs the STATE to protect environment, forests, and wildlife, whereas Article 51A(g) (Fundamental Duty) imposes a duty on EVERY CITIZEN to protect natural environment.",
        "உறுப்பு 48A (DPSP) சுற்றுச்சூழலையும் வனவிலங்குகளையும் பாதுகாக்குமாறு அரசுக்கு ஆணையிடுகிறது, மாறாக உறுப்பு 51A(g) (அடிப்படைக் கடமை) ஒவ்வொரு குடிமகனுக்கும் கடமையை விதிக்கிறது.",
        "Both 48A and 51A(g) were inserted by the 42nd Constitutional Amendment Act, 1976.",
        "48A மற்றும் 51A(g) ஆகிய இரண்டும் 1976-ன் 42வது அரசியலமைப்பு திருத்தச் சட்டத்தால் இணைக்கப்பட்டன.",
        "48A is a State directive; 51A(g) is a citizen duty.", "48A அரசு வழிகாட்டுதல்; 51A(g) குடிமகன் கடமை.",
        "Neither is a Fundamental Right in Part III.", "இரண்டும் பகுதி III-ல் உள்ள அடிப்படை உரிமை அல்ல.",
        "Both deal with natural environment, forests, and wildlife protection.", "இரண்டும் இயற்கைச் சூழல், காடுகள் மற்றும் வனவிலங்குகள் பாதுகாப்பு பற்றியவை.",
        "Correct. 48A is a State Directive; 51A(g) is a Citizen Fundamental Duty.", "சரி. 48A அரசு வழிகாட்டுதல்; 51A(g) குடிமகன் அடிப்படைக் கடமை."
    )

    # -------------------------------------------------------------------------
    # Q21 (Correct: A) - Article-based
    # -------------------------------------------------------------------------
    add_q(
        21, "Article-based",
        "Protection of monuments, places, and objects of national importance declared by Parliament by law is mandated under which Article?",
        "நாடாளுமன்றச் சட்டத்தால் தேசிய முக்கியத்துவம் வாய்ந்தது என அறிவிக்கப்பட்ட நினைவிடங்கள், இடங்களைப் பாதுகாப்பது எந்த உறுப்பின் கீழ் கட்டாயமாக்கப்பட்டுள்ளது?",
        "Article 49", "உறுப்பு 49",
        "Article 48", "உறுப்பு 48",
        "Article 50", "உறுப்பு 50",
        "Article 51", "உறுப்பு 51",
        "A",
        "Article 49 directs the State to protect every monument or place or object of artistic or historic interest declared by Parliament to be of national importance.",
        "நாடாளுமன்றச் சட்டத்தால் தேசிய முக்கியத்துவம் வாய்ந்தது என அறிவிக்கப்பட்ட நினைவிடங்கள், இடங்களைப் பாதுகாப்பது உறுப்பு 49-ன் கீழ் கட்டாயமாக்கப்பட்டுள்ளது.",
        "Archaeological Survey of India (ASI) functions to protect monuments covered under Article 49.",
        "உறுப்பு 49-ன் கீழ் உள்ள நினைவிடங்களைப் பாதுகாக்க இந்தியத் தொல்லியல் துறை (ASI) செயல்படுகிறது.",
        "Correct. Article 49 mandates protection of national monuments.", "சரி. உறுப்பு 49 தேசிய நினைவிடங்கள் பாதுகாப்பைக் கட்டாயமாக்குகிறது.",
        "Article 48 deals with agriculture and animal husbandry.", "உறுப்பு 48 விவசாயம் மற்றும் கால்நடை வளர்ப்பு பற்றியது.",
        "Article 50 deals with separation of judiciary from executive.", "உறுப்பு 50 நிர்வாகத்திலிருந்து நீதித்துறை பிரிப்பு பற்றியது.",
        "Article 51 deals with international peace and security.", "உறுப்பு 51 சர்வதேச அமைதி மற்றும் பாதுகாப்பு பற்றியது."
    )

    # -------------------------------------------------------------------------
    # Q22 (Correct: B) - Direct Factual
    # -------------------------------------------------------------------------
    add_q(
        22, "Direct",
        "Which Article of the Constitution directs the State to separate the judiciary from the executive in the public services of the State?",
        "மாநிலத்தின் பொது சேவைகளில் நிர்வாகத்திலிருந்து நீதித்துறையைப் பிரிக்க அரசுக்கு ஆணையிடும் அரசியலமைப்பு உறுப்பு எது?",
        "Article 49", "உறுப்பு 49",
        "Article 50", "உறுப்பு 50",
        "Article 51", "உறுப்பு 51",
        "Article 52", "உறுப்பு 52",
        "B",
        "Article 50 states that the State shall take steps to separate the judiciary from the executive in the public services of the State.",
        "உறுப்பு 50 மாநிலத்தின் பொது சேவைகளில் நிர்வாகத்திலிருந்து நீதித்துறையைப் பிரிக்க அரசு நடவடிக்கை எடுக்க வேண்டும் எனக் கூறுகிறது.",
        "The Code of Criminal Procedure (CrPC) 1973 statutorily fulfilled Article 50 by separating Judicial Magistrates from Executive Magistrates.",
        "1973 குற்றவியல் நடைமுறைச் சட்டம் (CrPC) நீதித்துறை மேஜிஸ்திரேட்டுகளை நிர்வாக மேஜிஸ்திரேட்டுகளிடமிருந்து பிரித்து உறுப்பு 50-ஐ நிறைவேற்றியது.",
        "Article 49 covers national monuments.", "உறுப்பு 49 தேசிய நினைவிடங்களை உள்ளடக்கியது.",
        "Correct. Article 50 mandates separation of Judiciary from Executive.", "சரி. உறுப்பு 50 நிர்வாகத்திலிருந்து நீதித்துறை பிரிப்பைக் கட்டாயமாக்குகிறது.",
        "Article 51 covers international peace and security.", "உறுப்பு 51 சர்வதேச அமைதி மற்றும் பாதுகாப்பை உள்ளடக்கியது.",
        "Article 52 begins Part V establishing The President of India.", "உறுப்பு 52 பகுதி V-ஐத் தொடங்கி இந்தியக் குடியரசுத் தலைவரை நிறுவுகிறது."
    )

    # -------------------------------------------------------------------------
    # Q23 (Correct: C) - Article-based
    # -------------------------------------------------------------------------
    add_q(
        23, "Article-based",
        "Which Article of the Constitution serves as the constitutional anchor for India's foreign policy by promoting international peace and security?",
        "சர்வதேச அமைதி மற்றும் பாதுகாப்பை மேம்படுத்துவதன் மூலம் இந்தியாவின் வெளியுறவுக் கொள்கைக்கான அரசியலமைப்பு நங்கூரமாகச் செயல்படும் உறுப்பு எது?",
        "Article 49", "உறுப்பு 49",
        "Article 50", "உறுப்பு 50",
        "Article 51", "உறுப்பு 51",
        "Article 51A", "உறுப்பு 51A",
        "C",
        "Article 51 directs the State to promote international peace and security, maintain just/honourable national relations, foster respect for international law, and encourage arbitration.",
        "உறுப்பு 51 சர்வதேச அமைதி மற்றும் பாதுகாப்பை மேம்படுத்தவும், சர்வதேச சட்டத்திற்கு மரியாதையை வளர்க்கவும், நடுவர் மன்றத்தை ஊக்குவிக்கவும் அரசுக்கு ஆணையிடுகிறது.",
        "Article 51 is the LAST article of Part IV (DPSP).", "உறுப்பு 51 என்பது பகுதி IV-ன் (DPSP) கடைசி உறுப்பாகும்.",
        "Article 49 covers national monuments.", "உறுப்பு 49 தேசிய நினைவிடங்களை உள்ளடக்கியது.",
        "Article 50 covers judicial separation.", "உறுப்பு 50 நீதித்துறை பிரிப்பை உள்ளடக்கியது.",
        "Correct. Article 51 is the foreign policy anchor DPSP.", "சரி. உறுப்பு 51 வெளியுறவுக் கொள்கை நங்கூர DPSP ஆகும்.",
        "Article 51A contains Fundamental Duties of citizens (Part IV-A).", "உறுப்பு 51A குடிமக்களின் அடிப்படைக் கடமைகளைக் கொண்டுள்ளது (பகுதி IV-A)."
    )

    # -------------------------------------------------------------------------
    # Q24 (Correct: D) - Basic Conceptual
    # -------------------------------------------------------------------------
    add_q(
        24, "Conceptual",
        "Which of the following statements regarding the conventional classification of Directive Principles into Socialist, Gandhian, and Liberal categories is CORRECT?",
        "வழிகாட்டு நெறிமுறைகளை சமதர்ம, காந்திய மற்றும் தாராளமயப் பிரிவுகளாகப் பிரிக்கும் மரபுவழி வகைப்பாடு பற்றிய பின்வரும் கூற்றுகளில் எது சரியானது?",
        "The classification is explicitly written in Chapter 1 of Part IV text", "இந்த வகைப்பாடு பகுதி IV உரையின் அத்தியாயம் 1-ல் வெளிப்படையாக எழுதப்பட்டுள்ளது",
        "The classification was added by the 42nd Constitutional Amendment 1976", "இந்த வகைப்பாடு 1976-ன் 42வது அரசியலமைப்பு திருத்தத்தால் சேர்க்கப்பட்டது",
        "The classification was created by the Supreme Court in Minerva Mills case", "இந்த வகைப்பாடு மினர்வா மில்ஸ் வழக்கில் உச்ச நீதிமன்றத்தால் உருவாக்கப்பட்டது",
        "The classification is a conventional academic division not explicitly stated in the Constitution", "இந்த வகைப்பாடு அரசியலமைப்பில் வெளிப்படையாகக் குறிப்பிடப்படாத ஒரு மரபுவழி கல்விப் பிரிவாகும்",
        "D",
        "The Constitution of India does not contain any formal classification of DPSP. On the basis of content and direction, scholars conventionally classify them into Socialist, Gandhian, and Liberal-Intellectual categories.",
        "இந்திய அரசியலமைப்பு DPSP-ன் எவ்வித முறையான வகைப்பாட்டையும் கொண்டிருக்கவில்லை. உள்ளடக்கத்தின் அடிப்படையில் அறிஞர்கள் அவற்றை சமதர்ம, காந்திய மற்றும் தாராளமயப் பிரிவுகளாக மரபுவழியாக வகைப்படுத்துகின்றனர்.",
        "TNPSC Trap: Always remember the classification is CONVENTIONAL and ACADEMIC, not constitutional text.",
        "டிஎன்பிஎஸ்சி பொறி: வகைப்பாடு மரபுவழியானது மற்றும் கல்வியுடையதே தவிர அரசியலமைப்பு உரையல்ல என்பதை எப்போதும் நினைவில் கொள்க.",
        "The text of Part IV contains no headings or sub-chapters.", "பகுதி IV உரை எந்த தலைப்புகளையும் அல்லது உட்பிரிவுகளையும் கொண்டிருக்கவில்லை.",
        "No amendment inserted ideological headings into Part IV.", "எந்தவொரு திருத்தமும் பகுதி IV-ல் தத்துவார்த்த தலைப்புகளை இணைக்கவில்லை.",
        "Minerva Mills case dealt with FR vs DPSP balance.", "மினர்வா மில்ஸ் வழக்கு FR vs DPSP சமநிலை பற்றியது.",
        "Correct. Classification is a conventional academic division not in the Constitution text.", "சரி. வகைப்பாடு என்பது அரசியலமைப்பு உரையில் இல்லாத ஒரு மரபுவழி கல்விப் பிரிவாகும்."
    )

    # -------------------------------------------------------------------------
    # Q25 (Correct: A) - Direct Factual
    # -------------------------------------------------------------------------
    add_q(
        25, "Direct",
        "Which of the following Articles of Part IV embodies a Gandhian principle promoting cottage industries in rural areas?",
        "கிராமப்புறங்களில் குடில்தொழில்களை மேம்படுத்தும் காந்தியக் கோட்பாட்டை வெளிப்படுத்தும் பகுதி IV-ன் உறுப்பு எது?",
        "Article 43", "உறுப்பு 43",
        "Article 39", "உறுப்பு 39",
        "Article 41", "உறுப்பு 41",
        "Article 44", "உறுப்பு 44",
        "A",
        "Article 43 directs the State to promote cottage industries on an individual or co-operative basis in rural areas, which is a classic Gandhian principle.",
        "கிராமப்புறங்களில் தனிநபர் அல்லது கூட்டுறவு அடிப்படையில் குடில்தொழில்களை மேம்படுத்த அரசு முயல வேண்டும் என உறுப்பு 43 வழிகாட்டுகிறது, இது ஒரு செவ்வியல் காந்தியக் கோட்பாடாகும்.",
        "Khadi and Village Industries Commission (KVIC) 1956 implements Article 43.",
        "காதி மற்றும் கிராமத் தொழில்கள் ஆணையம் (KVIC 1956) உறுப்பு 43-ஐ செயல்படுத்துகிறது.",
        "Correct. Article 43 contains Gandhian directive on cottage industries.", "சரி. உறுப்பு 43 குடில்தொழில்கள் பற்றிய காந்திய வழிகாட்டுதலைக் கொண்டுள்ளது.",
        "Article 39 contains socialist directives on resources and livelihood.", "உறுப்பு 39 வளங்கள் மற்றும் வாழ்வாதாரம் பற்றிய சமதர்ம வழிகாட்டுதல்களைக் கொண்டுள்ளது.",
        "Article 41 contains socialist directive on right to work.", "உறுப்பு 41 வேலை உரிமை பற்றிய சமதர்ம வழிகாட்டுதலைக் கொண்டுள்ளது.",
        "Article 44 contains liberal directive on Uniform Civil Code.", "உறுப்பு 44 பொது சிவில் சட்டம் பற்றிய தாராளமய வழிகாட்டுதலைக் கொண்டுள்ளது."
    )

    # -------------------------------------------------------------------------
    # Q26 (Correct: B) - Amendment / Case
    # -------------------------------------------------------------------------
    add_q(
        26, "Amendment/Case",
        "In which landmark case did the Supreme Court rule that the HARMONY AND BALANCE between Fundamental Rights (Part III) and DPSP (Part IV) is a Basic Feature of the Constitution?",
        "அடிப்படை உரிமைகள் (பகுதி III) மற்றும் DPSP (பகுதி IV) இடையிலான இணக்கமும் சமநிலையும் அரசியலமைப்பின் அடிப்படை அம்சம் என எந்த முக்கிய வழக்கில் உச்ச நீதிமன்றம் தீர்ப்பளித்தது?",
        "Golak Nath v. State of Punjab (1967)", "கோலக் நாத் எதிர் பஞ்சாப் மாநிலம் (1967)",
        "Minerva Mills v. Union of India (1980)", "மினர்வா மில்ஸ் எதிர் இந்திய யூனியன் (1980)",
        "Champakam Dorairajan v. State of Madras (1951)", "செண்பகம் துரைராஜன் எதிர் மதராஸ் மாநிலம் (1951)",
        "State of Bombay v. F.N. Balsara (1951)", "பம்பாய் மாநிலம் எதிர் F.N. பால்சரா (1951)",
        "B",
        "In Minerva Mills v. Union of India (1980), the Supreme Court declared that the Indian Constitution is founded on the bedrock of the balance between Part III and Part IV, and this harmony and balance is a Basic Feature.",
        "மினர்வா மில்ஸ் வழக்கில் (1980) பகுதி III மற்றும் பகுதி IV இடையிலான சமநிலையின் அடித்தளத்தில் இந்திய அரசியலமைப்பு நிறுவப்பட்டுள்ளது என்றும், இந்த இணக்கமும் சமநிலையும் அடிப்படை அம்சம் என்றும் உச்ச நீதிமன்றம் அறிவித்தது.",
        "Minerva Mills struck down Section 4 of 42nd Amendment which tried to give all DPSPs primacy over FRs.",
        "அனைத்து DPSP-களுக்கும் FR-களை விட முதன்மை அளிக்க முயன்ற 42வது திருத்தத்தின் பிரிவு 4-ஐ மினர்வா மில்ஸ் ரத்து செய்தது.",
        "Golak Nath (1967) held Fundamental Rights were non-amendable.", "கோலக் நாத் (1967) அடிப்படை உரிமைகளைத் திருத்த முடியாது என்றது.",
        "Correct. Minerva Mills (1980) established harmony and balance between Part III and IV as Basic Structure.", "சரி. மினர்வா மில்ஸ் (1980) பகுதி III மற்றும் IV இடையிலான சமநிலையை அடிப்படை அமைப்பாக நிறுவியது.",
        "Champakam Dorairajan (1951) held FRs were superior to DPSP.", "செண்பகம் துரைராஜன் (1951) FR-கள் DPSP-ஐ விட மேலானவை என்றது.",
        "F.N. Balsara (1951) upheld liquor prohibition under Article 47.", "F.N. பால்சரா (1951) உறுப்பு 47-ன் கீழ் மதுவிலக்கை உறுதி செய்தது."
    )

    # -------------------------------------------------------------------------
    # Q27 (Correct: C) - Simple Comparison
    # -------------------------------------------------------------------------
    add_q(
        27, "Comparison",
        "In Champakam Dorairajan case (1951), what was the Supreme Court's initial ruling regarding the relationship between Fundamental Rights and Directive Principles?",
        "செண்பகம் துரைராஜன் வழக்கில் (1951), அடிப்படை உரிமைகள் மற்றும் வழிகாட்டு நெறிமுறைகளுக்கு இடையிலான தொடர்பு குறித்து உச்ச நீதிமன்றத்தின் ஆரம்பத் தீர்ப்பு என்னவாக இருந்தது?",
        "Directive Principles override Fundamental Rights in case of conflict", "முரண்பாடு ஏற்படும் போது வழிகாட்டு நெறிமுறைகள் அடிப்படை உரிமைகளை மிஞ்சும்",
        "Directive Principles and Fundamental Rights have equal legal status", "வழிகாட்டு நெறிமுறைகளும் அடிப்படை உரிமைகளும் சமமான சட்ட அந்தஸ்தைக் கொண்டுள்ளன",
        "Fundamental Rights are superior to Directive Principles, and DPSP must run as subsidiary to Part III", "அடிப்படை உரிமைகள் வழிகாட்டு நெறிமுறைகளை விட மேலானவை, DPSP பகுதி III-க்கு துணையாகவே செயல்பட வேண்டும்",
        "Directive Principles can amend Fundamental Rights automatically", "வழிகாட்டு நெறிமுறைகள் அடிப்படை உரிமைகளைத் தானாகவே திருத்த முடியும்",
        "C",
        "In Champakam Dorairajan (1951), SC held that Fundamental Rights are sacrosanct and superior to DPSP, stating DPSPs have to conform to and run as subsidiary to Fundamental Rights.",
        "செண்பகம் துரைராஜன் வழக்கில் (1951) அடிப்படை உரிமைகள் DPSP-ஐ விட மேலானவை என்றும், DPSP-கள் அடிப்படை உரிமைகளுக்குத் துணையாகவே செயல்பட வேண்டும் என்றும் உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
        "This ruling led Parliament to enact the 1st Constitutional Amendment Act 1951, inserting Article 15(4).",
        "இத்தீர்ப்பு நாடாளுமன்றம் 1வது திருத்தச் சட்டம் 1951-ஐ இயற்றி உறுப்பு 15(4)-ஐ இணைக்க வழிவகுத்தது.",
        "Champakam Dorairajan did not give primacy to DPSP.", "செண்பகம் துரைராஜன் DPSP-க்கு முதன்மை அளிக்கவில்லை.",
        "SC did not hold them equal in 1951.", "1951-ல் SC அவற்றைச் சமமாக நினைக்கவில்லை.",
        "Correct. SC held FRs are superior and DPSP runs as subsidiary to Part III.", "சரி. FR-கள் மேலானவை மற்றும் DPSP பகுதி III-க்கு துணையாகவே செயல்பட வேண்டும் என SC கூறியது.",
        "DPSP cannot amend Fundamental Rights automatically.", "DPSP அடிப்படை உரிமைகளைத் தானாகத் திருத்த முடியாது."
    )

    # -------------------------------------------------------------------------
    # Q28 (Correct: D) - Direct Factual
    # -------------------------------------------------------------------------
    add_q(
        28, "Direct",
        "Under Article 31C inserted by the 25th Amendment 1971, laws giving effect to which specific DPSPs are protected from being declared void under Articles 14 and 19?",
        "1971-ன் 25வது திருத்தத்தால் இணைக்கப்பட்ட உறுப்பு 31C-ன் கீழ், எந்த குறிப்பிட்ட DPSP-களை செயல்படுத்தும் சட்டங்கள் உறுப்புகள் 14 மற்றும் 19-ன் கீழ் செல்லாததாக அறிவிக்கப்படுவதிலிருந்து பாதுகாக்கப்படுகின்றன?",
        "Article 40 and Article 44", "உறுப்பு 40 மற்றும் உறுப்பு 44",
        "Article 41 and Article 42", "உறுப்பு 41 மற்றும் உறுப்பு 42",
        "Article 48 and Article 48A", "உறுப்பு 48 மற்றும் உறுப்பு 48A",
        "Article 39(b) and Article 39(c)", "உறுப்பு 39(b) மற்றும் உறுப்பு 39(c)",
        "D",
        "Article 31C protects laws enacted to give effect to Directive Principles contained in Article 39(b) and Article 39(c) from being challenged under Articles 14 and 19.",
        "உறுப்பு 39(b) மற்றும் உறுப்பு 39(c)-ல் உள்ள வழிகாட்டு நெறிமுறைகளை அமல்படுத்த இயற்றப்படும் சட்டங்களை உறுப்புகள் 14 மற்றும் 19-ன் கீழ் சவால் செய்வதிலிருந்து உறுப்பு 31C பாதுகாக்கிறது.",
        "Kesavananda Bharati case (1973) upheld this constitutional protection of Article 39(b) and 39(c).",
        "கேசவானந்த பாரதி வழக்கு (1973) உறுப்பு 39(b) மற்றும் 39(c)-ன் இந்த அரசியலமைப்பு பாதுகாப்பை உறுதி செய்தது.",
        "Articles 40 and 44 are not protected under Article 31C.", "உறுப்புகள் 40 மற்றும் 44 உறுப்பு 31C-ன் கீழ் பாதுகாக்கப்படவில்லை.",
        "Articles 41 and 42 are not covered under Article 31C.", "உறுப்புகள் 41 மற்றும் 42 உறுப்பு 31C-ன் கீழ் வரவில்லை.",
        "Articles 48 and 48A are not covered under Article 31C.", "உறுப்புகள் 48 மற்றும் 48A உறுப்பு 31C-ன் கீழ் வரவில்லை.",
        "Correct. Article 31C protects laws implementing Article 39(b) and 39(c).", "சரி. உறுப்பு 31C உறுப்பு 39(b) மற்றும் 39(c)-ஐ செயல்படுத்தும் சட்டங்களைப் பாதுகாக்கிறது."
    )

    # -------------------------------------------------------------------------
    # Q29 (Correct: A) - Article-based
    # -------------------------------------------------------------------------
    add_q(
        29, "Article-based",
        "Which Constitutional Amendment Act added Article 43B directing the State to promote voluntary formation and autonomous functioning of Co-operative Societies?",
        "கூட்டுறவுச் சங்கங்களின் தன்னார்வ உருவாக்கம் மற்றும் தன்னாட்சி செயல்பாட்டை மேம்படுத்த அரசுக்கு ஆணையிடும் உறுப்பு 43B-ஐ எந்த அரசியலமைப்பு திருத்தச் சட்டம் சேர்த்தது?",
        "97th Constitutional Amendment Act, 2011", "97வது அரசியலமைப்பு திருத்தச் சட்டம், 2011",
        "86th Constitutional Amendment Act, 2002", "86வது அரசியலமைப்பு திருத்தச் சட்டம், 2002",
        "73rd Constitutional Amendment Act, 1992", "73வது அரசியலமைப்பு திருத்தச் சட்டம், 1992",
        "42nd Constitutional Amendment Act, 1976", "42வது அரசியலமைப்பு திருத்தச் சட்டம், 1976",
        "A",
        "The 97th Constitutional Amendment Act, 2011 added Article 43B to Part IV encouraging voluntary formation and autonomous management of co-operative societies.",
        "2011-ன் 97வது அரசியலமைப்பு திருத்தச் சட்டம் கூட்டுறவுச் சங்கங்களின் தன்னார்வ உருவாக்கம் மற்றும் தன்னாட்சி மேலாண்மையை ஊக்குவிக்க பகுதி IV-ல் உறுப்பு 43B-ஐச் சேர்த்தது.",
        "97th Amendment also added Right to form Co-operative Societies under Article 19(1)(c) and inserted Part IX-B.",
        "97வது திருத்தம் உறுப்பு 19(1)(c)-ன் கீழ் கூட்டுறவுச் சங்கங்களை அமைக்கும் உரிமையையும் பகுதி IX-B-ஐயும் இணைத்தது.",
        "Correct. 97th Constitutional Amendment Act 2011 inserted Article 43B.", "சரி. 97வது அரசியலமைப்பு திருத்தச் சட்டம் 2011 உறுப்பு 43B-ஐ இணைத்தது.",
        "86th Amendment 2002 substituted Article 45.", "86வது திருத்தம் 2002 உறுப்பு 45-ஐ மாற்றியமைத்தது.",
        "73rd Amendment 1992 added Part IX for Panchayats.", "73வது திருத்தம் 1992 பஞ்சாயத்துகளுக்காக பகுதி IX-ஐச் சேர்த்தது.",
        "42nd Amendment 1976 inserted Article 43A.", "42வது திருத்தம் 1976 உறுப்பு 43A-ஐ இணைத்தது."
    )

    # -------------------------------------------------------------------------
    # Q30 (Correct: B) - TNPSC Trap
    # -------------------------------------------------------------------------
    add_q(
        30, "TNPSC Trap",
        "If a State Government fails to implement a Directive Principle (such as Article 44 Uniform Civil Code), what legal remedy is available to a citizen?",
        "ஒரு மாநில அரசு ஒரு வழிகாட்டு நெறிமுறையை (உறுப்பு 44 பொது சிவில் சட்டம் போன்றவை) அமல்படுத்தத் தவறினால், ஒரு குடிமகனுக்கு உள்ள சட்டப் பரிகாரம் என்ன?",
        "The citizen can file a Writ of Mandamus in the Supreme Court under Article 32", "குடிமகன் உறுப்பு 32-ன் கீழ் உச்ச நீதிமன்றத்தில் செயலுறுத்தும் பேராணை மனு தாக்கல் செய்யலாம்",
        "No court writ can be issued; the sanction is public opinion and the ballot box during elections", "நீதிமன்றப் பேராணை எதுவும் பிறப்பிக்க முடியாது; இதன் ஒப்புதல் பொதுமக்களின் கருத்து மற்றும் தேர்தலின் போது வாக்களிப்பதே ஆகும்",
        "The Supreme Court will automatically dissolve the State Legislative Assembly", "உச்ச நீதிமன்றம் மாநில சட்டமன்றத்தைத் தானாகவே கலைத்துவிடும்",
        "The citizen can demand financial compensation from the High Court under Article 226", "குடிமகன் உறுப்பு 226-ன் கீழ் உயர் நீதிமன்றத்திலிருந்து நிதி நஷ்டஈடு கோரலாம்",
        "B",
        "DPSPs under Article 37 are non-justiciable in courts. As B.R. Ambedkar noted, the ultimate sanction behind DPSP is political sanction — public opinion and the electorate at the ballot box.",
        "உறுப்பு 37-ன் கீழ் DPSP-கள் நீதிமன்றங்களால் அமல்படுத்த முடியாதவை. பி.ஆர். அம்பேத்கர் குறிப்பிட்டது போல, DPSP-ன் பின்னால் உள்ள இறுதி ஒப்புதல் அரசியல் ஒப்புதலாகும் — பொதுமக்களின் கருத்து மற்றும் தேர்தலில் வாக்களிப்பதே ஆகும்.",
        "TNPSC Trap: Courts cannot issue writs to enforce DPSP. Electoral accountability is the real sanction.",
        "டிஎன்பிஎஸ்சி பொறி: DPSP-ஐ அமல்படுத்த நீதிமன்றங்கள் பேராணைகளைப் பிறப்பிக்க முடியாது. தேர்தல் பொறுப்புக்கூறலே உண்மையான ஒப்புதலாகும்.",
        "Writs under Art 32 apply only for Fundamental Rights violation.", "உறுப்பு 32-ன் கீழ் பேராணைகள் அடிப்படை உரிமைகள் மீறலுக்கு மட்டுமே பொருந்தும்.",
        "Correct. Non-justiciable means no court writ can be issued; electorate is the real sanction.", "சரி. அமல்படுத்த முடியாதது என்றால் நீதிமன்றப் பேராணை பிறப்பிக்க முடியாது; வாக்காளர்களே உண்மையான ஒப்புதலாவர்.",
        "Court cannot dissolve assembly for non-implementation of DPSP.", "DPSP-ஐ அமல்படுத்தாததற்காக நீதிமன்றம் சட்டமன்றத்தைக் கலைக்க முடியாது.",
        "Financial compensation cannot be claimed for non-justiciable DPSP.", "அமல்படுத்த முடியாத DPSP-க்காக நிதி நஷ்டஈடு கோர முடியாது."
    )

    # -------------------------------------------------------------------------
    # Q31 (Correct: C) - Direct Factual
    # -------------------------------------------------------------------------
    add_q(
        31, "Direct",
        "Which Constitutional Amendment Act substituted the text of Article 45 and inserted Article 21A to guarantee Right to Education as a Fundamental Right?",
        "கல்வி உரிமையை அடிப்படை உரிமையாக உத்தரவாதம் செய்ய உறுப்பு 45-ன் உரையை மாற்றியமைத்து உறுப்பு 21A-ஐ இணைத்த அரசியலமைப்பு திருத்தச் சட்டம் எது?",
        "42nd Constitutional Amendment Act, 1976", "42வது அரசியலமைப்பு திருத்தச் சட்டம், 1976",
        "44th Constitutional Amendment Act, 1978", "44வது அரசியலமைப்பு திருத்தச் சட்டம், 1978",
        "86th Constitutional Amendment Act, 2002", "86வது அரசியலமைப்பு திருத்தச் சட்டம், 2002",
        "91st Constitutional Amendment Act, 2003", "91வது அரசியலமைப்பு திருத்தச் சட்டம், 2003",
        "C",
        "The 86th Constitutional Amendment Act, 2002 inserted Article 21A (FR for 6-14 yrs), substituted Article 45 (DPSP for below 6 yrs), and added Article 51A(k) (FD).",
        "2002-ன் 86வது அரசியலமைப்பு திருத்தச் சட்டம் உறுப்பு 21A-ஐ (6-14 வயது FR) இணைத்து, உறுப்பு 45-ஐ (6 வயதுக்குட்பட்ட DPSP) மாற்றியமைத்து, உறுப்பு 51A(k)-ஐச் சேர்த்தது.",
        "86th Amendment created a 3-way reform across Part III (21A), Part IV (45), and Part IV-A (51A(k)).",
        "86வது திருத்தம் பகுதி III (21A), பகுதி IV (45) மற்றும் பகுதி IV-A (51A(k)) ஆகிய மூன்றிலும் சீர்திருத்தத்தை உருவாக்கியது.",
        "42nd Amendment added 39A, 39(f), 43A, 48A.", "42வது திருத்தம் 39A, 39(f), 43A, 48A-ஐச் சேர்த்தது.",
        "44th Amendment added Article 38(2).", "44வது திருத்தம் உறுப்பு 38(2)-ஐச் சேர்த்தது.",
        "Correct. 86th Amendment Act 2002 enacted the education constitutional package.", "சரி. 86வது திருத்தச் சட்டம் 2002 கல்வி அரசியலமைப்புத் தொகுப்பை இயற்றியது.",
        "91st Amendment limited council of ministers size.", "91வது திருத்தம் அமைச்சரவை அளவை வரம்பிற்குட்படுத்தியது."
    )

    # -------------------------------------------------------------------------
    # Q32 (Correct: D) - Simple Comparison
    # -------------------------------------------------------------------------
    add_q(
        32, "Comparison",
        "What is the key functional difference between Article 39A (DPSP) and Article 32 (Fundamental Right)?",
        "உறுப்பு 39A (DPSP) மற்றும் உறுப்பு 32 (அடிப்படை உரிமை) இடையேயான முதன்மை செயல்பாட்டு வேறுபாடு என்ன?",
        "Article 39A deals with environment, while Article 32 deals with taxation", "உறுப்பு 39A சுற்றுச்சூழல் பற்றியது, உறுப்பு 32 வரி விதிப்பு பற்றியது",
        "Article 39A applies to rich citizens, while Article 32 applies to foreign tourists", "உறுப்பு 39A பணக்கார குடிமக்களுக்குப் பொருந்தும், உறுப்பு 32 வெளிநாட்டு சுற்றுலாப் பயணிகளுக்குப் பொருந்தும்",
        "Article 39A is enforceable via writs, while Article 32 is non-justiciable", "உறுப்பு 39A பேராணைகள் மூலம் அமல்படுத்தத்தக்கது, உறுப்பு 32 அமல்படுத்த முடியாதது",
        "Article 39A provides Free Legal Aid directive, while Article 32 guarantees Constitutional Remedies for FR enforcement", "உறுப்பு 39A இலவச சட்ட உதவி வழிகாட்டுதலை வழங்குகிறது, உறுப்பு 32 FR அமலாக்கத்திற்கான அரசியலமைப்பு பரிகாரங்களை உத்தரவாதம் செய்கிறது",
        "D",
        "Article 39A is a non-justiciable DPSP guiding the State to provide free legal aid to the poor, whereas Article 32 is a justiciable Fundamental Right guaranteeing writ remedies for enforcing Part III rights.",
        "உறுப்பு 39A என்பது ஏழைகளுக்கு இலவச சட்ட உதவி வழங்க அரசுக்கு வழிகாட்டும் அமல்படுத்த முடியாத DPSP ஆகும், மாறாக உறுப்பு 32 என்பது பகுதி III உரிமைகளை அமல்படுத்துவதற்கான பேராணை பரிகாரங்களை உத்தரவாதம் செய்யும் அடிப்படை உரிமையாகும்.",
        "Legal Services Authorities Act 1987 (NALSA) was enacted to fulfill Article 39A.",
        "உறுப்பு 39A-ஐ நிறைவேற்ற 1987-ல் சட்டப் பணிகள் ஆணைக்குழுக்கள் சட்டம் (NALSA) இயற்றப்பட்டது.",
        "Neither deals with environment or taxation.", "எதுவும் சுற்றுச்சூழல் அல்லது வரி விதிப்பு பற்றியது அல்ல.",
        "Article 39A aims to help poor and weaker sections.", "உறுப்பு 39A ஏழைகள் மற்றும் எளிய பிரிவினருக்கு உதவ நோக்கமாகக் கொண்டது.",
        "Incorrect reversal: Article 32 is justiciable, Article 39A is non-justiciable DPSP.", "தவறான தலைகீழ் கூற்று: உறுப்பு 32 அமல்படுத்தக்கூடியது, உறுப்பு 39A அமல்படுத்த முடியாத DPSP.",
        "Correct. 39A is Free Legal Aid DPSP; 32 is Constitutional Remedies FR.", "சரி. 39A இலவச சட்ட உதவி DPSP; 32 அரசியலமைப்பு பரிகாரங்கள் FR."
    )

    # -------------------------------------------------------------------------
    # Q33 (Correct: A) - Basic Conceptual
    # -------------------------------------------------------------------------
    add_q(
        33, "Conceptual",
        "Why are the Directive Principles of State Policy fundamental in the governance of the country despite being non-justiciable?",
        "வழிகாட்டு நெறிமுறைகள் நீதிமன்றங்களால் அமல்படுத்த முடியாதவையாக இருந்தாலும், நாட்டின் ஆட்சியில் ஏன் அடிப்படையானவையாக இருக்கின்றன?",
        "Because they constitute the moral and socio-economic agenda that the State is duty-bound to apply in making laws", "ஏனெனில் அவை சட்டங்களை இயற்றுவதில் அரசு பயன்படுத்தக் கடமைப்பட்டுள்ள ஒழுக்க மற்றும் சமூக-பொருளாதார நிகழ்ச்சி நிரலாகும்",
        "Because any law violating DPSP is automatically void under Article 13", "ஏனெனில் DPSP-ஐ மீறும் எந்தவொரு சட்டமும் உறுப்பு 13-ன் கீழ் தானாகவே செல்லாததாகிவிடும்",
        "Because High Courts can send state ministers to jail for ignoring DPSP", "ஏனெனில் DPSP-ஐப் புறக்கணிப்பதற்காக உயர் நீதிமன்றங்கள் மாநில அமைச்சர்களைச் சிறைக்கு அனுப்பலாம்",
        "Because DPSP principles can override the Constitution of India in an emergency", "ஏனெனில் அவசரநிலையின் போது DPSP கோட்பாடுகள் இந்திய அரசியலமைப்பை மிஞ்ச முடியும்",
        "A",
        "Article 37 explicitly states that 'it shall be the duty of the State to apply these principles in making laws'. They form the fundamental charter for socio-economic legislation.",
        "உறுப்பு 37 'சட்டங்களை இயற்றுவதில் இக்கோட்பாடுகளைப் பயன்படுத்துவது அரசின் கடமையாகும்' என வெளிப்படையாகக் கூறுகிறது. அவை சமூக-பொருளாதாரச் சட்டங்களுக்கான அடிப்படைச் சாசனத்தை உருவாக்குகின்றன.",
        "Although non-justiciable, DPSPs guide all welfare laws, budget planning, and judicial interpretation.",
        "அமல்படுத்த முடியாதவையாக இருந்தாலும், DPSP-கள் அனைத்து நலச் சட்டங்கள், பட்ஜெட் திட்டமிடல் மற்றும் நீதித்துறை விளக்கங்களுக்கு வழிகாட்டுகின்றன.",
        "Correct. DPSP forms the socio-economic policy agenda for law-making.", "சரி. DPSP சட்டம் இயற்றுவதற்கான சமூக-பொருளாதாரக் கொள்கை நிகழ்ச்சி நிரலை உருவாக்குகிறது.",
        "Article 13 voids laws inconsistent with Fundamental Rights (Part III), not DPSP.", "உறுப்பு 13 அடிப்படை உரிமைகளுக்கு (பகுதி III) முரணான சட்டங்களைச் செல்லாததாக்குகிறது, DPSP-ஐ அல்ல.",
        "Courts cannot jail ministers for DPSP non-implementation.", "DPSP-ஐ அமல்படுத்தாததற்காக நீதிமன்றங்கள் அமைச்சர்களைச் சிறையில் அடைக்க முடியாது.",
        "DPSP cannot override the Constitution.", "DPSP அரசியலமைப்பை மிஞ்ச முடியாது."
    )

    # -------------------------------------------------------------------------
    # Q34 (Correct: B) - Direct Factual
    # -------------------------------------------------------------------------
    add_q(
        34, "Direct",
        "Which of the following is a Liberal-Intellectual Directive Principle under Part IV?",
        "பகுதி IV-ன் கீழ் உள்ள பின்வருவனவற்றுள் தாராளமய-அறிவுசார்க் வழிகாட்டு நெறிமுறை எது?",
        "Organisation of Village Panchayats (Article 40)", "கிராம ஊராட்சிகளை அமைத்தல் (உறுப்பு 40)",
        "Securing a Uniform Civil Code for all citizens (Article 44)", "அனைத்துக் குடிமக்களுக்கும் ஒரு பொது சிவில் சட்டத்தைப் பெறுதல் (உறுப்பு 44)",
        "Prohibition of intoxicating drinks and drugs (Article 47)", "போதைப் பானங்கள் மற்றும் மருந்துகள் அருந்துவதை மதுவிலக்கு செய்தல் (உறுப்பு 47)",
        "Promotion of cottage industries in rural areas (Article 43)", "கிராமப்புறங்களில் குடில்தொழில்களை மேம்படுத்துதல் (உறுப்பு 43)",
        "B",
        "Article 44 (Uniform Civil Code) is conventionally categorized as a Liberal-Intellectual Principle along with Articles 45, 48A, 49, 50, and 51.",
        "உறுப்பு 44 (பொது சிவில் சட்டம்) உறுப்புகள் 45, 48A, 49, 50 மற்றும் 51 ஆகியவற்றுடன் சேர்த்து மரபுவழியாக தாராளமய-அறிவுசார்க் கோட்பாடாக வகைப்படுத்தப்படுகிறது.",
        "Articles 40, 43 (cottage), and 47 (prohibition) are Gandhian Principles.", "உறுப்புகள் 40, 43 (குடில்தொழில்) மற்றும் 47 (மதுவிலக்கு) ஆகியவை காந்தியக் கோட்பாடுகள் ஆகும்.",
        "Article 40 is a Gandhian Principle.", "உறுப்பு 40 ஒரு காந்தியக் கோட்பாடு.",
        "Correct. Article 44 (UCC) is a Liberal-Intellectual Principle.", "சரி. உறுப்பு 44 (UCC) ஒரு தாராளமய-அறிவுசார்க் கோட்பாடு.",
        "Article 47 prohibition is a Gandhian Principle.", "உறுப்பு 47 மதுவிலக்கு ஒரு காந்தியக் கோட்பாடு.",
        "Article 43 cottage industry is a Gandhian Principle.", "உறுப்பு 43 குடில்தொழில் ஒரு காந்தியக் கோட்பாடு."
    )

    # -------------------------------------------------------------------------
    # Q35 (Correct: C) - Article-based
    # -------------------------------------------------------------------------
    add_q(
        35, "Article-based",
        "Which Article of the Constitution directs the State to secure 'just and humane conditions of work'?",
        "'நியாயமான மற்றும் மனிதத்தன்மையுள்ள வேலை நிலைமைகளை' உறுதி செய்ய அரசுக்கு ஆணையிடும் அரசியலமைப்பு உறுப்பு எது?",
        "Article 40", "உறுப்பு 40",
        "Article 41", "உறுப்பு 41",
        "Article 42", "உறுப்பு 42",
        "Article 43", "உறுப்பு 43",
        "C",
        "Article 42 directs the State to make provision for securing just and humane conditions of work and for maternity relief.",
        "உறுப்பு 42 நியாயமான மற்றும் மனிதத்தன்மையுள்ள வேலை நிலைமைகளையும் பேறுகால உதவியையும் உறுதிசெய்ய விதிகளை உருவாக்க அரசுக்கு ஆணையிடுகிறது.",
        "Factories Act 1948 implements the humane conditions requirement of Article 42.",
        "தொழிற்சாலைகள் சட்டம் 1948 உறுப்பு 42-ன் மனிதத்தன்மை வேலை நிலைமைகள் தேவையைச் செயல்படுத்துகிறது.",
        "Article 40 deals with Village Panchayats.", "உறுப்பு 40 கிராம ஊராட்சிகள் பற்றியது.",
        "Article 41 deals with Right to work and public assistance.", "உறுப்பு 41 வேலை உரிமை மற்றும் பொது உதவி பற்றியது.",
        "Correct. Article 42 mandates just and humane work conditions.", "சரி. உறுப்பு 42 நியாயமான மற்றும் மனிதத்தன்மை வேலை நிலைமைகளைக் கட்டாயமாக்குகிறது.",
        "Article 43 deals with living wage and cottage industries.", "உறுப்பு 43 வாழ்வாதார ஊதியம் மற்றும் குடில்தொழில்கள் பற்றியது."
    )

    # -------------------------------------------------------------------------
    # Q36 (Correct: D) - Direct Factual
    # -------------------------------------------------------------------------
    add_q(
        36, "Direct",
        "The Instrument of Instructions issued to the Governor-General and Governors under which colonial Act resembled the Directive Principles of State Policy?",
        "எந்தக் காலனித்துவச் சட்டத்தின் கீழ் கவர்னர் ஜெனரல் மற்றும் ஆளுநர்களுக்கு வழங்கப்பட்ட 'வழிகாட்டுதல் ஆவணம்' (Instrument of Instructions) அரசு வழிகாட்டு நெறிமுறைகளை ஒத்திருந்தது?",
        "Indian Councils Act, 1892", "இந்தியக் கவுன்சில்கள் சட்டம், 1892",
        "Government of India Act, 1909", "இந்திய அரசாங்கச் சட்டம், 1909",
        "Government of India Act, 1919", "இந்திய அரசாங்கச் சட்டம், 1919",
        "Government of India Act, 1935", "இந்திய அரசாங்கச் சட்டம், 1935",
        "D",
        "Dr. B.R. Ambedkar noted that the Directive Principles are like the 'Instrument of Instructions' issued to the Governor-General and Governors by the British Government under the Government of India Act, 1935.",
        "டாக்டர் பி.ஆர். அம்பேத்கர் வழிகாட்டு நெறிமுறைகள் 1935-ன் இந்திய அரசாங்கச் சட்டத்தின் கீழ் கவர்னர் ஜெனரல் மற்றும் ஆளுநர்களுக்கு வழங்கப்பட்ட 'வழிகாட்டுதல் ஆவணத்தை' ஒத்திருக்கின்றன எனக் குறிப்பிட்டார்.",
        "The only difference is that DPSPs are instructions issued to the Legislature and Executive of independent India.",
        "ஒரே வேறுபாடு என்னவென்றால் DPSP என்பது சுதந்திர இந்தியாவின் சட்டமன்றம் மற்றும் நிர்வாகத்திற்கு வழங்கப்பட்ட வழிகாட்டுதல்கள் ஆகும்.",
        "1892 Act introduced indirect elections.", "1892 சட்டம் மறைமுகத் தேர்தல்களை அறிமுகப்படுத்தியது.",
        "1909 Act introduced separate electorates.", "1909 சட்டம் தனித் தொகுதிகளை அறிமுகப்படுத்தியது.",
        "1919 Act introduced Dyarchy in provinces.", "1919 சட்டம் மாகாணங்களில் இரட்டை ஆட்சியை அறிமுகப்படுத்தியது.",
        "Correct. Government of India Act 1935 contained the Instrument of Instructions.", "சரி. இந்திய அரசாங்கச் சட்டம் 1935 வழிகாட்டுதல் ஆவணத்தைக் கொண்டிருந்தது."
    )

    # -------------------------------------------------------------------------
    # Q37 (Correct: A) - Simple Comparison
    # -------------------------------------------------------------------------
    add_q(
        37, "Comparison",
        "What is the basic difference between Fundamental Rights (Part III) and Directive Principles (Part IV)?",
        "அடிப்படை உரிமைகள் (பகுதி III) மற்றும் வழிகாட்டு நெறிமுறைகள் (பகுதி IV) இடையேயான அடிப்படை வேறுபாடு என்ன?",
        "Fundamental Rights are justiciable restrictions on State action, while DPSP are non-justiciable positive governance directives", "அடிப்படை உரிமைகள் அரசு நடவடிக்கையின் மீதான அமல்படுத்தக்கூடிய கட்டுப்பாடுகள், DPSP என்பது அமல்படுத்த முடியாத நேர்மறை ஆட்சி வழிகாட்டுதல்கள்",
        "Fundamental Rights are non-justiciable, while DPSP are directly justiciable in Supreme Court", "அடிப்படை உரிமைகள் அமல்படுத்த முடியாதவை, DPSP உச்ச நீதிமன்றத்தில் நேரடியாக அமல்படுத்தக்கூடியவை",
        "Fundamental Rights apply only to state employees, while DPSP apply to private citizens", "அடிப்படை உரிமைகள் அரசு ஊழியர்களுக்கு மட்டுமே பொருந்தும், DPSP தனிப்பட்ட குடிமக்களுக்குப் பொருந்தும்",
        "Fundamental Rights were borrowed from Ireland, while DPSP were borrowed from the US Bill of Rights", "அடிப்படை உரிமைகள் அயர்லாந்திலிருந்து பெறப்பட்டவை, DPSP அமெரிக்க உரிமைகள் மசோதாவிலிருந்து பெறப்பட்டவை",
        "A",
        "Fundamental Rights are justiciable negative obligations prohibiting arbitrary State action (establishing Political Democracy), whereas DPSPs are non-justiciable positive obligations commanding State action (establishing Social & Economic Democracy).",
        "அடிப்படை உரிமைகள் தன்னிச்சையான அரசு நடவடிக்கையைத் தடுக்கும் அமல்படுத்தக்கூடிய எதிர்மறைக் கடமைகள் (அரசியல் ஜனநாயகம்), மாறாக DPSP என்பது அரசு நடவடிக்கையை ஆணையிடும் அமல்படுத்த முடியாத நேர்மறை கடமைகள் (சமூக & பொருளாதார ஜனநாயகம்).",
        "This distinction was highlighted by constitutional jurists and affirmed by the Supreme Court.",
        "இந்த வேறுபாடு அரசியலமைப்பு வல்லுநர்களால் முன்னிலைப்படுத்தப்பட்டு உச்ச நீதிமன்றத்தால் உறுதி செய்யப்பட்டது.",
        "Correct. FRs are justiciable negative limits; DPSPs are non-justiciable positive directives.", "சரி. FR-கள் அமல்படுத்தக்கூடிய எதிர்மறை வரம்புகள்; DPSP-கள் அமல்படுத்த முடியாத நேர்மறை வழிகாட்டுதல்கள்.",
        "Incorrect reversal of justiciability.", "அமலாக்கத்தின் தவறான தலைகீழ் கூற்று.",
        "FRs apply to all individuals against State action under Article 12.", "உறுப்பு 12-ன் கீழ் அரசின் நடவடிக்கைக்கு எதிராக அனைத்துத் தனிநபர்களுக்கும் FR-கள் பொருந்தும்.",
        "FRs were borrowed from US; DPSP was borrowed from Ireland.", "FR-கள் அமெரிக்காவிலிருந்து பெறப்பட்டவை; DPSP அயர்லாந்திலிருந்து பெறப்பட்டது."
    )

    # -------------------------------------------------------------------------
    # Q38 (Correct: B) - Article-based
    # -------------------------------------------------------------------------
    add_q(
        38, "Article-based",
        "Which of the following Articles added by the 42nd Amendment Act 1976 directs the State to protect and improve the environment and safeguard forests and wildlife?",
        "1976-ன் 42வது திருத்தச் சட்டத்தால் சேர்க்கப்பட்டு, சுற்றுச்சூழலைப் பாதுகாக்கவும் மேம்படுத்தவும் காடுகள் மற்றும் வனவிலங்குகளைப் பாதுகாக்கவும் அரசுக்கு ஆணையிடும் உறுப்பு எது?",
        "Article 48", "உறுப்பு 48",
        "Article 48A", "உறுப்பு 48A",
        "Article 49", "உறுப்பு 49",
        "Article 50", "உறுப்பு 50",
        "B",
        "Article 48A was added by the 42nd Constitutional Amendment Act, 1976 directing the State to protect and improve the environment and safeguard forests and wildlife.",
        "1976-ன் 42வது அரசியலமைப்பு திருத்தச் சட்டத்தால் சுற்றுச்சூழலைப் பாதுகாக்கவும் மேம்படுத்தவும் காடுகள் மற்றும் வனவிலங்குகளைப் பாதுகாக்கவும் அரசுக்கு ஆணையிடும் உறுப்பு 48A சேர்க்கப்பட்டது.",
        "Wildlife Protection Act 1972 and Forest Conservation Act 1980 fulfill Article 48A.",
        "வனவிலங்கு பாதுகாப்புச் சட்டம் 1972 மற்றும் வனப் பாதுகாப்புச் சட்டம் 1980 உறுப்பு 48A-ஐ நிறைவேற்றுகின்றன.",
        "Article 48 was in the original 1950 text dealing with agriculture and cattle.", "உறுப்பு 48 விவசாயம் மற்றும் கால்நடை பற்றிய அசல் 1950 உரையில் இருந்தது.",
        "Correct. Article 48A was added by 42nd Amendment 1976 for environment protection.", "சரி. 42வது திருத்தம் 1976 மூலம் சுற்றுச்சூழல் பாதுகாப்பிற்காக உறுப்பு 48A சேர்க்கப்பட்டது.",
        "Article 49 deals with monuments protection.", "உறுப்பு 49 நினைவிடங்கள் பாதுகாப்பு பற்றியது.",
        "Article 50 deals with separation of judiciary from executive.", "உறுப்பு 50 நிர்வாகத்திலிருந்து நீதித்துறை பிரிப்பு பற்றியது."
    )

    # -------------------------------------------------------------------------
    # Q39 (Correct: C) - Direct Factual
    # -------------------------------------------------------------------------
    add_q(
        39, "Direct",
        "Which of the following is NOT a Socialist Directive Principle under Part IV?",
        "பின்வருவனவற்றுள் எது பகுதி IV-ன் கீழ் உள்ள சமதர்ம வழிகாட்டு நெறிமுறை அல்ல?",
        "Securing adequate means of livelihood for all citizens (Article 39(a))", "அனைத்துக் குடிமக்களுக்கும் போதுமான வாழ்வாதார வழிவகைகளை உறுதி செய்தல் (உறுப்பு 39(a))",
        "Securing equal pay for equal work for men and women (Article 39(d))", "ஆண், பெண் இருபாலருக்கும் சம வேலைக்கு சம ஊதியத்தை உறுதி செய்தல் (உறுப்பு 39(d))",
        "Promoting voluntary formation of Co-operative Societies (Article 43B)", "கூட்டுறவுச் சங்கங்களின் தன்னார்வ உருவாக்கத்தை மேம்படுத்துதல் (உறுப்பு 43B)",
        "Securing just and humane conditions of work and maternity relief (Article 42)", "நியாயமான, மனிதத்தன்மை வேலை நிலைமைகளையும் பேறுகால உதவியையும் உறுதி செய்தல் (உறுப்பு 42)",
        "C",
        "Article 43B (Co-operative Societies) is conventionally categorized as a GANDHIAN Principle along with Articles 40, 43, 46, 47 (prohibition), and 48.",
        "உறுப்பு 43B (கூட்டுறவுச் சங்கங்கள்) உறுப்புகள் 40, 43, 46, 47 (மதுவிலக்கு) மற்றும் 48 ஆகியவற்றுடன் சேர்த்து மரபுவழியாக காந்தியக் கோட்பாடாக வகைப்படுத்தப்படுகிறது.",
        "Articles 39(a), 39(d), and 42 are Socialist Principles.", "உறுப்புகள் 39(a), 39(d) மற்றும் 42 ஆகியவை சமதர்மக் கோட்பாடுகள் ஆகும்.",
        "Article 39(a) is a Socialist Principle.", "உறுப்பு 39(a) ஒரு சமதர்மக் கோட்பாடு.",
        "Article 39(d) is a Socialist Principle.", "உறுப்பு 39(d) ஒரு சமதர்மக் கோட்பாடு.",
        "Correct. Article 43B is a Gandhian Principle, not Socialist.", "சரி. உறுப்பு 43B ஒரு காந்தியக் கோட்பாடு, சமதர்மக் கோட்பாடு அல்ல.",
        "Article 42 is a Socialist Principle.", "உறுப்பு 42 ஒரு சமதர்மக் கோட்பாடு."
    )

    # -------------------------------------------------------------------------
    # Q40 (Correct: D) - Amendment / Case
    # -------------------------------------------------------------------------
    add_q(
        40, "Amendment/Case",
        "In which landmark case did the Supreme Court uphold liquor prohibition laws as a reasonable restriction under Article 19(6) implementing Article 47?",
        "உறுப்பு 47-ஐ செயல்படுத்தும் வகையில் மதுவிலக்குச் சட்டங்களை உறுப்பு 19(6)-ன் கீழ் நியாயமான கட்டுப்பாடு என எந்த முக்கிய வழக்கில் உச்ச நீதிமன்றம் உறுதி செய்தது?",
        "Sarla Mudgal v. Union of India (1995)", "சர்லா முத்கல் எதிர் இந்திய யூனியன் (1995)",
        "Randhir Singh v. Union of India (1982)", "ரந்தீர் சிங் எதிர் இந்திய யூனியன் (1982)",
        "Unni Krishnan v. State of AP (1993)", "உன்னி கிருஷ்ணன் எதிர் ஆந்திரப் பிரதேசம் (1993)",
        "State of Bombay v. F.N. Balsara (1951)", "பம்பாய் மாநிலம் எதிர் F.N. பால்சரா (1951)",
        "D",
        "In State of Bombay v. F.N. Balsara (1951), the Supreme Court held that state prohibition laws implementing Article 47 were valid reasonable restrictions under Article 19(6), ruling there is no fundamental right to trade in liquor.",
        "F.N. பால்சரா வழக்கில் (1951) உறுப்பு 47-ஐ செயல்படுத்தும் மாநில மதுவிலக்குச் சட்டங்கள் உறுப்பு 19(6)-ன் கீழ் செல்லுபடியாகும் நியாயமான கட்டுப்பாடுகள் என உச்ச நீதிமன்றம் தீர்ப்பளித்தது, மது வியாபாரம் செய்ய அடிப்படை உரிமை எதுவும் இல்லை என்றது.",
        "The court held liquor trade is res extra commercium (outside commerce).", "மதுபான வியாபாரம் வணிகத்திற்கு அப்பாற்பட்டது என நீதிமன்றம் கூறியது.",
        "Sarla Mudgal case dealt with Uniform Civil Code (Article 44).", "சர்லா முத்கல் வழக்கு பொது சிவில் சட்டம் (உறுப்பு 44) பற்றியது.",
        "Randhir Singh case dealt with Equal Pay for Equal Work (Article 39(d)).", "ரந்தீர் சிங் வழக்கு சம வேலைக்கு சம ஊதியம் (உறுப்பு 39(d)) பற்றியது.",
        "Unni Krishnan case dealt with Right to Education (Article 45/21A).", "உன்னி கிருஷ்ணன் வழக்கு கல்வி உரிமை (உறுப்பு 45/21A) பற்றியது.",
        "Correct. F.N. Balsara (1951) upheld liquor prohibition laws under Article 47.", "சரி. F.N. பால்சரா (1951) உறுப்பு 47-ன் கீழ் மதுவிலக்குச் சட்டங்களை உறுதி செய்தது."
    )

    # -------------------------------------------------------------------------
    # Q41 (Correct: A) - TNPSC Trap
    # -------------------------------------------------------------------------
    add_q(
        41, "TNPSC Trap",
        "Did Article 40 of the Constitution (1950) automatically create Part IX and the 11th Schedule for Panchayati Raj?",
        "அரசியலமைப்பின் உறுப்பு 40 (1950) பஞ்சாயத்து ராஜிற்கான பகுதி IX மற்றும் 11வது அட்டவணையைத் தானாகவே உருவாக்கியதா?",
        "No. Article 40 was only a DPSP directive; Part IX and 11th Schedule were created 42 years later by the 73rd Amendment Act 1992", "இல்லை. உறுப்பு 40 ஒரு DPSP வழிகாட்டுதல் மட்டுமே; பகுதி IX மற்றும் 11வது அட்டவணை 42 ஆண்டுகளுக்குப் பிறகு 1992-ன் 73வது திருத்தச் சட்டத்தாலேயே உருவாக்கப்பட்டன",
        "Yes. Article 40 contained all 29 subjects of the 11th Schedule in 1950", "ஆம். உறுப்பு 40 1950-லேயே 11வது அட்டவணையின் அனைத்து 29 தலைப்புகளையும் கொண்டிருந்தது",
        "Yes. Article 40 made 3-tier Panchayats mandatory in all states from January 26, 1950", "ஆம். உறுப்பு 40 ஜனவரி 26, 1950 முதல் அனைத்து மாநிலங்களிலும் 3-அடுக்கு பஞ்சாயத்துகளைக் கட்டாயமாக்கியது",
        "No. Part IX was created by the 42nd Amendment Act 1976", "இல்லை. பகுதி IX 1976-ன் 42வது திருத்தச் சட்டத்தால் உருவாக்கப்பட்டது",
        "A",
        "Article 40 was merely a DPSP policy directive directing the State to organize village panchayats. Constitutional status, 3-tier structure, Part IX (Arts 243-243O), and 11th Schedule were added by the 73rd Amendment Act, 1992.",
        "உறுப்பு 40 என்பது கிராம ஊராட்சிகளை அமைக்க அரசுக்கு ஆணையிடும் ஒரு DPSP கொள்கை வழிகாட்டுதல் மட்டுமே. அரசியலமைப்பு அந்தஸ்து, 3-அடுக்கு அமைப்பு, பகுதி IX மற்றும் 11வது அட்டவணை 1992-ன் 73வது திருத்தச் சட்டத்தால் சேர்க்கப்பட்டன.",
        "TNPSC Trap: Do not confuse Article 40 (1950 DPSP directive) with the 73rd Amendment Act 1992 (Part IX framework).",
        "டிஎன்பிஎஸ்சி பொறி: உறுப்பு 40-ஐ (1950 DPSP வழிகாட்டுதல்) 1992-ன் 73வது திருத்தச் சட்டத்துடன் (பகுதி IX கட்டமைப்பு) குழப்பிக் கொள்ள வேண்டாம்.",
        "Correct. Article 40 was only a directive; 73rd Amendment 1992 created Part IX and 11th Schedule.", "சரி. உறுப்பு 40 வழிகாட்டுதல் மட்டுமே; 73வது திருத்தம் 1992 பகுதி IX மற்றும் 11வது அட்டவணையை உருவாக்கியது.",
        "11th Schedule was added in 1992, not 1950.", "11வது அட்டவணை 1992-ல் சேர்க்கப்பட்டது, 1950-ல் அல்ல.",
        "3-tier structure became mandatory only post-73rd Amendment in 1992.", "3-அடுக்கு அமைப்பு 1992-ல் 73வது திருத்தத்திற்குப் பிறகே கட்டாயமானது.",
        "Part IX was created by 73rd Amendment 1992, not 42nd Amendment 1976.", "பகுதி IX 1992-ன் 73வது திருத்தத்தால் உருவாக்கப்பட்டது, 1976-ன் 42வது திருத்தத்தால் அல்ல."
    )

    # -------------------------------------------------------------------------
    # Q42 (Correct: B) - Article-based
    # -------------------------------------------------------------------------
    add_q(
        42, "Article-based",
        "Which clause of Article 39 directs the State to prevent the concentration of wealth and means of production to the common detriment?",
        "செல்வம் மற்றும் உற்பத்தி சாதனங்கள் பொது மக்களுக்குத் தீங்கு விளைவிக்கும் வகையில் குவிவதைத் தடுக்க அரசுக்கு ஆணையிடும் உறுப்பு 39-ன் உட்பிரிவு எது?",
        "Article 39(a)", "உறுப்பு 39(a)",
        "Article 39(c)", "உறுப்பு 39(c)",
        "Article 39(d)", "உறுப்பு 39(d)",
        "Article 39(e)", "உறுப்பு 39(e)",
        "B",
        "Article 39(c) directs that the operation of the economic system does not result in the concentration of wealth and means of production to the common detriment.",
        "உறுப்பு 39(c) பொருளாதார அமைப்பின் செயல்பாடு செல்வம் மற்றும் உற்பத்தி சாதனங்கள் பொதுத் தீங்கு விளைவிக்கும் வகையில் குவிவதற்கு வழிவகுக்கக் கூடாது என ஆணையிடுகிறது.",
        "Article 39(b) deals with material resources distribution; Article 39(c) deals with wealth concentration prevention.",
        "உறுப்பு 39(b) பொருள் வளப் பகிர்வு பற்றியது; உறுப்பு 39(c) செல்வக் குவிப்புத் தடை பற்றியது.",
        "Article 39(a) deals with adequate livelihood.", "உறுப்பு 39(a) போதுமான வாழ்வாதாரம் பற்றியது.",
        "Correct. Article 39(c) directs prevention of concentration of wealth.", "சரி. உறுப்பு 39(c) செல்வக் குவிப்புத் தடையை வழிகாட்டுகிறது.",
        "Article 39(d) deals with equal pay for equal work.", "உறுப்பு 39(d) சம வேலைக்கு சம ஊதியம் பற்றியது.",
        "Article 39(e) deals with protection of worker health.", "உறுப்பு 39(e) தொழிலாளர் சுகாதார பாதுகாப்பு பற்றியது."
    )

    # -------------------------------------------------------------------------
    # Q43 (Correct: C) - Direct Factual
    # -------------------------------------------------------------------------
    add_q(
        43, "Direct",
        "Which committee's recommendations led to the insertion of Fundamental Duties (Part IV-A) following Part IV DPSPs in 1976?",
        "1976-ல் பகுதி IV DPSP-களைத் தொடர்ந்து பகுதி IV-A அடிப்படைக் கடமைகள் சேர்க்கப்படக் காரணமான எந்தக் குழுவின் பரிந்துரைகள் ஆகும்?",
        "Sarkaria Commission", "சர்க்காரியா ஆணையம்",
        "Balwant Rai Mehta Committee", "பல்வந்த் ராய் மேத்தா குழு",
        "Swaran Singh Committee", "ஸ்வரன் சிங் குழு",
        "Verma Committee", "வர்மா குழு",
        "C",
        "The Swaran Singh Committee (1976) recommended the inclusion of a separate chapter on Fundamental Duties, which led to the 42nd Amendment Act 1976 inserting Part IV-A (Article 51A).",
        "ஸ்வரன் சிங் குழுவின் (1976) பரிந்துரைகள் 1976-ன் 42வது திருத்தச் சட்டம் மூலம் பகுதி IV-A (உறுப்பு 51A) சேர்க்கப்படக் காரணமாயின.",
        "Swaran Singh Committee recommended 8 duties; 42nd Amendment enacted 10 duties.",
        "ஸ்வரன் சிங் குழு 8 கடமைகளைப் பரிந்துரைத்தது; 42வது திருத்தம் 10 கடமைகளை இயற்றியது.",
        "Sarkaria Commission dealt with Centre-State relations.", "சர்க்காரியா ஆணையம் மத்திய-மாநில உறவுகள் பற்றியது.",
        "Balwant Rai Mehta Committee dealt with 3-tier Panchayati Raj.", "பல்வந்த் ராய் மேத்தா குழு 3-அடுக்கு பஞ்சாயத்து ராஜ் பற்றியது.",
        "Correct. Swaran Singh Committee recommended Fundamental Duties.", "சரி. ஸ்வரன் சிங் குழு அடிப்படைக் கடமைகளைப் பரிந்துரைத்தது.",
        "Verma Committee (1999) identified legal provisions implementing Fundamental Duties.", "வர்மா குழு (1999) அடிப்படைக் கடமைகளைச் செயல்படுத்தும் சட்ட விதிகளை அடையாளம் கண்டது."
    )

    # -------------------------------------------------------------------------
    # Q44 (Correct: D) - Simple Comparison
    # -------------------------------------------------------------------------
    add_q(
        44, "Comparison",
        "How does Article 49 (Monuments Protection DPSP) differ from Articles 29 and 30 (Minority Cultural Rights FR)?",
        "உறுப்பு 49 (நினைவிடங்கள் பாதுகாப்பு DPSP) உறுப்புகள் 29 மற்றும் 30-லிருந்து (சிறுபான்மையினர் பண்பாட்டு உரிமைகள் FR) எவ்வாறு வேறுபடுகிறது?",
        "Article 49 applies only to foreign monuments, while Arts 29-30 apply to Indian monuments", "உறுப்பு 49 வெளிநாட்டு நினைவிடங்களுக்கு மட்டுமே பொருந்தும், 29-30 இந்திய நினைவிடங்களுக்குப் பொருந்தும்",
        "Article 49 is a justiciable Fundamental Right, while Arts 29-30 are non-justiciable DPSPs", "உறுப்பு 49 ஒரு அமல்படுத்தக்கூடிய அடிப்படை உரிமை, 29-30 அமல்படுத்த முடியாத DPSP-கள்",
        "Article 49 deals with tax exemptions, while Arts 29-30 deal with police powers", "உறுப்பு 49 வரி விலக்குகள் பற்றியது, 29-30 காவல் அதிகாரங்கள் பற்றியது",
        "Article 49 directs State to protect physical monuments of national importance, while Arts 29-30 guarantee cultural/educational rights to minority communities", "உறுப்பு 49 தேசிய முக்கியத்துவம் வாய்ந்த பௌதிக நினைவிடங்களைப் பாதுகாக்க அரசுக்கு வழிகாட்டுகிறது, மாறாக 29-30 சிறுபான்மையினருக்குப் பண்பாட்டு/கல்வி உரிமைகளை உத்தரவாதம் செய்கின்றன",
        "D",
        "Article 49 is a non-justiciable DPSP focusing on protecting physical monuments and historic places declared by Parliament, whereas Articles 29-30 are justiciable Fundamental Rights protecting minority language, script, culture, and educational institutions.",
        "உறுப்பு 49 என்பது நாடாளுமன்றத்தால் அறிவிக்கப்பட்ட பௌதிக நினைவிடங்களைப் பாதுகாப்பதில் கவனம் செலுத்தும் அமல்படுத்த முடியாத DPSP ஆகும், மாறாக உறுப்புகள் 29-30 சிறுபான்மையினரின் மொழி, பண்பாடு மற்றும் கல்வி நிறுவனங்களைப் பாதுகாக்கும் அமல்படுத்தக்கூடிய அடிப்படை உரிமைகள் ஆகும்.",
        "Ancient Monuments and Archaeological Sites and Remains (AMASR) Act 1958 implements Article 49.",
        "1958 AMASR சட்டம் உறுப்பு 49-ஐ செயல்படுத்துகிறது.",
        "Article 49 applies to Indian monuments declared of national importance.", "உறுப்பு 49 தேசிய முக்கியத்துவம் வாய்ந்தது என அறிவிக்கப்பட்ட இந்திய நினைவிடங்களுக்குப் பொருந்தும்.",
        "Incorrect reversal of legal status: Art 49 is DPSP; Arts 29-30 are FRs.", "சட்ட அந்தஸ்தின் தவறான தலைகீழ் கூற்று: உறுப்பு 49 DPSP; 29-30 FR-கள்.",
        "Neither deals with taxation or police powers.", "எதுவும் வரி விதிப்பு அல்லது காவல் அதிகாரங்கள் பற்றியது அல்ல.",
        "Correct. 49 is physical monuments DPSP; 29-30 are minority cultural rights FR.", "சரி. 49 பௌதிக நினைவிடங்கள் DPSP; 29-30 சிறுபான்மையினர் பண்பாட்டு உரிமைகள் FR."
    )

    # -------------------------------------------------------------------------
    # Q45 (Correct: A) - Basic Conceptual
    # -------------------------------------------------------------------------
    add_q(
        45, "Conceptual",
        "Which famous constitutional scholar described the Fundamental Rights and the Directive Principles of State Policy together as the 'Conscience of the Constitution'?",
        "அடிப்படை உரிமைகள் மற்றும் அரசு வழிகாட்டு நெறிமுறைகள் ஆகிய இரண்டையும் சேர்த்து 'அரசியலமைப்பின் மனசாட்சி' என்று விவரித்த புகழ்பெற்ற அரசியலமைப்பு அறிஞர் யார்?",
        "Granville Austin", "கிரான்வில் ஆஸ்டின்",
        "K.C. Wheare", "கே.சி. வியர்",
        "Sir Ivor Jennings", "சர் ஐவர் ஜென்னிங்ஸ்",
        "A.V. Dicey", "ஏ.வி. டைசி",
        "A",
        "Granville Austin, a renowned American historian of the Indian Constitution, described Part III (Fundamental Rights) and Part IV (DPSP) together as the 'Conscience of the Constitution'.",
        "புகழ்பெற்ற அமெரிக்க வரலாற்று அறிஞர் கிரான்வில் ஆஸ்டின் பகுதி III (அடிப்படை உரிமைகள்) மற்றும் பகுதி IV (DPSP) ஆகிய இரண்டையும் சேர்த்து 'அரசியலமைப்பின் மனசாட்சி' என்று விவரித்தார்.",
        "Granville Austin observed that DPSPs were aimed at furthering the goals of the social revolution.",
        "DPSP-கள் சமூகப் புரட்சியின் இலக்குகளை முன்னெடுத்துச் செல்வதை நோக்கமாகக் கொண்டவை என கிரான்வில் ஆஸ்டின் குறிப்பிட்டார்.",
        "Correct. Granville Austin called FR and DPSP the 'Conscience of the Constitution'.", "சரி. கிரான்வில் ஆஸ்டின் FR மற்றும் DPSP-ஐ 'அரசியலமைப்பின் மனசாட்சி' என்றார்.",
        "K.C. Wheare described Indian Constitution as 'Quasi-Federal'.", "கே.சி. வியர் இந்திய அரசியலமைப்பை 'அரை-கூட்டாட்சி' என்றார்.",
        "Sir Ivor Jennings criticized DPSP as 'pious aspirations'.", "சர் ஐவர் ஜென்னிங்ஸ் DPSP-ஐ 'பக்தி விருப்பங்கள்' என விமர்சித்தார்.",
        "A.V. Dicey formulated the legal doctrine of Rule of Law.", "ஏ.வி. டைசி சட்டத்தின் ஆட்சி கோட்பாட்டை உருவாக்கினார்."
    )

    # -------------------------------------------------------------------------
    # Q46 (Correct: B) - Article-based
    # -------------------------------------------------------------------------
    add_q(
        46, "Article-based",
        "Under Article 39(f), substituted by the 42nd Amendment 1976, the State is directed to ensure that children are given opportunities and facilities to develop in a healthy manner and in conditions of:",
        "42வது திருத்தம் 1976 மூலம் மாற்றியமைக்கப்பட்ட உறுப்பு 39(f)-ன் கீழ், குழந்தைகள் ஆரோக்கியமான முறையில் வளர வாய்ப்புகளும் வசதிகளும் மற்றும் எந்த நிலைமைகளும் வழங்கப்படுவதை உறுதி செய்ய அரசு வழிகாட்டப்படுகிறது?",
        "Strict military discipline and religious obedience", "கடுமையான இராணுவ ஒழுக்கம் மற்றும் மத கீழ்ப்படிதல்",
        "Freedom and dignity", "சுதந்திரம் மற்றும் கண்ணியம் (Freedom and dignity)",
        "Compulsory state apprenticeship without wages", "ஊதியமற்ற கட்டாய அரசு பயிற்சி",
        "Exclusive private school guardianship", "பிரத்யேக தனியார் பள்ளி பாதுகாப்பு",
        "B",
        "Article 39(f) directs that children are given opportunities and facilities to develop in a healthy manner and in conditions of freedom and dignity, and that childhood and youth are protected against exploitation.",
        "உறுப்பு 39(f) குழந்தைகள் ஆரோக்கியமான முறையிலும் சுதந்திரம் மற்றும் கண்ணியத்துடனும் வளர வாய்ப்புகளும் வசதிகளும் வழங்கப்படுவதையும், குழந்தைப்பருவம் துஷ்பிரயோகத்திலிருந்து பாதுகாக்கப்படுவதையும் உறுதி செய்ய அரசுக்கு ஆணையிடுகிறது.",
        "Article 39(f) was substituted by the 42nd Constitutional Amendment Act, 1976.",
        "உறுப்பு 39(f) 1976-ன் 42வது அரசியலமைப்பு திருத்தச் சட்டத்தால் மாற்றியமைக்கப்பட்டது.",
        "Military discipline is not the language of Article 39(f).", "இராணுவ ஒழுக்கம் உறுப்பு 39(f)-ன் மொழி அல்ல.",
        "Correct. Article 39(f) uses the exact words 'freedom and dignity'.", "சரி. உறுப்பு 39(f) 'சுதந்திரம் மற்றும் கண்ணியம்' என்ற சொற்களைப் பயன்படுத்துகிறது.",
        "Unpaid apprenticeship is contrary to child protection.", "ஊதியமற்ற பயிற்சி குழந்தை பாதுகாப்பிற்கு எதிரானது.",
        "Private guardianship is not mentioned.", "தனியார் பாதுகாப்பு குறிப்பிடப்படவில்லை."
    )

    # -------------------------------------------------------------------------
    # Q47 (Correct: C) - Direct Factual
    # -------------------------------------------------------------------------
    add_q(
        47, "Direct",
        "Which British constitutional scholar famously criticized the Directive Principles of State Policy as 'pious aspirations'?",
        "அரசு வழிகாட்டு நெறிமுறைகளை 'பக்தி விருப்பங்கள்' (Pious aspirations) என்று புகழ்பெற்ற முறையில் விமர்சித்த பிரிட்டிஷ் அரசியலமைப்பு அறிஞர் யார்?",
        "Granville Austin", "கிரான்வில் ஆஸ்டின்",
        "Dr. B.R. Ambedkar", "டாக்டர் பி.ஆர். அம்பேத்கர்",
        "Sir Ivor Jennings", "சர் ஐவர் ஜென்னிங்ஸ்",
        "K.T. Shah", "கே.டி. ஷா",
        "C",
        "Sir Ivor Jennings criticized Part IV of the Indian Constitution, stating that the Directive Principles were merely 'pious aspirations' with no legal enforceability.",
        "சர் ஐவர் ஜென்னிங்ஸ் பகுதி IV-ஐ விமர்சித்து, வழிகாட்டு நெறிமுறைகள் எவ்வித சட்ட அமலாக்கமும் இல்லாத வெறும் 'பக்தி விருப்பங்கள்' என்றார்.",
        "K.T. Shah compared DPSP to 'a cheque on a bank payable at the convenience of the bank'.",
        "கே.டி. ஷா DPSP-ஐ 'வங்கியின் வசதிக்கேற்ப செலுத்தத்தக்க வங்கிச் காசோலைக்கு' ஒப்பிட்டார்.",
        "Granville Austin praised DPSP as 'Conscience of the Constitution'.", "கிரான்வில் ஆஸ்டின் DPSP-ஐ 'அரசியலமைப்பின் மனசாட்சி' எனப் பாராட்டினார்.",
        "Dr. B.R. Ambedkar praised DPSP as 'Novel Features'.", "டாக்டர் பி.ஆர். அம்பேத்கர் DPSP-ஐ 'நவீன அம்சங்கள்' எனப் பாராட்டினார்.",
        "Correct. Sir Ivor Jennings called DPSP 'pious aspirations'.", "சரி. சர் ஐவர் ஜென்னிங்ஸ் DPSP-ஐ 'பக்தி விருப்பங்கள்' என்றார்.",
        "K.T. Shah called DPSP 'a cheque payable at the convenience of the bank'.", "கே.டி. ஷா DPSP-ஐ 'வங்கியின் வசதிக்கேற்ப செலுத்தத்தக்க காசோலை' என்றார்."
    )

    # -------------------------------------------------------------------------
    # Q48 (Correct: D) - Amendment / Case
    # -------------------------------------------------------------------------
    add_q(
        48, "Amendment/Case",
        "In Randhir Singh v. Union of India (1982), the Supreme Court held that 'Equal Pay for Equal Work' under Article 39(d) is a constitutional goal enforceable when read with which Fundamental Rights?",
        "ரந்தீர் சிங் வழக்கில் (1982), உறுப்பு 39(d)-ன் கீழ் உள்ள 'சம வேலைக்கு சம ஊதியம்' எந்த அடிப்படை உரிமைகளுடன் சேர்த்து வாசிக்கப்படும் போது அமல்படுத்தக்கூடிய அரசியலமைப்பு இலக்காகும் என உச்ச நீதிமன்றம் தீர்ப்பளித்தது?",
        "Articles 19 and 21", "உறுப்புகள் 19 மற்றும் 21",
        "Articles 25 and 28", "உறுப்புகள் 25 மற்றும் 28",
        "Articles 32 and 226", "உறுப்புகள் 32 மற்றும் 226",
        "Articles 14 and 16", "உறுப்புகள் 14 மற்றும் 16",
        "D",
        "In Randhir Singh (1982), the SC held that Equal Pay for Equal Work under Article 39(d) read with Articles 14 (Equality before Law) and 16 (Equality of Opportunity in Public Employment) is a constitutional goal enforceable in public services.",
        "ரந்தீர் சிங் வழக்கில் (1982), உறுப்புகள் 14 மற்றும் 16-உடன் சேர்த்து வாசிக்கப்படும் போது உறுப்பு 39(d)-ன் கீழ் உள்ள சம வேலைக்கு சம ஊதியம் என்பது பொதுப்பணியில் அமல்படுத்தக்கூடிய அரசியலமைப்பு இலக்காகும் என SC தீர்ப்பளித்தது.",
        "Equal Remuneration Act 1976 statutorily enforces Article 39(d).", "சம ஊதியச் சட்டம் 1976 உறுப்பு 39(d)-ஐச் சட்டப்பூர்வமாக அமல்படுத்துகிறது.",
        "Articles 19 and 21 deal with freedoms and life/liberty.", "உறுப்புகள் 19 மற்றும் 21 சுதந்திரங்கள் மற்றும் வாழ்வு/சுதந்திரம் பற்றியவை.",
        "Articles 25 and 28 deal with religious freedom.", "உறுப்புகள் 25 மற்றும் 28 மத சுதந்திரம் பற்றியவை.",
        "Articles 32 and 226 deal with writ remedies.", "உறுப்புகள் 32 மற்றும் 226 பேராணை பரிகாரங்கள் பற்றியவை.",
        "Correct. Equal Pay for Equal Work (39(d)) is read with Articles 14 and 16.", "சரி. சம வேலைக்கு சம ஊதியம் (39(d)) உறுப்புகள் 14 மற்றும் 16-உடன் வாசிக்கப்படுகிறது."
    )

    # -------------------------------------------------------------------------
    # Q49 (Correct: A) - Simple Comparison
    # -------------------------------------------------------------------------
    add_q(
        49, "Comparison",
        "How does Article 50 (Judicial Separation DPSP) compare with the US doctrine of rigid Separation of Powers?",
        "உறுப்பு 50 (நீதித்துறை பிரிப்பு DPSP) அமெரிக்காவின் கடுமையான அதிகாரப் பிரிப்புக் கோட்பாட்டுடன் எவ்வாறு ஒப்பிடப்படுகிறது?",
        "Article 50 directs separation of judiciary from executive in public services within Parliamentary democracy, unlike rigid US separation", "உறுப்பு 50 கடுமையான அமெரிக்கப் பிரிப்பைப் போலன்றி, நாடாளுமன்ற ஜனநாயகத்திற்குள் பொது சேவைகளில் நிர்வாகத்திலிருந்து நீதித்துறையைப் பிரிக்க வழிகாட்டுகிறது",
        "Article 50 adopts the exact US presidential system of complete separation", "உறுப்பு 50 முற்றுமுழுதான பிரிப்பின் அமெரிக்க அதிபர் முறையை அப்படியே ஏற்கிறது",
        "Article 50 allows executive ministers to sit as High Court judges", "உறுப்பு 50 நிர்வாக அமைச்சர்கள் உயர் நீதிமன்ற நீதிபதிகளாக அமர அனுமதிக்கிறது",
        "Article 50 abolishes judicial review completely", "உறுப்பு 50 நீதித்துறை ஆய்வை முழுமையாக ஒழிக்கிறது",
        "A",
        "India follows Parliamentary Democracy where Executive is part of Legislature. Article 50 specifically directs separating Judiciary from Executive in public services (CrPC 1973), maintaining checks and balances rather than rigid compartmentalization.",
        "இந்தியா நாடாளுமன்ற ஜனநாயகத்தைப் பின்பற்றுகிறது, இதில் நிர்வாகம் சட்டமன்றத்தின் பகுதியாகும். உறுப்பு 50 கடுமையான துறைப் பிரிப்பை விட கட்டுப்பாடுகள் மற்றும் சமநிலைகளைப் பேணி, பொது சேவைகளில் நிர்வாகத்திலிருந்து நீதித்துறையைப் பிரிக்க வழிகாட்டுகிறது.",
        "CrPC 1973 separated Judicial Magistrates from Executive Magistrates under Article 50.",
        "CrPC 1973 உறுப்பு 50-ன் கீழ் நீதித்துறை மேஜிஸ்திரேட்டுகளை நிர்வாக மேஜிஸ்திரேட்டுகளிடமிருந்து பிரித்தது.",
        "Correct. Article 50 operates within Parliamentary Democracy with checks and balances.", "சரி. உறுப்பு 50 கட்டுப்பாடுகள் மற்றும் சமநிலைகளுடன் கூடிய நாடாளுமன்ற ஜனநாயகத்திற்குள் செயல்படுகிறது.",
        "India does not follow Presidential system.", "இந்தியா அதிபர் முறையைப் பின்பற்றவில்லை.",
        "Ministers cannot hold judicial office under Article 50.", "அமைச்சர்கள் உறுப்பு 50-ன் கீழ் நீதித்துறை பதவியை வகிக்க முடியாது.",
        "Article 50 strengthens judicial independence, not abolishes review.", "உறுப்பு 50 நீதித்துறை சுயசார்பை வலுப்படுத்துகிறதே தவிர, ஆய்வை ஒழிக்கவில்லை."
    )

    # -------------------------------------------------------------------------
    # Q50 (Correct: B) - TNPSC Trap
    # -------------------------------------------------------------------------
    add_q(
        50, "TNPSC Trap",
        "Does Article 51 (International Peace & Security) empower the Parliament to automatically enforce international treaties into domestic Indian law without enacting implementing legislation under Article 253?",
        "உறுப்பு 51 (சர்வதேச அமைதி & பாதுகாப்பு) உறுப்பு 253-ன் கீழ் செயலாக்கச் சட்டத்தை இயற்றாமல் பன்னாட்டு ஒப்பந்தங்களை இந்திய உள்நாட்டுச் சட்டத்தில் தானாகவே அமல்படுத்த நாடாளுமன்றத்திற்கு அதிகாரமளிக்கிறதா?",
        "Yes. Article 51 makes all international treaties automatically self-executing domestic laws", "ஆம். உறுப்பு 51 அனைத்து சர்வதேச ஒப்பந்தங்களையும் தானாகவே செயல்படும் உள்நாட்டுச் சட்டங்களாக மாற்றுகிறது",
        "No. Article 51 is a DPSP policy guide; international treaties require implementing legislation passed by Parliament under Article 253 to become enforceable domestic law", "இல்லை. உறுப்பு 51 ஒரு DPSP கொள்கை வழிகாட்டி மட்டுமே; பன்னாட்டு ஒப்பந்தங்கள் அமல்படுத்தக்கூடிய உள்நாட்டுச் சட்டமாக மாற உறுப்பு 253-ன் கீழ் நாடாளுமன்றத்தால் இயற்றப்படும் செயலாக்கச் சட்டம் தேவைப்படுகிறது",
        "Yes. Article 51 overrides the legislative powers of State Assemblies during treaty making", "ஆம். ஒப்பந்தம் செய்யும் போது உறுப்பு 51 மாநில சட்டமன்றங்களின் சட்ட அதிகாரங்களை மிஞ்சுகிறது",
        "No. Treaties can only be enforced by the Governor of each state independently", "இல்லை. ஒப்பந்தங்களை ஒவ்வொரு மாநில ஆளுநரும் மட்டுமே சுயாதீனமாக அமல்படுத்த முடியும்",
        "B",
        "Article 51 is a Part IV DPSP guiding State foreign policy. India follows a 'dualist' system where international treaties are NOT automatically self-executing into domestic law. Parliament must enact implementing legislation under Article 253.",
        "உறுப்பு 51 என்பது பகுதி IV DPSP ஆகும். இந்தியா ஒரு 'இருத்துவ' முறையைப் பின்பற்றுகிறது, இதில் பன்னாட்டு ஒப்பந்தங்கள் தானாகவே உள்நாட்டுச் சட்டமாக மாறாது. நாடாளுமன்றம் உறுப்பு 253-ன் கீழ் செயலாக்கச் சட்டத்தை இயற்ற வேண்டும்.",
        "TNPSC Trap: Treaty enforcement into domestic law requires Parliamentary legislation under Article 253.",
        "டிஎன்பிஎஸ்சி பொறி: பன்னாட்டு ஒப்பந்தங்களை உள்நாட்டுச் சட்டமாக அமல்படுத்த உறுப்பு 253-ன் கீழ் நாடாளுமன்றச் சட்டம் தேவைப்படுகிறது.",
        "International treaties are not self-executing in India (Jolly George Varghese case).", "இந்தியாவில் பன்னாட்டு ஒப்பந்தங்கள் தானாகவே செயல்படுபவை அல்ல.",
        "Correct. Article 51 is a DPSP policy guide; Article 253 legislation is required for domestic treaty enforcement.", "சரி. உறுப்பு 51 ஒரு DPSP கொள்கை வழிகாட்டி; உள்நாட்டு ஒப்பந்த அமலாக்கத்திற்கு உறுப்பு 253 சட்டம் தேவைப்படுகிறது.",
        "Article 253 empowers Parliament, not state assemblies.", "உறுப்பு 253 நாடாளுமன்றத்திற்கு அதிகாரமளிக்கிறது, மாநில சட்டமன்றங்களுக்கு அல்ல.",
        "Governors cannot enforce treaties independently.", "ஆளுநர்கள் ஒப்பந்தங்களைச் சுயாதீனமாக அமல்படுத்த முடியாது."
    )

    # Output directory & file creation
    output_dir = "data/questions/polity"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "directive_principles_easy.json")

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)

    print(f"Successfully generated {len(questions)} DPSP Easy MCQs at {output_path}")

    # Answer Key audit
    counts = {"A": 0, "B": 0, "C": 0, "D": 0}
    for q in questions:
        counts[q["correct_answer"]] += 1
    print(f"Answer Key Distribution: A={counts['A']}, B={counts['B']}, C={counts['C']}, D={counts['D']}")

if __name__ == "__main__":
    generate_50_easy_mcqs()
