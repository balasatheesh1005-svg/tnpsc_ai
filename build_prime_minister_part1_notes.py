import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

def generate_part1():
    part1_data = {
        "meta": {
            "topic_id": "polity_prime_minister_part_1",
            "repository_id": "polity_prime_minister",
            "display_title": "Prime Minister of India – Part 1",
            "part": 1,
            "total_parts": 3,
            "subject": "polity",
            "chapter": "Prime Minister of India",
            "language": "English + Tamil"
        },
        "metadata": {
            "topic_id": "polity_prime_minister_part_1",
            "repository_id": "polity_prime_minister",
            "display_title": "Prime Minister of India – Part 1",
            "part": 1,
            "total_parts": 3,
            "subject": "polity",
            "chapter": "Prime Minister of India",
            "language": "English + Tamil"
        },
        "keywords": [
            "Prime Minister of India",
            "இந்தியப் பிரதமர்",
            "Article 74",
            "உறுப்பு 74",
            "Article 75",
            "உறுப்பு 75",
            "Article 77",
            "உறுப்பு 77",
            "Article 78",
            "உறுப்பு 78",
            "Real Executive",
            "உண்மை நிர்வாகி",
            "Nominal Executive",
            "பெயரளவு நிர்வாகி",
            "Council of Ministers",
            "அமைச்சரவை",
            "Westminster Model",
            "வெஸ்ட்மின்ஸ்டர் மாதிரி",
            "Appointment of Prime Minister",
            "பிரதமர் நியமனம்",
            "Oath of Secrecy",
            "இரகசியக் காப்புப் பிரமாணம்",
            "Hung Lok Sabha",
            "தொங்கு மக்களவை"
        ],
        "learning_outcomes": {
            "Understand": {
                "en": [
                    "Master the constitutional position of the Prime Minister under Articles 74 and 75 as the real executive (de facto head).",
                    "Differentiate between the President as Nominal Executive (De Jure) and Prime Minister as Real Executive (De Facto).",
                    "Understand the appointment process under Article 75(1) and the political convention of selecting the majority leader in Lok Sabha.",
                    "Analyze qualifications, membership requirements in Parliament (either House or non-MP with 6-month limit under Art 75(5)).",
                    "Grasp the nature of oath of office and secrecy (Third Schedule) administered by the President under Article 75(4).",
                    "Understand the tenure of office (pleasure of President tied strictly to Lok Sabha confidence)."
                ],
                "ta": [
                    "உறுப்புகள் 74 மற்றும் 75-ன் கீழ் உண்மை நிர்வாகத் தலைவராகப் (De facto head) பிரதமரின் அரசியலமைப்பு நிலையைத் தெரிந்துகொள்ளுதல்.",
                    "பெயரளவு நிர்வாகியான (De jure) குடியரசுத் தலைவருக்கும் உண்மை நிர்வாகியான (De facto) பிரதமருக்கும் இடையிலான வேறுபாட்டைப் புரிந்துகொள்ளுதல்.",
                    "உறுப்பு 75(1)-ன் கீழ் நியமன நடைமுறை மற்றும் மக்களவை பெரும்பான்மை தலைவரைத் தேர்ந்தெடுக்கும் அரசியலமைப்பு மரபைப் புரிந்துகொள்ளுதல்.",
                    "நாடாளுமன்ற தகுதிகள், இரு அவைகளில் ஏதேனும் ஒன்றில் உறுப்பினராக இருத்தல் (அல்லது உறுப்பு 75(5)-ன் கீழ் 6 மாத அவகாசம் பெற்ற உறுப்பினர் அல்லாதவர்) குறித்த அறிவைப் பெறுதல்.",
                    "உறுப்பு 75(4)-ன் கீழ் குடியரசுத் தலைவரால் செய்து வைக்கப்படும் பதவிப் பிரமாணம் மற்றும் இரகசியக் காப்புப் பிரமாணத்தின் (மூன்றாவது அட்டவணை) தன்மையைப் புரிந்துகொள்ளுதல்.",
                    "பதவிக் காலத்தின் தன்மையைப் புரிந்துகொள்ளுதல் (குடியரசுத் தலைவரின் விருப்பம் என்பது மக்களவை நம்பிக்கையைச் சார்ந்ததே)."
                ]
            },
            "Remember": {
                "en": [
                    "Remember Article 74 (Council of Ministers with PM at head to aid and advise President).",
                    "Remember Article 75 (PM appointed by President; other ministers appointed on PM's advice).",
                    "Remember non-MP can be PM for maximum 6 consecutive months (Art 75(5)).",
                    "Remember PM can be a member of either Lok Sabha or Rajya Sabha.",
                    "Remember PM holds office during the pleasure of President, but 'pleasure' means enjoyment of Lok Sabha majority."
                ],
                "ta": [
                    "உறுப்பு 74 (குடியரசுத் தலைவருக்கு உதவவும் அறிவுரை வழங்கவும் பிரதமரைத் தலைவராகக் கொண்ட அமைச்சரவை) என்பதை நினைவில் கொள்ளுதல்.",
                    "உறுப்பு 75 (பிரதமர் குடியரசுத் தலைவரால் நியமிக்கப்படுகிறார்; பிற அமைச்சர்கள் பிரதமரின் அறிவுரைப்படி நியமிக்கப்படுகிறார்கள்) என்பதை நினைவில் கொள்ளுதல்.",
                    "உறுப்பினர் அல்லாத ஒருவர் அதிகபட்சம் 6 தொடர்ச்சியான மாதங்கள் பிரதமராக இருக்க முடியும் (உறுப்பு 75(5)) என்பதை நினைவில் கொள்ளுதல்.",
                    "பிரதமர் மக்களவை அல்லது மாநிலங்களவை ஆகிய இரண்டில் ஏதேனும் ஒன்றில் உறுப்பினராக இருக்கலாம் என்பதை நினைவில் கொள்ளுதல்.",
                    "பிரதமர் குடியரசுத் தலைவரின் விருப்பம் உள்ளவரை பதவி வகிக்கிறார், ஆனால் 'விருப்பம்' என்பது மக்களவை பெரும்பான்மை ஆதரவையே குறிக்கும் என்பதை நினைவில் கொள்ளுதல்."
                ]
            }
        },
        "subject": "polity",
        "topic": "Prime Minister of India",
        "language": "English + Tamil",
        "ui_type": "standard_notes",
        "sections": [
            {
                "id": "sec_constitutional_position",
                "title_en": "1. Constitutional Position & Executive Role (Articles 74 & 75)",
                "title_ta": "1. அரசியலமைப்பு நிலை & நிர்வாகப் பொறுப்பு (உறுப்புகள் 74 & 75)",
                "type": "standard_topic"
            },
            {
                "id": "sec_nominal_vs_real",
                "title_en": "2. Nominal Executive vs Real Executive & Parliamentary System",
                "title_ta": "2. பெயரளவு நிர்வாகி vs உண்மை நிர்வாகி & நாடாளுமன்ற முறைமை",
                "type": "standard_topic"
            },
            {
                "id": "sec_appointment_process",
                "title_en": "3. Appointment Procedure & Hung House Situations (Article 75(1))",
                "title_ta": "3. நியமன நடைமுறை & தொங்கு மக்களவை நிலைகள் (உறுப்பு 75(1))",
                "type": "standard_topic"
            },
            {
                "id": "sec_qualifications_membership",
                "title_en": "4. Qualifications & Parliamentary Membership Rules (Article 75(5))",
                "title_ta": "4. தகுதிகள் & நாடாளுமன்ற உறுப்பினர் விதிகள் (உறுப்பு 75(5))",
                "type": "standard_topic"
            },
            {
                "id": "sec_oath_and_term",
                "title_en": "5. Oath of Office & Tenure of Prime Minister (Article 75(2) & 75(4))",
                "title_ta": "5. பதவிப் பிரமாணம் & பதவிக் காலம் (உறுப்பு 75(2) & 75(4))",
                "type": "standard_topic"
            },
            {
                "id": "sec_article_map",
                "title_en": "6. Constitutional Articles Map (Articles 74, 75, 77 & 78)",
                "title_ta": "6. அரசியலமைப்பு விதிகள் வரைபடம் (உறுப்புகள் 74, 75, 77 & 78)",
                "type": "standard_topic"
            },
            {
                "id": "comparison_tables",
                "title_en": "7. Mandatory Comparison Tables (Oppositional Analysis)",
                "title_ta": "7. கட்டாய ஒப்பீட்டு அட்டவணைகள் (எதிரெதிர் பகுப்பாய்வு)",
                "type": "comparison"
            },
            {
                "id": "mind_map",
                "title_en": "8. Mind Map & TNPSC Trap Points",
                "title_ta": "8. மன வரைபடம் & TNPSC தேர்வுப் பொறிகள்",
                "type": "mind_map"
            }
        ],
        "content": {
            "definition": {
                "en": "The Prime Minister of India is the real executive authority (de facto executive) of the Republic of India. While the President is the Head of State (de jure executive), the Prime Minister is the Head of Government. Under Article 74(1), the Prime Minister heads the Council of Ministers which aids and advises the President in the exercise of constitutional functions.",
                "ta": "இந்தியப் பிரதமர் இந்தியக் குடியரசின் உண்மையான நிர்வாக அதிகார அமைப்பாவார் (De facto executive). குடியரசுத் தலைவர் நாட்டின் தலைவராக (Head of State / De jure executive) இருக்கும் போது, பிரதமர் அரசாங்கத்தின் தலைவராக (Head of Government) செயல்படுகிறார். உறுப்பு 74(1)-ன் கீழ், அரசியலமைப்புச் செயல்பாடுகளை மேற்கொள்வதில் குடியரசுத் தலைவருக்கு உதவவும் அறிவுரை வழங்கவும் உள்ள அமைச்சரவையின் தலைவராகப் பிரதமர் விளங்குகிறார்."
            },
            "introduction": {
                "en": "In the scheme of parliamentary system of government envisaged by the Constitution of India (modelled on the British Westminster model), executive powers are constitutionally vested in the President (Article 53), but practically exercised by the Prime Minister and the Council of Ministers. Part V Chapter I (The Executive) establishes the Prime Minister as the central pivot around which the entire executive machinery and legislative governance revolve.",
                "ta": "இந்திய அரசியலமைப்பால் முன்மொழியப்பட்ட நாடாளுமன்ற முறைமையில் (பிரிட்டிஷ் வெஸ்ட்மின்ஸ்டர் மாதிரியை அடிப்படையாகக் கொண்டது), நிர்வாக அதிகாரங்கள் அரசியலமைப்புப் படி குடியரசுத் தலைவரிடம் (உறுப்பு 53) ஒப்படைக்கப்பட்டிருந்தாலும், நடைமுறையில் அவை பிரதமர் மற்றும் அமைச்சரவையால் செயல்படுத்தப்படுகின்றன. பகுதி V அத்தியாயம் I (நிர்வாகம்) பிரதமரை முழு நிர்வாக இயந்திரமும் சட்டமியற்றும் ஆட்சியும் சுழலும் மைய அச்சாக நிறுவுகிறது."
            },
            "sec_constitutional_position": [
                {
                    "title": "1. Core Constitutional Position under Articles 74 & 75",
                    "points": {
                        "en": [
                            "Head of Council of Ministers: Article 74(1) explicitly specifies that there shall be a Council of Ministers with the Prime Minister at the head to aid and advise the President.",
                            "Binding Aid & Advice: The advice tendered by the Prime Minister-led Council of Ministers is binding on the President (after 42nd CAA 1976 and 44th CAA 1978).",
                            "Pivot of Government Formation: Under Article 75(1), the President appoints the Prime Minister, and all other Ministers are appointed by the President strictly on the advice of the Prime Minister.",
                            "Keystone of Cabinet Arch: Sir Ivor Jennings called the Prime Minister 'the keystone of the Cabinet arch'. Laski described PM as 'the pivot around which the whole political machinery turns'."
                        ],
                        "ta": [
                            "அமைச்சரவையின் தலைவர்: உறுப்பு 74(1) குடியரசுத் தலைவருக்கு உதவவும் அறிவுரை வழங்கவும் பிரதமரைத் தலைவராகக் கொண்ட ஓர் அமைச்சரவை இருக்க வேண்டும் என்று தெளிவாகக் குறிப்பிடுகிறது.",
                            "கட்டுப்படுத்தும் அறிவுரை: பிரதமரின் தலைமையிலான அமைச்சரவை வழங்கும் அறிவுரை குடியரசுத் தலைவரைக் கட்டுப்படுத்தும் (42வது திருத்தம் 1976 & 44வது திருத்தம் 1978க்குப் பிறகு).",
                            "அரசாங்க அமைப்பின் மைய அச்சு: உறுப்பு 75(1)-ன் கீழ், குடியரசுத் தலைவர் பிரதமரை நியமிக்கிறார், மேலும் அனைத்து பிற அமைச்சர்களும் பிரதமரின் அறிவுரையின் பேரில் மட்டுமே குடியரசுத் தலைவரால் நியமிக்கப்படுகிறார்கள்.",
                            "அமைச்சரவை வளைவின் முதன்மைக் கல்: சர் ஐவர் ஜென்னிங்ஸ் பிரதமரை 'அமைச்சரவை வளைவின் முதன்மைக் கல்' (Keystone of Cabinet arch) என்று அழைத்தார். லஸ்கி பிரதமரை 'அரசியல் இயந்திரம் சுழலும் மைய அச்சு' என்று விவரித்தார்."
                        ]
                    }
                },
                {
                    "title": "2. Position in the Union Executive",
                    "points": {
                        "en": [
                            "Union Executive Composition: Part V Chapter I (Articles 52 to 78) defines Union Executive comprising President, Vice-President, Prime Minister, Council of Ministers, and Attorney General of India.",
                            "Leader of the House & Nation: Prime Minister acts as the leader of the majority party in Lok Sabha, leader of the Union Government, and chief spokesman of national policy.",
                            "Link between President & Cabinet: Article 78 makes it the constitutional duty of the Prime Minister to communicate all decisions of the Council of Ministers to the President."
                        ],
                        "ta": [
                            "ஒன்றிய நிர்வாகத்தின் அமைப்பு: பகுதி V அத்தியாயம் I (உறுப்புகள் 52 முதல் 78 வரை) குடியரசுத் தலைவர், துணைக் குடியரசுத் தலைவர், பிரதமர், அமைச்சரவை மற்றும் தலைமை வழக்கறிஞர் (Attorney General) ஆகியோரைக் கொண்ட ஒன்றிய நிர்வாகத்தை வரையறுக்கிறது.",
                            "அவையின் தலைவரும் நாட்டின் தலைவரும்: பிரதமர் மக்களவையின் பெரும்பான்மைக் கட்சியின் தலைவராகவும், ஒன்றிய அரசாங்கத்தின் தலைவராகவும், தேசியக் கொள்கையின் முதன்மை प्रवக்தாவாகவும் (spokesman) செயல்படுகிறார்.",
                            "குடியரசுத் தலைவர் & அமைச்சரவை இடையிலான இணைப்பு: உறுப்பு 78 அமைச்சரவையின் அனைத்து முடிவுகளையும் குடியரசுத் தலைவருக்குத் தெரிவிப்பதை பிரதமரின் அரசியலமைப்பு கடமையாக்குகிறது."
                        ]
                    }
                }
            ],
            "sec_nominal_vs_real": [
                {
                    "title": "1. Nominal (De Jure) vs Real (De Facto) Executive Dichotomy",
                    "points": {
                        "en": [
                            "De Jure Head (President): Constitutional head of state. All executive actions of the Union Government are formally taken in the President's name (Article 77(1)).",
                            "De Facto Head (Prime Minister): Real executive head of government. Actual administrative discretion, policy formation, and cabinet control reside with the Prime Minister.",
                            "Lord Morley's Description: Described the Prime Minister as 'primus inter pares' (first among equals). However, Sir William Harcourt noted PM is 'inter stellas luna minor' (a moon among lesser stars)."
                        ],
                        "ta": [
                            "சட்டப்படியான (De Jure) vs செயல்முறையிலான (De Facto) நிர்வாக வேறுபாடு: குடியரசுத் தலைவர் சட்டப்படியான (De jure) நாட்டின் தலைவர்; ஒன்றிய அரசின் அனைத்து நிர்வாக நடவடிக்கைகளும் குடியரசுத் தலைவரின் பெயரிலேயே மேற்கொள்ளப்படுகின்றன (உறுப்பு 77(1)).",
                            "செயல்முறைத் தலைவர் (பிரதமர்): பிரதமர் அரசாங்கத்தின் உண்மையான (De facto) நிர்வாகத் தலைவர். நடைமுறை நிர்வாக விவேகம், கொள்கை உருவாக்கம் மற்றும் அமைச்சரவைக் கட்டுப்பாடு ஆகியவை பிரதமரிடமே உள்ளன.",
                            "லார்ட் மார்லியின் விளக்கம்: பிரதமரை 'சமமானவர்களில் முதன்மையானவர்' (Primus inter pares) என விவரித்தார். இருப்பினும், சர் வில்லியம் ஹார்கோர்ட் 'சிறிய நட்சத்திரங்களுக்கு மத்தியில் ஒளிரும் நிலவு' (Inter stellas luna minor) எனக் குறிப்பிட்டடைத்தார்."
                        ]
                    }
                },
                {
                    "title": "2. Parliamentary System & Government Formation",
                    "points": {
                        "en": [
                            "Westminster Model Core Principle: The executive is drawn from the legislature and remains collectively responsible to the House of the People (Lok Sabha) under Article 75(3).",
                            "Government Formation Role: The President does not select ministers independently; the Prime Minister selects members, allocates portfolios, and recommends their appointment."
                        ],
                        "ta": [
                            "வெஸ்ட்மின்ஸ்டர் மாதிரியின் முதன்மைக் கோட்பாடு: நிர்வாகத்துறை சட்டமன்றத்திலிருந்து தேர்ந்தெடுக்கப்பட்டு, உறுப்பு 75(3)-ன் கீழ் மக்களவைக்குக் கூட்டாகப் பொறுப்புடையதாக இருக்கும்.",
                            "அரசாங்க உருவாக்கப் பொறுப்பு: குடியரசுத் தலைவர் சுதந்திரமாக அமைச்சர்களைத் தேர்ந்தெடுப்பதில்லை; பிரதமரே உறுப்பினர்களைத் தேர்ந்தெடுத்து, துறைகளை ஒதுக்கி, அவர்களது நியமனத்தைப் பரிந்துரைக்கிறார்."
                        ]
                    }
                }
            ],
            "sec_appointment_process": [
                {
                    "title": "1. Article 75(1) Appointment & Conventions",
                    "points": {
                        "en": [
                            "Constitutional Provision: Article 75(1) states simply that 'The Prime Minister shall be appointed by the President'. The Constitution provides no specific procedure for PM selection.",
                            "Dominant Political Convention: In accordance with parliamentary conventions, the President MUST appoint the leader of the majority party in the Lok Sabha as Prime Minister.",
                            "Discretionary Powers: President gets personal/situational discretion to select PM ONLY when no single party secures a clear majority in Lok Sabha (Hung House) or upon sudden death of an incumbent PM without an obvious successor."
                        ],
                        "ta": [
                            "உறுப்பு 75(1) நியமனம் & மரபுகள்: உறுப்பு 75(1) 'பிரதமர் குடியரசுத் தலைவரால் நியமிக்கப்படுவார்' என்று மட்டுமே சுருக்கமாகக் கூறுகிறது. பிரதமர் தேர்வுக்கு அரசியலமைப்பு குறிப்பிட்ட எந்த நடைமுறையையும் வழங்கவில்லை.",
                            "முக்கிய அரசியல் மரபு: நாடாளுமன்ற மரபுகளின்படி, மக்களவையில் பெரும்பான்மை பெற்ற கட்சியின் தலைவரைக் குடியரசுத் தலைவர் பிரதமராக நியமிக்க வேண்டும்.",
                            "விருப்ப அதிகாரம்: மக்களவையில் எந்தவொரு கட்சிக்கும் தெளிவான பெரும்பான்மை கிடைக்காத போது (தொங்கு மக்களவை) அல்லது பதவியில் இருக்கும் பிரதமர் திடீரென இறந்து வாரிசு இல்லாத போது மட்டுமே குடியரசுத் தலைவருக்குச் சூழ்நிலை சார்ந்த தனிப்பட்ட விருப்ப அதிகாரம் கிடைக்கிறது."
                        ]
                    }
                },
                {
                    "title": "2. Hung House & Presidential Situational Discretion",
                    "points": {
                        "en": [
                            "Hung House Convention: When no party gets majority, President appoints the leader of the largest party or coalition in Lok Sabha as PM and asks him to seek a vote of confidence within one month.",
                            "Historical Precedents: Neelam Sanjiva Reddy appointed Charan Singh in 1979 after Morarji Desai's fall; R. Venkataraman appointed V.P. Singh in 1989; Shankar Dayal Sharma appointed A.B. Vajpayee in 1996.",
                            "Court Ruling on Appointment First: In 1997, Supreme Court (Delhi HC in Akaash Saxena / Deve Gowda precedent context) affirmed that a person can be appointed as PM first and asked to prove majority on floor of Lok Sabha later."
                        ],
                        "ta": [
                            "தொங்கு மக்களவை மரபு: எந்தக் கட்சிக்கும் பெரும்பான்மை இல்லாத போது, குடியரசுத் தலைவர் மக்களவையின் மிகப்பெரிய கட்சி அல்லது கூட்டணியின் தலைவரைப் பிரதமராக நியமித்து, ஒரு மாதத்திற்குள் நம்பிக்க வாக்கெடுப்பு கோருமாறு பணிக்கிறார்.",
                            "வரலாற்று உதாரணங்கள்: 1979-ல் மொரார்ஜி தேசாயின் வீழ்ச்சிக்குப் பின் நீலம் சஞ்சீவ ரெட்டி சரண் சிங்கை நியமித்தார்; 1989-ல் ஆர். வெங்கடராமன் வி.பி. சிங்கை நியமித்தார்; 1996-ல் சங்கர் தயாள் சர்மா ஏ.பி. வஜ்பாயியை நியமித்தார்.",
                            "நியமனம் முதலில் என்ற நீதிமன்றத் தீர்ப்பு: 1997-ல் உச்ச நீதிமன்றம் ஒருவரை முதலில் பிரதமராக நியமித்து, பின்னர் மக்களவையில் பெரும்பான்மையை நிரூபிக்க உத்தரவிடலாம் என்பதை உறுதிப்படுத்தியது."
                        ]
                    }
                }
            ],
            "sec_qualifications_membership": [
                {
                    "title": "1. Parliamentary Membership Requirement (Article 75(5))",
                    "points": {
                        "en": [
                            "Membership of Either House: Prime Minister can be a member of EITHER Lok Sabha or Rajya Sabha.",
                            "Non-MP Appointment Rule: A person who is NOT a member of either House of Parliament can be appointed as Prime Minister, but MUST become a member of either House within 6 consecutive months (Article 75(5)).",
                            "Consequence of Failure: If he fails to secure a seat in either House within 6 months, he ceases to be Prime Minister.",
                            "Age Qualification: Minimum 25 years if member of Lok Sabha; Minimum 30 years if member of Rajya Sabha."
                        ],
                        "ta": [
                            "இரு அவைகளில் ஏதேனும் ஒன்றில் உறுப்பினர்: பிரதமர் மக்களவை அல்லது மாநிலங்களவை ஆகிய இரண்டில் ஏதேனும் ஒன்றில் உறுப்பினராக இருக்கலாம்.",
                            "உறுப்பினர் அல்லாதவர் நியமன விதி: நாடாளுமன்றத்தின் எந்த அவையிலும் உறுப்பினர் இல்லாத ஒருவரைப் பிரதமராக நியமிக்க முடியும், ஆனால் அவர் 6 தொடர்ச்சியான மாதங்களுக்குள் ஏதேனும் ஒரு அவையில் உறுப்பினராக வேண்டும் (உறுப்பு 75(5)).",
                            "தோல்வியின் விளைவு: 6 மாதங்களுக்குள் இரு அவைகளில் ஒன்றில் இடம் பெறத் தவறினால், அவர் பிரதமர் பதவியை இழப்பார்.",
                            "வயதுத் தகுதி: மக்களவை உறுப்பினராக இருந்தால் குறைந்தபட்சம் 25 வயது; மாநிலங்களவை உறுப்பினராக இருந்தால் குறைந்தபட்சம் 30 வயது."
                        ]
                    }
                },
                {
                    "title": "2. Prominent Rajya Sabha Prime Ministers",
                    "points": {
                        "en": [
                            "Indira Gandhi (1966): First Prime Minister appointed from Rajya Sabha.",
                            "H.D. Deve Gowda (1996): Member of Rajya Sabha when appointed PM.",
                            "I.K. Gujral (1997): Member of Rajya Sabha when appointed PM.",
                            "Dr. Manmohan Singh (2004 & 2009): Served two full terms as Prime Minister while being a Rajya Sabha member (Assam seat)."
                        ],
                        "ta": [
                            "இந்திரா காந்தி (1966): மாநிலங்களவையிலிருந்து பிரதமராக நியமிக்கப்பட்ட முதல் நபர்.",
                            "எச்.டி. தேவ கௌடா (1996): பிரதமராக நியமிக்கப்பட்ட போது மாநிலங்களவை உறுப்பினர்.",
                            "ஐ.கே. குஜ்ரால் (1997): பிரதமராக நியமிக்கப்பட்ட போது மாநிலங்களவை உறுப்பினர்.",
                            "டாக்டர் மன்மோகன் சிங் (2004 & 2009): மாநிலங்களவை உறுப்பினராக (அஸ்ஸாம் தொகுதி) இருந்துகொண்டே இரு முழு பதவிக் காலங்கள் பிரதமராகப் பணியாற்றினார்."
                        ]
                    }
                }
            ],
            "sec_oath_and_term": [
                {
                    "title": "1. Oath of Office & Secrecy (Article 75(4))",
                    "points": {
                        "en": [
                            "Oath Administration: Before entering office, the President administers the Oath of Office and Oath of Secrecy to the Prime Minister (Article 75(4)).",
                            "Third Schedule: The texts of both oaths are prescribed in the Third Schedule of the Constitution of India.",
                            "Oath of Secrecy: Unique requirement for Ministers that they will not directly or indirectly communicate or reveal any matter brought under consideration except as required for discharge of duties."
                        ],
                        "ta": [
                            "பதவிப் பிரமாண நிர்வாகம்: பதவியேற்பதற்கு முன், குடியரசுத் தலைவர் பிரதமருக்குப் பதவிப் பிரமாணமும் இரகசியக் காப்புப் பிரமாணமும் செய்து வைக்கிறார் (உறுப்பு 75(4)).",
                            "மூன்றாவது அட்டவணை: இரு பிரமாணங்களின் உரைகளும் இந்திய அரசியலமைப்பின் மூன்றாவது அட்டவணையில் குறிப்பிடப்பட்டுள்ளன.",
                            "இரகசியக் காப்புப் பிரமாணம்: அமைச்சர்களுக்கான தனித்துவமான தேவை என்னவெனில், கடமைகளை நிறைவேற்றுவதற்குத் தேவையானதைத் தவிர, பரிசீலனைக்குக் கொண்டு வரப்படும் எந்தவொரு விஷயத்தையும் நேரடியாகவோ மறைமுகமாகவோ தெரிவிக்கவோ வெளிப்படுத்தவோ மாட்டார்கள் என்பதாகும்."
                        ]
                    }
                },
                {
                    "title": "2. Term of Office & Resignation Dynamics (Article 75(2))",
                    "points": {
                        "en": [
                            "No Fixed Independent Tenure: The Constitution specifies that the Prime Minister holds office 'during the pleasure of the President' (Article 75(2)).",
                            "Meaning of Pleasure: The President CANNOT dismiss the PM as long as he enjoys majority support in Lok Sabha.",
                            "Loss of Majority: If PM loses Lok Sabha confidence (defeated in No-Confidence Motion or Money Bill), he must resign. If he does not resign, President can dismiss him.",
                            "Impact of Resignation/Death: The resignation or death of the Prime Minister automatically dissolves the entire Council of Ministers (vacates all ministerial offices)."
                        ],
                        "ta": [
                            "நிலையான சுதந்திரக் காலம் இல்லை: பிரதமர் 'குடியரசுத் தலைவரின் விருப்பம் உள்ளவரை' பதவி வகிப்பார் என அரசியலமைப்பு குறிப்பிடுகிறது (உறுப்பு 75(2)).",
                            "விருப்பத்தின் பொருள்: மக்களவையில் பெரும்பான்மை ஆதரவு இருக்கும் வரை குடியரசுத் தலைவரால் பிரதமரைப் பதவி நீக்கம் செய்ய முடியாது.",
                            "பெரும்பான்மை இழப்பு: பிரதமர் மக்களவை நம்பிக்கையை இழந்தால் (நம்பிக்கையில்லாத் தீர்மானம் அல்லது பண மசோதாவில் தோல்வியடைந்தால்), அவர் ராஜினாமா செய்ய வேண்டும். ராஜினாமா செய்யாவிட்டால், குடியரசுத் தலைவர் அவரைப் பதவி நீக்கம் செய்யலாம்.",
                            "ராஜினாமா / இறப்பின் தாக்கம்: பிரதமரின் ராஜினாமா அல்லது இறப்பு தானாகவே முழு அமைச்சரவையையும் கலைத்துவிடும் (அனைத்து அமைச்சர் பதவிகளும் காலியாகும்)."
                        ]
                    }
                }
            ],
            "sec_article_map": [
                {
                    "title": "1. Articles 74, 75, 77 and 78 Core Summary",
                    "points": {
                        "en": [
                            "Article 74: Council of Ministers with Prime Minister as Head to aid and advise the President of India.",
                            "Article 75: Other provisions as to Ministers — Appointment of PM & Ministers, tenure (pleasure), collective responsibility to Lok Sabha, oath, 6-month non-MP rule, salaries.",
                            "Article 77: Conduct of business of the Government of India — All executive actions in President's name; Allocation of business rules made by President on PM advice.",
                            "Article 78: Duties of Prime Minister as respects furnishing of information to President regarding administration and legislation."
                        ],
                        "ta": [
                            "உறுப்பு 74: இந்தியக் குடியரசுத் தலைவருக்கு உதவவும் அறிவுரை வழங்கவும் பிரதமரைத் தலைவராகக் கொண்ட அமைச்சரவை.",
                            "உறுப்பு 75: அமைச்சர்கள் பற்றிய பிற விதிகள் — பிரதமர் & அமைச்சர்கள் நியமனம், பதவிக் காலம் (விருப்பம்), மக்களவைக்குக் கூட்டுப் பொறுப்பு, பதவிப் பிரமாணம், 6 மாத உறுப்பினர் அல்லாதவர் விதி, ஊதியங்கள்.",
                            "உறுப்பு 77: இந்திய அரசின் ஆட்சிப் பணிகள் நிர்வாகம் — அனைத்து நிர்வாக நடவடிக்கைகளும் குடியரசுத் தலைவர் பெயரால்; வணிகப் பகிர்வு விதிகளைப் பிரதமர் அறிவுரைப்படி குடியரசுத் தலைவர் உருவாக்குதல்.",
                            "உறுப்பு 78: நிர்வாகம் மற்றும் சட்டவாக்கம் குறித்து குடியரசுத் தலைவருக்குத் தகவல்களைத் தெரிவிப்பதில் பிரதமரின் கடமைகள்."
                        ]
                    }
                }
            ],
            "comparison_tables": [
                {
                    "id": "comp_pres_vs_pm",
                    "title_en": "1. President of India vs Prime Minister of India",
                    "title_ta": "1. இந்தியக் குடியரசுத் தலைவர் vs இந்தியப் பிரதமர்",
                    "headers_en": ["Feature", "President of India", "Prime Minister of India"],
                    "headers_ta": ["அம்சம்", "இந்தியக் குடியரசுத் தலைவர்", "இந்தியப் பிரதமர்"],
                    "rows_en": [
                        ["Executive Status", "Nominal / Constitutional Executive (De Jure)", "Real Executive Authority (De Facto)"],
                        ["Role in State/Govt", "Head of the State (Rank 1 in Precedence)", "Head of the Government (Rank 3 in Precedence)"],
                        ["Constitutional Basis", "Article 52 & Article 53", "Article 74 & Article 75"],
                        ["Selection / Election", "Elected indirectly by Electoral College (MPs + MLAs)", "Appointed by President (Majority leader in Lok Sabha)"],
                        ["Cabinet Relationship", "Acts on aid and advice of PM-led Cabinet (Art 74)", "Heads the Cabinet & Council of Ministers"],
                        ["Dissolution of LS", "Dissolves Lok Sabha on advice of PM (Art 85)", "Advises President to dissolve Lok Sabha"]
                    ],
                    "rows_ta": [
                        ["நிர்வாக நிலை", "பெயரளவு / அரசியலமைப்பு நிர்வாகி (De Jure)", "உண்மையான நிர்வாக அதிகாரம் (De Facto)"],
                        ["நாடு / அரசின் பங்கு", "நாட்டின் தலைவர் (முன்னுரிமை வரிசையில் 1ம் இடம்)", "அரசாங்கத்தின் தலைவர் (முன்னுரிமை வரிசையில் 3ம் இடம்)"],
                        ["அரசியலமைப்பு அடிப்படை", "உறுப்பு 52 & உறுப்பு 53", "உறுப்பு 74 & உறுப்பு 75"],
                        ["தேர்வு / தேர்தல்", "வாக்காளர் குழுவால் மறைமுகமாகத் தேர்வு (MPs + MLAs)", "குடியரசுத் தலைவரால் நியமனம் (மக்களவை பெரும்பான்மைத் தலைவர்)"],
                        ["அமைச்சரவை தொடர்பு", "பிரதமர் தலைமையிலான அமைச்சரவையின் அறிவுரைப்படி செயல்", "அமைச்சரவை மற்றும் அமைச்சர்கள் குழுவின் தலைவர்"],
                        ["மக்களவைக் கலைப்பு", "பிரதமரின் அறிவுரைப்படி மக்களவையைக் கலைக்கிறார்", "மக்களவையைக் கலைக்கக் குடியரசுத் தலைவருக்கு அறிவுறுத்துகிறார்"]
                    ]
                },
                {
                    "id": "comp_pm_vs_com",
                    "title_en": "2. Prime Minister vs Council of Ministers",
                    "title_ta": "2. பிரதமர் vs அமைச்சரவை (Council of Ministers)",
                    "headers_en": ["Feature", "Prime Minister", "Council of Ministers"],
                    "headers_ta": ["அம்சம்", "இந்தியப் பிரதமர்", "அமைச்சரவை (Council of Ministers)"],
                    "rows_en": [
                        ["Constitutional Status", "Head and Leader of Council of Ministers (Art 74)", "Body of Ministers aiding President (Art 74)"],
                        ["Appointment Order", "Appointed first by President (Art 75(1))", "Appointed later on PM's recommendation"],
                        ["Leadership Dynamics", "Keystone of Cabinet Arch; guides and directs", "Functions under PM's direct leadership"],
                        ["Impact of Vacancy", "PM's death/resignation collapses entire Council", "Minister's death/resignation creates single vacancy"],
                        ["Portfolio Authority", "Allocates and reshuffles portfolios at will", "Receives portfolio allocated by Prime Minister"]
                    ],
                    "rows_ta": [
                        ["அரசியலமைப்பு நிலை", "அமைச்சரவையின் தலைவர் மற்றும் வழிநடத்துனர் (உறுப்பு 74)", "குடியரசுத் தலைவருக்கு உதவும் அமைச்சர்களின் குழு (உறுப்பு 74)"],
                        ["நியமன வரிசை", "முதலில் குடியரசுத் தலைவரால் நியமிக்கப்படுகிறார்", "பிரதமரின் பரிந்துரையின் பேரில் பின்னர் நியமிக்கப்படுகின்றனர்"],
                        ["தலைமை இயக்கம்", "அமைச்சரவை வளைவின் முதன்மைக் கல்; வழிகாட்டுகிறார்", "பிரதமரின் நேரடித் தலைமையின் கீழ் செயல்படுகிறது"],
                        ["காலியிடத் தாக்கம்", "பிரதமரின் இறப்பு/ராஜினாமா முழு குழுவையும் கலைக்கும்", "அமைச்சரின் இறப்பு/ராஜினாமா ஒரு காலியிடத்தை மட்டுமே உருவாக்கும்"],
                        ["துறை ஒதுக்கீடு அதிகாரம்", "விருப்பப்படி துறைகளை ஒதுக்குகிறார் & மாற்றுகிறார்", "பிரதமரால் ஒதுக்கப்பட்ட துறையைப் பெறுகின்றனர்"]
                    ]
                },
                {
                    "id": "comp_majority_leader_vs_pm",
                    "title_en": "3. Lok Sabha Majority Leader vs Prime Minister",
                    "title_ta": "3. மக்களவை பெரும்பான்மைத் தலைவர் vs இந்தியப் பிரதமர்",
                    "headers_en": ["Dimension", "Lok Sabha Majority Leader (Party Role)", "Prime Minister of India (Constitutional Post)"],
                    "headers_ta": ["பரிமாணம்", "மக்களவை பெரும்பான்மைத் தலைவர் (கட்சிப் பொறுப்பு)", "இந்தியப் பிரதமர் (அரசியலமைப்புப் பதவி)"],
                    "rows_en": [
                        ["Nature of Authority", "Political convention and parliamentary party leader", "Constitutional head of Union Executive under Art 74"],
                        ["Scope of Function", "Manages majority party discipline and confidence", "Directs national executive, foreign policy & administration"],
                        ["Appointment Base", "Elected by elected MPs of majority political party", "Formally appointed by President under Article 75(1)"],
                        ["House Membership", "Must strictly be a member of Lok Sabha", "Can be member of Lok Sabha, Rajya Sabha or non-MP (6 months)"]
                    ],
                    "rows_ta": [
                        ["அதிகாரத்தின் தன்மை", "அரசியல் மரபு மற்றும் நாடாளுமன்றக் கட்சித் தலைவர்", "உறுப்பு 74-ன் கீழ் ஒன்றிய நிர்வாகத்தின் அரசியலமைப்புத் தலைவர்"],
                        ["செயல்பாட்டு எல்லை", "பெரும்பான்மைக் கட்சியின் ஒழுக்கம் மற்றும் நம்பிக்கையைக் நிர்வகிக்கிறார்", "தேசிய நிர்வாகம், வெளியுறவுக் கொள்கை & ஆட்சியை வழிகாட்டுகிறார்"],
                        ["நியமன அடிப்படை", "பெரும்பான்மை அரசியல் கட்சியின் எம்பிக்களால் தேர்வு", "உறுப்பு 75(1)-ன் கீழ் குடியரசுத் தலைவரால் முறைப்படி நியமனம்"],
                        ["அவை உறுப்பினர் தகுதி", "கட்டாயமாக மக்களவை உறுப்பினராக இருக்க வேண்டும்", "மக்களவை, மாநிலங்களவை அல்லது உறுப்பினர் அல்லாதவராக (6 மாதம்) இருக்கலாம்"]
                    ]
                },
                {
                    "id": "comp_nominal_vs_real",
                    "title_en": "4. Nominal Executive vs Real Executive",
                    "title_ta": "4. பெயரளவு நிர்வாகி vs உண்மை நிர்வாகி",
                    "headers_en": ["Criteria", "Nominal Executive (President)", "Real Executive (Prime Minister)"],
                    "headers_ta": ["அளவுகோல்", "பெயரளவு நிர்வாகி (குடியரசுத் தலைவர்)", "உண்மை நிர்வாகி (பிரதமர்)"],
                    "rows_en": [
                        ["Latin Terminology", "De Jure Executive (By Right / Law)", "De Facto Executive (In Fact / Practice)"],
                        ["Constitutional Headship", "Head of the State of India", "Head of the Government of India"],
                        ["Discretionary Power", "Constitutional discretion is severely restricted", "Exercises wide administrative and political discretion"],
                        ["Accountability", "Not answerable to Parliament directly for policy", "Directly accountable to Lok Sabha via collective responsibility"]
                    ],
                    "rows_ta": [
                        ["லத்தீன் கலைச்சொல்", "De Jure Executive (சட்டப்படி நியாயமான)", "De Facto Executive (நடைமுறையில் உண்மையான)"],
                        ["அரசியலமைப்புத் தலைமை", "இந்திய நாட்டின் தலைவர்", "இந்திய அரசாங்கத்தின் தலைவர்"],
                        ["விவேக அதிகாரம்", "அரசியலமைப்பு விவேகம் மிகவும் வரம்பிற்குட்பட்டது", "பரந்த நிர்வாக மற்றும் அரசியல் விவேகத்தைப் செயல்படுத்துகிறார்"],
                        ["பொறுப்புக்கூறல்", "கொள்கைகளுக்காக நாடாளுமன்றத்திற்கு நேரடியாகப் பொறுப்பல்ல", "கூட்டுப் பொறுப்பு மூலம் மக்களவைக்கு நேரடியாகப் பொறுப்புடையவர்"]
                    ]
                },
                {
                    "id": "comp_pm_vs_cm",
                    "title_en": "5. Prime Minister vs Chief Minister",
                    "title_ta": "5. பிரதமர் vs முதலமைச்சர்",
                    "headers_en": ["Aspect", "Prime Minister of India", "Chief Minister of a State"],
                    "headers_ta": ["அம்சம்", "இந்தியப் பிரதமர்", "மாநில முதலமைச்சர்"],
                    "rows_en": [
                        ["Jurisdiction", "Union level (Whole of India) under Part V", "State level (Respective State) under Part VI"],
                        ["Constitutional Provision", "Article 74 & Article 75", "Article 163 & Article 164"],
                        ["Appointing Authority", "Appointed by President of India", "Appointed by Governor of the State"],
                        ["Executive Leadership", "Head of Union Council of Ministers", "Head of State Council of Ministers"],
                        ["House Membership", "Member of Lok Sabha or Rajya Sabha", "Member of Legislative Assembly or Council"]
                    ],
                    "rows_ta": [
                        ["அதிகார எல்லை", "ஒன்றிய நிலை (இந்தியா முழுவதும்) பகுதி V", "மாநில நிலை (குறிப்பிட்ட மாநிலம்) பகுதி VI"],
                        ["அரசியலமைப்பு விதி", "உறுப்பு 74 & உறுப்பு 75", "உறுப்பு 163 & உறுப்பு 164"],
                        ["நியமன அதிகாரம்", "இந்தியக் குடியரசுத் தலைவரால் நியமிக்கப்படுகிறார்", "மாநில ஆளுநரால் நியமிக்கப்படுகிறார்"],
                        ["நிர்வாகத் தலைமை", "ஒன்றிய அமைச்சரவையின் தலைவர்", "மாநில அமைச்சரவையின் தலைவர்"],
                        ["அவை உறுப்பினர் தகுதி", "மக்களவை அல்லது மாநிலங்களவை உறுப்பினர்", "சட்டமன்றப் பேரவை அல்லது மேலவை உறுப்பினர்"]
                    ]
                }
            ],
            "mind_map": [
                {
                    "title": "Prime Minister of India (Part V - Articles 74, 75, 77, 78)",
                    "short_label": "Prime Minister Part 1",
                    "children": [
                        {
                            "title": "1. Constitutional Position",
                            "short_label": "Position",
                            "children": [
                                {
                                    "title": "Article 74: Head of Council of Ministers aiding President",
                                    "short_label": "Art 74 Aid & Advice"
                                },
                                {
                                    "title": "Real Executive Authority (De Facto Head of Govt)",
                                    "short_label": "De Facto Head"
                                }
                            ]
                        },
                        {
                            "title": "2. Appointment & Tenure",
                            "short_label": "Appointment",
                            "children": [
                                {
                                    "title": "Article 75(1): Appointed by President (Majority leader convention)",
                                    "short_label": "Art 75(1) Appt"
                                },
                                {
                                    "title": "Hung House: President's situational discretion (1 month floor test)",
                                    "short_label": "Hung House"
                                }
                            ]
                        },
                        {
                            "title": "3. Qualifications & Membership",
                            "short_label": "Qualifications",
                            "children": [
                                {
                                    "title": "Either House MP (LS: min 25 yrs; RS: min 30 yrs)",
                                    "short_label": "LS / RS MP"
                                },
                                {
                                    "title": "Article 75(5): Non-MP can be PM for max 6 months",
                                    "short_label": "6-Month Rule"
                                }
                            ]
                        },
                        {
                            "title": "4. Oath & Term",
                            "short_label": "Oath & Term",
                            "children": [
                                {
                                    "title": "Article 75(4): Oath of Office & Secrecy by President",
                                    "short_label": "Art 75(4) Oath"
                                },
                                {
                                    "title": "Article 75(2): Pleasure of President (LS Majority Confidence)",
                                    "short_label": "Pleasure Term"
                                }
                            ]
                        }
                    ]
                }
            ],
            "tnpsc_traps": [
                {
                    "title": "1. Nominal vs Real Executive Trap (பெயரளவு vs உண்மை நிர்வாகப் பொறி)",
                    "points": {
                        "en": [
                            "TRAP: Believing President has real independent executive power in day-to-day administration.",
                            "FACT: President is Nominal (De Jure) Executive. Real (De Facto) Executive power is vested in the Prime Minister and Council of Ministers!"
                        ],
                        "ta": [
                            "பொறி: அன்றாட நிர்வாகத்தில் குடியரசுத் தலைவருக்குத் தனிப்பட்ட சுதந்திரமான நிர்வாக அதிகாரம் உண்டு என நம்புவது.",
                            "உண்மை: குடியரசுத் தலைவர் பெயரளவு (De Jure) நிர்வாகி. உண்மையான (De Facto) நிர்வாக அதிகாரம் பிரதமர் மற்றும் அமைச்சரவையிடமே உள்ளது!"
                        ]
                    }
                },
                {
                    "title": "2. Constitutional Rule vs Political Convention Trap (அரசியலமைப்பு விதி vs அரசியல் மரபுப் பொறி)",
                    "points": {
                        "en": [
                            "TRAP: Assuming Constitution explicitly mandates appointing the Lok Sabha majority leader as PM.",
                            "FACT: Article 75(1) ONLY states 'The Prime Minister shall be appointed by the President'. Appointing majority leader is a political CONVENTION, not explicit constitutional text!"
                        ],
                        "ta": [
                            "பொறி: மக்களவை பெரும்பான்மை தலைவரைத் தான் பிரதமராக நியமிக்க வேண்டும் என்று அரசியலமைப்பு தெளிவாகக் குறிப்பிடுகிறது என நினைப்பது.",
                            "உண்மை: உறுப்பு 75(1) 'பிரதமர் குடியரசுத் தலைவரால் நியமிக்கப்படுவார்' என்று மட்டுமே கூறுகிறது. பெரும்பான்மை தலைவரை நியமிப்பது அரசியல் மரபு (Convention), எழுத்துப்பூர்வ அரசியலமைப்பு விதியல்ல!"
                        ]
                    }
                },
                {
                    "title": "3. House Membership Rule Trap (அவை உறுப்பினர் தகுதிப் பொறி)",
                    "points": {
                        "en": [
                            "TRAP: Believing Prime Minister MUST strictly be a member of Lok Sabha at the time of appointment.",
                            "FACT: PM can be from Lok Sabha OR Rajya Sabha, OR even a Non-MP at appointment (provided membership is obtained within 6 months under Art 75(5))!"
                        ],
                        "ta": [
                            "பொறி: நியமனத்தின் போது பிரதமர் கட்டாயமாக மக்களவை உறுப்பினராக மட்டுமே இருக்க வேண்டும் என நம்புவது.",
                            "உண்மை: பிரதமர் மக்களவை அல்லது மாநிலங்களவை உறுப்பினராக இருக்கலாம், அல்லது உறுப்பினர் அல்லாதவராகவும் இருக்கலாம் (உறுப்பு 75(5)-ன் கீழ் 6 மாதங்களுக்குள் உறுப்பினராக வேண்டும்)!"
                        ]
                    }
                },
                {
                    "title": "4. Minimum Age Qualification Trap (குறைந்தபட்ச வயதுத் தகுதிப் பொறி)",
                    "points": {
                        "en": [
                            "TRAP: Stating fixed minimum age for Prime Minister is always 35 years.",
                            "FACT: Minimum age is 25 years if PM is from Lok Sabha, and 30 years if PM is from Rajya Sabha!"
                        ],
                        "ta": [
                            "பொறி: பிரதமருக்கான குறைந்தபட்ச வயது எப்போதும் 35 ஆண்டுகள் எனத் தவறாகக் குறிப்பிடுவது.",
                            "உண்மை: பிரதமர் மக்களவையிலிருந்து தேர்ந்தெடுக்கப்பட்டால் குறைந்தபட்ச வயது 25; மாநிலங்களவையிலிருந்து தேர்ந்தெடுக்கப்பட்டால் 30 ஆண்டுகள் ஆகும்!"
                        ]
                    }
                },
                {
                    "title": "5. Pleasure of President Scope Trap (குடியரசுத் தலைவர் விருப்பப் பொறி)",
                    "points": {
                        "en": [
                            "TRAP: Believing President can dismiss PM at any time at his personal discretion under Art 75(2).",
                            "FACT: 'Pleasure of President' is tied to Lok Sabha majority. President CANNOT dismiss PM as long as PM enjoys Lok Sabha confidence!"
                        ],
                        "ta": [
                            "பொறி: உறுப்பு 75(2)-ன் கீழ் குடியரசுத் தலைவர் தனது தனிப்பட்ட விருப்பப்படி எப்போது வேண்டுமானாலும் பிரதமரைக் கலைக்கலாம் எனக் கருதுவது.",
                            "உண்மை: 'குடியரசுத் தலைவரின் விருப்பம்' என்பது மக்களவை பெரும்பான்மையைச் சார்ந்ததாகும். மக்களவை நம்பிக்கை இருக்கும் வரை குடியரசுத் தலைவரால் பிரதமரைப் பதவி நீக்கம் செய்ய முடியாது!"
                        ]
                    }
                },
                {
                    "title": "6. Impact of PM Resignation Trap (பிரதமர் ராஜினாமாவின் தாக்கப் பொறி)",
                    "points": {
                        "en": [
                            "TRAP: Thinking resignation of PM creates only a single vacancy in Council of Ministers.",
                            "FACT: Resignation or death of Prime Minister automatically DISSOLVES the entire Council of Ministers!"
                        ],
                        "ta": [
                            "பொறி: பிரதமரின் ராஜினாமா அமைச்சரவையில் ஒரு காலியிடத்தை மட்டுமே உருவாக்கும் என நினைப்பது.",
                            "உண்மை: பிரதமரின் ராஜினாமா அல்லது இறப்பு தானாகவே முழு அமைச்சரவையையும் கலைத்துவிடும்!"
                        ]
                    }
                },
                {
                    "title": "7. Article 74 vs Article 75 Trap (உறுப்பு 74 vs உறுப்பு 75 பொறி)",
                    "points": {
                        "en": [
                            "TRAP: Confusing Article 74 (Aid and Advice role) with Article 75 (Appointment, Tenure & Responsibility).",
                            "FACT: Article 74 creates Council of Ministers to aid & advise; Article 75 deals with Appointment, Tenure, Oath, and Responsibility!"
                        ],
                        "ta": [
                            "பொறி: உறுப்பு 74 (உதவி & அறிவுரை) மற்றும் உறுப்பு 75 (நியமனம், பதவிக் காலம் & பொறுப்பு) ஆகியவற்றை குழப்பிக் கொள்ளுதல்.",
                            "உண்மை: உறுப்பு 74 உதவவும் அறிவுறுத்தவும் அமைச்சரவையை உருவாக்குகிறது; உறுப்பு 75 நியமனம், பதவிக் காலம், பிரமாணம் மற்றும் பொறுப்பு பற்றி பேசுகிறது!"
                        ]
                    }
                },
                {
                    "title": "8. Oath Administration Trap (பதவிப் பிரமாண நிர்வாகப் பொறி)",
                    "points": {
                        "en": [
                            "TRAP: Believing Chief Justice of India administers oath to the Prime Minister.",
                            "FACT: The PRESIDENT OF INDIA administers both Oath of Office and Oath of Secrecy to the Prime Minister under Article 75(4)!"
                        ],
                        "ta": [
                            "பொறி: இந்தியத் தலைமை நீதிபதி பிரதமருக்குப் பதவிப் பிரமாணம் செய்து வைப்பார் என நினைப்பது.",
                            "உண்மை: உறுப்பு 75(4)-ன் கீழ் இந்தியக் குடியரசுத் தலைவரே பிரதமருக்குப் பதவிப் பிரமாணமும் இரகசியக் காப்புப் பிரமாணமும் செய்து வைக்கிறார்!"
                        ]
                    }
                }
            ],
            "important_facts": {
                "en": [
                    "Article 74(1) establishes that there shall be a Council of Ministers with Prime Minister at head to aid and advise President.",
                    "Article 75(1) mandates that Prime Minister shall be appointed by the President of India.",
                    "The Prime Minister is the Real Executive (De Facto head of government), while President is Nominal Executive (De Jure head of state).",
                    "A non-MP can be appointed Prime Minister for a maximum period of 6 consecutive months under Article 75(5).",
                    "Prime Minister can be a member of either Lok Sabha or Rajya Sabha (Indira Gandhi, Deve Gowda, Gujral, Manmohan Singh were RS members).",
                    "President administers Oath of Office and Oath of Secrecy to Prime Minister under Article 75(4) as per Third Schedule.",
                    "Prime Minister holds office during the pleasure of President (Article 75(2)), which means as long as he enjoys Lok Sabha confidence.",
                    "Resignation or death of Prime Minister automatically collapses/dissolves the entire Council of Ministers."
                ],
                "ta": [
                    "உறுப்பு 74(1) குடியரசுத் தலைவருக்கு உதவவும் அறிவுரை வழங்கவும் பிரதமரைத் தலைவராகக் கொண்ட அமைச்சரவையை நிறுவுகிறது.",
                    "உறுப்பு 75(1) பிரதமர் இந்தியக் குடியரசுத் தலைவரால் நியமிக்கப்பட வேண்டும் என்று ஆணையிடுகிறது.",
                    "பிரதமர் உண்மையான நிர்வாகி (De Facto head of government), குடியரசுத் தலைவர் பெயரளவு நிர்வாகி (De Jure head of state).",
                    "உறுப்பு 75(5)-ன் கீழ் நாடாளுமன்ற உறுப்பினர் அல்லாத ஒருவர் அதிகபட்சமாக 6 தொடர்ச்சியான மாதங்கள் பிரதமராக இருக்க முடியும்.",
                    "பிரதமர் மக்களவை அல்லது மாநிலங்களவை இரண்டிலும் உறுப்பினராக இருக்கலாம் (இந்திரா காந்தி, தேவ கௌடா, குஜ்ரால், மன்மோகன் சிங் RS உறுப்பினர்களாக இருந்தனர்).",
                    "மூன்றாவது அட்டவணைப்படி உறுப்பு 75(4)-ன் கீழ் குடியரசுத் தலைவர் பிரதமருக்குப் பதவிப் பிரமாணமும் இரகசியக் காப்புப் பிரமாணமும் செய்து வைக்கிறார்.",
                    "உறுப்பு 75(2)-ன் கீழ் பிரதமர் குடியரசுத் தலைவரின் விருப்பம் உள்ளவரை பதவி வகிக்கிறார், இதன் பொருள் மக்களவை நம்பிக்கை இருக்கும் வரை மட்டுமே.",
                    "பிரதமரின் ராஜினாமா அல்லது இறப்பு தானாகவே முழு அமைச்சரவையையும் கலைத்துவிடும்."
                ]
            },
            "quick_revision": {
                "en": [
                    "Status: Real Executive (De Facto Head of Govt); Rank 3 in Indian Precedence.",
                    "Article 74: Head of Council of Ministers aiding & advising President (Advice binding post 42nd & 44th CAAs).",
                    "Article 75(1): Appointed by President; Convention mandates appointing Lok Sabha majority leader.",
                    "Hung House: Presidential situational discretion to appoint largest party/coalition leader (1 month floor test window).",
                    "Membership: Lok Sabha or Rajya Sabha; Non-MP has 6-month constitutional window under Article 75(5).",
                    "Age Limit: Minimum 25 years (if Lok Sabha MP) / Minimum 30 years (if Rajya Sabha MP).",
                    "Oath: Administered by President (Article 75(4)) — Oath of Office + Oath of Secrecy (Third Schedule).",
                    "Tenure: Holds office during pleasure of President (Article 75(2)), tied strictly to Lok Sabha majority confidence."
                ],
                "ta": [
                    "நிலை: உண்மை நிர்வாகி (De Facto Head of Govt); இந்திய முன்னுரிமை வரிசையில் 3ம் இடம்.",
                    "உறுப்பு 74: குடியரசுத் தலைவருக்கு உதவவும் அறிவுரை வழங்கவும் உள்ள அமைச்சரவையின் தலைவர் (42 & 44 CAAs பின் அறிவுரை கட்டுப்படுத்தும்).",
                    "உறுப்பு 75(1): குடியரசுத் தலைவரால் நியமனம்; மக்களவை பெரும்பான்மை தலைவரை நியமிப்பது அரசியல் மரபு.",
                    "தொங்கு மக்களவை: மிகப்பெரிய கட்சி/கூட்டணி தலைவரை நியமிக்கக் குடியரசுத் தலைவருக்குச் சூழ்நிலை விருப்ப அதிகாரம் (1 மாத நம்பிக்க வாக்கெடுப்பு).",
                    "அவை உறுப்பினர் தகுதி: மக்களவை அல்லது மாநிலங்களவை; உறுப்பினர் அல்லாதவருக்கு உறுப்பு 75(5)-ன் கீழ் 6 மாத அவகாசம்.",
                    "வயது வரம்பு: குறைந்தபட்சம் 25 வயது (மக்களவை) / குறைந்தபட்சம் 30 வயது (மாநிலங்களவை).",
                    "பதவிப் பிரமாணம்: குடியரசுத் தலைவரால் செய்து வைக்கப்படுகிறது (உறுப்பு 75(4)) — பதவிப் பிரமாணம் + இரகசியக் காப்புப் பிரமாணம் (3வது அட்டவணை).",
                    "பதவிக் காலம்: குடியரசுத் தலைவரின் விருப்பம் உள்ளவரை (உறுப்பு 75(2)), இது மக்களவை பெரும்பான்மை நம்பிக்கையுடன் பிணைக்கப்பட்டது."
                ]
            },
            "revision_cards": [
                {
                    "title": "Article 74(1)",
                    "content_en": "Council of Ministers with Prime Minister at head to aid and advise President of India.",
                    "content_ta": "குடியரசுத் தலைவருக்கு உதவவும் அறிவுரை வழங்கவும் பிரதமரைத் தலைவராகக் கொண்ட அமைச்சரவை."
                },
                {
                    "title": "Article 75(1)",
                    "content_en": "Prime Minister shall be appointed by the President of India.",
                    "content_ta": "பிரதமர் இந்தியக் குடியரசுத் தலைவரால் நியமிக்கப்படுவார்."
                },
                {
                    "title": "Article 75(2)",
                    "content_en": "Prime Minister holds office during the pleasure of the President (LS majority confidence).",
                    "content_ta": "பிரதமர் குடியரசுத் தலைவரின் விருப்பம் உள்ளவரை (மக்களவை பெரும்பான்மை நம்பிக்கை) பதவி வகிப்பார்."
                },
                {
                    "title": "Article 75(4)",
                    "content_en": "President administers Oath of Office and Oath of Secrecy to Prime Minister.",
                    "content_ta": "குடியரசுத் தலைவர் பிரதமருக்குப் பதவிப் பிரமாணமும் இரகசியக் காப்புப் பிரமாணமும் செய்து வைக்கிறார்."
                },
                {
                    "title": "Article 75(5)",
                    "content_en": "Non-MP can be Prime Minister for a maximum period of 6 consecutive months.",
                    "content_ta": "உறுப்பினர் அல்லாத ஒருவர் அதிகபட்சமாக 6 தொடர்ச்சியான மாதங்கள் பிரதமராக இருக்க முடியும்."
                },
                {
                    "title": "De Facto Executive",
                    "content_en": "Prime Minister is the real executive head of government in parliamentary system.",
                    "content_ta": "நாடாளுமன்ற அமைப்பில் பிரதமர் அரசாங்கத்தின் உண்மையான நிர்வாகத் தலைவராவார்."
                },
                {
                    "title": "Rajya Sabha PMs",
                    "content_en": "Indira Gandhi (1966), Deve Gowda (1996), I.K. Gujral (1997), Manmohan Singh (2004, 2009).",
                    "content_ta": "இந்திரா காந்தி (1966), தேவ கௌடா (1996), ஐ.கே. குஜ்ரால் (1997), மன்மோகன் சிங் (2004, 2009)."
                },
                {
                    "title": "Hung House Discretion",
                    "content_en": "President appoints largest party/coalition leader as PM & asks to prove majority in 1 month.",
                    "content_ta": "குடியரசுத் தலைவர் மிகப்பெரிய கட்சித் தலைவரை நியமித்து 1 மாதத்தில் பெரும்பான்மையை நிரூபிக்கப் பணிக்கிறார்."
                },
                {
                    "title": "Resignation Impact",
                    "content_en": "Resignation or death of Prime Minister automatically collapses/dissolves entire ministry.",
                    "content_ta": "பிரதமரின் ராஜினாமா அல்லது இறப்பு தானாகவே முழு அமைச்சரவையையும் கலைத்துவிடும்."
                },
                {
                    "title": "Keystone of Cabinet",
                    "content_en": "Sir Ivor Jennings described Prime Minister as the 'Keystone of the Cabinet Arch'.",
                    "content_ta": "சர் ஐவர் ஜென்னிங்ஸ் பிரதமரை 'அமைச்சரவை வளைவின் முதன்மைக் கல்' என விவரித்தார்."
                }
            ]
        }
    }
    return part1_data

