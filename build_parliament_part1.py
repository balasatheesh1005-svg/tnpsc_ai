# -*- coding: utf-8 -*-
"""
Builder Script for Parliament of India Notes — Part 1
Subject: Indian Polity
Topic: Parliament of India – Part 1 (Foundation + Houses)
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("==================================================")
print("BUILDING PARLIAMENT NOTES — PART 1")
print("==================================================")

part1_data = {
  "meta": {
    "topic_id": "polity_parliament_part_1",
    "repository_id": "polity_parliament",
    "display_title": "Parliament of India – Part 1",
    "part": 1,
    "total_parts": 3,
    "subject": "polity",
    "chapter": "Parliament of India",
    "language": "English + Tamil"
  },
  "metadata": {
    "topic_id": "polity_parliament_part_1",
    "repository_id": "polity_parliament",
    "display_title": "Parliament of India – Part 1",
    "part": 1,
    "total_parts": 3,
    "subject": "polity",
    "chapter": "Parliament of India",
    "language": "English + Tamil"
  },
  "keywords": [
    "Parliament of India",
    "Article 79",
    "Article 80",
    "Article 81",
    "Article 83",
    "Article 84",
    "Article 85",
    "Article 89",
    "Article 93",
    "Article 99",
    "Article 101",
    "Article 102",
    "Lok Sabha",
    "Rajya Sabha",
    "President of India",
    "Council of States",
    "House of the People",
    "Adjournment",
    "Prorogation",
    "Dissolution",
    "Provisional Representation",
    "Single Transferable Vote",
    "TNPSC Polity Notes"
  ],
  "learning_outcomes": {
    "Understand": {
      "en": [
        "Master the constitutional basis of Parliament under Article 79 comprising President, Rajya Sabha, and Lok Sabha.",
        "Analyze Rajya Sabha composition (Art 80), permanent nature, 6-year member term (RPA 1951), 1/3rd retirement every 2 years, and Vice-President as ex-officio Chairman (Art 89).",
        "Understand Lok Sabha composition (Art 81), direct election via universal adult franchise, 5-year normal term (Art 83), earlier dissolution, and Speaker/Deputy Speaker (Art 93).",
        "Learn qualifications (Art 84 - 25 yrs LS / 30 yrs RS), disqualifications (Art 102), oath (Art 99), and vacation of seats (Art 101 - 60 days absence rule).",
        "Distinguish clearly between Adjournment, Prorogation, and Dissolution of Houses under Article 85."
      ],
      "ta": [
        "உறுப்பு 79-ன் கீழ் குடியரசுத் தலைவர், மாநிலங்களவை மற்றும் மக்களவை உள்ளடக்கிய நாடாளுமன்றத்தின் அரசியலமைப்பு அமைப்பில் தேர்ச்சி பெறுதல்.",
        "மாநிலங்களவை அமைப்பு (விதி 80), நிரந்தர அவைத் தன்மை, 6 ஆண்டு உறுப்பினர் பதவிக்காலம் (RPA 1951), 2 ஆண்டிற்கு ஒருமுறை 1/3 பங்கு ஓய்வு மற்றும் துணை குடியரசுத் தலைவர் பதவிவழித் தலைவராகச் செயல்படுதல் (விதி 89) ஆகியவற்றைப் புரிந்துகொள்ளுதல்.",
        "மக்களவை அமைப்பு (விதி 81), நேரடித் தேர்தல், 5 ஆண்டு சாதாரண பதவிக்காலம் (விதி 83), அவைக் கலைப்பு மற்றும் சபாநாயகர்/துணை சபாநாயகர் (விதி 93) ஆகியவற்றை அறிந்துகொள்ளுதல்.",
        "தகுதிகள் (விதி 84 - 25 வயது மக்களவை / 30 வயது மாநிலங்களவை), தகுதியிழப்புகள் (விதி 102), பதவிப் பிரமாணம் (விதி 99) மற்றும் இடங்கள் காலியாதல் (விதி 101 - 60 நாட்கள் வராமை விதி) ஆகியவற்றைக் கற்றல்.",
        "உறுப்பு 85-ன் கீழ் அவ ஒத்திவைப்பு (Adjournment), கூட்டத்தொடர் ஒத்திவைப்பு (Prorogation) மற்றும் அவைக் கலைப்பு (Dissolution) இடையிலான வேறுபாடுகளைத் தெளிவாகப் பகுப்பாய்வு செய்தல்."
      ]
    }
  },
  "subject": "polity",
  "topic": "Parliament of India",
  "language": "English + Tamil",
  "ui_type": "standard_notes",
  "sections": [
    {
      "id": "sec_constitutional_basis",
      "title_en": "1. Constitutional Basis & Composition of Parliament (Article 79)",
      "title_ta": "1. அரசியலமைப்பு அடிப்படை & நாடாளுமன்ற அமைப்பு (உறுப்பு 79)",
      "type": "standard_topic"
    },
    {
      "id": "sec_rajya_sabha",
      "title_en": "2. Rajya Sabha — Council of States (Articles 80 & 89)",
      "title_ta": "2. மாநிலங்களவை — மேலவை (உறுப்புகள் 80 & 89)",
      "type": "standard_topic"
    },
    {
      "id": "sec_lok_sabha",
      "title_en": "3. Lok Sabha — House of the People (Articles 81 & 93)",
      "title_ta": "3. மக்களவை — கீழவை (உறுப்புகள் 81 & 93)",
      "type": "standard_topic"
    },
    {
      "id": "sec_membership_rules",
      "title_en": "4. Membership Qualifications, Disqualifications & Seat Vacation (Articles 84, 99, 101, 102)",
      "title_ta": "4. உறுப்பினர் தகுதிகள், தகுதியிழப்புகள் & இடங்கள் காலியாதல் (உறுப்புகள் 84, 99, 101, 102)",
      "type": "standard_topic"
    },
    {
      "id": "sec_sessions_mechanics",
      "title_en": "5. Sessions of Parliament — Summoning, Prorogation & Dissolution (Article 85)",
      "title_ta": "5. நாடாளுமன்றக் கூட்டத்தொடர்கள் — கூட்டுதல், ஒத்திவைப்பு & கலைப்பு (உறுப்பு 85)",
      "type": "standard_topic"
    },
    {
      "id": "sec_articles_cheat_sheet",
      "title_en": "6. Parliamentary Articles Map (Articles 79 to 104)",
      "title_ta": "6. நாடாளுமன்ற விதிகள் நினைவுக் குறிப்பு (உறுப்புகள் 79 முதல் 104)",
      "type": "standard_topic"
    },
    {
      "id": "comparison_tables",
      "title_en": "7. Mandatory Comparison Tables (Houses, Sessions & Membership)",
      "title_ta": "7. கட்டாய ஒப்பீட்டு அட்டவணைகள் (அவைகள், கூட்டத்தொடர்கள் & உறுப்பினர்கள்)",
      "type": "comparison"
    },
    {
      "id": "mind_map",
      "title_en": "8. Mind Map & TNPSC Trap Points",
      "title_ta": "8. மன வரைபடம் & டிஎன்பிஎஸ்சி பொறிப் புள்ளிகள்",
      "type": "mind_map"
    }
  ],
  "content": {
    "definition": {
      "en": "The Parliament of India is the supreme legislative body of the Republic of India, established under Part V (Articles 79 to 122) of the Constitution, functioning on the Westminster bicameral parliamentary system.",
      "ta": "இந்திய நாடாளுமன்றம் என்பது இந்தியக் குடியரசின் மிகயுயர்ந்த சட்டமன்ற அமைப்பாகும். இது அரசியலமைப்பின் பகுதி V (உறுப்புகள் 79 முதல் 122 வரை) கீழ் நிறுவப்பட்டு, வெஸ்ட்மின்ஸ்டர் ஈரவை நாடாளுமன்ற முறையின் கீழ் இயங்குகிறது."
    },
    "introduction": {
      "en": "Article 79 explicitly defines Parliament as consisting of the President and two Houses: Rajya Sabha (Council of States) and Lok Sabha (House of the People). Though the President is not a member of either House, he is an integral part of Parliament.",
      "ta": "உறுப்பு 79 நாடாளுமன்றம் என்பது குடியரசுத் தலைவர் மற்றும் இரண்டு அவைகளான மாநிலங்களவை (மேலவை) மற்றும் மக்களவை (கீழவை) உள்ளடக்கியது எனத் தெளிவாக வரையறுக்கிறது. குடியரசுத் தலைவர் எந்த அவையிலும் உறுப்பினராக இல்லாவிட்டாலும், அவர் நாடாளுமன்றத்தின் பிரிக்க முடியாத அங்கமாவார்."
    },
    "sec_constitutional_basis": [
      {
        "title_en": "Article 79 — Composition of Parliament",
        "title_ta": "உறுப்பு 79 — நாடாளுமன்ற அமைப்பு",
        "points": {
          "en": [
            "Article 79 mandates that there shall be a Parliament for the Union consisting of the President and two Houses: Council of States (Rajya Sabha) and House of the People (Lok Sabha).",
            "CRITICAL CONSTITUTIONAL POINT: Parliament DOES NOT consist only of Lok Sabha and Rajya Sabha. The President is constitutionally an integral component of Parliament.",
            "Why President is part of Parliament: A Bill passed by both Houses cannot become law without President's assent (Art 111). President summons, prorogues both Houses, dissolves Lok Sabha, addresses joint sittings, and issues Ordinances (Art 123) when Parliament is not in session.",
            "Bicameralism Adopted: Adopted from the UK Westminster system, replacing the Central Legislative Assembly under the Government of India Act 1935."
          ],
          "ta": [
            "உறுப்பு 79 ஒன்றியத்திற்கு ஒரு நாடாளுமன்றம் இருக்கும் என்றும், அது குடியரசுத் தலைவர் மற்றும் இரு அவைகளான மாநிலங்களவை மற்றும் மக்களவையை உள்ளடக்கியது என்றும் கூறுகிறது.",
            "முக்கிய அரசியலமைப்பு புள்ளி: நாடாளுமன்றம் என்பது மக்களவை மற்றும் மாநிலங்களவை மட்டுமே கொண்டது அல்ல. குடியரசுத் தலைவர் நாடாளுமன்றத்தின் பிரிக்க முடியாத அங்கமாவார்.",
            "ஏன் குடியரசுத் தலைவர் நாடாளுமன்றத்தின் அங்கமாகிறார்: இரு அவைகளும் நிறைவேற்றும் மசோதா குடியரசுத் தலைவரின் ஒப்புதல் (விதி 111) இன்றி சட்டமாக முடியாது. மேலும் அவைகளைக் கூட்டுவது, ஒத்திவைப்பது, மக்களவையைக் கலைப்பது, கூட்டுத் தொடரில் உரையாற்றுவது மற்றும் அவசரச் சட்டம் (விதி 123) பிறப்பிப்பது குடியரசுத் தலைவரேயாவார்.",
            "ஈரவை முறை ஏற்றுக்கொள்வது: 1935-ஆம் ஆண்டு இந்திய அரசுச் சட்டத்தின் கீழ் இருந்த மத்திய சட்டமன்றத்திற்குப் பதிலாக, இங்கிலாந்தின் வெஸ்ட்மின்ஸ்டர் முறையைப் பின்பற்றி ஈரவை முறை ஏற்றுக்கொள்ளப்பட்டது."
          ]
        }
      }
    ],
    "sec_rajya_sabha": [
      {
        "title_en": "Article 80 — Composition & Nature of Rajya Sabha",
        "title_ta": "உறுப்பு 80 — மாநிலங்களவை அமைப்பு & தன்மை",
        "points": {
          "en": [
            "Maximum Strength (Art 80): 250 Members (238 elected from States/UTs + 12 Nominated by President).",
            "Current Strength: 245 Members (233 elected + 12 nominated).",
            "Nominated Members (Art 80(3)): 12 members nominated by President having special knowledge/practical experience in 4 fields: Literature, Science, Art, and Social Service. (Note: 'Co-operative Movement' is NOT in Rajya Sabha nomination!).",
            "Representation of States: Fourth Schedule allocates Rajya Sabha seats to States and Union Territories based on population. (UP has highest with 31 seats; Tamil Nadu has 18 seats).",
            "Election Method: Indirect election by elected members of State Legislative Assemblies (MLAs) using System of Proportional Representation by means of Single Transferable Vote (STV).",
            "UT Representation: Only 3 UTs (Delhi - 3, Puducherry - 1, Jammu & Kashmir - 4) have Rajya Sabha representation because they have Legislative Assemblies.",
            "Permanent House (Art 83(1)): Rajya Sabha is a continuing chamber and is NOT subject to dissolution.",
            "Member Tenure: 6 Years term. One-third of its members retire every two years. (Note: 6-year term is NOT explicitly written in Constitution, but fixed by Representation of the People Act 1951!).",
            "Presiding Officers (Art 89): Vice-President of India is ex-officio Chairman of Rajya Sabha. Deputy Chairman is elected from amongst Rajya Sabha members."
          ],
          "ta": [
            "அதிகபட்ச உறுப்பினர் எண்ணிக்கை (விதி 80): 250 உறுப்பினர்கள் (238 மாநிலங்கள்/யூனியன் பிரதேசங்களால் தேர்ந்தெடுக்கப்படுபவர்கள் + 12 குடியரசுத் தலைவரால் நியமிக்கப்படுபவர்கள்).",
            "தற்போதைய எண்ணிக்கை: 245 உறுப்பினர்கள் (233 தேர்ந்தெடுக்கப்பட்டவர்கள் + 12 நியமிக்கப்பட்டவர்கள்).",
            "நியமன உறுப்பினர்கள் (விதி 80(3)): இலக்கியம், அறிவியல், கலை, சமூக சேவை ஆகிய 4 துறைகளில் சிறப்பு அறிவுடைய 12 உறுப்பினர்களைக் குடியரசுத் தலைவர் நியமிக்கிறார். (குறிப்பு: 'கூட்டுறவு இயக்கம்' மாநிலங்களவை நியமனத்தில் இல்லை!).",
            "மாநிலங்களின் பிரதிநிதித்துவம்: நான்காவது அட்டவணை மக்கள் தொகை அடிப்படையில் மாநிலங்களுக்கும் யூனியன் பிரதேசங்களுக்கும் இடங்களைப் பங்கீடு செய்கிறது. (உத்தரப் பிரதேசம் அதிகபட்சமாக 31 இடங்கள்; தமிழ்நாடு 18 இடங்கள்).",
            "தேர்தல் முறை: மாநில சட்டப்பேரவை தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்களால் (MLAs) விகிதாசாரப் பிரதிநிதித்துவ ஒற்றை மாற்று வாக்கு முறை மூலம் மறைமுகத் தேர்தல்.",
            "யூனியன் பிரதேசப் பிரதிநிதித்துவம்: சட்டமன்றம் கொண்ட டெல்லி (3), புதுச்சேரி (1), ஜம்மு & காஷ்மீர் (4) ஆகிய 3 யூனியன் பிரதேசங்களுக்கு மட்டுமே மாநிலங்களவையில் பிரதிநிதித்துவம் உண்டு.",
            "நிரந்தர அவை (விதி 83(1)): மாநிலங்களவை ஒரு நிலையான அவையாகும்; இது கலைக்கப்பட முடியாதது.",
            "உறுப்பினர் பதவிக்காலம்: 6 ஆண்டுகள். மூன்றில் ஒரு பங்கு (1/3) உறுப்பினர்கள் இரண்டு ஆண்டிற்கு ஒருமுறை ஓய்வு பெறுகின்றனர். (குறிப்பு: 6 ஆண்டு பதவிக்காலம் அரசியலமைப்பில் நேரடியாகக் குறிப்பிடப்படவில்லை, 1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தால் தீர்மானிக்கப்பட்டது!).",
            "தலைவர்கள் (விதி 89): இந்தியத் துணைக் குடியரசுத் தலைவர் மாநிலங்களவையின் பதவிவழித் தலைவராவார். துணைத் தலைவர் மாநிலங்களவை உறுப்பினர்களிலிருந்து தேர்ந்தெடுக்கப்படுகிறார்."
          ]
        }
      }
    ],
    "sec_lok_sabha": [
      {
        "title_en": "Article 81 — Composition & Nature of Lok Sabha",
        "title_ta": "உறுப்பு 81 — மக்களவை அமைப்பு & தன்மை",
        "points": {
          "en": [
            "Maximum Strength (Art 81): 550 Members (530 from States + 20 from UTs). Note: 104th Constitutional Amendment Act (2019) discontinued the nomination of 2 Anglo-Indians.",
            "Current Strength: 543 Members (All directly elected by the people). (Tamil Nadu has 39 Lok Sabha seats).",
            "Election Method: Direct election based on Universal Adult Suffrage (Art 326) using First-Past-The-Post (FPTP) system.",
            "Voting Age: Reduced from 21 years to 18 years by the 61st Constitutional Amendment Act 1988 (enforced 1989).",
            "Normal Duration (Art 83(2)): 5 years from the date appointed for its first meeting.",
            "Dissolution: Subject to earlier dissolution by President on CM/PM advice.",
            "Extension during Emergency: Term can be extended by Parliament by law for 1 year at a time during National Emergency (Art 352), but cannot extend beyond 6 months after Emergency ceases to operate. (Happened during 5th Lok Sabha 1971-1977).",
            "Presiding Officers (Art 93): Speaker and Deputy Speaker are elected by Lok Sabha from amongst its members."
          ],
          "ta": [
            "அதிகபட்ச உறுப்பினர் எண்ணிக்கை (விதி 81): 550 உறுப்பினர்கள் (530 மாநிலங்களிலிருந்து + 20 யூனியன் பிரதேசங்களிலிருந்து). குறிப்பு: 104-வது அரசியலமைப்புச் சட்டத்திருத்தம் (2019) 2 ஆங்கிலோ-இந்தியர் நியமனத்தை ரத்து செய்தது.",
            "தற்போதைய எண்ணிக்கை: 543 உறுப்பினர்கள் (அனைவரும் மக்களால் நேரடியாகத் தேர்ந்தெடுக்கப்படுபவர்கள்). (தமிழ்நாட்டிற்கு 39 மக்களவை இடங்கள்).",
            "தேர்தல் முறை: வயது வந்தோர் வாக்குரிமை (விதி 326) அடிப்படையில் முதன்மையாக வாக்கு பெற்றவர் வெற்றி (First-Past-The-Post) முறையில் நேரடித் தேர்தல்.",
            "வாக்குரிமை வயது: 1988-ஆம் ஆண்டின் 61-வது அரசியலமைப்புச் சட்டத்திருத்தத்தின் மூலம் வாக்குரிமை வயது 21-லிருந்து 18 ஆகக் குறைக்கப்பட்டது.",
            "சாதாரண பதவிக்காலம் (விதி 83(2)): முதல் கூட்டத் தேதியிலிருந்து 5 ஆண்டுகள்.",
            "அவைக் கலைப்பு: பிரதமர்/அமைச்சரவை ஆலோசனையின் பேரில் குடியரசுத் தலைவரால் 5 ஆண்டுகளுக்கு முன்பே கலைக்கப்படலாம்.",
            "அவசரநிலையின் போது நீட்டிப்பு: தேசிய அவசரநிலையின் போது (விதி 352) நாடாளுமன்றச் சட்டத்தின் மூலம் ஒரு முறைக்கு 1 ஆண்டு வரை பதவிக்காலத்தை நீட்டிக்கலாம்; ஆனால் அவசரநிலை முடிந்த பின் 6 மாதங்களுக்கு மேல் நீடிக்கக்கூடாது. (5-வது மக்களவையின் போது 1971-1977 இது நிகழ்ந்தது).",
            "தலைவர்கள் (விதி 93): சபாநாயகர் மற்றும் துணை சபாநாயகர் மக்களவை உறுப்பினர்களிலிருந்து உறுப்பினர்களால் தேர்ந்தெடுக்கப்படுகின்றனர்."
          ]
        }
      }
    ],
    "sec_membership_rules": [
      {
        "title_en": "Qualifications, Disqualifications & Seat Vacation Rules",
        "title_ta": "உறுப்பினர் தகுதிகள், தகுதியிழப்புகள் & இடங்கள் காலியாதல் விதிகள்",
        "points": {
          "en": [
            "Article 84 Qualifications:",
            "  1. Must be a Citizen of India.",
            "  2. Oath or Affirmation before person authorized by Election Commission (3rd Schedule format).",
            "  3. Minimum Age: 25 YEARS for Lok Sabha; 30 YEARS for Rajya Sabha.",
            "  4. Statutory Qualifications under Representation of People Act 1951 (e.g. Registered Elector).",
            "Article 102 Disqualifications:",
            "  • Holding Office of Profit under Union or State Government (except Ministers or exempted offices).",
            "  • Unsound mind declared by competent court.",
            "  • Undischarged insolvent.",
            "  • Not a citizen of India / Voluntary acquisition of foreign citizenship.",
            "  • Disqualified under Tenth Schedule (Anti-Defection Law).",
            "Decision on Disqualification (Art 103): Question of disqualification under Art 102 is decided by PRESIDENT on the binding opinion of ELECTION COMMISSION OF INDIA (Except 10th Schedule anti-defection, which is decided by Speaker/Chairman).",
            "Oath of Members (Art 99): Every member must make and subscribe an oath before President or person appointed by him (Pro-tem Speaker) before taking seat.",
            "Article 101 Vacation of Seats:",
            "  1. Double Membership: Cannot be a member of both Houses or Parliament and State Legislature simultaneously.",
            "  2. Resignation: Member may resign by writing to Speaker (LS) or Chairman (RS).",
            "  3. Absenteeism 60-Day Rule: House may declare seat vacant if a member is absent from all meetings for 60 CONSECUTIVE DAYS without permission (excluding period when House is prorogued or adjourned for > 4 consecutive days)."
          ],
          "ta": [
            "உறுப்பு 84 தகுதிகள்:",
            "  1. இந்தியக் குடிமகனாக இருக்க வேண்டும்.",
            "  2. தேர்தல் ஆணையத்தால் அதிகாரமளிக்கப்பட்ட நபர் முன் பதவிப் பிரமாணம் (3-வது அட்டவணை வடிவம்).",
            "  3. குறைந்தபட்ச வயது: மக்களவைக்கு 25 வயது; மாநிலங்களவைக்கு 30 வயது.",
            "  4. 1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் கீழ் உள்ள சட்டப்பூர்வ தகுதிகள் (எ.கா. வாக்காளர் பட்டியலில் பெயர் இருத்தல்).",
            "உறுப்பு 102 தகுதியிழப்புகள்:",
            "  • மத்திய/மாநில அரசின் கீழ் ஆதாயம் தரும் பதவி வகித்தல் (அமைச்சர்கள் தவிர).",
            "  • நீதிமன்றத்தால் மனநிலை சரியில்லாதவர் என அறிவிக்கப்படுதல்.",
            "  • தீர்க்கப்படாத கடனாளி (வங்கி நொடிப்பு).",
            "  • இந்தியக் குடிமகனாக இல்லாதிருத்தல் / வெளிநாட்டு குடியுரிமையைத் தானாகப் பெறுதல்.",
            "  • பத்தாவது அட்டவணையின் கீழ் தகுதியிழப்பு (கட்சித் தாவல் தடைச் சட்டம்).",
            "தகுதியிழப்பு குறித்த முடிவு (விதி 103): விதி 102-ன் கீழ் தகுதியிழப்பு குறித்த கேள்வியை இந்தியத் தேர்தல் ஆணையத்தின் கட்டாய ஆலோசனையின் பேரில் குடியரசுத் தலைவர் தீர்மானிக்கிறார் (கட்சித் தாவல் தகுதியிழப்பு தவிர, அதை சபாநாயகர்/தலைவர் தீர்மானிக்கிறார்).",
            "உறுப்பினர்கள் பதவிப் பிரமாணம் (விதி 99): ஒவ்வொரு உறுப்பினரும் பதவியேற்கும் முன் குடியரசுத் தலைவர் அல்லது அவரால் நியமிக்கப்பட்ட நபர் (தற்காலிக சபாநாயகர்) முன் பிரமாணம் செய்ய வேண்டும்.",
            "உறுப்பு 101 இடங்கள் காலியாதல்:",
            "  1. இரட்டை உறுப்பினர்: ஒரே நேரத்தில் இரு அவைகளிலும் அல்லது நாடாளுமன்றம் மற்றும் மாநில சட்டமன்றம் இரண்டிலும் உறுப்பினராக இருக்க முடியாது.",
            "  2. ராஜினாமா: சபாநாயகர் (LS) அல்லது தலைவர் (RS) அவர்களிடம் எழுத்துப்பூர்வமாகக் கடிதம் அளித்து ராஜினாமா செய்யலாம்.",
            "  3. 60 நாட்கள் வராமை விதி: அனுமதி பெறாமல் தொடர்ச்சியாக 60 நாட்கள் அவைக் கூட்டங்களில் பங்கேற்காத உறுப்பினரின் இடத்தை அவை காலியாக அறிவிக்கலாம் (கூட்டத்தொடர் ஒத்திவைக்கப்பட்ட அல்லது 4 நாட்களுக்கு மேல் ஒத்திவைக்கப்பட்ட காலம் சேர்க்கப்படாது)."
          ]
        }
      }
    ],
    "sec_sessions_mechanics": [
      {
        "title_en": "Article 85 — Summoning, Prorogation & Dissolution Mechanics",
        "title_ta": "உறுப்பு 85 — கூட்டுதல், ஒத்திவைப்பு & அவைக் கலைப்பு முறைகள்",
        "points": {
          "en": [
            "Summoning (Art 85(1)): President summons each House of Parliament to meet. Max gap between last sitting of one session and first sitting of next session MUST NOT EXCEED 6 MONTHS. (Must meet at least twice a year).",
            "Three Conventional Sessions: 1. Budget Session (Feb-May, longest); 2. Monsoon Session (July-Sept); 3. Winter Session (Nov-Dec, shortest).",
            "Adjournment: Suspends the work in a sitting for a specified time (hours, days, or weeks). Done by PRESIDING OFFICER (Speaker/Chairman). Does not affect pending bills or business.",
            "Adjournment Sine Die: Terminating a sitting of Parliament without naming a day for reassembly. Done by PRESIDING OFFICER.",
            "Prorogation (Art 85(2)(a)): Terminates NOT ONLY a sitting but a SESSION of the House. Done by PRESIDENT OF INDIA by notification. Does not lapse pending Bills (Art 107(3)).",
            "Dissolution (Art 85(2)(b)): Ends the very life of the existing House (ONLY Lok Sabha is dissolved; Rajya Sabha is permanent). Done by PRESIDENT on advice of Cabinet.",
            "Lapsing of Bills on Dissolution (Art 107):",
            "  1. Bill pending in Lok Sabha LAPSES (whether originating in LS or transmitted to it).",
            "  2. Bill passed by LS but pending in RS LAPSES.",
            "  3. Bill pending in RS but NOT passed by LS DOES NOT LAPSE.",
            "  4. Bill passed by both Houses but pending President's assent DOES NOT LAPSE.",
            "  5. Bill returned by President for reconsideration DOES NOT LAPSE.",
            "  6. Bill where Joint Sitting has been notified by President before dissolution DOES NOT LAPSE."
          ],
          "ta": [
            "அவைகளைக் கூட்டுதல் (விதி 85(1)): நாடாளுமன்றத்தின் ஒவ்வொரு அவையையும் குடியரசுத் தலைவர் கூட்டுகிறார். இரு கூட்டத்தொடர்களுக்கு இடையே உள்ள அதிகபட்ச இடைவெளி 6 மாதங்களுக்கு மிகக்கூடாது. (ஆண்டிற்குக் குறைந்தபட்சம் இருமுறை கூட வேண்டும்).",
            "மூன்று பாரம்பரிய கூட்டத்தொடர்கள்: 1. பட்ஜெட் கூட்டத்தொடர் (பிப்ரவரி-மே, மிக நீண்டது); 2. பருவமழைக் கூட்டத்தொடர் (ஜூலை-செப்டம்பர்); 3. குளிர்காலக் கூட்டத்தொடர் (நவம்பர்-டிசம்பர், மிகக் குறுகியது).",
            "அவை ஒத்திவைப்பு (Adjournment): குறிப்பிட்ட நேரத்திற்கு (மணிநேரம், நாட்கள்) அவைப் பணியை நிறுத்தி வைத்தல். இதைச் செய்பவர் அவைத் தலைவர் (சபாநாயகர்/தலைவர்). இது நிலுவையில் உள்ள மசோதாக்களைப் பாதிக்காது.",
            "தேதி குறிப்பிடாமல் ஒத்திவைப்பு (Adjournment Sine Die): மீண்டும் கூடும் தேதியைக் குறிப்பிடாமல் அவைக் கூட்டத்தை ஒத்திவைத்தல். அவைத் தலைவரால் செய்யப்படுகிறது.",
            "கூட்டத்தொடர் ஒத்திவைப்பு (Prorogation - விதி 85(2)(a)): அவைக் கூட்டத்தை மட்டுமல்லாமல் கூட்டத்தொடரையே முடிவுக்குக் கொண்டு வருதல். அறிவிக்கை மூலம் இந்தியக் குடியரசுத் தலைவரால் செய்யப்படுகிறது. இது நிலுவை மசோதாக்களை ரத்து செய்யாது (விதி 107(3)).",
            "அவைக் கலைப்பு (Dissolution - விதி 85(2)(b)): அவையின் ஆயுட்காலத்தையே முடிவுக்குக் கொண்டு வருதல் (மக்களவை மட்டுமே கலைக்கப்படும்; மாநிலங்களவை நிரந்தரமானது). அமைச்சரவை ஆலோசனையின் பேரில் குடியரசுத் தலைவரால் செய்யப்படுகிறது.",
            "அவைக் கலைப்பின் போது மசோதாக்கள் காலாவதியாகும் விதிகள் (விதி 107):",
            "  1. மக்களவையில் நிலுவையில் உள்ள மசோதா காலாவதியாகும் (LS-ல் உருவானதோ அல்லது RS-லிருந்து வந்ததோ).",
            "  2. LS நிறைவேற்றி RS-ல் நிலுவையில் உள்ள மசோதா காலாவதியாகும்.",
            "  3. RS-ல் நிலுவையில் இருந்து LS நிறைவேற்றாத மசோதா காலாவதியாகாது.",
            "  4. இரு அவைகளும் நிறைவேற்றி குடியரசுத் தலைவர் ஒப்புதலுக்கு நிலுவையில் உள்ள மசோதா காலாவதியாகாது.",
            "  5. குடியரசுத் தலைவரால் மறுபரிசீலனைக்குத் திருப்பப்பட்ட மசோதா காலாவதியாகாது.",
            "  6. அவைக் கலைப்புக்கு முன் கூட்டுத் தொடருக்குக் குடியரசுத் தலைவரால் அறிவிக்கப்பட்ட மசோதா காலாவதியாகாது."
          ]
        }
      }
    ],
    "sec_articles_cheat_sheet": [
      {
        "title_en": "Parliament Cheat-Sheet (Articles 79 to 104)",
        "title_ta": "நாடாளுமன்ற விதிகள் நினைவுக் குறிப்பு (உறுப்புகள் 79 முதல் 104)",
        "points": {
          "en": [
            "Article 79: Constitution of Parliament (President + Rajya Sabha + Lok Sabha)",
            "Article 80: Composition of Rajya Sabha (250 Max; 12 Nominated; 4th Schedule)",
            "Article 81: Composition of Lok Sabha (550 Max; Direct Election; FPTP)",
            "Article 82: Readjustment after each census (Delimitation Commission)",
            "Article 83: Duration of Houses of Parliament (RS Permanent; LS 5 Years)",
            "Article 84: Qualification for membership of Parliament (25 yrs LS / 30 yrs RS)",
            "Article 85: Sessions, Summoning, Prorogation, and Dissolution of Parliament",
            "Article 86: Right of President to address and send messages to Houses",
            "Article 87: Special Address by President at commencement of 1st Session",
            "Article 88: Rights of Ministers and Attorney General as respects Houses",
            "Article 89: Chairman and Deputy Chairman of Council of States (RS)",
            "Article 93: Speaker and Deputy Speaker of House of the People (LS)",
            "Article 99: Oath or Affirmation by members of Parliament",
            "Article 100: Voting in Houses, power of Houses to act notwithstanding vacancies and Quorum (1/10th)",
            "Article 101: Vacation of Seats (60 Days absence rule)",
            "Article 102: Disqualifications for membership (Office of profit, Insolvency, etc.)",
            "Article 103: Decision on questions as to disqualifications of members (President + ECI)",
            "Article 104: Penalty for sitting and voting before making oath or when not qualified"
          ],
          "ta": [
            "உறுப்பு 79: நாடாளுமன்ற அமைப்பு (குடியரசுத் தலைவர் + மாநிலங்களவை + மக்களவை)",
            "உறுப்பு 80: மாநிலங்களவை அமைப்பு (அதிகபட்சம் 250; 12 நியமனம்; 4-வது அட்டவணை)",
            "உறுப்பு 81: மக்களவை அமைப்பு (அதிகபட்சம் 550; நேரடித் தேர்தல்; FPTP முறை)",
            "உறுப்பு 82: ஒவ்வொரு மக்கள் தொகை கணக்கெடுப்பிற்குப் பின் மறுசீரமைப்பு (எல்லை மறுவரையறை)",
            "உறுப்பு 83: நாடாளுமன்ற அவைகளின் பதவிக்காலம் (RS நிரந்தரம்; LS 5 ஆண்டுகள்)",
            "உறுப்பு 84: நாடாளுமன்ற உறுப்பினர் தகுதிகள் (25 வயது LS / 30 வயது RS)",
            "உறுப்பு 85: கூட்டத்தொடர்கள், அவைகளைக் கூட்டுதல், ஒத்திவைப்பு மற்றும் கலைப்பு",
            "உறுப்பு 86: அவைகளில் உரையாற்றவும் செய்திகள் அனுப்பவும் குடியரசுத் தலைவரின் உரிமை",
            "உறுப்பு 87: முதல் கூட்டத்தொடரின் தொடக்கத்தில் குடியரசுத் தலைவரின் சிறப்பு உரை",
            "உறுப்பு 88: அவைகள் தொடர்பாக அமைச்சர்கள் மற்றும் அட்வகேட் ஜெனரலின் உரிமைகள்",
            "உறுப்பு 89: மாநிலங்களவைத் தலைவர் மற்றும் துணைத் தலைவர் (RS)",
            "உறுப்பு 93: மக்களவைச் சபாநாயகர் மற்றும் துணை சபாநாயகர் (LS)",
            "உறுப்பு 99: நாடாளுமன்ற உறுப்பினர்களின் பதவிப் பிரமாணம்",
            "உறுப்பு 100: அவைகளில் வாக்களிப்பு மற்றும் குறைந்தபட்ச உறுப்பினர் வரம்பு / குவோரம் (1/10 பங்கு)",
            "உறுப்பு 101: இடங்கள் காலியாதல் (60 நாட்கள் வராமை விதி)",
            "உறுப்பு 102: உறுப்பினர் தகுதியிழப்புகள் (ஆதாயம் தரும் பதவி, வங்கி நொடிப்பு போன்றவை)",
            "உறுப்பு 103: உறுப்பினர்களின் தகுதியிழப்பு குறித்த முடிவு (குடியரசுத் தலைவர் + ECI)",
            "உறுப்பு 104: பிரமாணம் செய்யாமல் அல்லது தகுதியின்றி அமர்ந்து வாக்களிப்பதற்கான அபராதம்"
          ]
        }
      }
    ],
    "revision_cards": [
      {
        "id": "parl_p1_c1",
        "front_en": "Which Article provides for the Constitution of Parliament in India?",
        "front_ta": "இந்தியாவில் நாடாளுமன்ற அமைப்பைக் குறிப்பிடும் அரசியலமைப்பு உறுப்பு எது?",
        "back_en": "Article 79. Parliament consists of President, Rajya Sabha (Council of States), and Lok Sabha (House of the People).",
        "back_ta": "உறுப்பு 79. நாடாளுமன்றம் என்பது குடியரசுத் தலைவர், மாநிலங்களவை மற்றும் மக்களவை உள்ளடக்கியது."
      },
      {
        "id": "parl_p1_c2",
        "front_en": "Is the President of India a member of either House of Parliament?",
        "front_ta": "இந்தியக் குடியரசுத் தலைவர் நாடாளுமன்றத்தின் ஏதேனும் ஒரு அவையில் உறுப்பினரா?",
        "back_en": "NO. The President is NOT a member of either House, but is constitutionally an integral PART of Parliament.",
        "back_ta": "இல்லை. குடியரசுத் தலைவர் எந்த அவையிலும் உறுப்பினரல்ல, ஆனால் அரசியலமைப்புப்படி நாடாளுமன்றத்தின் பிரிக்க முடியாத அங்கமாவார்."
      },
      {
        "id": "parl_p1_c3",
        "front_en": "What is the maximum strength and nomination quota for Rajya Sabha under Article 80?",
        "front_ta": "உறுப்பு 80-ன் கீழ் மாநிலங்களவையின் அதிகபட்ச உறுப்பினர் எண்ணிக்கையும் நியமன ஒதுக்கீடும் என்ன?",
        "back_en": "Max 250 Members (238 elected from States/UTs + 12 Nominated by President in Art, Lit, Sci, Social Service).",
        "back_ta": "அதிகபட்சம் 250 உறுப்பினர்கள் (238 தேர்ந்தெடுக்கப்படுபவர்கள் + 12 கலை, இலக்கியம், அறிவியல், சமூக சேவையில் குடியரசுத் தலைவரால் நியமிக்கப்படுபவர்கள்)."
      },
      {
        "id": "parl_p1_c4",
        "front_en": "Where is the 6-year tenure of Rajya Sabha members specified?",
        "front_ta": "மாநிலங்களவை உறுப்பினர்களின் 6 ஆண்டு பதவிக்காலம் எதில் குறிப்பிடப்பட்டுள்ளது?",
        "back_en": "In the Representation of the People Act 1951 (NOT explicitly specified in the Constitution!).",
        "back_ta": "1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தில் (அரசியலமைப்பில் நேரடியாகக் குறிப்பிடப்படவில்லை!)."
      },
      {
        "id": "parl_p1_c5",
        "front_en": "What is the minimum age qualification for Lok Sabha and Rajya Sabha membership under Article 84?",
        "front_ta": "உறுப்பு 84-ன் கீழ் மக்களவை மற்றும் மாநிலங்களவை உறுப்பினருக்கான குறைந்தபட்ச வயதுத் தகுதி என்ன?",
        "back_en": "Lok Sabha: 25 Years; Rajya Sabha: 30 Years.",
        "back_ta": "மக்களவை: 25 வயது; மாநிலங்களவை: 30 வயது."
      },
      {
        "id": "parl_p1_c6",
        "front_en": "What Constitutional Amendment reduced the voting age from 21 to 18 years?",
        "front_ta": "வாக்குரிமை வயதை 21-லிருந்து 18 ஆகக் குறைத்த அரசியலமைப்புச் சட்டத்திருத்தம் எது?",
        "back_en": "61st Constitutional Amendment Act 1988 (enforced 1989).",
        "back_ta": "1988-ஆம் ஆண்டின் 61-வது அரசியலமைப்புச் சட்டத்திருத்தம் (1989-ல் நடைமுறை)."
      },
      {
        "id": "parl_p1_c7",
        "front_en": "Who performs Adjournment vs Prorogation vs Dissolution?",
        "front_ta": "அவை ஒத்திவைப்பு, கூட்டத்தொடர் ஒத்திவைப்பு மற்றும் அவைக் கலைப்பைச் செய்பவர்கள் யார்?",
        "back_en": "Adjournment: Presiding Officer (Speaker/Chairman). Prorogation & Dissolution: President of India.",
        "back_ta": "அவை ஒத்திவைப்பு (Adjournment): அவைத் தலைவர் (சபாநாயகர்/தலைவர்). கூட்டத்தொடர் ஒத்திவைப்பு & கலைப்பு: குடியரசுத் தலைவர்."
      },
      {
        "id": "parl_p1_c8",
        "front_en": "Under Article 101, after how many days of unapproved absence can a member's seat be declared vacant?",
        "front_ta": "உறுப்பு 101-ன் கீழ் அனுமதி பெறாமல் எத்தனை நாட்கள் வராவிட்டால் ஒரு உறுப்பினரின் இடம் காலியாக அறிவிக்கப்படும்?",
        "back_en": "60 CONSECUTIVE DAYS (excluding prorogation or adjournment > 4 consecutive days).",
        "back_ta": "தொடர்ச்சியாக 60 நாட்கள் (4 நாட்களுக்கு மேல் ஒத்திவைக்கப்பட்ட காலம் நீங்கலாக)."
      },
      {
        "id": "parl_p1_c9",
        "front_en": "Who decides disqualification of an MP under Article 102 (other than 10th Schedule)?",
        "front_ta": "உறுப்பு 102-ன் கீழ் எம்பி-யின் தகுதியிழப்பைத் தீர்மானிப்பவர் யார் (10-வது அட்டவணை தவிர)?",
        "back_en": "President of India, according to the binding opinion of the Election Commission of India (Art 103).",
        "back_ta": "இந்தியத் தேர்தல் ஆணையத்தின் கட்டாய ஆலோசனையின் பேரில் இந்தியக் குடியரசுத் தலைவர் (விதி 103)."
      },
      {
        "id": "parl_p1_c10",
        "front_en": "What is the maximum gap allowed between two parliamentary sessions under Article 85?",
        "front_ta": "உறுப்பு 85-ன் கீழ் இரு நாடாளுமன்றக் கூட்டத்தொடர்களுக்கு இடையே அனுமதிக்கப்படும் அதிகபட்ச இடைவெளி என்ன?",
        "back_en": "MUST NOT EXCEED 6 MONTHS. (Parliament must meet at least twice a year).",
        "back_ta": "6 மாதங்களுக்கு மிகக்கூடாது. (நாடாளுமன்றம் ஆண்டிற்கு குறைந்தபட்சம் இருமுறை கூட வேண்டும்)."
      }
    ],
    "comparison_tables": [
      {
        "id": "tbl_ls_vs_rs_p1",
        "title_en": "1. Lok Sabha vs Rajya Sabha Comparison",
        "title_ta": "1. மக்களவை vs மாநிலங்களவை ஒப்பீடு",
        "headers_en": ["Dimension / Feature", "Lok Sabha (House of the People)", "Rajya Sabha (Council of States)"],
        "headers_ta": ["அம்சம் / காரணி", "மக்களவை (கீழவை)", "மாநிலங்களவை (மேலவை)"],
        "rows_en": [
          ["Popular Name", "First Chamber / Lower House / Popular House", "Second Chamber / Upper House / House of Elders"],
          ["Constitutional Article", "Article 81", "Article 80"],
          ["Max Strength", "550 Members (530 States + 20 UTs)", "250 Members (238 Elected + 12 Nominated)"],
          ["Election Method", "Direct election by people via Universal Suffrage (FPTP)", "Indirect election by State MLAs via STV"],
          ["Minimum Age", "25 Years (Art 84)", "30 Years (Art 84)"],
          ["House Permanence", "Temporary House; Dissolvable after 5 years or earlier", "Permanent House; NOT subject to dissolution (Art 83(1))"],
          ["Member Tenure", "5 Years (can be extended 1 yr in Emergency)", "6 Years (1/3rd members retire every 2 years - RPA 1951)"],
          ["Presiding Officers", "Speaker and Deputy Speaker (Elected from LS)", "Vice-President (Ex-Officio Chairman) & Deputy Chairman"],
          ["Special Powers", "Exclusive power over Money Bills & No-Confidence Motions", "Special powers under Art 249 (State List) & Art 312 (All India Services)"]
        ],
        "rows_ta": [
          ["பிரபலமான பெயர்", "முதல் அவை / கீழவை / மக்கள் அவை", "இரண்டாம் அவை / மேலவை / மூத்தோர் அவை"],
          ["அரசியலமைப்பு விதி", "உறுப்பு 81", "உறுப்பு 80"],
          ["அதிகபட்ச எண்ணிக்கை", "550 உறுப்பினர்கள் (530 மாநிலங்கள் + 20 UTs)", "250 உறுப்பினர்கள் (238 தேர்வு + 12 நியமனம்)"],
          ["தேர்தல் முறை", "வயது வந்தோர் வாக்குரிமை மூலம் நேரடித் தேர்தல் (FPTP)", "மாநில சட்டமன்ற எம்பிக்களால் மறைமுகத் தேர்தல் (STV)"],
          ["குறைந்தபட்ச வயது", "25 வயது (விதி 84)", "30 வயது (விதி 84)"],
          ["அவை நிலைத்தன்மை", "தற்காலிக அவை; 5 ஆண்டுகள் அல்லது அதற்கு முன் கலைக்கப்படலாம்", "நிரந்தர அவை; கலைக்கப்பட முடியாதது (விதி 83(1))"],
          ["உறுப்பினர் பதவிக்காலம்", "5 ஆண்டுகள் (அவசரநிலையில் 1 ஆண்டு நீட்டிக்கலாம்)", "6 ஆண்டுகள் (1/3 பங்கு உறுப்பினர்கள் 2 ஆண்டிற்கு ஒருமுறை ஓய்வு)"],
          ["தலைவர்கள்", "சபாநாயகர் மற்றும் துணை சபாநாயகர் (LS-லிருந்து தேர்வு)", "துணைக் குடியரசுத் தலைவர் (பதவிவழித் தலைவர்) & துணைத் தலைவர்"],
          ["சிறப்பு அதிகாரங்கள்", "பண மசோதாக்கள் & நம்பிக்கையில்லாத் தீர்மானங்களில் தனி அதிகாரம்", "விதி 249 (மாநிலப் பட்டியல்) & விதி 312 (அகில இந்திய பணிகள்) சிறப்பு அதிகாரங்கள்"]
        ]
      },
      {
        "id": "tbl_perm_vs_dissolvable_p1",
        "title_en": "2. Permanent House vs Dissolvable House Comparison",
        "title_ta": "2. நிரந்தர அவை vs கலைக்கப்படும் அவை ஒப்பீடு",
        "headers_en": ["Aspect", "Permanent House (Rajya Sabha)", "Dissolvable House (Lok Sabha)"],
        "headers_ta": ["கூறு", "நிரந்தர அவை (மாநிலங்களவை)", "கலைக்கப்படும் அவை (மக்களவை)"],
        "rows_en": [
          ["Dissolution Power", "Cannot be dissolved under any circumstances (Art 83(1))", "Can be dissolved by President under Art 85(2)(b)"],
          ["Continuity of Body", "Continuous chamber; never fully vacates at one time", "Entire House vacates upon dissolution or expiry of 5 years"],
          ["Retirement Cycle", "One-third members retire every 2 years", "All members vacate simultaneously upon dissolution"],
          ["Effect of Emergency", "Unaffected by Emergency proclamation", "Term can be extended by 1 year at a time during Emergency"],
          ["Federal Representation", "Represents the federal units (States & UTs)", "Represents the total population of India directly"]
        ],
        "rows_ta": [
          ["கலைப்பு அதிகாரம்", "எந்தச் சூழலிலும் கலைக்கப்பட முடியாது (விதி 83(1))", "விதி 85(2)(b)-ன் கீழ் குடியரசுத் தலைவரால் கலைக்கப்படலாம்"],
          ["தொடர்ச்சித் தன்மை", "தொடர்ச்சியான அவை; ஒரே நேரத்தில் முழுமையாகக் காலியாகாது", "கலைக்கப்படும் போது அல்லது 5 ஆண்டுகள் முடிந்ததும் முழு அவையும் காலியாகும்"],
          ["ஓய்வு சுழற்சி", "மூன்றில் ஒரு பங்கு உறுப்பினர்கள் 2 ஆண்டிற்கு ஒருமுறை ஓய்வு பெறுகின்றனர்", "அவைக் கலைப்பின் போது அனைத்து உறுப்பினர்களும் ஒரே நேரத்தில் விலகுகின்றனர்"],
          ["அவசரநிலைத் தாக்கம்", "அவசரநிலை பிரகடனத்தால் பாதிக்கப்படாது", "அவசரநிலையின் போது பதவிக்காலம் 1 ஆண்டு நீட்டிக்கப்படலாம்"],
          ["கூட்டாட்சிப் பிரதிநிதித்துவம்", "கூட்டாட்சி ክፍகளான மாநிலங்கள் & யூனியன் பிரதேசங்களைப் பிரதிநிதித்துவப்படுத்துகிறது", "இந்திய முழு மக்கள் தொகையையும் நேரடியாகப் பிரதிநிதித்துவப்படுத்துகிறது"]
        ]
      },
      {
        "id": "tbl_adj_vs_pro_vs_dis_p1",
        "title_en": "3. Adjournment vs Prorogation vs Dissolution Comparison",
        "title_ta": "3. அவை ஒத்திவைப்பு vs கூட்டத்தொடர் ஒத்திவைப்பு vs அவைக் கலைப்பு ஒப்பீடு",
        "headers_en": ["Feature", "Adjournment", "Prorogation", "Dissolution"],
        "headers_ta": ["அம்சம்", "அவை ஒத்திவைப்பு (Adjournment)", "கூட்டத்தொடர் ஒத்திவைப்பு (Prorogation)", "அவைக் கலைப்பு (Dissolution)"],
        "rows_en": [
          ["Meaning", "Terminates a sitting of the House", "Terminates a session of the House", "Ends the very life of the existing Lok Sabha"],
          ["Authorized Officer", "Presiding Officer (Speaker / Chairman)", "President of India (Art 85(2)(a))", "President of India (Art 85(2)(b))"],
          ["Applicable Houses", "Both Lok Sabha and Rajya Sabha", "Both Lok Sabha and Rajya Sabha", "Lok Sabha ONLY (Rajya Sabha is permanent)"],
          ["Effect on Pending Bills", "Does NOT affect pending Bills or business", "Does NOT affect pending Bills (Art 107(3))", "Lapses pending Bills as per Article 107 rules"],
          ["Reassembly Notice", "Names specific time/day for reassembly", "Issued via Presidential notification for next session", "Requires fresh general elections to constitute new House"]
        ],
        "rows_ta": [
          ["பொருள்", "அவையின் ஒரு கூட்டத்தை முடிவுக்குக் கொண்டு வருதல்", "அவையின் ஒரு கூட்டத்தொடரையே முடிவுக்குக் கொண்டு வருதல்", "தற்போதைய மக்களவையின் ஆயுட்காலத்தையே முடிவுக்குக் கொண்டு வருதல்"],
          ["அதிகாரமளிக்கப்பட்ட அதிகாரி", "அவைத் தலைவர் (சபாநாயகர் / தலைவர்)", "இந்தியக் குடியரசுத் தலைவர் (விதி 85(2)(a))", "இந்தியக் குடியரசுத் தலைவர் (விதி 85(2)(b))"],
          ["பொருந்தும் அவைகள்", "மக்களவை மற்றும் மாநிலங்களவை இரண்டுக்கும்", "மக்களவை மற்றும் மாநிலங்களவை இரண்டுக்கும்", "மக்களவைக்கு மட்டுமே (மாநிலங்களவை நிரந்தரமானது)"],
          ["நிலுவை மசோதாக்கள் தாக்கம்", "நிலுவை மசோதாக்கள் அல்லது பணிகளைப் பாதிக்காது", "நிலுவை மசோதாக்களைப் பாதிக்காது (விதி 107(3))", "விதி 107 விதிகளின் படி நிலுவை மசோதாக்கள் காலாவதியாகும்"],
          ["மீண்டும் கூடும் அறிவிப்பு", "மீண்டும் கூடும் குறிப்பிட்ட நேரம்/நாளைக் குறிப்பிடுகிறது", "அடுத்த கூட்டத்தொடருக்குக் குடியரசுத் தலைவர் அறிவிக்கை வெளியிடுகிறார்", "புதிய அவையை அமைக்கப் புதிய பொதுத் தேர்தல்கள் தேவைப்படுகின்றன"]
        ]
      },
      {
        "id": "tbl_elec_vs_nom_p1",
        "title_en": "4. Elected vs Nominated Members Comparison",
        "title_ta": "4. தேர்ந்தெடுக்கப்பட்ட vs நியமிக்கப்பட்ட உறுப்பினர்கள் ஒப்பீடு",
        "headers_en": ["Parameter", "Elected Members", "Nominated Members"],
        "headers_ta": ["அளவுரு", "தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்கள்", "நியமிக்கப்பட்ட உறுப்பினர்கள்"],
        "rows_en": [
          ["Source of Mandate", "Elected directly (LS) or indirectly (RS)", "Nominated by President of India (Art 80(3))"],
          ["Rajya Sabha Count", "238 Members (Current 233)", "12 Members"],
          ["Fields for Nomination", "N/A (Elected through public political voting)", "Special knowledge in Literature, Science, Art, Social Service"],
          ["President Election Role", "ELIGIBLE to vote in Presidential Election (Art 54)", "NOT ELIGIBLE to vote in Presidential Election"],
          ["President Impeachment Role", "ELIGIBLE to vote in Presidential Impeachment (Art 61)", "ELIGIBLE to vote in Presidential Impeachment"],
          ["Political Party Joining", "Bound by Anti-Defection from day 1", "Can join any political party within 6 months of taking seat"]
        ],
        "rows_ta": [
          ["மக்களாணை ஆதாரம்", "நேரடியாக (LS) அல்லது மறைமுகமாக (RS) தேர்ந்தெடுக்கப்படுபவர்கள்", "இந்தியக் குடியரசுத் தலைவரால் நியமிக்கப்படுபவர்கள் (விதி 80(3))"],
          ["மாநிலங்களவை எண்ணிக்கை", "238 உறுப்பினர்கள் (தற்போது 233)", "12 உறுப்பினர்கள்"],
          ["நியமனத் துறைகள்", "பொருந்தாது (பொது அரசியல் தேர்தல் மூலம் தேர்வு)", "இலக்கியம், அறிவியல், கலை, சமூக சேவையில் சிறப்பு அறிவு"],
          ["குடியரசுத் தலைவர் தேர்தல் பங்கு", "குடியரசுத் தலைவர் தேர்தலில் வாக்களிக்கத் தகுதியுடையவர்கள் (விதி 54)", "குடியரசுத் தலைவர் தேர்தலில் வாக்களிக்கத் தகுதியற்றவர்கள்"],
          ["குடியரசுத் தலைவர் பதவி நீக்கப் பங்கு", "குடியரசுத் தலைவர் பதவி நீக்கத் தீர்மானத்தில் வாக்களிக்கத் தகுதியுடையவர்கள்", "குடியரசுத் தலைவர் பதவி நீக்கத் தீர்மானத்தில் வாக்களிக்கத் தகுதியுடையவர்கள்"],
          ["அரசியல் கட்சியில் சேருதல்", "முதல் நாளிலிருந்தே கட்சித் தாவல் தடைச் சட்டத்திற்குக் கட்டுப்பட்டவர்கள்", "பதவியேற்ற 6 மாதங்களுக்குள் எந்த அரசியல் கட்சியிலும் சேரலாம்"]
        ]
      },
      {
        "id": "tbl_parl_vs_state_leg_p1",
        "title_en": "5. Parliament vs State Legislature Comparison",
        "title_ta": "5. நாடாளுமன்றம் vs மாநில சட்டமன்றம் ஒப்பீடு",
        "headers_en": ["Feature", "Parliament of India", "State Legislature"],
        "headers_ta": ["அம்சம்", "இந்திய நாடாளுமன்றம்", "மாநில சட்டமன்றம்"],
        "rows_en": [
          ["Level of Governance", "Union Level (Part V - Articles 79 to 122)", "State Level (Part VI - Articles 168 to 212)"],
          ["Constitutional Structure", "President + Rajya Sabha + Lok Sabha (Mandatory Bicameral)", "Governor + Legislative Assembly (+ Legislative Council in 6 States)"],
          ["Legislative Competence", "Union List (100 subjects) + Concurrent List", "State List (61 subjects) + Concurrent List"],
          ["Upper House Permanence", "Rajya Sabha CANNOT be abolished by Parliament", "Legislative Council CAN be created/abolished by Parliament (Art 169)"],
          ["Emergency Legislation", "Can legislate on State List during National Emergency (Art 250)", "Legislative powers suspended/subordinated during Art 356"]
        ],
        "rows_ta": [
          ["ஆட்சி நிலை", "ஒன்றிய நிலை (பகுதி V - உறுப்புகள் 79 முதல் 122)", "மாநில நிலை (பகுதி VI - உறுப்புகள் 168 முதல் 212)"],
          ["அரசியலமைப்பு அமைப்பு", "குடியரசுத் தலைவர் + மாநிலங்களவை + மக்களவை (கட்டாய ஈரவை)", "ஆளுநர் + சட்டப்பேரவை (+ 6 மாநிலங்களில் சட்ட மேலவை)"],
          ["சட்டமன்ற அதிகார எல்லை", "மத்தியப் பட்டியல் (100 தலைப்புகள்) + பொதுப் பட்டியல்", "மாநிலப் பட்டியல் (61 தலைப்புகள்) + பொதுப் பட்டியல்"],
          ["மேலவை நிலைத்தன்மை", "மாநிலங்களவையை நாடாளுமன்றத்தால் ஒழிக்க முடியாது", "சட்ட மேலவையை நாடாளுமன்றத்தால் உருவாக்கவோ ஒழிக்கவோ முடியும் (விதி 169)"],
          ["அவசரநிலைச் சட்டம்", "தேசிய அவசரநிலையின் போது மாநிலப் பட்டியலில் சட்டமியற்றலாம் (விதி 250)", "விதி 356-ன் போது சட்டமன்ற அதிகாரங்கள் இடைநிறுத்தம்/கட்டுப்படுத்தப்படும்"]
        ]
      },
      {
        "id": "tbl_ls_vs_la_p1",
        "title_en": "6. Lok Sabha vs Legislative Assembly (Vidhan Sabha) Comparison",
        "title_ta": "6. மக்களவை vs மாநிலச் சட்டப்பேரவை ஒப்பீடு",
        "headers_en": ["Parameter", "Lok Sabha (Union)", "Legislative Assembly (State)"],
        "headers_ta": ["அளவுரு", "மக்களவை (ஒன்றியம்)", "மாநிலச் சட்டப்பேரவை (மாநிலம்)"],
        "rows_en": [
          ["Representation Area", "National constituencies across India", "State legislative constituencies within a single State"],
          ["Minimum Age", "25 Years (Art 84)", "25 Years (Art 173)"],
          ["Normal Tenure", "5 Years (Art 83(2))", "5 Years (Art 172(1))"],
          ["Dissolution Authority", "President of India on advice of Cabinet", "Governor of the State on advice of CM/Cabinet"],
          ["Presiding Officer", "Speaker of Lok Sabha (Art 93)", "Speaker of Legislative Assembly (Art 178)"],
          ["Money Bill Monopoly", "Exclusive origin of Union Money Bills (Art 109)", "Exclusive origin of State Money Bills (Art 198)"]
        ],
        "rows_ta": [
          ["பிரதிநிதித்துவப் பகுதி", "இந்தியா முழுவதிலும் உள்ள தேசியத் தொகுதிகள்", "ஒரு மாநிலத்திற்குள் உள்ள மாநிலச் சட்டமன்றத் தொகுதிகள்"],
          ["குறைந்தபட்ச வயது", "25 வயது (விதி 84)", "25 வயது (விதி 173)"],
          ["சாதாரண பதவிக்காலம்", "5 ஆண்டுகள் (விதி 83(2))", "5 ஆண்டுகள் (விதி 172(1))"],
          ["அவைக் கலைப்பு அதிகாரி", "அமைச்சரவை ஆலோசனையின் பேரில் இந்தியக் குடியரசுத் தலைவர்", "முதலமைச்சர் ஆலோசனையின் பேரில் மாநில ஆளுநர்"],
          ["அவைத் தலைவர்", "மக்களவைச் சபாநாயகர் (விதி 93)", "மாநிலச் சட்டப்பேரவைச் சபாநாயகர் (விதி 178)"],
          ["பண மசோதா ஏகபோகம்", "ஒன்றிய பண மசோதாக்களின் பிரத்யேகத் தொடக்கம் (விதி 109)", "மாநில பண மசோதாக்களின் பிரத்யேகத் தொடக்கம் (விதி 198)"]
        ]
      }
    ],
    "mind_map": [
      {
        "title": "Parliament of India (Part V - Articles 79 to 104)",
        "short_label": "Parliament Part 1",
        "children": [
          {
            "title": "1. Constitutional Structure (Art 79)",
            "short_label": "Structure",
            "children": [
              {"title": "President of India (Integral part, Not a member of either House)", "short_label": "President"},
              {"title": "Rajya Sabha (Council of States - Upper House)", "short_label": "Rajya Sabha"},
              {"title": "Lok Sabha (House of the People - Lower House)", "short_label": "Lok Sabha"}
            ]
          },
          {
            "title": "2. Rajya Sabha (Art 80 & 89)",
            "short_label": "Rajya Sabha",
            "children": [
              {"title": "Max 250 (238 Elected + 12 Nominated in Lit, Sci, Art, Social Service)", "short_label": "Composition"},
              {"title": "Permanent House (Not dissolvable); 6-yr term (RPA 1951); 1/3rd retire every 2 yrs", "short_label": "Tenure"},
              {"title": "Vice-President is Ex-Officio Chairman (Art 89)", "short_label": "Chairman"}
            ]
          },
          {
            "title": "3. Lok Sabha (Art 81 & 93)",
            "short_label": "Lok Sabha",
            "children": [
              {"title": "Max 550 (Direct election by Adult Franchise Art 326; 61st Amend 18 yrs)", "short_label": "Composition"},
              {"title": "5-yr normal term; Dissolvable by President; Extended 1 yr in Emergency", "short_label": "Tenure"},
              {"title": "Speaker & Deputy Speaker elected from members (Art 93)", "short_label": "Speaker"}
            ]
          },
          {
            "title": "4. Membership & Sessions (Art 84, 85, 101, 102)",
            "short_label": "Rules & Sessions",
            "children": [
              {"title": "Qualifications (Art 84: 25 yrs LS / 30 yrs RS); Disqualifications (Art 102)", "short_label": "Qualifications"},
              {"title": "Vacation: 60 Days unapproved absence rule (Art 101)", "short_label": "60-Day Rule"},
              {"title": "Art 85: Max gap 6 months; Adjournment (Speaker) vs Prorogation & Dissolution (President)", "short_label": "Sessions"}
            ]
          }
        ]
      }
    ],
    "tnpsc_traps": [
      {
        "title": "1. Parliament Component Trap (நாடாளுமன்ற அங்கப் பொறி)",
        "points": {
          "en": [
            "TRAP: Believing Parliament consists ONLY of Lok Sabha and Rajya Sabha.",
            "FACT: Under Article 79, Parliament consists of the PRESIDENT, Rajya Sabha, and Lok Sabha. President is an integral constitutional part of Parliament."
          ],
          "ta": [
            "பொறி: நாடாளுமன்றம் என்பது மக்களவை மற்றும் மாநிலங்களவை மட்டுமே கொண்டது என நினைப்பது.",
            "உண்மை: உறுப்பு 79-ன் படி நாடாளுமன்றம் என்பது குடியரசுத் தலைவர், மாநிலங்களவை மற்றும் மக்களவை உள்ளடக்கியது."
          ]
        }
      },
      {
        "title": "2. Rajya Sabha Member Tenure Source Trap (மாநிலங்களவை உறுப்பினர் பதவிக்காலப் பொறி)",
        "points": {
          "en": [
            "TRAP: Thinking the 6-year tenure of Rajya Sabha members is explicitly written in the Constitution.",
            "FACT: The Constitution DOES NOT specify the tenure of Rajya Sabha members! It left it to Parliament, which fixed it at 6 YEARS under the Representation of the People Act 1951."
          ],
          "ta": [
            "பொறி: மாநிலங்களவை உறுப்பினர்களின் 6 ஆண்டு பதவிக்காலம் அரசியலமைப்பில் நேரடியாக எழுதப்பட்டுள்ளது என நினைப்பது.",
            "உண்மை: அரசியலமைப்பு மாநிலங்களவை உறுப்பினர்களின் பதவிக்காலத்தைக் குறிப்பிடவில்லை! 1951 மக்கள் பிரதிநிதித்துவச் சட்டம் மூலமே நாடாளுமன்றம் அதை 6 ஆண்டுகளாக நிர்ணயித்தது."
          ]
        }
      },
      {
        "title": "3. Adjournment vs Prorogation Authority Trap (ஒத்திவைப்பு அதிகாரப் பொறி)",
        "points": {
          "en": [
            "TRAP: Assuming the President of India adjourns daily sittings of the House.",
            "FACT: ADJOURNMENT (and Adjournment Sine Die) is done by the PRESIDING OFFICER (Speaker/Chairman). PROROGATION and DISSOLUTION are done by the PRESIDENT OF INDIA under Article 85."
          ],
          "ta": [
            "பொறி: அவையின் தினசரி கூட்டங்களை இந்தியக் குடியரசுத் தலைவர் ஒத்திவைக்கிறார் என நினைப்பது.",
            "உண்மை: அவை ஒத்திவைப்பு (Adjournment) அவைத் தலைவரால் (சபாநாயகர்/தலைவர்) செய்யப்படுகிறது. கூட்டத்தொடர் ஒத்திவைப்பு (Prorogation) மற்றும் அவைக் கலைப்பு (Dissolution) குடியரசுத் தலைவரால் செய்யப்படுகிறது."
          ]
        }
      },
      {
        "title": "4. Age Qualification Swap Trap (வயதுத் தகுதிக் குழப்பப் பொறி)",
        "points": {
          "en": [
            "TRAP: Swapping age qualifications for Lok Sabha and Rajya Sabha.",
            "FACT: Under Article 84, minimum age for LOK SABHA is 25 YEARS (same as Legislative Assembly / CM), while minimum age for RAJYA SABHA is 30 YEARS (same as Legislative Council)."
          ],
          "ta": [
            "பொறி: மக்களவை மற்றும் மாநிலங்களவைக்கான வயதுத் தகுதிகளைக் குழப்பிக் கொள்ளுதல்.",
            "உண்மை: உறுப்பு 84-ன் படி மக்களவைக்குக் குறைந்தபட்ச வயது 25 ஆண்டுகள்; மாநிலங்களவைக்குக் குறைந்தபட்ச வயது 30 ஆண்டுகள் ஆகும்."
          ]
        }
      },
      {
        "title": "5. Absenteeism Seat Vacation 60-Day Rule Trap (60 நாட்கள் வராமைப் பொறி)",
        "points": {
          "en": [
            "TRAP: Counting prorogued days or long adjournments towards the 60-day absenteeism limit.",
            "FACT: Under Article 101(4), in calculating the 60 consecutive days of absence without permission, NO ACCOUNT is taken of any period during which the House is prorogued or adjourned for more than 4 consecutive days."
          ],
          "ta": [
            "பொறி: 60 நாட்கள் வராமை வரம்பில் கூட்டத்தொடர் ஒத்திவைக்கப்பட்ட நாட்களையும் கணக்கிடுவது.",
            "உண்மை: உறுப்பு 101(4)-ன் படி 60 நாட்கள் கணக்கிடப்படும் போது, அவை ஒத்திவைக்கப்பட்ட அல்லது 4 நாட்களுக்கு மேல் ஒத்திவைக்கப்பட்ட காலம் கணக்கில் எடுத்துக்கொள்ளப்படாது."
          ]
        }
      }
    ],
    "quick_revision": {
      "en": [
        "Constitutional Basis: Article 79 (Parliament = President + Rajya Sabha + Lok Sabha).",
        "Rajya Sabha: Article 80 (Max 250; 238 elected + 12 nominated in Lit, Sci, Art, Social Service). Permanent House (Art 83(1)), 6-yr member term (RPA 1951), 1/3rd retire every 2 yrs.",
        "Lok Sabha: Article 81 (Max 550; Direct election via Adult Franchise Art 326; 61st Amend 18 yrs). 5-yr term (Art 83(2)), dissolvable by President.",
        "Qualifications: Article 84 (25 yrs LS / 30 yrs RS; Citizen of India). Disqualifications: Article 102 (Office of profit, Insolvency, 10th Schedule). Decided by President + ECI (Art 103).",
        "Sessions: Article 85 (Max gap 6 months). Adjournment by Presiding Officer; Prorogation & Dissolution by President.",
        "Seat Vacation: Article 101 (Double membership, resignation, 60 days unapproved absence)."
      ],
      "ta": [
        "அரசியலமைப்பு அடிப்படை: உறுப்பு 79 (நாடாளுமன்றம் = குடியரசுத் தலைவர் + மாநிலங்களவை + மக்களவை).",
        "மாநிலங்களவை: உறுப்பு 80 (அதிகபட்சம் 250; 238 தேர்வு + 12 இலக்கியம், அறிவியல், கலை, சமூக சேவை நியமனம்). நிரந்தர அவை (விதி 83(1)), 6 ஆண்டு உறுப்பினர் பதவிக்காலம் (RPA 1951), 2 ஆண்டிற்கு 1/3 பங்கு ஓய்வு.",
        "மக்களவை: உறுப்பு 81 (அதிகபட்சம் 550; நேரடித் தேர்தல் விதி 326; 61-வது திருத்தம் 18 வயது). 5 ஆண்டு பதவிக்காலம் (விதி 83(2)), குடியரசுத் தலைவரால் கலைக்கப்படக்கூடியது.",
        "தகுதிகள்: உறுப்பு 84 (25 வயது LS / 30 வயது RS; இந்தியக் குடிமகன்). தகுதியிழப்புகள்: உறுப்பு 102 (ஆதாயம் தரும் பதவி, வங்கி நொடிப்பு, 10-வது அட்டவணை). முடிவெடுப்பவர் குடியரசுத் தலைவர் + ECI (விதி 103).",
        "கூட்டத்தொடர்கள்: உறுப்பு 85 (அதிகபட்ச இடைவெளி 6 மாதங்கள்). அவை ஒத்திவைப்பு அவைத் தலைவரால்; கூட்டத்தொடர் ஒத்திவைப்பு & கலைப்பு குடியரசுத் தலைவரால்.",
        "இடங்கள் காலியாதல்: உறுப்பு 101 (இரட்டை உறுப்பினர், ராஜினாமா, 60 நாட்கள் அனுமதி பெறாமல் வராமை)."
      ]
    },
    "must_remember": {
      "en": [
        "MUST REMEMBER: Parliament = President + Rajya Sabha + Lok Sabha (Article 79).",
        "MUST REMEMBER: Minimum age = 25 years for Lok Sabha, 30 years for Rajya Sabha (Article 84).",
        "MUST REMEMBER: Rajya Sabha member 6-year term is in RPA 1951, NOT directly in Constitution.",
        "MUST REMEMBER: Adjournment is done by Presiding Officer; Prorogation & Dissolution by President (Article 85).",
        "MUST REMEMBER: 60 consecutive days of unapproved absence leads to seat vacation (Article 101)."
      ],
      "ta": [
        "நினைவில் கொள்க: நாடாளுமன்றம் = குடியரசுத் தலைவர் + மாநிலங்களவை + மக்களவை (உறுப்பு 79).",
        "நினைவில் கொள்க: குறைந்தபட்ச வயது = மக்களவைக்கு 25 வயது, மாநிலங்களவைக்கு 30 வயது (உறுப்பு 84).",
        "நினைவில் கொள்க: மாநிலங்களவை உறுப்பினர் 6 ஆண்டு பதவிக்காலம் 1951 RPA-வில் உள்ளது, அரசியலமைப்பில் நேரடியாக இல்லை.",
        "நினைவில் கொள்க: அவை ஒத்திவைப்பு அவைத் தலைவரால் செய்யப்படுகிறது; கூட்டத்தொடர் ஒத்திவைப்பு & கலைப்பு குடியரசுத் தலைவரால் (உறுப்பு 85).",
        "நினைவில் கொள்க: அனுமதி பெறாமல் தொடர்ச்சியாக 60 நாட்கள் வராமை இடம் காலியாவதற்கு வழிவகுக்கும் (உறுப்பு 101)."
      ]
    }
  }
}

target_file = "data/notes/polity/parliament_part_1.json"
os.makedirs("data/notes/polity", exist_ok=True)

with open(target_file, "w", encoding="utf-8") as f:
  json.dump(part1_data, f, ensure_ascii=False, indent=2)

print(f"✅ Parliament Part 1 successfully saved to: {target_file}")
