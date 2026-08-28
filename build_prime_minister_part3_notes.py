import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

def generate_part3():
    part3_data = {
        "meta": {
            "topic_id": "polity_prime_minister_part_3",
            "repository_id": "polity_prime_minister",
            "display_title": "Prime Minister of India – Part 3",
            "part": 3,
            "total_parts": 3,
            "subject": "polity",
            "chapter": "Prime Minister of India",
            "language": "English + Tamil"
        },
        "metadata": {
            "topic_id": "polity_prime_minister_part_3",
            "repository_id": "polity_prime_minister",
            "display_title": "Prime Minister of India – Part 3",
            "part": 3,
            "total_parts": 3,
            "subject": "polity",
            "chapter": "Prime Minister of India",
            "language": "English + Tamil"
        },
        "keywords": [
            "Collective Responsibility",
            "கூட்டுப் பொறுப்பு",
            "Individual Responsibility",
            "தனிப்பட்ட பொறுப்பு",
            "Hung Lok Sabha",
            "தொங்கு மக்களவை",
            "Floor Test Principle",
            "நம்பிக்கை வாக்கெடுப்புக் கோட்பாடு",
            "Caretaker Government",
            "பராமரிப்பு அரசாங்கம்",
            "Cabinet Committees",
            "அமைச்சரவைக் குழுக்கள்",
            "Super Cabinet",
            "சூப்பர் கேபினட்",
            "Constitutional Conventions",
            "அரசியலமைப்பு மரபுகள்",
            "No-Confidence Motion",
            "நம்பிக்கையில்லாத் தீர்மானம்",
            "Articles 74-78 Map",
            "உறுப்புகள் 74-78 வரைபடம்"
        ],
        "learning_outcomes": {
            "Understand": {
                "en": [
                    "Master the doctrine of Collective Responsibility under Article 75(3) and No-Confidence Motion dynamics in Lok Sabha.",
                    "Understand Individual Responsibility of Ministers under Article 75(2) and President's pleasure exercised on PM's advice.",
                    "Analyze constitutional conventions and Presidential discretion during a Hung Lok Sabha and Floor Test mandates.",
                    "Understand the legal and operational status of a Caretaker Government (continuation of admin without major policy changes).",
                    "Analyze the advanced relationship between President and Prime Minister across Articles 74, 75, and 78 (post 42nd & 44th CAAs).",
                    "Understand the role of Cabinet Committees (e.g. Cabinet Committee on Political Affairs as 'Super Cabinet') headed by PM."
                ],
                "ta": [
                    "உறுப்பு 75(3)-ன் கீழ் கூட்டுப் பொறுப்புக் கோட்பாட்டையும் மக்களவையில் நம்பிக்கையில்லாத் தீர்மானத்தின் இயக்கவியலையும் தெரிந்துகொள்ளுதல்.",
                    "உறுப்பு 75(2)-ன் கீழ் அமைச்சர்களின் தனிப்பட்ட பொறுப்பையும் பிரதமரின் அறிவுரைப்படி குடியரசுத் தலைவரின் விருப்பம் பயன்படுத்தப்படுவதையும் புரிந்துகொள்ளுதல்.",
                    "தொங்கு மக்களவை மற்றும் நம்பிக்கை வாக்கெடுப்பு உத்தரவுகளின் போது அரசியலமைப்பு மரபுகள் மற்றும் குடியரசுத் தலைவரின் விவேகத்தைப் பகுப்பாய்வு செய்தல்.",
                    "பராமரிப்பு அரசாங்கத்தின் (Caretaker Government) சட்டப்பூர்வ மற்றும் செயல்பாட்டு நிலையைப் புரிந்துகொள்ளுதல்.",
                    "உறுப்புகள் 74, 75 மற்றும் 78 (42 & 44வது திருத்தங்களுக்குப் பிந்தைய) மூலம் குடியரசுத் தலைவர் மற்றும் பிரதமர் இடையிலான மேம்பட்ட தொடர்பைப் பகுப்பாய்வு செய்தல்.",
                    "பிரதமர் தலைமையிலான கேபினட் குழுக்களின் ('சூப்பர் கேபினட்' எனக் அழைக்கப்படும் அரசியல் விவகாரங்களுக்கான கேபினட் குழு) பங்கைப் புரிந்துகொள்ளுதல்."
                ]
            },
            "Remember": {
                "en": [
                    "Remember No-Confidence Motion can be moved ONLY in Lok Sabha (requires 50 members support).",
                    "Remember Caretaker Government is a convention-based concept; Article 74 mandates Council of Ministers must ALWAYS exist.",
                    "Remember Cabinet Committee on Political Affairs chaired by PM is known as the 'Super Cabinet'.",
                    "Remember 44th CAA 1978 allows President to return aid and advice ONCE for reconsideration.",
                    "Remember failure of a Money Bill in Lok Sabha leads to immediate resignation of the Prime Minister and Council."
                ],
                "ta": [
                    "நம்பிக்கையில்லாத் தீர்மானம் மக்களவையில் (LOK SABHA) மட்டுமே கொண்டு வர முடியும் (50 உறுப்பினர்கள் ஆதரவு தேவை) என்பதை நினைவில் கொள்ளுதல்.",
                    "பராமரிப்பு அரசாங்கம் (Caretaker Govt) என்பது மரபு சார்ந்த கருத்து; உறுப்பு 74 எப்போதும் ஓர் அமைச்சரவை இருக்க வேண்டும் என ஆணையிடுகிறது என்பதை நினைவில் கொள்ளுதல்.",
                    "பிரதமர் தலைமையிலான அரசியல் விவகாரங்களுக்கான கேபினட் குழு 'சூப்பர் கேபினட்' என அழைக்கப்படுகிறது என்பதை நினைவில் கொள்ளுதல்.",
                    "1978-ன் 44வது திருத்தம் குடியரசுத் தலைவர் அமைச்சரவை ஆலோசனையை ஒருமுறை மறுபரிசீலனைக்கு அனுப்ப அனுமதிக்கிறது என்பதை நினைவில் கொள்ளுதல்.",
                    "மக்களவையில் பண மசோதா தோல்வியடைவது பிரதமர் மற்றும் அமைச்சரவையின் உடனடி ராஜினாமாவிற்கு வழிவகுக்கும் என்பதை நினைவில் கொள்ளுதல்."
                ]
            }
        },
        "subject": "polity",
        "topic": "Prime Minister of India",
        "language": "English + Tamil",
        "ui_type": "standard_notes",
        "sections": [
            {
                "id": "sec_collective_responsibility",
                "title_en": "1. Doctrine of Collective Responsibility (Article 75(3)) & No-Confidence Motion",
                "title_ta": "1. கூட்டுப் பொறுப்புக் கோட்பாடு (உறுப்பு 75(3)) & நம்பிக்கையில்லாத் தீர்மானம்",
                "type": "standard_topic"
            },
            {
                "id": "sec_individual_responsibility",
                "title_en": "2. Individual Responsibility of Ministers (Article 75(2))",
                "title_ta": "2. அமைச்சர்களின் தனிப்பட்ட பொறுப்பு (உறுப்பு 75(2))",
                "type": "standard_topic"
            },
            {
                "id": "sec_hung_loksabha_floortest",
                "title_en": "3. Hung Lok Sabha, Presidential Discretion & Floor Test Mandate",
                "title_ta": "3. தொங்கு மக்களவை, குடியரசுத் தலைவரின் விவேகம் & நம்பிக்கை வாக்கெடுப்பு",
                "type": "standard_topic"
            },
            {
                "id": "sec_caretaker_government",
                "title_en": "4. Caretaker Government — Constitutional & Convention Boundaries",
                "title_ta": "4. பராமரிப்பு அரசாங்கம் (Caretaker Govt) — அரசியலமைப்பு & மரபு எல்லைகள்",
                "type": "standard_topic"
            },
            {
                "id": "sec_advanced_pm_president",
                "title_en": "5. Advanced PM-President Relationship (42nd & 44th Amendments)",
                "title_ta": "5. மேம்பட்ட பிரதமர்-குடியரசுத் தலைவர் தொடர்பு (42 & 44வது திருத்தங்கள்)",
                "type": "standard_topic"
            },
            {
                "id": "sec_cabinet_committees",
                "title_en": "6. Cabinet Committees & The 'Super Cabinet' Dynamics",
                "title_ta": "6. கேபினட் குழுக்கள் & 'சூப்பர் கேபினட்' இயக்கம்",
                "type": "standard_topic"
            },
            {
                "id": "comparison_tables",
                "title_en": "7. Mandatory Comparison Tables (Advanced Group 1 Master Tables)",
                "title_ta": "7. கட்டாய ஒப்பீட்டு அட்டவணைகள் (மேம்பட்ட குரூப் 1 மாஸ்டர் அட்டவணைகள்)",
                "type": "comparison"
            },
            {
                "id": "mind_map",
                "title_en": "8. Mind Map & High-Yield TNPSC Traps",
                "title_ta": "8. மன வரைபடம் & அதிகக் கேள்விகள் கேட்கப்படும் TNPSC பொறிகள்",
                "type": "mind_map"
            }
        ],
        "content": {
            "definition": {
                "en": "Part 3 examines the operational mechanics of parliamentary democracy under the Prime Minister's leadership. It covers collective responsibility (Article 75(3)), individual minister liability (Article 75(2)), Presidential situational discretion in a Hung Lok Sabha, the constitutional status of Caretaker Governments, and the institutional power of PM-led Cabinet Committees like the Cabinet Committee on Political Affairs ('Super Cabinet').",
                "ta": "பகுதி 3 பிரதமரின் தலைமையின் கீழ் நாடாளுமன்ற ஜனநாயகத்தின் செயல்பாட்டு இயக்கவியலை ஆராய்கிறது. இது கூட்டுப் பொறுப்பு (உறுப்பு 75(3)), தனிப்பட்ட அமைச்சர் பொறுப்பு (உறுப்பு 75(2)), தொங்கு மக்களவையில் குடியரசுத் தலைவரின் சூழ்நிலை விவேகம், பராமரிப்பு அரசாங்கத்தின் (Caretaker Govt) அரசியலமைப்பு நிலை மற்றும் 'சூப்பர் கேபினட்' எனப்படும் அரசியல் விவகாரங்களுக்கான கேபினட் குழு போன்ற பிரதமர் தலைமையிலான கேபினட் குழுக்களின் அதிகாரங்களை உள்ளடக்கியது."
            },
            "introduction": {
                "en": "The Indian parliamentary system relies on a delicate balance between codified constitutional provisions and unwritten conventions. Understanding how the Prime Minister navigates Lok Sabha confidence, manages coalition dynamics, interacts with the President under Articles 74, 75, and 78, and maintains cabinet solidarity is crucial for TNPSC Group 1 examinations.",
                "ta": "இந்திய நாடாளுமன்ற முறைமை எழுதப்பட்ட அரசியலமைப்பு விதிகளுக்கும் எழுதப்படாத அரசியலமைப்பு மரபுகளுக்கும் இடையிலான நுட்பமான சமநிலையை நம்பியுள்ளது. பிரதமர் எவ்வாறு மக்களவை நம்பிக்கையைக் கையாளுகிறார், கூட்டணிகளை நிர்வகிக்கிறார், உறுப்புகள் 74, 75 மற்றும் 78-ன் கீழ் குடியரசுத் தலைவருடன் தொடர்பு கொள்கிறார், மற்றும் அமைச்சரவை ஒற்றுமையைப் பராமரிக்கிறார் என்பதைப் புரிந்துகொள்வது TNPSC குரூப் 1 தேர்வுகளுக்கு மிக முக்கியமானது."
            },
            "sec_collective_responsibility": [
                {
                    "title": "1. Doctrine of Collective Responsibility under Article 75(3)",
                    "points": {
                        "en": [
                            "Core Constitutional Mandate: Article 75(3) states that 'The Council of Ministers shall be collectively responsible to the House of the People (Lok Sabha)'.",
                            "Swim Together & Sink Together: All ministers share joint responsibility for cabinet decisions. A minister who disagrees with a cabinet decision MUST accept it or resign (e.g. Dr. B.R. Ambedkar resigned in 1951 over Hindu Code Bill; C.D. Deshmukh resigned in 1956 over reorganization of Bombay state).",
                            "No-Confidence Motion (Rule 198): Can be moved ONLY in Lok Sabha. Requires support of minimum 50 members for admission. If passed by simple majority, the ENTIRE Council of Ministers (including PM) MUST resign immediately.",
                            "Censure Motion vs No-Confidence Motion: Censure motion targets a specific minister or policy (requires reasons), whereas No-Confidence Motion targets entire Council of Ministers (no reasons required)."
                        ],
                        "ta": [
                            "முக்கிய அரசியலமைப்பு கட்டளை: உறுப்பு 75(3) 'அமைச்சரவை மக்களவைக்குக் (Lok Sabha) கூட்டாகப் பொறுப்புடையது' எனக் குறிப்பிடுகிறது.",
                            "ஒன்றாக நீந்துவார்கள் & ஒன்றாக மூழ்குவார்கள்: கேபினட் முடிவுகளுக்கு அனைத்து அமைச்சர்களும் கூட்டாகப் பொறுப்பேற்க வேண்டும். கேபினட் முடிவை ஏற்காத அமைச்சர் அதை ஏற்க வேண்டும் அல்லது ராஜினாமா செய்ய வேண்டும் (எ.கா. 1951-ல் இந்து சட்ட மசோதா தொடர்பாக டாக்டர் பி.ஆர். அம்பேத்கர் ராஜினாமா செய்தார்; 1956-ல் பாம்பே மாநில மறுசீரமைப்பு தொடர்பாக சி.டி. தேஷ்முக் ராஜினாமா செய்தார்).",
                            "நம்பிக்கையில்லாத் தீர்மானம் (விதி 198): மக்களவையில் (Lok Sabha) மட்டுமே கொண்டு வர முடியும். அனுமதி பெற குறைந்தபட்சம் 50 உறுப்பினர்கள் ஆதரவு தேவை. சாதாரண பெரும்பான்மையால் நிறைவேற்றப்பட்டால், பிரதமர் உட்பட முழு அமைச்சரவையும் உடனடியாக ராஜினாமா செய்ய வேண்டும்.",
                            "கண்டனத் தீர்மானம் vs நம்பிக்கையில்லாத் தீர்மானம்: கண்டனத் தீர்மானம் ஒரு குறிப்பிட்ட அமைச்சர் அல்லது கொள்கையைக் குறிவைக்கிறது (காரணங்கள் தேவை), ஆனால் நம்பிக்கையில்லாத் தீர்மானம் முழு அமைச்சரவையையும் குறிவைக்கிறது (காரணங்கள் தேவையில்லை)."
                        ]
                    }
                }
            ],
            "sec_individual_responsibility": [
                {
                    "title": "1. Principle of Individual Responsibility under Article 75(2)",
                    "points": {
                        "en": [
                            "Constitutional Mandate: Article 75(2) states that 'Ministers shall hold office during the pleasure of the President'.",
                            "Role of Prime Minister: The President exercises this pleasure ONLY on the advice of the Prime Minister. If a minister loses PM's confidence, PM can demand his resignation or advise President to dismiss him.",
                            "Saves Cabinet: Individual responsibility allows PM to remove an uncooperative or corrupt minister without causing dissolution of the entire Cabinet."
                        ],
                        "ta": [
                            "அரசியலமைப்பு கட்டளை: உறுப்பு 75(2) 'அமைச்சர்கள் குடியரசுத் தலைவரின் விருப்பம் உள்ளவரை பதவி வகிப்பார்கள்' எனக் குறிப்பிடுகிறது.",
                            "பிரதமரின் பங்கு: குடியரசுத் தலைவர் இந்த விருப்பத்தைப் பிரதமரின் அறிவுரையின் பேரில் மட்டுமே பயன்படுத்துகிறார். ஒரு அமைச்சர் பிரதமரின் நம்பிக்கையை இழந்தால், பிரதமர் அவரது ராஜினாமையைக் கோரலாம் அல்லது அவரைப் பதவி நீக்கம் செய்யக் குடியரசுத் தலைவருக்கு அறிவுறுத்தலாம்.",
                            "கேபினட்டைக் காப்பாற்றுகிறது: தனிப்பட்ட பொறுப்பு பிரதமர் முழு அமைச்சரவையையும் கலைக்காமல் ஒரு கூட்டுப்பணியில் ஈடுபடாத அல்லது ஊழல் நிறைந்த அமைச்சரை நீக்க அனுமதிக்கிறது."
                        ]
                    }
                }
            ],
            "sec_hung_loksabha_floortest": [
                {
                    "title": "1. Presidential Discretion in Hung Lok Sabha & Floor Test Principle",
                    "points": {
                        "en": [
                            "Hung House Definition: Situation where no political party or pre-poll alliance secures clear majority (272+ seats) in Lok Sabha.",
                            "Presidential Situational Discretion: President exercises personal discretion under Art 75(1) to appoint PM. Convention dictates appointing leader of largest single party or largest post-poll coalition.",
                            "Floor Test Requirement: Appointed PM is mandated to seek a vote of confidence on the floor of Lok Sabha within a specified window (usually 10 to 30 days).",
                            "S.R. Bommai Principle (1994): Supreme Court ruled that majority of executive MUST be tested ONLY on the floor of the House (Floor Test), not in the Raj Bhavan / Rashtrapati Bhavan corridors."
                        ],
                        "ta": [
                            "தொங்கு மக்களவை வரையறை: மக்களவையில் எந்தவொரு அரசியல் கட்சிக்கும் அல்லது தேர்தலுக்கு முந்தைய கூட்டணிக்கும் தெளிவான பெரும்பான்மை (272+ இடங்கள்) கிடைக்காத நிலை.",
                            "குடியரசுத் தலைவரின் சூழ்நிலை விவேகம்: உறுப்பு 75(1)-ன் கீழ் பிரதமரை நியமிக்கக் குடியரசுத் தலைவர் தனது தனிப்பட்ட விவேகத்தைப் பயன்படுத்துகிறார். மிகப்பெரிய ஒற்றைக் கட்சி அல்லது தேர்தலுக்குப் பிந்தைய மிகப்பெரிய கூட்டணியின் தலைவரை நியமிப்பது அரசியல் மரபாகும்.",
                            "நம்பிக்கை வாக்கெடுப்புத் தேவை: நியமிக்கப்பட்ட பிரதமர் குறிப்பிட்ட அவகாசத்திற்குள் (பொதுவாக 10 முதல் 30 நாட்கள்) மக்களவையில் நம்பிக்கை வாக்கெடுப்பு கோர வேண்டும்.",
                            "எஸ்.ஆர். பொம்மை தீர்ப்பு (1994): நிர்வாகத்தின் பெரும்பான்மை அவையின் தளத்தில் (Floor Test) மட்டுமே நிரூபிக்கப்பட வேண்டும், ஆளுநர் மாளிகை அல்லது குடியரசுத் தலைவர் பவன நடைபாதைகளில் அல்ல என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது."
                        ]
                    }
                }
            ],
            "sec_caretaker_government": [
                {
                    "title": "1. Caretaker Government Status & Constitutional Boundaries",
                    "points": {
                        "en": [
                            "Meaning & Context: A government that continues in office after dissolution of Lok Sabha or after resigning following loss of majority, until a new government takes oath.",
                            "No Constitutional Term: The term 'Caretaker Government' does NOT exist in the Indian Constitution. However, Article 74 mandates that there must ALWAYS be a Council of Ministers to advise President.",
                            "Convention-Bound Powers: Caretaker government carries on day-to-day routine administration. By convention, it CANNOT make major policy decisions, institute financial commitments, or make key appointments."
                        ],
                        "ta": [
                            "பொருள் & சூழல்: மக்களவைக் கலைக்கப்பட்ட பிறகோ அல்லது பெரும்பான்மை இழந்து ராஜினாமா செய்த பிறகோ, புதிய அரசாங்கம் பதவியேற்கும் வரை பதவியில் தொடரும் அரசாங்கம்.",
                            "அரசியலமைப்புச் சொல் இல்லை: 'Caretaker Government' (பராமரிப்பு அரசாங்கம்) என்ற சொல் இந்திய அரசியலமைப்பில் இல்லை. இருப்பினும், குடியரசுத் தலைவருக்கு அறிவுறுத்த எப்போதும் ஓர் அமைச்சரவை இருக்க வேண்டும் என்று உறுப்பு 74 ஆணையிடுகிறது.",
                            "மரபுக்கு உட்பட்ட அதிகாரங்கள்: பராமரிப்பு அரசாங்கம் அன்றாட வழக்கமான நிர்வாகத்தை மேற்கொள்கிறது. மரபுப்படி, இது முக்கிய கொள்கை முடிவுகளை எடுக்க முடியாது, நிதிப் பொறுப்புகளை ஏற்க முடியாது அல்லது முக்கிய நியமனங்களைச் செய்ய முடியாது."
                        ]
                    }
                }
            ],
            "sec_advanced_pm_president": [
                {
                    "title": "1. Evolution of Articles 74, 75 & 78 Dynamics",
                    "points": {
                        "en": [
                            "Original Constitution (1950): Article 74(1) stated Council of Ministers aids and advises President, but word 'binding' was absent.",
                            "42nd Amendment Act 1976 (Indira Gandhi): Made aid and advice of PM-led Council explicitly BINDING on the President.",
                            "44th Amendment Act 1978 (Morarji Desai): Added a proviso allowing President to return aid and advice ONCE for reconsideration. However, reconsidered advice is ABSOLUTELY BINDING on President.",
                            "Article 74(2) Protection: The question whether any, and if so what, advice was tendered by Ministers to the President shall NOT be inquired into in any court."
                        ],
                        "ta": [
                            "மூல அரசியலமைப்பு (1950): உறுப்பு 74(1) அமைச்சரவை குடியரசுத் தலைவருக்கு உதவவும் அறிவுரை வழங்கவும் செய்கிறது என்று கூறியது, ஆனால் 'கட்டுப்படுத்தும்' என்ற சொல் இல்லை.",
                            "42வது திருத்தச் சட்டம் 1976: பிரதமர் தலைமையிலான அமைச்சரவையின் உதவி & அறிவுரையைக் குடியரசுத் தலைவரைக் கட்டுப்படுத்தும் ஒன்றாக மாற்றியது.",
                            "44வது திருத்தச் சட்டம் 1978: குடியரசுத் தலைவர் அமைச்சரவை ஆலோசனையை ஒருமுறை மறுபரிசீலனைக்கு அனுப்ப அனுமதிக்கப்படும் ஒரு நிபந்தனையைச் சேர்த்தது. இருப்பினும், மறுபரிசீலனை செய்யப்பட்ட அறிவுரை குடியரசுத் தலைவரைக் கட்டாயமாகக் கட்டுப்படுத்தும்.",
                            "உறுப்பு 74(2) பாதுகாப்பு: அமைச்சர்கள் குடியரசுத் தலைவருக்கு ஏதேனும் அறிவுரை வழங்கினார்களா, வழங்கினால் அது என்ன என்ற கேள்வியை எந்தவொரு நீதிமன்றமும் விசாரிக்க முடியாது."
                        ]
                    }
                }
            ],
            "sec_cabinet_committees": [
                {
                    "title": "1. Cabinet Committees & The 'Super Cabinet'",
                    "points": {
                        "en": [
                            "Extra-Constitutional Standing Bodies: Cabinet Committees are extra-constitutional standing/adhoc bodies set up under Government of India Transaction of Business Rules.",
                            "Chaired by PM: Prime Minister heads major Cabinet Committees including:",
                            "1. Cabinet Committee on Political Affairs (CCPA - known as the 'Super Cabinet')",
                            "2. Cabinet Committee on Economic Affairs (CCEA)",
                            "3. Cabinet Committee on Security (CCS)",
                            "4. Appointments Committee of the Cabinet (ACC)",
                            "Super Cabinet Role: CCPA deals with all domestic and foreign political issues and is the most powerful committee of the Indian Government."
                        ],
                        "ta": [
                            "அரசியலமைப்பற்ற நிரந்தரக் குழுக்கள்: கேபினட் குழுக்கள் என்பது இந்திய அரசு பரிவர்த்தனை வணிக விதிகளின் கீழ் அமைக்கப்பட்ட அரசியலமைப்பற்ற நிலைக் குழுக்களாகும்.",
                            "பிரதமர் தலைமை: முக்கிய கேபினட் குழுக்களுக்குப் பிரதமர் தலைமை தாங்குகிறார்:",
                            "1. அரசியல் விவகாரங்களுக்கான கேபினட் குழு (CCPA - 'சூப்பர் கேபினட்' என அழைக்கப்படுகிறது)",
                            "2. பொருளாதார விவகாரங்களுக்கான கேபினட் குழு (CCEA)",
                            "3. பாதுகாப்பு விவகாரங்களுக்கான கேபினட் குழு (CCS)",
                            "4. கேபினட்டின் நியமனங்கள் குழு (ACC)",
                            "சூப்பர் கேபினட் பங்கு: CCPA அனைத்து உள்நாட்டு மற்றும் வெளிநாட்டு அரசியல் பிரச்சினைகளையும் கையாள்கிறது மற்றும் இந்திய அரசின் மிகவும் சக்திவாய்ந்த குழுவாகும்."
                        ]
                    }
                }
            ],
            "comparison_tables": [
                {
                    "id": "comp_pres_vs_pm_master",
                    "title_en": "1. President of India vs Prime Minister of India — Master Comparison",
                    "title_ta": "1. இந்தியக் குடியரசுத் தலைவர் vs இந்தியப் பிரதமர் — மாஸ்டர் ஒப்பீடு",
                    "headers_en": ["Dimension", "President of India", "Prime Minister of India"],
                    "headers_ta": ["பரிமாணம்", "இந்தியக் குடியரசுத் தலைவர்", "இந்தியப் பிரதமர்"],
                    "rows_en": [
                        ["Constitutional Status", "Head of State (De Jure Executive)", "Head of Government (De Facto Executive)"],
                        ["Precedence Rank", "Rank 1 in Official Warrant of Precedence", "Rank 3 in Official Warrant of Precedence"],
                        ["Primary Articles", "Articles 52, 53, 54, 55, 56, 60, 61, 72, 123", "Articles 74, 75, 77, 78, 85"],
                        ["Legislative Role", "Integral part of Parliament; assents to bills (Art 111)", "Leader of the House; shapes legislative agenda"],
                        ["Emergency Powers", "Proclaims Emergency under Articles 352, 356, 360", "Recommends emergency invocation to President in writing"]
                    ],
                    "rows_ta": [
                        ["அரசியலமைப்பு நிலை", "நாட்டின் தலைவர் (De Jure நிர்வாகி)", "அரசாங்கத்தின் தலைவர் (De Facto நிர்வாகி)"],
                        ["முன்னுரிமை வரிசை", "அதிகாரப்பூர்வ முன்னுரிமை வரிசையில் 1ம் இடம்", "அதிகாரப்பூர்வ முன்னுரிமை வரிசையில் 3ம் இடம்"],
                        ["முதன்மை உறுப்புகள்", "உறுப்புகள் 52, 53, 54, 55, 56, 60, 61, 72, 123", "உறுப்புகள் 74, 75, 77, 78, 85"],
                        ["சட்டவாக்கப் பங்கு", "நாடாளுமன்றத்தின் ஒருங்கிணைந்த பகுதி; மசோதாக்களுக்கு ஒப்புதல் அளிக்கிறார்", "அவையின் தலைவர்; சட்டவாக்க நிகழ்ச்சி நிரலை வடிவமைக்கிறார்"],
                        ["அவசரகால அதிகாரங்கள்", "உறுப்புகள் 352, 356, 360-ன் கீழ் அவசரநிலையை அறிவிக்கிறார்", "எழுத்துப்பூர்வமாக அவசரநிலையைப் பிரகடனப்படுத்தக் குடியரசுத் தலைவருக்குப் பரிந்துரைக்கிறார்"]
                    ]
                },
                {
                    "id": "comp_pm_vs_cm_master",
                    "title_en": "2. Prime Minister vs Chief Minister — Constitutional Parallel",
                    "title_ta": "2. பிரதமர் vs முதலமைச்சர் — அரசியலமைப்பு ஒப்பீடு",
                    "headers_en": ["Constitutional Aspect", "Prime Minister of India", "Chief Minister of a State"],
                    "headers_ta": ["அரசியலமைப்பு அம்சம்", "இந்தியப் பிரதமர்", "மாநில முதலமைச்சர்"],
                    "rows_en": [
                        ["Constitutional Position", "Real Executive at Union Level (Part V)", "Real Executive at State Level (Part VI)"],
                        ["Core Article Parallel", "Article 74 (Aid & Advice to President)", "Article 163 (Aid & Advice to Governor)"],
                        ["Appointment Article", "Article 75(1) by President", "Article 164(1) by Governor"],
                        ["Duty to Inform Article", "Article 78 (Duty to inform President)", "Article 167 (Duty to inform Governor)"],
                        ["House Membership", "Member of Lok Sabha or Rajya Sabha", "Member of Legislative Assembly or Council"]
                    ],
                    "rows_ta": [
                        ["அரசியலமைப்பு நிலை", "ஒன்றிய அளவில் உண்மை நிர்வாகி (பகுதி V)", "மாநில அளவில் உண்மை நிர்வாகி (பகுதி VI)"],
                        ["முதன்மை விதி ஒப்பீடு", "உறுப்பு 74 (குடியரசுத் தலைவருக்கு உதவி & அறிவுரை)", "உறுப்பு 163 (ஆளுநருக்கு உதவி & அறிவுரை)"],
                        ["நியமன விதி", "உறுப்பு 75(1) குடியரசுத் தலைவரால்", "உறுப்பு 164(1) ஆளுநரால்"],
                        ["தகவல் தெரிவிக்கும் விதி", "உறுப்பு 78 (குடியரசுத் தலைவருக்குத் தெரிவிக்கும் கடமை)", "உறுப்பு 167 (ஆளுநருக்குத் தெரிவிக்கும் கடமை)"],
                        ["அவை உறுப்பினர் தகுதி", "மக்களவை அல்லது மாநிலங்களவை உறுப்பினர்", "சட்டமன்றப் பேரவை அல்லது மேலவை உறுப்பினர்"]
                    ]
                },
                {
                    "id": "comp_pm_vs_com_master",
                    "title_en": "3. Prime Minister vs Council of Ministers",
                    "title_ta": "3. பிரதமர் vs அமைச்சரவை (Council of Ministers)",
                    "headers_en": ["Feature", "Prime Minister", "Council of Ministers"],
                    "headers_ta": ["அம்சம்", "இந்தியப் பிரதமர்", "அமைச்சரவை (Council of Ministers)"],
                    "rows_en": [
                        ["Hierarchy", "Head and Keystone of Cabinet Arch", "Body of ministers headed by Prime Minister"],
                        ["Selection Role", "Selects candidates and advises President on appts", "Appointed by President on PM's recommendation"],
                        ["Effect of Resignation", "PM's resignation collapses entire Council", "Individual minister's resignation creates 1 vacancy"],
                        ["Cabinet Committee Role", "Chairs key Cabinet Committees (CCPA, CCEA, CCS)", "Members serve on committees allocated by PM"]
                    ],
                    "rows_ta": [
                        ["படிநிலை", "தலைவர் மற்றும் அமைச்சரவை வளைவின் முதன்மைக் கல்", "பிரதமரைத் தலைவராகக் கொண்ட அமைச்சர்களின் குழு"],
                        ["தேர்வுப் பங்கு", "வேட்பாளர்களைத் தேர்ந்தெடுத்து நியமனங்களுக்கு அறிவுறுத்துகிறார்", "பிரதமரின் பரிந்துரையின் பேரில் குடியரசுத் தலைவரால் நியமனம்"],
                        ["ராஜினாமா தாக்கம்", "பிரதமரின் ராஜினாமா முழு குழுவையும் கலைக்கும்", "தனிப்பட்ட அமைச்சரின் ராஜினாமா 1 காலியிடத்தை உருவாக்கும்"],
                        ["கேபினட் குழுப் பங்கு", "முக்கிய கேபினட் குழுக்களுக்குத் தலைமை தாங்குகிறார்", "பிரதமரால் ஒதுக்கப்பட்ட குழுக்களில் உறுப்பினர்களாகச் செயல்படுகின்றனர்"]
                    ]
                },
                {
                    "id": "comp_com_vs_cabinet_master",
                    "title_en": "4. Council of Ministers vs Cabinet — Advanced Analysis",
                    "title_ta": "4. அமைச்சர்கள் குழு vs கேபினட் — மேம்பட்ட பகுப்பாய்வு",
                    "headers_en": ["Dimension", "Council of Ministers", "Cabinet"],
                    "headers_ta": ["பரிமாணம்", "அமைச்சர்கள் குழு (Council of Ministers)", "கேபினட் (Cabinet)"],
                    "rows_en": [
                        ["Composition", "All 3 tiers: Cabinet Mins, Mins of State, Deputy Mins", "Only 1st tier: Senior Cabinet Rank Ministers"],
                        ["Constitutional Status", "Articles 74 & 75 (Original 1950 Constitution)", "Article 352 (Inserted by 44th CAA 1978)"],
                        ["Body Meetings", "Does not meet as a collective body in practice", "Meets frequently to formulate and direct policy"],
                        ["Policy Authority", "Vested with formal authority; executes cabinet policy", "Vested with real policy-making authority"]
                    ],
                    "rows_ta": [
                        ["அமைப்பு", "அனைத்து 3 நிலைகள்: கேபினட், ராஜாங்க, இணை அமைச்சர்கள்", "1ம் நிலை மட்டுமே: மூத்த கேபினட் அந்தஸ்து அமைச்சர்கள்"],
                        ["அரசியலமைப்பு நிலை", "உறுப்புகள் 74 & 75 (மூல 1950 அரசியலமைப்பு)", "உறுப்பு 352 (1978-ன் 44வது திருத்தத்தால் சேர்க்கப்பட்டது)"],
                        ["கூட்டங்கள்", "நடைமுறையில் ஒரு கூட்டமைப்பாக ஒன்று கூடுவதில்லை", "கொள்கைகளை உருவாக்க அடிக்கடி கூடுகிறது"],
                        ["கொள்கை அதிகாரம்", "முறையான அதிகாரம் கொண்டது; கேபினட் கொள்கையைச் செயல்படுத்துகிறது", "உண்மையான கொள்கை முடிவு எடுக்கும் அதிகாரம் கொண்டது"]
                    ]
                },
                {
                    "id": "comp_collective_vs_individual_master",
                    "title_en": "5. Collective Responsibility vs Individual Responsibility",
                    "title_ta": "5. கூட்டுப் பொறுப்பு vs தனிப்பட்ட பொறுப்பு",
                    "headers_en": ["Feature", "Collective Responsibility", "Individual Responsibility"],
                    "headers_ta": ["அம்சம்", "கூட்டுப் பொறுப்பு", "தனிப்பட்ட பொறுப்பு"],
                    "rows_en": [
                        ["Article", "Article 75(3)", "Article 75(2)"],
                        ["Target Body", "Lok Sabha (House of the People)", "President of India"],
                        ["Key Mechanism", "No-Confidence Motion under Rule 198", "Dismissal by President on advice of PM"],
                        ["Core Principle", "Solidarity of Cabinet; swim or sink together", "Minister holds office during pleasure of President"]
                    ],
                    "rows_ta": [
                        ["உறுப்பு", "உறுப்பு 75(3)", "உறுப்பு 75(2)"],
                        ["பொறுப்பான அமைப்பு", "மக்களவை (House of the People)", "இந்தியக் குடியரசுத் தலைவர்"],
                        ["முக்கிய பொறிமுறை", "விதி 198-ன் கீழ் நம்பிக்கையில்லாத் தீர்மானம்", "பிரதமரின் அறிவுரைப்படி குடியரசுத் தலைவரால் பதவி நீக்கம்"],
                        ["முதன்மை தத்துவம்", "அமைச்சரவையின் ஒற்றுமை; ஒன்றாக நீந்துதல் அல்லது மூழ்குதல்", "அமைச்சர் குடியரசுத் தலைவரின் விருப்பம் உள்ளவரை பதவி வகிக்கிறார்"]
                    ]
                },
                {
                    "id": "comp_const_power_vs_convention",
                    "title_en": "6. Constitutional Power vs Constitutional Convention",
                    "title_ta": "6. அரசியலமைப்பு அதிகாரம் vs அரசியலமைப்பு மரபு",
                    "headers_en": ["Criteria", "Constitutional Power (Codified Text)", "Constitutional Convention (Unwritten Tradition)"],
                    "headers_ta": ["அளவுகோல்", "அரசியலமைப்பு அதிகாரம் (எழுதப்பட்ட உரை)", "அரசியலமைப்பு மரபு (எழுதப்படாத பாரம்பரியம்)"],
                    "rows_en": [
                        ["Legal Enforceability", "Written in text of Constitution; legally binding", "Unwritten parliamentary practice; politically binding"],
                        ["Example: Appointment", "Art 75(1): 'PM shall be appointed by President'", "President appoints leader of Lok Sabha majority party as PM"],
                        ["Example: Cabinet", "Art 74 creates Council of Ministers", "Caretaker Govt avoids taking major policy decisions"],
                        ["Modification", "Requires Constitutional Amendment Act (Art 368)", "Evolves naturally through parliamentary precedents"]
                    ],
                    "rows_ta": [
                        ["சட்ட அமலாக்கம்", "அரசியலமைப்பு உரையில் எழுதப்பட்டது; சட்டப்படி கட்டுப்படுத்தும்", "எழுதப்படாத நாடாளுமன்ற நடைமுறை; அரசியல் ரீதியாக கட்டுப்படுத்தும்"],
                        ["உதாரணம்: நியமனம்", "உறுப்பு 75(1): 'பிரதமர் குடியரசுத் தலைவரால் நியமிக்கப்படுவார்'", "மக்களவை பெரும்பான்மை தலைவரைப் பிரதமராகக் குடியரசுத் தலைவர் நியமிக்கிறார்"],
                        ["உதாரணம்: கேபினட்", "உறுப்பு 74 அமைச்சரவையை உருவாக்குகிறது", "பராமரிப்பு அரசாங்கம் முக்கிய கொள்கை முடிவுகளை எடுப்பதைத் தவிர்க்கிறது"],
                        ["மாற்றம்", "அரசியலமைப்பு திருத்தச் சட்டம் தேவை (உறுப்பு 368)", "நாடாளுமன்ற முன்னுதாரணங்கள் மூலம் இயற்கையாக உருவாகிறது"]
                    ]
                },
                {
                    "id": "comp_majority_vs_coalition",
                    "title_en": "7. Majority Government vs Coalition Government",
                    "title_ta": "7. பெரும்பான்மை அரசாங்கம் vs கூட்டணி அரசாங்கம்",
                    "headers_en": ["Aspect", "Majority Government", "Coalition Government"],
                    "headers_ta": ["அம்சம்", "பெரும்பான்மை அரசாங்கம்", "கூட்டணி அரசாங்கம்"],
                    "rows_en": [
                        ["Lok Sabha Strength", "Single political party holds 272+ seats", "Multiple political parties join together to reach 272+ seats"],
                        ["PM Authority", "Prime Minister exercises dominant cabinet control", "Prime Minister must consensus-build among coalition allies"],
                        ["Cabinet Stability", "High stability; low threat of internal collapse", "Vulnerable to withdrawal of support by coalition partners"],
                        ["Policy Flexibility", "Swift decision making aligned with single party manifesto", "Policy making constrained by Common Minimum Programme (CMP)"]
                    ],
                    "rows_ta": [
                        ["மக்களவை பலம்", "ஒற்றை அரசியல் கட்சி 272+ இடங்களைக் கொண்டுள்ளது", "272+ இடங்களை எட்ட பல அரசியல் கட்சிகள் இணைகின்றன"],
                        ["பிரதமர் அதிகாரம்", "பிரதமர் ஆதிக்கம் செலுத்தும் கேபினட் கட்டுப்பாட்டைப் பயன்படுத்துகிறார்", "கூட்டணிக் கூட்டாளிகளிடையே பிரதமர் ஒருமித்த கருத்தை உருவாக்க வேண்டும்"],
                        ["கேபினட் ஸ்திரத்தன்மை", "அதிக ஸ்திரத்தன்மை; உள்நாட்டு வீழ்ச்சி அச்சுறுத்தல் குறைவு", "கூட்டணிக் பங்காளிகள் ஆதரவை வாபஸ் பெறுவதால் பாதிப்படையக்கூடியது"],
                        ["கொள்கை நெகிழ்வுத்தன்மை", "ஒற்றைக் கட்சி தேர்தல் அறிக்கையுடன் இணைந்த விரைவான முடிவு", "பொதுக் குறைந்தபட்சத் திட்டத்தால் (CMP) கொள்கை முடிவு கட்டுப்படுத்தப்படுகிறது"]
                    ]
                },
                {
                    "id": "comp_normal_vs_caretaker",
                    "title_en": "8. Normal Government vs Caretaker Government",
                    "title_ta": "8. சாதாரண அரசாங்கம் vs பராமரிப்பு அரசாங்கம் (Caretaker Govt)",
                    "headers_en": ["Dimension", "Normal Government", "Caretaker Government"],
                    "headers_ta": ["பரிமாணம்", "சாதாரண அரசாங்கம்", "பராமரிப்பு அரசாங்கம் (Caretaker Govt)"],
                    "rows_en": [
                        ["Operational Basis", "Enjoys active majority confidence in Lok Sabha", "Continues after LS dissolution until new govt takes oath"],
                        ["Policy Powers", "Can introduce new legislation, policy & budgets", "Restricted by convention to routine day-to-day administration"],
                        ["Financial Decisions", "Can pass full Union Budget & major expenditure", "Limited to Vote on Account / essential routine expenditure"],
                        ["Constitutional Status", "Constitutional body under Article 74 & 75", "Convention-based continuity under Article 74 requirement"]
                    ],
                    "rows_ta": [
                        ["செயல்பாட்டு அடிப்படை", "மக்களவையில் செயலில் உள்ள பெரும்பான்மை நம்பிக்கையைக் கொண்டுள்ளது", "மக்களவைக் கலைக்கப்பட்ட பின் புதிய அரசு பதவியேற்கும் வரை தொடர்கிறது"],
                        ["கொள்கை அதிகாரங்கள்", "புதிய சட்டங்கள், கொள்கைகள் & பட்ஜெட்டுகளை அறிமுகப்படுத்தலாம்", "மரபுப்படி அன்றாட வழக்கமான நிர்வாகத்திற்கு மட்டுமே வரம்பிற்குட்பட்டது"],
                        ["நிதி முடிவுகள்", "முழு ஒன்றிய பட்ஜெட் & முக்கிய செலவினங்களை நிறைவேற்றலாம்", "கணக்கு வாக்கெடுப்பு (Vote on Account) / அத்தியாவசிய செலவினங்களுக்கு வரம்பிற்குட்பட்டது"],
                        ["அரசியலமைப்பு நிலை", "உறுப்புகள் 74 & 75-ன் கீழ் உள்ள அரசியலமைப்பு அமைப்பு", "உறுப்பு 74 தேவையின் கீழ் மரபு சார்ந்த தொடர்ச்சி"]
                    ]
                }
            ],
            "mind_map": [
                {
                    "title": "Prime Minister Special Topics & Master Revision (Part V)",
                    "short_label": "PM Part 3 Master",
                    "children": [
                        {
                            "title": "1. Responsibility Doctrines",
                            "short_label": "Responsibility",
                            "children": [
                                {
                                    "title": "Collective Responsibility (Art 75(3)): Lok Sabha only (Rule 198 No-Confidence)",
                                    "short_label": "Art 75(3) Collective"
                                },
                                {
                                    "title": "Individual Responsibility (Art 75(2)): President's pleasure on PM advice",
                                    "short_label": "Art 75(2) Individual"
                                }
                            ]
                        },
                        {
                            "title": "2. Hung House & Caretaker Govt",
                            "short_label": "Hung & Caretaker",
                            "children": [
                                {
                                    "title": "Hung House: President appoints largest party leader (SR Bommai Floor Test)",
                                    "short_label": "Hung House Floor Test"
                                },
                                {
                                    "title": "Caretaker Govt: Art 74 continuity mandate; routine admin only (no major policy)",
                                    "short_label": "Caretaker Admin"
                                }
                            ]
                        },
                        {
                            "title": "3. Advanced PM-President Relations",
                            "short_label": "PM-President",
                            "children": [
                                {
                                    "title": "42nd CAA 1976: Aid & advice binding on President",
                                    "short_label": "42nd CAA Binding"
                                },
                                {
                                    "title": "44th CAA 1978: One-time reconsideration option for President",
                                    "short_label": "44th CAA Reconsider"
                                },
                                {
                                    "title": "Article 74(2): Advice tendered by ministers cannot be inquired by court",
                                    "short_label": "Art 74(2) Protection"
                                }
                            ]
                        },
                        {
                            "title": "4. Cabinet Committees & TNPSC Revision",
                            "short_label": "Committees & Revision",
                            "children": [
                                {
                                    "title": "CCPA ('Super Cabinet'), CCEA, CCS, ACC chaired by PM",
                                    "short_label": "Super Cabinet CCPA"
                                },
                                {
                                    "title": "Articles 74 to 78 Quick Map & Top 20 TNPSC Trap Points",
                                    "short_label": "Art 74-78 Master Map"
                                }
                            ]
                        }
                    ]
                }
            ],
            "tnpsc_traps": [
                {
                    "title": "1. Directly Elected PM Myth Trap (நேரடித் தேர்தல் கட்டுக்கதைப் பொறி)",
                    "points": {
                        "en": [
                            "TRAP: Believing the Prime Minister of India is directly elected by the voters of India.",
                            "FACT: Voters elect Members of Parliament (MPs). The Prime Minister is APPOINTED by the President of India under Article 75(1)!"
                        ],
                        "ta": [
                            "பொறி: இந்தியப் பிரதமர் இந்திய வாக்காளர்களால் நேரடியாகத் தேர்ந்தெடுக்கப்படுகிறார் என நம்புவது.",
                            "உண்மை: வாக்காளர்கள் நாடாளுமன்ற உறுப்பினர்களைத் (எம்பிக்கள்) தேர்ந்தெடுக்கின்றனர். பிரதமர் உறுப்பு 75(1)-ன் கீழ் இந்தியக் குடியரசுத் தலைவரால் நியமிக்கப்படுகிறார்!"
                        ]
                    }
                },
                {
                    "title": "2. Rajya Sabha Collective Responsibility Trap (மாநிலங்களவைக் கூட்டுப் பொறுப்புப் பொறி)",
                    "points": {
                        "en": [
                            "TRAP: Assuming Council of Ministers is collectively responsible to Rajya Sabha or Parliament as a whole.",
                            "FACT: Article 75(3) strictly specifies collective responsibility ONLY to Lok Sabha (House of the People)!"
                        ],
                        "ta": [
                            "பொறி: அமைச்சரவை மாநிலங்களவைக்கு அல்லது முழு நாடாளுமன்றத்திற்கும் கூட்டாகப் பொறுப்புடையது எனக் கருதுவது.",
                            "உண்மை: உறுப்பு 75(3) மக்களவைக்கு (Lok Sabha) மட்டுமே கூட்டாகப் பொறுப்புடையது என்று தெளிவாகக் குறிப்பிடுகிறது!"
                        ]
                    }
                },
                {
                    "title": "3. Non-MP Prime Minister 6-Month Window Trap (6 மாத அவகாசப் பொறி)",
                    "points": {
                        "en": [
                            "TRAP: Believing a non-MP can NEVER be appointed as Prime Minister.",
                            "FACT: Under Article 75(5), a non-MP CAN be appointed Prime Minister, but MUST secure membership of either House within 6 consecutive months!"
                        ],
                        "ta": [
                            "பொறி: நாடாளுமன்ற உறுப்பினர் அல்லாத ஒருவர் ஒருபோதும் பிரதமராக நியமிக்கப்பட முடியாது என நினைப்பது.",
                            "உண்மை: உறுப்பு 75(5)-ன் கீழ் உறுப்பினர் அல்லாத ஒருவர் பிரதமராக நியமிக்கப்படலாம், ஆனால் 6 மாதங்களுக்குள் ஏதேனும் ஒரு அவையில் உறுப்பினராக வேண்டும்!"
                        ]
                    }
                },
                {
                    "title": "4. No-Confidence Motion Origination Trap (நம்பிக்கையில்லாத் தீர்மான அவை பொறி)",
                    "points": {
                        "en": [
                            "TRAP: Believing No-Confidence Motion can be introduced in Rajya Sabha.",
                            "FACT: No-Confidence Motion can be introduced ONLY in Lok Sabha under Lok Sabha Rule 198 (requires 50 MPs support)!"
                        ],
                        "ta": [
                            "பொறி: நம்பிக்கையில்லாத் தீர்மானத்தை மாநிலங்களவையிலும் கொண்டு வரலாம் என நம்புவது.",
                            "உண்மை: நம்பிக்கையில்லாத் தீர்மானம் மக்களவை விதி 198-ன் கீழ் மக்களவையில் மட்டுமே கொண்டு வர முடியும் (50 எம்பிக்கள் ஆதரவு தேவை)!"
                        ]
                    }
                },
                {
                    "title": "5. Cabinet Word Constitutional History Trap (கேபினட் சொல் வரலாறு பொறி)",
                    "points": {
                        "en": [
                            "TRAP: Believing 'Cabinet' was defined in Article 74 or 75 of original Constitution.",
                            "FACT: The word 'Cabinet' was added ONLY to Article 352 by the 44th Constitutional Amendment Act 1978!"
                        ],
                        "ta": [
                            "பொறி: மூல அரசியலமைப்பின் உறுப்பு 74 அல்லது 75-ல் 'Cabinet' வரையறுக்கப்பட்டது எனக் கருதுவது.",
                            "உண்மை: 'Cabinet' என்ற சொல் 1978-ன் 44வது அரசியலமைப்புத் திருத்தச் சட்டத்தின் மூலம் உறுப்பு 352-ல் மட்டுமே சேர்க்கப்பட்டது!"
                        ]
                    }
                },
                {
                    "title": "6. Caretaker Government Text Trap (பராமரிப்பு அரசாங்க உரையாக்கப் பொறி)",
                    "points": {
                        "en": [
                            "TRAP: Assuming 'Caretaker Government' is explicitly defined in Part V of the Constitution.",
                            "FACT: 'Caretaker Government' is a constitutional CONVENTION. The Constitution in Article 74 mandates that a Council of Ministers must ALWAYS exist!"
                        ],
                        "ta": [
                            "பொறி: 'Caretaker Government' என்பது அரசியலமைப்பின் பகுதி V-ல் தெளிவாக வரையறுக்கப்பட்டுள்ளது என நினைப்பது.",
                            "உண்மை: 'Caretaker Government' என்பது ஓர் அரசியலமைப்பு மரபு. உறுப்பு 74 எப்போதும் ஓர் அமைச்சரவை இருக்க வேண்டும் என்று ஆணையிடுகிறது!"
                        ]
                    }
                },
                {
                    "title": "7. Article 74(2) Judicial Review Trap (நீதிமன்ற மறுஆய்வுப் பொறி)",
                    "points": {
                        "en": [
                            "TRAP: Thinking courts can inquire into what advice ministers gave to the President.",
                            "FACT: Article 74(2) explicitly bars courts from inquiring into any advice tendered by Ministers to the President!"
                        ],
                        "ta": [
                            "பொறி: குடியரசுத் தலைவருக்கு அமைச்சர்கள் என்ன அறிவுரை வழங்கினார்கள் என்பதை நீதிமன்றங்கள் விசாரிக்கலாம் என நினைப்பது.",
                            "உண்மை: உறுப்பு 74(2) குடியரசுத் தலைவருக்கு அமைச்சர்கள் வழங்கிய அறிவுரையை நீதிமன்றங்கள் விசாரிப்பதைத் தெளிவாகத் தடுக்கிறது!"
                        ]
                    }
                },
                {
                    "title": "8. Super Cabinet Identity Trap (சூப்பர் கேபினட் அடையாளப் பொறி)",
                    "points": {
                        "en": [
                            "TRAP: Believing NITI Aayog or Union Cabinet itself is called the 'Super Cabinet'.",
                            "FACT: The Cabinet Committee on Political Affairs (CCPA), chaired by the PM, is known as the 'Super Cabinet'!"
                        ],
                        "ta": [
                            "பொறி: நிதி ஆயோக் அல்லது ஒன்றிய அமைச்சரவையே 'சூப்பர் கேபினட்' என்று அழைக்கப்படுகிறது என நினைப்பது.",
                            "உண்மை: பிரதமர் தலைமையிலான அரசியல் விவகாரங்களுக்கான கேபினட் குழுவே (CCPA) 'சூப்பர் கேபினட்' என அழைக்கப்படுகிறது!"
                        ]
                    }
                },
                {
                    "title": "9. Presidential Reconsideration Trap (குடியரசுத் தலைவர் மறுபரிசீலனைப் பொறி)",
                    "points": {
                        "en": [
                            "TRAP: Believing President can repeatedly return Cabinet advice for reconsideration.",
                            "FACT: Under 44th CAA 1978, President can return advice ONCE. If Cabinet resends it, President MUST accept it!"
                        ],
                        "ta": [
                            "பொறி: குடியரசுத் தலைவர் அமைச்சரவை ஆலோசனையை மீண்டும் மீண்டும் மறுபரிசீலனைக்கு அனுப்பலாம் என நினைப்பது.",
                            "உண்மை: 44வது CAA 1978-ன் கீழ் குடியரசுத் தலைவர் ஆலோசனையை ஒருமுறை மட்டுமே அனுப்ப முடியும். அமைச்சரவை மீண்டும் அனுப்பினால், குடியரசுத் தலைவர் அதை ஏற்க வேண்டும்!"
                        ]
                    }
                },
                {
                    "title": "10. Money Bill Defeat Consequence Trap (பண மசோதா தோல்விப் பொறி)",
                    "points": {
                        "en": [
                            "TRAP: Believing defeat of a Money Bill in Lok Sabha does not affect the Prime Minister.",
                            "FACT: Defeat of a Money Bill in Lok Sabha signifies loss of majority confidence, forcing the PM and Cabinet to resign immediately!"
                        ],
                        "ta": [
                            "பொறி: மக்களவையில் பண மசோதா தோற்பது பிரதமரைப் பாதிக்காது என நினைப்பது.",
                            "உண்மை: மக்களவையில் பண மசோதா தோற்பது பெரும்பான்மை நம்பிக்கையை இழப்பதைக் குறிக்கிறது, இது பிரதமரையும் அமைச்சரவையையும் உடனடியாக ராஜினாமா செய்யக் கட்டாயப்படுத்துகிறது!"
                        ]
                    }
                }
            ],
            "important_facts": {
                "en": [
                    "Article 75(3): Council of Ministers is collectively responsible strictly to Lok Sabha (House of the People).",
                    "Article 75(2): Ministers hold office individually during pleasure of President (exercised on advice of PM).",
                    "Article 75(5): A non-MP can be appointed Prime Minister for maximum 6 consecutive months.",
                    "Rule 198: No-Confidence Motion can be moved ONLY in Lok Sabha with support of minimum 50 MPs.",
                    "44th CAA 1978: Inserted the word 'Cabinet' into Article 352 and allowed President one-time reconsideration of advice.",
                    "Article 74(2): Advice tendered by Ministers to President cannot be inquired into by any court.",
                    "Super Cabinet: Cabinet Committee on Political Affairs (CCPA) chaired by Prime Minister.",
                    "S.R. Bommai Case (1994): Executive majority MUST be tested strictly on the floor of the House (Floor Test).",
                    "Caretaker Government: Convention-based continuation of admin post-dissolution; cannot make major policy changes.",
                    "Rajya Sabha PMs: Indira Gandhi (1966), H.D. Deve Gowda (1996), I.K. Gujral (1997), Dr. Manmohan Singh (2004, 2009)."
                ],
                "ta": [
                    "உறுப்பு 75(3): அமைச்சரவை மக்களவைக்கு (House of the People) மட்டுமே கூட்டாகப் பொறுப்புடையது.",
                    "உறுப்பு 75(2): அமைச்சர்கள் தனித்தனியாகக் குடியரசுத் தலைவரின் விருப்பம் உள்ளவரை பதவி வகிக்கின்றனர் (பிரதமரின் அறிவுரைப்படி).",
                    "உறுப்பு 75(5): நாடாளுமன்ற உறுப்பினர் அல்லாத ஒருவர் அதிகபட்சம் 6 தொடர்ச்சியான மாதங்கள் பிரதமராக இருக்க முடியும்.",
                    "விதி 198: நம்பிக்கையில்லாத் தீர்மானம் மக்களவையில் மட்டுமே 50 எம்பிக்கள் ஆதரவுடன் கொண்டு வர முடியும்.",
                    "44வது CAA 1978: உறுப்பு 352-ல் 'Cabinet' என்ற சொல்லைச் சேர்த்தது மற்றும் குடியரசுத் தலைவருக்கு ஒருமுறை மறுபரிசீலனை உரிமையை அளித்தது.",
                    "உறுப்பு 74(2): குடியரசுத் தலைவருக்கு அமைச்சர்கள் வழங்கிய அறிவுரையை எந்தவொரு நீதிமன்றமும் விசாரிக்க முடியாது.",
                    "சூப்பர் கேபினட்: பிரதமர் தலைமையிலான அரசியல் விவகாரங்களுக்கான கேபினட் குழு (CCPA).",
                    "எஸ்.ஆர். பொம்மை வழக்கு (1994): நிர்வாகப் பெரும்பான்மை கட்டாயமாக அவையின் தளத்தில் (Floor Test) மட்டுமே நிரூபிக்கப்பட வேண்டும்.",
                    "பராமரிப்பு அரசாங்கம்: கலைப்பிற்குப் பிந்தைய மரபு சார்ந்த நிர்வாகத் தொடர்ச்சி; முக்கிய கொள்கை மாற்றங்களைச் செய்ய முடியாது.",
                    "மாநிலங்களவைப் பிரதமர்கள்: இந்திரா காந்தி (1966), தேவ கௌடா (1996), ஐ.கே. குஜ்ரால் (1997), மன்மோகன் சிங் (2004, 2009)."
                ]
            },
            "quick_revision": {
                "en": [
                    "Article 74: Council of Ministers with PM at head aids & advises President; advice binding post 42nd/44th CAAs.",
                    "Article 75(1): President appoints PM (majority leader convention); appoints other ministers on PM advice.",
                    "Article 75(2): Individual responsibility — ministers hold office during pleasure of President (exercised on PM advice).",
                    "Article 75(3): Collective responsibility — Council of Ministers collectively responsible strictly to Lok Sabha.",
                    "Article 75(5): Non-MP PM/minister must secure Parliament seat within 6 consecutive months.",
                    "Article 77: All executive action taken in President's name; PM makes rules for transaction of business.",
                    "Article 78: PM duty to inform President of cabinet decisions, legislative proposals, & submit single minister decisions.",
                    "No-Confidence Motion: LS Rule 198, requires 50 MPs; floor test is ultimate proof of majority."
                ],
                "ta": [
                    "உறுப்பு 74: பிரதமரைத் தலைவராகக் கொண்ட அமைச்சரவை குடியரசுத் தலைவருக்கு உதவவும் அறிவுறுத்தவும் செய்கிறது; 42/44 திருத்தங்களுக்கு பின் அறிவுரை கட்டுப்படுத்தும்.",
                    "உறுப்பு 75(1): குடியரசுத் தலைவர் பிரதமரை நியமிக்கிறார் (பெரும்பான்மை தலைவர் மரபு); பிரதமர் அறிவுரைப்படி பிற அமைச்சர்களை நியமிக்கிறார்.",
                    "உறுப்பு 75(2): தனிப்பட்ட பொறுப்பு — அமைச்சர்கள் குடியரசுத் தலைவரின் விருப்பம் உள்ளவரை பதவி வகிக்கின்றனர் (பிரதமர் அறிவுரைப்படி).",
                    "உறுப்பு 75(3): கூட்டுப் பொறுப்பு — அமைச்சரவை மக்களவைக்கு மட்டுமே கூட்டாகப் பொறுப்புடையது.",
                    "உறுப்பு 75(5): உறுப்பினர் அல்லாத பிரதமர்/அமைச்சர் 6 தொடர்ச்சியான மாதங்களுக்குள் நாடாளுமன்ற இடத்தை பெற வேண்டும்.",
                    "உறுப்பு 77: அனைத்து நிர்வாக நடவடிக்கைகளும் குடியரசுத் தலைவர் பெயரால் மேற்கொள்ளப்படுகின்றன; ஆட்சிப் பணி விதிகளைப் பிரதமர் உருவாக்குகிறார்.",
                    "உறுப்பு 78: கேபினட் முடிவுகள், சட்ட முன்மொழிவுகளைக் குடியரசுத் தலைவருக்குத் தெரிவிப்பது & தனி அமைச்சர் முடிவை அளிப்பது பிரதமரின் கடமை.",
                    "நம்பிக்கையில்லாத் தீர்மானம்: மக்களவை விதி 198, 50 எம்பிக்கள் தேவை; நம்பிக்கை வாக்கெடுப்பே பெரும்பான்மையின் இறுதிச் சான்றாகும்."
                ]
            },
            "revision_cards": [
                {
                    "title": "Article 74(1)",
                    "content_en": "Council of Ministers with Prime Minister at head aids and advises President.",
                    "content_ta": "பிரதமரைத் தலைவராகக் கொண்ட அமைச்சரவை குடியரசுத் தலைவருக்கு உதவவும் அறிவுரை வழங்கவும் செய்கிறது."
                },
                {
                    "title": "Article 75(1)",
                    "content_en": "Prime Minister appointed by President; Ministers appointed on PM advice.",
                    "content_ta": "பிரதமர் குடியரசுத் தலைவரால் நியமனம்; பிற அமைச்சர்கள் பிரதமர் அறிவுரைப்படி நியமனம்."
                },
                {
                    "title": "Article 75(2)",
                    "content_en": "Individual Responsibility — Ministers hold office during pleasure of President.",
                    "content_ta": "தனிப்பட்ட பொறுப்பு — அமைச்சர்கள் குடியரசுத் தலைவரின் விருப்பம் உள்ளவரை பதவி வகிக்கின்றனர்."
                },
                {
                    "title": "Article 75(3)",
                    "content_en": "Collective Responsibility — Council of Ministers collectively responsible to Lok Sabha.",
                    "content_ta": "கூட்டுப் பொறுப்பு — அமைச்சரவை மக்களவைக்குக் கூட்டாகப் பொறுப்புடையது."
                },
                {
                    "title": "Article 75(5)",
                    "content_en": "Non-MP PM or Minister has 6 consecutive months to get elected to Parliament.",
                    "content_ta": "உறுப்பினர் அல்லாத பிரதமர்/அமைச்சர் நாடாளுமன்றத்திற்குத் தேர்ந்தெடுக்கப்பட 6 மாத அவகாசம்."
                },
                {
                    "title": "Article 77",
                    "content_en": "Conduct of business of Govt of India; all executive action in President's name.",
                    "content_ta": "இந்திய அரசின் ஆட்சிப் பணிகள் நிர்வாகம்; அனைத்து நிர்வாக நடவடிக்கைகளும் குடியரசுத் தலைவர் பெயரால்."
                },
                {
                    "title": "Article 78",
                    "content_en": "Duties of Prime Minister in furnishing administrative info to President.",
                    "content_ta": "குடியரசுத் தலைவருக்கு நிர்வாகத் தகவல்களை வழங்குவதில் பிரதமரின் கடமைகள்."
                },
                {
                    "title": "Super Cabinet",
                    "content_en": "Cabinet Committee on Political Affairs (CCPA) chaired by Prime Minister.",
                    "content_ta": "பிரதமர் தலைமையிலான அரசியல் விவகாரங்களுக்கான கேபினட் குழு (CCPA)."
                },
                {
                    "title": "Rule 198 No-Confidence",
                    "content_en": "Moved ONLY in Lok Sabha with support of 50 MPs; causes cabinet collapse.",
                    "content_ta": "மக்களவையில் மட்டுமே 50 எம்பிக்கள் ஆதரவுடன் கொண்டு வரப்படும்; அமைச்சரவையைக் கலைக்கும்."
                },
                {
                    "title": "44th CAA 1978 Proviso",
                    "content_en": "President can return Cabinet advice ONCE for reconsideration.",
                    "content_ta": "குடியரசுத் தலைவர் அமைச்சரவை ஆலோசனையை ஒருமுறை மறுபரிசீலனைக்கு அனுப்பலாம்."
                },
                {
                    "title": "S.R. Bommai Principle",
                    "content_en": "Executive majority must be tested strictly on the floor of the House.",
                    "content_ta": "நிர்வாகப் பெரும்பான்மை கட்டாயமாக அவையின் தளத்தில் மட்டுமே நிரூபிக்கப்பட வேண்டும்."
                },
                {
                    "title": "Caretaker Government",
                    "content_en": "Convention-based continuity body; restricted to routine day-to-day administration.",
                    "content_ta": "மரபு சார்ந்த நிர்வாகத் தொடர்ச்சி அமைப்பு; அன்றாட வழக்கமான நிர்வாகத்திற்கு வரம்பிற்குட்பட்டது."
                },
                {
                    "title": "Hung House Discretion",
                    "content_en": "President appoints largest party leader as PM and mandates 1-month floor test.",
                    "content_ta": "குடியரசுத் தலைவர் மிகப்பெரிய கட்சித் தலைவரை நியமித்து 1 மாதத்தில் பெரும்பான்மையை நிரூபிக்கப் பணிக்கிறார்."
                },
                {
                    "title": "Rajya Sabha PM Precedents",
                    "content_en": "Indira Gandhi (1966), Deve Gowda (1996), I.K. Gujral (1997), Manmohan Singh (2004, 2009).",
                    "content_ta": "இந்திரா காந்தி (1966), தேவ கௌடா (1996), ஐ.கே. குஜ்ரால் (1997), மன்மோகன் சிங் (2004, 2009)."
                },
                {
                    "title": "Article 74(2) Protection",
                    "content_en": "Courts barred from inquiring into advice tendered by ministers to President.",
                    "content_ta": "குடியரசுத் தலைவருக்கு அமைச்சர்கள் வழங்கிய அறிவுரையை நீதிமன்றங்கள் விசாரிக்கத் தடை."
                }
            ]
        }
    }
    return part3_data

