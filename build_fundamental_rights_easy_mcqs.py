# -*- coding: utf-8 -*-
"""
Master Builder for Fundamental Rights – Easy 50 MCQs (Bilingual)
Subject: Indian Polity
Topic: Fundamental Rights
Type: Easy
Target Output: data/questions/polity/fundamental_rights_easy.json
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

questions = [
  # 1. Foundation & Magna Carta (Direct Factual) - Ans: B
  {
    "id": "FR_E_001",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Easy",
    "question_type": "Direct",
    "question": {
      "en": "Which Part of the Constitution of India is described as the 'Magna Carta of India'?",
      "ta": "இந்திய அரசியலமைப்பின் எந்தப் பகுதி 'இந்தியாவின் மகா சாசனம்' என்று விவரிக்கப்படுகிறது?"
    },
    "options": [
      { "id": "A", "en": "Part II (Articles 5 to 11)", "ta": "பகுதி II (உறுப்புகள் 5 முதல் 11)" },
      { "id": "B", "en": "Part III (Articles 12 to 35)", "ta": "பகுதி III (உறுப்புகள் 12 முதல் 35)" },
      { "id": "C", "en": "Part IV (Articles 36 to 51)", "ta": "பகுதி IV (உறுப்புகள் 36 முதல் 51)" },
      { "id": "D", "en": "Part IV-A (Article 51A)", "ta": "பகுதி IV-A (உறுப்பு 51A)" }
    ],
    "correct_answer": "B",
    "explanation": {
      "en": "Part III of the Constitution containing Articles 12 to 35 is described as the Magna Carta of India because it contains a comprehensive list of justiciable Fundamental Rights.",
      "ta": "அரசியலமைப்பின் பகுதி III (உறுப்புகள் 12 முதல் 35 வரை) நீதிமன்றத்தால் நிலைநிறுத்தக்கூடிய அடிப்படை உரிமைகளின் விரிவான பட்டியலைக் கொண்டுள்ளதால் 'இந்தியாவின் மகா சாசனம்' என அழைக்கப்படுகிறது."
    },
    "why_not_others": {
      "A": { "en": "Part II deals with Citizenship.", "ta": "பகுதி II குடியுரிமை பற்றியது." },
      "B": { "en": "Correct. Part III is the Magna Carta of India.", "ta": "சரி. பகுதி III இந்தியாவின் மகா சாசனம் ஆகும்." },
      "C": { "en": "Part IV deals with Directive Principles of State Policy.", "ta": "பகுதி IV அரசு நெறிமுறைக் கோட்பாடுகள் பற்றியது." },
      "D": { "en": "Part IV-A deals with Fundamental Duties.", "ta": "பகுதி IV-A அடிப்படை கடமைகள் பற்றியது." }
    },
    "tnpsc_tip": {
      "en": "Part III (Articles 12-35) was inspired by the US Constitution's Bill of Rights.",
      "ta": "பகுதி III (உறுப்புகள் 12-35) அமெரிக்க அரசியலமைப்பின் உரிமைகள் மசோதாவால் ஈர்க்கப்பட்டது."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Easy", "level": "TNPSC Group 1" }
  },

  # 2. Number of Original vs Present Rights (Direct Factual) - Ans: A
  {
    "id": "FR_E_002",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Easy",
    "question_type": "Direct",
    "question": {
      "en": "How many Fundamental Rights are currently guaranteed to citizens under Part III of the Constitution?",
      "ta": "அரசியலமைப்பின் பகுதி III-ன் கீழ் தற்சமயம் குடிமக்களுக்கு எத்தனை அடிப்படை உரிமைகள் உத்தரவாதம் அளிக்கப்பட்டுள்ளன?"
    },
    "options": [
      { "id": "A", "en": "Six (6)", "ta": "ஆறு (6)" },
      { "id": "B", "en": "Seven (7)", "ta": "ஏழு (7)" },
      { "id": "C", "en": "Eight (8)", "ta": "எட்டு (8)" },
      { "id": "D", "en": "Five (5)", "ta": "ஐந்து (5)" }
    ],
    "correct_answer": "A",
    "explanation": {
      "en": "Originally there were 7 Fundamental Rights. After the deletion of the Right to Property in 1978, there are currently 6 Fundamental Rights.",
      "ta": "ஆரம்பத்தில் 7 அடிப்படை உரிமைகள் இருந்தன. 1978-ல் சொத்துரிமை நீக்கப்பட்ட பிறகு, தற்சமயம் 6 அடிப்படை உரிமைகள் மட்டுமே உள்ளன."
    },
    "why_not_others": {
      "A": { "en": "Correct. Currently 6 Fundamental Rights exist.", "ta": "சரி. தற்சமயம் 6 அடிப்படை உரிமைகள் உள்ளன." },
      "B": { "en": "Incorrect. 7 was the original number before 1978.", "ta": "தவறு. 7 என்பது 1978-க்கு முந்தைய அசல் எண்ணிக்கை." },
      "C": { "en": "Incorrect. Never was eight.", "ta": "தவறு. எட்டு எப்போதுமே இல்லை." },
      "D": { "en": "Incorrect. Five is incorrect.", "ta": "தவறு. ஐந்து என்பது தவறானது." }
    },
    "tnpsc_tip": {
      "en": "Right to Property was deleted by the 44th Constitutional Amendment Act, 1978.",
      "ta": "சொத்துரிமை 1978-ன் 44வது அரசியலமைப்பு திருத்தச் சட்டத்தால் நீக்கப்பட்டது."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Easy", "level": "TNPSC Group 1" }
  },

  # 3. Article 12 State Definition (Direct Factual) - Ans: C
  {
    "id": "FR_E_003",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Easy",
    "question_type": "Direct",
    "question": {
      "en": "Which Article of the Constitution defines the term 'State' for the purposes of Part III?",
      "ta": "பகுதி III-ன் நோக்கங்களுக்காக 'அரசு' என்ற சொல்லை அரசியலமைப்பின் எந்த உறுப்பு வரையறுக்கிறது?"
    },
    "options": [
      { "id": "A", "en": "Article 11", "ta": "உறுப்பு 11" },
      { "id": "B", "en": "Article 13", "ta": "உறுப்பு 13" },
      { "id": "C", "en": "Article 12", "ta": "உறுப்பு 12" },
      { "id": "D", "en": "Article 14", "ta": "உறுப்பு 14" }
    ],
    "correct_answer": "C",
    "explanation": {
      "en": "Article 12 defines 'State' incorporating the Union Government/Parliament, State Governments/Legislatures, Local Authorities, and Other Authorities.",
      "ta": "உறுப்பு 12 மத்திய அரசு/நாடாளுமன்றம், மாநில அரசுகள்/சட்டமன்றங்கள், உள்ளாட்சி அமைப்புகள் மற்றும் இதர அமைப்புகளை உள்ளடக்கி 'அரசை' வரையறுக்கிறது."
    },
    "why_not_others": {
      "A": { "en": "Article 11 relates to citizenship regulation by Parliament.", "ta": "உறுப்பு 11 நாடாளுமன்றத்தின் குடியுரிமை ஒழுங்குமுறை பற்றியது." },
      "B": { "en": "Article 13 deals with laws inconsistent with fundamental rights.", "ta": "உறுப்பு 13 முரணான சட்டங்கள் பற்றியது." },
      "C": { "en": "Correct. Article 12 defines State.", "ta": "சரி. உறுப்பு 12 அரசை வரையறுக்கிறது." },
      "D": { "en": "Article 14 deals with Equality before Law.", "ta": "உறுப்பு 14 சட்டத்தின் முன் சமத்துவம் பற்றியது." }
    },
    "tnpsc_tip": {
      "en": "Article 12 definition applies specifically to Part III rights enforcement.",
      "ta": "உறுப்பு 12 வரையறை பகுதி III உரிமைகள் அமலாக்கத்திற்கு மட்டுமே பொருந்தும்."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Easy", "level": "TNPSC Group 1" }
  },

  # 4. Article 13 Judicial Review Basis (Article-based) - Ans: D
  {
    "id": "FR_E_004",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Easy",
    "question_type": "Article-based",
    "question": {
      "en": "Which Article provides the explicit constitutional basis for Judicial Review of laws violating Fundamental Rights in India?",
      "ta": "இந்தியாவில் அடிப்படை உரிமைகளை மீறும் சட்டங்களின் நீதித்துறை ஆய்வுக்கு வெளிப்படையான அரசியலமைப்பு அடிப்படையை வழங்கும் உறுப்பு எது?"
    },
    "options": [
      { "id": "A", "en": "Article 368", "ta": "உறுப்பு 368" },
      { "id": "B", "en": "Article 300A", "ta": "உறுப்பு 300A" },
      { "id": "C", "en": "Article 356", "ta": "உறுப்பு 356" },
      { "id": "D", "en": "Article 13", "ta": "உறுப்பு 13" }
    ],
    "correct_answer": "D",
    "explanation": {
      "en": "Article 13 declares that all laws inconsistent with or in derogation of Fundamental Rights shall be void, forming the bedrock of Judicial Review.",
      "ta": "அடிப்படை உரிமைகளுக்கு முரணான அனைத்துச் சட்டங்களும் செல்லாது என உறுப்பு 13 அறிவிக்கிறது, இதுவே நீதித்துறை ஆய்வின் அடித்தளமாகும்."
    },
    "why_not_others": {
      "A": { "en": "Article 368 deals with Constitutional Amendment procedure.", "ta": "உறுப்பு 368 அரசியலமைப்பு திருத்த நடைமுறை பற்றியது." },
      "B": { "en": "Article 300A deals with Right to Property.", "ta": "உறுப்பு 300A சொத்துரிமை பற்றியது." },
      "C": { "en": "Article 356 deals with President's Rule in States.", "ta": "உறுப்பு 356 மாநிலங்களில் குடியரசுத் தலைவர் ஆட்சி பற்றியது." },
      "D": { "en": "Correct. Article 13 is the foundation of Judicial Review.", "ta": "சரி. உறுப்பு 13 நீதித்துறை ஆய்வின் அடித்தளமாகும்." }
    },
    "tnpsc_tip": {
      "en": "Article 13 expressly empowers the Supreme Court (Art 32) and High Courts (Art 226) for judicial review.",
      "ta": "உறுப்பு 13 உச்ச நீதிமன்றம் (32) மற்றும் உயர் நீதிமன்றங்களுக்கு (226) நீதித்துறை ஆய்வு அதிகாரத்தை வெளிப்படையாக வழங்குகிறது."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Easy", "level": "TNPSC Group 1" }
  },

  # 5. Article 14 Equality Concepts (Basic Conceptual) - Ans: B
  {
    "id": "FR_E_005",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Easy",
    "question_type": "Basic Conceptual",
    "question": {
      "en": "The concept of 'Equality before Law' in Article 14 of the Indian Constitution is borrowed from the constitutional tradition of which country?",
      "ta": "இந்திய அரசியலமைப்பின் உறுப்பு 14-ல் உள்ள 'சட்டத்தின் முன் சமத்துவம்' என்ற கருத்து எந்த நாட்டின் அரசியலமைப்பு மரபிலிருந்து பெறப்பட்டது?"
    },
    "options": [
      { "id": "A", "en": "United States of America", "ta": "அமெரிக்க ஐக்கிய நாடுகள்" },
      { "id": "B", "en": "Britain (United Kingdom)", "ta": "பிரிட்டன் (ஐக்கிய இராச்சியம்)" },
      { "id": "C", "en": "France", "ta": "பிரான்ஸ்" },
      { "id": "D", "en": "Ireland", "ta": "அயர்லாந்து" }
    ],
    "correct_answer": "B",
    "explanation": {
      "en": "'Equality before Law' is a British negative concept (derived from Dicey's Rule of Law), whereas 'Equal Protection of Laws' is an American positive concept.",
      "ta": "'சட்டத்தின் முன் சமத்துவம்' என்பது பிரிட்டிஷ் எதிர்மறைக் கருத்து (டைசியின் சட்டத்தின் ஆட்சியிலிருந்து பெறப்பட்டது); 'சட்டங்களின் சமமான பாதுகாப்பு' என்பது அமெரிக்க நேர்மறைக் கருத்து."
    },
    "why_not_others": {
      "A": { "en": "USA gave 'Equal Protection of Laws'.", "ta": "அமெரிக்கா 'சட்டங்களின் சமமான பாதுகாப்பு' கருத்தை அளித்தது." },
      "B": { "en": "Correct. British origin for Equality before Law.", "ta": "சரி. சட்டத்தின் முன் சமத்துவம் பிரிட்டிஷ் மூலத்தைக் கொண்டது." },
      "C": { "en": "France gave Liberty, Equality, Fraternity ideals in Preamble.", "ta": "பிரான்ஸ் சுதந்திரம், சமத்துவம், சகோதரத்துவ இலக்குகளை அளித்தது." },
      "D": { "en": "Ireland gave Directive Principles.", "ta": "அயர்லாந்து அரசு நெறிமுறைக் கோட்பாடுகளை அளித்தது." }
    },
    "tnpsc_tip": {
      "en": "Art 14 combines British 'Equality before law' + American 'Equal protection of laws'.",
      "ta": "உறுப்பு 14 பிரிட்டிஷ் 'சட்டத்தின் முன் சமத்துவம்' + அமெரிக்க 'சட்டங்களின் சமமான பாதுகாப்பு' இரண்டையும் இணைக்கிறது."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Easy", "level": "TNPSC Group 1" }
  },

  # 6. Article 15 Prohibited Grounds Count (Direct Factual) - Ans: C
  {
    "id": "FR_E_006",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Easy",
    "question_type": "Direct",
    "question": {
      "en": "Under Article 15(1), the State shall not discriminate against any citizen on grounds ONLY of how many specific grounds?",
      "ta": "உறுப்பு 15(1)-ன் கீழ், எந்தவொரு குடிமகனுக்கும் எதிராக எத்தனை குறிப்பிட்ட அடிப்படைகளில் மட்டுமே அரசு பாகுபாடு காட்டக்கூடாது?"
    },
    "options": [
      { "id": "A", "en": "Seven (7) grounds", "ta": "ஏழு (7) அடிப்படைகள்" },
      { "id": "B", "en": "Six (6) grounds", "ta": "ஆறு (6) அடிப்படைகள்" },
      { "id": "C", "en": "Five (5) grounds", "ta": "ஐந்து (5) அடிப்படைகள்" },
      { "id": "D", "en": "Four (4) grounds", "ta": "நான்கு (4) அடிப்படைகள்" }
    ],
    "correct_answer": "C",
    "explanation": {
      "en": "Article 15 prohibits discrimination on ONLY 5 grounds: Religion, Race, Caste, Sex, Place of Birth. (Residence and Descent are added in Article 16).",
      "ta": "உறுப்பு 15 5 அடிப்படைகளில் மட்டுமே பாகுபாட்டைத் தடுக்கிறது: மதம், இனம், சாதி, பாலினம், பிறந்த இடம். (வசிப்பிடம் மற்றும் வம்சாவளி உறுப்பு 16-ல் மட்டுமே சேர்கின்றன)."
    },
    "why_not_others": {
      "A": { "en": "7 grounds belong to Article 16(2).", "ta": "7 அடிப்படைகள் உறுப்பு 16(2)-க்கு உரியவை." },
      "B": { "en": "Six is incorrect.", "ta": "ஆறு என்பது தவறானது." },
      "C": { "en": "Correct. Article 15 has 5 prohibited grounds.", "ta": "சரி. உறுப்பு 15-ல் 5 தடைசெய்யப்பட்ட அடிப்படைகள் உள்ளன." },
      "D": { "en": "Four belongs to Article 29(2).", "ta": "நான்கு உறுப்பு 29(2)-க்கு உரியது." }
    },
    "tnpsc_tip": {
      "en": "TRAP: Art 15 = 5 grounds; Art 16 = 7 grounds (+ Residence, + Descent).",
      "ta": "பொறி: உறுப்பு 15 = 5 அடிப்படைகள்; உறுப்பு 16 = 7 அடிப்படைகள் (+ வசிப்பிடம், + வம்சாவளி)."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Easy", "level": "TNPSC Group 1" }
  },

  # 7. Article 16 Prohibited Grounds Count (Direct Factual) - Ans: A
  {
    "id": "FR_E_007",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Easy",
    "question_type": "Direct",
    "question": {
      "en": "Which two extra grounds of discrimination are prohibited specifically under Article 16(2) for public employment, which are NOT listed in Article 15?",
      "ta": "பொது வேலைவாய்ப்பிற்காக உறுப்பு 16(2)-ன் கீழ் குறிப்பாகத் தடைசெய்யப்பட்ட, உறுப்பு 15-ல் இல்லாத இரண்டு கூடுதல் அடிப்படைகள் எவை?"
    },
    "options": [
      { "id": "A", "en": "Residence and Descent", "ta": "வசிப்பிடம் மற்றும் வம்சாவளி" },
      { "id": "B", "en": "Language and Script", "ta": "மொழி மற்றும் எழுத்து" },
      { "id": "C", "en": "Sex and Place of Birth", "ta": "பாலினம் மற்றும் பிறந்த இடம்" },
      { "id": "D", "en": "Religion and Caste", "ta": "மதம் மற்றும் சாதி" }
    ],
    "correct_answer": "A",
    "explanation": {
      "en": "Article 16(2) prohibits discrimination in public employment on 7 grounds: Religion, Race, Caste, Sex, Place of Birth + Residence + Descent.",
      "ta": "பொது வேலைவாய்ப்பில் உறுப்பு 16(2) 7 அடிப்படைகளில் பாகுபாட்டைத் தடுக்கிறது: மதம், இனம், சாதி, பாலினம், பிறந்த இடம் + வசிப்பிடம் + வம்சாவளி."
    },
    "why_not_others": {
      "A": { "en": "Correct. Residence and Descent are the two extra grounds in Art 16.", "ta": "சரி. வசிப்பிடம் மற்றும் வம்சாவளி ஆகிய இரண்டும் உறுப்பு 16-ல் உள்ள கூடுதல் அடிப்படைகள்." },
      "B": { "en": "Language is in Article 29(2).", "ta": "மொழி உறுப்பு 29(2)-ல் உள்ளது." },
      "C": { "en": "Sex and Place of Birth are already present in Article 15.", "ta": "பாலினம் மற்றும் பிறந்த இடம் உறுப்பு 15-லேயே உள்ளன." },
      "D": { "en": "Religion and Caste are already present in Article 15.", "ta": "மதம் மற்றும் சாதி உறுப்பு 15-லேயே உள்ளன." }
    },
    "tnpsc_tip": {
      "en": "Article 16 has 7 prohibited grounds in total.",
      "ta": "உறுப்பு 16-ல் மொத்தம் 7 தடைசெய்யப்பட்ட அடிப்படைகள் உள்ளன."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Easy", "level": "TNPSC Group 1" }
  },

  # 8. 1st Amendment Act 1951 & Art 15(4) (Case / Amendment) - Ans: B
  {
    "id": "FR_E_008",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Easy",
    "question_type": "Case / Amendment",
    "question": {
      "en": "Article 15(4), empowering the State to make special provisions for SEBCs, SCs, and STs, was added by which Constitutional Amendment Act?",
      "ta": "SEBCs, SCs மற்றும் STs முன்னேற்றத்திற்காக சிறப்பு விதிகளை உருவாக்க அரசுக்கு அதிகாரமளிக்கும் உறுப்பு 15(4), எந்த அரசியலமைப்பு திருத்தச் சட்டத்தால் சேர்க்கப்பட்டது?"
    },
    "options": [
      { "id": "A", "en": "42nd Constitutional Amendment Act, 1976", "ta": "42வது அரசியலமைப்பு திருத்தச் சட்டம், 1976" },
      { "id": "B", "en": "1st Constitutional Amendment Act, 1951", "ta": "1வது அரசியலமைப்பு திருத்தச் சட்டம், 1951" },
      { "id": "C", "en": "44th Constitutional Amendment Act, 1978", "ta": "44வது அரசியலமைப்பு திருத்தச் சட்டம், 1978" },
      { "id": "D", "en": "93rd Constitutional Amendment Act, 2005", "ta": "93வது அரசியலமைப்பு திருத்தச் சட்டம், 2005" }
    ],
    "correct_answer": "B",
    "explanation": {
      "en": "Article 15(4) was inserted by the 1st Constitutional Amendment Act, 1951 following the Supreme Court judgment in Champakam Dorairajan case (1951).",
      "ta": "செம்பகம் துரைராஜன் வழக்கு (1951) தீர்ப்பைத் தொடர்ந்து 1951-ன் 1வது அரசியலமைப்பு திருத்தச் சட்டத்தால் உறுப்பு 15(4) சேர்க்கப்பட்டது."
    },
    "why_not_others": {
      "A": { "en": "42nd Amendment was in 1976 (Mini Constitution).", "ta": "42வது திருத்தம் 1976 இல் வந்தது." },
      "B": { "en": "Correct. 1st CAA 1951 inserted Article 15(4).", "ta": "சரி. 1வது திருத்தம் 1951 உறுப்பு 15(4)-ஐச் சேர்த்தது." },
      "C": { "en": "44th Amendment deleted Right to Property.", "ta": "44வது திருத்தம் சொத்துரிமையை நீக்கியது." },
      "D": { "en": "93rd Amendment inserted Article 15(5) for higher education.", "ta": "93வது திருத்தம் உயர்கல்விக்கான உறுப்பு 15(5)-ஐச் சேர்த்தது." }
    },
    "tnpsc_tip": {
      "en": "Champakam Dorairajan (1951) -> Prompted 1st CAA 1951 inserting Art 15(4).",
      "ta": "செம்பகம் துரைராஜன் (1951) -> 1வது திருத்தம் 1951 மூலம் உறுப்பு 15(4) சேர வழிவகுத்தது."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Easy", "level": "TNPSC Group 1" }
  },

  # 9. Article 17 Abolition of Untouchability Nature (Direct Factual) - Ans: C
  {
    "id": "FR_E_009",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Easy",
    "question_type": "Direct",
    "question": {
      "en": "Which Article of the Indian Constitution abolishes 'Untouchability' and forbids its practice in any form?",
      "ta": "இந்திய அரசியலமைப்பின் எந்த உறுப்பு 'தீண்டாமை'யை ஒழித்து, எந்த வடிவிலும் அதனைப் பின்பற்றுவதைத் தடை செய்கிறது?"
    },
    "options": [
      { "id": "A", "en": "Article 15", "ta": "உறுப்பு 15" },
      { "id": "B", "en": "Article 16", "ta": "உறுப்பு 16" },
      { "id": "C", "en": "Article 17", "ta": "உறுப்பு 17" },
      { "id": "D", "en": "Article 18", "ta": "உறுப்பு 18" }
    ],
    "correct_answer": "C",
    "explanation": {
      "en": "Article 17 abolishes untouchability and makes its practice an offence punishable by law. It is an absolute right with no exceptions.",
      "ta": "உறுப்பு 17 தீண்டாமையை ஒழித்து, அதைப் பின்பற்றுவது சட்டப்படி தண்டனைக்குரிய குற்றமாக்குகிறது. இது எந்த விலக்குகளும் இல்லாத முழுமையான உரிமை."
    },
    "why_not_others": {
      "A": { "en": "Art 15 prohibits discrimination.", "ta": "உறுப்பு 15 பாகுபாட்டைத் தடுக்கிறது." },
      "B": { "en": "Art 16 deals with public employment.", "ta": "உறுப்பு 16 பொது வேலைவாய்ப்பு பற்றியது." },
      "C": { "en": "Correct. Article 17 abolishes untouchability.", "ta": "சரி. உறுப்பு 17 தீண்டாமையை ஒழிக்கிறது." },
      "D": { "en": "Art 18 abolishes titles.", "ta": "உறுப்பு 18 பட்டங்களை ஒழிக்கிறது." }
    },
    "tnpsc_tip": {
      "en": "Article 17 is ABSOLUTE in nature and enforced via Protection of Civil Rights Act 1955.",
      "ta": "உறுப்பு 17 இயல்பிலேயே முழுமையானது (Absolute) மற்றும் 1955 சிவில் உரிமைகள் பாதுகாப்புச் சட்டம் மூலம் அமலாக்கம் பெறுகிறது."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Easy", "level": "TNPSC Group 1" }
  },

  # 10. Article 18 Abolition of Titles Exceptions (Basic Conceptual) - Ans: D
  {
    "id": "FR_E_010",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Easy",
    "question_type": "Basic Conceptual",
    "question": {
      "en": "Under Article 18(1), which two categories of distinctions are PERMITTED to be conferred by the State as valid exceptions?",
      "ta": "உறுப்பு 18(1)-ன் கீழ், அரசு வழங்குவதற்கு அனுமதிக்கப்பட்ட செல்லுபடியாகும் இரண்டு விலக்குகள் எவை?"
    },
    "options": [
      { "id": "A", "en": "Hereditary and Royal distinctions", "ta": "பாரம்பரிய மற்றும் அரச குடும்பப் பட்டங்கள்" },
      { "id": "B", "en": "Feudal and Zamindari distinctions", "ta": "நிலப்பிரபுத்துவ மற்றும் ஜமீன்தாரி பட்டங்கள்" },
      { "id": "C", "en": "Political and Administrative distinctions", "ta": "அரசியல் மற்றும் நிர்வாகப் பட்டங்கள்" },
      { "id": "D", "en": "Military and Academic distinctions", "ta": "ராணுவ மற்றும் கல்விப் பட்டங்கள்" }
    ],
    "correct_answer": "D",
    "explanation": {
      "en": "Article 18(1) states that the State shall not confer any title, except military or academic distinctions (e.g. Major, Captain, Doctor, Professor).",
      "ta": "ராணுவ அல்லது கல்வி ரீதியான வேறுபாடுகளைத் தவிர (எ.கா. மேஜர், கேப்டன், டாக்டர், பேராசிரியர்) அரசு எந்தப் பட்டத்தையும் வழங்கக்கூடாது என உறுப்பு 18(1) கூறுகிறது."
    },
    "why_not_others": {
      "A": { "en": "Hereditary titles are prohibited.", "ta": "பாரம்பரியப் பட்டங்கள் தடைசெய்யப்பட்டுள்ளன." },
      "B": { "en": "Feudal titles are prohibited.", "ta": "நிலப்பிரபுத்துவப் பட்டங்கள் தடைசெய்யப்பட்டுள்ளன." },
      "C": { "en": "Political titles are not exceptions.", "ta": "அரசியல் பட்டங்கள் விலக்குகள் அல்ல." },
      "D": { "en": "Correct. Military and Academic distinctions are allowed.", "ta": "சரி. ராணுவ மற்றும் கல்விப் பட்டங்கள் அனுமதிக்கப்படுகின்றன." }
    },
    "tnpsc_tip": {
      "en": "Military ranks (Major) and Academic titles (Dr., Prof.) are VALID under Art 18.",
      "ta": "ராணுவப் பதவிகள் (மேஜர்) மற்றும் கல்விப் பட்டங்கள் (டாக்டர், பேராசிரியர்) உறுப்பு 18-ன் கீழ் செல்லுபடியாகும்."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Easy", "level": "TNPSC Group 1" }
  },

  # 11. Article 19 Citizen Scope (Basic Conceptual) - Ans: B
  {
    "id": "FR_E_011",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Easy",
    "question_type": "Basic Conceptual",
    "question": {
      "en": "The six fundamental freedoms guaranteed under Article 19 of the Constitution are available to which category of persons?",
      "ta": "அரசியலமைப்பின் உறுப்பு 19-ன் கீழ் உத்தரவாதம் அளிக்கப்பட்ட ஆறு அடிப்படை சுதந்திரங்கள் எந்த வகையினருக்கு மட்டுமே கிடைக்கக்கூடியவை?"
    },
    "options": [
      { "id": "A", "en": "All persons including foreigners", "ta": "வெளிநாட்டினர் உட்பட அனைத்து நபர்களுக்கும்" },
      { "id": "B", "en": "Citizens of India only", "ta": "இந்தியக் குடிமக்களுக்கு மட்டுமே" },
      { "id": "C", "en": "Foreign tourists and diplomats", "ta": "வெளிநாட்டு சுற்றுலாப் பயணிகள் மற்றும் தூதர்களுக்கு" },
      { "id": "D", "en": "Registered foreign corporations only", "ta": "பதிவு செய்யப்பட்ட வெளிநாட்டு கார்ப்பரேஷன்களுக்கு மட்டுமே" }
    ],
    "correct_answer": "B",
    "explanation": {
      "en": "Article 19 rights are guaranteed ONLY to Citizens of India. They are not available to foreigners, non-citizens, or corporations.",
      "ta": "உறுப்பு 19 உரிமைகள் இந்தியக் குடிமக்களுக்கு மட்டுமே உத்தரவாதம் செய்யப்பட்டுள்ளன. இவை வெளிநாட்டினருக்கோ அல்லது கார்ப்பரேஷன்களுக்கோ கிடைக்காது."
    },
    "why_not_others": {
      "A": { "en": "Incorrect. Foreigners get Art 20 & 21, but NOT Art 19.", "ta": "தவறு. வெளிநாட்டினருக்கு உறுப்புகள் 20 & 21 உண்டு, உறுப்பு 19 இல்லை." },
      "B": { "en": "Correct. Article 19 is available ONLY to Citizens.", "ta": "சரி. உறுப்பு 19 குடிமக்களுக்கு மட்டுமே கிடைக்கும்." },
      "C": { "en": "Incorrect. Foreign tourists do not enjoy Art 19.", "ta": "தவறு. வெளிநாட்டு சுற்றுலாப் பயணிகளுக்கு உறுப்பு 19 இல்லை." },
      "D": { "en": "Incorrect. Corporations are legal entities, not citizens.", "ta": "தவறு. கார்ப்பரேஷன்கள் குடிமக்கள் அல்ல." }
    },
    "tnpsc_tip": {
      "en": "Articles 15, 16, 19, 29, 30 are available ONLY to Citizens.",
      "ta": "உறுப்புகள் 15, 16, 19, 29, 30 குடிமக்களுக்கு மட்டுமே கிடைக்கக்கூடியவை."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Easy", "level": "TNPSC Group 1" }
  },

  # 12. Article 19(1)(f) Property Deletion (Case / Amendment) - Ans: A
  {
    "id": "FR_E_012",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Easy",
    "question_type": "Case / Amendment",
    "question": {
      "en": "Which Constitutional Amendment Act deleted the Right to acquire, hold and dispose of property [Article 19(1)(f)] from the list of Fundamental Rights?",
      "ta": "அடிப்படை உரிமைகள் பட்டியலிலிருந்து சொத்தை வாங்குதல், வைத்திருத்தல் மற்றும் விற்றல் உரிமையை [உறுப்பு 19(1)(f)] நீக்கிய அரசியலமைப்பு திருத்தச் சட்டம் எது?"
    },
    "options": [
      { "id": "A", "en": "44th Constitutional Amendment Act, 1978", "ta": "44வது அரசியலமைப்பு திருத்தச் சட்டம், 1978" },
      { "id": "B", "en": "42nd Constitutional Amendment Act, 1976", "ta": "42வது அரசியலமைப்பு திருத்தச் சட்டம், 1976" },
      { "id": "C", "en": "24th Constitutional Amendment Act, 1971", "ta": "24வது அரசியலமைப்பு திருத்தச் சட்டம், 1971" },
      { "id": "D", "en": "86th Constitutional Amendment Act, 2002", "ta": "86வது அரசியலமைப்பு திருத்தச் சட்டம், 2002" }
    ],
    "correct_answer": "A",
    "explanation": {
      "en": "The 44th Constitutional Amendment Act, 1978 enacted by the Janata Party Government deleted Article 19(1)(f) and Article 31 from Part III.",
      "ta": "ஜனதா கட்சி அரசாங்கத்தால் இயற்றப்பட்ட 1978-ன் 44வது அரசியலமைப்பு திருத்தச் சட்டம் பகுதி III லிருந்து உறுப்பு 19(1)(f) மற்றும் உறுப்பு 31-ஐ நீக்கியது."
    },
    "why_not_others": {
      "A": { "en": "Correct. 44th CAA 1978 deleted Right to Property from FRs.", "ta": "சரி. 44வது திருத்தம் 1978 சொத்துரிமையை அடிப்படை உரிமையிலிருந்து நீக்கியது." },
      "B": { "en": "42nd CAA 1976 added Secular, Socialist to Preamble.", "ta": "42வது திருத்தம் 1976 மதச்சார்பற்ற, சமதர்ம சொற்களை முகவுரையில் சேர்த்தது." },
      "C": { "en": "24th CAA 1971 modified Art 13 & 368.", "ta": "24வது திருத்தம் 1971 உறுப்புகள் 13 & 368-ஐ திருத்தியது." },
      "D": { "en": "86th CAA 2002 added Right to Education.", "ta": "86வது திருத்தம் 2002 கல்வி உரிமையைச் சேர்த்தது." }
    },
    "tnpsc_tip": {
      "en": "44th CAA 1978 reduced 7 Fundamental Rights to 6.",
      "ta": "44வது திருத்தம் 1978 7 அடிப்படை உரிமைகளை 6 ஆகக் குறைத்தது."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Easy", "level": "TNPSC Group 1" }
  },

  # 13. 97th Amendment & Cooperative Societies (Case / Amendment) - Ans: C
  {
    "id": "FR_E_013",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Easy",
    "question_type": "Case / Amendment",
    "question": {
      "en": "The right to form 'cooperative societies' was added to Article 19(1)(c) by which Constitutional Amendment Act?",
      "ta": "'கூட்டுறவு சங்கங்களை' அமைக்கும் உரிமை, எந்த அரசியலமைப்பு திருத்தச் சட்டத்தின் மூலம் உறுப்பு 19(1)(c)-ல் சேர்க்கப்பட்டது?"
    },
    "options": [
      { "id": "A", "en": "91st Constitutional Amendment Act, 2003", "ta": "91வது அரசியலமைப்பு திருத்தச் சட்டம், 2003" },
      { "id": "B", "en": "93rd Constitutional Amendment Act, 2005", "ta": "93வது அரசியலமைப்பு திருத்தச் சட்டம், 2005" },
      { "id": "C", "en": "97th Constitutional Amendment Act, 2011", "ta": "97வது அரசியலமைப்பு திருத்தச் சட்டம், 2011" },
      { "id": "D", "en": "103rd Constitutional Amendment Act, 2019", "ta": "103வது அரசியலமைப்பு திருத்தச் சட்டம், 2019" }
    ],
    "correct_answer": "C",
    "explanation": {
      "en": "The 97th Constitutional Amendment Act, 2011 gave constitutional status to cooperative societies and added 'cooperative societies' to Article 19(1)(c).",
      "ta": "2011-ன் 97வது அரசியலமைப்பு திருத்தச் சட்டம் கூட்டுறவு சங்கங்களுக்கு அரசியலமைப்பு அந்தஸ்தை வழங்கி, உறுப்பு 19(1)(c)-ல் 'கூட்டுறவு சங்கங்கள்' என்பதைச் சேர்த்தது."
    },
    "why_not_others": {
      "A": { "en": "91st CAA 2003 limited Cabinet size to 15%.", "ta": "91வது திருத்தம் 2003 அமைச்சரவை அளவை 15% ஆகக் கட்டுப்படுத்தியது." },
      "B": { "en": "93rd CAA 2005 inserted Art 15(5) higher education reservations.", "ta": "93வது திருத்தம் 2005 உயர்கல்வி இடஒதுக்கீட்டு உறுப்பு 15(5)-ஐச் சேர்த்தது." },
      "C": { "en": "Correct. 97th CAA 2011 added cooperative societies.", "ta": "சரி. 97வது திருத்தம் 2011 கூட்டுறவு சங்கங்களைச் சேர்த்தது." },
      "D": { "en": "103rd CAA 2019 introduced EWS reservation.", "ta": "103வது திருத்தம் 2019 EWS இடஒதுக்கீட்டை அறிமுகப்படுத்தியது." }
    },
    "tnpsc_tip": {
      "en": "97th CAA 2011 created Part IX-B for Cooperative Societies.",
      "ta": "97வது திருத்தம் 2011 கூட்டுறவு சங்கங்களுக்காக பகுதி IX-B-ஐ உருவாக்கியது."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Easy", "level": "TNPSC Group 1" }
  },

  # 14. Article 20 Three Protections (Article-based) - Ans: B
  {
    "id": "FR_E_014",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Easy",
    "question_type": "Article-based",
    "question": {
      "en": "Article 20 of the Indian Constitution provides protection in respect of conviction for offences. Which of the following is NOT one of the three protections under Article 20?",
      "ta": "இந்திய அரசியலமைப்பின் உறுப்பு 20 குற்றச்சாட்டுகளிலிருந்து தண்டனைப் பாதுகாப்பை வழங்குகிறது. பின்வருவனவற்றில் எது உறுப்பு 20-ன் கீழ் உள்ள மூன்று பாதுகாப்புகளில் ஒன்று அல்ல?"
    },
    "options": [
      { "id": "A", "en": "No Ex-Post-Facto Law", "ta": "முந்தைய தேதியிட்ட குற்றவியல் சட்டத் தடை" },
      { "id": "B", "en": "Right to Preventive Detention", "ta": "தடுப்புக் காவல் உரிமை" },
      { "id": "C", "en": "No Double Jeopardy", "ta": "இரட்டை தண்டனைத் தடை" },
      { "id": "D", "en": "No Self-Incrimination", "ta": "தனக்குத்தானே எதிரான சாட்சியத் தடை" }
    ],
    "correct_answer": "B",
    "explanation": {
      "en": "Article 20 contains 3 criminal protections: 20(1) No Ex-Post-Facto Law, 20(2) No Double Jeopardy, 20(3) No Self-Incrimination. Preventive detention is under Article 22.",
      "ta": "உறுப்பு 20 3 குற்றவியல் பாதுகாப்புகளைக் கொண்டுள்ளது: 20(1) முந்தைய தேதியிட்ட சட்டத் தடை, 20(2) இரட்டை தண்டனைத் தடை, 20(3) தனக்குத்தானே சாட்சியத் தடை. தடுப்புக் காவல் உறுப்பு 22-ல் உள்ளது."
    },
    "why_not_others": {
      "A": { "en": "Ex-Post-Facto is under Art 20(1).", "ta": "முந்தைய தேதியிட்ட சட்டம் உறுப்பு 20(1)-ல் உள்ளது." },
      "B": { "en": "Correct. Preventive detention is under Article 22, NOT Article 20.", "ta": "சரி. தடுப்புக் காவல் உறுப்பு 22-ல் உள்ளது, உறுப்பு 20-ல் அல்ல." },
      "C": { "en": "Double Jeopardy is under Art 20(2).", "ta": "இரட்டை தண்டனை உறுப்பு 20(2)-ல் உள்ளது." },
      "D": { "en": "Self-Incrimination is under Art 20(3).", "ta": "தனக்குத்தானே சாட்சியத் தடை உறுப்பு 20(3)-ல் உள்ளது." }
    },
    "tnpsc_tip": {
      "en": "Article 20 has 3 specific criminal trial protections.",
      "ta": "உறுப்பு 20-ல் 3 குறிப்பிட்ட குற்றவியல் விசாரணை பாதுகாப்புகள் உள்ளன."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Easy", "level": "TNPSC Group 1" }
  },

  # 15. Article 20(1) Ex-Post-Facto Limit (Basic Conceptual) - Ans: A
  {
    "id": "FR_E_015",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Easy",
    "question_type": "Basic Conceptual",
    "question": {
      "en": "The protection against Ex-Post-Facto laws under Article 20(1) applies strictly to which category of laws?",
      "ta": "உறுப்பு 20(1)-ன் கீழ் முந்தைய தேதியிட்ட சட்டங்களுக்கு எதிரான பாதுகாப்பு எந்த வகை சட்டங்களுக்கு மட்டுமே கண்டிப்பாகப் பொருந்தும்?"
    },
    "options": [
      { "id": "A", "en": "Criminal laws only", "ta": "குற்றவியல் சட்டங்களுக்கு மட்டுமே" },
      { "id": "B", "en": "Civil liabilities only", "ta": "சிவில் பொறுப்புகளுக்கு மட்டுமே" },
      { "id": "C", "en": "Taxation laws only", "ta": "வரிச் சட்டங்களுக்கு மட்டுமே" },
      { "id": "D", "en": "Both Criminal and Civil laws equally", "ta": "குற்றவியல் மற்றும் சிவில் சட்டங்கள் இரண்டிற்கும் சமமாக" }
    ],
    "correct_answer": "A",
    "explanation": {
      "en": "Article 20(1) protection against ex-post-facto laws applies ONLY to Criminal laws. Retrospective civil liabilities or tax laws are FULLY VALID.",
      "ta": "உறுப்பு 20(1) முந்தைய தேதியிட்ட சட்டப் பாதுகாப்பு குற்றவியல் சட்டங்களுக்கு மட்டுமே பொருந்தும். முந்தைய தேதியிட்ட சிவில் அல்லது வரிப் பொறுப்புகள் செல்லுபடியாகும்."
    },
    "why_not_others": {
      "A": { "en": "Correct. Art 20(1) applies ONLY to Criminal laws.", "ta": "சரி. உறுப்பு 20(1) குற்றவியல் சட்டங்களுக்கு மட்டுமே பொருந்தும்." },
      "B": { "en": "Incorrect. Civil liabilities can be enacted retrospectively.", "ta": "தவறு. சிவில் பொறுப்புகளை முந்தைய தேதியிட்டு இயற்றலாம்." },
      "C": { "en": "Incorrect. Tax laws can be enacted retrospectively.", "ta": "தவறு. வரிச் சட்டங்களை முந்தைய தேதியிட்டு இயற்றலாம்." },
      "D": { "en": "Incorrect. It does NOT apply to Civil laws.", "ta": "தவறு. இது சிவில் சட்டங்களுக்குப் பொருந்தாது." }
    },
    "tnpsc_tip": {
      "en": "TRAP: Retrospective tax/civil laws are constitutional; retrospective criminal laws are unconstitutional.",
      "ta": "பொறி: முந்தைய தேதியிட்ட வரி/சிவில் சட்டங்கள் செல்லுபடியாகும்; குற்றவியல் சட்டங்கள் செல்லாது."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Easy", "level": "TNPSC Group 1" }
  },

  # 16. Article 20(2) Double Jeopardy Limit (Simple Application) - Ans: D
  {
    "id": "FR_E_016",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Easy",
    "question_type": "Simple Application",
    "question": {
      "en": "A government servant is dismissed from service following a departmental inquiry and later prosecuted in a criminal court for the same act. Does this violate Article 20(2) Double Jeopardy?",
      "ta": "ஒரு அரசு ஊழியர் துறைசார் விசாரணைக்குப் பின் பணியிலிருந்து நீக்கப்பட்டு, பின்னர் அதே செயலுக்காகக் குற்றவியல் நீதிமன்றத்தில் விசாரிக்கப்படுகிறார். இது உறுப்பு 20(2) இரட்டை தண்டனைத் தடையை மீறுகிறதா?"
    },
    "options": [
      { "id": "A", "en": "Yes, because he was punished twice for the same act", "ta": "ஆம், ஏனெனில் ஒரே செயலுக்காக அவர் இருமுறை தண்டிக்கப்பட்டார்" },
      { "id": "B", "en": "Yes, because departmental inquiry is a judicial trial", "ta": "ஆம், ஏனெனில் துறைசார் விசாரணை ஒரு நீதிமுறை விசாரணையாகும்" },
      { "id": "C", "en": "No, because government servants are exempt from Fundamental Rights", "ta": "இல்லை, ஏனெனில் அரசு ஊழியர்களுக்கு அடிப்படை உரிமைகளிலிருந்து விலக்கு உண்டு" },
      { "id": "D", "en": "No, because Double Jeopardy applies only before Courts of Law or Judicial Tribunals", "ta": "இல்லை, ஏனெனில் இரட்டை தண்டனைத் தடை நீதிமன்றங்கள் அல்லது நீதித்துறை தீர்ப்பாயங்களுக்கு மட்டுமே பொருந்தும்" }
    ],
    "correct_answer": "D",
    "explanation": {
      "en": "Protection against Double Jeopardy under Article 20(2) is available ONLY before Courts of Law or Judicial Tribunals. Departmental or administrative proceedings are NOT judicial prosecutions.",
      "ta": "உறுப்பு 20(2)-ன் கீழ் இரட்டை தண்டனைத் தடை நீதிமன்றங்கள் அல்லது நீதித்துறை தீர்ப்பாயங்களுக்கு மட்டுமே பொருந்தும். துறைசார் அல்லது நிர்வாக நடவடிக்கைகள் நீதிமுறை விசாரணைகள் அல்ல."
    },
    "why_not_others": {
      "A": { "en": "Incorrect. Departmental dismissal is an administrative penalty, not judicial punishment.", "ta": "தவறு. துறைசார் பணிநீக்கம் நிர்வாகத் தண்டனையே தவிர நீதித்துறைத் தண்டனை அல்ல." },
      "B": { "en": "Incorrect. Departmental inquiry is NOT a judicial trial.", "ta": "தவறு. துறைசார் விசாரணை நீதிமுறை விசாரணை அல்ல." },
      "C": { "en": "Incorrect. Government servants do enjoy Fundamental Rights.", "ta": "தவறு. அரசு ஊழியர்களுக்கும் அடிப்படை உரிமைகள் உண்டு." },
      "D": { "en": "Correct. Departmental action + criminal trial is constitutionally valid.", "ta": "சரி. துறைசார் நடவடிக்கை + குற்றவியல் வழக்கு செல்லுபடியாகும்." }
    },
    "tnpsc_tip": {
      "en": "Departmental proceedings are administrative; they do not attract Art 20(2) protection.",
      "ta": "துறைசார் நடவடிக்கைகள் நிர்வாக சார்ந்தவை; அவை உறுப்பு 20(2) பாதுகாப்பைப் பெறாது."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Easy", "level": "TNPSC Group 1" }
  },

  # 17. Article 21 Text & Gopalan vs Maneka (Basic Conceptual) - Ans: B
  {
    "id": "FR_E_017",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Easy",
    "question_type": "Basic Conceptual",
    "question": {
      "en": "In which landmark case did the Supreme Court overrule its Gopalan judgment and introduce the concept of 'Due Process of Law' into Article 21, requiring procedure to be 'just, fair and reasonable'?",
      "ta": "எந்த மைல்கல் வழக்கில் உச்ச நீதிமன்றம் தனது கோபாலன் தீர்ப்பை மாற்றி, நடைமுறை 'நியாயமானதாக, நேர்மையானதாக' இருக்க வேண்டும் எனக்கூறி உறுப்பு 21-ல் 'சட்டத்தின் உரிய நடைமுறை' கருத்தை அறிமுகப்படுத்தியது?"
    },
    "options": [
      { "id": "A", "en": "A.K. Gopalan v. State of Madras (1950)", "ta": "ஏ.கே. கோபாலன் எதிர் மெட்ராஸ் மாநிலம் (1950)" },
      { "id": "B", "en": "Maneka Gandhi v. Union of India (1978)", "ta": "மேனகா காந்தி எதிர் இந்திய யூனியன் (1978)" },
      { "id": "C", "en": "Kesavananda Bharati v. State of Kerala (1973)", "ta": "கேசவானந்த பாரதி எதிர் கேரளா மாநிலம் (1973)" },
      { "id": "D", "en": "Minerva Mills v. Union of India (1980)", "ta": "மினர்வா மில்ஸ் எதிர் இந்திய யூனியன் (1980)" }
    ],
    "correct_answer": "B",
    "explanation": {
      "en": "In Maneka Gandhi Case (1978), the Supreme Court gave a wide interpretation to Article 21, holding that procedure depriving personal liberty must be just, fair, and reasonable.",
      "ta": "மேனகா காந்தி வழக்கில் (1978), தனிநபர் சுதந்திரத்தைப் பறிக்கும் நடைமுறை நியாயமானதாகவும் நேர்மையானதாகவும் இருக்க வேண்டும் எனக் கூறி உறுப்பு 21-க்கு உச்ச நீதிமன்றம் அகன்ற விளக்கமளித்தது."
    },
    "why_not_others": {
      "A": { "en": "Gopalan case (1950) gave a narrow interpretation.", "ta": "கோபாலன் வழக்கு (1950) குறுகிய விளக்கமளித்தது." },
      "B": { "en": "Correct. Maneka Gandhi (1978) introduced Due Process into Art 21.", "ta": "சரி. மேனகா காந்தி (1978) உறுப்பு 21-ல் சட்டத்தின் உரிய நடைமுறையை அறிமுகப்படுத்தியது." },
      "C": { "en": "Kesavananda Bharati established Basic Structure doctrine.", "ta": "கேசவானந்த பாரதி அடிப்படை கட்டமைப்புக் கோட்பாட்டை நிறுவியது." },
      "D": { "en": "Minerva Mills affirmed balance between FR and DPSP.", "ta": "மினர்வா மில்ஸ் அடிப்படை உரிமைகள் & DPSP நல்லிணக்கத்தை உறுதி செய்தது." }
    },
    "tnpsc_tip": {
      "en": "Maneka Gandhi Case (1978) formed the 'Golden Triangle' of Articles 14, 19, and 21.",
      "ta": "மேனகா காந்தி வழக்கு (1978) உறுப்புகள் 14, 19, 21 ஆகியவற்றின் 'தங்க முக்கோணத்தை' உருவாக்கியது."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Easy", "level": "TNPSC Group 1" }
  },

  # 18. Article 21 Privacy Ruling Puttaswamy (Case / Amendment) - Ans: C
  {
    "id": "FR_E_018",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Easy",
    "question_type": "Case / Amendment",
    "question": {
      "en": "In which landmark 9-judge bench ruling did the Supreme Court unanimously declare the 'Right to Privacy' as a Fundamental Right under Article 21?",
      "ta": "எந்த மைல்கல் 9 நீதிபதிகள் அமர்வு தீர்ப்பில், உச்ச நீதிமன்றம் 'தனிமனித ரகசிய உரிமையை' உறுப்பு 21-ன் கீழ் அடிப்படை உரிமையாக ஒருமனதாக அறிவித்தது?"
    },
    "options": [
      { "id": "A", "en": "Shreya Singhal v. Union of India (2015)", "ta": "ஸ்ரேயா சிங்கால் எதிர் இந்திய யூனியன் (2015)" },
      { "id": "B", "en": "Shayara Bano v. Union of India (2017)", "ta": "ஷாயரா பானோ எதிர் இந்திய யூனியன் (2017)" },
      { "id": "C", "en": "K.S. Puttaswamy v. Union of India (2017)", "ta": "K.S. புட்டசுவாமி எதிர் இந்திய யூனியன் (2017)" },
      { "id": "D", "en": "Navtej Singh Johar v. Union of India (2018)", "ta": "நவ்தேஜ் சிங் ஜோஹர் எதிர் இந்திய யூனியன் (2018)" }
    ],
    "correct_answer": "C",
    "explanation": {
      "en": "In Justice K.S. Puttaswamy (Retd) v. Union of India (2017), a 9-judge Constitution Bench unanimously held that Right to Privacy is an intrinsic part of Right to Life and Personal Liberty under Article 21.",
      "ta": "K.S. புட்டசுவாமி எதிர் இந்திய யூனியன் (2017) வழக்கில் 9 நீதிபதிகள் அமர்வு தனிமனித ரகசிய உரிமை உறுப்பு 21-ன் கீழ் வாழ்வு மற்றும் தனிநபர் சுதந்திரத்தின் உள்ளார்ந்த பகுதி என ஒருமனதாகத் தீர்ப்பளித்தது."
    },
    "why_not_others": {
      "A": { "en": "Shreya Singhal struck down Sec 66A of IT Act.", "ta": "ஸ்ரேயா சிங்கால் தகவல் தொழில்நுட்பச் சட்டப் பிரிவு 66A-ஐ ரத்து செய்தது." },
      "B": { "en": "Shayara Bano struck down Triple Talaq.", "ta": "ஷாயரா பானோ முத்தலாக் முறையை ரத்து செய்தது." },
      "C": { "en": "Correct. Puttaswamy case (2017) declared Right to Privacy a FR under Art 21.", "ta": "சரி. புட்டசுவாமி வழக்கு (2017) ரகசிய உரிமையை உறுப்பு 21-ன் கீழ் அடிப்படை உரிமையாக்கியது." },
      "D": { "en": "Navtej Singh Johar decriminalized Sec 377 IPC.", "ta": "நவ்தேஜ் சிங் ஜோஹர் IPC பிரிவு 377-ஐக் குற்றமற்றதாக்கியது." }
    },
    "tnpsc_tip": {
      "en": "Puttaswamy 2017 = Right to Privacy is a Fundamental Right under Article 21.",
      "ta": "புட்டசுவாமி 2017 = ரகசிய உரிமை உறுப்பு 21-ன் கீழ் ஒரு அடிப்படை உரிமை."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Easy", "level": "TNPSC Group 1" }
  },

  # 19. Article 21A Age Group (Direct Factual) - Ans: A
  {
    "id": "FR_E_019",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Easy",
    "question_type": "Direct",
    "question": {
      "en": "Article 21A guarantees the Right to Free and Compulsory Education to children of which specific age group?",
      "ta": "உறுப்பு 21A எந்த குறிப்பிட்ட வயதுக் குழுவைச் சேர்ந்த குழந்தைகளுக்கு இலவச மற்றும் கட்டாயக் கல்வி உரிமையை உத்தரவாதம் செய்கிறது?"
    },
    "options": [
      { "id": "A", "en": "6 to 14 years", "ta": "6 முதல் 14 ஆண்டுகள்" },
      { "id": "B", "en": "0 to 6 years", "ta": "0 முதல் 6 ஆண்டுகள்" },
      { "id": "C", "en": "6 to 18 years", "ta": "6 முதல் 18 ஆண்டுகள்" },
      { "id": "D", "en": "5 to 15 years", "ta": "5 முதல் 15 ஆண்டுகள்" }
    ],
    "correct_answer": "A",
    "explanation": {
      "en": "Article 21A guarantees free and compulsory education to children aged 6 to 14 years. (Age group 0 to 6 years is covered under DPSP Article 45).",
      "ta": "உறுப்பு 21A 6 முதல் 14 வயதுக் குழந்தைகளுக்கு இலவச மற்றும் கட்டாயக் கல்வியை உத்தரவாதம் செய்கிறது. (0 முதல் 6 வயது DPSP உறுப்பு 45-ன் கீழ் வருகிறது)."
    },
    "why_not_others": {
      "A": { "en": "Correct. Article 21A covers children aged 6 to 14 years.", "ta": "சரி. உறுப்பு 21A 6 முதல் 14 வயதுக் குழந்தைகளை உள்ளடக்குகிறது." },
      "B": { "en": "0 to 6 years belongs to DPSP Article 45.", "ta": "0 முதல் 6 வயது DPSP உறுப்பு 45-க்கு உரியது." },
      "C": { "en": "6 to 18 years is incorrect for Article 21A.", "ta": "6 முதல் 18 வயது உறுப்பு 21A-க்கு தவறானது." },
      "D": { "en": "5 to 15 years is incorrect.", "ta": "5 முதல் 15 வயது தவறானது." }
    },
    "tnpsc_tip": {
      "en": "TRAP: Art 21A = 6-14 years (FR); Art 45 = 0-6 years early childhood care (DPSP).",
      "ta": "பொறி: உறுப்பு 21A = 6-14 வயது (அடிப்படை உரிமை); உறுப்பு 45 = 0-6 வயது ஆரம்ப காலப் பராமரிப்பு (DPSP)."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Easy", "level": "TNPSC Group 1" }
  },

  # 20. Article 21A 86th Amendment 2002 (Case / Amendment) - Ans: D
  {
    "id": "FR_E_020",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Easy",
    "question_type": "Case / Amendment",
    "question": {
      "en": "Article 21A was inserted into Part III of the Constitution by which Amendment Act?",
      "ta": "உறுப்பு 21A எந்த திருத்தச் சட்டத்தின் மூலம் அரசியலமைப்பின் பகுதி III-ல் சேர்க்கப்பட்டது?"
    },
    "options": [
      { "id": "A", "en": "73rd Constitutional Amendment Act, 1992", "ta": "73வது அரசியலமைப்பு திருத்தச் சட்டம், 1992" },
      { "id": "B", "en": "74th Constitutional Amendment Act, 1992", "ta": "74வது அரசியலமைப்பு திருத்தச் சட்டம், 1992" },
      { "id": "C", "en": "91st Constitutional Amendment Act, 2003", "ta": "91வது அரசியலமைப்பு திருத்தச் சட்டம், 2003" },
      { "id": "D", "en": "86th Constitutional Amendment Act, 2002", "ta": "86வது அரசியலமைப்பு திருத்தச் சட்டம், 2002" }
    ],
    "correct_answer": "D",
    "explanation": {
      "en": "The 86th Constitutional Amendment Act, 2002 inserted Article 21A making primary education a Fundamental Right for children aged 6 to 14 years.",
      "ta": "2002-ன் 86வது அரசியலமைப்பு திருத்தச் சட்டம் உறுப்பு 21A-ஐச் சேர்த்து 6 முதல் 14 வயதுக் குழந்தைகளுக்கான தொடக்கக் கல்வியை அடிப்படை உரிமையாக்கியது."
    },
    "why_not_others": {
      "A": { "en": "73rd Amendment created Panchayats.", "ta": "73வது திருத்தம் ஊராட்சிகளை உருவாக்கியது." },
      "B": { "en": "74th Amendment created Municipalities.", "ta": "74வது திருத்தம் நகராட்சிகளை உருவாக்கியது." },
      "C": { "en": "91st Amendment limited council of ministers.", "ta": "91வது திருத்தம் அமைச்சரவை அளவைக் கட்டுப்படுத்தியது." },
      "D": { "en": "Correct. 86th CAA 2002 inserted Article 21A.", "ta": "சரி. 86வது திருத்தம் 2002 உறுப்பு 21A-ஐச் சேர்த்தது." }
    },
    "tnpsc_tip": {
      "en": "RTE Act 2009 was enacted to implement Article 21A and came into force on April 1, 2010.",
      "ta": "உறுப்பு 21A-ஐச் செயல்படுத்த 2009 RTE சட்டம் இயற்றப்பட்டு ஏப்ரல் 1, 2010 அன்று அமலுக்கு வந்தது."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Easy", "level": "TNPSC Group 1" }
  },

  # 21. Article 22 24-Hour Rule (Simple Application) - Ans: B
  {
    "id": "FR_E_021",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Easy",
    "question_type": "Simple Application",
    "question": {
      "en": "Under Article 22(2), an arrested person must be produced before the nearest magistrate within 24 hours. Which time period is EXCLUDED while calculating these 24 hours?",
      "ta": "உறுப்பு 22(2)-ன் கீழ் கைது செய்யப்பட்ட நபர் 24 மணி நேரத்திற்குள் அருகிலுள்ள நடுவரிடம் ஆஜர்படுத்தப்பட வேண்டும். இந்த 24 மணி நேரத்தைக் கணக்கிடும் போது எந்தக் காலம் விலக்கப்படுகிறது?"
    },
    "options": [
      { "id": "A", "en": "Time spent during police interrogation", "ta": "காவல்துறை விசாரணையின் போது செலவிட்ட காலம்" },
      { "id": "B", "en": "Time necessary for the journey from place of arrest to magistrate court", "ta": "கைது செய்யப்பட்ட இடத்திலிருந்து நடுவர் நீதிமன்றத்திற்கான பயண நேரம்" },
      { "id": "C", "en": "Public holidays and Sundays", "ta": "பொது விடுமுறை நாட்கள் மற்றும் ஞாயிற்றுக்கிழமைகள்" },
      { "id": "D", "en": "Time taken by advocate to arrive", "ta": "வழக்கறிஞர் வர எடுத்துக்கொண்ட நேரம்" }
    ],
    "correct_answer": "B",
    "explanation": {
      "en": "Article 22(2) specifies that the 24-hour limit excludes the time necessary for the journey from the place of arrest to the court of the magistrate.",
      "ta": "24 மணி நேர வரம்பு கைது செய்யப்பட்ட இடத்திலிருந்து நடுவர் நீதிமன்றத்திற்குச் செல்லும் பயண நேரத்தை விலக்குகிறது என உறுப்பு 22(2) குறிப்பிடுகிறது."
    },
    "why_not_others": {
      "A": { "en": "Interrogation time is included in 24 hours.", "ta": "விசாரணை நேரம் 24 மணி நேரத்திற்குள் அடங்கும்." },
      "B": { "en": "Correct. Journey time is expressly excluded by Art 22(2).", "ta": "சரி. பயண நேரம் உறுப்பு 22(2) மூலம் வெளிப்படையாக விலக்கப்படுகிறது." },
      "C": { "en": "Holidays are not automatically excluded unless travel time applies.", "ta": "பயண நேரம் பொருந்தினாலன்றி விடுமுறை நாட்கள் தானாக விலக்கப்படாது." },
      "D": { "en": "Advocate arrival time is not excluded.", "ta": "வழக்கறிஞர் வருகை நேரம் விலக்கப்படாது." }
    },
    "tnpsc_tip": {
      "en": "Article 22(2) = Production before Magistrate within 24h (excluding journey time).",
      "ta": "உறுப்பு 22(2) = 24 மணி நேரத்திற்குள் நடுவரிடம் ஆஜர்படுத்துதல் (பயண நேரம் நீங்கலாக)."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Easy", "level": "TNPSC Group 1" }
  },

  # 22. Preventive Detention Maximum Period (TNPSC Trap) - Ans: C
  {
    "id": "FR_E_022",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Easy",
    "question_type": "TNPSC Trap",
    "question": {
      "en": "What is the maximum period for which a person can be detained under a Preventive Detention law without obtaining the opinion of an Advisory Board under Article 22(4)?",
      "ta": "உறுப்பு 22(4)-ன் கீழ் ஆலோசனை வாரியத்தின் கருத்தைப் பெறாமல் ஒரு நபரைத் தடுப்புக் காவல் சட்டத்தின் கீழ் காவலில் வைக்கக்கூடிய அதிகபட்சக் காலம் என்ன?"
    },
    "options": [
      { "id": "A", "en": "One month", "ta": "ஒரு மாதம்" },
      { "id": "B", "en": "Two months", "ta": "இரண்டு மாதங்கள்" },
      { "id": "C", "en": "Three months", "ta": "மூன்று மாதங்கள்" },
      { "id": "D", "en": "Six months", "ta": "ஆறு மாதங்கள்" }
    ],
    "correct_answer": "C",
    "explanation": {
      "en": "Under Article 22(4), no person can be detained under preventive detention for more than 3 months unless an Advisory Board approves extended detention.",
      "ta": "உறுப்பு 22(4)-ன் கீழ், ஆலோசனை வாரியம் நீட்டிக்கப்பட்ட காவலுக்கு ஒப்புதலளித்தாலன்றி 3 மாதங்களுக்கு மேல் ஒருவரைத் தடுப்புக் காவலில் வைக்க முடியாது."
    },
    "why_not_others": {
      "A": { "en": "One month is incorrect.", "ta": "ஒரு மாதம் தவறானது." },
      "B": { "en": "44th CAA passed a provision to reduce to 2 months, but it was NEVER notified/enforced.", "ta": "44வது திருத்தம் 2 மாதமாகக் குறைக்கும் விதியை நிறைவேற்றியது, ஆனால் அது நடைமுறைப்படுத்தப்படவில்லை." },
      "C": { "en": "Correct. Current constitutional maximum period remains 3 months.", "ta": "சரி. தற்போதைய அதிகபட்சக் காலம் 3 மாதங்கள் மட்டுமே." },
      "D": { "en": "Six months is incorrect without advisory board approval.", "ta": "ஆலோசனை வாரிய ஒப்புதலின்றி ஆறு மாதங்கள் என்பது தவறானது." }
    },
    "tnpsc_tip": {
      "en": "TRAP: Though 44th CAA 1978 proposed 2 months, 3 months remains the operative rule today.",
      "ta": "பொறி: 44வது திருத்தம் 2 மாதங்களை முன்மொழிந்தாலும், தற்போதைய நடைமுறை விதி 3 மாதங்கள் மட்டுமே."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Easy", "level": "TNPSC Group 1" }
  },

  # 23. Article 23 Begar & Human Trafficking (Article-based) - Ans: A
  {
    "id": "FR_E_023",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Easy",
    "question_type": "Article-based",
    "question": {
      "en": "Which Article of the Indian Constitution prohibits traffic in human beings, 'begar', and other similar forms of forced labour?",
      "ta": "இந்திய அரசியலமைப்பின் எந்த உறுப்பு மனித வியாபாரம், 'வெட்டி வேலை' (begar) மற்றும் அதுபோன்ற பிற கட்டாய வேலை வடிவங்களைத் தடை செய்கிறது?"
    },
    "options": [
      { "id": "A", "en": "Article 23", "ta": "உறுப்பு 23" },
      { "id": "B", "en": "Article 24", "ta": "உறுப்பு 24" },
      { "id": "C", "en": "Article 25", "ta": "உறுப்பு 25" },
      { "id": "D", "en": "Article 21", "ta": "உறுப்பு 21" }
    ],
    "correct_answer": "A",
    "explanation": {
      "en": "Article 23(1) prohibits traffic in human beings, begar (unpaid forced labour), and forced labour, making contravention punishable by law.",
      "ta": "உறுப்பு 23(1) மனித வியாபாரம், வெட்டி வேலை (ஊதியமில்லா கட்டாய வேலை) மற்றும் கட்டாய வேலையைத் தடை செய்து அதை தண்டனைக்குரிய குற்றமாக்குகிறது."
    },
    "why_not_others": {
      "A": { "en": "Correct. Article 23 prohibits begar and human trafficking.", "ta": "சரி. உறுப்பு 23 வெட்டி வேலை மற்றும் மனித வியாபாரத்தைத் தடுக்கிறது." },
      "B": { "en": "Article 24 prohibits child labour in hazardous work.", "ta": "உறுப்பு 24 ஆபத்தான வேலைகளில் குழந்தை தொழிலாளர்களைத் தடுக்கிறது." },
      "C": { "en": "Article 25 deals with Freedom of Religion.", "ta": "உறுப்பு 25 மத சுதந்திரம் பற்றியது." },
      "D": { "en": "Article 21 deals with Life and Personal Liberty.", "ta": "உறுப்பு 21 வாழ்வு மற்றும் தனிநபர் சுதந்திரம் பற்றியது." }
    },
    "tnpsc_tip": {
      "en": "Begar means involuntary work performed without any payment.",
      "ta": "வெட்டி வேலை (Begar) என்பது எந்த ஊதியமுமின்றி கட்டாயப்படுத்தி வேலை வாங்குவதைக் குறிக்கும்."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Easy", "level": "TNPSC Group 1" }
  },

  # 24. Article 23(2) Compulsory Public Service (TNPSC Trap) - Ans: B
  {
    "id": "FR_E_024",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Easy",
    "question_type": "TNPSC Trap",
    "question": {
      "en": "Under Article 23(2), the State may impose compulsory service for public purposes. In imposing such service, which ground is OMITTED from the non-discrimination list?",
      "ta": "உறுப்பு 23(2)-ன் கீழ் பொது நோக்கங்களுக்காக அரசு கட்டாயச் சேவையை விதிக்கலாம். அத்தகைய சேவையை விதிப்பதில் பாகுபாடின்மைப் பட்டியலிலிருந்து விடுவிக்கப்பட்ட அடிப்படை எது?"
    },
    "options": [
      { "id": "A", "en": "Religion", "ta": "மதம்" },
      { "id": "B", "en": "Sex", "ta": "பாலினம்" },
      { "id": "C", "en": "Caste", "ta": "சாதி" },
      { "id": "D", "en": "Race", "ta": "இனம்" }
    ],
    "correct_answer": "B",
    "explanation": {
      "en": "Article 23(2) states that in imposing compulsory service for public purposes, the State shall not discriminate on grounds only of Religion, Race, Caste or Class — 'SEX' IS OMITTED.",
      "ta": "பொதுக் கட்டாயச் சேவையை விதிப்பதில் அரசு மதம், இனம், சாதி, வகுப்பு அடிப்படையில் மட்டுமே பாகுபாடு காட்டக்கூடாது என உறுப்பு 23(2) கூறுகிறது — 'பாலினம்' (SEX) விடுவிக்கப்பட்டுள்ளது."
    },
    "why_not_others": {
      "A": { "en": "Religion is included in Art 23(2).", "ta": "மதம் உறுப்பு 23(2)-ல் சேர்க்கப்பட்டுள்ளது." },
      "B": { "en": "Correct. 'Sex' is omitted, allowing conscription of males for military service.", "ta": "சரி. 'பாலினம்' விடுவிக்கப்பட்டுள்ளது (ஆண்களுக்கு மட்டும் ராணுவ சேவை விதிக்க அரசுக்கு வழியமைக்கிறது)." },
      "C": { "en": "Caste is included in Art 23(2).", "ta": "சாதி உறுப்பு 23(2)-ல் சேர்க்கப்பட்டுள்ளது." },
      "D": { "en": "Race is included in Art 23(2).", "ta": "இனம் உறுப்பு 23(2)-ல் சேர்க்கப்பட்டுள்ளது." }
    },
    "tnpsc_tip": {
      "en": "TRAP: Art 23(2) non-discrimination grounds = Religion, Race, Caste, Class ('Sex' omitted!).",
      "ta": "பொறி: உறுப்பு 23(2) பாகுபாடின்மை = மதம், இனம், சாதி, வகுப்பு ('பாலினம்' விடுவிப்பு!)."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Easy", "level": "TNPSC Group 1" }
  },

  # 25. Article 24 Child Labour Prohibition Age Limit (Direct Factual) - Ans: C
  {
    "id": "FR_E_025",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Easy",
    "question_type": "Direct",
    "question": {
      "en": "Article 24 of the Indian Constitution prohibits the employment of children below what age in any factory, mine, or other hazardous employment?",
      "ta": "இந்திய அரசியலமைப்பின் உறுப்பு 24 எந்த வயதிற்குட்பட்ட குழந்தைகளைத் தொழிற்சாலைகள், சுரங்கங்கள் அல்லது பிற ஆபத்தான வேலைகளில் அமர்த்துவதைத் தடை செய்கிறது?"
    },
    "options": [
      { "id": "A", "en": "Sixteen (16) years", "ta": "பதினாறு (16) ஆண்டுகள்" },
      { "id": "B", "en": "Eighteen (18) years", "ta": "பதினெட்டு (18) ஆண்டுகள்" },
      { "id": "C", "en": "Fourteen (14) years", "ta": "பதினான்கு (14) ஆண்டுகள்" },
      { "id": "D", "en": "Twelve (12) years", "ta": "பன்னிரண்டு (12) ஆண்டுகள்" }
    ],
    "correct_answer": "C",
    "explanation": {
      "en": "Article 24 specifies that no child below the age of 14 years shall be employed to work in any factory, mine, or engaged in any other hazardous employment.",
      "ta": "14 வயதுக்குட்பட்ட எந்தவொரு குழந்தையும் எந்தவொரு தொழிற்சாலையிலும், சுரங்கத்திலும் அல்லது பிற ஆபத்தான வேலைகளிலும் வேலைக்கு அமர்த்தப்படக்கூடாது என உறுப்பு 24 குறிப்பிடுகிறது."
    },
    "why_not_others": {
      "A": { "en": "16 years is incorrect.", "ta": "16 ஆண்டுகள் தவறானது." },
      "B": { "en": "18 years is for adolescents in hazardous work under 2016 Act.", "ta": "18 ஆண்டுகள் 2016 சட்டத்தின் கீழ் ஆபத்தான வேலைக்கான சிறார் வயது." },
      "C": { "en": "Correct. Article 24 prohibits child labor below 14 years.", "ta": "சரி. உறுப்பு 24 14 வயதுக்குட்பட்ட குழந்தை தொழிலாளர்களைத் தடுக்கிறது." },
      "D": { "en": "12 years is incorrect.", "ta": "12 ஆண்டுகள் தவறானது." }
    },
    "tnpsc_tip": {
      "en": "Articles 21A and 24 both use 14 years as the threshold age limit.",
      "ta": "உறுப்புகள் 21A மற்றும் 24 இரண்டுமே 14 வயதையே உச்ச வயது வரம்பாகக் கொண்டுள்ளன."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Easy", "level": "TNPSC Group 1" }
  },

  # 26. Freedom of Religion Articles Scope (Article-based) - Ans: D
  {
    "id": "FR_E_026",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Easy",
    "question_type": "Article-based",
    "question": {
      "en": "Which set of Articles in Part III of the Constitution guarantees the 'Right to Freedom of Religion'?",
      "ta": "அரசியலமைப்பின் பகுதி III-ல் உள்ள எந்த உறுப்புகளின் தொகுதி 'மத சுதந்திர உரிமையை' உத்தரவாதம் செய்கிறது?"
    },
    "options": [
      { "id": "A", "en": "Articles 14 to 18", "ta": "உறுப்புகள் 14 முதல் 18 வரை" },
      { "id": "B", "en": "Articles 19 to 22", "ta": "உறுப்புகள் 19 முதல் 22 வரை" },
      { "id": "C", "en": "Articles 23 to 24", "ta": "உறுப்புகள் 23 முதல் 24 வரை" },
      { "id": "D", "en": "Articles 25 to 28", "ta": "உறுப்புகள் 25 முதல் 28 வரை" }
    ],
    "correct_answer": "D",
    "explanation": {
      "en": "Articles 25 to 28 guarantee the Right to Freedom of Religion (Art 25 Individual, Art 26 Denominational, Art 27 Taxation freedom, Art 28 Instruction rules).",
      "ta": "உறுப்புகள் 25 முதல் 28 மத சுதந்திர உரிமையை உத்தரவாதம் செய்கின்றன (25 தனிநபர், 26 குழு, 27 வரிவிலக்கு, 28 கல்வி போதனை விதிகள்)."
    },
    "why_not_others": {
      "A": { "en": "Arts 14-18 deal with Right to Equality.", "ta": "உறுப்புகள் 14-18 சமத்துவ உரிமை பற்றியது." },
      "B": { "en": "Arts 19-22 deal with Right to Freedom.", "ta": "உறுப்புகள் 19-22 சுதந்திர உரிமை பற்றியது." },
      "C": { "en": "Arts 23-24 deal with Right against Exploitation.", "ta": "உறுப்புகள் 23-24 சுரண்டலுக்கு எதிரான உரிமை பற்றியது." },
      "D": { "en": "Correct. Articles 25 to 28 cover Freedom of Religion.", "ta": "சரி. உறுப்புகள் 25 முதல் 28 மத சுதந்திரத்தை உள்ளடக்குகின்றன." }
    },
    "tnpsc_tip": {
      "en": "Right to Freedom of Religion is covered under Articles 25–28.",
      "ta": "மத சுதந்திர உரிமை உறுப்புகள் 25–28 இன் கீழ் உள்ளடங்கியுள்ளது."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Easy", "level": "TNPSC Group 1" }
  },

  # 27. Article 25 Forced Conversion Case Stainislaus (Case / Amendment) - Ans: A
  {
    "id": "FR_E_027",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Easy",
    "question_type": "Case / Amendment",
    "question": {
      "en": "In which landmark case did the Supreme Court rule that the Right to Propagate religion under Article 25 does NOT include the right to forcibly convert another person?",
      "ta": "எந்த மைல்கல் வழக்கில் உச்ச நீதிமன்றம் உறுப்பு 25-ன் கீழ் மதத்தைப் பரப்பும் உரிமை ஒருவரைப் பலவந்தமாக மதமாற்றம் செய்யும் உரிமையை உள்ளடக்காது எனத் தீர்ப்பளித்தது?"
    },
    "options": [
      { "id": "A", "en": "Stainislaus v. State of Madhya Pradesh (1977)", "ta": "ஸ்டேனிஸ்லாஸ் எதிர் மத்தியப் பிரதேசம் (1977)" },
      { "id": "B", "en": "S.R. Bommai v. Union of India (1994)", "ta": "எஸ்.ஆர். பொம்மை எதிர் இந்திய யூனியன் (1994)" },
      { "id": "C", "en": "Bijoe Emmanuel v. State of Kerala (1986)", "ta": "பிஜோய் இம்மானுவேல் எதிர் கேரளா மாநிலம் (1986)" },
      { "id": "D", "en": "Sarla Mudgal v. Union of India (1995)", "ta": "சர்லா முத்கல் எதிர் இந்திய யூனியன் (1995)" }
    ],
    "correct_answer": "A",
    "explanation": {
      "en": "In Rev. Stainislaus v. State of MP (1977), SC held that Art 25 gives right to transmit tenets, but forced conversion violates freedom of conscience of the converted person.",
      "ta": "ஸ்டேனிஸ்லாஸ் வழக்கில் (1977), உறுப்பு 25 கோட்பாடுகளைப் பரப்ப உரிமை அளிக்கிறது, ஆனால் பலவந்த மதமாற்றம் மதமாற்றம் செய்யப்படுபவரின் மனச்சாட்சி சுதந்திரத்தைப் பாதிப்பதால் செல்லாது என தீர்ப்பளிக்கப்பட்டது."
    },
    "why_not_others": {
      "A": { "en": "Correct. Stainislaus case (1977) ruled against forced conversion.", "ta": "சரி. ஸ்டேனிஸ்லாஸ் வழக்கு (1977) பலவந்த மதமாற்றத்திற்கு எதிராகத் தீர்ப்பளித்தது." },
      "B": { "en": "S.R. Bommai declared Secularism a Basic Structure.", "ta": "எஸ்.ஆர். பொம்மை மதச்சார்பின்மையை அடிப்படை கட்டமைப்பாக்கியது." },
      "C": { "en": "Bijoe Emmanuel dealt with National Anthem Jehovah's Witnesses.", "ta": "பிஜோய் இம்மானுவேல் தேசிய கீதம் பாடுதல் பற்றியது." },
      "D": { "en": "Sarla Mudgal dealt with Uniform Civil Code and Bigamy.", "ta": "சர்லா முத்கல் பொது சிவில் சட்டம் பற்றியது." }
    },
    "tnpsc_tip": {
      "en": "Stainislaus 1977: Right to propagate = Right to transmit tenets; NO right to convert.",
      "ta": "ஸ்டேனிஸ்லாஸ் 1977: பரப்பும் உரிமை = கோட்பாடுகளைக் கூறும் உரிமை; மதமாற்றம் செய்ய உரிமை இல்லை."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Easy", "level": "TNPSC Group 1" }
  },

  # 28. Article 26 Religious Denominations vs Art 25 (Basic Conceptual) - Ans: B
  {
    "id": "FR_E_028",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Easy",
    "question_type": "Basic Conceptual",
    "question": {
      "en": "What is the primary difference between Article 25 and Article 26 of the Constitution regarding religious freedom?",
      "ta": "மத சுதந்திரம் தொடர்பாக அரசியலமைப்பின் உறுப்பு 25 மற்றும் உறுப்பு 26 இடையேயான முதன்மை வேறுபாடு என்ன?"
    },
    "options": [
      { "id": "A", "en": "Article 25 applies only to Hindus; Article 26 applies to all religions", "ta": "உறுப்பு 25 இந்துக்களுக்கு மட்டுமே பொருந்தும்; உறுப்பு 26 அனைத்து மதங்களுக்கும் பொருந்தும்" },
      { "id": "B", "en": "Article 25 guarantees individual rights; Article 26 guarantees collective denominational rights", "ta": "உறுப்பு 25 தனிநபர் உரிமைகளை உத்தரவாதம் செய்கிறது; உறுப்பு 26 கூட்டு சமயக் குழு உரிமைகளை உத்தரவாதம் செய்கிறது" },
      { "id": "C", "en": "Article 25 is non-justiciable; Article 26 is justiciable", "ta": "உறுப்பு 25 நிலைநிறுத்த முடியாதது; உறுப்பு 26 நிலைநிறுத்தக்கூடியது" },
      { "id": "D", "en": "Article 25 applies to foreigners only; Article 26 applies to citizens only", "ta": "உறுப்பு 25 வெளிநாட்டினருக்கு மட்டுமே பொருந்தும்; உறுப்பு 26 குடிமக்களுக்கு மட்டுமே பொருந்தும்" }
    ],
    "correct_answer": "B",
    "explanation": {
      "en": "Article 25 protects individual freedom of conscience and religion for every person, whereas Article 26 protects collective rights of religious denominations.",
      "ta": "உறுப்பு 25 ஒவ்வொரு நபரின் தனிநபர் மனச்சாட்சி மற்றும் மத சுதந்திரத்தைப் பாதுகாக்கிறது, உறுப்பு 26 சமயக் குழுக்களின் கூட்டு உரிமைகளைப் பாதுகாக்கிறது."
    },
    "why_not_others": {
      "A": { "en": "Both Articles apply to all religions.", "ta": "இரண்டு உறுப்புகளுமே அனைத்து மதங்களுக்கும் பொருந்தும்." },
      "B": { "en": "Correct. Art 25 = Individual Right; Art 26 = Collective Denominational Right.", "ta": "சரி. உறுப்பு 25 = தனிநபர் உரிமை; உறுப்பு 26 = கூட்டு சமயக் குழு உரிமை." },
      "C": { "en": "Both Articles are justiciable Part III rights.", "ta": "இரண்டு உறுப்புகளுமே பகுதி III-ல் உள்ள நிலைநிறுத்தக்கூடிய உரிமைகள்." },
      "D": { "en": "Both Articles apply to citizens and non-citizens.", "ta": "இரண்டு உறுப்புகளுமே பொருந்தும்." }
    },
    "tnpsc_tip": {
      "en": "Article 25 = Individual Freedom; Article 26 = Collective Denominational Rights.",
      "ta": "உறுப்பு 25 = தனிநபர் சுதந்திரம்; உறுப்பு 26 = கூட்டு சமயக் குழு உரிமைகள்."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Easy", "level": "TNPSC Group 1" }
  },

  # 29. Article 27 Tax vs Fee (Basic Conceptual) - Ans: C
  {
    "id": "FR_E_029",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Easy",
    "question_type": "Basic Conceptual",
    "question": {
      "en": "Article 27 prohibits the levying of taxes for the promotion of a particular religion. Does Article 27 prohibit the State from levying a FEE on religious pilgrims or institutions?",
      "ta": "உறுப்பு 27 ஒரு குறிப்பிட்ட மதத்தை ஊக்குவிப்பதற்கு வரிகளை விதிப்பதைத் தடுக்கிறது. உறுப்பு 27 மத யாத்திரீகர்கள் அல்லது நிறுவனங்கள் மீது கட்டணம் (FEE) விதிப்பதை அரசுக்குத் தடுக்கிறதா?"
    },
    "options": [
      { "id": "A", "en": "Yes, both taxes and fees are completely banned", "ta": "ஆம், வரிகள் மற்றும் கட்டணங்கள் இரண்டுமே முற்றிலும் தடை செய்யப்பட்டுள்ளன" },
      { "id": "B", "en": "Yes, fees can be levied only with Supreme Court permission", "ta": "ஆம், உச்ச நீதிமன்ற அனுமதியுடன் மட்டுமே கட்டணம் விதிக்க முடியும்" },
      { "id": "C", "en": "No, Article 27 prohibits taxes only; levying a fee for regulation or special services is PERMITTED", "ta": "இல்லை, உறுப்பு 27 வரிகளை மட்டுமே தடுக்கிறது; ஒழுங்குமுறை அல்லது சிறப்புச் சேவைகளுக்காகக் கட்டணம் விதிப்பது அனுமதிக்கப்படுகிறது" },
      { "id": "D", "en": "No, fees can be levied for promoting one specific religion only", "ta": "இல்லை, ஒரு குறிப்பிட்ட மதத்தைப் பரப்புவதற்காக மட்டும் கட்டணம் விதிக்கலாம்" }
    ],
    "correct_answer": "C",
    "explanation": {
      "en": "Article 27 prohibits levying a TAX for religion, but does NOT prohibit levying a FEE. A fee can be levied to meet administrative expenses or provide safety/services to pilgrims.",
      "ta": "உறுப்பு 27 மதத்திற்காக வரி (TAX) விதிப்பதைத் தடுக்கிறது, ஆனால் கட்டணம் (FEE) விதிப்பதைத் தடுக்கவில்லை. நிர்வாகச் செலவுகள் அல்லது பாதுகாப்பு/சேவைகளுக்காகக் கட்டணம் விதிக்கலாம்."
    },
    "why_not_others": {
      "A": { "en": "Incorrect. Fees are permitted.", "ta": "தவறு. கட்டணங்கள் அனுமதிக்கப்படுகின்றன." },
      "B": { "en": "Incorrect. Supreme Court permission is not needed.", "ta": "தவறு. உச்ச நீதிமன்ற அனுமதி தேவையில்லை." },
      "C": { "en": "Correct. Taxes prohibited, Fees permitted under Art 27.", "ta": "சரி. உறுப்பு 27-ன் கீழ் வரிகள் தடை, கட்டணம் அனுமதி." },
      "D": { "en": "Incorrect. Fee proceeds are for regulatory services, not religious promotion favoritism.", "ta": "தவறு. கட்டணப் பணம் ஒழுங்குமுறைச் சேவைகளுக்கானது." }
    },
    "tnpsc_tip": {
      "en": "TRAP: Tax = Compulsory payment without direct service (Banned); Fee = Payment for service/regulation (Permitted).",
      "ta": "பொறி: வரி = சேவை இல்லாத கட்டாயச் செலுத்துகை (தடை); கட்டணம் = சேவைக்கான செலுத்துகை (அனுமதி)."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Easy", "level": "TNPSC Group 1" }
  },

  # 30. Article 29 Scope Minority vs Citizen (Basic Conceptual) - Ans: B
  {
    "id": "FR_E_030",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Easy",
    "question_type": "Basic Conceptual",
    "question": {
      "en": "Article 29(1) guarantees the right to conserve distinct language, script, or culture. Who is entitled to this right under the Constitution?",
      "ta": "உறுப்பு 29(1) தனித்துவமான மொழி, எழுத்து அல்லது பண்பாட்டைப் பாதுகாக்கும் உரிமையை உத்தரவாதம் செய்கிறது. அரசியலமைப்பின் கீழ் இந்த உரிமை யாருக்கு உரியது?"
    },
    "options": [
      { "id": "A", "en": "Religious and Linguistic Minorities exclusively", "ta": "மத மற்றும் மொழி சிறுபான்மையினருக்கு மட்டுமே பிரத்யேகமாக" },
      { "id": "B", "en": "ANY Section of Citizens residing in India (Majority and Minorities)", "ta": "இந்தியாவில் வசிக்கும் குடிமக்களின் எந்தவொரு பிரிவினருக்கும் (பெரும்பான்மையினர் & சிறுபான்மையினர்)" },
      { "id": "C", "en": "Foreign tourists and non-citizens only", "ta": "வெளிநாட்டு சுற்றுலாப் பயணிகள் மற்றும் குடிமக்கள் அல்லாதோருக்கு மட்டுமே" },
      { "id": "D", "en": "Scheduled Castes and Scheduled Tribes only", "ta": "பட்டியல் சாதியினர் மற்றும் பட்டியல் பழங்குடியினருக்கு மட்டுமே" }
    ],
    "correct_answer": "B",
    "explanation": {
      "en": "Article 29(1) uses the expression 'ANY SECTION OF CITIZENS', protecting the language/culture of both minorities and majority section of citizens.",
      "ta": "உறுப்பு 29(1) 'குடிமக்களின் எந்தவொரு பிரிவினர்' என்ற சொல்லைப் பயன்படுத்துகிறது, இது சிறுபான்மையினர் மற்றும் பெரும்பான்மையினர் இருவரின் மொழியையும் பண்பாட்டையும் பாதுகாக்கிறது."
    },
    "why_not_others": {
      "A": { "en": "Incorrect. Article 30 applies exclusively to minorities, NOT Article 29(1).", "ta": "தவறு. உறுப்பு 30 சிறுபான்மையினருக்கு மட்டுமே பொருந்தும், உறுப்பு 29(1) அல்ல." },
      "B": { "en": "Correct. Article 29(1) applies to ANY section of citizens.", "ta": "சரி. உறுப்பு 29(1) குடிமக்களின் எந்தவொரு பிரிவிற்கும் பொருந்தும்." },
      "C": { "en": "Incorrect. Article 29 is available to citizens only.", "ta": "தவறு. உறுப்பு 29 குடிமக்களுக்கு மட்டுமே கிடைக்கும்." },
      "D": { "en": "Incorrect. It is not limited to SC/STs.", "ta": "தவறு. இது எஸ்சி/எஸ்டிகளுக்கு மட்டுமே கட்டுப்படுத்தப்பட்டது அல்ல." }
    },
    "tnpsc_tip": {
      "en": "TRAP: Art 29(1) protects ANY section of citizens (Majority + Minority); Art 30 protects Minorities only.",
      "ta": "பொறி: உறுப்பு 29(1) எந்தவொரு குடிமக்கள் பிரிவையும் பாதுகாக்கும்; உறுப்பு 30 சிறுபான்மையினரை மட்டுமே பாதுகாக்கும்."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Easy", "level": "TNPSC Group 1" }
  },

  # 31. Article 30 Types of Minorities (Direct Factual) - Ans: D
  {
    "id": "FR_E_031",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Easy",
    "question_type": "Direct",
    "question": {
      "en": "Which two categories of minorities are specifically recognized under Article 30 for the right to establish and administer educational institutions?",
      "ta": "கல்வி நிறுவனங்களை நிறுவவும் நிர்வகிக்கவும் உறுப்பு 30-ன் கீழ் குறிப்பாக அங்கீகரிக்கப்பட்ட இரண்டு வகையான சிறுபான்மையினர் யாவர்?"
    },
    "options": [
      { "id": "A", "en": "Caste and Racial minorities", "ta": "சாதி மற்றும் இன சிறுபான்மையினர்" },
      { "id": "B", "en": "Economic and Social minorities", "ta": "பொருளாதார மற்றும் சமூக சிறுபான்மையினர்" },
      { "id": "C", "en": "Regional and Political minorities", "ta": "பிராந்திய மற்றும் அரசியல் சிறுபான்மையினர்" },
      { "id": "D", "en": "Religious and Linguistic minorities", "ta": "மத மற்றும் மொழி சிறுபான்மையினர்" }
    ],
    "correct_answer": "D",
    "explanation": {
      "en": "Article 30 recognizes ONLY Religious and Linguistic Minorities. (Note: The word 'Minority' is not defined anywhere in the Constitution).",
      "ta": "உறுப்பு 30 மத மற்றும் மொழி சிறுபான்மையினரை மட்டுமே அங்கீகரிக்கிறது. (குறிப்பு: 'சிறுபான்மையினர்' என்ற சொல் அரசியலமைப்பில் வரையறுக்கப்படவில்லை)."
    },
    "why_not_others": {
      "A": { "en": "Caste/Racial minorities are not recognized under Art 30.", "ta": "சாதி/இன சிறுபான்மையினர் உறுப்பு 30-ல் இல்லை." },
      "B": { "en": "Economic minorities are not recognized under Art 30.", "ta": "பொருளாதார சிறுபான்மையினர் உறுப்பு 30-ல் இல்லை." },
      "C": { "en": "Regional minorities are not recognized under Art 30.", "ta": "பிராந்திய சிறுபான்மையினர் உறுப்பு 30-ல் இல்லை." },
      "D": { "en": "Correct. Religious and Linguistic minorities are the 2 types in Art 30.", "ta": "சரி. மத மற்றும் மொழி சிறுபான்மையினரே உறுப்பு 30-ல் உள்ள 2 வகைகள்." }
    },
    "tnpsc_tip": {
      "en": "T.M.A. Pai Foundation (2002): Minority status under Art 30 is determined STATE-WISE.",
      "ta": "T.M.A. பாய் வழக்கு (2002): உறுப்பு 30-ன் கீழ் சிறுபான்மை அந்தஸ்து மாநில வாரியாக தீர்மானிக்கப்படுகிறது."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Easy", "level": "TNPSC Group 1" }
  },

  # 32. Right to Property Present Status Article 300A (Article-based) - Ans: A
  {
    "id": "FR_E_032",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Easy",
    "question_type": "Article-based",
    "question": {
      "en": "Under which Article and Part of the Constitution is the Right to Property presently placed as a Constitutional/Legal Right?",
      "ta": "சொத்துரிமை தற்சமயம் ஒரு அரசியலமைப்பு / சட்டப்பூர்வ உரிமையாக அரசியலமைப்பின் எந்த உறுப்பு மற்றும் பகுதியில் வைக்கப்பட்டுள்ளது?"
    },
    "options": [
      { "id": "A", "en": "Article 300A in Part XII", "ta": "பகுதி XII-ல் உறுப்பு 300A" },
      { "id": "B", "en": "Article 31 in Part III", "ta": "பகுதி III-ல் உறுப்பு 31" },
      { "id": "C", "en": "Article 19(1)(f) in Part III", "ta": "பகுதி III-ல் உறுப்பு 19(1)(f)" },
      { "id": "D", "en": "Article 368 in Part XX", "ta": "பகுதி XX-ல் உறுப்பு 368" }
    ],
    "correct_answer": "A",
    "explanation": {
      "en": "The Right to Property was removed from Part III in 1978 and placed as a legal right under Article 300A in Part XII of the Constitution.",
      "ta": "சொத்துரிமை 1978-ல் பகுதி III லிருந்து நீக்கப்பட்டு, பகுதி XII-ல் உறுப்பு 300A-ன் கீழ் சட்டப்பூர்வ உரிமையாக வைக்கப்பட்டது."
    },
    "why_not_others": {
      "A": { "en": "Correct. Article 300A in Part XII is the present location.", "ta": "சரி. பகுதி XII-ல் உறுப்பு 300A தற்போதைய இடமாகும்." },
      "B": { "en": "Article 31 was omitted in 1978.", "ta": "உறுப்பு 31 1978-ல் நீக்கப்பட்டது." },
      "C": { "en": "Article 19(1)(f) was omitted in 1978.", "ta": "உறுப்பு 19(1)(f) 1978-ல் நீக்கப்பட்டது." },
      "D": { "en": "Article 368 is for Amendment procedure.", "ta": "உறுப்பு 368 திருத்த நடைமுறை பற்றியது." }
    },
    "tnpsc_tip": {
      "en": "Right to Property is now a Legal/Constitutional Right, NOT a Fundamental Right.",
      "ta": "சொத்துரிமை இப்போது ஒரு சட்டப்பூர்வ/அரசியலமைப்பு உரிமை, அடிப்படை உரிமை அல்ல."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Easy", "level": "TNPSC Group 1" }
  },

  # 33. Article 32 Ambedkar Heart and Soul Quote (Direct Factual) - Ans: B
  {
    "id": "FR_E_033",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Easy",
    "question_type": "Direct",
    "question": {
      "en": "Which Article of the Constitution was described by Dr. B.R. Ambedkar as the 'very soul of the Constitution and the very heart of it'?",
      "ta": "அரசியலமைப்பின் எந்த உறுப்பை டாக்டர் பி.ஆர். அம்பேத்கர் 'அரசியலமைப்பின் இதயம் மற்றும் ஆன்மா' என்று விவரித்தார்?"
    },
    "options": [
      { "id": "A", "en": "Article 14", "ta": "உறுப்பு 14" },
      { "id": "B", "en": "Article 32", "ta": "உறுப்பு 32" },
      { "id": "C", "en": "Article 21", "ta": "உறுப்பு 21" },
      { "id": "D", "en": "Article 368", "ta": "உறுப்பு 368" }
    ],
    "correct_answer": "B",
    "explanation": {
      "en": "Dr. B.R. Ambedkar called Article 32 (Right to Constitutional Remedies) the 'heart and soul' of the Constitution because without it, fundamental rights would be meaningless paper guarantees.",
      "ta": "டாக்டர் பி.ஆர். அம்பேத்கர் உறுப்பு 32-ஐ (அரசியலமைப்புத் தீர்வு காணும் உரிமை) அரசியலமைப்பின் 'இதயமும் ஆன்மாவும்' என்றார், ஏனெனில் அது இல்லாவிட்டால் அடிப்படை உரிமைகள் வெறும் காகித உறுதிகளாகிவிடும்."
    },
    "why_not_others": {
      "A": { "en": "Art 14 is Equality before Law.", "ta": "உறுப்பு 14 சட்டத்தின் முன் சமத்துவம்." },
      "B": { "en": "Correct. Article 32 is the Heart and Soul of the Constitution.", "ta": "சரி. உறுப்பு 32 அரசியலமைப்பின் இதயமும் ஆன்மாவும் ஆகும்." },
      "C": { "en": "Art 21 is Right to Life.", "ta": "உறுப்பு 21 வாழ்வுரிமை." },
      "D": { "en": "Art 368 is Amendment procedure.", "ta": "உறுப்பு 368 திருத்த நடைமுறை." }
    },
    "tnpsc_tip": {
      "en": "Right to move Supreme Court under Article 32 is ITSELF a Fundamental Right.",
      "ta": "உறுப்பு 32-ன் கீழ் உச்ச நீதிமன்றத்தை அணுகும் உரிமை சுயமாகவே ஒரு அடிப்படை உரிமையாகும்."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Easy", "level": "TNPSC Group 1" }
  },

  # 34. Article 32 vs Article 226 Scope Comparison (Basic Conceptual) - Ans: C
  {
    "id": "FR_E_034",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Easy",
    "question_type": "Basic Conceptual",
    "question": {
      "en": "How does the writ jurisdiction of High Courts under Article 226 compare with the writ jurisdiction of the Supreme Court under Article 32?",
      "ta": "உறுப்பு 226-ன் கீழ் உயர் நீதிமன்றங்களின் மனு அதிகாரம் உறுப்பு 32-ன் கீழ் உச்ச நீதிமன்றத்தின் மனு அதிகாரத்துடன் எவ்வாறு ஒப்பிடப்படுகிறது?"
    },
    "options": [
      { "id": "A", "en": "Article 32 has wider scope than Article 226", "ta": "உறுப்பு 32 உறுப்பு 226-ஐ விட விரிவான எல்லை கொண்டது" },
      { "id": "B", "en": "Both Articles 32 and 226 have identical writ scope", "ta": "உறுப்புகள் 32 மற்றும் 226 இரண்டுமே ஒரே மாதிரியான மனு எல்லையைக் கொண்டுள்ளன" },
      { "id": "C", "en": "Article 226 has wider scope because High Courts can issue writs for FRs as well as ordinary legal rights", "ta": "உயர் நீதிமன்றங்கள் அடிப்படை உரிமைகள் மற்றும் சாதாரண சட்ட உரிமைகளுக்காகவும் மனுக்களைப் பிறப்பிக்க முடிவதால் உறுப்பு 226 விரிவான எல்லை கொண்டது" },
      { "id": "D", "en": "Article 226 can issue writs for Fundamental Rights only", "ta": "உறுப்பு 226 அடிப்படை உரிமைகளுக்கு மட்டுமே மனுக்களைப் பிறப்பிக்க முடியும்" }
    ],
    "correct_answer": "C",
    "explanation": {
      "en": "Article 226 is wider in subject scope than Article 32 because High Courts can issue writs for enforcement of Fundamental Rights AND for 'any other purpose' (ordinary legal rights).",
      "ta": "அடிப்படை உரிமைகள் மற்றும் 'வேறு எந்த நோக்கத்திற்காகவும்' (சாதாரண சட்ட உரிமைகள்) உயர் நீதிமன்றங்கள் மனுக்களைப் பிறப்பிக்க முடிவதால் உறுப்பு 226 உறுப்பு 32-ஐ விட விரிவானது."
    },
    "why_not_others": {
      "A": { "en": "Incorrect. Article 32 enforces ONLY Fundamental Rights.", "ta": "தவறு. உறுப்பு 32 அடிப்படை உரிமைகளை மட்டுமே அமல்படுத்துகிறது." },
      "B": { "en": "Incorrect. Their subject scopes differ.", "ta": "தவறு. அவற்றின் பாட எல்லைகள் வேறுபடுகின்றன." },
      "C": { "en": "Correct. Article 226 has a wider subject scope.", "ta": "சரி. உறுப்பு 226 விரிவான பாட எல்லையைக் கொண்டுள்ளது." },
      "D": { "en": "Incorrect. Art 226 can issue writs for ordinary legal rights too.", "ta": "தவறு. உறுப்பு 226 சாதாரண சட்ட உரிமைகளுக்கும் மனு அனுப்பலாம்." }
    },
    "tnpsc_tip": {
      "en": "Subject scope: Art 226 (HC) > Art 32 (SC). Territorial scope: Art 32 (SC) > Art 226 (HC).",
      "ta": "பாட எல்லை: உறுப்பு 226 (HC) > உறுப்பு 32 (SC). நிலப்பரப்பு எல்லை: உறுப்பு 32 (SC) > உறுப்பு 226 (HC)."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Easy", "level": "TNPSC Group 1" }
  },

  # 35. Habeas Corpus Meaning (Direct Factual) - Ans: A
  {
    "id": "FR_E_035",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Easy",
    "question_type": "Direct",
    "question": {
      "en": "What is the literal meaning of the Latin phrase 'Habeas Corpus'?",
      "ta": "'Habeas Corpus' (ஆட்கொணர்வு) என்ற இலத்தீன் தொடரின் நேரடிப் பொருள் என்ன?"
    },
    "options": [
      { "id": "A", "en": "To have the body of", "ta": "உடலைக் கொண்டு வா (ஆஜர்படுத்து)" },
      { "id": "B", "en": "We Command", "ta": "நாங்கள் கட்டளையிடுகிறோம்" },
      { "id": "C", "en": "To be certified", "ta": "சான்றளிப்பது" },
      { "id": "D", "en": "By what authority?", "ta": "எந்த அதிகாரத்தின் அடிப்படையில்?" }
    ],
    "correct_answer": "A",
    "explanation": {
      "en": "Habeas Corpus literally means 'To have the body of'. It is an order issued to a person/authority detaining another person to produce the detainee before court.",
      "ta": "Habeas Corpus என்பதன் நேரடிப் பொருள் 'உடலைக் கொண்டு வா' என்பதாகும். ஒருவரைக் காவலில் வைத்துள்ள அதிகாரியிடம் அந்த நபரை நீதிமன்றத்தில் ஆஜர்படுத்தப் பிறப்பிக்கப்படும் உத்தரவு."
    },
    "why_not_others": {
      "A": { "en": "Correct. Habeas Corpus = To have the body of.", "ta": "சரி. Habeas Corpus = உடலைக் கொண்டு வா." },
      "B": { "en": "We Command is the meaning of Mandamus.", "ta": "நாங்கள் கட்டளையிடுகிறோம் என்பது Mandamus-ன் பொருள்." },
      "C": { "en": "To be certified is the meaning of Certiorari.", "ta": "சான்றளிப்பது என்பது Certiorari-ன் பொருள்." },
      "D": { "en": "By what authority is the meaning of Quo Warranto.", "ta": "எந்த அதிகாரத்தின் அடிப்படையில் என்பது Quo Warranto-ன் பொருள்." }
    },
    "tnpsc_tip": {
      "en": "Habeas Corpus can be issued against BOTH public authorities and private individuals.",
      "ta": "ஆட்கொணர்வு பேராணை அரசு அமைப்புகள் மற்றும் தனியார் நபர்கள் இருவருக்கும் எதிராக வழங்கப்படலாம்."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Easy", "level": "TNPSC Group 1" }
  },

  # 36. Mandamus Limitation (TNPSC Trap) - Ans: C
  {
    "id": "FR_E_036",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Easy",
    "question_type": "TNPSC Trap",
    "question": {
      "en": "The writ of 'Mandamus' (We Command) CANNOT be issued against which of the following?",
      "ta": "'Mandamus' (செயலுறுத்தும் பேராணை) பின்வருவனவற்றில் யாருக்கு எதிராகப் பிறப்பிக்கப்பட முடியாது?"
    },
    "options": [
      { "id": "A", "en": "A public officer failing to perform statutory duty", "ta": "சட்டப்பூர்வ கடமையைச் செய்யத் தவறிய அரசு அதிகாரி" },
      { "id": "B", "en": "A lower court exceeding administrative duty", "ta": "நிர்வாகக் கடமையை மீறும் கீழ் நீதிமன்றம்" },
      { "id": "C", "en": "The President of India or State Governors", "ta": "இந்தியக் குடியரசுத் தலைவர் அல்லது மாநில ஆளுநர்கள்" },
      { "id": "D", "en": "A statutory public corporation", "ta": "ஒரு சட்டப்பூர்வ பொது கார்ப்பரேஷன்" }
    ],
    "correct_answer": "C",
    "explanation": {
      "en": "Mandamus CANNOT be issued against private individuals, President of India, State Governors, or to enforce departmental instructions lacking statutory force or contractual obligations.",
      "ta": "செயலுறுத்தும் பேராணையைத் (Mandamus) தனியார் நபர்கள், இந்தியக் குடியரசுத் தலைவர், மாநில ஆளுநர்களுக்கு எதிராகப் பிறப்பிக்க முடியாது."
    },
    "why_not_others": {
      "A": { "en": "Mandamus CAN be issued against a public officer.", "ta": "அரசு அதிகாரிக்கு எதிராக வழங்க முடியும்." },
      "B": { "en": "Mandamus CAN be issued against a lower court for public duty.", "ta": "கீழ் நீதிமன்றத்திற்கு எதிராக வழங்க முடியும்." },
      "C": { "en": "Correct. Mandamus CANNOT be issued against President or Governors.", "ta": "சரி. குடியரசுத் தலைவர் அல்லது ஆளுநர்களுக்கு எதிராக வழங்க முடியாது." },
      "D": { "en": "Mandamus CAN be issued against a statutory corporation.", "ta": "சட்டப்பூர்வ கார்ப்பரேஷனுக்கு எதிராக வழங்க முடியும்." }
    },
    "tnpsc_tip": {
      "en": "TRAP: Mandamus lies against public officials ONLY, never against President, Governors, or private persons.",
      "ta": "பொறி: செயலுறுத்தும் பேராணை அரசு அதிகாரிகளுக்கு மட்டுமே பொருந்தும்; குடியரசுத் தலைவர், ஆளுநர்கள், தனியாருக்கு எதிராக முடியாது."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Easy", "level": "TNPSC Group 1" }
  },

  # 37. Prohibition vs Certiorari Distinction (Basic Conceptual) - Ans: B
  {
    "id": "FR_E_037",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Easy",
    "question_type": "Basic Conceptual",
    "question": {
      "en": "What is the key functional difference between the writ of 'Prohibition' and the writ of 'Certiorari'?",
      "ta": "'Prohibition' (தடைசெய் பேராணை) மற்றும் 'Certiorari' (நெறிமுறையுறுத்தும் பேராணை) ஆகியவற்றிற்கு இடையேயான முதன்மைச் செயல்பாட்டு வேறுபாடு என்ன?"
    },
    "options": [
      { "id": "A", "en": "Prohibition is curative only, whereas Certiorari is preventative only", "ta": "தடைசெய் பேராணை நிவாரணம் மட்டுமே, நெறிமுறையுறுத்தும் பேராணை தடுப்பு மட்டுமே" },
      { "id": "B", "en": "Prohibition is preventative only (issued while case is pending), whereas Certiorari is both preventative and curative (quashes order after decision)", "ta": "தடைசெய் பேராணை தடுப்பு மட்டுமே (வழக்கு நிலுவையில் இருக்கும் போது), நெறிமுறையுறுத்தும் பேராணை தடுப்பு மற்றும் நிவாரணம் இரண்டும் (தீர்ப்பிற்குப் பின் ரத்து செய்ய)" },
      { "id": "C", "en": "Prohibition applies to private individuals, whereas Certiorari applies to public bodies", "ta": "தடைசெய் பேராணை தனியாருக்குப் பொருந்தும், நெறிமுறையுறுத்தும் பேராணை பொது அமைப்புகளுக்குப் பொருந்தும்" },
      { "id": "D", "en": "Prohibition is issued by High Courts, whereas Certiorari is issued by Supreme Court only", "ta": "தடைசெய் பேராணை உயர் நீதிமன்றத்தால் வழங்கப்படுகிறது, நெறிமுறையுறுத்தும் பேராணை உச்ச நீதிமன்றத்தால் மட்டுமே வழங்கப்படுகிறது" }
    ],
    "correct_answer": "B",
    "explanation": {
      "en": "Prohibition is preventative only (stops ongoing proceedings in lower court). Certiorari is both preventative and curative (quashes an unconstitutional order already passed).",
      "ta": "தடைசெய் பேராணை தடுப்பு மட்டுமே (நிலுவையிலுள்ள வழக்கைத் தடுக்கும்). நெறிமுறையுறுத்தும் பேராணை தடுப்பு மற்றும் நிவாரணம் இரண்டும் (ஏற்கனவே பிறப்பிக்கப்பட்ட உத்தரவை ரத்து செய்யும்)."
    },
    "why_not_others": {
      "A": { "en": "Reversed description.", "ta": "தலைகீழ் விளக்கம்." },
      "B": { "en": "Correct. Prohibition = Preventative; Certiorari = Preventative + Curative.", "ta": "சரி. Prohibition = தடுப்பு; Certiorari = தடுப்பு + நிவாரணம்." },
      "C": { "en": "Neither writ applies to private individuals.", "ta": "இரண்டு பேராணைகளுமே தனியாருக்குப் பொருந்தாது." },
      "D": { "en": "Both SC and HC can issue both writs.", "ta": "இரண்டு நீதிமன்றங்களும் இரண்டு பேராணைகளையும் பிறப்பிக்கலாம்." }
    },
    "tnpsc_tip": {
      "en": "Prohibition = 'Prevention is better than cure'; Certiorari = 'Curative quashing of order'.",
      "ta": "Prohibition = 'வருமுன் காப்பதே மேல்'; Certiorari = 'உத்தரவை ரத்து செய்யும் நிவாரணம்'."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Easy", "level": "TNPSC Group 1" }
  },

  # 38. Quo Warranto Locus Standi (Direct Factual) - Ans: D
  {
    "id": "FR_E_038",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Easy",
    "question_type": "Direct",
    "question": {
      "en": "Which of the Five Writs is unique because the rule of 'Locus Standi' (who can file) is RELAXED, allowing any interested person (not necessarily the aggrieved party) to seek it?",
      "ta": "பாதிக்கப்பட்ட நபர் மட்டுமின்றி எந்தவொரு ஆர்வமுள்ள நபரும் மனு தாக்கல் செய்யக்கூடும் வகையில் 'Locus Standi' விதி தளர்த்தப்பட்டுள்ள தனித்துவமான பேராணை எது?"
    },
    "options": [
      { "id": "A", "en": "Mandamus", "ta": "செயலுறுத்தும் பேராணை (Mandamus)" },
      { "id": "B", "en": "Certiorari", "ta": "நெறிமுறையுறுத்தும் பேராணை (Certiorari)" },
      { "id": "C", "en": "Prohibition", "ta": "தடைசெய் பேராணை (Prohibition)" },
      { "id": "D", "en": "Quo Warranto", "ta": "தகுதி வினா பேராணை (Quo Warranto)" }
    ],
    "correct_answer": "D",
    "explanation": {
      "en": "Quo Warranto (By what authority) is the only writ where locus standi is relaxed. Any public-spirited or interested citizen can petition the court to challenge illegal usurpation of a public office.",
      "ta": "தகுதி வினா பேராணையில் (Quo Warranto) மட்டுமே மனு தாக்கல் செய்யும் உரிமை தளர்த்தப்பட்டுள்ளது. பொதுப் பதவியைச் சட்டவிரோதமாகக் கைப்பற்றுவதை எதிர்க்க எந்தவொரு ஆர்வமுள்ள குடிமகனும் மனு தாக்கல் செய்யலாம்."
    },
    "why_not_others": {
      "A": { "en": "Mandamus requires aggrieved person with a legal right.", "ta": "Mandamus-க்கு சட்ட உரிமை கொண்ட பாதிக்கப்பட்ட நபர் தேவை." },
      "B": { "en": "Certiorari requires an aggrieved party.", "ta": "Certiorari-க்கு பாதிக்கப்பட்ட தரப்பு தேவை." },
      "C": { "en": "Prohibition requires an aggrieved party.", "ta": "Prohibition-க்கு பாதிக்கப்பட்ட தரப்பு தேவை." },
      "D": { "en": "Correct. Quo Warranto locus standi is relaxed.", "ta": "சரி. தகுதி வினா பேராணையில் மனு தாக்கல் உரிமை தளர்த்தப்பட்டுள்ளது." }
    },
    "tnpsc_tip": {
      "en": "TRAP: Quo Warranto is the ONLY writ that can be sought by any interested non-aggrieved citizen.",
      "ta": "பொறி: தகுதி வினா பேராணை மட்டுமே பாதிக்கப்படாத எந்தவொரு ஆர்வமுள்ள குடிமகனாலும் கேட்கப்படலாம்."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Easy", "level": "TNPSC Group 1" }
  },

  # 39. Article 33 Parliament Exclusivity (Article-based) - Ans: A
  {
    "id": "FR_E_039",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Easy",
    "question_type": "Article-based",
    "question": {
      "en": "Under Article 33 of the Constitution, who possesses the exclusive power to restrict or modify the Fundamental Rights of members of Armed Forces, Para-military forces, and Police forces?",
      "ta": "அரசியலமைப்பின் உறுப்பு 33-ன் கீழ், ஆயுதப் படைகள், துணை ராணுவப் படைகள் மற்றும் காவல்துறையினரின் அடிப்படை உரிமைகளைக் கட்டுப்படுத்த அல்லது மாற்றியமைக்க யாருக்கு மட்டுமே பிரத்யேக அதிகாரம் உண்டு?"
    },
    "options": [
      { "id": "A", "en": "Parliament of India only", "ta": "இந்திய நாடாளுமன்றத்திற்கு மட்டுமே" },
      { "id": "B", "en": "State Legislatures only", "ta": "மாநில சட்டமன்றங்களுக்கு மட்டுமே" },
      { "id": "C", "en": "Supreme Court of India", "ta": "இந்திய உச்ச நீதிமன்றம்" },
      { "id": "D", "en": "President of India acting independently", "ta": "சுயமாகச் செயல்படும் இந்தியக் குடியரசுத் தலைவர்" }
    ],
    "correct_answer": "A",
    "explanation": {
      "en": "Article 33 empowers PARLIAMENT ONLY to make laws restricting or abrogating Fundamental Rights for armed forces personnel to ensure proper discharge of duties and maintenance of discipline.",
      "ta": "ஆயுதப் படையினரின் கடமைகளைச் சரிவரச் செய்வதையும் ஒழுக்கத்தைப் பராமரிப்பதையும் உறுதி செய்ய அடிப்படை உரிமைகளைக் கட்டுப்படுத்தும் சட்டங்களை இயற்ற நாடாளுமன்றத்திற்கு மட்டுமே உறுப்பு 33 அதிகாரமளிக்கிறது."
    },
    "why_not_others": {
      "A": { "en": "Correct. Article 33 power belongs EXCLUSIVELY to Parliament.", "ta": "சரி. உறுப்பு 33 அதிகாரம் நாடாளுமன்றத்திற்கு மட்டுமே உள்ளது." },
      "B": { "en": "State Legislatures have NO power under Article 33.", "ta": "மாநில சட்டமன்றங்களுக்கு உறுப்பு 33-ன் கீழ் அதிகாரம் இல்லை." },
      "C": { "en": "Supreme Court does not enact laws restricting FRs.", "ta": "உச்ச நீதிமன்றம் சட்டங்களை இயற்றுவதில்லை." },
      "D": { "en": "President acts on Parliamentary legislation.", "ta": "குடியரசுத் தலைவர் நாடாளுமன்றச் சட்டத்தின்படியே செயல்படுகிறார்." }
    },
    "tnpsc_tip": {
      "en": "Laws made under Article 33 cannot be challenged in court for FR violation.",
      "ta": "உறுப்பு 33-ன் கீழ் இயற்றப்படும் சட்டங்களை அடிப்படை உரிமை மீறலுக்காக நீதிமன்றத்தில் எதிர்க்க முடியாது."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Easy", "level": "TNPSC Group 1" }
  },

  # 40. Article 34 Martial Law Meaning (Direct Factual) - Ans: C
  {
    "id": "FR_E_040",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Easy",
    "question_type": "Direct",
    "question": {
      "en": "Article 34 provides for restrictions on Fundamental Rights while 'Martial Law' is in force. What does 'Martial Law' literally mean?",
      "ta": "'ராணுவ சட்டம்' (Martial Law) அமலில் இருக்கும் போது அடிப்படை உரிமைகளின் மீதான கட்டுப்பாடுகளை உறுப்பு 34 வழங்குகிறது. 'Martial Law' என்பதன் நேரடிப் பொருள் என்ன?"
    },
    "options": [
      { "id": "A", "en": "President's Rule under Article 356", "ta": "உறுப்பு 356-ன் கீழ் குடியரசுத் தலைவர் ஆட்சி" },
      { "id": "B", "en": "National Emergency under Article 352", "ta": "உறுப்பு 352-ன் கீழ் தேசிய அவசரநிலை" },
      { "id": "C", "en": "Military Rule / Administration by Military authorities", "ta": "ராணுவ ஆட்சி / ராணுவ அதிகாரிகளின் நிர்வாகம்" },
      { "id": "D", "en": "Financial Emergency under Article 360", "ta": "உறுப்பு 360-ன் கீழ் நிதி அவசரநிலை" }
    ],
    "correct_answer": "C",
    "explanation": {
      "en": "Martial Law literally means 'Military Rule', where civil administration is taken over by military authorities under extraordinary circumstances to restore order.",
      "ta": "Martial Law என்பதன் நேரடிப் பொருள் 'ராணுவ ஆட்சி' என்பதாகும், இங்கு ஒழுங்கைப் பராமரிக்க அவசரச் சூழ்நிலைகளில் சிவில் நிர்வாகம் ராணுவ அதிகாரிகளால் பொறுப்பேற்கப்படுகிறது."
    },
    "why_not_others": {
      "A": { "en": "President's Rule is under Art 356.", "ta": "குடியரசுத் தலைவர் ஆட்சி உறுப்பு 356-ன் கீழ் வருகிறது." },
      "B": { "en": "National Emergency is under Art 352.", "ta": "தேசிய அவசரநிலை உறுப்பு 352-ன் கீழ் வருகிறது." },
      "C": { "en": "Correct. Martial Law means Military Rule.", "ta": "சரி. Martial Law என்றால் ராணுவ ஆட்சி." },
      "D": { "en": "Financial Emergency is under Art 360.", "ta": "நிதி அவசரநிலை உறுப்பு 360-ன் கீழ் வருகிறது." }
    },
    "tnpsc_tip": {
      "en": "Martial Law is NOT defined anywhere in the Constitution.",
      "ta": "ராணுவ சட்டம் (Martial Law) அரசியலமைப்பில் எங்கும் வரையறுக்கப்படவில்லை."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Easy", "level": "TNPSC Group 1" }
  },

  # 41. Article 35 Exclusive Parliamentary Power (Direct Factual) - Ans: B
  {
    "id": "FR_E_041",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Easy",
    "question_type": "Direct",
    "question": {
      "en": "Why does Article 35 confer exclusive power on Parliament to prescribe punishments for offences under Article 17 (Untouchability) and Article 23 (Forced Labour)?",
      "ta": "உறுப்பு 17 (தீண்டாமை) மற்றும் உறுப்பு 23 (கட்டாய வேலை) குற்றங்களுக்கான தண்டனைகளை நிர்ணயிக்க உறுப்பு 35 ஏன் நாடாளுமன்றத்திற்கு மட்டுமே பிரத்யேக அதிகாரத்தை வழங்குகிறது?"
    },
    "options": [
      { "id": "A", "en": "To increase central government revenue", "ta": "மத்திய அரசின் வருவாயை அதிகரிக்க" },
      { "id": "B", "en": "To ensure UNIFORMITY of Fundamental Rights and punishments throughout India", "ta": "இந்தியா முழுவதும் அடிப்படை உரிமைகள் மற்றும் தண்டனைகளின் சீரான தன்மையை (UNIFORMITY) உறுதி செய்ய" },
      { "id": "C", "en": "Because State Legislatures are prohibited from making any laws", "ta": "மாநில சட்டமன்றங்கள் எந்தச் சட்டத்தையும் இயற்றத் தடை செய்யப்பட்டுள்ளதால்" },
      { "id": "D", "en": "To transfer police administration to the Union Government", "ta": "காவல்துறை நிர்வாகத்தை மத்திய அரசுக்கு மாற்ற" }
    ],
    "correct_answer": "B",
    "explanation": {
      "en": "Article 35 ensures that laws giving effect to specified FRs and punishments for offences (Arts 17 & 23) are uniform across all States in India.",
      "ta": "குறிப்பிட்ட அடிப்படை உரிமைகளைச் செயல்படுத்தும் சட்டங்களும் குற்றங்களுக்கான தண்டனைகளும் (உறுப்புகள் 17 & 23) இந்தியாவின் அனைத்து மாநிலங்களிலும் சீராக இருப்பதை உறுப்பு 35 உறுதி செய்கிறது."
    },
    "why_not_others": {
      "A": { "en": "Revenue is not the object.", "ta": "வருவாய் நோக்கம் அல்ல." },
      "B": { "en": "Correct. Uniformity of FR implementation is the constitutional goal of Art 35.", "ta": "சரி. அடிப்படை உரிமைகள் அமலாக்கத்தின் சீரான தன்மையே உறுப்பு 35-ன் அரசியலமைப்பு இலக்கு." },
      "C": { "en": "State Legislatures make general laws, but Art 35 reserves FR penal laws to Parliament.", "ta": "மாநில சட்டமன்றங்கள் பொதுச் சட்டங்களை இயற்றுகின்றன, ஆனால் உறுப்பு 35 FR தண்டனைச் சட்டங்களை நாடாளுமன்றத்திற்கு ஒதுக்குகிறது." },
      "D": { "en": "Police remains a State subject under List II.", "ta": "காவல்துறை பட்டியல் II-ன் கீழ் மாநிலப் பொருளாகவே உள்ளது." }
    },
    "tnpsc_tip": {
      "en": "Article 35 = Uniformity of Fundamental Rights enforcement nationwide.",
      "ta": "உறுப்பு 35 = நாடு முழுவதும் அடிப்படை உரிமைகள் அமலாக்கத்தின் சீரான தன்மை."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Easy", "level": "TNPSC Group 1" }
  },

  # 42. Non-Suspendable Rights Emergency Arts 20 & 21 (Direct Factual) - Ans: A
  {
    "id": "FR_E_042",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Easy",
    "question_type": "Direct",
    "question": {
      "en": "Which two Fundamental Rights CANNOT be suspended even during the operation of a National Emergency under Article 352?",
      "ta": "உறுப்பு 352-ன் கீழ் தேசிய அவசரநிலை அமலில் இருக்கும் போது கூட இடைநிறுத்தப்பட முடியாத இரண்டு அடிப்படை உரிமைகள் எவை?"
    },
    "options": [
      { "id": "A", "en": "Articles 20 and 21", "ta": "உறுப்புகள் 20 மற்றும் 21" },
      { "id": "B", "en": "Articles 14 and 19", "ta": "உறுப்புகள் 14 மற்றும் 19" },
      { "id": "C", "en": "Articles 23 and 24", "ta": "உறுப்புகள் 23 மற்றும் 24" },
      { "id": "D", "en": "Articles 29 and 30", "ta": "உறுப்புகள் 29 மற்றும் 30" }
    ],
    "correct_answer": "A",
    "explanation": {
      "en": "The 44th Constitutional Amendment Act, 1978 provided that the rights guaranteed by Articles 20 (Conviction protection) and 21 (Life & Liberty) cannot be suspended during National Emergency.",
      "ta": "1978-ன் 44வது அரசியலமைப்பு திருத்தச் சட்டம் உறுப்புகள் 20 (தண்டனைப் பாதுகாப்பு) மற்றும் 21 (வாழ்வுரிமை) வழங்கும் உரிமைகளை தேசிய அவசரநிலையின் போது கூட இடைநிறுத்த முடியாது என வழங்கியது."
    },
    "why_not_others": {
      "A": { "en": "Correct. Articles 20 and 21 remain enforceable during Emergency.", "ta": "சரி. உறுப்புகள் 20 மற்றும் 21 அவசரநிலையின் போது அமலில் இருக்கும்." },
      "B": { "en": "Art 19 can be suspended under Art 358 during external emergency.", "ta": "வெளிநாட்டு அவசரநிலையின் போது உறுப்பு 358-ன் கீழ் உறுப்பு 19 இடைநிறுத்தப்படலாம்." },
      "C": { "en": "Arts 23 & 24 can be suspended under Art 359 if presidential order specifies.", "ta": "குடியரசுத் தலைவர் ஆணை குறிப்பிட்டால் உறுப்புகள் 23 & 24 இடைநிறுத்தப்படலாம்." },
      "D": { "en": "Arts 29 & 30 can be suspended under Art 359.", "ta": "உறுப்புகள் 29 & 30 இடைநிறுத்தப்படலாம்." }
    },
    "tnpsc_tip": {
      "en": "44th CAA 1978 protected Articles 20 and 21 from emergency suspension.",
      "ta": "44வது திருத்தம் 1978 உறுப்புகள் 20 மற்றும் 21-ஐ அவசரநிலை இடைநிறுத்தத்திலிருந்து பாதுகாத்தது."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Easy", "level": "TNPSC Group 1" }
  },

  # 43. FR vs DPSP Minerva Mills Balance (Basic Conceptual) - Ans: C
  {
    "id": "FR_E_043",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Easy",
    "question_type": "Basic Conceptual",
    "question": {
      "en": "In which landmark case did the Supreme Court hold that the Indian Constitution is founded on the 'harmonious balance' between Part III (Fundamental Rights) and Part IV (DPSP)?",
      "ta": "எந்த மைல்கல் வழக்கில் உச்ச நீதிமன்றம் இந்திய அரசியலமைப்பு பகுதி III (அடிப்படை உரிமைகள்) மற்றும் பகுதி IV (DPSP) இடையேயான 'நல்லிணக்கச் சமநிலையின்' மீதே நிறுவப்பட்டுள்ளது எனத் தீர்ப்பளித்தது?"
    },
    "options": [
      { "id": "A", "en": "Golak Nath v. State of Punjab (1967)", "ta": "கோலக் நாத் எதிர் பஞ்சாப் மாநிலம் (1967)" },
      { "id": "B", "en": "Champakam Dorairajan v. State of Madras (1951)", "ta": "செம்பகம் துரைராஜன் எதிர் மெட்ராஸ் மாநிலம் (1951)" },
      { "id": "C", "en": "Minerva Mills v. Union of India (1980)", "ta": "மினர்வா மில்ஸ் எதிர் இந்திய யூனியன் (1980)" },
      { "id": "D", "en": "Indra Sawhney v. Union of India (1992)", "ta": "இந்திரா சாஹ்னி எதிர் இந்திய யூனியன் (1992)" }
    ],
    "correct_answer": "C",
    "explanation": {
      "en": "In Minerva Mills Case (1980), the Supreme Court held that Part III and Part IV are like two wheels of a chariot; the harmonious balance between them is part of the Basic Structure.",
      "ta": "மினர்வா மில்ஸ் வழக்கில் (1980), பகுதி III மற்றும் பகுதி IV ஆகியவை ஒரு தேரின் இரு சக்கரங்கள் போன்றவை; அவற்றுக்கிடையேயான நல்லிணக்கச் சமநிலை அடிப்படை கட்டமைப்பின் பகுதி என உச்ச நீதிமன்றம் தீர்ப்பளித்தது."
    },
    "why_not_others": {
      "A": { "en": "Golak Nath held Parliament cannot amend FRs.", "ta": "கோலக் நாத் நாடாளுமன்றம் FRs-ஐ திருத்த முடியாது என்றது." },
      "B": { "en": "Champakam Dorairajan held FRs prevail over DPSP in case of conflict.", "ta": "செம்பகம் துரைராஜன் மோதல் ஏற்பட்டால் FRs மேலோங்கும் என்றது." },
      "C": { "en": "Correct. Minerva Mills (1980) established harmonious balance as Basic Structure.", "ta": "சரி. மினர்வா மில்ஸ் (1980) நல்லிணக்கச் சமநிலையை அடிப்படை கட்டமைப்பாக நிறுவியது." },
      "D": { "en": "Indra Sawhney dealt with OBC reservation cap.", "ta": "இந்திரா சாஹ்னி OBC இடஒதுக்கீடு உச்ச வரம்பு பற்றியது." }
    },
    "tnpsc_tip": {
      "en": "Minerva Mills (1980) = Harmonious balance between FR & DPSP is Basic Structure.",
      "ta": "மினர்வா மில்ஸ் (1980) = அடிப்படை உரிமைகள் & DPSP நல்லிணக்கச் சமநிலை அடிப்படை கட்டமைப்பு."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Easy", "level": "TNPSC Group 1" }
  },

  # 44. FR vs Fundamental Duties Correlation (Basic Conceptual) - Ans: B
  {
    "id": "FR_E_044",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Easy",
    "question_type": "Basic Conceptual",
    "question": {
      "en": "Which Fundamental Duty under Article 51A directly corresponds to and reinforces the Fundamental Right to Education under Article 21A?",
      "ta": "உறுப்பு 21A-ன் கீழ் உள்ள கல்விக்கான அடிப்படை உரிமையை நேரடியாக ஒத்திருந்து வலுப்படுத்தும் உறுப்பு 51A-ன் கீழ் உள்ள அடிப்படை கடமை எது?"
    },
    "options": [
      { "id": "A", "en": "Article 51A(a) – Abide by Constitution and respect National Flag", "ta": "உறுப்பு 51A(a) – அரசியலமைப்பிற்குக் கீழ்ப்படிதல் மற்றும் தேசியக் கொடியை மதித்தல்" },
      { "id": "B", "en": "Article 51A(k) – Duty of parent/guardian to provide education to child aged 6-14", "ta": "உறுப்பு 51A(k) – 6-14 வயதுக் குழந்தைக்குக் கல்வி வாய்ப்புகளை வழங்குவது பெற்றோர்/பாதுகாவலர் கடமை" },
      { "id": "C", "en": "Article 51A(g) – Protect natural environment and wildlife", "ta": "உறுப்பு 51A(g) – இயற்கை சுற்றுச்சூழல் மற்றும் வனவிலங்குகளைப் பாதுகாத்தல்" },
      { "id": "D", "en": "Article 51A(h) – Develop scientific temper and spirit of inquiry", "ta": "உறுப்பு 51A(h) – அறிவியல் மனப்பான்மை மற்றும் ஆராய்ச்சி உணர்வை வளர்த்தல்" }
    ],
    "correct_answer": "B",
    "explanation": {
      "en": "The 86th Amendment Act 2002 added Article 51A(k) as the 11th Fundamental Duty, creating a direct duty for parents to provide education to children aged 6-14, corresponding to Art 21A.",
      "ta": "2002-ன் 86வது திருத்தச் சட்டம் உறுப்பு 51A(k)-ஐ 11வது அடிப்படை கடமையாகச் சேர்த்தது, இது உறுப்பு 21A-க்கு இணையாகக் குழந்தைக்குக் கல்வி அளிக்கும் கடமையைப் பெற்றோருக்கு உருவாக்குகிறது."
    },
    "why_not_others": {
      "A": { "en": "Art 51A(a) is about National Flag and Anthem.", "ta": "உறுப்பு 51A(a) தேசியக் கொடி மற்றும் கீதம் பற்றியது." },
      "B": { "en": "Correct. Article 51A(k) corresponds directly to Article 21A.", "ta": "சரி. உறுப்பு 51A(k) உறுப்பு 21A-க்கு நேரடியாக ஒத்திருக்கிறது." },
      "C": { "en": "Art 51A(g) is about Environment.", "ta": "உறுப்பு 51A(g) சுற்றுச்சூழல் பற்றியது." },
      "D": { "en": "Art 51A(h) is about Scientific Temper.", "ta": "உறுப்பு 51A(h) அறிவியல் மனப்பான்மை பற்றியது." }
    },
    "tnpsc_tip": {
      "en": "86th CAA 2002 added Art 21A (FR), modified Art 45 (DPSP), and added Art 51A(k) (Duty).",
      "ta": "86வது திருத்தம் 2002 உறுப்பு 21A (FR), உறுப்பு 45 (DPSP), உறுப்பு 51A(k) (கடமை) மூன்றையும் திருத்தியது."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Easy", "level": "TNPSC Group 1" }
  },

  # 45. FR + Preamble Connection (Basic Conceptual) - Ans: D
  {
    "id": "FR_E_045",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Easy",
    "question_type": "Basic Conceptual",
    "question": {
      "en": "Which specific objective promised in the Preamble of the Constitution is operationalized primarily by the Right to Freedom guaranteed in Articles 19 to 22?",
      "ta": "அரசியலமைப்பின் முகவுரையில் வாக்களிக்கப்பட்ட எந்த குறிப்பிட்ட இலக்கு, உறுப்புகள் 19 முதல் 22 வரை உத்தரவாதம் அளிக்கப்பட்ட சுதந்திர உரிமையால் முதன்மையாகச் செயல்பட வைக்கப்படுகிறது?"
    },
    "options": [
      { "id": "A", "en": "Social Justice", "ta": "சமூக நீதி" },
      { "id": "B", "en": "Economic Equality", "ta": "பொருளாதார சமத்துவம்" },
      { "id": "C", "en": "Sovereignty of the Nation", "ta": "நாட்டின் இறையாண்மை" },
      { "id": "D", "en": "Liberty of Thought, Expression, Belief, Faith and Worship", "ta": "எண்ணம், கருத்து வெளிப்பாடு, நம்பிக்கை, பக்தி மற்றும் வழிபாட்டு சுதந்திரம் (Liberty)" }
    ],
    "correct_answer": "D",
    "explanation": {
      "en": "The Right to Freedom (Arts 19-22) operationalizes the Preamble's promise to secure LIBERTY of Thought, Expression, Belief, Faith, and Worship for all citizens.",
      "ta": "சுதந்திர உரிமை (உறுப்புகள் 19-22) அனைத்துக் குடிமக்களுக்கும் எண்ணம், கருத்து வெளிப்பாடு, நம்பிக்கை, பக்தி, வழிபாட்டு சுதந்திரத்தை (LIBERTY) வழங்குவதற்கான முகவுரையின் வாக்குறுதியைச் செயல்படுத்துகிறது."
    },
    "why_not_others": {
      "A": { "en": "Social Justice is operationalized via Arts 15, 16 & DPSPs.", "ta": "சமூக நீதி உறுப்புகள் 15, 16 & DPSP மூலம் செயல்படுகிறது." },
      "B": { "en": "Economic Equality is guided via DPSPs (Art 39).", "ta": "பொருளாதார சமத்துவம் DPSP (39) மூலம் வழிகாட்டப்படுகிறது." },
      "C": { "en": "Sovereignty refers to external/internal state authority.", "ta": "இறையாண்மை அரசின் அதிகாரத்தைக் குறிக்கிறது." },
      "D": { "en": "Correct. Liberty of thought/expression is operationalized by Arts 19-22.", "ta": "சரி. எண்ணம்/கருத்து சுதந்திரம் உறுப்புகள் 19-22 மூலம் செயல்படுகிறது." }
    },
    "tnpsc_tip": {
      "en": "Preamble states philosophy; Part III Fundamental Rights provides enforceable protections.",
      "ta": "முகவுரை தத்துவத்தைக் கூறுகிறது; பகுதி III அடிப்படை உரிமைகள் அமல்படுத்தக்கூடிய பாதுகாப்புகளை வழங்குகிறது."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Easy", "level": "TNPSC Group 1" }
  },

  # 46. 103rd Amendment EWS Reservation (Case / Amendment) - Ans: A
  {
    "id": "FR_E_046",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Easy",
    "question_type": "Case / Amendment",
    "question": {
      "en": "Which Constitutional Amendment Act inserted Articles 15(6) and 16(6) providing up to 10% reservation for Economically Weaker Sections (EWS)?",
      "ta": "பொருளாதாரத்தில் நலிவடைந்த பிரிவினருக்கு (EWS) 10% வரை இடஒதுக்கீடு வழங்கும் உறுப்புகள் 15(6) மற்றும் 16(6)-ஐச் சேர்த்த அரசியலமைப்பு திருத்தச் சட்டம் எது?"
    },
    "options": [
      { "id": "A", "en": "103rd Constitutional Amendment Act, 2019", "ta": "103வது அரசியலமைப்பு திருத்தச் சட்டம், 2019" },
      { "id": "B", "en": "102nd Constitutional Amendment Act, 2018", "ta": "102வது அரசியலமைப்பு திருத்தச் சட்டம், 2018" },
      { "id": "C", "en": "104th Constitutional Amendment Act, 2020", "ta": "104வது அரசியலமைப்பு திருத்தச் சட்டம், 2020" },
      { "id": "D", "en": "105th Constitutional Amendment Act, 2021", "ta": "105வது அரசியலமைப்பு திருத்தச் சட்டம், 2021" }
    ],
    "correct_answer": "A",
    "explanation": {
      "en": "The 103rd Constitutional Amendment Act, 2019 introduced 10% EWS reservation in educational admissions (Art 15(6)) and public employment (Art 16(6)), upheld in Janhit Abhiyan case (2022).",
      "ta": "2019-ன் 103வது அரசியலமைப்பு திருத்தச் சட்டம் கல்விச் சேர்க்கை (15(6)) மற்றும் பொது வேலைவாய்ப்பில் (16(6)) 10% EWS இடஒதுக்கீட்டை அறிமுகப்படுத்தியது; இது ஜன்ஹித் அபியான் வழக்கில் (2022) உறுதி செய்யப்பட்டது."
    },
    "why_not_others": {
      "A": { "en": "Correct. 103rd CAA 2019 introduced EWS reservation.", "ta": "சரி. 103வது திருத்தம் 2019 EWS இடஒதுக்கீட்டை அறிமுகப்படுத்தியது." },
      "B": { "en": "102nd CAA 2018 gave constitutional status to NCBC.", "ta": "102வது திருத்தம் 2018 NCBC-க்கு அரசியலமைப்பு அந்தஸ்து அளித்தது." },
      "C": { "en": "104th CAA 2020 extended SC/ST reservation in Lok Sabha and discontinued Anglo-Indian nomination.", "ta": "104வது திருத்தம் 2020 எஸ்சி/எஸ்டி இடஒதுக்கீட்டை நீட்டித்து ஆங்கிலோ-இந்தியர் நியமனத்தை நீக்கியது." },
      "D": { "en": "105th CAA 2021 restored state power to identify SEBCs.", "ta": "105வது திருத்தம் 2021 SEBC-களை அடையாளம் காண மாநில அதிகாரத்தை மீட்டெடுத்தது." }
    },
    "tnpsc_tip": {
      "en": "103rd CAA 2019 added Arts 15(6) and 16(6) for 10% EWS quota.",
      "ta": "103வது திருத்தம் 2019 10% EWS ஒதுக்கீட்டிற்காக உறுப்புகள் 15(6) மற்றும் 16(6)-ஐச் சேர்த்தது."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Easy", "level": "TNPSC Group 1" }
  },

  # 47. Quo Warranto Meaning (Direct Factual) - Ans: C
  {
    "id": "FR_E_047",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Easy",
    "question_type": "Direct",
    "question": {
      "en": "What is the literal meaning of the Latin phrase 'Quo Warranto'?",
      "ta": "'Quo Warranto' (தகுதி வினா) என்ற இலத்தீன் தொடரின் நேரடிப் பொருள் என்ன?"
    },
    "options": [
      { "id": "A", "en": "We Command", "ta": "நாங்கள் கட்டளையிடுகிறோம்" },
      { "id": "B", "en": "To have the body of", "ta": "உடலைக் கொண்டு வா" },
      { "id": "C", "en": "By what authority or warrant?", "ta": "எந்த அதிகாரத்தின் அல்லது ஆணையின் அடிப்படையில்?" },
      { "id": "D", "en": "To be fully informed", "ta": "முழுமையாகத் தெரிந்த கொள்ள" }
    ],
    "correct_answer": "C",
    "explanation": {
      "en": "Quo Warranto literally means 'By what authority or warrant?'. It is issued to inquire into the legality of a person's claim to a public office.",
      "ta": "Quo Warranto என்பதன் நேரடிப் பொருள் 'எந்த அதிகாரத்தின் அல்லது ஆணையின் அடிப்படையில்?' என்பதாகும். ஒரு நபர் பொதுப் பதவியைக் கோருவதன் சட்டப்பூர்வத் தன்மையை வினவ இது பிறப்பிக்கப்படுகிறது."
    },
    "why_not_others": {
      "A": { "en": "We Command is Mandamus.", "ta": "நாங்கள் கட்டளையிடுகிறோம் என்பது Mandamus." },
      "B": { "en": "To have the body of is Habeas Corpus.", "ta": "உடலைக் கொண்டு வா என்பது Habeas Corpus." },
      "C": { "en": "Correct. Quo Warranto = By what authority?", "ta": "சரி. Quo Warranto = எந்த அதிகாரத்தின் அடிப்படையில்?" },
      "D": { "en": "To be fully informed is Certiorari.", "ta": "முழுமையாகத் தெரிந்து கொள்ள என்பது Certiorari." }
    },
    "tnpsc_tip": {
      "en": "Quo Warranto prevents illegal usurpation of a public office.",
      "ta": "தகுதி வினா பேராணை பொதுப் பதவியைச் சட்டவிரோதமாகக் கைப்பற்றுவதைத் தடுக்கிறது."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Easy", "level": "TNPSC Group 1" }
  },

  # 48. Certiorari Meaning & Quashing Order (Simple Application) - Ans: B
  {
    "id": "FR_E_048",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Easy",
    "question_type": "Simple Application",
    "question": {
      "en": "A lower tribunal passes an illegal order exceeding its jurisdiction, violating natural justice. Which writ should be sought from the High Court to QUASH this illegal order?",
      "ta": "ஒரு கீழ் தீர்ப்பாயம் இயற்கை நீதியை மீறி தனது அதிகார வரம்பைக் கடந்து ஒரு சட்டவிரோத உத்தரவைப் பிறப்பிக்கிறது. இந்தச் சட்டவிரோத உத்தரவை ரத்து செய்ய (QUASH) உயர் நீதிமன்றத்திலிருந்து எந்தப் பேராணையைக் கேட்க வேண்டும்?"
    },
    "options": [
      { "id": "A", "en": "Mandamus", "ta": "செயலுறுத்தும் பேராணை (Mandamus)" },
      { "id": "B", "en": "Certiorari", "ta": "நெறிமுறையுறுத்தும் பேராணை (Certiorari)" },
      { "id": "C", "en": "Habeas Corpus", "ta": "ஆட்கொணர்வு பேராணை (Habeas Corpus)" },
      { "id": "D", "en": "Quo Warranto", "ta": "தகுதி வினா பேராணை (Quo Warranto)" }
    ],
    "correct_answer": "B",
    "explanation": {
      "en": "Certiorari is issued by a higher court to quash an illegal order passed by a lower court, tribunal, or administrative authority in excess of jurisdiction.",
      "ta": "கீழ் நீதிமன்றம், தீர்ப்பாயம் அல்லது நிர்வாக அமைப்பு அதிகார வரம்பை மீறி பிறப்பித்த சட்டவிரோத உத்தரவை ரத்து செய்ய (quash) நெறிமுறையுறுத்தும் பேராணை (Certiorari) வழங்கப்படுகிறது."
    },
    "why_not_others": {
      "A": { "en": "Mandamus commands performance of a positive duty.", "ta": "Mandamus ஒரு நேர்மறை பணியைச் செய்யக் கட்டளையிடுகிறது." },
      "B": { "en": "Correct. Certiorari is used to QUASH an illegal order passed.", "ta": "சரி. பிறப்பிக்கப்பட்ட சட்டவிரோத உத்தரவை ரத்து செய்ய Certiorari பயன்படுகிறது." },
      "C": { "en": "Habeas Corpus is for illegal detention of a person.", "ta": "Habeas Corpus நபரைச் சட்டவிரோதமாகக் காவலில் வைப்பதற்கு உரியது." },
      "D": { "en": "Quo Warranto is for usurpation of public office.", "ta": "Quo Warranto பொதுப் பதவியைக் கைப்பற்றுவதற்கு உரியது." }
    },
    "tnpsc_tip": {
      "en": "Certiorari = 'To quash an unconstitutional/illegal order already passed'.",
      "ta": "Certiorari = 'ஏற்கனவே பிறப்பிக்கப்பட்ட அரசியலமைப்புக்கு முரணான/சட்டவிரோத உத்தரவை ரத்து செய்தல்'."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Easy", "level": "TNPSC Group 1" }
  },

  # 49. Article 31A/31B 9th Schedule Purpose (Article-based) - Ans: A
  {
    "id": "FR_E_049",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Easy",
    "question_type": "Article-based",
    "question": {
      "en": "Which Schedule was added to the Constitution by the 1st Constitutional Amendment Act, 1951 along with Article 31B to protect land reform laws from judicial review?",
      "ta": "நிலச்சீர்திருத்தச் சட்டங்களை நீதித்துறை ஆய்விலிருந்து பாதுகாக்க உறுப்பு 31B உடன் சேர்த்து 1வது அரசியலமைப்பு திருத்தச் சட்டம் 1951 மூலம் அரசியலமைப்பில் சேர்க்கப்பட்ட அட்டவணை எது?"
    },
    "options": [
      { "id": "A", "en": "Ninth Schedule (9th Schedule)", "ta": "ஒன்பதாவது அட்டவணை (9th Schedule)" },
      { "id": "B", "en": "Tenth Schedule (10th Schedule)", "ta": "பத்தாவது அட்டவணை (10th Schedule)" },
      { "id": "C", "en": "Eleventh Schedule (11th Schedule)", "ta": "பதினோராவது அட்டவணை (11th Schedule)" },
      { "id": "D", "en": "Twelfth Schedule (12th Schedule)", "ta": "பன்னிரண்டாவது அட்டவணை (12th Schedule)" }
    ],
    "correct_answer": "A",
    "explanation": {
      "en": "The 1st Constitutional Amendment Act, 1951 inserted Article 31B and the Ninth Schedule to shield land reform and agrarian reform laws from fundamental rights challenge.",
      "ta": "1951-ன் 1வது அரசியலமைப்பு திருத்தச் சட்டம் நிலச்சீர்திருத்தச் சட்டங்களை அடிப்படை உரிமை சவால்களிலிருந்து பாதுகாக்க உறுப்பு 31B மற்றும் ஒன்பதாவது அட்டவணையைச் சேர்த்தது."
    },
    "why_not_others": {
      "A": { "en": "Correct. 9th Schedule was inserted by 1st CAA 1951.", "ta": "சரி. 9வது அட்டவணை 1வது திருத்தம் 1951 மூலம் சேர்க்கப்பட்டது." },
      "B": { "en": "10th Schedule (Anti-defection) was inserted by 52nd CAA 1985.", "ta": "10வது அட்டவணை (கட்சித் தாவல்) 52வது திருத்தம் 1985 மூலம் சேர்க்கப்பட்டது." },
      "C": { "en": "11th Schedule (Panchayats) was inserted by 73rd CAA 1992.", "ta": "11வது அட்டவணை (ஊராட்சிகள்) 73வது திருத்தம் 1992 மூலம் சேர்க்கப்பட்டது." },
      "D": { "en": "12th Schedule (Municipalities) was inserted by 74th CAA 1992.", "ta": "12வது அட்டவணை (நகராட்சிகள்) 74வது திருத்தம் 1992 மூலம் சேர்க்கப்பட்டது." }
    },
    "tnpsc_tip": {
      "en": "I.R. Coelho Case (2007): Laws placed in 9th Schedule after April 24, 1973 are open to judicial review if they violate Basic Structure.",
      "ta": "ஐ.ஆர். கொஹெலோ வழக்கு (2007): 24 ஏப்ரல் 1973-க்கு பின் 9வது அட்டவணையில் வைக்கப்பட்ட சட்டங்கள் அடிப்படை கட்டமைப்பை மீறினால் நீதித்துறை ஆய்வுக்கு உட்பட்டவை."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Easy", "level": "TNPSC Group 1" }
  },

  # 50. Total Fundamental Rights Articles Range (Direct Factual) - Ans: B
  {
    "id": "FR_E_050",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Easy",
    "question_type": "Direct",
    "question": {
      "en": "What is the complete span of Articles covered under Part III of the Constitution of India?",
      "ta": "இந்திய அரசியலமைப்பின் பகுதி III-ன் கீழ் உள்ளடக்கப்பட்டுள்ள உறுப்புகளின் முழுமையான வரம்பு என்ன?"
    },
    "options": [
      { "id": "A", "en": "Articles 5 to 11", "ta": "உறுப்புகள் 5 முதல் 11 வரை" },
      { "id": "B", "en": "Articles 12 to 35", "ta": "உறுப்புகள் 12 முதல் 35 வரை" },
      { "id": "C", "en": "Articles 36 to 51", "ta": "உறுப்புகள் 36 முதல் 51 வரை" },
      { "id": "D", "en": "Articles 52 to 78", "ta": "உறுப்புகள் 52 முதல் 78 வரை" }
    ],
    "correct_answer": "B",
    "explanation": {
      "en": "Part III of the Constitution spans Articles 12 to 35, comprehensively covering the definition of State, judicial review, fundamental rights, remedies, and parliamentary legislative powers.",
      "ta": "அரசியலமைப்பின் பகுதி III உறுப்புகள் 12 முதல் 35 வரை உள்ளது, இது அரசின் வரையறை, நீதித்துறை ஆய்வு, அடிப்படை உரிமைகள், தீர்வுகள் மற்றும் நாடாளுமன்றச் சட்ட அதிகாரங்களை விரிவாக உள்ளடக்குகிறது."
    },
    "why_not_others": {
      "A": { "en": "Articles 5 to 11 cover Citizenship (Part II).", "ta": "உறுப்புகள் 5 முதல் 11 வரை குடியுரிமை (பகுதி II)." },
      "B": { "en": "Correct. Part III spans Articles 12 to 35.", "ta": "சரி. பகுதி III உறுப்புகள் 12 முதல் 35 வரை உள்ளடக்கப்பட்டுள்ளது." },
      "C": { "en": "Articles 36 to 51 cover DPSP (Part IV).", "ta": "உறுப்புகள் 36 முதல் 51 வரை DPSP (பகுதி IV)." },
      "D": { "en": "Articles 52 to 78 cover Union Executive (Part V).", "ta": "உறுப்புகள் 52 முதல் 78 வரை மத்திய நிர்வாகம் (பகுதி V)." }
    },
    "tnpsc_tip": {
      "en": "Part III = Articles 12 to 35 = Magna Carta of India.",
      "ta": "பகுதி III = உறுப்புகள் 12 முதல் 35 = இந்தியாவின் மகா சாசனம்."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Easy", "level": "TNPSC Group 1" }
  }
]

target_file = "data/questions/polity/fundamental_rights_easy.json"
os.makedirs(os.path.dirname(target_file), exist_ok=True)

with open(target_file, "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"Successfully generated '{target_file}' with exactly {len(questions)} Easy MCQs!")
