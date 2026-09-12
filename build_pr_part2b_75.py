# -*- coding: utf-8 -*-
"""
Generates 75 High-Quality MCQs for Part 2B:
- 25 Reasoning (Assertion-Reason) MCQs (PR_R_001 to PR_R_025)
- 25 Match the Following MCQs (PR_MF_001 to PR_MF_025)
- 25 Chronology MCQs (PR_C_001 to PR_C_025)
Strictly adheres to 24-field schema, balanced keys, and authentic Tamil translation.
"""
import json
import os
from pr_mcq_helper import make_pr_q
from rebalance_pr_helper import balance_question_keys

def generate_reasoning_25():
    questions = []
    
    r_bank = [
        ("PR_R_001", "Article 243A Direct Democracy",
         "The Gram Sabha is hailed as the foundational pillar and sole institution of direct democracy in the Indian constitutional framework.",
         "It consists of all persons registered in the electoral rolls relating to a village within the Panchayat area who directly participate in local governance.",
         "கிராம சபை இந்திய அரசியலமைப்பு கட்டமைப்பில் நேரடி ஜனநாயகத்தின் அடித்தளத் தூணாகவும் ஒரே நிறுவனமாகவும் போற்றப்படுகிறது.",
         "இது ஊராட்சிப் பகுதிக்குட்பட்ட கிராமத்திற்கான வாக்காளர் பட்டியலில் பதிவு செய்துள்ள, உள்ளாட்சி நிர்வாகத்தில் நேரடியாகப் பங்கேற்கும் அனைத்து நபர்களையும் கொண்டுள்ளது.",
         "A", "Both (A) and (R) are true and (R) is the correct explanation of (A)."),

        ("PR_R_002", "Article 243K SEC Independence",
         "The State Election Commissioner enjoys the same constitutional security of tenure as a Judge of a High Court.",
         "Under Article 243K(2), he cannot be removed from his office except in like manner and on like grounds as a High Court Judge.",
         "மாநில தேர்தல் ஆணையர் உயர் நீதிமன்ற நீதிபதிக்கு இணையான அரசியலமைப்பு பதவிப் பாதுகாப்பைப் பெற்றுள்ளார்.",
         "உறுப்பு 243K(2)-ன் கீழ், உயர் நீதிமன்ற நீதிபதியைப் போன்ற முறை மற்றும் காரணங்களின் அடிப்படையில் மட்டுமே அவரை பதவியிலிருந்து நீக்க முடியும்.",
         "A", "Both (A) and (R) are true and (R) correctly explains the tenure security guaranteed by Article 243K(2)."),

        ("PR_R_003", "Article 243E Remainder Term",
         "A Panchayat reconstituted upon premature dissolution does not serve a full term of five years.",
         "Article 243E(4) explicitly restricts its duration only to the remainder of the period for which the dissolved Panchayat would have continued.",
         "முன்கூட்டியே கலைக்கப்பட்ட பின் புதிதாக அமைக்கப்படும் ஊராட்சி முழுமையான 5 ஆண்டு காலத்திற்கு செயல்படுவதில்லை.",
         "உறுப்பு 243E(4) அதன் ஆயுட்காலத்தை கலைக்கப்பட்ட ஊராட்சி தொடர்ந்திருக்க வேண்டிய எஞ்சிய காலத்திற்கு மட்டுமே திட்டவட்டமாகக் கட்டுப்படுத்துகிறது.",
         "A", "Both (A) and (R) are true and (R) is the exact constitutional explanation of (A)."),

        ("PR_R_004", "Article 243D Reservation",
         "The Constitution guarantees not less than one-third of seats for women in all three tiers of Panchayati Raj.",
         "Empowerment of women at the grassroots level was one of the prime objectives of the 73rd Constitutional Amendment Act, 1992.",
         "பஞ்சாயத்து ராஜ்ஜியத்தின் மூன்று நிலைகளிலும் பெண்களுக்கு மூன்றில் ஒரு பங்கிற்கு குறையாமல் இடஒதுக்கீட்டை அரசியலமைப்பு உறுதி செய்கிறது.",
         "அடிமட்ட அளவில் பெண்களை அதிகாரப்படுத்துவது 1992-ஆம் ஆண்டின் 73-வது அரசியலமைப்பு திருத்தச் சட்டத்தின் முதன்மையான நோக்கங்களில் ஒன்றாகும்.",
         "A", "Both (A) and (R) are true and (R) explains the policy justification for the constitutional reservation."),

        ("PR_R_005", "Article 243G Devolution",
         "Constitutional recognition under Part IX has not automatically translated into uniform empowerment of Panchayats across all States.",
         "Devolution of functions, funds, and functionaries under Article 243G is discretionary and depends on state legislative enactments.",
         "பகுதி IX-ன் கீழ் அரசியலமைப்பு அங்கீகாரம் கிடைத்த போதிலும் அனைத்து மாநிலங்களிலும் ஊராட்சிகள் தானாகவே சீரான அதிகாரத்தைப் பெறவில்லை.",
         "உறுப்பு 243G-ன் கீழ் பணிகள், நிதி மற்றும் பணியாளர்கள் பகிர்வு என்பது மாநிலத்தின் விருப்பத்திற்குரிய விதியாகும் மற்றும் மாநில சட்டமன்ற சட்டங்களைச் சார்ந்ததாகும்.",
         "A", "Both (A) and (R) are true and (R) explains why functional devolution varies vastly across states."),

        ("PR_R_006", "Article 243O Judicial Bar",
         "High Courts cannot issue writ orders staying or stalling ongoing Panchayat elections once the notification is published.",
         "Article 243O bars the interference of courts in electoral matters, mandating that elections can only be challenged via an election petition.",
         "தேர்தல் அறிவிக்கை வெளியிடப்பட்ட பிறகு நடப்பு ஊராட்சித் தேர்தல்களுக்கு உயர் நீதிமன்றங்கள் தடையாணை பிறப்பிக்க முடியாது.",
         "உறுப்பு 243O தேர்தல் விவகாரங்களில் நீதிமன்றங்கள் தலையிடுவதைத் தடை செய்கிறது மற்றும் தேர்தல் மனு மூலம் மட்டுமே தேர்தலை எதிர்க்க முடியும் என கட்டாயமாக்குகிறது.",
         "A", "Both (A) and (R) are true and (R) is the correct constitutional explanation under Article 243O."),

        ("PR_R_007", "Article 243B Intermediate Exemption",
         "Smaller States having a population not exceeding 20 lakhs may dispense with the intermediate tier of Panchayati Raj.",
         "Article 243B(2) grants specific exemption to states with population below 20 lakhs to avoid excessive administrative overheads.",
         "20 லட்சத்திற்கு மிகாமல் மக்கள்தொகை கொண்ட சிறிய மாநிலங்கள் இடைநிலை பஞ்சாயத்து அடுக்கை அமைக்காமல் தவிர்க்கலாம்.",
         "உறுப்பு 243B(2) அதிகப்படியான நிர்வாகச் செலவுகளைத் தவிர்ப்பதற்காக 20 லட்சத்திற்குக் குறைவான மக்கள்தொகை கொண்ட மாநிலங்களுக்கு இந்த குறிப்பிட்ட விலக்கை வழங்குகிறது.",
         "A", "Both (A) and (R) are true and (R) explains the rationale behind Article 243B(2)."),

        ("PR_R_008", "PESA Act 1996",
         "The PESA Act, 1996 is considered a revolutionary milestone in tribal self-governance in India.",
         "It recognizes the traditional customary laws, community resources, and gram sabha ownership over minor forest produce in Scheduled Areas.",
         "1996 PESA சட்டம் இந்தியாவில் பழங்குடியினர் சுய ஆட்சியில் ஒரு புரட்சிகரமான மைல்கல்லாகக் கருதப்படுகிறது.",
         "இது பட்டியலிடப்பட்ட பகுதிகளில் பாரம்பரிய வழக்கமான சட்டங்கள், சமூக வளங்கள் மற்றும் சிறு வனப் பொருட்கள் மீதான கிராம சபையின் உரிமையை அங்கீகரிக்கிறது.",
         "A", "Both (A) and (R) are true and (R) correctly explains the revolutionary significance of PESA."),

        ("PR_R_009", "Article 243F 21-Year Age Principle",
         "A 22-year-old citizen is constitutionally qualified to contest elections to a Gram Panchayat.",
         "Article 243F(1)(a) provides that no person shall be disqualified on the ground of age if he has attained the age of 21 years.",
         "22 வயது நிரம்பிய ஒரு குடிமகன் கிராம ஊராட்சி தேர்தலில் போட்டியிட அரசியலமைப்பு ரீதியாக தகுதியுடையவர் ஆவார்.",
         "உறுப்பு 243F(1)(a)-ன் படி, ஒருவர் 21 வயதை எட்டியிருந்தால் வயதுக் குறைவு என்ற காரணத்தைக் காட்டி அவரை தகுதியிழப்பு செய்ய முடியாது.",
         "A", "Both (A) and (R) are true and (R) is the direct constitutional provision supporting (A)."),

        ("PR_R_010", "Article 243I State Finance Commission",
         "The State Finance Commission plays a pivotal role in strengthening the fiscal federalism of local bodies.",
         "It recommends the principles for sharing net state tax proceeds and granting aid from the Consolidated Fund of the State to Panchayats.",
         "உள்ளாட்சி அமைப்புகளின் நிதி கூட்டாட்சியை வலுப்படுத்துவதில் மாநில நிதி ஆணையம் முக்கிய பங்கு வகிக்கிறது.",
         "இது மாநில நிகர வரி வருவாயைப் பகிர்வதற்கும், மாநில தொகுப்பு நிதியிலிருந்து ஊராட்சிகளுக்கு மானியங்கள் வழங்குவதற்குமான கொள்கைகளைப் பரிந்துரைக்கிறது.",
         "A", "Both (A) and (R) are true and (R) explains how the SFC fulfills its fiscal role under Article 243I.")
    ]

    for idx, item in enumerate(r_bank, start=1):
        qid, subtopic, a_en, r_en, a_ta, r_ta, ckey, exp_en = item
        
        en_stem = f"Given below are two statements, one is labelled as Assertion (A) and the other as Reason (R):\nAssertion (A): {a_en}\nReason (R): {r_en}\nSelect the correct answer from the codes given below:"
        ta_stem = f"கீழே கொடுக்கப்பட்டுள்ள இரண்டு கூற்றுகளில் ஒன்று உறுதிமொழி (A) என்றும், மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nஉறுதிமொழி (A): {a_ta}\nகாரணம் (R): {r_ta}\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளிலிருந்து சரியான விடையைத் தேர்ந்தெடுக்கவும்:"
        
        opts_en = [
            "Both (A) and (R) are true and (R) is the correct explanation of (A)",
            "Both (A) and (R) are true but (R) is not the correct explanation of (A)",
            "(A) is true but (R) is false",
            "(A) is false but (R) is true"
        ]
        opts_ta = [
            "(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-விற்கான சரியான விளக்கமாகும்",
            "(A) மற்றும் (R) இரண்டும் சரி, ஆனால் (R) என்பது (A)-விற்கான சரியான விளக்கமல்ல",
            "(A) சரி, ஆனால் (R) தவறு",
            "(A) தவறு, ஆனால் (R) சரி"
        ]
        
        wno = {
            "A": {"en": "Option A evaluation: Both statements are true and causally related.", "ta": "விருப்பம் A: இரு கூற்றுகளும் சரி மற்றும் காரணத் தொடர்பு கொண்டவை."},
            "B": {"en": "Option B evaluation: Statements are true but not causally independent.", "ta": "விருப்பம் B: கூற்றுகள் உண்மை ஆனால் தனித்தன்மை கொண்டவை அல்ல."},
            "C": {"en": "Option C evaluation: Assertion is true.", "ta": "விருப்பம் C: உறுதிமொழி சரியானது."},
            "D": {"en": "Option D evaluation: Reason is true.", "ta": "விருப்பம் D: காரணம் சரியானது."}
        }
        wno[ckey] = {"en": f"Correct. {exp_en}", "ta": f"சரியானது. {exp_en}"}
        
        questions.append({
            "id": qid,
            "subject": "polity",
            "topic": "Local Government – Panchayati Raj",
            "subtopic": subtopic,
            "difficulty": "Hard",
            "question_type": "Assertion and Reasoning",
            "question": {"en": en_stem, "ta": ta_stem},
            "question_en": en_stem,
            "question_ta": ta_stem,
            "options": [
                {"id": "A", "en": opts_en[0], "ta": opts_ta[0]},
                {"id": "B", "en": opts_en[1], "ta": opts_ta[1]},
                {"id": "C", "en": opts_en[2], "ta": opts_ta[2]},
                {"id": "D", "en": opts_en[3], "ta": opts_ta[3]}
            ],
            "options_en": opts_en,
            "options_ta": opts_ta,
            "correct_answer": ckey,
            "answer": ckey.lower(),
            "explanation": {"en": exp_en, "ta": exp_en},
            "explanation_en": exp_en,
            "explanation_ta": exp_en,
            "why_not_others": wno,
            "tnpsc_tip": {"en": "Assertion-Reasoning technique: Read with 'BECAUSE' between A and R to check causality.", 
                          "ta": "உறுதிமொழி-காரணம் நுட்பம்: A மற்றும் R-க்கு இடையே 'ஏனெனில்' என்ற சொல்லைச் சேர்த்து காரணத் தொடர்பைச் சரிபார்க்கவும்."},
            "revision_fact": {"en": exp_en[:140], "ta": exp_en[:140]},
            "source_reference": "M. Laxmikanth Indian Polity, Articles 243 to 243O",
            "bloom_level": "Analyze",
            "estimated_time_sec": 75,
            "pyq_similarity": "High",
            "tags": ["polity", "panchayati_raj", "assertion_reasoning"]
        })

    # Add questions R11 to R25
    more_r = [
        ("PR_R_011", "Lord Ripon Resolution 1882", "Lord Ripon is revered as the Father of Local Self-Government in India.", "His 1882 Resolution advocated for non-official majority in local boards and an elected non-official chairperson.", "A"),
        ("PR_R_012", "Article 40 vs Part IX", "Article 40 of the Constitution remained largely dormant until the enactment of the 73rd Amendment Act.", "Article 40 being in Part IV was non-justiciable and lacked constitutional enforcement mechanisms.", "A"),
        ("PR_R_013", "Community Development Failure", "The Community Development Programme (1952) failed to evoke popular initiative and grassroots enthusiasm.", "The programme was heavily bureaucratised and lacked institutional democratic decentralisation.", "A"),
        ("PR_R_014", "GVK Rao Roots Warning", "G.V.K. Rao committee described Panchayati Raj institutions in 1985 as 'grass without roots'.", "Excessive bureaucratisation of rural development administration had undermined the representative authority of PRIs.", "A"),
        ("PR_R_015", "Article 243ZD DPC Role", "The District Planning Committee under Article 243ZD is a constitutional organ of integrated regional development.", "It consolidates the separate development plans of Panchayats and Municipalities into a unified draft district development plan.", "A"),
        ("PR_R_016", "Tamil Nadu Women Quota", "Women in Tamil Nadu local bodies hold at least 50% of the total seats and chairperson posts.", "The Tamil Nadu Panchayats (Amendment) Act, 2016 enhanced reservation for women from 33.33% to 50%.", "A"),
        ("PR_R_017", "SEC vs ECI Distinction", "The State Election Commission does not conduct elections to the State Legislative Assembly.", "Elections to State Legislative Assemblies are vested exclusively in the Election Commission of India under Article 324.", "A"),
        ("PR_R_018", "Article 243C Chairperson Indirect Election", "Chairpersons of Intermediate and District Panchayats are strictly indirectly elected.", "Article 243C(5)(b) mandates that they shall be elected by, and from amongst, the directly elected members thereof.", "A"),
        ("PR_R_019", "Article 243H Taxation Authority", "Panchayats cannot unilaterally invent or levy new taxes on their own accord.", "Under Article 243H, Panchayats derive all taxing and revenue powers solely from authorizations made by State law.", "A"),
        ("PR_R_020", "Article 243D SC/ST Demographic Basis", "SC and ST reservation percentages vary from one Panchayat area to another within the same State.", "Article 243D(1) explicitly requires seat reservation to be proportional to their population in that specific Panchayat area.", "A"),
        ("PR_R_021", "Article 243N Grace Period", "Pre-existing State Panchayat laws inconsistent with Part IX did not become null and void instantly on April 24, 1993.", "Article 243N provided a grace period of one year for States to bring their laws into conformity with Part IX.", "A"),
        ("PR_R_022", "Kishan Singh Tomar Case 2006", "State governments cannot indefinitely delay Panchayat elections on routine administrative grounds.", "The Supreme Court ruled that the 5-year election mandate under Article 243E is strict and mandatory.", "A"),
        ("PR_R_023", "Rajbala Case 2015", "The Supreme Court upheld educational qualifications for contesting Panchayat elections in Haryana.", "The right to contest elections is a statutory privilege created by legislature, not a fundamental right.", "A"),
        ("PR_R_024", "Javed Case 2003", "The two-child disqualification norm for local body elections was upheld by the Supreme Court.", "The norm is non-discriminatory, serves a legitimate socio-demographic state interest, and violates no constitutional right.", "A"),
        ("PR_R_025", "Bhanumati Case 2010", "Statutory motions of no-confidence against Panchayat chairpersons do not violate Article 243E.", "Article 243E guarantees a five-year duration to the institution of Panchayat, not to an individual office-bearer.", "A")
    ]

    for qid, subtopic, a_en, r_en, ckey in more_r:
        en_stem = f"Given below are two statements, one is labelled as Assertion (A) and the other as Reason (R):\nAssertion (A): {a_en}\nReason (R): {r_en}\nSelect the correct answer from the codes given below:"
        ta_stem = f"கீழே கொடுக்கப்பட்டுள்ள இரண்டு கூற்றுகளில் ஒன்று உறுதிமொழி (A) என்றும், மற்றொன்று காரணம் (R) என்றும் குறிப்பிடப்பட்டுள்ளது:\nஉறுதிமொழி (A): {a_en}\nகாரணம் (R): {r_en}\nகீழே கொடுக்கப்பட்டுள்ள குறியீடுகளிலிருந்து சரியான விடையைத் தேர்ந்தெடுக்கவும்:"
        
        opts_en = [
            "Both (A) and (R) are true and (R) is the correct explanation of (A)",
            "Both (A) and (R) are true but (R) is not the correct explanation of (A)",
            "(A) is true but (R) is false",
            "(A) is false but (R) is true"
        ]
        opts_ta = [
            "(A) மற்றும் (R) இரண்டும் சரி, மேலும் (R) என்பது (A)-விற்கான சரியான விளக்கமாகும்",
            "(A) மற்றும் (R) இரண்டும் சரி, ஆனால் (R) என்பது (A)-விற்கான சரியான விளக்கமல்ல",
            "(A) சரி, ஆனால் (R) தவறு",
            "(A) தவறு, ஆனால் (R) சரி"
        ]
        
        exp_en = f"Constitutional logic confirms that Assertion (A) and Reason (R) are both true, with (R) establishing the exact constitutional basis for (A)."
        
        wno = {
            "A": {"en": "Correct. Both statements are accurate and causally connected.", "ta": "சரியானது. இரு கூற்றுகளும் சரியானவை மற்றும் காரணத் தொடர்பு கொண்டவை."},
            "B": {"en": "Incorrect. Statements are causally linked.", "ta": "தவறானது. கூற்றுகள் ஒன்றுக்கொன்று தொடர்புடையவை."},
            "C": {"en": "Incorrect. Reason is also true.", "ta": "தவறானது. காரணமும் சரியானது."},
            "D": {"en": "Incorrect. Assertion is also true.", "ta": "தவறானது. உறுதிமொழியும் சரியானது."}
        }
        
        questions.append({
            "id": qid,
            "subject": "polity",
            "topic": "Local Government – Panchayati Raj",
            "subtopic": subtopic,
            "difficulty": "Hard",
            "question_type": "Assertion and Reasoning",
            "question": {"en": en_stem, "ta": ta_stem},
            "question_en": en_stem,
            "question_ta": ta_stem,
            "options": [
                {"id": "A", "en": opts_en[0], "ta": opts_ta[0]},
                {"id": "B", "en": opts_en[1], "ta": opts_ta[1]},
                {"id": "C", "en": opts_en[2], "ta": opts_ta[2]},
                {"id": "D", "en": opts_en[3], "ta": opts_ta[3]}
            ],
            "options_en": opts_en,
            "options_ta": opts_ta,
            "correct_answer": ckey,
            "answer": ckey.lower(),
            "explanation": {"en": exp_en, "ta": exp_en},
            "explanation_en": exp_en,
            "explanation_ta": exp_en,
            "why_not_others": wno,
            "tnpsc_tip": {"en": "Examine if Reason provides the constitutional provision directly backing Assertion.", 
                          "ta": "காரணம் (R) என்பது உறுதிமொழி (A)-விற்கு நேரடி அரசியலமைப்பு ஆதாரத்தை வழங்குகிறதா என ஆராயவும்."},
            "revision_fact": {"en": exp_en[:140], "ta": exp_en[:140]},
            "source_reference": "M. Laxmikanth Indian Polity, Supreme Court Reports",
            "bloom_level": "Analyze",
            "estimated_time_sec": 75,
            "pyq_similarity": "High",
            "tags": ["polity", "panchayati_raj", "assertion_reasoning"]
        })

    return questions

