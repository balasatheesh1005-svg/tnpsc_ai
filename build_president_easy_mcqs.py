import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("Building President Easy MCQs Dataset...")

easy_questions = [
  {
    "id": "POLITY_PRESIDENT_EASY_001",
    "subject": "Polity",
    "topic": "President of India",
    "difficulty": "Easy",
    "question_type": "Direct",
    "question": {
      "en": "Which Article of the Indian Constitution states that 'There shall be a President of India'?",
      "ta": "'இந்தியாவிற்கு ஒரு குடியரசுத் தலைவர் இருக்க வேண்டும்' எனக் கூறும் இந்திய அரசியலமைப்பின் உறுப்பு எது?"
    },
    "question_en": "Which Article of the Indian Constitution states that 'There shall be a President of India'?",
    "question_ta": "'இந்தியாவிற்கு ஒரு குடியரசுத் தலைவர் இருக்க வேண்டும்' எனக் கூறும் இந்திய அரசியலமைப்பின் உறுப்பு எது?",
    "options": [
      {"id": "A", "en": "Article 52", "ta": "உறுப்பு 52"},
      {"id": "B", "en": "Article 53", "ta": "உறுப்பு 53"},
      {"id": "C", "en": "Article 54", "ta": "உறுப்பு 54"},
      {"id": "D", "en": "Article 55", "ta": "உறுப்பு 55"}
    ],
    "correct_answer": "A",
    "explanation": {
      "en": "Article 52 creates the office of the President of India as the Head of State and First Citizen of India.",
      "ta": "உறுப்பு 52 நாட்டின் தலைவர் மற்றும் முதல் குடிமகனாக இந்தியக் குடியரசுத் தலைவர் பதவியை உருவாக்குகிறது."
    },
    "explanation_en": "Article 52 creates the office of the President of India as the Head of State and First Citizen of India.",
    "explanation_ta": "உறுப்பு 52 நாட்டின் தலைவர் மற்றும் முதல் குடிமகனாக இந்தியக் குடியரசுத் தலைவர் பதவியை உருவாக்குகிறது.",
    "source_reference": "Part V - Article 52",
    "trap_point": {
      "en": "Do not confuse Article 52 (Creation of Office) with Article 53 (Executive Power of the Union).",
      "ta": "உறுப்பு 52 (பதவி உருவாக்கம்) மற்றும் உறுப்பு 53 (ஒன்றிய நிர்வாக அதிகாரம்) ஆகியவற்றை குழப்பிக் கொள்ள வேண்டாம்."
    },
    "tnpsc_tip": {
      "en": "Article 52 mandates a permanent constitutional office with no interregnum.",
      "ta": "உறுப்பு 52 காலியிடமற்ற நிரந்தர அரசியலமைப்பு பதவியைக் கட்டாயப்படுத்துகிறது."
    },
    "why_not_others": {
      "A": {"en": "Correct. Article 52 establishes the office of President of India.", "ta": "சரி. உறுப்பு 52 இந்தியக் குடியரசுத் தலைவர் பதவியை நிறுவுகிறது."},
      "B": {"en": "Article 53 deals with the executive power of the Union.", "ta": "உறுப்பு 53 ஒன்றியத்தின் நிர்வாக அதிகாரத்தைப் பற்றியது."},
      "C": {"en": "Article 54 deals with the election of the President (Electoral College).", "ta": "உறுப்பு 54 குடியரசுத் தலைவர் தேர்தலைப் (வாக்காளர் குழு) பற்றியது."},
      "D": {"en": "Article 55 deals with the manner/method of election of the President.", "ta": "உறுப்பு 55 குடியரசுத் தலைவர் தேர்தல் முறையைப் பற்றியது."}
    },
    "metadata": {"subject": "Polity", "topic": "President of India", "type": "Easy", "level": "TNPSC Group 1"}
  },
  {
    "id": "POLITY_PRESIDENT_EASY_002",
    "subject": "Polity",
    "topic": "President of India",
    "difficulty": "Easy",
    "question_type": "Direct",
    "question": {
      "en": "Who is the Constitutional Supreme Commander of the Armed Forces of India under Article 53(2)?",
      "ta": "உறுப்பு 53(2)-ன் கீழ் இந்தியப் பாதுகாப்புப் படைகளின் அரசியலமைப்பு உச்சத் தளபதி யார்?"
    },
    "question_en": "Who is the Constitutional Supreme Commander of the Armed Forces of India under Article 53(2)?",
    "question_ta": "உறுப்பு 53(2)-ன் கீழ் இந்தியப் பாதுகாப்புப் படைகளின் அரசியலமைப்பு உச்சத் தளபதி யார்?",
    "options": [
      {"id": "A", "en": "Prime Minister of India", "ta": "இந்தியப் பிரதமர்"},
      {"id": "B", "en": "President of India", "ta": "இந்தியக் குடியரசுத் தலைவர்"},
      {"id": "C", "en": "Union Defence Minister", "ta": "மத்திய பாதுகாப்பு அமைச்சர்"},
      {"id": "D", "en": "Chief of Defence Staff (CDS)", "ta": "பாதுகாப்புப் படைகளின் தலைமை தளபதி"}
    ],
    "correct_answer": "B",
    "explanation": {
      "en": "Article 53(2) expressly vests the Supreme Command of the Defence Forces of the Union in the President of India.",
      "ta": "உறுப்பு 53(2) ஒன்றியத்தின் பாதுகாப்புப் படைகளின் உச்ச தளபதி அதிகாரத்தை இந்தியக் குடியரசுத் தலைவரிடம் வெளிப்படையாக வழங்குகிறது."
    },
    "explanation_en": "Article 53(2) expressly vests the Supreme Command of the Defence Forces of the Union in the President of India.",
    "explanation_ta": "உறுப்பு 53(2) ஒன்றியத்தின் பாதுகாப்புப் படைகளின் உச்ச தளபதி அதிகாரத்தை இந்தியக் குடியரசுத் தலைவரிடம் வெளிப்படையாக வழங்குகிறது.",
    "source_reference": "Part V - Article 53(2)",
    "trap_point": {
      "en": "Do not confuse the Constitutional Supreme Commander (President) with the operational military heads.",
      "ta": "அரசியலமைப்பு உச்சத் தளபதி (குடியரசுத் தலைவர்) மற்றும் இராணுவ செயல்பாட்டுத் தலைவர்களைக் குழப்ப வேண்டாம்."
    },
    "tnpsc_tip": {
      "en": "The exercise of supreme command is regulated by Parliamentary law.",
      "ta": "உச்ச தளபதி அதிகாரத்தின் பயன்பாடு நாடாளுமன்றச் சட்டத்தால் சீர்படுத்தப்படுகிறது."
    },
    "why_not_others": {
      "A": {"en": "PM is the real executive head, but not the constitutional supreme commander.", "ta": "பிரதமர் உண்மை நிர்வாகத் தலைவர், ஆனால் அரசியலமைப்பு உச்சத் தளபதி அல்ல."},
      "B": {"en": "Correct. President is the Supreme Commander under Article 53(2).", "ta": "சரி. உறுப்பு 53(2)-ன் கீழ் குடியரசுத் தலைவரே உச்ச தளபதி ஆவார்."},
      "C": {"en": "Defence Minister holds political cabinet portfolio for defence.", "ta": "பாதுகாப்பு அமைச்சர் பாதுகாப்பிற்கான அரசியல் கேபினட் பொறுப்பை வகிக்கிறார்."},
      "D": {"en": "CDS is the military advisor, not the constitutional supreme commander.", "ta": "சிடிஎஸ் இராணுவ ஆலோசகர் மட்டுமே, அரசியலமைப்பு உச்சத் தளபதி அல்ல."}
    },
    "metadata": {"subject": "Polity", "topic": "President of India", "type": "Easy", "level": "TNPSC Group 1"}
  },
  {
    "id": "POLITY_PRESIDENT_EASY_003",
    "subject": "Polity",
    "topic": "President of India",
    "difficulty": "Easy",
    "question_type": "Direct",
    "question": {
      "en": "What is the minimum age required for a person to be eligible for election as President of India under Article 58?",
      "ta": "உறுப்பு 58-ன் கீழ் ஒரு நபர் இந்தியக் குடியரசுத் தலைவராகத் தேர்ந்தெடுக்கப்படத் தேவையான குறைந்தபட்ச வயது என்ன?"
    },
    "question_en": "What is the minimum age required for a person to be eligible for election as President of India under Article 58?",
    "question_ta": "உறுப்பு 58-ன் கீழ் ஒரு நபர் இந்தியக் குடியரசுத் தலைவராகத் தேர்ந்தெடுக்கப்படத் தேவையான குறைந்தபட்ச வயது என்ன?",
    "options": [
      {"id": "A", "en": "25 years", "ta": "25 ஆண்டுகள்"},
      {"id": "B", "en": "30 years", "ta": "30 ஆண்டுகள்"},
      {"id": "C", "en": "35 years", "ta": "35 ஆண்டுகள்"},
      {"id": "D", "en": "40 years", "ta": "40 ஆண்டுகள்"}
    ],
    "correct_answer": "C",
    "explanation": {
      "en": "Article 58(1)(b) specifies that a candidate for Presidential election must have completed the age of 35 years.",
      "ta": "உறுப்பு 58(1)(b) குடியரசுத் தலைவர் தேர்தலில் போட்டியிடும் வேட்பாளர் 35 வயதைப் பூர்த்தி செய்திருக்க வேண்டும் எனக் குறிப்பிடுகிறது."
    },
    "explanation_en": "Article 58(1)(b) specifies that a candidate for Presidential election must have completed the age of 35 years.",
    "explanation_ta": "உறுப்பு 58(1)(b) குடியரசுத் தலைவர் தேர்தலில் போட்டியிடும் வேட்பாளர் 35 வயதைப் பூர்த்தி செய்திருக்க வேண்டும் எனக் குறிப்பிடுகிறது.",
    "source_reference": "Part V - Article 58",
    "trap_point": {
      "en": "Do not confuse Lok Sabha age limit (25) or Rajya Sabha age limit (30) with President/VP/Governor age limit (35).",
      "ta": "மக்களவை வயது வரம்பு (25) அல்லது மாநிலங்களவை வயது வரம்பை (30) குடியரசுத் தலைவர்/துணைத் தலைவர்/ஆளுநர் வயது வரம்புடன் (35) குழப்ப வேண்டாம்."
    },
    "tnpsc_tip": {
      "en": "President, Vice-President, and State Governor all require a minimum age of 35 years.",
      "ta": "குடியரசுத் தலைவர், துணைத் தலைவர் மற்றும் மாநில ஆளுநர் ஆகிய அனைவருக்கும் குறைந்தபட்ச வயது 35 ஆகும்."
    },
    "why_not_others": {
      "A": {"en": "25 years is the minimum age for Lok Sabha and Legislative Assembly.", "ta": "25 வயது என்பது மக்களவை மற்றும் சட்டப்பேரவைக்கான குறைந்தபட்ச வயது."},
      "B": {"en": "30 years is the minimum age for Rajya Sabha and Legislative Council.", "ta": "30 வயது என்பது மாநிலங்களவை மற்றும் சட்ட மேலவைக்கான குறைந்தபட்ச வயது."},
      "C": {"en": "Correct. 35 years is mandatory under Article 58.", "ta": "சரி. உறுப்பு 58-ன் கீழ் 35 வயது கட்டாயமாகும்."},
      "D": {"en": "40 years is not a prescribed minimum age qualification under the Constitution.", "ta": "40 வயது என்பது அரசியலமைப்பில் குறிப்பிடப்பட்ட தகுதி அல்ல."}
    },
    "metadata": {"subject": "Polity", "topic": "President of India", "type": "Easy", "level": "TNPSC Group 1"}
  },
  {
    "id": "POLITY_PRESIDENT_EASY_004",
    "subject": "Polity",
    "topic": "President of India",
    "difficulty": "Easy",
    "question_type": "Direct",
    "question": {
      "en": "Who administers the Oath of Office to the President of India under Article 60?",
      "ta": "உறுப்பு 60-ன் கீழ் இந்தியக் குடியரசுத் தலைவருக்குப் பதவிப் பிரமாணம் செய்து வைப்பவர் யார்?"
    },
    "question_en": "Who administers the Oath of Office to the President of India under Article 60?",
    "question_ta": "உறுப்பு 60-ன் கீழ் இந்தியக் குடியரசுத் தலைவருக்குப் பதவிப் பிரமாணம் செய்து வைப்பவர் யார்?",
    "options": [
      {"id": "A", "en": "Prime Minister of India", "ta": "இந்தியப் பிரதமர்"},
      {"id": "B", "en": "Vice-President of India", "ta": "இந்தியத் துணைத் தலைவர்"},
      {"id": "C", "en": "Speaker of Lok Sabha", "ta": "மக்களவை சபாநாயகர்"},
      {"id": "D", "en": "Chief Justice of India", "ta": "இந்தியத் தலைமை நீதிபதி"}
    ],
    "correct_answer": "D",
    "explanation": {
      "en": "Article 60 mandates that the oath of office to the President is administered by the Chief Justice of India, or in his absence, the senior-most Judge of the Supreme Court available.",
      "ta": "உறுப்பு 60 குடியரசுத் தலைவரின் பதவிப் பிரமாணம் இந்தியத் தலைமை நீதிபதியால் அல்லது அவர் இல்லாத போது உச்ச நீதிமன்றத்தின் மூத்த நீதிபதியால் செய்து வைக்கப்பட வேண்டும் எனக் கட்டாயப்படுத்துகிறது."
    },
    "explanation_en": "Article 60 mandates that the oath of office to the President is administered by the Chief Justice of India, or in his absence, the senior-most Judge of the Supreme Court available.",
    "explanation_ta": "உறுப்பு 60 குடியரசுத் தலைவரின் பதவிப் பிரமாணம் இந்தியத் தலைமை நீதிபதியால் அல்லது அவர் இல்லாத போது உச்ச நீதிமன்றத்தின் மூத்த நீதிபதியால் செய்து வைக்கப்பட வேண்டும் எனக் கட்டாயப்படுத்துகிறது.",
    "source_reference": "Part V - Article 60",
    "trap_point": {
      "en": "President resigns to Vice-President, but takes oath before Chief Justice of India!",
      "ta": "குடியரசுத் தலைவர் துணைத் தலைவரிடம் ராஜினாமா செய்வார், ஆனால் இந்தியத் தலைமை நீதிபதி முன் உறுதிமொழி ஏற்பார்!"
    },
    "tnpsc_tip": {
      "en": "The President's oath text is specified directly in Article 60, NOT in the Third Schedule.",
      "ta": "குடியரசுத் தலைவரின் உறுதிமொழி உரை நேரடியாக உறுப்பு 60-ல் குறிப்பிடப்பட்டுள்ளது, 3வது அட்டவணையில் இல்லை."
    },
    "why_not_others": {
      "A": {"en": "PM does not administer oath to President.", "ta": "பிரதமர் குடியரசுத் தலைவருக்கு உறுதிமொழி செய்து வைப்பதில்லை."},
      "B": {"en": "President resigns to VP, but takes oath before CJI.", "ta": "குடியரசுத் தலைவர் துணைத் தலைவரிடம் ராஜினாமா செய்வார், ஆனால் CJI முன் உறுதிமொழி ஏற்பார்."},
      "C": {"en": "LS Speaker does not administer oath to President.", "ta": "சபாநாயகர் குடியரசுத் தலைவருக்கு உறுதிமொழி செய்து வைப்பதில்லை."},
      "D": {"en": "Correct. CJI (or senior SC Judge) administers oath under Article 60.", "ta": "சரி. உறுப்பு 60-ன் கீழ் CJI (அல்லது மூத்த உச்ச நீதிமன்ற நீதிபதி) உறுதிமொழி செய்து வைப்பார்."}
    },
    "metadata": {"subject": "Polity", "topic": "President of India", "type": "Easy", "level": "TNPSC Group 1"}
  },
  {
    "id": "POLITY_PRESIDENT_EASY_005",
    "subject": "Polity",
    "topic": "President of India",
    "difficulty": "Easy",
    "question_type": "Direct",
    "question": {
      "en": "To whom does the President of India address his written letter of resignation under Article 56(1)(a)?",
      "ta": "உறுப்பு 56(1)(a)-ன் கீழ் இந்தியக் குடியரசுத் தலைவர் தனது எழுத்துப்பூர்வ ராஜினாமா கடிதத்தை யாரிடம் சமர்ப்பிக்க வேண்டும்?"
    },
    "question_en": "To whom does the President of India address his written letter of resignation under Article 56(1)(a)?",
    "question_ta": "உறுப்பு 56(1)(a)-ன் கீழ் இந்தியக் குடியரசுத் தலைவர் தனது எழுத்துப்பூர்வ ராஜினாமா கடிதத்தை யாரிடம் சமர்ப்பிக்க வேண்டும்?",
    "options": [
      {"id": "A", "en": "Chief Justice of India", "ta": "இந்தியத் தலைமை நீதிபதி"},
      {"id": "B", "en": "Vice-President of India", "ta": "இந்தியத் துணைத் தலைவர்"},
      {"id": "C", "en": "Prime Minister of India", "ta": "இந்தியப் பிரதமர்"},
      {"id": "D", "en": "Speaker of Lok Sabha", "ta": "மக்களவை சபாநாயகர்"}
    ],
    "correct_answer": "B",
    "explanation": {
      "en": "Article 56(1)(a) states that the President may, by writing under his hand addressed to the Vice-President, resign his office.",
      "ta": "உறுப்பு 56(1)(a) குடியரசுத் தலைவர் துணைத் தலைவருக்குத் தன் கையொப்பமிட்ட எழுத்துப்பூர்வ கடிதம் மூலம் தனது பதவியை ராஜினாமா செய்யலாம் எனக் கூறுகிறது."
    },
    "explanation_en": "Article 56(1)(a) states that the President may, by writing under his hand addressed to the Vice-President, resign his office.",
    "explanation_ta": "உறுப்பு 56(1)(a) குடியரசுத் தலைவர் துணைத் தலைவருக்குத் தன் கையொப்பமிட்ட எழுத்துப்பூர்வ கடிதம் மூலம் தனது பதவியை ராஜினாமா செய்யலாம் எனக் கூறுகிறது.",
    "source_reference": "Part V - Article 56(1)(a)",
    "trap_point": {
      "en": "The Vice-President must immediately communicate the President's resignation to the Speaker of Lok Sabha under Article 56(2).",
      "ta": "துணைத் தலைவர் குடியரசுத் தலைவரின் ராஜினாமாவை உறுப்பு 56(2)-ன் கீழ் உடனடியாக மக்களவை சபாநாயகருக்குத் தெரிவிக்க வேண்டும்."
    },
    "tnpsc_tip": {
      "en": "President resigns to Vice-President, and Vice-President resigns to President (mutual cross-resignation).",
      "ta": "குடியரசுத் தலைவர் துணைத் தலைவரிடமும், துணைத் தலைவர் குடியரசுத் தலைவரிடமும் ராஜினாமா செய்வார்கள்."
    },
    "why_not_others": {
      "A": {"en": "CJI administers oath, but does not receive resignation.", "ta": "CJI உறுதிமொழி செய்து வைப்பார், ஆனால் ராஜினாமாவைப் பெறுவதில்லை."},
      "B": {"en": "Correct. Resignation letter is addressed to the Vice-President.", "ta": "சரி. ராஜினாமா கடிதம் துணைத் தலைவருக்கு எழுதப்படும்."},
      "C": {"en": "PM does not receive President's resignation.", "ta": "பிரதமர் குடியரசுத் தலைவரின் ராஜினாமாவைப் பெறுவதில்லை."},
      "D": {"en": "Speaker receives communication from VP, but letter is addressed to VP.", "ta": "துணைத் தலைவரிடமிருந்து தகவல் சபாநாயகருக்குச் செல்லும், ஆனால் கடிதம் துணைத் தலைவருக்கே எழுதப்படும்."}
    },
    "metadata": {"subject": "Polity", "topic": "President of India", "type": "Easy", "level": "TNPSC Group 1"}
  },
  {
    "id": "POLITY_PRESIDENT_EASY_006",
    "subject": "Polity",
    "topic": "President of India",
    "difficulty": "Easy",
    "question_type": "Direct",
    "question": {
      "en": "Which Article of the Indian Constitution empowers the President to grant pardons, reprieves, respites or remissions of punishment?",
      "ta": "இந்தியக் குடியரசுத் தலைவருக்கு மன்னிப்பு, இடைநிறுத்தம், நிவாரணம் அல்லது தண்டனைக் குறைப்பு வழங்க அதிகாரமளிக்கும் அரசியலமைப்பு உறுப்பு எது?"
    },
    "question_en": "Which Article of the Indian Constitution empowers the President to grant pardons, reprieves, respites or remissions of punishment?",
    "question_ta": "இந்தியக் குடியரசுத் தலைவருக்கு மன்னிப்பு, இடைநிறுத்தம், நிவாரணம் அல்லது தண்டனைக் குறைப்பு வழங்க அதிகாரமளிக்கும் அரசியலமைப்பு உறுப்பு எது?",
    "options": [
      {"id": "A", "en": "Article 72", "ta": "உறுப்பு 72"},
      {"id": "B", "en": "Article 74", "ta": "உறுப்பு 74"},
      {"id": "C", "en": "Article 123", "ta": "உறுப்பு 123"},
      {"id": "D", "en": "Article 143", "ta": "உறுப்பு 143"}
    ],
    "correct_answer": "A",
    "explanation": {
      "en": "Article 72 grants the President power to grant pardons, reprieves, respites, or remissions of punishment, or to suspend, remit, or commute sentences.",
      "ta": "உறுப்பு 72 குடியரசுத் தலைவருக்கு மன்னிப்பு, இடைநிறுத்தம், நிவாரணம், தண்டனைக் குறைப்பு அல்லது தண்டனை மாற்றுதல் வழங்க அதிகாரமளிக்கிறது."
    },
    "explanation_en": "Article 72 grants the President power to grant pardons, reprieves, respites, or remissions of punishment, or to suspend, remit, or commute sentences.",
    "explanation_ta": "உறுப்பு 72 குடியரசுத் தலைவருக்கு மன்னிப்பு, இடைநிறுத்தம், நிவாரணம், தண்டனைக் குறைப்பு அல்லது தண்டனை மாற்றுதல் வழங்க அதிகாரமளிக்கிறது.",
    "source_reference": "Part V - Article 72",
    "trap_point": {
      "en": "Do not confuse President's pardoning power (Article 72) with Governor's pardoning power (Article 161).",
      "ta": "குடியரசுத் தலைவரின் மன்னிப்பளிக்கும் அதிகாரத்தையும் (உறுப்பு 72) ஆளுநரின் மன்னிப்பளிக்கும் அதிகாரத்தையும் (உறுப்பு 161) குழப்ப வேண்டாம்."
    },
    "tnpsc_tip": {
      "en": "President (Art 72) can pardon death sentences and court-martial sentences, whereas Governor (Art 161) cannot.",
      "ta": "குடியரசுத் தலைவரால் (உறுப்பு 72) மரண தண்டனை & ராணுவ நீதிமன்றத் தண்டனையை மன்னிக்க முடியும், ஆளுநரால் (உறுப்பு 161) முடியாது."
    },
    "why_not_others": {
      "A": {"en": "Correct. Article 72 deals with President's pardoning power.", "ta": "சரி. உறுப்பு 72 குடியரசுத் தலைவரின் மன்னிப்பளிக்கும் அதிகாரம் பற்றியது."},
      "B": {"en": "Article 74 deals with Council of Ministers to aid and advise President.", "ta": "உறுப்பு 74 அமைச்சரவையின் உதவி மற்றும் ஆலோசனை பற்றியது."},
      "C": {"en": "Article 123 deals with Ordinance-making power.", "ta": "உறுப்பு 123 அவசரச் சட்ட அதிகாரம் பற்றியது."},
      "D": {"en": "Article 143 deals with Supreme Court advisory jurisdiction.", "ta": "உறுப்பு 143 உச்ச நீதிமன்ற ஆலோசனை அதிகார வரம்பு பற்றியது."}
    },
    "metadata": {"subject": "Polity", "topic": "President of India", "type": "Easy", "level": "TNPSC Group 1"}
  },
  {
    "id": "POLITY_PRESIDENT_EASY_007",
    "subject": "Polity",
    "topic": "President of India",
    "difficulty": "Easy",
    "question_type": "Direct",
    "question": {
      "en": "Under which Article of the Constitution can the President promulgate Ordinances when Parliament is not in session?",
      "ta": "நாடாளுமன்றக் கூட்டத்தொடர் இல்லாத போது குடியரசுத் தலைவர் எந்த உறுப்பின் கீழ் அவசரச் சட்டங்களைப் பிறப்பிக்க முடியும்?"
    },
    "question_en": "Under which Article of the Constitution can the President promulgate Ordinances when Parliament is not in session?",
    "question_ta": "நாடாளுமன்றக் கூட்டத்தொடர் இல்லாத போது குடியரசுத் தலைவர் எந்த உறுப்பின் கீழ் அவசரச் சட்டங்களைப் பிறப்பிக்க முடியும்?",
    "options": [
      {"id": "A", "en": "Article 111", "ta": "உறுப்பு 111"},
      {"id": "B", "en": "Article 123", "ta": "உறுப்பு 123"},
      {"id": "C", "en": "Article 213", "ta": "உறுப்பு 213"},
      {"id": "D", "en": "Article 356", "ta": "உறுப்பு 356"}
    ],
    "correct_answer": "B",
    "explanation": {
      "en": "Article 123 empowers the President to promulgate Ordinances during recess of Parliament if satisfied that circumstances exist requiring immediate action.",
      "ta": "உறுப்பு 123 நாடாளுமன்றக் கூட்டத்தொடர் இல்லாத போது உடனடி நடவடிக்கை தேவைப்படும் சூழல் இருப்பதாகத் திருப்தியடைந்தால் அவசரச் சட்டங்களைப் பிறப்பிக்கக் குடியரசுத் தலைவருக்கு அதிகாரமளிக்கிறது."
    },
    "explanation_en": "Article 123 empowers the President to promulgate Ordinances during recess of Parliament if satisfied that circumstances exist requiring immediate action.",
    "explanation_ta": "உறுப்பு 123 நாடாளுமன்றக் கூட்டத்தொடர் இல்லாத போது உடனடி நடவடிக்கை தேவைப்படும் சூழல் இருப்பதாகத் திருப்தியடைந்தால் அவசரச் சட்டங்களைப் பிறப்பிக்கக் குடியரசுத் தலைவருக்கு அதிகாரமளிக்கிறது.",
    "source_reference": "Part V - Article 123",
    "trap_point": {
      "en": "Remember Article 123 is for President's Ordinance and Article 213 is for Governor's Ordinance (easy mnemonic: swap 1 and 2!).",
      "ta": "உறுப்பு 123 குடியரசுத் தலைவர் அவசரச் சட்டம், உறுப்பு 213 ஆளுநர் அவசரச் சட்டம் (1 மற்றும் 2 இடங்களை மாற்றி நினைவில் கொள்க!)."
    },
    "tnpsc_tip": {
      "en": "Max life of Ordinance under Art 123 = 6 months + 6 weeks.",
      "ta": "உறுப்பு 123-ன் கீழ் அவசரச் சட்டத்தின் அதிகபட்ச காலம் = 6 மாதங்கள் + 6 வாரங்கள்."
    },
    "why_not_others": {
      "A": {"en": "Article 111 deals with Assent to Bills.", "ta": "உறுப்பு 111 மசோதாக்களுக்கு ஒப்புதல் அளிப்பது பற்றியது."},
      "B": {"en": "Correct. Article 123 is President's Ordinance power.", "ta": "சரி. உறுப்பு 123 குடியரசுத் தலைவரின் அவசரச் சட்ட அதிகாரம்."},
      "C": {"en": "Article 213 is Governor's Ordinance power in States.", "ta": "உறுப்பு 213 மாநிலங்களில் ஆளுநரின் அவசரச் சட்ட அதிகாரம்."},
      "D": {"en": "Article 356 deals with President's Rule in States.", "ta": "உறுப்பு 356 மாநிலங்களில் குடியரசுத் தலைவர் ஆட்சி பற்றியது."}
    },
    "metadata": {"subject": "Polity", "topic": "President of India", "type": "Easy", "level": "TNPSC Group 1"}
  },
  {
    "id": "POLITY_PRESIDENT_EASY_008",
    "subject": "Polity",
    "topic": "President of India",
    "difficulty": "Easy",
    "question_type": "Direct",
    "question": {
      "en": "Which Constitutional Amendment Act made Presidential assent MANDATORY for Constitutional Amendment Bills?",
      "ta": "அரசியலமைப்பு திருத்த மசோதாக்களுக்குக் குடியரசுத் தலைவரின் ஒப்புதலைக் கட்டாயமாக்கிய அரசியலமைப்பு திருத்தச் சட்டம் எது?"
    },
    "question_en": "Which Constitutional Amendment Act made Presidential assent MANDATORY for Constitutional Amendment Bills?",
    "question_ta": "அரசியலமைப்பு திருத்த மசோதாக்களுக்குக் குடியரசுத் தலைவரின் ஒப்புதலைக் கட்டாயமாக்கிய அரசியலமைப்பு திருத்தச் சட்டம் எது?",
    "options": [
      {"id": "A", "en": "24th Amendment Act, 1971", "ta": "24வது திருத்தச் சட்டம், 1971"},
      {"id": "B", "en": "42nd Amendment Act, 1976", "ta": "42வது திருத்தச் சட்டம், 1976"},
      {"id": "C", "en": "44th Amendment Act, 1978", "ta": "44வது திருத்தச் சட்டம், 1978"},
      {"id": "D", "en": "86th Amendment Act, 2002", "ta": "86வது திருத்தச் சட்டம், 2002"}
    ],
    "correct_answer": "A",
    "explanation": {
      "en": "The 24th Constitutional Amendment Act, 1971 amended Article 368 to make it mandatory for the President to give assent to Constitutional Amendment Bills.",
      "ta": "1971-ன் 24வது அரசியலமைப்பு திருத்தச் சட்டம் உறுப்பு 368-ஐத் திருத்தி அரசியலமைப்பு திருத்த மசோதாக்களுக்குக் குடியரசுத் தலைவர் ஒப்புதல் அளிப்பதைக் கட்டாயமாக்கியது."
    },
    "explanation_en": "The 24th Constitutional Amendment Act, 1971 amended Article 368 to make it mandatory for the President to give assent to Constitutional Amendment Bills.",
    "explanation_ta": "1971-ன் 24வது அரசியலமைப்பு திருத்தச் சட்டம் உறுப்பு 368-ஐத் திருத்தி அரசியலமைப்பு திருத்த மசோதாக்களுக்குக் குடியரசுத் தலைவர் ஒப்புதல் அளிப்பதைக் கட்டாயமாக்கியது.",
    "source_reference": "Part XX - Article 368",
    "trap_point": {
      "en": "President cannot withhold assent or return a Constitutional Amendment Bill for reconsideration.",
      "ta": "அரசியலமைப்பு திருத்த மசோதாவைக் குடியரசுத் தலைவர் ஒப்புதலை நிறுத்தவோ மறுபரிசீலனைக்குத் திருப்பவோ முடியாது."
    },
    "tnpsc_tip": {
      "en": "24th CAA 1971 amended Article 368 and Article 13 to override Golak Nath judgment.",
      "ta": "24வது திருத்தம் 1971 கோலக்நாத் தீர்ப்பை மாற்றியமைக்க உறுப்புகள் 368 மற்றும் 13-ஐத் திருத்தியது."
    },
    "why_not_others": {
      "A": {"en": "Correct. 24th CAA 1971 made assent mandatory for Art 368 bills.", "ta": "சரி. 24வது திருத்தம் 1971 உறுப்பு 368 மசோதாக்களுக்கு ஒப்புதலைக் கட்டாயமாக்கியது."},
      "B": {"en": "42nd CAA 1976 made Cabinet advice binding under Art 74.", "ta": "42வது திருத்தம் 1976 உறுப்பு 74-ன் கீழ் அமைச்சரவை ஆலோசனையைக் கட்டாயமாக்கியது."},
      "C": {"en": "44th CAA 1978 added 1-time reconsideration proviso to Art 74.", "ta": "44வது திருத்தம் 1978 உறுப்பு 74-ல் ஒருமுறை மறுபரிசீலனை விதியைச் சேர்த்தது."},
      "D": {"en": "86th CAA 2002 made Right to Education a Fundamental Right (Art 21A).", "ta": "86வது திருத்தம் 2002 கல்வி உரிமையை அடிப்படை உரிமையாக்கியது (உறுப்பு 21A)."}
    },
    "metadata": {"subject": "Polity", "topic": "President of India", "type": "Easy", "level": "TNPSC Group 1"}
  },
  {
    "id": "POLITY_PRESIDENT_EASY_009",
    "subject": "Polity",
    "topic": "President of India",
    "difficulty": "Easy",
    "question_type": "Direct",
    "question": {
      "en": "Which Article of the Constitution contains the procedure for Impeachment of the President of India?",
      "ta": "இந்தியக் குடியரசுத் தலைவரின் பதவி நீக்க நடைமுறையைக் கொண்டுள்ள அரசியலமைப்பு உறுப்பு எது?"
    },
    "question_en": "Which Article of the Constitution contains the procedure for Impeachment of the President of India?",
    "question_ta": "இந்தியக் குடியரசுத் தலைவரின் பதவி நீக்க நடைமுறையைக் கொண்டுள்ள அரசியலமைப்பு உறுப்பு எது?",
    "options": [
      {"id": "A", "en": "Article 56", "ta": "உறுப்பு 56"},
      {"id": "B", "en": "Article 60", "ta": "உறுப்பு 60"},
      {"id": "C", "en": "Article 61", "ta": "உறுப்பு 61"},
      {"id": "D", "en": "Article 62", "ta": "உறுப்பு 62"}
    ],
    "correct_answer": "C",
    "explanation": {
      "en": "Article 61 lays down the detailed quasi-judicial procedure for the impeachment of the President of India for 'Violation of the Constitution'.",
      "ta": "உறுப்பு 61 'அரசியலமைப்பு மீறலுக்காக' இந்தியக் குடியரசுத் தலைவரைப் பதவி நீக்கம் செய்வதற்கான விரிவான பகுதி-நீதிமன்ற நடைமுறையைக் வழங்குகிறது."
    },
    "explanation_en": "Article 61 lays down the detailed quasi-judicial procedure for the impeachment of the President of India for 'Violation of the Constitution'.",
    "explanation_ta": "உறுப்பு 61 'அரசியலமைப்பு மீறலுக்காக' இந்தியக் குடியரசுத் தலைவரைப் பதவி நீக்கம் செய்வதற்கான விரிவான பகுதி-நீதிமன்ற நடைமுறையைக் வழங்குகிறது.",
    "source_reference": "Part V - Article 61",
    "trap_point": {
      "en": "Article 56(1)(b) mentions that President may be removed by impeachment, but Article 61 prescribes the actual PROCEDURE.",
      "ta": "உறுப்பு 56(1)(b) பதவி நீக்கம் மூலம் நீக்கப்படலாம் எனக் குறிப்பிடுகிறது, ஆனால் உறுப்பு 61 மட்டுமே நடைமுறையைக் கூறுகிறது."
    },
    "tnpsc_tip": {
      "en": "Impeachment resolution requires 14 days notice and 2/3rd TOTAL membership majority in both Houses.",
      "ta": "பதவி நீக்கத் தீர்மானத்திற்கு 14 நாட்கள் அறிவிப்பும் இரு அவைகளிலும் 2/3 பங்கு மொத்த உறுப்பினர் பெரும்பான்மையும் தேவை."
    },
    "why_not_others": {
      "A": {"en": "Article 56 specifies term of office and mentions impeachment ground.", "ta": "உறுப்பு 56 பதவிக்காலம் மற்றும் பதவி நீக்கக் காரணத்தைக் குறிப்பிடுகிறது."},
      "B": {"en": "Article 60 specifies the Oath or Affirmation.", "ta": "உறுப்பு 60 உறுதிமொழியைக் குறிப்பிடுகிறது."},
      "C": {"en": "Correct. Article 61 is the Impeachment Procedure.", "ta": "சரி. உறுப்பு 61 பதவி நீக்க நடைமுறையாகும்."},
      "D": {"en": "Article 62 specifies time of holding election to fill vacancy.", "ta": "உறுப்பு 62 காலியிடத் தேர்தல் நடத்துவதற்கான கால அவகாசத்தைக் குறிப்பிடுகிறது."}
    },
    "metadata": {"subject": "Polity", "topic": "President of India", "type": "Easy", "level": "TNPSC Group 1"}
  },
  {
    "id": "POLITY_PRESIDENT_EASY_010",
    "subject": "Polity",
    "topic": "President of India",
    "difficulty": "Easy",
    "question_type": "Direct",
    "question": {
      "en": "Within what maximum time period must an election be held to fill a casual vacancy in the office of President caused by death, resignation or removal under Article 62(2)?",
      "ta": "மறைவு, ராஜினாமா அல்லது நீக்கத்தால் ஏற்படும் குடியரசுத் தலைவர் அலுவலகத் தற்செயல் காலியிடத்தை நிரப்ப உறுப்பு 62(2)-ன் கீழ் அதிகபட்சமாக எந்தக் காலத்திற்குள் தேர்தல் நடத்தப்பட வேண்டும்?"
    },
    "question_en": "Within what maximum time period must an election be held to fill a casual vacancy in the office of President caused by death, resignation or removal under Article 62(2)?",
    "question_ta": "மறைவு, ராஜினாமா அல்லது நீக்கத்தால் ஏற்படும் குடியரசுத் தலைவர் அலுவலகத் தற்செயல் காலியிடத்தை நிரப்ப உறுப்பு 62(2)-ன் கீழ் அதிகபட்சமாக எந்தக் காலத்திற்குள் தேர்தல் நடத்தப்பட வேண்டும்?",
    "options": [
      {"id": "A", "en": "1 month", "ta": "1 மாதம்"},
      {"id": "B", "en": "3 months", "ta": "3 மாதங்கள்"},
      {"id": "C", "en": "6 months", "ta": "6 மாதங்கள்"},
      {"id": "D", "en": "1 year", "ta": "1 ஆண்டு"}
    ],
    "correct_answer": "C",
    "explanation": {
      "en": "Article 62(2) mandates that an election to fill a casual vacancy in the office of President shall be held as soon as possible after, and in no case later than six months from, the date of occurrence of the vacancy.",
      "ta": "உறுப்பு 62(2) தற்செயல் காலியிடத்திற்கான தேர்தல் கூடிய விரைவில், எந்தச் சூழலிலும் காலியிடம் ஏற்பட்ட தேதியிலிருந்து 6 மாதங்களுக்குள் நடத்தப்பட வேண்டும் எனக் கட்டாயப்படுத்துகிறது."
    },
    "explanation_en": "Article 62(2) mandates that an election to fill a casual vacancy in the office of President shall be held as soon as possible after, and in no case later than six months from, the date of occurrence of the vacancy.",
    "explanation_ta": "உறுப்பு 62(2) தற்செயல் காலியிடத்திற்கான தேர்தல் கூடிய விரைவில், எந்தச் சூழலிலும் காலியிடம் ஏற்பட்ட தேதியிலிருந்து 6 மாதங்களுக்குள் நடத்தப்பட வேண்டும் எனக் கட்டாயப்படுத்துகிறது.",
    "source_reference": "Part V - Article 62(2)",
    "trap_point": {
      "en": "The newly elected President serves a FULL 5-year term, NOT just the remaining period of predecessor.",
      "ta": "புதிதாகத் தேர்ந்தெடுக்கப்படும் குடியரசுத் தலைவர் முழு 5 ஆண்டுகள் பணியாற்றுவார், மீதமுள்ள காலம் அல்ல."
    },
    "tnpsc_tip": {
      "en": "During this 6-month period, the Vice-President acts as President under Article 65.",
      "ta": "இந்த 6 மாத காலத்தில் உறுப்பு 65-ன் கீழ் துணைத் தலைவர் செயல் குடியரசுத் தலைவராகச் செயல்படுவார்."
    },
    "why_not_others": {
      "A": {"en": "1 month is too short and not the constitutional deadline.", "ta": "1 மாதம் அரசியலமைப்பு காலக்கெடு அல்ல."},
      "B": {"en": "3 months is not the constitutional requirement under Article 62(2).", "ta": "3 மாதங்கள் உறுப்பு 62(2)-ன் கீழ் நிபந்தனை அல்ல."},
      "C": {"en": "Correct. 6 months is the maximum limit under Article 62(2).", "ta": "சரி. உறுப்பு 62(2)-ன் கீழ் 6 மாதங்கள் அதிகபட்ச வரம்பாகும்."},
      "D": {"en": "1 year is incorrect for Presidential casual vacancy.", "ta": "1 ஆண்டு என்பது குடியரசுத் தலைவர் காலியிடத்திற்கு தவறானது."}
    },
    "metadata": {"subject": "Polity", "topic": "President of India", "type": "Easy", "level": "TNPSC Group 1"}
  }
]

# Write easy.json
target_path = "data/questions/polity/president_easy.json"
os.makedirs(os.path.dirname(target_path), exist_ok=True)
with open(target_path, "w", encoding="utf-8") as f:
    json.dump(easy_questions, f, ensure_ascii=False, indent=2)

print(f"✅ Generated {len(easy_questions)} questions in {target_path}")
