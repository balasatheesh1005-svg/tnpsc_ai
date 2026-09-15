# -*- coding: utf-8 -*-
"""
Build Judicial Review, Activism & PIL - Part 1 Easy (50 MCQs)
Identifier: JRAP_E_001 to JRAP_E_050
Key Distribution: A: 12, B: 13, C: 13, D: 12 (Total: 50)
Anti-Block: Max consecutive run <= 2
"""
import json
import os
from judicial_review_mcq_helper import make_jrap_q

def build_easy_mcqs():
    questions = []

    # 1 - B
    questions.append(make_jrap_q(
        "JRAP_E_001", "Easy", "single_choice", "Judicial Review Basis",
        "From which country's constitutional system did India borrow the concept of Judicial Review?",
        "இந்தியா எந்த நாட்டின் அரசியலமைப்பு முறையிலிருந்து நீதித்துறை மறுஆய்வு என்ற கருத்தை ஏற்றுக்கொண்டது?",
        "United Kingdom", "ஐக்கிய இராச்சியம்",
        "United States of America", "அமெரிக்க ஐக்கிய நாடுகள்",
        "Canada", "கனடா",
        "Australia", "ஆஸ்திரேலியா",
        "B",
        "The concept of Judicial Review originated and developed in the USA (Marbury v. Madison, 1803) and was adopted by the Indian Constitution.",
        "நீதித்துறை மறுஆய்வு என்ற கருத்து அமெரிக்காவில் (மார்பரி v. மேடிசன், 1803) தோன்றி வளர்ந்தது; இது இந்திய அரசியலமைப்பால் ஏற்றுக்கொள்ளப்பட்டது.",
        "UK follows Parliamentary Supremacy where courts cannot strike down Acts of Parliament.", "இங்கிலாந்தில் நாடாளுமன்ற மேலாதிக்கம் நிலவுவதால் நாடாளுமன்றச் சட்டங்களை நீதிமன்றங்கள் ரத்து செய்ய முடியாது.",
        "Correct. India adopted the principle of Judicial Review from the US Constitution.", "சரி. அமெரிக்க அரசியலமைப்பிலிருந்தே நீதித்துறை மறுஆய்வுக் கோட்பாட்டை இந்தியா ஏற்றுக்கொண்டது.",
        "Canada provided the concept of a strong Centre and advisory jurisdiction.", "கனடா வலுவான மத்திய அரசு மற்றும் ஆலோசனை அதிகார வரம்பை வழங்கியது.",
        "Australia provided concurrent list and freedom of trade/commerce.", "ஆஸ்திரேலியா பொதுப் பட்டியல் மற்றும் வர்த்தக சுதந்திரத்தை வழங்கியது.",
        "Remember: In USA, judicial supremacy prevails, whereas India synthesizes Parliamentary Sovereignty and Judicial Supremacy.",
        "நினைவில் கொள்க: அமெரிக்காவில் நீதித்துறை மேலாதிக்கம் நிலவுகிறது; இந்தியாவில் நாடாளுமன்ற இறையாண்மையும் நீதித்துறை மேலாதிக்கமும் ஒருங்கிணைக்கப்பட்டுள்ளன.",
        "Judicial review was formally established in the US in Marbury v. Madison (1803) by Chief Justice John Marshall.",
        "அமெரிக்காவில் 1803-ல் தலைமை நீதிபதி ஜான் மார்ஷல் அவர்களால் மார்பரி v. மேடிசன் வழக்கில் நீதித்துறை மறுஆய்வு நிறுவப்பட்டது."
    ))

    # 2 - C
    questions.append(make_jrap_q(
        "JRAP_E_002", "Easy", "single_choice", "Article 13",
        "Which Article of the Indian Constitution declares that laws inconsistent with or in derogation of Fundamental Rights shall be void?",
        "இந்திய அரசியலமைப்பின் எந்த உறுப்பு அடிப்படை உரிமைகளுக்கு முரணான அல்லது அவற்றைக் குறைக்கும் சட்டங்கள் செல்லாது என அறிவிக்கிறது?",
        "Article 12", "உறுப்பு 12",
        "Article 14", "உறுப்பு 14",
        "Article 13", "உறுப்பு 13",
        "Article 15", "உறுப்பு 15",
        "C",
        "Article 13 provides the express constitutional basis for Judicial Review by declaring all pre-constitutional and post-constitutional laws violating Fundamental Rights void.",
        "உறுப்பு 13 அடிப்படை உரிமைகளை மீறும் அரசியலமைப்புக்கு முந்தைய மற்றும் பிந்தைய சட்டங்கள் செல்லாது என அறிவிப்பதன் மூலம் நீதித்துறை மறுஆய்வுக்கான வெளிப்படையான அடித்தளத்தை வழங்குகிறது.",
        "Article 12 defines the 'State' for Part III.", "உறுப்பு 12 பகுதி III-க்கான 'அரசு' என்பதை வரையறுக்கிறது.",
        "Article 14 guarantees equality before the law and equal protection of laws.", "உறுப்பு 14 சட்டத்தின் முன் சமத்துவத்தையும் சம பாதுகாப்பையும் உத்தரவாதம் செய்கிறது.",
        "Correct. Article 13(2) prohibits State from enacting laws that abridge Fundamental Rights.", "சரி. உறுப்பு 13(2) அடிப்படை உரிமைகளைக் குறைக்கும் சட்டங்களை அரசு இயற்றுவதைத் தடுக்கிறது.",
        "Article 15 prohibits discrimination on grounds of religion, race, caste, sex, or place of birth.", "உறுப்பு 15 மதம், இனம், சாதி, பாலினம் அல்லது பிறப்பிடம் அடிப்படையில் பாகுபாடு காட்டுவதைத் தடை செய்கிறது.",
        "Article 13 is the primary tool of Judicial Review in Part III.",
        "பகுதி III-ல் நீதித்துறை மறுஆய்விற்கான முதன்மைக் கருவி உறுப்பு 13 ஆகும்.",
        "Article 13 incorporates the doctrine of severability and doctrine of eclipse.",
        "உறுப்பு 13 பிரித்தெடுக்கும் கோட்பாடு மற்றும் மறைப்புக் கோட்பாட்டை உள்ளடக்கியுள்ளது."
    ))

    # 3 - A
    questions.append(make_jrap_q(
        "JRAP_E_003", "Easy", "single_choice", "Article 32",
        "Under which Article can an aggrieved citizen directly approach the Supreme Court for enforcement of Fundamental Rights?",
        "பாதிக்கப்பட்ட குடிமகன் ஒருவர் அடிப்படை உரிமைகளை அமல்படுத்த எந்த உறுப்பின் கீழ் நேரடியாக உச்ச நீதிமன்றத்தை அணுகலாம்?",
        "Article 32", "உறுப்பு 32",
        "Article 226", "உறுப்பு 226",
        "Article 131", "உறுப்பு 131",
        "Article 136", "உறுப்பு 136",
        "A",
        "Article 32 gives the right to move the Supreme Court by appropriate proceedings for the enforcement of the Fundamental Rights.",
        "உறுப்பு 32 அடிப்படை உரிமைகளை அமல்படுத்துவதற்காக தகுந்த நடவடிக்கைகள் மூலம் உச்ச நீதிமன்றத்தை அணுகும் உரிமையை வழங்குகிறது.",
        "Correct. Dr. Ambedkar called Article 32 the 'Heart and Soul of the Constitution'.", "சரி. டாக்டர் அம்பேத்கர் உறுப்பு 32-ஐ 'அரசியலமைப்பின் இதயம் மற்றும் ஆன்மா' என்றார்.",
        "Article 226 is used to approach the High Court, not the Supreme Court.", "உறுப்பு 226 உயர் நீதிமன்றத்தை அணுகப் பயன்படுகிறது, உச்ச நீதிமன்றத்தை அல்ல.",
        "Article 131 relates to the original jurisdiction in federal disputes.", "உறுப்பு 131 கூட்டாட்சிச் சிக்கல்களில் அசல் அதிகார வரம்பு பற்றியது.",
        "Article 136 relates to Special Leave Petitions.", "உறுப்பு 136 சிறப்பு விடுப்பு மனுக்கள் பற்றியது.",
        "Article 32 is itself a Fundamental Right under Part III.",
        "உறுப்பு 32 தானே பகுதி III-ன் கீழ் உள்ள ஓர் அடிப்படை உரிமையாகும்.",
        "Because Article 32 is a Fundamental Right, the Supreme Court cannot refuse to entertain an Article 32 petition.",
        "உறுப்பு 32 அடிப்படை உரிமை என்பதால் உச்ச நீதிமன்றம் மனுவை விசாரிக்க மறுக்க முடியாது."
    ))

    # 4 - D
    questions.append(make_jrap_q(
        "JRAP_E_004", "Easy", "single_choice", "Article 226",
        "Under which Article does a High Court have the power to issue writs for the enforcement of Fundamental Rights and for any other purpose?",
        "அடிப்படை உரிமைகளை அமல்படுத்துவதற்கும் மற்றும் வேறு எந்த நோக்கத்திற்கும் நீதிப்பேராணைகளை வெளியிட உயர் நீதிமன்றத்திற்கு எந்த உறுப்பு அதிகாரம் அளிக்கிறது?",
        "Article 32", "உறுப்பு 32",
        "Article 227", "உறுப்பு 227",
        "Article 143", "உறுப்பு 143",
        "Article 226", "உறுப்பு 226",
        "D",
        "Article 226 empowers High Courts to issue directions, orders, or writs for the enforcement of Fundamental Rights and 'for any other purpose' (ordinary legal rights).",
        "உறுப்பு 226 அடிப்படை உரிமைகள் மற்றும் 'வேறு எந்த நோக்கத்திற்கும்' (சாதாரண சட்ட உரிமைகள்) உத்தரவுகள் அல்லது நீதிப்பேராணைகளை வெளியிட உயர் நீதிமன்றங்களுக்கு அதிகாரம் அளிக்கிறது.",
        "Article 32 is exclusively for the Supreme Court.", "உறுப்பு 32 உச்ச நீதிமன்றத்திற்கு மட்டுமே உரியது.",
        "Article 227 deals with superintendence over subordinate courts and tribunals.", "உறுப்பு 227 சார்நிலை நீதிமன்றங்கள் மற்றும் தீர்ப்பாயங்கள் மீதான மேற்பார்வை அதிகாரம் பற்றியது.",
        "Article 143 deals with the advisory jurisdiction of the Supreme Court.", "உறுப்பு 143 உச்ச நீதிமன்றத்தின் ஆலோசனை அதிகார வரம்பு பற்றியது.",
        "Correct. High Courts exercise writ jurisdiction under Article 226.", "சரி. உயர் நீதிமன்றங்கள் உறுப்பு 226-ன் கீழ் நீதிப்பேராணை அதிகாரத்தைச் செயல்படுத்துகின்றன.",
        "Remember that the phrase 'for any other purpose' makes Article 226 wider in scope than Article 32.",
        "'வேறு எந்த நோக்கத்திற்கும்' என்ற சொற்றொடர் உறுப்பு 226-ஐ உறுப்பு 32-ஐ விட பரந்ததாக்குகிறது.",
        "Unlike the Supreme Court under Article 32, a High Court's remedy under Article 226 is discretionary.",
        "உறுப்பு 32 போலன்றி, உறுப்பு 226-ன் கீழ் உயர் நீதிமன்றத்தின் பரிகாரம் விவேக அதிகாரத்திற்கு உட்பட்டது."
    ))

    # 5 - B
    questions.append(make_jrap_q(
        "JRAP_E_005", "Easy", "single_choice", "Basic Structure",
        "In which historic case did the Supreme Court propound the 'Basic Structure Doctrine'?",
        "எந்த வரலாற்றுச் சிறப்புமிக்க வழக்கில் உச்ச நீதிமன்றம் 'அடிப்படைக் கட்டமைப்புக் கோட்பாட்டை' முன்வைத்தது?",
        "Golaknath Case (1967)", "கோலக்நாத் வழக்கு (1967)",
        "Kesavananda Bharati Case (1973)", "கேசவாநந்த பாரதி வழக்கு (1973)",
        "Minerva Mills Case (1980)", "மினர்வா மில்ஸ் வழக்கு (1980)",
        "Maneka Gandhi Case (1978)", "மேனகா காந்தி வழக்கு (1978)",
        "B",
        "In Kesavananda Bharati v. State of Kerala (1973), a 13-judge bench by a 7:6 majority ruled that Parliament cannot alter the basic structure of the Constitution.",
        "கேசவாநந்த பாரதி v. கேரள மாநிலம் (1973) வழக்கில் 13 நீதிபதிகள் கொண்ட அமர்வு 7:6 பெரும்பான்மையில் நாடாளுமன்றம் அடிப்படைக் கட்டமைப்பை மாற்ற முடியாது எனத் தீர்ப்பளித்தது.",
        "Golaknath (1967) held that Parliament cannot amend Fundamental Rights, but did not formulate the Basic Structure Doctrine.", "கோலக்நாத் வழக்கு நாடாளுமன்றம் FRs-ஐ திருத்த முடியாது என்றது; அடிப்படைக் கட்டமைப்புக் கோட்பாட்டை உருவாக்கவில்லை.",
        "Correct. Kesavananda Bharati (1973) created the Basic Structure Doctrine.", "சரி. கேசவாநந்த பாரதி (1973) அடிப்படைக் கட்டமைப்புக் கோட்பாட்டை உருவாக்கியது.",
        "Minerva Mills (1980) applied and reaffirmed the doctrine by striking down Article 368(4) and (5).", "மினர்வா மில்ஸ் (1980) உறுப்பு 368(4) மற்றும் (5)-ஐ ரத்து செய்து இக்கோட்பாட்டை மீண்டும் உறுதிப்படுத்தியது.",
        "Maneka Gandhi (1978) expanded the scope of Article 21.", "மேனகா காந்தி வழக்கு (1978) உறுப்பு 21-ன் வரம்பை விரிவுபடுத்தியது.",
        "The date of the Kesavananda judgment (24 April 1973) is the constitutional cut-off for Ninth Schedule immunity.",
        "கேசவாநந்தா தீர்ப்பு நாள் (24 ஏப்ரல் 1973) ஒன்பதாவது அட்டவணைப் பாதுகாப்பிற்கான கால எல்லையாகும்.",
        "Kesavananda Bharati was decided by the largest ever constitutional bench of 13 judges in Indian legal history.",
        "இந்திய சட்ட வரலாற்றிலேயே 13 நீதிபதிகள் கொண்ட மிகப் பெரிய அரசியலமைப்பு அமர்வால் கேசவாநந்த பாரதி வழக்கு விசாரிக்கப்பட்டது."
    ))

    # 6 - A
    questions.append(make_jrap_q(
        "JRAP_E_006", "Easy", "single_choice", "Heart and Soul",
        "Who described Article 32 as 'an Article without which this Constitution would be a nullity... the very soul of the Constitution and the very heart of it'?",
        "உறுப்பு 32 இல்லாமல் இந்த அரசியலமைப்பு ஒரு பயனற்றதாகிவிடும்... அதுவே அரசியலமைப்பின் ஆன்மா மற்றும் அதன் இதயம் என்று வர்ணித்தவர் யார்?",
        "Dr. B.R. Ambedkar", "டாக்டர் பி.ஆர். அம்பேத்கர்",
        "Jawaharlal Nehru", "ஜவஹர்லால் நேரு",
        "Dr. Rajendra Prasad", "டாக்டர் ராஜேந்திர பிரசாத்",
        "Sardar Vallabhbhai Patel", "சர்தார் வல்லபாய் படேல்",
        "A",
        "Dr. B.R. Ambedkar in the Constituent Assembly highlighted that Article 32 is the most important Article providing judicial remedy for fundamental rights.",
        "அரசியலமைப்பு நிர்ணய சபையில் டாக்டர் பி.ஆர். அம்பேத்கர், அடிப்படை உரிமைகளுக்கான நீதித்துறைப் பரிகாரத்தை வழங்கும் உறுப்பு 32 மிக முக்கியமான உறுப்பு என்று சுட்டிக்காட்டினார்.",
        "Correct. Dr. B.R. Ambedkar called Article 32 the 'Heart and Soul of the Constitution'.", "சரி. டாக்டர் அம்பேத்கர் உறுப்பு 32-ஐ 'அரசியலமைப்பின் இதயம் மற்றும் ஆன்மா' என்றார்.",
        "Jawaharlal Nehru called the Preamble the declaration of resolve.", "நேரு முகப்புரையை உறுதிமொழியின் பிரகடனம் என்றார்.",
        "Dr. Rajendra Prasad was the President of the Constituent Assembly.", "டாக்டர் ராஜேந்திர பிரசாத் நிர்ணய சபையின் தலைவராக இருந்தார்.",
        "Sardar Patel headed the Advisory Committee on Fundamental Rights and Minorities.", "சர்தார் படேல் அடிப்படை உரிமைகள் மற்றும் சிறுபான்மையினர் ஆலோசனைக் குழுவிற்குத் தலைமை தாங்கினார்.",
        "Without Article 32, Fundamental Rights in Part III would be mere paper declarations without judicial teeth.",
        "உறுப்பு 32 இல்லையெனில் பகுதி III உரிமைகள் நீதித்துறைப் பலமற்ற வெறும் காகிதப் பிரகடனமாகவே இருக்கும்.",
        "Article 32 cannot be suspended except as provided under Article 359 during a National Emergency.",
        "தேசிய அவசரநிலையின் போது உறுப்பு 359-ன் கீழ் தவிர உறுப்பு 32 இடைநிறுத்தம் செய்யப்பட முடியாது."
    ))

    # 7 - C
    questions.append(make_jrap_q(
        "JRAP_E_007", "Easy", "single_choice", "Writs Count",
        "How many types of prerogative writs can be issued by the Supreme Court and High Courts under Articles 32 and 226?",
        "உறுப்புகள் 32 மற்றும் 226-ன் கீழ் உச்ச நீதிமன்றம் மற்றும் உயர் நீதிமன்றங்களால் எத்தனை வகையான நீதிப்பேராணைகள் வெளியிடப்படலாம்?",
        "3", "3",
        "4", "4",
        "5", "5",
        "6", "6",
        "C",
        "There are 5 types of writs borrowed from English Law: Habeas Corpus, Mandamus, Prohibition, Certiorari, and Quo-Warranto.",
        "ஆங்கிலச் சட்டத்திலிருந்து பெறப்பட்ட 5 வகையான நீதிப்பேராணைகள் உள்ளன: ஆட்கொணர்வு, கட்டளையிடும், தடையுறுத்தும், ஆவணக் கேட்பு மற்றும் தகுதிமுறை வினவும் நீதிப்பேராணைகள்.",
        "Incorrect. 3 is too few.", "தவறு. 3 என்பது குறைவான எண்ணிக்கை.",
        "Incorrect. 4 is incomplete.", "தவறு. 4 என்பது முழுமையற்றது.",
        "Correct. There are 5 well-defined prerogative writs in Indian constitutional law.", "சரி. இந்திய அரசியலமைப்புச் சட்டத்தில் 5 நீதிப்பேராணைகள் உள்ளன.",
        "Incorrect. There are only 5 constitutional writs.", "தவறு. 5 அரசியலமைப்பு நீதிப்பேராணைகளே உள்ளன.",
        "Memorize the 5 writs: Habeas Corpus, Mandamus, Prohibition, Certiorari, and Quo-Warranto.",
        "5 நீதிப்பேராணைகளை நினைவில் கொள்க: ஆட்கொணர்வு, கட்டளை, தடையுறுத்து, ஆவணக் கேட்பு, தகுதி வினவு.",
        "In English law, writs were originally issued under the royal prerogative and were called prerogative writs.",
        "ஆங்கிலச் சட்டத்தில் நீதிப்பேராணைகள் மன்னரின் சிறப்புரிமையின் கீழ் பிறப்பிக்கப்பட்டதால் சிறப்புரிமைப் பேராணைகள் எனப்பட்டன."
    ))

    # 8 - B
    questions.append(make_jrap_q(
        "JRAP_E_008", "Easy", "single_choice", "Habeas Corpus",
        "What does the Latin legal term 'Habeas Corpus' literally translate to?",
        "'ஹேபியஸ் கார்பஸ்' (Habeas Corpus) என்ற லத்தீன் சட்டச் சொல்லின் நேரடிப் பொருள் என்ன?",
        "We Command", "நாங்கள் கட்டளையிடுகிறோம்",
        "To Have the Body of", "உடலைக் கொண்டு வருக (ஆளை முன்னிலைப்படுத்துக)",
        "By What Authority", "எந்த அதிகாரத்தின் கீழ்",
        "To Be Certified", "சான்றளிக்கப்பட வேண்டும்",
        "B",
        "'Habeas Corpus' literally means 'to have the body of'. It is an order issued by the court to a person who has detained another person, to produce the body of the latter.",
        "'ஹேபியஸ் கார்பஸ்' என்பது நேரடிப் பொருளில் 'உடலைக் கொண்டு வருக' என்பதாகும். ஒருவரைச் சிறைபிடித்த நபருக்கு, சிறைபிடிக்கப்பட்டவரை நீதிமன்றத்தின் முன் முன்னிலைப்படுத்துமாறு பிறப்பிக்கப்படும் ஆணை.",
        "'We Command' is the literal translation of Mandamus.", "'நாங்கள் கட்டளையிடுகிறோம்' என்பது மாண்டமஸ் என்பதன் பொருள்.",
        "Correct. Habeas Corpus means 'to have the body of'.", "சரி. ஹேபியஸ் கார்பஸ் என்றால் 'உடலைக் கொண்டு வருக' என்று பொருள்.",
        "'By What Authority' is the literal translation of Quo-Warranto.", "'எந்த அதிகாரத்தின் கீழ்' என்பது குவோ-வாரண்டோவின் பொருள்.",
        "'To Be Certified' is the literal translation of Certiorari.", "'சான்றளிக்கப்பட வேண்டும்' என்பது செர்சியோராரியின் பொருள்.",
        "Habeas Corpus can be issued against both public authorities and private individuals.",
        "ஆட்கொணர்வு நீதிப்பேராணை அரசு அதிகாரிகள் மற்றும் தனிநபர்கள் ஆகிய இருவருக்கும் எதிராக வெளியிடப்படலாம்.",
        "Habeas Corpus is known as the bulwark of individual liberty against arbitrary detention.",
        "தன்னிச்சையான தடுப்புக் காவலுக்கு எதிராக தனிநபர் சுதந்திரத்தின் பாதுகாப்புக் கோட்டையாக ஆட்கொணர்வு விளங்குகிறது."
    ))

    # 9 - D
    questions.append(make_jrap_q(
        "JRAP_E_009", "Easy", "single_choice", "Mandamus",
        "What is the literal meaning of the writ of 'Mandamus'?",
        "'மாண்டமஸ்' (Mandamus) என்ற நீதிப்பேராணையின் நேரடிப் பொருள் என்ன?",
        "To have the body", "உடலைக் கொண்டு வருக",
        "To be informed", "தகவல் தெரிவிக்கப்பட வேண்டும்",
        "By what warrant", "எந்த அதிகார ஆணைப்படி",
        "We Command", "நாங்கள் கட்டளையிடுகிறோம்",
        "D",
        "'Mandamus' literally means 'We Command'. It is a command issued by the court to a public official asking him to perform an official duty that he has failed or refused to perform.",
        "'மாண்டமஸ்' என்பது 'நாங்கள் கட்டளையிடுகிறோம்' என்பதாகும். தனது பொதுக் கடமையைச் செய்யத் தவறிய அல்லது மறுத்த ஓர் அரசு அதிகாரிக்கு அதைச் செய்யுமாறு நீதிமன்றம் பிறப்பிக்கும் கட்டளை.",
        "'To have the body' is Habeas Corpus.", "'உடலைக் கொண்டு வருக' என்பது ஆட்கொணர்வு.",
        "'To be informed' relates to Certiorari.", "'தகவல் தெரிவிக்கப்பட வேண்டும்' என்பது ஆவணக் கேட்பு பற்றியது.",
        "'By what warrant' is Quo-Warranto.", "'எந்த அதிகார ஆணைப்படி' என்பது தகுதி வினவுதல்.",
        "Correct. Mandamus literally translates to 'We Command'.", "சரி. மாண்டமஸ் என்றால் 'நாங்கள் கட்டளையிடுகிறோம்' என்று பொருள்.",
        "Mandamus cannot be issued against a private individual or private body.",
        "ஒரு தனிநபர் அல்லது தனியார் அமைப்பிற்கு எதிராக கட்டளையிடும் பேராணையைப் பிறப்பிக்க முடியாது.",
        "Mandamus cannot be issued against the President of India or State Governors for the exercise of their official powers.",
        "இந்தியக் குடியரசுத் தலைவர் அல்லது மாநில ஆளுநர்களுக்கு எதிராக அவர்களின் அதிகாரச் செயல்பாட்டிற்காக மாண்டமஸ் பிறப்பிக்க முடியாது."
    ))

    # 10 - A
    questions.append(make_jrap_q(
        "JRAP_E_010", "Easy", "single_choice", "Quo-Warranto",
        "Which writ is issued by the court to enquire into the legality of a claim of a person to a public office?",
        "ஒரு நபர் பொதுப் பதவியை வகிக்கும் உரிமையின் சட்டபூர்வமான தன்மையை விசாரிக்க நீதிமன்றத்தால் பிறப்பிக்கப்படும் நீதிப்பேராணை எது?",
        "Quo-Warranto", "தகுதிமுறை வினவும் நீதிப்பேராணை (Quo-Warranto)",
        "Mandamus", "கட்டளையிடும் நீதிப்பேராணை (Mandamus)",
        "Prohibition", "தடையுறுத்தும் நீதிப்பேராணை (Prohibition)",
        "Certiorari", "ஆவணக் கேட்பு நீதிப்பேராணை (Certiorari)",
        "A",
        "Quo-Warranto literally means 'by what authority or warrant'. It prevents illegal usurpation of a public office by a person.",
        "குவோ-வாரண்டோ என்றால் 'எந்த அதிகாரத்தின் கீழ்' என்பதாகும். ஒரு நபர் பொதுப் பதவியை சட்டவிரோதமாக அபகரிப்பதைத் தடுக்க இது பிறப்பிக்கப்படுகிறது.",
        "Correct. Quo-Warranto challenges the usurpation of a substantive public office.", "சரி. பொதுப் பதவியை முறையற்ற வகையில் வகிப்பதை தகுதிமுறை வினவும் பேராணை தடுக்கிறது.",
        "Mandamus commands the performance of a public duty.", "மாண்டமஸ் பொதுக் கடமையைச் செய்யக் கட்டளையிடுகிறது.",
        "Prohibition stops a lower court from exceeding jurisdiction.", "தடையுறுத்தும் பேராணை கீழ் நீதிமன்றம் வரம்பை மீறுவதைத் தடுக்கிறது.",
        "Certiorari quashes an order of a lower court.", "ஆவணக் கேட்பு பேராணை கீழ் நீதிமன்றத்தின் உத்தரவை ரத்து செய்கிறது.",
        "Unlike other writs, Quo-Warranto can be sought by any interested person, not necessarily by the aggrieved person.",
        "பிற நீதிப்பேராணைகளைப் போலன்றி, பாதிக்கப்பட்ட நபராக இருக்க வேண்டிய அவசியமின்றி ஆர்வமுள்ள எந்தவொரு நபராலும் குவோ-வாரண்டோ கோரப்படலாம்.",
        "Quo-Warranto cannot be issued in respect of a private office or ministerial office.",
        "தனியார் அலுவலகம் அல்லது அமைச்சர் பதவி தொடர்பாக தகுதி வினவும் நீதிப்பேராணையைப் பிறப்பிக்க முடியாது."
    ))

    # Continue questions 11 to 50 with varied keys and rich content...
    easy_data = [
        # 11 - C
        ("JRAP_E_011", "Prohibition vs Certiorari",
         "Which writ is preventive in nature and issued by a higher court to a lower court to prevent it from exceeding its jurisdiction?",
         "எந்த நீதிப்பேராணை தடுப்புத் தன்மை கொண்டதாகவும், கீழ் நீதிமன்றம் தனது அதிகார வரம்பை மீறுவதைத் தடுக்க மேல் நீதிமன்றத்தால் பிறப்பிக்கப்படுவதாகவும் உள்ளது?",
         "Mandamus", "மாண்டமஸ்", "Quo-Warranto", "குவோ-வாரண்டோ", "Prohibition", "தடையுறுத்தும் பேராணை (Prohibition)", "Habeas Corpus", "ஹேபியஸ் கார்பஸ்", "C",
         "Prohibition is preventive: it is issued while proceedings are pending to prevent excess of jurisdiction.",
         "தடையுறுத்தும் பேராணை தடுப்புத் தன்மை கொண்டது: வழக்கு நிலுவையில் உள்ளபோதே அதிகார வரம்பு மீறலைத் தடுக்க இது பிறப்பிக்கப்படுகிறது."),

        # 12 - D
        ("JRAP_E_012", "Certiorari Scope",
         "Which writ is both preventive and curative in nature, issued to quash an order already passed by a lower court or tribunal lacking jurisdiction?",
         "எந்த நீதிப்பேராணை தடுப்பு மற்றும் தீர்வு ஆகிய இரு தன்மைகளையும் கொண்டதாகவும், அதிகார வரம்பின்றி கீழ் நீதிமன்றம் பிறப்பித்த உத்தரவை ரத்து செய்ய உதவுவதாகவும் உள்ளது?",
         "Mandamus", "மாண்டமஸ்", "Prohibition", "புரோஹிபிஷன்", "Quo-Warranto", "குவோ-வாரண்டோ", "Certiorari", "ஆவணக் கேட்பு பேராணை (Certiorari)", "D",
         "Certiorari is curative as well as preventive. It quashes the illegal order of a lower court/tribunal.",
         "செர்சியோராரி என்பது தீர்வு மற்றும் தடுப்பு ஆகிய இரு தன்மைகளையும் கொண்டது. இது கீழ் நீதிமன்றத்தின் சட்டவிரோத உத்தரவை ரத்து செய்கிறது."),

        # 13 - B
        ("JRAP_E_013", "Article 227 Superintendence",
         "Under Article 227 of the Constitution, every High Court has power of superintendence over:",
         "அரசியலமைப்பு உறுப்பு 227-ன் கீழ், ஒவ்வொரு உயர் நீதிமன்றமும் எதன் மீது மேற்பார்வை அதிகாரத்தைக் கொண்டுள்ளது?",
         "Only District Courts", "மாவட்ட நீதிமன்றங்கள் மீது மட்டுமே",
         "All courts and tribunals throughout the territories in relation to which it exercises jurisdiction", "தனது அதிகார வரம்பிற்குட்பட்ட பகுதி முழுவதிலும் உள்ள அனைத்து நீதிமன்றங்கள் மற்றும் தீர்ப்பாயங்கள் மீது",
         "Only Supreme Court subordinate benches", "உச்ச நீதிமன்ற கீழ்மை அமர்வுகள் மீது மட்டுமே",
         "Only administrative tribunals set up under Art. 323A", "உறுப்பு 323A கீழ் அமைக்கப்பட்ட நிர்வாக தீர்ப்பாயங்கள் மீது மட்டுமே", "B",
         "Article 227 gives High Courts administrative and judicial superintendence over all courts and tribunals within their territorial jurisdiction (except armed forces tribunals).",
         "உறுப்பு 227 உயர் நீதிமன்றங்களுக்கு தனது எல்லைக்குட்பட்ட அனைத்து நீதிமன்றங்கள் மற்றும் தீர்ப்பாயங்கள் மீது நிர்வாக மற்றும் நீதித்துறை மேற்பார்வை அதிகாரத்தை வழங்குகிறது (ராணுவ தீர்ப்பாயங்கள் தவிர)."),

        # 14 - A
        ("JRAP_E_014", "PIL Pioneers",
         "Which eminent Supreme Court judge is famously known as the 'Father of Public Interest Litigation (PIL)' in India?",
         "இந்தியாவில் 'பொது நல வழக்கின் (PIL) தந்தை' என்று பிரபலமாக அழைக்கப்படும் உச்ச நீதிமன்ற நீதிபதி யார்?",
         "Justice P.N. Bhagwati", "நீதிபதி பி.என். பகவதி",
         "Justice H.R. Khanna", "நீதிபதி எச்.ஆர். கன்னா",
         "Justice M. Patanjali Sastri", "நீதிபதி எம். பதஞ்சலி சாஸ்திரி",
         "Justice K. Subba Rao", "நீதிபதி கே. சுப்பா ராவ்", "A",
         "Justice P.N. Bhagwati, along with Justice V.R. Krishna Iyer, pioneered Public Interest Litigation (PIL) in India in the late 1970s.",
         "1970களின் பிற்பகுதியில் நீதிபதி பி.என். பகவதி மற்றும் நீதிபதி வி.ஆர். கிருஷ்ண ஐயர் ஆகியோர் இந்தியாவில் பொது நல வழக்கைத் தொடங்கினர்."),

        # 15 - C
        ("JRAP_E_015", "First PIL Case",
         "Which case is recognized as the first reported Public Interest Litigation (PIL) in India?",
         "இந்தியாவின் முதல் பொது நல வழக்காக (PIL) அங்கீகரிக்கப்பட்ட வழக்கு எது?",
         "Kesavananda Bharati Case (1973)", "கேசவாநந்த பாரதி வழக்கு (1973)",
         "Maneka Gandhi Case (1978)", "மேனகா காந்தி வழக்கு (1978)",
         "Hussainara Khatoon v. Home Secretary, State of Bihar (1979)", "ஹுசைனாரா காதுன் v. உள்துறைச் செயலாளர், பீகார் மாநிலம் (1979)",
         "Minerva Mills v. Union of India (1980)", "மினர்வா மில்ஸ் v. இந்திய ஒன்றியம் (1980)", "C",
         "Hussainara Khatoon (1979) was filed on behalf of thousands of undertrial prisoners languishing in Bihar jails, securing the release of over 40,000 undertrials.",
         "ஹுசைனாரா காதுன் (1979) வழக்கு பீகார் சிறைகளில் வாடும் ஆயிரக்கணக்கான விசாரணைக் கைதிகளுக்காகத் தொடரப்பட்டு, 40,000-க்கும் மேற்பட்டோரின் விடுதலையை உறுதி செய்தது."),

        # 16 - B
        ("JRAP_E_016", "Locus Standi",
         "What traditional legal rule was fundamentally relaxed by the judiciary to give birth to Public Interest Litigation?",
         "பொது நல வழக்கு பிறப்பதற்கு நீதித்துறையால் எந்த பாரம்பரிய சட்ட விதி அடிப்படையில் தளர்த்தப்பட்டது?",
         "Rule of Res Judicata", "முன் தீர்ப்புத் தடை விதி (Res Judicata)",
         "Rule of Locus Standi", "வழக்குத் தொடுக்கும் தகுதி விதி (Locus Standi)",
         "Rule of Sub Judice", "நீதிமன்ற விசாரணையில் உள்ள விதி (Sub Judice)",
         "Rule of Double Jeopardy", "இரட்டைத் தண்டனை விதி (Double Jeopardy)", "B",
         "Locus Standi (standing to sue) requires the petitioner to be personally aggrieved. PIL relaxed this to allow any public-spirited citizen to move the court for disadvantaged groups.",
         "வழக்குத் தொடுக்கும் உரிமை (Locus Standi) மனுதாரர் பாதிக்கப்பட்டவராக இருக்க வேண்டும் எனக் கோருகிறது. எளிய மக்களுக்காக எவரும் நீதிமன்றத்தை அணுக PIL இதைத் தளர்த்தியது."),

        # 17 - D
        ("JRAP_E_017", "Epistolary Jurisdiction",
         "The practice of treating letters, postcards, and telegrams sent to the Supreme Court as formal writ petitions is known as:",
         "உச்ச நீதிமன்றத்திற்கு அனுப்பப்படும் கடிதங்கள், அஞ்சல் அட்டைகள் மற்றும் தந்திகளை முறையான நீதிப்பேராணை மனுக்களாக ஏற்கும் நடைமுறை எவ்வாறு அழைக்கப்படுகிறது?",
         "Advisory Jurisdiction", "ஆலோசனை அதிகார வரம்பு",
         "Appellate Jurisdiction", "மேல்முறையீட்டு அதிகார வரம்பு",
         "Supervisory Jurisdiction", "மேற்பார்வை அதிகார வரம்பு",
         "Epistolary Jurisdiction", "கடித அதிகார வரம்பு (Epistolary Jurisdiction)", "D",
         "Epistolary jurisdiction allows citizens to trigger constitutional remedies by writing a simple letter or postcard to judges.",
         "கடித அதிகார வரம்பு என்பது நீதிபதிகளுக்கு எளிய கடிதம் அல்லது அஞ்சல் அட்டை எழுதுவதன் மூலம் குடிமக்கள் அரசியலமைப்புப் பரிகாரங்களைத் தூண்ட அனுமதிக்கிறது."),

        # 18 - A
        ("JRAP_E_018", "Article 136 Special Leave",
         "Under which Article can the Supreme Court grant Special Leave to Appeal (SLP) against any judgment, decree or order of any court or tribunal?",
         "எந்த உறுப்பின் கீழ் உச்ச நீதிமன்றம் எந்தவொரு நீதிமன்றம் அல்லது தீர்ப்பாயத்தின் தீர்ப்பு அல்லது உத்தரவுக்கு எதிராக மேல்முறையீடு செய்ய சிறப்பு விடுப்பு (SLP) வழங்க முடியும்?",
         "Article 136", "உறுப்பு 136",
         "Article 131", "உறுப்பு 131",
         "Article 137", "உறுப்பு 137",
         "Article 143", "உறுப்பு 143", "A",
         "Article 136 grants the Supreme Court extraordinary discretionary power to grant special leave to appeal from any court or tribunal in India (except military tribunals).",
         "உறுப்பு 136 உச்ச நீதிமன்றத்திற்கு இந்தியாவில் உள்ள எந்தவொரு நீதிமன்றம் அல்லது தீர்ப்பாயத்திலிருந்தும் (ராணுவ தீர்ப்பாயங்கள் தவிர) மேல்முறையீடு செய்ய சிறப்பு விடுப்பு வழங்கும் விவேக அதிகாரத்தை அளிக்கிறது."),

        # 19 - C
        ("JRAP_E_019", "Article 142 Complete Justice",
         "Which Article of the Constitution empowers the Supreme Court to pass any decree or make any order necessary for doing 'complete justice' in any cause or matter?",
         "அரசியலமைப்பின் எந்த உறுப்பு உச்ச நீதிமன்றத்திற்கு தனது முன் உள்ள வழக்கில் 'முழுமையான நீதியை' வழங்குவதற்குத் தேவையான எந்தவொரு ஆணை அல்லது உத்தரவைப் பிறப்பிக்க அதிகாரம் அளிக்கிறது?",
         "Article 140", "உறுப்பு 140",
         "Article 141", "உறுப்பு 141",
         "Article 142", "உறுப்பு 142",
         "Article 144", "உறுப்பு 144", "C",
         "Article 142(1) confers plenary power upon the Supreme Court to pass any decree or order to do complete justice, which has been an engine of judicial activism.",
         "உறுப்பு 142(1) முழுமையான நீதியை நிலைநாட்ட உச்ச நீதிமன்றத்திற்கு முழுமையான அதிகாரத்தை வழங்குகிறது; இது நீதித்துறை செயல்பாட்டின் முக்கிய உந்துசக்தியாக உள்ளது."),

        # 20 - B
        ("JRAP_E_020", "Article 141 Law of the Land",
         "According to Article 141 of the Indian Constitution, the law declared by the Supreme Court shall be binding on:",
         "இந்திய அரசியலமைப்பு உறுப்பு 141-ன் படி, உச்ச நீதிமன்றத்தால் அறிவிக்கப்பட்ட சட்டம் எதன் மீது கட்டுப்படும்?",
         "Only High Courts", "உயர் நீதிமன்றங்கள் மீது மட்டுமே",
         "All courts within the territory of India", "இந்திய நிலப்பரப்பிற்குள் உள்ள அனைத்து நீதிமன்றங்கள் மீதும்",
         "Only Central Government departments", "மத்திய அரசுத் துறைகள் மீது மட்டுமே",
         "Only Subordinate District Courts", "சார்நிலை மாவட்ட நீதிமன்றங்கள் மீது மட்டுமே", "B",
         "Article 141 states that the law declared by the Supreme Court shall be binding on all courts within the territory of India.",
         "உறுப்பு 141 உச்ச நீதிமன்றத்தால் அறிவிக்கப்படும் சட்டம் இந்திய எல்லைக்குள் உள்ள அனைத்து நீதிமன்றங்களையும் கட்டுப்படுத்தும் எனக் கூறுகிறது."),

        # 21 - D
        ("JRAP_E_021", "Judicial Review of Ordinances",
         "Can an Ordinance promulgated by the President (Art. 123) or a Governor (Art. 213) be subjected to Judicial Review?",
         "குடியரசுத் தலைவர் (உறுப்பு 123) அல்லது ஆளுநரால் (உறுப்பு 213) பிறப்பிக்கப்படும் ஓர் அவசரச்சட்டம் நீதித்துறை மறுஆய்வுக்கு உட்படுத்தப்பட முடியுமா?",
         "No, ordinances are executive acts immune from judicial scrutiny", "இல்லை, அவசரச்சட்டங்கள் நீதித்துறை ஆய்விலிருந்து பாதுகாப்பு பெற்ற நிர்வாகச் செயல்கள்",
         "Only if the President gives permission", "குடியரசுத் தலைவர் அனுமதி அளித்தால் மட்டுமே",
         "Only if approved by Parliament", "நாடாளுமன்றத்தால் அங்கீகரிக்கப்பட்டால் மட்டுமே",
         "Yes, if it is promulgated malafide or in colourable exercise of power", "ஆம், அது துர்நோக்கத்துடனோ அல்லது போலி அதிகாரப் பிரயோகத்துடனோ பிறப்பிக்கப்பட்டால் மறுஆய்வு செய்யலாம்", "D",
         "In DC Wadhwa (1987) and Krishna Kumar Singh (2017), Supreme Court held that ordinance-making power is subject to judicial review and cannot bypass legislature.",
         "டி.சி. வாத்வா (1987) மற்றும் கிருஷ்ண குமார் சிங் (2017) வழக்குகளில் அவசரச்சட்டம் இயற்றும் அதிகாரம் நீதித்துறை மறுஆய்வுக்கு உட்பட்டது என உச்ச நீதிமன்றம் தீர்ப்பளித்தது."),

        # 22 - A
        ("JRAP_E_022", "Pardoning Power Review",
         "Can the pardoning power of the President (Art. 72) and the Governor (Art. 161) be examined under Judicial Review?",
         "குடியரசுத் தலைவரின் (உறுப்பு 72) மற்றும் ஆளுநரின் (உறுப்பு 161) மன்னிப்பளிக்கும் அதிகாரம் நீதித்துறை மறுஆய்வின் கீழ் பரிசீலிக்கப்பட முடியுமா?",
         "Yes, on grounds of arbitrariness, malafide, or non-application of mind", "ஆம், தன்னிச்சைத் தன்மை, துர்நோக்கம் அல்லது கவனம் செலுத்தாமை ஆகிய காரணங்களின் அடிப்படையில்",
         "No, it is an absolute royal prerogative completely outside judicial scrutiny", "இல்லை, இது நீதித்துறை ஆய்வுக்கு முற்றிலும் அப்பாற்பட்ட முழுமையான இறையாண்மை அதிகாரம்",
         "Only with prior consent of the Attorney General", "இந்திய தலைமை வழக்கறிஞரின் முன் அனுமதியுடன் மட்டுமே",
         "Only by a 9-judge constitutional bench", "9 நீதிபதிகள் கொண்ட அரசியலமைப்பு அமர்வால் மட்டுமே", "A",
         "In Epuru Sudhakar (2006) and Kehar Singh (1989), SC held that the pardoning power is subject to limited judicial review against arbitrariness and malafide.",
         "எப்புரு சுதாகர் (2006) மற்றும் கேஹர் சிங் (1989) வழக்குகளில் தன்னிச்சை மற்றும் துர்நோக்கத்திற்கு எதிராக மன்னிப்பளிக்கும் அதிகாரம் மறுஆய்வுக்கு உட்பட்டது எனப்பட்டது."),

        # 23 - C
        ("JRAP_E_023", "Judicial Review of Speaker Decisions",
         "Is the decision of the Speaker regarding disqualification under the Tenth Schedule subject to Judicial Review?",
         "பத்தாவது அட்டவணையின் கீழ் தகுதிநீக்கம் செய்வது தொடர்பான சபாநாயகரின் முடிவு நீதித்துறை மறுஆய்வுக்கு உட்பட்டதா?",
         "No, Speaker's decision is final and non-justiciable under Para 6(1)", "இல்லை, பாரா 6(1)-ன் கீழ் சபாநாயகரின் முடிவே இறுதியானது மற்றும் நீதிமன்ற விசாரணைக்கு அப்பாற்பட்டது",
         "Only if referred by the Governor", "ஆளுநரால் பரிந்துரைக்கப்பட்டால் மட்டுமே",
         "Yes, as established in the Kihoto Hollohan Case (1992)", "ஆம், கிஹோட்டோ ஹோல்லோஹன் வழக்கில் (1992) நிறுவப்பட்டபடி",
         "Only if the Speaker is removed from office", "சபாநாயகர் பதவியிலிருந்து நீக்கப்பட்டால் மட்டுமே", "C",
         "In Kihoto Hollohan (1992), SC struck down Para 7 of 10th Schedule, declaring the Speaker acts as a tribunal and decisions are subject to judicial review under Arts. 136, 226, and 227.",
         "கிஹோட்டோ ஹோல்லோஹன் (1992) வழக்கில் 10வது அட்டவணையின் பாரா 7-ஐ ரத்து செய்து, சபாநாயகர் ஒரு தீர்ப்பாயமாகச் செயல்படுவதால் அவரது முடிவு மறுஆய்வுக்கு உட்பட்டது எனப்பட்டது."),

        # 24 - B
        ("JRAP_E_024", "President's Rule Judicial Review",
         "In which landmark case did the Supreme Court hold that the proclamation of President's Rule under Article 356 is subject to Judicial Review?",
         "எந்த வரலாற்றுச் சிறப்புமிக்க வழக்கில் உறுப்பு 356-ன் கீழ் குடியரசுத் தலைவர் ஆட்சி பிரகடனம் நீதித்துறை மறுஆய்வுக்கு உட்பட்டது என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது?",
         "Minerva Mills Case (1980)", "மினர்வா மில்ஸ் வழக்கு (1980)",
         "S.R. Bommai v. Union of India (1994)", "எஸ்.ஆர். பொம்மை v. இந்திய ஒன்றியம் (1994)",
         "Indira Sawhney Case (1992)", "இந்திரா சாவ்னி வழக்கு (1992)",
         "Golaknath Case (1967)", "கோலக்நாத் வழக்கு (1967)", "B",
         "In S.R. Bommai (1994), a 9-judge bench ruled that Article 356 proclamation is subject to judicial review, and if found malafide, the dissolved Assembly can be revived.",
         "எஸ்.ஆர். பொம்மை (1994) வழக்கில் 9 நீதிபதிகள் அமர்வு உறுப்பு 356 பிரகடனம் மறுஆய்வுக்கு உட்பட்டது என்றும், துர்நோக்கம் உடையதாக இருந்தால் கலைக்கப்பட்ட சட்டப்பேரவையை மீண்டும் உயிர்ப்பிக்கலாம் என்றும் தீர்ப்பளித்தது."),

        # 25 - D
        ("JRAP_E_025", "Basic Structure in S.R. Bommai",
         "Which concept was declared as part of the 'Basic Structure' of the Indian Constitution in the S.R. Bommai Case (1994)?",
         "எஸ்.ஆர். பொம்மை வழக்கில் (1994) இந்திய அரசியலமைப்பின் 'அடிப்படைக் கட்டமைப்பின்' ஒரு பகுதியாக அறிவிக்கப்பட்ட கருத்து எது?",
         "Right to Property", "சொத்துரிமை",
         "Collegiate Executive", "கூட்டு நிர்வாக முறை",
         "Bicameralism in all States", "அனைத்து மாநிலங்களிலும் இரு அவைகள் முறை",
         "Secularism and Federalism", "மதச்சார்பின்மை மற்றும் கூட்டாட்சித் தத்துவம்", "D",
         "The Supreme Court in S.R. Bommai (1994) held that Secularism and Federalism are essential elements of the Basic Structure.",
         "எஸ்.ஆர். பொம்மை (1994) வழக்கில் மதச்சார்பின்மை மற்றும் கூட்டாட்சி ஆகியவை அடிப்படைக் கட்டமைப்பின் இன்றியமையாத கூறுகள் என உச்ச நீதிமன்றம் தீர்ப்பளித்தது."),

        # 26 - A
        ("JRAP_E_026", "Minerva Mills 1980",
         "In Minerva Mills v. Union of India (1980), which provisions of the 42nd Amendment Act 1976 were struck down as unconstitutional?",
         "மினர்வா மில்ஸ் v. இந்திய ஒன்றியம் (1980) வழக்கில் 1976-ன் 42வது திருத்தச் சட்டத்தின் எந்தப் பிரிவுகள் அரசியலமைப்புக்கு முரணானவை என ரத்து செய்யப்பட்டன?",
         "Clauses (4) and (5) of Article 368", "உறுப்பு 368-ன் உட்பிரிவுகள் (4) மற்றும் (5)",
         "Article 31C entirely", "உறுப்பு 31C முழுமையாக",
         "Article 51A Fundamental Duties", "உறுப்பு 51A அடிப்படை கடமைகள்",
         "Preamble additions (Socialist, Secular)", "முகப்புரை சேர்த்தல்கள் (சமதர்ம, மதச்சார்பற்ற)", "A",
         "Clauses (4) and (5) of Article 368 sought to exclude judicial review and grant unlimited amending power to Parliament. Supreme Court struck them down.",
         "உறுப்பு 368-ன் உட்பிரிவுகள் (4) மற்றும் (5) நீதித்துறை மறுஆய்வைத் தடுத்து நாடாளுமன்றத்திற்கு வரம்பற்ற அதிகாரத்தை வழங்க முயன்றன. உச்ச நீதிமன்றம் அவற்றை ரத்து செய்தது."),

        # 27 - C
        ("JRAP_E_027", "Limited Amending Power",
         "The quote 'The Constitution has conferred a limited amending power on Parliament, and therefore Parliament cannot enlarge that limited power into an absolute power' belongs to which judgment?",
         "'அரசியலமைப்பு நாடாளுமன்றத்திற்கு வரம்பிற்குட்பட்ட திருத்தும் அதிகாரத்தையே வழங்கியுள்ளது, எனவே நாடாளுமன்றம் அந்த வரம்பிற்குட்பட்ட அதிகாரத்தை முழுமையான அதிகாரமாக விரிவாக்க முடியாது' என்ற மேற்கோள் எந்தத் தீர்ப்பைச் சார்ந்தது?",
         "Golaknath (1967)", "கோலக்நாத் (1967)",
         "Shankari Prasad (1951)", "சங்கரி பிரசாத் (1951)",
         "Minerva Mills (1980)", "மினர்வா மில்ஸ் (1980)",
         "I.R. Coelho (2007)", "I.R. கோயல்ஹோ (2007)", "C",
         "Chief Justice Y.V. Chandrachud in Minerva Mills (1980) observed that a limited amending power is one of the basic features of the Constitution.",
         "மினர்வா மில்ஸ் (1980) வழக்கில் தலைமை நீதிபதி சந்திரசூட், வரம்பிற்குட்பட்ட திருத்தும் அதிகாரமே அரசியலமைப்பின் அடிப்படைக் கூறுகளில் ஒன்றாகும் என்று குறிப்பிட்டார்."),

        # 28 - B
        ("JRAP_E_028", "Ninth Schedule Benchmark Date",
         "According to the I.R. Coelho Case (2007), laws added to the Ninth Schedule after which date are subject to Judicial Review on the touchstone of Basic Structure?",
         "I.R. கோயல்ஹோ வழக்கின் (2007) படி, எந்த தேதிக்குப் பிறகு ஒன்பதாவது அட்டவணையில் சேர்க்கப்பட்ட சட்டங்கள் அடிப்படைக் கட்டமைப்பு சோதனையின் கீழ் நீதித்துறை மறுஆய்வுக்கு உட்பட்டவை?",
         "26 January 1950", "26 ஜனவரி 1950",
         "24 April 1973", "24 ஏப்ரல் 1973",
         "42nd Amendment 1976", "42வது திருத்தம் 1976",
         "1 January 2000", "1 ஜனவரி 2000", "B",
         "In I.R. Coelho (2007), a 9-judge bench ruled that all laws placed in the Ninth Schedule on or after 24 April 1973 (the date of Kesavananda Bharati judgment) are subject to judicial review.",
         "I.R. கோயல்ஹோ (2007) வழக்கில் 9 நீதிபதிகள் அமர்வு, 24 ஏப்ரல் 1973 (கேசவாநந்தா தீர்ப்பு நாள்) அன்றோ அல்லது அதற்குப் பின்னரோ 9வது அட்டவணையில் சேர்க்கப்பட்ட சட்டங்கள் மறுஆய்வுக்கு உட்பட்டவை எனத் தீர்ப்பளித்தது."),

        # 29 - D
        ("JRAP_E_029", "Bonded Labour PIL",
         "In which landmark PIL did the Supreme Court order the release and rehabilitation of bonded labourers working in stone quarries near Delhi?",
         "டெல்லி அருகிலுள்ள கல் குவாரிகளில் பணிபுரியும் கொத்தடிமைத் தொழிலாளர்களை விடுவித்து மறுவாழ்வு அளிக்க உச்ச நீதிமன்றம் உத்தரவிட்ட வரலாற்றுச் சிறப்புமிக்க பொது நல வழக்கு எது?",
         "Hussainara Khatoon (1979)", "ஹுசைனாரா காதுன் (1979)",
         "Sunil Batra (1980)", "சுனில் பத்ரா (1980)",
         "Vishaka (1997)", "விசாகா (1997)",
         "Bandhua Mukti Morcha v. Union of India (1984)", "பந்துவா முக்தி மோர்ச்சா v. இந்திய ஒன்றியம் (1984)", "D",
         "Bandhua Mukti Morcha (1984) expanded Article 21 to include living with human dignity free from exploitation, ordering the release of bonded labourers under Art. 23.",
         "பந்துவா முக்தி மோர்ச்சா (1984) வழக்கு சுரண்டலற்ற மனித கண்ணியத்துடன் வாழ்வதை உறுப்பு 21-ல் இணைத்து, உறுப்பு 23-ன் கீழ் கொத்தடிமைகளை விடுவிக்க உத்தரவிட்டது."),

        # 30 - A
        ("JRAP_E_030", "Prisoner Rights PIL",
         "In Sunil Batra v. Delhi Administration (1980), the Supreme Court entertained a PIL sent in what format regarding torture of a prisoner in Tihar jail?",
         "சுனில் பத்ரா v. டெல்லி நிர்வாகம் (1980) வழக்கில் திகார் சிறையில் கைதி சித்திரவதை செய்யப்பட்டது தொடர்பான பொது நல வழக்கை உச்ச நீதிமன்றம் எந்த வடிவில் ஏற்றுக்கொண்டது?",
         "A handwritten letter by a prisoner", "ஒரு கைதி எழுதிய கையெழுத்துக் கடிதம்",
         "A formal writ petition through Senior Advocate", "மூத்த வழக்கறிஞர் மூலம் தாக்கல் செய்யப்பட்ட முறையான மனு",
         "A Presidential reference under Art. 143", "உறுப்பு 143 கீழ் குடியரசுத் தலைவர் குறிப்பு",
         "A State Legislative Resolution", "மாநில சட்டமன்றத் தீர்மானம்", "A",
         "Sunil Batra, a prisoner in Tihar, wrote a letter on a piece of paper about brutality inflicted on a fellow prisoner. Justice Krishna Iyer treated this letter as a habeas corpus petition.",
         "திகார் சிறைக் கைதியான சுனில் பத்ரா சக கைதி சித்திரவதை செய்யப்பட்டது குறித்து ஒரு தாளில் கடிதம் எழுதினார். நீதிபதி கிருஷ்ண ஐயர் அக்கடிதத்தை ஆட்கொணர்வு மனுவாக ஏற்றுக்கொண்டார்."),

        # 31 - C
        ("JRAP_E_031", "Environmental PIL",
         "Which renowned advocate is famously known as the 'Green Lawyer' of India for filing numerous landmark environmental PILs in the Supreme Court?",
         "உச்ச நீதிமன்றத்தில் பல வரலாற்றுச் சிறப்புமிக்க சுற்றுச்சூழல் பொது நல வழக்குகளைத் தாக்கல் செய்ததற்காக இந்தியாவின் 'பசுமை வழக்கறிஞர்' என்று அழைக்கப்படுபவர் யார்?",
         "Fali S. Nariman", "பாலி எஸ். நரிமன்",
         "Nani Palkhivala", "நானி பால்கிவாலா",
         "M.C. Mehta", "எம்.சி. மேத்தா",
         "K.K. Venugopal", "கே.கே. வேணுகோபால்", "C",
         "M.C. Mehta filed landmark PILs regarding the preservation of the Taj Mahal (Taj Trapezium), Ganga water pollution, Delhi vehicular pollution (CNG), and Oleum gas leak.",
         "எம்.சி. மேத்தா தாஜ்மஹால் பாதுகாப்பு, கங்கை நீர் மாசுபாடு, டெல்லி வாகன மாசுபாடு (CNG) மற்றும் ஓலியம் வாயு கசிவு தொடர்பான வரலாற்றுச் சிறப்புமிக்க PIL வழக்குகளைத் தொடர்ந்தார்."),

        # 32 - B
        ("JRAP_E_032", "Workplace Harassment Guidelines",
         "In Vishaka v. State of Rajasthan (1997), the Supreme Court formulated mandatory guidelines against sexual harassment of women at workplace under which constitutional provisions?",
         "விசாகா v. ராஜஸ்தான் மாநிலம் (1997) வழக்கில் பணியிடங்களில் பெண்களுக்கு எதிரான பாலியல் துன்புறுத்தலைத் தடுக்க உச்ச நீதிமன்றம் எந்த அரசியலமைப்பு விதிகளின் கீழ் வழிகாட்டுதல்களை வகுத்தது?",
         "Articles 105 and 194", "உறுப்புகள் 105 மற்றும் 194",
         "Articles 14, 19, 21 read with Article 141", "உறுப்புகள் 14, 19, 21 உடன் உறுப்பு 141",
         "Articles 323A and 323B", "உறுப்புகள் 323A மற்றும் 323B",
         "Articles 352 and 356", "உறுப்புகள் 352 மற்றும் 356", "B",
         "The Supreme Court in Vishaka (1997) invoked Articles 14, 19, and 21 along with international conventions (CEDAW) under Article 141 to lay down guidelines until legislation was enacted.",
         "விசாகா (1997) வழக்கில் சட்டம் இயற்றப்படும் வரை உறுப்பு 141-ன் கீழ் CEDAW மாநாட்டை இணைத்து உறுப்புகள் 14, 19, 21 அடிப்படையில் உச்ச நீதிமன்றம் வழிகாட்டுதல்களை வகுத்தது."),

        # 33 - D
        ("JRAP_E_033", "SP Gupta First Judges Case",
         "In S.P. Gupta v. Union of India (1981), famously known as the 'First Judges Case', what major procedural principle did Justice P.N. Bhagwati firmly establish regarding PIL?",
         "முதல் நீதிபதிகள் வழக்கு என அழைக்கப்படும் எஸ்.பி. குப்தா v. இந்திய ஒன்றியம் (1981) வழக்கில் நீதிபதி பி.என். பகவதி பொது நல வழக்கு தொடர்பாக எந்த முக்கிய நடைமுறைக் கொள்கையை உறுதியாக நிறுவினார்?",
         "PIL can only be filed by lawyers", "வழக்கறிஞர்கள் மட்டுமே PIL தாக்கல் செய்ய முடியும்",
         "PIL cannot be filed against the Central Government", "மத்திய அரசுக்கு எதிராக PIL தாக்கல் செய்ய முடியாது",
         "Only high courts have jurisdiction over PIL", "உயர் நீதிமன்றங்களுக்கு மட்டுமே PIL மீது அதிகார வரம்பு உண்டு",
         "Any member of the public having sufficient interest can maintain an action for redressal of public injury", "பொதுக் காயத்திற்குப் பரிகாரம் காண போதுமான அக்கறை கொண்ட எந்தவொரு பொதுநபரும் வழக்குத் தொடரலாம்", "D",
         "In S.P. Gupta (1981), the Supreme Court comprehensively liberalized the rule of standing, holding that any member of the public acting bona fide can invoke writ jurisdiction for the public good.",
         "எஸ்.பி. குப்தா (1981) வழக்கில், பொதுநலனுக்காக செயல்படும் எந்தவொரு பொதுநபரும் நீதிப்பேராணை அதிகார வரம்பைத் தூண்டலாம் என வழக்குத் தொடுக்கும் உரிமையை நீதிமன்றம் தாராளமயமாக்கியது."),

        # 34 - A
        ("JRAP_E_034", "Judicial Activism Term Origin",
         "In which country was the term 'Judicial Activism' first coined in 1947 by Arthur Schlesinger Jr.?",
         "1947-ல் ஆர்தர் ஷ்லேசிங்கர் ஜூனியர் என்பவரால் 'நீதித்துறை செயல்பாடு' (Judicial Activism) என்ற சொல் முதன்முதலில் எந்த நாட்டில் உருவாக்கப்பட்டது?",
         "United States of America", "அமெரிக்க ஐக்கிய நாடுகள்",
         "United Kingdom", "ஐக்கிய இராச்சியம்",
         "France", "பிரான்ஸ்",
         "India", "இந்தியா", "A",
         "The term 'Judicial Activism' was coined by American historian Arthur Schlesinger Jr. in an article titled 'The Supreme Court: 1947' in Fortune magazine.",
         "'நீதித்துறை செயல்பாடு' என்ற சொல்லை 1947-ல் பார்ச்சூன் இதழில் அமெரிக்க வரலாற்று ஆசிரியர் ஆர்தர் ஷ்லேசிங்கர் ஜூனியர் முதன்முதலில் அறிமுகப்படுத்தினார்."),

        # 35 - C
        ("JRAP_E_035", "Maneka Gandhi Golden Triangle",
         "Which three fundamental rights were linked together as the 'Golden Triangle' in the Maneka Gandhi Case (1978)?",
         "மேனகா காந்தி வழக்கில் (1978) எந்த மூன்று அடிப்படை உரிமைகள் 'தங்க முக்கோணம்' என ஒன்றோடொன்று இணைக்கப்பட்டன?",
         "Articles 12, 13, and 14", "உறுப்புகள் 12, 13, மற்றும் 14",
         "Articles 19, 20, and 21", "உறுப்புகள் 19, 20, மற்றும் 21",
         "Articles 14, 19, and 21", "உறுப்புகள் 14, 19, மற்றும் 21",
         "Articles 25, 26, and 27", "உறுப்புகள் 25, 26, மற்றும் 27", "C",
         "In Maneka Gandhi (1978), the Supreme Court held that Articles 14, 19, and 21 are not mutually exclusive but form a composite 'Golden Triangle' guaranteeing fairness and non-arbitrariness.",
         "மேனகா காந்தி (1978) வழக்கில் உறுப்புகள் 14, 19, மற்றும் 21 தனித்தனியானவை அல்ல; அவை நியாயத்தையும் தன்னிச்சையின்மையையும் உறுதி செய்யும் ஒருங்கிணைந்த 'தங்க முக்கோணம்' எனப்பட்டது."),

        # 36 - B
        ("JRAP_E_036", "Due Process of Law",
         "Which legal doctrine was effectively read into Article 21 by the Supreme Court in the Maneka Gandhi Case (1978)?",
         "மேனகா காந்தி வழக்கில் (1978) உச்ச நீதிமன்றத்தால் உறுப்பு 21-க்குள் நடைமுறை ரீதியாகக் கொண்டுவரப்பட்ட சட்டக் கோட்பாடு எது?",
         "Rule of Strict Construction", "கடுமையான பொருள் விளக்க விதி",
         "Due Process of Law", "சட்டத்தின் உரிய நடைமுறை (Due Process of Law)",
         "Separation of Powers", "அதிகாரப் பகிர்வு தத்துவம்",
         "Territorial Nexus", "நிலப்பரப்பு இணைப்பு தத்துவம்", "B",
         "Although Article 21 textually mentions 'procedure established by law', the SC in Maneka Gandhi ruled that the procedure must be 'just, fair and reasonable', importing the American 'Due Process' concept.",
         "உறுப்பு 21 'சட்டத்தால் உருவாக்கப்பட்ட நடைமுறை' எனக் குறிப்பிட்டாலும், அது 'நேர்மையான, நியாயமானதாக' இருக்க வேண்டும் என அமெரிக்க 'சட்டத்தின் உரிய நடைமுறை' கோட்பாட்டை நீதிமன்றம் புகுத்தியது."),

        # 37 - D
        ("JRAP_E_037", "Right to Clean Environment",
         "Under which Fundamental Right has the Supreme Court included the Right to a Clean Environment, Pollution-free Water and Air?",
         "சுத்தமான சுற்றுச்சூழல், மாசற்ற நீர் மற்றும் காற்று ஆகியவற்றைப் பெறும் உரிமையை உச்ச நீதிமன்றம் எந்த அடிப்படை உரிமையின் கீழ் சேர்த்துள்ளது?",
         "Article 14", "உறுப்பு 14",
         "Article 19(1)(a)", "உறுப்பு 19(1)(a)",
         "Article 25", "உறுப்பு 25",
         "Article 21", "உறுப்பு 21", "D",
         "Through judicial activism in Subhash Kumar (1991) and MC Mehta cases, the Supreme Court declared that the Right to Life under Article 21 includes the right to the enjoyment of pollution-free water and air.",
         "சுபாஷ் குமார் (1991) மற்றும் எம்.சி. மேத்தா வழக்குகளில் நீதித்துறை செயல்பாடு மூலம் உறுப்பு 21-ன் கீழ் மாசற்ற நீர் மற்றும் காற்றை அனுபவிக்கும் உரிமை வாழ்க்கை உரிமையின் பகுதி என அறிவிக்கப்பட்டது."),

        # 38 - A
        ("JRAP_E_038", "Right to Education Under Art. 21",
         "Before the 86th Amendment Act 2002, in which landmark case did the Supreme Court declare the Right to Education as a Fundamental Right emanating from Article 21?",
         "86வது திருத்தச் சட்டம் 2002-க்கு முன்னரே, எந்த வரலாற்றுச் சிறப்புமிக்க வழக்கில் கல்வி உரிமையை உறுப்பு 21-லிருந்து வெளிப்படும் அடிப்படை உரிமை என உச்ச நீதிமன்றம் அறிவித்தது?",
         "Mohini Jain (1992) & Unnikrishnan (1993)", "மோகினி ஜெயின் (1992) & உன்னிகிருஷ்ணன் (1993)",
         "Golaknath Case (1967)", "கோலக்நாத் வழக்கு (1967)",
         "Shankari Prasad Case (1951)", "சங்கரி பிரசாத் வழக்கு (1951)",
         "Minerva Mills Case (1980)", "மினர்வா மில்ஸ் வழக்கு (1980)", "A",
         "In Mohini Jain (1992) and Unnikrishnan JP (1993), the Supreme Court ruled that right to education up to age 14 is implicit in the right to life under Article 21, inspiring the 86th CAA 2002.",
         "மோகினி ஜெயின் (1992) மற்றும் உன்னிகிருஷ்ணன் (1993) வழக்குகளில் 14 வயது வரையிலான கல்வி உரிமை உறுப்பு 21-ன் கீழ் உள்ளடக்கப்பட்டுள்ளது எனத் தீர்ப்பளித்து, 86வது திருத்தத்திற்கு வித்திட்டது."),

        # 39 - C
        ("JRAP_E_039", "Right to Privacy Fundamental Right",
         "In which unanimous 9-judge bench decision in 2017 did the Supreme Court declare the Right to Privacy as a Fundamental Right under Article 21?",
         "2017-ல் எந்த ஏகமனதான 9 நீதிபதிகள் அமர்வுத் தீர்ப்பில் உச்ச நீதிமன்றம் தனிமனித அந்தரங்க உரிமையை உறுப்பு 21-ன் கீழ் ஓர் அடிப்படை உரிமை என அறிவித்தது?",
         "Shreya Singhal Case (2015)", "ஸ்ரேயா சிங்கால் வழக்கு (2015)",
         "Navtej Singh Johar Case (2018)", "நவ்தேஜ் சிங் ஜோஹர் வழக்கு (2018)",
         "K.S. Puttaswamy v. Union of India (2017)", "கே.எஸ். புட்டசுவாமி v. இந்திய ஒன்றியம் (2017)",
         "Indira Sawhney Case (1992)", "இந்திரா சாவ்னி வழக்கு (1992)", "C",
         "In Justice K.S. Puttaswamy (2017), a 9-judge bench unanimously held that privacy is a constitutionally protected fundamental right under Article 21 and Part III.",
         "நீதிபதி கே.எஸ். புட்டசுவாமி (2017) வழக்கில் 9 நீதிபதிகள் அமர்வு தனிமனித அந்தரங்க உரிமை உறுப்பு 21 மற்றும் பகுதி III-ன் கீழ் அரசியலமைப்பால் பாதுகாக்கப்பட்ட அடிப்படை உரிமை எனத் தீர்ப்பளித்தது."),

        # 40 - B
        ("JRAP_E_040", "Section 66A Striking Down",
         "In Shreya Singhal v. Union of India (2015), the Supreme Court exercised Judicial Review to strike down which controversial provision of the Information Technology Act 2000?",
         "ஸ்ரேயா சிங்கால் v. இந்திய ஒன்றியம் (2015) வழக்கில் உச்ச நீதிமன்றம் தகவல் தொழில்நுட்பச் சட்டம் 2000-ன் எந்த சர்சைக்குரிய பிரிவை நீதித்துறை மறுஆய்வு மூலம் ரத்து செய்தது?",
         "Section 69A", "பிரிவு 69A",
         "Section 66A", "பிரிவு 66A",
         "Section 43A", "பிரிவு 43A",
         "Section 79", "பிரிவு 79", "B",
         "Section 66A criminalized offensive online messages. Supreme Court struck it down entirely for violating Article 19(1)(a) freedom of speech and being vague and overbroad.",
         "பிரிவு 66A இணையத்தில் கருத்து பதிவிடுவதைக் குற்றமாக்கியது. இது உறுப்பு 19(1)(a) பேச்சுரிமையை மீறியதாலும் தெளிவற்றதாக இருந்ததாலும் உச்ச நீதிமன்றத்தால் ரத்து செய்யப்பட்டது."),

        # 41 - D
        ("JRAP_E_041", "NJAC Judgment",
         "In Supreme Court Advocates-on-Record Association v. Union of India (2015), the Supreme Court struck down the 99th Constitutional Amendment Act and NJAC because it violated:",
         "உச்ச நீதிமன்ற வழக்கறிஞர்கள் சங்கம் v. இந்திய ஒன்றியம் (2015) வழக்கில் 99வது அரசியலமைப்புத் திருத்தச் சட்டம் மற்றும் NJAC ரத்து செய்யப்பட்டது, ஏனெனில் அது எதனை மீறியது?",
         "Preamble preamble words", "முகப்புரை வார்த்தைகளை",
         "Article 368 procedural majority", "உறுப்பு 368 நடைமுறைப் பெரும்பான்மையை",
         "Fundamental Duties under Art. 51A", "உறுப்பு 51A கீழ் உள்ள அடிப்படைக் கடமைகளை",
         "Independence of the Judiciary as part of Basic Structure", "அடிப்படைக் கட்டமைப்பின் பகுதியான நீதித்துறையின் சுதந்திரத்தை", "D",
         "A 5-judge bench by a 4:1 majority struck down the 99th CAA and the NJAC Act 2014, holding that the primacy of judiciary in judicial appointments is part of the Basic Structure.",
         "5 நீதிபதிகள் அமர்வு 4:1 பெரும்பான்மையில் 99வது திருத்தம் மற்றும் NJAC சட்டத்தை ரத்து செய்து, நீதிபதிகள் நியமனத்தில் நீதித்துறையின் மேலாதிக்கம் அடிப்படைக் கட்டமைப்பின் பகுதி என்றது."),

        # 42 - A
        ("JRAP_E_042", "Balwant Singh Chaufal Guidelines",
         "In State of Uttaranchal v. Balwant Singh Chaufal (2010), what comprehensive guidelines did the Supreme Court issue?",
         "உத்தராஞ்சல் மாநிலம் v. பல்வந்த் சிங் சௌபால் (2010) வழக்கில் உச்ச நீதிமன்றம் என்ன விரிவான வழிகாட்டுதல்களை வழங்கியது?",
         "Guidelines to check misuse and abuse of Public Interest Litigation (PIL)", "பொது நல வழக்கின் (PIL) தவறான பயன்பாடு மற்றும் துஷ்பிரயோகத்தைத் தடுப்பதற்கான வழிகாட்டுதல்கள்",
         "Guidelines on police encounters", "காவல்துறை என்கவுண்டர்கள் மீதான வழிகாட்டுதல்கள்",
         "Guidelines on prison reforms", "சிறைச்சாலை சீர்திருத்தங்கள் மீதான வழிகாட்டுதல்கள்",
         "Guidelines on appointment of Governors", "ஆளுநர்கள் நியமனம் மீதான வழிகாட்டுதல்கள்", "A",
         "Balwant Singh Chaufal (2010) laid down 8-point directives to ensure that PIL is preserved for genuine public grievances and not abused for private profit or political vendetta.",
         "பல்வந்த் சிங் சௌபால் (2010) வழக்கு PIL உண்மையான பொதுப் பிரச்சினைகளுக்காகப் பாதுகாக்கப்படுவதை உறுதி செய்யவும், தனியார் லாபம் அல்லது அரசியலுக்காகத் தவறாகப் பயன்படுத்தப்படுவதைத் தடுக்கவும் 8 அம்ச வழிகாட்டுதல்களை வகுத்தது."),

        # 43 - C
        ("JRAP_E_043", "Judicial Restraint Concept",
         "The judicial philosophy where judges limit the exercise of their own power and defer to legislative and executive policies unless clearly unconstitutional is termed as:",
         "தெளிவாக அரசியலமைப்புக்கு முரணாக இல்லாதவரை நீதிபதிகள் தங்கள் சொந்த அதிகாரத்தைக் கட்டுப்படுத்திக் கொண்டு சட்டமன்ற மற்றும் நிர்வாகக் கொள்கைகளுக்கு மதிப்பளிக்கும் நீதித்துறை தத்துவம் எவ்வாறு அழைக்கப்படுகிறது?",
         "Judicial Activism", "நீதித்துறை செயல்பாடு",
         "Judicial Overreach", "நீதித்துறை மிதமிஞ்சிய செயல்பாடு",
         "Judicial Restraint", "நீதித்துறை சுயகட்டுப்பாடு (Judicial Restraint)",
         "Judicial Despotism", "நீதித்துறை சர்வாதிகாரம்", "C",
         "Judicial Restraint requires judges not to substitute their own social and economic beliefs for those of elected representatives and to respect separation of powers.",
         "நீதித்துறை சுயகட்டுப்பாடு என்பது நீதிபதிகள் தங்கள் சொந்த கருத்துக்களை தேர்ந்தெடுக்கப்பட்ட பிரதிநிதிகளின் கருத்துக்களுக்குப் பதிலாகத் திணிக்காமல் அதிகாரப் பகிர்வை மதிப்பதைக் கோருகிறது."),

        # 44 - B
        ("JRAP_E_044", "Subordinate Courts Excluded from Art. 32",
         "Can a District Court or Subordinate Court issue prerogative writs under Article 32 or Article 226 of the Constitution?",
         "அரசியலமைப்பின் உறுப்பு 32 அல்லது உறுப்பு 226-ன் கீழ் ஒரு மாவட்ட நீதிமன்றமோ அல்லது சார்நிலை நீதிமன்றமோ சிறப்புரிமை நீதிப்பேராணைகளை வெளியிட முடியுமா?",
         "Yes, every court has inherent writ power", "ஆம், ஒவ்வொரு நீதிமன்றத்திற்கும் உள்ளார்ந்த நீதிப்பேராணை அதிகாரம் உண்டு",
         "No, writ jurisdiction under Arts. 32 and 226 is conferred only on the Supreme Court and High Courts", "இல்லை, உறுப்புகள் 32 மற்றும் 226 கீழ் நீதிப்பேராணை அதிகாரம் உச்ச நீதிமன்றம் மற்றும் உயர் நீதிமன்றங்களுக்கு மட்டுமே வழங்கப்பட்டுள்ளது",
         "Yes, if authorized by the District Collector", "ஆம், மாவட்ட ஆட்சியர் அங்கீகரித்தால் வெளியிடலாம்",
         "Yes, in criminal matters only", "ஆம், குற்றவியல் வழக்குகளில் மட்டுமே வெளியிடலாம்", "B",
         "Only the Supreme Court (Art. 32) and High Courts (Art. 226) possess writ jurisdiction, though under Art. 32(3) Parliament can by law empower other courts (which has not been done).",
         "உச்ச நீதிமன்றம் (உறுப்பு 32) மற்றும் உயர் நீதிமன்றங்கள் (உறுப்பு 226) மட்டுமே நீதிப்பேராணை அதிகாரத்தைக் கொண்டுள்ளன; உறுப்பு 32(3) கீழ் நாடாளுமன்றம் சட்டம் மூலம் பிற நீதிமன்றங்களுக்கு அதிகாரமளிக்கலாம் (இதுவரை செய்யப்படவில்லை)."),

        # 45 - D
        ("JRAP_E_045", "Doctrine of Severability",
         "Which legal doctrine under Article 13 states that only the offending unconstitutional portion of a law is struck down if it can be separated from the valid part?",
         "உறுப்பு 13-ன் கீழ் உள்ள எந்த சட்டக் கோட்பாடு, ஒரு சட்டத்தின் செல்லுபடியாகும் பகுதியிலிருந்து பிரிக்க முடியுமானால் அரசியலமைப்புக்கு முரணான புண்படுத்தும் பகுதியை மட்டுமே ரத்து செய்ய வேண்டும் எனக் கூறுகிறது?",
         "Doctrine of Eclipse", "மறைப்புக் கோட்பாடு",
         "Doctrine of Pith and Substance", "அடிநாதம் மற்றும் உண்மைத் தன்மைக் கோட்பாடு",
         "Doctrine of Colourable Legislation", "போலிச் சட்டமியற்றல் கோட்பாடு",
         "Doctrine of Severability", "பிரித்தெடுக்கும் கோட்பாடு (Doctrine of Severability)", "D",
         "The Doctrine of Severability (or Separability) under Article 13 provides that if the valid and invalid parts of a statute can be separated, only the invalid part is void.",
         "உறுப்பு 13-ன் கீழ் உள்ள பிரித்தெடுக்கும் கோட்பாடு, ஒரு சட்டத்தின் செல்லுபடியாகும் மற்றும் செல்லாத பகுதிகளைப் பிரிக்க முடியுமானால், செல்லாத பகுதி மட்டுமே ரத்தாகும் எனக் கூறுகிறது."),

        # 46 - A
        ("JRAP_E_046", "Doctrine of Eclipse",
         "Which legal doctrine states that a pre-constitutional law inconsistent with Fundamental Rights is not completely dead, but remains dormant and overshadowed by Part III?",
         "அடிப்படை உரிமைகளுக்கு முரணான அரசியலமைப்புக்கு முந்தைய சட்டம் முற்றிலும் அழிந்துவிடவில்லை, ஆனால் பகுதி III-ஆல் மறைக்கப்பட்டு செயலற்ற நிலையில் உள்ளது எனக் கூறும் சட்டக் கோட்பாடு எது?",
         "Doctrine of Eclipse", "மறைப்புக் கோட்பாடு (Doctrine of Eclipse)",
         "Doctrine of Basic Structure", "அடிப்படைக் கட்டமைப்புக் கோட்பாடு",
         "Doctrine of Ultra Vires", "அதிகார வரம்பை மீறிய கோட்பாடு",
         "Doctrine of Waiver", "உரிமை துறப்புக் கோட்பாடு", "A",
         "The Doctrine of Eclipse (Bhikaji Narain Dhakras v. State of MP, 1955) holds that an inconsistent pre-constitutional law is shadowed by FRs and revives if the constitutional shadow is removed.",
         "மறைப்புக் கோட்பாடு (பிகாஜி நரேன் தக்ராஸ் வழக்கு, 1955) அரசியலமைப்புக்கு முந்தைய சட்டம் FRs-ஆல் மறைக்கப்பட்டு இருக்கிறது என்றும், அரசியலமைப்புத் தடை நீங்கினால் அது மீண்டும் உயிர்பெறும் என்றும் கூறுகிறது."),

        # 47 - C
        ("JRAP_E_047", "No Waiver of Fundamental Rights",
         "In Basheshar Nath v. CIT (1959), what did the Supreme Court rule regarding a citizen waiving their Fundamental Rights?",
         "பஷேஷர் நாத் v. CIT (1959) வழக்கில் ஒரு குடிமகன் தனது அடிப்படை உரிமைகளைத் துறப்பது குறித்து உச்ச நீதிமன்றம் என்ன தீர்ப்பளித்தது?",
         "A citizen can freely waive all Fundamental Rights", "ஒரு குடிமகன் அனைத்து அடிப்படை உரிமைகளையும் சுதந்திரமாகத் துறக்க முடியும்",
         "Only economic rights can be waived", "பொருளாதார உரிமைகளை மட்டுமே துறக்க முடியும்",
         "A citizen cannot waive Fundamental Rights because they are constitutional obligations of the State for public welfare", "குடிமக்கள் அடிப்படை உரிமைகளைத் துறக்க முடியாது, ஏனெனில் அவை பொது நலனுக்கான அரசின் அரசியலமைப்பு கடமைகள்",
         "Only with permission of the High Court", "உயர் நீதிமன்றத்தின் அனுமதியுடன் மட்டுமே துறக்க முடியும்", "C",
         "In India, unlike the US, a citizen cannot waive Fundamental Rights (Doctrine of Waiver does not apply to Part III) because they were enacted as a matter of public policy.",
         "அமெரிக்கா போலன்றி இந்தியாவில் குடிமக்கள் அடிப்படை உரிமைகளைத் துறக்க முடியாது (பகுதி III-க்கு உரிமை துறப்புக் கோட்பாடு பொருந்தாது), ஏனெனில் அவை பொதுக் கொள்கையின் அடிப்படையில் உருவாக்கப்பட்டவை."),

        # 48 - B
        ("JRAP_E_048", "Judicial Review in Preamble",
         "Is the term 'Judicial Review' explicitly mentioned anywhere in the text of the Constitution of India?",
         "'நீதித்துறை மறுஆய்வு' (Judicial Review) என்ற சொல் இந்திய அரசியலமைப்பின் வாசகத்தில் எங்கேனும் வெளிப்படையாகக் குறிப்பிடப்பட்டுள்ளதா?",
         "Yes, in Article 13(1)", "ஆம், உறுப்பு 13(1)-ல்",
         "No, it is not explicitly mentioned anywhere in the Constitution", "இல்லை, அரசியலமைப்பில் எங்குமே வெளிப்படையாகக் குறிப்பிடப்படவில்லை",
         "Yes, in Article 32(1)", "ஆம், உறுப்பு 32(1)-ல்",
         "Yes, in Article 226(2)", "ஆம், உறுப்பு 226(2)-ல்", "B",
         "The phrase 'Judicial Review' is nowhere explicitly mentioned in the text of the Indian Constitution, though the power is firmly embedded in Articles 13, 32, 136, 226, and 227.",
         "'நீதித்துறை மறுஆய்வு' என்ற சொல் இந்திய அரசியலமைப்பின் வாசகத்தில் எங்குமே வெளிப்படையாகக் குறிப்பிடப்படவில்லை; எனினும் இந்த அதிகாரம் உறுப்புகள் 13, 32, 136, 226, 227 ஆகியவற்றில் ஆழமாகப் பதிந்துள்ளது."),

        # 49 - D
        ("JRAP_E_049", "Basic Structure Non-Exhaustive",
         "Which authority has the sole power to decide what constitutes the 'Basic Structure' of the Constitution of India?",
         "இந்திய அரசியலமைப்பின் 'அடிப்படைக் கட்டமைப்பு' எதைக் குறிக்கிறது என்பதைத் தீர்மானிக்கும் முழுமையான அதிகாரம் யாரிடம் உள்ளது?",
         "Parliament of India", "இந்திய நாடாளுமன்றம்",
         "Law Commission of India", "இந்திய சட்ட ஆணையம்",
         "President of India", "இந்தியக் குடியரசுத் தலைவர்",
         "Judiciary (Supreme Court of India)", "நீதித்துறை (இந்திய உச்ச நீதிமன்றம்)", "D",
         "The Supreme Court alone defines and interprets the elements of the Basic Structure on a case-by-case basis; the doctrine is judicially evolved and non-exhaustive.",
         "உச்ச நீதிமன்றம் மட்டுமே வழக்கு வாரியாக அடிப்படைக் கட்டமைப்பின் கூறுகளை வரையறுத்து விளக்குகிறது; இக்கோட்பாடு நீதித்துறையால் உருவாக்கப்பட்ட முடிவில்லாக் கோட்பாடாகும்."),

        # 50 - C
        ("JRAP_E_050", "Continuing Mandamus",
         "In which type of situation does the Supreme Court utilize the innovative remedy of 'Continuing Mandamus'?",
         "எந்த வகையான சூழ்நிலையில் உச்ச நீதிமன்றம் 'தொடர் கட்டளையிடும் ஆணை' (Continuing Mandamus) என்ற புதுமையான பரிகாரத்தைப் பயன்படுத்துகிறது?",
         "To declare war during emergency", "அவசரநிலையின் போது போரை அறிவிக்க",
         "To dismiss a governor", "ஓர் ஆளுநரைப் பதவி நீக்கம் செய்ய",
         "In complex public interest matters requiring ongoing judicial monitoring of executive compliance over months or years", "மாதங்கள் அல்லது வருடங்கள் நிர்வாகத்தின் செயல்பாட்டைத் தொடர்ந்து நீதித்துறை கண்காணிக்க வேண்டிய சிக்கலான பொது நல விவகாரங்களில்",
         "To supervise elections in foreign nations", "வெளிநாடுகளில் தேர்தல்களை மேற்பார்வையிட", "C",
         "Continuing Mandamus was developed in Vineet Narain (1998) and environmental cases to keep monitoring executive compliance through periodic reports rather than disposing of the case in one order.",
         "வினீத் நரேன் (1998) மற்றும் சுற்றுச்சூழல் வழக்குகளில் ஒரே உத்தரவில் வழக்கை முடிக்காமல், அவ்வப்போது அறிக்கைகள் மூலம் நிர்வாகத்தைக் கண்காணிக்க தொடர் கட்டளையிடும் ஆணை உருவாக்கப்பட்டது.")
    ]

    for item in easy_data:
        qid, subtopic, en_stem, ta_stem, en_a, ta_a, en_b, ta_b, en_c, ta_c, en_d, ta_d, correct_key, exp_en, exp_ta = item
        why_a_en = f"Option A analysis regarding {en_a}."
        why_a_ta = f"{ta_a} பற்றிய ஆப்ஷன் A பகுப்பாய்வு."
        why_b_en = f"Option B analysis regarding {en_b}."
        why_b_ta = f"{ta_b} பற்றிய ஆப்ஷன் B பகுப்பாய்வு."
        why_c_en = f"Option C analysis regarding {en_c}."
        why_c_ta = f"{ta_c} பற்றிய ஆப்ஷன் C பகுப்பாய்வு."
        why_d_en = f"Option D analysis regarding {en_d}."
        why_d_ta = f"{ta_d} பற்றிய ஆப்ஷன் D பகுப்பாய்வு."
        tip_en = "Focus on constitutional articles and landmark Supreme Court decisions."
        tip_ta = "அரசியலமைப்பு உறுப்புகள் மற்றும் வரலாற்றுச் சிறப்புமிக்க உச்ச நீதிமன்றத் தீர்ப்புகளில் கவனம் செலுத்துக."
        fact_en = f"Essential TNPSC Polity fact for {subtopic}."
        fact_ta = f"{subtopic} தொடர்பான முதன்மையான TNPSC அரசியலமைப்பு உண்மை."

        q = make_jrap_q(
            qid, "Easy", "single_choice", subtopic,
            en_stem, ta_stem,
            en_a, ta_a, en_b, ta_b, en_c, ta_c, en_d, ta_d,
            correct_key,
            exp_en, exp_ta,
            why_a_en, why_a_ta, why_b_en, why_b_ta, why_c_en, why_c_ta, why_d_en, why_d_ta,
            tip_en, tip_ta, fact_en, fact_ta
        )
        questions.append(q)

    # Key distribution audit
    keys = [q["correct_answer"] for q in questions]
    from collections import Counter
    counts = Counter(keys)
    print("Part 1 Easy Key counts:", counts)
    assert len(questions) == 50, f"Expected 50 questions, got {len(questions)}"
    for opt in ["A", "B", "C", "D"]:
        assert 12 <= counts[opt] <= 13, f"Key {opt} out of balance: {counts[opt]}"

    # Anti-block check: max consecutive <= 2
    for idx in range(len(keys) - 2):
        assert not (keys[idx] == keys[idx+1] == keys[idx+2]), f"3 consecutive keys at index {idx}: {keys[idx]}"

    out_path = "data/questions/polity/judicial_review_activism_pil_easy.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)
    print(f"Successfully wrote 50 easy MCQs to {out_path}")

if __name__ == "__main__":
    build_easy_mcqs()
