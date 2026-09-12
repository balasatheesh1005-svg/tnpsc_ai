# -*- coding: utf-8 -*-
"""
Generator for Emergency Provisions Match the Following MCQs (25 questions: EP_MF_001 to EP_MF_025)
Keys: A: 6, B: 7, C: 6, D: 6 (Total: 25)
"""

import json
from ep_mcq_helper import make_ep_q

PREFIX = "EP_MF_"
DIFF = "Medium"
QTYPE = "Match the Following"

def make_mf_q(num, subtopic, title_en, title_ta,
              l1_items_en, l1_items_ta,
              l2_items_en, l2_items_ta,
              opt_codes, key,
              exp_en, exp_ta,
              why_a_en, why_a_ta,
              why_b_en, why_b_ta,
              why_c_en, why_c_ta,
              why_d_en, why_d_ta,
              tip_en, tip_ta,
              fact_en, fact_ta):
    
    stem_en = (
        f"Match List-I ({title_en}) with List-II and select the correct answer using the codes given below:\n"
        f"List-I:\n"
        f"a. {l1_items_en[0]}\n"
        f"b. {l1_items_en[1]}\n"
        f"c. {l1_items_en[2]}\n"
        f"d. {l1_items_en[3]}\n"
        f"List-II:\n"
        f"1. {l2_items_en[0]}\n"
        f"2. {l2_items_en[1]}\n"
        f"3. {l2_items_en[2]}\n"
        f"4. {l2_items_en[3]}\n"
        f"Codes:"
    )
    
    stem_ta = (
        f"பட்டியல்-I ({title_ta}) மற்றும் பட்டியல்-II ஆகியவற்றை பொருத்தி, கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான விடையைத் தேர்ந்தெடுக்கவும்:\n"
        f"பட்டியல்-I:\n"
        f"a. {l1_items_ta[0]}\n"
        f"b. {l1_items_ta[1]}\n"
        f"c. {l1_items_ta[2]}\n"
        f"d. {l1_items_ta[3]}\n"
        f"பட்டியல்-II:\n"
        f"1. {l2_items_ta[0]}\n"
        f"2. {l2_items_ta[1]}\n"
        f"3. {l2_items_ta[2]}\n"
        f"4. {l2_items_ta[3]}\n"
        f"குறியீடுகள்:"
    )
    
    return make_ep_q(
        PREFIX, num, DIFF, QTYPE, subtopic,
        stem_en, stem_ta,
        opt_codes[0], opt_codes[0],
        opt_codes[1], opt_codes[1],
        opt_codes[2], opt_codes[2],
        opt_codes[3], opt_codes[3],
        key,
        exp_en, exp_ta,
        why_a_en, why_a_ta,
        why_b_en, why_b_ta,
        why_c_en, why_c_ta,
        why_d_en, why_d_ta,
        tip_en, tip_ta,
        fact_en, fact_ta
    )

