# -*- coding: utf-8 -*-
"""
Master Notes Builder for Fundamental Rights – Part 3 (Bilingual)
Subject: Indian Polity
Topic: Fundamental Rights – Part 3 (Part 3 of 3)
Target Output: data/notes/polity/fundamental_rights_part_3.json
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

notes_data = {
  "meta": {
    "topic_id": "polity_fundamental_rights_part_3",
    "repository_id": "polity_fundamental_rights",
    "display_title": "Fundamental Rights – Part 3",
    "part": 3,
    "total_parts": 3,
    "subject": "polity",
    "chapter": "Fundamental Rights",
    "language": "English + Tamil"
  },
  "metadata": {
    "version": "1.0",
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
    "Freedom of Religion",
    "மத சுதந்திர உரிமை",
    "Article 25 Conscience Profession",
    "உறுப்பு 25 மனச்சாட்சி சுதந்திரம்",
    "Article 26 Religious Affairs",
    "உறுப்பு 26 மத விவகாரங்கள் மேலாண்மை",
    "Article 27 Religious Tax Immunity",
    "உறுப்பு 27 மத வரிவிலக்கு",
    "Article 28 Religious Instruction",
    "உறுப்பு 28 மதக் கல்வி போதனை",
    "Article 29 Cultural Interests",
    "உறுப்பு 29 பண்பாட்டு நலம் பாதுகாப்பு",
    "Article 30 Minority Educational Institutions",
    "உறுப்பு 30 சிறுபான்மையினர் கல்வி நிறுவனங்கள்",
    "Article 31 Right to Property",
    "உறுப்பு 31 சொத்துரிமை",
    "Article 300A Legal Right",
    "உறுப்பு 300A சட்டப்பூர்வ உரிமை",
    "Article 32 Constitutional Remedies",
    "உறுப்பு 32 அரசியலமைப்புத் தீர்வுகள்",
    "Five Writs",
    "ஐந்து பேராணைகள்",
    "Habeas Corpus",
    "ஆட்கொணர்வு பேராணை",
    "Mandamus",
    "செயலுறுத்தும் பேராணை",
    "Prohibition",
    "தடைசெய் பேராணை",
    "Certiorari",
    "நெறிமுறையுறுத்தும் பேராணை",
    "Quo Warranto",
    "தகுதி வினா பேராணை",
    "Article 33 Armed Forces",
    "உறுப்பு 33 ஆயுதப் படைகள்",
    "Article 34 Martial Law",
    "உறுப்பு 34 ராணுவ சட்டம்",
    "Article 35 Parliamentary Law Power",
    "உறுப்பு 35 நாடாளுமன்ற சட்ட அதிகாரம்",
    "FR vs DPSP",
    "அடிப்படை உரிமைகள் vs அரசு நெறிமுறைக் கோட்பாடுகள்"
  ],
  "learning_outcomes": {
    "Understand": {
      "en": [
        "Understand Articles 25 to 28 establishing individual and collective freedom of religion, secularism, and exemption from religious taxation.",
        "Understand Articles 29 and 30 safeguarding cultural, linguistic, and educational rights of minorities and distinct sections of citizens.",
        "Understand the historical transfer of the Right to Property from Article 31 (Part III) to Article 300A (Part XII) via the 44th CAA 1978.",
        "Understand Article 32, Dr. B.R. Ambedkar's 'heart and soul' description, and the scope of the Five Writs (Habeas Corpus, Mandamus, Prohibition, Certiorari, Quo Warranto).",
        "Understand Articles 33-35, Article 300A, and the complementary relationships between Fundamental Rights, DPSPs, Fundamental Duties, and the Preamble."
      ],
      "ta": [
        "தனிநபர் மற்றும் கூட்டு மத சுதந்திரம், மதச்சார்பின்மை மற்றும் மத வரிவிலக்கு ஆகியவற்றை நிறுவும் உறுப்புகள் 25 முதல் 28 வரை புரிந்து கொள்ளுதல்.",
        "சிறுபான்மையினர் மற்றும் குடிமக்களின் பண்பாட்டு, மொழி மற்றும் கல்வி உரிமைகளைப் பாதுகாக்கும் உறுப்புகள் 29 மற்றும் 30-ஐப் புரிந்து கொள்ளுதல்.",
        "1978-ன் 44வது திருத்தத்தின் மூலம் சொத்துரிமை உறுப்பு 31 லிருந்து உறுப்பு 300A-க்கு மாற்றப்பட்ட வரலாற்று வளர்ச்சியைப் புரிந்து கொள்ளுதல்.",
        "அம்பேத்கரின் 'இதயமும் ஆன்மாவும்' என விவரிக்கப்பட்ட உறுப்பு 32 மற்றும் ஐந்து நீதிப் பேராணைகளின் எல்லையைப் புரிந்து கொள்ளுதல்.",
        "உறுப்புகள் 33-35, உறுப்பு 300A மற்றும் அடிப்படை உரிமைகள், DPSP, அடிப்படை கடமைகள், முகவுரை இடையேயான தொடர்புகளைப் புரிந்து கொள்ளுதல்."
      ]
    },
    "Remember": {
      "en": [
        "Remember that Article 29(1) applies to ANY section of citizens (not exclusively to minorities).",
        "Remember that Article 30 guarantees educational institution rights to Religious and Linguistic minorities only.",
        "Remember that the Right to Property was made a legal right under Article 300A in Part XII by the 44th Constitutional Amendment Act, 1978.",
        "Remember that Article 32 is specifically for enforcement of Fundamental Rights and is itself a Fundamental Right.",
        "Remember that Quo Warranto is the only writ that can be sought by any interested person, not strictly the aggrieved party."
      ],
      "ta": [
        "உறுப்பு 29(1) அனைத்துக் குடிமக்கள் பிரிவினருக்கும் பொருந்தும் (சிறுபான்மையினருக்கு மட்டுமே அல்ல) என்பதை நினைவில் கொள்ளுதல்.",
        "உறுப்பு 30 மத மற்றும் மொழி சிறுபான்மையினருக்கு மட்டுமே கல்வி நிறுவன உரிமைகளை உத்தரவாதம் செய்கிறது என்பதை நினைவில் கொள்ளுதல்.",
        "1978-ன் 44வது திருத்தச் சட்டத்தால் சொத்துரிமை பகுதி XII-ல் உறுப்பு 300A இன் கீழ் சட்டப்பூர்வ உரிமையாக்கப்பட்டதை நினைவில் கொள்ளுதல்.",
        "உறுப்பு 32 அடிப்படை உரிமைகளை அமல்படுத்துவதற்காக மட்டுமே மற்றும் அதுவே ஒரு அடிப்படை உரிமை என்பதை நினைவில் கொள்ளுதல்.",
        "தகுதி வினா பேராணை (Quo Warranto) மட்டுமே பாதிக்கப்பட்ட நபர் மட்டுமின்றி எந்தவொரு ஆர்வமுள்ள நபராலும் கேட்கப்படலாம் என்பதை நினைவில் கொள்ளுதல்."
      ]
    },
    "Analyze": {
      "en": [
        "Analyze the distinction between Article 25 (Individual Freedom of Religion) and Article 26 (Collective Denominational Freedom).",
        "Analyze the jurisdictional and constitutional differences between Article 32 (Supreme Court FR writ jurisdiction) and Article 226 (High Court wider writ jurisdiction).",
        "Analyze the operational scope of Prohibition (preventative judicial writ) vs Certiorari (curative/preventative judicial and administrative writ).",
        "Analyze the historical conflict and basic structure harmony between Fundamental Rights (Part III) and Directive Principles (Part IV) per Minerva Mills (1980)."
      ],
      "ta": [
        "உறுப்பு 25 (தனிநபர் மத சுதந்திரம்) மற்றும் உறுப்பு 26 (கூட்டு சமயக் குழு சுதந்திரம்) இடையேயான வேறுபாட்டை பகுப்பாய்வு செய்தல்.",
        "உறுப்பு 32 (உச்ச நீதிமன்ற அடிப்படை உரிமை மனு அதிகாரம்) மற்றும் உறுப்பு 226 (உயர் நீதிமன்ற விரிவான மனு அதிகாரம்) இடையேயான வேறுபாடுகளை பகுப்பாய்வு செய்தல்.",
        "தடைசெய் பேராணை (Prohibition) vs நெறிமுறையுறுத்தும் பேராணை (Certiorari) ஆகியவற்றின் செயல்பாட்டு எல்லையை பகுப்பாய்வு செய்தல்.",
        "அடிப்படை உரிமைகள் (பகுதி III) மற்றும் அரசு நெறிமுறைக் கோட்பாடுகள் (பகுதி IV) இடையேயான நல்லிணக்கத்தைப் பகுப்பாய்வு செய்தல் (மினர்வா மில்ஸ் 1980)."
      ]
    },
    "Apply": {
      "en": [
        "Identify TNPSC trap points regarding Article 29 citizen scope, Article 27 fee vs tax distinction, and Article 33 parliamentary exclusivity.",
        "Apply constitutional rules to distinguish between the Five Writs in scenario-based MCQs."
      ],
      "ta": [
        "உறுப்பு 29 குடிமக்கள் எல்லை, உறுப்பு 27 கட்டணம் vs வரி வேறுபாடு மற்றும் உறுப்பு 33 நாடாளுமன்ற பிரத்யேக அதிகாரம் பற்றிய டிஎன்பிஎஸ்சி பொறி புள்ளிகளைக் கண்டறிதல்.",
        "சூழ்நிலை சார்ந்த கேள்விகளில் ஐந்து நீதிப் பேராணைகளை வேறுபடுத்த அரசியலமைப்பு விதிகளைப் பயன்படுத்துதல்."
      ]
    }
  },
  "subject": "Polity",
  "topic": "Fundamental Rights – Part 3",
  "language": "bilingual",
  "ui_type": "polity",
  "sections": [
    {
      "id": "sec_article_25",
      "title_en": "1. Article 25: Individual Freedom of Conscience & Religion",
      "title_ta": "1. உறுப்பு 25: தனிநபர் மனச்சாட்சி மற்றும் மத சுதந்திரம்",
      "type": "standard_topic"
    },
    {
      "id": "sec_article_26",
      "title_en": "2. Article 26: Freedom to Manage Religious Affairs (Denominational Rights)",
      "title_ta": "2. உறுப்பு 26: மத விவகாரங்களை நிர்வகிக்கும் சுதந்திரம்",
      "type": "standard_topic"
    },
    {
      "id": "sec_article_27",
      "title_en": "3. Article 27: Freedom from Taxation for Promoting a Particular Religion",
      "title_ta": "3. உறுப்பு 27: குறிப்பிட்ட மதத்தை ஊக்குவிக்க வரி செலுத்தலிலிருந்து சுதந்திரம்",
      "type": "standard_topic"
    },
    {
      "id": "sec_article_28",
      "title_en": "4. Article 28: Freedom from Attending Religious Instruction in Educational Institutions",
      "title_ta": "4. உறுப்பு 28: கல்வி நிறுவனங்களில் மத போதனைகளில் பங்கேற்பதிலிருந்து சுதந்திரம்",
      "type": "standard_topic"
    },
    {
      "id": "sec_article_29",
      "title_en": "5. Article 29: Protection of Language, Script & Culture of Minorities & Citizens",
      "title_ta": "5. உறுப்பு 29: சிறுபான்மையினர் & குடிமக்களின் மொழி, எழுத்து, பண்பாட்டுப் பாதுகாப்பு",
      "type": "standard_topic"
    },
    {
      "id": "sec_article_30",
      "title_en": "6. Article 30: Right of Religious & Linguistic Minorities to Establish Educational Institutions",
      "title_ta": "6. உறுப்பு 30: மத & மொழி சிறுபான்மையினர் கல்வி நிறுவனங்களை நிறுவும் உரிமை",
      "type": "standard_topic"
    },
    {
      "id": "sec_article_31_property",
      "title_en": "7. Article 31 & Right to Property Evolution (Transfer to Article 300A)",
      "title_ta": "7. உறுப்பு 31 & சொத்துரிமை வளர்ச்சி (உறுப்பு 300A-க்கு மாற்றம்)",
      "type": "standard_topic"
    },
    {
      "id": "sec_article_32",
      "title_en": "8. Article 32: Right to Constitutional Remedies (Heart & Soul of Constitution)",
      "title_ta": "8. உறுப்பு 32: அரசியலமைப்புத் தீர்வு காணும் உரிமை (அரசியலமைப்பின் இதயம் & ஆன்மா)",
      "type": "standard_topic"
    },
    {
      "id": "sec_five_writs",
      "title_en": "9. Five Prerogative Writs (Habeas Corpus, Mandamus, Prohibition, Certiorari, Quo Warranto)",
      "title_ta": "9. ஐந்து நீதிப் பேராணைகள் (ஆட்கொணர்வு, செயலுறுத்தும், தடைசெய், நெறிமுறையுறுத்தும், தகுதி வினா)",
      "type": "standard_topic"
    },
    {
      "id": "sec_articles_33_35",
      "title_en": "10. Articles 33–35: Armed Forces Restriction, Martial Law & Parliamentary Enforcement",
      "title_ta": "10. உறுப்புகள் 33–35: ஆயுதப் படைகள் கட்டுப்பாடு, ராணுவ சட்டம் & நாடாளுமன்ற அமலாக்கம்",
      "type": "standard_topic"
    },
    {
      "id": "sec_article_300a",
      "title_en": "11. Article 300A: Right to Property as a Constitutional/Legal Right",
      "title_ta": "11. உறுப்பு 300A: சாதாரண அரசியலமைப்பு/சட்டப்பூர்வ உரிமையாக சொத்துரிமை",
      "type": "standard_topic"
    },
    {
      "id": "sec_inter_relationships",
      "title_en": "12. Inter-Relationships: FR vs DPSP, Fundamental Duties & Preamble",
      "title_ta": "12. இடை-தொடர்புகள்: அடிப்படை உரிமைகள் vs DPSP, அடிப்படை கடமைகள் & முகவுரை",
      "type": "standard_topic"
    },
    {
      "id": "sec_case_laws_part3",
      "title_en": "13. Landmark Judicial Case Laws (Part 3 Focus)",
      "title_ta": "13. முக்கிய மைல்கல் வழக்கு தீர்ப்புகள் (பகுதி 3)",
      "type": "standard_topic"
    },
    {
      "id": "sec_traps_connections_part3",
      "title_en": "14. TNPSC Traps (Bilingual), Cross-Topic Connections & High-Yield Revision",
      "title_ta": "14. டிஎன்பிஎஸ்சி பொறிகள் (இருமொழி), பாடத் தொடர்புகள் & முக்கிய திருப்புதல்",
      "type": "standard_topic"
    }
  ],
  "content": {
    "definition": {
      "en": "Fundamental Rights – Part 3 covers the 'Right to Freedom of Religion' (Articles 25–28), 'Cultural and Educational Rights' (Articles 29–30), the historical transition of the 'Right to Property' from Article 31 to Article 300A, the paramount 'Right to Constitutional Remedies' and Five Writs under Article 32, specialized provisions for Armed Forces and Martial Law (Articles 33–35), and the comprehensive synthesis connecting Fundamental Rights with DPSPs, Fundamental Duties, and Preamble philosophy.",
      "ta": "அடிப்படை உரிமைகள் – பகுதி 3 என்பது 'மத சுதந்திர உரிமை' (உறுப்புகள் 25–28), 'பண்பாடு மற்றும் கல்வி உரிமைகள்' (உறுப்புகள் 29–30), 'சொத்துரிமை' உறுப்பு 31 லிருந்து உறுப்பு 300A-க்கு மாறிய வரலாறு, உறுப்பு 32-ன் கீழ் 'அரசியலமைப்புத் தீர்வு காணும் உரிமை' மற்றும் ஐந்து நீதிப் பேராணைகள், ஆயுதப் படைகள் மற்றும் ராணுவ சட்டத்திற்கான சிறப்பு விதிகள் (உறுப்புகள் 33–35), மற்றும் அடிப்படை உரிமைகளை DPSP, அடிப்படை கடமைகள் மற்றும் முகவுரையுடன் இணைக்கும் விரிவான தத்துவத் தொகுப்பை உள்ளடக்கியது."
    },
    "introduction": {
      "en": "Part 3 completes the study of Part III of the Constitution. It analyzes individual and collective religious freedom, non-taxation of religion, restrictions on religious instruction in state institutions, minority language and educational institution guarantees, the evolution of property rights, Article 32 writ jurisdiction (Dr. Ambedkar's 'heart and soul'), the 5 prerogative writs, Parliament's power under Articles 33-35, Article 300A legal status, and the harmonious balance between Fundamental Rights, DPSPs, and Fundamental Duties.",
      "ta": "பகுதி 3 அரசியலமைப்பின் பகுதி III பற்றிய ஆய்வை நிறைவு செய்கிறது. இது தனிநபர் மற்றும் கூட்டு மத சுதந்திரம், மத வரிவிலக்கு, அரசு நிறுவனங்களில் மதக் கல்வி போதனை வரம்புகள், சிறுபான்மையினரின் மொழி மற்றும் கல்வி நிறுவன உத்தரவாதங்கள், சொத்துரிமையின் வளர்ச்சி, உறுப்பு 32 மனு அதிகாரம் (அம்பேத்கரின் 'இதயமும் ஆன்மாவும்'), 5 நீதிப் பேராணைகள், உறுப்புகள் 33-35-ன் கீழ் நாடாளுமன்ற அதிகாரம், உறுப்பு 300A சட்ட அந்தஸ்து மற்றும் அடிப்படை உரிமைகள், DPSP, அடிப்படை கடமைகள் இடையேயான நல்லிணக்கத்தை பகுப்பாய்வு செய்கிறது."
    },
    "sec_article_25": [
      {
        "title": "1. Individual Freedom of Religion & 4 Aspects (மத சுதந்திரத்தின் 4 அம்சங்கள்)",
        "points": {
          "en": [
            "Article 25(1) Core Rule: All persons (citizens and foreigners) are equally entitled to freedom of conscience and the right freely to profess, practise, and propagate religion.",
            "Four Key Terms Distinguished:\n1. Freedom of Conscience: Absolute inner freedom of an individual to mold his relation with God or Creatures in whatever way he desires.\n2. Right to Profess: Right to declare openly and freely one's religious beliefs and faith.\n3. Right to Practise: Right to perform religious worship, duties, rituals, ceremonies, and exhibition of beliefs.\n4. Right to Propagate: Right to transmit or spread one's religious tenets to others. CRITICAL TRAP: It does NOT include the right to forcibly convert another person to one's own religion (forced conversion violates freedom of conscience of converted person - Stainislaus Case 1977).",
            "Constitutional Limitations under Art 25(1): Freedom of religion is subject to: 1. Public Order, 2. Morality, 3. Health, and 4. Other provisions of Part III.",
            "State Regulation under Art 25(2):\n- State can regulate economic, financial, political, or secular activities associated with religious practice.\n- State can provide for social welfare and reform, including opening of Hindu religious institutions of a public character to all classes and sections of Hindus.",
            "Explanations to Article 25:\n- Explanation I: Wearing and carrying of Kirpans is included in the profession of Sikh religion.\n- Explanation II: Reference to 'Hindus' includes persons professing Sikh, Jain, or Buddhist religion."
          ],
          "ta": [
            "உறுப்பு 25(1) முதன்மை விதி: அனைத்து நபர்களும் (குடிமக்கள் & வெளிநாட்டினர்) மனச்சாட்சி சுதந்திரம் மற்றும் மதத்தைப் பரப்பவும், பின்பற்றவும், வெளிப்படையாகக் கூறவும் சமமான உரிமை உடையவர்கள்.",
            "நான்கு முக்கிய சொற்களின் வேறுபாடு:\n1. மனச்சாட்சி சுதந்திரம் (Conscience): ஒரு தனிநபர் கடவுளுடனான தனது தொடர்பைத் தான் விரும்பும் வழியில் வடிவமைத்துக் கொள்ளும் உள் சுதந்திரம்.\n2. வெளிப்படையாகக் கூறும் உரிமை (Profess): தனது மத நம்பிக்கைகளை வெளிப்படையாக அறிவிக்கும் உரிமை.\n3. பின்பற்றும் உரிமை (Practise): மத வழிபாடு, சடங்குகள், வழிபாட்டு முறைகளைச் செய்யும் உரிமை.\n4. பரப்பும் உரிமை (Propagate): தனது மதக் கோட்பாடுகளைப் பிறருக்குப் பரப்பும் உரிமை. முக்கிய பொறி: இது ஒருவரைத் தனது மதத்திற்குப் பலவந்தமாக மதமாற்றம் செய்யும் உரிமையை உள்ளடக்காது (ஸ்டேனிஸ்லாஸ் வழக்கு 1977).\n\nஅரசியலமைப்பு வரம்புகள் (உறுப்பு 25(1)):\n1. பொது ஒழுங்கு, 2. ஒழுக்கம், 3. சுகாதாரம், 4. பகுதி III-ன் பிற விதிகளுக்கு உட்பட்டது.\n\nஅரசு ஒழுங்குமுறை (உறுப்பு 25(2)):\n- மத நடைமுறையுடன் தொடர்புடைய பொருளாதார, நிதி, அரசியல் அல்லது மதச்சார்பற்ற நடவடிக்கைகளை அரசு ஒழுங்குபடுத்தலாம்.\n- சமூக நலன் மற்றும் சீர்திருத்தங்களுக்காக இந்து சமய நிறுவனங்களைப் அனைத்துப் பிரிவு இந்துக்களுக்கும் திறந்து விடலாம்.\n\nஉறுப்பு 25-ன் விளக்கங்கள்:\n- விளக்கம் I: கிர்பான் (வாள்) அணிவதும் வைப்பதும் சீக்கிய மதப் பின்பற்றுதலில் அடங்கும்.\n- விளக்கம் II: 'இந்துக்கள்' என்ற குறிப்பில் சீக்கியர், ஜைனர், பௌத்த மதத்தைப் பின்பற்றுவோரும் அடங்குவர்."
          ]
        }
      }
    ],
    "sec_article_26": [
      {
        "title": "1. Collective Religious Denominational Rights (சமயக் குழுக்களின் கூட்டு உரிமைகள்)",
        "points": {
          "en": [
            "Article 26 Core Scope: Guarantees freedom to manage religious affairs to every RELIGIOUS DENOMINATION or any section thereof (Collective religious right).",
            "Four Specific Rights of Religious Denominations:\n1. Art 26(a): Establish and maintain institutions for religious and charitable purposes.\n2. Art 26(b): Manage its own affairs in matters of religion.\n3. Art 26(c): Own and acquire movable and immovable property.\n4. Art 26(d): Administer such property in accordance with law.",
            "Definition of Religious Denomination (Supreme Court Test):\n- Collection of individuals with a system of beliefs (doctrines) conductive to spiritual well-being.\n- Common organization.\n- Designated by a distinctive name.\n- Example: Ramakrishna Mission and Ananda Marga are religious denominations (*Aurobindo Society* is NOT a religious denomination).",
            "Limitation Grounds: Subject to Public Order, Morality, and Health (NOTE: Art 26 is NOT subject to 'other provisions of Part III', unlike Art 25).",
            "TNPSC Trap Comparison:\n- Article 25 protects INDIVIDUAL religious rights.\n- Article 26 protects COLLECTIVE rights of religious denominations."
          ],
          "ta": [
            "உறுப்பு 26 முதன்மை எல்லை: ஒவ்வொரு சமயக் குழுவிற்கும் (Religious Denomination) அல்லது அதன் பிரிவிற்கும் தனது மத விவகாரங்களை நிர்வகிக்கும் சுதந்திரத்தை உத்தரவாதம் செய்கிறது (கூட்டு மத உரிமை).",
            "சமயக் குழுக்களின் 4 குறிப்பிட்ட உரிமைகள்:\n1. 26(a): சமய மற்றும் தொண்டு நிறுவனங்களை நிறுவுதல் மற்றும் பராமரித்தல்.\n2. 26(b): மத விவகாரங்களில் தனது சொந்த விஷயங்களை நிர்வகித்தல்.\n3. 26(c): அசையும் மற்றும் அசையாச் சொத்துக்களைச் சொந்தமாக வைப்பது மற்றும் வாங்குவது.\n4. 26(d): அத்தகைய சொத்துக்களைச் சட்டத்தின்படி நிர்வகிப்பது.\n\nசமயக் குழுவின் வரையறை (உச்ச நீதிமன்ற சோதனை):\n- ஆன்மீக நல்வாழ்விற்கான தத்துவ அமைப்பைக் கொண்ட தனிநபர்களின் கூட்டம்.\n- பொதுவான அமைப்பு.\n- தனித்துவமான பெயரால் குறிப்பிடப்படுவது.\n- உதாரணம்: ராமகிருஷ்ணா மிஷன் மற்றும் ஆனந்த மார்க்கா சமயக் குழுக்கள் ஆகும் (அரவிந்தோ சொசைட்டி சமயக் குழு அல்ல).\n\nகட்டுப்பாட்டு அடிப்படைகள்: பொது ஒழுங்கு, ஒழுக்கம் மற்றும் சுகாதாரத்திற்கு உட்பட்டது.\n\nடிஎன்பிஎஸ்சி பொறி ஒப்பீடு:\n- உறுப்பு 25 TANI NABAR (தனிநபர்) மத உரிமைகளைப் பாதுகாக்கிறது.\n- உறுப்பு 26 KOOTTU (கூட்டு) சமயக் குழு உரிமைகளைப் பாதுகாக்கிறது."
          ]
        }
      }
    ],
    "sec_article_27": [
      {
        "title": "1. Freedom from Taxation for Religion (மத வரி செலுத்தலிலிருந்து சுதந்திரம்)",
        "points": {
          "en": [
            "Article 27 Core Principle: No person shall be compelled to pay any TAXES, the proceeds of which are specifically appropriated in payment of expenses for the promotion or maintenance of any particular religion or religious denomination.",
            "Prohibits Tax Favoritism: State cannot favor, patronize, or support one religion over another using public tax money. Maintains strict State secularism.",
            "State Spending Allowed if Neutral: Public money can be spent on promoting/maintaining ALL religions equally.",
            "CRITICAL TNPSC DISTINCTION — Tax vs Fee:\n- Article 27 prohibits levying a TAX for religion.\n- Article 27 DOES NOT PROHIBIT LEVYING A FEE!\n- A FEE can be levied on religious pilgrims/institutions to provide special services, regulation, safety, or secular administration (e.g. pilgrim fee at major temples).",
            "TNPSC Trap: Taxes are prohibited for religious promotion, but FEES are constitutionally permitted."
          ],
          "ta": [
            "உறுப்பு 27 முதன்மைக் கோட்பாடு: ஒரு குறிப்பிட்ட மதத்தை அல்லது சமயக் குழுவை ஊக்குவிப்பதற்கு அல்லது பராமரிப்பதற்கு வரிப் பணத்தைப் பயன்படுத்த எந்தவொரு நபரும் எந்தவொரு வரியையும் செலுத்துமாறு வற்புறுத்தப்படக்கூடாது.",
            "வரிச் சலுகையைத் தடுக்கிறது: பொது வரிப் பணத்தைப் பயன்படுத்தி ஒரு மதத்தை மற்றொரு மதத்தை விட ஆதரிக்கவோ ஆதாயம் அளிக்கவோ அரசு முடியாது.",
            "சமமான அரசு செலவு அனுமதிக்கப்படும்: அனைத்து மதங்களையும் சமமாக ஊக்குவிக்கப் பொதுப் பணத்தைச் செலவிடலாம்.",
            "முக்கிய டிஎன்பிஎஸ்சி வேறுபாடு — வரி vs கட்டணம்:\n- உறுப்பு 27 மதத்திற்காக வரி (TAX) விதிப்பதைத் தடுக்கிறது.\n- உறுப்பு 27 கட்டணம் (FEE) விதிப்பதைத் தடுக்கவில்லை!\n- சிறப்புச் சேவைகள், ஒழுங்குமுறை, பாதுகாப்பு அல்லது நிர்வாகத்தை வழங்குவதற்காக மதப் யாத்திரீகர்கள்/நிறுவனங்கள் மீது கட்டணம் விதிக்கப்படலாம்.",
            "டிஎன்பிஎஸ்சி பொறி: மதப் பிரச்சாரத்திற்காக வரிகள் தடை செய்யப்பட்டுள்ளன, ஆனால் கட்டணங்கள் அரசியலமைப்பு ரீதியாக அனுமதிக்கப்படுகின்றன."
          ]
        }
      }
    ],
    "sec_article_28": [
      {
        "title": "1. Religious Instruction in Educational Institutions (கல்வி நிறுவனங்களில் மதக் கல்வி)",
        "points": {
          "en": [
            "Article 28 Scope: Regulates religious instruction and religious worship in educational institutions.",
            "Four Categories of Educational Institutions:\n\n1. Category A – Wholly Maintained out of State Funds:\n   - Religious instruction is COMPLETELY PROHIBITED.\n\n2. Category B – Administered by State but Established under Trust/Endowment:\n   - Religious instruction IS PERMITTED (e.g. Sanskrit/Vedic institutions established under trust).\n\n3. Category C – Recognized by the State:\n   - Religious instruction is PERMITTED on a VOLUNTARY BASIS (No person compelled; minor requires guardian consent).\n\n4. Category D – Receiving Aid from State Funds:\n   - Religious instruction is PERMITTED on a VOLUNTARY BASIS (Consent required)."
          ],
          "ta": [
            "உறுப்பு 28 எல்லை: கல்வி நிறுவனங்களில் மதக் கல்வி போதனை மற்றும் மத வழிபாட்டை ஒழுங்குபடுத்துகிறது.",
            "கல்வி நிறுவனங்களின் 4 பிரிவுகள்:\n\n1. பிரிவு A – முழுமையாக அரசு நிதியால் பராமரிக்கப்படுபவை:\n   - மதக் கல்வி போதனை முற்றிலும் தடை செய்யப்பட்டுள்ளது.\n\n2. பிரிவு B – அரசால் நிர்வகிக்கப்படும் ஆனால் அறக்கட்டளையின் கீழ் நிறுவப்பட்டவை:\n   - மதக் கல்வி போதனை அனுமதிக்கப்படுகிறது (எ.கா. அறக்கட்டளையின் கீழ் நிறுவப்பட்ட வேத நிறுவனங்கள்).\n\n3. பிரிவு C – அரசால் அங்கீகரிக்கப்பட்டவை:\n   - மதக் கல்வி போதனை விருப்பத்தின் அடிப்படையில் அனுமதிக்கப்படுகிறது (கட்டாயம் இல்லை; சிறாருக்குக் காப்பாளர் ஒப்புதல் தேவை).\n\n4. பிரிவு D – அரசிடமிருந்து நிதியுதவி பெறுபவை:\n   - மதக் கல்வி போதனை விருப்பத்தின் அடிப்படையில் அனுமதிக்கப்படுகிறது (ஒப்புதல் தேவை)."
          ]
        }
      }
    ],
    "sec_article_29": [
      {
        "title": "1. Cultural & Linguistic Rights (பண்பாட்டு மற்றும் மொழி உரிமைகள்)",
        "points": {
          "en": [
            "Article 29(1) Protection of Language, Script & Culture:\n  - Any SECTION OF CITIZENS residing in India having a distinct language, script, or culture of its own has the right to conserve the same.\n  - CRITICAL TNPSC TRAP: Article 29(1) applies to ANY SECTION OF CITIZENS (including majority), NOT exclusively to minorities! (Upheld in *Supreme Court 1992*).",
            "Article 29(2) Non-Discrimination in Educational Admission:\n  - No CITIZEN shall be denied admission into any educational institution maintained by the State or receiving aid out of State funds on grounds ONLY of RELIGION, RACE, CASTE, LANGUAGE (4 Grounds!).",
            "Difference between Art 15(1) & Art 29(2) Grounds:\n  - Art 15(1) Grounds: Religion, Race, Caste, Sex, Place of Birth (5 Grounds).\n  - Art 29(2) Grounds: Religion, Race, Caste, LANGUAGE (4 Grounds - 'Sex' & 'Place of Birth' omitted; 'Language' added!)."
          ],
          "ta": [
            "உறுப்பு 29(1) மொழி, எழுத்து & பண்பாட்டுப் பாதுகாப்பு:\n  - இந்தியாவில் வசிக்கும் குடிமக்களின் எந்தவொரு பிரிவினரும் (Section of Citizens) தனது சொந்த மொழி, எழுத்து அல்லது பண்பாட்டைப் பாதுகாக்கும் உரிமை உண்டு.\n  - முக்கிய டிஎன்பிஎஸ்சி பொறி: உறுப்பு 29(1) குடிமக்களின் எந்தவொரு பிரிவிற்கும் பொருந்தும் (பெரும்பான்மையினர் உட்பட), சிறுபான்மையினருக்கு மட்டுமே அல்ல!",
            "உறுப்பு 29(2) கல்விச் சேர்க்கையில் பாகுபாடின்மை:\n  - அரசால் பராமரிக்கப்படும் அல்லது அரசு நிதியுதவி பெறும் எந்தவொரு கல்வி நிறுவனத்திலும் மதம், இனம், சாதி, மொழி ஆகிய 4 அடிப்படைகளில் மட்டுமே எந்தவொரு குடிமகனுக்கும் சேர்க்கை மறுக்கப்படக்கூடாது.",
            "உறுப்பு 15(1) vs உறுப்பு 29(2) அடிப்படைகள் ஒப்பீடு:\n  - உறுப்பு 15(1) அடிப்படைகள்: மதம், இனம், சாதி, பாலினம், பிறந்த இடம் (5 அடிப்படைகள்).\n  - உறுப்பு 29(2) அடிப்படைகள்: மதம், இனம், சாதி, மொழி (4 அடிப்படைகள் - பாலினம், பிறந்த இடம் நீக்கம்; மொழி சேர்க்கை!)."
          ]
        }
      }
    ],
    "sec_article_30": [
      {
        "title": "1. Minority Educational Institutions (சிறுபான்மையினர் கல்வி நிறுவனங்கள்)",
        "points": {
          "en": [
            "Article 30 Core Scope: Right of MINORITIES to establish and administer educational institutions.",
            "Two Types of Minorities Recognized: Article 30 recognizes ONLY RELIGIOUS and LINGUISTIC minorities. (NOTE: The word 'Minority' is NOT defined anywhere in the Constitution!).",
            "Provisions of Article 30:\n- Art 30(1): All religious and linguistic minorities have the right to establish and administer educational institutions of their choice.\n- Art 30(1A): Added by 44th CAA 1978 — In compulsory acquisition of property of minority educational institutions, State must fix compensation that does not restrict their right.\n- Art 30(2): State shall not discriminate in granting aid to educational institutions on the ground that it is under minority management.",
            "T.M.A. Pai Foundation Case 2002: Supreme Court held that minority status (religious or linguistic) must be determined STATE-WISE, taking the state population as a unit.",
            "TNPSC Trap Comparison:\n- Article 29 applies to ANY section of citizens (Majority + Minority).\n- Article 30 applies EXCLUSIVELY to Religious and Linguistic Minorities."
          ],
          "ta": [
            "உறுப்பு 30 முதன்மை எல்லை: சிறுபான்மையினர் கல்வி நிறுவனங்களை நிறுவுவதற்கும் நிர்வகிப்பதற்கும் உள்ள உரிமை.",
            "அங்கீகரிக்கப்பட்ட 2 வகை சிறுபான்மையினர்: உறுப்பு 30 மத மற்றும் மொழி சிறுபான்மையினரை மட்டுமே அங்கீகரிக்கிறது. (குறிப்பு: 'சிறுபான்மையினர்' என்ற சொல் அரசியலமைப்பில் எங்கும் வரையறுக்கப்படவில்லை!).",
            "உறுப்பு 30-ன் விதிகள்:\n- 30(1): அனைத்து மத மற்றும் மொழி சிறுபான்மையினருக்கும் தங்களுக்கு விருப்பமான கல்வி நிறுவனங்களை நிறுவவும் நிர்வகிக்கவும் உரிமை உண்டு.\n- 30(1A): 1978-ன் 44வது திருத்தத்தால் சேர்க்கப்பட்டது — சிறுபான்மை கல்வி நிறுவனங்களின் சொத்தை கட்டாயமாகக் கையகப்படுத்தும்போது, அவர்களின் உரிமையைக் கட்டுப்படுத்தாத இழப்பீட்டை அரசு நிர்ணயிக்க வேண்டும்.\n- 30(2): கல்வி நிறுவனங்களுக்கு நிதியுதவி அளிப்பதில் சிறுபான்மை நிர்வாகத்தின் கீழ் உள்ளது என்ற அடிப்படையில் அரசு பாகுபாடு காட்டக்கூடாது.",
            "T.M.A. பாய் அறக்கட்டளை வழக்கு 2002: சிறுபான்மை அந்தஸ்து (மதம் அல்லது மொழி) மாநில மக்கள் தொகையை ஒரு அலகாகக் கொண்டு மாநில வாரியாகத் தீர்மானிக்கப்பட வேண்டும் என உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
            "டிஎன்பிஎஸ்சி பொறி ஒப்பீடு:\n- உறுப்பு 29 குடிமக்களின் எந்தவொரு பிரிவிற்கும் பொருந்தும் (பெரும்பான்மையினர் + சிறுபான்மையினர்).\n- உறுப்பு 30 மத மற்றும் மொழி சிறுபான்மையினருக்கு மட்டுமே பொருந்தும்."
          ]
        }
      }
    ],
    "sec_article_31_property": [
      {
        "title": "1. Article 31 & Right to Property Transfer (சொத்துரிமை வரலாற்று மாற்றம்)",
        "points": {
          "en": [
            "Original Constitutional Position: Originally, the Right to Property was a Fundamental Right guaranteed under Article 19(1)(f) and Article 31.",
            "Historical Conflict: Led to continuous friction between Legislature and Judiciary over agrarian reforms and compulsory acquisition compensation.",
            "44th Constitutional Amendment Act, 1978: Omitted Article 19(1)(f) and Article 31 from Part III of the Constitution.",
            "Present Article 300A in Part XII: Inserted a new Article 300A under Part XII (Title: 'No person shall be deprived of his property save by authority of law').",
            "Present Legal Status: Right to Property is now a CONSTITUTIONAL / LEGAL RIGHT, NOT a Fundamental Right.",
            "Implications of Being a Legal Right:\n1. It can be regulated or curtailed by ordinary law without constitutional amendment.\n2. In case of violation, aggrieved person CANNOT go directly to Supreme Court under Article 32 (must go to High Court under Article 226 or file ordinary suit).\n3. State is not constitutionally bound to pay compensation for acquiring private property (except under Art 30(1A) minority institutions & Art 31A personal cultivation land)."
          ],
          "ta": [
            "அசல் அரசியலமைப்பு நிலை: ஆரம்பத்தில், சொத்துரிமை உறுப்பு 19(1)(f) மற்றும் உறுப்பு 31-ன் கீழ் உத்தரவாதம் அளிக்கப்பட்ட ஒரு அடிப்படை உரிமையாகும்.",
            "வரலாற்று மோதல்: நிலச்சீர்திருத்தங்கள் மற்றும் சொத்து கையகப்படுத்தும் இழப்பீடு குறித்து சட்டமன்றத்திற்கும் நீதித்துறைக்கும் இடையே தொடர்ச்சியான உராய்வுக்கு வழிவகுத்தது.",
            "1978-ன் 44வது அரசியலமைப்பு திருத்தச் சட்டம்: பகுதி III லிருந்து உறுப்பு 19(1)(f) மற்றும் உறுப்பு 31-ஐ நீக்கியது.",
            "பகுதி XII-ல் தற்போதைய உறுப்பு 300A: பகுதி XII-ல் புதிய உறுப்பு 300A-ஐச் சேர்த்தது ('சட்டத்தின் அதிகாரத்தினால் அன்றி வேறு எவ்வழியிலும் எந்தவொரு நபரின் சொத்தும் பறிக்கப்படக்கூடாது').",
            "தற்போதைய சட்ட நிலை: சொத்துரிமை இப்போது ஒரு அரசியலமைப்பு / சட்டப்பூர்வ உரிமை மட்டுமே, அடிப்படை உரிமை அல்ல.",
            "சட்டப்பூர்வ உரிமையாக இருப்பதன் விளைவுகள்:\n1. அரசியலமைப்பு திருத்தமின்றி சாதாரண சட்டத்தால் இதை ஒழுங்குபடுத்தலாம் அல்லது குறைக்கலாம்.\n2. மீறப்பட்டால், பாதிக்கப்பட்டவர் உறுப்பு 32-ன் கீழ் நேரடியாக உச்ச நீதிமன்றத்திற்குச் செல்ல முடியாது (உயர் நீதிமன்ற உறுப்பு 226 அல்லது சாதாரண வழக்கு தொடர வேண்டும்).\n3. தனியார் சொத்தைக் கையகப்படுத்த இழப்பீடு வழங்க அரசுக்கு அரசியலமைப்பு ரீதியாகக் கட்டாயமில்லை."
          ]
        }
      }
    ],
    "sec_article_32": [
      {
        "title": "1. Article 32: Right to Constitutional Remedies (அரசியலமைப்புத் தீர்வு காணும் உரிமை)",
        "points": {
          "en": [
            "Article 32 Significance: Provides the right to move the Supreme Court by appropriate proceedings for the ENFORCEMENT of Fundamental Rights.",
            "Dr. B.R. Ambedkar's Famous Description: Described Article 32 as the 'VERY SOUL OF THE CONSTITUTION AND THE VERY HEART OF IT'. He stated: 'An Article without which this Constitution would be a nullity.'",
            "Fundamental Right Itself: Right to move Supreme Court under Art 32 is ITSELF a Fundamental Right. Therefore, SC cannot refuse to entertain an Art 32 petition for FR violation.",
            "Basic Structure: Judicial Review under Article 32 is part of the Basic Structure of the Constitution (*Minerva Mills Case 1980*).",
            "Article 32 vs Article 226 Scope:\n- Article 32 (Supreme Court): Enforces ONLY Fundamental Rights. Mandatory remedy. Narrower subject scope.\n- Article 226 (High Court): Enforces Fundamental Rights AND ordinary legal rights ('for any other purpose'). Discretionary remedy. Wider subject scope."
          ],
          "ta": [
            "உறுப்பு 32 முக்கியத்துவம்: அடிப்படை உரிமைகளை அமல்படுத்துவதற்காகப் பொருத்தமான நடவடிக்கைகள் மூலம் உச்ச நீதிமன்றத்தை அணுகும் உரிமையை வழங்குகிறது.",
            "டாக்டர் பி.ஆர். அம்பேத்கரின் புகழ்பெற்ற விளக்கம்: உறுப்பு 32-ஐ 'அரசியலமைப்பின் இதயம் மற்றும் ஆன்மா' என விவரித்தார். 'இந்த உறுப்பு இல்லாவிட்டால் அரசியலமைப்பு பயனற்றதாகிவிடும்' எனக் கூறினார்.",
            "சுயமாகவே அடிப்படை உரிமை: உறுப்பு 32-ன் கீழ் உச்ச நீதிமன்றத்தை அணுகும் உரிமை சுயமாகவே ஒரு அடிப்படை உரிமையாகும். எனவே, அடிப்படை உரிமை மீறல் மனுவை விசாரிக்க உச்ச நீதிமன்றம் மறுக்க முடியாது.",
            "அடிப்படை கட்டமைப்பு: உறுப்பு 32-ன் கீழ் நீதித்துறை ஆய்வு அரசியலமைப்பின் அடிப்படை கட்டமைப்பின் பகுதியாகும் (மினர்வா மில்ஸ் வழக்கு 1980).",
            "உறுப்பு 32 vs உறுப்பு 226 எல்லை:\n- உறுப்பு 32 (உச்ச நீதிமன்றம்): அடிப்படை உரிமைகளை மட்டுமே அமல்படுத்துகிறது. கட்டாய தீர்வு.\n- உறுப்பு 226 (உயர் நீதிமன்றம்): அடிப்படை உரிமைகள் மற்றும் சாதாரண சட்டப்பூர்வ உரிமைகளை ('வேறு எந்த நோக்கத்திற்காகவும்') அமல்படுத்துகிறது. விரிவான எல்லை."
          ]
        }
      }
    ],
    "sec_five_writs": [
      {
        "title": "1. Five Prerogative Writs Detailed Breakdown (ஐந்து நீதிப் பேராணைகள்)",
        "points": {
          "en": [
            "Writs Origin: Derived from English Law ('Prerogative Writs'). Supreme Court (Art 32) and High Courts (Art 226) can issue 5 types of writs:\n\n1. Habeas Corpus (ஆட்கொணர்வு பேராணை):\n   - Literal Meaning: 'To have the body of'.\n   - Purpose: Order issued to a person/authority who has detained another person, to produce the detainee before court to examine legality of detention.\n   - Issued Against: BOTH Public Authorities and Private Individuals.\n   - Key Identification: Safeguard against arbitrary illegal detention.\n\n2. Mandamus (செயலுறுத்தும் பேராணை):\n   - Literal Meaning: 'We Command'.\n   - Purpose: Command issued to a public official/body to perform a mandatory statutory public duty.\n   - Issued Against: Public bodies, officers, lower courts, tribunals, government.\n   - CANNOT BE ISSUED AGAINST: Private individuals, President, State Governors, or to enforce contractual obligations.\n\n3. Prohibition (தடைசெய் பேராணை):\n   - Literal Meaning: 'To Forbid'.\n   - Purpose: Issued by a higher court to a lower court or tribunal to prevent it from exceeding its jurisdiction or usurping power.\n   - Nature: PREVENTATIVE ONLY ('Prevention is better than cure').\n   - Issued Against: ONLY Judicial and Quasi-judicial authorities (NOT administrative bodies or private bodies).\n\n4. Certiorari (நெறிமுறையுறுத்தும் பேராணை):\n   - Literal Meaning: 'To be certified' or 'To be more fully informed'.\n   - Purpose: Issued by a higher court to a lower court, tribunal, or administrative authority to QUASH an illegal order passed in excess of jurisdiction.\n   - Nature: BOTH PREVENTATIVE AND CURATIVE.\n   - Issued Against: Judicial, Quasi-judicial, AND Administrative authorities (*A.K. Kraipak Case*).\n\n5. Quo Warranto (தகுதி வினா பேராணை):\n   - Literal Meaning: 'By what authority or warrant?'.\n   - Purpose: Issued to inquire into the legality of claim of a person to a public office, preventing illegal usurpation of public office.\n   - Essential Condition: Public office must be substantive, created by statute/constitution.\n   - CRITICAL TRAP: Locus Standi is RELAXED! Can be sought by ANY INTERESTED PERSON (does not need to be the aggrieved party)."
          ],
          "ta": [
            "பேராணைகளின் மூலம்: ஆங்கிலச் சட்டத்திலிருந்து பெறப்பட்டது ('Prerogative Writs'). உச்ச நீதிமன்றம் (உறுப்பு 32) மற்றும் உயர் நீதிமன்றங்கள் (உறுப்பு 226) 5 வகையான பேராணைகளை பிறப்பிக்கலாம்:\n\n1. ஆட்கொணர்வு பேராணை (Habeas Corpus):\n   - நேரடிப் பொருள்: 'உடலைக் கொண்டு வா'.\n   - நோக்கம்: ஒருவரைக் காவலில் வைத்துள்ள அதிகாரியிடம் காவலில் வைக்கப்பட்ட நபரை நீதிமன்றத்தில் ஆஜர்படுத்தி தடுப்புக் காவலின் சட்டப்பூர்வ தன்மையை சோதிக்கும் உத்தரவு.\n   - யாருக்கு எதிராக: அரசு அமைப்புகள் மற்றும் தனியார் நபர்கள் இருவருக்கும் எதிராக.\n\n2. செயலுறுத்தும் பேராணை (Mandamus):\n   - நேரடிப் பொருள்: 'நாங்கள் கட்டளையிடுகிறோம்'.\n   - நோக்கம்: ஒரு அரசு அதிகாரி/அமைப்பு தனது கட்டாயச் சட்டப்பூர்வப் பணியைச் செய்ய பிறப்பிக்கப்படும் கட்டளை.\n   - யாருக்கு எதிராக: அரசு அமைப்புகள், அதிகாரிகள், கீழ் நீதிமன்றங்கள்.\n   - வழங்க முடியாதவை: தனியார் நபர்கள், குடியரசுத் தலைவர், ஆளுநர்களுக்கு எதிராக வழங்க முடியாது.\n\n3. தடைசெய் பேராணை (Prohibition):\n   - நேரடிப் பொருள்: 'தடுப்பது / தட்டறுப்பது'.\n   - நோக்கம்: ஒரு கீழ் நீதிமன்றம்/தீர்ப்பாயம் தனது அதிகார வரம்பை மீறுவதைத் தடுக்க உயர் நீதிமன்றம் பிறப்பிக்கும் உத்தரவு.\n   - இயல்பு: தடுப்பு நடவடிக்கை மட்டுமே ('வருமுன் காப்பதே மேல்').\n   - யாருக்கு எதிராக: நீதித்துறை மற்றும் நீதித்துறை சார்ந்த அதிகாரிகளுக்கு மட்டுமே.\n\n4. நெறிமுறையுறுத்தும் பேராணை (Certiorari):\n   - நேரடிப் பொருள்: 'சான்றளிப்பது / முழுமையாக அறிவது'.\n   - நோக்கம்: கீழ் நீதிமன்றம் அல்லது நிர்வாக அமைப்பு பிறப்பித்த சட்டவிரோத உத்தரவை ரத்து செய்ய உயர் நீதிமன்றம் பிறப்பிக்கும் உத்தரவு.\n   - இயல்பு: தடுப்பு மற்றும் குணப்படுத்தும் நடவடிக்கை இரண்டும்.\n   - யாருக்கு எதிராக: நீதித்துறை, பகுதி-நீதித்துறை மற்றும் நிர்வாக அமைப்புகளுக்கு எதிராக.\n\n5. தகுதி வினா பேராணை (Quo Warranto):\n   - நேரடிப் பொருள்: 'எந்த அதிகாரத்தின் அடிப்படையில்?'.\n   - நோக்கம்: ஒரு பொதுப் பதவியில் இருக்கும் நபரின் தகுதியை வினவி சட்டவிரோதமாகப் பதவியைக் கைப்பற்றுவதைத் தடுக்கும் உத்தரவு.\n   - முக்கிய பொறி: பாதிக்கப்பட்ட நபர் மட்டுமின்றி எந்தவொரு ஆர்வமுள்ள நபராலும் கேட்கப்படலாம்!"
          ]
        }
      }
    ],
    "sec_articles_33_35": [
      {
        "title": "1. Articles 33, 34, 35 Breakdown (உறுப்புகள் 33, 34, 35 விளக்கம்)",
        "points": {
          "en": [
            "Article 33 – Modification of FRs for Armed Forces:\n  - Empowers PARLIAMENT ONLY to restrict or abrogate Fundamental Rights of members of Armed Forces, Para-military forces, Police forces, Intelligence agencies, and Telecommunication personnel.\n  - Purpose: To ensure proper discharge of their duties and maintenance of discipline among them.\n  - Note: Laws made under Art 33 cannot be challenged in any court for FR violation.\n\nArticle 34 – Restrictions During Martial Law:\n  - Provides for restrictions on FRs while MARTIAL LAW (military rule) is in force in any area within India.\n  - Empowers Parliament to indemnify any government servant for acts done during martial law.\n  - Note: 'Martial Law' is NOT defined in the Constitution. It is distinct from National Emergency.\n\nArticle 35 – Exclusive Parliamentary Legislation for FRs:\n  - Lays down that power to make laws to give effect to specified Fundamental Rights rests EXCLUSIVELY WITH PARLIAMENT (NOT State Legislatures).\n  - Applies to: Art 16(3) residence law, Art 32(3) lower court writ power, Art 33, Art 34, and prescribing punishment for offences under Art 17 (untouchability) and Art 23 (forced labour).\n  - Purpose: Ensures uniformity of Fundamental Rights throughout India."
          ],
          "ta": [
            "உறுப்பு 33 – ஆயுதப் படைகளுக்கான அடிப்படை உரிமைகள் கட்டுப்பாடு:\n  - ஆயுதப் படைகள், துணை ராணுவப் படைகள், காவல்துறை, உளவு அமைப்புகள் ஊழியர்களின் அடிப்படை உரிமைகளைக் கட்டுப்படுத்த அல்லது நீக்க நாடாளுமன்றத்திற்கு மட்டுமே அதிகாரமளிக்கிறது.\n  - நோக்கம்: அவர்களின் கடமைகளைச் சரிவரச் செய்வதையும் ஒழுக்கத்தைப் பராமரிப்பதையும் உறுதி செய்தல்.\n\nஉறுப்பு 34 – ராணுவ சட்டத்தின் போது கட்டுப்பாடுகள்:\n  - இந்தியாவின் எந்தப் பகுதியிலும் ராணுவ சட்டம் (Martial Law) அமலில் இருக்கும் போது அடிப்படை உரிமைகளின் மீதான கட்டுப்பாடுகளை வழங்குகிறது.\n  - ராணுவ சட்டத்தின் போது அரசு ஊழியர்கள் செய்த செயல்களுக்கு நாடாளுமன்றம் இழப்பீடு/பாதுகாப்பு வழங்கலாம்.\n  - குறிப்பு: 'ராணுவ சட்டம்' அரசியலமைப்பில் வரையறுக்கப்படவில்லை.\n\nஉறுப்பு 35 – அடிப்படை உரிமைகளுக்கான நாடாளுமன்ற பிரத்யேகச் சட்ட அதிகாரம்:\n  - குறிப்பிட்ட அடிப்படை உரிமைகளுக்குச் செயலுருவம் கொடுக்கும் சட்டங்களை இயற்றும் அதிகாரம் நாடாளுமன்றத்திற்கு மட்டுமே உண்டு (மாநில சட்டமன்றங்களுக்கு இல்லை).\n  - பொருந்தும் பகுதிகள்: உறுப்பு 16(3) வசிப்பிடச் சட்டம், உறுப்பு 33, 34, மற்றும் உறுப்பு 17 (தீண்டாமை), உறுப்பு 23 (கட்டாய வேலை) குற்றங்களுக்கான தண்டனை நிர்ணயித்தல்.\n  - நோக்கம்: இந்தியா முழுவதும் அடிப்படை உரிமைகளின் சீரான தன்மையை உறுதி செய்தல்."
          ]
        }
      }
    ],
    "sec_article_300a": [
      {
        "title": "1. Constitutional Status of Article 300A (உறுப்பு 300A-ன் அரசியலமைப்பு அந்தஸ்து)",
        "points": {
          "en": [
            "Location & Wording: Placed in Part XII under Chapter IV. Text: 'No person shall be deprived of his property save by authority of law.'",
            "Constitutional Nature: It is a Constitutional / Legal Right, NOT a Fundamental Right.",
            "Key Consequences:\n1. Protection against Executive action, NOT Legislative action (Parliament/State Legislature can deprive property by valid law).\n2. Remedy for violation lies under Article 226 in High Court or civil suit, NOT Article 32 in Supreme Court.\n3. Compensation is NOT guaranteed except for minority educational institutions (Art 30(1A)) and land under personal cultivation (Art 31A)."
          ],
          "ta": [
            "இடம் & உரை: பகுதி XII-ல் அத்தியாயம் IV-ன் கீழ் உள்ளது. உரை: 'சட்டத்தின் அதிகாரத்தினால் அன்றி வேறு எவ்வழியிலும் எந்தவொரு நபரின் சொத்தும் பறிக்கப்படக்கூடாது.'",
            "அரசியலமைப்பு இயல்பு: இது ஒரு அரசியலமைப்பு / சட்டப்பூர்வ உரிமை மட்டுமே, அடிப்படை உரிமை அல்ல.",
            "முக்கிய விளைவுகள்:\n1. நிர்வாக நடவடிக்கைக்கு மட்டுமே பாதுகாப்பு, சட்டமன்ற நடவடிக்கைக்கு அல்ல (செல்லுபடியாகும் சட்டத்தின் மூலம் அரசே சொத்தைப் பறிக்கலாம்).\n2. மீறப்பட்டால் தீர்வு உயர் நீதிமன்ற உறுப்பு 226 அல்லது சிவில் வழக்கே தவிர உறுப்பு 32 அல்ல.\n3. சிறுபான்மை கல்வி நிறுவனங்கள் (30(1A)) மற்றும் சொந்த சாகுபடி நிலங்கள் (31A) தவிர மற்ற சொத்துக்களுக்கு இழப்பீடு உத்தரவாதம் இல்லை."
          ]
        }
      }
    ],
    "sec_inter_relationships": [
      {
        "title": "1. FR vs DPSP, Fundamental Duties & Preamble Connections (இடை-தொடர்புகள்)",
        "points": {
          "en": [
            "FR vs DPSP Balance:\n- Fundamental Rights (Part III) guarantee Political Democracy (Justiciable).\n- DPSP (Part IV) guarantee Social and Economic Democracy (Non-justiciable).\n- Minerva Mills Case (1980): SC held that the Constitution is founded on the HARMONIOUS BALANCE between Part III and Part IV; this balance is part of the Basic Structure.\n\nFR vs Fundamental Duties:\n- Rights and Duties are correlative and inseparable. Fundamental Duties (Part IV-A) serve as a reminder to citizens while enjoying Part III rights.\n\nFR and Preamble:\n- Fundamental Rights operationalize the Preamble's solemn resolve to secure JUSTICE (Social, Economic, Political), LIBERTY (Thought, Expression, Belief, Faith, Worship), EQUALITY (Status and Opportunity), and FRATERNITY assuring Dignity of Individual."
          ],
          "ta": [
            "அடிப்படை உரிமைகள் vs DPSP சமநிலை:\n- அடிப்படை உரிமைகள் (பகுதி III) அரசியல் ஜனநாயகத்தை உறுதி செய்கின்றன (நீதிமன்றத்தால் நிலைநிறுத்தக்கூடியவை).\n- DPSP (பகுதி IV) சமூக மற்றும் பொருளாதார ஜனநாயகத்தை உறுதி செய்கின்றன (நிலைநிறுத்த முடியாதவை).\n- மினர்வா மில்ஸ் வழக்கு (1980): பகுதி III மற்றும் பகுதி IV இடையேயான நல்லிணக்கச் சமநிலையின் மீதே அரசியலமைப்பு நிறுவப்பட்டுள்ளது என உச்ச நீதிமன்றம் தீர்ப்பளித்தது.\n\nஅடிப்படை உரிமைகள் vs அடிப்படை கடமைகள்:\n- உரிமைகளும் கடமைகளும் ஒன்றுக்கொன்று தொடர்புடையவை. பகுதி III உரிமைகளை அனுபவிக்கும் போது குடிமக்களுக்கு நினைவூட்டலாக பகுதி IV-A கடமைகள் செயல்படுகின்றன.\n\nஅடிப்படை உரிமைகள் & முகவுரைத் தொடர்பு:\n- அடிப்படை உரிமைகள் முகவுரையின் நீதி, சுதந்திரம், சமத்துவம், சகோதரத்துவம் மற்றும் தனிநபர் கண்ணிய இலக்குகளைச் செயல்படுத்துகின்றன."
          ]
        }
      }
    ],
    "sec_case_laws_part3": [
      {
        "title": "1. Landmark Case Rulings Summary (பகுதி 3 வழக்குகள்)",
        "points": {
          "en": [
            "1. Stainislaus v. State of MP (1977): SC held that Right to Propagate under Art 25 does NOT include right to forcibly convert.",
            "2. S.R. Bommai v. Union of India (1994): Secularism declared part of the Basic Structure of the Constitution.",
            "3. T.M.A. Pai Foundation v. State of Karnataka (2002): Minority status under Art 30 determined state-wise based on state population.",
            "4. Minerva Mills v. Union of India (1980): Harmony between Part III & Part IV and Art 32 judicial review are Basic Structure.",
            "5. L. Chandra Kumar v. Union of India (1997): Writ jurisdiction of SC (Art 32) and HC (Art 226) declared Basic Structure.",
            "6. A.K. Kraipak v. Union of India (1969): Expanded Certiorari writ to administrative orders violating principles of natural justice."
          ],
          "ta": [
            "1. ஸ்டேனிஸ்லாஸ் எதிர் மத்தியப் பிரதேசம் (1977): உறுப்பு 25-ன் கீழ் பரப்பும் உரிமை பலவந்த மதமாற்ற உரிமையை உள்ளடக்கியது அல்ல எனத் தீர்ப்பளித்தது.",
            "2. எஸ்.ஆர். பொம்மை எதிர் இந்திய யூனியன் (1994): மதச்சார்பின்மை அரசியலமைப்பின் அடிப்படை கட்டமைப்பின் பகுதி என அறிவிக்கப்பட்டது.",
            "3. T.M.A. பாய் அறக்கட்டளை வழக்கு (2002): உறுப்பு 30-ன் கீழ் சிறுபான்மை அந்தஸ்து மாநில மக்கள் தொகையின் அடிப்படையில் மாநில வாரியாக தீர்மானிக்கப்பட வேண்டும்.",
            "4. மினர்வா மில்ஸ் எதிர் இந்திய யூனியன் (1980): பகுதி III & IV நல்லிணக்கம் மற்றும் உறுப்பு 32 நீதித்துறை ஆய்வு அடிப்படை கட்டமைப்பாகும்.",
            "5. எல். சந்திரகுமார் எதிர் இந்திய யூனியன் (1997): உச்ச நீதிமன்ற (32) மற்றும் உயர் நீதிமன்ற (226) மனு அதிகாரம் அடிப்படை கட்டமைப்பு என அறிவிக்கப்பட்டது.",
            "6. ஏ.கே. கிரைபக் எதிர் இந்திய யூனியன் (1969): இயற்கை நீதி தத்துவங்களை மீறும் நிர்வாக உத்தரவுகளுக்கும் நெறிமுறையுறுத்தும் பேராணையை (Certiorari) விரிவுபடுத்தியது."
          ]
        }
      }
    ],
    "sec_traps_connections_part3": [
      {
        "title": "1. Bilingual TNPSC Traps & High-Yield Revision (பொறிகளும் திருப்புதலும்)",
        "points": {
          "en": [
            "TRAP 1: Article 29(1) is NOT exclusively available to minorities; it applies to ANY section of citizens.\nதமிழ்: Article 29(1) சிறுபான்மையினருக்கு மட்டுமேயானது அல்ல; அது குடிமக்களின் எந்தவொரு பிரிவிற்கும் பொருந்தும்.\n\nTRAP 2: Word 'Minority' is NOT defined anywhere in the Constitution.\nதமிழ்: 'சிறுபான்மையினர்' என்ற சொல் அரசியலமைப்பில் எங்கும் வரையறுக்கப்படவில்லை.\n\nTRAP 3: Article 27 prohibits TAXES for religion, but permits FEES for services/regulation.\nதமிழ்: உறுப்பு 27 மதத்திற்காக வரிகளைத் தடுக்கிறது, ஆனால் கட்டணங்களை அனுமதிக்கிறது.\n\nTRAP 4: Quo Warranto is the ONLY writ where Locus Standi is relaxed (can be filed by any interested person).\nதமிழ்: தகுதி வினா பேராணை மட்டுமே பாதிக்கப்பட்ட நபர் மட்டுமின்றி எந்தவொரு ஆர்வமுள்ள நபராலும் கேட்கப்படலாம்.\n\nTRAP 5: Article 33 power to modify FRs of Armed Forces belongs EXCLUSIVELY to Parliament, NOT State Legislatures.\nதமிழ்: உறுப்பு 33-ன் கீழ் ஆயுதப் படைகளின் உரிமைகளைக் கட்டுப்படுத்தும் அதிகாரம் நாடாளுமன்றத்திற்கு மட்டுமே உண்டு."
          ],
          "ta": [
            "பொறி 1: Article 29(1) சிறுபான்மையினருக்கு மட்டுமேயானது அல்ல; அது குடிமக்களின் எந்தவொரு பிரிவிற்கும் பொருந்தும்.\n\nபொறி 2: 'சிறுபான்மையினர்' என்ற சொல் அரசியலமைப்பில் எங்கும் வரையறுக்கப்படவில்லை.\n\nபொறி 3: உறுப்பு 27 மதத்திற்காக வரிகளைத் தடுக்கிறது, ஆனால் கட்டணங்களை அனுமதிக்கிறது.\n\nபொறி 4: தகுதி வினா பேராணை மட்டுமே பாதிக்கப்பட்ட நபர் மட்டுமின்றி எந்தவொரு ஆர்வமுள்ள நபராலும் கேட்கப்படலாம்.\n\nபொறி 5: உறுப்பு 33-ன் கீழ் ஆயுதப் படைகளின் உரிமைகளைக் கட்டுப்படுத்தும் அதிகாரம் நாடாளுமன்றத்திற்கு மட்டுமே உண்டு."
          ]
        }
      },
      {
        "title": "2. High-Yield Revision Summary (முக்கிய திருப்புதல் சுருக்கம்)",
        "points": {
          "en": [
            "MUST REMEMBER QUICK REVISION LIST:\n- Art 25 = Individual freedom of conscience & religion (No forced conversion).\n- Art 26 = Collective freedom of religious denominations to manage affairs.\n- Art 27 = Immunity from taxation for religion (Fees allowed).\n- Art 28 = Regulates religious instruction in 4 categories of schools.\n- Art 29 = Protects language, script, culture of ANY section of citizens.\n- Art 30 = Religious & Linguistic Minorities right to establish educational institutions.\n- Art 31 -> Art 300A = Property right made legal right by 44th CAA 1978 in Part XII.\n- Art 32 = Constitutional Remedies (Dr. Ambedkar's Heart & Soul); 5 Writs (Habeas Corpus, Mandamus, Prohibition, Certiorari, Quo Warranto).\n- Arts 33-35 = Parliament exclusive power for Armed Forces, Martial Law, and FR enforcement laws."
          ],
          "ta": [
            "அவசிய நினைவில் கொள்ள வேண்டிய விரைவு திருப்புதல் பட்டியல்:\n- உறுப்பு 25 = தனிநபர் மனச்சாட்சி & மத சுதந்திரம் (பலவந்த மதமாற்றம் இல்லை).\n- உறுப்பு 26 = சமயக் குழுக்களின் கூட்டு மத விவகார நிர்வாக சுதந்திரம்.\n- உறுப்பு 27 = மதத்திற்கான வரிவிலக்கு (கட்டணம் அனுமதிக்கப்படும்).\n- உறுப்பு 28 = 4 வகை பள்ளிகளில் மதக் கல்வி போதனை ஒழுங்குமுறை.\n- உறுப்பு 29 = அனைத்துக் குடிமக்கள் பிரிவினரின் மொழி, எழுத்து, பண்பாட்டுப் பாதுகாப்பு.\n- உறுப்பு 30 = மத & மொழி சிறுபான்மையினரின் கல்வி நிறுவன உரிமை.\n- உறுப்பு 31 -> உறுப்பு 300A = 44வது திருத்தம் 1978 மூலம் பகுதி XII-ல் சட்டப்பூர்வ உரிமையாக்கம்.\n- உறுப்பு 32 = அரசியலமைப்புத் தீர்வுகள் (அம்பேத்கரின் இதயம் & ஆன்மா); 5 பேராணைகள்.\n- உறுப்புகள் 33-35 = ஆயுதப் படைகள், ராணுவ சட்டம், அமலாக்கச் சட்டங்களில் நாடாளுமன்ற பிரத்யேக அதிகாரம்."
          ]
        }
      }
    ]
  },
  "important_facts": {
    "en": [
      "Article 25 guarantees individual freedom of conscience and religion to both citizens and foreigners.",
      "Stainislaus Case (1977) ruled that Right to Propagate under Art 25 does NOT include right to forcibly convert.",
      "Article 26 protects collective rights of religious denominations (e.g. Ramakrishna Mission, Ananda Marga).",
      "Article 27 prohibits levying taxes for promoting religion, but DOES NOT prohibit levying fees for services.",
      "Article 28 completely bans religious instruction in educational institutions wholly maintained out of State funds.",
      "Article 29(1) applies to ANY section of citizens (majority and minority) having a distinct language, script, or culture.",
      "Article 30 guarantees educational rights EXCLUSIVELY to Religious and Linguistic Minorities.",
      "Word 'Minority' is NOT defined anywhere in the Constitution of India.",
      "T.M.A. Pai Foundation Case (2002) held minority status must be determined STATE-WISE.",
      "Right to Property was removed from Part III by the 44th Constitutional Amendment Act, 1978 and relocated to Article 300A in Part XII.",
      "Dr. B.R. Ambedkar called Article 32 the 'Heart and Soul' of the Constitution.",
      "Article 32 is specifically for enforcement of Fundamental Rights and is itself a Fundamental Right.",
      "Habeas Corpus is the only writ that can be issued against both public authorities and private individuals.",
      "Mandamus CANNOT be issued against private individuals, President, or State Governors.",
      "Prohibition is preventative only; Certiorari is both preventative and curative.",
      "Quo Warranto is the ONLY writ where Locus Standi is relaxed (can be sought by any interested person).",
      "Article 33 power to modify FRs for Armed Forces belongs EXCLUSIVELY to Parliament."
    ],
    "ta": [
      "உறுப்பு 25 குடிமக்கள் மற்றும் வெளிநாட்டினருக்குத் தனிநபர் மனச்சாட்சி மற்றும் மத சுதந்திரத்தை உத்தரவாதம் செய்கிறது.",
      "ஸ்டேனிஸ்லாஸ் வழக்கு (1977) பரப்பும் உரிமை பலவந்த மதமாற்ற உரிமையை உள்ளடக்கியது அல்ல எனத் தீர்ப்பளித்தது.",
      "உறுப்பு 26 சமயக் குழுக்களின் (எ.கா. ராமகிருஷ்ணா மிஷன்) கூட்டு உரிமைகளைப் பாதுகாக்கிறது.",
      "உறுப்பு 27 மதத்திற்காக வரி விதிப்பதைத் தடுக்கிறது, ஆனால் கட்டணம் விதிப்பதைத் தடுக்கவில்லை.",
      "உறுப்பு 28 முழுமையாக அரசு நிதியால் பராமரிக்கப்படும் கல்வி நிறுவனங்களில் மதக் கல்வியை முற்றிலும் தடை செய்கிறது.",
      "உறுப்பு 29(1) தனித்துவமான மொழி, எழுத்து கொண்ட குடிமக்களின் எந்தவொரு பிரிவிற்கும் பொருந்தும்.",
      "உறுப்பு 30 மத மற்றும் மொழி சிறுபான்மையினருக்கு மட்டுமே கல்வி நிறுவன உரிமைகளை உத்தரவாதம் செய்கிறது.",
      "'சிறுபான்மையினர்' என்ற சொல் இந்திய அரசியலமைப்பில் எங்கும் வரையறுக்கப்படவில்லை.",
      "T.M.A. பாய் வழக்கு (2002) சிறுபான்மை அந்தஸ்து மாநில வாரியாக தீர்மானிக்கப்பட வேண்டும் எனத் தீர்ப்பளித்தது.",
      "சொத்துரிமை 1978-ன் 44வது திருத்தச் சட்டத்தால் பகுதி III லிருந்து நீக்கப்பட்டு பகுதி XII-ல் உறுப்பு 300A-க்கு மாற்றப்பட்டது.",
      "டாக்டர் பி.ஆர். அம்பேத்கர் உறுப்பு 32-ஐ அரசியலமைப்பின் 'இதயமும் ஆன்மாவும்' என்று அழைத்தார்.",
      "உறுப்பு 32 அடிப்படை உரிமைகளை அமல்படுத்துவதற்காக மட்டுமே மற்றும் சுயமாகவே ஒரு அடிப்படை உரிமையாகும்.",
      "ஆட்கொணர்வு பேராணை (Habeas Corpus) மட்டுமே அரசு அமைப்புகள் மற்றும் தனியார் இருவருக்கும் எதிராக வழங்கப்படலாம்.",
      "செயலுறுத்தும் பேராணை (Mandamus) தனியார் நபர்கள், குடியரசுத் தலைவர், ஆளுநர்களுக்கு எதிராக வழங்க முடியாது.",
      "தடைசெய் பேராணை (Prohibition) தடுப்பு மட்டுமே; நெறிமுறையுறுத்தும் பேராணை (Certiorari) தடுப்பு மற்றும் நிவாரணம் இரண்டும் ஆகும்.",
      "தகுதி வினா பேராணை (Quo Warranto) மட்டுமே பாதிக்கப்பட்ட நபர் மட்டுமின்றி எந்தவொரு ஆர்வமுள்ள நபராலும் கேட்கப்படலாம்.",
      "உறுப்பு 33-ன் கீழ் ஆயுதப் படைகளின் உரிமைகளைக் கட்டுப்படுத்தும் அதிகாரம் நாடாளுமன்றத்திற்கு மட்டுமே உண்டு."
    ]
  },
  "tnpsc_traps": [
    "⚠️ TRAP 1: Article 29(1) applies to ANY section of citizens (including majority), NOT exclusively to minorities.\nதமிழ்: Article 29(1) சிறுபான்மையினருக்கு மட்டுமேயானது அல்ல; அது குடிமக்களின் எந்தவொரு பிரிவிற்கும் பொருந்தும்.",
    "⚠️ TRAP 2: The word 'Minority' is NOT defined anywhere in the Constitution of India.\nதமிழ்: 'சிறுபான்மையினர்' என்ற சொல் இந்திய அரசியலமைப்பில் எங்கும் வரையறுக்கப்படவில்லை.",
    "⚠️ TRAP 3: Article 27 prohibits TAXES for promoting religion, but DOES NOT prohibit FEES for services/regulation.\nதமிழ்: உறுப்பு 27 மதத்திற்காக வரிகளைத் தடுக்கிறது, ஆனால் கட்டணங்களை அனுமதிக்கிறது.",
    "⚠️ TRAP 4: Right to Property under Article 300A is a Legal/Constitutional Right in Part XII, NOT a Fundamental Right.\nதமிழ்: உறுப்பு 300A-ன் கீழ் உள்ள சொத்துரிமை பகுதி XII-ல் உள்ள சட்டப்பூர்வ உரிமையே தவிர அடிப்படை உரிமை அல்ல.",
    "⚠️ TRAP 5: Article 32 is specifically for enforcement of Fundamental Rights. Article 226 (High Court) has a WIDER scope.\nதமிழ்: உறுப்பு 32 அடிப்படை உரிமைகளை அமல்படுத்துவதற்கு மட்டுமே. உறுப்பு 226 (உயர் நீதிமன்றம்) விரிவான எல்லை கொண்டது.",
    "⚠️ TRAP 6: Quo Warranto is the ONLY writ where Locus Standi is relaxed (can be filed by any interested person).\nதமிழ்: தகுதி வினா பேராணை மட்டுமே பாதிக்கப்பட்ட நபர் மட்டுமின்றி எந்தவொரு ஆர்வமுள்ள நபராலும் கேட்கப்படலாம்.",
    "⚠️ TRAP 7: Mandamus CANNOT be issued against private individuals, President, or State Governors.\nதமிழ்: செயலுறுத்தும் பேராணையைத் தனியார் நபர்கள், குடியரசுத் தலைவர், ஆளுநர்களுக்கு எதிராகப் பிறப்பிக்க முடியாது.",
    "⚠️ TRAP 8: Article 33 legislative power rests EXCLUSIVELY with Parliament, NOT State Legislatures.\nதமிழ்: உறுப்பு 33 நாடாளுமன்றத்திற்கு மட்டுமே பிரத்யேக அதிகாரத்தை வழங்குகிறது, மாநில சட்டமன்றங்களுக்கு இல்லை."
  ],
  "tables": [
    {
      "id": "tbl_art25_28_religion",
      "title_en": "Articles 25 to 28 Freedom of Religion Summary",
      "title_ta": "உறுப்புகள் 25 முதல் 28 மத சுதந்திர சுருக்கம்",
      "headers_en": [
        "Article",
        "Core Guarantee Focus",
        "Individual vs Collective",
        "Key Limitation / Exception",
        "TNPSC Takeaway"
      ],
      "headers_ta": [
        "உறுப்பு",
        "முதன்மை உத்தரவாத மையம்",
        "தனிநபர் vs கூட்டு",
        "முக்கிய வரம்பு / விலக்கு",
        "டிஎன்பிஎஸ்சி குறிப்பு"
      ],
      "rows_en": [
        [
          "Article 25",
          "Conscience, Profess, Practise, Propagate religion",
          "INDIVIDUAL Right (All Persons)",
          "Public order, morality, health; No forced conversion",
          "Kirpan allowed for Sikhs; 'Hindu' includes Sikh, Jain, Buddhist"
        ],
        [
          "Article 26",
          "Manage religious affairs, institutions, & property",
          "COLLECTIVE Right (Religious Denomination)",
          "Public order, morality, and health ONLY",
          "Does NOT include 'other Part III provisions' limitation"
        ],
        [
          "Article 27",
          "Freedom from taxation to promote particular religion",
          "Financial immunity against state favoritism",
          "Prohibits TAXES; Does NOT prohibit FEES",
          "Temple pilgrim fees are constitutionally valid"
        ],
        [
          "Article 28",
          "Freedom from religious instruction in schools",
          "Institutional secularism",
          "Banned in wholly State-funded schools",
          "Voluntary in State-aided/recognized schools"
        ]
      ],
      "rows_ta": [
        [
          "உறுப்பு 25",
          "மனச்சாட்சி, வெளிப்படையாகக் கூறல், பின்பற்றல், பரப்புதல்",
          "TANI NABAR (தனிநபர்) உரிமை (அனைத்து நபர்களும்)",
          "பொது ஒழுங்கு, ஒழுக்கம், சுகாதாரம்; பலவந்த மதமாற்றம் இல்லை",
          "சீக்கியர்களுக்கு கிர்பான் அனுமதி; 'இந்து' என்பதில் சீக்கியர், ஜைனர், பௌத்தர் அடங்குவர்"
        ],
        [
          "உறுப்பு 26",
          "மத விவகாரங்கள், நிறுவனங்கள் & சொத்துக்களை நிர்வகித்தல்",
          "KOOTTU (கூட்டு) உரிமை (சமயக் குழு)",
          "பொது ஒழுங்கு, ஒழுக்கம், சுகாதாரம் மட்டுமே",
          "பகுதி III-ன் பிற விதிகளுக்கு உட்பட்டது என்ற சொல் இல்லை"
        ],
        [
          "உறுப்பு 27",
          "குறிப்பிட்ட மதத்தை ஊக்குவிக்க வரி செலுத்தலிலிருந்து சுதந்திரம்",
          "அரசுச் சார்புக்கு எதிரான நிதி விலக்கு",
          "வரிகளைத் தடுக்கிறது; கட்டணங்களைத் தடுக்கவில்லை",
          "கோயில் யாத்திரீகர் கட்டணம் அரசியலமைப்பு ரீதியாக செல்லுபடியாகும்"
        ],
        [
          "உறுப்பு 28",
          "பள்ளிகளில் மதக் கல்வி போதனையிலிருந்து சுதந்திரம்",
          "நிறுவன மதச்சார்பின்மை",
          "முழுமையான அரசு நிதிப் பள்ளிகளில் முற்றிலும் தடை",
          "அரசு உதவிபெறும்/அங்கீகரிக்கப்பட்ட பள்ளிகளில் விருப்பத்தின் பேரில்"
        ]
      ]
    },
    {
      "id": "tbl_art29_vs_art30",
      "title_en": "Article 29 vs Article 30 Comparison",
      "title_ta": "உறுப்பு 29 vs உறுப்பு 30 ஒப்பீடு",
      "headers_en": [
        "Dimension",
        "Article 29 (Conservation of Culture & Admission)",
        "Article 30 (Minority Educational Institutions)"
      ],
      "headers_ta": [
        "பரிமாணம்",
        "உறுப்பு 29 (பண்பாட்டுப் பாதுகாப்பு & சேர்க்கை)",
        "உறுப்பு 30 (சிறுபான்மையினர் கல்வி நிறுவனங்கள்)"
      ],
      "rows_en": [
        [
          "Beneficiary Scope",
          "ANY SECTION of Citizens (Majority and Minorities)",
          "EXCLUSIVELY Religious and Linguistic Minorities"
        ],
        [
          "Core Right Granted",
          "Right to conserve distinct language, script, or culture",
          "Right to establish and administer educational institutions of choice"
        ],
        [
          "Non-Discrimination Grounds",
          "4 Grounds in Art 29(2): Religion, Race, Caste, Language",
          "State aid non-discrimination under Art 30(2)"
        ],
        [
          "Judicial Principle",
          "Protects language/culture conservation generally",
          "T.M.A. Pai 2002: Minority status determined STATE-WISE"
        ]
      ],
      "rows_ta": [
        [
          "பயனாளி எல்லை",
          "குடிமக்களின் எந்தவொரு பிரிவினர் (பெரும்பான்மையினர் & சிறுபான்மையினர்)",
          "மத மற்றும் மொழி சிறுபான்மையினருக்கு மட்டுமே"
        ],
        [
          "வழங்கப்பட்ட முதன்மை உரிமை",
          "தனித்துவமான மொழி, எழுத்து அல்லது பண்பாட்டைப் பாதுகாக்கும் உரிமை",
          "விருப்பமான கல்வி நிறுவனங்களை நிறுவவும் நிர்வகிக்கவும் உரிமை"
        ],
        [
          "பாகுபாடின்மை அடிப்படைகள்",
          "உறுப்பு 29(2)-ல் 4 அடிப்படைகள்: மதம், இனம், சாதி, மொழி",
          "உறுப்பு 30(2)-ன் கீழ் அரசு நிதியுதவி பாகுபாடின்மை"
        ],
        [
          "நீதிமுறைத் தத்துவம்",
          "பொதுவாக மொழி/பண்பாட்டுப் பாதுகாப்பைப் பாதுகாக்கிறது",
          "T.M.A. பாய் 2002: சிறுபான்மை அந்தஸ்து மாநில வாரியாக நிர்ணயம்"
        ]
      ]
    },
    {
      "id": "tbl_art31_vs_art300a",
      "title_en": "Article 31 vs Article 300A (Right to Property Shift)",
      "title_ta": "உறுப்பு 31 vs உறுப்பு 300A (சொத்துரிமை மாற்றம்)",
      "headers_en": [
        "Feature",
        "Article 31 (Original Position)",
        "Article 300A (Present Position)"
      ],
      "headers_ta": [
        "அம்சம்",
        "உறுப்பு 31 (அசல் நிலை)",
        "உறுப்பு 300A (தற்போதைய நிலை)"
      ],
      "rows_en": [
        [
          "Location & Part",
          "Part III (Fundamental Rights)",
          "Part XII (Chapter IV - Legal/Constitutional Right)"
        ],
        [
          "Amendment Action",
          "Omitted by 44th Constitutional Amendment Act, 1978",
          "Inserted by 44th Constitutional Amendment Act, 1978"
        ],
        [
          "Remedy for Violation",
          "Direct Supreme Court Writ Petition under Article 32",
          "High Court Writ under Article 226 or Ordinary Civil Suit"
        ],
        [
          "Protection & Compensation",
          "Protected against both Executive and Legislative action; Compensation guaranteed",
          "Protected ONLY against Executive action; Compensation NOT guaranteed by Constitution"
        ]
      ],
      "rows_ta": [
        [
          "இடம் & பகுதி",
          "பகுதி III (அடிப்படை உரிமைகள்)",
          "பகுதி XII (அத்தியாயம் IV - சட்டப்பூர்வ/அரசியலமைப்பு உரிமை)"
        ],
        [
          "திருத்த நடவடிக்கை",
          "1978-ன் 44வது அரசியலமைப்பு திருத்தச் சட்டத்தால் நீக்கப்பட்டது",
          "1978-ன் 44வது அரசியலமைப்பு திருத்தச் சட்டத்தால் சேர்க்கப்பட்டது"
        ],
        [
          "மீறலுக்கான தீர்வு",
          "உறுப்பு 32-ன் கீழ் நேரடி உச்ச நீதிமன்ற மனு",
          "உயர் நீதிமன்ற உறுப்பு 226 மனு அல்லது சாதாரண சிவில் வழக்கு"
        ],
        [
          "பாதுகாப்பு & இழப்பீடு",
          "நிர்வாக மற்றும் சட்டமன்ற நடவடிக்கைகளுக்கு எதிராகப் பாதுகாப்பு; இழப்பீடு கட்டாயம்",
          "நிர்வாக நடவடிக்கைக்கு மட்டுமே பாதுகாப்பு; இழப்பீடு அரசியலமைப்பு ரீதியாக கட்டாயமில்லை"
        ]
      ]
    },
    {
      "id": "tbl_art32_vs_art226",
      "title_en": "Article 32 vs Article 226 Writ Jurisdiction Comparison",
      "title_ta": "உறுப்பு 32 vs உறுப்பு 226 மனு அதிகாரம் ஒப்பீடு",
      "headers_en": [
        "Dimension",
        "Article 32 (Supreme Court)",
        "Article 226 (High Court)"
      ],
      "headers_ta": [
        "பரிமாணம்",
        "உறுப்பு 32 (உச்ச நீதிமன்றம்)",
        "உறுப்பு 226 (உயர் நீதிமன்றம்)"
      ],
      "rows_en": [
        [
          "Constitutional Status",
          "Itself a Fundamental Right in Part III",
          "Constitutional provision in Part VI (Not a FR itself)"
        ],
        [
          "Enforcement Purpose",
          "ONLY for enforcement of Fundamental Rights",
          "For Fundamental Rights AND ordinary legal rights ('any other purpose')"
        ],
        [
          "Nature of Remedy",
          "MANDATORY: SC cannot refuse to entertain a valid FR petition",
          "DISCRETIONARY: HC may refuse to issue writ if alternative remedy exists"
        ],
        [
          "Territorial Scope",
          "Wider territorial jurisdiction (Entire territory of India)",
          "Narrower territorial jurisdiction (Within state or cause of action)"
        ]
      ],
      "rows_ta": [
        [
          "அரசியலமைப்பு அந்தஸ்து",
          "பகுதி III-ல் சுயமாகவே ஒரு அடிப்படை உரிமை",
          "பகுதி VI-ல் உள்ள அரசியலமைப்பு விதி (அடிப்படை உரிமை அல்ல)"
        ],
        [
          "அமலாக்க நோக்கம்",
          "அடிப்படை உரிமைகளை அமல்படுத்துவதற்கு மட்டுமே",
          "அடிப்படை உரிமைகள் மற்றும் சாதாரண சட்டப்பூர்வ உரிமைகளுக்காக ('வேறு எந்த நோக்கத்திற்காகவும்')"
        ],
        [
          "தீர்வின் இயல்பு",
          "KATTAYAM (கட்டாயம்): மனுவை விசாரிக்க உச்ச நீதிமன்றம் மறுக்க முடியாது",
          "VIRUPPAM (விருப்பத்திற்குரியது): உயர் நீதிமன்றம் மனுவை நிராகரிக்கலாம்"
        ],
        [
          "நிலப்பரப்பு எல்லை",
          "விரிவான நிலப்பரப்பு எல்லை (இந்திய நிலப்பரப்பு முழுவதும்)",
          "குறுகிய நிலப்பரப்பு எல்லை (மாநிலத்திற்குள் மட்டுமே)"
        ]
      ]
    },
    {
      "id": "tbl_five_writs_comparison",
      "title_en": "Summary of Five Prerogative Writs",
      "title_ta": "ஐந்து நீதிப் பேராணைகளின் சுருக்கம்",
      "headers_en": [
        "Writ Name",
        "Literal Meaning",
        "Core Purpose",
        "Targeted Against",
        "Key Identification / Locus Standi"
      ],
      "headers_ta": [
        "பேராணை பெயர்",
        "நேரடிப் பொருள்",
        "முதன்மை நோக்கம்",
        "யாருக்கு எதிராக",
        "முக்கிய அடையாளம் / மனு தாக்கல் செய்யும் உரிமை"
      ],
      "rows_en": [
        [
          "Habeas Corpus",
          "To have the body of",
          "Release person illegally detained",
          "Public authorities AND Private individuals",
          "Bulwark of individual liberty against arbitrary detention"
        ],
        [
          "Mandamus",
          "We Command",
          "Command public official to perform statutory duty",
          "Public officers, bodies, lower courts",
          "CANNOT be issued against private bodies, President/Governors"
        ],
        [
          "Prohibition",
          "To Forbid",
          "Prevent lower court from exceeding jurisdiction",
          "Judicial and Quasi-Judicial bodies ONLY",
          "PREVENTATIVE only ('Prevention is better than cure')"
        ],
        [
          "Certiorari",
          "To be certified",
          "Quash illegal order passed by lower authority",
          "Judicial, Quasi-Judicial AND Administrative bodies",
          "BOTH Preventative and Curative"
        ],
        [
          "Quo Warranto",
          "By what authority?",
          "Inquire into legality of claim to public office",
          "Substantive public office holders created by statute",
          "LOCUS STANDI RELAXED: Can be filed by ANY interested person"
        ]
      ],
      "rows_ta": [
        [
          "ஆட்கொணர்வு (Habeas Corpus)",
          "உடலைக் கொண்டு வா",
          "சட்டவிரோதமாகக் காவலில் வைக்கப்பட்டவரை விடுவித்தல்",
          "அரசு அமைப்புகள் & தனியார் நபர்கள்",
          "தன்னிச்சையான காவலுக்கு எதிரான தனிநபர் சுதந்திரக் கேடயம்"
        ],
        [
          "செயலுறுத்தும் (Mandamus)",
          "நாங்கள் கட்டளையிடுகிறோம்",
          "அரசு அதிகாரியைச் சட்டப்பூர்வப் பணியைச் செய்யக் பணித்தல்",
          "அரசு அதிகாரிகள், அமைப்புகள், கீழ் நீதிமன்றங்கள்",
          "தனியார் அமைப்புகள், குடியரசுத் தலைவர்/ஆளுநர்களுக்கு எதிராக முடியாது"
        ],
        [
          "தடைசெய் (Prohibition)",
          "தடுப்பது / தட்டறுப்பது",
          "கீழ் நீதிமன்றம் அதிகார வரம்பை மீறுவதைத் தடுத்தல்",
          "நீதித்துறை & பகுதி-நீதித்துறை அமைப்புகள் மட்டுமே",
          "தடுப்பு நடவடிக்கை மட்டுமே ('வருமுன் காப்பதே மேல்')"
        ],
        [
          "நெறிமுறையுறுத்தும் (Certiorari)",
          "சான்றளிப்பது / முழுமையாக அறிவது",
          "சட்டவிரோத உத்தரவை ரத்து செய்தல்",
          "நீதித்துறை, பகுதி-நீதித்துறை & நிர்வாக அமைப்புகள்",
          "தடுப்பு மற்றும் நிவாரண நடவடிக்கை இரண்டும்"
        ],
        [
          "தகுதி வினா (Quo Warranto)",
          "எந்த அதிகாரத்தின் அடிப்படையில்?",
          "பொதுப் பதவியைக் கைப்பற்றுவதைத் தடுத்தல்",
          "சட்டத்தால் உருவாக்கப்பட்ட பொதுப் பதவி வகிப்போர்",
          "LOCUS STANDI தளர்த்தப்பட்டது: எந்தவொரு ஆர்வமுள்ள நபரும் மனு தாக்கல் செய்யலாம்"
        ]
      ]
    },
    {
      "id": "tbl_fr_vs_dpsp",
      "title_en": "Fundamental Rights (Part III) vs Directive Principles (Part IV)",
      "title_ta": "அடிப்படை உரிமைகள் (பகுதி III) vs அரசு நெறிமுறைக் கோட்பாடுகள் (பகுதி IV)",
      "headers_en": [
        "Dimension",
        "Fundamental Rights (Part III)",
        "Directive Principles (Part IV)"
      ],
      "headers_ta": [
        "பரிமாணம்",
        "அடிப்படை உரிமைகள் (பகுதி III)",
        "அரசு நெறிமுறைக் கோட்பாடுகள் (பகுதி IV)"
      ],
      "rows_en": [
        [
          "Justiciability",
          "JUSTICIABLE (Enforceable through Courts under Arts 32 & 226)",
          "NON-JUSTICIABLE (Not enforceable through courts)"
        ],
        [
          "Democracy Type",
          "Establishes POLITICAL Democracy",
          "Establishes SOCIAL and ECONOMIC Democracy (Welfare State)"
        ],
        [
          "Nature & Sanction",
          "Negative obligations on State; Legal Sanctions",
          "Positive obligations on State; Moral & Political Sanctions"
        ],
        [
          "Constitutional Balance",
          "Minerva Mills (1980): Harmonious balance between Part III & Part IV is Basic Structure",
          "DPSP guides legislation; Art 31C saves 39(b) & (c) laws overriding Arts 14 & 19"
        ]
      ],
      "rows_ta": [
        [
          "நீதிமன்ற அமலாக்கம்",
          "JUSTICIABLE (உறுப்புகள் 32 & 226 மூலம் நீதிமன்றத்தால் அமல்படுத்தக்கூடியவை)",
          "NON-JUSTICIABLE (நீதிமன்றத்தால் அமல்படுத்த முடியாதவை)"
        ],
        [
          "ஜனநாயக வகை",
          "ARASIYAL (அரசியல்) ஜனநாயகத்தை நிறுவுகிறது",
          "SAMUGA & PORULADHARA (சமூக & பொருளாதார) ஜனநாயகத்தை நிறுவுகிறது",
        ],
        [
          "இயல்பு & அதிகாரம்",
          "அரசுக்கான எதிர்மறைக் கடமைகள்; சட்டப்பூர்வ அதிகாரம்",
          "அரசுக்கான நேர்மறைக் கடமைகள்; ஒழுக்க & அரசியல் அதிகாரம்"
        ],
        [
          "அரசியலமைப்பு சமநிலை",
          "மினர்வா மில்ஸ் (1980): பகுதி III & IV நல்லிணக்கச் சமநிலை அடிப்படை கட்டமைப்பு",
          "DPSP சட்டமியற்றலை வழிகாட்டுகிறது; உறுப்பு 31C 39(b)&(c) சட்டங்களைக் காப்பாற்றுகிறது"
        ]
      ]
    },
    {
      "id": "tbl_fr_vs_fd",
      "title_en": "Fundamental Rights (Part III) vs Fundamental Duties (Part IV-A)",
      "title_ta": "அடிப்படை உரிமைகள் (பகுதி III) vs அடிப்படை கடமைகள் (பகுதி IV-A)",
      "headers_en": [
        "Dimension",
        "Fundamental Rights (Part III)",
        "Fundamental Duties (Part IV-A)"
      ],
      "headers_ta": [
        "பரிமாணம்",
        "அடிப்படை உரிமைகள் (பகுதி III)",
        "அடிப்படை கடமைகள் (பகுதி IV-A)"
      ],
      "rows_en": [
        [
          "Core Focus",
          "Guarantees Rights & Liberty TO Citizens/Persons",
          "Prescribes Obligations & Duties FOR Citizens"
        ],
        [
          "Constitutional Insertion",
          "Original 1950 Constitution",
          "Added by 42nd CAA 1976 (Swaran Singh Committee) & 86th CAA 2002"
        ],
        [
          "Justiciability",
          "Justiciable directly via writs",
          "Non-justiciable directly, but Parliament can enact enforcement laws"
        ],
        [
          "Correlative Nature",
          "Rights cannot exist without duties; duty performance strengthens rights",
          "Article 51A(k) duty directly supports Article 21A right to education"
        ]
      ],
      "rows_ta": [
        [
          "முதன்மை மையம்",
          "குடிமக்கள்/நபர்களுக்கு உரிமைகள் & சுதந்திரத்தை உத்தரவாதம் செய்கிறது",
          "குடிமக்களுக்கான கடமைகளை நிர்ணயிக்கிறது"
        ],
        [
          "அரசியலமைப்புச் சேர்ப்பு",
          "அசல் 1950 அரசியலமைப்பு",
          "1976-ன் 42வது திருத்தம் (சுவரண் சிங் குழு) & 2002-ன் 86வது திருத்தம்"
        ],
        [
          "நீதிமன்ற அமலாக்கம்",
          "மனுக்கள் மூலம் நேரடியாக நிலைநிறுத்தக்கூடியவை",
          "நேரடியாக நிலைநிறுத்த முடியாது, ஆனால் நாடாளுமன்றம் அமலாக்கச் சட்டங்களை இயற்றலாம்"
        ],
        [
          "ஒன்றோடொன்று தொடர்பு",
          "கடமைகளின்றி உரிமைகள் இருக்க முடியாது; கடமை நிறைவேற்றம் உரிமைகளைப் பலப்படுத்துகிறது",
          "உறுப்பு 51A(k) கடமை உறுப்பு 21A கல்வி உரிமையை நேரடியாக ஆதரிக்கிறது"
        ]
      ]
    }
  ],
  "concept_map": [
    {
      "id": "mm_fr3_root",
      "parent_id": None,
      "title": "Fundamental Rights Part 3 (அடிப்படை உரிமைகள் - பகுதி 3)",
      "short_label": "FR Part 3"
    },
    {
      "id": "mm_religion_root",
      "parent_id": "mm_fr3_root",
      "title": "Freedom of Religion (Articles 25 to 28)",
      "short_label": "Freedom of Religion"
    },
    {
      "id": "mm_art25",
      "parent_id": "mm_religion_root",
      "title": "Article 25: Conscience, Profess, Practise, Propagate (No Forced Conversion)",
      "short_label": "Art 25: Religion"
    },
    {
      "id": "mm_art26",
      "parent_id": "mm_religion_root",
      "title": "Article 26: Manage Religious Affairs & Institutions (Denominational Rights)",
      "short_label": "Art 26: Denominations"
    },
    {
      "id": "mm_art27",
      "parent_id": "mm_religion_root",
      "title": "Article 27: Freedom from Religious Taxation (Taxes Banned, Fees Allowed)",
      "short_label": "Art 27: Tax Freedom"
    },
    {
      "id": "mm_art28",
      "parent_id": "mm_religion_root",
      "title": "Article 28: Religious Instruction Rules in 4 Categories of Schools",
      "short_label": "Art 28: Instruction"
    },
    {
      "id": "mm_culture_root",
      "parent_id": "mm_fr3_root",
      "title": "Cultural & Educational Rights (Articles 29 & 30)",
      "short_label": "Cultural Rights"
    },
    {
      "id": "mm_art29",
      "parent_id": "mm_culture_root",
      "title": "Article 29: Conserve Language/Script/Culture (Applies to ANY Section of Citizens)",
      "short_label": "Art 29: Conservation"
    },
    {
      "id": "mm_art30",
      "parent_id": "mm_culture_root",
      "title": "Article 30: Religious & Linguistic Minorities Educational Institutions",
      "short_label": "Art 30: Minorities"
    },
    {
      "id": "mm_art32_root",
      "parent_id": "mm_fr3_root",
      "title": "Article 32: Constitutional Remedies (Heart & Soul of Constitution)",
      "short_label": "Art 32 Remedies"
    },
    {
      "id": "mm_five_writs",
      "parent_id": "mm_art32_root",
      "title": "Five Writs: Habeas Corpus, Mandamus, Prohibition, Certiorari, Quo Warranto",
      "short_label": "Five Writs"
    },
    {
      "id": "mm_arts_33_35",
      "parent_id": "mm_fr3_root",
      "title": "Articles 33-35: Armed Forces Restriction, Martial Law & Parliamentary Power",
      "short_label": "Arts 33-35"
    },
    {
      "id": "mm_art300a",
      "parent_id": "mm_fr3_root",
      "title": "Article 300A: Right to Property as Legal Right (44th CAA 1978 in Part XII)",
      "short_label": "Art 300A Property"
    }
  ],
  "revision_cards": [
    {
      "id": "RC_FR3_001",
      "title": {
        "en": "Article 25 Propagate Limit",
        "ta": "உறுப்பு 25 பரப்பும் உரிமை வரம்பு"
      },
      "front": {
        "en": "Does the Right to Propagate religion under Article 25 include the right to forcibly convert?",
        "ta": "உறுப்பு 25-ன் கீழ் மதத்தைப் பரப்பும் உரிமை பலவந்த மதமாற்ற உரிமையை உள்ளடக்குமா?"
      },
      "back": {
        "en": "NO. In Stainislaus Case (1977), SC held that Art 25 does NOT include the right to convert another person, as forced conversion violates the freedom of conscience of the converted person.",
        "ta": "இல்லை. ஸ்டேனிஸ்லாஸ் வழக்கில் (1977), பலவந்த மதமாற்றம் மதமாற்றம் செய்யப்பட்டவரின் மனச்சாட்சி சுதந்திரத்தைப் பாதிப்பதால் அது உறுப்பு 25-ல் அடங்காது என தீர்ப்பளிக்கப்பட்டது."
      },
      "one_line_revision": "Art 25 Propagate = Transmit tenets; Forced conversion is UNCONSTITUTIONAL.",
      "type": "trap"
    },
    {
      "id": "RC_FR3_002",
      "title": {
        "en": "Article 27 Tax vs Fee",
        "ta": "உறுப்பு 27 வரி vs கட்டணம்"
      },
      "front": {
        "en": "Does Article 27 prohibit levying fees on religious pilgrims or temples?",
        "ta": "உறுப்பு 27 மத யாத்திரீகர்கள் அல்லது கோயில்கள் மீது கட்டணம் (Fee) விதிப்பதைத் தடுக்கிறதா?"
      },
      "back": {
        "en": "NO. Article 27 prohibits TAXES for religion, but permits FEES for providing special services, safety, or regulation.",
        "ta": "இல்லை. உறுப்பு 27 மதத்திற்காக வரிகளைத் (Taxes) தடுக்கிறது, ஆனால் சிறப்புச் சேவைகள்/ஒழுங்குமுறைக்கான கட்டணங்களை (Fees) அனுமதிக்கிறது."
      },
      "one_line_revision": "Art 27 = Religious TAXES prohibited; FEES for services permitted.",
      "type": "trap"
    },
    {
      "id": "RC_FR3_003",
      "title": {
        "en": "Article 29 Scope",
        "ta": "உறுப்பு 29 எல்லை"
      },
      "front": {
        "en": "Is Article 29 exclusively available to minority communities?",
        "ta": "உறுப்பு 29 சிறுபான்மை சமூகத்தினருக்கு மட்டுமே கிடைக்கக்கூடியதா?"
      },
      "back": {
        "en": "NO. Article 29(1) applies to ANY SECTION OF CITIZENS (including majority) having a distinct language, script, or culture.",
        "ta": "இல்லை. உறுப்பு 29(1) தனித்துவமான மொழி, எழுத்து கொண்ட குடிமக்களின் எந்தவொரு பிரிவிற்கும் (பெரும்பான்மையினர் உட்பட) பொருந்தும்."
      },
      "one_line_revision": "Art 29(1) = Applies to ANY section of citizens (Not exclusively minorities).",
      "type": "trap"
    },
    {
      "id": "RC_FR3_004",
      "title": {
        "en": "Article 30 Minorities",
        "ta": "உறுப்பு 30 சிறுபான்மையினர்"
      },
      "front": {
        "en": "What types of minorities are recognized under Article 30?",
        "ta": "உறுப்பு 30-ன் கீழ் எந்த வகையான சிறுபான்மையினர் அங்கீகரிக்கப்பட்டுள்ளனர்?"
      },
      "back": {
        "en": "RELIGIOUS and LINGUISTIC Minorities only. (TRAP: The word 'Minority' is NOT defined in the Constitution).",
        "ta": "மத மற்றும் மொழி சிறுபான்மையினர் மட்டுமே. (பொறி: 'சிறுபான்மையினர்' என்ற சொல் அரசியலமைப்பில் வரையறுக்கப்படவில்லை)."
      },
      "one_line_revision": "Art 30 = Religious & Linguistic Minorities only; Minority status determined State-wise.",
      "type": "fact"
    },
    {
      "id": "RC_FR3_005",
      "title": {
        "en": "Right to Property Status",
        "ta": "சொத்துரிமை அந்தஸ்து"
      },
      "front": {
        "en": "What is the present constitutional status of the Right to Property?",
        "ta": "சொத்துரிமையின் தற்போதைய அரசியலமைப்பு அந்தஸ்து என்ன?"
      },
      "back": {
        "en": "CONSTITUTIONAL / LEGAL RIGHT under Article 300A in Part XII (inserted by 44th Constitutional Amendment Act, 1978). NOT a Fundamental Right.",
        "ta": "பகுதி XII-ல் உறுப்பு 300A-ன் கீழ் உள்ள அரசியலமைப்பு / சட்டப்பூர்வ உரிமை (1978-ன் 44வது திருத்தத்தால் மாற்றப்பட்டது). அடிப்படை உரிமை அல்ல."
      },
      "one_line_revision": "Right to Property = Legal Right under Art 300A (Part XII) via 44th CAA 1978.",
      "type": "fact"
    },
    {
      "id": "RC_FR3_006",
      "title": {
        "en": "Article 32 Ambedkar Description",
        "ta": "உறுப்பு 32 அம்பேத்கர் விளக்கம்"
      },
      "front": {
        "en": "How did Dr. B.R. Ambedkar describe Article 32?",
        "ta": "உறுப்பு 32-ஐ டாக்டர் பி.ஆர். அம்பேத்கர் எவ்வாறு விவரித்தார்?"
      },
      "back": {
        "en": "As the 'VERY SOUL OF THE CONSTITUTION AND THE VERY HEART OF IT'.",
        "ta": "'அரசியலமைப்பின் இதயம் மற்றும் ஆன்மா' என விவரித்தார்."
      },
      "one_line_revision": "Art 32 = Heart & Soul of Constitution (Dr. Ambedkar); Enforces Part III rights.",
      "type": "concept"
    },
    {
      "id": "RC_FR3_007",
      "title": {
        "en": "Quo Warranto Locus Standi",
        "ta": "தகுதி வினா பேராணை மனு உரிமை"
      },
      "front": {
        "en": "Why is Quo Warranto unique among the Five Writs regarding Locus Standi?",
        "ta": "மனு தாக்கல் செய்யும் உரிமையில் (Locus Standi) ஐந்து பேராணைகளில் தகுதி வினா பேராணை ஏன் தனித்துவமானது?"
      },
      "back": {
        "en": "Locus Standi is RELAXED. Unlike other writs, Quo Warranto can be filed by ANY INTERESTED PERSON, not strictly the aggrieved party.",
        "ta": "மனு உரிமை தளர்த்தப்பட்டுள்ளது. பிற பேராணைகளைப் போலன்றி, பாதிக்கப்பட்ட நபர் மட்டுமின்றி எந்தவொரு ஆர்வமுள்ள நபராலும் மனு தாக்கல் செய்யப்படலாம்."
      },
      "one_line_revision": "Quo Warranto = Locus standi relaxed; Any interested person can file.",
      "type": "trap"
    },
    {
      "id": "RC_FR3_008",
      "title": {
        "en": "Prohibition vs Certiorari",
        "ta": "தடைசெய் vs நெறிமுறையுறுத்தும் பேராணை"
      },
      "front": {
        "en": "What is the key difference between Prohibition and Certiorari writs?",
        "ta": "தடைசெய் பேராணைக்கும் நெறிமுறையுறுத்தும் பேராணைக்கும் இடையேயான முக்கிய வேறுபாடு என்ன?"
      },
      "back": {
        "en": "Prohibition is PREVENTATIVE ONLY (issued while case is pending). Certiorari is BOTH PREVENTATIVE AND CURATIVE (issued after order passed to quash it).",
        "ta": "தடைசெய் பேராணை தடுப்பு மட்டுமே (வழக்கு நிலுவையில் இருக்கும் போது). நெறிமுறையுறுத்தும் பேராணை தடுப்பு மற்றும் நிவாரணம் இரண்டும் (உத்தரவு பிறப்பிக்கப்பட்ட பின் அதை ரத்து செய்ய)."
      },
      "one_line_revision": "Prohibition = Preventative only; Certiorari = Preventative + Curative (Quashes order).",
      "type": "comparison"
    },
    {
      "id": "RC_FR3_009",
      "title": {
        "en": "Article 33 Exclusive Power",
        "ta": "உறுப்பு 33 பிரத்யேக அதிகாரம்"
      },
      "front": {
        "en": "Who has the power to restrict Fundamental Rights of Armed Forces under Article 33?",
        "ta": "உறுப்பு 33-ன் கீழ் ஆயுதப் படைகளின் அடிப்படை உரிமைகளைக் கட்டுப்படுத்தும் அதிகாரம் யாருக்கு உண்டு?"
      },
      "back": {
        "en": "PARLIAMENT ONLY. State Legislatures have NO power under Article 33.",
        "ta": "நாடாளுமன்றத்திற்கு மட்டுமே (PARLIAMENT ONLY). மாநில சட்டமன்றங்களுக்கு அதிகாரம் இல்லை."
      },
      "one_line_revision": "Art 33 Armed Forces FR restriction = Exclusively by Parliament law.",
      "type": "trap"
    },
    {
      "id": "RC_FR3_010",
      "title": {
        "en": "Minerva Mills FR vs DPSP",
        "ta": "மினர்வா மில்ஸ் அடிப்படை உரிமைகள் vs DPSP"
      },
      "front": {
        "en": "What principle did Minerva Mills case (1980) lay down regarding FRs and DPSPs?",
        "ta": "மினர்வா மில்ஸ் வழக்கில் (1980) அடிப்படை உரிமைகள் மற்றும் DPSP தொடர்பாக என்ன கோட்பாடு வழங்கப்பட்டது?"
      },
      "back": {
        "en": "The Constitution is founded on the HARMONIOUS BALANCE between Part III (FRs) and Part IV (DPSPs); this balance is part of the Basic Structure.",
        "ta": "பகுதி III (அடிப்படை உரிமைகள்) மற்றும் பகுதி IV (DPSP) இடையேயான நல்லிணக்கச் சமநிலையின் மீதே அரசியலமைப்பு நிறுவப்பட்டுள்ளது; இச்சமநிலை அடிப்படை கட்டமைப்பாகும்."
      },
      "one_line_revision": "Minerva Mills 1980 = Harmonious balance between FR & DPSP is Basic Structure.",
      "type": "concept"
    }
  ]
}

target_file = "data/notes/polity/fundamental_rights_part_3.json"
os.makedirs(os.path.dirname(target_file), exist_ok=True)

with open(target_file, "w", encoding="utf-8") as f:
    json.dump(notes_data, f, ensure_ascii=False, indent=2)

print(f"Successfully generated '{target_file}' with complete bilingual notes!")
