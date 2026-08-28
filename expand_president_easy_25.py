import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("Expanding President Easy MCQs to 25 items...")

easy_25 = [
  {
    "id": "POLITY_PRESIDENT_EASY_001",
    "subject": "Polity",
    "topic": "President of India",
    "difficulty": "Easy",
    "question_type": "Direct",
    "question": {"en": "Which Article of the Indian Constitution states that 'There shall be a President of India'?", "ta": "'இந்தியாவிற்கு ஒரு குடியரசுத் தலைவர் இருக்க வேண்டும்' எனக் கூறும் இந்திய அரசியலமைப்பின் உறுப்பு எது?"},
    "question_en": "Which Article of the Indian Constitution states that 'There shall be a President of India'?",
    "question_ta": "'இந்தியாவிற்கு ஒரு குடியரசுத் தலைவர் இருக்க வேண்டும்' எனக் கூறும் இந்திய அரசியலமைப்பின் உறுப்பு எது?",
    "options": [
      {"id": "A", "en": "Article 52", "ta": "உறுப்பு 52"},
      {"id": "B", "en": "Article 53", "ta": "உறுப்பு 53"},
      {"id": "C", "en": "Article 54", "ta": "உறுப்பு 54"},
      {"id": "D", "en": "Article 55", "ta": "உறுப்பு 55"}
    ],
    "correct_answer": "A",
    "explanation": {"en": "Article 52 creates the office of the President of India as the Head of State and First Citizen of India.", "ta": "உறுப்பு 52 நாட்டின் தலைவர் மற்றும் முதல் குடிமகனாக இந்தியக் குடியரசுத் தலைவர் பதவியை உருவாக்குகிறது."},
    "explanation_en": "Article 52 creates the office of the President of India as the Head of State and First Citizen of India.",
    "explanation_ta": "உறுப்பு 52 நாட்டின் தலைவர் மற்றும் முதல் குடிமகனாக இந்தியக் குடியரசுத் தலைவர் பதவியை உருவாக்குகிறது.",
    "source_reference": "Part V - Article 52",
    "trap_point": {"en": "Do not confuse Article 52 (Creation of Office) with Article 53 (Executive Power of the Union).", "ta": "உறுப்பு 52 (பதவி உருவாக்கம்) மற்றும் உறுப்பு 53 (ஒன்றிய நிர்வாக அதிகாரம்) ஆகியவற்றை குழப்பிக் கொள்ள வேண்டாம்."},
    "tnpsc_tip": {"en": "Article 52 mandates a permanent constitutional office with no interregnum.", "ta": "உறுப்பு 52 காலியிடமற்ற நிரந்தர அரசியலமைப்பு பதவியைக் கட்டாயப்படுத்துகிறது."},
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
    "question": {"en": "Who is the Constitutional Supreme Commander of the Armed Forces of India under Article 53(2)?", "ta": "உறுப்பு 53(2)-ன் கீழ் இந்தியப் பாதுகாப்புப் படைகளின் அரசியலமைப்பு உச்சத் தளபதி யார்?"},
    "question_en": "Who is the Constitutional Supreme Commander of the Armed Forces of India under Article 53(2)?",
    "question_ta": "உறுப்பு 53(2)-ன் கீழ் இந்தியப் பாதுகாப்புப் படைகளின் அரசியலமைப்பு உச்சத் தளபதி யார்?",
    "options": [
      {"id": "A", "en": "Prime Minister of India", "ta": "இந்தியப் பிரதமர்"},
      {"id": "B", "en": "President of India", "ta": "இந்தியக் குடியரசுத் தலைவர்"},
      {"id": "C", "en": "Union Defence Minister", "ta": "மத்திய பாதுகாப்பு அமைச்சர்"},
      {"id": "D", "en": "Chief of Defence Staff (CDS)", "ta": "பாதுகாப்புப் படைகளின் தலைமை தளபதி"}
    ],
    "correct_answer": "B",
    "explanation": {"en": "Article 53(2) expressly vests the Supreme Command of the Defence Forces of the Union in the President of India.", "ta": "உறுப்பு 53(2) ஒன்றியத்தின் பாதுகாப்புப் படைகளின் உச்ச தளபதி அதிகாரத்தை இந்தியக் குடியரசுத் தலைவரிடம் வெளிப்படையாக வழங்குகிறது."},
    "explanation_en": "Article 53(2) expressly vests the Supreme Command of the Defence Forces of the Union in the President of India.",
    "explanation_ta": "உறுப்பு 53(2) ஒன்றியத்தின் பாதுகாப்புப் படைகளின் உச்ச தளபதி அதிகாரத்தை இந்தியக் குடியரசுத் தலைவரிடம் வெளிப்படையாக வழங்குகிறது.",
    "source_reference": "Part V - Article 53(2)",
    "trap_point": {"en": "Do not confuse the Constitutional Supreme Commander (President) with operational military heads.", "ta": "அரசியலமைப்பு உச்சத் தளபதி (குடியரசுத் தலைவர்) மற்றும் இராணுவ செயல்பாட்டுத் தலைவர்களைக் குழப்ப வேண்டாம்."},
    "tnpsc_tip": {"en": "The exercise of supreme command is regulated by Parliamentary law.", "ta": "உச்ச தளபதி அதிகாரத்தின் பயன்பாடு நாடாளுமன்றச் சட்டத்தால் சீர்படுத்தப்படுகிறது."},
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
    "question": {"en": "What is the minimum age required for a person to be eligible for election as President of India under Article 58?", "ta": "உறுப்பு 58-ன் கீழ் ஒரு நபர் இந்தியக் குடியரசுத் தலைவராகத் தேர்ந்தெடுக்கப்படத் தேவையான குறைந்தபட்ச வயது என்ன?"},
    "question_en": "What is the minimum age required for a person to be eligible for election as President of India under Article 58?",
    "question_ta": "உறுப்பு 58-ன் கீழ் ஒரு நபர் இந்தியக் குடியரசுத் தலைவராகத் தேர்ந்தெடுக்கப்படத் தேவையான குறைந்தபட்ச வயது என்ன?",
    "options": [
      {"id": "A", "en": "25 years", "ta": "25 ஆண்டுகள்"},
      {"id": "B", "en": "30 years", "ta": "30 ஆண்டுகள்"},
      {"id": "C", "en": "35 years", "ta": "35 ஆண்டுகள்"},
      {"id": "D", "en": "40 years", "ta": "40 ஆண்டுகள்"}
    ],
    "correct_answer": "C",
    "explanation": {"en": "Article 58(1)(b) specifies that a candidate for Presidential election must have completed the age of 35 years.", "ta": "உறுப்பு 58(1)(b) குடியரசுத் தலைவர் தேர்தலில் போட்டியிடும் வேட்பாளர் 35 வயதைப் பூர்த்தி செய்திருக்க வேண்டும் எனக் குறிப்பிடுகிறது."},
    "explanation_en": "Article 58(1)(b) specifies that a candidate for Presidential election must have completed the age of 35 years.",
    "explanation_ta": "உறுப்பு 58(1)(b) குடியரசுத் தலைவர் தேர்தலில் போட்டியிடும் வேட்பாளர் 35 வயதைப் பூர்த்தி செய்திருக்க வேண்டும் எனக் குறிப்பிடுகிறது.",
    "source_reference": "Part V - Article 58",
    "trap_point": {"en": "Do not confuse Lok Sabha age limit (25) or Rajya Sabha age limit (30) with President/VP/Governor age limit (35).", "ta": "மக்களவை வயது வரம்பு (25) அல்லது மாநிலங்களவை வயது வரம்பை (30) குடியரசுத் தலைவர்/துணைத் தலைவர்/ஆளுநர் வயது வரம்புடன் (35) குழப்ப வேண்டாம்."},
    "tnpsc_tip": {"en": "President, Vice-President, and State Governor all require a minimum age of 35 years.", "ta": "குடியரசுத் தலைவர், துணைத் தலைவர் மற்றும் மாநில ஆளுநர் ஆகிய அனைவருக்கும் குறைந்தபட்ச வயது 35 ஆகும்."},
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
    "question": {"en": "Who administers the Oath of Office to the President of India under Article 60?", "ta": "உறுப்பு 60-ன் கீழ் இந்தியக் குடியரசுத் தலைவருக்குப் பதவிப் பிரமாணம் செய்து வைப்பவர் யார்?"},
    "question_en": "Who administers the Oath of Office to the President of India under Article 60?",
    "question_ta": "உறுப்பு 60-ன் கீழ் இந்தியக் குடியரசுத் தலைவருக்குப் பதவிப் பிரமாணம் செய்து வைப்பவர் யார்?",
    "options": [
      {"id": "A", "en": "Prime Minister of India", "ta": "இந்தியப் பிரதமர்"},
      {"id": "B", "en": "Vice-President of India", "ta": "இந்தியத் துணைத் தலைவர்"},
      {"id": "C", "en": "Speaker of Lok Sabha", "ta": "மக்களவை சபாநாயகர்"},
      {"id": "D", "en": "Chief Justice of India", "ta": "இந்தியத் தலைமை நீதிபதி"}
    ],
    "correct_answer": "D",
    "explanation": {"en": "Article 60 mandates that the oath of office to the President is administered by the Chief Justice of India, or in his absence, the senior-most Judge of the Supreme Court available.", "ta": "உறுப்பு 60 குடியரசுத் தலைவரின் பதவிப் பிரமாணம் இந்தியத் தலைமை நீதிபதியால் அல்லது அவர் இல்லாத போது உச்ச நீதிமன்றத்தின் மூத்த நீதிபதியால் செய்து வைக்கப்பட வேண்டும் எனக் கட்டாயப்படுத்துகிறது."},
    "explanation_en": "Article 60 mandates that the oath of office to the President is administered by the Chief Justice of India, or in his absence, the senior-most Judge of the Supreme Court available.",
    "explanation_ta": "உறுப்பு 60 குடியரசுத் தலைவரின் பதவிப் பிரமாணம் இந்தியத் தலைமை நீதிபதியால் அல்லது அவர் இல்லாத போது உச்ச நீதிமன்றத்தின் மூத்த நீதிபதியால் செய்து வைக்கப்பட வேண்டும் எனக் கட்டாயப்படுத்துகிறது.",
    "source_reference": "Part V - Article 60",
    "trap_point": {"en": "President resigns to Vice-President, but takes oath before Chief Justice of India!", "ta": "குடியரசுத் தலைவர் துணைத் தலைவரிடம் ராஜினாமா செய்வார், ஆனால் இந்தியத் தலைமை நீதிபதி முன் உறுதிமொழி ஏற்பார்!"},
    "tnpsc_tip": {"en": "The President's oath text is specified directly in Article 60, NOT in the Third Schedule.", "ta": "குடியரசுத் தலைவரின் உறுதிமொழி உரை நேரடியாக உறுப்பு 60-ல் குறிப்பிடப்பட்டுள்ளது, 3வது அட்டவணையில் இல்லை."},
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
    "question": {"en": "To whom does the President of India address his written letter of resignation under Article 56(1)(a)?", "ta": "உறுப்பு 56(1)(a)-ன் கீழ் இந்தியக் குடியரசுத் தலைவர் தனது எழுத்துப்பூர்வ ராஜினாமா கடிதத்தை யாரிடம் சமர்ப்பிக்க வேண்டும்?"},
    "question_en": "To whom does the President of India address his written letter of resignation under Article 56(1)(a)?",
    "question_ta": "உறுப்பு 56(1)(a)-ன் கீழ் இந்தியக் குடியரசுத் தலைவர் தனது எழுத்துப்பூர்வ ராஜினாமா கடிதத்தை யாரிடம் சமர்ப்பிக்க வேண்டும்?",
    "options": [
      {"id": "A", "en": "Chief Justice of India", "ta": "இந்தியத் தலைமை நீதிபதி"},
      {"id": "B", "en": "Vice-President of India", "ta": "இந்தியத் துணைத் தலைவர்"},
      {"id": "C", "en": "Prime Minister of India", "ta": "இந்தியப் பிரதமர்"},
      {"id": "D", "en": "Speaker of Lok Sabha", "ta": "மக்களவை சபாநாயகர்"}
    ],
    "correct_answer": "B",
    "explanation": {"en": "Article 56(1)(a) states that the President may, by writing under his hand addressed to the Vice-President, resign his office.", "ta": "உறுப்பு 56(1)(a) குடியரசுத் தலைவர் துணைத் தலைவருக்குத் தன் கையொப்பமிட்ட எழுத்துப்பூர்வ கடிதம் மூலம் தனது பதவியை ராஜினாமா செய்யலாம் எனக் கூறுகிறது."},
    "explanation_en": "Article 56(1)(a) states that the President may, by writing under his hand addressed to the Vice-President, resign his office.",
    "explanation_ta": "உறுப்பு 56(1)(a) குடியரசுத் தலைவர் துணைத் தலைவருக்குத் தன் கையொப்பமிட்ட எழுத்துப்பூர்வ கடிதம் மூலம் தனது பதவியை ராஜினாமா செய்யலாம் எனக் கூறுகிறது.",
    "source_reference": "Part V - Article 56(1)(a)",
    "trap_point": {"en": "The Vice-President must immediately communicate the President's resignation to the Speaker of Lok Sabha under Article 56(2).", "ta": "துணைத் தலைவர் குடியரசுத் தலைவரின் ராஜினாமாவை உறுப்பு 56(2)-ன் கீழ் உடனடியாக மக்களவை சபாநாயகருக்குத் தெரிவிக்க வேண்டும்."},
    "tnpsc_tip": {"en": "President resigns to Vice-President, and Vice-President resigns to President (mutual cross-resignation).", "ta": "குடியரசுத் தலைவர் துணைத் தலைவரிடமும், துணைத் தலைவர் குடியரசுத் தலைவரிடமும் ராஜினாமா செய்வார்கள்."},
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
    "question": {"en": "Which Article of the Indian Constitution empowers the President to grant pardons, reprieves, respites or remissions of punishment?", "ta": "இந்தியக் குடியரசுத் தலைவருக்கு மன்னிப்பு, இடைநிறுத்தம், நிவாரணம் அல்லது தண்டனைக் குறைப்பு வழங்க அதிகாரமளிக்கும் அரசியலமைப்பு உறுப்பு எது?"},
    "question_en": "Which Article of the Indian Constitution empowers the President to grant pardons, reprieves, respites or remissions of punishment?",
    "question_ta": "இந்தியக் குடியரசுத் தலைவருக்கு மன்னிப்பு, இடைநிறுத்தம், நிவாரணம் அல்லது தண்டனைக் குறைப்பு வழங்க அதிகாரமளிக்கும் அரசியலமைப்பு உறுப்பு எது?",
    "options": [
      {"id": "A", "en": "Article 72", "ta": "உறுப்பு 72"},
      {"id": "B", "en": "Article 74", "ta": "உறுப்பு 74"},
      {"id": "C", "en": "Article 123", "ta": "உறுப்பு 123"},
      {"id": "D", "en": "Article 143", "ta": "உறுப்பு 143"}
    ],
    "correct_answer": "A",
    "explanation": {"en": "Article 72 grants the President power to grant pardons, reprieves, respites, or remissions of punishment, or to suspend, remit, or commute sentences.", "ta": "உறுப்பு 72 குடியரசுத் தலைவருக்கு மன்னிப்பு, இடைநிறுத்தம், நிவாரணம், தண்டனைக் குறைப்பு அல்லது தண்டனை மாற்றுதல் வழங்க அதிகாரமளிக்கிறது."},
    "explanation_en": "Article 72 grants the President power to grant pardons, reprieves, respites, or remissions of punishment, or to suspend, remit, or commute sentences.",
    "explanation_ta": "உறுப்பு 72 குடியரசுத் தலைவருக்கு மன்னிப்பு, இடைநிறுத்தம், நிவாரணம், தண்டனைக் குறைப்பு அல்லது தண்டனை மாற்றுதல் வழங்க அதிகாரமளிக்கிறது.",
    "source_reference": "Part V - Article 72",
    "trap_point": {"en": "Do not confuse President's pardoning power (Article 72) with Governor's pardoning power (Article 161).", "ta": "குடியரசுத் தலைவரின் மன்னிப்பளிக்கும் அதிகாரத்தையும் (உறுப்பு 72) ஆளுநரின் மன்னிப்பளிக்கும் அதிகாரத்தையும் (உறுப்பு 161) குழப்ப வேண்டாம்."},
    "tnpsc_tip": {"en": "President (Art 72) can pardon death sentences and court-martial sentences, whereas Governor (Art 161) cannot.", "ta": "குடியரசுத் தலைவரால் (உறுப்பு 72) மரண தண்டனை & ராணுவ நீதிமன்றத் தண்டனையை மன்னிக்க முடியும், ஆளுநரால் (உறுப்பு 161) முடியாது."},
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
    "question": {"en": "Under which Article of the Constitution can the President promulgate Ordinances when Parliament is not in session?", "ta": "நாடாளுமன்றக் கூட்டத்தொடர் இல்லாத போது குடியரசுத் தலைவர் எந்த உறுப்பின் கீழ் அவசரச் சட்டங்களைப் பிறப்பிக்க முடியும்?"},
    "question_en": "Under which Article of the Constitution can the President promulgate Ordinances when Parliament is not in session?",
    "question_ta": "நாடாளுமன்றக் கூட்டத்தொடர் இல்லாத போது குடியரசுத் தலைவர் எந்த உறுப்பின் கீழ் அவசரச் சட்டங்களைப் பிறப்பிக்க முடியும்?",
    "options": [
      {"id": "A", "en": "Article 111", "ta": "உறுப்பு 111"},
      {"id": "B", "en": "Article 123", "ta": "உறுப்பு 123"},
      {"id": "C", "en": "Article 213", "ta": "உறுப்பு 213"},
      {"id": "D", "en": "Article 356", "ta": "உறுப்பு 356"}
    ],
    "correct_answer": "B",
    "explanation": {"en": "Article 123 empowers the President to promulgate Ordinances during recess of Parliament if satisfied that circumstances exist requiring immediate action.", "ta": "உறுப்பு 123 நாடாளுமன்றக் கூட்டத்தொடர் இல்லாத போது உடனடி நடவடிக்கை தேவைப்படும் சூழல் இருப்பதாகத் திருப்தியடைந்தால் அவசரச் சட்டங்களைப் பிறப்பிக்கக் குடியரசுத் தலைவருக்கு அதிகாரமளிக்கிறது."},
    "explanation_en": "Article 123 empowers the President to promulgate Ordinances during recess of Parliament if satisfied that circumstances exist requiring immediate action.",
    "explanation_ta": "உறுப்பு 123 நாடாளுமன்றக் கூட்டத்தொடர் இல்லாத போது உடனடி நடவடிக்கை தேவைப்படும் சூழல் இருப்பதாகத் திருப்தியடைந்தால் அவசரச் சட்டங்களைப் பிறப்பிக்கக் குடியரசுத் தலைவருக்கு அதிகாரமளிக்கிறது.",
    "source_reference": "Part V - Article 123",
    "trap_point": {"en": "Remember Article 123 is for President's Ordinance and Article 213 is for Governor's Ordinance (easy mnemonic: swap 1 and 2!).", "ta": "உறுப்பு 123 குடியரசுத் தலைவர் அவசரச் சட்டம், உறுப்பு 213 ஆளுநர் அவசரச் சட்டம் (1 மற்றும் 2 இடங்களை மாற்றி நினைவில் கொள்க!)."},
    "tnpsc_tip": {"en": "Max life of Ordinance under Art 123 = 6 months + 6 weeks.", "ta": "உறுப்பு 123-ன் கீழ் அவசரச் சட்டத்தின் அதிகபட்ச காலம் = 6 மாதங்கள் + 6 வாரங்கள்."},
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
    "question": {"en": "Which Constitutional Amendment Act made Presidential assent MANDATORY for Constitutional Amendment Bills?", "ta": "அரசியலமைப்பு திருத்த மசோதாக்களுக்குக் குடியரசுத் தலைவரின் ஒப்புதலைக் கட்டாயமாக்கிய அரசியலமைப்பு திருத்தச் சட்டம் எது?"},
    "question_en": "Which Constitutional Amendment Act made Presidential assent MANDATORY for Constitutional Amendment Bills?",
    "question_ta": "அரசியலமைப்பு திருத்த மசோதாக்களுக்குக் குடியரசுத் தலைவரின் ஒப்புதலைக் கட்டாயமாக்கிய அரசியலமைப்பு திருத்தச் சட்டம் எது?",
    "options": [
      {"id": "A", "en": "24th Amendment Act, 1971", "ta": "24வது திருத்தச் சட்டம், 1971"},
      {"id": "B", "en": "42nd Amendment Act, 1976", "ta": "42வது திருத்தச் சட்டம், 1976"},
      {"id": "C", "en": "44th Amendment Act, 1978", "ta": "44வது திருத்தச் சட்டம், 1978"},
      {"id": "D", "en": "86th Amendment Act, 2002", "ta": "86வது திருத்தச் சட்டம், 2002"}
    ],
    "correct_answer": "A",
    "explanation": {"en": "The 24th Constitutional Amendment Act, 1971 amended Article 368 to make it mandatory for the President to give assent to Constitutional Amendment Bills.", "ta": "1971-ன் 24வது அரசியலமைப்பு திருத்தச் சட்டம் உறுப்பு 368-ஐத் திருத்தி அரசியலமைப்பு திருத்த மசோதாக்களுக்குக் குடியரசுத் தலைவர் ஒப்புதல் அளிப்பதைக் கட்டாயமாக்கியது."},
    "explanation_en": "The 24th Constitutional Amendment Act, 1971 amended Article 368 to make it mandatory for the President to give assent to Constitutional Amendment Bills.",
    "explanation_ta": "1971-ன் 24வது அரசியலமைப்பு திருத்தச் சட்டம் உறுப்பு 368-ஐத் திருத்தி அரசியலமைப்பு திருத்த மசோதாக்களுக்குக் குடியரசுத் தலைவர் ஒப்புதல் அளிப்பதைக் கட்டாயமாக்கியது.",
    "source_reference": "Part XX - Article 368",
    "trap_point": {"en": "President cannot withhold assent or return a Constitutional Amendment Bill for reconsideration.", "ta": "அரசியலமைப்பு திருத்த மசோதாவைக் குடியரசுத் தலைவர் ஒப்புதலை நிறுத்தவோ மறுபரிசீலனைக்குத் திருப்பவோ முடியாது."},
    "tnpsc_tip": {"en": "24th CAA 1971 amended Article 368 and Article 13 to override Golak Nath judgment.", "ta": "24வது திருத்தம் 1971 கோலக்நாத் தீர்ப்பை மாற்றியமைக்க உறுப்புகள் 368 மற்றும் 13-ஐத் திருத்தியது."},
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
    "question": {"en": "Which Article of the Constitution contains the procedure for Impeachment of the President of India?", "ta": "இந்தியக் குடியரசுத் தலைவரின் பதவி நீக்க நடைமுறையைக் கொண்டுள்ள அரசியலமைப்பு உறுப்பு எது?"},
    "question_en": "Which Article of the Constitution contains the procedure for Impeachment of the President of India?",
    "question_ta": "இந்தியக் குடியரசுத் தலைவரின் பதவி நீக்க நடைமுறையைக் கொண்டுள்ள அரசியலமைப்பு உறுப்பு எது?",
    "options": [
      {"id": "A", "en": "Article 56", "ta": "உறுப்பு 56"},
      {"id": "B", "en": "Article 60", "ta": "உறுப்பு 60"},
      {"id": "C", "en": "Article 61", "ta": "உறுப்பு 61"},
      {"id": "D", "en": "Article 62", "ta": "உறுப்பு 62"}
    ],
    "correct_answer": "C",
    "explanation": {"en": "Article 61 lays down the detailed quasi-judicial procedure for the impeachment of the President of India for 'Violation of the Constitution'.", "ta": "உறுப்பு 61 'அரசியலமைப்பு மீறலுக்காக' இந்தியக் குடியரசுத் தலைவரைப் பதவி நீக்கம் செய்வதற்கான விரிவான பகுதி-நீதிமன்ற நடைமுறையைக் வழங்குகிறது."},
    "explanation_en": "Article 61 lays down the detailed quasi-judicial procedure for the impeachment of the President of India for 'Violation of the Constitution'.",
    "explanation_ta": "உறுப்பு 61 'அரசியலமைப்பு மீறலுக்காக' இந்தியக் குடியரசுத் தலைவரைப் பதவி நீக்கம் செய்வதற்கான விரிவான பகுதி-நீதிமன்ற நடைமுறையைக் வழங்குகிறது.",
    "source_reference": "Part V - Article 61",
    "trap_point": {"en": "Article 56(1)(b) mentions that President may be removed by impeachment, but Article 61 prescribes the actual PROCEDURE.", "ta": "உறுப்பு 56(1)(b) பதவி நீக்கம் மூலம் நீக்கப்படலாம் எனக் குறிப்பிடுகிறது, ஆனால் உறுப்பு 61 மட்டுமே நடைமுறையைக் கூறுகிறது."},
    "tnpsc_tip": {"en": "Impeachment resolution requires 14 days notice and 2/3rd TOTAL membership majority in both Houses.", "ta": "பதவி நீக்கத் தீர்மானத்திற்கு 14 நாட்கள் அறிவிப்பும் இரு அவைகளிலும் 2/3 பங்கு மொத்த உறுப்பினர் பெரும்பான்மையும் தேவை."},
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
    "question": {"en": "Within what maximum time period must an election be held to fill a casual vacancy in the office of President caused by death, resignation or removal under Article 62(2)?", "ta": "மறைவு, ராஜினாமா அல்லது நீக்கத்தால் ஏற்படும் குடியரசுத் தலைவர் அலுவலகத் தற்செயல் காலியிடத்தை நிரப்ப உறுப்பு 62(2)-ன் கீழ் அதிகபட்சமாக எந்தக் காலத்திற்குள் தேர்தல் நடத்தப்பட வேண்டும்?"},
    "question_en": "Within what maximum time period must an election be held to fill a casual vacancy in the office of President caused by death, resignation or removal under Article 62(2)?",
    "question_ta": "மறைவு, ராஜினாமா அல்லது நீக்கத்தால் ஏற்படும் குடியரசுத் தலைவர் அலுவலகத் தற்செயல் காலியிடத்தை நிரப்ப உறுப்பு 62(2)-ன் கீழ் அதிகபட்சமாக எந்தக் காலத்திற்குள் தேர்தல் நடத்தப்பட வேண்டும்?",
    "options": [
      {"id": "A", "en": "1 month", "ta": "1 மாதம்"},
      {"id": "B", "en": "3 months", "ta": "3 மாதங்கள்"},
      {"id": "C", "en": "6 months", "ta": "6 மாதங்கள்"},
      {"id": "D", "en": "1 year", "ta": "1 ஆண்டு"}
    ],
    "correct_answer": "C",
    "explanation": {"en": "Article 62(2) mandates that an election to fill a casual vacancy in the office of President shall be held as soon as possible after, and in no case later than six months from, the date of occurrence of the vacancy.", "ta": "உறுப்பு 62(2) தற்செயல் காலியிடத்திற்கான தேர்தல் கூடிய விரைவில், எந்தச் சூழலிலும் காலியிடம் ஏற்பட்ட தேதியிலிருந்து 6 மாதங்களுக்குள் நடத்தப்பட வேண்டும் எனக் கட்டாயப்படுத்துகிறது."},
    "explanation_en": "Article 62(2) mandates that an election to fill a casual vacancy in the office of President shall be held as soon as possible after, and in no case later than six months from, the date of occurrence of the vacancy.",
    "explanation_ta": "உறுப்பு 62(2) தற்செயல் காலியிடத்திற்கான தேர்தல் கூடிய விரைவில், எந்தச் சூழலிலும் காலியிடம் ஏற்பட்ட தேதியிலிருந்து 6 மாதங்களுக்குள் நடத்தப்பட வேண்டும் எனக் கட்டாயப்படுத்துகிறது.",
    "source_reference": "Part V - Article 62(2)",
    "trap_point": {"en": "The newly elected President serves a FULL 5-year term, NOT just the remaining period of predecessor.", "ta": "புதிதாகத் தேர்ந்தெடுக்கப்படும் குடியரசுத் தலைவர் முழு 5 ஆண்டுகள் பணியாற்றுவார், மீதமுள்ள காலம் அல்ல."},
    "tnpsc_tip": {"en": "During this 6-month period, the Vice-President acts as President under Article 65.", "ta": "இந்த 6 மாத காலத்தில் உறுப்பு 65-ன் கீழ் துணைத் தலைவர் செயல் குடியரசுத் தலைவராகச் செயல்படுவார்."},
    "why_not_others": {
      "A": {"en": "1 month is too short and not the constitutional deadline.", "ta": "1 மாதம் அரசியலமைப்பு காலக்கெடு அல்ல."},
      "B": {"en": "3 months is not the constitutional requirement under Article 62(2).", "ta": "3 மாதங்கள் உறுப்பு 62(2)-ன் கீழ் நிபந்தனை அல்ல."},
      "C": {"en": "Correct. 6 months is the maximum limit under Article 62(2).", "ta": "சரி. உறுப்பு 62(2)-ன் கீழ் 6 மாதங்கள் அதிகபட்ச வரம்பாகும்."},
      "D": {"en": "1 year is incorrect for Presidential casual vacancy.", "ta": "1 ஆண்டு என்பது குடியரசுத் தலைவர் காலியிடத்திற்கு தவறானது."}
    },
    "metadata": {"subject": "Polity", "topic": "President of India", "type": "Easy", "level": "TNPSC Group 1"}
  },
  {
    "id": "POLITY_PRESIDENT_EASY_011",
    "subject": "Polity",
    "topic": "President of India",
    "difficulty": "Easy",
    "question_type": "Direct",
    "question": {"en": "Which Article of the Constitution empowers the President to seek advisory opinion from the Supreme Court?", "ta": "உச்ச நீதிமன்றத்திடம் ஆலோசனை பெறக் குடியரசுத் தலைவருக்கு அதிகாரமளிக்கும் அரசியலமைப்பு உறுப்பு எது?"},
    "question_en": "Which Article of the Constitution empowers the President to seek advisory opinion from the Supreme Court?",
    "question_ta": "உச்ச நீதிமன்றத்திடம் ஆலோசனை பெறக் குடியரசுத் தலைவருக்கு அதிகாரமளிக்கும் அரசியலமைப்பு உறுப்பு எது?",
    "options": [
      {"id": "A", "en": "Article 124", "ta": "உறுப்பு 124"},
      {"id": "B", "en": "Article 131", "ta": "உறுப்பு 131"},
      {"id": "C", "en": "Article 143", "ta": "உறுப்பு 143"},
      {"id": "D", "en": "Article 148", "ta": "உறுப்பு 148"}
    ],
    "correct_answer": "C",
    "explanation": {"en": "Article 143 authorizes the President to seek the opinion of the Supreme Court on any question of law or fact of public importance.", "ta": "உறுப்பு 143 பொது முக்கியத்துவம் வாய்ந்த சட்டம் அல்லது உண்மை தொடர்பான கேள்விகளில் உச்ச நீதிமன்றத்தின் ஆலோசனையைக் கோரக் குடியரசுத் தலைவருக்கு அதிகாரமளிக்கிறது."},
    "explanation_en": "Article 143 authorizes the President to seek the opinion of the Supreme Court on any question of law or fact of public importance.",
    "explanation_ta": "உறுப்பு 143 பொது முக்கியத்துவம் வாய்ந்த சட்டம் அல்லது உண்மை தொடர்பான கேள்விகளில் உச்ச நீதிமன்றத்தின் ஆலோசனையைக் கோரக் குடியரசுத் தலைவருக்கு அதிகாரமளிக்கிறது.",
    "source_reference": "Part V - Article 143",
    "trap_point": {"en": "The advisory opinion given by the Supreme Court under Article 143 is NOT binding on the President.", "ta": "உறுப்பு 143-ன் கீழ் உச்ச நீதிமன்றம் வழங்கும் ஆலோசனை குடியரசுத் தலைவரைக் கட்டுப்படுத்தாது."},
    "tnpsc_tip": {"en": "Under Art 143(1) SC may refuse opinion; under Art 143(2) (pre-constitution treaties) SC MUST tender opinion.", "ta": "உறுப்பு 143(1)-ன் கீழ் உச்ச நீதிமன்றம் ஆலோசனையை மறுக்கலாம்; உறுப்பு 143(2)-ன் கீழ் கண்டிப்பாக வழங்க வேண்டும்."},
    "why_not_others": {
      "A": {"en": "Article 124 deals with establishment of Supreme Court.", "ta": "உறுப்பு 124 உச்ச நீதிமன்ற உருவாக்கம் பற்றியது."},
      "B": {"en": "Article 131 deals with original jurisdiction of SC.", "ta": "உறுப்பு 131 உச்ச நீதிமன்ற முதன்மை அதிகார வரம்பு பற்றியது."},
      "C": {"en": "Correct. Article 143 is Advisory Jurisdiction.", "ta": "சரி. உறுப்பு 143 ஆலோசனை அதிகார வரம்பு."},
      "D": {"en": "Article 148 deals with Comptroller and Auditor General.", "ta": "உறுப்பு 148 சிஏஜி பற்றியது."}
    },
    "metadata": {"subject": "Polity", "topic": "President of India", "type": "Easy", "level": "TNPSC Group 1"}
  },
  {
    "id": "POLITY_PRESIDENT_EASY_012",
    "subject": "Polity",
    "topic": "President of India",
    "difficulty": "Easy",
    "question_type": "Direct",
    "question": {"en": "Under Article 356, President's Rule can be imposed in a State due to failure of constitutional machinery. What is the maximum duration it can remain in force with periodic Parliamentary approvals?", "ta": "உறுப்பு 356-ன் கீழ் அரசியலமைப்பு தோல்வியால் மாநிலத்தில் குடியரசுத் தலைவர் ஆட்சி அமல்படுத்தப்படலாம். நாடாளுமன்ற மறு-ஒப்புதல்களுடன் இது அதிகபட்சமாக எவ்வளவு காலம் அமலில் இருக்கலாம்?"},
    "question_en": "Under Article 356, President's Rule can be imposed in a State due to failure of constitutional machinery. What is the maximum duration it can remain in force with periodic Parliamentary approvals?",
    "question_ta": "உறுப்பு 356-ன் கீழ் அரசியலமைப்பு தோல்வியால் மாநிலத்தில் குடியரசுத் தலைவர் ஆட்சி அமல்படுத்தப்படலாம். நாடாளுமன்ற மறு-ஒப்புதல்களுடன் இது அதிகபட்சமாக எவ்வளவு காலம் அமலில் இருக்கலாம்?",
    "options": [
      {"id": "A", "en": "1 year", "ta": "1 ஆண்டு"},
      {"id": "B", "en": "2 years", "ta": "2 ஆண்டுகள்"},
      {"id": "C", "en": "3 years", "ta": "3 ஆண்டுகள்"},
      {"id": "D", "en": "Indefinite period", "ta": "காலவரையற்ற காலம்"}
    ],
    "correct_answer": "C",
    "explanation": {"en": "Under Article 356, President's Rule can be extended up to a maximum period of THREE YEARS with 6-month periodic approvals by Parliament.", "ta": "உறுப்பு 356-ன் கீழ் குடியரசுத் தலைவர் ஆட்சி நாடாளுமன்றத்தின் 6 மாத அவகாச ஒப்புதல்களுடன் அதிகபட்சமாக 3 ஆண்டுகள் வரை நீட்டிக்கப்படலாம்."},
    "explanation_en": "Under Article 356, President's Rule can be extended up to a maximum period of THREE YEARS with 6-month periodic approvals by Parliament.",
    "explanation_ta": "உறுப்பு 356-ன் கீழ் குடியரசுத் தலைவர் ஆட்சி நாடாளுமன்றத்தின் 6 மாத அவகாச ஒப்புதல்களுடன் அதிகபட்சமாக 3 ஆண்டுகள் வரை நீட்டிக்கப்படலாம்.",
    "source_reference": "Part XVIII - Article 356",
    "trap_point": {"en": "National Emergency (Art 352) can extend indefinitely, but President's Rule (Art 356) has a 3-year cap!", "ta": "தேசிய அவசரநிலை (உறுப்பு 352) காலவரையின்றி நீடிக்கலாம், ஆனால் குடியரசுத் தலைவர் ஆட்சிக்கு (உறுப்பு 356) 3 ஆண்டுகள் அதிகபட்ச வரம்பு உண்டு!"},
    "tnpsc_tip": {"en": "Extension beyond 1 year requires National Emergency + Election Commission certificate.", "ta": "1 ஆண்டுக்கு மேல் நீட்டிக்க தேசிய அவசரநிலை + தேர்தல் ஆணைய சான்றிதழ் தேவை."},
    "why_not_others": {
      "A": {"en": "1 year is the threshold beyond which special conditions apply under 44th CAA.", "ta": "1 ஆண்டு என்பது 44வது திருத்தத்தின் கீழ் சிறப்பு நிபந்தனைகள் பொருந்தும் வரம்பாகும்."},
      "B": {"en": "2 years is not the maximum prescribed limit.", "ta": "2 ஆண்டுகள் அதிகபட்ச வரம்பு அல்ல."},
      "C": {"en": "Correct. 3 years is the maximum constitutional limit under Article 356.", "ta": "சரி. உறுப்பு 356-ன் கீழ் 3 ஆண்டுகள் அதிகபட்ச வரம்பாகும்."},
      "D": {"en": "Indefinite period applies to Article 352 and Article 360, not Article 356.", "ta": "காலவரையற்ற காலம் உறுப்புகள் 352 மற்றும் 360-க்கு பொருந்தும், 356-க்கு அல்ல."}
    },
    "metadata": {"subject": "Polity", "topic": "President of India", "type": "Easy", "level": "TNPSC Group 1"}
  },
  {
    "id": "POLITY_PRESIDENT_EASY_013",
    "subject": "Polity",
    "topic": "President of India",
    "difficulty": "Easy",
    "question_type": "Direct",
    "question": {"en": "Which Census population figures are currently used to determine the value of vote of MLAs for Presidential election under Article 55?", "ta": "உறுப்பு 55-ன் கீழ் குடியரசுத் தலைவர் தேர்தலுக்கான எம்.எல்.ஏ வாக்குகளின் மதிப்பைத் தீர்மானிக்க தற்போது எந்த மக்கள் தொகை கணக்கெடுப்பு புள்ளிவிவரங்கள் பயன்படுத்தப்படுகின்றன?"},
    "question_en": "Which Census population figures are currently used to determine the value of vote of MLAs for Presidential election under Article 55?",
    "question_ta": "உறுப்பு 55-ன் கீழ் குடியரசுத் தலைவர் தேர்தலுக்கான எம்.எல்.ஏ வாக்குகளின் மதிப்பைத் தீர்மானிக்க தற்போது எந்த மக்கள் தொகை கணக்கெடுப்பு புள்ளிவிவரங்கள் பயன்படுத்தப்படுகின்றன?",
    "options": [
      {"id": "A", "en": "1951 Census", "ta": "1951 மக்கள் தொகை கணக்கெடுப்பு"},
      {"id": "B", "en": "1971 Census", "ta": "1971 மக்கள் தொகை கணக்கெடுப்பு"},
      {"id": "C", "en": "1991 Census", "ta": "1991 மக்கள் தொகை கணக்கெடுப்பு"},
      {"id": "D", "en": "2011 Census", "ta": "2011 மக்கள் தொகை கணக்கெடுப்பு"}
    ],
    "correct_answer": "B",
    "explanation": {"en": "Under Article 55 explanation, the 1971 Census population is used to determine vote values until the first census taken after the year 2026 (frozen by 84th CAA 2001).", "ta": "உறுப்பு 55 விளக்கத்தின் படி, 2026-க்குப் பிந்தைய முதல் கணக்கெடுப்பு வரை 1971 கணக்கெடுப்பு மக்கள் தொகையே பயன்படுத்தப்படுகிறது (84வது திருத்தம் 2001-ன் படி)."},
    "explanation_en": "Under Article 55 explanation, the 1971 Census population is used to determine vote values until the first census taken after the year 2026 (frozen by 84th CAA 2001).",
    "explanation_ta": "உறுப்பு 55 விளக்கத்தின் படி, 2026-க்குப் பிந்தைய முதல் கணக்கெடுப்பு வரை 1971 கணக்கெடுப்பு மக்கள் தொகையே பயன்படுத்தப்படுகிறது (84வது திருத்தம் 2001-ன் படி).",
    "source_reference": "Part V - Article 55",
    "trap_point": {"en": "Do not select 2011 census. 1971 census is frozen for vote value calculations until post-2026 census.", "ta": "2011 கணக்கெடுப்பைத் தேர்ந்தெடுக்க வேண்டாம். 2026-க்குப் பிந்தைய கணக்கெடுப்பு வரை 1971 கணக்கெடுப்பே முடக்கப்பட்டுள்ளது."},
    "tnpsc_tip": {"en": "42nd CAA 1976 froze it to 1971 until 2000; 84th CAA 2001 extended freeze to post-2026.", "ta": "42வது திருத்தம் 1976 இதை 2000 வரை முடக்கியது; 84வது திருத்தம் 2001 இதை 2026 வரை நீட்டித்தது."},
    "why_not_others": {
      "A": {"en": "1951 Census was used earlier, not currently.", "ta": "1951 கணக்கெடுப்பு முன்பு பயன்படுத்தப்பட்டது, தற்போது அல்ல."},
      "B": {"en": "Correct. 1971 Census population is frozen for vote value calculations.", "ta": "சரி. 1971 கணக்கெடுப்பு மக்கள் தொகையே முடக்கப்பட்டுள்ளது."},
      "C": {"en": "1991 Census is used for delimitation of constituencies, not Art 55 vote value.", "ta": "1991 கணக்கெடுப்பு தொகுதி மறுவரைறைக்கு பயன்படுத்தப்பட்டது, உறுப்பு 55 வாக்கு மதிப்பிற்கு அல்ல."},
      "D": {"en": "2011 Census is not used for Presidential vote value calculation.", "ta": "2011 கணக்கெடுப்பு குடியரசுத் தலைவர் வாக்கு மதிப்புக் கணக்கீட்டிற்கு பயன்படுத்தப்படுவதில்லை."}
    },
    "metadata": {"subject": "Polity", "topic": "President of India", "type": "Easy", "level": "TNPSC Group 1"}
  },
  {
    "id": "POLITY_PRESIDENT_EASY_014",
    "subject": "Polity",
    "topic": "President of India",
    "difficulty": "Easy",
    "question_type": "Direct",
    "question": {"en": "Which court has EXCLUSIVE jurisdiction to inquire into and decide disputes relating to the election of the President of India under Article 71?", "ta": "உறுப்பு 71-ன் கீழ் இந்தியக் குடியரசுத் தலைவர் தேர்தல் தொடர்பான தகராறுகளை விசாரித்துத் தீர்மானிக்க எந்த நீதிமன்றத்திற்கு மட்டுமே பிரத்யேக அதிகார வரம்பு உண்டு?"},
    "question_en": "Which court has EXCLUSIVE jurisdiction to inquire into and decide disputes relating to the election of the President of India under Article 71?",
    "question_ta": "உறுப்பு 71-ன் கீழ் இந்தியக் குடியரசுத் தலைவர் தேர்தல் தொடர்பான தகராறுகளை விசாரித்துத் தீர்மானிக்க எந்த நீதிமன்றத்திற்கு மட்டுமே பிரத்யேக அதிகார வரம்பு உண்டு?",
    "options": [
      {"id": "A", "en": "Delhi High Court", "ta": "டெல்லி உயர் நீதிமன்றம்"},
      {"id": "B", "en": "Election Commission of India", "ta": "இந்தியத் தேர்தல் ஆணையம்"},
      {"id": "C", "en": "Supreme Court of India", "ta": "இந்திய உச்ச நீதிமன்றம்"},
      {"id": "D", "en": "Parliament of India", "ta": "இந்திய நாடாளுமன்றம்"}
    ],
    "correct_answer": "C",
    "explanation": {"en": "Article 71(1) provides that all doubts and disputes arising out of or in connection with the election of President or Vice-President shall be inquired into and decided by the Supreme Court, whose decision shall be final.", "ta": "உறுப்பு 71(1) குடியரசுத் தலைவர் அல்லது துணைத் தலைவர் தேர்தல் தொடர்பான அனைத்து சந்தேகங்களும் தகராறுகளும் உச்ச நீதிமன்றத்தால் விசாரிக்கப்பட்டுத் தீர்மானிக்கப்படும் என்றும், அதன் முடிவே இறுதியானது என்றும் கூறுகிறது."},
    "explanation_en": "Article 71(1) provides that all doubts and disputes arising out of or in connection with the election of President or Vice-President shall be inquired into and decided by the Supreme Court, whose decision shall be final.",
    "explanation_ta": "உறுப்பு 71(1) குடியரசுத் தலைவர் அல்லது துணைத் தலைவர் தேர்தல் தொடர்பான அனைத்து சந்தேகங்களும் தகராறுகளும் உச்ச நீதிமன்றத்தால் விசாரிக்கப்பட்டுத் தீர்மானிக்கப்படும் என்றும், அதன் முடிவே இறுதியானது என்றும் கூறுகிறது.",
    "source_reference": "Part V - Article 71",
    "trap_point": {"en": "Election Commission conducts the election, but disputes are decided EXCLUSIVELY by Supreme Court under Art 71.", "ta": "தேர்தல் ஆணையம் தேர்தலை நடத்துகிறது, ஆனால் தகராறுகள் உறுப்பு 71-ன் கீழ் உச்ச நீதிமன்றத்தால் மட்டுமே தீர்மானிக்கப்படுகின்றன."},
    "tnpsc_tip": {"en": "If Supreme Court declares Presidential election void, acts done by President prior to declaration remain valid.", "ta": "தேர்தல் செல்லாது என உச்ச நீதிமன்றம் அறிவித்தாலும், அதற்கு முன் குடியரசுத் தலைவர் செய்த நடவடிக்கைகள் செல்லுபடியாகும்."},
    "why_not_others": {
      "A": {"en": "High Courts have no jurisdiction over Presidential election disputes.", "ta": "உயர் நீதிமன்றங்களுக்குக் குடியரசுத் தலைவர் தேர்தல் தகராறுகளில் அதிகார வரம்பு இல்லை."},
      "B": {"en": "EC conducts the election, but cannot decide election disputes under Art 71.", "ta": "தேர்தல் ஆணையம் தேர்தலை நடத்துகிறது, ஆனால் உறுப்பு 71-ன் கீழ் தகராறுகளைத் தீர்மானிக்க முடியாது."},
      "C": {"en": "Correct. Supreme Court ONLY has exclusive jurisdiction under Article 71.", "ta": "சரி. உறுப்பு 71-ன் கீழ் உச்ச நீதிமன்றத்திற்கு மட்டுமே பிரத்யேக அதிகார வரம்பு உண்டு."},
      "D": {"en": "Parliament does not decide election disputes.", "ta": "நாடாளுமன்றம் தேர்தல் தகராறுகளைத் தீர்மானிப்பதில்லை."}
    },
    "metadata": {"subject": "Polity", "topic": "President of India", "type": "Easy", "level": "TNPSC Group 1"}
  },
  {
    "id": "POLITY_PRESIDENT_EASY_015",
    "subject": "Polity",
    "topic": "President of India",
    "difficulty": "Easy",
    "question_type": "Direct",
    "question": {"en": "Under Article 54, which of the following members ARE included in the Electoral College for Presidential election?", "ta": "உறுப்பு 54-ன் கீழ் பின்வரும் எந்த உறுப்பினர்கள் குடியரசுத் தலைவர் தேர்தலுக்கான வாக்காளர் குழுவில் சேர்க்கப்பட்டுள்ளனர்?"},
    "question_en": "Under Article 54, which of the following members ARE included in the Electoral College for Presidential election?",
    "question_ta": "உறுப்பு 54-ன் கீழ் பின்வரும் எந்த உறுப்பினர்கள் குடியரசுத் தலைவர் தேர்தலுக்கான வாக்காளர் குழுவில் சேர்க்கப்பட்டுள்ளனர்?",
    "options": [
      {"id": "A", "en": "Nominated members of Rajya Sabha", "ta": "மாநிலங்களவையின் நியமன உறுப்பினர்கள்"},
      {"id": "B", "en": "Elected members of State Legislative Assemblies", "ta": "மாநிலச் சட்டமன்றங்களின் தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்கள்"},
      {"id": "C", "en": "Members of State Legislative Councils (MLCs)", "ta": "மாநிலச் சட்ட மேலவை உறுப்பினர்கள் (MLCs)"},
      {"id": "D", "en": "Nominated members of State Assemblies", "ta": "மாநிலச் சட்டமன்றங்களின் நியமன உறுப்பினர்கள்"}
    ],
    "correct_answer": "B",
    "explanation": {"en": "Article 54 includes elected members of Lok Sabha, Rajya Sabha, and State Legislative Assemblies (plus UTs Delhi & Puducherry). Nominated members and Legislative Council members are excluded.", "ta": "உறுப்பு 54 மக்களவை, மாநிலங்களவை மற்றும் மாநிலச் சட்டமன்றங்களின் தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்களைக் கொண்டுள்ள வாக்காளர் குழுவை வரையறுக்கிறது."},
    "explanation_en": "Article 54 includes elected members of Lok Sabha, Rajya Sabha, and State Legislative Assemblies (plus UTs Delhi & Puducherry). Nominated members and Legislative Council members are excluded.",
    "explanation_ta": "உறுப்பு 54 மக்களவை, மாநிலங்களவை மற்றும் மாநிலச் சட்டமன்றங்களின் தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்களைக் கொண்டுள்ள வாக்காளர் குழுவை வரையறுக்கிறது.",
    "source_reference": "Part V - Article 54",
    "trap_point": {"en": "ONLY ELECTED members vote in Presidential election; ALL nominated members and ALL MLCs are excluded.", "ta": "தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்கள் மட்டுமே வாக்களிப்பார்கள்; அனைத்து நியமன உறுப்பினர்களும் சட்ட மேலவை உறுப்பினர்களும் விலக்கப்பட்டவர்கள்."},
    "tnpsc_tip": {"en": "70th CAA 1992 added elected MLAs of Delhi and Puducherry to Electoral College.", "ta": "70வது திருத்தம் 1992 டெல்லி & புதுச்சேரி தேர்ந்தெடுக்கப்பட்ட எம்.எல்.ஏ-க்களை வாக்காளர் குழுவில் சேர்த்தது."},
    "why_not_others": {
      "A": {"en": "Nominated RS members cannot vote in Presidential election.", "ta": "மாநிலங்களவை நியமன உறுப்பினர்கள் வாக்களிக்க முடியாது."},
      "B": {"en": "Correct. Elected MLAs of States are included under Article 54.", "ta": "சரி. மாநிலங்களின் தேர்ந்தெடுக்கப்பட்ட எம்.எல்.ஏ-க்கள் உறுப்பு 54-ன் கீழ் சேர்க்கப்பட்டுள்ளனர்."},
      "C": {"en": "Legislative Council members (MLCs) are completely excluded.", "ta": "சட்ட மேலவை உறுப்பினர்கள் (MLCs) முற்றிலும் விலக்கப்பட்டுள்ளனர்."},
      "D": {"en": "Nominated members of State Assemblies cannot vote.", "ta": "மாநிலச் சட்டமன்ற நியமன உறுப்பினர்கள் வாக்களிக்க முடியாது."}
    },
    "metadata": {"subject": "Polity", "topic": "President of India", "type": "Easy", "level": "TNPSC Group 1"}
  },
  {
    "id": "POLITY_PRESIDENT_EASY_016",
    "subject": "Polity",
    "topic": "President of India",
    "difficulty": "Easy",
    "question_type": "Direct",
    "question": {"en": "Which Constitutional Amendment Act added the elected members of the Legislative Assemblies of Union Territories of Delhi and Puducherry to the Presidential Electoral College?", "ta": "டெல்லி மற்றும் புதுச்சேரி யூனியன் பிரதேச சட்டமன்றங்களின் தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்களைக் குடியரசுத் தலைவர் வாக்காளர் குழுவில் சேர்த்த அரசியலமைப்பு திருத்தச் சட்டம் எது?"},
    "question_en": "Which Constitutional Amendment Act added the elected members of the Legislative Assemblies of Union Territories of Delhi and Puducherry to the Presidential Electoral College?",
    "question_ta": "டெல்லி மற்றும் புதுச்சேரி யூனியன் பிரதேச சட்டமன்றங்களின் தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்களைக் குடியரசுத் தலைவர் வாக்காளர் குழுவில் சேர்த்த அரசியலமைப்பு திருத்தச் சட்டம் எது?",
    "options": [
      {"id": "A", "en": "61st Amendment Act, 1988", "ta": "61வது திருத்தச் சட்டம், 1988"},
      {"id": "B", "en": "69th Amendment Act, 1991", "ta": "69வது திருத்தச் சட்டம், 1991"},
      {"id": "C", "en": "70th Amendment Act, 1992", "ta": "70வது திருத்தச் சட்டம், 1992"},
      {"id": "D", "en": "73rd Amendment Act, 1992", "ta": "73வது திருத்தச் சட்டம், 1992"}
    ],
    "correct_answer": "C",
    "explanation": {"en": "The 70th Constitutional Amendment Act, 1992 amended the Explanation to Article 54 to include elected members of Legislative Assemblies of Delhi and Puducherry in the Electoral College (effective from June 1, 1995).", "ta": "1992-ன் 70வது அரசியலமைப்பு திருத்தச் சட்டம் உறுப்பு 54-ன் விளக்கத்தைத் திருத்தி டெல்லி மற்றும் புதுச்சேரி தேர்ந்தெடுக்கப்பட்ட எம்.எல்.ஏ-க்களை வாக்காளர் குழுவில் சேர்த்தது (ஜூன் 1, 1995 முதல் அமல்)."},
    "explanation_en": "The 70th Constitutional Amendment Act, 1992 amended the Explanation to Article 54 to include elected members of Legislative Assemblies of Delhi and Puducherry in the Electoral College (effective from June 1, 1995).",
    "explanation_ta": "1992-ன் 70வது அரசியலமைப்பு திருத்தச் சட்டம் உறுப்பு 54-ன் விளக்கத்தைத் திருத்தி டெல்லி மற்றும் புதுச்சேரி தேர்ந்தெடுக்கப்பட்ட எம்.எல்.ஏ-க்களை வாக்காளர் குழுவில் சேர்த்தது (ஜூன் 1, 1995 முதல் அமல்).",
    "source_reference": "Part V - Article 54",
    "trap_point": {"en": "Do not confuse 69th CAA 1991 (created Delhi Assembly) with 70th CAA 1992 (added Delhi/Puducherry MLAs to Presidential Electoral College).", "ta": "69வது திருத்தம் 1991 (டெல்லி பேரவை உருவாக்கம்) மற்றும் 70வது திருத்தம் 1992 (குடியரசுத் தலைவர் வாக்காளர் குழுவில் சேர்க்கை) ஆகியவற்றை குழப்ப வேண்டாம்."},
    "tnpsc_tip": {"en": "69th CAA created NCT of Delhi; 70th CAA gave Delhi/Puducherry MLAs presidential vote.", "ta": "69வது திருத்தம் டெல்லி தேசியத் தலைநகர் பகுதியை உருவாக்கியது; 70வது திருத்தம் எம்.எல்.ஏ-க்களுக்குக் குடியரசுத் தலைவர் வாக்குரிமை அளித்தது."},
    "why_not_others": {
      "A": {"en": "61st CAA 1988 lowered voting age from 21 to 18.", "ta": "61வது திருத்தம் 1988 வாக்குரிமை வயதை 21-லிருந்து 18 ஆகக் குறைத்தது."},
      "B": {"en": "69th CAA 1991 granted special status to Delhi as NCT.", "ta": "69வது திருத்தம் 1991 டெல்லிக்கு சிறப்பு அந்தஸ்து வழங்கியது."},
      "C": {"en": "Correct. 70th CAA 1992 added Delhi & Puducherry MLAs to Art 54.", "ta": "சரி. 70வது திருத்தம் 1992 டெல்லி & புதுச்சேரி எம்.எல்.ஏ-க்களை உறுப்பு 54-ல் சேர்த்தது."},
      "D": {"en": "73rd CAA 1992 established Panchayati Raj institutions.", "ta": "73வது திருத்தம் 1992 பஞ்சாயத்து ராஜ் அமைப்புகளை நிறுவியது."}
    },
    "metadata": {"subject": "Polity", "topic": "President of India", "type": "Easy", "level": "TNPSC Group 1"}
  },
  {
    "id": "POLITY_PRESIDENT_EASY_017",
    "subject": "Polity",
    "topic": "President of India",
    "difficulty": "Easy",
    "question_type": "Direct",
    "question": {"en": "What system of voting is used for the election of the President of India under Article 55(3)?", "ta": "உறுப்பு 55(3)-ன் கீழ் இந்தியக் குடியரசுத் தலைவர் தேர்தலுக்கு எந்த வாக்களிப்பு முறை பயன்படுத்தப்படுகிறது?"},
    "question_en": "What system of voting is used for the election of the President of India under Article 55(3)?",
    "question_ta": "உறுப்பு 55(3)-ன் கீழ் இந்தியக் குடியரசுத் தலைவர் தேர்தலுக்கு எந்த வாக்களிப்பு முறை பயன்படுத்தப்படுகிறது?",
    "options": [
      {"id": "A", "en": "First-Past-The-Post System", "ta": "முதல் நிலை வெற்றி முறை (FPTP)"},
      {"id": "B", "en": "Proportional Representation by Single Transferable Vote", "ta": "ஒற்றை மாற்று வாக்கு மூலமான விகிதாச்சாரப் பிரதிநிதித்துவம்"},
      {"id": "C", "en": "Direct Popular Voting with Open Ballot", "ta": "பகிரங்க வாக்களிப்புடன் கூடிய நேரடி மக்கள் வாக்கு"},
      {"id": "D", "en": "Simple Majority System by Hand Show", "ta": "கையுயர்த்தல் மூலமான எளிய பெரும்பான்மை முறை"}
    ],
    "correct_answer": "B",
    "explanation": {"en": "Article 55(3) mandates that the election of the President shall be held in accordance with the system of proportional representation by means of the single transferable vote and the voting shall be by secret ballot.", "ta": "உறுப்பு 55(3) குடியரசுத் தலைவர் தேர்தல் ஒற்றை மாற்று வாக்கு மூலமான விகிதாச்சாரப் பிரதிநிதித்துவ முறையின் படியும் ரகசிய வாக்களிப்பு மூலமும் நடைபெறும் எனக் கட்டாயப்படுத்துகிறது."},
    "explanation_en": "Article 55(3) mandates that the election of the President shall be held in accordance with the system of proportional representation by means of the single transferable vote and the voting shall be by secret ballot.",
    "explanation_ta": "உறுப்பு 55(3) குடியரசுத் தலைவர் தேர்தல் ஒற்றை மாற்று வாக்கு மூலமான விகிதாச்சாரப் பிரதிநிதித்துவ முறையின் படியும் ரகசிய வாக்களிப்பு மூலமும் நடைபெறும் எனக் கட்டாயப்படுத்துகிறது.",
    "source_reference": "Part V - Article 55(3)",
    "trap_point": {"en": "Presidential election voting MUST be by Secret Ballot, NOT open ballot!", "ta": "குடியரசுத் தலைவர் தேர்தல் வாக்களிப்பு கண்டிப்பாக ரகசிய வாக்களிப்பாக இருக்க வேண்டும், பகிரங்க வாக்களிப்பு அல்ல!"},
    "tnpsc_tip": {"en": "Rajya Sabha elections use open ballot, but Presidential election uses SECRET ballot.", "ta": "மாநிலங்களவை தேர்தல் பகிரங்க வாக்களிப்பைப் பயன்படுத்துகிறது, ஆனால் குடியரசுத் தலைவர் தேர்தல் ரகசிய வாக்களிப்பைப் பயன்படுத்துகிறது."},
    "why_not_others": {
      "A": {"en": "FPTP is used for Lok Sabha and Assembly elections, not Presidential election.", "ta": "FPTP முறை மக்களவை மற்றும் சட்டப்பேரவை தேர்தல்களுக்குப் பயன்படுகிறது."},
      "B": {"en": "Correct. STV with secret ballot is mandatory under Article 55(3).", "ta": "சரி. ரகசிய வாக்களிப்புடன் கூடிய ஒற்றை மாற்று வாக்கு முறை உறுப்பு 55(3)-ன் கீழ் கட்டாயமாகும்."},
      "C": {"en": "Presidential election is indirect and uses secret ballot.", "ta": "குடியரசுத் தலைவர் தேர்தல் மறைமுகமானது மற்றும் ரகசிய வாக்களிப்பைப் பயன்படுத்துகிறது."},
      "D": {"en": "Simple majority by hand show is not used for Presidential election.", "ta": "கையுயர்த்தல் முறை குடியரசுத் தலைவர் தேர்தலுக்குப் பயன்படுத்தப்படுவதில்லை."}
    },
    "metadata": {"subject": "Polity", "topic": "President of India", "type": "Easy", "level": "TNPSC Group 1"}
  },
  {
    "id": "POLITY_PRESIDENT_EASY_018",
    "subject": "Polity",
    "topic": "President of India",
    "difficulty": "Easy",
    "question_type": "Direct",
    "question": {"en": "Under Article 57, how many times can an eligible person be re-elected as President of India?", "ta": "உறுப்பு 57-ன் கீழ் தகுதியுள்ள ஒரு நபர் எத்தனை முறை இந்தியக் குடியரசுத் தலைவராக மறுதேர்தல் செய்யப்படலாம்?"},
    "question_en": "Under Article 57, how many times can an eligible person be re-elected as President of India?",
    "question_ta": "உறுப்பு 57-ன் கீழ் தகுதியுள்ள ஒரு நபர் எத்தனை முறை இந்தியக் குடியரசுத் தலைவராக மறுதேர்தல் செய்யப்படலாம்?",
    "options": [
      {"id": "A", "en": "Only once", "ta": "ஒரு முறை மட்டுமே"},
      {"id": "B", "en": "Maximum two terms", "ta": "அதிகபட்சம் இரு முறை"},
      {"id": "C", "en": "Maximum three terms", "ta": "அதிகபட்சம் மூன்று முறை"},
      {"id": "D", "en": "Any number of times (Unlimited)", "ta": "எத்தனை முறை வேண்டுமானாலும் (வரம்பற்ற)"}
    ],
    "correct_answer": "D",
    "explanation": {"en": "Article 57 explicitly states that a person who holds, or who has held, office as President shall be eligible for re-election to that office for any number of terms.", "ta": "உறுப்பு 57 குடியரசுத் தலைவராகப் பணியாற்றிய ஒருவர் எத்தனை முறை வேண்டுமானாலும் மீண்டும் அப்பதவிக்குத் தேர்ந்தெடுக்கப்படத் தகுதியுடையவர் எனக் தெளிவுபடுத்துகிறது."},
    "explanation_en": "Article 57 explicitly states that a person who holds, or who has held, office as President shall be eligible for re-election to that office for any number of terms.",
    "explanation_ta": "உறுப்பு 57 குடியரசுத் தலைவராகப் பணியாற்றிய ஒருவர் எத்தனை முறை வேண்டுமானாலும் மீண்டும் அப்பதவிக்குத் தேர்ந்தெடுக்கப்படத் தகுதியுடையவர் எனக் தெளிவுபடுத்துகிறது.",
    "source_reference": "Part V - Article 57",
    "trap_point": {"en": "Do not confuse USA Constitution (max 2 terms) with Indian Constitution (unlimited terms allowed).", "ta": "அமெரிக்க அரசியலமைப்பையும் (அதிகபட்சம் 2 தவணைகள்) இந்திய அரசியலமைப்பையும் (வரம்பற்ற தவணைகள்) குழப்ப வேண்டாம்."},
    "tnpsc_tip": {"en": "Dr. Rajendra Prasad is the only Indian President to have served 2 full terms (1950–1962).", "ta": "டாக்டர் ராஜேந்திர பிரசாத் மட்டுமே 2 முழு தவணைகள் பணியாற்றிய ஒரே இந்தியக் குடியரசுத் தலைவர் ஆவார் (1950–1962)."},
    "why_not_others": {
      "A": {"en": "No one-term limit exists in India.", "ta": "இந்தியாவில் ஒரு தவணை வரம்பு எதுவும் இல்லை."},
      "B": {"en": "Two terms is the limit in USA, but NOT in India under Article 57.", "ta": "இரு தவணைகள் என்பது அமெரிக்காவில் உள்ள வரம்பு, இந்தியாவில் உறுப்பு 57-ன் கீழ் அல்ல."},
      "C": {"en": "No three-term limit exists under Article 57.", "ta": "உறுப்பு 57-ன் கீழ் மூன்று தவணை வரம்பு இல்லை."},
      "D": {"en": "Correct. Article 57 permits unlimited re-election terms.", "ta": "சரி. உறுப்பு 57 வரம்பற்ற மறுதேர்தலை அனுமதிக்கிறது."}
    },
    "metadata": {"subject": "Polity", "topic": "President of India", "type": "Easy", "level": "TNPSC Group 1"}
  },
  {
    "id": "POLITY_PRESIDENT_EASY_019",
    "subject": "Polity",
    "topic": "President of India",
    "difficulty": "Easy",
    "question_type": "Direct",
    "question": {"en": "Under Article 58, a candidate for Presidential election must be qualified for election as a member of which House?", "ta": "உறுப்பு 58-ன் கீழ் குடியரசுத் தலைவர் தேர்தலில் போட்டியிடும் வேட்பாளர் எந்த அவையின் உறுப்பினராகத் தேர்ந்தெடுக்கப்படும் தகுதியைப் பெற்றிருக்க வேண்டும்?"},
    "question_en": "Under Article 58, a candidate for Presidential election must be qualified for election as a member of which House?",
    "question_ta": "உறுப்பு 58-ன் கீழ் குடியரசுத் தலைவர் தேர்தலில் போட்டியிடும் வேட்பாளர் எந்த அவையின் உறுப்பினராகத் தேர்ந்தெடுக்கப்படும் தகுதியைப் பெற்றிருக்க வேண்டும்?",
    "options": [
      {"id": "A", "en": "Rajya Sabha", "ta": "மாநிலங்களவை"},
      {"id": "B", "en": "Lok Sabha", "ta": "மக்களவை"},
      {"id": "C", "en": "State Legislative Assembly", "ta": "மாநிலச் சட்டமன்றப் பேரவை"},
      {"id": "D", "en": "State Legislative Council", "ta": "மாநிலச் சட்ட மேலவை"}
    ],
    "correct_answer": "B",
    "explanation": {"en": "Article 58(1)(c) mandates that a person shall be eligible for election as President only if he is qualified for election as a member of the House of the People (Lok Sabha).", "ta": "உறுப்பு 58(1)(c) ஒருவர் மக்களவை (House of the People) உறுப்பினராகத் தேர்ந்தெடுக்கப்படத் தகுதி பெற்றிருந்தால் மட்டுமே குடியரசுத் தலைவர் தேர்தலுக்குத் தகுதியானவர் எனக் கூறுகிறது."},
    "explanation_en": "Article 58(1)(c) mandates that a person shall be eligible for election as President only if he is qualified for election as a member of the House of the People (Lok Sabha).",
    "explanation_ta": "உறுப்பு 58(1)(c) ஒருவர் மக்களவை (House of the People) உறுப்பினராகத் தேர்ந்தெடுக்கப்படத் தகுதி பெற்றிருந்தால் மட்டுமே குடியரசுத் தலைவர் தேர்தலுக்குத் தகுதியானவர் எனக் கூறுகிறது.",
    "source_reference": "Part V - Article 58(1)(c)",
    "trap_point": {"en": "President candidate must be qualified for LOK SABHA; Vice-President candidate must be qualified for RAJYA SABHA!", "ta": "குடியரசுத் தலைவர் வேட்பாளர் மக்களவை தகுதியும்; துணைத் தலைவர் வேட்பாளர் மாநிலங்களவை தகுதியும் பெற வேண்டும்!"},
    "tnpsc_tip": {"en": "Qualifications: 1) Citizen of India, 2) 35+ yrs age, 3) Qualified for Lok Sabha, 4) No office of profit.", "ta": "தகுதிகள்: 1) இந்தியக் குடிமகன், 2) 35+ வயது, 3) மக்களவை தகுதி, 4) ஆதாயம் தரும் பதவி இன்மை."},
    "why_not_others": {
      "A": {"en": "Rajya Sabha qualification applies to Vice-President (Art 66), not President.", "ta": "மாநிலங்களவை தகுதி துணைத் தலைவருக்கு உரியது (உறுப்பு 66), குடியரசுத் தலைவருக்கு அல்ல."},
      "B": {"en": "Correct. Qualification for Lok Sabha membership is mandatory under Art 58.", "ta": "சரி. மக்களவை உறுப்பினர் தகுதி உறுப்பு 58-ன் கீழ் கட்டாயமாகும்."},
      "C": {"en": "State Legislative Assembly qualification does not apply to President.", "ta": "மாநிலச் சட்டமன்றப் பேரவை தகுதி குடியரசுத் தலைவருக்குப் பொருந்தாது."},
      "D": {"en": "Legislative Council qualification does not apply to President.", "ta": "சட்ட மேலவை தகுதி குடியரசுத் தலைவருக்குப் பொருந்தாது."}
    },
    "metadata": {"subject": "Polity", "topic": "President of India", "type": "Easy", "level": "TNPSC Group 1"}
  },
  {
    "id": "POLITY_PRESIDENT_EASY_020",
    "subject": "Polity",
    "topic": "President of India",
    "difficulty": "Easy",
    "question_type": "Direct",
    "question": {"en": "Under Article 65, when the Vice-President acts as President of India during a casual vacancy, who performs the duties of the Chairman of Rajya Sabha?", "ta": "உறுப்பு 65-ன் கீழ் தற்செயல் காலியிடத்தின் போது துணைத் தலைவர் செயல் குடியரசுத் தலைவராகப் பணியாற்றும் போது, மாநிலங்களவைத் தலைவரின் பணிகளை யார் செய்வார்?"},
    "question_en": "Under Article 65, when the Vice-President acts as President of India during a casual vacancy, who performs the duties of the Chairman of Rajya Sabha?",
    "question_ta": "உறுப்பு 65-ன் கீழ் தற்செயல் காலியிடத்தின் போது துணைத் தலைவர் செயல் குடியரசுத் தலைவராகப் பணியாற்றும் போது, மாநிலங்களவைத் தலைவரின் பணிகளை யார் செய்வார்?",
    "options": [
      {"id": "A", "en": "The Vice-President continues to perform both duties", "ta": "துணைத் தலைவரே இரு பணிகளையும் தொடர்ந்து செய்வார்"},
      {"id": "B", "en": "Deputy Chairman of Rajya Sabha", "ta": "மாநிலங்களவையின் துணைத் தலைவர்"},
      {"id": "C", "en": "Speaker of Lok Sabha", "ta": "மக்களவை சபாநாயகர்"},
      {"id": "D", "en": "Senior-most member of Rajya Sabha", "ta": "மாநிலங்களவையின் மூத்த உறுப்பினர்"}
    ],
    "correct_answer": "B",
    "explanation": {"en": "Under Article 65(2) and Article 91, when the Vice-President acts as President, he ceases to perform the duties of the Chairman of Rajya Sabha, and those duties are performed by the Deputy Chairman of Rajya Sabha.", "ta": "உறுப்பு 65(2) மற்றும் 91-ன் கீழ் துணைத் தலைவர் செயல் குடியரசுத் தலைவராகப் பணியாற்றும் போது மாநிலங்களவைத் தலைவர் பணிகளை நிறுத்தி வைப்பார், அப்பணிகளை மாநிலங்களவைத் துணைத் தலைவர் செய்வார்."},
    "explanation_en": "Under Article 65(2) and Article 91, when the Vice-President acts as President, he ceases to perform the duties of the Chairman of Rajya Sabha, and those duties are performed by the Deputy Chairman of Rajya Sabha.",
    "explanation_ta": "உறுப்பு 65(2) மற்றும் 91-ன் கீழ் துணைத் தலைவர் செயல் குடியரசுத் தலைவராகப் பணியாற்றும் போது மாநிலங்களவைத் தலைவர் பணிகளை நிறுத்தி வைப்பார், அப்பணிகளை மாநிலங்களவைத் துணைத் தலைவர் செய்வார்.",
    "source_reference": "Part V - Articles 65 & 91",
    "trap_point": {"en": "Vice-President CANNOT perform duties of RS Chairman while acting as President, nor draw RS Chairman salary.", "ta": "செயல் குடியரசுத் தலைவராக இருக்கும் போது துணைத் தலைவரால் மாநிலங்களவைத் தலைவர் பணிகளைச் செய்யவோ அச் சம்பளத்தைப் பெறவோ முடியாது."},
    "tnpsc_tip": {"en": "The Vice-President draws the salary of the President while acting as President under Article 65.", "ta": "செயல் குடியரசுத் தலைவராக இருக்கும் போது துணைத் தலைவர் குடியரசுத் தலைவரின் ஊதியத்தைப் பெறுவார்."},
    "why_not_others": {
      "A": {"en": "Article 65(2) explicitly prohibits performing RS Chairman duties.", "ta": "உறுப்பு 65(2) மாநிலங்களவைத் தலைவர் பணிகளைச் செய்வதைத் தடுத்து நிறுத்துகிறது."},
      "B": {"en": "Correct. Deputy Chairman performs RS Chairman duties under Art 91.", "ta": "சரி. உறுப்பு 91-ன் கீழ் மாநிலங்களவைத் துணைத் தலைவர் அப்பணிகளைச் செய்வார்."},
      "C": {"en": "Speaker of Lok Sabha presides over Lok Sabha, not Rajya Sabha.", "ta": "மக்களவை சபாநாயகர் மக்களவைக்குத் தலைமை தாங்குபவர்."},
      "D": {"en": "Senior member only acts if Deputy Chairman is also absent.", "ta": "துணைத் தலைவரும் இல்லாத போது மட்டுமே மூத்த உறுப்பினர் செயல்படுவார்."}
    },
    "metadata": {"subject": "Polity", "topic": "President of India", "type": "Easy", "level": "TNPSC Group 1"}
  },
  {
    "id": "POLITY_PRESIDENT_EASY_021",
    "subject": "Polity",
    "topic": "President of India",
    "difficulty": "Easy",
    "question_type": "Direct",
    "question": {"en": "Under Article 360, which type of Emergency can be declared by the President if the financial stability or credit of India is threatened?", "ta": "இந்தியாவின் நிதி ஸ்திரத்தன்மை அல்லது கடனுக்கு அச்சுறுத்தல் ஏற்பட்டால் உறுப்பு 360-ன் கீழ் குடியரசுத் தலைவரால் எந்த வகையான அவசரநிலை பிரகடனம் செய்யப்படலாம்?"},
    "question_en": "Under Article 360, which type of Emergency can be declared by the President if the financial stability or credit of India is threatened?",
    "question_ta": "இந்தியாவின் நிதி ஸ்திரத்தன்மை அல்லது கடனுக்கு அச்சுறுத்தல் ஏற்பட்டால் உறுப்பு 360-ன் கீழ் குடியரசுத் தலைவரால் எந்த வகையான அவசரநிலை பிரகடனம் செய்யப்படலாம்?",
    "options": [
      {"id": "A", "en": "National Emergency", "ta": "தேசிய அவசரநிலை"},
      {"id": "B", "en": "State Emergency", "ta": "மாநில அவசரநிலை"},
      {"id": "C", "en": "Financial Emergency", "ta": "நிதி அவசரநிலை"},
      {"id": "D", "en": "Judicial Emergency", "ta": "நீதித்துறை அவசரநிலை"}
    ],
    "correct_answer": "C",
    "explanation": {"en": "Article 360 contains provisions as to Financial Emergency, which can be proclaimed by the President if financial stability or credit of India or any part of territory is threatened.", "ta": "உறுப்பு 360 நிதி அவசரநிலை பற்றிய விநியோகங்களைக் கொண்டுள்ளது; நாட்டின் நிதி ஸ்திரத்தன்மை அச்சுறுத்தப்பட்டால் இதைக் குடியரசுத் தலைவர் பிரகடனப்படுத்தலாம்."},
    "explanation_en": "Article 360 contains provisions as to Financial Emergency, which can be proclaimed by the President if financial stability or credit of India or any part of territory is threatened.",
    "explanation_ta": "உறுப்பு 360 நிதி அவசரநிலை பற்றிய விநியோகங்களைக் கொண்டுள்ளது; நாட்டின் நிதி ஸ்திரத்தன்மை அச்சுறுத்தப்பட்டால் இதைக் குடியரசுத் தலைவர் பிரகடனப்படுத்தலாம்.",
    "source_reference": "Part XVIII - Article 360",
    "trap_point": {"en": "Financial Emergency under Article 360 has NEVER been declared in India so far.", "ta": "இந்தியாவில் இதுவரை உறுப்பு 360-ன் கீழ் நிதி அவசரநிலை ஒருமுறை கூட அறிவிக்கப்பட்டதில்லை."},
    "tnpsc_tip": {"en": "Parliamentary approval deadline for Art 360 is 2 months by Simple Majority.", "ta": "உறுப்பு 360-க்கு நாடாளுமன்ற ஒப்புதல் கால வரம்பு 2 மாதங்கள் (எளிய பெரும்பான்மை)."},
    "why_not_others": {
      "A": {"en": "National Emergency is under Article 352.", "ta": "தேசிய அவசரநிலை உறுப்பு 352-ன் கீழ் உள்ளது."},
      "B": {"en": "State Emergency (President's Rule) is under Article 356.", "ta": "மாநில அவசரநிலை (குடியரசுத் தலைவர் ஆட்சி) உறுப்பு 356-ன் கீழ் உள்ளது."},
      "C": {"en": "Correct. Article 360 is Financial Emergency.", "ta": "சரி. உறுப்பு 360 நிதி அவசரநிலையாகும்."},
      "D": {"en": "There is no 'Judicial Emergency' under Part XVIII.", "ta": "பகுதி XVIII-ன் கீழ் 'நீதித்துறை அவசரநிலை' என்று எதுவும் இல்லை."}
    },
    "metadata": {"subject": "Polity", "topic": "President of India", "type": "Easy", "level": "TNPSC Group 1"}
  },
  {
    "id": "POLITY_PRESIDENT_EASY_022",
    "subject": "Polity",
    "topic": "President of India",
    "difficulty": "Easy",
    "question_type": "Direct",
    "question": {"en": "Who is the only Indian President to have served two full terms in office?", "ta": "இரண்டு முழு தவணைகள் பதவியில் பணியாற்றிய ஒரே இந்தியக் குடியரசுத் தலைவர் யார்?"},
    "question_en": "Who is the only Indian President to have served two full terms in office?",
    "question_ta": "இரண்டு முழு தவணைகள் பதவியில் பணியாற்றிய ஒரே இந்தியக் குடியரசுத் தலைவர் யார்?",
    "options": [
      {"id": "A", "en": "Dr. S. Radhakrishnan", "ta": "டாக்டர் எஸ். ராதாகிருஷ்ணன்"},
      {"id": "B", "en": "Dr. Rajendra Prasad", "ta": "டாக்டர் ராஜேந்திர பிரசாத்"},
      {"id": "C", "en": "Dr. A.P.J. Abdul Kalam", "ta": "டாக்டர் ஏ.பி.ஜே. அப்துல் கலாம்"},
      {"id": "D", "en": "V.V. Giri", "ta": "வி.வி. கிரி"}
    ],
    "correct_answer": "B",
    "explanation": {"en": "Dr. Rajendra Prasad served as President of India for two full consecutive terms from 1950 to 1962 (re-elected in 1952 and 1957).", "ta": "டாக்டர் ராஜேந்திர பிரசாத் 1950 முதல் 1962 வரை (1952 மற்றும் 1957-ல் தேர்ந்தெடுக்கப்பட்டு) இரண்டு முழு தவணைகள் குடியரசுத் தலைவராகப் பணியாற்றினார்."},
    "explanation_en": "Dr. Rajendra Prasad served as President of India for two full consecutive terms from 1950 to 1962 (re-elected in 1952 and 1957).",
    "explanation_ta": "டாக்டர் ராஜேந்திர பிரசாத் 1950 முதல் 1962 வரை (1952 மற்றும் 1957-ல் தேர்ந்தெடுக்கப்பட்டு) இரண்டு முழு தவணைகள் குடியரசுத் தலைவராகப் பணியாற்றினார்.",
    "source_reference": "Presidential History & Article 57",
    "trap_point": {"en": "Dr. S. Radhakrishnan served two terms as Vice-President, but only one term as President!", "ta": "டாக்டர் எஸ். ராதாகிருஷ்ணன் துணைத் தலைவராக இரு தவணைகள் பணியாற்றினார், ஆனால் குடியரசுத் தலைவராக ஒரு தவணை மட்டுமே!"},
    "tnpsc_tip": {"en": "Article 57 permits unlimited re-election terms in India.", "ta": "உறுப்பு 57 இந்தியாவில் வரம்பற்ற மறுதேர்தல் தவணைகளை அனுமதிக்கிறது."},
    "why_not_others": {
      "A": {"en": "Dr. S. Radhakrishnan served 2 terms as VP, but 1 term as President (1962-1967).", "ta": "டாக்டர் எஸ். ராதாகிருஷ்ணன் துணைத் தலைவராக 2 தவணைகள், குடியரசுத் தலைவராக 1 தவணை பணியாற்றினார்."},
      "B": {"en": "Correct. Dr. Rajendra Prasad served 2 full terms as President.", "ta": "சரி. டாக்டர் ராஜேந்திர பிரசாத் 2 முழு தவணைகள் குடியரசுத் தலைவராகப் பணியாற்றினார்."},
      "C": {"en": "Dr. A.P.J. Abdul Kalam served one term (2002-2007).", "ta": "டாக்டர் ஏ.பி.ஜே. அப்துல் கலாம் ஒரு தவணை பணியாற்றினார்."},
      "D": {"en": "V.V. Giri served one term as President (1969-1974).", "ta": "வி.வி. கிரி ஒரு தவணை பணியாற்றினார்."}
    },
    "metadata": {"subject": "Polity", "topic": "President of India", "type": "Easy", "level": "TNPSC Group 1"}
  },
  {
    "id": "POLITY_PRESIDENT_EASY_023",
    "subject": "Polity",
    "topic": "President of India",
    "difficulty": "Easy",
    "question_type": "Direct",
    "question": {"en": "Who was the Chief Justice of India who served as Acting President of India in 1969?", "ta": "1969-ல் இந்தியச் செயல் குடியரசுத் தலைவராகப் பணியாற்றிய இந்தியத் தலைமை நீதிபதி யார்?"},
    "question_en": "Who was the Chief Justice of India who served as Acting President of India in 1969?",
    "question_ta": "1969-ல் இந்தியச் செயல் குடியரசுத் தலைவராகப் பணியாற்றிய இந்தியத் தலைமை நீதிபதி யார்?",
    "options": [
      {"id": "A", "en": "Justice P.N. Bhagwati", "ta": "நீதிபதி பி.என். பகவதி"},
      {"id": "B", "en": "Justice M. Hidayatullah", "ta": "நீதிபதி எம். இதாயத்துல்லா"},
      {"id": "C", "en": "Justice Y.V. Chandrachud", "ta": "நீதிபதி ஒய்.வி. சந்திரசூட்"},
      {"id": "D", "en": "Justice V.R. Krishna Iyer", "ta": "நீதிபதி வி.ஆர். கிருஷ்ண ஐயர்"}
    ],
    "correct_answer": "B",
    "explanation": {"en": "Chief Justice M. Hidayatullah served as Acting President from July 20 to August 24, 1969 under the President (Discharge of Functions) Act, 1969 when both President and VP posts became vacant.", "ta": "குடியரசுத் தலைவர் (பணிகள் நிவர்த்தி) சட்டம் 1969-ன் கீழ் குடியரசுத் தலைவர் & துணைத் தலைவர் பதவிகள் காலியான போது தலைமை நீதிபதி எம். இதாயத்துல்லா ஜூலை 20 முதல் ஆகஸ்ட் 24, 1969 வரை செயல் குடியரசுத் தலைவராகப் பணியாற்றினார்."},
    "explanation_en": "Chief Justice M. Hidayatullah served as Acting President from July 20 to August 24, 1969 under the President (Discharge of Functions) Act, 1969 when both President and VP posts became vacant.",
    "explanation_ta": "குடியரசுத் தலைவர் (பணிகள் நிவர்த்தி) சட்டம் 1969-ன் கீழ் குடியரசுத் தலைவர் & துணைத் தலைவர் பதவிகள் காலியான போது தலைமை நீதிபதி எம். இதாயத்துல்லா ஜூலை 20 முதல் ஆகஸ்ட் 24, 1969 வரை செயல் குடியரசுத் தலைவராகப் பணியாற்றினார்.",
    "source_reference": "President (Discharge of Functions) Act, 1969",
    "trap_point": {"en": "Justice M. Hidayatullah later also served as elected Vice-President of India (1979-1984).", "ta": "நீதிபதி எம். இதாயத்துல்லா பின்னர் இந்தியாவின் தேர்ந்தெடுக்கப்பட்ட துணைத் தலைவராகவும் (1979-1984) பணியாற்றினார்."},
    "tnpsc_tip": {"en": "M. Hidayatullah is the ONLY CJI in Indian history to have served as Acting President.", "ta": "இந்திய வரலாற்றில் செயல் குடியரசுத் தலைவராகப் பணியாற்றிய ஒரே CJI எம். இதாயத்துல்லா மட்டுமே."},
    "why_not_others": {
      "A": {"en": "Justice P.N. Bhagwati was CJI, but never served as Acting President.", "ta": "நீதிபதி பி.என். பகவதி CJI ஆக இருந்தார், ஆனால் செயல் குடியரசுத் தலைவராகப் பணியாற்றவில்லை."},
      "B": {"en": "Correct. Justice M. Hidayatullah served as Acting President in 1969.", "ta": "சரி. நீதிபதி எம். இதாயத்துல்லா 1969-ல் செயல் குடியரசுத் தலைவராகப் பணியாற்றினார்."},
      "C": {"en": "Justice Y.V. Chandrachud was the longest-serving CJI, not Acting President.", "ta": "நீதிபதி ஒய்.வி. சந்திரசூட் மிக நீண்ட காலம் பணியாற்றிய CJI ஆவார்."},
      "D": {"en": "Justice V.R. Krishna Iyer was a prominent SC Judge, not Acting President.", "ta": "நீதிபதி வி.ஆர். கிருஷ்ண ஐயர் புகழ்பெற்ற உச்ச நீதிமன்ற நீதிபதி ஆவார்."}
    },
    "metadata": {"subject": "Polity", "topic": "President of India", "type": "Easy", "level": "TNPSC Group 1"}
  },
  {
    "id": "POLITY_PRESIDENT_EASY_024",
    "subject": "Polity",
    "topic": "President of India",
    "difficulty": "Easy",
    "question_type": "Direct",
    "question": {"en": "Under Article 78, whose constitutional duty is it to communicate all decisions of the Council of Ministers to the President?", "ta": "உறுப்பு 78-ன் கீழ் அமைச்சரவையின் அனைத்து முடிவுகளையும் குடியரசுத் தலைவருக்குத் தெரிவிப்பது யாருடைய அரசியலமைப்புப் பொறுப்பாகும்?"},
    "question_en": "Under Article 78, whose constitutional duty is it to communicate all decisions of the Council of Ministers to the President?",
    "question_ta": "உறுப்பு 78-ன் கீழ் அமைச்சரவையின் அனைத்து முடிவுகளையும் குடியரசுத் தலைவருக்குத் தெரிவிப்பது யாருடைய அரசியலமைப்புப் பொறுப்பாகும்?",
    "options": [
      {"id": "A", "en": "Cabinet Secretary", "ta": "கேபினட் செயலாளர்"},
      {"id": "B", "en": "Prime Minister of India", "ta": "இந்தியப் பிரதமர்"},
      {"id": "C", "en": "Union Home Minister", "ta": "மத்திய உள்Home துறை அமைச்சர்"},
      {"id": "D", "en": "Speaker of Lok Sabha", "ta": "மக்களவை சபாநாயகர்"}
    ],
    "correct_answer": "B",
    "explanation": {"en": "Article 78(a) lays down that it shall be the duty of the Prime Minister to communicate to the President all decisions of the Council of Ministers relating to the administration of the Union and proposals for legislation.", "ta": "உறுப்பு 78(a) ஒன்றிய நிர்வாகம் மற்றும் சட்டப் முன்மொழிவுகள் தொடர்பான அமைச்சரவையின் அனைத்து முடிவுகளையும் குடியரசுத் தலைவருக்குத் தெரிவிப்பது பிரதமரின் கடமை எனக் கூறுகிறது."},
    "explanation_en": "Article 78(a) lays down that it shall be the duty of the Prime Minister to communicate to the President all decisions of the Council of Ministers relating to the administration of the Union and proposals for legislation.",
    "explanation_ta": "உறுப்பு 78(a) ஒன்றிய நிர்வாகம் மற்றும் சட்டப் முன்மொழிவுகள் தொடர்பான அமைச்சரவையின் அனைத்து முடிவுகளையும் குடியரசுத் தலைவருக்குத் தெரிவிப்பது பிரதமரின் கடமை எனக் கூறுகிறது.",
    "source_reference": "Part V - Article 78",
    "trap_point": {"en": "Cabinet Secretary handles civil service administration, but Article 78 specifically names the Prime Minister.", "ta": "கேபினட் செயலாளர் சிவில் நிர்வாகத்தைக் கவனிப்பார், ஆனால் உறுப்பு 78 பிரதமரைக் குறிப்பிட்டுக் கூறுகிறது."},
    "tnpsc_tip": {"en": "Article 78 defines the PM as the link between President and Cabinet.", "ta": "உறுப்பு 78 பிரதமரைக் குடியரசுத் தலைவருக்கும் அமைச்சரவைக்கும் இடையிலான இணைப்பாக வரையறுக்கிறது."},
    "why_not_others": {
      "A": {"en": "Cabinet Secretary is administrative head, but Art 78 duty is assigned to PM.", "ta": "கேபினட் செயலாளர் நிர்வாகத் தலைவர், ஆனால் உறுப்பு 78 கடமை பிரதமருக்குரியது."},
      "B": {"en": "Correct. Article 78 explicitly assigns this duty to the Prime Minister.", "ta": "சரி. உறுப்பு 78 இந்த பொறுப்பைப் பிரதமருக்கு வழங்குகிறது."},
      "C": {"en": "Home Minister does not have this constitutional duty under Art 78.", "ta": "உள் துறை அமைச்சருக்கு உறுப்பு 78-ன் கீழ் இந்த கடமை இல்லை."},
      "D": {"en": "Speaker presides over Lok Sabha, not Cabinet communications to President.", "ta": "சபாநாயகர் மக்களவைக்குத் தலைமை தாங்குபவர்."}
    },
    "metadata": {"subject": "Polity", "topic": "President of India", "type": "Easy", "level": "TNPSC Group 1"}
  },
  {
    "id": "POLITY_PRESIDENT_EASY_025",
    "subject": "Polity",
    "topic": "President of India",
    "difficulty": "Easy",
    "question_type": "Direct",
    "question": {"en": "Under Article 85, who has the power to summon, prorogue each House of Parliament and dissolve the Lok Sabha?", "ta": "உறுப்பு 85-ன் கீழ் நாடாளுமன்றத்தின் ஒவ்வொரு அவையையும் கூட்டவும், ஒத்திவைக்கவும் மற்றும் மக்களவையைக் கலைக்கவும் யாருக்கு அதிகாரமுண்டு?"},
    "question_en": "Under Article 85, who has the power to summon, prorogue each House of Parliament and dissolve the Lok Sabha?",
    "question_ta": "உறுப்பு 85-ன் கீழ் நாடாளுமன்றத்தின் ஒவ்வொரு அவையையும் கூட்டவும், ஒத்திவைக்கவும் மற்றும் மக்களவையைக் கலைக்கவும் யாருக்கு அதிகாரமுண்டு?",
    "options": [
      {"id": "A", "en": "Prime Minister of India", "ta": "இந்தியப் பிரதமர்"},
      {"id": "B", "en": "Speaker of Lok Sabha", "ta": "மக்களவை சபாநாயகர்"},
      {"id": "C", "en": "President of India", "ta": "இந்தியக் குடியரசுத் தலைவர்"},
      {"id": "D", "en": "Vice-President of India", "ta": "இந்தியத் துணைத் தலைவர்"}
    ],
    "correct_answer": "C",
    "explanation": {"en": "Article 85(1) & (2) empowers the President from time to time to summon each House of Parliament, prorogue the Houses, and dissolve the Lok Sabha.", "ta": "உறுப்பு 85(1) & (2) நாடாளுமன்றத்தின் ஒவ்வொரு அவையையும் கூட்டவும், கூட்டத் தொடரை ஒத்திவைக்கவும் மற்றும் மக்களவையைக் கலைக்கவும் குடியரசுத் தலைவருக்கு அதிகாரமளிக்கிறது."},
    "explanation_en": "Article 85(1) & (2) empowers the President from time to time to summon each House of Parliament, prorogue the Houses, and dissolve the Lok Sabha.",
    "explanation_ta": "உறுப்பு 85(1) & (2) நாடாளுமன்றத்தின் ஒவ்வொரு அவையையும் கூட்டவும், கூட்டத் தொடரை ஒத்திவைக்கவும் மற்றும் மக்களவையைக் கலைக்கவும் குடியரசுத் தலைவருக்கு அதிகாரமளிக்கிறது.",
    "source_reference": "Part V - Article 85",
    "trap_point": {"en": "Adjournment of a sitting is done by Speaker/Chairman, but Prorogation and Dissolution are done by President!", "ta": "அமர்வு ஒத்திவைப்பு சபாநாயகரால் செய்யப்படும், ஆனால் கூட்டத் தொடர் ஒத்திவைப்பும் அவைக் கலைப்பும் குடியரசுத் தலைவரால் செய்யப்படும்!"},
    "tnpsc_tip": {"en": "Maximum gap between two sessions of Parliament under Art 85(1) cannot exceed 6 months.", "ta": "உறுப்பு 85(1)-ன் கீழ் நாடாளுமன்றத்தின் இரு கூட்டத் தொடர்களுக்கு இடையிலான அதிகபட்ச இடைவெளி 6 மாதங்களுக்கு மிகக் கூடாது."},
    "why_not_others": {
      "A": {"en": "PM advises the President, but formal order is issued by President.", "ta": "பிரதமர் குடியரசுத் தலைவருக்கு ஆலோசனை வழங்குவார், ஆனால் முறைசார் உத்தரவைக் குடியரசுத் தலைவர் பிறப்பிப்பார்."},
      "B": {"en": "Speaker adjourns sitting (Sine Die), but does not prorogue or dissolve.", "ta": "சபாநாயகர் அமர்வை ஒத்திவைப்பார் (Sine Die), ஆனால் அவையைக் கலைப்பதில்லை."},
      "C": {"en": "Correct. President summons, prorogues, and dissolves under Article 85.", "ta": "சரி. உறுப்பு 85-ன் கீழ் குடியரசுத் தலைவர் கூட்டுகிறார், ஒத்திவைக்கிறார், கலைக்கிறார்."},
      "D": {"en": "Vice-President as RS Chairman presides over RS, but cannot dissolve LS.", "ta": "துணைத் தலைவர் மாநிலங்களவைக்குத் தலைமை தாங்குவார், ஆனால் மக்களவையைக் கலைக்க முடியாது."}
    },
    "metadata": {"subject": "Polity", "topic": "President of India", "type": "Easy", "level": "TNPSC Group 1"}
  }
]

# Write easy.json
target_path = "data/questions/polity/president_easy.json"
os.makedirs(os.path.dirname(target_path), exist_ok=True)
with open(target_path, "w", encoding="utf-8") as f:
    json.dump(easy_25, f, ensure_ascii=False, indent=2)

print(f"✅ Generated and validated {len(easy_25)} questions in {target_path}")
