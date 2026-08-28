import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

def generate_part2():
    part2_data = {
        "meta": {
            "topic_id": "polity_prime_minister_part_2",
            "repository_id": "polity_prime_minister",
            "display_title": "Prime Minister of India – Part 2",
            "part": 2,
            "total_parts": 3,
            "subject": "polity",
            "chapter": "Prime Minister of India",
            "language": "English + Tamil"
        },
        "metadata": {
            "topic_id": "polity_prime_minister_part_2",
            "repository_id": "polity_prime_minister",
            "display_title": "Prime Minister of India – Part 2",
            "part": 2,
            "total_parts": 3,
            "subject": "polity",
            "chapter": "Prime Minister of India",
            "language": "English + Tamil"
        },
        "keywords": [
            "Powers and Functions of Prime Minister",
            "பிரதமரின் அதிகாரங்கள் மற்றும் பணிகள்",
            "Article 78 Duties of PM",
            "உறுப்பு 78 பிரதமரின் கடமைகள்",
            "Council of Ministers vs Cabinet",
            "அமைச்சரவை vs அமைச்சரவை குழு",
            "Collective Responsibility",
            "கூட்டுப் பொறுப்பு",
            "Individual Responsibility",
            "தனிப்பட்ட பொறுப்பு",
            "NITI Aayog Chairman",
            "நிதி ஆயோக் தலைவர்",
            "Inter-State Council",
            "மாநிலங்களுக்கிடையேயான குழு",
            "Parliamentary Leadership",
            "நாடாளுமன்றத் தலைமை",
            "Foreign Policy Spokesman",
            "வெளியுறவுக் கொள்கை प्रवக்தா"
        ],
        "learning_outcomes": {
            "Understand": {
                "en": [
                    "Master the powers and functions of the Prime Minister in relation to the President under Article 78.",
                    "Analyze the leadership role of the Prime Minister over the Council of Ministers and Cabinet coordination.",
                    "Distinguish clearly between the Council of Ministers (Article 74) and Cabinet (Article 352, added by 44th CAA 1978).",
                    "Understand the Prime Minister's powers in relation to Parliament (summoning, prorogation, dissolution of Lok Sabha).",
                    "Examine the Prime Minister's advisory role in major constitutional appointments (CAG, Attorney General, Election Commission, etc.).",
                    "Grasp the Prime Minister's leadership roles as Chairman of NITI Aayog, Inter-State Council, NDMA, and chief foreign policy maker."
                ],
                "ta": [
                    "உறுப்பு 78-ன் கீழ் குடியரசுத் தலைவருடனான தொடர்பில் பிரதமரின் அதிகாரங்கள் மற்றும் கடமைகளைத் தெரிந்துகொள்ளுதல்.",
                    "அமைச்சர்கள் குழு மற்றும் அமைச்சரவைக் குழுவின் (Cabinet) ஒருங்கிணைப்பில் பிரதமரின் தலைமைப் பங்கைப் பகுப்பாய்வு செய்தல்.",
                    "அமைச்சரவை குழுவிற்கும் (Council of Ministers - Art 74) அமைச்சரவைக்கும் (Cabinet - Art 352, 44வது CAA 1978) இடையிலான வேறுபாடுகளைத் தெளிவாகப் புரிந்துகொள்ளுதல்.",
                    "நாடாளுமன்றத்துடனான தொடர்பில் பிரதமரின் அதிகாரங்களைப் புரிந்துகொள்ளுதல் (கூட்டுதல், ஒத்திவைத்தல், மக்களவையைக் கலைத்தல்).",
                    "முக்கிய அரசியலமைப்பு நியமனங்களில் (CAG, அட்டர்னி ஜெனரல், தேர்தல் ஆணையம் போன்றவை) பிரதமரின் ஆலோசனையைப் புரிந்துகொள்ளுதல்.",
                    "நிதி ஆயோக், மாநிலங்களுக்கிடையேயான குழு, NDMA ஆகியவற்றின் தலைவராகவும் வெளியுறவுக் கொள்கை வடிவமைப்பாளராகவும் பிரதமரின் பங்கைப் புரிந்துகொள்ளுதல்."
                ]
            },
            "Remember": {
                "en": [
                    "Remember Article 78 specifies duties of Prime Minister to inform President.",
                    "Remember Cabinet word was inserted into Article 352 by the 44th Constitutional Amendment Act 1978.",
                    "Remember PM is Ex-officio Chairman of NITI Aayog, Inter-State Council, National Integration Council, and NDMA.",
                    "Remember PM recommends appointment and dismissal of individual ministers to the President.",
                    "Remember PM advises President on dissolution of Lok Sabha under Article 85."
                ],
                "ta": [
                    "உறுப்பு 78 குடியரசுத் தலைவருக்குத் தகவல் தெரிவிக்கும் பிரதமரின் கடமைகளைக் குறிப்பிடுகிறது என்பதை நினைவில் கொள்ளுதல்.",
                    "1978-ன் 44-வது அரசியலமைப்புத் திருத்தச் சட்டத்தின் மூலம் உறுப்பு 352-ல் 'Cabinet' என்ற சொல் சேர்க்கப்பட்டது என்பதை நினைவில் கொள்ளுதல்.",
                    "பிரதமர் நிதி ஆயோக், மாநிலங்களுக்கிடையேயான குழு, தேசிய ஒருமைப்பாட்டுக் குழு, NDMA ஆகியவற்றின் பதவிவழித் தலைவர் என்பதை நினைவில் கொள்ளுதல்.",
                    "பிரதமர் தனிப்பட்ட அமைச்சர்களின் நியமனம் மற்றும் பதவி நீக்கத்தைக் குடியரசுத் தலைவருக்குப் பரிந்துரைக்கிறார் என்பதை நினைவில் கொள்ளுதல்.",
                    "உறுப்பு 85-ன் கீழ் மக்களவையைக் கலைப்பது தொடர்பாகப் பிரதமர் குடியரசுத் தலைவருக்கு அறிவுறுத்துகிறார் என்பதை நினைவில் கொள்ளுதல்."
                ]
            }
        },
        "subject": "polity",
        "topic": "Prime Minister of India",
        "language": "English + Tamil",
        "ui_type": "standard_notes",
        "sections": [
            {
                "id": "sec_relation_with_president",
                "title_en": "1. Relationship with the President & Article 78 Duties",
                "title_ta": "1. குடியரசுத் தலைவருடனான தொடர்பு & உறுப்பு 78 கடமைகள்",
                "type": "standard_topic"
            },
            {
                "id": "sec_relation_with_council",
                "title_en": "2. Powers in Relation to Council of Ministers",
                "title_ta": "2. அமைச்சர்கள் குழுவுடனான அதிகாரங்கள்",
                "type": "standard_topic"
            },
            {
                "id": "sec_cabinet_leadership",
                "title_en": "3. Leadership of Cabinet & Distinction: Council vs Cabinet",
                "title_ta": "3. அமைச்சரவையின் தலைமை & வேறுபாடு: Council vs Cabinet",
                "type": "standard_topic"
            },
            {
                "id": "sec_powers_in_parliament",
                "title_en": "4. Powers in Relation to Parliament (Article 85)",
                "title_ta": "4. நாடாளுமன்றத்துடனான அதிகாரங்கள் (உறுப்பு 85)",
                "type": "standard_topic"
            },
            {
                "id": "sec_appointments_and_bodies",
                "title_en": "5. Constitutional Appointments & Institutional Ex-Officio Chairmanships",
                "title_ta": "5. அரசியலமைப்பு நியமனங்கள் & நிறுவனப் பதவிவழித் தலைமைகள்",
                "type": "standard_topic"
            },
            {
                "id": "sec_foreign_national_leadership",
                "title_en": "6. Foreign Policy Spokesman & Crisis Manager-in-Chief",
                "title_ta": "6. வெளியுறவுக் கொள்கைப் प्रवக்தா & அவசர கால நிர்வாகி",
                "type": "standard_topic"
            },
            {
                "id": "comparison_tables",
                "title_en": "7. Mandatory Comparison Tables (Powers & Functions)",
                "title_ta": "7. கட்டாய ஒப்பீட்டு அட்டவணைகள் (அதிகாரங்கள் & பணிகள்)",
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
                "en": "The Prime Minister of India possesses extensive executive, legislative, and emergency functions as the real operational head of the Union administration. From chairing Cabinet meetings and allocating portfolios to advising the President on major constitutional appointments and representing India internationally, the Prime Minister functions as the chief policy architect and crisis manager of the nation.",
                "ta": "இந்தியப் பிரதமர் ஒன்றிய நிர்வாகத்தின் உண்மையான செயல்முறைத் தலைவராக பரந்த நிர்வாக, சட்டவாக்க மற்றும் அவசரகாலப் பணிகளைக் கொண்டுள்ளார். அமைச்சரவைக் கூட்டங்களுக்குத் தலைமை தாங்குவது மற்றும் துறைகளை ஒதுக்குவது முதல் முக்கிய அரசியலமைப்பு நியமனங்களில் குடியரசுத் தலைவருக்கு அறிவுறுத்துவது மற்றும் சர்வதேச அளவில் இந்தியாவைப் பிரதிநிதித்துவப்படுத்துவது வரை, பிரதமர் நாட்டின் முதன்மை கொள்கைக் வடிவமைப்பாளராகவும் அவசரகால நிர்வாகியாகவும் செயல்படுகிறார்."
            },
            "introduction": {
                "en": "While the Constitution formally vests executive authority in the President under Article 53, the actual exercise of these powers flows through the Prime Minister. Article 78 acts as the constitutional bridge connecting the Cabinet to the President, defining the Prime Minister's duties to keep the Head of State fully informed of all administrative and legislative actions.",
                "ta": "உறுப்பு 53-ன் கீழ் அரசியலமைப்பு முறைப்படி குடியரசுத் தலைவரிடம் நிர்வாக அதிகாரங்களை வழங்கியிருந்தாலும், அந்த அதிகாரங்களின் நடைமுறைப் பயன்பாடு பிரதமர் மூலமாகவே நிகழ்கிறது. உறுப்பு 78 அமைச்சரவையைக் குடியரசுத் தலைவருடன் இணைக்கும் அரசியலமைப்புப் பாலமாகச் செயல்பட்டு, அனைத்து நிர்வாக மற்றும் சட்டவாக்க நடவடிக்கைகளையும் நாட்டின் தலைவருக்குத் தெரிவிக்கும் பிரதமரின் கடமைகளை வரையறுக்கிறது."
            },
            "sec_relation_with_president": [
                {
                    "title": "1. Article 78: Constitutional Duties of Prime Minister towards President",
                    "points": {
                        "en": [
                            "Article 78(a): Principal Channel of Communication — To communicate to the President all decisions of the Council of Ministers relating to administration of affairs of the Union and proposals for legislation.",
                            "Article 78(b): Furnishing Information — To furnish such information relating to administration and proposals for legislation as the President may call for.",
                            "Article 78(c): Submission for Cabinet Consideration — If the President so requires, to submit for consideration of Council of Ministers any matter on which a decision has been taken by a Minister but which has not been considered by the Council.",
                            "Constitutional Bridge: PM acts as the sole constitutional link between the Head of State (President) and the Executive Cabinet."
                        ],
                        "ta": [
                            "உறுப்பு 78(a): முதன்மைத் தொடர்பு ஊடகம் — ஒன்றியத்தின் நிர்வாகம் தொடர்பான அமைச்சரவையின் அனைத்து முடிவுகளையும் சட்டவாக்க முன்மொழிவுகளையும் குடியரசுத் தலைவருக்குத் தெரிவித்தல்.",
                            "உறுப்பு 78(b): தகவல்களை வழங்குதல் — நிர்வாகம் மற்றும் சட்டவாக்க முன்மொழிவுகள் குறித்து குடியரசுத் தலைவர் கோரும் தகவல்களை வழங்குதல்.",
                            "உறுப்பு 78(c): அமைச்சரவையின் பரிசீலனைக்குச் சமர்ப்பித்தல் — ஒரு தனிப்பட்ட அமைச்சரால் முடிவு எடுக்கப்பட்டு அமைச்சரவையால் பரிசீலிக்கப்படாத எந்தவொரு விஷயத்தையும் குடியரசுத் தலைவர் கோரினால் அமைச்சரவையின் பரிசீலனைக்குச் சமர்ப்பித்தல்.",
                            "அரசியலமைப்புப் பாலம்: நாட்டின் தலைவருக்கும் (குடியரசுத் தலைவர்) நிர்வாக அமைச்சரவைக்கும் இடையே பிரதமர் ஒரே அரசியலமைப்பு இணைப்பாகச் செயல்படுகிறார்."
                        ]
                    }
                },
                {
                    "title": "2. Recommendation of Constitutional Appointments",
                    "points": {
                        "en": [
                            "Advisory Role: PM advises President on appointment of key constitutional officers:",
                            "• Attorney General of India (Article 76)",
                            "• Comptroller and Auditor General of India (CAG - Article 148)",
                            "• Chief Election Commissioner & Election Commissioners (Article 324)",
                            "• Chairman and Members of Union Public Service Commission (UPSC - Article 316)",
                            "• Finance Commission Chairman & Members (Article 280)",
                            "• Governors of States (Article 155)",
                            "Reality of Appointment: Although President issues appointment warrants, choices are determined by PM and Cabinet."
                        ],
                        "ta": [
                            "ஆலோசனைப் பங்கு: முக்கிய அரசியலமைப்பு அதிகாரிகளின் நியமனத்தில் பிரதமர் குடியரசுத் தலைவருக்கு அறிவுறுத்துகிறார்:",
                            "• இந்திய அட்டர்னி ஜெனரல் (உறுப்பு 76)",
                            "• இந்தியக் தலைமைத் தணிக்கையாளர் (CAG - உறுப்பு 148)",
                            "• தலைமைத் தேர்தல் ஆணையர் & தேர்தல் ஆணையர்கள் (உறுப்பு 324)",
                            "• UPSC தலைவர் மற்றும் உறுப்பினர்கள் (உறுப்பு 316)",
                            "• நிதி ஆணையத் தலைவர் & உறுப்பினர்கள் (உறுப்பு 280)",
                            "• மாநில ஆளுநர்கள் (உறுப்பு 155)",
                            "நியமனத்தின் உண்மைநிலை: குடியரசுத் தலைவர் நியமன ஆணைகளை வெளியிட்டாலும், தேர்வுகளைப் பிரதமரும் அமைச்சரவையுமே தீர்மானிக்கின்றனர்."
                        ]
                    }
                }
            ],
            "sec_relation_with_council": [
                {
                    "title": "1. Formation, Allocation and Direction of Council of Ministers",
                    "points": {
                        "en": [
                            "Recommendation for Appointment: President appoints Ministers ONLY on the recommendation of the Prime Minister (Article 75(1)).",
                            "Allocation of Portfolios: PM allocates and reshuffles portfolios among Ministers at his personal discretion.",
                            "Presiding Officer of Cabinet: PM presides over Cabinet meetings and influences its decisions.",
                            "Guidance & Control: PM guides, directs, controls, and coordinates activities of all Ministers and ministries.",
                            "Dismissal of Ministers: PM can ask a minister to resign or advise the President to dismiss him in case of disagreement."
                        ],
                        "ta": [
                            "நியமனப் பரிந்துரை: பிரதமரின் பரிந்துரையின் பேரில் மட்டுமே குடியரசுத் தலைவர் அமைச்சர்களை நியமிக்கிறார் (உறுப்பு 75(1)).",
                            "துறைகள் ஒதுக்கீடு: பிரதமர் தனது தனிப்பட்ட விவேகத்தின் படி அமைச்சர்களுக்கு இடையே துறைகளை ஒதுக்குகிறார் மற்றும் மாற்றுகிறார்.",
                            "அமைச்சரவையின் தலைவர்: பிரதமர் அமைச்சரவைக் கூட்டங்களுக்குத் தலைமை தாங்கி அதன் முடிவுகளைத் தீர்மானிக்கிறார்.",
                            "வழிகாட்டல் & கட்டுப்பாடு: அனைத்து அமைச்சர்கள் மற்றும் அமைச்சகங்களின் செயல்பாடுகளைப் பிரதமர் வழிகாட்டுகிறார், இயக்குகிறார், கட்டுப்படுத்துகிறார், ஒருங்கிணைக்கிறார்.",
                            "அமைச்சர்கள் பதவி நீக்கம்: கருத்து வேறுபாடு ஏற்பட்டால் ஒரு அமைச்சரை ராஜினாமா செய்யுமாறு கேட்கலாம் அல்லது குடியரசுத் தலைவருக்குப் பரிந்துரைத்து அவரைப் பதவி நீக்கம் செய்யலாம்."
                        ]
                    }
                },
                {
                    "title": "2. Central Pivot of Ministerial Survival",
                    "points": {
                        "en": [
                            "Resignation / Death Effect: The death or resignation of Prime Minister automatically causes dissolution of Council of Ministers.",
                            "Contrast with Individual Minister: The death or resignation of any other minister creates merely a single vacancy which PM fills.",
                            "Individual Responsibility (Art 75(2)): Ministers hold office during pleasure of President, which is exercised on advice of PM."
                        ],
                        "ta": [
                            "ராஜினாமா / இறப்பின் தாக்கம்: பிரதமரின் இறப்பு அல்லது ராஜினாமா தானாகவே அமைச்சரவையைக் கலைக்க வழிவகுக்கும்.",
                            "தனிப்பட்ட அமைச்சருடனான ஒப்பீடு: வேறு எந்த அமைச்சரின் இறப்பும் அல்லது ராஜினாமாவும் ஒரு காலியிடத்தை மட்டுமே உருவாக்கும், அதை பிரதமர் நிரப்புவார்.",
                            "தனிப்பட்ட பொறுப்பு (உறுப்பு 75(2)): அமைச்சர்கள் குடியரசுத் தலைவரின் விருப்பம் உள்ளவரை பதவி வகிக்கின்றனர், இது பிரதமரின் அறிவுரைப்படி பயன்படுத்தப்படுகிறது."
                        ]
                    }
                }
            ],
            "sec_cabinet_leadership": [
                {
                    "title": "1. Distinction between Council of Ministers & Cabinet",
                    "points": {
                        "en": [
                            "Council of Ministers (Article 74 & 75): Wide constitutional body comprising 60 to 70 ministers across three tiers — Cabinet Ministers, Ministers of State, and Deputy Ministers. It does not meet as a single body to transact business.",
                            "Cabinet (Article 352): Inner core body comprising 15 to 20 senior ministers holding cabinet rank. It meets regularly to formulate national policies.",
                            "44th CAA 1978 History: The word 'Cabinet' was NOT part of original Constitution. It was inserted into Article 352 by 44th Amendment 1978 (defined as Council of Ministers of Cabinet rank).",
                            "PM's Cabinet Leadership: PM heads the Cabinet, sets agenda, and ensures implementation of decisions across all ministries."
                        ],
                        "ta": [
                            "அமைச்சர்கள் குழு (Council of Ministers) vs அமைச்சரவை (Cabinet) வேறுபாடு: அமைச்சர்கள் குழு (உறுப்புகள் 74 & 75) என்பது 60 முதல் 70 அமைச்சர்களைக் கொண்ட பரந்த அரசியலமைப்பு அமைப்பாகும் (கேபினட் அமைச்சர்கள், ராஜாங்க அமைச்சர்கள், இணை அமைச்சர்கள்). இது ஆட்சிப் பணிகளைச் செய்ய ஒரே அமைப்பாக ஒன்று கூடுவதில்லை.",
                            "அமைச்சரவை (Cabinet - உறுப்பு 352): கேபினட் அந்தஸ்து கொண்ட 15 முதல் 20 மூத்த அமைச்சர்களைக் கொண்ட உள்கட்டமைப்பு அமைப்பு. இது தேசியக் கொள்கைகளை உருவாக்க வழக்கமாக கூட்டுகிறது.",
                            "44வது திருத்தம் 1978 வரலாறு: 'Cabinet' என்ற சொல் மூல அரசியலமைப்பில் இல்லை. 1978-ன் 44வது திருத்தத்தின் மூலம் உறுப்பு 352-ல் சேர்க்கப்பட்டது.",
                            "பிரதமரின் கேபினட் தலைமை: பிரதமர் கேபினட்டிற்குத் தலைமை தாங்கி, நிகழ்ச்சி நிரலை அமைத்து, அனைத்து அமைச்சகங்களிலும் முடிவுகள் செயல்படுத்தப்படுவதை உறுதி செய்கிறார்."
                        ]
                    }
                }
            ],
            "sec_powers_in_parliament": [
                {
                    "title": "1. Leadership in Parliament & Legislative Functions (Article 85)",
                    "points": {
                        "en": [
                            "Leader of the House: PM is the leader of Lok Sabha (if member of LS) or appoints a senior cabinet minister as Leader of the House.",
                            "Summoning & Prorogation Advice: PM advises President with regard to summoning and proroguing sessions of Parliament (Article 85).",
                            "Dissolution Advice: PM can advise President to dissolve Lok Sabha at any time before expiry of term (Article 85(2)(b)).",
                            "Policy Announcements: PM announces major national policies on the floor of the House."
                        ],
                        "ta": [
                            "அவையின் தலைவர்: பிரதமர் மக்களவையின் தலைவராகச் செயல்படுகிறார் (மக்களவை உறுப்பினராக இருந்தால்) அல்லது ஒரு மூத்த கேபினட் அமைச்சரை அவைத் தலைவராக நியமிக்கிறார்.",
                            "கூட்டுதல் & ஒத்திவைத்தல் அறிவுரை: நாடாளுமன்றக் கூட்டங்களைக் கூட்டுவது மற்றும் ஒத்திவைப்பது குறித்துப் பிரதமர் குடியரசுத் தலைவருக்கு அறிவுறுத்துகிறார் (உறுப்பு 85).",
                            "கலைப்பு அறிவுரை: பதவிக் காலம் முடிவதற்கு முன்பாக எந்த நேரத்திலும் மக்களவையைக் கலைக்கப் பிரதமர் குடியரசுத் தலைவருக்கு அறிவுறுத்தலாம் (உறுப்பு 85(2)(b)).",
                            "கொள்கை அறிவிப்புகள்: பிரதமர் முக்கிய தேசியக் கொள்கைகளை நாடாளுமன்றத்தில் அறிவிக்கிறார்."
                        ]
                    }
                }
            ],
            "sec_appointments_and_bodies": [
                {
                    "title": "1. Ex-Officio Chairmanships of Key National Bodies",
                    "points": {
                        "en": [
                            "NITI Aayog: Ex-officio Chairman of NITI Aayog (National Institution for Transforming India - replaced Planning Commission in 2015).",
                            "Inter-State Council: Ex-officio Chairman of Inter-State Council set up under Article 263.",
                            "National Integration Council (NIC): Chairman of NIC promoting national unity.",
                            "National Disaster Management Authority (NDMA): Chairman of NDMA established under Disaster Management Act 2005.",
                            "National Water Resources Council: Chairman of National Water Resources Council."
                        ],
                        "ta": [
                            "நிதி ஆயோக் (NITI Aayog): நிதி ஆயோக்கின் பதவிவழித் தலைவர் (2015-ல் திட்டக் குழுவுக்குப் பதிலாக உருவாக்கப்பட்டது).",
                            "மாநிலங்களவைக்குடையேயான குழு: உறுப்பு 263-ன் கீழ் அமைக்கப்பட்ட மாநிலங்களவைக்குடையேயான குழுவின் பதவிவழித் தலைவர்.",
                            "தேசிய ஒருமைப்பாட்டுக் குழு (NIC): தேசிய ஒருமைப்பாட்டை ஊக்குவிக்கும் NIC-ன் தலைவர்.",
                            "தேசிய பேரிடர் மேலாண்மை ஆணையம் (NDMA): 2005 பேரிடர் மேலாண்மைச் சட்டத்தின் கீழ் அமைக்கப்பட்ட NDMA-வின் தலைவர்.",
                            "தேசிய நீர் ஆதாரக் குழு: தேசிய நீர் ஆதாரக் குழுவின் தலைவர்."
                        ]
                    }
                }
            ],
            "sec_foreign_national_leadership": [
                {
                    "title": "1. Chief Spokesman of Foreign Policy & Crisis Leadership",
                    "points": {
                        "en": [
                            "Chief Foreign Policy Architect: PM represents India at G20, BRICS, SCO, Commonwealth, United Nations, and bilateral summits.",
                            "Crisis Manager-in-Chief: During political, economic, security or health crises, PM acts as the supreme operational manager of the nation.",
                            "Leader of the Nation: Addresses nation on Independence Day (August 15) from Red Fort ramparts."
                        ],
                        "ta": [
                            "வெளியுறவுக் கொள்கையின் முதன்மை வடிவமைப்பாளர்: ஜி20, பிரிக்ஸ், எஸ்சிஓ, காமன்வெல்த், ஐக்கிய நாடுகள் சபை மற்றும் இருதரப்பு உச்சிமாநாடுகளில் இந்தியாவைப் பிரதமர் பிரதிநிதித்துவப்படுத்துகிறார்.",
                            "அவசரகால முதன்மை நிர்வாகி: அரசியல், பொருளாதார, பாதுகாப்பு அல்லது சுகாதார நெருக்கடிகளின் போது, நாட்டின் உச்ச செயல்பாட்டு நிர்வாகியாகப் பிரதமர் செயல்படுகிறார்.",
                            "தேசியத் தலைவர்: சுதந்திர தினத்தன்று (ஆகஸ்ட் 15) செங்கோட்டை முகப்பிலிருந்து நாட்டிற்கு உரையாற்றுகிறார்."
                        ]
                    }
                }
            ],
            "comparison_tables": [
                {
                    "id": "comp_pm_vs_pres_powers",
                    "title_en": "1. Prime Minister vs President — Powers & Functions",
                    "title_ta": "1. பிரதமர் vs குடியரசுத் தலைவர் — அதிகாரங்கள் & பணிகள்",
                    "headers_en": ["Area", "Prime Minister of India", "President of India"],
                    "headers_ta": ["துறை", "இந்தியப் பிரதமர்", "இந்தியக் குடியரசுத் தலைவர்"],
                    "rows_en": [
                        ["Executive Action", "Formulates policies and makes actual administrative decisions", "Promulgates decisions in formal name of President (Art 77)"],
                        ["Cabinet Role", "Heads Cabinet, sets agenda, and coordinates portfolios", "Acts strictly on binding aid and advice of PM-led Cabinet"],
                        ["Appointments", "Recommends names for CAG, Attorney General, Governors", "Formally signs appointment warrants and instruments"],
                        ["Parliament Role", "Advises summoning, proroguing & dissolution of Lok Sabha", "Summons, prorogues & dissolves Lok Sabha on PM advice (Art 85)"],
                        ["Foreign Affairs", "Shapes foreign policy & negotiates treaties directly", "Represents India formally; treaties signed in his name"]
                    ],
                    "rows_ta": [
                        ["நிர்வாக நடவடிக்கை", "கொள்கைகளை உருவாக்கி நடைமுறை நிர்வாக முடிவுகளை எடுக்கிறார்", "முறையான பெயரில் முடிவுகளை வெளியிடுகிறார் (உறுப்பு 77)"],
                        ["அமைச்சரவைப் பங்கு", "அமைச்சரவைக்குத் தலைமை தாங்கி துறைகளை ஒருங்கிணைக்கிறார்", "அமைச்சரவையின் கட்டுப்படுத்தும் அறிவுரைப்படி செயல்படுகிறார்"],
                        ["நியமனங்கள்", "CAG, அட்டர்னி ஜெனரல், ஆளுநர்கள் பெயர்களைப் பரிந்துரைக்கிறார்", "நியமன ஆணைகளில் முறைப்படி கையெழுத்திடுகிறார்"],
                        ["நாடாளுமன்றப் பங்கு", "கூட்டுதல், ஒத்திவைத்தல் & கலைப்பு குறித்து அறிவுறுத்துகிறார்", "பிரதமர் அறிவுரைப்படி கூட்டுகிறார், ஒத்திவைக்கிறார் & கலைக்கிறார்"],
                        ["வெளியுறவு விவகாரங்கள்", "வெளியுறவுக் கொள்கையை வடிவமைத்து ஒப்பந்தங்களை பேசுகிறார்", "நாட்டை முறைப்படி பிரதிநிதித்துவப்படுத்துகிறார்; ஒப்பந்தங்கள் அவர் பெயரில்"]
                    ]
                },
                {
                    "id": "comp_pm_vs_cabinet",
                    "title_en": "2. Prime Minister vs Cabinet",
                    "title_ta": "2. பிரதமர் vs கேபினட் (Cabinet)",
                    "headers_en": ["Dimension", "Prime Minister of India", "Cabinet (Inner Core)"],
                    "headers_ta": ["பரிமாணம்", "இந்தியப் பிரதமர்", "கேபினட் (உள்கட்டமைப்பு)"],
                    "rows_en": [
                        ["Position", "Individual leader & Head of Cabinet", "Collective body of senior cabinet rank ministers"],
                        ["Relationship", "Keystone of Cabinet arch; Moon among lesser stars", "Consultative decision-making council led by PM"],
                        ["Authority", "Can advise dismissal of any minister or resign to dissolve", "Recommends collective policies to Parliament under PM"],
                        ["Constitutional Origin", "Article 74(1) & 75(1) original text", "Article 352 inserted by 44th CAA 1978"]
                    ],
                    "rows_ta": [
                        ["நிலை", "தனிப்பட்ட தலைவர் & கேபினட்டின் தலைவர்", "மூத்த கேபினட் அமைச்சர்களின் கூட்டு அமைப்பு"],
                        ["தொடர்பு", "அமைச்சரவை வளைவின் முதன்மைக் கல்; விண்மீன்களுக்கிடையே நிலவு", "பிரதமர் தலைமையிலான கலந்தாய்வு முடிவு எடுக்கும் மன்றம்"],
                        ["அதிகாரம்", "அமைச்சரை நீக்கப் பரிந்துரைக்கலாம்; ராஜினாமா செய்து கலைக்கலாம்", "பிரதமர் தலைமையில் நாடாளுமன்றத்திற்கு கூட்டுக் கொள்கைகளைப் பரிந்துரைக்கிறது"],
                        ["அரசியலமைப்புத் தோற்றம்", "மூல உரையில் உறுப்புகள் 74(1) & 75(1)", "44வது திருத்தம் 1978 மூலம் உறுப்பு 352-ல் சேர்க்கப்பட்டது"]
                    ]
                },
                {
                    "id": "comp_com_vs_cabinet",
                    "title_en": "3. Council of Ministers vs Cabinet",
                    "title_ta": "3. அமைச்சர்கள் குழு vs அமைச்சரவை (Council of Ministers vs Cabinet)",
                    "headers_en": ["Feature", "Council of Ministers", "Cabinet"],
                    "headers_ta": ["அம்சம்", "அமைச்சர்கள் குழு (Council of Ministers)", "அமைச்சரவை (Cabinet)"],
                    "rows_en": [
                        ["Size & Scope", "Wider body (60 to 70 ministers across 3 tiers)", "Smaller inner body (15 to 20 cabinet ministers)"],
                        ["Constitutional Status", "Vested under Articles 74 & 75 in original text", "Inserted into Article 352 by 44th CAA 1978"],
                        ["Frequency of Meeting", "Does not meet as a single body to transact business", "Meets regularly (weekly/fortnightly) for decisions"],
                        ["Policy Functions", "Implements policies decided by Cabinet", "Formulates national policy and directs government"],
                        ["Responsibility", "Collectively responsible to Lok Sabha under Art 75(3)", "Enforces collective responsibility of entire Council"]
                    ],
                    "rows_ta": [
                        ["அளவு & எல்லை", "பரந்த அமைப்பு (3 நிலைகளில் 60 முதல் 70 அமைச்சர்கள்)", "சிறிய உள்கட்டமைப்பு அமைப்பு (15 முதல் 20 கேபினட் அமைச்சர்கள்)"],
                        ["அரசியலமைப்பு நிலை", "மூல உரையில் உறுப்புகள் 74 & 75-ன் கீழ் அமைந்தது", "1978-ன் 44வது திருத்தத்தின் மூலம் உறுப்பு 352-ல் சேர்க்கப்பட்டது"],
                        ["கூட்டங்களின் நிகழ்வெண்", "ஆட்சிப் பணிகளைச் செய்ய ஒரே அமைப்பாக ஒன்று கூடுவதில்லை", "முடிவுகளுக்காக வழக்கமாக (வாராந்திரம்) கூட்டுகிறது"],
                        ["கொள்கைப் பணிகள்", "கேபினட் தீர்மானிக்கும் கொள்கைகளைச் செயல்படுத்துகிறது", "தேசியக் கொள்கையை உருவாக்கி அரசாங்கத்தை வழிகாட்டுகிறது"],
                        ["பொறுப்பு", "உறுப்பு 75(3)-ன் கீழ் மக்களவைக்குக் கூட்டாகப் பொறுப்புடையது", "முழு அமைச்சரவையின் கூட்டுப் பொறுப்பை நடைமுறைப்படுத்துகிறது"]
                    ]
                },
                {
                    "id": "comp_pm_vs_cm_functions",
                    "title_en": "4. Prime Minister vs Chief Minister — Functions",
                    "title_ta": "4. பிரதமர் vs முதலமைச்சர் — பணிகள்",
                    "headers_en": ["Function", "Prime Minister of India", "Chief Minister of a State"],
                    "headers_ta": ["பணி", "இந்தியப் பிரதமர்", "மாநில முதலமைச்சர்"],
                    "rows_en": [
                        ["Advisory Link", "Advises President of India (Article 74/78)", "Advises Governor of State (Article 163/167)"],
                        ["National Chairmanships", "Chairs NITI Aayog, Inter-State Council & NDMA", "Member of NITI Aayog Governing Council & Inter-State Council"],
                        ["House Dissolution", "Advises President to dissolve Lok Sabha (Art 85)", "Advises Governor to dissolve Legislative Assembly (Art 174)"],
                        ["Foreign Policy", "Chief architect and spokesman of Indian Foreign Policy", "No role in foreign policy (Union list subject)"]
                    ],
                    "rows_ta": [
                        ["ஆலோசனை இணைப்பு", "இந்தியக் குடியரசுத் தலைவருக்கு அறிவுறுத்துகிறார் (உறுப்பு 74/78)", "மாநில ஆளுநருக்கு அறிவுறுத்துகிறார் (உறுப்பு 163/167)"],
                        ["தேசியத் தலைமைகள்", "நிதி ஆயோக், மாநிலங்களுக்கிடையேயான குழு & NDMA தலைவர்", "நிதி ஆயோக் ஆளும் குழு & மாநிலங்களுக்கிடையேயான குழு உறுப்பினர்"],
                        ["அவைக் கலைப்பு", "மக்களவையைக் கலைக்கக் குடியரசுத் தலைவருக்கு அறிவுறுத்துகிறார்", "சட்டமன்றத்தைக் கலைக்க ஆளுநருக்கு அறிவுறுத்துகிறார்"],
                        ["வெளியுறவுக் கொள்கை", "இந்திய வெளியுறவுக் கொள்கையின் முதன்மை வடிவமைப்பாளர்", "வெளியுறவுக் கொள்கையில் பங்கில்லை (ஒன்றியப் பட்டியல் വിഷயம்)"]
                    ]
                },
                {
                    "id": "comp_collective_vs_individual",
                    "title_en": "5. Collective Responsibility vs Individual Responsibility",
                    "title_ta": "5. கூட்டுப் பொறுப்பு vs தனிப்பட்ட பொறுப்பு",
                    "headers_en": ["Dimension", "Collective Responsibility (Art 75(3))", "Individual Responsibility (Art 75(2))"],
                    "headers_ta": ["பரிமாணம்", "கூட்டுப் பொறுப்பு (உறுப்பு 75(3))", "தனிப்பட்ட பொறுப்பு (உறுப்பு 75(2))"],
                    "rows_en": [
                        ["Constitutional Article", "Article 75(3)", "Article 75(2)"],
                        ["Target Authority", "Responsible collectively to the House of the People (Lok Sabha)", "Responsible individually to the President of India"],
                        ["Operational Principle", "Swim together and sink together; No-confidence motion collapses all", "President removes individual minister on PM's advice"],
                        ["Scope of Enforcement", "If Lok Sabha passes No-Confidence, ALL ministers must resign", "PM can remove uncooperative minister without cabinet falling"]
                    ],
                    "rows_ta": [
                        ["அரசியலமைப்பு விதி", "உறுப்பு 75(3)", "உறுப்பு 75(2)"],
                        ["பொறுப்பான அமைப்பு", "மக்களவைக்கு (Lok Sabha) கூட்டாகப் பொறுப்புடையவர்கள்", "இந்தியக் குடியரசுத் தலைவருக்குத் தனித்தனியாகப் பொறுப்புடையவர்கள்"],
                        ["செயல்முறைக் கோட்பாடு", "ஒன்றாக நீந்துவார்கள், ஒன்றாக மூழ்குவார்கள்; நம்பிக்கையில்லாத் தீர்மானம் அனைவரையும் கலைக்கும்", "பிரதமரின் அறிவுரைப்படி தனிப்பட்ட அமைச்சரைக் குடியரசுத் தலைவர் நீக்குகிறார்"],
                        ["அமலாக்க எல்லை", "மக்களவை நம்பிக்கையில்லாத் தீர்மானத்தை நிறைவேற்றினால், அனைத்து அமைச்சர்களும் ராஜினாமா செய்ய வேண்டும்", "அமைச்சரவை வீழாமல் ஒத்துழைக்காத அமைச்சரைப் பிரதமர் நீக்க முடியும்"]
                    ]
                }
            ],
            "mind_map": [
                {
                    "title": "Prime Minister Powers & Functions (Part V)",
                    "short_label": "PM Part 2 Powers",
                    "children": [
                        {
                            "title": "1. Relation with President",
                            "short_label": "President Link",
                            "children": [
                                {
                                    "title": "Article 78: Duty to inform President on admin & legislation",
                                    "short_label": "Art 78 Info Duty"
                                },
                                {
                                    "title": "Advises President on appointments (CAG, AG, EC, Governors)",
                                    "short_label": "Constitutional Appts"
                                }
                            ]
                        },
                        {
                            "title": "2. Council & Cabinet Leadership",
                            "short_label": "Cabinet Role",
                            "children": [
                                {
                                    "title": "Allocates portfolios & advises minister appointments/dismissals",
                                    "short_label": "Portfolios & Dismissal"
                                },
                                {
                                    "title": "Cabinet vs Council: Art 352 (44th CAA 1978) Cabinet definition",
                                    "short_label": "Council vs Cabinet"
                                }
                            ]
                        },
                        {
                            "title": "3. Parliamentary Leadership",
                            "short_label": "Parliament Role",
                            "children": [
                                {
                                    "title": "Article 85: Advises President on summoning, proroguing & LS dissolution",
                                    "short_label": "Art 85 Dissolution"
                                },
                                {
                                    "title": "Leader of Lok Sabha & Chief spokesman of government policy",
                                    "short_label": "Leader of House"
                                }
                            ]
                        },
                        {
                            "title": "4. Institutional Chairmanships",
                            "short_label": "Ex-Officio Heads",
                            "children": [
                                {
                                    "title": "Chairman of NITI Aayog, Inter-State Council (Art 263), NDMA & NIC",
                                    "short_label": "NITI / ISC / NDMA"
                                }
                            ]
                        }
                    ]
                }
            ],
            "tnpsc_traps": [
                {
                    "title": "1. Cabinet Term Constitutional Insertion Trap (கேபினட் சொல் சேர்க்கைப் பொறி)",
                    "points": {
                        "en": [
                            "TRAP: Believing the word 'Cabinet' was present in the original 1950 Constitution.",
                            "FACT: The word 'Cabinet' was NOT in the original Constitution. It was inserted ONLY into Article 352 by the 44th Constitutional Amendment Act 1978!"
                        ],
                        "ta": [
                            "பொறி: 'Cabinet' என்ற சொல் 1950-ன் மூல அரசியலமைப்பிலேயே இருந்தது என நம்புவது.",
                            "உண்மை: 'Cabinet' என்ற சொல் மூல அரசியலமைப்பில் இல்லை. 1978-ன் 44வது அரசியலமைப்புத் திருத்தச் சட்டத்தின் மூலம் உறுப்பு 352-ல் மட்டுமே சேர்க்கப்பட்டது!"
                        ]
                    }
                },
                {
                    "title": "2. Article 74 vs Article 78 Trap (உறுப்பு 74 vs உறுப்பு 78 பொறி)",
                    "points": {
                        "en": [
                            "TRAP: Confusing Article 74 (Aid and advice requirement) with Article 78 (PM's duties to inform President).",
                            "FACT: Article 74 specifies Council of Ministers aids and advises President; Article 78 specifies duties of PM to communicate decisions to President!"
                        ],
                        "ta": [
                            "பொறி: உறுப்பு 74 (உதவி & அறிவுரை) மற்றும் உறுப்பு 78 (குடியரசுத் தலைவருக்குத் தகவல் தெரிவிக்கும் பிரதமரின் கடமை) ஆகியவற்றை குழப்பிக் கொள்ளுதல்.",
                            "உண்மை: உறுப்பு 74 அமைச்சரவை உதவி & அறிவுரை வழங்குவதைக் கூறுகிறது; உறுப்பு 78 குடியரசுத் தலைவருக்கு முடிவுகளைத் தெரிவிக்கும் பிரதமரின் கடமைகளைக் கூறுகிறது!"
                        ]
                    }
                },
                {
                    "title": "3. Individual vs Collective Responsibility Trap (தனிப்பட்ட vs கூட்டுப் பொறுப்புப் பொறி)",
                    "points": {
                        "en": [
                            "TRAP: Believing Ministers are collectively responsible to the President of India.",
                            "FACT: Ministers are COLLECTIVELY responsible to Lok Sabha (Art 75(3)), but INDIVIDUALLY responsible to the President (Art 75(2))!"
                        ],
                        "ta": [
                            "பொறி: அமைச்சர்கள் இந்தியக் குடியரசுத் தலைவருக்குக் கூட்டாகப் பொறுப்புடையவர்கள் என நினைப்பது.",
                            "உண்மை: அமைச்சர்கள் மக்களவைக்குக் கூட்டாகப் பொறுப்புடையவர்கள் (உறுப்பு 75(3)), ஆனால் குடியரசுத் தலைவருக்குத் தனித்தனியாகப் பொறுப்புடையவர்கள் (உறுப்பு 75(2))!"
                        ]
                    }
                },
                {
                    "title": "4. Parliamentary Responsibility House Trap (நாடாளுமன்றப் பொறுப்பு அவை பொறி)",
                    "points": {
                        "en": [
                            "TRAP: Assuming Council of Ministers is collectively responsible to both Houses of Parliament equally.",
                            "FACT: Council of Ministers is collectively responsible strictly ONLY to the House of the People (LOK SABHA) under Article 75(3), NOT Rajya Sabha!"
                        ],
                        "ta": [
                            "பொறி: அமைச்சரவை நாடாளுமன்றத்தின் இரு அவைகளுக்கும் சமமாகக் கூட்டாகப் பொறுப்புடையது என நினைப்பது.",
                            "உண்மை: அமைச்சரவை உறுப்பு 75(3)-ன் கீழ் மக்களவைக்கு (LOK SABHA) மட்டுமே கூட்டாகப் பொறுப்புடையது, மாநிலங்களவைக்கு அல்ல!"
                        ]
                    }
                },
                {
                    "title": "5. Lok Sabha Dissolution Power Trap (மக்களவைக் கலைப்பு அதிகாரப் பொறி)",
                    "points": {
                        "en": [
                            "TRAP: Assuming President can dissolve Lok Sabha independently without PM's advice.",
                            "FACT: President dissolves Lok Sabha under Article 85(2)(b) ONLY on the advice of the Prime Minister!"
                        ],
                        "ta": [
                            "பொறி: பிரதமரின் அறிவுரை இன்றி குடியரசுத் தலைவர் சுதந்திரமாக மக்களவையைக் கலைக்க முடியும் என நினைப்பது.",
                            "உண்மை: உறுப்பு 85(2)(b)-ன் கீழ் பிரதமரின் அறிவுரையின் பேரில் மட்டுமே குடியரசுத் தலைவர் மக்களவையைக் கலைக்கிறார்!"
                        ]
                    }
                },
                {
                    "title": "6. Constitutional Authority vs Statutory Chairmanship Trap (அரசியலமைப்பு vs சட்டப்பூர்வத் தலைமைப் பொறி)",
                    "points": {
                        "en": [
                            "TRAP: Believing NITI Aayog is a constitutional body created under Article 78.",
                            "FACT: NITI Aayog is a non-constitutional, non-statutory executive body created by Cabinet resolution; PM is its Ex-officio Chairman."
                        ],
                        "ta": [
                            "பொறி: நிதி ஆயோக் என்பது உறுப்பு 78-ன் கீழ் உருவாக்கப்பட்ட ஓர் அரசியலமைப்பு அமைப்பு எனக் கருதுவது.",
                            "உண்மை: நிதி ஆயோக் என்பது கேபினட் தீர்மானத்தால் உருவாக்கப்பட்ட அரசியலமைப்பற்ற, சட்டப்பூர்வமற்ற நிர்வாக அமைப்பாகும்; பிரதமர் இதன் பதவிவழித் தலைவராவார்."
                        ]
                    }
                }
            ],
            "important_facts": {
                "en": [
                    "Article 78 details the constitutional duties of Prime Minister to communicate cabinet decisions and furnish administrative info to President.",
                    "The word 'Cabinet' was inserted into Article 352 of Constitution by the 44th Constitutional Amendment Act 1978.",
                    "Council of Ministers (Articles 74 & 75) is a wider body of 60-70 ministers, whereas Cabinet is a smaller core body of 15-20 senior ministers.",
                    "Under Article 75(3), Council of Ministers is collectively responsible strictly to Lok Sabha (House of the People).",
                    "Under Article 75(2), ministers hold office individually during the pleasure of President (individual responsibility).",
                    "Prime Minister advises President on dissolving Lok Sabha under Article 85(2)(b).",
                    "Prime Minister is Ex-officio Chairman of NITI Aayog, Inter-State Council (Art 263), National Integration Council, and NDMA.",
                    "Resignation or death of Prime Minister automatically causes dissolution of Council of Ministers."
                ],
                "ta": [
                    "உறுப்பு 78 அமைச்சரவை முடிவுகளைத் தெரிவிப்பது மற்றும் நிர்வாகத் தகவல்களைக் குடியரசுத் தலைவருக்கு வழங்குவது தொடர்பான பிரதமரின் அரசியலமைப்பு கடமைகளை விவரிக்கிறது.",
                    "1978-ன் 44வது அரசியலமைப்புத் திருத்தச் சட்டத்தின் மூலம் அரசியலமைப்பின் உறுப்பு 352-ல் 'Cabinet' என்ற சொல் சேர்க்கப்பட்டது.",
                    "அமைச்சர்கள் குழு (உறுப்புகள் 74 & 75) என்பது 60-70 அமைச்சர்களைக் கொண்ட பரந்த அமைப்பு, ஆனால் கேபினட் என்பது 15-20 மூத்த அமைச்சர்களைக் கொண்ட சிறிய உள்கட்டமைப்பு.",
                    "உறுப்பு 75(3)-ன் கீழ் அமைச்சரவை மக்களவைக்கு (House of the People) மட்டுமே கூட்டாகப் பொறுப்புடையது.",
                    "உறுப்பு 75(2)-ன் கீழ் அமைச்சர்கள் தனித்தனியாகக் குடியரசுத் தலைவரின் விருப்பம் உள்ளவரை பதவி வகிக்கின்றனர் (தனிப்பட்ட பொறுப்பு).",
                    "உறுப்பு 85(2)(b)-ன் கீழ் மக்களவையைக் கலைப்பது குறித்துப் பிரதமர் குடியரசுத் தலைவருக்கு அறிவுறுத்துகிறார்.",
                    "பிரதமர் நிதி ஆயோக், மாநிலங்களுக்கிடையேயான குழு (உறுப்பு 263), தேசிய ஒருமைப்பாட்டுக் குழு மற்றும் NDMA ஆகியவற்றின் பதவிவழித் தலைவராவார்.",
                    "பிரதமரின் ராஜினாமா அல்லது இறப்பு தானாகவே அமைச்சரவையைக் கலைக்க வழிவகுக்கும்."
                ]
            },
            "quick_revision": {
                "en": [
                    "Article 78: PM's duty to inform President on admin decisions, legislative proposals, & submit individual minister decisions to Cabinet.",
                    "Constitutional Appointments: PM advises President on CAG, AG, CEC/ECs, UPSC, Finance Commission & Governors.",
                    "Council vs Cabinet: Council (Art 74/75, 60-70 mins, 3 tiers) vs Cabinet (Art 352 post 44th CAA 1978, 15-20 senior mins).",
                    "Responsibility: Collective responsibility to Lok Sabha (Art 75(3)); Individual responsibility to President (Art 75(2)).",
                    "Parliament: PM advises President under Art 85 to summon, prorogue & dissolve Lok Sabha.",
                    "Chairmanships: Ex-officio Chairman of NITI Aayog, Inter-State Council (Art 263), NDMA (2005 Act), National Integration Council.",
                    "Resignation Effect: PM's resignation/death dissolves entire Council of Ministers instantly."
                ],
                "ta": [
                    "உறுப்பு 78: நிர்வாக முடிவுகள், சட்ட முன்மொழிவுகள் குறித்து குடியரசுத் தலைவருக்குத் தெரிவிப்பது & தனி அமைச்சர் முடிவைக் கேபினட் பரிசீலனைக்கு அளிப்பது பிரதமரின் கடமை.",
                    "அரசியலமைப்பு நியமனங்கள்: CAG, AG, CEC/ECs, UPSC, நிதி ஆணையம் & ஆளுநர்கள் நியமனத்தில் குடியரசுத் தலைவருக்குப் பிரதமர் அறிவுறுத்துகிறார்.",
                    "Council vs Cabinet: அமைச்சர்கள் குழு (உறுப்பு 74/75, 60-70 அமைச்சர்கள், 3 நிலைகள்) vs கேபினட் (44வது CAA 1978க்கு பின் உறுப்பு 352, 15-20 மூத்த அமைச்சர்கள்).",
                    "பொறுப்பு: மக்களவைக்குக் கூட்டுப் பொறுப்பு (உறுப்பு 75(3)); குடியரசுத் தலைவருக்குத் தனிப்பட்ட பொறுப்பு (உறுப்பு 75(2)).",
                    "நாடாளுமன்றம்: உறுப்பு 85-ன் கீழ் மக்களவையைக் கூட்ட, ஒத்திவைக்க & கலைக்கப் பிரதமர் குடியரசுத் தலைவருக்கு அறிவுறுத்துகிறார்.",
                    "தலைமைப் பொறுப்புகள்: நிதி ஆயோக், மாநிலங்களுக்கிடையேயான குழு (உறுப்பு 263), NDMA (2005 சட்டம்), தேசிய ஒருமைப்பாட்டுக் குழு ஆகியவற்றின் பதவிவழித் தலைவர்.",
                    "ராஜினாமா தாக்கம்: பிரதமரின் ராஜினாமா/இறப்பு உடனடி முழு அமைச்சரவையையும் கலைக்கும்."
                ]
            },
            "revision_cards": [
                {
                    "title": "Article 78(a)",
                    "content_en": "PM duty to communicate all Council decisions to President.",
                    "content_ta": "அமைச்சரவையின் அனைத்து முடிவுகளையும் குடியரசுத் தலைவருக்குத் தெரிவிக்கும் பிரதமரின் கடமை."
                },
                {
                    "title": "Article 78(b)",
                    "content_en": "PM duty to furnish admin & legislative info requested by President.",
                    "content_ta": "குடியரசுத் தலைவர் கோரும் நிர்வாக & சட்ட தகவல்களை வழங்கும் பிரதமரின் கடமை."
                },
                {
                    "title": "Article 78(c)",
                    "content_en": "President can ask PM to submit single minister decision to Council.",
                    "content_ta": "தனி அமைச்சர் முடிவைக் அமைச்சரவையின் பரிசீலனைக்கு அளிக்க குடியரசுத் தலைவர் கோரலாம்."
                },
                {
                    "title": "44th CAA 1978",
                    "content_en": "Inserted the word 'Cabinet' into Article 352 of Indian Constitution.",
                    "content_ta": "இந்திய அரசியலமைப்பின் உறுப்பு 352-ல் 'Cabinet' என்ற சொல்லைச் சேர்த்தது."
                },
                {
                    "title": "Article 75(3)",
                    "content_en": "Council of Ministers collectively responsible strictly to Lok Sabha.",
                    "content_ta": "அமைச்சரவை மக்களவைக்கு மட்டுமே கூட்டாகப் பொறுப்புடையது."
                },
                {
                    "title": "Article 75(2)",
                    "content_en": "Ministers hold office individually during pleasure of President.",
                    "content_ta": "அமைச்சர்கள் தனித்தனியாகக் குடியரசுத் தலைவரின் விருப்பம் உள்ளவரை பதவி வகிக்கின்றனர்."
                },
                {
                    "title": "Article 85 Dissolution",
                    "content_en": "President dissolves Lok Sabha on advice of Prime Minister.",
                    "content_ta": "பிரதமரின் அறிவுரைப்படி குடியரசுத் தலைவர் மக்களவையைக் கலைக்கிறார்."
                },
                {
                    "title": "NITI Aayog Chairman",
                    "content_en": "Prime Minister is Ex-officio Chairman of NITI Aayog.",
                    "content_ta": "பிரதமர் நிதி ஆயோக்கின் பதவிவழித் தலைவராவார்."
                },
                {
                    "title": "Inter-State Council",
                    "content_en": "PM is Chairman of Inter-State Council created under Article 263.",
                    "content_ta": "உறுப்பு 263-ன் கீழ் அமைக்கப்பட்ட மாநிலங்களுக்கிடையேயான குழுவின் தலைவர் பிரதமர்."
                },
                {
                    "title": "NDMA Chairman",
                    "content_en": "PM is Chairman of National Disaster Management Authority (NDMA).",
                    "content_ta": "பிரதமர் தேசிய பேரிடர் மேலாண்மை ஆணையத்தின் (NDMA) தலைவராவார்."
                }
            ]
        }
    }
    return part2_data

