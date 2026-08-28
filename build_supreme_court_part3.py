# -*- coding: utf-8 -*-
"""
Builder Script for Supreme Court of India Notes — Part 3
Subject: Indian Polity
Topic: Supreme Court of India – Part 3 (Advanced Constitutional Concepts)
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("==================================================")
print("BUILDING SUPREME COURT NOTES — PART 3")
print("==================================================")

part3_data = {
  "meta": {
    "topic_id": "polity_supreme_court_part_3",
    "repository_id": "polity_supreme_court",
    "display_title": "Supreme Court of India – Part 3",
    "part": 3,
    "total_parts": 3,
    "subject": "polity",
    "chapter": "Supreme Court of India",
    "language": "English + Tamil"
  },
  "metadata": {
    "topic_id": "polity_supreme_court_part_3",
    "repository_id": "polity_supreme_court",
    "display_title": "Supreme Court of India – Part 3",
    "part": 3,
    "total_parts": 3,
    "subject": "polity",
    "chapter": "Supreme Court of India",
    "language": "English + Tamil"
  },
  "keywords": [
    "Judicial Review",
    "Judicial Activism",
    "Judicial Restraint",
    "Public Interest Litigation",
    "PIL",
    "Locus Standi Relaxation",
    "Justice V.R. Krishna Iyer",
    "Justice P.N. Bhagwati",
    "Epistolary Jurisdiction",
    "Basic Structure Doctrine",
    "Kesavananda Bharati Case 1973",
    "Golaknath Case 1967",
    "Minerva Mills Case 1980",
    "S.R. Bommai Case 1994",
    "I.R. Coelho Case 2007",
    "Maneka Gandhi Case 1978",
    "NJAC Fourth Judges Case 2015",
    "Collegium System Evolution",
    "Separation of Powers",
    "Judicial Independence Safeguards",
    "Article 32 vs Article 226",
    "TNPSC Master Polity Notes"
  ],
  "learning_outcomes": {
    "Understand": {
      "en": [
        "Master Judicial Review: Meaning, constitutional basis (Arts 13, 32, 131-136, 141, 246), and scope over legislative and executive actions.",
        "Differentiate Judicial Activism vs Judicial Restraint: Proactive protection of public interest and fundamental rights vs self-imposed judicial discipline and respect for separation of powers.",
        "Understand Public Interest Litigation (PIL): Relaxation of locus standi, pioneers (Justice Krishna Iyer & Justice P.N. Bhagwati), epistolary jurisdiction, and anti-misuse safeguards.",
        "Master the Basic Structure Doctrine: Landmark ruling in Kesavananda Bharati (1973) limiting Article 368 amending power, and subsequent landmark cases (Minerva Mills, S.R. Bommai, I.R. Coelho).",
        "Understand the Collegium System vs Constitutional Text: Judicially evolved 4-tier senior judge consultation mechanism vs Article 124(2) text, and invalidation of NJAC (99th Amend).",
        "Analyze Separation of Powers and Judicial Independence: Advanced institutional safeguards (security of tenure, charged expenses Art 146, conduct discussion ban Art 121, practice ban Art 124(7), contempt Art 129).",
        "Master Landmark Supreme Court Cases: Facts, core principles, dates, and exam significance."
      ],
      "ta": [
        "நீதித்துறை ஆய்வில் தேர்ச்சி பெறுதல்: பொருள், அரசியலமைப்பு அடிப்படை (விதிகள் 13, 32, 131-136, 141, 246) மற்றும் சட்டமன்ற/நிர்வாக நடவடிக்கைகளின் மீதான எல்லை.",
        "நீதித்துறை செயலாக்கம் vs நீதித்துறை சுயகட்டுப்பாடு வேறுபாடு: பொது நலன்/அடிப்படை உரிமைகளை முன்வந்து பாதுகாத்தல் vs அதிகாரப் பகிர்வை மதித்து சுயமாக விதிக்கும் கட்டுப்பாடுகள்.",
        "பொது நல வழக்கைப் (PIL) புரிந்துகொள்ளுதல்: Locus standi தளர்வு, முன்னோடி நீதிபதிகள் (கிருஷ்ணய்யர் & பகவதி), கடித வடிவிலான ஆதிக்கம் மற்றும் துஷ்பிரயோகத் தடுப்புகள்.",
        "அடிப்படை கட்டமைப்புக் கோட்பாட்டில் தேர்ச்சி பெறுதல்: கேசவாநந்த பாரதி (1973) வரலாற்றுத் தீர்ப்பு (விதி 368 வரம்பு) மற்றும் தொடர் வழக்குகள் (மினெர்வா மில்ஸ், எஸ்.ஆர். பொம்மை, ஐ.ஆர். கோயல்ஹோ).",
        "கொலீஜியம் vs அரசியலமைப்பு விதியை உணர்தல்: நீதித்துறையால் உருவாக்கப்பட்ட 4 மூத்த நீதிபதிகள் கலந்தாய்வு vs விதி 124(2) உரை மற்றும் NJAC ரத்து (99-வது திருத்தம்).",
        "அதிகாரப் பகிர்வு மற்றும் நீதித்துறை சுதந்திரத்தைப் பகுப்பாய்வு செய்தல்: மேம்பட்ட நிறுவனப் பாதுகாப்புகள் (பதவிப் பாதுகாப்பு, தொகுப்பு நிதி செலவுகள் விதி 146, விவாதத் தடை விதி 121, பயிற்சித் தடை விதி 124(7), அவமதிப்பு விதி 129).",
        "முக்கிய வரலாற்றுச் சிறப்புமிக்க உச்ச நீதிமன்ற வழக்குகளில் தேர்ச்சி பெறுதல்: வழக்கு பெயர்கள், கோட்பாடுகள், ஆண்டுகள் மற்றும் தேர்வு முக்கியத்துவம்."
      ]
    }
  },
  "subject": "polity",
  "topic": "Supreme Court of India",
  "language": "English + Tamil",
  "ui_type": "standard_notes",
  "sections": [
    {
      "id": "sec_judicial_review_deep",
      "title_en": "1. Judicial Review — Scope, Constitutional Basis & Principles",
      "title_ta": "1. நீதித்துறை ஆய்வு — எல்லை, அரசியலமைப்பு அடிப்படை & கோட்பாடுகள்",
      "type": "standard_topic"
    },
    {
      "id": "sec_activism_vs_restraint",
      "title_en": "2. Judicial Activism vs Judicial Restraint",
      "title_ta": "2. நீதித்துறை செயலாக்கம் vs நீதித்துறை சுயகட்டுப்பாடு",
      "type": "standard_topic"
    },
    {
      "id": "sec_pil_public_interest",
      "title_en": "3. Public Interest Litigation (PIL) & Locus Standi Relaxation",
      "title_ta": "3. பொது நல வழக்கு (PIL) & Locus Standi கோட்பாட்டுத் தளர்வு",
      "type": "standard_topic"
    },
    {
      "id": "sec_basic_structure_cases",
      "title_en": "4. Basic Structure Doctrine & Evolution of Constitutional Amendments",
      "title_ta": "4. அடிப்படை கட்டமைப்புக் கோட்பாடு & அரசியலமைப்புத் திருத்தங்களின் வளர்ச்சி",
      "type": "standard_topic"
    },
    {
      "id": "sec_collegium_njac_history",
      "title_en": "5. Collegium System Evolution vs NJAC Invalidation (99th Amendment)",
      "title_ta": "5. கொலீஜியம் அமைப்பின் வளர்ச்சி vs NJAC ரத்து (99-வது திருத்தம்)",
      "type": "standard_topic"
    },
    {
      "id": "sec_separation_independence",
      "title_en": "6. Separation of Powers & Advanced Judicial Independence Safeguards",
      "title_ta": "6. அதிகாரப் பகிர்வு & மேம்பட்ட நீதித்துறை சுதந்திரப் பாதுகாப்புகள்",
      "type": "standard_topic"
    },
    {
      "id": "sec_landmark_cases_summary",
      "title_en": "7. Summary of Landmark Supreme Court Cases",
      "title_ta": "7. வரலாற்றுச் சிறப்புமிக்க உச்ச நீதிமன்ற வழக்குகளின் தொகுப்பு",
      "type": "standard_topic"
    },
    {
      "id": "comparison_tables",
      "title_en": "8. Mandatory Advanced Comparison Tables (9 Tables)",
      "title_ta": "8. கட்டாய மேம்பட்ட ஒப்பீட்டு அட்டவணைகள் (9 அட்டவணைகள்)",
      "type": "comparison"
    },
    {
      "id": "mind_map",
      "title_en": "9. Master Mind Map & Top 25 TNPSC Traps",
      "title_ta": "9. முதன்மை மன வரைபடம் & சிறந்த 25 டிஎன்பிஎஸ்சி பொறிகள்",
      "type": "mind_map"
    }
  ],
  "content": {
    "definition": {
      "en": "Advanced Constitutional Concepts of the Judiciary encompass Judicial Review, Judicial Activism, Public Interest Litigation (PIL), Basic Structure Doctrine, Collegium practice, and Separation of Powers through which the Supreme Court maintains constitutional balance, protects fundamental rights, and limits parliamentary sovereignty.",
      "ta": "நீதித்துறையின் மேம்பட்ட அரசியலமைப்பு அமைப்புகள் என்பது நீதித்துறை ஆய்வு, நீதித்துறை செயலாக்கம், பொது நல வழக்கு (PIL), அடிப்படை கட்டமைப்புக் கோட்பாடு, கொலீஜியம் நடைமுறை மற்றும் அதிகாரப் பகிர்வு ஆகியவற்றை உள்ளடக்கியது. இவற்றின் மூலமே உச்ச நீதிமன்றம் அரசியலமைப்புச் சமநிலையைப் பேணி, அடிப்படை உரிமைகளைப் பாதுகாத்து, நாடாளுமன்ற இறையாண்மையை வரையறுக்கிறது."
    },
    "introduction": {
      "en": "From the historic Kesavananda Bharati (1973) ruling establishing the Basic Structure Doctrine to the evolution of PIL and the invalidation of the 99th Constitutional Amendment (NJAC) in 2015, the Supreme Court of India has dynamically defined its role as the custodian of the Constitution while preserving judicial independence.",
      "ta": "அடிப்படை கட்டமைப்புக் கோட்பாட்டை நிறுவிய வரலாற்றுச் சிறப்புமிக்க கேசவாநந்த பாரதி (1973) தீர்ப்பு முதல், பொது நல வழக்கின் (PIL) வளர்ச்சி மற்றும் 2015-ல் 99-வது திருத்தத் (NJAC) ரத்து வரை, இந்திய உச்ச நீதிமன்றம் நீதித்துறை சுதந்திரத்தைப் பேணிக் கொண்டே அரசியலமைப்பின் பாதுகாவலனாகத் தன் பங்கைத் துடிப்பாக வரையறுத்துள்ளது."
    },
    "sec_judicial_review_deep": [
      {
        "title_en": "Judicial Review — Meaning, Scope & Constitutional Articles",
        "title_ta": "நீதித்துறை ஆய்வு — பொருள், எல்லை & அரசியலமைப்பு விதிகள்",
        "points": {
          "en": [
            "Meaning: Judicial Review is the power of the Judiciary to examine the constitutionality of legislative enactments and executive orders of Union and State Governments.",
            "Outcome of Review: If a law or executive order is found violating any provision of the Constitution or its Basic Structure, it is declared UNCONSTITUTIONAL AND VOID by the Supreme Court.",
            "Constitutional Anchors (Implicitly & Explicitly):",
            "  • Article 13: Declare any law inconsistent with or in derogation of Fundamental Rights as null and void.",
            "  • Article 32 & Article 226: Supreme Court and High Courts power to issue writs for enforcement of rights.",
            "  • Article 131 to 136: Original and Appellate jurisdiction of Supreme Court.",
            "  • Article 141: Law declared by SC binding on all courts.",
            "  • Article 142: Complete justice decrees.",
            "  • Article 246: Division of legislative powers under 7th Schedule.",
            "Three Categories of Judicial Review:",
            "  1. Judicial Review of Legislative Enactments (Union & State Acts).",
            "  2. Judicial Review of Executive Actions (Administrative orders & policies).",
            "  3. Judicial Review of Constitutional Amendments (under Article 368 subject to Basic Structure)."
          ],
          "ta": [
            "பொருள்: நீதித்துறை ஆய்வு என்பது மத்திய மற்றும் மாநில அரசுகளின் சட்டமன்றச் சட்டங்கள் மற்றும் நிர்வாக உத்தரவுகளின் அரசியலமைப்புத் தன்மையை ஆய்வு செய்யும் நீதித்துறையின் அதிகாரமாகும்.",
            "ஆய்வின் முடிவு: ஒரு சட்டமோ அல்லது நிர்வாக உத்தரவோ அரசியலமைப்பின் விதிகளையோ அல்லது அதன் அடிப்படை அமைப்பையோ மீறுவதாகக் கண்டறியப்பட்டால், அது அரசியலமைப்புக்கு எதிரானது மற்றும் செல்லாது என உச்ச நீதிமன்றத்தால் அறிவிக்கப்படும்.",
            "அரசியலமைப்பு ஆதாரங்கள்:",
            "  • உறுப்பு 13: அடிப்படை உரிமைகளுக்கு எதிரான எந்தவொரு சட்டத்தையும் செல்லாததாக அறிவித்தல்.",
            "  • உறுப்பு 32 & உறுப்பு 226: உரிமைகளை அமல்படுத்த பேராணைகள் பிறப்பிக்கும் உச்ச மற்றும் உயர் நீதிமன்ற அதிகாரங்கள்.",
            "  • உறுப்பு 131 முதல் 136: உச்ச நீதிமன்றத்தின் மூல மற்றும் மேல்முறையீட்டு ஆதிக்கங்கள்.",
            "  • உறுப்பு 141: SC சட்டத்தை அனைத்து நீதிமன்றங்களுக்கும் கட்டுப்படியாக்குதல்.",
            "  • உறுப்பு 142: முழுமையான நீதி ஆணைகள்.",
            "  • உறுப்பு 246: 7-வது அட்டவணையின் கீழ் சட்டமன்ற அதிகாரப் பகிர்வு.",
            "நீதித்துறை ஆய்வின் 3 பிரிவுகள்:",
            "  1. சட்டமன்றச் சட்டங்கள் மீதான நீதித்துறை ஆய்வு (மத்திய & மாநில சட்டங்கள்).",
            "  2. நிர்வாக நடவடிக்கைகள் மீதான நீதித்துறை ஆய்வு (நிர்வாக உத்தரவுகள் & கொள்கைகள்).",
            "  3. அரசியலமைப்புத் திருத்தங்கள் மீதான நீதித்துறை ஆய்வு (உறுப்பு 368 திருத்தங்கள் அடிப்படை கட்டமைப்புக்கு உட்பட்டவை)."
          ]
        }
      }
    ],
    "sec_activism_vs_restraint": [
      {
        "title_en": "Judicial Activism vs Judicial Restraint",
        "title_ta": "நீதித்துறை செயலாக்கம் vs நீதித்துறை சுயகட்டுப்பாடு",
        "points": {
          "en": [
            "Judicial Activism:",
            "  • Definition: Proactive role played by the Judiciary in protecting the rights of citizens and promoting justice in society when the Executive or Legislature fails to act.",
            "  • Origin: Term coined by Arthur Schlesinger Jr. in 1947 (USA). Introduced in India in late 1970s.",
            "  • Key Drivers: Expanded interpretation of Article 21 (Right to Life & Liberty) to include Right to Clean Environment, Right to Privacy (Puttaswamy 2017), Right to Speed Trial, Right to Education, and Public Interest Litigation (PIL).",
            "  • Caution: Excess activism leading to 'Judicial Overreach' or 'Judicial Tyranny' where Judiciary usurps Executive/Legislative functions.",
            "Judicial Restraint:",
            "  • Definition: Self-imposed discipline where judges refrain from interfering in policy matters or legislative wisdom, recognizing the Constitutional separation of powers.",
            "  • Core Principle: Courts should not substitute their own socio-economic or political views for those of elected legislature unless a clear constitutional violation occurs."
          ],
          "ta": [
            "நீதித்துறை செயலாக்கம் (Judicial Activism):",
            "  • வரையறை: நிர்வாகமோ அல்லது சட்டமன்றமோ செயல்படத் தவறும் போது, குடிமக்களின் உரிமைகளைப் பாதுகாக்கவும் சமூக நீதியை மேம்படுத்தவும் நீதித்துறை முன்வந்து ஆற்றும் துடிப்பான பங்காகும்.",
            "  • தோற்றம்: 1947-ல் அமெரிக்காவில் ஆர்தர் ஷ்லெசிங்கர் ஜூனியரால் உருவாக்கப்பட்டது. இந்தியாவில் 1970-களின் பிற்பகுதியில் அறிமுகமானது.",
            "  • முக்கிய தூண்டுகோல்கள்: உறுப்பு 21 (வாழ்வு உரிமை) பரந்த விளக்கம் — சுத்தமான சுற்றுச்சூழல் உரிமை, தனிப்பரிவு உரிமை (புட்டசுவாமி 2017), விரைவு விசாரணை உரிமை, கல்வி உரிமை மற்றும் பொது நல வழக்கு (PIL).",
            "  • எச்சரிக்கை: அதிகப்படியான செயலாக்கம் 'நீதித்துறை மீறல் (Judicial Overreach)' அல்லது 'நீதித்துறை சர்வாதிகாரத்திற்கு' வழிவகுத்து நிர்வாக/சட்டமன்றப் பணிகளை நீதித்துறை ஆக்கிரமிக்கலாம்.",
            "நீதித்துறை சுயகட்டுப்பாடு (Judicial Restraint):",
            "  • வரையறை: அரசியலமைப்பு அதிகாரப் பகிர்வை மதித்து, கொள்கை விஷயங்களிலோ அல்லது சட்டமன்ற அறிவிலோ நீதிபதிகள் தலையிடாமல் சுயமாக விதிக்கும் கட்டுப்பாடாகும்.",
            "  • முதன்மைக் கோட்பாடு: தெளிவான அரசியலமைப்பு மீறல் இல்லாத வரை, தேர்ந்தெடுக்கப்பட்ட சட்டமன்றத்தின் கருத்துக்களுக்குப் பதிலாக நீதிபதிகள் தங்கள் சொந்த கருத்துக்களை மாற்றீடு செய்யக்கூடாது."
          ]
        }
      }
    ],
    "sec_pil_public_interest": [
      {
        "title_en": "Public Interest Litigation (PIL) & Locus Standi Relaxation",
        "title_ta": "பொது நல வழக்கு (PIL) & Locus Standi கோட்பாட்டுத் தளர்வு",
        "points": {
          "en": [
            "Traditional Locus Standi Rule: Historically, only an 'aggrieved person' whose personal legal right was directly violated could move the court for judicial remedy.",
            "PIL Concept & Locus Standi Relaxation: Under PIL, ANY PUBLIC-SPIRITED CITIZEN or organization can move the Supreme Court (Art 32) or High Court (Art 226) on behalf of a person or class of persons who are unable to approach the court due to poverty, ignorance, or socially disadvantaged position.",
            "Pioneer Judges in India: Justice V.R. Krishna Iyer and Justice P.N. Bhagwati (S.P. Gupta v. Union of India 1981 - First Judges Case).",
            "Epistolary Jurisdiction: SC treats ordinary letters, telegrams, or postcards sent by public-spirited citizens as formal Writ Petitions (e.g. Sunil Batra case on prison torture).",
            "Key Focus Areas: Child labor abolition, bonded labor release, environmental protection (M.C. Mehta cases), prison reforms, gender safety at workplace (Vishaka guidelines 1997).",
            "Safeguards against Misuse: SC imposes heavy costs on frivolous PILs filed for personal publicity, private vendetta, or political motives."
          ],
          "ta": [
            "பாரம்பரிய Locus Standi விதி: வரலாற்று ரீதியாக, தனது சொந்த சட்ட உரிமை நேரடியாகப் பாதிக்கப்பட்ட 'பாதிக்கப்பட்ட நபர் மட்டுமே' பரிகாரத்திற்காக நீதிமன்றத்தை அணுக முடியும்.",
            "PIL கருத்து & Locus Standi தளர்வு: பொது நல வழக்கின் கீழ், வறுமை, அறியாமை அல்லது சமூகப் பின்தங்கிய நிலை காரணமாக நீதிமன்றத்தை அணுக முடியாத நபர் அல்லது வகுப்பினருக்காக எந்தவொரு 'பொதுநல அக்கறையுள்ள குடிமகனும்' அல்லது அமைப்பும் உச்ச (விதி 32) அல்லது உயர் நீதிமன்றங்களை (விதி 226) அணுகலாம்.",
            "இந்திய முன்னோடி நீதிபதிகள்: நீதிபதி V.R. கிருஷ்ணய்யர் மற்றும் நீதிபதி P.N. பகவதி (எஸ்.பி. குப்தா v. இந்திய ஒன்றியம் 1981).",
            "கடித வடிவிலான ஆதிக்கம் (Epistolary Jurisdiction): பொதுநலக் குடிமக்கள் அனுப்பும் சாதாரணக் கடிதங்கள், தபால்களை உச்ச நீதிமன்றம் முறையான பேராணை மனுக்களாக ஏற்று விசாரிக்கிறது (எ.கா. சிறைக் கொடுமைகள் பற்றிய சுனில் பத்ரா வழக்கு).",
            "முக்கியக் கவனப் பகுதிகள்: குழந்தைத்தொழிலாளர் ஒழிப்பு, கொத்தடிமை விடுதலை, சுற்றுச்சூழல் பாதுகாப்பு (எம்.சி. மேத்தா வழக்குகள்), சிறைச் சீர்திருத்தங்கள், பணியிடப் பெண்கள் பாதுகாப்பு (விசாகா வழிகாட்டுதல்கள் 1997).",
            "துஷ்பிரயோகத் தடுப்புகள்: சுய விளம்பரம், தனிப்பட்டப் பகை அல்லது அரசியல் காரணங்களுக்காகத் தாக்கல் செய்யப்படும் வீண் பொது நல வழக்குகளுக்கு உச்ச நீதிமன்றம் அபராதம் விதிக்கிறது."
          ]
        }
      }
    ],
    "sec_basic_structure_cases": [
      {
        "title_en": "Basic Structure Doctrine & Evolution of Amendment Power",
        "title_ta": "அடிப்படை கட்டமைப்புக் கோட்பாடு & திருத்த அதிகாரத்தின் வளர்ச்சி",
        "points": {
          "en": [
            "Landmark Ruling: Kesavananda Bharati v. State of Kerala (April 24, 1973):",
            "  • Bench: Largest Constitution Bench in Indian judicial history — 13 JUDGES (Decided by a narrow 7-6 majority).",
            "  • Principle: Supreme Court held that Parliament has wide power to amend ANY PART of the Constitution under Article 368 (including Fundamental Rights), BUT Parliament CANNOT ALTER OR DESTROY THE 'BASIC STRUCTURE' of the Constitution.",
            "Evolution of Basic Structure Cases:",
            "  1. Shankari Prasad Case (1951) & Sajjan Singh Case (1965): SC held Parliament CAN amend Fundamental Rights under Art 368.",
            "  2. Golaknath Case (1967): 11-Judge Bench held Fundamental Rights are SACROSANCT and Parliament CANNOT amend or abridge Fundamental Rights under Art 368. (Overruled later by Kesavananda Bharati).",
            "  3. Kesavananda Bharati Case (1973): Established Basic Structure Doctrine. Overruled Golaknath judgment.",
            "  4. Indira Nehru Gandhi Case (1975): SC invalidated 39th Amend clause excluding PM election from judicial review. Added Rule of Law and Free & Fair Elections to Basic Structure.",
            "  5. Minerva Mills Case (1980): SC invalidated 42nd Amend clauses that gave unlimited amending power to Parliament. Held that 'Harmony and Balance between Fundamental Rights and Directive Principles' and 'Judicial Review' are Basic Features.",
            "  6. S.R. Bommai Case (1994): Declared SECULARISM and FEDERALISM as essential features of Basic Structure.",
            "  7. I.R. Coelho Case (2007): 9-Judge Bench held that laws placed in the NINTH SCHEDULE AFTER APRIL 24, 1973 ARE SUBJECT TO JUDICIAL REVIEW and open to challenge if they violate Fundamental Rights or Basic Structure."
          ],
          "ta": [
            "வரலாற்றுச் சிறப்புமிக்கத் தீர்ப்பு: கேசவாநந்த பாரதி v. கேரளா மாநிலம் (ஏப்ரல் 24, 1973):",
            "  • அமர்வு: இந்திய நீதித்துறை வரலாற்றிலேயே மிகப்பெரிய அரசியலமைப்பு அமர்வு — 13 நீதிபதிகள் (7-6 என்ற குறைந்த பெரும்பான்மையால் தீர்ப்பு).",
            "  • கோட்பாடு: உறுப்பு 368-ன் கீழ் அரசியலமைப்பின் எந்தவொரு பகுதியையும் (அடிப்படை உரிமைகள் உட்பட) திருத்த நாடாளுமன்றத்திற்கு பரந்த அதிகாரமுண்டு, ஆனால் அரசியலமைப்பின் 'அடிப்படை கட்டமைப்பை (Basic Structure)' மாற்றவோ அழிக்கவோ முடியாது என தீர்ப்பளித்தது.",
            "அடிப்படை கட்டமைப்பு வழக்கின் வளர்ச்சி வரலாறு:",
            "  1. சங்கரி பிரசாத் வழக்கு (1951) & சஜ்ஜன் சிங் வழக்கு (1965): உறுப்பு 368 கீழ் அடிப்படை உரிமைகளை நாடாளுமன்றம் திருத்தலாம் என SC கூறியது.",
            "  2. கோலக்நாத் வழக்கு (1967): 11 நீதிபதிகள் அமர்வு அடிப்படை உரிமைகள் புனிதமானவை; உறுப்பு 368 கீழ் நாடாளுமன்றம் அவற்றை திருத்தவோ குறைக்கவோ முடியாது எனக் கூறியது. (பின்னர் கேசவாநந்த பாரதி வழக்கால் ரத்து செய்யப்பட்டது).",
            "  3. கேசவாநந்த பாரதி வழக்கு (1973): அடிப்படை கட்டமைப்புக் கோட்பாட்டை நிறுவியது. கோலக்நாத் தீர்ப்பை ரத்து செய்தது.",
            "  4. இந்திரா நேரு காந்தி வழக்கு (1975): பிரதமர் தேர்தலை நீதித்துறை ஆய்விலிருந்து விலக்கிய 39-வது திருத்தப் பிரிவை SC ரத்து செய்தது. சட்டத்தின் ஆட்சி மற்றும் சுதந்திரமான தேர்தல் அடிப்படை கட்டமைப்பில் சேர்க்கப்பட்டது.",
            "  5. மினெர்வா மில்ஸ் வழக்கு (1980): நாடாளுமன்றத்திற்கு வரம்பற்ற திருத்த அதிகாரம் அளித்த 42-வது திருத்தப் பிரிவுகளை SC ரத்து செய்தது. 'அடிப்படை உரிமைகள் - வழிகாட்டு நெறிமுறைகள் சமநிலை' மற்றும் 'நீதித்துறை ஆய்வு' அடிப்படை கூறுகள் எனப்பட்டது.",
            "  6. எஸ்.ஆர். பொம்மை வழக்கு (1994): மதச்சார்பின்மை மற்றும் கூட்டாட்சி தத்துவம் அடிப்படை கட்டமைப்பின் முக்கிய கூறுகள் என அறிவிக்கப்பட்டது.",
            "  7. ஐ.ஆர். கோயல்ஹோ வழக்கு (2007): 9 நீதிபதிகள் அமர்வு ஏப்ரல் 24, 1973-க்கு பின் 9-வது அட்டவணையில் வைக்கப்பட்ட சட்டங்கள் நீதித்துறை ஆய்வுக்கு உட்பட்டவை எனக் கூறியது."
          ]
        }
      }
    ],
    "sec_collegium_njac_history": [
      {
        "title_en": "Collegium System vs NJAC Invalidation (99th Amendment)",
        "title_ta": "கொலீஜியம் அமைப்பு vs NJAC ரத்து (99-வது திருத்தம்)",
        "points": {
          "en": [
            "Collegium Mechanism: Supreme Court Collegium consists of the CHIEF JUSTICE OF INDIA + 4 SENIOR-MOST JUDGES of the Supreme Court. High Court Collegium consists of HC CJ + 2 senior-most HC judges.",
            "Judicial Primacy Rationale: Evolved through 2nd Judges Case (1993) and 3rd Judges Case (1998) to safeguard judicial independence from executive dominance.",
            "99th Constitutional Amendment Act 2014 & NJAC Act:",
            "  • Passed by Parliament to establish National Judicial Appointments Commission (NJAC) consisting of 6 members (CJI, 2 SC Judges, Law Minister, 2 Eminent Persons).",
            "Fourth Judges Case (2015): Supreme Court Advocates-on-Record Association v. Union of India (5-Judge Bench by 4-1 majority):",
            "  • SC declared both the 99th Constitutional Amendment Act 2014 and the NJAC Act UNCONSTITUTIONAL AND VOID.",
            "  • Ground: Inclusion of Executive (Law Minister) and laymen in judicial selection compromised 'Judicial Independence', which is a part of the Basic Structure of the Constitution.",
            "  • Result: Restored the Collegium System for judicial appointments."
          ],
          "ta": [
            "கொலீஜியம் அமைப்பு: உச்ச நீதிமன்ற கொலீஜியத்தில் இந்தியத் தலைமை நீதிபதி (CJI) + 4 மூத்த உச்ச நீதிமன்ற நீதிபதிகள் இருப்பர். உயர் நீதிமன்ற கொலீஜியத்தில் HC தலைமை நீதிபதி + 2 மூத்த HC நீதிபதிகள் இருப்பர்.",
            "நீதித்துறை முதன்மைக்கான காரணம்: நிர்வாக ஆதிக்கத்திலிருந்து நீதித்துறை சுதந்திரத்தைப் பாதுகாக்க 2-வது (1993) & 3-வது (1998) நீதிபதிகள் வழக்குகள் மூலம் உருவாக்கப்பட்டது.",
            "99-வது அரசியலமைப்புத் திருத்தச் சட்டம் 2014 & NJAC சட்டம்:",
            "  • 6 உறுப்பினர்கள் (CJI, 2 SC நீதிபதிகள், சட்ட அமைச்சர், 2 பிரபல நபர்கள்) கொண்ட தேசிய நீதிபதிகள் நியமன ஆணையம் (NJAC) அமைக்க நாடாளுமன்றத்தால் நிறைவேற்றப்பட்டது.",
            "4-வது நீதிபதிகள் வழக்கு (2015): வழக்கறிஞர்கள் சங்கம் v. இந்திய ஒன்றியம் (5 நீதிபதிகள் அமர்வு 4-1 பெரும்பான்மையால்):",
            "  • 99-வது திருத்தம் மற்றும் NJAC சட்டம் இரண்டுமே அரசியலமைப்புக்கு எதிரானது மற்றும் செல்லாது என உச்ச நீதிமன்றம் அறிவித்தது.",
            "  • காரணம்: நீதிபதிகள் தேர்வில் நிர்வாகத்தை (சட்ட அமைச்சர்) சேர்ப்பது 'நீதித்துறை சுதந்திரத்தைப்' பாதிக்கிறது. நீதித்துறை சுதந்திரம் அரசியலமைப்பின் அடிப்படை கட்டமைப்பாகும்.",
            "  • முடிவு: நீதிபதிகள் நியமனத்திற்கான கொலீஜியம் அமைப்பை மீண்டும் நிறுவியது."
          ]
        }
      }
    ],
    "sec_separation_independence": [
      {
        "title_en": "Separation of Powers & Judicial Independence Safeguards",
        "title_ta": "அதிகாரப் பகிர்வு & மேம்பட்ட நீதித்துறை சுதந்திரப் பாதுகாப்புகள்",
        "points": {
          "en": [
            "Doctrine of Separation of Powers: Proposed by Montesquieu. Three distinct organs: Legislature (Law making), Executive (Law implementing), Judiciary (Law interpreting & adjudicating).",
            "Checks and Balances: India does not follow rigid separation of powers (like USA), but follows a system of functional separation with CHECKS AND BALANCES.",
            "Safeguards for Judicial Independence in India:",
            "  1. Security of Tenure (Art 124(4)): Judges can be removed only by President on Parliamentary Special Majority Address on proved misbehaviour/incapacity.",
            "  2. Non-Votable Expenses (Art 146): Salaries, pensions, administrative expenses charged on Consolidated Fund of India.",
            "  3. Ban on Discussion in Legislature (Art 121): Conduct of judges in discharge of duties cannot be discussed in Parliament or State Assemblies.",
            "  4. Ban on Post-Retirement Practice (Art 124(7)): SC judges banned from pleading in any Indian court after retirement.",
            "  5. Contempt Powers (Art 129): Power to punish for contempt of court.",
            "  6. Directive Principles Mandate (Art 50 DPSP): Mandates state to separate judiciary from executive."
          ],
          "ta": [
            "அதிகாரப் பகிர்வுக் கோட்பாடு: மாண்டெஸ்கியூவால் முன்மொழியப்பட்டது. 3 தன்னாட்சி உறுப்புகள்: சட்டமன்றம் (சட்டம் இயற்றல்), நிர்வாகம் (சட்டம் அமலாக்கம்), நீதித்துறை (சட்டம் விளக்கம் & தீர்ப்பளித்தல்).",
            "தடைகள் மற்றும் சமநிலைகள் (Checks & Balances): இந்தியா அமெரிக்கா போல கடுமையான அதிகாரப் பகிர்வை பின்பற்றாமல், தடைகள் மற்றும் சமநிலைகளுடன் கூடிய செயல்பாட்டுப் பகிர்வை பின்பற்றுகிறது.",
            "இந்தியாவில் நீதித்துறை சுதந்திரத்திற்கான பாதுகாப்புகள்:",
            "  1. பதவிப் பாதுகாப்பு (விதி 124(4)): நாடாளுமன்றச் சிறப்பு பெரும்பான்மை மூலம் மட்டுமே குடியரசுத் தலைவரால் நீக்கப்பட முடியும்.",
            "  2. வாக்களிக்கப்படாத செலவுகள் (விதி 146): சம்பளம், ஓய்வூதியம் இந்தியத் தொகுப்பு நிதியில் சுமத்தப்பட்டவை.",
            "  3. சட்டமன்ற விவாதத் தடை (விதி 121): நீதிபதிகள் செயல்பாட்டை நாடாளுமன்றத்திலோ மாநில சட்டமன்றங்களிலோ விவாதிக்க முடியாது.",
            "  4. ஓய்வுக்குப் பின் பயிற்சித் தடை (விதி 124(7)): SC நீதிபதிகள் ஓய்வுக்குப் பின் எந்த நீதிமன்றத்திலும் பணியாற்றத் தடை.",
            "  5. அவமதிப்பு அதிகாரம் (விதி 129): நீதிமன்ற அவமதிப்பிற்குத் தண்டிக்கும் அதிகாரம்.",
            "  6. வழிகாட்டு நெறிமுறை ஆணை (விதி 50 DPSP): நீதித்துறையை நிர்வாகத்திலிருந்து பிரிக்க அரசு நடவடிக்கை எடுக்க வேண்டும்."
          ]
        }
      }
    ],
    "sec_landmark_cases_summary": [
      {
        "title_en": "Summary of Landmark Supreme Court Cases",
        "title_ta": "வரலாற்றுச் சிறப்புமிக்க உச்ச நீதிமன்ற வழக்குகளின் தொகுப்பு",
        "points": {
          "en": [
            "1. Shankari Prasad Case (1951): First case on Art 368. SC held Parliament CAN amend Fundamental Rights.",
            "2. Golaknath Case (1967): 11-Judge Bench held Fundamental Rights are sacrosanct and CANNOT be amended under Art 368.",
            "3. Kesavananda Bharati Case (April 24, 1973): 13-Judge Bench established BASIC STRUCTURE DOCTRINE. Parliament can amend FRs but cannot alter Basic Structure.",
            "4. Indira Nehru Gandhi Case (1975): Added Rule of Law, Free & Fair Elections to Basic Structure.",
            "5. Maneka Gandhi Case (1978): Expanded Article 21. Replaced 'Procedure Established by Law' with 'DUE PROCESS OF LAW' concept (Fair, Just & Reasonable).",
            "6. Minerva Mills Case (1980): Struck down 42nd Amend unlimited amending power clauses. Added Judicial Review and FR-DPSP Harmony to Basic Structure.",
            "7. S.P. Gupta Case / First Judges Case (1981): Executive primacy in judicial appointments; initiated PIL concept.",
            "8. Second Judges Case (1993): Judiciary primacy; introduced 3-member Collegium.",
            "9. Third Judges Case (1998): Expanded Collegium to CJI + 4 senior SC judges.",
            "10. S.R. Bommai Case (1994): Article 356 Presidential Rule subject to Judicial Review. SECULARISM and FEDERALISM declared Basic Structure.",
            "11. Vishaka v. State of Rajasthan (1997): Framed Vishaka Guidelines for protection of women against sexual harassment at workplace.",
            "12. Rupa Ashok Hurra Case (2002): Evolved Curative Petition under Article 137.",
            "13. I.R. Coelho Case (2007): 9-Judge Bench held laws in Ninth Schedule after April 24, 1973 are SUBJECT TO JUDICIAL REVIEW.",
            "14. Fourth Judges Case / NJAC Case (2015): Invalidated 99th Amend & NJAC Act; restored Collegium.",
            "15. K.S. Puttaswamy Case (2017): 9-Judge Bench declared RIGHT TO PRIVACY as a Fundamental Right under Article 21."
          ],
          "ta": [
            "1. சங்கரி பிரசாத் வழக்கு (1951): விதி 368 குறித்த முதல் வழக்கு. அடிப்படை உரிமைகளை நாடாளுமன்றம் திருத்தலாம் எனப்பட்டது.",
            "2. கோலக்நாத் வழக்கு (1967): 11 நீதிபதிகள் அமர்வு அடிப்படை உரிமைகளை திருத்த முடியாது எனப்பட்டது.",
            "3. கேசவாநந்த பாரதி வழக்கு (ஏப்ரல் 24, 1973): 13 நீதிபதிகள் அமர்வு அடிப்படை கட்டமைப்புக் கோட்பாட்டை நிறுவியது.",
            "4. இந்திரா நேரு காந்தி வழக்கு (1975): சட்டத்தின் ஆட்சி, சுதந்திரமான தேர்தல் அடிப்படை கட்டமைப்பில் சேர்க்கப்பட்டது.",
            "5. மேனகா காந்தி வழக்கு (1978): உறுப்பு 21 விரிவாக்கம். 'சட்டத்தால் அமைக்கப்பட்ட நடைமுறை' என்பதற்குப் பதிலாக 'சரியான சட்ட நடைமுறை (Due Process of Law)' கருத்து வரவு.",
            "6. மினெர்வா மில்ஸ் வழக்கு (1980): 42-வது திருத்த வரம்பற்ற பிரிவுகள் ரத்து. நீதித்துறை ஆய்வு & FR-DPSP சமநிலை அடிப்படை கட்டமைப்பு எனப்பட்டது.",
            "7. எஸ்.பி. குப்தா வழக்கு / 1-வது நீதிபதிகள் வழக்கு (1981): நியமனத்தில் நிர்வாக முதன்மை; PIL கருத்தின் தொடக்கம்.",
            "8. 2-வது நீதிபதிகள் வழக்கு (1993): நீதித்துறை முதன்மை; 3 உறுப்பினர்கள் கொலீஜியம் அறிமுகம்.",
            "9. 3-வது நீதிபதிகள் வழக்கு (1998): கொலீஜியம் CJI + 4 மூத்த நீதிபதிகளாக விரிவாக்கம்.",
            "10. எஸ்.ஆர். பொம்மை வழக்கு (1994): உறுப்பு 356 குடியரசுத் தலைவர் ஆட்சி நீதித்துறை ஆய்வுக்கு உட்பட்டது. மதச்சார்பின்மை மற்றும் கூட்டாட்சி அடிப்படை கட்டமைப்பு எனப்பட்டது.",
            "11. விசாகா v. ராஜஸ்தான் மாநிலம் (1997): பணியிடப் பெண்கள் பாதுகாப்பு விசாகா வழிகாட்டுதல்கள் உருவாக்கம்.",
            "12. ரூபா அசோக் ஹுர்ரா வழக்கு (2002): உறுப்பு 137 கீழ் நிவர்த்தி மனு (Curative Petition) உருவாக்கம்.",
            "13. ஐ.ஆர். கோயல்ஹோ வழக்கு (2007): 9 நீதிபதிகள் அமர்வு ஏப்ரல் 24, 1973-க்கு பின் 9-வது அட்டவணையில் வைக்கப்பட்ட சட்டங்கள் நீதித்துறை ஆய்வுக்கு உட்பட்டவை எனக் கூறியது.",
            "14. 4-வது நீதிபதிகள் வழக்கு / NJAC வழக்கு (2015): 99-வது திருத்தம் மற்றும் NJAC ரத்து; கொலீஜியம் மீண்டும் நிறுவல்.",
            "15. கே.எஸ். புட்டசுவாமி வழக்கு (2017): 9 நீதிபதிகள் அமர்வு தனிப்பரிவு உரிமையை (Right to Privacy) உறுப்பு 21 கீழ் அடிப்படை உரிமையாக அறிவித்தது."
          ]
        }
      }
    ],
    "revision_cards": [
      {
        "id": "sc_p3_c1",
        "front_en": "On what date was the Kesavananda Bharati judgment establishing the Basic Structure Doctrine delivered?",
        "front_ta": "அடிப்படை கட்டமைப்புக் கோட்பாட்டை நிறுவிய கேசவாநந்த பாரதி தீர்ப்பு வழங்கப்பட்ட தேதி எது?",
        "back_en": "APRIL 24, 1973 (Delivered by a 13-Judge Bench by 7-6 majority).",
        "back_ta": "ஏப்ரல் 24, 1973 (13 நீதிபதிகள் அமர்வால் 7-6 பெரும்பான்மையால் வழங்கப்பட்டது)."
      },
      {
        "id": "sc_p3_c2",
        "front_en": "Which landmark judgment expanded Article 21 to include 'Due Process of Law' (Fair, Just and Reasonable procedure)?",
        "front_ta": "உறுப்பு 21-ஐ விரிவுபடுத்தி 'சரியான சட்ட நடைமுறை (Due Process of Law)' என்பதையும் உள்ளடக்கிய வரலாற்று தீர்ப்பு எது?",
        "back_en": "Maneka Gandhi v. Union of India (1978).",
        "back_ta": "மேனகா காந்தி v. இந்திய ஒன்றியம் (1978)."
      },
      {
        "id": "sc_p3_c3",
        "front_en": "Which judges are recognized as the key pioneers of Public Interest Litigation (PIL) in India?",
        "front_ta": "இந்தியாவில் பொது நல வழக்கின் (PIL) முக்கிய முன்னோடி நீதிபதிகளாக அங்கீகரிக்கப்படுபவர்கள் யார்?",
        "back_en": "Justice V.R. Krishna Iyer and Justice P.N. Bhagwati (S.P. Gupta Case 1981).",
        "back_ta": "நீதிபதி V.R. கிருஷ்ணய்யர் மற்றும் நீதிபதி P.N. பகவதி (எஸ்.பி. குப்தா வழக்கு 1981)."
      },
      {
        "id": "sc_p3_c4",
        "front_en": "What did the Supreme Court decide in the I.R. Coelho Case (2007) regarding Ninth Schedule laws?",
        "front_ta": "9-வது அட்டவணை சட்டங்கள் குறித்து ஐ.ஆர். கோயல்ஹோ வழக்கில் (2007) உச்ச நீதிமன்றம் என்ன தீர்ப்பளித்தது?",
        "back_en": "Laws placed in 9th Schedule AFTER April 24, 1973 ARE SUBJECT TO JUDICIAL REVIEW under Basic Structure test.",
        "back_ta": "ஏப்ரல் 24, 1973-க்கு பின் 9-வது அட்டவணையில் வைக்கப்பட்ட சட்டங்கள் அடிப்படை கட்டமைப்பு ஆய்வுக்கு உட்பட்டவை."
      },
      {
        "id": "sc_p3_c5",
        "front_en": "Which landmark case declared Secularism and Federalism as essential features of Basic Structure?",
        "front_ta": "மதச்சார்பின்மை மற்றும் கூட்டாட்சி தத்துவத்தை அடிப்படை கட்டமைப்பின் முக்கிய கூறுகளாக அறிவித்த வழக்கு எது?",
        "back_en": "S.R. Bommai v. Union of India (1994).",
        "back_ta": "எஸ்.ஆர். பொம்மை v. இந்திய ஒன்றியம் (1994)."
      },
      {
        "id": "sc_p3_c6",
        "front_en": "What is the difference between Judicial Review and Judicial Activism?",
        "front_ta": "நீதித்துறை ஆய்வுக்கும் நீதித்துறை செயலாக்கத்திற்கும் இடையிலான வேறுபாடு என்ன?",
        "back_en": "Judicial Review: Reviewing law constitutionality. Judicial Activism: Proactive intervention when executive/legislature fails.",
        "back_ta": "நீதித்துறை ஆய்வு: சட்ட அரசியலமைப்புத் தன்மையை ஆய்வு செய்தல். நீதித்துறை செயலாக்கம்: நிர்வாகம்/சட்டமன்றம் தவறும்போது முன்வந்து செயல்படுதல்."
      },
      {
        "id": "sc_p3_c7",
        "front_en": "Why was the 99th Constitutional Amendment (NJAC) declared unconstitutional in the Fourth Judges Case (2015)?",
        "front_ta": "4-வது நீதிபதிகள் வழக்கில் (2015) 99-வது திருத்தம் (NJAC) ஏன் அரசியலமைப்புக்கு எதிரானது என அறிவிக்கப்பட்டது?",
        "back_en": "Because executive inclusion violated 'Judicial Independence', which is a part of Basic Structure.",
        "back_ta": "ஏனெனில் நிர்வாகச் சேர்க்கை அடிப்படை கட்டமைப்பின் அங்கமான 'நீதித்துறை சுதந்திரத்தைப்' பாதித்தது."
      },
      {
        "id": "sc_p3_c8",
        "front_en": "Which judgment declared the Right to Privacy as a Fundamental Right under Article 21?",
        "front_ta": "தனிப்பரிவு உரிமையை (Right to Privacy) உறுப்பு 21 கீழ் அடிப்படை உரிமையாக அறிவித்த தீர்ப்பு எது?",
        "back_en": "K.S. Puttaswamy v. Union of India (2017).",
        "back_ta": "கே.எஸ். புட்டசுவாமி v. இந்திய ஒன்றியம் (2017)."
      },
      {
        "id": "sc_p3_c9",
        "front_en": "What is Epistolary Jurisdiction in the context of PIL?",
        "front_ta": "பொது நல வழக்கில் (PIL) கடித வடிவிலான ஆதிக்கம் (Epistolary Jurisdiction) என்றால் என்ன?",
        "back_en": "Power of SC/HC to treat ordinary letters or postcards sent by public-spirited citizens as formal Writ Petitions.",
        "back_ta": "பொதுநலக் குடிமக்கள் அனுப்பும் சாதாரணக் கடிதங்கள் அல்லது தபால்களை முறையான பேராணை மனுக்களாக ஏற்கும் அதிகாரம்."
      },
      {
        "id": "sc_p3_c10",
        "front_en": "Which landmark judgment held that 'Harmony and Balance between FRs and DPSPs' is a Basic Feature?",
        "front_ta": "'அடிப்படை உரிமைகள் - வழிகாட்டு நெறிமுறைகள் சமநிலை' அடிப்படை கூறு என தீர்ப்பளித்த வழக்கு எது?",
        "back_en": "Minerva Mills v. Union of India (1980).",
        "back_ta": "மினெர்வா மில்ஸ் v. இந்திய ஒன்றியம் (1980)."
      },
      {
        "id": "sc_p3_c11",
        "front_en": "Under Article 121, can the conduct of a Supreme Court judge be discussed in Parliament during regular business?",
        "front_ta": "உறுப்பு 121-ன் கீழ் வழக்கமான நாடாளுமன்றப் பணியின் போது உச்ச நீதிமன்ற நீதிபதியின் நடத்தையை விவாதிக்க முடியுமா?",
        "back_en": "NO. Conduct of judges CANNOT be discussed in Parliament except during debate on a Removal Motion.",
        "back_ta": "இல்லை. நீக்கத் தீர்மான விவாதத்தின் போது தவிர பிற நேரத்தில் நீதிபதியின் நடத்தையை விவாதிக்க முடியாது."
      },
      {
        "id": "sc_p3_c12",
        "front_en": "How many senior judges constitute the Supreme Court Collegium for selecting Supreme Court judges?",
        "front_ta": "உச்ச நீதிமன்ற நீதிபதிகளைத் தேர்வு செய்ய உச்ச நீதிமன்ற கொலீஜியத்தில் எத்தனை மூத்த நீதிபதிகள் இருப்பர்?",
        "back_en": "5 Judges in total (Chief Justice of India + 4 Senior-most Supreme Court Judges).",
        "back_ta": "மொத்தம் 5 நீதிபதிகள் (இந்தியத் தலைமை நீதிபதி + 4 மூத்த உச்ச நீதிமன்ற நீதிபதிகள்)."
      }
    ],
    "comparison_tables": [
      {
        "id": "tbl_sc_vs_hc_p3",
        "title_en": "1. Supreme Court vs High Court Comprehensive Comparison",
        "title_ta": "1. உச்ச நீதிமன்றம் vs உயர் நீதிமன்றம் விரிவான ஒப்பீடு",
        "headers_en": ["Dimension", "Supreme Court of India", "High Courts of States"],
        "headers_ta": ["அம்சம்", "இந்திய உச்ச நீதிமன்றம்", "மாநில உயர் நீதிமன்றங்கள்"],
        "rows_en": [
          ["Constitutional Status", "Apex Union Judiciary (Part V Chapter IV)", "State Judiciary (Part VI Chapter V)"],
          ["Writ Scope (Art 32 vs 226)", "ONLY Fundamental Rights (Narrower subject scope)", "Fundamental Rights + Other Legal Rights (Wider subject scope)"],
          ["Territorial Reach", "Entire Territory of India (Wider territorial scope)", "State / UT territorial limits (Narrower territorial scope)"],
          ["Retirement Age", "65 Years", "62 Years"],
          ["Superintendence Power", "Supervises all courts across India", "Supervises subordinate courts under Art 227"],
          ["Court of Record Provision", "Article 129", "Article 215"]
        ],
        "rows_ta": [
          ["அரசியலமைப்பு நிலை", "உச்ச ஒன்றிய நீதித்துறை (பகுதி V அத்தியாயம் IV)", "மாநில நீதித்துறை (பகுதி VI அத்தியாயம் V)"],
          ["பேராணை எல்லை (விதி 32 vs 226)", "அடிப்படை உரிமைகள் மட்டுமே (குறுகிய பாட எல்லை)", "அடிப்படை உரிமைகள் + பிற சட்ட உரிமைகள் (பரந்த பாட எல்லை)"],
          ["நிலப்பரப்பு வரம்பு", "இந்தியா முழுவதற்கும் பொருந்தும் (பரந்த நிலப்பரப்பு)", "மாநில / யூனியன் பிரதேச எல்லைக்குள் (குறுகிய நிலப்பரப்பு)"],
          ["ஓய்வு பெறும் வயது", "65 வயது", "62 வயது"],
          ["மேற்பார்வை அதிகாரம்", "இந்தியா முழுவதிலும் உள்ள நீதிமன்றங்களை மேற்பார்வையிடுகிறது", "உறுப்பு 227-ன் கீழ் சார்பு நீதிமன்றங்களை மேற்பார்வையிடுகிறது"],
          ["பதிவு நீதிமன்ற விதி", "உறுப்பு 129", "உறுப்பு 215"]
        ]
      },
      {
        "id": "tbl_art32_vs_226_p3",
        "title_en": "2. Article 32 vs Article 226 High-Priority Comparison",
        "title_ta": "2. உறுப்பு 32 vs உறுப்பு 226 உயர் முன்னுரிமை ஒப்பீடு",
        "headers_en": ["Feature", "Article 32 (Supreme Court)", "Article 226 (High Courts)"],
        "headers_ta": ["அம்சம்", "உறுப்பு 32 (உச்ச நீதிமன்றம்)", "உறுப்பு 226 (உயர் நீதிமன்றங்கள்)"],
        "rows_en": [
          ["Fundamental Right Status", "IS ITSELF a Fundamental Right (Right to Constitutional Remedies)", "NOT a Fundamental Right (Constitutional remedy provision)"],
          ["Enforcement Subject", "ONLY Fundamental Rights enforcement", "Fundamental Rights AND 'any other purpose' / legal rights"],
          ["Refusal Discretion", "SC CANNOT refuse to exercise jurisdiction (Guarantor)", "HC MAY refuse to issue writs (Discretionary power)"],
          ["Geographical Scope", "Pan-India territorial jurisdiction", "State-wide territorial jurisdiction"]
        ],
        "rows_ta": [
          ["அடிப்படை உரிமை நிலை", "தானே ஒரு அடிப்படை உரிமையாகும் (அரசியலமைப்பு பரிகார உரிமை)", "அடிப்படை உரிமையல்ல (அரசியலமைப்பு பரிகார விதி மட்டுமே)"],
          ["அமலாக்கப் பொருள்", "அடிப்படை உரிமைகளை அமல்படுத்த மட்டுமே", "அடிப்படை உரிமைகள் மற்றும் 'பிற சட்ட உரிமைகளுக்கும்'"],
          ["மறுப்பு விருப்பவுரிமை", "SC அதிகாரத்தைப் பயன்படுத்த மறுக்க முடியாது (பாதுகாவலன்)", "HC பேராணை பிறப்பிக்க மறுக்கலாம் (விருப்பவுரிமை பரிகாரம்)"],
          ["புவியியல் எல்லை", "இந்தியா தழுவிய நிலப்பரப்பு ஆதிக்கம்", "மாநில தழுவிய நிலப்பரப்பு ஆதிக்கம்"]
        ]
      },
      {
        "id": "tbl_review_vs_activism_p3",
        "title_en": "3. Judicial Review vs Judicial Activism Comparison",
        "title_ta": "3. நீதித்துறை ஆய்வு vs நீதித்துறை செயலாக்கம் ஒப்பீடு",
        "headers_en": ["Dimension", "Judicial Review", "Judicial Activism"],
        "headers_ta": ["அம்சம்", "நீதித்துறை ஆய்வு (Judicial Review)", "நீதித்துறை செயலாக்கம் (Judicial Activism)"],
        "rows_en": [
          ["Primary Function", "Examining constitutionality of laws & executive orders", "Proactively intervening to protect rights when executive fails"],
          ["Constitutional Source", "Explicitly & implicitly anchored in Arts 13, 32, 131–142", "Judicially evolved proactive approach; expansion of Art 21 & PIL"],
          ["Nature of Action", "Reactive check on legislative/executive excess", "Proactive enforcement of socio-economic justice & public policy guidance"],
          ["Locus Standi", "Follows standard legal standing parameters", "Relaxes locus standi via Public Interest Litigation (PIL)"]
        ],
        "rows_ta": [
          ["முதன்மைப் பணி", "சட்டங்கள் & நிர்வாக உத்தரவுகளின் அரசியலமைப்புத் தன்மையை ஆய்வு செய்தல்", "நிர்வாகம் தவறும்போது உரிமைகளைப் பாதுகாக்க முன்வந்து தலையிடுதல்"],
          ["அரசியலமைப்பு ஆதாரம்", "உறுப்புகள் 13, 32, 131–142 ஆகியவற்றில் வெளிப்படையாகவும் உள்ளடங்கியும் உள்ளது", "நீதித்துறையால் உருவாக்கப்பட்ட முன்முயற்சி அணுகுமுறை; விதி 21 & PIL விரிவாக்கம்"],
          ["செயல்பாட்டின் தன்மை", "சட்டமன்ற/நிர்வாக மீறல்கள் மீதான எதிர்வினைச் சோதனை", "சமூக-பொருளாதார நீதியை அமல்படுத்தும் முன்முயற்சிச் செயல்பாடு"],
          ["Locus Standi", "வழக்கமான சட்டப் பங்கேற்பு அளவுருக்களைப் பின்பற்றுகிறது", "பொது நல வழக்கு (PIL) மூலம் Locus Standi கோட்பாட்டைத் தளர்த்துகிறது"]
        ]
      },
      {
        "id": "tbl_activism_vs_restraint_p3",
        "title_en": "4. Judicial Activism vs Judicial Restraint Comparison",
        "title_ta": "4. நீதித்துறை செயலாக்கம் vs நீதித்துறை சுயகட்டுப்பாடு ஒப்பீடு",
        "headers_en": ["Parameter", "Judicial Activism", "Judicial Restraint"],
        "headers_ta": ["அளவுரு", "நீதித்துறை செயலாக்கம் (Activism)", "நீதித்துறை சுயகட்டுப்பாடு (Restraint)"],
        "rows_en": [
          ["Judicial Approach", "Proactive, creative interpretation of constitutional rights", "Self-imposed discipline; refrains from policy interference"],
          ["Separation of Powers", "Intervenes when executive or legislature fails in public duty", "Strictly respects institutional boundaries of executive & legislature"],
          ["Policy Decisions", "May issue directives framing policy guidelines (e.g. Vishaka)", "Leaves policy choices exclusively to elected Legislature & Executive"],
          ["Risk / Criticism", "Risk of 'Judicial Overreach' or usurping executive functions", "Risk of judicial inaction when fundamental rights are threatened"]
        ],
        "rows_ta": [
          ["நீதித்துறை அணுகுமுறை", "அரசியலமைப்பு உரிமைகளின் முன்முயற்சியான, ஆக்கப்பூர்வமான விளக்கம்", "சுயமாக விதிக்கும் கட்டுப்பாடு; கொள்கை தலையீட்டைத் தவிர்க்கிறது"],
          ["அதிகாரப் பகிர்வு", "நிர்வாகம்/சட்டமன்றம் பொதுக் கடமையில் தவறும்போது தலையிடுகிறது", "நிர்வாகம் & சட்டமன்றத்தின் நிறுவன எல்லைகளைக் கடுமையாக மதிக்கிறது"],
          ["கொள்கை முடிவுகள்", "கொள்கை வழிகாட்டுதல்களை உருவாக்கும் ஆணைகளைப் பிறப்பிக்கலாம் (எ.கா. விசாகா)", "கொள்கைத் தேர்வுகளைத் தேர்ந்தெடுக்கப்பட்ட மன்றங்களுக்கே விட்டுவிடுகிறது"],
          ["அபாயம் / விமர்சனம்", "'நீதித்துறை மீறல் (Judicial Overreach)' அல்லது நிர்வாகப் பணிகளை ஆக்கிரமிக்கும் அபாயம்", "அடிப்படை உரிமைகள் அச்சுறுத்தப்படும்போது நீதித்துறை செயலற்றிருக்கும் அபாயம்"]
        ]
      },
      {
        "id": "tbl_jurisdictions_all_p3",
        "title_en": "5. Original vs Appellate vs Advisory Jurisdiction Comparison",
        "title_ta": "5. மூல vs மேல்முறையீட்டு vs ஆலோசனை ஆதிக்கங்கள் ஒப்பீடு",
        "headers_en": ["Feature", "Original Jurisdiction (Art 131)", "Appellate Jurisdiction (Arts 132-136)", "Advisory Jurisdiction (Art 143)"],
        "headers_ta": ["அம்சம்", "மூல ஆதிக்கம் (விதி 131)", "மேல்முறையீட்டு ஆதிக்கம் (விதிகள் 132-136)", "ஆலோசனை ஆதிக்கம் (விதி 143)"],
        "rows_en": [
          ["Initiating Authority", "Disputing Central / State Governments", "Litigants appealing against lower court orders", "PRESIDENT OF INDIA seeking legal opinion"],
          ["Binding Effect", "Final binding judicial decision between Centre/States", "Final binding appellate judgment on parties & lower courts", "ONLY ADVISORY; NOT binding on President"],
          ["Subject Matter", "Federal Centre-State and Inter-State disputes", "Constitutional, Civil, Criminal cases, and SLP", "Public importance legal questions or pre-Const treaties"],
          ["Exclusions", "Water disputes (Art 262), pre-Const treaties", "Art 136 excludes Armed Forces Military Courts", "Court has discretion to decline Art 143(1) references"]
        ],
        "rows_ta": [
          ["தொடங்கும் அதிகாரி", "தகராறில் உள்ள மத்திய / மாநில அரசுகள்", "கீழ் நீதிமன்ற உத்தரவுகளை எதிர்த்து மேல்முறையீடு செய்யும் மனுதாரர்கள்", "சட்ட ஆலோசனை கோரும் இந்தியக் குடியரசுத் தலைவர்"],
          ["கட்டுப்படுத்தும் விளைவு", "மத்திய/மாநிலங்களுக்கு இடையிலான இறுதி கட்டுப்படுத்தும் நீதித்துறை முடிவு", "தரப்பினரையும் கீழ் நீதிமன்றங்களையும் கட்டுப்படுத்தும் இறுதித் தீர்ப்பு", "வெறும் ஆலோசனையே; குடியரசுத் தலைவரைக் கட்டுப்படுத்தாது"],
          ["பாடப்பொருள்", "கூட்டாட்சி மத்திய-மாநில மற்றும் மாநிலங்களுக்கு இடையிலான தகராறுகள்", "அரசியலமைப்பு, சிவில், குற்றவியல் மற்றும் SLP வழக்குகள்", "பொது முக்கியத்துவம் வாய்ந்த சட்டக் கேள்விகள் அல்லது ஒப்பந்தங்கள்"],
          ["விலக்குகள்", "நதிநீர் தகராறுகள் (விதி 262), முன் ஒப்பந்தங்கள்", "விதி 136 இராணுவ நீதிமன்றங்களை விலக்குகிறது", "விதி 143(1) குறிப்புகளை மறுக்க நீதிமன்றத்திற்கு விருப்பவுரிமை உண்டு"]
        ]
      },
      {
        "id": "tbl_appeal_review_slp_deep_p3",
        "title_en": "6. Appeal vs Review vs Special Leave Petition (SLP)",
        "title_ta": "6. மேல்முறையீடு vs சீராய்வு vs சிறப்பு விடுப்பு மனு ஒப்பீடு",
        "headers_en": ["Parameter", "Ordinary Appeal (Arts 132-134)", "Review Petition (Article 137)", "Special Leave Petition (Article 136)"],
        "headers_ta": ["அளவுரு", "சாதாரண மேல்முறையீடு (விதிகள் 132-134)", "சீராய்வு மனு (உறுப்பு 137)", "சிறப்பு விடுப்பு மனு (உறுப்பு 136)"],
        "rows_en": [
          ["Forum Order Reviewed", "High Court judgment or decree", "Supreme Court's OWN judgment or order", "ANY court or tribunal in India (except Military)"],
          ["Constitutional Right", "Constitutional / Statutory right of appeal", "Power to correct error apparent on face of record", "Plenary extraordinary discretionary power of SC"],
          ["Prerequisite Certificate", "Requires HC Certificate (Art 134A) or death sentence", "Requires error apparent or discovery of new evidence", "No HC certificate needed; SC grants leave"],
          ["Final Remedy Evolution", "Leads to SC judgment", "If dismissed, Curative Petition can be filed (Rupa Hurra)", "SC may grant or refuse leave at preliminary stage"]
        ],
        "rows_ta": [
          ["ஆய்வு செய்யப்படும் உத்தரவு", "உயர் நீதிமன்றத் தீர்ப்பு அல்லது உத்தரவு", "உச்ச நீதிமன்றத்தின் சொந்த தீர்ப்பு அல்லது உத்தரவு", "இந்தியாவில் உள்ள எந்தவொரு நீதிமன்ற உத்தரவு (இராணுவத் தவிர)"],
          ["அரசியலமைப்பு உரிமை", "அரசியலமைப்பு / சட்டப்பூர்வ மேல்முறையீட்டு உரிமை", "பதிவேட்டின் முகப்பிலுள்ள பிழையைத் திருத்தும் அதிகாரம்", "உச்ச நீதிமன்றத்தின் சிறப்பு எச்ச விருப்பவுரிமை அதிகாரம்"],
          ["முன்-தேவை சான்றிதழ்", "HC சான்றிதழ் (விதி 134A) அல்லது மரண தண்டனை தேவை", "வெளிப்படையான பிழை அல்லது புதிய ஆதாரம் தேவை", "HC சான்றிதழ் தேவையில்லை; SC அனுமதி அளிக்கிறது"],
          ["இறுதி பரிகார வளர்ச்சி", "SC தீர்ப்பிற்கு வழிவகுக்கிறது", "தள்ளுபடி செய்யப்பட்டால் நிவர்த்தி மனு (Curative Petition) தாக்கல் செய்யலாம்", "ஆரம்ப நிலையிலேயே அனுமதி வழங்கவோ மறுக்கவோ SC-க்கு அதிகாரம்"]
        ]
      },
      {
        "id": "tbl_collegium_vs_text_p3",
        "title_en": "7. Collegium Practice vs Constitutional Appointment Text",
        "title_ta": "7. கொலீஜியம் நடைமுறை vs அரசியலமைப்பு நியமன உரை ஒப்பீடு",
        "headers_en": ["Aspect", "Constitutional Text (Article 124(2))", "Collegium System Practice"],
        "headers_ta": ["அம்சம்", "அரசியலமைப்பு உரை (உறுப்பு 124(2))", "கொலீஜியம் அமைப்பு நடைமுறை"],
        "rows_en": [
          ["Key Term Used", "Uses the term 'CONSULTATION' with CJI & judges", "Interpreted 'Consultation' as 'CONCURRENCE' (2nd Judges Case 1993)"],
          ["Structural Body", "Does not mention any 'Collegium' body", "CJI + 4 Senior-most SC Judges (3rd Judges Case 1998)"],
          ["Executive Role", "Gave President discretion after consultation", "Judicial primacy; Government bound upon reiteration"],
          ["Evolution Source", "Written text of Constitution of India 1950", "Judicially evolved through 1981, 1993, 1998, 2015 SC judgments"],
          ["NJAC Outcome", "99th Amend introduced NJAC body", "NJAC struck down in 4th Judges Case (2015); Collegium restored"]
        ],
        "rows_ta": [
          ["முக்கியச் சொல்", "CJI மற்றும் நீதிபதிகளுடன் 'ஆலோசனை' என்ற சொல்லைப் பயன்படுத்துகிறது", "'ஆலோசனை' என்பதை 'ஒப்புதல்' என விளக்கியது (2-வது வழக்கு 1993)"],
          ["அமைப்புக் குழு", "'கொலீஜியம்' என்ற அமைப்பைக் குறிப்பிடவில்லை", "CJI + 4 மூத்த உச்ச நீதிமன்ற நீதிபதிகள் கொண்ட குழு (3-வது வழக்கு 1998)"],
          ["நிர்வாகத்தின் பங்கு", "ஆலோசனைக்குப் பின் குடியரசுத் தலைவருக்கு விருப்பவுரிமை அளித்தது", "நீதித்துறை முதன்மை; மீண்டும் வலியுறுத்தப்படும் போது அரசு கட்டுப்படும்"],
          ["வளர்ச்சி ஆதாரம்", "1950 இந்திய அரசியலமைப்பின் எழுதப்பட்ட உரை", "1981, 1993, 1998, 2015 உச்ச நீதிமன்றத் தீர்ப்புகள் மூலம் உருவானது"],
          ["NJAC முடிவு", "99-வது திருத்தம் NJAC அமைப்பை அறிமுகப்படுத்தியது", "4-வது நீதிபதிகள் வழக்கில் (2015) NJAC ரத்து செய்யப்பட்டு கொலீஜியம் மீண்டும் வந்தது"]
        ]
      },
      {
        "id": "tbl_independence_vs_accountability_p3",
        "title_en": "8. Judicial Independence vs Judicial Accountability Comparison",
        "title_ta": "8. நீதித்துறை சுதந்திரம் vs நீதித்துறை பொறுப்புக்கூறல் ஒப்பீடு",
        "headers_en": ["Feature", "Judicial Independence Safeguards", "Judicial Accountability Mechanisms"],
        "headers_ta": ["அம்சம்", "நீதித்துறை சுதந்திரப் பாதுகாப்புகள்", "நீதித்துறை பொறுப்புக்கூறல் அமைப்புகள்"],
        "rows_en": [
          ["Core Objective", "Protecting judges from executive/legislative political interference", "Ensuring judges remain accountable to Constitution and ethical standards"],
          ["Key Provisions", "Security of tenure (Art 124(4)), Charged expenses (Art 146)", "Removal procedure for proved misbehaviour/incapacity (Art 124(4))"],
          ["Discussion Protection", "Conduct cannot be discussed in Parliament (Art 121)", "Conduct discussed during Removal Motion debate in Parliament"],
          ["Post-Retirement Rule", "Ban on practice in any court in India (Art 124(7))", "In-house judicial ethics code & public transparency declarations"]
        ],
        "rows_ta": [
          ["முதன்மை நோக்கம்", "நிர்வாக/சட்டமன்ற அரசியல் தலையீட்டிலிருந்து நீதிபதிகளைப் பாதுகாத்தல்", "நீதிபதிகள் அரசியலமைப்புக்கும் நன்னெறித் தரங்களுக்கும் பொறுப்புடன் இருப்பதை உறுதி செய்தல்"],
          ["முக்கிய விதிகள்", "பதவிப் பாதுகாப்பு (விதி 124(4)), சுமத்தப்பட்ட செலவுகள் (விதி 146)", "நிரூபிக்கப்பட்ட தவறான நடத்தைக்கான நீக்க நடைமுறை (விதி 124(4))"],
          ["விவாதப் பாதுகாப்பு", "நீதிபதிகள் நடத்தையை நாடாளுமன்றத்தில் விவாதிக்க முடியாது (விதி 121)", "நீக்கத் தீர்மான விவாதத்தின் போது நடத்தையை விவாதிக்கலாம்"],
          ["ஓய்வுக்குப் பின் விதி", "இந்தியாவின் எந்த நீதிமன்றத்திலும் பயிற்சி செய்யத் தடை (விதி 124(7))", "உள்-அமைப்பு நீதித்துறை நன்னெறி விதிகள் & வெளிப்படைத்தன்மை பிரகடனங்கள்"]
        ]
      },
      {
        "id": "tbl_amendment_vs_basic_structure_p3",
        "title_en": "9. Constitutional Amendment vs Basic Structure Limitation",
        "title_ta": "9. அரசியலமைப்புத் திருத்தம் vs அடிப்படை கட்டமைப்பு வரம்பு ஒப்பீடு",
        "headers_en": ["Feature", "Constitutional Amendment Power (Article 368)", "Basic Structure Limitation (Kesavananda 1973)"],
        "headers_ta": ["அம்சம்", "அரசியலமைப்புத் திருத்த அதிகாரம் (உறுப்பு 368)", "அடிப்படை கட்டமைப்பு வரம்பு (கேசவாநந்த 1973)"],
        "rows_en": [
          ["Organ Holding Power", "PARLIAMENT OF INDIA (Constituent Power)", "JUDICIARY (Supreme Court of India)"],
          ["Scope of Power", "Empowers Parliament to add, vary, or repeal any provision", "Limits Article 368 power; Parliament CANNOT alter Basic Features"],
          ["Judicial Test", "Amendments passed by Special Majority", "Subject to Judicial Review test under Basic Structure Doctrine"],
          ["Landmark Anchor", "Part XX Article 368", "Kesavananda Bharati (1973), Minerva Mills (1980), I.R. Coelho (2007)"]
        ],
        "rows_ta": [
          ["அதிகாரம் கொண்ட உறுப்பு", "இந்திய நாடாளுமன்றம் (அரசியலமைப்பு உருவாக்க அதிகாரம்)", "நீதித்துறை (இந்திய உச்ச நீதிமன்றம்)"],
          ["அதிகார எல்லை", "எந்தவொரு விதியையும் சேர்க்க, மாற்ற, ரத்து செய்ய அதிகாரமளிக்கிறது", "விதி 368 அதிகாரத்தை வரையறுக்கிறது; அடிப்படை கூறுகளை மாற்ற முடியாது"],
          ["நீதித்துறை சோதனை", "சிறப்பு பெரும்பான்மையால் நிறைவேற்றப்படும் திருத்தங்கள்", "அடிப்படை கட்டமைப்புக் கோட்பாட்டின் கீழ் நீதித்துறை ஆய்வுக்கு உட்பட்டவை"],
          ["வரலாற்று ஆதாரம்", "பகுதி XX உறுப்பு 368", "கேசவாநந்த பாரதி (1973), மினெர்வா மில்ஸ் (1980), ஐ.ஆர். கோயல்ஹோ (2007)"]
        ]
      }
    ],
    "mind_map": [
      {
        "title": "Supreme Court Advanced Constitutional Concepts (Part V & XX)",
        "short_label": "Supreme Court Part 3",
        "children": [
          {
            "title": "1. Judicial Review & Activism",
            "short_label": "Review & Activism",
            "children": [
              {"title": "Judicial Review: Arts 13, 32, 131-142; Strikes down unconstitutional laws", "short_label": "Judicial Review"},
              {"title": "Activism vs Restraint: Proactive Art 21 expansion vs Self-imposed discipline", "short_label": "Activism/Restraint"},
              {"title": "PIL: Relaxed Locus Standi; Pioneers Krishna Iyer & Bhagwati (S.P. Gupta 1981)", "short_label": "PIL"}
            ]
          },
          {
            "title": "2. Basic Structure Doctrine",
            "short_label": "Basic Structure",
            "children": [
              {"title": "Kesavananda Bharati (April 24, 1973): 13 Judges Bench (7-6); Art 368 limited", "short_label": "Kesavananda 1973"},
              {"title": "Minerva Mills (1980): Judicial Review & FR-DPSP Harmony is Basic Feature", "short_label": "Minerva Mills"},
              {"title": "S.R. Bommai (1994): Secularism & Federalism; I.R. Coelho (2007): 9th Schedule review", "short_label": "Bommai/Coelho"}
            ]
          },
          {
            "title": "3. Collegium & NJAC Invalidation",
            "short_label": "Collegium & NJAC",
            "children": [
              {"title": "Collegium: CJI + 4 Senior SC Judges (3rd Judges 1998); Judicially evolved", "short_label": "Collegium 5"},
              {"title": "4th Judges Case (2015): 99th Amend NJAC struck down; Judicial Independence restored", "short_label": "NJAC Struck Down"}
            ]
          },
          {
            "title": "4. Separation of Powers & Landmark Cases",
            "short_label": "Powers & Landmark Cases",
            "children": [
              {"title": "Separation of Powers & Safeguards: Charged expenses (Art 146), Discussion ban (Art 121), Practice ban (Art 124(7))", "short_label": "Independence"},
              {"title": "Landmark Cases: Maneka Gandhi (1978 Due Process), Vishaka (1997), Puttaswamy (2017 Privacy)", "short_label": "Landmark Cases"}
            ]
          }
        ]
      }
    ],
    "tnpsc_traps": [
      {
        "title": "1. Kesavananda Bharati Date & Bench Trap (கேசவாநந்த பாரதி தேதி & அமர்வுப் பொறி)",
        "points": {
          "en": [
            "TRAP: Confusing the bench size or date of the Kesavananda Bharati judgment.",
            "FACT: Kesavananda Bharati judgment was delivered on APRIL 24, 1973 by the LARGEST BENCH IN INDIAN HISTORY — 13 JUDGES (Decided by a 7-6 majority)!"
          ],
          "ta": [
            "பொறி: கேசவாநந்த பாரதி தீர்ப்பின் அமர்வு அளவு அல்லது தேதியை குழப்பிக் கொள்ளுதல்.",
            "உண்மை: கேசவாநந்த பாரதி தீர்ப்பு ஏப்ரல் 24, 1973 அன்று இந்திய வரலாற்றிலேயே மிகப்பெரிய 13 நீதிபதிகள் கொண்ட அமர்வால் (7-6 பெரும்பான்மையால்) வழங்கப்பட்டது!"
          ]
        }
      },
      {
        "title": "2. Ninth Schedule Immunity Expiration Trap (9-வது அட்டவணை பாதுகாப்புக் காலப் பொறி)",
        "points": {
          "en": [
            "TRAP: Believing all laws in the Ninth Schedule are completely immune from Judicial Review.",
            "FACT: In I.R. Coelho Case (2007), a 9-Judge Bench held that laws placed in the Ninth Schedule AFTER APRIL 24, 1973 ARE SUBJECT TO JUDICIAL REVIEW under the Basic Structure test!"
          ],
          "ta": [
            "பொறி: 9-வது அட்டவணையில் உள்ள அனைத்துச் சட்டங்களுக்கும் நீதித்துறை ஆய்விலிருந்து முழுப் பாதுகாப்பு உண்டு என நினைப்பது.",
            "உண்மை: ஐ.ஆர். கோயல்ஹோ வழக்கில் (2007) 9 நீதிபதிகள் அமர்வு ஏப்ரல் 24, 1973-க்கு பின் 9-வது அட்டவணையில் வைக்கப்பட்ட சட்டங்கள் அடிப்படை கட்டமைப்பு ஆய்வுக்கு உட்பட்டவை எனத் தீர்ப்பளித்தது!"
          ]
        }
      },
      {
        "title": "3. Due Process of Law Case Origin Trap ('Due Process of Law' வழக்கு தோற்றப் பொறி)",
        "points": {
          "en": [
            "TRAP: Thinking 'Due Process of Law' was established in AK Gopalan case (1950).",
            "FACT: AK Gopalan case rejected 'Due Process'. It was the MANEKA GANDHI CASE (1978) that established 'Due Process of Law' in Article 21, requiring procedure to be Fair, Just, and Reasonable!"
          ],
          "ta": [
            "பொறி: 'சரியான சட்ட நடைமுறை (Due Process of Law)' ஏ.கே. கோபாலன் வழக்கில் (1950) நிறுவப்பட்டது என நினைப்பது.",
            "உண்மை: ஏ.கே. கோபாலன் வழக்கு அதை நிராகரித்தது. மேனகா காந்தி வழக்கே (1978) உறுப்பு 21-ல் 'சரியான சட்ட நடைமுறையை' நிறுவி, நடைமுறை நியாயமானதாக இருக்க வேண்டும் எனக்கூறியது!"
          ]
        }
      },
      {
        "title": "4. PIL Locus Standi Exception Trap (பொது நல வழக்கு Locus Standi விலக்குப் பொறி)",
        "points": {
          "en": [
            "TRAP: Assuming PIL can be filed for private personal property or family disputes.",
            "FACT: PIL is allowed ONLY for public cause or enforcement of rights of disadvantaged groups. Frivolous private or personal disputes filed as PIL are dismissed with heavy penalty costs!"
          ],
          "ta": [
            "பொறி: தனிப்பட்ட சொத்து அல்லது குடும்பத் தகராறுகளுக்கு பொது நல வழக்கு (PIL) தாக்கல் செய்யலாம் என நினைப்பது.",
            "உண்மை: பொது காரணம் அல்லது பின்தங்கிய வகுப்பினரின் உரிமைகளுக்கு மட்டுமே PIL அனுமதிக்கப்படும். தனிப்பட்ட தகராறுகளுக்கு தாக்கல் செய்யப்படும் PIL அபராதத்துடன் தள்ளுபடி செய்யப்படும்!"
          ]
        }
      },
      {
        "title": "5. Fourth Judges Case NJAC Invalidation Trap (4-வது நீதிபதிகள் வழக்கு NJAC ரத்துப் பொறி)",
        "points": {
          "en": [
            "TRAP: Believing NJAC was invalidated because it was passed without 2/3rd majority in Parliament.",
            "FACT: NJAC (99th Amendment) was passed with near unanimity in Parliament, BUT was struck down by Supreme Court in 2015 because executive inclusion violated 'Judicial Independence', a Basic Feature!"
          ],
          "ta": [
            "பொறி: நாடாளுமன்றத்தில் 2/3 பங்கு பெரும்பான்மையுடன் நிறைவேற்றப்படாததால் NJAC ரத்து செய்யப்பட்டது என நினைப்பது.",
            "உண்மை: NJAC நாடாளுமன்றத்தில் ஒருமனதாக நிறைவேற்றப்பட்டது, ஆனால் நிர்வாகச் சேர்க்கை அடிப்படை கட்டமைப்பான 'நீதித்துறை சுதந்திரத்தைப்' பாதித்ததால் 2015-ல் உச்ச நீதிமன்றத்தால் ரத்து செய்யப்பட்டது!"
          ]
        }
      }
    ],
    "quick_revision": {
      "en": [
        "Judicial Review: Power to examine constitutionality of laws & executive orders (Arts 13, 32, 131-142, 246). Unconstitutional laws declared void.",
        "Judicial Activism vs Restraint: Activism = Proactive protection of public interest & Art 21 expansion. Restraint = Self-imposed discipline respecting separation of powers.",
        "Public Interest Litigation (PIL): Relaxation of locus standi. Pioneers: Justice V.R. Krishna Iyer & Justice P.N. Bhagwati (S.P. Gupta 1981). Epistolary jurisdiction (letters/postcards).",
        "Basic Structure Doctrine: Established in Kesavananda Bharati (April 24, 1973 - 13 Judges Bench 7-6). Art 368 amending power wide but CANNOT alter Basic Structure.",
        "Evolution of Basic Structure: Shankari Prasad (1951) & Sajjan Singh (1965) allowed FR amend -> Golaknath (1967) banned FR amend -> Kesavananda (1973) Basic Structure -> Minerva Mills (1980) Judicial Review Basic Feature -> I.R. Coelho (2007) 9th Sch post-1973 review.",
        "Collegium System: CJI + 4 senior SC judges. Judicially evolved. 99th Amend NJAC struck down in 4th Judges Case (2015) for violating Judicial Independence.",
        "Landmark Cases: Maneka Gandhi (1978 Due Process), S.R. Bommai (1994 Secularism/Federalism), Vishaka (1997 Workplace Safety), Rupa Hurra (2002 Curative Petition), Puttaswamy (2017 Privacy)."
      ],
      "ta": [
        "நீதித்துறை ஆய்வு: சட்டங்கள் & நிர்வாக உத்தரவுகளின் அரசியலமைப்புத் தன்மையை ஆய்வு செய்யும் அதிகாரம் (விதிகள் 13, 32, 131-142, 246). அரசியலமைப்புக்கு எதிரானவை ரத்து.",
        "நீதித்துறை செயலாக்கம் vs சுயகட்டுப்பாடு: செயலாக்கம் = பொது நலன் & விதி 21 முன்முயற்சி பாதுகாப்பு. சுயகட்டுப்பாடு = அதிகாரப் பகிர்வை மதித்து சுயமாக விதிக்கும் கட்டுப்பாடு.",
        "பொது நல வழக்கு (PIL): Locus standi தளர்வு. முன்னோடிகள்: நீதிபதி V.R. கிருஷ்ணய்யர் & P.N. பகவதி (எஸ்.பி. குப்தா 1981). கடித வடிவிலான ஆதிக்கம்.",
        "அடிப்படை கட்டமைப்புக் கோட்பாடு: கேசவாநந்த பாரதி வழக்கில் நிறுவல் (ஏப்ரல் 24, 1973 - 13 நீதிபதிகள் அமர்வு 7-6). விதி 368 திருத்த அதிகாரம் பரந்தது ஆனால் அடிப்படை கட்டமைப்பை மாற்ற முடியாது.",
        "வளர்ச்சி வரலாறு: சங்கரி பிரசாத் (1951) திருத்தம் அனுமதி -> கோலக்நாத் (1967) திருத்தம் தடை -> கேசவாநந்த (1973) அடிப்படை கட்டமைப்பு -> மினெர்வா மில்ஸ் (1980) நீதித்துறை ஆய்வு -> ஐ.ஆர். கோயல்ஹோ (2007) 9-வது அட்டவணை 1973-க்குப் பின் ஆய்வு.",
        "கொலீஜியம் அமைப்பு: CJI + 4 மூத்த SC நீதிபதிகள். நீதித்துறையால் உருவானது. 99-வது திருத்த NJAC 4-வது வழக்கில் (2015) ரத்து.",
        "முக்கிய வழக்குகள்: மேனகா காந்தி (1978 சரியான சட்ட நடைமுறை), எஸ்.ஆர். பொம்மை (1994 மதச்சார்பின்மை/கூட்டாட்சி), விசாகா (1997 பணியிட பாதுகாப்பு), ரூபா ஹுர்ரா (2002 நிவர்த்தி மனு), புட்டசுவாமி (2017 தனிப்பரிவு)."
      ]
    },
    "must_remember": {
      "en": [
        "MUST REMEMBER: Kesavananda Bharati judgment was delivered on APRIL 24, 1973 by a 13-Judge Bench (7-6 majority).",
        "MUST REMEMBER: Basic Structure Doctrine limits Parliament's amending power under Article 368.",
        "MUST REMEMBER: Minerva Mills Case (1980) declared Judicial Review and FR-DPSP Harmony as Basic Features.",
        "MUST REMEMBER: I.R. Coelho Case (2007) held 9th Schedule laws post-April 24, 1973 are subject to Judicial Review.",
        "MUST REMEMBER: Maneka Gandhi Case (1978) established 'Due Process of Law' in Article 21.",
        "MUST REMEMBER: S.R. Bommai Case (1994) declared Secularism and Federalism as Basic Features.",
        "MUST REMEMBER: Fourth Judges Case (2015) invalidated 99th Amendment (NJAC) to protect Judicial Independence.",
        "MUST REMEMBER: Supreme Court Collegium consists of CJI + 4 senior-most Supreme Court judges.",
        "MUST REMEMBER: Justice V.R. Krishna Iyer and Justice P.N. Bhagwati are pioneers of PIL in India.",
        "MUST REMEMBER: K.S. Puttaswamy Case (2017) declared Right to Privacy as a Fundamental Right under Article 21."
      ],
      "ta": [
        "நினைவில் கொள்க: கேசவாநந்த பாரதி தீர்ப்பு ஏப்ரல் 24, 1973 அன்று 13 நீதிபதிகள் அமர்வால் (7-6) வழங்கப்பட்டது.",
        "நினைவில் கொள்க: அடிப்படை கட்டமைப்புக் கோட்பாடு உறுப்பு 368 நாடாளுமன்றத் திருத்த அதிகாரத்தை வரையறுக்கிறது.",
        "நினைவில் கொள்க: மினெர்வா மில்ஸ் வழக்கு (1980) நீதித்துறை ஆய்வு மற்றும் FR-DPSP சமநிலையை அடிப்படை கூறுகளாக அறிவித்தது.",
        "நினைவில் கொள்க: ஐ.ஆர். கோயல்ஹோ வழக்கு (2007) ஏப்ரல் 24, 1973-க்கு பின் 9-வது அட்டவணைச் சட்டங்கள் நீதித்துறை ஆய்வுக்கு உட்பட்டவை என்றது.",
        "நினைவில் கொள்க: மேனகா காந்தி வழக்கு (1978) உறுப்பு 21-ல் 'சரியான சட்ட நடைமுறையை (Due Process of Law)' நிறுவியது.",
        "நினைவில் கொள்க: எஸ்.ஆர். பொம்மை வழக்கு (1994) மதச்சார்பின்மை மற்றும் கூட்டாட்சியை அடிப்படை கூறுகளாக அறிவித்தது.",
        "நினைவில் கொள்க: 4-வது நீதிபதிகள் வழக்கு (2015) நீதித்துறை சுதந்திரத்தைப் பாதுகாக்க 99-வது திருத்தத்தை (NJAC) ரத்து செய்தது.",
        "நினைவில் கொள்க: உச்ச நீதிமன்ற கொலீஜியத்தில் CJI + 4 மூத்த உச்ச நீதிமன்ற நீதிபதிகள் இருப்பர்.",
        "நினைவில் கொள்க: நீதிபதி V.R. கிருஷ்ணய்யர் மற்றும் P.N. பகவதி இந்தியாவில் PIL-ன் முன்னோடிகள் ஆவர்.",
        "நினைவில் கொள்க: கே.எஸ். புட்டசுவாமி வழக்கு (2017) தனிப்பரிவு உரிமையை (Right to Privacy) உறுப்பு 21 கீழ் அடிப்படை உரிமையாக அறிவித்தது."
      ]
    }
  }
}

target_file = "data/notes/polity/supreme_court_part_3.json"
os.makedirs("data/notes/polity", exist_ok=True)

with open(target_file, "w", encoding="utf-8") as f:
  json.dump(part3_data, f, ensure_ascii=False, indent=2)

print(f"✅ Supreme Court Part 3 successfully saved to: {target_file}")
