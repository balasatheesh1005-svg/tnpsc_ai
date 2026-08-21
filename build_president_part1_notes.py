import json
import os
import sys

# Ensure UTF-8 encoding for standard output
sys.stdout.reconfigure(encoding='utf-8')

print("Building President Part 1 Notes JSON...")

notes_data = {
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
    "விகிதாச்சாரப் பிரதிநிதித்துவம்",
    "MLA MP Vote Value Formula",
    "எம்.எல்.ஏ எம்பி வாக்கு மதிப்பு சூத்திரம்"
  ],
  "learning_outcomes": {
    "Understand": {
      "en": [
        "Understand the constitutional position of the President as the nominal executive head of India under Articles 52 and 53.",
        "Understand the exact composition of the Electoral College for Presidential election under Article 54.",
        "Understand the formulas for calculating the vote values of MLAs and MPs under Article 55.",
        "Understand the method of election using Proportional Representation by Single Transferable Vote (STV) with Secret Ballot.",
        "Understand the qualifications, conditions of office, oath, term, vacancy, and impeachment foundation under Articles 56–61."
      ],
      "ta": [
        "உறுப்புகள் 52 மற்றும் 53-ன் கீழ் இந்தியாவின் பெயரளவு நிர்வாகத் தலைவராகக் குடியரசுத் தலைவரின் அரசியலமைப்பு நிலையைப் புரிந்து கொள்ளுதல்.",
        "உறுப்பு 54-ன் கீழ் குடியரசுத் தலைவர் தேர்தலுக்கான வாக்காளர் குழுவின் துல்லியமான அமைப்பைப் புரிந்து கொள்ளுதல்.",
        "உறுப்பு 55-ன் கீழ் எம்.எல்.ஏ மற்றும் எம்பி வாக்குகளின் மதிப்புகளைக் கணக்கிடுவதற்கான சூத்திரங்களைப் புரிந்து கொள்ளுதல்.",
        "ரகசிய வாக்களிப்புடன் ஒற்றை மாற்று வாக்கு மூலமான விகிதாச்சாரப் பிரதிநிதித்துவத் தேர்தல் முறையைப் புரிந்து கொள்ளுதல்.",
        "உறுப்புகள் 56–61 வரையிலான தகுதிகள், அலுவலக நிபந்தனைகள், உறுதிமொழி, பதவிக்காலம், காலியிடம் மற்றும் பதவி நீக்க அடிப்படையைப் புரிந்து கொள்ளுதல்."
      ]
    },
    "Remember": {
      "en": [
        "Remember that Article 52 states 'There shall be a President of India'.",
        "Remember that nominated members of Parliament and all members of Legislative Councils DO NOT vote in the Presidential election.",
        "Remember that 70th CAA 1992 included elected MLAs of Delhi and Puducherry in the Electoral College.",
        "Remember that MLA vote value is based on the 1971 Census population until the first census after 2026.",
        "Remember that President takes oath under Article 60 to 'preserve, protect and defend the Constitution'."
      ],
      "ta": [
        "உறுப்பு 52 'இந்தியாவிற்கு ஒரு குடியரசுத் தலைவர் இருக்க வேண்டும்' எனக் குறிப்பிடுகிறது என்பதை நினைவில் கொள்ளுதல்.",
        "நாடாளுமன்றத்தின் நியமன உறுப்பினர்கள் மற்றும் சட்ட மேலவைகளின் அனைத்து உறுப்பினர்களும் குடியரசுத் தலைவர் தேர்தலில் வாக்களிக்க முடியாது என்பதை நினைவில் கொள்ளுதல்.",
        "1992-ன் 70வது திருத்தம் டெல்லி மற்றும் புதுச்சேரியின் தேர்ந்தெடுக்கப்பட்ட எம்.எல்.ஏ-க்களை வாக்காளர் குழுவில் சேர்த்தது என்பதை நினைவில் கொள்ளுதல்.",
        "எம்.எல்.ஏ வாக்கு மதிப்பு 2026-க்குப் பிந்தைய முதல் மக்கள் தொகை கணக்கெடுப்பு வரை 1971 மக்கள் தொகை கணக்கெடுப்பின் அடிப்படையில் அமைந்தது என்பதை நினைவில் கொள்ளுதல்.",
        "குடியரசுத் தலைவர் உறுப்பு 60-ன் கீழ் 'அரசியலமைப்பைப் பேணவும், பாதுகாக்கவும், தற்காக்கவும்' உறுதிமொழி ஏற்கிறார் என்பதை நினைவில் கொள்ளுதல்."
      ]
    },
    "Analyze": {
      "en": [
        "Analyze the distinction between the President's Electoral College (elected members only) and the Vice-President's Electoral College (both elected and nominated MPs).",
        "Analyze why the principle of uniformity among States and parity between States and the Union is maintained in Article 55.",
        "Analyze why nominated MPs can vote in President's impeachment (Art 61) even though they cannot vote in President's election (Art 54).",
        "Analyze the difference between US Presidential executive system (Real head) and Indian Parliamentary executive system (Nominal head)."
      ],
      "ta": [
        "குடியரசுத் தலைவர் வாக்காளர் குழு (தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்கள் மட்டுமே) மற்றும் துணைத் தலைவர் வாக்காளர் குழு (தேர்ந்தெடுக்கப்பட்ட + நியமன எம்பிக்கள்) இடையேயான வேறுபாட்டை பகுப்பாய்வு செய்தல்.",
        "மாநிலங்களுக்கிடையேயான சீரான தன்மை மற்றும் மாநிலங்கள்-மத்திய அரசு இடையேயான சமநிலை ஏன் உறுப்பு 55-ல் பராமரிக்கப்படுகிறது என்பதை பகுப்பாய்வு செய்தல்.",
        "குடியரசுத் தலைவர் தேர்தலில் (உறுப்பு 54) வாக்களிக்க முடியாத நியமன எம்பிக்கள் பதவி நீக்கத்தில் (உறுப்பு 61) ஏன் வாக்களிக்க முடியும் என்பதை பகுப்பாய்வு செய்தல்.",
        "அமெரிக்க அதிபர் நிர்வாக முறைக்கும் (உண்மைத் தலைவர்) இந்திய நாடாளுமன்ற நிர்வாக முறைக்கும் (பெயரளவுத் தலைவர்) இடையேயான வேறுபாட்டை பகுப்பாய்வு செய்தல்."
      ]
    },
    "Apply": {
      "en": [
        "Apply TNPSC elimination strategies to solve complex statement-based MCQs on Presidential election voting rights.",
        "Accurately calculate vote value concepts and identify rounding rules under Article 55.",
        "Correctly match Articles 52 to 61 with their constitutional titles in Match the Following items."
      ],
      "ta": [
        "குடியரசுத் தலைவர் தேர்தல் வாக்குரிமை பற்றிய வினாக்களில் நீக்கல் உத்திகளைச் சரியாகப் பயன்படுத்துதல்.",
        "வாக்கு மதிப்பு கருத்துகளைத் துல்லியமாகக் கணக்கிட்டு உறுப்பு 55-ன் கீழ் உள்ள முழுமையாக்கல் விதிகளை அடையாளம் காணுதல்.",
        "பொருத்துக வினாக்களில் உறுப்புகள் 52 முதல் 61 வரையிலானவற்றை அவற்றின் தலைப்புகளுடன் சரியாகப் பொருத்துதல்."
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
  ]
}

print("Base metadata assembled. Adding section contents...")