def validate_part2(data):
    meta = data.get("meta", {})
    assert meta.get("topic_id") == "polity_prime_minister_part_2", f"Invalid topic_id: {meta.get('topic_id')}"
    assert meta.get("part") == 2, f"Invalid part: {meta.get('part')}"
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
    assert len(traps) >= 6, f"Expected at least 6 TNPSC traps, got {len(traps)}"
    
    rev = content.get("revision_cards", [])
    assert len(rev) >= 10, f"Expected at least 10 revision cards, got {len(rev)}"

    assert content.get("important_facts", {}).get("en") and content.get("important_facts", {}).get("ta")
    assert content.get("quick_revision", {}).get("en") and content.get("quick_revision", {}).get("ta")
    print("✅ PART 2 VALIDATION PASSED COMPLETELY!")

def main():
    print("==================================================")
    print("GENERATING & VALIDATING PRIME MINISTER PART 2 NOTES")
    print("==================================================")
    data = generate_part2()
    validate_part2(data)
    
    out_dir = "data/notes/polity"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "prime_minister_part_2.json")
    
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
    assert os.path.exists(out_path), f"File was not created at {out_path}"
    print(f"✅ SAVED IMMEDIATELY & CONFIRMED FILE EXISTS: {out_path}")

if __name__ == "__main__":
    main()