def validate_part1(data):
    meta = data.get("meta", {})
    assert meta.get("topic_id") == "polity_prime_minister_part_1", f"Invalid topic_id: {meta.get('topic_id')}"
    assert meta.get("part") == 1, f"Invalid part: {meta.get('part')}"
    assert meta.get("total_parts") == 3, f"Invalid total_parts: {meta.get('total_parts')}"
    
    content = data.get("content", {})
    tables = content.get("comparison_tables") or []
    assert len(tables) == 5, f"Expected 5 comparison tables, got {len(tables)}"
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
    assert len(traps) >= 8, f"Expected at least 8 TNPSC traps, got {len(traps)}"
    
    rev = content.get("revision_cards", [])
    assert len(rev) >= 10, f"Expected at least 10 revision cards, got {len(rev)}"

    assert content.get("important_facts", {}).get("en") and content.get("important_facts", {}).get("ta")
    assert content.get("quick_revision", {}).get("en") and content.get("quick_revision", {}).get("ta")
    print("✅ PART 1 VALIDATION PASSED COMPLETELY!")

def main():
    print("==================================================")
    print("GENERATING & VALIDATING PRIME MINISTER PART 1 NOTES")
    print("==================================================")
    data = generate_part1()
    validate_part1(data)
    
    out_dir = "data/notes/polity"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "prime_minister_part_1.json")
    
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
    assert os.path.exists(out_path), f"File was not created at {out_path}"
    print(f"✅ SAVED IMMEDIATELY & CONFIRMED FILE EXISTS: {out_path}")

if __name__ == "__main__":
    main()
