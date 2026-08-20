# build_preamble_part1_notes.py
import json
import os
import shutil

def generate_preamble_part1_payload():
    note = {
        "meta": {
            "topic_id": "polity_preamble_part_1",
            "repository_id": "polity_preamble",
            "display_title": "Preamble of the Constitution of India – Part 1",
            "part": 1,
            "total_parts": 2,
            "subject": "polity",
            "chapter": "Preamble of the Constitution of India",
            "language": "English + Tamil"
        },
        "metadata": {
            "version": "1.0",
            "status": "approved",
            "review_status": "gold_standard",
            "difficulty": "foundation",
            "estimated_study_time": {
                "reading": "25 min",
                "revision": "10 min",
                "total": "35 min"
            }
        },
        "keywords": [
            "Preamble of Indian Constitution",
            "அரசியலமைப்பின் முகவுரை",
            "We the People of India",
            "இந்திய மக்களாகிய நாம்",
            "Popular Sovereignty",
            "மக்களின் இறையாண்மை",
            "Sovereign",
            "இறையாண்மை கொண்ட",
            "Socialist",
            "சமதர்ம",
            "Secular",
            "மதச்சார்பற்ற",
            "Democratic",
            "ஜனநாயக",
            "Republic",
            "குடியரசு",
            "Justice",
            "நீதி",
            "Liberty",
            "சுதந்திரம்",
            "Equality",
            "சமத்துவம்",
            "Fraternity",
            "சகோதரத்துவம்",
            "42nd Amendment Act 1976",
            "42வது திருத்தச் சட்டம் 1976"
        ],
        "learning_outcomes": {
            "Understand": {
                "en": [
                    "Understand the meaning, purpose, and constitutional philosophy expressed in the Preamble.",
                    "Understand the concept of Popular Sovereignty embodied in 'We, the People of India'.",
                    "Understand the five key attributes defining the Nature of the Indian State (Sovereign, Socialist, Secular, Democratic, Republic).",
                    "Understand the four fundamental Objectives of the Constitution (Justice, Liberty, Equality, Fraternity)."
                ],
                "ta": [
                    "முகவுரையில் வெளிப்படுத்தப்பட்டுள்ள பொருள், நோக்கம் மற்றும் அரசியலமைப்பு தத்துவத்தைப் புரிந்துகொள்ளுதல்.",
                    "'இந்திய மக்களாகிய நாம்' என்ற தொடரில் பொதிந்துள்ள மக்களின் இறையாண்மை கருத்தைப் புரிந்துகொள்ளுதல்.",
                    "இந்திய அரசின் தன்மையை வரையறுக்கும் ஐந்து முக்கிய பண்புகளை (இறையாண்மை, சமதர்ம, மதச்சார்பற்ற, ஜனநாயக, குடியரசு) புரிந்துகொள்ளுதல்.",
                    "அரசியலமைப்பின் நான்கு அடிப்படை இலக்குகளை (நீதி, சுதந்திரம், சமத்துவம், சகோதரத்துவம்) புரிந்துகொள்ளுதல்."
                ]
            },
            "Remember": {
                "en": [
                    "Remember the exact order of State attributes: Sovereign, Socialist, Secular, Democratic, Republic (S-S-S-D-R).",
                    "Remember the exact order of Objectives: Justice, Liberty, Equality, Fraternity (J-L-E-F).",
                    "Remember that 'Socialist', 'Secular', and 'Integrity' were added by the 42nd Amendment Act, 1976.",
                    "Remember the historical origin of Preamble in Pandit Nehru's Objectives Resolution (moved Dec 13, 1946; adopted Jan 22, 1947)."
                ],
                "ta": [
                    "அரசின் பண்புகளின் துல்லியமான வரிசையை நினைவில் கொள்ளுதல்: இறையாண்மை, சமதர்ம, மதச்சார்பற்ற, ஜனநாயக, குடியரசு.",
                    "இலக்குகளின் துல்லியமான வரிசையை நினைவில் கொள்ளுதல்: நீதி, சுதந்திரம், சமத்துவம், சகோதரத்துவம்.",
                    "'சமதர்ம', 'மதச்சார்பற்ற' மற்றும் 'ஒருமைப்பாடு' ஆகிய சொற்கள் 1976 இன் 42வது திருத்தச் சட்டத்தால் சேர்க்கப்பட்டதை நினைவில் கொள்ளுதல்.",
                    "பண்டிட் நேருவின் குறிக்கோள் தீர்மானத்தில் (டிசம்பர் 13, 1946 இல் முன்மொழியப்பட்டு ஜனவரி 22, 1947 இல் ஏற்றுக்கொள்ளப்பட்டது) முகவுரையின் வரலாற்று மூலத்தை நினைவில் கொள்ளுதல்."
                ]
            },
            "Analyze": {
                "en": [
                    "Analyze why Indian Secularism is a positive concept (Sarva Dharma Sambhava) unlike Western negative secularism.",
                    "Analyze the crucial distinction between Democracy (popular mandate) and Republic (elected Head of State).",
                    "Analyze why Liberty in the Preamble is not absolute but subject to reasonable constitutional restrictions."
                ],
                "ta": [
                    "மேற்கத்திய எதிர்மறை மதச்சார்பின்மையைப் போலல்லாமல் இந்திய மதச்சார்பின்மை ஏன் ஒரு நேர்மறையான கருத்து (சர்வ தர்ம சம்பவ) என்பதை பகுப்பாய்வு செய்தல்.",
                    "ஜனநாயகம் (மக்கள் வாக்குரிமை) மற்றும் குடியரசு (தேர்ந்தெடுக்கப்பட்ட நாட்டின் தலைவர்) இடையேயான முக்கிய வேறுபாட்டை பகுப்பாய்வு செய்தல்.",
                    "முகவுரையில் உள்ள சுதந்திரம் ஏன் வரம்பற்றது அல்ல, அரசியலமைப்பு கட்டுப்பாடுகளுக்கு உட்பட்டது என்பதை பகுப்பாய்வு செய்தல்."
                ]
            },
            "Apply": {
                "en": [
                    "Identify TNPSC trap points regarding amendment years, non-synonymous terms, and source of authority.",
                    "Connect Preamble objectives directly to Fundamental Rights (Part III), DPSP (Part IV), and Fundamental Duties (Part IVA)."
                ],
                "ta": [
                    "திருத்த ஆண்டுகள், இணையான சொற்கள் அல்லாதவைகளை வேறுபடுத்துதல் மற்றும் அதிகாரத்தின் மூலம் பற்றிய டிஎன்பிஎஸ்சி பொறி புள்ளிகளைக் கண்டறிதல்.",
                    "முகவுரை இலக்குகளை அடிப்படை உரிமைகள் (பகுதி III), DPSP (பகுதி IV) மற்றும் அடிப்படை கடமைகளுடன் (பகுதி IVA) நேரடியாக இணைத்தல்."
                ]
            }
        },
        "subject": "Polity",
        "topic": "Preamble of the Constitution of India – Part 1",
        "language": "bilingual",
        "ui_type": "polity",
        "sections": [
            {
                "id": "sec_what_is_preamble",
                "title_en": "1. What is the Preamble?",
                "title_ta": "1. முகவுரை என்றால் என்ன?",
                "type": "standard_topic"
            },
            {
                "id": "sec_source_of_authority",
                "title_en": "2. Source of Authority: 'WE, THE PEOPLE OF INDIA'",
                "title_ta": "2. அதிகாரத்தின் மூலம்: 'இந்திய மக்களாகிய நாம்'",
                "type": "standard_topic"
            },
            {
                "id": "sec_sovereign",
                "title_en": "3. Nature of State: SOVEREIGN (இறையாண்மை)",
                "title_ta": "3. அரசின் தன்மை: இறையாண்மை கொண்ட (SOVEREIGN)",
                "type": "standard_topic"
            },
            {
                "id": "sec_socialist",
                "title_en": "4. Nature of State: SOCIALIST (சமதர்ம)",
                "title_ta": "4. அரசின் தன்மை: சமதர்ம (SOCIALIST)",
                "type": "standard_topic"
            },
            {
                "id": "sec_secular",
                "title_en": "5. Nature of State: SECULAR (மதச்சார்பற்ற)",
                "title_ta": "5. அரசின் தன்மை: மதச்சார்பற்ற (SECULAR)",
                "type": "standard_topic"
            },
            {
                "id": "sec_democratic",
                "title_en": "6. Nature of State: DEMOCRATIC (ஜனநாயக)",
                "title_ta": "6. அரசின் தன்மை: ஜனநாயக (DEMOCRATIC)",
                "type": "standard_topic"
            },
            {
                "id": "sec_republic",
                "title_en": "7. Nature of State: REPUBLIC (குடியரசு)",
                "title_ta": "7. அரசின் தன்மை: குடியரசு (REPUBLIC)",
                "type": "standard_topic"
            },
            {
                "id": "sec_justice",
                "title_en": "8. Objectives of Constitution: JUSTICE (நீதி)",
                "title_ta": "8. அரசியலமைப்பின் இலக்குகள்: நீதி (JUSTICE)",
                "type": "standard_topic"
            },
            {
                "id": "sec_liberty",
                "title_en": "9. Objectives of Constitution: LIBERTY (சுதந்திரம்)",
                "title_ta": "9. அரசியலமைப்பின் இலக்குகள்: சுதந்திரம் (LIBERTY)",
                "type": "standard_topic"
            },
            {
                "id": "sec_equality",
                "title_en": "10. Objectives of Constitution: EQUALITY (சமத்துவம்)",
                "title_ta": "10. அரசியலமைப்பின் இலக்குகள்: சமத்துவம் (EQUALITY)",
                "type": "standard_topic"
            },
            {
                "id": "sec_fraternity",
                "title_en": "11. Objectives of Constitution: FRATERNITY (சகோதரத்துவம்)",
                "title_ta": "11. அரசியலமைப்பின் இலக்குகள்: சகோதரத்துவம் (FRATERNITY)",
                "type": "standard_topic"
            },
            {
                "id": "sec_concept_connections",
                "title_en": "12. Key Concept Connections & Architecture",
                "title_ta": "12. முக்கிய கருத்துத் தொடர்புகள் மற்றும் கட்டமைப்பு",
                "type": "standard_topic"
            }
        ],
        "content": {
            "definition": {
                "en": "The Preamble is the introductory statement of the Constitution of India that outlines its source of authority, the nature of the Indian State, its fundamental socio-political objectives, and the historic date of adoption (26th November 1949). It represents the 'identity card' and philosophical key to the mind of the constitutional framers.",
                "ta": "முகவுரை என்பது இந்திய அரசியலமைப்பின் அறிமுக உரையாகும், இது அரசியலமைப்பு அதிகாரத்தின் மூலம், இந்திய அரசின் தன்மை, அதன் அடிப்படை சமூக-அரசியல் இலக்குகள் மற்றும் ஏற்றுக்கொள்ளப்பட்ட வரலாற்று நாள் (26 நவம்பர் 1949) ஆகியவற்றை விவரிக்கிறது. இது அரசியலமைப்புச் சிற்பிகளின் சிந்தனையைத் திறக்கும் சாவி மற்றும் அரசியலமைப்பின் 'அடையாள அட்டை'யாகச் செயல்படுகிறது."
            },
            "introduction": {
                "en": "The Preamble to the Indian Constitution is based on the historic 'Objectives Resolution', drafted and moved by Pandit Jawaharlal Nehru on December 13, 1946, and unanimously adopted by the Constituent Assembly on January 22, 1947. Part 1 establishes the conceptual foundation of the Preamble by dissecting the Source of Authority, the five attributes of the Indian Republic (Sovereign, Socialist, Secular, Democratic, Republic), and the four core noble Objectives (Justice, Liberty, Equality, Fraternity).",
                "ta": "இந்திய அரசியலமைப்பின் முகவுரை, 1946 டிசம்பர் 13 அன்று பண்டிட் ஜவஹர்லால் நேருவால் உருவாக்கப்பட்டு முன்மொழியப்பட்ட வரலாற்றுச் சிறப்புமிக்க 'குறிக்கோள் தீர்மானத்தின்' அடிப்படையில் அமைக்கப்பட்டது, இது 1947 ஜனவரி 22 அன்று அரசியலமைப்புச் சபையால் ஏகமனதாக ஏற்றுக்கொள்ளப்பட்டது. பகுதி 1 முகவுரையின் அதிகார மூலம், இந்தியக் குடியரசின் ஐந்து பண்புகள் (இறையாண்மை, சமதர்ம, மதச்சார்பற்ற, ஜனநாயக, குடியரசு) மற்றும் நான்கு உன்னத இலக்குகள் (நீதி, சுதந்திரம், சமத்துவம், சகோதரத்துவம்) ஆகியவற்றை ஆழமாக விளக்குகிறது."
            },
            "sec_what_is_preamble": [
                {
                    "title": "1. Meaning and Purpose of a Preamble (முகவுரையின் பொருளும் நோக்கமும்)",
                    "points": {
                        "en": [
                            "Meaning: The term 'Preamble' refers to the introduction or preface to the Constitution. It contains the summary or essence of the Constitution.",
                            "American Precedent: The American Constitution was the first in the world to begin with a Preamble. India followed this constitutional tradition.",
                            "Identity Card of the Constitution: Eminent jurist and constitutional expert N.A. Palkhivala called the Preamble the 'Identity Card of the Constitution'.",
                            "Four Key Ingredients of Preamble:\n1. Source of Authority: Derives authority from 'We, the People of India'.\n2. Nature of Indian State: Declares India as Sovereign, Socialist, Secular, Democratic, Republic.\n3. Objectives of Constitution: Specifies Justice, Liberty, Equality, and Fraternity.\n4. Date of Adoption: Mentions 26th November 1949."
                        ],
                        "ta": [
                            "பொருள்: 'முகவுரை' (Preamble) என்ற சொல் அரசியலமைப்பின் அறிமுகம் அல்லது முன்னுரையைக் குறிக்கிறது. இது அரசியலமைப்பின் சுருக்கம் அல்லது சாராம்சத்தைக் கொண்டுள்ளது.",
                            "அமெரிக்க முன்னுதாரணம்: உலகிலேயே முதன்முதலில் முகவுரையுடன் அமைந்த அரசியலமைப்பு அமெரிக்க அரசியலமைப்பாகும். இந்தியா இந்த அரசியலமைப்பு மரபைப் பின்பற்றியது.",
                            "அரசியலமைப்பின் அடையாள அட்டை: பிரபல சட்ட நிபுணர் என்.ஏ. பால்கிவாலா முகவுரையை 'அரசியலமைப்பின் அடையாள அட்டை' என்று அழைத்தார்.",
                            "முகவுரையின் நான்கு முக்கிய கூறுகள்:\n1. அதிகாரத்தின் மூலம்: 'இந்திய மக்களாகிய நாம்' என்பதிலிருந்து அதிகாரத்தைப் பெறுகிறது.\n2. இந்திய அரசின் தன்மை: இந்தியாவை இறையாண்மை, சமதர்ம, மதச்சார்பற்ற, ஜனநாயக, குடியரசு நாடாக அறிவிக்கிறது.\n3. அரசியலமைப்பின் இலக்குகள்: நீதி, சுதந்திரம், சமத்துவம் மற்றும் சகோதரத்துவத்தைக் குறிப்பிடுகிறது.\n4. ஏற்றுக்கொள்ளப்பட்ட நாள்: 26 நவம்பர் 1949 ஐக் குறிப்பிடுகிறது."
                        ]
                    }
                },
                {
                    "title": "2. Philosophical Significance (அரசியலமைப்பு தத்துவ முக்கியத்துவம்)",
                    "points": {
                        "en": [
                            "Key to Framers' Mind: As observed by Sir Alladi Krishnaswami Ayyar, 'The Preamble to our Constitution expresses what we had thought or dreamed so long.'",
                            "Horoscope of Sovereign Democratic Republic: K.M. Munshi described the Preamble as the 'Horoscope of our Sovereign Democratic Republic'.",
                            "Jewel Set in Constitution: Pandit Thakur Das Bhargava stated: 'The Preamble is the most precious part of the Constitution. It is the soul of the Constitution. It is a key to the Constitution.'",
                            "Interpretative Light: Whenever any constitutional provision is ambiguous, the Supreme Court uses the Preamble to interpret the true intention of the framers."
                        ],
                        "ta": [
                            "வரைவாளர்களின் சிந்தனைக் திறவுகோல்: சர் அல்லாடி கிருஷ்ணசாமி ஐயர் குறிப்பிட்டது போல, 'நமது அரசியலமைப்பின் முகவுரை நாம் இவ்வளவு காலம் சிந்தித்ததை அல்லது கனவு கண்டதை வெளிப்படுத்துகிறது.'",
                            "இறையாண்மை ஜனநாயகக் குடியரசின் ஜாதகம்: கே.எம். முன்ஷி முகவுரையை நமது 'இறையாண்மை ஜனநாயகக் குடியரசின் ஜாதகம்' என்று விவரித்தார்.",
                            "அரசியலமைப்பில் பதிக்கப்பட்ட மாணிக்கம்: பண்டிட் தாக்கூர் தாஸ் பார்கவா கூறினார்: 'முகவுரை அரசியலமைப்பின் மிக விலையுயர்ந்த பகுதியாகும். இது அரசியலமைப்பின் ஆன்மா. இது அரசியலமைப்பின் சாவி.'",
                            "விளக்கமளிக்கும் ஒளி: எந்தவொரு அரசியலமைப்பு விதியும் தெளிவற்றதாக இருக்கும்போதெல்லாம், வரைவாளர்களின் உண்மையான நோக்கத்தை விளக்குவதற்கு உச்ச நீதிமன்றம் முகவுரையைப் பயன்படுத்துகிறது."
                        ]
                    }
                }
            ],
            "sec_source_of_authority": [
                {
                    "title": "1. Popular Sovereignty & Democratic Foundation (மக்களின் இறையாண்மை)",
                    "points": {
                        "en": [
                            "The opening words of the Preamble — 'WE, THE PEOPLE OF INDIA' — explicitly locate the ultimate source of constitutional authority in the citizens of India.",
                            "Popular Sovereignty: Means that the Constitution is not a gift or decree granted by the British Crown, British Parliament, or an external monarch. It was enacted, adopted, and given to themselves by the sovereign people of India.",
                            "Democratic Foundation: Establishes that all state organs (Legislature, Executive, Judiciary) derive their authority directly or indirectly from the people.",
                            "Constitutional Mandate: The ultimate power resides in the people, and the government remains accountable to the people through periodic elections based on Universal Adult Franchise (Article 326)."
                        ],
                        "ta": [
                            "முகவுரையின் தொடக்கச் சொற்களான — 'இந்திய மக்களாகிய நாம்' — அரசியலமைப்பு அதிகாரத்தின் இறுதி மூலத்தை இந்தியக் குடிமக்களிடம் வெளிப்படையாக அமைக்கிறது.",
                            "மக்களின் இறையாண்மை: அரசியலமைப்பு என்பது பிரிட்டிஷ் முடிசூட்டு மன்னராலோ, பிரிட்டிஷ் நாடாளுமன்றத்தாலோ அல்லது வெளிநாட்டு ஆட்சியாளராலோ வழங்கப்பட்ட கொடை அல்ல. இது இறையாண்மை கொண்ட இந்திய மக்களால் உருவாக்கப்பட்டு, ஏற்றுக்கொள்ளப்பட்டு, தங்களுக்குத்தானே வழங்கப்பட்டதாகும்.",
                            "ஜனநாயக அடித்தளம்: அனைத்து அரசு உறுப்புகளும் (சட்டமன்றம், நிர்வாகம், நீதித்துறை) நேரடியாகவோ அல்லது மறைமுகமாகவோ மக்களிடமிருந்தே அதிகாரத்தைப் பெறுகின்றன என்பதை நிறுவுகிறது.",
                            "அரசியலமைப்பு ஆணை: இறுதி அதிகாரம் மக்களிடம் உள்ளது, மேலும் அரசாங்கம் உலகளாவிய வயதுவந்தோர் வாக்குரிமை (உறுப்பு 326) அடிப்படையிலான காலமுறை தேர்தல்கள் மூலம் மக்களுக்குப் பொறுப்பாக உள்ளது."
                        ]
                    }
                },
                {
                    "title": "2. TNPSC Exam Relevance & Trap Point (டிஎன்பிஎஸ்சி தேர்வு நோக்கு & பொறி)",
                    "points": {
                        "en": [
                            "TNPSC Question Pattern: Who is the ultimate source of authority under the Indian Constitution? Option A: Parliament, Option B: Supreme Court, Option C: President, Option D: We, the People of India. Correct Answer: D.",
                            "TNPSC Trap: Do NOT select Parliament or Supreme Court. Parliament is a creature of the Constitution; the Constitution itself derives authority from the PEOPLE.",
                            "Key Revision Line: Sovereign power in India resides in the People of India, NOT in Parliament."
                        ],
                        "ta": [
                            "டிஎன்பிஎஸ்சி வினா மாதிரி: இந்திய அரசியலமைப்பின் கீழ் அதிகாரத்தின் இறுதி மூலம் யார்? விருப்பம் A: நாடாளுமன்றம், விருப்பம் B: உச்ச நீதிமன்றம், விருப்பம் C: குடியரசுத் தலைவர், விருப்பம் D: இந்திய மக்களாகிய நாம். சரியான விடை: D.",
                            "டிஎன்பிஎஸ்சி பொறி: நாடாளுமன்றம் அல்லது உச்ச நீதிமன்றத்தைத் தேர்ந்தெடுக்க வேண்டாம். நாடாளுமன்றம் அரசியலமைப்பால் உருவாக்கப்பட்ட ஒரு அமைப்பு; அரசியலமைப்பு 자체가 மக்களிடமிருந்தே அதிகாரத்தைப் பெறுகிறது.",
                            "முக்கிய திருப்புதல் வரி: இந்தியாவில் இறையாண்மை அதிகாரம் நாடாளுமன்றத்தில் இல்லை, இந்திய மக்களிடம் மட்டுமே உள்ளது."
                        ]
                    }
                }
            ],
            "sec_sovereign": [
                {
                    "title": "1. Concept & Constitutional Meaning (இறையாண்மை என்பதன் பொருள்)",
                    "points": {
                        "en": [
                            "Meaning: 'Sovereign' implies that India is an independent nation. It is neither a dependency nor a dominion of any other nation.",
                            "Dual Dimension of Sovereignty:\n1. Internal Sovereignty: India has absolute authority to make laws for its territory and govern its citizens without internal superior power.\n2. External Sovereignty: India is free from any external control, direction, or subordination to foreign powers.",
                            "Freedom of Territory: Being a sovereign state, India can either acquire a foreign territory or cede a part of its territory in favor of a foreign state (subject to constitutional amendment under Article 368)."
                        ],
                        "ta": [
                            "பொருள்: 'இறையாண்மை' என்பது இந்தியா ஒரு சுதந்திரமான தேசம் என்பதைக் குறிக்கிறது. இது எந்தவொரு நாட்டின் சார்பு பகுதியோ (dependency) அல்லது டொமினியனோ (dominion) அல்ல.",
                            "இறையாண்மையின் இரட்டைப் பரிமாணம்:\n1. உள்நாட்டு இறையாண்மை: இந்தியா தனது நிலப்பரப்பிற்கு சட்டங்களை இயற்றவும், உள்நாட்டு மேலதிகாரங்கள் ஏதுமின்றி தன் குடிமக்களை ஆளவும் முழு அதிகாரம் கொண்டுள்ளது.\n2. வெளிநாட்டு இறையாண்மை: இந்தியா வெளிநாட்டு அதிகாரங்களின் எந்தவொரு வெளிக்கட்டுப்பாடு, வழிகாட்டுதல் அல்லது கீழ்நிலைக்கு உட்பட்டதல்ல.",
                            "நிலப்பரப்பு சுதந்திரம்: இறையாண்மை கொண்ட நாடாக இருப்பதால், இந்தியா ஒரு வெளிநாட்டு நிலப்பரப்பைக் கையகப்படுத்தலாம் அல்லது ஒரு வெளிநாட்டு மாநிலத்திற்கு சாதகமாக தனது நிலப்பரப்பின் ஒரு பகுதியை விட்டுக்கொடுக்கலாம் (உறுப்பு 368 இன் கீழ் அரசியலமைப்பு திருத்தத்திற்கு உட்பட்டு)."
                        ]
                    }
                },
                {
                    "title": "2. International Commitments & TNPSC Trap (சர்வதேசக் கடமைகளும் டிஎன்பிஎஸ்சி பொறியும்)",
                    "points": {
                        "en": [
                            "Commonwealth Membership: Though India decided to remain a member of the Commonwealth of Nations in 1949, Pandit Nehru clarified that this voluntary association does NOT affect India's sovereignty in any way.",
                            "UN Membership: India's membership in the United Nations Organisation (UNO) or international treaties does NOT curtail its national sovereignty.",
                            "Simple Example: India deciding its foreign policy, defense alliances, or trade agreements independently without taking orders from any super-power.",
                            "TNPSC Trap: International treaties and UN membership do NOT diminish Indian sovereignty because India enters them voluntarily and can withdraw at will.",
                            "2-Line Revision: Sovereign = Independent internally and externally; no foreign authority above India."
                        ],
                        "ta": [
                            "காமன்வெல்த் உறுப்பினர்: 1949 இல் இந்தியா காமன்வெல்த் நாடுகளின் உறுப்பினராக தொடர முடிவு செய்தபோதிலும், இந்த தன்னார்வ சங்கம் இந்தியாவின் இறையாண்மையை எந்த வகையிலும் பாதிக்காது என்று பண்டிட் நேரு தெளிவுபடுத்தினார்.",
                            "ஐ.நா உறுப்பினர்: ஐக்கிய நாடுகள் சபையில் (UNO) இந்தியா உறுப்பினராக இருப்பதோ அல்லது சர்வதேச ஒப்பந்தங்களோ அதன் தேசிய இறையாண்மையைக் குறைக்காது.",
                            "எளிய உதாரணம்: எந்தவொரு வல்லரசின் உத்தரவையும் பெறாமல் இந்தியா தனது வெளியுறவுக் கொள்கை, பாதுகாப்பு கூட்டணிகள் அல்லது வர்த்தக ஒப்பந்தங்களை சுதந்திரமாக தீர்மானித்தல்.",
                            "டிஎன்பிஎஸ்சி பொறி: சர்வதேச ஒப்பந்தங்கள் மற்றும் ஐ.நா உறுப்பினர் தகுதி இந்திய இறையாண்மையைக் குறைக்காது, ஏனெனில் இந்தியா அவற்றில் தன்னிச்சையாக இணையகிறது மற்றும் விரும்பினால் விலகலாம்.",
                            "2-வரி திருப்புதல்: இறையாண்மை = உள்நாட்டிலும் வெளிநாட்டிலும் சுதந்திரமானது; இந்தியாவிற்கு மேலே வெளிநாட்டு அதிகாரம் எதுவுமில்லை."
                        ]
                    }
                }
            ],
            "sec_socialist": [
                {
                    "title": "1. Constitutional Meaning & Indian Democratic Socialism (சமதர்மக் கருத்து)",
                    "points": {
                        "en": [
                            "Explicit Insertion: The word 'Socialist' was added to the Preamble by the 42nd Constitutional Amendment Act, 1976 (enforced on January 3, 1977).",
                            "Pre-1976 Existence: Even before 1976, the Indian Constitution had a socialist content in the form of Directive Principles of State Policy (DPSP) in Part IV (Articles 38, 39, etc.).",
                            "Democratic Socialism: Indian socialism is 'Democratic Socialism' and NOT 'Communistic Socialism' (Marxist/State socialism which involves nationalization of all means of production and abolition of private property).",
                            "Mixed Economy: Democratic Socialism aims to end poverty, ignorance, disease, and inequality of opportunity through a 'Mixed Economy' where both public and private sectors co-exist side-by-side.",
                            "Supreme Court Stance: In the landmark Excel Wear vs Union of India (1978) and D.S. Nakara cases, SC held that Indian socialism is a blend of Marxism and Gandhism, leaning heavily towards Gandhian socialism."
                        ],
                        "ta": [
                            "வெளிப்படையான சேர்ப்பு: 'சமதர்ம' என்ற சொல் 1976 இன் 42வது அரசியலமைப்பு திருத்தச் சட்டத்தின் மூலம் (ஜனவரி 3, 1977 இல் நடைமுறைக்கு வந்தது) முகவுரையில் சேர்க்கப்பட்டது.",
                            "1976க்கு முந்தைய நிலை: 1976க்கு முன்பே, பகுதி IV இல் உள்ள அரசு நெறிமுறைப்படுத்தும் கோட்பாடுகள் (DPSP) (உறுப்புகள் 38, 39 போன்றவை) வடிவில் இந்திய அரசியலமைப்பு சமதர்ம உள்ளடக்கத்தைக் கொண்டிருந்தது.",
                            "ஜனநாயக சமதர்மம்: இந்திய சமதர்மம் என்பது 'ஜனநாயக சமதர்மம்' ஆகும், இது 'கம்யூனிச சமதர்மம்' (அனைத்து உற்பத்தி சாதனங்களையும் அரசுமயமாக்கல் மற்றும் தனிநபர் சொத்து ஒழிப்பு கொண்ட மார்க்சிஸ்ட் சமதர்மம்) அல்ல.",
                            "கலப்பு பொருளாதாரம்: ஜனநாயக சமதர்மம் வறுமை, அறியாமை, நோய் மற்றும் வாய்ப்பு சமமின்மையை 'கலப்பு பொருளாதாரம்' மூலம் ஒழிப்பதை நோக்கமாகக் கொண்டுள்ளது, அங்கு பொது மற்றும் தனியார் துறைகள் அருகருகே இணைந்து செயல்படுகின்றன.",
                            "உச்ச நீதிமன்ற நிலைப்பாடு: எக்செல் வேர் vs யூனியன் ஆஃப் இந்தியா (1978) வழக்கில், இந்திய சமதர்மம் மார்க்சியம் மற்றும் காந்தியத்தின் கலவையாகும், இது காந்திய சமதர்மத்தை நோக்கி பெரிதும் சாய்ந்துள்ளது என்று உச்ச நீதிமன்றம் குறிப்பிட்டது."
                        ]
                    }
                },
                {
                    "title": "2. Impact of 1991 LPG Reforms & TNPSC Trap (1991 சீர்திருத்தங்களும் டிஎன்பிஎஸ்சி பொறியும்)",
                    "points": {
                        "en": [
                            "1991 LPG Impact: The New Economic Policy of 1991 (Liberalisation, Privatisation, and Globalisation) diluted the state-dominated socialist features, but the constitutional mandate for a welfare state remains intact.",
                            "Simple Example: Government running free public schools/hospitals (Public Sector) alongside private international schools/hospitals (Private Sector).",
                            "TNPSC Trap 1: Word 'Socialist' was NOT in the original 1950 Preamble. It was added by 42nd Amendment 1976.",
                            "TNPSC Trap 2: Do not assume socialist principles were completely absent before 1976; they were already present in Part IV DPSP (Articles 38 & 39).",
                            "2-Line Revision: Socialist = Democratic Socialism & Mixed Economy; added by 42nd Amendment 1976."
                        ],
                        "ta": [
                            "1991 LPG தாக்கம்: 1991 இன் புதிய பொருளாதாரக் கொள்கை (தாராளமயமாக்கல், தனியார்மயமாக்கல் மற்றும் உலகமயமாக்கல்) அரசின் ஆதிக்கத்தில் இருந்த சமதர்ம அம்சங்களை நீர்த்தது, ஆனால் நலன்புரி அரசுக்கான அரசியலமைப்பு ஆணை அப்படியே உள்ளது.",
                            "எளிய உதாரணம்: தனியார் சர்வதேச பள்ளிகள்/மருத்துவமனைகளுடன் (தனியார் துறை) அரசு இலவச பொதுப் பள்ளிகள்/மருத்துவமனைகளை (பொதுத் துறை) நடத்துவது.",
                            "டிஎன்பிஎஸ்சி பொறி 1: 'சமதர்ம' என்ற சொல் அசல் 1950 முகவுரையில் இல்லை. இது 42வது திருத்தம் 1976 மூலம் சேர்க்கப்பட்டது.",
                            "டிஎன்பிஎஸ்சி பொறி 2: 1976க்கு முன்னர் சமதர்மக் கோட்பாடுகள் முற்றிலும் இல்லை என்று நினைக்க வேண்டாம்; அவை பகுதி IV DPSP இல் (உறுப்புகள் 38 & 39) ஏற்கனவே இருந்தன.",
                            "2-வரி திருப்புதல்: சமதர்மம் = ஜனநாயக சமதர்மம் & கலப்பு பொருளாதாரம்; 42வது திருத்தம் 1976 மூலம் சேர்க்கப்பட்டது."
                        ]
                    }
                }
            ],
            "sec_secular": [
                {
                    "title": "1. Positive Concept of Indian Secularism (இந்திய மதச்சார்பின்மை கருத்து)",
                    "points": {
                        "en": [
                            "Explicit Insertion: The word 'Secular' was inserted into the Preamble by the 42nd Constitutional Amendment Act, 1976.",
                            "Pre-1976 Standing: Even before 1976, secularism was embedded in Articles 25 to 28 (Right to Freedom of Religion) as Fundamental Rights in Part III.",
                            "Positive Secularism (Sarva Dharma Sambhava): Unlike Western secularism which mandates rigid separation of State and Religion (strict neutrality/exclusion), Indian secularism embodies 'Positive Secularism' — all religions in India give equal respect, protection, and support from the State.",
                            "No State Religion: The Indian State has no official religion of its own. It is neither pro-religious nor anti-religious, but equal towards all religions.",
                            "Basic Structure: Supreme Court in S.R. Bommai vs Union of India (1994) held that 'Secularism' is part of the Basic Structure of the Constitution."
                        ],
                        "ta": [
                            "வெளிப்படையான சேர்ப்பு: 'மதச்சார்பற்ற' என்ற சொல் 1976 இன் 42வது அரசியலமைப்பு திருத்தச் சட்டத்தின் மூலம் முகவுரையில் சேர்க்கப்பட்டது.",
                            "1976க்கு முந்தைய நிலை: 1976க்கு முன்பே, மதச்சார்பின்மை பகுதி III இல் அடிப்படை உரிமைகளாக உறுப்புகள் 25 முதல் 28 வரை (சமய சுதந்திர உரிமை) பதிந்திருந்தது.",
                            "நேர்மறை மதச்சார்பின்மை (சர்வ தர்ம சம்பவ): அரசு மற்றும் மதத்தைப் பிரிக்கும் மேற்கத்திய மதச்சார்பின்மையைப் போலல்லாமல், இந்திய மதச்சார்பின்மை 'நேர்மறை மதச்சார்பின்மை'யைக் கொண்டுள்ளது — இந்தியாவில் உள்ள அனைத்து மதங்களுக்கும் அரசிடமிருந்து சமமான மரியாதை, பாதுகாப்பு மற்றும் ஆதரவு வழங்கப்படுகிறது.",
                            "அதிகாரப்பூர்வ அரசு மதமின்மை: இந்திய அரசுக்கு சொந்தமாக அதிகாரப்பூர்வ மதம் எதுவும் இல்லை. இது மதத்திற்கு ஆதரவானதோ அல்லது மதத்திற்கு எதிரானதோ அல்ல, மாறாக அனைத்து மதங்களுக்கும் சமமானது.",
                            "அடிப்படை அமைப்பு: எஸ்.ஆர்.பொம்மை vs யூனியன் ஆஃப் இந்தியா (1994) வழக்கில் உச்ச நீதிமன்றம் 'மதச்சார்பின்மை' என்பது அரசியலமைப்பின் அடிப்படை அமைப்பின் ஒரு பகுதி என்று தீர்ப்பளித்தது."
                        ]
                    }
                },
                {
                    "title": "2. Constitutional Protections & TNPSC Trap (அரசியலமைப்பு பாதுகாப்புகளும் பொறியும்)",
                    "points": {
                        "en": [
                            "Key Articles Safeguarding Secularism:\n- Article 14: Equal protection of laws regardless of religion.\n- Article 15: Prohibition of discrimination on grounds of religion.\n- Article 16: Equal opportunity in public employment regardless of religion.\n- Articles 25-28: Freedom of conscience, practice, propagation, and management of religious affairs.\n- Article 27: No person compelled to pay taxes for promotion of any specific religion.",
                            "Simple Example: State declared holidays for Diwali, Id, Christmas, and Buddha Jayanti, treating all religious festivals with equal respect.",
                            "TNPSC Trap: Indian secularism does NOT mean strict anti-religious separation as in France/USA. It means EQUAL RESPECT FOR ALL RELIGIONS (Positive Secularism).",
                            "2-Line Revision: Secular = Positive Secularism (equal respect to all religions); added by 42nd Amendment 1976, Basic Structure."
                        ],
                        "ta": [
                            "மதச்சார்பின்மையைப் பாதுகாக்கும் முக்கிய உறுப்புகள்:\n- உறுப்பு 14: மதத்தைப் பொருட்படுத்தாமல் சட்டங்களின் சமமான பாதுகாப்பு.\n- உறுப்பு 15: மதத்தின் அடிப்படையில் பாகுபாடு காட்டுவது தடை செய்யப்பட்டுள்ளது.\n- உறுப்பு 16: பொது வேலைவாய்ப்பில் மதத்தைப் பொருட்படுத்தாமல் சம வாய்ப்பு.\n- உறுப்புகள் 25-28: மனசாட்சி, வழிபாடு, மதப் பரப்புரை மற்றும் மத விவகாரங்களை நிர்வகிக்கும் சுதந்திரம்.\n- உறுப்பு 27: எந்தவொரு குறிப்பிட்ட மதத்தையும் ஊக்குவிக்க வரி செலுத்த கட்டாயப்படுத்த முடியாது.",
                            "எளிய உதாரணம்: அனைத்து மதப் பண்டிகைகளையும் சம மரியாதையுடன் நடத்தி தீபாவளி, ரம்ஜான், கிறிஸ்துமஸ் மற்றும் புத்த பூர்ணிமாவிற்கு அரசு விடுமுறை அறிவிப்பது.",
                            "டிஎன்பிஎஸ்சி பொறி: இந்திய மதச்சார்பின்மை என்பது பிரான்ஸ்/அமெரிக்கா போல கடுமையான மத எதிர்ப்புப் பிரிவினையைக் குறிக்காது. இது அனைத்து மதங்களுக்கும் சமமான மரியாதையைக் குறிக்கிறது (நேர்மறை மதச்சார்பின்மை).",
                            "2-வரி திருப்புதல்: மதச்சார்பற்ற = நேர்மறை மதச்சார்பின்மை (அனைத்து மதங்களுக்கும் சம மரியாதை); 42வது திருத்தம் 1976 மூலம் சேர்க்கப்பட்டது, அடிப்படை அமைப்பு."
                        ]
                    }
                }
            ],
            "sec_democratic": [
                {
                    "title": "1. Meaning & Dimensions of Democracy (ஜனநாயகத்தின் பொருள்)",
                    "points": {
                        "en": [
                            "Meaning: Derived from Greek words 'Demos' (People) and 'Kratos' (Power). Means government of the people, by the people, and for the people.",
                            "Popular Sovereignty: The supreme power rests with the people.",
                            "Two Types of Democracy:\n1. Direct Democracy: People exercise supreme power directly (e.g. Switzerland) using Referendum, Initiative, Recall, and Plebiscite.\n2. Indirect Democracy (Representative): Supreme power is exercised by representatives elected by the people. India follows Indirect Representative Parliamentary Democracy.",
                            "Broader Vision: Preamble envisions not only political democracy but also social and economic democracy. As Dr. Ambedkar stressed: 'Political democracy cannot last unless there lies at the base of it social democracy.'"
                        ],
                        "ta": [
                            "பொருள்: கிரேக்க வார்த்தைகளான 'டெமோஸ்' (மக்கள்) மற்றும் 'கிராடோஸ்' (அதிகாரம்) ஆகியவற்றிலிருந்து பெறப்பட்டது. மக்கள் ஆட்சி, மக்களால் ஆட்சி, மக்களுக்கான ஆட்சி என்பதைக் குறிக்கிறது.",
                            "மக்களின் இறையாண்மை: உச்ச அதிகாரம் மக்களிடம் உள்ளது.",
                            "ஜனநாயகத்தின் இரண்டு வகைகள்:\n1. நேரடி ஜனநாயகம்: மக்கள் பொதுவாக்கெடுப்பு (Referendum), முன்முயற்சி (Initiative), திரும்பப் பெறுதல் (Recall) மற்றும் கருத்துக்கணிப்பு (Plebiscite) மூலம் உச்ச அதிகாரத்தை நேரடியாகப் பயன்படுத்துகின்றனர் (எ.கா. சுவிட்சர்லாந்து).\n2. மறைமுக ஜனநாயகம் (பிரதிநிதித்துவ): மக்களால் தேர்ந்தெடுக்கப்பட்ட பிரதிநிதிகள் மூலம் உச்ச அதிகாரம் பயன்படுத்தப்படுகிறது. இந்தியா மறைமுக பிரதிநிதித்துவ நாடாளுமன்ற ஜனநாயகத்தைப் பின்பற்றுகிறது.",
                            "பரந்த தொலைநோக்கு: முகவுரை அரசியல் ஜனநாயகத்தை மட்டுமல்ல, சமூக மற்றும் பொருளாதார ஜனநாயகத்தையும் நோக்கமாகக் கொண்டுள்ளது. டாக்டர் அம்பேத்கர் வலியுறுத்தியது போல: 'சமூக ஜனநாயகம் அதன் அடித்தளமாக இல்லாவிட்டால் அரசியல் ஜனநாயகம் நீடிக்க முடியாது.'"
                        ]
                    }
                },
                {
                    "title": "2. Pillars of Indian Democracy & TNPSC Trap (ஜனநாயகத் தூண்களும் பொறியும்)",
                    "points": {
                        "en": [
                            "Pillars of Democracy in Indian Constitution:\n- Universal Adult Franchise (Article 326, reduced to 18 yrs by 61st Amendment 1988).\n- Periodic Free and Fair Elections (conducted by Election Commission, Article 324).\n- Rule of Law (Article 14).\n- Independence of Judiciary.\n- Absence of Discrimination on specific grounds (Article 15).",
                            "Simple Example: Citizens over 18 years voting in Lok Sabha or Vidhan Sabha elections to choose their representatives.",
                            "TNPSC Trap: India does NOT have Direct Democracy tools like Referendum or Recall at the national level. India is a Representative Parliamentary Democracy.",
                            "2-Line Revision: Democratic = Representative Parliamentary Democracy based on Universal Adult Franchise (Art 326)."
                        ],
                        "ta": [
                            "இந்திய அரசியலமைப்பில் ஜனநாயகத்தின் தூண்கள்:\n- உலகளாவிய வயதுவந்தோர் வாக்குரிமை (உறுப்பு 326, 61வது திருத்தம் 1988 மூலம் 18 வயதாகக் குறைக்கப்பட்டது).\n- காலமுறை சுதந்திரமான மற்றும் நியாயமான தேர்தல்கள் (தேர்தல் ஆணையத்தால் நடத்தப்படுகிறது, உறுப்பு 324).\n- சட்டத்தின் ஆட்சி (உறுப்பு 14).\n- நீதித்துறையின் சுதந்திரம்.\n- குறிப்பிட்ட காரணங்களின் அடிப்படையில் பாகுபாடு இல்லாமை (உறுப்பு 15).",
                            "எளிய உதாரணம்: 18 வயதுக்கு மேற்பட்ட குடிமக்கள் மக்களவை அல்லது சட்டமன்றத் தேர்தல்களில் தங்கள் பிரதிநிதிகளைத் தேர்ந்தெடுக்க வாக்களிப்பது.",
                            "டிஎன்பிஎஸ்சி பொறி: தேசிய அளவில் பொதுவாக்கெடுப்பு அல்லது திரும்பப் பெறுதல் போன்ற நேரடி ஜனநாயகக் கருவிகள் இந்தியாவில் இல்லை. இந்தியா ஒரு பிரதிநிதித்துவ நாடாளுமன்ற ஜனநாயகமாகும்.",
                            "2-வரி திருப்புதல்: ஜனநாயகம் = உலகளாவிய வயதுவந்தோர் வாக்குரிமை (உறுப்பு 326) அடிப்படையிலான பிரதிநிதித்துவ நாடாளுமன்ற ஜனநாயகம்."
                        ]
                    }
                }
            ],
            "sec_republic": [
                {
                    "title": "1. Republic vs Constitutional Monarchy (குடியரசு vs முடியாட்சி)",
                    "points": {
                        "en": [
                            "Meaning: A democratic polity is classified into Monarchy or Republic. A Republic means the Head of State is ALWAYS ELECTED for a fixed tenure, rather than a hereditary monarch.",
                            "Indian Republic: The Head of the State in India — the President of India — is indirectly elected by the people for a fixed term of 5 years.",
                            "Two Key Distinctions of a Republic:\n1. Political Sovereignty: Vested in the people, not in a single individual like a King.\n2. Absence of Privileged Class: All public offices are open to every citizen without any discrimination.",
                            "Comparison with UK: Britain is a Democracy but a Constitutional Monarchy (King is hereditary). India is BOTH a Democracy AND a Republic (President is elected)."
                        ],
                        "ta": [
                            "பொருள்: ஒரு ஜனநாயக அரசு முடியாட்சி அல்லது குடியரசு என வகைப்படுத்தப்படுகிறது. குடியரசு என்பது நாட்டின் தலைவர் பரம்பரை மன்னராக இல்லாமல் எப்போதும் ஒரு குறிப்பிட்ட காலத்திற்கு தேர்ந்தெடுக்கப்படுபவர் என்பதைக் குறிக்கிறது.",
                            "இந்தியக் குடியரசு: இந்தியாவின் அரசுத் தலைவர் — இந்தியக் குடியரசுத் தலைவர் — 5 ஆண்டுகள் குறிப்பிட்ட காலத்திற்கு மக்களால் மறைமுகமாகத் தேர்ந்தெடுக்கப்படுகிறார்.",
                            "குடியரசின் இரண்டு முக்கிய வேறுபாடுகள்:\n1. அரசியல் இறையாண்மை: மன்னர் போன்ற தனிநபரிடம் இல்லாமல் மக்களிடம் உள்ளது.\n2. சலுகை பெற்ற வகுப்பு இல்லாமை: அனைத்து பொதுப் பதவிகளும் எந்தவொரு பாகுபாடும் இன்றி ஒவ்வொரு குடிமகனுக்கும் திறந்திருக்கும்.",
                            "இங்கிலாந்துடன் ஒப்பீடு: பிரிட்டன் ஒரு ஜனநாயகம் ஆனால் அரசியலமைப்பு முடியாட்சி (மன்னர் பரம்பரை வழியினராவார்). இந்தியா ஜனநாயகம் மற்றும் குடியரசு ஆகிய இரண்டும் ஆகும் (குடியரசுத் தலைவர் தேர்ந்தெடுக்கப்படுபவர்)."
                        ]
                    }
                },
                {
                    "title": "2. CRITICAL TNPSC TRAP: Democracy vs Republic (முக்கிய பொறி: ஜனநாயகம் vs குடியரசு)",
                    "points": {
                        "en": [
                            "CRITICAL TRAP: 'Democracy' and 'Republic' are NOT synonyms!",
                            "Why? A country can be Democratic WITHOUT being a Republic (e.g. United Kingdom has free elections, but its head of state is a Hereditary Queen/King).",
                            "India chose to be BOTH Democratic (elections for PM & MPs) AND Republic (elected President).",
                            "Simple Example: President of India is elected by MPs and MLAs, whereas King of UK inherits the throne by birth.",
                            "2-Line Revision: Republic = Elected Head of State (President for 5 yrs) + No Hereditary Monopoly on Public Office."
                        ],
                        "ta": [
                            "முக்கிய பொறி: 'ஜனநாயகம்' மற்றும் 'குடியரசு' ஆகியவை இணையான சொற்கள் அல்ல!",
                            "ஏன்? ஒரு நாடு குடியரசாக இல்லாமலேயே ஜனநாயகமாக இருக்க முடியும் (எ.கா. இங்கிலாந்தில் சுதந்திரமான தேர்தல்கள் உள்ளன, ஆனால் அதன் நாட்டின் தலைவர் பரம்பரை ராணி/மன்னர் ஆவார்).",
                            "இந்தியா ஜனநாயகம் (பிரதமர் & எம்பிக்களுக்கான தேர்தல்கள்) மற்றும் குடியரசு (தேர்ந்தெடுக்கப்பட்ட குடியரசுத் தலைவர்) ஆகிய இரண்டாகவும் இருக்கத் தேர்ந்தெடுத்தது.",
                            "எளிய உதாரணம்: இந்தியக் குடியரசுத் தலைவர் எம்பிக்கள் மற்றும் எம்எல்ஏக்களால் தேர்ந்தெடுக்கப்படுகிறார், அதே நேரத்தில் இங்கிலாந்து மன்னர் பிறப்பால் அரியணையைக் கைப்பற்றுகிறார்.",
                            "2-வரி திருப்புதல்: குடியரசு = தேர்ந்தெடுக்கப்பட்ட நாட்டின் தலைவர் (5 ஆண்டுகளுக்கு குடியரசுத் தலைவர்) + பொதுப் பதவிகளில் பரம்பரை ஆதிக்கம் இல்லாமை."
                        ]
                    }
                }
            ],
            "sec_justice": [
                {
                    "title": "1. Three Dimensions of Justice (நீதியின் மூன்று பரிமாணங்கள்)",
                    "points": {
                        "en": [
                            "The term 'Justice' in the Preamble embraces three distinct forms: Social, Economic, and Political, secured through Fundamental Rights (Part III) and Directive Principles (Part IV).",
                            "1. Social Justice: Equal treatment of all citizens without distinction based on caste, color, race, religion, sex, etc. Eliminates social privileges and promotes welfare of SCs, STs, OBCs, and women.",
                            "2. Economic Justice: Non-discrimination between people on the basis of economic factors. Aims to eliminate glaring inequalities in wealth, income, and property.",
                            "Distributive Justice: Social Justice + Economic Justice = 'Distributive Justice'.",
                            "3. Political Justice: All citizens should have equal political rights, equal access to all political offices, and equal voice in government.",
                            "Russian Source: The ideal of Justice — Social, Economic, and Political — was borrowed from the Russian Revolution (1917)."
                        ],
                        "ta": [
                            "முகவுரையில் உள்ள 'நீதி' என்ற சொல் மூன்று வேறுபட்ட வடிவங்களை உள்ளடக்கியது: சமூக, பொருளாதார மற்றும் அரசியல், இது அடிப்படை உரிமைகள் (பகுதி III) மற்றும் வழிகாட்டு நெறிமுறைகள் (பகுதி IV) மூலம் பாதுகாக்கப்படுகிறது.",
                            "1. சமூக நீதி: சாதி, நிறம், இனம், மதம், பாலினம் ஆகியவற்றின் அடிப்படையில் பாகுபாடின்றி அனைத்து குடிமக்களையும் சமமாக நடத்துதல். சமூகச் சலுகைகளை ஒழித்து SC, ST, OBC மற்றும் பெண்களின் நலனை ஊக்குவிக்கிறது.",
                            "2. பொருளாதார நீதி: பொருளாதார காரணிகளின் அடிப்படையில் மக்களிடையே பாகுபாடு காட்டாமை. செல்வம், வருமானம் மற்றும் சொத்து ஆகியவற்றில் உள்ள பெரும் ஏற்றத்தாழ்வுகளை ஒழிப்பதை நோக்கமாகக் கொண்டுள்ளது.",
                            "விநியோக நீதி: சமூக நீதி + பொருளாதார நீதி = 'விநியோக நீதி' (Distributive Justice).",
                            "3. அரசியல் நீதி: அனைத்து குடிமக்களும் சமமான அரசியல் உரிமைகள், அனைத்து அரசியல் பதவிகளுக்கும் சமமான அணுகல் மற்றும் அரசாங்கத்தில் சமமான குரல் கொண்டிருக்க வேண்டும்.",
                            "ரஷ்ய மூலம்: நீதி — சமூக, பொருளாதார மற்றும் அரசியல் — பற்றிய தத்துவம் ரஷ்ய புரட்சியிலிருந்து (1917) பெறப்பட்டது."
                        ]
                    }
                }
            ],
            "sec_liberty": [
                {
                    "title": "1. Concept of Liberty & Reasonable Restrictions (சுதந்திரக் கருத்து)",
                    "points": {
                        "en": [
                            "Meaning: Liberty means the absence of restraints on the activities of individuals, and at the same time, providing opportunities for the development of individual personalities.",
                            "Five Dimensions in Preamble: Liberty of Thought, Expression, Belief, Faith, and Worship.",
                            "Secured through Part III: Enforced primarily through Fundamental Rights (Articles 19, 25-28).",
                            "IMPORTANT TNPSC TRAP: Liberty is NOT absolute; it is QUALIFIED. Liberty does not mean 'license' to do whatever one likes.",
                            "Bound by Restrictions: Liberty expressed in Preamble must be enjoyed within the limitations conceived in the Constitution itself (e.g. Reasonable Restrictions under Article 19(2)).",
                            "French Origin: Ideals of Liberty, Equality, and Fraternity were borrowed from the French Revolution (1789-1799)."
                        ],
                        "ta": [
                            "பொருள்: சுதந்திரம் என்பது தனிநபர்களின் நடவடிக்கைகளின் மீது தடைகள் இல்லாதது, அதே நேரத்தில் தனிநபர் ஆளுமைகளின் வளர்ச்சிக்கு வாய்ப்புகளை வழங்குவதாகும்.",
                            "முகவுரையில் ஐந்து பரிமாணங்கள்: சிந்தனை, வெளிப்பாடு, நம்பிக்கை, சமயம் மற்றும் வழிபாட்டுச் சுதந்திரம்.",
                            "பகுதி III மூலம் பாதுகாப்பு: முக்கியமாக அடிப்படை உரிமைகள் (உறுப்புகள் 19, 25-28) மூலம் அமல்படுத்தப்படுகிறது.",
                            "முக்கிய டிஎன்பிஎஸ்சி பொறி: சுதந்திரம் என்பது வரம்பற்றது (absolute) அல்ல; இது தகுதிவாய்ந்தது (qualified). சுதந்திரம் என்பது ஒருவர் விரும்புவதை எதையும் செய்ய அனுமதிப்பது அல்ல.",
                            "கட்டுப்பாடுகளுக்கு உட்பட்டது: முகவுரையில் வெளிப்படுத்தப்பட்ட சுதந்திரம் அரசியலமைப்பிலேயே கற்பனை செய்யப்பட்ட வரம்புகளுக்குள் அனுபவிக்கப்பட வேண்டும் (எ.கா. உறுப்பு 19(2) இன் கீழ் நியாயமான கட்டுப்பாடுகள்).",
                            "பிரெஞ்சு மூலம்: சுதந்திரம், சமத்துவம் மற்றும் சகோதரத்துவம் ஆகியவற்றின் தத்துவங்கள் பிரெஞ்சு புரட்சியிலிருந்து (1789-1799) பெறப்பட்டன."
                        ]
                    }
                }
            ],
            "sec_equality": [
                {
                    "title": "1. Dimensions of Equality (சமத்துவத்தின் பரிமாணங்கள்)",
                    "points": {
                        "en": [
                            "Meaning: Absence of special privileges to any section of society, and provision of adequate opportunities for all individuals without discrimination.",
                            "Two Dimensions in Preamble: Equality of Status and Equality of Opportunity.",
                            "Three Aspects of Equality:\n1. Civic Equality: Guaranteed under Fundamental Rights (Art 14 Equality before law, Art 15 Prohibition of discrimination, Art 16 Opportunity in employment, Art 17 Abolition of untouchability, Art 18 Abolition of titles).\n2. Political Equality: Art 325 (No person ineligible for electoral rolls on grounds of religion, race, caste, sex) and Art 326 (Universal adult suffrage).\n3. Economic Equality: Art 39 (DPSP securing equal right to livelihood and equal pay for equal work for men & women).",
                            "Formal vs Constitutional Equality: Equality does NOT mean identical treatment in all circumstances; it allows reasonable classification (e.g. Affirmative action/Reservations under Art 15(4) & 16(4))."
                        ],
                        "ta": [
                            "பொருள்: சமூகத்தின் எந்தவொரு பிரிவினருக்கும் சிறப்புச் சலுகைகள் இல்லாதது, மற்றும் பாகுபாடின்றி அனைத்து தனிநபர்களுக்கும் போதுமான வாய்ப்புகளை வழங்குதல்.",
                            "முகவுரையில் இரண்டு பரிமாணங்கள்: தகுதி சமத்துவம் மற்றும் வாய்ப்பு சமத்துவம்.",
                            "சமத்துவத்தின் மூன்று அம்சங்கள்:\n1. குடிமைச் சமத்துவம்: அடிப்படை உரிமைகளின் கீழ் உத்தரவாதம் அளிக்கப்படுகிறது (உறுப்பு 14 சட்டத்தின் முன் சமநிலை, உறுப்பு 15 பாகுபாடு தடை, உறுப்பு 16 வேலைவாய்ப்பில் சமவாய்ப்பு, உறுப்பு 17 தீண்டாமை ஒழிப்பு, உறுப்பு 18 பட்டங்கள் ஒழிப்பு).\n2. அரசியல் சமத்துவம்: உறுப்பு 325 (மதம், இனம், சாதி, பாலினம் காரணமாக வாக்காளர் பட்டியலில் சேர்க்கத் தகுதியின்மை இல்லை) மற்றும் உறுப்பு 326 (உலகளாவிய வயதுவந்தோர் வாக்குரிமை).\n3. பொருளாதாரச் சமத்துவம்: உறுப்பு 39 (ஆண்கள் & பெண்களுக்கு சமமான வாழ்வாதார உரிமை மற்றும் சம வேலைக்கு சம ஊதியம் உறுதியளிக்கும் DPSP).",
                            "முறையான vs அரசியலமைப்புச் சமத்துவம்: சமத்துவம் என்பது அனைத்து சூழ்நிலைகளிலும் ஒரே மாதிரியான சிகிச்சையைக் குறிக்காது; இது நியாயமான வகைப்பாட்டை அனுமதிக்கிறது (எ.கா. உறுப்பு 15(4) & 16(4) இன் கீழ் இடஒதுக்கீடு)."
                        ]
                    }
                }
            ],
            "sec_fraternity": [
                {
                    "title": "1. Brotherhood, Dignity & Integrity (சகோதரத்துவமும் ஒருமைப்பாடும்)",
                    "points": {
                        "en": [
                            "Meaning: Fraternity means a sense of common brotherhood among all citizens. The Constitution promotes this through Single Citizenship (Part II) and Fundamental Duties (Article 51A(e) promoting harmony and spirit of common brotherhood).",
                            "Two Aspects Assured by Fraternity:\n1. Dignity of the Individual: Ensures that every citizen's personality is respected and valued. Dr. K.M. Munshi noted it ensures material development and moral personality.",
                            "2. Unity and Integrity of the Nation: Embraces both psychological and territorial dimensions of national integration.",
                            "Explicit Addition: The word 'Integrity' was added to the Preamble by the 42nd Amendment Act, 1976.",
                            "Why Vital in India? In a deeply diverse nation with multiple religions, languages, and regional identities, Fraternity is the indispensable binding force preventing communal friction and Balkanisation."
                        ],
                        "ta": [
                            "பொருள்: சகோதரத்துவம் என்பது அனைத்து குடிமக்களிடையேயும் பொதுவான சகோதரத்துவ உணர்வைக் குறிக்கிறது. ஒற்றைக் குடியுரிமை (பகுதி II) மற்றும் அடிப்படை கடமைகள் (உறுப்பு 51A(e) நல்லிணக்கம் மற்றும் பொதுவான சகோதரத்துவ உணர்வை ஊக்குவித்தல்) மூலம் அரசியலமைப்பு இதை ஊக்குவிக்கிறது.",
                            "சகோதரத்துவத்தால் உறுதி செய்யப்படும் இரண்டு அம்சங்கள்:\n1. தனிமனித கண்ணியம்: ஒவ்வொரு குடிமகனின் ஆளுமையும் மதிக்கப்படுவதையும் மதிப்பிடப்படுவதையும் உறுதி செய்கிறது. இது பொருள் வளர்ச்சி மற்றும் நெறிமுறை ஆளுமையை உறுதி செய்வதாக டாக்டர் கே.எம். முன்ஷி குறிப்பிட்டார்.",
                            "2. தேசத்தின் ஒற்றுமையும் ஒருமைப்பாடும்: தேசிய ஒருமைப்பாட்டின் உளவியல் மற்றும் நிலப்பரப்பு பரிமாணங்கள் இரண்டையும் உள்ளடக்கியது.",
                            "வெளிப்படையான சேர்ப்பு: 'ஒருமைப்பாடு' என்ற சொல் 1976 இன் 42வது திருத்தச் சட்டத்தின் மூலம் முகவுரையில் சேர்க்கப்பட்டது.",
                            "இந்தியாவில் ஏன் முக்கியம்? பல மதங்கள், மொழிகள் மற்றும் பிராந்திய அடையாளங்களைக் கொண்ட ஆழமான பன்முகத்தன்மை கொண்ட ஒரு தேசத்தில், சகோதரத்துவம் என்பது வகுப்புவாத மோதல்களையும் பிரிவினையையும் தடுக்கும் தவிர்க்க முடியாத பிணைப்புச் சக்தியாகும்."
                        ]
                    }
                }
            ],
            "sec_concept_connections": [
                {
                    "title": "1. Preamble Architecture & Conceptual Map (முகவுரை வடிவமைப்பு)",
                    "points": {
                        "en": [
                            "Hierarchy of Preamble:\nPREAMBLE OF INDIA\n  ├── Source of Authority ──► We, the People of India (Popular Sovereignty)\n  ├── Nature of State (S-S-S-D-R) ──► Sovereign -> Socialist -> Secular -> Democratic -> Republic\n  └── Objectives (J-L-E-F) ──► Justice -> Liberty -> Equality -> Fraternity\n        └── Fraternity leads to ──► Dignity of Individual + Unity & Integrity of Nation\n\nCross-Topic Bridges:\n- Sovereign/Republic ──► Part V (President, Parliament)\n- Socialist/Secular ──► Part IV (DPSP) & Part III (Arts 25-28)\n- Democratic ──► Part XV (Elections, Art 324, 326)\n- Justice/Liberty/Equality ──► Part III (Fundamental Rights)\n- Fraternity/Integrity ──► Part IVA (Fundamental Duties, Art 51A)"
                        ],
                        "ta": [
                            "முகவுரையின் அதிகாரவரிசை:\nஇந்திய முகவுரை\n  ├── அதிகார மூலம் ──► இந்திய மக்களாகிய நாம் (மக்களின் இறையாண்மை)\n  ├── அரசின் தன்மை (S-S-S-D-R) ──► இறையாண்மை -> சமதர்ம -> மதச்சார்பற்ற -> ஜனநாயக -> குடியரசு\n  └── இலக்குகள் (J-L-E-F) ──► நீதி -> சுதந்திரம் -> சமத்துவம் -> சகோதரத்துவம்\n        └── சகோதரத்துவம் வழிநடத்துவது ──► தனிமனித கண்ணியம் + தேசத்தின் ஒற்றுமையும் ஒருமைப்பாடும்\n\nபாலங்கள்:\n- இறையாண்மை/குடியரசு ──► பகுதி V (குடியரசுத் தலைவர், நாடாளுமன்றம்)\n- சமதர்ம/மதச்சார்பற்ற ──► பகுதி IV (DPSP) & பகுதி III (உறுப்புகள் 25-28)\n- ஜனநாயகம் ──► பகுதி XV (தேர்தல்கள், உறுப்பு 324, 326)\n- நீதி/சுதந்திரம்/சமத்துவம் ──► பகுதி III (அடிப்படை உரிமைகள்)\n- சகோதரத்துவம்/ஒருமைப்பாடு ──► பகுதி IVA (அடிப்படை கடமைகள், உறுப்பு 51A)"
                        ]
                    }
                }
            ]
        },
        "important_facts": {
            "en": [
                "Preamble begins with the phrase 'WE, THE PEOPLE OF INDIA'.",
                "Based on Nehru's 'Objectives Resolution' moved on Dec 13, 1946, and adopted on Jan 22, 1947.",
                "Nature of State Order: Sovereign, Socialist, Secular, Democratic, Republic (S-S-S-D-R).",
                "Objectives Order: Justice, Liberty, Equality, Fraternity (J-L-E-F).",
                "42nd Constitutional Amendment Act, 1976 added THREE words: 'Socialist', 'Secular', and 'Integrity'.",
                "Ideals of Justice (Social, Economic, Political) were borrowed from the Russian Revolution (1917).",
                "Ideals of Liberty, Equality, and Fraternity were borrowed from the French Revolution (1789-1799).",
                "N.A. Palkhivala called Preamble the 'Identity Card of the Constitution'.",
                "K.M. Munshi called Preamble the 'Horoscope of our Sovereign Democratic Republic'."
            ],
            "ta": [
                "முகவுரை 'இந்திய மக்களாகிய நாம்' என்ற தொடருடன் தொடங்குகிறது.",
                "1946 டிசம்பர் 13 அன்று முன்மொழியப்பட்டு 1947 ஜனவரி 22 அன்று ஏற்றுக்கொள்ளப்பட்ட நேருவின் 'குறிக்கோள் தீர்மானத்தை' அடிப்படையாகக் கொண்டது.",
                "அரசின் தன்மையின் வரிசை: இறையாண்மை, சமதர்ம, மதச்சார்பற்ற, ஜனநாயக, குடியரசு.",
                "இலக்குகளின் வரிசை: நீதி, சுதந்திரம், சமத்துவம், சகோதரத்துவம்.",
                "1976 இன் 42வது அரசியலமைப்பு திருத்தச் சட்டம் மூன்ரு சொற்களைச் சேர்த்தது: 'சமதர்ம', 'மதச்சார்பற்ற' மற்றும் 'ஒருமைப்பாடு'.",
                "நீதியின் தத்துவங்கள் (சமூக, பொருளாதார, அரசியல்) ரஷ்ய புரட்சியிலிருந்து (1917) பெறப்பட்டவை.",
                "சுதந்திரம், சமத்துவம் மற்றும் சகோதரத்துவம் ஆகியவற்றின் தத்துவங்கள் பிரெஞ்சு புரட்சியிலிருந்து (1789-1799) பெறப்பட்டவை.",
                "என்.ஏ. பால்கிவாலா முகவுரையை 'அரசியலமைப்பின் அடையாள அட்டை' என்று அழைத்தார்.",
                "கே.எம். முன்ஷி முகவுரையை 'நமது இறையாண்மை ஜனநாயகக் குடியரசின் ஜாதகம்' என்று அழைத்தார்."
            ]
        },
        "tnpsc_traps": [
            "⚠️ TRAP 1: 42nd Amendment Act 1976 added THREE words: 'Socialist', 'Secular', and 'Integrity'. (Note: 'Integrity' was added to Fraternity section: 'Unity and Integrity of the Nation').",
            "⚠️ TRAP 2: 'Democracy' and 'Republic' are NOT synonyms. UK is Democratic but a Monarchy. India is BOTH Democratic and Republic.",
            "⚠️ TRAP 3: Ultimate Source of Authority is 'WE, THE PEOPLE OF INDIA', NOT the Parliament or Supreme Court.",
            "⚠️ TRAP 4: Liberty in Preamble is NOT absolute; it is qualified and subject to reasonable restrictions under Article 19(2).",
            "⚠️ TRAP 5: Indian Secularism is POSITIVE (equal respect to all religions), NOT negative anti-religious separation as in Western models.",
            "⚠️ TRAP 6: Indian Socialism is DEMOCRATIC socialism (mixed economy), NOT Marxist state socialism.",
            "⚠️ TRAP 7: Preamble mentions date of ADOPTION (26th November 1949), NOT date of commencement (26th January 1950).",
            "⚠️ TRAP 8: Order of terms matters in TNPSC: Nature = Sovereign, Socialist, Secular, Democratic, Republic. Objectives = Justice, Liberty, Equality, Fraternity."
        ],
        "tables": [
            {
                "id": "tbl_justice_comparison",
                "title_en": "Comparison of Three Dimensions of Justice",
                "title_ta": "நீதியின் மூன்று பரிமாணங்களின் ஒப்பீடு",
                "headers_en": ["Dimension", "Core Meaning", "Constitutional Provisions", "Historical Source"],
                "headers_ta": ["பரிமாணம்", "முதன்மைப் பொருள்", "அரசியலமைப்பு விதிகள்", "வரலாற்று மூலம்"],
                "rows_en": [
                    ["Social Justice", "Equal treatment without discrimination based on caste, religion, sex", "Articles 15, 17, 38, Part XVI", "Russian Revolution (1917)"],
                    ["Economic Justice", "Non-discrimination based on wealth; reduction of income gap", "Articles 39(b), 39(c), Part IV DPSP", "Russian Revolution (1917)"],
                    ["Political Justice", "Equal political rights, voting, and access to public offices", "Articles 16, 325, 326", "Russian Revolution (1917)"]
                ],
                "rows_ta": [
                    ["சமூக நீதி", "சாதி, மதம், பாலினம் அடிப்படையில் பாகுபாடின்றி சமமான நடத்தை", "உறுப்புகள் 15, 17, 38, பகுதி XVI", "ரஷ்ய புரட்சி (1917)"],
                    ["பொருளாதார நீதி", "செல்வத்தின் அடிப்படையில் பாகுபாடின்மை; வருமான இடைவெளியைக் குறைத்தல்", "உறுப்புகள் 39(b), 39(c), பகுதி IV DPSP", "ரஷ்ய புரட்சி (1917)"],
                    ["அரசியல் நீதி", "சமமான அரசியல் உரிமைகள், வாக்குரிமை மற்றும் பொதுப் பதவிகளுக்கான அணுகல்", "உறுப்புகள் 16, 325, 326", "ரஷ்ய புரட்சி (1917)"]
                ]
            }
        ],
        "concept_map": [
            {
                "id": "mm_root",
                "parent_id": None,
                "title": "Preamble of India (இந்திய முகவுரை)",
                "short_label": "Preamble"
            },
            {
                "id": "mm_source",
                "parent_id": "mm_root",
                "title": "Source of Authority: We, the People of India",
                "short_label": "Source: People"
            },
            {
                "id": "mm_nature",
                "parent_id": "mm_root",
                "title": "Nature of State: Sovereign, Socialist, Secular, Democratic, Republic",
                "short_label": "Nature of State"
            },
            {
                "id": "mm_sovereign",
                "parent_id": "mm_nature",
                "title": "Sovereign: Independent internally & externally",
                "short_label": "Sovereign"
            },
            {
                "id": "mm_socialist",
                "parent_id": "mm_nature",
                "title": "Socialist: Democratic Socialism & Mixed Economy (42nd Amend 1976)",
                "short_label": "Socialist"
            },
            {
                "id": "mm_secular",
                "parent_id": "mm_nature",
                "title": "Secular: Positive Secularism / Sarva Dharma Sambhava (42nd Amend 1976)",
                "short_label": "Secular"
            },
            {
                "id": "mm_democratic",
                "parent_id": "mm_nature",
                "title": "Democratic: Representative Parliamentary Democracy (Art 326)",
                "short_label": "Democratic"
            },
            {
                "id": "mm_republic",
                "parent_id": "mm_nature",
                "title": "Republic: Elected Head of State (President) for 5 years",
                "short_label": "Republic"
            },
            {
                "id": "mm_objectives",
                "parent_id": "mm_root",
                "title": "Objectives: Justice, Liberty, Equality, Fraternity",
                "short_label": "Objectives"
            },
            {
                "id": "mm_justice",
                "parent_id": "mm_objectives",
                "title": "Justice: Social, Economic, Political (Russian Rev 1917)",
                "short_label": "Justice"
            },
            {
                "id": "mm_liberty",
                "parent_id": "mm_objectives",
                "title": "Liberty: Thought, Expression, Belief, Faith, Worship (French Rev 1789)",
                "short_label": "Liberty"
            },
            {
                "id": "mm_equality",
                "parent_id": "mm_objectives",
                "title": "Equality: Status & Opportunity (Arts 14-18)",
                "short_label": "Equality"
            },
            {
                "id": "mm_fraternity",
                "parent_id": "mm_objectives",
                "title": "Fraternity: Dignity of Individual + Unity & Integrity (42nd Amend 1976)",
                "short_label": "Fraternity"
            }
        ],
        "revision_cards": [
            {
                "id": "RC_PRE1_001",
                "title": {
                    "en": "Source of Authority",
                    "ta": "அதிகாரத்தின் மூலம்"
                },
                "front": {
                    "en": "Who is the ultimate source of authority under the Indian Constitution?",
                    "ta": "இந்திய அரசியலமைப்பின் கீழ் அதிகாரத்தின் இறுதி மூலம் யார்?"
                },
                "back": {
                    "en": "'WE, THE PEOPLE OF INDIA'. Embodying Popular Sovereignty. The Constitution is created by and for the people, not granted by any monarch or external power.",
                    "ta": "'இந்திய மக்களாகிய நாம்'. மக்களின் இறையாண்மையை வெளிப்படுத்துகிறது. அரசியலமைப்பு மக்களால் உருவாக்கப்பட்டு தங்களுக்குத்தானே வழங்கப்பட்டதாகும்."
                },
                "one_line_revision": "Source of Authority = We, the People of India (Popular Sovereignty).",
                "type": "fact"
            },
            {
                "id": "RC_PRE1_002",
                "title": {
                    "en": "Nature of State Order",
                    "ta": "அரசின் தன்மையின் வரிசை"
                },
                "front": {
                    "en": "What is the exact sequence of terms defining the Nature of the Indian State?",
                    "ta": "இந்திய அரசின் தன்மையை வரையறுக்கும் சொற்களின் துல்லியமான வரிசை என்ன?"
                },
                "back": {
                    "en": "SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC, REPUBLIC (S-S-S-D-R).",
                    "ta": "இறையாண்மை, சமதர்ம, மதச்சார்பற்ற, ஜனநாயக, குடியரசு."
                },
                "one_line_revision": "Nature Order = Sovereign -> Socialist -> Secular -> Democratic -> Republic.",
                "type": "fact"
            },
            {
                "id": "RC_PRE1_003",
                "title": {
                    "en": "Objectives Order",
                    "ta": "இலக்குகளின் வரிசை"
                },
                "front": {
                    "en": "What is the exact sequence of constitutional Objectives in the Preamble?",
                    "ta": "முகவுரையில் உள்ள அரசியலமைப்பு இலக்குகளின் துல்லியமான வரிசை என்ன?"
                },
                "back": {
                    "en": "JUSTICE (Social, Economic, Political), LIBERTY (Thought, Expression, Belief, Faith, Worship), EQUALITY (Status, Opportunity), FRATERNITY (Dignity, Unity & Integrity).",
                    "ta": "நீதி (சமூக, பொருளாதார, அரசியல்), சுதந்திரம், சமத்துவம், சகோதரத்துவம்."
                },
                "one_line_revision": "Objectives Order = Justice -> Liberty -> Equality -> Fraternity.",
                "type": "fact"
            },
            {
                "id": "RC_PRE1_004",
                "title": {
                    "en": "42nd Amendment Act 1976",
                    "ta": "42வது திருத்தச் சட்டம் 1976"
                },
                "front": {
                    "en": "Which three words were added to the Preamble by the 42nd Amendment Act 1976?",
                    "ta": "42வது திருத்தச் சட்டம் 1976 மூலம் முகவுரையில் சேர்க்கப்பட்ட மூன்று சொற்கள் யாவை?"
                },
                "back": {
                    "en": "SOCIALIST, SECULAR, and INTEGRITY (added to Fraternity). Enforced on Jan 3, 1977.",
                    "ta": "சமதர்ம (SOCIALIST), மதச்சார்பற்ற (SECULAR) மற்றும் ஒருமைப்பாடு (INTEGRITY). ஜனவரி 3, 1977 இல் அமலானது."
                },
                "one_line_revision": "42nd Amendment 1976 = Socialist + Secular + Integrity added.",
                "type": "concept"
            },
            {
                "id": "RC_PRE1_005",
                "title": {
                    "en": "Democracy vs Republic",
                    "ta": "ஜனநாயகம் vs குடியரசு"
                },
                "front": {
                    "en": "Why are Democracy and Republic NOT synonymous?",
                    "ta": "ஜனநாயகமும் குடியரசும் ஏன் இணையான சொற்கள் அல்ல?"
                },
                "back": {
                    "en": "Democracy means government by popular elections. Republic specifically means an ELECTED Head of State (President) rather than a hereditary monarch. UK is Democratic but a Monarchy; India is both.",
                    "ta": "ஜனநாயகம் என்பது தேர்தல் மூலம் மக்கள் ஆட்சி. குடியரசு என்பது பரம்பரை மன்னருக்குப் பதிலாகத் தேர்ந்தெடுக்கப்பட்ட அரசுத் தலைவரைக் குறிப்பது. இங்கிலாந்து ஜனநாயகம் ஆனால் முடியாட்சி; இந்தியா இரண்டும் ஆகும்."
                },
                "one_line_revision": "Republic = Elected Head of State (President); Democracy = Popular sovereignty.",
                "type": "trap"
            },
            {
                "id": "RC_PRE1_006",
                "title": {
                    "en": "Indian Secularism",
                    "ta": "இந்திய மதச்சார்பின்மை"
                },
                "front": {
                    "en": "How does Indian Secularism differ from Western Secularism?",
                    "ta": "இந்திய மதச்சார்பின்மை மேற்கத்திய மதச்சார்பின்மையிலிருந்து எவ்வாறு வேறுபடுகிறது?"
                },
                "back": {
                    "en": "Indian secularism is POSITIVE (equal respect/support to all religions - Sarva Dharma Sambhava), whereas Western secularism mandates strict negative separation of state and religion.",
                    "ta": "இந்திய மதச்சார்பின்மை என்பது நேர்மறை மதச்சார்பின்மை (அனைத்து மதங்களுக்கும் சம மரியாதை - சர்வ தர்ம சம்பவ); மேற்கத்திய மதச்சார்பின்மை அரசு-மதத்திற்கு இடையே கடுமையான பிரிவினையை ஆணையிடுகிறது."
                },
                "one_line_revision": "Indian Secularism = Positive concept (Sarva Dharma Sambhava, Basic Structure).",
                "type": "comparison"
            }
        ]
    }
    return note

def build_notes_file():
    payload = generate_preamble_part1_payload()
    
    output_dir = r"c:\Users\Home\Desktop\tnpsc_ai\data\notes\polity"
    os.makedirs(output_dir, exist_ok=True)
    
    file_path1 = os.path.join(output_dir, "preamble_part_1.json")
    file_path2 = os.path.join(output_dir, "preamble_part1.json")

    with open(file_path1, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    with open(file_path2, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    print(f"SUCCESSFULLY SAVED PREAMBLE PART 1 NOTES AT:")
    print(f"  - {file_path1}")
    print(f"  - {file_path2}")

if __name__ == "__main__":
    build_notes_file()