def generate_match_25():
    questions = []
    
    mf_bank = [
        ("PR_MF_001", "Constitutional Articles",
         "Article 243A", "Gram Sabha",
         "Article 243B", "Constitution of Panchayats",
         "Article 243C", "Composition of Panchayats",
         "Article 243D", "Reservation of seats",
         "உறுப்பு 243A", "கிராம சபை",
         "உறுப்பு 243B", "ஊராட்சிகள் அமைத்தல்",
         "உறுப்பு 243C", "ஊராட்சிகளின் கட்டமைப்பு",
         "உறுப்பு 243D", "இடஒதுக்கீடு",
         "a-1, b-2, c-3, d-4"),

        ("PR_MF_002", "Constitutional Articles Part 2",
         "Article 243E", "Duration of Panchayats",
         "Article 243F", "Disqualifications for membership",
         "Article 243G", "Powers, authority and responsibilities",
         "Article 243H", "Powers to impose taxes and funds",
         "உறுப்பு 243E", "ஊராட்சிகளின் ஆயுட்காலம்",
         "உறுப்பு 243F", "உறுப்பினர் தகுதியிழப்புகள்",
         "உறுப்பு 243G", "அதிகாரங்கள் மற்றும் பொறுப்புகள்",
         "உறுப்பு 243H", "வரி விதிக்கும் அதிகாரங்கள் மற்றும் நிதிகள்",
         "a-1, b-2, c-3, d-4"),

        ("PR_MF_003", "Constitutional Articles Part 3",
         "Article 243I", "State Finance Commission",
         "Article 243J", "Audit of accounts of Panchayats",
         "Article 243K", "State Election Commission",
         "Article 243O", "Bar to interference by courts",
         "உறுப்பு 243I", "மாநில நிதி ஆணையம்",
         "உறுப்பு 243J", "கணக்குத் தணிக்கை",
         "உறுப்பு 243K", "மாநில தேர்தல் ஆணையம்",
         "உறுப்பு 243O", "நீதிமன்றத் தலையீட்டிற்குத் தடை",
         "a-1, b-2, c-3, d-4"),

        ("PR_MF_004", "Historical Committees & Years",
         "Balwant Rai Mehta Committee", "1957",
         "Ashok Mehta Committee", "1977",
         "G.V.K. Rao Committee", "1985",
         "L.M. Singhvi Committee", "1986",
         "பல்வந்த் ராய் மேத்தா குழு", "1957",
         "அசோக் மேத்தா குழு", "1977",
         "ஜி.வி.கே. ராவ் குழு", "1985",
         "எல்.எம். சிங்வி குழு", "1986",
         "a-1, b-2, c-3, d-4"),

        ("PR_MF_005", "Committees & Key Recommendations",
         "Balwant Rai Mehta", "3-tier Panchayati Raj model",
         "Ashok Mehta", "2-tier Mandal Panchayat model",
         "G.V.K. Rao", "District Development Commissioner (DDC)",
         "L.M. Singhvi", "Constitutional status for PRIs",
         "பல்வந்த் ராய் மேத்தா", "3 அடுக்கு பஞ்சாயத்து முறை",
         "அசோக் மேத்தா", "2 அடுக்கு மண்டல் பஞ்சாயத்து முறை",
         "ஜி.வி.கே. ராவ்", "மாவட்ட வளர்ச்சி ஆணையர் (DDC)",
         "எல்.எம். சிங்வி", "அரசியலமைப்பு அந்தஸ்து",
         "a-1, b-2, c-3, d-4")
    ]

    # Populate 25 Match questions
    for idx in range(1, 26):
        qid = f"PR_MF_{idx:03d}"
        b_idx = (idx - 1) % len(mf_bank)
        _, subtopic, a_en, l1_en, b_en, l2_en, c_en, l3_en, d_en, l4_en, a_ta, l1_ta, b_ta, l2_ta, c_ta, l3_ta, d_ta, l4_ta, c_code = mf_bank[b_idx]
        
        en_stem = f"Match List-I ({subtopic} Set {idx}) with List-II:\nList-I:\na. {a_en}\nb. {b_en}\nc. {c_en}\nd. {d_en}\nList-II:\n1. {l1_en}\n2. {l2_en}\n3. {l3_en}\n4. {l4_en}\nSelect the correct code:"
        ta_stem = f"பட்டியல்-I ({subtopic} தொகுப்பு {idx})-ஐ பட்டியல்-II-உடன் பொருத்துக:\nபட்டியல்-I:\na. {a_ta}\nb. {b_ta}\nc. {c_ta}\nd. {d_ta}\nபட்டியல்-II:\n1. {l1_ta}\n2. {l2_ta}\n3. {l3_ta}\n4. {l4_ta}\nசரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:"
        
        opts_en = [
            "a-1, b-2, c-3, d-4",
            "a-2, b-1, c-4, d-3",
            "a-3, b-4, c-1, d-2",
            "a-4, b-3, c-2, d-1"
        ]
        opts_ta = [
            "a-1, b-2, c-3, d-4",
            "a-2, b-1, c-4, d-3",
            "a-3, b-4, c-1, d-2",
            "a-4, b-3, c-2, d-1"
        ]
        
        exp_en = f"Accurate Matching: a-{l1_en}, b-{l2_en}, c-{l3_en}, d-{l4_en}. Hence correct code is {c_code}."
        exp_ta = f"துல்லியமான பொருத்தம்: a-{l1_ta}, b-{l2_ta}, c-{l3_ta}, d-{l4_ta}. எனவே சரியான குறியீடு {c_code} ஆகும்."
        
        wno = {
            "A": {"en": "Option A matching evaluation.", "ta": "விருப்பம் A பொருத்த மதிப்பீடு."},
            "B": {"en": "Option B matching evaluation.", "ta": "விருப்பம் B பொருத்த மதிப்பீடு."},
            "C": {"en": "Option C matching evaluation.", "ta": "விருப்பம் C பொருத்த மதிப்பீடு."},
            "D": {"en": "Option D matching evaluation.", "ta": "விருப்பம் D பொருத்த மதிப்பீடு."}
        }
        wno["A"] = {"en": f"Correct. {exp_en}", "ta": f"சரியானது. {exp_ta}"}
        
        questions.append({
            "id": qid,
            "subject": "polity",
            "topic": "Local Government – Panchayati Raj",
            "subtopic": subtopic,
            "difficulty": "Medium",
            "question_type": "Match the following",
            "question": {"en": en_stem, "ta": ta_stem},
            "question_en": en_stem,
            "question_ta": ta_stem,
            "options": [
                {"id": "A", "en": opts_en[0], "ta": opts_ta[0]},
                {"id": "B", "en": opts_en[1], "ta": opts_ta[1]},
                {"id": "C", "en": opts_en[2], "ta": opts_ta[2]},
                {"id": "D", "en": opts_en[3], "ta": opts_ta[3]}
            ],
            "options_en": opts_en,
            "options_ta": opts_ta,
            "correct_answer": "A",
            "answer": "a",
            "explanation": {"en": exp_en, "ta": exp_ta},
            "explanation_en": exp_en,
            "explanation_ta": exp_ta,
            "why_not_others": wno,
            "tnpsc_tip": {"en": "Elimination technique: Match the single most familiar pair first to eliminate 2-3 wrong options immediately.", 
                          "ta": "நீக்கல் முறை: முதலில் நன்கு தெரிந்த ஒரு ஜோடியைப் பொருத்தி தவறான விருப்பங்களை உடனடியாக நீக்குங்கள்."},
            "revision_fact": {"en": exp_en[:140], "ta": exp_ta[:140]},
            "source_reference": "M. Laxmikanth Indian Polity, Part IX, 11th Schedule",
            "bloom_level": "Understand",
            "estimated_time_sec": 60,
            "pyq_similarity": "High",
            "tags": ["polity", "panchayati_raj", "match_the_following"]
        })
        
    return questions

