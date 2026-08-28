# -*- coding: utf-8 -*-
"""
Builder Script for Supreme Court of India Notes — Part 1
Subject: Indian Polity
Topic: Supreme Court of India – Part 1 (Structure, Judges & Independence)
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("==================================================")
print("BUILDING SUPREME COURT NOTES — PART 1")
print("==================================================")

part1_data = {
  "meta": {
    "topic_id": "polity_supreme_court_part_1",
    "repository_id": "polity_supreme_court",
    "display_title": "Supreme Court of India – Part 1",
    "part": 1,
    "total_parts": 3,
    "subject": "polity",
    "chapter": "Supreme Court of India",
    "language": "English + Tamil"
  },
  "metadata": {
    "topic_id": "polity_supreme_court_part_1",
    "repository_id": "polity_supreme_court",
    "display_title": "Supreme Court of India – Part 1",
    "part": 1,
    "total_parts": 3,
    "subject": "polity",
    "chapter": "Supreme Court of India",
    "language": "English + Tamil"
  },
  "keywords": [
    "Supreme Court of India",
    "Part V Chapter IV",
    "Articles 124 to 147",
    "Article 124",
    "Article 125",
    "Article 126",
    "Article 127",
    "Article 128",
    "Article 129",
    "Article 130",
    "Article 146",
    "Chief Justice of India",
    "Collegium System",
    "First Judges Case 1981",
    "Second Judges Case 1993",
    "Third Judges Case 1998",
    "NJAC 99th Amendment",
    "Qualifications of SC Judge",
    "Retirement Age 65",
    "Removal of SC Judge",
    "Judges Inquiry Act 1968",
    "Proved Misbehaviour",
    "Incapacity",
    "Acting CJI",
    "Ad Hoc Judges",
    "Retired Judges",
    "Judicial Independence",
    "Article 50 DPSP",
    "Article 121 Discussion Ban",
    "Article 124(7) Practice Ban",
    "TNPSC Master Polity Notes"
  ],
  "learning_outcomes": {
    "Understand": {
      "en": [
        "Master the Constitutional Basis of Supreme Court under Part V Chapter IV (Articles 124 to 147) as the apex judicial authority and guarantor of Fundamental Rights.",
        "Understand Article 124 on Establishment and Composition: CJI + 33 Judges (Total 34 as amended by Supreme Court Number of Judges Amendment Act 2019; Parliament determines strength by law).",
        "Master Article 125 (Salaries and Conditions of Service), Article 126 (Acting CJI), Article 127 (Ad Hoc Judges), Article 128 (Retired Judges), Article 129 (Court of Record), and Article 130 (Seat of Supreme Court in Delhi).",
        "Master the Appointment framework & Collegium evolution: Constitutional text (Art 124(2) consultation) vs Judicial Conventions (1st Judges 1981, 2nd Judges 1993, 3rd Judges 1998, 4th Judges 2015 invalidating 99th Amend NJAC).",
        "Analyze Qualifications (Art 124(3): Citizen + 5 yrs HC Judge OR 10 yrs HC Advocate OR Distinguished Jurist) and Tenure (retires at age 65).",
        "Master the Removal Procedure (Art 124(4) & Judges Inquiry Act 1968): Address by both Houses by Special Majority on grounds of Proved Misbehaviour or Incapacity.",
        "Master Constitutional Safeguards for Judicial Independence: Security of tenure, expenses charged on Consolidated Fund under Article 146, prohibition of discussion in Parliament (Art 121), ban on post-retirement practice (Art 124(7)), and separation from executive (Art 50)."
      ],
      "ta": [
        "பகுதி V அத்தியாயம் IV (உறுப்புகள் 124 முதல் 147) கீழ் உச்ச நீதிமன்றத்தின் அரசியலமைப்பு அமைப்பை மேல்முறையீட்டு நீதிமன்றமாகவும் அடிப்படை உரிமைகளின் பாதுகாவலனாகவும் உணர்தல்.",
        "உறுப்பு 124 நிறுவுதல் மற்றும் அமைப்பு: தலைமை நீதிபதி + 33 நீதிபதிகள் (மொத்தம் 34 - 2019 திருத்தச் சட்டம் மூலம்; நாடாளுமன்றம் சட்டத்தின் மூலம் எண்ணிக்கையைத் தீர்மானிக்கிறது).",
        "உறுப்பு 125 (சம்பளங்கள் & சேவை நிபந்தனைகள்), உறுப்பு 126 (தற்காலிக CJI), உறுப்பு 127 (தற்காலிக நீதிபதிகள்), உறுப்பு 128 (ஓய்வு பெற்ற நீதிபதிகள்), உறுப்பு 129 (பதிவு நீதிமன்றம்) மற்றும் உறுப்பு 130 (டெல்லியில் அமர்வு) ஆகியவற்றில் தேர்ச்சி பெறுதல்.",
        "நியமன அமைப்பு மற்றும் கொலீஜியம் வளர்ச்சி: அரசியலமைப்பு விதி (விதி 124(2) ஆலோசனை) vs நீதித்துறை மரபுகள் (1-வது நீதிபதிகள் வழக்கு 1981, 2-வது வழக்கு 1993, 3-வது வழக்கு 1998, 99-வது திருத்த NJAC ரத்து 2015).",
        "தகுதிகள் (விதி 124(3): குடிமகன் + 5 ஆண்டுகள் உயர் நீதிமன்ற நீதிபதி அல்லது 10 ஆண்டுகள் உயர் நீதிமன்ற வழக்கறிஞர் அல்லது சிறப்புமிக்க சட்ட நிபுணர்) மற்றும் பதவிக்காலம் (65 வயதில் ஓய்வு).",
        "நீக்க நடைமுறையில் தேர்ச்சி பெறுதல் (விதி 124(4) & 1968 நீதிபதிகள் விசாரணைச் சட்டம்): நிரூபிக்கப்பட்ட தவறான நடத்தை அல்லது திறமையின்மை அடிப்படையில் சிறப்பு பெரும்பான்மை தீர்மானம்.",
        "நீதித்துறை சுதந்திரத்திற்கான அரசியலமைப்புப் பாதுகாப்புகள்: பதவிப் பாதுகாப்பு, உறுப்பு 146-ன் கீழ் இந்தியத் தொகுப்பு நிதியில் சுமத்தப்பட்ட செலவுகள், நாடாளுமன்ற விவாதத் தடை (விதி 121), ஓய்வுக்குப் பின் வழக்கறிஞர் பயிற்சித் தடை (விதி 124(7)) மற்றும் நிர்வாகத்திலிருந்து பிரிப்பு (விதி 50)."
      ]
    }
  },
  "subject": "polity",
  "topic": "Supreme Court of India",
  "language": "English + Tamil",
  "ui_type": "standard_notes",
  "sections": [
    {
      "id": "sec_sc_constitutional_basis",
      "title_en": "1. Constitutional Basis & Established Structure (Articles 124 to 147 & Art 130)",
      "title_ta": "1. அரசியலமைப்பு அடிப்படை & அமைக்கப்பட்ட கட்டமைப்பு (உறுப்புகள் 124 முதல் 147 & விதி 130)",
      "type": "standard_topic"
    },
    {
      "id": "sec_article_124_composition",
      "title_en": "2. Article 124 & Article 125 — Establishment, Composition & Salaries of Supreme Court",
      "title_ta": "2. உறுப்பு 124 & உறுப்பு 125 — உச்ச நீதிமன்றத்தின் தோற்றம், அமைப்பு & சம்பளங்கள்",
      "type": "standard_topic"
    },
    {
      "id": "sec_appointment_collegium",
      "title_en": "3. Appointment of Judges & Evolution of Collegium System",
      "title_ta": "3. நீதிபதிகள் நியமனம் & கொலீஜியம் அமைப்பின் பரிணாமம்",
      "type": "standard_topic"
    },
    {
      "id": "sec_qualifications_tenure_oath",
      "title_en": "4. Qualifications, Tenure, Oath & Resignation (Article 124(3), (6))",
      "title_ta": "4. தகுதிகள், பதவிக்காலம், உறுதிமொழி & ராஜினாமா (உறுப்பு 124(3), (6))",
      "type": "standard_topic"
    },
    {
      "id": "sec_removal_procedure",
      "title_en": "5. Removal Procedure of Supreme Court Judges (Article 124(4) & 1968 Act)",
      "title_ta": "5. உச்ச நீதிமன்ற நீதிபதிகள் நீக்க நடைமுறை (உறுப்பு 124(4) & 1968 சட்டம்)",
      "type": "standard_topic"
    },
    {
      "id": "sec_special_judges",
      "title_en": "6. Acting CJI, Ad Hoc Judges & Retired Judges (Articles 126, 127 & 128)",
      "title_ta": "6. தற்காலிக தலைமை நீதிபதி, தற்காலிக நீதிபதிகள் & ஓய்வு பெற்ற நீதிபதிகள் (உறுப்புகள் 126, 127 & 128)",
      "type": "standard_topic"
    },
    {
      "id": "sec_judicial_independence",
      "title_en": "7. Constitutional Safeguards for Judicial Independence (Articles 121, 129, 146 & Art 50)",
      "title_ta": "7. நீதித்துறை சுதந்திரத்திற்கான அரசியலமைப்புப் பாதுகாப்புகள் (உறுப்புகள் 121, 129, 146 & விதி 50)",
      "type": "standard_topic"
    },
    {
      "id": "comparison_tables",
      "title_en": "8. Mandatory Comparison Tables (6 Tables)",
      "title_ta": "8. கட்டாய ஒப்பீட்டு அட்டவணைகள் (6 அட்டவணைகள்)",
      "type": "comparison"
    },
    {
      "id": "mind_map",
      "title_en": "9. Mind Map & TNPSC Trap Points",
      "title_ta": "9. மன வரைபடம் & டிஎன்பிஎஸ்சி பொறிப் புள்ளிகள்",
      "type": "mind_map"
    }
  ],
  "content": {
    "definition": {
      "en": "The Supreme Court of India is the apex judicial body established under Part V Chapter IV (Articles 124 to 147) of the Constitution. It functions as the highest court of appeal, final interpreter of the Constitution, and guardian of Fundamental Rights.",
      "ta": "இந்திய உச்ச நீதிமன்றம் என்பது அரசியலமைப்பின் பகுதி V அத்தியாயம் IV (உறுப்புகள் 124 முதல் 147 வரை) கீழ் அமைக்கப்பட்ட நாட்டின் மிகவுயர்ந்த நீதித்துறை அமைப்பாகும். இதுவே நாட்டின் உச்ச மேல்முறையீட்டு நீதிமன்றமாகவும், அரசியலமைப்பின் இறுதி விளக்கவுரையாளராகவும், அடிப்படை உரிமைகளின் பாதுகாவலனாகவும் செயல்படுகிறது."
    },
    "introduction": {
      "en": "Inaugurated on January 28, 1950 (succeeding the Federal Court of India established under GOI Act 1935), the Supreme Court stands at the apex of an integrated, single judicial system in India. Article 124 establishes the court, Article 125 determines salaries, Article 130 specifies the Seat of Supreme Court in Delhi, while Articles 126 to 128 provide for special judge appointments.",
      "ta": "1950 ஜனவரி 28 அன்று தொடக்கப்பட்ட உச்ச நீதிமன்றம், இந்தியாவின் ஒருங்கிணைந்த ஒற்றை நீதித்துறை அமைப்பின் உச்சியில் நிற்கிறது. உறுப்பு 124 நீதிமன்ற தோற்றத்தை அமைக்கிறது, உறுப்பு 125 சம்பளங்களைத் தீர்மானிக்கிறது, உறுப்பு 130 டெல்லியில் உச்ச நீதிமன்ற அமர்வைக் (Seat of Supreme Court) குறிப்பிடுகிறது."
    },
    "sec_sc_constitutional_basis": [
      {
        "title_en": "Part V Chapter IV — The Union Judiciary & Seat of Court (Articles 124 to 147, Art 130)",
        "title_ta": "பகுதி V அத்தியாயம் IV — ஒன்றிய நீதித்துறை & நீதிமன்ற அமர்வு (உறுப்புகள் 124 முதல் 147, விதி 130)",
        "points": {
          "en": [
            "Single Integrated Judicial System: Supreme Court at top, High Courts in middle, Subordinate Courts below.",
            "Historical Predecessor: Federal Court of India (1937 to 1950) created under GOI Act 1935.",
            "Inauguration Date: January 28, 1950.",
            "Constitutional Location: Part V (The Union), Chapter IV (The Union Judiciary), Articles 124 to 147.",
            "Seat of Supreme Court (Article 130): The Constitution declares DELHI as the seat of the Supreme Court. The Chief Justice of India is empowered to appoint other place or places as seat of Supreme Court ONLY WITH THE PRIOR APPROVAL OF THE PRESIDENT OF INDIA.",
            "Role & Status: Apex Constitutional Court, Highest Court of Appeal, Final Interpreter of Constitution, and Custodian of Fundamental Rights."
          ],
          "ta": [
            "ஒருங்கிணைந்த ஒற்றை நீதித்துறை: உச்சத்தில் உச்ச நீதிமன்றம், நடுவில் உயர் நீதிமன்றங்கள், கீழே சார்பு நீதிமன்றங்கள்.",
            "வரலாற்று முன்னோடி: 1935 இந்திய அரசுச் சட்டத்தின் கீழ் அமைக்கப்பட்ட இந்தியக் கூட்டாட்சி நீதிமன்றம் (1937 முதல் 1950 வரை).",
            "தொடங்கப்பட்ட நாள்: 1950 ஜனவரி 28.",
            "அரசியலமைப்பு இடம்: பகுதி V (ஒன்றியம்), அத்தியாயம் IV (ஒன்றிய நீதித்துறை), உறுப்புகள் 124 முதல் 147 வரை.",
            "உச்ச நீதிமன்றத்தின் அமர்வு இடம் (உறுப்பு 130): அரசியலமைப்பு டெல்லியை உச்ச நீதிமன்றத்தின் முதன்மை அமர்வு இடமாக அறிவிக்கிறது. இந்தியக் குடியரசுத் தலைவரின் முன்-ஒப்புதலுடன் மட்டுமே CJI பிற இடங்களை அமர்வு இடமாக நியமிக்க முடியும்.",
            "பங்கு & நிலை: உச்ச அரசியலமைப்பு நீதிமன்றம், மிகவுயர்ந்த மேல்முறையீட்டு நீதிமன்றம், அரசியலமைப்பின் இறுதி விளக்கவுரையாளர் மற்றும் அடிப்படை உரிமைகளின் பாதுகாவலன்."
          ]
        }
      }
    ],
    "sec_article_124_composition": [
      {
        "title_en": "Article 124 & Article 125 — Composition, Strength & Salaries",
        "title_ta": "உறுப்பு 124 & உறுப்பு 125 — அமைப்பு, நீதிபதிகள் எண்ணிக்கை & சம்பளங்கள்",
        "points": {
          "en": [
            "Original Strength in 1950: 8 Judges (1 CJI + 7 other Judges).",
            "Parliamentary Authority (Article 124(1)): PARLIAMENT TO INCREASE THE NUMBER OF JUDGES BY LAW.",
            "Evolution of Strength:",
            "  • 1956: 11 (1 CJI + 10) | 1960: 14 | 1977: 18 | 1986: 26 | 2009: 31 | 2019: 34 (1 CJI + 33 Judges).",
            "Current Total Strength: 34 Judges including the Chief Justice of India.",
            "Salaries and Conditions of Service (Article 125): Salaries, allowances, privileges, leave, and pensions of Supreme Court judges are determined by PARLIAMENT BY LAW under Article 125. Specified in Second Schedule. Cannot be altered to their disadvantage after appointment."
          ],
          "ta": [
            "1950-ல் மூல எண்ணிக்கை: 8 நீதிபதிகள் (1 CJI + 7 இதர நீதிபதிகள்).",
            "நாடாளுமன்ற அதிகாரம் (உறுப்பு 124(1)): நாடாளுமன்றத்திற்குச் சட்டத்தின் மூலம் எண்ணிக்கையை உயர்த்த அதிகாரம் உண்டு.",
            "எண்ணிக்கை வளர்ச்சி: 1956 (11), 1960 (14), 1977 (18), 1986 (26), 2009 (31), 2019 திருத்தச் சட்டம் (34 - 1 CJI + 33 நீதிபதிகள்).",
            "தற்போதைய மொத்த எண்ணிக்கை: 34 நீதிபதிகள்.",
            "சம்பளங்கள் & சேவை நிபந்தனைகள் (உறுப்பு 125): உறுப்பு 125-ன் கீழ் நாடாளுமன்றத்தால் சட்டத்தின் மூலம் நிர்ணயிக்கப்படுகிறது. இரண்டாவது அட்டவணையில் குறிப்பிடப்பட்டுள்ளது. நியமனத்திற்குப் பின் அவர்களது சம்பளத்தைக் குறைக்க முடியாது."
          ]
        }
      }
    ],
    "sec_appointment_collegium": [
      {
        "title_en": "Appointment of Judges & Collegium Evolution (Article 124(2))",
        "title_ta": "நீதிபதிகள் நியமனம் & கொலீஜியம் அமைப்பின் பரிணாமம் (உறுப்பு 124(2))",
        "points": {
          "en": [
            "Appointing Authority (Article 124(2)): Appointed by the PRESIDENT OF INDIA by warrant under his hand and seal after compulsory consultation with CJI.",
            "Evolution of Collegium System:",
            "  1. First Judges Case (1981): Consultation != concurrence; executive primacy.",
            "  2. Second Judges Case (1993): Consultation == Concurrence; CJI primacy; 3-member Collegium formed.",
            "  3. Third Judges Case (1998): Collegium expanded to CJI + 4 SENIOR-MOST SC JUDGES.",
            "Seniority Convention: Senior-most judge of SC appointed as CJI.",
            "NJAC & 99th Constitutional Amendment (2014-2015): Invalidated in Fourth Judges Case (2015) as unconstitutional to protect Judicial Independence.",
            "CRITICAL TRAP: The word 'COLLEGIUM' is NOT mentioned anywhere in the Constitution!"
          ],
          "ta": [
            "நியமிக்கும் அதிகாரி (உறுப்பு 124(2)): CJI ஆலோசனையுடன் இந்தியக் குடியரசுத் தலைவரால் ஆணை மூலம் நியமிக்கப்படுகிறார்.",
            "கொலீஜியம் வளர்ச்சி: 1-வது வழக்கு (1981 - நிர்வாக முதன்மை), 2-வது வழக்கு (1993 - CJI முதன்மை, 3 நபர் கொலீஜியம்), 3-வது வழக்கு (1998 - CJI + 4 மூத்த நீதிபதிகள்).",
            "மூப்பு மரபு: மூத்த நீதிபதியே CJI ஆக நியமிக்கப்படுகிறார்.",
            "NJAC 99-வது திருத்தம் 4-வது நீதிபதிகள் வழக்கில் (2015) ரத்து செய்யப்பட்டு கொலீஜியம் மீண்டும் வந்தது.",
            "முக்கியப் பொறி: 'கொலீஜியம்' என்ற சொல் அரசியலமைப்பில் எங்குமே இல்லை!"
          ]
        }
      }
    ],
    "sec_qualifications_tenure_oath": [
      {
        "title_en": "Qualifications, Tenure, Oath & Resignation (Article 124(3), (6))",
        "title_ta": "தகுதிகள், பதவிக்காலம், உறுதிமொழி & ராஜினாமா (உறுப்பு 124(3), (6))",
        "points": {
          "en": [
            "Qualifications of SC Judge (Article 124(3)): Citizen of India AND (a) 5 yrs High Court Judge OR (b) 10 yrs High Court Advocate OR (c) Distinguished Jurist in President's opinion.",
            "NO Minimum Age: Constitution DOES NOT prescribe any minimum age for appointment as SC judge.",
            "Tenure of Office: Retires upon attaining the AGE OF 65 YEARS.",
            "Resignation: Writing under hand addressed to the PRESIDENT OF INDIA.",
            "Oath or Affirmation (Article 124(6)): Before the PRESIDENT OF INDIA. Form in THIRD SCHEDULE."
          ],
          "ta": [
            "தகுதிகள் (உறுப்பு 124(3)): இந்தியக் குடிமகன் + 5 ஆண்டுகள் HC நீதிபதி அல்லது 10 ஆண்டுகள் HC வழக்கறிஞர் அல்லது குடியரசுத் தலைவர் பார்வையில் சிறப்புமிக்க சட்ட நிபுணர்.",
            "குறைந்தபட்ச வயது இல்லை: அரசியலமைப்பில் குறைந்தபட்ச வயது வரம்பில்லை.",
            "பதவிக்காலம்: 65 வயதை அடையும் போது ஓய்வு பெறுகிறார்.",
            "ராஜினாமா: இந்தியக் குடியரசுத் தலைவருக்குக் கடிதம் எழுதி பதவி விலகல்.",
            "உறுதிமொழி (உறுப்பு 124(6)): இந்தியக் குடியரசுத் தலைவர் முன்னிலையில் எடுக்கப்படுகிறது. 3-வது அட்டவணையில் உள்ளது."
          ]
        }
      }
    ],
    "sec_removal_procedure": [
      {
        "title_en": "Removal Procedure of Supreme Court Judges (Article 124(4) & 1968 Act)",
        "title_ta": "உச்ச நீதிமன்ற நீதிபதிகள் நீக்க நடைமுறை (உறுப்பு 124(4) & 1968 சட்டம்)",
        "points": {
          "en": [
            "Constitutional Basis (Article 124(4)): Order of PRESIDENT after Parliamentary Address supported by SPECIAL MAJORITY in same session.",
            "Two Constitutional Grounds: 1. Proved Misbehaviour; OR 2. Incapacity.",
            "Judges Inquiry Act 1968 Procedure: Motion signed by 100 LS or 50 RS members -> 3-Member Judicial Committee (SC Judge + HC CJ + Distinguished Jurist) -> Special Majority voting in both Houses -> President's Removal Order.",
            "NO Supreme Court judge has been impeached / removed so far in India!"
          ],
          "ta": [
            "அரசியலமைப்பு அடிப்படை (உறுப்பு 124(4)): நாடாளுமன்றச் சிறப்பு பெரும்பான்மைத் தீர்மானத்திற்குப் பின் குடியரசுத் தலைவர் ஆணை மூலம் நீக்கம்.",
            "இரண்டு அடிப்படைகள்: 1. நிரூபிக்கப்பட்ட தவறான நடத்தை; 2. திறமையின்மை.",
            "1968 சட்டம் நடைமுறை: 100 LS / 50 RS எம்பிக்கள் கையொப்பம் -> 3 நீதிபதிகள் விசாரணைக் குழு -> சிறப்பு பெரும்பான்மை வாக்கெடுப்பு -> குடியரசுத் தலைவர் நீக்க ஆணை.",
            "இந்தியாவில் இதுவரை எந்தவொரு உச்ச நீதிமன்ற நீதிபதியும் பதவியிலிருந்து நீக்கப்படவில்லை!"
          ]
        }
      }
    ],
    "sec_special_judges": [
      {
        "title_en": "Acting CJI, Ad Hoc Judges & Retired Judges (Articles 126, 127 & 128)",
        "title_ta": "தற்காலிக தலைமை நீதிபதி, தற்காலிக நீதிபதிகள் & ஓய்வு பெற்ற நீதிபதிகள் (உறுப்புகள் 126, 127 & 128)",
        "points": {
          "en": [
            "Acting Chief Justice of India (Article 126): Appointed by PRESIDENT when CJI office is vacant, absent, or unable to perform duties.",
            "Ad Hoc Judges (Article 127): Appointed by CHIEF JUSTICE OF INDIA when there is a LACK OF QUORUM of permanent judges. Mandatory: Prior consent of President + Consultation with concerned High Court CJ.",
            "Retired Judges at Supreme Court (Article 128): CJI requests retired SC/HC judge with prior consent of President & person concerned to attend and act as SC judge."
          ],
          "ta": [
            "தற்காலிக தலைமை நீதிபதி (உறுப்பு 126): CJI பதவி காலியாக உள்ள போது குடியரசுத் தலைவரால் நியமிக்கப்படுகிறார்.",
            "தற்காலிக நீதிபதிகள் / Ad Hoc (உறுப்பு 127): கணப்போர்வு (Quorum) பற்றாக்குறை ஏற்படும் போது CJI நியமிக்கிறார் (குடியரசுத் தலைவர் முன்-ஒப்புதல் + HC தலைமை நீதிபதி ஆலோசனை தேவை).",
            "ஓய்வு பெற்ற நீதிபதிகள் (உறுப்பு 128): குடியரசுத் தலைவர் முன்-ஒப்புதலுடன் ஓய்வு பெற்ற நீதிபதியை அமர்ந்து பணியாற்ற CJI கோரலாம்."
          ]
        }
      }
    ],
    "sec_judicial_independence": [
      {
        "title_en": "Constitutional Safeguards for Judicial Independence (Articles 121, 129, 146 & Art 50)",
        "title_ta": "நீதித்துறை சுதந்திரத்திற்கான அரசியலமைப்புப் பாதுகாப்புகள் (உறுப்புகள் 121, 129, 146 & விதி 50)",
        "points": {
          "en": [
            "Security of Tenure: Removed only by President on Parliamentary Special Majority Address (Art 124(4)).",
            "Fixed Service Conditions: Salaries under Art 125 cannot be altered to disadvantage.",
            "Expenses Charged on Consolidated Fund (Article 146): Salaries and administrative expenses charged on Consolidated Fund of India (non-votable by Parliament).",
            "Conduct Cannot Be Discussed (Article 121): Conduct of judges cannot be discussed in Parliament except during removal motion.",
            "Ban on Post-Retirement Practice (Article 124(7)): Banned from pleading in ANY court in India.",
            "Contempt Power (Article 129): Power to punish for contempt of itself.",
            "Separation from Executive (Article 50 DPSP): Mandates separation of judiciary from executive."
          ],
          "ta": [
            "பதவிப் பாதுகாப்பு: நாடாளுமன்றச் சிறப்பு பெரும்பான்மை மூலம் மட்டுமே குடியரசுத் தலைவரால் நீக்கம் (விதி 124(4)).",
            "நிலையான சேவை நிபந்தனைகள்: விதி 125 சம்பளங்களைக் குறைக்க முடியாது.",
            "தொகுப்பு நிதியில் சுமத்தப்பட்ட செலவுகள் (உறுப்பு 146): செலவுகள் இந்தியத் தொகுப்பு நிதியில் சுமத்தப்பட்டவை (நாடாளுமன்ற வாக்கெடுப்பிற்கு அப்பாற்பட்டவை).",
            "நடத்தையை விவாதிக்கத் தடை (உறுப்பு 121): நீதிபதிகள் நடவடிக்கைகளை நாடாளுமன்றத்தில் விவாதிக்க முடியாது.",
            "ஓய்வுக்குப் பின் பயிற்சித் தடை (உறுப்பு 124(7)): இந்தியாவின் எந்த நீதிமன்றத்திலும் பணியாற்றத் தடை.",
            "அவமதிப்பு அதிகாரம் (உறுப்பு 129): நீதிமன்ற அவமதிப்பிற்குத் தண்டிக்கும் அதிகாரம்.",
            "நிர்வாகத்திலிருந்து பிரிப்பு (உறுப்பு 50 DPSP): நீதித்துறையை நிர்வாகத்திலிருந்து பிரிக்க ஆணை."
          ]
        }
      }
    ],
    "revision_cards": [
      {
        "id": "sc_p1_c1",
        "front_en": "What is the total sanctioned strength of Supreme Court judges under the 2019 Amendment Act?",
        "front_ta": "2019 திருத்தச் சட்டத்தின் படி உச்ச நீதிமன்ற நீதிபதிகளின் மொத்த அனுமதிக்கப்பட்ட எண்ணிக்கை எவ்வளவு?",
        "back_en": "34 Judges (1 Chief Justice of India + 33 other Judges).",
        "back_ta": "34 நீதிபதிகள் (1 இந்தியத் தலைமை நீதிபதி + 33 இதர நீதிபதிகள்)."
      },
      {
        "id": "sc_p1_c2",
        "front_en": "Who has the authority to increase the number of Supreme Court judges under Article 124(1)?",
        "front_ta": "உறுப்பு 124(1)-ன் கீழ் உச்ச நீதிமன்ற நீதிபதிகளின் எண்ணிக்கையை உயர்த்த அதிகாரம் கொண்ட அமைப்பு எது?",
        "back_en": "PARLIAMENT OF INDIA by law.",
        "back_ta": "நாடாளுமன்றம் (சட்டத்தின் மூலம்)."
      },
      {
        "id": "sc_p1_c3",
        "front_en": "Is the word 'Collegium' explicitly mentioned in the Constitution of India?",
        "front_ta": "'கொலீஜியம்' என்ற சொல் இந்திய அரசியலமைப்பில் நேரடியாகக் குறிப்பிடப்பட்டுள்ளதா?",
        "back_en": "NO. It is a judicially evolved mechanism through Three Judges Cases (1981, 1993, 1998).",
        "back_ta": "இல்லை. இது மூன்று நீதிபதிகள் வழக்குகள் (1981, 1993, 1998) மூலம் நீதித்துறையால் உருவாக்கப்பட்ட நடைமுறையாகும்."
      },
      {
        "id": "sc_p1_c4",
        "front_en": "What is the retirement age of a Supreme Court judge?",
        "front_ta": "உச்ச நீதிமன்ற நீதிபதியின் ஓய்வு பெறும் வயது என்ன?",
        "back_en": "65 YEARS (High Court judges retire at 62 years).",
        "back_ta": "65 வயது (உயர் நீதிமன்ற நீதிபதிகள் 62 வயதில் ஓய்வு பெறுகின்றனர்)."
      },
      {
        "id": "sc_p1_c5",
        "front_en": "What are the qualifications required to be appointed as a Supreme Court judge under Article 124(3)?",
        "front_ta": "உறுப்பு 124(3)-ன் கீழ் உச்ச நீதிமன்ற நீதிபதியாக நியமிக்கப்படத் தேவையான தகுதிகள் யாவை?",
        "back_en": "Citizen of India + 5 yrs High Court Judge OR 10 yrs High Court Advocate OR Distinguished Jurist in President's opinion.",
        "back_ta": "இந்தியக் குடிமகன் + 5 ஆண்டுகள் உயர் நீதிமன்ற நீதிபதி அல்லது 10 ஆண்டுகள் உயர் நீதிமன்ற வழக்கறிஞர் அல்லது குடியரசுத் தலைவர் பார்வையில் சிறப்புமிக்க சட்ட நிபுணர்."
      },
      {
        "id": "sc_p1_c6",
        "front_en": "Who appoints Ad Hoc judges of Supreme Court under Article 127?",
        "front_ta": "உறுப்பு 127-ன் கீழ் உச்ச நீதிமன்றத் தற்காலிக நீதிபதிகளை (Ad Hoc) நியமிப்பவர் யார்?",
        "back_en": "Chief Justice of India (with prior consent of President and consultation with concerned HC CJ).",
        "back_ta": "இந்தியத் தலைமை நீதிபதி (குடியரசுத் தலைவரின் முன்-ஒப்புதல் மற்றும் உயர் நீதிமன்றத் தலைமை நீதிபதி ஆலோசனையுடன்)."
      },
      {
        "id": "sc_p1_c7",
        "front_en": "What majority is required in Parliament to remove a Supreme Court judge under Article 124(4)?",
        "front_ta": "உறுப்பு 124(4)-ன் கீழ் உச்ச நீதிமன்ற நீதிபதியை நீக்க நாடாளுமன்றத்தில் என்ன பெரும்பான்மை தேவை?",
        "back_en": "SPECIAL MAJORITY (Majority of total membership of House + 2/3rds of members present & voting in EACH House).",
        "back_ta": "சிறப்பு பெரும்பான்மை (மொத்த உறுப்பினர் பெரும்பான்மை + பங்கேற்று வாக்களிப்பவர்களில் 2/3 பங்கு)."
      },
      {
        "id": "sc_p1_c8",
        "front_en": "Has any Supreme Court judge been successfully removed/impeached in India so far?",
        "front_ta": "இந்தியாவில் இதுவரை ஏதேனும் ஒரு உச்ச நீதிமன்ற நீதிபதி வெற்றிகரமாகப் பதவி நீக்கம் செய்யப்பட்டுள்ளாரா?",
        "back_en": "NO. No Supreme Court judge has been removed so far.",
        "back_ta": "இல்லை. இதுவரை எந்தவொரு உச்ச நீதிமன்ற நீதிபதியும் பதவியிலிருந்து நீக்கப்படவில்லை."
      },
      {
        "id": "sc_p1_c9",
        "front_en": "Can a retired Supreme Court judge practice in any court in India under Article 124(7)?",
        "front_ta": "உறுப்பு 124(7)-ன் கீழ் ஓய்வு பெற்ற உச்ச நீதிமன்ற நீதிபதி இந்தியாவின் எந்த நீதிமன்றத்திலாவது வழக்கறிஞராகப் பணியாற்ற முடியுமா?",
        "back_en": "NO. Retired SC judges are BANNED from pleading or acting in any court or authority in India.",
        "back_ta": "இல்லை. ஓய்வு பெற்ற உச்ச நீதிமன்ற நீதிபதிகள் இந்தியாவின் எந்தவொரு நீதிமன்றத்திலும் பணியாற்றத் தடை விதிக்கப்பட்டுள்ளது."
      },
      {
        "id": "sc_p1_c10",
        "front_en": "Which Article declares Delhi as the Seat of the Supreme Court?",
        "front_ta": "உச்ச நீதிமன்றத்தின் அமர்வு இடமாக டெல்லியை அறிவிக்கும் உறுப்பு எது?",
        "back_en": "ARTICLE 130 (CJI can appoint other places ONLY with prior approval of President).",
        "back_ta": "உறுப்பு 130 (குடியரசுத் தலைவர் முன்-ஒப்புதலுடன் மட்டுமே CJI பிற இடங்களை நியமிக்க முடியும்)."
      }
    ],
    "comparison_tables": [
      {
        "id": "tbl_sc_vs_hc_p1",
        "title_en": "1. Supreme Court vs High Court Comparison",
        "title_ta": "1. உச்ச நீதிமன்றம் vs உயர் நீதிமன்றம் ஒப்பீடு",
        "headers_en": ["Feature / Dimension", "Supreme Court of India", "High Courts of States"],
        "headers_ta": ["அம்சம் / காரணி", "இந்திய உச்ச நீதிமன்றம்", "மாநில உயர் நீதிமன்றங்கள்"],
        "rows_en": [
          ["Constitutional Provisions", "Part V Chapter IV (Articles 124 to 147)", "Part VI Chapter V (Articles 214 to 231)"],
          ["Territorial Jurisdiction", "Entire Territory of India", "Respective State / Union Territory limits"],
          ["Retirement Age", "65 Years", "62 Years"],
          ["Writ Jurisdiction Scope", "Article 32: ONLY for Fundamental Rights protection", "Article 226: Fundamental Rights + Other legal rights (Wider scope)"],
          ["Administrative Oversight", "Supervises all courts in India", "Supervises all subordinate courts within state jurisdiction"],
          ["Court of Record Status", "Article 129", "Article 215"]
        ],
        "rows_ta": [
          ["அரசியலமைப்பு விதிகள்", "பகுதி V அத்தியாயம் IV (உறுப்புகள் 124 முதல் 147)", "பகுதி VI அத்தியாயம் V (உறுப்புகள் 214 முதல் 231)"],
          ["நிலப்பரப்பு வரம்பு", "இந்தியா முழுவதற்கும் பொருந்தும்", "சம்மந்தப்பட்ட மாநிலம் / யூனியன் பிரதேச எல்லைகள்"],
          ["ஓய்வு பெறும் வயது", "65 வயது", "62 வயது"],
          ["பேராணை அதிகாரம்", "உறுப்பு 32: அடிப்படை உரிமைகளுக்கு மட்டுமே", "உறுப்பு 226: அடிப்படை உரிமைகள் + பிற சட்ட உரிமைகள் (பரந்த எல்லை)"],
          ["நிர்வாகக் மேலாண்மை", "இந்தியாவின் அனைத்து நீதிமன்றங்களையும் மேற்பார்வையிடுகிறது", "மாநில எல்லைக்குள் உள்ள சார்பு நீதிமன்றங்களை மேற்பார்வையிடுகிறது"],
          ["பதிவு நீதிமன்ற நிலை", "உறுப்பு 129", "உறுப்பு 215"]
        ]
      },
      {
        "id": "tbl_sc_vs_hc_judge_p1",
        "title_en": "2. Supreme Court Judge vs High Court Judge Comparison",
        "title_ta": "2. உச்ச நீதிமன்ற நீதிபதி vs உயர் நீதிமன்ற நீதிபதி ஒப்பீடு",
        "headers_en": ["Parameter", "Supreme Court Judge", "High Court Judge"],
        "headers_ta": ["அளவுரு", "உச்ச நீதிமன்ற நீதிபதி", "உயர் நீதிமன்ற நீதிபதி"],
        "rows_en": [
          ["Retirement Age", "65 Years", "62 Years"],
          ["Distinguished Jurist Criteria", "Eligible for appointment as Distinguished Jurist (Art 124(3)(c))", "NO provision for Distinguished Jurist in High Court appointment"],
          ["Advocate Experience Needed", "10 Years as High Court Advocate", "10 Years as High Court Advocate"],
          ["Judicial Service Experience", "5 Years as High Court Judge", "10 Years in Judicial Service"],
          ["Post-Retirement Practice", "Banned from pleading in ANY court in India (Art 124(7))", "Can practice in SC and HC OTHER THAN the HC where served"],
          ["Removal Process", "Removed by President on Parliamentary Special Majority Address", "Removed by President on Parliamentary Special Majority Address (Same as SC Judge)"]
        ],
        "rows_ta": [
          ["ஓய்வு பெறும் வயது", "65 வயது", "62 வயது"],
          ["சிறப்புமிக்க சட்ட நிபுணர் தகுதி", "சிறப்புமிக்க சட்ட நிபுணராக நியமிக்கப்பட தகுதியுண்டு (விதி 124(3)(c))", "உயர் நீதிமன்ற நியமனத்தில் சிறப்புமிக்க சட்ட நிபுணர் விதி இல்லை"],
          ["வழக்கறிஞர் அனுபவம்", "உயர் நீதிமன்ற வழக்கறிஞராக 10 ஆண்டுகள்", "உயர் நீதிமன்ற வழக்கறிஞராக 10 ஆண்டுகள்"],
          ["நீதித்துறை சேவை அனுபவம்", "உயர் நீதிமன்ற நீதிபதியாக 5 ஆண்டுகள்", "நீதித்துறை சேவையில் 10 ஆண்டுகள்"],
          ["ஓய்வுக்குப் பின் பயிற்சி", "இந்தியாவின் எந்த நீதிமன்றத்திலும் பயிற்சி செய்யத் தடை (விதி 124(7))", "பணியாற்றிய HC தவிர உச்ச நீதிமன்றம் மற்றும் பிற HC-களில் பயிற்சி செய்யலாம்"],
          ["நீக்க நடைமுறை", "நாடாளுமன்றச் சிறப்பு பெரும்பான்மை மூலம் குடியரசுத் தலைவரால் நீக்கம்", "நாடாளுமன்றச் சிறப்பு பெரும்பான்மை மூலம் குடியரசுத் தலைவரால் நீக்கம் (SC நீதிபதி போல)"]
        ]
      },
      {
        "id": "tbl_appt_vs_rem_p1",
        "title_en": "3. Appointment vs Removal of Supreme Court Judge Comparison",
        "title_ta": "3. உச்ச நீதிமன்ற நீதிபதி நியமனம் vs நீக்கம் ஒப்பீடு",
        "headers_en": ["Aspect", "Appointment of SC Judge", "Removal of SC Judge (Article 124(4))"],
        "headers_ta": ["அம்சம்", "உச்ச நீதிமன்ற நீதிபதி நியமனம்", "உச்ச நீதிமன்ற நீதிபதி நீக்கம் (உறுப்பு 124(4))"],
        "rows_en": [
          ["Constitutional Provision", "Article 124(2)", "Article 124(4) & Judges Inquiry Act 1968"],
          ["Initiating Authority", "CJI Collegium recommendation to President", "Motion signed by 100 LS MPs or 50 RS MPs"],
          ["Role of Executive", "President appoints by warrant after Collegium concurrence", "President issues removal order ONLY AFTER Parliamentary Address"],
          ["Role of Parliament", "Parliament has NO direct role in individual appointment", "Parliament MUST pass removal address by SPECIAL MAJORITY"],
          ["Grounds Required", "Fulfillment of constitutional qualifications (Art 124(3))", "Proved Misbehaviour OR Incapacity ONLY"],
          ["Inquiry Mechanism", "Intelligence / IB background checks", "3-Member Judicial Committee investigation under 1968 Act"]
        ],
        "rows_ta": [
          ["அரசியலமைப்பு விதி", "உறுப்பு 124(2)", "உறுப்பு 124(4) & 1968 நீதிபதிகள் விசாரணைச் சட்டம்"],
          ["தொடங்கும் அதிகாரி", "குடியரசுத் தலைவருக்கு CJI கொலீஜியம் பரிந்துரை", "100 LS எம்பிக்கள் அல்லது 50 RS எம்பிக்கள் கையொப்பமிட்ட தீர்மானம்"],
          ["நிர்வாகத்தின் பங்கு", "கொலீஜியம் ஒப்புதலுக்குப் பின் குடியரசுத் தலைவர் நியமிக்கிறார்", "நாடாளுமன்றத் தீர்மானத்திற்குப் பின்னரே குடியரசுத் தலைவர் நீக்க ஆணை பிறப்பிக்கிறார்"],
          ["நாடாளுமன்றத்தின் பங்கு", "தனிநபர் நியமனத்தில் நாடாளுமன்றத்திற்கு நேரடிப் பங்கில்லை", "நாடாளுமன்றம் சிறப்பு பெரும்பான்மையால் நீக்கத் தீர்மானத்தை நிறைவேற்ற வேண்டும்"],
          ["தேவைப்படும் அடிப்படைகள்", "அரசியலமைப்புத் தகுடிகளைப் பூர்த்தி செய்தல் (விதி 124(3))", "நிரூபிக்கப்பட்ட தவறான நடத்தை அல்லது திறமையின்மை மட்டுமே"],
          ["விசாரணை அமைப்பு", "உளவுத்துறை / IB பின்னணிச் சோதனைகள்", "1968 சட்டத்தின் கீழ் 3 உறுப்பினர்கள் கொண்ட நீதித்துறை விசாரணைக் குழு"]
        ]
      },
      {
        "id": "tbl_sc_vs_parl_p1",
        "title_en": "4. Supreme Court vs Parliament Operational Boundaries",
        "title_ta": "4. உச்ச நீதிமன்றம் vs நாடாளுமன்ற செயல்பாட்டு எல்லைகள் ஒப்பீடு",
        "headers_en": ["Dimension", "Supreme Court Powers", "Parliament Limitations & Powers"],
        "headers_ta": ["அம்சம்", "உச்ச நீதிமன்ற அதிகாரங்கள்", "நாடாளுமன்ற வரம்புகள் & அதிகாரங்கள்"],
        "rows_en": [
          ["Judicial Review", "Can strike down Parliamentary Acts violating Constitution (Art 13)", "Cannot override Judicial Review or alter Basic Structure (Kesavananda 1973)"],
          ["Judge Strength", "Cannot alter its own sanctioned strength", "Parliament increases SC judge strength by passing law (Art 124(1))"],
          ["Conduct Discussion", "Judges' conduct cannot be discussed in Parliament (Art 121)", "Can discuss judges' conduct ONLY during Removal Motion debate"],
          ["Court Proceedings", "Courts cannot inquire into Parliamentary proceedings (Art 122)", "Parliament cannot inquire into judicial decisions except via appeal/law"],
          ["Rules & Staff", "CJI frames Court rules (Art 145) and appoints staff (Art 146)", "Expenses charged on Consolidated Fund non-votable by Parliament"]
        ],
        "rows_ta": [
          ["நீதித்துறை ஆய்வு", "அரசியலமைப்பை மீறும் நாடாளுமன்றச் சட்டங்களை ரத்து செய்யலாம் (விதி 13)", "நீதித்துறை ஆய்வை மீறவோ அடிப்படை கட்டமைப்பை மாற்றவோ முடியாது"],
          ["நீதிபதிகள் எண்ணிக்கை", "தன் சொந்த எண்ணிக்கையைத் தானே மாற்ற முடியாது", "சட்டம் இயற்றி SC நீதிபதிகள் எண்ணிக்கையை உயர்த்துகிறது (விதி 124(1))"],
          ["நடத்தை விவாதம்", "நீதிபதிகளின் செயல்பாடுகளை நாடாளுமன்றத்தில் விவாதிக்க முடியாது (விதி 121)", "நீக்கத் தீர்மான விவாதத்தின் போது மட்டுமே விவாதிக்க முடியும்"],
          ["நீதிமன்ற நடவடிக்கைகள்", "நாடாளுமன்ற நடவடிக்கைகளை நீதிமன்றங்கள் விசாரிக்க முடியாது (விதி 122)", "நீதிமன்ற முடிவுகளை நாடாளுமன்றம் விசாரிக்க முடியாது"],
          ["விதிகள் & ஊழியர்கள்", "CJI நீதிமன்ற விதிகளை உருவாக்கி (விதி 145) ஊழியர்களை நியமிக்கிறார்", "செலவுகள் தொகுப்பு நிதியில் சுமத்தப்பட்டவை; வாக்கெடுப்பிற்கு அப்பாற்பட்டவை"]
        ]
      },
      {
        "id": "tbl_const_vs_collegium_p1",
        "title_en": "5. Constitutional Text vs Collegium Practice Comparison",
        "title_ta": "5. அரசியலமைப்பு விதி vs கொலீஜியம் நடைமுறை ஒப்பீடு",
        "headers_en": ["Feature", "Constitutional Text (Article 124(2))", "Collegium System Practice"],
        "headers_ta": ["அம்சம்", "அரசியலமைப்பு விதி (உறுப்பு 124(2))", "கொலீஜியம் அமைப்பு நடைமுறை"],
        "rows_en": [
          ["Term Used", "Uses the term 'CONSULTATION' with CJI and judges", "Interpreted 'Consultation' as 'CONCURRENCE' (2nd Judges Case 1993)"],
          ["Composition Mentioned", "No mention of a 'Collegium' body", "CJI + 4 Senior-most Judges of SC (3rd Judges Case 1998)"],
          ["Primacy Authority", "Literally gave executive/President discretion", "Gave Judiciary/CJI absolute primacy in judicial selection"],
          ["Constitutional Source", "Written text of the Constitution of India 1950", "Judicially evolved through 1981, 1993, 1998 & 2015 Supreme Court judgments"],
          ["Government Binding", "Text does not explicitly say CJI opinion is binding", "Collegium recommendation is BINDING on Government upon reiteration"]
        ],
        "rows_ta": [
          ["பயன்படுத்தப்பட்ட சொல்", "CJI மற்றும் நீதிபதிகளுடன் 'ஆலோசனை (Consultation)' என்ற சொல்லைப் பயன்படுத்துகிறது", "'ஆலோசனை' என்பதை 'ஒப்புதல் (Concurrence)' என விளக்கியது (2-வது வழக்கு 1993)"],
          ["அமைப்பு குறிப்பிடல்", "'கொலீஜியம்' என்ற அமைப்பு பற்றி குறிப்பிடப்படவில்லை", "CJI + 4 மூத்த உச்ச நீதிமன்ற நீதிபதிகள் கொண்ட குழு (3-வது வழக்கு 1998)"],
          ["முதன்மை அதிகாரி", "எழுத்துப்பூர்வமாக நிர்வாகத்திற்கு/குடியரசுத் தலைவருக்கு விருப்பவுரிமை அளித்தது", "நீதிபதிகள் தேர்வில் நீதித்துறைக்கே/CJI-க்கே முற்றுரிமை முதன்மை அளித்தது"],
          ["அரசியலமைப்பு ஆதாரம்", "1950 இந்திய அரசியலமைப்பின் எழுதப்பட்ட உரை", "1981, 1993, 1998 & 2015 உச்ச நீதிமன்றத் தீர்ப்புகள் மூலம் உருவானது"],
          ["அரசு கட்டுப்பாடு", "CJI கருத்து அரசைக் கட்டுப்படுத்தும் என உரையில் வெளிப்படையாக இல்லை", "மீண்டும் வலியுறுத்தப்படும் கொலீஜியம் பரிந்துரை அரசைக் கட்டாயம் கட்டுப்படுத்தும்"]
        ]
      },
      {
        "id": "tbl_special_judges_p1",
        "title_en": "6. Acting CJI vs Ad Hoc Judge vs Retired Judge Comparison",
        "title_ta": "6. தற்காலிக தலைமை நீதிபதி vs தற்காலிக நீதிபதி vs ஓய்வு பெற்ற நீதிபதி ஒப்பீடு",
        "headers_en": ["Parameter", "Acting CJI (Article 126)", "Ad Hoc Judge (Article 127)", "Retired Judge (Article 128)"],
        "headers_ta": ["அளவுரு", "தற்காலிக தலைமை நீதிபதி (விதி 126)", "தற்காலிக நீதிபதி / Ad Hoc (விதி 127)", "ஓய்வு பெற்ற நீதிபதி (விதி 128)"],
        "rows_en": [
          ["Appointing Authority", "PRESIDENT OF INDIA", "CHIEF JUSTICE OF INDIA (with President's prior consent)", "CHIEF JUSTICE OF INDIA (with President's prior consent)"],
          ["Eligible Candidate", "Existing Supreme Court Judge", "Qualified High Court Judge", "Retired SC or Retired HC Judge"],
          ["Primary Reason", "CJI office vacant, absent, or unable to perform duties", "Lack of QUORUM of permanent judges in SC", "Temporary increase in workload or special cases"],
          ["Consents Required", "President's appointment order", "President's consent + HC CJ consultation", "President's consent + Person's consent"],
          ["Judge Status", "Full Acting Chief Justice of India", "Enjoys powers/privileges of SC judge during tenure", "Enjoys powers/privileges BUT NOT deemed a SC judge"]
        ],
        "rows_ta": [
          ["நியமிக்கும் அதிகாரி", "இந்தியக் குடியரசுத் தலைவர்", "இந்தியத் தலைமை நீதிபதி (குடியரசுத் தலைவர் முன்-ஒப்புதலுடன்)", "இந்தியத் தலைமை நீதிபதி (குடியரசுத் தலைவர் முன்-ஒப்புதலுடன்)"],
          ["தகுதியான நபர்", "ஏற்கனவே உள்ள உச்ச நீதிமன்ற நீதிபதி", "தகுதியுள்ள உயர் நீதிமன்ற நீதிபதி", "ஓய்வு பெற்ற SC அல்லது HC நீதிபதி"],
          ["முதன்மை காரணம்", "CJI பதவி காலியாக உள்ள போது, வராத போது அல்லது கடமை செய்ய இயலாத போது", "SC-ல் நிலையான நீதிபதிகளின் கணப்போர்வு (Quorum) பற்றாக்குறை", "தற்காலிக பணிச்சுமை அல்லது சிறப்பு வழக்குகள்"],
          ["தேவைப்படும் ஒப்புதல்கள்", "குடியரசுத் தலைவரின் நியமன ஆணை", "குடியரசுத் தலைவர் ஒப்புதல் + HC தலைமை நீதிபதி ஆலோசனை", "குடியரசுத் தலைவர் ஒப்புதல் + சம்மந்தப்பட்ட நபர் ஒப்புதல்"],
          ["நீதிபதி நிலை", "முழு தற்காலிக இந்தியத் தலைமை நீதிபதி", "பதவிக்காலத்தில் SC நீதிபதியின் அனைத்து அதிகாரங்களையும் அனுபவிப்பார்", "அதிகாரங்களை அனுபவிப்பார் ஆனால் SC நீதிபதியாகக் கருதப்பட மாட்டார்"]
        ]
      }
    ],
    "mind_map": [
      {
        "title": "Supreme Court Structure, Judges & Independence (Part V)",
        "short_label": "Supreme Court Part 1",
        "children": [
          {
            "title": "1. Constitutional Basis & Composition (Arts 124, 125, 130)",
            "short_label": "Basis & Composition",
            "children": [
              {"title": "Part V Chap IV (Arts 124-147); Art 130 Seat in Delhi", "short_label": "Part V"},
              {"title": "Current Strength: 34 (1 CJI + 33 Judges); Art 125 Salaries by Parliament", "short_label": "Strength 34"}
            ]
          },
          {
            "title": "2. Appointment & Collegium Evolution",
            "short_label": "Appointment",
            "children": [
              {"title": "Art 124(2): Appointed by President; CJI consultation compulsory", "short_label": "Art 124(2)"},
              {"title": "Collegium: CJI + 4 Senior Judges (3rd Judges 1998); NJAC struck down (4th Judges 2015)", "short_label": "Collegium"}
            ]
          },
          {
            "title": "3. Qualifications, Tenure & Removal",
            "short_label": "Qualifications & Removal",
            "children": [
              {"title": "Qualifications: Citizen + 5 yrs HC Judge OR 10 yrs HC Advocate OR Distinguished Jurist", "short_label": "Quals"},
              {"title": "Tenure: Retires at 65 yrs; Resigns to President", "short_label": "Age 65"},
              {"title": "Removal (Art 124(4)): Special Majority in Parliament on Proved Misbehaviour / Incapacity (Judges Inquiry Act 1968)", "short_label": "Removal"}
            ]
          },
          {
            "title": "4. Special Judges & Independence",
            "short_label": "Special Judges & Independence",
            "children": [
              {"title": "Acting CJI (Art 126), Ad Hoc (Art 127 - Quorum), Retired (Art 128)", "short_label": "Special Judges"},
              {"title": "Independence: Charged expenses (Art 146), Discussion ban (Art 121), Practice ban (Art 124(7)), DPSP Art 50", "short_label": "Independence"}
            ]
          }
        ]
      }
    ],
    "tnpsc_traps": [
      {
        "title": "1. Parliament Judge Strength Authority Trap (நீதிபதிகள் எண்ணிக்கை அதிகாரம் பற்றிய பொறி)",
        "points": {
          "en": [
            "TRAP: Believing the President or Supreme Court itself has the authority to increase the number of Supreme Court judges.",
            "FACT: Under Article 124(1), ONLY PARLIAMENT HAS THE AUTHORITY TO INCREASE THE NUMBER OF SUPREME COURT JUDGES BY LAW!"
          ],
          "ta": [
            "பொறி: உச்ச நீதிமன்ற நீதிபதிகளின் எண்ணிக்கையை உயர்த்த குடியரசுத் தலைவருக்கோ உச்ச நீதிமன்றத்திற்கோ அதிகாரம் உள்ளது என நினைப்பது.",
            "உண்மை: உறுப்பு 124(1)-ன் கீழ் நாடாளுமன்றத்திற்கு மட்டுமே சட்டம் இயற்றி உச்ச நீதிமன்ற நீதிபதிகளின் எண்ணிக்கையை உயர்த்த அதிகாரமுண்டு!"
          ]
        }
      },
      {
        "title": "2. Collegium Word Mention Trap ('கொலீஜியம்' சொல் பற்றிய பொறி)",
        "points": {
          "en": [
            "TRAP: Assuming the word 'Collegium' is directly defined in Article 124 of the Constitution.",
            "FACT: The word 'Collegium' DOES NOT appear anywhere in the text of the Constitution of India! It is a judicially evolved mechanism."
          ],
          "ta": [
            "பொறி: 'கொலீஜியம்' என்ற சொல் அரசியலமைப்பின் உறுப்பு 124-ல் நேரடியாக வரையறுக்கப்பட்டுள்ளது என நினைப்பது.",
            "உண்மை: 'கொலீஜியம்' என்ற சொல் இந்திய அரசியலமைப்பு உரையில் எங்குமே இல்லை!"
          ]
        }
      },
      {
        "title": "3. Retirement Age Confusion Trap (ஓய்வு பெறும் வயதுக் குழப்பப் பொறி)",
        "points": {
          "en": [
            "TRAP: Confusing the retirement age of Supreme Court judges with High Court judges.",
            "FACT: Supreme Court judges retire upon attaining the age of 65 YEARS (Article 124(2)), whereas High Court judges retire at 62 YEARS (Article 217)."
          ],
          "ta": [
            "பொறி: உச்ச நீதிமன்ற நீதிபதிகளின் ஓய்வு பெறும் வயதை உயர் நீதிமன்ற நீதிபதிகளுடன் குழப்பிக் கொள்ளுதல்.",
            "உண்மை: உச்ச நீதிமன்ற நீதிபதிகள் 65 வயதில் ஓய்வு பெறுகின்றனர் (உறுப்பு 124(2)), அதே வேளையில் உயர் நீதிமன்ற நீதிபதிகள் 62 வயதில் ஓய்வு பெறுகின்றனர்."
          ]
        }
      },
      {
        "title": "4. Ad Hoc Judge Appointing Authority Trap (தற்காலிக நீதிபதி நியமன அதிகாரிப் பொறி)",
        "points": {
          "en": [
            "TRAP: Thinking the President appoints Ad Hoc judges of the Supreme Court.",
            "FACT: Under Article 127, the CHIEF JUSTICE OF INDIA appoints Ad Hoc judges when there is a lack of quorum."
          ],
          "ta": [
            "பொறி: உச்ச நீதிமன்றத் தற்காலிக நீதிபதிகளைக் (Ad Hoc) குடியரசுத் தலைவர் நியமிக்கிறார் என நினைப்பது.",
            "உண்மை: உறுப்பு 127-ன் கீழ் கணப்போர்வு பற்றாக்குறை ஏற்படும் போது இந்தியத் தலைமை நீதிபதியே தற்காலிக நீதிபதிகளை நியமிக்கிறார்."
          ]
        }
      },
      {
        "title": "5. Removal History Trap (நீக்க வரலாறு பற்றிய பொறி)",
        "points": {
          "en": [
            "TRAP: Believing that several Supreme Court judges have been impeached and removed from office in India.",
            "FACT: NO Supreme Court judge has been removed / impeached so far in Indian history!"
          ],
          "ta": [
            "பொறி: இந்தியாவில் பல உச்ச நீதிமன்ற நீதிபதிகள் பதவி நீக்கம் செய்யப்பட்டுள்ளனர் என நினைப்பது.",
            "உண்மை: இந்திய வரலாற்றில் இதுவரை எந்தவொரு உச்ச நீதிமன்ற நீதிபதியும் பதவியிலிருந்து நீக்கப்படவில்லை!"
          ]
        }
      }
    ],
    "quick_revision": {
      "en": [
        "Constitutional Basis: Part V Chapter IV (Articles 124 to 147). Inaugurated Jan 28, 1950. Article 130 defines Seat of SC in Delhi.",
        "Composition & Salaries: Article 124 (34 Judges: 1 CJI + 33 Judges). Article 125 (Salaries determined by Parliament by law, 2nd Schedule).",
        "Appointment & Collegium: Appointed by President (Art 124(2)). Collegium (CJI + 4 senior SC judges) evolved via 1st, 2nd, 3rd Judges cases.",
        "Qualifications & Tenure: Article 124(3) Citizen + (5 yrs HC Judge OR 10 yrs HC Advocate OR Distinguished Jurist). Retires at 65 YEARS.",
        "Removal (Art 124(4)): Order of President after Parliamentary Special Majority Address. Judges Inquiry Act 1968.",
        "Special Judges: Article 126 (Acting CJI), Article 127 (Ad Hoc Judges for Quorum), Article 128 (Retired Judges).",
        "Independence: Article 121 (Conduct discussion ban), Article 124(7) (Practice ban), Article 129 (Contempt), Article 146 (Charged expenses), Article 50 DPSP."
      ],
      "ta": [
        "அரசியலமைப்பு அடிப்படை: பகுதி V அத்தியாயம் IV (உறுப்புகள் 124 முதல் 147). 1950 ஜனவரி 28. உறுப்பு 130 டெல்லியில் அமர்வை வரையறுக்கிறது.",
        "அமைப்பு & சம்பளங்கள்: உறுப்பு 124 (34 நீதிபதிகள்: 1 CJI + 33 நீதிபதிகள்). உறுப்பு 125 (சம்பளங்கள் நாடாளுமன்றச் சட்டத்தால்).",
        "நியமனம் & கொலீஜியம்: குடியரசுத் தலைவரால் நியமனம் (விதி 124(2)). கொலீஜியம் (CJI + 4 மூத்த நீதிபதிகள்).",
        "தகுதிகள் & பதவிக்காலம்: உறுப்பு 124(3) குடிமகன் + (5 ஆண்டுகள் HC நீதிபதி அல்லது 10 ஆண்டுகள் HC வழக்கறிஞர் அல்லது சிறப்புமிக்க சட்ட நிபுணர்). 65 வயதில் ஓய்வு.",
        "நீக்கம் (விதி 124(4)): நாடாளுமன்றச் சிறப்பு பெரும்பான்மைக்குப் பின் குடியரசுத் தலைவர் ஆணை. 1968 சட்டம்.",
        "சிறப்பு நீதிபதிகள்: உறுப்பு 126 (தற்காலிக CJI), உறுப்பு 127 (தற்காலிக நீதிபதிகள்), உறுப்பு 128 (ஓய்வு பெற்ற நீதிபதிகள்).",
        "சுதந்திரம்: உறுப்பு 121 (விவாதத் தடை), உறுப்பு 124(7) (பயிற்சித் தடை), உறுப்பு 129 (அவமதிப்பு), உறுப்பு 146 (சுமத்தப்பட்ட செலவுகள்), உறுப்பு 50 DPSP."
      ]
    },
    "must_remember": {
      "en": [
        "MUST REMEMBER: Current strength of Supreme Court is 34 (1 CJI + 33 Judges) as per 2019 Act.",
        "MUST REMEMBER: Article 125 governs salaries and service conditions of SC judges.",
        "MUST REMEMBER: Article 130 specifies Delhi as the seat of Supreme Court.",
        "MUST REMEMBER: Article 126 governs appointment of Acting Chief Justice.",
        "MUST REMEMBER: Article 127 governs appointment of Ad Hoc Judges by CJI for quorum.",
        "MUST REMEMBER: Article 128 governs attendance of retired judges.",
        "MUST REMEMBER: Article 146 provides that administrative expenses of SC are charged on Consolidated Fund.",
        "MUST REMEMBER: SC judges retire at age 65 (HC judges retire at 62).",
        "MUST REMEMBER: Removal of SC judge requires SPECIAL MAJORITY in each House of Parliament (Art 124(4)).",
        "MUST REMEMBER: NO Supreme Court judge has been removed / impeached in India so far."
      ],
      "ta": [
        "நினைவில் கொள்க: 2019 திருத்தச் சட்டத்தின் படி உச்ச நீதிமன்றத்தின் தற்போதைய எண்ணிக்கை 34.",
        "நினைவில் கொள்க: உறுப்பு 125 SC நீதிபதிகளின் சம்பளங்கள் மற்றும் சேவை நிபந்தனைகளை ஒழுங்குபடுத்துகிறது.",
        "நினைவில் கொள்க: உறுப்பு 130 டெல்லியை உச்ச நீதிமன்றத்தின் அமர்வு இடமாகக் குறிப்பிடுகிறது.",
        "நினைவில் கொள்க: உறுப்பு 126 தற்காலிக தலைமை நீதிபதி நியமனத்தை ஒழுங்குபடுத்துகிறது.",
        "நினைவில் கொள்க: உறுப்பு 127 கணப்போர்விற்கு CJI தற்காலிக நீதிபதிகள் நியமிப்பதை ஒழுங்குபடுத்துகிறது.",
        "நினைவில் கொள்க: உறுப்பு 128 ஓய்வு பெற்ற நீதிபதிகள் வருகையை ஒழுங்குபடுத்துகிறது.",
        "நினைவில் கொள்க: உறுப்பு 146 உச்ச நீதிமன்ற நிர்வாகச் செலவுகள் இந்தியத் தொகுப்பு நிதியில் சுமத்தப்பட்டவை எனக்கூறுகிறது.",
        "நினைவில் கொள்க: SC நீதிபதிகள் 65 வயதில் ஓய்வு பெறுகின்றனர் (HC நீதிபதிகள் 62 வயதில்).",
        "நினைவில் கொள்க: SC நீதிபதியை நீக்க நாடாளுமன்றத்தில் சிறப்பு பெரும்பான்மை தேவை (விதி 124(4)).",
        "நினைவில் கொள்க: இந்தியாவில் இதுவரை எந்தவொரு உச்ச நீதிமன்ற நீதிபதியும் பதவியிலிருந்து நீக்கப்படவில்லை."
      ]
    }
  }
}

target_file = "data/notes/polity/supreme_court_part_1.json"
os.makedirs("data/notes/polity", exist_ok=True)

with open(target_file, "w", encoding="utf-8") as f:
  json.dump(part1_data, f, ensure_ascii=False, indent=2)

print(f"✅ Supreme Court Part 1 updated with Articles 124, 125, 126, 127, 128, 129, 130, 146 tags and saved to: {target_file}")
