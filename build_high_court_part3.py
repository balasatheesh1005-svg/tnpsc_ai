# -*- coding: utf-8 -*-
"""
Builder Script for High Courts in India Notes — Part 3
Subject: Indian Polity
Topic: High Courts in India – Part 3 (Advanced High Court Concepts)
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("==================================================")
print("BUILDING HIGH COURT NOTES — PART 3")
print("==================================================")

part3_data = {
  "meta": {
    "topic_id": "polity_high_court_part_3",
    "repository_id": "polity_high_court",
    "display_title": "High Courts in India – Part 3",
    "part": 3,
    "total_parts": 3,
    "subject": "polity",
    "chapter": "High Courts in India",
    "language": "English + Tamil"
  },
  "metadata": {
    "topic_id": "polity_high_court_part_3",
    "repository_id": "polity_high_court",
    "display_title": "High Courts in India – Part 3",
    "part": 3,
    "total_parts": 3,
    "subject": "polity",
    "chapter": "High Courts in India",
    "language": "English + Tamil"
  },
  "keywords": [
    "Common High Courts",
    "Article 231",
    "Article 230 UT Jurisdiction",
    "Article 229 Officers and Staff",
    "Article 235 Control Subordinate Courts",
    "25 High Courts in India",
    "Andhra Pradesh High Court 2019",
    "Delhi High Court UT",
    "Bombay High Court Common",
    "Gauhati High Court Common",
    "Punjab and Haryana High Court",
    "Calcutta High Court A&N Islands",
    "Madras High Court Puducherry",
    "Kerala High Court Lakshadweep",
    "Article 227 vs Article 235",
    "Landmark High Court Cases",
    "Shamsher Singh Case 1974",
    "TNPSC Master Polity Notes"
  ],
  "learning_outcomes": {
    "Understand": {
      "en": [
        "Master Common High Courts under Article 231 (7th Amend 1956) and UT jurisdiction under Article 230. Know that India currently has 25 High Courts.",
        "Master High Court Control over Subordinate Judiciary under Article 235 (posting, promotion, leave, and discipline vested in High Court).",
        "Understand Article 229 (Administrative independence & Chief Justice authority to appoint HC staff without executive interference).",
        "Deeply synthesize key comparisons: Article 226 vs 32, Article 226 vs 227, Article 227 vs 235, and High Court vs Supreme Court.",
        "Master the 7 Common High Courts in India and Union Territory arrangements (Only Delhi UT has its own separate High Court established 1966).",
        "Understand Landmark Constitutional Cases: Shamsher Singh (1974), L. Chandra Kumar (1997), and K. Ashok Reddy (1994)."
      ],
      "ta": [
        "உறுப்பு 231-ன் கீழ் பொது உயர் நீதிமன்றங்கள் (1956 7-வது திருத்தம்) மற்றும் உறுப்பு 230-ன் கீழ் UT அதிகார வரம்பில் தேர்ச்சி பெறுதல். இந்தியாவில் தற்போது 25 உயர் நீதிமன்றங்கள் உள்ளன என்பதை அறிதல்.",
        "உறுப்பு 235-ன் கீழ் சார்பு நீதிமன்றங்கள் மீதான உயர் நீதிமன்றக் கட்டுப்பாடு (பணியமர்த்தல், உயர்வு, விடுப்பு, ஒழுங்கு நடவடிக்கை HC வசம்).",
        "உறுப்பு 229 (நிர்வாக சுதந்திரம் & நிர்வாகத் தலையீடின்றி ஊழியர்களை நியமிக்க HC தலைமை நீதிபதியின் அதிகாரம்) ஆகியவற்றைப் புரிந்துகொள்ளுதல்.",
        "முக்கிய ஒப்பீடுகளை விரிவாகத் தொகுத்தல்: விதி 226 vs 32, விதி 226 vs 227, விதி 227 vs 235 மற்றும் உயர் நீதிமன்றம் vs உச்ச நீதிமன்றம்.",
        "இந்தியாவில் உள்ள 7 பொது உயர் நீதிமன்றங்கள் மற்றும் யூனியன் பிரதேச அமைப்புகள் (டெல்லி UT மட்டுமே தனது சொந்த தனி HC கொண்டுள்ளது - 1966).",
        "வரலாற்றுச் சிறப்புமிக்க அரசியலமைப்பு வழக்குகள்: சம்ஷேர் சிங் (1974), எல். சந்திரகுமார் (1997), கே. அசோக் ரெட்டி (1994)."
      ]
    }
  },
  "subject": "polity",
  "topic": "High Courts in India",
  "language": "English + Tamil",
  "ui_type": "standard_notes",
  "sections": [
    {
      "id": "sec_common_hcs_art231",
      "title_en": "1. Common High Courts & UT Jurisdiction (Articles 230, 231 & 25 HCs)",
      "title_ta": "1. பொது உயர் நீதிமன்றங்கள் & UT அதிகார வரம்பு (உறுப்புகள் 230, 231 & 25 HCs)",
      "type": "standard_topic"
    },
    {
      "id": "sec_subordinate_control_art235",
      "title_en": "2. Article 235 — Control over Subordinate Judiciary",
      "title_ta": "2. உறுப்பு 235 — சார்பு நீதிமன்றங்கள் மீதான கட்டுப்பாடு",
      "type": "standard_topic"
    },
    {
      "id": "sec_staff_independence_art229",
      "title_en": "3. Article 229 — Officers, Servants & Administrative Independence",
      "title_ta": "3. உறுப்பு 229 — அதிகாரிகள், ஊழியர்கள் & நிர்வாக சுதந்திரம்",
      "type": "standard_topic"
    },
    {
      "id": "sec_synthesis_comparisons",
      "title_en": "4. Deep Synthesis of High Court Key Constitutional Comparisons",
      "title_ta": "4. உயர் நீதிமன்ற முக்கிய அரசியலமைப்பு ஒப்பீடுகளின் விரிவான தொகுப்பு",
      "type": "standard_topic"
    },
    {
      "id": "sec_landmark_cases_hc",
      "title_en": "5. Summary of Landmark High Court Cases & Principles",
      "title_ta": "5. வரலாற்றுச் சிறப்புமிக்க உயர் நீதிமன்ற வழக்குகள் & கோட்பாடுகளின் சுருக்கம்",
      "type": "standard_topic"
    },
    {
      "id": "comparison_tables",
      "title_en": "6. Mandatory Advanced Comparison Tables (10 Tables)",
      "title_ta": "6. கட்டாய மேம்பட்ட ஒப்பீட்டு அட்டவணைகள் (10 அட்டவணைகள்)",
      "type": "comparison"
    },
    {
      "id": "mind_map",
      "title_en": "7. Mind Map & TNPSC Trap Points",
      "title_ta": "7. மன வரைபடம் & டிஎன்பிஎஸ்சி பொறிப் புள்ளிகள்",
      "type": "mind_map"
    }
  ],
  "content": {
    "definition": {
      "en": "Advanced High Court concepts encompass Article 231 (Establishment of Common High Courts), Article 230 (Extension of HC jurisdiction to Union Territories), Article 235 (HC control over subordinate judiciary), Article 229 (Administrative staff independence), structural distribution across 25 High Courts, and judicial independence safeguards.",
      "ta": "மேம்பட்ட உயர் நீதிமன்றக் கோட்பாடுகள் என்பது உறுப்பு 231 (பொது உயர் நீதிமன்றங்கள் அமைப்பு), உறுப்பு 230 (யூனியன் பிரதேசங்களுக்கு அதிகார வரம்பு விரிவாக்கம்), உறுப்பு 235 (சார்பு நீதிமன்றங்கள் மீதான HC கட்டுப்பாடு), உறுப்பு 229 (நிர்வாக ஊழியர்கள் சுதந்திரம்) மற்றும் 25 உயர் நீதிமன்றங்களின் அமைப்புகளை உள்ளடக்கியது."
    },
    "introduction": {
      "en": "India currently has 25 High Courts for 28 States and 8 Union Territories. While Article 214 mandates a High Court for each State, Article 231 empowers Parliament to establish a Common High Court for two or more States/UTs. Article 235 vests administrative and disciplinary control over subordinate courts in the High Court.",
      "ta": "இந்தியாவில் தற்போது 28 மாநிலங்கள் மற்றும் 8 யூனியன் பிரதேசங்களுக்கு 25 உயர் நீதிமன்றங்கள் உள்ளன. உறுப்பு 214 ஒவ்வொரு மாநிலத்திற்கும் ஒரு HC என்கிறது, ஆனால் உறுப்பு 231 நாடாளுமன்றம் பொது உயர் நீதிமன்றத்தை அமைக்க அதிகாரமளிக்கிறது. உறுப்பு 235 சார்பு நீதிமன்றங்களின் கட்டுப்பாட்டை உயர் நீதிமன்றத்திற்கு அளிக்கிறது."
    },
    "sec_common_hcs_art231": [
      {
        "title_en": "Articles 230 & 231 — Common High Courts & UT Jurisdiction (25 HCs Total)",
        "title_ta": "உறுப்புகள் 230 & 231 — பொது உயர் நீதிமன்றங்கள் & UT அதிகார வரம்பு (மொத்தம் 25 HCs)",
        "points": {
          "en": [
            "Constitutional Provision (Article 231): Added by 7th Amendment 1956. PARLIAMENT MAY BY LAW ESTABLISH A COMMON HIGH COURT for two or more States or States and a Union Territory.",
            "UT Jurisdiction (Article 230): Parliament may by law extend or exclude High Court jurisdiction with respect to any Union Territory.",
            "Total High Courts in India: CURRENTLY 25 HIGH COURTS in India. The 25th High Court is the Andhra Pradesh High Court at Amaravati (established Jan 1, 2019 following bifurcation of Telangana HC).",
            "Union Territory High Court Rule: ONLY ONE Union Territory has a separate High Court of its own — DELHI HIGH COURT (established 1966).",
            "List of Common High Courts & Jurisdictions:",
            "  1. Bombay High Court: Maharashtra, Goa, Dadra & Nagar Haveli and Daman & Diu.",
            "  2. Gauhati High Court: Assam, Nagaland, Mizoram, Arunachal Pradesh (4 States).",
            "  3. Punjab & Haryana High Court: Punjab, Haryana, Chandigarh (UT).",
            "  4. Calcutta High Court: West Bengal, Andaman & Nicobar Islands (UT).",
            "  5. Madras High Court: Tamil Nadu, Puducherry (UT).",
            "  6. Kerala High Court: Kerala, Lakshadweep (UT).",
            "  7. Jammu & Kashmir and Ladakh High Court: Common HC for UT of J&K and UT of Ladakh."
          ],
          "ta": [
            "அரசியலமைப்பு விதி (உறுப்பு 231): 1956 7-வது திருத்தத்தால் சேர்க்கப்பட்டது. இரண்டு அல்லது அதற்கு மேற்பட்ட மாநிலங்கள் / யூனியன் பிரதேசங்களுக்கு நாடாளுமன்றம் சட்டம் இயற்றிப் பொது உயர் நீதிமன்றத்தை அமைக்கலாம்.",
            "UT அதிகார வரம்பு (உறுப்பு 230): யூனியன் பிரதேசங்களுக்கு உயர் நீதிமன்ற அதிகார வரம்பை நீட்டிக்கவோ விலக்கவோ நாடாளுமன்றத்திற்கு சட்ட அதிகாரம் உண்டு.",
            "இந்தியாவில் மொத்த உயர் நீதிமன்றங்கள்: தற்போது இந்தியாவில் 25 உயர் நீதிமன்றங்கள் உள்ளன. 25-வது உயர் நீதிமன்றம் அமராவதியில் உள்ள ஆந்திரப் பிரதேச உயர் நீதிமன்றமாகும் (2019 ஜனவரி 1).",
            "யூனியன் பிரதேச விதி: டெல்லி யூனியன் பிரதேசம் மட்டுமே தனது சொந்த தனி உயர் நீதிமன்றத்தைக் (1966) கொண்டுள்ளது.",
            "பொது உயர் நீதிமன்றங்கள் பட்டியல்:",
            "  1. பாம்பே உயர் நீதிமன்றம்: மகாராஷ்டிரா, கோவா, தாத்ரா & நகர் ஹவேலி மற்றும் தாமன் & தியூ.",
            "  2. கௌஹாத்தி உயர் நீதிமன்றம்: அசாம், நாகாலாந்து, மிசோரம், அருணாச்சலப் பிரதேசம் (4 மாநிலங்கள்).",
            "  3. பஞ்சாப் & ஹரியானா உயர் நீதிமன்றம்: பஞ்சாப், ஹரியானா, சண்டிகர் (UT).",
            "  4. கல்கத்தா உயர் நீதிமன்றம்: மேற்கு வங்கம், அந்தமான் & நிக்கோபார் தீவுகள் (UT).",
            "  5. மதராஸ் உயர் நீதிமன்றம்: தமிழ்நாடு, புதுச்சேரி (UT).",
            "  6. கேரளா உயர் நீதிமன்றம்: கேரளா, இலட்சத்தீவுகள் (UT).",
            "  7. ஜம்மு & காஷ்மீர் மற்றும் லடாக் உயர் நீதிமன்றம்: J&K மற்றும் லடாக் UT-களுக்கான பொது நீதிமன்றம்."
          ]
        }
      }
    ],
    "sec_subordinate_control_art235": [
      {
        "title_en": "Article 235 — High Court Control over Subordinate Judiciary",
        "title_ta": "உறுப்பு 235 — சார்பு நீதிமன்றங்கள் மீதான உயர் நீதிமன்றக் கட்டுப்பாடு",
        "points": {
          "en": [
            "Vesting of Control (Article 235): The control over district courts and courts subordinate thereto, including the posting and promotion of, and the grant of leave to, persons belonging to the judicial service of a State and holding any post inferior to the post of district judge SHALL BE VESTED IN THE HIGH COURT.",
            "Scope of Control under Art 235: High Court holds complete administrative and disciplinary control over subordinate judicial officers (transfers, postings, promotions, leave, disciplinary inquiries, and recommendations for compulsory retirement).",
            "Shamsher Singh v. State of Punjab (1974): Supreme Court ruled that the control vested in the High Court under Article 235 is COMPLETE AND EXCLUSIVE. Executive Government CANNOT interfere in disciplinary proceedings or transfers of judicial officers."
          ],
          "ta": [
            "கட்டுப்பாடு அளித்தல் (உறுப்பு 235): மாவட்ட நீதிமன்றங்கள் மற்றும் சார்பு நீதிமன்றங்களின் பணி ஒதுக்கீடு, பதவி உயர்வு, விடுப்பு வழங்குதல் மற்றும் ஒழுங்கு நடவடிக்கைகள் அனைத்தும் உயர் நீதிமன்றத்தின் வசம் மட்டுமே இருக்கும்.",
            "விதி 235 கட்டுப்பாட்டின் எல்லை: சார்பு நீதித்துறை அதிகாரிகள் மீது உயர் நீதிமன்றம் முழுமையான நிர்வாக மற்றும் ஒழுங்கு நடவடிக்கைக் கட்டுப்பாடு கொண்டுள்ளது.",
            "சம்ஷேர் சிங் v. பஞ்சாப் மாநிலம் (1974): உறுப்பு 235-ன் கீழ் உயர் நீதிமன்றத்திற்கு வழங்கப்பட்ட கட்டுப்பாடு முற்றுரிமையானது மற்றும் முழுமையானது என உச்ச நீதிமன்றம் தீர்ப்பளித்தது. நிர்வாக அரசு இதில் தலையிட முடியாது."
          ]
        }
      }
    ],
    "sec_staff_independence_art229": [
      {
        "title_en": "Article 229 — Officers, Servants & Administrative Independence",
        "title_ta": "உறுப்பு 229 — அதிகாரிகள், ஊழியர்கள் & நிர்வாக சுதந்திரம்",
        "points": {
          "en": [
            "Staff Appointing Authority (Article 229(1)): Appointments of officers and servants of a High Court SHALL BE MADE BY THE CHIEF JUSTICE OF THE HIGH COURT or such other judge/officer of the Court as he may direct.",
            "Service Conditions (Article 229(2)): Conditions of service of officers and servants of a High Court shall be prescribed by rules made by the Chief Justice of the High Court (rules relating to salaries/pensions require approval of State Governor).",
            "Charged Expenses (Article 229(3)): Administrative expenses of the High Court, including salaries, allowances, and pensions payable to officers/servants, SHALL BE CHARGED UPON THE CONSOLIDATED FUND OF THE STATE (non-votable by State Assembly)."
          ],
          "ta": [
            "ஊழியர்கள் நியமன அதிகாரி (உறுப்பு 229(1)): உயர் நீதிமன்றத்தின் அதிகாரிகள் மற்றும் ஊழியர்களின் நியமனங்கள் உயர் நீதிமன்றத் தலைமை நீதிபதியால் (அல்லது அவரால் நியமிக்கப்பட்ட அதிகாரியால்) செய்யப்பட வேண்டும்.",
            "சேவை நிபந்தனைகள் (உறுப்பு 229(2)): சேவை நிபந்தனைகள் தலைமை நீதிபதியால் உருவாக்கப்படும் விதிகளால் நிர்ணயிக்கப்படும் (சம்பளம் தொடர்பான விதிகளுக்கு ஆளுநர் ஒப்புதல் தேவை).",
            "சுமத்தப்பட்ட செலவுகள் (உறுப்பு 229(3)): உயர் நீதிமன்ற நிர்வாகச் செலவுகள் மற்றும் ஊழியர்களின் சம்பளங்கள் மாநிலத் தொகுப்பு நிதியில் சுமத்தப்பட்டவை (மாநிலச் சட்டமன்ற வாக்கெடுப்பிற்கு அப்பாற்பட்டவை)."
          ]
        }
      }
    ],
    "sec_synthesis_comparisons": [
      {
        "title_en": "Deep Synthesis of High Court Key Constitutional Comparisons",
        "title_ta": "உயர் நீதிமன்ற முக்கிய அரசியலமைப்பு ஒப்பீடுகளின் விரிவான தொகுப்பு",
        "points": {
          "en": [
            "1. Article 226 vs Article 32: Art 226 is WIDER in subject matter (FRs + other legal rights), whereas Art 32 applies ONLY for FRs. Art 32 IS ITSELF a Fundamental Right; Art 226 is a constitutional remedy.",
            "2. Article 226 vs Article 227: Art 226 is Writ Jurisdiction (primarily judicial relief); Art 227 is Supervisory Jurisdiction (covers judicial + administrative control over lower courts/tribunals).",
            "3. Article 227 vs Article 235: Art 227 provides general superintendence over ALL courts/tribunals in territory; Art 235 provides specific administrative & disciplinary control over SUBORDINATE JUDICIAL OFFICERS (postings, promotions, leave).",
            "4. High Court vs Supreme Court: SC strength determined by Parliament (Art 124(1)); HC strength determined by President (Art 216). SC judge retires at 65; HC judge retires at 62.",
            "5. Constitutional Text vs Collegium Practice: Art 217 text mentions consultation with CJI, Governor & HC CJ; Collegium practice (CJI + 2 senior SC judges) was judicially evolved."
          ],
          "ta": [
            "1. உறுப்பு 226 vs உறுப்பு 32: விதி 226 பாட எல்லையில் பரந்தது (அடிப்படை உரிமைகள் + பிற சட்ட உரிமைகள்), விதி 32 அடிப்படை உரிமைகளுக்கு மட்டுமே. விதி 32 தானே அடிப்படை உரிமை; விதி 226 பரிகார விதி.",
            "2. உறுப்பு 226 vs உறுப்பு 227: விதி 226 பேராணை ஆதிக்கம்; விதி 227 மேற்பார்வை ஆதிக்கம் (நீதித்துறை + நிர்வாகக் கட்டுப்பாடு).",
            "3. உறுப்பு 227 vs உறுப்பு 235: விதி 227 அனைத்து கீழ் நீதிமன்றங்கள்/தீர்ப்பாயங்கள் மீதான பொதுவான மேற்பார்வை; விதி 235 சார்பு நீதித்துறை அதிகாரிகள் மீதான குறிப்பிட்ட நிர்வாக & ஒழுங்கு நடவடிக்கைக் கட்டுப்பாடு.",
            "4. உயர் நீதிமன்றம் vs உச்ச நீதிமன்றம்: SC எண்ணிக்கை நாடாளுமன்றத்தால் தீர்மானிக்கப்படுகிறது; HC எண்ணிக்கை குடியரசுத் தலைவரால் தீர்மானிக்கப்படுகிறது. SC நீதிபதி 65 வயதில், HC நீதிபதி 62 வயதில் ஓய்வு பெறுகின்றனர்.",
            "5. அரசியலமைப்பு உரை vs கொலீஜியம் நடைமுறை: விதி 217 உரை CJI, ஆளுநர் & HC தலைமை நீதிபதி ஆலோசனையைக் குறிப்பிடுகிறது; கொலீஜியம் நடைமுறை நீதித்துறையால் உருவாக்கப்பட்டது."
          ]
        }
      }
    ],
    "sec_landmark_cases_hc": [
      {
        "title_en": "Summary of Landmark High Court Cases & Principles",
        "title_ta": "வரலாற்றுச் சிறப்புமிக்க உயர் நீதிமன்ற வழக்குகள் & கோட்பாடுகளின் சுருக்கம்",
        "points": {
          "en": [
            "1. Indian High Courts Act 1861: Authorized creation of first 3 High Courts in 1862 at Calcutta, Bombay, and Madras.",
            "2. Shamsher Singh v. State of Punjab (1974): Ruled that control over subordinate judiciary under Article 235 is vested exclusively in High Court, not Executive.",
            "3. K. Ashok Reddy v. Union of India (1994): Judicial transfer of High Court judges under Article 222 is subject to limited Judicial Review only to eliminate arbitrariness.",
            "4. L. Chandra Kumar v. Union of India (1997): Declared writ jurisdiction under Article 226 and supervisory jurisdiction under Article 227 as part of the BASIC STRUCTURE of the Constitution."
          ],
          "ta": [
            "1. 1861 இந்திய உயர் நீதிமன்றங்கள் சட்டம்: 1862-ல் கல்கத்தா, பாம்பே, மதராஸ் ஆகிய இடங்களில் முதல் 3 உயர் நீதிமன்றங்களை உருவாக்க அதிகாரமளித்தது.",
            "2. சம்ஷேர் சிங் v. பஞ்சாப் மாநிலம் (1974): உறுப்பு 235-ன் கீழ் சார்பு நீதிமன்றங்கள் மீதான கட்டுப்பாடு உயர் நீதிமன்றத்திற்கு மட்டுமே உரியது எனத் தீர்ப்பளித்தது.",
            "3. கே. அசோக் ரெட்டி v. யூனியன் ஆஃப் இந்தியா (1994): உறுப்பு 222-ன் கீழ் நீதிபதிகள் இடமாற்றம் தன்னிச்சையானதைத் தடுக்க மட்டுமே வரம்பிற்குட்பட்ட நீதித்துறை ஆய்வுக்கு உட்பட்டது.",
            "4. எல். சந்திரகுமார் v. யூனியன் ஆஃப் இந்தியா (1997): விதிகள் 226 மற்றும் 227 அரசியலமைப்பின் அடிப்படை அமைப்பின் (Basic Structure) பகுதி என அறிவித்தது."
          ]
        }
      }
    ],
    "revision_cards": [
      {
        "id": "hc_p3_c1",
        "front_en": "How many High Courts are there currently in India?",
        "front_ta": "இந்தியாவில் தற்போது எத்தனை உயர் நீதிமன்றங்கள் உள்ளன?",
        "back_en": "25 HIGH COURTS (25th is Andhra Pradesh High Court at Amaravati, est. Jan 1, 2019).",
        "back_ta": "25 உயர் நீதிமன்றங்கள் (25-வது அமராவதியில் உள்ள ஆந்திரப் பிரதேச உயர் நீதிமன்றம் - 2019 ஜனவரி 1)."
      },
      {
        "id": "hc_p3_c2",
        "front_en": "Which is the ONLY Union Territory in India that has a separate High Court of its own?",
        "front_ta": "தனக்கெனத் தனி உயர் நீதிமன்றத்தைக் கொண்டுள்ள ஒரே யூனியன் பிரதேசம் எது?",
        "back_en": "DELHI UNION TERRITORY (Delhi High Court established in 1966).",
        "back_ta": "டெல்லி யூனியன் பிரதேசம் (டெல்லி உயர் நீதிமன்றம் 1966-ல் அமைக்கப்பட்டது)."
      },
      {
        "id": "hc_p3_c3",
        "front_en": "Which Amendment authorized Parliament to establish a Common High Court for two or more States under Article 231?",
        "front_ta": "உறுப்பு 231-ன் கீழ் இரண்டு அல்லது அதற்கு மேற்பட்ட மாநிலங்களுக்கு பொது உயர் நீதிமன்றத்தை அமைக்க நாடாளுமன்றத்திற்கு அதிகாரமளித்த திருத்தம் எது?",
        "back_en": "7TH CONSTITUTIONAL AMENDMENT ACT 1956.",
        "back_ta": "1956 7-வது அரசியலமைப்புச் சட்டத்திருத்தம்."
      },
      {
        "id": "hc_p3_c4",
        "front_en": "Which Article vests control over subordinate courts (postings, promotions, leave) in the High Court?",
        "front_ta": "சார்பு நீதிமன்றங்கள் மீதான கட்டுப்பாட்டை (பணியமர்த்தல், உயர்வு, விடுப்பு) உயர் நீதிமன்றத்திற்கு அளிக்கும் உறுப்பு எது?",
        "back_en": "ARTICLE 235.",
        "back_ta": "உறுப்பு 235."
      },
      {
        "id": "hc_p3_c5",
        "front_en": "Who appoints the officers and servants of a High Court under Article 229(1)?",
        "front_ta": "உறுப்பு 229(1)-ன் கீழ் உயர் நீதிமன்ற அதிகாரிகள் மற்றும் ஊழியர்களை நியமிப்பவர் யார்?",
        "back_en": "CHIEF JUSTICE OF THE HIGH COURT (or judge/officer authorized by him).",
        "back_ta": "உயர் நீதிமன்றத் தலைமை நீதிபதி (அல்லது அவரால் நியமிக்கப்பட்ட அதிகாரி)."
      },
      {
        "id": "hc_p3_c6",
        "front_en": "Where are the administrative expenses of a High Court charged under Article 229(3)?",
        "front_ta": "உறுப்பு 229(3)-ன் கீழ் உயர் நீதிமன்ற நிர்வாகச் செலவுகள் எங்கு சுமத்தப்படுகின்றன?",
        "back_en": "Consolidated Fund of the STATE (non-votable by State Assembly).",
        "back_ta": "மாநிலத் தொகுப்பு நிதியில் (சட்டமன்ற வாக்கெடுப்பிற்கு அப்பாற்பட்டது)."
      },
      {
        "id": "hc_p3_c7",
        "front_en": "Which High Courts were first established in India in 1862 under the Indian High Courts Act 1861?",
        "front_ta": "1861 இந்திய உயர் நீதிமன்றங்கள் சட்டத்தின் கீழ் 1862-ல் இந்தியாவில் முதன்முதலில் அமைக்கப்பட்ட உயர் நீதிமன்றங்கள் எவை?",
        "back_en": "Calcutta, Bombay, and Madras High Courts.",
        "back_ta": "கல்கத்தா, பாம்பே மற்றும் மதராஸ் உயர் நீதிமன்றங்கள்."
      },
      {
        "id": "hc_p3_c8",
        "front_en": "Which High Court has jurisdiction over Lakshadweep UT?",
        "front_ta": "இலட்சத்தீவுகள் யூனியன் பிரதேசத்திற்கு எந்த உயர் நீதிமன்றம் அதிகார வரம்பு கொண்டுள்ளது?",
        "back_en": "KERALA HIGH COURT.",
        "back_ta": "கேரளா உயர் நீதிமன்றம்."
      },
      {
        "id": "hc_p3_c9",
        "front_en": "Which High Court has jurisdiction over Andaman and Nicobar Islands UT?",
        "front_ta": "அந்தமான் & நிக்கோபார் தீவுகளுக்கு எந்த உயர் நீதிமன்றம் அதிகார வரம்பு கொண்டுள்ளது?",
        "back_en": "CALCUTTA HIGH COURT.",
        "back_ta": "கல்கத்தா உயர் நீதிமன்றம்."
      },
      {
        "id": "hc_p3_c10",
        "front_en": "Which High Court has jurisdiction over Puducherry UT?",
        "front_ta": "புதுச்சேரி யூனியன் பிரதேசத்திற்கு எந்த உயர் நீதிமன்றம் அதிகார வரம்பு கொண்டுள்ளது?",
        "back_en": "MADRAS HIGH COURT.",
        "back_ta": "மதராஸ் உயர் நீதிமன்றம்."
      },
      {
        "id": "hc_p3_c11",
        "front_en": "What is the key difference between Article 227 and Article 235?",
        "front_ta": "உறுப்பு 227 மற்றும் உறுப்பு 235-க்கு இடையிலான முக்கிய வேறுபாடு என்ன?",
        "back_en": "Art 227 is general superintendence over lower courts/tribunals; Art 235 is specific administrative/disciplinary control over subordinate judicial officers.",
        "back_ta": "விதி 227 கீழ் நீதிமன்றங்கள் மீதான பொதுவான மேற்பார்வை; விதி 235 சார்பு நீதித்துறை அதிகாரிகள் மீதான குறிப்பிட்ட நிர்வாக & ஒழுங்கு நடவடிக்கைக் கட்டுப்பாடு."
      },
      {
        "id": "hc_p3_c12",
        "front_en": "Which landmark judgment ruled that control over subordinate judiciary under Article 235 is exclusive to High Court?",
        "front_ta": "உறுப்பு 235-ன் கீழ் சார்பு நீதிமன்றங்கள் மீதான கட்டுப்பாடு உயர் நீதிமன்றத்திற்கு மட்டுமே உரியது எனத் தீர்ப்பளித்த வழக்கு எது?",
        "back_en": "Shamsher Singh v. State of Punjab (1974).",
        "back_ta": "சம்ஷேர் சிங் v. பஞ்சாப் மாநிலம் (1974)."
      }
    ],
    "comparison_tables": [
      {
        "id": "tbl_hc_vs_sc_p3",
        "title_en": "1. Supreme Court vs High Court Comprehensive Comparison",
        "title_ta": "1. உச்ச நீதிமன்றம் vs உயர் நீதிமன்றம் விரிவான ஒப்பீடு",
        "headers_en": ["Feature / Dimension", "High Courts of States", "Supreme Court of India"],
        "headers_ta": ["அம்சம் / காரணி", "மாநில உயர் நீதிமன்றங்கள்", "இந்திய உச்ச நீதிமன்றம்"],
        "rows_en": [
          ["Constitutional Provisions", "Part VI Chapter V (Articles 214 to 231)", "Part V Chapter IV (Articles 124 to 147)"],
          ["Total Number", "25 High Courts in India", "1 Apex Supreme Court"],
          ["Strength Authority", "President of India determines strength (Art 216)", "Parliament of India determines strength by law (Art 124(1))"],
          ["Retirement Age", "62 Years (15th Amend 1963)", "65 Years"],
          ["Oath Administered By", "Governor of the State (Art 219)", "President of India (Art 124(6))"],
          ["Writ Scope (Art 226 vs 32)", "Fundamental Rights + Other legal rights (Wider)", "Fundamental Rights ONLY (Narrower)"]
        ],
        "rows_ta": [
          ["அரசியலமைப்பு விதிகள்", "பகுதி VI அத்தியாயம் V (உறுப்புகள் 214 முதல் 231)", "பகுதி V அத்தியாயம் IV (உறுப்புகள் 124 முதல் 147)"],
          ["மொத்த எண்ணிக்கை", "இந்தியாவில் 25 உயர் நீதிமன்றங்கள்", "1 உச்ச உச்ச நீதிமன்றம்"],
          ["எண்ணிக்கை அதிகாரம்", "குடியரசுத் தலைவர் தீர்மானிக்கிறார் (விதி 216)", "நாடாளுமன்றம் சட்டத்தால் தீர்மானிக்கிறது (விதி 124(1))"],
          ["ஓய்வு பெறும் வயது", "62 வயது (1963 15-வது திருத்தம்)", "65 வயது"],
          ["உறுதிமொழி வழங்குபவர்", "மாநில ஆளுநர் (விதி 219)", "இந்தியக் குடியரசுத் தலைவர் (விதி 124(6))"],
          ["பேராணை எல்லை (விதி 226 vs 32)", "அடிப்படை உரிமைகள் + பிற சட்ட உரிமைகள் (பரந்தது)", "அடிப்படை உரிமைகள் மட்டுமே (குறுகியது)"]
        ]
      },
      {
        "id": "tbl_art226_vs_art32_p3",
        "title_en": "2. Article 226 vs Article 32 Deep Comparison",
        "title_ta": "2. உறுப்பு 226 vs உறுப்பு 32 விரிவான ஒப்பீடு",
        "headers_en": ["Parameter", "Article 226 (High Courts)", "Article 32 (Supreme Court)"],
        "headers_ta": ["அளவுரு", "உறுப்பு 226 (உயர் நீதிமன்றங்கள்)", "உறுப்பு 32 (உச்ச நீதிமன்றம்)"],
        "rows_en": [
          ["Subject Matter Scope", "WIDER: Fundamental Rights AND 'any other legal purpose'", "NARROWER: Fundamental Rights ONLY"],
          ["Territorial Reach", "State / UT territorial limits (unless cause of action arises)", "Entire territory of India"],
          ["Fundamental Right Status", "Constitutional remedy (NOT ITSELF a Fundamental Right)", "IS ITSELF a Fundamental Right (Art 32)"],
          ["Refusal Power", "Discretionary (HC may refuse if alternative remedy exists)", "Mandatory (SC cannot refuse FR remedy)"],
          ["Basic Structure Status", "Part of Basic Structure (L. Chandra Kumar 1997)", "Part of Basic Structure (Kesavananda 1973)"]
        ],
        "rows_ta": [
          ["பாட எல்லை", "பரந்தது: அடிப்படை உரிமைகள் + 'பிற சட்ட நோக்கங்களுக்கும்'", "குறுகியது: அடிப்படை உரிமைகள் மட்டுமே"],
          ["நிலப்பரப்பு எல்லை", "மாநில எல்லைக்குள் (காரணம் எழுந்தால் தவிர)", "இந்தியா முழுவதற்கும் பொருந்தும்"],
          ["அடிப்படை உரிமை நிலை", "அரசியலமைப்பு பரிகாரம் (தானே அடிப்படை உரிமையல்ல)", "தானே ஒரு அடிப்படை உரிமையாகும் (விதி 32)"],
          ["மறுப்பு அதிகாரம்", "விருப்பவுரிமை (மாற்று பரிகாரம் இருந்தால் மறுக்கலாம்)", "கட்டாயம் (SC நிராகரிக்க முடியாது)"],
          ["அடிப்படை அமைப்பு நிலை", "அடிப்படை அமைப்பின் பகுதி (எல். சந்திரகுமார் 1997)", "அடிப்படை அமைப்பின் பகுதி (கேசவானந்தா 1973)"]
        ]
      },
      {
        "id": "tbl_art226_vs_art227_p3",
        "title_en": "3. Article 226 vs Article 227 Deep Comparison",
        "title_ta": "3. உறுப்பு 226 vs உறுப்பு 227 விரிவான ஒப்பீடு",
        "headers_en": ["Feature", "Article 226 (Writ Jurisdiction)", "Article 227 (Supervisory Jurisdiction)"],
        "headers_ta": ["அம்சம்", "உறுப்பு 226 (பேராணை ஆதிக்கம்)", "உறுப்பு 227 (மேற்பார்வை ஆதிக்கம்)"],
        "rows_en": [
          ["Function", "Judicial remedy to enforce legal/fundamental rights", "Administrative and judicial superintendence over lower bodies"],
          ["Target Authority", "Any person, authority, or Government", "Subordinate courts and tribunals ONLY"],
          ["Suo Motu Power", "Rarely exercised suo motu (requires petition)", "Can be exercised SUO MOTU by High Court"],
          ["Military Exclusion", "No explicit military court exclusion", "Military Courts Martial explicitly EXCLUDED (Art 227(4))"]
        ],
        "rows_ta": [
          ["பணி", "உரிமைகளை அமல்படுத்தும் நீதித்துறைப் பரிகாரம்", "கீழ் அமைப்புகள் மீதான நிர்வாக மற்றும் நீதித்துறை மேற்பார்வை"],
          ["இலக்கு அதிகாரம்", "எந்தவொரு நபருக்கும், அதிகார அமைப்பிற்கும் அல்லது அரசிற்கும்", "சார்பு நீதிமன்றங்கள் மற்றும் தீர்ப்பாயங்களுக்கு மட்டுமே"],
          ["Suo Motu அதிகாரம்", "அரிதாகவே suo motu (மனு தேவை)", "HC தாமாக முன்வந்து (SUO MOTU) பயன்படுத்தலாம்"],
          ["இராணுவ விலக்கு", "வெளிப்படையான இராணுவ விலக்கு இல்லை", "இராணுவ நீதிமன்றங்கள் வெளிப்படையாக விலக்கப்பட்டுள்ளன (விதி 227(4))"]
        ]
      },
      {
        "id": "tbl_art227_vs_art235_p3",
        "title_en": "4. Article 227 vs Article 235 Comparison",
        "title_ta": "4. உறுப்பு 227 vs உறுப்பு 235 ஒப்பீடு",
        "headers_en": ["Dimension", "Article 227 (Superintendence)", "Article 235 (Control over Subordinate Judiciary)"],
        "headers_ta": ["அம்சம்", "உறுப்பு 227 (மேற்பார்வை)", "உறுப்பு 235 (சார்பு நீதிமன்றக் கட்டுப்பாடு)"],
        "rows_en": [
          ["Scope", "General judicial & administrative superintendence over ALL courts/tribunals", "Specific administrative & disciplinary control over SUBORDINATE JUDGES"],
          ["Target", "Courts and Tribunals as institutions", "Judicial Officers (persons in judicial service)"],
          ["Matters Covered", "Rules of practice, forms, judicial supervision", "Postings, promotions, leave, disciplinary proceedings, compulsory retirement"],
          ["Exclusions", "Armed Forces Military Courts excluded", "Applies to State subordinate judicial service"]
        ],
        "rows_ta": [
          ["எல்லை", "அனைத்து நீதிமன்றங்கள்/தீர்ப்பாயங்கள் மீதான பொதுவான மேற்பார்வை", "சார்பு நீதிபதிகள் மீதான குறிப்பிட்ட நிர்வாக & ஒழுங்கு நடவடிக்கைக் கட்டுப்பாடு"],
          ["இலக்கு", "நிறுவனங்களாக நீதிமன்றங்கள் மற்றும் தீர்ப்பாயங்கள்", "நீதித்துறை அதிகாரிகள் (நீதிச் சேவையிலுள்ள நபர்கள்)"],
          ["உள்ளடங்கிய விஷயங்கள்", "நடைமுறை விதிகள், படிவங்கள், நீதித்துறை மேற்பார்வை", "பணியமர்த்தல், உயர்வு, விடுப்பு, ஒழுங்கு நடவடிக்கைகள், கட்டாய ஓய்வு"],
          ["விலக்குகள்", "இராணுவ நீதிமன்றங்கள் விலக்கப்பட்டுள்ளன", "மாநில சார்பு நீதிச் சேவைக்குப் பொருந்தும்"]
        ]
      },
      {
        "id": "tbl_hc_vs_subordinate_p3",
        "title_en": "5. High Court vs Subordinate Courts Comparison",
        "title_ta": "5. உயர் நீதிமன்றம் vs சார்பு நீதிமன்றங்கள் ஒப்பீடு",
        "headers_en": ["Aspect", "High Court (Part VI Chapter V)", "Subordinate Courts (Part VI Chapter VI)"],
        "headers_ta": ["கூறு", "உயர் நீதிமன்றம் (பகுதி VI அத்தியாயம் V)", "சார்பு நீதிமன்றங்கள் (பகுதி VI அத்தியாயம் VI)"],
        "rows_en": [
          ["Constitutional Status", "Constitutional Court of Record (Art 215)", "Statutory / Subordinate Courts under HC control (Arts 233-237)"],
          ["Appointing Authority", "PRESIDENT OF INDIA (Art 217)", "GOVERNOR of the State (Art 233/234)"],
          ["Writ Jurisdiction", "Possesses Writ Powers under Article 226", "NO Writ Powers under Constitution"],
          ["Control Mechanism", "Vested with control over subordinate courts (Art 235)", "Subject to complete administrative control of High Court"]
        ],
        "rows_ta": [
          ["அரசியலமைப்பு நிலை", "அரசியலமைப்புப் பதிவு நீதிமன்றம் (விதி 215)", "HC கட்டுப்பாட்டில் உள்ள சார்பு நீதிமன்றங்கள் (விதிகள் 233-237)"],
          ["நியமிக்கும் அதிகாரி", "இந்தியக் குடியரசுத் தலைவர் (விதி 217)", "மாநில ஆளுநர் (விதி 233/234)"],
          ["பேராணை அதிகாரம்", "உறுப்பு 226-ன் கீழ் பேராணை அதிகாரம் உண்டு", "அரசியலமைப்பின் கீழ் பேராணை அதிகாரம் இல்லை"],
          ["கட்டுப்பாட்டு நடைமுறை", "சார்பு நீதிமன்றங்கள் மீது கட்டுப்பாடு கொண்டுள்ளவை (விதி 235)", "உயர் நீதிமன்றத்தின் முழுமையான நிர்வாகக் கட்டுப்பாடுக்கு உட்பட்டவை"]
        ]
      },
      {
        "id": "tbl_review_vs_superintendence_p3",
        "title_en": "6. Judicial Review vs Judicial Superintendence",
        "title_ta": "6. நீதித்துறை ஆய்வு vs நீதித்துறை மேற்பார்வை ஒப்பீடு",
        "headers_en": ["Feature", "Judicial Review (Article 226)", "Judicial Superintendence (Article 227)"],
        "headers_ta": ["அம்சம்", "நீதித்துறை ஆய்வு (உறுப்பு 226)", "நீதித்துறை மேற்பார்வை (உறுப்பு 227)"],
        "rows_en": [
          ["Primary Function", "Testing constitutional validity of statutes and executive acts", "Keeping lower tribunals within legal bounds and proper procedure"],
          ["Target Subject", "Acts of Parliament/Assembly and Executive Orders", "Subordinate courts and statutory tribunals"],
          ["Outcome", "Declaring unconstitutional laws void", "Correcting procedural errors, setting aside illegal lower orders"]
        ],
        "rows_ta": [
          ["முதன்மைப் பணி", "சட்டங்கள் & நிர்வாக ஆணைகளின் அரசியலமைப்புச் செல்லுபடியை ஆய்வு செய்தல்", "கீழ் தீர்ப்பாயங்களைச் சட்ட எல்லைக்குள் வைப்பது"],
          ["இலக்கு பாடம்", "நாடாளுமன்ற/சட்டமன்றச் சட்டங்கள் மற்றும் நிர்வாக ஆணைகள்", "சார்பு நீதிமன்றங்கள் மற்றும் சட்டப்பூர்வ தீர்ப்பாயங்கள்"],
          ["முடிவு", "அரசியலமைப்பிற்கு எதிரான சட்டங்களை ரத்து செய்தல்", "நடைமுறைப் பிழைகளைத் திருத்துதல், சட்டவிரோதக் கீழ் உத்தரவுகளை ரத்து செய்தல்"]
        ]
      },
      {
        "id": "tbl_common_vs_separate_hc_p3",
        "title_en": "7. Common High Court vs Separate High Court Comparison",
        "title_ta": "7. பொது உயர் நீதிமன்றம் vs தனி உயர் நீதிமன்றம் ஒப்பீடு",
        "headers_en": ["Parameter", "Common High Court (Article 231)", "Separate High Court (Article 214)"],
        "headers_ta": ["அளவுரு", "பொது உயர் நீதிமன்றம் (உறுப்பு 231)", "தனி உயர் நீதிமன்றம் (உறுப்பு 214)"],
        "rows_en": [
          ["Constitutional Source", "Article 231 (7th Constitutional Amendment Act 1956)", "Article 214 (Original Constitutional Mandate)"],
          ["Jurisdiction Reach", "Covers two or more States, or States and UTs", "Covers a single State territory"],
          ["Examples", "Bombay HC (Maha, Goa, Dadra), Punjab & Haryana HC", "Madras HC (for TN), Kerala HC (for Kerala)"],
          ["Establishment Authority", "Established by PARLIAMENT BY LAW", "Established per Constitutional framework"]
        ],
        "rows_ta": [
          ["அரசியலமைப்பு ஆதாரம்", "உறுப்பு 231 (1956 7-வது அரசியலமைப்புச் சட்டத்திருத்தம்)", "உறுப்பு 214 (மூல அரசியலமைப்பு விதி)"],
          ["அதிகார வரம்பு எல்லை", "இரண்டு அல்லது அதற்கு மேற்பட்ட மாநிலங்கள் / UT-களை உள்ளடக்கும்", "ஒற்றை மாநில நிலப்பரப்பை மட்டுமே உள்ளடக்கும்"],
          ["உதாரணங்கள்", "பாம்பே HC, பஞ்சாப் & ஹரியானா HC, கௌஹாத்தி HC", "மதராஸ் HC, கேரளா HC, கர்நாடகா HC"],
          ["அமைக்கும் அதிகாரம்", "நாடாளுமன்றத்தால் சட்டத்தின் மூலம் அமைக்கப்படுவது", "அரசியலமைப்பு கட்டமைப்பின் படி அமைக்கப்படுவது"]
        ]
      },
      {
        "id": "tbl_hc_vs_sc_writ_p3",
        "title_en": "8. High Court Writ Jurisdiction vs Supreme Court Writ Jurisdiction",
        "title_ta": "8. உயர் நீதிமன்ற பேராணை ஆதிக்கம் vs உச்ச நீதிமன்ற பேராணை ஆதிக்கம்",
        "headers_en": ["Aspect", "High Court Writ Jurisdiction (Art 226)", "Supreme Court Writ Jurisdiction (Art 32)"],
        "headers_ta": ["கூறு", "உயர் நீதிமன்ற பேராணை (விதி 226)", "உச்ச நீதிமன்ற பேராணை (விதி 32)"],
        "rows_en": [
          ["Subject Matter Scope", "Broader: Protects FRs and ordinary legal/statutory rights", "Narrower: Protects ONLY Fundamental Rights"],
          ["Territorial Reach", "State / UT territorial boundaries (or cause of action)", "Entire Territory of India"],
          ["Remedy Status", "Discretionary remedy (Alternative remedies considered)", "Guaranteed Fundamental Right (Art 32 itself is FR)"],
          ["Refusal Power", "HC MAY refuse to issue writ if alternative remedy exists", "SC CANNOT refuse to entertain petition for FR violation"]
        ],
        "rows_ta": [
          ["பாட எல்லை", "பரந்தது: அடிப்படை உரிமைகள் + சாதாரண சட்ட உரிமைகள்", "குறுகியது: அடிப்படை உரிமைகள் மட்டுமே"],
          ["நிலப்பரப்பு எல்லை", "மாநில / UT எல்லைக்குள் (காரணம் எழுந்தால் தவிர)", "இந்தியா முழுவதற்கும் பொருந்தும்"],
          ["பரிகார நிலை", "விருப்பவுரிமை பரிகாரம் (மாற்று பரிகாரம் பரிசீலிக்கப்படும்)", "உத்திரவாதம் அளிக்கப்பட்ட அடிப்படை உரிமைப் பரிகாரம்"],
          ["மறுப்பு அதிகாரம்", "மாற்று பரிகாரம் இருந்தால் HC பேராணை பிறப்பிக்க மறுக்கலாம்", "அடிப்படை உரிமை மீறல் மனுவை SC நிராகரிக்க முடியாது"]
        ]
      },
      {
        "id": "tbl_transfer_vs_removal_hc_p3",
        "title_en": "9. High Court Judge Transfer vs Judge Removal Comparison",
        "title_ta": "9. உயர் நீதிமன்ற நீதிபதி இடமாற்றம் vs நீக்கம் ஒப்பீடு",
        "headers_en": ["Feature", "Judge Transfer (Article 222)", "Judge Removal (Article 218)"],
        "headers_ta": ["அம்சம்", "நீதிபதி இடமாற்றம் (உறுப்பு 222)", "நீதிபதி நீக்கம் (உறுப்பு 218)"],
        "rows_en": [
          ["Authority", "President of India after consultation with CJI", "President of India after Parliamentary Address"],
          ["Process", "Executive order following CJI Collegium consultation", "Special Majority voting in both Houses of Parliament"],
          ["Grounds", "Public interest / judicial administration", "Proved Misbehaviour OR Incapacity ONLY"],
          ["Judicial Status", "Continues as judge in transferee High Court", "Office terminated permanently"]
        ],
        "rows_ta": [
          ["அதிகாரி", "CJI ஆலோசனையுடன் இந்தியக் குடியரசுத் தலைவர்", "நாடாளுமன்றத் தீர்மானத்திற்குப் பின் இந்தியக் குடியரசுத் தலைவர்"],
          ["நடைமுறை", "CJI கொலீஜியம் ஆலோசனையைத் தொடர்ந்து நிர்வாக ஆணை", "நாடாளுமன்றத்தின் இரு அவைகளிலும் சிறப்பு பெரும்பான்மை വാக்கெடுப்பு"],
          ["அடிப்படைகள்", "பொது நலன் / நீதித்துறை நிர்வாகம்", "நிரூபிக்கப்பட்ட தவறான நடத்தை அல்லது திறமையின்மை மட்டுமே"],
          ["நீதிபதி நிலை", "மாற்றப்பட்ட உயர் நீதிமன்றத்தில் நீதிபதியாகத் தொடர்கிறார்", "பதவி நிரந்தரமாக முடிவுக்கு வருகிறது"]
        ]
      },
      {
        "id": "tbl_const_vs_collegium_p3",
        "title_en": "10. Constitutional Appointment Text vs Collegium Practice Comparison",
        "title_ta": "10. அரசியலமைப்பு நியமன உரை vs கொலீஜியம் நடைமுறை ஒப்பீடு",
        "headers_en": ["Parameter", "Constitutional Text (Article 217)", "Collegium System Practice"],
        "headers_ta": ["அளவுரு", "அரசியலமைப்பு உரை (உறுப்பு 217)", "கொலீஜியம் அமைப்பு நடைமுறை"],
        "rows_en": [
          ["Term Used", "Uses the term 'CONSULTATION' with CJI and Governor", "Interpreted 'Consultation' as 'CONCURRENCE'"],
          ["Collegium Mention", "No mention of a 'Collegium' body", "CJI + 2 Senior-most SC Judges (for HC appointments)"],
          ["Primacy Authority", "Gave President/Executive apparent final say", "Gave Judicial Collegium binding primacy in selection"],
          ["Constitutional Source", "Written text of 1950 Constitution of India", "Judicially evolved through 1981, 1993, 1998 Supreme Court rulings"]
        ],
        "rows_ta": [
          ["பயன்படுத்தப்பட்ட சொல்", "CJI மற்றும் ஆளுநருடன் 'ஆலோசனை' என்ற சொல்லைப் பயன்படுத்துகிறது", "'ஆலோசனை' என்பதை 'ஒப்புதல் (Concurrence)' என விளக்கியது"],
          ["கொலீஜியம் குறிப்பிடல்", "'கொலீஜியம்' என்ற அமைப்பு பற்றி குறிப்பிடப்படவில்லை", "CJI + 2 மூத்த உச்ச நீதிமன்ற நீதிபதிகள் கொண்ட குழு (HC நியமனங்களுக்கு)"],
          ["முதன்மை அதிகாரி", "நிர்வாகத்திற்கு/குடியரசுத் தலைவருக்கு இறுதி அதிகாரம் அளித்தது", "நீதித்துறை கொலீஜியத்திற்கே பிணைப்புறுதி முதன்மை அளித்தது"],
          ["அரசியலமைப்பு ஆதாரம்", "1950 இந்திய அரசியலமைப்பின் எழுதப்பட்ட உரை", "1981, 1993, 1998 உச்ச நீதிமன்றத் தீர்ப்புகள் மூலம் உருவானது"]
        ]
      }
    ],
    "mind_map": [
      {
        "title": "High Courts Advanced Concepts, Common HCs & Controls",
        "short_label": "High Court Part 3",
        "children": [
          {
            "title": "1. Articles 230 & 231 (Common High Courts)",
            "short_label": "Arts 230 & 231",
            "children": [
              {"title": "25 High Courts Total; 25th AP HC Amaravati 2019; Common HCs (7th Amend 1956)", "short_label": "25 HCs"},
              {"title": "UT Rule: Only DELHI UT has separate High Court (est. 1966)", "short_label": "Delhi UT HC"}
            ]
          },
          {
            "title": "2. Article 235 & Subordinate Judiciary",
            "short_label": "Art 235 Control",
            "children": [
              {"title": "Art 235: Control over postings, promotions, leave, discipline vested in HC", "short_label": "HC Control"},
              {"title": "Shamsher Singh 1974: Control under Art 235 is EXCLUSIVE to High Court", "short_label": "Shamsher Singh"}
            ]
          },
          {
            "title": "3. Article 229 Staff Independence",
            "short_label": "Art 229 Staff",
            "children": [
              {"title": "HC CJ appoints officers & servants; Expenses charged on State Fund", "short_label": "Staff & Fund"}
            ]
          },
          {
            "title": "4. Master Comparisons & Landmark Principles",
            "short_label": "Comparisons & Cases",
            "children": [
              {"title": "Art 226 vs 32 (Scope), Art 226 vs 227, Art 227 vs 235 (Superintendence vs Control)", "short_label": "Comparisons"},
              {"title": "L. Chandra Kumar 1997 (Basic Structure), K. Ashok Reddy 1994 (Transfers)", "short_label": "Landmark Cases"}
            ]
          }
        ]
      }
    ],
    "tnpsc_traps": [
      {
        "title": "1. Total High Courts & Union Territory Trap (மொத்த HCs & UT பற்றிய பொறி)",
        "points": {
          "en": [
            "TRAP: Believing every Union Territory has its own High Court or that India has 28 High Courts.",
            "FACT: India currently has 25 HIGH COURTS! ONLY ONE Union Territory (DELHI UT) has a separate High Court of its own (established 1966)."
          ],
          "ta": [
            "பொறி: ஒவ்வொரு யூனியன் பிரதேசத்திற்கும் தனி உயர் நீதிமன்றம் உள்ளது என்றோ இந்தியாவில் 28 உயர் நீதிமன்றங்கள் உள்ளன என்றோ நினைப்பது.",
            "உண்மை: இந்தியாவில் தற்போது 25 உயர் நீதிமன்றங்கள் மட்டுமே உள்ளன! டெல்லி யூனியன் பிரதேசம் மட்டுமே தனக்கெனத் தனி உயர் நீதிமன்றத்தைக் (1966) கொண்டுள்ளது."
          ]
        }
      },
      {
        "title": "2. Article 235 Subordinate Judiciary Control Trap (சார்பு நீதிமன்றக் கட்டுப்பாடு பொறி)",
        "points": {
          "en": [
            "TRAP: Assuming the State Executive or Law Minister controls the postings, promotions, and discipline of subordinate judicial officers.",
            "FACT: Under Article 235, control over subordinate courts (postings, promotions, leave, disciplinary proceedings) is VESTED EXCLUSIVELY IN THE HIGH COURT!"
          ],
          "ta": [
            "பொறி: மாநில நிர்வாகமோ அல்லது சட்ட அமைச்சரோ சார்பு நீதித்துறை அதிகாரிகளின் நியமனம், பதவி உயர்வு மற்றும் ஒழுங்கு நடவடிக்கைகளைக் கட்டுப்படுத்துவதாக நினைப்பது.",
            "உண்மை: உறுப்பு 235-ன் கீழ் சார்பு நீதிமன்றங்கள் மீதான கட்டுப்பாடு (பணியமர்த்தல், பதவி உயர்வு, ஒழுங்கு நடவடிக்கை) உயர் நீதிமன்றத்தின் வசம் மட்டுமே உள்ளது!"
          ]
        }
      },
      {
        "title": "3. Article 227 vs Article 235 Distinctions Trap (விதி 227 vs 235 வேறுபாட்டுப் பொறி)",
        "points": {
          "en": [
            "TRAP: Merging Article 227 and Article 235 as the same power.",
            "FACT: Article 227 is general SUPERINTENDENCE over all lower courts and tribunals as institutions; Article 235 is specific ADMINISTRATIVE CONTROL over subordinate judicial officers (persons)."
          ],
          "ta": [
            "பொறி: உறுப்பு 227 மற்றும் உறுப்பு 235 இரண்டையும் ஒரே அதிகாரம் என இணைத்துக் குழப்புவது.",
            "உண்மை: உறுப்பு 227 என்பது கீழ் நீதிமன்றங்கள்/தீர்ப்பாயங்கள் மீதான பொதுவான மேற்பார்வை (Superintendence); உறுப்பு 235 என்பது சார்பு நீதித்துறை அதிகாரிகள் மீதான குறிப்பிட்ட நிர்வாகக் கட்டுப்பாடு (Control)."
          ]
        }
      },
      {
        "title": "4. High Court Staff Appointment Trap (ஊழியர்கள் நியமன அதிகாரிப் பொறி)",
        "points": {
          "en": [
            "TRAP: Thinking High Court staff and officers are appointed by the State Public Service Commission (TNPSC).",
            "FACT: Under Article 229(1), officers and servants of a High Court are APPOINTED BY THE CHIEF JUSTICE OF THE HIGH COURT (or judge/officer authorized by him) without executive interference!"
          ],
          "ta": [
            "பொறி: உயர் நீதிமன்ற ஊழியர்கள் மற்றும் அதிகாரிகள் மாநில அரசுப் பணியாளர் தேர்வாணையத்தால் (TNPSC) நியமிக்கப்படுகின்றனர் என நினைப்பது.",
            "உண்மை: உறுப்பு 229(1)-ன் கீழ் உயர் நீதிமன்ற அதிகாரிகள் மற்றும் ஊழியர்கள் உயர் நீதிமன்றத் தலைமை நீதிபதியால் (அல்லது அவரால் அதிகாரம் அளிக்கப்பட்ட நபரால்) நியமிக்கப்படுகின்றனர்!"
          ]
        }
      },
      {
        "title": "5. Common High Court Establishment Trap (பொது உயர் நீதிமன்ற அதிகாரம் பற்றிய பொறி)",
        "points": {
          "en": [
            "TRAP: Believing the President or Governors can establish a Common High Court for two or more States.",
            "FACT: Under Article 231 (added by 7th Amendment 1956), ONLY PARLIAMENT HAS THE AUTHORITY TO ESTABLISH A COMMON HIGH COURT BY LAW!"
          ],
          "ta": [
            "பொறி: குடியரசுத் தலைவரோ ஆளுநர்களோ இரண்டு அல்லது அதற்கு மேற்பட்ட மாநிலங்களுக்குப் பொது உயர் நீதிமன்றத்தை அமைக்க முடியும் என நினைப்பது.",
            "உண்மை: உறுப்பு 231-ன் கீழ் (1956 7-வது திருத்தம்) நாடாளுமன்றத்திற்கு மட்டுமே சட்டத்தின் மூலம் பொது உயர் நீதிமன்றத்தை அமைக்க அதிகாரமுண்டு!"
          ]
        }
      }
    ],
    "quick_revision": {
      "en": [
        "Common High Courts (Art 231): 7th Amend 1956 empowers Parliament by law to establish Common HC. Total HCs: 25 (25th AP HC Amaravati 2019). Only DELHI UT has separate HC (1966).",
        "Common HCs List: Bombay (Maha, Goa, Dadra), Gauhati (Assam, Nagaland, Mizoram, Arunachal), Punjab & Haryana (Punjab, Haryana, Chandigarh), Calcutta (WB, A&N), Madras (TN, Puducherry), Kerala (Kerala, Lakshadweep), J&K & Ladakh.",
        "Subordinate Judiciary Control (Art 235): Postings, promotions, leave, discipline of subordinate judicial officers vested EXCLUSIVELY in High Court (Shamsher Singh 1974).",
        "Staff Independence (Art 229): HC Chief Justice appoints officers & servants. Administrative expenses charged on Consolidated Fund of STATE (Art 229(3)).",
        "Master Comparisons: Art 226 (FRs + legal rights, wider) vs Art 32 (FRs only). Art 226 (Writs) vs Art 227 (Superintendence over all courts/tribunals). Art 227 (Superintendence) vs Art 235 (Subordinate judicial officer control).",
        "Landmark Cases: L. Chandra Kumar 1997 (Arts 226 & 227 Basic Structure; CAT appeals to HC Division Bench), K. Ashok Reddy 1994 (Transfers limited review), Shamsher Singh 1974 (Art 235 exclusive control)."
      ],
      "ta": [
        "பொது உயர் நீதிமன்றங்கள் (விதி 231): 1956 7-வது திருத்தம் பொது HC அமைக்க நாடாளுமன்றத்திற்கு அதிகாரமளிக்கிறது. மொத்த HCs: 25 (25-வது அமராவதி ஆந்திரா HC 2019). டெல்லி UT மட்டுமே தனி HC கொண்டுள்ளது (1966).",
        "பொது HCs பட்டியல்: பாம்பே, கௌஹாத்தி (4 மாநிலங்கள்), பஞ்சாப் & ஹரியானா, கல்கத்தா, மதராஸ், கேரளா, J&K & லடாக்.",
        "சார்பு நீதிமன்றக் கட்டுப்பாடு (விதி 235): சார்பு நீதித்துறை அதிகாரிகளின் நியமனம், உயர்வு, விடுப்பு, ஒழுங்கு நடவடிக்கை முழுமையாக உயர் நீதிமன்றத்தின் வசம் மட்டுமே (சம்ஷேர் சிங் 1974).",
        "ஊழியர்கள் சுதந்திரம் (விதி 229): HC தலைமை நீதிபதி ஊழியர்களை நியமிக்கிறார். செலவுகள் மாநிலத் தொகுப்பு நிதியில் சுமத்தப்பட்டவை (விதி 229(3)).",
        "முக்கிய ஒப்பீடுகள்: விதி 226 vs 32, விதி 226 vs 227, விதி 227 vs 235 (மேற்பார்வை vs கட்டுப்பாடு).",
        "வரலாற்று வழக்குகள்: எல். சந்திரகுமார் 1997 (விதிகள் 226 & 227 அடிப்படை அமைப்பு; CAT உத்தரவுகள் HC இரு நீதிபதிகள் அமர்வுக்கு), கே. அசோக் ரெட்டி 1994, சம்ஷேர் சிங் 1974."
      ]
    },
    "must_remember": {
      "en": [
        "MUST REMEMBER: India currently has 25 High Courts (25th is Andhra Pradesh HC at Amaravati, 2019).",
        "MUST REMEMBER: ONLY Delhi Union Territory has a separate High Court of its own (est. 1966).",
        "MUST REMEMBER: Article 231 empowers Parliament by law to establish a Common High Court (7th Amend 1956).",
        "MUST REMEMBER: Article 235 vests administrative and disciplinary control over subordinate courts in the High Court.",
        "MUST REMEMBER: Article 229 empowers High Court Chief Justice to appoint officers and servants of the High Court.",
        "MUST REMEMBER: High Court administrative expenses are charged on Consolidated Fund of the STATE (Art 229(3)).",
        "MUST REMEMBER: High Court judge pensions are charged on Consolidated Fund of INDIA.",
        "MUST REMEMBER: Shamsher Singh (1974) held Article 235 control over subordinate judiciary is exclusive to High Court.",
        "MUST REMEMBER: L. Chandra Kumar (1997) held Articles 226 and 227 are part of Basic Structure of Constitution.",
        "MUST REMEMBER: Gauhati High Court has common jurisdiction over 4 North-Eastern States (Assam, Nagaland, Mizoram, Arunachal)."
      ],
      "ta": [
        "நினைவில் கொள்க: இந்தியாவில் தற்போது 25 உயர் நீதிமன்றங்கள் உள்ளன (25-வது அமராவதி ஆந்திரா HC, 2019).",
        "நினைவில் கொள்க: டெல்லி யூனியன் பிரதேசம் மட்டுமே தனக்கெனத் தனி உயர் நீதிமன்றத்தைக் கொண்டுள்ளது (1966).",
        "நினைவில் கொள்க: உறுப்பு 231 நாடாளுமன்றம் பொது உயர் நீதிமன்றத்தை அமைக்க அதிகாரமளிக்கிறது (1956 7-வது திருத்தம்).",
        "நினைவில் கொள்க: உறுப்பு 235 சார்பு நீதிமன்றங்கள் மீதான நிர்வாக & ஒழுங்கு நடவடிக்கைக் கட்டுப்பாட்டை உயர் நீதிமன்றத்திற்கு அளிக்கிறது.",
        "நினைவில் கொள்க: உறுப்பு 229 உயர் நீதிமன்றத் தலைமை நீதிபதி ஊழியர்களை நியமிக்க அதிகாரமளிக்கிறது.",
        "நினைவில் கொள்க: உயர் நீதிமன்ற நிர்வாகச் செலவுகள் மாநிலத் தொகுப்பு நிதியில் சுமத்தப்படுகின்றன (விதி 229(3)).",
        "நினைவில் கொள்க: உயர் நீதிமன்ற நீதிபதிகளின் ஓய்வூதியம் இந்தியத் தொகுப்பு நிதியில் சுமத்தப்படுகிறது.",
        "நினைவில் கொள்க: சம்ஷேர் சிங் (1974) வழக்கு உறுப்பு 235 சார்பு நீதிமன்றக் கட்டுப்பாடு உயர் நீதிமன்றத்திற்கு மட்டுமே உரியது எனத் தீர்ப்பளித்தது.",
        "நினைவில் கொள்க: எல். சந்திரகுமார் (1997) வழக்கு விதிகள் 226 மற்றும் 227 அடிப்படை அமைப்பின் பகுதி எனத் தீர்ப்பளித்தது.",
        "நினைவில் கொள்க: கௌஹாத்தி உயர் நீதிமன்றம் 4 வடகிழக்கு மாநிலங்களுக்குப் (அசாம், நாகாலாந்து, மிசோரம், அருணாச்சலம்) பொதுவான அதிகார வரம்பு கொண்டுள்ளது."
      ]
    }
  }
}

target_file = "data/notes/polity/high_court_part_3.json"
os.makedirs("data/notes/polity", exist_ok=True)

with open(target_file, "w", encoding="utf-8") as f:
  json.dump(part3_data, f, ensure_ascii=False, indent=2)

print(f"✅ High Court Part 3 successfully saved to: {target_file}")
