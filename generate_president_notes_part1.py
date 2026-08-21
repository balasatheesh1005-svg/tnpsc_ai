import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("Generating President Part 1 Notes...")

data = {
  "meta": {
    "topic_id": "polity_president_part_1",
    "repository_id": "polity_president",
    "display_title": "President – Part 1",
    "part": 1,
    "total_parts": 3,
    "subject": "polity",
    "chapter": "President of India",
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
    "President of India",
    "இந்தியக் குடியரசுத் தலைவர்",
    "Article 52",
    "உறுப்பு 52",
    "Article 53 Union Executive",
    "உறுப்பு 53 மத்திய நிர்வாகம்",
    "Article 54 Electoral College",
    "உறுப்பு 54 வாக்காளர் குழு",
    "Article 55 Value of Votes",
    "உறுப்பு 55 வாக்குகளின் மதிப்பு",
    "Article 56 Term of Office",
    "உறுப்பு 56 பதவிக்காலம்",
    "Article 58 Qualifications",
    "உறுப்பு 58 தகுதிகள்",
    "Article 59 Conditions of Office",
    "உறுப்பு 59 அலுவலக நிபந்தனைகள்",
    "Article 60 Oath or Affirmation",
    "உறுப்பு 60 உறுதிமொழி",
    "Article 61 Impeachment",
    "உறுப்பு 61 பதவி நீக்கம்",
    "Single Transferable Vote",
    "ஒற்றை மாற்று வாக்கு முறை",
    "Proportional Representation",
    "விகிதாச்சாரப் பிரதிநிதித்துவம்"
  ],
  "learning_outcomes": {
    "Understand": {
      "en": [
        "Understand the constitutional position of the President as the nominal executive head under Articles 52 & 53.",
        "Understand the composition of the Electoral College for Presidential election under Article 54.",
        "Understand the vote value formulas for MLAs and MPs under Article 55.",
        "Understand the election method of Proportional Representation by Single Transferable Vote (STV) with secret ballot.",
        "Understand qualifications, conditions of office, oath, term, vacancy, and impeachment foundation under Articles 56–61."
      ],
      "ta": [
        "உறுப்புகள் 52 & 53-ன் கீழ் இந்தியாவின் பெயரளவு நிர்வாகத் தலைவராகக் குடியரசுத் தலைவரின் நிலையைப் புரிந்து கொள்ளுதல்.",
        "உறுப்பு 54-ன் கீழ் குடியரசுத் தலைவர் தேர்தலுக்கான வாக்காளர் குழுவின் அமைப்பைப் புரிந்து கொள்ளுதல்.",
        "உறுப்பு 55-ன் கீழ் எம்.எல்.ஏ மற்றும் எம்பி வாக்குகளின் மதிப்புகளைக் கணக்கிடும் சூத்திரங்களைப் புரிந்து கொள்ளுதல்.",
        "ரகசிய வாக்களிப்புடன் ஒற்றை மாற்று வாக்கு மூலமான விகிதாச்சாரப் பிரதிநிதித்துவத் தேர்தல் முறையைப் புரிந்து கொள்ளுதல்.",
        "உறுப்புகள் 56–61 வரையிலான தகுதிகள், நிபந்தனைகள், உறுதிமொழி, பதவிக்காலம், காலியிடம் மற்றும் பதவி நீக்கத்தைப் புரிந்து கொள்ளுதல்."
      ]
    },
    "Remember": {
      "en": [
        "Remember Article 52 ('There shall be a President of India').",
        "Remember nominated MPs and all Legislative Council members DO NOT vote in Presidential election.",
        "Remember 70th CAA 1992 added elected MLAs of Delhi and Puducherry to Electoral College.",
        "Remember 1971 Census population is used for MLA vote value until first census after 2026.",
        "Remember Article 60 oath is to 'preserve, protect and defend the Constitution'."
      ],
      "ta": [
        "உறுப்பு 52 ('இந்தியாவிற்கு ஒரு குடியரசுத் தலைவர் இருக்க வேண்டும்') என்பதை நினைவில் கொள்ளுதல்.",
        "நியமன எம்பிக்கள் மற்றும் சட்ட மேலவை உறுப்பினர்கள் குடியரசுத் தலைவர் தேர்தலில் வாக்களிக்க முடியாது என்பதை நினைவில் கொள்ளுதல்.",
        "70வது திருத்தம் 1992 டெல்லி மற்றும் புதுச்சேரி எம்.எல்.ஏ-க்களை வாக்காளர் குழுவில் சேர்த்தது என்பதை நினைவில் கொள்ளுதல்.",
        "2026-க்குப் பிந்தைய முதல் மக்கள் தொகை கணக்கெடுப்பு வரை 1971 கணக்கெடுப்பே பயன்படுத்தப்படுகிறது என்பதை நினைவில் கொள்ளுதல்.",
        "உறுப்பு 60 உறுதிமொழி 'அரசியலமைப்பைப் பேணவும், பாதுகாக்கவும், தற்காக்கவும்' என்பதாகும் என்பதை நினைவில் கொள்ளுதல்."
      ]
    },
    "Analyze": {
      "en": [
        "Analyze differences between President's Electoral College (elected only) and Vice-President's Electoral College (elected + nominated MPs).",
        "Analyze why uniformity among States and parity between States and Union is maintained under Article 55.",
        "Analyze why nominated MPs vote in impeachment (Art 61) but not in election (Art 54).",
        "Analyze nominal executive (President) vs real executive (Prime Minister & Council of Ministers)."
      ],
      "ta": [
        "குடியரசுத் தலைவர் வாக்காளர் குழு மற்றும் துணைத் தலைவர் வாக்காளர் குழு இடையேயான வேறுபாடுகளை பகுப்பாய்வு செய்தல்.",
        "மாநிலங்களுக்கிடையேயான சீரான தன்மை மற்றும் மாநிலங்கள்-மத்திய அரசு சமநிலை ஏன் பராமரிக்கப்படுகிறது என்பதை பகுப்பாய்வு செய்தல்.",
        "நியமன எம்பிக்கள் தேர்தலில் வாக்களிக்க முடியாத நிலையில் பதவி நீக்கத்தில் ஏன் வாக்களிக்கலாம் என்பதை பகுப்பாய்வு செய்தல்.",
        "பெயரளவு நிர்வாகி (குடியரசுத் தலைவர்) vs உண்மை நிர்வாகி (பிரதமர் & அமைச்சரவை) நிலையை பகுப்பாய்வு செய்தல்."
      ]
    },
    "Apply": {
      "en": [
        "Apply TNPSC elimination strategies to solve tricky MCQs on voting rights.",
        "Accurately calculate vote value concepts under Article 55.",
        "Match Articles 52 to 61 with constitutional titles in exam questions."
      ],
      "ta": [
        "வாக்குரிமை பற்றிய வினாக்களில் நீக்கல் உத்திகளைப் பயன்படுத்துதல்.",
        "உறுப்பு 55-ன் கீழ் வாக்கு மதிப்புக் கருத்துகளைத் துல்லியமாகக் கணக்கிடுதல்.",
        "தேர்வு வினாக்களில் உறுப்புகள் 52 முதல் 61 வரையிலானவற்றைத் தலைப்புகளுடன் பொருத்துதல்."
      ]
    }
  },
  "subject": "Polity",
  "topic": "President of India – Part 1",
  "language": "bilingual",
  "ui_type": "polity",
  "sections": [
    {
      "id": "sec_constitutional_position",
      "title_en": "1. Constitutional Position & Executive Power (Articles 52 & 53)",
      "title_ta": "1. அரசியலமைப்பு நிலை & நிர்வாக அதிகாரம் (உறுப்புகள் 52 & 53)",
      "type": "standard_topic"
    },
    {
      "id": "sec_electoral_college",
      "title_en": "2. Election of President & Electoral College (Article 54)",
      "title_ta": "2. குடியரசுத் தலைவர் தேர்தல் & வாக்காளர் குழு (உறுப்பு 54)",
      "type": "standard_topic"
    },
    {
      "id": "sec_value_of_votes",
      "title_en": "3. Value of Votes & Principle of Parity (Article 55)",
      "title_ta": "3. வாக்குகளின் மதிப்பு & சமநிலைத் தத்துவம் (உறுப்பு 55)",
      "type": "standard_topic"
    },
    {
      "id": "sec_method_of_election",
      "title_en": "4. Method of Election: STV & Electoral Quota",
      "title_ta": "4. தேர்தல் முறை: ஒற்றை மாற்று வாக்கு & தேர்தல் பங்கு",
      "type": "standard_topic"
    },
    {
      "id": "sec_qualifications",
      "title_en": "5. Qualifications for Office (Article 58)",
      "title_ta": "5. பதவிக்கான தகுதிகள் (உறுப்பு 58)",
      "type": "standard_topic"
    },
    {
      "id": "sec_conditions_of_office",
      "title_en": "6. Conditions of President's Office (Article 59)",
      "title_ta": "6. குடியரசுத் தலைவர் அலுவலக நிபந்தனைகள் (உறுப்பு 59)",
      "type": "standard_topic"
    },
    {
      "id": "sec_oath_affirmation",
      "title_en": "7. Oath or Affirmation by the President (Article 60)",
      "title_ta": "7. குடியரசுத் தலைவரின் உறுதிமொழி (உறுப்பு 60)",
      "type": "standard_topic"
    },
    {
      "id": "sec_term_resignation_re-election",
      "title_en": "8. Term of Office, Resignation & Re-election (Articles 56 & 57)",
      "title_ta": "8. பதவிக்காலம், ராஜினாமா & மறுதேர்தல் (உறுப்புகள் 56 & 57)",
      "type": "standard_topic"
    },
    {
      "id": "sec_vacancy_impeachment",
      "title_en": "9. Vacancy in Office & Impeachment Foundation (Articles 62 & 61)",
      "title_ta": "9. அலுவலகக் காலியிடம் & பதவி நீக்க அடிப்படை (உறுப்புகள் 62 & 61)",
      "type": "standard_topic"
    },
    {
      "id": "sec_comparison_tables",
      "title_en": "10. Mandatory Comparison Tables (Oppositional Analysis)",
      "title_ta": "10. கட்டாய ஒப்பீட்டு அட்டவணைகள் (எதிரெதிர் பகுப்பாய்வு)",
      "type": "standard_topic"
    },
    {
      "id": "sec_mind_map_traps",
      "title_en": "11. Mind Map & TNPSC Trap Points",
      "title_ta": "11. மன வரைபடம் & டிஎன்பிஎஸ்சி பொறி புள்ளிகள்",
      "type": "standard_topic"
    },
    {
      "id": "sec_revision",
      "title_en": "12. Must Remember, Rapid Revision & Flashcards",
      "title_ta": "12. முக்கிய நினைவூட்டல், அதிவிரைவுத் திருப்புதல் & அட்டைகள்",
      "type": "standard_topic"
    }
  ],
  "content": {
    "definition": {
      "en": "The President of India is the Head of State, First Citizen of India, and Constitutional Supreme Commander of the Armed Forces under Part V (Articles 52–62). Exercising executive power under Article 53 on the advice of the Council of Ministers (Article 74), the President is indirectly elected by an Electoral College consisting of elected MPs and elected MLAs of States and UTs (Delhi & Puducherry) through proportional representation by single transferable vote.",
      "ta": "இந்தியக் குடியரசுத் தலைவர் பகுதி V (உறுப்புகள் 52–62) ன் கீழ் அரசின் தலைவர், இந்தியாவின் முதல் குடிமகன் மற்றும் ஆயுதப்படைகளின் அரசியலமைப்பு உச்சத் தளபதி ஆவார். உறுப்பு 74-ன் கீழ் அமைச்சரவையின் ஆலோசனையின் பேரில் உறுப்பு 53-ன் கீழ் நிர்வாக அதிகாரத்தைச் செலுத்தும் இவர், ஒற்றை மாற்று வாக்கு மூலமான விகிதாச்சாரப் பிரதிநிதித்துவ அடிப்படையில் தேர்ந்தெடுக்கப்பட்ட எம்பிக்கள் மற்றும் மாநில/யூனியன் பிரதேச (டெல்லி & புதுச்சேரி) எம்.எல்.ஏ-க்களைக் கொண்ட வாக்காளர் குழுவால் மறைமுகமாகத் தேர்ந்தெடுக்கப்படுகிறார்."
    },
    "introduction": {
      "en": "Part 1 of the President of India series provides an exhaustive analysis of the constitutional position, election mechanism, vote value formulas, method of voting, qualifications, conditions of office, oath, term, vacancy, and impeachment foundation under Articles 52 to 61. It features 10 mandatory comparison tables, mind map, 10 bilingual TNPSC trap points, and a 2-minute rapid revision module.",
      "ta": "இந்தியக் குடியரசுத் தலைவர் தொடரின் பகுதி 1, உறுப்புகள் 52 முதல் 61 வரையிலான அரசியலமைப்பு நிலை, தேர்தல் முறை, வாக்கு மதிப்பு சூத்திரங்கள், வாக்களிப்பு முறை, தகுதிகள், அலுவலக நிபந்தனைகள், உறுதிமொழி, பதவிக்காலம், காலியிடம் மற்றும் பதவி நீக்க அடித்தளத்தை விரிவாக பகுப்பாய்வு செய்கிறது. இது 10 கட்டாய ஒப்பீட்டு அட்டவணைகள், மன வரைபடம், 10 இருமொழி டிஎன்பிஎஸ்சி பொறி புள்ளிகள் மற்றும் 2 நிமிட விரைவுத் திருப்புதல் தொகுதியைக் கொண்டுள்ளது."
    },
    "sec_constitutional_position": [
      {
        "title": "1. Article 52: President of India (இந்தியக் குடியரசுத் தலைவர்)",
        "points": {
          "en": [
            "Meaning: Establishes the office of the President of India as the Head of State and First Citizen.",
            "Constitutional Provision: Article 52 mandates 'There shall be a President of India'. It creates a permanent constitutional office with no interregnum.",
            "Simple Explanation: The President is the formal executive head of the Union of India, symbolising the unity, integrity, and solidarity of the nation.",
            "Example: All executive actions of the Union Government are formally taken in the name of the President (Article 77).",
            "Important Point: The office of President can never remain vacant even for a single moment; if the sitting President's term ends, they continue until the successor assumes office.",
            "TNPSC Trap: Article 52 specifies 'President of India', NOT 'President of the Executive'. Do not confuse Article 52 (Creation of Office) with Article 53 (Executive Power).",
            "2-Line Revision: Article 52 creates the office of President of India as Head of State. It is a mandatory permanent constitutional post."
          ],
          "ta": [
            "பொருள்: நாட்டின் தலைவர் மற்றும் முதல் குடிமகனாக இந்தியக் குடியரசுத் தலைவர் அலுவலகத்தை நிறுவுகிறது.",
            "அரசியலமைப்பு விதி: உறுப்பு 52 'இந்தியாவிற்கு ஒரு குடியரசுத் தலைவர் இருக்க வேண்டும்' எனக் கட்டாயப்படுத்துகிறது. இது காலியிடமற்ற நிரந்தர அரசியலமைப்பு பதவியை உருவாக்குகிறது.",
            "எளிய விளக்கம்: குடியரசுத் தலைவர் இந்திய ஒன்றியத்தின் முறைசார் நிர்வாகத் தலைவர் ஆவார், நாட்டின் ஒற்றுமை, ஒருமைப்பாடு மற்றும் ஒருமைப்பாட்டின் சின்னமாவார்.",
            "உதாரணம்: மத்திய அரசின் அனைத்து நிர்வாக நடவடிக்கைகளும் முறைப்படி குடியரசுத் தலைவரின் பெயரிலேயே எடுக்கப்படுகின்றன (உறுப்பு 77).",
            "முக்கிய புள்ளி: குடியரசுத் தலைவர் பதவி ஒரு கணம் கூட காலியாக இருக்க முடியாது; பதவியில் உள்ளவரின் காலம் முடிந்தாலும் புதியவர் பொறுப்பேற்கும் வரை அவரே தொடர்வார்.",
            "TNPSC பொறி: உறுப்பு 52 'இந்தியக் குடியரசுத் தலைவர்' எனக் குறிப்பிடுகிறது, 'நிர்வாகத் தலைவர்' என்று அல்ல. உறுப்பு 52 (பதவி உருவாக்கம்) மற்றும் உறுப்பு 53 (நிர்வாக அதிகாரம்) ஆகியவற்றை குழப்பிக் கொள்ள வேண்டாம்.",
            "2-வரி திருப்புதல்: உறுப்பு 52 இந்தியக் குடியரசுத் தலைவர் பதவியை உருவாக்குகிறது. இது ஒரு கட்டாய நிரந்தர அரசியலமைப்பு பதவியாகும்."
          ]
        }
      },
      {
        "title": "2. Article 53: Executive Power of the Union (ஒன்றியத்தின் நிர்வாக அதிகாரம்)",
        "points": {
          "en": [
            "Meaning: Vests the executive power of the Union of India in the President.",
            "Constitutional Provision: Article 53(1) states that executive power of the Union is vested in the President and exercised directly or through officers subordinate to him in accordance with the Constitution.",
            "Supreme Command: Article 53(2) vests the Supreme Command of the Defence Forces of the Union in the President, to be regulated by Parliamentary law.",
            "Simple Explanation: While executive power legally belongs to the President, under Article 74, it MUST be exercised on the aid and advice of the Council of Ministers headed by the Prime Minister.",
            "Example: Formal appointments of Governors, Ambassadors, and Judges are made by the President, but decided by the Cabinet.",
            "Important Point: 42nd CAA 1976 made Cabinet advice binding on President; 44th CAA 1978 added power to send advice back ONCE for reconsideration, but re-sent advice is binding.",
            "TNPSC Trap: President is Nominal (De Jure) Executive; Prime Minister is Real (De Facto) Executive. In India's parliamentary system, President acts as constitutional head, not real ruler.",
            "2-Line Revision: Article 53 vests Union executive power & Supreme Military Command in President. Power is exercised on Council of Ministers' binding advice."
          ],
          "ta": [
            "பொருள்: இந்திய ஒன்றியத்தின் நிர்வாக அதிகாரத்தைக் குடியரசுத் தலைவரிடம் ஒப்படைக்கிறது.",
            "அரசியலமைப்பு விதி: உறுப்பு 53(1) ஒன்றியத்தின் நிர்வாக அதிகாரம் குடியரசுத் தலைவரிடம் உள்ளது என்றும், அது நேரடியாகவோ அல்லது கீழ்நிலை அதிகாரிகள் மூலமாகவோ அரசியலமைப்பின் படி செலுத்தப்படும் என்றும் கூறுகிறது.",
            "உச்ச தளபதி அதிகாரம்: உறுப்பு 53(2) ஒன்றியத்தின் பாதுகாப்புப் படைகளின் உச்ச தளபதி அதிகாரத்தைக் குடியரசுத் தலைவரிடம் வழங்குகிறது (நாடாளுமன்றச் சட்டத்தால் சீர்படுத்தப்படும்).",
            "எளிய விளக்கம்: நிர்வாக அதிகாரம் சட்டப்படி குடியரசுத் தலைவரிடம் இருந்தாலும், உறுப்பு 74-ன் கீழ் பிரதமரைக் கொண்ட அமைச்சரவையின் ஆலோசனையின் பேரிலேயே அது செலுத்தப்பட வேண்டும்.",
            "உதாரணம்: ஆளுநர்கள், தூதர்கள், நீதிபதிகளின் முறைசார் நியமனங்கள் குடியரசுத் தலைவரால் செய்யப்படுகின்றன, ஆனால் அமைச்சரவையால் தீர்மானிக்கப்படுகின்றன.",
            "முக்கிய புள்ளி: 42வது திருத்தம் 1976 அமைச்சரவை ஆலோசனையைக் குடியரசுத் தலைவருக்குக் கட்டாயமாக்கியது; 44வது திருத்தம் 1978 ஆலோசனையை ஒருமுறை மறுபரிசீலனைக்கு அனுப்ப அதிகாரமளித்தது, ஆனால் மீண்டும் அனுப்பப்பட்ட ஆலோசனை கட்டாயமாகும்.",
            "TNPSC பொறி: குடியரசுத் தலைவர் பெயரளவு (De Jure) நிர்வாகி; பிரதமர் உண்மை (De Facto) நிர்வாகி. இந்திய நாடாளுமன்ற முறையில் குடியரசுத் தலைவர் அரசியலமைப்புத் தலைவராகச் செயல்படுகிறார், உண்மையான ஆட்சியாளர் அல்ல.",
            "2-வரி திருப்புதல்: உறுப்பு 53 ஒன்றிய நிர்வாக அதிகாரம் & இராணுவ உச்ச தளபதி அதிகாரத்தைக் குடியரசுத் தலைவரிடம் வழங்குகிறது. அதிகாரம் அமைச்சரவையின் கட்டாய ஆலோசனையின் பேரில் செலுத்தப்படுகிறது."
          ]
        }
      }
    ],
    "sec_electoral_college": [
      {
        "title": "1. Article 54: Electoral College Composition (வாக்காளர் குழு அமைப்பு)",
        "points": {
          "en": [
            "Meaning: Defines who votes in the election of the President of India.",
            "Constitutional Provision: Article 54 provides that the President shall be elected by the members of an Electoral College consisting of elected members of Lok Sabha, Rajya Sabha, and State Legislative Assemblies.",
            "Inclusion of UTs: The 70th Constitutional Amendment Act, 1992 (w.e.f. June 1, 1995) included the elected members of the Legislative Assemblies of the Union Territories of Delhi and Puducherry.",
            "WHO VOTES (Elected Only):\n1. Elected members of Lok Sabha (543 MPs)\n2. Elected members of Rajya Sabha (233 MPs)\n3. Elected members of State Legislative Assemblies (Vidhan Sabhas) of all States\n4. Elected members of Legislative Assemblies of Delhi and Puducherry",
            "WHO DOES NOT VOTE (Excluded):\n1. Nominated members of Lok Sabha & Rajya Sabha (12 nominated RS MPs)\n2. Nominated members of State Legislative Assemblies\n3. All members (elected & nominated) of State Legislative Councils (Vidhan Parishads)\n4. Nominated members of UT Assemblies",
            "Important Point: Legislative Councils (Vidhan Parishads) exist in 6 States (UP, Bihar, Maharashtra, Karnataka, Andhra Pradesh, Telangana). None of their members (elected or nominated) can vote in Presidential election!",
            "TNPSC Trap: Nominated MPs DO NOT vote in President's election (Art 54), BUT they DO vote in Vice-President's election (Art 66) AND President's impeachment (Art 61). State MLAs vote in President's election, BUT DO NOT vote in Vice-President's election or President's impeachment!",
            "2-Line Revision: Article 54 Electoral College consists of ELECTED members of LS, RS, State Assemblies & UT Assemblies (Delhi/Puducherry). Nominated MPs & Legislative Council members are excluded."
          ],
          "ta": [
            "பொருள்: இந்தியக் குடியரசுத் தலைவர் தேர்தலில் யார் வாக்களிக்கிறார்கள் என்பதை வரையறுக்கிறது.",
            "அரசியலமைப்பு விதி: உறுப்பு 54 மக்களவை, மாநிலங்களவை மற்றும் மாநிலச் சட்டமன்றங்களின் தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்களைக் கொண்ட வாக்காளர் குழுவால் குடியரசுத் தலைவர் தேர்ந்தெடுக்கப்படுவார் எனக் கூறுகிறது.",
            "யூனியன் பிரதேசங்கள் சேர்க்கை: 1992-ன் 70வது அரசியலமைப்பு திருத்தச் சட்டம் (அமலுக்கு வந்த நாள்: ஜூன் 1, 1995) டெல்லி மற்றும் புதுச்சேரி யூனியன் பிரதேச சட்டமன்றங்களின் தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்களைச் சேர்த்தது.",
            "யார் வாக்களிக்கிறார்கள் (தேர்ந்தெடுக்கப்பட்டவர்கள் மட்டுமே):\n1. மக்களவையின் தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்கள் (543 எம்பிக்கள்)\n2. மாநிலங்களவையின் தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்கள் (233 எம்பிக்கள்)\n3. அனைத்து மாநிலங்களின் சட்டமன்றங்களின் (விதான் சபா) தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்கள்\n4. டெல்லி மற்றும் புதுச்சேரி சட்டமன்றங்களின் தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்கள்",
            "யார் வாக்களிப்பதில்லை (விலக்கப்பட்டவர்கள்):\n1. மக்களவை & மாநிலங்களவையின் நியமன உறுப்பினர்கள் (12 மாநிலங்களவை நியமன எம்பிக்கள்)\n2. மாநிலச் சட்டமன்றங்களின் நியமன உறுப்பினர்கள்\n3. மாநிலச் சட்ட மேலவைகளின் (விதான் பரிஷத்) அனைத்து உறுப்பினர்களும் (தேர்ந்தெடுக்கப்பட்டவர்கள் & நியமனம் செய்யப்பட்டவர்கள்)\n4. யூனியன் பிரதேச சட்டமன்ற நியமன உறுப்பினர்கள்",
            "முக்கிய புள்ளி: 6 மாநிலங்களில் சட்ட மேலவைகள் (விதான் பரிஷத்) உள்ளன (உ.பி, பீகார், மகாராஷ்டிரா, கர்நாடகா, ஆந்திரா, தெலங்கானா). அவற்றின் எந்த உறுப்பினரும் குடியரசுத் தலைவர் தேர்தலில் வாக்களிக்க முடியாது!",
            "TNPSC பொறி: நியமன எம்பிக்கள் குடியரசுத் தலைவர் தேர்தலில் (உறுப்பு 54) வாக்களிக்க முடியாது, ஆனால் துணைத் தலைவர் தேர்தலிலும் (உறுப்பு 66) குடியரசுத் தலைவர் பதவி நீக்கத்திலும் (உறுப்பு 61) வாக்களிக்கலாம். மாநில எம்.எல்.ஏ-க்கள் குடியரசுத் தலைவர் தேர்தலில் வாக்களிக்கலாம், ஆனால் துணைத் தலைவர் தேர்தலிலோ பதவி நீக்கத்திலோ வாக்களிக்க முடியாது!",
            "2-வரி திருப்புதல்: உறுப்பு 54 வாக்காளர் குழு மக்களவை, மாநிலங்களவை, மாநில & யூனியன் பிரதேச (டெல்லி/புதுச்சேரி) தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்களைக் கொண்டுள்ளது. நியமன எம்பிக்கள் & சட்ட மேலவை உறுப்பினர்கள் விலக்கப்பட்டுள்ளனர்."
          ]
        }
      }
    ],
    "sec_value_of_votes": [
      {
        "title": "1. Article 55: Parity & Uniformity in Vote Values (வாக்கு மதிப்புகளில் சமநிலை & சீரான தன்மை)",
        "points": {
          "en": [
            "Meaning: Ensures uniform representation among different States and parity between States as a whole and the Union.",
            "Constitutional Provision: Article 55 mandates that as far as practicable, there shall be uniformity in the scale of representation of the different States at the election of the President.",
            "Two Core Principles:\n1. Uniformity among States: Value of vote of MLAs of different States varies according to state population so that every MLA represents a proportional population size.\n2. Parity between States & Union: Total vote value of all elected MLAs of all States combined equals the total vote value of all elected MPs of Parliament.",
            "MLA Vote Value Formula:\nValue of vote of an MLA = (Total population of the State / Total number of elected MLAs of the State) ÷ 1000\n[Or: Total Population / (Total elected MLAs × 1000)]",
            "Rounding Rule for MLA Vote Value: If after dividing by 1000, the remainder is 500 or more, the value of vote of each MLA is increased by 1.",
            "1971 Census Freeze: Under 84th CAA 2001 (originally 42nd CAA 1976), 'population' for calculating vote value means population as per 1971 Census until figures of first census after 2026 are published.",
            "MP Vote Value Formula:\nValue of vote of an MP = Total value of votes of all elected MLAs of all States / Total number of elected MPs of both Houses (LS + RS)",
            "Rounding Rule for MP Vote Value: If the fraction is greater than 0.5 (half), it is rounded off to the next higher whole number.",
            "TNPSC Trap: UP MLA vote value is highest (~208) because UP has largest population; Sikkim MLA vote value is lowest (~7). But ALL MPs have the EXACT SAME vote value (~700 / 708 depending on current assembly count).",
            "2-Line Revision: Article 55 mandates MLA vote value = (State Population / Elected MLAs) ÷ 1000 based on 1971 Census. MP vote value = Total MLA votes / Total elected MPs."
          ],
          "ta": [
            "பொருள்: பல்வேறு மாநிலங்களுக்கிடையே சீரான பிரதிநிதித்துவத்தையும், மாநிலங்கள் மற்றும் மத்திய அரசு இடையே சமநிலையையும் உறுதி செய்கிறது.",
            "அரசியலமைப்பு விதி: உறுப்பு 55 குடியரசுத் தலைவர் தேர்தலில் பல்வேறு மாநிலங்களின் பிரதிநிதித்துவ அளவில் முடிந்தவரை சீரான தன்மை இருக்க வேண்டும் எனக் கட்டாயப்படுத்துகிறது.",
            "இரண்டு முக்கிய தத்துவங்கள்:\n1. மாநிலங்களுக்கிடையே சீரான தன்மை: மாநில மக்கள் தொகைக்கேற்ப எம்.எல்.ஏ வாக்குகளின் மதிப்பு மாறுபடுவதால் ஒவ்வொரு எம்.எல்.ஏ-வும் விகிதாச்சார மக்கள் தொகையைப் பிரதிநிதித்துவப்படுத்துகிறார்.\n2. மாநிலங்கள் & மத்திய அரசு இடையே சமநிலை: அனைத்து மாநிலங்களின் தேர்ந்தெடுக்கப்பட்ட அனைத்து எம்.எல்.ஏ-க்களின் மொத்த வாக்கு மதிப்பும் நாடாளுமன்றத்தின் அனைத்து தேர்ந்தெடுக்கப்பட்ட எம்பிக்களின் மொத்த வாக்கு மதிப்பிற்குச் சமமாகும்.",
            "எம்.எல்.ஏ வாக்கு மதிப்பு சூத்திரம்:\nஒரு எம்.எல்.ஏ வாக்கின் மதிப்பு = (மாநிலத்தின் மொத்த மக்கள் தொகை / மாநிலத்தின் தேர்ந்தெடுக்கப்பட்ட மொத்த எம்.எல்.ஏ-க்கள்) ÷ 1000\n[அல்லது: மொத்த மக்கள் தொகை / (தேர்ந்தெடுக்கப்பட்ட எம்.எல்.ஏ-க்கள் × 1000)]",
            "எம்.எல்.ஏ வாக்கு மதிப்பு முழுமையாக்கல் விதி: 1000 ஆல் வகுத்த பிறகு மீதி 500 அல்லது அதற்கு மேல் இருந்தால், ஒவ்வொரு எம்.எல்.ஏ வாக்கின் மதிப்பும் 1 கூட்டப்படும்.",
            "1971 மக்கள் தொகை கணக்கெடுப்பு முடக்கம்: 84வது திருத்தம் 2001-ன் படி (முதலில் 42வது திருத்தம் 1976), வாக்கு மதிப்பைக் கணக்கிடுவதற்கான 'மக்கள் தொகை' என்பது 2026-க்குப் பிந்தைய முதல் மக்கள் தொகை கணக்கெடுப்பு வெளியாகும் வரை 1971 கணக்கெடுப்பின் படியே ஆகும்.",
            "எம்பி வாக்கு மதிப்பு சூத்திரம்:\nஒரு எம்பி வாக்கின் மதிப்பு = அனைத்து மாநிலங்களின் தேர்ந்தெடுக்கப்பட்ட அனைத்து எம்.எல்.ஏ-க்களின் மொத்த வாக்கு மதிப்பு / இரு அவைகளின் தேர்ந்தெடுக்கப்பட்ட மொத்த எம்பிக்கள் (மக்களவை + மாநிலங்களவை)",
            "எம்பி வாக்கு மதிப்பு முழுமையாக்கல் விதி: பின்னம் 0.5 (அரை) க்கு மேல் இருந்தால், அது அடுத்த உயர்ந்த முழு எண்ணாக முழுமையாக்கப்படும்.",
            "TNPSC பொறி: உ.பி எம்.எல்.ஏ வாக்கு மதிப்பு மிக அதிகம் (~208); சிக்கிம் எம்.எல்.ஏ வாக்கு மதிப்பு மிகக் குறைவு (~7). ஆனால் அனைத்து எம்பிக்களுக்கும் ஒரே துல்லியமான வாக்கு மதிப்பு உண்டு (~700 / 708).",
            "2-வரி திருப்புதல்: உறுப்பு 55 எம்.எல்.ஏ வாக்கு மதிப்பு = (மக்கள் தொகை / தேர்ந்தெடுக்கப்பட்ட எம்.எல்.ஏ-க்கள்) ÷ 1000 (1971 கணக்கெடுப்பு). எம்பி வாக்கு மதிப்பு = மொத்த எம்.எல்.ஏ வாக்குகள் / மொத்த தேர்ந்தெடுக்கப்பட்ட எம்பிக்கள்."
          ]
        }
      }
    ],
    "sec_method_of_election": [
      {
        "title": "1. Method of Voting & Electoral Quota (தேர்தல் முறை & தேர்தல் பங்கு)",
        "points": {
          "en": [
            "System: Article 55(3) mandates that Presidential election shall be held in accordance with the system of Proportional Representation by means of the Single Transferable Vote (STV).",
            "Ballot Type: Voting is by Secret Ballot. No political party can issue a whip to its members in Presidential election!",
            "Indirect Election: The President is NOT directly elected by the adult citizens of India, but indirectly by their elected representatives.",
            "Preference System: Each voter marks preferences on the ballot paper (1, 2, 3...) against candidate names.",
            "Electoral Quota Formula:\nElectoral Quota = [Total valid votes polled / (1 + 1)] + 1 = (Total valid votes polled / 2) + 1\nA candidate must secure MORE THAN 50% of total valid votes (Quota) to be declared elected.",
            "Counting Process: First-preference votes are counted first. If a candidate reaches Quota in 1st count, he is declared elected. If no candidate reaches Quota, the candidate with lowest 1st preference votes is eliminated, and his 2nd preference votes are transferred to remaining candidates. Process continues until a candidate reaches Quota.",
            "Historical Example: In 1969 election, V.V. Giri won on second preference counting against N. Sanjiva Reddy (only instance in Indian history).",
            "Election Disputes: Under Article 71, all doubts and disputes arising out of Presidential election are inquired into and decided EXCLUSIVELY by the Supreme Court of India, whose decision is final.",
            "TNPSC Trap: Election disputes of President CANNOT be challenged in High Courts or Election Commission. Supreme Court has EXCLUSIVE jurisdiction under Article 71.",
            "2-Line Revision: Presidential election uses Proportional Representation with STV and Secret Ballot. Candidate must secure Electoral Quota (>50%). Supreme Court decides disputes under Art 71."
          ],
          "ta": [
            "முறை: உறுப்பு 55(3) குடியரசுத் தலைவர் தேர்தல் ஒற்றை மாற்று வாக்கு மூலமான விகிதாச்சாரப் பிரதிநிதித்துவ முறையின் படி நடத்தப்பட வேண்டும் எனக் கட்டாயப்படுத்துகிறது.",
            "வாக்களிப்பு வகை: வாக்களிப்பு ரகசிய வாக்களிப்பு மூலம் நடைபெறுகிறது. குடியரசுத் தலைவர் தேர்தலில் எந்தக் அரசியல் கட்சியும் தனது உறுப்பினர்களுக்கு கொறடா (Whip) பிறப்பிக்க முடியாது!",
            "மறைமுகத் தேர்தல்: குடியரசுத் தலைவர் இந்திய வயதுவந்த குடிமக்களால் நேரடியாகத் தேர்ந்தெடுக்கப்படுவதில்லை, மாறாக அவர்களின் தேர்ந்தெடுக்கப்பட்ட பிரதிநிதிகள் மூலம் மறைமுகமாகத் தேர்ந்தெடுக்கப்படுகிறார்.",
            "விருப்ப முறை: ஒவ்வொரு வாக்காளரும் வேட்பாளர் பெயர்களுக்கு எதிராக வாக்குச் சீட்டில் விருப்பங்களை (1, 2, 3...) குறியிடுகின்றனர்.",
            "தேர்தல் பங்கு (Quota) சூத்திரம்:\nதேர்தல் பங்கு = [பதிவான மொத்த செல்லுபடியாகும் வாக்குகள் / (1 + 1)] + 1 = (மொத்த செல்லுபடியாகும் வாக்குகள் / 2) + 1\nவெற்றி பெற்றவராக அறிவிக்கப்பட ஒரு வேட்பாளர் மொத்த செல்லுபடியாகும் வாக்குகளில் 50%-க்கும் மேல் (தேர்தல் பங்கு) பெற வேண்டும்.",
            "எண்ணிக்கை முறை: முதல் விருப்ப வாக்குகள் முதலில் எண்ணப்படுகின்றன. 1வது எண்ணிக்கையில் தேர்தல் பங்கை எட்டினால் அவர் வெற்றி பெற்றவராக அறிவிக்கப்படுவார். எட்டவில்லை என்றால், குறைந்த வாக்குகள் பெற்றவர் நீக்கப்பட்டு அவரின் 2வது விருப்ப வாக்குகள் மற்றவர்களுக்கு மாற்றப்படும். பங்கு எட்டும் வரை இது தொடரும்.",
            "வரலாற்று உதாரணம்: 1969 தேர்தலில் என். சஞ்சீவ ரெட்டிக்கு எதிராக வி.வி. கிரி இரண்டாவது விருப்ப வாக்கு எண்ணிக்கையில் வெற்றி பெற்றார் (இந்திய வரலாற்றில் ஒரே நிகழ்வு).",
            "தேர்தல் தகராறுகள்: உறுப்பு 71-ன் கீழ் குடியரசுத் தலைவர் தேர்தல் தொடர்பான அனைத்து சந்தேகங்களும் தகராறுகளும் இந்திய உச்ச நீதிமன்றத்தால் மட்டுமே விசாரிக்கப்பட்டுத் தீர்மானிக்கப்படும் (தீர்ப்பு இறுதியானது).",
            "TNPSC பொறி: குடியரசுத் தலைவர் தேர்தல் தகராறுகளை உயர் நீதிமன்றங்களிலோ தேர்தல் ஆணையத்திலோ சவால் செய்ய முடியாது. உறுப்பு 71-ன் கீழ் உச்ச நீதிமன்றத்திற்கு மட்டுமே பிரத்யேக அதிகார வரம்பு உண்டு.",
            "2-வரி திருப்புதல்: குடியரசுத் தலைவர் தேர்தல் STV & ரகசிய வாக்களிப்புடன் கூடிய விகிதாச்சாரப் பிரதிநிதித்துவத்தைப் பயன்படுத்துகிறது. வேட்பாளர் தேர்தல் பங்கை (>50%) பெற வேண்டும். உறுப்பு 71-ன் கீழ் உச்ச நீதிமன்றம் தகராறுகளைத் தீர்மானிக்கிறது."
          ]
        }
      }
    ],
    "sec_qualifications": [
      {
        "title": "1. Article 58: Qualifications for Office (பதவிக்கான தகுதிகள்)",
        "points": {
          "en": [
            "Meaning: Sets out constitutional requirements to contest for the post of President of India.",
            "Constitutional Provision: Under Article 58(1), a person is eligible for election as President ONLY if he:\n1. Is a citizen of India\n2. Has completed 35 years of age\n3. Is qualified for election as a member of the Lok Sabha\n4. Does not hold any office of profit under Union, State, or local/public authority.",
            "Citizen Rule: In India, BOTH a citizen by birth AND a naturalised citizen are eligible for President. (Contrast with USA where ONLY a natural-born citizen can become President!).",
            "Age Requirement: Minimum age is 35 years. There is NO upper age limit in the Constitution!",
            "House Qualification: Must be qualified to become a Lok Sabha MP (NOT Rajya Sabha MP). (Contrast with Vice-President who must be qualified for Rajya Sabha!).",
            "Office of Profit Exceptions: Under Article 58(2), the following sitting post-holders are NOT deemed to hold an office of profit and CAN contest without resigning prior:\n- Sitting President of India\n- Sitting Vice-President of India\n- Sitting Governor of any State\n- Minister for the Union or any State",
            "Nomination Conditions: Nomination paper must be subscribed by at least 50 proposers and 50 seconders (among Electoral College members). Security deposit is ₹15,000 in Reserve Bank of India (forfeited if candidate gets less than 1/6th of valid votes).",
            "TNPSC Trap: President candidate must be qualified for Lok Sabha membership, NOT Rajya Sabha. Age limit is 35 years, NOT 25 or 30 years. Naturalised citizens CAN become President in India.",
            "2-Line Revision: Article 58 requires: Citizen of India, 35 years of age, Lok Sabha qualification, no office of profit. Requires 50 proposers & 50 seconders."
          ],
          "ta": [
            "பொருள்: இந்தியக் குடியரசுத் தலைவர் பதவிக்குப் போட்டியிடுவதற்கான அரசியலமைப்புத் தேவைகளை அமைக்கிறது.",
            "அரசியலமைப்பு விதி: உறுப்பு 58(1)-ன் கீழ் ஒருவர் குடியரசுத் தலைவராகத் தேர்ந்தெடுக்கப்பட பின்வரும் தகுதிகளைக் கொண்டிருக்க வேண்டும்:\n1. இந்தியக் குடிமகனாக இருக்க வேண்டும்\n2. 35 வயதைப் பூர்த்தி செய்திருக்க வேண்டும்\n3. மக்களவை உறுப்பினராகத் தேர்ந்தெடுக்கப்படும் தகுதி பெற்றிருக்க வேண்டும்\n4. மத்திய, மாநில அல்லது உள்ளாட்சி/பொது அதிகார அமைப்பின் கீழ் எவ்வித ஆதாயம் தரும் பதவியையும் வகிக்கக் கூடாது.",
            "குடியுரிமை விதி: இந்தியாவில் பிறப்பால் குடிமகனானவர் மற்றும் இயல்புரிமை பெற்ற குடிமகன் இருவருமே குடியரசுத் தலைவராகலாம். (அமெரிக்காவில் பிறப்பால் குடிமகன் மட்டுமே அதிபராக முடியும்!).",
            "வயதுத் தேவை: குறைந்தபட்ச வயது 35 ஆண்டுகள். அரசியலமைப்பில் உச்ச வயது வரம்பு இல்லை!",
            "அவை தகுதி: மக்களவை எம்பியாகும் தகுதி இருக்க வேண்டும் (மாநிலங்களவை அல்ல). (துணைத் தலைவருக்கு மாநிலங்களவை தகுதி தேவை!).",
            "ஆதாயம் தரும் பதவி விலக்குகள்: உறுப்பு 58(2)-ன் கீழ் பின்வரும் பதவிகளில் உள்ளவர்கள் ஆதாயம் தரும் பதவியாகக் கருதப்பட மாட்டார்கள், எனவே பதவியை ராஜினாமா செய்யாமல் போட்டியிடலாம்:\n- பதவியில் உள்ள இந்தியக் குடியரசுத் தலைவர்\n- பதவியில் உள்ள இந்தியத் துணைத் தலைவர்\n- பதவியில் உள்ள மாநில ஆளுநர்\n- மத்திய அல்லது மாநில அமைச்சர்",
            "வேட்புமனு நிபந்தனைகள்: வேட்புமனுவை வாக்காளர் குழு உறுப்பினர்களில் குறைந்தபட்சம் 50 முன்மொழிபவர்களும் 50 வழிமொழிபவர்களும் கையொப்பமிட வேண்டும். பிணைத்தொகை ரிசர்வ் வங்கியில் ₹15,000 (செல்லுபடியாகும் వాக்குகளில் 1/6 பங்கு பெறாவிட்டால் பிணைத்தொகை பறிமுதல் செய்யப்படும்).",
            "TNPSC பொறி: குடியரசுத் தலைவர் வேட்பாளர் மக்களவை தகுதி பெற வேண்டும், மாநிலங்களவை அல்ல. வயது வரம்பு 35 ஆண்டுகள், 25 அல்லது 30 அல்ல. இந்தியாவில் இயல்புரிமை குடிமகனும் குடியரசுத் தலைவராகலாம்.",
            "2-வரி திருப்புதல்: உறுப்பு 58 தகுதிகள்: இந்தியக் குடிமகன், 35 வயது, மக்களவை தகுதி, ஆதாயம் தரும் பதவி இன்மை. 50 முன்மொழிபவர்கள் & 50 வழிமொழிபவர்கள் தேவை."
          ]
        }
      }
    ],
    "sec_conditions_of_office": [
      {
        "title": "1. Article 59: Conditions of President's Office (அலுவலக நிபந்தனைகள்)",
        "points": {
          "en": [
            "Meaning: Lays down constitutional conditions and immunities during the President's tenure.",
            "Constitutional Provision: Under Article 59:\n1. Non-Membership: President shall NOT be a member of either House of Parliament or of a House of State Legislature. If an elected member is elected President, he is deemed to have vacated his seat in that House on the date he enters upon office.\n2. No Office of Profit: President shall not hold any other office of profit.\n3. Official Residence: Entitled without payment of rent to the use of official residence (Rashtrapati Bhavan, New Delhi; Retreat Building, Shimla; Rashtrapati Nilayam, Hyderabad).\n4. Emoluments & Allowances: Entitled to emoluments, allowances, and privileges determined by Parliament by law.\n5. Non-Diminution Protection: Emoluments and allowances of the President CANNOT be diminished during his term of office.",
            "Personal Immunities: Under Article 361, President enjoys personal immunity from legal proceedings during tenure. Cannot be arrested or imprisoned. Civil proceedings can be instituted only after giving 2 months' written notice.",
            "TNPSC Trap: Emoluments cannot be reduced even during a Financial Emergency under Article 360! (Salary of judges can be reduced in Financial Emergency, but President's emoluments cannot).",
            "2-Line Revision: Article 59 mandates non-membership of Parliament/Legislature, rent-free Rashtrapati Bhavan, and protection against reduction of emoluments during term."
          ],
          "ta": [
            "பொருள்: குடியரசுத் தலைவரின் பதவிக்காலத்தில் அரசியலமைப்பு நிபந்தனைகள் மற்றும் விலக்குகளை அமைக்கிறது.",
            "அரசியலமைப்பு விதி: உறுப்பு 59-ன் கீழ்:\n1. உறுப்பினர் அல்லாத நிலை: குடியரசுத் தலைவர் நாடாளுமன்றத்தின் எந்த அவையிலும் மாநில சட்டமன்றத்திலும் உறுப்பினராக இருக்கக் கூடாது. தேர்ந்தெடுக்கப்பட்ட உறுப்பினர் குடியரசுத் தலைவராகத் தேர்ந்தெடுக்கப்பட்டால், அவர் அலுவலகத்தில் நுழையும் தேதியில் அவ்அவை சீட்டை காலி செய்ததாகக் கருதப்படுவார்.\n2. ஆதாயம் தரும் பதவி இன்மை: வேறு எந்த ஆதாயம் தரும் பதவியையும் வகிக்கக் கூடாது.\n3. அதிகாரப்பூர்வ இல்லம்: வாடகை இன்றி அதிகாரப்பூர்வ இல்லத்தைப் பயன்படுத்த உரிமையுடையவர் (ராஷ்டிரபதி பவன், புதுடெல்லி; ரிட்ரீட் கட்டிடம், சிம்லா; ராஷ்டிரபதி நிலயம், ஹைதராபாத்).\n4. ஊதியம் & படிகள்: நாடாளுமன்றச் சட்டத்தால் தீர்மானிக்கப்படும் ஊதியம், படிகள் மற்றும் சலுகைகளுக்கு உரிமையுடையவர்.\n5. குறைக்காப் பாதுகாப்பு: குடியரசுத் தலைவரின் ஊதியமும் படிகளும் அவரது பதவிக்காலத்தில் குறைக்கப்பட முடியாது.",
            "தனிப்பட்ட விலக்குகள்: உறுப்பு 361-ன் கீழ் பதவிக்காலத்தில் சட்ட நடவடிக்கைகளிலிருந்து தனிப்பட்ட விலக்கு பெறுகிறார். கைது செய்யவோ சிறையில் அடைக்கவோ முடியாது. 2 மாத எழுத்துப்பூர்வ அறிவிப்புக்குப் பிறகே உரிமையியல் நடவடிக்கை எடுக்க முடியும்.",
            "TNPSC பொறி: உறுப்பு 360 நிதி அவசரநிலையின் போது கூட ஊதியத்தைக் குறைக்க முடியாது! (நிதி அவசரநிலையில் நீதிபதிகளின் சம்பளத்தைக் குறைக்கலாம், ஆனால் குடியரசுத் தலைவரின் ஊதியத்தைக் குறைக்க முடியாது).",
            "2-வரி திருப்புதல்: உறுப்பு 59 நாடாளுமன்ற/சட்டமன்ற உறுப்பினர் அல்லாத நிலை, வாடகையில்லா ராஷ்டிரபதி பவன் மற்றும் பதவிக்காலத்தில் ஊதியத்தைக் குறைக்க முடியாத பாதுகாப்பை கட்டாயப்படுத்துகிறது."
          ]
        }
      }
    ],
    "sec_oath_affirmation": [
      {
        "title": "1. Article 60: Oath or Affirmation by the President (குடியரசுத் தலைவரின் உறுதிமொழி)",
        "points": {
          "en": [
            "Meaning: Prescribes the exact text and administering authority for the President's oath of office.",
            "Constitutional Provision: Article 60 mandates that every President before entering upon office shall make and subscribe an oath or affirmation in the presence of the Chief Justice of India (CJI), or in his absence, the senior-most Judge of the Supreme Court available.",
            "Administering Authority: Chief Justice of India (CJI). If CJI is absent, the senior-most available Supreme Court Judge administers the oath.",
            "Core Words of Oath:\nTo faithfully execute the office of President of India, AND to the best of ability 'PRESERVE, PROTECT AND DEFEND THE CONSTITUTION AND THE LAW', AND devote to the service and well-being of the people of India.",
            "Unique Constitutional Purpose: President is the ONLY constitutional functionary who takes a specific oath to 'preserve, protect and defend the Constitution'.",
            "Comparison of Oaths:\n- President (Art 60): Preserve, protect and defend the Constitution.\n- Governors (Art 159): Preserve, protect and defend the Constitution.\n- Ministers / MPs / Judges (3rd Schedule): Bear true faith and allegiance to the Constitution.",
            "TNPSC Trap: President's oath is NOT in the Third Schedule! It is specified directly in Article 60. (Vice-President Art 69 and Governor Art 159 are also NOT in Third Schedule).",
            "2-Line Revision: Article 60 oath is administered by CJI (or senior-most SC Judge). Text promises to 'preserve, protect and defend the Constitution'. Oath is in Art 60, NOT 3rd Schedule."
          ],
          "ta": [
            "பொருள்: குடியரசுத் தலைவர் பதவிப் பிரமாணத்திற்கான துல்லியமான உரை மற்றும் பிரமாணம் செய்து வைக்கும் அதிகார அமைப்பை விவரிக்கிறது.",
            "அரசியலமைப்பு விதி: உறுப்பு 60 ஒவ்வொரு குடியரசுத் தலைவரும் பொறுப்பேற்பதற்கு முன் இந்தியத் தலைமை நீதிபதி (CJI) அல்லது அவர் இல்லாத போது உச்ச நீதிமன்றத்தின் மூத்த நீதிபதி முன்னிலையில் உறுதிமொழி ஏற்க வேண்டும் எனக் கட்டாயப்படுத்துகிறது.",
            "பிரமாணம் செய்து வைப்பவர்: இந்தியத் தலைமை நீதிபதி (CJI). CJI இல்லாத போது உச்ச நீதிமன்றத்தின் கிடைக்கக்கூடிய மிக மூத்த நீதிபதி பிரமாணம் செய்து வைப்பார்.",
            "உறுதிமொழியின் முக்கிய சொற்கள்:\nகுடியரசுத் தலைவர் பதவியை உண்மையுடன் வகிக்கவும், தனது திறனுக்கு ஏற்ப 'அரசியலமைப்பையும் சட்டத்தையும் பேணவும், பாதுகாக்கவும், தற்காக்கவும்', மற்றும் இந்திய மக்களின் சேவை மற்றும் நலனுக்குத் தன்னை அர்ப்பணிக்கவும் உறுதி ஏற்கிறார்.",
            "தனித்துவமான அரசியலமைப்பு நோக்கம்: 'அரசியலமைப்பைப் பேணவும், பாதுகாக்கவும், தற்காக்கவும்' என்ற குறிப்பிட்ட உறுதிமொழியை ஏற்கும் ஒரே அரசியலமைப்புப் பொறுப்பாளர் குடியரசுத் தலைவர் (மற்றும் ஆளுநர்) மட்டுமே.",
            "உறுதிமொழிகளின் ஒப்பீடு:\n- குடியரசுத் தலைவர் (உறுப்பு 60): அரசியலமைப்பைப் பேணவும், பாதுகாக்கவும், தற்காக்கவும்.\n- ஆளுநர்கள் (உறுப்பு 159): அரசியலமைப்பைப் பேணவும், பாதுகாக்கவும், தற்காக்கவும்.\n- அமைச்சர்கள் / எம்பிக்கள் / நீதிபதிகள் (3வது அட்டவணை): அரசியலமைப்பின் மீது உண்மையான நம்பிக்கையும் விசுவாசமும் கொள்ளுதல்.",
            "TNPSC பொறி: குடியரசுத் தலைவரின் உறுதிமொழி 3வது அட்டவணையில் இல்லை! அது நேரடியாக உறுப்பு 60-ல் குறிப்பிடப்பட்டுள்ளது. (துணைத் தலைவர் உறுப்பு 69 & ஆளுநர் உறுப்பு 159 ஆகியவையும் 3வது அட்டவணையில் இல்லை).",
            "2-வரி திருப்புதல்: உறுப்பு 60 உறுதிமொழி CJI (அல்லது மூத்த உச்ச நீதிமன்ற நீதிபதி) ஆல் பிரமாணம் செய்து வைக்கப்படுகிறது. உரை 'அரசியலமைப்பைப் பேணவும், பாதுகாக்கவும், தற்காக்கவும்' என வாக்குறுதியளிக்கிறது. உறுதிமொழி உறுப்பு 60-ல் உள்ளது, 3வது அட்டவணையில் இல்லை."
          ]
        }
      }
    ],
    "sec_term_resignation_re-election": [
      {
        "title": "1. Articles 56 & 57: Term, Resignation & Re-election (பதவிக்காலம், ராஜினாமா & மறுதேர்தல்)",
        "points": {
          "en": [
            "Term of Office: Under Article 56(1), President holds office for a term of 5 YEARS from the date on which he enters upon his office.",
            "Resignation: President may resign at any time by writing under his hand addressed to the Vice-President of India.",
            "Communication of Resignation: Under Article 56(2), any resignation addressed to the Vice-President shall forthwith be communicated by him to the Speaker of the Lok Sabha.",
            "Holding Over: President continues to hold office, notwithstanding the expiration of his term, until his successor enters upon office. (Prevents interregnum).",
            "Re-election (Article 57): Under Article 57, a person who holds or has held office as President is eligible for re-election to that office for ANY number of terms.",
            "No Constitutional Cap: Unlike USA (22nd Amendment limits US President to maximum 2 terms), Indian Constitution puts NO limit on re-election terms!",
            "Historical Fact: Dr. Rajendra Prasad is the ONLY President of India to have served two full terms in office (1950–1962).",
            "TNPSC Trap: Resignation letter is addressed to Vice-President, NOT to Chief Justice of India or Prime Minister! Vice-President must inform Speaker of Lok Sabha immediately.",
            "2-Line Revision: Article 56 term is 5 years. Resignation addressed to Vice-President (communicated to LS Speaker). Article 57 allows unlimited re-election."
          ],
          "ta": [
            "பதவிக்காலம்: உறுப்பு 56(1)-ன் கீழ் குடியரசுத் தலைவர் அலுவலகத்தில் நுழையும் தேதியிலிருந்து 5 ஆண்டுகள் பதவிக் காலம் வகிப்பார்.",
            "ராஜினாமா: இந்தியத் துணைத் தலைவருக்குத் தன் கையொப்பமிட்ட கடிதம் மூலம் எப்போது வேண்டுமானாலும் ராஜினாமா செய்யலாம்.",
            "ராஜினாமா அறிவிப்பு: உறுப்பு 56(2)-ன் கீழ் துணைத் தலைவருக்கு அனுப்பப்படும் எந்தவொரு ராஜினாமா கடிதமும் அவரால் உடனடியாக மக்களவை சபாநாயகருக்குத் தெரிவிக்கப்பட வேண்டும்.",
            "பதவி நீடிப்பு: பதவிக்காலம் முடிந்த போதிலும், புதியவர் பொறுப்பேற்கும் வரை குடியரசுத் தலைவர் பதவியில் தொடர்வார் (காலியிடத்தைத் தவிர்க்கிறது).",
            "மறுதேர்தல் (உறுப்பு 57): உறுப்பு 57-ன் கீழ் குடியரசுத் தலைவராக உள்ளவர் அல்லது இருந்தவர் எத்தனை முறை வேண்டுமானாலும் மீண்டும் தேர்ந்தெடுக்கப்படத் தகுதியுடையவர்.",
            "அரசியலமைப்பு வரம்பின்மை: அமெரிக்காவைப் போலன்றி (22வது திருத்தம் அமெரிக்க அதிபரை அதிகபட்சம் 2 தவணைகளுக்குக் கட்டுப்படுத்துகிறது), இந்திய அரசியலமைப்பு மறுதேர்தல் தவணைகளுக்கு வரம்பு விதிக்கவில்லை!",
            "வரலாற்று உண்மை: டாக்டர் ராஜேந்திர பிரசாத் மட்டுமே இரண்டு முழு தவணைகளுக்குக் குடியரசுத் தலைவராகப் பணியாற்றிய ஒரே இந்தியக் குடியரசுத் தலைவர் (1950–1962).",
            "TNPSC பொறி: ராஜினாமா கடிதம் துணைத் தலைவருக்கு முகவரியிடப்பட வேண்டும், தலைமை நீதிபதிக்கோ பிரதமர்க்கோ அல்ல! துணைத் தலைவர் உடனடியாக மக்களவை சபாநாயகருக்குத் தெரிவிக்க வேண்டும்.",
            "2-வரி திருப்புதல்: உறுப்பு 56 பதவிக்காலம் 5 ஆண்டுகள். ராஜினாமா துணைத் தலைவருக்கு முகவரியிடப்படும் (மக்களவை சபாநாயகருக்குத் தெரிவிக்கப்படும்). உறுப்பு 57 வரம்பற்ற மறுதேர்தலை அனுமதிக்கிறது."
          ]
        }
      }
    ],
    "sec_vacancy_impeachment": [
      {
        "title": "1. Articles 62 & 61: Vacancy & Impeachment Foundation (காலியிடம் & பதவி நீக்க அடிப்படை)",
        "points": {
          "en": [
            "Causes of Vacancy (Article 62):\n1. Expiry of 5-year tenure\n2. Resignation\n3. Removal by impeachment\n4. Death\n5. Election declared void by Supreme Court under Article 71.",
            "Expiry Rule: Election to fill vacancy caused by expiry of term MUST be completed BEFORE the expiration of the term.",
            "Casual Vacancy Rule: Election to fill vacancy occurring due to death, resignation, removal or otherwise must be held within 6 MONTHS from date of vacancy. Newly elected President holds office for a FULL 5-year term!",
            "Acting President Mechanism: When vacancy occurs due to death/resignation/removal, Vice-President acts as President until new President is elected. If VP unavailable, CJI acts; if CJI unavailable, senior-most SC Judge acts.",
            "1969 Acting President Instance: When President Dr. Zakir Hussain died in May 1969, VP V.V. Giri acted as President. Giri resigned to contest election; then CJI M. Hidayatullah acted as President.",
            "Impeachment Foundation (Article 61):\n- Sole Ground: 'Violation of the Constitution' (phrase not defined in Constitution).\n- Quasi-Judicial Process: Initiated in EITHER House of Parliament.\n- 1/4th Notice: Charge resolution signed by at least 1/4th total members of initiating House + 14 days' written notice given to President.\n- 2/3rd Total Majority: Resolution must be passed by 2/3rd majority of TOTAL MEMBERSHIP of initiating House.\n- Investigation & 2nd House: Other House investigates charge; President has right to appear & be represented. Passed by 2/3rd majority of TOTAL MEMBERSHIP of 2nd House.\n- Voting Distinction: Nominated MPs VOTE in impeachment, but State MLAs DO NOT vote in impeachment!",
            "TNPSC Trap: Impeachment majority is 2/3rd of TOTAL MEMBERSHIP of the House (NOT present & voting!). No President has ever been impeached in India.",
            "2-Line Revision: Vacancy election held within 6 months (new President gets full 5 yrs). Article 61 impeachment ground is 'Violation of Constitution'; requires 14 days notice & 2/3rd total membership majority."
          ],
          "ta": [
            "காலியிடத்திற்கான காரணங்கள் (உறுப்பு 62):\n1. 5 ஆண்டு பதவிக்காலம் முடிவடைதல்\n2. ராஜினாமா\n3. பதவி நீக்கம்\n4. மரணம்\n5. உறுப்பு 71-ன் கீழ் உச்ச நீதிமன்றத்தால் தேர்தல் செல்லாது என அறிவிக்கப்படுதல்.",
            "பதவிக்கால முடிவு விதி: பதவிக்கால முடிவால் ஏற்படும் காலியிடத்தை நிரப்புவதற்கான தேர்தல் பதவிக்காலம் முடிவடைவதற்கு முன்பே முடிக்கப்பட வேண்டும்.",
            "தற்செயல் காலியிட விதி: மரணம், ராஜினாமா, பதவி நீக்கத்தால் ஏற்படும் காலியிடத்திற்கான தேர்தல் காலியிடம் ஏற்பட்ட தேதியிலிருந்து 6 மாதங்களுக்குள் நடத்தப்பட வேண்டும். புதிதாகத் தேர்ந்தெடுக்கப்படும் குடியரசுத் தலைவர் முழு 5 ஆண்டு பதவிக்காலத்தைப் பெறுவார்!",
            "செயல் குடியரசுத் தலைவர் முறை: மரணம்/ராஜினாமா/பதவி நீக்கத்தால் காலியிடம் ஏற்படும் போது புதியவர் தேர்ந்தெடுக்கப்படும் வரை துணைத் தலைவர் செயல் குடியரசுத் தலைவராகச் செயல்படுவார். துணைத் தலைவர் இல்லையெனில் CJI; CJI இல்லையெனில் மூத்த உச்ச நீதிமன்ற நீதிபதி செயல்படுவார்.",
            "1969 செயல் குடியரசுத் தலைவர் நிகழ்வு: மே 1969-ல் குடியரசுத் தலைவர் டாக்டர் ஜாகீர் உசேன் மறைந்த போது துணைத் தலைவர் வி.வி. கிரி செயல் குடியரசுத் தலைவரானார். கிரி போட்டியிட ராஜினாமா செய்ததால் CJI எம். இதாயத்துல்லா செயல் குடியரசுத் தலைவராகச் செயல்பட்டார்.",
            "பதவி நீக்க அடிப்படை (உறுப்பு 61):\n- ஒரே காரணம்: 'அரசியலமைப்பு மீறல்' (சொற்றொடர் அரசியலமைப்பில் வரையறுக்கப்படவில்லை).\n- பகுதி-நீதிமன்ற முறை: நாடாளுமன்றத்தின் எந்த அவையிலும் தொடங்கப்படலாம்.\n- 1/4 பங்கு அறிவிப்பு: தீர்மானம் தொடங்கும் அவையின் குறைந்தபட்சம் 1/4 பங்கு மொத்த உறுப்பினர்களால் கையொப்பமிடப்பட வேண்டும் + 14 நாட்கள் எழுத்துப்பூர்வ அறிவிப்பு குடியரசுத் தலைவருக்கு வழங்கப்பட வேண்டும்.\n- 2/3 பங்கு மொத்த பெரும்பான்மை: தொடங்கும் அவையின் மொத்த உறுப்பினர்களில் 2/3 பங்கு பெரும்பான்மையால் தீர்மானம் நிறைவேற்றப்பட வேண்டும்.\n- விசாரணை & 2வது அவை: மற்ற அவை குற்றச்சாட்டை விசாரிக்கும்; குடியரசுத் தலைவருக்கு முன்னிலையாகவும் பிரதிநிதித்துவப்படுத்தவும் உரிமை உண்டு. 2வது அவையின் மொத்த உறுப்பினர்களில் 2/3 பங்கு பெரும்பான்மையால் நிறைவேற்றப்படும்.\n- வாக்களிப்பு வேறுபாடு: நியமன எம்பிக்கள் பதவி நீக்கத்தில் வாக்களிக்கலாம், ஆனால் மாநில எம்.எல்.ஏ-க்கள் பதவி நீக்கத்தில் வாக்களிக்க முடியாது!",
            "TNPSC பொறி: பதவி நீக்க பெரும்பான்மை அவையின் மொத்த உறுப்பினர்களில் 2/3 பங்கு ஆகும் (வந்திருந்து வாக்களிப்பவர்களில் அல்ல!). இந்தியாவில் இதுவரை எந்தக் குடியரசுத் தலைவரும் பதவி நீக்கம் செய்யப்பட்டதில்லை.",
            "2-வரி திருப்புதல்: தற்செயல் காலியிடத் தேர்தல் 6 மாதங்களுக்குள் நடத்தப்படும் (புதியவர் முழு 5 ஆண்டுகள் பெறுவார்). உறுப்பு 61 பதவி நீக்கக் காரணம் 'அரசியலமைப்பு மீறல்'; 14 நாட்கள் அறிவிப்பு & 2/3 பங்கு மொத்த உறுப்பினர் பெரும்பான்மை தேவை."
          ]
        }
      }
    ],
    "comparison_tables": [
      {
        "id": "tbl_pres_vs_vp",
        "title_en": "1. President vs Vice-President (Constitutional Comparison)",
        "title_ta": "1. குடியரசுத் தலைவர் vs துணைத் தலைவர் (அரசியலமைப்பு ஒப்பீடு)",
        "headers_en": ["Dimension", "President of India", "Vice-President of India"],
        "headers_ta": ["பரிமாணம்", "இந்தியக் குடியரசுத் தலைவர்", "இந்தியத் துணைத் தலைவர்"],
        "rows_en": [
          ["Constitutional Role", "Head of State & Union Executive (Art 52)", "Ex-officio Chairman of Rajya Sabha (Art 64)"],
          ["Electoral College", "Elected MPs + Elected MLAs (States & UTs)", "Elected MPs + Nominated MPs (NO MLAs)"],
          ["House Qualification", "Must be qualified for Lok Sabha (Art 58)", "Must be qualified for Rajya Sabha (Art 66)"],
          ["Removal / Impeachment", "Impeached for 'Violation of Constitution' by 2/3rd total majority in both Houses (Art 61)", "Removed by Effective Majority in RS + Agreed by LS (Art 67)"],
          ["Oath Text", "Preserve, protect and defend the Constitution (Art 60)", "Bear true faith and allegiance to Constitution (Art 69)"]
        ],
        "rows_ta": [
          ["அரசியலமைப்புப் பங்கு", "நாட்டின் தலைவர் & ஒன்றிய நிர்வாகி (உறுப்பு 52)", "மாநிலங்களவையின் பதவிவழித் தலைவர் (உறுப்பு 64)"],
          ["வாக்காளர் குழு", "தேர்ந்தெடுக்கப்பட்ட எம்பிக்கள் + தேர்ந்தெடுக்கப்பட்ட எம்.எல்.ஏ-க்கள்", "தேர்ந்தெடுக்கப்பட்ட எம்பிக்கள் + நியமன எம்பிக்கள் (எம்.எல்.ஏ-க்கள் இல்லை)"],
          ["அவை தகுதி", "மக்களவை தகுதி பெற வேண்டும் (உறுப்பு 58)", "மாநிலங்களவை தகுதி பெற வேண்டும் (உறுப்பு 66)"],
          ["பதவி நீக்கம்", "இரு அவைகளிலும் 2/3 பங்கு மொத்த பெரும்பான்மையால் 'அரசியலமைப்பு மீறலுக்காக' நீக்கம் (உறுப்பு 61)", "மாநிலங்களவையில் பயனுள்ள பெரும்பான்மை + மக்களவை ஒப்புதலால் நீக்கம் (உறுப்பு 67)"],
          ["உறுதிமொழி உரை", "அரசியலமைப்பைப் பேணவும், பாதுகாக்கவும், தற்காக்கவும் (உறுப்பு 60)", "அரசியலமைப்பின் மீது உண்மையான நம்பிக்கையும் விசுவாசமும் கொள்ளுதல் (உறுப்பு 69)"]
        ]
      },
      {
        "id": "tbl_pres_vs_pm",
        "title_en": "2. President vs Prime Minister (Executive Powers)",
        "title_ta": "2. குடியரசுத் தலைவர் vs பிரதமர் (நிர்வாக அதிகாரங்கள்)",
        "headers_en": ["Dimension", "President of India", "Prime Minister of India"],
        "headers_ta": ["பரிமாணம்", "இந்தியக் குடியரசுத் தலைவர்", "இந்தியப் பிரதமர்"],
        "rows_en": [
          ["Executive Status", "Nominal / De Jure Executive Head", "Real / De Facto Executive Head"],
          ["Government Status", "Head of the State", "Head of the Government"],
          ["Constitutional Source", "Article 52 & Article 53", "Article 74 & Article 75"],
          ["Advice Bindingness", "Bound by Cabinet advice under Art 74(1)", "Heads the Cabinet that gives binding advice"],
          ["Election Method", "Indirectly elected by Electoral College", "Appointed by President as majority leader in LS"]
        ],
        "rows_ta": [
          ["நிர்வாக நிலை", "பெயரளவு / De Jure நிர்வாகத் தலைவர்", "உண்மை / De Facto நிர்வாகத் தலைவர்"],
          ["அரசாங்க நிலை", "நாட்டின் தலைவர் (Head of State)", "அரசாங்கத்தின் தலைவர் (Head of Government)"],
          ["அரசியலமைப்பு மூலாதாரம்", "உறுப்பு 52 & உறுப்பு 53", "உறுப்பு 74 & உறுப்பு 75"],
          ["ஆலோசனைப் பிணைப்பு", "உறுப்பு 74(1)-ன் கீழ் அமைச்சரவை ஆலோசனைக்குக் கட்டுப்பட்டவர்", "கட்டாய ஆலோசனை வழங்கும் அமைச்சரவைக்குத் தலைமை தாங்குபவர்"],
          ["தேர்தல் முறை", "வாக்காளர் குழுவால் மறைமுகமாகத் தேர்ந்தெடுக்கப்படுபவர்", "மக்களவை பெரும்பான்மை தலைவராகக் குடியரசுத் தலைவரால் நியமிக்கப்படுபவர்"]
        ]
      },
      {
        "id": "tbl_pres_ec_vs_vp_ec",
        "title_en": "3. President's Electoral College vs Vice-President's Electoral College",
        "title_ta": "3. குடியரசுத் தலைவர் வாக்காளர் குழு vs துணைத் தலைவர் வாக்காளர் குழு",
        "headers_en": ["Feature", "President's Electoral College (Art 54)", "Vice-President's Electoral College (Art 66)"],
        "headers_ta": ["அம்சம்", "குடியரசுத் தலைவர் வாக்காளர் குழு (உறுப்பு 54)", "துணைத் தலைவர் வாக்காளர் குழு (உறுப்பு 66)"],
        "rows_en": [
          ["Parliament MPs", "Elected MPs ONLY (LS + RS)", "BOTH Elected and Nominated MPs (LS + RS)"],
          ["Nominated MPs", "EXCLUDED (Cannot vote)", "INCLUDED (Can vote)"],
          ["State Assembly MLAs", "INCLUDED (Elected MLAs of all States)", "EXCLUDED (State MLAs cannot vote)"],
          ["UT Assembly MLAs", "INCLUDED (Elected MLAs of Delhi & Puducherry)", "EXCLUDED (UT MLAs cannot vote)"],
          ["Legislative Councils", "EXCLUDED (No MLC can vote)", "EXCLUDED (No MLC can vote)"]
        ],
        "rows_ta": [
          ["நாடாளுமன்ற எம்பிக்கள்", "தேர்ந்தெடுக்கப்பட்ட எம்பிக்கள் மட்டுமே (மக்களவை + மாநிலங்களவை)", "தேர்ந்தெடுக்கப்பட்ட மற்றும் நியமன எம்பிக்கள் இருவருமே"],
          ["நியமன எம்பிக்கள்", "விலக்கப்பட்டவர்கள் (வாக்களிக்க முடியாது)", "சேர்க்கப்பட்டவர்கள் (வாக்களிக்கலாம்)"],
          ["மாநில எம்.எல்.ஏ-க்கள்", "சேர்க்கப்பட்டவர்கள் (அனைத்து மாநிலங்களின் தேர்ந்தெடுக்கப்பட்ட எம்.எல்.ஏ-க்கள்)", "விலக்கப்பட்டவர்கள் (மாநில எம்.எல்.ஏ-க்கள் வாக்களிக்க முடியாது)"],
          ["யூனியன் பிரதேச எம்.எல்.ஏ-க்கள்", "சேர்க்கப்பட்டவர்கள் (டெல்லி & புதுச்சேரியின் தேர்ந்தெடுக்கப்பட்ட எம்.எல்.ஏ-க்கள்)", "விலக்கப்பட்டவர்கள் (யூனியன் பிரதேச எம்.எல்.ஏ-க்கள் வாக்களிக்க முடியாது)"],
          ["சட்ட மேலவைகள்", "விலக்கப்பட்டவர்கள் (எந்த மேலவை உறுப்பினரும் வாக்களிக்க முடியாது)", "விலக்கப்பட்டவர்கள் (எந்த மேலவை உறுப்பினரும் வாக்களிக்க முடியாது)"]
        ]
      },
      {
        "id": "tbl_elected_vs_nominated",
        "title_en": "4. Elected vs Nominated Members in Presidential Election & Impeachment",
        "title_ta": "4. குடியரசுத் தலைவர் தேர்தல் & பதவி நீக்கத்தில் தேர்ந்தெடுக்கப்பட்ட vs நியமன உறுப்பினர்கள்",
        "headers_en": ["Category of Members", "Presidential Election (Art 54)", "Presidential Impeachment (Art 61)"],
        "headers_ta": ["உறுப்பினர்களின் வகை", "குடியரசுத் தலைவர் தேர்தல் (உறுப்பு 54)", "குடியரசுத் தலைவர் பதவி நீக்கம் (உறுப்பு 61)"],
        "rows_en": [
          ["Elected MPs of LS & RS", "CAN VOTE", "CAN VOTE"],
          ["Nominated MPs of LS & RS", "CANNOT VOTE", "CAN VOTE"],
          ["Elected MLAs of State Assemblies", "CAN VOTE", "CANNOT VOTE"],
          ["Nominated MLAs of State Assemblies", "CANNOT VOTE", "CANNOT VOTE"],
          ["Members of Legislative Councils", "CANNOT VOTE", "CANNOT VOTE"]
        ],
        "rows_ta": [
          ["மக்களவை & மாநிலங்களவை தேர்ந்தெடுக்கப்பட்ட எம்பிக்கள்", "வாக்களிக்கலாம்", "வாக்களிக்கலாம்"],
          ["மக்களவை & மாநிலங்களவை நியமன எம்பிக்கள்", "வாக்களிக்க முடியாது", "வாக்களிக்கலாம்"],
          ["மாநிலச் சட்டமன்றங்களின் தேர்ந்தெடுக்கப்பட்ட எம்.எல்.ஏ-க்கள்", "வாக்களிக்கலாம்", "வாக்களிக்க முடியாது"],
          ["மாநிலச் சட்டமன்றங்களின் நியமன எம்.எல்.ஏ-க்கள்", "வாக்களிக்க முடியாது", "வாக்களிக்க முடியாது"],
          ["சட்ட மேலவைகளின் உறுப்பினர்கள்", "வாக்களிக்க முடியாது", "வாக்களிக்க முடியாது"]
        ]
      },
      {
        "id": "tbl_qual_pres_vs_ls",
        "title_en": "5. President's Qualifications vs Lok Sabha MP Qualifications",
        "title_ta": "5. குடியரசுத் தலைவர் தகுதிகள் vs மக்களவை எம்பி தகுதிகள்",
        "headers_en": ["Qualification Criteria", "President of India (Art 58)", "Lok Sabha Member (Art 84)"],
        "headers_ta": ["தகுதி அளவுகோல்", "இந்தியக் குடியரசுத் தலைவர் (உறுப்பு 58)", "மக்களவை உறுப்பினர் (உறுப்பு 84)"],
        "rows_en": [
          ["Minimum Age", "35 Years", "25 Years"],
          ["Citizenship", "Citizen of India (Birth OR Naturalization)", "Citizen of India"],
          ["House Eligibility", "Must be qualified for election as Lok Sabha MP", "Must be registered voter in any parliamentary constituency"],
          ["Proposers / Seconders", "50 Proposers and 50 Seconders from Electoral College", "1 Proposer (10 if unrecognised party candidate)"],
          ["Security Deposit", "₹15,000 in RBI", "₹25,000 in Treasury (₹12,500 for SC/ST)"]
        ],
        "rows_ta": [
          ["குறைந்தபட்ச வயது", "35 ஆண்டுகள்", "25 ஆண்டுகள்"],
          ["குடியுரிமை", "இந்தியக் குடிமகன் (பிறப்பால் அல்லது இயல்புரிமையால்)", "இந்தியக் குடிமகன்"],
          ["அவை தகுதி", "மக்களவை எம்பியாகத் தேர்ந்தெடுக்கப்படும் தகுதி பெற்றிருக்க வேண்டும்", "எந்தவொரு நாடாளுமன்றத் தொகுதியிலும் பதிவுசெய்த வாக்காளராக இருக்க வேண்டும்"],
          ["முன்மொழிபவர்கள் / வழிமொழிபவர்கள்", "வாக்காளர் குழுவிலிருந்து 50 முன்மொழிபவர்கள் மற்றும் 50 வழிமொழிபவர்கள்", "1 முன்மொழிபவர் (அங்கீகரிக்கப்படாத கட்சி வேட்பாளருக்கு 10)"],
          ["பிணைத்தொகை", "ரிசர்வ் வங்கியில் ₹15,000", "கருவூலத்தில் ₹25,000 (SC/ST பிரிவினருக்கு ₹12,500)"]
        ]
      },
      {
        "id": "tbl_term_pres_vs_vp",
        "title_en": "6. President's Term vs Vice-President's Term & Succession",
        "title_ta": "6. குடியரசுத் தலைவர் பதவிக்காலம் vs துணைத் தலைவர் பதவிக்காலம் & வாரிசு உரிமை",
        "headers_en": ["Feature", "President of India", "Vice-President of India"],
        "headers_ta": ["அம்சம்", "இந்தியக் குடியரசுத் தலைவர்", "இந்தியத் துணைத் தலைவர்"],
        "rows_en": [
          ["Tenure Duration", "5 Years from date of entering office (Art 56)", "5 Years from date of entering office (Art 67)"],
          ["Resignation Letter Addressed To", "Vice-President of India", "President of India"],
          ["Re-election Cap", "Unlimited re-election allowed (Art 57)", "Unlimited re-election allowed"],
          ["Casual Vacancy Succession", "Vice-President acts as President (Art 65)", "Deputy Chairman of RS performs Chairman duties; NO Acting VP post!"],
          ["New Election Period", "Within 6 Months (New President gets full 5 yrs)", "As soon as possible (New VP gets full 5 yrs)"]
        ],
        "rows_ta": [
          ["பதவிக்காலம்", "அலுவலகத்தில் நுழையும் தேதியிலிருந்து 5 ஆண்டுகள் (உறுப்பு 56)", "அலுவலகத்தில் நுழையும் தேதியிலிருந்து 5 ஆண்டுகள் (உறுப்பு 67)"],
          ["ராஜினாமா கடிதம் அனுப்புவது", "இந்தியத் துணைத் தலைவருக்கு", "இந்தியக் குடியரசுத் தலைவருக்கு"],
          ["மறுதேர்தல் வரம்பு", "வரம்பற்ற மறுதேர்தல் அனுமதிக்கப்படுகிறது (உறுப்பு 57)", "வரம்பற்ற மறுதேர்தல் அனுமதிக்கப்படுகிறது"],
          ["தற்செயல் காலியிட வாரிசுரிமை", "துணைத் தலைவர் செயல் குடியரசுத் தலைவராகிறார் (உறுப்பு 65)", "மாநிலங்களவை துணைத் தலைவர் தலைவர் பணிகளைச் செய்கிறார்; செயல் துணைத் தலைவர் பதவி இல்லை!"],
          ["புதிய தேர்தல் காலம்", "6 மாதங்களுக்குள் (புதியவர் முழு 5 ஆண்டுகள் பெறுவார்)", "எவ்வளவு விரைவில் முடியுமோ அவ்வளவு விரைவில் (புதியவர் முழு 5 ஆண்டுகள் பெறுவார்)"]
        ]
      },
      {
        "id": "tbl_resig_vs_impeachment",
        "title_en": "7. President's Resignation vs Impeachment",
        "title_ta": "7. குடியரசுத் தலைவரின் ராஜினாமா vs பதவி நீக்கம்",
        "headers_en": ["Aspect", "Resignation (Art 56)", "Impeachment (Art 61)"],
        "headers_ta": ["அம்சம்", "ராஜினாமா (உறுப்பு 56)", "பதவி நீக்கம் (உறுப்பு 61)"],
        "rows_en": [
          ["Voluntariness", "Voluntary act by President", "Involuntary removal by Parliament"],
          ["Grounds", "No constitutional ground required", "Sole ground: 'Violation of the Constitution'"],
          ["Procedure", "Writing under hand addressed to Vice-President", "Quasi-judicial resolution passed by both Houses"],
          ["Notice & Resolution", "No notice required", "14 days' written notice signed by 1/4th total members"],
          ["Majority Required", "None (Takes effect immediately)", "2/3rd majority of TOTAL MEMBERSHIP of each House"]
        ],
        "rows_ta": [
          ["சுயவிருப்ப நிலை", "குடியரசுத் தலைவரின் சுயவிருப்ப நடவடிக்கை", "நாடாளுமன்றத்தால் செய்யப்படும் கட்டாய நீக்கம்"],
          ["காரணங்கள்", "அரசியலமைப்பு காரணம் எதுவும் தேவையில்லை", "ஒரே காரணம்: 'அரசியலமைப்பு மீறல்'"],
          ["முறை", "துணைத் தலைவருக்குத் தன் கையொப்பமிட்ட கடிதம் அனுப்புதல்", "இரு அவைகளாலும் நிறைவேற்றப்படும் பகுதி-நீதிமன்ற தீர்மானம்"],
          ["அறிவிப்பு & தீர்மானம்", "அறிவிப்பு எதுவும் தேவையில்லை", "1/4 பங்கு மொத்த உறுப்பினர்கள் கையொப்பமிட்ட 14 நாட்கள் அறிவிப்பு"],
          ["தேவையான பெரும்பான்மை", "எதுவுமில்லை (உடனடியாக அமலுக்கு வரும்)", "ஒவ்வொரு அவையின் மொத்த உறுப்பினர்களில் 2/3 பங்கு பெரும்பான்மை"]
        ]
      },
      {
        "id": "tbl_oath_pres_vs_min",
        "title_en": "8. President's Oath vs Union Minister's Oath",
        "title_ta": "8. குடியரசுத் தலைவரின் உறுதிமொழி vs மத்திய அமைச்சரின் உறுதிமொழி",
        "headers_en": ["Feature", "President's Oath (Art 60)", "Union Minister's Oath (Art 75 & 3rd Schedule)"],
        "headers_ta": ["அம்சம்", "குடியரசுத் தலைவர் உறுதிமொழி (உறுப்பு 60)", "மத்திய அமைச்சர் உறுதிமொழி (உறுப்பு 75 & 3வது அட்டவணை)"],
        "rows_en": [
          ["Constitutional Location", "Article 60 (NOT in Third Schedule)", "Third Schedule"],
          ["Administered By", "Chief Justice of India (or senior SC Judge)", "President of India"],
          ["Core Promise", "Preserve, protect and defend the Constitution and the law", "Bear true faith and allegiance to Constitution & maintain secrecy"],
          ["Secrecy Clause", "NO Secrecy Clause", "Includes Oath of Secrecy"]
        ],
        "rows_ta": [
          ["அரசியலமைப்பு இடம்", "உறுப்பு 60 (3வது அட்டவணையில் இல்லை)", "3வது அட்டவணை"],
          ["பிரமாணம் செய்து வைப்பவர்", "இந்தியத் தலைமை நீதிபதி (அல்லது மூத்த உச்ச நீதிமன்ற நீதிபதி)", "இந்தியக் குடியரசுத் தலைவர்"],
          ["முக்கிய வாக்குறுதி", "அரசியலமைப்பையும் சட்டத்தையும் பேணவும், பாதுகாக்கவும், தற்காக்கவும்", "அரசியலமைப்பின் மீது உண்மையான நம்பிக்கையும் விசுவாசமும் கொள்ளுதல் & ரகசியம் காத்தல்"],
          ["ரகசியக் காப்புப் பிரிவு", "ரகசியக் காப்புப் பிரிவு இல்லை", "ரகசியக் காப்புப் பிரமாணம் அடங்கும்"]
        ]
      },
      {
        "id": "tbl_pres_elec_vs_ls_elec",
        "title_en": "9. President's Election Method vs Lok Sabha Election Method",
        "title_ta": "9. குடியரசுத் தலைவர் தேர்தல் முறை vs மக்களவைத் தேர்தல் முறை",
        "headers_en": ["Parameter", "President's Election (Art 55)", "Lok Sabha Election (Art 81)"],
        "headers_ta": ["அளவுகோல்", "குடியரசுத் தலைவர் தேர்தல் (உறுப்பு 55)", "மக்களவைத் தேர்தல் (உறுப்பு 81)"],
        "rows_en": [
          ["Electoral System", "Proportional Representation by Single Transferable Vote (STV)", "First-Past-The-Post (FPTP) System"],
          ["Electorate", "Indirect (Elected MPs & MLAs)", "Direct (All adult citizens aged 18+)"],
          ["Winning Criterion", "Must secure Absolute Majority / Electoral Quota (>50%)", "Plurality of votes (highest votes wins, no quota needed)"],
          ["Party Whip", "No Party Whip allowed", "Party Whip applies during House voting"]
        ],
        "rows_ta": [
          ["தேர்தல் முறை", "ஒற்றை மாற்று வாக்கு மூலமான விகிதாச்சாரப் பிரதிநிதித்துவம் (STV)", "முன்பு செல்பவரே வெற்றியாளர் முறை (FPTP)"],
          ["வாக்காளர்கள்", "மறைமுக (தேர்ந்தெடுக்கப்பட்ட எம்பிக்கள் & எம்.எல்.ஏ-க்கள்)", "நேரடி (18 வயது நிரம்பிய அனைத்து வயதுவந்த குடிமக்களும்)"],
          ["வெற்றி அளவுகோல்", "கேவலமான பெரும்பான்மை / தேர்தல் பங்கை (>50%) பெற வேண்டும்", "அதிக வாக்குகள் (அதிக வாக்குகள் பெறுபவர் வெற்றி, பங்கு தேவையில்லை)"],
          ["கட்சி கொறடா", "கட்சி கொறடா அனுமதிக்கப்படுவதில்லை", "அவை வாக்களிப்பின் போது கட்சி கொறடா பொருந்தும்"]
        ]
      },
      {
        "id": "tbl_pres_vs_gov",
        "title_en": "10. President vs State Governor (Constitutional Position)",
        "title_ta": "10. குடியரசுத் தலைவர் vs மாநில ஆளுநர் (அரசியலமைப்பு நிலை)",
        "headers_en": ["Dimension", "President of India", "State Governor"],
        "headers_ta": ["பரிமாணம்", "இந்தியக் குடியரசுத் தலைவர்", "மாநில ஆளுநர்"],
        "rows_en": [
          ["Executive Sphere", "Head of the Union (Part V)", "Head of the State (Part VI)"],
          ["Appointment / Election", "Indirectly elected by Electoral College", "Appointed by President (holds office during pleasure of President)"],
          ["Discretionary Powers", "NO constitutional discretionary powers explicitly stated (bound by Art 74 advice)", "HAS explicit constitutional discretionary powers under Art 163(1)"],
          ["Pardon Power Sphere", "Pardons court-martial & death sentences (Art 72)", "Cannot pardon death sentence or court-martial (Art 161)"],
          ["Diplomatic / Military", "Supreme Commander of Armed Forces & Diplomatic head", "No military or diplomatic powers"]
        ],
        "rows_ta": [
          ["நிர்வாக எல்லை", "ஒன்றியத்தின் தலைவர் (பகுதி V)", "மாநிலத்தின் தலைவர் (பகுதி VI)"],
          ["நியமனம் / தேர்தல்", "வாக்காளர் குழுவால் மறைமுகமாகத் தேர்ந்தெடுக்கப்படுபவர்", "குடியரசுத் தலைவரால் நியமிக்கப்படுபவர் (குடியரசுத் தலைவரின் விருப்பம் உள்ளவரை பதவி வகிப்பார்)"],
          ["விருப்ப அதிகாரங்கள்", "வெளிப்படையான அரசியலமைப்பு விருப்ப அதிகாரங்கள் இல்லை (உறுப்பு 74 ஆலோசனைக்குக் கட்டுப்பட்டவர்)", "உறுப்பு 163(1)-ன் கீழ் வெளிப்படையான அரசியலமைப்பு விருப்ப அதிகாரங்கள் உண்டு"],
          ["மன்னிப்பளிக்கும் அதிகாரம்", "ராணுவ நீதிமன்றத் தண்டனை & மரண தண்டனையை மன்னிக்கலாம் (உறுப்பு 72)", "மரண தண்டனையையோ ராணுவ நீதிமன்றத் தண்டனையையோ மன்னிக்க முடியாது (உறுப்பு 161)"],
          ["ராஜதந்திர / இராணுவ அதிகாரம்", "ஆயுதப்படைகளின் உச்ச தளபதி & ராஜதந்திரத் தலைவர்", "இராணுவ அல்லது ராஜதந்திர அதிகாரங்கள் இல்லை"]
        ]
      }
    ],
    "mind_map": [
      {
        "title": "President of India (Part V - Articles 52 to 62)",
        "short_label": "President Part 1",
        "children": [
          {
            "title": "1. Constitutional Position",
            "short_label": "Position",
            "children": [
              {
                "title": "Article 52: There shall be a President of India (Head of State)",
                "short_label": "Art 52 Office"
              },
              {
                "title": "Article 53: Union Executive Power & Supreme Military Command",
                "short_label": "Art 53 Exec Power"
              },
              {
                "title": "Nominal Executive (De Jure) acting on Council of Ministers advice (Art 74)",
                "short_label": "Nominal Head"
              }
            ]
          },
          {
            "title": "2. Election & Electoral College",
            "short_label": "Election",
            "children": [
              {
                "title": "Article 54 Electoral College: Elected MPs + Elected MLAs (States, Delhi, Puducherry)",
                "short_label": "Art 54 EC"
              },
              {
                "title": "Excluded: Nominated MPs, Nominated MLAs, ALL Legislative Council Members (MLCs)",
                "short_label": "Excluded Voters"
              },
              {
                "title": "Article 55: Proportional Representation by Single Transferable Vote (STV) & Secret Ballot",
                "short_label": "Art 55 Voting Method"
              },
              {
                "title": "MLA Vote Value = (State Pop / Elected MLAs) ÷ 1000 (1971 Census)",
                "short_label": "MLA Formula"
              },
              {
                "title": "MP Vote Value = Total MLA Votes / Total Elected MPs",
                "short_label": "MP Formula"
              },
              {
                "title": "Electoral Quota = (Total Valid Votes / 2) + 1 (>50% required)",
                "short_label": "Quota"
              },
              {
                "title": "Article 71: Election Disputes decided EXCLUSIVELY by Supreme Court",
                "short_label": "Art 71 SC Disputes"
              }
            ]
          },
          {
            "title": "3. Qualifications & Conditions",
            "short_label": "Quals & Conditions",
            "children": [
              {
                "title": "Article 58 Qualifications: Citizen of India, 35+ yrs age, Lok Sabha qualification, No Office of Profit",
                "short_label": "Art 58 Qualifications"
              },
              {
                "title": "Exceptions: President, Vice-President, Governor, Ministers NOT office of profit",
                "short_label": "Profit Exceptions"
              },
              {
                "title": "Article 59 Conditions: Non-membership of Parliament/Legislature, Rent-free Rashtrapati Bhavan, Non-diminution of salary",
                "short_label": "Art 59 Conditions"
              }
            ]
          },
          {
            "title": "4. Oath, Term & Impeachment",
            "short_label": "Oath & Removal",
            "children": [
              {
                "title": "Article 60 Oath: Administered by CJI to 'Preserve, protect and defend the Constitution' (NOT 3rd Sched)",
                "short_label": "Art 60 Oath"
              },
              {
                "title": "Article 56 Term: 5 Years. Resignation addressed to Vice-President (inform LS Speaker)",
                "short_label": "Art 56 Term & Resig"
              },
              {
                "title": "Article 57 Re-election: Eligible for UNLIMITED terms (Dr. Rajendra Prasad served 2 terms)",
                "short_label": "Art 57 Re-election"
              },
              {
                "title": "Article 61 Impeachment: Ground = 'Violation of Constitution'. 14 days notice (1/4th members) + 2/3rd TOTAL membership majority in both Houses",
                "short_label": "Art 61 Impeachment"
              },
              {
                "title": "Article 62 Vacancy: Election within 6 months. New President gets full 5 years",
                "short_label": "Art 62 Vacancy"
              }
            ]
          }
        ]
      }
    ],
    "tnpsc_traps": [
      {
        "title": "1. Article 52 vs Article 53 Trap (உறுப்பு 52 vs உறுப்பு 53 பொறி)",
        "points": {
          "en": [
            "TRAP: Confusing Article 52 with Article 53 regarding the executive power vesting.",
            "FACT: Article 52 establishes the OFFICE ('There shall be a President of India'). Article 53 vests the EXECUTIVE POWER of the Union in the President."
          ],
          "ta": [
            "பொறி: நிர்வாக அதிகாரம் வழங்குவது தொடர்பாக உறுப்பு 52 மற்றும் 53-ஐ குழப்பிக் கொள்ளுதல்.",
            "உண்மை: உறுப்பு 52 பதவியை நிறுவுகிறது ('இந்தியாவிற்கு ஒரு குடியரசுத் தலைவர் இருக்க வேண்டும்'). உறுப்பு 53 ஒன்றியத்தின் நிர்வாக அதிகாரத்தைக் குடியரசுத் தலைவரிடம் வழங்குகிறது."
          ]
        }
      },
      {
        "title": "2. Nominated MPs Voting Rights Trap (நியமன எம்பிக்கள் வாக்குரிமைப் பொறி)",
        "points": {
          "en": [
            "TRAP: Believing nominated MPs cannot vote in any Presidential process.",
            "FACT: Nominated MPs CANNOT vote in President's ELECTION (Article 54), BUT they CAN vote in President's IMPEACHMENT (Article 61)!"
          ],
          "ta": [
            "பொறி: குடியரசுத் தலைவர் தொடர்பான எந்தவொரு நடைமுறையிலும் நியமன எம்பிக்கள் வாக்களிக்க முடியாது என நம்புவது.",
            "உண்மை: நியமன எம்பிக்கள் குடியரசுத் தலைவர் தேர்தலில் வாக்களிக்க முடியாது (உறுப்பு 54), ஆனால் குடியரசுத் தலைவர் பதவி நீக்கத்தில் வாக்களிக்கலாம் (உறுப்பு 61)!"
          ]
        }
      },
      {
        "title": "3. State Legislative Council (MLC) Trap (மாநில சட்ட மேலவை பொறி)",
        "points": {
          "en": [
            "TRAP: Assuming elected Legislative Council members (MLCs) vote in Presidential election.",
            "FACT: ALL members of Legislative Councils (both elected and nominated) are EXCLUDED from voting in Presidential election and impeachment!"
          ],
          "ta": [
            "பொறி: தேர்ந்தெடுக்கப்பட்ட சட்ட மேலவை உறுப்பினர்கள் (MLCs) குடியரசுத் தலைவர் தேர்தலில் வாக்களிப்பார்கள் எனக் கருதுவது.",
            "உண்மை: சட்ட மேலவைகளின் அனைத்து உறுப்பினர்களும் (தேர்ந்தெடுக்கப்பட்டவர்கள் & நியமனம் செய்யப்பட்டவர்கள்) குடியரசுத் தலைவர் தேர்தலிலும் பதவி நீக்கத்திலும் வாக்களிப்பதிலிருந்து முழுமையாக விலக்கப்பட்டுள்ளனர்!"
          ]
        }
      },
      {
        "title": "4. Delhi & Puducherry Inclusion Amendment Trap (டெல்லி & புதுச்சேரி சேர்க்கை திருத்தப் பொறி)",
        "points": {
          "en": [
            "TRAP: Stating that Delhi and Puducherry MLAs were part of the original 1950 Electoral College.",
            "FACT: Delhi and Puducherry elected MLAs were added by the 70th Constitutional Amendment Act, 1992 (effective from June 1, 1995)."
          ],
          "ta": [
            "பொறி: அசல் 1950 வாக்காளர் குழுவில் டெல்லி மற்றும் புதுச்சேரி எம்.எல்.ஏ-க்கள் இடம்பெற்றிருந்தனர் எனக் கூறுவது.",
            "உண்மை: டெல்லி மற்றும் புதுச்சேரி தேர்ந்தெடுக்கப்பட்ட எம்.எல்.ஏ-க்கள் 1992-ன் 70வது அரசியலமைப்பு திருத்தச் சட்டத்தால் சேர்க்கப்பட்டனர் (அமலுக்கு வந்த நாள்: ஜூன் 1, 1995)."
          ]
        }
      },
      {
        "title": "5. Census Year Population Trap for Vote Value (வாக்கு மதிப்பிற்கான மக்கள் தொகை கணக்கெடுப்பு ஆண்டின் பொறி)",
        "points": {
          "en": [
            "TRAP: Thinking current census population (2011) is used for calculating MLA vote value.",
            "FACT: Under 84th CAA 2001, population as per 1971 Census is used for calculating vote values until the first census figures after 2026 are published!"
          ],
          "ta": [
            "பொறி: எம்.எல்.ஏ வாக்கு மதிப்பைக் கணக்கிட தற்போதைய 2011 மக்கள் தொகை கணக்கெடுப்பு பயன்படுத்தப்படுகிறது என நினைப்பது.",
            "உண்மை: 84வது திருத்தம் 2001-ன் படி, 2026-க்குப் பிந்தைய முதல் மக்கள் தொகை கணக்கெடுப்பு விவரங்கள் வெளியாகும் வரை 1971 கணக்கெடுப்பே பயன்படுத்தப்படுகிறது!"
          ]
        }
      },
      {
        "title": "6. House Qualification Trap: Lok Sabha vs Rajya Sabha (அவை தகுதிப் பொறி: மக்களவை vs மாநிலங்களவை)",
        "points": {
          "en": [
            "TRAP: Confusing candidate qualification house for President vs Vice-President.",
            "FACT: President candidate must be qualified for election to LOK SABHA (Art 58). Vice-President candidate must be qualified for election to RAJYA SABHA (Art 66)."
          ],
          "ta": [
            "பொறி: குடியரசுத் தலைவர் vs துணைத் தலைவருக்கான வேட்பாளர் தகுதி அவையைக் குழப்பிக் கொள்ளுதல்.",
            "உண்மை: குடியரசுத் தலைவர் வேட்பாளர் மக்களவைக்குத் தேர்ந்தெடுக்கப்படும் தகுதி பெற்றிருக்க வேண்டும் (உறுப்பு 58). துணைத் தலைவர் வேட்பாளர் மாநிலங்களவைக்குத் தேர்ந்தெடுக்கப்படும் தகுதி பெற்றிருக்க வேண்டும் (உறுப்பு 66)."
          ]
        }
      },
      {
        "title": "7. Citizenship Requirement Trap: India vs USA (குடியுரிமைத் தேவைப் பொறி: இந்தியா vs அமெரிக்கா)",
        "points": {
          "en": [
            "TRAP: Believing that only a citizen by birth can become President of India.",
            "FACT: In India, BOTH a citizen by birth AND a naturalised citizen are eligible to become President. In USA, ONLY a natural-born citizen can become President!"
          ],
          "ta": [
            "பொறி: இந்தியாவில் பிறப்பால் குடிமகனானவர் மட்டுமே குடியரசுத் தலைவராக முடியும் என நம்புவது.",
            "உண்மை: இந்தியாவில் பிறப்பால் குடிமகனானவர் மற்றும் இயல்புரிமை பெற்ற குடிமகன் இருவருமே குடியரசுத் தலைவராகலாம். அமெரிக்காவில் பிறப்பால் குடிமகன் மட்டுமே அதிபராக முடியும்!"
          ]
        }
      },
      {
        "title": "8. Resignation Addressee & Information Trap (ராஜினாமா கடிதம் & தகவல் பொறி)",
        "points": {
          "en": [
            "TRAP: Thinking President addresses resignation to Chief Justice of India.",
            "FACT: President addresses resignation letter to the VICE-PRESIDENT of India (Art 56). The Vice-President must immediately communicate it to the Speaker of the Lok Sabha."
          ],
          "ta": [
            "பொறி: குடியரசுத் தலைவர் தனது ராஜினாமா கடிதத்தைத் தலைமை நீதிபதிக்கு அனுப்புகிறார் என நினைப்பது.",
            "உண்மை: குடியரசுத் தலைவர் தனது ராஜினாமா கடிதத்தை இந்தியத் துணைத் தலைவருக்கு அனுப்புகிறார் (உறுப்பு 56). துணைத் தலைவர் அதை உடனடியாக மக்களவை சபாநாயகருக்குத் தெரிவிக்க வேண்டும்."
          ]
        }
      },
      {
        "title": "9. Third Schedule Oath Exclusion Trap (3வது அட்டவணை உறுதிமொழி விலக்குப் பொறி)",
        "points": {
          "en": [
            "TRAP: Option stating President's oath is contained in the Third Schedule of the Constitution.",
            "FACT: President's oath is specified directly in ARTICLE 60, NOT in the Third Schedule! (Vice-President Art 69 and Governor Art 159 are also outside 3rd Schedule)."
          ],
          "ta": [
            "பொறி: குடியரசுத் தலைவரின் உறுதிமொழி அரசியலமைப்பின் 3வது அட்டவணையில் உள்ளது எனக் கூறும் தெரிவு.",
            "உண்மை: குடியரசுத் தலைவரின் உறுதிமொழி நேரடியாக உறுப்பு 60-ல் குறிப்பிடப்பட்டுள்ளது, 3வது அட்டவணையில் இல்லை! (துணைத் தலைவர் உறுப்பு 69 & ஆளுநர் உறுப்பு 159 ஆகியவையும் 3வது அட்டவணையில் இல்லை)."
          ]
        }
      },
      {
        "title": "10. Impeachment Majority Type Trap (பதவி நீக்க பெரும்பான்மை வகை பொறி)",
        "points": {
          "en": [
            "TRAP: Believing impeachment resolution requires 2/3rd of members present and voting.",
            "FACT: Article 61 requires a special majority of 2/3rd of the TOTAL MEMBERSHIP of each House (the strictest majority requirement in the Indian Constitution!)."
          ],
          "ta": [
            "பொறி: பதவி நீக்கத் தீர்மானத்திற்கு வந்திருந்து வாக்களிப்பவர்களில் 2/3 பங்கு போதுமானது என நம்புவது.",
            "உண்மை: உறுப்பு 61 ஒவ்வொரு அவையின் மொத்த உறுப்பினர்களில் 2/3 பங்கு பெரும்பான்மையைக் கோருகிறது (இந்திய அரசியலமைப்பில் உள்ள மிகக் கடுமையான பெரும்பான்மை தேவை!)."
          ]
        }
      }
    ],
    "important_facts": {
      "en": [
        "Article 52 creates the office of President of India as Head of State.",
        "Article 53 vests Union executive power & Supreme Command of Armed Forces in President.",
        "Article 54 defines Electoral College: Elected MPs (LS+RS) + Elected MLAs (States + UTs of Delhi & Puducherry).",
        "70th CAA 1992 added elected MLAs of Delhi and Puducherry to Electoral College (w.e.f. June 1, 1995).",
        "Nominated MPs and all Legislative Council members (MLCs) CANNOT vote in Presidential election.",
        "Article 55 mandates Proportional Representation by Single Transferable Vote (STV) and Secret Ballot.",
        "MLA Vote Value = (State Population / Total Elected MLAs) ÷ 1000 (1971 Census population freeze under 84th CAA 2001).",
        "MP Vote Value = Total value of votes of all elected MLAs of all States / Total elected MPs (LS + RS).",
        "Article 71 vests EXCLUSIVE jurisdiction in Supreme Court to decide Presidential election disputes.",
        "Article 58 qualifications: Citizen of India, 35+ years age, Lok Sabha qualification, no office of profit.",
        "Both citizen by birth and naturalised citizen are eligible for President in India (unlike USA).",
        "Article 59 mandates non-membership of Parliament/Legislature and rent-free Rashtrapati Bhavan.",
        "Article 60 oath is administered by CJI (or senior SC Judge) to 'preserve, protect and defend the Constitution'.",
        "Article 56 term is 5 years; resignation letter is addressed to Vice-President (who informs LS Speaker).",
        "Article 57 permits UNLIMITED re-election terms. Dr. Rajendra Prasad served 2 full terms (1950–1962).",
        "Article 61 impeachment ground is 'Violation of the Constitution'; requires 14 days notice & 2/3rd TOTAL membership majority in both Houses.",
        "Nominated MPs CAN vote in President's impeachment, but State MLAs CANNOT vote in impeachment.",
        "Article 62 requires casual vacancy election within 6 months; newly elected President serves full 5 years."
      ],
      "ta": [
        "உறுப்பு 52 நாட்டின் தலைவராக இந்தியக் குடியரசுத் தலைவர் பதவியை உருவாக்குகிறது.",
        "உறுப்பு 53 ஒன்றிய நிர்வாக அதிகாரம் & முப்படை உச்ச தளபதி அதிகாரத்தைக் குடியரசுத் தலைவரிடம் வழங்குகிறது.",
        "உறுப்பு 54 வாக்காளர் குழுவை வரையறுக்கிறது: தேர்ந்தெடுக்கப்பட்ட எம்பிக்கள் + தேர்ந்தெடுக்கப்பட்ட எம்.எல்.ஏ-க்கள் (மாநிலங்கள் + டெல்லி & புதுச்சேரி).",
        "70வது திருத்தம் 1992 டெல்லி மற்றும் புதுச்சேரி தேர்ந்தெடுக்கப்பட்ட எம்.எல்.ஏ-க்களை வாக்காளர் குழுவில் சேர்த்தது (ஜூன் 1, 1995 முதல்).",
        "நியமன எம்பிக்கள் மற்றும் அனைத்து சட்ட மேலவை உறுப்பினர்களும் குடியரசுத் தலைவர் தேர்தலில் வாக்களிக்க முடியாது.",
        "உறுப்பு 55 ஒற்றை மாற்று வாக்கு மூலமான விகிதாச்சாரப் பிரதிநிதித்துவம் மற்றும் ரகசிய வாக்களிப்பைக் கட்டாயப்படுத்துகிறது.",
        "எம்.எல்.ஏ வாக்கு மதிப்பு = (மாநில மக்கள் தொகை / தேர்ந்தெடுக்கப்பட்ட மொத்த எம்.எல்.ஏ-க்கள்) ÷ 1000 (1971 கணக்கெடுப்பு 84வது திருத்தம் 2001-ன் படி).",
        "எம்பி வாக்கு மதிப்பு = அனைத்து மாநிலங்களின் தேர்ந்தெடுக்கப்பட்ட எம்.எல்.ஏ வாக்குகளின் மொத்த மதிப்பு / தேர்ந்தெடுக்கப்பட்ட மொத்த எம்பிக்கள்.",
        "உறுப்பு 71 குடியரசுத் தலைவர் தேர்தல் தகராறுகளைத் தீர்மானிக்க உச்ச நீதிமன்றத்திற்கு மட்டுமே பிரத்யேக அதிகார வரம்பை வழங்குகிறது.",
        "உறுப்பு 58 தகுதிகள்: இந்தியக் குடிமகன், 35+ வயது, மக்களவை தகுதி, ஆதாயம் தரும் பதவி இன்மை.",
        "இந்தியாவில் பிறப்பால் குடிமகனானவர் மற்றும் இயல்புரிமை பெற்ற குடிமகன் இருவருமே குடியரசுத் தலைவராகலாம் (அமெரிக்காவைப் போலன்றி).",
        "உறுப்பு 59 நாடாளுமன்ற/சட்டமன்ற உறுப்பினர் அல்லாத நிலை மற்றும் வாடகையில்லா ராஷ்டிரபதி பவனைக் கட்டாயப்படுத்துகிறது.",
        "உறுப்பு 60 உறுதிமொழி CJI ஆல் பிரமாணம் செய்து வைக்கப்படுகிறது உரை: 'அரசியலமைப்பைப் பேணவும், பாதுகாக்கவும், தற்காக்கவும்'.",
        "உறுப்பு 56 பதவிக்காலம் 5 ஆண்டுகள்; ராஜினாமா கடிதம் துணைத் தலைவருக்கு அனுப்பப்படுகிறது (சபாநாயகருக்குத் தெரிவிக்கப்படும்).",
        "உறுப்பு 57 வரம்பற்ற மறுதேர்தலை அனுமதிக்கிறது. டாக்டர் ராஜேந்திர பிரசாத் 2 முழு தவணைகள் பணியாற்றினார் (1950–1962).",
        "உறுப்பு 61 பதவி நீக்கக் காரணம் 'அரசியலமைப்பு மீறல்'; 14 நாட்கள் அறிவிப்பு & இரு அவைகளிலும் 2/3 பங்கு மொத்த உறுப்பினர் பெரும்பான்மை தேவை.",
        "நியமன எம்பிக்கள் பதவி நீக்கத்தில் வாக்களிக்கலாம், ஆனால் மாநில எம்.எல்.ஏ-க்கள் பதவி நீக்கத்தில் வாக்களிக்க முடியாது.",
        "உறுப்பு 62 தற்செயல் காலியிடத் தேர்தலை 6 மாதங்களுக்குள் நடத்தக் கோருகிறது; புதியவர் முழு 5 ஆண்டுகள் பணியாற்றுவார்."
      ]
    },
    "quick_revision": {
      "en": [
        "Art 52 & 53: President is Head of State & Nominal Executive. Executive power exercised on Council of Ministers advice (Art 74).",
        "Art 54 Electoral College: Elected MPs (LS+RS) + Elected MLAs (States + UTs Delhi/Puducherry). Nominated MPs & MLCs EXCLUDED.",
        "Art 55 Vote Value: Uniformity & Parity. MLA Vote = (Pop / MLAs) ÷ 1000 based on 1971 Census. MP Vote = Total MLA votes / Total elected MPs.",
        "Election Method: Proportional Representation by Single Transferable Vote (STV) & Secret Ballot. Electoral Quota = (Valid Votes / 2) + 1.",
        "Art 71: Supreme Court has EXCLUSIVE jurisdiction over Presidential election disputes.",
        "Art 58 Qualifications: Citizen of India (birth or naturalised), 35+ yrs, LS qualification, No office of profit (Pres, VP, Gov, Ministers exempt). Requires 50 proposers & 50 seconders.",
        "Art 59 Conditions: Non-membership of Parliament/Legislature, rent-free Rashtrapati Bhavan, emoluments cannot be reduced during term.",
        "Art 60 Oath: Administered by CJI to 'preserve, protect and defend the Constitution'. Specified in Art 60, NOT Third Schedule.",
        "Art 56 & 57: 5-year term. Resignation addressed to Vice-President. Unlimited re-election terms allowed (Dr. Rajendra Prasad served 2 terms).",
        "Art 61 Impeachment: Ground = 'Violation of Constitution'. 14 days notice (1/4th members) + 2/3rd TOTAL membership majority in both Houses. Nominated MPs vote; MLAs do not vote.",
        "Art 62 Vacancy: Election within 6 months. VP acts as President. New President gets full 5 years."
      ],
      "ta": [
        "உறுப்பு 52 & 53: குடியரசுத் தலைவர் நாட்டின் தலைவர் & பெயரளவு நிர்வாகி. நிர்வாக அதிகாரம் அமைச்சரவை ஆலோசனையின் பேரில் செலுத்தப்படுகிறது (உறுப்பு 74).",
        "உறுப்பு 54 வாக்காளர் குழு: தேர்ந்தெடுக்கப்பட்ட எம்பிக்கள் + தேர்ந்தெடுக்கப்பட்ட எம்.எல்.ஏ-க்கள் (மாநிலங்கள் + டெல்லி/புதுச்சேரி). நியமன எம்பிக்கள் & சட்ட மேலவை உறுப்பினர்கள் விலக்கப்பட்டவர்கள்.",
        "உறுப்பு 55 வாக்கு மதிப்பு: சீரான தன்மை & சமநிலை. எம்.எல்.ஏ வாக்கு = (மக்கள் தொகை / எம்.எல்.ஏ-க்கள்) ÷ 1000 (1971 கணக்கெடுப்பு). எம்பி வாக்கு = மொத்த எம்.எல்.ஏ வாக்குகள் / மொத்த தேர்ந்தெடுக்கப்பட்ட எம்பிக்கள்.",
        "தேர்தல் முறை: ஒற்றை மாற்று வாக்கு (STV) & ரகசிய வாக்களிப்புடன் கூடிய விகிதாச்சாரப் பிரதிநிதித்துவம். தேர்தல் பங்கு = (செல்லுபடியாகும் வாக்குகள் / 2) + 1.",
        "உறுப்பு 71: குடியரசுத் தலைவர் தேர்தல் தகராறுகளில் உச்ச நீதிமன்றத்திற்கு மட்டுமே பிரத்யேக அதிகார வரம்பு உண்டு.",
        "உறுப்பு 58 தகுதிகள்: இந்தியக் குடிமகன், 35+ வயது, மக்களவை தகுதி, ஆதாயம் தரும் பதவி இன்மை. 50 முன்மொழிபவர்கள் & 50 வழிமொழிபவர்கள் தேவை.",
        "உறுப்பு 59 நிபந்தனைகள்: நாடாளுமன்ற/சட்டமன்ற உறுப்பினர் அல்லாத நிலை, வாடகையில்லா ராஷ்டிரபதி பவன், பதவிக்காலத்தில் ஊதியத்தைக் குறைக்க முடியாது.",
        "உறுப்பு 60 உறுதிமொழி: CJI ஆல் பிரமாணம் செய்து வைக்கப்படுகிறது ('அரசியலமைப்பைப் பேணவும், பாதுகாக்கவும், தற்காக்கவும்'). உறுப்பு 60-ல் உள்ளது, 3வது அட்டவணையில் இல்லை.",
        "உறுப்பு 56 & 57: 5 ஆண்டு பதவிக்காலம். ராஜினாமா துணைத் தலைவருக்கு அனுப்பப்படும். வரம்பற்ற மறுதேர்தல் அனுமதிக்கப்படுகிறது (டாக்டர் ராஜேந்திர பிரசாத் 2 தவணைகள் பணியாற்றினார்).",
        "உறுப்பு 61 பதவி நீக்கம்: காரணம் = 'அரசியலமைப்பு மீறல்'. 14 நாட்கள் அறிவிப்பு + இரு அவைகளிலும் 2/3 பங்கு மொத்த உறுப்பினர் பெரும்பான்மை. நியமன எம்பிக்கள் வாக்களிப்பார்கள்; எம்.எல்.ஏ-க்கள் வாக்களிக்க முடியாது.",
        "உறுப்பு 62 காலியிடம்: 6 மாதங்களுக்குள் தேர்தல். துணைத் தலைவர் செயல் குடியரசுத் தலைவராவார். புதியவர் முழு 5 ஆண்டுகள் பெறுவார்."
      ]
    },
    "revision_cards": [
      {
        "id": "card_1",
        "front_en": "Which Article creates the office of the President of India?",
        "front_ta": "இந்தியக் குடியரசுத் தலைவர் பதவியை உருவாக்கும் உறுப்பு எது?",
        "back_en": "Article 52 ('There shall be a President of India').",
        "back_ta": "உறுப்பு 52 ('இந்தியாவிற்கு ஒரு குடியரசுத் தலைவர் இருக்க வேண்டும்')."
      },
      {
        "id": "card_2",
        "front_en": "Who consists the Electoral College for Presidential Election under Article 54?",
        "front_ta": "உறுப்பு 54-ன் கீழ் குடியரசுத் தலைவர் தேர்தலுக்கான வாக்காளர் குழுவில் யார் இடம்பெற்றுள்ளனர்?",
        "back_en": "ELECTED members of Lok Sabha, Rajya Sabha, State Legislative Assemblies, and UT Assemblies of Delhi & Puducherry.",
        "back_ta": "மக்களவை, மாநிலங்களவை, மாநிலச் சட்டமன்றங்கள் மற்றும் டெல்லி & புதுச்சேரி யூனியன் பிரதேச சட்டமன்றங்களின் தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்கள்."
      },
      {
        "id": "card_3",
        "front_en": "Do Nominated MPs and Legislative Council members (MLCs) vote in Presidential election?",
        "front_ta": "நியமன எம்பிக்கள் மற்றும் சட்ட மேலவை உறுப்பினர்கள் (MLCs) குடியரசுத் தலைவர் தேர்தலில் வாக்களிக்கலாமா?",
        "back_en": "NO. Nominated members and ALL Legislative Council members are EXCLUDED from Article 54 Electoral College.",
        "back_ta": "இல்லை. நியமன உறுப்பினர்கள் மற்றும் அனைத்து சட்ட மேலவை உறுப்பினர்களும் உறுப்பு 54 வாக்காளர் குழுவிலிருந்து விலக்கப்பட்டுள்ளனர்."
      },
      {
        "id": "card_4",
        "front_en": "Which Census population is used to calculate MLA vote value under Article 55?",
        "front_ta": "உறுப்பு 55-ன் கீழ் எம்.எல்.ஏ வாக்கு மதிப்பைக் கணக்கிட எந்த மக்கள் தொகை கணக்கெடுப்பு பயன்படுத்தப்படுகிறது?",
        "back_en": "1971 Census population (frozen until the first census after 2026 under 84th CAA 2001).",
        "back_ta": "1971 மக்கள் தொகை கணக்கெடுப்பு (84வது திருத்தம் 2001-ன் படி 2026-க்குப் பிந்தைய முதல் கணக்கெடுப்பு வரை முடக்கப்பட்டது)."
      },
      {
        "id": "card_5",
        "front_en": "What is the formula for Electoral Quota in Presidential election?",
        "front_ta": "குடியரசுத் தலைவர் தேர்தலில் தேர்தல் பங்குக்கான (Electoral Quota) சூத்திரம் என்ன?",
        "back_en": "Electoral Quota = (Total Valid Votes Polled / 2) + 1. (Candidate must secure >50% votes).",
        "back_ta": "தேர்தல் பங்கு = (பதிவான மொத்த செல்லுபடியாகும் வாக்குகள் / 2) + 1. (வேட்பாளர் >50% வாக்குகளைப் பெற வேண்டும்)."
      },
      {
        "id": "card_6",
        "front_en": "Which court has EXCLUSIVE jurisdiction to decide Presidential election disputes under Article 71?",
        "front_ta": "உறுப்பு 71-ன் கீழ் குடியரசுத் தலைவர் தேர்தல் தகராறுகளைத் தீர்மானிக்க எந்த நீதிமன்றத்திற்கு மட்டுமே பிரத்யேக அதிகார வரம்பு உண்டு?",
        "back_en": "Supreme Court of India ONLY.",
        "back_ta": "இந்திய உச்ச நீதிமன்றத்திற்கு மட்டுமே."
      },
      {
        "id": "card_7",
        "front_en": "What are the minimum age and House qualification required for President under Article 58?",
        "front_ta": "உறுப்பு 58-ன் கீழ் குடியரசுத் தலைவருக்குத் தேவையான குறைந்தபட்ச வயது மற்றும் அவை தகுதி என்ன?",
        "back_en": "Minimum 35 years of age; must be qualified for election as a member of LOK SABHA.",
        "back_ta": "குறைந்தபட்சம் 35 வயது; மக்களவை உறுப்பினராகத் தேர்ந்தெடுக்கப்படும் தகுதி பெற்றிருக்க வேண்டும்."
      },
      {
        "id": "card_8",
        "front_en": "Can a naturalised citizen of India become President of India?",
        "front_ta": "இயல்புரிமை பெற்ற இந்தியக் குடிமகன் இந்தியக் குடியரசுத் தலைவராக முடியுமா?",
        "back_en": "YES. Both a citizen by birth and a naturalised citizen can become President in India (unlike USA).",
        "back_ta": "ஆம். இந்தியாவில் பிறப்பால் குடிமகனானவர் மற்றும் இயல்புரிமை பெற்ற குடிமகன் இருவருமே குடியரசுத் தலைவராகலாம் (அமெரிக்காவைப் போலன்றி)."
      },
      {
        "id": "card_9",
        "front_en": "Who administers the oath of office to the President under Article 60?",
        "front_ta": "உறுப்பு 60-ன் கீழ் குடியரசுத் தலைவருக்குப் பதவிப் பிரமாணம் செய்து வைப்பவர் யார்?",
        "back_en": "Chief Justice of India (CJI), or in his absence, the senior-most Judge of the Supreme Court available.",
        "back_ta": "இந்தியத் தலைமை நீதிபதி (CJI), அல்லது அவர் இல்லாத போது உச்ச நீதிமன்றத்தின் மிக மூத்த நீதிபதி."
      },
      {
        "id": "card_10",
        "front_en": "To whom does the President address his resignation letter under Article 56?",
        "front_ta": "உறுப்பு 56-ன் கீழ் குடியரசுத் தலைவர் தனது ராஜினாமா கடிதத்தை யாருக்கு முகவரியிடுகிறார்?",
        "back_en": "Vice-President of India (who must forthwith inform the Speaker of Lok Sabha).",
        "back_ta": "இந்தியத் துணைத் தலைவருக்கு (அவர் அதை உடனடியாக மக்களவை சபாநாயகருக்குத் தெரிவிக்க வேண்டும்)."
      },
      {
        "id": "card_11",
        "front_en": "What is the sole ground and majority required for President's impeachment under Article 61?",
        "front_ta": "உறுப்பு 61-ன் கீழ் குடியரசுத் தலைவர் பதவி நீக்கத்திற்கான ஒரே காரணம் மற்றும் தேவையான பெரும்பான்மை என்ன?",
        "back_en": "Ground: 'Violation of the Constitution'. Majority: 2/3rd majority of the TOTAL MEMBERSHIP of each House.",
        "back_ta": "காரணம்: 'அரசியலமைப்பு மீறல்'. பெரும்பான்மை: ஒவ்வொரு அவையின் மொத்த உறுப்பினர்களில் 2/3 பங்கு பெரும்பான்மை."
      },
      {
        "id": "card_12",
        "front_en": "Within what period must a casual vacancy election for President be held under Article 62?",
        "front_ta": "உறுப்பு 62-ன் கீழ் குடியரசுத் தலைவருக்கான தற்செயல் காலியிடத் தேர்தல் எந்தக் காலத்திற்குள் நடத்தப்பட வேண்டும்?",
        "back_en": "Within 6 MONTHS from the date of vacancy. The newly elected President gets a full 5-year term.",
        "back_ta": "காலியிடம் ஏற்பட்ட தேதியிலிருந்து 6 மாதங்களுக்குள். புதிதாகத் தேர்ந்தெடுக்கப்படும் குடியரசுத் தலைவர் முழு 5 ஆண்டு பதவிக்காலத்தைப் பெறுவார்."
      }
    ]
  }
}

os.makedirs("data/notes/polity", exist_ok=True)
output_path = "data/notes/polity/president_part_1.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Successfully generated {output_path}!")
