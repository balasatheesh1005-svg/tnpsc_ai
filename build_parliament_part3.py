# -*- coding: utf-8 -*-
"""
Builder Script for Parliament of India Notes — Part 3
Subject: Indian Polity
Topic: Parliament of India – Part 3 (Privileges + Budget + Advanced Concepts)
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("==================================================")
print("BUILDING PARLIAMENT NOTES — PART 3")
print("==================================================")

part3_data = {
  "meta": {
    "topic_id": "polity_parliament_part_3",
    "repository_id": "polity_parliament",
    "display_title": "Parliament of India – Part 3",
    "part": 3,
    "total_parts": 3,
    "subject": "polity",
    "chapter": "Parliament of India",
    "language": "English + Tamil"
  },
  "metadata": {
    "topic_id": "polity_parliament_part_3",
    "repository_id": "polity_parliament",
    "display_title": "Parliament of India – Part 3",
    "part": 3,
    "total_parts": 3,
    "subject": "polity",
    "chapter": "Parliament of India",
    "language": "English + Tamil"
  },
  "keywords": [
    "Parliamentary Privileges",
    "Article 105",
    "Individual Privileges",
    "Collective Privileges",
    "Freedom of Speech",
    "Anti-Defection Law",
    "Tenth Schedule",
    "52nd Amendment Act 1985",
    "91st Amendment Act 2003",
    "Kihoto Hollohan Case 1992",
    "Annual Financial Statement",
    "Article 112",
    "Article 113",
    "Article 114",
    "Article 115",
    "Article 116",
    "Article 117",
    "Article 118",
    "Article 123",
    "Demands for Grants",
    "Cut Motions",
    "Appropriation Bill",
    "Finance Bill",
    "Vote on Account",
    "Supplementary Grants",
    "Excess Grant",
    "Consolidated Fund of India",
    "Public Account",
    "Contingency Fund",
    "Article 368",
    "Constitutional Amendment",
    "Parliamentary Sovereignty vs Constitutional Supremacy",
    "Basic Structure Doctrine",
    "TNPSC Master Polity Notes"
  ],
  "learning_outcomes": {
    "Understand": {
      "en": [
        "Master Parliamentary Privileges under Article 105: Individual privileges (Freedom of speech Art 105(2), Freedom from arrest in civil cases 40 days before/after session, Jury exemption) and Collective privileges (Publishing proceedings, secret sittings, punishing for contempt).",
        "Understand Anti-Defection Law under Tenth Schedule (52nd Amend 1985 & 91st Amend 2003): Grounds for disqualification, 2/3rd merger exception, 6-month rule for nominated members, and Speaker's decision subject to judicial review (Kihoto Hollohan 1992).",
        "Analyze the Parliamentary Budget Process under Articles 112 to 114: Presentation, General Discussion, Committee Scrutiny, Demands for Grants under Article 113 (Policy, Economy, Token Cut Motions, Guillotine), Appropriation Bill (Art 114), and Finance Bill (Art 117).",
        "Master Special Grants & Funds: Vote on Account & Vote on Credit (Article 116), Supplementary/Additional/Excess Grants (Article 115), Consolidated Fund (Art 266(1)), Public Account (Art 266(2)), and Contingency Fund (Art 267(1)).",
        "Master Constitutional Amendment under Article 368: Procedure, Special Majority, State Ratification for federal provisions, 24th Amend mandatory assent, and NO Joint Sitting rule.",
        "Evaluate Parliamentary Sovereignty vs Constitutional Supremacy: Limitations on Indian Parliament (Written Constitution, Federal structure, Fundamental Rights, Basic Structure Doctrine - Kesavananda Bharati 1973)."
      ],
      "ta": [
        "உறுப்பு 105-ன் கீழ் நாடாளுமன்றச் சலுகைகளில் தேர்ச்சி பெறுதல்: தனிநபர் சலுகைகள் (பேச்சுரிமை விதி 105(2), சிவில் வழக்குகளில் கைது செய்யப்படாமை 40 நாட்கள் முன்/பின், நடுவர் சபை விலக்கு) மற்றும் கூட்டுச் சலுகைகள் (நடவடிக்கைகளை வெளியிடுதல், இரகசிய தொடர், நீதிமன்ற அவமதிப்பிற்குத் தண்டித்தல்).",
        "பத்தாவது அட்டவணையின் கீழ் கட்சித் தாவல் தடைச் சட்டத்தைப் புரிந்துகொள்ளுதல் (52-வது திருத்தம் 1985 & 91-வது திருத்தம் 2003): தகுதியிழப்பு அடிப்படைகள், 2/3 பங்கு இணைப்பு விலக்கு, நியமன உறுப்பினர்களுக்கான 6 மாத விதி மற்றும் சபாநாயகரின் முடிவு நீதித்துறை ஆய்வுக்கு உட்பட்டது (கிஹோட்டோ ஹோலோஹான் 1992).",
        "உறுப்புகள் 112 முதல் 114 வரை நாடாளுமன்ற பட்ஜெட் நடைமுறையைப் பகுப்பாய்வு செய்தல்: சமர்ப்பிப்பு, பொது விவாதம், குழு பரிசீலனை, உறுப்பு 113-ன் கீழ் மானியக் கோரிக்கைகள் (கொள்கை, சிக்கன, அடையாள வெட்டுத் தீர்மானங்கள், கில்லட்டின்), ஒதுக்கீட்டு மசோதா (விதி 114) மற்றும் நிதி மசோதா (விதி 117).",
        "சிறப்பு மானியங்கள் & நிதிகளில் தேர்ச்சி பெறுதல்: கணக்கு வாக்கு & கடன் வாக்கு (உறுப்பு 116), கூடுதல்/மேலதிக/உபரி மானியங்கள் (உறுப்பு 115), தொகுப்பு நிதி (விதி 266(1)), பொதுக் கணக்கு (விதி 266(2)) மற்றும் அவசரக்கால நிதி (விதி 267(1)).",
        "உறுப்பு 368-ன் கீழ் அரசியலமைப்புத் திருத்தத்தில் தேர்ச்சி பெறுதல்: நடைமுறை, சிறப்பு பெரும்பான்மை, கூட்டாட்சி விதிகளுக்கு மாநில ஒப்புதல், 24-வது திருத்தம் கட்டாய ஒப்புதல் மற்றும் கூட்டுத் தொடர் இல்லை என்ற விதி.",
        "நாடாளுமன்ற இறையாண்மை vs அரசியலமைப்பு மேலாதிக்கத்தை மதிப்பீடு செய்தல்: இந்திய நாடாளுமன்றத்தின் வரம்புகள் (எழுதப்பட்ட அரசியலமைப்பு, கூட்டாட்சி அமைப்பு, அடிப்படை உரிமைகள், அடிப்படை கட்டமைப்பு கோட்பாடு - கேசவாநந்த பாரதி 1973)."
      ]
    }
  },
  "subject": "polity",
  "topic": "Parliament of India",
  "language": "English + Tamil",
  "ui_type": "standard_notes",
  "sections": [
    {
      "id": "sec_parliamentary_privileges",
      "title_en": "1. Parliamentary Privileges & Immunities (Article 105)",
      "title_ta": "1. நாடாளுமன்றச் சலுகைகள் & விலக்களிப்புகள் (உறுப்பு 105)",
      "type": "standard_topic"
    },
    {
      "id": "sec_anti_defection_law",
      "title_en": "2. Anti-Defection Law (Tenth Schedule & Amendments)",
      "title_ta": "2. கட்சித் தாவல் தடைச் சட்டம் (பத்தாவது அட்டவணை & திருத்தங்கள்)",
      "type": "standard_topic"
    },
    {
      "id": "sec_parliamentary_budget",
      "title_en": "3. Parliamentary Budget Process & Cut Motions (Articles 112, 113, 114)",
      "title_ta": "3. நாடாளுமன்ற பட்ஜெட் நடைமுறை & வெட்டுத் தீர்மானங்கள் (உறுப்புகள் 112, 113, 114)",
      "type": "standard_topic"
    },
    {
      "id": "sec_special_grants_funds",
      "title_en": "4. Special Grants, Vote on Account & Public Funds (Articles 115, 116, 266 & 267)",
      "title_ta": "4. சிறப்பு மானியங்கள், கணக்கு வாக்கு & பொது நிதிகள் (உறுப்புகள் 115, 116, 266 & 267)",
      "type": "standard_topic"
    },
    {
      "id": "sec_constitutional_amendment",
      "title_en": "5. Constitutional Amendment Power & Procedure (Article 368)",
      "title_ta": "5. அரசியலமைப்புத் திருத்த அதிகாரம் & நடைமுறை (உறுப்பு 368)",
      "type": "standard_topic"
    },
    {
      "id": "sec_sovereignty_vs_supremacy",
      "title_en": "6. Parliamentary Control over Executive & Parliamentary Sovereignty vs Constitutional Supremacy",
      "title_ta": "6. நிர்வாகத்தின் மீதான நாடாளுமன்றக் கட்டுப்பாடு & நாடாளுமன்ற இறையாண்மை vs அரசியலமைப்பு மேலாதிக்கம்",
      "type": "standard_topic"
    },
    {
      "id": "comparison_tables",
      "title_en": "7. Mandatory Advanced Comparison Tables (9 Tables)",
      "title_ta": "7. கட்டாய மேம்பட்ட ஒப்பீட்டு அட்டவணைகள் (9 அட்டவணைகள்)",
      "type": "comparison"
    },
    {
      "id": "mind_map",
      "title_en": "8. Master Mind Map & Top 25 TNPSC Traps",
      "title_ta": "8. முதன்மை மன வரைபடம் & சிறந்த 25 டிஎன்பிஎஸ்சி பொறிகள்",
      "type": "mind_map"
    }
  ],
  "content": {
    "definition": {
      "en": "Parliamentary Privileges (Article 105), Budgetary Control (Articles 112 to 116), Anti-Defection enforcement (Tenth Schedule), and Constitutional Amendment powers (Article 368) constitute the advanced operational mechanisms through which Parliament exercises financial oversight, maintains party discipline, and modifies the constitutional framework within defined supremacy limits.",
      "ta": "நாடாளுமன்றச் சலுகைகள் (உறுப்பு 105), பட்ஜெட் கட்டுப்பாடு (உறுப்புகள் 112 முதல் 116), கட்சித் தாவல் தடைச் சட்ட அமலாக்கம் (பத்தாவது அட்டவணை) மற்றும் அரசியலமைப்புத் திருத்த அதிகாரங்கள் (உறுப்பு 368) ஆகிய நாடாளுமன்றத்தின் மேம்பட்ட செயல்பாட்டு அமைப்புகளாகும்."
    },
    "introduction": {
      "en": "Part V (Articles 105, 112 to 118, 123) and Part XX (Article 368) along with the Tenth Schedule form the bedrock of advanced parliamentary functioning. While Indian Parliament possesses vast legislative and financial powers, its authority is bounded by Constitutional Supremacy and Judicial Review.",
      "ta": "பகுதி V (உறுப்புகள் 105, 112 முதல் 118, 123) மற்றும் பகுதி XX (உறுப்பு 368) பத்தாவது அட்டவணையுடன் இணைந்து மேம்பட்ட நாடாளுமன்றச் செயல்பாட்டின் அடித்தளமாக அமைகின்றன."
    },
    "sec_parliamentary_privileges": [
      {
        "title_en": "Article 105 — Privileges of Parliament & Its Members",
        "title_ta": "உறுப்பு 105 — நாடாளுமன்றம் & அதன் உறுப்பினர்களின் சலுகைகள்",
        "points": {
          "en": [
            "Definition: Special rights, immunities, and exemptions enjoyed by Houses of Parliament, their committees, and their members under Article 105 without which they cannot discharge their functions effectively.",
            "Individual Privileges (Enjoyed by Members personally):",
            "  1. Freedom of Speech in Parliament (Article 105(1) & (2)): No member is liable to any proceeding in any court in respect of anything said or any vote given by him in Parliament or any committee thereof.",
            "  2. Freedom from Arrest: Free from arrest in CIVIL CASES during the session of Parliament and 40 DAYS BEFORE and 40 DAYS AFTER a session. (CRITICAL TRAP: Freedom from arrest is NOT AVAILABLE in CRIMINAL CASES, Preventive Detention cases, or Contempt of Court!).",
            "  3. Exemption from Jury Service: Exempted from attending court as witnesses during parliamentary sessions.",
            "Collective Privileges (Enjoyed by House as a whole):",
            "  1. Right to publish debates and proceedings, and right to restrain publication by outsiders.",
            "  2. Right to exclude strangers from galleries and hold SECRET SITTINGS under Article 118 Rules.",
            "  3. Right to punish members and outsiders for breach of privilege or contempt of House (imprisonment or reprimand).",
            "  4. Right to receive immediate notification of arrest, detention, conviction, or release of a member.",
            "  5. Right to institute inquiries and summon witnesses.",
            "Privileges vs Fundamental Rights: M.S.M. Sharma case (1959) & Searchlight case established that parliamentary privileges under Article 105 prevail over Article 19(1)(a) freedom of speech outside, BUT are subject to Article 20(2), Article 21, and Article 22 fundamental rights."
          ],
          "ta": [
            "வரையறை: நாடாளுமன்ற அவைகள், அவற்றின் குழுக்கள் மற்றும் உறுப்பினர்கள் தங்கள் பணிகளைத் திறம்படச் செய்ய உறுப்பு 105-ன் கீழ் அனுபவிக்கும் சிறப்பு உரிமைகள், விலக்குகள் மற்றும் விடுவிப்புகள் ஆகும்.",
            "தனிநபர் சலுகைகள் (உறுப்பினர்கள் தனிப்பட்ட முறையில் அனுபவிப்பவை):",
            "  1. நாடாளுமன்றத்தில் பேச்சுரிமை (உறுப்பு 105(1) & (2)): நாடாளுமன்றத்தில் அல்லது அதன் குழுவில் பேசியவை அல்லது அளித்த வாக்கு தொடர்பாக எந்த உறுப்பினருக்கும் எந்த நீதிமன்றத்திலும் வழக்குத் தொடர முடியாது.",
            "  2. கைதிலிருந்து விலக்கு: நாடாளுமன்றக் கூட்டத்தொடர் நடைபெறும் போதும், தொடங்குவதற்கு 40 நாட்களுக்கு முன்னரும், முடிந்த 40 நாட்களுக்குப் பின்னரும் சிவில் வழக்குகளில் (Civil Cases) கைது செய்யப்படாமல் விலக்கு உண்டு. (முக்கியப் பொறி: குற்றவியல் வழக்குகள் - Criminal Cases, தடுப்புக் காவல் அல்லது நீதிமன்ற அவமதிப்பில் கைதிலிருந்து விலக்கு இல்லை!).",
            "  3. நடுவர் சபை சேவை விலக்கு: கூட்டத்தொடரின் போது நீதிமன்ற சாட்சியாக ஆஜராவதிலிருந்து விலக்கு உண்டு.",
            "கூட்டுச் சலுகைகள் (அவை முழுமையாக அனுபவிப்பவை):",
            "  1. விவாதங்கள் மற்றும் நடவடிக்கைகளை வெளியிடும் உரிமை, மற்றும் பிறர் வெளியிடுவதைத் தடுக்கும் உரிமை.",
            "  2. பார்வையாளர்களை வெளியேற்றி இரகசியத் தொடர் (Secret Sitting - உறுப்பு 118 விதிகள்) நடத்தும் உரிமை.",
            "  3. சலுகை மீறல் அல்லது அவை அவமதிப்பிற்கு உறுப்பினர்கள் மற்றும் வெளிநபர்களைத் தண்டிக்கும் உரிமை (சிறை அல்லது எச்சரிக்கை).",
            "  4. உறுப்பினர் கைது, தடுப்புக் காவல், தண்டனை அல்லது விடுதலை பற்றிய தகவலை உடனடியாகப் பெறும் உரிமை.",
            "  5. விசாரணைகளை அமைத்து சாட்சிகளை அழைக்கும் உரிமை.",
            "சலுகைகள் vs அடிப்படை உரிமைகள்: எம்.எஸ்.எம். சர்மா வழக்கு (1959) & சர்ச்ட்லைட் வழக்கில் உறுப்பு 105 நாடாளுமன்ற சலுகைகள் வெளியிலுள்ள விதி 19(1)(a) பேச்சுரிமையை விட மேலோங்கும், ஆனால் விதி 20(2), 21, 22 அடிப்படை உரிமைகளுக்கு உட்பட்டது என நிறுவப்பட்டது."
          ]
        }
      }
    ],
    "sec_anti_defection_law": [
      {
        "title_en": "Tenth Schedule — Anti-Defection Provisions & Case Laws",
        "title_ta": "பத்தாவது அட்டவணை — கட்சித் தாவல் தடை விதிகள் & வழக்குத் தீர்ப்புகள்",
        "points": {
          "en": [
            "Constitutional Basis: Added by the 52nd Constitutional Amendment Act 1985 (Tenth Schedule, Article 102(2) & 191(2)). Modified by 91st Constitutional Amendment Act 2003.",
            "Four Disqualification Grounds under 10th Schedule:",
            "  1. Voluntary Giving Up Membership: If an elected member voluntarily gives up membership of the political party on whose ticket he was elected. ('Voluntarily giving up' is wider than formal resignation; covers conduct/anti-party activities - Ravi Naik case 1994).",
            "  2. Voting Against Party Whip: If he votes or abstains from voting contrary to any direction issued by his party without prior permission and not condoned within 15 DAYS.",
            "  3. Independent Member Joining Party: If an independently elected member joins ANY political party after election.",
            "  4. Nominated Member Joining Party after 6 Months: If a nominated member joins a political party AFTER THE EXPIRY OF 6 MONTHS from taking seat. (Note: He CAN join a party within 6 months!).",
            "EXCEPTIONS (Where Defection does NOT cause disqualification):",
            "  • Merger Exception (91st Amend 2003): If a political party merges with another party and AT LEAST 2/3rds OF THE MEMBERS of the party agree to the merger.",
            "  • Presiding Officer Exception: If a member elected as Speaker/Chairman voluntarily resigns from his party upon election and re-joins after stepping down.",
            "Decision Making Authority: Question of disqualification under 10th Schedule is decided by the SPEAKER / CHAIRMAN of the concerned House.",
            "Judicial Review (Kihoto Hollohan v. Zachillhu 1992): Supreme Court held that Speaker/Chairman acts as a Quasi-Judicial Tribunal while deciding defection cases. Hence, the decision of Speaker is SUBJECT TO JUDICIAL REVIEW on grounds of mala fides, perversity, or violation of natural justice."
          ],
          "ta": [
            "அரசியலமைப்பு அடிப்படை: 1985-ஆம் ஆண்டின் 52-வது அரசியலமைப்புச் சட்டத்திருத்தம் மூலம் சேர்க்கப்பட்டது (பத்தாவது அட்டவணை, உறுப்புகள் 102(2) & 191(2)). 2003-ஆம் ஆண்டின் 91-வது திருத்தத்தால் மாற்றியமைக்கப்பட்டது.",
            "10-வது அட்டவணையின் கீழ் 4 தகுதியிழப்பு அடிப்படைகள்:",
            "  1. தானாக முன்வந்து கட்சி உறுப்பினர் பதவியை விடுதல்: தேர்தலில் போட்டியிட்டு வென்ற அரசியல் கட்சியின் உறுப்பினர் பதவியை தானாக விடுதல். ('தானாக விடுதல்' என்பது முறையான ராஜினாமாவை விடப் பரந்தது; கட்சி எதிர்ப்பு செயல்பாடுகளையும் உள்ளடக்கும் - ரவி நாயக் வழக்கு 1994).",
            "  2. கட்சி கொறடா உத்தரவிற்கு எதிராக வாக்களித்தல்: முன்-அனுமதியின்றி கட்சி கொறடா உத்தரவிற்கு எதிராக வாக்களித்தல் அல்லது வாக்களிப்பதைத் தவிர்த்தல் மற்றும் 15 நாட்களுக்குள் கட்சி அதை மன்னிக்காதிருத்தல்.",
            "  3. சுயேச்சை உறுப்பினர் கட்சியில் சேருதல்: சுயேச்சையாக வென்ற உறுப்பினர் தேர்தலுக்குப் பின் எந்தவொரு அரசியல் கட்சியிலும் சேருதல்.",
            "  4. நியமன உறுப்பினர் 6 மாதங்களுக்குப் பின் கட்சியில் சேருதல்: நியமிக்கப்பட்ட உறுப்பினர் பதவியேற்ற 6 மாதங்களுக்குப் பின் எந்தவொரு கட்சியிலும் சேருதல். (குறிப்பு: 6 மாதங்களுக்குள் அவர் கட்சியில் சேரலாம்!).",
            "விலக்குகள் (தகுதியிழப்பு ஏற்படாத சூழல்கள்):",
            "  • கட்சி இணைப்பு விலக்கு (91-வது திருத்தம் 2003): ஒரு அரசியல் கட்சி மற்றொரு கட்சியுடன் இணைய கட்டுப்பட்ட அவையின் குறைந்தபட்சம் 2/3 பங்கு உறுப்பினர்கள் ஒப்புக்கொண்டால்.",
            "  • அவைத் தலைவர் விலக்கு: சபாநாயகராகத் தேர்ந்தெடுக்கப்படும் நபர் தனது கட்சிப் பதவியை ராஜினாமா செய்து, பதவி முடிந்த பின் மீண்டும் சேருதல்.",
            "முடிவெடுக்கும் அதிகாரி: 10-வது அட்டவணையின் கீழ் தகுதியிழப்பு குறித்த கேள்வியைச் சம்மந்தப்பட்ட அவையின் சபாநாயகர் / தலைவர் தீர்மானிக்கிறார்.",
            "நீதிமன்ற ஆய்வு (கிஹோட்டோ ஹோலோஹான் v. ஜாச்சிலு 1992): கட்சித் தாவல் வழக்குகளைத் தீர்மானிக்கும் போது சபாநாயகர் ஒரு பகுதி-நீதிமன்ற அமைப்பாகச் (Quasi-Judicial Tribunal) செயல்படுகிறார். எனவே சபாநாயகரின் முடிவு நீதித்துறை ஆய்வுக்கு உட்பட்டது (Judicial Review) என உச்ச நீதிமன்றம் தீர்ப்பளித்தது."
          ]
        }
      }
    ],
    "sec_parliamentary_budget": [
      {
        "title_en": "Article 112 & Article 113 — Annual Financial Statement, Demands for Grants & Budget Stages",
        "title_ta": "உறுப்புகள் 112 & 113 — ஆண்டு நிதிநிலை அறிக்கை, மானியக் கோரிக்கைகள் & பட்ஜெட் நிலைகள்",
        "points": {
          "en": [
            "Annual Financial Statement (Article 112): Popularly known as the 'Budget'. Statement of estimated receipts and expenditure of Union Govt for that financial year (April 1 to March 31).",
            "Charged Expenditure vs Made Expenditure:",
            "  • Charged Expenditure (Article 112(3)): Non-votable by Parliament. Can only be discussed. (e.g. Salaries of President, Vice-President, Speaker, SC Judges, CAG, UPSC Chairman).",
            "  • Made Expenditure: Votable by Lok Sabha under Article 113.",
            "Article 113 Procedure for Demands for Grants:",
            "  • Estimates relating to expenditure charged on Consolidated Fund are not submitted to vote of Parliament (Article 113(1)).",
            "  • Estimates relating to other expenditure are submitted in form of Demands for Grants to Lok Sabha ONLY (Article 113(2)). Lok Sabha has power to assent, refuse, or reduce any demand.",
            "  • Recommendation of President Mandatory (Article 113(3)): No demand for a grant shall be made except on the recommendation of the President.",
            "Six Stages of Budget in Parliament:",
            "  1. Presentation of Budget (by Finance Minister in Lok Sabha).",
            "  2. General Discussion (on broad principles without voting).",
            "  3. Scrutiny by Departmental Standing Committees (House adjourned for 3-4 weeks for detailed scrutiny of demands).",
            "  4. Voting on Demands for Grants under Article 113 (LOK SABHA ONLY! Rajya Sabha has no voting power).",
            "  5. Passing of Appropriation Bill (Article 114).",
            "  6. Passing of Finance Bill (Article 117).",
            "Three Types of Cut Motions (Moved during Voting on Demands for Grants under Article 113):",
            "  1. Policy Cut Motion: Represents disapproval of policy underlying demand. States 'that the amount of demand be reduced to Re 1'.",
            "  2. Economy Cut Motion: Represents economy that can be effected. States 'that the amount of demand be reduced by a specified amount'.",
            "  3. Token Cut Motion: Ventilates a specific grievance within sphere of responsibility of GOI. States 'that the amount of demand be reduced by Rs 100'.",
            "Guillotine Mechanics: On the last day allotted for voting on demands for grants, the Speaker puts ALL remaining demands to vote immediately whether discussed or not."
          ],
          "ta": [
            "ஆண்டு நிதிநிலை அறிக்கை (உறுப்பு 112): பொதுவாக 'பட்ஜெட்' என அழைக்கப்படுகிறது. அந்த நிதியாண்டிற்கான (ஏப்ரல் 1 முதல் மார்ச் 31 வரை) மத்திய அரசின் மதிப்பிடப்பட்ட வரவு செலவு அறிக்கை.",
            "சுமத்தப்பட்ட செலவினம் vs வாக்கெடுப்புச் செலவினம்:",
            "  • சுமத்தப்பட்ட செலவினம் (உறுப்பு 112(3)): நாடாளுமன்றத்தால் வாக்களிக்கப்பட முடியாதது. விவாதிக்க மட்டுமே முடியும். (எ.கா. குடியரசுத் தலைவர், சபாநாயகர், உச்ச நீதிமன்ற நீதிபதிகள், CAG, UPSC தலைவரின் சம்பளங்கள்).",
            "  • வாக்கெடுப்புச் செலவினம்: உறுப்பு 113-ன் கீழ் மக்களவையால் வாக்களிக்கப்படக்கூடியது.",
            "உறுப்பு 113 மானியக் கோரிக்கைகள் நடைமுறை:",
            "  • இந்தியத் தொகுப்பு நிதியில் சுமத்தப்பட்ட செலவின மதிப்பீடுகள் நாடாளுமன்ற வாக்கெடுப்பிற்குப் சமர்ப்பிக்கப்படுவதில்லை (உறுப்பு 113(1)).",
            "  • இதர செலவின மதிப்பீடுகள் மானியக் கோரிக்கைகளாக மக்களவையில் மட்டுமே சமர்ப்பிக்கப்படுகின்றன (உறுப்பு 113(2)). மக்களவைக்கு ஒப்புதல் அளிக்க, மறுக்க அல்லது குறைக்க அதிகாரமுண்டு.",
            "  • குடியரசுத் தலைவர் பரிந்துரை கட்டாயம் (உறுப்பு 113(3)): குடியரசுத் தலைவரின் பரிந்துரையின்றி எந்தவொரு மானியக் கோரிக்கையும் கொண்டு வர முடியாது.",
            "நாடாளுமன்ற பட்ஜெட்டின் 6 நிலைகள்:",
            "  1. பட்ஜெட் சமர்ப்பிப்பு (மக்களவையில் நிதி அமைச்சரால்).",
            "  2. பொது விவாதம் (வாக்கெடுப்பின்றி பொதுக் கொள்கைகள் மீதான விவாதம்).",
            "  3. துறைசார் நிலைக்குழுக்களின் பரிசீலனை (கோரிக்கைகளை விரிவாகப் பரிசீலிக்க அவை 3-4 வாரங்கள் ஒத்திவைப்பு).",
            "  4. உறுப்பு 113-ன் கீழ் மானியக் கோரிக்கைகள் மீதான வாக்கெடுப்பு (மக்களவைக்கு மட்டுமே அதிகாரம்! மாநிலங்களவைக்கு வாக்கெடுப்பு அதிகாரமில்லை).",
            "  5. ஒதுக்கீட்டு மசோதா நிறைவேற்றம் (உறுப்பு 114).",
            "  6. நிதி மசோதா நிறைவேற்றம் (உறுப்பு 117).",
            "மூன்று வகை வெட்டுத் தீர்மானங்கள் (உறுப்பு 113 மானியக் கோரிக்கை வாக்கெடுப்பின் போது):",
            "  1. கொள்கை வெட்டுத் தீர்மானம் (Policy Cut): கோரிக்கையின் கொள்கையை நிராகரிப்பது. 'மானியத் தொகை 1 ரூபாயாகக் குறைக்கப்பட வேண்டும்' எனக் கூறும்.",
            "  2. சிக்கன வெட்டுத் தீர்மானம் (Economy Cut): செய்யப்பட வேண்டிய சிக்கனத்தைக் குறிப்பது. 'மானியத் தொகையில் ஒரு குறிப்பிட்ட தொகை குறைக்கப்பட வேண்டும்' எனக் கூறும்.",
            "  3. அடையாள வெட்டுத் தீர்மானம் (Token Cut): குறிப்பிட்ட குறைகளைத் தெரிவிப்பது. 'மானியத் தொகையில் 100 ரூபாய் குறைக்கப்பட வேண்டும்' எனக் கூறும்.",
            "கில்லட்டின் முறை (Guillotine): மானியக் கோரிக்கை வாக்கெடுப்பிற்கு ஒதுக்கப்பட்ட கடைசி நாளில், விவாதிக்கப்பட்டதோ இல்லையோ எஞ்சியுள்ள அனைத்து கோரிக்கைகளையும் சபாநாயகர் உடனடியாக ஒரே நேரத்தில் வாக்கெடுப்பிற்கு விடுவார்."
          ]
        }
      }
    ],
    "sec_special_grants_funds": [
      {
        "title_en": "Special Grants & Public Funds of India (Articles 114, 115, 116, 266, 267)",
        "title_ta": "சிறப்பு மானியங்கள் & இந்தியப் பொது நிதிகள் (உறுப்புகள் 114, 115, 116, 266, 267)",
        "points": {
          "en": [
            "Appropriation Bill (Article 114): Authorizes withdrawal of money from Consolidated Fund of India to meet voted grants and charged expenditure.",
            "Special Parliamentary Grants:",
            "  • Vote on Account (Article 116(1)(a)): Advance grant given to executive to meet interim expenditure before Budget is passed (usually 1/6th of total estimate for 2 months).",
            "  • Supplementary Grant (Article 115(1)(a)): Granted when amount authorized for a current service is found INSUFFICIENT.",
            "  • Additional Grant (Article 115(1)(a)): Granted when a need arises for expenditure upon a NEW SERVICE not contemplated in budget.",
            "  • Excess Grant (Article 115(1)(b)): Granted when money has been spent ON ANY SERVICE during a financial year IN EXCESS of the amount voted. Voted AFTER financial year by LS after PAC approval.",
            "  • Vote on Credit (Article 116(1)(b)): Granted for meeting an unexpected demand of indefinite character (e.g. war preparedness). Act as a 'BLANK CHEQUE' to executive.",
            "  • Exceptional Grant (Article 116(1)(c)): Granted for a special purpose, forming no part of current service.",
            "  • Token Grant (Article 115): Granted when funds to meet expenditure for a new service can be made available by re-appropriation (nominal sum of Re 1).",
            "Three Public Funds of India:",
            "  1. Consolidated Fund of India (Article 266(1)): All revenues received, loans raised, and loan repayments received by GOI. NO money withdrawn EXCEPT under Parliamentary Appropriation law (Article 114).",
            "  2. Public Account of India (Article 266(2)): Provident fund deposits, judicial deposits, savings deposits. Operated by executive action (No prior parliamentary law needed).",
            "  3. Contingency Fund of India (Article 267(1)): Created by Parliament by law. Placed at disposal of PRESIDENT to meet unforeseen expenditure pending authorization. Operated by Finance Secretary on President's behalf."
          ],
          "ta": [
            "ஒதுக்கீட்டு மசோதா (உறுப்பு 114): வாக்களிக்கப்பட்ட மானியங்கள் மற்றும் சுமத்தப்பட்ட செலவுகளைச் சந்திக்க இந்தியத் தொகுப்பு நிதியிலிருந்து பணம் எடுக்க அதிகாரமளிக்கிறது.",
            "சிறப்பு நாடாளுமன்ற மானியங்கள்:",
            "  • கணக்கு வாக்கு / வோட் ஆன் அக்கவுண்ட் (உறுப்பு 116(1)(a)): பட்ஜெட் நிறைவேறும் முன் இடைக்காலச் செலவுகளைச் சந்திக்க அரசுக்கு வழங்கப்படும் முன்பண மானியம் (பொதுவாக 2 மாதங்களுக்கு மொத்த மதிப்பீட்டில் 1/6 பங்கு).",
            "  • கூடுதல் மானியம் (Supplementary Grant - உறுப்பு 115(1)(a)): ஒரு நடைமுறைச் சேவைக்கு ஒதுக்கப்பட்ட தொகை போதவில்லை எனத் தெரியும் போது வழங்கப்படுவது.",
            "  • மேலதிக மானியம் (Additional Grant - உறுப்பு 115(1)(a)): பட்ஜெட்டில் குறிப்பிடப்படாத புதிய சேவைக்குச் செலவு செய்ய வேண்டிய சூழல் ஏற்படும் போது வழங்கப்படுவது.",
            "  • உபரி மானியம் (Excess Grant - உறுப்பு 115(1)(b)): ஒரு நிதியாண்டில் ஒரு சேவைக்கு வாக்களிக்கப்பட்ட தொகையை விட அதிகமாகச் செலவிடப்பட்ட பின் வழங்கப்படுவது. PAC ஒப்புதலுக்குப் பின் மக்களவையால் வாக்களிக்கப்படும்.",
            "  • கடன் வாக்கு / வோட் ஆன் கிரெடிட் (உறுப்பு 116(1)(b)): வரையறுக்க முடியாத அவசரக் கோரிக்கையைச் (எ.கா. போர் ஆயத்தம்) சந்திக்க வழங்கப்படுவது. அரசுக்கு வழங்கப்படும் 'வெற்றுக் காசோலை (Blank Cheque)'.",
            "  • விதிவிலக்கு மானியம் (Exceptional Grant - உறுப்பு 116(1)(c)): நடப்புச் சேவையின் பகுதியாக இல்லாத சிறப்பு நோக்கத்திற்காக வழங்கப்படுவது.",
            "  • அடையாள மானியம் (Token Grant - உறுப்பு 115): நிதி மறு-ஒதுக்கீடு மூலம் புதிய சேவைக்கு நிதி கிடைக்கும் போது அளிக்கப்படும் அடையாள மானியம் (அடையாளத் தொகை 1 ரூபாய்).",
            "இந்தியாவின் மூன்று பொது நிதிகள்:",
            "  1. இந்தியத் தொகுப்பு நிதி (Consolidated Fund - உறுப்பு 266(1)): அரசுக்கு வரும் அனைத்து வருவாய்கள், கடன்கள் மற்றும் கடன் திரும்பப் பெறுதல்கள். நாடாளுமன்ற ஒதுக்கீட்டுச் சட்டமின்றி (உறுப்பு 114) இதில் பணம் எடுக்க முடியாது.",
            "  2. இந்தியப் பொதுக் கணக்கு (Public Account - உறுப்பு 266(2)): வருங்கால வைப்பு நிதி வைப்புகள், நீதித்துறை வைப்புகள், சேமிப்பு வைப்புகள். நிர்வாக நடவடிக்கையால் இயக்கப்படுகிறது (முன் சட்டம் தேவையில்லை).",
            "  3. இந்திய அவசரக்கால நிதி (Contingency Fund - உறுப்பு 267(1)): நாடாளுமன்றச் சட்டத்தால் உருவாக்கப்பட்டது. எதிர்பாராத செலவுகளைச் சந்திக்க குடியரசுத் தலைவரின் கட்டுப்பாட்டில் வைக்கப்பட்டுள்ளது. குடியரசுத் தலைவர் சார்பில் நிதிச் செயலாளர் இயக்குகிறார்."
          ]
        }
      }
    ],
    "sec_constitutional_amendment": [
      {
        "title_en": "Article 368 — Constitutional Amendment Power & Procedure",
        "title_ta": "உறுப்பு 368 — அரசியலமைப்புத் திருத்த அதிகாரம் & நடைமுறை",
        "points": {
          "en": [
            "Constitutional Provision: Part XX Article 368 empowers Parliament to amend the Constitution by way of addition, variation, or repeal.",
            "Procedure under Article 368:",
            "  1. Introduced in EITHER House of Parliament (Cannot be introduced in State Legislature).",
            "  2. Can be introduced by a Minister or a Private Member.",
            "  3. DOES NOT require prior recommendation of President.",
            "  4. MUST be passed in EACH House separately by a SPECIAL MAJORITY (Majority of total membership of the House + 2/3rds of members present and voting).",
            "  5. NO Joint Sitting provision under Article 368 if a deadlock occurs between the two Houses!",
            "  6. Federal Provisions Ratification: If the Bill seeks to amend federal provisions (e.g. Art 54 election of President, Executive power extent Art 73/162, Supreme Court & High Courts, 7th Schedule lists, Representation in Parliament, Art 368 itself), it MUST be ratified by the Legislatures of AT LEAST HALF OF THE STATES by Simple Majority.",
            "President's Assent Mandatory: 24th Constitutional Amendment Act 1971 made it OBLIGATORY for the President to give assent to a Constitutional Amendment Bill under Article 368. President CANNOT withhold assent or return the Bill!"
          ],
          "ta": [
            "அரசியலமைப்பு விதி: பகுதி XX உறுப்பு 368 நாடாளுமன்றத்திற்கு அரசியலமைப்பைச் சேர்த்தல், மாறுதல் அல்லது ரத்து செய்தல் மூலம் திருத்துவதற்கு அதிகாரமளிக்கிறது.",
            "உறுப்பு 368-ன் கீழ் நடைமுறை:",
            "  1. நாடாளுமன்றத்தின் எந்தவொரு அவையிலும் அறிமுகப்படுத்தலாம் (மாநில சட்டமன்றத்தில் அறிமுகப்படுத்த முடியாது).",
            "  2. அமைச்சர் அல்லது தனிநபர் உறுப்பினரால் அறிமுகப்படுத்தப்படலாம்.",
            "  3. குடியரசுத் தலைவரின் முன் பரிந்துரை தேவையில்லை.",
            "  4. ஒவ்வொரு அவையிலும் தனித்தனியாகச் சிறப்பு பெரும்பான்மையால் (அவையின் மொத்த உறுப்பினர்களின் பெரும்பான்மை + பங்கேற்று வாக்களிப்பவர்களில் 2/3 பங்கு) நிறைவேற்றப்பட வேண்டும்.",
            "  5. இரு அவைகளுக்கும் இடையே முட்டுக் கட்டை ஏற்பட்டால் உறுப்பு 368-ன் கீழ் கூட்டுத் தொடர் விதி இல்லை!",
            "  6. கூட்டாட்சி விதிகளுக்கு மாநில ஒப்புதல்: மசோதா கூட்டாட்சி விதிகளைத் (எ.கா. குடியரசுத் தலைவர் தேர்தல் விதி 54, உயர்/உச்ச நீதிமன்றங்கள், 7-வது அட்டவணைப் பட்டியல்கள், விதி 368) திருத்த முயன்றால், குறைந்தபட்சம் பாதி மாநிலங்களின் சட்டமன்றங்கள் எளிய பெரும்பான்மையால் ஒப்புதல் அளிக்க வேண்டும்.",
            "குடியரசுத் தலைவர் கட்டாய ஒப்புதல்: 1971-ஆம் ஆண்டின் 24-வது அரசியலமைப்புச் சட்டத்திருத்தம் அரசியலமைப்புத் திருத்த மசோதாவிற்கு குடியரசுத் தலைவர் ஒப்புதல் அளிப்பதைக் கட்டாயமாக்கியது. குடியரசுத் தலைவர் ஒப்புதலை நிறுத்தவோ திருப்பவோ முடியாது!"
          ]
        }
      }
    ],
    "sec_sovereignty_vs_supremacy": [
      {
        "title_en": "Parliamentary Control & Sovereignty vs Constitutional Supremacy",
        "title_ta": "நிர்வாகக் கட்டுப்பாடு & நாடாளுமன்ற இறையாண்மை vs அரசியலமைப்பு மேலாதிக்கம்",
        "points": {
          "en": [
            "Executive Accountability Mechanisms: Parliament enforces collective responsibility (Article 75(3)) via Question Hour, Motions, Cut Motions, Budgetary voting under Article 113, and Committees.",
            "Is Indian Parliament Sovereign?: NO. Unlike British Parliament which is sovereign (can make/unmake any law and no court can declare it invalid), Indian Parliament is NOT a sovereign law-making body.",
            "Four Limitations on Indian Parliament:",
            "  1. Written Constitution: Parliament derives its powers from the Constitution and must operate within constitutional limits.",
            "  2. Federal System: Legislative authority is divided between Centre and States under 7th Schedule. Parliament cannot normally legislate on State List subjects.",
            "  3. Fundamental Rights & Judicial Review: Laws made by Parliament are subject to Judicial Review under Article 13. Courts can strike down unconstitutional laws.",
            "  4. Basic Structure Doctrine: Established in Kesavananda Bharati case (1973). Parliament has power to amend Constitution under Article 368, BUT CANNOT alter or destroy its 'Basic Structure'."
          ],
          "ta": [
            "நிர்வாகப் பொறுப்பு அமைப்புகள்: நாடாளுமன்றம் கேள்வி நேரம், தீர்மானங்கள், வெட்டுத் தீர்மானங்கள், உறுப்பு 113 பட்ஜெட் வாக்கெடுப்பு மற்றும் குழுக்கள் மூலம் கூட்டுப் பொறுப்பை (உறுப்பு 75(3)) உறுதி செய்கிறது.",
            "இந்திய நாடாளுமன்றம் இறையாண்மை கொண்டதா?: இல்லை. இறையாண்மை கொண்ட பிரிட்டிஷ் நாடாளுமன்றம் போலன்றி (எந்தச் சட்டத்தையும் உருவாக்கலாம்/நீக்கலாம், நீதிமன்றம் அதைச் செல்லாது எனக் கூற முடியாது), இந்திய நாடாளுமன்றம் வரம்பற்ற இறையாண்மை கொண்ட அமைப்பல்ல.",
            "இந்திய நாடாளுமன்றத்தின் நான்கு வரம்புகள்:",
            "  1. எழுதப்பட்ட அரசியலமைப்பு: நாடாளுமன்றம் தனது அதிகாரங்களை அரசியலமைப்பிலிருந்தே பெறுகிறது மற்றும் அதன் எல்லைகளுக்குள்ளேயே செயல்பட வேண்டும்.",
            "  2. கூட்டாட்சி அமைப்பு: 7-வது அட்டவணையின் கீழ் சட்டமன்ற அதிகாரம் மத்திய-மாநிலங்களுக்கு இடையே பிரிக்கப்பட்டுள்ளது. நாடாளுமன்றம் சாதாரண சூழலில் மாநிலப் பட்டியலில் சட்டமியற்ற முடியாது.",
            "  3. அடிப்படை உரிமைகள் & நீதித்துறை ஆய்வு: நாடாளுமன்றச் சட்டங்கள் உறுப்பு 13-ன் கீழ் நீதித்துறை ஆய்வுக்கு உட்பட்டவை. அரசியலமைப்புக்கு எதிரான சட்டங்களை நீதிமன்றங்கள் ரத்து செய்யலாம்.",
            "  4. அடிப்படை கட்டமைப்புக் கோட்பாடு: கேசவாநந்த பாரதி வழக்கில் (1973) நிறுவப்பட்டது. உறுப்பு 368-ன் கீழ் அரசியலமைப்பைத் திருத்த நாடாளுமன்றத்திற்கு அதிகாரமுண்டு, ஆனால் அதன் 'அடிப்படை கட்டமைப்பை' மாற்றவோ அழிக்கவோ முடியாது."
          ]
        }
      }
    ],
    "revision_cards": [
      {
        "id": "parl_p3_c1",
        "front_en": "What protection is granted to MPs for speeches made inside Parliament under Article 105(2)?",
        "front_ta": "உறுப்பு 105(2)-ன் கீழ் நாடாளுமன்றத்தில் பேசும் பேச்சுகளுக்கு எம்பிக்களுக்கு என்ன பாதுகாப்பு அளிக்கப்பட்டுள்ளது?",
        "back_en": "Full immunity: No member is liable to any proceeding in any court in respect of anything said or any vote given in Parliament.",
        "back_ta": "முழு சட்ட விலக்கு: நாடாளுமன்றத்தில் பேசியவை அல்லது அளித்த வாக்கு தொடர்பாக எந்த நீதிமன்றத்திலும் வழக்குத் தொடர முடியாது."
      },
      {
        "id": "parl_p3_c2",
        "front_en": "Does freedom from arrest under Article 105 apply to Criminal Cases?",
        "front_ta": "உறுப்பு 105-ன் கீழ் கைதிலிருந்து விலக்கு குற்றவியல் வழக்குகளுக்குப் (Criminal Cases) பொருந்துமா?",
        "back_en": "NO. Freedom from arrest applies ONLY to Civil Cases (40 days before/after session). NOT available in criminal cases or preventive detention.",
        "back_ta": "இல்லை. கைதிலிருந்து விலக்கு சிவில் வழக்குகளுக்கு மட்டுமே பொருந்தும் (40 நாட்கள் முன்/பின்). குற்றவியல் வழக்குகள் அல்லது தடுப்புக் காவலில் பொருந்தாது."
      },
      {
        "id": "parl_p3_c3",
        "front_en": "Under 10th Schedule, when does a Nominated Member get disqualified for joining a political party?",
        "front_ta": "10-வது அட்டவணையின் கீழ் ஒரு நியமன உறுப்பினர் அரசியல் கட்சியில் சேர்ந்தால் எப்போது தகுதியிழப்பு செய்யப்படுவார்?",
        "back_en": "If he joins a political party AFTER THE EXPIRY OF 6 MONTHS from taking seat. (He CAN join within 6 months!).",
        "back_ta": "பதவியேற்ற 6 மாதங்களுக்குப் பின் கட்சியில் சேர்ந்தால் தகுதியிழப்பு செய்யப்படுவார். (6 மாதங்களுக்குள் அவர் சேரலாம்!)."
      },
      {
        "id": "parl_p3_c4",
        "front_en": "What is the merger exception threshold under Tenth Schedule?",
        "front_ta": "பத்தாவது அட்டவணையின் கீழ் கட்சி இணைப்பு விலக்கிற்கான வரம்பு என்ன?",
        "back_en": "Merger requires agreement of AT LEAST 2/3rds OF THE MEMBERS of the political party (91st Amend 2003).",
        "back_ta": "கட்சி இணைப்புக்கு கட்சியின் குறைந்தபட்சம் 2/3 பங்கு உறுப்பினர்களின் ஒப்புதல் தேவை (91-வது திருத்தம் 2003)."
      },
      {
        "id": "parl_p3_c5",
        "front_en": "What is the decision of Supreme Court in Kihoto Hollohan case (1992) on Anti-Defection?",
        "front_ta": "கட்சித் தாவல் தடைச் சட்டம் குறித்த கிஹோட்டோ ஹோலோஹான் வழக்கில் (1992) உச்ச நீதிமன்றத்தின் தீர்ப்பு என்ன?",
        "back_en": "Speaker acts as a Quasi-Judicial Tribunal; Speaker's defection decision IS SUBJECT TO JUDICIAL REVIEW.",
        "back_ta": "சபாநாயகர் ஒரு பகுதி-நீதிமன்ற அமைப்பாகச் செயல்படுகிறார்; சபாநாயகரின் கட்சித் தாவல் முடிவு நீதித்துறை ஆய்வுக்கு உட்பட்டது."
      },
      {
        "id": "parl_p3_c6",
        "front_en": "What is a 'Policy Cut Motion' during Budget voting under Article 113?",
        "front_ta": "உறுப்பு 113 பட்ஜெட் வாக்கெடுப்பின் போது 'கொள்கை வெட்டுத் தீர்மானம் (Policy Cut)' என்றால் என்ன?",
        "back_en": "Represents disapproval of policy underlying demand; states that the amount of demand be REDUCED TO Re 1.",
        "back_ta": "கோரிக்கையின் கொள்கையை நிராகரிப்பதாகும்; மானியத் தொகை 1 ரூபாயாகக் குறைக்கப்பட வேண்டும் எனக் கூறும்."
      },
      {
        "id": "parl_p3_c7",
        "front_en": "What is 'Vote on Credit' under Article 116(1)(b)?",
        "front_ta": "உறுப்பு 116(1)(b)-ன் கீழ் 'கடன் வாக்கு (Vote on Credit)' என்றால் என்ன?",
        "back_en": "Granted for meeting an unexpected demand of indefinite character (e.g. war preparedness); acts as a 'BLANK CHEQUE' to executive.",
        "back_ta": "வரையறுக்க முடியாத அவசரக் கோரிக்கையைச் (எ.கா. போர் ஆயத்தம்) சந்திக்க வழங்கப்படுவது; அரசுக்கு வழங்கப்படும் 'வெற்றுக் காசோலை'."
      },
      {
        "id": "parl_p3_c8",
        "front_en": "What grant is voted by Lok Sabha AFTER the financial year for money spent in excess?",
        "front_ta": "அதிகமாகச் செலவிடப்பட்ட பணத்திற்காக நிதியாண்டு முடிந்த பின் மக்களவையால் வாக்களிக்கப்படும் மானியம் எது?",
        "back_en": "EXCESS GRANT under Article 115(1)(b) (Voted after financial year upon PAC approval).",
        "back_ta": "உறுப்பு 115(1)(b)-ன் கீழ் உபரி மானியம் (Excess Grant) (PAC ஒப்புதலுக்குப் பின் நிதியாண்டு முடிந்து வாக்களிக்கப்படுவது)."
      },
      {
        "id": "parl_p3_c9",
        "front_en": "Is Joint Sitting allowed for Constitutional Amendment Bills under Article 368?",
        "front_ta": "உறுப்பு 368-ன் கீழ் அரசியலமைப்புத் திருத்த மசோதாக்களுக்குக் கூட்டுத் தொடர் அனுமதிக்கப்படுமா?",
        "back_en": "NO. Constitutional Amendment Bills MUST be passed by each House separately by Special Majority.",
        "back_ta": "இல்லை. அரசியலமைப்புத் திருத்த மசோதாக்கள் ஒவ்வொரு அவையிலும் தனித்தனியாக சிறப்பு பெரும்பான்மையால் நிறைவேற்றப்பட வேண்டும்."
      },
      {
        "id": "parl_p3_c10",
        "front_en": "Did the 24th Constitutional Amendment Act 1971 make President's assent mandatory for Amendment Bills?",
        "front_ta": "1971-ஆம் ஆண்டின் 24-வது திருத்தம் திருத்த மசோதாக்களுக்கு குடியரசுத் தலைவரின் ஒப்புதலைக் கட்டாயமாக்கியதா?",
        "back_en": "YES. 24th Amendment 1971 made it obligatory for President to give assent to Constitutional Amendment Bills.",
        "back_ta": "ஆம். 1971 24-வது திருத்தம் அரசியலமைப்புத் திருத்த மசோதாக்களுக்கு குடியரசுத் தலைவர் ஒப்புதல் அளிப்பதைக் கட்டாயமாக்கியது."
      },
      {
        "id": "parl_p3_c11",
        "front_en": "Under Article 267(1), who operates the Contingency Fund of India?",
        "front_ta": "உறுப்பு 267(1)-ன் கீழ் இந்திய அவசரக்கால நிதியை இயக்குபவர் யார்?",
        "back_en": "Finance Secretary operates it on behalf of the PRESIDENT OF INDIA.",
        "back_ta": "இந்தியக் குடியரசுத் தலைவர் சார்பில் நிதிச் செயலாளர் இயக்குகிறார்."
      },
      {
        "id": "parl_p3_c12",
        "front_en": "Why is the Indian Parliament NOT a sovereign law-making body?",
        "front_ta": "இந்திய நாடாளுமன்றம் ஏன் வரம்பற்ற இறையாண்மை கொண்ட அமைப்பல்ல?",
        "back_en": "Because it is limited by Written Constitution, Federal system, Fundamental Rights, and Basic Structure Doctrine.",
        "back_ta": "ஏனெனில் அது எழுதப்பட்ட அரசியலமைப்பு, கூட்டாட்சி அமைப்பு, அடிப்படை உரிமைகள் மற்றும் அடிப்படை கட்டமைப்புக் கோட்பாட்டால் வரையறுக்கப்பட்டுள்ளது."
      }
    ],
    "comparison_tables": [
      {
        "id": "tbl_privileges_vs_fr_p3",
        "title_en": "1. Parliamentary Privileges vs Fundamental Rights Comparison",
        "title_ta": "1. நாடாளுமன்றச் சலுகைகள் vs அடிப்படை உரிமைகள் ஒப்பீடு",
        "headers_en": ["Feature / Dimension", "Parliamentary Privileges (Art 105)", "Fundamental Rights (Part III)"],
        "headers_ta": ["அம்சம் / காரணி", "நாடாளுமன்றச் சலுகைகள் (விதி 105)", "அடிப்படை உரிமைகள் (பகுதி III)"],
        "rows_en": [
          ["Beneficiaries", "Houses of Parliament, Committees, and MPs only", "All Citizens (and Persons for certain rights)"],
          ["Constitutional Source", "Article 105 (and conventions/laws)", "Articles 12 to 35 (Part III)"],
          ["Freedom of Speech Scope", "Absolute immunity inside Parliament for official speech (Art 105(2))", "Subject to reasonable restrictions under Art 19(2)"],
          ["Conflict Precedence", "Privileges prevail over Art 19(1)(a) inside House (Searchlight Case)", "Privileges are subject to Art 20(2), 21, and 22 fundamental rights"],
          ["Judicial Enforcement", "House itself punishes breach of privilege", "Supreme Court (Art 32) and High Courts (Art 226) enforce FRs"]
        ],
        "rows_ta": [
          ["பயனாளிகள்", "நாடாளுமன்ற அவைகள், குழுக்கள் மற்றும் எம்பிக்கள் மட்டுமே", "அனைத்துக் குடிமக்கள் (மற்றும் சில உரிமைகளுக்கு நபர்கள்)"],
          ["அரசியலமைப்பு ஆதாரம்", "உறுப்பு 105 (மற்றும் மரபுகள்/சட்டங்கள்)", "உறுப்புகள் 12 முதல் 35 வரை (பகுதி III)"],
          ["பேச்சுரிமை எல்லை", "அவைக்குள் அதிகாரப்பூர்வ பேச்சிற்கு முற்றுரிமைச் சட்ட விலக்கு (விதி 105(2))", "விதி 19(2)-ன் கீழ் நியாயமான கட்டுப்பாடுகளுக்கு உட்பட்டது"],
          ["முரண்பாடு முன்னுரிமை", "அவைக்குள் சலுகைகள் விதி 19(1)(a)-வை விட மேலோங்கும் (சர்ச்ட்லைட் வழக்கு)", "சலுகைகள் விதி 20(2), 21, 22 அடிப்படை உரிமைகளுக்கு உட்பட்டவை"],
          ["நீதிமன்ற அமலாக்கம்", "சலுகை மீறலை அவையே தண்டிக்கும்", "உச்ச நீதிமன்றம் (விதி 32) & உயர் நீதிமன்றங்கள் (விதி 226) அமல்படுத்துகின்றன"]
        ]
      },
      {
        "id": "tbl_ind_vs_coll_priv_p3",
        "title_en": "2. Individual Privileges vs Collective Privileges Comparison",
        "title_ta": "2. தனிநபர் சலுகைகள் vs கூட்டுச் சலுகைகள் ஒப்பீடு",
        "headers_en": ["Aspect", "Individual Privileges (Art 105)", "Collective Privileges (Art 105)"],
        "headers_ta": ["கூறு", "தனிநபர் சலுகைகள் (உறுப்பு 105)", "கூட்டுச் சலுகைகள் (உறுப்பு 105)"],
        "rows_en": [
          ["Enjoyed By", "Enjoyed by members of Parliament individually", "Enjoyed by each House of Parliament collectively as a body"],
          ["Speech Immunity", "No member liable in court for speech or vote in House", "House has right to publish or restrain publication of debates"],
          ["Arrest Immunity", "Freedom from arrest in CIVIL cases 40 days before/after session", "House has right to receive immediate notice of member's arrest/release"],
          ["Jury Service", "Exempted from jury service and court witness duty during session", "Right to exclude strangers and hold SECRET SITTINGS under Article 118"],
          ["Punishment Power", "Individual cannot punish anyone", "House has power to punish members/outsiders for contempt/breach"]
        ],
        "rows_ta": [
          ["அனுபவிப்பவர்", "நாடாளுமன்ற உறுப்பினர்களால் தனிப்பட்ட முறையில் அனுபவிக்கப்படுபவை", "நாடாளுமன்றத்தின் ஒவ்வொரு அவையாலும் கூட்டாக அனுபவிக்கப்படுபவை"],
          ["பேச்சுச் சட்ட விலக்கு", "அவையில் பேசிய பேச்சிற்கு எந்த உறுப்பினரும் நீதிமன்றத்திற்குப் பொறுப்பல்ல", "விவாதங்களை வெளியிட அல்லது வெளியீட்டைத் தடுக்க அவைக்கு உரிமையுண்டு"],
          ["கைது விலக்கு", "சிவில் வழக்குகளில் கூட்டத்தொடரின் 40 நாட்கள் முன்/பின் கைதிலிருந்து விலக்கு", "உறுப்பினரின் கைது/விடுதலை தகவலை உடனடியாகப் பெற அவைக்கு உரிமையுண்டு"],
          ["நடுவர் சபை சேவை", "கூட்டத்தொடரின் போது நீதிமன்ற சாட்சி மற்றும் நடுவர் சேவையிலிருந்து விலக்கு", "பார்வையாளர்களை வெளியேற்றி இரகசியக் கூட்டம் (Secret Sitting - விதி 118) நடத்தும் உரிமை"],
          ["தண்டனை அதிகாரம்", "தனிநபர் எவரையும் தண்டிக்க முடியாது", "அவமதிப்பிற்கு உறுப்பினர்கள்/வெளிநபர்களைத் தண்டிக்கும் அதிகாரம் அவைக்கு உண்டு"]
        ]
      },
      {
        "id": "tbl_antidef_vs_disqual_p3",
        "title_en": "3. Anti-Defection Disqualification vs Ordinary Disqualification",
        "title_ta": "3. கட்சித் தாவல் தகுதியிழப்பு vs சாதாரணத் தகுதியிழப்பு ஒப்பீடு",
        "headers_en": ["Parameter", "Anti-Defection Disqualification (Tenth Schedule)", "Ordinary Disqualification (Article 102(1))"],
        "headers_ta": ["அளவுரு", "கட்சித் தாவல் தகுதியிழப்பு (10-வது அட்டவணை)", "சாதாரணத் தகுதியிழப்பு (உறுப்பு 102(1))"],
        "rows_en": [
          ["Constitutional Provision", "Tenth Schedule (Art 102(2) & 191(2)) added by 52nd Amend 1985", "Article 102(1) (Office of profit, unsound mind, insolvency, non-citizen)"],
          ["Deciding Authority", "Speaker of Lok Sabha / Chairman of Rajya Sabha", "PRESIDENT OF INDIA (on binding opinion of Election Commission under Article 103)"],
          ["Grounds", "Voluntarily giving up party, voting against whip, joining party after election", "Holding office of profit, insolvency, unsound mind, foreign citizenship"],
          ["Merger Exception", "2/3rd members merging party is EXEMPTED from disqualification", "No merger exception concept in ordinary disqualifications"],
          ["Judicial Review", "Subject to Judicial Review (Kihoto Hollohan 1992)", "Decided by President after ECI opinion; final subject to writ jurisdiction"]
        ],
        "rows_ta": [
          ["அரசியலமைப்பு விதி", "10-வது அட்டவணை (விதி 102(2) & 191(2)) 52-வது திருத்தம் 1985", "உறுப்பு 102(1) (ஆதாயம் தரும் பதவி, மனநிலை, வங்கி நொடிப்பு, வெளிநாட்டு குடியுரிமை)"],
          ["முடிவெடுக்கும் அதிகாரி", "மக்களவைச் சபாநாயகர் / மாநிலங்களவைத் தலைவர்", "இந்தியக் குடியரசுத் தலைவர் (உறுப்பு 103 கீழ் இந்தியத் தேர்தல் ஆணையத்தின் ஆலோசனையின் பேரில்)"],
          ["அடிப்படைகள்", "கட்சி உறுப்பினர் பதவி விலகல், கொறடா மீறல், தேர்தலுக்குப் பின் கட்சியில் சேருதல்", "ஆதாயம் தரும் பதவி, வங்கி நொடிப்பு, மனநிலை சரியின்மை, வெளிநாட்டு குடியுரிமை"],
          ["இணைப்பு விலக்கு", "2/3 பங்கு உறுப்பினர்கள் கட்சி இணைப்பிற்கு தகுதியிழப்பிலிருந்து விலக்கு உண்டு", "சாதாரணத் தகுதியிழப்பில் கட்சி இணைப்பு கருத்து இல்லை"],
          ["நீதிமன்ற ஆய்வு", "நீதித்துறை ஆய்வுக்கு உட்பட்டது (கிஹோட்டோ ஹோலோஹான் 1992)", "ECI ஆலோசனையுடன் குடியரசுத் தலைவர் முடிவு; பேராணை வரம்பிற்கு உட்பட்டது"]
        ]
      },
      {
        "id": "tbl_appr_vs_fin_bill_p3",
        "title_en": "4. Appropriation Bill vs Finance Bill Comparison",
        "title_ta": "4. ஒதுக்கீட்டு மசோதா vs நிதி மசோதா ஒப்பீடு",
        "headers_en": ["Feature", "Appropriation Bill (Article 114)", "Finance Bill (Article 117)"],
        "headers_ta": ["அம்சம்", "ஒதுக்கீட்டு மசோதா (உறுப்பு 114)", "நிதி மசோதா (உறுப்பு 117)"],
        "rows_en": [
          ["Primary Purpose", "Authorizes withdrawal of money from Consolidated Fund for voted grants under Article 113", "Imposes, alters, or regulates taxation proposals for the financial year"],
          ["Nature of Bill", "Certified as a Money Bill under Article 110", "Certified as a Money Bill (or Financial Bill Type I/II under Article 117)"],
          ["Amendment Restriction", "NO amendment can be proposed that varies amount or destination of grant", "Amendments can be proposed seeking reduction or abolition of taxes"],
          ["Passage Order", "Passed BEFORE the Finance Bill during Budget session", "Passed AFTER the Appropriation Bill during Budget session"],
          ["Constitutional Deadline", "Must be passed to allow lawful spending from April 1", "Must be passed within 75 days of presentation (Taxation Act 1931)"]
        ],
        "rows_ta": [
          ["முதன்மை நோக்கம்", "உறுப்பு 113 வாக்களிக்கப்பட்ட மானியங்களுக்கு இந்தியத் தொகுப்பு நிதியிலிருந்து பணம் எடுக்க அதிகாரமளிப்பது", "நிதியாண்டிற்கான வரி விதிப்புகள், மாற்றங்கள் அல்லது ஒழுங்குமுறைகளை அமல்படுத்துவது"],
          ["மசோதாவின் தன்மை", "உறுப்பு 110-ன் கீழ் பண மசோதாவாகச் சான்றளிக்கப்படுகிறது", "பண மசோதா (அல்லது உறுப்பு 117 கீழ் நிதி மசோதா வகை I/II) ஆகச் சான்றளிக்கப்படுகிறது"],
          ["திருத்தக் கட்டுப்பாடு", "மானியத் தொகை அல்லது நோக்கத்தை மாற்றும் எந்தத் திருத்தமும் கொண்டு வர முடியாது", "வரிகளைக் குறைக்க அல்லது ரத்து செய்ய திருத்தங்களைக் கொண்டு வரலாம்"],
          ["நிறைவேற்றும் வரிசை", "பட்ஜெட் கூட்டத்தொடரில் நிதி மசோதாவிற்கு முன்பே நிறைவேற்றப்படும்", "பட்ஜெட் கூட்டத்தொடரில் ஒதுக்கீட்டு மசோதாவிற்குப் பின் நிறைவேற்றப்படும்"],
          ["அரசியலமைப்பு காலக்கெடு", "ஏப்ரல் 1 முதல் சட்டப்பூர்வமாகச் செலவழிக்க நிறைவேற்றப்பட வேண்டும்", "சமர்ப்பிக்கப்பட்ட 75 நாட்களுக்குள் நிறைவேற்றப்பட வேண்டும் (வரிவிதிப்புச் சட்டம் 1931)"]
        ]
      },
      {
        "id": "tbl_voa_vs_voc_p3",
        "title_en": "5. Vote on Account vs Vote on Credit Comparison",
        "title_ta": "5. கணக்கு வாக்கு vs கடன் வாக்கு ஒப்பீடு",
        "headers_en": ["Parameter", "Vote on Account (Article 116(1)(a))", "Vote on Credit (Article 116(1)(b))"],
        "headers_ta": ["அளவுரு", "கணக்கு வாக்கு / வோட் ஆன் அக்கவுண்ட் (விதி 116(1)(a))", "கடன் வாக்கு / வோட் ஆன் கிரெடிட் (விதி 116(1)(b))"],
        "rows_en": [
          ["Purpose", "Grant for meeting estimated interim expenditure pending Budget enactment", "Grant for meeting unexpected demand of indefinite character"],
          ["Nature of Demand", "Regular, routine annual expenditure items in budget under Article 113", "Unexpected, emergency demand (e.g. war or national crisis)"],
          ["Quantum", "Usually 1/6th of total estimate for a period of 2 months", "Blank cheque; amount depends on magnitude of emergency"],
          ["Details Provided", "Full details of estimated demands provided to Parliament", "Detailed expenditure cannot be stated due to nature of service"],
          ["Frequency", "Passed every financial year before April 1", "Passed rarely during war or national emergency contingencies"]
        ],
        "rows_ta": [
          ["நோக்கம்", "பட்ஜெட் நிறைவேறும் முன் இடைக்கால மதிப்பிடப்பட்ட செலவுகளைச் சந்திக்க வழங்கப்படும் மானியம்", "வரையறுக்க முடியாத அவசரக் கோரிக்கையைச் சந்திக்க வழங்கப்படும் மானியம்"],
          ["கோரிக்கையின் தன்மை", "உறுப்பு 113 பட்ஜெட்டில் உள்ள வழக்கமான, தினசரி ஆண்டுச் செலவினத் தலைப்புகள்", "எதிர்பாராத அவசரக் கோரிக்கை (எ.கா. போர் அல்லது தேசிய நெருக்கடி)"],
          ["தொகை அளவு", "பொதுவாக 2 மாதங்களுக்கு மொத்த மதிப்பீட்டில் 1/6 பங்கு", "வெற்றுக் காசோலை (Blank Cheque); தொகை அவசரநிலை அளவைப் பொறுத்தது"],
          ["வழங்கப்பட்ட விவரங்கள்", "மதிப்பிடப்பட்ட கோரிக்கைகளின் முழு விவரங்களும் நாடாளுமன்றத்திற்கு வழங்கப்படும்", "சேவையின் தன்மை காரணமாக விரிவான செலவினங்களைக் குறிப்பிட முடியாது"],
          ["அதிர்வெண்", "ஒவ்வொரு நிதியாண்டும் ஏப்ரல் 1-க்கு முன் வழக்கமாக நிறைவேற்றப்படும்", "போர் அல்லது தேசிய அவசரநிலைகளின் போது அரிதாக நிறைவேற்றப்படும்"]
        ]
      },
      {
        "id": "tbl_grants_comparison_p3",
        "title_en": "6. Supplementary vs Additional vs Excess Grant Comparison",
        "title_ta": "6. கூடுதல் vs மேலதிக vs உபரி மானியங்கள் ஒப்பீடு",
        "headers_en": ["Feature", "Supplementary Grant (Art 115(1)(a))", "Additional Grant (Art 115(1)(a))", "Excess Grant (Art 115(1)(b))"],
        "headers_ta": ["அம்சம்", "கூடுதல் மானியம் (Supplementary)", "மேலதிக மானியம் (Additional)", "உபரி மானியம் (Excess Grant)"],
        "rows_en": [
          ["Condition", "Authorized amount for a current service is INSUFFICIENT", "Need arises for expenditure on a NEW SERVICE not in budget", "Money SPENT IN EXCESS of voted amount during financial year"],
          ["Timing of Grant", "Voted during current financial year when money runs short", "Voted during current financial year when new service arises", "Voted AFTER the expiry of financial year"],
          ["PAC Role", "Standard parliamentary voting procedure", "Standard parliamentary voting procedure", "MUST be examined and approved by PAC before voting in Lok Sabha"],
          ["New Service Element", "Applies to existing service already voted in budget", "Applies exclusively to a NEW service not in original budget", "Applies to over-spending on an existing service"]
        ],
        "rows_ta": [
          ["நிபந்தனை", "நடப்புச் சேவைக்கு ஒதுக்கப்பட்ட தொகை போதவில்லை எனத் தெரியும் போது", "பட்ஜெட்டில் இல்லாத புதிய சேவைக்குச் செலவு செய்ய தேவைப்படும் போது", "நிதியாண்டில் வாக்களிக்கப்பட்ட தொகையை விட அதிகமாகச் செலவிடப்பட்ட பின்"],
          ["மானிய நேரம்", "பணம் பற்றாக்குறை ஏற்படும் போது நடப்பு நிதியாண்டில் வாக்களிக்கப்படும்", "புதிய சேவை ஏற்படும் போது நடப்பு நிதியாண்டில் வாக்களிக்கப்படும்", "நிதியாண்டு முடிந்த பின்னரே வாக்களிக்கப்படும்"],
          ["PAC பங்கு", "வழக்கமான நாடாளுமன்ற வாக்கெடுப்பு நடைமுறை", "வழக்கமான நாடாளுமன்ற வாக்கெடுப்பு நடைமுறை", "மக்களவையில் வாக்களிப்பதற்கு முன் PAC கட்டாயம் ஆய்வு செய்து ஒப்புதல் அளிக்க வேண்டும்"],
          ["புதிய சேவை அம்சம்", "பட்ஜெட்டில் ஏற்கனவே வாக்களிக்கப்பட்ட நடப்புச் சேவைக்குப் பொருந்தும்", "மூல பட்ஜெட்டில் இல்லாத புதிய சேவைக்கு மட்டுமே பொருந்தும்", "ஏற்கனவே உள்ள சேவையில் கூடுதல் செலவு செய்ததற்குப் பொருந்தும்"]
        ]
      },
      {
        "id": "tbl_ord_vs_amend_bill_p3",
        "title_en": "7. Ordinary Bill vs Constitutional Amendment Bill Comparison",
        "title_ta": "7. சாதாரண மசோதா vs அரசியலமைப்புத் திருத்த மசோதா ஒப்பீடு",
        "headers_en": ["Feature", "Ordinary Bill (Article 107)", "Constitutional Amendment Bill (Article 368)"],
        "headers_ta": ["அம்சம்", "சாதாரண மசோதா (உறுப்பு 107)", "அரசியலமைப்புத் திருத்த மசோதா (உறுப்பு 368)"],
        "rows_en": [
          ["Voting Majority", "Simple Majority of members present and voting", "SPECIAL MAJORITY (Total membership majority + 2/3rd present & voting)"],
          ["Joint Sitting Provision", "APPLICABLE under Article 108 if deadlock occurs", "NO Joint Sitting allowed under Article 368"],
          ["State Ratification", "State ratification is never required", "Required by AT LEAST HALF of States for federal amendments"],
          ["President's Assent", "President can Assent, Withhold, or Return for reconsideration (Art 111)", "President MUST give assent (24th Amend 1971; cannot return)"],
          ["House of Origin", "Can be introduced in either Lok Sabha or Rajya Sabha", "Can be introduced in either Lok Sabha or Rajya Sabha"]
        ],
        "rows_ta": [
          ["வாக்கெடுப்பு பெரும்பான்மை", "பங்கேற்று வாக்களிக்கும் உறுப்பினர்களின் எளிய பெரும்பான்மை", "சிறப்பு பெரும்பான்மை (மொத்த உறுப்பினர் பெரும்பான்மை + 2/3 பங்கு பங்கேற்று வாக்களிப்பு)"],
          ["கூட்டுத் தொடர் விதி", "முட்டுக் கட்டையின் போது உறுப்பு 108-ன் கீழ் பொருந்தும்", "உறுப்பு 368-ன் கீழ் கூட்டுத் தொடர் அனுமதி இல்லை"],
          ["மாநில ஒப்புதல்", "மாநில சட்டமன்றங்களின் ஒப்புதல் ஒருபோதும் தேவையில்லை", "கூட்டாட்சித் திருத்தங்களுக்குக் குறைந்தபட்சம் பாதி மாநிலங்களின் ஒப்புதல் தேவை"],
          ["குடியரசுத் தலைவர் ஒப்புதல்", "ஒப்புதல் அளிக்கலாம், நிறுத்தலாம் அல்லது மறுபரிசீலனைக்குத் திருப்பலாம் (விதி 111)", "குடியரசுத் தலைவர் கட்டாயம் ஒப்புதல் அளிக்க வேண்டும் (24-வது திருத்தம் 1971)"],
          ["தொடங்கும் அவை", "மக்களவை அல்லது மாநிலங்களவை இரண்டிலும் அறிமுகப்படுத்தலாம்", "மக்களவை அல்லது மாநிலங்களவை இரண்டிலும் அறிமுகப்படுத்தலாம்"]
        ]
      },
      {
        "id": "tbl_sovereignty_vs_limitation_p3",
        "title_en": "8. Parliament's Legislative Power vs Constitutional Limitations",
        "title_ta": "8. நாடாளுமன்றச் சட்டமன்ற அதிகாரம் vs அரசியலமைப்பு வரம்புகள்",
        "headers_en": ["Dimension", "Parliament's Power", "Constitutional Limitation"],
        "headers_ta": ["அம்சம்", "நாடாளுமன்ற அதிகாரம்", "அரசியலமைப்பு வரம்பு"],
        "rows_en": [
          ["Law Making Scope", "Can legislate on Union List (100) & Concurrent List", "Cannot normally legislate on State List (61) except under Art 249/250/252/253"],
          ["Constitutional Amendment", "Can amend Constitution under Article 368", "CANNOT alter or destroy 'Basic Structure' (Kesavananda Bharati 1973)"],
          ["Fundamental Rights", "Can restrict Fundamental Rights by law under Art 19(2)-(6)", "Laws violating FRs are void under Art 13 (Judicial Review)"],
          ["Territorial Extent", "Can make laws for whole or any part of India (Art 245)", "Subject to Presidential/Gubernatorial modifications in Sch V/VI areas"]
        ],
        "rows_ta": [
          ["சட்டமியற்றும் எல்லை", "மத்தியப் பட்டியல் (100) & பொதுப் பட்டியலில் சட்டமியற்றலாம்", "விதி 249/250/252/253 தவிர சாதாரண சூழலில் மாநிலப் பட்டியலில் சட்டமியற்ற முடியாது"],
          ["அரசியலமைப்புத் திருத்தம்", "உறுப்பு 368-ன் கீழ் அரசியலமைப்பைத் திருத்தலாம்", "அரசியலமைப்பின் 'அடிப்படை கட்டமைப்பை' மாற்றவோ அழிக்கவோ முடியாது (கேசவாநந்த பாரதி)"],
          ["அடிப்படை உரிமைகள்", "விதி 19(2)-(6) கீழ் சட்டத்தின் மூலம் அடிப்படை உரிமைகளைக் கட்டுப்படுத்தலாம்", "அடிப்படை உரிமைகளை மீறும் சட்டங்கள் விதி 13-ன் கீழ் செல்லாது (நீதிமன்ற ஆய்வு)"],
          ["நிலப்பரப்பு எல்லை", "இந்தியா முழுவதற்கும் அல்லது எந்தப் பகுதிக்கும் சட்டமியற்றலாம் (விதி 245)", "அட்டவணை V/VI பகுதிகளில் குடியரசுத் தலைவர்/ஆளுநர் மாற்றங்களுக்கு உட்பட்டது"]
        ]
      },
      {
        "id": "tbl_accountability_vs_review_p3",
        "title_en": "9. Parliamentary Accountability vs Judicial Review Comparison",
        "title_ta": "9. நாடாளுமன்றப் பொறுப்புக்கூறல் vs நீதித்துறை ஆய்வு ஒப்பீடு",
        "headers_en": ["Feature", "Parliamentary Accountability (Legislative Control)", "Judicial Review (Judicial Control)"],
        "headers_ta": ["அம்சம்", "நாடாளுமன்றப் பொறுப்புக்கூறல் (சட்டமன்றக் கட்டுப்பாடு)", "நீதித்துறை ஆய்வு (நீதிமன்றக் கட்டுப்பாடு)"],
        "rows_en": [
          ["Primary Organ", "Legislature (Parliament)", "Judiciary (Supreme Court & High Courts)"],
          ["Target of Control", "Executive (Council of Ministers under Art 75(3))", "Both Executive actions and Legislative enactments"],
          ["Key Tools", "Questions, Motions, Budget voting under Art 113, Committees (PAC, Estimates)", "Writs (Art 32/226), Judicial strike down of ultra vires laws (Art 13)"],
          ["Timing of Check", "Continuous, real-time control during parliamentary sessions", "Post-enactment check when challenged by affected citizens"]
        ],
        "rows_ta": [
          ["முதன்மை உறுப்பு", "சட்டமன்றம் (நாடாளுமன்றம்)", "நீதித்துறை (உச்ச நீதிமன்றம் & உயர் நீதிமன்றங்கள்)"],
          ["கட்டுப்பாட்டின் இலக்கு", "நிர்வாகம் (விதி 75(3) கீழ் அமைச்சரவை)", "நிர்வாக நடவடிக்கைகள் மற்றும் சட்டமன்றச் சட்டங்கள் இரண்டுமே"],
          ["முக்கியக் கருவிகள்", "கேள்விகள், தீர்மானங்கள், உறுப்பு 113 பட்ஜெட் வாக்கெடுப்பு, குழுக்கள் (PAC, மதிப்பீடு)", "பேராணைகள் (விதி 32/226), அரசியலமைப்புக்கு எதிரான சட்டங்களை ரத்து செய்தல் (விதி 13)"],
          ["கட்டுப்பாட்டு நேரம்", "நாடாளுமன்றக் கூட்டத்தொடர்களின் போது தொடர்ச்சியான, உடனுக்குடனான கட்டுப்பாடு", "பாதிக்கப்பட்ட குடிமக்களால் சவால் செய்யப்படும் போது சட்டமியற்றப்பட்ட பின் ஆய்வு"]
        ]
      }
    ],
    "mind_map": [
      {
        "title": "Parliament Privileges, Budget & Advanced Concepts (Part V & XX)",
        "short_label": "Parliament Part 3",
        "children": [
          {
            "title": "1. Parliamentary Privileges (Art 105)",
            "short_label": "Privileges",
            "children": [
              {"title": "Individual: Freedom of speech (Art 105(2)); Civil arrest immunity 40 days; Jury exemption", "short_label": "Individual"},
              {"title": "Collective: Right to publish proceedings, Secret sittings (Art 118), Punish for contempt", "short_label": "Collective"}
            ]
          },
          {
            "title": "2. Anti-Defection Law (10th Schedule)",
            "short_label": "Anti-Defection",
            "children": [
              {"title": "52nd Amend 1985 & 91st Amend 2003 (Art 102(2)): 4 grounds of disqualification", "short_label": "Grounds"},
              {"title": "2/3rd merger exception; Speaker decision subject to Judicial Review (Kihoto Hollohan 1992)", "short_label": "Kihoto 1992"}
            ]
          },
          {
            "title": "3. Budget & Financial Control (Art 112-118, 266, 267)",
            "short_label": "Budget & Funds",
            "children": [
              {"title": "Art 112 AFS Budget; Art 113 Demands for Grants & Cut Motions (Policy Re 1, Economy, Token Rs 100); Art 114 Appropriation Bill", "short_label": "Budget Stages"},
              {"title": "Art 116: Vote on Account (interim 1/6th) & Vote on Credit (blank cheque)", "short_label": "Special Grants"},
              {"title": "Art 115: Supplementary, Additional & Excess Grants (PAC approval needed)", "short_label": "Grants"},
              {"title": "Funds: Consolidated Fund (Art 266(1)), Public Account (Art 266(2)), Contingency Fund (Art 267(1))", "short_label": "Funds"}
            ]
          },
          {
            "title": "4. Amendment & Sovereignty (Art 368)",
            "short_label": "Amendment & Sovereignty",
            "children": [
              {"title": "Art 368: Special Majority; 1/2 State ratification for federal laws; NO Joint Sitting; Assent mandatory (24th Amend)", "short_label": "Art 368"},
              {"title": "Constitutional Supremacy: Limited by Written Constitution, FRs (Art 13), Federalism & Basic Structure (Kesavananda 1973)", "short_label": "Supremacy"}
            ]
          }
        ]
      }
    ],
    "tnpsc_traps": [
      {
        "title": "1. Article 105 Arrest Immunity Trap (கைது விலக்கு வரம்புப் பொறி)",
        "points": {
          "en": [
            "TRAP: Believing MPs cannot be arrested under any circumstances during parliamentary sessions.",
            "FACT: Freedom from arrest under Article 105 applies ONLY to CIVIL CASES (40 days before/after session). It DOES NOT apply to Criminal Cases, Preventive Detention, or Contempt of Court!"
          ],
          "ta": [
            "பொறி: நாடாளுமன்றக் கூட்டத்தொடரின் போது எம்பிக்களை எந்தச் சூழலிலும் கைது செய்ய முடியாது என நினைப்பது.",
            "உண்மை: உறுப்பு 105-ன் கீழ் கைதிலிருந்து விலக்கு சிவில் வழக்குகளுக்கு மட்டுமே பொருந்தும் (40 நாட்கள் முன்/பின்). குற்றவியல் வழக்குகள், தடுப்புக் காவல் அல்லது நீதிமன்ற அவமதிப்பில் கைதிலிருந்து விலக்கு இல்லை!"
          ]
        }
      },
      {
        "title": "2. Nominated Member Defection 6-Month Rule Trap (நியமன உறுப்பினர் கட்சித் தாவல் 6 மாத விதியைப் பொறி)",
        "points": {
          "en": [
            "TRAP: Thinking a nominated member gets disqualified if he joins a party immediately after taking seat.",
            "FACT: A nominated member is allowed to join ANY political party WITHIN 6 MONTHS of taking his seat. Disqualification under 10th Schedule (Art 102(2)) occurs ONLY if he joins a political party AFTER 6 MONTHS!"
          ],
          "ta": [
            "பொறி: நியமிக்கப்பட்ட உறுப்பினர் பதவியேற்றவுடன் கட்சியில் சேர்ந்தால் தகுதியிழப்பு செய்யப்படுவார் என நினைப்பது.",
            "உண்மை: நியமன உறுப்பினர் பதவியேற்ற 6 மாதங்களுக்குள் எந்தக் கட்சியிலும் சேர அனுமதிக்கப்படுகிறார். 6 மாதங்கள் முடிந்த பின்னரே கட்சியில் சேர்ந்தால் மட்டுமே 10-வது அட்டவணையின் கீழ் தகுதியிழப்பு ஏற்படும்!"
          ]
        }
      },
      {
        "title": "3. Article 368 Joint Sitting Exclusion Trap (அரசியலமைப்புத் திருத்தக் கூட்டுத் தொடர் பொறி)",
        "points": {
          "en": [
            "TRAP: Assuming a Joint Sitting can be summoned if Lok Sabha and Rajya Sabha disagree on a Constitutional Amendment Bill.",
            "FACT: There is NO PROVISION for a Joint Sitting under Article 368. A Constitutional Amendment Bill MUST be passed by EACH House separately by Special Majority!"
          ],
          "ta": [
            "பொறி: அரசியலமைப்புத் திருத்த மசோதாவில் முட்டுக் கட்டை ஏற்பட்டால் கூட்டுத் தொடரைக் கூட்டலாம் என நினைப்பது.",
            "உண்மை: உறுப்பு 368-ன் கீழ் கூட்டுத் தொடருக்கு வழியில்லை. அரசியலமைப்புத் திருத்த மசோதா ஒவ்வொரு அவையிலும் தனித்தனியாகச் சிறப்பு பெரும்பான்மையால் நிறைவேற்றப்பட வேண்டும்!"
          ]
        }
      },
      {
        "title": "4. Vote on Account vs Vote on Credit Trap (கணக்கு வாக்கு vs கடன் வாக்குக் குழப்பப் பொறி)",
        "points": {
          "en": [
            "TRAP: Confusing Vote on Account with Vote on Credit.",
            "FACT: Vote on Account (Article 116(1)(a)) is an interim grant for routine budget expenditure pending Budget enactment. Vote on Credit (Article 116(1)(b)) is a 'BLANK CHEQUE' for unexpected emergency demands of indefinite character (e.g. war)."
          ],
          "ta": [
            "பொறி: கணக்கு வாக்கையும் (Vote on Account) கடன் வாக்கையும் (Vote on Credit) குழப்பிக் கொள்ளுதல்.",
            "உண்மை: கணக்கு வாக்கு என்பது பட்ஜெட் நிறைவேறும் முன் வழக்கமான இடைக்காலச் செலவுகளுக்கு வழங்கப்படுவது. கடன் வாக்கு என்பது அவசரக் கோரிக்கைகளுக்கு அரசுக்கு வழங்கப்படும் 'வெற்றுக் காசோலை' ஆகும்."
          ]
        }
      },
      {
        "title": "5. Excess Grant Approval Order Trap (உபரி மானிய ஒப்புதல் வரிசைப் பொறி)",
        "points": {
          "en": [
            "TRAP: Believing Excess Grant is voted before the financial year begins.",
            "FACT: Excess Grant (Article 115(1)(b)) is voted AFTER the expiry of the financial year for money spent in excess, and MUST be examined and recommended by the Public Accounts Committee (PAC) before Lok Sabha voting."
          ],
          "ta": [
            "பொறி: உபரி மானியம் நிதியாண்டு தொடங்கும் முன் வாக்களிக்கப்படுகிறது என நினைப்பது.",
            "உண்மை: உபரி மானியம் நிதியாண்டு முடிந்த பின்னரே அதிகமாகச் செலவிட்ட தொகைகளுக்காக வாக்களிக்கப்படும், மேலும் மக்களவை வாக்களிப்பதற்கு முன் PAC கட்டாயம் ஆய்வு செய்ய வேண்டும்."
          ]
        }
      }
    ],
    "quick_revision": {
      "en": [
        "Parliamentary Privileges: Article 105. Individual: Freedom of speech inside House (Art 105(2)), Civil arrest immunity (40 days before/after session). Collective: Publishing proceedings, secret sittings (Art 118), contempt punishment.",
        "Anti-Defection: Tenth Schedule (52nd Amend 1985 & 91st Amend 2003, Art 102(2)). Disqualification: Voluntary resignation, voting against whip, independent joining party, nominated member joining party AFTER 6 months. Merger exception: 2/3rd members. Speaker decision subject to Judicial Review (Kihoto Hollohan 1992).",
        "Budget: Article 112 (Annual Financial Statement), Article 113 (Demands for Grants). Cut Motions: Policy Cut (reduce to Re 1), Economy Cut (specified amount), Token Cut (reduce by Rs 100). Guillotine on last day. Appropriation Bill (Art 114) & Finance Bill (Art 117).",
        "Grants: Vote on Account (Art 116(1)(a) interim grant), Vote on Credit (Art 116(1)(b) blank cheque for war), Supplementary Grant (Art 115), Excess Grant (Art 115 after financial year + PAC approval).",
        "Funds: Consolidated Fund (Art 266(1) law needed), Public Account (Art 266(2) executive), Contingency Fund (Art 267(1) President/Finance Sec).",
        "Amendment: Article 368 (Special Majority, 1/2 State ratification for federal laws, NO Joint Sitting, President assent mandatory via 24th Amend 1971).",
        "Sovereignty: Indian Parliament is NOT sovereign; limited by Written Constitution, FRs (Art 13), Federalism, and Basic Structure (Kesavananda Bharati 1973)."
      ],
      "ta": [
        "நாடாளுமன்றச் சலுகைகள்: உறுப்பு 105. தனிநபர்: அவைக்குள் பேச்சுரிமை (விதி 105(2)), சிவில் கைது விலக்கு (40 நாட்கள் முன்/பின்). கூட்டு: நடவடிக்கைகளை வெளியிடுதல், இரகசிய தொடர் (விதி 118), அவமதிப்புத் தண்டனை.",
        "கட்சித் தாவல் தடை: பத்தாவது அட்டவணை (52-வது திருத்தம் 1985 & 91-வது திருத்தம் 2003, விதி 102(2)). தகுதியிழப்பு: தானாக விலகல், கொறடா மீறல், சுயேச்சை கட்சியில் சேருதல், நியமன உறுப்பினர் 6 மாதத்திற்குப் பின் சேருதல். இணைப்பு விலக்கு: 2/3 பங்கு. சபாநாயகர் முடிவு நீதிமன்ற ஆய்வுக்கு உட்பட்டது (கிஹோட்டோ 1992).",
        "பட்ஜெட்: உறுப்பு 112 (ஆண்டு நிதிநிலை அறிக்கை), உறுப்பு 113 (மானியக் கோரிக்கைகள்). வெட்டுத் தீர்மானங்கள்: கொள்கை வெட்டு (1 ரூபாயாகக் குறைப்பு), சிக்கன வெட்டு (குறிப்பிட்ட தொகை), அடையாள வெட்டு (100 ரூபாய் குறைப்பு). கடைசி நாளில் கில்லட்டின். ஒதுக்கீட்டு மசோதா (விதி 114) & நிதி மசோதா (விதி 117).",
        "மானியங்கள்: கணக்கு வாக்கு (விதி 116(1)(a) இடைக்காலம்), கடன் வாக்கு (விதி 116(1)(b) வெற்றுக் காசோலை), கூடுதல் மானியம் (விதி 115), உபரி மானியம் (விதி 115 நிதியாண்டு பின் + PAC ஒப்புதல்).",
        "நிதிகள்: தொகுப்பு நிதி (விதி 266(1) சட்டம் தேவை), பொதுக் கணக்கு (விதி 266(2) நிர்வாகம்), அவசரக்கால நிதி (விதி 267(1) குடியரசுத் தலைவர்/நிதிச் செயலாளர்).",
        "திருத்தம்: உறுப்பு 368 (சிறப்பு பெரும்பான்மை, கூட்டாட்சிக்கு 1/2 மாநில ஒப்புதல், கூட்டுத் தொடர் இல்லை, 24-வது திருத்தம் மூலம் கட்டாய ஒப்புதல்).",
        "இறையாண்மை: இந்திய நாடாளுமன்றம் வரம்பற்ற இறையாண்மை கொண்டதல்ல; எழுதப்பட்ட அரசியலமைப்பு, அடிப்படை உரிமைகள் (விதி 13), கூட்டாட்சி மற்றும் அடிப்படை கட்டமைப்பால் வரையறுக்கப்பட்டது (கேசவாநந்த பாரதி 1973)."
      ]
    },
    "must_remember": {
      "en": [
        "MUST REMEMBER: Freedom from arrest (Art 105) applies ONLY to Civil Cases (40 days before/after), NOT Criminal Cases.",
        "MUST REMEMBER: Nominated member is disqualified under 10th Schedule ONLY if he joins a party AFTER 6 MONTHS.",
        "MUST REMEMBER: 2/3rd members agreement needed for party merger exception under Tenth Schedule.",
        "MUST REMEMBER: Speaker's anti-defection decision IS subject to Judicial Review (Kihoto Hollohan 1992).",
        "MUST REMEMBER: Article 113 governs the procedure for Demands for Grants in Lok Sabha.",
        "MUST REMEMBER: Policy Cut Motion states 'that the amount of demand be reduced to Re 1'.",
        "MUST REMEMBER: Excess Grant (Art 115(1)(b)) requires prior PAC examination before voting in Lok Sabha.",
        "MUST REMEMBER: Constitutional Amendment Bills under Article 368 CANNOT have a Joint Sitting.",
        "MUST REMEMBER: 24th Amendment 1971 made President's assent mandatory for Constitutional Amendment Bills.",
        "MUST REMEMBER: Indian Parliament is NOT sovereign; limited by Basic Structure Doctrine (Kesavananda Bharati 1973)."
      ],
      "ta": [
        "நினைவில் கொள்க: கைதிலிருந்து விலக்கு (விதி 105) சிவில் வழக்குகளுக்கு மட்டுமே பொருந்தும் (40 நாட்கள் முன்/பின்), குற்றவியல் வழக்குகளுக்கு இல்லை.",
        "நினைவில் கொள்க: நியமன உறுப்பினர் 6 மாதங்களுக்குப் பின் கட்சியில் சேர்ந்தால் மட்டுமே 10-வது அட்டவணையின் கீழ் தகுதியிழப்பு செய்யப்படுவார்.",
        "நினைவில் கொள்க: 10-வது அட்டவணையின் கீழ் கட்சி இணைப்பு விலக்கிற்கு 2/3 பங்கு உறுப்பினர்களின் ஒப்புதல் தேவை.",
        "நினைவில் கொள்க: சபாநாயகரின் கட்சித் தாவல் முடிவு நீதித்துறை ஆய்வுக்கு உட்பட்டது (கிஹோட்டோ ஹோலோஹான் 1992).",
        "நினைவில் கொள்க: உறுப்பு 113 மக்களவையில் மானியக் கோரிக்கைகளுக்கான நடைமுறையை வரையறுக்கிறது.",
        "நினைவில் கொள்க: கொள்கை வெட்டுத் தீர்மானம் 'மானியத் தொகை 1 ரூபாயாகக் குறைக்கப்பட வேண்டும்' எனக் கூறும்.",
        "நினைவில் கொள்க: உபரி மானியத்திற்கு (விதி 115(1)(b)) மக்களவை வாக்களிப்பதற்கு முன் PAC கட்டாயம் ஆய்வு செய்ய வேண்டும்.",
        "நினைவில் கொள்க: உறுப்பு 368-ன் கீழ் அரசியலமைப்புத் திருத்த மசோதாக்களுக்குக் கூட்டுத் தொடர் கூட்ட முடியாது.",
        "நினைவில் கொள்க: 1971 24-வது திருத்தம் திருத்த மசோதாக்களுக்கு குடியரசுத் தலைவர் ஒப்புதலைக் கட்டாயமாக்கியது.",
        "நினைவில் கொள்க: இந்திய நாடாளுமன்றம் வரம்பற்ற இறையாண்மை கொண்டதல்ல; அடிப்படை கட்டமைப்புக் கோட்பாட்டால் வரையறுக்கப்பட்டது (கேசவாநந்த பாரதி 1973)."
      ]
    }
  }
}

target_file = "data/notes/polity/parliament_part_3.json"
os.makedirs("data/notes/polity", exist_ok=True)

with open(target_file, "w", encoding="utf-8") as f:
  json.dump(part3_data, f, ensure_ascii=False, indent=2)

print(f"✅ Parliament Part 3 successfully updated with explicit Article tags and saved to: {target_file}")
