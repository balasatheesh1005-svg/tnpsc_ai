# -*- coding: utf-8 -*-
"""
Master Builder for Fundamental Rights – Medium 50 MCQs (Bilingual)
Subject: Indian Polity
Topic: Fundamental Rights
Type: Medium
Target Output: data/questions/polity/fundamental_rights_medium.json
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

questions = [
  # 1. Conceptual Distinction: Art 12 vs Art 13 - Ans: B
  {
    "id": "FR_M_001",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Medium",
    "question_type": "Conceptual Distinction",
    "question": {
      "en": "How do Article 12 and Article 13 differ in their primary functional role within Part III of the Constitution?",
      "ta": "அரசியலமைப்பின் பகுதி III-ல் உறுப்பு 12 மற்றும் உறுப்பு 13 ஆகியவை தங்களின் முதன்மைச் செயல்பாட்டுப் பங்கில் எவ்வாறு வேறுபடுகின்றன?"
    },
    "options": [
      { "id": "A", "en": "Article 12 guarantees individual remedies, while Article 13 defines the territory of India.", "ta": "உறுப்பு 12 தனிநபர் தீர்வுகளை உத்தரவாதம் செய்கிறது, உறுப்பு 13 இந்திய நிலப்பரப்பை வரையறுக்கிறது." },
      { "id": "B", "en": "Article 12 defines the entities against which rights are enforced ('State'), while Article 13 invalidates laws that infringe upon those rights ('Judicial Review').", "ta": "உறுப்பு 12 உரிமைகள் எவருக்கு எதிராக நிலைநாட்டப்படுகின்றன என்பதைத் ('அரசு') வரையறுக்கிறது, உறுப்பு 13 அவ்வுரிமைகளை மீறும் சட்டங்களைச் செல்லாததாக்குகிறது ('நீதித்துறை ஆய்வு')." },
      { "id": "C", "en": "Article 12 applies only during Emergency, while Article 13 applies only during normal times.", "ta": "உறுப்பு 12 அவசரநிலையின் போது மட்டுமே பொருந்தும், உறுப்பு 13 சாதாரண காலத்தில் மட்டுமே பொருந்தும்." },
      { "id": "D", "en": "Article 12 covers Parliament only, while Article 13 covers State Legislatures only.", "ta": "உறுப்பு 12 நாடாளுமன்றத்தை மட்டுமே உள்ளடக்குகிறது, உறுப்பு 13 மாநில சட்டமன்றங்களை மட்டுமே உள்ளடக்குகிறது." }
    ],
    "correct_answer": "B",
    "explanation": {
      "en": "Article 12 sets the boundary of state authority against which Part III operates. Article 13 provides the testing mechanism (Judicial Review) to strike down laws violating those rights.",
      "ta": "உறுப்பு 12 பகுதி III யாருக்கு எதிராகச் செயல்படுகிறது என்பதற்கான அரசு அதிகார எல்லையை நிர்ணயிக்கிறது. உறுப்பு 13 அவ்வுரிமைகளை மீறும் சட்டங்களை ரத்து செய்யும் நீதித்துறை ஆய்வு அமைப்பை வழங்குகிறது."
    },
    "why_not_others": {
      "A": { "en": "Article 32 guarantees remedies, not Article 12.", "ta": "உறுப்பு 32 தீர்வுகளை உத்தரவாதம் செய்கிறது, உறுப்பு 12 அல்ல." },
      "B": { "en": "Correct. Art 12 defines 'State'; Art 13 mandates 'Judicial Review'.", "ta": "சரி. உறுப்பு 12 'அரசை' வரையறுக்கிறது; உறுப்பு 13 'நீதித்துறை ஆய்வை' விதிக்கிறது." },
      "C": { "en": "Both Articles apply during normal times.", "ta": "இரண்டு உறுப்புகளுமே சாதாரண காலத்தில் பொருந்தும்." },
      "D": { "en": "Both Articles cover Union and State authorities.", "ta": "இரண்டு உறுப்புகளுமே மத்திய மற்றும் மாநில அதிகார அமைப்புகளை உள்ளடக்குகின்றன." }
    },
    "tnpsc_tip": {
      "en": "Art 12 defines WHO must respect FRs; Art 13 defines WHAT LAWS violate FRs.",
      "ta": "உறுப்பு 12 அடிப்படை உரிமைகளை யார் மதிக்க வேண்டும் என்பதை வரையறுக்கிறது; உறுப்பு 13 எந்தச் சட்டங்கள் உரிமைகளை மீறுகின்றன என்பதை வரையறுக்கிறது."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Medium", "level": "TNPSC Group 1" }
  },

  # 2. Conceptual Distinction: Equality before Law vs Equal Protection of Laws - Ans: C
  {
    "id": "FR_M_002",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Medium",
    "question_type": "Conceptual Distinction",
    "question": {
      "en": "Which statement accurately highlights the conceptual difference between 'Equality before Law' and 'Equal Protection of Laws' under Article 14?",
      "ta": "உறுப்பு 14-ன் கீழ் 'சட்டத்தின் முன் சமத்துவம்' மற்றும் 'சட்டங்களின் சமமான பாதுகாப்பு' ஆகியவற்றிற்கு இடையேயான கருத்தியல் வேறுபாட்டைத் துல்லியமாகச் சுட்டிக்காட்டும் கூற்று எது?"
    },
    "options": [
      { "id": "A", "en": "'Equality before Law' is a positive concept requiring state intervention; 'Equal Protection' is a negative concept restricting state action.", "ta": "'சட்டத்தின் முன் சமத்துவம்' என்பது அரசின் தலையீட்டைக் கோரும் நேர்மறைக் கருத்து; 'சமமான பாதுகாப்பு' என்பது அரசின் நடவடிக்கையைக் கட்டுப்படுத்தும் எதிர்மறைக் கருத்து." },
      { "id": "B", "en": "Both concepts prohibit any form of classification among citizens under any circumstances.", "ta": "இரண்டு கருத்துக்களுமே எந்தச் சூழ்நிலையிலும் குடிமக்களிடையே எந்தவொரு வகைப்பாட்டையும் தடை செய்கின்றன." },
      { "id": "C", "en": "'Equality before Law' means absence of special privileges (negative concept), whereas 'Equal Protection of Laws' permits equal treatment among equals in equal circumstances (positive concept).", "ta": "'சட்டத்தின் முன் சமத்துவம்' என்பது சிறப்புச் சலுகைகள் இல்லாததைக் குறிக்கிறது (எதிர்மறைக் கருத்து), அதேவேளையில் 'சட்டங்களின் சமமான பாதுகாப்பு' என்பது சமமான சூழ்நிலைகளில் சமமானவர்களிடையே சமமான சிகிச்சையை அனுமதிக்கிறது (நேர்மறைக் கருத்து)." },
      { "id": "D", "en": "'Equality before Law' applies to citizens only, while 'Equal Protection of Laws' applies to foreigners only.", "ta": "'சட்டத்தின் முன் சமத்துவம்' குடிமக்களுக்கு மட்டுமே பொருந்தும், அதேவேளையில் 'சட்டங்களின் சமமான பாதுகாப்பு' வெளிநாட்டினருக்கு மட்டுமே பொருந்தும்." }
    ],
    "correct_answer": "C",
    "explanation": {
      "en": "'Equality before Law' (British) declares no man is above law. 'Equal Protection of Laws' (American) permits reasonable classification so that equals are treated equally ('like should be treated alike').",
      "ta": "'சட்டத்தின் முன் சமத்துவம்' (பிரிட்டிஷ்) எந்த மனிதனும் சட்டத்திற்கு மேற்பட்டவன் அல்ல என்கிறது. 'சட்டங்களின் சமமான பாதுகாப்பு' (அமெரிக்கா) நியாயமான வகைப்பாட்டை அனுமதித்து சமமானவர்கள் சமமாக நடத்தப்பட வேண்டும் என்கிறது."
    },
    "why_not_others": {
      "A": { "en": "Reversed. Equality before Law is negative; Equal Protection is positive.", "ta": "தலைகீழானது. சட்டத்தின் முன் சமத்துவம் எதிர்மறை; சமமான பாதுகாப்பு நேர்மறை." },
      "B": { "en": "Equal Protection expressly allows reasonable classification.", "ta": "சமமான பாதுகாப்பு நியாயமான வகைப்பாட்டை வெளிப்படையாக அனுமதிக்கிறது." },
      "C": { "en": "Correct. Negative British concept vs Positive American concept.", "ta": "சரி. எதிர்மறை பிரிட்டிஷ் கருத்து vs நேர்மறை அமெரிக்க கருத்து." },
      "D": { "en": "Both concepts apply equally to all persons (citizens and foreigners).", "ta": "இரண்டு கருத்துக்களுமே அனைத்து நபர்களுக்கும் பொருந்தும்." }
    },
    "tnpsc_tip": {
      "en": "Article 14 forbids class legislation, but permits reasonable classification of persons.",
      "ta": "உறுப்பு 14 வகுப்புச் சட்டத்தைத் தடை செய்கிறது, ஆனால் நபர்களின் நியாயமான வகைப்பாட்டை அனுமதிக்கிறது."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Medium", "level": "TNPSC Group 1" }
  },

  # 3. Article / Provision Based: Reasonable Classification Test - Ans: A
  {
    "id": "FR_M_003",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Medium",
    "question_type": "Article/Provision Based",
    "question": {
      "en": "To satisfy the test of 'Reasonable Classification' under Article 14, what two conditions must be cumulatively fulfilled by a legislative classification?",
      "ta": "உறுப்பு 14-ன் கீழ் 'நியாயமான வகைப்பாடு' சோதனையை பூர்த்தி செய்ய, ஒரு சட்டமன்ற வகைப்பாடு எந்த இரண்டு நிபந்தனைகளையும் ஒன்றாகப் பூர்த்தி செய்ய வேண்டும்?"
    },
    "options": [
      { "id": "A", "en": "1. Intelligible Differentia, and 2. Rational Nexus between the differentia and the object sought to be achieved.", "ta": "1. புரிந்துகொள்ளக்கூடிய வேறுபாடு (Intelligible Differentia), மற்றும் 2. அவ்வேறுபாட்டிற்கும் அடைவதற்குக் கோரப்படும் இலக்கிற்கும் இடையே பகுத்தறிவுத் தொடர்பு (Rational Nexus)." },
      { "id": "B", "en": "1. Judicial approval prior to enactment, and 2. Unanimous Parliamentary vote.", "ta": "1. இயற்றுவதற்கு முன் நீதித்துறை ஒப்புதல், மற்றும் 2. ஏகமனதான நாடாளுமன்ற வாக்கு." },
      { "id": "C", "en": "1. Application to citizens only, and 2. Exemption of all tax laws.", "ta": "1. குடிமக்களுக்கு மட்டுமே பொருந்தும் தன்மை, மற்றும் 2. அனைத்து வரிச் சட்டங்களுக்கும் விலக்கு." },
      { "id": "D", "en": "1. Inclusion in the Ninth Schedule, and 2. Executive discretion.", "ta": "1. ஒன்பதாவது அட்டவணையில் சேர்ப்பு, மற்றும் 2. நிர்வாக விருப்ப உரிமை." }
    ],
    "correct_answer": "A",
    "explanation": {
      "en": "Under Article 14, reasonable classification requires: 1. Intelligible Differentia (clear distinction separating classified group from others), and 2. Rational Nexus (nexus between the distinction and the statute's objective).",
      "ta": "உறுப்பு 14-ன் கீழ் நியாயமான வகைப்பாட்டிற்கு: 1. புரிந்துகொள்ளக்கூடிய வேறுபாடு, மற்றும் 2. அவ்வேறுபாட்டிற்கும் சட்டத்தின் நோக்கத்திற்கும் இடையே பகுத்தறிவுத் தொடர்பு ஆகிய இரண்டும் தேவை."
    },
    "why_not_others": {
      "A": { "en": "Correct. Intelligible Differentia + Rational Nexus is the twin test of Art 14.", "ta": "சரி. புரிந்துகொள்ளக்கூடிய வேறுபாடு + பகுத்தறிவுத் தொடர்பு ஆகியவையே உறுப்பு 14-ன் இரட்டைச் சோதனையாகும்." },
      "B": { "en": "Judicial prior approval is not required.", "ta": "நீதிமன்ற முன் ஒப்புதல் தேவையில்லை." },
      "C": { "en": "Article 14 applies to all persons.", "ta": "உறுப்பு 14 அனைத்து நபர்களுக்கும் பொருந்தும்." },
      "D": { "en": "Ninth Schedule inclusion is not a test for Article 14 classification.", "ta": "9வது அட்டவணை சேர்ப்பு உறுப்பு 14 வகைப்பாட்டிற்கான சோதனை அல்ல." }
    },
    "tnpsc_tip": {
      "en": "Reasonable Classification under Art 14 = Intelligible Differentia + Rational Nexus.",
      "ta": "உறுப்பு 14-ன் நியாயமான வகைப்பாடு = புரிந்துகொள்ளக்கூடிய வேறுபாடு + பகுத்தறிவுத் தொடர்பு."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Medium", "level": "TNPSC Group 1" }
  },

  # 4. Conceptual Distinction: Article 15 vs Article 16 Scope - Ans: D
  {
    "id": "FR_M_004",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Medium",
    "question_type": "Conceptual Distinction",
    "question": {
      "en": "What is the core distinction regarding scope and field of application between Article 15 and Article 16 of the Constitution?",
      "ta": "அரசியலமைப்பின் உறுப்பு 15 மற்றும் உறுப்பு 16 ஆகியவற்றிற்கு இடையே எல்லை மற்றும் பயன்பாட்டுத் துறை தொடர்பான முதன்மை வேறுபாடு என்ன?"
    },
    "options": [
      { "id": "A", "en": "Article 15 applies to employment, whereas Article 16 applies to educational institutions.", "ta": "உறுப்பு 15 வேலைவாய்ப்பிற்குப் பொருந்தும், அதேவேளையில் உறுப்பு 16 கல்வி நிறுவனங்களுக்குப் பொருந்தும்." },
      { "id": "B", "en": "Article 15 covers foreigners, whereas Article 16 covers citizens only.", "ta": "உறுப்பு 15 வெளிநாட்டினரை உள்ளடக்குகிறது, அதேவேளையில் உறுப்பு 16 குடிமக்களை மட்டுமே உள்ளடக்குகிறது." },
      { "id": "C", "en": "Article 15 is non-justiciable, whereas Article 16 is justiciable in High Courts.", "ta": "உறுப்பு 15 நிலைநிறுத்த முடியாதது, அதேவேளையில் உறுப்பு 16 உயர் நீதிமன்றத்தில் நிலைநிறுத்தக்கூடியது." },
      { "id": "D", "en": "Article 15 is a general prohibition of discrimination in general social spheres and educational admission, whereas Article 16 is a specific guarantee limited to public employment under the State.", "ta": "உறுப்பு 15 பொதுச் சமூகக் கோளங்கள் மற்றும் கல்விச் சேர்க்கையில் பாகுபாட்டைத் தடுக்கும் பொதுவான விதியாகும், அதேவேளையில் உறுப்பு 16 என்பது அரசின் கீழ் உள்ள பொது வேலைவாய்ப்பிற்கு மட்டுமே கட்டுப்படுத்தப்பட்ட குறிப்பிட்ட உத்தரவாதமாகும்." }
    ],
    "correct_answer": "D",
    "explanation": {
      "en": "Article 15 prohibits discrimination broadly in public places, educational institutions, etc. Article 16 is a specific facet of equality restricted to employment or appointment to any office under the State.",
      "ta": "உறுப்பு 15 பொது இடங்கள், கல்வி நிறுவனங்களில் பரந்த அளவில் பாகுபாட்டைத் தடுக்கிறது. உறுப்பு 16 என்பது அரசின் கீழ் உள்ள வேலைவாய்ப்பு அல்லது பதவி நியமனத்திற்கு மட்டுமே கட்டுப்படுத்தப்பட்ட சமத்துவத்தின் குறிப்பிட்ட அம்சமாகும்."
    },
    "why_not_others": {
      "A": { "en": "Reversed. Art 15 covers educational admissions; Art 16 covers public employment.", "ta": "தலைகீழானது. உறுப்பு 15 கல்விச் சேர்க்கை; உறுப்பு 16 பொது வேலைவாய்ப்பு." },
      "B": { "en": "Both Articles 15 and 16 apply ONLY to Citizens.", "ta": "உறுப்புகள் 15 மற்றும் 16 இரண்டுமே குடிமக்களுக்கு மட்டுமே பொருந்தும்." },
      "C": { "en": "Both Articles are justiciable Fundamental Rights.", "ta": "இரண்டு உறுப்புகளுமே நிலைநிறுத்தக்கூடிய அடிப்படை உரிமைகள்." },
      "D": { "en": "Correct. Art 15 = General non-discrimination; Art 16 = Specific public employment non-discrimination.", "ta": "சரி. உறுப்பு 15 = பொதுப் பாகுபாடின்மை; உறுப்பு 16 = பொது வேலைவாய்ப்பு பாகுபாடின்மை." }
    },
    "tnpsc_tip": {
      "en": "Article 16 is an extension and specific application of the general principle in Article 15.",
      "ta": "உறுப்பு 16 என்பது உறுப்பு 15-ன் பொதுக் கோட்பாட்டின் நீட்சியும் குறிப்பிட்ட பயன்பாடும் ஆகும்."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Medium", "level": "TNPSC Group 1" }
  },

  # 5. Article / Provision Based: Article 16(4A) & 16(4B) Reservation Clauses - Ans: B
  {
    "id": "FR_M_005",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Medium",
    "question_type": "Article/Provision Based",
    "question": {
      "en": "Article 16(4B) was inserted by the 81st Constitutional Amendment Act, 2000 to overcome the 50% reservation ceiling limit for which specific purpose?",
      "ta": "81வது அரசியலமைப்பு திருத்தச் சட்டம் 2000 மூலம் உறுப்பு 16(4B) எந்த குறிப்பிட்ட நோக்கத்திற்காக 50% இடஒதுக்கீடு உச்சவரம்பு வரம்பை முறியடிக்கச் சேர்க்கப்பட்டது?"
    },
    "options": [
      { "id": "A", "en": "Reservation in private sector employment", "ta": "தனியார் துறை வேலைவாய்ப்பில் இடஒதுக்கீடு" },
      { "id": "B", "en": "Filling up unfilled reserved vacancies of a year ('backlog vacancies') in subsequent years as a separate class of vacancies.", "ta": "ஒரு ஆண்டின் நிரப்பப்படாத இடஒதுக்கீட்டுக் காலிப்பணியிடங்களை ('பின்தங்கிய காலிப்பணியிடங்கள்' - Backlog vacancies) அடுத்தடுத்த ஆண்டுகளில் தனிப் பிரிவாக நிரப்புதல்." },
      { "id": "C", "en": "Granting reservation to Economically Weaker Sections", "ta": "பொருளாதாரத்தில் நலிவடைந்த பிரிவினருக்கு இடஒதுக்கீடு வழங்குதல்" },
      { "id": "D", "en": "Granting 33% reservation for women in Parliament", "ta": "நாடாளுமன்றத்தில் பெண்களுக்கு 33% இடஒதுக்கீடு வழங்குதல்" }
    ],
    "correct_answer": "B",
    "explanation": {
      "en": "Article 16(4B) permits the State to treat unfilled reserved vacancies of a year ('backlog vacancies') as a separate class of vacancies to be filled in any succeeding year, without counting them against the 50% ceiling for that year.",
      "ta": "உறுப்பு 16(4B) நிரப்பப்படாத பின்தங்கிய காலிப்பணியிடங்களை (Backlog vacancies) அடுத்தடுத்த ஆண்டுகளில் நிரப்பப்படும் தனிப் பிரிவாகக் கருதி, அ ஆண்டின் 50% உச்சவரம்பில் அவற்றைக் கணக்கிடாமல் இருக்க அரசுக்கு அனுமதியளிக்கிறது."
    },
    "why_not_others": {
      "A": { "en": "Private sector reservation is not in Art 16(4B).", "ta": "தனியார் துறை இடஒதுக்கீடு உறுப்பு 16(4B)-ல் இல்லை." },
      "B": { "en": "Correct. Art 16(4B) protects carrying forward backlog vacancies without 50% cap limit.", "ta": "சரி. உறுப்பு 16(4B) 50% வரம்பின்றி பின்தங்கிய காலிப்பணியிடங்களை நிரப்ப பாதுகாக்கிறது." },
      "C": { "en": "EWS reservation is under Art 16(6).", "ta": "EWS இடஒதுக்கீடு உறுப்பு 16(6)-ன் கீழ் உள்ளது." },
      "D": { "en": "Women's parliamentary quota is not in Art 16(4B).", "ta": "பெண்கள் நாடாளுமன்ற ஒதுக்கீடு உறுப்பு 16(4B)-ல் இல்லை." }
    },
    "tnpsc_tip": {
      "en": "81st CAA 2000 -> Art 16(4B) -> Carry forward rule for Backlog Vacancies exempt from 50% cap.",
      "ta": "81வது திருத்தம் 2000 -> உறுப்பு 16(4B) -> 50% வரம்பின்றி பின்தங்கிய காலிப்பணியிடங்களை முன்னெடுத்துச் செல்லும் விதி."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Medium", "level": "TNPSC Group 1" }
  },

  # 6. Case / Amendment Based: Indra Sawhney Case 1992 Ruling - Ans: C
  {
    "id": "FR_M_006",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Medium",
    "question_type": "Case / Amendment",
    "question": {
      "en": "Which of the following principles was NOT laid down by the Supreme Court nine-judge bench in the landmark Indra Sawhney v. Union of India case (1992)?",
      "ta": "புகழ்பெற்ற இந்திரா சாஹ்னி எதிர் இந்திய யூனியன் வழக்கில் (1992) உச்ச நீதிமன்றத்தின் ஒன்பது நீதிபதிகள் அமர்வால் வழங்கப்படாத கோட்பாடு எது?"
    },
    "options": [
      { "id": "A", "en": "Total reserved quota should not exceed 50% except in extraordinary situations.", "ta": "அசாாதாரண சூழ்நிலைகளைத் தவிர மொத்த இடஒதுக்கீட்டு அளவு 50%-ஐத் தாண்டக்கூடாது." },
      { "id": "B", "en": "The 'Creamy Layer' must be excluded from the Backward Classes for reservation benefit.", "ta": "இடஒதுக்கீட்டுப் பயனிலிருந்து பிற்படுத்தப்பட்ட வகுப்பினரிடையே உள்ள 'கிரீமி லேயர்' (சலுகை பெற்ற மேல்தட்டு) விலக்கப்பட வேண்டும்." },
      { "id": "C", "en": "Reservation in promotions for OBCs is a permanent Fundamental Right.", "ta": "OBC-களுக்குப் பதவி உயர்வில் இடஒதுக்கீடு என்பது ஒரு நிரந்தர அடிப்படை உரிமையாகும்." },
      { "id": "D", "en": "Backwardness cannot be defined solely on the basis of economic criteria alone without social backwardness.", "ta": "சமூகப் பின்தங்கிய நிலையின்றி வெறும் பொருளாதார அடிப்படைகளில் மட்டுமே பின்தங்கிய நிலையை வரையறுக்க முடியாது." }
    ],
    "correct_answer": "C",
    "explanation": {
      "en": "In Indra Sawhney (1992), SC held that reservation under Art 16(4) is confined to INITIAL APPOINTMENT ONLY and cannot be extended to promotions. (77th CAA 1997 subsequently inserted Art 16(4A) for SC/ST promotions).",
      "ta": "இந்திரா சாஹ்னி வழக்கில் (1992), உறுப்பு 16(4)-ன் கீழ் இடஒதுக்கீடு ஆரம்ப நியமனத்திற்கு மட்டுமே பொருந்தும், பதவி உயர்வுக்கு விரிவாக்க முடியாது என SC தீர்ப்பளித்தது."
    },
    "why_not_others": {
      "A": { "en": "Indra Sawhney fixed the 50% ceiling rule.", "ta": "இந்திரா சாஹ்னி 50% உச்ச வரம்பு விதியை நிர்ணயித்தது." },
      "B": { "en": "Indra Sawhney mandated creamy layer exclusion.", "ta": "இந்திரா சாஹ்னி கிரீமி லேயர் விலக்கைக் கட்டாயமாக்கியது." },
      "C": { "en": "Correct. SC REJECTED reservation in promotions under Art 16(4).", "ta": "சரி. SC உறுப்பு 16(4)-ன் கீழ் பதவி உயர்வு இடஒதுக்கீட்டை நிராகரித்தது." },
      "D": { "en": "Indra Sawhney held economic status alone cannot define backwardness under Art 16(4).", "ta": "இந்திரா சாஹ்னி பொருளாதார நிலை மட்டுமே பின்தங்கிய நிலையை வரையறுக்க முடியாது என்றது." }
    },
    "tnpsc_tip": {
      "en": "Indra Sawhney (1992) = Mandal Case (50% cap, Creamy layer exclusion, No promotion quota in Art 16(4)).",
      "ta": "இந்திரா சாஹ்னி (1992) = மண்டல் வழக்கு (50% உச்சவரம்பு, கிரீமி லேயர் நீக்கம், 16(4)-ல் பதவி உயர்வு இடஒதுக்கீடு இல்லை)."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Medium", "level": "TNPSC Group 1" }
  },

  # 7. Article / Provision Based: Reasonable Restrictions Grounds under Art 19 - Ans: A
  {
    "id": "FR_M_007",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Medium",
    "question_type": "Article/Provision Based",
    "question": {
      "en": "Freedom of Speech and Expression under Article 19(1)(a) is subject to reasonable restrictions under Article 19(2). Which ground was added to Article 19(2) by the 16th Constitutional Amendment Act, 1963?",
      "ta": "உறுப்பு 19(1)(a)-ன் கீழ் பேச்சு மற்றும் கருத்துச் சுதந்திரம் உறுப்பு 19(2)-ன் நியாயமான கட்டுப்பாடுகளுக்கு உட்பட்டது. 1963-ன் 16வது அரசியலமைப்பு திருத்தச் சட்டத்தால் உறுப்பு 19(2)-ல் சேர்க்கப்பட்ட அடிப்படை எது?"
    },
    "options": [
      { "id": "A", "en": "Sovereignty and Integrity of India", "ta": "இந்தியாவின் இறையாண்மை மற்றும் ஒருமைப்பாடு" },
      { "id": "B", "en": "Public Order and Morality", "ta": "பொது ஒழுங்கு மற்றும் ஒழுக்கம்" },
      { "id": "C", "en": "Contempt of Court", "ta": "நீதிமன்ற அவமதிப்பு" },
      { "id": "D", "en": "Friendly relations with foreign States", "ta": "வெளிநாட்டு அரசுகளுடனான நட்புறவு" }
    ],
    "correct_answer": "A",
    "explanation": {
      "en": "The 16th Constitutional Amendment Act, 1963 added 'Sovereignty and Integrity of India' as a restriction ground across Article 19 freedoms to prevent secessionist demands.",
      "ta": "1963-ன் 16வது அரசியலமைப்பு திருத்தச் சட்டம் பிரிவினைவாதக் கோரிக்கைகளைத் தடுக்க உறுப்பு 19 சுதந்திரங்களில் 'இந்தியாவின் இறையாண்மை மற்றும் ஒருமைப்பாடு' என்பதை வரம்பு அடிப்படையாகச் சேர்த்தது."
    },
    "why_not_others": {
      "A": { "en": "Correct. 16th CAA 1963 added 'Sovereignty and Integrity of India'.", "ta": "சரி. 16வது திருத்தம் 1963 'இந்தியாவின் இறையாண்மை மற்றும் ஒருமைப்பாடு' என்பதைச் சேர்த்தது." },
      "B": { "en": "Public Order was added by 1st CAA 1951.", "ta": "பொது ஒழுங்கு 1வது திருத்தம் 1951 மூலம் சேர்க்கப்பட்டது." },
      "C": { "en": "Contempt of Court was present in original text/early amendments.", "ta": "நீதிமன்ற அவமதிப்பு ஆரம்ப விதிகளில் இருந்தது." },
      "D": { "en": "Friendly relations with foreign States was added by 1st CAA 1951.", "ta": "வெளிநாட்டு நட்புறவு 1வது திருத்தம் 1951 மூலம் சேர்க்கப்பட்டது." }
    },
    "tnpsc_tip": {
      "en": "16th CAA 1963 introduced 'Sovereignty and Integrity of India' into Art 19 restriction grounds.",
      "ta": "16வது திருத்தம் 1963 உறுப்பு 19 கட்டுப்பாட்டு அடிப்படைகளில் 'இந்தியாவின் இறையாண்மை மற்றும் ஒருமைப்பாடு' என்பதை அறிமுகப்படுத்தியது."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Medium", "level": "TNPSC Group 1" }
  },

  # 8. Conceptual Distinction: Article 19 vs Article 21 Relationship - Ans: D
  {
    "id": "FR_M_008",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Medium",
    "question_type": "Conceptual Distinction",
    "question": {
      "en": "Prior to Maneka Gandhi (1978), the Supreme Court in Gopalan (1950) viewed Articles 19 and 21 as mutually exclusive 'water-tight compartments'. How did Maneka Gandhi (1978) transform this relationship?",
      "ta": "மேனகா காந்திக்கு (1978) முன், கோபாலன் வழக்கில் (1950) உச்ச நீதிமன்றம் உறுப்புகள் 19 மற்றும் 21-ஐ ஒன்றுக்கொன்று தொடர்பற்ற தனியறைகளாகக் கருதியது. மேனகா காந்தி (1978) இந்தத் தொடர்பை எவ்வாறு மாற்றியது?"
    },
    "options": [
      { "id": "A", "en": "It declared Article 19 superior to Article 21 in all emergency situations.", "ta": "இது அனைத்து அவசரநிலைகளிலும் உறுப்பு 19 உறுப்பு 21-ஐ விட மேலானது என அறிவித்தது." },
      { "id": "B", "en": "It held that Article 21 applies only to criminal cases, while Article 19 applies to civil matters.", "ta": "உறுப்பு 21 குற்றவியல் வழக்குகளுக்கு மட்டுமே பொருந்தும், உறுப்பு 19 சிவில் விஷயங்களுக்குப் பொருந்தும் எனத் தீர்ப்பளித்தது." },
      { "id": "C", "en": "It completely abolished judicial review of procedure established by law.", "ta": "இது சட்டத்தால் நிறுவப்பட்ட நடைமுறையின் நீதித்துறை ஆய்வை முற்றிலும் நீக்கியது." },
      { "id": "D", "en": "It established that Articles 14, 19, and 21 are non-exclusive and interconnected ('Golden Triangle'), meaning a law depriving personal liberty under Art 21 must also pass tests of Art 14 and Art 19.", "ta": "இது உறுப்புகள் 14, 19, 21 ஆகியவை ஒன்றுக்கொன்று தொடர்புள்ள 'தங்க முக்கோணம்' என நிறுவியது, அதாவது உறுப்பு 21-ன் கீழ் தனிநபர் சுதந்திரத்தைப் பறிக்கும் ஒரு சட்டம் உறுப்பு 14 மற்றும் 19-ன் சோதனைகளையும் கடக்க வேண்டும்." }
    ],
    "correct_answer": "D",
    "explanation": {
      "en": "Maneka Gandhi (1978) established that a law depriving personal liberty under Art 21 must not be arbitrary (Art 14) and must satisfy reasonable restriction tests (Art 19), creating the Golden Triangle doctrine.",
      "ta": "மேனகா காந்தி (1978) உறுப்பு 21-ன் கீழ் தனிநபர் சுதந்திரத்தைப் பறிக்கும் ஒரு சட்டம் தன்னிச்சையானதாக இருக்கக்கூடாது (உறுப்பு 14) மற்றும் உறுப்பு 19-ன் கட்டுப்பாட்டுச் சோதனைகளைப் பூர்த்தி செய்ய வேண்டும் எனத் தங்க முக்கோணக் கோட்பாட்டை நிறுவியது."
    },
    "why_not_others": {
      "A": { "en": "Incorrect. Article 21 cannot be suspended during Emergency.", "ta": "தவறு. உறுப்பு 21 அவசரநிலையின் போது இடைநிறுத்தப்பட முடியாது." },
      "B": { "en": "Incorrect. Art 21 applies broadly to life and liberty.", "ta": "தவறு. உறுப்பு 21 வாழ்வு மற்றும் சுதந்திரத்திற்குப் பரவலாகப் பொருந்தும்." },
      "C": { "en": "Incorrect. Maneka Gandhi EXPANDED judicial review.", "ta": "தவறு. மேனகா காந்தி நீதித்துறை ஆய்வை விரிவுபடுத்தியது." },
      "D": { "en": "Correct. Maneka Gandhi established the Golden Triangle of Arts 14, 19, and 21.", "ta": "சரி. மேனகா காந்தி உறுப்புகள் 14, 19, 21-ன் தங்க முக்கோணத்தை நிறுவியது." }
    },
    "tnpsc_tip": {
      "en": "Golden Triangle of Indian Constitution = Articles 14, 19, and 21.",
      "ta": "இந்திய அரசியலமைப்பின் தங்க முக்கோணம் = உறுப்புகள் 14, 19 மற்றும் 21."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Medium", "level": "TNPSC Group 1" }
  },

  # 9. Conceptual Distinction: Punitive vs Preventive Detention - Ans: B
  {
    "id": "FR_M_009",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Medium",
    "question_type": "Conceptual Distinction",
    "question": {
      "en": "Which statement correctly distinguishes 'Punitive Detention' from 'Preventive Detention' under the Indian Constitution?",
      "ta": "இந்திய அரசியலமைப்பின் கீழ் 'தண்டனைக்கான காவல்' (Punitive Detention) மற்றும் 'தடுப்புக் காவல்' (Preventive Detention) ஆகியவற்றிற்கு இடையேயான வேறுபாட்டைச் சரியாக விளக்கும் கூற்று எது?"
    },
    "options": [
      { "id": "A", "en": "Punitive detention is ordered without trial, whereas preventive detention requires a full criminal trial.", "ta": "தண்டனைக்கான காவல் விசாரணையின்றி உத்தரவிடப்படுகிறது, தடுப்புக் காவலுக்கு முழுமையான குற்றவியல் விசாரணை தேவை." },
      { "id": "B", "en": "Punitive detention punishes a person for an offence ALREADY committed after judicial trial; Preventive detention detains a person ON SUSPICION to prevent him from committing a future offence.", "ta": "தண்டனைக்கான காவல் என்பது நீதித்துறை விசாரணைக்குப் பின் ஏற்கனவே செய்த குற்றத்திற்காக ஒருவரைத் தண்டிப்பதாகும்; தடுப்புக் காவல் என்பது எதிர்காலக் குற்றத்தைச் செய்வதைத் தடுக்கச் சந்தேகத்தின் பேரில் ஒருவரைக் காவலில் வைப்பதாகும்." },
      { "id": "C", "en": "Punitive detention is governed by Article 22, whereas preventive detention is governed by Article 20.", "ta": "தண்டனைக்கான காவல் உறுப்பு 22-ல் ஆளப்படுகிறது, தடுப்புக் காவல் உறுப்பு 20-ல் ஆளப்படுகிறது." },
      { "id": "D", "en": "Punitive detention applies to foreigners only, whereas preventive detention applies to citizens only.", "ta": "தண்டனைக்கான காவல் வெளிநாட்டினருக்கு மட்டுமே பொருந்தும், தடுப்புக் காவல் குடிமக்களுக்கு மட்டுமே பொருந்தும்." }
    ],
    "correct_answer": "B",
    "explanation": {
      "en": "Punitive detention is post-trial punishment for a proven crime. Preventive detention is pre-crime precautionary detention based on reasonable apprehension/suspicion without formal trial.",
      "ta": "தண்டனைக்கான காவல் என்பது நிரூபிக்கப்பட்ட குற்றத்திற்கான விசாரணைக்குப் பிந்தைய தண்டனையாகும். தடுப்புக் காவல் என்பது முறையான விசாரணையின்றி முன்எச்சரிக்கை சந்தேகத்தின் பேரிலான காவமுறையாகும்."
    },
    "why_not_others": {
      "A": { "en": "Reversed. Punitive requires trial; Preventive is without full judicial trial.", "ta": "தலைகீழானது. தண்டனைக்கான காவலுக்கு விசாரணை தேவை; தடுப்புக் காவலுக்கு முழு நீதி விசாரணை இல்லை." },
      "B": { "en": "Correct. Post-offence punishment (Punitive) vs Pre-offence suspicion detention (Preventive).", "ta": "சரி. குற்றத்திற்குப் பிந்தைய தண்டனை (Punitive) vs குற்றத்திற்கு முந்தைய சந்தேகக் காவல் (Preventive)." },
      "C": { "en": "Preventive detention safeguards are in Article 22(4)-(7).", "ta": "தடுப்புக் காவல் பாதுகாப்புகள் உறுப்பு 22(4)-(7)-ல் உள்ளன." },
      "D": { "en": "Both types can apply to citizens and non-citizens.", "ta": "இரண்டு காவல்களுமே குடிமக்களுக்கும் வெளிநாட்டினருக்கும் பொருந்தும்." }
    },
    "tnpsc_tip": {
      "en": "India is one of the few democratic nations incorporating Preventive Detention within its Constitution.",
      "ta": "தன்னுடைய அரசியலமைப்பிற்குள்ளேயே தடுப்புக் காவலைச் சேர்த்துள்ள சில ஜனநாயக நாடுகளில் இந்தியாவும் ஒன்று."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Medium", "level": "TNPSC Group 1" }
  },

  # 10. Application / Inference: Article 22 Safeguards Exception (Alien Enemies) - Ans: A
  {
    "id": "FR_E_010_M",
    "id_alt": "FR_M_010",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Medium",
    "question_type": "Application/Inference",
    "question": {
      "en": "Under Article 22(3), which two classes of persons are DENIED the procedural safeguards of ordinary arrest (right to consult lawyer, 24-hour magistrate production)?",
      "ta": "உறுப்பு 22(3)-ன் கீழ், சாதாரணக் கைதின் நடைமுறைப் பாதுகாப்புகள் (வழக்கறிஞரைக் கலந்தாலோசிக்கும் உரிமை, 24 மணி நேர நடுவர் ஆஜர்) மறுக்கப்பட்ட இரண்டு பிரிவினர் யார்?"
    },
    "options": [
      { "id": "A", "en": "1. Enemy Aliens, and 2. Persons detained under a Preventive Detention law.", "ta": "1. எதிரி நாட்டு வெளிநாட்டினர் (Enemy Aliens), மற்றும் 2. தடுப்புக் காவல் சட்டத்தின் கீழ் காவலில் வைக்கப்பட்ட நபர்கள்." },
      { "id": "B", "en": "1. Government servants, and 2. Members of Parliament.", "ta": "1. அரசு ஊழியர்கள், மற்றும் 2. நாடாளுமன்ற உறுப்பினர்கள்." },
      { "id": "C", "en": "1. Minorities, and 2. Foreign tourists.", "ta": "1. சிறுபான்மையினர், மற்றும் 2. வெளிநாட்டு சுற்றுலாப் பயணிகள்." },
      { "id": "D", "en": "1. Persons arrested under civil warrants, and 2. Tax evaders.", "ta": "1. சிவில் வாரண்டுகளின் கீழ் கைது செய்யப்பட்ட நபர்கள், மற்றும் 2. வரி ஏய்ப்பாளர்கள்." }
    ],
    "correct_answer": "A",
    "explanation": {
      "en": "Article 22(3) explicitly states that the protective clauses 22(1) and 22(2) shall NOT apply to: (a) an enemy alien, or (b) any person arrested/detained under any law providing for preventive detention.",
      "ta": "உறுப்பு 22(3) வெளிப்படையாக 22(1) மற்றும் 22(2) பாதுகாப்புகள்: (a) எதிரி நாட்டு வெளிநாட்டினர், அல்லது (b) தடுப்புக் காவல் சட்டத்தின் கீழ் காவலில் வைக்கப்பட்ட நபர்கள் ஆகிய இருவருக்கும் பொருந்தாது என்கிறது."
    },
    "why_not_others": {
      "A": { "en": "Correct. Enemy Aliens and Preventive Detenus are excluded under Art 22(3).", "ta": "சரி. எதிரி நாட்டு வெளிநாட்டினரும் தடுப்புக் காவலில் உள்ளோரும் உறுப்பு 22(3)-ன் கீழ் விலக்கப்பட்டுள்ளனர்." },
      "B": { "en": "Government servants and MPs retain Art 22(1)&(2) safeguards when arrested.", "ta": "அரசு ஊழியர்கள் மற்றும் எம்பிக்களுக்கு கைது செய்யப்படும் போது 22(1)&(2) பாதுகாப்புகள் உண்டு." },
      "C": { "en": "Minorities and foreign tourists (friendly aliens) get Art 22 safeguards.", "ta": "சிறுபான்மையினர் மற்றும் நட்பு நாட்டு வெளிநாட்டினருக்கு உறுப்பு 22 பாதுகாப்புகள் உண்டு." },
      "D": { "en": "Civil arrest safeguards are separate under Civil Procedure Code.", "ta": "சிவில் கைது பாதுகாப்புகள் சிவில் நடைமுறைச் சட்டத்தின் கீழ் தனிப்பயனானவை." }
    },
    "tnpsc_tip": {
      "en": "Enemy Aliens & Preventive Detenus do NOT get the 24-hour Magistrate production right under Art 22(2).",
      "ta": "எதிரி நாட்டு வெளிநாட்டினருக்கும் தடுப்புக் காவலில் உள்ளோருக்கும் உறுப்பு 22(2)-ன் கீழ் 24 மணி நேர நடுவர் ஆஜர் உரிமை கிடையாது."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Medium", "level": "TNPSC Group 1" }
  },

  # 11. Conceptual Distinction: Article 23 vs Article 24 - Ans: C
  {
    "id": "FR_M_011",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Medium",
    "question_type": "Conceptual Distinction",
    "question": {
      "en": "What is the primary difference in scope between Article 23 and Article 24 under the 'Right Against Exploitation'?",
      "ta": "'சுரண்டலுக்கு எதிரான உரிமையின்' கீழ் உறுப்பு 23 மற்றும் உறுப்பு 24 ஆகியவற்றிற்கு இடையேயான முதன்மை எல்லை வேறுபாடு என்ன?"
    },
    "options": [
      { "id": "A", "en": "Article 23 applies only to children, whereas Article 24 applies only to women.", "ta": "உறுப்பு 23 குழந்தைகளுக்கு மட்டுமே பொருந்தும், அதேவேளையில் உறுப்பு 24 பெண்களுக்கு மட்டுமே பொருந்தும்." },
      { "id": "B", "en": "Article 23 is non-justiciable, whereas Article 24 is justiciable.", "ta": "உறுப்பு 23 நிலைநிறுத்த முடியாதது, அதேவேளையில் உறுப்பு 24 நிலைநிறுத்தக்கூடியது." },
      { "id": "C", "en": "Article 23 protects all persons against human trafficking, begar, and forced labour; Article 24 specifically protects children below 14 from employment in hazardous factories/mines.", "ta": "உறுப்பு 23 அனைத்து நபர்களையும் மனித வியாபாரம், வெட்டி வேலை, கட்டாய வேலையிலிருந்து பாதுகாக்கிறது; உறுப்பு 24 குறிப்பாக 14 வயதுக்குட்பட்ட குழந்தைகளை ஆபத்தான தொழிற்சாலைகள்/சுரங்க வேலைகளிலிருந்து பாதுகாக்கிறது." },
      { "id": "D", "en": "Article 23 applies to public sector only, whereas Article 24 applies to private sector only.", "ta": "உறுப்பு 23 பொதுத் துறைக்கு மட்டுமே பொருந்தும், அதேவேளையில் உறுப்பு 24 னியார்த் துறைக்கு மட்டுமே பொருந்தும்." }
    ],
    "correct_answer": "C",
    "explanation": {
      "en": "Article 23 is a general prohibition of forced labour, begar, and human trafficking protecting all persons. Article 24 is a specific child protection clause prohibiting child labour below 14 in hazardous industries.",
      "ta": "உறுப்பு 23 என்பது அனைத்து நபர்களையும் பாதுகாக்கும் கட்டாய வேலை, வெட்டி வேலை, மனித வியாபாரத் தடையாகும். உறுப்பு 24 என்பது ஆபத்தான தொழில்களில் 14 வயதுக்குட்பட்ட குழந்தை தொழிலாளர் தடையாகும்."
    },
    "why_not_others": {
      "A": { "en": "Incorrect. Art 23 covers all human beings; Art 24 covers children below 14.", "ta": "தவறு. உறுப்பு 23 அனைத்து மனிதர்களையும் உள்ளடக்கும்; உறுப்பு 24 14 வயதுக்குட்பட்ட குழந்தைகளை உள்ளடக்கும்." },
      "B": { "en": "Both Articles are justiciable Fundamental Rights.", "ta": "இரண்டு உறுப்புகளுமே நிலைநிறுத்தக்கூடிய அடிப்படை உரிமைகள்." },
      "C": { "en": "Correct. Art 23 = Forced Labour/Trafficking (General); Art 24 = Hazardous Child Labour (Specific).", "ta": "சரி. உறுப்பு 23 = கட்டாய வேலை/மனித வியாபாரம் (பொது); உறுப்பு 24 = ஆபத்தான குழந்தை தொழிலாளர் (குறிப்பிட்ட)." },
      "D": { "en": "Both Articles apply against both State and private individuals.", "ta": "இரண்டு உறுப்புகளுமே அரசு மற்றும் தனியார் நபர்கள் இருவருக்கும் எதிராகப் பொருந்தும்." }
    },
    "tnpsc_tip": {
      "en": "Both Art 23 and Art 24 are enforceable against private individuals as well as the State.",
      "ta": "உறுப்பு 23 மற்றும் 24 இரண்டுமே அரசு மற்றும் தனியார் நபர்களுக்கு எதிராக அமல்படுத்தக்கூடியவை."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Medium", "level": "TNPSC Group 1" }
  },

  # 12. Article / Provision Based: Articles 25-28 Religion Breakdown - Ans: B
  {
    "id": "FR_M_012",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Medium",
    "question_type": "Article/Provision Based",
    "question": {
      "en": "Regarding Article 28, in which type of educational institution is religious instruction COMPLETELY PROHIBITED?",
      "ta": "உறுப்பு 28 தொடர்பாக, எந்த வகையான கல்வி நிறுவனத்தில் மதக் கல்வி போதனை முற்றிலும் தடை செய்யப்பட்டுள்ளது?"
    },
    "options": [
      { "id": "A", "en": "Institutions administered by the State but established under a religious endowment or trust.", "ta": "அரசால் நிர்வகிக்கப்படும் ஆனால் மத அறக்கட்டளையின் கீழ் நிறுவப்பட்ட நிறுவனங்கள்." },
      { "id": "B", "en": "Institutions wholly maintained out of State funds.", "ta": "முழுமையாக அரசு நிதியால் பராமரிக்கப்படும் நிறுவனங்கள்." },
      { "id": "C", "en": "Institutions recognized by the State.", "ta": "அரசால் அங்கீகரிக்கப்பட்ட நிறுவனங்கள்." },
      { "id": "D", "en": "Institutions receiving financial aid from the State.", "ta": "அரசிடமிருந்து நிதியுதவி பெறும் நிறுவனங்கள்." }
    ],
    "correct_answer": "B",
    "explanation": {
      "en": "Under Article 28(1), no religious instruction shall be provided in any educational institution wholly maintained out of State funds. In Category B (trust schools), it is permitted; in Categories C & D, voluntary.",
      "ta": "உறுப்பு 28(1)-ன் கீழ் முழுமையாக அரசு நிதியால் பராமரிக்கப்படும் கல்வி நிறுவனங்களில் மதக் கல்வி போதிக்கப்படக்கூடாது. அறக்கட்டளைப் பள்ளிகளில் அனுமதிக்கப்படும்; அரசு உதவிபெறும்/அங்கீகரிக்கப்பட்ட பள்ளிகளில் விருப்பத்தின் பேரில்."
    },
    "why_not_others": {
      "A": { "en": "Category B (trust institutions) PERMITS religious instruction per Art 28(2).", "ta": "அறக்கட்டளை நிறுவனங்களில் உறுப்பு 28(2)-ன் கீழ் மதக் கல்வி போதனை அனுமதிக்கப்படுகிறது." },
      "B": { "en": "Correct. Wholly State-funded institutions face TOTAL PROHIBITION.", "ta": "சரி. முழுமையான அரசு நிதி நிறுவனங்களில் முற்றிலும் தடை செய்யப்பட்டுள்ளது." },
      "C": { "en": "State-recognized institutions allow voluntary religious instruction.", "ta": "அரசு அங்கீகரிக்கப்பட்ட நிறுவனங்கள் விருப்பத்தின் பேரில் அனுமதிக்கின்றன." },
      "D": { "en": "State-aided institutions allow voluntary religious instruction.", "ta": "அரசு உதவிபெறும் நிறுவனங்கள் விருப்பத்தின் பேரில் அனுமதிக்கின்றன." }
    },
    "tnpsc_tip": {
      "en": "Art 28: Wholly State Funded = Total Ban; Trust Administered = Permitted; Aided/Recognized = Voluntary.",
      "ta": "உறுப்பு 28: முழு அரசு நிதி = முழு தடை; அறக்கட்டளை நிர்வாகம் = அனுமதி; உதவிபெறும்/அங்கீகரிக்கப்பட்டவை = விருப்பத்தின் பேரில்."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Medium", "level": "TNPSC Group 1" }
  },

  # 13. Conceptual Distinction: Article 29 vs Article 30 - Ans: A
  {
    "id": "FR_M_013",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Medium",
    "question_type": "Conceptual Distinction",
    "question": {
      "en": "How do Article 29 and Article 30 differ with respect to their beneficiary group?",
      "ta": "பயனாளி குழு தொடர்பாக உறுப்பு 29 மற்றும் உறுப்பு 30 ஆகியவை எவ்வாறு வேறுபடுகின்றன?"
    },
    "options": [
      { "id": "A", "en": "Article 29 grants rights to ANY section of citizens (majority or minority), whereas Article 30 grants rights EXCLUSIVELY to Religious and Linguistic Minorities.", "ta": "உறுப்பு 29 குடிமக்களின் எந்தவொரு பிரிவிற்கும் (பெரும்பான்மையினர் அல்லது சிறுபான்மையினர்) உரிமைகளை வழங்குகிறது, அதேவேளையில் உறுப்பு 30 மத மற்றும் மொழி சிறுபான்மையினருக்கு மட்டுமே பிரத்யேகமாக உரிமைகளை வழங்குகிறது." },
      { "id": "B", "en": "Article 29 applies to foreigners only, whereas Article 30 applies to citizens only.", "ta": "உறுப்பு 29 வெளிநாட்டினருக்கு மட்டுமே பொருந்தும், அதேவேளையில் உறுப்பு 30 குடிமக்களுக்கு மட்டுமே பொருந்தும்." },
      { "id": "C", "en": "Article 29 covers linguistic minorities only, whereas Article 30 covers religious minorities only.", "ta": "உறுப்பு 29 மொழி சிறுபான்மையினரை மட்டுமே உள்ளடக்குகிறது, அதேவேளையில் உறுப்பு 30 மத சிறுபான்மையினரை மட்டுமே உள்ளடக்குகிறது." },
      { "id": "D", "en": "Article 29 applies to employment, whereas Article 30 applies to property acquisition.", "ta": "உறுப்பு 29 வேலைவாய்ப்பிற்குப் பொருந்தும், அதேவேளையில் உறுப்பு 30 சொத்து கையகப்படுத்தலுக்குப் பொருந்தும்." }
    ],
    "correct_answer": "A",
    "explanation": {
      "en": "Article 29(1) uses 'any section of citizens' (broader group, including majority). Article 30 specifically confers educational institution rights on 'all minorities, whether based on religion or language'.",
      "ta": "உறுப்பு 29(1) 'குடிமக்களின் எந்தவொரு பிரிவினர்' என்ற சொல்லைப் பயன்படுத்துகிறது (பெரும்பான்மையினர் உட்பட பரந்த குழு). உறுப்பு 30 குறிப்பாக 'மதம் அல்லது மொழி சார்ந்த அனைத்து சிறுபான்மையினருக்கும்' கல்வி நிறுவன உரிமைகளை வழங்குகிறது."
    },
    "why_not_others": {
      "A": { "en": "Correct. Art 29 = Any section of citizens; Art 30 = Religious & Linguistic Minorities only.", "ta": "சரி. உறுப்பு 29 = குடிமக்களின் எந்தப் பிரிவும்; உறுப்பு 30 = மத & மொழி சிறுபான்மையினர் மட்டுமே." },
      "B": { "en": "Both Articles apply to citizens.", "ta": "இரண்டு உறுப்புகளுமே குடிமக்களுக்குப் பொருந்தும்." },
      "C": { "en": "Article 30 explicitly covers BOTH Religious and Linguistic minorities.", "ta": "உறுப்பு 30 மத மற்றும் மொழி சிறுபான்மையினர் இருவரையுமே வெளிப்படையாக உள்ளடக்குகிறது." },
      "D": { "en": "Incorrect. Both Articles deal with cultural and educational rights.", "ta": "தவறு. இரண்டு உறுப்புகளுமே பண்பாட்டு மற்றும் கல்வி உரிமைகள் பற்றியவை." }
    },
    "tnpsc_tip": {
      "en": "TRAP: Article 29 is NOT confined to minorities only; Article 30 IS confined to minorities only.",
      "ta": "பொறி: உறுப்பு 29 சிறுபான்மையினருக்கு மட்டுமேயானது அல்ல; உறுப்பு 30 சிறுபான்மையினருக்கு மட்டுமேயானது."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Medium", "level": "TNPSC Group 1" }
  },

  # 14. Elimination-Based: Article 30 Judicial Principles (T.M.A. Pai 2002) - Ans: D
  {
    "id": "FR_M_014",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Medium",
    "question_type": "Elimination-Based",
    "question": {
      "en": "Which of the following statements regarding minority educational institutions under Article 30 is INCORRECT?",
      "ta": "உறுப்பு 30-ன் கீழ் உள்ள சிறுபான்மை கல்வி நிறுவனங்கள் தொடர்பான பின்வரும் கூற்றுகளில் எது தவறானது?"
    },
    "options": [
      { "id": "A", "en": "Minority status under Article 30 must be determined state-wise, treating the state population as the unit (T.M.A. Pai Foundation Case 2002).", "ta": "உறுப்பு 30-ன் கீழ் சிறுபான்மை அந்தஸ்து மாநில மக்கள் தொகையை ஒரு அலகாகக் கொண்டு மாநில வாரியாகத் தீர்மானிக்கப்பட வேண்டும் (T.M.A. பாய் வழக்கு 2002)." },
      { "id": "B", "en": "The right to administer does not include the right to maladminister; State can prescribe regulatory standards for academic excellence and sanitation.", "ta": "நிர்வகிக்கும் உரிமை தவறாக நிர்வகிக்கும் உரிமையை உள்ளடக்குவதில்லை; கல்விச் சிறப்பு மற்றும் சுகாதாரத்திற்கான ஒழுங்குமுறைத் தரங்களை அரசு நிர்ணயிக்கலாம்." },
      { "id": "C", "en": "Under Article 30(1A), compulsory acquisition of property of minority institutions requires compensation that does not abridge their constitutional right.", "ta": "உறுப்பு 30(1A)-ன் கீழ், சிறுபான்மை நிறுவனங்களின் சொத்தைக் கட்டாயமாகக் கையகப்படுத்தும்போது அவர்களின் அரசியலமைப்பு உரிமையைக் குறைக்காத இழப்பீடு வழங்கப்பட வேண்டும்." },
      { "id": "D", "en": "Minority educational institutions are completely immune from any regulatory laws enacted by the State for national security or labour welfare.", "ta": "சிறுபான்மை கல்வி நிறுவனங்கள் தேசிய பாதுகாப்பு அல்லது தொழிலாளர் நலனுக்காக அரசு இயற்றும் எந்தவொரு ஒழுங்குமுறைச் சட்டங்களிலிருந்தும் முற்றிலும் விலக்கு பெற்றவை." }
    ],
    "correct_answer": "D",
    "explanation": {
      "en": "Statement D is incorrect because minority educational institutions are NOT immune from general regulatory laws relating to national security, public order, sanitation, academic standards, or labour laws.",
      "ta": "கூற்று D தவறானது, ஏனெனில் சிறுபான்மை கல்வி நிறுவனங்கள் தேசிய பாதுகாப்பு, பொது ஒழுங்கு, சுகாதாரம், கல்வித் தரம் அல்லது தொழிலாளர் நலன் சார்ந்த பொதுவான ஒழுங்குமுறைச் சட்டங்களிலிருந்து விலக்கு பெறவில்லை."
    },
    "why_not_others": {
      "A": { "en": "Statement A is correct (T.M.A. Pai 2002 principle).", "ta": "கூற்று A சரியானது (T.M.A. பாய் 2002 கோட்பாடு)." },
      "B": { "en": "Statement B is correct ('Right to administer is not right to maladminister').", "ta": "கூற்று B சரியானது ('நிர்வகிக்கும் உரிமை தவறாக நிர்வகிக்கும் உரிமை அல்ல')." },
      "C": { "en": "Statement C is correct (Inserted by 44th CAA 1978 Art 30(1A)).", "ta": "கூற்று C சரியானது (44வது திருத்தம் 1978 உறுப்பு 30(1A) மூலம் சேர்ப்பு)." },
      "D": { "en": "Correct. Statement D is INCORRECT (State CAN regulate academic & welfare standards).", "ta": "சரி. கூற்று D தவறானது (அரசு கல்வி & நலத் தரங்களை ஒழுங்குபடுத்த முடியும்)." }
    },
    "tnpsc_tip": {
      "en": "Right to administer minority institutions is subject to general regulatory measures of the State.",
      "ta": "சிறுபான்மை நிறுவனங்களை நிர்வகிக்கும் உரிமை அரசின் பொதுவான ஒழுங்குமுறை நடவடிக்கைகளுக்கு உட்பட்டது."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Medium", "level": "TNPSC Group 1" }
  },

  # 15. Conceptual Distinction: Article 31 vs Article 300A - Ans: B
  {
    "id": "FR_M_015",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Medium",
    "question_type": "Conceptual Distinction",
    "question": {
      "en": "Which statement accurately describes the legal consequences of shifting the Right to Property from Article 31 (Part III) to Article 300A (Part XII) by the 44th Amendment Act, 1978?",
      "ta": "1978-ன் 44வது திருத்தச் சட்டத்தின் மூலம் சொத்துரிமையை உறுப்பு 31-லிருந்து (பகுதி III) உறுப்பு 300A-க்கு (பகுதி XII) மாற்றியதன் சட்ட விளைவுகளைத் துல்லியமாக விளக்கும் கூற்று எது?"
    },
    "options": [
      { "id": "A", "en": "Property deprivation can now be challenged directly in the Supreme Court under Article 32 without invoking ordinary laws.", "ta": "சொத்து பறிப்பை இப்போது சாதாரண சட்டங்களைப் பயன்படுத்தாமல் உறுப்பு 32-ன் கீழ் நேரடியாக உச்ச நீதிமன்றத்தில் எதிர்க்க முடியும்." },
      { "id": "B", "en": "Property right is no longer part of the Basic Structure; it protects against Executive action but NOT against valid Legislative law.", "ta": "சொத்துரிமை இனி அடிப்படை கட்டமைப்பின் பகுதி அல்ல; இது நிர்வாக நடவடிக்கைக்கு எதிராகப் பாதுகாக்கிறது, ஆனால் செல்லுபடியாகும் சட்டமன்றச் சட்டத்திற்கு எதிராக அல்ல." },
      { "id": "C", "en": "State is constitutionally bound to pay market-value compensation for acquiring any private property.", "ta": "எந்தவொரு தனியார் சொத்தையும் கையகப்படுத்தச் சந்தை மதிப்பு இழப்பீடு வழங்க அரசுக்கு அரசியலமைப்பு ரீதியாகக் கடமை உண்டு." },
      { "id": "D", "en": "Right to Property was completely abolished and declared illegal in India.", "ta": "சொத்துரிமை முற்றிலும் ஒழிக்கப்பட்டு இந்தியாவில் சட்டவிரோதமானது என அறிவிக்கப்பட்டது." }
    ],
    "correct_answer": "B",
    "explanation": {
      "en": "As a legal right under Art 300A, property is protected against executive action without authority of law, but Parliament can deprive property by enacting a valid law without constitutional amendment.",
      "ta": "உறுப்பு 300A-ன் கீழ் சட்டப்பூர்வ உரிமையாக, சட்ட அதிகாரமில்லாத நிர்வாக நடவடிக்கைக்கு எதிராகச் சொத்து பாதுகாக்கப்படுகிறது, ஆனால் அரசியலமைப்பு திருத்தமின்றி செல்லுபடியாகும் சட்டத்தை இயற்றி அரசே சொத்தைப் பறிக்கலாம்."
    },
    "why_not_others": {
      "A": { "en": "Art 32 is NOT available for legal rights under Art 300A (Art 226 must be used).", "ta": "உறுப்பு 300A சட்டப்பூர்வ உரிமைகளுக்கு உறுப்பு 32 கிடைக்காது (உறுப்பு 226-ஐப் பயன்படுத்த வேண்டும்)." },
      "B": { "en": "Correct. Art 300A protects against Executive action, NOT Legislative law.", "ta": "சரி. உறுப்பு 300A நிர்வாக நடவடிக்கைக்கு எதிராகப் பாதுகாக்கிறது, சட்டமன்றச் சட்டத்திற்கு எதிராக அல்ல." },
      "C": { "en": "Compensation is no longer guaranteed under Art 300A.", "ta": "உறுப்பு 300A-ன் கீழ் இழப்பீடு உத்தரவாதம் இல்லை." },
      "D": { "en": "Property right was NOT abolished; it was reclassified as a Constitutional/Legal right.", "ta": "சொத்துரிமை ஒழிக்கப்படவில்லை; அது அரசியலமைப்பு/சட்டப்பூர்வ உரிமையாக வகைப்படுத்தப்பட்டது." }
    },
    "tnpsc_tip": {
      "en": "Art 300A protects against Executive action without law, but NOT against valid Legislative law.",
      "ta": "உறுப்பு 300A சட்டமற்ற நிர்வாக நடவடிக்கைக்கு எதிராகப் பாதுகாக்கிறது, ஆனால் செல்லுபடியாகும் சட்டமன்றச் சட்டத்திற்கு எதிராக அல்ல."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Medium", "level": "TNPSC Group 1" }
  },

  # 16. Article / Provision Based: Article 32 Fundamental Right Status - Ans: A
  {
    "id": "FR_M_016",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Medium",
    "question_type": "Article/Provision Based",
    "question": {
      "en": "Why is the Supreme Court constitutionally obligated to entertain a writ petition filed under Article 32, whereas a High Court under Article 226 has discretionary power?",
      "ta": "உறுப்பு 32-ன் கீழ் தாக்கல் செய்யப்படும் மனுவை விசாரிக்க உச்ச நீதிமன்றம் அரசியலமைப்பு ரீதியாகக் கடமைப்பட்டுள்ளது ஏன், அதேவேளையில் உறுப்பு 226-ன் கீழ் உயர் நீதிமன்றத்திற்கு விருப்ப அதிகாரம் உள்ளது ஏன்?"
    },
    "options": [
      { "id": "A", "en": "Because the right to move the Supreme Court under Article 32 is ITSELF a Fundamental Right in Part III, whereas Article 226 is a constitutional provision outside Part III.", "ta": "ஏனெனில் உறுப்பு 32-ன் கீழ் உச்ச நீதிமன்றத்தை அணுகும் உரிமை சுயமாகவே பகுதி III-ல் உள்ள ஒரு அடிப்படை உரிமையாகும், அதேவேளையில் உறுப்பு 226 பகுதி III-க்கு வெளியே உள்ள அரசியலமைப்பு விதியாகும்." },
      { "id": "B", "en": "Because Supreme Court judges are appointed directly by the President.", "ta": "ஏனெனில் உச்ச நீதிமன்ற நீதிபதிகள் நேரடியாகக் குடியரசுத் தலைவரால் நியமிக்கப்படுகிறார்கள்." },
      { "id": "C", "en": "Because High Courts have no jurisdiction over Fundamental Rights.", "ta": "ஏனெனில் உயர் நீதிமன்றங்களுக்கு அடிப்படை உரிமைகள் மீது அதிகார வரம்பு இல்லை." },
      { "id": "D", "en": "Because Article 32 applies only to Parliament members.", "ta": "ஏனெனில் உறுப்பு 32 நாடாளுமன்ற உறுப்பினர்களுக்கு மட்டுமே பொருந்தும்." }
    ],
    "correct_answer": "A",
    "explanation": {
      "en": "Article 32 is itself a Fundamental Right guaranteed in Part III. Hence, Supreme Court cannot refuse to entertain an Art 32 petition for FR violation. Art 226 is a discretionary constitutional remedy.",
      "ta": "உறுப்பு 32 சுயமாகவே பகுதி III-ல் உத்தரவாதம் அளிக்கப்பட்ட ஒரு அடிப்படை உரிமையாகும். எனவே, அடிப்படை உரிமை மீறல் மனுவை விசாரிக்க உச்ச நீதிமன்றம் மறுக்க முடியாது. உறுப்பு 226 என்பது விருப்பத்திற்குரிய அரசியலமைப்புத் தீர்வாகும்."
    },
    "why_not_others": {
      "A": { "en": "Correct. Art 32 is ITSELF a Fundamental Right, making SC remedy mandatory.", "ta": "சரி. உறுப்பு 32 சுயமாகவே ஒரு அடிப்படை உரிமையாகும், எனவே உச்ச நீதிமன்றத் தீர்வு கட்டாயமானது." },
      "B": { "en": "Appointment method does not dictate writ jurisdiction obligation.", "ta": "நியமன முறை மனு அதிகார வரம்புக் கடமையை நிர்ணயிப்பதில்லை." },
      "C": { "en": "High Courts DO have jurisdiction over FRs under Art 226.", "ta": "உயர் நீதிமன்றங்களுக்கு உறுப்பு 226-ன் கீழ் FRs மீது அதிகாரம் உண்டு." },
      "D": { "en": "Art 32 applies to all persons whose FRs are violated.", "ta": "உறுப்பு 32 அடிப்படை உரிமை மீறப்பட்ட அனைத்து நபர்களுக்கும் பொருந்தும்." }
    },
    "tnpsc_tip": {
      "en": "Article 32 remedy is a Fundamental Right; Article 226 remedy is a Constitutional Right.",
      "ta": "உறுப்பு 32 தீர்வு ஒரு அடிப்படை உரிமை; உறுப்பு 226 தீர்வு ஒரு அரசியலமைப்பு உரிமை."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Medium", "level": "TNPSC Group 1" }
  },

  # 17. Conceptual Distinction: Habeas Corpus vs Mandamus Target Scope - Ans: C
  {
    "id": "FR_M_017",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Medium",
    "question_type": "Conceptual Distinction",
    "question": {
      "en": "Which statement accurately highlights the difference in target scope between the writ of 'Habeas Corpus' and the writ of 'Mandamus'?",
      "ta": "'Habeas Corpus' (ஆட்கொணர்வு) மற்றும் 'Mandamus' (செயலுறுத்தும்) பேராணைகளின் இலக்கு எல்லை வேறுபாட்டைத் துல்லியமாகச் சுட்டிக்காட்டும் கூற்று எது?"
    },
    "options": [
      { "id": "A", "en": "Mandamus can be issued against private individuals, whereas Habeas Corpus cannot.", "ta": "Mandamus தனியார் நபர்களுக்கு எதிராக வழங்கப்படலாம், அதேவேளையில் Habeas Corpus முடியாது." },
      { "id": "B", "en": "Both writs can be issued against the President of India and State Governors.", "ta": "இரண்டு பேராணைகளுமே இந்தியக் குடியரசுத் தலைவர் மற்றும் மாநில ஆளுநர்களுக்கு எதிராக வழங்கப்படலாம்." },
      { "id": "C", "en": "Habeas Corpus can be issued against BOTH public authorities and private individuals, whereas Mandamus can be issued ONLY against public authorities and NOT against private individuals.", "ta": "Habeas Corpus அரசு அமைப்புகள் மற்றும் தனியார் நபர்கள் இருவருக்குமே எதிராக வழங்கப்படலாம், அதேவேளையில் Mandamus அரசு அமைப்புகளுக்கு மட்டுமே வழங்கப்பட முடியும், தனியார் நபர்களுக்கு எதிராக முடியாது." },
      { "id": "D", "en": "Habeas Corpus is issued by High Courts only, whereas Mandamus is issued by Supreme Court only.", "ta": "Habeas Corpus உயர் நீதிமன்றத்தால் மட்டுமே வழங்கப்படுகிறது, அதேவேளையில் Mandamus உச்ச நீதிமன்றத்தால் மட்டுமே வழங்கப்படுகிறது." }
    ],
    "correct_answer": "C",
    "explanation": {
      "en": "Habeas Corpus is unique in being enforceable against both public bodies and private individuals detaining someone. Mandamus lies strictly against public bodies/officers to perform statutory duties.",
      "ta": "Habeas Corpus ஒருவரைக் காவலில் வைத்துள்ள அரசு அமைப்புகள் மற்றும் தனியார் நபர்கள் இருவருக்கும் எதிராக அமல்படுத்தக்கூடிய தனித்துவம் கொண்டது. Mandamus அரசு அமைப்புகள்/அதிகாரிகளுக்கு மட்டுமே பொருந்தும்."
    },
    "why_not_others": {
      "A": { "en": "Reversed. Mandamus CANNOT be issued against private individuals.", "ta": "தலைகீழானது. Mandamus தனியார் நபர்களுக்கு எதிராக வழங்க முடியாது." },
      "B": { "en": "Mandamus CANNOT be issued against President or Governors.", "ta": "Mandamus குடியரசுத் தலைவர் அல்லது ஆளுநர்களுக்கு எதிராக வழங்க முடியாது." },
      "C": { "en": "Correct. Habeas Corpus = Public + Private; Mandamus = Public ONLY.", "ta": "சரி. Habeas Corpus = அரசு + தனியார்; Mandamus = அரசு மட்டுமே." },
      "D": { "en": "Both SC (Art 32) and HC (Art 226) can issue both writs.", "ta": "இரண்டு நீதிமன்றங்களும் இரண்டு பேராணைகளையும் பிறப்பிக்கலாம்." }
    },
    "tnpsc_tip": {
      "en": "Habeas Corpus is the ONLY writ among the five that can be issued against a private individual.",
      "ta": "ஐந்து பேராணைகளில் தனியார் நபருக்கு எதிராக வழங்கப்படக்கூடிய ஒரே பேராணை ஆட்கொணர்வு பேராணை (Habeas Corpus) மட்டுமே."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Medium", "level": "TNPSC Group 1" }
  },

  # 18. Application / Inference: Prohibition vs Certiorari Target Authorities - Ans: D
  {
    "id": "FR_M_018",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Medium",
    "question_type": "Application/Inference",
    "question": {
      "en": "Following the Supreme Court judgment in Kraipak (1969), how does the scope of authorities against which 'Certiorari' can be issued differ from 'Prohibition'?",
      "ta": "கிரைபக் வழக்கு (1969) தீர்ப்பைத் தொடர்ந்து, 'Certiorari' பேராணை பிறப்பிக்கப்படக்கூடிய அதிகார அமைப்புகளின் எல்லை 'Prohibition' பேராணையிலிருந்து எவ்வாறு வேறுபடுகிறது?"
    },
    "options": [
      { "id": "A", "en": "Prohibition applies to administrative authorities, whereas Certiorari applies to judicial bodies only.", "ta": "Prohibition நிர்வாக அமைப்புகளுக்குப் பொருந்தும், அதேவேளையில் Certiorari நீதித்துறை அமைப்புகளுக்கு மட்டுமே பொருந்தும்." },
      { "id": "B", "en": "Certiorari applies to private individuals, whereas Prohibition applies to legislative bodies.", "ta": "Certiorari தனியார் நபர்களுக்குப் பொருந்தும், அதேவேளையில் Prohibition சட்டமன்ற அமைப்புகளுக்குப் பொருந்தும்." },
      { "id": "C", "en": "Both writs apply strictly to private corporations only.", "ta": "இரண்டு பேராணைகளுமே தனியார் கார்ப்பரேஷன்களுக்கு மட்டுமே கண்டிப்பாகப் பொருந்தும்." },
      { "id": "D", "en": "Prohibition can be issued ONLY against Judicial and Quasi-Judicial authorities, whereas Certiorari can be issued against Judicial, Quasi-Judicial AND Administrative authorities affecting rights.", "ta": "Prohibition நீதித்துறை மற்றும் பகுதி-நீதித்துறை அமைப்புகளுக்கு மட்டுமே வழங்க முடியும், அதேவேளையில் Certiorari நீதித்துறை, பகுதி-நீதித்துறை மற்றும் உரிமைகளைப் பாதிக்கும் நிர்வாக அமைப்புகளுக்கும் (Administrative authorities) வழங்க முடியும்." }
    ],
    "correct_answer": "D",
    "explanation": {
      "en": "In A.K. Kraipak (1969), SC expanded Certiorari to cover administrative authorities affecting rights of individuals. Prohibition remains restricted to judicial and quasi-judicial bodies.",
      "ta": "ஏ.கே. கிரைபக் வழக்கில் (1969), தனிநபர்களின் உரிமைகளைப் பாதிக்கும் நிர்வாக அமைப்புகளுக்கும் Certiorari-ஐ உச்ச நீதிமன்றம் விரிவுபடுத்தியது. Prohibition நீதித்துறை அமைப்புகளுக்கு மட்டுமே கட்டுப்படுத்தப்பட்டுள்ளது."
    },
    "why_not_others": {
      "A": { "en": "Reversed. Certiorari covers administrative bodies; Prohibition does not.", "ta": "தலைகீழானது. Certiorari நிர்வாக அமைப்புகளை உள்ளடக்கும்; Prohibition இல்லை." },
      "B": { "en": "Neither writ applies to private individuals or legislative bodies.", "ta": "இரண்டு பேராணைகளுமே தனியாருக்கோ சட்டமன்றத்திற்கோ பொருந்தாது." },
      "C": { "en": "Writs do not lie against private corporations.", "ta": "பேராணைகள் தனியார் கார்ப்பரேஷன்களுக்குப் பொருந்தாது." },
      "D": { "en": "Correct. Certiorari extended to Administrative bodies in Kraipak 1969; Prohibition remains Judicial/Quasi-judicial only.", "ta": "சரி. கிரைபக் 1969-ல் Certiorari நிர்வாக அமைப்புகளுக்கு விரிவுபடுத்தப்பட்டது; Prohibition நீதித்துறை சார்ந்த அமைப்புகளுக்கு மட்டுமே." }
    },
    "tnpsc_tip": {
      "en": "Kraipak Case 1969 -> Certiorari extended to Administrative Authorities violating Principles of Natural Justice.",
      "ta": "கிரைபக் வழக்கு 1969 -> இயற்கை நீதியை மீறும் நிர்வாக அமைப்புகளுக்கும் Certiorari விரிவுபடுத்தப்பட்டது."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Medium", "level": "TNPSC Group 1" }
  },

  # 19. Application / Inference: Quo Warranto Substantive Public Office Test - Ans: A
  {
    "id": "FR_M_019",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Medium",
    "question_type": "Application/Inference",
    "question": {
      "en": "A petitioner files a writ of Quo Warranto challenging the appointment of a private company manager. Will the High Court entertain this petition?",
      "ta": "ஒரு மனுதாரர் ஒரு தனியார் நிறுவன மேலாளரின் நியமனத்தை எதிர்த்து தகுதி வினா பேராணை (Quo Warranto) தாக்கல் செய்கிறார். உயர் நீதிமன்றம் இந்த மனுவை விசாரிக்குமா?"
    },
    "options": [
      { "id": "A", "en": "No, because Quo Warranto lies ONLY in respect of a substantive PUBLIC office of permanent character created by statute or Constitution, NOT private offices.", "ta": "இல்லை, ஏனெனில் Quo Warranto என்பது சட்டத்தால் அல்லது அரசியலமைப்பால் உருவாக்கப்பட்ட நிரந்தரத் தன்மை கொண்ட பொதுப் பதவிக்கு (PUBLIC office) மட்டுமே பொருந்தும், தனியார் பதவிகளுக்கு அல்ல." },
      { "id": "B", "en": "Yes, because Quo Warranto applies to all employment positions across India.", "ta": "ஆம், ஏனெனில் Quo Warranto இந்தியா முழுவதிலும் உள்ள அனைத்து வேலைவாய்ப்புப் பதவிகளுக்கும் பொருந்தும்." },
      { "id": "C", "en": "Yes, because Locus Standi is relaxed for all private dispute petitions.", "ta": "ஆம், ஏனெனில் அனைத்துத் தனியார் தகராறு மனுக்களுக்கும் Locus Standi தளர்த்தப்பட்டுள்ளது." },
      { "id": "D", "en": "No, because only the Attorney General of India can file Quo Warranto.", "ta": "இல்லை, ஏனெனில் இந்திய தலைமை வழக்கறிஞர் மட்டுமே Quo Warranto தாக்கல் செய்ய முடியும்." }
    ],
    "correct_answer": "A",
    "explanation": {
      "en": "Quo Warranto requires that the office in question MUST be a substantive public office created by Constitution or statute. It CANNOT be issued against a private office or ministerial office.",
      "ta": "Quo Warranto-விற்கு சம்பந்தப்பட்ட பதவி அரசியலமைப்பு அல்லது சட்டத்தால் உருவாக்கப்பட்ட பொதுப் பதவியாக இருக்க வேண்டும். தனியார் பதவிக்கு எதிராக இதைப் பிறப்பிக்க முடியாது."
    },
    "why_not_others": {
      "A": { "en": "Correct. Quo Warranto requires a SUBSTANTIVE PUBLIC OFFICE.", "ta": "சரி. Quo Warranto-விற்கு ஒரு சட்டப்பூர்வ பொதுப் பதவி தேவை." },
      "B": { "en": "Quo Warranto does NOT apply to private sector jobs.", "ta": "Quo Warranto தனியார் துறை வேலைகளுக்குப் பொருந்தாது." },
      "C": { "en": "Relaxed locus standi applies only to public office challenges, not private contract disputes.", "ta": "தளர்த்தப்பட்ட மனு உரிமை பொதுப் பதவி சவால்களுக்கு மட்டுமே பொருந்தும்." },
      "D": { "en": "Any interested citizen can file Quo Warranto, not just the AG.", "ta": "ஆர்வமுள்ள எந்தக் குடிமகனும் Quo Warranto தாக்கல் செய்யலாம்." }
    },
    "tnpsc_tip": {
      "en": "Quo Warranto test: Substantive Public Office + Created by Statute/Constitution + Illegal Usurpation.",
      "ta": "Quo Warranto சோதனை: சட்டப்பூர்வ பொதுப் பதவி + சட்டத்தால் உருவாக்கப்பட்டது + சட்டவிரோதக் ஆக்கிரமிப்பு."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Medium", "level": "TNPSC Group 1" }
  },

  # 20. Article / Provision Based: Article 33 Parliament Power Limits - Ans: B
  {
    "id": "FR_M_020",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Medium",
    "question_type": "Article/Provision Based",
    "question": {
      "en": "Article 33 empowers Parliament to modify Fundamental Rights for members of Armed Forces. Does this power extend to non-combatant civilian employees attached to Armed Forces (such as cooks, tailors, mechanics)?",
      "ta": "ஆயுதப் படையினருக்கு அடிப்படை உரிமைகளை மாற்றியமைக்க நாடாளுமன்றத்திற்கு உறுப்பு 35 அதிகாரமளிக்கிறது. இந்த அதிகாரம் ஆயுதப் படைகளுடன் இணைந்துள்ள சண்டையிடா சிவில் ஊழியர்களுக்கும் (சமையல்காரர்கள், தையல்காரர்கள், மெக்கானிக்குகள்) விரிவாக்கப்படுமா?"
    },
    "options": [
      { "id": "A", "en": "No, Article 33 applies strictly to combat officers holding weapons only.", "ta": "இல்லை, உறுப்பு 33 ஆயுதங்களை வைத்துள்ள சண்டையிடும் அதிகாரிகளுக்கு மட்டுமே கண்டிப்பாகப் பொருந்தும்." },
      { "id": "B", "en": "Yes, Parliamentary laws made under Article 33 cover both combatants and non-combatant employees attached to the Armed Forces to maintain discipline.", "ta": "ஆம், உறுப்பு 33-ன் கீழ் இயற்றப்பட்ட நாடாளுமன்றச் சட்டங்கள் ஒழுங்கைப் பராமரிக்க ஆயுதப் படைகளுடன் இணைந்துள்ள சண்டையிடுவோர் மற்றும் சண்டையிடா ஊழியர்கள் இருவரையுமே உள்ளடக்குகின்றன." },
      { "id": "C", "en": "Yes, but only with prior written consent from the State Governor.", "ta": "ஆம், ஆனால் மாநில ஆளுநரின் முன் எழுத்துப்பூர்வ ஒப்புதலுடன் மட்டுமே." },
      { "id": "D", "en": "No, non-combatants are governed exclusively by local panchayat laws.", "ta": "இல்லை, சண்டையிடாதோர் உள்ளூர் பஞ்சாயத்துச் சட்டங்களால் மட்டுமே ஆளப்படுகிறார்கள்." }
    ],
    "correct_answer": "B",
    "explanation": {
      "en": "The Supreme Court has held that the expression 'members of the Armed Forces' in Article 33 includes non-combatant employees (cooks, barbers, mechanics) attached to armed forces, as discipline applies to the entire force.",
      "ta": "உறுப்பு 33-ல் உள்ள 'ஆயுதப் படையினர்' என்ற சொல் படைகளுடன் இணைந்துள்ள சண்டையிடா ஊழியர்களையும் (சமையல்காரர்கள், சலவை செய்பவர்கள்) உள்ளடக்கும் என உச்ச நீதிமன்றம் தீர்ப்பளித்துள்ளது."
    },
    "why_not_others": {
      "A": { "en": "SC rejected restricting Art 33 to combat officers only.", "ta": "உச்ச நீதிமன்றம் சண்டையிடும் அதிகாரிகளுக்கு மட்டுமேயானது என்பதை நிராகரித்தது." },
      "B": { "en": "Correct. Art 33 covers both combatant and non-combatant staff attached to forces.", "ta": "சரி. உறுப்பு 33 படைகளுடன் இணைந்துள்ள சண்டையிடுவோர் மற்றும் சண்டையிடா ஊழியர்கள் இருவரையுமே உள்ளடக்கும்." },
      "C": { "en": "Governor consent is not required for Parliamentary laws under Art 33.", "ta": "உறுப்பு 33 நாடாளுமன்றச் சட்டங்களுக்கு ஆளுநர் ஒப்புதல் தேவையில்லை." },
      "D": { "en": "Panchayat laws have no application to defense forces.", "ta": "பஞ்சாயத்துச் சட்டங்களுக்கும் பாதுகாப்புப் படைகளுக்கும் தொடர்பில்லை." }
    },
    "tnpsc_tip": {
      "en": "Article 33 covers Armed Forces, Police, Intelligence, and non-combatant support staff attached to them.",
      "ta": "உறுப்பு 33 ஆயுதப் படைகள், காவல்துறை, உளவுத்துறை மற்றும் அவற்றுடன் இணைந்துள்ள சண்டையிடா ஆதரவு ஊழியர்களையும் உள்ளடக்கும்."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Medium", "level": "TNPSC Group 1" }
  },

  # 21. Conceptual Distinction: Martial Law (Art 34) vs National Emergency (Art 352) - Ans: C
  {
    "id": "FR_M_021",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Medium",
    "question_type": "Conceptual Distinction",
    "question": {
      "en": "Which statement correctly highlights the constitutional distinction between 'Martial Law' (Article 34) and 'National Emergency' (Article 352)?",
      "ta": "'ராணுவ சட்டம்' (உறுப்பு 34) மற்றும் 'தேசிய அவசரநிலை' (உறுப்பு 352) ஆகியவற்றிற்கு இடையேயான அரசியலமைப்பு வேறுபாட்டைச் சரியாகச் சுட்டிக்காட்டும் கூற்று எது?"
    },
    "options": [
      { "id": "A", "en": "Martial Law affects the entire country, whereas National Emergency affects specific local areas only.", "ta": "ராணுவ சட்டம் நாடு முழுவதையும் பாதிக்கிறது, அதேவேளையில் தேசிய அவசரநிலை குறிப்பிட்ட உள்ளூர் பகுதிகளை மட்டுமே பாதிக்கிறது." },
      { "id": "B", "en": "Martial Law has detailed statutory provisions in Part XVIII, whereas National Emergency is not mentioned in the Constitution.", "ta": "ராணுவ சட்டம் பகுதி XVIII-ல் விரிவான விதிகளைக் கொண்டுள்ளது, அதேவேளையில் தேசிய அவசரநிலை அரசியலமைப்பில் குறிப்பிடப்படவில்லை." },
      { "id": "C", "en": "Martial Law affects ONLY Fundamental Rights in a specified area under military rule; National Emergency affects FRs, Centre-State relations, and legislative powers across the nation or state.", "ta": "ராணுவ சட்டம் ராணுவ ஆட்சியின் கீழ் உள்ள குறிப்பிட்ட பகுதியில் அடிப்படை உரிமைகளை மட்டுமே பாதிக்கிறது; தேசிய அவசரநிலை அடிப்படை உரிமைகள், மத்திய-மாநில உறவுகள் மற்றும் நாடாளுமன்ற அதிகாரங்களைப் பாதிக்கக்கூடியது." },
      { "id": "D", "en": "Both Martial Law and National Emergency automatically suspend Article 21.", "ta": "ராணுவ சட்டம் மற்றும் தேசிய அவசரநிலை இரண்டுமே தானாக உறுப்பு 21-ஐ இடைநிறுத்தும்." }
    ],
    "correct_answer": "C",
    "explanation": {
      "en": "Martial Law (Art 34) suspends civil administration and affects FRs locally to restore breakdown of order. National Emergency (Art 352) has wider constitutional impacts on Centre-State relations, revenues, and legislative powers.",
      "ta": "ராணுவ சட்டம் (உறுப்பு 34) சிவில் நிர்வாகத்தை நிறுத்தி உள்ளூரில் FRs-ஐப் பாதிக்கிறது. தேசிய அவசரநிலை (உறுப்பு 352) மத்திய-மாநில உறவுகள், வருவாய் பகிர்வு மீது பரந்த தாக்கத்தைக் கொண்டுள்ளது."
    },
    "why_not_others": {
      "A": { "en": "Reversed. Martial law affects specific areas; National Emergency can affect whole country.", "ta": "தலைகீழானது. ராணுவ சட்டம் குறிப்பிட்ட பகுதிகளைப் பாதிக்கும்; அவசரநிலை நாடு முழுவதையும் பாதிக்கும்." },
      "B": { "en": "National Emergency is detailed in Part XVIII; Martial Law is NOT defined in Constitution.", "ta": "தேசிய அவசரநிலை பகுதி XVIII-ல் உள்ளது; ராணுவ சட்டம் அரசியலமைப்பில் வரையறுக்கப்படவில்லை." },
      "C": { "en": "Correct. Martial Law = Local FR impact; National Emergency = Comprehensive Centre-State & FR impact.", "ta": "சரி. ராணுவ சட்டம் = உள்ளூர் FR தாக்கம்; தேசிய அவசரநிலை = விரிவான மத்திய-மாநில & FR தாக்கம்." },
      "D": { "en": "Article 21 CANNOT be suspended even during National Emergency.", "ta": "தேசிய அவசரநிலையின் போது கூட உறுப்பு 21 இடைநிறுத்தப்பட முடியாது." }
    },
    "tnpsc_tip": {
      "en": "Martial Law (Art 34) restores breakdown of order locally; National Emergency (Art 352) addresses war/external aggression/armed rebellion.",
      "ta": "ராணுவ சட்டம் (34) உள்ளூர் சட்டம் ஒழுங்கு முறிவைச் சீரமைக்கிறது; தேசிய அவசரநிலை (352) போர்/வெளிநாட்டு ஆக்கிரமிப்பு/ஆயுதமேந்திய கலகத்தைக் கையாள்கிறது."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Medium", "level": "TNPSC Group 1" }
  },

  # 22. Case / Amendment Based: Kesavananda Bharati & Basic Structure FRs - Ans: A
  {
    "id": "FR_M_022",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Medium",
    "question_type": "Case / Amendment",
    "question": {
      "en": "What ruling did the Supreme Court 13-judge bench give in Kesavananda Bharati v. State of Kerala (1973) regarding Parliament's power to amend Fundamental Rights under Article 368?",
      "ta": "கேசவானந்த பாரதி எதிர் கேரளா மாநிலம் (1973) வழக்கில் 13 நீதிபதிகள் அமர்வு உறுப்பு 368-ன் கீழ் அடிப்படை உரிமைகளைத் திருத்தும் நாடாளுமன்ற அதிகாரம் குறித்து என்ன தீர்ப்பளித்தது?"
    },
    "options": [
      { "id": "A", "en": "Parliament can amend ANY Part of the Constitution including Fundamental Rights under Article 368, provided it does NOT alter or damage the 'Basic Structure' of the Constitution.", "ta": "அரசியலமைப்பின் 'அடிப்படை கட்டமைப்பை' (Basic Structure) மாற்றவோ சிதைக்கவோ செய்யாதவரை, உறுப்பு 368-ன் கீழ் அடிப்படை உரிமைகள் உட்பட அரசியலமைப்பின் எந்தப் பகுதியையும் நாடாளுமன்றம் திருத்த முடியும்." },
      { "id": "B", "en": "Parliament has zero power to touch or amend any Fundamental Right under any circumstances.", "ta": "எந்தச் சூழ்நிலையிலும் எந்தவொரு அடிப்படை உரிமையையும் தொடுவதற்கோ திருத்துவதற்கோ நாடாளுமன்றத்திற்கு சுழி (பூஜ்ய) அதிகாரம் மட்டுமே உண்டு." },
      { "id": "C", "en": "Fundamental Rights can be amended only with 100% approval from all State Legislatures.", "ta": "அனைத்து மாநில சட்டமன்றங்களின் 100% ஒப்புதலுடன் மட்டுமே அடிப்படை உரிமைகளைத் திருத்த முடியும்." },
      { "id": "D", "en": "Article 368 amendments are completely beyond judicial review forever.", "ta": "உறுப்பு 368 திருத்தங்கள் எப்போதும் நீதித்துறை ஆய்வுக்கு முற்றிலும் அப்பாற்பட்டவை." }
    ],
    "correct_answer": "A",
    "explanation": {
      "en": "Kesavananda Bharati (1973) overruled Golak Nath (1967) and held that Parliament can amend Part III FRs, but its amending power under Art 368 is subject to the 'Basic Structure' doctrine.",
      "ta": "கேசவானந்த பாரதி (1973) கோலக் நாத் (1967) தீர்ப்பை மாற்றி, நாடாளுமன்றம் பகுதி III FRs-ஐத் திருத்த முடியும், ஆனால் உறுப்பு 368-ன் கீழ் அதன் திருத்தும் அதிகாரம் 'அடிப்படை கட்டமைப்பு' கோட்பாட்டிற்கு உட்பட்டது எனத் தீர்ப்பளித்தது."
    },
    "why_not_others": {
      "A": { "en": "Correct. Kesavananda Bharati established the Basic Structure doctrine.", "ta": "சரி. கேசவானந்த பாரதி அடிப்படை கட்டமைப்புக் கோட்பாட்டை நிறுவியது." },
      "B": { "en": "This was the Golak Nath 1967 view, which was OVERRULED in Kesavananda Bharati.", "ta": "இது கோலக் நாத் 1967 கருத்து, இது கேசவானந்த பாரதியில் மாற்றப்பட்டது." },
      "C": { "en": "State ratification is required only for specific federal provisions under Art 368 proviso.", "ta": "உறுப்பு 368-ன் கீழ் குறிப்பிட்ட கூட்டாட்சி விதிகளுக்கு மட்டுமே மாநில ஒப்புதல் தேவை." },
      "D": { "en": "Judicial review of amendments is part of Basic Structure (Minerva Mills 1980).", "ta": "திருத்தங்களின் நீதித்துறை ஆய்வு அடிப்படை கட்டமைப்பின் பகுதியாகும்." }
    },
    "tnpsc_tip": {
      "en": "Kesavananda Bharati (1973) = Largest 13-judge bench (7-6 majority) establishing Basic Structure.",
      "ta": "கேசவானந்த பாரதி (1973) = அடிப்படை கட்டமைப்பை நிறுவிய மிகப்பெரிய 13 நீதிபதிகள் அமர்வு (7-6 பெரும்பான்மை)."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Medium", "level": "TNPSC Group 1" }
  },

  # 23. Elimination-Based: Prohibited Discrimination Grounds Multi-Article Check - Ans: C
  {
    "id": "FR_M_023",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Medium",
    "question_type": "Elimination-Based",
    "question": {
      "en": "Which prohibited ground of discrimination is present in Article 15(1) and Article 16(2), but is EXCLUDED from Article 29(2)?",
      "ta": "உறுப்பு 15(1) மற்றும் உறுப்பு 16(2)-ல் உள்ள, ஆனால் உறுப்பு 29(2)-லிருந்து விலக்கப்பட்ட தடைசெய்யப்பட்ட பாகுபாட்டடிப்படைகள் எவை?"
    },
    "options": [
      { "id": "A", "en": "Religion and Caste", "ta": "மதம் மற்றும் சாதி" },
      { "id": "B", "en": "Race and Language", "ta": "இனம் மற்றும் மொழி" },
      { "id": "C", "en": "Sex and Place of Birth", "ta": "பாலினம் மற்றும் பிறந்த இடம்" },
      { "id": "D", "en": "Descent and Residence", "ta": "வம்சாவளி மற்றும் வசிப்பிடம்" }
    ],
    "correct_answer": "C",
    "explanation": {
      "en": "Art 15(1) grounds = Religion, Race, Caste, Sex, Place of Birth (5 grounds).\nArt 29(2) grounds = Religion, Race, Caste, Language (4 grounds).\n'SEX' and 'PLACE OF BIRTH' are in Art 15(1), but excluded from Art 29(2). 'Language' is added to Art 29(2).",
      "ta": "உறுப்பு 15(1) = மதம், இனம், சாதி, பாலினம், பிறந்த இடம் (5).\nஉறுப்பு 29(2) = மதம், இனம், சாதி, மொழி (4).\n'பாலினம்' மற்றும் 'பிறந்த இடம்' 15(1)-ல் உள்ளன, ஆனால் 29(2)-லிருந்து விலக்கப்பட்டு 'மொழி' சேர்க்கப்பட்டுள்ளது."
    },
    "why_not_others": {
      "A": { "en": "Religion and Caste are present in all three Articles (15, 16, 29).", "ta": "மதம் மற்றும் சாதி மூன்று உறுப்புகளிலுமே (15, 16, 29) உள்ளன." },
      "B": { "en": "Race is present in Art 29(2).", "ta": "இனம் உறுப்பு 29(2)-ல் உள்ளது." },
      "C": { "en": "Correct. Sex & Place of Birth are in Art 15, but NOT in Art 29(2).", "ta": "சரி. பாலினம் & பிறந்த இடம் உறுப்பு 15-ல் உள்ளன, உறுப்பு 29(2)-ல் இல்லை." },
      "D": { "en": "Descent and Residence are in Art 16(2) only.", "ta": "வம்சாவளி மற்றும் வசிப்பிடம் உறுப்பு 16(2)-ல் மட்டுமே உள்ளன." }
    },
    "tnpsc_tip": {
      "en": "Art 15(1) = 5 grounds; Art 16(2) = 7 grounds; Art 29(2) = 4 grounds (Religion, Race, Caste, Language).",
      "ta": "உறுப்பு 15(1) = 5; உறுப்பு 16(2) = 7; உறுப்பு 29(2) = 4 (மதம், இனம், சாதி, மொழி)."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Medium", "level": "TNPSC Group 1" }
  },

  # 24. Article / Provision Based: Doctrine of Severability & Eclipse - Ans: B
  {
    "id": "FR_M_024",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Medium",
    "question_type": "Article/Provision Based",
    "question": {
      "en": "Under Article 13(1), how does the 'Doctrine of Eclipse' apply to pre-constitutional laws that violate Fundamental Rights?",
      "ta": "உறுப்பு 13(1)-ன் கீழ், அடிப்படை உரிமைகளை மீறும் அரசியலமைப்பிற்கு முந்தைய சட்டங்களுக்கு 'மறைப்புக் கோட்பாடு' (Doctrine of Eclipse) எவ்வாறு பொருந்தும்?"
    },
    "options": [
      { "id": "A", "en": "The pre-constitutional law is dead for all time and cannot be revived under any circumstances.", "ta": "அரசியலமைப்பிற்கு முந்தைய சட்டம் எப்போதும் இறந்துவிட்டது, எந்தச் சூழ்நிலையிலும் அதை மீண்டும் உயிர்ப்பிக்க முடியாது." },
      { "id": "B", "en": "The unconstitutional pre-constitutional law is NOT dead ab initio, but remains dormant/eclipsed by the FR; if the FR is amended removing the shadow, the law becomes active again automatically.", "ta": "அரசியலமைப்புக்கு முரணான பழைய சட்டம் ஆரம்பத்திலிருந்தே இறந்துவிடவில்லை (dead ab initio அல்ல), மாறாக FR-ஆல் மறைக்கப்பட்டு (eclipsed) உறக்க நிலையில் உள்ளது; அரசியலமைப்பு திருத்தப்பட்டு நிழல் நீக்கப்பட்டால் அச்சட்டம் தானாக மீண்டும் செயல்படத் தொடங்கும்." },
      { "id": "C", "en": "The law applies only to non-citizens automatically.", "ta": "அச்சட்டம் குடிமக்கள் அல்லாதோருக்கு மட்டுமே தானாகப் பொருந்தும்." },
      { "id": "D", "en": "The law is transferred to the State List automatically.", "ta": "அச்சட்டம் தானாக மாநிலப் பட்டியலுக்கு மாற்றப்படும்." }
    ],
    "correct_answer": "B",
    "explanation": {
      "en": "Bhikaji Narain Case (1955): Pre-constitutional laws violating Part III are not void ab initio, but eclipsed by Fundamental Rights. Once the shadow is removed by constitutional amendment, the law revives.",
      "ta": "பிகாஜி நரேன் வழக்கு (1955): பகுதி III-ஐ மீறும் பழைய சட்டங்கள் ஆரம்பத்திலிருந்தே செல்லாதவை அல்ல, FRs-ஆல் மறைக்கப்படுகின்றன. அரசியலமைப்பு திருத்தத்தால் நிழல் நீக்கப்பட்டதும் சட்டம் உயிர்பெறும்."
    },
    "why_not_others": {
      "A": { "en": "Post-constitutional laws violating FRs are void ab initio, NOT pre-constitutional ones.", "ta": "FRs-ஐ மீறும் புதிய சட்டங்களே ஆரம்பத்திலிருந்தே செல்லாதவை (void ab initio), பழைய சட்டங்கள் அல்ல." },
      "B": { "en": "Correct. Doctrine of Eclipse applies to pre-constitutional laws (Art 13(1)).", "ta": "சரி. மறைப்புக் கோட்பாடு பழைய சட்டங்களுக்குப் பொருந்தும் (உறுப்பு 13(1))." },
      "C": { "en": "Pre-constitutional laws remain enforceable against non-citizens for rights not available to non-citizens.", "ta": "குடிமக்களுக்கு இல்லாத உரிமைகளுக்கு பழைய சட்டம் வெளிநாட்டினருக்குச் செயல்படலாம்." },
      "D": { "en": "List transfer does not occur.", "ta": "பட்டியல் மாற்றம் நடப்பதில்லை." }
    },
    "tnpsc_tip": {
      "en": "Doctrine of Severability = Cut invalid portion; Doctrine of Eclipse = Shadowed pre-const law revives if shadow removed.",
      "ta": "பிரிபடுதன்மை கோட்பாடு = செல்லாத பகுதியை நீக்குவது; மறைப்புக் கோட்பாடு = நிழல் நீங்கினால் பழைய சட்டம் உயிர்பெறுவது."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Medium", "level": "TNPSC Group 1" }
  },

  # 25. TNPSC Trap: Article 31C vs Article 14 & 19 Priority - Ans: A
  {
    "id": "FR_M_025",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Medium",
    "question_type": "TNPSC Trap",
    "question": {
      "en": "Under Article 31C, laws enacted to give effect to Directive Principles under Article 39(b) and 39(c) cannot be declared void on the ground of violating which Fundamental Rights?",
      "ta": "உறுப்பு 31C-ன் கீழ், உறுப்பு 39(b) மற்றும் 39(c)-ல் உள்ள அரசு நெறிமுறைக் கோட்பாடுகளைச் செயல்படுத்த இயற்றப்படும் சட்டங்கள் எந்த அடிப்படை உரிமைகளை மீறுகின்றன என்ற அடிப்படையில் செல்லாதென அறிவிக்கப்பட முடியாது?"
    },
    "options": [
      { "id": "A", "en": "Article 14 and Article 19", "ta": "உறுப்பு 14 மற்றும் உறுப்பு 19" },
      { "id": "B", "en": "Article 20 and Article 21", "ta": "உறுப்புகள் 20 மற்றும் 21" },
      { "id": "C", "en": "Article 25 and Article 26", "ta": "உறுப்புகள் 25 மற்றும் 26" },
      { "id": "D", "en": "Article 29 and Article 30", "ta": "உறுப்புகள் 29 மற்றும் 30" }
    ],
    "correct_answer": "A",
    "explanation": {
      "en": "Article 31C (inserted by 25th CAA 1971) states that no law giving effect to DPSP Art 39(b)&(c) shall be void for violating Art 14 or Art 19 ('Where Article 31C comes in, Article 14 goes out').",
      "ta": "உறுப்பு 31C (25வது திருத்தம் 1971) DPSP 39(b)&(c)-ஐச் செயல்படுத்தும் சட்டம் உறுப்பு 14 அல்லது 19-ஐ மீறினாலும் செல்லுபடியாகும் என்கிறது ('உறுப்பு 31C உள்ளே வரும் போது, உறுப்பு 14 வெளியே செல்லும்')."
    },
    "why_not_others": {
      "A": { "en": "Correct. Art 31C saves 39(b)&(c) laws from challenge under Art 14 and Art 19.", "ta": "சரி. உறுப்பு 31C 39(b)&(c) சட்டங்களை உறுப்புகள் 14 மற்றும் 19 சவால்களிலிருந்து காப்பாற்றுகிறது." },
      "B": { "en": "Arts 20 & 21 cannot be overridden by DPSP laws.", "ta": "உறுப்புகள் 20 & 21-ஐ DPSP சட்டங்கள் முறியடிக்க முடியாது." },
      "C": { "en": "Religious rights are not overridden by Art 31C.", "ta": "மத உரிமைகளை உறுப்பு 31C முறியடிக்காது." },
      "D": { "en": "Minority rights are not overridden by Art 31C.", "ta": "சிறுபான்மை உரிமைகளை உறுப்பு 31C முறியடிக்காது." }
    },
    "tnpsc_tip": {
      "en": "TRAP: Supreme Court held that DPSP Articles 39(b) and 39(c) take precedence over Fundamental Rights Articles 14 and 19 via Article 31C.",
      "ta": "பொறி: உறுப்பு 31C மூலம் DPSP உறுப்புகள் 39(b) மற்றும் 39(c) அடிப்படை உரிமைகள் 14 மற்றும் 19-ஐ விட முன்னுரிமை பெறுகின்றன."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Medium", "level": "TNPSC Group 1" }
  },

  # 26. Application / Inference: Habeas Corpus Against Private Person - Ans: D
  {
    "id": "FR_M_026",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Medium",
    "question_type": "Application/Inference",
    "question": {
      "en": "A citizen is illegally confined inside a private house by a private landlord. Which writ can be issued by the High Court under Article 226 against the private landlord?",
      "ta": "ஒரு குடிமகன் ஒரு தனியார் வீட்டு உரிமையாளரால் ஒரு தனியார் வீட்டிற்குள் சட்டவிரோதமாக அடைத்து வைக்கப்பட்டுள்ளார். அந்தத் தனியார் வீட்டு உரிமையாளருக்கு எதிராக உறுப்பு 226-ன் கீழ் உயர் நீதிமன்றம் எந்தப் பேராணையைப் பிறப்பிக்கலாம்?"
    },
    "options": [
      { "id": "A", "en": "Mandamus", "ta": "செயலுறுத்தும் பேராணை (Mandamus)" },
      { "id": "B", "en": "Certiorari", "ta": "நெறிமுறையுறுத்தும் பேராணை (Certiorari)" },
      { "id": "C", "en": "Prohibition", "ta": "தடைசெய் பேராணை (Prohibition)" },
      { "id": "D", "en": "Habeas Corpus", "ta": "ஆட்கொணர்வு பேராணை (Habeas Corpus)" }
    ],
    "correct_answer": "D",
    "explanation": {
      "en": "Habeas Corpus is the ONLY writ among the five that can be issued against BOTH public authorities and private individuals to secure release of a person illegally detained.",
      "ta": "சட்டவிரோதமாக அடைத்து வைக்கப்பட்ட நபரை விடுவிக்க அரசு அமைப்புகள் மற்றும் தனியார் நபர்கள் இருவருக்குமே எதிராகப் பிறப்பிக்கப்படக்கூடிய ஒரே பேராணை ஆட்கொணர்வு பேராணை (Habeas Corpus) மட்டுமே."
    },
    "why_not_others": {
      "A": { "en": "Mandamus CANNOT be issued against private individuals.", "ta": "Mandamus தனியார் நபர்களுக்கு எதிராகப் பிறப்பிக்க முடியாது." },
      "B": { "en": "Certiorari lies against judicial/administrative authorities only.", "ta": "Certiorari நீதித்துறை/நிர்வாக அமைப்புகளுக்கு மட்டுமே பொருந்தும்." },
      "C": { "en": "Prohibition lies against lower courts/tribunals only.", "ta": "Prohibition கீழ் நீதிமன்றங்களுக்கு மட்டுமே பொருந்தும்." },
      "D": { "en": "Correct. Habeas Corpus lies against private individuals.", "ta": "சரி. Habeas Corpus தனியார் நபர்களுக்கு எதிராகப் பொருந்தும்." }
    },
    "tnpsc_tip": {
      "en": "Habeas Corpus protects individual liberty against arbitrary detention by State OR private persons.",
      "ta": "ஆட்கொணர்வு பேராணை அரசு அல்லது தனியார் நபர்களின் தன்னிச்சையான காவலுக்கு எதிராக தனிநபர் சுதந்திரத்தைப் பாதுகாக்கிறது."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Medium", "level": "TNPSC Group 1" }
  },

  # 27. Article / Provision Based: Article 15(5) 93rd CAA Reservation Scope - Ans: B
  {
    "id": "FR_M_027",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Medium",
    "question_type": "Article/Provision Based",
    "question": {
      "en": "Article 15(5), added by the 93rd Amendment Act 2005, enables reservation for SEBCs/SCs/STs in educational institutions. Which specific category of institutions is EXEMPTED from Article 15(5)?",
      "ta": "2005-ன் 93வது திருத்தச் சட்டத்தால் சேர்க்கப்பட்ட உறுப்பு 15(5) கல்வி நிறுவனங்களில் SEBCs/SCs/STs-க்கு இடஒதுக்கீட்டை வழங்குகிறது. உறுப்பு 15(5)-லிருந்து விலக்கப்பட்ட குறிப்பிட்ட வகை நிறுவனம் எது?"
    },
    "options": [
      { "id": "A", "en": "State government medical colleges", "ta": "மாநில அரசு மருத்துவக் கல்லூரிகள்" },
      { "id": "B", "en": "Minority Educational Institutions referred to in Article 30(1)", "ta": "உறுப்பு 30(1)-ல் குறிப்பிடப்பட்டுள்ள சிறுபான்மை கல்வி நிறுவனங்கள்" },
      { "id": "C", "en": "Private un-aided engineering colleges", "ta": "தனியார் உதவிபெறா பொறியியல் கல்லூரிகள்" },
      { "id": "D", "en": "Central Universities (IITs & IIMs)", "ta": "மத்தியப் பல்கலைக்கழகங்கள் (IITs & IIMs)" }
    ],
    "correct_answer": "B",
    "explanation": {
      "en": "Article 15(5) permits state reservation in all educational institutions (aided or unaided, public or private), EXCEPT minority educational institutions referred to in Article 30(1).",
      "ta": "உறுப்பு 15(5) உறுப்பு 30(1)-ல் உள்ள சிறுபான்மை கல்வி நிறுவனங்களைத் தவிர மற்ற அனைத்துக் கல்வி நிறுவனங்களிலும் (அரசு, உதவிபெறும், உதவிபெறாத் தனியார்) இடஒதுக்கீட்டை அனுமதிக்கிறது."
    },
    "why_not_others": {
      "A": { "en": "State medical colleges are covered under Art 15(5).", "ta": "அரசு மருத்துவக் கல்லூரிகள் உறுப்பு 15(5)-ல் அடங்கும்." },
      "B": { "en": "Correct. Minority institutions under Art 30(1) are EXEMPTED from Art 15(5).", "ta": "சரி. உறுப்பு 30(1) சிறுபான்மை நிறுவனங்கள் உறுப்பு 15(5)-லிருந்து விலக்கப்பட்டுள்ளன." },
      "C": { "en": "Private unaided non-minority colleges ARE covered under Art 15(5).", "ta": "தனியார் உதவிபெறா சிறுபான்மையற்ற கல்லூரிகள் உறுப்பு 15(5)-ல் அடங்கும்." },
      "D": { "en": "Central Universities are covered under Central Educational Institutions Act 2006.", "ta": "மத்தியப் பல்கலைக்கழகங்கள் 2006 சட்டத்தின் கீழ் அடங்கும்." }
    },
    "tnpsc_tip": {
      "en": "Ashoka Kumar Thakur Case (2008) upheld Art 15(5) 93rd CAA & 27% OBC quota in higher education.",
      "ta": "அசோக் குமார் தாக்கூர் வழக்கு (2008) உறுப்பு 15(5) 93வது திருத்தம் & உயர்கல்வியில் 27% OBC ஒதுக்கீட்டை உறுதி செய்தது."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Medium", "level": "TNPSC Group 1" }
  },

  # 28. TNPSC Trap: Article 19 Reasonable Restrictions Prescribed List - Ans: A
  {
    "id": "FR_M_028",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Medium",
    "question_type": "TNPSC Trap",
    "question": {
      "en": "Can the Executive or Legislature impose restrictions on Article 19 freedoms on grounds OTHER THAN those explicitly mentioned in Clauses (2) to (6) of Article 19?",
      "ta": "உறுப்பு 19-ன் பிரிவுகள் (2) முதல் (6) வரை வெளிப்படையாகக் குறிப்பிடப்பட்டுள்ளதைத் தவிர வேறு அடிப்படைகளில் நிர்வாகமோ சட்டமன்றமோ உறுப்பு 19 சுதந்திரங்கள் மீது கட்டுப்பாடுகளை விதிக்க முடியுமா?"
    },
    "options": [
      { "id": "A", "en": "No, restrictions on Article 19 freedoms can be imposed ONLY on the grounds specified in Article 19(2) to (6) itself; no outside ground is constitutionally valid.", "ta": "இல்லை, உறுப்பு 19(2) முதல் (6) வரை குறிப்பிடப்பட்டுள்ள அடிப்படைகளில் மட்டுமே கட்டுப்பாடுகளை விதிக்க முடியும்; எந்தவொரு வெளிப்புற அடிப்படையையும் அரசியலமைப்பு ரீதியாக செல்லுபடியாகாது." },
      { "id": "B", "en": "Yes, Executive orders can add new restriction grounds whenever required.", "ta": "ஆம், தேவைப்படும்போதெல்லாம் நிர்வாக ஆணைகள் புதிய கட்டுப்பாட்டு அடிப்படைகளைச் சேர்க்கலாம்." },
      { "id": "C", "en": "Yes, any ground approved by simple majority in State Assembly is valid.", "ta": "ஆம், மாநிலச் சட்டமன்றத்தில் சாதாரண பெரும்பான்மையால் ஒப்புதலளிக்கப்பட்ட எந்த அடிப்படையும் செல்லுபடியாகும்." },
      { "id": "D", "en": "Yes, provided it is for economic growth.", "ta": "ஆம், பொருளாதார வளர்ச்சிக்காக இருக்கும் வரை செல்லுபடியாகும்." }
    ],
    "correct_answer": "A",
    "explanation": {
      "en": "The grounds of restriction specified in Art 19(2)-(6) are EXHAUSTIVE. Courts will strike down any restriction imposed on a ground not listed in the Constitution (e.g. Express Newspapers Case).",
      "ta": "உறுப்பு 19(2)-(6)-ல் குறிப்பிடப்பட்டுள்ள கட்டுப்பாட்டு அடிப்படைகள் முழுமையானவை. அரசியலமைப்பில் பட்டியலிடப்படாத அடிப்படையில் விதிக்கப்படும் எந்தக் கட்டுப்பாட்டையும் நீதிமன்றங்கள் ரத்து செய்யும்."
    },
    "why_not_others": {
      "A": { "en": "Correct. Restriction grounds in Art 19(2)-(6) are EXHAUSTIVE.", "ta": "சரி. உறுப்பு 19(2)-(6)-ல் உள்ள கட்டுப்பாட்டு அடிப்படைகள் முழுமையானவை." },
      "B": { "en": "Executive orders cannot create new restriction grounds.", "ta": "நிர்வாக ஆணைகள் புதிய கட்டுப்பாட்டு அடிப்படைகளை உருவாக்க முடியாது." },
      "C": { "en": "State Assembly cannot alter Art 19 grounds.", "ta": "மாநிலச் சட்டமன்றம் உறுப்பு 19 அடிப்படைகளை மாற்ற முடியாது." },
      "D": { "en": "Economic growth is not a standalone restriction ground in Art 19(2).", "ta": "பொருளாதார வளர்ச்சி என்பது உறுப்பு 19(2)-ல் தனிப்பட்ட கட்டுப்பாட்டு அடிப்படை அல்ல." }
    },
    "tnpsc_tip": {
      "en": "TRAP: Grounds of reasonable restriction under Art 19 are EXHAUSTIVE; no extra ground can be added by ordinary law.",
      "ta": "பொறி: உறுப்பு 19-ன் கீழ் நியாயமான கட்டுப்பாட்டு அடிப்படைகள் முழுமையானவை; சாதாரண சட்டத்தால் புதிய அடிப்படையைச் சேர்க்க முடியாது."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Medium", "level": "TNPSC Group 1" }
  },

  # 29. Elimination-Based: Article 20 Self-Incrimination Scope (Selvi Case 2010) - Ans: C
  {
    "id": "FR_M_029",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Medium",
    "question_type": "Elimination-Based",
    "question": {
      "en": "Under Article 20(3) protection against Self-Incrimination, which of the following forced tests was declared UNCONSTITUTIONAL by the Supreme Court in Selvi v. State of Karnataka (2010)?",
      "ta": "உறுப்பு 20(3) தனக்குத்தானே சாட்சியமளிப்பதற்கு எதிரான பாதுகாப்பின் கீழ், செல்வி எதிர் கர்நாடகா மாநிலம் (2010) வழக்கில் உச்ச நீதிமன்றத்தால் அரசியலமைப்புக்கு முரணானது என அறிவிக்கப்பட்ட கட்டாயச் சோதனை எது?"
    },
    "options": [
      { "id": "A", "en": "Giving thumb impressions", "ta": "கைரேகை அடையாளங்களை அளித்தல்" },
      { "id": "B", "en": "Giving blood samples for DNA matching", "ta": "DNA ஒப்பீட்டிற்காக இரத்த மாதிரிகளை அளித்தல்" },
      { "id": "C", "en": "Compulsory Narco-analysis, Polygraph (Lie Detector), and Brain Electrical Activation Profile (BEAP) tests without consent.", "ta": "சம்மதமின்றி கட்டாய நார்கோ-பகுப்பாய்வு (Narco-analysis), பாலிகிராஃப் (பொய் கண்டறியும் சோதனை) மற்றும் மூளை மின் அதிர்வு (BEAP) சோதனைகள்." },
      { "id": "D", "en": "Giving specimen handwriting or signature", "ta": "மாதிரிக் கையெழுத்து அல்லது கையொப்பத்தை அளித்தல்" }
    ],
    "correct_answer": "C",
    "explanation": {
      "en": "In Selvi v. State of Karnataka (2010), SC held that involuntary Narco-analysis, Polygraph, and Brain Mapping violate Article 20(3) (Self-incrimination) and Article 21 (Personal Liberty & Privacy).",
      "ta": "செல்வி எதிர் கர்நாடகா (2010) வழக்கில், கட்டாய நார்கோ-பகுப்பாய்வு, பாலிகிராஃப், மூளை வரைபட சோதனைகள் உறுப்பு 20(3) மற்றும் உறுப்பு 21-ஐ மீறுகின்றன என SC தீர்ப்பளித்தது."
    },
    "why_not_others": {
      "A": { "en": "Thumb impressions are physical evidence, permitted under Art 20(3) (Kathu Kalu Oghad 1961).", "ta": "கைரேகை அடையாளங்கள் பௌதிக சான்றுகள், உறுப்பு 20(3)-ன் கீழ் அனுமதிக்கப்படும்." },
      "B": { "en": "Blood samples for DNA are physical evidence, permitted under Art 20(3).", "ta": "இரத்த மாதிரிகள் பௌதிக சான்றுகள், அனுமதிக்கப்படும்." },
      "C": { "en": "Correct. Involuntary Narco/Polygraph tests violate Art 20(3) & Art 21.", "ta": "சரி. கட்டாய நார்கோ/பாலிகிராஃப் சோதனைகள் உறுப்பு 20(3) & 21-ஐ மீறுகின்றன." },
      "D": { "en": "Specimen signatures are physical evidence, permitted under Art 20(3).", "ta": "மாதிரிக் கையெழுத்து பௌதிக சான்று, அனுமதிக்கப்படும்." }
    },
    "tnpsc_tip": {
      "en": "Art 20(3) protects against TESTIMONIAL compulsion (verbal/mental disclosures), NOT physical evidence (fingerprints, blood).",
      "ta": "உறுப்பு 20(3) வாய்மொழி/மன வெளிப்பாட்டுச் சாட்சியக் கட்டாயத்திற்கு எதிராக மட்டுமே பாதுகாக்கிறது, பௌதிக சான்றுகளுக்கு (கைரேகை, இரத்தம்) அல்ல."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Medium", "level": "TNPSC Group 1" }
  },

  # 30. Article / Provision Based: Fundamental Rights Available ONLY to Citizens - Ans: D
  {
    "id": "FR_M_030",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Medium",
    "question_type": "Article/Provision Based",
    "question": {
      "en": "Which of the following complete combinations of Articles represents Fundamental Rights available EXCLUSIVELY to Citizens of India and NOT to foreigners?",
      "ta": "பின்வரும் எந்த முழுமையான உறுப்புகளின் சேர்க்கை வெளிநாட்டினருக்கு இல்லாமல் இந்தியக் குடிமக்களுக்கு மட்டுமே பிரத்யேகமாகக் கிடைக்கக்கூடிய அடிப்படை உரிமைகளைக் குறிக்கிறது?"
    },
    "options": [
      { "id": "A", "en": "Articles 14, 20, 21, 25, 27", "ta": "உறுப்புகள் 14, 20, 21, 25, 27" },
      { "id": "B", "en": "Articles 14, 15, 19, 21, 32", "ta": "உறுப்புகள் 14, 15, 19, 21, 32" },
      { "id": "C", "en": "Articles 17, 18, 20, 22, 24", "ta": "உறுப்புகள் 17, 18, 20, 22, 24" },
      { "id": "D", "en": "Articles 15, 16, 19, 29, 30", "ta": "உறுப்புகள் 15, 16, 19, 29, 30" }
    ],
    "correct_answer": "D",
    "explanation": {
      "en": "Articles 15 (Non-discrimination), 16 (Public employment), 19 (Six freedoms), 29 (Conservation of culture), and 30 (Minority institutions) are available ONLY to Citizens of India.",
      "ta": "உறுப்புகள் 15 (பாகுபாடின்மை), 16 (பொது வேலைவாய்ப்பு), 19 (ஆறு சுதந்திரங்கள்), 29 (பண்பாட்டுப் பாதுகாப்பு) மற்றும் 30 (சிறுபான்மை நிறுவனங்கள்) இந்தியக் குடிமக்களுக்கு மட்டுமே கிடைக்கக்கூடியவை."
    },
    "why_not_others": {
      "A": { "en": "Arts 14, 20, 21, 25 are available to ALL persons (citizens + foreigners).", "ta": "உறுப்புகள் 14, 20, 21, 25 அனைத்து நபர்களுக்கும் (குடிமக்கள் + வெளிநாட்டினர்) பொருந்தும்." },
      "B": { "en": "Arts 14 & 21 are available to foreigners.", "ta": "உறுப்புகள் 14 & 21 வெளிநாட்டினருக்குக் கிடைக்கும்." },
      "C": { "en": "Arts 20 & 22 are available to foreigners.", "ta": "உறுப்புகள் 20 & 22 வெளிநாட்டினருக்குக் கிடைக்கும்." },
      "D": { "en": "Correct. Articles 15, 16, 19, 29, and 30 are EXCLUSIVELY for Citizens.", "ta": "சரி. உறுப்புகள் 15, 16, 19, 29, மற்றும் 30 குடிமக்களுக்கு மட்டுமே பிரத்யேகமானவை." }
    },
    "tnpsc_tip": {
      "en": "Citizens ONLY = 15, 16, 19, 29, 30. All Persons (Citizens + Foreigners) = 14, 20, 21, 21A, 22, 23, 24, 25, 26, 27, 28.",
      "ta": "குடிமக்கள் மட்டுமே = 15, 16, 19, 29, 30. அனைத்து நபர்களும் (குடிமக்கள் + வெளிநாட்டினர்) = 14, 20, 21, 21A, 22, 23, 24, 25, 26, 27, 28."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Medium", "level": "TNPSC Group 1" }
  },

  # 31. Application / Inference: Article 21 Evolution Case Laws Matching - Ans: A
  {
    "id": "FR_M_031",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Medium",
    "question_type": "Application/Inference",
    "question": {
      "en": "Which landmark judgment expanded Article 21 to include the 'Right to Livelihood' for pavement dwellers?",
      "ta": "நடைபாதைவாசிகளுக்கான 'வாழ்வாதார உரிமையை' உறுப்பு 21-ல் சேர்க்க எந்த மைல்கல் தீர்ப்பு விரிவுபடுத்தியது?"
    },
    "options": [
      { "id": "A", "en": "Olga Tellis v. Bombay Municipal Corporation (1985)", "ta": "ஒல்கா டெல்லிஸ் எதிர் பம்பாய் முனிசிபல் கார்ப்பரேஷன் (1985)" },
      { "id": "B", "en": "Unni Krishnan v. State of Andhra Pradesh (1993)", "ta": "உன்னிகிருஷ்ணன் எதிர் ஆந்திரப் பிரதேசம் (1993)" },
      { "id": "C", "en": "Vishaka v. State of Rajasthan (1997)", "ta": "விஷாகா எதிர் ராஜஸ்தான் மாநிலம் (1997)" },
      { "id": "D", "en": "Parmanand Katara v. Union of India (1989)", "ta": "பர்மானந்த் கட்டாரா எதிர் இந்திய யூனியன் (1989)" }
    ],
    "correct_answer": "A",
    "explanation": {
      "en": "In Olga Tellis (1985), SC held that Right to Life under Art 21 includes Right to Livelihood because no person can live without the means of living.",
      "ta": "ஒல்கா டெல்லிஸ் வழக்கில் (1985), வாழ்வாதார வழிகளின்றி யாரும் வாழ முடியாது என்பதால் உறுப்பு 21-ன் கீழ் வாழ்வுரிமை வாழ்வாதார உரிமையையும் உள்ளடக்கும் என SC தீர்ப்பளித்தது."
    },
    "why_not_others": {
      "A": { "en": "Correct. Olga Tellis (1985) = Right to Livelihood under Art 21.", "ta": "சரி. ஒல்கா டெல்லிஸ் (1985) = உறுப்பு 21-ன் கீழ் வாழ்வாதார உரிமை." },
      "B": { "en": "Unni Krishnan (1993) declared Right to Education up to 14 years under Art 21.", "ta": "உன்னிகிருஷ்ணன் (1993) 14 வயது வரை கல்வி உரிமையை உறுப்பு 21-ல் அறிவித்தது." },
      "C": { "en": "Vishaka (1997) issued guidelines against sexual harassment at workplace.", "ta": "விஷாகா (1997) வேலை இடத்தில் பாலியல் துன்புறுத்தலுக்கு எதிரான வழிகாட்டுதல்களை வழங்கியது." },
      "D": { "en": "Parmanand Katara (1989) declared Right to Emergency Medical Aid.", "ta": "பர்மானந்த் கட்டாரா (1989) அவசர மருத்துவ உதவி உரிமையை அறிவித்தது." }
    },
    "tnpsc_tip": {
      "en": "Olga Tellis (1985) = Pavement Dwellers Case = Right to Livelihood under Art 21.",
      "ta": "ஒல்கா டெல்லிஸ் (1985) = நடைபாதைவாசிகள் வழக்கு = உறுப்பு 21-ன் கீழ் வாழ்வாதார உரிமை."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Medium", "level": "TNPSC Group 1" }
  },

  # 32. Case / Amendment Based: Vishaka Guidelines & Article 21 (Case / Amendment) - Ans: C
  {
    "id": "FR_M_032",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Medium",
    "question_type": "Case / Amendment",
    "question": {
      "en": "In Vishaka v. State of Rajasthan (1997), the Supreme Court laid down binding guidelines for protection of women against sexual harassment at workplaces by referring to which International Convention?",
      "ta": "விஷாகா எதிர் ராஜஸ்தான் மாநிலம் (1997) வழக்கில், எந்த சர்வதேச மாநாட்டைக் குறிப்பிட்டு வேலை இடங்களில் பெண்களுக்கு எதிரான பாலியல் துன்புறுத்தலுக்கு எதிரான பிணைப்பு வழிகாட்டுதல்களை உச்ச நீதிமன்றம் வழங்கியது?"
    },
    "options": [
      { "id": "A", "en": "Universal Declaration of Human Rights (UDHR 1948)", "ta": "மனித உரிமைகள் உலகளாவிய அறிவிப்பு (UDHR 1948)" },
      { "id": "B", "en": "International Covenant on Civil and Political Rights (ICCPR 1966)", "ta": "சிவில் மற்றும் அரசியல் உரிமைகள் சர்வதேச உடன்படிக்கை (ICCPR 1966)" },
      { "id": "C", "en": "Convention on the Elimination of All Forms of Discrimination Against Women (CEDAW 1979)", "ta": "பெண்களுக்கு எதிரான அனைத்து வகையான பாகுபாடுகளையும் ஒழிப்பதற்கான சர்வதேச மாநாடு (CEDAW 1979)" },
      { "id": "D", "en": "Geneva Convention on Red Cross 1949", "ta": "ரெட் க்ராஸ் ஜெனீவா மாநாடு 1949" }
    ],
    "correct_answer": "C",
    "explanation": {
      "en": "In Vishaka Case (1997), the Supreme Court enforced Articles 14, 19, and 21 by incorporating CEDAW (Convention on the Elimination of All Forms of Discrimination Against Women) principles into domestic law.",
      "ta": "விஷாகா வழக்கில் (1997), CEDAW (பெண்களுக்கு எதிரான பாகுபாடு ஒழிப்பு மாநாடு) தத்துவங்களை உள்நாட்டுச் சட்டத்திற்குள் இணைத்து உறுப்புகள் 14, 19, 21-ஐ உச்ச நீதிமன்றம் அமல்படுத்தியது."
    },
    "why_not_others": {
      "A": { "en": "UDHR is a general human rights instrument.", "ta": "UDHR என்பது பொதுவான மனித உரிமை ஆவணம்." },
      "B": { "en": "ICCPR deals with civil and political rights broadly.", "ta": "ICCPR பரந்த சிவில் உரிமைகள் பற்றியது." },
      "C": { "en": "Correct. Vishaka Guidelines relied directly on CEDAW.", "ta": "சரி. விஷாகா வழிகாட்டுதல்கள் நேரடியாக CEDAW-ஐச் சார்ந்திருந்தன." },
      "D": { "en": "Geneva Convention relates to armed conflict/prisoners of war.", "ta": "ஜெனீவா மாநாடு ஆயுத மோதல்/போர்க்கைதிகள் பற்றியது." }
    },
    "tnpsc_tip": {
      "en": "Vishaka (1997) led to the enactment of the POSH Act, 2013.",
      "ta": "விஷாகா (1997) வழக்கு 2013 POSH சட்டம் இயற்றப்பட வழிவகுத்தது."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Medium", "level": "TNPSC Group 1" }
  },

  # 33. Article / Provision Based: Article 27 Secular Spending Neutrality - Ans: B
  {
    "id": "FR_M_033",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Medium",
    "question_type": "Article/Provision Based",
    "question": {
      "en": "Under Article 27, if the State spends public tax funds for maintaining historical monuments or religious places, under what condition is such expenditure CONSTITUTIONALLY PERMISSIBLE?",
      "ta": "உறுப்பு 27-ன் கீழ் வரலாற்றுச் சின்னங்கள் அல்லது மத இடங்களைப் பராமரிக்க அரசு பொது வரிப் பணத்தைச் செலவிட்டால், எந்த நிபந்தனையின் கீழ் அச்செலவு அரசியலமைப்பு ரீதியாக அனுமதிக்கப்படும்?"
    },
    "options": [
      { "id": "A", "en": "If the funds are spent exclusively on the majority community's temples.", "ta": "நிதி பெரும்பான்மை சமூகத்தின் கோயில்களுக்கு மட்டுமே செலவிடப்பட்டால்." },
      { "id": "B", "en": "If public funds are spent neutrally and equally for promoting/maintaining ALL religions without favoring one particular religion over others.", "ta": "ஒரு குறிப்பிட்ட மதத்தை மற்ற மதங்களை விட ஆதரிக்காமல், அனைத்து மதங்களையும் ஊக்குவிக்க/பராமரிக்கப் பொது நிதி நடுநிலையாகவும் சமமாகவும் செலவிடப்பட்டால்." },
      { "id": "C", "en": "If the expenditure is approved by a religious trust.", "ta": "செலவு ஒரு மத அறக்கட்டளையால் ஒப்புதலளிக்கப்பட்டால்." },
      { "id": "D", "en": "Public tax funds can NEVER be spent on any place of worship under any circumstances.", "ta": "எந்தச் சூழ்நிலையிலும் எந்தவொரு வழிபாட்டுத் தலத்திற்கும் பொது வரிப் பணத்தைச் செலவிடவே முடியாது." }
    ],
    "correct_answer": "B",
    "explanation": {
      "en": "Article 27 prohibits using tax funds specifically for promoting ONE PARTICULAR religion. If the State promotes or maintains ALL religions equally without discrimination, it is constitutionally valid.",
      "ta": "ஒரு குறிப்பிட்ட மதத்தை ஊக்குவிக்க வரிப் பணத்தைப் பயன்படுத்துவதை மட்டுமே உறுப்பு 27 தடுக்கிறது. பாகுபாடின்றி அனைத்து மதங்களையும் அரசு சமமாகப் பராமரித்தால் அது அரசியலமைப்பு ரீதியாகச் செல்லுபடியாகும்."
    },
    "why_not_others": {
      "A": { "en": "Favoring majority religion violates Article 27.", "ta": "பெரும்பான்மை மதத்தை ஆதரிப்பது உறுப்பு 27-ஐ மீறும்." },
      "B": { "en": "Correct. Equal neutral spending on all religions does not violate Art 27.", "ta": "சரி. அனைத்து மதங்களுக்கும் சமமான நடுநிலைச் செலவு உறுப்பு 27-ஐ மீறாது." },
      "C": { "en": "Trust approval does not dictate constitutional validity.", "ta": "அறக்கட்டளை ஒப்புதல் அரசியலமைப்புச் செல்லுபடியை நிர்ணயிப்பதில்லை." },
      "D": { "en": "Neutral historical monument maintenance is allowed.", "ta": "நடுநிலையான வரலாற்றுச் சின்னப் பராமரிப்பு அனுமதிக்கப்படுகிறது." }
    },
    "tnpsc_tip": {
      "en": "Article 27 bars State favoritism of a particular religion, not neutral equal support to all religions.",
      "ta": "உறுப்பு 27 குறிப்பிட்ட மதத்திற்கான அரசின் சார்புநிலையைத் தடுக்கிறது, அனைத்து மதங்களுக்கும் நடுநிலையான சம ஆதரவைத் தடுக்கவில்லை."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Medium", "level": "TNPSC Group 1" }
  },

  # 34. TNPSC Trap: Article 20 Protection Against Civil/Tax Penalties - Ans: A
  {
    "id": "FR_M_034",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Medium",
    "question_type": "TNPSC Trap",
    "question": {
      "en": "An individual is assessed a retrospective tax penalty for a transaction completed three years ago. Can the individual claim protection under Article 20(1) Ex-Post-Facto Law?",
      "ta": "ஒரு தனிநபருக்கு மூன்று ஆண்டுகளுக்கு முன் முடிந்த பரிவர்த்தனைக்காக முந்தைய தேதியிட்ட வரித் தண்டம் (tax penalty) விதிக்கப்படுகிறது. அத்தனிநபர் உறுப்பு 20(1) முந்தைய தேதியிட்ட சட்டப் பாதுகாப்பைக் கோர முடியுமா?"
    },
    "options": [
      { "id": "A", "en": "No, because Article 20(1) protection applies strictly to criminal convictions and sentences, NOT to civil liabilities or tax penalties.", "ta": "இல்லை, ஏனெனில் உறுப்பு 20(1) பாதுகாப்பு குற்றவியல் தண்டனைகளுக்கு மட்டுமே கண்டிப்பாகப் பொருந்தும், சிவில் பொறுப்புகள் அல்லது வரித் தண்டங்களுக்கு அல்ல." },
      { "id": "B", "en": "Yes, because all penalties retrospective in nature are unconstitutional.", "ta": "ஆம், ஏனெனில் முந்தைய தேதியிட்ட அனைத்துத் தண்டங்களும் அரசியலமைப்புக்கு முரணானவை." },
      { "id": "C", "en": "Yes, provided the tax amount exceeds Rs 1 lakh.", "ta": "ஆம், வரித் தொகை ரூ. 1 லட்சத்திற்கு மேல் இருக்கும் வரை கோரலாம்." },
      { "id": "D", "en": "No, but only if the individual is a foreign citizen.", "ta": "இல்லை, ஆனால் அத்தனிநபர் வெளிநாட்டுக் குடிமகனாக இருந்தால் மட்டுமே." }
    ],
    "correct_answer": "A",
    "explanation": {
      "en": "Hathising Manufacturing Co. v. Union of India: Article 20(1) protects against retrospective CRIMINAL laws. Civil liabilities, tax penalties, or statutory dues can be validly imposed retrospectively.",
      "ta": "உறுப்பு 20(1) முந்தைய தேதியிட்ட குற்றவியல் சட்டங்களுக்கு எதிராக மட்டுமே பாதுகாக்கிறது. சிவில் பொறுப்புகள், வரித் தண்டங்களை முந்தைய தேதியிட்டு செல்லுபடியாகும் வகையில் விதிக்கலாம்."
    },
    "why_not_others": {
      "A": { "en": "Correct. Art 20(1) protection is limited strictly to CRIMINAL convictions.", "ta": "சரி. உறுப்பு 20(1) பாதுகாப்பு குற்றவியல் தண்டனைகளுக்கு மட்டுமே கட்டுப்படுத்தப்பட்டது." },
      "B": { "en": "Incorrect. Retrospective tax penalties are constitutional.", "ta": "தவறு. முந்தைய தேதியிட்ட வரித் தண்டங்கள் செல்லுபடியாகும்." },
      "C": { "en": "Tax amount threshold does not alter Art 20(1) scope.", "ta": "வரித் தொகை வரம்பு உறுப்பு 20(1) எல்லையை மாற்றுவதில்லை." },
      "D": { "en": "Citizens and foreigners have the same Art 20(1) protection for criminal laws.", "ta": "குடிமக்களுக்கும் வெளிநாட்டினருக்கும் குற்றவியல் சட்டங்களில் ஒரே மாதிரியான உறுப்பு 20(1) பாதுகாப்பு உண்டு." }
    },
    "tnpsc_tip": {
      "en": "TRAP: Tax penalties & civil liabilities CAN be imposed retrospectively; criminal offences CANNOT.",
      "ta": "பொறி: வரித் தண்டங்கள் & சிவில் பொறுப்புகளை முந்தைய தேதியிட்டு விதிக்கலாம்; குற்றவியல் குற்றங்களை முடியாது."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Medium", "level": "TNPSC Group 1" }
  },

  # 35. Elimination-Based: Fundamental Rights vs DPSP Case Chronology - Ans: D
  {
    "id": "FR_M_035",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Medium",
    "question_type": "Elimination-Based",
    "question": {
      "en": "Which of the following represents the correct chronological order of landmark judicial decisions concerning the relationship between Fundamental Rights and Directive Principles?",
      "ta": "அடிப்படை உரிமைகள் மற்றும் அரசு நெறிமுறைக் கோட்பாடுகளுக்கு இடையேயான தொடர்பு தொடர்பான முக்கிய நீதித்துறை தீர்ப்புகளின் சரியான காலவரிசை எது?"
    },
    "options": [
      { "id": "A", "en": "Minerva Mills (1980) -> Golak Nath (1967) -> Champakam Dorairajan (1951) -> Kesavananda Bharati (1973)", "ta": "மினர்வா மில்ஸ் (1980) -> கோலக் நாத் (1967) -> செம்பகம் துரைராஜன் (1951) -> கேசவானந்த பாரதி (1973)" },
      { "id": "B", "en": "Kesavananda Bharati (1973) -> Champakam Dorairajan (1951) -> Minerva Mills (1980) -> Golak Nath (1967)", "ta": "கேசவானந்த பாரதி (1973) -> செம்பகம் துரைராஜன் (1951) -> மினர்வா மில்ஸ் (1980) -> கோலக் நாத் (1967)" },
      { "id": "C", "en": "Golak Nath (1967) -> Champakam Dorairajan (1951) -> Kesavananda Bharati (1973) -> Minerva Mills (1980)", "ta": "கோலக் நாத் (1967) -> செம்பகம் துரைராஜன் (1951) -> கேசவானந்த பாரதி (1973) -> மினர்வா மில்ஸ் (1980)" },
      { "id": "D", "en": "Champakam Dorairajan (1951) -> Golak Nath (1967) -> Kesavananda Bharati (1973) -> Minerva Mills (1980)", "ta": "செம்பகம் துரைராஜன் (1951) -> கோலக் நாத் (1967) -> கேசவானந்த பாரதி (1973) -> மினர்வா மில்ஸ் (1980)" }
    ],
    "correct_answer": "D",
    "explanation": {
      "en": "1. Champakam Dorairajan (1951 - FRs superior to DPSP)\n2. Golak Nath (1967 - FRs sacrosanct)\n3. Kesavananda Bharati (1973 - Basic Structure)\n4. Minerva Mills (1980 - Harmonious balance).",
      "ta": "1. செம்பகம் துரைராஜன் (1951 - FRs மேலானது)\n2. கோலக் நாத் (1967 - FRs புனிதமானது)\n3. கேசவானந்த பாரதி (1973 - அடிப்படை கட்டமைப்பு)\n4. மினர்வா மில்ஸ் (1980 - நல்லிணக்கச் சமநிலை)."
    },
    "why_not_others": {
      "A": { "en": "Incorrect order.", "ta": "தவறான வரிசை." },
      "B": { "en": "Incorrect order.", "ta": "தவறான வரிசை." },
      "C": { "en": "Incorrect order.", "ta": "தவறான வரிசை." },
      "D": { "en": "Correct. 1951 -> 1967 -> 1973 -> 1980 is the authentic chronology.", "ta": "சரி. 1951 -> 1967 -> 1973 -> 1980 என்பதே சரியான காலவரிசை." }
    },
    "tnpsc_tip": {
      "en": "Champakam 1951 -> Golak Nath 1967 -> Kesavananda 1973 -> Minerva Mills 1980.",
      "ta": "செம்பகம் 1951 -> கோலக் நாத் 1967 -> கேசவானந்த 1973 -> மினர்வா மில்ஸ் 1980."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Medium", "level": "TNPSC Group 1" }
  },

  # 36. Application / Inference: Article 32 vs Article 226 Territorial Jurisdiction - Ans: B
  {
    "id": "FR_M_036",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Medium",
    "question_type": "Application/Inference",
    "question": {
      "en": "A fundamental right violation occurs in Tamil Nadu against a resident of Tamil Nadu. Can the Madras High Court issue a writ under Article 226 outside Tamil Nadu if the cause of action partly arose elsewhere?",
      "ta": "தமிழ்நாட்டில் தமிழ்நாட்டைச் சேர்ந்த ஒருவருக்கு எதிராக அடிப்படை உரிமை மீறல் ஏற்படுகிறது. நடவடிக்கைக்கான காரணம் (cause of action) பகுதி வேறு இடத்தில் எழுந்திருந்தால் மெட்ராஸ் உயர் நீதிமன்றம் உறுப்பு 226-ன் கீழ் தமிழ்நாட்டிற்கு வெளியே மனு பிறப்பிக்க முடியுமா?"
    },
    "options": [
      { "id": "A", "en": "No, High Courts can never issue writs beyond their state borders under any circumstances.", "ta": "இல்லை, உயர் நீதிமன்றங்கள் எந்தச் சூழ்நிலையிலும் தங்கள் மாநில எல்லைக்கு அப்பால் மனுக்களைப் பிறப்பிக்க முடியாது." },
      { "id": "B", "en": "Yes, under Article 226(2), a High Court can issue writs against an authority located outside its territory if the cause of action arises, wholly or in part, within its territorial jurisdiction.", "ta": "ஆம், உறுப்பு 226(2)-ன் கீழ், நடவடிக்கைக்கான காரணம் முழுமையாகவோ அல்லது பகுதியாகவோ அதன் நிலப்பரப்பு எல்லைக்குள் எழுந்தால், தனது எல்லைக்கு வெளியே உள்ள அதிகார அமைப்புக்கு எதிராகவும் உயர் நீதிமன்றம் மனு பிறப்பிக்கலாம்." },
      { "id": "C", "en": "Yes, but only if the Supreme Court grants a special leave petition first.", "ta": "ஆம், ஆனால் உச்ச நீதிமன்றம் முதலில் சிறப்பு விடுப்பு மனுவை வழங்கினால் மட்டுமே." },
      { "id": "D", "en": "No, only the Supreme Court under Article 32 has territorial jurisdiction outside states.", "ta": "இல்லை, உறுப்பு 32-ன் கீழ் உச்ச நீதிமன்றத்திற்கு மட்டுமே மாநிலங்களுக்கு வெளியே நிலப்பரப்பு எல்லை அதிகாரம் உண்டு." }
    ],
    "correct_answer": "B",
    "explanation": {
      "en": "Article 226(2) (inserted by 15th CAA 1963) empowers High Courts to issue writs to any government or authority located outside its state boundary if the cause of action arose wholly or partly within its territory.",
      "ta": "உறுப்பு 226(2) (15வது திருத்தம் 1963) நடவடிக்கைக்கான காரணம் பகுதி அல்லது முழுமையாகத் தன் எல்லைக்குள் எழுந்தால், மாநிலத்திற்கு வெளியே உள்ள அரசு/அதிகார அமைப்புக்கும் மனு அனுப்ப உயர் நீதிமன்றத்திற்கு அதிகாரமளிக்கிறது."
    },
    "why_not_others": {
      "A": { "en": "Art 226(2) permits extra-territorial writ issuance if cause of action arises in state.", "ta": "காரணம் மாநிலத்தில் எழுந்தால் உறுப்பு 226(2) மாநிலத்திற்கு வெளியே மனு அனுப்புவதை அனுமதிக்கிறது." },
      "B": { "en": "Correct. Cause of action test under Art 226(2).", "ta": "சரி. உறுப்பு 226(2)-ன் கீழ் நடவடிக்கைக் காரணச் சோதனை." },
      "C": { "en": "SC special leave is not required.", "ta": "உச்ச நீதிமன்ற சிறப்பு விடுப்பு தேவையில்லை." },
      "D": { "en": "Art 226(2) gives High Courts extra-territorial writ powers based on cause of action.", "ta": "உறுப்பு 226(2) உயர் நீதிமன்றங்களுக்கும் மாநில எல்லை தாண்டிய மனு அதிகாரத்தை வழங்குகிறது." }
    },
    "tnpsc_tip": {
      "en": "15th CAA 1963 added Art 226(2): Cause of action within state = High Court can issue writ outside state.",
      "ta": "15வது திருத்தம் 1963 உறுப்பு 226(2)-ஐச் சேர்த்தது: மாநிலத்திற்குள் நடவடிக்கைக் காரணம் = மாநிலத்திற்கு வெளியே மனு பிறப்பிக்க உயர் நீதிமன்றத்திற்கு அதிகாரம்."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Medium", "level": "TNPSC Group 1" }
  },

  # 37. Article / Provision Based: Article 21A RTE Constitutional Scheme - Ans: C
  {
    "id": "FR_M_037",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Medium",
    "question_type": "Article/Provision Based",
    "question": {
      "en": "The 86th Constitutional Amendment Act, 2002 made a tripartite change in the Constitution regarding education. Which three Articles were simultaneously added or modified?",
      "ta": "2002-ன் 86வது அரசியலமைப்பு திருத்தச் சட்டம் கல்வி தொடர்பாக அரசியலமைப்பில் முத்தரப்பு மாற்றத்தை செய்தது. எந்த மூன்று உறுப்புகள் ஒரே நேரத்தில் சேர்க்கப்பட்டன அல்லது மாற்றப்பட்டன?"
    },
    "options": [
      { "id": "A", "en": "Articles 14, 19, and 21", "ta": "உறுப்புகள் 14, 19, மற்றும் 21" },
      { "id": "B", "en": "Articles 15, 16, and 29", "ta": "உறுப்புகள் 15, 16, மற்றும் 29" },
      { "id": "C", "en": "Article 21A (added as FR), Article 45 (modified in DPSP), and Article 51A(k) (added as Fundamental Duty)", "ta": "உறுப்பு 21A (FR-ஆக சேர்ப்பு), உறுப்பு 45 (DPSP-ல் மாற்றம்), மற்றும் உறுப்பு 51A(k) (அடிப்படை கடமையாக சேர்ப்பு)" },
      { "id": "D", "en": "Articles 30, 31, and 300A", "ta": "உறுப்புகள் 30, 31, மற்றும் 300A" }
    ],
    "correct_answer": "C",
    "explanation": {
      "en": "The 86th CAA 2002 executed a 3-part educational reform: 1. Inserted Art 21A (FR for 6-14 yrs), 2. Substituted Art 45 (DPSP for 0-6 yrs), 3. Added Art 51A(k) (11th Duty for parents).",
      "ta": "86வது திருத்தம் 2002 3-பகுதி கல்விச் சீர்திருத்தத்தை செய்தது: 1. உறுப்பு 21A சேர்ப்பு (6-14 வயது FR), 2. உறுப்பு 45 மாற்றம் (0-6 வயது DPSP), 3. உறுப்பு 51A(k) சேர்ப்பு (பெற்றோருக்கான 11வது கடமை)."
    },
    "why_not_others": {
      "A": { "en": "Arts 14, 19, 21 is the Golden Triangle, not 86th CAA package.", "ta": "உறுப்புகள் 14, 19, 21 தங்க முக்கோணம், 86வது திருத்தத் தொகுப்பு அல்ல." },
      "B": { "en": "Arts 15, 16, 29 relate to reservations and culture.", "ta": "உறுப்புகள் 15, 16, 29 இடஒதுக்கீடு மற்றும் பண்பாடு பற்றியவை." },
      "C": { "en": "Correct. 86th CAA 2002 affected Art 21A (FR), Art 45 (DPSP), and Art 51A(k) (Duty).", "ta": "சரி. 86வது திருத்தம் 2002 உறுப்பு 21A (FR), உறுப்பு 45 (DPSP), மற்றும் உறுப்பு 51A(k) (கடமை) மூன்றையும் பாதித்தது." },
      "D": { "en": "Art 31 deletion was by 44th CAA 1978.", "ta": "உறுப்பு 31 நீக்கம் 44வது திருத்தம் 1978 மூலம் செய்யப்பட்டது." }
    },
    "tnpsc_tip": {
      "en": "86th CAA 2002 connected Part III (Art 21A), Part IV (Art 45), and Part IV-A (Art 51A(k)).",
      "ta": "86வது திருத்தம் 2002 பகுதி III (21A), பகுதி IV (45), பகுதி IV-A (51A(k)) மூன்றையும் இணைத்தது."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Medium", "level": "TNPSC Group 1" }
  },

  # 38. Case / Amendment Based: S.R. Bommai 1994 Secularism Ruling - Ans: A
  {
    "id": "FR_M_038",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Medium",
    "question_type": "Case / Amendment",
    "question": {
      "en": "In S.R. Bommai v. Union of India (1994), what major constitutional principle regarding religion and state policy was declared to be part of the 'Basic Structure' of the Constitution?",
      "ta": "எஸ்.ஆர். பொம்மை எதிர் இந்திய யூனியன் (1994) வழக்கில், மத சுதந்திரம் மற்றும் அரசுக் கொள்கை தொடர்பான எந்த முக்கிய அரசியலமைப்புக் கோட்பாடு அரசியலமைப்பின் 'அடிப்படை கட்டமைப்பின்' பகுதி என அறிவிக்கப்பட்டது?"
    },
    "options": [
      { "id": "A", "en": "Secularism", "ta": "மதச்சார்பின்மை (Secularism)" },
      { "id": "B", "en": "Right to Property", "ta": "சொத்துரிமை" },
      { "id": "C", "en": "Absolute Freedom of Speech", "ta": "முழுமையான பேச்சு சுதந்திரம்" },
      { "id": "D", "en": "Dual Citizenship", "ta": "இரட்டைக் குடியுரிமை" }
    ],
    "correct_answer": "A",
    "explanation": {
      "en": "In S.R. Bommai (1994), a 9-judge bench ruled that Secularism is a Basic Feature of the Constitution. Any state government pursuing anti-secular policies can be dismissed under Article 356.",
      "ta": "எஸ்.ஆர். பொம்மை வழக்கில் (1994), 9 நீதிபதிகள் அமர்வு மதச்சார்பின்மை அரசியலமைப்பின் அடிப்படை அம்சம் எனத் தீர்ப்பளித்தது. மதச்சார்பற்ற கொள்கைகளுக்கு எதிராகச் செயல்படும் மாநில அரசை உறுப்பு 356-ன் கீழ் பணிநீக்கம் செய்யலாம்."
    },
    "why_not_others": {
      "A": { "en": "Correct. S.R. Bommai (1994) declared Secularism a Basic Structure.", "ta": "சரி. எஸ்.ஆர். பொம்மை (1994) மதச்சார்பின்மையை அடிப்படை கட்டமைப்பாக்கியது." },
      "B": { "en": "Right to Property is NOT part of Basic Structure.", "ta": "சொத்துரிமை அடிப்படை கட்டமைப்பின் பகுதி அல்ல." },
      "C": { "en": "Freedom of Speech is subject to reasonable restrictions.", "ta": "பேச்சு சுதந்திரம் நியாயமான கட்டுப்பாடுகளுக்கு உட்பட்டது." },
      "D": { "en": "India has single citizenship.", "ta": "இந்தியா ஒற்றைக் குடியுரிமையைக் கொண்டுள்ளது." }
    },
    "tnpsc_tip": {
      "en": "S.R. Bommai (1994) = Secularism is part of Basic Structure + SC review of Art 356 proclamations.",
      "ta": "எஸ்.ஆர். பொம்மை (1994) = மதச்சார்பின்மை அடிப்படை கட்டமைப்பு + உறுப்பு 356 பிரகடனங்களின் உச்ச நீதிமன்ற ஆய்வு."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Medium", "level": "TNPSC Group 1" }
  },

  # 39. Conceptual Distinction: Public Order vs Security of State Restrictions - Ans: B
  {
    "id": "FR_M_039",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Medium",
    "question_type": "Conceptual Distinction",
    "question": {
      "en": "In constitutional jurisprudence, how does 'Public Order' differ from 'Security of State' as a restriction ground under Article 19(2)?",
      "ta": "அரசியலமைப்புச் சட்டத்துறையில், உறுப்பு 19(2)-ன் கீழ் உள்ள கட்டுப்பாட்டு அடிப்படையாக 'பொது ஒழுங்கு' (Public Order) என்பது 'அரசின் பாதுகாப்பு' (Security of State) என்பதிலிருந்து எவ்வாறு வேறுபடுகிறது?"
    },
    "options": [
      { "id": "A", "en": "Security of State is narrower than Public Order.", "ta": "அரசின் பாதுகாப்பு என்பது பொது ஒழுங்கை விடக் குறுகியது." },
      { "id": "B", "en": "'Public Order' refers to general tranquility and public peace locally (concentric circle), whereas 'Security of State' refers to grave threats endangering the survival or stability of the State itself (innermost circle).", "ta": "'பொது ஒழுங்கு' என்பது உள்ளூரில் பொது அமைதி மற்றும் அமைதியைக் குறிக்கிறது (வெளிப்புற வட்டம்), அதேவேளையில் 'அரசின் பாதுகாப்பு' என்பது அரசே அழிவதற்கோ அல்லது ஸ்திரத்தன்மைக்கோ ஆபத்தை விளைவிக்கும் தீவிர அச்சுறுத்தல்களைக் குறிக்கிறது (உள் வட்டம்)." },
      { "id": "C", "en": "Public Order applies to armed forces only, while Security of State applies to civilians.", "ta": "பொது ஒழுங்கு ஆயுதப் படைகளுக்கு மட்டுமே பொருந்தும், அரசின் பாதுகாப்பு சிவிலியன்களுக்குப் பொருந்தும்." },
      { "id": "D", "en": "Both terms have identical legal meaning in Indian courts.", "ta": "இரண்டு சொற்களுமே இந்திய நீதிமன்றங்களில் ஒரே மாதிரியான சட்டப் பொருளைக் கொண்டுள்ளன." }
    ],
    "correct_answer": "B",
    "explanation": {
      "en": "Ram Manohar Lohia Case: Law and order is the widest circle, Public Order is the middle circle, and Security of State is the innermost circle representing grave threats like overthrowing the state.",
      "ta": "ராம் மனோகர் லோஹியா வழக்கு: சட்டம் ஒழுங்கு என்பது அகன்ற வட்டம், பொது ஒழுங்கு நடு வட்டம், அரசின் பாதுகாப்பு என்பது அரசைப் renverser செய்யும் தீவிர அச்சுறுத்தல்களைக் குறிக்கும் உள் வட்டம்."
    },
    "why_not_others": {
      "A": { "en": "Reversed. Security of State is a graver, tighter concept than general Public Order.", "ta": "தலைகீழானது. அரசின் பாதுகாப்பு என்பது பொது ஒழுங்கை விடத் தீவிரமான கருத்து." },
      "B": { "en": "Correct. Concentric circles model: Law & Order > Public Order > Security of State.", "ta": "சரி. இணை மைய வட்டங்கள் மாதிரி: சட்டம் ஒழுங்கு > பொது ஒழுங்கு > அரசின் பாதுகாப்பு." },
      "C": { "en": "Both restriction grounds apply to all citizens.", "ta": "இரண்டு கட்டுப்பாட்டு அடிப்படைகளுமே அனைத்துக் குடிமக்களுக்கும் பொருந்தும்." },
      "D": { "en": "Courts clearly distinguish their degree of gravity.", "ta": "நீதிமன்றங்கள் அவற்றின் தீவிரத்தன்மையின் அளவை தெளிவாக வேறுபடுத்துகின்றன." }
    },
    "tnpsc_tip": {
      "en": "Public Order was added to Art 19(2) by the 1st CAA 1951 to cover local public tranquility.",
      "ta": "உள்ளூர் பொது அமைதியை உள்ளடக்க 1வது திருத்தம் 1951 மூலம் உறுப்பு 19(2)-ல் பொது ஒழுங்கு சேர்க்கப்பட்டது."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Medium", "level": "TNPSC Group 1" }
  },

  # 40. Application / Inference: Fundamental Rights Enforceability Against Private Persons - Ans: C
  {
    "id": "FR_M_040",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Medium",
    "question_type": "Application/Inference",
    "question": {
      "en": "Which set of Fundamental Rights are enforceable DIRECTLY against private individuals as well as against the State?",
      "ta": "அரசுக்கு எதிராக மட்டுமன்றித் தனியார் நபர்களுக்கு எதிராகவும் நேரடியாக அமல்படுத்தக்கூடிய அடிப்படை உரிமைகளின் தொகுதி எது?"
    },
    "options": [
      { "id": "A", "en": "Articles 14, 19, and 21", "ta": "உறுப்புகள் 14, 19, மற்றும் 21" },
      { "id": "B", "en": "Articles 15(1), 16(1), and 29(1)", "ta": "உறுப்புகள் 15(1), 16(1), மற்றும் 29(1)" },
      { "id": "C", "en": "Articles 17 (Untouchability), 23 (Forced Labour/Trafficking), and 24 (Child Labour)", "ta": "உறுப்புகள் 17 (தீண்டாமை), 23 (கட்டாய வேலை/மனித வியாபாரம்), மற்றும் 24 (குழந்தை தொழிலாளர்)" },
      { "id": "D", "en": "Articles 25, 26, and 27", "ta": "உறுப்புகள் 25, 26, மற்றும் 27" }
    ],
    "correct_answer": "C",
    "explanation": {
      "en": "Articles 17, 23, and 24 are constitutional prohibitions directed against private individuals as well as the State, creating immediate horizontal applicability (horizontal effect).",
      "ta": "உறுப்புகள் 17, 23 மற்றும் 24 ஆகியவை அரசு மற்றும் தனியார் நபர்களுக்கு எதிராக நேரடியாக அமல்படுத்தக்கூடிய அரசியலமைப்புத் தடைகளாகும் (கிடைமட்டப் பயன்பாடு)."
    },
    "why_not_others": {
      "A": { "en": "Art 14 & 19 operate primarily against State action.", "ta": "உறுப்புகள் 14 & 19 முதன்மையாக அரசு நடவடிக்கைக்கு எதிராகச் செயல்படுகின்றன." },
      "B": { "en": "Art 16(1) is against State employment discrimination.", "ta": "உறுப்பு 16(1) அரசு வேலைவாய்ப்பு பாகுபாட்டிற்கு எதிராக செயல்படுகிறது." },
      "C": { "en": "Correct. Articles 17, 23, and 24 bind private citizens directly.", "ta": "சரி. உறுப்புகள் 17, 23, மற்றும் 24 தனியார் குடிமக்களை நேரடியாகக் கட்டுப்படுத்துகின்றன." },
      "D": { "en": "Arts 25-27 regulate state interference and denominational rights.", "ta": "உறுப்புகள் 25-27 அரசு தலையீடு மற்றும் சமயக் குழு உரிமைகளை ஒழுங்குபடுத்துகின்றன." }
    },
    "tnpsc_tip": {
      "en": "Articles 17, 23, 24 have horizontal applicability (enforceable against private individuals).",
      "ta": "உறுப்புகள் 17, 23, 24 கிடைமட்டப் பயன்பாடு கொண்டவை (தனியார் நபர்களுக்கு எதிராக அமல்படுத்தக்கூடியவை)."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Medium", "level": "TNPSC Group 1" }
  },

  # 41. Case / Amendment Based: Golak Nath 1967 Ruling - Ans: D
  {
    "id": "FR_M_041",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Medium",
    "question_type": "Case / Amendment",
    "question": {
      "en": "In I.C. Golak Nath v. State of Punjab (1967), what controversial ruling did the Supreme Court give regarding Parliament's power to amend Fundamental Rights?",
      "ta": "ஐ.சி. கோலக் நாத் எதிர் பஞ்சாப் மாநிலம் (1967) வழக்கில், அடிப்படை உரிமைகளைத் திருத்தும் நாடாளுமன்ற அதிகாரம் குறித்து உச்ச நீதிமன்றம் என்ன சர்ச்சைக்கூரிய தீர்ப்பை வழங்கியது?"
    },
    "options": [
      { "id": "A", "en": "Parliament can amend Fundamental Rights by a simple majority.", "ta": "நாடாளுமன்றம் சாதாரண பெரும்பான்மையால் அடிப்படை உரிமைகளைத் திருத்த முடியும்." },
      { "id": "B", "en": "Fundamental Rights are subject to Directive Principles in case of conflict.", "ta": "மோதல் ஏற்படும் போது அடிப்படை உரிமைகள் அரசு நெறிமுறைக் கோட்பாடுகளுக்கு உட்பட்டவை." },
      { "id": "C", "en": "Right to Property is part of the Basic Structure.", "ta": "சொத்துரிமை அடிப்படை கட்டமைப்பின் பகுதியாகும்." },
      { "id": "D", "en": "Fundamental Rights are 'transcendental and sacrosanct'; Parliament has NO power under Article 368 to take away or abridge any Fundamental Right.", "ta": "அடிப்படை உரிமைகள் 'உன்னதமானவை மற்றும் புனிதமானவை' (transcendental and sacrosanct); உறுப்பு 368-ன் கீழ் எந்தவொரு அடிப்படை உரிமையையும் பறிக்கவோ குறைக்கவோ நாடாளுமன்றத்திற்கு அதிகாரம் இல்லை." }
    ],
    "correct_answer": "D",
    "explanation": {
      "en": "In Golak Nath (1967), an 11-judge bench (6-5 majority) held that FRs are sacrosanct and Parliament cannot amend Part III under Art 368. This led to the 24th CAA 1971, which was later modified in Kesavananda Bharati 1973.",
      "ta": "கோலக் நாத் வழக்கில் (1967), 11 நீதிபதிகள் அமர்வு (6-5 பெரும்பான்மை) FRs புனிதமானவை என்றும் உறுப்பு 368-ன் கீழ் நாடாளுமன்றம் பகுதி III-ஐத் திருத்த முடியாது என்றும் தீர்ப்பளித்தது. இது 24வது திருத்தம் 1971-க்கு வழிவகுத்தது."
    },
    "why_not_others": {
      "A": { "en": "Simple majority was rejected.", "ta": "சாதாரண பெரும்பான்மை நிராகரிக்கப்பட்டது." },
      "B": { "en": "Golak Nath gave primacy to FRs over DPSPs.", "ta": "கோலக் நாத் DPSPs-ஐ விட FRs-க்கு முதன்மை அளித்தது." },
      "C": { "en": "Basic structure was introduced later in Kesavananda Bharati (1973).", "ta": "அடிப்படை கட்டமைப்பு பின்னர் கேசவானந்த பாரதியில் (1973) அறிமுகப்படுத்தப்பட்டது." },
      "D": { "en": "Correct. Golak Nath 1967 declared FRs transcendental and unamendable.", "ta": "சரி. கோலக் நாத் 1967 FRs-ஐ திருத்த முடியாத உன்னதமானவை என அறிவித்தது." }
    },
    "tnpsc_tip": {
      "en": "Golak Nath (1967) = FRs are transcendental & sacrosanct (Overruled in Kesavananda 1973).",
      "ta": "கோலக் நாத் (1967) = FRs உன்னதமானவை & புனிதமானவை (கேசவானந்த 1973-ல் மாற்றி அமைக்கப்பட்டது)."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Medium", "level": "TNPSC Group 1" }
  },

  # 42. Article / Provision Based: Article 19(1)(g) Trade Restrictions - Ans: B
  {
    "id": "FR_M_042",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Medium",
    "question_type": "Article/Provision Based",
    "question": {
      "en": "Under Article 19(6), the State is constitutionally permitted to create a State Monopoly in any trade, business, industry, or service. Can a citizen challenge a State Monopoly on the ground of violating Article 19(1)(g)?",
      "ta": "உறுப்பு 19(6)-ன் கீழ், எந்தவொரு வர்த்தகம், வணிகம் அல்லது தொழிலில் அரசு ஏகபோகத்தை (State Monopoly) உருவாக்க அரசுக்கு அரசியலமைப்பு ரீதியாக அனுமதியளிக்கப்பட்டுள்ளது. ஒரு குடிமகன் உறுப்பு 19(1)(g)-ஐ மீறுவதாகக் கூறி அரசு ஏகபோகத்தை எதிர்க்க முடியுமா?"
    },
    "options": [
      { "id": "A", "en": "Yes, because State Monopoly is inherently illegal in a free market economy.", "ta": "ஆம், ஏனெனில் சுதந்திர சந்தைப் பொருளாதாரத்தில் அரசு ஏகபோகம் இயல்பிலேயே சட்டவிரோதமானது." },
      { "id": "B", "en": "No, Article 19(6)(ii) expressly empowers the State to create a monopoly in its favor to the complete or partial exclusion of citizens.", "ta": "இல்லை, உறுப்பு 19(6)(ii) குடிமக்களை முழுமையாகவோ அல்லது பகுதியாகவோ விலக்கித் தன் சாதகமாக ஏகபோகத்தை உருவாக்க அரசுக்கு வெளிப்படையாக அதிகாரமளிக்கிறது." },
      { "id": "C", "en": "Yes, provided the citizen obtains prior permission from the Finance Commission.", "ta": "ஆம், குடிமகன் நிதி ஆணையத்திடமிருந்து முன் அனுமதி பெற்றால் எதிர்க்கலாம்." },
      { "id": "D", "en": "No, but only during National Emergency under Article 352.", "ta": "இல்லை, ஆனால் உறுப்பு 352-ன் கீழ் தேசிய அவசரநிலையின் போது மட்டுமே." }
    ],
    "correct_answer": "B",
    "explanation": {
      "en": "Article 19(6)(ii) (inserted by 1st CAA 1951) enables the State to carry on any trade or business to the exclusion of citizens. State Monopoly is constitutionally protected and cannot be questioned for reasonableness.",
      "ta": "உறுப்பு 19(6)(ii) (1வது திருத்தம் 1951) குடிமக்களை விலக்கி அரசு எந்த வர்த்தகத்தையும் நடத்த அதிகாரமளிக்கிறது. அரசு ஏகபோகம் அரசியலமைப்பு ரீதியாகப் பாதுகாக்கப்படுகிறது."
    },
    "why_not_others": {
      "A": { "en": "State monopoly is constitutionally permitted under Art 19(6)(ii).", "ta": "அரசு ஏகபோகம் உறுப்பு 19(6)(ii)-ன் கீழ் அரசியலமைப்பு ரீதியாக அனுமதிக்கப்படுகிறது." },
      "B": { "en": "Correct. Art 19(6)(ii) explicitly authorizes State Monopoly in trade.", "ta": "சரி. உறுப்பு 19(6)(ii) வர்த்தகத்தில் அரசு ஏகபோகத்தை வெளிப்படையாக அதிகாரப்படுத்துகிறது." },
      "C": { "en": "Finance Commission permission is irrelevant.", "ta": "நிதி ஆணைய அனுமதி தொடர்பற்றது." },
      "D": { "en": "State Monopoly is valid during normal times as well.", "ta": "அரசு ஏகபோகம் சாதாரண காலத்திலும் செல்லுபடியாகும்." }
    },
    "tnpsc_tip": {
      "en": "1st CAA 1951 added Art 19(6)(ii) protecting State Monopoly in trade/industry.",
      "ta": "1வது திருத்தம் 1951 வர்த்தகத்தில் அரசு ஏகபோகத்தைப் பாதுகாக்கும் உறுப்பு 19(6)(ii)-ஐச் சேர்த்தது."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Medium", "level": "TNPSC Group 1" }
  },

  # 43. Application / Inference: Preventive Detention Safeguards Breakdown - Ans: C
  {
    "id": "FR_M_043",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Medium",
    "question_type": "Application/Inference",
    "question": {
      "en": "Under Article 22(5), when a person is detained under preventive detention, the detaining authority must communicate the grounds of detention to the detenu. However, under Article 22(6), the authority CAN REFUSE to disclose facts on which ground?",
      "ta": "உறுப்பு 22(5)-ன் கீழ் ஒருவர் தடுப்புக் காவலில் வைக்கப்படும் போது, தடுப்புக் காவல் அதிகாரி காவலுக்கான காரணங்களை அவருக்குத் தெரிவிக்க வேண்டும். இருப்பினும், உறுப்பு 22(6)-ன் கீழ் எந்த அடிப்படையில் உண்மைகளை வெளிப்படுத்த அதிகாரி மறுக்க முடியும்?"
    },
    "options": [
      { "id": "A", "en": "If disclosing facts would increase government administrative expenditure.", "ta": "உண்மைகளை வெளிப்படுத்துவது அரசின் நிர்வாகச் செலவை அதிகரிக்கும் என்றால்." },
      { "id": "B", "en": "If disclosing facts would harm the private reputation of police officers.", "ta": "உண்மைகளை வெளிப்படுத்துவது காவலதிகாரிகளின் தனிப்பட்ட புகழைக் கெடுக்கும் என்றால்." },
      { "id": "C", "en": "If the detaining authority considers disclosure of such facts to be AGAINST PUBLIC INTEREST.", "ta": "அத்தகைய உண்மைகளை வெளிப்படுத்துவது பொது நலனுக்கு எதிரானது (AGAINST PUBLIC INTEREST) எனத் தடுப்புக் காவல் அதிகாரி கருதினால்." },
      { "id": "D", "en": "If the detenu is a foreigner.", "ta": "காவலில் வைக்கப்பட்டவர் வெளிநாட்டவர் என்றால்." }
    ],
    "correct_answer": "C",
    "explanation": {
      "en": "Article 22(6) provides an exception: the detaining authority is not required to disclose facts which such authority considers to be against the public interest to disclose.",
      "ta": "உறுப்பு 22(6) ஒரு விலக்கை வழங்குகிறது: பொது நலனுக்கு எதிரானது எனத் தடுப்புக் காவல் அதிகாரி கருதும் உண்மைகளை வெளிப்படுத்த வேண்டிய கட்டாயமில்லை."
    },
    "why_not_others": {
      "A": { "en": "Administrative expenditure is not a valid ground.", "ta": "நிர்வாகச் செலவு செல்லுபடியாகும் அடிப்படை அல்ல." },
      "B": { "en": "Police reputation is not a valid ground.", "ta": "காவல்துறை புகழ் செல்லுபடியாகும் அடிப்படை அல்ல." },
      "C": { "en": "Correct. Art 22(6) allows non-disclosure of facts on grounds of 'Public Interest'.", "ta": "சரி. உறுப்பு 22(6) 'பொது நலன்' அடிப்படையில் உண்மைகளை வெளிப்படுத்தாமல் இருக்க அனுமதிக்கிறது." },
      "D": { "en": "Applies to both citizens and non-citizens.", "ta": "குடிமக்கள் மற்றும் வெளிநாட்டினர் இருவருக்குமே பொருந்தும்." }
    },
    "tnpsc_tip": {
      "en": "Art 22(5) = Right to know grounds of detention; Art 22(6) = Exception for facts against Public Interest.",
      "ta": "உறுப்பு 22(5) = காவலுக்கான காரணங்களை அறியும் உரிமை; உறுப்பு 22(6) = பொது நலனுக்கு எதிரான உண்மைகளுக்கான விலக்கு."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Medium", "level": "TNPSC Group 1" }
  },

  # 44. Case / Amendment Based: I.R. Coelho 2007 9th Schedule Ruling - Ans: A
  {
    "id": "FR_M_044",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Medium",
    "question_type": "Case / Amendment",
    "question": {
      "en": "In I.R. Coelho v. State of Tamil Nadu (2007), what landmark ruling did the Supreme Court 9-judge bench deliver regarding laws placed in the Ninth Schedule?",
      "ta": "ஐ.ஆர். கொஹெலோ எதிர் தமிழ்நாடு மாநிலம் (2007) வழக்கில், ஒன்பதாவது அட்டவணையில் வைக்கப்பட்டுள்ள சட்டங்கள் குறித்து உச்ச நீதிமன்றத்தின் 9 நீதிபதிகள் அமர்வு என்ன மைல்கல் தீர்ப்பை வழங்கியது?"
    },
    "options": [
      { "id": "A", "en": "Laws included in the Ninth Schedule AFTER April 24, 1973 (date of Kesavananda judgment) are subject to Judicial Review if they violate the Basic Structure or Fundamental Rights.", "ta": "ஏப்ரல் 24, 1973-க்கு (கேசவானந்த தீர்ப்பு நாள்) பிறகு ஒன்பதாவது அட்டவணையில் சேர்க்கப்பட்ட சட்டங்கள் அடிப்படை கட்டமைப்பு அல்லது அடிப்படை உரிமைகளை மீறினால் நீதித்துறை ஆய்வுக்கு உட்பட்டவை." },
      { "id": "B", "en": "All laws in the Ninth Schedule are completely immune from judicial review forever regardless of date.", "ta": "தேதியை பொருட்படுத்தாமல் ஒன்பதாவது அட்டவணையில் உள்ள அனைத்துச் சட்டங்களும் எப்போதும் நீதித்துறை ஆய்விலிருந்து முற்றிலும் விலக்கு பெற்றவை." },
      { "id": "C", "en": "The Ninth Schedule was declared unconstitutional and struck down.", "ta": "ஒன்பதாவது அட்டவணை அரசியலமைப்புக்கு முரணானது என அறிவிக்கப்பட்டு ரத்து செய்யப்பட்டது." },
      { "id": "D", "en": "Only Tamil Nadu land laws are subject to judicial review.", "ta": "தமிழ்நாடு நிலச் சட்டங்கள் மட்டுமே நீதித்துறை ஆய்வுக்கு உட்பட்டவை." }
    ],
    "correct_answer": "A",
    "explanation": {
      "en": "In I.R. Coelho (2007), SC held that Ninth Schedule is not a sanctuary from judicial review. Laws inserted after April 24, 1973 that destroy the Basic Structure will be invalidated.",
      "ta": "ஐ.ஆர். கொஹெலோ (2007) வழக்கில், 9வது அட்டவணை நீதித்துறை ஆய்விலிருந்து தப்பிக்கும் சரணாலயம் அல்ல என SC தீர்ப்பளித்தது. ஏப்ரல் 24, 1973-க்கு பின் சேர்க்கப்பட்ட அடிப்படை கட்டமைப்பைச் சிதைக்கும் சட்டங்கள் ரத்து செய்யப்படும்."
    },
    "why_not_others": {
      "A": { "en": "Correct. I.R. Coelho 2007 fixed April 24, 1973 cut-off date for 9th Schedule judicial review.", "ta": "சரி. ஐ.ஆர். கொஹெலோ 2007 9வது அட்டவணை நீதித்துறை ஆய்வுக்கு ஏப்ரல் 24, 1973-ஐ எல்லைத் தேதியாக நிர்ணயித்தது." },
      "B": { "en": "Immunity was rejected for post-1973 laws.", "ta": "1973-க்கு பிந்தைய சட்டங்களுக்கான விலக்கு நிராகரிக்கப்பட்டது." },
      "C": { "en": "Ninth Schedule was NOT struck down; its absolute immunity was modified.", "ta": "9வது அட்டவணை ரத்து செய்யப்படவில்லை; அதன் பூரண விலக்கு மாற்றியமைக்கப்பட்டது." },
      "D": { "en": "Applies to all laws in the Ninth Schedule across India.", "ta": "இந்தியா முழுவதும் 9வது அட்டவணையில் உள்ள அனைத்துச் சட்டங்களுக்கும் பொருந்தும்." }
    },
    "tnpsc_tip": {
      "en": "I.R. Coelho (2007) = Cut-off date April 24, 1973 for 9th Schedule Judicial Review.",
      "ta": "ஐ.ஆர். கொஹெலோ (2007) = 9வது அட்டவணை நீதித்துறை ஆய்விற்கான எல்லைத் தேதி ஏப்ரல் 24, 1973."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Medium", "level": "TNPSC Group 1" }
  },

  # 45. Conceptual Distinction: Fundamental Rights vs Fundamental Duties - Ans: D
  {
    "id": "FR_M_045",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Medium",
    "question_type": "Conceptual Distinction",
    "question": {
      "en": "How do Fundamental Rights (Part III) and Fundamental Duties (Part IV-A) differ regarding their enforcement mechanism?",
      "ta": "அமலாக்க அமைப்பு தொடர்பாக அடிப்படை உரிமைகள் (பகுதி III) மற்றும் அடிப்படை கடமைகள் (பகுதி IV-A) எவ்வாறு வேறுபடுகின்றன?"
    },
    "options": [
      { "id": "A", "en": "Fundamental Rights are non-justiciable, whereas Fundamental Duties are directly enforceable by writs.", "ta": "அடிப்படை உரிமைகள் நிலைநிறுத்த முடியாதவை, அதேவேளையில் அடிப்படை கடமைகள் மனுக்கள் மூலம் நேரடியாக அமல்படுத்தக்கூடியவை." },
      { "id": "B", "en": "Both Parts III and IV-A are non-justiciable in High Courts.", "ta": "பகுதிகள் III மற்றும் IV-A இரண்டுமே உயர் நீதிமன்றங்களில் நிலைநிறுத்த முடியாதவை." },
      { "id": "C", "en": "Fundamental Duties apply to foreigners, whereas Fundamental Rights apply to citizens only.", "ta": "அடிப்படை கடமைகள் வெளிநாட்டினருக்குப் பொருந்தும், அதேவேளையில் அடிப்படை உரிமைகள் குடிமக்களுக்கு மட்டுமே பொருந்தும்." },
      { "id": "D", "en": "Fundamental Rights are directly justiciable through constitutional writs (Art 32 & 226), whereas Fundamental Duties are non-justiciable directly unless Parliament enacts specific legislation enforcing them.", "ta": "அடிப்படை உரிமைகள் அரசியலமைப்பு மனுக்கள் (உறுப்புகள் 32 & 226) மூலம் நேரடியாக நிலைநிறுத்தக்கூடியவை, அதேவேளையில் நாடாளுமன்றம் அவற்றை அமல்படுத்த குறிப்பிட்ட சட்டத்தை இயற்றினாலன்றி அடிப்படை கடமைகள் நேரடியாக நிலைநிறுத்த முடியாதவை." }
    ],
    "correct_answer": "D",
    "explanation": {
      "en": "Part III rights are directly justiciable via writs under Arts 32 & 226. Part IV-A duties carry no direct judicial enforcement, though Parliament can enact penal statutes to enforce specific duties (Verma Committee 1999).",
      "ta": "பகுதி III உரிமைகள் உறுப்புகள் 32 & 226 மனுக்கள் மூலம் நேரடியாக நிலைநிறுத்தக்கூடியவை. பகுதி IV-A கடமைகள் நேரடியாக நிலைநிறுத்த முடியாது, எனினும் நாடாளுமன்றம் குறிப்பிட்ட சட்டங்களை இயற்றி அமல்படுத்தலாம்."
    },
    "why_not_others": {
      "A": { "en": "Reversed. FRs are justiciable; FDs are non-justiciable directly.", "ta": "தலைகீழானது. FRs நிலைநிறுத்தக்கூடியவை; FDs நேரடியாக நிலைநிறுத்த முடியாதவை." },
      "B": { "en": "Part III is fully justiciable in High Courts under Art 226.", "ta": "பகுதி III உறுப்பு 226-ன் கீழ் உயர் நீதிமன்றங்களில் நிலைநிறுத்தக்கூடியது." },
      "C": { "en": "Fundamental Duties apply ONLY to Citizens of India.", "ta": "அடிப்படை கடமைகள் இந்தியக் குடிமக்களுக்கு மட்டுமே பொருந்தும்." },
      "D": { "en": "Correct. FRs = Directly Justiciable; FDs = Non-justiciable directly (requires Parliamentary law).", "ta": "சரி. FRs = நேரடியாக நிலைநிறுத்தக்கூடியவை; FDs = நேரடியாக நிலைநிறுத்த முடியாதவை (நாடாளுமன்றச் சட்டம் தேவை)." }
    },
    "tnpsc_tip": {
      "en": "Verma Committee (1999) identified legal provisions enforcing specific Fundamental Duties.",
      "ta": "வர்மா குழு (1999) குறிப்பிட்ட அடிப்படை கடமைகளை அமல்படுத்தும் சட்ட விதிகளை அடையாளம் கண்டது."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Medium", "level": "TNPSC Group 1" }
  },

  # 46. Article / Provision Based: Article 19(1)(d) vs Article 21 Freedom of Movement - Ans: B
  {
    "id": "FR_M_046",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Medium",
    "question_type": "Article/Provision Based",
    "question": {
      "en": "How does freedom of movement under Article 19(1)(d) differ from freedom of movement protected under Article 21?",
      "ta": "உறுப்பு 19(1)(d)-ன் கீழ் உள்ள நடமாடும் சுதந்திரம் உறுப்பு 21-ன் கீழ் பாதுகாக்கப்படும் நடமாடும் சுதந்திரத்திலிருந்து எவ்வாறு வேறுபடுகிறது?"
    },
    "options": [
      { "id": "A", "en": "Article 19(1)(d) covers international travel, whereas Article 21 covers domestic travel inside India.", "ta": "உறுப்பு 19(1)(d) சர்வதேசப் பயணத்தை உள்ளடக்குகிறது, அதேவேளையில் உறுப்பு 21 இந்தியாவிற்குள் உள்நாட்டுப் பயணத்தை உள்ளடக்குகிறது." },
      { "id": "B", "en": "Article 19(1)(d) protects the right to move freely THROUGHOUT THE TERRITORY OF INDIA (internal movement), whereas Article 21 protects the right to TRAVEL ABROAD and return to India (external movement).", "ta": "உறுப்பு 19(1)(d) இந்தியா நிலப்பரப்பு முழுவதும் சுதந்திரமாக நடமாடும் உரிமையைப் பாதுகாக்கிறது (உள்நாட்டு நடமாட்டம்), அதேவேளையில் உறுப்பு 21 வெளிநாடு செல்லும் மற்றும் இந்தியா திரும்பும் உரிமையைப் பாதுகாக்கிறது (வெளிநாட்டு நடமாட்டம்)." },
      { "id": "C", "en": "Both Articles cover international travel exclusively.", "ta": "இரண்டு உறுப்புகளுமே சர்வதேசப் பயணத்தை மட்டுமே பிரத்யேகமாக உள்ளடக்குகின்றன." },
      { "id": "D", "en": "Article 19(1)(d) applies to non-citizens only.", "ta": "உறுப்பு 19(1)(d) குடிமக்கள் அல்லாதோருக்கு மட்டுமே பொருந்தும்." }
    ],
    "correct_answer": "B",
    "explanation": {
      "en": "Maneka Gandhi Case (1978): Internal movement within India is protected under Art 19(1)(d). External movement (right to travel abroad and return to India) is an integral aspect of personal liberty under Art 21.",
      "ta": "மேனகா காந்தி வழக்கு (1978): இந்தியாவிற்குள் உள்நாட்டு நடமாட்டம் உறுப்பு 19(1)(d)-ன் கீழ் பாதுகாக்கப்படுகிறது. வெளிநாடு செல்லும் உரிமை உறுப்பு 21-ன் கீழ் தனிநபர் சுதந்திரத்தின் அங்கமாகும்."
    },
    "why_not_others": {
      "A": { "en": "Reversed. Art 19(1)(d) = Internal; Art 21 = External travel abroad.", "ta": "தலைகீழானது. 19(1)(d) = உள்நாட்டு; 21 = வெளிநாட்டுப் பயணம்." },
      "B": { "en": "Correct. Art 19(1)(d) = Internal movement; Art 21 = Right to go abroad (Maneka Gandhi).", "ta": "சரி. 19(1)(d) = உள்நாட்டு நடமாட்டம்; 21 = வெளிநாடு செல்லும் உரிமை (மேனகா காந்தி)." },
      "C": { "en": "Incorrect. Art 19(1)(d) covers internal movement.", "ta": "தவறு. 19(1)(d) உள்நாட்டு நடமாட்டத்தை உள்ளடக்கும்." },
      "D": { "en": "Art 19(1)(d) applies to Citizens ONLY.", "ta": "உறுப்பு 19(1)(d) குடிமக்களுக்கு மட்டுமே பொருந்தும்." }
    },
    "tnpsc_tip": {
      "en": "Internal movement = Art 19(1)(d); External travel abroad = Art 21.",
      "ta": "உள்நாட்டு நடமாட்டம் = உறுப்பு 19(1)(d); வெளிநாட்டுப் பயணம் = உறுப்பு 21."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Medium", "level": "TNPSC Group 1" }
  },

  # 47. TNPSC Trap: Article 17 Untouchability Definition in Constitution - Ans: C
  {
    "id": "FR_M_047",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Medium",
    "question_type": "TNPSC Trap",
    "question": {
      "en": "Where is the term 'Untouchability' defined in the Constitution of India?",
      "ta": "'தீண்டாமை' (Untouchability) என்ற சொல் இந்திய அரசியலமைப்பில் எங்கு வரையறுக்கப்பட்டுள்ளது?"
    },
    "options": [
      { "id": "A", "en": "In Article 17 itself", "ta": "உறுப்பு 17-லேயே" },
      { "id": "B", "en": "In Article 366 (Definitions Clause)", "ta": "உறுப்பு 366-ல் (வரையறைகள் பிரிவு)" },
      { "id": "C", "en": "It is NOT defined anywhere in the Constitution or in the Protection of Civil Rights Act, 1955.", "ta": "இது அரசியலமைப்பில் அல்லது 1955 சிவில் உரிமைகள் பாதுகாப்புச் சட்டத்தில் எங்குமே வரையறுக்கப்படவில்லை." },
      { "id": "D", "en": "In the Preamble of the Constitution", "ta": "அரசியலமைப்பின் முகவுரையில்" }
    ],
    "correct_answer": "C",
    "explanation": {
      "en": "Neither the Constitution nor the Protection of Civil Rights Act 1955 defines 'Untouchability'. Mysore High Court held it refers to social disabilities historically imposed on certain classes by reason of birth.",
      "ta": "அரசியலமைப்போ அல்லது 1955 சிவில் உரிமைகள் பாதுகாப்புச் சட்டமோ 'தீண்டாமை'யை வரையறுக்கவில்லை. மைசூர் உயர் நீதிமன்றம் இது பிறப்பின் காரணமாக சில வகுப்பினர் மீது வரலாற்று ரீதியாக விதிக்கப்பட்ட சமூகத் தடைகளைக் குறிக்கிறது என்றது."
    },
    "why_not_others": {
      "A": { "en": "Article 17 abolishes it, but DOES NOT define it.", "ta": "உறுப்பு 17 அதை ஒழிக்கிறது, ஆனால் வரையறுக்கவில்லை." },
      "B": { "en": "Article 366 does not contain a definition of untouchability.", "ta": "உறுப்பு 366-ல் தீண்டாமை வரையறை இல்லை." },
      "C": { "en": "Correct. 'Untouchability' is NOT defined anywhere in the Constitution or statute.", "ta": "சரி. 'தீண்டாமை' அரசியலமைப்பில் அல்லது சட்டத்தில் எங்குமே வரையறுக்கப்படவில்லை." },
      "D": { "en": "Preamble mentions Equality and Fraternity, not untouchability definition.", "ta": "முகவுரை சமத்துவத்தைக் குறிப்பிடுகிறது, தீண்டாமை வரையறையை அல்ல." }
    },
    "tnpsc_tip": {
      "en": "TRAP: The words 'Untouchability' (Art 17), 'Minority' (Art 30), and 'Martial Law' (Art 34) are NOT defined in the Constitution.",
      "ta": "பொறி: 'தீண்டாமை' (17), 'சிறுபான்மையினர்' (30), மற்றும் 'ராணுவ சட்டம்' (34) ஆகிய சொற்கள் அரசியலமைப்பில் வரையறுக்கப்படவில்லை."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Medium", "level": "TNPSC Group 1" }
  },

  # 48. Application / Inference: Writs Mandamus vs Prohibition Functional Test - Ans: A
  {
    "id": "FR_M_048",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Medium",
    "question_type": "Application/Inference",
    "question": {
      "en": "An administrative officer refuses to issue a statutory license despite the applicant fulfilling all legal requirements. Which writ is appropriate to compel the officer to perform his duty?",
      "ta": "விண்ணப்பதாரர் அனைத்துச் சட்டப்பூர்வத் தேவைகளையும் பூர்த்தி செய்த போதிலும் ஒரு நிர்வாக அதிகாரி சட்டப்பூர்வ உரிமத்தை வழங்க மறுக்கிறார். அதிகாரியைத் தனது கடமையைச் செய்யக் கட்டாயப்படுத்த எந்தப் பேராணை பொருத்தமானது?"
    },
    "options": [
      { "id": "A", "en": "Mandamus", "ta": "செயலுறுத்தும் பேராணை (Mandamus)" },
      { "id": "B", "en": "Prohibition", "ta": "தடைசெய் பேராணை (Prohibition)" },
      { "id": "C", "en": "Quo Warranto", "ta": "தகுதி வினா பேராணை (Quo Warranto)" },
      { "id": "D", "en": "Habeas Corpus", "ta": "ஆட்கொணர்வு பேராணை (Habeas Corpus)" }
    ],
    "correct_answer": "A",
    "explanation": {
      "en": "Mandamus (We Command) is issued to compel a public official to perform a mandatory statutory duty that he has refused or failed to perform.",
      "ta": "அரசு அதிகாரி செய்ய மறுத்த அல்லது செய்யத் தவறிய கட்டாயச் சட்டப்பூர்வக் கடமையைச் செய்யப் பணிப்பதற்குச் செயலுறுத்தும் பேராணை (Mandamus) வழங்கப்படுகிறது."
    },
    "why_not_others": {
      "A": { "en": "Correct. Mandamus compels performance of a positive statutory duty.", "ta": "சரி. Mandamus ஒரு நேர்மறைச் சட்டப்பூர்வக் கடமையைச் செய்யப் பணிக்கிறது." },
      "B": { "en": "Prohibition stops lower courts from exceeding jurisdiction.", "ta": "Prohibition கீழ் நீதிமன்றங்கள் அதிகார வரம்பை மீறுவதைத் தடுக்கிறது." },
      "C": { "en": "Quo Warranto challenges illegal holding of public office.", "ta": "Quo Warranto பொதுப் பதவியைச் சட்டவிரோதமாக வகிப்பதை எதிர்க்கிறது." },
      "D": { "en": "Habeas Corpus releases illegally detained persons.", "ta": "Habeas Corpus சட்டவிரோதமாக அடைத்து வைக்கப்பட்டவரை விடுவிக்கிறது." }
    },
    "tnpsc_tip": {
      "en": "Mandamus = Command to perform mandatory public duty; Applicant must have a legal right.",
      "ta": "Mandamus = கட்டாயப் பொதுக் கடமையைச் செய்யக் கட்டளை; விண்ணப்பதாரருக்குச் சட்ட உரிமை இருக்க வேண்டும்."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Medium", "level": "TNPSC Group 1" }
  },

  # 49. Case / Amendment Based: 44th Amendment 1978 Comprehensive FR Changes - Ans: C
  {
    "id": "FR_M_049",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Medium",
    "question_type": "Case / Amendment",
    "question": {
      "en": "Which of the following complete sets of changes was enacted by the 44th Constitutional Amendment Act, 1978 regarding Fundamental Rights?",
      "ta": "அடிப்படை உரிமைகள் தொடர்பாக 1978-ன் 44வது அரசியலமைப்பு திருத்தச் சட்டத்தால் இயற்றப்பட்ட மாற்றங்களின் முழுமையான தொகுதி எது?"
    },
    "options": [
      { "id": "A", "en": "Added Right to Education, added EWS quota, and deleted Article 17.", "ta": "கல்வி உரிமையைச் சேர்த்தது, EWS ஒதுக்கீட்டைச் சேர்த்தது, உறுப்பு 17-ஐ நீக்கியது." },
      { "id": "B", "en": "Added Cooperative societies, deleted Article 32, and made DPSP superior to FRs.", "ta": "கூட்டுறவு சங்கங்களைச் சேர்த்தது, உறுப்பு 32-ஐ நீக்கியது, DPSP-ஐ FRs-ஐ விட மேலாக்கியது." },
      { "id": "C", "en": "Deleted Right to Property [Arts 19(1)(f) & 31], inserted Art 300A in Part XII, inserted Art 30(1A) for minority property compensation, and protected Arts 20 & 21 from emergency suspension.", "ta": "சொத்துரிமையை நீக்கியது [உறுப்புகள் 19(1)(f) & 31], பகுதி XII-ல் உறுப்பு 300A-ஐச் சேர்த்தது, சிறுபான்மை சொத்து இழப்பீட்டிற்கு உறுப்பு 30(1A)-ஐச் சேர்த்தது, மற்றும் உறுப்புகள் 20 & 21-ஐ அவசரநிலை இடைநிறுத்தத்திலிருந்து பாதுகாத்தது." },
      { "id": "D", "en": "Omitted Article 19 freedoms completely during peacetime.", "ta": "அமைதி காலத்தில் உறுப்பு 19 சுதந்திரங்களை முற்றிலும் நீக்கியது." }
    ],
    "correct_answer": "C",
    "explanation": {
      "en": "The 44th CAA 1978 executed a comprehensive FR package: 1. Deleted Property from FRs (19(1)(f) & 31), 2. Made Property legal right (Art 300A), 3. Added Art 30(1A) compensation, 4. Protected Arts 20 & 21 from Art 359 suspension.",
      "ta": "44வது திருத்தம் 1978 விரிவான மாற்றங்களைச் செய்தது: 1. சொத்துரிமை நீக்கம் (19(1)(f) & 31), 2. சட்டப்பூர்வ உரிமையாக்கம் (300A), 3. சிறுபான்மையினருக்கான 30(1A) இழப்பீடு, 4. உறுப்புகள் 20 & 21 அவசரநிலை பாதுகாப்பு."
    },
    "why_not_others": {
      "A": { "en": "Education was by 86th CAA; EWS was by 103rd CAA.", "ta": "கல்வி 86வது திருத்தம்; EWS 103வது திருத்தம்." },
      "B": { "en": "Cooperatives was by 97th CAA; Art 32 was never deleted.", "ta": "கூட்டுறவு 97வது திருத்தம்; உறுப்பு 32 நீக்கப்படவில்லை." },
      "C": { "en": "Correct. Statement C summarizes the 44th CAA 1978 Fundamental Rights package.", "ta": "சரி. கூற்று C 44வது திருத்தம் 1978-ன் அடிப்படை உரிமை மாற்றங்களைச் சுருக்குகிறது." },
      "D": { "en": "Article 19 freedoms were restored and protected.", "ta": "உறுப்பு 19 சுதந்திரங்கள் சீரமைக்கப்பட்டுப் பாதுகாக்கப்பட்டன." }
    },
    "tnpsc_tip": {
      "en": "44th CAA 1978: Property removed from Part III; Arts 20 & 21 non-suspendable in Emergency.",
      "ta": "44வது திருத்தம் 1978: சொத்துரிமை பகுதி III லிருந்து நீக்கம்; உறுப்புகள் 20 & 21 அவசரநிலையில் இடைநிறுத்த முடியாதவை."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Medium", "level": "TNPSC Group 1" }
  },

  # 50. Elimination-Based: Fundamental Rights & Preamble Philosophy Synthesis - Ans: B
  {
    "id": "FR_M_050",
    "subject": "Polity",
    "topic": "Fundamental Rights",
    "difficulty": "Medium",
    "question_type": "Elimination-Based",
    "question": {
      "en": "Which of the following statements incorrectly pairs a Preamble objective with its corresponding operational Fundamental Right in Part III?",
      "ta": "பின்வரும் கூற்றுகளில் எது முகவுரை இலக்கை பகுதி III-ல் உள்ள அதற்குரிய செயல்பாட்டு அடிப்படை உரிமையுடன் தவறாக இணையாக இணைக்கிறது?"
    },
    "options": [
      { "id": "A", "en": "Equality of status and opportunity ➔ Articles 14 to 18 (Right to Equality)", "ta": "அந்தஸ்து மற்றும் வாய்ப்பு சமத்துவம் ➔ உறுப்புகள் 14 முதல் 18 வரை (சமத்துவ உரிமை)" },
      { "id": "B", "en": "Fraternity assuring dignity of the individual ➔ Article 31 (Right to Property)", "ta": "தனிநபர் கண்ணியத்தை உறுதி செய்யும் சகோதரத்துவம் ➔ உறுப்பு 31 (சொத்துரிமை)" },
      { "id": "C", "en": "Liberty of thought, expression, belief, faith and worship ➔ Articles 19 to 22 & Articles 25 to 28", "ta": "எண்ணம், கருத்து வெளிப்பாடு, நம்பிக்கை, வழிபாட்டு சுதந்திரம் ➔ உறுப்புகள் 19 முதல் 22 & 25 முதல் 28 வரை" },
      { "id": "D", "en": "Social and political justice ➔ Articles 15, 16, 17, and Article 32 remedies", "ta": "சமூக மற்றும் அரசியல் நீதி ➔ உறுப்புகள் 15, 16, 17, மற்றும் உறுப்பு 32 தீர்வுகள்" }
    ],
    "correct_answer": "B",
    "explanation": {
      "en": "Fraternity assuring individual dignity is operationalized primarily through Article 17 (untouchability abolition), Article 21 (dignified life), and Article 23 (prohibition of begar/trafficking), NOT Article 31 (Property).",
      "ta": "தனிநபர் கண்ணியத்தை உறுதி செய்யும் சகோதரத்துவம் முதன்மையாக உறுப்பு 17 (தீண்டாமை ஒழிப்பு), உறுப்பு 21 (கண்ணியமான வாழ்வு) மற்றும் உறுப்பு 23 (வெட்டி வேலை ஒழிப்பு) மூலம் செயல்படுகிறது, உறுப்பு 31 (சொத்துரிமை) மூலம் அல்ல."
    },
    "why_not_others": {
      "A": { "en": "Statement A is correctly paired.", "ta": "கூற்று A சரியாக இணைக்கப்பட்டுள்ளது." },
      "B": { "en": "Correct. Statement B is INCORRECTLY paired (Property does not operationalize individual dignity/fraternity).", "ta": "சரி. கூற்று B தவறாக இணைக்கப்பட்டுள்ளது (சொத்துரிமை தனிநபர் கண்ணியம்/சகோதரத்துவத்தை முதன்மையாகச் செயல்படுத்துவதில்லை)." },
      "C": { "en": "Statement C is correctly paired.", "ta": "கூற்று C சரியாக இணைக்கப்பட்டுள்ளது." },
      "D": { "en": "Statement D is correctly paired.", "ta": "கூற்று D சரியாக இணைக்கப்பட்டுள்ளது." }
    },
    "tnpsc_tip": {
      "en": "Individual Dignity in Preamble is operationalized via Articles 17, 21, and 23.",
      "ta": "முகவுரையில் உள்ள தனிநபர் கண்ணியம் உறுப்புகள் 17, 21, மற்றும் 23 மூலம் செயல்படுகிறது."
    },
    "metadata": { "subject": "Polity", "topic": "Fundamental Rights", "type": "Medium", "level": "TNPSC Group 1" }
  }
]

target_file = "data/questions/polity/fundamental_rights_medium.json"
os.makedirs(os.path.dirname(target_file), exist_ok=True)

with open(target_file, "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"Successfully generated '{target_file}' with exactly {len(questions)} Medium MCQs!")