def validate_part3(data):
    meta = data.get("meta", {})
    assert meta.get("topic_id") == "polity_prime_minister_part_3", f"Invalid topic_id: {meta.get('topic_id')}"
    assert meta.get("part") == 3, f"Invalid part: {meta.get('part')}"
    assert meta.get("total_parts") == 3, f"Invalid total_parts: {meta.get('total_parts')}"
    
    content = data.get("content", {})
    tables = content.get("comparison_tables") or []
    assert len(tables) == 8, f"Expected 8 comparison tables, got {len(tables)}"
    for idx, t in enumerate(tables, 1):
        assert "headers_en" in t and len(t["headers_en"]) > 0, f"Table {idx} missing headers_en"
        assert "headers_ta" in t and len(t["headers_ta"]) > 0, f"Table {idx} missing headers_ta"
        assert "rows_en" in t and len(t["rows_en"]) > 0, f"Table {idx} missing rows_en"
        assert "rows_ta" in t and len(t["rows_ta"]) > 0, f"Table {idx} missing rows_ta"
        assert len(t["rows_en"]) == len(t["rows_ta"]), f"Table {idx} row count mismatch"
        for r_idx, r in enumerate(t["rows_en"]):
            assert len(r) == len(t["headers_en"]), f"Table {idx} Row EN {r_idx} len mismatch"
        for r_idx, r in enumerate(t["rows_ta"]):
            assert len(r) == len(t["headers_ta"]), f"Table {idx} Row TA {r_idx} len mismatch"

    mind_map = content.get("mind_map", [])
    assert len(mind_map) > 0, "Mind map missing"
    
    traps = content.get("tnpsc_traps", [])
    assert len(traps) >= 10, f"Expected at least 10 TNPSC traps, got {len(traps)}"
    
    rev = content.get("revision_cards", [])
    assert len(rev) >= 12, f"Expected at least 12 revision cards, got {len(rev)}"

    assert content.get("important_facts", {}).get("en") and content.get("important_facts", {}).get("ta")
    assert content.get("quick_revision", {}).get("en") and content.get("quick_revision", {}).get("ta")
    print("✅ PART 3 VALIDATION PASSED COMPLETELY!")

def main():
    print("==================================================")
    print("GENERATING & VALIDATING PRIME MINISTER PART 3 NOTES")
    print("==================================================")
    data = generate_part3()
    validate_part3(data)
    
    out_dir = "data/notes/polity"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "prime_minister_part_3.json")
    
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
    assert os.path.exists(out_path), f"File was not created at {out_path}"
    print(f"✅ SAVED IMMEDIATELY & CONFIRMED FILE EXISTS: {out_path}")

if __name__ == "__main__":
    main()
