# -*- coding: utf-8 -*-
"""
Full Dataset Generator for 100 TNPSC Group 1 Standard Grand Test MCQs
Topic: Preamble of the Constitution of India
Target File: data/questions/polity/preamble_grand_test.json
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

from build_full_100_preamble_gt import make_q

questions = []

# =============================================================================
# BLOCK 1: Questions 1 to 25
# =============================================================================

# Q1 (C) - Direct MCQ
questions.append(make_q(
    1, "Direct MCQ", "Easy", "C",
    "Which date is explicitly mentioned in the Preamble of the Constitution of India as the date of its adoption and enactment?",
    "இந்திய அரசியலமைப்பின் முகவுரையில் அரசியலமைப்பு ஏற்றுக்கொள்ளப்பட்ட மற்றும் இயற்றப்பட்ட நாளாக வெளிப்படையாகக் குறிப்பிடப்பட்டுள்ள தேதி எது?",
    [
        {"id": "A", "en": "26th January 1950", "ta": "26 ஜனவரி 1950"},
        {"id": "B", "en": "15th August 1947", "ta": "15 ஆகஸ்ட் 1947"},
        {"id": "C", "en": "26th November 1949", "ta": "26 நவம்பர் 1949"},
        {"id": "D", "en": "9th December 1946", "ta": "9 டிசம்பர் 1946"}
    ],
    "The Preamble explicitly mentions 26th November 1949 as the date of adoption, enactment, and giving to ourselves the Constitution.",
    "முகவுரை 26 நவம்பர் 1949 ஆம் தேதியை அரசியலமைப்பு ஏற்றுக்கொள்ளப்பட்ட மற்றும் இயற்றப்பட்ட நாளாக வெளிப்படையாகக் குறிப்பிடுகிறது."
))

# Q2 (A) - Conceptual
questions.append(make_q(
    2, "Conceptual MCQ", "Easy", "A",
    "The doctrine of 'Popular Sovereignty' in the Indian Constitution is explicitly reflected in which opening phrase of the Preamble?",
    "இந்திய அரசியலமைப்பில் 'மக்களின் இறையாண்மை' என்ற கோட்பாடு முகவுரையின் எந்தத் தொடக்கச் சொற்றொடரில் வெளிப்படையாகப் பிரதிபலிக்கிறது?",
    [
        {"id": "A", "en": "'We, the People of India'", "ta": "'இந்திய மக்களாகிய நாம்'"},
        {"id": "B", "en": "'Sovereign Socialist Secular'", "ta": "'இறையாண்மை சமதர்ம மதச்சார்பற்ற'"},
        {"id": "C", "en": "'In our Constituent Assembly'", "ta": "'நமது அரசியலமைப்பு நிர்ணய அவையில்'"},
        {"id": "D", "en": "'Give to ourselves this Constitution'", "ta": "'நமக்கு நாமே இந்த அரசியலமைப்பை வழங்கிக் கொள்கிறோம்'"}
    ],
    "The phrase 'We, the People of India' signifies Popular Sovereignty—that all authority of the Constitution is derived directly from the citizens of India.",
    "'இந்திய மக்களாகிய நாம்' என்ற சொற்றொடர் மக்களின் இறையாண்மையைக் குறிக்கிறது; அரசியலமைப்பின் அனைத்து அதிகாரங்களும் இந்திய மக்களிடமிருந்தே பெறப்படுகின்றன."
))

# Q3 (B) - Statement-Based
questions.append(make_q(
    3, "Statement-Based", "Medium", "B",
    "Consider the following statements regarding the 42nd Constitutional Amendment Act of 1976:\n1. It inserted the words 'Socialist', 'Secular', and 'Integrity' into the Preamble.\n2. It substituted the phrase 'Unity of the Nation' with 'Unity and Integrity of the Nation'.\n3. It was enacted based on the recommendations of the Sarkaria Commission.\nWhich of the statements given above are CORRECT?",
    "1976 ஆம் ஆண்டின் 42வது அரசியலமைப்புத் திருத்தச் சட்டம் பற்றிய பின்வரும் கூற்றுகளைக் ஆராய்க:\n1. இது 'சமதர்ம', 'மதச்சார்பற்ற' மற்றும் 'ஒருமைப்பாடு' ஆகிய சொற்களை முகவுரையில் சேர்த்தது.\n2. இது 'நாட்டின் ஒற்றுமை' என்ற தொடருக்குப் பதிலாக 'நாட்டின் ஒற்றுமை மற்றும் ஒருமைப்பாடு' என மாற்றியது.\n3. இது சர்க்காரியா ஆணையத்தின் பரிந்துரைகளின் அடிப்படையில் இயற்றப்பட்டது.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எவை சரியானவை?",
    [
        {"id": "A", "en": "1 and 3 only", "ta": "1 மற்றும் 3 மட்டுமே"},
        {"id": "B", "en": "1 and 2 only", "ta": "1 மற்றும் 2 மட்டுமே"},
        {"id": "C", "en": "2 and 3 only", "ta": "2 மற்றும் 3 மட்டுமே"},
        {"id": "D", "en": "1, 2 and 3", "ta": "1, 2 மற்றும் 3"}
    ],
    "Statements 1 and 2 are CORRECT. Statement 3 is INCORRECT because the 42nd Amendment was enacted based on the Swaran Singh Committee recommendations (1976), not Sarkaria Commission.",
    "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது; ஏனெனில் 42வது திருத்தம் சர்க்காரியா ஆணையத்திற்குப் பதிலாக சுரன் சிங் குழுவின் பரிந்துரைகளின் அடிப்படையில் இயற்றப்பட்டது."
))

# Q4 (D) - Hard Analytical
questions.append(make_q(
    4, "Hard Analytical", "Hard", "D",
    "Which of the following correctly describes the constitutional boundary of Parliament's power to amend the Preamble under Article 368 as established in Kesavananda Bharati case (1973)?",
    "கேசவானந்த பாரதி வழக்கில் (1973) நிறுவப்பட்டபடி, உறுப்பு 368-ன் கீழ் முகவுரையைத் திருத்துவதற்கான நாடாளுமன்றத்தின் அதிகாரத்தின் அரசியலமைப்பு வரம்பை பின்வருவனவற்றில் எது சரியாக விவரிக்கிறது?",
    [
        {"id": "A", "en": "Parliament cannot amend the Preamble under any circumstances as it is not a part of the Constitution", "ta": "முகவுரை அரசியலமைப்பின் ஒரு பகுதி அல்ல என்பதால் நாடாளுமன்றம் எந்தச் சூழ்நிலையிலும் அதைத் திருத்த முடியாது"},
        {"id": "B", "en": "Parliament has absolute sovereign power to delete any word or provision from the Preamble without judicial review", "ta": "நீதிமன்ற ஆய்வின்றி முகவுரையிலிருந்து எந்தவொரு சொல்லையோ விதியையோ நீக்க நாடாளுமன்றத்திற்கு முழுமையான இறையாண்மை அதிகாரம் உள்ளது"},
        {"id": "C", "en": "Preamble can be amended only by a simple majority like ordinary legislation", "ta": "சாதாரணச் சட்டத்தைப் போல சாதாரண பெரும்பான்மையால் மட்டுமே முகவுரையைத் திருத்த முடியும்"},
        {"id": "D", "en": "Parliament can amend the Preamble under Article 368, provided the 'Basic Features' or basic structure contained in it are not damaged or destroyed", "ta": "முகவுரையில் உள்ள 'அடிப்படை அம்சங்கள்' அல்லது அடிப்படை கட்டமைப்பு சேதமடையாமலும் அழிக்கப்படாமலும் இருக்கும் வரம்பிற்கு உட்பட்டு நாடாளுமன்றம் உறுப்பு 368-ன் கீழ் முகவுரையைத் திருத்தலாம்"}
    ],
    "In Kesavananda Bharati (1973), the Supreme Court ruled that Parliament can amend the Preamble under Article 368, but cannot alter or destroy its Basic Features.",
    "கேசவானந்த பாரதி வழக்கில் (1973), அடிப்படை அம்சங்கள் சேதமடையாத வரம்பிற்கு உட்பட்டு நாடாளுமன்றம் உறுப்பு 368-ன் கீழ் முகவுரையைத் திருத்தலாம் என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது."
))

# Q5 (A) - Reasoning
questions.append(make_q(
    5, "Assertion & Reason", "Hard", "A",
    "Assertion (A): India's continued membership of the Commonwealth of Nations does not compromise its constitutional sovereignty proclaimed in the Preamble.\nReason (R): Commonwealth membership is an extra-constitutional voluntary declaration that can be terminated at India's own free will.",
    "கூற்று (A): காமன்வெல்த் நாடுகளின் கூட்டமைப்பில் இந்தியா தொடர்ந்து உறுப்பினராக இருப்பது முகவுரையில் பிரகடனப்படுத்தப்பட்ட அதன் அரசியலமைப்பு இறையாண்மையைப் பாதிக்காது.\nகாரணம் (R): காமன்வெல்த் உறுப்பினர் நிலை என்பது அரசியலமைப்புக்கு அப்பாற்பட்ட ஒரு தன்னார்வப் பிரகடனமாகும், இது இந்தியாவின் சொந்த விருப்பத்தின் பேரில் ரத்து செய்யப்படலாம்.",
    [
        {"id": "A", "en": "Both A and R are true and R is the correct explanation of A", "ta": "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்"},
        {"id": "B", "en": "Both A and R are true but R is NOT the correct explanation of A", "ta": "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல"},
        {"id": "C", "en": "A is true but R is false", "ta": "A சரி, ஆனால் R தவறு"},
        {"id": "D", "en": "A is false but R is true", "ta": "A தவறு, ஆனால் R சரி"}
    ],
    "Both A and R are true, and R correctly explains A. India's association with the Commonwealth is voluntary and does not impair its external or internal sovereignty.",
    "A மற்றும் R இரண்டும் சரி, R என்பது A விற்கு சரியான விளக்கமாகும். காமன்வெல்த் கூட்டமைப்புடனான இந்தியாவின் உறவு தன்னார்வமானது, அது இறையாண்மையைக் குறைக்காது."
))

# Q6 (B) - Match the Following
questions.append(make_q(
    6, "Match the Following", "Medium", "B",
    "Match List I (Preamble Terms) with List II (Constitutional Meanings) and select the correct answer using the codes given below:\n\nList I\nA. Sovereign\nB. Socialist\nC. Secular\nD. Republic\n\nList II\n1. Equal status, respect, and state protection for all religions\n2. Supreme internal authority and complete independence from foreign control\n3. Head of the State is elected for a fixed term and not a hereditary monarch\n4. Democratic mixed economy aiming to eliminate poverty and inequalities",
    "பட்டியல் I-ஐ (முகப்புரைச் சொற்கள்) பட்டியல் II உடன் (அரசியலமைப்புப் பொருள்கள்) பொருத்தி கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளைப் பயன்படுத்தி சரியான பதிலைத் தேர்ந்தெடுக்கவும்:\n\nபட்டியல் I\nA. இறையாண்மை\nB. சமதர்ம\nC. மதச்சார்பற்ற\nD. குடியரசு\n\nபட்டியல் II\n1. அனைத்து மதங்களுக்கும் சமமான அந்தஸ்து, மரியாதை மற்றும் அரசு ஆதரவு\n2. வெளிநாட்டுக் கட்டுப்பாடின்மை மற்றும் நாட்டின் உச்ச வரம்பற்ற உள்நாட்டு அதிகாரம்\n3. நாட்டின் தலைவர் ஒரு குறிப்பிட்ட காலத்திற்கு தேர்ந்தெடுக்கப்படுபவர், வம்சாவளி மன்னர் அல்ல\n4. வறுமை மற்றும் சமத்துவமின்மைகளை அகற்றும் ஜனநாயகக் கலப்புப் பொருளாதாரம்",
    [
        {"id": "A", "en": "A-1, B-4, C-2, D-3", "ta": "A-1, B-4, C-2, D-3"},
        {"id": "B", "en": "A-2, B-4, C-1, D-3", "ta": "A-2, B-4, C-1, D-3"},
        {"id": "C", "en": "A-2, B-1, C-4, D-3", "ta": "A-2, B-1, C-4, D-3"},
        {"id": "D", "en": "A-4, B-2, C-1, D-3", "ta": "A-4, B-2, C-1, D-3"}
    ],
    "Correct Matching: A-2 (Sovereign = Supreme internal authority & foreign independence), B-4 (Socialist = Democratic mixed economy), C-1 (Secular = Equal status/respect for all religions), D-3 (Republic = Elected head of state).",
    "சரியான பொருத்தம்: A-2 (இறையாண்மை = உச்ச அதிகாரம்), B-4 (சமதர்ம = கலப்புப் பொருளாதாரம்), C-1 (மதச்சார்பற்ற = அனைத்து மதங்களுக்கும் சம மரியாதை), D-3 (குடியரசு = தேர்ந்தெடுக்கப்பட்ட நாட்டின் தலைவர்)."
))

# Q7 (C) - Chronology
questions.append(make_q(
    7, "Chronology", "Medium", "C",
    "Arrange the following historical milestones relating to the origin and enforcement of the Preamble in correct chronological order:\n1. Objectives Resolution adopted by the Constituent Assembly\n2. Objectives Resolution moved by Jawaharlal Nehru in the Constituent Assembly\n3. Preamble voted and enacted by the Constituent Assembly\n4. Constitution of India and Preamble came into full force",
    "முகவுரையின் தோற்றம் மற்றும் அமலாக்கம் தொடர்பான பின்வரும் வரலாற்று மைல்கற்களை சரியான காலவரிசையில் அமைக்கவும்:\n1. அரசியலமைப்பு நிர்ணய அவையால் குறிக்கோள் தீர்மானம் ஏற்றுக்கொள்ளப்படுதல்\n2. ஜவஹர்லால் நேருவால் அரசியலமைப்பு நிர்ணய அவையில் குறிக்கோள் தீர்மானம் முன்மொழியப்படுதல்\n3. அரசியலமைப்பு நிர்ணய அவையால் முகவுரை வாக்களிக்கப்பட்டு இயற்றப்படுதல்\n4. இந்திய அரசியலமைப்பு மற்றும் முகவுரை முழுமையாக நடைமுறைக்கு வருதல்",
    [
        {"id": "A", "en": "1 -> 2 -> 3 -> 4", "ta": "1 -> 2 -> 3 -> 4"},
        {"id": "B", "en": "2 -> 3 -> 1 -> 4", "ta": "2 -> 3 -> 1 -> 4"},
        {"id": "C", "en": "2 -> 1 -> 3 -> 4", "ta": "2 -> 1 -> 3 -> 4"},
        {"id": "D", "en": "2 -> 1 -> 4 -> 3", "ta": "2 -> 1 -> 4 -> 3"}
    ],
    "Correct Chronological Sequence: 2 (Objectives Resolution moved: Dec 13, 1946) -> 1 (Objectives Resolution adopted: Jan 22, 1947) -> 3 (Preamble enacted: Oct 17, 1949) -> 4 (Came into force: Jan 26, 1950).",
    "சரியான காலவரிசை: 2 (முன்மொழியப்பட்டது: டிசம்பர் 13, 1946) -> 1 (ஏற்றுக்கொள்ளப்பட்டது: ஜனவரி 22, 1947) -> 3 (இயற்றப்பட்டது: அக்டோபர் 17, 1949) -> 4 (நடைமுறை: ஜனவரி 26, 1950)."
))

# Q8 (D) - PYQ Pattern
questions.append(make_q(
    8, "Direct PYQ Pattern", "Easy", "D",
    "Which eminent constitutional expert and jurist described the Preamble as the 'Identity Card of the Constitution'?",
    "முகவுரையை 'அரசியலமைப்பின் அடையாள அட்டை' என்று வர்ணித்த புகழ்பெற்ற அரசியலமைப்பு நிபுணர் மற்றும் சட்ட வல்லுநர் யார்?",
    [
        {"id": "A", "en": "Dr. B.R. Ambedkar", "ta": "டாக்டர் பி.ஆர். அம்பேத்கர்"},
        {"id": "B", "en": "K.M. Munshi", "ta": "கே.எம். முன்ஷி"},
        {"id": "C", "en": "Sir Alladi Krishnaswami Iyer", "ta": "சர் அல்லாடி கிருஷ்ணசுவாமி ஐயர்"},
        {"id": "D", "en": "N.A. Palkhivala", "ta": "என்.ஏ. பல்கிவாலா"}
    ],
    "N.A. Palkhivala, an eminent jurist and constitutional expert, famously called the Preamble the 'Identity Card of the Constitution'.",
    "புகழ்பெற்ற சட்ட வல்லுநரான என்.ஏ. பல்கிவாலா முகவுரையை 'அரசியலமைப்பின் அடையாள அட்டை' என்று அழைத்தார்."
))

# Q9 (A) - TNPSC Trap
questions.append(make_q(
    9, "TNPSC Trap", "Hard", "A",
    "Which of the following words does NOT find any explicit mention in the Preamble of the Constitution of India?",
    "பின்வரும் சொற்களில் எது இந்திய அரசியலமைப்பின் முகவுரையில் எந்த இடத்திலும் வெளிப்படையாக இடம்பெறவில்லை?",
    [
        {"id": "A", "en": "Federal", "ta": "கூட்டாட்சி"},
        {"id": "B", "en": "Integrity", "ta": "ஒருமைப்பாடு"},
        {"id": "C", "en": "Fraternity", "ta": "சகோதரத்துவம்"},
        {"id": "D", "en": "Socialist", "ta": "சமதர்ம"}
    ],
    "TNPSC Trap Alert: The word 'Federal' is NOT mentioned anywhere in the Preamble (nor in Article 1, which uses 'Union of States').",
    "TNPSC பொறி எச்சரிக்கை: 'கூட்டாட்சி' (Federal) என்ற சொல் முகவுரையிலோ அல்லது உறுப்பு 1-லிலோ எங்கும் இடம்பெறவில்லை."
))

# Q10 (B) - Direct MCQ
questions.append(make_q(
    10, "Direct MCQ", "Easy", "B",
    "On which date was the historic 'Objectives Resolution' introduced by Pandit Jawaharlal Nehru in the Constituent Assembly?",
    "பண்டித ஜவஹர்லால் நேருவால் அரசியலமைப்பு நிர்ணய அவையில் வரலாற்றுச் சிறப்புமிக்க 'குறிக்கோள் தீர்மானம்' எந்த தேதியில் அறிமுகப்படுத்தப்பட்டது?",
    [
        {"id": "A", "en": "9th December 1946", "ta": "9 டிசம்பர் 1946"},
        {"id": "B", "en": "13th December 1946", "ta": "13 டிசம்பர் 1946"},
        {"id": "C", "en": "22nd January 1947", "ta": "22 ஜனவரி 1947"},
        {"id": "D", "en": "26th November 1949", "ta": "26 நவம்பர் 1949"}
    ],
    "Pandit Jawaharlal Nehru introduced the historic Objectives Resolution in the Constituent Assembly on December 13, 1946.",
    "பண்டித ஜவஹர்லால் நேரு வரலாற்றுச் சிறப்புமிக்க குறிக்கோள் தீர்மானத்தை டிசம்பர் 13, 1946 அன்று அரசியலமைப்பு அவையில் அறிமுகப்படுத்தினார்."
))

# Q11 (C) - Conceptual
questions.append(make_q(
    11, "Conceptual MCQ", "Medium", "C",
    "In Indian constitutional jurisprudence, what does the concept of 'Distributive Justice' mentioned in the Preamble represent?",
    "இந்திய சட்டவியலில், முகவுரையில் குறிப்பிடப்பட்டுள்ள 'பகிர்வு நீதி' (Distributive Justice) என்ற கருத்து எதனைக் குறிக்கிறது?",
    [
        {"id": "A", "en": "Combination of Legal Justice and Political Justice", "ta": "சட்ட நீதி மற்றும் அரசியல் நீதியின் சேர்க்கை"},
        {"id": "B", "en": "Distribution of legislative powers between Union and States", "ta": "மத்திய மற்றும் மாநில அரசுகளுக்கு இடையேயான சட்ட அதிகாரப் பங்கீடு"},
        {"id": "C", "en": "Combination of Social Justice and Economic Justice", "ta": "சமூக நீதி மற்றும் பொருளாதார நீதியின் சேர்க்கை"},
        {"id": "D", "en": "Equal distribution of judicial benches across India", "ta": "இந்தியா முழுவதும் நீதித்துறை அமர்வுகளின் சமமான பங்கீடு"}
    ],
    "Social Justice and Economic Justice together constitute what is known as 'Distributive Justice', aiming to remove social and economic inequalities.",
    "சமூக நீதியும் பொருளாதார நீதியும் இணைந்து 'பகிர்வு நீதி' என்று அழைக்கப்படுகிறது, இது சமூக மற்றும் பொருளாதார சமத்துவமின்மையை நீக்குவதை நோக்கமாகக் கொண்டுள்ளது."
))

# Q12 (D) - Statement-Based
questions.append(make_q(
    12, "Statement-Based", "Hard", "D",
    "Consider the following statements regarding Supreme Court rulings on the Preamble:\n1. In Berubari Union Case (1960), SC held that Preamble is NOT a part of the Constitution.\n2. In Kesavananda Bharati Case (1973), SC held that Preamble IS a part of the Constitution.\n3. In LIC of India Case (1995), SC held that Preamble is an integral part of the Constitution.\nWhich of the statements given above are CORRECT?",
    "முகவுரை குறித்த உச்ச நீதிமன்றத் தீர்ப்புகள் பற்றிய பின்வரும் கூற்றுகளைக் ஆராய்க:\n1. பெருபாரி யூனியன் வழக்கில் (1960), முகவுரை அரசியலமைப்பின் ஒரு பகுதி அல்ல என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது.\n2. கேசவானந்த பாரதி வழக்கில் (1973), முகவுரை அரசியலமைப்பின் ஒரு பகுதி தான் என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது.\n3. எல்.ஐ.சி வழக்கில் (1995), முகவுரை அரசியலமைப்பின் ஒரு ஒருங்கிணைந்த பகுதி என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எவை சரியானவை?",
    [
        {"id": "A", "en": "1 and 2 only", "ta": "1 மற்றும் 2 மட்டுமே"},
        {"id": "B", "en": "2 and 3 only", "ta": "2 மற்றும் 3 மட்டுமே"},
        {"id": "C", "en": "1 and 3 only", "ta": "1 மற்றும் 3 மட்டுமே"},
        {"id": "D", "en": "1, 2 and 3", "ta": "1, 2 மற்றும் 3"}
    ],
    "All three statements (1, 2, and 3) are CORRECT and accurately reflect the judicial evolution of the Preamble's constitutional status.",
    "மூன்று கூற்றுகளும் (1, 2 மற்றும் 3) சரியானவை மற்றும் முகவுரையின் அரசியலமைப்பு அந்தஸ்தின் நீதித்துறை வளர்ச்சியைத் துல்லியமாகப் பிரதிபலிக்கின்றன."
))

# Q13 (A) - Hard Analytical
questions.append(make_q(
    13, "Hard Analytical", "Hard", "A",
    "Which of the following correctly analyzes the functional relationship between the Preamble, Fundamental Rights (Part III), and Directive Principles of State Policy (Part IV)?",
    "முகவுரை, அடிப்படை உரிமைகள் (பகுதி III) மற்றும் அரசு வழிகாட்டு நெறிமுறைகள் (பகுதி IV) ஆகியவற்றுக்கு இடையேயான செயல்பாட்டு உறவை பின்வருவனவற்றில் எது சரியாக பகுப்பாய்வு செய்கிறது?",
    [
        {"id": "A", "en": "Preamble sets out the vision of Liberty, Equality, and Justice; Part III translates Liberty into justiciable civil rights; Part IV operationalizes Socio-Economic Justice through state policy", "ta": "முகவுரை சுதந்திரம், சமத்துவம், நீதியின் தொலைநோக்கை அமைக்கிறது; பகுதி III அதை சட்டப்பூர்வ உரிமைகளாக மாற்றுகிறது; பகுதி IV அரசு கொள்கை மூலம் சமூக-பொருளாதார நீதியைச் செயல்படுத்துகிறது"},
        {"id": "B", "en": "Part III overrides Preamble in all cases of conflict, while Part IV has no connection with the Preamble", "ta": "முரண்பாடுகள் ஏற்படும் போது பகுதி III முகவுரையை மேலெழுதுகிறது, அதே நேரத்தில் பகுதி IV-க்கு முகவுரையுடன் எந்த தொடர்பும் இல்லை"},
        {"id": "C", "en": "Preamble is an executive decree, Part III is a statutory law, and Part IV is a judicial order", "ta": "முகவுரை என்பது நிர்வாக ஆணை, பகுதி III ஒரு சட்டப்பூர்வ சட்டம், பகுதி IV ஒரு நீதித்துறை உத்தரவு"},
        {"id": "D", "en": "Preamble applies only to Parliament, Part III applies only to States, and Part IV applies only to Judiciary", "ta": "முகவுரை நாடாளுமன்றத்திற்கு மட்டுமே பொருந்தும், பகுதி III மாநிலங்களுக்கு மட்டுமே பொருந்தும், பகுதி IV நீதித்துறைக்கு மட்டுமே பொருந்தும்"}
    ],
    "Granville Austin noted that Preamble sets out the grand vision, Part III guarantees Political Democracy & Civil Liberties, and Part IV secures Social & Economic Democracy.",
    "முகவுரை உன்னத தொலைநோக்கை அமைக்கிறது, பகுதி III அரசியல் ஜனநாயகத்தையும் சிவில் சுதந்திரங்களையும் உத்தரவாதம் செய்கிறது, பகுதி IV சமூக மற்றும் பொருளாதார ஜனநாயகத்தை உறுதி செய்கிறது."
))

# Q14 (A) - Reasoning
questions.append(make_q(
    14, "Assertion & Reason", "Medium", "A",
    "Assertion (A): The provisions of the Preamble of the Constitution of India are non-justiciable in nature.\nReason (R): The provisions of the Preamble cannot be directly enforced in any court of law to obtain legal relief or remedies.",
    "கூற்று (A): இந்திய அரசியலமைப்பின் முகவுரையில் உள்ள விதிகள் இயல்பிலேயே நீதிமன்றத்தால் நிலைநிறுத்த முடியாதவை (Non-justiciable).\nகாரணம் (R): முகவுரையின் விதிகளை சட்ட நிவாரணம் அல்லது தீர்வுகளைப் பெற எந்தவொரு நீதிமன்றத்திலும் நேரடியாக அமல்படுத்த முடியாது.",
    [
        {"id": "A", "en": "Both A and R are true and R is the correct explanation of A", "ta": "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்"},
        {"id": "B", "en": "Both A and R are true but R is NOT the correct explanation of A", "ta": "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல"},
        {"id": "C", "en": "A is true but R is false", "ta": "A சரி, ஆனால் R தவறு"},
        {"id": "D", "en": "A is false but R is true", "ta": "A தவறு, ஆனால் R சரி"}
    ],
    "Both A and R are true, and R correctly explains A. Non-justiciability specifically means that non-compliance with Preamble provisions cannot be directly challenged in a court of law.",
    "A மற்றும் R இரண்டும் சரி, R என்பது A விற்கு சரியான விளக்கமாகும். நீதிமன்றத்தால் நிலைநிறுத்த முடியாத தன்மை என்றால் அதன் விதிகளை நேரடியாக நீதிமன்றத்தில் அமல்படுத்த முடியாது என்பதாகும்."
))

# Q15 (B) - Match the Following
questions.append(make_q(
    15, "Match the Following", "Medium", "B",
    "Match List I (Constitutional Commentators) with List II (Quotes/Descriptions of Preamble) and select the correct answer:\n\nList I\nA. N.A. Palkhivala\nB. K.M. Munshi\nC. Pandit Thakur Das Bhargava\nD. Sir Ernest Barker\n\nList II\n1. Horoscope of our Sovereign Democratic Republic\n2. Key-note to the Constitution\n3. Identity Card of the Constitution\n4. Soul of the Constitution and Jewel set in the Constitution",
    "பட்டியல் I-ஐ (அரசியலமைப்பு உரையாசிரியர்கள்) பட்டியல் II உடன் (முகவுரை பற்றிய மேற்கோள்கள்) பொருத்தி சரியான பதிலைத் தேர்ந்தெடுக்கவும்:\n\nபட்டியல் I\nA. என்.ஏ. பல்கிவாலா\nB. கே.எம். முன்ஷி\nC. பண்டிட் தாக்கூர் தாஸ் பார்கவா\nD. சர் எர்னஸ்ட் பார்கர்\n\nபட்டியல் II\n1. நமது இறையாண்மை கொண்ட ஜனநாயக குடியரசின் ஜாதகம்\n2. அரசியலமைப்பின் முக்கிய குறிப்பு (Key-note)\n3. அரசியலமைப்பின் அடையாள அட்டை\n4. அரசியலமைப்பின் ஆன்மா மற்றும் பதிக்கப்பட்ட ஆபரணம்",
    [
        {"id": "A", "en": "A-1, B-3, C-4, D-2", "ta": "A-1, B-3, C-4, D-2"},
        {"id": "B", "en": "A-3, B-1, C-4, D-2", "ta": "A-3, B-1, C-4, D-2"},
        {"id": "C", "en": "A-3, B-4, C-1, D-2", "ta": "A-3, B-4, C-1, D-2"},
        {"id": "D", "en": "A-2, B-1, C-4, D-3", "ta": "A-2, B-1, C-4, D-3"}
    ],
    "Correct Match: A-3 (Palkhivala = Identity Card), B-1 (Munshi = Horoscope), C-4 (Bhargava = Soul & Jewel), D-2 (Barker = Key-note).",
    "சரியான பொருத்தம்: A-3 (பல்கிவாலா = அடையாள அட்டை), B-1 (முன்ஷி = ஜாதகம்), C-4 (பார்கவா = ஆன்மா & ஆபரணம்), D-2 (பார்கர் = முக்கிய குறிப்பு)."
))

# Q16 (C) - Chronology
questions.append(make_q(
    16, "Chronology", "Hard", "C",
    "Arrange the following landmark Supreme Court cases involving Preamble interpretation in correct chronological order:\n1. Minerva Mills v. Union of India\n2. In re Berubari Union Reference\n3. Kesavananda Bharati v. State of Kerala\n4. Golak Nath v. State of Punjab",
    "முகவுரை விளக்கத்தை உள்ளடக்கிய பின்வரும் மைல்கல் உச்ச நீதிமன்ற வழக்குகளை சரியான காலவரிசையில் அமைக்கவும்:\n1. மினர்வா மில்ஸ் எதிர் இந்திய யூனியன்\n2. பெருபாரி யூனியன் வழக்கு\n3. கேசவானந்த பாரதி எதிர் கேரளா மாநிலம்\n4. கோலக் நாத் எதிர் பஞ்சாப் மாநிலம்",
    [
        {"id": "A", "en": "2 -> 3 -> 4 -> 1", "ta": "2 -> 3 -> 4 -> 1"},
        {"id": "B", "en": "4 -> 2 -> 3 -> 1", "ta": "4 -> 2 -> 3 -> 1"},
        {"id": "C", "en": "2 -> 4 -> 3 -> 1", "ta": "2 -> 4 -> 3 -> 1"},
        {"id": "D", "en": "2 -> 4 -> 1 -> 3", "ta": "2 -> 4 -> 1 -> 3"}
    ],
    "Chronological Sequence: 2 (Berubari: 1960) -> 4 (Golak Nath: 1967) -> 3 (Kesavananda Bharati: 1973) -> 1 (Minerva Mills: 1980).",
    "காலவரிசை: 2 (பெருபாரி: 1960) -> 4 (கோலக் நாத்: 1967) -> 3 (கேசவானந்த பாரதி: 1973) -> 1 (மினர்வா மில்ஸ்: 1980)."
))

# Q17 (D) - Direct PYQ Pattern
questions.append(make_q(
    17, "Direct PYQ Pattern", "Medium", "D",
    "The 42nd Constitutional Amendment Act of 1976 that inserted new words into the Preamble came into force officially on which date?",
    "முகவுரையில் புதிய சொற்களைச் சேர்த்த 1976 ஆம் ஆண்டின் 42வது அரசியலமைப்புத் திருத்தச் சட்டம் அதிகாரப்பூர்வமாக எந்த தேதியில் நடைமுறைக்கு வந்தது?",
    [
        {"id": "A", "en": "18th December 1976", "ta": "18 டிசம்பர் 1976"},
        {"id": "B", "en": "26th November 1976", "ta": "26 நவம்பர் 1976"},
        {"id": "C", "en": "26th January 1977", "ta": "26 ஜனவரி 1977"},
        {"id": "D", "en": "3rd January 1977", "ta": "3 ஜனவரி 1977"}
    ],
    "Section 2 of the 42nd Constitutional Amendment Act 1976 amending the Preamble officially came into force on January 3, 1977.",
    "42வது திருத்தச் சட்டத்தின் முகவுரையைத் திருத்தும் பிரிவு 2 அதிகாரப்பூர்வமாக ஜனவரி 3, 1977 அன்று நடைமுறைக்கு வந்தது."
))

# Q18 (A) - TNPSC Trap
questions.append(make_q(
    18, "TNPSC Trap", "Hard", "A",
    "Which of the following forms of Liberty is NOT guaranteed in the Preamble of the Constitution of India?",
    "பின்வரும் சுதந்திர வடிவங்களில் எது இந்திய அரசியலமைப்பின் முகவுரையில் உத்தரவாதம் அளிக்கப்படவில்லை?",
    [
        {"id": "A", "en": "Economic Liberty", "ta": "பொருளாதார சுதந்திரம்"},
        {"id": "B", "en": "Liberty of Thought", "ta": "எண்ண சுதந்திரம்"},
        {"id": "C", "en": "Liberty of Expression", "ta": "கருத்து வெளிப்பாட்டு சுதந்திரம்"},
        {"id": "D", "en": "Liberty of Worship", "ta": "வழிபாட்டு சுதந்திரம்"}
    ],
    "TNPSC Trap Alert: The Preamble secures 'Economic Justice', NOT 'Economic Liberty'. It secures Liberty of Thought, Expression, Belief, Faith, and Worship.",
    "TNPSC பொறி எச்சரிக்கை: முகவுரை 'பொருளாதார நீதியை' மட்டுமே வழங்குகிறது, 'பொருளாதார சுதந்திரத்தை' அல்ல. இது எண்ணம், கருத்து வெளிப்பாடு, நம்பிக்கை, பக்தி, வழிபாடு ஆகிய 5 சுதந்திரங்களை மட்டுமே வழங்குகிறது."
))

# Q19 (B) - Direct MCQ
questions.append(make_q(
    19, "Direct MCQ", "Easy", "B",
    "How many times has the Preamble of the Constitution of India been amended since 1949?",
    "1949 முதல் இந்திய அரசியலமைப்பின் முகவுரை எத்தனை முறை திருத்தப்பட்டுள்ளது?",
    [
        {"id": "A", "en": "Two times", "ta": "இரண்டு முறை"},
        {"id": "B", "en": "Only once", "ta": "ஒரே ஒரு முறை மட்டுமே"},
        {"id": "C", "en": "Three times", "ta": "மூன்று முறை"},
        {"id": "D", "en": "Never amended", "ta": "ஒருபோதும் திருத்தப்படவில்லை"}
    ],
    "The Preamble has been amended ONLY ONCE by the 42nd Constitutional Amendment Act of 1976.",
    "முகவுரை 1976-ன் 42வது அரசியலமைப்புத் திருத்தச் சட்டத்தின் மூலம் ஒரே ஒரு முறை மட்டுமே திருத்தப்பட்டுள்ளது."
))

# Q20 (C) - Conceptual
questions.append(make_q(
    20, "Conceptual MCQ", "Medium", "C",
    "What is the true nature of 'Secularism' as embodied in the Preamble of the Constitution of India?",
    "இந்திய அரசியலமைப்பின் முகவுரையில் உள்ள 'மதச்சார்பின்மையின்' உண்மையான இயல்பு என்ன?",
    [
        {"id": "A", "en": "Strict Western separation forbidding state aid to any religious institution", "ta": "மத நிறுவனங்களுக்கு அரசு உதவிகளை முற்றிலும் தடைசெய்யும் கண்டிப்பான மேற்கத்திய பிரிவினை"},
        {"id": "B", "en": "Anti-religious state posture promoting rationalist atheism", "ta": "பகுத்தறிவு நாத்திகத்தை ஊக்குவிக்கும் மத எதிர்ப்பு அரசு நிலைப்பாடு"},
        {"id": "C", "en": "Positive Secularism guaranteeing equal status, respect, and protection to all religions ('Sarva Dharma Sambhava')", "ta": "அனைத்து மதங்களுக்கும் சமமான அந்தஸ்து, மரியாதை மற்றும் பாதுகாப்பை உறுதி செய்யும் நேர்மறை மதச்சார்பின்மை ('சர்வ தர்ம சமபாவா')"},
        {"id": "D", "en": "State patronage to the majority religion while tolerating minority faiths", "ta": "சிறுபான்மை மதங்களைச் சகித்துக் கொண்டு பெரும்பான்மை மதத்திற்கு அரசு ஆதரவு அளிப்பது"}
    ],
    "Indian secularism is positive secularism, ensuring equal treatment, equal respect, and equal protection for all religions.",
    "இந்திய மதச்சார்பின்மை என்பது நேர்மறை மதச்சார்பின்மை ஆகும்; இது அனைத்து மதங்களுக்கும் சமமான மரியாதை மற்றும் பாதுகாப்பை அளிக்கிறது."
))

# Q21 (D) - Statement-Based
questions.append(make_q(
    21, "Statement-Based", "Hard", "D",
    "Consider the following statements regarding 'Democratic Socialism' as reflected in the Preamble:\n1. It believes in a mixed economy where public and private sectors co-exist.\n2. It aims to eliminate poverty, ignorance, disease, and inequality of opportunity.\n3. It involves complete nationalization of all private property and means of production.\nWhich of the statements given above are CORRECT?",
    "முகவுரையில் பிரதிபலிக்கும் 'ஜனநாயக சமதர்மம்' பற்றிய பின்வரும் கூற்றுகளைக் ஆராய்க:\n1. இது பொது மற்றும் தனியார் துறைகள் இணைந்து செயல்படும் கலப்புப் பொருளாதாரத்தை நம்புகிறது.\n2. இது வறுமை, அறியாமை, நோய் மற்றும் வாய்ப்பு சமத்துவமின்மையை ஒழிப்பதை நோக்கமாகக் கொண்டுள்ளது.\n3. இது அனைத்து தனியார் சொத்துக்கள் மற்றும் உற்பத்தி சாதனங்களையும் முழுமையாக அரசுடைமையாக்குவதை உள்ளடக்கியது.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் எவை சரியானவை?",
    [
        {"id": "A", "en": "1 and 3 only", "ta": "1 மற்றும் 3 மட்டுமே"},
        {"id": "B", "en": "2 and 3 only", "ta": "2 மற்றும் 3 மட்டுமே"},
        {"id": "C", "en": "1, 2 and 3", "ta": "1, 2 மற்றும் 3"},
        {"id": "D", "en": "1 and 2 only", "ta": "1 மற்றும் 2 மட்டுமே"}
    ],
    "Statements 1 and 2 are CORRECT. Statement 3 is INCORRECT because complete nationalization of private property describes Marxist/Communistic Socialism, whereas Indian Democratic Socialism leans on Gandhian socialism favoring a mixed economy.",
    "கூற்றுகள் 1 மற்றும் 2 சரியானவை. கூற்று 3 தவறானது; ஏனெனில் முழுமையான அரசுடைமையாக்கல் கம்யூனிச சமதர்மத்தின் பண்பாகும், இந்திய ஜனநாயக சமதர்மம் கலப்புப் பொருளாதாரத்தை ஆதரிக்கிறது."
))

# Q22 (A) - Hard Analytical
questions.append(make_q(
    22, "Hard Analytical", "Hard", "A",
    "Where the language of any Article of the Constitution is ambiguous and capable of two interpretations, how does the Supreme Court utilize the Preamble?",
    "அரசியலமைப்பின் எந்தவொரு உறுப்பின் வாசகமும் தெளிவற்றதாகவும் இரு வேறு விளக்கங்களுக்கு இடமளிப்பதாகவும் இருக்கும்போது, உச்ச நீதிமன்றம் முகவுரையை எவ்வாறு பயன்படுத்துகிறது?",
    [
        {"id": "A", "en": "As an interpretive compass/key-note to adopt the interpretation aligning with the grand vision of the Preamble", "ta": "முகவுரையின் உன்னத நோக்கத்துடன் ஒத்துப்போகும் விளக்கத்தை ஏற்றுக்கொள்ள வழிகாட்டும் திசைகாட்டியாகப் பயன்படுத்துகிறது"},
        {"id": "B", "en": "To strike down the ambiguous Article as unconstitutional automatically", "ta": "தெளிவற்ற உறுப்பைத் தானாகவே அரசியலமைப்பிற்கு முரணானது என ரத்து செய்யப் பயன்படுத்துகிறது"},
        {"id": "C", "en": "To refer the ambiguity to the British Privy Council for clarification", "ta": "தெளிவுபடுத்தலுக்காக அந்தத் தெளிவின்மையை பிரிட்டிஷ் பிரைவி கவுன்சிலுக்கு அனுப்பப் பயன்படுத்துகிறது"},
        {"id": "D", "en": "Preamble can never be referred to in any constitutional interpretation", "ta": "எந்தவொரு அரசியலமைப்பு விளக்கத்திலும் முகவுரையைக் குறிப்பிடவே முடியாது"}
    ],
    "When constitutional provisions are ambiguous, the Supreme Court relies on the Preamble as an interpretive key to determine the true legislative intent.",
    "அரசியலமைப்பு விதிகள் தெளிவற்றதாக இருக்கும்போது, உண்மையான நோக்கத்தைத் தீர்மானிக்க உச்ச நீதிமன்றம் முகவுரையை ஒரு விளக்கச் சாவியாகப் பயன்படுத்துகிறது."
))

# Q23 (B) - Reasoning
questions.append(make_q(
    23, "Assertion & Reason", "Hard", "B",
    "Assertion (A): The Preamble is neither a source of power to the Legislature nor a prohibition upon the powers of the Legislature.\nReason (R): Legislative powers of Parliament and State Legislatures are traceably derived from Article 245 and the Seventh Schedule of the Constitution.",
    "கூற்று (A): முகவுரை என்பது சட்டமன்றத்திற்கு அதிகாரத்தை வழங்கும் மூலமும் அல்ல, சட்டமன்றத்தின் அதிகாரங்கள் மீதான தடையாகவும் அமையாது.\nகாரணம் (R): நாடாளுமன்றம் மற்றும் மாநில சட்டமன்றங்களின் சட்டமியற்றும் அதிகாரங்கள் உறுப்பு 245 மற்றும் ஏழாவது அட்டவணையிலிருந்தே பெறப்படுகின்றன.",
    [
        {"id": "A", "en": "Both A and R are true and R is the correct explanation of A", "ta": "A மற்றும் R இரண்டும் சரி, மேலும் R என்பது A விற்கு சரியான விளக்கமாகும்"},
        {"id": "B", "en": "Both A and R are true but R is NOT the correct explanation of A", "ta": "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது A விற்கு சரியான விளக்கம் அல்ல"},
        {"id": "C", "en": "A is true but R is false", "ta": "A சரி, ஆனால் R தவறு"},
        {"id": "D", "en": "A is false but R is true", "ta": "A தவறு, ஆனால் R சரி"}
    ],
    "Both A and R are true, but R is an independent constitutional fact establishing where legislative powers reside, while A states the legal attribute of Preamble.",
    "A மற்றும் R இரண்டும் சரி, ஆனால் R என்பது ஒரு சுயாதீன அரசியலமைப்பு உண்மையாகும்."
))

# Q24 (C) - Match the Following
questions.append(make_q(
    24, "Match the Following", "Medium", "C",
    "Match List I (Preamble Objectives) with List II (Associated Articles/Inspirations) and select the correct answer:\n\nList I\nA. Justice (Social, Economic, Political)\nB. Liberty (Thought, Expression, Belief)\nC. Equality (Status and Opportunity)\nD. Fraternity (Brotherhood)\n\nList II\n1. Article 19 & 25 (Part III)\n2. Article 51A(e) (Part IV-A)\n3. Russian Revolution (1917) & DPSP Articles 38, 39\n4. Articles 14, 15, 16, 17, 18 (Part III)",
    "பட்டியல் I-ஐ (முகப்புரைக் குறிக்கோள்கள்) பட்டியல் II உடன் (தொடர்புடைய உறுப்புகள்/ஈர்ப்புகள்) பொருத்தி சரியான பதிலைத் தேர்ந்தெடுக்கவும்:\n\nபட்டியல் I\nA. நீதி (சமூக, பொருளாதார, அரசியல்)\nB. சுதந்திரம் (எண்ணம், கருத்து வெளிப்பாடு)\nC. சமத்துவம் (அந்தஸ்து மற்றும் வாய்ப்பு)\nD. சகோதரத்துவம்\n\nபட்டியல் II\n1. உறுப்புகள் 19 & 25 (பகுதி III)\n2. உறுப்பு 51A(e) (பகுதி IV-A)\n3. ரஷ்யப் புரட்சி (1917) & DPSP உறுப்புகள் 38, 39\n4. உறுப்புகள் 14, 15, 16, 17, 18 (பகுதி III)",
    [
        {"id": "A", "en": "A-1, B-3, C-4, D-2", "ta": "A-1, B-3, C-4, D-2"},
        {"id": "B", "en": "A-3, B-1, C-2, D-4", "ta": "A-3, B-1, C-2, D-4"},
        {"id": "C", "en": "A-3, B-1, C-4, D-2", "ta": "A-3, B-1, C-4, D-2"},
        {"id": "D", "en": "A-4, B-1, C-3, D-2", "ta": "A-4, B-1, C-3, D-2"}
    ],
    "Correct Match: A-3 (Justice = Russian Rev / Arts 38, 39), B-1 (Liberty = Arts 19, 25), C-4 (Equality = Arts 14-18), D-2 (Fraternity = Art 51A(e)).",
    "சரியான பொருத்தம்: A-3 (நீதி = ரஷ்யப் புரட்சி / உறுப்புகள் 38, 39), B-1 (சுதந்திரம் = உறுப்புகள் 19, 25), C-4 (சமத்துவம் = உறுப்புகள் 14-18), D-2 (சகோதரத்துவம் = உறுப்பு 51A(e))."
))

# Q25 (D) - Chronology
questions.append(make_q(
    25, "Chronology", "Hard", "D",
    "Arrange the following legislative steps of the 42nd Constitutional Amendment Act, 1976 in correct chronological order:\n1. Presidential assent given by Fakhruddin Ali Ahmed\n2. Swaran Singh Committee submits its recommendations\n3. Amendment provisions relating to the Preamble came into force officially\n4. Bill passed by Lok Sabha and Rajya Sabha",
    "1976-ன் 42வது அரசியலமைப்புத் திருத்தச் சட்டத்தின் பின்வரும் சட்டமன்றப் படிகளை சரியான காலவரிசையில் அமைக்கவும்:\n1. பக்ருதீன் அலி அகமதால் குடியரசுத் தலைவர் ஒப்புதல் அளிக்கப்படுதல்\n2. சுரன் சிங் குழு தனது பரிந்துரைகளைச் சமர்ப்பித்தல்\n3. முகவுரை தொடர்பான திருத்த விதிகள் அதிகாரப்பூர்வமாக நடைமுறைக்கு வருதல்\n4. மக்களவை மற்றும் மாநிலங்களவையால் மசோதா நிறைவேற்றப்படுதல்",
    [
        {"id": "A", "en": "2 -> 1 -> 4 -> 3", "ta": "2 -> 1 -> 4 -> 3"},
        {"id": "B", "en": "1 -> 2 -> 4 -> 3", "ta": "1 -> 2 -> 4 -> 3"},
        {"id": "C", "en": "2 -> 4 -> 3 -> 1", "ta": "2 -> 4 -> 3 -> 1"},
        {"id": "D", "en": "2 -> 4 -> 1 -> 3", "ta": "2 -> 4 -> 1 -> 3"}
    ],
    "Correct Chronological Sequence: 2 (Swaran Singh Report: 1976) -> 4 (Passed by Parliament: Nov 1976) -> 1 (Assent: Dec 18, 1976) -> 3 (Came into force: Jan 3, 1977).",
    "சரியான காலவரிசை: 2 (சுரன் சிங் அறிக்கை: 1976) -> 4 (நாடாளுமன்றம் நிறைவேற்றியது: நவம்பர் 1976) -> 1 (குடியரசுத் தலைவர் ஒப்புதல்: டிசம்பர் 18, 1976) -> 3 (நடைமுறைக்கு வந்தது: ஜனவரி 3, 1977)."
))

print(f"Block 1 complete. Total questions: {len(questions)}")
