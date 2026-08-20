# -*- coding: utf-8 -*-
"""
Master Upgraded Notes Builder for Fundamental Rights – Part 2 (Bilingual)
Subject: Indian Polity
Topic: Fundamental Rights – Part 2 (Part 2 of 3)
Target Output: data/notes/polity/fundamental_rights_part_2.json
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

notes_data = {
  "meta": {
    "topic_id": "polity_fundamental_rights_part_2",
    "repository_id": "polity_fundamental_rights",
    "display_title": "Fundamental Rights – Part 2",
    "part": 2,
    "total_parts": 3,
    "subject": "polity",
    "chapter": "Fundamental Rights",
    "language": "English + Tamil"
  },
  "metadata": {
    "version": "2.0",
    "status": "approved",
    "review_status": "gold_standard",
    "difficulty": "foundation",
    "estimated_study_time": {
      "reading": "40 min",
      "revision": "15 min",
      "total": "55 min"
    }
  },
  "keywords": [
    "Right to Freedom",
    "சுதந்திர உரிமை",
    "Article 19 Six Freedoms",
    "உறுப்பு 19 ஆறு சுதந்திரங்கள்",
    "Reasonable Restrictions",
    "நியாயமான கட்டுப்பாடுகள்",
    "Article 20 Conviction Protection",
    "உறுப்பு 20 குற்றச்சாட்டுகளிலிருந்து பாதுகாப்பு",
    "Ex-Post-Facto Law",
    "முந்தைய தேதியிட்ட குற்றவியல் சட்டம்",
    "Double Jeopardy",
    "இரட்டை தண்டனைத் தடை",
    "Self-Incrimination",
    "தனக்குத்தானே எதிரான சாட்சியத் தடை",
    "Article 21 Life and Personal Liberty",
    "உறுப்பு 21 வாழ்வு மற்றும் தனிநபர் சுதந்திரம்",
    "Procedure Established by Law",
    "சட்டத்தால் நிறுவப்பட்ட நடைமுறை",
    "Due Process of Law",
    "சட்டத்தின் உரிய நடைமுறை",
    "Right to Privacy Puttaswamy Case",
    "தனிமனித ரகசிய உரிமை புட்டசுவாமி வழக்கு",
    "Article 21A Right to Education 86th Amendment",
    "உறுப்பு 21A கல்வி உரிமை 86வது திருத்தம்",
    "Article 22 Protection Against Arrest",
    "உறுப்பு 22 கைது மற்றும் தடுப்புக் காவலில் பாதுகாப்பு",
    "Punitive vs Preventive Detention",
    "தண்டனைக்காவல் vs தடுப்புக் காவல்",
    "Article 23 Traffic in Human Beings Begar",
    "உறுப்பு 23 மனித வியாபாரம் வெட்டி வேலை தடை",
    "Article 24 Child Labour Prohibition",
    "உறுப்பு 24 குழந்தை தொழிலாளர் தடை"
  ],
  "learning_outcomes": {
    "Understand": {
      "en": [
        "Understand the six fundamental freedoms guaranteed to citizens under Article 19 and their specific constitutional limitation grounds.",
        "Understand the three criminal justice protections under Article 20: No Ex-Post-Facto Law, No Double Jeopardy, and No Self-Incrimination.",
        "Understand Article 21, the evolution from 'Procedure Established by Law' to 'Due Process of Law', and expanded rights like Privacy.",
        "Understand Article 21A (Right to Education for 6-14 years), Article 22 (Arrest & Preventive Detention), and Articles 23-24 (Right Against Exploitation)."
      ],
      "ta": [
        "உறுப்பு 19-ன் கீழ் குடிமக்களுக்கு உத்தரவாதம் அளிக்கப்பட்ட ஆறு அடிப்படை சுதந்திரங்களையும் அவற்றின் குறிப்பிட்ட அரசியலமைப்பு கட்டுப்பாட்டு அடிப்படைகளையும் புரிந்து கொள்ளுதல்.",
        "உறுப்பு 20-ன் கீழ் மூன்று குற்றவியல் நீதிப் பாதுகாப்புகளைப் புரிந்து கொள்ளுதல்: முந்தைய தேதியிட்ட சட்டத் தடை, இரட்டை தண்டனைத் தடை மற்றும் தனக்குத்தானே எதிரான சாட்சியத் தடை.",
        "உறுப்பு 21, 'சட்டத்தால் நிறுவப்பட்ட நடைமுறை'யிலிருந்து 'சட்டத்தின் உரிய நடைமுறை'க்கான வளர்ச்சி மற்றும் தனிமனித ரகசியம் போன்ற விரிவுபடுத்தப்பட்ட உரிமைகளைப் புரிந்து கொள்ளுதல்.",
        "உறுப்பு 21A (6-14 வயதுக் கல்வி உரிமை), உறுப்பு 22 (கைது & தடுப்புக் காவல்) மற்றும் உறுப்புகள் 23-24 (சுரண்டலுக்கு எதிரான உரிமை) ஆகியவற்றைப் புரிந்து கொள்ளுதல்."
      ]
    },
    "Remember": {
      "en": [
        "Remember that Article 19 freedoms are available ONLY to Citizens of India.",
        "Remember that Article 20 protection against ex-post-facto laws applies ONLY to criminal laws, not civil liabilities.",
        "Remember that Article 21A was added by the 86th Constitutional Amendment Act, 2002 for children aged 6 to 14 years.",
        "Remember that Article 22 preventive detention without Advisory Board approval is capped at 3 months.",
        "Remember that Article 23 prohibits begar/forced labour/human trafficking, and Article 24 prohibits child labour below 14 years in hazardous work."
      ],
      "ta": [
        "உறுப்பு 19 சுதந்திரங்கள் இந்தியக் குடிமக்களுக்கு மட்டுமே கிடைக்கக்கூடியவை என்பதை நினைவில் கொள்ளுதல்.",
        "உறுப்பு 20 முந்தைய தேதியிட்ட சட்டப் பாதுகாப்பு குற்றவியல் சட்டங்களுக்கு மட்டுமே பொருந்தும், சிவில் சட்டங்களுக்கு அல்ல என்பதை நினைவில் கொள்ளுதல்.",
        "உறுப்பு 21A 6 முதல் 14 வயது வரையிலான குழந்தைகளுக்கு 2002-ன் 86வது திருத்தச் சட்டத்தால் சேர்க்கப்பட்டது என்பதை நினைவில் கொள்ளுதல்.",
        "உறுப்பு 22 ஆலோசனை வாரிய ஒப்புதலின்றி தடுப்புக் காவல் அதிகபட்சமாக 3 மாதங்கள் மட்டுமே இருக்க முடியும் என்பதை நினைவில் கொள்ளுதல்.",
        "உறுப்பு 23 மனித வியாபாரம்/வெட்டி வேலை/கட்டாய வேலையைத் தடுக்கிறது, உறுப்பு 24 ஆபத்தான வேலையில் 14 வயதுக்குட்பட்ட குழந்தை தொழிலாளர்களைத் தடுக்கிறது என்பதை நினைவில் கொள்ளுதல்."
      ]
    },
    "Analyze": {
      "en": [
        "Analyze the distinction between 'Procedure Established by Law' (A.K. Gopalan 1950) and 'Due Process of Law' (Maneka Gandhi 1978).",
        "Analyze the crucial operational differences between Punitive Detention (post-trial) and Preventive Detention (suspicion-based).",
        "Analyze the distinction between Begar (unpaid work), Forced Labour (compelled work), and Human Trafficking under Article 23."
      ],
      "ta": [
        "'சட்டத்தால் நிறுவப்பட்ட நடைமுறை' (ஏ.கே. கோபாலன் 1950) மற்றும் 'சட்டத்தின் உரிய நடைமுறை' (மேனகா காந்தி 1978) இடையேயான வேறுபாட்டை பகுப்பாய்வு செய்தல்.",
        "தண்டனைக்காவல் (விசாரணைக்குப் பின்) மற்றும் தடுப்புக் காவல் (சந்தேகத்தின் பேரில்) இடையேயான செயல்பாட்டு வேறுபாடுகளை பகுப்பாய்வு செய்தல்.",
        "உறுப்பு 23-ன் கீழ் வெட்டி வேலை (ஊதியமில்லா வேலை), கட்டாய வேலை மற்றும் மனித வியாபாரம் இடையேயான வேறுபாட்டை பகுப்பாய்வு செய்தல்."
      ]
    },
    "Apply": {
      "en": [
        "Identify TNPSC trap points regarding Article 19 citizen availability, Article 20 double jeopardy tribunals, and Article 22 24-hour travel time exclusion.",
        "Apply constitutional rules to distinguish between Article 21A (educational entitlement) and Article 24 (child labor prohibition)."
      ],
      "ta": [
        "உறுப்பு 19 குடிமக்கள் தகுதி, உறுப்பு 20 இரட்டை தண்டனை தீர்ப்பாயங்கள் மற்றும் உறுப்பு 22 24-மணி நேர பயண நேர விலக்கு பற்றிய டிஎன்பிஎஸ்சி பொறி புள்ளிகளைக் கண்டறிதல்.",
        "உறுப்பு 21A (கல்வி உரிமை) மற்றும் உறுப்பு 24 (குழந்தை தொழிலாளர் தடை) ஆகியவற்றை வேறுபடுத்த அரசியலமைப்பு விதிகளைப் பயன்படுத்துதல்."
      ]
    }
  },
  "subject": "Polity",
  "topic": "Fundamental Rights – Part 2",
  "language": "bilingual",
  "ui_type": "polity",
  "sections": [
    {
      "id": "sec_article_19",
      "title_en": "1. Article 19: Six Fundamental Freedoms & Citizen Scope",
      "title_ta": "1. உறுப்பு 19: ஆறு அடிப்படை சுதந்திரங்களும் குடிமக்கள் எல்லையும்",
      "type": "standard_topic"
    },
    {
      "id": "sec_reasonable_restrictions",
      "title_en": "2. Reasonable Restrictions under Article 19",
      "title_ta": "2. உறுப்பு 19-ன் கீழ் நியாயமான கட்டுப்பாடுகள்",
      "type": "standard_topic"
    },
    {
      "id": "sec_article_20",
      "title_en": "3. Article 20: Protection in Respect of Conviction for Offences",
      "title_ta": "3. உறுப்பு 20: குற்றச்சாட்டுகளிலிருந்து தண்டனைப் பாதுகாப்பு",
      "type": "standard_topic"
    },
    {
      "id": "sec_article_21",
      "title_en": "4. Article 21: Protection of Life and Personal Liberty",
      "title_ta": "4. உறுப்பு 21: வாழ்வு மற்றும் தனிநபர் சுதந்திரப் பாதுகாப்பு",
      "type": "standard_topic"
    },
    {
      "id": "sec_article_21a",
      "title_en": "5. Article 21A: Right to Education (86th Amendment Act 2002)",
      "title_ta": "5. உறுப்பு 21A: கல்வி உரிமை (86வது திருத்தச் சட்டம் 2002)",
      "type": "standard_topic"
    },
    {
      "id": "sec_article_22",
      "title_en": "6. Article 22: Protection Against Arrest & Ordinary Detention",
      "title_ta": "6. உறுப்பு 22: கைது மற்றும் சாதாரண தடுப்புக் காவலில் பாதுகாப்பு",
      "type": "standard_topic"
    },
    {
      "id": "sec_preventive_detention",
      "title_en": "7. Preventive Detention & Constitutional Safeguards",
      "title_ta": "7. தடுப்புக் காவலும் அரசியலமைப்புப் பாதுகாப்புகளும்",
      "type": "standard_topic"
    },
    {
      "id": "sec_article_23",
      "title_en": "8. Article 23: Prohibition of Traffic in Human Beings & Forced Labour",
      "title_ta": "8. உறுப்பு 23: மனித வியாபாரம் மற்றும் கட்டாய வேலை தடை",
      "type": "standard_topic"
    },
    {
      "id": "sec_article_24",
      "title_en": "9. Article 24: Prohibition of Employment of Children in Hazardous Work",
      "title_ta": "9. உறுப்பு 24: ஆபத்தான பணிகளில் குழந்தை தொழிலாளர்கள் வேலைவாய்ப்பு தடை",
      "type": "standard_topic"
    },
    {
      "id": "sec_case_laws_part2",
      "title_en": "10. Landmark Judicial Case Laws (Part 2 Focus)",
      "title_ta": "10. முக்கிய மைல்கல் வழக்கு தீர்ப்புகள் (பகுதி 2)",
      "type": "standard_topic"
    },
    {
      "id": "sec_traps_connections_part2",
      "title_en": "11. TNPSC Traps, Cross-Topic Connections & High-Yield Revision",
      "title_ta": "11. டிஎன்பிஎஸ்சி பொறிகள், பாடத் தொடர்புகள் & முக்கிய திருப்புதல்",
      "type": "standard_topic"
    }
  ],
  "content": {
    "definition": {
      "en": "Fundamental Rights – Part 2 encompasses the 'Right to Freedom' (Articles 19 to 22) and the 'Right Against Exploitation' (Articles 23 to 24). It guarantees democratic freedoms of speech, assembly, association, movement, residence, and profession (Article 19), essential criminal safeguards against retroactive penalties and self-incrimination (Article 20), expansive protection of life, privacy, and personal liberty (Article 21), compulsory education for children (Article 21A), safeguards against arbitrary arrest and preventive detention (Article 22), and absolute prohibitions against human trafficking, begar, forced labour, and child employment in hazardous industries (Articles 23-24).",
      "ta": "அடிப்படை உரிமைகள் – பகுதி 2 என்பது 'சுதந்திர உரிமை' (உறுப்புகள் 19 முதல் 22 வரை) மற்றும் 'சுரண்டலுக்கு எதிரான உரிமை' (உறுப்புகள் 23 முதல் 24 வரை) ஆகியவற்றை உள்ளடக்கியது. இது பேச்சு, கூட்டம், சங்கம், இயக்கம், வசிப்பிடம், தொழில் ஆகியவற்றின் ஜனநாயக சுதந்திரங்களையும் (உறுப்பு 19), முந்தைய தேதியிட்ட தண்டனைகள் மற்றும் தனக்குத்தானே எதிரான சாட்சியத்திற்கு எதிரான குற்றவியல் பாதுகாப்புகளையும் (உறுப்பு 20), வாழ்வு, தனிமனித ரகசியம் மற்றும் தனிநபர் சுதந்திரத்தின் விரிவான பாதுகாப்பையும் (உறுப்பு 21), குழந்தைகளுக்கான கட்டாயக் கல்வியையும் (உறுப்பு 21A), தன்னிச்சையான கைது மற்றும் தடுப்புக் காவலுக்கு எதிரான பாதுகாப்புகளையும் (உறுப்பு 22), மற்றும் மனித வியாபாரம், வெட்டி வேலை, கட்டாய வேலை, ஆபத்தான தொழில்களில் குழந்தை வேலைவாய்ப்பு ஆகியவற்றிற்கு எதிரான முழுமையான தடைகளையும் (உறுப்புகள் 23-24) உத்தரவாதம் செய்கிறது."
    },
    "introduction": {
      "en": "Part 2 of the Fundamental Rights series provides an exhaustive TNPSC Group 1 level study of Articles 19 through 24. It dissects the six freedoms under Article 19 and their specific constitutional limitation grounds, criminal trial guarantees under Article 20, the transformative expansion of Article 21 from Gopalan to Maneka Gandhi and Puttaswamy, the 86th Amendment RTE framework under Article 21A, the dual framework of punitive vs preventive detention under Article 22, and the absolute anti-exploitation protections under Articles 23 and 24.",
      "ta": "அடிப்படை உரிமைகள் தொடரின் பகுதி 2, உறுப்புகள் 19 முதல் 24 வரையிலான விரிவான டிஎன்பிஎஸ்சி குரூப் 1 நிலை ஆய்வை வழங்குகிறது. இது உறுப்பு 19-ன் கீழ் உள்ள ஆறு சுதந்திரங்கள் மற்றும் அவற்றின் குறிப்பிட்ட அரசியலமைப்பு கட்டுப்பாட்டு அடிப்படைகள், உறுப்பு 20-ன் கீழ் குற்றவியல் விசாரணை உத்தரவாதங்கள், கோபாலன் முதல் மேனகா காந்தி மற்றும் புட்டசுவாமி வரை உறுப்பு 21-ன் மாற்றத்தக்க வளர்ச்சி, உறுப்பு 21A-ன் கீழ் 86வது திருத்த RTE கட்டமைப்பு, உறுப்பு 22-ன் கீழ் தண்டனைக்காவல் vs தடுப்புக் காவளின் இரட்டைக் கட்டமைப்பு, மற்றும் உறுப்புகள் 23 மற்றும் 24-ன் கீழ் சுரண்டலுக்கு எதிரான முழுமையான பாதுகாப்புகள் ஆகியவற்றை ஆழமாக விளக்குகிறது."
    },
    "sec_article_19": [
      {
        "title": "1. Article 19 Overview & Citizen Scope (உறுப்பு 19 கண்ணோட்டமும் குடிமக்கள் எல்லையும்)",
        "points": {
          "en": [
            "Article 19 Core Guarantee: Guarantees six fundamental freedoms to all citizens of India. It is considered the backbone of democratic liberties.",
            "AVAILABLE TO CITIZENS ONLY: Article 19 rights are available ONLY to citizens of India and shareholders of Indian companies. They are NOT available to foreigners, non-citizens, or legal entities like corporations.",
            "Original vs Present Count: Originally contained SEVEN freedoms. Article 19(1)(f) [Right to acquire, hold and dispose of property] was deleted by the 44th Constitutional Amendment Act, 1978. Present count: SIX Freedoms.",
            "Protects Against State Action: Article 19 protects against arbitrary State action, NOT against private individuals."
          ],
          "ta": [
            "உறுப்பு 19 முதன்மை உத்தரவாதம்: இந்தியாவின் அனைத்துக் குடிமக்களுக்கும் ஆறு அடிப்படை சுதந்திரங்களை உத்தரவாதம் செய்கிறது. இது ஜனநாயக சுதந்திரங்களின் முதுகெலும்பாகக் கருதப்படுகிறது.",
            "குடிமக்களுக்கு மட்டுமே கிடைக்கும்: உறுப்பு 19 உரிமைகள் இந்தியக் குடிமக்களுக்கு மட்டுமே கிடைக்கக்கூடியவை. இவை வெளிநாட்டினருக்கோ அல்லது கார்ப்பரேஷன்கள் போன்ற சட்டப்பூர்வ அமைப்புகளுக்கோ கிடைக்காது.",
            "அசல் vs தற்போதைய எண்ணிக்கை: ஆரம்பத்தில் 7 சுதந்திரங்களைக் கொண்டிருந்தது. உறுப்பு 19(1)(f) (சொத்துரிமை) 1978-ன் 44வது அரசியலமைப்பு திருத்தச் சட்டத்தால் நீக்கப்பட்டது. தற்போதைய எண்ணிக்கை: 6 சுதந்திரங்கள்.",
            "அரசு நடவடிக்கைக்கு மட்டுமே பாதுகாப்பு: உறுப்பு 19 அரசின் தன்னிச்சையான நடவடிக்கைக்கு எதிராக மட்டுமே பாதுகாக்கிறது, தனியார் நபர்களுக்கு எதிராக அல்ல."
          ]
        }
      },
      {
        "title": "2. Six Freedoms Detailed Analysis (ஆறு சுதந்திரங்களின் விரிவான பகுப்பாய்வு)",
        "points": {
          "en": [
            "1. Article 19(1)(a) – Freedom of Speech and Expression:\n  - Meaning: Right to express one's convictions and opinions freely by word of mouth, writing, printing, picture, or any other mode.\n  - Implied Rights Included: Freedom of Press, Freedom of Commercial Advertisements, Right to Telecast, Right to Silence (not to speak), Right to Know about government activities.\n  - Limitations: Subject to reasonable restrictions under Article 19(2).\n\n2. Article 19(1)(b) – Freedom of Peaceful Assembly:\n  - Meaning: Right to assemble peacefully and WITHOUT ARMS in public places.\n  - Includes: Right to hold public meetings, demonstrations, and processions.\n  - Does NOT include: Right to strike, violent assembly, or assembly on private property.\n\n3. Article 19(1)(c) – Freedom of Association & Cooperative Societies:\n  - Meaning: Right to form associations, unions, political parties, companies, partnership firms, societies, or trade unions.\n  - 97th Amendment Act 2011: Added 'cooperative societies' to Article 19(1)(c).\n  - Does NOT include: Right to compel recognition of a union or right to strike.\n\n4. Article 19(1)(d) – Freedom of Movement:\n  - Meaning: Right to move freely throughout the territory of India.\n  - Internal Movement: Art 19(1)(d) protects INTERNAL movement within India; EXTERNAL movement abroad is protected under Article 21 (Maneka Gandhi Case).\n\n5. Article 19(1)(e) – Freedom of Residence:\n  - Meaning: Right to reside and settle in any part of the territory of India (temporary residence or permanent settlement).\n\n6. Article 19(1)(g) – Freedom of Profession, Trade, Occupation, Business:\n  - Meaning: Right to practise any profession, or carry on any occupation, trade, or business.\n  - Does NOT include: Right to carry on immoral or dangerous trade (e.g. trafficking, gambling, dangerous explosives)."
          ],
          "ta": [
            "1. உறுப்பு 19(1)(a) – பேச்சு மற்றும் கருத்து வெளிப்பாட்டு சுதந்திரம்:\n  - பொருள்: வாய்மொழி, எழுத்து, அச்சு, படம் அல்லது வேறு எந்த முறையிலும் தனது கருத்துக்களை சுதந்திரமாக வெளிப்படுத்தும் உரிமை.\n  - உள்ளடங்கிய மறைமுக உரிமைகள்: பத்திரிகை சுதந்திரம், வணிக விளம்பர சுதந்திரம், ஒளிபரப்பு உரிமை, அமைதி காக்கும் உரிமை (பேசாமல் இருப்பது), அரசு நடவடிக்கைகள் பற்றி அறியும் உரிமை.\n  - கட்டுப்பாடுகள்: உறுப்பு 19(2)-ன் கீழ் நியாயமான கட்டுப்பாடுகளுக்கு உட்பட்டது.\n\n2. உறுப்பு 19(1)(b) – ஆயுதமின்றி அமைதியாகக் கூடும் சுதந்திரம்:\n  - பொருள்: பொது இடங்களில் ஆயுதங்களின்றி அமைதியாகக் கூடும் உரிமை.\n  - உள்ளடங்கியவை: பொதுக்கூட்டங்கள், ஆர்ப்பாட்டங்கள், ஊர்வலங்கள் நடத்தும் உரிமை.\n  - உள்ளடங்காதவை: வேலைநிறுத்தம் செய்யும் உரிமை, வன்முறை கூட்டம், தனியார் சொத்தில் கூடுதல்.\n\n3. உறுப்பு 19(1)(c) – சங்கங்கள் மற்றும் கூட்டுறவு சங்கங்கள் அமைக்கும் சுதந்திரம்:\n  - பொருள்: சங்கங்கள், தொழிற்சங்கங்கள், அரசியல் கட்சிகள், நிறுவனங்கள், கூட்டுறவு சங்கங்களை அமைக்கும் உரிமை.\n  - 97வது திருத்தச் சட்டம் 2011: உறுப்பு 19(1)(c)-ல் 'கூட்டுறவு சங்கங்கள்' என்பதைச் சேர்த்தது.\n  - உள்ளடங்காதவை: தொழிற்சங்க அங்கீகாரத்தைக் கட்டாயப்படுத்தும் உரிமை அல்லது வேலைநிறுத்த உரிமை.\n\n4. உறுப்பு 19(1)(d) – இந்திய நிலப்பரப்பு முழுவதும் சுதந்திரமாக நடமாடும் சுதந்திரம்:\n  - பொருள்: இந்தியாவின் நிலப்பரப்பு முழுவதும் சுதந்திரமாக நடமாடும் உரிமை.\n  - உள்நாட்டு இயக்கம்: உறுப்பு 19(1)(d) இந்தியாவிற்குள் உள்நாட்டு இயக்கத்தைப் பாதுகாக்கிறது; வெளிநாட்டிற்குச் செல்லும் இயக்கம் உறுப்பு 21-ன் கீழ் பாதுகாக்கப்படுகிறது (மேனகா காந்தி வழக்கு).\n\n5. உறுப்பு 19(1)(e) – வசிக்கும் மற்றும் குடியேறும் சுதந்திரம்:\n  - பொருள்: இந்தியாவின் எந்தப் பகுதியிலும் தற்காலிகமாக வசிக்கும் அல்லது நிரந்தரமாகக் குடியேறும் உரிமை.\n\n6. உறுப்பு 19(1)(g) – தொழில், வியாபாரம் செய்யும் சுதந்திரம்:\n  - பொருள்: எந்தவொரு தொழிலையும் செய்ய அல்லது எந்தவொரு வியாபாரத்தையும் நடத்த உரிமை.\n  - உள்ளடங்காதவை: ஒழுக்கக்கேடான அல்லது ஆபத்தான வர்த்தகம் (எ.கா. மனித வியாபாரம், சூதாட்டம், ஆபத்தான வெடிபொருட்கள்)."
          ]
        }
      }
    ],
    "sec_reasonable_restrictions": [
      {
        "title": "1. Constitutional Permissibility & Specific Grounds (நியாயமான கட்டுப்பாடுகளின் அடிப்படைகள்)",
        "points": {
          "en": [
            "Freedoms are NOT Absolute: The freedoms guaranteed under Article 19 are qualified and subject to 'reasonable restrictions' imposed by law under clauses (2) to (6).",
            "Must be Imposed by LAW: Restrictions cannot be imposed by mere executive order; they must have statutory authority.",
            "Judicial Review of Reasonability: The Supreme Court and High Courts determine whether a restriction is 'reasonable'. Reasonability considers the strike of balance between individual freedom and social interest.",
            "Specific Grounds per Freedom:\n- Art 19(1)(a) Grounds (Art 19(2)): 1. Sovereignty and integrity of India, 2. Security of the State, 3. Friendly relations with foreign States, 4. Public order, 5. Decency or morality, 6. Contempt of court, 7. Defamation, 8. Incitement to an offence. (Total 8 grounds!)\n- Art 19(1)(b) Grounds (Art 19(3)): Sovereignty & integrity of India, Public order.\n- Art 19(1)(c) Grounds (Art 19(4)): Sovereignty & integrity of India, Public order, Morality.\n- Art 19(1)(d) & (e) Grounds (Art 19(5)): 1. Interests of the general public, 2. Protection of interests of any Scheduled Tribe (to protect tribal culture, language, and land).\n- Art 19(1)(g) Grounds (Art 19(6)): 1. Interests of general public, 2. Prescribing professional/technical qualifications, 3. State monopoly over any trade/industry.",
            "TNPSC Trap: The grounds of reasonable restrictions differ for each freedom. For example, 'Protection of Scheduled Tribes' applies to Movement and Residence (19(1)(d) & (e)), NOT to Speech (19(1)(a))."
          ],
          "ta": [
            "சுதந்திரங்கள் வரம்பற்றவை அல்ல: உறுப்பு 19-ன் கீழ் உத்தரவாதம் அளிக்கப்பட்ட சுதந்திரங்கள் தகுதி வாய்ந்தவை மற்றும் விclauseகள் (2) முதல் (6) வரை சட்டத்தால் விதிக்கப்படும் 'நியாயமான கட்டுப்பாடுகளுக்கு' உட்பட்டவை.",
            "சட்டத்தால் விதிக்கப்பட வேண்டும்: வெறுமனே நிர்வாக ஆணையால் கட்டுப்பாடுகளை விதிக்க முடியாது; அவை சட்டப்பூர்வ அதிகாரத்தைக் கொண்டிருக்க வேண்டும்.",
            "நியாயத்தன்மையின் நீதித்துறை ஆய்வு: ஒரு கட்டுப்பாடு 'நியாயமானதா' என்பதை உச்ச நீதிமன்றமும் உயர் நீதிமன்றங்களும் தீர்மானிக்கின்றன.",
            "ஒவ்வொரு சுதந்திரத்திற்குமான குறிப்பிட்ட அடிப்படைகள்:\n- 19(1)(a) அடிப்படைகள் (19(2)): 1. இந்தியாவின் இறையாண்மை மற்றும் ஒருமைப்பாடு, 2. அரசின் பாதுகாப்பு, 3. வெளிநாடுகளுடனான நட்பு உறவுகள், 4. பொது ஒழுங்கு, 5. ஒழுக்கம் அல்லது மொராலிட்டி, 6. நீதிமன்ற அவமதிப்பு, 7. அவதூறு, 8. குற்றத் தூண்டுதல். (மொத்தம் 8 அடிப்படைகள்!)\n- 19(1)(b) அடிப்படைகள் (19(3)): இறையாண்மை & ஒருமைப்பாடு, பொது ஒழுங்கு.\n- 19(1)(c) அடிப்படைகள் (19(4)): இறையாண்மை & ஒருமைப்பாடு, பொது ஒழுங்கு, ஒழுக்கம்.\n- 19(1)(d) & (e) அடிப்படைகள் (19(5)): 1. பொதுமக்களின் நலன், 2. பழங்குடியினரின் (ST) நலன்களைப் பாதுகாத்தல்.\n- 19(1)(g) அடிப்படைகள் (19(6)): 1. பொதுமக்களின் நலன், 2. தொழிற்கல்வித் தகுதிகள், 3. வர்த்தகத்தில் அரசு முற்றுரிமை.",
            "டிஎன்பிஎஸ்சி பொறி: நியாயமான கட்டுப்பாடுகளின் அடிப்படைகள் ஒவ்வொரு சுதந்திரத்திற்கும் வேறுபடுகின்றன. எ.கா. 'பழங்குடியினர் பாதுகாப்பு' நடமாட்டம் மற்றும் வசிப்பிடத்திற்கு மட்டுமே பொருந்தும், பேச்சு சுதந்திரத்திற்கு அல்ல."
          ]
        }
      }
    ],
    "sec_article_20": [
      {
        "title": "1. Three Protections for Conviction of Offences (குற்றச்சாட்டுகளிலிருந்து 3 பாதுகாப்புகள்)",
        "points": {
          "en": [
            "Scope of Article 20: Article 20 grants protection against arbitrary and excessive punishment to an accused person, whether citizen or foreigner or legal person.",
            "Three Distinct Protections in Article 20:\n\n1. Article 20(1) – No Ex-Post-Facto Criminal Law:\n   - Meaning: No person shall be convicted of any offence except for violation of a law IN FORCE at the time of the commission of the act.\n   - No Greater Penalty: No penalty greater than that prescribed by law at the time of commission can be imposed.\n   - CRITICAL LIMITATION: Applies ONLY to CRIMINAL laws, NOT to civil liabilities or tax laws. Retrospective civil/tax laws are VALID.\n   - Beneficent Ex-Post-Facto: Retrospective criminal law that reduces punishment or benefits the accused IS constitutional.\n\n2. Article 20(2) – No Double Jeopardy:\n   - Meaning: No person shall be prosecuted and punished for the SAME offence more than once.\n   - CRITICAL LIMITATION: Applies ONLY before COURTS OF LAW or judicial tribunals. Departmental, administrative, or departmental proceedings are NOT double jeopardy (e.g. dismissal from job + criminal trial is valid).\n\n3. Article 20(3) – No Self-Incrimination:\n   - Meaning: No person ACCUSED of any offence shall be compelled to be a witness against himself.\n   - Scope: Protects against oral testimony and production of self-incriminating documents.\n   - DOES NOT PROTECT: Compulsory production of material objects, thumb impressions, handwriting specimens, blood samples, or bodily search."
          ],
          "ta": [
            "உறுப்பு 20-ன் எல்லை: உறுப்பு 20 குடிமகன், வெளிநாட்டவர் அல்லது சட்டப்பூர்வ நபர் என எவருக்கும் தன்னிச்சையான மற்றும் அதிகப்படியான தண்டனைக்கு எதிராகப் பாதுகாப்பு அளிக்கிறது.",
            "உறுப்பு 20-ல் உள்ள மூன்று தனித்துவமான பாதுகாப்புகள்:\n\n1. உறுப்பு 20(1) – முந்தைய தேதியிட்ட குற்றவியல் சட்டத் தடை (No Ex-Post-Facto Law):\n   - பொருள்: குற்றம் செய்த நேரத்தில் நடைமுறையில் உள்ள சட்டத்தை மீறினால் தவிர வேறு எதற்காகவும் ஒரு நபரைத் தண்டிக்க முடியாது.\n   - அதிக தண்டனை இல்லை: குற்றம் செய்த நேரத்தில் சட்டத்தால் நிர்ணயிக்கப்பட்ட தண்டனையை விட அதிக தண்டனையை விதிக்க முடியாது.\n   - முக்கிய வரம்பு: குற்றவியல் சட்டங்களுக்கு மட்டுமே பொருந்தும், சிவில் சட்டங்கள் அல்லது வரிச் சட்டங்களுக்குப் பொருந்தாது.\n   - நன்மையளிக்கும் சட்டம்: தண்டனையைக் குறைக்கும் முந்தைய தேதியிட்ட குற்றவியல் சட்டம் செல்லுபடியாகும்.\n\n2. உறுப்பு 20(2) – இரட்டை தண்டனைத் தடை (No Double Jeopardy):\n   - பொருள்: ஒரே குற்றத்திற்காக எந்தவொரு நபரும் ஒன்றுக்கு மேற்பட்ட முறை விசாரிக்கப்பட்டு தண்டிக்கப்படக்கூடாது.\n   - முக்கிய வரம்பு: நீதிமன்றங்கள் அல்லது நீதித்துறை தீர்ப்பாயங்களுக்கு மட்டுமே பொருந்தும். துறைசார்/நிர்வாக நடவடிக்கைகள் இரட்டை தண்டனை ஆகாது (எ.கா. வேலையிலிருந்து நீக்கம் + குற்றவியல் வழக்கு செல்லுபடியாகும்).\n\n3. உறுப்பு 20(3) – தனக்குத்தானே எதிரான சாட்சியத் தடை (No Self-Incrimination):\n   - பொருள்: குற்றம் சாட்டப்பட்ட எந்தவொரு நபரும் தனக்குத்தானே எதிராகச் சாட்சியமளிக்க வற்புறுத்தப்படக்கூடாது.\n   - எல்லை: வாய்மொழி சாட்சியம் மற்றும் ஆவணங்களை உற்பத்தி செய்வதற்கு எதிராகப் பாதுகாக்கிறது.\n   - பாதுகாப்பளிக்காதவை: கட்டாய கைரேகை, கையெழுத்து மாதிரி, ரத்த மாதிரிகள் அல்லது உடல் சோதனைக்கு எதிராகப் பாதுகாப்பளிக்காது."
          ]
        }
      }
    ],
    "sec_article_21": [
      {
        "title": "1. Protection of Life & Personal Liberty (வாழ்வு மற்றும் தனிநபர் சுதந்திரப் பாதுகாப்பு)",
        "points": {
          "en": [
            "Article 21 Text: 'No person shall be deprived of his life or personal liberty except according to procedure established by law.'",
            "Available to ALL Persons: Available to both citizens and non-citizens (foreigners).",
            "Evolution of Interpretation (Gopalan to Maneka Gandhi):\n1. A.K. Gopalan Case (1950): SC took a NARROW interpretation. Held that Article 21 protects ONLY against arbitrary executive action, not legislative action. Parliament could enact any law depriving personal liberty provided it followed a procedure.\n2. Maneka Gandhi Case (1978): SC took a WIDE interpretation, overruling Gopalan. Held that procedure depriving life/personal liberty must be JUST, FAIR, AND REASONABLE (not arbitrary, fanciful, or oppressive). Introduced the American concept of 'Due Process of Law' into Article 21 in spirit.",
            "Expanded Dimensions of Article 21 (Landmark Rights Recognized by SC):\n- Right to live with human dignity (*Francis Coralie*)\n- Right to privacy (*K.S. Puttaswamy 2017* – 9-judge bench)\n- Right to clean environment, water & air (*M.C. Mehta*)\n- Right to free legal aid (*Hussainara Khatoon*)\n- Right to speedy trial (*Hussainara Khatoon*)\n- Right to livelihood (*Olga Tellis*)\n- Right against solitary confinement & public hanging\n- Right to shelter, health, sleep, and travel abroad.",
            "TNPSC Trap: Article 21 cannot be suspended even during a National Emergency under Article 352 (44th Amendment Act 1978)."
          ],
          "ta": [
            "உறுப்பு 21 உரை: 'சட்டத்தால் நிறுவப்பட்ட நடைமுறையின்படியன்றி வேறு எவ்வழியிலும் எந்தவொரு நபரின் உயிரோ அல்லது தனிநபர் சுதந்திரமோ பறிக்கப்படக்கூடாது.'",
            "அனைத்து நபர்களுக்கும் கிடைக்கும்: குடிமக்கள் மற்றும் குடிமக்கள் அல்லாதோர் (வெளிநாட்டினர்) இருவருக்குமே கிடைக்கும்.",
            "விளக்கத்தின் வளர்ச்சி (கோபாலன் முதல் மேனகா காந்தி வரை):\n1. ஏ.கே. கோபாலன் வழக்கு (1950): உச்ச நீதிமன்றம் ஒரு குறுகிய விளக்கத்தை எடுத்தது. உறுப்பு 21 தன்னிச்சையான நிர்வாக நடவடிக்கைக்கு எதிராக மட்டுமே பாதுகாக்கிறது, சட்டமன்ற நடவடிக்கைக்கு எதிராக அல்ல எனக் கூறியது.\n2. மேனகா காந்தி வழக்கு (1978): உச்ச நீதிமன்றம் கோபாலன் தீர்ப்பை மாற்றி அகன்ற விளக்கத்தை எடுத்தது. தனிநபர் சுதந்திரத்தைப் பறிக்கும் நடைமுறை நியாயமானதாக, நேர்மையானதாக, பகுத்தறிவுள்ளதாகவும் இருக்க வேண்டும் எனக் கூறியது (அமெரிக்க 'சட்டத்தின் உரிய நடைமுறை' கருத்தை அறிமுகப்படுத்தியது).\n\nஉறுப்பு 21-ன் விரிவுபடுத்தப்பட்ட பரிமாணங்கள் (உச்ச நீதிமன்றம் அங்கீகரித்த உரிமைகள்):\n- மனித கண்ணியத்துடன் வாழும் உரிமை\n- தனிமனித ரகசிய உரிமை (*K.S. புட்டசுவாமி 2017* – 9 நீதிபதிகள் அமர்வு)\n- தூய்மையான சுற்றுச்சூழல், குடிநீர் & காற்றுக்கான உரிமை (*M.C. மேத்தா*)\n- இலவச சட்ட உதவி உரிமை (*உசைனாரா கதூன்*)\n- விரைவு விசாரணை உரிமை (*உசைனாரா கதூன்*)\n- வாழ்வாதார உரிமை (*ஓல்கா டெல்லிஸ்*)\n- தனிமைச் சிறை & பகிரங்கத் தூக்கிலிடலுக்கு எதிரான உரிமை\n- தங்குமிடம், சுகாதாரம், தூக்கம், வெளிநாடு செல்லும் உரிமை.",
            "டிஎன்பிஎஸ்சி பொறி: தேசிய அவசரநிலையின் போது கூட (உறுப்பு 352) உறுப்பு 21-ஐ இடைநிறுத்த முடியாது (44வது திருத்தச் சட்டம் 1978)."
          ]
        }
      }
    ],
    "sec_article_21a": [
      {
        "title": "1. Right to Education Framework (கல்வி உரிமைச் சட்டக் கட்டமைப்பு)",
        "points": {
          "en": [
            "Article 21A Text: 'The State shall provide free and compulsory education to all children of the age of six to fourteen years in such manner as the State may, by law, determine.'",
            "Added by 86th Constitutional Amendment Act, 2002: Made primary education a Fundamental Right.",
            "Target Age Group: Children aged SIX to FOURTEEN years (6–14 years).",
            "RTE Act 2009: Parliament enacted the Right of Children to Free and Compulsory Education (RTE) Act, 2009 to operationalize Article 21A. It came into force on April 1, 2010.",
            "Consequential Amendments by 86th CAA 2002:\n1. Modified Article 45 (DPSP): State shall endeavor to provide early childhood care and education for all children until they complete the age of SIX years.\n2. Added Article 51A(k) (Fundamental Duty): Duty of every parent/guardian to provide educational opportunities to their child/ward aged 6 to 14 years.",
            "TNPSC Trap: Article 21A covers children aged 6 to 14 years, NOT 0 to 6 years (which is covered under DPSP Article 45)."
          ],
          "ta": [
            "உறுப்பு 21A உரை: 'அரசு சட்டத்தால் தீர்மானிக்கும் முறையில் ஆறு முதல் பதினான்கு வயது வரையிலான அனைத்துக் குழந்தைகளுக்கும் இலவச மற்றும் கட்டாயக் கல்வியை அரசு வழங்க வேண்டும்.'",
            "2002-ன் 86வது அரசியலமைப்பு திருத்தச் சட்டத்தால் சேர்க்கப்பட்டது: தொடக்கக் கல்வியை அடிப்படை உரிமையாக்கியது.",
            "இலக்கு வயதுக் குழு: ஆறு முதல் பதினான்கு வயது வரையிலான குழந்தைகள் (6-14 ஆண்டுகள்).",
            "RTE சட்டம் 2009: உறுப்பு 21A-ஐச் செயல்படுத்துவதற்காக நாடாளுமன்றம் இலவச மற்றும் கட்டாயக் கல்வி உரிமைச் சட்டத்தை (RTE Act) 2009 இல் இயற்றியது. இது ஏப்ரல் 1, 2010 அன்று நடைமுறைக்கு வந்தது.",
            "86வது திருத்தத்தால் ஏற்பட்ட தொடர் திருத்தங்கள்:\n1. உறுப்பு 45 (DPSP) திருத்தப்பட்டது: குழந்தைகள் ஆறு வயதை அடையும் வரை ஆரம்பகால குழந்தைப் பராமரிப்பு மற்றும் கல்வியை வழங்க அரசு முயல வேண்டும்.\n2. உறுப்பு 51A(k) (அடிப்படை கடமை) சேர்க்கப்பட்டது: 6 முதல் 14 வயது வரையிலான குழந்தைக்குக் கல்வி வாய்ப்புகளை வழங்குவது ஒவ்வொரு பெற்றோர்/பாதுகாவலரின் கடமையாகும்.",
            "டிஎன்பிஎஸ்சி பொறி: உறுப்பு 21A 6 முதல் 14 வயதுக் குழந்தைகளை மட்டுமே உள்ளடக்கிறது, 0 முதல் 6 வயதுக் குழந்தைகளை அல்ல (அது DPSP உறுப்பு 45-ன் கீழ் வருகிறது)."
          ]
        }
      }
    ],
    "sec_article_22": [
      {
        "title": "1. Safeguards Against Ordinary Arrest (சாதாரண கைதிற்கு எதிரான பாதுகாப்புகள்)",
        "points": {
          "en": [
            "Article 22 Purpose: Grants protection against arbitrary arrest and detention.",
            "Two Types of Detention:\n1. Punitive Detention: Punishing a person for an offence committed after trial and conviction by court.\n2. Preventive Detention: Detaining a person without trial and conviction, based on suspicion to prevent future crime.",
            "Four Rights under Ordinary/Punitive Arrest (Art 22(1) & 22(2)):\n1. Right to be informed as soon as may be of the GROUNDS OF ARREST.\n2. Right to consult and be defended by a LEGAL PRACTITIONER of choice.\n3. Right to be produced before the nearest MAGISTRATE within 24 HOURS (excluding time necessary for journey).\n4. Right not to be detained beyond 24 hours without authority of Magistrate.",
            "Exceptions (Art 22(3)): These four rights are NOT available to:\n1. Enemy aliens\n2. Persons arrested or detained under a PREVENTIVE DETENTION law."
          ],
          "ta": [
            "உறுப்பு 22 நோக்கம்: தன்னிச்சையான கைது மற்றும் தடுப்புக் காவலுக்கு எதிராகப் பாதுகாப்பு அளிக்கிறது.",
            "இரண்டு வகையான தடுப்புக் காவல்:\n1. தண்டனைக்காவல் (Punitive Detention): நீதிமன்ற விசாரணை மற்றும் தண்டனைக்குப் பிறகு ஒரு நபரைக் குற்றம் செய்ததற்காகத் தண்டிப்பது.\n2. தடுப்புக் காவல் (Preventive Detention): எதிர்காலக் குற்றத்தைத் தடுக்கும் சந்தேகத்தின் பேரில் நீதிமன்ற விசாரணையின்றி ஒரு நபரைக் காவலில் வைப்பது.",
            "சாதாரணக் கைதின் கீழ் 4 உரிமைகள் (உறுப்பு 22(1) & 22(2)):\n1. கைதுக்கான காரணங்களை உடனடியாக அறிந்து கொள்ளும் உரிமை.\n2. தான் விரும்பும் வழக்கறிஞரை ஆலோசிக்கவும் பிரதிநிதித்துவப்படுத்தவும் உரிமை.\n3. 24 மணி நேரத்திற்குள் அருகிலுள்ள நடுவரிடம் (Magistrate) ஆஜர்படுத்தப்படும் உரிமை (பயண நேரம் நீங்கலாக).\n4. நடுவரின் அதிகாரமின்றி 24 மணி நேரத்திற்கு மேல் காவலில் வைக்கப்படாமல் இருக்கும் உரிமை.",
            "விலக்குகள் (உறுப்பு 22(3)): இந்த 4 உரிமைகளும் பின்வருவோருக்குக் கிடைக்காது:\n1. எதிரி நாட்டு வெளிநாட்டினர்\n2. தடுப்புக் காவல் சட்டத்தின் கீழ் கைது செய்யப்பட்ட நபர்கள்."
          ]
        }
      }
    ],
    "sec_preventive_detention": [
      {
        "title": "1. Preventive Detention Rules & Safeguards (தடுப்புக் காவல் விதிகளும் பாதுகாப்புகளும்)",
        "points": {
          "en": [
            "Meaning: Preventive detention is detention without judicial trial, meant to prevent a person from committing an offence injurious to state security or public order.",
            "Constitutional Safeguards (Art 22(4) to 22(7)):\n1. Maximum Detention Period: Cannot exceed THREE MONTHS unless an Advisory Board reports sufficient cause for extended detention.\n2. Advisory Board Composition: Advisory Board consists of persons qualified to be appointed as High Court judges.\n3. Communication of Grounds: Detenu must be communicated grounds of detention as soon as possible (except facts against public interest).\n4. Opportunity for Representation: Detenu must be afforded earliest opportunity to make a representation against the detention order.",
            "Legislative Jurisdiction: Parliament has exclusive power for preventive detention related to Defense, Foreign Affairs, or Security of India. Parliament and State Legislatures share concurrent power for Public Order or Maintenance of Supplies/Services.",
            "TNPSC Trap: Preventive Detention laws exist in BOTH Union and State legislative spheres. 44th Amendment 1978 passed a provision reducing 3 months to 2 months, but it has NOT been brought into force; current maximum period remains 3 MONTHS."
          ],
          "ta": [
            "பொருள்: தடுப்புக் காவல் என்பது நீதிமன்ற விசாரணையின்றி ஒரு நபரைக் காவலில் வைப்பதாகும், இது மாநிலப் பாதுகாப்பு அல்லது பொது ஒழுங்கிற்குத் தீங்கு விளைவிக்கும் குற்றத்தைச் செய்யாமல் தடுப்பதாகும்.",
            "அரசியலமைப்புப் பாதுகாப்புகள் (உறுப்பு 22(4) முதல் 22(7)):\n1. அதிகபட்சக் காவல் காலம்: ஆலோசனை வாரியம் நீட்டிக்கப்பட்ட காவலுக்கு போதுமான காரணத்தை அறிக்கையிட்டாலன்றி 3 மாதங்களுக்கு மிகக்கூடாது.\n2. ஆலோசனை வாரிய அமைப்பு: உயர் நீதிமன்ற நீதிபதியாக நியமிக்கத் தகுதியுள்ள நபர்களைக் கொண்டது.\n3. காரணங்களை அறிவித்தல்: கைது செய்யப்பட்ட நபருக்குத் தடுப்புக் காவல் காரணங்கள் உடனடியாகத் தெரிவிக்கப்பட வேண்டும் (பொது நலனுக்கு எதிரான தகவல்கள் தவிர).\n4. மேல்முறையீட்டு வாய்ப்பு: தடுப்புக் காவல் உத்தரவுக்கு எதிராக மேல்முறையீடு செய்ய ஆரம்ப வாய்ப்பு வழங்கப்பட வேண்டும்.",
            "சட்டமன்ற அதிகாரம்: பாதுகாப்பு, வெளியுறவு, இந்தியப் பாதுகாப்பு தொடர்பான தடுப்புக் காவலுக்கு நாடாளுமன்றத்திற்கு மட்டுமே அதிகாரம் உண்டு. பொது ஒழுங்கு அல்லது அத்தியாவசிய சேவைகள் தொடர்பான தடுப்புக் காவலுக்கு நாடாளுமன்றம் மற்றும் மாநில சட்டமன்றங்கள் இரண்டிற்கும் அதிகாரம் உண்டு.",
            "டிஎன்பிஎஸ்சி பொறி: தடுப்புக் காவல் சட்டங்கள் மத்திய மற்றும் மாநிலப் பட்டியல்களில் உள்ளன. 44வது திருத்தம் 3 மாதங்களை 2 மாதங்களாகக் குறைக்கும் விதியை நிறைவேற்றியது, ஆனால் அது நடைமுறைக்கு வரவில்லை; தற்போதைய அதிகபட்ச காலம் 3 மாதங்கள் மட்டுமே."
          ]
        }
      }
    ],
    "sec_article_23": [
      {
        "title": "1. Prohibition of Human Trafficking & Forced Labour (மனித வியாபாரம் மற்றும் கட்டாய வேலை தடை)",
        "points": {
          "en": [
            "Article 23(1) Core Rule: Traffic in human beings, begar, and other similar forms of forced labour are prohibited and punishable by law.",
            "Enforceable Against State & Private Persons: Protects individuals against both State and private individuals.",
            "Three Core Terms Explained:\n1. Traffic in Human Beings: Buying and selling of men, women, and children like goods, immoral trafficking in women and children, and prostitution.\n2. Begar: Involuntary labour without ANY payment/remuneration (traditional Indian feudal practice).\n3. Forced Labour: Compelling a person to work against his will, or paying less than the statutory minimum wage (*People's Union for Democratic Rights Case 1982*).",
            "Article 23(2) Exception – Compulsory Service:\n- State is permitted to impose COMPULSORY SERVICE FOR PUBLIC PURPOSES (e.g. military conscription, national social service).\n- NON-DISCRIMINATION RULE: In imposing such compulsory service, State shall NOT discriminate on grounds ONLY of Religion, Race, Caste, or Class (NOTE: 'Sex' is NOT included in this non-discrimination list!).",
            "TNPSC Trap: In Article 23(2) compulsory service exception, discrimination is prohibited on grounds of Religion, Race, Caste, Class — 'SEX' IS OMITTED."
          ],
          "ta": [
            "உறுப்பு 23(1) முதன்மை விதி: மனித வியாபாரம், வெட்டி வேலை (begar) மற்றும் அதுபோன்ற பிற கட்டாய வேலை வடிவங்கள் தடைசெய்யப்பட்டுள்ளன மற்றும் சட்டத்தின்படி தண்டனைக்குரியவை.",
            "அரசு மற்றும் தனியாருக்கு எதிராகப் பொருந்தும்: அரசு மற்றும் தனியார் தனிநபர்கள் இருவருக்கும் எதிராகப் தனிநபர்களைப் பாதுகாக்கிறது.",
            "மூன்று முக்கிய சொற்களின் விளக்கம்:\n1. மனித வியாபாரம் (Traffic in Human Beings): ஆண்களையும், பெண்களையும், குழந்தைகளையும் பொருட்களைப் போல வாங்குவதும் விற்பதும், பாலியல் தொழில்.\n2. வெட்டி வேலை (Begar): எந்தவொரு ஊதியமுமின்றி கட்டாயப்படுத்தி வேலை வாங்குவது (பாரம்பரிய நிலப்பிரபுத்துவ முறை).\n3. கட்டாய வேலை (Forced Labour): விருப்பத்திற்கு மாறாக வேலை செய்ய வற்புறுத்துவது அல்லது குறைந்தபட்ச ஊதியத்தை விடக் குறைவாக வழங்குவது.\n\nஉறுப்பு 23(2) விலக்கு – கட்டாயப் பொதுச் சேவை:\n- பொது நோக்கங்களுக்காகக் கட்டாயப் பொதுச் சேவையை (எ.கா. ராணுவ சேவை, தேசிய சமூக சேவை) விதிக்க அரசுக்கு அனுமதியளிக்கிறது.\n- பாகுபாடின்மை விதி: அத்தகைய கட்டாயச் சேவையை விதிப்பதில், அரசு மதம், இனம், சாதி, வகுப்பு ஆகிய 4 அடிப்படைகளில் மட்டுமே பாகுபாடு காட்டக்கூடாது ('பாலினம்' இந்த பட்டியலில் இல்லை!).",
            "டிஎன்பிஎஸ்சி பொறி: உறுப்பு 23(2) கட்டாயச் சேவை விலக்கில், மதம், இனம், சாதி, வகுப்பு அடிப்படையில் பாகுபாடு தடை செய்யப்பட்டுள்ளது — 'பாலினம்' விடுக்கப்பட்டுள்ளது."
          ]
        }
      }
    ],
    "sec_article_24": [
      {
        "title": "1. Prohibition of Child Labour in Hazardous Work (ஆபத்தான வேலைகளில் குழந்தை தொழிலாளர் தடை)",
        "points": {
          "en": [
            "Article 24 Core Rule: No child below the age of FOURTEEN YEARS shall be employed to work in any factory, mine, or engaged in any other hazardous employment.",
            "Hazardous Employment Focus: Article 24 prohibits child labour specifically in HAZARDOUS occupations (factories, mines, construction, railways).",
            "Does NOT Prohibit Non-Hazardous Work Originally: Originally did not prohibit child employment in innocent/non-hazardous work.",
            "Child Labour Act Amendments:\n- Child Labour (Prohibition and Regulation) Act, 1986.\n- Amended in 2016 (renamed Child and Adolescent Labour Act, 1986): Completely prohibited employment of children below 14 years in ALL occupations and processes (except family enterprises after school hours). Prohibited employment of adolescents (14 to 18 years) in hazardous occupations.",
            "TNPSC Trap Comparison:\n- Article 21A = Right to Education for children aged 6 to 14 years.\n- Article 24 = Prohibition of child labour below 14 years in hazardous work."
          ],
          "ta": [
            "உறுப்பு 24 முதன்மை விதி: பதினான்கு வயதுக்குட்பட்ட எந்தவொரு குழந்தையும் எந்தவொரு தொழிற்சாலையிலும், சுரங்கத்திலும் அல்லது பிற ஆபத்தான வேலைகளிலும் வேலைக்கு அமர்த்தப்படக்கூடாது.",
            "ஆபத்தான வேலைவாய்ப்பு மையம்: உறுப்பு 24 குழந்தை தொழிலாளர்களைக் குறிப்பாக ஆபத்தான தொழில்களில் (தொழிற்சாலைகள், சுரங்கங்கள், கட்டுமானம்) தடை செய்கிறது.",
            "ஆபத்தற்ற வேலையை ஆரம்பத்தில் தடை செய்யவில்லை: ஆரம்பத்தில் ஆபத்தற்ற எளிய வேலைகளில் குழந்தை வேலைவாய்ப்பைத் தடை செய்யவில்லை.",
            "குழந்தை தொழிலாளர் சட்டத் திருத்தங்கள்:\n- குழந்தை தொழிலாளர் (தடை மற்றும் ஒழுங்குமுறை) சட்டம், 1986.\n- 2016 இல் திருத்தப்பட்டது: 14 வயதுக்குட்பட்ட குழந்தைகளை அனைத்து தொழில்களிலும் வேலைக்கு அமர்த்துவதை முற்றிலும் தடை செய்தது. 14 முதல் 18 வயதுடைய சிறார்களை ஆபத்தான தொழில்களில் வேலைக்கு அமர்த்துவதைத் தடை செய்தது.",
            "டிஎன்பிஎஸ்சி பொறி ஒப்பீடு:\n- உறுப்பு 21A = 6 முதல் 14 வயதுக் குழந்தைகளுக்கான கல்வி உரிமை.\n- உறுப்பு 24 = 14 வயதுக்குட்பட்ட குழந்தைகளின் ஆபத்தான வேலைவாய்ப்புத் தடை."
          ]
        }
      }
    ],
    "sec_case_laws_part2": [
      {
        "title": "1. Landmark Cases Summary (பகுதி 2 வழக்குகள்)",
        "points": {
          "en": [
            "1. A.K. Gopalan v. State of Madras (1950): Narrow interpretation of Article 21 ('procedure established by law').",
            "2. Maneka Gandhi v. Union of India (1978): Expanded Article 21; procedure must be just, fair, and reasonable (Due Process). Formed Golden Triangle of Arts 14, 19, 21.",
            "3. K.S. Puttaswamy v. Union of India (2017): 9-judge bench unanimously declared Right to Privacy a fundamental right under Article 21.",
            "4. Hussainara Khatoon v. Home Secretary, Bihar (1979): Right to speedy trial and free legal aid declared fundamental right under Article 21.",
            "5. Olga Tellis v. Bombay Municipal Corporation (1985): Right to livelihood included under Article 21.",
            "6. Unni Krishnan v. State of AP (1993): Right to education up to 14 years declared part of Article 21 (paved way for Art 21A).",
            "7. Shreya Singhal v. Union of India (2015): Section 66A of IT Act struck down for violating freedom of speech under Article 19(1)(a).",
            "8. D.K. Basu v. State of West Bengal (1997): Laid down 11 mandatory guidelines for arrest and detention under Articles 21 & 22."
          ],
          "ta": [
            "1. ஏ.கே. கோபாலன் எதிர் மெட்ராஸ் மாநிலம் (1950): உறுப்பு 21-ன் குறுகிய விளக்கம் ('சட்டத்தால் நிறுவப்பட்ட நடைமுறை').",
            "2. மேனகா காந்தி எதிர் இந்திய யூனியன் (1978): உறுப்பு 21-ன் விரிவாக்கம்; நடைமுறை நியாயமானதாக இருக்க வேண்டும். உறுப்புகள் 14, 19, 21 தங்க முக்கோணத்தை உருவாக்கியது.",
            "3. K.S. புட்டசுவாமி எதிர் இந்திய யூனியன் (2017): 9 நீதிபதிகள் அமர்வு தனிமனித ரகசிய உரிமையை உறுப்பு 21-ன் கீழ் அடிப்படை உரிமையாக அறிவித்தது.",
            "4. உசைனாரா கதூன் எதிர் பீகார் அரசு (1979): விரைவு விசாரணை மற்றும் இலவச சட்ட உதவி உரிமை உறுப்பு 21-ன் கீழ் அடிப்படை உரிமையாக அறிவிக்கப்பட்டது.",
            "5. ஓல்கா டெல்லிஸ் எதிர் பம்பாய் மாநகராட்சி (1985): வாழ்வாதார உரிமை உறுப்பு 21-ன் கீழ் சேர்க்கப்பட்டது.",
            "6. உன்னிகிருஷ்ணன் எதிர் ஆந்திரப் பிரதேசம் (1993): 14 வயது வரையிலான கல்வி உரிமை உறுப்பு 21-ன் பகுதியாக அறிவிக்கப்பட்டது (உறுப்பு 21A-க்கு வழிவகுத்தது).",
            "7. ஸ்ரேயா சிங்கால் எதிர் இந்திய யூனியன் (2015): தகவல் தொழில்நுட்பச் சட்டத்தின் பிரிவு 66A உறுப்பு 19(1)(a)-ஐ மீறியதால் ரத்து செய்யப்பட்டது.",
            "8. D.K. பாசு எதிர் மேற்கு வங்காளம் (1997): உறுப்புகள் 21 & 22-ன் கீழ் கைது மற்றும் காவலுக்கான 11 கட்டாய வழிகாட்டுதல்களை வழங்கியது."
          ]
        }
      }
    ],
    "sec_traps_connections_part2": [
      {
        "title": "1. Cross-Topic Connections (பாடத் தொடர்புகள்)",
        "points": {
          "en": [
            "Preamble Connection: Article 19 freedoms operationalize 'Liberty of Thought, Expression, Belief, Faith, Worship'.",
            "DPSP Connection: Article 21A (Education) connects to DPSP Article 45. Articles 23 & 24 connect to DPSP Article 39(e) & (f) protecting workers and children from exploitation.",
            "Fundamental Duties Connection: Article 21A connects directly to Article 51A(k) (duty of parent to educate child aged 6-14).",
            "Basic Structure Connection: Freedom of speech (19(1)(a)), Judicial Review (13/32/226), and Personal Liberty (21) form part of the Basic Structure."
          ],
          "ta": [
            "முகவுரைத் தொடர்பு: உறுப்பு 19 சுதந்திரங்கள் முகவுரையின் 'எண்ணம், கருத்து வெளிப்பாடு, நம்பிக்கை, பக்தி, வழிபாட்டு சுதந்திரத்தை' செயல்படுத்துகின்றன.",
            "DPSP தொடர்பு: உறுப்பு 21A (கல்வி) DPSP உறுப்பு 45 உடன் இணைகிறது. உறுப்புகள் 23 & 24 DPSP உறுப்பு 39(e) & (f) தொழிலாளர்கள் மற்றும் குழந்தைகளைப் பாதுகாப்பதுடன் இணைகின்றன.",
            "அடிப்படை கடமைகள் தொடர்பு: உறுப்பு 21A உறுப்பு 51A(k) உடன் நேரடியாக இணைகிறது (6-14 வயதுக் குழந்தைக்குக் கல்வி அளிக்கும் பெற்றோர் கடமை).",
            "அடிப்படை கட்டமைப்பு தொடர்பு: பேச்சு சுதந்திரம் (19(1)(a)), நீதித்துறை ஆய்வு, மற்றும் தனிநபர் சுதந்திரம் (21) அடிப்படை கட்டமைப்பின் பகுதிகளாகும்."
          ]
        }
      },
      {
        "title": "2. High-Yield Revision Summary (முக்கிய திருப்புதல் சுருக்கம்)",
        "points": {
          "en": [
            "MUST REMEMBER QUICK REVISION LIST:\n- Article 19 = 6 Freedoms for CITIZENS ONLY (Speech, Assembly, Association, Movement, Residence, Profession).\n- Article 19(2)-(6) = Reasonable Restrictions (Specific grounds per freedom).\n- Article 20 = 3 Protections: 20(1) No Ex-Post-Facto Law (criminal only), 20(2) No Double Jeopardy (courts only), 20(3) No Self-Incrimination (oral/doc only).\n- Article 21 = Protection of Life & Personal Liberty; Expanded to Privacy (Puttaswamy 2017) & Due Process (Maneka Gandhi 1978).\n- Article 21A = Free & compulsory education for children 6 to 14 years (86th CAA 2002; RTE Act 2009).\n- Article 22 = Ordinary arrest rights (grounds, lawyer, 24h magistrate); Preventive Detention (max 3 months without Advisory Board).\n- Article 23 = Prohibition of Traffic in Human Beings, Begar, and Forced Labour (Enforceable vs State & Private).\n- Article 24 = Prohibition of child labour below 14 years in HAZARDOUS work."
          ],
          "ta": [
            "அவசிய நினைவில் கொள்ள வேண்டிய விரைவு திருப்புதல் பட்டியல்:\n- உறுப்பு 19 = குடிமக்களுக்கு மட்டுமேயான 6 சுதந்திரங்கள் (பேச்சு, கூட்டம், சங்கம், இயக்கம், வசிப்பிடம், தொழில்).\n- உறுப்பு 19(2)-(6) = நியாயமான கட்டுப்பாடுகள் (ஒவ்வொரு சுதந்திரத்திற்கும் குறிப்பிட்ட அடிப்படைகள்).\n- உறுப்பு 20 = 3 பாதுகாப்புகள்: 20(1) முந்தைய தேதியிட்ட சட்டத் தடை (குற்றவியல் மட்டுமே), 20(2) இரட்டை தண்டனைத் தடை (நீதிமன்றங்கள் மட்டுமே), 20(3) தனக்குத்தானே எதிரான சாட்சியத் தடை.\n- உறுப்பு 21 = வாழ்வு & தனிநபர் சுதந்திரப் பாதுகாப்பு; ரகசிய உரிமை (புட்டசுவாமி 2017) & சட்டத்தின் உரிய நடைமுறை (மேனகா காந்தி 1978).\n- உறுப்பு 21A = 6 முதல் 14 வயதுக் குழந்தைகளுக்கான இலவச & கட்டாயக் கல்வி (86வது திருத்தம் 2002; RTE சட்டம் 2009).\n- உறுப்பு 22 = சாதாரண கைது உரிமைகள் (காரணங்கள், வழக்கறிஞர், 24 மணி நேர நடுவர்); தடுப்புக் காவல் (ஆலோசனை வாரியமின்றி அதிகபட்சம் 3 மாதங்கள்).\n- உறுப்பு 23 = மனித வியாபாரம், வெட்டி வேலை, கட்டாய வேலை தடை (அரசு & தனியாருக்கு எதிராகப் பொருந்தும்).\n- உறுப்பு 24 = ஆபத்தான வேலைகளில் 14 வயதுக்குட்பட்ட குழந்தை தொழிலாளர்கள் தடை."
          ]
        }
      }
    ]
  },
  "important_facts": {
    "en": [
      "Article 19 freedoms are available ONLY to Citizens of India, NOT to foreigners or corporations.",
      "Article 19(1)(f) Right to Property was deleted by the 44th Constitutional Amendment Act, 1978.",
      "97th Constitutional Amendment Act 2011 added 'cooperative societies' to Article 19(1)(c).",
      "Article 20(1) protection against ex-post-facto laws applies ONLY to criminal laws, NOT civil/tax liabilities.",
      "Article 20(2) double jeopardy protection applies ONLY before courts of law, NOT departmental/administrative inquiries.",
      "Article 20(3) self-incrimination protects against oral/documentary evidence, NOT thumb impressions, blood samples, or handwriting specimens.",
      "Maneka Gandhi Case (1978) introduced 'Due Process of Law' into Article 21, requiring procedure to be just, fair, and reasonable.",
      "Articles 20 and 21 CANNOT be suspended even during a National Emergency under Article 352 (44th CAA 1978).",
      "Article 21A was added by the 86th Constitutional Amendment Act, 2002 for children aged 6 to 14 years.",
      "Right of Children to Free and Compulsory Education (RTE) Act 2009 came into force on April 1, 2010.",
      "Article 22 preventive detention without Advisory Board approval is capped at a maximum of 3 MONTHS.",
      "Article 23 prohibits begar, forced labour, and human trafficking against BOTH State and private individuals.",
      "Article 23(2) compulsory public service exception omits 'Sex' from the non-discrimination list.",
      "Article 24 prohibits employment of children below 14 years specifically in HAZARDOUS occupations."
    ],
    "ta": [
      "உறுப்பு 19 சுதந்திரங்கள் இந்தியக் குடிமக்களுக்கு மட்டுமே கிடைக்கக்கூடியவை, வெளிநாட்டினருக்கோ கார்ப்பரேஷன்களுக்கோ அல்ல.",
      "உறுப்பு 19(1)(f) சொத்துரிமை 1978-ன் 44வது திருத்தச் சட்டத்தால் நீக்கப்பட்டது.",
      "2011-ன் 97வது திருத்தச் சட்டம் உறுப்பு 19(1)(c)-ல் 'கூட்டுறவு சங்கங்கள்' என்பதைச் சேர்த்தது.",
      "உறுப்பு 20(1) முந்தைய தேதியிட்ட சட்டப் பாதுகாப்பு குற்றவியல் சட்டங்களுக்கு மட்டுமே பொருந்தும், சிவில்/வரிப் பொறுப்புகளுக்கு அல்ல.",
      "உறுப்பு 20(2) இரட்டை தண்டனைப் பாதுகாப்பு நீதிமன்றங்களுக்கு மட்டுமே பொருந்தும், துறைசார்/நிர்வாக விசாரணைகளுக்கு அல்ல.",
      "உறுப்பு 20(3) தனக்குத்தானே எதிரான சாட்சியத் தடை வாய்மொழி/ஆவணச் சான்றுகளுக்கு மட்டுமே பாதுகாக்கிறது, கைரேகை/ரத்த மாதிரிகளுக்கு அல்ல.",
      "மேனகா காந்தி வழக்கு (1978) உறுப்பு 21-ல் 'சட்டத்தின் உரிய நடைமுறை'யை அறிமுகப்படுத்தியது.",
      "தேசிய அவசரநிலையின் போது கூட உறுப்புகள் 20 மற்றும் 21-ஐ இடைநிறுத்த முடியாது (44வது திருத்தம் 1978).",
      "உறுப்பு 21A 6 முதல் 14 வயதுக் குழந்தைகளுக்காக 2002-ன் 86வது திருத்தச் சட்டத்தால் சேர்க்கப்பட்டது.",
      "இலவச மற்றும் கட்டாயக் கல்வி உரிமைச் சட்டம் (RTE Act 2009) ஏப்ரல் 1, 2010 அன்று நடைமுறைக்கு வந்தது.",
      "உறுப்பு 22 ஆலோசனை வாரிய ஒப்புதலின்றி தடுப்புக் காவல் அதிகபட்சமாக 3 மாதங்கள் மட்டுமே இருக்க முடியும்.",
      "உறுப்பு 23 மனித வியாபாரம், வெட்டி வேலை, கட்டாய வேலையை அரசு மற்றும் தனியாருக்கு எதிராகத் தடுக்கிறது.",
      "உறுப்பு 23(2) கட்டாயப் பொதுச் சேவை விலக்கில் பாகுபாடின்மைப் பட்டியலிலிருந்து 'பாலினம்' விடுக்கப்பட்டுள்ளது.",
      "உறுப்பு 24 ஆபத்தான தொழில்களில் 14 வயதுக்குட்பட்ட குழந்தை தொழிலாளர்கள் வேலைவாய்ப்பைக் குறிப்பாகத் தடுக்கிறது."
    ]
  },
  "tnpsc_traps": [
    "⚠️ TRAP 1: Article 19 freedoms are available ONLY to Citizens, NOT to foreigners. (Contrast with Articles 20 & 21 which apply to ALL persons).",
    "⚠️ TRAP 2: Grounds of reasonable restrictions under Article 19 differ per freedom. E.g. 'Protection of Scheduled Tribes' applies to Movement/Residence (19(1)(d)/(e)), NOT Speech (19(1)(a)).",
    "⚠️ TRAP 3: Article 20(1) Ex-Post-Facto protection applies ONLY to Criminal laws. Retrospective Civil or Tax laws are FULLY VALID.",
    "⚠️ TRAP 4: Article 20(2) Double Jeopardy protection applies ONLY before Courts of Law/Judicial Tribunals. Departmental dismissal + criminal trial is VALID.",
    "⚠️ TRAP 5: Article 20(3) Self-Incrimination protects against oral/documentary evidence, NOT compulsory thumb impressions, blood samples, or handwriting specimens.",
    "⚠️ TRAP 6: Article 21A age group is 6 to 14 years (inserted by 86th CAA 2002). Age 0 to 6 years is covered under DPSP Article 45.",
    "⚠️ TRAP 7: Article 22 24-hour magistrate production rule EXCLUDES the time necessary for the journey from place of arrest to magistrate court.",
    "⚠️ TRAP 8: Preventive detention maximum period without Advisory Board approval remains 3 MONTHS (44th CAA provision reducing to 2 months was never notified).",
    "⚠️ TRAP 9: Article 23(2) compulsory public service exception forbids discrimination on grounds of Religion, Race, Caste, Class — 'SEX' IS OMITTED.",
    "⚠️ TRAP 10: Article 24 prohibits child labor below 14 years in HAZARDOUS occupations (factories, mines, construction), NOT non-hazardous family work."
  ],
  "tables": [
    {
      "id": "tbl_art19_six_freedoms",
      "title_en": "Article 19 – Six Freedoms & Reasonable Restriction Grounds",
      "title_ta": "உறுப்பு 19 – ஆறு சுதந்திரங்களும் நியாயமான கட்டுப்பாட்டு அடிப்படைகளும்",
      "headers_en": [
        "Freedom Article",
        "Freedom Description",
        "Reasonable Restriction Clause",
        "Major Restriction Grounds",
        "TNPSC Takeaway"
      ],
      "headers_ta": [
        "சுதந்திர உறுப்பு",
        "சுதந்திர விளக்கம்",
        "கட்டுப்பாட்டு விதி",
        "முக்கிய கட்டுப்பாட்டு அடிப்படைகள்",
        "டிஎன்பிஎஸ்சி குறிப்பு"
      ],
      "rows_en": [
        [
          "Art 19(1)(a)",
          "Speech & Expression",
          "Art 19(2)",
          "Sovereignty/Integrity, Security of State, Foreign relations, Public Order, Decency/Morality, Contempt of Court, Defamation, Incitement (8 grounds)",
          "Includes Press Freedom, Commercial ads, Right to silence"
        ],
        [
          "Art 19(1)(b)",
          "Peaceful Assembly",
          "Art 19(3)",
          "Sovereignty & Integrity of India, Public Order (Without arms)",
          "Does NOT include right to strike or violent assembly"
        ],
        [
          "Art 19(1)(c)",
          "Associations & Cooperatives",
          "Art 19(4)",
          "Sovereignty & Integrity of India, Public Order, Morality",
          "Cooperative societies added by 97th CAA 2011"
        ],
        [
          "Art 19(1)(d)",
          "Internal Movement",
          "Art 19(5)",
          "Interests of General Public, Protection of Scheduled Tribes",
          "Internal movement only; Foreign travel under Art 21"
        ],
        [
          "Art 19(1)(e)",
          "Residence & Settlement",
          "Art 19(5)",
          "Interests of General Public, Protection of Scheduled Tribes",
          "ST land protection restricts non-tribal settlement"
        ],
        [
          "Art 19(1)(g)",
          "Profession & Trade",
          "Art 19(6)",
          "Interests of General Public, Professional qualifications, State monopoly",
          "Does NOT include immoral trade, gambling or trafficking"
        ]
      ],
      "rows_ta": [
        [
          "உறுப்பு 19(1)(a)",
          "பேச்சு & கருத்து வெளிப்பாடு",
          "உறுப்பு 19(2)",
          "இறையாண்மை/ஒருமைப்பாடு, அரசின் பாதுகாப்பு, வெளிநாட்டு உறவுகள், பொது ஒழுங்கு, ஒழுக்கம், நீதிமன்ற அவமதிப்பு, அவதூறு, குற்றத் தூண்டுதல் (8 அடிப்படைகள்)",
          "பத்திரிகை சுதந்திரம், வணிக விளம்பரங்கள், அமைதி காக்கும் உரிமை அடங்கும்"
        ],
        [
          "உறுப்பு 19(1)(b)",
          "அமைதியான கூட்டம்",
          "உறுப்பு 19(3)",
          "இறையாண்மை & ஒருமைப்பாடு, பொது ஒழுங்கு (ஆயுதங்களின்றி)",
          "வேலைநிறுத்த உரிமை அல்லது வன்முறை கூட்டம் அடங்காது"
        ],
        [
          "உறுப்பு 19(1)(c)",
          "சங்கங்கள் & கூட்டுறவு",
          "உறுப்பு 19(4)",
          "இறையாண்மை & ஒருமைப்பாடு, பொது ஒழுங்கு, ஒழுக்கம்",
          "கூட்டுறவு சங்கங்கள் 97வது திருத்தம் 2011 மூலம் சேர்க்கப்பட்டது"
        ],
        [
          "உறுப்பு 19(1)(d)",
          "உள்நாட்டு இயக்கம்",
          "உறுப்பு 19(5)",
          "பொதுமக்களின் நலன், பழங்குடியினரின் (ST) நலன் பாதுகாப்பு",
          "உள்நாட்டு இயக்கம் மட்டுமே; வெளிநாட்டுப் பயணம் உறுப்பு 21"
        ],
        [
          "உறுப்பு 19(1)(e)",
          "வசிப்பிடம் & குடியேற்றம்",
          "உறுப்பு 19(5)",
          "பொதுமக்களின் நலன், பழங்குடியினரின் (ST) நலன் பாதுகாப்பு",
          "பழங்குடியின நிலப் பாதுகாப்பு பழங்குடியினரல்லாதோர் குடியேற்றத்தைக் கட்டுப்படுத்துகிறது"
        ],
        [
          "உறுப்பு 19(1)(g)",
          "தொழில் & வியாபாரம்",
          "உறுப்பு 19(6)",
          "பொதுமக்களின் நலன், தொழிற்கல்வித் தகுதிகள், அரசு முற்றுரிமை",
          "ஒழுக்கக்கேடான வர்த்தகம் அல்லது சூதாட்டம் அடங்காது"
        ]
      ]
    },
    {
      "id": "tbl_art19_restrictions",
      "title_en": "Article 19 Reasonable Restriction Clauses & Grounds",
      "title_ta": "உறுப்பு 19 நியாயமான கட்டுப்பாட்டு விதிகளும் அடிப்படைகளும்",
      "headers_en": [
        "Clause",
        "Restricted Freedom",
        "Constitutional Grounds Count",
        "Key Ground Highlights",
        "Judicial Test"
      ],
      "headers_ta": [
        "விதி",
        "கட்டுப்படுத்தப்பட்ட சுதந்திரம்",
        "அரசியலமைப்பு அடிப்படைகள் எண்ணிக்கை",
        "முக்கிய அடிப்படைகள் சிறப்பம்சம்",
        "நீதிமுறைச் சோதனை"
      ],
      "rows_en": [
        [
          "Article 19(2)",
          "Speech & Expression (19(1)(a))",
          "8 Grounds",
          "Sovereignty, Security, Public Order, Decency, Contempt, Defamation, Incitement",
          "Proportionality & Just balance"
        ],
        [
          "Article 19(3)",
          "Peaceful Assembly (19(1)(b))",
          "2 Grounds",
          "Sovereignty & Integrity of India, Public Order",
          "Police regulatory power under CrPC 144"
        ],
        [
          "Article 19(4)",
          "Associations & Unions (19(1)(c))",
          "3 Grounds",
          "Sovereignty & Integrity of India, Public Order, Morality",
          "Banning unlawful associations"
        ],
        [
          "Article 19(5)",
          "Movement & Residence (19(1)(d)/(e))",
          "2 Grounds",
          "Interests of General Public, Protection of Scheduled Tribes",
          "Inner Line Permit & Tribal Land laws"
        ],
        [
          "Article 19(6)",
          "Trade & Profession (19(1)(g))",
          "3 Grounds",
          "Interests of General Public, Technical Qualifications, State Monopoly",
          "Licensing & Nationalization laws"
        ]
      ],
      "rows_ta": [
        [
          "உறுப்பு 19(2)",
          "பேச்சு & கருத்து வெளிப்பாடு (19(1)(a))",
          "8 அடிப்படைகள்",
          "இறையாண்மை, பாதுகாப்பு, பொது ஒழுங்கு, ஒழுக்கம், அவமதிப்பு, அவதூறு, தூண்டுதல்",
          "விகிதாச்சாரத் தன்மை & நியாயமான சமநிலை"
        ],
        [
          "உறுப்பு 19(3)",
          "அமைதியான கூட்டம் (19(1)(b))",
          "2 அடிப்படைகள்",
          "இந்தியாவின் இறையாண்மை & ஒருமைப்பாடு, பொது ஒழுங்கு",
          "காவல்துறை ஒழுங்குமுறை அதிகாரம்"
        ],
        [
          "உறுப்பு 19(4)",
          "சங்கங்கள் & அமைப்புகள் (19(1)(c))",
          "3 அடிப்படைகள்",
          "இந்தியாவின் இறையாண்மை & ஒருமைப்பாடு, பொது ஒழுங்கு, ஒழுக்கம்",
          "சட்டவிரோத சங்கங்களைத் தடை செய்தல்"
        ],
        [
          "உறுப்பு 19(5)",
          "நடமாட்டம் & வசிப்பிடம் (19(1)(d)/(e))",
          "2 அடிப்படைகள்",
          "பொதுமக்களின் நலன், பழங்குடியினரின் (ST) நலன் பாதுகாப்பு",
          "இன்னர் லைன் பர்மிட் & பழங்குடியின நிலச் சட்டங்கள்"
        ],
        [
          "உறுப்பு 19(6)",
          "வியாபாரம் & தொழில் (19(1)(g))",
          "3 அடிப்படைகள்",
          "பொதுமக்களின் நலன், தொழிற்கல்வித் தகுதிகள், அரசு முற்றுரிமை",
          "உரிமம் & தேசியமயமாக்கல் சட்டங்கள்"
        ]
      ]
    },
    {
      "id": "tbl_art20_three_protections",
      "title_en": "Article 20 – Three Criminal Protections",
      "title_ta": "உறுப்பு 20 – மூன்று குற்றவியல் பாதுகாப்புகள்",
      "headers_en": [
        "Clause",
        "Protection Name",
        "Core Meaning",
        "Key Limitation / Scope",
        "TNPSC Trap"
      ],
      "headers_ta": [
        "விதி",
        "பாதுகாப்புப் பெயர்",
        "முதன்மைப் பொருள்",
        "முக்கிய வரம்பு / எல்லை",
        "டிஎன்பிஎஸ்சி பொறி"
      ],
      "rows_en": [
        [
          "Art 20(1)",
          "No Ex-Post-Facto Law",
          "No retroactive conviction or enhanced penalty for past acts",
          "Applies ONLY to Criminal Laws",
          "Does NOT apply to civil or tax liabilities"
        ],
        [
          "Art 20(2)",
          "No Double Jeopardy",
          "No person prosecuted and punished twice for same offence",
          "Applies ONLY before Courts of Law & Judicial Tribunals",
          "Departmental action + criminal trial is VALID"
        ],
        [
          "Art 20(3)",
          "No Self-Incrimination",
          "No accused compelled to be witness against himself",
          "Applies ONLY to Criminal Accused (Oral/Doc evidence)",
          "Thumb impressions, blood samples & handwriting are NOT protected"
        ]
      ],
      "rows_ta": [
        [
          "உறுப்பு 20(1)",
          "முந்தைய தேதியிட்ட சட்டத் தடை",
          "கடந்தகால செயல்களுக்கு முந்தைய தேதியிட்ட தண்டனையோ அதிக அபராதமோ இல்லை",
          "குற்றவியல் சட்டங்களுக்கு மட்டுமே பொருந்தும்",
          "சிவில் அல்லது வரிப் பொறுப்புகளுக்குப் பொருந்தாது"
        ],
        [
          "உறுப்பு 20(2)",
          "இரட்டை தண்டனைத் தடை",
          "ஒரே குற்றத்திற்காக இரண்டு முறை விசாரிக்கப்பட்டு தண்டிக்கப்படக்கூடாது",
          "நீதிமன்றங்கள் & நீதித்துறை தீர்ப்பாயங்களுக்கு மட்டுமே பொருந்தும்",
          "துறைசார் நடவடிக்கை + குற்றவியல் வழக்கு செல்லுபடியாகும்"
        ],
        [
          "உறுப்பு 20(3)",
          "தனக்குத்தானே எதிரான சாட்சியத் தடை",
          "குற்றம் சாட்டப்பட்டவர் தனக்குத்தானே எதிராக சாட்சியமளிக்க வற்புறுத்தப்படக்கூடாது",
          "குற்றவியல் பிரதிவாதிக்கு மட்டுமே பொருந்தும் (வாய்மொழி/ஆவணச் சான்று)",
          "கைரேகை, ரத்த மாதிரிகள் & கையெழுத்து மாதிரி பாதுகாக்கப்பட்டவை அல்ல"
        ]
      ]
    },
    {
      "id": "tbl_art20_vs_art21",
      "title_en": "Article 20 vs Article 21 (Non-Suspendable Rights)",
      "title_ta": "உறுப்பு 20 vs உறுப்பு 21 (இடைநிறுத்த முடியாத உரிமைகள்)",
      "headers_en": [
        "Dimension",
        "Article 20 (Criminal Conviction Protection)",
        "Article 21 (Life & Personal Liberty)"
      ],
      "headers_ta": [
        "பரிமாணம்",
        "உறுப்பு 20 (குற்றவியல் தண்டனைப் பாதுகாப்பு)",
        "உறுப்பு 21 (வாழ்வு & தனிநபர் சுதந்திரம்)"
      ],
      "rows_en": [
        [
          "Core Subject",
          "Protections against ex-post-facto law, double jeopardy, self-incrimination",
          "Protection of life and personal liberty except by procedure established by law"
        ],
        [
          "Target Scope",
          "Accused persons in criminal justice system",
          "All individuals (Citizens and Foreigners) in all general spheres"
        ],
        [
          "Emergency Protection",
          "CANNOT be suspended during National Emergency (44th CAA 1978)",
          "CANNOT be suspended during National Emergency (44th CAA 1978)"
        ],
        [
          "Judicial Expansion",
          "Specific constitutional protections strictly construed",
          "Expansive judicial interpretation (Privacy, Dignity, Environment, Due Process)"
        ]
      ],
      "rows_ta": [
        [
          "முதன்மை விஷயம்",
          "முந்தைய தேதியிட்ட சட்டம், இரட்டை தண்டனை, தனக்குத்தானே சாட்சியத்திற்கு எதிரான பாதுகாப்புகள்",
          "சட்டத்தால் நிறுவப்பட்ட நடைமுறையின்படியன்றி வாழ்வு & தனிநபர் சுதந்திரப் பாதுகாப்பு"
        ],
        [
          "இலக்கு எல்லை",
          "குற்றவியல் நீதி அமைப்பில் குற்றம் சாட்டப்பட்ட நபர்கள்",
          "அனைத்து பொதுப் பகுதிகளிலும் உள்ள அனைத்து நபர்களும் (குடிமக்கள் & வெளிநாட்டினர்)"
        ],
        [
          "அவசரநிலை பாதுகாப்பு",
          "தேசிய அவசரநிலையின் போது இடைநிறுத்த முடியாது (44வது திருத்தம் 1978)",
          "தேசிய அவசரநிலையின் போது இடைநிறுத்த முடியாது (44வது திருத்தம் 1978)"
        ],
        [
          "நீதிமுறை விரிவாக்கம்",
          "குறிப்பிட்ட அரசியலமைப்பு பாதுகாப்புகள் கண்டிப்பாகப் பின்பற்றப்படுகின்றன",
          "விரிவான நீதிமுறை விளக்கம் (ரகசிய உரிமை, கண்ணியம், சுற்றுச்சூழல்)"
        ]
      ]
    },
    {
      "id": "tbl_art21_vs_art21a",
      "title_en": "Article 21 vs Article 21A Comparison",
      "title_ta": "உறுப்பு 21 vs உறுப்பு 21A ஒப்பீடு",
      "headers_en": [
        "Dimension",
        "Article 21",
        "Article 21A"
      ],
      "headers_ta": [
        "பரிமாணம்",
        "உறுப்பு 21",
        "உறுப்பு 21A"
      ],
      "rows_en": [
        [
          "Core Subject",
          "Protection of Life and Personal Liberty",
          "Right to Free and Compulsory Education"
        ],
        [
          "Beneficiaries",
          "ALL Persons (Citizens and Foreigners)",
          "Children aged SIX to FOURTEEN years (6–14 years)"
        ],
        [
          "Constitutional Insertion",
          "Original 1950 Constitution",
          "Added by 86th Constitutional Amendment Act, 2002"
        ],
        [
          "Operational Legislation",
          "Judicial interpretation & specific procedural laws",
          "Right to Education (RTE) Act, 2009 (Enforced April 1, 2010)"
        ]
      ],
      "rows_ta": [
        [
          "முதன்மை விஷயம்",
          "வாழ்வு மற்றும் தனிநபர் சுதந்திரப் பாதுகாப்பு",
          "இலவச மற்றும் கட்டாயக் கல்வி உரிமை"
        ],
        [
          "பயனாளிகள்",
          "அனைத்து நபர்களும் (குடிமக்கள் மற்றும் வெளிநாட்டினர்)",
          "ஆறு முதல் பதினான்கு வயது வரையிலான குழந்தைகள் (6-14 ஆண்டுகள்)"
        ],
        [
          "அரசியலமைப்புச் சேர்ப்பு",
          "அசல் 1950 அரசியலமைப்பு",
          "2002-ன் 86வது அரசியலமைப்பு திருத்தச் சட்டத்தால் சேர்க்கப்பட்டது"
        ],
        [
          "செயல்பாட்டுச் சட்டம்",
          "நீதித்துறை விளக்கம் & குறிப்பிட்ட நடைமுறைச் சட்டங்கள்",
          "கல்வி உரிமைச் சட்டம் (RTE Act) 2009 (ஏப்ரல் 1, 2010 முதல் அமல்)"
        ]
      ]
    },
    {
      "id": "tbl_punitive_vs_preventive",
      "title_en": "Punitive Detention vs Preventive Detention",
      "title_ta": "தண்டனைக்காவல் vs தடுப்புக் காவல்",
      "headers_en": [
        "Feature",
        "Punitive Detention",
        "Preventive Detention"
      ],
      "headers_ta": [
        "அம்சம்",
        "தண்டனைக்காவல் (Punitive)",
        "தடுப்புக் காவல் (Preventive)"
      ],
      "rows_en": [
        [
          "Basis & Timing",
          "Detention AFTER offence is committed, following judicial trial and conviction",
          "Detention BEFORE offence is committed, based on suspicion to prevent future crime"
        ],
        [
          "Constitutional Goal",
          "Punitive justice for past illegal act",
          "Precautionary prevention for state security/public order"
        ],
        [
          "Right to Lawyer & Magistrate",
          "Guaranteed (Grounds info, Lawyer choice, 24h Magistrate production under Art 22(1)/(2))",
          "NOT available (Art 22(3) exception applies)"
        ],
        [
          "Maximum Period",
          "As sentenced by Court of Law",
          "Max 3 months without Advisory Board approval (Art 22(4))"
        ]
      ],
      "rows_ta": [
        [
          "அடிப்படை & நேரம்",
          "நீதிமன்ற விசாரணை மற்றும் தண்டனைக்குப் பிறகு குற்றம் செய்யப்பட்ட பின் கைது",
          "எதிர்காலக் குற்றத்தைத் தடுக்கும் சந்தேகத்தின் பேரில் குற்றம் செய்வதற்கு முன் கைது"
        ],
        [
          "அரசியலமைப்பு இலக்கு",
          "கடந்தகால சட்டவிரோத செயலுக்கான தண்டனை நீதி",
          "மாநிலப் பாதுகாப்பு/பொது ஒழுங்கிற்கான முன்னெச்சரிக்கை தடுப்பு"
        ],
        [
          "வழக்கறிஞர் & நடுவர் உரிமை",
          "உத்தரவாதம் அளிக்கப்பட்டது (காரணங்கள், வழக்கறிஞர், 24 மணி நேர நடுவர்)",
          "கிடைக்காது (உறுப்பு 22(3) விலக்கு பொருந்தும்)"
        ],
        [
          "அதிகபட்சக் காலம்",
          "நீதிமன்றம் விதித்த தண்டனையின்படி",
          "ஆலோசனை வாரிய ஒப்புதலின்றி அதிகபட்சம் 3 மாதங்கள் (உறுப்பு 22(4))"
        ]
      ]
    },
    {
      "id": "tbl_art22_arrest_safeguards",
      "title_en": "Article 22 Ordinary Arrest Safeguards",
      "title_ta": "உறுப்பு 22 சாதாரண கைது பாதுகாப்புகள்",
      "headers_en": [
        "Safeguard Clause",
        "Right Description",
        "Operational Detail",
        "Exceptions / Exclusion"
      ],
      "headers_ta": [
        "பாதுகாப்பு விதி",
        "உரிமை விளக்கம்",
        "செயல்பாட்டு விவரம்",
        "விலக்குகள் / சேர்க்கப்படாதவை"
      ],
      "rows_en": [
        [
          "Article 22(1)",
          "Grounds of Arrest Information",
          "Must be informed as soon as possible of reasons for arrest",
          "Preventive detenu & Enemy aliens exempt"
        ],
        [
          "Article 22(1)",
          "Legal Representation",
          "Right to consult and be defended by legal practitioner of choice",
          "State must allow access to legal counsel"
        ],
        [
          "Article 22(2)",
          "24-Hour Magistrate Production",
          "Must be produced before nearest magistrate within 24 hours",
          "EXCLUDES time necessary for journey to court"
        ],
        [
          "Article 22(2)",
          "Release after 24 Hours",
          "Cannot be detained beyond 24h without magistrate judicial custody order",
          "Preventive detenu governed by Art 22(4)"
        ]
      ],
      "rows_ta": [
        [
          "உறுப்பு 22(1)",
          "கைதுக்கான காரணங்கள் அறிவிப்பு",
          "கைதுக்கான காரணங்களை உடனடியாக அறிந்து கொள்ளும் உரிமை",
          "தடுப்புக் காவலில் உள்ளோர் & எதிரி நாட்டினர் விலக்கு"
        ],
        [
          "உறுப்பு 22(1)",
          "வழக்கறிஞர் பிரதிநிதித்துவம்",
          "தான் விரும்பும் வழக்கறிஞரை ஆலோசிக்கவும் பிரதிநிதித்துவப்படுத்தவும் உரிமை",
          "சட்ட ஆலோசகரை அணுக அரசு அனுமதிக்க வேண்டும்"
        ],
        [
          "உறுப்பு 22(2)",
          "24 மணி நேர நடுவர் ஆஜர்",
          "24 மணி நேரத்திற்குள் அருகிலுள்ள நடுவரிடம் ஆஜர்படுத்தப்பட வேண்டும்",
          "நீதிமன்றத்திற்கான பயண நேரம் சேர்க்கப்படாது"
        ],
        [
          "உறுப்பு 22(2)",
          "24 மணி நேரத்திற்குப் பின் விடுதலை",
          "நடுவர் உத்தரவின்றி 24 மணி நேரத்திற்கு மேல் காவலில் வைக்க முடியாது",
          "தடுப்புக் காவலில் உள்ளோர் உறுப்பு 22(4) மூலம் ஆளப்படுகின்றனர்"
        ]
      ]
    },
    {
      "id": "tbl_art23_vs_art24",
      "title_en": "Article 23 vs Article 24 (Right Against Exploitation)",
      "title_ta": "உறுப்பு 23 vs உறுப்பு 24 (சுரண்டலுக்கு எதிரான உரிமை)",
      "headers_en": [
        "Dimension",
        "Article 23",
        "Article 24"
      ],
      "headers_ta": [
        "பரிமாணம்",
        "உறுப்பு 23",
        "உறுப்பு 24"
      ],
      "rows_en": [
        [
          "Target Exploitation",
          "Human Trafficking, Begar (unpaid work), and Forced Labour",
          "Employment of Children in Hazardous Work (factories, mines)"
        ],
        [
          "Target Beneficiaries",
          "ALL Persons (Men, Women, Children)",
          "Children aged below FOURTEEN years (< 14 years)"
        ],
        [
          "Enforceability",
          "Enforceable against BOTH State and Private Individuals",
          "Enforceable against employers in state & private hazardous units"
        ],
        [
          "Constitutional Exception",
          "Compulsory service for public purposes (Art 23(2)) without religion/race/caste/class discrimination",
          "ABSOLUTE prohibition in hazardous work; no state exception"
        ]
      ],
      "rows_ta": [
        [
          "இலக்குச் சுரண்டல்",
          "மனித வியாபாரம், வெட்டி வேலை (begar) மற்றும் கட்டாய வேலை",
          "ஆபத்தான வேலைகளில் (தொழிற்சாலைகள், சுரங்கங்கள்) குழந்தை தொழிலாளர்கள்"
        ],
        [
          "இலக்கு பயனாளிகள்",
          "அனைத்து நபர்களும் (ஆண்கள், பெண்கள், குழந்தைகள்)",
          "பதினான்கு வயதுக்குட்பட்ட குழந்தைகள் (< 14 ஆண்டுகள்)"
        ],
        [
          "அமலாக்கம்",
          "அரசு மற்றும் தனியார் தனிநபர்கள் இருவருக்கும் எதிராகப் பொருந்தும்",
          "அரசு & தனியார் ஆபத்தான நிறுவன முதலாளிகளுக்கு எதிராகப் பொருந்தும்"
        ],
        [
          "அரசியலமைப்பு விலக்கு",
          "பொது நோக்கங்களுக்கான கட்டாயச் சேவை (உறுப்பு 23(2))",
          "ஆபத்தான பணிகளில் முழுமையான தடை; அரசுக்கு விலக்கு இல்லை"
        ]
      ]
    }
  ],
  "concept_map": [
    {
      "id": "mm_fr2_root",
      "parent_id": None,
      "title": "Fundamental Rights Part 2 (அடிப்படை உரிமைகள் - பகுதி 2)",
      "short_label": "FR Part 2"
    },
    {
      "id": "mm_freedom_root",
      "parent_id": "mm_fr2_root",
      "title": "Right to Freedom (Articles 19 to 22)",
      "short_label": "Right to Freedom"
    },
    {
      "id": "mm_art19",
      "parent_id": "mm_freedom_root",
      "title": "Article 19: 6 Freedoms for Citizens ONLY & Reasonable Restrictions (19(2)-19(6))",
      "short_label": "Art 19: 6 Freedoms"
    },
    {
      "id": "mm_art20",
      "parent_id": "mm_freedom_root",
      "title": "Article 20: 3 Criminal Protections (No Ex-Post-Facto, No Double Jeopardy, No Self-Incrimination)",
      "short_label": "Art 20: Conviction"
    },
    {
      "id": "mm_art21",
      "parent_id": "mm_freedom_root",
      "title": "Article 21: Life & Personal Liberty (Procedure Established by Law -> Due Process, Privacy)",
      "short_label": "Art 21: Life & Liberty"
    },
    {
      "id": "mm_art21a",
      "parent_id": "mm_freedom_root",
      "title": "Article 21A: Right to Education for 6-14 years (86th CAA 2002; RTE Act 2009)",
      "short_label": "Art 21A: Education"
    },
    {
      "id": "mm_art22",
      "parent_id": "mm_freedom_root",
      "title": "Article 22: Ordinary Arrest Rights & Preventive Detention (Max 3 Months)",
      "short_label": "Art 22: Arrest & Detention"
    },
    {
      "id": "mm_exploitation_root",
      "parent_id": "mm_fr2_root",
      "title": "Right Against Exploitation (Articles 23 & 24)",
      "short_label": "Against Exploitation"
    },
    {
      "id": "mm_art23",
      "parent_id": "mm_exploitation_root",
      "title": "Article 23: Prohibition of Human Trafficking, Begar & Forced Labour",
      "short_label": "Art 23: Begar & Traffic"
    },
    {
      "id": "mm_art24",
      "parent_id": "mm_exploitation_root",
      "title": "Article 24: Prohibition of Child Labour below 14 in Hazardous Work",
      "short_label": "Art 24: Child Labour"
    }
  ],
  "revision_cards": [
    {
      "id": "RC_FR2_001",
      "title": {
        "en": "Article 19 Citizen Availability",
        "ta": "உறுப்பு 19 குடிமக்கள் தகுதி"
      },
      "front": {
        "en": "To whom are the six fundamental freedoms under Article 19 available?",
        "ta": "உறுப்பு 19-ன் கீழ் உள்ள ஆறு அடிப்படை சுதந்திரங்கள் யாருக்கு மட்டுமே கிடைக்கும்?"
      },
      "back": {
        "en": "ONLY to Citizens of India. They are NOT available to foreigners or legal entities like corporations.",
        "ta": "இந்தியக் குடிமக்களுக்கு மட்டுமே. இவை வெளிநாட்டினருக்கோ கார்ப்பரேஷன்கள் போன்ற சட்டப்பூர்வ அமைப்புகளுக்கோ கிடைக்காது."
      },
      "one_line_revision": "Article 19 Freedoms = Available ONLY to Citizens of India.",
      "type": "trap"
    },
    {
      "id": "RC_FR2_002",
      "title": {
        "en": "Article 19(1)(c) Cooperative Societies",
        "ta": "உறுப்பு 19(1)(c) கூட்டுறவு சங்கங்கள்"
      },
      "front": {
        "en": "Which Constitutional Amendment added 'cooperative societies' to Article 19(1)(c)?",
        "ta": "உறுப்பு 19(1)(c)-ல் 'கூட்டுறவு சங்கங்கள்' என்பதைச் சேர்த்த அரசியலமைப்பு திருத்தம் எது?"
      },
      "back": {
        "en": "97th Constitutional Amendment Act, 2011.",
        "ta": "2011-ன் 97வது அரசியலமைப்பு திருத்தச் சட்டம்."
      },
      "one_line_revision": "97th CAA 2011 = Added 'cooperative societies' to Art 19(1)(c).",
      "type": "fact"
    },
    {
      "id": "RC_FR2_003",
      "title": {
        "en": "Article 20 Ex-Post-Facto Scope",
        "ta": "உறுப்பு 20(1) முந்தைய தேதியிட்ட சட்ட எல்லை"
      },
      "front": {
        "en": "Does Article 20(1) protection against ex-post-facto laws apply to civil liabilities?",
        "ta": "உறுப்பு 20(1) முந்தைய தேதியிட்ட சட்டப் பாதுகாப்பு சிவில் பொறுப்புகளுக்குப் பொருந்துமா?"
      },
      "back": {
        "en": "NO. Article 20(1) applies ONLY to Criminal laws. Retrospective civil liabilities or tax laws are FULLY VALID.",
        "ta": "இல்லை. உறுப்பு 20(1) குற்றவியல் சட்டங்களுக்கு மட்டுமே பொருந்தும். முந்தைய தேதியிட்ட சிவில் அல்லது வரிப் பொறுப்புகள் செல்லுபடியாகும்."
      },
      "one_line_revision": "Art 20(1) No Ex-Post-Facto = Criminal laws ONLY; Civil/tax retrospective valid.",
      "type": "trap"
    },
    {
      "id": "RC_FR2_004",
      "title": {
        "en": "Article 20 Double Jeopardy Limit",
        "ta": "உறுப்பு 20(2) இரட்டை தண்டனை வரம்பு"
      },
      "front": {
        "en": "Does departmental dismissal followed by criminal prosecution constitute Double Jeopardy under Article 20(2)?",
        "ta": "துறைசார் பணிநீக்கத்தைத் தொடர்ந்து குற்றவியல் வழக்குத் தொடர்வது உறுப்பு 20(2)-ன் கீழ் இரட்டை தண்டனை ஆகுமா?"
      },
      "back": {
        "en": "NO. Double jeopardy applies ONLY before Courts of Law or Judicial Tribunals. Departmental action + criminal trial is VALID.",
        "ta": "இல்லை. இரட்டை தண்டனைத் தடை நீதிமன்றங்கள்/நீதித்துறை தீர்ப்பாயங்களுக்கு மட்டுமே பொருந்தும். துறைசார் நடவடிக்கை + குற்றவியல் வழக்கு செல்லுபடியாகும்."
      },
      "one_line_revision": "Art 20(2) Double Jeopardy = Courts/Tribunals ONLY; Departmental action exempt.",
      "type": "trap"
    },
    {
      "id": "RC_FR2_005",
      "title": {
        "en": "Maneka Gandhi Case 1978",
        "ta": "மேனகா காந்தி வழக்கு 1978"
      },
      "front": {
        "en": "What landmark principle did the Supreme Court establish in Maneka Gandhi case (1978) regarding Article 21?",
        "ta": "மேனகா காந்தி வழக்கில் (1978) உறுப்பு 21 தொடர்பாக உச்ச நீதிமன்றம் நிறுவிய மைல்கல் கோட்பாடு என்ன?"
      },
      "back": {
        "en": "Overruled Gopalan case; held that procedure depriving personal liberty must be JUST, FAIR, AND REASONABLE (introduced Due Process of Law). Formed Golden Triangle (Arts 14, 19, 21).",
        "ta": "கோபாலன் வழக்கைத் தலைகீழாக மாற்றியது; தனிநபர் சுதந்திரத்தைப் பறிக்கும் நடைமுறை நியாயமானதாகவும் நேர்மையானதாகவும் இருக்க வேண்டும் எனக் கூறியது (சட்டத்தின் உரிய நடைமுறை). தங்க முக்கோணத்தை உருவாக்கியது (14, 19, 21)."
      },
      "one_line_revision": "Maneka Gandhi 1978 = Art 21 procedure must be just, fair, reasonable (Due Process).",
      "type": "concept"
    },
    {
      "id": "RC_FR2_006",
      "title": {
        "en": "Article 21A RTE Amendment",
        "ta": "உறுப்பு 21A RTE திருத்தம்"
      },
      "front": {
        "en": "Which Amendment Act introduced Article 21A and what is the target age group?",
        "ta": "உறுப்பு 21A-ஐ அறிமுகப்படுத்திய திருத்தச் சட்டம் எது மற்றும் அதன் இலக்கு வயதுக் குழு என்ன?"
      },
      "back": {
        "en": "86th Constitutional Amendment Act, 2002. Free and compulsory education for children aged 6 to 14 years.",
        "ta": "2002-ன் 86வது அரசியலமைப்பு திருத்தச் சட்டம். 6 முதல் 14 வயது வரையிலான குழந்தைகளுக்கான இலவச & கட்டாயக் கல்வி."
      },
      "one_line_revision": "Art 21A = 86th CAA 2002 for children aged 6 to 14 years.",
      "type": "fact"
    },
    {
      "id": "RC_FR2_007",
      "title": {
        "en": "Preventive Detention Maximum Period",
        "ta": "தடுப்புக் காவல் அதிகபட்சக் காலம்"
      },
      "front": {
        "en": "What is the maximum period of Preventive Detention without Advisory Board approval under Article 22(4)?",
        "ta": "உறுப்பு 22(4)-ன் கீழ் ஆலோசனை வாரிய ஒப்புதலின்றி தடுப்புக் காவலில் வைக்கக்கூடிய அதிகபட்சக் காலம் என்ன?"
      },
      "back": {
        "en": "THREE MONTHS (3 Months). Note: 44th CAA provision reducing to 2 months was never notified.",
        "ta": "மூன்று மாதங்கள் (3 மாதங்கள்). குறிப்பு: 2 மாதங்களாகக் குறைக்கும் 44வது திருத்த விதி நடைமுறைப்படுத்தப்படவில்லை."
      },
      "one_line_revision": "Preventive Detention Max Period (without Advisory Board) = 3 Months.",
      "type": "trap"
    },
    {
      "id": "RC_FR2_008",
      "title": {
        "en": "Article 23 Begar & Trafficking",
        "ta": "உறுப்பு 23 வெட்டி வேலை & மனித வியாபாரம்"
      },
      "front": {
        "en": "What three forms of exploitation are prohibited under Article 23(1)?",
        "ta": "உறுப்பு 23(1)-ன் கீழ் தடைசெய்யப்பட்ட மூன்று வகையான சுரண்டல்கள் யாவை?"
      },
      "back": {
        "en": "1. Traffic in human beings, 2. Begar (unpaid involuntary work), 3. Other similar forms of forced labour.",
        "ta": "1. மனித வியாபாரம், 2. வெட்டி வேலை (ஊதியமில்லா வேலை), 3. பிற கட்டாய வேலை வடிவங்கள்."
      },
      "one_line_revision": "Art 23 = Prohibits Human Trafficking, Begar, and Forced Labour against State & Private.",
      "type": "fact"
    },
    {
      "id": "RC_FR2_009",
      "title": {
        "en": "Article 23(2) Compulsory Service Exception",
        "ta": "உறுப்பு 23(2) கட்டாயச் சேவை விலக்கு"
      },
      "front": {
        "en": "Which ground is OMITTED from the non-discrimination list in Article 23(2) compulsory public service exception?",
        "ta": "உறுப்பு 23(2) கட்டாயப் பொதுச் சேவை விலக்கில் பாகுபாடின்மைப் பட்டியலிலிருந்து விடுவிக்கப்பட்ட அடிப்படை எது?"
      },
      "back": {
        "en": "'SEX'. State shall not discriminate on grounds only of Religion, Race, Caste, or Class (Sex is omitted).",
        "ta": "'பாலினம்' (SEX). அரசு மதம், இனம், சாதி, வகுப்பு ஆகியவற்றில் மட்டுமே பாகுபாடு காட்டக்கூடாது (பாலினம் விடுக்கப்பட்டுள்ளது)."
      },
      "one_line_revision": "Art 23(2) Exception = Prohibits discrimination on Religion, Race, Caste, Class ('Sex' omitted).",
      "type": "trap"
    },
    {
      "id": "RC_FR2_010",
      "title": {
        "en": "Article 24 Child Labour Prohibition",
        "ta": "உறுப்பு 24 குழந்தை தொழிலாளர் தடை"
      },
      "front": {
        "en": "What is the age limit and work scope under Article 24?",
        "ta": "உறுப்பு 24-ன் கீழ் உள்ள வயது வரம்பு மற்றும் வேலை எல்லை என்ன?"
      },
      "back": {
        "en": "Children below 14 YEARS prohibited from employment in FACTORIES, MINES, or HAZARDOUS occupations.",
        "ta": "14 வயதுக்குட்பட்ட குழந்தைகள் தொழிற்சாலைகள், சுரங்கங்கள் அல்லது ஆபத்தான வேலைகளில் வேலைக்கு அமர்த்தப்படுவது தடை செய்யப்பட்டுள்ளது."
      },
      "one_line_revision": "Art 24 = Prohibits child labour below 14 years in HAZARDOUS work.",
      "type": "fact"
    }
  ]
}

target_file = "data/notes/polity/fundamental_rights_part_2.json"
os.makedirs(os.path.dirname(target_file), exist_ok=True)

with open(target_file, "w", encoding="utf-8") as f:
    json.dump(notes_data, f, ensure_ascii=False, indent=2)

print(f"Successfully updated '{target_file}' with 8 comparison tables, mind map, and expanded content!")
