# -*- coding: utf-8 -*-
"""
Builder Script for Governor of a State Notes — Part 3
Subject: Indian Polity
Topic: Governor of a State – Part 3
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("==================================================")
print("BUILDING GOVERNOR NOTES — PART 3")
print("==================================================")

part3_data = {
  "meta": {
    "topic_id": "polity_governor_part_3",
    "repository_id": "polity_governor",
    "display_title": "Governor of a State – Part 3",
    "part": 3,
    "total_parts": 3,
    "subject": "polity",
    "chapter": "Governor of a State",
    "language": "English + Tamil"
  },
  "metadata": {
    "topic_id": "polity_governor_part_3",
    "repository_id": "polity_governor",
    "display_title": "Governor of a State – Part 3",
    "part": 3,
    "total_parts": 3,
    "subject": "polity",
    "chapter": "Governor of a State",
    "language": "English + Tamil"
  },
  "keywords": [
    "Constitutional Discretion",
    "Situational Discretion",
    "Article 163 Discretion",
    "Article 163(1)",
    "Article 163(2)",
    "Article 200 Reservation",
    "Article 356 Report",
    "Article 160 Contingencies",
    "Hung Assembly",
    "Floor Test Mandate",
    "S.R. Bommai 1994 Case",
    "Nbam Rebia 2016 Case",
    "Sarkaria Commission 1983",
    "Punchhi Commission 2007",
    "Administrative Reforms Commission",
    "Rajamannar Committee 1969",
    "TNPSC Polity Master Notes"
  ],
  "learning_outcomes": {
    "Understand": {
      "en": [
        "Master the unique Discretionary Powers of the Governor under Article 163(1) and Article 163(2) (Finality of Governor's decision on discretion).",
        "Understand Constitutional Discretion (Reservation of Bills Art 200, President's Rule Report Art 356, Tribal Affairs Art 371/Sch V/VI, Art 160 contingencies).",
        "Master Situational Discretion (Appointment of CM in Hung Assembly, Dismissal of Ministry failing to prove majority, Dissolution of Assembly).",
        "Analyze landmark Judicial Precedents (S.R. Bommai 1994 floor test mandate, Nabam Rebia 2016 discretionary scope, Rameshwar Prasad 2006 Assembly dissolution).",
        "Evaluate Major Reform Commissions (Sarkaria Commission 1983, Punchhi Commission 2007, Rajamannar Committee 1969 recommendations on Governor's office)."
      ],
      "ta": [
        "உறுப்பு 163(1) மற்றும் உறுப்பு 163(2)-ன் கீழ் ஆளுநரின் தனித்துவமான சுயவிருப்ப அதிகாரங்களில் தேர்ச்சி பெறுதல் (சுயவிருப்ப அதிகாரம் குறித்த ஆளுநரின் முடிவே இறுதியானது).",
        "அரசியலமைப்பு சுயவிருப்ப அதிகாரங்களைப் புரிந்துகொள்வது (மசோதா ஒதுக்கீடு - விதி 200, குடியரசுத் தலைவர் ஆட்சி அறிக்கை - விதி 356, பழங்குடியினர் விவகாரங்கள் - விதி 371/அட்டவணை V/VI, விதி 160 அவசரச் சூழல்கள்).",
        "சூழ்நிலை சுயவிருப்ப அதிகாரங்களைக் கற்றல் (தொங்கு சட்டமன்றத்தில் முதலமைச்சர் நியமனம், பெரும்பான்மையை நிரூபிக்கத் தவறிய அமைச்சரவையை நீக்குதல், அவையைக் கலைத்தல்).",
        "முக்கிய நீதிமன்றத் தீர்ப்புகளைப் பகுப்பாய்வு செய்தல் (எஸ்.ஆர். பொம்மை 1994 வாக்கெடுப்பு கட்டளை, நபம் ரெபியா 2016 சுயவிருப்ப எல்லை, ரமேஷ்வர் பிரசாத் 2006 சட்டமன்றக் கலைப்பு).",
        "முக்கிய சீர்திருத்த ஆணையங்களை மதிப்பீடு செய்தல் (சர்க்காரியா ஆணையம் 1983, பூஞ்சி ஆணையம் 2007, ராஜமன்னார் குழு 1969 ஆளுநர் பதவி குறித்த பரிந்துரைகள்)."
      ]
    }
  },
  "subject": "polity",
  "topic": "Governor of a State",
  "language": "English + Tamil",
  "ui_type": "standard_notes",
  "sections": [
    {
      "id": "sec_constitutional_discretion",
      "title_en": "1. Constitutional Discretion & Finality Clause (Article 163)",
      "title_ta": "1. அரசியலமைப்பு சுயவிருப்ப அதிகாரம் & இறுதித்தன்மை விதி (உறுப்பு 163)",
      "type": "standard_topic"
    },
    {
      "id": "sec_situational_discretion",
      "title_en": "2. Situational Discretion (Hung Assembly, Floor Test & Dissolution)",
      "title_ta": "2. சூழ்நிலை சுயவிருப்ப அதிகாரங்கள் (தொங்கு சட்டமன்றம், வாக்கெடுப்பு & கலைப்பு)",
      "type": "standard_topic"
    },
    {
      "id": "sec_article_160_special",
      "title_en": "3. Article 160 & Special Constitutional Duties (Articles 371 & Schedules V/VI)",
      "title_ta": "3. உறுப்பு 160 & சிறப்பு அரசியலமைப்புக் கடமைகள் (உறுப்புகள் 371 & அட்டவணைகள் V/VI)",
      "type": "standard_topic"
    },
    {
      "id": "sec_judicial_precedents",
      "title_en": "4. Landmark Judicial Precedents (S.R. Bommai, Nabam Rebia & Rameshwar Prasad)",
      "title_ta": "4. முக்கிய வரலாற்றுத் தீர்ப்புகள் (எஸ்.ஆர். பொம்மை, நபம் ரெபியா & ரமேஷ்வர் பிரசாத்)",
      "type": "standard_topic"
    },
    {
      "id": "sec_commissions_reforms",
      "title_en": "5. Reform Commissions & Recommendations (Sarkaria, Punchhi, Rajamannar & ARC)",
      "title_ta": "5. சீர்திருத்த ஆணையங்கள் & பரிந்துரைகள் (சர்க்காரியா, பூஞ்சி, ராஜமன்னார் & ஏஆர்சி)",
      "type": "standard_topic"
    },
    {
      "id": "comparison_tables",
      "title_en": "6. Master Comparison Tables (Discretion, Judicial & Commission Focus)",
      "title_ta": "6. முதன்மை ஒப்பீட்டு அட்டவணைகள் (சுயவிருப்பம், நீதித்துறை & ஆணையங்கள் கவனம்)",
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
      "en": "Governor's Discretionary Powers represent constitutional exceptions under Article 163 where the Governor acts independently without or contrary to the aid and advice of the Chief Minister and Council of Ministers.",
      "ta": "ஆளுநரின் சுயவிருப்ப அதிகாரம் என்பது உறுப்பு 163-ன் கீழ் அரசியலமைப்பு விதிவிலக்காகும். இதன் மூலம் ஆளுநர் முதலமைச்சர் மற்றும் அமைச்சரவையின் ஆலோசனையின்றி அல்லது அதற்கு எதிராகத் சுயாதீனமாகச் செயல்படுகிறார்."
    },
    "introduction": {
      "en": "Unlike the President of India who has NO express constitutional discretion (except situational discretion), the Constitution explicitly confers express Constitutional Discretion upon the Governor under Article 163(1) and makes the Governor's decision on discretion FINAL under Article 163(2).",
      "ta": "இந்தியக் குடியரசுத் தலைவருக்குத் தெளிவான அரசியலமைப்பு சுயவிருப்ப அதிகாரம் எதுவும் இல்லை என்ற நிலையில் (சூழ்நிலை அதிகாரம் தவிர), அரசியலமைப்பு உறுப்பு 163(1)-ன் கீழ் ஆளுநருக்குத் தெளிவான சுயவிருப்ப அதிகாரத்தை வழங்குகிறது மற்றும் உறுப்பு 163(2)-ன் கீழ் ஆளுநரின் முடிவே இறுதியானது என அறிவிக்கிறது."
    },
    "sec_constitutional_discretion": [
      {
        "title_en": "Article 163(1) & 163(2) — Express Constitutional Discretion",
        "title_ta": "உறுப்பு 163(1) & 163(2) — தெளிவான அரசியலமைப்பு சுயவிருப்ப அதிகாரம்",
        "points": {
          "en": [
            "Article 163(1): There shall be a Council of Ministers with Chief Minister at the head to aid and advise the Governor, EXCEPT in so far as he is by or under this Constitution required to exercise his functions or any of them in his discretion.",
            "Article 163(2) Finality Clause: If any question arises whether any matter is or is not a matter as respects which the Governor is required to act in his discretion, the decision of the Governor in his discretion shall be FINAL, and the validity of anything done by the Governor shall not be called in question on the ground that he ought or ought not to have acted in his discretion.",
            "Key Express Constitutional Discretions:",
            "  1. Reservation of a Bill for President's consideration (Art 200).",
            "  2. Recommendation for President's Rule under Article 356 (State Constitutional Breakdown).",
            "  3. Seeking information from Chief Minister regarding administrative and legislative affairs (Art 167(b)).",
            "  4. Determining the amount payable by Assam, Meghalaya, Tripura, Mizoram to autonomous Tribal District Council as royalty from mineral extraction (Schedule VI).",
            "  5. Special responsibilities under Article 371 (e.g. Maharashtra/Gujarat Vidarbha/Saurashtra boards, Assam, Nagaland law & order, Manipur, Sikkim, Arunachal Pradesh, Karnataka-Hyderabad region)."
          ],
          "ta": [
            "உறுப்பு 163(1): ஆளுநருக்கு உதவவும் ஆலோசனை வழங்கவும் முதலமைச்சரைத் தலைவராகக் கொண்ட அமைச்சரவை இருக்கும்; ஆனால் அரசியலமைப்பின் படி ஆளுநர் தனது சுயவிருப்பப்படி செயல்பட வேண்டிய விஷயங்களில் இது பொருந்தாது.",
            "உறுப்பு 163(2) இறுதித்தன்மை விதி: ஒரு விஷயம் ஆளுநரின் சுயவிருப்ப அதிகாரத்திற்கு உட்பட்டதா இல்லையா என்ற கேள்வி எழுந்தால், ஆளுநரின் சுயவிருப்ப முடிவே இறுதியானது; அதை எந்த நீதிமன்றத்திலும் கேள்வி கேட்க முடியாது.",
            "முக்கியத் தெளிவான அரசியலமைப்பு சுயவிருப்ப அதிகாரங்கள்:",
            "  1. மசோதாவைக் குடியரசுத் தலைவர் பரிசீலனைக்கு ஒதுக்கி வைத்தல் (விதி 200).",
            "  2. உறுப்பு 356-ன் கீழ் குடியரசுத் தலைவர் ஆட்சிக்கு பரிந்துரை செய்தல் (மாநில அரசியலமைப்பு செயலிழப்பு).",
            "  3. விதி 167(b)-ன் கீழ் முதலமைச்சரிடமிருந்து நிர்வாகம் மற்றும் சட்டமன்றத் தகவல்களைக் கோருதல்.",
            "  4. அஸ்ஸாம், மேகாலயா, திரிபுரா, மிசோரம் மாநில சுயாட்சி பழங்குடியின மாவட்டக் குழுக்களுக்கு கனிம ரோயல்டி தொகையைத் தீர்மானித்தல் (அட்டவணை VI).",
            "  5. உறுப்பு 371-ன் கீழ் சிறப்புப் பொறுப்புகள் (எ.கா. மகாராஷ்டிரா/குஜராத் வாரியங்கள், நாகாலாந்து சட்டம் ஒழுங்கு, சிக்கிம், அருணாச்சலப் பிரதேசம்)."
          ]
        }
      }
    ],
    "sec_situational_discretion": [
      {
        "title_en": "Situational Discretion & Political Scenarios",
        "title_ta": "சூழ்நிலை சுயவிருப்ப அதிகாரங்கள் & அரசியல் சூழல்கள்",
        "points": {
          "en": [
            "Appointment of Chief Minister in Hung Assembly: When no single political party gets a clear majority in Assembly elections or when a sitting CM dies in office with no obvious successor.",
            "Dismissal of Ministry: Dismissing the Council of Ministers when it cannot prove the confidence of the Legislative Assembly after losing majority.",
            "Dissolution of Assembly: Dissolving the State Legislative Assembly if the Council of Ministers has lost its majority and no alternative government can be formed.",
            "Discharge of Contingencies (Art 160): President may make such provision as he thinks fit for the discharge of the functions of the Governor of a State in any contingency not provided for in Part VI."
          ],
          "ta": [
            "தொங்கு சட்டமன்றத்தில் முதலமைச்சர் நியமனம்: சட்டமன்றத் தேர்தலில் எந்தக் கட்சிக்கும் பெரும்பான்மை கிடைக்காத போது அல்லது பதவியில் உள்ள முதலமைச்சர் வாரிசு இன்றி இறக்கும் போது.",
            "அமைச்சரவை நீக்கம்: பெரும்பான்மையை இழந்த பின் சட்டப்பேரவையின் நம்பிக்கையை நிரூபிக்கத் தவறும் அமைச்சரவையை நீக்குதல்.",
            "சட்டமன்றக் கலைப்பு: அமைச்சரவை பெரும்பான்மையை இழந்து மாற்று அரசாங்கம் அமைக்க முடியாத சூழலில் சட்டப்பேரவையைக் கலைத்தல்.",
            "அவசரச் சூழல்களைக் கையாளுதல் (விதி 160): பகுதி VI-ல் குறிப்பிடப்படாத எந்தவொரு அவசரச் சூழலிலும் ஆளுநரின் பணிகளைச் செயல்படுத்த குடியரசுத் தலைவர் ஏற்பாடுகளைச் செய்யலாம்."
          ]
        }
      }
    ],
    "sec_judicial_precedents": [
      {
        "title_en": "Landmark Supreme Court Rulings on Governor's Discretion",
        "title_ta": "ஆளுநரின் சுயவிருப்ப அதிகாரம் குறித்த உச்ச நீதிமன்ற வரலாற்றுத் தீர்ப்புகள்",
        "points": {
          "en": [
            "S.R. Bommai v. Union of India (1994): Supreme Court held that the ONLY legal test of majority support for a Chief Minister is a FLOOR TEST on the floor of the Legislative Assembly, NOT subjective assessment in Raj Bhavan! Article 356 proclamation is subject to Judicial Review.",
            "Nabam Rebia v. Deputy Speaker (2016): SC ruled that Governor's discretion under Art 163 is strictly bound by Constitutional guidelines. Governor cannot bypass or act independently of Council of Ministers in summoning session unless exceptional breakdown occurs.",
            "Rameshwar Prasad v. Union of India (2006): SC struck down dissolution of Bihar Assembly by President based on Governor's subjective report alleging horse-trading, holding that subjective satisfaction of Governor cannot bypass floor test.",
            "Shamsher Singh v. State of Punjab (1974): 7-Judge Constitution Bench ruled that Governor is a formal constitutional head and must exercise executive powers strictly on aid and advice of Ministers except where explicit discretion is conferred."
          ],
          "ta": [
            "எஸ்.ஆர். பொம்மை v. இந்திய ஒன்றியம் (1994): முதலமைச்சரின் பெரும்பான்மையை நிரூபிக்கும் ஒரே சட்டப்பூர்வ சோதனை 'சட்டமன்ற அவையில் நடக்கும் வாக்கெடுப்பு (Floor Test)' மட்டுமே; ராஜ் பவனின் தனிப்பட்ட மதிப்பீடு அல்ல! விதி 356 குடியரசுத் தலைவர் ஆட்சி நீதித்துறை ஆய்வுக்கு உட்பட்டது.",
            "நபம் ரெபியா v. துணை சபாநாயகர் (2016): விதி 163-ன் கீழ் ஆளுநரின் சுயவிருப்ப அதிகாரம் அரசியலமைப்பு வழிகாட்டுதல்களுக்கு உட்பட்டது. அவையைக் கூட்டுவதில் அமைச்சரவையின் ஆலோசனையை மீறி ஆளுநர் தன்னிச்சையாகச் செயல்பட முடியாது.",
            "ரமேஷ்வர் பிரசாத் v. இந்திய ஒன்றியம் (2006): ஆளுநரின் தன்னிச்சையான அறிக்கையின் அடிப்படையில் பீகார் சட்டமன்றம் கலைக்கப்பட்டதை உச்ச நீதிமன்றம் ரத்து செய்தது; வாக்கெடுப்பை மீறி ஆளுநரின் சொந்த திருப்தி இருக்க முடியாது.",
            "சம்ஷேர் சிங் v. பஞ்சாப் மாநிலம் (1974): 7 நீதிபதிகள் கொண்ட அமர்வு ஆளுநர் ஒரு முறைப்படியான அரசியலமைப்புத் தலைவர் என்றும், தெளிவான சுயவிருப்ப அதிகாரம் தவிர மற்ற அனைத்திலும் அமைச்சரவை ஆலோசனையின் படியே செயல்பட வேண்டும் என்றும் தீர்ப்பளித்தது."
          ]
        }
      }
    ],
    "sec_commissions_reforms": [
      {
        "title_en": "Major Reform Commissions on Governor's Office",
        "title_ta": "ஆளுநர் பதவி குறித்த முக்கிய சீர்திருத்த ஆணையங்கள்",
        "points": {
          "en": [
            "Sarkaria Commission (1983): Recommended that Governor should be an eminent person outside active politics, appointed in consultation with CM, Vice-President, and Speaker. 5-year tenure should not be disturbed except in rare, compelling circumstances. Floor test mandatory.",
            "Punchhi Commission (2007): Recommended that Governor should be given fixed 5-year tenure, removed ONLY by Impeachment procedure by State Legislature (similar to President)! Governor should step down as University Chancellor to avoid conflict.",
            "Rajamannar Committee (1969 - Tamil Nadu): Recommended that Chief Minister MUST be consulted before appointing Governor, or a panel of names should be prepared by State Legislature.",
            "Administrative Reforms Commission (ARC 1966): Recommended non-partisan appointments and objective guidelines for discretionary powers."
          ],
          "ta": [
            "சர்க்காரியா ஆணையம் (1983): தீவிர அரசியலில் இல்லாத ஒரு சான்றோர் ஆளுநராக நியமிக்கப்பட வேண்டும். முதலமைச்சர், துணைக் குடியரசுத் தலைவர் மற்றும் சபாநாயகரைக் கலந்தாலோசிக்க வேண்டும். 5 ஆண்டு பதவிக்காலம் அரிதான சூழ்நிலை தவிர மாற்றப்படக்கூடாது. வாக்கெடுப்பு கட்டாயம்.",
            "பூஞ்சி ஆணையம் (2007): ஆளுநருக்கு 5 ஆண்டுகள் நிலையான பதவிக்காலம் வழங்கப்பட வேண்டும்; மாநில சட்டமன்றத்தின் 'பதவி நீக்கத் தீர்மானம் (Impeachment)' மூலம் மட்டுமே நீக்கப்பட வேண்டும்! மோதல்களைத் தவிர்க்க ஆளுநர் பல்கலைக்கழக வேந்தர் பதவியிலிருந்து விலக வேண்டும்.",
            "ராஜமன்னார் குழு (1969 - தமிழ்நாடு): ஆளுநரை நியமிக்கும் முன் முதலமைச்சரைக் கட்டாயம் கலந்தாலோசிக்க வேண்டும் அல்லது மாநில சட்டமன்றத்தால் பெயர்களின் பட்டியல் தயாரிக்கப்பட வேண்டும்.",
            "நிர்வாக சீர்திருத்த ஆணையம் (ARC 1966): அரசியல் சார்பற்ற நியமனங்கள் மற்றும் சுயவிருப்ப அதிகாரங்களுக்கான புறநிலை வழிகாட்டுதல்களைப் பரிந்துரைத்தது."
          ]
        }
      }
    ],
    "revision_cards": [
      {
        "id": "gov_p3_c1",
        "front_en": "Which Constitutional Article confers express Discretionary Powers on the Governor?",
        "front_ta": "ஆளுநருக்குத் தெளிவான சுயவிருப்ப அதிகாரங்களை வழங்கும் அரசியலமைப்பு உறுப்பு எது?",
        "back_en": "Article 163(1) (And Article 163(2) makes Governor's decision on discretion FINAL).",
        "back_ta": "உறுப்பு 163(1) (மற்றும் உறுப்பு 163(2) சுயவிருப்ப அதிகாரம் குறித்த ஆளுநரின் முடிவே இறுதியானது என்கிறது)."
      },
      {
        "id": "gov_p3_c2",
        "front_en": "What did the Supreme Court mandate regarding proving majority support in S.R. Bommai case (1994)?",
        "front_ta": "எஸ்.ஆர். பொம்மை வழக்கில் (1994) பெரும்பான்மையை நிரூபிப்பது குறித்து உச்ச நீதிமன்றம் என்ன கட்டாயமாக்கியது?",
        "back_en": "Majority support MUST be tested ONLY via a Floor Test on the floor of the State Legislative Assembly.",
        "back_ta": "பெரும்பான்மை ஆதரவு மாநிலச் சட்டப்பேரவை அவையில் நடக்கும் வாக்கெடுப்பு (Floor Test) மூலமாக மட்டுமே சோதிக்கப்பட வேண்டும்."
      },
      {
        "id": "gov_p3_c3",
        "front_en": "Does the President of India have express Constitutional Discretion like the Governor under Art 163?",
        "front_ta": "விதி 163-ன் கீழ் ஆளுநருக்கு இருப்பது போல இந்தியக் குடியரசுத் தலைவருக்குத் தெளிவான அரசியலமைப்பு சுயவிருப்ப அதிகாரம் உள்ளதா?",
        "back_en": "NO. President has NO express constitutional discretion in the Constitution (Only situational discretion).",
        "back_ta": "இல்லை. அரசியலமைப்பில் குடியரசுத் தலைவருக்குத் தெளிவான சுயவிருப்ப அதிகாரம் எதுவும் இல்லை (சூழ்நிலை அதிகாரம் மட்டுமே)."
      },
      {
        "id": "gov_p3_c4",
        "front_en": "Which Commission recommended that Governors should be removed ONLY by Impeachment by State Legislature?",
        "front_ta": "மாநில சட்டமன்றத்தின் பதவி நீக்கத் தீர்மானம் (Impeachment) மூலம் மட்டுமே ஆளுநர் நீக்கப்பட வேண்டும் என பரிந்துரைத்த ஆணையம் எது?",
        "back_en": "Punchhi Commission (2007).",
        "back_ta": "பூஞ்சி ஆணையம் (2007)."
      },
      {
        "id": "gov_p3_c5",
        "front_en": "What Article allows the President to make provision for Governor's functions in unforeseen contingencies?",
        "front_ta": "குறிப்பிடப்படாத அவசரச் சூழல்களில் ஆளுநரின் பணிகளைச் செயல்படுத்த குடியரசுத் தலைவருக்கு அனுமதி அளிக்கும் விதி எது?",
        "back_en": "Article 160.",
        "back_ta": "உறுப்பு 160."
      },
      {
        "id": "gov_p3_c6",
        "front_en": "Which 1969 Committee constituted by Tamil Nadu Government made recommendations on Centre-State & Governor relations?",
        "front_ta": "மத்திய-மாநில மற்றும் ஆளுநர் உறவுகள் குறித்து 1969-ல் தமிழக அரசால் அமைக்கப்பட்ட குழு எது?",
        "back_en": "Rajamannar Committee (1969).",
        "back_ta": "ராஜமன்னார் குழு (1969)."
      },
      {
        "id": "gov_p3_c7",
        "front_en": "Under Schedule VI, who determines the mineral royalty share payable to autonomous tribal districts in Assam/Meghalaya?",
        "front_ta": "அட்டவணை VI-ன் கீழ் அஸ்ஸாம்/மேகாலயா சுயாட்சி பழங்குடியின மாவட்டங்களுக்குக் கனிம ரோயல்டி தொகையைத் தீர்மானிப்பவர் யார்?",
        "back_en": "Governor of the State in his discretion.",
        "back_ta": "மாநில ஆளுநர் தனது சுயவிருப்ப அதிகாரத்தின் கீழ்."
      },
      {
        "id": "gov_p3_c8",
        "front_en": "What was held in Nabam Rebia Case (2016) regarding Governor's power to summon session?",
        "front_ta": "நபம் ரெபியா வழக்கில் (2016) அவையைக் கூட்டும் ஆளுநரின் அதிகாரம் குறித்து என்ன தீர்ப்பளிக்கப்பட்டது?",
        "back_en": "Governor CANNOT summon session independently without or against aid/advice of Council of Ministers.",
        "back_ta": "அமைச்சரவையின் ஆலோசனையின்றி அல்லது அதற்கு எதிராக ஆளுநர் தன்னிச்சையாக அவையைக் கூட்ட முடியாது."
      },
      {
        "id": "gov_p3_c9",
        "front_en": "What is 'Situational Discretion' of Governor?",
        "front_ta": "ஆளுநரின் 'சூழ்நிலை சுயவிருப்ப அதிகாரம்' என்றால் என்ன?",
        "back_en": "Discretion arising out of political situations (e.g. Hung Assembly, CM appointment, dissolution when no majority).",
        "back_ta": "அரசியல் சூழல்களால் ஏற்படும் அதிகாரம் (எ.கா. தொங்கு சட்டமன்றம், முதலமைச்சர் நியமனம், பெரும்பான்மையற்ற சூழலில் அவையைக் கலைத்தல்)."
      },
      {
        "id": "gov_p3_c10",
        "front_en": "Which Commission recommended that Governor should step down as University Chancellor?",
        "front_ta": "ஆளுநர் பல்கலைக்கழக வேந்தர் பதவியிலிருந்து விலக வேண்டும் எனப் பரிந்துரைத்த ஆணையம் எது?",
        "back_en": "Punchhi Commission (2007).",
        "back_ta": "பூஞ்சி ஆணையம் (2007)."
      }
    ],
    "comparison_tables": [
      {
        "id": "tbl_gov_vs_pres_discretion_p3",
        "title_en": "1. Governor vs President Discretion Comparison",
        "title_ta": "1. ஆளுநர் vs குடியரசுத் தலைவர் சுயவிருப்ப அதிகாரம் ஒப்பீடு",
        "headers_en": ["Feature", "Governor of a State", "President of India"],
        "headers_ta": ["அம்சம்", "மாநில ஆளுநர்", "இந்தியக் குடியரசுத் தலைவர்"],
        "rows_en": [
          ["Express Constitutional Discretion", "EXPRESSLY PROVIDED under Art 163(1)", "NOT expressly provided anywhere in Constitution"],
          ["Finality Clause", "Governor's decision on discretion is FINAL under Art 163(2)", "No finality clause in Constitution"],
          ["Situational Discretion", "Enjoys situational discretion in Hung Assembly/CM appointment", "Enjoys situational discretion in Hung Lok Sabha/PM appointment"],
          ["Bill Reservation Discretion", "Constitutional discretion to reserve Bills for President (Art 200)", "No such reservation power over state bills"],
          ["Constitutional Breakdown Report", "Discretionary power to report Art 356 state breakdown", "Acts on Governor's report or otherwise"]
        ],
        "rows_ta": [
          ["தெளிவான அரசியலமைப்பு சுயவிருப்ப அதிகாரம்", "விதி 163(1)-ன் கீழ் தெளிவாக வழங்கப்பட்டுள்ளது", "அரசியலமைப்பில் எங்கும் தெளிவாக வழங்கப்படவில்லை"],
          ["இறுதித்தன்மை விதி", "விதி 163(2)-ன் கீழ் ஆளுநரின் சுயவிருப்ப முடிவே இறுதியானது", "அரசியலமைப்பில் இறுதித்தன்மை விதி இல்லை"],
          ["சூழ்நிலை சுயவிருப்ப அதிகாரம்", "தொங்கு சட்டமன்றம்/முதலமைச்சர் நியமனத்தில் சூழ்நிலை அதிகாரம் உண்டு", "தொங்கு மக்களவை/பிரதமர் நியமனத்தில் சூழ்நிலை அதிகாரம் உண்டு"],
          ["மசோதா ஒதுக்கீடு அதிகாரம்", "குடியரசுத் தலைவருக்கு மசோதாவை ஒதுக்கும் அரசியலமைப்பு அதிகாரம் (விதி 200)", "மாநில மசோதாக்கள் மீது இத்தகைய ஒதுக்கீட்டு அதிகாரம் இல்லை"],
          ["அரசியலமைப்பு செயலிழப்பு அறிக்கை", "விதி 356 மாநில செயலிழப்பு அறிக்கை அனுப்பும் சுயவிருப்ப அதிகாரம்", "ஆளுநர் அறிக்கை அல்லது பிற வழிகளில் செயல்படுகிறார்"]
        ]
      },
      {
        "id": "tbl_constitutional_vs_situational_p3",
        "title_en": "2. Constitutional Discretion vs Situational Discretion",
        "title_ta": "2. அரசியலமைப்பு சுயவிருப்ப அதிகாரம் vs சூழ்நிலை சுயவிருப்ப அதிகாரம்",
        "headers_en": ["Dimension", "Constitutional Discretion (Express)", "Situational Discretion (Implied)"],
        "headers_ta": ["அம்சம்", "அரசியலமைப்பு சுயவிருப்ப அதிகாரம் (தெளிவானது)", "சூழ்நிலை சுயவிருப்ப அதிகாரம் (உட்கிடையானது)"],
        "rows_en": [
          ["Source", "Explicitly written in Constitution (Art 163, Art 200, Art 356, Sch VI)", "Arises from political exigencies and absence of political majority"],
          ["Examples", "Reserving Bill for President, Art 356 report, Sch VI tribal royalties", "Appointing CM in Hung Assembly, Dismissing ministry failing floor test"],
          ["Judicial Oversight", "Subject to constitutional bounds (Nabam Rebia 2016)", "Strictly governed by Floor Test requirement (S.R. Bommai 1994)"],
          ["Cabinet Advice", "Bypasses Cabinet advice explicitly under constitutional text", "Operates when Cabinet advice is absent, questionable, or majority is lost"]
        ],
        "rows_ta": [
          ["ஆதாரம்", "அரசியலமைப்பில் தெளிவாக எழுதப்பட்டுள்ளது (விதி 163, 200, 356, அட்டவணை VI)", "அரசியல் அவசரங்கள் மற்றும் பெரும்பான்மையின்மையால் ஏற்படுகிறது"],
          ["எடுத்துக்காட்டுகள்", "குடியரசுத் தலைவருக்கு மசோதா ஒதுக்கீடு, விதி 356 அறிக்கை, அட்டவணை VI கனிம ரோயல்டி", "தொங்கு சட்டமன்றத்தில் முதலமைச்சர் நியமனம், வாக்கெடுப்பில் தோற்ற அமைச்சரவை நீக்கம்"],
          ["நீதிமன்றக் கண்காணிப்பு", "அரசியலமைப்பு எல்லைகளுக்கு உட்பட்டது (நபம் ரெபியா 2016)", "வாக்கெடுப்பு (Floor Test) விதியால் கடுமையாகக் கட்டுப்படுத்தப்படுகிறது (பொம்மை 1994)"],
          ["கேபினட் ஆலோசனை", "அரசியலமைப்பு உரையின் படி கேபினட் ஆலோசனையை நேரடியாகத் தவிர்க்கிறது", "கேபினட் ஆலோசனை இல்லாத போது அல்லது பெரும்பான்மை இழந்த போது செயல்படுகிறது"]
        ]
      },
      {
        "id": "tbl_bommai_vs_nabam_p3",
        "title_en": "3. S.R. Bommai (1994) vs Nabam Rebia (2016) Supreme Court Rulings",
        "title_ta": "3. எஸ்.ஆர். பொம்மை (1994) vs நபம் ரெபியா (2016) உச்ச நீதிமன்றத் தீர்ப்புகள்",
        "headers_en": ["Parameter", "S.R. Bommai v. Union of India (1994)", "Nabam Rebia v. Deputy Speaker (2016)"],
        "headers_ta": ["அளவுரு", "எஸ்.ஆர். பொம்மை v. இந்திய ஒன்றியம் (1994)", "நபம் ரெபியா v. துணை சபாநாயகர் (2016)"],
        "rows_en": [
          ["Core Focus", "Article 356 President's Rule & Floor Test mandate", "Governor's discretionary power under Art 163 in summoning Assembly"],
          ["Floor Test Rule", "Majority MUST be tested on Assembly Floor, NOT in Raj Bhavan", "Governor cannot act as a party actor or bypass CM in calling session"],
          ["Judicial Review", "Proclamation under Art 356 is fully subject to Judicial Review", "Discretion under Art 163 is subject to strict constitutional boundaries"],
          ["Constitutional Impact", "Curbed misuse of Article 356 by Central Government", "Prevented Governor from destabilizing elected state governments"]
        ],
        "rows_ta": [
          ["முதன்மை கவனம்", "விதி 356 குடியரசுத் தலைவர் ஆட்சி & அவையில் வாக்கெடுப்பு கட்டாயம்", "அவையைக் கூட்டுவதில் விதி 163-ன் கீழ் ஆளுநரின் சுயவிருப்ப அதிகாரம்"],
          ["வாக்கெடுப்பு விதி", "பெரும்பான்மை அவையில் மட்டுமே சோதிக்கப்பட வேண்டும், ராஜ் பவனில் அல்ல", "அவையைக் கூட்டுவதில் ஆளுநர் முதலமைச்சரைத் தவிர்த்துத் தன்னிச்சையாகச் செயல்பட முடியாது"],
          ["நீதிமன்ற ஆய்வு", "விதி 356 பிரகடனம் முழுமையாக நீதித்துறை ஆய்வுக்கு உட்பட்டது", "விதி 163 சுயவிருப்ப அதிகாரம் கடுமையான அரசியலமைப்பு எல்லைகளுக்கு உட்பட்டது"],
          ["அரசியலமைப்புத் தாக்கம்", "மத்திய அரசால் விதி 356 தவறாகப் பயன்படுத்தப்படுவதைத் தடுத்தது", "தேர்ந்தெடுக்கப்பட்ட மாநில அரசுகளை ஆளுநர் நிலையற்றதாக்குவதைத் தடுத்தது"]
        ]
      },
      {
        "id": "tbl_sarkaria_vs_punchhi_p3",
        "title_en": "4. Sarkaria Commission (1983) vs Punchhi Commission (2007)",
        "title_ta": "4. சர்க்காரியா ஆணையம் (1983) vs பூஞ்சி ஆணையம் (2007)",
        "headers_en": ["Recommendation Dimension", "Sarkaria Commission (1983)", "Punchhi Commission (2007)"],
        "headers_ta": ["பரிந்துரை அம்சம்", "சர்க்காரியா ஆணையம் (1983)", "பூஞ்சி ஆணையம் (2007)"],
        "rows_en": [
          ["Governor Profile", "Eminent person outside active politics for some time", "Person detached from local politics; fixed qualification"],
          ["Appointment Consultation", "Consult Chief Minister, Vice-President, and Speaker of Lok Sabha", "State CM must be consulted; panel system for selection"],
          ["Removal / Tenure Security", "5-year term should not be disturbed except in rare situations", "Removed ONLY by Impeachment by State Legislature (Like President)"],
          ["University Chancellorship", "Governor should continue as Chancellor of Universities", "Governor should step down as Chancellor to avoid controversies"],
          ["Floor Test Mandate", "Floor test in Assembly is mandatory for majority check", "Floor test mandatory within strict timeframes"]
        ],
        "rows_ta": [
          ["ஆளுநர் தகுதிப் சுயவிவரம்", "தீவிர அரசியலில் இல்லாத வெளிமாநில சான்றோர்", "உள்ளூர் அரசியலில் தொடர்பு இல்லாதவர்; நிலையான தகுதி"],
          ["நியமனக் கலந்தாய்வு", "முதலமைச்சர், துணைக் குடியரசுத் தலைவர், மக்களவை சபாநாயகரைக் கலந்தாலோசிக்க வேண்டும்", "மாநில முதலமைச்சர் கட்டாயம் கலந்தாலோசிக்கப்பட வேண்டும்; பெயர்ப் பட்டியல் முறை"],
          ["பதவி நீக்கம் / பதவிக்காலப் பாதுகாப்பு", "5 ஆண்டு பதவிக்காலம் அரிதான சூழல் தவிர மாற்றப்படக்கூடாது", "மாநில சட்டமன்றத்தின் பதவி நீக்கம் (Impeachment) மூலம் மட்டுமே நீக்கப்பட வேண்டும்"],
          ["பல்கலைக்கழக வேந்தர்", "ஆளுநர் பல்கலைக்கழக வேந்தராகத் தொடரலாம்", "சர்ச்சைகளைத் தவிர்க்க ஆளுநர் வேந்தர் பதவியிலிருந்து விலக வேண்டும்"],
          ["வாக்கெடுப்பு கட்டாயம்", "பெரும்பான்மையைச் சோதிக்க அவையில் வாக்கெடுப்பு கட்டாயம்", "குறிப்பிட்ட காலக்கெடுவுக்குள் வாக்கெடுப்பு கட்டாயம்"]
        ]
      },
      {
        "id": "tbl_rajamannar_vs_arc_p3",
        "title_en": "5. Rajamannar Committee (1969) vs ARC (1966) Focus",
        "title_ta": "5. ராஜமன்னார் குழு (1969) vs ஏஆர்சி (1966) கவனம்",
        "headers_en": ["Feature", "Rajamannar Committee (1969 - Tamil Nadu)", "Administrative Reforms Commission (ARC 1966)"],
        "headers_ta": ["அம்சம்", "ராஜமன்னார் குழு (1969 - தமிழ்நாடு)", "நிர்வாக சீர்திருத்த ஆணையம் (ஏஆர்சி 1966)"],
        "rows_en": [
          ["Origin & Scope", "Appointed by Tamil Nadu Government on Centre-State Relations", "Appointed by Central Government on Public Administration"],
          ["Governor Appointment", "Mandatory consultation with CM or panel by State Legislature", "Non-partisan appointments of experienced public figures"],
          ["Article 356 View", "Recommended complete deletion or strict limitation of Art 356", "Recommended Art 356 as an extreme last resort"],
          ["State Autonomy", "Strong emphasis on State autonomy and reducing Centre control", "Focused on administrative efficiency and inter-state coordination"]
        ],
        "rows_ta": [
          ["தோற்றம் & எல்லை", "மத்திய-மாநில உறவுகள் குறித்து தமிழக அரசால் அமைக்கப்பட்ட குழு", "பொது நிர்வாகம் குறித்து மத்திய அரசால் அமைக்கப்பட்ட ஆணையம்"],
          ["ஆளுநர் நியமனம்", "முதலமைச்சருடன் கட்டாயக் கலந்தாய்வு அல்லது சட்டமன்றப் பட்டியல் முறை", "அனுபவம் வாய்ந்த பொதுப் பிரமுகர்களின் அரசியல் சார்பற்ற நியமனங்கள்"],
          ["விதி 356 பார்வை", "விதி 356-ஐ முழுமையாக நீக்க அல்லது கடுமையாகக் கட்டுப்படுத்த பரிந்துரை", "விதி 356-ஐ மிகக் கடைசி கட்ட நடவடிக்கையாகப் பயன்படுத்தப் பரிந்துரை"],
          ["மாநில சுயாட்சி", "மாநில சுயாட்சி மற்றும் மத்திய கட்டுப்பாட்டைக் குறைப்பதில் தீவிர கவனம்", "நிர்வாகத் திறன் மற்றும் மாநிலங்களுக்கு இடையேயான ஒருங்கிணைப்பில் கவனம்"]
        ]
      },
      {
        "id": "tbl_discretion_summary_p3",
        "title_en": "6. Master Summary of Governor's Discretionary Powers",
        "title_ta": "6. ஆளுநரின் சுயவிருப்ப அதிகாரங்களின் முதன்மைச் சுருக்கம்",
        "headers_en": ["Discretion Category", "Constitutional Basis / Article", "Key Examples / Operations"],
        "headers_ta": ["சுயவிருப்பப் பிரிவு", "அரசியலமைப்பு அடிப்படை / விதி", "முக்கிய எடுத்துக்காட்டுகள் / செயல்பாடுகள்"],
        "rows_en": [
          ["Bill Assent & Reservation", "Article 200 & Article 201", "Reserving Bill for President; Withholding assent; Returning non-Money Bills"],
          ["State Emergency Report", "Article 356", "Reporting breakdown of constitutional machinery in State to President"],
          ["Contingencies Discharge", "Article 160", "Exercising special emergency functions defined by President"],
          ["Tribal Affairs & Schedule VI", "Schedule VI & Article 371", "Determining mineral royalties for autonomous councils in Assam/Meghalaya"],
          ["Hung Assembly CM Selection", "Situational (Art 164)", "Appointing CM when no party has clear majority"],
          ["Ministry Dismissal", "Situational (Art 164(2))", "Dismissing ministry that lost Assembly majority and refuses to resign"]
        ],
        "rows_ta": [
          ["மசோதா ஒப்புதல் & ஒதுக்கீடு", "உறுப்பு 200 & உறுப்பு 201", "குடியரசுத் தலைவருக்கு மசோதா ஒதுக்கீடு; ஒப்புதல் நிறுத்தம்; மறுபரிசீலனை திருப்புதல்"],
          ["மாநில அவசரநிலை அறிக்கை", "உறுப்பு 356", "மாநிலத்தில் அரசியலமைப்புச் இயந்திரம் செயலிழந்ததை குடியரசுத் தலைவருக்கு அறிக்கையிடல்"],
          ["அவசரச் சூழல்கள் கையாளுதல்", "உறுப்பு 160", "குடியரசுத் தலைவரால் வரையறுக்கப்பட்ட சிறப்பு அவசரப் பணிகளைச் செய்தல்"],
          ["பழங்குடியினர் விவகாரங்கள்", "அட்டவணை VI & உறுப்பு 371", "அஸ்ஸாம்/மேகாலயா சுயாட்சி மன்றங்களுக்குக் கனிம ரோயல்டி தொகையைத் தீர்மானித்தல்"],
          ["தொங்கு சட்டமன்றத்தில் முதலமைச்சர்", "சூழ்நிலை அதிகாரம் (விதி 164)", "எந்தக் கட்சிக்கும் பெரும்பான்மை இல்லாத போது முதலமைச்சரை நியமித்தல்"],
          ["அமைச்சரவை நீக்கம்", "சூழ்நிலை அதிகாரம் (விதி 164(2))", "பெரும்பான்மையை இழந்து ராஜினாமா செய்ய மறுக்கும் அமைச்சரவையை நீக்குதல்"]
        ]
      }
    ],
    "mind_map": [
      {
        "title": "Governor Discretion & Reforms (Part VI - Art 163 to Commissions)",
        "short_label": "Governor Part 3",
        "children": [
          {
            "title": "1. Express Discretion",
            "short_label": "Express Discretion",
            "children": [
              {"title": "Art 163(1): Express discretion conferred by Constitution", "short_label": "Art 163(1)"},
              {"title": "Art 163(2): Finality Clause (Governor's decision is final)", "short_label": "Art 163(2)"},
              {"title": "Art 200: Bill Reservation for President", "short_label": "Art 200"}
            ]
          },
          {
            "title": "2. Judicial Rulings",
            "short_label": "Judicial Rulings",
            "children": [
              {"title": "S.R. Bommai (1994): Majority tested ONLY by Floor Test on Assembly floor", "short_label": "Bommai 1994"},
              {"title": "Nabam Rebia (2016): Governor cannot bypass CM in summoning session", "short_label": "Nabam Rebia"}
            ]
          },
          {
            "title": "3. Reform Commissions",
            "short_label": "Commissions",
            "children": [
              {"title": "Sarkaria (1983): Outside eminent person; CM consultation; Floor test mandatory", "short_label": "Sarkaria"},
              {"title": "Punchhi (2007): Removed ONLY by Assembly Impeachment; Step down as Chancellor", "short_label": "Punchhi"},
              {"title": "Rajamannar (1969): TN Govt committee on State autonomy & Governor panel", "short_label": "Rajamannar"}
            ]
          }
        ]
      }
    ],
    "tnpsc_traps": [
      {
        "title": "1. Express Discretion Comparison Trap (தெளிவான சுயவிருப்ப அதிகார ஒப்பீட்டுப் பொறி)",
        "points": {
          "en": [
            "TRAP: Thinking the President has express constitutional discretion just like the Governor.",
            "FACT: The Constitution explicitly confers EXPLICIT Constitutional Discretion on the Governor (Art 163(1)), BUT DOES NOT confer express constitutional discretion on the President of India!"
          ],
          "ta": [
            "பொறி: ஆளுநர் போலவே குடியரசுத் தலைவருக்கும் தெளிவான அரசியலமைப்பு சுயவிருப்ப அதிகாரம் உண்டு என நினைப்பது.",
            "உண்மை: அரசியலமைப்பு ஆளுநருக்குத் தெளிவான சுயவிருப்ப அதிகாரத்தை வழங்குகிறது (விதி 163(1)), ஆனால் குடியரசுத் தலைவருக்கு இத்தகைய தெளிவான அதிகாரம் வழங்கப்படவில்லை!"
          ]
        }
      },
      {
        "title": "2. Floor Test Venue Trap (வாக்கெடுப்பு நடைபெறும் இடப் பொறி)",
        "points": {
          "en": [
            "TRAP: Believing the Governor can assess majority support by counting MLAs at Raj Bhavan.",
            "FACT: In S.R. Bommai (1994), the Supreme Court ruled that majority support MUST be tested ONLY through a Floor Test on the floor of the Legislative Assembly, NOT in Raj Bhavan."
          ],
          "ta": [
            "பொறி: ராஜ் பவனில் எம்எல்ஏ-க்களை எண்ணி ஆளுநர் பெரும்பான்மையைச் சோதிக்கலாம் என நினைப்பது.",
            "உண்மை: எஸ்.ஆர். பொம்மை வழக்கிற்குப் பிறகு (1994), பெரும்பான்மை சட்டப்பேரவை அவையில் நடக்கும் 'வாக்கெடுப்பு (Floor Test)' மூலம் மட்டுமே சோதிக்கப்பட வேண்டும் என உச்ச நீதிமன்றம் தீர்ப்பளித்தது."
          ]
        }
      },
      {
        "title": "3. Governor Impeachment Commission Trap (ஆளுநர் பதவி நீக்கப் பரிந்துரைப் பொறி)",
        "points": {
          "en": [
            "TRAP: Confusing Sarkaria Commission recommendations with Punchhi Commission recommendations.",
            "FACT: It was the PUNCHHI COMMISSION (2007) that recommended Governors should be removed ONLY by Impeachment by the State Legislature (similar to President impeachment)."
          ],
          "ta": [
            "பொறி: சர்க்காரியா ஆணையப் பரிந்துரைகளையும் பூஞ்சி ஆணையப் பரிந்துரைகளையும் குழப்பிக் கொள்ளுதல்.",
            "உண்மை: மாநில சட்டமன்றத்தின் பதவி நீக்கத் தீர்மானம் (Impeachment) மூலம் மட்டுமே ஆளுநர் நீக்கப்பட வேண்டும் எனப் பரிந்துரைத்தது பூஞ்சி ஆணையம் (2007) ஆகும்."
          ]
        }
      },
      {
        "title": "4. Rajamannar Committee Origin Trap (ராஜமன்னார் குழு தோற்றப் பொறி)",
        "points": {
          "en": [
            "TRAP: Believing the Rajamannar Committee was appointed by the Union Government.",
            "FACT: The Rajamannar Committee (1969) was appointed by the TAMIL NADU GOVERNMENT (DMK administration under M. Karunanidhi) to examine Centre-State relations and Governor's powers."
          ],
          "ta": [
            "பொறி: ராஜமன்னார் குழு மத்திய அரசால் அமைக்கப்பட்டது என நினைப்பது.",
            "உண்மை: ராஜமன்னார் குழு (1969) மத்திய-மாநில உறவுகள் மற்றும் ஆளுநர் அதிகாரங்களை ஆராய 'தமிழ்நாடு அரசால்' அமைக்கப்பட்டது."
          ]
        }
      },
      {
        "title": "5. Article 163(2) Finality Clause Trap (இறுதித்தன்மை விதிப் பொறி)",
        "points": {
          "en": [
            "TRAP: Assuming courts can easily challenge whether a matter was within the Governor's discretion.",
            "FACT: Under Article 163(2), the decision of the Governor on whether a matter is in his discretion is FINAL and cannot be questioned on that ground (though subject to constitutional guidelines as per Nabam Rebia)."
          ],
          "ta": [
            "பொறி: ஒரு விஷயம் ஆளுநரின் சுயவிருப்ப அதிகாரத்திற்கு உட்பட்டதா என்பதை நீதிமன்றங்கள் எளிதில் கேள்வி கேட்கலாம் என நினைப்பது.",
            "உண்மை: உறுப்பு 163(2)-ன் படி சுயவிருப்ப அதிகாரம் குறித்த ஆளுநரின் முடிவே இறுதியானது, அதை அந்த அடிப்படையில் கேள்வி கேட்க முடியாது (அரசியலமைப்பு எல்லைகளுக்கு உட்பட்டு - நபம் ரெபியா)."
          ]
        }
      }
    ],
    "quick_revision": {
      "en": [
        "Constitutional Discretion: Article 163(1) (Confers express discretion on Governor), Article 163(2) (Governor's decision on discretion is FINAL).",
        "Key Constitutional Discretions: Bill Reservation (Art 200), President's Rule Report (Art 356), Information Seeking (Art 167b), Schedule VI Tribal Royalties.",
        "Situational Discretion: Appointment of CM in Hung Assembly, Dismissal of Ministry losing majority, Dissolution of Assembly.",
        "S.R. Bommai Case (1994): Majority support MUST be tested ONLY on the floor of the Assembly via a Floor Test. Art 356 subject to Judicial Review.",
        "Nabam Rebia Case (2016): Governor cannot bypass CM/Cabinet in summoning Assembly session.",
        "Sarkaria Commission (1983): Eminent outside person, CM consultation, Floor test mandatory.",
        "Punchhi Commission (2007): Governor removed ONLY by Assembly Impeachment; Step down as University Chancellor.",
        "Rajamannar Committee (1969): Tamil Nadu Govt committee on Centre-State relations & Governor panel."
      ],
      "ta": [
        "அரசியலமைப்பு சுயவிருப்ப அதிகாரம்: உறுப்பு 163(1) (தெளிவான அதிகாரம் அளிக்கிறது), உறுப்பு 163(2) (ஆளுநரின் முடிவே இறுதியானது).",
        "முக்கிய அரசியலமைப்பு சுயவிருப்பங்கள்: மசோதா ஒதுக்கீடு (விதி 200), குடியரசுத் தலைவர் ஆட்சி அறிக்கை (விதி 356), தகவல் கோருதல் (விதி 167b), அட்டவணை VI கனிம ரோயல்டி.",
        "சூழ்நிலை சுயவிருப்ப அதிகாரம்: தொங்கு சட்டமன்றத்தில் முதலமைச்சர் நியமனம், பெரும்பான்மையற்ற அமைச்சரவை நீக்கம், அவையைக் கலைத்தல்.",
        "எஸ்.ஆர். பொம்மை வழக்கு (1994): பெரும்பான்மை அவையில் நடக்கும் வாக்கெடுப்பு (Floor Test) மூலம் மட்டுமே சோதிக்கப்பட வேண்டும். விதி 356 நீதிமன்ற ஆய்வுக்கு உட்பட்டது.",
        "நபம் ரெபியா வழக்கு (2016): அவையைக் கூட்டுவதில் ஆளுநர் முதலமைச்சரைத் தவிர்க்க முடியாது.",
        "சர்க்காரியா ஆணையம் (1983): அரசியல் சார்பற்ற சான்றோர், முதலமைச்சர் கலந்தாய்வு, வாக்கெடுப்பு கட்டாயம்.",
        "பூஞ்சி ஆணையம் (2007): சட்டமன்றத்தின் பதவி நீக்கம் (Impeachment) மூலம் மட்டுமே ஆளுநர் நீக்கம்; வேந்தர் பதவியிலிருந்து விலகல்.",
        "ராஜமன்னார் குழு (1969): மத்திய-மாநில உறவுகள் & ஆளுநர் நியமனம் குறித்த தமிழக அரசு குழு."
      ]
    },
    "must_remember": {
      "en": [
        "MUST REMEMBER: Article 163(1) confers express Constitutional Discretion on Governor (President has no express discretion).",
        "MUST REMEMBER: S.R. Bommai (1994) mandated FLOOR TEST on Assembly floor to prove majority.",
        "MUST REMEMBER: Punchhi Commission (2007) recommended Impeachment by State Assembly for Governor removal.",
        "MUST REMEMBER: Rajamannar Committee (1969) was appointed by TAMIL NADU Government.",
        "MUST REMEMBER: Schedule VI empowers Governor to determine mineral royalty share for tribal councils."
      ],
      "ta": [
        "நினைவில் கொள்க: உறுப்பு 163(1) ஆளுநருக்குத் தெளிவான அரசியலமைப்பு சுயவிருப்ப அதிகாரத்தை வழங்குகிறது (குடியரசுத் தலைவருக்கு இல்லை).",
        "நினைவில் கொள்க: எஸ்.ஆர். பொம்மை வழக்கு (1994) பெரும்பான்மையைச் சோதிக்க அவையில் வாக்கெடுப்பைக் (Floor Test) கட்டாயமாக்கியது.",
        "நினைவில் கொள்க: பூஞ்சி ஆணையம் (2007) ஆளுநரை நீக்க மாநில சட்டமன்றத்தின் பதவி நீக்கத் தீர்மானத்தைப் பரிந்துரைத்தது.",
        "நினைவில் கொள்க: ராஜமன்னார் குழு (1969) தமிழ்நாடு அரசால் அமைக்கப்பட்ட குழுவாகும்.",
        "நினைவில் கொள்க: அட்டவணை VI பழங்குடியின மன்றங்களின் கனிம ரோயல்டி தொகையைத் தீர்மானிக்க ஆளுநருக்கு அதிகாரமளிக்கிறது."
      ]
    }
  }
}

target_file = "data/notes/polity/governor_part_3.json"
os.makedirs("data/notes/polity", exist_ok=True)

with open(target_file, "w", encoding="utf-8") as f:
  json.dump(part3_data, f, ensure_ascii=False, indent=2)

print(f"✅ Governor Part 3 with revision_cards successfully updated and saved to: {target_file}")