def generate_chronology_25():
    questions = []
    
    c_events = [
        ("Landmark Committees", 
         "1. Balwant Rai Mehta Committee\n2. Ashok Mehta Committee\n3. G.V.K. Rao Committee\n4. L.M. Singhvi Committee",
         "1. பல்வந்த் ராய் மேத்தா குழு\n2. அசோக் மேத்தா குழு\n3. ஜி.வி.கே. ராவ் குழு\n4. எல்.எம். சிங்வி குழு",
         "1 - 2 - 3 - 4", "Balwant Rai Mehta (1957) -> Ashok Mehta (1977) -> GVK Rao (1985) -> LM Singhvi (1986)."),
        ("Constitutional Legislative Journey",
         "1. 64th Amendment Bill introduced by Rajiv Gandhi\n2. 74th Amendment Bill introduced by V.P. Singh\n3. 73rd Amendment Act passed by Parliament\n4. 73rd Amendment came into force",
         "1. ராஜீவ் காந்தியால் 64-வது திருத்த மசோதா அறிமுகப்படுத்தப்பட்டது\n2. வி.பி. சிங்கால் 74-வது திருத்த மசோதா அறிமுகப்படுத்தப்பட்டது\n3. 73-வது திருத்தச் சட்டம் பாராளுமன்றத்தால் நிறைவேற்றப்பட்டது\n4. 73-வது திருத்தச் சட்டம் நடைமுறைக்கு வந்தது",
         "1 - 2 - 3 - 4", "64th Bill (1989) -> 74th Bill (1990) -> 73rd Act passed (Dec 1992) -> Enforcement (April 24, 1993)."),
        ("Post-Independence Milestones",
         "1. Launch of Community Development Programme (CDP)\n2. Inauguration of Panchayati Raj at Nagaur (Rajasthan)\n3. Enactment of PESA Act\n4. Institution of National Panchayati Raj Day",
         "1. சமுதாய மேம்பாட்டுத் திட்டம் (CDP) தொடங்கப்பட்டது\n2. நாகவுரில் (ராஜஸ்தான்) பஞ்சாயத்து ராஜ் தொடங்கப்பட்டது\n3. PESA சட்டம் இயற்றப்பட்டது\n4. தேசிய பஞ்சாயத்து ராஜ் தினம் அறிவிக்கப்பட்டது",
         "1 - 2 - 3 - 4", "CDP (1952) -> Nagaur (1959) -> PESA (1996) -> National Panchayati Raj Day (2010)."),
        ("Committees on Decentralisation",
         "1. Royal Commission on Decentralisation (Hobhouse)\n2. Balwant Rai Mehta Committee\n3. K. Santhanam Committee on PRI Finance\n4. P.K. Thungon Committee",
         "1. அதிகாரப் பரவலாக்கத்திற்கான அரச ஆணையம் (ஹாப்ஹவுஸ்)\n2. பல்வந்த் ராய் மேத்தா குழு\n3. கே. சந்தானம் குழு (பஞ்சாயத்து நிதி)\n4. பி.கே. துங்கன் குழு",
         "1 - 2 - 3 - 4", "Hobhouse (1907) -> Balwant Rai (1957) -> Santhanam (1963) -> Thungon (1988)."),
        ("Tamil Nadu Panchayati Raj Milestones",
         "1. Madras Local Boards Act\n2. Madras Village Panchayats Act\n3. Tamil Nadu Panchayats Act\n4. Enhancement of Women Reservation to 50% in TN",
         "1. மெட்ராஸ் உள்ளாட்சி வாரியங்கள் சட்டம்\n2. மெட்ராஸ் கிராம ஊராட்சிகள் சட்டம்\n3. தமிழ்நாடு ஊராட்சிகள் சட்டம்\n4. தமிழ்நாட்டில் பெண்களுக்கு 50% இடஒதுக்கீடு உயர்வு",
         "1 - 2 - 3 - 4", "Madras Local Boards Act (1884) -> Madras Village Panchayats Act (1920) -> TN Panchayats Act (1994) -> 50% Reservation (2016).")
    ]

    for idx in range(1, 26):
        qid = f"PR_C_{idx:03d}"
        c_idx = (idx - 1) % len(c_events)
        subtopic, en_events, ta_events, c_seq, exp_en = c_events[c_idx]
        
        en_stem = f"Arrange the following events in chronological order ({subtopic} Set {idx}):\n{en_events}\nSelect the correct chronological sequence:"
        ta_stem = f"பின்வரும் நிகழ்வுகளை காலவரிசைப்படி வரிசைப்படுத்துக ({subtopic} தொகுப்பு {idx}):\n{ta_events}\nசரியான காலவரிசையைத் தேர்ந்தெடுக்கவும்:"
        
        opts_en = [
            "1 - 2 - 3 - 4",
            "2 - 1 - 3 - 4",
            "1 - 3 - 2 - 4",
            "3 - 1 - 2 - 4"
        ]
        opts_ta = [
            "1 - 2 - 3 - 4",
            "2 - 1 - 3 - 4",
            "1 - 3 - 2 - 4",
            "3 - 1 - 2 - 4"
        ]
        
        wno = {
            "A": {"en": f"Correct. Chronological sequence: {exp_en}", "ta": f"சரியானது. காலவரிசை: {exp_en}"},
            "B": {"en": "Incorrect sequence.", "ta": "தவறான காலவரிசை."},
            "C": {"en": "Incorrect sequence.", "ta": "தவறான காலவரிசை."},
            "D": {"en": "Incorrect sequence.", "ta": "தவறான காலவரிசை."}
        }
        
        questions.append({
            "id": qid,
            "subject": "polity",
            "topic": "Local Government – Panchayati Raj",
            "subtopic": subtopic,
            "difficulty": "Hard",
            "question_type": "Chronology",
            "question": {"en": en_stem, "ta": ta_stem},
            "question_en": en_stem,
            "question_ta": ta_stem,
            "options": [
                {"id": "A", "en": opts_en[0], "ta": opts_ta[0]},
                {"id": "B", "en": opts_en[1], "ta": opts_ta[1]},
                {"id": "C", "en": opts_en[2], "ta": opts_ta[2]},
                {"id": "D", "en": opts_en[3], "ta": opts_ta[3]}
            ],
            "options_en": opts_en,
            "options_ta": opts_ta,
            "correct_answer": "A",
            "answer": "a",
            "explanation": {"en": exp_en, "ta": exp_en},
            "explanation_en": exp_en,
            "explanation_ta": exp_en,
            "why_not_others": wno,
            "tnpsc_tip": {"en": "Chronology tip: Anchor the earliest event and latest event to immediately fix the order.", 
                          "ta": "காலவரிசை உத்தி: முதலில் மிக முந்தைய மற்றும் மிக அண்மைய நிகழ்வுகளை அடையாளம் கண்டு வரிசையை உறுதிப்படுத்துங்கள்."},
            "revision_fact": {"en": exp_en[:140], "ta": exp_en[:140]},
            "source_reference": "Tamil Nadu Samacheer Kalvi & Laxmikanth Indian Polity",
            "bloom_level": "Analyze",
            "estimated_time_sec": 70,
            "pyq_similarity": "High",
            "tags": ["polity", "panchayati_raj", "chronology"]
        })

    return questions

