# Constitutional Amendments - 50 Easy MCQs Builder Script
# File: data/questions/polity/constitutional_amendments_easy.json
# Target Distribution: A: 13, B: 13, C: 12, D: 12 (Total 50)

import json
import os

def create_easy_questions():
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
            "difficulty": "Easy",
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
            "estimated_time_sec": 45,
            "pyq_similarity": pyq_sim,
            "tags": tags
        })

    # Q001 - Correct: A
    add_q(
        "CZ_AM_EZ_001",
        "Which Article in Part XX of the Indian Constitution grants Parliament the power to amend the Constitution and lays down its procedure?",
        "இந்திய அரசியலமைப்பின் XX பகுதியில் உள்ள எந்த சரத்து, அரசியலமைப்பைத் திருத்துவதற்கான நாடாளுமன்றத்தின் அதிகாரத்தையும் அதன் நடைமுறையையும் அளிக்கிறது?",
        "Article 368", "சரத்து 368",
        "Article 356", "சரத்து 356",
        "Article 360", "சரத்து 360",
        "Article 370", "சரத்து 370",
        "A",
        "Article 368 in Part XX of the Constitution deals exclusively with the power of Parliament to amend the Constitution and its procedure.",
        "சரத்து 368, அரசியலமைப்பின் பகுதி XX இல் அமைந்திருந்து, நாடாளுமன்றத்தின் அரசியலமைப்பு திருத்த அதிகாரம் மற்றும் நடைமுறையை மட்டுமே கையாள்கிறது.",
        "Option A is correct because Article 368 contains the constitutional amendment provisions.", "விருப்பம் A சரியானது, ஏனெனில் சரத்து 368 அரசியலமைப்பு திருத்த விதிகளைக் கொண்டுள்ளது.",
        "Option B relates to President's Rule in States, not constitutional amendments.", "விருப்பம் B மாநிலத்தில் குடியரசுத் தலைவர் ஆட்சியைக் குறிப்பிடுகிறது, திருத்த நடைமுறை அல்ல.",
        "Option C relates to Financial Emergency under Article 360.", "விருப்பம் C சரத்து 360 இன் கீழ் நிதி நெருக்கடியைக் குறிப்பிடுகிறது.",
        "Option D relates to temporary provisions regarding Jammu and Kashmir.", "விருப்பம் D ஜம்மு-காஷ்மீர் தொடர்பான தற்காலிக விதிகளைக் குறிப்பிடுகிறது.",
        "Remember that Part XX contains only one single Article, which is Article 368.",
        "பகுதி XX இல் ஒரே ஒரு சரத்து மட்டுமே உள்ளது, அது சரத்து 368 என்பதை நினைவில் கொள்க.",
        "Article 368 was amended by the 24th Amendment Act, 1971, to clarify Parliament's amending power.",
        "24வது திருத்தச் சட்டம், 1971 மூலம் சரத்து 368 நாடாளுமன்றத் திருத்த அதிகாரத்தைத் தெளிவுபடுத்தத் திருத்தப்பட்டது.",
        "Remembering", "High", ["Article 368", "Part XX", "Procedure"], "Part 1"
    )

    # Q002 - Correct: B
    add_q(
        "CZ_AM_EZ_002",
        "A bill for the amendment of the Constitution can be initiated in which of the following bodies?",
        "அரசியலமைப்புத் திருத்த மசோதாவை பின்வரும் எந்த அமைப்பில் மட்டுமே அறிமுகப்படுத்த முடியும்?",
        "Only in the Lok Sabha", "மக்களவையில் மட்டுமே",
        "Either House of Parliament", "நாடாளுமன்றத்தின் ஏதேனும் ஒரு அவையில்",
        "Only in the State Legislative Assemblies", "மாநில சட்டமன்றங்களில் மட்டுமே",
        "In a Joint Sitting of both Houses of Parliament", "நாடாளுமன்ற இரு அவைகளின் கூட்டு அமர்வில்",
        "B",
        "An amendment bill can be initiated in either House of Parliament (Lok Sabha or Rajya Sabha), but NOT in state legislatures.",
        "அரசியலமைப்புத் திருத்த மசோதா நாடாளுமன்றத்தின் மக்களவை அல்லது மாநிலங்களவை ஆகிய இரண்டில் ஏதேனும் ஒரு அவையில் அறிமுகப்படுத்தப்படலாம்; மாநில சட்டமன்றங்களில் முடியாது.",
        "Option A is incorrect because amendment bills are not restricted to Lok Sabha alone; Rajya Sabha can also initiate them.", "விருப்பம் A தவறானது, ஏனெனில் திருத்த மசோதாக்கள் மக்களவையில் மட்டுமே அறிமுகப்படுத்தப்பட வேண்டியதில்லை; மாநிலங்களவையிலும் அறிமுகப்படுத்தலாம்.",
        "Option B is correct as per Article 368(2), which allows initiation in either Lok Sabha or Rajya Sabha.", "விருப்பம் B சரியானது, சரத்து 368(2) இன் படி மக்களவை அல்லது மாநிலங்களவை இரண்டிலும் அறிமுகப்படுத்தலாம்.",
        "Option C is incorrect because State Assemblies have no power to initiate constitutional amendment bills.", "விருப்பம் C தவறானது, ஏனெனில் மாநில சட்டமன்றங்களுக்கு அரசியலமைப்பு திருத்த மசோதாவை அறிமுகப்படுத்தும் அதிகாரம் இல்லை.",
        "Option D is incorrect because amendment bills cannot be initiated in a joint sitting; joint sitting is not even permitted for amendment bills.", "விருப்பம் D தவறானது, ஏனெனில் கூட்டு அமர்வில் அறிமுகப்படுத்த முடியாது; திருத்த மசோதாக்களுக்கு கூட்டு அமர்வே கிடையாது.",
        "State Legislatures CANNOT initiate constitutional amendment bills under any circumstances under Article 368.",
        "சரத்து 368 இன் கீழ் எந்தச் சூழ்நிலையிலும் மாநில சட்டமன்றங்களால் அரசியலமைப்புத் திருத்த மசோதாவை அறிமுகப்படுத்த முடியாது.",
        "Initiation of constitutional amendment requires no prior permission from the President.",
        "அரசியலமைப்புத் திருத்த மசோதாவை அறிமுகப்படுத்த குடியரசுத் தலைவரின் முன்அனுமதி தேவையில்லை.",
        "Remembering", "High", ["Initiation", "Parliament", "Article 368"], "Part 1"
    )

    # Q003 - Correct: C
    add_q(
        "CZ_AM_EZ_003",
        "Prior recommendation of which constitutional authority is NOT required for introducing a Constitutional Amendment Bill in Parliament?",
        "நாடாளுமன்றத்தில் அரசியலமைப்பு திருத்த மசோதாவை அறிமுகப்படுத்துவதற்கு பின்வரும் எந்த அரசியலமைப்பு அதிகாரியின் முன்அனுமதி தேவை இல்லை?",
        "Prime Minister of India", "இந்தியப் பிரதமர்",
        "Speaker of Lok Sabha", "மக்களவைத் தலைவர்",
        "President of India", "இந்தியக் குடியரசுத் தலைவர்",
        "Chief Justice of India", "இந்தியத் தலைமை நீதிபதி",
        "C",
        "Unlike money bills or financial bills, a Constitutional Amendment Bill does NOT require prior recommendation of the President.",
        "பண மசோதாக்கள் அல்லது நிதி மசோதாக்கள் போல் அல்லாமல், அரசியலமைப்புத் திருத்த மசோதாவிற்கு குடியரசுத் தலைவரின் முன்அனுமதி தேவை இல்லை.",
        "Option A is incorrect because the PM recommendation is not a formal constitutional requirement for bill introduction.", "விருப்பம் A தவறானது, ஏனெனில் பிரதமர் அனுமதி அரசியலமைப்பு சார்ந்த கட்டாய முன்அனுமதி அல்ல.",
        "Option B is incorrect because Speaker presiding role does not involve prior recommendation for introduction.", "விருப்பம் B தவறானது, ஏனெனில் சபாநாயகரின் முன்அனுமதி அறிமுகப்படுத்த தேவையில்லை.",
        "Option C is correct because the President's prior recommendation is NOT required for constitutional amendment bills under Art 368.", "விருப்பம் C சரியானது, ஏனெனில் சரத்து 368 இன் கீழ் குடியரசுத் தலைவரின் முன்அனுமதி அரசியலமைப்பு திருத்த மசோதாவிற்குத் தேவை இல்லை.",
        "Option D is incorrect because the CJI plays no role in the legislative introduction process.", "விருப்பம் D தவறானது, ஏனெனில் சட்டமுன்வடிவு அறிமுகத்தில் தலைமை நீதிபதிக்கு எந்தப் பங்கும் இல்லை.",
        "Money Bills (Art 110) require President's prior permission, but Constitutional Amendment Bills (Art 368) do NOT.",
        "பண மசோதாக்களுக்கு (சரத்து 110) குடியரசுத் தலைவரின் முன்அனுமதி தேவை, ஆனால் அரசியலமைப்பு திருத்த மசோதாக்களுக்குத் (சரத்து 368) தேவை இல்லை.",
        "Private members can also introduce Constitutional Amendment Bills without President's recommendation.",
        "தனியார் உறுப்பினர்களும் குடியரசுத் தலைவரின் பரிந்துரை இன்றி அரசியலமைப்பு திருத்த மசோதாவை அறிமுகப்படுத்தலாம்.",
        "Understanding", "High", ["President Assent", "Bill Introduction"], "Part 1"
    )

    # Q004 - Correct: D
    add_q(
        "CZ_AM_EZ_004",
        "Is there any provision for a joint sitting of both Houses of Parliament to resolve a deadlock over a Constitutional Amendment Bill?",
        "அரசியலமைப்பு திருத்த மசோதாவில் முடக்கம் ஏற்படும் போது நாடாளுமன்றத்தின் இரு அவைகளின் கூட்டு அமர்விற்கு அரசியலமைப்பில் வழிவகை உள்ளதா?",
        "Yes, convened by the Speaker", "ஆம், சபாநாயகரால் கூட்டப்படுகிறது",
        "Yes, convened by the President", "ஆம், குடியரசுத் தலைவரால் கூட்டப்படுகிறது",
        "Yes, if passed by 2/3 states", "ஆம், 2/3 மாநிலங்கள் ஒப்புதல் அளித்தால்",
        "No, there is no provision for a joint sitting", "இல்லை, கூட்டு அமர்விற்கு எவ்வித வழிவகையும் இல்லை",
        "D",
        "There is NO provision for holding a joint sitting of both Houses under Article 108 for resolving a deadlock over a Constitutional Amendment Bill. Each House must pass it separately.",
        "அரசியலமைப்பு திருத்த மசோதாவில் முடக்கம் ஏற்பட்டால் சரத்து 108 இன் கீழ் இரு அவைகளின் கூட்டு அமர்வைக் கூட்டுவதற்கு எவ்வித வழிவகையும் இல்லை. ஒவ்வொரு அவையும் தனித்தனியாக நிறைவேற்ற வேண்டும்.",
        "Option A is incorrect because Speaker cannot convene a joint sitting for CA bills.", "விருப்பம் A தவறானது, ஏனெனில் சபாநாயகர் திருத்த மசோதாவிற்கு கூட்டு அமர்வைக் கூட்ட முடியாது.",
        "Option B is incorrect because President cannot summon a joint sitting for amendment bills.", "விருப்பம் B தவறானது, ஏனெனில் குடியரசுத் தலைவரும் திருத்த மசோதாவிற்கு கூட்டு அமர்வைக் கூட்ட முடியாது.",
        "Option C is incorrect because state ratification comes after both Houses pass it separately.", "விருப்பம் C தவறானது, ஏனெனில் மாநில ஒப்புதல் என்பது இரு அவைகளும் தனித்தனியாக நிறைவேற்றிய பின் மட்டுமே வரும்.",
        "Option D is correct because joint sitting under Article 108 applies ONLY to ordinary bills and financial bills, NOT to constitutional amendment bills.", "விருப்பம் D சரியானது, ஏனெனில் சரத்து 108 இன் கீழ் கூட்டு அமர்வு சாதாரண மசோதாக்களுக்கு மட்டுமே பொருந்தும், திருத்த மசோதாக்களுக்குப் பொருந்தாது.",
        "TNPSC Trap: Joint sitting exists for Ordinary Bills (Art 108), but NOT for Money Bills (Art 110) or Constitutional Amendment Bills (Art 368).",
        "டிஎன்பிஎஸ்சி முக்கிய குறிப்பு: சாதாரண மசோதாக்களுக்கு மட்டுமே கூட்டு அமர்வு உண்டு (சரத்து 108); பண மசோதா மற்றும் அரசியலமைப்பு திருத்த மசோதாக்களுக்கு கூட்டு அமர்வு கிடையாது.",
        "Each House must pass the amendment bill individually by the required special majority.",
        "ஒவ்வொரு அவையும் திருத்த மசோதாவை தேவையான சிறப்பு பெரும்பான்மையுடன் தனித்தனியாக நிறைவேற்ற வேண்டும்.",
        "Understanding", "High", ["Joint Sitting", "Article 108", "Deadlock"], "Part 1"
    )

    # Q005 - Correct: A
    add_q(
        "CZ_AM_EZ_005",
        "By which Constitutional Amendment Act was the President made constitutionally bound to give assent to a Constitutional Amendment Bill?",
        "எந்த அரசியலமைப்பு திருத்தச் சட்டத்தின் மூலம் அரசியலமைப்பு திருத்த மசோதாவிற்கு குடியரசுத் தலைவர் கட்டாயமாக ஒப்புதல் அளிக்க வேண்டும் என மாற்றப்பட்டது?",
        "24th Constitutional Amendment Act, 1971", "24வது அரசியலமைப்பு திருத்தச் சட்டம், 1971",
        "42nd Constitutional Amendment Act, 1976", "42வது அரசியலமைப்பு திருத்தச் சட்டம், 1976",
        "44th Constitutional Amendment Act, 1978", "44வது அரசியலமைப்பு திருத்தச் சட்டம், 1978",
        "1st Constitutional Amendment Act, 1951", "1வது அரசியலமைப்பு திருத்தச் சட்டம், 1951",
        "A",
        "The 24th Constitutional Amendment Act, 1971 amended Article 368 to make it mandatory for the President to give assent to a Constitutional Amendment Bill.",
        "24வது அரசியலமைப்பு திருத்தச் சட்டம், 1971 சரத்து 368 ஐத் திருத்தி, அரசியலமைப்பு திருத்த மசோதாவிற்கு குடியரசுத் தலைவர் ஒப்புதல் அளிப்பதைக் கட்டாயமாக்கியது.",
        "Option A is correct because the 24th Amendment substituted 'shall give his assent' in Article 368(2).", "விருப்பம் A சரியானது, ஏனெனில் 24வது திருத்தம் சரத்து 368(2) இல் 'ஒப்புதல் அளிக்க வேண்டும்' என்று மாற்றியது.",
        "Option B is incorrect; 42nd Amendment made council advice binding on President for executive functions, not Article 368 assent obligation.", "விருப்பம் B தவறானது; 42வது திருத்தம் நிர்வாக செயல்பாடுகளுக்கான அமைச்சரவை ஆலோசனையைக் கட்டாயமாக்கியது.",
        "Option C is incorrect; 44th Amendment modified emergency provisions and cabinet written advice.", "விருப்பம் C தவறானது; 44வது திருத்தம் அவசரநிலை விதிகளை திருத்தியது.",
        "Option D is incorrect; 1st Amendment added 9th Schedule and Article 15(4).", "விருப்பம் D தவறானது; 1வது திருத்தம் 9வது அட்டவணை மற்றும் சரத்து 15(4) ஐ சேர்த்தது.",
        "The President cannot withhold assent nor return a Constitutional Amendment Bill for reconsideration.",
        "குடியரசுத் தலைவர் அரசியலமைப்பு திருத்த மசோதாவிற்கு ஒப்புதலை நிறுத்தவோ அல்லது மறுபரிசீலனைக்குத் திருப்பியனுப்பவோ முடியாது.",
        "Before 1971, the President had discretion under Article 111, which was modified for Art 368 bills by the 24th Amendment.",
        "1971க்கு முன் இருந்த விருப்ப அதிகாரத்தை 24வது திருத்தம் சரத்து 368 மசோதாக்களுக்கு நீக்கியது.",
        "Remembering", "High", ["24th Amendment", "President Assent"], "Part 1"
    )

    # Q006 - Correct: B
    add_q(
        "CZ_AM_EZ_006",
        "Which schedule of the Indian Constitution was added by the 1st Constitutional Amendment Act of 1951?",
        "1951 ஆம் ஆண்டின் 1வது அரசியலமைப்பு திருத்தச் சட்டத்தின் மூலம் இந்திய அரசியலமைப்பில் சேர்க்கப்பட்ட அட்டவணை எது?",
        "8th Schedule", "8வது அட்டவணை",
        "9th Schedule", "9வது அட்டவணை",
        "10th Schedule", "10வது அட்டவணை",
        "11th Schedule", "11வது அட்டவணை",
        "B",
        "The 1st Constitutional Amendment Act, 1951 introduced the 9th Schedule to protect land reform laws from judicial review on grounds of fundamental rights violation.",
        "1951 இன் 1வது அரசியலமைப்பு திருத்தச் சட்டம், நில சீர்திருத்தச் சட்டங்களை அடிப்படை உரிமைகள் மீறல் என்ற காரணத்தினால் நீதித்துறை மறுாய்விலிருந்து பாதுகாக்க 9வது அட்டவணையைச் சேர்த்தது.",
        "Option A is incorrect; 8th Schedule was in the original Constitution containing 14 official languages.", "விருப்பம் A தவறானது; 8வது அட்டவணை மூல அரசியலமைப்பிலேயே இருந்தது.",
        "Option B is correct because the 9th Schedule was added by the 1st Amendment Act, 1951.", "விருப்பம் B சரியானது, ஏனெனில் 9வது அட்டவணை 1வது திருத்தச் சட்டம் 1951 ஆல் சேர்க்கப்பட்டது.",
        "Option C is incorrect; 10th Schedule was added by 52nd Amendment Act, 1985 (Anti-Defection Law).", "விருப்பம் C தவறானது; 10வது அட்டவணை 52வது திருத்தத்தால் 1985 இல் சேர்க்கப்பட்டது.",
        "Option D is incorrect; 11th Schedule was added by 73rd Amendment Act, 1992 (Panchayati Raj).", "விருப்பம் D தவறானது; 11வது அட்டவணை 73வது திருத்தத்தால் 1992 இல் சேர்க்கப்பட்டது.",
        "The 1st Amendment Act, 1951 also inserted Article 31A and Article 31B alongside the 9th Schedule.",
        "1வது திருத்தச் சட்டம் 1951, 9வது அட்டவணையுடன் சேர்த்து சரத்து 31A மற்றும் 31B ஐயும் அறிமுகப்படுத்தியது.",
        "Prime Minister Jawaharlal Nehru introduced the 1st Amendment Bill in the Provisional Parliament.",
        "பிரதமர் ஜவஹர்லால் நேரு தற்காலிக நாடாளுமன்றத்தில் 1வது திருத்த மசோதாவை அறிமுகப்படுத்தினார்.",
        "Remembering", "High", ["1st Amendment", "9th Schedule"], "Part 2"
    )

    # Q007 - Correct: C
    add_q(
        "CZ_AM_EZ_007",
        "Which Constitutional Amendment Act abolished the classification of States into Part A, B, C, and D states and reorganised India into 14 States and 6 Union Territories?",
        "மாநிலங்களை பகுதி A, B, C, D எனப் பிரித்த வகைப்பாட்டை நீக்கி, இந்தியாவை 14 மாநிலங்கள் மற்றும் 6 யூனியன் பிரதேசங்களாக மறுசீரமைத்த அரசியலமைப்பு திருத்தச் சட்டம் எது?",
        "1st Constitutional Amendment Act, 1951", "1வது அரசியலமைப்பு திருத்தச் சட்டம், 1951",
        "5th Constitutional Amendment Act, 1955", "5வது அரசியலமைப்பு திருத்தச் சட்டம், 1955",
        "7th Constitutional Amendment Act, 1956", "7வது அரசியலமைப்பு திருத்தச் சட்டம், 1956",
        "10th Constitutional Amendment Act, 1961", "10வது அரசியலமைப்பு திருத்தச் சட்டம், 1961",
        "C",
        "The 7th Constitutional Amendment Act, 1956 implemented the State Reorganisation Act, replacing Part A, B, C, D states with 14 States and 6 UTs.",
        "7வது அரசியலமைப்பு திருத்தச் சட்டம், 1956 மாநில மறுசீரமைப்புச் சட்டத்தைச் செயல்படுத்தி, பகுதி A, B, C, D மாநில வகைப்பாட்டை நீக்கி 14 மாநிலங்கள் மற்றும் 6 யூனியன் பிரதேசங்களை உருவாக்கியது.",
        "Option A is incorrect; 1st Amendment dealt with land reforms and speech restrictions.", "விருப்பம் A தவறானது; 1வது திருத்தம் நிலச் சீர்திருத்தம் பற்றியது.",
        "Option B is incorrect; 5th Amendment dealt with state legislature consultation time limit.", "விருப்பம் B தவறானது; 5வது திருத்தம் மாநில சட்டமன்ற கருத்து கேட்பு பற்றியது.",
        "Option C is correct because the 7th Amendment Act, 1956 reorganised Indian states on linguistic lines.", "விருப்பம் C சரியானது, ஏனெனில் 7வது திருத்தச் சட்டம் 1956 மாநிலங்களை மொழியியல் அடிப்படையில் மறுசீரமைத்தது.",
        "Option D is incorrect; 10th Amendment incorporated Dadra and Nagar Haveli into India.", "விருப்பம் D தவறானது; 10வது திருத்தம் தாத்ரா நாகர் ஹவேலியை இணைத்தது.",
        "7th Amendment Act, 1956 also provided for establishing a common High Court for two or more states.",
        "7வது திருத்தச் சட்டம் 1956 இரண்டு அல்லது அதற்கு மேற்பட்ட மாநிலங்களுக்கு பொதுவான உயர் நீதிமன்றத்தை அமைக்கவும் வழிவகை செய்தது.",
        "Fazl Ali Commission recommendations led to the 7th Amendment Act, 1956.",
        "பஸல் அலி ஆணையப் பரிந்துரைகள் 7வது திருத்தச் சட்டம் 1956 உருவாகக் காரணமாயின.",
        "Remembering", "High", ["7th Amendment", "States Reorganisation"], "Part 2"
    )

    # Q008 - Correct: D
    add_q(
        "CZ_AM_EZ_008",
        "Which Constitutional Amendment Act is popularly known as the 'Mini-Constitution' of India due to its extensive changes?",
        "அதன் பரவலான திருத்தங்கள் காரணமாக இந்தியாவின் 'சிறிய அரசியலமைப்பு' (Mini-Constitution) என்று அழைக்கப்படும் அரசியலமைப்பு திருத்தச் சட்டம் எது?",
        "24th Constitutional Amendment Act, 1971", "24வது அரசியலமைப்பு திருத்தச் சட்டம், 1971",
        "36th Constitutional Amendment Act, 1975", "36வது அரசியலமைப்பு திருத்தச் சட்டம், 1975",
        "44th Constitutional Amendment Act, 1978", "44வது அரசியலமைப்பு திருத்தச் சட்டம், 1978",
        "42nd Constitutional Amendment Act, 1976", "42வது அரசியலமைப்பு திருத்தச் சட்டம், 1976",
        "D",
        "The 42nd Constitutional Amendment Act, 1976 enacted during Emergency introduced sweeping changes and is called the Mini-Constitution.",
        "நெருக்கடி நிலையின் போது இயற்றப்பட்ட 42வது அரசியலமைப்பு திருத்தச் சட்டம், 1976 மிகப்பரவலான மாற்றங்களைக் கொண்டு வந்ததால் 'சிறிய அரசியலமைப்பு' என்றழைக்கப்படுகிறது.",
        "Option A is incorrect; 24th Amendment dealt with amending power under Article 368.", "விருப்பம் A தவறானது; 24வது திருத்தம் சரத்து 368 இன் திருத்த அதிகாரம் பற்றியது.",
        "Option B is incorrect; 36th Amendment made Sikkim a full state of India.", "விருப்பம் B தவறானது; 36வது திருத்தம் சிக்கிமை முழு மாநிலமாக்கியது.",
        "Option C is incorrect; 44th Amendment reversed several excesses of 42nd Amendment.", "விருப்பம் C தவறானது; 44வது திருத்தம் 42வது திருத்தத்தின் பல விதியை ரத்து செய்தது.",
        "Option D is correct because 42nd Amendment Act, 1976 effected massive overhaul of Preamble, Part III, Part IV, and Parliament powers.", "விருப்பம் D சரியானது, ஏனெனில் 42வது திருத்தச் சட்டம் 1976 முகப்புரை, பகுதி III, பகுதி IV ஆகியவற்றில் பெரும் மாற்றங்களை ஏற்படுத்தியது.",
        "42nd Amendment was enacted based on the recommendations of the Swaran Singh Committee.",
        "42வது திருத்தம் ஸ்வரண் சிங் குழுவின் பரிந்துரைகளின் அடிப்படையில் இயற்றப்பட்டது.",
        "It added Fundamental Duties (Part IV-A) and words 'Socialist, Secular, Integrity' to the Preamble.",
        "இது அடிப்படை கடமைகளையும் (பகுதி IV-A) முகப்புரையில் 'சமதர்ம, மதச்சார்பற்ற, ஒருமைப்பாடு' என்ற சொற்களையும் சேர்த்தது.",
        "Remembering", "High", ["42nd Amendment", "Mini-Constitution"], "Part 2"
    )

    # Q009 - Correct: A
    add_q(
        "CZ_AM_EZ_009",
        "The words 'Socialist', 'Secular' and 'Integrity' were added to the Preamble of the Indian Constitution by which amendment?",
        "இந்திய அரசியலமைப்பின் முகப்புரையில் 'சமதர்ம', 'மதச்சார்பற்ற' மற்றும் 'ஒருமைப்பாடு' ஆகிய சொற்கள் எந்த திருத்தத்தின் மூலம் சேர்க்கப்பட்டன?",
        "42nd Constitutional Amendment Act, 1976", "42வது அரசியலமைப்பு திருத்தச் சட்டம், 1976",
        "44th Constitutional Amendment Act, 1978", "44வது அரசியலமைப்பு திருத்தச் சட்டம், 1978",
        "52nd Constitutional Amendment Act, 1985", "52வது அரசியலமைப்பு திருத்தச் சட்டம், 1985",
        "86th Constitutional Amendment Act, 2002", "86வது அரசியலமைப்பு திருத்தச் சட்டம், 2002",
        "A",
        "The Preamble has been amended only ONCE so far, by the 42nd Constitutional Amendment Act, 1976, inserting 'Socialist', 'Secular' and 'Integrity'.",
        "முகப்புரை இதுவரை ஒரே ஒரு முறை மட்டுமே திருத்தப்பட்டுள்ளது. அது 42வது அரசியலமைப்பு திருத்தச் சட்டம் 1976 இன் மூலம் 'சமதர்ம', 'மதச்சார்பற்ற', 'ஒருமைப்பாடு' ஆகிய சொற்களைச் சேர்த்தது.",
        "Option A is correct as it is the only amendment to the Preamble till date.", "விருப்பம் A சரியானது, ஏனெனில் இதுவரை முகப்புரைக்கு செய்யப்பட்ட ஒரே திருத்தம் இதுவே.",
        "Option B is incorrect; 44th Amendment removed Right to Property from Fundamental Rights.", "விருப்பம் B தவறானது; 44வது திருத்தம் சொத்துரிமையை அடிப்படை உரிமையிலிருந்து நீக்கியது.",
        "Option C is incorrect; 52nd Amendment introduced the Anti-Defection Law.", "விருப்பம் C தவறானது; 52வது திருத்தம் கட்சித் தாவல் தடைச் சட்டத்தைக் கொண்டுவந்தது.",
        "Option D is incorrect; 86th Amendment added Right to Education (Article 21A).", "விருப்பம் D தவறானது; 86வது திருத்தம் கல்வி உரிமையை (சரத்து 21A) சேர்த்தது.",
        "The Preamble has been amended ONLY ONCE in the history of Indian Constitutional Law.",
        "இந்திய அரசியலமைப்பு வரலாற்றில் முகப்புரை ஒரே ஒரு முறை மட்டுமே திருத்தப்பட்டுள்ளது.",
        "Kesavananda Bharati case (1973) held that Preamble is a part of Constitution and can be amended under Article 368 without altering basic structure.",
        "கேசவாநந்த பாரதி வழக்கில் முகப்புரை அரசியலமைப்பின் ஒரு பகுதி என்றும் அடிப்படை அமைப்பை மாற்றாமல் திருத்தலாம் என்றும் கூறப்பட்டது.",
        "Remembering", "High", ["Preamble", "42nd Amendment"], "Part 2"
    )

    # Q010 - Correct: B
    add_q(
        "CZ_AM_EZ_010",
        "By which Constitutional Amendment Act was the Right to Property removed from the list of Fundamental Rights and made a legal right under Article 300A?",
        "சொத்துரிமை அடிப்படை உரிமைகள் பட்டியலிலிருந்து நீக்கப்பட்டு, சரத்து 300A இன் கீழ் சட்ட உரிமையாக மாற்றப்பட்ட அரசியலமைப்பு திருத்தச் சட்டம் எது?",
        "42nd Constitutional Amendment Act, 1976", "42வது அரசியலமைப்பு திருத்தச் சட்டம், 1976",
        "44th Constitutional Amendment Act, 1978", "44வது அரசியலமைப்பு திருத்தச் சட்டம், 1978",
        "46th Constitutional Amendment Act, 1982", "46வது அரசியலமைப்பு திருத்தச் சட்டம், 1982",
        "50th Constitutional Amendment Act, 1984", "50வது அரசியலமைப்பு திருத்தச் சட்டம், 1984",
        "B",
        "The 44th Constitutional Amendment Act, 1978 repealed Article 31 and Article 19(1)(f) from Part III and made Right to Property a legal right under Article 300A in Part XII.",
        "44வது அரசியலமைப்பு திருத்தச் சட்டம், 1978 சரத்து 31 மற்றும் 19(1)(f) ஐப் பகுதி III இலிருந்து நீக்கி, பகுதி XII இல் சரத்து 300A இன் கீழ் சொத்துரிமையைச் சட்ட உரிமையாக்கியது.",
        "Option A is incorrect; 42nd Amendment did not delete Right to Property, though it restricted it.", "விருப்பம் A தவறானது; 42வது திருத்தம் சொத்துரிமையை நீக்கவில்லை.",
        "Option B is correct because 44th Amendment Act, 1978 under Morarji Desai Janata Government deleted Right to Property as a Fundamental Right.", "விருப்பம் B சரியானது, ஏனெனில் மொரார்ஜி தேசாய் தலைமையிலான ஜனதா அரசு 44வது திருத்தம் மூலம் சொத்துரிமையை நீக்கியது.",
        "Option C is incorrect; 46th Amendment dealt with sales tax and consignment sales.", "விருப்பம் C தவறானது; 46வது திருத்தம் விற்பனை வரி தொடர்பான திருத்தம்.",
        "Option D is incorrect; 50th Amendment dealt with intelligence forces fundamental rights restrictions.", "விருப்பம் D தவறானது; 50வது திருத்தம் உளவுத்துறை படையினரின் அடிப்படை உரிமைக் கட்டுப்பாடு பற்றியது.",
        "Right to Property is currently a Legal Right / Constitutional Right under Article 300A, NOT a Fundamental Right.",
        "சொத்துரிமை தற்போது சரத்து 300A இன் கீழ் சட்ட உரிமை / அரசியலமைப்பு உரிமை மட்டுமே, அடிப்படை உரிமை அல்ல.",
        "This amendment was enacted by the Janata Party government in 1978.",
        "இந்த திருத்தம் 1978 இல் ஜனதா கட்சி அரசாங்கத்தால் இயற்றப்பட்டது.",
        "Remembering", "High", ["44th Amendment", "Right to Property", "Article 300A"], "Part 2"
    )

    # Q011 - Correct: C
    add_q(
        "CZ_AM_EZ_011",
        "Anti-Defection Law was incorporated into the Indian Constitution through the 10th Schedule by which amendment?",
        "10வது அட்டவணையின் மூலம் இந்திய அரசியலமைப்பில் கட்சித் தாவல் தடைச் சட்டம் சேர்க்கப்பட்ட அரசியலமைப்பு திருத்தம் எது?",
        "42nd Constitutional Amendment Act, 1976", "42வது அரசியலமைப்பு திருத்தச் சட்டம், 1976",
        "44th Constitutional Amendment Act, 1978", "44வது அரசியலமைப்பு திருத்தச் சட்டம், 1978",
        "52nd Constitutional Amendment Act, 1985", "52வது அரசியலமைப்பு திருத்தச் சட்டம், 1985",
        "61st Constitutional Amendment Act, 1988", "61வது அரசியலமைப்பு திருத்தச் சட்டம், 1988",
        "C",
        "The 52nd Constitutional Amendment Act, 1985 added the 10th Schedule to disqualify members of Parliament and State Assemblies on grounds of defection.",
        "52வது அரசியலமைப்பு திருத்தச் சட்டம், 1985 கட்சித் தாவல் அடிப்படையில் நாடாளுமன்ற மற்றும் சட்டமன்ற உறுப்பினர்களைத் தகுதிநீக்கம் செய்ய 10வது அட்டவணையைச் சேர்த்தது.",
        "Option A is incorrect; 42nd Amendment did not deal with anti-defection.", "விருப்பம் A தவறானது; 42வது திருத்தம் கட்சித் தாவல் பற்றியது அல்ல.",
        "Option B is incorrect; 44th Amendment dealt with post-emergency restorations.", "விருப்பம் B தவறானது; 44வது திருத்தம் அவசரநிலைக்குப் பிந்தைய சீரமைப்பு பற்றியது.",
        "Option C is correct because 52nd Amendment Act, 1985 added 10th Schedule during Rajiv Gandhi premiership.", "விருப்பம் C சரியானது, ஏனெனில் ராஜீவ் காந்தி ஆட்சிக் காலத்தில் 52வது திருத்தம் 10வது அட்டவணையைச் சேர்த்தது.",
        "Option D is incorrect; 61st Amendment lowered voting age to 18 years.", "விருப்பம் D தவறானது; 61வது திருத்தம் வாக்குரிமை வயதை 18 ஆகக் குறைத்தது.",
        "The 91st Amendment Act, 2003 later strengthened the Anti-Defection Law by omitting the 'split' exception.",
        "பின்னர் 91வது திருத்தச் சட்டம் 2003 'பிளவு' விதிவிலக்கை நீக்கி கட்சித் தாவல் சட்டத்தை மேலும் வலுப்படுத்தியது.",
        "Disqualification under 10th Schedule is decided by the Presiding Officer of the respective House.",
        "10வது அட்டவணையின் கீழ் தகுதிநீக்கம் குறித்து சம்பந்தப்பட்ட அவையின் தலைவரால் தீர்மானிக்கப்படுகிறது.",
        "Remembering", "High", ["52nd Amendment", "10th Schedule", "Anti-Defection"], "Part 2"
    )

    # Q012 - Correct: D
    add_q(
        "CZ_AM_EZ_012",
        "Which Constitutional Amendment Act reduced the voting age for Lok Sabha and State Legislative Assembly elections from 21 years to 18 years?",
        "மக்களவை மற்றும் மாநில சட்டமன்றத் தேர்தல்களில் வாக்குரிமை வயதை 21 லிருந்து 18 ஆகக் குறைத்த அரசியலமைப்பு திருத்தச் சட்டம் எது?",
        "42nd Amendment Act, 1976", "42வது திருத்தச் சட்டம், 1976",
        "52nd Amendment Act, 1985", "52வது திருத்தச் சட்டம், 1985",
        "59th Amendment Act, 1988", "59வது திருத்தச் சட்டம், 1988",
        "61st Amendment Act, 1988", "61வது திருத்தச் சட்டம், 1988",
        "D",
        "The 61st Constitutional Amendment Act, 1988 (effective from March 1989) amended Article 326 to reduce the voting age from 21 to 18 years.",
        "61வது அரசியலமைப்பு திருத்தச் சட்டம், 1988 (1989 மார்ச் முதல் நடைமுறை) சரத்து 326 ஐத் திருத்தி வாக்களிக்கும் வயதை 21 லிருந்து 18 ஆகக் குறைத்தது.",
        "Option A is incorrect; 42nd Amendment extended Assembly terms to 6 years.", "விருப்பம் A தவறானது; 42வது திருத்தம் சட்டமன்ற பதவிக் காலத்தை 6 ஆண்டுகளாக உயர்த்தியது.",
        "Option B is incorrect; 52nd Amendment was Anti-Defection Law.", "விருப்பம் B தவறானது; 52வது திருத்தம் கட்சித் தாவல் தடைச் சட்டம்.",
        "Option C is incorrect; 59th Amendment related to emergency in Punjab.", "விருப்பம் C தவறானது; 59வது திருத்தம் பஞ்சாப் அவசரநிலை பற்றியது.",
        "Option D is correct because 61st Amendment Act, 1988 amended Article 326 to grant voting rights at 18 years.", "விருப்பம் D சரியானது, ஏனெனில் 61வது திருத்தச் சட்டம் 1988 சரத்து 326 ஐத் திருத்தி 18 வயதில் வாக்குரிமை அளித்தது.",
        "Article 326 deals with Elections to the House of the People and Legislative Assemblies of States on the basis of Adult Suffrage.",
        "சரத்து 326 வயதுவந்தோர் வாக்குரிமையின் அடிப்படையில் மக்களவை மற்றும் மாநில சட்டமன்றங்களுக்கான தேர்தல்களைக் கையாள்கிறது.",
        "It came into force on March 28, 1989 during the Rajiv Gandhi government.",
        "இது 1989 மார்ச் 28 இல் ராஜீவ் காந்தி அரசின் போது அமலுக்கு வந்தது.",
        "Remembering", "High", ["61st Amendment", "Voting Age", "Article 326"], "Part 2"
    )

    # Q013 - Correct: A
    add_q(
        "CZ_AM_EZ_013",
        "Constitutional status and protection were granted to Panchayati Raj Institutions by which amendment act?",
        "பஞ்சாயத்து ராஜ் நிறுவனங்களுக்கு அரசியலமைப்பு அந்தஸ்தும் பாதுகாப்பும் எந்த திருத்தச் சட்டத்தின் மூலம் வழங்கப்பட்டது?",
        "73rd Constitutional Amendment Act, 1992", "73வது அரசியலமைப்பு திருத்தச் சட்டம், 1992",
        "74th Constitutional Amendment Act, 1992", "74வது அரசியலமைப்பு திருத்தச் சட்டம், 1992",
        "65th Constitutional Amendment Act, 1990", "65வது அரசியலமைப்பு திருத்தச் சட்டம், 1990",
        "70th Constitutional Amendment Act, 1992", "70வது அரசியலமைப்பு திருத்தச் சட்டம், 1992",
        "A",
        "The 73rd Constitutional Amendment Act, 1992 added Part IX and the 11th Schedule to grant constitutional status to Panchayati Raj Institutions.",
        "73வது அரசியலமைப்பு திருத்தச் சட்டம், 1992 பகுதி IX மற்றும் 11வது அட்டவணையைச் சேர்த்து பஞ்சாயத்து ராஜ் நிறுவனங்களுக்கு அரசியலமைப்பு அந்தஸ்து வழங்கியது.",
        "Option A is correct because 73rd Amendment introduced 29 functional items for Panchayats in 11th Schedule.", "விருப்பம் A சரியானது, ஏனெனில் 73வது திருத்தம் 11வது அட்டவணையில் பஞ்சாயத்துகளுக்கு 29 அதிகாரப் புள்ளிகளை வழங்கியது.",
        "Option B is incorrect; 74th Amendment provided constitutional status to Municipalities (Part IX-A).", "விருப்பம் B தவறானது; 74வது திருத்தம் நகராட்சிகளுக்கு அரசியலமைப்பு அந்தஸ்து வழங்கியது.",
        "Option C is incorrect; 65th Amendment established National Commission for SCs & STs.", "விருப்பம் C தவறானது; 65வது திருத்தம் ஆதிதிராவிடர் மற்றும் பழங்குடியினர் தேசிய ஆணையத்தை அமைத்தது.",
        "Option D is incorrect; 70th Amendment included Delhi and Puducherry Assemblies in Presidential electoral college.", "விருப்பம் D தவறானது; 70வது திருத்தம் டெல்லி மற்றும் புதுச்சேரி சட்டமன்றங்களை குடியரசு தலைவர் தேர்தல் மன்றத்தில் சேர்த்தது.",
        "73rd Amendment came into force on 24th April 1993, which is celebrated annually as National Panchayati Raj Day.",
        "73வது திருத்தம் 1993 ஏப்ரல் 24 முதல் அமலுக்கு வந்தது, இந்நாள் தேசிய பஞ்சாயத்து ராஜ் தினமாகக் கொண்டாடப்படுகிறது.",
        "The 11th Schedule contains 29 functional items for Panchayats.",
        "11வது அட்டவணை பஞ்சாயத்துகளுக்கான 29 செயல் செயல்பாடுகளைக் கொண்டுள்ளது.",
        "Remembering", "High", ["73rd Amendment", "Panchayati Raj", "11th Schedule"], "Part 2"
    )

    # Q014 - Correct: B
    add_q(
        "CZ_AM_EZ_014",
        "Which Constitutional Amendment Act added Part IX-A and the 12th Schedule to give constitutional status to Urban Local Bodies (Municipalities)?",
        "நகர்ப்புற உள்ளாட்சி அமைப்புகளுக்கு (நகராட்சிகள்) அரசியலமைப்பு அந்தஸ்து வழங்க பகுதி IX-A மற்றும் 12வது அட்டவணையைச் சேர்த்த அரசியலமைப்பு திருத்தச் சட்டம் எது?",
        "73rd Constitutional Amendment Act, 1992", "73வது அரசியலமைப்பு திருத்தச் சட்டம், 1992",
        "74th Constitutional Amendment Act, 1992", "74வது அரசியலமைப்பு திருத்தச் சட்டம், 1992",
        "77th Constitutional Amendment Act, 1995", "77வது அரசியலமைப்பு திருத்தச் சட்டம், 1995",
        "80th Constitutional Amendment Act, 2000", "80வது அரசியலமைப்பு திருத்தச் சட்டம், 2000",
        "B",
        "The 74th Constitutional Amendment Act, 1992 added Part IX-A (Articles 243P to 243ZG) and 12th Schedule containing 18 functional items for Municipalities.",
        "74வது அரசியலமைப்பு திருத்தச் சட்டம், 1992 பகுதி IX-A மற்றும் நகராட்சிகளுக்கான 18 செயல்பாடுகளைக் கொண்ட 12வது அட்டவணையைச் சேர்த்தது.",
        "Option A is incorrect; 73rd Amendment applied to Rural Panchayats.", "விருப்பம் A தவறானது; 73வது திருத்தம் கிராமப் பஞ்சாயத்துகளுக்குப் பொருந்தும்.",
        "Option B is correct because 74th Amendment Act, 1992 constitutionalised Municipalities.", "விருப்பம் B சரியானது, ஏனெனில் 74வது திருத்தச் சட்டம் 1992 நகராட்சிகளுக்கு அரசியலமைப்பு அந்தஸ்தளித்தது.",
        "Option C is incorrect; 77th Amendment provided reservation in promotion for SC/STs.", "விருப்பம் C தவறானது; 77வது திருத்தம் எஸ்சி/எஸ்டி பிரிவினருக்குப் பதவி உயர்வில் இடஒதுக்கீடு பற்றியது.",
        "Option D is incorrect; 80th Amendment introduced alternative scheme of tax sharing.", "விருப்பம் D தவறானது; 80வது திருத்தம் மாற்று வரிப் பகிர்வுத் திட்டம் பற்றியது.",
        "The 12th Schedule contains 18 functional matters for Municipalities.",
        "12வது அட்டவணையில் நகராட்சிகளுக்கான 18 செயலாக்கப் பொருட்கள் உள்ளன.",
        "74th Amendment Act came into effect on June 1, 1993.",
        "74வது திருத்தச் சட்டம் 1993 ஜூன் 1 முதல் நடைமுறைக்கு வந்தது.",
        "Remembering", "High", ["74th Amendment", "Municipalities", "12th Schedule"], "Part 2"
    )

    # Q015 - Correct: C
    add_q(
        "CZ_AM_EZ_015",
        "Right to Education was made a Fundamental Right under Article 21A by which Constitutional Amendment Act?",
        "சரத்து 21A இன் கீழ் கல்வி உரிமை எந்த அரசியலமைப்பு திருத்தச் சட்டத்தின் மூலம் அடிப்படை உரிமையாக்கப்பட்டது?",
        "44th Constitutional Amendment Act, 1978", "44வது அரசியலமைப்பு திருத்தச் சட்டம், 1978",
        "73rd Constitutional Amendment Act, 1992", "73வது அரசியலமைப்பு திருத்தச் சட்டம், 1992",
        "86th Constitutional Amendment Act, 2002", "86வது அரசியலமைப்பு திருத்தச் சட்டம், 2002",
        "91st Constitutional Amendment Act, 2003", "91வது அரசியலமைப்பு திருத்தச் சட்டம், 2003",
        "C",
        "The 86th Constitutional Amendment Act, 2002 inserted Article 21A making free and compulsory education for children aged 6 to 14 years a Fundamental Right.",
        "86வது அரசியலமைப்பு திருத்தச் சட்டம், 2002 சரத்து 21A ஐச் சேர்த்து 6 முதல் 14 வயதுடைய குழந்தைகளுக்கு இலவச மற்றும் கட்டாயக் கல்வியை அடிப்படை உரிமையாக்கியது.",
        "Option A is incorrect; 44th Amendment restored civil liberties.", "விருப்பம் A தவறானது; 44வது திருத்தம் குடிமை உரிமைகளை சீரமைத்தது.",
        "Option B is incorrect; 73rd Amendment related to Panchayati Raj.", "விருப்பம் B தவறானது; 73வது திருத்தம் பஞ்சாயத்து ராஜ் பற்றியது.",
        "Option C is correct because 86th Amendment Act, 2002 added Article 21A, modified Article 45, and added Fundamental Duty 51A(k).", "விருப்பம் C சரியானது, ஏனெனில் 86வது திருத்தச் சட்டம் 2002 சரத்து 21A, சரத்து 45 திருத்தம் மற்றும் 51A(k) கடமையைச் சேர்த்தது.",
        "Option D is incorrect; 91st Amendment capped Council of Ministers size at 15%.", "விருப்பம் D தவறானது; 91வது திருத்தம் அமைச்சரவை அளவை 15% எனக் கட்டுப்படுத்தியது.",
        "86th Amendment Act, 2002 made changes in Part III (Art 21A), Part IV (Art 45), and Part IV-A (Art 51A(k)).",
        "86வது திருத்தச் சட்டம் 2002 பகுதி III, பகுதி IV மற்றும் பகுதி IV-A ஆகிய மூன்றிலும் மாற்றங்களை செய்தது.",
        "RTE Act 2009 was subsequently enacted to operationalise Article 21A from April 1, 2010.",
        "சரத்து 21A ஐ 2010 ஏப்ரல் 1 முதல் அமல்படுத்த இலவச கட்டாயக் கல்விச் சட்டம் 2009 இயற்றப்பட்டது.",
        "Remembering", "High", ["86th Amendment", "Article 21A", "Right to Education"], "Part 2"
    )

    # Q016 - Correct: D
    add_q(
        "CZ_AM_EZ_016",
        "Which Constitutional Amendment Act restricted the size of the Council of Ministers to 15% of the total strength of the Lok Sabha / Legislative Assembly?",
        "அமைச்சரவையின் அளவை மக்களவை / சட்டமன்றத்தின் மொத்த உறுப்பினர்களின் எண்ணிக்கையில் 15% ஆகக் கட்டுப்படுத்திய அரசியலமைப்பு திருத்தச் சட்டம் எது?",
        "42nd Amendment Act, 1976", "42வது திருத்தச் சட்டம், 1976",
        "84th Amendment Act, 2001", "84வது திருத்தச் சட்டம், 2001",
        "86th Amendment Act, 2002", "86வது திருத்தச் சட்டம், 2002",
        "91st Amendment Act, 2003", "91வது திருத்தச் சட்டம், 2003",
        "D",
        "The 91st Constitutional Amendment Act, 2003 mandated that the total number of Ministers, including PM/CM, shall not exceed 15% of total Lok Sabha/Assembly strength.",
        "91வது அரசியலமைப்பு திருத்தச் சட்டம், 2003 பிரதமர்/முதல்வர் உட்பட மொத்த அமைச்சர்களின் எண்ணிக்கை மக்களவை/சட்டமன்ற மொத்த உறுப்பினர்களில் 15% க்கு மிகாமல் இருக்க வேண்டும் எனக் கட்டுப்படுத்தியது.",
        "Option A is incorrect; 42nd Amendment made cabinet advice binding.", "விருப்பம் A தவறானது; 42வது திருத்தம் அமைச்சரவை ஆலோசனையைக் கட்டாயமாக்கியது.",
        "Option B is incorrect; 84th Amendment froze constituency delimitation till 2026.", "விருப்பம் B தவறானது; 84வது திருத்தம் தொகுதி மறுவரையறையை 2026 வரை முடக்கியது.",
        "Option C is incorrect; 86th Amendment related to Right to Education.", "விருப்பம் C தவறானது; 86வது திருத்தம் கல்வி உரிமை பற்றியது.",
        "Option D is correct because 91st Amendment Act, 2003 inserted Articles 75(1A) and 164(1A) establishing the 15% ceiling.", "விருப்பம் D சரியானது, ஏனெனில் 91வது திருத்தச் சட்டம் 2003 சரத்து 75(1A) மற்றும் 164(1A) ஐச் சேர்த்து 15% உச்சவரம்பை நிர்ணயித்தது.",
        "For smaller States, the minimum number of Ministers in the Council of Ministers shall not be less than 12 under Article 164(1A).",
        "சிறிய மாநிலங்களுக்கு அமைச்சரவையில் குறைந்தபட்ச அமைச்சர்களின் எண்ணிக்கை 12 ஆக இருக்க வேண்டும் (சரத்து 164(1A)).",
        "91st Amendment also omitted the provision about 1/3 split in 10th Schedule.",
        "91வது திருத்தம் 10வது அட்டவணையில் 1/3 பிளவு தொடர்பான விதிவிலக்கையும் நீக்கியது.",
        "Remembering", "High", ["91st Amendment", "Council of Ministers", "15% Cap"], "Part 2"
    )

    # Q017 - Correct: A
    add_q(
        "CZ_AM_EZ_017",
        "Goods and Services Tax (GST) was introduced in India by which Constitutional Amendment Act?",
        "சரக்கு மற்றும் சேவை வரி (GST) இந்தியாவில் எந்த அரசியலமைப்பு திருத்தச் சட்டத்தின் மூலம் அறிமுகப்படுத்தப்பட்டது?",
        "101st Constitutional Amendment Act, 2016", "101வது அரசியலமைப்பு திருத்தச் சட்டம், 2016",
        "100th Constitutional Amendment Act, 2015", "100வது அரசியலமைப்பு திருத்தச் சட்டம், 2015",
        "102nd Constitutional Amendment Act, 2018", "102வது அரசியலமைப்பு திருத்தச் சட்டம், 2018",
        "103rd Constitutional Amendment Act, 2019", "103வது அரசியலமைப்பு திருத்தச் சட்டம், 2019",
        "A",
        "The 101st Constitutional Amendment Act, 2016 introduced GST in India and inserted Articles 246A, 269A, and 279A (GST Council).",
        "101வது அரசியலமைப்பு திருத்தச் சட்டம், 2016 இந்தியாவில் ஜிஎஸ்டியை அறிமுகப்படுத்தி சரத்துகள் 246A, 269A மற்றும் 279A (ஜிஎஸ்டி கவுன்சில்) ஆகியவற்றைச் சேர்த்தது.",
        "Option A is correct because 101st Amendment Act, 2016 enabled nationwide indirect tax reform effective July 1, 2017.", "விருப்பம் A சரியானது, ஏனெனில் 101வது திருத்தச் சட்டம் 2016 ஜூலை 1, 2017 முதல் நாடு தழுவிய மறைமுக வரிச் சீர்திருத்தத்தை அமல்படுத்தியது.",
        "Option B is incorrect; 100th Amendment related to Land Boundary Agreement with Bangladesh.", "விருப்பம் B தவறானது; 100வது திருத்தம் வங்காளதேசத்துடனான எல்லை ஒப்பந்தம் பற்றியது.",
        "Option C is incorrect; 102nd Amendment gave constitutional status to National Commission for Backward Classes (NCBC).", "விருப்பம் C தவறானது; 102வது திருத்தம் பிற்படுத்தப்பட்டோர் தேசிய ஆணையத்திற்கு அரசியலமைப்பு அந்தஸ்தளித்தது.",
        "Option D is incorrect; 103rd Amendment introduced 10% EWS reservation.", "விருப்பம் D தவறானது; 103வது திருத்தம் 10% EWS இடஒதுக்கீட்டை அறிமுகப்படுத்தியது.",
        "101st Amendment created the GST Council chaired by the Union Finance Minister under Article 279A.",
        "101வது திருத்தம் சரத்து 279A இன் கீழ் மத்திய நிதி அமைச்சர் தலைமையில் ஜிஎஸ்டி கவுன்சிலை உருவாக்கியது.",
        "GST came into force on July 1, 2017.",
        "ஜிஎஸ்டி 2017 ஜூலை 1 முதல் அமலுக்கு வந்தது.",
        "Remembering", "High", ["101st Amendment", "GST", "Article 279A"], "Part 2"
    )

    # Q018 - Correct: B
    add_q(
        "CZ_AM_EZ_018",
        "10% Reservation for Economically Weaker Sections (EWS) in education and government jobs was introduced by which amendment?",
        "பொருளாதாரத்தில் பின்தங்கிய பிரிவினருக்கு (EWS) கல்வி மற்றும் அரசுப் பணிகளில் 10% இடஒதுக்கீடு எந்த திருத்தத்தின் மூலம் அறிமுகப்படுத்தப்பட்டது?",
        "101st Amendment Act, 2016", "101வது திருத்தச் சட்டம், 2016",
        "103rd Amendment Act, 2019", "103வது திருத்தச் சட்டம், 2019",
        "104th Amendment Act, 2020", "104வது திருத்தச் சட்டம், 2020",
        "105th Amendment Act, 2021", "105வது திருத்தச் சட்டம், 2021",
        "B",
        "The 103rd Constitutional Amendment Act, 2019 inserted Article 15(6) and Article 16(6) to provide up to 10% reservation for Economically Weaker Sections (EWS).",
        "103வது அரசியலமைப்பு திருத்தச் சட்டம், 2019 சரத்து 15(6) மற்றும் 16(6) ஐச் சேர்த்து பொருளாதாரத்தில் பின்தங்கிய பிரிவினருக்கு (EWS) 10% வரை இடஒதுக்கீடு வழங்கியது.",
        "Option A is incorrect; 101st Amendment introduced GST.", "விருப்பம் A தவறானது; 101வது திருத்தம் ஜிஎஸ்டி பற்றியது.",
        "Option B is correct because 103rd Amendment Act, 2019 provided 10% EWS quota for non-reserved categories.", "விருப்பம் B சரியானது, ஏனெனில் 103வது திருத்தச் சட்டம் 2019 இடஒதுக்கீடு பெறாத பொதுப் பிரிவினருக்கு 10% EWS இடஒதுக்கீடு வழங்கியது.",
        "Option C is incorrect; 104th Amendment extended SC/ST reservations and abolished Anglo-Indian nomination.", "விருப்பம் C தவறானது; 104வது திருத்தம் எஸ்சி/எஸ்டி இடஒதுக்கீடு நீட்டிப்பு மற்றும் ஆங்கிலோ-இந்திய நியமன நீக்கம் பற்றியது.",
        "Option D is incorrect; 105th Amendment restored state power to identify SEBCs.", "விருப்பம் D தவறானது; 105வது திருத்தம் மாநிலங்கள் பிற்படுத்தப்பட்ட வகுப்பினரை அடையாளம் காணும் அதிகாரத்தை மீட்டெடுத்தது.",
        "Supreme Court upheld the validity of 103rd Amendment (EWS reservation) in Janhit Abhiyan v. Union of India (2022).",
        "ஜன்ஹித் அபியான் எதிர் மத்திய அரசு (2022) வழக்கில் உச்ச நீதிமன்றம் 103வது திருத்தத்தின் செல்லுபடியாகும் தன்மையை உறுதி செய்தது.",
        "It amended Articles 15 and 16 by adding clause (6) to both.",
        "இது சரத்துகள் 15 மற்றும் 16 இரண்டிலும் உட்பிரிவு (6) ஐச் சேர்த்தது.",
        "Remembering", "High", ["103rd Amendment", "EWS Reservation", "Article 15(6)"], "Part 2"
    )

    # Q019 - Correct: C
    add_q(
        "CZ_AM_EZ_019",
        "Which Constitutional Amendment Act discontinued the nomination of Anglo-Indians to the Lok Sabha and State Legislative Assemblies?",
        "மக்களவை மற்றும் மாநில சட்டமன்றங்களுக்கு ஆங்கிலோ-இந்தியர்களின் நியமன முறையை ரத்து செய்த அரசியலமைப்பு திருத்தச் சட்டம் எது?",
        "101st Amendment Act, 2016", "101வது திருத்தச் சட்டம், 2016",
        "102nd Amendment Act, 2018", "102வது திருத்தச் சட்டம், 2018",
        "104th Amendment Act, 2020", "104வது திருத்தச் சட்டம், 2020",
        "105th Amendment Act, 2021", "105வது திருத்தச் சட்டம், 2021",
        "C",
        "The 104th Constitutional Amendment Act, 2020 extended SC/ST seat reservation in Lok Sabha and Assemblies for 10 years (till 2030) but discontinued Anglo-Indian nomination.",
        "104வது அரசியலமைப்பு திருத்தச் சட்டம், 2020 மக்களவை மற்றும் சட்டமன்றங்களில் எஸ்சி/எஸ்டி இடஒதுக்கீட்டை 10 ஆண்டுகள் நீட்டித்தது; ஆனால் ஆங்கிலோ-இந்தியர் நியமனத்தை ரத்து செய்தது.",
        "Option A is incorrect; 101st Amendment introduced GST.", "விருப்பம் A தவறானது; 101வது திருத்தம் ஜிஎஸ்டி பற்றியது.",
        "Option B is incorrect; 102nd Amendment dealt with NCBC constitutional status.", "விருப்பம் B தவறானது; 102வது திருத்தம் NCBC அரசியலமைப்பு அந்தஸ்து பற்றியது.",
        "Option C is correct because 104th Amendment Act, 2020 ended Anglo-Indian reserved nomination in Lok Sabha (Art 331) and Assemblies (Art 333).", "விருப்பம் C சரியானது, ஏனெனில் 104வது திருத்தச் சட்டம் 2020 மக்களவை மற்றும் சட்டமன்ற ஆங்கிலோ-இந்தியர் நியமனத்தை முடிவுக்குக் கொண்டு வந்தது.",
        "Option D is incorrect; 105th Amendment restored state SEBC list identification power.", "விருப்பம் D தவறானது; 105வது திருத்தம் மாநில பிற்படுத்தப்பட்டோர் பட்டியல் அதிகார மீட்சி பற்றியது.",
        "Before 104th Amendment, President could nominate 2 Anglo-Indians to Lok Sabha and Governor could nominate 1 to Assembly.",
        "104வது திருத்தத்திற்கு முன் குடியரசு தலைவர் மக்களவைக்கு 2 பேரையும், ஆளுநர் சட்டமன்றத்திற்கு 1 பேரையும் நியமிக்க முடியும்.",
        "104th Amendment came into force on January 25, 2020.",
        "104வது திருத்தம் 2020 ஜனவரி 25 முதல் அமலுக்கு வந்தது.",
        "Remembering", "High", ["104th Amendment", "Anglo-Indian Nomination", "SC ST Reservation"], "Part 2"
    )

    # Q020 - Correct: D
    add_q(
        "CZ_AM_EZ_020",
        "Which Constitutional Amendment Act is known as the 'Nari Shakti Vandan Adhiniyam' providing 33% reservation for women in Lok Sabha and State Legislative Assemblies?",
        "மக்களவை மற்றும் மாநில சட்டமன்றங்களில் பெண்களுக்கு 33% இடஒதுக்கீடு வழங்கும் 'நாரி சக்தி வந்தன் அதினியம்' என்று அழைக்கப்படும் அரசியலமைப்பு திருத்தச் சட்டம் எது?",
        "103rd Amendment Act, 2019", "103வது திருத்தச் சட்டம், 2019",
        "104th Amendment Act, 2020", "104வது திருத்தச் சட்டம், 2020",
        "105th Amendment Act, 2021", "105வது திருத்தச் சட்டம், 2021",
        "106th Amendment Act, 2023", "106வது திருத்தச் சட்டம், 2023",
        "D",
        "The 106th Constitutional Amendment Act, 2023 (Nari Shakti Vandan Adhiniyam) provides 1/3rd (33%) reservation for women in Lok Sabha, State Assemblies, and Delhi Assembly.",
        "106வது அரசியலமைப்பு திருத்தச் சட்டம், 2023 (நாரி சக்தி வந்தன் அதினியம்) மக்களவை, மாநில சட்டமன்றங்கள் மற்றும் டெல்லி சட்டமன்றத்தில் பெண்களுக்கு 33% இடஒதுக்கீடு வழங்குகிறது.",
        "Option A is incorrect; 103rd Amendment provided EWS reservation.", "விருப்பம் A தவறானது; 103வது திருத்தம் EWS இடஒதுக்கீடு பற்றியது.",
        "Option B is incorrect; 104th Amendment dealt with SC/ST reservation and Anglo-Indian seats.", "விருப்பம் B தவறானது; 104வது திருத்தம் எஸ்சி/எஸ்டி இடஒதுக்கீடு பற்றியது.",
        "Option C is incorrect; 105th Amendment restored state powers to notify SEBCs.", "விருப்பம் C தவறானது; 105வது திருத்தம் மாநில SEBC பட்டியல் அதிகாரம் பற்றியது.",
        "Option D is correct because 106th Amendment Act, 2023 inserted Articles 330A, 332A, and 239AA(2)(b) reserving 33% seats for women.", "விருப்பம் D சரியானது, ஏனெனில் 106வது திருத்தச் சட்டம் 2023 சரத்துகள் 330A, 332A, 239AA(2)(b) ஐச் சேர்த்து பெண்களுக்கு 33% இடங்களை ஒதுக்கியது.",
        "The women's reservation under 106th Amendment will come into effect after the first Census and subsequent delimitation exercise.",
        "106வது திருத்தத்தின் கீழ் பெண்களுக்கான இடஒதுக்கீடு முதல் மக்கள் தொகை கணக்கெடுப்பு மற்றும் தொகுதி மறுவரையறைக்கு பின் அமலுக்கு வரும்.",
        "The reservation period under 106th Amendment is initially fixed for 15 years from commencement.",
        "இந்த இடஒதுக்கீடு ஆரம்பத்தில் அமலுக்கு வந்த நாளிலிருந்து 15 ஆண்டுகளுக்கு அமலில் இருக்கும்.",
        "Remembering", "High", ["106th Amendment", "Nari Shakti Vandan", "Women Reservation"], "Part 2"
    )

    # Q021 - Correct: A
    add_q(
        "CZ_AM_EZ_021",
        "Which landmark Supreme Court judgment in 1973 established the famous 'Basic Structure Doctrine' of the Indian Constitution?",
        "1973 இல் வழங்கப்பட்ட எந்த வரலாற்றுச் சிறப்புமிக்க உச்ச நீதிமன்றத் தீர்ப்பு இந்திய அரசியலமைப்பின் புகழ்பெற்ற 'அடிப்படை அமைப்பு கோட்பாட்டை' (Basic Structure Doctrine) நிறுவியது?",
        "Kesavananda Bharati v. State of Kerala", "கேசவாநந்த பாரதி எதிர் கேரள அரசு",
        "Golaknath v. State of Punjab", "கோலக்நாத் எதிர் பஞ்சாப் அரசு",
        "Minerva Mills v. Union of India", "மினர்வா மில்ஸ் எதிர் மத்திய அரசு",
        "Shankari Prasad v. Union of India", "சங்கரி பிரசாத் எதிர் மத்திய அரசு",
        "A",
        "In Kesavananda Bharati v. State of Kerala (1973), a 13-judge bench ruled by 7-6 majority that Parliament can amend any part of the Constitution under Art 368, but cannot alter its Basic Structure.",
        "கேசவாநந்த பாரதி எதிர் கேரள அரசு (1973) வழக்கில் 13 நீதிபதிகள் கொண்ட அமர்வு, நாடாளுமன்றம் அரசியலமைப்பின் எந்தப் பகுதியையும் திருத்தலாம், ஆனால் அதன் அடிப்படை அமைப்பை மாற்ற முடியாது என 7-6 பெரும்பான்மையில் தீர்ப்பளித்தது.",
        "Option A is correct because Kesavananda Bharati (April 24, 1973) birthed the Basic Structure Doctrine.", "விருப்பம் A சரியானது, ஏனெனில் கேசவாநந்த பாரதி வழக்கு (1973 ஏப்ரல் 24) அடிப்படை அமைப்புக் கோட்பாட்டை உருவாக்கியது.",
        "Option B is incorrect; Golaknath (1967) ruled Parliament cannot amend Fundamental Rights at all.", "விருப்பம் B தவறானது; கோலக்நாத் வழக்கு (1967) அடிப்படை உரிமைகளைத் திருத்தவே முடியாது என்றது.",
        "Option C is incorrect; Minerva Mills (1980) applied basic structure to invalidate 42nd Amendment Art 368(4)&(5).", "விருப்பம் C தவறானது; மினர்வா மில்ஸ் (1980) அடிப்படை அமைப்பைப் பயன்படுத்தி 42வது திருத்தப் பிரிவுகளை ரத்து செய்தது.",
        "Option D is incorrect; Shankari Prasad (1951) upheld Parliament's unrestricted amending power.", "விருப்பம் D தவறானது; சங்கரி பிரசாத் (1951) நாடாளுமன்றத்தின் வரம்பற்ற திருத்த அதிகாரத்தை உறுதி செய்தது.",
        "Kesavananda Bharati bench of 13 judges remains the largest constitutional bench in the history of the Supreme Court of India.",
        "13 நீதிபதிகள் கொண்ட கேசவாநந்த பாரதி அமர்வு இந்திய உச்ச நீதிமன்ற வரலாற்றிலேயே மிகப்பெரிய அரசியலமைப்பு அமர்வாகும்.",
        "The judgment was delivered on April 24, 1973.",
        "இத்தீர்ப்பு 1973 ஏப்ரல் 24 அன்று வழங்கப்பட்டது.",
        "Remembering", "High", ["Kesavananda Bharati", "Basic Structure Doctrine"], "Part 3"
    )

    # Q022 - Correct: B
    add_q(
        "CZ_AM_EZ_022",
        "In which case did the Supreme Court hold for the first time in 1967 that Parliament CANNOT amend Fundamental Rights?",
        "நாடாளுமன்றம் அடிப்படை உரிமைகளைத் திருத்தவே முடியாது என்று உச்ச நீதிமன்றம் 1967 இல் முதன்முதலில் எந்த வழக்கில் தீர்ப்பளித்தது?",
        "Shankari Prasad Case (1951)", "சங்கரி பிரசாத் வழக்கு (1951)",
        "Golaknath Case (1967)", "கோலக்நாத் வழக்கு (1967)",
        "Sajjan Singh Case (1965)", "சஜ்ஜன் சிங் வழக்கு (1965)",
        "Maneka Gandhi Case (1978)", "மேனகா காந்தி வழக்கு (1978)",
        "B",
        "In Golaknath v. State of Punjab (1967), an 11-judge bench ruled that Fundamental Rights are sacrosanct and transcendental, and Parliament has no power to amend Part III.",
        "கோலக்நாத் எதிர் பஞ்சாப் அரசு (1967) வழக்கில் 11 நீதிபதிகள் கொண்ட அமர்வு, அடிப்படை உரிமைகள் புனிதமானவை மற்றும் மாற்ற முடியாதவை என்றும், பகுதி III ஐ திருத்த நாடாளுமன்றத்திற்கு அதிகாரம் இல்லை என்றும் தீர்ப்பளித்தது.",
        "Option A is incorrect; Shankari Prasad (1951) held Parliament CAN amend Fundamental Rights.", "விருப்பம் A தவறானது; சங்கரி பிரசாத் வழக்கு நாடாளுமன்றம் அடிப்படை உரிமைகளை திருத்தலாம் என்றது.",
        "Option B is correct because Golaknath case (1967) placed Fundamental Rights beyond Parliament's amending reach.", "விருப்பம் B சரியானது, ஏனெனில் கோலக்நாத் வழக்கு (1967) அடிப்படை உரிமைகளை நாடாளுமன்றத் திருத்த வரம்பிற்கு வெளியே வைத்தது.",
        "Option C is incorrect; Sajjan Singh (1965) supported Shankari Prasad ruling.", "விருப்பம் C தவறானது; சஜ்ஜன் சிங் வழக்கு சங்கரி பிரசாத் தீர்ப்பை ஆதரித்தது.",
        "Option D is incorrect; Maneka Gandhi (1978) expanded Article 21 due process scope.", "விருப்பம் D தவறானது; மேனகா காந்தி வழக்கு சரத்து 21 இன் நோக்கத்தை விரிவுபடுத்தியது.",
        "To override the Golaknath ruling, Parliament enacted the 24th Constitutional Amendment Act in 1971.",
        "கோலக்நாத் தீர்ப்பை ரத்து செய்ய நாடாளுமன்றம் 1971 இல் 24வது அரசியலமைப்பு திருத்தச் சட்டத்தை இயற்றியது.",
        "Golaknath case was decided by an 11-judge bench by a 6-5 majority.",
        "கோலக்நாத் வழக்கு 11 நீதிபதிகள் அமர்வில் 6-5 என்ற பெரும்பான்மையில் தீர்ப்பளிக்கப்பட்டது.",
        "Remembering", "High", ["Golaknath Case", "Fundamental Rights", "1967"], "Part 3"
    )

    # Q023 - Correct: C
    add_q(
        "CZ_AM_EZ_023",
        "Which Constitutional Amendment Act added Part IV-A (Fundamental Duties) to the Indian Constitution?",
        "இந்திய அரசியலமைப்பில் பகுதி IV-A (அடிப்படை கடமைகள்) எந்த அரசியலமைப்பு திருத்தச் சட்டத்தின் மூலம் சேர்க்கப்பட்டது?",
        "24th Amendment Act, 1971", "24வது திருத்தச் சட்டம், 1971",
        "44th Amendment Act, 1978", "44வது திருத்தச் சட்டம், 1978",
        "42nd Amendment Act, 1976", "42வது திருத்தச் சட்டம், 1976",
        "86th Amendment Act, 2002", "86வது திருத்தச் சட்டம், 2002",
        "C",
        "The 42nd Constitutional Amendment Act, 1976 added Part IV-A consisting of Article 51A specifying 10 Fundamental Duties for citizens.",
        "42வது அரசியலமைப்பு திருத்தச் சட்டம், 1976 சரத்து 51A ஐக் கொண்ட பகுதி IV-A ஐச் சேர்த்து குடிமக்களுக்கு 10 அடிப்படை கடமைகளை அறிமுகப்படுத்தியது.",
        "Option A is incorrect; 24th Amendment dealt with Article 368 amending power.", "விருப்பம் A தவறானது; 24வது திருத்தம் சரத்து 368 திருத்த அதிகாரம் பற்றியது.",
        "Option B is incorrect; 44th Amendment modified emergency provisions.", "விருப்பம் B தவறானது; 44வது திருத்தம் அவசரநிலை விதிகளை திருத்தியது.",
        "Option C is correct because 42nd Amendment Act, 1976 introduced Part IV-A based on Swaran Singh Committee recommendations.", "விருப்பம் C சரியானது, ஏனெனில் 42வது திருத்தச் சட்டம் 1976 ஸ்வரண் சிங் குழுவின் பரிந்துரையின் படி பகுதி IV-A ஐ சேர்த்தது.",
        "Option D is incorrect; 86th Amendment added the 11th Fundamental Duty (Art 51A(k)) in 2002.", "விருப்பம் D தவறானது; 86வது திருத்தம் 11வது அடிப்படை கடமையை 2002 இல் சேர்த்தது.",
        "Fundamental Duties were recommended by Swaran Singh Committee in 1976.",
        "அடிப்படை கடமைகள் 1976 இல் ஸ்வரண் சிங் குழுவால் பரிந்துரைக்கப்பட்டன.",
        "Originally 10 Fundamental Duties were added; 11th duty was added by 86th Amendment in 2002.",
        "ஆரம்பத்தில் 10 கடமைகள் சேர்க்கப்பட்டன; 11வது கடமை 86வது திருத்தத்தால் 2002 இல் சேர்க்கப்பட்டது.",
        "Remembering", "High", ["42nd Amendment", "Fundamental Duties", "Part IV-A"], "Part 2"
    )

    # Q024 - Correct: D
    add_q(
        "CZ_AM_EZ_024",
        "Creation of new States or alteration of areas, boundaries, or names of existing States under Articles 3 and 4 requires which type of majority in Parliament?",
        "சரத்துக்கள் 3 மற்றும் 4 இன் கீழ் புதிய மாநிலங்களை உருவாக்குவது அல்லது எல்லைகள், பெயர்களை மாற்றுவது நாடாளுமன்றத்தில் எந்த வகையான பெரும்பான்மையைக் கோருகிறது?",
        "Special majority under Article 368", "சரத்து 368 இன் கீழ் சிறப்பு பெரும்பான்மை",
        "Special majority with ratification by half of the states", "பாதி மாநிலங்களின் ஒப்புதலுடன் சிறப்பு பெரும்பான்மை",
        "Absolute majority of total membership", "மொத்த உறுப்பினர்களின் தனிப்பெரும்பான்மை",
        "Simple majority of Parliament", "நாடாளுமன்றத்தின் சாதாரண பெரும்பான்மை",
        "D",
        "Under Article 4(2), laws made under Articles 2 and 3 for creation/alteration of states are NOT considered constitutional amendments under Article 368 and require only a simple majority.",
        "சரத்து 4(2) இன் படி, மாநில உருவாக்கம்/எல்லை மாற்றத்திற்காக சரத்து 2 மற்றும் 3 இன் கீழ் செய்யப்படும் சட்டங்கள் சரத்து 368 இன் கீழான அரசியலமைப்பு திருத்தமாக கருதப்படாது; சாதாரண பெரும்பான்மையே போதுமானது.",
        "Option A is incorrect because Article 368 special majority is not required for reorganization of states within India.", "விருப்பம் A தவறானது, ஏனெனில் இந்தியாவிற்குள் மாநில மறுசீரமைப்பிற்கு சரத்து 368 சிறப்பு பெரும்பான்மை தேவை இல்லை.",
        "Option B is incorrect because state ratification is not needed for internal boundary changes.", "விருப்பம் B தவறானது, ஏனெனில் எல்லை மாற்றங்களுக்கு மாநிலங்களின் ஒப்புதல் தேவை இல்லை.",
        "Option C is incorrect because absolute majority is not the required threshold.", "விருப்பம் C தவறானது, ஏனெனில் தனிப்பெரும்பான்மை தேவையில்லை.",
        "Option D is correct because Article 4 explicitly states that Article 2 and 3 laws can be passed by simple majority like an ordinary law.", "விருப்பம் D சரியானது, ஏனெனில் சரத்து 4 இத்தகைய சட்டங்களை சாதாரண மசோதா போல சாதாரண பெரும்பான்மையால் நிறைவேற்றலாம் எனக் கூறுகிறது.",
        "However, ceding Indian territory to a foreign state (e.g. Berubari Union 1960) DOES require an amendment under Article 368.",
        "இருப்பினும், இந்திய நிலப்பரப்பை அயல்நாட்டிற்கு வழங்குவதற்கு (எ.கா. பெருபாரி யூனியன் 1960) சரத்து 368 இன் கீழ் திருத்தம் கட்டாயம் தேவை.",
        "Simple majority means a majority of members present and voting.",
        "சாதாரண பெரும்பான்மை என்பது வருகை தந்து வாக்களிக்கும் உறுப்பினர்களின் பெரும்பான்மையாகும்.",
        "Understanding", "High", ["Simple Majority", "Article 3 and 4", "State Creation"], "Part 1"
    )

    # Q025 - Correct: A
    add_q(
        "CZ_AM_EZ_025",
        "Which of the following matters CANNOT be amended by a simple majority of Parliament and requires a special majority under Article 368?",
        "பின்வரும் எந்த விஷயத்தை நாடாளுமன்றத்தின் சாதாரண பெரும்பான்மையால் திருத்த முடியாது, மேலும் சரத்து 368 இன் கீழ் சிறப்பு பெரும்பான்மை தேவைப்படுகிறது?",
        "Fundamental Rights and Directive Principles", "அடிப்படை உரிமைகள் மற்றும் அரசு நெறிமுறைக் கோட்பாடுகள்",
        "Abolition or creation of Legislative Councils in States", "மாநிலங்களில் சட்டமேலவையை உருவாக்குதல் அல்லது நீக்குதல்",
        "Use of official language in Parliament", "நாடாளுமன்றத்தில் அதிகாரப்பூர்வ மொழியின் பயன்பாடு",
        "Salaries and allowances of Members of Parliament", "நாடாளுமன்ற உறுப்பினர்களின் சம்பளம் மற்றும் படிகள்",
        "A",
        "Fundamental Rights (Part III) and Directive Principles (Part IV) require a Special Majority under Article 368 (2/3 present & voting + majority of total membership).",
        "அடிப்படை உரிமைகள் (பகுதி III) மற்றும் அரசு நெறிமுறைக் கோட்பாடுகள் (பகுதி IV) ஆகியவற்றைத் திருத்த சரத்து 368 இன் கீழ் சிறப்பு பெரும்பான்மை தேவைப்படுகிறது.",
        "Option A is correct because Fundamental Rights and DPSPs are amended under Article 368 by Special Majority.", "விருப்பம் A சரியானது, ஏனெனில் அடிப்படை உரிமைகள் மற்றும் DPSP சிறப்பு பெரும்பான்மையால் திருத்தப்படுகின்றன.",
        "Option B is incorrect; Article 169 allows creation/abolition of State Legislative Council by simple majority of Parliament.", "விருப்பம் B தவறானது; சரத்து 169 இன் படி சட்டமேலவை உருவாக்கம்/நீக்கம் சாதாரண பெரும்பான்மையால் செய்யப்படலாம்.",
        "Option C is incorrect; official language usage rules can be amended by simple majority.", "விருப்பம் C தவறானது; ஆட்சிமொழி பயன்பாட்டு விதிகளை சாதாரண பெரும்பான்மையால் திருத்தலாம்.",
        "Option D is incorrect; MP salaries are fixed by ordinary law using simple majority.", "விருப்பம் D தவறானது; எம்பி சம்பளங்கள் சாதாரண பெரும்பான்மை சட்டத்தால் நிர்ணயிக்கப்படுகின்றன.",
        "Amendments outside Article 368 (simple majority) are NOT deemed to be amendments of the Constitution for the purposes of Article 368.",
        "சரத்து 368 க்கு வெளியே செய்யப்படும் சாதாரண பெரும்பான்மை திருத்தங்கள் சரத்து 368 இன் கீழான அரசியலமைப்பு திருத்தங்களாகக் கருதப்பட மாட்டா.",
        "Simple majority matters include Quorum in Parliament, Rules of Procedure, Official Language, 5th and 6th Schedules.",
        "சாதாரண பெரும்பான்மை விஷயங்களில் குறைந்தபட்ச உறுப்பினர் எண்ணிக்கை (Quorum), நடைமுறை விதிகள், ஆட்சிமொழி, 5 மற்றும் 6வது அட்டவணைகள் அடங்கும்.",
        "Understanding", "High", ["Special Majority", "Article 368 Scope"], "Part 1"
    )

    # Q026 - Correct: B
    add_q(
        "CZ_AM_EZ_026",
        "Which of the following constitutional provisions requires Special Majority under Article 368 along with Ratification by Half of the State Legislatures?",
        "பின்வரும் எந்த அரசியலமைப்பு விதிக்கு சரத்து 368 இன் கீழ் சிறப்பு பெரும்பான்மையுடன் பாதி மாநில சட்டமன்றங்களின் ஒப்புதலும் தேவைப்படுகிறது?",
        "Salaries of Supreme Court Judges", "உச்ச நீதிமன்ற நீதிபதிகளின் சம்பளம்",
        "Election of the President and its manner", "குடியரசுத் தலைவர் தேர்தல் மற்றும் அதன் முறை",
        "Citizenship acquisition and termination", "குடியுரிமை பெறுதல் மற்றும் இழத்தல்",
        "Quorum in Parliament", "நாடாளுமன்றக் குறைந்தபட்ச உறுப்பினர் எண்ணிக்கை (Quorum)",
        "B",
        "Provisions affecting the federal structure (like Election of President under Articles 54 & 55) require Special Majority of Parliament PLUS ratification by at least half of the state legislatures by simple majority.",
        "கூட்டாட்சி அமைப்பைப் பாதிக்கும் விதிகள் (சரத்து 54 & 55 இன் கீழான குடியரசுத் தலைவர் தேர்தல் போன்றவை) நாடாளுமன்றத்தின் சிறப்பு பெரும்பான்மையுடன் குறைந்தது பாதி மாநில சட்டமன்றங்களின் சாதாரண பெரும்பான்மை ஒப்புதலையும் பெற வேண்டும்.",
        "Option A is incorrect; SC judges' salaries are specified in 2nd Schedule and amended by simple majority.", "விருப்பம் A தவறானது; நீதிപதிகள் சம்பளம் 2வது அட்டவணையில் உள்ளது, சாதாரண பெரும்பான்மையால் திருத்தலாம்.",
        "Option B is correct because Articles 54 and 55 (President election) form part of the federal framework requiring state ratification.", "விருப்பம் B சரியானது, ஏனெனில் சரத்து 54 மற்றும் 55 (குடியரசு தலைவர் தேர்தல்) கூட்டாட்சி அமைப்பின் அங்கமாக இருப்பதால் மாநில ஒப்புதல் தேவை.",
        "Option C is incorrect; Citizenship under Article 11 is amended by ordinary simple majority law.", "விருப்பம் C தவறானது; சரத்து 11 இன் கீழ் குடியுரிமை சாதாரண பெரும்பான்மையால் திருத்தப்படுகிறது.",
        "Option D is incorrect; Quorum in Parliament under Article 100(3) is amended by simple majority.", "விருப்பம் D தவறானது; Quorum விதி சாதாரண பெரும்பான்மையால் திருத்தப்படுகிறது.",
        "Ratification by States requires only a Simple Majority in the State Assembly.",
        "மாநில சட்டமன்றங்களில் ஒப்புதல் அளிப்பதற்கு சாதாரண பெரும்பான்மையே போதுமானது.",
        "States are given NO time limit in Article 368 to give or withhold their ratification.",
        "மாநிலங்கள் ஒப்புதல் அளிக்க சரத்து 368 இல் எவ்வித காலக்கெடுவும் நிர்ணயிக்கப்படவில்லை.",
        "Understanding", "High", ["State Ratification", "Federal Structure", "President Election"], "Part 1"
    )

    # Q027 - Correct: C
    add_q(
        "CZ_AM_EZ_027",
        "By which Constitutional Amendment Act were 4 new languages — Bodo, Dogri, Maithili, and Santhali — added to the 8th Schedule of the Constitution?",
        "போடோ, டோக்ரி, மைதிலி மற்றும் சந்தாலி ஆகிய 4 புதிய மொழிகள் எந்த அரசியலமைப்பு திருத்தச் சட்டத்தின் மூலம் 8வது அட்டவணையில் சேர்க்கப்பட்டன?",
        "21st Amendment Act, 1967", "21வது திருத்தச் சட்டம், 1967",
        "71st Amendment Act, 1992", "71வது திருத்தச் சட்டம், 1992",
        "92nd Amendment Act, 2003", "92வது திருத்தச் சட்டம், 2003",
        "96th Amendment Act, 2011", "96வது திருத்தச் சட்டம், 2011",
        "C",
        "The 92nd Constitutional Amendment Act, 2003 added Bodo, Dogri, Maithili, and Santhali (BDMS) to the 8th Schedule, raising total official languages from 18 to 22.",
        "92வது அரசியலமைப்பு திருத்தச் சட்டம், 2003 போடோ, டோக்ரி, மைதிலி, சந்தாலி ஆகிய 4 மொழிகளைச் சேர்த்து 8வது அட்டவணை மொழிகளின் எண்ணிக்கையை 18 லிருந்து 22 ஆக உயர்த்தியது.",
        "Option A is incorrect; 21st Amendment added Sindhi in 1967 (15th language).", "விருப்பம் A தவறானது; 21வது திருத்தம் 1967 இல் சிந்தியைச் சேர்த்தது.",
        "Option B is incorrect; 71st Amendment added Konkani, Manipuri, and Nepali in 1992 (16th, 17th, 18th languages).", "விருப்பம் B தவறானது; 71வது திருத்தம் கொங்கணி, மணிப்பூரி, நேபாளி மொழிகளைச் சேர்த்தது.",
        "Option C is correct because 92nd Amendment Act, 2003 added 4 languages (BDMS) making total 22.", "விருப்பம் C சரியானது, ஏனெனில் 92வது திருத்தச் சட்டம் 2003 4 மொழிகளைச் சேர்த்து மொத்தத்தை 22 ஆக்கியது.",
        "Option D is incorrect; 96th Amendment substituted 'Odia' for 'Oriya' in 2011.", "விருப்பம் D தவறானது; 96வது திருத்தம் 'ஒரியா' என்பதை 'ஒடியா' என மாற்றியது.",
        "Trick to remember 8th Schedule language additions: 21st CA (Sindhi) + 71st CA (KMN) = 92nd CA (BDMS). 21 + 71 = 92!",
        "நினைவில் கொள்ள சுலப வழி: 21வது திருத்தம் (சிந்தி) + 71வது திருத்தம் (கொங்கணி, மணிப்பூரி, நேபாளி) = 92வது திருத்தம் (போடோ, டோக்ரி, மைதிலி, சந்தாலி). 21 + 71 = 92!",
        "Original Constitution had 14 languages in the 8th Schedule.",
        "மூல அரசியலமைப்பின் 8வது அட்டவணையில் 14 மொழிகள் மட்டுமே இருந்தன.",
        "Remembering", "High", ["92nd Amendment", "8th Schedule", "Languages"], "Part 2"
    )

    # Q028 - Correct: D
    add_q(
        "CZ_AM_EZ_028",
        "National Commission for Backward Classes (NCBC) was given constitutional status by which Constitutional Amendment Act?",
        "தேசிய பிற்படுத்தப்பட்டோர் ஆணையத்திற்கு (NCBC) எந்த அரசியலமைப்பு திருத்தச் சட்டத்தின் மூலம் அரசியலமைப்பு அந்தஸ்து வழங்கப்பட்டது?",
        "89th Constitutional Amendment Act, 2003", "89வது அரசியலமைப்பு திருத்தச் சட்டம், 2003",
        "99th Constitutional Amendment Act, 2014", "99வது அரசியலமைப்பு திருத்தச் சட்டம், 2014",
        "101st Constitutional Amendment Act, 2016", "101வது அரசியலமைப்பு திருத்தச் சட்டம், 2016",
        "102nd Constitutional Amendment Act, 2018", "102வது அரசியலமைப்பு திருத்தச் சட்டம், 2018",
        "D",
        "The 102nd Constitutional Amendment Act, 2018 conferred constitutional status on NCBC by inserting Article 338B into the Constitution.",
        "102வது அரசியலமைப்பு திருத்தச் சட்டம், 2018 சரத்து 338B ஐச் சேர்த்து தேசிய பிற்படுத்தப்பட்டோர் ஆணையத்திற்கு அரசியலமைப்பு அந்தஸ்தை வழங்கியது.",
        "Option A is incorrect; 89th Amendment bifurcated NCSC (Art 338) and NCST (Art 338A).", "விருப்பம் A தவறானது; 89வது திருத்தம் எஸ்சி மற்றும் எஸ்டி ஆணையங்களைப் பிரித்தது.",
        "Option B is incorrect; 99th Amendment established NJAC (later invalidated).", "விருப்பம் B தவறானது; 99வது திருத்தம் NJAC அமைக்கப்பட்டது.",
        "Option C is incorrect; 101st Amendment introduced GST.", "விருப்பம் C தவறானது; 101வது திருத்தம் ஜிஎஸ்டி பற்றியது.",
        "Option D is correct because 102nd Amendment Act, 2018 inserted Article 338B giving constitutional status to NCBC.", "விருப்பம் D சரியானது, ஏனெனில் 102வது திருத்தச் சட்டம் 2018 சரத்து 338B ஐச் சேர்த்து NCBC க்கு அரசியலமைப்பு அந்தஸ்தளித்தது.",
        "Article 338 = NCSC, Article 338A = NCST, Article 338B = NCBC.",
        "சரத்து 338 = ஆதிதிராவிடர் ஆணையம், 338A = பழங்குடியினர் ஆணையம், 338B = பிற்படுத்தப்பட்டோர் ஆணையம்.",
        "102nd Amendment also inserted Article 342A relating to SEBC lists.",
        "102வது திருத்தம் பிற்படுத்தப்பட்டோர் பட்டியல் தொடர்பான சரத்து 342A ஐயும் சேர்த்தது.",
        "Remembering", "High", ["102nd Amendment", "NCBC", "Article 338B"], "Part 2"
    )

    # Q029 - Correct: A
    add_q(
        "CZ_AM_EZ_029",
        "Which Constitutional Amendment Act created the Union Territory of Puducherry and provided for its Council of Ministers and Legislature?",
        "புதுச்சேரி யூனியன் பிரதேசத்தை உருவாக்கி, அதன் சட்டமன்றம் மற்றும் அமைச்சரவைக்கு வழிவகை செய்த அரசியலமைப்பு திருத்தச் சட்டம் எது?",
        "14th Constitutional Amendment Act, 1962", "14வது அரசியலமைப்பு திருத்தச் சட்டம், 1962",
        "12th Constitutional Amendment Act, 1962", "12வது அரசியலமைப்பு திருத்தச் சட்டம், 1962",
        "10th Constitutional Amendment Act, 1961", "10வது அரசியலமைப்பு திருத்தச் சட்டம், 1961",
        "18th Constitutional Amendment Act, 1966", "18வது அரசியலமைப்பு திருத்தச் சட்டம், 1966",
        "A",
        "The 14th Constitutional Amendment Act, 1962 incorporated Puducherry into the Indian Union and inserted Article 239A enabling legislatures for UTs.",
        "14வது அரசியலமைப்பு திருத்தச் சட்டம், 1962 புதுச்சேரியை இந்திய யூனியனில் இணைத்ததுடன், யூனியன் பிரதேசங்களுக்குச் சட்டமன்றம் அமைக்க சரத்து 239A ஐச் சேர்த்தது.",
        "Option A is correct because 14th Amendment Act, 1962 added Puducherry as a UT and created Article 239A.", "விருப்பம் A சரியானது, ஏனெனில் 14வது திருத்தச் சட்டம் 1962 புதுச்சேரியை இணைத்து சரத்து 239A ஐ உருவாக்கியது.",
        "Option B is incorrect; 12th Amendment incorporated Goa, Daman and Diu as UT.", "விருப்பம் B தவறானது; 12வது திருத்தம் கோவா, டாமன் டையூவை இணைத்தது.",
        "Option C is incorrect; 10th Amendment incorporated Dadra and Nagar Haveli.", "விருப்பம் C தவறானது; 10வது திருத்தம் தாத்ரா நாகர் ஹவேலியை இணைத்தது.",
        "Option D is incorrect; 18th Amendment clarified meaning of 'State' in Article 3.", "விருப்பம் D தவறானது; 18வது திருத்தம் சரத்து 3 இல் 'மாநிலம்' என்ற சொல்லின் பொருளைத் தெளிவுபடுத்தியது.",
        "Article 239A enabled Parliament to create Legislature and Council of Ministers for certain UTs including Puducherry.",
        "சரத்து 239A புதுச்சேரி உள்ளிட்ட சில யூனியன் பிரதேசங்களுக்கு சட்டமன்றம் அமைக்க நாடாளுமன்றத்திற்கு அதிகாரம் அளித்தது.",
        "Puducherry was previously under French administration.",
        "புதுச்சேரி முன்னதாக பிரெஞ்சு நிர்வாகத்தின் கீழ் இருந்தது.",
        "Remembering", "High", ["14th Amendment", "Puducherry", "Article 239A"], "Part 2"
    )

    # Q030 - Correct: B
    add_q(
        "CZ_AM_EZ_030",
        "The National Capital Territory of Delhi was created with a 70-member Legislative Assembly by which Constitutional Amendment Act?",
        "70 உறுப்பினர்களைக் கொண்ட சட்டமன்றத்துடன் டெல்லி தேசிய தலைநகர் பிரதேசம் (NCT of Delhi) எந்த அரசியலமைப்பு திருத்தச் சட்டத்தின் மூலம் உருவாக்கப்பட்டது?",
        "65th Constitutional Amendment Act, 1990", "65வது அரசியலமைப்பு திருத்தச் சட்டம், 1990",
        "69th Constitutional Amendment Act, 1991", "69வது அரசியலமைப்பு திருத்தச் சட்டம், 1991",
        "70th Constitutional Amendment Act, 1992", "70வது அரசியலமைப்பு திருத்தச் சட்டம், 1992",
        "73rd Constitutional Amendment Act, 1992", "73வது அரசியலமைப்பு திருத்தச் சட்டம், 1992",
        "B",
        "The 69th Constitutional Amendment Act, 1991 inserted Articles 239AA and 239AB designating Delhi as National Capital Territory with a 70-member Assembly.",
        "69வது அரசியலமைப்பு திருத்தச் சட்டம், 1991 சரத்துகள் 239AA மற்றும் 239AB ஐச் சேர்த்து டெல்லியை 70 உறுப்பினர்களைக் கொண்ட சட்டமன்றத்துடன் தேசிய தலைநகர் பிரதேசமாக மாற்றியது.",
        "Option A is incorrect; 65th Amendment established NCSC & ST multi-member commission.", "விருப்பம் A தவறானது; 65வது திருத்தம் எஸ்சி/எஸ்டி ஆணையம் பற்றியது.",
        "Option B is correct because 69th Amendment Act, 1991 designated Delhi as NCT of Delhi.", "விருப்பம் B சரியானது, ஏனெனில் 69வது திருத்தச் சட்டம் 1991 டெல்லியை NCT ஆக்கியது.",
        "Option C is incorrect; 70th Amendment enabled Delhi Assembly members to vote in Presidential elections.", "விருப்பம் C தவறானது; 70வது திருத்தம் டெல்லி எம்.எல்.ஏக்கள் குடியரசு தலைவர் தேர்தலில் வாக்களிக்க வழிசெய்தது.",
        "Option D is incorrect; 73rd Amendment related to Panchayati Raj.", "விருப்பம் D தவறானது; 73வது திருத்தம் பஞ்சாயத்து ராஜ் பற்றியது.",
        "69th Amendment capped Delhi Council of Ministers at 10% of Assembly strength (7 ministers including CM) under Article 239AA(4).",
        "69வது திருத்தம் டெல்லி அமைச்சரவை அளவை சட்டமன்ற எண்ணிக்கையில் 10% (முதல்வர் உட்பட 7 அமைச்சர்கள்) என சரத்து 239AA(4) இல் நிர்ணயித்தது.",
        "S. Balakrishnan Committee recommendations led to the 69th Amendment Act, 1991.",
        "எஸ். பாலகிருஷ்ணன் குழுவின் பரிந்துரைகள் 69வது திருத்தச் சட்டம் உருவாக வழிவகுத்தன.",
        "Remembering", "High", ["69th Amendment", "Delhi NCT", "Article 239AA"], "Part 2"
    )

    # Q031 - Correct: C
    add_q(
        "CZ_AM_EZ_031",
        "Sikkim was conferred the status of a full-fledged 22nd State of the Indian Union by which Constitutional Amendment Act?",
        "சிக்கிம் இந்திய யூனியனின் 22வது மாநிலமாக முழு மாநில அந்தஸ்தைப் பெற்ற அரசியலமைப்பு திருத்தச் சட்டம் எது?",
        "35th Constitutional Amendment Act, 1974", "35வது அரசியலமைப்பு திருத்தச் சட்டம், 1974",
        "31st Constitutional Amendment Act, 1973", "31வது அரசியலமைப்பு திருத்தச் சட்டம், 1973",
        "36th Constitutional Amendment Act, 1975", "36வது அரசியலமைப்பு திருத்தச் சட்டம், 1975",
        "38th Constitutional Amendment Act, 1975", "38வது அரசியலமைப்பு திருத்தச் சட்டம், 1975",
        "C",
        "The 36th Constitutional Amendment Act, 1975 made Sikkim a full state of India (22nd State) and inserted Article 371F containing special provisions for Sikkim.",
        "36வது அரசியலமைப்பு திருத்தச் சட்டம், 1975 சிக்கிமை இந்தியாவின் 22வது முழு மாநிலமாக்கியது மற்றும் சரத்து 371F ஐச் சேர்த்தது.",
        "Option A is incorrect; 35th Amendment (1974) made Sikkim an 'Associate State' under 10th Schedule (old).", "விருப்பம் A தவறானது; 35வது திருத்தம் சிக்கிமை 'இணை மாநிலமாக' மட்டுமே ஆக்கியது.",
        "Option B is incorrect; 31st Amendment increased Lok Sabha strength from 525 to 545.", "விருப்பம் B தவறானது; 31வது திருத்தம் மக்களவை இடங்களை 545 ஆக உயர்த்தியது.",
        "Option C is correct because 36th Amendment Act, 1975 conferred full statehood on Sikkim.", "விருப்பம் C சரியானது, ஏனெனில் 36வது திருத்தச் சட்டம் 1975 சிக்கிமுக்கு முழு மாநில அந்தஸ்து வழங்கியது.",
        "Option D is incorrect; 38th Amendment made declaration of Emergency non-justiciable.", "விருப்பம் D தவறானது; 38வது திருத்தம் அவசரநிலை அறிவிப்பை நீதிமன்ற ஆய்வுக்கு அப்பாற்பட்டதாக்கியது.",
        "35th CA made Sikkim an 'Associate State' (1974), while 36th CA made Sikkim a 'Full State' (1975).",
        "35வது திருத்தம் இணை மாநில அந்தஸ்தையும் (1974), 36வது திருத்தம் முழு மாநில அந்தஸ்தையும் (1975) வழங்கின.",
        "Article 371F provides special provisions with respect to the State of Sikkim.",
        "சரத்து 371F சிக்கிம் மாநிலத்திற்கான சிறப்பு விதிகளைக் கொண்டுள்ளது.",
        "Remembering", "High", ["36th Amendment", "Sikkim Statehood", "Article 371F"], "Part 2"
    )

    # Q032 - Correct: D
    add_q(
        "CZ_AM_EZ_032",
        "By which Constitutional Amendment Act was the Privy Purses and privileges of former rulers of princely states abolished?",
        "சுதேச சமஸ்தானங்களின் முன்னாள் ஆட்சியாளர்களின் மன்னர் மானியம் (Privy Purses) மற்றும் சிறப்புரிமைகள் எந்த அரசியலமைப்பு திருத்தச் சட்டத்தின் மூலம் ரத்து செய்யப்பட்டன?",
        "24th Constitutional Amendment Act, 1971", "24வது அரசியலமைப்பு திருத்தச் சட்டம், 1971",
        "25th Constitutional Amendment Act, 1971", "25வது அரசியலமைப்பு திருத்தச் சட்டம், 1971",
        "29th Constitutional Amendment Act, 1972", "29வது அரசியலமைப்பு திருத்தச் சட்டம், 1972",
        "26th Constitutional Amendment Act, 1971", "26வது அரசியலமைப்பு திருத்தச் சட்டம், 1971",
        "D",
        "The 26th Constitutional Amendment Act, 1971 abolished Privy Purses and privileges of former princely state rulers by omitting Articles 291 and 362.",
        "26வது அரசியலமைப்பு திருத்தச் சட்டம், 1971 சரத்துகள் 291 மற்றும் 362 ஐ நீக்கி சுதேச மன்னர்களின் மன்னர் மானியத்தையும் சிறப்புரிமைகளையும் ரத்து செய்தது.",
        "Option A is incorrect; 24th Amendment affirmed Parliament's amending power under Art 368.", "விருப்பம் A தவறானது; 24வது திருத்தம் சரத்து 368 இன் திருத்த அதிகாரத்தை உறுதி செய்தது.",
        "Option B is incorrect; 25th Amendment curtailed Right to Property and inserted Art 31C.", "விருப்பம் B தவறானது; 25வது திருத்தம் சொத்துரிமையைக் குறைத்து சரத்து 31C ஐச் சேர்த்தது.",
        "Option C is incorrect; 29th Amendment placed Kerala land reform acts in 9th Schedule.", "விருப்பம் C தவறானது; 29வது திருத்தம் கேரள நிலச் சீர்திருத்தங்களை 9வது அட்டவணையில் சேர்த்தது.",
        "Option D is correct because 26th Amendment Act, 1971 abolished Privy Purses under Prime Minister Indira Gandhi.", "விருப்பம் D சரியானது, ஏனெனில் பிரதமர் இந்திரா காந்தி காலத்தில் 26வது திருத்தச் சட்டம் 1971 மன்னர் மானியத்தை ரத்து செய்தது.",
        "Articles 291 and 362 were omitted, and Article 363A was inserted by the 26th Amendment Act.",
        "26வது திருத்தத்தின் மூலம் சரத்துகள் 291, 362 நீக்கப்பட்டு, சரத்து 363A புதிதாகச் சேர்க்கப்பட்டது.",
        "Supreme Court had earlier struck down Presidential Order derecognising princes in Madhav Rao Scindia case (1970).",
        "முன்னதாக மாதவ் ராவ் சிந்தியா வழக்கில் (1970) மன்னர் உரிமையை பறித்த அரசாணையை உச்ச நீதிமன்றம் ரத்து செய்திருந்தது.",
        "Remembering", "High", ["26th Amendment", "Privy Purses Abolition"], "Part 2"
    )

    # Q033 - Correct: A
    add_q(
        "CZ_AM_EZ_033",
        "The National Judicial Appointments Commission (NJAC) introduced by the 99th Constitutional Amendment Act, 2014 was struck down as unconstitutional by Supreme Court in which year?",
        "99வது அரசியலமைப்பு திருத்தச் சட்டம் 2014 மூலம் கொண்டுவரப்பட்ட தேசிய நீதிபதிகள் நியமன ஆணையத்தை (NJAC) உச்ச நீதிமன்றம் எந்த ஆண்டில் அரசியலமைப்பிற்கு முரணானது என ரத்து செய்தது?",
        "2015", "2015",
        "2016", "2016",
        "2017", "2017",
        "2014", "2014",
        "A",
        "In October 2015 (Fourth Judges Case), a 5-judge Supreme Court bench by 4-1 majority struck down 99th CA and NJAC Act as violating judicial independence, a basic structure feature.",
        "2015 அக்டோபரில் (நான்காவது நீதிபதிகள் வழக்கு) 5 நீதிபதிகள் கொண்ட உச்ச நீதிமன்ற அமர்வு 4-1 பெரும்பான்மையில் 99வது திருத்தம் மற்றும் NJAC சட்டத்தை நீதித்துறை சுதந்திரத்தை மீறுவதாகக் கூறி ரத்து செய்தது.",
        "Option A is correct because the Supreme Court declared NJAC unconstitutional on October 16, 2015.", "விருப்பம் A சரியானது, ஏனெனில் 2015 அக்டோபர் 16 அன்று உச்ச நீதிமன்றம் NJAC செல்லாது என அறிவித்தது.",
        "Option B is incorrect; 2016 was when 101st GST amendment was passed.", "விருப்பம் B தவறானது; 2016 இல் 101வது ஜிஎஸ்டி திருத்தம் நிறைவேற்றப்பட்டது.",
        "Option C is incorrect; 2017 was the year GST was launched.", "விருப்பம் C தவறானது; 2017 ஜிஎஸ்டி அமல்படுத்தப்பட்ட ஆண்டு.",
        "Option D is incorrect; 2014 was the year Parliament passed the 99th Amendment Bill.", "விருப்பம் D தவறானது; 2014 நாடாளுமன்றம் 99வது திருத்தத்தை நிறைவேற்றிய ஆண்டு.",
        "99th Amendment is the ONLY Constitutional Amendment Act in Indian history to be completely struck down by the Supreme Court.",
        "இந்திய வரலாற்றிலேயே உச்ச நீதிமன்றத்தால் முழுமையாக ரத்து செய்யப்பட்ட ஒரே அரசியலமைப்பு திருத்தச் சட்டம் 99வது திருத்தச் சட்டமாகும்.",
        "The Judgment restored the Collegium System for appointment of judges.",
        "இத்தீர்ப்பு நீதிபதிகள் நியமனத்திற்கான கொலீஜியம் முறையை மீண்டும் அமல்படுத்தியது.",
        "Remembering", "High", ["99th Amendment", "NJAC", "2015 Judgment"], "Part 2"
    )

    # Q034 - Correct: B
    add_q(
        "CZ_AM_EZ_034",
        "Which Constitutional Amendment Act gave effect to the 1974 Land Boundary Agreement (LBA) and its 2011 Protocol between India and Bangladesh?",
        "இந்தியா மற்றும் வங்காளதேசம் இடையே 1974 நில எல்லை ஒப்பந்தம் மற்றும் 2011 நெறிமுறைக்கு செயல்வடிவம் அளித்த அரசியலமைப்பு திருத்தச் சட்டம் எது?",
        "99th Constitutional Amendment Act, 2014", "99வது அரசியலமைப்பு திருத்தச் சட்டம், 2014",
        "100th Constitutional Amendment Act, 2015", "100வது அரசியலமைப்பு திருத்தச் சட்டம், 2015",
        "101st Constitutional Amendment Act, 2016", "101வது அரசியலமைப்பு திருத்தச் சட்டம், 2016",
        "102nd Constitutional Amendment Act, 2018", "102வது அரசியலமைப்பு திருத்தச் சட்டம், 2018",
        "B",
        "The 100th Constitutional Amendment Act, 2015 amended 1st Schedule to exchange enclaves between India and Bangladesh under the 1974 Land Boundary Agreement.",
        "100வது அரசியலமைப்பு திருத்தச் சட்டம், 2015 1வது அட்டவணையைத் திருத்தி, 1974 நில எல்லை ஒப்பந்தத்தின்படி இந்தியாவிற்கும் வங்காளதேசத்திற்கும் இடையே நிலப் பகுதிகளை பரிமாற்றம் செய்ய வழிவகுத்தது.",
        "Option A is incorrect; 99th Amendment related to NJAC.", "விருப்பம் A தவறானது; 99வது திருத்தம் NJAC பற்றியது.",
        "Option B is correct because 100th Amendment Act, 2015 implemented the enclave exchange with Bangladesh.", "விருப்பம் B சரியானது, ஏனெனில் 100வது திருத்தச் சட்டம் 2015 வங்காளதேச எல்லை ஒப்பந்தத்தைச் செயல்படுத்தியது.",
        "Option C is incorrect; 101st Amendment introduced GST.", "விருப்பம் C தவறானது; 101வது திருத்தம் ஜிஎஸ்டி பற்றியது.",
        "Option D is incorrect; 102nd Amendment gave status to NCBC.", "விருப்பம் D தவறானது; 102வது திருத்தம் NCBC அந்தஸ்து பற்றியது.",
        "India transferred 111 enclaves to Bangladesh and received 51 enclaves from Bangladesh under the 100th Amendment Act.",
        "100வது திருத்தத்தின் படி இந்தியா 111 நிலப்பகுதிகளை வங்காளதேசத்திற்கும், வங்காளதேசம் 51 நிலப்பகுதிகளை இந்தியாவிற்கும் வழங்கின.",
        "It amended 1st Schedule territories of Assam, West Bengal, Meghalaya, and Tripura.",
        "இது அசாம், மேற்கு வங்கம், மேகலாயா, திரிபுரா ஆகிய மாநிலங்களின் எல்லைப் பகுதிகளைத் திருத்தியது.",
        "Remembering", "High", ["100th Amendment", "Land Boundary Agreement", "Bangladesh"], "Part 2"
    )

    # Q035 - Correct: C
    add_q(
        "CZ_AM_EZ_035",
        "Which Constitutional Amendment Act established the National Commission for Scheduled Castes (NCSC) and National Commission for Scheduled Tribes (NCST) as two separate bodies?",
        "ஆதிதிராவிடர் தேசிய ஆணையம் (NCSC) மற்றும் பழங்குடியினர் தேசிய ஆணையம் (NCST) என இரண்டையும் இரு தனித்தனி அமைப்புகளாகப் பிரித்த அரசியலமைப்பு திருத்தச் சட்டம் எது?",
        "65th Constitutional Amendment Act, 1990", "65வது அரசியலமைப்பு திருத்தச் சட்டம், 1990",
        "79th Constitutional Amendment Act, 1999", "79வது அரசியலமைப்பு திருத்தச் சட்டம், 1999",
        "89th Constitutional Amendment Act, 2003", "89வது அரசியலமைப்பு திருத்தச் சட்டம், 2003",
        "94th Constitutional Amendment Act, 2006", "94வது அரசியலமைப்பு திருத்தச் சட்டம், 2006",
        "C",
        "The 89th Constitutional Amendment Act, 2003 bifurcated the combined NCSC & ST into NCSC (Article 338) and NCST (Article 338A).",
        "89வது அரசியலமைப்பு திருத்தச் சட்டம், 2003 ஒருங்கிணைந்த ஆணையத்தைப் பிரித்து NCSC (சரத்து 338) மற்றும் NCST (சரத்து 338A) என இரு அமைப்புகளை உருவாக்கியது.",
        "Option A is incorrect; 65th Amendment created single combined multi-member NCSC & ST in 1990.", "விருப்பம் A தவறானது; 65வது திருத்தம் 1990 இல் ஒரே ஒருங்கிணைந்த ஆணையத்தை உருவாக்கியது.",
        "Option B is incorrect; 79th Amendment extended SC/ST reservation in Lok Sabha/Assemblies for 10 years.", "விருப்பம் B தவறானது; 79வது திருத்தம் எஸ்சி/எஸ்டி இடஒதுக்கீட்டை நீட்டித்தது.",
        "Option C is correct because 89th Amendment Act, 2003 split the body into NCSC (Art 338) and NCST (Art 338A).", "விருப்பம் C சரியானது, ஏனெனில் 89வது திருத்தச் சட்டம் 2003 ஆணையத்தை NCSC மற்றும் NCST எனப் பிரித்தது.",
        "Option D is incorrect; 94th Amendment freed Bihar from mandatory Tribal Welfare Minister requirement.", "விருப்பம் D தவறானது; 94வது திருத்தம் பீகாரை பழங்குடியினர் நல அமைச்சர் நியமனக் கட்டாயத்திலிருந்து விலக்கியது.",
        "Article 338 deals with NCSC, while Article 338A deals with NCST.",
        "சரத்து 338 ஆதிதிராவிடர் ஆணையத்தையும், சரத்து 338A பழங்குடியினர் ஆணையத்தையும் கையாள்கிறது.",
        "The split came into effect in February 2004.",
        "இந்த பிரிவு 2004 பிப்ரவரியில் அமலுக்கு வந்தது.",
        "Remembering", "High", ["89th Amendment", "NCSC and NCST", "Article 338A"], "Part 2"
    )

    # Q036 - Correct: D
    add_q(
        "CZ_AM_EZ_036",
        "By which Constitutional Amendment Act were Administrative Tribunals (Article 323A) and Tribunals for other matters (Article 323B) inserted under Part XIV-A?",
        "நிர்வாகத் தீர்ப்பாயங்கள் (சரத்து 323A) மற்றும் பிற விஷயங்களுக்கான தீர்ப்பாயங்கள் (சரத்து 323B) பகுதி XIV-A இன் கீழ் எந்த அரசியலமைப்பு திருத்தச் சட்டத்தின் மூலம் சேர்க்கப்பட்டன?",
        "24th Amendment Act, 1971", "24வது திருத்தச் சட்டம், 1971",
        "44th Amendment Act, 1978", "44வது திருத்தச் சட்டம், 1978",
        "52nd Amendment Act, 1985", "52வது திருத்தச் சட்டம், 1985",
        "42nd Amendment Act, 1976", "42வது திருத்தச் சட்டம், 1976",
        "D",
        "The 42nd Constitutional Amendment Act, 1976 added Part XIV-A entitled 'Tribunals', containing Articles 323A and 323B.",
        "42வது அரசியலமைப்பு திருத்தச் சட்டம், 1976 பகுதி XIV-A 'தீர்ப்பாயங்கள்' தலைப்பில் சரத்துகள் 323A மற்றும் 323B ஐச் சேர்த்தது.",
        "Option A is incorrect; 24th Amendment dealt with Art 368 amending procedures.", "விருப்பம் A தவறானது; 24வது திருத்தம் சரத்து 368 நடைமுறை பற்றியது.",
        "Option B is incorrect; 44th Amendment removed Right to Property as FR.", "விருப்பம் B தவறானது; 44வது திருத்தம் சொத்துரிமையை நீக்கியது.",
        "Option C is incorrect; 52nd Amendment dealt with Anti-Defection Law.", "விருப்பம் C தவறானது; 52வது திருத்தம் கட்சித் தாவல் சட்டம் பற்றியது.",
        "Option D is correct because 42nd Amendment Act, 1976 added Part XIV-A (Tribunals) to the Constitution.", "விருப்பம் D சரியானது, ஏனெனில் 42வது திருத்தச் சட்டம் 1976 பகுதி XIV-A (தீர்ப்பாயங்கள்) ஐச் சேர்த்தது.",
        "Article 323A deals with Administrative Tribunals, while Article 323B deals with Tribunals for other matters.",
        "சரத்து 323A நிர்வாகத் தீர்ப்பாயங்களையும், 323B பிற தீர்ப்பாயங்களையும் கையாள்கிறது.",
        "Central Administrative Tribunal (CAT) was set up in 1985 under the Administrative Tribunals Act, 1985.",
        "மத்திய நிர்வாகத் தீர்ப்பாயம் (CAT) 1985 இல் நிர்வாகத் தீர்ப்பாயச் சட்டத்தின் கீழ் அமைக்கப்பட்டது.",
        "Remembering", "High", ["42nd Amendment", "Part XIV-A", "Tribunals"], "Part 2"
    )

    # Q037 - Correct: A
    add_q(
        "CZ_AM_EZ_037",
        "Which Constitutional Amendment Act restored the power of State Governments and Union Territories to identify and specify Socially and Educationally Backward Classes (SEBCs)?",
        "சமூக மற்றும் கல்வியில் பின்தங்கிய வகுப்பினரை (SEBCs) அடையாளம் காணும் அதிகாரத்தை மாநில அரசுகள் மற்றும் யூனியன் பிரதேசங்களுக்கு மீண்டும் வழங்கிய அரசியலமைப்பு திருத்தச் சட்டம் எது?",
        "105th Constitutional Amendment Act, 2021", "105வது அரசியலமைப்பு திருத்தச் சட்டம், 2021",
        "102nd Constitutional Amendment Act, 2018", "102வது அரசியலமைப்பு திருத்தச் சட்டம், 2018",
        "103rd Constitutional Amendment Act, 2019", "103வது அரசியலமைப்பு திருத்தச் சட்டம், 2019",
        "104th Constitutional Amendment Act, 2020", "104வது அரசியலமைப்பு திருத்தச் சட்டம், 2020",
        "A",
        "The 105th Constitutional Amendment Act, 2021 clarified Article 342A to restore the power of States/UTs to prepare and maintain their own state SEBC lists, overcoming Supreme Court ruling in Maratha reservation case.",
        "105வது அரசியலமைப்பு திருத்தச் சட்டம், 2021 சரத்து 342A ஐத் தெளிவுபடுத்தி, மராத்தா இடஒதுக்கீட்டு வழக்கில் உச்ச நீதிமன்றத் தீர்ப்பைத் தொடர்ந்து மாநிலங்கள் தங்கள் சொந்த SEBC பட்டியலை தயாரிக்கும் அதிகாரத்தை மீட்டெடுத்தது.",
        "Option A is correct because 105th Amendment Act, 2021 restored state-level SEBC identification powers.", "விருப்பம் A சரியானது, ஏனெனில் 105வது திருத்தச் சட்டம் 2021 மாநிலங்களின் SEBC பட்டியல் அதிகாரத்தை மீட்டெடுத்தது.",
        "Option B is incorrect; 102nd Amendment (2018) inserted Art 338B and Art 342A which created confusion regarding state list powers.", "விருப்பம் B தவறானது; 102வது திருத்தம் மாநில அதிகாரத்தில் குழப்பத்தை உருவாக்கியது.",
        "Option C is incorrect; 103rd Amendment related to EWS 10% quota.", "விருப்பம் C தவறானது; 103வது திருத்தம் EWS இடஒதுக்கீடு பற்றியது.",
        "Option D is incorrect; 104th Amendment extended SC/ST reservation and ended Anglo-Indian seats.", "விருப்பம் D தவறானது; 104வது திருத்தம் எஸ்சி/எஸ்டி இடஒதுக்கீடு பற்றியது.",
        "105th Amendment amended Articles 338B, 342A, and 366(26C).",
        "105வது திருத்தம் சரத்துகள் 338B, 342A மற்றும் 366(26C) ஆகியவற்றைத் திருத்தியது.",
        "It clarifies that states can maintain a state SEBC list distinct from the Central List.",
        "மாநிலங்கள் மத்திய பட்டியலிலிருந்து வேறுபட்ட மாநில SEBC பட்டியலைப் பராமரிக்கலாம் என்பதை இது தெளிவுபடுத்துகிறது.",
        "Remembering", "High", ["105th Amendment", "SEBC State Power"], "Part 2"
    )

    # Q038 - Correct: B
    add_q(
        "CZ_AM_EZ_038",
        "Which Constitutional Amendment Act added Article 43B in Part IV (Directive Principles) promoting Voluntary Formation and Autonomous Functioning of Co-operative Societies?",
        "கூட்டுறவுச் சங்கங்களின் தன்னாட்சி இயக்கம் மற்றும் தன்னார்வ உருவாக்கத்தை ஊக்குவிக்க பகுதி IV (DPSP) இல் சரத்து 43B ஐச் சேர்த்த அரசியலமைப்பு திருத்தச் சட்டம் எது?",
        "91st Constitutional Amendment Act, 2003", "91வது அரசியலமைப்பு திருத்தச் சட்டம், 2003",
        "97th Constitutional Amendment Act, 2011", "97வது அரசியலமைப்பு திருத்தச் சட்டம், 2011",
        "86th Constitutional Amendment Act, 2002", "86வது அரசியலமைப்பு திருத்தச் சட்டம், 2002",
        "74th Constitutional Amendment Act, 1992", "74வது அரசியலமைப்பு திருத்தச் சட்டம், 1992",
        "B",
        "The 97th Constitutional Amendment Act, 2011 added Article 19(1)(c) right to form co-operatives, inserted DPSP Article 43B, and added Part IX-B (Articles 243ZH to 243ZT).",
        "97வது அரசியலமைப்பு திருத்தச் சட்டம், 2011 சரத்து 19(1)(c) இல் கூட்டுறவு உருவாக்கும் உரிமை, DPSP இல் சரத்து 43B மற்றும் பகுதி IX-B ஆகியவற்றைச் சேர்த்தது.",
        "Option A is incorrect; 91st Amendment capped Council of Ministers at 15%.", "விருப்பம் A தவறானது; 91வது திருத்தம் அமைச்சரவை அளவைக் கட்டுப்படுத்தியது.",
        "Option B is correct because 97th Amendment Act, 2011 constitutionalised Co-operative Societies by inserting Article 43B and Part IX-B.", "விருப்பம் B சரியானது, ஏனெனில் 97வது திருத்தச் சட்டம் 2011 சரத்து 43B மற்றும் பகுதி IX-B ஐச் சேர்த்தது.",
        "Option C is incorrect; 86th Amendment introduced Right to Education.", "விருப்பம் C தவறானது; 86வது திருத்தம் கல்வி உரிமை பற்றியது.",
        "Option D is incorrect; 74th Amendment constitutionalised Municipalities.", "விருப்பம் D தவறானது; 74வது திருத்தம் நகராட்சிகள் பற்றியது.",
        "Supreme Court in Union of India v. Rajendra N. Shah (2021) struck down Part IX-B in so far as it related to state co-operative societies for lack of state ratification under Art 368(2).",
        "மத்திய அரசு எதிர் ராஜேந்திர என் ஷா (2021) வழக்கில் உச்ச நீதிமன்றம் பகுதி IX-B இன் மாநில கூட்டுறவு சங்கங்கள் தொடர்பான விதிகளை மாநில ஒப்புதல் பெறாததால் ரத்து செய்தது.",
        "Article 19(1)(c) fundamental right was amended to include 'co-operative societies'.",
        "சரத்து 19(1)(c) அடிப்படை உரிமையில் 'கூட்டுறவு சங்கங்கள்' சேர்க்கப்பட்டன.",
        "Remembering", "High", ["97th Amendment", "Co-operative Societies", "Article 43B"], "Part 2"
    )

    # Q039 - Correct: C
    add_q(
        "CZ_AM_EZ_039",
        "In the Supreme Court judgement of Minerva Mills v. Union of India (1980), which section of the 42nd Amendment Act attempting to bar judicial review of amendments was struck down?",
        "மினர்வா மில்ஸ் எதிர் இந்திய யூனியன் (1980) வழக்கில் உச்ச நீதிமன்றம் 42வது திருத்தச் சட்டத்தின் எந்தப் பிரிவுகளை நீதித்துறை மறுாய்வைத் தடுப்பதாகக் கூறி ரத்து செய்தது?",
        "Section 2 and Section 3", "பிரிவு 2 மற்றும் பிரிவு 3",
        "Section 10 and Section 12", "பிரிவு 10 மற்றும் பிரிவு 12",
        "Section 4 and Section 55", "பிரிவு 4 மற்றும் பிரிவு 55",
        "Section 20 and Section 22", "பிரிவு 20 மற்றும் பிரிவு 22",
        "C",
        "In Minerva Mills Case (1980), Supreme Court struck down Section 4 (amending Art 31C) and Section 55 (inserting Art 368(4) & (5)) of the 42nd Amendment Act as unconstitutional.",
        "மினர்வா மில்ஸ் வழக்கில் (1980) 42வது திருத்தச் சட்டத்தின் பிரிவு 4 (சரத்து 31C திருத்தம்) மற்றும் பிரிவு 55 (சரத்து 368(4)&(5) சேர்க்கை) ஆகியவற்றை அரசியலமைப்பிற்கு முரண் என உச்ச நீதிமன்றம் ரத்து செய்தது.",
        "Option A is incorrect; Sections 2 & 3 dealt with Preamble and Directive Principles additions.", "விருப்பம் A தவறானது; பிரிவு 2 & 3 முகப்புரை மற்றும் DPSP பற்றியவை.",
        "Option B is incorrect; Sections 10 & 12 dealt with fundamental duties and executive rules.", "விருப்பம் B தவறானது; பிரிவு 10 & 12 கடமைகள் மற்றும் விதிகள் பற்றியவை.",
        "Option C is correct because Minerva Mills struck down Section 4 and Section 55 of 42nd Amendment Act 1976.", "விருப்பம் C சரியானது, ஏனெனில் மினர்வா மில்ஸ் வழக்கு 42வது திருத்தச் சட்டத்தின் பிரிவு 4 மற்றும் 55 ஐ ரத்து செய்தது.",
        "Option D is incorrect; Sections 20 & 22 dealt with state assembly terms.", "விருப்பம் D தவறானது; பிரிவு 20 & 22 சட்டமன்ற பதவி காலம் பற்றியது.",
        "Minerva Mills held that 'limited amending power is itself a basic feature of the Constitution'.",
        "வரம்பிற்குட்பட்ட திருத்த அதிகாரமே அரசியலமைப்பின் அடிப்படை அமைப்பாகும் என மினர்வா மில்ஸ் வழக்குக் கூறியது.",
        "It restored harmonious balance between Part III Fundamental Rights and Part IV DPSPs.",
        "இது பகுதி III அடிப்படை உரிமைகள் மற்றும் பகுதி IV DPSP களுக்கு இடையே இணக்கமான சமநிலையை மீட்டெடுத்தது.",
        "Remembering", "High", ["Minerva Mills Case", "Section 55", "Basic Structure"], "Part 3"
    )

    # Q040 - Correct: D
    add_q(
        "CZ_AM_EZ_040",
        "Which Constitutional Amendment Act transferred 5 subjects (including Education and Forests) from the State List to the Concurrent List?",
        "கல்வி மற்றும் காடுகள் உட்பட 5 துறைகளை மாநிலப் பட்டியலிலிருந்து பொதுப் பட்டியலுக்கு மாற்றிய அரசியலமைப்பு திருத்தச் சட்டம் எது?",
        "24th Amendment Act, 1971", "24வது திருத்தச் சட்டம், 1971",
        "36th Amendment Act, 1975", "36வது திருத்தச் சட்டம், 1975",
        "44th Amendment Act, 1978", "44வது திருத்தச் சட்டம், 1978",
        "42nd Amendment Act, 1976", "42வது திருத்தச் சட்டம், 1976",
        "D",
        "The 42nd Constitutional Amendment Act, 1976 transferred 5 subjects from State List to Concurrent List: Education, Forests, Weights & Measures, Protection of Wild Animals & Birds, and Administration of Justice.",
        "42வது அரசியலமைப்பு திருத்தச் சட்டம், 1976 மாநிலப் பட்டியலிலிருந்து 5 துறைகளைப் பொதுப் பட்டியலுக்கு மாற்றியது: கல்வி, காடுகள், எடைகள் & அளவைகள், வனவிலங்குகள் & பறவைகள் பாதுகாப்பு, மற்றும் நீதி நிர்வாகம்.",
        "Option A is incorrect; 24th Amendment affirmed amending power under Art 368.", "விருப்பம் A தவறானது; 24வது திருத்தம் திருத்த அதிகாரம் பற்றியது.",
        "Option B is incorrect; 36th Amendment made Sikkim a full state.", "விருப்பம் B தவறானது; 36வது திருத்தம் சிக்கிமை மாநிலமாக்கியது.",
        "Option C is incorrect; 44th Amendment restored 5-year assembly terms.", "விருப்பம் C தவறானது; 44வது திருத்தம் 5 ஆண்டு பதவிக் காலத்தை மீட்டெடுத்தது.",
        "Option D is correct because 42nd Amendment Act, 1976 shifted Education, Forests, etc., to Concurrent List.", "விருப்பம் D சரியானது, ஏனெனில் 42வது திருத்தச் சட்டம் 1976 கல்வி, காடுகள் உள்ளிட்ட 5 துறைகளைப் பொதுப் பட்டியலுக்கு மாற்றியது.",
        "5 subjects transferred by 42nd CA 1976: (1) Education, (2) Forests, (3) Weights and Measures, (4) Protection of Wild Animals and Birds, (5) Administration of Justice.",
        "42வது திருத்தம் 1976 ஆல் மாற்றப்பட்ட 5 துறைகள்: (1) கல்வி, (2) காடுகள், (3) எடைகள் மற்றும் அளவைகள், (4) வனவிலங்குகள் மற்றும் பறவைகள் பாதுகாப்பு, (5) நீதி நிர்வாகம்.",
        "This expanded Union Parliament's legislative power over education and environment.",
        "இது கல்வி மற்றும் சுற்றுச்சூழல் மீது நாடாளுமன்றத்தின் அதிகாரத்தை விரிவுபடுத்தியது.",
        "Remembering", "High", ["42nd Amendment", "Concurrent List", "Education"], "Part 2"
    )

    # Q041 - Correct: A
    add_q(
        "CZ_AM_EZ_041",
        "What is the maximum time limit specified under Article 368 for State Legislatures to ratify a Constitutional Amendment Bill?",
        "அரசியலமைப்பு திருத்த மசோதாவிற்கு மாநில சட்டமன்றங்கள் ஒப்புதல் அளிக்க சரத்து 368 இன் கீழ் குறிப்பிடப்பட்டுள்ள அதிகபட்ச காலக்கெடு என்ன?",
        "No time limit is specified in the Constitution", "அரசியலமைப்பில் எந்தக் காலக்கெடுவும் குறிப்பிடப்படவில்லை",
        "6 months from receipt of bill", "மசோதா பெறப்பட்ட நாளிலிருந்து 6 மாதங்கள்",
        "1 year from receipt of bill", "மசோதா பெறப்பட்ட நாளிலிருந்து 1 ஆண்டு",
        "30 days from receipt of bill", "மசோதா பெறப்பட்ட நாளிலிருந்து 30 நாட்கள்",
        "A",
        "Article 368 specifies NO time limit within which the State Legislatures must ratify or reject a Constitutional Amendment Bill submitted to them.",
        "மாநில சட்டமன்றங்களுக்கு அனுப்பப்படும் அரசியலமைப்பு திருத்த மசோதாவிற்கு அவை ஒப்புதல் அளிக்கவோ அல்லது நிராகரிக்கவோ சரத்து 368 இல் எந்தக் காலக்கெடுவும் நிர்ணயிக்கப்படவில்லை.",
        "Option A is correct because the Constitution is silent on the timeframe for state ratification under Article 368.", "விருப்பம் A சரியானது, ஏனெனில் சரத்து 368 இல் மாநில ஒப்புதலுக்கான காலக்கெடு பற்றி அரசியலமைப்பு மௌனமாக உள்ளது.",
        "Option B is incorrect; 6 months is not specified under Article 368.", "விருப்பம் B தவறானது; 6 மாத காலக்கெடு சரத்து 368 இல் இல்லை.",
        "Option C is incorrect; 1 year limit does not exist in Article 368.", "விருப்பம் C தவறானது; 1 ஆண்டு காலக்கெடு இல்லை.",
        "Option D is incorrect; 30 days is not prescribed for state ratification.", "விருப்பம் D தவறானது; 30 நாட்கள் கெடு இல்லை.",
        "The lack of a time limit for state ratification under Article 368 is often cited as a major drawback of the Indian amendment procedure.",
        "மாநில ஒப்புதலுக்குக் காலக்கெடு இல்லாதது இந்திய திருத்த நடைமுறையின் ஒரு முக்கியக் குறையாக சுட்டிக்காட்டப்படுகிறது.",
        "Once half the states ratify, the requirement is complete regardless of remaining states.",
        "பாதி மாநிலங்கள் ஒப்புதல் அளித்தவுடன் தேவைகள் பூர்த்தியாகிவிடும்.",
        "Understanding", "High", ["State Ratification Time Limit", "Article 368 Drawback"], "Part 1"
    )

    # Q042 - Correct: B
    add_q(
        "CZ_AM_EZ_042",
        "Which of the following describes the nature of the amendment procedure of the Indian Constitution?",
        "இந்திய அரசியலமைப்பின் திருத்த நடைமுறையின் தன்மையை பின்வருவனவற்றில் எது சரியாக விவரிக்கிறது?",
        "Rigid like the US Constitution", "அமெரிக்க அரசியலமைப்பு போல முற்றிலும் நெகிழ்வற்றது",
        "Synthesis of flexibility and rigidity", "நெகிழும் தன்மை மற்றும் நெகிழ்வற்ற தன்மையின் கலவை",
        "Flexible like the British Constitution", "பிரிட்டிஷ் அரசியலமைப்பு போல முற்றிலும் நெகிழும் தன்மை கொண்டது",
        "Completely non-amendable", "எந்த வகையிலும் திருத்த முடியாதது",
        "B",
        "The Indian Constitution is neither purely flexible nor purely rigid; it is a synthesis of flexibility and rigidity under Article 368.",
        "இந்திய அரசியலமைப்பு முற்றிலும் நெகிழும் தன்மையுடையதும் அல்ல, முற்றிலும் நெகிழ்வற்றதும் அல்ல; அது சரத்து 368 இன் கீழ் நெகிழும் தன்மை மற்றும் நெகிழ்வற்ற தன்மையின் கலவையாகும்.",
        "Option A is incorrect; US Constitution is extremely rigid requiring 3/4th states ratification.", "விருப்பம் A தவறானது; அமெரிக்க அரசியலமைப்பு மிகவும் நெகிழ்வற்றது.",
        "Option B is correct because Pandit Jawaharlal Nehru described it as a combination of flexibility and rigidity.", "விருப்பம் B சரியானது, ஏனெனில் பண்டிட் ஜவஹர்லால் நேரு இதை நெகிழ்வு மற்றும் நெகிழ்வின்மையின் கலவை என்றார்.",
        "Option C is incorrect; British Constitution can be amended by ordinary parliamentary laws.", "விருப்பம் C தவறானது; பிரிட்டிஷ் அரசியலமைப்பு சாதாரண சட்டங்களால் திருத்தப்படக்கூடியது.",
        "Option D is incorrect; Indian Constitution is amendable under Article 368.", "விருப்பம் D தவறானது; இந்திய அரசியலமைப்பு சரத்து 368 இன் கீழ் திருத்தப்படக்கூடியது.",
        "Some provisions can be amended by Simple Majority (flexible), while others require Special Majority or State Ratification (rigid).",
        "சில விதிகள் சாதாரண பெரும்பான்மையாலும் (நெகிழ்வு), பிற விதிகள் சிறப்பு பெரும்பான்மை அல்லது மாநில ஒப்புதலாலும் (நெகிழ்வின்மை) திருத்தப்படுகின்றன.",
        "K.C. Wheare described it as striking a good balance between flexibility and rigidity.",
        "கே.சி. வேரே இதை நெகிழ்வுத்தன்மைக்கும் நெகிழ்வின்மைக்கும் இடையிலான நல்ல சமநிலை என்று விவரித்தார்.",
        "Understanding", "High", ["Amendment Nature", "Flexibility and Rigidity"], "Part 1"
    )

    # Q043 - Correct: C
    add_q(
        "CZ_AM_EZ_043",
        "By which Constitutional Amendment Act was the term of the Lok Sabha and State Legislative Assemblies restored back to 5 years from 6 years?",
        "மக்களவை மற்றும் மாநில சட்டமன்றங்களின் பதவிக் காலத்தை 6 ஆண்டுகளிலிருந்து மீண்டும் 5 ஆண்டுகளாகக் குறைத்து சீரமைத்த அரசியலமைப்பு திருத்தச் சட்டம் எது?",
        "42nd Constitutional Amendment Act, 1976", "42வது அரசியலமைப்பு திருத்தச் சட்டம், 1976",
        "43rd Constitutional Amendment Act, 1977", "43வது அரசியலமைப்பு திருத்தச் சட்டம், 1977",
        "44th Constitutional Amendment Act, 1978", "44வது அரசியலமைப்பு திருத்தச் சட்டம், 1978",
        "45th Constitutional Amendment Act, 1980", "45வது அரசியலமைப்பு திருத்தச் சட்டம், 1980",
        "C",
        "The 44th Constitutional Amendment Act, 1978 restored the tenure of Lok Sabha and State Legislative Assemblies to 5 years (which had been extended to 6 years by 42nd Amendment Act 1976).",
        "44வது அரசியலமைப்பு திருத்தச் சட்டம், 1978 மக்களவை மற்றும் மாநில சட்டமன்றங்களின் பதவிக் காலத்தை 5 ஆண்டுகளாக மீண்டும் சீரமைத்தது (42வது திருத்தத்தால் 6 ஆண்டுகளாக உயர்த்தப்பட்டிருந்தது).",
        "Option A is incorrect; 42nd Amendment extended Lok Sabha & Assembly term to 6 years.", "விருப்பம் A தவறானது; 42வது திருத்தம் பதவிக் காலத்தை 6 ஆண்டுகளாக உயர்த்தியது.",
        "Option B is incorrect; 43rd Amendment restored judicial review scope of High Courts & Supreme Court.", "விருப்பம் B தவறானது; 43வது திருத்தம் நீதிமன்ற அதிகாரங்களை சீரமைத்தது.",
        "Option C is correct because 44th Amendment Act, 1978 under Janata Government restored 5-year tenure under Articles 83 and 172.", "விருப்பம் C சரியானது, ஏனெனில் 44வது திருத்தச் சட்டம் 1978 5 ஆண்டு பதவிக் காலத்தை மீட்டெடுத்தது.",
        "Option D is incorrect; 45th Amendment extended SC/ST reservation in Assemblies.", "விருப்பம் D தவறானது; 45வது திருத்தம் எஸ்சி/எஸ்டி இடஒதுக்கீட்டை நீட்டித்தது.",
        "44th Amendment Act, 1978 was brought by Janata Party Government to undo anti-democratic provisions of 42nd CA.",
        "44வது திருத்தச் சட்டம் 1978, 42வது திருத்தத்தின் ஜனநாயகத்திற்கு எதிரான விதிகளை ரத்து செய்ய ஜனதா கட்சி அரசால் கொண்டுவரப்பட்டது.",
        "It also replaced 'internal disturbance' with 'armed rebellion' in Article 352.",
        "இது சரத்து 352 இல் 'உள்நாட்டு அமைதியின்மை' என்ற சொல்லுக்குப் பதிலாக 'ஆயுதமேந்திய கிளர்ச்சி' என மாற்றியது.",
        "Remembering", "High", ["44th Amendment", "Assembly Tenure 5 Years"], "Part 2"
    )

    # Q044 - Correct: D
    add_q(
        "CZ_AM_EZ_044",
        "Which Constitutional Amendment Act replaced the phrase 'internal disturbance' with 'armed rebellion' for declaring National Emergency under Article 352?",
        "சரத்து 352 இன் கீழ் தேசிய அவசரநிலையை அறிவிப்பதற்கான 'உள்நாட்டு அமைதியின்மை' என்ற சொல்லுக்குப் பதிலாக 'ஆயுதமேந்திய கிளர்ச்சி' என்ற சொல்லை மாற்றிய அரசியலமைப்பு திருத்தச் சட்டம் எது?",
        "38th Amendment Act, 1975", "38வது திருத்தச் சட்டம், 1975",
        "42nd Amendment Act, 1976", "42வது திருத்தச் சட்டம், 1976",
        "43rd Amendment Act, 1977", "43வது திருத்தச் சட்டம், 1977",
        "44th Amendment Act, 1978", "44வது திருத்தச் சட்டம், 1978",
        "D",
        "The 44th Constitutional Amendment Act, 1978 substituted 'armed rebellion' for 'internal disturbance' in Article 352 to prevent misuse of National Emergency provisions.",
        "44வது அரசியலமைப்பு திருத்தச் சட்டம், 1978 சரத்து 352 இல் தேசிய அவசரநிலை தவறாகப் பயன்படுத்தப்படுவதைத் தடுக்க 'உள்நாட்டு அமைதியின்மை' என்பதற்குப் பதிலாக 'ஆயுதமேந்திய கிளர்ச்சி' என மாற்றியது.",
        "Option A is incorrect; 38th Amendment made Emergency declaration non-justiciable.", "விருப்பம் A தவறானது; 38வது திருத்தம் அவசரநிலை அறிவிப்பை நீதிமன்ற ஆய்வுக்கு அப்பாற்பட்டதாக்கியது.",
        "Option B is incorrect; 42nd Amendment permitted Emergency in part of India.", "விருப்பம் B தவறானது; 42வது திருத்தம் இந்தியாவின் ஒரு பகுதிக்கு அவசரநிலையை அனுமதித்தது.",
        "Option C is incorrect; 43rd Amendment repealed anti-national activity provisions.", "விருப்பம் C தவறானது; 43வது திருத்தம் தேசவிரோத செயல்பாட்டு விதிகளை நீக்கியது.",
        "Option D is correct because 44th Amendment Act, 1978 substituted 'armed rebellion' and mandated Cabinet's written communication under Article 352(3).", "விருப்பம் D சரியானது, ஏனெனில் 44வது திருத்தச் சட்டம் 1978 'ஆயுதமேந்திய கிளர்ச்சி' என்றும் அமைச்சரவை எழுத்துப்பூர்வ ஆலோசனை என்றும் மாற்றியது.",
        "44th CA also mandated that National Emergency can be proclaimed only on the WRITTEN recommendation of the Cabinet.",
        "44வது திருத்தம் அமைச்சரவையின் எழுத்துப்பூர்வப் பரிந்துரையின் பேரில் மட்டுமே தேசிய அவசரநிலையைப் பிரகடனம் செய்ய முடியும் எனக் கட்டாயமாக்கியது.",
        "It also ensured that Articles 20 and 21 cannot be suspended during National Emergency.",
        "தேசிய அவசரநிலையின் போது சரத்துகள் 20 மற்றும் 21 ஐ இடைநிறுத்தம் செய்ய முடியாது என்பதையும் இது உறுதிசெய்தது.",
        "Remembering", "High", ["44th Amendment", "Armed Rebellion", "Article 352"], "Part 2"
    )

    # Q045 - Correct: A
    add_q(
        "CZ_AM_EZ_045",
        "Which Constitutional Amendment Act explicitly provided that Fundamental Rights under Articles 20 and 21 CANNOT be suspended even during a National Emergency?",
        "தேசிய அவசரநிலையின் போது கூட சரத்துகள் 20 மற்றும் 21 இன் கீழான அடிப்படை உரிமைகளை இடைநிறுத்தம் செய்ய முடியாது என்று தெளிவாகக் கூறிய அரசியலமைப்பு திருத்தச் சட்டம் எது?",
        "44th Constitutional Amendment Act, 1978", "44வது அரசியலமைப்பு திருத்தச் சட்டம், 1978",
        "42nd Constitutional Amendment Act, 1976", "42வது அரசியலமைப்பு திருத்தச் சட்டம், 1976",
        "59th Constitutional Amendment Act, 1988", "59வது அரசியலமைப்பு திருத்தச் சட்டம், 1988",
        "24th Constitutional Amendment Act, 1971", "24வது அரசியலமைப்பு திருத்தச் சட்டம், 1971",
        "A",
        "The 44th Constitutional Amendment Act, 1978 amended Article 359 to provide that right to protection in respect of conviction for offences (Art 20) and protection of life & personal liberty (Art 21) cannot be suspended during Emergency.",
        "44வது அரசியலமைப்பு திருத்தச் சட்டம், 1978 சரத்து 359 ஐத் திருத்தி, குற்றங்களுக்கு தண்டனை அளிப்பதிலிருந்து பாதுகாப்பு (சரத்து 20) மற்றும் வாழ்வு & தனிநபர் சுதந்திரப் பாதுகாப்பு (சரத்து 21) ஆகியவற்றை அவசரநிலையின் போது இடைநிறுத்தம் செய்ய முடியாது என மாற்றியது.",
        "Option A is correct because 44th Amendment Act, 1978 protected Articles 20 and 21 from suspension under Article 359.", "விருப்பம் A சரியானது, ஏனெனில் 44வது திருத்தச் சட்டம் 1978 சரத்துகள் 20 மற்றும் 21 ஐ இடைநிறுத்தத்திலிருந்து பாதுகாத்தது.",
        "Option B is incorrect; 42nd Amendment did not protect Articles 20 and 21.", "விருப்பம் B தவறானது; 42வது திருத்தம் சரத்து 20 மற்றும் 21 ஐப் பாதுகாக்கவில்லை.",
        "Option C is incorrect; 59th Amendment provided emergency powers in Punjab.", "விருப்பம் C தவறானது; 59வது திருத்தம் பஞ்சாப்பில் அவசரநிலை அதிகாரம் பற்றியது.",
        "Option D is incorrect; 24th Amendment related to Art 368 amending procedure.", "விருப்பம் D தவறானது; 24வது திருத்தம் சரத்து 368 திருத்த நடைமுறை பற்றியது.",
        "Article 20 (protection against self-incrimination & double jeopardy) and Article 21 (right to life and liberty) remain active even during Emergency.",
        "அவசரநிலையின் போது கூட சரத்து 20 (தற்காப்பு தற்காப்பு உரிமை) மற்றும் சரத்து 21 (வாழும் உரிமை) செயல்பாட்டிலேயே இருக்கும்.",
        "This overrode the controversial ADM Jabalpur (Habeas Corpus) case judgment of 1976.",
        "இது 1976 இன் சர்ச்சைக்குரிய ஏடிஎம் ஜபல்பூர் (ஆட்கொணர்வு) வழக்குத் தீர்ப்பை ரத்து செய்தது.",
        "Remembering", "High", ["44th Amendment", "Articles 20 and 21", "Emergency Non-suspension"], "Part 2"
    )

    # Q046 - Correct: B
    add_q(
        "CZ_AM_EZ_046",
        "By which Constitutional Amendment Act was Article 15(4) inserted empowering the State to make special provisions for the advancement of Socially and Educationally Backward Classes (SEBCs), SCs, and STs?",
        "சமூக மற்றும் கல்வியில் பின்தங்கிய வகுப்பினர் (SEBCs), ஆதிதிராவிடர் மற்றும் பழங்குடியினரின் முன்னேற்றத்திற்காக சிறப்பு விதிகளை உருவாக்க அரசுக்கு அதிகாரமளிக்கும் சரத்து 15(4) எந்த அரசியலமைப்பு திருத்தச் சட்டத்தின் மூலம் சேர்க்கப்பட்டது?",
        "7th Constitutional Amendment Act, 1956", "7வது அரசியலமைப்பு திருத்தச் சட்டம், 1956",
        "1st Constitutional Amendment Act, 1951", "1வது அரசியலமைப்பு திருத்தச் சட்டம், 1951",
        "42nd Constitutional Amendment Act, 1976", "42வது அரசியலமைப்பு திருத்தச் சட்டம், 1976",
        "93rd Constitutional Amendment Act, 2005", "93வது அரசியலமைப்பு திருத்தச் சட்டம், 2005",
        "B",
        "The 1st Constitutional Amendment Act, 1951 inserted Article 15(4) following the Supreme Court judgment in State of Madras v. Champakam Dorairajan (1951).",
        "செண்பகம் துரைராஜன் எதிர் மதராஸ் மாகாணம் (1951) வழக்கில் உச்ச நீதிமன்றத் தீர்ப்பைத் தொடர்ந்து 1வது அரசியலமைப்பு திருத்தச் சட்டம், 1951 சரத்து 15(4) ஐச் சேர்த்தது.",
        "Option A is incorrect; 7th Amendment dealt with state reorganization.", "விருப்பம் A தவறானது; 7வது திருத்தம் மாநில மறுசீரமைப்பு பற்றியது.",
        "Option B is correct because 1st Amendment Act, 1951 inserted Article 15(4) to enable affirmative action in educational institutions.", "விருப்பம் B சரியானது, ஏனெனில் 1வது திருத்தச் சட்டம் 1951 கல்வி நிறுவனங்களில் சமூக இடஒதுக்கீடு வழங்க சரத்து 15(4) ஐச் சேர்த்தது.",
        "Option C is incorrect; 42nd Amendment did not insert Article 15(4).", "விருப்பம் C தவறானது; 42வது திருத்தம் சரத்து 15(4) ஐச் சேர்க்கவில்லை.",
        "Option D is incorrect; 93rd Amendment (2005) inserted Article 15(5) for OBC/SC/ST reservation in private educational institutions.", "விருப்பம் D தவறானது; 93வது திருத்தம் 2005 இல் சரத்து 15(5) ஐச் சேர்த்தது.",
        "Champakam Dorairajan case (1951) led directly to the enactment of the 1st Constitutional Amendment Act, 1951.",
        "செண்பகம் துரைராஜன் வழக்கு (1951) நேரடியாக 1வது அரசியலமைப்பு திருத்தச் சட்டம் 1951 உருவாகக் காரணமானது.",
        "Article 15(4) forms the constitutional foundation for educational reservations in India.",
        "சரத்து 15(4) இந்தியாவில் கல்வி இடஒதுக்கீடுகளுக்கான அரசியலமைப்பு அடித்தளமாகும்.",
        "Remembering", "High", ["1st Amendment", "Article 15(4)", "Champakam Dorairajan"], "Part 2"
    )

    # Q047 - Correct: C
    add_q(
        "CZ_AM_EZ_047",
        "Which Constitutional Amendment Act inserted Article 15(5) providing for OBC/SC/ST reservation in private unaided educational institutions (excluding minority institutions)?",
        "சிறுபான்மை நிறுவனங்கள் தவிர்ந்த தனியார் சுயநிதி கல்வி நிறுவனங்களில் OBC/SC/ST பிரிவினருக்கு இடஒதுக்கீடு வழங்க சரத்து 15(5) ஐச் சேர்த்த அரசியலமைப்பு திருத்தச் சட்டம் எது?",
        "86th Amendment Act, 2002", "86வது திருத்தச் சட்டம், 2002",
        "91st Amendment Act, 2003", "91வது திருத்தச் சட்டம், 2003",
        "93rd Amendment Act, 2005", "93வது திருத்தச் சட்டம், 2005",
        "103rd Amendment Act, 2019", "103வது திருத்தச் சட்டம், 2019",
        "C",
        "The 93rd Constitutional Amendment Act, 2005 inserted Article 15(5) permitting state reservations in admission to educational institutions, including private unaided institutions, except minority educational institutions under Art 30(1).",
        "93வது அரசியலமைப்பு திருத்தச் சட்டம், 2005 சரத்து 15(5) ஐச் சேர்த்து சிறுபான்மை நிறுவனங்கள் தவிர்ந்த தனியார் சுயநிதி கல்வி நிறுவனங்கள் உட்பட உயர்கல்வி நிறுவனங்களில் OBC/SC/ST இடஒதுக்கீட்டிற்கு வழிவகுத்தது.",
        "Option A is incorrect; 86th Amendment related to RTE Article 21A.", "விருப்பம் A தவறானது; 86வது திருத்தம் கல்வி உரிமை சரத்து 21A பற்றியது.",
        "Option B is incorrect; 91st Amendment related to Council of Ministers 15% cap.", "விருப்பம் B தவறானது; 91வது திருத்தம் அமைச்சரவை 15% வரம்பு பற்றியது.",
        "Option C is correct because 93rd Amendment Act, 2005 inserted Article 15(5) for Central Educational Institutions reservation.", "விருப்பம் C சரியானது, ஏனெனில் 93வது திருத்தச் சட்டம் 2005 சரத்து 15(5) ஐச் சேர்த்தது.",
        "Option D is incorrect; 103rd Amendment inserted Article 15(6) for EWS reservation.", "விருப்பம் D தவறானது; 103வது திருத்தம் EWS இடஒதுக்கீட்டிற்காக சரத்து 15(6) ஐச் சேர்த்தது.",
        "Supreme Court upheld 93rd Amendment in Ashok Kumar Thakur v. Union of India (2008).",
        "அசோக் குமார் தாக்குர் எதிர் மத்திய அரசு (2008) வழக்கில் உச்ச நீதிமன்றம் 93வது திருத்தத்தின் செல்லுபடியாகும் தன்மையை உறுதி செய்தது.",
        "It led to Central Educational Institutions (Reservation in Admission) Act, 2006 (27% OBC quota).",
        "இது மத்திய கல்வி நிறுவனங்கள் (சேர்க்கையில் இடஒதுக்கீடு) சட்டம் 2006 (27% OBC quota) உருவாக வழிவகுத்தது.",
        "Remembering", "High", ["93rd Amendment", "Article 15(5)", "OBC Reservation"], "Part 2"
    )

    # Q048 - Correct: D
    add_q(
        "CZ_AM_EZ_048",
        "Which Constitutional Amendment Act inserted Article 31C giving immunity to laws implementing Directive Principles in Article 39(b) and 39(c) over Articles 14 and 19?",
        "சரத்துகள் 14 மற்றும் 19 ஐ விட சரத்து 39(b) மற்றும் 39(c) இல் உள்ள அரசு நெறிமுறைக் கோட்பாடுகளைச் செயல்படுத்தும் சட்டங்களுக்குப் பாதுகாப்பு அளிக்கும் சரத்து 31C ஐச் சேர்த்த அரசியலமைப்பு திருத்தச் சட்டம் எது?",
        "24th Amendment Act, 1971", "24வது திருத்தச் சட்டம், 1971",
        "42nd Amendment Act, 1976", "42வது திருத்தச் சட்டம், 1976",
        "44th Amendment Act, 1978", "44வது திருத்தச் சட்டம், 1978",
        "25th Amendment Act, 1971", "25வது திருத்தச் சட்டம், 1971",
        "D",
        "The 25th Constitutional Amendment Act, 1971 inserted Article 31C stating that laws made to give effect to Directive Principles in Article 39(b) and (c) cannot be declared void for violating Articles 14 or 19.",
        "25வது அரசியலமைப்பு திருத்தச் சட்டம், 1971 சரத்து 31C ஐச் சேர்த்து, சரத்து 39(b) மற்றும் (c) இல் உள்ள நெறிமுறைக் கோட்பாடுகளைச் செயல்படுத்த இயற்றப்படும் சட்டங்கள் சரத்து 14 அல்லது 19 ஐ மீறுவதாகக் கூறி செல்லாது என அறிவிக்க முடியாது என மாற்றியது.",
        "Option A is incorrect; 24th Amendment dealt with Art 368 procedural clarifying clause.", "விருப்பம் A தவறானது; 24வது திருத்தம் சரத்து 368 திருத்த நடைமுறை பற்றியது.",
        "Option B is incorrect; 42nd Amendment expanded Art 31C to ALL Directive Principles (later invalidated in Minerva Mills).", "விருப்பம் B தவறானது; 42வது திருத்தம் அனைத்து நெறிமுறைக் கோட்பாடுகளுக்கும் விரிவாக்கியது (மினர்வா மில்ஸ் வழக்கில் ரத்து செய்யப்பட்டது).",
        "Option C is incorrect; 44th Amendment deleted Right to Property.", "விருப்பம் C தவறானது; 44வது திருத்தம் சொத்துரிமையை நீக்கியது.",
        "Option D is correct because 25th Amendment Act, 1971 inserted Article 31C into the Constitution.", "விருப்பம் D சரியானது, ஏனெனில் 25வது திருத்தச் சட்டம் 1971 சரத்து 31C ஐ அரசியலமைப்பில் சேர்த்தது.",
        "Kesavananda Bharati case (1973) upheld the 1st part of Article 31C (giving precedence to Art 39(b)&(c)) but struck down the 2nd part which ousted judicial review.",
        "கேசவாநந்த பாரதி வழக்கு (1973) சரத்து 31C இன் 1வது பகுதியை (சரத்து 39(b)&(c) முன்னுரிமை) உறுதி செய்தது, ஆனால் நீதிமன்ற ஆய்வைத் தடுக்கும் 2வது பகுதியை ரத்து செய்தது.",
        "Famous rule: 'Where Article 31C comes in, Article 14 goes out'.",
        "புகழ்பெற்ற கூற்று: 'சரத்து 31C நுழையும் போது, சரத்து 14 வெளியேறுகிறது'.",
        "Remembering", "High", ["25th Amendment", "Article 31C", "DPSP Primacy"], "Part 2"
    )

    # Q049 - Correct: A
    add_q(
        "CZ_AM_EZ_049",
        "Which Constitutional Amendment Act increased the strength of Lok Sabha from 525 to 545 members?",
        "மக்களவையின் மொத்த உறுப்பினர்களின் எண்ணிக்கையை 525 லிருந்து 545 ஆக உயர்த்திய அரசியலமைப்பு திருத்தச் சட்டம் எது?",
        "31st Constitutional Amendment Act, 1973", "31வது அரசியலமைப்பு திருத்தச் சட்டம், 1973",
        "42nd Constitutional Amendment Act, 1976", "42வது அரசியலமைப்பு திருத்தச் சட்டம், 1976",
        "84th Constitutional Amendment Act, 2001", "84வது அரசியலமைப்பு திருத்தச் சட்டம், 2001",
        "87th Constitutional Amendment Act, 2003", "87வது அரசியலமைப்பு திருத்தச் சட்டம், 2003",
        "A",
        "The 31st Constitutional Amendment Act, 1973 increased the maximum elective strength of Lok Sabha from 525 to 545 members (reducing UT representation from 25 to 20 while increasing state representation from 500 to 525).",
        "31வது அரசியலமைப்பு திருத்தச் சட்டம், 1973 மக்களவை உறுப்பினர்களின் அதிகபட்ச எண்ணிக்கையை 525 லிருந்து 545 ஆக உயர்த்தியது.",
        "Option A is correct because 31st Amendment Act, 1973 amended Article 81 raising Lok Sabha seats to 545.", "விருப்பம் A சரியானது, ஏனெனில் 31வது திருத்தச் சட்டம் 1973 சரத்து 81 ஐத் திருத்தி மக்களவை இடங்களை 545 ஆக உயர்த்தியது.",
        "Option B is incorrect; 42nd Amendment froze seat allocation based on 1971 Census till 2000.", "விருப்பம் B தவறானது; 42வது திருத்தம் 1971 மக்கள் தொகை அடிப்படையில் இடங்களை 2000 வரை முடக்கியது.",
        "Option C is incorrect; 84th Amendment extended freeze on seat allocation till 2026.", "விருப்பம் C தவறானது; 84வது திருத்தம் 2026 வரை இட ஒதுக்கீடு முடக்கத்தை நீட்டித்தது.",
        "Option D is incorrect; 87th Amendment permitted delimitation based on 2001 Census without changing total seats.", "விருப்பம் D தவறானது; 87வது திருத்தம் மொத்த இடங்களை மாற்றாமல் 2001 மக்கள் தொகை அடிப்படையில் தொகுதி சீரமைப்பு செய்ய அனுமதித்தது.",
        "The 1971 Census formed the basis of the 31st Amendment Act 1973 expansion.",
        "1971 மக்கள் தொகை கணக்கெடுப்பு 31வது திருத்தச் சட்டம் 1973 இன் தொகுதி விரிவாக்கத்திற்கு அடிப்படையாக அமைந்தது.",
        "Lok Sabha elective strength was set at 543 following 104th CA abolishing Anglo-Indian nomination.",
        "104வது திருத்தத்தின் படி ஆங்கிலோ-இந்தியர் நியமனம் ரத்து செய்யப்பட்ட பின் தற்போதைய தேர்வு செய்யப்படும் உறுப்பினர்கள் எண்ணிக்கை 543 ஆகும்.",
        "Remembering", "High", ["31st Amendment", "Lok Sabha Seats 545"], "Part 2"
    )

    # Q050 - Correct: B
    add_q(
        "CZ_AM_EZ_050",
        "Which Constitutional Amendment Act froze the allocation of seats in Lok Sabha and State Legislative Assemblies till the year 2026 based on the 1991 Census?",
        "1991 மக்கள் தொகை கணக்கெடுப்பின் அடிப்படையில் மக்களவை மற்றும் மாநில சட்டமன்றங்களின் தொகுதி ஒதுக்கீட்டை 2026 ஆம் ஆண்டு வரை முடக்கிய அரசியலமைப்பு திருத்தச் சட்டம் எது?",
        "42nd Constitutional Amendment Act, 1976", "42வது அரசியலமைப்பு திருத்தச் சட்டம், 1976",
        "84th Constitutional Amendment Act, 2001", "84வது அரசியலமைப்பு திருத்தச் சட்டம், 2001",
        "87th Constitutional Amendment Act, 2003", "87வது அரசியலமைப்பு திருத்தச் சட்டம், 2003",
        "91st Constitutional Amendment Act, 2003", "91வது அரசியலமைப்பு திருத்தச் சட்டம், 2003",
        "B",
        "The 84th Constitutional Amendment Act, 2001 extended the freeze on total seats in Lok Sabha and State Assemblies till 2026 and permitted internal boundary delimitation based on 1991 Census (later changed to 2001 Census by 87th CA).",
        "84வது அரசியலமைப்பு திருத்தச் சட்டம், 2001 மக்களவை மற்றும் சட்டமன்றங்களின் மொத்த இடங்கள் ஒதுக்கீடு முடக்கத்தை 2026 வரை நீட்டித்தது.",
        "Option A is incorrect; 42nd Amendment froze seat allocation till the year 2000 based on 1971 Census.", "விருப்பம் A தவறானது; 42வது திருத்தம் 1971 கணக்கெடுப்பு அடிப்படையில் 2000 வரை முடக்கியது.",
        "Option B is correct because 84th Amendment Act, 2001 extended seat freeze till 2026.", "விருப்பம் B சரியானது, ஏனெனில் 84வது திருத்தச் சட்டம் 2001 தொகுதி இட முடக்கத்தை 2026 வரை நீட்டித்தது.",
        "Option C is incorrect; 87th Amendment amended 84th CA to use 2001 Census for internal constituency boundary rationalisation.", "விருப்பம் C தவறானது; 87வது திருத்தம் 2001 மக்கள் தொகை கணக்கெடுப்பை உள்கட்டமைப்பு தொகுதி மறுவரையறைக்கு பயன்படுத்த அனுமதித்தது.",
        "Option D is incorrect; 91st Amendment capped Council of Ministers size at 15%.", "விருப்ப点 D தவறானது; 91வது திருத்தம் அமைச்சரவை 15% வரம்பு பற்றியது.",
        "The 84th CA was enacted to encourage population stabilization measures across states.",
        "மாநிலங்கள் மக்கள் தொகை கட்டுப்பாட்டு நடவடிக்கைகளை ஊக்குவிக்க 84வது திருத்தம் இயற்றப்பட்டது.",
        "Next fresh delimitation of parliamentary and assembly constituencies can take place after the first census after 2026.",
        "அடுத்த தொகுதி மறுவரையறை 2026 க்குப் பிறகான முதல் மக்கள் தொகை கணக்கெடுப்பிற்கு பிறகே நடைபெறும்.",
        "Remembering", "High", ["84th Amendment", "Seat Freeze 2026"], "Part 2"
    )

    return questions

if __name__ == "__main__":
    ez_qs = create_easy_questions()
    os.makedirs("data/questions/polity", exist_ok=True)
    out_path = "data/questions/polity/constitutional_amendments_easy.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(ez_qs, f, ensure_ascii=False, indent=2)
    
    from collections import Counter
    counts = Counter(q["correct_answer"] for q in ez_qs)
    print(f"Easy set complete. Total: {len(ez_qs)}")
    print(f"Answer balance: {dict(counts)}")
