# -*- coding: utf-8 -*-
"""
Complete Grand Test Generator (100 Questions)
Topic: Preamble of the Constitution of India
Output: data/questions/polity/preamble_grand_test.json
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

from build_full_100_preamble_gt import make_q
from compile_100_preamble_gt_dataset import questions as q_1_to_25

gt_all_questions = list(q_1_to_25)

# =============================================================================
# BLOCK 2: Questions 26 to 50
# =============================================================================

# Q26 (A) - PYQ Pattern
gt_all_questions.append(make_q(
    26, "Direct PYQ Pattern", "Easy", "A",
    "The grand ideals of 'Liberty, Equality, and Fraternity' enshrined in the Preamble of the Constitution of India were derived from which historical revolution?",
    "இந்திய அரசியலமைப்பின் முகவுரையில் பொறிக்கப்பட்டுள்ள 'சுதந்திரம், சமத்துவம் மற்றும் சகோதரத்துவம்' என்ற உன்னத இலட்சியங்கள் எந்த வரலாற்றுப் புரட்சியிலிருந்து பெறப்பட்டன?",
    [
        {"id": "A", "en": "French Revolution (1789-1799)", "ta": "பிரெஞ்சுப் புரட்சி (1789-1799)"},
        {"id": "B", "en": "Russian Revolution (1917)", "ta": "ரஷ்யப் புரட்சி (1917)"},
        {"id": "C", "en": "American War of Independence (1776)", "ta": "அமெரிக்க சுதந்திரப் போர் (1776)"},
        {"id": "D", "en": "Industrial Revolution in England", "ta": "இங்கிலாந்தின் தொழிற்புரட்சி"}
    ],
    "The ideals of Liberty, Equality, and Fraternity in our Preamble were taken from the French Revolution (1789-1799).",
    "நமது முகவுரையில் உள்ள சுதந்திரம், சமத்துவம் மற்றும் சகோதரத்துவம் ஆகிய இலட்சியங்கள் பிரெஞ்சுப் புரட்சியிலிருந்து (1789-1799) பெறப்பட்டன."
))

# Q27 (B) - TNPSC Trap
gt_all_questions.append(make_q(
    27, "TNPSC Trap", "Hard", "B",
    "Prior to the insertion of the word 'Secular' by the 42nd Amendment in 1976, which articles of the original 1950 Constitution already guaranteed the implicit secular character of India?",
    "1976-ல் 42வது திருத்தத்தின் மூலம் 'மதச்சார்பற்ற' என்ற சொல் சேர்க்கப்படுவதற்கு முன்பே, அசல் 1950 அரசியலமைப்பின் எந்த உறுப்புகள் இந்தியாவின் மறைமுக மதச்சார்பற்ற தன்மையை ஏற்கனவே உத்தரவாதம் செய்திருந்தன?",
    [
        {"id": "A", "en": "Articles 14 to 18", "ta": "உறுப்புகள் 14 முதல் 18 வரை"},
        {"id": "B", "en": "Articles 25 to 28", "ta": "உறுப்புகள் 25 முதல் 28 வரை"},
        {"id": "C", "en": "Articles 36 to 51", "ta": "உறுப்புகள் 36 முதல் 51 வரை"},
        {"id": "D", "en": "Articles 352 to 360", "ta": "உறுப்புகள் 352 முதல் 360 வரை"}
    ],
    "TNPSC Trap Alert: Articles 25 to 28 (Right to Freedom of Religion) were part of the original Constitution since Jan 26, 1950, proving secularism was implicit prior to 1976.",
    "TNPSC பொறி எச்சரிக்கை: உறுப்புகள் 25 முதல் 28 வரை (மத சுதந்திரத்திற்கான உரிமை) ஜனவரி 26, 1950 முதல் அசல் அரசியலமைப்பின் பகுதியாக இருந்தன."
))

# Q28 (C) - Direct MCQ
gt_all_questions.append(make_q(
    28, "Direct MCQ", "Medium", "C",
    "What are the two core features implied by designating India as a 'Republic' in the Preamble?",
    "முகவுரையில் இந்தியாவை ஒரு 'குடியரசு' எனக் குறிப்பிடுவதன் மூலம் உத்தேசிக்கப்படும் இரண்டு முக்கிய அம்சங்கள் எவை?",
    [
        {"id": "A", "en": "Having a Prime Minister as head of state and hereditary monarchy", "ta": "பிரதமரை நாட்டின் தலைவராகக் கொண்டிருப்பதும் பரம்பரை முடியாட்சியும்"},
        {"id": "B", "en": "A central government with complete power over states and no local elections", "ta": "மாநிலங்கள் மீது முழு அதிகாரம் கொண்ட மத்திய அரசும் உள்ளாட்சித் தேர்தல்கள் இல்லாமையும்"},
        {"id": "C", "en": "Political sovereignty vested in the people and an elected Head of State (President) with no privileged class", "ta": "மக்களிடம் உள்ள அரசியல் இறையாண்மை மற்றும் சலுகை பெற்ற வர்க்கம் இல்லாமல் தேர்ந்தெடுக்கப்பட்ட நாட்டின் தலைவர்"},
        {"id": "D", "en": "Membership in Commonwealth and single-party governance", "ta": "காமன்வெல்த்தில் உறுப்பினராக இருப்பதும் ஒரு கட்சி ஆட்சியும்"}
    ],
    "Republic signifies: 1. Political sovereignty in people (elected Head of State), 2. Absence of any privileged class (all public offices open to all).",
    "குடியரசு என்பது: 1. மக்களிடம் உள்ள அரசியல் இறையாண்மை (தேர்ந்தெடுக்கப்பட்ட தலைவர்), 2. சலுகை பெற்ற வர்க்கம் இல்லாமை (அனைத்து பொதுப் பதவிகளும் அனைவருக்கும் திறந்திருப்பது)."
))

# Q29 (D) - Conceptual
gt_all_questions.append(make_q(
    29, "Conceptual MCQ", "Medium", "D",
    "Why did the framers of the Constitution attach fundamental importance to 'Fraternity' in the Preamble?",
    "அரசியலமைப்புச் சிற்பிகள் முகவுரையில் 'சகோதரத்துவத்திற்கு' ஏன் அடிப்படை முக்கியத்துவம் அளித்தனர்?",
    [
        {"id": "A", "en": "To promote industrial growth and export markets", "ta": "தொழில்துறை வளர்ச்சி மற்றும் ஏற்றுமதி சந்தைகளை ஊக்குவிக்க"},
        {"id": "B", "en": "To enforce military conscription for all young citizens", "ta": "அனைத்து இளம் குடிமக்களுக்கும் கட்டாய ராணுவ சேவையை அமல்படுத்த"},
        {"id": "C", "en": "To establish a two-party political system", "ta": "இரு கட்சி அரசியல் முறையை நிறுவ"},
        {"id": "D", "en": "To build a feeling of common brotherhood essential for securing individual dignity and national unity in a diverse country", "ta": "பன்முகத்தன்மை கொண்ட நாட்டில் தனிநபர் கண்ணியத்தையும் தேசிய ஒற்றுமையையும் பாதுகாக்க அத்தியாவசியமான பொதுவான சகோதர உணர்வை உருவாக்க"}
    ],
    "Fraternity promotes common brotherhood to overcome communal, regional, and caste divisions, thereby ensuring individual dignity and national unity.",
    "சகோதரத்துவம் என்பது வகுப்புவாத, பிராந்திய, சாதியப் பிரிவினைகளைக் கடந்து பொதுவான சகோதரத்துவ உணர்வை வளர்த்து தனிநபர் கண்ணியத்தையும் தேசிய ஒற்றுமையையும் உறுதி செய்கிறது."
))

# Q30 (A) - Statement-Based
gt_all_questions.append(make_q(
    30, "Statement-Based", "Hard", "A",
    "Consider the following statements regarding the legal attributes of the Preamble:\n1. It is non-justiciable and cannot be directly enforced in courts of law.\n2. It is neither a source of power to the Legislature nor a prohibition upon legislative powers.\n3. It plays no role whatsoever in the judicial interpretation of ambiguous Articles.\nWhich of the statements given above are CORRECT?",
    "முகவுரையின் சட்டக்கூறுகள் பற்றிய பின்வரும் கூற்றுகளைக் ஆராய்க:\n1. இது நீதிமன்றத்தால் நிலைநிறுத்த முடியாதது மற்றும் நேரடியாக அமல்படுத்த முடியாது.\n2. இது சட்டமன்றத்திற்கு அதிகாரத்தை வழங்கும் மூலமும் அல்ல, சட்டமன்ற அதிகாரங்கள் மீதான தடையுமல்ல.\n3. தெளிவற்ற உறுப்புகளின் நீதித்துறை விளக்கத்தில் இது எந்தப் பங்கையும் வகிக்காது.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எவை சரியானவை?",
    [
        {"id": "A", "en": "1 and 2 only", "ta": "1 மற்றும் 2 மட்டுமே"},
        {"id": "B", "en": "2 and 3 only", "ta": "2 மற்றும் 3 மட்டுமே"},
        {"id": "C", "en": "1 and 3 only", "ta": "1 மற்றும் 3 மட்டுமே"},
        {"id": "D", "en": "1, 2 and 3", "ta": "1, 2 மற்றும் 3"}
    ],
    "Statements 1 and 2 are CORRECT. Statement 3 is INCORRECT because the Preamble IS used as an interpretive compass when constitutional provisions are ambiguous.",
    "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது; ஏனெனில் அரசியலமைப்பு விதிகள் தெளிவற்றதாக இருக்கும்போது முகவுரை விளக்க உதவியாகப் பயன்படுத்தப்படுகிறது."
))

# Q31 (B) - Hard Analytical
gt_all_questions.append(make_q(
    31, "Hard Analytical", "Hard", "B",
    "Can an ordinary statutory law enacted by Parliament be declared ultra vires and void solely on the abstract ground that it violates the Preamble?",
    "நாடாளுமன்றத்தால் இயற்றப்பட்ட சாதாரணச் சட்டம் ஒன்று, முகவுரையை அருவமாக மீறுகிறது என்ற தெளிவற்ற காரணத்திற்காக மட்டுமே செல்லாதது என அறிவிக்கப்பட முடியுமா?",
    [
        {"id": "A", "en": "Yes, because Preamble is superior to all statutory laws and constitutional articles", "ta": "ஆம், ஏனெனில் முகவுரை அனைத்து சட்டங்கள் மற்றும் அரசியலமைப்பு உறுப்புகளை விட மேலானது"},
        {"id": "B", "en": "No, a statutory law must be shown to violate a specific substantive provision of the Constitution or Basic Structure, not Preamble alone in the abstract", "ta": "இல்லை, ஒரு சட்டம் முகவுரையை அருவமாக மீறுகிறது என்று கூற முடியாது; அது அரசியலமைப்பின் குறிப்பிட்ட உறுப்பையோ அல்லது அடிப்படை கட்டமைப்பையோ மீறுகிறது என நிரூபிக்கப்பட வேண்டும்"},
        {"id": "C", "en": "Yes, but only if approved by a two-thirds majority of state assemblies", "ta": "ஆம், ஆனால் மூன்றில் இரண்டு பங்கு மாநில சட்டமன்றங்கள் ஒப்புதல் அளித்தால் மட்டுமே"},
        {"id": "D", "en": "Yes, if recommended by the Finance Commission", "ta": "ஆம், நிதி ஆணையம் பரிந்துரைத்தால் மட்டுமே"}
    ],
    "A statute can be declared void only if it infringes a specific constitutional provision or basic structure, reading that provision in light of the Preamble.",
    "அரசியலமைப்பின் குறிப்பிட்ட உறுப்பையோ அல்லது அடிப்படை கட்டமைப்பையோ மீறினால் மட்டுமே ஒரு சட்டம் செல்லாது என அறிவிக்கப்படும்."
))

# Q32 (A) - Reasoning
gt_all_questions.append(make_q(
    32, "Assertion & Reason", "Hard", "A",
    "Assertion (A): The Constituent Assembly enacted the Preamble LAST, after the rest of the Constitution was already enacted.\nReason (R): The Preamble was taken up last specifically to ensure that it conformed in every detail to the Constitution as approved by the Assembly.",
    "கூற்று (A): அரசியலமைப்பின் மற்ற பகுதிகள் இயற்றப்பட்ட பின்னரே அரசியலமைப்பு நிர்ணய அவையால் இறுதியாக முகவுரை இயற்றப்பட்டது.\nகாரணம் (R): அரசியலமைப்பு அவையால் ஏற்றுக்கொள்ளப்பட்ட அரசியலமைப்பின் அனைத்து விதிகளுடனும் முகவுரை முழுமையாக ஒத்துப்போவதை உறுதி செய்வதற்காகவே அது இறுதியில் எடுத்துக்கொள்ளப்பட்டது.",
    [
        {"id": "A", "en": "Both A and R are true and R is the correct explanation of A", "ta": "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்"},
        {"id": "B", "en": "Both A and R are true but R is NOT the correct explanation of A", "ta": "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல"},
        {"id": "C", "en": "A is true but R is false", "ta": "A சரி, ஆனால் R தவறு"},
        {"id": "D", "en": "A is false but R is true", "ta": "A தவறு, ஆனால் R சரி"}
    ],
    "Both A and R are true, and R is the correct explanation given by Assembly President Dr. Rajendra Prasad on Oct 17, 1949.",
    "A மற்றும் R இரண்டும் சரி, மேலும் அக்டோபர் 17, 1949 அன்று அவைத் தலைவர் டாக்டர் ராஜேந்திர பிரசாத் தெரிவித்த சரியான விளக்கம் இதுவே."
))

# Q33 (C) - Match the Following
gt_all_questions.append(make_q(
    33, "Match the Following", "Medium", "C",
    "Match List I (Five Facets of Liberty in Preamble) with List II (Constitutional Descriptions) and select the correct answer:\n\nList I\nA. Liberty of Thought\nB. Liberty of Expression\nC. Liberty of Faith\nD. Liberty of Worship\n\nList II\n1. Freedom to practice and perform religious rites and rituals\n2. Freedom of inner conviction and holding religious beliefs\n3. Freedom of mind to form opinions and ideas without external control\n4. Freedom to articulate and communicate thoughts through speech and writing",
    "பட்டியல் I-ஐ (முகவுரையில் உள்ள 5 சுதந்திரங்கள்) பட்டியல் II உடன் (அரசியலமைப்பு விளக்கங்கள்) பொருத்தி சரியான பதிலதைத் தேர்ந்தெடுக்கவும்:\n\nபட்டியல் I\nA. எண்ண சுதந்திரம்\nB. கருத்து வெளிப்பாட்டு சுதந்திரம்\nC. பக்தி/நம்பிக்கை சுதந்திரம்\nD. வழிபாட்டு சுதந்திரம்\n\nபட்டியல் II\n1. மதச் சடங்குகள் மற்றும் வழிபாடுகளைச் செய்வதற்கான சுதந்திரம்\n2. உள்மன நம்பிக்கை மற்றும் மதப் பற்றைக் கொண்டிருக்கும் சுதந்திரம்\n3. வெளிப்புறக் கட்டுப்பாடின்றி சிந்தனை மற்றும் கருத்துக்களை உருவாக்கும் சுதந்திரம்\n4. பேச்சு மற்றும் எழுத்து மூலம் எண்ணங்களை வெளிப்படுத்தும் சுதந்திரம்",
    [
        {"id": "A", "en": "A-3, B-1, C-2, D-4", "ta": "A-3, B-1, C-2, D-4"},
        {"id": "B", "en": "A-4, B-3, C-2, D-1", "ta": "A-4, B-3, C-2, D-1"},
        {"id": "C", "en": "A-3, B-4, C-2, D-1", "ta": "A-3, B-4, C-2, D-1"},
        {"id": "D", "en": "A-2, B-4, C-3, D-1", "ta": "A-2, B-4, C-3, D-1"}
    ],
    "Correct Match: A-3 (Thought = forming mind opinions), B-4 (Expression = articulating through speech/writing), C-2 (Faith = inner conviction), D-1 (Worship = performing religious rites).",
    "சரியான பொருத்தம்: A-3 (எண்ணம் = சிந்தனை உருவாக்கம்), B-4 (கருத்து வெளிப்பாடு = பேச்சு/எழுத்து), C-2 (பக்தி = உள்மன நம்பிக்கை), D-1 (வழிபாடு = மதச் சடங்குகள்)."
))

# Q34 (D) - Chronology
gt_all_questions.append(make_q(
    34, "Chronology", "Easy", "D",
    "Arrange the five attributes describing the Nature of the Indian State in the exact order in which they appear in the present Preamble:\n1. Secular\n2. Sovereign\n3. Republic\n4. Socialist\n5. Democratic",
    "தற்போதைய முகவுரையில் தோன்றும் அதே வரிசையில் இந்திய அரசின் தன்மையை விவரிக்கும் ஐந்து சொற்களை வரிசைப்படுத்தவும்:\n1. மதச்சார்பற்ற\n2. இறையாண்மை\n3. குடியரசு\n4. சமதர்ம\n5. ஜனநாயக",
    [
        {"id": "A", "en": "2 -> 1 -> 4 -> 5 -> 3", "ta": "2 -> 1 -> 4 -> 5 -> 3"},
        {"id": "B", "en": "4 -> 1 -> 2 -> 5 -> 3", "ta": "4 -> 1 -> 2 -> 5 -> 3"},
        {"id": "C", "en": "2 -> 4 -> 5 -> 1 -> 3", "ta": "2 -> 4 -> 5 -> 1 -> 3"},
        {"id": "D", "en": "2 -> 4 -> 1 -> 5 -> 3", "ta": "2 -> 4 -> 1 -> 5 -> 3"}
    ],
    "Correct Textual Sequence in Preamble: 2 (Sovereign) -> 4 (Socialist) -> 1 (Secular) -> 5 (Democratic) -> 3 (Republic).",
    "முகவுரையில் உள்ள சரியான உரை வரிசை: 2 (இறையாண்மை) -> 4 (சமதர்ம) -> 1 (மதச்சார்பற்ற) -> 5 (ஜனநாயக) -> 3 (குடியரசு)."
))

# Q35 (A) - PYQ Pattern
gt_all_questions.append(make_q(
    35, "Direct PYQ Pattern", "Easy", "A",
    "The ideal of 'Justice - Social, Economic and Political' in the Preamble of the Constitution of India was inspired by which historic international revolution?",
    "இந்திய அரசியலமைப்பின் முகவுரையில் உள்ள 'நீதி - சமூக, பொருளாதார மற்றும் அரசியல்' என்ற இலட்சியம் எந்த வரலாற்றுச் சிறப்புமிக்க சர்வதேசப் புரட்சியிலிருந்து ஈர்க்கப்பட்டது?",
    [
        {"id": "A", "en": "Russian Revolution (1917)", "ta": "ரஷ்யப் புரட்சி (1917)"},
        {"id": "B", "en": "French Revolution (1789)", "ta": "பிரெஞ்சுப் புரட்சி (1789)"},
        {"id": "C", "en": "American Revolution (1776)", "ta": "அமெரிக்கப் புரட்சி (1776)"},
        {"id": "D", "en": "Chinese Revolution (1949)", "ta": "சீனப் புரட்சி (1949)"}
    ],
    "The ideal of Justice (social, economic, and political) in our Preamble was borrowed from the Russian Revolution of 1917.",
    "நமது முகவுரையில் உள்ள நீதி (சமூக, பொருளாதார, அரசியல்) என்ற இலட்சியம் 1917 ஆம் ஆண்டின் ரஷ்யப் புரட்சியிலிருந்து பெறப்பட்டது."
))

# Q36 (B) - TNPSC Trap
gt_all_questions.append(make_q(
    36, "TNPSC Trap", "Hard", "B",
    "Did the Constitution of India in 1950 restrict voting rights to property owners and literate taxpayers prior to introducing universal adult franchise?",
    "இந்திய அரசியலமைப்பு 1950-ல் வயதுவந்தோர் வாக்குரிமையை அறிமுகப்படுத்துவதற்கு முன்பு சொத்து உரிமையாளர்கள் மற்றும் கல்வி கற்ற வரி செலுத்துவோருக்கு வாக்குரிமையைக் கட்டுப்படுத்தியதா?",
    [
        {"id": "A", "en": "Yes, property qualifications were mandatory until the 61st Amendment in 1988", "ta": "ஆம், 1988-ல் 61வது திருத்தம் வரும் வரை சொத்துத் தகுதிகள் கட்டாயமாக இருந்தன"},
        {"id": "B", "en": "No, Article 326 established Universal Adult Franchise immediately from Jan 26, 1950 without any property, tax, or educational qualification", "ta": "இல்லை, உறுப்பு 326 எந்தவொரு சொத்து, வரி அல்லது கல்வித் தகுதியும் இன்றி ஜனவரி 26, 1950 முதலே உடனடியாக வயதுவந்தோர் வாக்குரிமையை நிறுவியது"},
        {"id": "C", "en": "Yes, only university graduates were allowed to vote in the 1st General Election (1951-52)", "ta": "ஆம், 1st பொதுத் தேர்தலில் (1951-52) பல்கலைக்கழக பட்டதாரிகள் மட்டுமே வாக்களிக்க அனுமதிக்கப்பட்டனர்"},
        {"id": "D", "en": "Voting rights were extended only to military personnel initially", "ta": "வாக்குரிமை ஆரம்பத்தில் ராணுவ வீரர்களுக்கு மட்டுமே வழங்கப்பட்டது"}
    ],
    "TNPSC Trap Alert: Unlike the 1935 Act (which gave only 14% voting rights), the 1950 Constitution established Universal Adult Franchise immediately under Article 326.",
    "TNPSC பொறி எச்சரிக்கை: 1935 சட்டத்தைப் போலல்லாமல், 1950 அரசியலமைப்பு உறுப்பு 326-ன் கீழ் உடனடியாக வயதுவந்தோர் அனைவருக்கும் வாக்குரிமை தந்தது."
))

# Q37 (C) - Direct MCQ
gt_all_questions.append(make_q(
    37, "Direct MCQ", "Easy", "C",
    "Which Committee recommended the inclusion of Fundamental Duties and changes to the Preamble in 1976?",
    "1976 இல் அடிப்படை கடமைகளைச் சேர்க்கவும் முகவுரையில் மாற்றங்களைச் செய்யவும் பரிந்துரைத்த குழு எது?",
    [
        {"id": "A", "en": "Verma Committee", "ta": "வர்மா குழு"},
        {"id": "B", "en": "Kothari Commission", "ta": "கோத்தாரி ஆணையம்"},
        {"id": "C", "en": "Sardar Swaran Singh Committee", "ta": "சர்தார் சுரன் சிங் குழு"},
        {"id": "D", "en": "M.N. Venkatachaliah Commission", "ta": "எம்.என். வெங்கடாசலையா ஆணையம்"}
    ],
    "The Sardar Swaran Singh Committee (1976) recommended the insertion of Fundamental Duties (Part IV-A) and changes to the Preamble.",
    "சர்தார் சுரன் சிங் குழு (1976) அடிப்படை கடமைகளைச் சேர்க்கவும் முகவுரையில் மாற்றங்கள் செய்யவும் பரிந்துரைத்தது."
))

# Q38 (D) - Conceptual
gt_all_questions.append(make_q(
    38, "Conceptual MCQ", "Hard", "D",
    "How does the Preamble interact with the 'Basic Structure Doctrine' established in the Kesavananda Bharati case?",
    "கேசவானந்த பாரதி வழக்கில் நிறுவப்பட்ட 'அடிப்படை கட்டமைப்பு கோட்பாற்றுடன்' முகவுரை எவ்வாறு தொடர்பு கொள்கிறது?",
    [
        {"id": "A", "en": "Preamble is completely separate and has no overlap with Basic Structure", "ta": "முகவுரை முற்றிலும் தனித்துவமானது, அடிப்படை கட்டமைப்புடன் தொடர்பு இல்லை"},
        {"id": "B", "en": "Preamble allows Parliament to repeal any Basic Structure feature by two-thirds majority", "ta": "மூன்றில் இரண்டு பங்கு பெரும்பான்மையால் எந்தவொரு அடிப்படை கட்டமைப்பையும் ரத்து செய்ய நாடாளுமன்றத்திற்கு முகவுரை அனுமதியளிக்கிறது"},
        {"id": "C", "en": "Preamble can be erased completely under Article 368", "ta": "உறுப்பு 368-ன் கீழ் முகவுரையை முற்றிலும் அழிக்க முடியும்"},
        {"id": "D", "en": "Preamble contains core elements (Sovereignty, Secularism, Democracy, Republic, Justice) that form integral components of the inviolable Basic Structure", "ta": "முகவுரையானது மீற முடியாத அடிப்படை கட்டமைப்பின் ஒருங்கிணைந்த கூறுகளாக அமையும் முக்கிய அம்சங்களை (இறையாண்மை, மதச்சார்பின்மை, ஜனநாயகம், குடியரசு, நீதி) தன்னுள் கொண்டுள்ளது"}
    ],
    "The Supreme Court held that the noble vision and key attributes enshrined in the Preamble constitute fundamental pillars of the Basic Structure.",
    "முகவுரையில் பொறிக்கப்பட்டுள்ள உன்னத நோக்கங்கள் மற்றும் முக்கிய அம்சங்கள் அடிப்படை கட்டமைப்பின் முக்கிய தூண்களாக அமைகின்றன என்று உச்ச நீதிமன்றம் கூறியது."
))

# Q39 (A) - Statement-Based
gt_all_questions.append(make_q(
    39, "Statement-Based", "Medium", "A",
    "Consider the following statements regarding 'Equality' as secured in the Preamble:\n1. It embraces civic equality, political equality, and economic equality.\n2. Fundamental Rights Articles 14 to 18 ensure civic equality.\n3. Article 325 and Article 326 ensure political equality.\nWhich of the statements given above are CORRECT?",
    "முகவுரையில் உறுதிசெய்யப்பட்ட 'சமத்துவம்' பற்றிய பின்வரும் கூற்றுகளைக் ஆராய்க:\n1. இது சிவில் சமத்துவம், அரசியல் சமத்துவம் மற்றும் பொருளாதார சமத்துவத்தை உள்ளடக்கியது.\n2. அடிப்படை உரிமைகள் உறுப்புகள் 14 முதல் 18 வரை சிவில் சமத்துவத்தை உறுதி செய்கின்றன.\n3. உறுப்பு 325 மற்றும் உறுப்பு 326 அரசியல் சமத்துவத்தை உறுதி செய்கின்றன.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எவை சரியானவை?",
    [
        {"id": "A", "en": "1, 2 and 3", "ta": "1, 2 மற்றும் 3"},
        {"id": "B", "en": "1 and 2 only", "ta": "1 மற்றும் 2 மட்டுமே"},
        {"id": "C", "en": "2 and 3 only", "ta": "2 மற்றும் 3 மட்டுமே"},
        {"id": "D", "en": "1 and 3 only", "ta": "1 மற்றும் 3 மட்டுமே"}
    ],
    "All three statements are CORRECT. Equality in Preamble encompasses civic equality (Arts 14-18), political equality (Arts 325 & 326), and economic equality (Art 39 DPSP).",
    "மூன்று கூற்றுகளும் சரியானவை. முகவுரையில் உள்ள சமத்துவம் சிவில், அரசியல் மற்றும் பொருளாதார சமத்துவத்தை உள்ளடக்கியது."
))

# Q40 (B) - Hard Analytical
gt_all_questions.append(make_q(
    40, "Hard Analytical", "Hard", "B",
    "In In re Berubari Union Reference (1960), why did the Supreme Court hold that ceding Indian territory to Pakistan could NOT be done under Article 3?",
    "பெருபாரி யூனியன் வழக்கில் (1960), இந்திய நிலப்பரப்பை பாகிஸ்தானுக்கு விட்டுக்கொடுப்பதை உறுப்பு 3-ன் கீழ் செய்ய முடியாது என்று உச்ச நீதிமன்றம் ஏன் தீர்ப்பளித்தது?",
    [
        {"id": "A", "en": "Because Article 3 applies only to Union Territories and not States", "ta": "ஏனெனில் உறுப்பு 3 யூனியன் பிரதேசங்களுக்கு மட்டுமே பொருந்தும், மாநிலங்களுக்கு அல்ல"},
        {"id": "B", "en": "Because Article 3 deals with internal re-organisation of Indian states and does not cover ceding Indian territory to a foreign nation, which requires an amendment under Article 368", "ta": "ஏனெனில் உறுப்பு 3 இந்திய மாநிலங்களின் உள்நாட்டு மறுசீரமைப்பைப் பற்றியது; வெளிநாட்டுக்கு நிலத்தை விட்டுக் கொடுப்பதை அது உள்ளடக்காது, அதற்கு உறுப்பு 368-ன் கீழ் திருத்தம் தேவை"},
        {"id": "C", "en": "Because the Preamble explicitly forbids foreign treaties", "ta": "ஏனெனில் முகவுரை வெளிநாட்டு ஒப்பந்தங்களை வெளிப்படையாகத் தடை செய்கிறது"},
        {"id": "D", "en": "Because Parliament has no authority over border territories", "ta": "ஏனெனில் எல்லைப் பகுதிகள் மீது நாடாளுமன்றத்திற்கு எந்த அதிகாரமும் இல்லை"}
    ],
    "The Supreme Court held that Parliament's power to diminish state areas under Article 3 does not extend to ceding territory to a foreign country.",
    "மாநிலப் பகுதிகளைக் குறைக்கும் உறுப்பு 3-ன் கீழான நாடாளுமன்றத்தின் அதிகாரம் வெளிநாட்டுக்கு நிலத்தை விட்டுக் கொடுப்பதை உள்ளடக்காது என்று உச்ச நீதிமன்றம் கூறியது."
))

# Q41 (C) - Reasoning
gt_all_questions.append(make_q(
    41, "Assertion & Reason", "Hard", "C",
    "Assertion (A): Parliament cannot use its constituent amending power under Article 368 to completely abrogate the secular character of the Indian Constitution.\nReason (R): In Kesavananda Bharati (1973) and S.R. Bommai (1994), the Supreme Court held that Secularism is a part of the unamendable Basic Structure.",
    "கூற்று (A): இந்திய அரசியலமைப்பின் மதச்சார்பற்ற தன்மையை முற்றிலும் ரத்து செய்ய நாடாளுமன்றம் உறுப்பு 368-ன் கீழ் தனது திருத்தும் அதிகாரத்தைப் பயன்படுத்த முடியாது.\nகாரணம் (R): கேசவானந்த பாரதி (1973) மற்றும் எஸ்.ஆர். பொம்மை (1994) வழக்குகளில், மதச்சார்பின்மை என்பது திருத்தப்பட முடியாத அடிப்படை கட்டமைப்பின் ஒரு பகுதி என்று உச்ச நீதிமன்றம் கூறியது.",
    [
        {"id": "A", "en": "Both A and R are true and R is NOT the correct explanation of A", "ta": "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல"},
        {"id": "B", "en": "A is false but R is true", "ta": "A தவறு, ஆனால் R சரி"},
        {"id": "C", "en": "Both A and R are true and R is the correct explanation of A", "ta": "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்"},
        {"id": "D", "en": "A is true but R is false", "ta": "A சரி, ஆனால் R தவறு"}
    ],
    "Both A and R are true, and R correctly explains A. Secularism is a Basic Feature of the Constitution and cannot be destroyed by any constitutional amendment.",
    "A மற்றும் R இரண்டும் சரி, R என்பது A விற்கு சரியான விளக்கமாகும். மதச்சார்பின்மை அடிப்படை அம்சம் என்பதால் திருத்தத்தால் அழிக்க முடியாது."
))

# Q42 (D) - Match the Following
gt_all_questions.append(make_q(
    42, "Match the Following", "Hard", "D",
    "Match List I (Landmark Judicial Cases) with List II (Core Constitutional Rulings on Preamble):\n\nList I\nA. Berubari Union Case (1960)\nB. Kesavananda Bharati Case (1973)\nC. S.R. Bommai Case (1994)\nD. LIC of India Case (1995)\n\nList II\n1. Re-affirmed Preamble is an integral part of the Constitution\n2. Secularism is a part of the Basic Structure of the Constitution\n3. Preamble is NOT a part of the Constitution\n4. Preamble IS a part of the Constitution and subject to Basic Structure limitation",
    "பட்டியல் I-ஐ (மைல்கல் வழக்குகள்) பட்டியல் II உடன் (முகவுரை பற்றிய முக்கிய தீர்ப்புகள்) பொருத்தி சரியான பதிலதைத் தேர்ந்தெடுக்கவும்:\n\nபட்டியல் I\nA. பெருபாரி யூனியன் வழக்கு (1960)\nB. கேசவானந்த பாரதி வழக்கு (1973)\nC. எஸ்.ஆர். பொம்மை வழக்கு (1994)\nD. எல்.ஐ.சி வழக்கு (1995)\n\nபட்டியல் II\n1. முகவுரை அரசியலமைப்பின் ஒரு ஒருங்கிணைந்த பகுதி என்பதை மீண்டும் உறுதிப்படுத்தியது\n2. மதச்சார்பின்மை அரசியலமைப்பின் அடிப்படை கட்டமைப்பின் ஒரு பகுதியாகும்\n3. முகவுரை அரசியலமைப்பின் ஒரு பகுதி அல்ல\n4. முகவுரை அரசியலமைப்பின் ஒரு பகுதி தான் மற்றும் அடிப்படை கட்டமைப்பு வரம்பிற்கு உட்பட்டது",
    [
        {"id": "A", "en": "A-1, B-4, C-2, D-3", "ta": "A-1, B-4, C-2, D-3"},
        {"id": "B", "en": "A-3, B-2, C-4, D-1", "ta": "A-3, B-2, C-4, D-1"},
        {"id": "C", "en": "A-3, B-4, C-1, D-2", "ta": "A-3, B-4, C-1, D-2"},
        {"id": "D", "en": "A-3, B-4, C-2, D-1", "ta": "A-3, B-4, C-2, D-1"}
    ],
    "Correct Match: A-3 (Berubari = NOT part), B-4 (Kesavananda = IS part & Basic Structure), C-2 (Bommai = Secularism Basic Structure), D-1 (LIC = Integral part).",
    "சரியான பொருத்தம்: A-3 (பெருபாரி = பகுதி அல்ல), B-4 (கேசவானந்தா = பகுதி தான்), C-2 (பொம்மை = மதச்சார்பின்மை அடிப்படை கட்டமைப்பு), D-1 (LIC = ஒருங்கிணைந்த பகுதி)."
))

# Q43 (A) - Chronology
gt_all_questions.append(make_q(
    43, "Chronology", "Medium", "A",
    "Arrange the following Constitutional Amendment Acts in correct chronological order of their enactment:\n1. 1st Constitutional Amendment Act\n2. 24th Constitutional Amendment Act\n3. 42nd Constitutional Amendment Act\n4. 44th Constitutional Amendment Act",
    "பின்வரும் அரசியலமைப்புத் திருத்தச் சட்டங்களை அவை இயற்றப்பட்ட சரியான காலவரிசையில் அமைக்கவும்:\n1. 1வது அரசியலமைப்புத் திருத்தச் சட்டம்\n2. 24வது அரசியலமைப்புத் திருத்தச் சட்டம்\n3. 42வது அரசியலமைப்புத் திருத்தச் சட்டம்\n4. 44வது அரசியலமைப்புத் திருத்தச் சட்டம்",
    [
        {"id": "A", "en": "1 -> 2 -> 3 -> 4", "ta": "1 -> 2 -> 3 -> 4"},
        {"id": "B", "en": "2 -> 1 -> 3 -> 4", "ta": "2 -> 1 -> 3 -> 4"},
        {"id": "C", "en": "1 -> 3 -> 2 -> 4", "ta": "1 -> 3 -> 2 -> 4"},
        {"id": "D", "en": "1 -> 2 -> 4 -> 3", "ta": "1 -> 2 -> 4 -> 3"}
    ],
    "Chronological Sequence: 1 (1st CAA: 1951) -> 2 (24th CAA: 1971) -> 3 (42nd CAA: 1976) -> 4 (44th CAA: 1978).",
    "காலவரிசை: 1 (1வது திருத்தம்: 1951) -> 2 (24வது திருத்தம்: 1971) -> 3 (42வது திருத்தம்: 1976) -> 4 (44வது திருத்தம்: 1978)."
))

# Q44 (B) - PYQ Pattern
gt_all_questions.append(make_q(
    44, "Direct PYQ Pattern", "Easy", "B",
    "Who among the following described the Preamble of the Constitution of India as the 'Horoscope of our Sovereign Democratic Republic'?",
    "இந்திய அரசியலமைப்பின் முகவுரையை 'நமது இறையாண்மை கொண்ட ஜனநாயக குடியரசின் ஜாதகம்' என்று வர்ணித்தவர் யார்?",
    [
        {"id": "A", "en": "Dr. B.R. Ambedkar", "ta": "டாக்டர் பி.ஆர். அம்பேத்கர்"},
        {"id": "B", "en": "Dr. K.M. Munshi", "ta": "டாக்டர் கே.எம். முன்ஷி"},
        {"id": "C", "en": "Pandit Jawaharlal Nehru", "ta": "பண்டிட் ஜவஹர்லால் நேரு"},
        {"id": "D", "en": "Sardar Vallabhbhai Patel", "ta": "சர்தார் வல்லபாய் படேல்"}
    ],
    "Dr. K.M. Munshi, a member of the Drafting Committee, described the Preamble as the Horoscope of our Sovereign Democratic Republic.",
    "வரைவுக் குழு உறுப்பினரான டாக்டர் கே.எம். முன்ஷி முகவுரையை நமது இறையாண்மை கொண்ட ஜனநாயக குடியரசின் ஜாதகம் என்று வர்ணித்தார்."
))

# Q45 (C) - TNPSC Trap
gt_all_questions.append(make_q(
    45, "TNPSC Trap", "Hard", "C",
    "Which exact phrase in the Preamble was substituted by the 42nd Constitutional Amendment Act, 1976 to insert the word 'Integrity'?",
    "1976-ன் 42வது திருத்தச் சட்டத்தின் மூலம் 'ஒருமைப்பாடு' என்ற சொல்லைச் சேர்க்க முகவுரையில் இருந்த எந்தத் தொடர் மாற்றப்பட்டது?",
    [
        {"id": "A", "en": "'Sovereignty of India'", "ta": "'இந்தியாவின் இறையாண்மை'"},
        {"id": "B", "en": "'Fraternity of citizens'", "ta": "'குடிமக்களின் சகோதரத்துவம்'"},
        {"id": "C", "en": "'Unity of the Nation'", "ta": "'நாட்டின் ஒற்றுமை'"},
        {"id": "D", "en": "'Security of State'", "ta": "'மாநிலத்தின் பாதுகாப்பு'"}
    ],
    "TNPSC Trap Alert: The phrase 'Unity of the Nation' was replaced by 'Unity and Integrity of the Nation' in 1976.",
    "TNPSC பொறி எச்சரிக்கை: 'நாட்டின் ஒற்றுமை' என்ற தொடர் 1976 இல் 'நாட்டின் ஒற்றுமை மற்றும் ஒருமைப்பாடு' என மாற்றப்பட்டது."
))

# Q46 (D) - Direct MCQ
gt_all_questions.append(make_q(
    46, "Direct MCQ", "Medium", "D",
    "Who was the President of India who gave presidential assent to the 42nd Constitutional Amendment Act of 1976?",
    "1976 ஆம் ஆண்டின் 42வது அரசியலமைப்புத் திருத்தச் சட்டத்திற்கு ஒப்புதல் அளித்த இந்தியக் குடியரசுத் தலைவர் யார்?",
    [
        {"id": "A", "en": "Dr. S. Radhakrishnan", "ta": "டாக்டர் எஸ். ராதாகிருஷ்ணன்"},
        {"id": "B", "en": "Neelam Sanjiva Reddy", "ta": "நீலம் சஞ்சீவ ரெட்டி"},
        {"id": "C", "en": "V.V. Giri", "ta": "வி.வி. கிரி"},
        {"id": "D", "en": "Fakhruddin Ali Ahmed", "ta": "பக்ருதீன் அலி அகமது"}
    ],
    "President Fakhruddin Ali Ahmed gave assent to the 42nd Constitutional Amendment Act on December 18, 1976.",
    "குடியரசுத் தலைவர் பக்ருதீன் அலி அகமது டிசம்பர் 18, 1976 அன்று 42வது திருத்தச் சட்டத்திற்கு ஒப்புதல் அளித்தார்."
))

# Q47 (A) - Conceptual
gt_all_questions.append(make_q(
    47, "Conceptual MCQ", "Medium", "A",
    "What does the term 'Sovereign' in the Preamble signify regarding India's status in international law?",
    "சர்வதேச சட்டத்தில் இந்தியாவின் அந்தஸ்து தொடர்பாக முகவுரையில் உள்ள 'இறையாண்மை' என்ற சொல் எதனைக் குறிக்கிறது?",
    [
        {"id": "A", "en": "India is an independent state, neither a dominion nor a dependency of any foreign power, capable of conducting its own internal & external affairs", "ta": "இந்தியா எந்தவொரு வெளிநாட்டின் ஆதிக்கத்திலோ சார்பிலோ இல்லாத ஒரு சுயாதீனமான அரசு; தன் உள்நாட்டு, வெளிநாட்டு விவகாரங்களை தானே நடத்தும் திறன் கொண்டது"},
        {"id": "B", "en": "India is bound to seek approval from the British Parliament before enacting domestic laws", "ta": "உள்நாட்டுச் சட்டங்களை இயற்றுவதற்கு முன்பு இந்தியா பிரிட்டிஷ் நாடாளுமன்றத்தின் ஒப்புதலைப் பெற வேண்டும்"},
        {"id": "C", "en": "India cannot cede or acquire any territory under international law", "ta": "சர்வதேச சட்டத்தின் கீழ் இந்தியா எந்தவொரு நிலப்பரப்பையும் விட்டுக் கொடுக்கவோ பெறவோ முடியாது"},
        {"id": "D", "en": "India is a subordinate state under the United Nations Security Council", "ta": "இந்தியா ஐக்கிய நாடுகள் பாதுகாப்புச் சபையின் கீழ் உள்ள ஒரு துணை அரசு"}
    ],
    "'Sovereign' implies that India is an independent state, free from external control and possessing supreme internal authority.",
    "'இறையாண்மை' என்பது இந்தியா எந்தவொரு வெளிநாட்டுக் கட்டுப்பாடும் இல்லாமல் சுதந்திரமாகச் செயல்படும் அரசு என்பதைக் குறிக்கிறது."
))

# Q48 (B) - Statement-Based
gt_all_questions.append(make_q(
    48, "Statement-Based", "Medium", "B",
    "Consider the following statements regarding Fundamental Duties (Part IV-A) and the Preamble:\n1. Article 51A(e) requires citizens to promote harmony and the spirit of common brotherhood (Fraternity).\n2. Article 51A(c) requires citizens to uphold and protect the sovereignty, unity, and integrity of India.\nWhich of the statements given above are CORRECT?",
    "அடிப்படை கடமைகள் (பகுதி IV-A) மற்றும் முகவுரை பற்றிய பின்வரும் கூற்றுகளைக் ஆராய்க:\n1. உறுப்பு 51A(e) குடிமக்கள் நல்லிணக்கத்தையும் பொதுவான சகோதரத்துவ உணர்வையும் வளர்க்க வேண்டும் எனக் கூறுகிறது.\n2. உறுப்பு 51A(c) குடிமக்கள் இந்தியாவின் இறையாண்மை, ஒற்றுமை மற்றும் ஒருமைப்பாட்டை உயர்த்திப் பிடிக்க வேண்டும் எனக் கூறுகிறது.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எவை சரியானவை?",
    [
        {"id": "A", "en": "1 only", "ta": "1 மட்டுமே"},
        {"id": "B", "en": "Both 1 and 2", "ta": "1 மற்றும் 2 இரண்டும்"},
        {"id": "C", "en": "2 only", "ta": "2 மட்டுமே"},
        {"id": "D", "en": "Neither 1 nor 2", "ta": "1-ம் இல்லை 2-ம் இல்லை"}
    ],
    "Both statements 1 and 2 are CORRECT. Articles 51A(e) and 51A(c) directly operationalize the Preamble ideals of Fraternity, Sovereignty, Unity, and Integrity.",
    "கூற்றுகள் 1 மற்றும் 2 இரண்டும் சரியானவை. உறுப்புகள் 51A(e) மற்றும் 51A(c) முகவுரையின் சகோதரத்துவம், இறையாண்மை, ஒருமைப்பாடு இலட்சியங்களைச் செயல்படுத்துகின்றன."
))

# Q49 (C) - Hard Analytical
gt_all_questions.append(make_q(
    49, "Hard Analytical", "Hard", "C",
    "In Minerva Mills v. Union of India (1980), how did the Supreme Court describe the harmony and balance between Fundamental Rights (Part III) and Directive Principles (Part IV)?",
    "மினர்வா மில்ஸ் வழக்கில் (1980), அடிப்படை உரிமைகள் (பகுதி III) மற்றும் வழிகாட்டு நெறிமுறைகள் (பகுதி IV) இடையேயான நல்லிணக்கத்தையும் சமநிலையையும் உச்ச நீதிமன்றம் எவ்வாறு விவரித்தது?",
    [
        {"id": "A", "en": "Part IV completely abrogates Part III during economic distress", "ta": "பொருளாதார நெருக்கடியின் போது பகுதி IV பகுதி III-ஐ முற்றிலும் ரத்து செய்கிறது"},
        {"id": "B", "en": "Part III is permanent while Part IV is temporary and transitional", "ta": "பகுதி III நிரந்தரமானது, பகுதி IV தற்காலிகமானது"},
        {"id": "C", "en": "The Indian Constitution is founded on the bedrock of the balance between Part III and Part IV, which forms an essential feature of Basic Structure", "ta": "இந்திய அரசியலமைப்பு பகுதி III மற்றும் பகுதி IV இடையேயான சமநிலையின் அடித்தளத்திலேயே கட்டமைக்கப்பட்டுள்ளது, இது அடிப்படை கட்டமைப்பின் முக்கிய அம்சமாகும்"},
        {"id": "D", "en": "Part III and Part IV are mutually destructive and cannot co-exist", "ta": "பகுதி III மற்றும் பகுதி IV பரஸ்பரம் அழிவுகரமானவை, ஒன்றாக இணைந்திருக்க முடியாது"}
    ],
    "In Minerva Mills (1980), SC held that harmony and balance between Fundamental Rights and Directive Principles is an essential feature of Basic Structure.",
    "மினர்வா மில்ஸ் வழக்கில் (1980), அடிப்படை உரிமைகள் மற்றும் வழிகாட்டு நெறிமுறைகளுக்கு இடையேயான சமநிலை அடிப்படை கட்டமைப்பின் முக்கிய அம்சம் என தீர்ப்பளிக்கப்பட்டது."
))

# Q50 (A) - Reasoning
gt_all_questions.append(make_q(
    50, "Assertion & Reason", "Hard", "A",
    "Assertion (A): In Kesavananda Bharati case (1973), the Supreme Court held that the Preamble is an integral part of the Constitution.\nReason (R): The Drafting history shows that the Preamble was specifically voted upon and adopted by the Constituent Assembly to stand part of the Constitution.",
    "கூற்று (A): கேசவானந்த பாரதி வழக்கில் (1973), முகவுரை அரசியலமைப்பின் ஒரு ஒருங்கிணைந்த பகுதி என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது.\nகாரணம் (R): அரசியலமைப்பு நிர்ணய அவையால் முகவுரை அரசியலமைப்பின் ஒரு பகுதியாக நிற்க வேண்டும் என்ற பிரேரணையுடன் வாக்களிக்கப்பட்டு ஏற்றுக்கொள்ளப்பட்டது என்பதை வரைவு வரலாறு காட்டுகிறது.",
    [
        {"id": "A", "en": "Both A and R are true and R is the correct explanation of A", "ta": "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்"},
        {"id": "B", "en": "Both A and R are true but R is NOT the correct explanation of A", "ta": "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல"},
        {"id": "C", "en": "A is true but R is false", "ta": "A சரி, ஆனால் R தவறு"},
        {"id": "D", "en": "A is false but R is true", "ta": "A தவறு, ஆனால் R சரி"}
    ],
    "Both A and R are true, and R correctly explains A. The procedural adoption by Constituent Assembly was the key fact convincing SC to hold Preamble as part of Constitution.",
    "A மற்றும் R இரண்டும் சரி, R என்பது A விற்கு சரியான விளக்கமாகும். அவையின் நடைமுறை ஏற்பே உச்ச நீதிமன்றத்தை இந்த முடிவிற்கு கொண்டு வந்தது."
))

# =============================================================================
# BLOCK 3: Questions 51 to 75
# =============================================================================

# Q51 (D) - Direct MCQ
gt_all_questions.append(make_q(
    51, "Direct MCQ", "Easy", "D",
    "On which exact date was the Objectives Resolution adopted by the Constituent Assembly?",
    "குறிக்கோள் தீர்மானம் அரசியலமைப்பு நிர்ணய அவையால் எந்தத் தேதியில் ஏற்றுக்கொள்ளப்பட்டது?",
    [
        {"id": "A", "en": "13th December 1946", "ta": "13 டிசம்பர் 1946"},
        {"id": "B", "en": "15th August 1947", "ta": "15 ஆகஸ்ட் 1947"},
        {"id": "C", "en": "26th November 1949", "ta": "26 நவம்பர் 1949"},
        {"id": "D", "en": "22nd January 1947", "ta": "22 ஜனவரி 1947"}
    ],
    "The Objectives Resolution introduced by Nehru was unanimously adopted by the Constituent Assembly on January 22, 1947.",
    "நேருவால் அறிமுகப்படுத்தப்பட்ட குறிக்கோள் தீர்மானம் ஜனவரி 22, 1947 அன்று அரசியலமைப்பு அவையால் ஏகமனதாக ஏற்றுக்கொள்ளப்பட்டது."
))

# Q52 (A) - Conceptual
gt_all_questions.append(make_q(
    52, "Conceptual MCQ", "Medium", "A",
    "What does 'Social Justice' secured in the Preamble fundamentally guarantee to Indian citizens?",
    "முகவுரையில் உறுதிசெய்யப்பட்ட 'சமூக நீதி' இந்திய குடிமக்களுக்கு அடிப்படை ரீதியாக எதனை உத்தரவாதம் செய்கிறது?",
    [
        {"id": "A", "en": "Equal treatment of all citizens without any social distinction based on caste, color, race, religion or sex", "ta": "சாதி, நிறம், இனம், மதம் அல்லது பாலினத்தின் அடிப்படையில் எந்தவொரு சமூகப் பாகுபாடுமின்றி அனைத்து குடிமக்களையும் சமமாக நடத்துவது"},
        {"id": "B", "en": "Equal distribution of private property among all citizens by force", "ta": "அனைத்து குடிமக்களுக்கும் கட்டாயமாக தனியார் சொத்துக்களைச் சமமாகப் பகிர்ந்தளிப்பது"},
        {"id": "C", "en": "Reservation of all government jobs for urban residents only", "ta": "அனைத்து அரசுப் பணிகளையும் நகர்ப்புறவாசிகளுக்கு மட்டுமே ஒதுக்குவது"},
        {"id": "D", "en": "Abolition of all taxes on corporate enterprises", "ta": "கார்ப்பரேட் நிறுவனங்கள் மீதான அனைத்து வரிகளையும் ஒழிப்பது"}
    ],
    "Social Justice means equal treatment of all citizens without any social discrimination based on caste, religion, sex, or place of birth.",
    "சமூக நீதி என்பது சாதி, மதம், பாலினம் அல்லது பிறந்த இடத்தின் அடிப்படையில் எந்தவொரு சமூகப் பாகுபாடுமின்றி அனைத்து குடிமக்களையும் சமமாக நடத்துவதைக் குறிக்கிறது."
))

# Q53 (B) - Statement-Based
gt_all_questions.append(make_q(
    53, "Statement-Based", "Hard", "B",
    "Consider the following statements regarding the 5 Facets of Liberty in the Preamble:\n1. Liberty of Thought and Expression are guaranteed as justiciable Fundamental Rights under Article 19.\n2. Liberty of Belief, Faith, and Worship are guaranteed as Fundamental Rights under Articles 25 to 28.\nWhich of the statements given above are CORRECT?",
    "முகவுரையில் உள்ள 5 வகையான சுதந்திரங்கள் பற்றிய பின்வரும் கூற்றுகளைக் ஆராய்க:\n1. எண்ணம் மற்றும் கருத்து வெளிப்பாட்டு சுதந்திரம் உறுப்பு 19-ன் கீழ் சட்டப்பூர்வ அடிப்படை உரிமைகளாக உத்தரவாதம் அளிக்கப்பட்டுள்ளன.\n2. நம்பிக்கை, பக்தி மற்றும் வழிபாட்டு சுதந்திரம் உறுப்புகள் 25 முதல் 28 வரை அடிப்படை உரிமைகளாக உத்தரவாதம் அளிக்கப்பட்டுள்ளன.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எவை சரியானவை?",
    [
        {"id": "A", "en": "1 only", "ta": "1 மட்டுமே"},
        {"id": "B", "en": "Both 1 and 2", "ta": "1 மற்றும் 2 இரண்டும்"},
        {"id": "C", "en": "2 only", "ta": "2 மட்டுமே"},
        {"id": "D", "en": "Neither 1 nor 2", "ta": "1-ம் இல்லை 2-ம் இல்லை"}
    ],
    "Both statements 1 and 2 are CORRECT. The 5 facets of Liberty in Preamble find concrete legal expression in Articles 19 and 25-28.",
    "கூற்றுகள் 1 மற்றும் 2 இரண்டும் சரியானவை. முகவுரையில் உள்ள 5 சுதந்திரங்களும் உறுப்புகள் 19 மற்றும் 25-28 இல் சட்டப் பாதுகாப்பு பெறுகின்றன."
))

# Q54 (C) - Hard Analytical
gt_all_questions.append(make_q(
    54, "Hard Analytical", "Hard", "C",
    "Which of the following constitutional deductions correctly explains why the Indian Republic is declared a 'Union of States' rather than a 'Federation of States'?",
    "இந்தியக் குடியரசு 'மாநிலங்களின் கூட்டமைப்பு' (Federation) என்பதற்குப் பதிலாக 'மாநிலங்களின் ஒன்றியம்' (Union) என்று ஏன் அறிவிக்கப்பட்டுள்ளது என்பதற்கான அரசியலமைப்புப் பகுப்பாய்வு எது?",
    [
        {"id": "A", "en": "Because Indian federation is the result of an agreement among states like the United States", "ta": "ஏனெனில் இந்தியக் கூட்டமைப்பு அமெரிக்காவைப் போல மாநிலங்களுக்கு இடையேயான ஒப்பந்தத்தின் விளைவாகும்"},
        {"id": "B", "en": "Because States in India have the constitutional right to secede from the Union under Article 3", "ta": "ஏனெனில் இந்தியாவில் உள்ள மாநிலங்களுக்கு உறுப்பு 3-ன் கீழ் ஒன்றியத்திலிருந்து பிரியும் உரிமை உண்டு"},
        {"id": "C", "en": "Because the Indian federation is not the result of an agreement by states, and no state has the right to secede from the Union", "ta": "ஏனெனில் இந்தியக் கூட்டமைப்பு மாநிலங்களின் ஒப்பந்தத்தால் உருவானதல்ல, மேலும் எந்தவொரு மாநிலத்திற்கும் ஒன்றியத்திலிருந்து பிரியும் உரிமை இல்லை"},
        {"id": "D", "en": "Because the Supreme Court can dissolve any state legislative assembly at will", "ta": "ஏனெனில் உச்ச நீதிமன்றம் தனது விருப்பப்படி எந்தவொரு மாநிலச் சட்டமன்றத்தையும் கலைக்க முடியும்"}
    ],
    "Dr. B.R. Ambedkar explained in the Constituent Assembly that India is a 'Union' because it is not formed by an agreement of states and no state has the right to secede.",
    "டாக்டர் பி.ஆர். அம்பேத்கர் விளக்கியபடி, இந்தியா மாநிலங்களின் ஒப்பந்தத்தால் உருவாக்கப்படாததாலும், பிரியும் உரிமை இல்லாததாலும் அது 'ஒன்றியம்' எனப்படுகிறது."
))

# Q55 (B) - Reasoning
gt_all_questions.append(make_q(
    55, "Assertion & Reason", "Medium", "B",
    "Assertion (A): The Indian Constitution adopted an indirect representative democracy instead of direct democracy.\nReason (R): Devices of direct democracy such as Referendum, Initiative, Recall, and Plebiscite require small population and geographical size, whereas India has vast territory and population.",
    "கூற்று (A): இந்திய அரசியலமைப்பு நேரடி ஜனநாயகத்திற்குப் பதிலாக மறைமுக பிரதிநிதித்துவ ஜனநாயகத்தை ஏற்றுக்கொண்டது.\nகாரணம் (R): பொது வாக்கெடுப்பு, முன்முயற்சி, திரும்ப அழைத்தல் போன்ற நேரடி ஜனநாயகக் கருவிகளுக்கு குறைந்த மக்கள் தொகையும் சிறிய பரப்பளவும் தேவை, ஆனால் இந்தியா பரந்த பரப்பளவையும் மக்கள் தொகையையும் கொண்டுள்ளது.",
    [
        {"id": "A", "en": "Both A and R are true and R is the correct explanation of A", "ta": "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்"},
        {"id": "B", "en": "Both A and R are true but R is NOT the sole explanation of A", "ta": "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு மட்டுமேயான விளக்கமல்ல"},
        {"id": "C", "en": "A is true but R is false", "ta": "A சரி, ஆனால் R தவறு"},
        {"id": "D", "en": "A is false but R is true", "ta": "A தவறு, ஆனால் R சரி"}
    ],
    "Both A and R are true, but R is a descriptive factor alongside familiarity with British parliamentary system.",
    "A மற்றும் R இரண்டும் சரி, ஆனால் பிரிட்டனின் நாடாளுமன்ற முறை மீதான பரிச்சயமும் மற்றொரு முக்கிய காரணியாகும்."
))

# Q56 (D) - Match the Following
gt_all_questions.append(make_q(
    56, "Match the Following", "Hard", "D",
    "Match List I (Preamble Phrases) with List II (Derived Sources/Ideals):\n\nList I\nA. 'We, the People of India'\nB. 'Social, Economic and Political Justice'\nC. 'Liberty, Equality and Fraternity'\nD. 'Socialist & Secular'\n\nList II\n1. 42nd Constitutional Amendment Act, 1976\n2. French Revolution (1789)\n3. Russian Revolution (1917)\n4. American Preamble & Popular Sovereignty",
    "பட்டியல் I-ஐ (முகப்புரைத் தொடர்கள்) பட்டியல் II உடன் (பெறப்பட்ட மூலங்கள்/இலட்சியங்கள்) பொருத்தி சரியான பதிலதைத் தேர்ந்தெடுக்கவும்:\n\nபட்டியல் I\nA. 'இந்திய மக்களாகிய நாம்'\nB. 'சமூக, பொருளாதார மற்றும் அரசியல் நீதி'\nC. 'சுதந்திரம், சமத்துவம் மற்றும் சகோதரத்துவம்'\nD. 'சமதர்ம & மதச்சார்பற்ற'\n\nபட்டியல் II\n1. 42வது அரசியலமைப்புத் திருத்தச் சட்டம், 1976\n2. பிரெஞ்சுப் புரட்சி (1789)\n3. ரஷ்யப் புரட்சி (1917)\n4. அமெரிக்க முகவுரை & மக்களின் இறையாண்மை",
    [
        {"id": "A", "en": "A-4, B-1, C-2, D-3", "ta": "A-4, B-1, C-2, D-3"},
        {"id": "B", "en": "A-3, B-4, C-2, D-1", "ta": "A-3, B-4, C-2, D-1"},
        {"id": "C", "en": "A-4, B-3, C-1, D-2", "ta": "A-4, B-3, C-1, D-2"},
        {"id": "D", "en": "A-4, B-3, C-2, D-1", "ta": "A-4, B-3, C-2, D-1"}
    ],
    "Correct Match: A-4 (We the People = US Preamble / Popular Sovereignty), B-3 (Justice = Russian Rev), C-2 (Liberty/Equality/Fraternity = French Rev), D-1 (Socialist/Secular = 42nd CAA 1976).",
    "சரியான பொருத்தம்: A-4 (மக்களாகிய நாம் = அமெரிக்க முகவுரை), B-3 (நீதி = ரஷ்யப் புரட்சி), C-2 (சுதந்திரம்/சமத்துவம்/சகோதரத்துவம் = பிரெஞ்சுப் புரட்சி), D-1 (சமதர்ம/மதச்சார்பற்ற = 42வது திருத்தம்)."
))

# Q57 (A) - Chronology
gt_all_questions.append(make_q(
    57, "Chronology", "Medium", "A",
    "Arrange the following Constituent Assembly events relating to the Preamble in correct chronological order:\n1. Objectives Resolution introduced by Nehru\n2. Objectives Resolution adopted unanimously\n3. Drafting Committee prepares Draft Preamble\n4. Preamble voted and enacted by Constituent Assembly",
    "முகவுரை தொடர்பான அரசியலமைப்பு நிர்ணய அவையின் பின்வரும் நிகழ்வுகளை சரியான காலவரிசையில் அமைக்கவும்:\n1. நேருவால் குறிக்கோள் தீர்மானம் அறிமுகப்படுத்தப்படுதல்\n2. குறிக்கோள் தீர்மானம் ஏகமனதாக ஏற்றுக்கொள்ளப்படுதல்\n3. வரைவுக் குழு வரைவு முகவுரையைத் தயாரித்தல்\n4. அரசியலமைப்பு அவையால் முகவுரை வாக்களிக்கப்பட்டு இயற்றப்படுதல்",
    [
        {"id": "A", "en": "1 -> 2 -> 3 -> 4", "ta": "1 -> 2 -> 3 -> 4"},
        {"id": "B", "en": "2 -> 1 -> 3 -> 4", "ta": "2 -> 1 -> 3 -> 4"},
        {"id": "C", "en": "1 -> 3 -> 2 -> 4", "ta": "1 -> 3 -> 2 -> 4"},
        {"id": "D", "en": "1 -> 2 -> 4 -> 3", "ta": "1 -> 2 -> 4 -> 3"}
    ],
    "Chronological Sequence: 1 (Moved: Dec 13, 1946) -> 2 (Adopted: Jan 22, 1947) -> 3 (Draft Preamble: Feb 1948) -> 4 (Enacted: Oct 17, 1949).",
    "காலவரிசை: 1 (முன்மொழியப்பட்டது: டிசம்பர் 13, 1946) -> 2 (ஏற்கப்பட்டது: ஜனவரி 22, 1947) -> 3 (வரைவு: பிப்ரவரி 1948) -> 4 (இயற்றப்பட்டது: அக்டோபர் 17, 1949)."
))

# Q58 (B) - PYQ Pattern
gt_all_questions.append(make_q(
    58, "Direct PYQ Pattern", "Easy", "B",
    "Who among the following described the Preamble as 'a Jewel set in the Constitution' and 'the Soul of the Constitution'?",
    "முகவுரையை 'அரசியலமைப்பில் பதிக்கப்பட்ட ஆபரணம்' என்றும் 'அரசியலமைப்பின் ஆன்மா' என்றும் வர்ணித்தவர் யார்?",
    [
        {"id": "A", "en": "N.A. Palkhivala", "ta": "என்.ஏ. பல்கிவாலா"},
        {"id": "B", "en": "Pandit Thakur Das Bhargava", "ta": "பண்டிட் தாக்கூர் தாஸ் பார்கவா"},
        {"id": "C", "en": "K.M. Munshi", "ta": "கே.எம். முன்ஷி"},
        {"id": "D", "en": "Sir Alladi Krishnaswami Iyer", "ta": "சர் அல்லாடி கிருஷ்ணசுவாமி ஐயர்"}
    ],
    "Pandit Thakur Das Bhargava, a member of Constituent Assembly, described the Preamble as a Jewel set in the Constitution and the Soul of the Constitution.",
    "பண்டிட் தாக்கூர் தாஸ் பார்கவா முகவுரையை அரசியலமைப்பில் பதிக்கப்பட்ட ஆபரணம் என்றும் அரசியலமைப்பின் ஆன்மா என்றும் வர்ணித்தார்."
))

# Q59 (C) - TNPSC Trap
gt_all_questions.append(make_q(
    59, "TNPSC Trap", "Hard", "C",
    "Can a citizen file a writ petition under Article 32 in the Supreme Court seeking direct legal enforcement of the Preamble alone?",
    "ஒரு குடிமகன் முகவுரையை மட்டுமே நேரடியாகச் சட்டப்பூர்வமாக அமல்படுத்தக் கோரி உறுப்பு 32-ன் கீழ் உச்ச நீதிமன்றத்தில் நீதிப்பேராணை மனு தாக்கல் செய்ய முடியுமா?",
    [
        {"id": "A", "en": "Yes, because Preamble is superior to Fundamental Rights", "ta": "ஆம், ஏனெனில் முகவுரை அடிப்படை உரிமைகளை விட மேலானது"},
        {"id": "B", "en": "Yes, provided the citizen gets permission from Parliament", "ta": "ஆம், குடிமகன் நாடாளுமன்றத்தின் அனுமதியைப் பெற்றால்"},
        {"id": "C", "en": "No, because the Preamble is non-justiciable and Article 32 applies only to the enforcement of Fundamental Rights in Part III", "ta": "இல்லை, ஏனெனில் முகவுரை நீதிமன்றத்தால் நிலைநிறுத்த முடியாதது மற்றும் உறுப்பு 32 பகுதி III-ல் உள்ள அடிப்படை உரிமைகளை அமல்படுத்துவதற்கு மட்டுமே பொருந்தும்"},
        {"id": "D", "en": "Yes, but only during a Financial Emergency under Article 360", "ta": "ஆம், ஆனால் உறுப்பு 360-ன் கீழ் நிதி அவசரநிலையின் போது மட்டுமே"}
    ],
    "TNPSC Trap Alert: Article 32 enforces Fundamental Rights (Part III) only. The Preamble is non-justiciable and cannot be enforced under Article 32 directly.",
    "TNPSC பொறி எச்சரிக்கை: உறுப்பு 32 அடிப்படை உரிமைகளை மட்டுமே அமல்படுத்துகிறது. முகவுரை நீதிமன்றத்தால் நிலைநிறுத்த முடியாதது."
))

# Q60 (D) - Direct MCQ
gt_all_questions.append(make_q(
    60, "Direct MCQ", "Medium", "D",
    "Who was the Chief Justice of India who delivered the lead judgment in the 13-judge bench of Kesavananda Bharati case (1973)?",
    "1973-ன் கேசவானந்த பாரதி வழக்கின் 13 நீதிபதிகள் அமர்வில் தலைமைத் தீர்ப்பை வழங்கிய இந்தியத் தலைமை நீதிபதி யார்?",
    [
        {"id": "A", "en": "CJI A.N. Ray", "ta": "தலைமை நீதிபதி ஏ.என். ரே"},
        {"id": "B", "en": "CJI K. Subba Rao", "ta": "தலைமை நீதிபதி கே. சுப்பா ராவ்"},
        {"id": "C", "en": "CJI Y.V. Chandrachud", "ta": "தலைமை நீதிபதி ஒய்.வி. சந்திரசூட்"},
        {"id": "D", "en": "CJI S.M. Sikri", "ta": "தலைமை நீதிபதி எஸ்.எம். சிக்ரி"}
    ],
    "Chief Justice S.M. Sikri headed the 13-judge constitutional bench in Kesavananda Bharati v. State of Kerala (1973).",
    "தலைமை நீதிபதி எஸ்.எம். சிக்ரி 1973-ன் கேசவானந்த பாரதி வழக்கில் 13 நீதிபதிகள் அமர்விற்கு தலைமை தாங்கினார்."
))

# Q61 (A) - Conceptual
gt_all_questions.append(make_q(
    61, "Conceptual MCQ", "Medium", "A",
    "What does 'Economic Justice' secured in the Preamble fundamentally mean?",
    "முகவுரையில் உறுதிசெய்யப்பட்ட 'பொருளாதார நீதி' அடிப்படை ரீதியாக எதனைக் குறிக்கிறது?",
    [
        {"id": "A", "en": "Non-discrimination between people on the basis of economic factors and eliminating glaring inequalities in wealth and income", "ta": "பொருளாதாரக் காரணிகளின் அடிப்படையில் மக்களிடையே பாகுபாடு காட்டாமையும் செல்வம் மற்றும் வருமானத்தில் உள்ள வெளிப்படையான ஏற்றத்தாழ்வுகளை அகற்றுவதும்"},
        {"id": "B", "en": "Free distribution of land to foreign companies", "ta": "வெளிநாட்டு நிறுவனங்களுக்கு இலவச நில விநியோகம்"},
        {"id": "C", "en": "Abolition of all private property rights under Article 300A", "ta": "உறுப்பு 300A-ன் கீழ் அனைத்து தனியார் சொத்துரிமைகளையும் ஒழிப்பது"},
        {"id": "D", "en": "Fixing equal wages for all jobs regardless of skill or qualifications", "ta": "திறமை அல்லது தகுதியைப் பொருட்படுத்தாமல் அனைத்து வேலைகளுக்கும் சமமான ஊதியத்தை நிர்ணயம் செய்வது"}
    ],
    "Economic Justice involves non-discrimination based on wealth/income and striving to bridge the gap between rich and poor.",
    "பொருளாதார நீதி என்பது செல்வம்/வருமானத்தின் அடிப்படையில் பாகுபாடு காட்டாமையும் ஏழை எளியோருக்கிடையேயான இடைவெளியைக் குறைப்பதையும் குறிக்கிறது."
))

# Q62 (B) - Statement-Based
gt_all_questions.append(make_q(
    62, "Statement-Based", "Hard", "B",
    "Consider the following statements regarding Secularism in India:\n1. The Indian Constitution embodies positive secularism where all religions receive equal respect and state protection.\n2. In Western secularism, there is a rigid, absolute wall of separation between Church and State.\nWhich of the statements given above are CORRECT?",
    "இந்தியாவில் மதச்சார்பின்மை பற்றிய பின்வரும் கூற்றுகளைக் ஆராய்க:\n1. இந்திய அரசியலமைப்பு நேர்மறை மதச்சார்பின்மையை உள்ளடக்கியுள்ளது, இதில் அனைத்து மதங்களும் சமமான மரியாதையையும் அரசு ஆதரவையும் பெறுகின்றன.\n2. மேற்கத்திய மதச்சார்பின்மையில், மதம் மற்றும் அரசுக்கு இடையே கண்டிப்பான, முழுமையான பிரிப்புச் சுவர் உள்ளது.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எவை சரியானவை?",
    [
        {"id": "A", "en": "1 only", "ta": "1 மட்டுமே"},
        {"id": "B", "en": "Both 1 and 2", "ta": "1 மற்றும் 2 இரண்டும்"},
        {"id": "C", "en": "2 only", "ta": "2 மட்டுமே"},
        {"id": "D", "en": "Neither 1 nor 2", "ta": "1-ம் இல்லை 2-ம் இல்லை"}
    ],
    "Both statements 1 and 2 are CORRECT. Indian secularism is positive ('Sarva Dharma Sambhava'), whereas Western secularism is negative (strict separation).",
    "கூற்றுகள் 1 மற்றும் 2 இரண்டும் சரியானவை. இந்திய மதச்சார்பின்மை நேர்மறையானது, மேற்கத்திய மதச்சார்பின்மை எதிர்மறையானது."
))

# Q63 (C) - Hard Analytical
gt_all_questions.append(make_q(
    63, "Hard Analytical", "Hard", "C",
    "Why was the 42nd Amendment's insertion of 'Socialist' and 'Secular' into the Preamble upheld by the Supreme Court in subsequent decisions?",
    "42வது திருத்தத்தின் மூலம் முகவுரையில் 'சமதர்ம' மற்றும் 'மதச்சார்பற்ற' சொற்களைச் சேர்த்ததை உச்ச நீதிமன்றம் பிந்தைய தீர்ப்புகளில் ஏன் உறுதி செய்தது?",
    [
        {"id": "A", "en": "Because the 42nd Amendment abolished all Fundamental Rights", "ta": "ஏனெனில் 42வது திருத்தம் அனைத்து அடிப்படை உரிமைகளையும் ஒழித்தது"},
        {"id": "B", "en": "Because it converted India into a totalitarian communist state", "ta": "ஏனெனில் இது இந்தியாவை ஒரு சர்வாதிகார கம்யூனிச நாடாக மாற்றியது"},
        {"id": "C", "en": "Because the insertion merely clarified and made explicit what was already implicit in Directive Principles (Part IV) and Fundamental Rights (Arts 25-28)", "ta": "ஏனெனில் இந்த சேர்க்கை வழிகாட்டு நெறிமுறைகள் (பகுதி IV) மற்றும் அடிப்படை உரிமைகளில் (உறுப்புகள் 25-28) ஏற்கனவே மறைமுகமாக இருந்தவை தெளிவுபடுத்தப்பட்டு வெளிப்படையாக்கியது மட்டுமே"},
        {"id": "D", "en": "Because the Supreme Court has no jurisdiction over Preamble amendments", "ta": "ஏனெனில் முகவுரை திருத்தங்கள் மீது உச்ச நீதிமன்றத்திற்கு அதிகாரம் இல்லை"}
    ],
    "The Supreme Court observed that adding 'Socialist' and 'Secular' merely spelt out explicitly what was already built into Parts III and IV of the Constitution.",
    "முகவுரையில் சமதர்ம மற்றும் மதச்சார்பற்ற சொற்களைச் சேர்த்தது பகுதி III மற்றும் IV-ல் ஏற்கனவே இருந்தவையே வெளிப்படையாக்கியது என்று உச்ச நீதிமன்றம் கூறியது."
))

# Q64 (A) - Reasoning
gt_all_questions.append(make_q(
    64, "Assertion & Reason", "Medium", "A",
    "Assertion (A): The Preamble embodies the fundamental moral and political vision of the framers of the Constitution.\nReason (R): It summarizes the core democratic values, freedom struggle ideals, and socio-economic goals agreed upon during the constitution-making process.",
    "கூற்று (A): முகவுரை அரசியலமைப்புச் சிற்பிகளின் அடிப்படை ஒழுக்க நெறி மற்றும் அரசியல் தொலைநோக்குப் பார்வையைத் தன்னுள் கொண்டுள்ளது.\nகாரணம் (R): இது அரசியலமைப்பு உருவாக்கத்தின் போது ஒப்புக்கொள்ளப்பட்ட முக்கிய ஜனநாயக விழுமியங்கள், சுதந்திரப் போராட்ட இலட்சியங்கள் மற்றும் சமூக-பொருளாதார இலக்குகளைச் சுருக்குகிறது.",
    [
        {"id": "A", "en": "Both A and R are true and R is the correct explanation of A", "ta": "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்"},
        {"id": "B", "en": "Both A and R are true but R is NOT the correct explanation of A", "ta": "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல"},
        {"id": "C", "en": "A is true but R is false", "ta": "A சரி, ஆனால் R தவறு"},
        {"id": "D", "en": "A is false but R is true", "ta": "A தவறு, ஆனால் R சரி"}
    ],
    "Both A and R are true, and R correctly explains A. The Preamble serves as the moral summary of the constitutional philosophy.",
    "A மற்றும் R இரண்டும் சரி, R என்பது A விற்கு சரியான விளக்கமாகும். முகவுரை அரசியலமைப்பு தத்துவத்தின் சுருக்கமாகச் செயல்படுகிறது."
))

# Q65 (D) - Match the Following
gt_all_questions.append(make_q(
    65, "Match the Following", "Hard", "D",
    "Match List I (Preamble Features) with List II (Corresponding Constitutional Enactments/Articles):\n\nList I\nA. Fundamental Rights equality\nB. Religious freedom\nC. Welfare state goals\nD. Fundamental Duties brotherhood\n\nList II\n1. Articles 25 to 28\n2. Articles 38 & 39 (DPSP)\n3. Article 51A(e)\n4. Articles 14 to 18",
    "பட்டியல் I-ஐ (முகவுரை அம்சங்கள்) பட்டியல் II உடன் (தொடர்புடைய அரசியலமைப்பு விதிகளுடன்) பொருத்தி சரியான பதிலதைத் தேர்ந்தெடுக்கவும்:\n\nபட்டியல் I\nA. அடிப்படை உரிமைகள் சமத்துவம்\nB. மதச் சுதந்திரம்\nC. நல அரசு இலக்குகள்\nD. அடிப்படை கடமைகள் சகோதரத்துவம்\n\nபட்டியல் II\n1. உறுப்புகள் 25 முதல் 28 வரை\n2. உறுப்புகள் 38 & 39 (DPSP)\n3. உறுப்பு 51A(e)\n4. உறுப்புகள் 14 முதல் 18 வரை",
    [
        {"id": "A", "en": "A-1, B-4, C-2, D-3", "ta": "A-1, B-4, C-2, D-3"},
        {"id": "B", "en": "A-4, B-2, C-1, D-3", "ta": "A-4, B-2, C-1, D-3"},
        {"id": "C", "en": "A-4, B-1, C-3, D-2", "ta": "A-4, B-1, C-3, D-2"},
        {"id": "D", "en": "A-4, B-1, C-2, D-3", "ta": "A-4, B-1, C-2, D-3"}
    ],
    "Correct Match: A-4 (FR Equality = Arts 14-18), B-1 (Religious Freedom = Arts 25-28), C-2 (Welfare State = Arts 38, 39 DPSP), D-3 (Brotherhood = Art 51A(e)).",
    "சரியான பொருத்தம்: A-4 (சமத்துவம் = உறுப்புகள் 14-18), B-1 (மத சுதந்திரம் = உறுப்புகள் 25-28), C-2 (நல அரசு = உறுப்புகள் 38, 39), D-3 (சகோதரத்துவம் = உறுப்பு 51A(e))."
))

# Q66 (A) - Chronology
gt_all_questions.append(make_q(
    66, "Chronology", "Easy", "A",
    "Arrange the four core Objectives mentioned in the Preamble in the exact sequence in which they appear in the text of the Constitution:\n1. Liberty\n2. Justice\n3. Fraternity\n4. Equality",
    "அரசியலமைப்பு உரையில் தோன்றும் அதே வரிசையில் முகவுரையில் குறிப்பிடப்பட்டுள்ள நான்கு முக்கிய குறிக்கோள்களை வரிசைப்படுத்தவும்:\n1. சுதந்திரம்\n2. நீதி\n3. சகோதரத்துவம்\n4. சமத்துவம்",
    [
        {"id": "A", "en": "2 -> 1 -> 4 -> 3", "ta": "2 -> 1 -> 4 -> 3"},
        {"id": "B", "en": "1 -> 2 -> 4 -> 3", "ta": "1 -> 2 -> 4 -> 3"},
        {"id": "C", "en": "2 -> 4 -> 1 -> 3", "ta": "2 -> 4 -> 1 -> 3"},
        {"id": "D", "en": "2 -> 1 -> 3 -> 4", "ta": "2 -> 1 -> 3 -> 4"}
    ],
    "Correct Textual Sequence of Objectives: 2 (Justice) -> 1 (Liberty) -> 4 (Equality) -> 3 (Fraternity). Mnemonic: J-L-E-F.",
    "முகவுரையில் உள்ள சரியான உரை வரிசை: 2 (நீதி) -> 1 (சுதந்திரம்) -> 4 (சமத்துவம்) -> 3 (சகோதரத்துவம்)."
))

# Q67 (B) - PYQ Pattern
gt_all_questions.append(make_q(
    67, "Direct PYQ Pattern", "Easy", "B",
    "Who remarked: 'The Preamble to our Constitution expresses what we had thought or dreamt so long'?",
    "'நமது அரசியலமைப்பின் முகவுரை நாம் இவ்வளவு காலம் என்ன நினைத்தோம் அல்லது கனவு கண்டோம் என்பதை வெளிப்படுத்துகிறது' என்று கூறியவர் யார்?",
    [
        {"id": "A", "en": "Dr. B.R. Ambedkar", "ta": "டாக்டர் பி.ஆர். அம்பேத்கர்"},
        {"id": "B", "en": "Sir Alladi Krishnaswami Iyer", "ta": "சர் அல்லாடி கிருஷ்ணசுவாமி ஐயர்"},
        {"id": "C", "en": "K.M. Munshi", "ta": "கே.எம். முன்ஷி"},
        {"id": "D", "en": "N.A. Palkhivala", "ta": "என்.ஏ. பல்கிவாலா"}
    ],
    "Sir Alladi Krishnaswami Iyer, a distinguished member of the Drafting Committee, made this famous observation.",
    "வரைவுக் குழுவின் முக்கிய உறுப்பினரான சர் அல்லாடி கிருஷ்ணசுவாமி ஐயர் இந்த புகழ்பெற்ற கூற்றைக் கூறினார்."
))

# Q68 (C) - TNPSC Trap
gt_all_questions.append(make_q(
    68, "TNPSC Trap", "Hard", "C",
    "Is 'Religious Equality' mentioned as a separate explicit term alongside 'Equality of Status and Opportunity' in the Preamble?",
    "முகவுரையில் 'அந்தஸ்து மற்றும் வாய்ப்பில் சமத்துவம்' என்பவருடன் 'மதச் சமத்துவம்' என்ற சொல் தனிச் சொல்லாகக் குறிப்பிடப்பட்டுள்ளதா?",
    [
        {"id": "A", "en": "Yes, Religious Equality was added by the 44th Amendment Act in 1978", "ta": "ஆம், மதச் சமத்துவம் 1978-ல் 44வது திருத்தச் சட்டத்தால் சேர்க்கப்பட்டது"},
        {"id": "B", "en": "Yes, it is the 3rd category of Equality in the Preamble", "ta": "ஆம், இது முகவுரையில் உள்ள 3வது வகை சமத்துவமாகும்"},
        {"id": "C", "en": "No, the Preamble contains ONLY 'Equality of status and of opportunity'; religious equality is subsumed under 'Secular' and Article 25", "ta": "இல்லை, முகவுரையில் 'அந்தஸ்திலும் வாய்ப்பிலும் சமத்துவம்' மட்டுமே உள்ளது; மதச் சமத்துவம் 'மதச்சார்பற்ற' மற்றும் உறுப்பு 25-ல் அடங்கும்"},
        {"id": "D", "en": "Yes, it was in the original 1949 Preamble", "ta": "ஆம், இது அசல் 1949 முகவுரையில் இருந்தது"}
    ],
    "TNPSC Trap Alert: The Preamble mentions ONLY 2 categories of Equality: Status and Opportunity. 'Religious Equality' is not a separate phrase.",
    "TNPSC பொறி எச்சரிக்கை: முகவுரையில் 2 வகை சமத்துவங்கள் மட்டுமே உள்ளன: அந்தஸ்து மற்றும் வாய்ப்பு. 'மதச் சமத்துவம்' தனித் தொடராக இல்லை."
))

# Q69 (D) - Direct MCQ
gt_all_questions.append(make_q(
    69, "Direct MCQ", "Easy", "D",
    "Which body passed and enacted the Preamble of the Constitution of India on behalf of the people of India?",
    "இந்திய மக்களின் சார்பில் இந்திய அரசியலமைப்பின் முகவுரையை நிறைவேற்றி இயற்றிய அமைப்பு எது?",
    [
        {"id": "A", "en": "British House of Commons", "ta": "பிரிட்டிஷ் மக்களவை"},
        {"id": "B", "en": "Provisional Government of 1947", "ta": "1947 இன் இடைக்கால அரசாங்கம்"},
        {"id": "C", "en": "First Lok Sabha of Independent India", "ta": "சுதந்திர இந்தியாவின் முதல் மக்களவை"},
        {"id": "D", "en": "Constituent Assembly of India", "ta": "இந்திய அரசியலமைப்பு நிர்ணய அவை"}
    ],
    "The Constituent Assembly of India, acting on behalf of the people of India, adopted, enacted, and gave to themselves the Constitution.",
    "இந்திய மக்களின் சார்பில் செயல்பட்ட இந்திய அரசியலமைப்பு நிர்ணய அவையே அரசியலமைப்பை ஏற்று இயற்றி தந்தது."
))

# Q70 (A) - Conceptual
gt_all_questions.append(make_q(
    70, "Conceptual MCQ", "Medium", "A",
    "What does 'Political Justice' guaranteed in the Preamble essentially guarantee to all citizens?",
    "முகவுரையில் உத்தரவாதம் அளிக்கப்பட்டுள்ள 'அரசியல் நீதி' அனைத்து குடிமக்களுக்கும் முக்கியமாக எதனை உத்தரவாதம் செய்கிறது?",
    [
        {"id": "A", "en": "Equal political rights, equal access to all political offices, and equal voice in the government", "ta": "சமமான அரசியல் உரிமைகள், அனைத்து அரசியல் பதவிகளையும் அடையும் சம வாய்ப்பு மற்றும் அரசாங்கத்தில் சமமான குரல்"},
        {"id": "B", "en": "Guaranteed cabinet minister positions for all political parties", "ta": "அனைத்து அரசியல் கட்சிகளுக்கும் அமைச்சரவை அமைச்சர் பதவிகள் உத்தரவாதம்"},
        {"id": "C", "en": "Exemption of political leaders from criminal laws", "ta": "குற்றவியல் சட்டங்களிலிருந்து அரசியல் தலைவர்களுக்கு விலக்கு"},
        {"id": "D", "en": "Funding of political election campaigns by the Supreme Court", "ta": "உச்ச நீதிமன்றத்தால் அரசியல் தேர்தல் பிரச்சாரங்களுக்கு நிதி வழங்குவது"}
    ],
    "Political Justice implies that all citizens should have equal political rights, equal access to political offices, and equal participation in government.",
    "அரசியல் நீதி என்பது அனைத்து குடிமக்களுக்கும் சமமான அரசியல் உரிமைகள், அரசு பதவிகளை அடையும் சம வாய்ப்பு மற்றும் பங்கேற்பைக் குறிக்கிறது."
))

# Q71 (B) - Statement-Based
gt_all_questions.append(make_q(
    71, "Statement-Based", "Medium", "B",
    "Consider the following statements regarding the text of the Preamble:\n1. The phrase 'Sovereign Socialist Secular Democratic Republic' defines the Nature of the Indian State.\n2. The phrase 'Justice, Liberty, Equality, Fraternity' defines the Core Objectives of the Constitution.\nWhich of the statements given above are CORRECT?",
    "முகவுரையின் உரை பற்றிய பின்வரும் கூற்றுகளைக் ஆராய்க:\n1. 'இறையாண்மை சமதர்ம மதச்சார்பற்ற ஜனநாயக குடியரசு' என்ற தொடர் இந்திய அரசின் தன்மையை வரையறுக்கிறது.\n2. 'நீதி, சுதந்திரம், சமத்துவம், சகோதரத்துவம்' என்ற தொடர் அரசியலமைப்பின் முக்கிய குறிக்கோள்களை வரையறுக்கிறது.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எவை சரியானவை?",
    [
        {"id": "A", "en": "1 only", "ta": "1 மட்டுமே"},
        {"id": "B", "en": "Both 1 and 2", "ta": "1 மற்றும் 2 இரண்டும்"},
        {"id": "C", "en": "2 only", "ta": "2 மட்டுமே"},
        {"id": "D", "en": "Neither 1 nor 2", "ta": "1-ம் இல்லை 2-ம் இல்லை"}
    ],
    "Both statements 1 and 2 are CORRECT. Statement 1 defines Nature of State; Statement 2 defines Objectives.",
    "கூற்றுகள் 1 மற்றும் 2 இரண்டும் சரியானவை. கூற்று 1 அரசின் தன்மையையும், கூற்று 2 குறிக்கோள்களையும் வரையறுக்கின்றன."
))

# Q72 (C) - Hard Analytical
gt_all_questions.append(make_q(
    72, "Hard Analytical", "Hard", "C",
    "Which of the following correctly describes how executive and legislative powers are conditioned by the Preamble?",
    "நிர்வாக மற்றும் சட்ட அதிகாரங்கள் முகவுரையால் எவ்வாறு நிபந்தனைக்குட்படுத்தப்படுகின்றன என்பதை பின்வருவனவற்றில் எது சரியாக விவரிக்கிறது?",
    [
        {"id": "A", "en": "Preamble grants emergency decree powers directly to the President", "ta": "முகவுரை நேரடியாகக் குடியரசுத் தலைவருக்கு அவசர ஆணை அதிகாரங்களை வழங்குகிறது"},
        {"id": "B", "en": "Preamble prohibits Parliament from imposing any taxes on citizens", "ta": "முகவுரை குடிமக்கள் மீது எந்த வரியும் விதிப்பதை நாடாளுமன்றத்திற்குத் தடை செய்கிறது"},
        {"id": "C", "en": "Preamble does not directly confer substantive power or impose prohibition, but sets the normative philosophical goals that all state organs must strive to achieve", "ta": "முகவுரை நேரடியாக அதிகாரத்தையோ தடையையோ விதிக்காது, ஆனால் அனைத்து அரசு அமைப்புகளும் அடைய முனைய வேண்டிய தத்துவார்த்த இலக்குகளை அமைக்கிறது"},
        {"id": "D", "en": "Preamble allows the executive to bypass acts of Parliament during war", "ta": "போரின் போது நாடாளுமன்றச் சட்டங்களை நிர்வாகத்துறை புறக்கணிக்க முகவுரை அனுமதிக்கிறது"}
    ],
    "The Preamble is non-substantive in terms of direct power, but sets the normative constitutional principles guiding all branches of government.",
    "முகவுரை நேரடியாக அதிகாரத்தை வழங்காவிட்டாலும், அனைத்து அரசு அமைப்புகளுக்கும் வழிகாட்டும் தத்துவார்த்த இலக்குகளை அமைக்கிறது."
))

# Q73 (B) - Reasoning
gt_all_questions.append(make_q(
    73, "Assertion & Reason", "Medium", "B",
    "Assertion (A): Sir Ernest Barker described the Preamble of the Indian Constitution as the 'Key-note' to the Constitution.\nReason (R): He quoted the Indian Preamble at the very beginning of his famous treatise 'Principles of Social and Political Theory' (1951).",
    "கூற்று (A): சர் எர்னஸ்ட் பார்கர் இந்திய அரசியலமைப்பின் முகவுரையை அரசியலமைப்பின் 'முக்கிய குறிப்பு' (Key-note) என்று வர்ணித்தார்.\nகாரணம் (R): தனது புகழ்பெற்ற 'சமூக மற்றும் அரசியல் கோட்பாட்டின் கொள்கைகள்' (1951) நூலின் தொடக்கத்தில் இந்திய முகவுரையை அவர் மேற்கோள் காட்டினார்.",
    [
        {"id": "A", "en": "Both A and R are true and R is the correct explanation of A", "ta": "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்"},
        {"id": "B", "en": "Both A and R are true but R is an independent supporting fact", "ta": "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது ஒரு சுயாதீன ஆதரவு உண்மையாகும்"},
        {"id": "C", "en": "A is true but R is false", "ta": "A சரி, ஆனால் R தவறு"},
        {"id": "D", "en": "A is false but R is true", "ta": "A தவறு, ஆனால் R சரி"}
    ],
    "Both A and R are true. Barker admired the Preamble as the key-note of constitutional principles and reprinted it in his 1951 book.",
    "A மற்றும் R இரண்டும் சரி. பார்கர் முகவுரையைப் பாராட்டி தனது 1951 புத்தகத்தின் தொடக்கத்தில் அச்சிட்டார்."
))

# Q74 (D) - Match the Following
gt_all_questions.append(make_q(
    74, "Match the Following", "Hard", "D",
    "Match List I (Keywords in Preamble) with List II (Constitutional Definitions):\n\nList I\nA. Sovereign\nB. Socialist\nC. Secular\nD. Republic\n\nList II\n1. State has no official state religion; treats all religions equally\n2. Head of State is elected directly/indirectly for a fixed term\n3. Independent state free from external control\n4. Mixed economy seeking to bridge income inequalities through democratic means",
    "பட்டியல் I-ஐ (முகவுரைச் சொற்கள்) பட்டியல் II உடன் (அரசியலமைப்பு வரையறைகள்) பொருத்தி சரியான பதிலதைத் தேர்ந்தெடுக்கவும்:\n\nபட்டியல் I\nA. இறையாண்மை\nB. சமதர்ம\nC. மதச்சார்பற்ற\nD. குடியரசு\n\nபட்டியல் II\n1. அரசுக்கு அதிகாரப்பூர்வ மதம் இல்லை; அனைத்து மதங்களையும் சமமாக நடத்துகிறது\n2. நாட்டின் தலைவர் ஒரு குறிப்பிட்ட காலத்திற்கு நேரடியாக/மறைமுகமாகத் தேர்ந்தெடுக்கப்படுகிறார்\n3. வெளிநாட்டுக் கட்டுப்பாடற்ற சுதந்திரமான அரசு\n4. ஜனநாயக வழிகளில் வருமான ஏற்றத்தாழ்வுகளை அகற்றும் கலப்புப் பொருளாதாரம்",
    [
        {"id": "A", "en": "A-3, B-1, C-4, D-2", "ta": "A-3, B-1, C-4, D-2"},
        {"id": "B", "en": "A-4, B-3, C-1, D-2", "ta": "A-4, B-3, C-1, D-2"},
        {"id": "C", "en": "A-3, B-4, C-2, D-1", "ta": "A-3, B-4, C-2, D-1"},
        {"id": "D", "en": "A-3, B-4, C-1, D-2", "ta": "A-3, B-4, C-1, D-2"}
    ],
    "Correct Match: A-3 (Sovereign = Independent state), B-4 (Socialist = Mixed economy), C-1 (Secular = No official religion / equal treatment), D-2 (Republic = Elected head of state).",
    "சரியான பொருத்தம்: A-3 (இறையாண்மை = சுதந்திர அரசு), B-4 (சமதர்ம = கலப்பு பொருளாதாரம்), C-1 (மதச்சார்பற்ற = அதிகாரப்பூர்வ மதம் இல்லாமை), D-2 (குடியரசு = தேர்ந்தெடுக்கப்பட்ட தலைவர்)."
))

# Q75 (A) - Chronology
gt_all_questions.append(make_q(
    75, "Chronology", "Hard", "A",
    "Arrange the following key legal & legislative developments of the Preamble in correct chronological order:\n1. Moving of Objectives Resolution in Constituent Assembly\n2. Advisory Opinion of Supreme Court in Berubari Union Case\n3. Ruling of 13-Judge bench in Kesavananda Bharati Case\n4. Enactment of 42nd Constitutional Amendment Act",
    "முகவுரையின் பின்வரும் முக்கிய சட்ட மற்றும் சட்டமன்ற முன்னேற்றங்களை சரியான காலவரிசையில் அமைக்கவும்:\n1. அரசியலமைப்பு அவையில் குறிக்கோள் தீர்மானம் முன்மொழியப்படுதல்\n2. பெருபாரி யூனியன் வழக்கில் உச்ச நீதிமன்றத்தின் ஆலோசனைக் கருத்து\n3. கேசவானந்த பாரதி வழக்கில் 13 நீதிபதிகள் அமர்வின் தீர்ப்பு\n4. 42வது அரசியலமைப்புத் திருத்தச் சட்டம் இயற்றப்படுதல்",
    [
        {"id": "A", "en": "1 -> 2 -> 3 -> 4", "ta": "1 -> 2 -> 3 -> 4"},
        {"id": "B", "en": "2 -> 1 -> 3 -> 4", "ta": "2 -> 1 -> 3 -> 4"},
        {"id": "C", "en": "1 -> 3 -> 2 -> 4", "ta": "1 -> 3 -> 2 -> 4"},
        {"id": "D", "en": "1 -> 2 -> 4 -> 3", "ta": "1 -> 2 -> 4 -> 3"}
    ],
    "Chronological Sequence: 1 (Objectives Resolution: Dec 1946) -> 2 (Berubari: 1960) -> 3 (Kesavananda Bharati: 1973) -> 4 (42nd Amendment: 1976).",
    "காலவரிசை: 1 (குறிக்கோள் தீர்மானம்: டிசம்பர் 1946) -> 2 (பெருபாரி: 1960) -> 3 (கேசவானந்த பாரதி: 1973) -> 4 (42வது திருத்தம்: 1976)."
))

# =============================================================================
# BLOCK 4: Questions 76 to 100
# =============================================================================

# Q76 (B) - PYQ Pattern
gt_all_questions.append(make_q(
    76, "Direct PYQ Pattern", "Easy", "B",
    "Under whose Prime Ministership was the 42nd Constitutional Amendment Act of 1976 enacted?",
    "யாருடைய பிரதம மந்திரி பதவிக் காலத்தில் 1976 ஆம் ஆண்டின் 42வது அரசியலமைப்புத் திருத்தச் சட்டம் இயற்றப்பட்டது?",
    [
        {"id": "A", "en": "Jawaharlal Nehru", "ta": "ஜவஹர்லால் நேரு"},
        {"id": "B", "en": "Indira Gandhi", "ta": "இந்திரா காந்தி"},
        {"id": "C", "en": "Morarji Desai", "ta": "மொரார்ஜி தேசாய்"},
        {"id": "D", "en": "Lal Bahadur Shastri", "ta": "லால் பகதூர் சாஸ்திரி"}
    ],
    "The 42nd Amendment Act 1976 was enacted under the Prime Ministership of Smt. Indira Gandhi.",
    "42வது அரசியலமைப்புத் திருத்தச் சட்டம் 1976 திருமதி இந்திரா காந்தி பிரதமராக இருந்தபோது இயற்றப்பட்டது."
))

# Q77 (C) - TNPSC Trap
gt_all_questions.append(make_q(
    77, "TNPSC Trap", "Hard", "C",
    "Which of the following statements correctly captures the dual legal attributes of the Preamble as established by the Supreme Court?",
    "உச்ச நீதிமன்றத்தால் நிறுவப்பட்டபடி முகவுரையின் இரட்டை சட்டப் பண்புகளை பின்வரும் கூற்றுகளில் எது சரியாகப் படம்பிடிக்கிறது?",
    [
        {"id": "A", "en": "Preamble is both a source of power to the legislature and justiciable in courts", "ta": "முகவுரை சட்டமன்றத்திற்கு அதிகாரம் அளிக்கும் மூலமாகவும் நீதிமன்றங்களால் நிலைநிறுத்தக்கூடியதாகவும் உள்ளது"},
        {"id": "B", "en": "Preamble is a source of executive power and superior to Fundamental Rights", "ta": "முகவுரை நிர்வாக அதிகாரத்தின் மூலமாகவும் அடிப்படை உரிமைகளை விட மேலானதாகவும் உள்ளது"},
        {"id": "C", "en": "Preamble is NEITHER a source of power to the legislature NOR a prohibition upon powers, and it is NON-JUSTICIABLE", "ta": "முகவுரை சட்டமன்றத்திற்கு அதிகாரத்தை வழங்கும் மூலமும் அல்ல, அதிகாரங்கள் மீதான தடையுமல்ல, மேலும் இது நீதிமன்றத்தால் நிலைநிறுத்த முடியாதது (Non-justiciable)"},
        {"id": "D", "en": "Preamble is justiciable only in High Courts under Article 226", "ta": "முகவுரை உறுப்பு 226-ன் கீழ் உயர் நீதிமன்றங்களில் மட்டுமே நிலைநிறுத்தக்கூடியது"}
    ],
    "TNPSC Trap Alert: The 2 core legal attributes: 1. Neither a source nor prohibition on power. 2. Non-justiciable in courts of law.",
    "TNPSC பொறி எச்சரிக்கை: 2 முக்கிய சட்டப்பண்புகள்: 1. அதிகார மூலமும் அல்ல, தடையுமல்ல. 2. நீதிமன்றத்தால் நிலைநிறுத்த முடியாதது."
))

# Q78 (D) - Direct MCQ
gt_all_questions.append(make_q(
    78, "Direct MCQ", "Medium", "D",
    "On which date was the Preamble voted upon and enacted LAST by the Constituent Assembly?",
    "அரசியலமைப்பு நிர்ணய அவையால் முகவுரை வாக்களிக்கப்பட்டு இறுதியாக இயற்றப்பட்ட தேதி எது?",
    [
        {"id": "A", "en": "26th November 1949", "ta": "26 நவம்பர் 1949"},
        {"id": "B", "en": "26th January 1950", "ta": "26 ஜனவரி 1950"},
        {"id": "C", "en": "22nd January 1947", "ta": "22 ஜனவரி 1947"},
        {"id": "D", "en": "17th October 1949", "ta": "17 அக்டோபர் 1949"}
    ],
    "The Constituent Assembly passed the motion 'that the Preamble stand part of the Constitution' on October 17, 1949.",
    "அரசியலமைப்பு அவையில் அக்டோபர் 17, 1949 அன்று முகவுரையை இயற்றும் பிரேரணை நிறைவேற்றப்பட்டது."
))

# Q79 (A) - Conceptual
gt_all_questions.append(make_q(
    79, "Conceptual MCQ", "Medium", "A",
    "In the context of the Preamble, how is 'Dignity of the Individual' related to National Integration?",
    "முகவுரையின் சூழலில், 'தனிநபரின் கண்ணியம்' என்பது தேசிய ஒருமைப்பாட்டுடன் எவ்வாறு தொடர்பு கொண்டுள்ளது?",
    [
        {"id": "A", "en": "National unity and integrity cannot be achieved without guaranteeing the dignity and self-respect of every individual citizen", "ta": "ஒவ்வொரு தனிநபர் குடிமகனின் கண்ணியத்தையும் சுயமரியாதையையும் உறுதி செய்யாமல் தேசிய ஒற்றுமையையும் ஒருமைப்பாட்டையும் அடைய முடியாது"},
        {"id": "B", "en": "National integration requires individuals to renounce all personal freedom", "ta": "தேசிய ஒருமைப்பாட்டிற்கு தனிநபர்கள் தங்கள் அனைத்து தனிப்பட்ட சுதந்திரத்தையும் துறக்க வேண்டும்"},
        {"id": "C", "en": "Individual dignity applies only to tax-paying citizens", "ta": "தனிநபர் கண்ணியம் வரி செலுத்தும் குடிமக்களுக்கு மட்டுமே பொருந்தும்"},
        {"id": "D", "en": "Dignity is a economic term with no constitutional relevance", "ta": "கண்ணியம் என்பது அரசியலமைப்புத் தொடர்பற்ற ஒரு பொருளாதாரச் சொல்லாகும்"}
    ],
    "K.M. Munshi noted that dignity of the individual recognizes that the Constitution is not merely an instrument for governance, but for building personality and self-respect of citizens.",
    "கே.எம். முன்ஷி சுட்டிக்காட்டியபடி தனிநபர் கண்ணியம் என்பது குடிமக்களின் ஆளுமை மற்றும் சுயமரியாதையைக் கட்டியெழுப்ப உதவுகிறது."
))

# Q80 (B) - Statement-Based
gt_all_questions.append(make_q(
    80, "Statement-Based", "Hard", "B",
    "Consider the following statements regarding the Basic Structure features derived from the Preamble:\n1. Sovereign, Democratic, and Republican nature of Indian polity form part of Basic Structure.\n2. Secular character and Social & Economic Justice form part of Basic Structure.\n3. Unity and Integrity of the Nation form part of Basic Structure.\nWhich of the statements given above are CORRECT?",
    "முகவுரையிலிருந்து பெறப்பட்ட அடிப்படை கட்டமைப்பு அம்சங்கள் பற்றிய பின்வரும் கூற்றுகளைக் ஆராய்க:\n1. இந்திய அமைப்பின் இறையாண்மை, ஜனநாயக மற்றும் குடியரசுத் தன்மை ஆகியவை அடிப்படை கட்டமைப்பின் பகுதியாகும்.\n2. மதச்சார்பற்ற இயல்பு மற்றும் சமூக & பொருளாதார நீதி ஆகியவை அடிப்படை கட்டமைப்பின் பகுதியாகும்.\n3. நாட்டின் ஒற்றுமை மற்றும் ஒருமைப்பாடு ஆகியவை அடிப்படை கட்டமைப்பின் பகுதியாகும்.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எவை சரியானவை?",
    [
        {"id": "A", "en": "1 and 2 only", "ta": "1 மற்றும் 2 மட்டுமே"},
        {"id": "B", "en": "1, 2 and 3", "ta": "1, 2 மற்றும் 3"},
        {"id": "C", "en": "2 and 3 only", "ta": "2 மற்றும் 3 மட்டுமே"},
        {"id": "D", "en": "1 and 3 only", "ta": "1 மற்றும் 3 மட்டுமே"}
    ],
    "All three statements (1, 2, and 3) are CORRECT. The Supreme Court in Kesavananda Bharati, Bommai, and Minerva Mills affirmed these Preamble features as part of Basic Structure.",
    "மூன்று கூற்றுகளும் (1, 2 மற்றும் 3) சரியானவை. கேசவானந்த பாரதி, பொம்மை, மினர்வா மில்ஸ் வழக்குகளில் இவை அடிப்படை கட்டமைப்பாக உறுதி செய்யப்பட்டன."
))

# Q81 (C) - Hard Analytical
gt_all_questions.append(make_q(
    81, "Hard Analytical", "Hard", "C",
    "How does the Preamble bridge the justiciable Fundamental Rights (Part III) and non-justiciable Directive Principles (Part IV)?",
    "சட்டப்பூர்வ அடிப்படை உரிமைகளையும் (பகுதி III) சட்டப்பூர்வமற்ற வழிகாட்டு நெறிமுறைகளையும் (பகுதி IV) முகவுரை எவ்வாறு இணைக்கிறது?",
    [
        {"id": "A", "en": "By declaring both Parts III and IV to be non-justiciable during wartime", "ta": "போர்க்காலத்தில் பகுதி III மற்றும் IV ஆகிய இரண்டையும் சட்டப்பூர்வமற்றவை என அறிவிப்பதன் மூலம்"},
        {"id": "B", "en": "By giving supreme precedence to Fundamental Rights over Directive Principles in all situations", "ta": "அனைத்து சூழ்நிலைகளிலும் அடிப்படை உரிமைகளுக்கு வழிகாட்டு நெறிமுறைகளை விட மேலாதிக்கம் அளிப்பதன் மூலம்"},
        {"id": "C", "en": "By providing the common philosophy of Liberty, Equality, and Justice that unifies Part III (civil-political rights) and Part IV (socio-economic goals) into an integrated constitutional scheme", "ta": "பகுதி III (அரசியல் உரிமைகள்) மற்றும் பகுதி IV (சமூக-பொருளாதார இலக்குகள்) ஆகியவற்றை ஒருங்கிணைக்கும் சுதந்திரம், சமத்துவம், நீதியின் பொதுத் தத்துவத்தை வழங்குவதன் மூலம்"},
        {"id": "D", "en": "By allowing Parliament to abolish both Parts III and IV through ordinary legislation", "ta": "சாதாரணச் சட்டத்தின் மூலம் பகுதி III மற்றும் IV ஆகிய இரண்டையும் ரத்து செய்ய நாடாளுமன்றத்தை அனுமதிப்பதன் மூலம்"}
    ],
    "The Preamble encapsulates the common philosophy uniting Part III (individual civil-political freedoms) and Part IV (collective socio-economic welfare goals).",
    "முகவுரை பகுதி III (தனிநபர் உரிமைகள்) மற்றும் பகுதி IV (சமூக நல இலக்குகள்) ஆகியவற்றை இணைக்கும் பொதுவான தத்துவத்தை வழங்குகிறது."
))

# Q82 (A) - Reasoning
gt_all_questions.append(make_q(
    82, "Assertion & Reason", "Hard", "A",
    "Assertion (A): The Preamble is non-justiciable and cannot be directly enforced in a court of law to obtain legal relief.\nReason (R): The objectives stated in the Preamble are promotional and aspirational guidelines intended to be achieved through legislative enactments and executive policies.",
    "கூற்று (A): முகவுரை நீதிமன்றத்தால் நிலைநிறுத்த முடியாதது (Non-justiciable) மற்றும் சட்ட நிவாரணம் பெற நீதிமன்றத்தில் நேரடியாக அமல்படுத்தப்பட முடியாது.\nகாரணம் (R): முகவுரையில் குறிப்பிடப்பட்டுள்ள குறிக்கோள்கள் சட்டமன்றச் சட்டங்கள் மற்றும் நிர்வாகக் கொள்கைகள் மூலம் அடையப்பட வேண்டிய ஊக்குவிப்பு மற்றும் இலட்சிய வழிகாட்டுதல்கள் ஆகும்.",
    [
        {"id": "A", "en": "Both A and R are true and R is the correct explanation of A", "ta": "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்"},
        {"id": "B", "en": "Both A and R are true but R is NOT the correct explanation of A", "ta": "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல"},
        {"id": "C", "en": "A is true but R is false", "ta": "A சரி, ஆனால் R தவறு"},
        {"id": "D", "en": "A is false but R is true", "ta": "A தவறு, ஆனால் R சரி"}
    ],
    "Both A and R are true, and R correctly explains why Preamble provisions are non-justiciable (they are aspirational goals translated by legislation).",
    "A மற்றும் R இரண்டும் சரி, R என்பது A விற்கு சரியான விளக்கமாகும். முகவுரை இலக்குகள் சட்டங்கள் மூலம் அடையப்பட வேண்டிய உன்னத நோக்கங்கள் ஆகும்."
))

# Q83 (D) - Match the Following
gt_all_questions.append(make_q(
    83, "Match the Following", "Medium", "D",
    "Match List I (Key Dates in Preamble History) with List II (Historical Milestones):\n\nList I\nA. 13th December 1946\nB. 22nd January 1947\nC. 17th October 1949\nD. 26th November 1949\n\nList II\n1. Adoption date mentioned in the Preamble text\n2. Objectives Resolution moved by Jawaharlal Nehru\n3. Objectives Resolution adopted by Constituent Assembly\n4. Preamble voted and enacted by Constituent Assembly",
    "பட்டியல் I-ஐ (முகவுரை வரலாற்றின் முக்கிய தேதிகள்) பட்டியல் II உடன் (வரலாற்று மைல்கற்கள்) பொருத்தி சரியான பதிலதைத் தேர்ந்தெடுக்கவும்:\n\nபட்டியல் I\nA. 13 டிசம்பர் 1946\nB. 22 ஜனவரி 1947\nC. 17 அக்டோபர் 1949\nD. 26 நவம்பர் 1949\n\nபட்டியல் II\n1. முகவுரை உரையில் குறிப்பிடப்பட்டுள்ள ஏற்றுக்கொள்ளப்பட்ட தேதி\n2. ஜவஹர்லால் நேருவால் குறிக்கோள் தீர்மானம் முன்மொழியப்படுதல்\n3. அரசியலமைப்பு அவையால் குறிக்கோள் தீர்மானம் ஏற்றுக்கொள்ளப்படுதல்\n4. அரசியலமைப்பு அவையால் முகவுரை வாக்களிக்கப்பட்டு இயற்றப்படுதல்",
    [
        {"id": "A", "en": "A-2, B-3, C-1, D-4", "ta": "A-2, B-3, C-1, D-4"},
        {"id": "B", "en": "A-3, B-2, C-4, D-1", "ta": "A-3, B-2, C-4, D-1"},
        {"id": "C", "en": "A-2, B-1, C-4, D-3", "ta": "A-2, B-1, C-4, D-3"},
        {"id": "D", "en": "A-2, B-3, C-4, D-1", "ta": "A-2, B-3, C-4, D-1"}
    ],
    "Correct Match: A-2 (Dec 13, 1946 = Resolution moved), B-3 (Jan 22, 1947 = Resolution adopted), C-4 (Oct 17, 1949 = Preamble enacted), D-1 (Nov 26, 1949 = Adoption date in Preamble).",
    "சரியான பொருத்தம்: A-2 (டிசம்பர் 13, 1946 = முன்மொழிவு), B-3 (ஜனவரி 22, 1947 = ஏற்பு), C-4 (அக்டோபர் 17, 1949 = இயற்றப்பட்டது), D-1 (நவம்பர் 26, 1949 = ஏற்றுக்கொள்ளப்பட்ட தேதி)."
))

# Q84 (A) - Chronology
gt_all_questions.append(make_q(
    84, "Chronology", "Hard", "A",
    "Arrange the following landmark Supreme Court cases in REVERSE chronological order (most recent first):\n1. LIC of India Case\n2. S.R. Bommai Case\n3. 42nd Amendment Act enacted\n4. Kesavananda Bharati Case\n5. Berubari Union Case",
    "பின்வரும் மைல்கல் உச்ச நீதிமன்ற வழக்குகளை தலைகீழ் காலவரிசையில் (மிக சமீபத்தியது முதலில்) அமைக்கவும்:\n1. எல்.ஐ.சி வழக்கு\n2. எஸ்.ஆர். பொம்மை வழக்கு\n3. 42வது திருத்தச் சட்டம் இயற்றப்படுதல்\n4. கேசவானந்த பாரதி வழக்கு\n5. பெருபாரி யூனியன் வழக்கு",
    [
        {"id": "A", "en": "1 -> 2 -> 3 -> 4 -> 5", "ta": "1 -> 2 -> 3 -> 4 -> 5"},
        {"id": "B", "en": "5 -> 4 -> 3 -> 2 -> 1", "ta": "5 -> 4 -> 3 -> 2 -> 1"},
        {"id": "C", "en": "1 -> 3 -> 2 -> 4 -> 5", "ta": "1 -> 3 -> 2 -> 4 -> 5"},
        {"id": "D", "en": "2 -> 1 -> 3 -> 4 -> 5", "ta": "2 -> 1 -> 3 -> 4 -> 5"}
    ],
    "Reverse Chronological Sequence: 1 (LIC: 1995) -> 2 (Bommai: 1994) -> 3 (42nd CAA: 1976) -> 4 (Kesavananda: 1973) -> 5 (Berubari: 1960).",
    "தலைகீழ் காலவரிசை: 1 (LIC: 1995) -> 2 (பொம்மை: 1994) -> 3 (42வது திருத்தம்: 1976) -> 4 (கேசவானந்தா: 1973) -> 5 (பெருபாரி: 1960)."
))

# Q85 (B) - PYQ Pattern
gt_all_questions.append(make_q(
    85, "Direct PYQ Pattern", "Easy", "B",
    "Who was the leader who moved the historic 'Objectives Resolution' in the Constituent Assembly on 13th December 1946?",
    "13 டிசம்பர் 1946 அன்று அரசியலமைப்பு அவையில் வரலாற்றுச் சிறப்புமிக்க 'குறிக்கோள் தீர்மானத்தை' முன்மொழிந்த தலைவர் யார்?",
    [
        {"id": "A", "en": "Dr. B.R. Ambedkar", "ta": "டாக்டர் பி.ஆர். அம்பேத்கர்"},
        {"id": "B", "en": "Pandit Jawaharlal Nehru", "ta": "பண்டிட் ஜவஹர்லால் நேரு"},
        {"id": "C", "en": "Sardar Vallabhbhai Patel", "ta": "சர்தார் வல்லபாய் படேல்"},
        {"id": "D", "en": "Dr. Rajendra Prasad", "ta": "டாக்டர் ராஜேந்திர பிரசாத்"}
    ],
    "Pandit Jawaharlal Nehru moved the historic Objectives Resolution in the Constituent Assembly on December 13, 1946.",
    "பண்டித ஜவஹர்லால் நேரு டிசம்பர் 13, 1946 அன்று அரசியலமைப்பு அவையில் குறிக்கோள் தீர்மானத்தை முன்மொழிந்தார்."
))

# Q86 (C) - TNPSC Trap
gt_all_questions.append(make_q(
    86, "TNPSC Trap", "Hard", "C",
    "Which of the following pairs correctly distinguishes the occurrence of 'Economic' concepts in the Preamble?",
    "முகவுரையில் 'பொருளாதார' கருத்துக்கள் இடம்பெற்றுள்ளதன் சரியான வேறுபாட்டை பின்வரும் இணைகளில் எது சரியாகக் காட்டுகிறது?",
    [
        {"id": "A", "en": "Preamble contains 'Economic Liberty', but NO 'Economic Justice'", "ta": "முகவுரையில் 'பொருளாதார சுதந்திரம்' உள்ளது, ஆனால் 'பொருளாதார நீதி' இல்லை"},
        {"id": "B", "en": "Preamble contains both 'Economic Liberty' and 'Economic Equality'", "ta": "முகவுரையில் 'பொருளாதார சுதந்திரம்' மற்றும் 'பொருளாதார சமத்துவம்' ஆகிய இரண்டும் உள்ளன"},
        {"id": "C", "en": "Preamble contains 'Economic Justice', but NO 'Economic Liberty'", "ta": "முகவுரையில் 'பொருளாதார நீதி' உள்ளது, ஆனால் 'பொருளாதார சுதந்திரம்' இல்லை"},
        {"id": "D", "en": "Preamble contains neither 'Economic Justice' nor 'Economic Liberty'", "ta": "முகவுரையில் 'பொருளாதார நீதி' மற்றும் 'பொருளாதார சுதந்திரம்' ஆகிய இரண்டுமே இல்லை"}
    ],
    "TNPSC Trap Alert: The Preamble explicitly includes 'Economic Justice' (under Justice), but does NOT include 'Economic Liberty'.",
    "TNPSC பொறி எச்சரிக்கை: முகவுரையில் 'பொருளாதார நீதி' வெளிப்படையாக உள்ளது, ஆனால் 'பொருளாதார சுதந்திரம்' இல்லை."
))

# Q87 (D) - Direct MCQ
gt_all_questions.append(make_q(
    87, "Direct MCQ", "Easy", "D",
    "With which exact words does the Preamble of the Constitution of India begin?",
    "இந்திய அரசியலமைப்பின் முகவுரை எந்த துல்லியமான சொற்களுடன் தொடங்குகிறது?",
    [
        {"id": "A", "en": "'The Government of India'", "ta": "'இந்திய அரசாங்கம்'"},
        {"id": "B", "en": "'The Constituent Assembly of India'", "ta": "'இந்திய அரசியலமைப்பு நிர்ணய அவை'"},
        {"id": "C", "en": "'In the Name of God'", "ta": "'இறைவனின் பெயரால்'"},
        {"id": "D", "en": "'We, the People of India'", "ta": "'இந்திய மக்களாகிய நாம்'"}
    ],
    "The Preamble of the Constitution of India begins with the famous words: 'We, the People of India'.",
    "இந்திய அரசியலமைப்பின் முகவுரை 'இந்திய மக்களாகிய நாம்' என்ற புகழ்பெற்ற சொற்களுடன் தொடங்குகிறது."
))

# Q88 (A) - Conceptual
gt_all_questions.append(make_q(
    88, "Conceptual MCQ", "Medium", "A",
    "What is the underlying constitutional significance of the statement 'We, the People of India... do hereby adopt, enact and give to ourselves this Constitution'?",
    "'இந்திய மக்களாகிய நாம்... இந்த அரசியலமைப்பை ஏற்று, இயற்றி, நமக்கு நாமே வழங்கிக் கொள்கிறோம்' என்ற கூற்றின் பின்னணியில் உள்ள அரசியலமைப்பு முக்கியத்துவம் என்ன?",
    [
        {"id": "A", "en": "It affirms Popular Sovereignty—that the Constitution derives its authority from the people of India and not any external power", "ta": "இது மக்களின் இறையாண்மையை உறுதிப்படுத்துகிறது—அரசியலமைப்பு தனது அதிகாரத்தை எந்தவொரு வெளிச்சக்தியிலிருந்தும் பெறாமல் இந்திய மக்களிடமிருந்தே பெறுகிறது"},
        {"id": "B", "en": "It declares that only members of Constituent Assembly are bound by the Constitution", "ta": "அரசியலமைப்பு அவை உறுப்பினர்கள் மட்டுமே அரசியலமைப்புக்கு கட்டுப்பட்டவர்கள் என்று அது அறிவிக்கிறது"},
        {"id": "C", "en": "It gives Parliament absolute power to rewrite the Constitution without public elections", "ta": "பொதுத் தேர்தல்கள் இன்றி அரசியலமைப்பை மீண்டும் எழுத நாடாளுமன்றத்திற்கு அது முழு அதிகாரம் அளிக்கிறது"},
        {"id": "D", "en": "It signifies that India is a unitary monarchy under the President", "ta": "இந்தியா குடியரசுத் தலைவரின் கீழ் உள்ள ஒற்றையாட்சி முடியாட்சி என்பதை அது குறிக்கிறது"}
    ],
    "The opening and closing phrases together establish that ultimate sovereignty lies with the people of India.",
    "தொடக்க மற்றும் இறுதிச் சொற்றொடர்கள் இரண்டும் இணைந்து இறுதி இறையாண்மை இந்திய மக்களிடமே உள்ளது என்பதை நிறுவுகின்றன."
))

# Q89 (B) - Statement-Based
gt_all_questions.append(make_q(
    89, "Statement-Based", "Medium", "B",
    "Consider the following statements regarding the international influences on the Preamble:\n1. The ideal of Justice (social, economic, and political) was inspired by the 1917 Russian Revolution.\n2. The ideals of Liberty, Equality, and Fraternity were inspired by the 1789 French Revolution.\nWhich of the statements given above are CORRECT?",
    "முகவுரையின் மீதான சர்வதேச தாக்கங்கள் பற்றிய பின்வரும் கூற்றுகளைக் ஆராய்க:\n1. நீதி (சமூக, பொருளாதார, அரசியல்) என்ற இலட்சியம் 1917 ரஷ்யப் புரட்சியால் ஈர்க்கப்பட்டது.\n2. சுதந்திரம், சமத்துவம், சகோதரத்துவம் என்ற இலட்சியங்கள் 1789 பிரெஞ்சுப் புரட்சியால் ஈர்க்கப்பட்டன.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எவை சரியானவை?",
    [
        {"id": "A", "en": "1 only", "ta": "1 மட்டுமே"},
        {"id": "B", "en": "Both 1 and 2", "ta": "1 மற்றும் 2 இரண்டும்"},
        {"id": "C", "en": "2 only", "ta": "2 மட்டுமே"},
        {"id": "D", "en": "Neither 1 nor 2", "ta": "1-ம் இல்லை 2-ம் இல்லை"}
    ],
    "Both statements 1 and 2 are CORRECT. Justice came from the 1917 Russian Revolution, while Liberty, Equality, Fraternity came from the 1789 French Revolution.",
    "கூற்றுகள் 1 மற்றும் 2 இரண்டும் சரியானவை. நீதி 1917 ரஷ்யப் புரட்சியிலிருந்தும், சுதந்திரம்/சமத்துவம்/சகோதரத்துவம் 1789 பிரெஞ்சுப் புரட்சியிலிருந்தும் பெறப்பட்டன."
))

# Q90 (C) - Hard Analytical
gt_all_questions.append(make_q(
    90, "Hard Analytical", "Hard", "C",
    "Which of the following correctly synthesizes the five keywords describing the Nature of the Indian State (Sovereign, Socialist, Secular, Democratic, Republic)?",
    "இந்திய அரசின் தன்மையை விவரிக்கும் ஐந்து முக்கியச் சொற்களை (இறையாண்மை, சமதர்ம, மதச்சார்பற்ற, ஜனநாயக, குடியரசு) பின்வருவனவற்றில் எது சரியாகத் தொகுத்துக் கூறுகிறது?",
    [
        {"id": "A", "en": "India is an autocracy under military command with state-mandated religion", "ta": "இந்தியா என்பது அரசு ஆணையிட்ட மதத்துடன் ராணுவக் கட்டுப்பாட்டில் உள்ள ஒரு சர்வாதிகார நாடாகும்"},
        {"id": "B", "en": "India is a dominion under the British Crown with a capitalist economy", "ta": "இந்தியா என்பது முதலாளித்துவ பொருளாதாரத்துடன் பிரிட்டிஷ் மகுடத்தின் கீழ் உள்ள ஒரு டொமினியன் ஆகும்"},
        {"id": "C", "en": "India is an independent state free from external control, aiming for a welfare mixed economy, giving equal respect to all religions, governed by elected representatives of the people, with an elected Head of State", "ta": "இந்தியா வெளிநாட்டுக் கட்டுப்பாடற்ற சுதந்திரமான அரசு, நலக் கலப்புப் பொருளாதாரத்தை நோக்கமாகக் கொண்டு, அனைத்து மதங்களுக்கும் சம மரியாதை அளித்து, மக்களால் தேர்ந்தெடுக்கப்பட்ட பிரதிநிதிகளால் ஆளப்பட்டு, தேர்ந்தெடுக்கப்பட்ட நாட்டின் தலைவரைக் கொண்டுள்ளது"},
        {"id": "D", "en": "India is a unitary dictatorship where states have no independent identity", "ta": "இந்தியா என்பது மாநிலங்களுக்கு சுயாதீன அடையாளமே இல்லாத ஒரு ஒற்றையாட்சி சர்வாதிகார நாடாகும்"}
    ],
    "The 5 keywords together define a fully independent, welfare-oriented, multi-religious, representative democratic republic.",
    "இந்த 5 சொற்களும் இணைந்து முழு சுதந்திரமான, நல சார்ந்த, பல மதங்கள் கொண்ட, பிரதிநிதித்துவ ஜனநாயகக் குடியரசை வரையறுக்கின்றன."
))

# Q91 (A) - Reasoning
gt_all_questions.append(make_q(
    91, "Assertion & Reason", "Hard", "A",
    "Assertion (A): In Kesavananda Bharati (1973), the Supreme Court explicitly held that the Preamble CAN be amended under Article 368.\nReason (R): The Preamble is a part of the Constitution, and Parliament's constituent amending power extends to all parts of the Constitution subject to the Basic Structure limitation.",
    "கூற்று (A): கேசவானந்த பாரதி வழக்கில் (1973), உறுப்பு 368-ன் கீழ் முகவுரையைத் திருத்த முடியும் என்று உச்ச நீதிமன்றம் வெளிப்படையாகத் தீர்ப்பளித்தது.\nகாரணம் (R): முகவுரை அரசியலமைப்பின் ஒரு பகுதியாகும், மேலும் நாடாளுமன்றத்தின் அரசியலமைப்புத் திருத்தும் அதிகாரம் அடிப்படை கட்டமைப்பு வரம்பிற்கு உட்பட்டு அரசியலமைப்பின் அனைத்துப் பகுதிகளுக்கும் பொருந்தும்.",
    [
        {"id": "A", "en": "Both A and R are true and R is the correct explanation of A", "ta": "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்"},
        {"id": "B", "en": "Both A and R are true but R is NOT the correct explanation of A", "ta": "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல"},
        {"id": "C", "en": "A is true but R is false", "ta": "A சரி, ஆனால் R தவறு"},
        {"id": "D", "en": "A is false but R is true", "ta": "A தவறு, ஆனால் R சரி"}
    ],
    "Both A and R are true, and R correctly explains A. Because Preamble is part of Constitution, it can be amended under Art 368 subject to Basic Structure.",
    "A மற்றும் R இரண்டும் சரி, R என்பது A விற்கு சரியான விளக்கமாகும். முகவுரை அரசியலமைப்பின் ஒரு பகுதி என்பதால் உறுப்பு 368-ன் கீழ் திருத்தப்படலாம்."
))

# Q92 (D) - Match the Following
gt_all_questions.append(make_q(
    92, "Match the Following", "Hard", "D",
    "Match List I (Eminent Scholars) with List II (Key Metaphors used for Preamble):\n\nList I\nA. N.A. Palkhivala\nB. Dr. K.M. Munshi\nC. Pandit Thakur Das Bhargava\nD. Sir Ernest Barker\n\nList II\n1. Key-note to the Constitution\n2. Soul of the Constitution & Jewel set in the Constitution\n3. Horoscope of our Sovereign Democratic Republic\n4. Identity Card of the Constitution",
    "பட்டியல் I-ஐ (புகழ்பெற்ற அறிஞர்கள்) பட்டியல் II உடன் (முகவுரைக்குப் பயன்படுத்திய முக்கிய உருவகங்கள்) பொருத்தி சரியான பதிலதைத் தேர்ந்தெடுக்கவும்:\n\nபட்டியல் I\nA. என்.ஏ. பல்கிவாலா\nB. டாக்டர் கே.எம். முன்ஷி\nC. பண்டிட் தாக்கூர் தாஸ் பார்கவா\nD. சர் எர்னஸ்ட் பார்கர்\n\nபட்டியல் II\n1. அரசியலமைப்பின் முக்கிய குறிப்பு (Key-note)\n2. அரசியலமைப்பின் ஆன்மா & பதிக்கப்பட்ட ஆபரணம்\n3. நமது இறையாண்மை கொண்ட ஜனநாயக குடியரசின் ஜாதகம்\n4. அரசியலமைப்பின் அடையாள அட்டை",
    [
        {"id": "A", "en": "A-4, B-1, C-2, D-3", "ta": "A-4, B-1, C-2, D-3"},
        {"id": "B", "en": "A-3, B-4, C-2, D-1", "ta": "A-3, B-4, C-2, D-1"},
        {"id": "C", "en": "A-4, B-3, C-1, D-2", "ta": "A-4, B-3, C-1, D-2"},
        {"id": "D", "en": "A-4, B-3, C-2, D-1", "ta": "A-4, B-3, C-2, D-1"}
    ],
    "Correct Match: A-4 (Palkhivala = Identity Card), B-3 (Munshi = Horoscope), C-2 (Bhargava = Soul & Jewel), D-1 (Barker = Key-note).",
    "சரியான பொருத்தம்: A-4 (பல்கிவாலா = அடையாள அட்டை), B-3 (முன்ஷி = ஜாதகம்), C-2 (பார்கவா = ஆன்மா & ஆபரணம்), D-1 (பார்கர் = முக்கிய குறிப்பு)."
))

# Q93 (A) - Chronology
gt_all_questions.append(make_q(
    93, "Chronology", "Medium", "A",
    "Arrange the following early Supreme Court decisions involving judicial interpretation of Preamble/Fundamental Rights in correct chronological order:\n1. In re Berubari Union Reference\n2. Sajjan Singh v. State of Rajasthan\n3. Golak Nath v. State of Punjab\n4. Kesavananda Bharati v. State of Kerala",
    "முகவுரை/அடிப்படை உரிமைகள் பற்றிய நீதித்துறை விளக்கங்களை உள்ளடக்கிய பின்வரும் ஆரம்பகால உச்ச நீதிமன்றத் தீர்ப்புகளை சரியான காலவரிசையில் அமைக்கவும்:\n1. பெருபாரி யூனியன் வழக்கு\n2. சஜ்ஜன் சிங் எதிர் ராஜஸ்தான் மாநிலம்\n3. கோலக் நாத் எதிர் பஞ்சாப் மாநிலம்\n4. கேசவானந்த பாரதி எதிர் கேரளா மாநிலம்",
    [
        {"id": "A", "en": "1 -> 2 -> 3 -> 4", "ta": "1 -> 2 -> 3 -> 4"},
        {"id": "B", "en": "2 -> 1 -> 3 -> 4", "ta": "2 -> 1 -> 3 -> 4"},
        {"id": "C", "en": "1 -> 3 -> 2 -> 4", "ta": "1 -> 3 -> 2 -> 4"},
        {"id": "D", "en": "1 -> 2 -> 4 -> 3", "ta": "1 -> 2 -> 4 -> 3"}
    ],
    "Chronological Sequence: 1 (Berubari: 1960) -> 2 (Sajjan Singh: 1965) -> 3 (Golak Nath: 1967) -> 4 (Kesavananda Bharati: 1973).",
    "காலவரிசை: 1 (பெருபாரி: 1960) -> 2 (சஜ்ஜன் சிங்: 1965) -> 3 (கோலக் நாத்: 1967) -> 4 (கேசவானந்த பாரதி: 1973)."
))

# Q94 (B) - PYQ Pattern
gt_all_questions.append(make_q(
    94, "Direct PYQ Pattern", "Easy", "B",
    "How many new words were inserted into the Preamble of the Constitution of India by the 42nd Amendment Act of 1976?",
    "1976-ன் 42வது திருத்தச் சட்டத்தின் மூலம் இந்திய அரசியலமைப்பின் முகவுரையில் எத்தனை புதிய சொற்கள் சேர்க்கப்பட்டன?",
    [
        {"id": "A", "en": "Two words (Socialist, Secular)", "ta": "இரண்டு சொற்கள் (சமதர்ம, மதச்சார்பற்ற)"},
        {"id": "B", "en": "Three words (Socialist, Secular, Integrity)", "ta": "மூன்று சொற்கள் (சமதர்ம, மதச்சார்பற்ற, ஒருமைப்பாடு)"},
        {"id": "C", "en": "Four words (Socialist, Secular, Integrity, Republic)", "ta": "நான்கு சொற்கள் (சமதர்ம, மதச்சார்பற்ற, ஒருமைப்பாடு, குடியரசு)"},
        {"id": "D", "en": "One word (Secular)", "ta": "ஒரே ஒரு சொல் (மதச்சார்பற்ற)"}
    ],
    "The 42nd Amendment Act 1976 added THREE words to the Preamble: 'Socialist', 'Secular', and 'Integrity'.",
    "42வது திருத்தச் சட்டம் 1976 முகவுரையில் மூன்று சொற்களைச் சேர்த்தது: சமதர்ம, மதச்சார்பற்ற, ஒருமைப்பாடு."
))

# Q95 (C) - TNPSC Trap
gt_all_questions.append(make_q(
    95, "TNPSC Trap", "Hard", "C",
    "Has the Preamble of the Constitution of India been amended twice or thrice since 1950?",
    "1950 முதல் இந்திய அரசியலமைப்பின் முகவுரை இரண்டு அல்லது மூன்று முறை திருத்தப்பட்டுள்ளதா?",
    [
        {"id": "A", "en": "Yes, twice (in 1976 and 1978)", "ta": "ஆம், இரண்டு முறை (1976 மற்றும் 1978 இல்)"},
        {"id": "B", "en": "Yes, thrice (in 1951, 1976, and 2002)", "ta": "ஆம், மூன்று முறை (1951, 1976 மற்றும் 2002 இல்)"},
        {"id": "C", "en": "No, the Preamble has been amended ONLY ONCE (by 42nd Amendment Act 1976)", "ta": "இல்லை, முகவுரை ஒரே ஒரு முறை மட்டுமே திருத்தப்பட்டுள்ளது (1976-ன் 42வது திருத்தச் சட்டத்தால்)"},
        {"id": "D", "en": "Yes, every time a new State is created", "ta": "ஆம், ஒவ்வொரு முறையும் புதிய மாநிலம் உருவாக்கப்படும் போது"}
    ],
    "TNPSC Trap Alert: The Preamble has been amended ONLY ONCE in Indian constitutional history (42nd CAA, 1976).",
    "TNPSC பொறி எச்சரிக்கை: இந்திய அரசியலமைப்பு வரலாற்றில் முகவுரை ஒரே ஒரு முறை மட்டுமே திருத்தப்பட்டுள்ளது (42வது திருத்தம் 1976)."
))

# Q96 (D) - Direct MCQ
gt_all_questions.append(make_q(
    96, "Direct MCQ", "Easy", "D",
    "Which of the following three words was inserted alongside 'Socialist' and 'Secular' by the 42nd Amendment Act of 1976?",
    "1976-ன் 42வது திருத்தச் சட்டத்தின் மூலம் 'சமதர்ம' மற்றும் 'மதச்சார்பற்ற' ஆகியவற்றுடன் சேர்க்கப்பட்ட மூன்றாவது சொல் எது?",
    [
        {"id": "A", "en": "Sovereignty", "ta": "இறையாண்மை"},
        {"id": "B", "en": "Fraternity", "ta": "சகோதரத்துவம்"},
        {"id": "C", "en": "Republic", "ta": "குடியரசு"},
        {"id": "D", "en": "Integrity", "ta": "ஒருமைப்பாடு"}
    ],
    "The three words inserted by the 42nd Amendment Act 1976 were: Socialist, Secular, and Integrity.",
    "42வது திருத்தச் சட்டம் 1976 மூலம் சேர்க்கப்பட்ட மூன்று சொற்கள்: சமதர்ம, மதச்சார்பற்ற, ஒருமைப்பாடு."
))

# Q97 (A) - Conceptual
gt_all_questions.append(make_q(
    97, "Conceptual MCQ", "Medium", "A",
    "What does 'Fraternity' fundamentally promote among citizens according to the Preamble?",
    "முகவுரையின் படி 'சகோதரத்துவம்' குடிமக்களிடையே அடிப்படை ரீதியாக எதனை ஊக்குவிக்கிறது?",
    [
        {"id": "A", "en": "A sense of common brotherhood among all Indians transcending caste, linguistic, and regional diversities", "ta": "சாதி, மொழி மற்றும் பிராந்திய வேறுபாடுகளைக் கடந்து அனைத்து இந்தியர்களிடையேயும் பொதுவான சகோதரத்துவ உணர்வு"},
        {"id": "B", "en": "Compulsory membership in trade unions", "ta": "தொழிற்சங்கங்களில் கட்டாய உறுப்பினர் நிலை"},
        {"id": "C", "en": "Financial donations to political parties", "ta": "அரசியல் கட்சிகளுக்கு நிதி நன்கொடைகள்"},
        {"id": "D", "en": "Reservation of state jobs for blood relatives", "ta": "ரத்த சொந்தங்களுக்கு அரசுப் பணிகளில் இடஒதுக்கீடு"}
    ],
    "Fraternity promotes a spirit of common brotherhood among all citizens of India, transcending religious, linguistic, regional or sectional diversities.",
    "சகோதரத்துவம் என்பது மதம், மொழி, பிராந்திய வேறுபாடுகளைக் கடந்து அனைத்து இந்தியர்களிடையேயும் பொதுவான சகோதர உணர்வை வளர்க்கிறது."
))

# Q98 (B) - Statement-Based
gt_all_questions.append(make_q(
    98, "Statement-Based", "Hard", "B",
    "Consider the following comprehensive statements regarding the Preamble of the Indian Constitution:\n1. It is based on the Objectives Resolution drafted and moved by Pandit Jawaharlal Nehru.\n2. It was enacted by the Constituent Assembly on October 17, 1949 after the rest of the Constitution was passed.\n3. It was held to be an integral part of the Constitution in Kesavananda Bharati case (1973).\nWhich of the statements given above are CORRECT?",
    "இந்திய அரசியலமைப்பின் முகவுரை பற்றிய பின்வரும் விரிவான கூற்றுகளைக் ஆராய்க:\n1. இது பண்டித ஜவஹர்லால் நேருவால் வரைவு செய்யப்பட்டு முன்மொழியப்பட்ட குறிக்கோள் தீர்மானத்தை அடிப்படையாகக் கொண்டது.\n2. அரசியலமைப்பின் மற்ற பகுதிகள் நிறைவேற்றப்பட்ட பிறகு, அக்டோபர் 17, 1949 அன்று அரசியலமைப்பு அவையால் இயற்றப்பட்டது.\n3. கேசவானந்த பாரதி வழக்கில் (1973) இது அரசியலமைப்பின் ஒரு ஒருங்கிணைந்த பகுதி எனத் தீர்ப்பளிப்பப்பட்டது.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எவை சரியானவை?",
    [
        {"id": "A", "en": "1 and 2 only", "ta": "1 மற்றும் 2 மட்டுமே"},
        {"id": "B", "en": "1, 2 and 3", "ta": "1, 2 மற்றும் 3"},
        {"id": "C", "en": "2 and 3 only", "ta": "2 மற்றும் 3 மட்டுமே"},
        {"id": "D", "en": "1 and 3 only", "ta": "1 மற்றும் 3 மட்டுமே"}
    ],
    "All three statements (1, 2, and 3) are CORRECT and accurately reflect the historical origin, enactment timing, and judicial status of the Preamble.",
    "மூன்று கூற்றுகளும் (1, 2 மற்றும் 3) சரியானவை மற்றும் முகவுரையின் தோற்றம், இயற்றப்பட்ட நேரம், நீதித்துறை அந்தஸ்தைப் பிரதிபலிக்கின்றன."
))

# Q99 (C) - Hard Analytical
gt_all_questions.append(make_q(
    99, "Hard Analytical", "Hard", "C",
    "Which of the following correctly explains the distinction between Preamble being 'part of the Constitution' versus Preamble being 'justiciable'?",
    "முகவுரை 'அரசியலமைப்பின் ஒரு பகுதி' என்பதற்கும் முகவுரை 'நீதிமன்றத்தால் நிலைநிறுத்தக்கூடியது' என்பதற்கும் இடையிலான வேறுபாட்டை பின்வருவனவற்றில் எது சரியாக விவரிக்கிறது?",
    [
        {"id": "A", "en": "Being part of Constitution means it can be enforced in court, while non-justiciable means it cannot be amended", "ta": "அரசியலமைப்பின் ஒரு பகுதி என்றால் நீதிமன்றத்தில் அமல்படுத்தலாம், நிலைநிறுத்த முடியாது என்றால் திருத்த முடியாது"},
        {"id": "B", "en": "Being part of Constitution applies only to High Courts, while justiciability applies only to Supreme Court", "ta": "அரசியலமைப்பின் ஒரு பகுதி என்பது உயர் நீதிமன்றங்களுக்கு மட்டுமே பொருந்தும், நிலைநிறுத்துதல் உச்ச நீதிமன்றத்திற்கு பொருந்தும்"},
        {"id": "C", "en": "Being part of Constitution (Kesavananda 1973) means it is subject to Art 368 amendment & forms part of Basic Structure; Non-justiciable means its provisions cannot be directly enforced in a court of law to obtain remedies", "ta": "அரசியலமைப்பின் ஒரு பகுதி (கேசவானந்தா 1973) என்றால் அது உறுப்பு 368 திருத்தத்திற்கு உட்பட்டது & அடிப்படை கட்டமைப்பின் பகுதி; நிலைநிறுத்த முடியாது என்றால் அதன் விதிகளை நேரடியாக நீதிமன்றத்தில் அமல்படுத்த முடியாது"},
        {"id": "D", "en": "There is no distinction between the two concepts", "ta": "இரண்டு கருத்துக்களுக்கும் இடையே எந்த வேறுபாடும் இல்லை"}
    ],
    "Being part of the Constitution allows Art 368 amendment & Basic Structure inclusion; being non-justiciable means its provisions cannot be enforced in courts directly for legal remedies.",
    "அரசியலமைப்பின் பகுதி என்பது உறுப்பு 368 திருத்தம் & அடிப்படை கட்டமைப்பிற்கு உட்பட்டது; நிலைநிறுத்த முடியாது என்றால் நேரடியாக நீதிமன்றத்தில் வழக்கு தொடர முடியாது."
))

# Q100 (D) - Grand Synthesis MCQ
gt_all_questions.append(make_q(
    100, "Grand Synthesis MCQ", "Medium", "D",
    "What is the complete four-fold purpose served by the Preamble of the Constitution of India?",
    "இந்திய அரசியலமைப்பின் முகவுரை நிறைவேற்றும் முழுமையான நான்கு அம்ச நோக்கம் என்ன?",
    [
        {"id": "A", "en": "Listing the names of all 28 States, Union Territories, High Courts, and Cabinet Ministers", "ta": "அனைத்து 28 மாநிலங்கள், யூனியன் பிரதேசங்கள், உயர் நீதிமன்றங்கள் மற்றும் அமைச்சர்களின் பெயர்களைப் பட்டியலிடுவது"},
        {"id": "B", "en": "Defining the tax revenue share between Centre and States for five years", "ta": "ஐந்து ஆண்டுகளுக்கு மத்திய மற்றும் மாநில அரசுகளுக்கு இடையேயான வரி வருவாய் பங்கீட்டை வரையறுப்பது"},
        {"id": "C", "en": "Enumerating the Emergency powers, President's rule, and Financial Emergency rules", "ta": "அவசரநிலை அதிகாரங்கள், குடியரசுத் தலைவர் ஆட்சி மற்றும் நிதி அவசரநிலை விதிகளைப் பட்டியலிடுவது"},
        {"id": "D", "en": "Declaring the Source of Authority (People), Nature of Indian State (S-S-S-D-R), Core Objectives (J-L-E-F), and Date of Adoption (Nov 26, 1949)", "ta": "அதிகாரத்தின் மூலம் (மக்கள்), இந்திய அரசின் தன்மை (இ-ச-ம-ஜ-கு), முக்கிய குறிக்கோள்கள் (நீ-சு-ச-ச), மற்றும் ஏற்றுக்கொள்ளப்பட்ட தேதியை (நவம்பர் 26, 1949) அறிவிப்பது"}
    ],
    "The Preamble serves 4-fold purpose: 1. Source of Authority, 2. Nature of State, 3. Objectives, 4. Date of Adoption (Nov 26, 1949).",
    "முகவுரை 4 முக்கிய நோக்கங்களை நிறைவேற்றுகிறது: 1. அதிகாரத்தின் மூலம், 2. அரசின் தன்மை, 3. குறிக்கோள்கள், 4. ஏற்றுக்கொள்ளப்பட்ட தேதி (நவம்பர் 26, 1949)."
))

print(f"Total questions compiled: {len(gt_all_questions)}")

target_file = "data/questions/polity/preamble_grand_test.json"
os.makedirs(os.path.dirname(target_file), exist_ok=True)

with open(target_file, "w", encoding="utf-8") as f:
    json.dump(gt_all_questions, f, ensure_ascii=False, indent=2)

print(f"Successfully generated 100 Grand Test questions in '{target_file}'!")