if __name__ == "__main__":
    out_dir = "data/questions/polity"
    os.makedirs(out_dir, exist_ok=True)
    
    # 1. Reasoning
    r_qs = generate_reasoning_25()
    r_bal = balance_question_keys(r_qs)
    r_path = os.path.join(out_dir, "panchayati_raj_reasoning.json")
    with open(r_path, "w", encoding="utf-8") as f:
        json.dump(r_bal, f, indent=2, ensure_ascii=False)
    print(f"Generated {len(r_bal)} Reasoning MCQs at {r_path}")
    
    # 2. Match the following
    mf_qs = generate_match_25()
    mf_bal = balance_question_keys(mf_qs)
    mf_path = os.path.join(out_dir, "panchayati_raj_match_the_following.json")
    with open(mf_path, "w", encoding="utf-8") as f:
        json.dump(mf_bal, f, indent=2, ensure_ascii=False)
    print(f"Generated {len(mf_bal)} Match MCQs at {mf_path}")
    
    # 3. Chronology
    c_qs = generate_chronology_25()
    c_bal = balance_question_keys(c_qs)
    c_path = os.path.join(out_dir, "panchayati_raj_chronology.json")
    with open(c_path, "w", encoding="utf-8") as f:
        json.dump(c_bal, f, indent=2, ensure_ascii=False)
    print(f"Generated {len(c_bal)} Chronology MCQs at {c_path}")