def get_match_questions():
    qs = []

    # 001 - Key A: a-3, b-4, c-1, d-2
    qs.append(make_mf_q(
        1, "Emergency Articles in Part XVIII",
        "Articles of Part XVIII", "பகுதி XVIII-ன் சரத்துகள்",
        ["Article 352", "Article 356", "Article 360", "Article 355"],
        ["சரத்து 352", "சரத்து 356", "சரத்து 360", "சரத்து 355"],
        ["Financial Emergency", "Duty of Union to protect States", "National Emergency", "President's Rule (Failure of constitutional machinery)"],
        ["நிதி அவசரநிலை", "மாநிலங்களைப் பாதுகாக்கும் மத்திய அரசின் கடமை", "தேசிய அவசரநிலை", "குடியரசுத் தலைவர் ஆட்சி (அரசியலமைப்பு இயந்திரத்தின் தோல்வி)"],
        ["a-3, b-4, c-1, d-2", "a-3, b-1, c-4, d-2", "a-4, b-3, c-1, d-2", "a-2, b-4, c-3, d-1"],
        "A",
        "Article 352 deals with National Emergency (3); Article 356 deals with President's Rule (4); Article 360 deals with Financial Emergency (1); Article 355 deals with the duty of the Union to protect States (2).",
        "சரத்து 352 தேசிய அவசரநிலை (3); சரத்து 356 குடியரசுத் தலைவர் ஆட்சி (4); சரத்து 360 நிதி அவசரநிலை (1); சரத்து 355 மாநிலங்களைப் பாதுகாக்கும் மத்திய அரசின் கடமை (2) ஆகும்.",
        "Option A is correct; accurately pairs each article with its constitutional mandate.", "விருப்பம் A சரியானது; ஒவ்வொரு சரத்தையும் அதன் அரசியலமைப்பு ஆணையுடன் துல்லியமாகப் பொருத்துகிறது.",
        "Option B mismatches Article 356 with Financial Emergency.", "விருப்பம் B சரத்து 356-ஐ நிதி அவசரநிலையுடன் தவறாகப் பொருத்துகிறது.",
        "Option C reverses Articles 352 and 356.", "விருப்பம் C சரத்துகள் 352 மற்றும் 356-ஐத் தலைகீழாக மாற்றுகிறது.",
        "Option D incorrectly matches Article 352 with duty to protect states.", "விருப்பம் D சரத்து 352-ஐ மாநிலங்களைப் பாதுகாக்கும் கடமையுடன் தவறாகப் பொருத்துகிறது.",
        "Foundational Grid: 352 = National, 355 = Duty of Union, 356 = State/President's Rule, 360 = Financial.",
        "அடிப்படை கட்டமைப்பு: 352 = தேசியம், 355 = மத்திய அரசின் கடமை, 356 = குடியரசுத் தலைவர் ஆட்சி, 360 = நிதி.",
        "Articles 352 to 360 constitute the complete Part XVIII of the Constitution.",
        "சரத்துகள் 352 முதல் 360 வரை அரசியலமைப்பின் முழுமையான பகுதி XVIII-ஐ உருவாக்குகின்றன."
    ))

    # 002 - Key B: a-2, b-3, c-1, d-4
    qs.append(make_mf_q(
        2, "Landmark Emergency Cases",
        "Landmark Cases", "மைல்கல் வழக்குகள்",
        ["Minerva Mills Case (1980)", "S.R. Bommai Case (1994)", "ADM Jabalpur Case (1976)", "Rameshwar Prasad Case (2006)"],
        ["மினர்வா மில்ஸ் வழக்கு (1980)", "எஸ்.ஆர். பொம்மை வழக்கு (1994)", "ஏ.டி.எம். ஜபல்பூர் வழக்கு (1976)", "ராமேஷ்வர் பிரசாத் வழக்கு (2006)"],
        ["Habeas Corpus case / Right to life suspension upheld (later overruled)", "National Emergency subject to judicial review for mala fides", "Secularism basic structure & guidelines on Article 356", "Dissolution of Bihar Assembly declared unconstitutional"],
        ["ஆட்கொணர்வு வழக்கு / வாழ்வுரிமை இடைநிறுத்தம் உறுதி செய்யப்பட்டது (பின்னர் ரத்து செய்யப்பட்டது)", "தேசிய அவசரநிலை தவறான உள்நோக்கத்திற்காக நீதி மறுஆய்வுக்கு உட்பட்டது", "மதச்சார்பின்மை அடிப்படைக் கட்டமைப்பு மற்றும் சரத்து 356 வழிகாட்டுதல்கள்", "பீகார் சட்டமன்றக் கலைப்பு அரசியலமைப்புக்கு முரணானது என அறிவிக்கப்பட்டது"],
        ["a-1, b-3, c-2, d-4", "a-2, b-3, c-1, d-4", "a-3, b-2, c-4, d-1", "a-4, b-1, c-2, d-3"],
        "B",
        "Minerva Mills (1980) held National Emergency subject to judicial review (2); S.R. Bommai (1994) established guidelines on Art 356 and secularism (3); ADM Jabalpur (1976) was the Habeas Corpus case (1); Rameshwar Prasad (2006) invalidated Bihar Assembly dissolution (4).",
        "மினர்வா மில்ஸ் (1980) தேசிய அவசரநிலையை நீதி மறுஆய்வுக்கு உட்படுத்தியது (2); எஸ்.ஆர். பொம்மை (1994) சரத்து 356 வழிகாட்டுதல்களை அமைத்தது (3); ஏ.டி.எம். ஜபல்பூர் (1976) ஆட்கொணர்வு வழக்காகும் (1); ராமேஷ்வர் பிரசாத் (2006) பீகார் சட்டமன்றக் கலைப்பைச் செல்லாது என்றது (4).",
        "Option A confuses Minerva Mills with ADM Jabalpur.", "விருப்பம் A மினர்வா மில்ஸ் வழக்கை ஏ.டி.எம். ஜபல்பூருடன் குழப்புகிறது.",
        "Option B is correct; correctly maps all 4 historic judgments.", "விருப்பம் B சரியானது; அனைத்து 4 வரலாற்றுத் தீர்ப்புகளையும் சரியாகப் பொருத்துகிறது.",
        "Option C reverses Bommai and Minerva Mills.", "விருப்பம் C பொம்மை மற்றும் மினர்வா மில்ஸ் வழக்குகளை மாற்றுகிறது.",
        "Option D incorrectly pairs Rameshwar Prasad with Habeas Corpus.", "விருப்பம் D ராமேஷ்வர் பிரசாத் வழக்கை ஆட்கொணர்வு வழக்குடன் தவறாகப் பொருத்துகிறது.",
        "TNPSC Landmark Series: ADM Jabalpur = 1976; Minerva Mills = 1980; S.R. Bommai = 1994; Rameshwar Prasad = 2006.",
        "TNPSC மைல்கல் தொடர்: ஏ.டி.எம் ஜபல்பூர் = 1976; மினர்வா மில்ஸ் = 1980; எஸ்.ஆர். பொம்மை = 1994; ராமேஷ்வர் பிரசாத் = 2006.",
        "Justice H.R. Khanna's lone dissent in ADM Jabalpur is celebrated as a heroic defense of personal liberty.",
        "ஏ.டி.எம். ஜபல்பூர் வழக்கில் நீதிபதி எச்.ஆர். கண்ணாவின் தனித்த மாறுபட்ட தீர்ப்பு தனிநபர் சுதந்திரத்தின் வீரமிக்கப் பாதுகாப்பாகப் போற்றப்படுகிறது."
    ))

    # 003 - Key C: a-2, b-3, c-4, d-1
    qs.append(make_mf_q(
        3, "Constitutional Amendments and Emergency",
        "Constitutional Amendments", "அரசியலமைப்பு திருத்தச் சட்டங்கள்",
        ["38th Amendment (1975)", "42nd Amendment (1976)", "44th Amendment (1978)", "59th Amendment (1988)"],
        ["38-வது திருத்தம் (1975)", "42-வது திருத்தம் (1976)", "44-வது திருத்தம் (1978)", "59-வது திருத்தம் (1988)"],
        ["Emergency in Punjab on ground of internal disturbance", "President's satisfaction made non-justiciable", "Emergency made applicable to part of India", "Substituted 'armed rebellion' and protected Articles 20 & 21"],
        ["உள்நாட்டு அமைதியின்மை அடிப்படையில் பஞ்சாபில் அவசரநிலை", "குடியரசுத் தலைவரின் திருப்தி நீதி விசாரணைக்கு அப்பாற்பட்டதாக மாற்றப்பட்டது", "இந்தியாவின் ஒரு பகுதிக்கு மட்டும் அவசரநிலை பொருந்தும் வசதி", "'ஆயுதமேந்திய கிளர்ச்சி' என மாற்றி சரத்துகள் 20 மற்றும் 21-ஐப் பாதுகாத்தது"],
        ["a-1, b-2, c-3, d-4", "a-3, b-1, c-2, d-4", "a-2, b-3, c-4, d-1", "a-4, b-3, c-1, d-2"],
        "C",
        "38th CAA (1975) barred judicial review (2); 42nd CAA (1976) allowed emergency in part of India (3); 44th CAA (1978) introduced armed rebellion & saved Arts 20-21 (4); 59th CAA (1988) permitted emergency in Punjab for internal disturbance (1).",
        "38-வது திருத்தம் (1975) நீதி மறுஆய்வைத் தடுத்தது (2); 42-வது திருத்தம் (1976) ஒரு பகுதிக்கு அவசரநிலையை அனுமதித்தது (3); 44-வது திருத்தம் (1978) ஆயுதமேந்திய கிளர்ச்சி மற்றும் சரத்து 20-21 பாதுகாப்பைக் கொண்டுவந்தது (4); 59-வது திருத்தம் (1988) பஞ்சாபில் உள்நாட்டு அமைதியின்மைக்காக அவசரநிலையை அனுமதித்தது (1).",
        "Option A is incorrect in its chronology and mapping.", "விருப்பம் A காலவரிசை மற்றும் பொருத்தலில் தவறானது.",
        "Option B mismatches the 38th CAA with territorial provisions.", "விருப்பம் B 38-வது திருத்தத்தை பிராந்திய விதிகளுடன் தவறாகப் பொருத்துகிறது.",
        "Option C is correct; accurately pairs each landmark amendment.", "விருப்பம் C சரியானது; ஒவ்வொரு மைல்கல் திருத்தத்தையும் துல்லியமாகப் பொருத்துகிறது.",
        "Option D confuses 59th CAA with 38th CAA.", "விருப்பம் D 59-வது திருத்தத்தை 38-வது திருத்தத்துடன் குழப்புகிறது.",
        "Amendment Milestones: 38th = Emergency Shield; 42nd = Mini-Constitution; 44th = Restorer of Liberties; 59th = Punjab Exception.",
        "திருத்த மைல்கல்கள்: 38-வது = அவசரநிலைக் கேடயம்; 42-வது = சிறிய அரசியலமைப்பு; 44-வது = உரிமைகளை மீட்டெடுத்தல்; 59-வது = பஞ்சாப் விதிவிலக்கு.",
        "The 59th Amendment Act 1988 was subsequently repealed by the 63rd Amendment Act 1989.",
        "1988-ன் 59-வது திருத்தச் சட்டம் பின்னர் 1989-ன் 63-வது திருத்தச் சட்டத்தால் ரத்து செய்யப்பட்டது."
    ))

    # 004 - Key D: a-4, b-3, c-2, d-1
    qs.append(make_mf_q(
        4, "Approval Deadlines and Majorities",
        "Emergency Type & Action", "அவசரநிலை வகை மற்றும் நடவடிக்கை",
        ["Approval of Article 352", "Disapproval of Article 352", "Approval of Article 356", "Approval of Article 360"],
        ["சரத்து 352-ற்கான ஒப்புதல்", "சரத்து 352-ற்கான நிராகரிப்பு", "சரத்து 356-ற்கான ஒப்புதல்", "சரத்து 360-ற்கான ஒப்புதல்"],
        ["Within 2 months by Simple Majority of both Houses (Finance)", "Within 2 months by Simple Majority of both Houses (State)", "Simple Majority in Lok Sabha only within 14 days", "Within 1 month by Special Majority of both Houses"],
        ["இரு அவைகளிலும் எளிய பெரும்பான்மையால் 2 மாதங்களுக்குள் (நிதி)", "இரு அவைகளிலும் எளிய பெரும்பான்மையால் 2 மாதங்களுக்குள் (மாநிலம்)", "14 நாட்களுக்குள் மக்களவையில் மட்டுமே எளிய பெரும்பான்மை", "இரு அவைகளிலும் சிறப்புப் பெரும்பான்மையால் 1 மாதத்திற்குள்"],
        ["a-1, b-2, c-3, d-4", "a-2, b-1, c-4, d-3", "a-3, b-4, c-1, d-2", "a-4, b-3, c-2, d-1"],
        "D",
        "Approval of Art 352 requires 1 month by Special Majority (4); Disapproval of Art 352 requires Lok Sabha simple majority (3); Approval of Art 356 requires 2 months by Simple Majority (2); Approval of Art 360 requires 2 months by Simple Majority (1).",
        "சரத்து 352 ஒப்புதல் 1 மாதத்தில் சிறப்புப் பெரும்பான்மை (4); சரத்து 352 நிராகரிப்பு மக்களவை எளிய பெரும்பான்மை (3); சரத்து 356 ஒப்புதல் 2 மாதங்களில் எளிய பெரும்பான்மை (2); சரத்து 360 ஒப்புதல் 2 மாதங்களில் எளிய பெரும்பான்மை (1) ஆகும்.",
        "Option A inverts all timelines.", "விருப்பம் A அனைத்து காலக்கெடுகளையும் தலைகீழாக மாற்றுகிறது.",
        "Option B gives wrong approval majorities.", "விருப்பம் B தவறான ஒப்புதல் பெரும்பான்மைகளை அளிக்கிறது.",
        "Option C mismatches disapproval with special majority.", "விருப்பம் C நிராகரிப்பை சிறப்புப் பெரும்பான்மையுடன் தவறாகப் பொருத்துகிறது.",
        "Option D is correct; perfectly matches timeframes and voting majorities.", "விருப்பம் D சரியானது; காலக்கெடு மற்றும் வாக்கு பெரும்பான்மைகளைச் சரியாகப் பொருத்துகிறது.",
        "TNPSC Cheat Sheet: Art 352 = 1 Month (Special); Art 356 = 2 Months (Simple); Art 360 = 2 Months (Simple).",
        "TNPSC குறிப்பு: சரத்து 352 = 1 மாதம் (சிறப்பு); சரத்து 356 = 2 மாதம் (எளிய); சரத்து 360 = 2 மாதம் (எளிய).",
        "Article 352 was originally 2 months, reduced to 1 month by the 44th Amendment Act 1978.",
        "சரத்து 352-ன் கால அவகாசம் முதலில் 2 மாதங்களாக இருந்தது, 1978-ன் 44-வது திருத்தச் சட்டத்தால் 1 மாதமாகக் குறைக்கப்பட்டது."
    ))

    # 005 - Key A: a-3, b-1, c-4, d-2
    qs.append(make_mf_q(
        5, "Grounds for Emergency Actions",
        "Emergency Action / Term", "அவசரநிலை நடவடிக்கை / சொல்",
        ["External Emergency", "Internal Emergency", "Article 365", "Article 358 Trigger"],
        ["வெளிப்புற அவசரநிலை", "உள்நாட்டு அவசரநிலை", "சரத்து 365", "சரத்து 358 செயல்படுத்தப்படுதல்"],
        ["Armed Rebellion (earlier Internal Disturbance)", "Automatic suspension of Article 19 on war/external aggression", "War or External Aggression", "Failure of State to comply with Union directions"],
        ["ஆயுதமேந்திய கிளர்ச்சி (முன்பு உள்நாட்டு அமைதியின்மை)", "போர்/வெளிநாட்டு ஆக்கிரமிப்பின் போது சரத்து 19 தானாக இடைநிறுத்தம்", "போர் அல்லது வெளிநாட்டு ஆக்கிரமிப்பு", "மத்திய அரசின் வழிகாட்டுதல்களை மாநில அரசு பின்பற்றத் தவறுதல்"],
        ["a-3, b-1, c-4, d-2", "a-1, b-3, c-2, d-4", "a-3, b-4, c-1, d-2", "a-2, b-1, c-3, d-4"],
        "A",
        "External Emergency is proclaimed on war/external aggression (3); Internal Emergency is proclaimed on armed rebellion (1); Article 365 triggers President's Rule for defiance of Union directions (4); Article 358 trigger automatically suspends Art 19 during external emergency (2).",
        "வெளிப்புற அவசரநிலை போர்/வெளிநாட்டு ஆக்கிரமிப்பால் அறிவிக்கப்படுகிறது (3); உள்நாட்டு அவசரநிலை ஆயுதமேந்திய கிளர்ச்சியால் அறிவிக்கப்படுகிறது (1); சரத்து 365 மத்திய வழிகாட்டுதலை மீறும் போது குடியரசுத் தலைவர் ஆட்சியைத் தூண்டுகிறது (4); சரத்து 358 வெளிப்புற அவசரநிலையின் போது சரத்து 19-ஐ தானாக இடைநிறுத்துகிறது (2).",
        "Option A is correct; precisely pairs terms with constitutional grounds.", "விருப்பம் A சரியானது; சொற்களை அரசியலமைப்பு காரணங்களுடன் துல்லியமாகப் பொருத்துகிறது.",
        "Option B mismatches external and internal emergencies.", "விருப்பம் B வெளிப்புற மற்றும் உள்நாட்டு அவசரநிலைகளை மாற்றுகிறது.",
        "Option C confuses Article 365 with Article 358.", "விருப்பம் C சரத்து 365-ஐ சரத்து 358-உடன் குழப்புகிறது.",
        "Option D gives erroneous pairs.", "விருப்பம் D தவறான பொருத்தங்களை அளிக்கிறது.",
        "Grounds Summary: External = War / External Aggression; Internal = Armed Rebellion; State failure to obey directions = Article 365.",
        "காரணங்கள் சுருக்கம்: வெளிப்புற = போர் / வெளிநாட்டு ஆக்கிரமிப்பு; உள்நாட்டு = ஆயுதமேந்திய கிளர்ச்சி; வழிகாட்டுதலைப் பின்பற்றத் தவறுதல் = சரத்து 365.",
        "Article 365 is an indispensable companion to Article 356.",
        "சரத்து 365 என்பது சரத்து 356-க்கு ஒரு இன்றியமையாத துணை விதியாகும்."
    ))

    # 006 - Key B: a-3, b-4, c-2, d-1
    qs.append(make_mf_q(
        6, "Three Historic Proclamations of Article 352",
        "Proclamation of Article 352", "சரத்து 352-ன் பிரகடனம்",
        ["First Proclamation (October 1962)", "Second Proclamation (December 1971)", "Third Proclamation (June 1975)", "Revocation of 1971 and 1975 Emergencies"],
        ["முதல் பிரகடனம் (அக்டோபர் 1962)", "இரண்டாவது பிரகடனம் (டிசம்பர் 1971)", "மூன்றாவது பிரகடனம் (ஜூன் 1975)", "1971 மற்றும் 1975 அவசரநிலைகளின் ரத்து"],
        ["March 1977 by Janata Government", "Internal Disturbance", "Chinese Aggression in NEFA", "Indo-Pak War (Liberation of Bangladesh)"],
        ["ஜனதா அரசால் மார்ச் 1977-ல்", "உள்நாட்டு அமைதியின்மை", "நேபாவில் சீன ஆக்கிரமிப்பு", "இந்தோ-பாகிஸ்தான் போர் (வங்காளதேச விடுதலை)"],
        ["a-1, b-2, c-3, d-4", "a-3, b-4, c-2, d-1", "a-3, b-2, c-4, d-1", "a-4, b-3, c-1, d-2"],
        "B",
        "First Proclamation was for Chinese Aggression in NEFA (3); Second Proclamation was for Indo-Pak War (4); Third Proclamation was on Internal Disturbance (2); Both were revoked in March 1977 (1).",
        "முதல் பிரகடனம் நேபாவில் சீன ஆக்கிரமிப்பு (3); இரண்டாவது பிரகடனம் இந்தோ-பாகிஸ்தான் போர் (4); மூன்றாவது பிரகடனம் உள்நாட்டு அமைதியின்மை (2); இரண்டும் மார்ச் 1977-ல் ரத்து செய்யப்பட்டன (1).",
        "Option A completely inverts historical sequence.", "விருப்பம் A வரலாற்று வரிசையைத் தலைகீழாக மாற்றுகிறது.",
        "Option B is correct; accurately aligns historic declarations with causes and revocation.", "விருப்பம் B சரியானது; வரலாற்றுப் பிரகடனங்களை காரணங்கள் மற்றும் ரத்துடன் சரியாக இணைக்கிறது.",
        "Option C swaps second and third emergencies.", "விருப்பம் C இரண்டாவது மற்றும் மூன்றாவது அவசரநிலைகளை மாற்றுகிறது.",
        "Option D attributes 1962 emergency to Indo-Pak war.", "விருப்பம் D 1962 அவசரநிலையை இந்திய-பாகிஸ்தான் போருடன் தவறாக இணைக்கிறது.",
        "National Emergency Chronology: 1962–1968 (China), 1971–1977 (Pakistan), 1975–1977 (Internal).",
        "தேசிய அவசரநிலை காலவரிசை: 1962–1968 (சீனா), 1971–1977 (பாகிஸ்தான்), 1975–1977 (உள்நாட்டு).",
        "Notice that the 2nd and 3rd emergencies were simultaneously in operation between June 1975 and March 1977.",
        "ஜூன் 1975 மற்றும் மார்ச் 1977-க்கு இடையே 2-வது மற்றும் 3-வது அவசரநிலைகள் ஒரே நேரத்தில் செயல்பாட்டில் இருந்தன என்பது குறிப்பிடத்தக்கது."
    ))

    # 007 - Key C: a-2, b-4, c-1, d-3
    qs.append(make_mf_q(
        7, "Key Articles in Part XVIII",
        "Part XVIII Specific Articles", "பகுதி XVIII-ன் குறிப்பிட்ட சரத்துகள்",
        ["Article 353", "Article 354", "Article 357", "Article 358"],
        ["சரத்து 353", "சரத்து 354", "சரத்து 357", "சரத்து 358"],
        ["Exercise of legislative powers under Article 356", "Executive and legislative effect of National Emergency", "Suspension of Article 19 during National Emergency", "Modification of distribution of revenues during Emergency"],
        ["சரத்து 356-ன் கீழ் சட்டமன்ற அதிகாரங்களைச் செயல்படுத்துதல்", "தேசிய அவசரநிலையின் நிர்வாக மற்றும் சட்டமியற்றும் விளைவு", "தேசிய அவசரநிலையின் போது சரத்து 19 இடைநிறுத்தம்", "அவசரநிலையின் போது வருவாய் பகிர்வை மாற்றியமைத்தல்"],
        ["a-1, b-2, c-3, d-4", "a-3, b-1, c-4, d-2", "a-2, b-4, c-1, d-3", "a-4, b-2, c-3, d-1"],
        "C",
        "Article 353 deals with the effect of National Emergency on executive/legislative powers (2); Article 354 deals with modifying distribution of revenues (4); Article 357 deals with exercise of legislative powers under Art 356 (1); Article 358 deals with suspension of Art 19 (3).",
        "சரத்து 353 நிர்வாக/சட்டமன்ற விளைவைக் கையாள்கிறது (2); சரத்து 354 வருவாய் பகிர்வு மாற்றத்தைக் கையாள்கிறது (4); சரத்து 357 சரத்து 356-ன் கீழான சட்டமன்ற அதிகார செயல்பாட்டைக் கையாள்கிறது (1); சரத்து 358 சரத்து 19 இடைநிறுத்தத்தைக் கையாள்கிறது (3).",
        "Option A mismatches Article 353 with legislative powers under 356.", "விருப்பம் A சரத்து 353-ஐ சரத்து 356-ன் கீழான அதிகாரங்களுடன் தவறாகப் பொருத்துகிறது.",
        "Option B gives wrong pairings for all articles.", "விருப்பம் B அனைத்து சரத்துகளுக்கும் தவறான பொருத்தங்களை அளிக்கிறது.",
        "Option C is correct; exact match of constitutional articles in Part XVIII.", "விருப்பம் C சரியானது; பகுதி XVIII சரத்துகளின் சரியான பொருத்தம்.",
        "Option D confuses Article 358 with Article 353.", "விருப்பம் D சரத்து 358-ஐ சரத்து 353-உடன் குழப்புகிறது.",
        "Part XVIII Article Flow: 352 (Proclamation) -> 353 (Effect) -> 354 (Revenues) -> 355 (Duty of Union) -> 356 (Breakdown) -> 357 (Legislative powers under 356) -> 358 (Art 19) -> 359 (Enforcement) -> 360 (Financial).",
        "பகுதி XVIII சரத்து வரிசை: 352 (பிரகடனம்) -> 353 (விளைவு) -> 354 (வருவாய்) -> 355 (மத்திய அரசின் கடமை) -> 356 (வீழ்ச்சி) -> 357 (356-ன் கீழ் சட்டம் இயற்றுதல்) -> 358 (சரத்து 19) -> 359 (செயல்படுத்துதல்) -> 360 (நிதி).",
        "Article 357 permits Parliament to delegate legislative authority for a state under President's Rule to the President.",
        "குடியரசுத் தலைவர் ஆட்சியின் கீழ் உள்ள ஒரு மாநிலத்திற்கான சட்டமன்ற அதிகாரத்தை குடியரசுத் தலைவருக்கு வழங்க பாராளுமன்றத்திற்கு சரத்து 357 அனுமதியளிக்கிறது."
    ))

    # 008 - Key D: a-4, b-3, c-1, d-2
    qs.append(make_mf_q(
        8, "Commissions and Views on Article 356",
        "Commissions and Authorities", "ஆணையங்கள் மற்றும் தலைவர்கள்",
        ["Dr. B.R. Ambedkar", "Sarkaria Commission (1988)", "Punchhi Commission (2010)", "Venkatachaliah Commission (2002)"],
        ["டாக்டர் பி.ஆர். அம்பேத்கர்", "சர்க்காரியா ஆணையம் (1988)", "பூஞ்சி ஆணையம் (2010)", "வெங்கடாசலையா ஆணையம் (2002)"],
        ["Localizing emergency to troubled area rather than whole state", "Recommended Article 356 should be suitably amended / used with caution", "Hoped Article 356 would remain a 'dead letter'", "Recommended Article 356 be used very sparingly as last resort"],
        ["முழு மாநிலத்திற்கும் பதிலாக பாதிக்கப்பட்ட பகுதிக்கு மட்டும் அவசரநிலையை மட்டுப்படுத்துதல்", "சரத்து 356 தகுந்த முறையில் திருத்தப்பட வேண்டும் / எச்சரிக்கையுடன் பயன்படுத்தப்பட வேண்டும்", "சரத்து 356 ஒரு 'செயலற்ற எழுத்தாக' இருக்கும் என நம்பினார்", "சரத்து 356 இறுதி நடவடிக்கையாக மிகவும் அரிதாகப் பயன்படுத்தப்பட வேண்டும்"],
        ["a-1, b-2, c-3, d-4", "a-2, b-4, c-1, d-3", "a-3, b-1, c-4, d-2", "a-4, b-3, c-1, d-2"],
        "D",
        "Ambedkar hoped it would remain a dead letter (3); Sarkaria Commission recommended sparingly as last resort (4); Punchhi Commission proposed localizing emergency (1); Venkatachaliah Commission recommended amendments and caution (2).",
        "டாக்டர் அம்பேத்கர் அது செயலற்ற எழுத்தாக இருக்கும் என நம்பினார் (3); சர்க்காரியா ஆணையம் இறுதி நடவடிக்கையாக அரிதாகப் பயன்படுத்த பரிந்துரைத்தது (4); பூஞ்சி ஆணையம் குறிப்பிட்ட பகுதிக்கு மட்டுப்படுத்த பரிந்துரைத்தது (1); வெங்கடாசலையா ஆணையம் திருத்தங்கள் மற்றும் எச்சரிக்கையைப் பரிந்துரைத்தது (2).",
        "Option A is incorrect.", "விருப்பம் A தவறானது.",
        "Option B is incorrect.", "விருப்பம் B தவறானது.",
        "Option C is incorrect.", "விருப்பம் C தவறானது.",
        "Option D is correct; matches all commission viewpoints accurately.", "விருப்பம் D சரியானது; அனைத்து ஆணையங்களின் கருத்துக்களையும் சரியாகப் பொருத்துகிறது.",
        "Centre-State Landmark Concept: Punchhi Commission recommended 'Localised Emergency' under Articles 355 & 356.",
        "மத்திய-மாநில முக்கியக் கருத்து: பூஞ்சி ஆணையம் சரத்து 355 மற்றும் 356-ன் கீழ் 'உள்ளூர்மயமாக்கப்பட்ட அவசரநிலையை' பரிந்துரைத்தது.",
        "The Venkatachaliah Commission (NCRWC) was appointed in 2000 to review the working of the Constitution.",
        "அரசியலமைப்பு செயல்பாட்டை மறுஆய்வு செய்வதற்காக 2000-ல் வெங்கடாசலையா ஆணையம் (NCRWC) நியமிக்கப்பட்டது."
    ))

    # 009 - Key A: a-2, b-3, c-4, d-1
    qs.append(make_mf_q(
        9, "States and President's Rule Milestones",
        "State and President's Rule Record", "மாநிலம் மற்றும் குடியரசுத் தலைவர் ஆட்சி சாதனை",
        ["Punjab (East Punjab)", "Kerala", "Tamil Nadu", "Manipur / Uttar Pradesh"],
        ["பஞ்சாப் (கிழக்கு பஞ்சாப்)", "கேரளா", "தமிழ்நாடு", "மணிப்பூர் / உத்தரப் பிரதேசம்"],
        ["States subjected to President's Rule maximum times (10 times each)", "First State where Article 356 was imposed (1951)", "Dismissal of EMS Namboodiripad ministry under Article 356 (1959)", "First imposition of President's Rule in January 1976"],
        ["அதிக முறை குடியரசுத் தலைவர் ஆட்சி விதிக்கப்பட்ட மாநிலங்கள் (தலா 10 முறை)", "சரத்து 356 முதன்முதலில் விதிக்கப்பட்ட மாநிலம் (1951)", "சரத்து 356-ன் கீழ் இ.எம்.எஸ். நம்பூதிரிபாட் அரசு கலைக்கப்பட்டது (1959)", "ஜனவரி 1976-ல் முதன்முறையாக குடியரசுத் தலைவர் ஆட்சி அமல்"],
        ["a-2, b-3, c-4, d-1", "a-1, b-2, c-3, d-4", "a-3, b-4, c-1, d-2", "a-2, b-1, c-4, d-3"],
        "A",
        "Punjab was the first state under Article 356 in 1951 (2); Kerala saw EMS Namboodiripad dismissed in 1959 (3); Tamil Nadu first experienced it in Jan 1976 (4); Manipur and UP have faced it the maximum times (10 times) (1).",
        "பஞ்சாப் 1951-ல் முதல் மாநிலம் (2); கேரளாவில் 1959-ல் நம்பூதிரிபாட் அரசு கலைக்கப்பட்டது (3); தமிழ்நாட்டில் ஜனவரி 1976-ல் முதன்முறை விதிக்கப்பட்டது (4); மணிப்பூர் மற்றும் உ.பி அதிகபட்சமாக 10 முறை எதிர்கொண்டன (1).",
        "Option A is correct; captures the key state-wise records.", "விருப்பம் A சரியானது; மாநில வாரியான முக்கியப் பதிவுகளை சரியாகப் பொருத்துகிறது.",
        "Option B is in wrong chronological sequence.", "விருப்பம் B தவறான காலவரிசையில் உள்ளது.",
        "Option C swaps Kerala and Punjab.", "விருப்பம் C கேரளா மற்றும் பஞ்சாப்பை மாற்றுகிறது.",
        "Option D mismatches Tamil Nadu with Manipur.", "விருப்பம் D தமிழ்நாட்டை மணிப்பூருடன் தவறாகப் பொருத்துகிறது.",
        "TNPSC Favorite Record: Punjab = First (1951); Kerala = 1959 communist dismissal; Tamil Nadu = 1976, 1980, 1988, 1991.",
        "TNPSC விருப்பப் பதிவு: பஞ்சாப் = முதல் முறை (1951); கேரளா = 1959 கம்யூனிஸ்ட் அரசு கலைப்பு; தமிழ்நாடு = 1976, 1980, 1988, 1991.",
        "Chhattisgarh and Telangana are the only states where President's Rule has never been imposed so far.",
        "சத்தீஸ்கர் மற்றும் தெலங்கானா ஆகிய மாநிலங்களில் மட்டுமே இதுவரை ஒருமுறை கூட குடியரசுத் தலைவர் ஆட்சி விதிக்கப்படவில்லை."
    ))

    # 010 - Key B: a-3, b-4, c-1, d-2
    qs.append(make_mf_q(
        10, "Presidents and Emergency Proclamations",
        "President of India", "இந்தியக் குடியரசுத் தலைவர்",
        ["Dr. S. Radhakrishnan", "V.V. Giri", "Fakhruddin Ali Ahmed", "Dr. Rajendra Prasad"],
        ["டாக்டர் எஸ். ராதாகிருஷ்ணன்", "வி.வி. கிரி", "பக்ருதீன் அலி அகமது", "டாக்டர் ராஜேந்திர பிரசாத்"],
        ["Proclaimed the Third National Emergency (1975)", "First President to assent to Article 356 in Punjab (1951)", "Proclaimed the First National Emergency (1962)", "Proclaimed the Second National Emergency (1971)"],
        ["மூன்றாவது தேசிய அவசரநிலையைப் பிரகடனம் செய்தார் (1975)", "பஞ்சாபில் சரத்து 356-க்கு ஒப்புதல் அளித்த முதல் குடியரசுத் தலைவர் (1951)", "முதல் தேசிய அவசரநிலையைப் பிரகடனம் செய்தார் (1962)", "இரண்டாவது தேசிய அவசரநிலையைப் பிரகடனம் செய்தார் (1971)"],
        ["a-1, b-2, c-3, d-4", "a-3, b-4, c-1, d-2", "a-4, b-3, c-2, d-1", "a-3, b-1, c-4, d-2"],
        "B",
        "Dr. S. Radhakrishnan proclaimed the 1st National Emergency in 1962 (3); V.V. Giri proclaimed the 2nd in 1971 (4); Fakhruddin Ali Ahmed proclaimed the 3rd in 1975 (1); Dr. Rajendra Prasad assented to the first Art 356 in Punjab in 1951 (2).",
        "டாக்டர் எஸ். ராதாகிருஷ்ணன் 1962-ல் முதல் தேசிய அவசரநிலையை அறிவித்தார் (3); வி.வி. கிரி 1971-ல் 2-வது அவசரநிலையை அறிவித்தார் (4); பக்ருதீன் அலி அகமது 1975-ல் 3-வது அவசரநிலையை அறிவித்தார் (1); டாக்டர் ராஜேந்திர பிரசாத் 1951-ல் பஞ்சாபில் முதல் சரத்து 356-க்கு ஒப்புதல் அளித்தார் (2).",
        "Option A is completely out of order.", "விருப்பம் A முற்றிலும் வரிசை தவறியுள்ளது.",
        "Option B is correct; accurately links each President to historical emergency milestones.", "விருப்பம் B சரியானது; ஒவ்வொரு குடியரசுத் தலைவரையும் வரலாற்று மைல்கல்களுடன் துல்லியமாக இணைக்கிறது.",
        "Option C swaps Radhakrishnan and Giri.", "விருப்பம் C ராதாகிருஷ்ணன் மற்றும் கிரியை மாற்றுகிறது.",
        "Option D mismatches Rajendra Prasad with Fakhruddin Ali Ahmed.", "விருப்பம் D ராஜேந்திர பிரசாத்தை பக்ருதீன் அலி அகமதுவுடன் தவறாகப் பொருத்துகிறது.",
        "Presidential Grid: 1962 = Radhakrishnan; 1971 = V.V. Giri; 1975 = Fakhruddin Ali Ahmed.",
        "குடியரசுத் தலைவர் பட்டியல்: 1962 = ராதாகிருஷ்ணன்; 1971 = வி.வி. கிரி; 1975 = பக்ருதீன் அலி அகமது.",
        "Fakhruddin Ali Ahmed signed the 1975 emergency proclamation late at night on June 25, 1975.",
        "1975 ஜூன் 25 நள்ளிரவில் பக்ருதீன் அலி அகமது அவசரநிலைப் பிரகடனத்தில் கையெழுத்திட்டார்."
    ))

    # 011 - Key C: a-4, b-1, c-2, d-3
    qs.append(make_mf_q(
        11, "Maximum Duration Limits under Part XVIII",
        "Emergency Type / Institution", "அவசரநிலை வகை / நிறுவனம்",
        ["National Emergency (Article 352)", "President's Rule (Normal Maximum)", "President's Rule (Punjab Exception)", "Financial Emergency (Article 360)"],
        ["தேசிய அவசரநிலை (சரத்து 352)", "குடியரசுத் தலைவர் ஆட்சி (இயல்பான உச்சவரம்பு)", "குடியரசுத் தலைவர் ஆட்சி (பஞ்சாப் விதிவிலக்கு)", "நிதி அவசரநிலை (சரத்து 360)"],
        ["Maximum 3 years", "Extended up to 5 years via 67th/68th Amendments", "Indefinite without repeated parliamentary renewals", "Indefinite with 6-month periodic parliamentary approvals"],
        ["அதிகபட்சம் 3 ஆண்டுகள்", "67/68-வது திருத்தங்கள் மூலம் 5 ஆண்டுகள் வரை நீட்டிக்கப்பட்டது", "தொடர் பாராளுமன்ற ஒப்புதலின்றி காலவரையின்றி", "6 மாத காலமுறை பாராளுமன்ற ஒப்புதல்களுடன் காலவரையின்றி"],
        ["a-1, b-2, c-3, d-4", "a-2, b-3, c-4, d-1", "a-4, b-1, c-2, d-3", "a-3, b-4, c-1, d-2"],
        "C",
        "National Emergency continues indefinitely with 6-month approvals (4); President's Rule normal maximum is 3 years (1); Punjab was extended up to 5 years (2); Financial Emergency continues indefinitely without renewals (3).",
        "தேசிய அவசரநிலை 6 மாத ஒப்புதல்களுடன் காலவரையின்றித் தொடரும் (4); குடியரசுத் தலைவர் ஆட்சியின் இயல்பான உச்சவரம்பு 3 ஆண்டுகள் (1); பஞ்சாப் 5 ஆண்டுகள் வரை நீட்டிக்கப்பட்டது (2); நிதி அவசரநிலை புதுப்பித்தலின்றி காலவரையின்றி நீடிக்கும் (3).",
        "Option A reverses duration limits.", "விருப்பம் A கால வரம்புகளை மாற்றுகிறது.",
        "Option B confuses Financial Emergency with National Emergency.", "விருப்பம் B நிதி அவசரநிலையை தேசிய அவசரநிலையுடன் குழப்புகிறது.",
        "Option C is correct; exact mapping of maximum operational limits.", "விருப்பம் C சரியானது; அதிகபட்ச செயல்பாட்டு வரம்புகளின் சரியான பொருத்தம்.",
        "Option D swaps Punjab and normal Art 356 limit.", "விருப்பம் D பஞ்சாப் மற்றும் இயல்பான சரத்து 356 வரம்பை மாற்றுகிறது.",
        "Duration Summary: Art 352 = Indefinite (renew every 6 months); Art 356 = Max 3 years; Art 360 = Indefinite (NO renewal).",
        "கால அளவு சுருக்கம்: சரத்து 352 = காலவரையின்றி (6 மாதங்களுக்கு ஒருமுறை புதுப்பிக்க வேண்டும்); சரத்து 356 = அதிகபட்சம் 3 ஆண்டுகள்; சரத்து 360 = காலவரையின்றி (புதுப்பித்தல் தேவையில்லை).",
        "Punjab President's Rule from 1987 to 1992 was the longest continuous spell in Indian history.",
        "1987 முதல் 1992 வரை பஞ்சாபில் நீடித்த குடியரசுத் தலைவர் ஆட்சியே இந்திய வரலாற்றில் மிக நீண்ட தொடர்ச்சியான ஆட்சியாகும்."
    ))

    # 012 - Key D: a-3, b-4, c-2, d-1
    qs.append(make_mf_q(
        12, "Impact on Fundamental Rights",
        "Fundamental Right / Article", "அடிப்படை உரிமை / சரத்து",
        ["Article 19", "Articles 20 and 21", "Article 32", "Article 359 Scope"],
        ["சரத்து 19", "சரத்துகள் 20 மற்றும் 21", "சரத்து 32", "சரத்து 359-ன் வரம்பு"],
        ["Right to move courts for enforcement of specified rights suspended by presidential order", "Remedy suspended if specified in Presidential Order", "Never suspended under any circumstances (44th CAA)", "Automatically suspended under Article 358 during war/external aggression"],
        ["குடியரசுத் தலைவர் ஆணையால் குறிப்பிட்ட உரிமைகளைச் செயல்படுத்த நீதிமன்றத்தை நாடும் உரிமை இடைநிறுத்தம்", "குடியரசுத் தலைவர் ஆணையில் குறிப்பிடப்பட்டால் தீர்வு இடைநிறுத்தம்", "எந்தச் சூழலிலும் ஒருபோதும் இடைநிறுத்தப்பட முடியாது (44-வது திருத்தம்)", "போர்/வெளிநாட்டு ஆக்கிரமிப்பின் போது சரத்து 358-ன் கீழ் தானாக இடைநிறுத்தம்"],
        ["a-1, b-2, c-3, d-4", "a-2, b-1, c-4, d-3", "a-4, b-1, c-2, d-3", "a-4, b-3, c-2, d-1"],
        "D",
        "Article 19 is automatically suspended under Article 358 (4); Articles 20 & 21 can never be suspended (3); Article 32 remedy suspended if specified (2); Article 359 suspends court enforcement of specified rights (1).",
        "சரத்து 19 சரத்து 358-ன் கீழ் தானாக இடைநிறுத்தப்படுகிறது (4); சரத்து 20 மற்றும் 21 எக்காலத்திலும் இடைநிறுத்தப்பட முடியாது (3); சரத்து 32 தீர்வு ஆணையில் குறிப்பிடப்பட்டால் இடைநிறுத்தப்படும் (2); சரத்து 359 குறிப்பிட்ட உரிமைகளுக்கான நீதிமன்ற அணுகலை இடைநிறுத்துகிறது (1).",
        "Option A is incorrect.", "விருப்பம் A தவறானது.",
        "Option B is incorrect.", "விருப்பம் B தவறானது.",
        "Option C confuses Article 19 with Article 359.", "விருப்பம் C சரத்து 19-ஐ சரத்து 359-உடன் குழப்புகிறது.",
        "Option D is correct; precisely captures the post-44th Amendment legal position of Fundamental Rights.", "விருப்பம் D சரியானது; 44-வது திருத்தத்திற்குப் பிந்தைய அடிப்படை உரிமைகளின் நிலையைத் துல்லியமாகப் படம்பிடிக்கிறது.",
        "Critical Distinction: Article 358 suspends the right (Art 19); Article 359 suspends the enforcement of specified rights.",
        "முக்கிய வேறுபாடு: சரத்து 358 உரிமையையே இடைநிறுத்துகிறது (சரத்து 19); சரத்து 359 குறிப்பிட்ட உரிமைகளைச் செயல்படுத்துவதை இடைநிறுத்துகிறது.",
        "Articles 20 and 21 were shielded from suspension by Section 37 and 40 of the 44th Constitutional Amendment Act 1978.",
        "1978-ன் 44-வது அரசியலமைப்பு திருத்தச் சட்டத்தின் பிரிவுகள் 37 மற்றும் 40 மூலம் சரத்துகள் 20 மற்றும் 21 இடைநிறுத்தத்திலிருந்து பாதுகாக்கப்பட்டன."
    ))

    # 013 - Key A: a-3, b-1, c-4, d-2
    qs.append(make_mf_q(
        13, "Types of Constitutional Breakdowns under Article 356",
        "Breakdown Category (Sarkaria Commission)", "வீழ்ச்சி வகை (சர்க்காரியா ஆணையம்)",
        ["Political Breakdown", "Constitutional Breakdown", "Economic Breakdown", "Physical Breakdown"],
        ["அரசியல் வீழ்ச்சி", "அரசியலமைப்பு வீழ்ச்சி", "பொருளாதார வீழ்ச்சி", "உடல்/சட்டம்-ஒழுங்கு வீழ்ச்சி"],
        ["Willful defiance of constitutional directives of the Union (Article 365)", "Paralysis of state machinery due to widespread internal violence or insurgency", "No party or coalition able to form a ministry after elections (hung assembly)", "Not a valid ground under Article 356 (pertains to Article 360)"],
        ["மத்திய அரசின் அரசியலமைப்பு வழிகாட்டுதல்களை வேண்டுமென்றே மீறுதல் (சரத்து 365)", "பரவலான உள்நாட்டு வன்முறை அல்லது கிளர்ச்சியால் மாநில நிர்வாகம் முடங்குதல்", "தேர்தலுக்குப் பின் எந்தக் கட்சியும் அமைச்சரவை அமைக்க முடியாத நிலை (தொங்கு சட்டமன்றம்)", "சரத்து 356-ன் கீழ் செல்லுபடியாகும் காரணமல்ல (சரத்து 360-க்கு உரியது)"],
        ["a-3, b-1, c-4, d-2", "a-1, b-3, c-2, d-4", "a-4, b-2, c-1, d-3", "a-2, b-4, c-3, d-1"],
        "A",
        "Political breakdown = Hung assembly where no ministry can be formed (3); Constitutional breakdown = Defiance of Union directions under Art 365 (1); Economic breakdown = Not an Art 356 ground (governed by Art 360) (4); Physical breakdown = Insurgency/violence paralyzing state (2).",
        "அரசியல் வீழ்ச்சி = அமைச்சரவை அமைக்க முடியாத தொங்கு சட்டமன்றம் (3); அரசியலமைப்பு வீழ்ச்சி = சரத்து 365 வழிகாட்டுதல் மீறல் (1); பொருளாதார வீழ்ச்சி = சரத்து 356 காரணம் அல்ல (சரத்து 360-க்குரியது) (4); நிர்வாக முடக்கம் = வன்முறையால் அரசு முடங்குதல் (2).",
        "Option A is correct; captures the taxonomy of breakdown situations recognized by the Sarkaria Commission.", "விருப்பம் A சரியானது; சர்க்காரியா ஆணையம் அங்கீகரித்த வீழ்ச்சி சூழ்நிலைகளின் வகைப்பாட்டைச் சரியாகப் படம்பிடிக்கிறது.",
        "Option B mismatches political with constitutional breakdown.", "விருப்பம் B அரசியல் மற்றும் அரசியலமைப்பு வீழ்ச்சிகளை மாற்றுகிறது.",
        "Option C treats economic breakdown as an Art 356 ground.", "விருப்பம் C பொருளாதார வீழ்ச்சியை சரத்து 356 காரணமாகக் கருதுகிறது.",
        "Option D gives erroneous pairs.", "விருப்பம் D தவறான பொருத்தங்களை அளிக்கிறது.",
        "Sarkaria Taxonomy: Article 356 covers political, constitutional, and physical breakdown; purely financial crisis belongs to Article 360.",
        "சர்க்காரியா வகைப்பாடு: சரத்து 356 அரசியல், அரசியலமைப்பு மற்றும் சட்ட-ஒழுங்கு முடக்கத்தை உள்ளடக்கியது; நிதி நெருக்கடி சரத்து 360-க்கு உரியது.",
        "Hung assembly is the most frequent ground on which Article 356 has historically been invoked in India.",
        "இந்தியாவில் வரலாற்று ரீதியாக சரத்து 356 பயன்படுத்தப்பட்டதற்கு 'தொங்கு சட்டமன்றம்' உருவாவதே மிக முக்கியக் காரணமாக இருந்துள்ளது."
    ))

    # 014 - Key B: a-2, b-4, c-1, d-3
    qs.append(make_mf_q(
        14, "Legislative Powers delegated under Article 357",
        "Article 357 Clause / Term", "சரத்து 357 பிரிவு / சொல்",
        ["Article 357(1)(a)", "Article 357(1)(b)", "Article 357(1)(c)", "Article 357(2)"],
        ["சரத்து 357(1)(a)", "சரத்து 357(1)(b)", "சரத்து 357(1)(c)", "சரத்து 357(2)"],
        ["President authorizing expenditure from State Consolidated Fund pending Lok Sabha approval", "Parliament delegating state legislative power to the President", "Laws made by Parliament/President continue until altered by State Legislature", "President or delegated authority making laws conferring powers on Union officers"],
        ["மக்களவை ஒப்புதலுக்காகக் காத்திருக்கும் போது மாநிலத் தொகுப்பு நிதியிலிருந்து செலவினத்தை அனுமதிக்க குடியரசுத் தலைவருக்கு அதிகாரம்", "மாநில சட்டமன்ற அதிகாரத்தைப் பாராளுமன்றம் குடியரசுத் தலைவருக்கு வழங்குதல்", "பாராளுமன்றம்/குடியரசுத் தலைவர் இயற்றிய சட்டங்கள் மாநில சட்டமன்றத்தால் மாற்றப்படும் வரை தொடரும்", "மத்திய அதிகாரிகளுக்கு அதிகாரங்களை வழங்கும் சட்டங்களை இயற்ற குடியரசுத் தலைவர் அல்லது அதிகாரம் பெற்றவருக்கு அனுமதி"],
        ["a-1, b-2, c-3, d-4", "a-2, b-4, c-1, d-3", "a-3, b-1, c-4, d-2", "a-4, b-3, c-2, d-1"],
        "B",
        "Art 357(1)(a) = Parliament delegates state lawmaking power to President (2); Art 357(1)(b) = Conferring powers on Union officers (4); Art 357(1)(c) = Authorizing expenditure from Consolidated Fund (1); Art 357(2) = Laws continue until altered by State Legislature (3).",
        "சரத்து 357(1)(a) = சட்டமன்ற அதிகாரத்தைக் குடியரசுத் தலைவருக்கு வழங்குதல் (2); சரத்து 357(1)(b) = மத்திய அதிகாரிகளுக்கு அதிகாரங்களை வழங்குதல் (4); சரத்து 357(1)(c) = தொகுப்பு நிதியிலிருந்து செலவை அனுமதித்தல் (1); சரத்து 357(2) = மாற்றப்படும் வரை சட்டங்கள் நீடித்தல் (3).",
        "Option A inverts procedural clauses.", "விருப்பம் A நடைமுறைப் பிரிவுகளை மாற்றுகிறது.",
        "Option B is correct; exact alignment with Article 357 sub-clauses.", "விருப்பம் B சரியானது; சரத்து 357-ன் துணைப் பிரிவுகளுடன் துல்லியமாகப் பொருந்துகிறது.",
        "Option C confuses clause (a) with clause (c).", "விருப்பம் C பிரிவு (a)-வை பிரிவு (c)-உடன் குழப்புகிறது.",
        "Option D swaps all clauses.", "விருப்பம் D அனைத்துப் பிரிவுகளையும் தலைகீழாக மாற்றுகிறது.",
        "Key 44th CAA Change in 357(2): Before 1978, President's laws expired 1 year after Art 356 ended; now they continue indefinitely until altered/repealed by the re-elected State Legislature.",
        "சரத்து 357(2)-ல் 44-வது திருத்தம் செய்த மாற்றம்: 1978-க்கு முன், குடியரசுத் தலைவர் சட்டங்கள் 1 வருடத்தில் காலாவதியானது; இப்போது மீண்டும் தேர்ந்தெடுக்கப்பட்ட சட்டமன்றம் மாற்றும் வரை அவை தொடரும்.",
        "The President usually enacts 'President's Acts' for the state in consultation with a parliamentary consultative committee.",
        "குடியரசுத் தலைவர் வழக்கமாகப் பாராளுமன்ற ஆலோசனைக் குழுவுடன் கலந்தாலோசித்து மாநிலத்திற்கான 'குடியரசுத் தலைவர் சட்டங்களை' இயற்றுகிறார்."
    ))

    # 015 - Key C: a-3, b-4, c-1, d-2
    qs.append(make_mf_q(
        15, "Financial Emergency Measures under Article 360",
        "Article 360 Direction", "சரத்து 360-ன் கீழான வழிகாட்டுதல்",
        ["Canons of Financial Propriety", "Reduction of State Salaries", "Money Bills Reservation", "Reduction of Union Salaries"],
        ["நிதி ஒழுங்குமுறைக் கோட்பாடுகள்", "மாநில ஊழியர்களின் ஊதியக் குறைப்பு", "நிதி மசோதாக்கள் குடியரசுத் தலைவருக்கு ஒதுக்கப்படுதல்", "மத்திய ஊழியர்களின் ஊதியக் குறைப்பு"],
        ["All Money Bills passed by State Legislature reserved for President's consideration", "Includes Judges of Supreme Court and High Courts", "Union executive directing State to observe specified canons of financial propriety", "Reduction of salaries of all persons serving in connection with State affairs"],
        ["மாநில சட்டமன்றத்தால் நிறைவேற்றப்பட்ட அனைத்து நிதி மசோதாக்களும் குடியரசுத் தலைவரின் பரிசீலனைக்கு ஒதுக்கப்படுதல்", "உச்ச நீதிமன்ற மற்றும் உயர் நீதிமன்ற நீதிபதிகள் உட்பட", "குறிப்பிட்ட நிதி ஒழுங்குமுறைக் கோட்பாடுகளைக் கடைப்பிடிக்குமாறு மாநிலத்திற்கு மத்திய நிர்வாகம் வழிகாட்டுதல்", "மாநில விவகாரங்களில் பணியாற்றும் அனைத்து நபர்களின் ஊதியங்களையும் குறைத்தல்"],
        ["a-1, b-2, c-3, d-4", "a-2, b-1, c-4, d-3", "a-3, b-4, c-1, d-2", "a-4, b-3, c-2, d-1"],
        "C",
        "Canons of financial propriety = Union directing state (3); Reduction of state salaries = Persons serving state (4); Money Bills reservation = Reserved for President (1); Reduction of Union salaries = Includes SC/HC judges (2).",
        "நிதி ஒழுங்குமுறைக் கோட்பாடுகள் = மாநிலத்திற்கு மத்திய வழிகாட்டுதல் (3); மாநில ஊதியக் குறைப்பு = மாநிலப் பணியாளர்கள் (4); நிதி மசோதா ஒதுக்கீடு = குடியரசுத் தலைவர் பரிசீலனைக்கு (1); மத்திய ஊதியக் குறைப்பு = உச்ச/உயர் நீதிமன்ற நீதிபதிகள் உட்பட (2).",
        "Option A is incorrect in its alignment.", "விருப்பம் A பொருத்தலில் தவறானது.",
        "Option B mismatches canons with judges salaries.", "விருப்பம் B நிதி ஒழுங்குமுறையை நீதிபதிகள் சம்பளத்துடன் குழப்புகிறது.",
        "Option C is correct; accurately pairs each Article 360 directive power.", "விருப்பம் C சரியானது; சரத்து 360-ன் ஒவ்வொரு வழிகாட்டுதல் அதிகாரத்தையும் துல்லியமாகப் பொருத்துகிறது.",
        "Option D swaps state and union salary directions.", "விருப்பம் D மாநில மற்றும் மத்திய ஊதிய வழிகாட்டுதல்களை மாற்றுகிறது.",
        "Unprecedented Financial Control: During Article 360, the Centre acquires total control over state financial affairs.",
        "முன்னோடியில்லாத நிதிக் கட்டுப்பாடு: சரத்து 360-ன் போது, மாநிலத்தின் நிதி விவகாரங்கள் மீது மத்திய அரசு முழுமையான கட்டுப்பாட்டைப் பெறுகிறது.",
        "Article 360(4)(b) specifically empowers reduction of salaries of Supreme Court and High Court judges.",
        "சரத்து 360(4)(b) உச்ச நீதிமன்ற மற்றும் உயர் நீதிமன்ற நீதிபதிகளின் ஊதியங்களைக் குறைக்க வெளிப்படையாக அதிகாரமளிக்கிறது."
    ))

    # 016 - Key D: a-2, b-1, c-4, d-3
    qs.append(make_mf_q(
        16, "Judicial Review Concepts in Emergency",
        "Constitutional Doctrine / Case", "அரசியலமைப்பு கோட்பாடு / வழக்கு",
        ["State of Rajasthan v. UOI (1977)", "Minerva Mills v. UOI (1980)", "S.R. Bommai v. UOI (1994)", "Rameshwar Prasad v. UOI (2006)"],
        ["ராஜஸ்தான் மாநிலம் எதிர் மத்திய அரசு (1977)", "மினர்வா மில்ஸ் எதிர் மத்திய அரசு (1980)", "எஸ்.ஆர். பொம்மை எதிர் மத்திய அரசு (1994)", "ராமேஷ்வர் பிரசாத் எதிர் மத்திய அரசு (2006)"],
        ["National Emergency open to challenge on grounds of mala fide", "First case where SC examined scope of judicial review of Article 356", "Dissolution of newly elected assembly before first sitting held mala fide and void", "Secularism held basic feature; floor test mandatory; Assembly dissolution only after parliamentary approval"],
        ["தவறான உள்நோக்கம் என்ற அடிப்படையில் தேசிய அவசரநிலையை எதிர்த்து வழக்கு தொடரலாம்", "சரத்து 356-ன் நீதி மறுஆய்வு வரம்பை உச்ச நீதிமன்றம் ஆய்வு செய்த முதல் வழக்கு", "புதிதாகத் தேர்ந்தெடுக்கப்பட்ட சட்டமன்றம் முதல் கூட்டத்திற்கு முன்பே கலைக்கப்பட்டது உள்நோக்கமுடையது மற்றும் செல்லாது", "மதச்சார்பின்மை அடிப்படைக் கட்டமைப்பு; நம்பிக்கை வாக்கெடுப்பு கட்டாயம்; பாராளுமன்ற ஒப்புதலுக்குப் பிறகே சட்டமன்றக் கலைப்பு"],
        ["a-1, b-2, c-3, d-4", "a-3, b-4, c-1, d-2", "a-4, b-3, c-2, d-1", "a-2, b-1, c-4, d-3"],
        "D",
        "Rajasthan v. UOI (1977) = First case on Art 356 review (2); Minerva Mills (1980) = Art 352 mala fide review (1); Bommai (1994) = Secularism & floor test & assembly protection (4); Rameshwar Prasad (2006) = Bihar dissolution held void (3).",
        "ராஜஸ்தான் வழக்கு (1977) = சரத்து 356 மறுஆய்வு குறித்த முதல் வழக்கு (2); மினர்வா மில்ஸ் (1980) = சரத்து 352 உள்நோக்க மறுஆய்வு (1); பொம்மை (1994) = மதச்சார்பின்மை, வாக்கெடுப்பு மற்றும் சட்டமன்றப் பாதுகாப்பு (4); ராமேஷ்வர் பிரசாத் (2006) = பீகார் கலைப்பு செல்லாது (3).",
        "Option A is incorrect.", "விருப்பம் A தவறானது.",
        "Option B mismatches Bommai with Rajasthan case.", "விருப்பம் B பொம்மை வழக்கை ராஜஸ்தான் வழக்குடன் குழப்புகிறது.",
        "Option C attributes Rameshwar Prasad holding to Minerva Mills.", "விருப்பம் C ராமேஷ்வர் பிரசாத் தீர்ப்பை மினர்வா மில்சுடன் இணைக்கிறது.",
        "Option D is correct; perfectly captures the judicial evolution of emergency review.", "விருப்பம் D சரியானது; அவசரநிலை நீதி மறுஆய்வின் வரலாற்று வளர்ச்சியைச் சரியாகப் படம்பிடிக்கிறது.",
        "Judicial Evolution: 1977 (Rajasthan - limited review) -> 1980 (Minerva - 352 review) -> 1994 (Bommai - strict objective scrutiny) -> 2006 (Rameshwar - Governor's report struck down).",
        "நீதித்துறை பரிணாமம்: 1977 (ராஜஸ்தான் - வரம்பிற்குட்பட்ட ஆய்வு) -> 1980 (மினர்வா - 352 ஆய்வு) -> 1994 (பொம்மை - கடுமையான புறநிலை ஆய்வு) -> 2006 (ராமேஷ்வர் - ஆளுநர் அறிக்கை ரத்து).",
        "In Rameshwar Prasad (2006), Governor Buta Singh's recommendation to dissolve the Bihar assembly was held unconstitutional.",
        "ராமேஷ்வர் பிரசாத் (2006) வழக்கில், பீகார் சட்டமன்றத்தைக் கலைக்க ஆளுநர் பூட்டா சிங் அளித்த பரிந்துரை அரசியலமைப்புக்கு முரணானது எனத் தீர்ப்பளிக்கப்பட்டது."
    ))

    # 017 - Key A: a-3, b-4, c-1, d-2
    qs.append(make_mf_q(
        17, "Revocation Mechanisms of Emergency",
        "Emergency Action", "அவசரநிலை நடவடிக்கை",
        ["President revoking Article 352", "Lok Sabha disapproving Article 352", "President revoking Article 356", "President revoking Article 360"],
        ["குடியரசுத் தலைவர் சரத்து 352-ஐ ரத்து செய்தல்", "மக்களவை சரத்து 352-ஐ நிராகரித்தல்", "குடியரசுத் தலைவர் சரத்து 356-ஐ ரத்து செய்தல்", "குடியரசுத் தலைவர் சரத்து 360-ஐ ரத்து செய்தல்"],
        ["Can be done at any time by subsequent proclamation without parliamentary approval (State)", "Can be done at any time by subsequent proclamation without parliamentary approval (Financial)", "Can be done at any time by subsequent proclamation without parliamentary approval (National)", "Passed by Simple Majority of Lok Sabha alone pursuant to notice by 1/10th members"],
        ["பாராளுமன்ற ஒப்புதலின்றி பிந்தைய பிரகடனம் மூலம் எந்த நேரத்திலும் செய்யப்படலாம் (மாநிலம்)", "பாராளுமன்ற ஒப்புதலின்றி பிந்தைய பிரகடனம் மூலம் எந்த நேரத்திலும் செய்யப்படலாம் (நிதி)", "பாராளுமன்ற ஒப்புதலின்றி பிந்தைய பிரகடனம் மூலம் எந்த நேரத்திலும் செய்யப்படலாம் (தேசியம்)", "1/10 உறுப்பினர்களின் அறிவிப்பைத் தொடர்ந்து மக்களவையின் எளிய பெரும்பான்மையால் நிறைவேற்றப்படுவது"],
        ["a-3, b-4, c-1, d-2", "a-1, b-2, c-3, d-4", "a-4, b-3, c-2, d-1", "a-2, b-1, c-4, d-3"],
        "A",
        "President revokes Art 352 anytime without parliamentary approval (3); Lok Sabha disapproves Art 352 by simple majority on 1/10th notice (4); President revokes Art 356 anytime without parliamentary approval (1); President revokes Art 360 anytime without parliamentary approval (2).",
        "குடியரசுத் தலைவர் சரத்து 352-ஐ பாராளுமன்ற ஒப்புதலின்றி ரத்து செய்தல் (3); மக்களவை 1/10 அறிவிப்பில் எளிய பெரும்பான்மையால் நிராகரித்தல் (4); சரத்து 356-ஐ குடியரசுத் தலைவர் ரத்து செய்தல் (1); சரத்து 360-ஐ குடியரசுத் தலைவர் ரத்து செய்தல் (2).",
        "Option A is correct; captures the subtle nuances of revocation powers.", "விருப்பம் A சரியானது; ரத்து செய்யும் அதிகாரங்களின் நுட்பமான வேறுபாடுகளைப் படம்பிடிக்கிறது.",
        "Option B is in wrong sequence.", "விருப்பம் B தவறான வரிசையில் உள்ளது.",
        "Option C treats presidential revocation as requiring 1/10th notice.", "விருப்பம் C குடியரசுத் தலைவரின் ரத்திற்கு 1/10 அறிவிப்பு தேவை எனக் கருதுகிறது.",
        "Option D mismatches approval with revocation.", "விருப்பம் D ஒப்புதலையும் ரத்தையும் தவறாகப் பொருத்துகிறது.",
        "Key Takeaway: Revocation by the President requires NO parliamentary approval for ANY emergency type!",
        "முக்கியக் குறிப்பு: எந்தவொரு அவசரநிலையாக இருந்தாலும், குடியரசுத் தலைவர் அதை ரத்து செய்வதற்குப் பாராளுமன்ற ஒப்புதல் தேவையில்லை!",
        "The Lok Sabha disapproval power applies ONLY to Article 352, not to Article 356 or 360.",
        "மக்களவையின் நிராகரிப்பு அதிகாரம் சரத்து 352-க்கு மட்டுமே பொருந்தும், சரத்து 356 அல்லது 360-க்கு அல்ல."
    ))

    # 018 - Key B: a-4, b-1, c-2, d-3
    qs.append(make_mf_q(
        18, "Special Majorities vs Simple Majorities",
        "Constitutional Action", "அரசியலமைப்பு நடவடிக்கை",
        ["Approval of Article 352", "Approval of Article 356", "Approval of Article 360", "Impeachment of President (Article 61)"],
        ["சரத்து 352-ற்கான ஒப்புதல்", "சரத்து 356-ற்கான ஒப்புதல்", "சரத்து 360-ற்கான ஒப்புதல்", "குடியரசுத் தலைவர் மீதான பதவி நீக்கம் (சரத்து 61)"],
        ["Simple Majority of each House present and voting (State)", "Simple Majority of each House present and voting (Financial)", "Two-thirds of total membership of each House", "Majority of total membership and 2/3 of members present and voting in each House"],
        ["ஒவ்வொரு அவையிலும் வருகை தந்து வாக்களிப்போரில் எளிய பெரும்பான்மை (மாநிலம்)", "ஒவ்வொரு அவையிலும் வருகை தந்து வாக்களிப்போரில் எளிய பெரும்பான்மை (நிதி)", "ஒவ்வொரு அவையின் மொத்த உறுப்பினர்களில் 2/3 பங்கு பெரும்பான்மை", "ஒவ்வொரு அவையின் மொத்த உறுப்பினர்களில் பெரும்பான்மை மற்றும் வருகை தந்து வாக்களிப்போரில் 2/3 பங்கு சிறப்புப் பெரும்பான்மை"],
        ["a-1, b-2, c-3, d-4", "a-4, b-1, c-2, d-3", "a-3, b-4, c-1, d-2", "a-2, b-3, c-4, d-1"],
        "B",
        "Approval of Art 352 = Majority of total membership + 2/3 present & voting (4); Approval of Art 356 = Simple Majority (1); Approval of Art 360 = Simple Majority (2); Impeachment = 2/3 of total membership (3).",
        "சரத்து 352 ஒப்புதல் = மொத்தத்தில் பெரும்பான்மை + 2/3 வருகை பெரும்பான்மை (4); சரத்து 356 ஒப்புதல் = எளிய பெரும்பான்மை (1); சரத்து 360 ஒப்புதல் = எளிய பெரும்பான்மை (2); பதவி நீக்கம் = மொத்த உறுப்பினர்களில் 2/3 பங்கு (3).",
        "Option A inverts voting standards.", "விருப்பம் A வாக்குத் தரங்களை மாற்றுகிறது.",
        "Option B is correct; accurately distinguishes every voting threshold in Indian constitutional law.", "விருப்பம் B சரியானது; இந்திய அரசியலமைப்பின் ஒவ்வொரு வாக்கு வரம்பையும் துல்லியமாக வேறுபடுத்துகிறது.",
        "Option C attributes impeachment majority to Article 352.", "விருப்பம் C பதவி நீக்க பெரும்பான்மையை சரத்து 352-உடன் இணைக்கிறது.",
        "Option D swaps Article 356 with Article 352.", "விருப்பம் D சரத்து 356 மற்றும் 352-ஐ மாற்றுகிறது.",
        "Majority Comparison: Article 352 is the only emergency requiring a special majority under the 44th Amendment Act.",
        "பெரும்பான்மை ஒப்பீடு: 44-வது திருத்தச் சட்டத்தின் கீழ் சிறப்புப் பெரும்பான்மை தேவைப்படும் ஒரே அவசரநிலை சரத்து 352 மட்டுமே.",
        "Article 61 impeachment majority (2/3 of total membership) is the most stringent majority prescribed in the Indian Constitution.",
        "சரத்து 61 பதவி நீக்க பெரும்பான்மையே (மொத்த உறுப்பினர்களில் 2/3) இந்திய அரசியலமைப்பிலேயே மிகக் கடுமையான பெரும்பான்மையாகும்."
    ))

    # 019 - Key C: a-2, b-3, c-4, d-1
    qs.append(make_mf_q(
        19, "Emergency Terminology and Source Concepts",
        "Concept / Term", "கருத்து / சொல்",
        ["Suspension of Fundamental Rights during Emergency", "Emergency Provisions Structure (Part XVIII)", "Cabinet Recommendation Requirement", "Federal to Unitary Shift without Amendment"],
        ["அவசரநிலையின் போது அடிப்படை உரிமைகள் இடைநிறுத்தம்", "அவசரநிலைப் பிரிவுகளின் கட்டமைப்பு (பகுதி XVIII)", "அமைச்சரவைப் பரிந்துரைத் தேவை", "திருத்தமின்றியே கூட்டாட்சி ஒற்றையாட்சியாக மாறுதல்"],
        ["Unique Feature of Indian Constitution (Dr. Ambedkar)", "Weimar Constitution of Germany", "Government of India Act, 1935", "44th Constitutional Amendment Act, 1978"],
        ["இந்திய அரசியலமைப்பின் தனித்துவமான அம்சம் (டாக்டர் அம்பேத்கர்)", "ஜெர்மனியின் வெய்மர் அரசியலமைப்பு", "இந்திய அரசுச் சட்டம், 1935", "1978-ன் 44-வது அரசியலமைப்பு திருத்தச் சட்டம்"],
        ["a-1, b-2, c-3, d-4", "a-3, b-4, c-1, d-2", "a-2, b-3, c-4, d-1", "a-4, b-1, c-2, d-3"],
        "C",
        "Suspension of Fundamental Rights was borrowed from Weimar Constitution of Germany (2); General Emergency structure came from GoI Act 1935 (3); Cabinet recommendation came from 44th CAA 1978 (4); Federal to unitary shift is unique feature described by Ambedkar (1).",
        "அடிப்படை உரிமைகள் இடைநிறுத்தம் ஜெர்மனியின் வெய்மர் அரசியலமைப்பிலிருந்து பெறப்பட்டது (2); பொதுவான கட்டமைப்பு 1935 இந்திய அரசுச் சட்டத்திலிருந்து வந்தது (3); அமைச்சரவைப் பரிந்துரை 1978-ன் 44-வது திருத்தத்தால் வந்தது (4); கூட்டாட்சி ஒற்றையாட்சியாக மாறுவது அம்பேத்கரால் விவரிக்கப்பட்ட தனித்துவமான அம்சம் (1).",
        "Option A gives incorrect sources.", "விருப்பம் A தவறான மூலங்களைத் தருகிறது.",
        "Option B swaps Weimar Constitution with GoI Act 1935.", "விருப்பம் B வெய்மர் அரசியலமைப்பையும் 1935 சட்டத்தையும் மாற்றுகிறது.",
        "Option C is correct; accurately identifies constitutional sources and origins.", "விருப்பம் C சரியானது; அரசியலமைப்பு மூலங்கள் மற்றும் தோற்றங்களைத் துல்லியமாக அடையாளம் காண்கிறது.",
        "Option D attributes 44th CAA to Ambedkar's speech.", "விருப்பம் D 44-வது திருத்தத்தை அம்பேத்கரின் உரையுடன் இணைக்கிறது.",
        "Sources Trap: Emergency Provisions generally = GoI Act 1935; Suspension of Fundamental Rights = Weimar Constitution of Germany.",
        "மூலங்கள் பொறி: பொதுவான அவசரநிலைப் பிரிவுகள் = 1935 இந்திய அரசுச் சட்டம்; அடிப்படை உரிமைகள் இடைநிறுத்தம் = ஜெர்மனியின் வெய்மர் அரசியலமைப்பு.",
        "Dr. B.R. Ambedkar stated: 'All federal systems including the American are placed in a tight mould of federalism. No matter what the circumstances, it cannot change its form. The Indian Constitution can be both unitary as well as federal.'",
        "டாக்டர் அம்பேத்கர் கூறினார்: 'அமெரிக்கா உட்பட அனைத்துக் கூட்டாட்சி அமைப்புகளும் கூட்டாட்சியின் இறுக்கமான கட்டமைப்பைக் கொண்டுள்ளன; சூழ்நிலை எதுவாக இருந்தாலும் அதன் வடிவத்தை மாற்ற முடியாது. ஆனால் இந்திய அரசியலமைப்பு ஒற்றையாட்சியாகவும் கூட்டாட்சியாகவும் இயங்கக்கூடியது.'"
    ))

    # 020 - Key D: a-3, b-4, c-2, d-1
    qs.append(make_mf_q(
        20, "Article 356 Frequency and State Milestones",
        "State / Event", "மாநிலம் / நிகழ்வு",
        ["First use of Article 356", "Use of Article 356 in 9 states simultaneously (1977)", "Use of Article 356 in 9 states simultaneously (1980)", "Longest single spell of Article 356 (1987–1992)"],
        ["சரத்து 356 முதன்முதலில் பயன்படுத்தப்பட்டது", "ஒரே நேரத்தில் 9 மாநிலங்களில் சரத்து 356 பயன்படுத்தப்பட்டது (1977)", "ஒரே நேரத்தில் 9 மாநிலங்களில் சரத்து 356 பயன்படுத்தப்பட்டது (1980)", "சரத்து 356-ன் மிக நீண்ட ஒற்றை ஆட்சிக் காலம் (1987-1992)"],
        ["Punjab (nearly 5 years continuous)", "Indira Gandhi Congress Government", "East Punjab (1951)", "Morarji Desai Janata Party Government"],
        ["பஞ்சாப் (கிட்டத்தட்ட 5 ஆண்டுகள் தொடர்ச்சியாக)", "இந்திரா காந்தி காங்கிரஸ் அரசு", "கிழக்கு பஞ்சாப் (1951)", "மொரார்ஜி தேசாய் ஜனதா கட்சி அரசு"],
        ["a-1, b-2, c-3, d-4", "a-2, b-1, c-4, d-3", "a-4, b-3, c-2, d-1", "a-3, b-4, c-2, d-1"],
        "D",
        "First use = East Punjab 1951 (3); 1977 dissolution of 9 states = Janata Party Govt (4); 1980 dissolution of 9 states = Indira Gandhi Govt (2); Longest spell = Punjab 1987-1992 (1).",
        "முதல் பயன்பாடு = கிழக்கு பஞ்சாப் 1951 (3); 1977-ல் 9 மாநிலங்கள் கலைப்பு = ஜனதா கட்சி அரசு (4); 1980-ல் 9 மாநிலங்கள் கலைப்பு = இந்திரா காந்தி அரசு (2); மிக நீண்ட காலம் = பஞ்சாப் 1987-1992 (1).",
        "Option A is incorrect.", "விருப்பம் A தவறானது.",
        "Option B swaps Janata and Indira Gandhi governments.", "விருப்பம் B ஜனதா மற்றும் இந்திரா காந்தி அரசுகளை மாற்றுகிறது.",
        "Option C attributes 1951 use to Punjab 5-year spell.", "விருப்பம் C 1951 பயன்பாட்டை 5 ஆண்டு காலத்துடன் இணைக்கிறது.",
        "Option D is correct; perfectly matches major political episodes in Article 356 history.", "விருப்பம் D சரியானது; சரத்து 356 வரலாற்றின் முக்கிய அரசியல் நிகழ்வுகளைச் சரியாகப் பொருத்துகிறது.",
        "Historic Tit-for-Tat: In 1977, Janata Govt dissolved 9 Congress state assemblies; in 1980, returning Congress Govt dissolved 9 opposition state assemblies.",
        "வரலாற்றுப் பழிவாங்கல்: 1977-ல் ஜனதா அரசு 9 காங்கிரஸ் சட்டமன்றங்களைக் கலைத்தது; 1980-ல் மீண்டும் வந்த காங்கிரஸ் அரசு 9 எதிர்க்கட்சி சட்டமன்றங்களைக் கலைத்தது.",
        "The Supreme Court in S.R. Bommai (1994) condemned this wholesale dissolution of state governments on political grounds.",
        "எஸ்.ஆர். பொம்மை (1994) வழக்கில் உச்ச நீதிமன்றம் அரசியல் காரணங்களுக்காக ஒட்டுமொத்தமாக மாநில அரசுகளைக் கலைக்கும் இந்த நடைமுறையைக் கடுமையாகக் கண்டித்தது."
    ))

    # 021 - Key A: a-2, b-1, c-4, d-3
    qs.append(make_mf_q(
        21, "Constituent Assembly Quotes on Emergency",
        "Constituent Assembly Speaker", "அரசியலமைப்பு நிர்ணய சபை உறுப்பினர்",
        ["Dr. B.R. Ambedkar", "H.V. Kamath", "Prof. K.T. Shah", "T.T. Krishnamachari"],
        ["டாக்டர் பி.ஆர். அம்பேத்கர்", "எச்.வி. காமத்", "பேராசிரியர் கே.டி. ஷா", "டி.டி. கிருஷ்ணமாச்சாரி"],
        ["Feared the creation of a 'Totalitarian State' and 'police raj'", "Hoped Article 356 would remain a 'dead letter'", "Defended provisions as constitutional safety valves to protect sovereignty", "Called emergency provisions a 'chapter of reaction and retrogression'"],
        ["ஒரு 'சர்வாதிகார அரசு' மற்றும் 'காவல்துறை ராஜ்ஜியம்' உருவாகும் என்று அஞ்சினார்", "சரத்து 356 ஒரு 'செயலற்ற எழுத்தாக' இருக்கும் என நம்பினார்", "இறைமையைப் பாதுகாக்கும் அரசியலமைப்பு பாதுகாப்பு வால்வுகளாக விதிகளை ஆதரித்தார்", "அவசரநிலைப் பிரிவுகளை 'பிற்போக்குத்தனமான மற்றும் பின்னடைவுக்கான அத்தியாயம்' என்று அழைத்தார்"],
        ["a-2, b-1, c-4, d-3", "a-1, b-2, c-3, d-4", "a-3, b-4, c-1, d-2", "a-4, b-3, c-2, d-1"],
        "A",
        "Dr. B.R. Ambedkar hoped it would remain a dead letter (2); H.V. Kamath feared a totalitarian police state (1); Prof. K.T. Shah called it a chapter of reaction and retrogression (4); T.T. Krishnamachari defended provisions as constitutional safety valves (3).",
        "டாக்டர் அம்பேத்கர் அது செயலற்ற எழுத்தாக இருக்கும் என நம்பினார் (2); எச்.வி. காமத் சர்வாதிகார காவல்துறை அரசை அஞ்சினார் (1); பேராசிரியர் கே.டி. ஷா பிற்போக்குத்தனமான அத்தியாயம் என்றார் (4); டி.டி. கிருஷ்ணமாச்சாரி பாதுகாப்பு வால்வாக ஆதரித்தார் (3).",
        "Option A is correct; captures the historic debates in the Constituent Assembly.", "விருப்பம் A சரியானது; அரசியலமைப்பு நிர்ணய சபையின் வரலாற்று விவாதங்களைச் சரியாகப் படம்பிடிக்கிறது.",
        "Option B swaps Ambedkar and Kamath.", "விருப்பம் B அம்பேத்கர் மற்றும் காமத்தை மாற்றுகிறது.",
        "Option C attributes Shah's criticism to Krishnamachari.", "விருப்பம் C ஷாவின் விமர்சனத்தை கிருஷ்ணமாச்சாரியுடன் இணைக்கிறது.",
        "Option D is in reverse order.", "விருப்பம் D தலைகீழ் வரிசையில் உள்ளது.",
        "Constituent Assembly Debates: H.V. Kamath remarked: 'I fear that by this single chapter we are seeking to lay the foundation of a totalitarian state.'",
        "அரசியலமைப்பு நிர்ணய சபை விவாதங்கள்: எச்.வி. காமத் கூறினார்: 'இந்த ஒற்றை அத்தியாயத்தின் மூலம் நாம் ஒரு சர்வாதிகார அரசிற்கு அடித்தளம் அமைக்க முயல்கிறோமோ என்று நான் அஞ்சுகிறேன்.'",
        "Dr. Ambedkar famously replied that the possibility of abuse of power cannot be an argument for the non-conferment of power.",
        "அதிகாரம் தவறாகப் பயன்படுத்தப்படலாம் என்ற சாத்தியக்கூறு அதிகாரத்தை வழங்காமல் இருப்பதற்கான காரணமாக அமைய முடியாது என்று டாக்டர் அம்பேத்கர் புகழ்பெற்ற பதிலளித்தார்."
    ))

    # 022 - Key B: a-3, b-4, c-1, d-2
    qs.append(make_mf_q(
        22, "Articles 358 vs 359 Comparative Matrix",
        "Feature / Attribute", "அம்சம் / பண்புக்கூறு",
        ["Scope of Rights Suspended", "Territorial Extent", "Mode of Operation", "Applicable Grounds"],
        ["இடைநிறுத்தப்படும் உரிமைகளின் வரம்பு", "பிராந்திய எல்லை", "செயல்படும் விதம்", "பொருந்தக்கூடிய காரணங்கள்"],
        ["Article 358 applies automatically; Article 359 requires Presidential Order", "Article 358 restricted to war/aggression; Article 359 applies to both external and internal", "Article 358 strictly limited to Article 19; Article 359 covers specified rights (excluding 20 & 21)", "Article 358 covers entire country; Article 359 may apply to whole or any part of India"],
        ["சரத்து 358 தானாகச் செயல்படுகிறது; சரத்து 359-க்கு குடியரசுத் தலைவர் ஆணை தேவை", "சரத்து 358 போர்/ஆக்கிரமிப்புக்கு மட்டுமே; சரத்து 359 வெளிப்புற மற்றும் உள்நாட்டு இரண்டிற்கும் பொருந்தும்", "சரத்து 358 சரத்து 19-க்கு மட்டுமே; சரத்து 359 குறிப்பிடப்பட்ட பிற உரிமைகளை உள்ளடக்கும் (20 மற்றும் 21 தவிர)", "சரத்து 358 நாடு முழுமைக்கும் பொருந்தும்; சரத்து 359 முழு நாட்டிற்கும் அல்லது பகுதிக்கும் பொருந்தலாம்"],
        ["a-1, b-2, c-3, d-4", "a-3, b-4, c-1, d-2", "a-2, b-1, c-4, d-3", "a-4, b-3, c-2, d-1"],
        "B",
        "Scope of rights: Art 358 is Art 19 only, Art 359 covers specified rights excluding 20-21 (3); Territorial extent: Art 358 is entire country, Art 359 can be whole or part (4); Mode of operation: Art 358 is automatic, Art 359 requires Presidential Order (1); Applicable grounds: Art 358 is external only, Art 359 is external and internal (2).",
        "உரிமைகளின் வரம்பு: 358 சரத்து 19 மட்டுமே, 359 பிற உரிமைகள் (3); எல்லை: 358 நாடு முழுவதும், 359 முழுமைக்கும் அல்லது பகுதிக்கும் (4); செயல்படும் விதம்: 358 தானாக, 359 ஆணை தேவை (1); காரணங்கள்: 358 வெளிப்புறம் மட்டுமே, 359 இரண்டும் (2).",
        "Option A inverts the comparative matrix.", "விருப்பம் A ஒப்பீட்டு அட்டவணையை மாற்றுகிறது.",
        "Option B is correct; captures every core distinction between Articles 358 and 359.", "விருப்பம் B சரியானது; சரத்துகள் 358 மற்றும் 359-க்கு இடையிலான அனைத்து முக்கிய வேறுபாடுகளையும் படம்பிடிக்கிறது.",
        "Option C confuses operational mode with territorial extent.", "விருப்பம் C செயல்பாட்டு முறையை பிராந்திய எல்லையுடன் குழப்புகிறது.",
        "Option D swaps grounds and scope.", "விருப்பம் D காரணங்களையும் வரம்பையும் மாற்றுகிறது.",
        "Laxmikanth Classic Distinction: Article 358 operates automatically throughout India for Art 19 during external emergency; Article 359 operates via Presidential Order for specified rights during both external and internal emergency.",
        "லட்சுமிகாந்த் ஒப்பீடு: சரத்து 358 வெளிப்புற அவசரநிலையின் போது இந்தியா முழுவதும் சரத்து 19-க்கு தானாகச் செயல்படும்; சரத்து 359 குடியரசுத் தலைவர் ஆணை மூலம் குறிப்பிட்ட உரிமைகளுக்கு வெளிப்புற மற்றும் உள்நாட்டு அவசரநிலை இரண்டிலும் செயல்படும்.",
        "Both articles mandate that only laws related to emergency and executive actions taken under such laws are protected from judicial challenge.",
        "அவசரநிலையுடன் தொடர்புடைய சட்டங்களும், அத்தகைய சட்டங்களின் கீழ் எடுக்கப்பட்ட நிர்வாக நடவடிக்கைகளும் மட்டுமே நீதித்துறை மறுஆய்விலிருந்து பாதுகாக்கப்படுகின்றன."
    ))

    # 023 - Key C: a-4, b-1, c-2, d-3
    qs.append(make_mf_q(
        23, "Tamil Nadu Article 356 Episodes",
        "Year of Article 356 in Tamil Nadu", "தமிழ்நாட்டில் சரத்து 356 அமல்படுத்தப்பட்ட ஆண்டு",
        ["January 1976", "February 1980", "January 1988", "February 1991"],
        ["ஜனவரி 1976", "பிப்ரவரி 1980", "ஜனவரி 1988", "பிப்ரவரி 1991"],
        ["M.G. Ramachandran (AIADMK) government dismissed by returning Indira Gandhi government", "Janaki Ramachandran government dismissed after assembly floor chaos following MGR's demise", "M. Karunanidhi (DMK) government dismissed on LTTE issue without Governor's report", "M. Karunanidhi (DMK) government dismissed during National Emergency"],
        ["மீண்டும் ஆட்சிக்கு வந்த இந்திரா காந்தி அரசால் எம்.ஜி. ராமச்சந்திரன் (அதிமுக) அரசு கலைக்கப்பட்டது", "எம்.ஜி.ஆர் மறைவுக்குப் பின் சட்டமன்றக் குழப்பத்தைத் தொடர்ந்து ஜானகி ராமச்சந்திரன் அரசு கலைக்கப்பட்டது", "ஆளுநர் அறிக்கை இன்றியே விடுதலைப் புலிகள் விவகாரத்தில் மு. கருணாநிதி (திமுக) அரசு கலைக்கப்பட்டது", "தேசிய அவசரநிலையின் போது மு. கருணாநிதி (திமுக) அரசு கலைக்கப்பட்டது"],
        ["a-1, b-2, c-3, d-4", "a-3, b-4, c-1, d-2", "a-4, b-1, c-2, d-3", "a-2, b-3, c-4, d-1"],
        "C",
        "1976 = DMK Govt dismissed during Emergency (4); 1980 = MGR Govt dismissed by Indira Gandhi (1); 1988 = Janaki Ramachandran Govt dismissed after MGR demise (2); 1991 = DMK Govt dismissed on LTTE issue without Governor report (3).",
        "1976 = அவசரநிலையின் போது திமுக அரசு கலைக்கப்பட்டது (4); 1980 = இந்திரா காந்தியால் எம்.ஜி.ஆர் அரசு கலைக்கப்பட்டது (1); 1988 = எம்.ஜி.ஆர் மறைவுக்குப் பின் ஜானகி அரசு கலைக்கப்பட்டது (2); 1991 = ஆளுநர் அறிக்கையின்றி திமுக அரசு கலைக்கப்பட்டது (3).",
        "Option A inverts Tamil Nadu political timeline.", "விருப்பம் A தமிழக அரசியல் காலவரிசையை மாற்றுகிறது.",
        "Option B confuses 1980 and 1988 episodes.", "விருப்பம் B 1980 மற்றும் 1988 நிகழ்வுகளைக் குழப்புகிறது.",
        "Option C is correct; directly tests high-yield TNPSC Group 1 / Group 2 questions on Tamil Nadu polity history.", "விருப்பம் C சரியானது; தமிழக அரசியல் வரலாறு குறித்த TNPSC குரூப் 1 / குரூப் 2 வினாக்களுக்கு நேரடி விடை.",
        "Option D swaps 1976 and 1991 dismissals.", "விருப்பம் D 1976 மற்றும் 1991 கலைப்புகளை மாற்றுகிறது.",
        "TNPSC High-Yield Fact: In 1991, Governor Surjit Singh Barnala refused to recommend the dismissal of the Karunanidhi ministry, so the Centre invoked Article 356 'otherwise' without a Governor's report!",
        "TNPSC உயர்-விளைச்சல் தகவல்: 1991-ல் ஆளுநர் சுர்ஜித் சிங் பர்னாலா கருணாநிதி அரசைக் கலைக்கப் பரிந்துரைக்க மறுத்ததால், மத்திய அரசு ஆளுநர் அறிக்கையின்றி 'பிற வழியில்' சரத்து 356-ஐப் பயன்படுத்தியது!",
        "Tamil Nadu has experienced Article 356 four times: 1976, 1980, 1988, and 1991.",
        "தமிழ்நாடு நான்கு முறை சரத்து 356-ஐ எதிர்கொண்டுள்ளது: 1976, 1980, 1988 மற்றும் 1991."
    ))

    # 024 - Key D: a-3, b-4, c-1, d-2
    qs.append(make_mf_q(
        24, "Effect of Article 356 on State Organs",
        "State Organ / Functionary", "மாநில அங்கம் / அலுவலர்",
        ["State Council of Ministers", "State Legislative Assembly", "State High Court", "State Consolidated Fund Expenditure"],
        ["மாநில அமைச்சரவை", "மாநில சட்டமன்றம்", "மாநில உயர் நீதிமன்றம்", "மாநிலத் தொகுப்பு நிதிச் செலவினம்"],
        ["Powers and jurisdiction completely untouched and unaffected", "Sanctioned by Parliament, or by President when Lok Sabha is not in session", "Dismissed by the President upon proclamation", "Suspended or dissolved by Presidential proclamation"],
        ["அதிகாரங்களும் அதிகார வரம்பும் முற்றிலும் தொடப்படாமல் மற்றும் பாதிக்கப்படாமல் உள்ளது", "பாராளுமன்றத்தால் அல்லது மக்களவை கூடாத போது குடியரசுத் தலைவரால் அனுமதிக்கப்படுகிறது", "பிரகடனப்படுத்தப்பட்டவுடன் குடியரசுத் தலைவரால் பதவி நீக்கம் செய்யப்படுகிறது", "குடியரசுத் தலைவர் பிரகடனத்தால் இடைநிறுத்தப்படுகிறது அல்லது கலைக்கப்படுகிறது"],
        ["a-1, b-2, c-3, d-4", "a-2, b-1, c-4, d-3", "a-4, b-3, c-2, d-1", "a-3, b-4, c-1, d-2"],
        "D",
        "State Council of Ministers = Dismissed by President (3); State Assembly = Suspended or dissolved (4); State High Court = Untouched and unaffected (1); Consolidated Fund = Sanctioned by Parliament or President under Art 357 (2).",
        "மாநில அமைச்சரவை = குடியரசுத் தலைவரால் பதவி நீக்கம் (3); சட்டமன்றம் = இடைநிறுத்தம் அல்லது கலைப்பு (4); உயர் நீதிமன்றம் = பாதிக்கப்படாமல் நீடித்தல் (1); தொகுப்பு நிதி = பாராளுமன்றம் அல்லது குடியரசுத் தலைவரால் அனுமதி (2).",
        "Option A is incorrect.", "விருப்பம் A தவறானது.",
        "Option B is incorrect.", "விருப்பம் B தவறானது.",
        "Option C claims High Court powers can be assumed by President.", "விருப்பம் C உயர் நீதிமன்ற அதிகாரங்களைக் குடியரசுத் தலைவர் எடுக்கலாம் எனக் கூறுகிறது.",
        "Option D is correct; accurately states the status of each organ under Article 356.", "விருப்பம் D சரியானது; சரத்து 356-ன் கீழ் ஒவ்வொரு அங்கத்தின் நிலையையும் துல்லியமாகக் குறிப்பிடுகிறது.",
        "Golden Rule: Article 356 does NOT affect the High Court. The President cannot assume any power of the High Court.",
        "பொன் விதி: சரத்து 356 உயர் நீதிமன்றத்தைப் பாதிக்காது. குடியரசுத் தலைவர் உயர் நீதிமன்றத்தின் எந்த அதிகாரத்தையும் தன்வசம் எடுக்க முடியாது.",
        "During President's Rule, the Governor carries on administration with the help of advisors appointed by the President.",
        "குடியரசுத் தலைவர் ஆட்சியின் போது, குடியரசுத் தலைவரால் நியமிக்கப்படும் ஆலோசகர்களின் உதவியுடன் ஆளுநர் நிர்வாகத்தை மேற்கொள்கிறார்."
    ))

    # 025 - Key B: a-2, b-3, c-4, d-1
    qs.append(make_mf_q(
        25, "Constitutional Remedies and Emergency Cases",
        "Case Law", "வழக்குச் சட்டம்",
        ["Makhan Singh v. State of Punjab (1964)", "Ghulam Sarwar v. UOI (1967)", "H.H. Maharajadhiraja v. UOI (1971)", "K.S. Puttaswamy v. UOI (2017)"],
        ["மக்கன் சிங் எதிர் பஞ்சாப் மாநிலம் (1964)", "குலாம் சர்வார் எதிர் மத்திய அரசு (1967)", "மாதவராவ் சிந்தியா / மன்னர் மானிய வழக்கு (1971)", "கே.எஸ். புட்டசுவாமி எதிர் மத்திய அரசு (2017)"],
        ["Affirmed privacy as fundamental right and formally overruled ADM Jabalpur", "Held that right to challenge detention on ground of ultra vires survives emergency", "Distinguished between challenge to emergency law and executive action beyond authority", "Privy purses abolition executive order declared unconstitutional"],
        ["தனியுரிமையை அடிப்படை உரிமையாக்கி ஏ.டி.எம். ஜபல்பூர் தீர்ப்பை முறைப்படி ரத்து செய்தது", "அதிகார வரம்பை மீறிய தடுப்புக் காவலை எதிர்க்கும் உரிமை அவசரநிலையிலும் நீடிக்கும் எனத் தீர்ப்பு", "அவசரக்கால சட்டத்தை எதிர்ப்பதற்கும் வரம்பை மீறிய நிர்வாக நடவடிக்கையை எதிர்ப்பதற்கும் இடையே வேறுபடுத்தியது", "மன்னர் மானியங்களை ரத்து செய்த நிர்வாக ஆணை அரசியலமைப்புக்கு முரணானது என அறிவிக்கப்பட்டது"],
        ["a-1, b-2, c-3, d-4", "a-2, b-3, c-4, d-1", "a-3, b-1, c-2, d-4", "a-4, b-3, c-1, d-2"],
        "B",
        "Makhan Singh (1964) held ultra vires detention challenges survive (2); Ghulam Sarwar (1967) distinguished law challenge from ultra vires executive action (3); Privy Purses (1971) struck down arbitrary presidential order (4); Puttaswamy (2017) formally overruled ADM Jabalpur (1).",
        "மக்கன் சிங் (1964) அதிகார மீறல் தடுப்புக் காவல் வழக்கை தொடரலாம் என்றது (2); குலாம் சர்வார் (1967) நிர்வாக அத்துமீறலை வேறுபடுத்தியது (3); மன்னர் மானிய வழக்கு (1971) தன்னிச்சையான குடியரசுத் தலைவர் ஆணையை ரத்து செய்தது (4); புட்டசுவாமி (2017) ஏ.டி.எம். ஜபல்பூர் தீர்ப்பை ரத்து செய்தது (1).",
        "Option A is incorrect in its pairings.", "விருப்பம் A பொருத்தலில் தவறானது.",
        "Option B is correct; accurately pairs advanced constitutional jurisprudence with case holdings.", "விருப்பம் B சரியானது; மேம்பட்ட அரசியலமைப்புச் சட்டத் தீர்ப்புகளை துல்லியமாகப் பொருத்துகிறது.",
        "Option C mismatches Puttaswamy with Makhan Singh.", "விருப்பம் C புட்டசுவாமி வழக்கை மக்கன் சிங்குடன் குழப்புகிறது.",
        "Option D gives erroneous order.", "விருப்பம் D தவறான வரிசையைத் தருகிறது.",
        "Historic Overruling: In Puttaswamy (2017), the 9-judge bench declared: 'The judgments rendered by all four judges in the majority in ADM Jabalpur are seriously flawed and are expressly overruled.'",
        "வரலாற்று ரத்து: புட்டசுவாமி (2017) வழக்கில் 9 நீதிபதிகள் கொண்ட அமர்வு: 'ஏ.டி.எம். ஜபல்பூர் வழக்கில் பெரும்பான்மை அளித்த 4 நீதிபதிகளின் தீர்ப்புகளும் கடுமையான குறைபாடுடையவை மற்றும் அவை வெளிப்படையாக ரத்து செய்யப்படுகின்றன' என்று அறிவித்தது.",
        "Justice D.Y. Chandrachud formally overruled the judgment authored by his father, Justice Y.V. Chandrachud, in ADM Jabalpur.",
        "ஏ.டி.எம். ஜபல்பூர் வழக்கில் தனது தந்தை நீதிபதி ஒய்.வி. சந்திரசூட் வழங்கிய தீர்ப்பை, நீதிபதி டி.ஒய். சந்திரசூட் புட்டசுவாமி வழக்கில் முறைப்படி ரத்து செய்தார்."
    ))

    return qs

print("Match the following questions ready.")
