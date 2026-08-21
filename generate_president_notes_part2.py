import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("Building President Part 2 Notes JSON...")

data = {
  "meta": {
    "topic_id": "polity_president_part_2",
    "repository_id": "polity_president",
    "display_title": "President – Part 2",
    "part": 2,
    "total_parts": 3,
    "subject": "polity",
    "chapter": "President of India",
    "language": "English + Tamil"
  },
  "metadata": {
    "version": "2.0",
    "status": "approved",
    "review_status": "gold_standard",
    "difficulty": "conceptual",
    "estimated_study_time": {
      "reading": "45 min",
      "revision": "15 min",
      "total": "60 min"
    }
  },
  "keywords": [
    "President Powers and Functions",
    "குடியரசுத் தலைவரின் அதிகாரங்கள் மற்றும் பணிகள்",
    "Executive Powers Article 53",
    "நிர்வாக அதிகாரங்கள் உறுப்பு 53",
    "Legislative Powers Article 85",
    "சட்டமன்ற அதிகாரங்கள் உறுப்பு 85",
    "Assent to Bills Article 111",
    "மசோதாக்களுக்கு ஒப்புதல் உறுப்பு 111",
    "Veto Powers Absolute Suspensive Pocket",
    "வீட்டோ அதிகாரங்கள்",
    "Ordinance Making Power Article 123",
    "அவசரச் சட்ட அதிகாரம் உறுப்பு 123",
    "Financial Powers Article 112 Budget",
    "நிதி அதிகாரங்கள் உறுப்பு 112 பட்ஜெட்",
    "Judicial Powers Article 143",
    "நீதித் துறை அதிகாரங்கள் உறுப்பு 143",
    "Pardoning Power Article 72",
    "மன்னிப்பளிக்கும் அதிகாரம் உறுப்பு 72",
    "Article 74 Aid and Advice",
    "உறுப்பு 74 உதவி மற்றும் ஆலோசனை",
    "Diplomatic and Military Powers",
    "ராஜதந்திர மற்றும் இராணுவ அதிகாரங்கள்"
  ],
  "learning_outcomes": {
    "Understand": {
      "en": [
        "Understand the executive, legislative, financial, judicial, diplomatic, and military powers of the President of India.",
        "Understand the procedure for Presidential assent to Ordinary Bills, Money Bills, and Constitutional Amendment Bills under Article 111 & Article 368.",
        "Understand the nature and types of Veto Powers (Absolute, Suspensive, Pocket, and absence of Qualified Veto in India).",
        "Understand the conditions, limitations, and time limits for Ordinance-making power under Article 123.",
        "Understand the 5 forms of Pardoning Power under Article 72 (Pardon, Reprieve, Respite, Remission, Commutation) and its judicial review principles."
      ],
      "ta": [
        "இந்தியக் குடியரசுத் தலைவரின் நிர்வாக, சட்டமன்ற, நிதி, நீதித்துறை, ராஜதந்திர மற்றும் இராணுவ அதிகாரங்களைப் புரிந்து கொள்ளுதல்.",
        "உறுப்பு 111 & 368-ன் கீழ் சாதாரண மசோதாக்கள், பண மசோதாக்கள் மற்றும் அரசியலமைப்பு திருத்த மசோதாக்களுக்குக் குடியரசுத் தலைவரின் ஒப்புதல் நடைமுறையைப் புரிந்து கொள்ளுதல்.",
        "வீட்டோ அதிகாரங்களின் தன்மை மற்றும் வகைகளைப் (முழுமையான, இடைநிறுத்த, பாக்கெட் வீட்டோ மற்றும் இந்தியாவில் தகுதிவாய்ந்த வீட்டோ இல்லாத நிலை) புரிந்து கொள்ளுதல்.",
        "உறுப்பு 123-ன் கீழ் அவசரச் சட்ட அதிகாரத்தின் நிபந்தனைகள், வரம்புகள் மற்றும் கால வரம்புகளைப் புரிந்து கொள்ளுதல்.",
        "உறுப்பு 72-ன் கீழ் 5 வகை மன்னிப்பளிக்கும் அதிகாரங்களையும் (மன்னிப்பு, இடைநிறுத்தம், நிவாரணம், குறைப்பு, மாற்றுதல்) அதன் நீதித்துறை மறுஆய்வுக் கோட்பாடுகளையும் புரிந்து கொள்ளுதல்."
      ]
    },
    "Remember": {
      "en": [
        "Remember that the President appoints key constitutional post-holders (PM, Ministers, AG, CAG, CEC, Governors, UPSC Members) on Cabinet advice.",
        "Remember that 24th CAA 1971 made Presidential assent MANDATORY for Constitutional Amendment Bills.",
        "Remember that Money Bills CANNOT be returned for reconsideration by the President.",
        "Remember that Ordinance under Article 123 must be approved by Parliament within 6 weeks from its reassembly (max life 6 months + 6 weeks).",
        "Remember that Governor (Art 161) CANNOT pardon a death sentence or court-martial sentence, whereas President (Art 72) can."
      ],
      "ta": [
        "குடியரசுத் தலைவர் அமைச்சரவை ஆலோசனையின் பேரில் முக்கிய அரசியலமைப்புப் பதவிகளை (பிரதமர், அமைச்சர்கள், ஏஜி, சிஏஜி, தலைமை தேர்தல் ஆணையர், ஆளுநர்கள், UPSC உறுப்பினர்கள்) நியமிக்கிறார் என்பதை நினைவில் கொள்ளுதல்.",
        "1971-ன் 24வது திருத்தம் அரசியலமைப்பு திருத்த மசோதாக்களுக்குக் குடியரசுத் தலைவரின் ஒப்புதலைக் கட்டாயமாக்கியது என்பதை நினைவில் கொள்ளுதல்.",
        "பண மசோதாக்களைக் குடியரசுத் தலைவர் மறுபரிசீலனைக்குத் திருப்பி அனுப்ப முடியாது என்பதை நினைவில் கொள்ளுதல்.",
        "உறுப்பு 123-ன் கீழ் உள்ள அவசரச் சட்டம் நாடாளுமன்றம் மீண்டும் கூடிய 6 வாரங்களுக்குள் ஒப்புதல் பெற வேண்டும் (அதிகபட்ச காலம் 6 மாதங்கள் + 6 வாரங்கள்) என்பதை நினைவில் கொள்ளுதல்.",
        "மாநில ஆளுநரால் (உறுப்பு 161) மரண தண்டனையையோ ராணுவ நீதிமன்றத் தண்டனையையோ மன்னிக்க முடியாது, ஆனால் குடியரசுத் தலைவரால் (உறுப்பு 72) முடியும் என்பதை நினைவில் கொள்ளுதல்."
      ]
    },
    "Analyze": {
      "en": [
        "Analyze the impact of the 42nd Amendment (1976) and 44th Amendment (1978) on Article 74 (Aid and Advice of Council of Ministers).",
        "Analyze the landmark judicial rulings on Ordinance power (DC Wadhwa 1987 & Krishna Kumar Singh 2017) and Pardoning power (Maru Ram 1980 & Epuru Sudhakar 2006).",
        "Analyze why the Indian President possesses a Pocket Veto (1986 Post Office Bill) but lacks a Qualified Veto.",
        "Analyze the distinction between President's Supreme Military Command and actual Cabinet authority in declaring war."
      ],
      "ta": [
        "உறுப்பு 74 (அமைச்சரவை உதவி மற்றும் ஆலோசனை) மீது 42வது திருத்தம் (1976) மற்றும் 44வது திருத்தம் (1978) ஏற்படுத்திய தாக்கத்தை பகுப்பாய்வு செய்தல்.",
        "அவசரச் சட்ட அதிகாரம் (டி.சி. வாத்வா 1987 & கிருஷ்ண குமார் சிங் 2017) மற்றும் மன்னிப்பளிக்கும் அதிகாரம் (மாரு ராம் 1980 & எப்புரு சுதாகர் 2006) பற்றிய முக்கிய மைல்கல் நீதிமன்றத் தீர்ப்புகளை பகுப்பாய்வு செய்தல்.",
        "இந்தியக் குடியரசுத் தலைவர் பாக்கெட் வீட்டோவைக் கொண்டிருந்தாலும் (1986 தபால் அலுவலக மசோதா) தகுதிவாய்ந்த வீட்டோ ஏன் இல்லை என்பதை பகுப்பாய்வு செய்தல்.",
        "குடியரசுத் தலைவரின் இராணுவ உச்ச தளபதி அதிகாரத்திற்கும் போரைப் பிரகடனம் செய்வதில் அமைச்சரவையின் உண்மையான அதிகாரத்திற்குமான வேறுபாட்டை பகுப்பாய்வு செய்தல்."
      ]
    },
    "Apply": {
      "en": [
        "Apply TNPSC trap elimination rules to statement questions on Presidential veto and bill assent procedures.",
        "Differentiate between Pardon, Reprieve, Respite, Remission, and Commutation in match-the-following MCQs.",
        "Accurately calculate the maximum duration of an Ordinance under Article 123 in exam questions."
      ],
      "ta": [
        "குடியரசுத் தலைவர் வீட்டோ மற்றும் மசோதா ஒப்புதல் நடைமுறை பற்றிய வினாக்களில் நீக்கல் விதிகளைப் பயன்படுத்துதல்.",
        "பொருத்துக வினாக்களில் மன்னிப்பு, இடைநிறுத்தம், நிவாரணம், குறைப்பு மற்றும் மாற்றுதல் ஆகியவற்றை வேறுபடுத்துதல்.",
        "தேர்வு வினாக்களில் உறுப்பு 123-ன் கீழ் அவசரச் சட்டத்தின் அதிகபட்ச கால அளவைத் துல்லியமாகக் கணக்கிடுதல்."
      ]
    }
  },
  "subject": "Polity",
  "topic": "President of India – Part 2",
  "language": "bilingual",
  "ui_type": "polity",
  "sections": [
    {
      "id": "sec_executive_powers",
      "title_en": "1. Executive Powers & Appointment Function (Articles 53 & 78)",
      "title_ta": "1. நிர்வாக அதிகாரங்கள் & நியமனப் பணி (உறுப்புகள் 53 & 78)",
      "type": "standard_topic"
    },
    {
      "id": "sec_legislative_powers",
      "title_en": "2. Legislative Powers & Parliamentary Relationship (Articles 85, 86, 87)",
      "title_ta": "2. சட்டமன்ற அதிகாரங்கள் & நாடாளுமன்றத் தொடர்பு (உறுப்புகள் 85, 86, 87)",
      "type": "standard_topic"
    },
    {
      "id": "sec_president_and_bills",
      "title_en": "3. President's Assent to Bills (Ordinary, Money & Amendment Bills)",
      "title_ta": "3. மசோதாக்களுக்குக் குடியரசுத் தலைவரின் ஒப்புதல் (சாதாரண, பண & திருத்த மசோதாக்கள்)",
      "type": "standard_topic"
    },
    {
      "id": "sec_veto_powers",
      "title_en": "4. Veto Powers of the President (Absolute, Suspensive, Pocket, Qualified)",
      "title_ta": "4. குடியரசுத் தலைவரின் வீட்டோ அதிகாரங்கள் (முழுமையான, இடைநிறுத்த, பாக்கெட், தகுதிவாய்ந்த)",
      "type": "standard_topic"
    },
    {
      "id": "sec_ordinance_power",
      "title_en": "5. Ordinance-Making Power of the President (Article 123)",
      "title_ta": "5. குடியரசுத் தலைவரின் அவசரச் சட்ட அதிகாரம் (உறுப்பு 123)",
      "type": "standard_topic"
    },
    {
      "id": "sec_financial_powers",
      "title_en": "6. Financial Powers & Budgetary Role (Articles 112, 113, 117, 267, 280)",
      "title_ta": "6. நிதி அதிகாரங்கள் & பட்ஜெட் பங்கு (உறுப்புகள் 112, 113, 117, 267, 280)",
      "type": "standard_topic"
    },
    {
      "id": "sec_judicial_powers",
      "title_en": "7. Judicial Powers & Advisory Jurisdiction (Articles 124, 217, 143)",
      "title_ta": "7. நீதித் துறை அதிகாரங்கள் & ஆலோசனை அதிகார வரம்பு (உறுப்புகள் 124, 217, 143)",
      "type": "standard_topic"
    },
    {
      "id": "sec_pardoning_power",
      "title_en": "8. Pardoning Power of the President (Article 72 & 5 Terms)",
      "title_ta": "8. குடியரசுத் தலைவரின் மன்னிப்பளிக்கும் அதிகாரம் (உறுப்பு 72 & 5 சொற்கள்)",
      "type": "standard_topic"
    },
    {
      "id": "sec_diplomatic_military",
      "title_en": "9. Diplomatic, Military Powers & Council of Ministers Relationship (Article 74)",
      "title_ta": "9. ராஜதந்திர, இராணுவ அதிகாரங்கள் & அமைச்சரவை உறவு (உறுப்பு 74)",
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
      "title_en": "11. Mind Map, Case Law & TNPSC Trap Points",
      "title_ta": "11. மன வரைபடம், வழக்குத் தீர்ப்புகள் & டிஎன்பிஎஸ்சி பொறி புள்ளிகள்",
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
      "en": "The President of India exercises vast constitutional powers categorized into Executive, Legislative, Financial, Judicial, Diplomatic, Military, Emergency, Veto, Ordinance-making (Article 123), and Pardoning powers (Article 72). Under Article 74, all powers are exercised on the aid and advice of the Council of Ministers headed by the Prime Minister, making the President the nominal executive head bound by constitutional democracy.",
      "ta": "இந்தியக் குடியரசுத் தலைவர் நிர்வாக, சட்டமன்ற, நிதி, நீதித்துறை, ராஜதந்திர, இராணுவ, அவசரநிலை, வீட்டோ, அவசரச் சட்டம் இயற்றுதல் (உறுப்பு 123) மற்றும் மன்னிப்பளிக்கும் அதிகாரங்கள் (உறுப்பு 72) எனப் பரந்த அரசியலமைப்பு அதிகாரங்களைச் செலுத்துகிறார். உறுப்பு 74-ன் கீழ் அனைத்து அதிகாரங்களும் பிரதமரைக் கொண்ட அமைச்சரவையின் உதவி மற்றும் ஆலோசனையின் பேரிலேயே செலுத்தப்படுவதால், குடியரசுத் தலைவர் அரசியலமைப்பு ஜனநாயகத்தால் கட்டுப்பட்ட பெயரளவு நிர்வாகத் தலைவராகச் செயல்படுகிறார்."
    },
    "introduction": {
      "en": "Part 2 of the President of India series comprehensively covers the functional powers of the President across Executive, Legislative, Financial, Judicial, Diplomatic, Military, Veto, Ordinance, and Pardoning domains. It includes detailed analysis of Article 111 (Bills), Article 123 (Ordinance), Article 72 (Pardon), Article 74 (Aid & Advice), 10 mandatory comparison tables, verified landmark judicial cases, mind map, 10 bilingual TNPSC trap points, and a 2-minute rapid revision module.",
      "ta": "இந்தியக் குடியரசுத் தலைவர் தொடரின் பகுதி 2, நிர்வாக, சட்டமன்ற, நிதி, நீதித்துறை, ராஜதந்திர, இராணுவ, வீட்டோ, அவசரச் சட்டம் மற்றும் மன்னிப்பளிக்கும் துறைகளில் குடியரசுத் தலைவரின் செயல்பாட்டு அதிகாரங்களை விரிவாக உள்ளடக்கியுள்ளது. இதில் உறுப்பு 111 (மசோதாக்கள்), உறுப்பு 123 (அவசரச் சட்டம்), உறுப்பு 72 (மன்னிப்பு), உறுப்பு 74 (உதவி & ஆலோசனை), 10 கட்டாய ஒப்பீட்டு அட்டவணைகள், சரிபார்க்கப்பட்ட மைல்கல் வழக்குத் தீர்ப்புகள், மன வரைபடம், 10 இருமொழி டிஎன்பிஎஸ்சி பொறி புள்ளிகள் மற்றும் 2 நிமிட விரைவுத் திருப்புதல் தொகுதி ஆகியவை அடங்கும்."
    },
    "sec_executive_powers": [
      {
        "title": "1. Executive Powers & Constitutional Appointments (நிர்வாக அதிகாரங்கள் & நியமனங்கள்)",
        "points": {
          "en": [
            "Executive Action: Article 53 & Article 77 mandate that all executive actions of the Union Government are formally taken in the name of the President.",
            "Formulation of Rules: President makes rules specifying the manner in which orders and instruments made in his name shall be authenticated, and rules for more convenient transaction of government business (Article 77(3)).",
            "Key Appointments (Appointed on Cabinet Advice):\n1. Prime Minister of India & other Union Ministers (Article 75)\n2. Attorney General of India (Article 76) - holds office during pleasure of President\n3. Comptroller and Auditor General of India (CAG - Article 148)\n4. Chief Election Commissioner & Election Commissioners (Article 324)\n5. Chairman & Members of UPSC (Article 316)\n6. Governors of States (Article 155) - hold office during pleasure of President\n7. Chairman & Members of Finance Commission (Article 280)\n8. National Commissions Chairmen & Members (SC, ST, OBC, Minorities, Women)",
            "Administrative Information (Article 78): President has the right to be informed of all decisions of the Council of Ministers relating to Union administration and legislation. PM has a constitutional duty to furnish such information.",
            "Union Territory Administration: Directly administers UTs through Administrators / Lieutenant Governors appointed by him.",
            "TNPSC Trap: President DOES NOT independently select appointees. All appointments are made formally on the aid and advice of the Council of Ministers headed by the Prime Minister under Article 74.",
            "2-Line Revision: All Union executive actions are taken in President's name. President appoints PM, Ministers, CAG, CEC, Governors & Commissions on Cabinet advice."
          ],
          "ta": [
            "நிர்வாக நடவடிக்கை: உறுப்புகள் 53 & 77 மத்திய அரசின் அனைத்து நிர்வாக நடவடிக்கைகளும் முறைப்படி குடியரசுத் தலைவரின் பெயரிலேயே எடுக்கப்பட வேண்டும் எனக் கட்டாயப்படுத்துகின்றன.",
            "விதிகள் உருவாக்கம்: தனது பெயரில் பிறப்பிக்கப்படும் உத்தரவுகள் மற்றும் ஆவணங்களை உறுதிப்படுத்தும் முறையைக் குறிப்பிடும் விதிகளையும், அரசுப் பணிகளை மிகவும் வசதியாக நடத்தும் விதிகளையும் குடியரசுத் தலைவர் உருவாக்குகிறார் (உறுப்பு 77(3)).",
            "முக்கிய நியமனங்கள் (அமைச்சரவை ஆலோசனையின் பேரில் நியமிக்கப்படுபவை):\n1. இந்தியப் பிரதமர் & பிற மத்திய அமைச்சர்கள் (உறுப்பு 75)\n2. இந்திய அட்டர்னி ஜெனரல் (உறுப்பு 76) - குடியரசுத் தலைவரின் விருப்பம் உள்ளவரை பதவி வகிப்பார்\n3. இந்திய தலைமை கணக்குத் தணிக்கையாளர் (CAG - உறுப்பு 148)\n4. தலைமை தேர்தல் ஆணையர் & தேர்தல் ஆணையர்கள் (உறுப்பு 324)\n5. UPSC தலைவர் & உறுப்பினர்கள் (உறுப்பு 316)\n6. மாநில ஆளுநர்கள் (உறுப்பு 155) - குடியரசுத் தலைவரின் விருப்பம் உள்ளவரை பதவி வகிப்பார்கள்\n7. நிதி ஆணையத்தின் தலைவர் & உறுப்பினர்கள் (உறுப்பு 280)\n8. தேசிய ஆணையங்களின் தலைவர்கள் & உறுப்பினர்கள் (SC, ST, OBC, சிறுபான்மையினர், பெண்கள்)",
            "நிர்வாகத் தகவல் (உறுப்பு 78): ஒன்றிய நிர்வாகம் மற்றும் சட்டமியற்றல் தொடர்பான அமைச்சரவையின் அனைத்து முடிவுகளையும் தெரிந்து கொள்ளக் குடியரசுத் தலைவருக்கு உரிமை உண்டு. இத்தகவல்களை வழங்க வேண்டியது பிரதமரின் அரசியலமைப்புக் கடமையாகும்.",
            "யூனியன் பிரதேச நிர்வாகம்: தன்னால் நியமிக்கப்படும் ஆட்சியாளர்கள் / துணைநிலை ஆளுநர்கள் மூலம் யூனியன் பிரதேசங்களை நேரடியாக நிர்வகிக்கிறார்.",
            "TNPSC பொறி: குடியரசுத் தலைவர் நியமன நபர்களைச் சுயாதீனமாகத் தேர்ந்தெடுப்பதில்லை. அனைத்து நியமனங்களும் உறுப்பு 74-ன் கீழ் பிரதமரைக் கொண்ட அமைச்சரவையின் உதவி மற்றும் ஆலோசனையின் பேரிலேயே முறைப்படி செய்யப்படுகின்றன.",
            "2-வரி திருப்புதல்: அனைத்து ஒன்றிய நிர்வாக நடவடிக்கைகளும் குடியரசுத் தலைவர் பெயரிலேயே எடுக்கப்படுகின்றன. அமைச்சரவை ஆலோசனையின் பேரில் பிரதமர், அமைச்சர்கள், CAG, CEC, ஆளுநர்கள் & ஆணையங்களை குடியரசுத் தலைவர் நியமிக்கிறார்."
          ]
        }
      }
    ],
    "sec_legislative_powers": [
      {
        "title": "1. Legislative Powers & Parliamentary Relationship (சட்டமன்ற அதிகாரங்கள் & நாடாளுமன்றத் தொடர்பு)",
        "points": {
          "en": [
            "Integral Part of Parliament: Under Article 79, Parliament of India consists of the President, Rajya Sabha, and Lok Sabha.",
            "Summoning & Prorogation (Article 85): President summons and prorogues both Houses of Parliament. Can dissolve the Lok Sabha on Cabinet advice.",
            "Addressing Parliament (Article 87): President delivers a special address to both Houses assembled together at the commencement of the FIRST session after each General Election AND at the commencement of the FIRST session of EACH YEAR (Budget Session).",
            "Sending Messages (Article 86): Can send messages to either House of Parliament regarding pending bills or other matters.",
            "Nominations:\n- Rajya Sabha (Article 80): Nominates 12 members having special knowledge/practical experience in Art, Literature, Science, and Social Service.\n- Lok Sabha: Historically nominated 2 Anglo-Indians under Art 331, BUT this was DISCONTINUED by the 104th Constitutional Amendment Act, 2019!",
            "Joint Sitting (Article 108): President summons a Joint Sitting of both Houses in case of a deadlock over an Ordinary Bill. (Presided over by the Speaker of Lok Sabha).",
            "Laying Reports: Lays reports of CAG, UPSC, Finance Commission, and National Commissions before Parliament.",
            "TNPSC Trap: Distinguish Summoning/Prorogation/Dissolution (President's power) vs Adjournment/Adjournment Sine Die (Speaker/Chairman's power!). 104th CAA 2019 abolished Anglo-Indian nomination in Lok Sabha.",
            "2-Line Revision: President is an integral part of Parliament (Art 79). Summons, prorogues & dissolves LS (Art 85); nominates 12 RS members (Art 80); summons Joint Sitting (Art 108)."
          ],
          "ta": [
            "நாடாளுமன்றத்தின் ஒருங்கிணைந்த பகுதி: உறுப்பு 79-ன் கீழ் இந்திய நாடாளுமன்றம் குடியரசுத் தலைவர், மாநிலங்களவை மற்றும் மக்களவையை உள்ளடக்கியது.",
            "கூட்டுதல் & ஒத்திவைத்தல் (உறுப்பு 85): நாடாளுமன்ற இரு அவைகளையும் குடியரசுத் தலைவர் கூட்டுகிறார் மற்றும் கூட்டத் தொடரை ஒத்திவைக்கிறார் (Prorogue). அமைச்சரவை ஆலோசனையின் பேரில் மக்களவையைக் கலைக்க முடியும்.",
            "நாடாளுமன்றத்தில் உரையாற்றுதல் (உறுப்பு 87): ஒவ்வொரு பொதுத் தேர்தலுக்குப் பிறகும் முதல் கூட்டத் தொடரின் தொடக்கத்திலும், ஒவ்வொரு ஆண்டின் முதல் கூட்டத் தொடரின் (பட்ஜெட் தொடர்) தொடக்கத்திலும் இரு அவைகளின் கூட்டுக் கூட்டத்தில் குடியரசுத் தலைவர் சிறப்புரையாற்றுகிறார்.",
            "செய்தி அனுப்புதல் (உறுப்பு 86): நிலுவையில் உள்ள மசோதாக்கள் அல்லது பிற விஷயங்கள் குறித்து நாடாளுமன்றத்தின் எந்தவொரு அவைக்கும் செய்திகளை அனுப்பலாம்.",
            "நியமனங்கள்:\n- மாநிலங்களவை (உறுப்பு 80): கலை, இலக்கியம், அறிவியல் மற்றும் சமூக சேவையில் சிறப்பு அறிவாற்றல்/அனுபவம் கொண்ட 12 உறுப்பினர்களை நியமிக்கிறார்.\n- மக்களவை: வரலாற்று ரீதியாக உறுப்பு 331-ன் கீழ் 2 ஆங்கிலோ-இந்தியர்களை நியமித்தார், ஆனால் இது 2019-ன் 104வது அரசியலமைப்பு திருத்தச் சட்டத்தால் நிறுத்தப்பட்டது!",
            "கூட்டுக் கூட்டம் (உறுப்பு 108): சாதாரண மசோதா குறித்த முட்டுக்கட்டையின் போது இரு அவைகளின் கூட்டுக் கூட்டத்தைக் குடியரசுத் தலைவர் கூட்டுகிறார். (மக்களவை சபாநாயகர் தலைமை தாங்குவார்).",
            "அறிக்கைகளை வைத்தல்: CAG, UPSC, நிதி ஆணையம் மற்றும் தேசிய ஆணையங்களின் அறிக்கைகளை நாடாளுமன்றத்தின் முன் வைக்கிறார்.",
            "TNPSC பொறி: கூட்டுதல்/ஒத்திவைத்தல்/கலைத்தல் (குடியரசுத் தலைவரின் அதிகாரம்) vs அவையை ஒத்திவைப்பது/காலவரையறையின்றி ஒத்திவைப்பது (சபாநாயகர்/தலைவரின் அதிகாரம்!) என்பதை வேறுபடுத்துக. 104வது திருத்தம் 2019 மக்களவை ஆங்கிலோ-இந்திய நியமனத்தை ரத்து செய்தது.",
            "2-வரி திருப்புதல்: குடியரசுத் தலைவர் நாடாளுமன்றத்தின் ஒருங்கிணைந்த பகுதி (உறுப்பு 79). இரு அவைகளைக் கூட்டுகிறார், ஒத்திவைக்கிறார், மக்களவையைக் கலைக்கிறார் (உறுப்பு 85); 12 மாநிலங்களவை உறுப்பினர்களை நியமிக்கிறார் (உறுப்பு 80); கூட்டுக் கூட்டத்தைக் கூட்டுகிறார் (உறுப்பு 108)."
          ]
        }
      }
    ],
    "sec_president_and_bills": [
      {
        "title": "1. Article 111: President's Assent to Bills (மசோதாக்களுக்குக் குடியரசுத் தலைவரின் ஒப்புதல்)",
        "points": {
          "en": [
            "Constitutional Options (Article 111): When a bill passed by Parliament is presented to President, he has 3 alternatives:\n1. Give assent to the bill\n2. Withhold assent to the bill\n3. Return the bill (if it is NOT a Money Bill) for reconsideration of Parliament.",
            "Ordinary Bill Rules:\n- President can give assent, withhold assent, or return ONCE for reconsideration.\n- If Parliament passes the bill again with or without amendments, President MUST give assent! (Suspensive Veto overridden by simple majority).",
            "Money Bill Rules (Articles 110 & 111):\n- Introduced ONLY with prior recommendation of President.\n- President usually gives assent because it is introduced with his prior permission.\n- President can give assent or withhold assent, BUT CANNOT return a Money Bill for reconsideration!",
            "Constitutional Amendment Bill Rules (Article 368):\n- Under the 24th Constitutional Amendment Act, 1971, it is MANDATORY for the President to give assent to a Constitutional Amendment Bill duly passed by Parliament.\n- President CANNOT withhold assent or return a Constitutional Amendment Bill!",
            "TNPSC Trap: Ordinary Bill can be returned once; Money Bill cannot be returned for reconsideration; Constitutional Amendment Bill MUST receive assent under 24th CAA 1971.",
            "2-Line Revision: Article 111 governs assent. Ordinary bills can be returned once (re-passage forces assent). Money bills cannot be returned. Amendment bill assent is mandatory (24th CAA)."
          ],
          "ta": [
            "அரசியலமைப்பு தெரிவுகள் (உறுப்பு 111): நாடாளுமன்றத்தால் நிறைவேற்றப்பட்ட ஒரு மசோதா குடியரசுத் தலைவருக்குச் சமர்ப்பிக்கப்படும் போது, அவருக்கு 3 மாற்று வழிகள் உள்ளன:\n1. மசோதாவிற்கு ஒப்புதல் அளித்தல்\n2. மசோதாவிற்கு ஒப்புதலை நிறுத்தி வைத்தல்\n3. நாடாளுமன்றத்தின் மறுபரிசீலனைக்கு மசோதாவைத் திருப்பி அனுப்புதல் (அது பண மசோதாவாக இல்லாவிட்டால்).",
            "சாதாரண மசோதா விதிகள்:\n- குடியரசுத் தலைவர் ஒப்புதல் அளிக்கலாம், ஒப்புதலை நிறுத்தி வைக்கலாம் அல்லது ஒருமுறை மறுபரிசீலனைக்குத் திருப்பி அனுப்பலாம்.\n- திருத்தங்களுடனோ அல்லது திருத்தங்கள் இன்றியோ நாடாளுமன்றம் மீண்டும் மசோதாவை நிறைவேற்றினால், குடியரசுத் தலைவர் கட்டாயம் ஒப்புதல் அளிக்க வேண்டும்! (இடைநிறுத்த வீட்டோ சாதாரண பெரும்பான்மையால் முறியடிக்கப்படும்).",
            "பண மசோதா விதிகள் (உறுப்புகள் 110 & 111):\n- குடியரசுத் தலைவரின் முன் பரிந்துரையுடன் மட்டுமே அறிமுகப்படுத்தப்படும்.\n- அவரது முன் அனுமதியுடன் அறிமுகப்படுத்தப்படுவதால் குடியரசுத் தலைவர் வழக்கமாக ஒப்புதல் அளிக்கிறார்.\n- குடியரசுத் தலைவர் ஒப்புதல் அளிக்கலாம் அல்லது ஒப்புதலை நிறுத்தி வைக்கலாம், ஆனால் பண மசோதாவை மறுபரிசீலனைக்குத் திருப்பி அனுப்ப முடியாது!",
            "அரசியலமைப்பு திருத்த மசோதா விதிகள் (உறுப்பு 368):\n- 1971-ன் 24வது அரசியலமைப்பு திருத்தச் சட்டத்தின் கீழ், நாடாளுமன்றத்தால் முறையாக நிறைவேற்றப்பட்ட அரசியலமைப்பு திருத்த மசோதாவிற்குக் குடியரசுத் தலைவர் ஒப்புதல் அளிப்பது கட்டாயமாகும்.\n- அரசியலமைப்பு திருத்த மசோதாவிற்குக் குடியரசுத் தலைவர் ஒப்புதலை நிறுத்தி வைக்கவோ மறுபரிசீலனைக்குத் திருப்பி அனுப்பவோ முடியாது!",
            "TNPSC பொறி: சாதாரண மசோதாவை ஒருமுறை திருப்பி அனுப்பலாம்; பண மசோதாவை மறுபரிசீலனைக்குத் திருப்பி அனுப்ப முடியாது; அரசியலமைப்பு திருத்த மசோதாவிற்கு 24வது திருத்தம் 1971-ன் கீழ் கட்டாயம் ஒப்புதல் அளிக்க வேண்டும்.",
            "2-வரி திருப்புதல்: உறுப்பு 111 ஒப்புதலை நிர்வகிக்கிறது. சாதாரண மசோதாக்களை ஒருமுறை திருப்பி அனுப்பலாம் (மீண்டும் நிறைவேற்றினால் ஒப்புதல் கட்டாயம்). பண மசோதாக்களைத் திருப்பி அனுப்ப முடியாது. திருத்த மசோதா ஒப்புதல் கட்டாயமாகும் (24வது திருத்தம்)."
          ]
        }
      }
    ],
    "sec_veto_powers": [
      {
        "title": "1. Veto Powers of the President (குடியரசுத் தலைவரின் வீட்டோ அதிகாரங்கள்)",
        "points": {
          "en": [
            "Concept: 'Veto' means the constitutional power of the executive head to withhold assent to a bill passed by legislature.",
            "1. Absolute Veto: Power to withhold assent to a bill, resulting in the end of the bill (it does not become an Act). Exercised in 2 situations: (a) Private Member Bills, (b) Cabinet resigns before President gives assent and new Cabinet advises withholding assent. Example: 1954 PEPSU Appropriation Bill by Dr. Rajendra Prasad.",
            "2. Suspensive Veto: Power to return an ordinary bill for reconsideration of Parliament. However, if Parliament passes the bill again with simple majority, President MUST give assent. (Suspensive veto is overridden by simple majority!). Cannot be exercised for Money Bills.",
            "3. Pocket Veto: Power to keep a bill pending indefinitely without taking any action (giving assent, withholding assent, or returning). Because Article 111 prescribes NO TIME LIMIT for President to take action on a bill! Landmark Example: In 1986, President Giani Zail Singh exercised Pocket Veto on the Indian Post Office (Amendment) Bill.",
            "4. Qualified Veto (DOES NOT EXIST IN INDIA): A veto that can be overridden by legislature only by a higher/special majority (e.g. 2/3rd majority in US Congress). Qualified Veto operates in the USA, but DOES NOT exist in India!",
            "TNPSC Trap: USA President has Qualified Veto but small Pocket Veto (10 days limit). Indian President has NO Qualified Veto, but huge Pocket Veto because Article 111 sets no time limit ('Presidential pocket is bigger than US President's!').",
            "2-Line Revision: Absolute Veto = withholding assent; Suspensive Veto = returning once (overridden by simple majority); Pocket Veto = keeping pending indefinitely (1986 Post Office Bill). Qualified Veto does NOT exist in India."
          ],
          "ta": [
            "தத்துவம்: 'வீட்டோ' என்பது சட்டமன்றத்தால் நிறைவேற்றப்பட்ட மசோதாவிற்கு ஒப்புதலை நிறுத்தி வைக்கும் நிர்வாகத் தலைவரின் அரசியலமைப்பு அதிகாரமாகும்.",
            "1. முழுமையான வீட்டோ (Absolute Veto): மசோதாவிற்கு ஒப்புதலை நிறுத்தி வைக்கும் அதிகாரம், இதன் விளைவாக மசோதா முடிவுக்கு வரும் (சட்டமாகாது). 2 சூழ்நிலைகளில் செலுத்தப்படுகிறது: (a) தனிநபர் மசோதாக்கள், (b) குடியரசுத் தலைவர் ஒப்புதல் அளிப்பதற்கு முன் அமைச்சரவை ராஜினாமா செய்து புதிய அமைச்சரவை ஒப்புதலை நிறுத்தி வைக்க ஆலோசிப்பது. உதாரணம்: 1954-ல் டாக்டர் ராஜேந்திர பிரசாத்தின் PEPSU நிதியொதுக்கீட்டு மசோதா.",
            "2. இடைநிறுத்த வீட்டோ (Suspensive Veto): சாதாரண மசோதாவை நாடாளுமன்ற மறுபரிசீலனைக்குத் திருப்பி அனுப்பும் அதிகாரம். இருப்பினும், சாதாரண பெரும்பான்மையுடன் நாடாளுமன்றம் மீண்டும் மசோதாவை நிறைவேற்றினால், குடியரசுத் தலைவர் கட்டாயம் ஒப்புதல் அளிக்க வேண்டும். (சாதாரண பெரும்பான்மையால் இது முறியடிக்கப்படும்!). பண மசோதாக்களுக்குச் செலுத்த முடியாது.",
            "3. பாக்கெட் வீட்டோ (Pocket Veto): மசோதா மீது எந்த நடவடிக்கையும் எடுக்காமல் (ஒப்புதல் அளிப்பது, நிறுத்துவது, திருப்புவது) காலவரையின்றி நிலுவையில் வைக்கும் அதிகாரம்! ஏனெனில் உறுப்பு 111 குடியரசுத் தலைவர் நடவடிக்கை எடுக்க எந்தக் கால வரம்பையும் நிர்ணயிக்கவில்லை! மைல்கல் உதாரணம்: 1986-ல் குடியரசுத் தலைவர் கியானி ஜெயில் சிங் இந்திய தபால் அலுவலக (திருத்த) மசோதா மீது பாக்கெட் வீட்டோவைச் செலுத்தினார்.",
            "4. தகுதிவாய்ந்த வீட்டோ (Qualified Veto - இந்தியாவில் இல்லை): சட்டமன்றத்தால் அதிக/சிறப்பு பெரும்பான்மையால் மட்டுமே முறியடிக்கப்படக்கூடிய வீட்டோ (எ.கா. அமெரிக்க காங்கிரஸில் 2/3 பங்கு பெரும்பான்மை). தகுதிவாய்ந்த வீட்டோ அமெரிக்காவில் செயல்படுகிறது, ஆனால் இந்தியாவில் இல்லை!",
            "TNPSC பொறி: அமெரிக்க அதிபருக்குத் தகுதிவாய்ந்த வீட்டோ உண்டு ஆனால் சிறிய பாக்கெட் வீட்டோ (10 நாட்கள் வரம்பு). இந்தியக் குடியரசுத் தலைவருக்குத் தகுதிவாய்ந்த வீட்டோ இல்லை, ஆனால் உறுப்பு 111 கால வரம்பு நிர்ணயிக்காததால் பெரிய பாக்கெட் வீட்டோ உண்டு ('இந்தியக் குடியரசுத் தலைவரின் பாக்கெட் அமெரிக்க அதிபரை விடப் பெரியது!').",
            "2-வரி திருப்புதல்: முழுமையான வீட்டோ = ஒப்புதலை நிறுத்துதல்; இடைநிறுத்த வீட்டோ = ஒருமுறை திருப்புதல் (சாதாரண பெரும்பான்மையால் முறியடிக்கப்படும்); பாக்கெட் வீட்டோ = காலவரையின்றி நிலுவையில் வைத்தல் (1986 தபால் மசோதா). தகுதிவாய்ந்த வீட்டோ இந்தியாவில் இல்லை."
          ]
        }
      }
    ],
    "sec_ordinance_power": [
      {
        "title": "1. Article 123: Ordinance-Making Power of the President (அவசரச் சட்ட அதிகாரம்)",
        "points": {
          "en": [
            "Meaning: Empowers the President to promulgate Ordinances during recess of Parliament to meet urgent situations.",
            "Constitutional Conditions (Article 123):\n1. Recess of Parliament: Can be issued ONLY when either Lok Sabha or Rajya Sabha (or both) is NOT in session.\n2. Satisfaction of President: President must be satisfied that circumstances exist requiring immediate action. 'Satisfaction' means subjective satisfaction of Cabinet (subject to judicial review for mala fide per Cooper 1970 & DC Wadhwa 1987).\n3. Co-extensive Power: Ordinance has same force and effect as an Act of Parliament, but is a temporary law. Subject matter limits are identical to Parliament's legislative powers.",
            "Constitutional Limitations:\n- Cannot amend the Constitution.\n- Cannot abridge Fundamental Rights.\n- Cannot be issued when BOTH Houses are in session.",
            "Parliamentary Approval & Time Limits:\n- Must be laid before BOTH Houses of Parliament when it reassembles.\n- An Ordinance ceases to operate at the expiry of SIX WEEKS from the reassembly of Parliament.\n- If disapproved by Parliament before 6 weeks, it ceases to operate immediately.\n- Maximum Life of Ordinance: 6 months + 6 weeks (6 months = maximum gap between 2 sessions of Parliament under Art 85 + 6 weeks reassembly period).",
            "Judicial Principles (DC Wadhwa 1987 & Krishna Kumar Singh 2017): Supreme Court ruled that re-promulgation of Ordinances without placing them before legislature is a fraud on the Constitution and unconstitutional!",
            "TNPSC Trap: Ordinance power is NOT a parallel legislative power. It is an emergency law-making power exercised strictly on Cabinet advice. Max life = 6 months + 6 weeks.",
            "2-Line Revision: Article 123 permits Ordinances during recess of Parliament. Equal force to Act. Ceases 6 weeks from Parliamentary reassembly. Max life: 6 months + 6 weeks."
          ],
          "ta": [
            "பொருள்: அவசர சூழ்நிலைகளை எதிர்கொள்ள நாடாளுமன்றக் கூட்டத்தொடர் இல்லாத காலத்தில் அவசரச் சட்டங்களை (Ordinances) பிறப்பிக்கக் குடியரசுத் தலைவருக்கு அதிகாரமளிக்கிறது.",
            "அரசியலமைப்பு நிபந்தனைகள் (உறுப்பு 123):\n1. நாடாளுமன்றக் இடைவேளை: மக்களவை அல்லது மாநிலங்களவை (அல்லது இரண்டும்) கூட்டத்தொடரில் இல்லாத போது மட்டுமே பிறப்பிக்க முடியும்.\n2. குடியரசுத் தலைவரின் திருப்தி: உடனடியாக நடவடிக்கை எடுக்க வேண்டிய சூழ்நிலைகள் இருப்பதை உணர்ந்து குடியரசுத் தலைவர் திருப்தியடைய வேண்டும். 'திருப்தி' என்பது அமைச்சரவையின் திருப்தியைக் குறிக்கும் (துர்நோக்கத்திற்காக நீதிமன்ற மறுஆய்வுக்கு உட்பட்டது - கூப்பர் 1970 & டி.சி. வாத்வா 1987).\n3. சம அதிகார எல்லை: அவசரச் சட்டம் நாடாளுமன்றச் சட்டத்திற்குச் சமமான ஆற்றலையும் விளைவையும் கொண்டது, ஆனால் தற்காலிகச் சட்டமாகும். பொருள் வரம்புகள் நாடாளுமன்றத்தின் அதிகாரத்திற்கு இணையானவை.",
            "அரசியலமைப்பு வரம்புகள்:\n- அரசியலமைப்பைத் திருத்த முடியாது.\n- அடிப்படை உரிமைகளைக் குறைக்க முடியாது.\n- இரு அவைகளும் கூட்டத்தொடரில் இருக்கும் போது பிறப்பிக்க முடியாது.",
            "நாடாளுமன்ற ஒப்புதல் & கால வரம்புகள்:\n- நாடாளுமன்றம் மீண்டும் கூடும் போது இரு அவைகளின் முன்னும் வைக்கப்பட வேண்டும்.\n- நாடாளுமன்றம் மீண்டும் கூடிய தேதியிலிருந்து 6 வாரங்கள் முடிவடையும் போது அவசரச் சட்டம் செயலிழந்துவிடும்.\n- 6 வாரங்களுக்கு முன் நாடாளுமன்றம் நிராகரித்தால் உடனடியாகச் செயலிழக்கும்.\n- அவசரச் சட்டத்தின் அதிகபட்ச ஆயுள்: 6 மாதங்கள் + 6 வாரங்கள் (6 மாதங்கள் = உறுப்பு 85-ன் கீழ் 2 தொடர்களுக்கு இடைப்பட்ட அதிகபட்ச காலம் + 6 வாரங்கள் மீண்டும் கூடும் காலம்).",
            "நீதிமன்றக் கோட்பாடுகள் (டி.சி. வாத்வா 1987 & கிருஷ்ண குமார் சிங் 2017): சட்டமன்றத்தின் முன் வைக்காமல் அவசரச் சட்டங்களை மீண்டும் மீண்டும் பிறப்பிப்பது அரசியலமைப்பு மோசடி மற்றும் செல்லாதது என உச்ச நீதிமன்றம் தீர்ப்பளித்தது!",
            "TNPSC பொறி: அவசரச் சட்ட அதிகாரம் ஒரு இணை சட்டமியற்றும் அதிகாரம் அல்ல. இது அமைச்சரவை ஆலோசனையின் பேரில் மட்டுமே செலுத்தப்படும் அவசரகால சட்ட அதிகாரமாகும். அதிகபட்ச ஆயுள் = 6 மாதங்கள் + 6 வாரங்கள்.",
            "2-வரி திருப்புதல்: உறுப்பு 123 நாடாளுமன்ற இடைவேளையின் போது அவசரச் சட்டங்களை அனுமதிக்கிறது. நாடாளுமன்றச் சட்டத்திற்குச் சமமானது. மீண்டும் கூடிய 6 வாரங்களில் செயலிழக்கும். அதிகபட்ச ஆயுள்: 6 மாதங்கள் + 6 வாரங்கள்."
          ]
        }
      }
    ],
    "sec_financial_powers": [
      {
        "title": "1. Financial Powers of the President (நிதி அதிகாரங்கள்)",
        "points": {
          "en": [
            "Money Bills: Under Article 117(1), Money Bills can be introduced in Lok Sabha ONLY with the prior recommendation of the President.",
            "Annual Financial Statement (Budget): Under Article 112, President causes the Union Budget (Annual Financial Statement) to be laid before both Houses of Parliament every financial year.",
            "Demands for Grants: Under Article 113(3), no demand for a grant can be made except on the recommendation of the President.",
            "Contingency Fund of India: Under Article 267(1), President holds and controls the Contingency Fund of India and can make advances out of it to meet unforeseen expenditure pending Parliamentary authorization.",
            "Finance Commission: Under Article 280, President constitutes a Finance Commission every 5 years (or earlier) to recommend distribution of taxes between Union and States.",
            "TNPSC Trap: President does NOT personally prepare the Budget! The Finance Ministry (Department of Economic Affairs) prepares it, but it is presented by his constitutional direction under Article 112.",
            "2-Line Revision: Money bills & Demands for grants require President's prior recommendation. Causes Budget (Art 112) to be laid; controls Contingency Fund (Art 267); sets up Finance Commission (Art 280)."
          ],
          "ta": [
            "பண மசோதாக்கள்: உறுப்பு 117(1)-ன் கீழ் பண மசோதாக்கள் குடியரசுத் தலைவரின் முன் பரிந்துரையுடன் மட்டுமே மக்களவையில் அறிமுகப்படுத்தப்பட முடியும்.",
            "ஆண்டு நிதிநிலை அறிக்கை (பட்ஜெட்): உறுப்பு 112-ன் கீழ் குடியரசுத் தலைவர் ஒவ்வொரு நிதியாண்டிலும் மத்திய பட்ஜெட்டை (ஆண்டு நிதிநிலை அறிக்கை) நாடாளுமன்ற இரு அவைகளின் முன் சமர்ப்பிக்கச் செய்கிறார்.",
            "மானியக் கோரிக்கைகள்: உறுப்பு 113(3)-ன் கீழ் குடியரசுத் தலைவரின் பரிந்துரையின்றி எந்தவொரு மானியக் கோரிக்கையும் கொண்டு வர முடியாது.",
            "இந்திய அவசரகால நிதி: உறுப்பு 267(1)-ன் கீழ் குடியரசுத் தலைவர் இந்திய அவசரகால நிதியைக் கட்டுப்பாட்டில் வைத்துள்ளார், நாடாளுமன்ற ஒப்புதல் நிலுவையில் இருக்கும் போது எதிர்பாராத செலவினங்களைச் சமாளிக்க இதிலிருந்து முன் பணம் வழங்க முடியும்.",
            "நிதி ஆணையம்: உறுப்பு 280-ன் கீழ் மத்திய-மாநில வரிகளின் பங்கீட்டைப் பரிந்துரைக்கக் குடியரசுத் தலைவர் 5 ஆண்டுகளுக்கு ஒருமுறை (அல்லது அதற்கு முன்) நிதி ஆணையத்தை அமைக்கிறார்.",
            "TNPSC பொறி: குடியரசுத் தலைவர் பட்ஜெட்டை நேரில் தயார் செய்வதில்லை! நிதி அமைச்சகம் (பொருளாதார விவகாரங்கள் துறை) அதைத் தயாரிக்கிறது, ஆனால் உறுப்பு 112-ன் கீழ் அவரது அரசியலமைப்பு வழிகாட்டுதலின் படியே சமர்ப்பிக்கப்படுகிறது.",
            "2-வரி திருப்புதல்: பண மசோதாக்கள் & மானியக் கோரிக்கைகளுக்குக் குடியரசுத் தலைவரின் முன் பரிந்துரை தேவை. பட்ஜெட்டை (உறுப்பு 112) சமர்ப்பிக்கச் செய்கிறார்; அவசரகால நிதியைக் (உறுப்பு 267) கட்டுப்படுத்துகிறார்; நிதி ஆணையத்தை (உறுப்பு 280) அமைக்கிறார்."
          ]
        }
      }
    ],
    "sec_judicial_powers": [
      {
        "title": "1. Judicial Powers & Advisory Jurisdiction (நீதித் துறை அதிகாரங்கள்)",
        "points": {
          "en": [
            "Judicial Appointments: Appoints the Chief Justice of India and Supreme Court Judges under Article 124(2), and High Court Chief Justices & Judges under Article 217(1).",
            "Advisory Jurisdiction (Article 143): President can seek advisory opinion from the Supreme Court on any question of law or fact of public importance, or pre-constitution treaties. (Opinion of SC under Art 143 is advisory and NOT binding on President!).",
            "Pardoning Power (Article 72): Has the power to grant pardons, reprieves, respites, remissions, or commutations of punishment for offences against Union law, Court Martial, and Death Sentences.",
            "TNPSC Trap: Supreme Court's advice under Article 143 is NOT binding on the President; nor is the President bound to follow it if he decides otherwise. SC opinion is purely advisory.",
            "2-Line Revision: President appoints SC/HC judges (Arts 124/217). Can seek non-binding SC advisory opinion under Art 143. Holds pardoning power under Art 72."
          ],
          "ta": [
            "நீதிமன்ற நியமனங்கள்: உறுப்பு 124(2)-ன் கீழ் இந்தியத் தலைமை நீதிபதி மற்றும் உச்ச நீதிமன்ற நீதிபதிகளையும், உறுப்பு 217(1)-ன் கீழ் உயர் நீதிமன்றத் தலைமை நீதிபதிகள் & நீதிபதிகளையும் நியமிக்கிறார்.",
            "ஆலோசனை அதிகார வரம்பு (உறுப்பு 143): பொது முக்கியத்துவம் வாய்ந்த சட்டம் அல்லது உண்மை தொடர்பான எந்தவொரு கேள்வியிலும் உச்ச நீதிமன்றத்திடமிருந்து குடியரசுத் தலைவர் ஆலோசனை கோரலாம். (உறுப்பு 143-ன் கீழ் உச்ச நீதிமன்றத்தின் கருத்து ஆலோசனையே தவிரக் குடியரசுத் தலைவரைக் கட்டுப்படுத்தாது!).",
            "மன்னிப்பளிக்கும் அதிகாரம் (உறுப்பு 72): ஒன்றிய சட்டம், ராணுவ நீதிமன்றம் மற்றும் மரண தண்டனைகளுக்கு எதிரான குற்றங்களுக்கான தண்டனைகளை மன்னிக்க, இடைநிறுத்த, குறைக்க அல்லது மாற்ற அதிகாரமுடையவர்.",
            "TNPSC பொறி: உறுப்பு 143-ன் கீழ் உச்ச நீதிமன்றத்தின் ஆலோசனை குடியரசுத் தலைவரைக் கட்டுப்படுத்தாது; உச்ச நீதிமன்றத்தின் கருத்து தூய ஆலோசனையே ஆகும்.",
            "2-வரி திருப்புதல்: உச்ச/உயர் நீதிமன்ற நீதிபதிகளை நியமிக்கிறார் (உறுப்புகள் 124/217). உறுப்பு 143-ன் கீழ் கட்டுப்படுத்தாத உச்ச நீதிமன்ற ஆலோசனையைப் பெறலாம். உறுப்பு 72-ன் கீழ் மன்னிப்பளிக்கும் அதிகாரம் கொண்டுள்ளார்."
          ]
        }
      }
    ],
    "sec_pardoning_power": [
      {
        "title": "1. Article 72: Pardoning Power & 5 Constitutional Terms (மன்னிப்பளிக்கும் அதிகாரம்)",
        "points": {
          "en": [
            "Scope of Article 72: President can grant pardons in 3 categories of cases:\n1. All cases where punishment is by a Court Martial (Military Court)\n2. All cases where punishment is for an offence against a Union Law\n3. ALL cases where sentence is a sentence of DEATH.",
            "THE 5 CONSTITUTIONAL TERMS DEFINED:\n1. PARDON (மன்னிப்பு): Completely absolves the offender from both punishment and conviction. Restores person to position as if he never committed the offence.\n2. REPRIEVE (தற்காலிக இடைநிறுத்தம்): Temporary stay of execution of a sentence (especially death sentence) for a temporary period (e.g. pending mercy petition decision).\n3. RESPITE (நிவாரணம் / குறைத் தண்டனை): Awarding a lesser punishment in place of one originally sentenced due to some special fact (e.g. pregnancy of female offender, physical disability).\n4. REMISSION (தண்டனைக் குறைப்பு): Reducing the PERIOD of sentence WITHOUT changing its character (e.g. sentence of 2 years rigorous imprisonment reduced to 1 year rigorous imprisonment).\n5. COMMUTATION (தண்டனை மாற்றம்): Substitution of one form of punishment for a LIGHTER form (e.g. Death sentence commuted to Rigorous Imprisonment; Rigorous Imprisonment commuted to Simple Imprisonment).",
            "President (Art 72) vs Governor (Art 161) Differences:\n- Death Sentence: President CAN pardon death sentence. Governor CANNOT pardon death sentence (Governor can only suspend, remit or commute death sentence).\n- Court Martial: President CAN grant pardon/remission for Court Martial sentences. Governor HAS NO POWER regarding Court Martial sentences!",
            "Judicial Principles (Maru Ram 1980, Kehar Singh 1989, Epuru Sudhakar 2006):\n- Article 72 is exercised on advice of Council of Ministers (not personal discretion).\n- Petitioner has no inherent right to oral hearing by President.\n- Article 72 is subject to limited Judicial Review if exercised arbitrarily, mala fide, or on discriminatory/irrelevant grounds.",
            "TNPSC Trap: Governor (Art 161) CANNOT pardon a death sentence (even under State law); ONLY the President (Art 72) can grant absolute PARDON for a death sentence! Remission changes duration only; Commutation changes nature of punishment to a lighter form.",
            "2-Line Revision: Article 72 covers Court Martial, Union laws & Death sentences. 5 terms: Pardon (full release), Reprieve (stay), Respite (special facts), Remission (duration reduced), Commutation (lighter form). Only President pardons death sentences."
          ],
          "ta": [
            "உறுப்பு 72-ன் எல்லை: குடியரசுத் தலைவர் 3 வகை வழக்குகளில் மன்னிப்பளிக்கலாம்:\n1. ராணுவ நீதிமன்றத்தால் (Court Martial) தண்டனை வழங்கப்பட்ட அனைத்து வழக்குகள்\n2. ஒன்றிய சட்டத்திற்கு எதிரான குற்றத்திற்காகத் தண்டனை வழங்கப்பட்ட அனைத்து வழக்குகள்\n3. மரண தண்டனை விதிக்கப்பட்ட அனைத்து வழக்குகள்.",
            "5 அரசியலமைப்புச் சொற்களின் வரையறை:\n1. PARDON (முழு மன்னிப்பு): குற்றவாளியைத் தண்டனையிலிருந்தும் குற்றச்சாட்டிலிருந்தும் முழுமையாக விடுவிக்கிறது. அவர் குற்றமே செய்யாத நிலைக்குத் திருப்புகிறது.\n2. REPRIEVE (தற்காலிக இடைநிறுத்தம்): தண்டனையை (குறிப்பாக மரண தண்டனை) நிறைவேற்றுவதைத் தற்காலிகமாகக் ஒத்திவைத்தல் (எ.கா. கருணை மனு முடிவு நிலுவையில் இருக்கும் போது).\n3. RESPITE (நிவாரணம் / சிறப்பு குறைப்பு): சில சிறப்பு காரணங்களால் (எ.கா. பெண் குற்றவாளியின் கர்ப்பம், உடல் ஊனம்) அசலில் விதிக்கப்பட்ட தண்டனைக்கு பதிலாகக் குறைந்த தண்டனை வழங்குதல்.\n4. REMISSION (தண்டனைக் குறைப்பு): தண்டனையின் தன்மையை மாற்றாமல் அதன் கால அளவைக் குறைத்தல் (எ.கா. 2 ஆண்டுகள் கடுங்காவல் தண்டனையை 1 ஆண்டு கடுங்காவலாகக் குறைத்தல்).\n5. COMMUTATION (தண்டனை மாற்றம்): ஒரு வகை தண்டனைக்கு பதிலாக லேசான வகை தண்டனையை மாற்றுதல் (எ.கா. மரண தண்டனையைக் கடுங்காவல் தண்டனையாக மாற்றுவது; கடுங்காவலைச் சாதாரண காவலாக்குவது).",
            "குடியரசுத் தலைவர் (உறுப்பு 72) vs ஆளுநர் (உறுப்பு 161) வேறுபாடுகள்:\n- மரண தண்டனை: குடியரசுத் தலைவர் மரண தண்டனையை மன்னிக்க முடியும். ஆளுநரால் மரண தண்டனையை மன்னிக்க முடியாது (ஆளுநர் ஒத்திவைக்கலாம், குறைக்கலாம் அல்லது மாற்றலாம் மட்டுமே).\n- ராணுவ நீதிமன்றம்: ராணுவ நீதிமன்றத் தண்டனைகளைக் குடியரசுத் தலைவர் மன்னிக்கலாம்/குறைக்கலாம். ஆளுநருக்கு ராணுவ நீதிமன்ற தண்டனைகளில் எந்த அதிகாரமும் இல்லை!",
            "நீதிமன்றக் கோட்பாடுகள் (மாரு ராம் 1980, கேஹர் சிங் 1989, எப்புரு சுதாகர் 2006):\n- உறுப்பு 72 அமைச்சரவை ஆலோசனையின் பேரிலேயே செலுத்தப்படுகிறது (தனிப்பட்ட விருப்பம் அல்ல).\n- மனுதாரருக்குக் குடியரசுத் தலைவரிடம் நேரில் வாய்மொழி விசாரணை கோரும் உரிமை இல்லை.\n- தன்னிச்சையாகவோ, துர்நோக்கத்துடனோ, பாகுபாட்டுடனோ செலுத்தப்பட்டால் உறுப்பு 72 வரம்பிற்குட்பட்ட நீதிமன்ற மறுஆய்வுக்கு உட்பட்டது.",
            "TNPSC பொறி: மாநில ஆளுநரால் (உறுப்பு 161) மரண தண்டனையை முழுமையாக மன்னிக்க முடியாது; குடியரசுத் தலைவர் மட்டுமே மரண தண்டனைக்கு முழு மன்னிப்பு (Pardon) அளிக்க முடியும்! Remission கால அளவை மட்டுமே மாற்றும்; Commutation தண்டனையின் தன்மையை லேசான வடிவத்திற்கு மாற்றும்.",
            "2-வரி திருப்புதல்: உறுப்பு 72 ராணுவ நீதிமன்றம், ஒன்றிய சட்டங்கள் & மரண தண்டனைகளை உள்ளடக்கியது. 5 சொற்கள்: Pardon (முழு விடுதலை), Reprieve (ஒத்திவைப்பு), Respite (சிறப்பு காரணம்), Remission (காலக் குறைப்பு), Commutation (லேசான வடிவம்). குடியரசுத் தலைவர் மட்டுமே மரண தண்டனையை மன்னிக்கிறார்."
          ]
        }
      }
    ],
    "sec_diplomatic_military": [
      {
        "title": "1. Diplomatic, Military Powers & Article 74 Relationship (ராஜதந்திர, இராணுவ அதிகாரங்கள் & உறுப்பு 74)",
        "points": {
          "en": [
            "Diplomatic Powers: All international treaties and agreements are negotiated and concluded in the name of the President (subject to approval of Parliament). Represents India in international forums and sends/receives ambassadors and high commissioners.",
            "Military Powers: Under Article 53(2), President is the Supreme Commander of the Defence Forces of India. Appoints Chiefs of Army, Navy, and Air Force. Can declare war or conclude peace ONLY subject to Parliamentary law and Cabinet decision.",
            "Article 74 (Aid and Advice Framework):\n- Article 74(1): There shall be a Council of Ministers with Prime Minister at head to aid and advise President, who SHALL act in accordance with such advice.\n- 42nd CAA 1976: Made advice of Council of Ministers strictly BINDING on President.\n- 44th CAA 1978: Added a proviso allowing President to require Council of Ministers to reconsider advice ONCE. However, after reconsideration, President MUST accept the advice!",
            "Nominal vs Real Executive Rationale: In India's parliamentary democracy, the President is a constitutional figurehead (De Jure), whereas political power rests with the elected Prime Minister and Cabinet (De Facto) accountable to Lok Sabha.",
            "TNPSC Trap: President CANNOT independently declare war or sign treaties without Cabinet approval and Parliamentary legislation. 44th CAA allows ONE reconsideration of advice, but re-sent advice is 100% BINDING.",
            "2-Line Revision: Treaties & War in President's name subject to Cabinet & Parliament. Article 74 advice is binding (42nd CAA); President can return advice ONCE for reconsideration (44th CAA)."
          ],
          "ta": [
            "ராஜதந்திர அதிகாரங்கள்: அனைத்து சர்வதேச ஒப்பந்தங்களும் உடன்படிக்கைகளும் குடியரசுத் தலைவரின் பெயரிலேயே பேச்சுவார்த்தை நடத்தப்பட்டு முடிவடைக்கப்படுகின்றன (நாடாளுமன்ற ஒப்புதலுக்கு உட்பட்டது). சர்வதேச மன்றங்களில் இந்தியாவைப் பிரதிநிதித்துவப்படுத்துகிறார் மற்றும் தூதர்களை அனுப்புகிறார்/ஏற்கிறார்.",
            "இராணுவ அதிகாரங்கள்: உறுப்பு 53(2)-ன் கீழ் குடியரசுத் தலைவர் இந்தியப் பாதுகாப்புப் படைகளின் உச்ச தளபதி ஆவார். தரைப்படை, கடற்படை, விமானப்படைத் தலைவர்களை நியமிக்கிறார். நாடாளுமன்றச் சட்டம் மற்றும் அமைச்சரவை முடிவிற்கு உட்பட்டே போரைப் பிரகடனம் செய்யவோ அமைதியை ஏற்படுத்தவோ முடியும்.",
            "உறுப்பு 74 (உதவி மற்றும் ஆலோசனை கட்டமைப்பு):\n- உறுப்பு 74(1): குடியரசுத் தலைவருக்கு உதவி மற்றும் ஆலோசனை வழங்க பிரதமரைக் தலைவராகக் கொண்ட அமைச்சரவை இருக்கும், குடியரசுத் தலைவர் அவ்ஆலோசனைப்படியே செயல்பட வேண்டும்.\n- 42வது திருத்தம் 1976: அமைச்சரவையின் ஆலோசனையைக் குடியரசுத் தலைவருக்குக் கண்டிப்பான கட்டாயமாக்கியது (BINDING).\n- 44வது திருத்தம் 1978: ஆலோசனையை ஒருமுறை மறுபரிசீலனை செய்ய அமைச்சரவையைக் கோரக் குடியரசுத் தலைவருக்கு அனுமதியளிக்கும் நிபந்தனையைச் சேர்த்தது. இருப்பினும், மறுபரிசீலனைக்குப் பிறகு குடியரசுத் தலைவர் அவ்ஆலோசனையைக் கட்டாயம் ஏற்க வேண்டும்!",
            "பெயரளவு vs உண்மை நிர்வாகக் காரணம்: இந்தியாவின் நாடாளுமன்ற ஜனநாயகத்தில், குடியரசுத் தலைவர் ஒரு அரசியலமைப்பு முறைசார் தலைவர் (De Jure), அதே நேரத்தில் அரசியல் அதிகாரம் மக்களவைக்குப் பொறுப்பான தேர்ந்தெடுக்கப்பட்ட பிரதமர் மற்றும் அமைச்சரவையிடம் (De Facto) உள்ளது.",
            "TNPSC பொறி: அமைச்சரவை ஒப்புதல் மற்றும் நாடாளுமன்றச் சட்டமின்றி குடியரசுத் தலைவரால் சுயாதீனமாக போரைப் பிரகடனம் செய்யவோ ஒப்பந்தங்களில் கையெழுத்திடவோ முடியாது. 44வது திருத்தம் ஆலோசனையை ஒருமுறை மறுபரிசீலனை செய்ய அனுமதிக்கிறது, ஆனால் மீண்டும் அனுப்பப்படும் ஆலோசனை 100% கட்டாயமாகும்.",
            "2-வரி திருப்புதல்: ஒப்பந்தங்கள் & போர் குடியரசுத் தலைவர் பெயரில் அமைச்சரவை & நாடாளுமன்றத்திற்கு உட்பட்டவை. உறுப்பு 74 ஆலோசனை கட்டாயமானது (42வது திருத்தம்); குடியரசுத் தலைவர் ஆலோசனையை ஒருமுறை மறுபரிசீலனைக்கு அனுப்பலாம் (44வது திருத்தம்)."
          ]
        }
      }
    ],
    "comparison_tables": [
      {
        "id": "tbl_powers_categorization",
        "title_en": "1. Categorization of Presidential Powers (Executive, Legislative, Financial, Judicial)",
        "title_ta": "1. குடியரசுத் தலைவர் அதிகாரங்களின் வகைப்பாடு (நிர்வாக, சட்டமன்ற, நிதி, நீதித்துறை)",
        "headers_en": ["Category", "Core Scope & Constitutional Basis", "Key Example Powers"],
        "headers_ta": ["வகை", "முக்கிய எல்லை & அரசியலமைப்பு அடிப்படை", "முக்கிய உதாரண அதிகாரங்கள்"],
        "rows_en": [
          ["Executive Powers", "Union Administration & Appointments (Art 53, 77, 78)", "Appoints PM, Ministers, CAG, CEC, Governors, UPSC Members"],
          ["Legislative Powers", "Parliamentary Functioning & Bills (Art 79, 85, 87, 111)", "Summons/Prorogues Parliament, Dissolves LS, Assent to Bills, Art 80 RS nominations"],
          ["Financial Powers", "Budgetary Process & Funds (Art 112, 113, 267, 280)", "Prior recommendation for Money Bills, Lays Budget, Contingency Fund control"],
          ["Judicial Powers", "Court Appointments & Mercy (Art 124, 143, 72)", "Appoints SC/HC Judges, Art 143 Advisory opinion, Art 72 Pardoning power"]
        ],
        "rows_ta": [
          ["நிர்வாக அதிகாரங்கள்", "ஒன்றிய நிர்வாகம் & நியமனங்கள் (உறுப்புகள் 53, 77, 78)", "பிரதமர், அமைச்சர்கள், CAG, CEC, ஆளுநர்கள், UPSC உறுப்பினர்களை நியமித்தல்"],
          ["சட்டமன்ற அதிகாரங்கள்", "நாடாளுமன்றச் செயல்பாடு & மசோதாக்கள் (உறுப்புகள் 79, 85, 87, 111)", "நாடாளுமன்றத்தைக் கூட்டுதல்/ஒத்திவைத்தல், மக்களவையைக் கலைத்தல், மசோதா ஒப்புதல்"],
          ["நிதி அதிகாரங்கள்", "பட்ஜெட் நடைமுறை & நிதிகள் (உறுப்புகள் 112, 113, 267, 280)", "பண மசோதாக்களுக்கு முன் பரிந்துரை, பட்ஜெட் சமர்ப்பித்தல், அவசரகால நிதி"],
          ["நீதித் துறை அதிகாரங்கள்", "நீதிமன்ற நியமனங்கள் & கருணை (உறுப்புகள் 124, 143, 72)", "உச்ச/உயர் நீதிமன்ற நீதிபதிகள் நியமனம், உறுப்பு 143 ஆலோசனை, உறுப்பு 72 மன்னிப்பு"]
        ]
      },
      {
        "id": "tbl_bill_types_assent",
        "title_en": "2. Ordinary Bill vs Money Bill vs Constitutional Amendment Bill (Assent Rules)",
        "title_ta": "2. சாதாரண மசோதா vs பண மசோதா vs அரசியலமைப்பு திருத்த மசோதா (ஒப்புதல் விதிகள்)",
        "headers_en": ["Bill Type", "Prior Recommendation", "Can President Withhold Assent?", "Can President Return for Reconsideration?"],
        "headers_ta": ["மசோதா வகை", "முன் பரிந்துரை", "ஒப்புதலை நிறுத்தி வைக்க முடியுமா?", "மறுபரிசீலனைக்குத் திருப்பி அனுப்ப முடியுமா?"],
        "rows_en": [
          ["Ordinary Bill (Art 107/111)", "NO prior recommendation required", "YES (Absolute Veto)", "YES (Suspensive Veto - once only)"],
          ["Money Bill (Art 110/117)", "YES, mandatory prior recommendation", "YES (rarely exercised)", "NO (Cannot be returned for reconsideration)"],
          ["Constitutional Amendment Bill (Art 368)", "NO prior recommendation required", "NO (Mandatory assent under 24th CAA 1971)", "NO (Cannot be returned for reconsideration)"]
        ],
        "rows_ta": [
          ["சாதாரண மசோதா (உறுப்புகள் 107/111)", "முன் பரிந்துரை தேவையில்லை", "ஆம் (முழுமையான வீட்டோ)", "ஆம் (இடைநிறுத்த வீட்டோ - ஒருமுறை மட்டுமே)"],
          ["பண மசோதா (உறுப்புகள் 110/117)", "ஆம், கட்டாய முன் பரிந்துரை", "ஆம் (அரிதாகச் செலுத்தப்படும்)", "இல்லை (மறுபரிசீலனைக்குத் திருப்பி அனுப்ப முடியாது)"],
          ["அரசியலமைப்பு திருத்த மசோதா (உறுப்பு 368)", "முன் பரிந்துரை தேவையில்லை", "இல்லை (24வது திருத்தம் 1971-ன் கீழ் கட்டாய ஒப்புதல்)", "இல்லை (மறுபரிசீலனைக்குத் திருப்பி அனுப்ப முடியாது)"]
        ]
      },
      {
        "id": "tbl_veto_comparison",
        "title_en": "3. Comparison of Veto Types (Absolute, Suspensive, Pocket, Qualified)",
        "title_ta": "3. வீட்டோ வகைகளின் ஒப்பீடு (முழுமையான, இடைநிறுத்த, பாக்கெட், தகுதிவாய்ந்த)",
        "headers_en": ["Veto Type", "Core Meaning & Action", "How it is Overridden", "Status in India"],
        "headers_ta": ["வீட்டோ வகை", "முக்கிய பொருள் & நடவடிக்கை", "எவ்வாறு முறியடிக்கப்படுகிறது", "இந்தியாவில் நிலை"],
        "rows_en": [
          ["Absolute Veto", "Withholding assent to a bill completely", "Cannot be overridden", "OPERATES in India (Private member bills / Cabinet resigns)"],
          ["Suspensive Veto", "Returning ordinary bill for reconsideration", "Overridden by SIMPLE majority of Parliament upon re-passage", "OPERATES in India (Ordinary bills only)"],
          ["Pocket Veto", "Keeping bill pending indefinitely without action", "No time limit set in Art 111 to override", "OPERATES in India (1986 Post Office Bill)"],
          ["Qualified Veto", "Veto overridden only by higher/special majority", "Overridden by 2/3rd special majority in legislature", "DOES NOT EXIST in India (Operates in USA)"]
        ],
        "rows_ta": [
          ["முழுமையான வீட்டோ", "மசோதாவிற்கு ஒப்புதலை முழுமையாக நிறுத்தி வைத்தல்", "முறியடிக்க முடியாது", "இந்தியாவில் உண்டு (தனிநபர் மசோதாக்கள் / அமைச்சரவை ராஜினாமா)"],
          ["இடைநிறுத்த வீட்டோ", "சாதாரண மசோதாவை மறுபரிசீலனைக்குத் திருப்பி அனுப்புதல்", "மீண்டும் நிறைவேற்றும் போது நாடாளுமன்ற சாதாரண பெரும்பான்மையால் முறியடிக்கப்படும்", "இந்தியாவில் உண்டு (சாதாரண மசோதாக்கள் மட்டுமே)"],
          ["பாக்கெட் வீட்டோ", "நடவடிக்கையின்றி மசோதாவைக் காலவரையின்றி நிலுவையில் வைத்தல்", "முறியடிக்க உறுப்பு 111-ல் கால வரம்பு இல்லை", "இந்தியாவில் உண்டு (1986 தபால் மசோதா)"],
          ["தகுதிவாய்ந்த வீட்டோ", "அதிக/சிறப்பு பெரும்பான்மையால் மட்டுமே முறியடிக்கப்படும் வீட்டோ", "சட்டமன்றத்தில் 2/3 பங்கு சிறப்பு பெரும்பான்மையால் முறியடிக்கப்படும்", "இந்தியாவில் இல்லை (அமெரிக்காவில் செயல்படுகிறது)"]
        ]
      },
      {
        "id": "tbl_pardoning_terms",
        "title_en": "4. The 5 Pardoning Terms under Article 72",
        "title_ta": "4. உறுப்பு 72-ன் கீழ் 5 மன்னிப்பளிக்கும் சொற்கள்",
        "headers_en": ["Term", "Legal Effect / Action", "Key Example / Distinguishing Feature"],
        "headers_ta": ["சொல்", "சட்ட விளைவு / நடவடிக்கை", "முக்கிய உதாரணம் / வேறுபடுத்தும் அம்சம்"],
        "rows_en": [
          ["PARDON (முழு மன்னிப்பு)", "Completely removes sentence and conviction", "Restores offender as if crime was never committed"],
          ["REPRIEVE (தற்காலிக ஒத்திவைப்பு)", "Temporary stay of execution of a sentence", "Stay of death sentence pending mercy petition decision"],
          ["RESPITE (நிவாரணம் / குறைப்பு)", "Awarding lesser punishment due to special facts", "Lesser sentence due to pregnancy or physical disability"],
          ["REMISSION (காலக் குறைப்பு)", "Reducing period of sentence WITHOUT changing character", "2 years rigorous imprisonment reduced to 1 year rigorous"],
          ["COMMUTATION (தண்டனை மாற்றம்)", "Substituting punishment for a LIGHTER form", "Death sentence commuted to Rigorous Imprisonment"]
        ],
        "rows_ta": [
          ["PARDON (முழு மன்னிப்பு)", "தண்டனையையும் குற்றச்சாட்டையும் முழுமையாக நீக்குகிறது", "குற்றமே செய்யாத நிலைக்குக் குற்றவாளியைத் திருப்புகிறது"],
          ["REPRIEVE (தற்காலிக ஒத்திவைப்பு)", "தண்டனையை நிறைவேற்றுவதைத் தற்காலிகமாக ஒத்திவைத்தல்", "கருணை மனு நிலுவையில் இருக்கும் போது மரண தண்டனை ஒத்திவைப்பு"],
          ["RESPITE (நிவாரணம் / குறைப்பு)", "சிறப்பு காரணங்களால் குறைந்த தண்டனை வழங்குதல்", "கர்ப்பம் அல்லது உடல் ஊனம் காரணமாகக் குறைந்த தண்டனை"],
          ["REMISSION (காலக் குறைப்பு)", "தன்மையை மாற்றாமல் தண்டனையின் கால அளவைக் குறைத்தல்", "2 ஆண்டுகள் கடுங்காவல் தண்டனை 1 ஆண்டு கடுங்காவலாகக் குறைப்பு"],
          ["COMMUTATION (தண்டனை மாற்றம்)", "தண்டனையை லேசான வடிவத்திற்கு மாற்றுதல்", "மரண தண்டனையைக் கடுங்காவல் தண்டனையாக மாற்றுதல்"]
        ]
      },
      {
        "id": "tbl_pardon_pres_vs_gov",
        "title_en": "5. Article 72 (President) vs Article 161 (Governor) Pardoning Power",
        "title_ta": "5. உறுப்பு 72 (குடியரசுத் தலைவர்) vs உறுப்பு 161 (ஆளுநர்) மன்னிப்பளிக்கும் அதிகாரம்",
        "headers_en": ["Parameter", "President (Article 72)", "Governor (Article 161)"],
        "headers_ta": ["அளவுகோல்", "குடியரசுத் தலைவர் (உறுப்பு 72)", "ஆளுநர் (உறுப்பு 161)"],
        "rows_en": [
          ["Death Sentence Pardon", "CAN PARDON a death sentence completely", "CANNOT PARDON a death sentence (Can only suspend, remit or commute)"],
          ["Court Martial Sentences", "CAN grant pardon/remission for Court Martial sentences", "HAS NO POWER regarding Court Martial sentences"],
          ["Executive Jurisdiction", "Offences against Union Laws", "Offences against State Laws"],
          ["Advice Source", "Union Council of Ministers advice", "State Council of Ministers advice"]
        ],
        "rows_ta": [
          ["மரண தண்டனை மன்னிப்பு", "மரண தண்டனையை முழுமையாக மன்னிக்க முடியும்", "மரண தண்டனையை மன்னிக்க முடியாது (ஒத்திவைக்கலாம், குறைக்கலாம், மாற்றலாம் மட்டுமே)"],
          ["ராணுவ நீதிமன்ற தண்டனை", "ராணுவ நீதிமன்ற தண்டனைகளை மன்னிக்க/குறைக்க முடியும்", "ராணுவ நீதிமன்ற தண்டனைகளில் அதிகாரம் இல்லை"],
          ["நிர்வாக எல்லை", "ஒன்றிய சட்டங்களுக்கு எதிரான குற்றங்கள்", "மாநிலச் சட்டங்களுக்கு எதிரான குற்றங்கள்"],
          ["ஆலோசனை மூலாதாரம்", "மத்திய அமைச்சரவை ஆலோசனை", "மாநில அமைச்சரவை ஆலோசனை"]
        ]
      },
      {
        "id": "tbl_ordinance_vs_act",
        "title_en": "6. President's Ordinance (Art 123) vs Parliamentary Act",
        "title_ta": "6. குடியரசுத் தலைவரின் அவசரச் சட்டம் (உறுப்பு 123) vs நாடாளுமன்றச் சட்டம்",
        "headers_en": ["Feature", "Ordinance (Article 123)", "Act of Parliament"],
        "headers_ta": ["அம்சம்", "அவசரச் சட்டம் (உறுப்பு 123)", "நாடாளுமன்றச் சட்டம்"],
        "rows_en": [
          ["Promulgating Body", "President of India on Cabinet advice", "Both Houses of Parliament with Presidential assent"],
          ["Timing / Session", "Promulgated ONLY during recess of Parliament", "Enacted when Parliament is IN session"],
          ["Life / Validity", "Temporary (Max 6 months + 6 weeks unless approved)", "Permanent (until repealed or amended)"],
          ["Constitutional Amendment", "CANNOT amend the Constitution", "CAN amend the Constitution (under Art 368)"]
        ],
        "rows_ta": [
          ["பிறப்பிக்கும் அமைப்பு", "அமைச்சரவை ஆலோசனையின் பேரில் இந்தியக் குடியரசுத் தலைவர்", "குடியரசுத் தலைவர் ஒப்புதலுடன் நாடாளுமன்ற இரு அவைகள்"],
          ["காலம் / தொடர்", "நாடாளுமன்ற இடைவேளையின் போது மட்டுமே பிறப்பிக்கப்படும்", "நாடாளுமன்றக் கூட்டத்தொடரின் போது இயற்றப்படும்"],
          ["ஆயுள் / செல்லுபடி", "தற்காலிகமானது (ஒப்புதல் பெறாவிட்டால் அதிகபட்சம் 6 மாதங்கள் + 6 வாரங்கள்)", "நிரந்தரமானது (ரத்து செய்யப்படும் வரை அல்லது திருத்தப்படும் வரை)"],
          ["அரசியலமைப்பு திருத்தம்", "அரசியலமைப்பைத் திருத்த முடியாது", "அரசியலமைப்பைத் திருத்த முடியும் (உறுப்பு 368-ன் கீழ்)"]
        ]
      },
      {
        "id": "tbl_summon_prorogue_dissolve",
        "title_en": "7. Summoning vs Prorogation vs Dissolution vs Adjournment",
        "title_ta": "7. கூட்டுதல் vs ஒத்திவைத்தல் vs கலைத்தல் vs அவை ஒத்திவைப்பு",
        "headers_en": ["Action", "Authority", "Effect on Session / House", "Effect on Pending Bills"],
        "headers_ta": ["நடவடிக்கை", "அதிகார அமைப்பு", "தொடர் / அவை மீதான விளைவு", "நிலுவை மசோதாக்கள் மீதான விளைவு"],
        "rows_en": [
          ["Summoning (கூட்டுதல்)", "President (Art 85)", "Calls the House to meet", "No effect"],
          ["Prorogation (கூட்டத் தொடர் முடிப்பு)", "President (Art 85)", "Terminates a SESSION of Parliament", "Does NOT lapse pending bills"],
          ["Dissolution (அவைக் கலைப்பு)", "President (Art 85)", "Ends the LIFE of Lok Sabha completely", "Pending bills in LS lapse (subject to Art 107 rules)"],
          ["Adjournment (அவை இடைநிறுத்தம்)", "Presiding Officer (Speaker/Chairman)", "Terminates a SITTING for hours/days", "Does NOT lapse pending bills"]
        ],
        "rows_ta": [
          ["Summoning (கூட்டுதல்)", "குடியரசுத் தலைவர் (உறுப்பு 85)", "அவையைக் கூட்ட அழைப்பு விடுக்கிறது", "விளைவு இல்லை"],
          ["Prorogation (கூட்டத் தொடர் முடிப்பு)", "குடியரசுத் தலைவர் (உறுப்பு 85)", "நாடாளுமன்றக் கூட்டத் தொடரை முடிவுக்குக் கொண்டுவருகிறது", "நிலுவை மசோதாக்கள் காலாவதியாகாது"],
          ["Dissolution (அவைக் கலைப்பு)", "குடியரசுத் தலைவர் (உறுப்பு 85)", "மக்களவையின் ஆயுளை முழுமையாக முடிவுக்குக் கொண்டுவருகிறது", "மக்களவையில் நிலுவையிலுள்ள மசோதாக்கள் காலாவதியாகும்"],
          ["Adjournment (அவை இடைநிறுத்தம்)", "தலைமை அதிகாரி (சபாநாயகர்/தலைவர்)", "அமர்வை சில மணிநேரம்/நாட்களுக்கு இடைநிறுத்துகிறது", "நிலுவை மசோதாக்கள் காலாவதியாகாது"]
        ]
      },
      {
        "id": "tbl_pres_and_com",
        "title_en": "8. President and Council of Ministers (Article 74 Amendments)",
        "title_ta": "8. குடியரசுத் தலைவர் மற்றும் அமைச்சரவை (உறுப்பு 74 திருத்தங்கள்)",
        "headers_en": ["Constitutional Phase", "Provision / Rule on Advice", "President's Discretion"],
        "headers_ta": ["அரசியலமைப்பு கட்டம்", "ஆலோசனை மீதான விதி", "குடியரசுத் தலைவரின் விருப்பம்"],
        "rows_en": [
          ["Original Constitution (1950)", "Art 74 stated CoM to aid and advise President", "Implicitly bound by convention"],
          ["42nd CAA 1976 (Indira Gandhi Govt)", "Made Cabinet advice strictly BINDING on President", "Zero discretion to return advice"],
          ["44th CAA 1978 (Janata Party Govt)", "Added proviso: President may require CoM to reconsider advice ONCE", "Can return advice ONCE for reconsideration (re-sent advice is binding)"]
        ],
        "rows_ta": [
          ["அசல் அரசியலமைப்பு (1950)", "குடியரசுத் தலைவருக்கு உதவி & ஆலோசனை வழங்க அமைச்சரவை இருந்தது", "மரபுப்படி மறைமுகமாகக் கட்டுப்பட்டவர்"],
          ["42வது திருத்தம் 1976 (இந்திரா காந்தி அரசு)", "அமைச்சரவை ஆலோசனையைக் கண்டிப்பான கட்டாயமாக்கியது (BINDING)", "ஆலோசனையைத் திருப்புவதற்குச் சுழியம் விருப்பம்"],
          ["44வது திருத்தம் 1978 (ஜனதா கட்சி அரசு)", "நிபந்தனை சேர்க்கப்பட்டது: ஆலோசனையை ஒருமுறை மறுபரிசீலனை செய்யக் கோரலாம்", "ஆலோசனையை ஒருமுறை மறுபரிசீலனைக்கு அனுப்பலாம் (மீண்டும் அனுப்பினால் கட்டாயம்)"]
        ]
      },
      {
        "id": "tbl_de_jure_vs_de_facto",
        "title_en": "9. De Jure Executive (President) vs De Facto Executive (Prime Minister)",
        "title_ta": "9. சட்டப்பூர்வ நிர்வாகி (குடியரசுத் தலைவர்) vs உண்மையான நிர்வாகி (பிரதமர்)",
        "headers_en": ["Feature", "De Jure Executive (President)", "De Facto Executive (Prime Minister)"],
        "headers_ta": ["அம்சம்", "சட்டப்பூர்வ நிர்வாகி (குடியரசுத் தலைவர்)", "உண்மையான நிர்வாகி (பிரதமர்)"],
        "rows_en": [
          ["Constitutional Title", "Head of the State (Art 52)", "Head of the Government (Art 74/75)"],
          ["Authority Source", "Formal constitutional powers (Art 53)", "Political majority in Lok Sabha"],
          ["Actual Decision Power", "Acts on aid and advice of Cabinet", "Directs Cabinet decisions & policy"],
          ["Accountability to LS", "Not directly accountable to Lok Sabha", "Directly accountable to Lok Sabha (Collective Responsibility)"]
        ],
        "rows_ta": [
          ["அரசியலமைப்பு தலைப்பு", "நாட்டின் தலைவர் (உறுப்பு 52)", "அரசாங்கத்தின் தலைவர் (உறுப்புகள் 74/75)"],
          ["அதிகார மூலாதாரம்", "முறைசார் அரசியலமைப்பு அதிகாரங்கள் (உறுப்பு 53)", "மக்களவையில் அரசியல் பெரும்பான்மை"],
          ["உண்மையான முடிவு அதிகாரம்", "அமைச்சரவையின் உதவி & ஆலோசனையின் பேரில் செயல்படுகிறார்", "அமைச்சரவை முடிவுகள் & கொள்கையை இயக்குகிறார்"],
          ["மக்களவைக்குப் பொறுப்பு", "மக்களவைக்கு நேரடியாகப் பொறுப்பல்ல", "மக்களவைக்கு நேரடியாகப் பொறுப்பானவர் (கூட்டுப் பொறுப்பு)"]
        ]
      },
      {
        "id": "tbl_pres_vs_gov_powers",
        "title_en": "10. President vs Governor (Important Powers Comparison)",
        "title_ta": "10. குடியரசுத் தலைவர் vs ஆளுநர் (முக்கிய அதிகாரங்கள் ஒப்பீடு)",
        "headers_en": ["Power Domain", "President of India", "State Governor"],
        "headers_ta": ["அதிகாரத் துறை", "இந்தியக் குடியரசுத் தலைவர்", "மாநில ஆளுநர்"],
        "rows_en": [
          ["Ordinance Power", "Article 123 (Parliament Recess)", "Article 213 (State Legislature Recess)"],
          ["Pardoning Power", "Article 72 (Includes Court Martial & Death Sentence)", "Article 161 (Excludes Court Martial & Death Sentence Pardon)"],
          ["Constitutional Discretion", "NO explicit constitutional discretion mentioned", "HAS explicit constitutional discretion (Art 163(1))"],
          ["Veto on State Bills", "Final assent/withholding on reserved State Bills (Art 201)", "Can reserve State Bills for President's consideration (Art 200)"]
        ],
        "rows_ta": [
          ["அவசரச் சட்ட அதிகாரம்", "உறுப்பு 123 (நாடாளுமன்ற இடைவேளை)", "உறுப்பு 213 (மாநில சட்டமன்ற இடைவேளை)"],
          ["மன்னிப்பளிக்கும் அதிகாரம்", "உறுப்பு 72 (ராணுவ நீதிமன்றம் & மரண தண்டனை அடங்கும்)", "உறுப்பு 161 (ராணுவ நீதிமன்றம் & மரண தண்டனை மன்னிப்பு விலக்கு)"],
          ["அரசியலமைப்பு விருப்ப அதிகாரம்", "வெளிப்படையான அரசியலமைப்பு விருப்ப அதிகாரம் குறிப்பிடப்படவில்லை", "வெளிப்படையான அரசியலமைப்பு விருப்ப அதிகாரம் உண்டு (உறுப்பு 163(1))"],
          ["மாநில மசோதாக்கள் மீதான வீட்டோ", "ஒதுக்கப்பட்ட மாநில மசோதாக்கள் மீது இறுதி ஒப்புதல்/நிறுத்தம் (உறுப்பு 201)", "மாநில மசோதாக்களைக் குடியரசுத் தலைவர் பரிசீலனைக்கு ஒதுக்கலாம் (உறுப்பு 200)"]
        ]
      }
    ],
    "mind_map": [
      {
        "title": "President of India (Powers & Functions - Part 2)",
        "short_label": "President Powers",
        "children": [
          {
            "title": "1. Executive Powers",
            "short_label": "Executive",
            "children": [
              {
                "title": "Article 53 & 77: All executive actions in President's name",
                "short_label": "Art 53 Exec Name"
              },
              {
                "title": "Appointments: PM, Ministers, AG (Art 76), CAG (Art 148), CEC (Art 324), Governors, UPSC",
                "short_label": "Appointments"
              },
              {
                "title": "Article 78: Right to be informed by PM on Union administration",
                "short_label": "Art 78 Info"
              }
            ]
          },
          {
            "title": "2. Legislative Powers & Veto",
            "short_label": "Legislative & Veto",
            "children": [
              {
                "title": "Art 85: Summon, Prorogue Parliament & Dissolve Lok Sabha",
                "short_label": "Art 85 Sessions"
              },
              {
                "title": "Art 87: Special Address at 1st session after General Election & 1st session of year",
                "short_label": "Art 87 Address"
              },
              {
                "title": "Art 80: Nominates 12 RS members (Art, Lit, Sci, Social Service)",
                "short_label": "Art 80 Nominations"
              },
              {
                "title": "Art 108: Summons Joint Sitting of Parliament",
                "short_label": "Art 108 Joint Sitting"
              },
              {
                "title": "Veto Types: Absolute (withhold), Suspensive (return once), Pocket (keep pending - 1986 Post Office Bill)",
                "short_label": "Veto Types"
              },
              {
                "title": "Bill Assent (Art 111 & 368): Money Bills cannot be returned; Amendment Bill assent MANDATORY (24th CAA)",
                "short_label": "Bill Assent Rules"
              }
            ]
          },
          {
            "title": "3. Ordinance Power (Article 123)",
            "short_label": "Ordinance Art 123",
            "children": [
              {
                "title": "Promulgated during recess of Parliament on Cabinet advice",
                "short_label": "Recess Condition"
              },
              {
                "title": "Equal force to Act of Parliament (Temporary law)",
                "short_label": "Equal Force"
              },
              {
                "title": "Ceases 6 weeks from Parliamentary reassembly (Max life: 6 months + 6 weeks)",
                "short_label": "6 Weeks Rule"
              },
              {
                "title": "DC Wadhwa (1987) & KK Singh (2017): Re-promulgation is unconstitutional fraud",
                "short_label": "Wadhwa Ruling"
              }
            ]
          },
          {
            "title": "4. Financial & Judicial Powers",
            "short_label": "Financial & Judicial",
            "children": [
              {
                "title": "Financial: Prior recommendation for Money Bills (Art 117), Lays Budget (Art 112), Contingency Fund (Art 267), Finance Commission (Art 280)",
                "short_label": "Financial Powers"
              },
              {
                "title": "Judicial: Appoints SC/HC Judges (Art 124/217); Advisory opinion from SC (Art 143 - non-binding)",
                "short_label": "Judicial Appointments"
              },
              {
                "title": "Article 72 Pardoning Power (5 Terms): Pardon, Reprieve, Respite, Remission, Commutation (Covers Court Martial & Death Sentences)",
                "short_label": "Art 72 Pardon"
              }
            ]
          },
          {
            "title": "5. Diplomatic, Military & Art 74",
            "short_label": "Diplomatic & Art 74",
            "children": [
              {
                "title": "Diplomatic: Treaties in President's name; sends/receives ambassadors",
                "short_label": "Diplomatic"
              },
              {
                "title": "Military: Supreme Commander of Armed Forces (Art 53(2)); appoints Service Chiefs",
                "short_label": "Military Commander"
              },
              {
                "title": "Article 74: Cabinet advice BINDING (42nd CAA 1976); can return ONCE for reconsideration (44th CAA 1978)",
                "short_label": "Art 74 Binding Advice"
              }
            ]
          }
        ]
      }
    ],
    "tnpsc_traps": [
      {
        "title": "1. Money Bill vs Ordinary Bill Return Trap (பண மசோதா vs சாதாரண மசோதா திரும்புதல் பொறி)",
        "points": {
          "en": [
            "TRAP: Statement claiming President can return a Money Bill for reconsideration.",
            "FACT: President CANNOT return a Money Bill for reconsideration! He can return an Ordinary Bill ONCE under Article 111."
          ],
          "ta": [
            "பொறி: பண மசோதாவைக் குடியரசுத் தலைவர் மறுபரிசீலனைக்குத் திருப்பி அனுப்பலாம் எனக் கூறும் கூற்று.",
            "உண்மை: பண மசோதாவைக் குடியரசுத் தலைவர் மறுபரிசீலனைக்குத் திருப்பி அனுப்ப முடியாது! உறுப்பு 111-ன் கீழ் சாதாரண மசோதாவை ஒருமுறை மட்டுமே திருப்பி அனுப்ப முடியும்."
          ]
        }
      },
      {
        "title": "2. Constitutional Amendment Bill Assent Trap (அரசியலமைப்பு திருத்த மசோதா ஒப்புதல் பொறி)",
        "points": {
          "en": [
            "TRAP: Believing President has veto power over Constitutional Amendment Bills under Article 368.",
            "FACT: Under the 24th Constitutional Amendment Act 1971, it is MANDATORY for the President to give assent to a Constitutional Amendment Bill!"
          ],
          "ta": [
            "பொறி: உறுப்பு 368-ன் கீழ் அரசியலமைப்பு திருத்த மசோதாக்கள் மீது குடியரசுத் தலைவருக்கு வீட்டோ அதிகாரம் உண்டு என நம்புவது.",
            "உண்மை: 1971-ன் 24வது அரசியலமைப்பு திருத்தச் சட்டத்தின் கீழ், அரசியலமைப்பு திருத்த மசோதாவிற்குச் சான்றளிப்பது குடியரசுத் தலைவருக்குக் கட்டாயமாகும்!"
          ]
        }
      },
      {
        "title": "3. Qualified Veto Absence in India Trap (இந்தியாவில் தகுதிவாய்ந்த வீட்டோ இல்லாத நிலை பொறி)",
        "points": {
          "en": [
            "TRAP: Option stating that Indian President possesses a Qualified Veto.",
            "FACT: Qualified Veto operates in the USA (overridden by 2/3rd special majority). It DOES NOT exist in India!"
          ],
          "ta": [
            "பொறி: இந்தியக் குடியரசுத் தலைவருக்குத் தகுதிவாய்ந்த வீட்டோ உண்டு எனக் கூறும் தெரிவு.",
            "உண்மை: தகுதிவாய்ந்த வீட்டோ அமெரிக்காவில் செயல்படுகிறது (2/3 பங்கு சிறப்பு பெரும்பான்மையால் முறியடிக்கப்படும்). அது இந்தியாவில் இல்லை!"
          ]
        }
      },
      {
        "title": "4. Article 123 Ordinance Time Limit Trap (உறுப்பு 123 அவசரச் சட்ட கால வரம்புப் பொறி)",
        "points": {
          "en": [
            "TRAP: Thinking an Ordinance ceases 6 months after reassembly of Parliament.",
            "FACT: An Ordinance ceases to operate at the expiry of SIX WEEKS from the reassembly of Parliament (Max life = 6 months + 6 weeks)."
          ],
          "ta": [
            "பொறி: நாடாளுமன்றம் மீண்டும் கூடிய 6 மாதங்களுக்குப் பிறகே அவசரச் சட்டம் செயலிழக்கும் என நினைப்பது.",
            "உண்மை: நாடாளுமன்றம் மீண்டும் கூடிய தேதியிலிருந்து 6 வாரங்கள் முடிவடையும் போது அவசரச் சட்டம் செயலிழந்துவிடும் (அதிகபட்ச ஆயுள் = 6 மாதங்கள் + 6 வாரங்கள்)."
          ]
        }
      },
      {
        "title": "5. Article 72 vs 161 Death Sentence Pardon Trap (உறுப்பு 72 vs 161 மரண தண்டனை மன்னிப்புப் பொறி)",
        "points": {
          "en": [
            "TRAP: Claiming a State Governor can pardon a death sentence awarded under State law.",
            "FACT: ONLY the President of India (Article 72) can grant absolute PARDON for a death sentence. Governor (Article 161) CANNOT pardon a death sentence!"
          ],
          "ta": [
            "பொறி: மாநிலச் சட்டத்தின் கீழ் விதிக்கப்பட்ட மரண தண்டனையை மாநில ஆளுநர் மன்னிக்க முடியும் என்ற கூற்று.",
            "உண்மை: இந்தியக் குடியரசுத் தலைவர் (உறுப்பு 72) மட்டுமே மரண தண்டனைக்கு முழு மன்னிப்பு (Pardon) அளிக்க முடியும். ஆளுநரால் (உறுப்பு 161) மரண தண்டனையை மன்னிக்க முடியாது!"
          ]
        }
      },
      {
        "title": "6. Remission vs Commutation Distinction Trap (தண்டனைக் குறைப்பு vs தண்டனை மாற்றம் வேறுபாட்டுப் பொறி)",
        "points": {
          "en": [
            "TRAP: Confusing Remission with Commutation under Article 72.",
            "FACT: Remission reduces the DURATION of punishment without changing its character (2 yrs RI -> 1 yr RI). Commutation substitutes punishment for a LIGHTER form (Death -> RI)."
          ],
          "ta": [
            "பொறி: உறுப்பு 72-ன் கீழ் Remission மற்றும் Commutation ஆகியவற்றை குழப்பிக் கொள்ளுதல்.",
            "உண்மை: Remission தண்டனையின் தன்மையை மாற்றாமல் கால அளவைக் குறைக்கிறது (2 ஆண்டுகள் கடுங்காவல் -> 1 ஆண்டு கடுங்காவல்). Commutation தண்டனையை லேசான வடிவத்திற்கு மாற்றுகிறது (மரண தண்டனை -> கடுங்காவல்)."
          ]
        }
      },
      {
        "title": "7. Summoning vs Adjournment Authority Trap (கூட்டுதல் vs அவை ஒத்திவைப்பு அதிகார அமைப்பின் பொறி)",
        "points": {
          "en": [
            "TRAP: Statement attributing Adjournment of Lok Sabha to the President.",
            "FACT: Summoning, Prorogation & Dissolution are done by the PRESIDENT (Art 85). Adjournment & Adjournment Sine Die are done by the PRESIDING OFFICER (Speaker/Chairman)!"
          ],
          "ta": [
            "பொறி: மக்களவையை ஒத்திவைப்பது (Adjournment) குடியரசுத் தலைவரின் செயல் எனக் கூறும் கூற்று.",
            "உண்மை: கூட்டுதல், கூட்டத் தொடர் முடிப்பு & கலைத்தல் குடியரசுத் தலைவரால் செய்யப்படுகின்றன (உறுப்பு 85). அவை ஒத்திவைப்பு & காலவரையறையின்றி ஒத்திவைப்பு தலைமை அதிகாரியால் (சபாநாயகர்/தலைவர்) செய்யப்படுகின்றன!"
          ]
        }
      },
      {
        "title": "8. Article 74 42nd vs 44th Amendment Reconsideration Trap (உறுப்பு 74 42வது vs 44வது திருத்தப் பொறி)",
        "points": {
          "en": [
            "TRAP: Saying President can return Cabinet advice multiple times for reconsideration.",
            "FACT: Under 44th CAA 1978, President can return Cabinet advice ONCE for reconsideration. If Cabinet re-sends the advice, President MUST accept it!"
          ],
          "ta": [
            "பொறி: அமைச்சரவை ஆலோசனையைக் குடியரசுத் தலைவர் பலமுறை மறுபரிசீலனைக்கு அனுப்பலாம் எனக் கூறுவது.",
            "உண்மை: 1978-ன் 44வது திருத்தத்தின் கீழ், குடியரசுத் தலைவர் ஆலோசனையை ஒருமுறை மட்டுமே மறுபரிசீலனைக்கு அனுப்ப முடியும். அமைச்சரவை மீண்டும் அனுப்பினால் குடியரசுத் தலைவர் அதை கட்டாயம் ஏற்க வேண்டும்!"
          ]
        }
      },
      {
        "title": "9. Budget Preparation Responsibility Trap (பட்ஜெட் தயாரிப்புப் பொறுப்புப் பொறி)",
        "points": {
          "en": [
            "TRAP: Believing President personally drafts the Union Budget.",
            "FACT: Union Budget is prepared by the Finance Ministry (Dept of Economic Affairs). Under Article 112, President causes it to be laid before Parliament."
          ],
          "ta": [
            "பொறி: மத்திய பட்ஜெட்டைக் குடியரசுத் தலைவரே நேரில் தயாரிக்கிறார் என நம்புவது.",
            "உண்மை: மத்திய பட்ஜெட் நிதி அமைச்சகத்தால் (பொருளாதார விவகாரங்கள் துறை) தயாரிக்கப்படுகிறது. உறுப்பு 112-ன் கீழ் குடியரசுத் தலைவர் அதை நாடாளுமன்றத்தின் முன் சமர்ப்பிக்கச் செய்கிறார்."
          ]
        }
      },
      {
        "title": "10. Article 143 Advisory Opinion Binding Trap (உறுப்பு 143 ஆலோசனை அதிகாரம் பிணைப்புப் பொறி)",
        "points": {
          "en": [
            "TRAP: Option stating Supreme Court's advisory opinion under Article 143 is binding on President.",
            "FACT: Opinion given by Supreme Court under Article 143 is purely ADVISORY and NOT binding on the President."
          ],
          "ta": [
            "பொறி: உறுப்பு 143-ன் கீழ் உச்ச நீதிமன்றம் வழங்கும் ஆலோசனை குடியரசுத் தலைவரைக் கட்டுப்படுத்தும் எனக் கூறும் தெரிவு.",
            "உண்மை: உறுப்பு 143-ன் கீழ் உச்ச நீதிமன்றம் வழங்கும் கருத்து தூய ஆலோசனையே தவிரக் குடியரசுத் தலைவரைக் கட்டுப்படுத்தாது."
          ]
        }
      }
    ],
    "important_facts": {
      "en": [
        "Article 53 & 77: All executive actions of the Union Government are formally taken in President's name.",
        "Article 75 & 76: President appoints PM, Union Ministers, and Attorney General of India (AG holds office during President's pleasure).",
        "Article 78: PM has a constitutional duty to furnish all administrative & legislative info to President.",
        "Article 79: Parliament consists of President, Rajya Sabha, and Lok Sabha.",
        "Article 85: President summons & prorogues Parliament, and dissolves Lok Sabha on Cabinet advice.",
        "Article 87: President delivers special address at 1st session after General Election & 1st session of each year.",
        "Article 80: President nominates 12 members to Rajya Sabha for Art, Literature, Science, and Social Service.",
        "104th CAA 2019 abolished nomination of 2 Anglo-Indians to Lok Sabha.",
        "Article 108: President summons Joint Sitting of Parliament (presided by LS Speaker).",
        "Article 111: Governs assent to bills. Ordinary bills returned once; Money bills cannot be returned; Amendment bills assent MANDATORY (24th CAA 1971).",
        "Absolute Veto = withholding assent; Suspensive Veto = returning once; Pocket Veto = keeping pending indefinitely (1986 Post Office Bill). Qualified Veto does NOT exist in India.",
        "Article 123: Ordinance promulgated during Parliament recess. Ceases 6 weeks from reassembly (Max life: 6 months + 6 weeks). DC Wadhwa (1987) banned re-promulgation.",
        "Article 112: Annual Financial Statement (Budget) presented by President's direction. Money Bills require prior recommendation (Art 117).",
        "Article 267: President controls Contingency Fund of India; Article 280: Constitutes Finance Commission every 5 years.",
        "Article 124 & 217: President appoints Supreme Court and High Court Judges.",
        "Article 143: Seeking non-binding advisory opinion from Supreme Court.",
        "Article 72 Pardoning Power (5 terms): Pardon (full release), Reprieve (stay), Respite (special facts), Remission (duration reduced), Commutation (lighter form).",
        "Only President can pardon death sentences and Court Martial sentences (Governor under Art 161 cannot!).",
        "Article 74: Cabinet advice binding (42nd CAA 1976); President can return advice ONCE for reconsideration (44th CAA 1978)."
      ],
      "ta": [
        "உறுப்புகள் 53 & 77: மத்திய அரசின் அனைத்து நிர்வாக நடவடிக்கைகளும் முறைப்படி குடியரசுத் தலைவர் பெயரிலேயே எடுக்கப்படுகின்றன.",
        "உறுப்புகள் 75 & 76: குடியரசுத் தலைவர் பிரதமர், அமைச்சர்கள் மற்றும் அட்டர்னி ஜெனரலை நியமிக்கிறார் (ஏஜி குடியரசுத் தலைவரின் விருப்பம் உள்ளவரை பதவி வகிப்பார்).",
        "உறுப்பு 78: அனைத்து நிர்வாக & சட்டமன்றத் தகவல்களையும் குடியரசுத் தலைவருக்கு வழங்க வேண்டியது பிரதமரின் அரசியலமைப்புக் கடமையாகும்.",
        "உறுப்பு 79: நாடாளுமன்றம் குடியரசுத் தலைவர், மாநிலங்களவை மற்றும் மக்களவையை உள்ளடக்கியது.",
        "உறுப்பு 85: குடியரசுத் தலைவர் நாடாளுமன்றத்தைக் கூட்டுகிறார், ஒத்திவைக்கிறார், அமைச்சரவை ஆலோசனையின் பேரில் மக்களவையைக் கலைக்கிறார்.",
        "உறுப்பு 87: பொதுத் தேர்தலுக்குப் பிறகான 1வது தொடரிலும் ஒவ்வொரு ஆண்டின் 1வது தொடரிலும் குடியரசுத் தலைவர் சிறப்புரையாற்றுகிறார்.",
        "உறுப்பு 80: கலை, இலக்கியம், அறிவியல், சமூக சேவைக்காக 12 உறுப்பினர்களை மாநிலங்களவைக்குக் குடியரசுத் தலைவர் நியமிக்கிறார்.",
        "104வது திருத்தம் 2019 மக்களவைக்கு 2 ஆங்கிலோ-இந்தியர்கள் நியமனத்தை ரத்து செய்தது.",
        "உறுப்பு 108: நாடாளுமன்றக் கூட்டுக் கூட்டத்தைக் குடியரசுத் தலைவர் கூட்டுகிறார் (சபாநாயகர் தலைமை தாங்குவார்).",
        "உறுப்பு 111: மசோதா ஒப்புதலை நிர்வகிக்கிறது. சாதாரண மசோதா ஒருமுறை திரும்பும்; பண மசோதா திரும்ப முடியாது; திருத்த மசோதா ஒப்புதல் கட்டாயம் (24வது திருத்தம் 1971).",
        "முழுமையான வீட்டோ = ஒப்புதலை நிறுத்துவது; இடைநிறுத்த வீட்டோ = ஒருமுறை திருப்புவது; பாக்கெட் வீட்டோ = காலவரையின்றி நிறுத்துவது (1986 தபால் மசோதா). தகுதிவாய்ந்த வீட்டோ இந்தியாவில் இல்லை.",
        "உறுப்பு 123: நாடாளுமன்ற இடைவேளையின் போது அவசரச் சட்டம். மீண்டும் கூடிய 6 வாரங்களில் செயலிழக்கும் (அதிகபட்ச ஆயுள்: 6 மாதங்கள் + 6 வாரங்கள்). டி.சி. வாத்வா (1987) மீண்டும் பிறப்பிப்பதைத் தடை செய்தது.",
        "உறுப்பு 112: பட்ஜெட் குடியரசுத் தலைவர் வழிகாட்டுதலின் படி சமர்ப்பிக்கப்படுகிறது. பண மசோதாக்களுக்கு முன் பரிந்துரை தேவை (உறுப்பு 117).",
        "உறுப்பு 267: குடியரசுத் தலைவர் அவசரகால நிதியைக் கட்டுப்படுத்துகிறார்; உறுப்பு 280: 5 ஆண்டுகளுக்கு ஒருமுறை நிதி ஆணையத்தை அமைக்கிறார்.",
        "உறுப்புகள் 124 & 217: குடியரசுத் தலைவர் உச்ச/உயர் நீதிமன்ற நீதிபதிகளை நியமிக்கிறார்.",
        "உறுப்பு 143: உச்ச நீதிமன்றத்திடமிருந்து கட்டுப்படுத்தாத ஆலோசனையைப் பெறுதல்.",
        "உறுப்பு 72 மன்னிப்பளிக்கும் அதிகாரம் (5 சொற்கள்): Pardon (முழு விடுதலை), Reprieve (ஒத்திவைப்பு), Respite (சிறப்பு காரணம்), Remission (காலக் குறைப்பு), Commutation (லேசான வடிவம்).",
        "குடியரசுத் தலைவர் மட்டுமே மரண தண்டனை & ராணுவ நீதிமன்ற தண்டனைகளை மன்னிக்க முடியும் (உறுப்பு 161 ஆளுநரால் முடியாது!).",
        "உறுப்பு 74: அமைச்சரவை ஆலோசனை கட்டாயமானது (42வது திருத்தம் 1976); குடியரசுத் தலைவர் ஆலோசனையை ஒருமுறை மறுபரிசீலனைக்கு அனுப்பலாம் (44வது திருத்தம் 1978)."
      ]
    },
    "quick_revision": {
      "en": [
        "Executive Power (Art 53/77): Actions taken in President's name. Appoints PM, Ministers, AG, CAG, CEC, Governors & Commissions on Cabinet advice.",
        "Article 78: PM duty to inform President of Union administration and legislative proposals.",
        "Legislative Powers (Art 79/85/87): Integral part of Parliament. Summons, prorogues & dissolves LS. Special address at budget session start. Nominates 12 RS members (Art 80). Summons Joint Sitting (Art 108).",
        "Bill Assent (Art 111 & 368): Ordinary bill returned once (re-passage forces assent). Money bill cannot be returned. Constitutional Amendment bill assent MANDATORY under 24th CAA 1971.",
        "Veto Powers: Absolute Veto (withhold assent); Suspensive Veto (return once, simple majority override); Pocket Veto (indefinite pending - 1986 Post Office Bill). Qualified Veto DOES NOT exist in India.",
        "Ordinance Power (Art 123): Promulgated during Parliament recess on Cabinet advice. Max life = 6 months + 6 weeks. Ceases 6 weeks from reassembly. Re-promulgation banned (DC Wadhwa 1987).",
        "Financial Powers: Prior recommendation for Money Bills (Art 117) & Grants (Art 113). Lays Budget (Art 112). Controls Contingency Fund (Art 267). Sets up Finance Commission (Art 280).",
        "Judicial Powers: Appoints SC/HC Judges (Arts 124/217). Advisory opinion from SC (Art 143 - non-binding).",
        "Article 72 Pardoning Power: Pardon (full release), Reprieve (stay), Respite (special facts), Remission (duration reduced), Commutation (lighter form). Covers Court Martial & Death sentences.",
        "President (Art 72) vs Governor (Art 161): Only President pardons death sentences and Court Martial sentences.",
        "Article 74: Cabinet advice binding (42nd CAA 1976); President can return advice ONCE for reconsideration (44th CAA 1978)."
      ],
      "ta": [
        "நிர்வாக அதிகாரம் (உறுப்புகள் 53/77): குடியரசுத் தலைவர் பெயரில் நடவடிக்கைகள். அமைச்சரவை ஆலோசனையின் பேரில் பிரதமர், அமைச்சர்கள், ஏஜி, சிஏஜி, தலைமை தேர்தல் ஆணையர், ஆளுநர்களை நியமிக்கிறார்.",
        "உறுப்பு 78: ஒன்றிய நிர்வாகம் & சட்ட திட்டங்களை குடியரசுத் தலைவருக்கு தெரிவிக்க வேண்டியது பிரதமரின் கடமை.",
        "சட்டமன்ற அதிகாரங்கள் (உறுப்புகள் 79/85/87): நாடாளுமன்றத்தின் பகுதி. கூட்டுதல், ஒத்திவைத்தல் & மக்களவையைக் கலைத்தல். பட்ஜெட் தொடக்கத்தில் சிறப்புரை. 12 மாநிலங்களவை உறுப்பினர்களை நியமித்தல் (உறுப்பு 80). கூட்டுக் கூட்டத்தைக் கூட்டுதல் (உறுப்பு 108).",
        "மசோதா ஒப்புதல் (உறுப்புகள் 111 & 368): சாதாரண மசோதா ஒருமுறை திரும்பும் (மீண்டும் நிறைவேற்றினால் ஒப்புதல் கட்டாயம்). பண மசோதா திரும்ப முடியாது. அரசியலமைப்பு திருத்த மசோதா ஒப்புதல் 24வது திருத்தம் 1971-ன் கீழ் கட்டாயம்.",
        "வீட்டோ அதிகாரங்கள்: முழுமையான வீட்டோ (ஒப்புதலை நிறுத்துவது); இடைநிறுத்த வீட்டோ (ஒருமுறை திருப்புவது); பாக்கெட் வீட்டோ (காலவரையின்றி நிறுத்துவது - 1986 தபால் மசோதா). தகுதிவாய்ந்த வீட்டோ இந்தியாவில் இல்லை.",
        "அவசரச் சட்ட அதிகாரம் (உறுப்பு 123): நாடாளுமன்ற இடைவேளையில் அமைச்சரவை ஆலோசனையின் பேரில் பிறப்பிக்கப்படும். அதிகபட்ச ஆயுள் = 6 மாதங்கள் + 6 வாரங்கள். மீண்டும் கூடிய 6 வாரங்களில் செயலிழக்கும். மீண்டும் பிறப்பிப்பது தடை செய்யப்பட்டது (டி.சி. வாத்வா 1987).",
        "நிதி அதிகாரங்கள்: பண மசோதாக்கள் (உறுப்பு 117) & மானியங்களுக்கு முன் பரிந்துரை. பட்ஜெட்டை (உறுப்பு 112) சமர்ப்பிக்கிறார். அவசரகால நிதியைக் (உறுப்பு 267) கட்டுப்படுத்துகிறார். நிதி ஆணையத்தை (உறுப்பு 280) அமைக்கிறார்.",
        "நீதித் துறை அதிகாரங்கள்: உச்ச/உயர் நீதிமன்ற நீதிபதிகளை நியமிக்கிறார் (உறுப்புகள் 124/217). உச்ச நீதிமன்றத்திடமிருந்து ஆலோசனை (உறுப்பு 143 - கட்டுப்படுத்தாது).",
        "உறுப்பு 72 மன்னிப்பளிக்கும் அதிகாரம்: Pardon (முழு விடுதலை), Reprieve (ஒத்திவைப்பு), Respite (சிறப்பு காரணம்), Remission (காலக் குறைப்பு), Commutation (லேசான வடிவம்). ராணுவ நீதிமன்றம் & மரண தண்டனைகளை உள்ளடக்கியது.",
        "குடியரசுத் தலைவர் (உறுப்பு 72) vs ஆளுநர் (உறுப்பு 161): குடியரசுத் தலைவர் மட்டுமே மரண தண்டனை & ராணுவ நீதிமன்ற தண்டனைகளை மன்னிக்கிறார்.",
        "உறுப்பு 74: அமைச்சரவை ஆலோசனை கட்டாயமானது (42வது திருத்தம் 1976); குடியரசுத் தலைவர் ஆலோசனையை ஒருமுறை மறுபரிசீலனைக்கு அனுப்பலாம் (44வது திருத்தம் 1978)."
      ]
    },
    "revision_cards": [
      {
        "id": "card_1",
        "front_en": "Under which Article are all executive actions of the Union Government taken in the President's name?",
        "front_ta": "மத்திய அரசின் அனைத்து நிர்வாக நடவடிக்கைகளும் எந்த உறுப்பின் கீழ் குடியரசுத் தலைவர் பெயரில் எடுக்கப்படுகின்றன?",
        "back_en": "Article 77(1) (read with Article 53).",
        "back_ta": "உறுப்பு 77(1) (உறுப்பு 53 உடன் சேர்த்து படிக்க)."
      },
      {
        "id": "card_2",
        "front_en": "Which Constitutional Amendment Act made Presidential assent mandatory for Constitutional Amendment Bills?",
        "front_ta": "அரசியலமைப்பு திருத்த மசோதாக்களுக்குக் குடியரசுத் தலைவரின் ஒப்புதலைக் கட்டாயமாக்கிய அரசியலமைப்பு திருத்தச் சட்டம் எது?",
        "back_en": "24th Constitutional Amendment Act, 1971.",
        "back_ta": "1971-ன் 24வது அரசியலமைப்பு திருத்தச் சட்டம்."
      },
      {
        "id": "card_3",
        "front_en": "Can the President return a Money Bill for reconsideration under Article 111?",
        "front_ta": "உறுப்பு 111-ன் கீழ் பண மசோதாவைக் குடியரசுத் தலைவர் மறுபரிசீலனைக்குத் திருப்பி அனுப்ப முடியுமா?",
        "back_en": "NO. A Money Bill CANNOT be returned for reconsideration by the President.",
        "back_ta": "இல்லை. பண மசோதாவைக் குடியரசுத் தலைவர் மறுபரிசீலனைக்குத் திருப்பி அனுப்ப முடியாது."
      },
      {
        "id": "card_4",
        "front_en": "Which Indian President exercised Pocket Veto on the Indian Post Office (Amendment) Bill in 1986?",
        "front_ta": "1986-ல் இந்திய தபால் அலுவலக (திருத்த) மசோதா மீது பாக்கெட் வீட்டோவைச் செலுத்திய இந்தியக் குடியரசுத் தலைவர் யார்?",
        "back_en": "President Giani Zail Singh.",
        "back_ta": "குடியரசுத் தலைவர் கியானி ஜெயில் சிங்."
      },
      {
        "id": "card_5",
        "front_en": "Does a Qualified Veto exist in the Indian Constitutional framework?",
        "front_ta": "இந்திய அரசியலமைப்பு அமைப்பில் தகுதிவாய்ந்த வீட்டோ (Qualified Veto) உள்ளதா?",
        "back_en": "NO. Qualified Veto operates in the USA, but DOES NOT exist in India.",
        "back_ta": "இல்லை. தகுதிவாய்ந்த வீட்டோ அமெரிக்காவில் செயல்படுகிறது, ஆனால் இந்தியாவில் இல்லை."
      },
      {
        "id": "card_6",
        "front_en": "What is the maximum life of an Ordinance promulgated by the President under Article 123?",
        "front_ta": "உறுப்பு 123-ன் கீழ் குடியரசுத் தலைவரால் பிறப்பிக்கப்படும் அவசரச் சட்டத்தின் அதிகபட்ச ஆயுள் என்ன?",
        "back_en": "6 Months and 6 Weeks (Must be laid before Parliament within 6 weeks from reassembly).",
        "back_ta": "6 மாதங்கள் மற்றும் 6 வாரங்கள் (மீண்டும் கூடிய 6 வாரங்களுக்குள் நாடாளுமன்றத்தின் முன் வைக்கப்பட வேண்டும்)."
      },
      {
        "id": "card_7",
        "front_en": "Under which landmark case did Supreme Court rule that re-promulgation of Ordinances is unconstitutional?",
        "front_ta": "அவசரச் சட்டங்களை மீண்டும் மீண்டும் பிறப்பிப்பது செல்லாது என உச்ச நீதிமன்றம் தீர்ப்பளித்த முக்கிய வழக்கு எது?",
        "back_en": "D.C. Wadhwa v. State of Bihar (1987) & Krishna Kumar Singh v. State of Bihar (2017).",
        "back_ta": "டி.சி. வாத்வா vs பீகார் மாநிலம் (1987) & கிருஷ்ண குமார் சிங் vs பீகார் மாநிலம் (2017)."
      },
      {
        "id": "card_8",
        "front_en": "Which Article governs the Supreme Court's Advisory Jurisdiction to the President?",
        "front_ta": "குடியரசுத் தலைவருக்கு உச்ச நீதிமன்றத்தின் ஆலோசனை அதிகார வரம்பை நிர்வகிக்கும் உறுப்பு எது?",
        "back_en": "Article 143 (Opinion is advisory and NOT binding on President).",
        "back_ta": "உறுப்பு 143 (கருத்து ஆலோசனையே தவிரக் குடியரசுத் தலைவரைக் கட்டுப்படுத்தாது)."
      },
      {
        "id": "card_9",
        "front_en": "What is the difference between Remission and Commutation under Article 72?",
        "front_ta": "உறுப்பு 72-ன் கீழ் Remission மற்றும் Commutation இடையே உள்ள வேறுபாடு என்ன?",
        "back_en": "Remission reduces sentence DURATION without changing character; Commutation substitutes punishment for a LIGHTER form.",
        "back_ta": "Remission தன்மையை மாற்றாமல் கால அளவைக் குறைக்கிறது; Commutation தண்டனையை லேசான வடிவத்திற்கு மாற்றுகிறது."
      },
      {
        "id": "card_10",
        "front_en": "Can a State Governor pardon a death sentence under Article 161?",
        "front_ta": "உறுப்பு 161-ன் கீழ் ஒரு மாநில ஆளுநர் மரண தண்டனையை மன்னிக்க முடியுமா?",
        "back_en": "NO. ONLY the President (Article 72) can grant absolute PARDON for a death sentence.",
        "back_ta": "இல்லை. இந்தியக் குடியரசுத் தலைவர் (உறுப்பு 72) மட்டுமே மரண தண்டனைக்கு முழு மன்னிப்பு (Pardon) அளிக்க முடியும்."
      },
      {
        "id": "card_11",
        "front_en": "How did 44th Constitutional Amendment Act 1978 modify Article 74 regarding Cabinet advice?",
        "front_ta": "1978-ன் 44வது அரசியலமைப்பு திருத்தச் சட்டம் அமைச்சரவை ஆலோசனை தொடர்பாக உறுப்பு 74-ஐ எவ்வாறு திருத்தியது?",
        "back_en": "Allowed President to return Cabinet advice ONCE for reconsideration; however, re-sent advice is strictly BINDING.",
        "back_ta": "அமைச்சரவை ஆலோசனையை ஒருமுறை மறுபரிசீலனைக்கு அனுப்ப அனுமதித்தது; இருப்பினும் மீண்டும் அனுப்பப்படும் ஆலோசனை கட்டாயமாகும்."
      },
      {
        "id": "card_12",
        "front_en": "Which Amendment abolished the nomination of 2 Anglo-Indians to the Lok Sabha?",
        "front_ta": "மக்களவைக்கு 2 ஆங்கிலோ-இந்தியர்கள் நியமனத்தை ரத்து செய்த திருத்தம் எது?",
        "back_en": "104th Constitutional Amendment Act, 2019.",
        "back_ta": "2019-ன் 104வது அரசியலமைப்பு திருத்தச் சட்டம்."
      }
    ]
  }
}

os.makedirs("data/notes/polity", exist_ok=True)
output_path = "data/notes/polity/president_part_2.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Successfully generated {output_path}!")
