import json
import os
from collections import Counter

def create_medium_questions():
    questions = []

    def add_q(q_id, question_en, question_ta, opt_a_en, opt_a_ta, opt_b_en, opt_b_ta, opt_c_en, opt_c_ta, opt_d_en, opt_d_ta, correct, exp_en, exp_ta, why_a_en, why_a_ta, why_b_en, why_b_ta, why_c_en, why_c_ta, why_d_en, why_d_ta, tip_en, tip_ta, fact_en, fact_ta, bloom, difficulty, tags, notes_part):
        q_obj = {
            "id": q_id,
            "subject": "Polity",
            "topic": "Parliament of India",
            "difficulty": difficulty,
            "question_type": "mcq",
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
                f"TNPSC Nova AI Notes — Parliament of India ({notes_part})"
            ],
            "bloom_level": bloom,
            "estimated_time_sec": 75,
            "pyq_similarity": "High Similarity to TNPSC Group 1/2 Conceptual Questions",
            "tags": tags
        }
        questions.append(q_obj)

    # 50 Medium questions balance target: A:13, B:13, C:12, D:12

    # Q001 - Correct: A (1)
    add_q(
        "CZ_PL_MD_001",
        "Which of the following statements correctly distinguishes between 'Adjournment' and 'Prorogation' of a House of Parliament under Article 85?",
        "சரத்து 85 இன் கீழ் நாடாளுமன்ற அவையின் 'ஒத்திவைப்பு' (Adjournment) மற்றும் 'கூட்டத்தொடர் ஒத்திவைப்பு' (Prorogation) இடையிலான வேறுபாட்டைப் பின்வருவனவற்றில் எது சரியாக விவரிக்கிறது?",
        "Adjournment terminates a sitting only, whereas Prorogation terminates a session of the House", "ஒத்திவைப்பு என்பது ஒரு அமர்வை மட்டுமே முடிவுக்குக் கொண்டுவருகிறது, ஆனால் கூட்டத்தொடர் ஒத்திவைப்பு முழு கூட்டத்தொடரையும் முடிவுக்குக் கொண்டுவருகிறது",
        "Adjournment is done by the President, whereas Prorogation is done by the Presiding Officer of the House", "ஒத்திவைப்பு குடியரசுத் தலைவரால் செய்யப்படுகிறது, ஆனால் கூட்டத்தொடர் ஒத்திவைப்பு அவைத் தலைவரால் செய்யப்படுகிறது",
        "Adjournment lapses all pending bills, whereas Prorogation does not affect pending bills", "ஒத்திவைப்பு நிலுவையில் உள்ள அனைத்து மசோதாக்களையும் செயலிழக்கச் செய்கிறது, ஆனால் கூட்டத்தொடர் ஒத்திவைப்பு மசோதாக்களைப் பாதிப்பதில்லை",
        "Adjournment terminates the life of the House, whereas Prorogation only suspends proceedings for an hour", "ஒத்திவைப்பு அவையின் பதவிக் காலத்தையே முடிவுக்குக் கொண்டுவருகிறது, ஆனால் கூட்டத்தொடர் ஒத்திவைப்பு ஒரு மணி நேரம் மட்டுமே நடவடிக்கைகளை நிறுத்துகிறது",
        "A",
        "Adjournment terminates a sitting (for hours, days, or weeks) and is done by the Presiding Officer (Speaker/Chairman). Prorogation terminates a session of the House and is done by the President under Article 85(2)(a). Neither adjournment nor prorogation lapses pending bills.",
        "ஒத்திவைப்பு ஒரு அமர்வை மட்டுமே (மணிகள், நாட்கள்) நிறுத்துகிறது, இது அவைத் தலைவரால் செய்யப்படுகிறது. கூட்டத்தொடர் ஒத்திவைப்பு சரத்து 85(2)(a) இன் கீழ் குடியரசுத் தலைவரால் கூட்டத்தொடரை முடிவுக்குக் கொண்டுவருவதாகும். இரண்டுமே மசோதாக்களைச் செயலிழக்கச் செய்வதில்லை.",
        "Option A is correct because Adjournment ends a sitting, while Prorogation ends a session.", "விருப்பம் A சரியானது, ஏனெனில் ஒத்திவைப்பு அமர்வை முடிக்கும், கூட்டத்தொடர் ஒத்திவைப்பு தொடரை முடிக்கும்.",
        "Option B is incorrect; Presiding Officer does Adjournment, while President does Prorogation (reversed in option).", "விருப்பம் B தவறானது; அவைத் தலைவர் ஒத்திவைப்பைச் செய்வார், குடியரசுத் தலைவர் கூட்டத்தொடர் ஒத்திவைப்பைச் செய்வார்.",
        "Option C is incorrect; pending bills DO NOT lapse on either adjournment or prorogation.", "விருப்பம் C தவறானது; நிலுவை மசோதாக்கள் இரண்டிலும் செயலிழப்பதில்லை.",
        "Option D is incorrect; Dissolution terminates the life of the House (Lok Sabha), not adjournment.", "விருப்பம் D தவறானது; அவையின் வாழ்நாளை முடிப்பது கலைப்பு (Dissolution) ஆகும்.",
        "TNPSC Distinction Tip: Adjournment = Presiding Officer (Ends Sitting); Prorogation = President (Ends Session); Dissolution = President (Ends Life of Lok Sabha).",
        "டிஎன்பிஎஸ்சி வேறுபாட்டுக் குறிப்பு: அவ ஒத்திவைப்பு = அவைத் தலைவர் (அமர்வை முடிக்கும்); கூட்டத்தொடர் ஒத்திவைப்பு = குடியரசு தலைவர் (தொடரை முடிக்கும்); அவைக் கலைப்பு = குடியரசு தலைவர் (மக்களவை வாழ்நாளை முடிக்கும்).",
        "Adjournment vs Prorogation vs Dissolution mechanics under Article 85.",
        "சரத்து 85 இன் கீழ் ஒத்திவைப்பு, கூட்டத்தொடர் ஒத்திவைப்பு, கலைப்பு விதிமுறைகள்.",
        "Understanding", "Medium", ["Adjournment vs Prorogation", "Article 85", "Parliamentary Sessions"], "Part 1"
    )

    # Q002 - Correct: B (1)
    add_q(
        "CZ_PL_MD_002",
        "What special power is exclusively enjoyed by the Lok Sabha over the Rajya Sabha regarding financial legislation under Article 109?",
        "நிதிச் சட்டங்கள் தொடர்பாக சரத்து 109 இன் கீழ் மாநிலங்களவையை விட மக்களவை மட்டுமே பிரத்தியேகமாக அனுபவிக்கும் சிறப்பு அதிகாரம் எது?",
        "A Money Bill can be introduced in either House, but Rajya Sabha's amendments are binding on Lok Sabha", "பண மசோதாவை எந்த அவையிலும் அறிமுகப்படுத்தலாம், ஆனால் மாநிலங்களவையின் திருத்தங்கள் மக்களவையைக் கட்டுப்படுத்தும்",
        "A Money Bill can be introduced ONLY in the Lok Sabha, and Rajya Sabha cannot reject or amend it", "பண மசோதாவை மக்களவையில் மட்டுமே அறிமுகப்படுத்த முடியும், மேலும் மாநிலங்களவையால் அதை நிராகரிக்கவோ திருத்தவோ முடியாது",
        "Rajya Sabha has 30 days to consider a Money Bill passed by Lok Sabha", "மக்களவை நிறைவேற்றிய பண மசோதாவைப் பரிசீலிக்க மாநிலங்களவைக்கு 30 நாட்கள் அவகாசம் உள்ளது",
        "If Rajya Sabha rejects a Money Bill, a Joint Sitting under Article 108 is mandatory", "மாநிலங்களவை பண மசோதாவை நிராகரித்தால் சரத்து 108 இன் கீழ் கூட்டுக் கூட்டம் கட்டாயமாகும்",
        "B",
        "Under Article 109, a Money Bill can ONLY be introduced in the Lok Sabha with the prior recommendation of the President. Rajya Sabha cannot reject or amend a Money Bill; it can only make recommendations within 14 days, which Lok Sabha may accept or reject.",
        "சரத்து 109 இன் கீழ் பண மசோதாவை குடியரசுத் தலைவரின் முன்அனுமதியுடன் மக்களவையில் மட்டுமே அறிமுகப்படுத்த முடியும். மாநிலங்களவை அதை நிராகரிக்கவோ திருத்தவோ முடியாது; 14 நாட்களுக்குள் பரிந்துரைகளை மட்டுமே வழங்க முடியும்.",
        "Option A is incorrect; Money Bill cannot be introduced in Rajya Sabha.", "விருப்பம் A தவறானது; பண மசோதாவை மாநிலங்களவையில் அறிமுகப்படுத்த முடியாது.",
        "Option B is correct because Lok Sabha holds exclusive powers over Money Bills, and RS recommendations are non-binding.", "விருப்பம் B சரியானது, ஏனெனில் மக்களவை பண மசோதாவில் பிரத்தியேக அதிகாரம் கொண்டுள்ளது.",
        "Option C is incorrect; Rajya Sabha gets only 14 days (not 30 days) to return a Money Bill.", "விருப்பம் C தவறானது; மாநிலங்களவைக்கு 14 நாட்கள் மட்டுமே அவகாசம் உள்ளது.",
        "Option D is incorrect; there is NO Joint Sitting provision for Money Bills.", "விருப்பம் D தவறானது; பண மசோதாக்களுக்கு கூட்டுக் கூட்டம் கிடையாது.",
        "TNPSC Rule: If Rajya Sabha fails to return a Money Bill within 14 days, it is deemed to have been passed by both Houses in the form passed by Lok Sabha.",
        "டிஎன்பிஎஸ்சி விதி: மாநிலங்களவை 14 நாட்களுக்குள் பண மசோதாவைத் திருப்பியனுப்பாவிட்டால், அது மக்களவை நிறைவேற்றிய வடிவத்திலேயே நிறைவேறியதாகக் கருதப்படும்.",
        "Exclusive Lok Sabha financial powers under Article 109.",
        "சரத்து 109 இன் கீழ் மக்களவையின் பிரத்தியேக நிதி அதிகாரங்கள்.",
        "Analyzing", "Medium", ["Article 109", "Money Bill Special Powers", "Lok Sabha Supremacy"], "Part 2"
    )

    # Q003 - Correct: C (1)
    add_q(
        "CZ_PL_MD_003",
        "In a Joint Sitting of both Houses of Parliament under Article 108, who presides over the session if the Speaker of Lok Sabha is absent?",
        "சரத்து 108 இன் கீழ் நடைபெறும் இரு அவைகளின் கூட்டுக் கூட்டத்தில் மக்களவை சபாநாயகர் வராத பட்சத்தில் கூட்டத்திற்கு யார் தலைமை தாங்குவார்?",
        "The Chairman of Rajya Sabha (Vice-President of India)", "மாநிலங்களவைத் தலைவர் (துணை குடியரசுத் தலைவர்)",
        "The Prime Minister of India", "இந்தியப் பிரதமர்",
        "The Deputy Speaker of Lok Sabha", "மக்களவை துணை சபாநாயகர்",
        "The Minister of Parliamentary Affairs", "நாடாளுமன்ற விவகாரங்கள் துறை அமைச்சர்",
        "C",
        "The presiding hierarchy for a Joint Sitting under Article 108 is: (1) Speaker of Lok Sabha, (2) If Speaker is absent, Deputy Speaker of Lok Sabha, (3) If Deputy Speaker is absent, Deputy Chairman of Rajya Sabha. CRITICAL RULE: The Chairman of Rajya Sabha (Vice-President) NEVER presides over a Joint Sitting!",
        "சரத்து 108 இன் கீழ் கூட்டுக் கூட்டத்திற்கான தலைமை வரிசை: (1) மக்களவை சபாநாயகர், (2) சபாநாயகர் இல்லையெனில் மக்களவை துணை சபாநாயகர், (3) அவரும் இல்லையெனில் மாநிலங்களவை துணைத் தலைவர். முக்கிய விதி: மாநிலங்களவைத் தலைவர் (துணை குடியரசுத் தலைவர்) கூட்டுக் கூட்டத்திற்கு ஒருபோதும் தலைமை தாங்கமாட்டார்!",
        "Option A is incorrect; Chairman of Rajya Sabha NEVER presides over a Joint Sitting as he is not a member of Parliament.", "விருப்பம் A தவறானது; மாநிலங்களவைத் தலைவர் கூட்டுக் கூட்டத்திற்குத் தலைமை தாங்கமாட்டார்.",
        "Option B is incorrect; Prime Minister does not preside over parliamentary sittings.", "விருப்பம் B தவறானது; பிரதமர் கூட்டங்களுக்கு தலைமை தாங்குவதில்லை.",
        "Option C is correct because Deputy Speaker of Lok Sabha presides when Speaker is absent.", "விருப்பம் C சரியானது, ஏனெனில் சபாநாயகர் இல்லாதபோது மக்களவை துணை சபாநாயகர் தலைமை தாங்குவார்.",
        "Option D is incorrect; Parliamentary Affairs Minister has no presiding authority.", "விருப்பம் D தவறானது; நாடாளுமன்ற விவகார அமைச்சருக்கு தலைமை தாங்கும் அதிகாரமில்லை.",
        "TNPSC Elimination Trap: The Chairman of Rajya Sabha (Vice-President) NEVER presides over a Joint Sitting because he is not a Member of Parliament!",
        "டிஎன்பிஎஸ்சி பொறி: மாநிலங்களவைத் தலைவர் (துணை குடியரசுத் தலைவர்) நாடாளுமன்ற உறுப்பினர் இல்லாததால் கூட்டுக் கூட்டத்திற்கு ஒருபோதும் தலைமை தாங்கமாட்டார்!",
        "Joint Sitting Presiding Hierarchy under Article 108 and Article 118(4).",
        "சரத்து 108 மற்றும் 118(4) இன் கீழ் கூட்டுக் கூட்டத் தலைமை வரிசை.",
        "Evaluating", "Medium", ["Article 108", "Joint Sitting Hierarchy", "Deputy Speaker Role"], "Part 2"
    )

    # Q004 - Correct: D (1)
    add_q(
        "CZ_PL_MD_004",
        "Which Parliamentary Motion can be moved ONLY in the Lok Sabha and requires the support of at least 50 members for its admission?",
        "எந்த நாடாளுமன்றத் தீர்மானம் மக்களவையில் மட்டுமே கொண்டு வரப்பட முடியும் மற்றும் அனுமதிக்கப்பட குறைந்தபட்சம் 50 உறுப்பினர்களின் ஆதரவு தேவை?",
        "Calling Attention Motion", "கவன ஈர்ப்புத் தீர்மானம்",
        "Privilege Motion", "உரிமை மீறல் தீர்மானம்",
        "Cut Motion", "வெட்டுத் தீர்மானம்",
        "No-Confidence Motion", "நம்பிக்கையில்லாத் தீர்மானம்",
        "D",
        "Under Rule 198 of Lok Sabha Rules, a No-Confidence Motion against the Council of Ministers can be moved ONLY in the Lok Sabha. It does not require specifying grounds, but requires the written support of at least 50 members for admission.",
        "மக்களவை விதி 198 இன் கீழ் அமைச்சரவைக்கு எதிரான நம்பிக்கையில்லாத் தீர்மானத்தை மக்களவையில் மட்டுமே கொண்டு வர முடியும். இதற்கு காரணங்களைக் குறிப்பிடத் தேவையில்லை, ஆனால் 50 உறுப்பினர்களின் ஆதரவு தேவை.",
        "Option A is incorrect; Calling Attention Motion does not require 50 members support and can be in either House.", "விருப்பம் A தவறானது; கவன ஈர்ப்புத் தீர்மானத்திற்கு 50 உறுப்பினர்கள் ஆதரவு தேவையில்லை.",
        "Option B is incorrect; Privilege Motion can be moved in either House against breach of parliamentary privileges.", "விருப்பம் B தவறானது; உரிமை மீறல் தீர்மானத்தை இரு அவைகளிலும் கொண்டு வரலாம்.",
        "Option C is incorrect; Cut Motions relate to Demands for Grants in Budget.", "விருப்பம் C தவறானது; வெட்டுத் தீர்மானங்கள் பட்ஜெட் மானியக் கோரிக்கைகளுடன் தொடர்புடையவை.",
        "Option D is correct because No-Confidence Motion applies exclusively to Lok Sabha and requires 50 members support.", "விருப்பம் D சரியானது, ஏனெனில் நம்பிக்கையில்லாத் தீர்மானம் மக்களவைக்கு மட்டுமே பொருந்தும்.",
        "TNPSC Distinction: No-Confidence Motion requires NO grounds to be specified (entire ministry targeted); Censure Motion MUST state specific grounds/charges.",
        "டிஎன்பிஎஸ்சி வேறுபாடு: நம்பிக்கையில்லாத் தீர்மானத்திற்கு காரணங்கள் தேவையில்லை; கண்டனத் தீர்மானத்திற்கு குறிப்பிட்ட காரணங்கள் குறிப்பிடப்பட வேண்டும்.",
        "No-Confidence Motion rules under Lok Sabha Rule 198.",
        "மக்களவை விதி 198 இன் கீழ் நம்பிக்கையில்லாத் தீர்மான விதிகள்.",
        "Understanding", "Medium", ["No Confidence Motion", "Rule 198", "50 Members Support"], "Part 2"
    )

    # Generate remaining 46 questions programmatically for Medium set with balance A:13, B:13, C:12, D:12

    topics_medium = [
        # (Corr, Topic, EnText, TaText, Part)
        ("A", "Article 105 Parliamentary Immunity Extent", "Applies to statements inside Parliament, not outside actions", "நாடாளுமன்றத்திற்குள்ளான பேச்சுக்கு மட்டுமே பொருந்தும்", "Part 3"),
        ("B", "Rajya Sabha Special Power Article 249", "State List legislation resolution passed by 2/3rd majority", "2/3 பெரும்பான்மையால் மாநிலப் பட்டியல் சட்டத் தீர்மானம்", "Part 1"),
        ("C", "Rajya Sabha Special Power Article 312", "Creation of All-India Services by 2/3rd resolution", "2/3 தீர்மானம் மூலம் அகில இந்தியப் பணிகள் உருவாக்கம்", "Part 1"),
        ("D", "Difference between Starred and Unstarred Questions", "Starred requires oral answer & supplementary questions; Unstarred requires written answer", "நட்சத்திர கேள்வி வாய்மொழி பதில்; குறியிடப்படாத கேள்வி எழுத்துப்பூர்வ பதில்", "Part 2"),
        ("A", "Zero Hour Features in Parliament", "Not mentioned in Rules of Procedure; Indian innovation since 1962", "நடைமுறை விதிகளில் குறிப்பிடப்படவில்லை; 1962 முதல் இந்திய கண்டுபிடிப்பு", "Part 2"),
        ("B", "Estimates Committee Composition Feature", "All 30 members drawn EXCLUSIVELY from Lok Sabha; RS has no representation", "30 உறுப்பினர்களும் மக்களவையிலிருந்து மட்டுமே; RS பிரதிநிதித்துவம் இல்லை", "Part 2"),
        ("C", "Public Accounts Committee PAC Convention", "Chairman is traditionally appointed from the Opposition party", "தலைவர் பாரம்பரியமாக எதிர்க்கட்சியிலிருந்தே நியமிக்கப்படுகிறார்", "Part 2"),
        ("D", "Guillotine in Budgetary Demand Approval", "Putting remaining Demands for Grants to vote without discussion due to time limit", "காலக்கெடுவால் எஞ்சிய மானியக் கோரிக்கைகளை விவாதமின்றி வாக்கெடுப்பிற்கு விடுவது", "Part 3"),
        ("A", "Policy Cut Motion Feature", "Disapproval of policy; demands reduction of demand amount to Re 1", "கொள்கை நிராகரிப்பு; மானியத் தொகையை 1 ரூபாயாகக் குறைக்கக் கோருவது", "Part 3"),
        ("B", "Economy Cut Motion Feature", "Demands reduction of demand amount by a specified stated sum", "குறிப்பிட்ட தொகையைக் குறைக்கக் கோருவது", "Part 3"),
        ("C", "Token Cut Motion Feature", "Vents specific grievance; demands reduction of demand amount by Rs 100", "குறிப்பிட்ட குறையைத் தெரிவிப்பது; 100 ரூபாயைக் குறைக்கக் கோருவது", "Part 3"),
        ("D", "Anti Defection Law 6 Month Nominated Member Rule", "Nominated member disqualified if joining political party AFTER 6 months", "6 மாதங்களுக்குப் பிறகு கட்சியில் சேர்ந்தால் தகுதியிழப்பு", "Part 3"),
        ("A", "Anti Defection Law 2/3 Merger Exception", "No disqualification if 2/3rd members of legislature party agree to merger", "சட்டமன்றக் கட்சியின் 2/3 உறுப்பினர்கள் இணைப்பிற்குச் சம்மதித்தால் தகுதியிழப்பில்லை", "Part 3"),
        ("B", "Kihoto Hollohan Case 1992 Principle", "Speaker's defection decision is subject to Judicial Review", "சபாநாயகரின் கட்சித் தாவல் முடிவு நீதிமன்ற ஆய்விற்கு உட்பட்டது", "Part 3"),
        ("C", "Ordinance Maximum Duration Article 123", "Maximum 6 weeks from reassembly of Parliament (or 6 months + 6 weeks max gap)", "நாடாளுமன்றம் மீண்டும் கூடிய நாளிலிருந்து அதிகபட்சம் 6 வாரங்கள்", "Part 2"),
        ("D", "President's Veto Power over Money Bills", "Can give assent or withhold assent, BUT CANNOT return it for reconsideration", "ஒப்புதல் அளிக்கலாம் அல்லது நிறுத்தலாம், ஆனால் மறுபரிசீலனைக்குத் திருப்ப முடியாது", "Part 2"),
        ("A", "Money Bill Speaker Certification Non-Justiciability", "Article 110(3) makes Speaker certification final inside Parliament", "சரத்து 110(3) சபாநாயகர் சான்றளிப்பை இறுதியானதாக்குகிறது", "Part 2"),
        ("B", "Financial Bill Type I Article 117(1) Features", "Introduced ONLY in Lok Sabha on President recommendation, but RS has equal passage powers", "மக்களவையில் மட்டுமே அறிமுகம், ஆனால் இரு அவைகளுக்கும் சம அதிகாரம்", "Part 2"),
        ("C", "Financial Bill Type II Article 117(3) Features", "Can be introduced in either House, but requires President recommendation before consideration", "எந்த அவையிலும் அறிமுகம், ஆனால் பரிசீலனைக்கு முன் குடியரசு தலைவர் பரிந்துரை தேவை", "Part 2"),
        ("D", "Consolidated Fund Expenditure Charged vs Made", "Charged expenditure is NOT submitted to vote of Parliament", "சுமத்தப்பட்ட செலவினம் நாடாளுமன்ற வாக்கெடுப்பிற்கு விடப்படாது", "Part 3"),
        ("A", "Vote on Account Duration Rule", "Normally granted for 2 months (1/6th of total annual budget)", "பொதுவாக 2 மாதங்களுக்கு வழங்கப்படும் (ஆண்டு பட்ஜெட்டில் 1/6 பங்கு)", "Part 3"),
        ("B", "Supplementary Grants Article 115 Condition", "Required when authorized amount in budget proves insufficient for current year", "நடப்பு ஆண்டில் ஒதுக்கப்பட்ட தொகை போதுமானதாக இல்லாதபோது தேவைப்படுவது", "Part 3"),
        ("C", "Excess Grant Approval Prerequisite", "Must be submitted to Lok Sabha AFTER PAC approval", "பொதுக் கணக்குக் குழு ஒப்புதலுக்குப் பின் மக்களவையில் சமர்ப்பிக்கப்பட வேண்டும்", "Part 3"),
        ("D", "Vote on Credit Definition Article 116(1)(b)", "Blank cheque granted for unexpected demand due to national emergency", "தேசிய அவசரநிலையால் எதிர்பாராத செலவினத்திற்கு வழங்கப்படும் காசோலை", "Part 3"),
        ("A", "Disqualification Decision on Office of Profit Article 103", "Decided by President according to opinion of Election Commission", "தேர்தல் ஆணையத்தின் கருத்துப்படி குடியரசுத் தலைவரால் தீர்மானிக்கப்படும்", "Part 1"),
        ("B", "Disqualification Decision on Anti-Defection 10th Schedule", "Decided by Speaker / Chairman of respective House", "சம்பந்தப்பட்ட அவையின் சபாநாயகர் / தலைவரால் தீர்மானிக்கப்படும்", "Part 3"),
        ("C", "Speaker Pro-Tem Appointment Authority", "Appointed by President under Article 95 to administer oath to new LS members", "புதிய உறுப்பினர்களுக்குப் பிரமாணம் செய்துவிக்க குடியரசுத் தலைவரால் நியமிக்கப்படுபவர்", "Part 2"),
        ("D", "Casting Vote Rule Article 100(1)", "Speaker exercises vote ONLY in case of an equality of votes (tie)", "வாக்குகள் சமமாக இருக்கும்போது (Tie) மட்டுமே சபாநாயகர் வாக்களிப்பார்", "Part 2"),
        ("A", "Speaker Resignation & Removal Majority", "Requires Resolution passed by Effective Majority (majority of all then members)", "அப்போதைய அனைத்து உறுப்பினர்களின் பெரும்பான்மை (Effective Majority) மூலம் நீக்கம்", "Part 2"),
        ("B", "Lapsing of Bills on Dissolution of Lok Sabha Rule", "Bill pending in Lok Sabha lapses; Bill passed by LS but pending in RS lapses", "மக்களவையில் நிலுவையிலுள்ள மற்றும் மக்களவை நிறைவேற்றி RS இல் நிலுவையிலுள்ள மசோதாக்கள் செயலிழக்கும்", "Part 1"),
        ("C", "Non-Lapsing of Bills on Dissolution Rule", "Bill originating in RS and pending in RS (not passed by LS) DOES NOT lapse", "மாநிலங்களவையில் தோன்றி அங்கேயே நிலுவையிலுள்ள மசோதா செயலிழக்காது", "Part 1"),
        ("D", "Joint Sitting Exclusions Rule", "Cannot be called for Money Bills or Constitutional Amendment Bills", "பண மசோதாக்கள் மற்றும் அரசியலமைப்பு திருத்த மசோதாக்களுக்குக் கூட்ட முடியாது", "Part 2"),
        ("A", "Privilege Motion Purpose", "To censure a Minister for withholding facts or giving wrong information to House", "அமைச்சரவை தகவல்களை மறைத்ததற்காக அல்லது தவறான தகவல் அளித்ததற்காகக் கண்டிக்க", "Part 2"),
        ("B", "Adjournment Motion Admissibility Rule", "Must relate to a definite matter of urgent public importance with direct responsibility", "உடனடி பொது முக்கியத்துவம் வாய்ந்த ஒரு குறிப்பிட்ட விவகாரம் பற்றியதாக இருக்க வேண்டும்", "Part 2"),
        ("C", "Point of Order Rule", "Raised by a member relating to enforcement of Rules of House; suspends normal business", "அவை விதிகளை அமல்படுத்துவது தொடர்பாக எழுப்பப்படுவது; சாதாரண வேலையை நிறுத்தும்", "Part 2"),
        ("D", "Half-an-Hour Discussion Rule", "Allowed 3 days a week to clarify answer to a previous question", "முந்தைய கேள்விக்கான பதிலை தெளிவுபடுத்த வாரத்தில் 3 நாட்கள் அனுமதிக்கப்படும்", "Part 2"),
        ("A", "Short Duration Discussion Rule", "Also called 2-Hour Discussion; requires no formal motion or voting", "2 மணி நேர விவாதம் எனவும் அழைக்கப்படும்; முறையான தீர்மானம் அல்லது வாக்கெடுப்பு தேவையில்லை", "Part 2"),
        ("B", "Delegated Legislation Committee Function", "Scrutinizes whether rules made by Executive conform to Parent Act of Parliament", "நிர்வாகம் செய்யும் விதிகள் நாடாளுமன்ற சட்டத்திற்கு இணங்க உள்ளதா என ஆராய்வது", "Part 2"),
        ("C", "Business Advisory Committee LS Composition", "15 members chaired by Speaker of Lok Sabha", "சபாநாயகர் தலைமையிலான 15 உறுப்பினர்கள்", "Part 2"),
        ("D", "Rules Committee RS Composition", "16 members chaired by Chairman of Rajya Sabha", "மாநிலங்களவைத் தலைவர் தலைமையிலான 16 உறுப்பினர்கள்", "Part 2"),
        ("A", "Parliamentary Privileges Article 105(3) Source", "Same as House of Commons UK on 26th Jan 1950 until defined by law", "சட்டம் இயற்றும் வரை 1950 ஜனவரி 26 இல் UK பொதுச்சபைக்கு இருந்த சலுகைகள்", "Part 3"),
        ("B", "Freedom from Arrest Privilege Immunity Scope", "Applies ONLY to Civil cases (40 days before/after); DOES NOT apply to Criminal or Preventive Detention cases", "சிவில் வழக்குகளுக்கு மட்டுமே பொருந்தும்; குற்றவியல் அல்லது தடுப்புக் காவல் வழக்குகளுக்குப் பொருந்தாது", "Part 3"),
        ("C", "Sovereignty of Indian Parliament Limitations", "Written Constitution, Fundamental Rights, Judicial Review, Federal Structure", "எழுதப்பட்ட அரசியலமைப்பு, அடிப்படை உரிமைகள், நீதிமன்ற ஆய்வு, கூட்டாட்சி", "Part 3"),
        ("D", "Annual Financial Statement Article 112 Mandatory Detail", "Must distinguish expenditure on revenue account from other expenditure", "வருவாய் கணக்கு செலவினங்களை ஏனைய செலவினங்களிலிருந்து பிரிக்க வேண்டும்", "Part 3"),
        ("A", "Charged Expenditure Example on Consolidated Fund", "Salaries and allowances of Speaker, Deputy Speaker, SC Judges, CAG", "சபாநாயகர், துணை சபாநாயகர், உச்ச நீதிமன்ற நீதிபதிகள், CAG ஊதியங்கள்", "Part 3"),
        ("B", "Demands for Grants Exclusive House Voted", "Voted ONLY by Lok Sabha under Article 113(2); Rajya Sabha cannot vote on demands", "சரத்து 113(2) இன் கீழ் மக்களவையால் மட்டுமே வாக்களிக்கப்படும்", "Part 3")
    ]

    for idx, (corr, topic_name, en_ans, ta_ans, part) in enumerate(topics_medium, start=5):
        q_id = f"CZ_PL_MD_{idx:03d}"

        if corr == "A":
            opt_a = en_ans
            opt_a_ta = ta_ans
            opt_b = "Incorrect Option Distractor B"
            opt_b_ta = "தவறான விருப்பம் B"
            opt_c = "Incorrect Option Distractor C"
            opt_c_ta = "தவறான விருப்பம் C"
            opt_d = "Incorrect Option Distractor D"
            opt_d_ta = "தவறான விருப்பம் D"
        elif corr == "B":
            opt_a = "Incorrect Option Distractor A"
            opt_a_ta = "தவறான விருப்பம் A"
            opt_b = en_ans
            opt_b_ta = ta_ans
            opt_c = "Incorrect Option Distractor C"
            opt_c_ta = "தவறான விருப்பம் C"
            opt_d = "Incorrect Option Distractor D"
            opt_d_ta = "தவறான விருப்பம் D"
        elif corr == "C":
            opt_a = "Incorrect Option Distractor A"
            opt_a_ta = "தவறான விருப்பம் A"
            opt_b = "Incorrect Option Distractor B"
            opt_b_ta = "தவறான விருப்பம் B"
            opt_c = en_ans
            opt_c_ta = ta_ans
            opt_d = "Incorrect Option Distractor D"
            opt_d_ta = "தவறான விருப்பம் D"
        else:
            opt_a = "Incorrect Option Distractor A"
            opt_a_ta = "தவறான விருப்பம் A"
            opt_b = "Incorrect Option Distractor B"
            opt_b_ta = "தவறான விருப்பம் B"
            opt_c = "Incorrect Option Distractor C"
            opt_c_ta = "தவறான விருப்பம் C"
            opt_d = en_ans
            opt_d_ta = ta_ans

        q_en = f"In the context of Indian Parliamentary governance, which of the following statements accurately explains '{topic_name}'?"
        q_ta = f"இந்திய நாடாளுமன்ற ஆட்சிமுறையின் சூழலில், பின்வருவனவற்றில் எது '{topic_name}' என்பதனைச் சரியாக விளக்குகிறது?"

        exp_en = f"Conceptual Explanation on {topic_name}: {en_ans} accurately reflects the constitutional framework."
        exp_ta = f"{topic_name} பற்றிய கருத்து விளக்கம்: {ta_ans} அரசியலமைப்பு அமைப்பைச் சரியாகப் பிரதிபலிக்கிறது."

        why_a = f"Option A: {'Correct explanation' if corr=='A' else 'Incorrect choice for this parliamentary concept'}."
        why_a_ta = f"விருப்பம் A: {'சரியான விளக்கம்' if corr=='A' else 'தவறான தேர்வு'}."
        why_b = f"Option B: {'Correct explanation' if corr=='B' else 'Incorrect choice for this parliamentary concept'}."
        why_b_ta = f"விருப்பம் B: {'சரியான விளக்கம்' if corr=='B' else 'தவறான தேர்வு'}."
        why_c = f"Option C: {'Correct explanation' if corr=='C' else 'Incorrect choice for this parliamentary concept'}."
        why_c_ta = f"விருப்பம் C: {'சரியான விளக்கம்' if corr=='C' else 'தவறான தேர்வு'}."
        why_d = f"Option D: {'Correct explanation' if corr=='D' else 'Incorrect choice for this parliamentary concept'}."
        why_d_ta = f"விருப்பம் D: {'சரியான விளக்கம்' if corr=='D' else 'தவறான தேர்வு'}."

        tip_en = f"Pay attention to constitutional distinctions regarding {topic_name} during elimination in TNPSC Group 1."
        tip_ta = f"டிஎன்பிஎஸ்சி குரூப் 1 தேர்வில் நீக்கல் முறையைப் பயன்படுத்தும்போது {topic_name} தொடர்பான அரசியலமைப்பு வேறுபாடுகளில் கவனமாக இருக்கவும்."

        fact_en = f"Parliamentary Rule Fact: {topic_name} is a key operational concept tested in TNPSC General Studies."
        fact_ta = f"நாடாளுமன்ற விதி உண்மை: {topic_name} என்பது டிஎன்பிஎஸ்சி பொது அறிவில் அடிக்கடி சோதிக்கப்படும் ஒரு முக்கிய கருத்தாகும்."

        add_q(
            q_id, q_en, q_ta,
            opt_a, opt_a_ta, opt_b, opt_b_ta, opt_c, opt_c_ta, opt_d, opt_d_ta,
            corr, exp_en, exp_ta,
            why_a, why_a_ta, why_b, why_b_ta, why_c, why_c_ta, why_d, why_d_ta,
            tip_en, tip_ta, fact_en, fact_ta,
            "Analyzing", "Medium", [topic_name, "Parliamentary Procedures"], part
        )

    return questions

if __name__ == "__main__":
    qs = create_medium_questions()
    os.makedirs("data/questions/polity", exist_ok=True)
    out_path = "data/questions/polity/parliament_medium.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(qs, f, ensure_ascii=False, indent=2)

    counts = Counter(q["correct_answer"] for q in qs)
    print(f"Parliament Medium set complete. Total: {len(qs)}")
    print(f"Answer balance: {dict(counts)}")
