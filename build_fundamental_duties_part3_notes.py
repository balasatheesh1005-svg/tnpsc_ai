# -*- coding: utf-8 -*-
"""
Script to build production-ready bilingual TNPSC Group 1 Notes for:
Fundamental Duties - Part 3
Target File: data/notes/polity/fundamental_duties_part_3.json
"""

import json
import os

notes_data = {
    "meta": {
        "topic_id": "polity_fundamental_duties_part_3",
        "repository_id": "polity_fundamental_duties",
        "display_title": "Fundamental Duties – Part 3",
        "part": 3,
        "total_parts": 3,
        "subject": "polity",
        "chapter": "Fundamental Duties",
        "language": "English + Tamil"
    },
    "metadata": {
        "version": "2.0",
        "status": "approved",
        "review_status": "gold_standard",
        "difficulty": "foundation",
        "estimated_study_time": {
            "reading": "40 min",
            "revision": "20 min",
            "total": "60 min"
        }
    },
    "keywords": [
        "Fundamental Duties Part 3",
        "அடிப்படை கடமைகள் பகுதி 3",
        "Article 51Ak Education Duty",
        "உறுப்பு 51A(k) கல்வி கடமை",
        "Article 21A vs Article 45 vs Article 51Ak",
        "உறுப்பு 21A vs உறுப்பு 45 vs உறுப்பு 51A(k)",
        "86th Constitutional Amendment 2002",
        "86வது அரசியலமைப்பு திருத்தம் 2002",
        "Complete 11 Fundamental Duties Matrix",
        "முழுமையான 11 அடிப்படை கடமைகள் அணி",
        "Swaran Singh Committee Complete Timeline",
        "ஸ்வரன் சிங் குழு முழுமையான காலவரிசை",
        "Nature and Legal Enforceability",
        "இயல்பு மற்றும் சட்டப்பூர்வ அமலாக்கம்",
        "Rights Duties DPSP Triangle",
        "உரிமைகள் கடமைகள் DPSP முக்கோணம்",
        "Environmental Constitutional Triangle",
        "சுற்றுச்சூழல் அரசியலமைப்பு முக்கோணம்",
        "Thematic Classification of 11 Duties",
        "11 கடமைகளின் தலைப்பு வாரியான வகைப்பாடு",
        "Aruna Roy Case Value Education",
        "அருணா ராய் வழக்கு மதிப்புக் கல்வி",
        "Complete 2 Minute Revision",
        "முழுமையான 2 நிமிட திருப்புதல்"
    ],
    "learning_outcomes": {
        "Understand": {
            "en": [
                "Understand Article 51A(k), its insertion by the 86th Constitutional Amendment Act 2002, and the exact duty placed on parents/guardians.",
                "Understand the complete master matrix of all 11 Fundamental Duties from Article 51A(a) to 51A(k).",
                "Understand the Constitutional Triangles: Education Triangle (Art 21A ↔ Art 45 ↔ Art 51A(k)) and Environment Triangle (Art 21 ↔ Art 48A ↔ Art 51A(g)).",
                "Understand the nature, legal enforceability, and judicial role of Fundamental Duties in statutory construction and constitutional interpretation."
            ],
            "ta": [
                "உறுப்பு 51A(k), 2002-ன் 86வது அரசியலமைப்பு திருத்தச் சட்டத்தால் அது சேர்க்கப்பட்டது மற்றும் பெற்றோர்கள்/பாதுகாவலர்கள் மீது விதிக்கப்பட்ட சரியான கடமையைப் புரிந்து கொள்ளுதல்.",
                "உறுப்பு 51A(a) முதல் 51A(k) வரையிலான அனைத்து 11 அடிப்படை கடமைகளின் முழுமையான முதன்மை அணியைப் புரிந்து கொள்ளுதல்.",
                "அரசியலமைப்பு முக்கோணங்களைப் புரிந்து கொள்ளுதல்: கல்வி முக்கோணம் (உறுப்பு 21A ↔ உறுப்பு 45 ↔ உறுப்பு 51A(k)) மற்றும் சுற்றுச்சூழல் முக்கோணம் (உறுப்பு 21 ↔ உறுப்பு 48A ↔ உறுப்பு 51A(g)).",
                "சட்ட வரைவு விளக்கம் மற்றும் அரசியலமைப்பு விளக்கத்தில் அடிப்படை கடமைகளின் இயல்பு, சட்டப்பூர்வ அமலாக்கம் மற்றும் நீதித்துறையின் பங்கைப் புரிந்து கொள்ளுதல்."
            ]
        },
        "Remember": {
            "en": [
                "Remember that Article 51A(k) is the 11th Fundamental Duty added by the 86th Amendment Act in 2002 for children aged 6 to 14 years.",
                "Remember the exact distinction: Art 21A (FR - State duty), Art 45 (DPSP - Below 6 yrs care), Art 51A(k) (FD - Parent duty for 6-14 yrs).",
                "Remember the complete timeline: 1950 (0 Duties) → 1976 42nd CAA (10 Duties) → 2002 86th CAA (11 Duties).",
                "Remember the exam-oriented 6-fold thematic classification of all 11 duties.",
                "Remember key cases: Bijoe Emmanuel (1986), MC Mehta (1997), AIIMS Students Union (2002), Nagaraja (2014), Aruna Roy (2002)."
            ],
            "ta": [
                "உறுப்பு 51A(k) என்பது 6 முதல் 14 வயது வரையிலான குழந்தைகளுக்காக 2002-ன் 86வது திருத்தத்தால் சேர்க்கப்பட்ட 11வது அடிப்படை கடமை என்பதை நினைவில் கொள்ளுதல்.",
                "சரியான வேறுபாட்டை நினைவில் கொள்ளுதல்: உறுப்பு 21A (FR - அரசு கடமை), உறுப்பு 45 (DPSP - 6 வயதிற்குட்பட்டோர் பராமரிப்பு), உறுப்பு 51A(k) (FD - 6-14 வயதினருக்குப் பெற்றோர் கடமை).",
                "முழுமையான காலவரிசையை நினைவில் கொள்ளுதல்: 1950 (0 கடமைகள்) → 1976 42வது திருத்தம் (10 கடமைகள்) → 2002 86வது திருத்தம் (11 கடமைகள்).",
                "அனைத்து 11 கடமைகளின் தேர்வு சார்ந்த 6 வகை தலைப்பு வாரியான வகைப்பாட்டை நினைவில் கொள்ளுதல்.",
                "முக்கிய வழக்குகளை நினைவில் கொள்ளுதல்: பிஜோய் இம்மானுவேல் (1986), எம்.சி. மேத்தா (1997), AIIMS மாணவர் சங்கம் (2002), நாகராஜா (2014), அருணா ராய் (2002)."
            ]
        },
        "Analyze": {
            "en": [
                "Analyze the legal harmony between Part III (Fundamental Rights), Part IV (DPSP), and Part IVA (Fundamental Duties).",
                "Analyze why Fundamental Duties, despite being non-justiciable by themselves, are legally relevant and constitutionally backed by parliamentary statutes.",
                "Analyze the distinction between Swaran Singh Committee's rejected recommendations (duty to pay taxes, penalties) and enacted provisions.",
                "Analyze how courts apply Fundamental Duties to test the 'reasonableness' of restrictions on Fundamental Rights under Article 19."
            ],
            "ta": [
                "பகுதி III (அடிப்படை உரிமைகள்), பகுதி IV (DPSP) மற்றும் பகுதி IVA (அடிப்படை கடமைகள்) இடையேயான சட்டப்பூர்வ இணக்கத்தைப் பகுப்பாய்வு செய்தல்.",
                "அடிப்படை கடமைகள் நேரடியாக அமல்படுத்த முடியாதவை என்ற போதிலும், அவை ஏன் சட்டப்பூர்வமாகத் தொடர்புடையவை மற்றும் நாடாளுமன்றச் சட்டங்களால் ஆதரிக்கப்படுகின்றன என்பதை பகுப்பாய்வு செய்தல்.",
                "ஸ்வரன் சிங் குழுவின் நிராகரிக்கப்பட்ட பரிந்துரைகளுக்கும் (வரி செலுத்தும் கடமை, அபராதங்கள்) இயற்றப்பட்ட விதிகளுக்கும் இடையிலான வேறுபாட்டைப் பகுப்பாய்வு செய்தல்.",
                "உறுப்பு 19-ன் கீழ் அடிப்படை உரிமைகள் மீதான கட்டுப்பாடுகளின் 'நியாயத் தன்மையை' சோதிக்க நீதிமன்றங்கள் அடிப்படை கடமைகளை எவ்வாறு பயன்படுத்துகின்றன என்பதை பகுப்பாய்வு செய்தல்."
            ]
        },
        "Apply": {
            "en": [
                "Apply TNPSC trap points to eliminate incorrect options in complex MCQs on Article 21A vs Article 45 vs Article 51A(k).",
                "Accurately match all 11 Fundamental Duties (a to k) with their respective core keywords in Match the Following items.",
                "Solve statement-based and reasoning questions on Swaran Singh recommendations vs 42nd Amendment provisions."
            ],
            "ta": [
                "உறுப்பு 21A vs உறுப்பு 45 vs உறுப்பு 51A(k) பற்றிய சிக்கலான வினாக்களில் தவறான விருப்பங்களை நீக்க டிஎன்பிஎஸ்சி பொறி புள்ளிகளைப் பயன்படுத்துதல்.",
                "பொருத்துக வினாக்களில் அனைத்து 11 அடிப்படை கடமைகளையும் (a முதல் k வரை) அவற்றின் முதன்மை முக்கிய வார்த்தைகளுடன் சரியாகப் பொருத்துதல்.",
                "ஸ்வரன் சிங் பரிந்துரைகள் vs 42வது திருத்த விதிகள் பற்றிய கூற்று மற்றும் காரண வினாக்களுக்குத் தீர்வுகாணுதல்."
            ]
        }
    },
    "subject": "Polity",
    "topic": "Fundamental Duties – Part 3",
    "language": "bilingual",
    "ui_type": "polity",
    "sections": [
        {
            "id": "sec_art_51ak",
            "title_en": "1. Article 51A(k): Education Duty for Children Aged 6 to 14 Years",
            "title_ta": "1. உறுப்பு 51A(k): 6 முதல் 14 வயது வரையிலான குழந்தைகளுக்கான கல்விக் கடமை",
            "type": "standard_topic"
        },
        {
            "id": "sec_all_11_duties_matrix",
            "title_en": "2. Complete Master Matrix of All 11 Fundamental Duties (51A(a) to 51A(k))",
            "title_ta": "2. அனைத்து 11 அடிப்படை கடமைகளின் முழுமையான முதன்மை அணி (51A(a) முதல் 51A(k))",
            "type": "standard_topic"
        },
        {
            "id": "sec_constitutional_history_timeline",
            "title_en": "3. Constitutional History, Swaran Singh Committee & Amendment Timeline",
            "title_ta": "3. அரசியலமைப்பு வரலாறு, ஸ்வரன் சிங் குழு & திருத்தக் காலவரிசை",
            "type": "standard_topic"
        },
        {
            "id": "sec_nature_enforceability_part3",
            "title_en": "4. Nature, Legal Enforceability & Statutory Enforcement Framework",
            "title_ta": "4. இயல்பு, சட்டப்பூர்வ அமலாக்கம் & சட்டப்பூர்வ அமலாக்கக் கட்டமைப்பு",
            "type": "standard_topic"
        },
        {
            "id": "sec_tripartite_synthesis",
            "title_en": "5. Constitutional Synthesis: Rights (Part III) ↔ DPSP (Part IV) ↔ Duties (Part IVA)",
            "title_ta": "5. அரசியலமைப்புத் தொகுப்பு: உரிமைகள் (பகுதி III) ↔ DPSP (பகுதி IV) ↔ கடமைகள் (பகுதி IVA)",
            "type": "standard_topic"
        },
        {
            "id": "sec_cases_legal_context_part3",
            "title_en": "6. Comprehensive Judicial Verdicts & Landmark Precedents",
            "title_ta": "6. விரிவான நீதித்துறை தீர்ப்புகள் & முக்கிய முன்மாதிரிகள்",
            "type": "standard_topic"
        },
        {
            "id": "sec_environmental_education_triangles",
            "title_en": "7. Environmental & Educational Constitutional Triangles",
            "title_ta": "7. சுற்றுச்சூழல் & கல்வி தொடர்பான அரசியலமைப்பு முக்கோணங்கள்",
            "type": "standard_topic"
        },
        {
            "id": "sec_thematic_classification",
            "title_en": "8. Exam-Oriented Thematic Grouping of All 11 Fundamental Duties",
            "title_ta": "8. அனைத்து 11 அடிப்படை கடமைகளின் தேர்வு சார்ந்த தலைப்பு வாரியான வகைப்பாடு",
            "type": "standard_topic"
        },
        {
            "id": "sec_traps_revision_part3",
            "title_en": "9. TNPSC High-Yield Traps, Master Tables & 2-Minute Complete Revision",
            "title_ta": "9. டிஎன்பிஎஸ்சி பொறிகள், முதன்மை அட்டவணைகள் & 2 நிமிட முழுமையான திருப்புதல்",
            "type": "standard_topic"
        }
    ],
    "content": {
        "definition": {
            "en": "Part 3 of Fundamental Duties completes the chapter by providing an exhaustive analysis of Article 51A(k) (Parent duty for education of children 6-14 yrs), the complete 11 Fundamental Duties master matrix, constitutional timeline (1950 to 86th CAA 2002), legal enforceability and statutory framework, constitutional synthesis between Part III, IV, and IVA, landmark judicial case laws, thematic classification, 10 mandatory comparison tables, mind map, bilingual TNPSC trap points, and a 2-minute rapid revision of the entire Fundamental Duties subject.",
            "ta": "அடிப்படை கடமைகள் பகுதி 3 இப்பாடத்தை முழுமையாக்குகிறது. இது உறுப்பு 51A(k) (6-14 வயது குழந்தைகள் கல்விக்கான பெற்றோர் கடமை), அனைத்து 11 அடிப்படை கடமைகளின் முதன்மை அணி, அரசியலமைப்பு காலவரிசை (1950 முதல் 86வது திருத்தம் 2002 வரை), சட்டப்பூர்வ அமலாக்கம் மற்றும் சட்டக் கட்டமைப்பு, பகுதிகள் III, IV, மற்றும் IVA இடையேயான அரசியலமைப்புத் தொகுப்பு, முக்கிய நீதிமன்றத் தீர்ப்புகள், தலைப்பு வாரியான வகைப்பாடு, 10 கட்டாய ஒப்பீட்டு அட்டவணைகள், மன வரைபடம், இருமொழி டிஎன்பிஎஸ்சி பொறி புள்ளிகள் மற்றும் ஒட்டுமொத்த அடிப்படை கடமைகள் பாடத்தின் 2 நிமிட விரைவு திருப்புதல் ஆகியவற்றை விரிவாக வழங்குகிறது."
        },
        "introduction": {
            "en": "This final part integrates the entire Fundamental Duties chapter for TNPSC Group 1 level. It synthesizes all 11 duties under Article 51A(a)–(k), clarifies the critical Education Triangle (Art 21A ↔ Art 45 ↔ Art 51A(k)) and Environment Triangle (Art 21 ↔ Art 48A ↔ Art 51A(g)), reviews Swaran Singh recommendations vs accepted provisions, outlines statutory enforcement laws, and provides 10 comprehensive comparison tables, a complete mind map, and high-yield revision cards.",
            "ta": "இந்த இறுதிப் பகுதி டிஎன்பிஎஸ்சி குரூப் 1 நிலைகளுக்காக முழு அடிப்படை கடமைகள் பாடத்தையும் ஒருங்கிணைக்கிறது. இது உறுப்பு 51A(a)–(k) இன் கீழ் உள்ள அனைத்து 11 கடமைகளையும் தொகுக்கிறது, கல்வி முக்கோணம் (உறுப்பு 21A ↔ உறுப்பு 45 ↔ உறுப்பு 51A(k)) மற்றும் சுற்றுச்சூழல் முக்கோணத்தை (உறுப்பு 21 ↔ உறுப்பு 48A ↔ உறுப்பு 51A(g)) தெளிவுபடுத்துகிறது, ஸ்வரன் சிங் பரிந்துரைகள் vs இயற்றப்பட்ட விதிகளை மதிப்பாய்வு செய்கிறது, சட்டப்பூர்வ அமலாக்கச் சட்டங்களை விவரிக்கிறது, மேலும் 10 விரிவான ஒப்பீட்டு அட்டவணைகள், முழுமையான மன வரைபடம் மற்றும் முக்கிய திருப்புதல் அட்டைகளை வழங்குகிறது."
        },
        "sec_art_51ak": [
            {
                "title": "1. Article 51A(k): Duty of Parent/Guardian to Provide Education (உறுப்பு 51A(k): கல்விக்கான பெற்றோர்/பாதுகாவலர் கடமை)",
                "points": {
                    "en": [
                        "Constitutional Text: 'who is a parent or guardian to provide opportunities for education to his child or, as the case may be, ward between the age of six and fourteen years.'",
                        "Added By: 86th Constitutional Amendment Act, 2002 (under Prime Minister Atal Bihari Vajpayee).",
                        "Target Age Group: EXACTLY 6 to 14 years. (Crucial TNPSC point: Not 0–6 years, not 6–18 years!).",
                        "Duty Bearer: The PARENT or GUARDIAN of the child/ward.",
                        "Simple Explanation: While Article 21A obligates the State to construct schools and provide free education, Article 51A(k) obligates parents to actually send their children aged 6–14 to school and provide learning opportunities.",
                        "Example: A parent ensuring their 10-year-old child attends school regularly rather than putting them to child labor fulfills Article 51A(k).",
                        "TNPSC High-Yield Trap: Article 21A is a Fundamental Right (State Duty); Article 51A(k) is a Fundamental Duty (Parent Duty). Both relate to education of children aged 6–14 years!"
                    ],
                    "ta": [
                        "அரசியலமைப்பு உரை: 'ஆறு முதல் பதினான்கு வயது வரையிலான தனது குழந்தைக்கு அல்லது பாதுகாப்பில் உள்ளவருக்குக் கல்வி வாய்ப்புகளை வழங்குவது பெற்றோர் அல்லது பாதுகாவலரின் கடமையாகும்.'",
                        "சேர்க்கப்பட்ட திருத்தம்: 2002-ன் 86வது அரசியலமைப்பு திருத்தச் சட்டம் (பிரதமர் அடல் பிஹாரி வாஜ்பாய் காலத்தில்).",
                        "இலக்கு வயதுக் குழு: சரியாக 6 முதல் 14 வயது வரை. (டிஎன்பிஎஸ்சி முக்கிய குறிப்பு: 0–6 வயது அல்ல, 6–18 வயது அல்ல!).",
                        "கடமைப் பொறுப்பாளி: બાળக்கின் அல்லது பாதுகாப்பில் உள்ளவரின் பெற்றோர் அல்லது பாதுகாவலர்.",
                        "எளிய விளக்கம்: உறுப்பு 21A பள்ளிகளைக் கட்டி இலவசக் கல்வி வழங்க அரசுக்குக் கடமையாக்கும் நிலையில், உறுப்பு 51A(k) 6–14 வயதுள்ள தங்கள் குழந்தைகளைப் பள்ளிக்கு அனுப்பி கற்றல் வாய்ப்புகளை வழங்கப் பெற்றோருக்குக் கடமையாக்குகிறது.",
                        "உதாரணம்: ஒரு பெற்றோர் தங்கள் 10 வயதுக் குழந்தையைக் குழந்தை தொழிலாளியாக மாற்றாமல் தவறாமல் பள்ளிக்கு அனுப்புவது உறுப்பு 51A(k)-ஐப் பூர்த்தி செய்கிறது.",
                        "டிஎன்பிஎஸ்சி பொறிப் புள்ளி: உறுப்பு 21A என்பது அடிப்படை உரிமை (அரசு கடமை); உறுப்பு 51A(k) என்பது அடிப்படை கடமை (பெற்றோர் கடமை). இரண்டும் 6–14 வயது குழந்தைகளின் கல்வி தொடர்பானது!"
                    ]
                }
            }
        ],
        "sec_all_11_duties_matrix": [
            {
                "title": "1. Master Matrix of All 11 Fundamental Duties (அனைத்து 11 அடிப்படை கடமைகளின் முதன்மை அணி)",
                "points": {
                    "en": [
                        "51A(a) [National Symbols]: Abide by Constitution, respect ideals, institutions, National Flag, and National Anthem. Memory Aid: 'Constitution & Flag'.",
                        "51A(b) [Freedom Ideals]: Cherish and follow noble ideals of national freedom struggle. Memory Aid: 'Freedom Struggle'.",
                        "51A(c) [Sovereignty & Unity]: Uphold and protect sovereignty, unity, and integrity of India. Memory Aid: 'Sovereignty & Integrity'.",
                        "51A(d) [National Defence]: Defend country and render national service when called upon. Memory Aid: 'National Defence'.",
                        "51A(e) [Brotherhood & Women]: Promote harmony, common brotherhood; renounce practices derogatory to dignity of women. Memory Aid: 'Brotherhood & Women's Dignity'.",
                        "51A(f) [Composite Culture]: Value and preserve rich heritage of our composite culture. Memory Aid: 'Composite Culture'.",
                        "51A(g) [Environment & Animals]: Protect/improve forests, lakes, rivers, wildlife; have compassion for living creatures. Memory Aid: 'Environment & Wildlife'.",
                        "51A(h) [Scientific Temper]: Develop scientific temper, humanism, spirit of inquiry and reform. Memory Aid: 'Scientific Temper'.",
                        "51A(i) [Public Property]: Safeguard public property and abjure violence. Memory Aid: 'Public Property & Non-Violence'.",
                        "51A(j) [Strive for Excellence]: Strive towards excellence in individual and collective activity. Memory Aid: 'Strive for Excellence'.",
                        "51A(k) [Child Education]: Parent/guardian duty to provide education opportunities to child aged 6-14 years. Memory Aid: 'Child Education 6-14'."
                    ],
                    "ta": [
                        "51A(a) [தேசிய சின்னங்கள்]: அரசியலமைப்பு, லட்சியங்கள், நிறுவனங்கள், தேசியக் கொடி, தேசியக் கீதத்தை மதித்தல். நினைவுக் குறிப்பு: 'அரசியலமைப்பு & கொடி'.",
                        "51A(b) [சுதந்திர லட்சியங்கள்]: சுதந்திரப் போராட்டத்தின் உயரிய லட்சியங்களைப் பேணிப் பின்பற்றுதல். நினைவுக் குறிப்பு: 'சுதந்திரப் போராட்டம்'.",
                        "51A(c) [இறையாண்மை & ஒருமைப்பாடு]: இந்தியாவின் இறையாண்மை, ஒற்றுமை, ஒருமைப்பாட்டைப் பேணுதல். நினைவுக் குறிப்பு: 'இறையாண்மை & ஒருமைப்பாடு'.",
                        "51A(d) [தேசியப் பாதுகாப்பு]: தேசத்தைப் பாதுகாத்தல் & தேவைப்படும்போது தேசிய சேவை ஆற்றுதல். நினைவுக் குறிப்பு: 'தேசியப் பாதுகாப்பு'.",
                        "51A(e) [சகோதரத்துவம் & பெண்கள்]: நல்லிணக்கம், சகோதரத்துவத்தை வளர்த்தல்; பெண்களின் கண்ணியத்தைக் குறைக்கும் பழக்கங்களைக் கைவிடுதல். நினைவுக் குறிப்பு: 'சகோதரத்துவம் & பெண்கள் கண்ணியம்'.",
                        "51A(f) [கூட்டுப் பண்பாடு]: கூட்டுப் பண்பாட்டின் வளமான பாரம்பரியத்தை மதித்து பேணுதல். நினைவுக் குறிப்பு: 'கூட்டுப் பண்பாடு'.",
                        "51A(g) [சுற்றுச்சூழல் & விலங்குகள்]: காடுகள், ஏரிகள், ஆறுகள், வனவிலங்குகளைப் பாதுகாத்தல்; உயிரினங்கள் மீது கருணை காட்டுதல். நினைவுக் குறிப்பு: 'சுற்றுச்சூழல் & வனவிலங்குகள்'.",
                        "51A(h) [அறிவியல் மனப்பான்மை]: அறிவியல் மனப்பான்மை, மனிதநேயம், ஆராய்ச்சி & சீர்திருத்த உணர்வை வளர்த்தல். நினைவுக் குறிப்பு: 'அறிவியல் மனப்பான்மை'.",
                        "51A(i) [பொதுச் சொத்து]: பொதுச் சொத்தைப் பாதுகாத்தல் & வன்முறையைக் கைவிடுதல். நினைவுக் குறிப்பு: 'பொதுச் சொத்து & வன்முறையின்மை'.",
                        "51A(j) [சிறப்பினை நோக்கிய முயற்சி]: தனிநபர் & கூட்டுச் செயல்பாடுகளில் சிறப்பினை நோக்கி முயலுதல். நினைவுக் குறிப்பு: 'சிறப்பினை நோக்கிய முயற்சி'.",
                        "51A(k) [குழந்தைகள் கல்வி]: 6-14 வயது குழந்தைக்குக் கல்வி வாய்ப்பளிக்கும் பெற்றோர்/பாதுகாவலர் கடமை. நினைவுக் குறிப்பு: 'குழந்தைகள் கல்வி 6-14'."
                    ]
                }
            }
        ],
        "sec_constitutional_history_timeline": [
            {
                "title": "1. Complete Timeline of Fundamental Duties (அடிப்படை கடமைகளின் முழுமையான காலவரிசை)",
                "points": {
                    "en": [
                        "26th January 1950 (Original Constitution): NO Fundamental Duties included. Constitution contained only Parts III (FR) and IV (DPSP).",
                        "1976 (Swaran Singh Committee): Congress Government appointed Committee under Sardar Swaran Singh during Emergency. Committee recommended 8 duties.",
                        "4th December 1976 (42nd Amendment Passed): 42nd CAA added Part IVA and Article 51A with TEN (10) Fundamental Duties (came into effect on 3rd Jan 1977).",
                        "1999 (Verma Committee): Justice J.S. Verma Committee identified existing legal provisions for enforcement of Fundamental Duties.",
                        "2002 (86th Amendment Passed): 86th CAA added the 11th Fundamental Duty [Article 51A(k)], making total 11 duties."
                    ],
                    "ta": [
                        "1950 ஜனவரி 26 (அசல் அரசியலமைப்பு): அடிப்படை கடமைகள் சேர்க்கப்படவில்லை. அரசியலமைப்பில் பகுதிகள் III (FR) மற்றும் IV (DPSP) மட்டுமே இருந்தன.",
                        "1976 (ஸ்வரன் சிங் குழு): அவசரநிலையின் போது சர்தார் ஸ்வரன் சிங் தலைமையில் காங்கிரஸ் அரசு குழுவை நியமித்தது. குழு 8 கடமைகளைப் பரிந்துரைத்தது.",
                        "1976 டிசம்பர் 4 (42வது திருத்தம் நிறைவேற்றம்): 42வது திருத்தம் பகுதி IVA மற்றும் உறுப்பு 51A உடன் பத்து (10) அடிப்படை கடமைகளைச் சேர்த்தது (1977 ஜனவரி 3 முதல் அமலுக்கு வந்தது).",
                        "1999 (வர்மா குழு): நீதிபதி ஜே.எஸ். வர்மா குழு அடிப்படை கடமைகளை அமல்படுத்துவதற்கான நிலவும் சட்ட விதிகளைக் கண்டறிந்தது.",
                        "2002 (86வது திருத்தம் நிறைவேற்றம்): 86வது திருத்தம் 11வது அடிப்படை கடமையை [உறுப்பு 51A(k)] சேர்த்து மொத்தம் 11 கடமைகளாக்கியது."
                    ]
                }
            }
        ],
        "sec_nature_enforceability_part3": [
            {
                "title": "1. Nature, Enforceability & Legal Status (இயல்பு, அமலாக்கம் & சட்டப்பூர்வ நிலை)",
                "points": {
                    "en": [
                        "Non-Justiciable Nature: Fundamental Duties cannot be directly enforced by judicial writs (Mandamus) in court without a supporting parliamentary law.",
                        "Not Legally Irrelevant: Non-justiciable does NOT mean legally useless! Duties guide statutory interpretation, test reasonableness of laws under Art 19, and possess moral and political force.",
                        "Parliamentary Enactment: Parliament can pass laws punishing non-compliance with any duty (e.g. Flag Code 2002, UAPA 1967, Wildlife Act 1972, Environmental Protection Act 1986).",
                        "Applicability: Applicable EXCLUSIVELY to Citizens of India (not to foreign visitors or aliens)."
                    ],
                    "ta": [
                        "அமல்படுத்த முடியாத இயல்பு: ஆதரவு அளிக்கும் நாடாளுமன்றச் சட்டம் இன்றி அடிப்படை கடமைகளை நேரடியாக நீதிமன்றத்தில் பேராணைகள் மூலம் அமல்படுத்த முடியாது.",
                        "சட்டப்பூர்வ பயனற்றவை அல்ல: அமல்படுத்த முடியாதது என்பதற்காக அவை சட்டப்பூர்வமாகப் பயனற்றவை என்று அர்த்தமல்ல! கடமைகள் சட்ட விளக்கத்திற்கு வழிகாட்டுகின்றன, உறுப்பு 19-ன் கீழ் சட்டங்களின் நியாயத் தன்மையைச் சோதிக்கின்றன, மேலும் தார்மீக மற்றும் அரசியல் சக்தியைக் கொண்டுள்ளன.",
                        "நாடாளுமன்ற சட்டமாக்கல்: கடமைகளை மீறுவதற்குத் தண்டனை அளிக்கும் சட்டங்களை நாடாளுமன்றம் நிறைவேற்றலாம் (எ.கா. கொடி குறியீடு 2002, UAPA 1967, வனவிலங்கு சட்டம் 1972, சுற்றுச்சூழல் பாதுகாப்புச் சட்டம் 1986).",
                        "பொருந்தும் எல்லை: இந்தியக் குடிமக்களுக்கு மட்டுமே பொருந்தும் (வெளிநாட்டுப் பயணிகள் அல்லது வெளிநாட்டினருக்கு அல்ல)."
                    ]
                }
            }
        ],
        "sec_tripartite_synthesis": [
            {
                "title": "1. Comprehensive Constitutional Triangle: FRs ↔ DPSP ↔ FDs (அரசியலமைப்பு முக்கோணம்: FRs ↔ DPSP ↔ FDs)",
                "points": {
                    "en": [
                        "Part III (Fundamental Rights): Guarantees political democracy and individual liberties. Justiciable in Supreme Court & High Courts.",
                        "Part IV (DPSP): Directs State towards social and economic democracy and Welfare State. Non-justiciable directives to State.",
                        "Part IVA (Fundamental Duties): Commands citizens towards responsible citizenship, national discipline, and social order. Non-justiciable duties of citizens.",
                        "Harmonious Construction Balance: Supreme Court (Minerva Mills 1980 & AIIMS 2002) ruled that the harmony between Part III, IV, and IVA forms the bedrock of constitutional democracy. Neither part overrides the other."
                    ],
                    "ta": [
                        "பகுதி III (அடிப்படை உரிமைகள்): அரசியல் ஜனநாயகம் மற்றும் தனிநபர் சுதந்திரங்களை உத்தரவாதம் செய்கிறது. உச்ச நீதிமன்றம் & உயர் நீதிமன்றங்களில் அமல்படுத்தக் கூடியவை.",
                        "பகுதி IV (DPSP): சமூக மற்றும் பொருளாதார ஜனநாயகம் மற்றும் நல அரசை நோக்கி அரசை வழிநடத்துகிறது. அரசுக்கான அமல்படுத்த முடியாத வழிகாட்டுதல்கள்.",
                        "பகுதி IVA (அடிப்படை கடமைகள்): பொறுப்பான குடியுரிமை, தேசிய ஒழுக்கம் மற்றும் சமூக ஒழுங்கை நோக்கி குடிமக்களுக்கு ஆணையிடுகிறது. குடிமக்களின் அமல்படுத்த முடியாத கடமைகள்.",
                        "இணக்கமான விளக்க சமநிலை: பகுதிகள் III, IV, மற்றும் IVA இடையேயான இணக்கமே அரசியலமைப்பு ஜனநாயகத்தின் அடித்தளமாகும் என்று உச்ச நீதிமன்றம் (மினர்வா மில்ஸ் 1980 & AIIMS 2002) தீர்ப்பளித்துள்ளது. எந்தப் பகுதியும் மற்றொன்றை விட உயர்ந்ததல்ல."
                    ]
                }
            }
        ],
        "sec_cases_legal_context_part3": [
            {
                "title": "1. Key Precedents on Fundamental Duties (அடிப்படை கடமைகள் பற்றிய முக்கிய தீர்ப்புகள்)",
                "points": {
                    "en": [
                        "Bijoe Emmanuel v. State of Kerala (1986): Standing respectfully during National Anthem fulfills Art 51A(a). Silent standing protected under Arts 19(1)(a) & 25.",
                        "AIIMS Students Union v. AIIMS (2002): Fundamental Duties are as important as Fundamental Rights and cannot be ignored during statutory interpretation.",
                        "MC Mehta v. Union of India (1997): Art 51A(g) invoked along with Art 48A & 21 to mandate environmental protection around Taj Mahal.",
                        "Animal Welfare Board v. A. Nagaraja (2014): Art 51A(g) compassion duty used to uphold animal welfare and restrict cruelty.",
                        "Aruna Roy v. Union of India (2002): Supreme Court upheld value-based education in schools as aligning with Article 51A(e) & (h) to promote national integration and secular values."
                    ],
                    "ta": [
                        "பிஜோய் இம்மானுவேல் vs கேரளா மாநிலம் (1986): தேசிய கீதத்தின் போது மரியாதையுடன் எழுந்து நிற்பதே உறுப்பு 51A(a)-ஐப் பூர்த்தி செய்கிறது. அமைதியாக நிற்பது உறுப்புகள் 19(1)(a) & 25-ன் கீழ் பாதுகாக்கப்படுகிறது.",
                        "AIIMS மாணவர் சங்கம் vs AIIMS (2002): அடிப்படை கடமைகள் அடிப்படை உரிமைகளுக்குச் சமமான முக்கியத்துவம் வாய்ந்தவை, சட்ட விளக்கத்தின் போது அவற்றைப் புறக்கணிக்க முடியாது.",
                        "எம்.சி. மேத்தா vs இந்திய யூனியன் (1997): தாஜ்மஹால் சுற்றியுள்ள சுற்றுச்சூழல் பாதுகாப்பை கட்டாயமாக்க உறுப்புகள் 51A(g), 48A & 21 பயன்படுத்தப்பட்டன.",
                        "விலங்கு நல வாரியம் vs ஏ. நாகராஜா (2014): விலங்கு நலனை உயர்த்தவும் கொடுமைகளைக் கட்டுப்படுத்தவும் உறுப்பு 51A(g) கருணைக் கடமை பயன்படுத்தப்பட்டது.",
                        "அருணா ராய் vs இந்திய யூனியன் (2002): பள்ளிகளில் மதிப்பு சார்ந்த கல்வியை வழங்குவது தேசிய ஒருமைப்பாடு மற்றும் மதச்சார்பற்ற மதிப்புகளை மேம்படுத்த உறுப்பு 51A(e) & (h) உடன் ஒத்துப்போகிறது என உச்ச நீதிமன்றம் உறுதி செய்தது."
                    ]
                }
            }
        ],
        "sec_environmental_education_triangles": [
            {
                "title": "1. The Two Major Constitutional Triangles (இரண்டு முக்கிய அரசியலமைப்பு முக்கோணங்கள்)",
                "points": {
                    "en": [
                        "Environmental Triangle: 1. Article 21 (FR: Right to clean environment). 2. Article 48A (DPSP: State duty to protect environment/forests). 3. Article 51A(g) (FD: Citizen duty to protect environment & wildlife).",
                        "Educational Triangle: 1. Article 21A (FR: State duty for free & compulsory education for 6-14 yrs). 2. Article 45 (DPSP: State directive for early childhood care below 6 yrs). 3. Article 51A(k) (FD: Parent/guardian duty to provide education opportunities for 6-14 yrs)."
                    ],
                    "ta": [
                        "சுற்றுச்சூழல் முக்கோணம்: 1. உறுப்பு 21 (FR: தூய்மையான சுற்றுச்சூழலுக்கான உரிமை). 2. உறுப்பு 48A (DPSP: சுற்றுச்சூழல்/காடுகளைப் பாதுகாக்கும் அரசு கடமை). 3. உறுப்பு 51A(g) (FD: சுற்றுச்சூழல் & வனவிலங்குகளைப் பாதுகாக்கும் குடிமகன் கடமை).",
                        "கல்வி முக்கோணம்: 1. உறுப்பு 21A (FR: 6-14 வயது குழந்தைகளுக்கு இலவச கட்டாயக் கல்வி வழங்கும் அரசு கடமை). 2. உறுப்பு 45 (DPSP: 6 வயதிற்குட்பட்ட குழந்தைகளுக்கு முன்பருவப் பராமரிப்பு வழங்கும் அரசு வழிகாட்டுதல்). 3. உறுப்பு 51A(k) (FD: 6-14 வயது குழந்தைக்குக் கல்வி வாய்ப்பளிக்கும் பெற்றோர்/பாதுகாவலர் கடமை)."
                    ]
                }
            }
        ],
        "sec_thematic_classification": [
            {
                "title": "1. Exam-Oriented 6-Fold Thematic Classification (தேர்வு சார்ந்த 6 வகை தலைப்பு வாரியான வகைப்பாடு)",
                "points": {
                    "en": [
                        "1. National & Constitutional Loyalty: 51A(a) [Flag/Anthem], 51A(c) [Sovereignty/Integrity], 51A(d) [National Defence].",
                        "2. National Integration & Social Harmony: 51A(b) [Freedom Ideals], 51A(e) [Brotherhood & Women's Dignity].",
                        "3. Cultural & Environmental Responsibility: 51A(f) [Composite Culture], 51A(g) [Environment & Wildlife].",
                        "4. Rational & Civic Responsibility: 51A(h) [Scientific Temper], 51A(i) [Public Property & Non-Violence].",
                        "5. National Progress & Excellence: 51A(j) [Striving for Excellence].",
                        "6. Educational Responsibility: 51A(k) [Child Education 6-14 Years].",
                        "Note: This classification is a conventional academic study tool and is NOT explicitly written in the Constitution."
                    ],
                    "ta": [
                        "1. தேசிய & அரசியலமைப்பு விசுவாசம்: 51A(a) [கொடி/கீதம்], 51A(c) [இறையாண்மை/ஒருமைப்பாடு], 51A(d) [தேசியப் பாதுகாப்பு].",
                        "2. தேசிய ஒருமைப்பாடு & சமூக நல்லிணக்கம்: 51A(b) [சுதந்திர லட்சியங்கள்], 51A(e) [சகோதரத்துவம் & பெண்கள் கண்ணியம்].",
                        "3. பண்பாட்டு & சுற்றுச்சூழல் பொறுப்பு: 51A(f) [கூட்டுப் பண்பாடு], 51A(g) [சுற்றுச்சூழல் & வனவிலங்குகள்].",
                        "4. பகுத்தறிவு & குடிமைப் பொறுப்பு: 51A(h) [அறிவியல் மனப்பான்மை], 51A(i) [பொதுச் சொத்து & வன்முறையின்மை].",
                        "5. தேசிய முன்னேற்றம் & சிறப்பு: 51A(j) [சிறப்பினை நோக்கிய முயற்சி].",
                        "6. கல்விப் பொறுப்பு: 51A(k) [6-14 வயது குழந்தைகள் கல்வி].",
                        "குறிப்பு: இவ்வகைப்பாடு ஒரு மரபுவழி கல்வி படிப்பு சாதனமே தவிர, அரசியலமைப்பில் வெளிப்படையாக எழுதப்படவில்லை."
                    ]
                }
            }
        ],
        "sec_traps_revision_part3": [
            {
                "title": "TNPSC Traps & Complete 2-Minute Revision (டிஎன்பிஎஸ்சி பொறிகள் & 2 நிமிட முழுமையான திருப்புதல்)",
                "points": {
                    "en": [
                        "Part IVA (Article 51A) contains Fundamental Duties. Added by 42nd CAA 1976 (10 duties) & 86th CAA 2002 (11th duty).",
                        "Swaran Singh Committee recommended 8 duties; duty to pay taxes and penalties were REJECTED.",
                        "Article 21A (FR: State duty for 6-14 yrs) vs Article 45 (DPSP: State care below 6 yrs) vs Article 51A(k) (FD: Parent duty for 6-14 yrs).",
                        "Article 48A (DPSP: State environment duty) vs Article 51A(g) (FD: Citizen environment duty).",
                        "Fundamental Duties apply EXCLUSIVELY to Citizens and are non-justiciable without supporting parliamentary statutes."
                    ],
                    "ta": [
                        "பகுதி IVA (உறுப்பு 51A) அடிப்படை கடமைகளைக் கொண்டுள்ளது. 42வது திருத்தம் 1976 (10 கடமைகள்) & 86வது திருத்தம் 2002 (11வது கடமை) மூலம் சேர்க்கப்பட்டது.",
                        "ஸ்வரன் சிங் குழு 8 கடமைகளைப் பரிந்துரைத்தது; வரி செலுத்தும் கடமை மற்றும் அபராதங்கள் நிராகரிக்கப்பட்டன.",
                        "உறுப்பு 21A (FR: 6-14 வயதினருக்கு அரசு கடமை) vs உறுப்பு 45 (DPSP: 6 வயதிற்குட்பட்டோருக்கு அரசு பராமரிப்பு) vs உறுப்பு 51A(k) (FD: 6-14 வயதினருக்குப் பெற்றோர் கடமை).",
                        "உறுப்பு 48A (DPSP: அரசு சுற்றுச்சூழல் கடமை) vs உறுப்பு 51A(g) (FD: குடிமகன் சுற்றுச்சூழல் கடமை).",
                        "அடிப்படை கடமைகள் குடிமக்களுக்கு மட்டுமே பொருந்தும் மற்றும் நாடாளுமன்றச் சட்டங்கள் இன்றி நேரடியாக அமல்படுத்த முடியாதவை."
                    ]
                }
            }
        ],
        "tables": [
            {
                "id": "tbl_art21a_vs_art45_vs_art51ak",
                "title_en": "1. Education Triangle: Article 21A vs Article 45 vs Article 51A(k)",
                "title_ta": "1. கல்வி முக்கோணம்: உறுப்பு 21A vs உறுப்பு 45 vs உறுப்பு 51A(k)",
                "headers_en": ["Dimension", "Article 21A (Fundamental Right)", "Article 45 (Directive Principle)", "Article 51A(k) (Fundamental Duty)"],
                "headers_ta": ["பரிமாணம்", "உறுப்பு 21A (அடிப்படை உரிமை)", "உறுப்பு 45 (வழிகாட்டு நெறிமுறை)", "உறுப்பு 51A(k) (அடிப்படை கடமை)"],
                "rows_en": [
                    ["Enshrined Part", "Part III", "Part IV", "Part IVA"],
                    ["Duty Bearer", "The STATE (Government)", "The STATE (Government)", "Parent or Guardian"],
                    ["Target Age Group", "6 to 14 years", "Below 6 years (Early Childhood)", "6 to 14 years"],
                    ["Legal Nature", "Justiciable (Court writ against State)", "Non-justiciable Directive", "Non-justiciable Duty"],
                    ["Core Mandate", "Free & compulsory education", "Early childhood care & education", "Provide educational opportunities"]
                ],
                "rows_ta": [
                    ["பொறிக்கப்பட்டுள்ள பகுதி", "பகுதி III", "பகுதி IV", "பகுதி IVA"],
                    ["கடமைப் பொறுப்பாளி", "அரசு (Government)", "அரசு (Government)", "பெற்றோர் அல்லது பாதுகாவலர்"],
                    ["இலக்கு வயதுக் குழு", "6 முதல் 14 வயது வரை", "6 வயதிற்குட்பட்டோர் (முன்பருவக் கல்வி)", "6 முதல் 14 வயது வரை"],
                    ["சட்டப்பூர்வ இயல்பு", "அமல்படுத்தக் கூடியது (அரசுக்கு எதிராக பேராணை)", "அமல்படுத்த முடியாத வழிகாட்டுதல்", "அமல்படுத்த முடியாத கடமை"],
                    ["முதன்மை கட்டளை", "இலவச & கட்டாயக் கல்வி", "முன்பருவப் பராமரிப்பு & கல்வி", "கல்வி வாய்ப்புகளை வழங்குதல்"]
                ]
            },
            {
                "id": "tbl_42nd_vs_86th_amendment_full",
                "title_en": "2. 42nd Amendment (1976) vs 86th Amendment (2002) Comparison",
                "title_ta": "2. 42வது திருத்தம் (1976) vs 86வது திருத்தம் (2002) ஒப்பீடு",
                "headers_en": ["Dimension", "42nd Amendment Act, 1976", "86th Amendment Act, 2002"],
                "headers_ta": ["பரிமாணம்", "42வது திருத்தச் சட்டம், 1976", "86வது திருத்தச் சட்டம், 2002"],
                "rows_en": [
                    ["Prime Minister", "Indira Gandhi", "Atal Bihari Vajpayee"],
                    ["Duties Inserted", "Added Part IVA & Art 51A with 10 Original Duties", "Added 11th Duty [Article 51A(k)]"],
                    ["Committee / Commission", "Swaran Singh Committee", "Venkatachaliah Commission / Verma Committee"],
                    ["Key Focus", "Civic discipline, national integrity, environment", "Right & Duty for Child Education (6-14 yrs)"],
                    ["Other Constitutional Changes", "Added Preamble terms, DPSP Arts 39A, 43A, 48A", "Added Art 21A (FR) and modified Art 45 (DPSP)"]
                ],
                "rows_ta": [
                    ["பிரதமர்", "இந்திரா காந்தி", "அடல் பிஹாரி வாஜ்பாய்"],
                    ["சேர்க்கப்பட்ட கடமைகள்", "பகுதி IVA & உறுப்பு 51A உடன் அசல் 10 கடமைகளைச் சேர்த்தது", "11வது கடமையைச் சேர்த்தது [உறுப்பு 51A(k)]"],
                    ["குழு / ஆணையம்", "ஸ்வரன் சிங் குழு", "வெங்கடாசலையா ஆணையம் / வர்மா குழு"],
                    ["முக்கிய கவனம்", "குடிமை ஒழுக்கம், தேசிய ஒருமைப்பாடு, சுற்றுச்சூழல்", "குழந்தைகள் கல்வி உரிமை & கடமை (6-14 வயது)"],
                    ["இதர அரசியலமைப்பு மாற்றங்கள்", "முகப்புரைச் சொற்கள், DPSP உறுப்புகள் 39A, 43A, 48A சேர்க்கப்பட்டன", "உறுப்பு 21A (FR) சேர்க்கப்பட்டு உறுப்பு 45 (DPSP) மாற்றப்பட்டது"]
                ]
            },
            {
                "id": "tbl_original10_vs_present11",
                "title_en": "3. Original 10 Duties (1976) vs Present 11 Duties (2002)",
                "title_ta": "3. அசல் 10 கடமைகள் (1976) vs தற்போதைய 11 கடமைகள் (2002)",
                "headers_en": ["Feature", "Original 10 Duties (1976)", "Present 11 Duties (2002)"],
                "headers_ta": ["அம்சம்", "அசல் 10 கடமைகள் (1976)", "தற்போதைய 11 கடமைகள் (2002)"],
                "rows_en": [
                    ["Constitutional Status", "Inserted by 42nd Amendment Act 1976", "Expanded by 86th Amendment Act 2002"],
                    ["Article Scope", "Article 51A(a) to 51A(j)", "Article 51A(a) to 51A(k)"],
                    ["Education Duty Included?", "NO child education duty present", "YES, 11th duty Art 51A(k) added for 6-14 yrs education"]
                ],
                "rows_ta": [
                    ["அரசியலமைப்பு நிலை", "42வது திருத்தச் சட்டம் 1976 மூலம் சேர்க்கப்பட்டது", "86வது திருத்தச் சட்டம் 2002 மூலம் விரிவாக்கப்பட்டது"],
                    ["உறுப்பு எல்லை", "உறுப்பு 51A(a) முதல் 51A(j) வரை", "உறுப்பு 51A(a) முதல் 51A(k) வரை"],
                    ["கல்விக் கடமை சேர்க்கப்பட்டதா?", "குழந்தைகள் கல்விக் கடமை இடம்பெறவில்லை", "ஆம், 6-14 வயது கல்விக்காக 11வது கடமை உறுப்பு 51A(k) சேர்க்கப்பட்டது"]
                ]
            },
            {
                "id": "tbl_fr_vs_dpsp_vs_fd_full",
                "title_en": "4. Fundamental Rights vs DPSP vs Fundamental Duties Master Comparison",
                "title_ta": "4. அடிப்படை உரிமைகள் vs DPSP vs அடிப்படை கடமைகள் முதன்மை ஒப்பீடு",
                "headers_en": ["Feature", "Fundamental Rights (Part III)", "DPSP (Part IV)", "Fundamental Duties (Part IVA)"],
                "headers_ta": ["அம்சம்", "அடிப்படை உரிமைகள் (பகுதி III)", "DPSP (பகுதி IV)", "அடிப்படை கடமைகள் (பகுதி IVA)"],
                "rows_en": [
                    ["Addressing Whom", "State & Individuals", "State (Government)", "Citizens of India"],
                    ["Justiciability", "Justiciable (Court Writ)", "Non-justiciable", "Non-justiciable"],
                    ["Country Borrowed", "USA (Bill of Rights)", "Ireland (1937)", "USSR (Soviet Union)"],
                    ["Sanction", "Legal Sanction", "Moral & Political Sanction", "Moral & Statutory Sanction"],
                    ["Goal", "Political Democracy", "Social & Economic Welfare", "Responsible Citizenship"]
                ],
                "rows_ta": [
                    ["யாருக்கு ஆணையிடுகிறது", "அரசு & நபர்கள்", "அரசு (Government)", "இந்தியக் குடிமக்கள்"],
                    ["நீதிமன்ற அமலாக்கம்", "அமல்படுத்தக் கூடியது (பேராணை)", "அமல்படுத்த முடியாதது", "அமல்படுத்த முடியாதது"],
                    ["பெறப்பட்ட நாடு", "அமெரிக்கா (Bill of Rights)", "அயர்லாந்து (1937)", "சோவியத் யூனியன் (USSR)"],
                    ["அதிகாரம் / ஆதரவு", "சட்டப்பூர்வ அதிகாரம்", "தார்மீக & அரசியல் அதிகாரம்", "தார்மீக & சட்டப்பூர்வ அதிகாரம்"],
                    ["இலக்கு", "அரசியல் ஜனநாயகம்", "சமூக & பொருளாதார நலன்", "பொறுப்பான குடியுரிமை"]
                ]
            },
            {
                "id": "tbl_environmental_triangle",
                "title_en": "5. Environmental Constitutional Triangle: Art 48A vs Art 51A(g) vs Art 21",
                "title_ta": "5. சுற்றுச்சூழல் அரசியலமைப்பு முக்கோணம்: உறுப்பு 48A vs உறுப்பு 51A(g) vs உறுப்பு 21",
                "headers_en": ["Constitutional Provision", "Category", "Mandate / Duty Bearer", "Key MC Mehta / Nagaraja Takeaway"],
                "headers_ta": ["அரசியலமைப்பு விதி", "பிரிவு", "கட்டளை / கடமைப் பொறுப்பாளி", "முக்கிய மேத்தா / நாகராஜா தீர்ப்பு"],
                "rows_en": [
                    ["Article 21", "Fundamental Right (Part III)", "State must guarantee clean air & water for Right to Life", "Right to wholesome environment is a fundamental right"],
                    ["Article 48A", "DPSP (Part IV)", "State must protect environment, forests & wildlife", "Directs State policy for pollution control & Taj Mahal protection"],
                    ["Article 51A(g)", "Fundamental Duty (Part IVA)", "Citizen must protect forests, lakes, rivers & show compassion", "Places fundamental duty on citizens to refrain from polluting & show animal compassion"]
                ],
                "rows_ta": [
                    ["உறுப்பு 21", "அடிப்படை உரிமை (பகுதி III)", "வாழும் உரிமைக்கு அரசு தூய்மையான காற்று & நீரை உறுதி செய்ய வேண்டும்", "ஆரோக்கியமான சுற்றுச்சூழலுக்கான உரிமை ஒரு அடிப்படை உரிமை"],
                    ["உறுப்பு 48A", "DPSP (பகுதி IV)", "அரசு சுற்றுச்சூழல், காடுகள் & வனவிலங்குகளைப் பாதுகாக்க வேண்டும்", "மாசு கட்டுப்பாடு & தாஜ்மஹால் பாதுகாப்பிற்கு அரசு கொள்கையை வழிநடத்துகிறது"],
                    ["உறுப்பு 51A(g)", "அடிப்படை கடமை (பகுதி IVA)", "குடிமகன் காடுகள், ஏரிகள், ஆறுகளைப் பாதுகாத்து கருணை காட்ட வேண்டும்", "மாசுபடுத்தாமல் இருக்கவும் விலங்குகள் மீது கருணை காட்டவும் குடிமக்களுக்கு கடமை விதிக்கிறது"]
                ]
            },
            {
                "id": "tbl_part3_vs_part4_vs_part4a",
                "title_en": "6. Constitutional Architecture: Part III vs Part IV vs Part IVA",
                "title_ta": "6. அரசியலமைப்பு அமைப்பு: பகுதி III vs பகுதி IV vs பகுதி IVA",
                "headers_en": ["Part", "Articles Covered", "Chapter Title", "Enactment Year"],
                "headers_ta": ["பகுதி", "உள்ளடங்கிய உறுப்புகள்", "அத்தியாயத் தலைப்பு", "இயற்றப்பட்ட ஆண்டு"],
                "rows_en": [
                    ["Part III", "Articles 12 to 35", "Fundamental Rights", "1950 (Original Constitution)"],
                    ["Part IV", "Articles 36 to 51", "Directive Principles of State Policy", "1950 (Original Constitution)"],
                    ["Part IVA", "Article 51A (clauses a to k)", "Fundamental Duties", "1976 (42nd CAA) & 2002 (86th CAA)"]
                ],
                "rows_ta": [
                    ["பகுதி III", "உறுப்புகள் 12 முதல் 35 வரை", "அடிப்படை உரிமைகள்", "1950 (அசல் அரசியலமைப்பு)"],
                    ["பகுதி IV", "உறுப்புகள் 36 முதல் 51 வரை", "அரசு வழிகாட்டு நெறிமுறைகள்", "1950 (அசல் அரசியலமைப்பு)"],
                    ["பகுதி IVA", "உறுப்பு 51A (உட்பிரிவுகள் a முதல் k வரை)", "அடிப்படை கடமைகள்", "1976 (42வது திருத்தம்) & 2002 (86வது திருத்தம்)"]
                ]
            },
            {
                "id": "tbl_justiciable_vs_nonjusticiable",
                "title_en": "7. Justiciable vs Non-Justiciable Constitutional Provisions",
                "title_ta": "7. அமல்படுத்தக் கூடிய vs அமல்படுத்த முடியாத அரசியலமைப்பு விதிகள்",
                "headers_en": ["Aspect", "Justiciable Provisions (e.g. Part III FRs)", "Non-Justiciable Provisions (e.g. Part IV DPSP & Part IVA FDs)"],
                "headers_ta": ["பகுதி", "அமல்படுத்தக் கூடிய விதிகள் (எ.கா. பகுதி III FRs)", "அமல்படுத்த முடியாத விதிகள் (எ.கா. பகுதி IV DPSP & பகுதி IVA FDs)"],
                "rows_en": [
                    ["Court Enforcement", "Direct writ remedy under Art 32 / 226", "No direct writ remedy without parliamentary enabling statute"],
                    ["Legal Remedies", "Court can invalidate non-compliant laws", "Court uses them for statutory construction & evaluating Art 19 reasonableness"],
                    ["Primary Focus", "Enforceable legal rights", "Moral, policy, and civic principles"]
                ],
                "rows_ta": [
                    ["நீதிமன்ற அமலாக்கம்", "உறுப்பு 32 / 226-ன் கீழ் நேரடி பேராணை பரிகாரம்", "நாடாளுமன்ற ஆதரவுச் சட்டம் இன்றி நேரடி பேராணை பரிகாரம் இல்லை"],
                    ["சட்டப் பரிகாரங்கள்", "மீறும் சட்டங்களை நீதிமன்றம் செல்லாததாக்கலாம்", "சட்ட விளக்கம் & உறுப்பு 19 நியாயத் தன்மையை மதிப்பிட நீதிமன்றம் பயன்படுத்துகிறது"],
                    ["முதன்மை கவனம்", "அமல்படுத்தக்கூடிய சட்டப்பூர்வ உரிமைகள்", "தார்மீக, கொள்கை மற்றும் குடிமைத் தத்துவங்கள்"]
                ]
            },
            {
                "id": "tbl_51a_ak_master_reference",
                "title_en": "8. Complete Article 51A(a) to 51A(k) 11 Duties Master Reference Table",
                "title_ta": "8. முழுமையான உறுப்புகள் 51A(a) முதல் 51A(k) வரையிலான 11 கடமைகள் முதன்மை அட்டவணை",
                "headers_en": ["Clause", "Core Subject", "Key English Keyword", "Key Tamil Keyword"],
                "headers_ta": ["உட்பிரிவு", "முதன்மை விஷயம்", "முதன்மை ஆங்கில சொல்", "முதன்மை தமிழ் சொல்"],
                "rows_en": [
                    ["51A(a)", "Constitution, Flag, Anthem", "Respect National Symbols", "தேசிய சின்னங்களை மதித்தல்"],
                    ["51A(b)", "Freedom Struggle Ideals", "Cherish Freedom Ideals", "சுதந்திர லட்சியங்களைப் பேணுதல்"],
                    ["51A(c)", "Sovereignty, Unity, Integrity", "Protect Sovereignty & Integrity", "இறையாண்மை & ஒருமைப்பாடு"],
                    ["51A(d)", "National Defence & Service", "Defend Country & Render Service", "தேசியப் பாதுகாப்பு & சேவை"],
                    ["51A(e)", "Brotherhood & Women's Dignity", "Promote Harmony & Respect Women", "சகோதரத்துவம் & பெண்கள் கண்ணியம்"],
                    ["51A(f)", "Composite Culture & Heritage", "Preserve Composite Culture", "கூட்டுப் பண்பாட்டைப் பேணுதல்"],
                    ["51A(g)", "Environment & Animal Compassion", "Protect Environment & Wildlife", "சுற்றுச்சூழல் & உயிரினக் கருணை"],
                    ["51A(h)", "Scientific Temper & Reform", "Develop Scientific Temper", "அறிவியல் மனப்பான்மை"],
                    ["51A(i)", "Public Property & Non-Violence", "Safeguard Public Property", "பொதுச் சொத்துப் பாதுகாப்பு"],
                    ["51A(j)", "Individual & Collective Excellence", "Strive Towards Excellence", "சிறப்பினை நோக்கிய முயற்சி"],
                    ["51A(k)", "Child Education (6-14 Years)", "Parent Duty for Child Education", "6-14 வயது குழந்தைகள் கல்வி"]
                ],
                "rows_ta": [
                    ["51A(a)", "அரசியலமைப்பு, கொடி, கீதம்", "Respect National Symbols", "தேசிய சின்னங்களை மதித்தல்"],
                    ["51A(b)", "சுதந்திரப் போராட்ட லட்சியங்கள்", "Cherish Freedom Ideals", "சுதந்திர லட்சியங்களைப் பேணுதல்"],
                    ["51A(c)", "இறையாண்மை, ஒற்றுமை, ஒருமைப்பாடு", "Protect Sovereignty & Integrity", "இறையாண்மை & ஒருமைப்பாடு"],
                    ["51A(d)", "தேசியப் பாதுகாப்பு & சேவை", "Defend Country & Render Service", "தேசியப் பாதுகாப்பு & சேவை"],
                    ["51A(e)", "சகோதரத்துவம் & பெண்கள் கண்ணியம்", "Promote Harmony & Respect Women", "சகோதரத்துவம் & பெண்கள் கண்ணியம்"],
                    ["51A(f)", "கூட்டுப் பண்பாடு & பாரம்பரியம்", "Preserve Composite Culture", "கூட்டுப் பண்பாட்டைப் பேணுதல்"],
                    ["51A(g)", "சுற்றுச்சூழல் & உயிரினக் கருணை", "Protect Environment & Wildlife", "சுற்றுச்சூழல் & உயிரினக் கருணை"],
                    ["51A(h)", "அறிவியல் மனப்பான்மை & சீர்திருத்தம்", "Develop Scientific Temper", "அறிவியல் மனப்பான்மை"],
                    ["51A(i)", "பொதுச் சொத்து & வன்முறையின்மை", "Safeguard Public Property", "பொதுச் சொத்துப் பாதுகாப்பு"],
                    ["51A(j)", "தனிநபர் & கூட்டுச் சிறப்பு", "Strive Towards Excellence", "சிறப்பினை நோக்கிய முயற்சி"],
                    ["51A(k)", "குழந்தைகள் கல்வி (6-14 வயது)", "Parent Duty for Child Education", "6-14 வயது குழந்தைகள் கல்வி"]
                ]
            },
            {
                "id": "tbl_swaran_singh_vs_implementation",
                "title_en": "9. Swaran Singh Committee Recommendations vs Constitutional Implementation",
                "title_ta": "9. ஸ்வரன் சிங் குழு பரிந்துரைகள் vs அரசியலமைப்பு அமலாக்கம்",
                "headers_en": ["Recommendation", "Status in 42nd CAA 1976 / Art 51A", "Reason / Explanation"],
                "headers_ta": ["பரிந்துரை", "42வது திருத்தம் 1976 / உறுப்பு 51A-ல் நிலை", "காரணம் / விளக்கம்"],
                "rows_en": [
                    ["Inclusion of Fundamental Duties Chapter", "ACCEPTED", "Part IVA & Article 51A inserted in Constitution"],
                    ["Total Number of Duties Recommended (8)", "MODIFIED & EXPANDED", "Parliament enacted 10 duties in 1976 (adding duties on flag, culture, etc.)"],
                    ["Duty to Pay Taxes", "REJECTED & OMITTED", "Parliament did not include tax duty under Article 51A"],
                    ["Penalty / Punishment for non-compliance", "REJECTED & OMITTED", "Duties left non-justiciable without automatic penalties"],
                    ["Immunity of penalty laws from FR challenge", "REJECTED & OMITTED", "Laws enforcing duties remain subject to judicial review"]
                ],
                "rows_ta": [
                    ["அடிப்படை கடமைகள் அத்தியாயம் சேர்ப்பு", "ஏற்கப்பட்டது", "பகுதி IVA & உறுப்பு 51A அரசியலமைப்பில் இணைக்கப்பட்டன"],
                    ["பரிந்துரைக்கப்பட்ட கடமைகளின் எண்ணிக்கை (8)", "மாற்றப்பட்டு விரிவாக்கப்பட்டது", "நாடாளுமன்றம் 1976-ல் 10 கடமைகளை இயற்றியது (கொடி, பண்பாடு போன்றவற்றைச் சேர்த்து)"],
                    ["வரி செலுத்தும் கடமை", "நிராகரிக்கப்பட்டு விடுக்கப்பட்டது", "உறுப்பு 51A-ன் கீழ் வரி செலுத்தும் கடமையை நாடாளுமன்றம் சேர்க்கவில்லை"],
                    ["கடமை மீறலுக்கான தண்டனை / அபராதம்", "நிராகரிக்கப்பட்டு விடுக்கப்பட்டது", "தானியங்கி அபராதங்களின்றி கடமைகள் அமல்படுத்த முடியாதவையாக விடப்பட்டன"],
                    ["தண்டனைச் சட்டங்களுக்கு FR சவாலிலிருந்து விலக்கு", "நிராகரிக்கப்பட்டு விடுக்கப்பட்டது", "கடமைகளை அமல்படுத்தும் சட்டங்கள் நீதித்துறை ஆய்விற்கு உட்பட்டவையாகவே உள்ளன"]
                ]
            },
            {
                "id": "tbl_fd_vs_fr_practical_relationship",
                "title_en": "10. Fundamental Duties vs Fundamental Rights — Practical Relationship & Judicial Balance",
                "title_ta": "10. அடிப்படை கடமைகள் vs அடிப்படை உரிமைகள் — நடைமுறைத் தொடர்பும் நீதித்துறை சமநிலையும்",
                "headers_en": ["Practical Scenario / Dimension", "Fundamental Right Aspect", "Fundamental Duty Aspect", "Judicial Balance Rule"],
                "headers_ta": ["நடைமுறைச் சூழல் / பரிமாணம்", "அடிப்படை உரிமை அம்சம்", "அடிப்படை கடமை அம்சம்", "நீதித்துறை சமநிலை விதி"],
                "rows_en": [
                    ["National Anthem Respect", "Art 19(1)(a) Speech & Art 25 Religious Freedom", "Art 51A(a) Respect National Anthem", "Bijoe Emmanuel 1986: Standing respectfully satisfies Art 51A(a) without violating Art 19/25"],
                    ["Environmental Protection", "Art 21 Right to Clean Environment", "Art 51A(g) Citizen Duty to protect rivers/forests", "MC Mehta 1997: Court enforces duty on citizens/units to protect Art 21 clean environment"],
                    ["Protests & Demonstrations", "Art 19(1)(b) Freedom of Assembly", "Art 51A(i) Duty to abjure violence & protect public property", "2009 SC Guidelines: Violent damage to public property nullifies peaceful assembly right"]
                ],
                "rows_ta": [
                    ["தேசிய கீத மரியாதை", "உறுப்பு 19(1)(a) பேச்சுரிமை & உறுப்பு 25 மத சுதந்திரம்", "உறுப்பு 51A(a) தேசிய கீதத்தை மதித்தல்", "பிஜோய் இம்மானுவேல் 1986: மரியாதையுடன் எழுந்து நிற்பது உறுப்புகள் 19/25-ஐ மீறாமல் உறுப்பு 51A(a)-ஐப் பூர்த்தி செய்கிறது"],
                    ["சுற்றுச்சூழல் பாதுகாப்பு", "உறுப்பு 21 தூய்மையான சுற்றுச்சூழலுக்கான உரிமை", "உறுப்பு 51A(g) ஆறுகள்/காடுகளைப் பாதுகாக்கும் குடிமகன் கடமை", "எம்.சி. மேத்தா 1997: உறுப்பு 21 தூய்மை சுற்றுச்சூழலைப் பாதுகாக்கக் குடிமக்கள் மீது கடமையை நீதிமன்றம் அமல்படுத்துகிறது"],
                    ["போராட்டங்கள் & ஆர்ப்பாட்டங்கள்", "உறுப்பு 19(1)(b) அமைதியாகக் கூடும் சுதந்திரம்", "உறுப்பு 51A(i) வன்முறையைக் கைவிட்டு பொதுச் சொத்தைப் பாதுகாக்கும் கடமை", "2009 உச்ச நீதிமன்ற விதிகள்: பொதுச் சொத்து சேதம் அமைதியாகக் கூடும் உரிமையை ரத்து செய்கிறது"]
                ]
            }
        ],
        "mind_map": [
            {
                "title": "Fundamental Duties Complete Chapter (Part IVA & Article 51A)",
                "short_label": "FD Master Map",
                "children": [
                    {
                        "title": "1. Constitutional History & Amendments",
                        "short_label": "History & CAA",
                        "children": [
                            {
                                "title": "Original 1950 Constitution: NO Fundamental Duties",
                                "short_label": "1950 None"
                            },
                            {
                                "title": "Swaran Singh Committee 1976: Rec. 8 duties (Tax duty & Penalty REJECTED)",
                                "short_label": "Swaran Singh"
                            },
                            {
                                "title": "42nd CAA 1976: Added Part IVA & Art 51A (Original 10 Duties)",
                                "short_label": "42nd CAA 10"
                            },
                            {
                                "title": "86th CAA 2002: Added 11th Duty Art 51A(k) (Child Education 6-14 yrs)",
                                "short_label": "86th CAA 11th"
                            }
                        ]
                    },
                    {
                        "title": "2. Complete 11 Duties Matrix (51A(a) to 51A(k))",
                        "short_label": "All 11 Duties",
                        "children": [
                            {
                                "title": "51A(a) Flag/Anthem | 51A(b) Freedom Ideals | 51A(c) Sovereignty",
                                "short_label": "a-b-c Duties"
                            },
                            {
                                "title": "51A(d) Defence | 51A(e) Brotherhood/Women | 51A(f) Culture",
                                "short_label": "d-e-f Duties"
                            },
                            {
                                "title": "51A(g) Environment | 51A(h) Science | 51A(i) Public Property",
                                "short_label": "g-h-i Duties"
                            },
                            {
                                "title": "51A(j) Excellence | 51A(k) Child Education (6-14 yrs)",
                                "short_label": "j-k Duties"
                            }
                        ]
                    },
                    {
                        "title": "3. Constitutional Triangles & Case Laws",
                        "short_label": "Triangles & Cases",
                        "children": [
                            {
                                "title": "Education Triangle: Art 21A (FR) <-> Art 45 (DPSP) <-> Art 51A(k) (FD)",
                                "short_label": "Education Trio"
                            },
                            {
                                "title": "Environment Triangle: Art 21 (FR) <-> Art 48A (DPSP) <-> Art 51A(g) (FD)",
                                "short_label": "Env Trio"
                            },
                            {
                                "title": "Key Cases: Bijoe Emmanuel 1986, MC Mehta 1997, AIIMS 2002, Nagaraja 2014",
                                "short_label": "Landmark Cases"
                            }
                        ]
                    }
                ]
            }
        ],
        "tnpsc_traps": [
            {
                "title": "1. Article 21A vs Article 45 vs Article 51A(k) Age & Duty Bearer Trap (கல்வி உறுப்புகள் வயது & கடமையாளி பொறி)",
                "points": {
                    "en": [
                        "TRAP: Statements claiming Article 51A(k) places a duty on the State for children aged 0–6 years.",
                        "FACT: 1. Article 21A (FR) = STATE duty for children aged 6 to 14 years. 2. Article 45 (DPSP) = STATE directive for children BELOW 6 years. 3. Article 51A(k) (FD) = PARENT/GUARDIAN duty for children aged 6 to 14 years!"
                    ],
                    "ta": [
                        "பொறி: உறுப்பு 51A(k) 0–6 வயது குழந்தைகளுக்கு அரசுக்குக் கடமை விதிக்கிறது என்ற கூற்று.",
                        "உண்மை: 1. உறுப்பு 21A (FR) = 6 முதல் 14 வயது குழந்தைகளுக்கு அரசுக் கடமை. 2. உறுப்பு 45 (DPSP) = 6 வயதிற்குட்பட்ட குழந்தைகளுக்கு அரசு வழிகாட்டுதல். 3. உறுப்பு 51A(k) (FD) = 6 முதல் 14 வயது குழந்தைகளுக்குப் பெற்றோர்/பாதுகாவலர் கடமை!"
                    ]
                }
            },
            {
                "title": "2. Exact Number of Fundamental Duties Trap (அடிப்படை கடமைகளின் துல்லியமான எண்ணிக்கை பொறி)",
                "points": {
                    "en": [
                        "TRAP: Confusing the number of duties added by 42nd Amendment vs 86th Amendment vs original 1950 Constitution.",
                        "FACT: 1950 Original Constitution = ZERO duties. 42nd CAA (1976) = 10 duties added. 86th CAA (2002) = 1 duty added [Art 51A(k)]. Total present count = EXACTLY 11 duties!"
                    ],
                    "ta": [
                        "பொறி: 42வது திருத்தம் vs 86வது திருத்தம் vs அசல் 1950 அரசியலமைப்பு ஆகியவற்றில் உள்ள கடமைகளின் எண்ணிக்கையைக் குழப்பிக் கொள்ளுதல்.",
                        "உண்மை: 1950 அசல் அரசியலமைப்பு = 0 கடமைகள். 42வது திருத்தம் (1976) = 10 கடமைகள் சேர்க்கப்பட்டன. 86வது திருத்தம் (2002) = 1 கடமை சேர்க்கப்பட்டது [உறுப்பு 51A(k)]. தற்போதைய மொத்த எண்ணிக்கை = சரியாக 11 கடமைகள்!"
                    ]
                }
            },
            {
                "title": "3. Swaran Singh Committee Rejected Recommendations Trap (ஸ்வரன் சிங் குழு நிராகரிக்கப்பட்ட பரிந்துரைகள் பொறி)",
                "points": {
                    "en": [
                        "TRAP: MCQ statement claiming Swaran Singh Committee recommended 10 duties and that duty to pay taxes is in Article 51A.",
                        "FACT: Swaran Singh Committee recommended 8 duties. Parliament enacted 10 duties. 'Duty to Pay Taxes' and 'Penalties for Non-compliance' were REJECTED by Parliament and are NOT in Article 51A!"
                    ],
                    "ta": [
                        "பொறி: ஸ்வரன் சிங் குழு 10 கடமைகளைப் பரிந்துரைத்தது என்றோ அல்லது வரி செலுத்தும் கடமை உறுப்பு 51A-ல் உள்ளது என்றோ கூறும் வினா கூற்று.",
                        "உண்மை: ஸ்வரன் சிங் குழு 8 கடமைகளைப் பரிந்துரைத்தது. நாடாளுமன்றம் 10 கடமைகளை இயற்றியது. 'வரி செலுத்தும் கடமை' மற்றும் 'கடமை மீறலுக்கான அபராதங்கள்' நாடாளுமன்றத்தால் நிராகரிக்கப்பட்டன, அவை உறுப்பு 51A-ல் இல்லை!"
                    ]
                }
            },
            {
                "title": "4. Non-Justiciable vs Legally Irrelevant Trap (அமல்படுத்த முடியாத vs சட்டப்பூர்வ பயனற்ற பொறி)",
                "points": {
                    "en": [
                        "TRAP: Believing non-justiciable means Fundamental Duties have zero legal or judicial value.",
                        "FACT: Non-justiciable means no direct court writ for non-performance. However, duties guide courts in statutory interpretation and evaluating 'reasonableness' under Article 19, and Parliament has enacted statutes enforcing them."
                    ],
                    "ta": [
                        "பொறி: அமல்படுத்த முடியாதது என்பதால் அடிப்படை கடமைகளுக்குச் சட்டப்பூர்வ அல்லது நீதித்துறை மதிப்பு இல்லை என்று நம்புவது.",
                        "உண்மை: அமல்படுத்த முடியாதது என்றால் கடமை செய்யாததற்கு நேரடி நீதிமன்ற பேராணை இல்லை என்று பொருள். இருப்பினும், கடமைகள் சட்ட விளக்கத்திலும் உறுப்பு 19-ன் கீழ் 'நியாயத் தன்மையை' மதிப்பிடுவதிலும் நீதிமன்றங்களுக்கு வழிகாட்டுகின்றன, மேலும் நாடாளுமன்றம் அவற்றை அமல்படுத்தச் சட்டங்களை இயற்றியுள்ளது."
                    ]
                }
            },
            {
                "title": "5. Applicable Scope Trap: Citizens vs All Persons (பொருந்தும் எல்லைப் பொறி: குடிமக்கள் vs அனைத்து நபர்கள்)",
                "points": {
                    "en": [
                        "TRAP: Claiming Fundamental Duties apply to all persons including foreign tourists in India.",
                        "FACT: Article 51A duties apply EXCLUSIVELY to Citizens of India. Foreigners are not bound by Article 51A."
                    ],
                    "ta": [
                        "பொறி: இந்தியாவில் உள்ள வெளிநாட்டு சுற்றுலாப் பயணிகள் உட்பட அனைத்து நபர்களுக்கும் அடிப்படை கடமைகள் பொருந்தும் என்ற கோரிக்கை.",
                        "உண்மை: உறுப்பு 51A கடமைகள் இந்தியக் குடிமக்களுக்கு மட்டுமே பொருந்தும். வெளிநாட்டினருக்கு உறுப்பு 51A பொருந்தாது."
                    ]
                }
            },
            {
                "title": "6. Thematic Grouping Constitutional Status Trap (தலைப்பு வாரிய வகைப்பாட்டின் அரசியலமைப்பு அந்தஸ்து பொறி)",
                "points": {
                    "en": [
                        "TRAP: Statement asserting that the Constitution of India categorizes Fundamental Duties into 6 thematic groups.",
                        "FACT: The division into thematic groups (Loyalty, Culture, Science, etc.) is a conventional academic study classification, NOT explicitly written in the Constitution text!"
                    ],
                    "ta": [
                        "பொறி: இந்திய அரசியலமைப்பு அடிப்படை கடமைகளை 6 தலைப்பு வாரியாக வகைப்படுத்துகிறது என்று கூறும் கூற்று.",
                        "உண்மை: தலைப்பு வாரியப் பிரிவுகள் (விசுவாசம், பண்பாடு, அறிவியல் போன்றவை) ஒரு மரபுவழி கல்விப் படிப்பு வகைபாடே தவிர, அரசியலமைப்பு உரையில் வெளிப்படையாக எழுதப்படவில்லை!"
                    ]
                }
            }
        ],
        "important_facts": {
            "en": [
                "Article 51A(k) was added by the 86th Constitutional Amendment Act, 2002 for children aged 6 to 14 years.",
                "Article 21A (FR) = State duty for 6-14 yrs | Article 45 (DPSP) = State directive below 6 yrs | Article 51A(k) (FD) = Parent duty for 6-14 yrs.",
                "There are currently EXACTLY 11 Fundamental Duties in Article 51A (Part IVA).",
                "Original 1950 Constitution contained ZERO Fundamental Duties.",
                "42nd Amendment Act 1976 added Part IVA & Article 51A with 10 original duties.",
                "Swaran Singh Committee recommended 8 duties; duty to pay taxes and penalties for non-performance were REJECTED by Parliament.",
                "Fundamental Duties were borrowed from the USSR (Soviet Union) Constitution.",
                "Fundamental Duties apply EXCLUSIVELY to Citizens of India (not foreigners).",
                "Fundamental Duties are non-justiciable by themselves but legally relevant in statutory interpretation and Article 19 reasonableness tests.",
                "Environment Protection Act 1986, Wildlife Act 1972, Flag Code 2002, and UAPA 1967 provide statutory backing for Fundamental Duties.",
                "Minerva Mills (1980) & AIIMS Students Union (2002) established harmonious balance between FRs, DPSP, and Fundamental Duties."
            ],
            "ta": [
                "உறுப்பு 51A(k) 6 முதல் 14 வயது வரையிலான குழந்தைகளுக்காக 2002-ன் 86வது அரசியலமைப்பு திருத்தச் சட்டத்தால் சேர்க்கப்பட்டது.",
                "உறுப்பு 21A (FR) = 6-14 வயதினருக்கு அரசு கடமை | உறுப்பு 45 (DPSP) = 6 வயதிற்குட்பட்டோருக்கு அரசு பராமரிப்பு | உறுப்பு 51A(k) (FD) = 6-14 வயதினருக்குப் பெற்றோர் கடமை.",
                "தற்போது உறுப்பு 51A-ல் (பகுதி IVA) சரியாக 11 அடிப்படை கடமைகள் உள்ளன.",
                "அசல் 1950 அரசியலமைப்பில் அடிப்படை கடமைகள் ஏதும் இல்லை.",
                "42வது திருத்தச் சட்டம் 1976 பகுதி IVA & உறுப்பு 51A உடன் அசல் 10 கடமைகளைச் சேர்த்தது.",
                "ஸ்வரன் சிங் குழு 8 கடமைகளைப் பரிந்துரைத்தது; வரி செலுத்தும் கடமை மற்றும் அபராதங்கள் நாடாளுமன்றத்தால் நிராகரிக்கப்பட்டன.",
                "அடிப்படை கடமைகள் முன்னாள் சோவியத் யூனியன் (USSR) அரசியலமைப்பிலிருந்து பெறப்பட்டவை.",
                "அடிப்படை கடமைகள் இந்தியக் குடிமக்களுக்கு மட்டுமே பொருந்தும் (வெளிநாட்டினருக்கு அல்ல).",
                "அடிப்படை கடமைகள் நேரடியாக அமல்படுத்த முடியாதவை, ஆனால் சட்ட விளக்கம் மற்றும் உறுப்பு 19 நியாயத் தன்மையை மதிப்பிடுவதில் சட்டப்பூர்வமாகத் தொடர்புடையவை.",
                "சுற்றுச்சூழல் பாதுகாப்புச் சட்டம் 1986, வனவிலங்கு சட்டம் 1972, கொடி குறியீடு 2002 மற்றும் UAPA 1967 ஆகியவை அடிப்படை கடமைகளுக்குச் சட்டப்பூர்வ ஆதரவை வழங்குகின்றன.",
                "மினர்வா மில்ஸ் (1980) & AIIMS மாணவர் சங்கம் (2002) FRs, DPSP மற்றும் அடிப்படை கடமைகள் இடையே இணக்கமான சமநிலையை நிறுவின."
            ]
        },
        "quick_revision": {
            "en": [
                "Part IVA & Article 51A: Added by 42nd CAA 1976 (10 duties) & expanded by 86th CAA 2002 (11th duty Art 51A(k)).",
                "Article 51A(k): Parent/guardian duty to provide education opportunities to child/ward aged 6 to 14 years.",
                "Education Trio: Art 21A (FR - State duty 6-14 yrs) | Art 45 (DPSP - State care <6 yrs) | Art 51A(k) (FD - Parent duty 6-14 yrs).",
                "Environment Trio: Art 21 (FR - Clean Env Right) | Art 48A (DPSP - State Env Duty) | Art 51A(g) (FD - Citizen Env Duty).",
                "Swaran Singh Committee: Recommended 8 duties; Tax duty & Penalties REJECTED by Parliament.",
                "Nature: Non-justiciable by themselves; apply ONLY to Citizens; supported by parliamentary statutes (Flag Code, UAPA, Wildlife Act).",
                "All 11 Duties Matrix: 51A(a) Flag/Anthem | 51A(b) Freedom Ideals | 51A(c) Sovereignty | 51A(d) Defence | 51A(e) Brotherhood/Women | 51A(f) Composite Culture | 51A(g) Environment | 51A(h) Science | 51A(i) Public Property | 51A(j) Excellence | 51A(k) Child Education.",
                "Key Cases: Bijoe Emmanuel 1986 (Anthem respect), MC Mehta 1997 (Taj Trapezium), AIIMS 2002 (Duty importance), Nagaraja 2014 (Animal welfare)."
            ],
            "ta": [
                "பகுதி IVA & உறுப்பு 51A: 42வது திருத்தம் 1976 (10 கடமைகள்) மூலம் சேர்க்கப்பட்டு 86வது திருத்தம் 2002 (11வது கடமை உறுப்பு 51A(k)) மூலம் விரிவாக்கப்பட்டது.",
                "உறுப்பு 51A(k): 6 முதல் 14 வயது வரையிலான குழந்தைக்குக் கல்வி வாய்ப்புகளை வழங்கும் பெற்றோர்/பாதுகாவலர் கடமை.",
                "கல்வி முக்கோணம்: உறுப்பு 21A (FR - 6-14 வயது அரசு கடமை) | உறுப்பு 45 (DPSP - <6 வயது அரசு பராமரிப்பு) | உறுப்பு 51A(k) (FD - 6-14 வயது பெற்றோர் கடமை).",
                "சுற்றுச்சூழல் முக்கோணம்: உறுப்பு 21 (FR - தூய்மை சுற்றுச்சூழல் உரிமை) | உறுப்பு 48A (DPSP - அரசு சுற்றுச்சூழல் கடமை) | உறுப்பு 51A(g) (FD - குடிமகன் சுற்றுச்சூழல் கடமை).",
                "ஸ்வரன் சிங் குழு: 8 கடமைகளைப் பரிந்துரைத்தது; வரி செலுத்தும் கடமை & அபராதங்கள் நாடாளுமன்றத்தால் நிராகரிக்கப்பட்டன.",
                "இயல்பு: நேரடியாக அமல்படுத்த முடியாதவை; குடிமக்களுக்கு மட்டுமே பொருந்தும்; நாடாளுமன்றச் சட்டங்களால் ஆதரிக்கப்படுகின்றன (கொடி குறியீடு, UAPA, வனவிலங்கு சட்டம்).",
                "அனைத்து 11 கடமைகள் அணி: 51A(a) கொடி/கீதம் | 51A(b) சுதந்திர லட்சியங்கள் | 51A(c) இறையாண்மை | 51A(d) பாதுகாப்பு | 51A(e) சகோதரத்துவம்/பெண்கள் | 51A(f) கூட்டுப் பண்பாடு | 51A(g) சுற்றுச்சூழல் | 51A(h) அறிவியல் | 51A(i) பொதுச் சொத்து | 51A(j) சிறப்பு | 51A(k) குழந்தைகள் கல்வி.",
                "முக்கிய வழக்குகள்: பிஜோய் இம்மானுவேல் 1986 (கீத மரியாதை), எம்.சி. மேத்தா 1997 (தாஜ் ட்ரேபீசியம்), AIIMS 2002 (கடமை முக்கியத்துவம்), நாகராஜா 2014 (விலங்கு நலன்)."
            ]
        },
        "revision_cards": [
            {
                "id": "card_p3_1",
                "front_en": "What is the 11th Fundamental Duty added by the 86th Amendment in 2002?",
                "front_ta": "2002-ல் 86வது திருத்தத்தால் சேர்க்கப்பட்ட 11வது அடிப்படை கடமை எது?",
                "back_en": "Article 51A(k) - Duty of parent/guardian to provide education opportunities to child/ward aged 6 to 14 years.",
                "back_ta": "உறுப்பு 51A(k) - 6 முதல் 14 வயது வரையிலான தனது குழந்தைக்குக் கல்வி வாய்ப்புகளை வழங்கும் பெற்றோர்/பாதுகாவலர் கடமை."
            },
            {
                "id": "card_p3_2",
                "front_en": "What is the exact distinction between Article 21A, Article 45, and Article 51A(k)?",
                "front_ta": "உறுப்பு 21A, உறுப்பு 45 மற்றும் உறுப்பு 51A(k) இடையே உள்ள சரியான வேறுபாடு என்ன?",
                "back_en": "Art 21A (FR) = STATE duty for 6-14 yrs | Art 45 (DPSP) = STATE care below 6 yrs | Art 51A(k) (FD) = PARENT duty for 6-14 yrs.",
                "back_ta": "உறுப்பு 21A (FR) = 6-14 வயதினருக்கு அரசு கடமை | உறுப்பு 45 (DPSP) = <6 வயதினருக்கு அரசு பராமரிப்பு | உறுப்பு 51A(k) (FD) = 6-14 வயதினருக்குப் பெற்றோர் கடமை."
            },
            {
                "id": "card_p3_3",
                "front_en": "How many Fundamental Duties were in the original 1950 Constitution vs after 42nd CAA vs present?",
                "front_ta": "அசல் 1950 அரசியலமைப்பு vs 42வது திருத்தம் vs தற்போதைய கடமைகளின் எண்ணிக்கை என்ன?",
                "back_en": "1950 = ZERO | 42nd CAA (1976) = 10 duties | Present (86th CAA 2002) = 11 duties.",
                "back_ta": "1950 = 0 கடமைகள் | 42வது திருத்தம் (1976) = 10 கடமைகள் | தற்போதைய (86வது திருத்தம் 2002) = 11 கடமைகள்."
            },
            {
                "id": "card_p3_4",
                "front_en": "Were Swaran Singh Committee's recommendations on 'Duty to pay taxes' accepted?",
                "front_ta": "'வரி செலுத்தும் கடமை' பற்றிய ஸ்வரன் சிங் குழுவின் பரிந்துரைகள் ஏற்றுக்கொள்ளப்பட்டவா?",
                "back_en": "NO. Parliament REJECTED 'Duty to Pay Taxes' and 'Penalties for non-compliance'. They are NOT in Article 51A.",
                "back_ta": "இல்லை. நாடாளுமன்றம் 'வரி செலுத்தும் கடமை' மற்றும் 'கடமை மீறலுக்கான அபராதங்களை' நிராகரித்தது. அவை உறுப்பு 51A-ல் இல்லை."
            },
            {
                "id": "card_p3_5",
                "front_en": "What is the difference between Article 48A and Article 51A(g)?",
                "front_ta": "உறுப்பு 48A மற்றும் உறுப்பு 51A(g) இடையே உள்ள வேறுபாடு என்ன?",
                "back_en": "Article 48A is a DPSP for the STATE; Article 51A(g) is a Fundamental Duty for CITIZENS.",
                "back_ta": "உறுப்பு 48A என்பது அரசுக்கான DPSP; உறுப்பு 51A(g) என்பது குடிமக்களுக்கான அடிப்படை கடமை."
            },
            {
                "id": "card_p3_6",
                "front_en": "Do Fundamental Duties apply to foreign citizens in India?",
                "front_ta": "இந்தியாவில் உள்ள வெளிநாட்டு மக்களுக்கு அடிப்படை கடமைகள் பொருந்துமா?",
                "back_en": "NO. Fundamental Duties apply EXCLUSIVELY to Citizens of India.",
                "back_ta": "இல்லை. அடிப்படை கடமைகள் இந்தியக் குடிமக்களுக்கு மட்டுமே பொருந்தும்."
            },
            {
                "id": "card_p3_7",
                "front_en": "What are the 6 thematic groups of Fundamental Duties?",
                "front_ta": "அடிப்படை கடமைகளின் 6 தலைப்பு வாரிக் குழுக்கள் யாவை?",
                "back_en": "1. Loyalty (a,c,d), 2. Integration (b,e), 3. Culture/Env (f,g), 4. Rational/Civic (h,i), 5. Excellence (j), 6. Education (k).",
                "back_ta": "1. விசுவாசம் (a,c,d), 2. ஒருமைப்பாடு (b,e), 3. பண்பாடு/சுற்றுச்சூழல் (f,g), 4. பகுத்தறிவு/குடிமை (h,i), 5. சிறப்பு (j), 6. கல்வி (k)."
            },
            {
                "id": "card_p3_8",
                "front_en": "What was held in AIIMS Students Union v. AIIMS (2002)?",
                "front_ta": "AIIMS மாணவர் சங்கம் vs AIIMS (2002) வழக்கில் வழங்கப்பட்ட தீர்ப்பு என்ன?",
                "back_en": "Fundamental Duties are equally important as Fundamental Rights and must be considered in statutory interpretation.",
                "back_ta": "அடிப்படை கடமைகள் அடிப்படை உரிமைகளுக்குச் சமமான முக்கியத்துவம் வாய்ந்தவை, சட்ட விளக்கத்தின் போது அவற்றைப் புறக்கணிக்க முடியாது."
            }
        ]
    }
}

target_file = "data/notes/polity/fundamental_duties_part_3.json"
os.makedirs(os.path.dirname(target_file), exist_ok=True)

with open(target_file, "w", encoding="utf-8") as f:
    json.dump(notes_data, f, ensure_ascii=False, indent=2)

print(f"Successfully generated {target_file}")
